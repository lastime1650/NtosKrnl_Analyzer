# SshpSessionManagerSendControlEvent

- RVA: `0x00A871C0`–`0x00A871FA` (길이 `58` bytes)
- VA: `0x0000000140A871C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `18`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A871D7` → [Feature_SleepStudySlimControlEtl__private_ReportDeviceUsage](../../text/4F/Feature_SleepStudySlimControlEtl__private_ReportDeviceUsage_function_004FC658.md) (function, `0x004FC658`)
- `0x00A871E4` → [SshpSessionManagerSendControlEventSlimEtl](SshpSessionManagerSendControlEventSlimEtl_function_00A87200.md) (function, `0x00A87200`)

### Direct callers
- [SshSessionManagerTraceAcDcStateChange](../77/SshSessionManagerTraceAcDcStateChange_function_0077392C.md) at `0x007739C7`
- [SshSessionManagerTraceBatteryCountChange](../77/SshSessionManagerTraceBatteryCountChange_function_007739E8.md) at `0x00773A83`
- [SshSessionManagerTraceCsEnterReason](../77/SshSessionManagerTraceCsEnterReason_function_00773AA4.md) at `0x00773BB8`
- [SshSessionManagerTraceCsExitReason](../77/SshSessionManagerTraceCsExitReason_function_00773BDC.md) at `0x00773E7E`
- [SshSessionManagerTraceDirtyTransition](../77/SshSessionManagerTraceDirtyTransition_function_00773EB0.md) at `0x00774075`
- [SshSessionManagerTracePreSleepNotification](../77/SshSessionManagerTracePreSleepNotification_function_00774098.md) at `0x0077420A`
- [SshSessionManagerTraceShutdownAction](../77/SshSessionManagerTraceShutdownAction_function_0077422C.md) at `0x0077428F`
- [SshSessionManagerTraceSystemStop](../77/SshSessionManagerTraceSystemStop_function_007742B0.md) at `0x0077433A`
- [SshpSessionManagerTraceSystemStart](../77/SshpSessionManagerTraceSystemStart_function_007746CC.md) at `0x007746DC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A871D7` → [Feature_SleepStudySlimControlEtl__private_ReportDeviceUsage](../../text/4F/Feature_SleepStudySlimControlEtl__private_ReportDeviceUsage_function_004FC658.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A871C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A871C5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A871CA  57                              push rdi
00A871CB  48 83 EC 20                     sub rsp, 0x20
00A871CF  49 8B D8                        mov rbx, r8
00A871D2  8B FA                           mov edi, edx
00A871D4  48 8B F1                        mov rsi, rcx
00A871D7  E8 7C 54 A7 FF                  call 0x1404fc658
00A871DC  4C 8B C3                        mov r8, rbx
00A871DF  8B D7                           mov edx, edi
00A871E1  48 8B CE                        mov rcx, rsi
00A871E4  E8 17 00 00 00                  call 0x140a87200
00A871E9  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A871EE  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00A871F3  48 83 C4 20                     add rsp, 0x20
00A871F7  5F                              pop rdi
00A871F8  C3                              ret
00A871F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpSessionManagerSendControlEvent(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = Feature_SleepStudySlimControlEtl__private_ReportDeviceUsage(a1, a2, a3, a4);
    result = SshpSessionManagerSendControlEventSlimEtl(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SshpSessionManagerSendControlEvent(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = Feature_SleepStudySlimControlEtl__private_ReportDeviceUsage(Arg1, Arg2, Arg3, a4);
    result = SshpSessionManagerSendControlEventSlimEtl(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A871C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A871C0[BB_00A871C0]
  bb_00A871F9[BB_00A871F9]
```
