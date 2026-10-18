# ZwEnumerateValueKey

- RVA: `0x006AD330`–`0x006AD34F` (길이 `31` bytes)
- VA: `0x00000001406AD330`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFF74`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DifZwEnumerateValueKeyWrapper](../64/DifZwEnumerateValueKeyWrapper_function_00641BA0.md) at `0x00641CB7`
- [PipApplyFunctionToServiceInstances](../../page/72/PipApplyFunctionToServiceInstances_function_0072BF40.md) at `0x0072C033`
- [PiDcInitUpdateProperties](../../page/73/PiDcInitUpdateProperties_function_00730B3C.md) at `0x00730C85`
- [PiDevCfgFindDeviceMigrationNode](../../page/73/PiDevCfgFindDeviceMigrationNode_function_00732920.md) at `0x00732AA8`
- [PiDevCfgQueryPolicyStringList](../../page/73/PiDevCfgQueryPolicyStringList_function_00735358.md) at `0x007354DC`
- [KsepRegistryEnumValue](../../page/74/KsepRegistryEnumValue_function_0074B24C.md) at `0x0074B288`
- [KsepRegistryEnumValue](../../page/74/KsepRegistryEnumValue_function_0074B24C.md) at `0x0074B2D4`
- [SepLoadNgenLocations](../../page/79/SepLoadNgenLocations_function_0079BCCC.md) at `0x0079BDE2`
- [SepLoadNgenLocations](../../page/79/SepLoadNgenLocations_function_0079BCCC.md) at `0x0079BEDE`
- [SdbpGetManifestedMergeStubAlloc](../../page/81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x008128F5`
- [SdbpGetManifestedMergeStubAlloc](../../page/81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x00812991`
- [RtlpPopulateLanguageConfigList](../../page/83/RtlpPopulateLanguageConfigList_function_0083EF20.md) at `0x0083EFD5`
- [RtlpMuiRegInitLIPLanguage](../../page/83/RtlpMuiRegInitLIPLanguage_function_0083F8D8.md) at `0x0083FA4C`
- [RtlpMuiRegPopulateBaseLanguages](../../page/83/RtlpMuiRegPopulateBaseLanguages_function_0083FC4C.md) at `0x0083FF65`
- [RtlpQueryRegistryValues](../../page/8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C930D`
- [RegRtlEnumValue](../../page/99/RegRtlEnumValue_function_0099369C.md) at `0x00993730`
- [PiDevCfgCopyDeviceKey](../../page/99/PiDevCfgCopyDeviceKey_function_00997374.md) at `0x009974B7`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A882C2`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A8830D`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44EE7`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44F75`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B45141`
- [HalpInitChipHacks](../../init/C2/HalpInitChipHacks_function_00C24274.md) at `0x00C243B9`
- [PiLastGoodCopyKeyContents](../../init/C3/PiLastGoodCopyKeyContents_function_00C336E4.md) at `0x00C3380B`
- [PiLastGoodRevertLastKnownDirectory](../../init/C3/PiLastGoodRevertLastKnownDirectory_function_00C33980.md) at `0x00C33B6B`
- [PopReadSimulatedProcessorClass](../../init/C4/PopReadSimulatedProcessorClass_function_00C41978.md) at `0x00C41AB8`
- [PsInitializeBootCpuPartitions](../../init/C4/PsInitializeBootCpuPartitions_function_00C44D94.md) at `0x00C4506C`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C71495`

### Static image references
- `0x006AD33C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD349` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD330  48 8B C4                        mov rax, rsp
006AD333  FA                              cli
006AD334  48 83 EC 10                     sub rsp, 0x10
006AD338  50                              push rax
006AD339  9C                              pushfq
006AD33A  6A 10                           push 0x10
006AD33C  48 8D 05 1D 61 00 00            lea rax, [rip + 0x611d]
006AD343  50                              push rax
006AD344  B8 13 00 00 00                  mov eax, 0x13
006AD349  E9 72 76 01 00                  jmp 0x1406c49c0
006AD34E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwEnumerateValueKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwEnumerateValueKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD330[BB_006AD330]
  bb_006AD34E[BB_006AD34E]
```
