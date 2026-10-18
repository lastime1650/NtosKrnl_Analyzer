# ZwNotifyChangeKey

- RVA: `0x006AF550`–`0x006AF56F` (길이 `31` bytes)
- VA: `0x00000001406AF550`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0C40`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CcRegistryChangeCallback](../57/CcRegistryChangeCallback_function_0057CC20.md) at `0x0057CD4D`
- [CcSetupWatchForRegistryChanges](../57/CcSetupWatchForRegistryChanges_function_0057CE10.md) at `0x0057CEEE`
- [PspReadDfssConfigurationValues](../5E/PspReadDfssConfigurationValues_function_005E2508.md) at `0x005E26C0`
- [DifZwNotifyChangeKeyWrapper](../64/DifZwNotifyChangeKeyWrapper_function_006431E0.md) at `0x0064332B`
- [IopRegistryInitializeCallbacks](../../page/72/IopRegistryInitializeCallbacks_function_00722E58.md) at `0x00722F20`
- [PipUpdateAsyncOptionsCallback](../../page/72/PipUpdateAsyncOptionsCallback_function_00723740.md) at `0x007237D9`
- [PipUpdateSetupInProgressNotify](../../page/72/PipUpdateSetupInProgressNotify_function_00723918.md) at `0x0072397C`
- [PfpParametersWatcher](../../page/75/PfpParametersWatcher_function_00753140.md) at `0x007531D2`
- [PfpParametersWatcher](../../page/75/PfpParametersWatcher_function_00753140.md) at `0x00753295`
- [PopUpdateDeviceFamily](../../page/75/PopUpdateDeviceFamily_function_007546D0.md) at `0x0075483D`
- [PopUpdateUpgradeInProgress](../../page/75/PopUpdateUpgradeInProgress_function_00754880.md) at `0x007549E8`
- [PopPowerButtonBugcheckConfigure](../../page/76/PopPowerButtonBugcheckConfigure_function_00768F84.md) at `0x00768FDD`
- [ExpReadLeapSecondData](../../page/7C/ExpReadLeapSecondData_function_007C5EAC.md) at `0x007C5FD7`
- [IopRegistryCallback](../../page/A9/IopRegistryCallback_function_00A95FD0.md) at `0x00A960C7`
- [sub_00B478B4](../../page/B4/Unknown_function_00B478B4.md) at `0x00B47905`
- [PfInitializeSuperfetch](../../init/C3/PfInitializeSuperfetch_function_00C3CACC.md) at `0x00C3CC76`

### Static image references
- `0x006AF55C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AF569` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AF550  48 8B C4                        mov rax, rsp
006AF553  FA                              cli
006AF554  48 83 EC 10                     sub rsp, 0x10
006AF558  50                              push rax
006AF559  9C                              pushfq
006AF55A  6A 10                           push 0x10
006AF55C  48 8D 05 FD 3E 00 00            lea rax, [rip + 0x3efd]
006AF563  50                              push rax
006AF564  B8 24 01 00 00                  mov eax, 0x124
006AF569  E9 52 54 01 00                  jmp 0x1406c49c0
006AF56E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwNotifyChangeKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwNotifyChangeKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AF550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AF550[BB_006AF550]
  bb_006AF56E[BB_006AF56E]
```
