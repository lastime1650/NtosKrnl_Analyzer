# PopSuspendResumeInvocation

- RVA: `0x00AAE544`–`0x00AAE566` (길이 `34` bytes)
- VA: `0x0000000140AAE544`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AAE55F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopDirectedDripsSendSuspendResumeNotification](../75/PopDirectedDripsSendSuspendResumeNotification_function_00757CCC.md) at `0x00757D11`
- [PopDirectedDripsSendSuspendResumeNotification](../75/PopDirectedDripsSendSuspendResumeNotification_function_00757CCC.md) at `0x00757D21`
- [PopDirectedDripsSendSuspendResumeNotification](../75/PopDirectedDripsSendSuspendResumeNotification_function_00757CCC.md) at `0x00757DA0`
- [PopDirectedDripsSendSuspendResumeNotification](../75/PopDirectedDripsSendSuspendResumeNotification_function_00757CCC.md) at `0x00757DB6`
- [PopSendSuspendResumeApplicationNotification](../75/PopSendSuspendResumeApplicationNotification_function_0075EC74.md) at `0x0075ECF0`
- [PopSendSuspendResumeApplicationNotification](../75/PopSendSuspendResumeApplicationNotification_function_0075EC74.md) at `0x0075ED07`
- [PopSendSuspendResumeServiceNotification](../75/PopSendSuspendResumeServiceNotification_function_0075ED9C.md) at `0x0075EDEC`
- [PopSendSuspendResumeServiceNotification](../75/PopSendSuspendResumeServiceNotification_function_0075ED9C.md) at `0x0075EE03`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8D2B0`

### Static image references
- `0x00AAE548` → RVA `0x00E677A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AAE55F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAE544  48 83 EC 28                     sub rsp, 0x28
00AAE548  48 8B 15 59 92 3B 00            mov rdx, qword ptr [rip + 0x3b9259]
00AAE54F  33 C0                           xor eax, eax
00AAE551  48 85 D2                        test rdx, rdx
00AAE554  75 06                           jne 0x140aae55c
00AAE556  48 83 C4 28                     add rsp, 0x28
00AAE55A  C3                              ret
00AAE55B  CC                              int3
00AAE55C  48 8B C2                        mov rax, rdx
00AAE55F  E8 6C C5 C0 FF                  call 0x1406baad0
00AAE564  EB F0                           jmp 0x140aae556
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSuspendResumeInvocation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (*(unsigned __int64 *)(v_rip + 3904089) != 0) goto loc_00AAE55C;
loc_00AAE556:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AAE55C:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(v_rip + 3904089), a3, a4);
    goto loc_00AAE556;
}
```

## 5. (Beta) C Style

```c
void PopSuspendResumeInvocation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (*(uint64_t *)(v_rip + 0x3B9259) != 0) goto loc_00AAE55C;
loc_00AAE556:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AAE55C:
    result = guard_dispatch_icall(a1, *(uint64_t *)(v_rip + 0x3B9259), a3, a4);
    goto loc_00AAE556;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAE544&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAE544[BB_00AAE544]
  bb_00AAE556[BB_00AAE556]
  bb_00AAE55B[BB_00AAE55B]
  bb_00AAE55C[BB_00AAE55C]
  bb_00AAE544 -->|branch| bb_00AAE55C
  bb_00AAE544 -->|fallthrough| bb_00AAE556
  bb_00AAE55B -->|flow| bb_00AAE55C
  bb_00AAE55C -->|branch| bb_00AAE556
```
