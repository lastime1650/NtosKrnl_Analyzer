# ZwQueryKey

- RVA: `0x006AD390`–`0x006AD3AF` (길이 `31` bytes)
- VA: `0x00000001406AD390`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFF98`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **28**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BiOpenStoreKeyFromObject](../4B/BiOpenStoreKeyFromObject_function_004B1D14.md) at `0x004B1D7D`
- [BiZwQueryKey](../4B/BiZwQueryKey_function_004B2384.md) at `0x004B2392`
- [HalpMcEnumerateAndSetPatchConfig](../55/HalpMcEnumerateAndSetPatchConfig_function_0055AB38.md) at `0x0055AC12`
- [PipIs32bitKey](../5A/PipIs32bitKey_function_005A45F0.md) at `0x005A4636`
- [DifZwQueryKeyWrapper](../64/DifZwQueryKeyWrapper_function_00647ED0.md) at `0x00647FDA`
- [PipCallbackHasDeviceOverrides](../../page/72/PipCallbackHasDeviceOverrides_function_007231D4.md) at `0x00723248`
- [PiDrvDbOverlayCopyKeys](../../page/74/PiDrvDbOverlayCopyKeys_function_007413FC.md) at `0x007414CF`
- [KsepRegistryQueryKeyInformation](../../page/74/KsepRegistryQueryKeyInformation_function_0074B498.md) at `0x0074B4D5`
- [KsepRegistryQueryKeyInformation](../../page/74/KsepRegistryQueryKeyInformation_function_0074B498.md) at `0x0074B51A`
- [SepLoadNgenLocations](../../page/79/SepLoadNgenLocations_function_0079BCCC.md) at `0x0079BD86`
- [SepReadAndInsertCaps](../../page/7A/SepReadAndInsertCaps_function_007A3960.md) at `0x007A39FD`
- [SepReadAndInsertCaps](../../page/7A/SepReadAndInsertCaps_function_007A3960.md) at `0x007A3A4B`
- [SepReadAndInsertCaps](../../page/7A/SepReadAndInsertCaps_function_007A3960.md) at `0x007A3B62`
- [SepReadAndInsertCaps](../../page/7A/SepReadAndInsertCaps_function_007A3960.md) at `0x007A3BB6`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3D2E`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3D96`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3E61`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3ED9`
- [EtwpRemoveMicroarchitecturalPmcFromPmcGroup](../../page/7B/EtwpRemoveMicroarchitecturalPmcFromPmcGroup_function_007B7844.md) at `0x007B7A4D`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E335F`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E3E5E`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E423A`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E470C`
- [RegRtlCopyTreeInternal](../../page/83/RegRtlCopyTreeInternal_function_008324C0.md) at `0x008325B0`
- [RtlpValidateKeyTrust](../../page/8B/RtlpValidateKeyTrust_function_008BE114.md) at `0x008BE14C`
- [RegRtlQueryInfoKey](../../page/99/RegRtlQueryInfoKey_function_0099463C.md) at `0x00994696`
- [IopGetRegistryKeyInformation](../../page/99/IopGetRegistryKeyInformation_function_009972C0.md) at `0x009972ED`
- [IopGetRegistryKeyInformation](../../page/99/IopGetRegistryKeyInformation_function_009972C0.md) at `0x00997345`
- [IopGetDriverNameFromKeyNode](../../page/99/IopGetDriverNameFromKeyNode_function_00998808.md) at `0x009988D7`
- [IopGetDriverNameFromKeyNode](../../page/99/IopGetDriverNameFromKeyNode_function_00998808.md) at `0x009989EF`
- [IopApplyMutableTagToRegistryKey](../../page/99/IopApplyMutableTagToRegistryKey_function_00999364.md) at `0x00999395`
- [PiNormalizeDeviceText](../../page/99/PiNormalizeDeviceText_function_0099A43C.md) at `0x0099A5DB`
- [PiNormalizeDeviceText](../../page/99/PiNormalizeDeviceText_function_0099A43C.md) at `0x0099A622`
- [PiRearrangeDeviceInstances](../../page/99/PiRearrangeDeviceInstances_function_0099AF9C.md) at `0x0099AFF8`
- [DrvDbGetObjectSubKeyCallback](../../page/A1/DrvDbGetObjectSubKeyCallback_function_00A11300.md) at `0x00A11439`
- [sub_00B246DA](../../page/B2/Unknown_function_00B246DA.md) at `0x00B24801`
- [HalpInitChipHacks](../../init/C2/HalpInitChipHacks_function_00C24274.md) at `0x00C2433D`
- [PipInitDeviceOverrideCache](../../init/C3/PipInitDeviceOverrideCache_function_00C312C8.md) at `0x00C31382`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C713DF`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C71443`

### Static image references
- `0x006AD39C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD3A9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD390  48 8B C4                        mov rax, rsp
006AD393  FA                              cli
006AD394  48 83 EC 10                     sub rsp, 0x10
006AD398  50                              push rax
006AD399  9C                              pushfq
006AD39A  6A 10                           push 0x10
006AD39C  48 8D 05 BD 60 00 00            lea rax, [rip + 0x60bd]
006AD3A3  50                              push rax
006AD3A4  B8 16 00 00 00                  mov eax, 0x16
006AD3A9  E9 12 76 01 00                  jmp 0x1406c49c0
006AD3AE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwQueryKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwQueryKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD390[BB_006AD390]
  bb_006AD3AE[BB_006AD3AE]
```
