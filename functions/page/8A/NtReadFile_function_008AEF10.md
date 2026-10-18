# NtReadFile

- RVA: `0x008AEF10`–`0x008AEFE2` (길이 `210` bytes)
- VA: `0x00000001408AEF10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FA5C`
- 디코드: `46`개 명령, `210/210` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008AEF55` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008AEFC3` → [IopReadFile](IopReadFile_function_008AEFF0.md) (function, `0x008AEFF0`)

### Direct callers
- [SmKmIssueFileIo](../../text/60/SmKmIssueFileIo_function_0060F2F4.md) at `0x0060F341`
- [PfSnGetPrefetchInstructions](PfSnGetPrefetchInstructions_function_008AEBE4.md) at `0x008AEDFC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008AEF55` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AEF10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008AEF15  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
008AEF1A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008AEF1F  57                              push rdi
008AEF20  48 81 EC 80 00 00 00            sub rsp, 0x80
008AEF27  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AEF30  33 ED                           xor ebp, ebp
008AEF32  49 8B F9                        mov rdi, r9
008AEF35  48 89 6C 24 70                  mov qword ptr [rsp + 0x70], rbp
008AEF3A  49 8B F0                        mov rsi, r8
008AEF3D  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
008AEF42  48 8B DA                        mov rbx, rdx
008AEF45  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
008AEF4A  44 0F B6 80 32 02 00 00         movzx r8d, byte ptr [rax + 0x232]
008AEF52  8D 55 01                        lea edx, [rbp + 1]
008AEF55  E8 D6 E5 9E FF                  call 0x14029d530
008AEF5A  85 C0                           test eax, eax
008AEF5C  78 6A                           js 0x1408aefc8
008AEF5E  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008AEF66  4C 8B CF                        mov r9, rdi
008AEF69  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008AEF6E  4C 8B C6                        mov r8, rsi
008AEF71  48 89 6C 24 68                  mov qword ptr [rsp + 0x68], rbp
008AEF76  48 8B D3                        mov rdx, rbx
008AEF79  48 89 6C 24 60                  mov qword ptr [rsp + 0x60], rbp
008AEF7E  89 6C 24 58                     mov dword ptr [rsp + 0x58], ebp
008AEF82  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
008AEF87  48 89 6C 24 48                  mov qword ptr [rsp + 0x48], rbp
008AEF8C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008AEF91  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
008AEF99  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008AEF9E  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
008AEFA5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008AEFA9  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
008AEFB1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008AEFB6  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008AEFBE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008AEFC3  E8 28 00 00 00                  call 0x1408aeff0
008AEFC8  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
008AEFD0  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
008AEFD4  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
008AEFD8  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
008AEFDC  49 8B E3                        mov rsp, r11
008AEFDF  5F                              pop rdi
008AEFE0  C3                              ret
008AEFE1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtReadFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (128);
    v_rbp = 0;
    v_stack_m18 = 0;
    v_stack_m68 = 0;
    result = IopReferenceFileObject(a1, v_rbp + 1, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_stack_m18);
    if (!(sign_flag)) {
        result = a9;
        a4 = a4;
        a1 = v_stack_m18;
        a3 = a3;
        v_stack_m20 = 0;
        a2 = a2;
        v_stack_m28 = 0;
        v_stack_m30 = 0;
        v_stack_m38 = 0;
        v_stack_m40 = 0;
        v_stack_m48 = result;
        result = a8;
        v_stack_m50 = result;
        result = a7;
        v_stack_m58 = (unsigned int)(result);
        result = a6;
        v_stack_m60 = result;
        result = a5;
        v_stack_m68 = result;
        result = IopReadFile(a1, a2, a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtReadFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (128);
    local_rbp = 0;
    v_stack_m18 = 0;
    v_stack_m68 = 0;
    result = IopReferenceFileObject(Arg1, local_rbp + 1, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_stack_m18);
    if (!(sign_flag)) {
        result = Arg9;
        Arg4 = Arg4;
        Arg1 = v_stack_m18;
        Arg3 = Arg3;
        v_stack_m20 = 0;
        Arg2 = Arg2;
        v_stack_m28 = 0;
        v_stack_m30 = 0;
        v_stack_m38 = 0;
        v_stack_m40 = 0;
        v_stack_m48 = result;
        result = Arg8;
        v_stack_m50 = result;
        result = Arg7;
        v_stack_m58 = (uint32_t)(result);
        result = Arg6;
        v_stack_m60 = result;
        result = Arg5;
        v_stack_m68 = result;
        result = IopReadFile(Arg1, Arg2, Arg3, Arg4);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AEF10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008AEF10[BB_008AEF10]
  bb_008AEF5E[BB_008AEF5E]
  bb_008AEFC8[BB_008AEFC8]
  bb_008AEFE1[BB_008AEFE1]
  bb_008AEF10 -->|branch| bb_008AEFC8
  bb_008AEF10 -->|fallthrough| bb_008AEF5E
  bb_008AEF5E -->|flow| bb_008AEFC8
```
