# RtlUnicodeToOemN

- RVA: `0x0090F2B0`–`0x0090F325` (길이 `117` bytes)
- VA: `0x000000014090F2B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000898D0`
- 디코드: `32`개 명령, `117/117` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0090F2D1` → [RtlpIsUtf8Process](RtlpIsUtf8Process_function_0090DB60.md) (function, `0x0090DB60`)
- `0x0090F2DF` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0090F301` → [RtlUnicodeToCustomCPN](RtlUnicodeToCustomCPN_function_0090E6F0.md) (function, `0x0090E6F0`)

### Direct callers
- [RtlUnicodeStringToCountedOemString](RtlUnicodeStringToCountedOemString_function_0090F1A0.md) at `0x0090F236`
- [RtlUnicodeStringToOemString](../AC/RtlUnicodeStringToOemString_function_00AC1C10.md) at `0x00AC1CAE`

### Static image references
- `0x0090F31C` → RVA `0x00FD8720` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0090F2DF` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0090F2B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0090F2B5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0090F2BA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0090F2BF  57                              push rdi
0090F2C0  48 83 EC 30                     sub rsp, 0x30
0090F2C4  48 8B E9                        mov rbp, rcx
0090F2C7  49 8B D9                        mov rbx, r9
0090F2CA  33 C9                           xor ecx, ecx
0090F2CC  49 8B F8                        mov rdi, r8
0090F2CF  8B F2                           mov esi, edx
0090F2D1  E8 8A E8 FF FF                  call 0x14090db60
0090F2D6  84 C0                           test al, al
0090F2D8  75 42                           jne 0x14090f31c
0090F2DA  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0090F2DF  E8 0C EF 9E FF                  call 0x1402fe1f0
0090F2E4  48 8D 88 08 04 00 00            lea rcx, [rax + 0x408]
0090F2EB  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0090F2EF  4C 8B CF                        mov r9, rdi
0090F2F2  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0090F2F6  44 8B C6                        mov r8d, esi
0090F2F9  48 8B D5                        mov rdx, rbp
0090F2FC  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0090F301  E8 EA F3 FF FF                  call 0x14090e6f0
0090F306  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0090F30B  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0090F310  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0090F315  48 83 C4 30                     add rsp, 0x30
0090F319  5F                              pop rdi
0090F31A  C3                              ret
0090F31B  CC                              int3
0090F31C  48 8D 0D FD 93 6C 00            lea rcx, [rip + 0x6c93fd]
0090F323  EB C6                           jmp 0x14090f2eb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlUnicodeToOemN(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a1 = 0;
    result = RtlpIsUtf8Process(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0090F31C;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
loc_0090F2EB:
    v_stack_m10 = (unsigned int)((unsigned int)(a5));
    v_stack_m18 = a4;
    result = RtlUnicodeToCustomCPN(result + 1032, 0, (unsigned int)((unsigned int)((unsigned int)(a2))), a3);
    v_rsp = (v_rsp) + (48);
    return result;
loc_0090F31C:
    goto loc_0090F2EB;
}
```

## 5. (Beta) C Style

```c
int64_t RtlUnicodeToOemN(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg1 = 0;
    result = RtlpIsUtf8Process(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0090F31C;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
loc_0090F2EB:
    v_stack_m10 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m18 = Arg4;
    result = RtlUnicodeToCustomCPN(result + 1032, 0, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3);
    local_rsp = (local_rsp) + (48);
    return result;
loc_0090F31C:
    goto loc_0090F2EB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090F2B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0090F2B0[BB_0090F2B0]
  bb_0090F2DA[BB_0090F2DA]
  bb_0090F2EB[BB_0090F2EB]
  bb_0090F31B[BB_0090F31B]
  bb_0090F31C[BB_0090F31C]
  bb_0090F2B0 -->|branch| bb_0090F31C
  bb_0090F2B0 -->|fallthrough| bb_0090F2DA
  bb_0090F2DA -->|flow| bb_0090F2EB
  bb_0090F31B -->|flow| bb_0090F31C
  bb_0090F31C -->|branch| bb_0090F2EB
```
