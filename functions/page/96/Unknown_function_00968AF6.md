# sub_00968AF6

- RVA: `0x00968AF6`–`0x0096AF00` (길이 `9,226` bytes)
- VA: `0x0000000140968AF6`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095218`
- 디코드: `2,278`개 명령, `9,226/9,226` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **139**; 고유 호출 대상: **51**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **51**

### Outgoing calls
- `0x00968B45` → [sub_00967BF0](Unknown_function_00967BF0.md) (function, `0x00967BF0`)
- `0x00968D47` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00968D61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00968D90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00968DD4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00968F17` → [sub_00967A80](Unknown_function_00967A80.md) (function, `0x00967A80`)
- `0x00968F32` → [sub_00967B10](Unknown_function_00967B10.md) (function, `0x00967B10`)
- `0x00968F96` → [sub_00967A50](Unknown_function_00967A50.md) (function, `0x00967A50`)
- `0x00968FC1` → [sub_00967970](Unknown_function_00967970.md) (function, `0x00967970`)
- `0x00968FEB` → [sub_00967890](Unknown_function_00967890.md) (function, `0x00967890`)
- `0x0096900A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00969028` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009690B5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009690F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096911A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00969158` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096917F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00969297` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009692E3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009693FD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009695EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096964B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00969666` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096969B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009696B4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009696E1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009696F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096970C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096971A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00969744` → [SPCallServerHandleQueryPolicy](SPCallServerHandleQueryPolicy_function_0096AF24.md) (function, `0x0096AF24`)
- `0x0096978B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009697CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00969860` → [sub_006FE2A8](../6F/Unknown_function_006FE2A8.md) (function, `0x006FE2A8`)
- `0x009698A4` → [sub_00A0C12C](../A0/Unknown_function_00A0C12C.md) (function, `0x00A0C12C`)
- `0x00969942` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00969950` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x0096995E` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00969975` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096998F` → [RtlCreateAcl](../91/RtlCreateAcl_function_00916F00.md) (function, `0x00916F00`)
- `0x009699BD` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x009699EB` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x00969A19` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x00969A63` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00969AAA` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x00969AB9` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00969ACA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00969AF7` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x00969B1F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969B39` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969B58` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969B82` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969BAC` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969BD4` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969BEC` → `ext-ms-win-ntos-ksecurity-l1-1-1.dll!QueryUpdateFileEaAllowedExt` (import, 간접 대상; import `ext-ms-win-ntos-ksecurity-l1-1-1.dll!QueryUpdateFileEaAllowedExt`)
- `0x00969C32` → [sub_00A0BA74](../A0/Unknown_function_00A0BA74.md) (function, `0x00A0BA74`)
- `0x00969C54` → [sub_00A0B648](../A0/Unknown_function_00A0B648.md) (function, `0x00A0B648`)
- `0x00969CA2` → [sub_00A4991C](../A4/Unknown_function_00A4991C.md) (function, `0x00A4991C`)
- `0x00969CCF` → [sub_00A42ACC](../A4/Unknown_function_00A42ACC.md) (function, `0x00A42ACC`)
- `0x00969D47` → [sub_00A6EDAC](../A6/Unknown_function_00A6EDAC.md) (function, `0x00A6EDAC`)
- `0x00969D87` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969DA9` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969DCB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969DEB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00969E26` → [SPCallServerHandleUpdateLicense](../AA/SPCallServerHandleUpdateLicense_function_00AA4CE0.md) (function, `0x00AA4CE0`)
- `0x00969E53` → [sub_00AD3088](../AD/Unknown_function_00AD3088.md) (function, `0x00AD3088`)
- `0x00969EB2` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00969EC0` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00969ECE` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00969EE5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00969EFF` → [RtlCreateAcl](../91/RtlCreateAcl_function_00916F00.md) (function, `0x00916F00`)
- `0x00969F2D` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x00969F5B` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x00969F89` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x00969FCA` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0096A00E` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0096A01D` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0096A02E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096A05B` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x0096A084` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A0A6` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A0C8` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A0E8` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A102` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A12C` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A156` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A17E` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A1C4` → [SPCallServerHandleUpdatePolicies](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (function, `0x00A815EC`)
- `0x0096A1E9` → [SPCallServerHandleGetAppPolicyValue](../A6/SPCallServerHandleGetAppPolicyValue_function_00A6CCD0.md) (function, `0x00A6CCD0`)
- `0x0096A2D0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096A2E7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096A369` → [SPCallServerHandleCallbackPaintComplete](../AA/SPCallServerHandleCallbackPaintComplete_function_00AA16C4.md) (function, `0x00AA16C4`)
- `0x0096A396` → [sub_0096C058](Unknown_function_0096C058.md) (function, `0x0096C058`)
- `0x0096A3C3` → [sub_00703ECC](../70/Unknown_function_00703ECC.md) (function, `0x00703ECC`)
- `0x0096A3F0` → [sub_00703B14](../70/Unknown_function_00703B14.md) (function, `0x00703B14`)
- `0x0096A41D` → [sub_00AC8AA8](../AC/Unknown_function_00AC8AA8.md) (function, `0x00AC8AA8`)
- `0x0096A44A` → [sub_00AD1D78](../AD/Unknown_function_00AD1D78.md) (function, `0x00AD1D78`)
- `0x0096A477` → [sub_004DD3C8](../../text/4D/Unknown_function_004DD3C8.md) (function, `0x004DD3C8`)
- `0x0096A4BD` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x0096A4E5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A504` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A526` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A546` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A560` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A582` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A5A4` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A5C4` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A5E3` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A605` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A627` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A647` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A661` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A683` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A6A5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A6C5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096A6E7` → [sub_004C4874](../../text/4C/Unknown_function_004C4874.md) (function, `0x004C4874`)
- `0x0096A70C` → [sub_00AD7D60](../AD/Unknown_function_00AD7D60.md) (function, `0x00AD7D60`)
- `0x0096A739` → [sub_00ADAAF4](../AD/Unknown_function_00ADAAF4.md) (function, `0x00ADAAF4`)
- `0x0096A766` → [sub_00703688](../70/Unknown_function_00703688.md) (function, `0x00703688`)
- `0x0096A7A5` → [sub_006FEBA4](../6F/Unknown_function_006FEBA4.md) (function, `0x006FEBA4`)
- `0x0096A7D2` → [sub_00AD34D0](../AD/Unknown_function_00AD34D0.md) (function, `0x00AD34D0`)
- `0x0096A7FF` → [sub_00AD3B00](../AD/Unknown_function_00AD3B00.md) (function, `0x00AD3B00`)
- `0x0096A82C` → [sub_00AD777C](../AD/Unknown_function_00AD777C.md) (function, `0x00AD777C`)
- `0x0096A859` → [sub_006FEE40](../6F/Unknown_function_006FEE40.md) (function, `0x006FEE40`)
- `0x0096A886` → [sub_00AD9930](../AD/Unknown_function_00AD9930.md) (function, `0x00AD9930`)
- `0x0096A8B3` → [sub_006FF210](../6F/Unknown_function_006FF210.md) (function, `0x006FF210`)
- `0x0096A8E0` → [sub_00ADBBE8](../AD/Unknown_function_00ADBBE8.md) (function, `0x00ADBBE8`)
- `0x0096A931` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096A948` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096A96D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096A98B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096AAE5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096AB0F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096AB37` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096AB57` → [RtlUIntAdd](../../text/45/RtlUIntAdd_function_0045D360.md) (function, `0x0045D360`)
- `0x0096AB7C` → [RtlUIntAdd](../../text/45/RtlUIntAdd_function_0045D360.md) (function, `0x0045D360`)
- `0x0096ACB1` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096ACDB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096AD03` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0096ADA0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00968B51` → RVA `0x00967B10` (`PAGE`; read)
- `0x00968B5C` → RVA `0x00967A80` (`PAGE`; read)
- `0x00968EBA` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00968F4E` → RVA `0x00967BF0` (`PAGE`; read)
- `0x00968F75` → RVA `0x00967A50` (`PAGE`; read)
- `0x00968FA0` → RVA `0x00967970` (`PAGE`; read)
- `0x00968FCB` → RVA `0x00967890` (`PAGE`; read)
- `0x00969901` → RVA `0x00FD8458` (`PAGEDATA`; read)
- `0x00969A8D` → RVA `0x00B4B110` (`IopFileMapping`; read)
- `0x00969B12` → RVA `0x00B4FFB0` (`PAGE`; read)
- `0x00969B2F` → RVA `0x00B4FB50` (`PAGE`; read)
- `0x00969B4B` → RVA `0x00B50370` (`PAGE`; read)
- `0x00969B78` → RVA `0x00B4F970` (`PAGE`; read)
- `0x00969BA2` → RVA `0x00B4B2A8` (`PAGE`; read)
- `0x00969BCA` → RVA `0x00B4B2B0` (`PAGE`; read)
- `0x00969BEC` → RVA `0x001512D0` (`ext-ms-win-ntos-ksecurity-l1-1-1.dll!QueryUpdateFileEaAllowedExt (IAT)`; read)
- `0x00969D7D` → RVA `0x00B4FD30` (`PAGE`; read)
- `0x00969D9F` → RVA `0x00B4FBF0` (`PAGE`; read)
- `0x00969DC1` → RVA `0x00B4B2F8` (`PAGE`; read)
- `0x00969DE1` → RVA `0x00B4B288` (`PAGE`; read)
- `0x0096A075` → RVA `0x00B4F790` (`PAGE`; read)
- `0x0096A09C` → RVA `0x00B50190` (`PAGE`; read)
- `0x0096A0BE` → RVA `0x00B4B2E0` (`PAGE`; read)
- `0x0096A0DE` → RVA `0x00B4B280` (`PAGE`; read)
- `0x0096A0F8` → RVA `0x00B4FC90` (`PAGE`; read)
- `0x0096A122` → RVA `0x00B4FA10` (`PAGE`; read)
- `0x0096A14C` → RVA `0x00B4B308` (`PAGE`; read)
- `0x0096A174` → RVA `0x00B4B2D8` (`PAGE`; read)
- `0x0096A4D8` → RVA `0x00B4FDD0` (`PAGE`; read)
- `0x0096A4FA` → RVA `0x00B50050` (`PAGE`; read)
- `0x0096A51C` → RVA `0x00B4B2B8` (`PAGE`; read)
- `0x0096A53C` → RVA `0x00B4B300` (`PAGE`; read)
- `0x0096A556` → RVA `0x00B50230` (`PAGE`; read)
- `0x0096A578` → RVA `0x00B500F0` (`PAGE`; read)
- `0x0096A59A` → RVA `0x00B4B278` (`PAGE`; read)
- `0x0096A5BA` → RVA `0x00B4B2C0` (`PAGE`; read)
- `0x0096A5D6` → RVA `0x00B4F830` (`PAGE`; read)
- `0x0096A5FB` → RVA `0x00B4FE70` (`PAGE`; read)
- `0x0096A61D` → RVA `0x00B4B2D0` (`PAGE`; read)
- `0x0096A63D` → RVA `0x00B4B2F0` (`PAGE`; read)
- `0x0096A657` → RVA `0x00B4FAB0` (`PAGE`; read)
- `0x0096A679` → RVA `0x00B4F8D0` (`PAGE`; read)
- `0x0096A69B` → RVA `0x00B4B310` (`PAGE`; read)
- `0x0096A6BB` → RVA `0x00B4B2C8` (`PAGE`; read)
- `0x0096A961` → RVA `0x00FD8428` (`PAGEDATA`; read)
- `0x0096AADB` → RVA `0x00B4FF10` (`PAGE`; read)
- `0x0096AB05` → RVA `0x00B4B2A0` (`PAGE`; read)
- `0x0096AB2D` → RVA `0x00B4B290` (`PAGE`; read)
- `0x0096ACA7` → RVA `0x00B502D0` (`PAGE`; read)
- `0x0096ACD1` → RVA `0x00B4B298` (`PAGE`; read)
- `0x0096ACF9` → RVA `0x00B4B2E8` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **91**
  - `0x00968D47` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00968D61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00968D90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00968DD4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096900A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00969028` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009690B5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009690F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096911A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00969158` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096917F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00969297` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009692E3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009693FD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009695EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096964B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00969666` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096969B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009696B4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009696E1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009696F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096970C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096971A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096978B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009697CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00969942` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00969950` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x0096995E` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00969975` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00969AAA` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x00969ACA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00969AF7` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
  - `0x00969B1F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969B39` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969B58` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969B82` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969BAC` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969BD4` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969D87` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969DA9` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969DCB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969DEB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00969EB2` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00969EC0` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00969ECE` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00969EE5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096A00E` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0096A02E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096A05B` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
  - `0x0096A084` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A0A6` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A0C8` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A0E8` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A102` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A12C` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A156` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A17E` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A2D0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096A2E7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096A477` → [sub_004DD3C8](../../text/4D/Unknown_function_004DD3C8.md) (`PAGE` → `.text`)
  - `0x0096A4BD` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
  - `0x0096A4E5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A504` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A526` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A546` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A560` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A582` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A5A4` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A5C4` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A5E3` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A605` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A627` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A647` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A661` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A683` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A6A5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A6C5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096A6E7` → [sub_004C4874](../../text/4C/Unknown_function_004C4874.md) (`PAGE` → `.text`)
  - `0x0096A931` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096A948` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096A96D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0096A98B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096AAE5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096AB0F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096AB37` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096AB57` → [RtlUIntAdd](../../text/45/RtlUIntAdd_function_0045D360.md) (`PAGE` → `.text`)
  - `0x0096AB7C` → [RtlUIntAdd](../../text/45/RtlUIntAdd_function_0045D360.md) (`PAGE` → `.text`)
  - `0x0096ACB1` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096ACDB` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096AD03` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0096ADA0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **92**
  - `0x00968AFB` → [sub_00967CA6 + 0x12F](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00968B0B` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00968B1B` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00968B2B` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00968DAA` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969076` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969127` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096913C` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009694EB` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969505` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969597` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009695B2` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009697D9` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009697E4` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009697F6` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096980F` → [sub_00967F18 + 0x84F](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x00969877` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009698C0` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009698D5` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009698F2` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969C70` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969CBE` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969CEB` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969D00` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969D1D` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969D63` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969D75` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969E0D` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969E42` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00969E6F` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A205` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A358` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A385` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A3B2` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A3DF` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A40C` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A439` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A466` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A493` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A728` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A755` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A782` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A794` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A7C1` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A7EE` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A81B` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A848` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A875` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A8A2` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A8CF` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A8FC` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096A9D8` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AA3E` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AAAC` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AAC3` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AB69` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ABA4` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ABB6` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ABC8` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ABD5` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ABF1` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AC03` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AC15` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AC27` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AC76` → [sub_00967F18 + 0x84F](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AC8F` → [sub_00967F18 + 0x84F](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AD1A` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AD2A` → [sub_00967CA6 + 0x12F](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AD3A` → [sub_00967CA6 + 0x12F](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AD44` → [sub_00967CA6 + 0x111](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AD51` → [sub_00967F18 + 0x710](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AD59` → [sub_00967F18 + 0x70B](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AD66` → [sub_00967F18 + 0x710](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AD6E` → [sub_00967F18 + 0x70B](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AD78` → [sub_00967F18 + 0x93E](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096AD88` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ADA5` → [sub_00967F18 + 0x8CF](Unknown_function_00967F18.md) (`tail-transfer`)
  - `0x0096ADC1` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ADDD` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096ADF9` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE0B` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE25` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE3F` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE51` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE63` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE75` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE8E` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AE9D` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AEAC` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AEC6` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AEE2` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096AEFB` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00968AF6  BF 3E 00 00 C0                  mov edi, 0xc000003e
00968AFB  E9 D5 F2 FF FF                  jmp 0x140967dd5
00968B00  BF 0D 00 00 C0                  mov edi, 0xc000000d
00968B05  4D 8B FD                        mov r15, r13
00968B08  49 8B F5                        mov rsi, r13
00968B0B  E9 C8 F2 FF FF                  jmp 0x140967dd8
00968B10  BF 3E 00 00 C0                  mov edi, 0xc000003e
00968B15  4D 8B EF                        mov r13, r15
00968B18  49 8B F7                        mov rsi, r15
00968B1B  E9 B8 F2 FF FF                  jmp 0x140967dd8
00968B20  BF 3E 00 00 C0                  mov edi, 0xc000003e
00968B25  4D 8B EF                        mov r13, r15
00968B28  49 8B F7                        mov rsi, r15
00968B2B  E9 A8 F2 FF FF                  jmp 0x140967dd8
00968B30  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00968B37  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968B3C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968B41  48 8D 4E 01                     lea rcx, [rsi + 1]
00968B45  E8 A6 F0 FF FF                  call 0x140967bf0
00968B4A  44 33 E0                        xor r12d, eax
00968B4D  48 83 C6 02                     add rsi, 2
00968B51  4C 8D 15 B8 EF FF FF            lea r10, [rip - 0x1048]
00968B58  48 83 C7 02                     add rdi, 2
00968B5C  4C 8D 1D 1D EF FF FF            lea r11, [rip - 0x10e3]
00968B63  48 83 C3 08                     add rbx, 8
00968B67  49 83 EF 01                     sub r15, 1
00968B6B  0F 85 5F 03 00 00               jne 0x140968ed0
00968B71  48 8B 85 18 01 00 00            mov rax, qword ptr [rbp + 0x118]
00968B78  41 8B CC                        mov ecx, r12d
00968B7B  44 0F B7 85 1E 01 00 00         movzx r8d, word ptr [rbp + 0x11e]
00968B83  F7 D1                           not ecx
00968B85  44 0F B7 95 1A 01 00 00         movzx r10d, word ptr [rbp + 0x11a]
00968B8D  41 8B D0                        mov edx, r8d
00968B90  8B 9D 1C 01 00 00               mov ebx, dword ptr [rbp + 0x11c]
00968B96  41 8B FC                        mov edi, r12d
00968B99  C1 C9 05                        ror ecx, 5
00968B9C  44 0F B7 D8                     movzx r11d, ax
00968BA0  41 03 CB                        add ecx, r11d
00968BA3  44 0F B7 CB                     movzx r9d, bx
00968BA7  41 0F AF C8                     imul ecx, r8d
00968BAB  44 89 65 88                     mov dword ptr [rbp - 0x78], r12d
00968BAF  44 33 F1                        xor r14d, ecx
00968BB2  41 33 D6                        xor edx, r14d
00968BB5  41 8B CE                        mov ecx, r14d
00968BB8  41 0F AF D2                     imul edx, r10d
00968BBC  C1 E9 0A                        shr ecx, 0xa
00968BBF  33 D1                           xor edx, ecx
00968BC1  33 FA                           xor edi, edx
00968BC3  8B D7                           mov edx, edi
00968BC5  8B CF                           mov ecx, edi
00968BC7  33 D0                           xor edx, eax
00968BC9  C1 C9 0A                        ror ecx, 0xa
00968BCC  C1 CA 0C                        ror edx, 0xc
00968BCF  41 0F AF D1                     imul edx, r9d
00968BD3  33 D1                           xor edx, ecx
00968BD5  44 33 F2                        xor r14d, edx
00968BD8  41 8B D6                        mov edx, r14d
00968BDB  41 8B CE                        mov ecx, r14d
00968BDE  2B D0                           sub edx, eax
00968BE0  C1 C9 18                        ror ecx, 0x18
00968BE3  C1 CA 0E                        ror edx, 0xe
00968BE6  41 0F AF D0                     imul edx, r8d
00968BEA  2B D1                           sub edx, ecx
00968BEC  33 FA                           xor edi, edx
00968BEE  8B CF                           mov ecx, edi
00968BF0  C1 C9 1E                        ror ecx, 0x1e
00968BF3  8D 14 1F                        lea edx, [rdi + rbx]
00968BF6  C1 CA 0F                        ror edx, 0xf
00968BF9  41 0F AF D3                     imul edx, r11d
00968BFD  03 D1                           add edx, ecx
00968BFF  41 8B C9                        mov ecx, r9d
00968C02  44 33 F2                        xor r14d, edx
00968C05  41 33 CE                        xor ecx, r14d
00968C08  41 8B D6                        mov edx, r14d
00968C0B  C1 CA 06                        ror edx, 6
00968C0E  41 0F AF CA                     imul ecx, r10d
00968C12  33 D1                           xor edx, ecx
00968C14  8B CB                           mov ecx, ebx
00968C16  33 FA                           xor edi, edx
00968C18  8B D7                           mov edx, edi
00968C1A  33 D0                           xor edx, eax
00968C1C  2B CA                           sub ecx, edx
00968C1E  41 8B D2                        mov edx, r10d
00968C21  44 33 F1                        xor r14d, ecx
00968C24  41 33 D6                        xor edx, r14d
00968C27  41 8B CE                        mov ecx, r14d
00968C2A  C1 CA 1A                        ror edx, 0x1a
00968C2D  41 0F AF D0                     imul edx, r8d
00968C31  C1 C9 1E                        ror ecx, 0x1e
00968C34  2B D1                           sub edx, ecx
00968C36  33 FA                           xor edi, edx
00968C38  8B D7                           mov edx, edi
00968C3A  8B CF                           mov ecx, edi
00968C3C  41 2B D1                        sub edx, r9d
00968C3F  C1 E9 0D                        shr ecx, 0xd
00968C42  41 0F AF D3                     imul edx, r11d
00968C46  2B D1                           sub edx, ecx
00968C48  44 33 F2                        xor r14d, edx
00968C4B  41 8B CE                        mov ecx, r14d
00968C4E  C1 C9 1E                        ror ecx, 0x1e
00968C51  41 8D 14 1E                     lea edx, [r14 + rbx]
00968C55  C1 CA 09                        ror edx, 9
00968C58  41 0F AF D2                     imul edx, r10d
00968C5C  2B D1                           sub edx, ecx
00968C5E  33 FA                           xor edi, edx
00968C60  8B D7                           mov edx, edi
00968C62  2B D0                           sub edx, eax
00968C64  C1 CA 1B                        ror edx, 0x1b
00968C67  44 8B 65 C8                     mov r12d, dword ptr [rbp - 0x38]
00968C6B  4C 8D 15 9E EE FF FF            lea r10, [rip - 0x1162]
00968C72  44 8B 6D E8                     mov r13d, dword ptr [rbp - 0x18]
00968C76  4C 8D 1D 03 EE FF FF            lea r11, [rip - 0x11fd]
00968C7D  41 0F AF D1                     imul edx, r9d
00968C81  8B CF                           mov ecx, edi
00968C83  4C 8B 4D D8                     mov r9, qword ptr [rbp - 0x28]
00968C87  C1 C9 16                        ror ecx, 0x16
00968C8A  03 D1                           add edx, ecx
00968C8C  44 33 F2                        xor r14d, edx
00968C8F  41 33 FE                        xor edi, r14d
00968C92  44 33 75 A8                     xor r14d, dword ptr [rbp - 0x58]
00968C96  45 88 71 FC                     mov byte ptr [r9 - 4], r14b
00968C9A  33 FB                           xor edi, ebx
00968C9C  33 F8                           xor edi, eax
00968C9E  44 89 65 A8                     mov dword ptr [rbp - 0x58], r12d
00968CA2  33 7D A4                        xor edi, dword ptr [rbp - 0x5c]
00968CA5  41 8B CE                        mov ecx, r14d
00968CA8  41 88 39                        mov byte ptr [r9], dil
00968CAB  8B D7                           mov edx, edi
00968CAD  C1 E1 18                        shl ecx, 0x18
00968CB0  41 8B C6                        mov eax, r14d
00968CB3  C1 E8 08                        shr eax, 8
00968CB6  0B C8                           or ecx, eax
00968CB8  C1 E2 18                        shl edx, 0x18
00968CBB  41 88 49 FB                     mov byte ptr [r9 - 5], cl
00968CBF  44 8B C1                        mov r8d, ecx
00968CC2  41 C1 E0 18                     shl r8d, 0x18
00968CC6  8B C7                           mov eax, edi
00968CC8  C1 E8 08                        shr eax, 8
00968CCB  0B D0                           or edx, eax
00968CCD  C1 E9 08                        shr ecx, 8
00968CD0  41 88 51 FF                     mov byte ptr [r9 - 1], dl
00968CD4  44 0B C1                        or r8d, ecx
00968CD7  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00968CDB  8B C2                           mov eax, edx
00968CDD  45 88 41 FA                     mov byte ptr [r9 - 6], r8b
00968CE1  C1 E0 18                        shl eax, 0x18
00968CE4  C1 EA 08                        shr edx, 8
00968CE7  0B C2                           or eax, edx
00968CE9  41 C1 C8 08                     ror r8d, 8
00968CED  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
00968CF1  41 88 41 FE                     mov byte ptr [r9 - 2], al
00968CF5  C1 C8 08                        ror eax, 8
00968CF8  45 88 41 F9                     mov byte ptr [r9 - 7], r8b
00968CFC  41 88 41 FD                     mov byte ptr [r9 - 3], al
00968D00  49 83 C1 08                     add r9, 8
00968D04  48 83 6D C0 01                  sub qword ptr [rbp - 0x40], 1
00968D09  44 89 6D A4                     mov dword ptr [rbp - 0x5c], r13d
00968D0D  4C 89 4D D8                     mov qword ptr [rbp - 0x28], r9
00968D11  0F 85 3C 01 00 00               jne 0x140968e53
00968D17  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00968D1B  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
00968D1F  4C 8B 6D D0                     mov r13, qword ptr [rbp - 0x30]
00968D23  0F B6 45 A0                     movzx eax, byte ptr [rbp - 0x60]
00968D27  33 FF                           xor edi, edi
00968D29  49 89 04 1C                     mov qword ptr [r12 + rbx], rax
00968D2D  45 85 ED                        test r13d, r13d
00968D30  0F 84 85 04 00 00               je 0x1409691bb
00968D36  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00968D3C  41 8B D5                        mov edx, r13d
00968D3F  B9 00 01 00 00                  mov ecx, 0x100
00968D44  41 8B F5                        mov esi, r13d
00968D47  E8 A4 93 21 00                  call 0x140b820f0
00968D4C  48 8B D8                        mov rbx, rax
00968D4F  48 85 C0                        test rax, rax
00968D52  0F 84 DA 02 00 00               je 0x140969032
00968D58  44 8B C6                        mov r8d, esi
00968D5B  49 8B D4                        mov rdx, r12
00968D5E  48 8B C8                        mov rcx, rax
00968D61  E8 DA DA D5 FF                  call 0x1406c6840
00968D66  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00968D6B  48 89 58 08                     mov qword ptr [rax + 8], rbx
00968D6F  44 89 28                        mov dword ptr [rax], r13d
00968D72  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00968D77  33 D2                           xor edx, edx
00968D79  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00968D7E  49 8B CC                        mov rcx, r12
00968D81  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00968D86  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00968D8B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00968D90  E8 DB 9A 21 00                  call 0x140b82870
00968D95  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00968D9A  4D 8B C6                        mov r8, r14
00968D9D  85 FF                           test edi, edi
00968D9F  0F 89 97 02 00 00               jns 0x14096903c
00968DA5  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00968DAA  E9 29 F0 FF FF                  jmp 0x140967dd8
00968DAF  40 88 75 A0                     mov byte ptr [rbp - 0x60], sil
00968DB3  4D 8D 68 08                     lea r13, [r8 + 8]
00968DB7  B9 00 01 00 00                  mov ecx, 0x100
00968DBC  48 8D 87 80 00 00 00            lea rax, [rdi + 0x80]
00968DC3  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
00968DC7  49 8B D5                        mov rdx, r13
00968DCA  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00968DCE  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00968DD4  E8 17 93 21 00                  call 0x140b820f0
00968DD9  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00968DDD  4C 8B E0                        mov r12, rax
00968DE0  48 85 C0                        test rax, rax
00968DE3  0F 84 FE 20 00 00               je 0x14096aee7
00968DE9  45 33 F6                        xor r14d, r14d
00968DEC  48 89 9D 18 01 00 00            mov qword ptr [rbp + 0x118], rbx
00968DF3  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00968DF7  49 8B F7                        mov rsi, r15
00968DFA  83 E3 07                        and ebx, 7
00968DFD  48 89 45 08                     mov qword ptr [rbp + 8], rax
00968E01  48 89 5D B0                     mov qword ptr [rbp - 0x50], rbx
00968E05  4C 8B F8                        mov r15, rax
00968E08  44 89 75 A4                     mov dword ptr [rbp - 0x5c], r14d
00968E0C  44 89 75 A8                     mov dword ptr [rbp - 0x58], r14d
00968E10  0F 85 AF 03 00 00               jne 0x1409691c5
00968E16  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00968E1A  48 8B C3                        mov rax, rbx
00968E1D  48 C1 E8 03                     shr rax, 3
00968E21  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00968E25  48 85 C0                        test rax, rax
00968E28  0F 84 F5 FE FF FF               je 0x140968d23
00968E2E  48 8D 57 02                     lea rdx, [rdi + 2]
00968E32  49 83 C7 07                     add r15, 7
00968E36  8B 7D 88                        mov edi, dword ptr [rbp - 0x78]
00968E39  48 8D 4E 02                     lea rcx, [rsi + 2]
00968E3D  48 89 55 08                     mov qword ptr [rbp + 8], rdx
00968E41  4C 8D 15 C8 EC FF FF            lea r10, [rip - 0x1338]
00968E48  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00968E4C  4C 8D 1D 2D EC FF FF            lea r11, [rip - 0x13d3]
00968E53  0F B6 41 FF                     movzx eax, byte ptr [rcx - 1]
00968E57  48 8B DA                        mov rbx, rdx
00968E5A  44 0F B6 69 02                  movzx r13d, byte ptr [rcx + 2]
00968E5F  44 0F B6 61 FE                  movzx r12d, byte ptr [rcx - 2]
00968E64  41 C1 E4 08                     shl r12d, 8
00968E68  44 0B E0                        or r12d, eax
00968E6B  41 C1 E5 08                     shl r13d, 8
00968E6F  0F B6 01                        movzx eax, byte ptr [rcx]
00968E72  41 C1 E4 08                     shl r12d, 8
00968E76  44 0B E0                        or r12d, eax
00968E79  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00968E7D  41 C1 E4 08                     shl r12d, 8
00968E81  44 0B E0                        or r12d, eax
00968E84  0F B6 41 03                     movzx eax, byte ptr [rcx + 3]
00968E88  44 0B E8                        or r13d, eax
00968E8B  44 89 65 C8                     mov dword ptr [rbp - 0x38], r12d
00968E8F  0F B6 41 04                     movzx eax, byte ptr [rcx + 4]
00968E93  45 33 F4                        xor r14d, r12d
00968E96  41 C1 E5 08                     shl r13d, 8
00968E9A  44 0B E8                        or r13d, eax
00968E9D  0F B6 41 05                     movzx eax, byte ptr [rcx + 5]
00968EA1  41 C1 E5 08                     shl r13d, 8
00968EA5  48 83 C1 08                     add rcx, 8
00968EA9  44 0B E8                        or r13d, eax
00968EAC  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
00968EB0  41 33 FD                        xor edi, r13d
00968EB3  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
00968EB7  89 7D 88                        mov dword ptr [rbp - 0x78], edi
00968EBA  4C 8D 2D 3F 71 69 FF            lea r13, [rip - 0x968ec1]
00968EC1  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
00968EC5  33 F6                           xor esi, esi
00968EC7  44 8B 65 88                     mov r12d, dword ptr [rbp - 0x78]
00968ECB  44 8D 7E 10                     lea r15d, [rsi + 0x10]
00968ECF  90                              nop
00968ED0  0F B6 07                        movzx eax, byte ptr [rdi]
00968ED3  3C 1F                           cmp al, 0x1f
00968ED5  73 63                           jae 0x140968f3a
00968ED7  49 8B 84 C5 C0 84 FD 00         mov rax, qword ptr [r13 + rax*8 + 0xfd84c0]
00968EDF  0F B6 4B 01                     movzx ecx, byte ptr [rbx + 1]
00968EE3  44 0F B6 0B                     movzx r9d, byte ptr [rbx]
00968EE7  44 0F B6 43 FF                  movzx r8d, byte ptr [rbx - 1]
00968EEC  0F B6 53 FE                     movzx edx, byte ptr [rbx - 2]
00968EF0  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00968EF5  49 3B C2                        cmp rax, r10
00968EF8  74 24                           je 0x140968f1e
00968EFA  49 3B C3                        cmp rax, r11
00968EFD  0F 85 C8 00 00 00               jne 0x140968fcb
00968F03  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00968F0A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968F0F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968F14  48 8B CE                        mov rcx, rsi
00968F17  E8 64 EB FF FF                  call 0x140967a80
00968F1C  EB 19                           jmp 0x140968f37
00968F1E  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00968F25  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968F2A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968F2F  48 8B CE                        mov rcx, rsi
00968F32  E8 D9 EB FF FF                  call 0x140967b10
00968F37  44 33 F0                        xor r14d, eax
00968F3A  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
00968F3E  3C 1F                           cmp al, 0x1f
00968F40  0F 83 07 FC FF FF               jae 0x140968b4d
00968F46  49 8B 84 C5 C0 84 FD 00         mov rax, qword ptr [r13 + rax*8 + 0xfd84c0]
00968F4E  4C 8D 1D 9B EC FF FF            lea r11, [rip - 0x1365]
00968F55  0F B6 4B 05                     movzx ecx, byte ptr [rbx + 5]
00968F59  44 0F B6 4B 04                  movzx r9d, byte ptr [rbx + 4]
00968F5E  44 0F B6 43 03                  movzx r8d, byte ptr [rbx + 3]
00968F63  0F B6 53 02                     movzx edx, byte ptr [rbx + 2]
00968F67  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00968F6C  49 3B C3                        cmp rax, r11
00968F6F  0F 84 BB FB FF FF               je 0x140968b30
00968F75  4C 8D 1D D4 EA FF FF            lea r11, [rip - 0x152c]
00968F7C  49 3B C3                        cmp rax, r11
00968F7F  75 1F                           jne 0x140968fa0
00968F81  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00968F88  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968F8D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968F92  48 8D 4E 01                     lea rcx, [rsi + 1]
00968F96  E8 B5 EA FF FF                  call 0x140967a50
00968F9B  E9 AA FB FF FF                  jmp 0x140968b4a
00968FA0  4C 8D 1D C9 E9 FF FF            lea r11, [rip - 0x1637]
00968FA7  49 3B C3                        cmp rax, r11
00968FAA  75 49                           jne 0x140968ff5
00968FAC  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00968FB3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968FB8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968FBD  48 8D 4E 01                     lea rcx, [rsi + 1]
00968FC1  E8 AA E9 FF FF                  call 0x140967970
00968FC6  E9 7F FB FF FF                  jmp 0x140968b4a
00968FCB  4C 8D 15 BE E8 FF FF            lea r10, [rip - 0x1742]
00968FD2  49 3B C2                        cmp rax, r10
00968FD5  75 3D                           jne 0x140969014
00968FD7  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00968FDE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968FE3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968FE8  48 8B CE                        mov rcx, rsi
00968FEB  E8 A0 E8 FF FF                  call 0x140967890
00968FF0  E9 42 FF FF FF                  jmp 0x140968f37
00968FF5  4C 8D 9D 18 01 00 00            lea r11, [rbp + 0x118]
00968FFC  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
00969001  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00969006  48 8D 4E 01                     lea rcx, [rsi + 1]
0096900A  E8 C1 1A D5 FF                  call 0x1406baad0
0096900F  E9 36 FB FF FF                  jmp 0x140968b4a
00969014  4C 8D 95 18 01 00 00            lea r10, [rbp + 0x118]
0096901B  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
00969020  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00969025  48 8B CE                        mov rcx, rsi
00969028  E8 A3 1A D5 FF                  call 0x1406baad0
0096902D  E9 05 FF FF FF                  jmp 0x140968f37
00969032  BF 17 00 00 C0                  mov edi, 0xc0000017
00969037  E9 36 FD FF FF                  jmp 0x140968d72
0096903C  41 8B 45 00                     mov eax, dword ptr [r13]
00969040  4D 8D 75 20                     lea r14, [r13 + 0x20]
00969044  41 8B 1E                        mov ebx, dword ptr [r14]
00969047  49 8D 75 10                     lea rsi, [r13 + 0x10]
0096904B  44 8B 1E                        mov r11d, dword ptr [rsi]
0096904E  83 C0 04                        add eax, 4
00969051  83 F8 04                        cmp eax, 4
00969054  72 13                           jb 0x140969069
00969056  44 8D 50 04                     lea r10d, [rax + 4]
0096905A  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
0096905F  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00969064  44 3B D0                        cmp r10d, eax
00969067  73 12                           jae 0x14096907b
00969069  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096906E  BF 95 00 00 C0                  mov edi, 0xc0000095
00969073  4D 8B F0                        mov r14, r8
00969076  E9 5D ED FF FF                  jmp 0x140967dd8
0096907B  43 8D 0C 1A                     lea ecx, [r10 + r11]
0096907F  41 3B CA                        cmp ecx, r10d
00969082  72 E5                           jb 0x140969069
00969084  8D 41 04                        lea eax, [rcx + 4]
00969087  3B C1                           cmp eax, ecx
00969089  72 DE                           jb 0x140969069
0096908B  03 D8                           add ebx, eax
0096908D  3B D8                           cmp ebx, eax
0096908F  72 D8                           jb 0x140969069
00969091  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00969096  4D 8B FD                        mov r15, r13
00969099  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
0096909D  4D 8B E8                        mov r13, r8
009690A0  85 DB                           test ebx, ebx
009690A2  0F 84 09 1E 00 00               je 0x14096aeb1
009690A8  8B D3                           mov edx, ebx
009690AA  B9 00 01 00 00                  mov ecx, 0x100
009690AF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
009690B5  E8 36 90 21 00                  call 0x140b820f0
009690BA  48 85 C0                        test rax, rax
009690BD  0F 84 08 1E 00 00               je 0x14096aecb
009690C3  48 8B C8                        mov rcx, rax
009690C6  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
009690CB  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009690D0  41 8B 07                        mov eax, dword ptr [r15]
009690D3  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009690D8  48 8D 79 04                     lea rdi, [rcx + 4]
009690DC  89 01                           mov dword ptr [rcx], eax
009690DE  48 3B F9                        cmp rdi, rcx
009690E1  0F 82 BB 00 00 00               jb 0x1409691a2
009690E7  45 8B 07                        mov r8d, dword ptr [r15]
009690EA  48 8B CF                        mov rcx, rdi
009690ED  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009690F1  4D 8B EF                        mov r13, r15
009690F4  E8 47 D7 D5 FF                  call 0x1406c6840
009690F9  41 8B 0F                        mov ecx, dword ptr [r15]
009690FC  48 03 CF                        add rcx, rdi
009690FF  48 3B CF                        cmp rcx, rdi
00969102  73 3D                           jae 0x140969141
00969104  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00969109  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096910E  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969113  33 D2                           xor edx, edx
00969115  BF 95 00 00 C0                  mov edi, 0xc0000095
0096911A  E8 51 97 21 00                  call 0x140b82870
0096911F  48 8B 75 58                     mov rsi, qword ptr [rbp + 0x58]
00969123  33 DB                           xor ebx, ebx
00969125  85 FF                           test edi, edi
00969127  0F 88 AB EC FF FF               js 0x140967dd8
0096912D  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00969131  48 89 30                        mov qword ptr [rax], rsi
00969134  33 F6                           xor esi, esi
00969136  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0096913A  89 18                           mov dword ptr [rax], ebx
0096913C  E9 97 EC FF FF                  jmp 0x140967dd8
00969141  8B 06                           mov eax, dword ptr [rsi]
00969143  48 8D 79 04                     lea rdi, [rcx + 4]
00969147  89 01                           mov dword ptr [rcx], eax
00969149  48 3B F9                        cmp rdi, rcx
0096914C  72 B6                           jb 0x140969104
0096914E  44 8B 06                        mov r8d, dword ptr [rsi]
00969151  48 8B CF                        mov rcx, rdi
00969154  49 8B 57 18                     mov rdx, qword ptr [r15 + 0x18]
00969158  E8 E3 D6 D5 FF                  call 0x1406c6840
0096915D  8B 0E                           mov ecx, dword ptr [rsi]
0096915F  48 03 CF                        add rcx, rdi
00969162  48 3B CF                        cmp rcx, rdi
00969165  72 9D                           jb 0x140969104
00969167  41 8B 06                        mov eax, dword ptr [r14]
0096916A  48 8D 79 04                     lea rdi, [rcx + 4]
0096916E  89 01                           mov dword ptr [rcx], eax
00969170  48 3B F9                        cmp rdi, rcx
00969173  72 8F                           jb 0x140969104
00969175  45 8B 06                        mov r8d, dword ptr [r14]
00969178  48 8B CF                        mov rcx, rdi
0096917B  49 8B 57 28                     mov rdx, qword ptr [r15 + 0x28]
0096917F  E8 BC D6 D5 FF                  call 0x1406c6840
00969184  41 8B 06                        mov eax, dword ptr [r14]
00969187  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096918C  48 03 C7                        add rax, rdi
0096918F  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969194  48 3B C7                        cmp rax, rdi
00969197  72 18                           jb 0x1409691b1
00969199  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096919E  33 FF                           xor edi, edi
009691A0  EB 8B                           jmp 0x14096912d
009691A2  4D 8B F5                        mov r14, r13
009691A5  4D 8B EF                        mov r13, r15
009691A8  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
009691AC  E9 62 FF FF FF                  jmp 0x140969113
009691B1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009691B6  E9 58 FF FF FF                  jmp 0x140969113
009691BB  BF 3E 00 00 C0                  mov edi, 0xc000003e
009691C0  E9 AD FB FF FF                  jmp 0x140968d72
009691C5  45 33 C0                        xor r8d, r8d
009691C8  45 33 C9                        xor r9d, r9d
009691CB  33 D2                           xor edx, edx
009691CD  44 89 45 A4                     mov dword ptr [rbp - 0x5c], r8d
009691D1  44 89 4D A8                     mov dword ptr [rbp - 0x58], r9d
009691D5  85 DB                           test ebx, ebx
009691D7  74 58                           je 0x140969231
009691D9  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
009691DE  45 8D 68 38                     lea r13d, [r8 + 0x38]
009691E2  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
009691E7  48 8B FE                        mov rdi, rsi
009691EA  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
009691EF  0F B6 06                        movzx eax, byte ptr [rsi]
009691F2  48 FF C6                        inc rsi
009691F5  83 FA 04                        cmp edx, 4
009691F8  0F 83 AD 01 00 00               jae 0x1409693ab
009691FE  41 8D 4D E0                     lea ecx, [r13 - 0x20]
00969202  D3 E0                           shl eax, cl
00969204  44 0B C8                        or r9d, eax
00969207  FF C2                           inc edx
00969209  41 83 ED 08                     sub r13d, 8
0096920D  3B D3                           cmp edx, ebx
0096920F  7C DE                           jl 0x1409691ef
00969211  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00969216  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
0096921A  44 89 4D A8                     mov dword ptr [rbp - 0x58], r9d
0096921E  44 89 45 A4                     mov dword ptr [rbp - 0x5c], r8d
00969222  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
00969227  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0096922C  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00969231  B9 10 00 00 00                  mov ecx, 0x10
00969236  4C 8D AF 9E 00 00 00            lea r13, [rdi + 0x9e]
0096923D  4C 8D 67 7E                     lea r12, [rdi + 0x7e]
00969241  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00969245  BF FF FF FF FF                  mov edi, 0xffffffff
0096924A  48 8D 1D AF 6D 69 FF            lea rbx, [rip - 0x969251]
00969251  44 8D 79 0E                     lea r15d, [rcx + 0xe]
00969255  41 0F B6 45 01                  movzx eax, byte ptr [r13 + 1]
0096925A  3C 1F                           cmp al, 0x1f
0096925C  73 44                           jae 0x1409692a2
0096925E  45 0F B6 54 24 01               movzx r10d, byte ptr [r12 + 1]
00969264  4C 8D 9D 18 01 00 00            lea r11, [rbp + 0x118]
0096926B  48 8B 84 C3 C0 84 FD 00         mov rax, qword ptr [rbx + rax*8 + 0xfd84c0]
00969273  49 8D 4F 01                     lea rcx, [r15 + 1]
00969277  45 0F B6 0C 24                  movzx r9d, byte ptr [r12]
0096927C  45 0F B6 44 24 FF               movzx r8d, byte ptr [r12 - 1]
00969282  41 0F B6 54 24 FE               movzx edx, byte ptr [r12 - 2]
00969288  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0096928D  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
00969292  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00969297  E8 34 18 D5 FF                  call 0x1406baad0
0096929C  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
009692A0  33 F8                           xor edi, eax
009692A2  41 0F B6 45 00                  movzx eax, byte ptr [r13]
009692A7  3C 1F                           cmp al, 0x1f
009692A9  73 44                           jae 0x1409692ef
009692AB  41 0F B6 4C 24 FD               movzx ecx, byte ptr [r12 - 3]
009692B1  4C 8D 95 18 01 00 00            lea r10, [rbp + 0x118]
009692B8  48 8B 84 C3 C0 84 FD 00         mov rax, qword ptr [rbx + rax*8 + 0xfd84c0]
009692C0  45 0F B6 4C 24 FC               movzx r9d, byte ptr [r12 - 4]
009692C6  45 0F B6 44 24 FB               movzx r8d, byte ptr [r12 - 5]
009692CC  41 0F B6 54 24 FA               movzx edx, byte ptr [r12 - 6]
009692D2  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009692D6  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
009692DB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009692E0  49 8B CF                        mov rcx, r15
009692E3  E8 E8 17 D5 FF                  call 0x1406baad0
009692E8  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
009692EC  44 33 F0                        xor r14d, eax
009692EF  49 83 EF 02                     sub r15, 2
009692F3  49 83 ED 02                     sub r13, 2
009692F7  49 83 EC 08                     sub r12, 8
009692FB  48 83 E9 01                     sub rcx, 1
009692FF  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00969303  0F 85 4C FF FF FF               jne 0x140969255
00969309  44 33 75 A8                     xor r14d, dword ptr [rbp - 0x58]
0096930D  8B C7                           mov eax, edi
0096930F  33 45 A4                        xor eax, dword ptr [rbp - 0x5c]
00969312  45 33 C9                        xor r9d, r9d
00969315  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
00969319  41 8B D6                        mov edx, r14d
0096931C  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
00969320  44 8B C0                        mov r8d, eax
00969323  89 7D 88                        mov dword ptr [rbp - 0x78], edi
00969326  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
0096932A  89 45 88                        mov dword ptr [rbp - 0x78], eax
0096932D  85 DB                           test ebx, ebx
0096932F  74 57                           je 0x140969388
00969331  4C 8B 5C 24 70                  mov r11, qword ptr [rsp + 0x70]
00969336  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
0096933B  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00969340  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00969345  4D 8D 57 01                     lea r10, [r15 + 1]
00969349  41 83 F9 04                     cmp r9d, 4
0096934D  73 69                           jae 0x1409693b8
0096934F  8B CA                           mov ecx, edx
00969351  8B C2                           mov eax, edx
00969353  C1 E9 18                        shr ecx, 0x18
00969356  C1 E0 08                        shl eax, 8
00969359  8B D1                           mov edx, ecx
0096935B  0B D0                           or edx, eax
0096935D  8B C2                           mov eax, edx
0096935F  41 FF C1                        inc r9d
00969362  41 88 07                        mov byte ptr [r15], al
00969365  4D 8B FA                        mov r15, r10
00969368  44 3B CB                        cmp r9d, ebx
0096936B  7C D8                           jl 0x140969345
0096936D  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
00969370  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00969375  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
00969379  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
0096937E  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
00969383  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00969388  83 FB 04                        cmp ebx, 4
0096938B  76 42                           jbe 0x1409693cf
0096938D  B9 08 00 00 00                  mov ecx, 8
00969392  2B CB                           sub ecx, ebx
00969394  C1 E1 03                        shl ecx, 3
00969397  D3 E8                           shr eax, cl
00969399  D3 E0                           shl eax, cl
0096939B  89 45 88                        mov dword ptr [rbp - 0x78], eax
0096939E  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
009693A2  4C 8B 6D D0                     mov r13, qword ptr [rbp - 0x30]
009693A6  E9 6B FA FF FF                  jmp 0x140968e16
009693AB  41 8B CD                        mov ecx, r13d
009693AE  D3 E0                           shl eax, cl
009693B0  44 0B C0                        or r8d, eax
009693B3  E9 4F FE FF FF                  jmp 0x140969207
009693B8  41 8B C8                        mov ecx, r8d
009693BB  41 8B C0                        mov eax, r8d
009693BE  C1 E9 18                        shr ecx, 0x18
009693C1  C1 E0 08                        shl eax, 8
009693C4  44 8B C1                        mov r8d, ecx
009693C7  44 0B C0                        or r8d, eax
009693CA  41 8B C0                        mov eax, r8d
009693CD  EB 90                           jmp 0x14096935f
009693CF  C7 45 88 00 00 00 00            mov dword ptr [rbp - 0x78], 0
009693D6  73 C6                           jae 0x14096939e
009693D8  B8 04 00 00 00                  mov eax, 4
009693DD  2B C3                           sub eax, ebx
009693DF  C1 E0 03                        shl eax, 3
009693E2  8B C8                           mov ecx, eax
009693E4  41 D3 EE                        shr r14d, cl
009693E7  41 D3 E6                        shl r14d, cl
009693EA  EB B2                           jmp 0x14096939e
009693EC  4A 89 7C 03 F8                  mov qword ptr [rbx + r8 - 8], rdi
009693F1  4D 8B F8                        mov r15, r8
009693F4  44 8B 44 24 7C                  mov r8d, dword ptr [rsp + 0x7c]
009693F9  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
009693FD  E8 3E D4 D5 FF                  call 0x1406c6840
00969402  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
00969406  48 85 D2                        test rdx, rdx
00969409  0F 84 6B 1A 00 00               je 0x14096ae7a
0096940F  41 8B 4D 20                     mov ecx, dword ptr [r13 + 0x20]
00969413  85 C9                           test ecx, ecx
00969415  0F 84 69 1A 00 00               je 0x14096ae84
0096941B  49 8B 7D 18                     mov rdi, qword ptr [r13 + 0x18]
0096941F  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
00969423  48 85 FF                        test rdi, rdi
00969426  0F 84 67 1A 00 00               je 0x14096ae93
0096942C  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00969430  85 C0                           test eax, eax
00969432  0F 84 6A 1A 00 00               je 0x14096aea2
00969438  44 8B C3                        mov r8d, ebx
0096943B  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
0096943F  83 F9 08                        cmp ecx, 8
00969442  0F 85 A9 1A 00 00               jne 0x14096aef1
00969448  3D A0 00 00 00                  cmp eax, 0xa0
0096944D  0F 85 9E 1A 00 00               jne 0x14096aef1
00969453  48 8B 1A                        mov rbx, qword ptr [rdx]
00969456  33 C0                           xor eax, eax
00969458  C6 45 A0 00                     mov byte ptr [rbp - 0x60], 0
0096945C  4D 85 C0                        test r8, r8
0096945F  0F 84 4E F9 FF FF               je 0x140968db3
00969465  40 32 F6                        xor sil, sil
00969468  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00969470  42 32 34 38                     xor sil, byte ptr [rax + r15]
00969474  48 FF C0                        inc rax
00969477  49 3B C0                        cmp rax, r8
0096947A  72 F4                           jb 0x140969470
0096947C  E9 2E F9 FF FF                  jmp 0x140968daf
00969481  33 F6                           xor esi, esi
00969483  85 D2                           test edx, edx
00969485  48 0F 45 F1                     cmovne rsi, rcx
00969489  83 FA 04                        cmp edx, 4
0096948C  0F 85 6B 09 00 00               jne 0x140969dfd
00969492  48 83 7D 98 00                  cmp qword ptr [rbp - 0x68], 0
00969497  8B 36                           mov esi, dword ptr [rsi]
00969499  0F 84 51 08 00 00               je 0x140969cf0
0096949F  41 83 FF 01                     cmp r15d, 1
009694A3  0F 86 1C 04 00 00               jbe 0x1409698c5
009694A9  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
009694AD  45 33 C9                        xor r9d, r9d
009694B0  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
009694B5  48 8D 48 04                     lea rcx, [rax + 4]
009694B9  4D 8B C6                        mov r8, r14
009694BC  44 8B 30                        mov r14d, dword ptr [rax]
009694BF  41 83 F9 01                     cmp r9d, 1
009694C3  73 4A                           jae 0x14096950f
009694C5  48 3B C8                        cmp rcx, rax
009694C8  72 26                           jb 0x1409694f0
009694CA  4A 8D 04 31                     lea rax, [rcx + r14]
009694CE  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
009694D3  4D 8B F0                        mov r14, r8
009694D6  48 3B C1                        cmp rax, rcx
009694D9  73 2F                           jae 0x14096950a
009694DB  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009694E0  BF 95 00 00 C0                  mov edi, 0xc0000095
009694E5  4D 8B FD                        mov r15, r13
009694E8  49 8B F5                        mov rsi, r13
009694EB  E9 E8 E8 FF FF                  jmp 0x140967dd8
009694F0  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009694F5  BF 95 00 00 C0                  mov edi, 0xc0000095
009694FA  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009694FF  4D 8B FD                        mov r15, r13
00969502  49 8B F5                        mov rsi, r13
00969505  E9 CE E8 FF FF                  jmp 0x140967dd8
0096950A  41 FF C1                        inc r9d
0096950D  EB A6                           jmp 0x1409694b5
0096950F  48 3B C8                        cmp rcx, rax
00969512  72 DC                           jb 0x1409694f0
00969514  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
00969519  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
0096951E  45 33 E4                        xor r12d, r12d
00969521  45 85 F6                        test r14d, r14d
00969524  4C 0F 45 E1                     cmovne r12, rcx
00969528  48 83 7D 98 00                  cmp qword ptr [rbp - 0x68], 0
0096952D  0F 84 D2 07 00 00               je 0x140969d05
00969533  41 83 FF 02                     cmp r15d, 2
00969537  0F 86 9D 03 00 00               jbe 0x1409698da
0096953D  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
00969542  45 33 C9                        xor r9d, r9d
00969545  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00969549  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0096954E  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
00969553  44 8B 38                        mov r15d, dword ptr [rax]
00969556  48 8D 48 04                     lea rcx, [rax + 4]
0096955A  41 83 F9 02                     cmp r9d, 2
0096955E  73 57                           jae 0x1409695b7
00969560  48 3B C8                        cmp rcx, rax
00969563  72 18                           jb 0x14096957d
00969565  4A 8D 04 39                     lea rax, [rcx + r15]
00969569  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0096956E  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
00969573  48 3B C1                        cmp rax, rcx
00969576  72 24                           jb 0x14096959c
00969578  41 FF C1                        inc r9d
0096957B  EB D6                           jmp 0x140969553
0096957D  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00969582  BF 95 00 00 C0                  mov edi, 0xc0000095
00969587  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096958C  4D 8B FD                        mov r15, r13
0096958F  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00969594  49 8B F5                        mov rsi, r13
00969597  E9 3C E8 FF FF                  jmp 0x140967dd8
0096959C  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009695A1  BF 95 00 00 C0                  mov edi, 0xc0000095
009695A6  4D 8B FD                        mov r15, r13
009695A9  49 8B F5                        mov rsi, r13
009695AC  4D 8B F3                        mov r14, r11
009695AF  4D 8B E2                        mov r12, r10
009695B2  E9 21 E8 FF FF                  jmp 0x140967dd8
009695B7  48 3B C8                        cmp rcx, rax
009695BA  0F 82 3B 02 00 00               jb 0x1409697fb
009695C0  45 33 ED                        xor r13d, r13d
009695C3  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
009695C8  45 85 FF                        test r15d, r15d
009695CB  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
009695D0  BA 30 00 00 00                  mov edx, 0x30
009695D5  4C 89 55 C0                     mov qword ptr [rbp - 0x40], r10
009695D9  4C 0F 45 E9                     cmovne r13, rcx
009695DD  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
009695E1  B9 00 01 00 00                  mov ecx, 0x100
009695E6  41 B8 53 4C 53 20               mov r8d, 0x20534c53
009695EC  E8 FF 8A 21 00                  call 0x140b820f0
009695F1  48 8B D8                        mov rbx, rax
009695F4  48 85 C0                        test rax, rax
009695F7  0F 84 AD 17 00 00               je 0x14096adaa
009695FD  0F 57 C0                        xorps xmm0, xmm0
00969600  0F 11 00                        movups xmmword ptr [rax], xmm0
00969603  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
00969607  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
0096960B  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0096960F  33 D2                           xor edx, edx
00969611  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00969615  33 FF                           xor edi, edi
00969617  89 13                           mov dword ptr [rbx], edx
00969619  48 89 53 08                     mov qword ptr [rbx + 8], rdx
0096961D  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00969622  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00969627  4D 85 E4                        test r12, r12
0096962A  0F 84 0A 02 00 00               je 0x14096983a
00969630  44 89 73 10                     mov dword ptr [rbx + 0x10], r14d
00969634  45 85 F6                        test r14d, r14d
00969637  0F 84 38 06 00 00               je 0x140969c75
0096963D  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00969643  49 8B D6                        mov rdx, r14
00969646  B9 00 01 00 00                  mov ecx, 0x100
0096964B  E8 A0 8A 21 00                  call 0x140b820f0
00969650  48 85 C0                        test rax, rax
00969653  0F 84 CF 01 00 00               je 0x140969828
00969659  4D 8B C6                        mov r8, r14
0096965C  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00969660  49 8B D4                        mov rdx, r12
00969663  48 8B C8                        mov rcx, rax
00969666  E8 D5 D1 D5 FF                  call 0x1406c6840
0096966B  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00969670  33 D2                           xor edx, edx
00969672  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969677  4D 85 ED                        test r13, r13
0096967A  0F 84 0A 06 00 00               je 0x140969c8a
00969680  44 89 7B 20                     mov dword ptr [rbx + 0x20], r15d
00969684  45 85 FF                        test r15d, r15d
00969687  0F 84 6A 02 00 00               je 0x1409698f7
0096968D  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00969693  49 8B D7                        mov rdx, r15
00969696  B9 00 01 00 00                  mov ecx, 0x100
0096969B  E8 50 8A 21 00                  call 0x140b820f0
009696A0  48 85 C0                        test rax, rax
009696A3  74 23                           je 0x1409696c8
009696A5  33 FF                           xor edi, edi
009696A7  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
009696AB  4D 8B C7                        mov r8, r15
009696AE  49 8B D5                        mov rdx, r13
009696B1  48 8B C8                        mov rcx, rax
009696B4  E8 87 D1 D5 FF                  call 0x1406c6840
009696B9  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009696BE  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
009696C3  4C 8B EB                        mov r13, rbx
009696C6  EB 5C                           jmp 0x140969724
009696C8  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009696CD  BF 17 00 00 C0                  mov edi, 0xc0000017
009696D2  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
009696D6  48 85 C9                        test rcx, rcx
009696D9  0F 84 33 07 00 00               je 0x140969e12
009696DF  33 D2                           xor edx, edx
009696E1  E8 8A 91 21 00                  call 0x140b82870
009696E6  45 33 FF                        xor r15d, r15d
009696E9  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
009696ED  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
009696F1  48 85 C9                        test rcx, rcx
009696F4  74 0B                           je 0x140969701
009696F6  33 D2                           xor edx, edx
009696F8  E8 73 91 21 00                  call 0x140b82870
009696FD  4C 89 7B 18                     mov qword ptr [rbx + 0x18], r15
00969701  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00969705  48 85 C9                        test rcx, rcx
00969708  74 0B                           je 0x140969715
0096970A  33 D2                           xor edx, edx
0096970C  E8 5F 91 21 00                  call 0x140b82870
00969711  4C 89 7B 28                     mov qword ptr [rbx + 0x28], r15
00969715  33 D2                           xor edx, edx
00969717  48 8B CB                        mov rcx, rbx
0096971A  E8 51 91 21 00                  call 0x140b82870
0096971F  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00969724  85 FF                           test edi, edi
00969726  0F 88 8A 13 00 00               js 0x14096aab6
0096972C  85 F6                           test esi, esi
0096972E  0F 85 1D 01 00 00               jne 0x140969851
00969734  44 8B 45 E0                     mov r8d, dword ptr [rbp - 0x20]
00969738  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096973D  49 8B D5                        mov rdx, r13
00969740  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969744  E8 DB 17 00 00                  call 0x14096af24
00969749  8B F8                           mov edi, eax
0096974B  85 C0                           test eax, eax
0096974D  0F 88 1C 01 00 00               js 0x14096986f
00969753  0F 31                           rdtsc
00969755  48 C1 E2 20                     shl rdx, 0x20
00969759  48 0B C2                        or rax, rdx
0096975C  48 8B F8                        mov rdi, rax
0096975F  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
00969763  83 C1 08                        add ecx, 8
00969766  83 F9 08                        cmp ecx, 8
00969769  72 7E                           jb 0x1409697e9
0096976B  48 8D 59 07                     lea rbx, [rcx + 7]
0096976F  83 E3 F8                        and ebx, 0xfffffff8
00969772  3B D9                           cmp ebx, ecx
00969774  72 73                           jb 0x1409697e9
00969776  85 DB                           test ebx, ebx
00969778  0F 84 D8 16 00 00               je 0x14096ae56
0096977E  8B D3                           mov edx, ebx
00969780  B9 00 01 00 00                  mov ecx, 0x100
00969785  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096978B  E8 60 89 21 00                  call 0x140b820f0
00969790  48 85 C0                        test rax, rax
00969793  0F 84 CF 16 00 00               je 0x14096ae68
00969799  4C 8B C0                        mov r8, rax
0096979C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009697A1  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009697A5  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
009697AA  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
009697AF  49 8D 50 04                     lea rdx, [r8 + 4]
009697B3  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
009697B8  41 89 00                        mov dword ptr [r8], eax
009697BB  49 3B D0                        cmp rdx, r8
009697BE  73 54                           jae 0x140969814
009697C0  33 D2                           xor edx, edx
009697C2  49 8B C8                        mov rcx, r8
009697C5  BF 95 00 00 C0                  mov edi, 0xc0000095
009697CA  E8 A1 90 21 00                  call 0x140b82870
009697CF  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
009697D3  33 DB                           xor ebx, ebx
009697D5  8B F3                           mov esi, ebx
009697D7  85 FF                           test edi, edi
009697D9  0F 88 F9 E5 FF FF               js 0x140967dd8
009697DF  BF 0D 00 00 C0                  mov edi, 0xc000000d
009697E4  E9 EF E5 FF FF                  jmp 0x140967dd8
009697E9  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
009697EE  BF 95 00 00 C0                  mov edi, 0xc0000095
009697F3  49 8B F7                        mov rsi, r15
009697F6  E9 DD E5 FF FF                  jmp 0x140967dd8
009697FB  BF 95 00 00 C0                  mov edi, 0xc0000095
00969800  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00969805  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096980A  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096980F  E9 53 EF FF FF                  jmp 0x140968767
00969814  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00969818  48 8D 4A 04                     lea rcx, [rdx + 4]
0096981C  89 02                           mov dword ptr [rdx], eax
0096981E  48 3B CA                        cmp rcx, rdx
00969821  72 9D                           jb 0x1409697c0
00969823  E9 C4 FB FF FF                  jmp 0x1409693ec
00969828  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
0096982C  4C 8B 65 C0                     mov r12, qword ptr [rbp - 0x40]
00969830  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00969835  E9 93 FE FF FF                  jmp 0x1409696cd
0096983A  89 53 10                        mov dword ptr [rbx + 0x10], edx
0096983D  4C 8B F1                        mov r14, rcx
00969840  48 89 53 18                     mov qword ptr [rbx + 0x18], rdx
00969844  4C 8B E0                        mov r12, rax
00969847  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0096984C  E9 26 FE FF FF                  jmp 0x140969677
00969851  FF CE                           dec esi
00969853  81 FE D3 00 00 00               cmp esi, 0xd3
00969859  76 21                           jbe 0x14096987c
0096985B  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00969860  E8 43 4A D9 FF                  call 0x1406fe2a8
00969865  8B F8                           mov edi, eax
00969867  85 C0                           test eax, eax
00969869  0F 89 E4 FE FF FF               jns 0x140969753
0096986F  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969874  49 8B F7                        mov rsi, r15
00969877  E9 5C E5 FF FF                  jmp 0x140967dd8
0096987C  48 8D 15 7D 67 69 FF            lea rdx, [rip - 0x969883]
00969883  0F B6 84 32 98 34 04 00         movzx eax, byte ptr [rdx + rsi + 0x43498]
0096988B  8B 8C 82 18 34 04 00            mov ecx, dword ptr [rdx + rax*4 + 0x43418]
00969892  48 03 CA                        add rcx, rdx
00969895  FF E1                           jmp rcx
00969897  CC                              int3
00969898  CC                              int3
00969899  CC                              int3
0096989A  CC                              int3
0096989B  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
009698A0  48 8D 4D 90                     lea rcx, [rbp - 0x70]
009698A4  E8 83 28 0A 00                  call 0x140a0c12c
009698A9  8B F8                           mov edi, eax
009698AB  85 C0                           test eax, eax
009698AD  0F 89 A0 FE FF FF               jns 0x140969753
009698B3  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
009698B8  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009698BD  49 8B F7                        mov rsi, r15
009698C0  E9 13 E5 FF FF                  jmp 0x140967dd8
009698C5  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009698CA  BF 0D 00 00 C0                  mov edi, 0xc000000d
009698CF  4D 8B FD                        mov r15, r13
009698D2  49 8B F5                        mov rsi, r13
009698D5  E9 FE E4 FF FF                  jmp 0x140967dd8
009698DA  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009698DF  BF 0D 00 00 C0                  mov edi, 0xc000000d
009698E4  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
009698E9  4D 8B FD                        mov r15, r13
009698EC  49 8B F5                        mov rsi, r13
009698EF  4D 8B F3                        mov r14, r11
009698F2  E9 E1 E4 FF FF                  jmp 0x140967dd8
009698F7  BF 3E 00 00 C0                  mov edi, 0xc000003e
009698FC  E9 D1 FD FF FF                  jmp 0x1409696d2
00969901  4C 8B 35 50 EB 66 00            mov r14, qword ptr [rip + 0x66eb50]
00969908  0F 57 C0                        xorps xmm0, xmm0
0096990B  33 C0                           xor eax, eax
0096990D  45 33 FF                        xor r15d, r15d
00969910  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
00969917  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
0096991E  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
00969925  44 89 7D 28                     mov dword ptr [rbp + 0x28], r15d
00969929  0F 11 85 E8 00 00 00            movups xmmword ptr [rbp + 0xe8], xmm0
00969930  44 89 7D 00                     mov dword ptr [rbp], r15d
00969934  0F 11 85 F8 00 00 00            movups xmmword ptr [rbp + 0xf8], xmm0
0096993B  49 8B 8E 88 01 00 00            mov rcx, qword ptr [r14 + 0x188]
00969942  E8 29 39 AF FF                  call 0x14045d270
00969947  49 8B 8E 80 01 00 00            mov rcx, qword ptr [r14 + 0x180]
0096994E  8B D8                           mov ebx, eax
00969950  E8 1B 39 AF FF                  call 0x14045d270
00969955  49 8B 8E 10 01 00 00            mov rcx, qword ptr [r14 + 0x110]
0096995C  03 D8                           add ebx, eax
0096995E  E8 0D 39 AF FF                  call 0x14045d270
00969963  83 C0 20                        add eax, 0x20
00969966  B9 00 01 00 00                  mov ecx, 0x100
0096996B  03 D8                           add ebx, eax
0096996D  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00969973  8B D3                           mov edx, ebx
00969975  E8 76 87 21 00                  call 0x140b820f0
0096997A  48 8B F0                        mov rsi, rax
0096997D  48 85 C0                        test rax, rax
00969980  0F 84 4A 14 00 00               je 0x14096add0
00969986  45 8D 47 02                     lea r8d, [r15 + 2]
0096998A  8B D3                           mov edx, ebx
0096998C  48 8B C8                        mov rcx, rax
0096998F  E8 6C D5 FA FF                  call 0x140916f00
00969994  8B F8                           mov edi, eax
00969996  85 C0                           test eax, eax
00969998  0F 88 27 01 00 00               js 0x140969ac5
0096999E  49 8B 86 80 01 00 00            mov rax, qword ptr [r14 + 0x180]
009699A5  45 8D 4F 20                     lea r9d, [r15 + 0x20]
009699A9  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
009699AE  41 8D 57 02                     lea edx, [r15 + 2]
009699B2  45 33 C0                        xor r8d, r8d
009699B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009699BA  48 8B CE                        mov rcx, rsi
009699BD  E8 5E 00 FC FF                  call 0x140929a20
009699C2  8B F8                           mov edi, eax
009699C4  85 C0                           test eax, eax
009699C6  0F 88 F9 00 00 00               js 0x140969ac5
009699CC  49 8B 86 88 01 00 00            mov rax, qword ptr [r14 + 0x188]
009699D3  45 8D 4F 20                     lea r9d, [r15 + 0x20]
009699D7  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
009699DC  41 8D 57 02                     lea edx, [r15 + 2]
009699E0  45 33 C0                        xor r8d, r8d
009699E3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009699E8  48 8B CE                        mov rcx, rsi
009699EB  E8 30 00 FC FF                  call 0x140929a20
009699F0  8B F8                           mov edi, eax
009699F2  85 C0                           test eax, eax
009699F4  0F 88 CB 00 00 00               js 0x140969ac5
009699FA  49 8B 86 10 01 00 00            mov rax, qword ptr [r14 + 0x110]
00969A01  45 8D 4F 20                     lea r9d, [r15 + 0x20]
00969A05  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
00969A0A  41 8D 57 02                     lea edx, [r15 + 2]
00969A0E  45 33 C0                        xor r8d, r8d
00969A11  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00969A16  48 8B CE                        mov rcx, rsi
00969A19  E8 02 00 FC FF                  call 0x140929a20
00969A1E  8B F8                           mov edi, eax
00969A20  85 C0                           test eax, eax
00969A22  0F 88 9D 00 00 00               js 0x140969ac5
00969A28  0F B7 85 A2 00 00 00            movzx eax, word ptr [rbp + 0xa2]
00969A2F  C6 85 A0 00 00 00 01            mov byte ptr [rbp + 0xa0], 1
00969A36  66 85 C0                        test ax, ax
00969A39  0F 88 A3 13 00 00               js 0x14096ade2
00969A3F  B9 F7 FF 00 00                  mov ecx, 0xfff7
00969A44  48 89 B5 C0 00 00 00            mov qword ptr [rbp + 0xc0], rsi
00969A4B  66 23 C1                        and ax, cx
00969A4E  41 8B FF                        mov edi, r15d
00969A51  66 83 C8 04                     or ax, 4
00969A55  48 8D 8D E8 00 00 00            lea rcx, [rbp + 0xe8]
00969A5C  66 89 85 A2 00 00 00            mov word ptr [rbp + 0xa2], ax
00969A63  E8 B8 1D F0 FF                  call 0x14086b820
00969A68  48 8D 45 00                     lea rax, [rbp]
00969A6C  45 33 C0                        xor r8d, r8d
00969A6F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00969A74  45 8D 4F 20                     lea r9d, [r15 + 0x20]
00969A78  48 8D 45 28                     lea rax, [rbp + 0x28]
00969A7C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00969A81  48 8D 95 E8 00 00 00            lea rdx, [rbp + 0xe8]
00969A88  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
00969A8D  48 8D 05 7C 16 1E 00            lea rax, [rip + 0x1e167c]
00969A94  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00969A99  48 8D 8D A0 00 00 00            lea rcx, [rbp + 0xa0]
00969AA0  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00969AA5  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00969AAA  E8 11 D1 A3 FF                  call 0x1403a6bc0
00969AAF  48 8D 8D E8 00 00 00            lea rcx, [rbp + 0xe8]
00969AB6  0F B6 D8                        movzx ebx, al
00969AB9  E8 52 1C F0 FF                  call 0x14086b710
00969ABE  84 DB                           test bl, bl
00969AC0  75 03                           jne 0x140969ac5
00969AC2  8B 7D 00                        mov edi, dword ptr [rbp]
00969AC5  33 D2                           xor edx, edx
00969AC7  48 8B CE                        mov rcx, rsi
00969ACA  E8 A1 8D 21 00                  call 0x140b82870
00969ACF  85 FF                           test edi, edi
00969AD1  0F 88 DF 0F 00 00               js 0x14096aab6
00969AD7  33 C0                           xor eax, eax
00969AD9  44 89 7D 2C                     mov dword ptr [rbp + 0x2c], r15d
00969ADD  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00969AE1  4C 8D 4D 2C                     lea r9, [rbp + 0x2c]
00969AE5  B8 08 00 00 00                  mov eax, 8
00969AEA  48 8D 55 48                     lea rdx, [rbp + 0x48]
00969AEE  44 8B C0                        mov r8d, eax
00969AF1  89 45 48                        mov dword ptr [rbp + 0x48], eax
00969AF4  8D 48 5F                        lea ecx, [rax + 0x5f]
00969AF7  E8 94 3C D4 FF                  call 0x1406ad790
00969AFC  41 8B 5C 24 10                  mov ebx, dword ptr [r12 + 0x10]
00969B01  81 FB A0 00 00 00               cmp ebx, 0xa0
00969B07  0F 85 5B 02 00 00               jne 0x140969d68
00969B0D  49 8B 74 24 18                  mov rsi, qword ptr [r12 + 0x18]
00969B12  48 8D 0D 97 64 1E 00            lea rcx, [rip + 0x1e6497]
00969B19  48 8B D6                        mov rdx, rsi
00969B1C  44 8B C3                        mov r8d, ebx
00969B1F  E8 EC CF D5 FF                  call 0x1406c6b10
00969B24  85 C0                           test eax, eax
00969B26  0F 84 9C 0F 00 00               je 0x14096aac8
00969B2C  4C 8B C3                        mov r8, rbx
00969B2F  48 8D 0D 1A 60 1E 00            lea rcx, [rip + 0x1e601a]
00969B36  48 8B D6                        mov rdx, rsi
00969B39  E8 D2 CF D5 FF                  call 0x1406c6b10
00969B3E  85 C0                           test eax, eax
00969B40  0F 84 4E 11 00 00               je 0x14096ac94
00969B46  49 8B 7C 24 18                  mov rdi, qword ptr [r12 + 0x18]
00969B4B  48 8D 0D 1E 68 1E 00            lea rcx, [rip + 0x1e681e]
00969B52  48 8B D7                        mov rdx, rdi
00969B55  4C 8B C3                        mov r8, rbx
00969B58  E8 B3 CF D5 FF                  call 0x1406c6b10
00969B5D  85 C0                           test eax, eax
00969B5F  0F 85 15 02 00 00               jne 0x140969d7a
00969B65  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00969B69  3D A0 00 00 00                  cmp eax, 0xa0
00969B6E  0F 85 06 02 00 00               jne 0x140969d7a
00969B74  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
00969B78  48 8D 0D F1 5D 1E 00            lea rcx, [rip + 0x1e5df1]
00969B7F  44 8B C0                        mov r8d, eax
00969B82  E8 89 CF D5 FF                  call 0x1406c6b10
00969B87  85 C0                           test eax, eax
00969B89  0F 85 EB 01 00 00               jne 0x140969d7a
00969B8F  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
00969B94  83 F8 08                        cmp eax, 8
00969B97  0F 85 DD 01 00 00               jne 0x140969d7a
00969B9D  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
00969BA2  48 8D 0D FF 16 1E 00            lea rcx, [rip + 0x1e16ff]
00969BA9  44 8B C0                        mov r8d, eax
00969BAC  E8 5F CF D5 FF                  call 0x1406c6b10
00969BB1  85 C0                           test eax, eax
00969BB3  0F 85 C1 01 00 00               jne 0x140969d7a
00969BB9  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00969BBD  83 F8 08                        cmp eax, 8
00969BC0  0F 85 B4 01 00 00               jne 0x140969d7a
00969BC6  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
00969BCA  48 8D 0D DF 16 1E 00            lea rcx, [rip + 0x1e16df]
00969BD1  44 8B C0                        mov r8d, eax
00969BD4  E8 37 CF D5 FF                  call 0x1406c6b10
00969BD9  85 C0                           test eax, eax
00969BDB  0F 85 99 01 00 00               jne 0x140969d7a
00969BE1  48 8D 4D 04                     lea rcx, [rbp + 4]
00969BE5  44 89 7D 04                     mov dword ptr [rbp + 4], r15d
00969BE9  41 8B FF                        mov edi, r15d
00969BEC  48 FF 15 DD 76 7E FF            call qword ptr [rip - 0x818923]
00969BF3  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00969BF8  3D BB 00 00 C0                  cmp eax, 0xc00000bb
00969BFD  0F 85 1F 01 00 00               jne 0x140969d22
00969C03  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00969C0C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00969C13  F6 81 FA 05 00 00 07            test byte ptr [rcx + 0x5fa], 7
00969C1A  77 05                           ja 0x140969c21
00969C1C  BF 05 00 07 80                  mov edi, 0x80070005
00969C21  85 FF                           test edi, edi
00969C23  0F 88 8D 0E 00 00               js 0x14096aab6
00969C29  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969C2E  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969C32  E8 3D 1E 0A 00                  call 0x140a0ba74
00969C37  8B F8                           mov edi, eax
00969C39  85 C0                           test eax, eax
00969C3B  0F 88 75 0E 00 00               js 0x14096aab6
00969C41  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969C46  E9 08 FB FF FF                  jmp 0x140969753
00969C4B  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969C50  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969C54  E8 EF 19 0A 00                  call 0x140a0b648
00969C59  8B F8                           mov edi, eax
00969C5B  85 C0                           test eax, eax
00969C5D  0F 89 F0 FA FF FF               jns 0x140969753
00969C63  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969C68  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969C6D  49 8B F7                        mov rsi, r15
00969C70  E9 63 E1 FF FF                  jmp 0x140967dd8
00969C75  BF 3E 00 00 C0                  mov edi, 0xc000003e
00969C7A  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00969C7F  4C 8B F1                        mov r14, rcx
00969C82  4C 8B E0                        mov r12, rax
00969C85  E9 48 FA FF FF                  jmp 0x1409696d2
00969C8A  89 53 20                        mov dword ptr [rbx + 0x20], edx
00969C8D  48 89 53 28                     mov qword ptr [rbx + 0x28], rdx
00969C91  E9 2D FA FF FF                  jmp 0x1409696c3
00969C96  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969C9B  49 8B D5                        mov rdx, r13
00969C9E  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969CA2  E8 75 FC 0D 00                  call 0x140a4991c
00969CA7  8B F8                           mov edi, eax
00969CA9  85 C0                           test eax, eax
00969CAB  0F 89 A2 FA FF FF               jns 0x140969753
00969CB1  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969CB6  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969CBB  49 8B F7                        mov rsi, r15
00969CBE  E9 15 E1 FF FF                  jmp 0x140967dd8
00969CC3  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969CC8  49 8B D5                        mov rdx, r13
00969CCB  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969CCF  E8 F8 8D 0D 00                  call 0x140a42acc
00969CD4  8B F8                           mov edi, eax
00969CD6  85 C0                           test eax, eax
00969CD8  0F 89 75 FA FF FF               jns 0x140969753
00969CDE  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969CE3  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969CE8  49 8B F7                        mov rsi, r15
00969CEB  E9 E8 E0 FF FF                  jmp 0x140967dd8
00969CF0  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00969CF5  BF 0D 00 00 C0                  mov edi, 0xc000000d
00969CFA  4D 8B FD                        mov r15, r13
00969CFD  49 8B F5                        mov rsi, r13
00969D00  E9 D3 E0 FF FF                  jmp 0x140967dd8
00969D05  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00969D0A  BF 0D 00 00 C0                  mov edi, 0xc000000d
00969D0F  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00969D14  4D 8B FD                        mov r15, r13
00969D17  49 8B F5                        mov rsi, r13
00969D1A  4D 8B F3                        mov r14, r11
00969D1D  E9 B6 E0 FF FF                  jmp 0x140967dd8
00969D22  8B F8                           mov edi, eax
00969D24  85 C0                           test eax, eax
00969D26  0F 88 F5 FE FF FF               js 0x140969c21
00969D2C  83 7D 04 01                     cmp dword ptr [rbp + 4], 1
00969D30  0F 84 EB FE FF FF               je 0x140969c21
00969D36  E9 C8 FE FF FF                  jmp 0x140969c03
00969D3B  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969D40  49 8B D5                        mov rdx, r13
00969D43  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969D47  E8 60 50 10 00                  call 0x140a6edac
00969D4C  8B F8                           mov edi, eax
00969D4E  85 C0                           test eax, eax
00969D50  0F 89 FD F9 FF FF               jns 0x140969753
00969D56  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969D5B  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969D60  49 8B F7                        mov rsi, r15
00969D63  E9 70 E0 FF FF                  jmp 0x140967dd8
00969D68  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969D6D  BF 05 00 07 80                  mov edi, 0x80070005
00969D72  49 8B F7                        mov rsi, r15
00969D75  E9 5E E0 FF FF                  jmp 0x140967dd8
00969D7A  4C 8B C3                        mov r8, rbx
00969D7D  48 8D 0D AC 5F 1E 00            lea rcx, [rip + 0x1e5fac]
00969D84  48 8B D7                        mov rdx, rdi
00969D87  E8 84 CD D5 FF                  call 0x1406c6b10
00969D8C  85 C0                           test eax, eax
00969D8E  75 D8                           jne 0x140969d68
00969D90  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00969D94  3D A0 00 00 00                  cmp eax, 0xa0
00969D99  75 CD                           jne 0x140969d68
00969D9B  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
00969D9F  48 8D 0D 4A 5E 1E 00            lea rcx, [rip + 0x1e5e4a]
00969DA6  44 8B C0                        mov r8d, eax
00969DA9  E8 62 CD D5 FF                  call 0x1406c6b10
00969DAE  85 C0                           test eax, eax
00969DB0  75 B6                           jne 0x140969d68
00969DB2  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
00969DB7  83 F8 08                        cmp eax, 8
00969DBA  75 AC                           jne 0x140969d68
00969DBC  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
00969DC1  48 8D 0D 30 15 1E 00            lea rcx, [rip + 0x1e1530]
00969DC8  44 8B C0                        mov r8d, eax
00969DCB  E8 40 CD D5 FF                  call 0x1406c6b10
00969DD0  85 C0                           test eax, eax
00969DD2  75 94                           jne 0x140969d68
00969DD4  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00969DD8  83 F8 08                        cmp eax, 8
00969DDB  75 8B                           jne 0x140969d68
00969DDD  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
00969DE1  48 8D 0D A0 14 1E 00            lea rcx, [rip + 0x1e14a0]
00969DE8  44 8B C0                        mov r8d, eax
00969DEB  E8 20 CD D5 FF                  call 0x1406c6b10
00969DF0  85 C0                           test eax, eax
00969DF2  0F 85 70 FF FF FF               jne 0x140969d68
00969DF8  E9 E4 FD FF FF                  jmp 0x140969be1
00969DFD  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00969E02  BF 23 00 00 C0                  mov edi, 0xc0000023
00969E07  4D 8B FD                        mov r15, r13
00969E0A  49 8B F5                        mov rsi, r13
00969E0D  E9 C6 DF FF FF                  jmp 0x140967dd8
00969E12  45 33 FF                        xor r15d, r15d
00969E15  E9 D3 F8 FF FF                  jmp 0x1409696ed
00969E1A  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969E1F  49 8B D5                        mov rdx, r13
00969E22  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969E26  E8 B5 AE 13 00                  call 0x140aa4ce0
00969E2B  8B F8                           mov edi, eax
00969E2D  85 C0                           test eax, eax
00969E2F  0F 89 1E F9 FF FF               jns 0x140969753
00969E35  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969E3A  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969E3F  49 8B F7                        mov rsi, r15
00969E42  E9 91 DF FF FF                  jmp 0x140967dd8
00969E47  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00969E4C  49 8B D5                        mov rdx, r13
00969E4F  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00969E53  E8 30 92 16 00                  call 0x140ad3088
00969E58  8B F8                           mov edi, eax
00969E5A  85 C0                           test eax, eax
00969E5C  0F 89 F1 F8 FF FF               jns 0x140969753
00969E62  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00969E67  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00969E6C  49 8B F7                        mov rsi, r15
00969E6F  E9 64 DF FF FF                  jmp 0x140967dd8
00969E74  4C 8B 35 DD E5 66 00            mov r14, qword ptr [rip + 0x66e5dd]
00969E7B  0F 57 C0                        xorps xmm0, xmm0
00969E7E  33 C0                           xor eax, eax
00969E80  45 33 FF                        xor r15d, r15d
00969E83  0F 11 45 78                     movups xmmword ptr [rbp + 0x78], xmm0
00969E87  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
00969E8E  0F 11 85 88 00 00 00            movups xmmword ptr [rbp + 0x88], xmm0
00969E95  44 89 7D 20                     mov dword ptr [rbp + 0x20], r15d
00969E99  0F 11 85 C8 00 00 00            movups xmmword ptr [rbp + 0xc8], xmm0
00969EA0  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00969EA4  0F 11 85 D8 00 00 00            movups xmmword ptr [rbp + 0xd8], xmm0
00969EAB  49 8B 8E 80 01 00 00            mov rcx, qword ptr [r14 + 0x180]
00969EB2  E8 B9 33 AF FF                  call 0x14045d270
00969EB7  49 8B 8E 10 01 00 00            mov rcx, qword ptr [r14 + 0x110]
00969EBE  8B D8                           mov ebx, eax
00969EC0  E8 AB 33 AF FF                  call 0x14045d270
00969EC5  49 8B 8E 88 01 00 00            mov rcx, qword ptr [r14 + 0x188]
00969ECC  03 D8                           add ebx, eax
00969ECE  E8 9D 33 AF FF                  call 0x14045d270
00969ED3  83 C0 20                        add eax, 0x20
00969ED6  B9 00 01 00 00                  mov ecx, 0x100
00969EDB  03 D8                           add ebx, eax
00969EDD  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00969EE3  8B D3                           mov edx, ebx
00969EE5  E8 06 82 21 00                  call 0x140b820f0
00969EEA  48 8B F0                        mov rsi, rax
00969EED  48 85 C0                        test rax, rax
00969EF0  0F 84 BE 0E 00 00               je 0x14096adb4
00969EF6  45 8D 47 02                     lea r8d, [r15 + 2]
00969EFA  8B D3                           mov edx, ebx
00969EFC  48 8B C8                        mov rcx, rax
00969EFF  E8 FC CF FA FF                  call 0x140916f00
00969F04  8B F8                           mov edi, eax
00969F06  85 C0                           test eax, eax
00969F08  0F 88 1B 01 00 00               js 0x14096a029
00969F0E  49 8B 86 80 01 00 00            mov rax, qword ptr [r14 + 0x180]
00969F15  45 8D 4F 20                     lea r9d, [r15 + 0x20]
00969F19  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
00969F1E  41 8D 57 02                     lea edx, [r15 + 2]
00969F22  45 33 C0                        xor r8d, r8d
00969F25  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00969F2A  48 8B CE                        mov rcx, rsi
00969F2D  E8 EE FA FB FF                  call 0x140929a20
00969F32  8B F8                           mov edi, eax
00969F34  85 C0                           test eax, eax
00969F36  0F 88 ED 00 00 00               js 0x14096a029
00969F3C  49 8B 86 88 01 00 00            mov rax, qword ptr [r14 + 0x188]
00969F43  45 8D 4F 20                     lea r9d, [r15 + 0x20]
00969F47  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
00969F4C  41 8D 57 02                     lea edx, [r15 + 2]
00969F50  45 33 C0                        xor r8d, r8d
00969F53  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00969F58  48 8B CE                        mov rcx, rsi
00969F5B  E8 C0 FA FB FF                  call 0x140929a20
00969F60  8B F8                           mov edi, eax
00969F62  85 C0                           test eax, eax
00969F64  0F 88 BF 00 00 00               js 0x14096a029
00969F6A  49 8B 86 10 01 00 00            mov rax, qword ptr [r14 + 0x110]
00969F71  45 8D 4F 20                     lea r9d, [r15 + 0x20]
00969F75  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
00969F7A  41 8D 57 02                     lea edx, [r15 + 2]
00969F7E  45 33 C0                        xor r8d, r8d
00969F81  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00969F86  48 8B CE                        mov rcx, rsi
00969F89  E8 92 FA FB FF                  call 0x140929a20
00969F8E  8B F8                           mov edi, eax
00969F90  85 C0                           test eax, eax
00969F92  0F 88 91 00 00 00               js 0x14096a029
00969F98  0F B7 45 7A                     movzx eax, word ptr [rbp + 0x7a]
00969F9C  C6 45 78 01                     mov byte ptr [rbp + 0x78], 1
00969FA0  66 85 C0                        test ax, ax
00969FA3  0F 88 1D 0E 00 00               js 0x14096adc6
00969FA9  B9 F7 FF 00 00                  mov ecx, 0xfff7
00969FAE  48 89 B5 98 00 00 00            mov qword ptr [rbp + 0x98], rsi
00969FB5  66 23 C1                        and ax, cx
00969FB8  41 8B FF                        mov edi, r15d
00969FBB  66 83 C8 04                     or ax, 4
00969FBF  48 8D 8D C8 00 00 00            lea rcx, [rbp + 0xc8]
00969FC6  66 89 45 7A                     mov word ptr [rbp + 0x7a], ax
00969FCA  E8 51 18 F0 FF                  call 0x14086b820
00969FCF  48 8D 45 10                     lea rax, [rbp + 0x10]
00969FD3  45 33 C0                        xor r8d, r8d
00969FD6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00969FDB  45 8D 4F 20                     lea r9d, [r15 + 0x20]
00969FDF  48 8D 45 20                     lea rax, [rbp + 0x20]
00969FE3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00969FE8  48 8D 95 C8 00 00 00            lea rdx, [rbp + 0xc8]
00969FEF  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
00969FF4  48 8D 05 15 11 1E 00            lea rax, [rip + 0x1e1115]
00969FFB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0096A000  48 8D 4D 78                     lea rcx, [rbp + 0x78]
0096A004  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0096A009  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
0096A00E  E8 AD CB A3 FF                  call 0x1403a6bc0
0096A013  48 8D 8D C8 00 00 00            lea rcx, [rbp + 0xc8]
0096A01A  0F B6 D8                        movzx ebx, al
0096A01D  E8 EE 16 F0 FF                  call 0x14086b710
0096A022  84 DB                           test bl, bl
0096A024  75 03                           jne 0x14096a029
0096A026  8B 7D 10                        mov edi, dword ptr [rbp + 0x10]
0096A029  33 D2                           xor edx, edx
0096A02B  48 8B CE                        mov rcx, rsi
0096A02E  E8 3D 88 21 00                  call 0x140b82870
0096A033  85 FF                           test edi, edi
0096A035  0F 88 7B 0A 00 00               js 0x14096aab6
0096A03B  33 C0                           xor eax, eax
0096A03D  44 89 7D 24                     mov dword ptr [rbp + 0x24], r15d
0096A041  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0096A045  4C 8D 4D 24                     lea r9, [rbp + 0x24]
0096A049  B8 08 00 00 00                  mov eax, 8
0096A04E  48 8D 55 40                     lea rdx, [rbp + 0x40]
0096A052  44 8B C0                        mov r8d, eax
0096A055  89 45 40                        mov dword ptr [rbp + 0x40], eax
0096A058  8D 48 5F                        lea ecx, [rax + 0x5f]
0096A05B  E8 30 37 D4 FF                  call 0x1406ad790
0096A060  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
0096A065  3D A0 00 00 00                  cmp eax, 0xa0
0096A06A  0F 85 F8 FC FF FF               jne 0x140969d68
0096A070  49 8B 7C 24 18                  mov rdi, qword ptr [r12 + 0x18]
0096A075  48 8D 0D 14 57 1E 00            lea rcx, [rip + 0x1e5714]
0096A07C  48 8B D7                        mov rdx, rdi
0096A07F  44 8B C0                        mov r8d, eax
0096A082  8B D8                           mov ebx, eax
0096A084  E8 87 CA D5 FF                  call 0x1406c6b10
0096A089  85 C0                           test eax, eax
0096A08B  75 68                           jne 0x14096a0f5
0096A08D  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096A091  3D A0 00 00 00                  cmp eax, 0xa0
0096A096  75 5D                           jne 0x14096a0f5
0096A098  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096A09C  48 8D 0D ED 60 1E 00            lea rcx, [rip + 0x1e60ed]
0096A0A3  44 8B C0                        mov r8d, eax
0096A0A6  E8 65 CA D5 FF                  call 0x1406c6b10
0096A0AB  85 C0                           test eax, eax
0096A0AD  75 46                           jne 0x14096a0f5
0096A0AF  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096A0B4  83 F8 08                        cmp eax, 8
0096A0B7  75 3C                           jne 0x14096a0f5
0096A0B9  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096A0BE  48 8D 0D 1B 12 1E 00            lea rcx, [rip + 0x1e121b]
0096A0C5  44 8B C0                        mov r8d, eax
0096A0C8  E8 43 CA D5 FF                  call 0x1406c6b10
0096A0CD  85 C0                           test eax, eax
0096A0CF  75 24                           jne 0x14096a0f5
0096A0D1  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096A0D5  83 F8 08                        cmp eax, 8
0096A0D8  75 1B                           jne 0x14096a0f5
0096A0DA  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096A0DE  48 8D 0D 9B 11 1E 00            lea rcx, [rip + 0x1e119b]
0096A0E5  44 8B C0                        mov r8d, eax
0096A0E8  E8 23 CA D5 FF                  call 0x1406c6b10
0096A0ED  85 C0                           test eax, eax
0096A0EF  0F 84 96 00 00 00               je 0x14096a18b
0096A0F5  4C 8B C3                        mov r8, rbx
0096A0F8  48 8D 0D 91 5B 1E 00            lea rcx, [rip + 0x1e5b91]
0096A0FF  48 8B D7                        mov rdx, rdi
0096A102  E8 09 CA D5 FF                  call 0x1406c6b10
0096A107  85 C0                           test eax, eax
0096A109  0F 85 59 FC FF FF               jne 0x140969d68
0096A10F  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096A113  3D A0 00 00 00                  cmp eax, 0xa0
0096A118  0F 85 4A FC FF FF               jne 0x140969d68
0096A11E  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096A122  48 8D 0D E7 58 1E 00            lea rcx, [rip + 0x1e58e7]
0096A129  44 8B C0                        mov r8d, eax
0096A12C  E8 DF C9 D5 FF                  call 0x1406c6b10
0096A131  85 C0                           test eax, eax
0096A133  0F 85 2F FC FF FF               jne 0x140969d68
0096A139  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096A13E  83 F8 08                        cmp eax, 8
0096A141  0F 85 21 FC FF FF               jne 0x140969d68
0096A147  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096A14C  48 8D 0D B5 11 1E 00            lea rcx, [rip + 0x1e11b5]
0096A153  44 8B C0                        mov r8d, eax
0096A156  E8 B5 C9 D5 FF                  call 0x1406c6b10
0096A15B  85 C0                           test eax, eax
0096A15D  0F 85 05 FC FF FF               jne 0x140969d68
0096A163  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096A167  83 F8 08                        cmp eax, 8
0096A16A  0F 85 F8 FB FF FF               jne 0x140969d68
0096A170  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096A174  48 8D 0D 5D 11 1E 00            lea rcx, [rip + 0x1e115d]
0096A17B  44 8B C0                        mov r8d, eax
0096A17E  E8 8D C9 D5 FF                  call 0x1406c6b10
0096A183  85 C0                           test eax, eax
0096A185  0F 85 DD FB FF FF               jne 0x140969d68
0096A18B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0096A194  41 8B FF                        mov edi, r15d
0096A197  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0096A19E  F6 81 FA 05 00 00 07            test byte ptr [rcx + 0x5fa], 7
0096A1A5  77 05                           ja 0x14096a1ac
0096A1A7  BF 05 00 07 80                  mov edi, 0x80070005
0096A1AC  85 FF                           test edi, edi
0096A1AE  0F 88 02 09 00 00               js 0x14096aab6
0096A1B4  44 8B 45 E0                     mov r8d, dword ptr [rbp - 0x20]
0096A1B8  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A1BD  49 8B D5                        mov rdx, r13
0096A1C0  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A1C4  E8 23 74 11 00                  call 0x140a815ec
0096A1C9  8B F8                           mov edi, eax
0096A1CB  85 C0                           test eax, eax
0096A1CD  0F 88 E3 08 00 00               js 0x14096aab6
0096A1D3  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A1D8  E9 76 F5 FF FF                  jmp 0x140969753
0096A1DD  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A1E2  49 8B D5                        mov rdx, r13
0096A1E5  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A1E9  E8 E2 2A 10 00                  call 0x140a6ccd0
0096A1EE  8B F8                           mov edi, eax
0096A1F0  85 C0                           test eax, eax
0096A1F2  0F 89 5B F5 FF FF               jns 0x140969753
0096A1F8  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A1FD  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A202  49 8B F7                        mov rsi, r15
0096A205  E9 CE DB FF FF                  jmp 0x140967dd8
0096A20A  48 83 7D 98 00                  cmp qword ptr [rbp - 0x68], 0
0096A20F  0F 84 CF 09 00 00               je 0x14096abe4
0096A215  8B 7D 90                        mov edi, dword ptr [rbp - 0x70]
0096A218  83 FF 03                        cmp edi, 3
0096A21B  0F 86 76 09 00 00               jbe 0x14096ab97
0096A221  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0096A225  33 D2                           xor edx, edx
0096A227  44 8B 00                        mov r8d, dword ptr [rax]
0096A22A  48 8D 48 04                     lea rcx, [rax + 4]
0096A22E  83 FA 03                        cmp edx, 3
0096A231  73 1A                           jae 0x14096a24d
0096A233  48 3B C8                        cmp rcx, rax
0096A236  0F 82 AD F5 FF FF               jb 0x1409697e9
0096A23C  4A 8D 04 01                     lea rax, [rcx + r8]
0096A240  48 3B C1                        cmp rax, rcx
0096A243  0F 82 A0 F5 FF FF               jb 0x1409697e9
0096A249  FF C2                           inc edx
0096A24B  EB DA                           jmp 0x14096a227
0096A24D  48 3B C8                        cmp rcx, rax
0096A250  0F 82 93 F5 FF FF               jb 0x1409697e9
0096A256  33 DB                           xor ebx, ebx
0096A258  45 85 C0                        test r8d, r8d
0096A25B  48 0F 45 D9                     cmovne rbx, rcx
0096A25F  41 83 F8 08                     cmp r8d, 8
0096A263  0F 85 8D 09 00 00               jne 0x14096abf6
0096A269  48 83 7D 98 00                  cmp qword ptr [rbp - 0x68], 0
0096A26E  48 8B 1B                        mov rbx, qword ptr [rbx]
0096A271  0F 84 91 09 00 00               je 0x14096ac08
0096A277  83 FF 04                        cmp edi, 4
0096A27A  0F 86 29 09 00 00               jbe 0x14096aba9
0096A280  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0096A284  33 D2                           xor edx, edx
0096A286  8B 38                           mov edi, dword ptr [rax]
0096A288  48 8D 48 04                     lea rcx, [rax + 4]
0096A28C  83 FA 04                        cmp edx, 4
0096A28F  73 1A                           jae 0x14096a2ab
0096A291  48 3B C8                        cmp rcx, rax
0096A294  0F 82 4F F5 FF FF               jb 0x1409697e9
0096A29A  48 8D 04 39                     lea rax, [rcx + rdi]
0096A29E  48 3B C1                        cmp rax, rcx
0096A2A1  0F 82 42 F5 FF FF               jb 0x1409697e9
0096A2A7  FF C2                           inc edx
0096A2A9  EB DB                           jmp 0x14096a286
0096A2AB  48 3B C8                        cmp rcx, rax
0096A2AE  0F 82 35 F5 FF FF               jb 0x1409697e9
0096A2B4  33 F6                           xor esi, esi
0096A2B6  85 FF                           test edi, edi
0096A2B8  48 0F 45 F1                     cmovne rsi, rcx
0096A2BC  0F 84 2A 0B 00 00               je 0x14096adec
0096A2C2  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096A2C8  48 8B D7                        mov rdx, rdi
0096A2CB  B9 00 01 00 00                  mov ecx, 0x100
0096A2D0  E8 1B 7E 21 00                  call 0x140b820f0
0096A2D5  48 85 C0                        test rax, rax
0096A2D8  0F 84 20 0B 00 00               je 0x14096adfe
0096A2DE  4C 8B C7                        mov r8, rdi
0096A2E1  48 8B D6                        mov rdx, rsi
0096A2E4  48 8B C8                        mov rcx, rax
0096A2E7  E8 54 C5 D5 FF                  call 0x1406c6840
0096A2EC  83 FF 04                        cmp edi, 4
0096A2EF  0F 85 AA 07 00 00               jne 0x14096aa9f
0096A2F5  48 83 7D 98 00                  cmp qword ptr [rbp - 0x68], 0
0096A2FA  0F 84 1A 09 00 00               je 0x14096ac1a
0096A300  83 7D 90 05                     cmp dword ptr [rbp - 0x70], 5
0096A304  0F 86 B1 08 00 00               jbe 0x14096abbb
0096A30A  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0096A30E  33 D2                           xor edx, edx
0096A310  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0096A315  48 8D 48 04                     lea rcx, [rax + 4]
0096A319  4D 8B D6                        mov r10, r14
0096A31C  44 8B 30                        mov r14d, dword ptr [rax]
0096A31F  83 FA 05                        cmp edx, 5
0096A322  0F 83 D9 05 00 00               jae 0x14096a901
0096A328  48 3B C8                        cmp rcx, rax
0096A32B  72 19                           jb 0x14096a346
0096A32D  4A 8D 04 31                     lea rax, [rcx + r14]
0096A331  4C 89 54 24 58                  mov qword ptr [rsp + 0x58], r10
0096A336  4D 8B F2                        mov r14, r10
0096A339  48 3B C1                        cmp rax, rcx
0096A33C  0F 82 A7 F4 FF FF               jb 0x1409697e9
0096A342  FF C2                           inc edx
0096A344  EB CF                           jmp 0x14096a315
0096A346  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A34B  BF 95 00 00 C0                  mov edi, 0xc0000095
0096A350  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A355  49 8B F7                        mov rsi, r15
0096A358  E9 7B DA FF FF                  jmp 0x140967dd8
0096A35D  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A362  49 8B D5                        mov rdx, r13
0096A365  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A369  E8 56 73 13 00                  call 0x140aa16c4
0096A36E  8B F8                           mov edi, eax
0096A370  85 C0                           test eax, eax
0096A372  0F 89 DB F3 FF FF               jns 0x140969753
0096A378  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A37D  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A382  49 8B F7                        mov rsi, r15
0096A385  E9 4E DA FF FF                  jmp 0x140967dd8
0096A38A  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A38F  49 8B D5                        mov rdx, r13
0096A392  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A396  E8 BD 1C 00 00                  call 0x14096c058
0096A39B  8B F8                           mov edi, eax
0096A39D  85 C0                           test eax, eax
0096A39F  0F 89 AE F3 FF FF               jns 0x140969753
0096A3A5  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A3AA  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A3AF  49 8B F7                        mov rsi, r15
0096A3B2  E9 21 DA FF FF                  jmp 0x140967dd8
0096A3B7  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A3BC  49 8B D5                        mov rdx, r13
0096A3BF  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A3C3  E8 04 9B D9 FF                  call 0x140703ecc
0096A3C8  8B F8                           mov edi, eax
0096A3CA  85 C0                           test eax, eax
0096A3CC  0F 89 81 F3 FF FF               jns 0x140969753
0096A3D2  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A3D7  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A3DC  49 8B F7                        mov rsi, r15
0096A3DF  E9 F4 D9 FF FF                  jmp 0x140967dd8
0096A3E4  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A3E9  49 8B D5                        mov rdx, r13
0096A3EC  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A3F0  E8 1F 97 D9 FF                  call 0x140703b14
0096A3F5  8B F8                           mov edi, eax
0096A3F7  85 C0                           test eax, eax
0096A3F9  0F 89 54 F3 FF FF               jns 0x140969753
0096A3FF  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A404  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A409  49 8B F7                        mov rsi, r15
0096A40C  E9 C7 D9 FF FF                  jmp 0x140967dd8
0096A411  44 8B 45 E0                     mov r8d, dword ptr [rbp - 0x20]
0096A415  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A41A  49 8B D5                        mov rdx, r13
0096A41D  E8 86 E6 15 00                  call 0x140ac8aa8
0096A422  8B F8                           mov edi, eax
0096A424  85 C0                           test eax, eax
0096A426  0F 89 27 F3 FF FF               jns 0x140969753
0096A42C  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A431  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A436  49 8B F7                        mov rsi, r15
0096A439  E9 9A D9 FF FF                  jmp 0x140967dd8
0096A43E  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A443  49 8B D5                        mov rdx, r13
0096A446  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A44A  E8 29 79 16 00                  call 0x140ad1d78
0096A44F  8B F8                           mov edi, eax
0096A451  85 C0                           test eax, eax
0096A453  0F 89 FA F2 FF FF               jns 0x140969753
0096A459  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A45E  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A463  49 8B F7                        mov rsi, r15
0096A466  E9 6D D9 FF FF                  jmp 0x140967dd8
0096A46B  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A470  49 8B D5                        mov rdx, r13
0096A473  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A477  E8 4C 2F B7 FF                  call 0x1404dd3c8
0096A47C  8B F8                           mov edi, eax
0096A47E  85 C0                           test eax, eax
0096A480  0F 89 CD F2 FF FF               jns 0x140969753
0096A486  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A48B  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A490  49 8B F7                        mov rsi, r15
0096A493  E9 40 D9 FF FF                  jmp 0x140967dd8
0096A498  33 C0                           xor eax, eax
0096A49A  C7 45 30 00 00 00 00            mov dword ptr [rbp + 0x30], 0
0096A4A1  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0096A4A5  4C 8D 4D 30                     lea r9, [rbp + 0x30]
0096A4A9  B8 08 00 00 00                  mov eax, 8
0096A4AE  48 8D 55 50                     lea rdx, [rbp + 0x50]
0096A4B2  33 FF                           xor edi, edi
0096A4B4  89 45 50                        mov dword ptr [rbp + 0x50], eax
0096A4B7  44 8B C0                        mov r8d, eax
0096A4BA  8D 4F 67                        lea ecx, [rdi + 0x67]
0096A4BD  E8 CE 32 D4 FF                  call 0x1406ad790
0096A4C2  41 8B 5C 24 10                  mov ebx, dword ptr [r12 + 0x10]
0096A4C7  81 FB A0 00 00 00               cmp ebx, 0xa0
0096A4CD  0F 85 FB 01 00 00               jne 0x14096a6ce
0096A4D3  4D 8B 74 24 18                  mov r14, qword ptr [r12 + 0x18]
0096A4D8  48 8D 0D F1 58 1E 00            lea rcx, [rip + 0x1e58f1]
0096A4DF  49 8B D6                        mov rdx, r14
0096A4E2  44 8B C3                        mov r8d, ebx
0096A4E5  E8 26 C6 D5 FF                  call 0x1406c6b10
0096A4EA  85 C0                           test eax, eax
0096A4EC  75 65                           jne 0x14096a553
0096A4EE  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096A4F2  3B C3                           cmp eax, ebx
0096A4F4  75 5D                           jne 0x14096a553
0096A4F6  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096A4FA  48 8D 0D 4F 5B 1E 00            lea rcx, [rip + 0x1e5b4f]
0096A501  44 8B C0                        mov r8d, eax
0096A504  E8 07 C6 D5 FF                  call 0x1406c6b10
0096A509  85 C0                           test eax, eax
0096A50B  75 46                           jne 0x14096a553
0096A50D  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096A512  83 F8 08                        cmp eax, 8
0096A515  75 3C                           jne 0x14096a553
0096A517  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096A51C  48 8D 0D 95 0D 1E 00            lea rcx, [rip + 0x1e0d95]
0096A523  44 8B C0                        mov r8d, eax
0096A526  E8 E5 C5 D5 FF                  call 0x1406c6b10
0096A52B  85 C0                           test eax, eax
0096A52D  75 24                           jne 0x14096a553
0096A52F  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096A533  83 F8 08                        cmp eax, 8
0096A536  75 1B                           jne 0x14096a553
0096A538  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096A53C  48 8D 0D BD 0D 1E 00            lea rcx, [rip + 0x1e0dbd]
0096A543  44 8B C0                        mov r8d, eax
0096A546  E8 C5 C5 D5 FF                  call 0x1406c6b10
0096A54B  85 C0                           test eax, eax
0096A54D  0F 84 80 01 00 00               je 0x14096a6d3
0096A553  4C 8B C3                        mov r8, rbx
0096A556  48 8D 0D D3 5C 1E 00            lea rcx, [rip + 0x1e5cd3]
0096A55D  49 8B D6                        mov rdx, r14
0096A560  E8 AB C5 D5 FF                  call 0x1406c6b10
0096A565  85 C0                           test eax, eax
0096A567  75 68                           jne 0x14096a5d1
0096A569  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096A56D  3D A0 00 00 00                  cmp eax, 0xa0
0096A572  75 5D                           jne 0x14096a5d1
0096A574  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096A578  48 8D 0D 71 5B 1E 00            lea rcx, [rip + 0x1e5b71]
0096A57F  44 8B C0                        mov r8d, eax
0096A582  E8 89 C5 D5 FF                  call 0x1406c6b10
0096A587  85 C0                           test eax, eax
0096A589  75 46                           jne 0x14096a5d1
0096A58B  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096A590  83 F8 08                        cmp eax, 8
0096A593  75 3C                           jne 0x14096a5d1
0096A595  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096A59A  48 8D 0D D7 0C 1E 00            lea rcx, [rip + 0x1e0cd7]
0096A5A1  44 8B C0                        mov r8d, eax
0096A5A4  E8 67 C5 D5 FF                  call 0x1406c6b10
0096A5A9  85 C0                           test eax, eax
0096A5AB  75 24                           jne 0x14096a5d1
0096A5AD  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096A5B1  83 F8 08                        cmp eax, 8
0096A5B4  75 1B                           jne 0x14096a5d1
0096A5B6  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096A5BA  48 8D 0D FF 0C 1E 00            lea rcx, [rip + 0x1e0cff]
0096A5C1  44 8B C0                        mov r8d, eax
0096A5C4  E8 47 C5 D5 FF                  call 0x1406c6b10
0096A5C9  85 C0                           test eax, eax
0096A5CB  0F 84 02 01 00 00               je 0x14096a6d3
0096A5D1  49 8B 74 24 18                  mov rsi, qword ptr [r12 + 0x18]
0096A5D6  48 8D 0D 53 52 1E 00            lea rcx, [rip + 0x1e5253]
0096A5DD  48 8B D6                        mov rdx, rsi
0096A5E0  4C 8B C3                        mov r8, rbx
0096A5E3  E8 28 C5 D5 FF                  call 0x1406c6b10
0096A5E8  85 C0                           test eax, eax
0096A5EA  75 68                           jne 0x14096a654
0096A5EC  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096A5F0  3D A0 00 00 00                  cmp eax, 0xa0
0096A5F5  75 5D                           jne 0x14096a654
0096A5F7  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096A5FB  48 8D 0D 6E 58 1E 00            lea rcx, [rip + 0x1e586e]
0096A602  44 8B C0                        mov r8d, eax
0096A605  E8 06 C5 D5 FF                  call 0x1406c6b10
0096A60A  85 C0                           test eax, eax
0096A60C  75 46                           jne 0x14096a654
0096A60E  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096A613  83 F8 08                        cmp eax, 8
0096A616  75 3C                           jne 0x14096a654
0096A618  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096A61D  48 8D 0D AC 0C 1E 00            lea rcx, [rip + 0x1e0cac]
0096A624  44 8B C0                        mov r8d, eax
0096A627  E8 E4 C4 D5 FF                  call 0x1406c6b10
0096A62C  85 C0                           test eax, eax
0096A62E  75 24                           jne 0x14096a654
0096A630  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096A634  83 F8 08                        cmp eax, 8
0096A637  75 1B                           jne 0x14096a654
0096A639  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096A63D  48 8D 0D AC 0C 1E 00            lea rcx, [rip + 0x1e0cac]
0096A644  44 8B C0                        mov r8d, eax
0096A647  E8 C4 C4 D5 FF                  call 0x1406c6b10
0096A64C  85 C0                           test eax, eax
0096A64E  0F 84 7F 00 00 00               je 0x14096a6d3
0096A654  4C 8B C3                        mov r8, rbx
0096A657  48 8D 0D 52 54 1E 00            lea rcx, [rip + 0x1e5452]
0096A65E  48 8B D6                        mov rdx, rsi
0096A661  E8 AA C4 D5 FF                  call 0x1406c6b10
0096A666  85 C0                           test eax, eax
0096A668  75 64                           jne 0x14096a6ce
0096A66A  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096A66E  3D A0 00 00 00                  cmp eax, 0xa0
0096A673  75 59                           jne 0x14096a6ce
0096A675  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096A679  48 8D 0D 50 52 1E 00            lea rcx, [rip + 0x1e5250]
0096A680  44 8B C0                        mov r8d, eax
0096A683  E8 88 C4 D5 FF                  call 0x1406c6b10
0096A688  85 C0                           test eax, eax
0096A68A  75 42                           jne 0x14096a6ce
0096A68C  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096A691  83 F8 08                        cmp eax, 8
0096A694  75 38                           jne 0x14096a6ce
0096A696  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096A69B  48 8D 0D 6E 0C 1E 00            lea rcx, [rip + 0x1e0c6e]
0096A6A2  44 8B C0                        mov r8d, eax
0096A6A5  E8 66 C4 D5 FF                  call 0x1406c6b10
0096A6AA  85 C0                           test eax, eax
0096A6AC  75 20                           jne 0x14096a6ce
0096A6AE  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096A6B2  83 F8 08                        cmp eax, 8
0096A6B5  75 17                           jne 0x14096a6ce
0096A6B7  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096A6BB  48 8D 0D 06 0C 1E 00            lea rcx, [rip + 0x1e0c06]
0096A6C2  44 8B C0                        mov r8d, eax
0096A6C5  E8 46 C4 D5 FF                  call 0x1406c6b10
0096A6CA  85 C0                           test eax, eax
0096A6CC  74 05                           je 0x14096a6d3
0096A6CE  BF 05 00 07 80                  mov edi, 0x80070005
0096A6D3  85 FF                           test edi, edi
0096A6D5  0F 88 DB 03 00 00               js 0x14096aab6
0096A6DB  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A6E0  49 8B D5                        mov rdx, r13
0096A6E3  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A6E7  E8 88 A1 B5 FF                  call 0x1404c4874
0096A6EC  8B F8                           mov edi, eax
0096A6EE  85 C0                           test eax, eax
0096A6F0  0F 88 C0 03 00 00               js 0x14096aab6
0096A6F6  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A6FB  E9 53 F0 FF FF                  jmp 0x140969753
0096A700  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A705  49 8B D5                        mov rdx, r13
0096A708  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A70C  E8 4F D6 16 00                  call 0x140ad7d60
0096A711  8B F8                           mov edi, eax
0096A713  85 C0                           test eax, eax
0096A715  0F 89 38 F0 FF FF               jns 0x140969753
0096A71B  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A720  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A725  49 8B F7                        mov rsi, r15
0096A728  E9 AB D6 FF FF                  jmp 0x140967dd8
0096A72D  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A732  49 8B D5                        mov rdx, r13
0096A735  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A739  E8 B6 03 17 00                  call 0x140adaaf4
0096A73E  8B F8                           mov edi, eax
0096A740  85 C0                           test eax, eax
0096A742  0F 89 0B F0 FF FF               jns 0x140969753
0096A748  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A74D  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A752  49 8B F7                        mov rsi, r15
0096A755  E9 7E D6 FF FF                  jmp 0x140967dd8
0096A75A  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A75F  49 8B D5                        mov rdx, r13
0096A762  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A766  E8 1D 8F D9 FF                  call 0x140703688
0096A76B  8B F8                           mov edi, eax
0096A76D  85 C0                           test eax, eax
0096A76F  0F 89 DE EF FF FF               jns 0x140969753
0096A775  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A77A  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A77F  49 8B F7                        mov rsi, r15
0096A782  E9 51 D6 FF FF                  jmp 0x140967dd8
0096A787  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A78C  BF 02 00 00 C0                  mov edi, 0xc0000002
0096A791  49 8B F7                        mov rsi, r15
0096A794  E9 3F D6 FF FF                  jmp 0x140967dd8
0096A799  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A79E  49 8B D5                        mov rdx, r13
0096A7A1  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A7A5  E8 FA 43 D9 FF                  call 0x1406feba4
0096A7AA  8B F8                           mov edi, eax
0096A7AC  85 C0                           test eax, eax
0096A7AE  0F 89 9F EF FF FF               jns 0x140969753
0096A7B4  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A7B9  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A7BE  49 8B F7                        mov rsi, r15
0096A7C1  E9 12 D6 FF FF                  jmp 0x140967dd8
0096A7C6  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A7CB  49 8B D5                        mov rdx, r13
0096A7CE  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A7D2  E8 F9 8C 16 00                  call 0x140ad34d0
0096A7D7  8B F8                           mov edi, eax
0096A7D9  85 C0                           test eax, eax
0096A7DB  0F 89 72 EF FF FF               jns 0x140969753
0096A7E1  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A7E6  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A7EB  49 8B F7                        mov rsi, r15
0096A7EE  E9 E5 D5 FF FF                  jmp 0x140967dd8
0096A7F3  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A7F8  49 8B D5                        mov rdx, r13
0096A7FB  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A7FF  E8 FC 92 16 00                  call 0x140ad3b00
0096A804  8B F8                           mov edi, eax
0096A806  85 C0                           test eax, eax
0096A808  0F 89 45 EF FF FF               jns 0x140969753
0096A80E  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A813  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A818  49 8B F7                        mov rsi, r15
0096A81B  E9 B8 D5 FF FF                  jmp 0x140967dd8
0096A820  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A825  49 8B D5                        mov rdx, r13
0096A828  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A82C  E8 4B CF 16 00                  call 0x140ad777c
0096A831  8B F8                           mov edi, eax
0096A833  85 C0                           test eax, eax
0096A835  0F 89 18 EF FF FF               jns 0x140969753
0096A83B  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A840  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A845  49 8B F7                        mov rsi, r15
0096A848  E9 8B D5 FF FF                  jmp 0x140967dd8
0096A84D  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A852  49 8B D5                        mov rdx, r13
0096A855  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A859  E8 E2 45 D9 FF                  call 0x1406fee40
0096A85E  8B F8                           mov edi, eax
0096A860  85 C0                           test eax, eax
0096A862  0F 89 EB EE FF FF               jns 0x140969753
0096A868  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A86D  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A872  49 8B F7                        mov rsi, r15
0096A875  E9 5E D5 FF FF                  jmp 0x140967dd8
0096A87A  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A87F  49 8B D5                        mov rdx, r13
0096A882  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A886  E8 A5 F0 16 00                  call 0x140ad9930
0096A88B  8B F8                           mov edi, eax
0096A88D  85 C0                           test eax, eax
0096A88F  0F 89 BE EE FF FF               jns 0x140969753
0096A895  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A89A  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A89F  49 8B F7                        mov rsi, r15
0096A8A2  E9 31 D5 FF FF                  jmp 0x140967dd8
0096A8A7  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A8AC  49 8B D5                        mov rdx, r13
0096A8AF  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A8B3  E8 58 49 D9 FF                  call 0x1406ff210
0096A8B8  8B F8                           mov edi, eax
0096A8BA  85 C0                           test eax, eax
0096A8BC  0F 89 91 EE FF FF               jns 0x140969753
0096A8C2  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A8C7  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A8CC  49 8B F7                        mov rsi, r15
0096A8CF  E9 04 D5 FF FF                  jmp 0x140967dd8
0096A8D4  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0096A8D9  49 8B D5                        mov rdx, r13
0096A8DC  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0096A8E0  E8 03 13 17 00                  call 0x140adbbe8
0096A8E5  8B F8                           mov edi, eax
0096A8E7  85 C0                           test eax, eax
0096A8E9  0F 89 64 EE FF FF               jns 0x140969753
0096A8EF  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096A8F4  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A8F9  49 8B F7                        mov rsi, r15
0096A8FC  E9 D7 D4 FF FF                  jmp 0x140967dd8
0096A901  48 3B C8                        cmp rcx, rax
0096A904  0F 82 3C FA FF FF               jb 0x14096a346
0096A90A  33 FF                           xor edi, edi
0096A90C  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
0096A911  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0096A916  45 85 F6                        test r14d, r14d
0096A919  48 0F 45 F9                     cmovne rdi, rcx
0096A91D  0F 84 ED 04 00 00               je 0x14096ae10
0096A923  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096A929  49 8B D6                        mov rdx, r14
0096A92C  B9 00 01 00 00                  mov ecx, 0x100
0096A931  E8 BA 77 21 00                  call 0x140b820f0
0096A936  48 85 C0                        test rax, rax
0096A939  0F 84 EB 04 00 00               je 0x14096ae2a
0096A93F  4D 8B C6                        mov r8, r14
0096A942  48 8B D7                        mov rdx, rdi
0096A945  48 8B C8                        mov rcx, rax
0096A948  E8 F3 BE D5 FF                  call 0x1406c6840
0096A94D  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
0096A952  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096A957  41 83 FE 08                     cmp r14d, 8
0096A95B  0F 85 50 01 00 00               jne 0x14096aab1
0096A961  48 8B 05 C0 DA 66 00            mov rax, qword ptr [rip + 0x66dac0]
0096A968  48 8B 17                        mov rdx, qword ptr [rdi]
0096A96B  8B 0E                           mov ecx, dword ptr [rsi]
0096A96D  E8 5E 01 D5 FF                  call 0x1406baad0
0096A972  8B F8                           mov edi, eax
0096A974  41 8D 56 0C                     lea edx, [r14 + 0xc]
0096A978  C7 44 24 7C 14 00 00 00         mov dword ptr [rsp + 0x7c], 0x14
0096A980  B9 00 01 00 00                  mov ecx, 0x100
0096A985  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096A98B  E8 60 77 21 00                  call 0x140b820f0
0096A990  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096A995  48 85 C0                        test rax, rax
0096A998  0F 84 A6 04 00 00               je 0x14096ae44
0096A99E  45 33 FF                        xor r15d, r15d
0096A9A1  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0096A9A5  0F BA EF 1C                     bts edi, 0x1c
0096A9A9  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
0096A9AE  48 85 C0                        test rax, rax
0096A9B1  0F 84 92 01 00 00               je 0x14096ab49
0096A9B7  48 8B D0                        mov rdx, rax
0096A9BA  41 8B CF                        mov ecx, r15d
0096A9BD  41 3B CF                        cmp ecx, r15d
0096A9C0  73 1B                           jae 0x14096a9dd
0096A9C2  8B 02                           mov eax, dword ptr [rdx]
0096A9C4  83 C0 04                        add eax, 4
0096A9C7  83 F8 04                        cmp eax, 4
0096A9CA  0F 83 A3 00 00 00               jae 0x14096aa73
0096A9D0  BF 95 00 00 C0                  mov edi, 0xc0000095
0096A9D5  49 8B F7                        mov rsi, r15
0096A9D8  E9 FB D3 FF FF                  jmp 0x140967dd8
0096A9DD  4C 8D 42 04                     lea r8, [rdx + 4]
0096A9E1  4C 3B C2                        cmp r8, rdx
0096A9E4  72 EA                           jb 0x14096a9d0
0096A9E6  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
0096A9EA  48 8D 42 08                     lea rax, [rdx + 8]
0096A9EE  48 03 4D 80                     add rcx, qword ptr [rbp - 0x80]
0096A9F2  48 3B C1                        cmp rax, rcx
0096A9F5  0F 87 D2 01 00 00               ja 0x14096abcd
0096A9FB  C7 02 04 00 00 00               mov dword ptr [rdx], 4
0096AA01  41 89 38                        mov dword ptr [r8], edi
0096AA04  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
0096AA08  FF C1                           inc ecx
0096AA0A  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0096AA0E  4C 39 7D 80                     cmp qword ptr [rbp - 0x80], r15
0096AA12  0F 84 56 01 00 00               je 0x14096ab6e
0096AA18  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
0096AA1C  45 8B C7                        mov r8d, r15d
0096AA1F  44 3B C1                        cmp r8d, ecx
0096AA22  73 1F                           jae 0x14096aa43
0096AA24  8B 02                           mov eax, dword ptr [rdx]
0096AA26  83 C0 04                        add eax, 4
0096AA29  83 F8 04                        cmp eax, 4
0096AA2C  73 5E                           jae 0x14096aa8c
0096AA2E  BF 95 00 00 C0                  mov edi, 0xc0000095
0096AA33  85 FF                           test edi, edi
0096AA35  0F 89 18 ED FF FF               jns 0x140969753
0096AA3B  49 8B F7                        mov rsi, r15
0096AA3E  E9 95 D3 FF FF                  jmp 0x140967dd8
0096AA43  4C 8D 42 04                     lea r8, [rdx + 4]
0096AA47  4C 3B C2                        cmp r8, rdx
0096AA4A  72 E2                           jb 0x14096aa2e
0096AA4C  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
0096AA50  48 8D 42 0C                     lea rax, [rdx + 0xc]
0096AA54  48 03 4D 80                     add rcx, qword ptr [rbp - 0x80]
0096AA58  41 8B FF                        mov edi, r15d
0096AA5B  48 3B C1                        cmp rax, rcx
0096AA5E  0F 87 76 01 00 00               ja 0x14096abda
0096AA64  C7 02 08 00 00 00               mov dword ptr [rdx], 8
0096AA6A  49 89 18                        mov qword ptr [r8], rbx
0096AA6D  FF 44 24 78                     inc dword ptr [rsp + 0x78]
0096AA71  EB C0                           jmp 0x14096aa33
0096AA73  44 8B C0                        mov r8d, eax
0096AA76  4C 03 C2                        add r8, rdx
0096AA79  4C 3B C2                        cmp r8, rdx
0096AA7C  0F 82 4E FF FF FF               jb 0x14096a9d0
0096AA82  49 8B D0                        mov rdx, r8
0096AA85  FF C1                           inc ecx
0096AA87  E9 31 FF FF FF                  jmp 0x14096a9bd
0096AA8C  44 8B C8                        mov r9d, eax
0096AA8F  4C 03 CA                        add r9, rdx
0096AA92  4C 3B CA                        cmp r9, rdx
0096AA95  72 97                           jb 0x14096aa2e
0096AA97  49 8B D1                        mov rdx, r9
0096AA9A  41 FF C0                        inc r8d
0096AA9D  EB 80                           jmp 0x14096aa1f
0096AA9F  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AAA4  BF 06 02 00 C0                  mov edi, 0xc0000206
0096AAA9  49 8B F7                        mov rsi, r15
0096AAAC  E9 27 D3 FF FF                  jmp 0x140967dd8
0096AAB1  BF 06 02 00 C0                  mov edi, 0xc0000206
0096AAB6  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AABB  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096AAC0  49 8B F7                        mov rsi, r15
0096AAC3  E9 10 D3 FF FF                  jmp 0x140967dd8
0096AAC8  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096AACC  3D A0 00 00 00                  cmp eax, 0xa0
0096AAD1  0F 85 55 F0 FF FF               jne 0x140969b2c
0096AAD7  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096AADB  48 8D 0D 2E 54 1E 00            lea rcx, [rip + 0x1e542e]
0096AAE2  44 8B C0                        mov r8d, eax
0096AAE5  E8 26 C0 D5 FF                  call 0x1406c6b10
0096AAEA  85 C0                           test eax, eax
0096AAEC  0F 85 3A F0 FF FF               jne 0x140969b2c
0096AAF2  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096AAF7  83 F8 08                        cmp eax, 8
0096AAFA  0F 85 2C F0 FF FF               jne 0x140969b2c
0096AB00  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096AB05  48 8D 0D 94 07 1E 00            lea rcx, [rip + 0x1e0794]
0096AB0C  44 8B C0                        mov r8d, eax
0096AB0F  E8 FC BF D5 FF                  call 0x1406c6b10
0096AB14  85 C0                           test eax, eax
0096AB16  0F 85 10 F0 FF FF               jne 0x140969b2c
0096AB1C  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096AB20  83 F8 08                        cmp eax, 8
0096AB23  0F 85 03 F0 FF FF               jne 0x140969b2c
0096AB29  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096AB2D  48 8D 0D 5C 07 1E 00            lea rcx, [rip + 0x1e075c]
0096AB34  44 8B C0                        mov r8d, eax
0096AB37  E8 D4 BF D5 FF                  call 0x1406c6b10
0096AB3C  85 C0                           test eax, eax
0096AB3E  0F 85 E8 EF FF FF               jne 0x140969b2c
0096AB44  E9 98 F0 FF FF                  jmp 0x140969be1
0096AB49  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
0096AB4D  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
0096AB52  BA 08 00 00 00                  mov edx, 8
0096AB57  E8 04 28 AF FF                  call 0x14045d360
0096AB5C  8B F8                           mov edi, eax
0096AB5E  85 C0                           test eax, eax
0096AB60  0F 89 9E FE FF FF               jns 0x14096aa04
0096AB66  49 8B F7                        mov rsi, r15
0096AB69  E9 6A D2 FF FF                  jmp 0x140967dd8
0096AB6E  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
0096AB72  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
0096AB77  BA 0C 00 00 00                  mov edx, 0xc
0096AB7C  E8 DF 27 AF FF                  call 0x14045d360
0096AB81  8B F8                           mov edi, eax
0096AB83  85 C0                           test eax, eax
0096AB85  0F 88 A8 FE FF FF               js 0x14096aa33
0096AB8B  FF 44 24 78                     inc dword ptr [rsp + 0x78]
0096AB8F  41 8B FF                        mov edi, r15d
0096AB92  E9 9C FE FF FF                  jmp 0x14096aa33
0096AB97  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AB9C  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096ABA1  49 8B F7                        mov rsi, r15
0096ABA4  E9 2F D2 FF FF                  jmp 0x140967dd8
0096ABA9  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096ABAE  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096ABB3  49 8B F7                        mov rsi, r15
0096ABB6  E9 1D D2 FF FF                  jmp 0x140967dd8
0096ABBB  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096ABC0  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096ABC5  49 8B F7                        mov rsi, r15
0096ABC8  E9 0B D2 FF FF                  jmp 0x140967dd8
0096ABCD  BF 23 00 00 C0                  mov edi, 0xc0000023
0096ABD2  49 8B F7                        mov rsi, r15
0096ABD5  E9 FE D1 FF FF                  jmp 0x140967dd8
0096ABDA  BF 23 00 00 C0                  mov edi, 0xc0000023
0096ABDF  E9 4F FE FF FF                  jmp 0x14096aa33
0096ABE4  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096ABE9  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096ABEE  49 8B F7                        mov rsi, r15
0096ABF1  E9 E2 D1 FF FF                  jmp 0x140967dd8
0096ABF6  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096ABFB  BF 23 00 00 C0                  mov edi, 0xc0000023
0096AC00  49 8B F7                        mov rsi, r15
0096AC03  E9 D0 D1 FF FF                  jmp 0x140967dd8
0096AC08  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AC0D  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AC12  49 8B F7                        mov rsi, r15
0096AC15  E9 BE D1 FF FF                  jmp 0x140967dd8
0096AC1A  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AC1F  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AC24  49 8B F7                        mov rsi, r15
0096AC27  E9 AC D1 FF FF                  jmp 0x140967dd8
0096AC2C  85 FF                           test edi, edi
0096AC2E  0F 88 CC EB FF FF               js 0x140969800
0096AC34  48 83 7D 98 00                  cmp qword ptr [rbp - 0x68], 0
0096AC39  74 40                           je 0x14096ac7b
0096AC3B  45 85 FF                        test r15d, r15d
0096AC3E  74 22                           je 0x14096ac62
0096AC40  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0096AC44  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0096AC49  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096AC4E  8B 10                           mov edx, dword ptr [rax]
0096AC50  48 8D 48 04                     lea rcx, [rax + 4]
0096AC54  48 3B C8                        cmp rcx, rax
0096AC57  0F 82 7E E8 FF FF               jb 0x1409694db
0096AC5D  E9 1F E8 FF FF                  jmp 0x140969481
0096AC62  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0096AC67  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AC6C  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096AC71  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096AC76  E9 EC DA FF FF                  jmp 0x140968767
0096AC7B  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0096AC80  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AC85  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096AC8A  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096AC8F  E9 D3 DA FF FF                  jmp 0x140968767
0096AC94  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0096AC98  3D A0 00 00 00                  cmp eax, 0xa0
0096AC9D  0F 85 A3 EE FF FF               jne 0x140969b46
0096ACA3  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
0096ACA7  48 8D 0D 22 56 1E 00            lea rcx, [rip + 0x1e5622]
0096ACAE  44 8B C0                        mov r8d, eax
0096ACB1  E8 5A BE D5 FF                  call 0x1406c6b10
0096ACB6  85 C0                           test eax, eax
0096ACB8  0F 85 88 EE FF FF               jne 0x140969b46
0096ACBE  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0096ACC3  83 F8 08                        cmp eax, 8
0096ACC6  0F 85 7A EE FF FF               jne 0x140969b46
0096ACCC  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
0096ACD1  48 8D 0D C0 05 1E 00            lea rcx, [rip + 0x1e05c0]
0096ACD8  44 8B C0                        mov r8d, eax
0096ACDB  E8 30 BE D5 FF                  call 0x1406c6b10
0096ACE0  85 C0                           test eax, eax
0096ACE2  0F 85 5E EE FF FF               jne 0x140969b46
0096ACE8  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0096ACEC  83 F8 08                        cmp eax, 8
0096ACEF  0F 85 51 EE FF FF               jne 0x140969b46
0096ACF5  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
0096ACF9  48 8D 0D E8 05 1E 00            lea rcx, [rip + 0x1e05e8]
0096AD00  44 8B C0                        mov r8d, eax
0096AD03  E8 08 BE D5 FF                  call 0x1406c6b10
0096AD08  85 C0                           test eax, eax
0096AD0A  0F 85 36 EE FF FF               jne 0x140969b46
0096AD10  E9 CC EE FF FF                  jmp 0x140969be1
0096AD15  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AD1A  E9 B9 D0 FF FF                  jmp 0x140967dd8
0096AD1F  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AD24  4C 8B F6                        mov r14, rsi
0096AD27  4C 8B FE                        mov r15, rsi
0096AD2A  E9 A6 D0 FF FF                  jmp 0x140967dd5
0096AD2F  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AD34  4C 8B F6                        mov r14, rsi
0096AD37  4C 8B FE                        mov r15, rsi
0096AD3A  E9 96 D0 FF FF                  jmp 0x140967dd5
0096AD3F  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AD44  E9 6E D0 FF FF                  jmp 0x140967db7
0096AD49  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AD4E  45 33 FF                        xor r15d, r15d
0096AD51  E9 D2 D8 FF FF                  jmp 0x140968628
0096AD56  45 33 FF                        xor r15d, r15d
0096AD59  E9 C5 D8 FF FF                  jmp 0x140968623
0096AD5E  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AD63  45 33 FF                        xor r15d, r15d
0096AD66  E9 BD D8 FF FF                  jmp 0x140968628
0096AD6B  45 33 FF                        xor r15d, r15d
0096AD6E  E9 B0 D8 FF FF                  jmp 0x140968623
0096AD73  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AD78  E9 D9 DA FF FF                  jmp 0x140968856
0096AD7D  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AD82  4D 8B EF                        mov r13, r15
0096AD85  49 8B F7                        mov rsi, r15
0096AD88  E9 4B D0 FF FF                  jmp 0x140967dd8
0096AD8D  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AD92  E9 73 EA FF FF                  jmp 0x14096980a
0096AD97  4D 8B C3                        mov r8, r11
0096AD9A  48 8B D3                        mov rdx, rbx
0096AD9D  49 8B CD                        mov rcx, r13
0096ADA0  E8 9B BA D5 FF                  call 0x1406c6840
0096ADA5  E9 3D DA FF FF                  jmp 0x1409687e7
0096ADAA  BF 17 00 00 C0                  mov edi, 0xc0000017
0096ADAF  E9 4C EA FF FF                  jmp 0x140969800
0096ADB4  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096ADB9  BF 17 00 00 C0                  mov edi, 0xc0000017
0096ADBE  49 8B F7                        mov rsi, r15
0096ADC1  E9 12 D0 FF FF                  jmp 0x140967dd8
0096ADC6  BF 79 00 00 C0                  mov edi, 0xc0000079
0096ADCB  E9 59 F2 FF FF                  jmp 0x14096a029
0096ADD0  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096ADD5  BF 17 00 00 C0                  mov edi, 0xc0000017
0096ADDA  49 8B F7                        mov rsi, r15
0096ADDD  E9 F6 CF FF FF                  jmp 0x140967dd8
0096ADE2  BF 79 00 00 C0                  mov edi, 0xc0000079
0096ADE7  E9 D9 EC FF FF                  jmp 0x140969ac5
0096ADEC  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096ADF1  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096ADF6  49 8B F7                        mov rsi, r15
0096ADF9  E9 DA CF FF FF                  jmp 0x140967dd8
0096ADFE  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AE03  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AE08  49 8B F7                        mov rsi, r15
0096AE0B  E9 C8 CF FF FF                  jmp 0x140967dd8
0096AE10  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AE15  4D 8B F5                        mov r14, r13
0096AE18  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096AE1D  49 8B F7                        mov rsi, r15
0096AE20  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AE25  E9 AE CF FF FF                  jmp 0x140967dd8
0096AE2A  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AE2F  4D 8B F5                        mov r14, r13
0096AE32  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096AE37  49 8B F7                        mov rsi, r15
0096AE3A  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AE3F  E9 94 CF FF FF                  jmp 0x140967dd8
0096AE44  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AE49  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AE4E  49 8B F7                        mov rsi, r15
0096AE51  E9 82 CF FF FF                  jmp 0x140967dd8
0096AE56  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AE5B  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AE60  49 8B F7                        mov rsi, r15
0096AE63  E9 70 CF FF FF                  jmp 0x140967dd8
0096AE68  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AE6D  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AE72  49 8B F7                        mov rsi, r15
0096AE75  E9 5E CF FF FF                  jmp 0x140967dd8
0096AE7A  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AE7F  E9 21 DF FF FF                  jmp 0x140968da5
0096AE84  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096AE89  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AE8E  E9 45 CF FF FF                  jmp 0x140967dd8
0096AE93  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096AE98  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AE9D  E9 36 CF FF FF                  jmp 0x140967dd8
0096AEA2  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096AEA7  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096AEAC  E9 27 CF FF FF                  jmp 0x140967dd8
0096AEB1  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096AEB6  4D 8B EF                        mov r13, r15
0096AEB9  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AEBE  BF 3E 00 00 C0                  mov edi, 0xc000003e
0096AEC3  4D 8B F0                        mov r14, r8
0096AEC6  E9 0D CF FF FF                  jmp 0x140967dd8
0096AECB  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0096AED0  4D 8B F5                        mov r14, r13
0096AED3  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096AED8  BF 17 00 00 C0                  mov edi, 0xc0000017
0096AEDD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096AEE2  E9 F1 CE FF FF                  jmp 0x140967dd8
0096AEE7  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0096AEEC  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096AEF1  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0096AEF6  BF 01 00 00 C0                  mov edi, 0xc0000001
0096AEFB  E9 D8 CE FF FF                  jmp 0x140967dd8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00968AF6(__int64 a1)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p7C;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00968AF6(int64_t Arg1)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p7C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00968AF6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
