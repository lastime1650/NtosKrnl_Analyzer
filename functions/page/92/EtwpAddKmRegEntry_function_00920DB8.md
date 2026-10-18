# EtwpAddKmRegEntry

- RVA: `0x00920DB8`–`0x00920E44` (길이 `140` bytes)
- VA: `0x0000000140920DB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008CF6C`
- 디코드: `41`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00920DEA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00920E11` → [EtwpInitializeRegEntry](../8C/EtwpInitializeRegEntry_function_008C1A78.md) (function, `0x008C1A78`)

### Direct callers
- [EtwpRegisterKMProvider](EtwpRegisterKMProvider_function_009209A4.md) at `0x00920BE1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00920DEA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00920DB8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00920DBD  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00920DC2  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00920DC7  57                              push rdi
00920DC8  41 56                           push r14
00920DCA  41 57                           push r15
00920DCC  48 83 EC 40                     sub rsp, 0x40
00920DD0  33 DB                           xor ebx, ebx
00920DD2  49 8B E8                        mov rbp, r8
00920DD5  44 8B F2                        mov r14d, edx
00920DD8  4C 8B F9                        mov r15, rcx
00920DDB  41 B8 45 74 77 52               mov r8d, 0x52777445
00920DE1  49 8B F1                        mov rsi, r9
00920DE4  8D 53 78                        lea edx, [rbx + 0x78]
00920DE7  8D 4B 40                        lea ecx, [rbx + 0x40]
00920DEA  E8 01 13 26 00                  call 0x140b820f0
00920DEF  48 8B F8                        mov rdi, rax
00920DF2  48 85 C0                        test rax, rax
00920DF5  74 46                           je 0x140920e3d
00920DF7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00920DFC  4C 8B CD                        mov r9, rbp
00920DFF  66 89 5C 24 28                  mov word ptr [rsp + 0x28], bx
00920E04  45 8B C6                        mov r8d, r14d
00920E07  33 D2                           xor edx, edx
00920E09  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00920E0E  49 8B CF                        mov rcx, r15
00920E11  E8 62 0C FA FF                  call 0x1408c1a78
00920E16  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00920E1E  48 89 38                        mov qword ptr [rax], rdi
00920E21  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00920E26  8B C3                           mov eax, ebx
00920E28  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00920E2D  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00920E32  48 83 C4 40                     add rsp, 0x40
00920E36  41 5F                           pop r15
00920E38  41 5E                           pop r14
00920E3A  5F                              pop rdi
00920E3B  C3                              ret
00920E3C  CC                              int3
00920E3D  BB 17 00 00 C0                  mov ebx, 0xc0000017
00920E42  EB DD                           jmp 0x140920e21
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpAddKmRegEntry(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int16 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    v_rbx = 0;
    result = ExAllocatePool2(v_rbx + 64, v_rbx + 120, (unsigned int)(0x52777445ULL), a4);
    if (result == 0) goto loc_00920E3D;
    v_stack_m28 = result;
    v_stack_m30 = 0;
    a2 = 0;
    v_stack_m38 = a4;
    result = EtwpInitializeRegEntry(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a2))), a3);
    *(unsigned __int64 *)(a5) = result;
loc_00920E21:
    v_rsp = (v_rsp) + (64);
    return 0;
loc_00920E3D:
    goto loc_00920E21;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpAddKmRegEntry(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint16_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    local_rbx = 0;
    result = ExAllocatePool2(local_rbx + 64, local_rbx + 120, (uint32_t)(0x52777445ULL), Arg4);
    if (result == 0) goto loc_00920E3D;
    v_stack_m28 = result;
    v_stack_m30 = 0;
    Arg2 = 0;
    v_stack_m38 = Arg4;
    result = EtwpInitializeRegEntry(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3);
    *(uint64_t *)(arg5) = result;
loc_00920E21:
    local_rsp = (local_rsp) + (64);
    return 0;
loc_00920E3D:
    goto loc_00920E21;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00920DB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00920DB8[BB_00920DB8]
  bb_00920DF7[BB_00920DF7]
  bb_00920E21[BB_00920E21]
  bb_00920E3C[BB_00920E3C]
  bb_00920E3D[BB_00920E3D]
  bb_00920DB8 -->|branch| bb_00920E3D
  bb_00920DB8 -->|fallthrough| bb_00920DF7
  bb_00920DF7 -->|flow| bb_00920E21
  bb_00920E3C -->|flow| bb_00920E3D
  bb_00920E3D -->|branch| bb_00920E21
```
