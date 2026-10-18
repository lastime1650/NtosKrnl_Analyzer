# ExCallCallBack

- RVA: `0x009054B4`–`0x0090551D` (길이 `105` bytes)
- VA: `0x00000001409054B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069AD0`
- 디코드: `31`개 명령, `105/105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009054D1` → [ExReferenceCallBackBlock](../../text/2F/ExReferenceCallBackBlock_function_002F0040.md) (function, `0x002F0040`)
- `0x009054EC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009054F9` → [ExDereferenceCallBackBlock](../../text/44/ExDereferenceCallBackBlock_function_0044D730.md) (function, `0x0044D730`)

### Direct callers
- [PfpQueryGpuUtilization](PfpQueryGpuUtilization_function_00903974.md) at `0x00903A3A`
- [PspExitLastThread](PspExitLastThread_function_00904184.md) at `0x00904395`
- [ExpWin32CloseProcedure](ExpWin32CloseProcedure_function_00904FA0.md) at `0x0090504F`
- [ExpWin32OkayToCloseProcedure](ExpWin32OkayToCloseProcedure_function_009050A0.md) at `0x00905170`
- [ExpWin32DeleteProcedure](ExpWin32DeleteProcedure_function_009051E0.md) at `0x0090527F`
- [ExpWin32OpenProcedure](ExpWin32OpenProcedure_function_009052D0.md) at `0x00905394`
- [ExpWin32ParseProcedure](ExpWin32ParseProcedure_function_00905400.md) at `0x00905496`
- [PspExitThread](PspExitThread_function_00905F60.md) at `0x00906251`
- [PsConvertToGuiThread](../A2/PsConvertToGuiThread_function_00A2F8B0.md) at `0x00A2FA90`
- [PsConvertToGuiThread](../A2/PsConvertToGuiThread_function_00A2F8B0.md) at `0x00A2FAE8`
- [PsApplyDeepFreezeOptimizations](../AA/PsApplyDeepFreezeOptimizations_function_00AA9EDC.md) at `0x00AA9F55`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009054D1` → [ExReferenceCallBackBlock](../../text/2F/ExReferenceCallBackBlock_function_002F0040.md) (`PAGE` → `.text`)
  - `0x009054EC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009054F9` → [ExDereferenceCallBackBlock](../../text/44/ExDereferenceCallBackBlock_function_0044D730.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009054B4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009054B9  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
009054BE  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
009054C3  57                              push rdi
009054C4  48 83 EC 20                     sub rsp, 0x20
009054C8  49 8B D8                        mov rbx, r8
009054CB  48 8B EA                        mov rbp, rdx
009054CE  48 8B F1                        mov rsi, rcx
009054D1  E8 6A AB 9E FF                  call 0x1402f0040
009054D6  48 8B F8                        mov rdi, rax
009054D9  48 85 C0                        test rax, rax
009054DC  74 38                           je 0x140905516
009054DE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
009054E2  4C 8B C3                        mov r8, rbx
009054E5  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009054E9  48 8B D5                        mov rdx, rbp
009054EC  E8 DF 55 DB FF                  call 0x1406baad0
009054F1  48 8B D7                        mov rdx, rdi
009054F4  48 8B CE                        mov rcx, rsi
009054F7  8B D8                           mov ebx, eax
009054F9  E8 32 82 B4 FF                  call 0x14044d730
009054FE  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00905503  8B C3                           mov eax, ebx
00905505  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0090550A  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0090550F  48 83 C4 20                     add rsp, 0x20
00905513  5F                              pop rdi
00905514  C3                              ret
00905515  CC                              int3
00905516  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0090551B  EB E1                           jmp 0x1409054fe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExCallCallBack(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = ExReferenceCallBackBlock(a1, a2, a3, a4);
    if (result == 0) goto loc_00905516;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 16), a2, a3, a4);
    result = ExDereferenceCallBackBlock(a1, result, a3, a4);
loc_009054FE:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00905516:
    goto loc_009054FE;
}
```

## 5. (Beta) C Style

```c
int64_t ExCallCallBack(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = ExReferenceCallBackBlock(Arg1, Arg2, Arg3, a4);
    if (result == 0) goto loc_00905516;
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x10), Arg2, Arg3, a4);
    result = ExDereferenceCallBackBlock(Arg1, result, Arg3, a4);
loc_009054FE:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00905516:
    goto loc_009054FE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009054B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009054B4[BB_009054B4]
  bb_009054DE[BB_009054DE]
  bb_009054FE[BB_009054FE]
  bb_00905515[BB_00905515]
  bb_00905516[BB_00905516]
  bb_009054B4 -->|branch| bb_00905516
  bb_009054B4 -->|fallthrough| bb_009054DE
  bb_009054DE -->|flow| bb_009054FE
  bb_00905515 -->|flow| bb_00905516
  bb_00905516 -->|branch| bb_009054FE
```
