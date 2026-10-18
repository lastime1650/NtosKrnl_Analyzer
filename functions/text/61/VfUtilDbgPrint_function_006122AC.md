# VfUtilDbgPrint

- RVA: `0x006122AC`–`0x006122EC` (길이 `64` bytes)
- VA: `0x00000001406122AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CF7BC`
- 디코드: `17`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **32**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006122E1` → [vDbgPrintExWithPrefixInternal](../35/vDbgPrintExWithPrefixInternal_function_00359314.md) (function, `0x00359314`)

### Direct callers
- [VfDifCaptureIoCallbacks](../4A/VfDifCaptureIoCallbacks_function_004A8698.md) at `0x004A86EB`
- [VfDifCaptureDriverEntry](../4A/VfDifCaptureDriverEntry_function_004A86F8.md) at `0x004A8754`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00611EC1`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00611EF7`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00611F2D`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00611F63`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00611FA2`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00611FD8`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x0061200E`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x0061204D`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00612083`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x006120B9`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x006120EF`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00612125`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x0061215B`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00612179`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x00612189`
- [VfClearVerifierSettings](VfClearVerifierSettings_function_00611DB0.md) at `0x006121A2`
- [VfReportIssueWithOptions](VfReportIssueWithOptions_function_00614444.md) at `0x006144C6`
- [ViErrorReport1](ViErrorReport1_function_00614584.md) at `0x006145D2`
- [ViErrorReport10](ViErrorReport10_function_00614608.md) at `0x00614662`
- [ViErrorReport4](ViErrorReport4_function_0061469C.md) at `0x00614705`
- [ViErrorReport6](ViErrorReport6_function_00614740.md) at `0x00614799`
- [VfNotifyVerifierOfEvent](../../pagevrfy/B9/VfNotifyVerifierOfEvent_function_00B92E90.md) at `0x00B92EEA`
- [VfNotifyVerifierOfEvent](../../pagevrfy/B9/VfNotifyVerifierOfEvent_function_00B92E90.md) at `0x00B92F00`
- [VfNotifyVerifierOfEvent](../../pagevrfy/B9/VfNotifyVerifierOfEvent_function_00B92E90.md) at `0x00B92FA8`
- [VfUtilPrintCheckinString](../../pagevrfy/B9/VfUtilPrintCheckinString_function_00B934D4.md) at `0x00B93658`
- [VfUtilPrintCheckinString](../../pagevrfy/B9/VfUtilPrintCheckinString_function_00B934D4.md) at `0x00B936A0`
- [VfUtilPrintCheckinString](../../pagevrfy/B9/VfUtilPrintCheckinString_function_00B934D4.md) at `0x00B936B8`
- [VfUtilPrintCheckinString](../../pagevrfy/B9/VfUtilPrintCheckinString_function_00B934D4.md) at `0x00B936DF`
- [ViGenericDumpIrpStack](../../pagevrfy/B9/ViGenericDumpIrpStack_function_00B93EE0.md) at `0x00B93F1F`
- [ViGenericVerifyIrpStackDownward](../../pagevrfy/B9/ViGenericVerifyIrpStackDownward_function_00B93F90.md) at `0x00B9408D`
- [ViGenericVerifyNewIrp](../../pagevrfy/B9/ViGenericVerifyNewIrp_function_00B94260.md) at `0x00B94320`
- [ViAdapterCallback](../../pagevrfy/B9/ViAdapterCallback_function_00B97B40.md) at `0x00B97C0C`
- [ViAdapterCallback](../../pagevrfy/B9/ViAdapterCallback_function_00B97B40.md) at `0x00B97C18`
- [ViFlushDoubleBuffer](../../pagevrfy/B9/ViFlushDoubleBuffer_function_00B989D0.md) at `0x00B98B5B`
- [ViHalPreprocessOptions](../../pagevrfy/B9/ViHalPreprocessOptions_function_00B9920C.md) at `0x00B99265`
- [ViHalPreprocessOptions](../../pagevrfy/B9/ViHalPreprocessOptions_function_00B9920C.md) at `0x00B99271`
- [ViHalPreprocessOptions](../../pagevrfy/B9/ViHalPreprocessOptions_function_00B9920C.md) at `0x00B9927D`
- [ViHalPreprocessOptions](../../pagevrfy/B9/ViHalPreprocessOptions_function_00B9920C.md) at `0x00B992CA`
- [ViHalPreprocessOptions](../../pagevrfy/B9/ViHalPreprocessOptions_function_00B9920C.md) at `0x00B992D6`
- [ViHalPreprocessOptions](../../pagevrfy/B9/ViHalPreprocessOptions_function_00B9920C.md) at `0x00B992E2`
- [ViSpecialAllocateCommonBuffer](../../pagevrfy/B9/ViSpecialAllocateCommonBuffer_function_00B99BB0.md) at `0x00B99C1A`
- [ViXdvDriverLoadImage](../../pagevrfy/B9/ViXdvDriverLoadImage_function_00B9A9A0.md) at `0x00B9AAF7`
- [VfIoDeleteDevice](../../pagevrfy/BA/VfIoDeleteDevice_function_00BA221C.md) at `0x00BA2297`
- [VfIoDeleteDevice](../../pagevrfy/BA/VfIoDeleteDevice_function_00BA221C.md) at `0x00BA22EF`
- [VfIoDetachDevice](../../pagevrfy/BA/VfIoDetachDevice_function_00BA234C.md) at `0x00BA23A9`
- [VfErrorReport7](../../pagevrfy/BA/VfErrorReport7_function_00BA34B0.md) at `0x00BA350C`
- [VfErrorReport8](../../pagevrfy/BA/VfErrorReport8_function_00BA3548.md) at `0x00BA3599`
- [ViErrorDisplayDescription](../../pagevrfy/BA/ViErrorDisplayDescription_function_00BA361C.md) at `0x00BA362B`
- [ViErrorDisplayDescription](../../pagevrfy/BA/ViErrorDisplayDescription_function_00BA361C.md) at `0x00BA3658`
- [ViErrorFinishReport](../../pagevrfy/BA/ViErrorFinishReport_function_00BA366C.md) at `0x00BA3698`
- [ViDeadlockPreprocessOptions](../../pagevrfy/BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) at `0x00BA9C2F`
- [ViDeadlockPreprocessOptions](../../pagevrfy/BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) at `0x00BA9C3B`
- [ViDeadlockPreprocessOptions](../../pagevrfy/BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) at `0x00BA9C47`
- [ViDeadlockPreprocessOptions](../../pagevrfy/BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) at `0x00BA9C72`
- [ViDeadlockPreprocessOptions](../../pagevrfy/BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) at `0x00BA9C7E`
- [ViDeadlockPreprocessOptions](../../pagevrfy/BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) at `0x00BA9C8A`
- [VerifierNtCreateFile](../../pagevrfy/BB/VerifierNtCreateFile_function_00BB10A0.md) at `0x00BB1125`
- [VerifierNtReadFile](../../pagevrfy/BB/VerifierNtReadFile_function_00BB1250.md) at `0x00BB12ED`
- [VerifierNtWriteFile](../../pagevrfy/BB/VerifierNtWriteFile_function_00BB13A0.md) at `0x00BB143D`
- [ViCtxCheckAndReleaseIsrState](../../pagevrfy/BB/ViCtxCheckAndReleaseIsrState_function_00BB1F40.md) at `0x00BB1FC1`
- [ViCtxCheckAndReleaseIsrState](../../pagevrfy/BB/ViCtxCheckAndReleaseIsrState_function_00BB1F40.md) at `0x00BB1FE5`
- [VfPnpDumpIrpStack](../../pagevrfy/BB/VfPnpDumpIrpStack_function_00BB5310.md) at `0x00BB5357`
- [VfPnpDumpIrpStack](../../pagevrfy/BB/VfPnpDumpIrpStack_function_00BB5310.md) at `0x00BB53D6`
- [VfPnpDumpIrpStack](../../pagevrfy/BB/VfPnpDumpIrpStack_function_00BB5310.md) at `0x00BB54D8`
- [VfPowerDumpIrpStack](../../pagevrfy/BB/VfPowerDumpIrpStack_function_00BB5E00.md) at `0x00BB5E14`
- [VfPowerDumpIrpStack](../../pagevrfy/BB/VfPowerDumpIrpStack_function_00BB5E00.md) at `0x00BB5E30`
- [VfPowerDumpIrpStack](../../pagevrfy/BB/VfPowerDumpIrpStack_function_00BB5E00.md) at `0x00BB5E45`
- [VfPowerDumpIrpStack](../../pagevrfy/BB/VfPowerDumpIrpStack_function_00BB5E00.md) at `0x00BB5E78`
- [VfPowerDumpIrpStack](../../pagevrfy/BB/VfPowerDumpIrpStack_function_00BB5E00.md) at `0x00BB5E92`
- [VfPowerDumpIrpStack](../../pagevrfy/BB/VfPowerDumpIrpStack_function_00BB5E00.md) at `0x00BB5EB2`
- [VfWmiDumpIrpStack](../../pagevrfy/BB/VfWmiDumpIrpStack_function_00BB60C0.md) at `0x00BB60D0`
- [VfWmiDumpIrpStack](../../pagevrfy/BB/VfWmiDumpIrpStack_function_00BB60C0.md) at `0x00BB60FE`

### Static image references
- `0x006122D2` → RVA `0x006C7800` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006122AC  4C 8B DC                        mov r11, rsp
006122AF  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
006122B3  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
006122B7  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
006122BB  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
006122BF  48 83 EC 48                     sub rsp, 0x48
006122C3  45 33 C0                        xor r8d, r8d
006122C6  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
006122CB  49 8D 43 10                     lea rax, [r11 + 0x10]
006122CF  4C 8B C9                        mov r9, rcx
006122D2  48 8D 0D 27 55 0B 00            lea rcx, [rip + 0xb5527]
006122D9  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
006122DD  41 8D 50 65                     lea edx, [r8 + 0x65]
006122E1  E8 2E 70 D4 FF                  call 0x140359314
006122E6  48 83 C4 48                     add rsp, 0x48
006122EA  C3                              ret
006122EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfUtilDbgPrint(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (72);
    a3 = 0;
    v_stack_m20 = 1;
    *(unsigned __int64 *)(v_rsp - 40) = v_rsp + 16;
    result = vDbgPrintExWithPrefixInternal(v_rip + 742695, a3 + 101, a3, a1);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfUtilDbgPrint(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m20;

    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (72);
    Arg3 = 0;
    v_stack_m20 = 1;
    *(uint64_t *)(local_rsp - 0x28) = local_rsp + 16;
    result = vDbgPrintExWithPrefixInternal(v_rip + 742695, Arg3 + 101, Arg3, Arg1);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006122AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006122AC[BB_006122AC]
  bb_006122EB[BB_006122EB]
```
