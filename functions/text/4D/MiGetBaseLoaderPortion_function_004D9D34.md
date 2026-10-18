# MiGetBaseLoaderPortion

- RVA: `0x004D9D34`–`0x004D9D39` (길이 `5` bytes)
- VA: `0x00000001404D9D34`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `5/5` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **24**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiDriverLoadSucceeded](../../page/70/MiDriverLoadSucceeded_function_00702F08.md) at `0x00702F27`
- [MiApplyRequiredDriverHotPatches](../../page/70/MiApplyRequiredDriverHotPatches_function_007053D4.md) at `0x007053F3`
- [MiUnloadApproved](../../page/7F/MiUnloadApproved_function_007F82A0.md) at `0x007F82CE`
- [MiBackSingleImageWithPagefile](../../page/7F/MiBackSingleImageWithPagefile_function_007F8664.md) at `0x007F86CA`
- [MiBackSystemImageWithPagefile](../../page/7F/MiBackSystemImageWithPagefile_function_007F86E8.md) at `0x007F8710`
- [MiSplitDriverPage](../../page/7F/MiSplitDriverPage_function_007F8EB8.md) at `0x007F8EE2`
- [MiApplyDriverHotPatch](../../page/80/MiApplyDriverHotPatch_function_008018EC.md) at `0x00801946`
- [MiApplyDriverHotPatch](../../page/80/MiApplyDriverHotPatch_function_008018EC.md) at `0x00801967`
- [MiApplyHotPatchToDriver](../../page/80/MiApplyHotPatchToDriver_function_00801E64.md) at `0x00801EB2`
- [MiApplyHotPatchToLoadedDriver](../../page/80/MiApplyHotPatchToLoadedDriver_function_00802078.md) at `0x00802139`
- [MiApplyHotPatchToLoadedDriver](../../page/80/MiApplyHotPatchToLoadedDriver_function_00802078.md) at `0x008021D6`
- [MiIsActiveSystemHotPatch](../../page/80/MiIsActiveSystemHotPatch_function_008045D8.md) at `0x008045DF`
- [MiIsActiveSystemHotPatch](../../page/80/MiIsActiveSystemHotPatch_function_008045D8.md) at `0x008045FC`
- [MiLogHotPatchRundown](../../page/80/MiLogHotPatchRundown_function_008057A4.md) at `0x00805CD4`
- [MmLoadSystemImageEx](../../page/99/MmLoadSystemImageEx_function_00999B8C.md) at `0x00999CAD`
- [MmLoadSystemImageEx](../../page/99/MmLoadSystemImageEx_function_00999B8C.md) at `0x00999F22`
- [MmLoadSystemImageEx](../../page/99/MmLoadSystemImageEx_function_00999B8C.md) at `0x0099A118`
- [MiResolveImageReferences](../../page/A2/MiResolveImageReferences_function_00A23BE4.md) at `0x00A23DDA`
- [MiObtainSectionForDriver](../../page/A2/MiObtainSectionForDriver_function_00A24494.md) at `0x00A24501`
- [MiObtainSectionForDriver](../../page/A2/MiObtainSectionForDriver_function_00A24494.md) at `0x00A245F9`
- [MiGetSystemAddressForImage](../../page/A7/MiGetSystemAddressForImage_function_00A74EEC.md) at `0x00A74FB7`
- [MiUnlockDriverCode](../../page/A9/MiUnlockDriverCode_function_00A9FFEC.md) at `0x00AA0011`
- [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA301C`
- [MiReturnSystemImageCommitment](../../page/AA/MiReturnSystemImageCommitment_function_00AA6BE8.md) at `0x00AA6BEF`
- [MiLockdownSections](../../page/AA/MiLockdownSections_function_00AAA788.md) at `0x00AAA7BC`
- [MiFreeRetpolineImportInfo](../../page/AA/MiFreeRetpolineImportInfo_function_00AAFF1C.md) at `0x00AAFFC8`
- [MiInitializeImageSectionLocks](../../page/AB/MiInitializeImageSectionLocks_function_00AB8EDC.md) at `0x00AB8EF4`
- [MiQueryProcessActivePatches](../../page/AC/MiQueryProcessActivePatches_function_00AC6164.md) at `0x00AC66D3`
- [MiEnumerateBasePatches](../../pagelk/B7/MiEnumerateBasePatches_function_00B74B38.md) at `0x00B74B52`
- [MiEnumerateBasePatches](../../pagelk/B7/MiEnumerateBasePatches_function_00B74B38.md) at `0x00B74B6A`
- [MiMarkHotPatchesForHiberPhase](../../pagelk/B7/MiMarkHotPatchesForHiberPhase_function_00B74C10.md) at `0x00B74C22`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D9D34  48 8B C1                        mov rax, rcx
004D9D37  C3                              ret
004D9D38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetBaseLoaderPortion(__int64 a1)
{
    return a1;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetBaseLoaderPortion(int64_t Arg1)
{
    return Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D9D34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D9D34[BB_004D9D34]
  bb_004D9D38[BB_004D9D38]
```
