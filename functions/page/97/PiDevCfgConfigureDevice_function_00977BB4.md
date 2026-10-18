# PiDevCfgConfigureDevice

- RVA: `0x00977BB4`–`0x0097A084` (길이 `9,424` bytes)
- VA: `0x0000000140977BB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096774`
- 디코드: `2,162`개 명령, `9,424/9,424` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **144**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **46**

### Outgoing calls
- `0x00977D52` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00977D7E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977D93` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977DA8` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977DC0` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977DCD` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977DDE` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977DF2` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E03` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E14` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E28` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E35` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E46` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E57` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E68` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E7D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00977E9A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00977EAA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00977EB8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00977EC6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00977EDF` → [PiDevCfgQueryDriverConfiguration](PiDevCfgQueryDriverConfiguration_function_0097584C.md) (function, `0x0097584C`)
- `0x00977F0D` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00977F2F` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00977F50` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00977F74` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00977F98` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00977FBC` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00977FE0` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00978021` → [PiDevCfgQueryDriverConfiguration](PiDevCfgQueryDriverConfiguration_function_0097584C.md) (function, `0x0097584C`)
- `0x00978098` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x009780C4` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x009780F3` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00978122` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00978151` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x0097819B` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x009781BC` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x009781EC` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00978297` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00978308` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00978376` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0097838C` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x009783C2` → [PnpOpenObjectRegKey](../8E/PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x009783DE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009784B5` → [PiDevCfgQueryObjectProperties](PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x009784EF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0097853E` → [PiDevCfgGetDeviceClassDriverConfigurable](../73/PiDevCfgGetDeviceClassDriverConfigurable_function_00733504.md) (function, `0x00733504`)
- `0x009785E3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0097868C` → [PiDevCfgQueryObjectProperties](PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x009786CD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00978707` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00978753` → [PiDevCfgQueryObjectProperties](PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00978770` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0097878B` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x009787AC` → [PiDevCfgEnforceDevicePolicy](../A8/PiDevCfgEnforceDevicePolicy_function_00A89454.md) (function, `0x00A89454`)
- `0x009787E9` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00978807` → [PiDevCfgVerifyDeviceAllowed](../96/PiDevCfgVerifyDeviceAllowed_function_009664E4.md) (function, `0x009664E4`)
- `0x0097887B` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009788F7` → [_CmDeleteDeviceRegKey](../A0/_CmDeleteDeviceRegKey_function_00A09A2C.md) (function, `0x00A09A2C`)
- `0x0097890E` → [_CmDeleteDeviceRegKey](../A0/_CmDeleteDeviceRegKey_function_00A09A2C.md) (function, `0x00A09A2C`)
- `0x0097892D` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x00978940` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x00978977` → [_CmDeleteDeviceRegKey](../A0/_CmDeleteDeviceRegKey_function_00A09A2C.md) (function, `0x00A09A2C`)
- `0x009789A8` → [PiDevCfgMigrateDevice](../96/PiDevCfgMigrateDevice_function_00963E60.md) (function, `0x00963E60`)
- `0x009789F9` → [PiDevCfgResetDeviceDriverSettings](../96/PiDevCfgResetDeviceDriverSettings_function_00966168.md) (function, `0x00966168`)
- `0x00978A0F` → [PnpCtxRegDeleteTree](../96/PnpCtxRegDeleteTree_function_00965CC8.md) (function, `0x00965CC8`)
- `0x00978A25` → [PnpCtxRegDeleteTree](../96/PnpCtxRegDeleteTree_function_00965CC8.md) (function, `0x00965CC8`)
- `0x00978A3B` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x00978A82` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978ACE` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978B48` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978BA7` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978BF0` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978C44` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978C91` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978CE0` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978D3A` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00978D88` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978DB2` → [PiDevCfgBuildIndirectString](PiDevCfgBuildIndirectString_function_0097A890.md) (function, `0x0097A890`)
- `0x00978E28` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00978E8F` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00978EDA` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978EE7` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00978F18` → [PiDevCfgBuildIndirectString](PiDevCfgBuildIndirectString_function_0097A890.md) (function, `0x0097A890`)
- `0x00978F6D` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978FD4` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00978FF1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00979040` → [PiDevCfgQueryObjectProperties](PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x009790A8` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009790F6` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979160` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x009791AA` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979201` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979259` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00979296` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (function, `0x0048B984`)
- `0x009792F8` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00979354` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x009793B0` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x009793CE` → [PiDevCfgBuildDriverNodeStrongName](PiDevCfgBuildDriverNodeStrongName_function_0097A33C.md) (function, `0x0097A33C`)
- `0x009793FE` → [RtlCompareUnicodeStrings](RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x0097940B` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0097945D` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x0097946D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x009794C9` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979507` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979545` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979583` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009795C1` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979627` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979676` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009796C9` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979718` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x0097976B` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009797BA` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x0097980D` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x0097985C` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009798AF` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009798FE` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979968` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x009799BF` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00979A15` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979A53` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979A97` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979AE6` → [PiDevCfgConfigureDeviceDriver](../96/PiDevCfgConfigureDeviceDriver_function_00963ABC.md) (function, `0x00963ABC`)
- `0x00979B37` → [PiDevCfgConfigureDeviceDriver](../96/PiDevCfgConfigureDeviceDriver_function_00963ABC.md) (function, `0x00963ABC`)
- `0x00979B72` → [PiDevCfgConfigureDeviceLocation](../AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) (function, `0x00AA88C0`)
- `0x00979BC4` → [PnpDeleteDeviceInterfaces](PnpDeleteDeviceInterfaces_function_0097A08C.md) (function, `0x0097A08C`)
- `0x00979BE6` → [PipIsDevNodeDNStarted](../../text/47/PipIsDevNodeDNStarted_function_00470870.md) (function, `0x00470870`)
- `0x00979C31` → [PiDevCfgConfigureDeviceKeys](../96/PiDevCfgConfigureDeviceKeys_function_00964BA8.md) (function, `0x00964BA8`)
- `0x00979C7B` → [PiDevCfgGetDeviceClassConfigFlags](../AC/PiDevCfgGetDeviceClassConfigFlags_function_00AC7248.md) (function, `0x00AC7248`)
- `0x00979CF9` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00979D50` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979D9F` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979DFA` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979E49` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979EA1` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979EEF` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979F46` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979F97` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00979FAC` → [PipHardwareConfigActivateService](../96/PipHardwareConfigActivateService_function_00965BFC.md) (function, `0x00965BFC`)
- `0x00979FC7` → [PipHardwareConfigActivateService](../96/PipHardwareConfigActivateService_function_00965BFC.md) (function, `0x00965BFC`)
- `0x00979FE2` → [PiDevCfgMakeServiceBootStart](../73/PiDevCfgMakeServiceBootStart_function_00733BC8.md) (function, `0x00733BC8`)
- `0x0097A020` → [PipHardwareConfigActivateService](../96/PipHardwareConfigActivateService_function_00965BFC.md) (function, `0x00965BFC`)
- `0x0097A03B` → [PiDevCfgMakeServiceBootStart](../73/PiDevCfgMakeServiceBootStart_function_00733BC8.md) (function, `0x00733BC8`)
- `0x0097A06B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDevCfgProcessDevice](PiDevCfgProcessDevice_function_00976D34.md) at `0x00976E6B`
- [sub_00B29934](../B2/Unknown_function_00B29934.md) at `0x00B29A53`

### Static image references
- `0x00977BD0` → RVA `0x00E0A740` (`.data`; read)
- `0x00978039` → RVA `0x00E0A9E0` (`.data`; read)
- `0x00978045` → RVA `0x00FD8030` (`PAGEDATA`; read)
- `0x00978246` → RVA `0x00FD80B4` (`PAGEDATA`; read)
- `0x00978254` → RVA `0x00FC4148` (`.data`; read)
- `0x009782B1` → RVA `0x00AFF1D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009782E4` → RVA `0x00AFF100` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0097839E` → RVA `0x00E66398` (`.data`; read)
- `0x009783E7` → RVA `0x00014410` (`.rdata`; read)
- `0x0097840F` → RVA `0x00022998` (`.rdata`; read)
- `0x0097843F` → RVA `0x00027CE0` (`.rdata`; read)
- `0x00978462` → RVA `0x00022900` (`.rdata`; read)
- `0x009785C5` → RVA `0x00011688` (`.rdata`; read)
- `0x009785FD` → RVA `0x000229C0` (`.rdata`; read)
- `0x0097862B` → RVA `0x00012F88` (`.rdata`; read)
- `0x009786D4` → RVA `0x00012FA0` (`.rdata`; read)
- `0x009787C6` → RVA `0x00AFE850` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00978866` → RVA `0x00014428` (`.rdata`; read)
- `0x00978A05` → RVA `0x00AFD740` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00978A1B` → RVA `0x00AFE870` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00978B1F` → RVA `0x0001E550` (`.rdata`; read)
- `0x00978BD2` → RVA `0x00014068` (`.rdata`; read)
- `0x00978C6C` → RVA `0x000140E0` (`.rdata`; read)
- `0x00978D0B` → RVA `0x00012E98` (`.rdata`; read)
- `0x00978DF9` → RVA `0x00014128` (`.rdata`; read)
- `0x00978E62` → RVA `0x00012FE8` (`.rdata`; read)
- `0x00978F4B` → RVA `0x00028118` (`.rdata`; read)
- `0x00978FFA` → RVA `0x00027C80` (`.rdata`; read)
- `0x00979131` → RVA `0x00012FD0` (`.rdata`; read)
- `0x00979240` → RVA `0x00012F58` (`.rdata`; read)
- `0x0097928B` → RVA `0x00AFE8B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009792DF` → RVA `0x00012FB8` (`.rdata`; read)
- `0x00979383` → RVA `0x00012F70` (`.rdata`; read)
- `0x00979602` → RVA `0x00022EE8` (`.rdata`; read)
- `0x009796A4` → RVA `0x00021600` (`.rdata`; read)
- `0x00979746` → RVA `0x00022418` (`.rdata`; read)
- `0x009797E8` → RVA `0x00023020` (`.rdata`; read)
- `0x0097988A` → RVA `0x000219F0` (`.rdata`; read)
- `0x00979935` → RVA `0x00013018` (`.rdata`; read)
- `0x00979991` → RVA `0x00013000` (`.rdata`; read)
- `0x00979CA0` → RVA `0x00B4AD08` (`PiDevCfgEmptyString`; read)
- `0x00979CE0` → RVA `0x00012EB0` (`.rdata`; read)
- `0x00979D32` → RVA `0x00027F08` (`.rdata`; read)
- `0x00979DD5` → RVA `0x000227C8` (`.rdata`; read)
- `0x00979E83` → RVA `0x00023218` (`.rdata`; read)
- `0x00979F23` → RVA `0x000142A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **40**
  - `0x00977D52` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00977D7E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977D93` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977DA8` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977DC0` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977DCD` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977DDE` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977DF2` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E03` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E14` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E28` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E35` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E46` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E57` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E68` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E7D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977E9A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00977EAA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00977EB8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00977EC6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00977F0D` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00977F2F` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00977F50` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00977F74` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00977F98` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00977FBC` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00977FE0` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00978297` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009783DE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009784EF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009785E3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009786CD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00978707` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00978770` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00978EE7` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00978FF1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00979296` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (`PAGE` → `.text`)
  - `0x0097946D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00979BE6` → [PipIsDevNodeDNStarted](../../text/47/PipIsDevNodeDNStarted_function_00470870.md) (`PAGE` → `.text`)
  - `0x0097A06B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00977BB4  40 55                           push rbp
00977BB6  53                              push rbx
00977BB7  56                              push rsi
00977BB8  57                              push rdi
00977BB9  41 54                           push r12
00977BBB  41 55                           push r13
00977BBD  41 56                           push r14
00977BBF  41 57                           push r15
00977BC1  48 8D AC 24 88 FD FF FF         lea rbp, [rsp - 0x278]
00977BC9  48 81 EC 78 03 00 00            sub rsp, 0x378
00977BD0  48 8B 05 69 2B 49 00            mov rax, qword ptr [rip + 0x492b69]
00977BD7  48 33 C4                        xor rax, rsp
00977BDA  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00977BE1  41 BA 00 04 00 00               mov r10d, 0x400
00977BE7  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00977BEB  48 8B FA                        mov rdi, rdx
00977BEE  45 89 11                        mov dword ptr [r9], r10d
00977BF1  48 8B D1                        mov rdx, rcx
00977BF4  4C 89 4D 30                     mov qword ptr [rbp + 0x30], r9
00977BF8  48 8B 8D E0 02 00 00            mov rcx, qword ptr [rbp + 0x2e0]
00977BFF  33 C0                           xor eax, eax
00977C01  49 8B F0                        mov rsi, r8
00977C04  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
00977C08  45 33 C0                        xor r8d, r8d
00977C0B  89 85 DC 00 00 00               mov dword ptr [rbp + 0xdc], eax
00977C11  0F 57 C0                        xorps xmm0, xmm0
00977C14  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
00977C18  44 89 01                        mov dword ptr [rcx], r8d
00977C1B  4C 8D 72 28                     lea r14, [rdx + 0x28]
00977C1F  4C 8B 7F 10                     mov r15, qword ptr [rdi + 0x10]
00977C23  41 8D 52 10                     lea edx, [r10 + 0x10]
00977C27  4C 89 45 58                     mov qword ptr [rbp + 0x58], r8
00977C2B  45 8B E0                        mov r12d, r8d
00977C2E  4C 89 45 48                     mov qword ptr [rbp + 0x48], r8
00977C32  B9 00 01 00 00                  mov ecx, 0x100
00977C37  4C 89 45 50                     mov qword ptr [rbp + 0x50], r8
00977C3B  45 8B EA                        mov r13d, r10d
00977C3E  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
00977C43  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
00977C48  4C 89 45 68                     mov qword ptr [rbp + 0x68], r8
00977C4C  4C 89 45 70                     mov qword ptr [rbp + 0x70], r8
00977C50  4C 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], r8
00977C57  4C 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], r8
00977C5E  4C 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], r8
00977C65  4C 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], r8
00977C6C  4C 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], r8
00977C73  4C 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], r8
00977C7A  4C 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], r8
00977C81  4C 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], r8
00977C88  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
00977C8C  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
00977C90  4C 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], r8
00977C97  4C 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], r8
00977C9E  44 89 45 94                     mov dword ptr [rbp - 0x6c], r8d
00977CA2  44 89 45 9C                     mov dword ptr [rbp - 0x64], r8d
00977CA6  44 89 45 90                     mov dword ptr [rbp - 0x70], r8d
00977CAA  44 89 45 14                     mov dword ptr [rbp + 0x14], r8d
00977CAE  44 89 45 18                     mov dword ptr [rbp + 0x18], r8d
00977CB2  4C 89 45 20                     mov qword ptr [rbp + 0x20], r8
00977CB6  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
00977CBA  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
00977CBE  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
00977CC2  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
00977CC6  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
00977CCA  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00977CCE  4C 89 45 E8                     mov qword ptr [rbp - 0x18], r8
00977CD2  4C 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], r8
00977CD9  4C 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], r8
00977CE0  4C 89 45 78                     mov qword ptr [rbp + 0x78], r8
00977CE4  4C 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], r8
00977CEB  44 88 44 24 61                  mov byte ptr [rsp + 0x61], r8b
00977CF0  44 88 44 24 78                  mov byte ptr [rsp + 0x78], r8b
00977CF5  44 88 44 24 60                  mov byte ptr [rsp + 0x60], r8b
00977CFA  44 88 44 24 62                  mov byte ptr [rsp + 0x62], r8b
00977CFF  4C 89 45 60                     mov qword ptr [rbp + 0x60], r8
00977D03  44 89 45 08                     mov dword ptr [rbp + 8], r8d
00977D07  44 89 45 98                     mov dword ptr [rbp - 0x68], r8d
00977D0B  44 88 44 24 63                  mov byte ptr [rsp + 0x63], r8b
00977D10  4C 89 45 F8                     mov qword ptr [rbp - 8], r8
00977D14  4C 89 45 00                     mov qword ptr [rbp], r8
00977D18  44 88 44 24 79                  mov byte ptr [rsp + 0x79], r8b
00977D1D  44 88 44 24 7A                  mov byte ptr [rsp + 0x7a], r8b
00977D22  44 89 45 0C                     mov dword ptr [rbp + 0xc], r8d
00977D26  44 89 45 10                     mov dword ptr [rbp + 0x10], r8d
00977D2A  41 B8 50 70 64 63               mov r8d, 0x63647050
00977D30  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00977D34  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00977D39  0F 11 85 F8 00 00 00            movups xmmword ptr [rbp + 0xf8], xmm0
00977D40  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00977D44  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00977D48  C7 85 D8 00 00 00 00 00 10 04   mov dword ptr [rbp + 0xd8], 0x4100000
00977D52  E8 99 A3 20 00                  call 0x140b820f0
00977D57  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00977D5E  48 85 C0                        test rax, rax
00977D61  0F 85 6C 01 00 00               jne 0x140977ed3
00977D67  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00977D6C  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00977D70  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00977D75  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00977D79  48 85 C9                        test rcx, rcx
00977D7C  74 0C                           je 0x140977d8a
00977D7E  E8 CD AA 20 00                  call 0x140b82850
00977D83  0F 57 C0                        xorps xmm0, xmm0
00977D86  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00977D8A  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00977D8E  48 85 C9                        test rcx, rcx
00977D91  74 0C                           je 0x140977d9f
00977D93  E8 B8 AA 20 00                  call 0x140b82850
00977D98  0F 57 C0                        xorps xmm0, xmm0
00977D9B  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00977D9F  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00977DA3  48 85 C9                        test rcx, rcx
00977DA6  74 0C                           je 0x140977db4
00977DA8  E8 A3 AA 20 00                  call 0x140b82850
00977DAD  0F 57 C0                        xorps xmm0, xmm0
00977DB0  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
00977DB4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00977DB8  48 85 C0                        test rax, rax
00977DBB  74 08                           je 0x140977dc5
00977DBD  48 8B C8                        mov rcx, rax
00977DC0  E8 8B AA 20 00                  call 0x140b82850
00977DC5  4D 85 F6                        test r14, r14
00977DC8  74 08                           je 0x140977dd2
00977DCA  49 8B CE                        mov rcx, r14
00977DCD  E8 7E AA 20 00                  call 0x140b82850
00977DD2  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00977DD6  48 85 C0                        test rax, rax
00977DD9  74 08                           je 0x140977de3
00977DDB  48 8B C8                        mov rcx, rax
00977DDE  E8 6D AA 20 00                  call 0x140b82850
00977DE3  4C 8B 85 90 00 00 00            mov r8, qword ptr [rbp + 0x90]
00977DEA  4D 85 C0                        test r8, r8
00977DED  74 08                           je 0x140977df7
00977DEF  49 8B C8                        mov rcx, r8
00977DF2  E8 59 AA 20 00                  call 0x140b82850
00977DF7  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
00977DFE  48 85 C9                        test rcx, rcx
00977E01  74 05                           je 0x140977e08
00977E03  E8 48 AA 20 00                  call 0x140b82850
00977E08  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
00977E0F  48 85 C9                        test rcx, rcx
00977E12  74 05                           je 0x140977e19
00977E14  E8 37 AA 20 00                  call 0x140b82850
00977E19  48 8B 85 D0 00 00 00            mov rax, qword ptr [rbp + 0xd0]
00977E20  48 85 C0                        test rax, rax
00977E23  74 08                           je 0x140977e2d
00977E25  48 8B C8                        mov rcx, rax
00977E28  E8 23 AA 20 00                  call 0x140b82850
00977E2D  4D 85 ED                        test r13, r13
00977E30  74 08                           je 0x140977e3a
00977E32  49 8B CD                        mov rcx, r13
00977E35  E8 16 AA 20 00                  call 0x140b82850
00977E3A  48 8B 8D C0 00 00 00            mov rcx, qword ptr [rbp + 0xc0]
00977E41  48 85 C9                        test rcx, rcx
00977E44  74 05                           je 0x140977e4b
00977E46  E8 05 AA 20 00                  call 0x140b82850
00977E4B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00977E4F  48 85 C0                        test rax, rax
00977E52  74 08                           je 0x140977e5c
00977E54  48 8B C8                        mov rcx, rax
00977E57  E8 F4 A9 20 00                  call 0x140b82850
00977E5C  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00977E63  48 85 C9                        test rcx, rcx
00977E66  74 0C                           je 0x140977e74
00977E68  E8 E3 A9 20 00                  call 0x140b82850
00977E6D  0F 57 C0                        xorps xmm0, xmm0
00977E70  0F 11 45 78                     movups xmmword ptr [rbp + 0x78], xmm0
00977E74  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00977E78  48 85 C9                        test rcx, rcx
00977E7B  74 0C                           je 0x140977e89
00977E7D  E8 CE A9 20 00                  call 0x140b82850
00977E82  0F 57 C0                        xorps xmm0, xmm0
00977E85  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00977E89  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
00977E90  48 85 C0                        test rax, rax
00977E93  74 0A                           je 0x140977e9f
00977E95  33 D2                           xor edx, edx
00977E97  48 8B C8                        mov rcx, rax
00977E9A  E8 D1 A9 20 00                  call 0x140b82870
00977E9F  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00977EA3  48 85 C9                        test rcx, rcx
00977EA6  74 07                           je 0x140977eaf
00977EA8  33 D2                           xor edx, edx
00977EAA  E8 C1 A9 20 00                  call 0x140b82870
00977EAF  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00977EB3  48 85 C9                        test rcx, rcx
00977EB6  74 05                           je 0x140977ebd
00977EB8  E8 F3 53 D3 FF                  call 0x1406ad2b0
00977EBD  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00977EC1  48 85 C9                        test rcx, rcx
00977EC4  74 05                           je 0x140977ecb
00977EC6  E8 E5 53 D3 FF                  call 0x1406ad2b0
00977ECB  8B C3                           mov eax, ebx
00977ECD  E9 8F 21 00 00                  jmp 0x14097a061
00977ED2  CC                              int3
00977ED3  48 85 F6                        test rsi, rsi
00977ED6  0F 84 E7 06 00 00               je 0x1409785c3
00977EDC  48 8B CE                        mov rcx, rsi
00977EDF  E8 68 D9 FF FF                  call 0x14097584c
00977EE4  8B D8                           mov ebx, eax
00977EE6  85 C0                           test eax, eax
00977EE8  0F 88 7E FE FF FF               js 0x140977d6c
00977EEE  48 8B 86 08 01 00 00            mov rax, qword ptr [rsi + 0x108]
00977EF5  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00977EF9  4C 39 A6 28 01 00 00            cmp qword ptr [rsi + 0x128], r12
00977F00  74 18                           je 0x140977f1a
00977F02  48 8D 96 20 01 00 00            lea rdx, [rsi + 0x120]
00977F09  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00977F0D  E8 32 41 B5 FF                  call 0x1404cc044
00977F12  84 C0                           test al, al
00977F14  0F 84 4D FE FF FF               je 0x140977d67
00977F1A  4C 39 A6 38 01 00 00            cmp qword ptr [rsi + 0x138], r12
00977F21  74 19                           je 0x140977f3c
00977F23  48 8D 96 30 01 00 00            lea rdx, [rsi + 0x130]
00977F2A  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00977F2F  E8 10 41 B5 FF                  call 0x1404cc044
00977F34  84 C0                           test al, al
00977F36  0F 84 2B FE FF FF               je 0x140977d67
00977F3C  4C 39 A6 48 01 00 00            cmp qword ptr [rsi + 0x148], r12
00977F43  74 18                           je 0x140977f5d
00977F45  48 8D 96 40 01 00 00            lea rdx, [rsi + 0x140]
00977F4C  48 8D 4D 68                     lea rcx, [rbp + 0x68]
00977F50  E8 EF 40 B5 FF                  call 0x1404cc044
00977F55  84 C0                           test al, al
00977F57  0F 84 0A FE FF FF               je 0x140977d67
00977F5D  4C 39 A6 58 01 00 00            cmp qword ptr [rsi + 0x158], r12
00977F64  74 1B                           je 0x140977f81
00977F66  48 8D 96 50 01 00 00            lea rdx, [rsi + 0x150]
00977F6D  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
00977F74  E8 CB 40 B5 FF                  call 0x1404cc044
00977F79  84 C0                           test al, al
00977F7B  0F 84 E6 FD FF FF               je 0x140977d67
00977F81  4C 39 A6 68 01 00 00            cmp qword ptr [rsi + 0x168], r12
00977F88  74 1B                           je 0x140977fa5
00977F8A  48 8D 96 60 01 00 00            lea rdx, [rsi + 0x160]
00977F91  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
00977F98  E8 A7 40 B5 FF                  call 0x1404cc044
00977F9D  84 C0                           test al, al
00977F9F  0F 84 C2 FD FF FF               je 0x140977d67
00977FA5  4C 39 A6 78 01 00 00            cmp qword ptr [rsi + 0x178], r12
00977FAC  74 1B                           je 0x140977fc9
00977FAE  48 8D 96 70 01 00 00            lea rdx, [rsi + 0x170]
00977FB5  48 8D 8D A8 00 00 00            lea rcx, [rbp + 0xa8]
00977FBC  E8 83 40 B5 FF                  call 0x1404cc044
00977FC1  84 C0                           test al, al
00977FC3  0F 84 9E FD FF FF               je 0x140977d67
00977FC9  4C 39 A6 98 01 00 00            cmp qword ptr [rsi + 0x198], r12
00977FD0  74 1B                           je 0x140977fed
00977FD2  48 8D 96 90 01 00 00            lea rdx, [rsi + 0x190]
00977FD9  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
00977FE0  E8 5F 40 B5 FF                  call 0x1404cc044
00977FE5  84 C0                           test al, al
00977FE7  0F 84 7A FD FF FF               je 0x140977d67
00977FED  8B 86 A4 01 00 00               mov eax, dword ptr [rsi + 0x1a4]
00977FF3  44 8B AE A0 01 00 00            mov r13d, dword ptr [rsi + 0x1a0]
00977FFA  8B 96 B8 00 00 00               mov edx, dword ptr [rsi + 0xb8]
00978000  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00978003  48 8D 86 D0 00 00 00            lea rax, [rsi + 0xd0]
0097800A  4C 8B 20                        mov r12, qword ptr [rax]
0097800D  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00978012  89 55 9C                        mov dword ptr [rbp - 0x64], edx
00978015  4C 3B E0                        cmp r12, rax
00978018  0F 84 0A 02 00 00               je 0x140978228
0097801E  49 8B CC                        mov rcx, r12
00978021  E8 26 D8 FF FF                  call 0x14097584c
00978026  33 C9                           xor ecx, ecx
00978028  8B D8                           mov ebx, eax
0097802A  85 C0                           test eax, eax
0097802C  79 36                           jns 0x140978064
0097802E  3D 93 04 00 C0                  cmp eax, 0xc0000493
00978033  0F 85 33 FD FF FF               jne 0x140977d6c
00978039  38 0D A1 29 49 00               cmp byte ptr [rip + 0x4929a1], cl
0097803F  0F 84 27 FD FF FF               je 0x140977d6c
00978045  8B 05 E5 FF 65 00               mov eax, dword ptr [rip + 0x65ffe5]
0097804B  A8 02                           test al, 2
0097804D  0F 84 19 FD FF FF               je 0x140977d6c
00978053  41 0F BA ED 0A                  bts r13d, 0xa
00978058  8B D9                           mov ebx, ecx
0097805A  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
0097805F  E9 97 01 00 00                  jmp 0x1409781fb
00978064  49 39 8C 24 28 01 00 00         cmp qword ptr [r12 + 0x128], rcx
0097806C  74 0E                           je 0x14097807c
0097806E  41 83 A4 24 B8 00 00 00 FE      and dword ptr [r12 + 0xb8], 0xfffffffe
00978077  E9 7F 01 00 00                  jmp 0x1409781fb
0097807C  49 39 8C 24 38 01 00 00         cmp qword ptr [r12 + 0x138], rcx
00978084  74 23                           je 0x1409780a9
00978086  4D 8D 84 24 30 01 00 00         lea r8, [r12 + 0x130]
0097808E  45 33 C9                        xor r9d, r9d
00978091  33 D2                           xor edx, edx
00978093  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00978098  E8 8B 9A DB FF                  call 0x140731b28
0097809D  33 C9                           xor ecx, ecx
0097809F  8B D8                           mov ebx, eax
009780A1  85 C0                           test eax, eax
009780A3  0F 88 C3 FC FF FF               js 0x140977d6c
009780A9  49 39 8C 24 48 01 00 00         cmp qword ptr [r12 + 0x148], rcx
009780B1  74 22                           je 0x1409780d5
009780B3  4D 8D 84 24 40 01 00 00         lea r8, [r12 + 0x140]
009780BB  45 33 C9                        xor r9d, r9d
009780BE  33 D2                           xor edx, edx
009780C0  48 8D 4D 68                     lea rcx, [rbp + 0x68]
009780C4  E8 5F 9A DB FF                  call 0x140731b28
009780C9  33 C9                           xor ecx, ecx
009780CB  8B D8                           mov ebx, eax
009780CD  85 C0                           test eax, eax
009780CF  0F 88 97 FC FF FF               js 0x140977d6c
009780D5  49 39 8C 24 58 01 00 00         cmp qword ptr [r12 + 0x158], rcx
009780DD  74 25                           je 0x140978104
009780DF  4D 8D 84 24 50 01 00 00         lea r8, [r12 + 0x150]
009780E7  45 33 C9                        xor r9d, r9d
009780EA  33 D2                           xor edx, edx
009780EC  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
009780F3  E8 30 9A DB FF                  call 0x140731b28
009780F8  33 C9                           xor ecx, ecx
009780FA  8B D8                           mov ebx, eax
009780FC  85 C0                           test eax, eax
009780FE  0F 88 68 FC FF FF               js 0x140977d6c
00978104  49 39 8C 24 68 01 00 00         cmp qword ptr [r12 + 0x168], rcx
0097810C  74 25                           je 0x140978133
0097810E  4D 8D 84 24 60 01 00 00         lea r8, [r12 + 0x160]
00978116  45 33 C9                        xor r9d, r9d
00978119  33 D2                           xor edx, edx
0097811B  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
00978122  E8 01 9A DB FF                  call 0x140731b28
00978127  33 C9                           xor ecx, ecx
00978129  8B D8                           mov ebx, eax
0097812B  85 C0                           test eax, eax
0097812D  0F 88 39 FC FF FF               js 0x140977d6c
00978133  49 39 8C 24 78 01 00 00         cmp qword ptr [r12 + 0x178], rcx
0097813B  74 23                           je 0x140978160
0097813D  4D 8D 84 24 70 01 00 00         lea r8, [r12 + 0x170]
00978145  45 33 C9                        xor r9d, r9d
00978148  33 D2                           xor edx, edx
0097814A  48 8D 8D A8 00 00 00            lea rcx, [rbp + 0xa8]
00978151  E8 D2 99 DB FF                  call 0x140731b28
00978156  8B D8                           mov ebx, eax
00978158  85 C0                           test eax, eax
0097815A  0F 88 0C FC FF FF               js 0x140977d6c
00978160  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
00978163  49 8D 54 24 28                  lea rdx, [r12 + 0x28]
00978168  41 0B 84 24 A4 01 00 00         or eax, dword ptr [r12 + 0x1a4]
00978170  48 8D 8D C8 00 00 00            lea rcx, [rbp + 0xc8]
00978177  45 0B AC 24 A0 01 00 00         or r13d, dword ptr [r12 + 0x1a0]
0097817F  45 33 C9                        xor r9d, r9d
00978182  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00978185  45 33 C0                        xor r8d, r8d
00978188  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
0097818B  41 0B 84 24 B8 00 00 00         or eax, dword ptr [r12 + 0xb8]
00978193  89 45 9C                        mov dword ptr [rbp - 0x64], eax
00978196  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
0097819B  E8 88 99 DB FF                  call 0x140731b28
009781A0  8B D8                           mov ebx, eax
009781A2  85 C0                           test eax, eax
009781A4  0F 88 C2 FB FF FF               js 0x140977d6c
009781AA  49 8D 94 24 A8 01 00 00         lea rdx, [r12 + 0x1a8]
009781B2  45 33 C9                        xor r9d, r9d
009781B5  45 33 C0                        xor r8d, r8d
009781B8  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009781BC  E8 67 99 DB FF                  call 0x140731b28
009781C1  33 C9                           xor ecx, ecx
009781C3  8B D8                           mov ebx, eax
009781C5  85 C0                           test eax, eax
009781C7  0F 88 9F FB FF FF               js 0x140977d6c
009781CD  49 39 8C 24 98 01 00 00         cmp qword ptr [r12 + 0x198], rcx
009781D5  74 24                           je 0x1409781fb
009781D7  49 8D 94 24 90 01 00 00         lea rdx, [r12 + 0x190]
009781DF  45 33 C9                        xor r9d, r9d
009781E2  45 33 C0                        xor r8d, r8d
009781E5  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
009781EC  E8 37 99 DB FF                  call 0x140731b28
009781F1  8B D8                           mov ebx, eax
009781F3  85 C0                           test eax, eax
009781F5  0F 88 71 FB FF FF               js 0x140977d6c
009781FB  4D 8B 24 24                     mov r12, qword ptr [r12]
009781FF  48 8D 86 D0 00 00 00            lea rax, [rsi + 0xd0]
00978206  4C 3B E0                        cmp r12, rax
00978209  0F 85 0F FE FF FF               jne 0x14097801e
0097820F  8B 4D 94                        mov ecx, dword ptr [rbp - 0x6c]
00978212  45 33 E4                        xor r12d, r12d
00978215  8B 55 9C                        mov edx, dword ptr [rbp - 0x64]
00978218  89 4D 94                        mov dword ptr [rbp - 0x6c], ecx
0097821B  89 55 9C                        mov dword ptr [rbp - 0x64], edx
0097821E  85 DB                           test ebx, ebx
00978220  0F 88 46 FB FF FF               js 0x140977d6c
00978226  EB 03                           jmp 0x14097822b
00978228  45 33 E4                        xor r12d, r12d
0097822B  8B 05 FF FD 65 00               mov eax, dword ptr [rip + 0x65fdff]
00978231  A8 02                           test al, 2
00978233  74 53                           je 0x140978288
00978235  41 0F BA E5 0A                  bt r13d, 0xa
0097823A  73 34                           jae 0x140978270
0097823C  F6 86 B8 01 00 00 02            test byte ptr [rsi + 0x1b8], 2
00978243  0F 94 C1                        sete cl
00978246  F6 05 67 FE 65 00 01            test byte ptr [rip + 0x65fe67], 1
0097824D  0F 94 C0                        sete al
00978250  84 C8                           test al, cl
00978252  74 1C                           je 0x140978270
00978254  44 38 25 ED BE 64 00            cmp byte ptr [rip + 0x64beed], r12b
0097825B  75 13                           jne 0x140978270
0097825D  44 38 25 7C 27 49 00            cmp byte ptr [rip + 0x49277c], r12b
00978264  75 0A                           jne 0x140978270
00978266  BB 95 04 00 C0                  mov ebx, 0xc0000495
0097826B  E9 FC FA FF FF                  jmp 0x140977d6c
00978270  F6 C2 40                        test dl, 0x40
00978273  74 13                           je 0x140978288
00978275  44 38 25 64 27 49 00            cmp byte ptr [rip + 0x492764], r12b
0097827C  74 E8                           je 0x140978266
0097827E  41 0F BA ED 0A                  bts r13d, 0xa
00978283  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00978288  33 D2                           xor edx, edx
0097828A  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00978291  41 B8 A8 00 00 00               mov r8d, 0xa8
00978297  E8 A4 E9 D4 FF                  call 0x1406c6c40
0097829C  B9 20 01 00 00                  mov ecx, 0x120
009782A1  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009782A6  BA 00 00 00 01                  mov edx, 0x1000000
009782AB  89 8D B8 01 00 00               mov dword ptr [rbp + 0x1b8], ecx
009782B1  48 8D 05 18 6F 18 00            lea rax, [rip + 0x186f18]
009782B8  89 95 D0 01 00 00               mov dword ptr [rbp + 0x1d0], edx
009782BE  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
009782C5  4C 8D 85 B0 01 00 00            lea r8, [rbp + 0x1b0]
009782CC  48 8D 45 A8                     lea rax, [rbp - 0x58]
009782D0  89 95 08 02 00 00               mov dword ptr [rbp + 0x208], edx
009782D6  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
009782DA  45 33 C9                        xor r9d, r9d
009782DD  48 89 85 C8 01 00 00            mov qword ptr [rbp + 0x1c8], rax
009782E4  48 8D 05 15 6E 18 00            lea rax, [rip + 0x186e15]
009782EB  48 89 85 F8 01 00 00            mov qword ptr [rbp + 0x1f8], rax
009782F2  48 8D 45 D8                     lea rax, [rbp - 0x28]
009782F6  89 8D F0 01 00 00               mov dword ptr [rbp + 0x1f0], ecx
009782FC  B9 00 00 00 C0                  mov ecx, 0xc0000000
00978301  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
00978308  E8 43 0D F5 FF                  call 0x1408c9050
0097830D  8B D8                           mov ebx, eax
0097830F  85 C0                           test eax, eax
00978311  0F 88 55 FA FF FF               js 0x140977d6c
00978317  4C 39 65 B0                     cmp qword ptr [rbp - 0x50], r12
0097831B  75 48                           jne 0x140978365
0097831D  4C 39 65 E0                     cmp qword ptr [rbp - 0x20], r12
00978321  75 42                           jne 0x140978365
00978323  4C 39 A6 A8 00 00 00            cmp qword ptr [rsi + 0xa8], r12
0097832A  74 39                           je 0x140978365
0097832C  8B 05 FE FC 65 00               mov eax, dword ptr [rip + 0x65fcfe]
00978332  A8 02                           test al, 2
00978334  74 2F                           je 0x140978365
00978336  44 38 25 0B BE 64 00            cmp byte ptr [rip + 0x64be0b], r12b
0097833D  75 26                           jne 0x140978365
0097833F  44 38 25 9A 26 49 00            cmp byte ptr [rip + 0x49269a], r12b
00978346  75 13                           jne 0x14097835b
00978348  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0097834D  BB 95 04 00 C0                  mov ebx, 0xc0000495
00978352  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00978356  E9 44 FA FF FF                  jmp 0x140977d9f
0097835B  41 0F BA ED 0A                  bts r13d, 0xa
00978360  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00978365  66 44 39 65 A8                  cmp word ptr [rbp - 0x58], r12w
0097836A  75 0F                           jne 0x14097837b
0097836C  4C 39 65 B0                     cmp qword ptr [rbp - 0x50], r12
00978370  74 09                           je 0x14097837b
00978372  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00978376  E8 85 84 04 00                  call 0x1409c0800
0097837B  66 44 39 65 D8                  cmp word ptr [rbp - 0x28], r12w
00978380  75 0F                           jne 0x140978391
00978382  4C 39 65 E0                     cmp qword ptr [rbp - 0x20], r12
00978386  74 09                           je 0x140978391
00978388  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0097838C  E8 6F 84 04 00                  call 0x1409c0800
00978391  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
00978395  48 85 DB                        test rbx, rbx
00978398  0F 84 B5 01 00 00               je 0x140978553
0097839E  48 8B 0D F3 DF 4E 00            mov rcx, qword ptr [rip + 0x4edff3]
009783A5  48 8D 45 C8                     lea rax, [rbp - 0x38]
009783A9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009783AE  41 B9 19 00 02 00               mov r9d, 0x20019
009783B4  41 B8 02 00 00 00               mov r8d, 2
009783BA  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
009783BF  48 8B D3                        mov rdx, rbx
009783C2  E8 21 92 F6 FF                  call 0x1408e15e8
009783C7  85 C0                           test eax, eax
009783C9  0F 88 84 01 00 00               js 0x140978553
009783CF  33 D2                           xor edx, edx
009783D1  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
009783D8  41 B8 A0 00 00 00               mov r8d, 0xa0
009783DE  E8 5D E8 D4 FF                  call 0x1406c6c40
009783E3  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
009783E7  48 8D 05 22 C0 69 FF            lea rax, [rip - 0x963fde]
009783EE  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
009783F5  B9 11 00 00 00                  mov ecx, 0x11
009783FA  48 8D 44 24 61                  lea rax, [rsp + 0x61]
009783FF  89 8D 18 01 00 00               mov dword ptr [rbp + 0x118], ecx
00978405  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
0097840C  48 8B D3                        mov rdx, rbx
0097840F  48 8D 05 82 A5 6A FF            lea rax, [rip - 0x955a7e]
00978416  89 8D 40 01 00 00               mov dword ptr [rbp + 0x140], ecx
0097841C  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
00978423  B9 02 00 00 00                  mov ecx, 2
00978428  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0097842D  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00978435  48 89 85 48 01 00 00            mov qword ptr [rbp + 0x148], rax
0097843C  44 8B C1                        mov r8d, ecx
0097843F  48 8D 05 9A F8 6A FF            lea rax, [rip - 0x950766]
00978446  C7 85 28 01 00 00 01 00 00 00   mov dword ptr [rbp + 0x128], 1
00978450  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00978457  48 8D 45 38                     lea rax, [rbp + 0x38]
0097845B  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00978462  48 8D 05 97 A4 6A FF            lea rax, [rip - 0x955b69]
00978469  48 89 85 88 01 00 00            mov qword ptr [rbp + 0x188], rax
00978470  48 8D 45 60                     lea rax, [rbp + 0x60]
00978474  48 89 85 98 01 00 00            mov qword ptr [rbp + 0x198], rax
0097847B  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00978482  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00978487  C7 85 50 01 00 00 01 00 00 00   mov dword ptr [rbp + 0x150], 1
00978491  C7 85 68 01 00 00 12 00 00 00   mov dword ptr [rbp + 0x168], 0x12
0097849B  C7 85 7C 01 00 00 06 00 00 00   mov dword ptr [rbp + 0x17c], 6
009784A5  C7 85 90 01 00 00 03 10 00 00   mov dword ptr [rbp + 0x190], 0x1003
009784AF  89 8D A4 01 00 00               mov dword ptr [rbp + 0x1a4], ecx
009784B5  E8 B2 F2 FF FF                  call 0x14097776c
009784BA  8B D8                           mov ebx, eax
009784BC  85 C0                           test eax, eax
009784BE  0F 88 A8 F8 FF FF               js 0x140977d6c
009784C4  44 39 A5 30 01 00 00            cmp dword ptr [rbp + 0x130], r12d
009784CB  7D 05                           jge 0x1409784d2
009784CD  44 88 64 24 61                  mov byte ptr [rsp + 0x61], r12b
009784D2  44 39 A5 58 01 00 00            cmp dword ptr [rbp + 0x158], r12d
009784D9  7D 05                           jge 0x1409784e0
009784DB  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
009784E0  44 39 A5 80 01 00 00            cmp dword ptr [rbp + 0x180], r12d
009784E7  7D 0B                           jge 0x1409784f4
009784E9  33 D2                           xor edx, edx
009784EB  48 8D 4D 38                     lea rcx, [rbp + 0x38]
009784EF  E8 8C 22 AB FF                  call 0x14042a780
009784F4  44 39 A5 A8 01 00 00            cmp dword ptr [rbp + 0x1a8], r12d
009784FB  7D 06                           jge 0x140978503
009784FD  4C 89 65 60                     mov qword ptr [rbp + 0x60], r12
00978501  EB 09                           jmp 0x14097850c
00978503  8B 85 A0 01 00 00               mov eax, dword ptr [rbp + 0x1a0]
00978509  89 45 08                        mov dword ptr [rbp + 8], eax
0097850C  44 38 64 24 61                  cmp byte ptr [rsp + 0x61], r12b
00978511  75 76                           jne 0x140978589
00978513  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978517  48 8D 44 24 78                  lea rax, [rsp + 0x78]
0097851C  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
00978520  4D 8B CF                        mov r9, r15
00978523  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00978527  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0097852C  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00978530  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00978535  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
00978539  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0097853E  E8 C1 AF DB FF                  call 0x140733504
00978543  85 C0                           test eax, eax
00978545  78 0C                           js 0x140978553
00978547  44 38 64 24 78                  cmp byte ptr [rsp + 0x78], r12b
0097854C  74 05                           je 0x140978553
0097854E  C6 44 24 61 FF                  mov byte ptr [rsp + 0x61], 0xff
00978553  44 38 64 24 61                  cmp byte ptr [rsp + 0x61], r12b
00978558  75 2F                           jne 0x140978589
0097855A  F6 05 53 FB 65 00 01            test byte ptr [rip + 0x65fb53], 1
00978561  0F 94 C1                        sete cl
00978564  F6 05 C5 FA 65 00 02            test byte ptr [rip + 0x65fac5], 2
0097856B  0F 95 C0                        setne al
0097856E  84 C8                           test al, cl
00978570  74 17                           je 0x140978589
00978572  44 38 25 67 24 49 00            cmp byte ptr [rip + 0x492467], r12b
00978579  0F 84 E7 FC FF FF               je 0x140978266
0097857F  41 0F BA ED 0A                  bts r13d, 0xa
00978584  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00978589  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0097858D  48 85 C9                        test rcx, rcx
00978590  74 2C                           je 0x1409785be
00978592  44 8B 45 08                     mov r8d, dword ptr [rbp + 8]
00978596  41 8B C4                        mov eax, r12d
00978599  8A 56 6E                        mov dl, byte ptr [rsi + 0x6e]
0097859C  45 85 C0                        test r8d, r8d
0097859F  74 13                           je 0x1409785b4
009785A1  38 11                           cmp byte ptr [rcx], dl
009785A3  74 0A                           je 0x1409785af
009785A5  FF C0                           inc eax
009785A7  48 FF C1                        inc rcx
009785AA  41 3B C0                        cmp eax, r8d
009785AD  72 F2                           jb 0x1409785a1
009785AF  41 3B C0                        cmp eax, r8d
009785B2  72 0A                           jb 0x1409785be
009785B4  BB 24 04 00 C0                  mov ebx, 0xc0000424
009785B9  E9 AE F7 FF FF                  jmp 0x140977d6c
009785BE  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
009785C3  8B 07                           mov eax, dword ptr [rdi]
009785C5  48 8D 1D BC 90 69 FF            lea rbx, [rip - 0x966f44]
009785CC  A8 01                           test al, 1
009785CE  0F 85 FE 00 00 00               jne 0x1409786d2
009785D4  33 D2                           xor edx, edx
009785D6  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
009785DD  41 B8 A0 00 00 00               mov r8d, 0xa0
009785E3  E8 58 E6 D4 FF                  call 0x1406c6c40
009785E8  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
009785EC  48 8D 85 F8 00 00 00            lea rax, [rbp + 0xf8]
009785F3  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
009785FA  4D 8B CF                        mov r9, r15
009785FD  48 8D 05 BC A3 6A FF            lea rax, [rip - 0x955c44]
00978604  C7 44 24 28 03 00 00 00         mov dword ptr [rsp + 0x28], 3
0097860C  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
00978613  41 B8 01 00 00 00               mov r8d, 1
00978619  48 8D 45 98                     lea rax, [rbp - 0x68]
0097861D  48 89 9D 10 01 00 00            mov qword ptr [rbp + 0x110], rbx
00978624  48 89 85 48 01 00 00            mov qword ptr [rbp + 0x148], rax
0097862B  48 8D 05 56 A9 69 FF            lea rax, [rip - 0x9656aa]
00978632  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00978639  48 8D 45 F8                     lea rax, [rbp - 8]
0097863D  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00978644  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
0097864B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00978650  C7 85 18 01 00 00 0D 00 00 00   mov dword ptr [rbp + 0x118], 0xd
0097865A  C7 85 28 01 00 00 10 00 00 00   mov dword ptr [rbp + 0x128], 0x10
00978664  C7 85 40 01 00 00 07 00 00 00   mov dword ptr [rbp + 0x140], 7
0097866E  C7 85 50 01 00 00 04 00 00 00   mov dword ptr [rbp + 0x150], 4
00978678  C7 85 68 01 00 00 12 00 00 00   mov dword ptr [rbp + 0x168], 0x12
00978682  C7 85 7C 01 00 00 06 00 00 00   mov dword ptr [rbp + 0x17c], 6
0097868C  E8 DB F0 FF FF                  call 0x14097776c
00978691  33 D2                           xor edx, edx
00978693  8B D8                           mov ebx, eax
00978695  85 C0                           test eax, eax
00978697  0F 88 CF F6 FF FF               js 0x140977d6c
0097869D  39 95 30 01 00 00               cmp dword ptr [rbp + 0x130], edx
009786A3  7D 0C                           jge 0x1409786b1
009786A5  0F 57 C0                        xorps xmm0, xmm0
009786A8  0F 11 85 F8 00 00 00            movups xmmword ptr [rbp + 0xf8], xmm0
009786AF  EB 05                           jmp 0x1409786b6
009786B1  C6 44 24 63 01                  mov byte ptr [rsp + 0x63], 1
009786B6  39 95 58 01 00 00               cmp dword ptr [rbp + 0x158], edx
009786BC  7D 03                           jge 0x1409786c1
009786BE  89 55 98                        mov dword ptr [rbp - 0x68], edx
009786C1  39 95 80 01 00 00               cmp dword ptr [rbp + 0x180], edx
009786C7  7D 0B                           jge 0x1409786d4
009786C9  48 8D 4D F8                     lea rcx, [rbp - 8]
009786CD  E8 AE 20 AB FF                  call 0x14042a780
009786D2  33 D2                           xor edx, edx
009786D4  48 8D 1D C5 A8 69 FF            lea rbx, [rip - 0x96573b]
009786DB  38 54 24 60                     cmp byte ptr [rsp + 0x60], dl
009786DF  0F 85 D8 00 00 00               jne 0x1409787bd
009786E5  F6 45 98 04                     test byte ptr [rbp - 0x68], 4
009786E9  0F 84 B2 00 00 00               je 0x1409787a1
009786EF  48 85 F6                        test rsi, rsi
009786F2  0F 84 9E 00 00 00               je 0x140978796
009786F8  33 D2                           xor edx, edx
009786FA  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00978701  41 B8 A0 00 00 00               mov r8d, 0xa0
00978707  E8 34 E5 D4 FF                  call 0x1406c6c40
0097870C  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978710  48 8D 45 78                     lea rax, [rbp + 0x78]
00978714  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
0097871B  4D 8B CF                        mov r9, r15
0097871E  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00978725  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0097872D  41 B8 01 00 00 00               mov r8d, 1
00978733  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00978738  48 89 9D 10 01 00 00            mov qword ptr [rbp + 0x110], rbx
0097873F  C7 85 18 01 00 00 12 00 00 00   mov dword ptr [rbp + 0x118], 0x12
00978749  C7 85 2C 01 00 00 06 00 00 00   mov dword ptr [rbp + 0x12c], 6
00978753  E8 14 F0 FF FF                  call 0x14097776c
00978758  33 D2                           xor edx, edx
0097875A  8B D8                           mov ebx, eax
0097875C  85 C0                           test eax, eax
0097875E  0F 88 08 F6 FF FF               js 0x140977d6c
00978764  39 95 30 01 00 00               cmp dword ptr [rbp + 0x130], edx
0097876A  7D 0B                           jge 0x140978777
0097876C  48 8D 4D 78                     lea rcx, [rbp + 0x78]
00978770  E8 0B 20 AB FF                  call 0x14042a780
00978775  33 D2                           xor edx, edx
00978777  48 39 95 80 00 00 00            cmp qword ptr [rbp + 0x80], rdx
0097877E  74 1B                           je 0x14097879b
00978780  48 8D 56 28                     lea rdx, [rsi + 0x28]
00978784  41 B0 01                        mov r8b, 1
00978787  48 8D 4D 78                     lea rcx, [rbp + 0x78]
0097878B  E8 90 A2 FB FF                  call 0x140932a20
00978790  33 D2                           xor edx, edx
00978792  84 C0                           test al, al
00978794  74 05                           je 0x14097879b
00978796  C6 44 24 60 FF                  mov byte ptr [rsp + 0x60], 0xff
0097879B  38 54 24 60                     cmp byte ptr [rsp + 0x60], dl
0097879F  75 1C                           jne 0x1409787bd
009787A1  4C 8B 45 20                     mov r8, qword ptr [rbp + 0x20]
009787A5  48 8B D7                        mov rdx, rdi
009787A8  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
009787AC  E8 A3 0C 11 00                  call 0x140a89454
009787B1  33 D2                           xor edx, edx
009787B3  8B D8                           mov ebx, eax
009787B5  85 C0                           test eax, eax
009787B7  0F 88 AF F5 FF FF               js 0x140977d6c
009787BD  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
009787C1  48 85 C9                        test rcx, rcx
009787C4  74 55                           je 0x14097881b
009787C6  48 8D 05 83 60 18 00            lea rax, [rip + 0x186083]
009787CD  C7 45 B8 1A 00 1C 00            mov dword ptr [rbp - 0x48], 0x1c001a
009787D4  48 8B D1                        mov rdx, rcx
009787D7  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
009787DB  48 8D 4D 58                     lea rcx, [rbp + 0x58]
009787DF  41 B9 19 00 02 00               mov r9d, 0x20019
009787E5  4C 8D 45 B8                     lea r8, [rbp - 0x48]
009787E9  E8 56 93 0D 00                  call 0x140a51b44
009787EE  8B D8                           mov ebx, eax
009787F0  3D 34 00 00 C0                  cmp eax, 0xc0000034
009787F5  74 22                           je 0x140978819
009787F7  85 C0                           test eax, eax
009787F9  0F 88 6D F5 FF FF               js 0x140977d6c
009787FF  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00978803  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00978807  E8 D8 DC FE FF                  call 0x1409664e4
0097880C  33 D2                           xor edx, edx
0097880E  8B D8                           mov ebx, eax
00978810  85 C0                           test eax, eax
00978812  79 07                           jns 0x14097881b
00978814  E9 53 F5 FF FF                  jmp 0x140977d6c
00978819  33 D2                           xor edx, edx
0097881B  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
0097881F  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00978823  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00978827  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0097882A  A8 04                           test al, 4
0097882C  74 68                           je 0x140978896
0097882E  48 8B 0D 63 DB 4E 00            mov rcx, qword ptr [rip + 0x4edb63]
00978835  48 8D 45 10                     lea rax, [rbp + 0x10]
00978839  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
0097883D  4D 8B CF                        mov r9, r15
00978840  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00978845  41 B8 01 00 00 00               mov r8d, 1
0097884B  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00978853  48 8D 44 24 62                  lea rax, [rsp + 0x62]
00978858  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0097885D  48 8D 45 0C                     lea rax, [rbp + 0xc]
00978861  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978866  48 8D 05 BB BB 69 FF            lea rax, [rip - 0x964445]
0097886D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00978872  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00978877  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0097887B  E8 00 99 F6 FF                  call 0x1408e2180
00978880  33 D2                           xor edx, edx
00978882  85 C0                           test eax, eax
00978884  78 0C                           js 0x140978892
00978886  83 7D 0C 11                     cmp dword ptr [rbp + 0xc], 0x11
0097888A  75 06                           jne 0x140978892
0097888C  83 7D 10 01                     cmp dword ptr [rbp + 0x10], 1
00978890  74 04                           je 0x140978896
00978892  88 54 24 62                     mov byte ptr [rsp + 0x62], dl
00978896  48 85 F6                        test rsi, rsi
00978899  74 29                           je 0x1409788c4
0097889B  48 83 7D 50 00                  cmp qword ptr [rbp + 0x50], 0
009788A0  75 22                           jne 0x1409788c4
009788A2  48 39 55 40                     cmp qword ptr [rbp + 0x40], rdx
009788A6  75 1C                           jne 0x1409788c4
009788A8  38 54 24 62                     cmp byte ptr [rsp + 0x62], dl
009788AC  75 16                           jne 0x1409788c4
009788AE  F7 83 30 02 00 00 00 01 00 00   test dword ptr [rbx + 0x230], 0x100
009788B8  75 0A                           jne 0x1409788c4
009788BA  BB 94 04 00 C0                  mov ebx, 0xc0000494
009788BF  E9 A8 F4 FF FF                  jmp 0x140977d6c
009788C4  8B 07                           mov eax, dword ptr [rdi]
009788C6  A8 01                           test al, 1
009788C8  0F 85 B8 00 00 00               jne 0x140978986
009788CE  48 85 F6                        test rsi, rsi
009788D1  75 53                           jne 0x140978926
009788D3  38 54 24 63                     cmp byte ptr [rsp + 0x63], dl
009788D7  74 0C                           je 0x1409788e5
009788D9  F7 83 30 02 00 00 00 01 00 00   test dword ptr [rbx + 0x230], 0x100
009788E3  75 17                           jne 0x1409788fc
009788E5  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
009788E9  45 33 C9                        xor r9d, r9d
009788EC  48 8B 0D A5 DA 4E 00            mov rcx, qword ptr [rip + 0x4edaa5]
009788F3  45 8D 41 11                     lea r8d, [r9 + 0x11]
009788F7  E8 30 11 09 00                  call 0x140a09a2c
009788FC  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978900  45 33 C9                        xor r9d, r9d
00978903  48 8B 0D 8E DA 4E 00            mov rcx, qword ptr [rip + 0x4eda8e]
0097890A  45 8D 41 12                     lea r8d, [r9 + 0x12]
0097890E  E8 19 11 09 00                  call 0x140a09a2c
00978913  33 D2                           xor edx, edx
00978915  4C 8B CA                        mov r9, rdx
00978918  48 85 F6                        test rsi, rsi
0097891B  74 70                           je 0x14097898d
0097891D  4C 8D 86 00 01 00 00            lea r8, [rsi + 0x100]
00978924  EB 6A                           jmp 0x140978990
00978926  48 8D 8D F8 00 00 00            lea rcx, [rbp + 0xf8]
0097892D  E8 AE 50 F6 FF                  call 0x1408dd9e0
00978932  84 C0                           test al, al
00978934  75 4A                           jne 0x140978980
00978936  48 8D 9E F0 00 00 00            lea rbx, [rsi + 0xf0]
0097893D  48 8B CB                        mov rcx, rbx
00978940  E8 9B 50 F6 FF                  call 0x1408dd9e0
00978945  84 C0                           test al, al
00978947  75 33                           jne 0x14097897c
00978949  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
00978950  48 2B 0B                        sub rcx, qword ptr [rbx]
00978953  75 0B                           jne 0x140978960
00978955  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
0097895C  48 2B 4B 08                     sub rcx, qword ptr [rbx + 8]
00978960  48 85 C9                        test rcx, rcx
00978963  74 17                           je 0x14097897c
00978965  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978969  45 33 C9                        xor r9d, r9d
0097896C  48 8B 0D 25 DA 4E 00            mov rcx, qword ptr [rip + 0x4eda25]
00978973  45 8D 41 12                     lea r8d, [r9 + 0x12]
00978977  E8 B0 10 09 00                  call 0x140a09a2c
0097897C  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
00978980  4C 8D 4E 28                     lea r9, [rsi + 0x28]
00978984  EB 97                           jmp 0x14097891d
00978986  48 85 F6                        test rsi, rsi
00978989  75 F5                           jne 0x140978980
0097898B  EB 88                           jmp 0x140978915
0097898D  4C 8B C2                        mov r8, rdx
00978990  48 8D 45 18                     lea rax, [rbp + 0x18]
00978994  48 8B D7                        mov rdx, rdi
00978997  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0097899C  48 8B CB                        mov rcx, rbx
0097899F  48 8D 45 14                     lea rax, [rbp + 0x14]
009789A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009789A8  E8 B3 B4 FE FF                  call 0x140963e60
009789AD  33 D2                           xor edx, edx
009789AF  85 C0                           test eax, eax
009789B1  78 0F                           js 0x1409789c2
009789B3  44 0B 6D 14                     or r13d, dword ptr [rbp + 0x14]
009789B7  8B 45 18                        mov eax, dword ptr [rbp + 0x18]
009789BA  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
009789BF  89 45 90                        mov dword ptr [rbp - 0x70], eax
009789C2  8B 07                           mov eax, dword ptr [rdi]
009789C4  A8 01                           test al, 1
009789C6  75 64                           jne 0x140978a2c
009789C8  8A 44 24 63                     mov al, byte ptr [rsp + 0x63]
009789CC  4C 8D 86 F0 00 00 00            lea r8, [rsi + 0xf0]
009789D3  F6 D8                           neg al
009789D5  48 8D 85 F8 00 00 00            lea rax, [rbp + 0xf8]
009789DC  48 1B C9                        sbb rcx, rcx
009789DF  48 23 C8                        and rcx, rax
009789E2  48 85 F6                        test rsi, rsi
009789E5  75 03                           jne 0x1409789ea
009789E7  4C 8B C2                        mov r8, rdx
009789EA  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
009789EE  48 8B D7                        mov rdx, rdi
009789F1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009789F6  48 8B CB                        mov rcx, rbx
009789F9  E8 6A D7 FE FF                  call 0x140966168
009789FE  48 8B 0D 93 D9 4E 00            mov rcx, qword ptr [rip + 0x4ed993]
00978A05  4C 8D 05 34 4D 18 00            lea r8, [rip + 0x184d34]
00978A0C  49 8B D7                        mov rdx, r15
00978A0F  E8 B4 D2 FE FF                  call 0x140965cc8
00978A14  48 8B 0D 7D D9 4E 00            mov rcx, qword ptr [rip + 0x4ed97d]
00978A1B  4C 8D 05 4E 5E 18 00            lea r8, [rip + 0x185e4e]
00978A22  49 8B D7                        mov rdx, r15
00978A25  E8 9E D2 FE FF                  call 0x140965cc8
00978A2A  33 D2                           xor edx, edx
00978A2C  48 85 F6                        test rsi, rsi
00978A2F  74 61                           je 0x140978a92
00978A31  48 8D 9E F0 00 00 00            lea rbx, [rsi + 0xf0]
00978A38  48 8B CB                        mov rcx, rbx
00978A3B  E8 A0 4F F6 FF                  call 0x1408dd9e0
00978A40  33 D2                           xor edx, edx
00978A42  84 C0                           test al, al
00978A44  75 4C                           jne 0x140978a92
00978A46  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978A4A  48 8D 05 37 8C 69 FF            lea rax, [rip - 0x9673c9]
00978A51  48 8B 0D 40 D9 4E 00            mov rcx, qword ptr [rip + 0x4ed940]
00978A58  44 8D 4A 01                     lea r9d, [rdx + 1]
00978A5C  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00978A60  48 8B D7                        mov rdx, rdi
00978A63  C7 44 24 48 10 00 00 00         mov dword ptr [rsp + 0x48], 0x10
00978A6B  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00978A70  C7 44 24 38 0D 00 00 00         mov dword ptr [rsp + 0x38], 0xd
00978A78  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978A7D  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978A82  E8 C9 50 11 00                  call 0x140a8db50
00978A87  8B D8                           mov ebx, eax
00978A89  85 C0                           test eax, eax
00978A8B  79 46                           jns 0x140978ad3
00978A8D  E9 DA F2 FF FF                  jmp 0x140977d6c
00978A92  8B 07                           mov eax, dword ptr [rdi]
00978A94  A8 01                           test al, 1
00978A96  75 3B                           jne 0x140978ad3
00978A98  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978A9C  48 8D 05 E5 8B 69 FF            lea rax, [rip - 0x96741b]
00978AA3  48 8B 0D EE D8 4E 00            mov rcx, qword ptr [rip + 0x4ed8ee]
00978AAA  41 B9 01 00 00 00               mov r9d, 1
00978AB0  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00978AB4  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00978AB8  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00978ABD  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00978AC1  48 8B D7                        mov rdx, rdi
00978AC4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978AC9  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978ACE  E8 7D 50 11 00                  call 0x140a8db50
00978AD3  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
00978AD7  33 DB                           xor ebx, ebx
00978AD9  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00978ADD  48 85 D2                        test rdx, rdx
00978AE0  74 1B                           je 0x140978afd
00978AE2  0F B7 45 48                     movzx eax, word ptr [rbp + 0x48]
00978AE6  66 85 C0                        test ax, ax
00978AE9  74 70                           je 0x140978b5b
00978AEB  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00978AEF  83 C0 02                        add eax, 2
00978AF2  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978AF6  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00978AFB  EB 1E                           jmp 0x140978b1b
00978AFD  48 85 C9                        test rcx, rcx
00978B00  74 59                           je 0x140978b5b
00978B02  0F B7 45 38                     movzx eax, word ptr [rbp + 0x38]
00978B06  66 85 C0                        test ax, ax
00978B09  74 50                           je 0x140978b5b
00978B0B  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00978B0F  83 C0 02                        add eax, 2
00978B12  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978B16  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00978B1B  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978B1F  48 8D 05 2A 5A 6A FF            lea rax, [rip - 0x95a5d6]
00978B26  48 8B 0D 6B D8 4E 00            mov rcx, qword ptr [rip + 0x4ed86b]
00978B2D  41 B9 01 00 00 00               mov r9d, 1
00978B33  C7 44 24 38 12 00 00 00         mov dword ptr [rsp + 0x38], 0x12
00978B3B  48 8B D7                        mov rdx, rdi
00978B3E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978B43  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978B48  E8 03 50 11 00                  call 0x140a8db50
00978B4D  8B D8                           mov ebx, eax
00978B4F  85 C0                           test eax, eax
00978B51  0F 88 15 F2 FF FF               js 0x140977d6c
00978B57  33 DB                           xor ebx, ebx
00978B59  EB 51                           jmp 0x140978bac
00978B5B  8B 07                           mov eax, dword ptr [rdi]
00978B5D  A8 01                           test al, 1
00978B5F  75 4B                           jne 0x140978bac
00978B61  48 85 D2                        test rdx, rdx
00978B64  74 05                           je 0x140978b6b
00978B66  48 85 C9                        test rcx, rcx
00978B69  75 06                           jne 0x140978b71
00978B6B  38 5C 24 62                     cmp byte ptr [rsp + 0x62], bl
00978B6F  75 3B                           jne 0x140978bac
00978B71  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978B75  48 8D 05 D4 59 6A FF            lea rax, [rip - 0x95a62c]
00978B7C  48 8B 0D 15 D8 4E 00            mov rcx, qword ptr [rip + 0x4ed815]
00978B83  41 B9 01 00 00 00               mov r9d, 1
00978B89  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00978B8D  48 8B D7                        mov rdx, rdi
00978B90  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00978B94  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00978B99  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00978B9D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978BA2  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978BA7  E8 A4 4F 11 00                  call 0x140a8db50
00978BAC  4D 85 E4                        test r12, r12
00978BAF  74 52                           je 0x140978c03
00978BB1  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
00978BB6  41 B9 01 00 00 00               mov r9d, 1
00978BBC  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978BC0  48 8B D7                        mov rdx, rdi
00978BC3  48 8B 0D CE D7 4E 00            mov rcx, qword ptr [rip + 0x4ed7ce]
00978BCA  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00978BCE  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978BD2  48 8D 05 8F B4 69 FF            lea rax, [rip - 0x964b71]
00978BD9  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00978BDE  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00978BE6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978BEB  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978BF0  E8 5B 4F 11 00                  call 0x140a8db50
00978BF5  45 33 E4                        xor r12d, r12d
00978BF8  8B D8                           mov ebx, eax
00978BFA  85 C0                           test eax, eax
00978BFC  79 4B                           jns 0x140978c49
00978BFE  E9 69 F1 FF FF                  jmp 0x140977d6c
00978C03  8B 07                           mov eax, dword ptr [rdi]
00978C05  45 33 E4                        xor r12d, r12d
00978C08  A8 01                           test al, 1
00978C0A  75 3D                           jne 0x140978c49
00978C0C  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978C10  48 8D 05 51 B4 69 FF            lea rax, [rip - 0x964baf]
00978C17  48 8B 0D 7A D7 4E 00            mov rcx, qword ptr [rip + 0x4ed77a]
00978C1E  45 8D 4C 24 01                  lea r9d, [r12 + 1]
00978C23  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00978C28  48 8B D7                        mov rdx, rdi
00978C2B  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00978C30  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00978C35  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00978C3A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978C3F  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978C44  E8 07 4F 11 00                  call 0x140a8db50
00978C49  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
00978C4D  48 85 C9                        test rcx, rcx
00978C50  74 4F                           je 0x140978ca1
00978C52  0F B7 45 68                     movzx eax, word ptr [rbp + 0x68]
00978C56  41 B9 01 00 00 00               mov r9d, 1
00978C5C  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978C60  48 8B D7                        mov rdx, rdi
00978C63  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00978C68  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978C6C  48 8D 05 6D B4 69 FF            lea rax, [rip - 0x964b93]
00978C73  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00978C78  48 8B 0D 19 D7 4E 00            mov rcx, qword ptr [rip + 0x4ed719]
00978C7F  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00978C87  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978C8C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978C91  E8 BA 4E 11 00                  call 0x140a8db50
00978C96  8B D8                           mov ebx, eax
00978C98  85 C0                           test eax, eax
00978C9A  79 49                           jns 0x140978ce5
00978C9C  E9 CB F0 FF FF                  jmp 0x140977d6c
00978CA1  8B 07                           mov eax, dword ptr [rdi]
00978CA3  A8 01                           test al, 1
00978CA5  75 3E                           jne 0x140978ce5
00978CA7  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978CAB  48 8D 05 2E B4 69 FF            lea rax, [rip - 0x964bd2]
00978CB2  48 8B 0D DF D6 4E 00            mov rcx, qword ptr [rip + 0x4ed6df]
00978CB9  41 B9 01 00 00 00               mov r9d, 1
00978CBF  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00978CC4  48 8B D7                        mov rdx, rdi
00978CC7  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00978CCC  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00978CD1  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00978CD6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978CDB  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978CE0  E8 6B 4E 11 00                  call 0x140a8db50
00978CE5  4C 8B 85 90 00 00 00            mov r8, qword ptr [rbp + 0x90]
00978CEC  8B 07                           mov eax, dword ptr [rdi]
00978CEE  4D 85 C0                        test r8, r8
00978CF1  74 58                           je 0x140978d4b
00978CF3  0F B7 8D 88 00 00 00            movzx ecx, word ptr [rbp + 0x88]
00978CFA  83 E0 01                        and eax, 1
00978CFD  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978D01  4D 8B CF                        mov r9, r15
00978D04  C1 E0 11                        shl eax, 0x11
00978D07  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978D0B  48 8D 05 86 A1 69 FF            lea rax, [rip - 0x965e7a]
00978D12  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00978D16  48 8B 0D 7B D6 4E 00            mov rcx, qword ptr [rip + 0x4ed67b]
00978D1D  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00978D22  41 B8 01 00 00 00               mov r8d, 1
00978D28  C7 44 24 30 12 20 00 00         mov dword ptr [rsp + 0x30], 0x2012
00978D30  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00978D35  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00978D3A  E8 61 D5 F7 FF                  call 0x1408f62a0
00978D3F  8B D8                           mov ebx, eax
00978D41  85 C0                           test eax, eax
00978D43  0F 88 23 F0 FF FF               js 0x140977d6c
00978D49  EB 42                           jmp 0x140978d8d
00978D4B  A8 01                           test al, 1
00978D4D  75 3E                           jne 0x140978d8d
00978D4F  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978D53  48 8D 05 3E A1 69 FF            lea rax, [rip - 0x965ec2]
00978D5A  48 8B 0D 37 D6 4E 00            mov rcx, qword ptr [rip + 0x4ed637]
00978D61  41 B9 01 00 00 00               mov r9d, 1
00978D67  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00978D6C  48 8B D7                        mov rdx, rdi
00978D6F  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00978D74  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00978D79  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00978D7E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978D83  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978D88  E8 C3 4D 11 00                  call 0x140a8db50
00978D8D  48 85 F6                        test rsi, rsi
00978D90  0F 84 FB 01 00 00               je 0x140978f91
00978D96  4C 39 65 B0                     cmp qword ptr [rbp - 0x50], r12
00978D9A  0F 84 F1 01 00 00               je 0x140978f91
00978DA0  4C 8D 8D E8 00 00 00            lea r9, [rbp + 0xe8]
00978DA7  48 8B CE                        mov rcx, rsi
00978DAA  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00978DAE  48 8D 55 A8                     lea rdx, [rbp - 0x58]
00978DB2  E8 D9 1A 00 00                  call 0x14097a890
00978DB7  8B D8                           mov ebx, eax
00978DB9  85 C0                           test eax, eax
00978DBB  0F 88 C3 01 00 00               js 0x140978f84
00978DC1  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
00978DC5  41 0F BA E5 0A                  bt r13d, 0xa
00978DCA  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
00978DCE  0F 92 C1                        setb cl
00978DD1  F6 05 DC F2 65 00 01            test byte ptr [rip + 0x65f2dc], 1
00978DD8  0F 94 C0                        sete al
00978DDB  84 C8                           test al, cl
00978DDD  75 58                           jne 0x140978e37
00978DDF  8B 07                           mov eax, dword ptr [rdi]
00978DE1  4D 8B CF                        mov r9, r15
00978DE4  0F B7 4D E8                     movzx ecx, word ptr [rbp - 0x18]
00978DE8  83 E0 01                        and eax, 1
00978DEB  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978DEF  83 C1 02                        add ecx, 2
00978DF2  C1 E0 11                        shl eax, 0x11
00978DF5  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978DF9  48 8D 05 28 B3 69 FF            lea rax, [rip - 0x964cd8]
00978E00  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00978E04  48 8B 0D 8D D5 4E 00            mov rcx, qword ptr [rip + 0x4ed58d]
00978E0B  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00978E10  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00978E18  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00978E1D  33 C0                           xor eax, eax
00978E1F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00978E24  44 8D 40 01                     lea r8d, [rax + 1]
00978E28  E8 73 D4 F7 FF                  call 0x1408f62a0
00978E2D  8B D8                           mov ebx, eax
00978E2F  85 C0                           test eax, eax
00978E31  0F 88 35 EF FF FF               js 0x140977d6c
00978E37  4C 8B 85 F0 00 00 00            mov r8, qword ptr [rbp + 0xf0]
00978E3E  33 DB                           xor ebx, ebx
00978E40  8B 07                           mov eax, dword ptr [rdi]
00978E42  4D 85 C0                        test r8, r8
00978E45  74 59                           je 0x140978ea0
00978E47  0F B7 8D E8 00 00 00            movzx ecx, word ptr [rbp + 0xe8]
00978E4E  83 E0 01                        and eax, 1
00978E51  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978E55  83 C1 02                        add ecx, 2
00978E58  C1 E0 11                        shl eax, 0x11
00978E5B  4D 8B CF                        mov r9, r15
00978E5E  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978E62  48 8D 05 7F A1 69 FF            lea rax, [rip - 0x965e81]
00978E69  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00978E6D  48 8B 0D 24 D5 4E 00            mov rcx, qword ptr [rip + 0x4ed524]
00978E74  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00978E79  44 8D 43 01                     lea r8d, [rbx + 1]
00978E7D  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00978E85  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00978E8A  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00978E8F  E8 0C D4 F7 FF                  call 0x1408f62a0
00978E94  8B D8                           mov ebx, eax
00978E96  85 C0                           test eax, eax
00978E98  0F 88 CE EE FF FF               js 0x140977d6c
00978E9E  EB 3F                           jmp 0x140978edf
00978EA0  A8 01                           test al, 1
00978EA2  75 3B                           jne 0x140978edf
00978EA4  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978EA8  48 8D 05 39 A1 69 FF            lea rax, [rip - 0x965ec7]
00978EAF  48 8B 0D E2 D4 4E 00            mov rcx, qword ptr [rip + 0x4ed4e2]
00978EB6  41 B9 01 00 00 00               mov r9d, 1
00978EBC  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00978EC0  48 8B D7                        mov rdx, rdi
00978EC3  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00978EC7  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00978ECC  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00978ED0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978ED5  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978EDA  E8 71 4C 11 00                  call 0x140a8db50
00978EDF  4D 85 E4                        test r12, r12
00978EE2  74 19                           je 0x140978efd
00978EE4  49 8B CC                        mov rcx, r12
00978EE7  E8 64 99 20 00                  call 0x140b82850
00978EEC  0F 57 C0                        xorps xmm0, xmm0
00978EEF  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00978EF3  66 0F 73 D8 08                  psrldq xmm0, 8
00978EF8  66 0F D6 45 D0                  movq qword ptr [rbp - 0x30], xmm0
00978EFD  45 33 E4                        xor r12d, r12d
00978F00  4C 39 65 E0                     cmp qword ptr [rbp - 0x20], r12
00978F04  0F 84 AD 01 00 00               je 0x1409790b7
00978F0A  45 33 C9                        xor r9d, r9d
00978F0D  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00978F11  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00978F15  48 8B CE                        mov rcx, rsi
00978F18  E8 73 19 00 00                  call 0x14097a890
00978F1D  8B D8                           mov ebx, eax
00978F1F  85 C0                           test eax, eax
00978F21  78 61                           js 0x140978f84
00978F23  0F B7 45 E8                     movzx eax, word ptr [rbp - 0x18]
00978F27  41 B9 01 00 00 00               mov r9d, 1
00978F2D  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978F31  83 C0 02                        add eax, 2
00978F34  48 8B 0D 5D D4 4E 00            mov rcx, qword ptr [rip + 0x4ed45d]
00978F3B  48 8B D7                        mov rdx, rdi
00978F3E  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00978F43  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
00978F47  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00978F4B  48 8D 05 C6 F1 6A FF            lea rax, [rip - 0x950e3a]
00978F52  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00978F57  C7 44 24 38 12 00 00 00         mov dword ptr [rsp + 0x38], 0x12
00978F5F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978F64  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978F69  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
00978F6D  E8 DE 4B 11 00                  call 0x140a8db50
00978F72  45 33 E4                        xor r12d, r12d
00978F75  8B D8                           mov ebx, eax
00978F77  85 C0                           test eax, eax
00978F79  0F 89 7C 01 00 00               jns 0x1409790fb
00978F7F  E9 E8 ED FF FF                  jmp 0x140977d6c
00978F84  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00978F88  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00978F8C  E9 DB ED FF FF                  jmp 0x140977d6c
00978F91  8B 07                           mov eax, dword ptr [rdi]
00978F93  A8 01                           test al, 1
00978F95  0F 85 19 02 00 00               jne 0x1409791b4
00978F9B  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00978F9F  48 8D 05 42 A0 69 FF            lea rax, [rip - 0x965fbe]
00978FA6  48 8B 0D EB D3 4E 00            mov rcx, qword ptr [rip + 0x4ed3eb]
00978FAD  41 B9 01 00 00 00               mov r9d, 1
00978FB3  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00978FB8  48 8B D7                        mov rdx, rdi
00978FBB  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00978FC0  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00978FC5  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00978FCA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00978FCF  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00978FD4  E8 77 4B 11 00                  call 0x140a8db50
00978FD9  48 85 F6                        test rsi, rsi
00978FDC  0F 85 1E FF FF FF               jne 0x140978f00
00978FE2  33 D2                           xor edx, edx
00978FE4  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00978FEB  41 B8 A0 00 00 00               mov r8d, 0xa0
00978FF1  E8 4A DC D4 FF                  call 0x1406c6c40
00978FF6  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00978FFA  48 8D 05 7F EC 6A FF            lea rax, [rip - 0x951381]
00979001  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00979008  8D 5E 01                        lea ebx, [rsi + 1]
0097900B  48 8D 45 A8                     lea rax, [rbp - 0x58]
0097900F  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00979013  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
0097901A  4D 8B CF                        mov r9, r15
0097901D  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00979024  C7 85 18 01 00 00 12 00 00 00   mov dword ptr [rbp + 0x118], 0x12
0097902E  44 8B C3                        mov r8d, ebx
00979031  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00979036  C7 85 2C 01 00 00 06 00 00 00   mov dword ptr [rbp + 0x12c], 6
00979040  E8 27 E7 FF FF                  call 0x14097776c
00979045  85 C0                           test eax, eax
00979047  0F 88 27 01 00 00               js 0x140979174
0097904D  44 39 A5 30 01 00 00            cmp dword ptr [rbp + 0x130], r12d
00979054  0F 8C 1A 01 00 00               jl 0x140979174
0097905A  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0097905E  48 85 C9                        test rcx, rcx
00979061  0F 84 0D 01 00 00               je 0x140979174
00979067  0F B7 45 A8                     movzx eax, word ptr [rbp - 0x58]
0097906B  44 8B CB                        mov r9d, ebx
0097906E  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979072  83 C0 02                        add eax, 2
00979075  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0097907A  48 8B D7                        mov rdx, rdi
0097907D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979081  8B 85 18 01 00 00               mov eax, dword ptr [rbp + 0x118]
00979087  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0097908C  48 8B 0D 05 D3 4E 00            mov rcx, qword ptr [rip + 0x4ed305]
00979093  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00979097  48 8D 05 8A B0 69 FF            lea rax, [rip - 0x964f76]
0097909E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009790A3  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009790A8  E8 A3 4A 11 00                  call 0x140a8db50
009790AD  8B D8                           mov ebx, eax
009790AF  85 C0                           test eax, eax
009790B1  0F 88 B5 EC FF FF               js 0x140977d6c
009790B7  8B 07                           mov eax, dword ptr [rdi]
009790B9  A8 01                           test al, 1
009790BB  75 3E                           jne 0x1409790fb
009790BD  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009790C1  48 8D 05 50 F0 6A FF            lea rax, [rip - 0x950fb0]
009790C8  48 8B 0D C9 D2 4E 00            mov rcx, qword ptr [rip + 0x4ed2c9]
009790CF  41 B9 01 00 00 00               mov r9d, 1
009790D5  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009790DA  48 8B D7                        mov rdx, rdi
009790DD  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009790E2  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009790E7  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009790EC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009790F1  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009790F6  E8 55 4A 11 00                  call 0x140a8db50
009790FB  48 85 F6                        test rsi, rsi
009790FE  0F 84 BE 00 00 00               je 0x1409791c2
00979104  4C 8B 86 18 01 00 00            mov r8, qword ptr [rsi + 0x118]
0097910B  4D 85 C0                        test r8, r8
0097910E  0F 84 AE 00 00 00               je 0x1409791c2
00979114  8B 07                           mov eax, dword ptr [rdi]
00979116  4D 8B CF                        mov r9, r15
00979119  0F B7 8E 10 01 00 00            movzx ecx, word ptr [rsi + 0x110]
00979120  83 E0 01                        and eax, 1
00979123  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979127  83 C1 02                        add ecx, 2
0097912A  C1 E0 11                        shl eax, 0x11
0097912D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979131  48 8D 05 98 9E 69 FF            lea rax, [rip - 0x966168]
00979138  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0097913C  48 8B 0D 55 D2 4E 00            mov rcx, qword ptr [rip + 0x4ed255]
00979143  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00979148  41 B8 01 00 00 00               mov r8d, 1
0097914E  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00979156  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0097915B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00979160  E8 3B D1 F7 FF                  call 0x1408f62a0
00979165  8B D8                           mov ebx, eax
00979167  85 C0                           test eax, eax
00979169  0F 89 A0 00 00 00               jns 0x14097920f
0097916F  E9 F8 EB FF FF                  jmp 0x140977d6c
00979174  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979178  48 8D 05 A9 AF 69 FF            lea rax, [rip - 0x965057]
0097917F  48 8B 0D 12 D2 4E 00            mov rcx, qword ptr [rip + 0x4ed212]
00979186  44 8B CB                        mov r9d, ebx
00979189  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0097918E  48 8B D7                        mov rdx, rdi
00979191  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979196  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0097919B  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009791A0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009791A5  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009791AA  E8 A1 49 11 00                  call 0x140a8db50
009791AF  E9 03 FF FF FF                  jmp 0x1409790b7
009791B4  48 85 F6                        test rsi, rsi
009791B7  0F 85 43 FD FF FF               jne 0x140978f00
009791BD  E9 F5 FE FF FF                  jmp 0x1409790b7
009791C2  8B 07                           mov eax, dword ptr [rdi]
009791C4  A8 01                           test al, 1
009791C6  75 3E                           jne 0x140979206
009791C8  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009791CC  48 8D 05 FD 9D 69 FF            lea rax, [rip - 0x966203]
009791D3  48 8B 0D BE D1 4E 00            mov rcx, qword ptr [rip + 0x4ed1be]
009791DA  41 B9 01 00 00 00               mov r9d, 1
009791E0  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009791E5  48 8B D7                        mov rdx, rdi
009791E8  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009791ED  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009791F2  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009791F7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009791FC  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979201  E8 4A 49 11 00                  call 0x140a8db50
00979206  48 85 F6                        test rsi, rsi
00979209  0F 84 77 02 00 00               je 0x140979486
0097920F  8B 0F                           mov ecx, dword ptr [rdi]
00979211  48 8D 46 70                     lea rax, [rsi + 0x70]
00979215  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979219  83 E1 01                        and ecx, 1
0097921C  C1 E1 11                        shl ecx, 0x11
0097921F  4D 8B CF                        mov r9, r15
00979222  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00979226  41 B8 01 00 00 00               mov r8d, 1
0097922C  48 8B 0D 65 D1 4E 00            mov rcx, qword ptr [rip + 0x4ed165]
00979233  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
0097923B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00979240  48 8D 05 11 9D 69 FF            lea rax, [rip - 0x9662ef]
00979247  C7 44 24 30 10 00 00 00         mov dword ptr [rsp + 0x30], 0x10
0097924F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00979254  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00979259  E8 42 D0 F7 FF                  call 0x1408f62a0
0097925E  8B D8                           mov ebx, eax
00979260  85 C0                           test eax, eax
00979262  0F 88 04 EB FF FF               js 0x140977d6c
00979268  0F B7 4E 78                     movzx ecx, word ptr [rsi + 0x78]
0097926C  0F B7 56 7A                     movzx edx, word ptr [rsi + 0x7a]
00979270  8B 46 7C                        mov eax, dword ptr [rsi + 0x7c]
00979273  44 0F B7 4E 7C                  movzx r9d, word ptr [rsi + 0x7c]
00979278  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0097927C  48 8D 8D D8 00 00 00            lea rcx, [rbp + 0xd8]
00979283  48 C1 E8 10                     shr rax, 0x10
00979287  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0097928B  48 8D 15 1E 56 18 00            lea rdx, [rip + 0x18561e]
00979292  44 0F B7 C0                     movzx r8d, ax
00979296  E8 E9 26 B1 FF                  call 0x14048b984
0097929B  8B D8                           mov ebx, eax
0097929D  85 C0                           test eax, eax
0097929F  0F 88 C7 EA FF FF               js 0x140977d6c
009792A5  8B 07                           mov eax, dword ptr [rdi]
009792A7  4D 8B CF                        mov r9, r15
009792AA  0F B7 8D D8 00 00 00            movzx ecx, word ptr [rbp + 0xd8]
009792B1  83 E0 01                        and eax, 1
009792B4  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
009792B8  83 C1 02                        add ecx, 2
009792BB  C1 E0 11                        shl eax, 0x11
009792BE  41 B8 01 00 00 00               mov r8d, 1
009792C4  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009792C8  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
009792CF  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
009792D3  48 8B 0D BE D0 4E 00            mov rcx, qword ptr [rip + 0x4ed0be]
009792DA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009792DF  48 8D 05 D2 9C 69 FF            lea rax, [rip - 0x96632e]
009792E6  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
009792EE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009792F3  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009792F8  E8 A3 CF F7 FF                  call 0x1408f62a0
009792FD  8B D8                           mov ebx, eax
009792FF  85 C0                           test eax, eax
00979301  0F 88 65 EA FF FF               js 0x140977d6c
00979307  8B 07                           mov eax, dword ptr [rdi]
00979309  4D 8B CF                        mov r9, r15
0097930C  0F B7 56 28                     movzx edx, word ptr [rsi + 0x28]
00979310  83 E0 01                        and eax, 1
00979313  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00979317  83 C2 02                        add edx, 2
0097931A  C1 E0 11                        shl eax, 0x11
0097931D  41 B8 01 00 00 00               mov r8d, 1
00979323  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979327  48 8D 05 72 9C 69 FF            lea rax, [rip - 0x96638e]
0097932E  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00979332  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979336  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0097933B  48 8B 0D 56 D0 4E 00            mov rcx, qword ptr [rip + 0x4ed056]
00979342  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
0097934A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0097934F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00979354  E8 47 CF F7 FF                  call 0x1408f62a0
00979359  8B D8                           mov ebx, eax
0097935B  85 C0                           test eax, eax
0097935D  0F 88 09 EA FF FF               js 0x140977d6c
00979363  8B 07                           mov eax, dword ptr [rdi]
00979365  4D 8B CF                        mov r9, r15
00979368  0F B7 56 58                     movzx edx, word ptr [rsi + 0x58]
0097936C  83 E0 01                        and eax, 1
0097936F  48 8B 4E 60                     mov rcx, qword ptr [rsi + 0x60]
00979373  83 C2 02                        add edx, 2
00979376  C1 E0 11                        shl eax, 0x11
00979379  41 B8 01 00 00 00               mov r8d, 1
0097937F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979383  48 8D 05 E6 9B 69 FF            lea rax, [rip - 0x96641a]
0097938A  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
0097938E  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979392  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00979397  48 8B 0D FA CF 4E 00            mov rcx, qword ptr [rip + 0x4ecffa]
0097939E  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
009793A6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009793AB  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009793B0  E8 EB CE F7 FF                  call 0x1408f62a0
009793B5  8B D8                           mov ebx, eax
009793B7  85 C0                           test eax, eax
009793B9  0F 88 AD E9 FF FF               js 0x140977d6c
009793BF  4C 8D 4D B8                     lea r9, [rbp - 0x48]
009793C3  48 8B CE                        mov rcx, rsi
009793C6  4C 8D 45 A8                     lea r8, [rbp - 0x58]
009793CA  48 8D 55 D8                     lea rdx, [rbp - 0x28]
009793CE  E8 69 0F 00 00                  call 0x14097a33c
009793D3  8B D8                           mov ebx, eax
009793D5  85 C0                           test eax, eax
009793D7  0F 88 8F E9 FF FF               js 0x140977d6c
009793DD  48 8B 4D 00                     mov rcx, qword ptr [rbp]
009793E1  48 85 C9                        test rcx, rcx
009793E4  74 2A                           je 0x140979410
009793E6  44 0F B7 4D B8                  movzx r9d, word ptr [rbp - 0x48]
009793EB  0F B7 55 F8                     movzx edx, word ptr [rbp - 8]
009793EF  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
009793F3  49 D1 E9                        shr r9, 1
009793F6  48 D1 EA                        shr rdx, 1
009793F9  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
009793FE  E8 DD 93 FF FF                  call 0x1409727e0
00979403  85 C0                           test eax, eax
00979405  75 09                           jne 0x140979410
00979407  48 8D 4D F8                     lea rcx, [rbp - 8]
0097940B  E8 F0 73 04 00                  call 0x1409c0800
00979410  8B 07                           mov eax, dword ptr [rdi]
00979412  4D 8B CF                        mov r9, r15
00979415  0F B7 4D B8                     movzx ecx, word ptr [rbp - 0x48]
00979419  83 E0 01                        and eax, 1
0097941C  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979420  83 C1 02                        add ecx, 2
00979423  C1 E0 11                        shl eax, 0x11
00979426  41 B8 01 00 00 00               mov r8d, 1
0097942C  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979430  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00979434  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00979438  48 8B 0D 59 CF 4E 00            mov rcx, qword ptr [rip + 0x4ecf59]
0097943F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00979444  48 8D 05 3D 9B 69 FF            lea rax, [rip - 0x9664c3]
0097944B  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00979453  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00979458  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0097945D  E8 3E CE F7 FF                  call 0x1408f62a0
00979462  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00979466  8B D8                           mov ebx, eax
00979468  48 85 C9                        test rcx, rcx
0097946B  74 0C                           je 0x140979479
0097946D  E8 DE 93 20 00                  call 0x140b82850
00979472  0F 57 C0                        xorps xmm0, xmm0
00979475  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00979479  85 DB                           test ebx, ebx
0097947B  0F 88 EB E8 FF FF               js 0x140977d6c
00979481  E9 40 01 00 00                  jmp 0x1409795c6
00979486  8B 07                           mov eax, dword ptr [rdi]
00979488  A8 01                           test al, 1
0097948A  0F 85 36 01 00 00               jne 0x1409795c6
00979490  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979494  48 8D 05 BD 9A 69 FF            lea rax, [rip - 0x966543]
0097949B  48 8B 0D F6 CE 4E 00            mov rcx, qword ptr [rip + 0x4ecef6]
009794A2  41 B9 01 00 00 00               mov r9d, 1
009794A8  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009794AD  48 8B D7                        mov rdx, rdi
009794B0  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009794B5  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009794BA  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009794BF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009794C4  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009794C9  E8 82 46 11 00                  call 0x140a8db50
009794CE  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009794D2  48 8D 05 DF 9A 69 FF            lea rax, [rip - 0x966521]
009794D9  48 8B 0D B8 CE 4E 00            mov rcx, qword ptr [rip + 0x4eceb8]
009794E0  41 B9 01 00 00 00               mov r9d, 1
009794E6  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009794EB  48 8B D7                        mov rdx, rdi
009794EE  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009794F3  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009794F8  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009794FD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979502  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979507  E8 44 46 11 00                  call 0x140a8db50
0097950C  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979510  48 8D 05 89 9A 69 FF            lea rax, [rip - 0x966577]
00979517  48 8B 0D 7A CE 4E 00            mov rcx, qword ptr [rip + 0x4ece7a]
0097951E  41 B9 01 00 00 00               mov r9d, 1
00979524  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979529  48 8B D7                        mov rdx, rdi
0097952C  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979531  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979536  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0097953B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979540  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979545  E8 06 46 11 00                  call 0x140a8db50
0097954A  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
0097954E  48 8D 05 1B 9A 69 FF            lea rax, [rip - 0x9665e5]
00979555  48 8B 0D 3C CE 4E 00            mov rcx, qword ptr [rip + 0x4ece3c]
0097955C  41 B9 01 00 00 00               mov r9d, 1
00979562  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979567  48 8B D7                        mov rdx, rdi
0097956A  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
0097956F  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979574  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979579  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0097957E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979583  E8 C8 45 11 00                  call 0x140a8db50
00979588  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
0097958C  48 8D 05 F5 99 69 FF            lea rax, [rip - 0x96660b]
00979593  48 8B 0D FE CD 4E 00            mov rcx, qword ptr [rip + 0x4ecdfe]
0097959A  41 B9 01 00 00 00               mov r9d, 1
009795A0  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009795A5  48 8B D7                        mov rdx, rdi
009795A8  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009795AD  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009795B2  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009795B7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009795BC  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009795C1  E8 8A 45 11 00                  call 0x140a8db50
009795C6  48 8B 4D 00                     mov rcx, qword ptr [rbp]
009795CA  48 85 C9                        test rcx, rcx
009795CD  74 68                           je 0x140979637
009795CF  F6 45 98 08                     test byte ptr [rbp - 0x68], 8
009795D3  75 62                           jne 0x140979637
009795D5  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
009795D9  F7 80 8C 01 00 00 00 60 00 00   test dword ptr [rax + 0x18c], 0x6000
009795E3  75 52                           jne 0x140979637
009795E5  0F B7 45 F8                     movzx eax, word ptr [rbp - 8]
009795E9  41 B9 01 00 00 00               mov r9d, 1
009795EF  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009795F3  83 C0 02                        add eax, 2
009795F6  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009795FB  48 8B D7                        mov rdx, rdi
009795FE  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979602  48 8D 05 DF 98 6A FF            lea rax, [rip - 0x956721]
00979609  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0097960E  48 8B 0D 83 CD 4E 00            mov rcx, qword ptr [rip + 0x4ecd83]
00979615  C7 44 24 38 12 00 00 00         mov dword ptr [rsp + 0x38], 0x12
0097961D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979622  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979627  E8 24 45 11 00                  call 0x140a8db50
0097962C  8B D8                           mov ebx, eax
0097962E  85 C0                           test eax, eax
00979630  79 49                           jns 0x14097967b
00979632  E9 35 E7 FF FF                  jmp 0x140977d6c
00979637  8B 07                           mov eax, dword ptr [rdi]
00979639  A8 01                           test al, 1
0097963B  75 3E                           jne 0x14097967b
0097963D  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979641  48 8D 05 A0 98 6A FF            lea rax, [rip - 0x956760]
00979648  48 8B 0D 49 CD 4E 00            mov rcx, qword ptr [rip + 0x4ecd49]
0097964F  41 B9 01 00 00 00               mov r9d, 1
00979655  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0097965A  48 8B D7                        mov rdx, rdi
0097965D  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979662  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979667  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0097966C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979671  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979676  E8 D5 44 11 00                  call 0x140a8db50
0097967B  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
00979682  48 85 C9                        test rcx, rcx
00979685  74 52                           je 0x1409796d9
00979687  0F B7 85 98 00 00 00            movzx eax, word ptr [rbp + 0x98]
0097968E  41 B9 01 00 00 00               mov r9d, 1
00979694  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979698  48 8B D7                        mov rdx, rdi
0097969B  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009796A0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009796A4  48 8D 05 55 7F 6A FF            lea rax, [rip - 0x9580ab]
009796AB  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009796B0  48 8B 0D E1 CC 4E 00            mov rcx, qword ptr [rip + 0x4ecce1]
009796B7  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
009796BF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009796C4  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009796C9  E8 82 44 11 00                  call 0x140a8db50
009796CE  8B D8                           mov ebx, eax
009796D0  85 C0                           test eax, eax
009796D2  79 49                           jns 0x14097971d
009796D4  E9 93 E6 FF FF                  jmp 0x140977d6c
009796D9  8B 07                           mov eax, dword ptr [rdi]
009796DB  A8 01                           test al, 1
009796DD  75 3E                           jne 0x14097971d
009796DF  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009796E3  48 8D 05 16 7F 6A FF            lea rax, [rip - 0x9580ea]
009796EA  48 8B 0D A7 CC 4E 00            mov rcx, qword ptr [rip + 0x4ecca7]
009796F1  41 B9 01 00 00 00               mov r9d, 1
009796F7  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009796FC  48 8B D7                        mov rdx, rdi
009796FF  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979704  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979709  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0097970E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979713  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979718  E8 33 44 11 00                  call 0x140a8db50
0097971D  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
00979724  48 85 C9                        test rcx, rcx
00979727  74 52                           je 0x14097977b
00979729  0F B7 85 A8 00 00 00            movzx eax, word ptr [rbp + 0xa8]
00979730  41 B9 01 00 00 00               mov r9d, 1
00979736  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
0097973A  48 8B D7                        mov rdx, rdi
0097973D  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979742  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979746  48 8D 05 CB 8C 6A FF            lea rax, [rip - 0x957335]
0097974D  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00979752  48 8B 0D 3F CC 4E 00            mov rcx, qword ptr [rip + 0x4ecc3f]
00979759  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00979761  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979766  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0097976B  E8 E0 43 11 00                  call 0x140a8db50
00979770  8B D8                           mov ebx, eax
00979772  85 C0                           test eax, eax
00979774  79 49                           jns 0x1409797bf
00979776  E9 F1 E5 FF FF                  jmp 0x140977d6c
0097977B  8B 07                           mov eax, dword ptr [rdi]
0097977D  A8 01                           test al, 1
0097977F  75 3E                           jne 0x1409797bf
00979781  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979785  48 8D 05 8C 8C 6A FF            lea rax, [rip - 0x957374]
0097978C  48 8B 0D 05 CC 4E 00            mov rcx, qword ptr [rip + 0x4ecc05]
00979793  41 B9 01 00 00 00               mov r9d, 1
00979799  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0097979E  48 8B D7                        mov rdx, rdi
009797A1  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009797A6  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009797AB  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009797B0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009797B5  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009797BA  E8 91 43 11 00                  call 0x140a8db50
009797BF  48 8B 8D C0 00 00 00            mov rcx, qword ptr [rbp + 0xc0]
009797C6  48 85 C9                        test rcx, rcx
009797C9  74 52                           je 0x14097981d
009797CB  0F B7 85 B8 00 00 00            movzx eax, word ptr [rbp + 0xb8]
009797D2  41 B9 01 00 00 00               mov r9d, 1
009797D8  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009797DC  48 8B D7                        mov rdx, rdi
009797DF  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009797E4  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009797E8  48 8D 05 31 98 6A FF            lea rax, [rip - 0x9567cf]
009797EF  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009797F4  48 8B 0D 9D CB 4E 00            mov rcx, qword ptr [rip + 0x4ecb9d]
009797FB  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00979803  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979808  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0097980D  E8 3E 43 11 00                  call 0x140a8db50
00979812  8B D8                           mov ebx, eax
00979814  85 C0                           test eax, eax
00979816  79 49                           jns 0x140979861
00979818  E9 4F E5 FF FF                  jmp 0x140977d6c
0097981D  8B 07                           mov eax, dword ptr [rdi]
0097981F  A8 01                           test al, 1
00979821  75 3E                           jne 0x140979861
00979823  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979827  48 8D 05 F2 97 6A FF            lea rax, [rip - 0x95680e]
0097982E  48 8B 0D 63 CB 4E 00            mov rcx, qword ptr [rip + 0x4ecb63]
00979835  41 B9 01 00 00 00               mov r9d, 1
0097983B  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979840  48 8B D7                        mov rdx, rdi
00979843  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979848  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0097984D  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979852  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979857  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0097985C  E8 EF 42 11 00                  call 0x140a8db50
00979861  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
00979868  48 85 C9                        test rcx, rcx
0097986B  74 52                           je 0x1409798bf
0097986D  0F B7 85 C8 00 00 00            movzx eax, word ptr [rbp + 0xc8]
00979874  41 B9 01 00 00 00               mov r9d, 1
0097987A  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
0097987E  48 8B D7                        mov rdx, rdi
00979881  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979886  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0097988A  48 8D 05 5F 81 6A FF            lea rax, [rip - 0x957ea1]
00979891  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00979896  48 8B 0D FB CA 4E 00            mov rcx, qword ptr [rip + 0x4ecafb]
0097989D  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
009798A5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009798AA  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009798AF  E8 9C 42 11 00                  call 0x140a8db50
009798B4  8B D8                           mov ebx, eax
009798B6  85 C0                           test eax, eax
009798B8  79 49                           jns 0x140979903
009798BA  E9 AD E4 FF FF                  jmp 0x140977d6c
009798BF  8B 07                           mov eax, dword ptr [rdi]
009798C1  A8 01                           test al, 1
009798C3  75 3E                           jne 0x140979903
009798C5  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009798C9  48 8D 05 20 81 6A FF            lea rax, [rip - 0x957ee0]
009798D0  48 8B 0D C1 CA 4E 00            mov rcx, qword ptr [rip + 0x4ecac1]
009798D7  41 B9 01 00 00 00               mov r9d, 1
009798DD  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009798E2  48 8B D7                        mov rdx, rdi
009798E5  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009798EA  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009798EF  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
009798F4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009798F9  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009798FE  E8 4D 42 11 00                  call 0x140a8db50
00979903  48 85 F6                        test rsi, rsi
00979906  0F 84 CA 00 00 00               je 0x1409799d6
0097990C  4C 8D 66 6C                     lea r12, [rsi + 0x6c]
00979910  41 83 3C 24 FF                  cmp dword ptr [r12], -1
00979915  0F 84 B8 00 00 00               je 0x1409799d3
0097991B  8B 07                           mov eax, dword ptr [rdi]
0097991D  4D 8B CF                        mov r9, r15
00979920  0F B7 56 48                     movzx edx, word ptr [rsi + 0x48]
00979924  83 E0 01                        and eax, 1
00979927  48 8B 4E 50                     mov rcx, qword ptr [rsi + 0x50]
0097992B  83 C2 02                        add edx, 2
0097992E  C1 E0 11                        shl eax, 0x11
00979931  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979935  48 8D 05 DC 96 69 FF            lea rax, [rip - 0x966924]
0097993C  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00979940  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979944  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00979949  48 8B 0D 48 CA 4E 00            mov rcx, qword ptr [rip + 0x4eca48]
00979950  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00979958  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0097995D  33 C0                           xor eax, eax
0097995F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00979964  44 8D 40 01                     lea r8d, [rax + 1]
00979968  E8 33 C9 F7 FF                  call 0x1408f62a0
0097996D  8B D8                           mov ebx, eax
0097996F  85 C0                           test eax, eax
00979971  0F 88 F5 E3 FF FF               js 0x140977d6c
00979977  8B 07                           mov eax, dword ptr [rdi]
00979979  4D 8B CF                        mov r9, r15
0097997C  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979980  83 E0 01                        and eax, 1
00979983  48 8B 0D 0E CA 4E 00            mov rcx, qword ptr [rip + 0x4eca0e]
0097998A  C1 E0 11                        shl eax, 0x11
0097998D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979991  48 8D 05 68 96 69 FF            lea rax, [rip - 0x966998]
00979998  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
009799A0  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
009799A5  45 33 E4                        xor r12d, r12d
009799A8  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
009799B0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009799B5  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009799BA  45 8D 44 24 01                  lea r8d, [r12 + 1]
009799BF  E8 DC C8 F7 FF                  call 0x1408f62a0
009799C4  8B D8                           mov ebx, eax
009799C6  85 C0                           test eax, eax
009799C8  0F 88 9E E3 FF FF               js 0x140977d6c
009799CE  E9 85 00 00 00                  jmp 0x140979a58
009799D3  45 33 E4                        xor r12d, r12d
009799D6  8B 07                           mov eax, dword ptr [rdi]
009799D8  A8 01                           test al, 1
009799DA  75 7C                           jne 0x140979a58
009799DC  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
009799E0  48 8D 05 31 96 69 FF            lea rax, [rip - 0x9669cf]
009799E7  48 8B 0D AA C9 4E 00            mov rcx, qword ptr [rip + 0x4ec9aa]
009799EE  41 B9 01 00 00 00               mov r9d, 1
009799F4  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
009799F9  48 8B D7                        mov rdx, rdi
009799FC  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979A01  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979A06  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979A0B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979A10  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979A15  E8 36 41 11 00                  call 0x140a8db50
00979A1A  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979A1E  48 8D 05 DB 95 69 FF            lea rax, [rip - 0x966a25]
00979A25  48 8B 0D 6C C9 4E 00            mov rcx, qword ptr [rip + 0x4ec96c]
00979A2C  41 B9 01 00 00 00               mov r9d, 1
00979A32  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979A37  48 8B D7                        mov rdx, rdi
00979A3A  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979A3F  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979A44  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979A49  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979A4E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979A53  E8 F8 40 11 00                  call 0x140a8db50
00979A58  44 39 65 98                     cmp dword ptr [rbp - 0x68], r12d
00979A5C  74 3E                           je 0x140979a9c
00979A5E  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979A62  48 8D 05 57 8F 6A FF            lea rax, [rip - 0x9570a9]
00979A69  48 8B 0D 28 C9 4E 00            mov rcx, qword ptr [rip + 0x4ec928]
00979A70  41 B9 01 00 00 00               mov r9d, 1
00979A76  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979A7B  48 8B D7                        mov rdx, rdi
00979A7E  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979A83  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979A88  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979A8D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979A92  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979A97  E8 B4 40 11 00                  call 0x140a8db50
00979A9C  48 85 F6                        test rsi, rsi
00979A9F  0F 84 F5 00 00 00               je 0x140979b9a
00979AA5  4C 8B 65 30                     mov r12, qword ptr [rbp + 0x30]
00979AA9  45 89 2C 24                     mov dword ptr [r12], r13d
00979AAD  F6 86 B8 00 00 00 08            test byte ptr [rsi + 0xb8], 8
00979AB4  0F 95 C1                        setne cl
00979AB7  F6 05 72 E5 65 00 02            test byte ptr [rip + 0x65e572], 2
00979ABE  0F 95 C0                        setne al
00979AC1  84 C8                           test al, cl
00979AC3  74 09                           je 0x140979ace
00979AC5  41 0F BA ED 0A                  bts r13d, 0xa
00979ACA  45 89 2C 24                     mov dword ptr [r12], r13d
00979ACE  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00979AD2  48 8D 45 90                     lea rax, [rbp - 0x70]
00979AD6  4C 8D 4C 24 64                  lea r9, [rsp + 0x64]
00979ADB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00979AE0  4C 8B C6                        mov r8, rsi
00979AE3  48 8B D7                        mov rdx, rdi
00979AE6  E8 D1 9F FE FF                  call 0x140963abc
00979AEB  8B D8                           mov ebx, eax
00979AED  85 C0                           test eax, eax
00979AEF  0F 88 77 E2 FF FF               js 0x140977d6c
00979AF5  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00979AF9  4C 8D AE D0 00 00 00            lea r13, [rsi + 0xd0]
00979B00  41 09 04 24                     or dword ptr [r12], eax
00979B04  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00979B08  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00979B0B  09 01                           or dword ptr [rcx], eax
00979B0D  4D 8B 65 00                     mov r12, qword ptr [r13]
00979B11  EB 4A                           jmp 0x140979b5d
00979B13  41 8B 84 24 B8 00 00 00         mov eax, dword ptr [r12 + 0xb8]
00979B1B  A8 01                           test al, 1
00979B1D  74 3A                           je 0x140979b59
00979B1F  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00979B23  48 8D 45 90                     lea rax, [rbp - 0x70]
00979B27  4C 8D 4C 24 64                  lea r9, [rsp + 0x64]
00979B2C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00979B31  4D 8B C4                        mov r8, r12
00979B34  48 8B D7                        mov rdx, rdi
00979B37  E8 80 9F FE FF                  call 0x140963abc
00979B3C  8B D8                           mov ebx, eax
00979B3E  85 C0                           test eax, eax
00979B40  0F 88 26 E2 FF FF               js 0x140977d6c
00979B46  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00979B4A  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00979B4E  09 01                           or dword ptr [rcx], eax
00979B50  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00979B54  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00979B57  09 01                           or dword ptr [rcx], eax
00979B59  4D 8B 24 24                     mov r12, qword ptr [r12]
00979B5D  4D 3B E5                        cmp r12, r13
00979B60  75 B1                           jne 0x140979b13
00979B62  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00979B66  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00979B6A  4C 8D 44 24 64                  lea r8, [rsp + 0x64]
00979B6F  48 8B D7                        mov rdx, rdi
00979B72  E8 49 ED 12 00                  call 0x140aa88c0
00979B77  8B D8                           mov ebx, eax
00979B79  85 C0                           test eax, eax
00979B7B  0F 88 EB E1 FF FF               js 0x140977d6c
00979B81  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00979B85  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00979B89  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00979B8D  41 09 45 00                     or dword ptr [r13], eax
00979B91  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00979B94  41 09 04 24                     or dword ptr [r12], eax
00979B98  EB 33                           jmp 0x140979bcd
00979B9A  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
00979B9E  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00979BA2  41 F7 82 30 02 00 00 00 01 00 00  test dword ptr [r10 + 0x230], 0x100
00979BAD  74 0A                           je 0x140979bb9
00979BAF  45 89 65 00                     mov dword ptr [r13], r12d
00979BB3  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00979BB7  EB 18                           jmp 0x140979bd1
00979BB9  49 8B CE                        mov rcx, r14
00979BBC  41 C7 45 00 40 00 00 00         mov dword ptr [r13], 0x40
00979BC4  E8 C3 04 00 00                  call 0x14097a08c
00979BC9  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00979BCD  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
00979BD1  45 33 C9                        xor r9d, r9d
00979BD4  44 39 4D 94                     cmp dword ptr [rbp - 0x6c], r9d
00979BD8  74 1A                           je 0x140979bf4
00979BDA  44 38 0D 67 A5 64 00            cmp byte ptr [rip + 0x64a567], r9b
00979BE1  75 11                           jne 0x140979bf4
00979BE3  49 8B CA                        mov rcx, r10
00979BE6  E8 85 6C AF FF                  call 0x140470870
00979BEB  85 C0                           test eax, eax
00979BED  74 05                           je 0x140979bf4
00979BEF  41 83 0C 24 10                  or dword ptr [r12], 0x10
00979BF4  F6 45 98 02                     test byte ptr [rbp - 0x68], 2
00979BF8  74 05                           je 0x140979bff
00979BFA  41 83 0C 24 20                  or dword ptr [r12], 0x20
00979BFF  44 38 4C 24 63                  cmp byte ptr [rsp + 0x63], r9b
00979C04  74 05                           je 0x140979c0b
00979C06  41 83 0C 24 01                  or dword ptr [r12], 1
00979C0B  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
00979C0F  4D 85 C0                        test r8, r8
00979C12  74 3B                           je 0x140979c4f
00979C14  48 8D 45 90                     lea rax, [rbp - 0x70]
00979C18  41 83 C9 FF                     or r9d, 0xffffffff
00979C1C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00979C21  48 8B D7                        mov rdx, rdi
00979C24  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00979C29  49 8B CA                        mov rcx, r10
00979C2C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00979C31  E8 72 AF FE FF                  call 0x140964ba8
00979C36  8B D8                           mov ebx, eax
00979C38  85 C0                           test eax, eax
00979C3A  0F 88 2C E1 FF FF               js 0x140977d6c
00979C40  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00979C44  41 09 45 00                     or dword ptr [r13], eax
00979C48  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00979C4B  41 09 04 24                     or dword ptr [r12], eax
00979C4F  41 8B 04 24                     mov eax, dword ptr [r12]
00979C53  45 33 E4                        xor r12d, r12d
00979C56  A8 02                           test al, 2
00979C58  75 38                           jne 0x140979c92
00979C5A  80 7C 24 61 FF                  cmp byte ptr [rsp + 0x61], 0xff
00979C5F  75 31                           jne 0x140979c92
00979C61  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
00979C65  48 85 C0                        test rax, rax
00979C68  74 28                           je 0x140979c92
00979C6A  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
00979C6E  48 85 D2                        test rdx, rdx
00979C71  74 1F                           je 0x140979c92
00979C73  4C 8D 44 24 64                  lea r8, [rsp + 0x64]
00979C78  48 8B C8                        mov rcx, rax
00979C7B  E8 C8 D5 14 00                  call 0x140ac7248
00979C80  8B D8                           mov ebx, eax
00979C82  85 C0                           test eax, eax
00979C84  0F 88 E2 E0 FF FF               js 0x140977d6c
00979C8A  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00979C8E  41 09 45 00                     or dword ptr [r13], eax
00979C92  48 85 F6                        test rsi, rsi
00979C95  74 09                           je 0x140979ca0
00979C97  0F 10 86 A8 01 00 00            movups xmm0, xmmword ptr [rsi + 0x1a8]
00979C9E  EB 07                           jmp 0x140979ca7
00979CA0  0F 10 05 61 10 1D 00            movups xmm0, xmmword ptr [rip + 0x1d1061]
00979CA7  8B 07                           mov eax, dword ptr [rdi]
00979CA9  4D 8B CF                        mov r9, r15
00979CAC  48 8B 0D E5 C6 4E 00            mov rcx, qword ptr [rip + 0x4ec6e5]
00979CB3  83 E0 01                        and eax, 1
00979CB6  C1 E0 11                        shl eax, 0x11
00979CB9  41 B8 01 00 00 00               mov r8d, 1
00979CBF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979CC3  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
00979CC8  0F B7 55 B8                     movzx edx, word ptr [rbp - 0x48]
00979CCC  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00979CD0  83 C2 02                        add edx, 2
00979CD3  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00979CD7  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00979CDB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00979CE0  48 8D 05 C9 91 69 FF            lea rax, [rip - 0x966e37]
00979CE7  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00979CEF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00979CF4  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00979CF9  E8 A2 C5 F7 FF                  call 0x1408f62a0
00979CFE  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00979D02  8B D8                           mov ebx, eax
00979D04  85 C0                           test eax, eax
00979D06  0F 88 64 E0 FF FF               js 0x140977d70
00979D0C  4D 85 ED                        test r13, r13
00979D0F  74 4F                           je 0x140979d60
00979D11  0F B7 45 80                     movzx eax, word ptr [rbp - 0x80]
00979D15  41 B9 01 00 00 00               mov r9d, 1
00979D1B  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979D1F  48 8B D7                        mov rdx, rdi
00979D22  48 8B 0D 6F C6 4E 00            mov rcx, qword ptr [rip + 0x4ec66f]
00979D29  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979D2E  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979D32  48 8D 05 CF E1 6A FF            lea rax, [rip - 0x951e31]
00979D39  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00979D3E  C7 44 24 38 12 20 00 00         mov dword ptr [rsp + 0x38], 0x2012
00979D46  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979D4B  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979D50  E8 FB 3D 11 00                  call 0x140a8db50
00979D55  8B D8                           mov ebx, eax
00979D57  85 C0                           test eax, eax
00979D59  79 49                           jns 0x140979da4
00979D5B  E9 10 E0 FF FF                  jmp 0x140977d70
00979D60  8B 07                           mov eax, dword ptr [rdi]
00979D62  A8 01                           test al, 1
00979D64  75 3E                           jne 0x140979da4
00979D66  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979D6A  48 8D 05 97 E1 6A FF            lea rax, [rip - 0x951e69]
00979D71  48 8B 0D 20 C6 4E 00            mov rcx, qword ptr [rip + 0x4ec620]
00979D78  41 B9 01 00 00 00               mov r9d, 1
00979D7E  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979D83  48 8B D7                        mov rdx, rdi
00979D86  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979D8B  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979D90  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979D95  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979D9A  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979D9F  E8 AC 3D 11 00                  call 0x140a8db50
00979DA4  48 85 F6                        test rsi, rsi
00979DA7  74 61                           je 0x140979e0a
00979DA9  48 8B 8E 88 00 00 00            mov rcx, qword ptr [rsi + 0x88]
00979DB0  48 85 C9                        test rcx, rcx
00979DB3  74 55                           je 0x140979e0a
00979DB5  0F B7 86 80 00 00 00            movzx eax, word ptr [rsi + 0x80]
00979DBC  41 B9 01 00 00 00               mov r9d, 1
00979DC2  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979DC6  83 C0 02                        add eax, 2
00979DC9  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979DCE  48 8B D7                        mov rdx, rdi
00979DD1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979DD5  48 8D 05 EC 89 6A FF            lea rax, [rip - 0x957614]
00979DDC  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00979DE1  48 8B 0D B0 C5 4E 00            mov rcx, qword ptr [rip + 0x4ec5b0]
00979DE8  C7 44 24 38 12 00 00 00         mov dword ptr [rsp + 0x38], 0x12
00979DF0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979DF5  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979DFA  E8 51 3D 11 00                  call 0x140a8db50
00979DFF  8B D8                           mov ebx, eax
00979E01  85 C0                           test eax, eax
00979E03  79 49                           jns 0x140979e4e
00979E05  E9 66 DF FF FF                  jmp 0x140977d70
00979E0A  8B 07                           mov eax, dword ptr [rdi]
00979E0C  A8 01                           test al, 1
00979E0E  75 3E                           jne 0x140979e4e
00979E10  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979E14  48 8D 05 AD 89 6A FF            lea rax, [rip - 0x957653]
00979E1B  48 8B 0D 76 C5 4E 00            mov rcx, qword ptr [rip + 0x4ec576]
00979E22  41 B9 01 00 00 00               mov r9d, 1
00979E28  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979E2D  48 8B D7                        mov rdx, rdi
00979E30  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979E35  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979E3A  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979E3F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979E44  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979E49  E8 02 3D 11 00                  call 0x140a8db50
00979E4E  44 8B 65 9C                     mov r12d, dword ptr [rbp - 0x64]
00979E52  45 84 E4                        test r12b, r12b
00979E55  79 5A                           jns 0x140979eb1
00979E57  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979E5B  33 C0                           xor eax, eax
00979E5D  48 8B 0D 34 C5 4E 00            mov rcx, qword ptr [rip + 0x4ec534]
00979E64  41 B9 01 00 00 00               mov r9d, 1
00979E6A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00979E6E  48 8B D7                        mov rdx, rdi
00979E71  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
00979E79  48 8D 44 24 79                  lea rax, [rsp + 0x79]
00979E7E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00979E83  48 8D 05 8E 93 6A FF            lea rax, [rip - 0x956c72]
00979E8A  C7 44 24 38 11 00 00 00         mov dword ptr [rsp + 0x38], 0x11
00979E92  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979E97  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979E9C  C6 44 24 79 FF                  mov byte ptr [rsp + 0x79], 0xff
00979EA1  E8 AA 3C 11 00                  call 0x140a8db50
00979EA6  8B D8                           mov ebx, eax
00979EA8  85 C0                           test eax, eax
00979EAA  79 48                           jns 0x140979ef4
00979EAC  E9 BF DE FF FF                  jmp 0x140977d70
00979EB1  8B 07                           mov eax, dword ptr [rdi]
00979EB3  A8 01                           test al, 1
00979EB5  75 3D                           jne 0x140979ef4
00979EB7  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979EBB  33 C0                           xor eax, eax
00979EBD  48 8B 0D D4 C4 4E 00            mov rcx, qword ptr [rip + 0x4ec4d4]
00979EC4  41 B9 01 00 00 00               mov r9d, 1
00979ECA  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00979ECE  48 8B D7                        mov rdx, rdi
00979ED1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00979ED5  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00979EDA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00979EDE  48 8D 05 33 93 6A FF            lea rax, [rip - 0x956ccd]
00979EE5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979EEA  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979EEF  E8 5C 3C 11 00                  call 0x140a8db50
00979EF4  41 0F BA E4 08                  bt r12d, 8
00979EF9  73 5B                           jae 0x140979f56
00979EFB  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979EFF  48 8D 44 24 7A                  lea rax, [rsp + 0x7a]
00979F04  48 8B 0D 8D C4 4E 00            mov rcx, qword ptr [rip + 0x4ec48d]
00979F0B  45 33 E4                        xor r12d, r12d
00979F0E  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979F13  48 8B D7                        mov rdx, rdi
00979F16  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
00979F1E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00979F23  48 8D 05 7E A3 69 FF            lea rax, [rip - 0x965c82]
00979F2A  C7 44 24 38 11 00 00 00         mov dword ptr [rsp + 0x38], 0x11
00979F32  45 8D 4C 24 01                  lea r9d, [r12 + 1]
00979F37  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979F3C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979F41  C6 44 24 7A FF                  mov byte ptr [rsp + 0x7a], 0xff
00979F46  E8 05 3C 11 00                  call 0x140a8db50
00979F4B  8B D8                           mov ebx, eax
00979F4D  85 C0                           test eax, eax
00979F4F  79 4B                           jns 0x140979f9c
00979F51  E9 1A DE FF FF                  jmp 0x140977d70
00979F56  8B 07                           mov eax, dword ptr [rdi]
00979F58  45 33 E4                        xor r12d, r12d
00979F5B  A8 01                           test al, 1
00979F5D  75 3D                           jne 0x140979f9c
00979F5F  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00979F63  48 8D 05 3E A3 69 FF            lea rax, [rip - 0x965cc2]
00979F6A  48 8B 0D 27 C4 4E 00            mov rcx, qword ptr [rip + 0x4ec427]
00979F71  45 8D 4C 24 01                  lea r9d, [r12 + 1]
00979F76  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00979F7B  48 8B D7                        mov rdx, rdi
00979F7E  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00979F83  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00979F88  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00979F8D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00979F92  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00979F97  E8 B4 3B 11 00                  call 0x140a8db50
00979F9C  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00979FA0  48 85 C9                        test rcx, rcx
00979FA3  74 0C                           je 0x140979fb1
00979FA5  66 44 39 65 48                  cmp word ptr [rbp + 0x48], r12w
00979FAA  74 05                           je 0x140979fb1
00979FAC  E8 4B BC FE FF                  call 0x140965bfc
00979FB1  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00979FB6  4D 85 F6                        test r14, r14
00979FB9  74 48                           je 0x14097a003
00979FBB  49 8B FE                        mov rdi, r14
00979FBE  66 45 39 26                     cmp word ptr [r14], r12w
00979FC2  74 3F                           je 0x14097a003
00979FC4  48 8B CF                        mov rcx, rdi
00979FC7  E8 30 BC FE FF                  call 0x140965bfc
00979FCC  44 38 25 0D 0A 49 00            cmp byte ptr [rip + 0x490a0d], r12b
00979FD3  75 12                           jne 0x140979fe7
00979FD5  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
00979FDB  A8 10                           test al, 0x10
00979FDD  74 08                           je 0x140979fe7
00979FDF  48 8B CF                        mov rcx, rdi
00979FE2  E8 E1 9B DB FF                  call 0x140733bc8
00979FE7  48 83 C8 FF                     or rax, 0xffffffffffffffff
00979FEB  48 FF C0                        inc rax
00979FEE  66 44 39 24 47                  cmp word ptr [rdi + rax*2], r12w
00979FF3  75 F6                           jne 0x140979feb
00979FF5  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00979FF9  48 83 C7 02                     add rdi, 2
00979FFD  66 44 39 27                     cmp word ptr [rdi], r12w
0097A001  75 C1                           jne 0x140979fc4
0097A003  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0097A007  48 85 C0                        test rax, rax
0097A00A  0F 84 65 DD FF FF               je 0x140977d75
0097A010  48 8B F8                        mov rdi, rax
0097A013  66 44 39 20                     cmp word ptr [rax], r12w
0097A017  0F 84 58 DD FF FF               je 0x140977d75
0097A01D  48 8B CF                        mov rcx, rdi
0097A020  E8 D7 BB FE FF                  call 0x140965bfc
0097A025  44 38 25 B4 09 49 00            cmp byte ptr [rip + 0x4909b4], r12b
0097A02C  75 12                           jne 0x14097a040
0097A02E  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
0097A034  A8 10                           test al, 0x10
0097A036  74 08                           je 0x14097a040
0097A038  48 8B CF                        mov rcx, rdi
0097A03B  E8 88 9B DB FF                  call 0x140733bc8
0097A040  48 83 C8 FF                     or rax, 0xffffffffffffffff
0097A044  48 FF C0                        inc rax
0097A047  66 44 39 24 47                  cmp word ptr [rdi + rax*2], r12w
0097A04C  75 F6                           jne 0x14097a044
0097A04E  48 8D 3C 47                     lea rdi, [rdi + rax*2]
0097A052  48 83 C7 02                     add rdi, 2
0097A056  66 44 39 27                     cmp word ptr [rdi], r12w
0097A05A  75 C1                           jne 0x14097a01d
0097A05C  E9 14 DD FF FF                  jmp 0x140977d75
0097A061  48 8B 8D 60 02 00 00            mov rcx, qword ptr [rbp + 0x260]
0097A068  48 33 CC                        xor rcx, rsp
0097A06B  E8 D0 25 D3 FF                  call 0x1406ac640
0097A070  48 81 C4 78 03 00 00            add rsp, 0x378
0097A077  41 5F                           pop r15
0097A079  41 5E                           pop r14
0097A07B  41 5D                           pop r13
0097A07D  41 5C                           pop r12
0097A07F  5F                              pop rdi
0097A080  5E                              pop rsi
0097A081  5B                              pop rbx
0097A082  5D                              pop rbp
0097A083  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgConfigureDevice(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1DC;
    unsigned int v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned int v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned int v_stack_m2A8;
    unsigned int v_stack_m2AC;
    unsigned int v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned int v_stack_m31C;
    unsigned int v_stack_m320;
    unsigned int v_stack_m324;
    unsigned int v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int8 v_stack_m33E;
    unsigned __int8 v_stack_m33F;
    unsigned __int8 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned int v_stack_m354;
    unsigned __int8 v_stack_m355;
    unsigned __int8 v_stack_m356;
    unsigned __int8 v_stack_m357;
    unsigned __int8 v_stack_m358;
    unsigned int v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned int v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int64 v_stack_m388;
    unsigned __int8 v_stack_m390;
    unsigned __int8 v_stack_m398;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (888);
    result = (*(unsigned __int64 *)(v_rip + 4795241)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m318 = a1;
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(0x400ULL));
    v_stack_m288 = a4;
    result = 0;
    v_stack_m290 = a5;
    a3 = 0;
    v_stack_m1DC = 0;
    v_stack_m2F0 = 0;
    *(unsigned int *)(a5) = 0;
    v_stack_m260 = 0;
    v_stack_m270 = 0;
    v_stack_m268 = 0;
    v_stack_m350 = 0;
    v_stack_m348 = 0;
    v_stack_m250 = 0;
    v_stack_m248 = 0;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    v_stack_m218 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = 0;
    v_stack_m1F0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m338 = 0;
    v_stack_m330 = 0;
    v_stack_m200 = 0;
    v_stack_m1F8 = 0;
    v_stack_m324 = 0;
    v_stack_m31C = 0;
    v_stack_m328 = 0;
    v_stack_m2A4 = 0;
    v_stack_m2A0 = 0;
    v_stack_m298 = 0;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    v_stack_m310 = 0;
    v_stack_m308 = 0;
    v_stack_m2E0 = 0;
    v_stack_m2D8 = 0;
    v_stack_m2D0 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m240 = 0;
    v_stack_m238 = 0;
    v_stack_m357 = 0;
    v_stack_m340 = 0;
    v_stack_m358 = 0;
    v_stack_m356 = 0;
    v_stack_m258 = 0;
    v_stack_m2B0 = 0;
    v_stack_m320 = 0;
    v_stack_m355 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m33F = 0;
    v_stack_m33E = 0;
    v_stack_m2AC = 0;
    v_stack_m2A8 = 0;
    v_stack_m300 = v_xmm0;
    v_stack_m354 = (unsigned int)((unsigned int)(0x400ULL));
    v_stack_m1C0 = v_xmm0;
    v_stack_m2E8 = 0;
    v_stack_m2C8 = 0;
    v_stack_m1E0 = 0x4100000ULL;
    result = ExAllocatePool2(256, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
    v_stack_m1D8 = result;
    if (result != 0) goto loc_00977ED3;
loc_00977D67:
loc_00977D6C:
loc_00977D70:
loc_00977D75:
    if (v_stack_m308 != 0) {
        result = ExFreePool(v_stack_m308, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
        v_stack_m310 = v_xmm0;
    }
    if (v_stack_m2D8 != 0) {
        result = ExFreePool(v_stack_m2D8, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
        v_stack_m2E0 = v_xmm0;
    }
    if (v_stack_m278 != 0) {
        result = ExFreePool(v_stack_m278, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
        v_stack_m280 = v_xmm0;
    }
    result = v_stack_m268;
    if (v_stack_m268 != 0) {
        a1 = v_stack_m268;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
    }
    if (v_stack_m348 != 0) {
        a1 = v_stack_m348;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
    }
    result = v_stack_m248;
    if (v_stack_m248 != 0) {
        a1 = v_stack_m248;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, (unsigned int)(0x63647050ULL), a4);
    }
    if (v_stack_m228 != 0) {
        a1 = v_stack_m228;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    if (v_stack_m218 != 0) {
        result = ExFreePool(v_stack_m218, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    if (v_stack_m208 != 0) {
        result = ExFreePool(v_stack_m208, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    result = v_stack_m1E8;
    if (v_stack_m1E8 != 0) {
        a1 = v_stack_m1E8;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    if (v_stack_m330 != 0) {
        a1 = v_stack_m330;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    if (v_stack_m1F8 != 0) {
        result = ExFreePool(v_stack_m1F8, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    result = v_stack_m2E8;
    if (v_stack_m2E8 != 0) {
        a1 = v_stack_m2E8;
        result = ExFreePool(a1, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
    }
    if (v_stack_m238 != 0) {
        result = ExFreePool(v_stack_m238, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
        v_stack_m240 = v_xmm0;
    }
    if (v_stack_m2B8 != 0) {
        result = ExFreePool(v_stack_m2B8, (unsigned int)(0x400ULL) + 16, v_stack_m228, a4);
        v_stack_m2C0 = v_xmm0;
    }
    result = v_stack_m1D8;
    if (v_stack_m1D8 != 0) {
        a2 = 0;
        a1 = v_stack_m1D8;
        result = ExFreePoolWithTag(a1, a2, v_stack_m228, a4);
    }
    if (v_stack_m258 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m258, a2, v_stack_m228, a4);
    }
    if (v_stack_m2F0 != 0) {
        result = ZwClose(v_stack_m2F0, a2, v_stack_m228, a4);
    }
    if (v_stack_m260 != 0) {
        result = ZwClose(v_stack_m260, a2, v_stack_m228, a4);
    }
    goto loc_0097A061;
loc_00977ED3:
    if (0 == 0) goto loc_009785C3;
    result = PiDevCfgQueryDriverConfiguration(0, a2, v_stack_m228, a4);
    if (sign_flag) goto loc_00977D6C;
    v_stack_m298 = *(unsigned __int64 *)(a3 + 264);
    if ((*(unsigned __int64 *)(a3 + 296)) == 0) goto loc_00977F1A;
    result = PnpDuplicateUnicodeString(v_stack_m270, a3 + 288, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977F1A:
    if ((*(unsigned __int64 *)(a3 + 312)) == 0) goto loc_00977F3C;
    result = PnpDuplicateUnicodeString(v_stack_m350, a3 + 304, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977F3C:
    if ((*(unsigned __int64 *)(a3 + 328)) == 0) goto loc_00977F5D;
    result = PnpDuplicateUnicodeString(v_stack_m250, a3 + 320, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977F5D:
    if ((*(unsigned __int64 *)(a3 + 344)) == 0) goto loc_00977F81;
    result = PnpDuplicateUnicodeString(v_stack_m230, a3 + 336, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977F81:
    if ((*(unsigned __int64 *)(a3 + 360)) == 0) goto loc_00977FA5;
    result = PnpDuplicateUnicodeString(v_stack_m220, a3 + 352, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977FA5:
    if ((*(unsigned __int64 *)(a3 + 376)) == 0) goto loc_00977FC9;
    result = PnpDuplicateUnicodeString(v_stack_m210, a3 + 368, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977FC9:
    if ((*(unsigned __int64 *)(a3 + 408)) == 0) goto loc_00977FED;
    result = PnpDuplicateUnicodeString(v_stack_m200, a3 + 400, v_stack_m228, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00977D67;
loc_00977FED:
    v_stack_m324 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 420)));
    v_stack_m354 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 416)));
    v_stack_m31C = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 184)));
    if ((*(unsigned __int64 *)(a3 + 208)) == (a3 + 208)) goto loc_00978228;
loc_0097801E:
    result = PiDevCfgQueryDriverConfiguration(*(unsigned __int64 *)(a3 + 208), (unsigned int)(*(unsigned int *)(a3 + 184)), v_stack_m228, a4);
    a1 = 0;
    if (!sign_flag) goto loc_00978064;
    if (((unsigned int)(result)) != 0xC0000493ULL) goto loc_00977D6C;
    if ((*(unsigned __int8 *)(v_rip + 4794785)) == 0) goto loc_00977D6C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6684645)))) & (2)) == 0) goto loc_00977D6C;
    v_stack_m354 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 416)));
    goto loc_009781FB;
loc_00978064:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 296)) == 0) goto loc_0097807C;
    goto loc_009781FB;
loc_0097807C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 312)) == 0) goto loc_009780A9;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m350, a2, *(unsigned __int64 *)(a3 + 208) + 304, a4);
    a1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_009780A9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 328)) == 0) goto loc_009780D5;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m250, a2, *(unsigned __int64 *)(a3 + 208) + 320, a4);
    a1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_009780D5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 344)) == 0) goto loc_00978104;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m230, a2, *(unsigned __int64 *)(a3 + 208) + 336, a4);
    a1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_00978104:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 360)) == 0) goto loc_00978133;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m220, a2, *(unsigned __int64 *)(a3 + 208) + 352, a4);
    a1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_00978133:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 376)) == 0) goto loc_00978160;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m210, a2, *(unsigned __int64 *)(a3 + 208) + 368, a4);
    if (sign_flag) goto loc_00977D6C;
loc_00978160:
    result = (unsigned int)(((unsigned int)(v_stack_m324)) | (*(unsigned int *)(*(unsigned __int64 *)(a3 + 208) + 420)));
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 416))) | (*(unsigned int *)(*(unsigned __int64 *)(a3 + 208) + 416)));
    a4 = 0;
    v_stack_m324 = (unsigned int)(result);
    a3 = 0;
    result = (unsigned int)(((unsigned int)(v_stack_m31C)) | (*(unsigned int *)(*(unsigned __int64 *)(a3 + 208) + 184)));
    v_stack_m31C = (unsigned int)(result);
    v_stack_m354 = (unsigned int)(v_r13);
    result = PiDevCfgAppendMultiSz(v_stack_m1F0, *(unsigned __int64 *)(a3 + 208) + 40, a3, a4);
    if (sign_flag) goto loc_00977D6C;
    a4 = 0;
    a3 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m338, *(unsigned __int64 *)(a3 + 208) + 424, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00977D6C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 408)) == 0) goto loc_009781FB;
    a4 = 0;
    a3 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m200, *(unsigned __int64 *)(a3 + 208) + 400, a3, a4);
    if (sign_flag) goto loc_00977D6C;
loc_009781FB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208))) != (a3 + 208)) goto loc_0097801E;
    v_r12 = 0;
    v_stack_m324 = (unsigned int)((unsigned int)(v_stack_m324));
    v_stack_m31C = (unsigned int)((unsigned int)(v_stack_m31C));
    if (sign_flag) goto loc_00977D6C;
    goto loc_0097822B;
loc_00978228:
    v_r12 = 0;
loc_0097822B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6684159)))) & (2)) == 0) goto loc_00978288;
    if (condition_is_above_or_equal) goto loc_00978270;
    a1 = (((*(unsigned __int8 *)(a3 + 440)) & (2)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_rip + 6684263)) & (1)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00978270;
    if ((*(unsigned __int8 *)(v_rip + 6602477)) != 0) goto loc_00978270;
    if ((*(unsigned __int8 *)(v_rip + 4794236)) != 0) goto loc_00978270;
loc_00978266:
    goto loc_00977D6C;
loc_00978270:
    if ((((unsigned __int8)((unsigned int)(v_stack_m31C))) & (64)) == 0) goto loc_00978288;
    if ((*(unsigned __int8 *)(v_rip + 4794212)) == 0) goto loc_00978266;
    v_stack_m354 = (unsigned int)(v_r13);
loc_00978288:
    a2 = 0;
    result = memset(v_stack_m108, a2, 168, a4);
    v_stack_m390 = 1;
    v_stack_m100 = 288;
    v_stack_mE8 = (unsigned int)((unsigned int)(0x1000000ULL));
    v_stack_mF8 = v_rip + 1601304;
    v_stack_mB0 = (unsigned int)((unsigned int)(0x1000000ULL));
    a4 = 0;
    v_stack_mF0 = v_stack_m310;
    v_stack_mC0 = v_rip + 1601045;
    v_stack_mC8 = 288;
    v_stack_mB8 = v_stack_m2E0;
    result = RtlpQueryRegistryValues((unsigned int)(0xC0000000ULL), *(unsigned __int64 *)(a3 + 24), v_stack_m108, a4);
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m308 != 0) goto loc_00978365;
    if (v_stack_m2D8 != 0) goto loc_00978365;
    if ((*(unsigned __int64 *)(a3 + 168)) == 0) goto loc_00978365;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6683902)))) & (2)) == 0) goto loc_00978365;
    if ((*(unsigned __int8 *)(v_rip + 6602251)) != 0) goto loc_00978365;
    if ((*(unsigned __int8 *)(v_rip + 4794010)) != 0) goto loc_0097835B;
    goto loc_00977D9F;
loc_0097835B:
    v_stack_m354 = (unsigned int)(v_stack_m330);
loc_00978365:
    if (v_stack_m310 != 0) goto loc_0097837B;
    result = (unsigned int)(*(unsigned int *)(v_rip + 6683902));
    if (v_stack_m308 != 0) {
        a1 = v_stack_m310;
        result = RtlFreeAnsiString(a1, *(unsigned __int64 *)(a3 + 24), v_stack_m108, a4);
    }
    if (v_stack_m2E0 != 0) goto loc_00978391;
    if (v_stack_m2D8 != 0) {
        a1 = v_stack_m2E0;
        result = RtlFreeAnsiString(a1, *(unsigned __int64 *)(a3 + 24), v_stack_m108, a4);
    }
    if (v_stack_m298 == 0) goto loc_00978553;
    v_stack_m390 = v_stack_m2F0;
    v_stack_m398 = 0;
    result = PnpOpenObjectRegKey(*(unsigned __int64 *)(v_rip + 5169139), v_stack_m298, 2, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00978553;
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 160, (unsigned int)(0x20019ULL));
    v_stack_m1A8 = v_rip - 9846750;
    v_stack_m1A0 = 17;
    v_stack_m198 = v_stack_m357;
    v_stack_m178 = 17;
    v_stack_m180 = v_rip - 9788030;
    v_stack_m390 = 4;
    v_stack_m170 = v_stack_m358;
    v_stack_m190 = 1;
    v_stack_m158 = v_rip - 9766758;
    v_stack_m148 = v_stack_m280;
    v_stack_m130 = v_rip - 9788265;
    v_stack_m120 = v_stack_m258;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m168 = 1;
    v_stack_m150 = 18;
    v_stack_m13C = 6;
    v_stack_m128 = 0x1003ULL;
    v_stack_m114 = 2;
    result = PiDevCfgQueryObjectProperties(2, v_stack_m298, 2, v_stack_m2F0);
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m188 < 0) {
        v_stack_m357 = 0;
    }
    if (v_stack_m160 < 0) {
        v_stack_m358 = 0;
    }
    if (v_stack_m138 < 0) {
        a2 = 0;
        a1 = v_stack_m280;
        result = RtlInitUnicodeString(a1, a2, 2, v_stack_m2F0);
    }
    if (v_stack_m110 >= 0) goto loc_00978503;
    v_stack_m258 = 0;
    goto loc_0097850C;
loc_00978503:
    v_stack_m2B0 = (unsigned int)((unsigned int)(v_stack_m118));
loc_0097850C:
    if (v_stack_m357 != 0) goto loc_00978589;
    v_stack_m388 = v_stack_m340;
    v_stack_m390 = *(unsigned __int64 *)(a3 + 16);
    v_stack_m398 = *(unsigned __int64 *)(a3 + 64);
    result = PiDevCfgGetDeviceClassDriverConfigurable(v_stack_m298, v_stack_m2F0, *(unsigned __int64 *)(v_stack_m348 + 8), *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00978553;
    if (v_stack_m340 != 0) {
        v_stack_m357 = 255;
    }
    if (v_stack_m357 != 0) goto loc_00978589;
    a1 = (((*(unsigned __int8 *)(v_rip + 6683475)) & (1)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_rip + 6683333)) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00978589;
    if ((*(unsigned __int8 *)(v_rip + 4793447)) == 0) goto loc_00978266;
    v_stack_m354 = (unsigned int)(v_stack_m330);
loc_00978589:
    if (v_stack_m258 == 0) goto loc_009785BE;
    if ((unsigned int)((unsigned int)(v_stack_m2B0)) == 0) goto loc_009785B4;
loc_009785A1:
    if ((*(unsigned __int8 *)(v_stack_m258)) == ((unsigned __int8)(*(unsigned __int8 *)(a3 + 110)))) goto loc_009785AF;
    result = (unsigned int)((0) + 1);
    a1 = (v_stack_m258) + 1;
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(v_stack_m2B0)))) goto loc_009785A1;
loc_009785AF:
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(v_stack_m2B0)))) goto loc_009785BE;
loc_009785B4:
    goto loc_00977D6C;
loc_009785BE:
loc_009785C3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) != 0) goto loc_009786D2;
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 160, *(unsigned __int64 *)(a2 + 16));
    v_stack_m198 = v_stack_m1C0;
    v_stack_m390 = 3;
    v_stack_m180 = v_rip - 9788484;
    v_stack_m1A8 = v_rip - 9858884;
    v_stack_m170 = v_stack_m320;
    v_stack_m158 = v_rip - 9852586;
    v_stack_m148 = v_stack_m2C0;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m1A0 = 13;
    v_stack_m190 = 16;
    v_stack_m178 = 7;
    v_stack_m168 = 4;
    v_stack_m150 = 18;
    v_stack_m13C = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1A8, *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    a2 = 0;
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m188 >= 0) goto loc_009786B1;
    v_stack_m1C0 = v_xmm0;
    goto loc_009786B6;
loc_009786B1:
    v_stack_m355 = 1;
loc_009786B6:
    if (v_stack_m160 < 0) {
        v_stack_m320 = 0;
    }
    if (v_stack_m138 >= 0) goto loc_009786D4;
    result = RtlInitUnicodeString(v_stack_m2C0, a2, 1, *(unsigned __int64 *)(a2 + 16));
loc_009786D2:
    a2 = 0;
loc_009786D4:
    if (v_stack_m358 != 0) goto loc_009787BD;
    if (((v_stack_m320) & (4)) == 0) goto loc_009787A1;
    if (0 == 0) goto loc_00978796;
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 160, *(unsigned __int64 *)(a2 + 16));
    v_stack_m198 = v_stack_m240;
    v_stack_m390 = 1;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m1A8 = v_rip - 9852731;
    v_stack_m1A0 = 18;
    v_stack_m18C = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1A8, *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    a2 = 0;
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m188 < 0) {
        a1 = v_stack_m240;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(a2 + 16));
        a2 = 0;
    }
    if (v_stack_m238 == 0) goto loc_0097879B;
    result = RtlEqualUnicodeString(v_stack_m240, a3 + 40, 1, *(unsigned __int64 *)(a2 + 16));
    a2 = 0;
    if ((unsigned __int8)(result) != 0) {
        v_stack_m358 = 255;
    }
    if (v_stack_m358 != 0) goto loc_009787BD;
loc_009787A1:
    result = PiDevCfgEnforceDevicePolicy(v_stack_m318, 0, v_stack_m298, *(unsigned __int64 *)(a2 + 16));
    a2 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_009787BD:
    if (v_stack_m2F0 == 0) goto loc_0097881B;
    v_stack_m300 = 0x1C001AULL;
    v_stack_m2F8 = v_rip + 1597571;
    result = IopOpenRegistryKeyEx(v_stack_m260, v_stack_m2F0, v_stack_m300, (unsigned int)(0x20019ULL));
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00978819;
    if (sign_flag) goto loc_00977D6C;
    result = PiDevCfgVerifyDeviceAllowed(v_stack_m318, v_stack_m260, v_stack_m300, (unsigned int)(0x20019ULL));
    a2 = 0;
    if (!sign_flag) goto loc_0097881B;
    goto loc_00977D6C;
loc_00978819:
    a2 = 0;
loc_0097881B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m318 + 32) + 8) + 16)))) & (4)) == 0) goto loc_00978896;
    v_stack_m368 = 0;
    v_stack_m370 = v_stack_m2A8;
    v_stack_m378 = 1;
    v_stack_m380 = v_stack_m356;
    v_stack_m388 = v_stack_m2AC;
    v_stack_m390 = v_rip - 9847877;
    v_stack_m398 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5167971), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    a2 = 0;
    if (sign_flag) goto loc_00978892;
    if (v_stack_m2AC != 17) goto loc_00978892;
    if (v_stack_m2A8 != 1) {
        v_stack_m356 = 0;
    }
    if (0 == 0) goto loc_009788C4;
    if (v_stack_m268 != 0) goto loc_009788C4;
    if (v_stack_m278 != 0) goto loc_009788C4;
    if (v_stack_m356 != 0) goto loc_009788C4;
    if (((*(unsigned int *)(v_stack_m318 + 560)) & (256)) != 0) goto loc_009788C4;
    goto loc_00977D6C;
loc_009788C4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) != 0) goto loc_00978986;
    if (0 != 0) goto loc_00978926;
    if (v_stack_m355 == 0) goto loc_009788E5;
    result = (unsigned int)(*(unsigned int *)(a2));
    if (((*(unsigned int *)((unsigned int)(0xC0000494ULL) + 560)) & (256)) == 0) {
        a2 = *(unsigned __int64 *)(v_stack_m348 + 8);
        a4 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 5167781);
        a3 = a4 + 17;
        result = _CmDeleteDeviceRegKey(a1, a2, a3, a4);
    }
    a4 = 0;
    result = _CmDeleteDeviceRegKey(*(unsigned __int64 *)(v_rip + 5167758), *(unsigned __int64 *)(v_stack_m348 + 8), a4 + 18, a4);
    a2 = 0;
loc_00978915:
    if (a3 == 0) goto loc_0097898D;
loc_0097891D:
    goto loc_00978990;
loc_00978926:
    result = PnpIsNullGuid(v_stack_m1C0, a2, a3 + 256, 0);
    if ((unsigned __int8)(result) != 0) goto loc_00978980;
    result = PnpIsNullGuid(a3 + 240, a2, a3 + 256, 0);
    if ((unsigned __int8)(result) != 0) goto loc_0097897C;
    a1 = (v_stack_m1C0) - (*(unsigned __int64 *)(a3 + 240));
    if (!(condition_is_not_equal)) {
        a1 = v_stack_m1B8;
        a1 = (a1) - (*(unsigned __int64 *)(a3 + 240 + 8));
    }
    if (a1 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m348 + 8);
        a4 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 5167653);
        a3 = a4 + 18;
        result = _CmDeleteDeviceRegKey(a1, a2, a3, a4);
    }
loc_00978980:
    goto loc_0097891D;
loc_00978986:
    if (a3 != 0) goto loc_00978980;
    goto loc_00978915;
loc_0097898D:
loc_00978990:
    v_stack_m390 = v_stack_m2A0;
    v_stack_m398 = v_stack_m2A4;
    result = PiDevCfgMigrateDevice(v_stack_m318, a2, a2, a3 + 40);
    a2 = 0;
    v_r13 = v_stack_m330;
    if (!(sign_flag)) {
        v_r13 = (unsigned int)((v_stack_m330) | (v_stack_m2A4));
        result = v_stack_m2A0;
        v_stack_m354 = (unsigned int)(v_r13);
        v_stack_m328 = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) != 0) goto loc_00978A2C;
    result = (unsigned __int8)(-(v_stack_m355));
    a1 = (v_stack_m318) & (v_stack_m1C0);
    if (a3 == 0) {
        a3 = 0;
    }
    v_stack_m398 = a1;
    result = PiDevCfgResetDeviceDriverSettings(v_stack_m318, 0, a3, v_stack_m2F0);
    result = PnpCtxRegDeleteTree(*(unsigned __int64 *)(v_rip + 5167507), *(unsigned __int64 *)(a2 + 16), v_rip + 1592628, v_stack_m2F0);
    result = PnpCtxRegDeleteTree(*(unsigned __int64 *)(v_rip + 5167485), *(unsigned __int64 *)(a2 + 16), v_rip + 1597006, v_stack_m2F0);
    a2 = 0;
loc_00978A2C:
    if (a3 == 0) goto loc_00978A92;
    result = PnpIsNullGuid(a3 + 240, a2, v_rip + 1597006, v_stack_m2F0);
    a2 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00978A92;
    v_stack_m368 = 0;
    v_stack_m370 = 16;
    v_stack_m378 = a3 + 240;
    v_stack_m380 = 13;
    v_stack_m388 = v_rip - 9860041;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5167424), 0, *(unsigned __int64 *)(v_stack_m348 + 8), a2 + 1);
    if (!sign_flag) goto loc_00978AD3;
    goto loc_00977D6C;
loc_00978A92:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9860123;
        a1 = *(unsigned __int64 *)(v_rip + 5167342);
        a4 = 1;
        v_stack_m368 = 0;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        a2 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    v_rbx = 0;
    if (v_stack_m268 == 0) goto loc_00978AFD;
    if ((unsigned __int16)(v_stack_m270) == 0) goto loc_00978B5B;
    v_stack_m368 = 0;
    result = (unsigned int)((v_stack_m270) + (2));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = v_stack_m268;
    goto loc_00978B1B;
loc_00978AFD:
    if (v_stack_m278 == 0) goto loc_00978B5B;
    if ((unsigned __int16)(v_stack_m280) == 0) goto loc_00978B5B;
    v_stack_m368 = 0;
    result = (unsigned int)((v_stack_m280) + (2));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = v_stack_m278;
loc_00978B1B:
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9807318;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5167211), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (sign_flag) goto loc_00977D6C;
    v_rbx = 0;
    goto loc_00978BAC;
loc_00978B5B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) != 0) goto loc_00978BAC;
    if (a2 == 0) goto loc_00978B6B;
    if (*(unsigned __int64 *)(v_rip + 5167211) != 0) goto loc_00978B71;
loc_00978B6B:
    result = (unsigned int)(*(unsigned int *)(a2));
    if (v_stack_m356 == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9807404;
        a1 = *(unsigned __int64 *)(v_rip + 5167125);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m348 == 0) goto loc_00978C03;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m350);
    v_stack_m378 = v_stack_m348;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9849713;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5167054), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    v_r12 = 0;
    if (!sign_flag) goto loc_00978C49;
    goto loc_00977D6C;
loc_00978C03:
    v_r12 = 0;
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9849775;
        a1 = *(unsigned __int64 *)(v_rip + 5166970);
        a4 = v_r12 + 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m248 == 0) goto loc_00978CA1;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m250);
    v_stack_m378 = v_stack_m248;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9849747;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5166873), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_00978CE5;
    goto loc_00977D6C;
loc_00978CA1:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9849810;
        a1 = *(unsigned __int64 *)(v_rip + 5166815);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m228 == 0) goto loc_00978D4B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(v_stack_m230);
    v_stack_m380 = v_stack_m228;
    v_stack_m388 = 0x2012ULL;
    v_stack_m390 = v_rip - 9854586;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5166715), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    goto loc_00978D8D;
loc_00978D4B:
    if ((((unsigned __int8)(result)) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9854658;
        a1 = *(unsigned __int64 *)(v_rip + 5166647);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (a3 == 0) goto loc_00978F91;
    if (v_stack_m308 == 0) goto loc_00978F91;
    result = PiDevCfgBuildIndirectString(a3, v_stack_m310, v_stack_m2D0, v_stack_m1D0);
    if (sign_flag) goto loc_00978F84;
    v_stack_m2E8 = v_stack_m2C8;
    a1 = (condition_is_below) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_rip + 6681308)) & (1)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00978E37;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a1 = (unsigned int)((v_stack_m2D0) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a1);
    v_stack_m380 = v_stack_m2C8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9850072;
    result = 0;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5166477), *(unsigned __int64 *)(v_stack_m348 + 8), result + 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
loc_00978E37:
    v_rbx = 0;
    if (v_stack_m1C8 == 0) goto loc_00978EA0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a1 = (unsigned int)((v_stack_m1D0) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a1);
    v_stack_m380 = v_stack_m1C8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9854593;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5166372), *(unsigned __int64 *)(v_stack_m348 + 8), v_rbx + 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    goto loc_00978EDF;
loc_00978EA0:
    if ((((unsigned __int8)(result)) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9854663;
        a1 = *(unsigned __int64 *)(v_rip + 5166306);
        a4 = 1;
        v_stack_m368 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a2 = a2;
        v_stack_m370 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m378 = (unsigned int)((unsigned int)(result));
        v_stack_m380 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m2C8 != 0) {
        a1 = v_stack_m2C8;
        result = ExFreePool(a1, a2, a3, a4);
        v_stack_m2D0 = v_xmm0;
        v_stack_m2E8 = v_xmm0;
    }
    v_r12 = 0;
loc_00978F00:
    if (v_stack_m2D8 == 0) goto loc_009790B7;
    a4 = 0;
    result = PiDevCfgBuildIndirectString(a3, v_stack_m2E0, v_stack_m2D0, a4);
    if (sign_flag) goto loc_00978F84;
    result = (unsigned int)((v_stack_m2D0) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = v_stack_m2C8;
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9768506;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    v_stack_m2E8 = v_stack_m2C8;
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5166173), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    v_r12 = 0;
    if (!sign_flag) goto loc_009790FB;
    goto loc_00977D6C;
loc_00978F84:
    v_stack_m2E8 = v_stack_m2C8;
    goto loc_00977D6C;
loc_00978F91:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) != 0) goto loc_009791B4;
    v_stack_m368 = 0;
    v_stack_m370 = 0;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m388 = v_rip - 9854910;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5166059), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (a3 != 0) goto loc_00978F00;
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 160, 1);
    v_stack_m1A8 = v_rip - 9769857;
    v_stack_m390 = (unsigned int)(a3 + 1);
    v_stack_m198 = v_stack_m310;
    v_stack_m1A0 = 18;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m18C = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1A8, *(unsigned __int64 *)(v_stack_m348 + 8), (unsigned int)((unsigned int)(a3 + 1)), *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00979174;
    if (v_stack_m188 < 0) goto loc_00979174;
    if (v_stack_m308 == 0) goto loc_00979174;
    result = (unsigned int)((v_stack_m310) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = v_stack_m308;
    v_stack_m380 = (unsigned int)((unsigned int)(v_stack_m1A0));
    v_stack_m388 = v_rip - 9850742;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165829), 0, *(unsigned __int64 *)(v_stack_m348 + 8), (unsigned int)((unsigned int)(a3 + 1)));
    if (sign_flag) goto loc_00977D6C;
loc_009790B7:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9768880;
        a1 = *(unsigned __int64 *)(v_rip + 5165769);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = 0;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (a3 == 0) goto loc_009791C2;
    if (*(unsigned __int64 *)(a3 + 280) == 0) goto loc_009791C2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a1 = (unsigned int)((*(unsigned __int16 *)(a3 + 272)) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a1);
    v_stack_m380 = *(unsigned __int64 *)(a3 + 280);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9855336;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165653), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (!sign_flag) goto loc_0097920F;
    goto loc_00977D6C;
loc_00979174:
    v_stack_m368 = 0;
    v_stack_m370 = 0;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m388 = v_rip - 9850967;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165586), a2, *(unsigned __int64 *)(v_stack_m348 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_009790B7;
loc_009791B4:
    if (a3 != 0) goto loc_00978F00;
    goto loc_009790B7;
loc_009791C2:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9855491;
        a1 = *(unsigned __int64 *)(v_rip + 5165502);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (a3 == 0) goto loc_00979486;
loc_0097920F:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a1 = (unsigned int)((a1) << (17));
    v_stack_m370 = (unsigned int)(a1);
    v_stack_m378 = 8;
    v_stack_m380 = a3 + 112;
    v_stack_m388 = 16;
    v_stack_m390 = v_rip - 9855727;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165413), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    v_stack_m390 = (unsigned int)(*(unsigned __int16 *)(a3 + 120));
    result = ((unsigned int)(*(unsigned int *)(a3 + 124))) >> (16);
    v_stack_m398 = (unsigned int)(*(unsigned __int16 *)(a3 + 122));
    result = RtlUnicodeStringPrintf(v_stack_m1E0, v_rip + 1594910, (unsigned __int16)(result), *(unsigned __int16 *)(a3 + 124));
    if (sign_flag) goto loc_00977D6C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a1 = (unsigned int)((v_stack_m1E0) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a1);
    v_stack_m380 = v_stack_m1D8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9855790;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165246), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a2 = (unsigned int)((*(unsigned __int16 *)(a3 + 40)) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a2);
    v_stack_m380 = *(unsigned __int64 *)(a3 + 48);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9855886;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165142), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a2 = (unsigned int)((*(unsigned __int16 *)(a3 + 88)) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a2);
    v_stack_m380 = *(unsigned __int64 *)(a3 + 96);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9856026;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5165050), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    result = PiDevCfgBuildDriverNodeStrongName(a3, v_stack_m2E0, v_stack_m310, v_stack_m300);
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m2B8 == 0) goto loc_00979410;
    a4 = (v_stack_m300) >> (1);
    a2 = (v_stack_m2C0) >> (1);
    v_stack_m398 = 1;
    result = RtlCompareUnicodeStrings(v_stack_m2B8, a2, v_stack_m2F8, a4);
    if ((unsigned int)(result) == 0) {
        a1 = v_stack_m2C0;
        result = RtlFreeAnsiString(a1, a2, v_stack_m2F8, a4);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a1 = (unsigned int)((v_stack_m300) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a1);
    v_stack_m380 = v_stack_m2F8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9856195;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5164889), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (v_stack_m2F8 != 0) {
        result = ExFreePool(v_stack_m2F8, *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
        v_stack_m300 = v_xmm0;
    }
    if (sign_flag) goto loc_00977D6C;
    goto loc_009795C6;
loc_00979486:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9856323;
        a1 = *(unsigned __int64 *)(v_rip + 5164790);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9856289;
        a1 = *(unsigned __int64 *)(v_rip + 5164728);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9856375;
        a1 = *(unsigned __int64 *)(v_rip + 5164666);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9856485;
        a1 = *(unsigned __int64 *)(v_rip + 5164604);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9856523;
        a1 = *(unsigned __int64 *)(v_rip + 5164542);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m2B8 == 0) goto loc_00979637;
    if (((v_stack_m320) & (8)) != 0) goto loc_00979637;
    if (((*(unsigned int *)(v_stack_m318 + 396)) & (0x6000ULL)) != 0) goto loc_00979637;
    result = (unsigned int)((v_stack_m2C0) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = v_stack_m2B8;
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9791265;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5164419), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_0097967B;
    goto loc_00977D6C;
loc_00979637:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9791328;
        a1 = *(unsigned __int64 *)(v_rip + 5164361);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m218 == 0) goto loc_009796D9;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m220);
    v_stack_m378 = v_stack_m218;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9797803;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5164257), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_0097971D;
    goto loc_00977D6C;
loc_009796D9:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9797866;
        a1 = *(unsigned __int64 *)(v_rip + 5164199);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m208 == 0) goto loc_0097977B;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m210);
    v_stack_m378 = v_stack_m208;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9794357;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5164095), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_009797BF;
    goto loc_00977D6C;
loc_0097977B:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9794420;
        a1 = *(unsigned __int64 *)(v_rip + 5164037);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m1F8 == 0) goto loc_0097981D;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m200);
    v_stack_m378 = v_stack_m1F8;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9791439;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5163933), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_00979861;
    goto loc_00977D6C;
loc_0097981D:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9791502;
        a1 = *(unsigned __int64 *)(v_rip + 5163875);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m1E8 == 0) goto loc_009798BF;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m1F0);
    v_stack_m378 = v_stack_m1E8;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9797281;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5163771), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_00979903;
    goto loc_00977D6C;
loc_009798BF:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9797344;
        a1 = *(unsigned __int64 *)(v_rip + 5163713);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (a3 == 0) goto loc_009799D6;
    if ((*(unsigned int *)(a3 + 108)) == -1) goto loc_009799D3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    a2 = (unsigned int)((*(unsigned __int16 *)(a3 + 72)) + (2));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = (unsigned int)(a2);
    v_stack_m380 = *(unsigned __int64 *)(a3 + 80);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9857316;
    result = 0;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5163592), *(unsigned __int64 *)(v_stack_m348 + 8), result + 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = 4;
    v_stack_m380 = a3 + 108;
    v_r12 = 0;
    v_stack_m388 = 7;
    v_stack_m390 = v_rip - 9857432;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5163534), *(unsigned __int64 *)(v_stack_m348 + 8), v_r12 + 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D6C;
    goto loc_00979A58;
loc_009799D3:
    v_r12 = 0;
loc_009799D6:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9857487;
        a1 = *(unsigned __int64 *)(v_rip + 5163434);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9857573;
        a1 = *(unsigned __int64 *)(v_rip + 5163372);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m320 != 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9793705;
        a1 = *(unsigned __int64 *)(v_rip + 5163304);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (a3 == 0) goto loc_00979B9A;
    *(unsigned int *)(v_stack_m288) = (unsigned int)(v_r13);
    a1 = (((*(unsigned __int8 *)(a3 + 184)) & (8)) != 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_rip + 6677874)) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        *(unsigned int *)(v_stack_m288) = (unsigned int)(v_r13);
    }
    v_stack_m398 = v_stack_m328;
    result = PiDevCfgConfigureDeviceDriver(v_stack_m318, a2, a3, v_stack_m354);
    if (sign_flag) goto loc_00977D6C;
    goto loc_00979B5D;
loc_00979B13:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 208) + 184)))) & (1)) == 0) goto loc_00979B59;
    v_stack_m398 = v_stack_m328;
    result = PiDevCfgConfigureDeviceDriver(v_stack_m318, a2, *(unsigned __int64 *)(a3 + 208), v_stack_m354);
    if (sign_flag) goto loc_00977D6C;
loc_00979B59:
loc_00979B5D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208))) != (a3 + 208)) goto loc_00979B13;
    result = PiDevCfgConfigureDeviceLocation(v_stack_m318, a2, v_stack_m354, v_stack_m328);
    if (sign_flag) goto loc_00977D6C;
    goto loc_00979BCD;
loc_00979B9A:
    if (((*(unsigned int *)(v_stack_m318 + 560)) & (256)) == 0) goto loc_00979BB9;
    *(unsigned int *)(v_stack_m288) = (unsigned int)(v_stack_m290);
    goto loc_00979BD1;
loc_00979BB9:
    *(unsigned int *)(v_stack_m288) = 64;
    result = PnpDeleteDeviceInterfaces(v_stack_m348, a2, v_stack_m354, v_stack_m328);
loc_00979BCD:
loc_00979BD1:
    a4 = 0;
    if (v_stack_m324 == 0) goto loc_00979BF4;
    if ((*(unsigned __int8 *)(v_rip + 6595943)) != 0) goto loc_00979BF4;
    result = PipIsDevNodeDNStarted(v_stack_m318, a2, v_stack_m354, a4);
    if ((unsigned int)(result) != 0) {
    }
    if (((v_stack_m320) & (2)) != 0) {
    }
    if (v_stack_m355 != 0) {
    }
    if (v_stack_m260 == 0) goto loc_00979C4F;
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    v_stack_m390 = v_stack_m328;
    v_stack_m398 = v_stack_m354;
    result = PiDevCfgConfigureDeviceKeys(v_stack_m318, a2, v_stack_m260, a4);
    if (sign_flag) goto loc_00977D6C;
loc_00979C4F:
    v_r12 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m290)))) & (2)) != 0) goto loc_00979C92;
    if (v_stack_m357 != 255) goto loc_00979C92;
    if (v_stack_m298 == 0) goto loc_00979C92;
    if (v_stack_m2F0 == 0) goto loc_00979C92;
    result = PiDevCfgGetDeviceClassConfigFlags(v_stack_m298, v_stack_m2F0, v_stack_m354, a4);
    if (sign_flag) goto loc_00977D6C;
loc_00979C92:
    if (a3 == 0) goto loc_00979CA0;
    goto loc_00979CA7;
loc_00979CA0:
loc_00979CA7:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    result = (unsigned int)((result) << (17));
    v_stack_m370 = (unsigned int)(result);
    v_stack_m300 = v_xmm0;
    a2 = (unsigned int)((v_stack_m300) + (2));
    v_stack_m378 = (unsigned int)(a2);
    v_stack_m380 = v_stack_m2F8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9858615;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5162725), *(unsigned __int64 *)(v_stack_m348 + 8), 1, *(unsigned __int64 *)(a2 + 16));
    if (sign_flag) goto loc_00977D70;
    if (v_stack_m330 == 0) goto loc_00979D60;
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(v_stack_m338);
    v_stack_m378 = v_stack_m330;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9772593;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5162607), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_00979DA4;
    goto loc_00977D70;
loc_00979D60:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9772649;
        a1 = *(unsigned __int64 *)(v_rip + 5162528);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (a3 == 0) goto loc_00979E0A;
    if (*(unsigned __int64 *)(a3 + 136) == 0) goto loc_00979E0A;
    result = (unsigned int)((*(unsigned __int16 *)(a3 + 128)) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (unsigned int)(result);
    v_stack_m378 = *(unsigned __int64 *)(a3 + 136);
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9795092;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5162416), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_00979E4E;
    goto loc_00977D70;
loc_00979E0A:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9795155;
        a1 = *(unsigned __int64 *)(v_rip + 5162358);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (!sign_flag) goto loc_00979EB1;
    result = 0;
    v_stack_m368 = 0;
    v_stack_m370 = 1;
    v_stack_m378 = v_stack_m33F;
    v_stack_m380 = 17;
    v_stack_m388 = v_rip - 9792626;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    v_stack_m33F = 255;
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5162292), a2, *(unsigned __int64 *)(v_stack_m348 + 8), 1);
    if (!sign_flag) goto loc_00979EF4;
    goto loc_00977D70;
loc_00979EB1:
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = 0;
        a1 = *(unsigned __int64 *)(v_rip + 5162196);
        a4 = 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        result = v_rip - 9792717;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (condition_is_above_or_equal) goto loc_00979F56;
    v_r12 = 0;
    v_stack_m368 = 0;
    v_stack_m370 = 1;
    v_stack_m378 = v_stack_m33E;
    v_stack_m380 = 17;
    v_stack_m388 = v_rip - 9854082;
    v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
    v_stack_m33E = 255;
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5162125), a2, *(unsigned __int64 *)(v_stack_m348 + 8), v_r12 + 1);
    if (!sign_flag) goto loc_00979F9C;
    goto loc_00977D70;
loc_00979F56:
    v_r12 = 0;
    result = (unsigned int)(*(unsigned int *)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) & (1)) == 0) {
        a3 = *(unsigned __int64 *)(v_stack_m348 + 8);
        result = v_rip - 9854146;
        a1 = *(unsigned __int64 *)(v_rip + 5162023);
        a4 = v_r12 + 1;
        v_stack_m368 = 0;
        a2 = a2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(unsigned __int64 *)(a2 + 16);
        result = PiDevCfgSetObjectProperty(a1, a2, a3, a4);
    }
    if (v_stack_m268 == 0) goto loc_00979FB1;
    if (v_stack_m270 != 0) {
        result = PipHardwareConfigActivateService(v_stack_m268, a2, a3, a4);
    }
    if (v_stack_m348 == 0) goto loc_0097A003;
    if ((*(unsigned __int16 *)(v_stack_m348)) == 0) goto loc_0097A003;
loc_00979FC4:
    result = PipHardwareConfigActivateService(v_stack_m348, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 4786701)) != 0) goto loc_00979FE7;
    result = (unsigned int)(*(unsigned int *)(a3 + 184));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 184)))) & (16)) != 0) {
        a1 = v_stack_m348;
        result = PiDevCfgMakeServiceBootStart(a1, a2, a3, a4);
    }
    result = (result) | (-1);
loc_00979FEB:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m348 + result * 2)) != 0) goto loc_00979FEB;
    v_rdi = (v_stack_m348 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rdi)) != 0) goto loc_00979FC4;
loc_0097A003:
    if (v_stack_m248 == 0) goto loc_00977D75;
    if ((*(unsigned __int16 *)(v_stack_m248)) == 0) goto loc_00977D75;
loc_0097A01D:
    result = PipHardwareConfigActivateService(v_stack_m248, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 4786612)) != 0) goto loc_0097A040;
    result = (unsigned int)(*(unsigned int *)(a3 + 184));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 184)))) & (16)) != 0) {
        a1 = v_stack_m248;
        result = PiDevCfgMakeServiceBootStart(a1, a2, a3, a4);
    }
    result = (result) | (-1);
loc_0097A044:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m248 + result * 2)) != 0) goto loc_0097A044;
    v_rdi = (v_stack_m248 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rdi)) != 0) goto loc_0097A01D;
    goto loc_00977D75;
loc_0097A061:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (888);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgConfigureDevice(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1DC;
    uint32_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint32_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint32_t v_stack_m2A8;
    uint32_t v_stack_m2AC;
    uint32_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint32_t v_stack_m31C;
    uint32_t v_stack_m320;
    uint32_t v_stack_m324;
    uint32_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint8_t v_stack_m33E;
    uint8_t v_stack_m33F;
    uint8_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint32_t v_stack_m354;
    uint8_t v_stack_m355;
    uint8_t v_stack_m356;
    uint8_t v_stack_m357;
    uint8_t v_stack_m358;
    uint32_t v_stack_m368;
    uint64_t v_stack_m370;
    uint32_t v_stack_m378;
    uint64_t v_stack_m380;
    uint64_t v_stack_m388;
    uint8_t v_stack_m390;
    uint8_t v_stack_m398;
    uint64_t v_stack_m58;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (888);
    result = (*(uint64_t *)(v_rip + 0x492B69)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m318 = Arg1;
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(0x400ULL));
    v_stack_m288 = Arg4;
    result = 0;
    v_stack_m290 = Arg5;
    Arg3 = 0;
    v_stack_m1DC = 0;
    v_stack_m2F0 = 0;
    *(uint32_t *)(arg5) = 0;
    v_stack_m260 = 0;
    v_stack_m270 = 0;
    v_stack_m268 = 0;
    v_stack_m350 = 0;
    v_stack_m348 = 0;
    v_stack_m250 = 0;
    v_stack_m248 = 0;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    v_stack_m218 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = 0;
    v_stack_m1F0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m338 = 0;
    v_stack_m330 = 0;
    v_stack_m200 = 0;
    v_stack_m1F8 = 0;
    v_stack_m324 = 0;
    v_stack_m31C = 0;
    v_stack_m328 = 0;
    v_stack_m2A4 = 0;
    v_stack_m2A0 = 0;
    v_stack_m298 = 0;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    v_stack_m310 = 0;
    v_stack_m308 = 0;
    v_stack_m2E0 = 0;
    v_stack_m2D8 = 0;
    v_stack_m2D0 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m240 = 0;
    v_stack_m238 = 0;
    v_stack_m357 = 0;
    v_stack_m340 = 0;
    v_stack_m358 = 0;
    v_stack_m356 = 0;
    v_stack_m258 = 0;
    v_stack_m2B0 = 0;
    v_stack_m320 = 0;
    v_stack_m355 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m33F = 0;
    v_stack_m33E = 0;
    v_stack_m2AC = 0;
    v_stack_m2A8 = 0;
    v_stack_m300 = v_xmm0;
    v_stack_m354 = (uint32_t)((uint32_t)(0x400ULL));
    v_stack_m1C0 = v_xmm0;
    v_stack_m2E8 = 0;
    v_stack_m2C8 = 0;
    v_stack_m1E0 = 0x4100000ULL;
    result = ExAllocatePool2(256, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
    v_stack_m1D8 = result;
    if (result != 0) goto loc_00977ED3;
loc_00977D67:
loc_00977D6C:
loc_00977D70:
loc_00977D75:
    if (v_stack_m308 != 0) {
        result = ExFreePool(v_stack_m308, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
        v_stack_m310 = v_xmm0;
    }
    if (v_stack_m2D8 != 0) {
        result = ExFreePool(v_stack_m2D8, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
        v_stack_m2E0 = v_xmm0;
    }
    if (v_stack_m278 != 0) {
        result = ExFreePool(v_stack_m278, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
        v_stack_m280 = v_xmm0;
    }
    result = v_stack_m268;
    if (v_stack_m268 != 0) {
        Arg1 = v_stack_m268;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
    }
    if (v_stack_m348 != 0) {
        Arg1 = v_stack_m348;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
    }
    result = v_stack_m248;
    if (v_stack_m248 != 0) {
        Arg1 = v_stack_m248;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, (uint32_t)(0x63647050ULL), Arg4);
    }
    if (v_stack_m228 != 0) {
        Arg1 = v_stack_m228;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    if (v_stack_m218 != 0) {
        result = ExFreePool(v_stack_m218, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    if (v_stack_m208 != 0) {
        result = ExFreePool(v_stack_m208, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    result = v_stack_m1E8;
    if (v_stack_m1E8 != 0) {
        Arg1 = v_stack_m1E8;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    if (v_stack_m330 != 0) {
        Arg1 = v_stack_m330;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    if (v_stack_m1F8 != 0) {
        result = ExFreePool(v_stack_m1F8, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    result = v_stack_m2E8;
    if (v_stack_m2E8 != 0) {
        Arg1 = v_stack_m2E8;
        result = ExFreePool(Arg1, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
    }
    if (v_stack_m238 != 0) {
        result = ExFreePool(v_stack_m238, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
        v_stack_m240 = v_xmm0;
    }
    if (v_stack_m2B8 != 0) {
        result = ExFreePool(v_stack_m2B8, (uint32_t)(0x400ULL) + 16, v_stack_m228, Arg4);
        v_stack_m2C0 = v_xmm0;
    }
    result = v_stack_m1D8;
    if (v_stack_m1D8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m1D8;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m228, Arg4);
    }
    if (v_stack_m258 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m258, Arg2, v_stack_m228, Arg4);
    }
    if (v_stack_m2F0 != 0) {
        result = ZwClose(v_stack_m2F0, Arg2, v_stack_m228, Arg4);
    }
    if (v_stack_m260 != 0) {
        result = ZwClose(v_stack_m260, Arg2, v_stack_m228, Arg4);
    }
    goto loc_0097A061;
loc_00977ED3:
    if (0 == 0) goto loc_009785C3;
    result = PiDevCfgQueryDriverConfiguration(0, Arg2, v_stack_m228, Arg4);
    if (sign_flag) goto loc_00977D6C;
    v_stack_m298 = *(uint64_t *)(Arg3 + 0x108);
    if ((*(uint64_t *)(Arg3 + 0x128)) == 0) goto loc_00977F1A;
    result = PnpDuplicateUnicodeString(v_stack_m270, Arg3 + 288, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977F1A:
    if ((*(uint64_t *)(Arg3 + 0x138)) == 0) goto loc_00977F3C;
    result = PnpDuplicateUnicodeString(v_stack_m350, Arg3 + 304, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977F3C:
    if ((*(uint64_t *)(Arg3 + 0x148)) == 0) goto loc_00977F5D;
    result = PnpDuplicateUnicodeString(v_stack_m250, Arg3 + 320, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977F5D:
    if ((*(uint64_t *)(Arg3 + 0x158)) == 0) goto loc_00977F81;
    result = PnpDuplicateUnicodeString(v_stack_m230, Arg3 + 336, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977F81:
    if ((*(uint64_t *)(Arg3 + 0x168)) == 0) goto loc_00977FA5;
    result = PnpDuplicateUnicodeString(v_stack_m220, Arg3 + 352, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977FA5:
    if ((*(uint64_t *)(Arg3 + 0x178)) == 0) goto loc_00977FC9;
    result = PnpDuplicateUnicodeString(v_stack_m210, Arg3 + 368, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977FC9:
    if ((*(uint64_t *)(Arg3 + 0x198)) == 0) goto loc_00977FED;
    result = PnpDuplicateUnicodeString(v_stack_m200, Arg3 + 400, v_stack_m228, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00977D67;
loc_00977FED:
    v_stack_m324 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x1A4)));
    v_stack_m354 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x1A0)));
    v_stack_m31C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xB8)));
    if ((*(uint64_t *)(Arg3 + 0xD0)) == (Arg3 + 208)) goto loc_00978228;
loc_0097801E:
    result = PiDevCfgQueryDriverConfiguration(*(uint64_t *)(Arg3 + 0xD0), (uint32_t)(*(uint32_t *)(Arg3 + 0xB8)), v_stack_m228, Arg4);
    Arg1 = 0;
    if (!sign_flag) goto loc_00978064;
    if (((uint32_t)(result)) != 0xC0000493ULL) goto loc_00977D6C;
    if ((*(uint8_t *)(v_rip + 0x4929A1)) == 0) goto loc_00977D6C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x65FFE5)))) & (2)) == 0) goto loc_00977D6C;
    v_stack_m354 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x1A0)));
    goto loc_009781FB;
loc_00978064:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x128)) == 0) goto loc_0097807C;
    goto loc_009781FB;
loc_0097807C:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x138)) == 0) goto loc_009780A9;
    Arg4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m350, Arg2, *(uint64_t *)(Arg3 + 0xD0) + 304, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_009780A9:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x148)) == 0) goto loc_009780D5;
    Arg4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m250, Arg2, *(uint64_t *)(Arg3 + 0xD0) + 320, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_009780D5:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x158)) == 0) goto loc_00978104;
    Arg4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m230, Arg2, *(uint64_t *)(Arg3 + 0xD0) + 336, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_00978104:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x168)) == 0) goto loc_00978133;
    Arg4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m220, Arg2, *(uint64_t *)(Arg3 + 0xD0) + 352, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_00978133:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x178)) == 0) goto loc_00978160;
    Arg4 = 0;
    Arg2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m210, Arg2, *(uint64_t *)(Arg3 + 0xD0) + 368, Arg4);
    if (sign_flag) goto loc_00977D6C;
loc_00978160:
    result = (uint32_t)(((uint32_t)(v_stack_m324)) | (*(uint32_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x1A4)));
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x1A0))) | (*(uint32_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x1A0)));
    Arg4 = 0;
    v_stack_m324 = (uint32_t)(result);
    Arg3 = 0;
    result = (uint32_t)(((uint32_t)(v_stack_m31C)) | (*(uint32_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0xB8)));
    v_stack_m31C = (uint32_t)(result);
    v_stack_m354 = (uint32_t)(local_r13);
    result = PiDevCfgAppendMultiSz(v_stack_m1F0, *(uint64_t *)(Arg3 + 0xD0) + 40, Arg3, Arg4);
    if (sign_flag) goto loc_00977D6C;
    Arg4 = 0;
    Arg3 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m338, *(uint64_t *)(Arg3 + 0xD0) + 424, Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00977D6C;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0x198)) == 0) goto loc_009781FB;
    Arg4 = 0;
    Arg3 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_m200, *(uint64_t *)(Arg3 + 0xD0) + 400, Arg3, Arg4);
    if (sign_flag) goto loc_00977D6C;
loc_009781FB:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0))) != (Arg3 + 208)) goto loc_0097801E;
    local_r12 = 0;
    v_stack_m324 = (uint32_t)((uint32_t)(v_stack_m324));
    v_stack_m31C = (uint32_t)((uint32_t)(v_stack_m31C));
    if (sign_flag) goto loc_00977D6C;
    goto loc_0097822B;
loc_00978228:
    local_r12 = 0;
loc_0097822B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x65FDFF)))) & (2)) == 0) goto loc_00978288;
    if (condition_is_above_or_equal) goto loc_00978270;
    Arg1 = (((*(uint8_t *)(Arg3 + 0x1B8)) & (2)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(v_rip + 0x65FE67)) & (1)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00978270;
    if ((*(uint8_t *)(v_rip + 0x64BEED)) != 0) goto loc_00978270;
    if ((*(uint8_t *)(v_rip + 0x49277C)) != 0) goto loc_00978270;
loc_00978266:
    goto loc_00977D6C;
loc_00978270:
    if ((((uint8_t)((uint32_t)(v_stack_m31C))) & (64)) == 0) goto loc_00978288;
    if ((*(uint8_t *)(v_rip + 0x492764)) == 0) goto loc_00978266;
    v_stack_m354 = (uint32_t)(local_r13);
loc_00978288:
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, 168, Arg4);
    v_stack_m390 = 1;
    v_stack_m100 = 288;
    v_stack_mE8 = (uint32_t)((uint32_t)(0x1000000ULL));
    v_stack_mF8 = v_rip + 1601304;
    v_stack_mB0 = (uint32_t)((uint32_t)(0x1000000ULL));
    Arg4 = 0;
    v_stack_mF0 = v_stack_m310;
    v_stack_mC0 = v_rip + 1601045;
    v_stack_mC8 = 288;
    v_stack_mB8 = v_stack_m2E0;
    result = RtlpQueryRegistryValues((uint32_t)(0xC0000000ULL), *(uint64_t *)(Arg3 + 0x18), v_stack_m108, Arg4);
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m308 != 0) goto loc_00978365;
    if (v_stack_m2D8 != 0) goto loc_00978365;
    if ((*(uint64_t *)(Arg3 + 0xA8)) == 0) goto loc_00978365;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x65FCFE)))) & (2)) == 0) goto loc_00978365;
    if ((*(uint8_t *)(v_rip + 0x64BE0B)) != 0) goto loc_00978365;
    if ((*(uint8_t *)(v_rip + 0x49269A)) != 0) goto loc_0097835B;
    goto loc_00977D9F;
loc_0097835B:
    v_stack_m354 = (uint32_t)(v_stack_m330);
loc_00978365:
    if (v_stack_m310 != 0) goto loc_0097837B;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x65FCFE));
    if (v_stack_m308 != 0) {
        Arg1 = v_stack_m310;
        result = RtlFreeAnsiString(Arg1, *(uint64_t *)(Arg3 + 0x18), v_stack_m108, Arg4);
    }
    if (v_stack_m2E0 != 0) goto loc_00978391;
    if (v_stack_m2D8 != 0) {
        Arg1 = v_stack_m2E0;
        result = RtlFreeAnsiString(Arg1, *(uint64_t *)(Arg3 + 0x18), v_stack_m108, Arg4);
    }
    if (v_stack_m298 == 0) goto loc_00978553;
    v_stack_m390 = v_stack_m2F0;
    v_stack_m398 = 0;
    result = PnpOpenObjectRegKey(*(uint64_t *)(v_rip + 0x4EDFF3), v_stack_m298, 2, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00978553;
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 160, (uint32_t)(0x20019ULL));
    v_stack_m1A8 = v_rip - 9846750;
    v_stack_m1A0 = 17;
    v_stack_m198 = v_stack_m357;
    v_stack_m178 = 17;
    v_stack_m180 = v_rip - 9788030;
    v_stack_m390 = 4;
    v_stack_m170 = v_stack_m358;
    v_stack_m190 = 1;
    v_stack_m158 = v_rip - 9766758;
    v_stack_m148 = v_stack_m280;
    v_stack_m130 = v_rip - 9788265;
    v_stack_m120 = v_stack_m258;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m168 = 1;
    v_stack_m150 = 18;
    v_stack_m13C = 6;
    v_stack_m128 = 0x1003ULL;
    v_stack_m114 = 2;
    result = PiDevCfgQueryObjectProperties(2, v_stack_m298, 2, v_stack_m2F0);
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m188 < 0) {
        v_stack_m357 = 0;
    }
    if (v_stack_m160 < 0) {
        v_stack_m358 = 0;
    }
    if (v_stack_m138 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m280;
        result = RtlInitUnicodeString(Arg1, Arg2, 2, v_stack_m2F0);
    }
    if (v_stack_m110 >= 0) goto loc_00978503;
    v_stack_m258 = 0;
    goto loc_0097850C;
loc_00978503:
    v_stack_m2B0 = (uint32_t)((uint32_t)(v_stack_m118));
loc_0097850C:
    if (v_stack_m357 != 0) goto loc_00978589;
    v_stack_m388 = v_stack_m340;
    v_stack_m390 = *(uint64_t *)(Arg3 + 0x10);
    v_stack_m398 = *(uint64_t *)(Arg3 + 0x40);
    result = PiDevCfgGetDeviceClassDriverConfigurable(v_stack_m298, v_stack_m2F0, *(uint64_t *)(v_stack_m348 + 0x8), *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00978553;
    if (v_stack_m340 != 0) {
        v_stack_m357 = 255;
    }
    if (v_stack_m357 != 0) goto loc_00978589;
    Arg1 = (((*(uint8_t *)(v_rip + 0x65FB53)) & (1)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(v_rip + 0x65FAC5)) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00978589;
    if ((*(uint8_t *)(v_rip + 0x492467)) == 0) goto loc_00978266;
    v_stack_m354 = (uint32_t)(v_stack_m330);
loc_00978589:
    if (v_stack_m258 == 0) goto loc_009785BE;
    if ((uint32_t)((uint32_t)(v_stack_m2B0)) == 0) goto loc_009785B4;
loc_009785A1:
    if ((*(uint8_t *)(v_stack_m258)) == ((uint8_t)(*(uint8_t *)(Arg3 + 0x6E)))) goto loc_009785AF;
    result = (uint32_t)((0) + 1);
    Arg1 = (v_stack_m258) + 1;
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(v_stack_m2B0)))) goto loc_009785A1;
loc_009785AF:
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(v_stack_m2B0)))) goto loc_009785BE;
loc_009785B4:
    goto loc_00977D6C;
loc_009785BE:
loc_009785C3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) != 0) goto loc_009786D2;
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 160, *(uint64_t *)(arg2 + 0x10));
    v_stack_m198 = v_stack_m1C0;
    v_stack_m390 = 3;
    v_stack_m180 = v_rip - 9788484;
    v_stack_m1A8 = v_rip - 9858884;
    v_stack_m170 = v_stack_m320;
    v_stack_m158 = v_rip - 9852586;
    v_stack_m148 = v_stack_m2C0;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m1A0 = 13;
    v_stack_m190 = 16;
    v_stack_m178 = 7;
    v_stack_m168 = 4;
    v_stack_m150 = 18;
    v_stack_m13C = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1A8, *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    Arg2 = 0;
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m188 >= 0) goto loc_009786B1;
    v_stack_m1C0 = v_xmm0;
    goto loc_009786B6;
loc_009786B1:
    v_stack_m355 = 1;
loc_009786B6:
    if (v_stack_m160 < 0) {
        v_stack_m320 = 0;
    }
    if (v_stack_m138 >= 0) goto loc_009786D4;
    result = RtlInitUnicodeString(v_stack_m2C0, Arg2, 1, *(uint64_t *)(arg2 + 0x10));
loc_009786D2:
    Arg2 = 0;
loc_009786D4:
    if (v_stack_m358 != 0) goto loc_009787BD;
    if (((v_stack_m320) & (4)) == 0) goto loc_009787A1;
    if (0 == 0) goto loc_00978796;
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 160, *(uint64_t *)(arg2 + 0x10));
    v_stack_m198 = v_stack_m240;
    v_stack_m390 = 1;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m1A8 = v_rip - 9852731;
    v_stack_m1A0 = 18;
    v_stack_m18C = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1A8, *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    Arg2 = 0;
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m188 < 0) {
        Arg1 = v_stack_m240;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(arg2 + 0x10));
        Arg2 = 0;
    }
    if (v_stack_m238 == 0) goto loc_0097879B;
    result = RtlEqualUnicodeString(v_stack_m240, Arg3 + 40, 1, *(uint64_t *)(arg2 + 0x10));
    Arg2 = 0;
    if ((uint8_t)(result) != 0) {
        v_stack_m358 = 255;
    }
    if (v_stack_m358 != 0) goto loc_009787BD;
loc_009787A1:
    result = PiDevCfgEnforceDevicePolicy(v_stack_m318, 0, v_stack_m298, *(uint64_t *)(arg2 + 0x10));
    Arg2 = 0;
    if (sign_flag) goto loc_00977D6C;
loc_009787BD:
    if (v_stack_m2F0 == 0) goto loc_0097881B;
    v_stack_m300 = 0x1C001AULL;
    v_stack_m2F8 = v_rip + 1597571;
    result = IopOpenRegistryKeyEx(v_stack_m260, v_stack_m2F0, v_stack_m300, (uint32_t)(0x20019ULL));
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00978819;
    if (sign_flag) goto loc_00977D6C;
    result = PiDevCfgVerifyDeviceAllowed(v_stack_m318, v_stack_m260, v_stack_m300, (uint32_t)(0x20019ULL));
    Arg2 = 0;
    if (!sign_flag) goto loc_0097881B;
    goto loc_00977D6C;
loc_00978819:
    Arg2 = 0;
loc_0097881B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m318 + 0x20) + 0x8) + 0x10)))) & (4)) == 0) goto loc_00978896;
    v_stack_m368 = 0;
    v_stack_m370 = v_stack_m2A8;
    v_stack_m378 = 1;
    v_stack_m380 = v_stack_m356;
    v_stack_m388 = v_stack_m2AC;
    v_stack_m390 = v_rip - 9847877;
    v_stack_m398 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x4EDB63), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    Arg2 = 0;
    if (sign_flag) goto loc_00978892;
    if (v_stack_m2AC != 17) goto loc_00978892;
    if (v_stack_m2A8 != 1) {
        v_stack_m356 = 0;
    }
    if (0 == 0) goto loc_009788C4;
    if (v_stack_m268 != 0) goto loc_009788C4;
    if (v_stack_m278 != 0) goto loc_009788C4;
    if (v_stack_m356 != 0) goto loc_009788C4;
    if (((*(uint32_t *)(v_stack_m318 + 0x230)) & (256)) != 0) goto loc_009788C4;
    goto loc_00977D6C;
loc_009788C4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) != 0) goto loc_00978986;
    if (0 != 0) goto loc_00978926;
    if (v_stack_m355 == 0) goto loc_009788E5;
    result = (uint32_t)(*(uint32_t *)(arg2));
    if (((*(uint32_t *)((uint32_t)(0xC0000494ULL) + 0x230)) & (256)) == 0) {
        Arg2 = *(uint64_t *)(v_stack_m348 + 0x8);
        Arg4 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x4EDAA5);
        Arg3 = Arg4 + 17;
        result = _CmDeleteDeviceRegKey(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    result = _CmDeleteDeviceRegKey(*(uint64_t *)(v_rip + 0x4EDA8E), *(uint64_t *)(v_stack_m348 + 0x8), Arg4 + 18, Arg4);
    Arg2 = 0;
loc_00978915:
    if (Arg3 == 0) goto loc_0097898D;
loc_0097891D:
    goto loc_00978990;
loc_00978926:
    result = PnpIsNullGuid(v_stack_m1C0, Arg2, Arg3 + 256, 0);
    if ((uint8_t)(result) != 0) goto loc_00978980;
    result = PnpIsNullGuid(Arg3 + 240, Arg2, Arg3 + 256, 0);
    if ((uint8_t)(result) != 0) goto loc_0097897C;
    Arg1 = (v_stack_m1C0) - (*(uint64_t *)(Arg3 + 0xF0));
    if (!(condition_is_not_equal)) {
        Arg1 = v_stack_m1B8;
        Arg1 = (Arg1) - (*(uint64_t *)(Arg3 + 0xF0 + 0x8));
    }
    if (Arg1 != NULL) {
        Arg2 = *(uint64_t *)(v_stack_m348 + 0x8);
        Arg4 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x4EDA25);
        Arg3 = Arg4 + 18;
        result = _CmDeleteDeviceRegKey(Arg1, Arg2, Arg3, Arg4);
    }
loc_00978980:
    goto loc_0097891D;
loc_00978986:
    if (Arg3 != 0) goto loc_00978980;
    goto loc_00978915;
loc_0097898D:
loc_00978990:
    v_stack_m390 = v_stack_m2A0;
    v_stack_m398 = v_stack_m2A4;
    result = PiDevCfgMigrateDevice(v_stack_m318, Arg2, Arg2, Arg3 + 40);
    Arg2 = 0;
    local_r13 = v_stack_m330;
    if (!(sign_flag)) {
        local_r13 = (uint32_t)((v_stack_m330) | (v_stack_m2A4));
        result = v_stack_m2A0;
        v_stack_m354 = (uint32_t)(local_r13);
        v_stack_m328 = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) != 0) goto loc_00978A2C;
    result = (uint8_t)(-(v_stack_m355));
    Arg1 = (v_stack_m318) & (v_stack_m1C0);
    if (Arg3 == 0) {
        Arg3 = 0;
    }
    v_stack_m398 = Arg1;
    result = PiDevCfgResetDeviceDriverSettings(v_stack_m318, 0, Arg3, v_stack_m2F0);
    result = PnpCtxRegDeleteTree(*(uint64_t *)(v_rip + 0x4ED993), *(uint64_t *)(arg2 + 0x10), v_rip + 1592628, v_stack_m2F0);
    result = PnpCtxRegDeleteTree(*(uint64_t *)(v_rip + 0x4ED97D), *(uint64_t *)(arg2 + 0x10), v_rip + 1597006, v_stack_m2F0);
    Arg2 = 0;
loc_00978A2C:
    if (Arg3 == 0) goto loc_00978A92;
    result = PnpIsNullGuid(Arg3 + 240, Arg2, v_rip + 1597006, v_stack_m2F0);
    Arg2 = 0;
    if ((uint8_t)(result) != 0) goto loc_00978A92;
    v_stack_m368 = 0;
    v_stack_m370 = 16;
    v_stack_m378 = Arg3 + 240;
    v_stack_m380 = 13;
    v_stack_m388 = v_rip - 9860041;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED940), 0, *(uint64_t *)(v_stack_m348 + 0x8), Arg2 + 1);
    if (!sign_flag) goto loc_00978AD3;
    goto loc_00977D6C;
loc_00978A92:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9860123;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED8EE);
        Arg4 = 1;
        v_stack_m368 = 0;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        Arg2 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = 0;
    if (v_stack_m268 == 0) goto loc_00978AFD;
    if ((uint16_t)(v_stack_m270) == 0) goto loc_00978B5B;
    v_stack_m368 = 0;
    result = (uint32_t)((v_stack_m270) + (2));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = v_stack_m268;
    goto loc_00978B1B;
loc_00978AFD:
    if (v_stack_m278 == 0) goto loc_00978B5B;
    if ((uint16_t)(v_stack_m280) == 0) goto loc_00978B5B;
    v_stack_m368 = 0;
    result = (uint32_t)((v_stack_m280) + (2));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = v_stack_m278;
loc_00978B1B:
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9807318;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED86B), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (sign_flag) goto loc_00977D6C;
    local_rbx = 0;
    goto loc_00978BAC;
loc_00978B5B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) != 0) goto loc_00978BAC;
    if (Arg2 == NULL) goto loc_00978B6B;
    if (*(uint64_t *)(v_rip + 0x4ED86B) != 0) goto loc_00978B71;
loc_00978B6B:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if (v_stack_m356 == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9807404;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED815);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m348 == 0) goto loc_00978C03;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m350);
    v_stack_m378 = v_stack_m348;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9849713;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED7CE), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    local_r12 = 0;
    if (!sign_flag) goto loc_00978C49;
    goto loc_00977D6C;
loc_00978C03:
    local_r12 = 0;
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9849775;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED77A);
        Arg4 = local_r12 + 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m248 == 0) goto loc_00978CA1;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m250);
    v_stack_m378 = v_stack_m248;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9849747;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED719), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_00978CE5;
    goto loc_00977D6C;
loc_00978CA1:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9849810;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED6DF);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m228 == 0) goto loc_00978D4B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(v_stack_m230);
    v_stack_m380 = v_stack_m228;
    v_stack_m388 = 0x2012ULL;
    v_stack_m390 = v_rip - 9854586;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED67B), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    goto loc_00978D8D;
loc_00978D4B:
    if ((((uint8_t)(result)) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9854658;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED637);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg3 == 0) goto loc_00978F91;
    if (v_stack_m308 == 0) goto loc_00978F91;
    result = PiDevCfgBuildIndirectString(Arg3, v_stack_m310, v_stack_m2D0, v_stack_m1D0);
    if (sign_flag) goto loc_00978F84;
    v_stack_m2E8 = v_stack_m2C8;
    Arg1 = (condition_is_below) ? 1 : 0;
    result = (((*(uint8_t *)(v_rip + 0x65F2DC)) & (1)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00978E37;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg1 = (uint32_t)((v_stack_m2D0) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg1);
    v_stack_m380 = v_stack_m2C8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9850072;
    result = 0;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED58D), *(uint64_t *)(v_stack_m348 + 0x8), result + 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
loc_00978E37:
    local_rbx = 0;
    if (v_stack_m1C8 == 0) goto loc_00978EA0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg1 = (uint32_t)((v_stack_m1D0) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg1);
    v_stack_m380 = v_stack_m1C8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9854593;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED524), *(uint64_t *)(v_stack_m348 + 0x8), local_rbx + 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    goto loc_00978EDF;
loc_00978EA0:
    if ((((uint8_t)(result)) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9854663;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED4E2);
        Arg4 = 1;
        v_stack_m368 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg2 = Arg2;
        v_stack_m370 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m378 = (uint32_t)((uint32_t)(result));
        v_stack_m380 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m2C8 != 0) {
        Arg1 = v_stack_m2C8;
        result = ExFreePool(Arg1, Arg2, Arg3, Arg4);
        v_stack_m2D0 = v_xmm0;
        v_stack_m2E8 = v_xmm0;
    }
    local_r12 = 0;
loc_00978F00:
    if (v_stack_m2D8 == 0) goto loc_009790B7;
    Arg4 = 0;
    result = PiDevCfgBuildIndirectString(Arg3, v_stack_m2E0, v_stack_m2D0, Arg4);
    if (sign_flag) goto loc_00978F84;
    result = (uint32_t)((v_stack_m2D0) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = v_stack_m2C8;
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9768506;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    v_stack_m2E8 = v_stack_m2C8;
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED45D), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    local_r12 = 0;
    if (!sign_flag) goto loc_009790FB;
    goto loc_00977D6C;
loc_00978F84:
    v_stack_m2E8 = v_stack_m2C8;
    goto loc_00977D6C;
loc_00978F91:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) != 0) goto loc_009791B4;
    v_stack_m368 = 0;
    v_stack_m370 = 0;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m388 = v_rip - 9854910;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED3EB), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (Arg3 != 0) goto loc_00978F00;
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 160, 1);
    v_stack_m1A8 = v_rip - 9769857;
    v_stack_m390 = (uint32_t)(Arg3 + 1);
    v_stack_m198 = v_stack_m310;
    v_stack_m1A0 = 18;
    v_stack_m398 = v_stack_m1A8;
    v_stack_m18C = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1A8, *(uint64_t *)(v_stack_m348 + 0x8), (uint32_t)((uint32_t)(Arg3 + 1)), *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00979174;
    if (v_stack_m188 < 0) goto loc_00979174;
    if (v_stack_m308 == 0) goto loc_00979174;
    result = (uint32_t)((v_stack_m310) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = v_stack_m308;
    v_stack_m380 = (uint32_t)((uint32_t)(v_stack_m1A0));
    v_stack_m388 = v_rip - 9850742;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED305), 0, *(uint64_t *)(v_stack_m348 + 0x8), (uint32_t)((uint32_t)(Arg3 + 1)));
    if (sign_flag) goto loc_00977D6C;
loc_009790B7:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9768880;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED2C9);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = 0;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg3 == 0) goto loc_009791C2;
    if (*(uint64_t *)(Arg3 + 0x118) == 0) goto loc_009791C2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg1 = (uint32_t)((*(uint16_t *)(Arg3 + 0x110)) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg1);
    v_stack_m380 = *(uint64_t *)(Arg3 + 0x118);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9855336;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED255), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (!sign_flag) goto loc_0097920F;
    goto loc_00977D6C;
loc_00979174:
    v_stack_m368 = 0;
    v_stack_m370 = 0;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m388 = v_rip - 9850967;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED212), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_009790B7;
loc_009791B4:
    if (Arg3 != 0) goto loc_00978F00;
    goto loc_009790B7;
loc_009791C2:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9855491;
        Arg1 = *(uint64_t *)(v_rip + 0x4ED1BE);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg3 == 0) goto loc_00979486;
loc_0097920F:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg1 = (uint32_t)((Arg1) << (17));
    v_stack_m370 = (uint32_t)(Arg1);
    v_stack_m378 = 8;
    v_stack_m380 = Arg3 + 112;
    v_stack_m388 = 16;
    v_stack_m390 = v_rip - 9855727;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED165), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    v_stack_m390 = (uint32_t)(*(uint16_t *)(Arg3 + 0x78));
    result = ((uint32_t)(*(uint32_t *)(Arg3 + 0x7C))) >> (16);
    v_stack_m398 = (uint32_t)(*(uint16_t *)(Arg3 + 0x7A));
    result = RtlUnicodeStringPrintf(v_stack_m1E0, v_rip + 1594910, (uint16_t)(result), *(uint16_t *)(Arg3 + 0x7C));
    if (sign_flag) goto loc_00977D6C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg1 = (uint32_t)((v_stack_m1E0) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg1);
    v_stack_m380 = v_stack_m1D8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9855790;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED0BE), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg2 = (uint32_t)((*(uint16_t *)(Arg3 + 0x28)) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg2);
    v_stack_m380 = *(uint64_t *)(Arg3 + 0x30);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9855886;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ED056), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg2 = (uint32_t)((*(uint16_t *)(Arg3 + 0x58)) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg2);
    v_stack_m380 = *(uint64_t *)(Arg3 + 0x60);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9856026;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECFFA), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    result = PiDevCfgBuildDriverNodeStrongName(Arg3, v_stack_m2E0, v_stack_m310, v_stack_m300);
    if (sign_flag) goto loc_00977D6C;
    if (v_stack_m2B8 == 0) goto loc_00979410;
    Arg4 = (v_stack_m300) >> (1);
    Arg2 = (v_stack_m2C0) >> (1);
    v_stack_m398 = 1;
    result = RtlCompareUnicodeStrings(v_stack_m2B8, Arg2, v_stack_m2F8, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = v_stack_m2C0;
        result = RtlFreeAnsiString(Arg1, Arg2, v_stack_m2F8, Arg4);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg1 = (uint32_t)((v_stack_m300) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg1);
    v_stack_m380 = v_stack_m2F8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9856195;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECF59), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (v_stack_m2F8 != 0) {
        result = ExFreePool(v_stack_m2F8, *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
        v_stack_m300 = v_xmm0;
    }
    if (sign_flag) goto loc_00977D6C;
    goto loc_009795C6;
loc_00979486:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9856323;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECEF6);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9856289;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECEB8);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9856375;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECE7A);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9856485;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECE3C);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9856523;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECDFE);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m2B8 == 0) goto loc_00979637;
    if (((v_stack_m320) & (8)) != 0) goto loc_00979637;
    if (((*(uint32_t *)(v_stack_m318 + 0x18C)) & (0x6000ULL)) != 0) goto loc_00979637;
    result = (uint32_t)((v_stack_m2C0) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = v_stack_m2B8;
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9791265;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECD83), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_0097967B;
    goto loc_00977D6C;
loc_00979637:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9791328;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECD49);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m218 == 0) goto loc_009796D9;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m220);
    v_stack_m378 = v_stack_m218;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9797803;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECCE1), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_0097971D;
    goto loc_00977D6C;
loc_009796D9:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9797866;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECCA7);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m208 == 0) goto loc_0097977B;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m210);
    v_stack_m378 = v_stack_m208;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9794357;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECC3F), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_009797BF;
    goto loc_00977D6C;
loc_0097977B:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9794420;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECC05);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1F8 == 0) goto loc_0097981D;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m200);
    v_stack_m378 = v_stack_m1F8;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9791439;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECB9D), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_00979861;
    goto loc_00977D6C;
loc_0097981D:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9791502;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECB63);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1E8 == 0) goto loc_009798BF;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m1F0);
    v_stack_m378 = v_stack_m1E8;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9797281;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECAFB), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_00979903;
    goto loc_00977D6C;
loc_009798BF:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9797344;
        Arg1 = *(uint64_t *)(v_rip + 0x4ECAC1);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg3 == 0) goto loc_009799D6;
    if ((*(uint32_t *)(Arg3 + 0x6C)) == -1) goto loc_009799D3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    Arg2 = (uint32_t)((*(uint16_t *)(Arg3 + 0x48)) + (2));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = (uint32_t)(Arg2);
    v_stack_m380 = *(uint64_t *)(Arg3 + 0x50);
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9857316;
    result = 0;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECA48), *(uint64_t *)(v_stack_m348 + 0x8), result + 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = 4;
    v_stack_m380 = Arg3 + 108;
    local_r12 = 0;
    v_stack_m388 = 7;
    v_stack_m390 = v_rip - 9857432;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4ECA0E), *(uint64_t *)(v_stack_m348 + 0x8), local_r12 + 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D6C;
    goto loc_00979A58;
loc_009799D3:
    local_r12 = 0;
loc_009799D6:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9857487;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC9AA);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9857573;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC96C);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m320 != 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9793705;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC928);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg3 == 0) goto loc_00979B9A;
    *(uint32_t *)(v_stack_m288) = (uint32_t)(local_r13);
    Arg1 = (((*(uint8_t *)(Arg3 + 0xB8)) & (8)) != 0) ? 1 : 0;
    result = (((*(uint8_t *)(v_rip + 0x65E572)) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        *(uint32_t *)(v_stack_m288) = (uint32_t)(local_r13);
    }
    v_stack_m398 = v_stack_m328;
    result = PiDevCfgConfigureDeviceDriver(v_stack_m318, Arg2, Arg3, v_stack_m354);
    if (sign_flag) goto loc_00977D6C;
    goto loc_00979B5D;
loc_00979B13:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3 + 0xD0) + 0xB8)))) & (1)) == 0) goto loc_00979B59;
    v_stack_m398 = v_stack_m328;
    result = PiDevCfgConfigureDeviceDriver(v_stack_m318, Arg2, *(uint64_t *)(Arg3 + 0xD0), v_stack_m354);
    if (sign_flag) goto loc_00977D6C;
loc_00979B59:
loc_00979B5D:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0xD0))) != (Arg3 + 208)) goto loc_00979B13;
    result = PiDevCfgConfigureDeviceLocation(v_stack_m318, Arg2, v_stack_m354, v_stack_m328);
    if (sign_flag) goto loc_00977D6C;
    goto loc_00979BCD;
loc_00979B9A:
    if (((*(uint32_t *)(v_stack_m318 + 0x230)) & (256)) == 0) goto loc_00979BB9;
    *(uint32_t *)(v_stack_m288) = (uint32_t)(v_stack_m290);
    goto loc_00979BD1;
loc_00979BB9:
    *(uint32_t *)(v_stack_m288) = 64;
    result = PnpDeleteDeviceInterfaces(v_stack_m348, Arg2, v_stack_m354, v_stack_m328);
loc_00979BCD:
loc_00979BD1:
    Arg4 = 0;
    if (v_stack_m324 == 0) goto loc_00979BF4;
    if ((*(uint8_t *)(v_rip + 0x64A567)) != 0) goto loc_00979BF4;
    result = PipIsDevNodeDNStarted(v_stack_m318, Arg2, v_stack_m354, Arg4);
    if ((uint32_t)(result) != 0) {
    }
    if (((v_stack_m320) & (2)) != 0) {
    }
    if (v_stack_m355 != 0) {
    }
    if (v_stack_m260 == 0) goto loc_00979C4F;
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    v_stack_m390 = v_stack_m328;
    v_stack_m398 = v_stack_m354;
    result = PiDevCfgConfigureDeviceKeys(v_stack_m318, Arg2, v_stack_m260, Arg4);
    if (sign_flag) goto loc_00977D6C;
loc_00979C4F:
    local_r12 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m290)))) & (2)) != 0) goto loc_00979C92;
    if (v_stack_m357 != 255) goto loc_00979C92;
    if (v_stack_m298 == 0) goto loc_00979C92;
    if (v_stack_m2F0 == 0) goto loc_00979C92;
    result = PiDevCfgGetDeviceClassConfigFlags(v_stack_m298, v_stack_m2F0, v_stack_m354, Arg4);
    if (sign_flag) goto loc_00977D6C;
loc_00979C92:
    if (Arg3 == 0) goto loc_00979CA0;
    goto loc_00979CA7;
loc_00979CA0:
loc_00979CA7:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    result = (uint32_t)((result) << (17));
    v_stack_m370 = (uint32_t)(result);
    v_stack_m300 = v_xmm0;
    Arg2 = (uint32_t)((v_stack_m300) + (2));
    v_stack_m378 = (uint32_t)(Arg2);
    v_stack_m380 = v_stack_m2F8;
    v_stack_m388 = 18;
    v_stack_m390 = v_rip - 9858615;
    v_stack_m398 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x4EC6E5), *(uint64_t *)(v_stack_m348 + 0x8), 1, *(uint64_t *)(arg2 + 0x10));
    if (sign_flag) goto loc_00977D70;
    if (v_stack_m330 == 0) goto loc_00979D60;
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(v_stack_m338);
    v_stack_m378 = v_stack_m330;
    v_stack_m380 = 0x2012ULL;
    v_stack_m388 = v_rip - 9772593;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4EC66F), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_00979DA4;
    goto loc_00977D70;
loc_00979D60:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9772649;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC620);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg3 == 0) goto loc_00979E0A;
    if (*(uint64_t *)(Arg3 + 0x88) == 0) goto loc_00979E0A;
    result = (uint32_t)((*(uint16_t *)(Arg3 + 0x80)) + (2));
    v_stack_m368 = 0;
    v_stack_m370 = (uint32_t)(result);
    v_stack_m378 = *(uint64_t *)(Arg3 + 0x88);
    v_stack_m380 = 18;
    v_stack_m388 = v_rip - 9795092;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4EC5B0), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_00979E4E;
    goto loc_00977D70;
loc_00979E0A:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9795155;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC576);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (!sign_flag) goto loc_00979EB1;
    result = 0;
    v_stack_m368 = 0;
    v_stack_m370 = 1;
    v_stack_m378 = v_stack_m33F;
    v_stack_m380 = 17;
    v_stack_m388 = v_rip - 9792626;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    v_stack_m33F = 255;
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4EC534), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), 1);
    if (!sign_flag) goto loc_00979EF4;
    goto loc_00977D70;
loc_00979EB1:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC4D4);
        Arg4 = 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        result = v_rip - 9792717;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (condition_is_above_or_equal) goto loc_00979F56;
    local_r12 = 0;
    v_stack_m368 = 0;
    v_stack_m370 = 1;
    v_stack_m378 = v_stack_m33E;
    v_stack_m380 = 17;
    v_stack_m388 = v_rip - 9854082;
    v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
    v_stack_m33E = 255;
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4EC48D), Arg2, *(uint64_t *)(v_stack_m348 + 0x8), local_r12 + 1);
    if (!sign_flag) goto loc_00979F9C;
    goto loc_00977D70;
loc_00979F56:
    local_r12 = 0;
    result = (uint32_t)(*(uint32_t *)(arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) & (1)) == 0) {
        Arg3 = *(uint64_t *)(v_stack_m348 + 0x8);
        result = v_rip - 9854146;
        Arg1 = *(uint64_t *)(v_rip + 0x4EC427);
        Arg4 = local_r12 + 1;
        v_stack_m368 = 0;
        Arg2 = Arg2;
        v_stack_m370 = 0;
        v_stack_m378 = 0;
        v_stack_m380 = 0;
        v_stack_m388 = result;
        v_stack_m398 = *(uint64_t *)(arg2 + 0x10);
        result = PiDevCfgSetObjectProperty(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m268 == 0) goto loc_00979FB1;
    if (v_stack_m270 != 0) {
        result = PipHardwareConfigActivateService(v_stack_m268, Arg2, Arg3, Arg4);
    }
    if (v_stack_m348 == 0) goto loc_0097A003;
    if ((*(uint16_t *)(v_stack_m348)) == 0) goto loc_0097A003;
loc_00979FC4:
    result = PipHardwareConfigActivateService(v_stack_m348, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x490A0D)) != 0) goto loc_00979FE7;
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0xB8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xB8)))) & (16)) != 0) {
        Arg1 = v_stack_m348;
        result = PiDevCfgMakeServiceBootStart(Arg1, Arg2, Arg3, Arg4);
    }
    result = (result) | (-1);
loc_00979FEB:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m348 + result * 2)) != 0) goto loc_00979FEB;
    local_rdi = (v_stack_m348 + result * 2) + (2);
    if ((*(uint16_t *)(local_rdi)) != 0) goto loc_00979FC4;
loc_0097A003:
    if (v_stack_m248 == 0) goto loc_00977D75;
    if ((*(uint16_t *)(v_stack_m248)) == 0) goto loc_00977D75;
loc_0097A01D:
    result = PipHardwareConfigActivateService(v_stack_m248, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x4909B4)) != 0) goto loc_0097A040;
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0xB8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xB8)))) & (16)) != 0) {
        Arg1 = v_stack_m248;
        result = PiDevCfgMakeServiceBootStart(Arg1, Arg2, Arg3, Arg4);
    }
    result = (result) | (-1);
loc_0097A044:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m248 + result * 2)) != 0) goto loc_0097A044;
    local_rdi = (v_stack_m248 + result * 2) + (2);
    if ((*(uint16_t *)(local_rdi)) != 0) goto loc_0097A01D;
    goto loc_00977D75;
loc_0097A061:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (888);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00977BB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
