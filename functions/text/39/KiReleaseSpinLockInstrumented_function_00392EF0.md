# KiReleaseSpinLockInstrumented

- RVA: `0x00392EF0`–`0x00392F16` (길이 `38` bytes)
- VA: `0x0000000140392EF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **54**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00392F0B` → [PerfLogSpinLockRelease](../4C/PerfLogSpinLockRelease_function_004CD094.md) (function, `0x004CD094`)

### Direct callers
- [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) at `0x00206697`
- [sub_00207070](../20/Unknown_function_00207070.md) at `0x002070DF`
- [sub_00207070](../20/Unknown_function_00207070.md) at `0x00207100`
- [sub_002072AC](../20/Unknown_function_002072AC.md) at `0x002072C1`
- [sub_00207480](../20/Unknown_function_00207480.md) at `0x002074AB`
- [IopQueueThreadIrp](../20/IopQueueThreadIrp_function_002075C0.md) at `0x002076B0`
- [sub_00207C21](../20/Unknown_function_00207C21.md) at `0x00207C37`
- [sub_00207D3E](../20/Unknown_function_00207D3E.md) at `0x0020828C`
- [sub_00208E4A](../20/Unknown_function_00208E4A.md) at `0x00208EA3`
- [IoRemoveIoCompletion](../20/IoRemoveIoCompletion_function_0020B580.md) at `0x0020BCEE`
- [ExpFreeOwnerEntry](../20/ExpFreeOwnerEntry_function_0020F740.md) at `0x0020F962`
- [sub_00210801](../21/Unknown_function_00210801.md) at `0x00210935`
- [ExEnterPriorityRegionAndAcquireResourceShared](../21/ExEnterPriorityRegionAndAcquireResourceShared_function_00213870.md) at `0x00213A2B`
- [sub_002142F9](../21/Unknown_function_002142F9.md) at `0x00214D78`
- [NtCancelTimer](../23/NtCancelTimer_function_00230D90.md) at `0x00230F83`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x002321EE`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x0023220E`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x00232235`
- [ExpUpdateTimerConfigurationWorker](../23/ExpUpdateTimerConfigurationWorker_function_00235410.md) at `0x0023564A`
- [HalpPCIReleaseConfigSpaceLock](../23/HalpPCIReleaseConfigSpaceLock_function_002362D8.md) at `0x00236331`
- [KiExecuteAllDpcs](../25/KiExecuteAllDpcs_function_0025B740.md) at `0x0025C7B8`
- [sub_0025EB5D](../25/Unknown_function_0025EB5D.md) at `0x0025EE15`
- [sub_00261078](../26/Unknown_function_00261078.md) at `0x002610C5`
- [sub_00261078](../26/Unknown_function_00261078.md) at `0x00261119`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x002754B3`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x00275509`
- [PopFxDispatchPluginWorkOnce](../2B/PopFxDispatchPluginWorkOnce_function_002BC69C.md) at `0x002BC819`
- [PopFxDisableWorkOrderWatchdog](../2B/PopFxDisableWorkOrderWatchdog_function_002BC858.md) at `0x002BC90B`
- [PopFxEnableWorkOrderWatchdog](../2B/PopFxEnableWorkOrderWatchdog_function_002BD268.md) at `0x002BD3CF`
- [sub_002BD6E6](../2B/Unknown_function_002BD6E6.md) at `0x002BD7C6`
- [PopFxActivateComponentDependents](../2B/PopFxActivateComponentDependents_function_002BE9F0.md) at `0x002BED70`
- [KeIntSteerPeriodic](../2D/KeIntSteerPeriodic_function_002D6D04.md) at `0x002D6EBB`
- [PopFxActivateComponentDependencies](../2D/PopFxActivateComponentDependencies_function_002D9B10.md) at `0x002D9CC1`
- [PpmUpdatePerformanceFeedback](../2D/PpmUpdatePerformanceFeedback_function_002DE580.md) at `0x002DEF18`
- [EtwpApcPoolThunk](../2F/EtwpApcPoolThunk_function_002FA090.md) at `0x002FA2A2`
- [sub_0034DBE0](../34/Unknown_function_0034DBE0.md) at `0x0034DBFA`
- [sub_0034FEB1](../34/Unknown_function_0034FEB1.md) at `0x0035007D`
- [IopFreeWaitCompletionPacket](../35/IopFreeWaitCompletionPacket_function_00351A50.md) at `0x00351EAE`
- [FsRtlFastUnlockSingleExclusive](../38/FsRtlFastUnlockSingleExclusive_function_0038C8E0.md) at `0x0038CB17`
- [sub_0038D68D](../38/Unknown_function_0038D68D.md) at `0x0038D6A6`
- [FsRtlPrivateLock](../38/FsRtlPrivateLock_function_0038DF90.md) at `0x0038E539`
- [PsLeavePriorityRegion](PsLeavePriorityRegion_function_00390F00.md) at `0x0039100E`
- [ExpUpdateTimerResolution](ExpUpdateTimerResolution_function_003914A0.md) at `0x003916CC`
- [PsBoostThreadIo](PsBoostThreadIo_function_003927C0.md) at `0x003929C4`
- [KeReleaseSpinLock](KeReleaseSpinLock_function_00392BA0.md) at `0x00392BE6`
- [PsBoostThreadIoEx](PsBoostThreadIoEx_function_00392C00.md) at `0x00392E11`
- [KeSetTimer2](../3A/KeSetTimer2_function_003A08E0.md) at `0x003A1005`
- [KeSetTimer2](../3A/KeSetTimer2_function_003A08E0.md) at `0x003A1039`
- [sub_003A1A0C](../3A/Unknown_function_003A1A0C.md) at `0x003A1BF6`
- [PsEnterPriorityRegion](../3F/PsEnterPriorityRegion_function_003F8CD0.md) at `0x003F8E00`
- [sub_003FD43F](../3F/Unknown_function_003FD43F.md) at `0x003FD4CC`
- [ExGenRandom](../41/ExGenRandom_function_0041B010.md) at `0x0041B1BD`
- [sub_004314C3](../43/Unknown_function_004314C3.md) at `0x0043153A`
- [sub_004339AF](../43/Unknown_function_004339AF.md) at `0x004339C5`
- [KeReleaseSpinLockFromDpcLevel](../43/KeReleaseSpinLockFromDpcLevel_function_0043FDA0.md) at `0x0043FDC7`
- [IopIncrementCompletionContextUsageCountAndReadData](../44/IopIncrementCompletionContextUsageCountAndReadData_function_00443C60.md) at `0x00443D32`
- [EtwpCovSampCaptureApc](../44/EtwpCovSampCaptureApc_function_004440D0.md) at `0x00444201`
- [KeReleaseInterruptSpinLock](../44/KeReleaseInterruptSpinLock_function_0044D7A0.md) at `0x0044D7EF`
- [IopDecrementCompletionContextUsageCount](../45/IopDecrementCompletionContextUsageCount_function_00452678.md) at `0x00452708`
- [BgpFwReleaseLock](../4B/BgpFwReleaseLock_function_004B357C.md) at `0x004B35E6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00392EF0  48 83 EC 28                     sub rsp, 0x28
00392EF4  4C 8B CA                        mov r9, rdx
00392EF7  F0 48 83 21 00                  lock and qword ptr [rcx], 0
00392EFC  0F 31                           rdtsc
00392EFE  48 C1 E2 20                     shl rdx, 0x20
00392F02  48 0B C2                        or rax, rdx
00392F05  49 8B D1                        mov rdx, r9
00392F08  4C 8B C0                        mov r8, rax
00392F0B  E8 84 A1 13 00                  call 0x1404cd094
00392F10  48 83 C4 28                     add rsp, 0x28
00392F14  C3                              ret
00392F15  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiReleaseSpinLockInstrumented(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (a2) << (32);
    result = (result) | (a2);
    result = PerfLogSpinLockRelease(a1, a2, result, a2);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiReleaseSpinLockInstrumented(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    result = PerfLogSpinLockRelease(Arg1, Arg2, result, Arg2);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00392EF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00392EF0[BB_00392EF0]
  bb_00392F15[BB_00392F15]
```
