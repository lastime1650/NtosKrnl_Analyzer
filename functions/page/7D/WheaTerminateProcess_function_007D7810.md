# WheaTerminateProcess

- RVA: `0x007D7810`–`0x007D787E` (길이 `110` bytes)
- VA: `0x00000001407D7810`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CBDD4`
- 디코드: `29`개 명령, `110/110` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007D783E` → [WheaGetCurrentProcessName](../../text/65/WheaGetCurrentProcessName_function_0065F260.md) (function, `0x0065F260`)
- `0x007D784B` → [PsTerminateProcess](../90/PsTerminateProcess_function_00904C64.md) (function, `0x00904C64`)
- `0x007D7859` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x007D786B` → [WheapLogProcessTerminateEvent](../../text/66/WheapLogProcessTerminateEvent_function_006609EC.md) (function, `0x006609EC`)

### Direct callers
- [KiMcheckAlternateReturn](../../text/5C/KiMcheckAlternateReturn_function_005CB180.md) at `0x005CB343`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007D783E` → [WheaGetCurrentProcessName](../../text/65/WheaGetCurrentProcessName_function_0065F260.md) (`PAGE` → `.text`)
  - `0x007D7859` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x007D786B` → [WheapLogProcessTerminateEvent](../../text/66/WheapLogProcessTerminateEvent_function_006609EC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D7810  4C 8B DC                        mov r11, rsp
007D7813  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
007D7817  57                              push rdi
007D7818  48 83 EC 20                     sub rsp, 0x20
007D781C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D7825  49 8D 53 08                     lea rdx, [r11 + 8]
007D7829  49 83 63 10 00                  and qword ptr [r11 + 0x10], 0
007D782E  49 8D 4B 10                     lea rcx, [r11 + 0x10]
007D7832  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
007D7837  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
007D783E  E8 1D 7A E8 FF                  call 0x14065f260
007D7843  BA 13 07 00 C0                  mov edx, 0xc0000713
007D7848  48 8B CF                        mov rcx, rdi
007D784B  E8 14 D4 12 00                  call 0x140904c64
007D7850  8B D8                           mov ebx, eax
007D7852  85 C0                           test eax, eax
007D7854  78 1A                           js 0x1407d7870
007D7856  48 8B CF                        mov rcx, rdi
007D7859  E8 B2 60 C6 FF                  call 0x14043d910
007D785E  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
007D7863  48 8B C8                        mov rcx, rax
007D7866  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
007D786B  E8 7C 91 E8 FF                  call 0x1406609ec
007D7870  8B C3                           mov eax, ebx
007D7872  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
007D7877  48 83 C4 20                     add rsp, 0x20
007D787B  5F                              pop rdi
007D787C  C3                              ret
007D787D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaTerminateProcess(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = WheaGetCurrentProcessName(v_rsp + 16, v_rsp + 8, a3, a4);
    result = PsTerminateProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0xC0000713ULL), a3, a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
        result = PsGetProcessId(a1, (unsigned int)(0xC0000713ULL), a3, a4);
        a3 = v_stack_p8;
        a1 = result;
        a2 = v_stack_p10;
        result = WheapLogProcessTerminateEvent(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
void WheaTerminateProcess(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = WheaGetCurrentProcessName(local_rsp + 16, local_rsp + 8, a3, a4);
    result = PsTerminateProcess(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0xC0000713ULL), a3, a4);
    if (!(sign_flag)) {
        a1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
        result = PsGetProcessId(a1, (uint32_t)(0xC0000713ULL), a3, a4);
        a3 = v_stack_p8;
        a1 = result;
        a2 = v_stack_p10;
        result = WheapLogProcessTerminateEvent(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D7810&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D7810[BB_007D7810]
  bb_007D7856[BB_007D7856]
  bb_007D7870[BB_007D7870]
  bb_007D787D[BB_007D787D]
  bb_007D7810 -->|branch| bb_007D7870
  bb_007D7810 -->|fallthrough| bb_007D7856
  bb_007D7856 -->|flow| bb_007D7870
```
