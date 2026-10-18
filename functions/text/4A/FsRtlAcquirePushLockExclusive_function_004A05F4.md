# FsRtlAcquirePushLockExclusive

- RVA: `0x004A05F4`–`0x004A064A` (길이 `86` bytes)
- VA: `0x00000001404A05F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **29**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A0617` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x004A0630` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [FsRtlInsertPerStreamContext](../26/FsRtlInsertPerStreamContext_function_00265F70.md) at `0x00266015`
- [FsRtlRemovePerStreamContext](../26/FsRtlRemovePerStreamContext_function_00267760.md) at `0x0026783D`
- [sub_00342A4A](../34/Unknown_function_00342A4A.md) at `0x00342A63`
- [sub_00342A4A](../34/Unknown_function_00342A4A.md) at `0x00342A7D`
- [sub_00342B2F](../34/Unknown_function_00342B2F.md) at `0x00342B56`
- [sub_00342B2F](../34/Unknown_function_00342B2F.md) at `0x00342B70`
- [PfpRpCHashGrow](../../page/70/PfpRpCHashGrow_function_0070189C.md) at `0x007018D2`
- [PfpRpCHashGrow](../../page/70/PfpRpCHashGrow_function_0070189C.md) at `0x007018EA`
- [PfpRpCHashGrow](../../page/70/PfpRpCHashGrow_function_0070189C.md) at `0x00701ACA`
- [PfpRpShutdown](../../page/75/PfpRpShutdown_function_00751C70.md) at `0x00751CA2`
- [PfSnSetAltPrefetchParam](../../page/75/PfSnSetAltPrefetchParam_function_00752424.md) at `0x007526A0`
- [PfpParametersWatcher](../../page/75/PfpParametersWatcher_function_00753140.md) at `0x00753188`
- [VmCleanProcessAddressSpace](../../page/7A/VmCleanProcessAddressSpace_function_007ACD38.md) at `0x007ACD5A`
- [VmCreateMemoryRange](../../page/7A/VmCreateMemoryRange_function_007AD1D0.md) at `0x007AD2D5`
- [VmUpdateCommitMemoryRange](../../page/7A/VmUpdateCommitMemoryRange_function_007AD860.md) at `0x007AD8AB`
- [VmpPauseResumeNotify](../../page/7A/VmpPauseResumeNotify_function_007ADA08.md) at `0x007ADA52`
- [VmpPauseResumeNotify](../../page/7A/VmpPauseResumeNotify_function_007ADA08.md) at `0x007ADBD6`
- [VmpUnpinMemoryRange](../../page/7A/VmpUnpinMemoryRange_function_007ADF6C.md) at `0x007ADFD2`
- [sub_0085EBA1](../../page/85/Unknown_function_0085EBA1.md) at `0x0085EC8C`
- [sub_0085EE4E](../../page/85/Unknown_function_0085EE4E.md) at `0x0085EE56`
- [PfProcessExitNotification](../../page/90/PfProcessExitNotification_function_00903CA4.md) at `0x00903CC2`
- [PfpPrefetchSharedStart](../../page/93/PfpPrefetchSharedStart_function_00939D24.md) at `0x00939D89`
- [PfpPrefetchSharedCleanup](../../page/93/PfpPrefetchSharedCleanup_function_00939EB0.md) at `0x00939EEB`
- [FsRtlTeardownPerStreamContexts](../../page/9A/FsRtlTeardownPerStreamContexts_function_009A5CD0.md) at `0x009A5DCA`
- [FsRtlTeardownPerStreamContexts](../../page/9A/FsRtlTeardownPerStreamContexts_function_009A5CD0.md) at `0x009A5E3C`
- [PfpRpCHashDeleteEntries](../../page/A3/PfpRpCHashDeleteEntries_function_00A322A8.md) at `0x00A322DC`
- [VmDeleteMemoryRange](../../page/A7/VmDeleteMemoryRange_function_00A7AC50.md) at `0x00A7ACAE`
- [PfpRpCHashAddEntries](../../page/A7/PfpRpCHashAddEntries_function_00A7D43C.md) at `0x00A7D4B9`
- [VmSplitMemoryRange](../../page/A9/VmSplitMemoryRange_function_00A922A0.md) at `0x00A922F7`
- [VmMergeMemoryRanges](../../page/A9/VmMergeMemoryRanges_function_00A94AE0.md) at `0x00A94B9F`
- [PfpRpCHashEmpty](../../page/AB/PfpRpCHashEmpty_function_00AB4D84.md) at `0x00AB4DEE`
- [PfpRpCHashEmpty](../../page/AB/PfpRpCHashEmpty_function_00AB4D84.md) at `0x00AB4DF9`
- [PfTAccessTracingCleanup](../../pagelk/B6/PfTAccessTracingCleanup_function_00B6B8AC.md) at `0x00B6B8DF`
- [PfTAccessTracingStart](../../pagelk/B6/PfTAccessTracingStart_function_00B6B9F0.md) at `0x00B6BA08`
- [PfTSetTracingPriority](../../pagelk/B6/PfTSetTracingPriority_function_00B6BA6C.md) at `0x00B6BA84`
- [PfpPartitionAccessTraceLockAcquire](../../pagelk/B6/PfpPartitionAccessTraceLockAcquire_function_00B6BBC4.md) at `0x00B6BBCC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A05F4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004A05F9  57                              push rdi
004A05FA  48 83 EC 20                     sub rsp, 0x20
004A05FE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004A0607  45 33 C0                        xor r8d, r8d
004A060A  33 D2                           xor edx, edx
004A060C  48 8B F9                        mov rdi, rcx
004A060F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004A0616  90                              nop
004A0617  E8 14 FC D6 FF                  call 0x140210230
004A061C  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
004A0622  48 8B D8                        mov rbx, rax
004A0625  73 0E                           jae 0x1404a0635
004A0627  4C 8B C7                        mov r8, rdi
004A062A  48 8B D0                        mov rdx, rax
004A062D  48 8B CF                        mov rcx, rdi
004A0630  E8 5B F6 D6 FF                  call 0x14020fc90
004A0635  48 85 DB                        test rbx, rbx
004A0638  74 04                           je 0x1404a063e
004A063A  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
004A063E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004A0643  48 83 C4 20                     add rsp, 0x20
004A0647  5F                              pop rdi
004A0648  C3                              ret
004A0649  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlAcquirePushLockExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1;
        a2 = result;
        a1 = a1;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlAcquirePushLockExclusive(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1;
        Arg2 = result;
        Arg1 = Arg1;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A05F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A05F4[BB_004A05F4]
  bb_004A0627[BB_004A0627]
  bb_004A0635[BB_004A0635]
  bb_004A063A[BB_004A063A]
  bb_004A063E[BB_004A063E]
  bb_004A0649[BB_004A0649]
  bb_004A05F4 -->|branch| bb_004A0635
  bb_004A05F4 -->|fallthrough| bb_004A0627
  bb_004A0627 -->|flow| bb_004A0635
  bb_004A0635 -->|branch| bb_004A063E
  bb_004A0635 -->|fallthrough| bb_004A063A
  bb_004A063A -->|flow| bb_004A063E
```
