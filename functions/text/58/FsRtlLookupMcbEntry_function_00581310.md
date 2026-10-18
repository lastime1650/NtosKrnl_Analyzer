# FsRtlLookupMcbEntry

- RVA: `0x00581310`–`0x0058138C` (길이 `124` bytes)
- VA: `0x0000000140581310`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F83C`
- 디코드: `38`개 명령, `124/124` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0058135A` → [FsRtlLookupLargeMcbEntry](../40/FsRtlLookupLargeMcbEntry_function_0040A540.md) (function, `0x0040A540`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00581310  4C 8B DC                        mov r11, rsp
00581313  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00581317  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
0058131B  57                              push rdi
0058131C  48 83 EC 50                     sub rsp, 0x50
00581320  33 F6                           xor esi, esi
00581322  8B D2                           mov edx, edx
00581324  49 8B C1                        mov rax, r9
00581327  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
0058132B  48 F7 D8                        neg rax
0058132E  49 89 73 E8                     mov qword ptr [r11 - 0x18], rsi
00581332  49 8B D9                        mov rbx, r9
00581335  49 8D 43 E8                     lea rax, [r11 - 0x18]
00581339  4D 1B C9                        sbb r9, r9
0058133C  49 8B F8                        mov rdi, r8
0058133F  4C 23 C8                        and r9, rax
00581342  4D 8D 43 20                     lea r8, [r11 + 0x20]
00581346  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0058134E  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00581352  49 89 73 D0                     mov qword ptr [r11 - 0x30], rsi
00581356  49 89 73 C8                     mov qword ptr [r11 - 0x38], rsi
0058135A  E8 E1 91 E8 FF                  call 0x14040a540
0058135F  84 C0                           test al, al
00581361  74 18                           je 0x14058137b
00581363  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00581368  83 F9 FF                        cmp ecx, -1
0058136B  0F 44 CE                        cmove ecx, esi
0058136E  89 0F                           mov dword ptr [rdi], ecx
00581370  48 85 DB                        test rbx, rbx
00581373  74 06                           je 0x14058137b
00581375  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00581379  89 0B                           mov dword ptr [rbx], ecx
0058137B  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00581380  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00581385  48 83 C4 50                     add rsp, 0x50
00581389  5F                              pop rdi
0058138A  C3                              ret
0058138B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlLookupMcbEntry(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (80);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp + 32) = 0;
    result = -(a4);
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    a4 = (a4) & (v_rsp - 24);
    *(unsigned __int64 *)(v_rsp - 40) = a5;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    result = FsRtlLookupLargeMcbEntry(a1, (unsigned int)(a2), v_rsp + 32, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0058137B;
    a1 = v_stack_p20;
    if (((unsigned int)(v_stack_p20)) == -1) { a1 = 0; }
    *(unsigned int *)(a3) = (unsigned int)(a1);
    if (a4 != 0) {
        a1 = v_stack_m18;
        *(unsigned int *)(a4) = (unsigned int)(a1);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlLookupMcbEntry(int64_t Arg1, int32_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (80);
    local_rsi = 0;
    *(uint64_t *)(local_rsp + 0x20) = 0;
    result = -(Arg4);
    *(uint64_t *)(local_rsp - 0x18) = 0;
    Arg4 = (Arg4) & (local_rsp - 24);
    *(uint64_t *)(local_rsp - 0x28) = Arg5;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    result = FsRtlLookupLargeMcbEntry(Arg1, (uint32_t)(Arg2), local_rsp + 32, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0058137B;
    Arg1 = v_stack_p20;
    if (((uint32_t)(v_stack_p20)) == -1) { Arg1 = 0; }
    *(uint32_t *)(arg3) = (uint32_t)(Arg1);
    if (Arg4 != 0) {
        Arg1 = v_stack_m18;
        *(uint32_t *)(Arg4) = (uint32_t)(Arg1);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00581310[BB_00581310]
  bb_00581363[BB_00581363]
  bb_00581375[BB_00581375]
  bb_0058137B[BB_0058137B]
  bb_0058138B[BB_0058138B]
  bb_00581310 -->|branch| bb_0058137B
  bb_00581310 -->|fallthrough| bb_00581363
  bb_00581363 -->|branch| bb_0058137B
  bb_00581363 -->|fallthrough| bb_00581375
  bb_00581375 -->|flow| bb_0058137B
```
