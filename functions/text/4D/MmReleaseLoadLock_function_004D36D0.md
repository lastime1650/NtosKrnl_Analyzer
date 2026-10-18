# MmReleaseLoadLock

- RVA: `0x004D36D0`–`0x004D36F4` (길이 `36` bytes)
- VA: `0x00000001404D36D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **29**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004D36DE` → [MiReleaseLoadLock](../2A/MiReleaseLoadLock_function_002A3CD0.md) (function, `0x002A3CD0`)

### Direct callers
- [ViAddVerifierSpecialThunks](../61/ViAddVerifierSpecialThunks_function_0061233C.md) at `0x00612404`
- [ViAddVerifierSpecialThunks](../61/ViAddVerifierSpecialThunks_function_0061233C.md) at `0x00612423`
- [ViAddVerifierSpecialThunks](../61/ViAddVerifierSpecialThunks_function_0061233C.md) at `0x0061242F`
- [ViAddVerifierThunks](../61/ViAddVerifierThunks_function_0061245C.md) at `0x0061254B`
- [ViAddVerifierThunks](../61/ViAddVerifierThunks_function_0061245C.md) at `0x00612557`
- [VfDriverRemoveAllDifVerification](../61/VfDriverRemoveAllDifVerification_function_006130E4.md) at `0x00613161`
- [MiProtectDriverSectionPte](../67/MiProtectDriverSectionPte_function_006706C0.md) at `0x00670778`
- [MiFlushDeferredRetpolineImageLoadEvents](../../page/80/MiFlushDeferredRetpolineImageLoadEvents_function_00801540.md) at `0x008015AA`
- [MiLogHotPatchRundown](../../page/80/MiLogHotPatchRundown_function_008057A4.md) at `0x00805E0C`
- [MmInsertSecureImageActivePatch](../../page/80/MmInsertSecureImageActivePatch_function_008073E4.md) at `0x00807492`
- [MmRemoveSecureImageActivePatch](../../page/80/MmRemoveSecureImageActivePatch_function_0080760C.md) at `0x00807685`
- [MmLoadSystemImageEx](../../page/99/MmLoadSystemImageEx_function_00999B8C.md) at `0x00999D13`
- [MiObtainSectionForDriver](../../page/A2/MiObtainSectionForDriver_function_00A24494.md) at `0x00A24650`
- [MiMarkRetpolineBits](../../page/AA/MiMarkRetpolineBits_function_00AA0394.md) at `0x00AA0459`
- [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA305E`
- [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA3474`
- [MiLoadHotPatch](../../page/AB/MiLoadHotPatch_function_00AB521C.md) at `0x00AB5588`
- [MiLoadHotPatch](../../page/AB/MiLoadHotPatch_function_00AB521C.md) at `0x00AB55E9`
- [MiLogStrongCodeDriverLoadFailure](../../page/AC/MiLogStrongCodeDriverLoadFailure_function_00AC2E6C.md) at `0x00AC3027`
- [MiQueryProcessActivePatches](../../page/AC/MiQueryProcessActivePatches_function_00AC6164.md) at `0x00AC67E1`
- [MiProcessKernelCfgAddressTakenImports](../../page/AD/MiProcessKernelCfgAddressTakenImports_function_00AD4384.md) at `0x00AD43D9`
- [MiShutdownSystem](../../pagelk/B7/MiShutdownSystem_function_00B73934.md) at `0x00B73AF8`
- [VfDriverEnableDisableVerifier](../../pagevrfy/B9/VfDriverEnableDisableVerifier_function_00B9A1B0.md) at `0x00B9A217`
- [VfDriverEnableVerifierForAll](../../pagevrfy/B9/VfDriverEnableVerifierForAll_function_00B9A3A4.md) at `0x00B9A44D`
- [ViDriverReApplyVerifierForAll](../../pagevrfy/B9/ViDriverReApplyVerifierForAll_function_00B9A8D4.md) at `0x00B9A977`
- [VfAddVerifierEntry](../../pagevrfy/BA/VfAddVerifierEntry_function_00BAC31C.md) at `0x00BAC3ED`
- [VfAddVerifierEntry](../../pagevrfy/BA/VfAddVerifierEntry_function_00BAC31C.md) at `0x00BAC42C`
- [MiFlushStrongCodeDriverLoadFailures](../../init/C6/MiFlushStrongCodeDriverLoadFailures_function_00C61680.md) at `0x00C617E7`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C6789E`
- [MmRegisterHotPatches](../../init/C6/MmRegisterHotPatches_function_00C678DC.md) at `0x00C67C7F`
- [MiBuildImportsForBootDrivers](../../init/C6/MiBuildImportsForBootDrivers_function_00C6B2E8.md) at `0x00C6B5A7`
- [MiInitializeLoadedModuleList](../../init/C6/MiInitializeLoadedModuleList_function_00C6BCDC.md) at `0x00C6BE07`
- [MiReloadBootLoadedDrivers](../../init/C6/MiReloadBootLoadedDrivers_function_00C6C3F8.md) at `0x00C6C45C`
- [PipInitializeCoreDriversAndElam](../../init/C7/PipInitializeCoreDriversAndElam_function_00C73F84.md) at `0x00C73FF6`
- [PipInitializeDriverDependentDLLs](../../init/C7/PipInitializeDriverDependentDLLs_function_00C74398.md) at `0x00C7450D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D36D0  48 83 EC 28                     sub rsp, 0x28
004D36D4  48 85 C9                        test rcx, rcx
004D36D7  74 10                           je 0x1404d36e9
004D36D9  BA 01 00 00 00                  mov edx, 1
004D36DE  E8 ED 05 DD FF                  call 0x1402a3cd0
004D36E3  48 83 C4 28                     add rsp, 0x28
004D36E7  C3                              ret
004D36E8  CC                              int3
004D36E9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004D36F2  EB E5                           jmp 0x1404d36d9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmReleaseLoadLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_004D36E9;
loc_004D36D9:
    result = MiReleaseLoadLock(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_004D36E9:
    goto loc_004D36D9;
}
```

## 5. (Beta) C Style

```c
int64_t MmReleaseLoadLock(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_004D36E9;
loc_004D36D9:
    result = MiReleaseLoadLock(Arg1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_004D36E9:
    goto loc_004D36D9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D36D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D36D0[BB_004D36D0]
  bb_004D36D9[BB_004D36D9]
  bb_004D36E8[BB_004D36E8]
  bb_004D36E9[BB_004D36E9]
  bb_004D36D0 -->|branch| bb_004D36E9
  bb_004D36D0 -->|fallthrough| bb_004D36D9
  bb_004D36E8 -->|flow| bb_004D36E9
  bb_004D36E9 -->|branch| bb_004D36D9
```
