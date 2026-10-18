# EtwpReleaseLoggerContext

- RVA: `0x00A04160`–`0x00A041A1` (길이 `65` bytes)
- VA: `0x0000000140A04160`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **36**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A04176` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)
- `0x00A04195` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)

### Direct callers
- [EtwpAdjustSiloTraceBuffers](../../text/3E/EtwpAdjustSiloTraceBuffers_function_003EB720.md) at `0x003EB77D`
- [EtwpGetPmcSessions](../../text/64/EtwpGetPmcSessions_function_0064EB08.md) at `0x0064EBA2`
- [EtwpGetPmcSessions](../../text/64/EtwpGetPmcSessions_function_0064EB08.md) at `0x0064EC84`
- [EtwpTransitionToRealtime](../../text/65/EtwpTransitionToRealtime_function_006518D8.md) at `0x00651A33`
- [EtwpGetCompressionSettings](../../text/65/EtwpGetCompressionSettings_function_006535A8.md) at `0x0065366D`
- [EtwpSetCompressionSettings](../../text/65/EtwpSetCompressionSettings_function_00653910.md) at `0x006539CE`
- [EtwpTrackProviderBinaryKm](../6F/EtwpTrackProviderBinaryKm_function_006FD8E8.md) at `0x006FDA4E`
- [EtwpTrackProviderBinaryKm](../6F/EtwpTrackProviderBinaryKm_function_006FD8E8.md) at `0x006FDA9E`
- [EtwShutdown](../7B/EtwShutdown_function_007B50B0.md) at `0x007B5192`
- [EtwShutdown](../7B/EtwShutdown_function_007B50B0.md) at `0x007B51B6`
- [EtwpIncrementTraceFile](../7B/EtwpIncrementTraceFile_function_007B9210.md) at `0x007B92CD`
- [EtwpQueryReferenceTime](../7B/EtwpQueryReferenceTime_function_007B92F0.md) at `0x007B933C`
- [WmiQueryTraceInformation](../7B/WmiQueryTraceInformation_function_007B9370.md) at `0x007B947D`
- [WmiQueryTraceInformation](../7B/WmiQueryTraceInformation_function_007B9370.md) at `0x007B9509`
- [WmiQueryTraceInformation](../7B/WmiQueryTraceInformation_function_007B9370.md) at `0x007B9A1F`
- [WmiQueryTraceInformation](../7B/WmiQueryTraceInformation_function_007B9370.md) at `0x007B9B1B`
- [WmiQueryTraceInformation](../7B/WmiQueryTraceInformation_function_007B9370.md) at `0x007B9B76`
- [EtwRegisterEventCallback](../7B/EtwRegisterEventCallback_function_007BC3B0.md) at `0x007BC454`
- [EtwpUpdatePeriodicCaptureState](../7B/EtwpUpdatePeriodicCaptureState_function_007BCC4C.md) at `0x007BCE83`
- [SendCaptureStateNotificationsWorker](../7B/SendCaptureStateNotificationsWorker_function_007BCF30.md) at `0x007BD2BD`
- [EtwpGetSoftRestartInformation](../7B/EtwpGetSoftRestartInformation_function_007BEC70.md) at `0x007BED37`
- [EtwpKsrCallback](../7B/EtwpKsrCallback_function_007BEE10.md) at `0x007BEEE5`
- [EtwpUpdateEnableMask](../8C/EtwpUpdateEnableMask_function_008C0948.md) at `0x008C0AD3`
- [sub_008C2DC2](../8C/Unknown_function_008C2DC2.md) at `0x008C2E71`
- [EtwpTrackProviderRegistration](../8C/EtwpTrackProviderRegistration_function_008C368C.md) at `0x008C3700`
- [EtwpTrackProviderRegistration](../8C/EtwpTrackProviderRegistration_function_008C368C.md) at `0x008C376F`
- [EtwpTrackProviderRegistration](../8C/EtwpTrackProviderRegistration_function_008C368C.md) at `0x008C37D2`
- [EtwpAcquireLoggerContextByLoggerName](../93/EtwpAcquireLoggerContextByLoggerName_function_0093283C.md) at `0x00932911`
- [sub_0093299F](../93/Unknown_function_0093299F.md) at `0x00932A06`
- [EtwpStopTrace](../9B/EtwpStopTrace_function_009BCE84.md) at `0x009BD0A3`
- [EtwpStopTrace](../9B/EtwpStopTrace_function_009BCE84.md) at `0x009BD0F4`
- [EtwpAddRegEntryToGroup](../9F/EtwpAddRegEntryToGroup_function_009F39D4.md) at `0x009F3C99`
- [EtwpAddRegEntryToGroup](../9F/EtwpAddRegEntryToGroup_function_009F39D4.md) at `0x009F3DDE`
- [EtwpAddRegEntryToGroup](../9F/EtwpAddRegEntryToGroup_function_009F39D4.md) at `0x009F3F18`
- [EtwpAddRegEntryToGroup](../9F/EtwpAddRegEntryToGroup_function_009F39D4.md) at `0x009F4012`
- [EtwpSetProviderBinaryTracking](EtwpSetProviderBinaryTracking_function_00A03BF4.md) at `0x00A03C9C`
- [EtwpSetSoftRestartInformation](../A5/EtwpSetSoftRestartInformation_function_00A53DB8.md) at `0x00A53FB9`
- [EtwpEnableGuid](../A5/EtwpEnableGuid_function_00A5CD28.md) at `0x00A5D9AA`
- [EtwpLookupLoggerIdByName](../A6/EtwpLookupLoggerIdByName_function_00A60FF8.md) at `0x00A61078`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9A4A1`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9A4B6`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9ADC0`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9ADF5`
- [NtTraceControl](../A9/NtTraceControl_function_00A9ED40.md) at `0x00A9F859`
- [EtwpUpdateTrace](../AB/EtwpUpdateTrace_function_00ABCC7C.md) at `0x00ABD12E`
- [EtwpTracingProvEnableCallback](../AC/EtwpTracingProvEnableCallback_function_00AC28B0.md) at `0x00AC290D`
- [EtwQueryPerformanceTraceInformation](../AF/EtwQueryPerformanceTraceInformation_function_00AF28A4.md) at `0x00AF2B42`
- [EtwQueryPerformanceTraceInformation](../AF/EtwQueryPerformanceTraceInformation_function_00AF28A4.md) at `0x00AF2BF6`
- [EtwQueryPerformanceTraceInformation](../AF/EtwQueryPerformanceTraceInformation_function_00AF28A4.md) at `0x00AF2E51`
- [EtwpFlushTrace](../AF/EtwpFlushTrace_function_00AF47B4.md) at `0x00AF499A`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3CC3E`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3D497`
- [sub_00B48F36](../B4/Unknown_function_00B48F36.md) at `0x00B48FC8`
- [EtwpEnableBootLoggerRegistryProviders](../../init/C4/EtwpEnableBootLoggerRegistryProviders_function_00C4EF8C.md) at `0x00C4F05E`
- [EtwpFixBootLoggers](../../init/C4/EtwpFixBootLoggers_function_00C4F09C.md) at `0x00C4F18E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A04176` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
  - `0x00A04195` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A04160  40 53                           push rbx
00A04162  48 83 EC 20                     sub rsp, 0x20
00A04166  48 8B D9                        mov rbx, rcx
00A04169  84 D2                           test dl, dl
00A0416B  74 0E                           je 0x140a0417b
00A0416D  48 81 C1 78 02 00 00            add rcx, 0x278
00A04174  33 D2                           xor edx, edx
00A04176  E8 95 26 99 FF                  call 0x140396810
00A0417B  48 8B 83 50 05 00 00            mov rax, qword ptr [rbx + 0x550]
00A04182  BA 01 00 00 00                  mov edx, 1
00A04187  44 8B 03                        mov r8d, dword ptr [rbx]
00A0418A  48 8B 88 C0 02 00 00            mov rcx, qword ptr [rax + 0x2c0]
00A04191  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
00A04195  E8 B6 AE 85 FF                  call 0x14025f050
00A0419A  48 83 C4 20                     add rsp, 0x20
00A0419E  5B                              pop rbx
00A0419F  C3                              ret
00A041A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpReleaseLoggerContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((unsigned __int8)(a2) != 0) {
        a1 = (a1) + (632);
        a2 = 0;
        result = KeReleaseMutex(a1, a2, a3, a4);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1360) + 704) + (unsigned int)(*(unsigned int *)(a1)) * 8), 1, (unsigned int)(*(unsigned int *)(a1)), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpReleaseLoggerContext(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((uint8_t)(Arg2) != 0) {
        Arg1 = (Arg1) + (632);
        Arg2 = 0;
        result = KeReleaseMutex(Arg1, Arg2, a3, a4);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x550) + 0x2C0) + (uint32_t)(*(uint32_t *)(arg1)) * 8), 1, (uint32_t)(*(uint32_t *)(arg1)), a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x550` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A04160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A04160[BB_00A04160]
  bb_00A0416D[BB_00A0416D]
  bb_00A0417B[BB_00A0417B]
  bb_00A041A0[BB_00A041A0]
  bb_00A04160 -->|branch| bb_00A0417B
  bb_00A04160 -->|fallthrough| bb_00A0416D
  bb_00A0416D -->|flow| bb_00A0417B
```
