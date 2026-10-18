# PfLockExclusiveRelease

- RVA: `0x00491D88`–`0x00491DB9` (길이 `49` bytes)
- VA: `0x0000000140491D88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **25**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00491DA0` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00491DA8` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00491DAD` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [sub_00342A4A](../34/Unknown_function_00342A4A.md) at `0x00342ABD`
- [sub_00342A4A](../34/Unknown_function_00342A4A.md) at `0x00342AEE`
- [sub_00342B2F](../34/Unknown_function_00342B2F.md) at `0x00342B83`
- [sub_00342B2F](../34/Unknown_function_00342B2F.md) at `0x00342BBE`
- [PfpRpCHashGrow](../../page/70/PfpRpCHashGrow_function_0070189C.md) at `0x00701AFC`
- [PfpRpShutdown](../../page/75/PfpRpShutdown_function_00751C70.md) at `0x00751E19`
- [PfSnSetAltPrefetchParam](../../page/75/PfSnSetAltPrefetchParam_function_00752424.md) at `0x00752803`
- [PfSnSetAltPrefetchParam](../../page/75/PfSnSetAltPrefetchParam_function_00752424.md) at `0x00752838`
- [PfpParametersWatcher](../../page/75/PfpParametersWatcher_function_00753140.md) at `0x00753313`
- [VmCleanProcessAddressSpace](../../page/7A/VmCleanProcessAddressSpace_function_007ACD38.md) at `0x007ACD6B`
- [VmCreateMemoryRange](../../page/7A/VmCreateMemoryRange_function_007AD1D0.md) at `0x007AD382`
- [VmPinMemoryRange](../../page/7A/VmPinMemoryRange_function_007AD450.md) at `0x007AD669`
- [VmUnpinMemoryRange](../../page/7A/VmUnpinMemoryRange_function_007AD730.md) at `0x007AD831`
- [VmUpdateCommitMemoryRange](../../page/7A/VmUpdateCommitMemoryRange_function_007AD860.md) at `0x007AD8D0`
- [VmpPauseResumeNotify](../../page/7A/VmpPauseResumeNotify_function_007ADA08.md) at `0x007ADAA2`
- [VmpPauseResumeNotify](../../page/7A/VmpPauseResumeNotify_function_007ADA08.md) at `0x007ADC0C`
- [PfProcessExitNotification](../../page/90/PfProcessExitNotification_function_00903CA4.md) at `0x00903CDE`
- [PfpPrefetchSharedStart](../../page/93/PfpPrefetchSharedStart_function_00939D24.md) at `0x00939DD1`
- [PfpPrefetchSharedCleanup](../../page/93/PfpPrefetchSharedCleanup_function_00939EB0.md) at `0x00939F17`
- [PfpRpCHashDeleteEntries](../../page/A3/PfpRpCHashDeleteEntries_function_00A322A8.md) at `0x00A32451`
- [VmDeleteMemoryRange](../../page/A7/VmDeleteMemoryRange_function_00A7AC50.md) at `0x00A7ACF2`
- [PfpRpCHashAddEntries](../../page/A7/PfpRpCHashAddEntries_function_00A7D43C.md) at `0x00A7D5C7`
- [PfpRpCHashAddEntries](../../page/A7/PfpRpCHashAddEntries_function_00A7D43C.md) at `0x00A7D606`
- [VmSplitMemoryRange](../../page/A9/VmSplitMemoryRange_function_00A922A0.md) at `0x00A9234A`
- [VmMergeMemoryRanges](../../page/A9/VmMergeMemoryRanges_function_00A94AE0.md) at `0x00A94BC1`
- [PfpRpCHashEmpty](../../page/AB/PfpRpCHashEmpty_function_00AB4D84.md) at `0x00AB4E14`
- [PfpRpCHashEmpty](../../page/AB/PfpRpCHashEmpty_function_00AB4D84.md) at `0x00AB4E20`
- [PfTAccessTracingCleanup](../../pagelk/B6/PfTAccessTracingCleanup_function_00B6B8AC.md) at `0x00B6B95B`
- [PfTAccessTracingStart](../../pagelk/B6/PfTAccessTracingStart_function_00B6B9F0.md) at `0x00B6BA50`
- [PfTSetTracingPriority](../../pagelk/B6/PfTSetTracingPriority_function_00B6BA6C.md) at `0x00B6BAA8`
- [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) at `0x00B6BBE8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00491D88  40 53                           push rbx
00491D8A  48 83 EC 20                     sub rsp, 0x20
00491D8E  48 8B D9                        mov rbx, rcx
00491D91  48 83 C8 FF                     or rax, 0xffffffffffffffff
00491D95  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
00491D9A  24 06                           and al, 6
00491D9C  3C 02                           cmp al, 2
00491D9E  75 05                           jne 0x140491da5
00491DA0  E8 2B 40 DD FF                  call 0x140265dd0
00491DA5  48 8B CB                        mov rcx, rbx
00491DA8  E8 53 F8 E4 FF                  call 0x1402e1600
00491DAD  E8 FE BA DC FF                  call 0x14025d8b0
00491DB2  48 83 C4 20                     add rsp, 0x20
00491DB6  5B                              pop rbx
00491DB7  C3                              ret
00491DB8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfLockExclusiveRelease(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfLockExclusiveRelease(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1, a2, a3, a4);
    result = KeLeaveCriticalRegion(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00491D88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00491D88[BB_00491D88]
  bb_00491DA0[BB_00491DA0]
  bb_00491DA5[BB_00491DA5]
  bb_00491DB8[BB_00491DB8]
  bb_00491D88 -->|branch| bb_00491DA5
  bb_00491D88 -->|fallthrough| bb_00491DA0
  bb_00491DA0 -->|flow| bb_00491DA5
```
