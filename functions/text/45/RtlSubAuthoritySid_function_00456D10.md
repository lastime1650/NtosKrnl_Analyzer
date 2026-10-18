# RtlSubAuthoritySid

- RVA: `0x00456D10`–`0x00456D1C` (길이 `12` bytes)
- VA: `0x0000000140456D10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **34**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlIsParentOfChildAppContainer](../../page/70/RtlIsParentOfChildAppContainer_function_007047CC.md) at `0x00704825`
- [RtlIsParentOfChildAppContainer](../../page/70/RtlIsParentOfChildAppContainer_function_007047CC.md) at `0x00704832`
- [PiAuCheckClientInteractive](../../page/73/PiAuCheckClientInteractive_function_00731284.md) at `0x007312EE`
- [PopCreateHiberFileSecurityDescriptor](../../page/75/PopCreateHiberFileSecurityDescriptor_function_0075D3DC.md) at `0x0075D43F`
- [RtlGetAppContainerParent](../../page/78/RtlGetAppContainerParent_function_0078E4A0.md) at `0x0078E52A`
- [RtlpGetTokenNamedObjectPath](../../page/78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078F046`
- [RtlpGetTokenNamedObjectPath](../../page/78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078F056`
- [RtlpGetTokenNamedObjectPath](../../page/78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078F066`
- [RtlpGetTokenNamedObjectPath](../../page/78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078F076`
- [InitializeSidLookupTable](../../page/7A/InitializeSidLookupTable_function_007A4B90.md) at `0x007A4C68`
- [InitializeSidLookupTable](../../page/7A/InitializeSidLookupTable_function_007A4B90.md) at `0x007A4C8B`
- [InitializeSidLookupTable](../../page/7A/InitializeSidLookupTable_function_007A4B90.md) at `0x007A4C9E`
- [InitializeSidLookupTable](../../page/7A/InitializeSidLookupTable_function_007A4B90.md) at `0x007A4CC1`
- [InitializeSidLookupTable](../../page/7A/InitializeSidLookupTable_function_007A4B90.md) at `0x007A4CEA`
- [InitializeSidLookupTable](../../page/7A/InitializeSidLookupTable_function_007A4B90.md) at `0x007A4D23`
- [SmKmStoreFileMakeSecurityDescriptor](../../page/7A/SmKmStoreFileMakeSecurityDescriptor_function_007A9988.md) at `0x007A9A8E`
- [SmKmStoreFileMakeSecurityDescriptor](../../page/7A/SmKmStoreFileMakeSecurityDescriptor_function_007A9988.md) at `0x007A9A9A`
- [SmKmStoreFileMakeSecurityDescriptor](../../page/7A/SmKmStoreFileMakeSecurityDescriptor_function_007A9988.md) at `0x007A9AAA`
- [SmKmStoreFileMakeSecurityDescriptor](../../page/7A/SmKmStoreFileMakeSecurityDescriptor_function_007A9988.md) at `0x007A9ABD`
- [NtSetUuidSeed](../../page/7D/NtSetUuidSeed_function_007D0DD0.md) at `0x007D0EF2`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2BF7`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2C44`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2C57`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2C6C`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2C7D`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2C8E`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2C9F`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2D08`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2D1D`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2D73`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2D85`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2DDC`
- [CMFCreateSecurityDescriptor](../../page/7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D2DEF`
- [CmpAdminSystemSecurityDescriptor](../../page/7E/CmpAdminSystemSecurityDescriptor_function_007EBED8.md) at `0x007EBF82`
- [CmpAdminSystemSecurityDescriptor](../../page/7E/CmpAdminSystemSecurityDescriptor_function_007EBED8.md) at `0x007EBF92`
- [CmpAdminSystemSecurityDescriptor](../../page/7E/CmpAdminSystemSecurityDescriptor_function_007EBED8.md) at `0x007EBFA5`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED27D`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED289`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED299`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED2A9`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED2BA`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED2CA`
- [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) at `0x007ED2DB`
- [PnpGetEnumSecurityDescriptor](../../page/83/PnpGetEnumSecurityDescriptor_function_00831FCC.md) at `0x00832045`
- [PnpGetEnumSecurityDescriptor](../../page/83/PnpGetEnumSecurityDescriptor_function_00831FCC.md) at `0x0083207F`
- [PnpGetEnumSecurityDescriptor](../../page/83/PnpGetEnumSecurityDescriptor_function_00831FCC.md) at `0x008320B9`
- [PnpGetEnumSecurityDescriptor](../../page/83/PnpGetEnumSecurityDescriptor_function_00831FCC.md) at `0x008320F3`
- [PnpGetEnumSecurityDescriptor](../../page/83/PnpGetEnumSecurityDescriptor_function_00831FCC.md) at `0x00832105`
- [DrvDbGetSecurityDescriptor](../../page/83/DrvDbGetSecurityDescriptor_function_0083580C.md) at `0x0083589F`
- [DrvDbGetSecurityDescriptor](../../page/83/DrvDbGetSecurityDescriptor_function_0083580C.md) at `0x008358EF`
- [DrvDbGetSecurityDescriptor](../../page/83/DrvDbGetSecurityDescriptor_function_0083580C.md) at `0x0083593F`
- [DrvDbGetSecurityDescriptor](../../page/83/DrvDbGetSecurityDescriptor_function_0083580C.md) at `0x00835995`
- [DrvDbGetSecurityDescriptor](../../page/83/DrvDbGetSecurityDescriptor_function_0083580C.md) at `0x008359A6`
- [SeQueryInformationToken](../../page/8B/SeQueryInformationToken_function_008B5090.md) at `0x008B56FE`
- [SeQueryMandatoryLabel](../../page/8C/SeQueryMandatoryLabel_function_008C8D38.md) at `0x008C8DA6`
- [SysCtxRegOpenCurrentUserKey](../../page/8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) at `0x008F46A7`
- [sub_0092949C](../../page/92/Unknown_function_0092949C.md) at `0x009295DD`
- [sub_00929657](../../page/92/Unknown_function_00929657.md) at `0x00929687`
- [RtlpNewSecurityObject](../../page/92/RtlpNewSecurityObject_function_0092AB50.md) at `0x0092C438`
- [RtlpNewSecurityObject](../../page/92/RtlpNewSecurityObject_function_0092AB50.md) at `0x0092C5C9`
- [SepCopyTokenLoggingInformation](../../page/9A/SepCopyTokenLoggingInformation_function_009A8618.md) at `0x009A86AF`
- [ObpVerifyCreatorAccessCheck](../../page/9C/ObpVerifyCreatorAccessCheck_function_009CA524.md) at `0x009CA5ED`
- [RtlIsElevatedRid](../../page/9D/RtlIsElevatedRid_function_009D4B30.md) at `0x009D4B5F`
- [RtlIsElevatedRid](../../page/9D/RtlIsElevatedRid_function_009D4B30.md) at `0x009D4B74`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A204D1`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A2052F`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A2067D`
- [_CmGetRegKeySecurityDescriptor](../../page/A8/_CmGetRegKeySecurityDescriptor_function_00A83F34.md) at `0x00A83FB2`
- [_CmGetRegKeySecurityDescriptor](../../page/A8/_CmGetRegKeySecurityDescriptor_function_00A83F34.md) at `0x00A83FE8`
- [_CmGetRegKeySecurityDescriptor](../../page/A8/_CmGetRegKeySecurityDescriptor_function_00A83F34.md) at `0x00A8401B`
- [_CmGetRegKeySecurityDescriptor](../../page/A8/_CmGetRegKeySecurityDescriptor_function_00A83F34.md) at `0x00A8402F`
- [_CmGetRegKeySecurityDescriptor](../../page/A8/_CmGetRegKeySecurityDescriptor_function_00A83F34.md) at `0x00A841D2`
- [_CmGetRegKeySecurityDescriptor](../../page/A8/_CmGetRegKeySecurityDescriptor_function_00A83F34.md) at `0x00A841E6`
- [_PnpGetPropertiesSecurityDescriptor](../../page/A9/_PnpGetPropertiesSecurityDescriptor_function_00A91B8C.md) at `0x00A91BCA`
- [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4B75`
- [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4BB9`
- [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4BCD`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AAD845`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADB81`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADB92`
- [ExpFirmwareAccessAppContainerCheck](../../page/AB/ExpFirmwareAccessAppContainerCheck_function_00AB7AFC.md) at `0x00AB7CA8`
- [ExpFirmwareAccessAppContainerCheck](../../page/AB/ExpFirmwareAccessAppContainerCheck_function_00AB7AFC.md) at `0x00AB7CBD`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9F74`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9FEB`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA0DA`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE8CA`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1999`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1A22`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1A79`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1AD8`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1B51`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1BD2`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1C52`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1D8D`
- [sub_00B1E93A](../../page/B1/Unknown_function_00B1E93A.md) at `0x00B1E9B7`
- [sub_00B1E93A](../../page/B1/Unknown_function_00B1E93A.md) at `0x00B1E9C7`
- [sub_00B1E93A](../../page/B1/Unknown_function_00B1E93A.md) at `0x00B1E9D7`
- [sub_00B1E93A](../../page/B1/Unknown_function_00B1E93A.md) at `0x00B1E9E7`
- [sub_00B37578](../../page/B3/Unknown_function_00B37578.md) at `0x00B3759A`
- [sub_00B37784](../../page/B3/Unknown_function_00B37784.md) at `0x00B377CE`
- [sub_00B37784](../../page/B3/Unknown_function_00B37784.md) at `0x00B377E2`
- [sub_00B37784](../../page/B3/Unknown_function_00B37784.md) at `0x00B37827`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00456D10  8B C2                           mov eax, edx
00456D12  48 83 C0 02                     add rax, 2
00456D16  48 8D 04 81                     lea rax, [rcx + rax*4]
00456D1A  C3                              ret
00456D1B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlSubAuthoritySid(__int64 a1, int a2)
{
    __int64 result;

    result = ((unsigned int)(a2)) + (2);
    return a1 + result * 4;
}
```

## 5. (Beta) C Style

```c
int64_t RtlSubAuthoritySid(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = ((uint32_t)(Arg2)) + (2);
    return Arg1 + result * 4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00456D10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00456D10[BB_00456D10]
  bb_00456D1B[BB_00456D1B]
```
