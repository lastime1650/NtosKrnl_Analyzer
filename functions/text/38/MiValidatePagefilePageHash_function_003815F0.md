# MiValidatePagefilePageHash

- RVA: `0x003815F0`–`0x0038167C` (길이 `140` bytes)
- VA: `0x00000001403815F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B98C`
- 디코드: `34`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiWaitForInPageComplete](MiWaitForInPageComplete_function_00380AB8.md) at `0x00380D4C`
- [MiReadPagefilePage](../66/MiReadPagefilePage_function_0066F78C.md) at `0x0066FA07`

### Static image references
- `0x00381602` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00381676` → [sub_0038184F](Unknown_function_0038184F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003815F0  4C 8B DC                        mov r11, rsp
003815F3  56                              push rsi
003815F4  57                              push rdi
003815F5  41 54                           push r12
003815F7  41 55                           push r13
003815F9  41 57                           push r15
003815FB  48 81 EC 50 01 00 00            sub rsp, 0x150
00381602  48 8B 05 37 91 A8 00            mov rax, qword ptr [rip + 0xa89137]
00381609  48 33 C4                        xor rax, rsp
0038160C  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
00381614  48 8B 81 00 01 00 00            mov rax, qword ptr [rcx + 0x100]
0038161B  48 8D 91 10 01 00 00            lea rdx, [rcx + 0x110]
00381622  4C 8B C9                        mov r9, rcx
00381625  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0038162A  45 33 C0                        xor r8d, r8d
0038162D  48 85 C0                        test rax, rax
00381630  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
00381635  48 0F 45 D0                     cmovne rdx, rax
00381639  49 8B 41 58                     mov rax, qword ptr [r9 + 0x58]
0038163D  48 05 FF 0F 00 00               add rax, 0xfff
00381643  33 F6                           xor esi, esi
00381645  45 33 E4                        xor r12d, r12d
00381648  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
0038164C  8B 4A 2C                        mov ecx, dword ptr [rdx + 0x2c]
0038164F  4C 8D 6A 30                     lea r13, [rdx + 0x30]
00381653  48 03 4A 20                     add rcx, qword ptr [rdx + 0x20]
00381657  48 8D 7A 30                     lea rdi, [rdx + 0x30]
0038165B  81 E1 FF 0F 00 00               and ecx, 0xfff
00381661  48 03 C8                        add rcx, rax
00381664  48 C1 E9 0C                     shr rcx, 0xc
00381668  4C 8D 3C CD 00 00 00 00         lea r15, [rcx*8]
00381670  4D 03 EF                        add r13, r15
00381673  49 3B FD                        cmp rdi, r13
00381676  0F 83 D3 01 00 00               jae 0x14038184f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiValidatePagefilePageHash(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 11047223)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m148 = a1;
    a3 = 0;
    v_stack_m158 = 0;
    a2 = a1 + 272;
    if (*(unsigned __int64 *)(a1 + 256) != 0) { a2 = *(unsigned __int64 *)(a1 + 256); }
    result = (*(unsigned __int64 *)(a1 + 88)) + (0xFFFULL);
    v_rsi = 0;
    v_r12 = 0;
    v_stack_m150 = 0;
    a1 = ((unsigned int)(*(unsigned int *)(a2 + 44))) + (*(unsigned __int64 *)(a2 + 32));
    a1 = (unsigned int)((a1) & (0xFFFULL));
    a1 = (a1) + (result);
    a1 = (a1) >> (12);
    v_r13 = (a2 + 48) + (a1 * 8);
}
```

## 5. (Beta) C Style

```c
int64_t MiValidatePagefilePageHash(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0xA89137)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m148 = Arg1;
    Arg3 = 0;
    v_stack_m158 = 0;
    Arg2 = Arg1 + 272;
    if (*(uint64_t *)(arg1 + 0x100) != 0) { Arg2 = *(uint64_t *)(arg1 + 0x100); }
    result = (*(uint64_t *)(arg1 + 0x58)) + (0xFFFULL);
    local_rsi = 0;
    local_r12 = 0;
    v_stack_m150 = 0;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg2 + 0x2C))) + (*(uint64_t *)(Arg2 + 0x20));
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    Arg1 = (Arg1) + (result);
    Arg1 = (Arg1) >> (12);
    local_r13 = (Arg2 + 48) + (Arg1 * 8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x110` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003815F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003815F0[BB_003815F0]
```
