# PspInitializeNetRateControl

- RVA: `0x00C466DC`–`0x00C4674B` (길이 `111` bytes)
- VA: `0x0000000140C466DC`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE5B4`
- 디코드: `29`개 명령, `111/111` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C46725` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (function, `0x007D06CC`)

### Direct callers
- [PspInitPhase1](PspInitPhase1_function_00C453B8.md) at `0x00C453F2`

### Static image references
- `0x00C4670C` → RVA `0x00F065A0` (`.data`; read)
- `0x00C4672E` → RVA `0x00F065A0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C46725` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C466DC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C466E1  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00C466E6  55                              push rbp
00C466E7  48 8B EC                        mov rbp, rsp
00C466EA  48 83 EC 60                     sub rsp, 0x60
00C466EE  33 FF                           xor edi, edi
00C466F0  48 C7 45 D0 04 00 01 00         mov qword ptr [rbp - 0x30], 0x10004
00C466F8  48 8D 45 C0                     lea rax, [rbp - 0x40]
00C466FC  48 C7 45 E0 01 00 00 00         mov qword ptr [rbp - 0x20], 1
00C46704  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C46708  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
00C4670C  48 8D 0D 8D FE 2B 00            lea rcx, [rip + 0x2bfe8d]
00C46713  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00C46717  8D 5F 01                        lea ebx, [rdi + 1]
00C4671A  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
00C4671E  89 5D C0                        mov dword ptr [rbp - 0x40], ebx
00C46721  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
00C46725  E8 A2 9F B8 FF                  call 0x1407d06cc
00C4672A  85 C0                           test eax, eax
00C4672C  79 0A                           jns 0x140c46738
00C4672E  48 89 3D 6B FE 2B 00            mov qword ptr [rip + 0x2bfe6b], rdi
00C46735  40 8A DF                        mov bl, dil
00C46738  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00C4673D  8A C3                           mov al, bl
00C4673F  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00C46744  48 83 C4 60                     add rsp, 0x60
00C46748  5D                              pop rbp
00C46749  C3                              ret
00C4674A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInitializeNetRateControl(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (96);
    v_rdi = 0;
    v_stack_m38 = 0x10004ULL;
    v_stack_m28 = 1;
    v_stack_m40 = 0;
    v_stack_m30 = v_stack_m48;
    v_stack_m20 = 0;
    v_stack_m48 = (unsigned int)(v_rdi + 1);
    v_stack_m18 = 0;
    result = ExRegisterHost(v_rip + 2883213, a2, v_stack_m38, a4);
    v_rbx = v_rdi + 1;
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 2883179) = 0;
        v_rbx = 0;
    }
    v_rsp = (v_rsp) + (96);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void PspInitializeNetRateControl(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (96);
    local_rdi = 0;
    v_stack_m38 = 0x10004ULL;
    v_stack_m28 = 1;
    v_stack_m40 = 0;
    v_stack_m30 = v_stack_m48;
    v_stack_m20 = 0;
    v_stack_m48 = (uint32_t)(local_rdi + 1);
    v_stack_m18 = 0;
    result = ExRegisterHost(v_rip + 2883213, a2, v_stack_m38, a4);
    local_rbx = local_rdi + 1;
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x2BFE6B) = 0;
        local_rbx = 0;
    }
    local_rsp = (local_rsp) + (96);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C466DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C466DC[BB_00C466DC]
  bb_00C4672E[BB_00C4672E]
  bb_00C46738[BB_00C46738]
  bb_00C4674A[BB_00C4674A]
  bb_00C466DC -->|branch| bb_00C46738
  bb_00C466DC -->|fallthrough| bb_00C4672E
  bb_00C4672E -->|flow| bb_00C46738
```
