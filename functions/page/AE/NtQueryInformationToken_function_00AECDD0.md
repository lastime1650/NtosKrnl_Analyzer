# NtQueryInformationToken

- RVA: `0x00AECDD0`–`0x00AF0523` (길이 `14,163` bytes)
- VA: `0x0000000140AECDD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D0828`
- 디코드: `2,984`개 명령, `14,163/14,163` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **373**; 고유 호출 대상: **53**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00AECE92` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AECF68` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AECF94` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AECFCD` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AECFE5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AECFEA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AECFF7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED011` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED016` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED023` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED066` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED092` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AED0E5` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AED0FD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED102` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED10F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED129` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED12E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED13B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED17E` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED1AA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AED1B2` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (function, `0x00432EC0`)
- `0x00AED1ED` → [SepConvertTokenPrivileges](../../text/46/SepConvertTokenPrivileges_function_00463EF8.md) (function, `0x00463EF8`)
- `0x00AED205` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED20A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED217` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED231` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED236` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED243` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED286` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED2B2` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AED359` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AED371` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED376` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED383` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED39D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED3A2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED3AF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED3F2` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED41E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AED44B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED450` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED45D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED49B` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AED4A5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED4AA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED4B7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED4D1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED4D6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED4E3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED4FD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED502` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED50F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED51B` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (function, `0x004F0968`)
- `0x00AED558` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AED599` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED5B7` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AED5D3` → [RtlQueryElevationFlags](../A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x00AED5FB` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (function, `0x0047B1C4`)
- `0x00AED62E` → [SepReferenceLogonSessionSilo](../A3/SepReferenceLogonSessionSilo_function_00A3B784.md) (function, `0x00A3B784`)
- `0x00AED687` → [SeQuerySessionIdToken](../A0/SeQuerySessionIdToken_function_00A04490.md) (function, `0x00A04490`)
- `0x00AED69F` → [SeSetSessionIdToken](../AF/SeSetSessionIdToken_function_00AF1F0C.md) (function, `0x00AF1F0C`)
- `0x00AED6AD` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (function, `0x0044EDCC`)
- `0x00AED6E9` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x00AED6F3` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (function, `0x0044EDCC`)
- `0x00AED71A` → [SepReferenceLogonSession](../A3/SepReferenceLogonSession_function_00A3B74C.md) (function, `0x00A3B74C`)
- `0x00AED75E` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x00AED771` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AED799` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED7A6` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x00AED7BF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED7EF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED82F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED863` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AED8A0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED8A5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED8CE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AED8DC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED8E1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED8FC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED901` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED90E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED928` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AED92D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AED93A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AED9A9` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AED9D8` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEDA30` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEDA35` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEDA87` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEDA91` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEDA96` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEDAB1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEDAB6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEDAC3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDADD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEDAE2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEDAEF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDB2F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEDB76` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEDC05` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (function, `0x00432EC0`)
- `0x00AEDC29` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEDC2E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEDC3B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDC56` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDC94` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEDCF8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDD13` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDD51` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEDD99` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDDB4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDDF6` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEDE44` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDE5F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDE9D` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEDED0` → [SeQuerySessionIdToken](../A0/SeQuerySessionIdToken_function_00A04490.md) (function, `0x00A04490`)
- `0x00AEDF04` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDF1F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDF9E` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEDFCC` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (function, `0x0047B1C4`)
- `0x00AEDFDC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEDFF7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE012` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE052` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEE096` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE0B1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE0C7` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AEE10C` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEE151` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEE194` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEE199` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEE1A6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE1C1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE1FF` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEE24D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE290` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEE2C1` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEE2C9` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (function, `0x00432EC0`)
- `0x00AEE419` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEE45E` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEE469` → [SepConvertTokenPrivilegesToLuidAndAttributes](../../text/42/SepConvertTokenPrivilegesToLuidAndAttributes_function_0042A870.md) (function, `0x0042A870`)
- `0x00AEE481` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEE486` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEE493` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE4AD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEE4B2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEE4BF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEE530` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEE554` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AEE56C` → [RtlQueryElevationFlags](../A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x00AEE599` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AEE5B7` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AEE5D8` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (function, `0x0047B1C4`)
- `0x00AEE60D` → [SepLogonSystemManagedAdmin](../70/SepLogonSystemManagedAdmin_function_00704DA4.md) (function, `0x00704DA4`)
- `0x00AEE648` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AEE659` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00AEE688` → [SepReferenceLogonSessionSilo](../A3/SepReferenceLogonSessionSilo_function_00A3B784.md) (function, `0x00A3B784`)
- `0x00AEE693` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AEE6B5` → [SeQuerySessionIdToken](../A0/SeQuerySessionIdToken_function_00A04490.md) (function, `0x00A04490`)
- `0x00AEE6CD` → [SeSetSessionIdToken](../AF/SeSetSessionIdToken_function_00AF1F0C.md) (function, `0x00AF1F0C`)
- `0x00AEE6DC` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (function, `0x0044EDCC`)
- `0x00AEE70C` → [SepReferenceLogonSession](../A3/SepReferenceLogonSession_function_00A3B74C.md) (function, `0x00A3B74C`)
- `0x00AEE71A` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (function, `0x0044EDCC`)
- `0x00AEE748` → [SepReferenceLogonSessionSilo](../A3/SepReferenceLogonSessionSilo_function_00A3B784.md) (function, `0x00A3B784`)
- `0x00AEE75F` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AEE7B9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEE7C9` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEE7CE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEE7FE` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00AEE832` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEE842` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEE847` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEE87D` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x00AEE8A0` → [SeQueryTokenIntegrity](../../text/41/SeQueryTokenIntegrity_function_00419CF4.md) (function, `0x00419CF4`)
- `0x00AEE8B7` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AEE8CA` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AEE904` → [RtlSuffixUnicodeString](../78/RtlSuffixUnicodeString_function_0078A780.md) (function, `0x0078A780`)
- `0x00AEE921` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00AEE967` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AEE9AD` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x00AEE9BC` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (function, `0x0044EDCC`)
- `0x00AEE9EE` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x00AEEA06` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEA31` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEA3E` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x00AEEA59` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEABF` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEEB4F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEEB7E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEEC19` → [SepGetTokenAccessInformationBufferSize](../9E/SepGetTokenAccessInformationBufferSize_function_009E995C.md) (function, `0x009E995C`)
- `0x00AEECB0` → [SepCopyTokenAccessInformation](../9E/SepCopyTokenAccessInformation_function_009E9C0C.md) (function, `0x009E9C0C`)
- `0x00AEECC8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEECCD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEECDA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEECF4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEECF9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEED06` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEED44` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEED93` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEDAE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEE03` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEEE32` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEEE3A` → [SepGetTokenElevation](../../text/44/SepGetTokenElevation_function_0044F3C8.md) (function, `0x0044F3C8`)
- `0x00AEEE45` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEEE4A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEEE67` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEEAA` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEEEDB` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEEEEB` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (function, `0x00419D10`)
- `0x00AEEF52` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEEF6A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEEF6F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEEF7C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEEF96` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEEF9B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEEFA8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF034` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF065` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEF102` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEF11A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF11F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF12C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF146` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF14B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF158` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF196` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF1C7` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEF20F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF214` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF221` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF2A4` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEF2BC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF2C1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF2CE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF2E8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF2ED` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF2FA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF338` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF366` → [SeQueryMandatoryPolicyToken](../../text/43/SeQueryMandatoryPolicyToken_function_004382B0.md) (function, `0x004382B0`)
- `0x00AEF388` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF3A3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF3E3` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF410` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEF45A` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AEF472` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF477` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF484` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF49E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF4A3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF4B0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF51C` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF54B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEF57B` → [AuthzBasepQuerySecurityAttributesToken](../../text/3A/AuthzBasepQuerySecurityAttributesToken_function_003A7D80.md) (function, `0x003A7D80`)
- `0x00AEF5C3` → [AuthzBasepQuerySecurityAttributesToken](../../text/3A/AuthzBasepQuerySecurityAttributesToken_function_003A7D80.md) (function, `0x003A7D80`)
- `0x00AEF5E4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF5E9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF5F6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF610` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF615` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF622` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF662` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF691` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEF757` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x00AEF76F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF774` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF781` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF79B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF7A0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF7AD` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF7EB` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF81A` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEF867` → [AuthzBasepQueryClaimAttributesToken](../A1/AuthzBasepQueryClaimAttributesToken_function_00A1830C.md) (function, `0x00A1830C`)
- `0x00AEF8F7` → [AuthzBasepQueryClaimAttributesToken](../A1/AuthzBasepQueryClaimAttributesToken_function_00A1830C.md) (function, `0x00A1830C`)
- `0x00AEF909` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF90E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF929` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF92E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF93B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF955` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEF95A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEF967` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEF9A5` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEF9EA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEFA02` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFA07` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFA24` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFA3F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFABE` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEFAEF` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEFB48` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AEFB5A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFB74` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFB79` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFB86` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFBA0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFBA5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFBB2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFBF0` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEFC21` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEFC49` → [SepInternalQuerySecurityAttributesTokenEx](../../text/3A/SepInternalQuerySecurityAttributesTokenEx_function_003A77B0.md) (function, `0x003A77B0`)
- `0x00AEFC5B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFC60` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFC7B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFC80` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFC8D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFCCD` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEFCFA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEFD63` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AEFD7B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFD80` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFD8D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFDA7` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFDAC` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFDB9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFE00` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (function, `0x006066CC`)
- `0x00AEFE3F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEFE6E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AEFE92` → [SepGetAgentIdClaimValue](../7A/SepGetAgentIdClaimValue_function_007A0FDC.md) (function, `0x007A0FDC`)
- `0x00AEFEB6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00AEFEED` → [RtlWriteULongToUser](../70/RtlWriteULongToUser_function_00705E8C.md) (function, `0x00705E8C`)
- `0x00AEFF16` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AEFF36` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFF3B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFF48` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFF62` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AEFF67` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AEFF74` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEFF80` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00AEFFC1` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AEFFF0` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AF0013` → [SepIsAppSuiteSid](../../text/60/SepIsAppSuiteSid_function_006083A0.md) (function, `0x006083A0`)
- `0x00AF005C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0061` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF006E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF0088` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF008D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF009A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF00C0` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AF00D8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF00DD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF00EA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF0104` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0109` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0116` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF0122` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00AF0163` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AF0190` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AF01F9` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AF0211` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0216` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0223` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF023D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0242` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF024F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF025B` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00AF029C` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00AF02C9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AF032F` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x00AF0339` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF034E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0353` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0360` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF037A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF037F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF038C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF039C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF03A6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF045A` → [SepIsSandboxedToken](../../text/45/SepIsSandboxedToken_function_00458704.md) (function, `0x00458704`)
- `0x00AF048C` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x00AF0499` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00AF04B1` → [SeHasTamperProtection](../../text/60/SeHasTamperProtection_function_0060777C.md) (function, `0x0060777C`)
- `0x00AF04E6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF04FE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [RtlGetAppContainerNamedObjectPath](../../text/5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E7050`
- [RtlGetAppContainerNamedObjectPath](../../text/5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E707F`
- [RtlGetAppContainerNamedObjectPath](../../text/5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E70B2`
- [RtlGetAppContainerNamedObjectPath](../../text/5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E70D5`
- [RtlGetAppContainerNamedObjectPath](../../text/5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E712A`
- [RtlpGetTokenNamedObjectPath](../78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078EE74`
- [RtlpGetTokenNamedObjectPath](../78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078EEA5`
- [RtlpGetTokenNamedObjectPath](../78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078EEE6`
- [RtlpGetTokenNamedObjectPath](../78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078EF16`
- [RtlpGetTokenNamedObjectPath](../78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078EF5B`
- [RtlpGetTokenNamedObjectPath](../78/RtlpGetTokenNamedObjectPath_function_0078ED40.md) at `0x0078EFCB`

### Static image references
- `0x00AED551` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00AEE0C0` → RVA `0x00FD9B00` (`PAGEDATA`; read)
- `0x00AEE61A` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x00AEE8F4` → RVA `0x0000B7E0` (`.rdata`; read)
- `0x00AEFEA7` → RVA `0x00B05DF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AF0483` → RVA `0x00E67BD8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **323**
  - `0x00AECF68` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AECF94` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AECFE5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AECFEA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AECFF7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED011` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED016` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED023` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED066` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED092` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AED0FD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED102` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED10F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED129` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED12E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED13B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED17E` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED1AA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AED1B2` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (`PAGE` → `.text`)
  - `0x00AED1ED` → [SepConvertTokenPrivileges](../../text/46/SepConvertTokenPrivileges_function_00463EF8.md) (`PAGE` → `.text`)
  - `0x00AED205` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED20A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED217` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED231` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED236` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED243` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED286` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED2B2` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AED371` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED376` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED383` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED39D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED3A2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED3AF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED3F2` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED41E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AED44B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED450` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED45D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED4A5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED4AA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED4B7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED4D1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED4D6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED4E3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED4FD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED502` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED50F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED51B` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (`PAGE` → `.text`)
  - `0x00AED599` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED5B7` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AED5FB` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (`PAGE` → `.text`)
  - `0x00AED6AD` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (`PAGE` → `.text`)
  - `0x00AED6F3` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (`PAGE` → `.text`)
  - `0x00AED771` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AED799` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED7BF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED7EF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED82F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED863` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AED8A0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED8A5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED8CE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AED8DC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED8E1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED8FC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED901` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED90E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED928` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AED92D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AED93A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AED9A9` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AED9D8` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEDA30` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEDA35` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEDA91` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEDA96` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEDAB1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEDAB6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEDAC3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDADD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEDAE2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEDAEF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDB2F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEDB76` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEDC05` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (`PAGE` → `.text`)
  - `0x00AEDC29` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEDC2E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEDC3B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDC56` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDC94` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEDCF8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDD13` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDD51` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEDD99` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDDB4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDDF6` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEDE44` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDE5F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDE9D` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEDF04` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDF1F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDF9E` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEDFCC` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (`PAGE` → `.text`)
  - `0x00AEDFDC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEDFF7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE012` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE052` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEE096` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE0B1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE10C` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEE151` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEE194` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEE199` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEE1A6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE1C1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE1FF` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEE24D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE290` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEE2C1` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEE2C9` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (`PAGE` → `.text`)
  - `0x00AEE469` → [SepConvertTokenPrivilegesToLuidAndAttributes](../../text/42/SepConvertTokenPrivilegesToLuidAndAttributes_function_0042A870.md) (`PAGE` → `.text`)
  - `0x00AEE481` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEE486` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEE493` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE4AD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEE4B2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEE4BF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEE530` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEE554` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AEE5B7` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AEE5D8` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (`PAGE` → `.text`)
  - `0x00AEE693` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AEE6DC` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (`PAGE` → `.text`)
  - `0x00AEE71A` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (`PAGE` → `.text`)
  - `0x00AEE75F` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AEE7B9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEE7C9` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEE7CE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEE832` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEE842` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEE847` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEE87D` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x00AEE8A0` → [SeQueryTokenIntegrity](../../text/41/SeQueryTokenIntegrity_function_00419CF4.md) (`PAGE` → `.text`)
  - `0x00AEE8B7` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AEE8CA` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AEE967` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AEE9BC` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (`PAGE` → `.text`)
  - `0x00AEEA06` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEA31` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEA59` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEABF` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEEB4F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEEB7E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEECC8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEECCD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEECDA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEECF4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEECF9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEED06` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEED44` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEED93` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEDAE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEE03` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEEE32` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEEE3A` → [SepGetTokenElevation](../../text/44/SepGetTokenElevation_function_0044F3C8.md) (`PAGE` → `.text`)
  - `0x00AEEE45` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEEE4A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEEE67` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEEAA` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEEEDB` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEEEEB` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (`PAGE` → `.text`)
  - `0x00AEEF6A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEEF6F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEEF7C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEEF96` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEEF9B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEEFA8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF034` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF065` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEF11A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF11F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF12C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF146` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF14B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF158` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF196` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF1C7` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEF20F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF214` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF221` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF2BC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF2C1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF2CE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF2E8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF2ED` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF2FA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF338` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF366` → [SeQueryMandatoryPolicyToken](../../text/43/SeQueryMandatoryPolicyToken_function_004382B0.md) (`PAGE` → `.text`)
  - `0x00AEF388` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF3A3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF3E3` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF410` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEF472` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF477` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF484` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF49E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF4A3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF4B0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF51C` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF54B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEF57B` → [AuthzBasepQuerySecurityAttributesToken](../../text/3A/AuthzBasepQuerySecurityAttributesToken_function_003A7D80.md) (`PAGE` → `.text`)
  - `0x00AEF5C3` → [AuthzBasepQuerySecurityAttributesToken](../../text/3A/AuthzBasepQuerySecurityAttributesToken_function_003A7D80.md) (`PAGE` → `.text`)
  - `0x00AEF5E4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF5E9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF5F6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF610` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF615` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF622` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF662` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF691` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEF76F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF774` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF781` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF79B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF7A0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF7AD` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF7EB` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF81A` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEF909` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF90E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF929` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF92E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF93B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF955` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEF95A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEF967` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEF9A5` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEF9EA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEFA02` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFA07` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFA24` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFA3F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFABE` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEFAEF` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEFB48` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AEFB5A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFB74` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFB79` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFB86` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFBA0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFBA5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFBB2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFBF0` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEFC21` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEFC49` → [SepInternalQuerySecurityAttributesTokenEx](../../text/3A/SepInternalQuerySecurityAttributesTokenEx_function_003A77B0.md) (`PAGE` → `.text`)
  - `0x00AEFC5B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFC60` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFC7B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFC80` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFC8D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFCCD` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEFCFA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEFD7B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFD80` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFD8D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFDA7` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFDAC` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFDB9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFE00` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (`PAGE` → `.text`)
  - `0x00AEFE3F` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEFE6E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AEFEB6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00AEFF16` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AEFF36` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFF3B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFF48` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFF62` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AEFF67` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AEFF74` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEFF80` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00AEFFC1` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AEFFF0` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AF0013` → [SepIsAppSuiteSid](../../text/60/SepIsAppSuiteSid_function_006083A0.md) (`PAGE` → `.text`)
  - `0x00AF005C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0061` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF006E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF0088` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF008D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF009A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF00D8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF00DD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF00EA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF0104` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0109` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0116` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF0122` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00AF0163` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AF0190` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AF0211` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0216` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0223` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF023D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0242` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF024F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF025B` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00AF029C` → [SepReferenceTokenByHandle](../../text/3E/SepReferenceTokenByHandle_function_003EDAD0.md) (`PAGE` → `.text`)
  - `0x00AF02C9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AF0339` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF034E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0353` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0360` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF037A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF037F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF038C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF039C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF03A6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF045A` → [SepIsSandboxedToken](../../text/45/SepIsSandboxedToken_function_00458704.md) (`PAGE` → `.text`)
  - `0x00AF048C` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (`PAGE` → `.text`)
  - `0x00AF0499` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00AF04B1` → [SeHasTamperProtection](../../text/60/SeHasTamperProtection_function_0060777C.md) (`PAGE` → `.text`)
  - `0x00AF04E6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF04FE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AECDD0  48 8B C4                        mov rax, rsp
00AECDD3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00AECDD7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00AECDDB  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00AECDDF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AECDE3  57                              push rdi
00AECDE4  41 54                           push r12
00AECDE6  41 55                           push r13
00AECDE8  41 56                           push r14
00AECDEA  41 57                           push r15
00AECDEC  48 81 EC D0 01 00 00            sub rsp, 0x1d0
00AECDF3  41 8B F1                        mov esi, r9d
00AECDF6  4D 8B F8                        mov r15, r8
00AECDF9  44 8B F2                        mov r14d, edx
00AECDFC  48 8B D9                        mov rbx, rcx
00AECDFF  33 FF                           xor edi, edi
00AECE01  48 89 B8 90 FE FF FF            mov qword ptr [rax - 0x170], rdi
00AECE08  89 B8 A4 FE FF FF               mov dword ptr [rax - 0x15c], edi
00AECE0E  89 B8 04 FF FF FF               mov dword ptr [rax - 0xfc], edi
00AECE14  89 B8 00 FF FF FF               mov dword ptr [rax - 0x100], edi
00AECE1A  48 89 B8 78 FF FF FF            mov qword ptr [rax - 0x88], rdi
00AECE21  89 B8 C0 FE FF FF               mov dword ptr [rax - 0x140], edi
00AECE27  0F 57 C0                        xorps xmm0, xmm0
00AECE2A  0F 11 40 80                     movups xmmword ptr [rax - 0x80], xmm0
00AECE2E  48 89 B8 B0 FE FF FF            mov qword ptr [rax - 0x150], rdi
00AECE35  89 B8 BC FE FF FF               mov dword ptr [rax - 0x144], edi
00AECE3B  40 88 B8 D8 FE FF FF            mov byte ptr [rax - 0x128], dil
00AECE42  0F 11 40 C0                     movups xmmword ptr [rax - 0x40], xmm0
00AECE46  0F 57 C9                        xorps xmm1, xmm1
00AECE49  0F 11 88 48 FF FF FF            movups xmmword ptr [rax - 0xb8], xmm1
00AECE50  0F 11 88 58 FF FF FF            movups xmmword ptr [rax - 0xa8], xmm1
00AECE57  0F 11 88 68 FF FF FF            movups xmmword ptr [rax - 0x98], xmm1
00AECE5E  40 88 BC 24 98 00 00 00         mov byte ptr [rsp + 0x98], dil
00AECE66  40 88 B8 88 FE FF FF            mov byte ptr [rax - 0x178], dil
00AECE6D  48 89 B8 98 FE FF FF            mov qword ptr [rax - 0x168], rdi
00AECE74  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AECE7D  44 8A A8 32 02 00 00            mov r13b, byte ptr [rax + 0x232]
00AECE84  45 84 ED                        test r13b, r13b
00AECE87  74 32                           je 0x140aecebb
00AECE89  8B D6                           mov edx, esi
00AECE8B  44 8D 47 04                     lea r8d, [rdi + 4]
00AECE8F  49 8B CF                        mov rcx, r15
00AECE92  E8 29 C3 DF FF                  call 0x1408e91c0
00AECE97  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00AECEA1  4C 8B A4 24 20 02 00 00         mov r12, qword ptr [rsp + 0x220]
00AECEA9  4C 3B E1                        cmp r12, rcx
00AECEAC  49 0F 42 CC                     cmovb rcx, r12
00AECEB0  8B 01                           mov eax, dword ptr [rcx]
00AECEB2  89 01                           mov dword ptr [rcx], eax
00AECEB4  EB 0D                           jmp 0x140aecec3
00AECEB6  E9 4A 36 00 00                  jmp 0x140af0505
00AECEBB  4C 8B A4 24 20 02 00 00         mov r12, qword ptr [rsp + 0x220]
00AECEC3  41 83 FE 19                     cmp r14d, 0x19
00AECEC7  0F 8F E7 20 00 00               jg 0x140aeefb4
00AECECD  0F 84 A5 1F 00 00               je 0x140aeee78
00AECED3  41 83 FE 0C                     cmp r14d, 0xc
00AECED7  0F 8F 4E 10 00 00               jg 0x140aedf2b
00AECEDD  0F 84 88 0F 00 00               je 0x140aede6b
00AECEE3  41 83 FE 06                     cmp r14d, 6
00AECEE7  0F 8F 59 0A 00 00               jg 0x140aed946
00AECEED  0F 84 08 09 00 00               je 0x140aed7fb
00AECEF3  41 83 FE FE                     cmp r14d, -2
00AECEF7  0F 84 1E 06 00 00               je 0x140aed51b
00AECEFD  BB 01 00 00 00                  mov ebx, 1
00AECF02  44 3B F3                        cmp r14d, ebx
00AECF05  0F 84 B0 04 00 00               je 0x140aed3bb
00AECF0B  41 83 FE 02                     cmp r14d, 2
00AECF0F  0F 84 3A 03 00 00               je 0x140aed24f
00AECF15  41 83 FE 03                     cmp r14d, 3
00AECF19  0F 84 28 02 00 00               je 0x140aed147
00AECF1F  41 83 FE 04                     cmp r14d, 4
00AECF23  0F 84 06 01 00 00               je 0x140aed02f
00AECF29  41 83 FE 05                     cmp r14d, 5
00AECF2D  0F 85 91 08 00 00               jne 0x140aed7c4
00AECF33  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AECF3B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AECF40  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AECF48  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AECF4D  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AECF55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AECF5A  45 8A C5                        mov r8b, r13b
00AECF5D  8D 53 07                        lea edx, [rbx + 7]
00AECF60  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
00AECF68  E8 63 0B 90 FF                  call 0x1403edad0
00AECF6D  85 C0                           test eax, eax
00AECF6F  0F 88 90 35 00 00               js 0x140af0505
00AECF75  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AECF7E  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AECF85  90                              nop
00AECF86  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AECF8E  8A D3                           mov dl, bl
00AECF90  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AECF94  E8 27 4C 72 FF                  call 0x140211bc0
00AECF99  48 8B 87 A8 00 00 00            mov rax, qword ptr [rdi + 0xa8]
00AECFA0  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AECFA4  8D 0C 8D 10 00 00 00            lea ecx, [rcx*4 + 0x10]
00AECFAB  41 89 0C 24                     mov dword ptr [r12], ecx
00AECFAF  39 8C 24 18 02 00 00            cmp dword ptr [rsp + 0x218], ecx
00AECFB6  0F 82 8B 04 00 00               jb 0x140aed447
00AECFBC  49 8D 57 08                     lea rdx, [r15 + 8]
00AECFC0  49 89 17                        mov qword ptr [r15], rdx
00AECFC3  83 C1 F8                        add ecx, -8
00AECFC6  4C 8B 87 A8 00 00 00            mov r8, qword ptr [rdi + 0xa8]
00AECFCD  E8 7E CA EB FF                  call 0x1409a9a50
00AECFD2  E9 CA 04 00 00                  jmp 0x140aed4a1
00AECFD7  8B F8                           mov edi, eax
00AECFD9  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AECFE1  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AECFE5  E8 26 2A 77 FF                  call 0x14025fa10
00AECFEA  E8 C1 08 77 FF                  call 0x14025d8b0
00AECFEF  BA 53 68 72 74                  mov edx, 0x74726853
00AECFF4  48 8B CB                        mov rcx, rbx
00AECFF7  E8 E4 A8 80 FF                  call 0x1402f78e0
00AECFFC  8B C7                           mov eax, edi
00AECFFE  E9 02 35 00 00                  jmp 0x140af0505
00AED003  8B F8                           mov edi, eax
00AED005  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED00D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED011  E8 FA 29 77 FF                  call 0x14025fa10
00AED016  E8 95 08 77 FF                  call 0x14025d8b0
00AED01B  BA 53 68 72 74                  mov edx, 0x74726853
00AED020  48 8B CB                        mov rcx, rbx
00AED023  E8 B8 A8 80 FF                  call 0x1402f78e0
00AED028  8B C7                           mov eax, edi
00AED02A  E9 D6 34 00 00                  jmp 0x140af0505
00AED02F  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED037  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED03C  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED044  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED049  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED051  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED056  45 8A C5                        mov r8b, r13b
00AED059  BA 08 00 00 00                  mov edx, 8
00AED05E  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
00AED066  E8 65 0A 90 FF                  call 0x1403edad0
00AED06B  85 C0                           test eax, eax
00AED06D  0F 88 92 34 00 00               js 0x140af0505
00AED073  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AED07C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AED083  90                              nop
00AED084  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AED08C  8A D3                           mov dl, bl
00AED08E  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AED092  E8 29 4B 72 FF                  call 0x140211bc0
00AED097  8B 8F 90 00 00 00               mov ecx, dword ptr [rdi + 0x90]
00AED09D  48 03 C9                        add rcx, rcx
00AED0A0  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
00AED0A7  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
00AED0AB  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AED0AF  8D 0C 85 10 00 00 00            lea ecx, [rax*4 + 0x10]
00AED0B6  41 89 0C 24                     mov dword ptr [r12], ecx
00AED0BA  39 8C 24 18 02 00 00            cmp dword ptr [rsp + 0x218], ecx
00AED0C1  0F 82 80 03 00 00               jb 0x140aed447
00AED0C7  49 8D 57 08                     lea rdx, [r15 + 8]
00AED0CB  49 89 17                        mov qword ptr [r15], rdx
00AED0CE  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
00AED0D4  48 03 C0                        add rax, rax
00AED0D7  4C 8B 87 98 00 00 00            mov r8, qword ptr [rdi + 0x98]
00AED0DE  83 C1 F8                        add ecx, -8
00AED0E1  4D 8B 04 C0                     mov r8, qword ptr [r8 + rax*8]
00AED0E5  E8 66 C9 EB FF                  call 0x1409a9a50
00AED0EA  E9 B2 03 00 00                  jmp 0x140aed4a1
00AED0EF  8B F8                           mov edi, eax
00AED0F1  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED0F9  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED0FD  E8 0E 29 77 FF                  call 0x14025fa10
00AED102  E8 A9 07 77 FF                  call 0x14025d8b0
00AED107  BA 53 68 72 74                  mov edx, 0x74726853
00AED10C  48 8B CB                        mov rcx, rbx
00AED10F  E8 CC A7 80 FF                  call 0x1402f78e0
00AED114  8B C7                           mov eax, edi
00AED116  E9 EA 33 00 00                  jmp 0x140af0505
00AED11B  8B F8                           mov edi, eax
00AED11D  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED125  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED129  E8 E2 28 77 FF                  call 0x14025fa10
00AED12E  E8 7D 07 77 FF                  call 0x14025d8b0
00AED133  BA 53 68 72 74                  mov edx, 0x74726853
00AED138  48 8B CB                        mov rcx, rbx
00AED13B  E8 A0 A7 80 FF                  call 0x1402f78e0
00AED140  8B C7                           mov eax, edi
00AED142  E9 BE 33 00 00                  jmp 0x140af0505
00AED147  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED14F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED154  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED15C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED161  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED169  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED16E  45 8A C5                        mov r8b, r13b
00AED171  BA 08 00 00 00                  mov edx, 8
00AED176  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
00AED17E  E8 4D 09 90 FF                  call 0x1403edad0
00AED183  85 C0                           test eax, eax
00AED185  0F 88 7A 33 00 00               js 0x140af0505
00AED18B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AED194  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AED19B  90                              nop
00AED19C  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AED1A4  8A D3                           mov dl, bl
00AED1A6  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AED1AA  E8 11 4A 72 FF                  call 0x140211bc0
00AED1AF  48 8B CF                        mov rcx, rdi
00AED1B2  E8 09 5D 94 FF                  call 0x140432ec0
00AED1B7  3B C3                           cmp eax, ebx
00AED1B9  76 0D                           jbe 0x140aed1c8
00AED1BB  8D 04 40                        lea eax, [rax + rax*2]
00AED1BE  44 8D 24 85 04 00 00 00         lea r12d, [rax*4 + 4]
00AED1C6  EB 06                           jmp 0x140aed1ce
00AED1C8  41 BC 10 00 00 00               mov r12d, 0x10
00AED1CE  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AED1D6  44 89 20                        mov dword ptr [rax], r12d
00AED1D9  44 39 A4 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r12d
00AED1E1  0F 82 60 02 00 00               jb 0x140aed447
00AED1E7  49 8B D7                        mov rdx, r15
00AED1EA  48 8B CF                        mov rcx, rdi
00AED1ED  E8 06 6D 97 FF                  call 0x140463ef8
00AED1F2  E9 AA 02 00 00                  jmp 0x140aed4a1
00AED1F7  8B F8                           mov edi, eax
00AED1F9  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED201  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED205  E8 06 28 77 FF                  call 0x14025fa10
00AED20A  E8 A1 06 77 FF                  call 0x14025d8b0
00AED20F  BA 53 68 72 74                  mov edx, 0x74726853
00AED214  48 8B CB                        mov rcx, rbx
00AED217  E8 C4 A6 80 FF                  call 0x1402f78e0
00AED21C  8B C7                           mov eax, edi
00AED21E  E9 E2 32 00 00                  jmp 0x140af0505
00AED223  8B F8                           mov edi, eax
00AED225  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED22D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED231  E8 DA 27 77 FF                  call 0x14025fa10
00AED236  E8 75 06 77 FF                  call 0x14025d8b0
00AED23B  BA 53 68 72 74                  mov edx, 0x74726853
00AED240  48 8B CB                        mov rcx, rbx
00AED243  E8 98 A6 80 FF                  call 0x1402f78e0
00AED248  8B C7                           mov eax, edi
00AED24A  E9 B6 32 00 00                  jmp 0x140af0505
00AED24F  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED257  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED25C  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED264  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED269  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED271  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED276  45 8A C5                        mov r8b, r13b
00AED279  BA 08 00 00 00                  mov edx, 8
00AED27E  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
00AED286  E8 45 08 90 FF                  call 0x1403edad0
00AED28B  85 C0                           test eax, eax
00AED28D  0F 88 72 32 00 00               js 0x140af0505
00AED293  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AED29C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AED2A3  90                              nop
00AED2A4  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AED2AC  8A D3                           mov dl, bl
00AED2AE  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AED2B2  E8 09 49 72 FF                  call 0x140211bc0
00AED2B7  8B 4F 7C                        mov ecx, dword ptr [rdi + 0x7c]
00AED2BA  44 8B C1                        mov r8d, ecx
00AED2BD  41 C1 E0 04                     shl r8d, 4
00AED2C1  41 83 C0 F8                     add r8d, -8
00AED2C5  41 BC 10 00 00 00               mov r12d, 0x10
00AED2CB  3B CB                           cmp ecx, ebx
00AED2CD  76 25                           jbe 0x140aed2f4
00AED2CF  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
00AED2D6  49 03 D4                        add rdx, r12
00AED2D9  44 8D 49 FF                     lea r9d, [rcx - 1]
00AED2DD  48 8B 02                        mov rax, qword ptr [rdx]
00AED2E0  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AED2E4  45 8D 04 88                     lea r8d, [r8 + rcx*4]
00AED2E8  41 83 C0 08                     add r8d, 8
00AED2EC  49 03 D4                        add rdx, r12
00AED2EF  4C 2B CB                        sub r9, rbx
00AED2F2  75 E9                           jne 0x140aed2dd
00AED2F4  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AED2FC  44 89 00                        mov dword ptr [rax], r8d
00AED2FF  44 39 84 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r8d
00AED307  0F 82 3A 01 00 00               jb 0x140aed447
00AED30D  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
00AED310  2B C3                           sub eax, ebx
00AED312  41 89 07                        mov dword ptr [r15], eax
00AED315  8B 4F 7C                        mov ecx, dword ptr [rdi + 0x7c]
00AED318  44 8B D1                        mov r10d, ecx
00AED31B  41 C1 E2 04                     shl r10d, 4
00AED31F  41 83 EA 20                     sub r10d, 0x20
00AED323  49 83 C2 18                     add r10, 0x18
00AED327  4D 03 D7                        add r10, r15
00AED32A  4D 8D 4F 08                     lea r9, [r15 + 8]
00AED32E  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
00AED335  49 03 D4                        add rdx, r12
00AED338  FF C9                           dec ecx
00AED33A  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AED342  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED347  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AED34F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED354  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00AED359  E8 82 B8 EB FF                  call 0x1409a8be0
00AED35E  E9 3E 01 00 00                  jmp 0x140aed4a1
00AED363  8B F8                           mov edi, eax
00AED365  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED36D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED371  E8 9A 26 77 FF                  call 0x14025fa10
00AED376  E8 35 05 77 FF                  call 0x14025d8b0
00AED37B  BA 53 68 72 74                  mov edx, 0x74726853
00AED380  48 8B CB                        mov rcx, rbx
00AED383  E8 58 A5 80 FF                  call 0x1402f78e0
00AED388  8B C7                           mov eax, edi
00AED38A  E9 76 31 00 00                  jmp 0x140af0505
00AED38F  8B F8                           mov edi, eax
00AED391  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED399  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED39D  E8 6E 26 77 FF                  call 0x14025fa10
00AED3A2  E8 09 05 77 FF                  call 0x14025d8b0
00AED3A7  BA 53 68 72 74                  mov edx, 0x74726853
00AED3AC  48 8B CB                        mov rcx, rbx
00AED3AF  E8 2C A5 80 FF                  call 0x1402f78e0
00AED3B4  8B C7                           mov eax, edi
00AED3B6  E9 4A 31 00 00                  jmp 0x140af0505
00AED3BB  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED3C3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED3C8  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED3D0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED3D5  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED3DD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED3E2  45 8A C5                        mov r8b, r13b
00AED3E5  BA 08 00 00 00                  mov edx, 8
00AED3EA  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
00AED3F2  E8 D9 06 90 FF                  call 0x1403edad0
00AED3F7  85 C0                           test eax, eax
00AED3F9  0F 88 06 31 00 00               js 0x140af0505
00AED3FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AED408  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AED40F  90                              nop
00AED410  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AED418  8A D3                           mov dl, bl
00AED41A  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AED41E  E8 9D 47 72 FF                  call 0x140211bc0
00AED423  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
00AED42A  48 8B 08                        mov rcx, qword ptr [rax]
00AED42D  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AED431  44 8D 04 85 18 00 00 00         lea r8d, [rax*4 + 0x18]
00AED439  45 89 04 24                     mov dword ptr [r12], r8d
00AED43D  44 39 84 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r8d
00AED445  73 25                           jae 0x140aed46c
00AED447  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AED44B  E8 C0 25 77 FF                  call 0x14025fa10
00AED450  E8 5B 04 77 FF                  call 0x14025d8b0
00AED455  48 8B CF                        mov rcx, rdi
00AED458  BA 53 68 72 74                  mov edx, 0x74726853
00AED45D  E8 7E A4 80 FF                  call 0x1402f78e0
00AED462  B8 23 00 00 C0                  mov eax, 0xc0000023
00AED467  E9 99 30 00 00                  jmp 0x140af0505
00AED46C  49 8D 47 10                     lea rax, [r15 + 0x10]
00AED470  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AED478  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AED47D  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AED485  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AED48A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED48F  4D 8B CF                        mov r9, r15
00AED492  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
00AED499  8B CB                           mov ecx, ebx
00AED49B  E8 40 B7 EB FF                  call 0x1409a8be0
00AED4A0  90                              nop
00AED4A1  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AED4A5  E8 66 25 77 FF                  call 0x14025fa10
00AED4AA  E8 01 04 77 FF                  call 0x14025d8b0
00AED4AF  48 8B CF                        mov rcx, rdi
00AED4B2  BA 53 68 72 74                  mov edx, 0x74726853
00AED4B7  E8 24 A4 80 FF                  call 0x1402f78e0
00AED4BC  33 C0                           xor eax, eax
00AED4BE  E9 42 30 00 00                  jmp 0x140af0505
00AED4C3  8B F8                           mov edi, eax
00AED4C5  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED4CD  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED4D1  E8 3A 25 77 FF                  call 0x14025fa10
00AED4D6  E8 D5 03 77 FF                  call 0x14025d8b0
00AED4DB  BA 53 68 72 74                  mov edx, 0x74726853
00AED4E0  48 8B CB                        mov rcx, rbx
00AED4E3  E8 F8 A3 80 FF                  call 0x1402f78e0
00AED4E8  8B C7                           mov eax, edi
00AED4EA  E9 16 30 00 00                  jmp 0x140af0505
00AED4EF  8B F8                           mov edi, eax
00AED4F1  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED4F9  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED4FD  E8 0E 25 77 FF                  call 0x14025fa10
00AED502  E8 A9 03 77 FF                  call 0x14025d8b0
00AED507  BA 53 68 72 74                  mov edx, 0x74726853
00AED50C  48 8B CB                        mov rcx, rbx
00AED50F  E8 CC A3 80 FF                  call 0x1402f78e0
00AED514  8B C7                           mov eax, edi
00AED516  E9 EA 2F 00 00                  jmp 0x140af0505
00AED51B  E8 48 34 A0 FF                  call 0x1404f0968
00AED520  85 C0                           test eax, eax
00AED522  0F 84 9C 02 00 00               je 0x140aed7c4
00AED528  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
00AED530  48 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdi
00AED538  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00AED540  89 BC 24 14 01 00 00            mov dword ptr [rsp + 0x114], edi
00AED547  89 BC 24 2C 01 00 00            mov dword ptr [rsp + 0x12c], edi
00AED54E  41 8A D5                        mov dl, r13b
00AED551  48 8B 0D 20 C5 4E 00            mov rcx, qword ptr [rip + 0x4ec520]
00AED558  E8 C3 48 D8 FF                  call 0x140871e20
00AED55D  84 C0                           test al, al
00AED55F  0F 84 5F 02 00 00               je 0x140aed7c4
00AED565  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED56D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED572  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED57A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED57F  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED587  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED58C  45 8A C5                        mov r8b, r13b
00AED58F  BE 08 00 00 00                  mov esi, 8
00AED594  8B D6                           mov edx, esi
00AED596  48 8B CB                        mov rcx, rbx
00AED599  E8 32 05 90 FF                  call 0x1403edad0
00AED59E  85 C0                           test eax, eax
00AED5A0  0F 88 5F 2F 00 00               js 0x140af0505
00AED5A6  41 89 34 24                     mov dword ptr [r12], esi
00AED5AA  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AED5B1  0F 85 93 0F 00 00               jne 0x140aee54a
00AED5B7  E8 2C A3 9D FF                  call 0x1404c78e8
00AED5BC  85 C0                           test eax, eax
00AED5BE  0F 84 0A 02 00 00               je 0x140aed7ce
00AED5C4  89 BC 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edi
00AED5CB  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00AED5D3  E8 D8 36 F7 FF                  call 0x140a60cb0
00AED5D8  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00AED5DF  24 18                           and al, 0x18
00AED5E1  41 BC 10 00 00 00               mov r12d, 0x10
00AED5E7  41 3A C4                        cmp al, r12b
00AED5EA  0F 85 C2 01 00 00               jne 0x140aed7b2
00AED5F0  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00AED5F8  48 8B CA                        mov rcx, rdx
00AED5FB  E8 C4 DB 98 FF                  call 0x14047b1c4
00AED600  83 F8 02                        cmp eax, 2
00AED603  0F 85 A9 01 00 00               jne 0x140aed7b2
00AED609  48 8B 92 D8 00 00 00            mov rdx, qword ptr [rdx + 0xd8]
00AED610  48 8D 4A 18                     lea rcx, [rdx + 0x18]
00AED614  8B 42 1C                        mov eax, dword ptr [rdx + 0x1c]
00AED617  0B 01                           or eax, dword ptr [rcx]
00AED619  0F 84 93 01 00 00               je 0x140aed7b2
00AED61F  4C 8D 84 24 C0 00 00 00         lea r8, [rsp + 0xc0]
00AED627  48 8B 92 A8 00 00 00            mov rdx, qword ptr [rdx + 0xa8]
00AED62E  E8 51 E1 F4 FF                  call 0x140a3b784
00AED633  8B D8                           mov ebx, eax
00AED635  85 C0                           test eax, eax
00AED637  0F 88 BC 13 00 00               js 0x140aee9f9
00AED63D  C7 84 24 10 01 00 00 30 00 00 00  mov dword ptr [rsp + 0x110], 0x30
00AED648  48 89 BC 24 18 01 00 00         mov qword ptr [rsp + 0x118], rdi
00AED650  41 F6 DD                        neg r13b
00AED653  1B C0                           sbb eax, eax
00AED655  F7 D0                           not eax
00AED657  25 00 02 00 00                  and eax, 0x200
00AED65C  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
00AED663  48 89 BC 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdi
00AED66B  0F 57 C0                        xorps xmm0, xmm0
00AED66E  F3 0F 7F 84 24 30 01 00 00      movdqu xmmword ptr [rsp + 0x130], xmm0
00AED677  48 8D 94 24 B4 00 00 00         lea rdx, [rsp + 0xb4]
00AED67F  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AED687  E8 04 6E F1 FF                  call 0x140a04490
00AED68C  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
00AED694  8B 94 24 B4 00 00 00            mov edx, dword ptr [rsp + 0xb4]
00AED69B  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
00AED69F  E8 68 48 00 00                  call 0x140af1f0c
00AED6A4  8B D8                           mov ebx, eax
00AED6A6  85 C0                           test eax, eax
00AED6A8  79 0D                           jns 0x140aed6b7
00AED6AA  48 8B CE                        mov rcx, rsi
00AED6AD  E8 1A 17 96 FF                  call 0x14044edcc
00AED6B2  E9 42 13 00 00                  jmp 0x140aee9f9
00AED6B7  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00AED6BF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AED6C4  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00AED6C9  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AED6CE  BB 01 00 00 00                  mov ebx, 1
00AED6D3  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00AED6D7  44 8B CB                        mov r9d, ebx
00AED6DA  45 33 C0                        xor r8d, r8d
00AED6DD  48 8D 94 24 10 01 00 00         lea rdx, [rsp + 0x110]
00AED6E5  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
00AED6E9  E8 FE B0 DC FF                  call 0x1408b87ec
00AED6EE  8B D8                           mov ebx, eax
00AED6F0  48 8B CE                        mov rcx, rsi
00AED6F3  E8 D4 16 96 FF                  call 0x14044edcc
00AED6F8  85 DB                           test ebx, ebx
00AED6FA  0F 88 F9 12 00 00               js 0x140aee9f9
00AED700  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00AED708  48 8B 88 D8 00 00 00            mov rcx, qword ptr [rax + 0xd8]
00AED70F  49 03 CC                        add rcx, r12
00AED712  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00AED71A  E8 2D E0 F4 FF                  call 0x140a3b74c
00AED71F  8B D8                           mov ebx, eax
00AED721  85 C0                           test eax, eax
00AED723  78 44                           js 0x140aed769
00AED725  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00AED72D  0F BA A8 C8 00 00 00 1C         bts dword ptr [rax + 0xc8], 0x1c
00AED735  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00AED73D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED742  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AED747  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AED74B  45 33 C9                        xor r9d, r9d
00AED74E  33 D2                           xor edx, edx
00AED750  41 B8 FF 01 0F 00               mov r8d, 0xf01ff
00AED756  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00AED75E  E8 3D C0 DC FF                  call 0x1408b97a0
00AED763  8B D8                           mov ebx, eax
00AED765  85 C0                           test eax, eax
00AED767  79 12                           jns 0x140aed77b
00AED769  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00AED771  E8 DA BB 80 FF                  call 0x1402f9350
00AED776  E9 7E 12 00 00                  jmp 0x140aee9f9
00AED77B  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00AED783  49 89 07                        mov qword ptr [r15], rax
00AED786  33 FF                           xor edi, edi
00AED788  EB 49                           jmp 0x140aed7d3
00AED78A  8B D8                           mov ebx, eax
00AED78C  BA 53 68 72 74                  mov edx, 0x74726853
00AED791  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AED799  E8 42 A1 80 FF                  call 0x1402f78e0
00AED79E  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00AED7A6  E8 C5 B0 D7 FF                  call 0x140868870
00AED7AB  8B C3                           mov eax, ebx
00AED7AD  E9 53 2D 00 00                  jmp 0x140af0505
00AED7B2  BA 53 68 72 74                  mov edx, 0x74726853
00AED7B7  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AED7BF  E8 1C A1 80 FF                  call 0x1402f78e0
00AED7C4  B8 03 00 00 C0                  mov eax, 0xc0000003
00AED7C9  E9 37 2D 00 00                  jmp 0x140af0505
00AED7CE  BF 03 00 00 C0                  mov edi, 0xc0000003
00AED7D3  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AED7DB  E9 F7 07 00 00                  jmp 0x140aedfd7
00AED7E0  8B D8                           mov ebx, eax
00AED7E2  BA 53 68 72 74                  mov edx, 0x74726853
00AED7E7  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AED7EF  E8 EC A0 80 FF                  call 0x1402f78e0
00AED7F4  8B C3                           mov eax, ebx
00AED7F6  E9 0A 2D 00 00                  jmp 0x140af0505
00AED7FB  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED803  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED808  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED810  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED815  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED81D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED822  45 8A C5                        mov r8b, r13b
00AED825  BE 08 00 00 00                  mov esi, 8
00AED82A  8B D6                           mov edx, esi
00AED82C  48 8B CB                        mov rcx, rbx
00AED82F  E8 9C 02 90 FF                  call 0x1403edad0
00AED834  85 C0                           test eax, eax
00AED836  0F 88 C9 2C 00 00               js 0x140af0505
00AED83C  89 B4 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], esi
00AED843  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AED84C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AED853  90                              nop
00AED854  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AED85C  8D 56 F9                        lea edx, [rsi - 7]
00AED85F  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AED863  E8 58 43 72 FF                  call 0x140211bc0
00AED868  49 8B 86 B8 00 00 00            mov rax, qword ptr [r14 + 0xb8]
00AED86F  48 85 C0                        test rax, rax
00AED872  74 0D                           je 0x140aed881
00AED874  0F B7 40 02                     movzx eax, word ptr [rax + 2]
00AED878  03 C6                           add eax, esi
00AED87A  89 84 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], eax
00AED881  8B 84 24 9C 00 00 00            mov eax, dword ptr [rsp + 0x9c]
00AED888  41 89 04 24                     mov dword ptr [r12], eax
00AED88C  8B 94 24 18 02 00 00            mov edx, dword ptr [rsp + 0x218]
00AED893  3B 94 24 9C 00 00 00            cmp edx, dword ptr [rsp + 0x9c]
00AED89A  73 16                           jae 0x140aed8b2
00AED89C  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AED8A0  E8 6B 21 77 FF                  call 0x14025fa10
00AED8A5  E8 06 00 77 FF                  call 0x14025d8b0
00AED8AA  49 8B CE                        mov rcx, r14
00AED8AD  E9 A6 FB FF FF                  jmp 0x140aed458
00AED8B2  49 8D 4F 08                     lea rcx, [r15 + 8]
00AED8B6  49 39 BE B8 00 00 00            cmp qword ptr [r14 + 0xb8], rdi
00AED8BD  74 16                           je 0x140aed8d5
00AED8BF  49 89 0F                        mov qword ptr [r15], rcx
00AED8C2  49 8B 96 B8 00 00 00            mov rdx, qword ptr [r14 + 0xb8]
00AED8C9  44 0F B7 42 02                  movzx r8d, word ptr [rdx + 2]
00AED8CE  E8 6D 8F BD FF                  call 0x1406c6840
00AED8D3  EB 03                           jmp 0x140aed8d8
00AED8D5  49 89 3F                        mov qword ptr [r15], rdi
00AED8D8  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AED8DC  E8 2F 21 77 FF                  call 0x14025fa10
00AED8E1  E8 CA FF 76 FF                  call 0x14025d8b0
00AED8E6  49 8B CE                        mov rcx, r14
00AED8E9  E9 C4 FB FF FF                  jmp 0x140aed4b2
00AED8EE  8B F8                           mov edi, eax
00AED8F0  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED8F8  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED8FC  E8 0F 21 77 FF                  call 0x14025fa10
00AED901  E8 AA FF 76 FF                  call 0x14025d8b0
00AED906  BA 53 68 72 74                  mov edx, 0x74726853
00AED90B  48 8B CB                        mov rcx, rbx
00AED90E  E8 CD 9F 80 FF                  call 0x1402f78e0
00AED913  8B C7                           mov eax, edi
00AED915  E9 EB 2B 00 00                  jmp 0x140af0505
00AED91A  8B F8                           mov edi, eax
00AED91C  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AED924  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AED928  E8 E3 20 77 FF                  call 0x14025fa10
00AED92D  E8 7E FF 76 FF                  call 0x14025d8b0
00AED932  BA 53 68 72 74                  mov edx, 0x74726853
00AED937  48 8B CB                        mov rcx, rbx
00AED93A  E8 A1 9F 80 FF                  call 0x1402f78e0
00AED93F  8B C7                           mov eax, edi
00AED941  E9 BF 2B 00 00                  jmp 0x140af0505
00AED946  41 83 EE 07                     sub r14d, 7
00AED94A  0F 84 70 04 00 00               je 0x140aeddc0
00AED950  41 83 EE 01                     sub r14d, 1
00AED954  0F 84 C5 03 00 00               je 0x140aedd1f
00AED95A  41 83 EE 01                     sub r14d, 1
00AED95E  0F 84 FE 02 00 00               je 0x140aedc62
00AED964  41 83 EE 01                     sub r14d, 1
00AED968  0F 84 8D 01 00 00               je 0x140aedafb
00AED96E  41 83 FE 01                     cmp r14d, 1
00AED972  0F 85 4C FE FF FF               jne 0x140aed7c4
00AED978  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AED980  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AED985  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AED98D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AED992  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AED99A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AED99F  45 8A C5                        mov r8b, r13b
00AED9A2  41 8D 56 07                     lea edx, [r14 + 7]
00AED9A6  48 8B CB                        mov rcx, rbx
00AED9A9  E8 22 01 90 FF                  call 0x1403edad0
00AED9AE  85 C0                           test eax, eax
00AED9B0  0F 88 4F 2B 00 00               js 0x140af0505
00AED9B6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AED9BF  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AED9C6  90                              nop
00AED9C7  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AED9CF  41 8B DE                        mov ebx, r14d
00AED9D2  8A D3                           mov dl, bl
00AED9D4  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AED9D8  E8 E3 41 72 FF                  call 0x140211bc0
00AED9DD  8B 8E 80 00 00 00               mov ecx, dword ptr [rsi + 0x80]
00AED9E3  44 8B C1                        mov r8d, ecx
00AED9E6  41 C1 E0 04                     shl r8d, 4
00AED9EA  41 83 C0 08                     add r8d, 8
00AED9EE  85 C9                           test ecx, ecx
00AED9F0  74 25                           je 0x140aeda17
00AED9F2  48 8B 96 A0 00 00 00            mov rdx, qword ptr [rsi + 0xa0]
00AED9F9  44 8B C9                        mov r9d, ecx
00AED9FC  45 8D 66 0F                     lea r12d, [r14 + 0xf]
00AEDA00  48 8B 02                        mov rax, qword ptr [rdx]
00AEDA03  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AEDA07  45 8D 04 88                     lea r8d, [r8 + rcx*4]
00AEDA0B  41 83 C0 08                     add r8d, 8
00AEDA0F  49 03 D4                        add rdx, r12
00AEDA12  4C 2B CB                        sub r9, rbx
00AEDA15  75 E9                           jne 0x140aeda00
00AEDA17  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEDA1F  44 89 00                        mov dword ptr [rax], r8d
00AEDA22  44 39 84 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r8d
00AEDA2A  73 16                           jae 0x140aeda42
00AEDA2C  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEDA30  E8 DB 1F 77 FF                  call 0x14025fa10
00AEDA35  E8 76 FE 76 FF                  call 0x14025d8b0
00AEDA3A  48 8B CE                        mov rcx, rsi
00AEDA3D  E9 16 FA FF FF                  jmp 0x140aed458
00AEDA42  8B 86 80 00 00 00               mov eax, dword ptr [rsi + 0x80]
00AEDA48  41 89 07                        mov dword ptr [r15], eax
00AEDA4B  8B 8E 80 00 00 00               mov ecx, dword ptr [rsi + 0x80]
00AEDA51  8B D1                           mov edx, ecx
00AEDA53  C1 E2 04                        shl edx, 4
00AEDA56  48 83 C2 08                     add rdx, 8
00AEDA5A  49 03 D7                        add rdx, r15
00AEDA5D  4D 8D 4F 08                     lea r9, [r15 + 8]
00AEDA61  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEDA69  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDA6E  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEDA76  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDA7B  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00AEDA80  48 8B 96 A0 00 00 00            mov rdx, qword ptr [rsi + 0xa0]
00AEDA87  E8 54 B1 EB FF                  call 0x1409a8be0
00AEDA8C  90                              nop
00AEDA8D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEDA91  E8 7A 1F 77 FF                  call 0x14025fa10
00AEDA96  E8 15 FE 76 FF                  call 0x14025d8b0
00AEDA9B  48 8B CE                        mov rcx, rsi
00AEDA9E  E9 0F FA FF FF                  jmp 0x140aed4b2
00AEDAA3  8B F8                           mov edi, eax
00AEDAA5  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEDAAD  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEDAB1  E8 5A 1F 77 FF                  call 0x14025fa10
00AEDAB6  E8 F5 FD 76 FF                  call 0x14025d8b0
00AEDABB  BA 53 68 72 74                  mov edx, 0x74726853
00AEDAC0  48 8B CB                        mov rcx, rbx
00AEDAC3  E8 18 9E 80 FF                  call 0x1402f78e0
00AEDAC8  8B C7                           mov eax, edi
00AEDACA  E9 36 2A 00 00                  jmp 0x140af0505
00AEDACF  8B F8                           mov edi, eax
00AEDAD1  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEDAD9  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEDADD  E8 2E 1F 77 FF                  call 0x14025fa10
00AEDAE2  E8 C9 FD 76 FF                  call 0x14025d8b0
00AEDAE7  BA 53 68 72 74                  mov edx, 0x74726853
00AEDAEC  48 8B CB                        mov rcx, rbx
00AEDAEF  E8 EC 9D 80 FF                  call 0x1402f78e0
00AEDAF4  8B C7                           mov eax, edi
00AEDAF6  E9 0A 2A 00 00                  jmp 0x140af0505
00AEDAFB  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEDB03  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDB08  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEDB10  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDB15  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEDB1D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEDB22  45 8A C5                        mov r8b, r13b
00AEDB25  BE 08 00 00 00                  mov esi, 8
00AEDB2A  8B D6                           mov edx, esi
00AEDB2C  48 8B CB                        mov rcx, rbx
00AEDB2F  E8 9C FF 8F FF                  call 0x1403edad0
00AEDB34  85 C0                           test eax, eax
00AEDB36  0F 88 C9 29 00 00               js 0x140af0505
00AEDB3C  41 C7 04 24 38 00 00 00         mov dword ptr [r12], 0x38
00AEDB44  83 BC 24 18 02 00 00 38         cmp dword ptr [rsp + 0x218], 0x38
00AEDB4C  0F 82 C1 02 00 00               jb 0x140aede13
00AEDB52  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEDB5B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEDB62  90                              nop
00AEDB63  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEDB6B  BB 01 00 00 00                  mov ebx, 1
00AEDB70  8A D3                           mov dl, bl
00AEDB72  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEDB76  E8 45 40 72 FF                  call 0x140211bc0
00AEDB7B  90                              nop
00AEDB7C  89 BC 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], edi
00AEDB83  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00AEDB87  49 89 07                        mov qword ptr [r15], rax
00AEDB8A  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00AEDB8E  49 89 47 08                     mov qword ptr [r15 + 8], rax
00AEDB92  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00AEDB96  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
00AEDB9A  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
00AEDBA1  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
00AEDBA5  41 8B 86 C4 00 00 00            mov eax, dword ptr [r14 + 0xc4]
00AEDBAC  41 89 47 1C                     mov dword ptr [r15 + 0x1c], eax
00AEDBB0  41 8B 86 88 00 00 00            mov eax, dword ptr [r14 + 0x88]
00AEDBB7  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
00AEDBBB  49 8B 86 A8 00 00 00            mov rax, qword ptr [r14 + 0xa8]
00AEDBC2  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AEDBC6  C1 E1 02                        shl ecx, 2
00AEDBC9  41 8B 96 88 00 00 00            mov edx, dword ptr [r14 + 0x88]
00AEDBD0  2B D1                           sub edx, ecx
00AEDBD2  2B D6                           sub edx, esi
00AEDBD4  89 94 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], edx
00AEDBDB  49 8B 86 B8 00 00 00            mov rax, qword ptr [r14 + 0xb8]
00AEDBE2  48 85 C0                        test rax, rax
00AEDBE5  74 0D                           je 0x140aedbf4
00AEDBE7  0F B7 40 02                     movzx eax, word ptr [rax + 2]
00AEDBEB  2B D0                           sub edx, eax
00AEDBED  89 94 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], edx
00AEDBF4  41 89 57 24                     mov dword ptr [r15 + 0x24], edx
00AEDBF8  41 8B 46 7C                     mov eax, dword ptr [r14 + 0x7c]
00AEDBFC  2B C3                           sub eax, ebx
00AEDBFE  41 89 47 28                     mov dword ptr [r15 + 0x28], eax
00AEDC02  49 8B CE                        mov rcx, r14
00AEDC05  E8 B6 52 94 FF                  call 0x140432ec0
00AEDC0A  41 89 47 2C                     mov dword ptr [r15 + 0x2c], eax
00AEDC0E  49 8B 46 38                     mov rax, qword ptr [r14 + 0x38]
00AEDC12  49 89 47 30                     mov qword ptr [r15 + 0x30], rax
00AEDC16  E9 BD FC FF FF                  jmp 0x140aed8d8
00AEDC1B  8B F8                           mov edi, eax
00AEDC1D  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEDC25  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEDC29  E8 E2 1D 77 FF                  call 0x14025fa10
00AEDC2E  E8 7D FC 76 FF                  call 0x14025d8b0
00AEDC33  BA 53 68 72 74                  mov edx, 0x74726853
00AEDC38  48 8B CB                        mov rcx, rbx
00AEDC3B  E8 A0 9C 80 FF                  call 0x1402f78e0
00AEDC40  8B C7                           mov eax, edi
00AEDC42  E9 BE 28 00 00                  jmp 0x140af0505
00AEDC47  8B D8                           mov ebx, eax
00AEDC49  BA 53 68 72 74                  mov edx, 0x74726853
00AEDC4E  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDC56  E8 85 9C 80 FF                  call 0x1402f78e0
00AEDC5B  8B C3                           mov eax, ebx
00AEDC5D  E9 A3 28 00 00                  jmp 0x140af0505
00AEDC62  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEDC6A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDC6F  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEDC77  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDC7C  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEDC84  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEDC89  45 8A C5                        mov r8b, r13b
00AEDC8C  BA 08 00 00 00                  mov edx, 8
00AEDC91  48 8B CB                        mov rcx, rbx
00AEDC94  E8 37 FE 8F FF                  call 0x1403edad0
00AEDC99  85 C0                           test eax, eax
00AEDC9B  0F 88 64 28 00 00               js 0x140af0505
00AEDCA1  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
00AEDCA9  41 83 B8 C0 00 00 00 02         cmp dword ptr [r8 + 0xc0], 2
00AEDCB1  74 0A                           je 0x140aedcbd
00AEDCB3  BF 03 00 00 C0                  mov edi, 0xc0000003
00AEDCB8  E9 17 03 00 00                  jmp 0x140aedfd4
00AEDCBD  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEDCC5  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEDCCD  73 08                           jae 0x140aedcd7
00AEDCCF  49 8B C8                        mov rcx, r8
00AEDCD2  E9 81 F7 FF FF                  jmp 0x140aed458
00AEDCD7  41 8B 80 C4 00 00 00            mov eax, dword ptr [r8 + 0xc4]
00AEDCDE  41 89 07                        mov dword ptr [r15], eax
00AEDCE1  49 8B C8                        mov rcx, r8
00AEDCE4  E9 C9 F7 FF FF                  jmp 0x140aed4b2
00AEDCE9  8B D8                           mov ebx, eax
00AEDCEB  BA 53 68 72 74                  mov edx, 0x74726853
00AEDCF0  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDCF8  E8 E3 9B 80 FF                  call 0x1402f78e0
00AEDCFD  8B C3                           mov eax, ebx
00AEDCFF  E9 01 28 00 00                  jmp 0x140af0505
00AEDD04  8B D8                           mov ebx, eax
00AEDD06  BA 53 68 72 74                  mov edx, 0x74726853
00AEDD0B  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDD13  E8 C8 9B 80 FF                  call 0x1402f78e0
00AEDD18  8B C3                           mov eax, ebx
00AEDD1A  E9 E6 27 00 00                  jmp 0x140af0505
00AEDD1F  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEDD27  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDD2C  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEDD34  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDD39  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEDD41  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEDD46  45 8A C5                        mov r8b, r13b
00AEDD49  BA 08 00 00 00                  mov edx, 8
00AEDD4E  48 8B CB                        mov rcx, rbx
00AEDD51  E8 7A FD 8F FF                  call 0x1403edad0
00AEDD56  85 C0                           test eax, eax
00AEDD58  0F 88 A7 27 00 00               js 0x140af0505
00AEDD5E  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEDD66  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEDD6E  0F 82 9F 00 00 00               jb 0x140aede13
00AEDD74  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDD7C  8B 81 C0 00 00 00               mov eax, dword ptr [rcx + 0xc0]
00AEDD82  41 89 07                        mov dword ptr [r15], eax
00AEDD85  E9 28 F7 FF FF                  jmp 0x140aed4b2
00AEDD8A  8B D8                           mov ebx, eax
00AEDD8C  BA 53 68 72 74                  mov edx, 0x74726853
00AEDD91  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDD99  E8 42 9B 80 FF                  call 0x1402f78e0
00AEDD9E  8B C3                           mov eax, ebx
00AEDDA0  E9 60 27 00 00                  jmp 0x140af0505
00AEDDA5  8B D8                           mov ebx, eax
00AEDDA7  BA 53 68 72 74                  mov edx, 0x74726853
00AEDDAC  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDDB4  E8 27 9B 80 FF                  call 0x1402f78e0
00AEDDB9  8B C3                           mov eax, ebx
00AEDDBB  E9 45 27 00 00                  jmp 0x140af0505
00AEDDC0  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEDDC8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDDCD  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEDDD5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDDDA  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEDDE2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEDDE7  45 8A C5                        mov r8b, r13b
00AEDDEA  41 BC 10 00 00 00               mov r12d, 0x10
00AEDDF0  41 8B D4                        mov edx, r12d
00AEDDF3  48 8B CB                        mov rcx, rbx
00AEDDF6  E8 D5 FC 8F FF                  call 0x1403edad0
00AEDDFB  85 C0                           test eax, eax
00AEDDFD  0F 88 02 27 00 00               js 0x140af0505
00AEDE03  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEDE0B  44 89 20                        mov dword ptr [rax], r12d
00AEDE0E  41 3B F4                        cmp esi, r12d
00AEDE11  73 0D                           jae 0x140aede20
00AEDE13  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDE1B  E9 38 F6 FF FF                  jmp 0x140aed458
00AEDE20  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDE28  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00AEDE2B  F3 41 0F 7F 07                  movdqu xmmword ptr [r15], xmm0
00AEDE30  E9 7D F6 FF FF                  jmp 0x140aed4b2
00AEDE35  8B D8                           mov ebx, eax
00AEDE37  BA 53 68 72 74                  mov edx, 0x74726853
00AEDE3C  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDE44  E8 97 9A 80 FF                  call 0x1402f78e0
00AEDE49  8B C3                           mov eax, ebx
00AEDE4B  E9 B5 26 00 00                  jmp 0x140af0505
00AEDE50  8B D8                           mov ebx, eax
00AEDE52  BA 53 68 72 74                  mov edx, 0x74726853
00AEDE57  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDE5F  E8 7C 9A 80 FF                  call 0x1402f78e0
00AEDE64  8B C3                           mov eax, ebx
00AEDE66  E9 9A 26 00 00                  jmp 0x140af0505
00AEDE6B  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEDE73  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDE78  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEDE80  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDE85  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEDE8D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEDE92  45 8A C5                        mov r8b, r13b
00AEDE95  BA 08 00 00 00                  mov edx, 8
00AEDE9A  48 8B CB                        mov rcx, rbx
00AEDE9D  E8 2E FC 8F FF                  call 0x1403edad0
00AEDEA2  85 C0                           test eax, eax
00AEDEA4  0F 88 5B 26 00 00               js 0x140af0505
00AEDEAA  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEDEB2  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDEBA  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEDEC2  0F 82 90 F5 FF FF               jb 0x140aed458
00AEDEC8  48 8D 94 24 B4 00 00 00         lea rdx, [rsp + 0xb4]
00AEDED0  E8 BB 65 F1 FF                  call 0x140a04490
00AEDED5  90                              nop
00AEDED6  8B 84 24 B4 00 00 00            mov eax, dword ptr [rsp + 0xb4]
00AEDEDD  41 89 07                        mov dword ptr [r15], eax
00AEDEE0  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEDEE8  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDEF0  E9 BD F5 FF FF                  jmp 0x140aed4b2
00AEDEF5  8B D8                           mov ebx, eax
00AEDEF7  BA 53 68 72 74                  mov edx, 0x74726853
00AEDEFC  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDF04  E8 D7 99 80 FF                  call 0x1402f78e0
00AEDF09  8B C3                           mov eax, ebx
00AEDF0B  E9 F5 25 00 00                  jmp 0x140af0505
00AEDF10  8B D8                           mov ebx, eax
00AEDF12  BA 53 68 72 74                  mov edx, 0x74726853
00AEDF17  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDF1F  E8 BC 99 80 FF                  call 0x1402f78e0
00AEDF24  8B C3                           mov eax, ebx
00AEDF26  E9 DA 25 00 00                  jmp 0x140af0505
00AEDF2B  41 83 FE 13                     cmp r14d, 0x13
00AEDF2F  0F 8F 30 0B 00 00               jg 0x140aeea65
00AEDF35  0F 84 90 05 00 00               je 0x140aee4cb
00AEDF3B  41 83 EE 0D                     sub r14d, 0xd
00AEDF3F  0F 84 19 03 00 00               je 0x140aee25e
00AEDF45  41 83 EE 02                     sub r14d, 2
00AEDF49  0F 84 7E 02 00 00               je 0x140aee1cd
00AEDF4F  41 83 EE 01                     sub r14d, 1
00AEDF53  0F 84 64 01 00 00               je 0x140aee0bd
00AEDF59  41 83 EE 01                     sub r14d, 1
00AEDF5D  0F 84 BB 00 00 00               je 0x140aee01e
00AEDF63  41 83 FE 01                     cmp r14d, 1
00AEDF67  0F 85 57 F8 FF FF               jne 0x140aed7c4
00AEDF6D  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEDF75  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEDF7A  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEDF82  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEDF87  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEDF8F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEDF94  45 8A C5                        mov r8b, r13b
00AEDF97  41 8D 56 07                     lea edx, [r14 + 7]
00AEDF9B  48 8B CB                        mov rcx, rbx
00AEDF9E  E8 2D FB 8F FF                  call 0x1403edad0
00AEDFA3  85 C0                           test eax, eax
00AEDFA5  0F 88 5A 25 00 00               js 0x140af0505
00AEDFAB  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEDFB3  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEDFBB  0F 82 52 FE FF FF               jb 0x140aede13
00AEDFC1  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
00AEDFC9  49 8B C8                        mov rcx, r8
00AEDFCC  E8 F3 D1 98 FF                  call 0x14047b1c4
00AEDFD1  41 89 07                        mov dword ptr [r15], eax
00AEDFD4  49 8B C8                        mov rcx, r8
00AEDFD7  BA 53 68 72 74                  mov edx, 0x74726853
00AEDFDC  E8 FF 98 80 FF                  call 0x1402f78e0
00AEDFE1  8B C7                           mov eax, edi
00AEDFE3  E9 1D 25 00 00                  jmp 0x140af0505
00AEDFE8  8B D8                           mov ebx, eax
00AEDFEA  BA 53 68 72 74                  mov edx, 0x74726853
00AEDFEF  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEDFF7  E8 E4 98 80 FF                  call 0x1402f78e0
00AEDFFC  8B C3                           mov eax, ebx
00AEDFFE  E9 02 25 00 00                  jmp 0x140af0505
00AEE003  8B D8                           mov ebx, eax
00AEE005  BA 53 68 72 74                  mov edx, 0x74726853
00AEE00A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE012  E8 C9 98 80 FF                  call 0x1402f78e0
00AEE017  8B C3                           mov eax, ebx
00AEE019  E9 E7 24 00 00                  jmp 0x140af0505
00AEE01E  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEE026  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEE02B  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEE033  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEE038  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEE040  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE045  45 8A C5                        mov r8b, r13b
00AEE048  BE 08 00 00 00                  mov esi, 8
00AEE04D  8B D6                           mov edx, esi
00AEE04F  48 8B CB                        mov rcx, rbx
00AEE052  E8 79 FA 8F FF                  call 0x1403edad0
00AEE057  85 C0                           test eax, eax
00AEE059  0F 88 A6 24 00 00               js 0x140af0505
00AEE05F  41 89 34 24                     mov dword ptr [r12], esi
00AEE063  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AEE06A  0F 82 A3 FD FF FF               jb 0x140aede13
00AEE070  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE078  48 8B 81 E0 00 00 00            mov rax, qword ptr [rcx + 0xe0]
00AEE07F  49 89 07                        mov qword ptr [r15], rax
00AEE082  E9 2B F4 FF FF                  jmp 0x140aed4b2
00AEE087  8B D8                           mov ebx, eax
00AEE089  BA 53 68 72 74                  mov edx, 0x74726853
00AEE08E  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE096  E8 45 98 80 FF                  call 0x1402f78e0
00AEE09B  8B C3                           mov eax, ebx
00AEE09D  E9 63 24 00 00                  jmp 0x140af0505
00AEE0A2  8B D8                           mov ebx, eax
00AEE0A4  BA 53 68 72 74                  mov edx, 0x74726853
00AEE0A9  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE0B1  E8 2A 98 80 FF                  call 0x1402f78e0
00AEE0B6  8B C3                           mov eax, ebx
00AEE0B8  E9 48 24 00 00                  jmp 0x140af0505
00AEE0BD  41 8A D5                        mov dl, r13b
00AEE0C0  48 8B 0D 39 BA 4E 00            mov rcx, qword ptr [rip + 0x4eba39]
00AEE0C7  E8 54 3D D8 FF                  call 0x140871e20
00AEE0CC  84 C0                           test al, al
00AEE0CE  75 0A                           jne 0x140aee0da
00AEE0D0  B8 61 00 00 C0                  mov eax, 0xc0000061
00AEE0D5  E9 2B 24 00 00                  jmp 0x140af0505
00AEE0DA  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEE0E2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEE0E7  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEE0EF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEE0F4  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEE0FC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE101  45 8A C5                        mov r8b, r13b
00AEE104  BA 08 00 00 00                  mov edx, 8
00AEE109  48 8B CB                        mov rcx, rbx
00AEE10C  E8 BF F9 8F FF                  call 0x1403edad0
00AEE111  85 C0                           test eax, eax
00AEE113  0F 88 EC 23 00 00               js 0x140af0505
00AEE119  41 C7 04 24 1F 00 00 00         mov dword ptr [r12], 0x1f
00AEE121  83 BC 24 18 02 00 00 1F         cmp dword ptr [rsp + 0x218], 0x1f
00AEE129  0F 82 E4 FC FF FF               jb 0x140aede13
00AEE12F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEE138  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEE13F  90                              nop
00AEE140  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AEE148  BA 01 00 00 00                  mov edx, 1
00AEE14D  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEE151  E8 6A 3A 72 FF                  call 0x140211bc0
00AEE156  90                              nop
00AEE157  0F 10 47 58                     movups xmm0, xmmword ptr [rdi + 0x58]
00AEE15B  41 0F 11 07                     movups xmmword ptr [r15], xmm0
00AEE15F  F2 0F 10 4F 68                  movsd xmm1, qword ptr [rdi + 0x68]
00AEE164  F2 41 0F 11 4F 10               movsd qword ptr [r15 + 0x10], xmm1
00AEE16A  8B 47 70                        mov eax, dword ptr [rdi + 0x70]
00AEE16D  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
00AEE171  0F B7 47 74                     movzx eax, word ptr [rdi + 0x74]
00AEE175  66 41 89 47 1C                  mov word ptr [r15 + 0x1c], ax
00AEE17A  8A 47 76                        mov al, byte ptr [rdi + 0x76]
00AEE17D  41 88 47 1E                     mov byte ptr [r15 + 0x1e], al
00AEE181  E9 1B F3 FF FF                  jmp 0x140aed4a1
00AEE186  8B F8                           mov edi, eax
00AEE188  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEE190  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEE194  E8 77 18 77 FF                  call 0x14025fa10
00AEE199  E8 12 F7 76 FF                  call 0x14025d8b0
00AEE19E  BA 53 68 72 74                  mov edx, 0x74726853
00AEE1A3  48 8B CB                        mov rcx, rbx
00AEE1A6  E8 35 97 80 FF                  call 0x1402f78e0
00AEE1AB  8B C7                           mov eax, edi
00AEE1AD  E9 53 23 00 00                  jmp 0x140af0505
00AEE1B2  8B D8                           mov ebx, eax
00AEE1B4  BA 53 68 72 74                  mov edx, 0x74726853
00AEE1B9  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE1C1  E8 1A 97 80 FF                  call 0x1402f78e0
00AEE1C6  8B C3                           mov eax, ebx
00AEE1C8  E9 38 23 00 00                  jmp 0x140af0505
00AEE1CD  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEE1D5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEE1DA  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEE1E2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEE1E7  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEE1EF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE1F4  45 8A C5                        mov r8b, r13b
00AEE1F7  BA 08 00 00 00                  mov edx, 8
00AEE1FC  48 8B CB                        mov rcx, rbx
00AEE1FF  E8 CC F8 8F FF                  call 0x1403edad0
00AEE204  85 C0                           test eax, eax
00AEE206  0F 88 F9 22 00 00               js 0x140af0505
00AEE20C  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEE214  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEE21C  0F 82 40 F2 FF FF               jb 0x140aed462
00AEE222  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE22A  8B 81 C8 00 00 00               mov eax, dword ptr [rcx + 0xc8]
00AEE230  C1 E8 06                        shr eax, 6
00AEE233  83 E0 01                        and eax, 1
00AEE236  41 89 07                        mov dword ptr [r15], eax
00AEE239  E9 74 F2 FF FF                  jmp 0x140aed4b2
00AEE23E  8B D8                           mov ebx, eax
00AEE240  BA 53 68 72 74                  mov edx, 0x74726853
00AEE245  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE24D  E8 8E 96 80 FF                  call 0x1402f78e0
00AEE252  8B C3                           mov eax, ebx
00AEE254  E9 AC 22 00 00                  jmp 0x140af0505
00AEE259  E9 A7 22 00 00                  jmp 0x140af0505
00AEE25E  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEE266  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEE26B  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEE273  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEE278  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEE280  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE285  45 8A C5                        mov r8b, r13b
00AEE288  BA 08 00 00 00                  mov edx, 8
00AEE28D  48 8B CB                        mov rcx, rbx
00AEE290  E8 3B F8 8F FF                  call 0x1403edad0
00AEE295  85 C0                           test eax, eax
00AEE297  0F 88 68 22 00 00               js 0x140af0505
00AEE29D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEE2A6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEE2AD  90                              nop
00AEE2AE  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEE2B6  BB 01 00 00 00                  mov ebx, 1
00AEE2BB  8A D3                           mov dl, bl
00AEE2BD  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEE2C1  E8 FA 38 72 FF                  call 0x140211bc0
00AEE2C6  48 8B CE                        mov rcx, rsi
00AEE2C9  E8 F2 4B 94 FF                  call 0x140432ec0
00AEE2CE  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00AEE2D5  44 8D 1C 40                     lea r11d, [rax + rax*2]
00AEE2D9  41 C1 E3 02                     shl r11d, 2
00AEE2DD  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
00AEE2E0  44 8B D1                        mov r10d, ecx
00AEE2E3  41 C1 E2 04                     shl r10d, 4
00AEE2E7  45 8B C2                        mov r8d, r10d
00AEE2EA  44 8D 63 0F                     lea r12d, [rbx + 0xf]
00AEE2EE  85 C9                           test ecx, ecx
00AEE2F0  74 26                           je 0x140aee318
00AEE2F2  48 8B 96 98 00 00 00            mov rdx, qword ptr [rsi + 0x98]
00AEE2F9  44 8B C9                        mov r9d, ecx
00AEE2FC  48 8B 02                        mov rax, qword ptr [rdx]
00AEE2FF  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AEE303  8D 0C 8D 0F 00 00 00            lea ecx, [rcx*4 + 0xf]
00AEE30A  83 E1 F8                        and ecx, 0xfffffff8
00AEE30D  44 03 C1                        add r8d, ecx
00AEE310  49 03 D4                        add rdx, r12
00AEE313  4C 2B CB                        sub r9, rbx
00AEE316  75 E4                           jne 0x140aee2fc
00AEE318  8B 86 80 00 00 00               mov eax, dword ptr [rsi + 0x80]
00AEE31E  44 8B E8                        mov r13d, eax
00AEE321  41 C1 E5 04                     shl r13d, 4
00AEE325  45 8B F5                        mov r14d, r13d
00AEE328  41 8B CD                        mov ecx, r13d
00AEE32B  85 C0                           test eax, eax
00AEE32D  74 29                           je 0x140aee358
00AEE32F  48 8B 96 A0 00 00 00            mov rdx, qword ptr [rsi + 0xa0]
00AEE336  44 8B C8                        mov r9d, eax
00AEE339  48 8B 02                        mov rax, qword ptr [rdx]
00AEE33C  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AEE340  8D 0C 8D 0F 00 00 00            lea ecx, [rcx*4 + 0xf]
00AEE347  83 E1 F8                        and ecx, 0xfffffff8
00AEE34A  44 03 F1                        add r14d, ecx
00AEE34D  41 8B CE                        mov ecx, r14d
00AEE350  49 03 D4                        add rdx, r12
00AEE353  4C 2B CB                        sub r9, rbx
00AEE356  75 E1                           jne 0x140aee339
00AEE358  83 C1 38                        add ecx, 0x38
00AEE35B  41 03 CB                        add ecx, r11d
00AEE35E  41 03 C8                        add ecx, r8d
00AEE361  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEE369  89 08                           mov dword ptr [rax], ecx
00AEE36B  39 8C 24 18 02 00 00            cmp dword ptr [rsp + 0x218], ecx
00AEE372  0F 82 B4 F6 FF FF               jb 0x140aeda2c
00AEE378  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00AEE37C  49 89 47 30                     mov qword ptr [r15 + 0x30], rax
00AEE380  45 89 47 04                     mov dword ptr [r15 + 4], r8d
00AEE384  8B 46 7C                        mov eax, dword ptr [rsi + 0x7c]
00AEE387  41 89 07                        mov dword ptr [r15], eax
00AEE38A  4D 8D 4F 38                     lea r9, [r15 + 0x38]
00AEE38E  4D 89 4F 08                     mov qword ptr [r15 + 8], r9
00AEE392  45 89 77 14                     mov dword ptr [r15 + 0x14], r14d
00AEE396  8B 86 80 00 00 00               mov eax, dword ptr [rsi + 0x80]
00AEE39C  41 89 47 10                     mov dword ptr [r15 + 0x10], eax
00AEE3A0  39 BE 80 00 00 00               cmp dword ptr [rsi + 0x80], edi
00AEE3A6  74 14                           je 0x140aee3bc
00AEE3A8  41 8B D8                        mov ebx, r8d
00AEE3AB  48 83 C3 07                     add rbx, 7
00AEE3AF  48 83 E3 F8                     and rbx, 0xfffffffffffffff8
00AEE3B3  49 03 D9                        add rbx, r9
00AEE3B6  49 89 5F 18                     mov qword ptr [r15 + 0x18], rbx
00AEE3BA  EB 0C                           jmp 0x140aee3c8
00AEE3BC  49 89 7F 18                     mov qword ptr [r15 + 0x18], rdi
00AEE3C0  48 8B 9C 24 70 01 00 00         mov rbx, qword ptr [rsp + 0x170]
00AEE3C8  45 89 5F 24                     mov dword ptr [r15 + 0x24], r11d
00AEE3CC  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00AEE3D3  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
00AEE3D7  41 8B C6                        mov eax, r14d
00AEE3DA  45 8B E0                        mov r12d, r8d
00AEE3DD  49 03 C1                        add rax, r9
00AEE3E0  4C 03 E0                        add r12, rax
00AEE3E3  4D 89 67 28                     mov qword ptr [r15 + 0x28], r12
00AEE3E7  41 8B C2                        mov eax, r10d
00AEE3EA  49 03 C1                        add rax, r9
00AEE3ED  45 2B C2                        sub r8d, r10d
00AEE3F0  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AEE3F8  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AEE3FD  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AEE405  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AEE40A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE40F  48 8B 96 98 00 00 00            mov rdx, qword ptr [rsi + 0x98]
00AEE416  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
00AEE419  E8 C2 A7 EB FF                  call 0x1409a8be0
00AEE41E  41 8B C5                        mov eax, r13d
00AEE421  48 03 C3                        add rax, rbx
00AEE424  48 85 DB                        test rbx, rbx
00AEE427  74 3A                           je 0x140aee463
00AEE429  45 2B F5                        sub r14d, r13d
00AEE42C  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AEE434  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AEE439  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AEE441  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AEE446  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE44B  4C 8B CB                        mov r9, rbx
00AEE44E  45 8B C6                        mov r8d, r14d
00AEE451  48 8B 96 A0 00 00 00            mov rdx, qword ptr [rsi + 0xa0]
00AEE458  8B 8E 80 00 00 00               mov ecx, dword ptr [rsi + 0x80]
00AEE45E  E8 7D A7 EB FF                  call 0x1409a8be0
00AEE463  49 8B D4                        mov rdx, r12
00AEE466  48 8B CE                        mov rcx, rsi
00AEE469  E8 02 C4 93 FF                  call 0x14042a870
00AEE46E  E9 1A F6 FF FF                  jmp 0x140aeda8d
00AEE473  8B F8                           mov edi, eax
00AEE475  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEE47D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEE481  E8 8A 15 77 FF                  call 0x14025fa10
00AEE486  E8 25 F4 76 FF                  call 0x14025d8b0
00AEE48B  BA 53 68 72 74                  mov edx, 0x74726853
00AEE490  48 8B CB                        mov rcx, rbx
00AEE493  E8 48 94 80 FF                  call 0x1402f78e0
00AEE498  8B C7                           mov eax, edi
00AEE49A  E9 66 20 00 00                  jmp 0x140af0505
00AEE49F  8B F8                           mov edi, eax
00AEE4A1  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEE4A9  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEE4AD  E8 5E 15 77 FF                  call 0x14025fa10
00AEE4B2  E8 F9 F3 76 FF                  call 0x14025d8b0
00AEE4B7  BA 53 68 72 74                  mov edx, 0x74726853
00AEE4BC  48 8B CB                        mov rcx, rbx
00AEE4BF  E8 1C 94 80 FF                  call 0x1402f78e0
00AEE4C4  8B C7                           mov eax, edi
00AEE4C6  E9 3A 20 00 00                  jmp 0x140af0505
00AEE4CB  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00AEE4D3  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
00AEE4DB  48 89 BC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdi
00AEE4E3  89 BC 24 8C 01 00 00            mov dword ptr [rsp + 0x18c], edi
00AEE4EA  89 BC 24 A4 01 00 00            mov dword ptr [rsp + 0x1a4], edi
00AEE4F1  44 8A F7                        mov r14b, dil
00AEE4F4  40 88 BC 24 98 00 00 00         mov byte ptr [rsp + 0x98], dil
00AEE4FC  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEE504  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEE509  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEE511  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEE516  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEE51E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE523  45 8A C5                        mov r8b, r13b
00AEE526  BE 08 00 00 00                  mov esi, 8
00AEE52B  8B D6                           mov edx, esi
00AEE52D  48 8B CB                        mov rcx, rbx
00AEE530  E8 9B F5 8F FF                  call 0x1403edad0
00AEE535  85 C0                           test eax, eax
00AEE537  0F 88 C8 1F 00 00               js 0x140af0505
00AEE53D  41 89 34 24                     mov dword ptr [r12], esi
00AEE541  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AEE548  74 0A                           je 0x140aee554
00AEE54A  BB 04 00 00 C0                  mov ebx, 0xc0000004
00AEE54F  E9 A5 04 00 00                  jmp 0x140aee9f9
00AEE554  E8 8F 93 9D FF                  call 0x1404c78e8
00AEE559  85 C0                           test eax, eax
00AEE55B  74 32                           je 0x140aee58f
00AEE55D  89 BC 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edi
00AEE564  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00AEE56C  E8 3F 27 F7 FF                  call 0x140a60cb0
00AEE571  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00AEE578  24 18                           and al, 0x18
00AEE57A  41 BC 10 00 00 00               mov r12d, 0x10
00AEE580  41 3A C4                        cmp al, r12b
00AEE583  41 0F 94 C6                     sete r14b
00AEE587  44 88 B4 24 98 00 00 00         mov byte ptr [rsp + 0x98], r14b
00AEE58F  41 8A D5                        mov dl, r13b
00AEE592  48 8B 0D DF B4 4E 00            mov rcx, qword ptr [rip + 0x4eb4df]
00AEE599  E8 82 38 D8 FF                  call 0x140871e20
00AEE59E  8A D8                           mov bl, al
00AEE5A0  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00AEE5A7  8A C8                           mov cl, al
00AEE5A9  F6 D9                           neg cl
00AEE5AB  1B C0                           sbb eax, eax
00AEE5AD  83 C0 02                        add eax, 2
00AEE5B0  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00AEE5B7  E8 2C 93 9D FF                  call 0x1404c78e8
00AEE5BC  85 C0                           test eax, eax
00AEE5BE  0F 84 62 01 00 00               je 0x140aee726
00AEE5C4  45 84 F6                        test r14b, r14b
00AEE5C7  0F 84 59 01 00 00               je 0x140aee726
00AEE5CD  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEE5D5  49 8B CE                        mov rcx, r14
00AEE5D8  E8 E7 CB 98 FF                  call 0x14047b1c4
00AEE5DD  83 F8 03                        cmp eax, 3
00AEE5E0  0F 85 40 01 00 00               jne 0x140aee726
00AEE5E6  49 8B 8E D8 00 00 00            mov rcx, qword ptr [r14 + 0xd8]
00AEE5ED  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00AEE5F0  0B 41 10                        or eax, dword ptr [rcx + 0x10]
00AEE5F3  0F 85 2D 01 00 00               jne 0x140aee726
00AEE5F9  48 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdi
00AEE601  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
00AEE609  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AEE60D  E8 92 67 C1 FF                  call 0x140704da4
00AEE612  85 C0                           test eax, eax
00AEE614  0F 88 DD 03 00 00               js 0x140aee9f7
00AEE61A  4C 8B 05 FF 99 4E 00            mov r8, qword ptr [rip + 0x4e99ff]
00AEE621  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
00AEE629  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AEE62E  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
00AEE636  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEE63B  45 33 C9                        xor r9d, r9d
00AEE63E  8B D6                           mov edx, esi
00AEE640  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00AEE648  E8 63 A7 D7 FF                  call 0x140868db0
00AEE64D  8B D8                           mov ebx, eax
00AEE64F  33 D2                           xor edx, edx
00AEE651  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00AEE659  E8 12 32 DB FF                  call 0x1408a1870
00AEE65E  85 DB                           test ebx, ebx
00AEE660  0F 88 93 03 00 00               js 0x140aee9f9
00AEE666  49 8B 96 D8 00 00 00            mov rdx, qword ptr [r14 + 0xd8]
00AEE66D  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00AEE675  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00AEE679  4C 8D 84 24 A0 00 00 00         lea r8, [rsp + 0xa0]
00AEE681  48 8B 92 A8 00 00 00            mov rdx, qword ptr [rdx + 0xa8]
00AEE688  E8 F7 D0 F4 FF                  call 0x140a3b784
00AEE68D  44 8B E0                        mov r12d, eax
00AEE690  48 8B CB                        mov rcx, rbx
00AEE693  E8 B8 AC 80 FF                  call 0x1402f9350
00AEE698  45 85 E4                        test r12d, r12d
00AEE69B  79 08                           jns 0x140aee6a5
00AEE69D  41 8B DC                        mov ebx, r12d
00AEE6A0  E9 54 03 00 00                  jmp 0x140aee9f9
00AEE6A5  48 8D 94 24 B4 00 00 00         lea rdx, [rsp + 0xb4]
00AEE6AD  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEE6B5  E8 D6 5D F1 FF                  call 0x140a04490
00AEE6BA  8B 94 24 B4 00 00 00            mov edx, dword ptr [rsp + 0xb4]
00AEE6C1  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00AEE6C9  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00AEE6CD  E8 3A 38 00 00                  call 0x140af1f0c
00AEE6D2  44 8B E0                        mov r12d, eax
00AEE6D5  85 C0                           test eax, eax
00AEE6D7  79 0A                           jns 0x140aee6e3
00AEE6D9  48 8B CB                        mov rcx, rbx
00AEE6DC  E8 EB 06 96 FF                  call 0x14044edcc
00AEE6E1  EB BA                           jmp 0x140aee69d
00AEE6E3  49 8B 86 D8 00 00 00            mov rax, qword ptr [r14 + 0xd8]
00AEE6EA  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AEE6EE  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00AEE6F6  48 89 4B 10                     mov qword ptr [rbx + 0x10], rcx
00AEE6FA  49 8B 8E D8 00 00 00            mov rcx, qword ptr [r14 + 0xd8]
00AEE701  48 03 CE                        add rcx, rsi
00AEE704  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
00AEE70C  E8 3B D0 F4 FF                  call 0x140a3b74c
00AEE711  8B F0                           mov esi, eax
00AEE713  85 C0                           test eax, eax
00AEE715  79 3F                           jns 0x140aee756
00AEE717  48 8B CB                        mov rcx, rbx
00AEE71A  E8 AD 06 96 FF                  call 0x14044edcc
00AEE71F  8B DE                           mov ebx, esi
00AEE721  E9 D3 02 00 00                  jmp 0x140aee9f9
00AEE726  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00AEE72E  48 8B 90 D8 00 00 00            mov rdx, qword ptr [rax + 0xd8]
00AEE735  48 8D 4A 10                     lea rcx, [rdx + 0x10]
00AEE739  4C 8D 84 24 A0 00 00 00         lea r8, [rsp + 0xa0]
00AEE741  48 8B 92 A8 00 00 00            mov rdx, qword ptr [rdx + 0xa8]
00AEE748  E8 37 D0 F4 FF                  call 0x140a3b784
00AEE74D  85 C0                           test eax, eax
00AEE74F  79 0C                           jns 0x140aee75d
00AEE751  E9 A1 02 00 00                  jmp 0x140aee9f7
00AEE756  8A 9C 24 80 00 00 00            mov bl, byte ptr [rsp + 0x80]
00AEE75D  8B F7                           mov esi, edi
00AEE75F  E8 84 91 9D FF                  call 0x1404c78e8
00AEE764  85 C0                           test eax, eax
00AEE766  0F 84 BC 01 00 00               je 0x140aee928
00AEE76C  40 38 BC 24 98 00 00 00         cmp byte ptr [rsp + 0x98], dil
00AEE774  0F 84 AE 01 00 00               je 0x140aee928
00AEE77A  84 DB                           test bl, bl
00AEE77C  0F 85 A6 01 00 00               jne 0x140aee928
00AEE782  44 8B F7                        mov r14d, edi
00AEE785  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00AEE78D  48 8B 88 D8 00 00 00            mov rcx, qword ptr [rax + 0xd8]
00AEE794  48 8B 71 38                     mov rsi, qword ptr [rcx + 0x38]
00AEE798  BB 01 00 00 00                  mov ebx, 1
00AEE79D  48 85 F6                        test rsi, rsi
00AEE7A0  74 31                           je 0x140aee7d3
00AEE7A2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEE7AB  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEE7B2  90                              nop
00AEE7B3  8A D3                           mov dl, bl
00AEE7B5  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEE7B9  E8 02 34 72 FF                  call 0x140211bc0
00AEE7BE  44 8B B6 C8 00 00 00            mov r14d, dword ptr [rsi + 0xc8]
00AEE7C5  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEE7C9  E8 42 12 77 FF                  call 0x14025fa10
00AEE7CE  E8 DD F0 76 FF                  call 0x14025d8b0
00AEE7D3  8B F7                           mov esi, edi
00AEE7D5  41 0F BA E6 1B                  bt r14d, 0x1b
00AEE7DA  0F 83 4D 01 00 00               jae 0x140aee92d
00AEE7E0  44 8B E7                        mov r12d, edi
00AEE7E3  0F 57 C0                        xorps xmm0, xmm0
00AEE7E6  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
00AEE7EE  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
00AEE7F6  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00AEE7FE  E8 1D D0 D7 FF                  call 0x14086b820
00AEE803  4C 8B B4 24 20 01 00 00         mov r14, qword ptr [rsp + 0x120]
00AEE80B  49 8B 86 D8 00 00 00            mov rax, qword ptr [r14 + 0xd8]
00AEE812  48 8B 70 38                     mov rsi, qword ptr [rax + 0x38]
00AEE816  48 85 F6                        test rsi, rsi
00AEE819  74 39                           je 0x140aee854
00AEE81B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEE824  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEE82B  90                              nop
00AEE82C  8A D3                           mov dl, bl
00AEE82E  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEE832  E8 89 33 72 FF                  call 0x140211bc0
00AEE837  44 8B A6 C8 00 00 00            mov r12d, dword ptr [rsi + 0xc8]
00AEE83E  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEE842  E8 C9 11 77 FF                  call 0x14025fa10
00AEE847  E8 64 F0 76 FF                  call 0x14025d8b0
00AEE84C  4C 8B B4 24 20 01 00 00         mov r14, qword ptr [rsp + 0x120]
00AEE854  8B F7                           mov esi, edi
00AEE856  41 0F BA E4 1B                  bt r12d, 0x1b
00AEE85B  0F 83 B8 00 00 00               jae 0x140aee919
00AEE861  49 8B 96 98 00 00 00            mov rdx, qword ptr [r14 + 0x98]
00AEE868  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00AEE870  48 8B 88 98 00 00 00            mov rcx, qword ptr [rax + 0x98]
00AEE877  48 8B 12                        mov rdx, qword ptr [rdx]
00AEE87A  48 8B 09                        mov rcx, qword ptr [rcx]
00AEE87D  E8 4E 22 91 FF                  call 0x140400ad0
00AEE882  84 C0                           test al, al
00AEE884  0F 84 8F 00 00 00               je 0x140aee919
00AEE88A  0F 57 C0                        xorps xmm0, xmm0
00AEE88D  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
00AEE895  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
00AEE89D  49 8B CE                        mov rcx, r14
00AEE8A0  E8 4F B4 92 FF                  call 0x140419cf4
00AEE8A5  83 BC 24 F0 00 00 00 60         cmp dword ptr [rsp + 0xf0], 0x60
00AEE8AD  75 6A                           jne 0x140aee919
00AEE8AF  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00AEE8B7  E8 54 A6 97 FF                  call 0x140468f10
00AEE8BC  38 18                           cmp byte ptr [rax], bl
00AEE8BE  75 59                           jne 0x140aee919
00AEE8C0  33 D2                           xor edx, edx
00AEE8C2  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00AEE8CA  E8 41 84 96 FF                  call 0x140456d10
00AEE8CF  81 38 00 30 00 00               cmp dword ptr [rax], 0x3000
00AEE8D5  75 42                           jne 0x140aee919
00AEE8D7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEE8E0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AEE8E7  4C 8B B1 50 03 00 00            mov r14, qword ptr [rcx + 0x350]
00AEE8EE  8B CE                           mov ecx, esi
00AEE8F0  48 C1 E1 04                     shl rcx, 4
00AEE8F4  48 8D 05 E5 CE 51 FF            lea rax, [rip - 0xae311b]
00AEE8FB  48 03 C8                        add rcx, rax
00AEE8FE  44 8A C3                        mov r8b, bl
00AEE901  49 8B D6                        mov rdx, r14
00AEE904  E8 77 BE C9 FF                  call 0x14078a780
00AEE909  84 C0                           test al, al
00AEE90B  75 0A                           jne 0x140aee917
00AEE90D  03 F3                           add esi, ebx
00AEE90F  3B F3                           cmp esi, ebx
00AEE911  72 DB                           jb 0x140aee8ee
00AEE913  8B F7                           mov esi, edi
00AEE915  EB 02                           jmp 0x140aee919
00AEE917  8B F3                           mov esi, ebx
00AEE919  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00AEE921  E8 EA CD D7 FF                  call 0x14086b710
00AEE926  EB 05                           jmp 0x140aee92d
00AEE928  BB 01 00 00 00                  mov ebx, 1
00AEE92D  C7 84 24 88 01 00 00 30 00 00 00  mov dword ptr [rsp + 0x188], 0x30
00AEE938  48 89 BC 24 90 01 00 00         mov qword ptr [rsp + 0x190], rdi
00AEE940  41 F6 DD                        neg r13b
00AEE943  1B C0                           sbb eax, eax
00AEE945  F7 D0                           not eax
00AEE947  25 00 02 00 00                  and eax, 0x200
00AEE94C  89 84 24 A0 01 00 00            mov dword ptr [rsp + 0x1a0], eax
00AEE953  48 89 BC 24 98 01 00 00         mov qword ptr [rsp + 0x198], rdi
00AEE95B  0F 57 C0                        xorps xmm0, xmm0
00AEE95E  F3 0F 7F 84 24 A8 01 00 00      movdqu xmmword ptr [rsp + 0x1a8], xmm0
00AEE967  E8 7C 8F 9D FF                  call 0x1404c78e8
00AEE96C  85 C0                           test eax, eax
00AEE96E  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00AEE976  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00AEE97A  74 03                           je 0x140aee97f
00AEE97C  8D 5E 01                        lea ebx, [rsi + 1]
00AEE97F  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00AEE987  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AEE98C  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00AEE991  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AEE996  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00AEE99A  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
00AEE9A2  45 33 C0                        xor r8d, r8d
00AEE9A5  48 8D 94 24 88 01 00 00         lea rdx, [rsp + 0x188]
00AEE9AD  E8 3A 9E DC FF                  call 0x1408b87ec
00AEE9B2  8B D8                           mov ebx, eax
00AEE9B4  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00AEE9BC  E8 0B 04 96 FF                  call 0x14044edcc
00AEE9C1  85 DB                           test ebx, ebx
00AEE9C3  78 34                           js 0x140aee9f9
00AEE9C5  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00AEE9CD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEE9D2  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AEE9D7  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AEE9DB  45 33 C9                        xor r9d, r9d
00AEE9DE  33 D2                           xor edx, edx
00AEE9E0  41 B8 FF 01 0F 00               mov r8d, 0xf01ff
00AEE9E6  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00AEE9EE  E8 AD AD DC FF                  call 0x1408b97a0
00AEE9F3  85 C0                           test eax, eax
00AEE9F5  79 1B                           jns 0x140aeea12
00AEE9F7  8B D8                           mov ebx, eax
00AEE9F9  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEEA01  BA 53 68 72 74                  mov edx, 0x74726853
00AEEA06  E8 D5 8E 80 FF                  call 0x1402f78e0
00AEEA0B  8B C3                           mov eax, ebx
00AEEA0D  E9 F3 1A 00 00                  jmp 0x140af0505
00AEEA12  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00AEEA1A  49 89 07                        mov qword ptr [r15], rax
00AEEA1D  E9 C6 F4 FF FF                  jmp 0x140aedee8
00AEEA22  8B D8                           mov ebx, eax
00AEEA24  BA 53 68 72 74                  mov edx, 0x74726853
00AEEA29  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEEA31  E8 AA 8E 80 FF                  call 0x1402f78e0
00AEEA36  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00AEEA3E  E8 2D 9E D7 FF                  call 0x140868870
00AEEA43  8B C3                           mov eax, ebx
00AEEA45  E9 BB 1A 00 00                  jmp 0x140af0505
00AEEA4A  8B D8                           mov ebx, eax
00AEEA4C  BA 53 68 72 74                  mov edx, 0x74726853
00AEEA51  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEEA59  E8 82 8E 80 FF                  call 0x1402f78e0
00AEEA5E  8B C3                           mov eax, ebx
00AEEA60  E9 A0 1A 00 00                  jmp 0x140af0505
00AEEA65  41 8B CE                        mov ecx, r14d
00AEEA68  83 E9 14                        sub ecx, 0x14
00AEEA6B  0F 84 49 03 00 00               je 0x140aeedba
00AEEA71  83 E9 01                        sub ecx, 1
00AEEA74  0F 84 98 02 00 00               je 0x140aeed12
00AEEA7A  83 E9 01                        sub ecx, 1
00AEEA7D  74 6D                           je 0x140aeeaec
00AEEA7F  83 E9 01                        sub ecx, 1
00AEEA82  74 09                           je 0x140aeea8d
00AEEA84  83 F9 01                        cmp ecx, 1
00AEEA87  0F 85 37 ED FF FF               jne 0x140aed7c4
00AEEA8D  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEEA95  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEEA9A  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEEAA2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEEAA7  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEEAAF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEEAB4  45 8A C5                        mov r8b, r13b
00AEEAB7  BA 08 00 00 00                  mov edx, 8
00AEEABC  48 8B CB                        mov rcx, rbx
00AEEABF  E8 0C F0 8F FF                  call 0x1403edad0
00AEEAC4  85 C0                           test eax, eax
00AEEAC6  0F 88 39 1A 00 00               js 0x140af0505
00AEEACC  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEEAD4  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEEADC  0F 83 D1 18 00 00               jae 0x140af03b3
00AEEAE2  BF 23 00 00 C0                  mov edi, 0xc0000023
00AEEAE7  E9 E7 EC FF FF                  jmp 0x140aed7d3
00AEEAEC  89 BC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edi
00AEEAF3  89 BC 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edi
00AEEAFA  89 BC 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], edi
00AEEB01  89 BC 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edi
00AEEB08  89 BC 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edi
00AEEB0F  89 BC 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edi
00AEEB16  89 BC 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edi
00AEEB1D  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEEB25  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEEB2A  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEEB32  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEEB37  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEEB3F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEEB44  45 8A C5                        mov r8b, r13b
00AEEB47  BA 08 00 00 00                  mov edx, 8
00AEEB4C  48 8B CB                        mov rcx, rbx
00AEEB4F  E8 7C EF 8F FF                  call 0x1403edad0
00AEEB54  85 C0                           test eax, eax
00AEEB56  0F 88 A9 19 00 00               js 0x140af0505
00AEEB5C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEEB65  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEEB6C  90                              nop
00AEEB6D  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AEEB75  BA 01 00 00 00                  mov edx, 1
00AEEB7A  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEEB7E  E8 3D 30 72 FF                  call 0x140211bc0
00AEEB83  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00AEEB8B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AEEB90  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
00AEEB98  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AEEB9D  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00AEEBA5  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AEEBAA  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
00AEEBB2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AEEBB7  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00AEEBBF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AEEBC4  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00AEEBCC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AEEBD1  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
00AEEBD9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEEBDE  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00AEEBE6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEEBEB  48 8D 84 24 FC 00 00 00         lea rax, [rsp + 0xfc]
00AEEBF3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEEBF8  4C 8D 8C 24 B8 00 00 00         lea r9, [rsp + 0xb8]
00AEEC00  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00AEEC08  4C 8B C3                        mov r8, rbx
00AEEC0B  40 8A B4 24 80 00 00 00         mov sil, byte ptr [rsp + 0x80]
00AEEC13  40 8A D6                        mov dl, sil
00AEEC16  48 8B CF                        mov rcx, rdi
00AEEC19  E8 3E AD EF FF                  call 0x1409e995c
00AEEC1E  90                              nop
00AEEC1F  41 89 04 24                     mov dword ptr [r12], eax
00AEEC23  8B 94 24 18 02 00 00            mov edx, dword ptr [rsp + 0x218]
00AEEC2A  3B D0                           cmp edx, eax
00AEEC2C  0F 82 15 E8 FF FF               jb 0x140aed447
00AEEC32  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00AEEC37  40 88 74 24 68                  mov byte ptr [rsp + 0x68], sil
00AEEC3C  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00AEEC43  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00AEEC47  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00AEEC4E  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AEEC52  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00AEEC59  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AEEC5D  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00AEEC64  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AEEC68  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00AEEC6F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00AEEC73  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
00AEEC7A  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AEEC7E  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00AEEC85  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AEEC89  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00AEEC90  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AEEC94  8B 84 24 FC 00 00 00            mov eax, dword ptr [rsp + 0xfc]
00AEEC9B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AEEC9F  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
00AEECA7  44 8B C2                        mov r8d, edx
00AEECAA  49 8B D7                        mov rdx, r15
00AEECAD  48 8B CF                        mov rcx, rdi
00AEECB0  E8 57 AF EF FF                  call 0x1409e9c0c
00AEECB5  E9 E7 E7 FF FF                  jmp 0x140aed4a1
00AEECBA  8B F8                           mov edi, eax
00AEECBC  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEECC4  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEECC8  E8 43 0D 77 FF                  call 0x14025fa10
00AEECCD  E8 DE EB 76 FF                  call 0x14025d8b0
00AEECD2  BA 53 68 72 74                  mov edx, 0x74726853
00AEECD7  48 8B CB                        mov rcx, rbx
00AEECDA  E8 01 8C 80 FF                  call 0x1402f78e0
00AEECDF  8B C7                           mov eax, edi
00AEECE1  E9 1F 18 00 00                  jmp 0x140af0505
00AEECE6  8B F8                           mov edi, eax
00AEECE8  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEECF0  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEECF4  E8 17 0D 77 FF                  call 0x14025fa10
00AEECF9  E8 B2 EB 76 FF                  call 0x14025d8b0
00AEECFE  BA 53 68 72 74                  mov edx, 0x74726853
00AEED03  48 8B CB                        mov rcx, rbx
00AEED06  E8 D5 8B 80 FF                  call 0x1402f78e0
00AEED0B  8B C7                           mov eax, edi
00AEED0D  E9 F3 17 00 00                  jmp 0x140af0505
00AEED12  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEED1A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEED1F  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEED27  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEED2C  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEED34  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEED39  45 8A C5                        mov r8b, r13b
00AEED3C  BA 08 00 00 00                  mov edx, 8
00AEED41  48 8B CB                        mov rcx, rbx
00AEED44  E8 87 ED 8F FF                  call 0x1403edad0
00AEED49  85 C0                           test eax, eax
00AEED4B  0F 88 B4 17 00 00               js 0x140af0505
00AEED51  BB 01 00 00 00                  mov ebx, 1
00AEED56  41 89 1C 24                     mov dword ptr [r12], ebx
00AEED5A  39 9C 24 18 02 00 00            cmp dword ptr [rsp + 0x218], ebx
00AEED61  0F 82 AC F0 FF FF               jb 0x140aede13
00AEED67  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEED6F  F7 81 C8 00 00 00 10 08 00 00   test dword ptr [rcx + 0xc8], 0x810
00AEED79  0F 95 C0                        setne al
00AEED7C  41 88 07                        mov byte ptr [r15], al
00AEED7F  E9 2E E7 FF FF                  jmp 0x140aed4b2
00AEED84  8B D8                           mov ebx, eax
00AEED86  BA 53 68 72 74                  mov edx, 0x74726853
00AEED8B  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEED93  E8 48 8B 80 FF                  call 0x1402f78e0
00AEED98  8B C3                           mov eax, ebx
00AEED9A  E9 66 17 00 00                  jmp 0x140af0505
00AEED9F  8B D8                           mov ebx, eax
00AEEDA1  BA 53 68 72 74                  mov edx, 0x74726853
00AEEDA6  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEEDAE  E8 2D 8B 80 FF                  call 0x1402f78e0
00AEEDB3  8B C3                           mov eax, ebx
00AEEDB5  E9 4B 17 00 00                  jmp 0x140af0505
00AEEDBA  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEEDC2  83 FE 04                        cmp esi, 4
00AEEDC5  74 0A                           je 0x140aeedd1
00AEEDC7  B8 04 00 00 C0                  mov eax, 0xc0000004
00AEEDCC  E9 34 17 00 00                  jmp 0x140af0505
00AEEDD1  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEEDD9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEEDDE  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEEDE6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEEDEB  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEEDF3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEEDF8  45 8A C5                        mov r8b, r13b
00AEEDFB  BA 08 00 00 00                  mov edx, 8
00AEEE00  48 8B CB                        mov rcx, rbx
00AEEE03  E8 C8 EC 8F FF                  call 0x1403edad0
00AEEE08  85 C0                           test eax, eax
00AEEE0A  0F 88 F5 16 00 00               js 0x140af0505
00AEEE10  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEEE19  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEEE20  90                              nop
00AEEE21  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AEEE29  BA 01 00 00 00                  mov edx, 1
00AEEE2E  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEEE32  E8 89 2D 72 FF                  call 0x140211bc0
00AEEE37  48 8B CF                        mov rcx, rdi
00AEEE3A  E8 89 05 96 FF                  call 0x14044f3c8
00AEEE3F  8B D8                           mov ebx, eax
00AEEE41  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEEE45  E8 C6 0B 77 FF                  call 0x14025fa10
00AEEE4A  E8 61 EA 76 FF                  call 0x14025d8b0
00AEEE4F  90                              nop
00AEEE50  41 89 1F                        mov dword ptr [r15], ebx
00AEEE53  E9 57 E6 FF FF                  jmp 0x140aed4af
00AEEE58  8B D8                           mov ebx, eax
00AEEE5A  BA 53 68 72 74                  mov edx, 0x74726853
00AEEE5F  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEEE67  E8 74 8A 80 FF                  call 0x1402f78e0
00AEEE6C  8B C3                           mov eax, ebx
00AEEE6E  E9 92 16 00 00                  jmp 0x140af0505
00AEEE73  E9 8D 16 00 00                  jmp 0x140af0505
00AEEE78  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEEE80  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEEE85  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEEE8D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEEE92  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEEE9A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEEE9F  45 8A C5                        mov r8b, r13b
00AEEEA2  BA 08 00 00 00                  mov edx, 8
00AEEEA7  48 8B CB                        mov rcx, rbx
00AEEEAA  E8 21 EC 8F FF                  call 0x1403edad0
00AEEEAF  85 C0                           test eax, eax
00AEEEB1  0F 88 4E 16 00 00               js 0x140af0505
00AEEEB7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEEEC0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEEEC7  90                              nop
00AEEEC8  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AEEED0  BB 01 00 00 00                  mov ebx, 1
00AEEED5  8A D3                           mov dl, bl
00AEEED7  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEEEDB  E8 E0 2C 72 FF                  call 0x140211bc0
00AEEEE0  48 8D 94 24 78 01 00 00         lea rdx, [rsp + 0x178]
00AEEEE8  48 8B CF                        mov rcx, rdi
00AEEEEB  E8 20 AE 92 FF                  call 0x140419d10
00AEEEF0  4C 8B 84 24 78 01 00 00         mov r8, qword ptr [rsp + 0x178]
00AEEEF8  41 0F B6 40 01                  movzx eax, byte ptr [r8 + 1]
00AEEEFD  8D 04 85 18 00 00 00            lea eax, [rax*4 + 0x18]
00AEEF04  41 89 04 24                     mov dword ptr [r12], eax
00AEEF08  39 84 24 18 02 00 00            cmp dword ptr [rsp + 0x218], eax
00AEEF0F  0F 82 32 E5 FF FF               jb 0x140aed447
00AEEF15  49 8D 47 10                     lea rax, [r15 + 0x10]
00AEEF19  45 0F B6 40 01                  movzx r8d, byte ptr [r8 + 1]
00AEEF1E  46 8D 04 85 08 00 00 00         lea r8d, [r8*4 + 8]
00AEEF26  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AEEF2E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AEEF33  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00AEEF3B  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AEEF40  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEEF45  4D 8B CF                        mov r9, r15
00AEEF48  48 8D 94 24 78 01 00 00         lea rdx, [rsp + 0x178]
00AEEF50  8B CB                           mov ecx, ebx
00AEEF52  E8 89 9C EB FF                  call 0x1409a8be0
00AEEF57  E9 45 E5 FF FF                  jmp 0x140aed4a1
00AEEF5C  8B F8                           mov edi, eax
00AEEF5E  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEEF66  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEEF6A  E8 A1 0A 77 FF                  call 0x14025fa10
00AEEF6F  E8 3C E9 76 FF                  call 0x14025d8b0
00AEEF74  BA 53 68 72 74                  mov edx, 0x74726853
00AEEF79  48 8B CB                        mov rcx, rbx
00AEEF7C  E8 5F 89 80 FF                  call 0x1402f78e0
00AEEF81  8B C7                           mov eax, edi
00AEEF83  E9 7D 15 00 00                  jmp 0x140af0505
00AEEF88  8B F8                           mov edi, eax
00AEEF8A  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEEF92  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEEF96  E8 75 0A 77 FF                  call 0x14025fa10
00AEEF9B  E8 10 E9 76 FF                  call 0x14025d8b0
00AEEFA0  BA 53 68 72 74                  mov edx, 0x74726853
00AEEFA5  48 8B CB                        mov rcx, rbx
00AEEFA8  E8 33 89 80 FF                  call 0x1402f78e0
00AEEFAD  8B C7                           mov eax, edi
00AEEFAF  E9 51 15 00 00                  jmp 0x140af0505
00AEEFB4  41 83 FE 28                     cmp r14d, 0x28
00AEEFB8  0F 8F 8D 0A 00 00               jg 0x140aefa4b
00AEEFBE  0F 84 C9 FA FF FF               je 0x140aeea8d
00AEEFC4  41 83 FE 1F                     cmp r14d, 0x1f
00AEEFC8  0F 8F EE 04 00 00               jg 0x140aef4bc
00AEEFCE  0F 84 DB 03 00 00               je 0x140aef3af
00AEEFD4  41 8B CE                        mov ecx, r14d
00AEEFD7  83 E9 1A                        sub ecx, 0x1a
00AEEFDA  0F 84 AD FA FF FF               je 0x140aeea8d
00AEEFE0  83 E9 01                        sub ecx, 1
00AEEFE3  0F 84 1D 03 00 00               je 0x140aef306
00AEEFE9  83 E9 01                        sub ecx, 1
00AEEFEC  0F 84 72 01 00 00               je 0x140aef164
00AEEFF2  83 E9 01                        sub ecx, 1
00AEEFF5  0F 84 92 FA FF FF               je 0x140aeea8d
00AEEFFB  83 F9 01                        cmp ecx, 1
00AEEFFE  0F 85 C0 E7 FF FF               jne 0x140aed7c4
00AEF004  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF00C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF011  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF019  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF01E  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF026  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF02B  45 8A C5                        mov r8b, r13b
00AEF02E  8D 51 07                        lea edx, [rcx + 7]
00AEF031  48 8B CB                        mov rcx, rbx
00AEF034  E8 97 EA 8F FF                  call 0x1403edad0
00AEF039  85 C0                           test eax, eax
00AEF03B  0F 88 C4 14 00 00               js 0x140af0505
00AEF041  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF04A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF051  90                              nop
00AEF052  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEF05A  BB 01 00 00 00                  mov ebx, 1
00AEF05F  8A D3                           mov dl, bl
00AEF061  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF065  E8 56 2B 72 FF                  call 0x140211bc0
00AEF06A  8B 8E 20 03 00 00               mov ecx, dword ptr [rsi + 0x320]
00AEF070  44 8B C1                        mov r8d, ecx
00AEF073  41 C1 E0 04                     shl r8d, 4
00AEF077  41 83 C0 08                     add r8d, 8
00AEF07B  85 C9                           test ecx, ecx
00AEF07D  74 25                           je 0x140aef0a4
00AEF07F  48 8B 96 18 03 00 00            mov rdx, qword ptr [rsi + 0x318]
00AEF086  44 8B C9                        mov r9d, ecx
00AEF089  44 8D 63 0F                     lea r12d, [rbx + 0xf]
00AEF08D  48 8B 02                        mov rax, qword ptr [rdx]
00AEF090  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AEF094  45 8D 04 88                     lea r8d, [r8 + rcx*4]
00AEF098  41 83 C0 08                     add r8d, 8
00AEF09C  49 03 D4                        add rdx, r12
00AEF09F  4C 2B CB                        sub r9, rbx
00AEF0A2  75 E9                           jne 0x140aef08d
00AEF0A4  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEF0AC  44 89 00                        mov dword ptr [rax], r8d
00AEF0AF  44 39 84 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r8d
00AEF0B7  0F 82 6F E9 FF FF               jb 0x140aeda2c
00AEF0BD  8B 86 20 03 00 00               mov eax, dword ptr [rsi + 0x320]
00AEF0C3  41 89 07                        mov dword ptr [r15], eax
00AEF0C6  8B 8E 20 03 00 00               mov ecx, dword ptr [rsi + 0x320]
00AEF0CC  8B D1                           mov edx, ecx
00AEF0CE  C1 E2 04                        shl edx, 4
00AEF0D1  48 83 C2 08                     add rdx, 8
00AEF0D5  49 03 D7                        add rdx, r15
00AEF0D8  4D 8D 4F 08                     lea r9, [r15 + 8]
00AEF0DC  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEF0E4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF0E9  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEF0F1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF0F6  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00AEF0FB  48 8B 96 18 03 00 00            mov rdx, qword ptr [rsi + 0x318]
00AEF102  E8 D9 9A EB FF                  call 0x1409a8be0
00AEF107  E9 81 E9 FF FF                  jmp 0x140aeda8d
00AEF10C  8B F8                           mov edi, eax
00AEF10E  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF116  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF11A  E8 F1 08 77 FF                  call 0x14025fa10
00AEF11F  E8 8C E7 76 FF                  call 0x14025d8b0
00AEF124  BA 53 68 72 74                  mov edx, 0x74726853
00AEF129  48 8B CB                        mov rcx, rbx
00AEF12C  E8 AF 87 80 FF                  call 0x1402f78e0
00AEF131  8B C7                           mov eax, edi
00AEF133  E9 CD 13 00 00                  jmp 0x140af0505
00AEF138  8B F8                           mov edi, eax
00AEF13A  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF142  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF146  E8 C5 08 77 FF                  call 0x14025fa10
00AEF14B  E8 60 E7 76 FF                  call 0x14025d8b0
00AEF150  BA 53 68 72 74                  mov edx, 0x74726853
00AEF155  48 8B CB                        mov rcx, rbx
00AEF158  E8 83 87 80 FF                  call 0x1402f78e0
00AEF15D  8B C7                           mov eax, edi
00AEF15F  E9 A1 13 00 00                  jmp 0x140af0505
00AEF164  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF16C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF171  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF179  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF17E  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF186  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF18B  45 8A C5                        mov r8b, r13b
00AEF18E  BA 08 00 00 00                  mov edx, 8
00AEF193  48 8B CB                        mov rcx, rbx
00AEF196  E8 35 E9 8F FF                  call 0x1403edad0
00AEF19B  85 C0                           test eax, eax
00AEF19D  0F 88 62 13 00 00               js 0x140af0505
00AEF1A3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF1AC  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF1B3  90                              nop
00AEF1B4  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEF1BC  BB 01 00 00 00                  mov ebx, 1
00AEF1C1  8A D3                           mov dl, bl
00AEF1C3  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF1C7  E8 F4 29 72 FF                  call 0x140211bc0
00AEF1CC  4C 8B CF                        mov r9, rdi
00AEF1CF  8B CF                           mov ecx, edi
00AEF1D1  44 8B 56 7C                     mov r10d, dword ptr [rsi + 0x7c]
00AEF1D5  45 85 D2                        test r10d, r10d
00AEF1D8  74 2C                           je 0x140aef206
00AEF1DA  4C 8B 86 98 00 00 00            mov r8, qword ptr [rsi + 0x98]
00AEF1E1  41 BB 00 00 00 C0               mov r11d, 0xc0000000
00AEF1E7  8B D1                           mov edx, ecx
00AEF1E9  48 03 D2                        add rdx, rdx
00AEF1EC  41 8B 44 D0 08                  mov eax, dword ptr [r8 + rdx*8 + 8]
00AEF1F1  41 23 C3                        and eax, r11d
00AEF1F4  41 3B C3                        cmp eax, r11d
00AEF1F7  74 09                           je 0x140aef202
00AEF1F9  03 CB                           add ecx, ebx
00AEF1FB  41 3B CA                        cmp ecx, r10d
00AEF1FE  72 E7                           jb 0x140aef1e7
00AEF200  EB 04                           jmp 0x140aef206
00AEF202  4D 8B 0C D0                     mov r9, qword ptr [r8 + rdx*8]
00AEF206  4D 85 C9                        test r9, r9
00AEF209  75 25                           jne 0x140aef230
00AEF20B  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF20F  E8 FC 07 77 FF                  call 0x14025fa10
00AEF214  E8 97 E6 76 FF                  call 0x14025d8b0
00AEF219  BA 53 68 72 74                  mov edx, 0x74726853
00AEF21E  48 8B CE                        mov rcx, rsi
00AEF221  E8 BA 86 80 FF                  call 0x1402f78e0
00AEF226  B8 25 02 00 C0                  mov eax, 0xc0000225
00AEF22B  E9 D5 12 00 00                  jmp 0x140af0505
00AEF230  44 8B C1                        mov r8d, ecx
00AEF233  49 C1 E0 04                     shl r8, 4
00AEF237  48 8B 86 98 00 00 00            mov rax, qword ptr [rsi + 0x98]
00AEF23E  49 8B 0C 00                     mov rcx, qword ptr [r8 + rax]
00AEF242  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AEF246  8D 04 85 20 00 00 00            lea eax, [rax*4 + 0x20]
00AEF24D  41 89 04 24                     mov dword ptr [r12], eax
00AEF251  39 84 24 18 02 00 00            cmp dword ptr [rsp + 0x218], eax
00AEF258  0F 82 CE E7 FF FF               jb 0x140aeda2c
00AEF25E  41 89 1F                        mov dword ptr [r15], ebx
00AEF261  49 8D 4F 18                     lea rcx, [r15 + 0x18]
00AEF265  48 8B 96 98 00 00 00            mov rdx, qword ptr [rsi + 0x98]
00AEF26C  49 03 D0                        add rdx, r8
00AEF26F  4D 8D 4F 08                     lea r9, [r15 + 8]
00AEF273  48 8B 02                        mov rax, qword ptr [rdx]
00AEF276  44 0F B6 40 01                  movzx r8d, byte ptr [rax + 1]
00AEF27B  46 8D 04 85 08 00 00 00         lea r8d, [r8*4 + 8]
00AEF283  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEF28B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF290  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEF298  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF29D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AEF2A2  8B CB                           mov ecx, ebx
00AEF2A4  E8 37 99 EB FF                  call 0x1409a8be0
00AEF2A9  E9 DF E7 FF FF                  jmp 0x140aeda8d
00AEF2AE  8B F8                           mov edi, eax
00AEF2B0  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF2B8  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF2BC  E8 4F 07 77 FF                  call 0x14025fa10
00AEF2C1  E8 EA E5 76 FF                  call 0x14025d8b0
00AEF2C6  BA 53 68 72 74                  mov edx, 0x74726853
00AEF2CB  48 8B CB                        mov rcx, rbx
00AEF2CE  E8 0D 86 80 FF                  call 0x1402f78e0
00AEF2D3  8B C7                           mov eax, edi
00AEF2D5  E9 2B 12 00 00                  jmp 0x140af0505
00AEF2DA  8B F8                           mov edi, eax
00AEF2DC  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF2E4  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF2E8  E8 23 07 77 FF                  call 0x14025fa10
00AEF2ED  E8 BE E5 76 FF                  call 0x14025d8b0
00AEF2F2  BA 53 68 72 74                  mov edx, 0x74726853
00AEF2F7  48 8B CB                        mov rcx, rbx
00AEF2FA  E8 E1 85 80 FF                  call 0x1402f78e0
00AEF2FF  8B C7                           mov eax, edi
00AEF301  E9 FF 11 00 00                  jmp 0x140af0505
00AEF306  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF30E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF313  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF31B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF320  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF328  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF32D  45 8A C5                        mov r8b, r13b
00AEF330  BA 08 00 00 00                  mov edx, 8
00AEF335  48 8B CB                        mov rcx, rbx
00AEF338  E8 93 E7 8F FF                  call 0x1403edad0
00AEF33D  85 C0                           test eax, eax
00AEF33F  0F 88 C0 11 00 00               js 0x140af0505
00AEF345  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEF34D  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEF355  0F 82 B8 EA FF FF               jb 0x140aede13
00AEF35B  49 8B D7                        mov rdx, r15
00AEF35E  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEF366  E8 45 8F 94 FF                  call 0x1404382b0
00AEF36B  8B D8                           mov ebx, eax
00AEF36D  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AEF374  E9 88 F6 FF FF                  jmp 0x140aeea01
00AEF379  8B D8                           mov ebx, eax
00AEF37B  BA 53 68 72 74                  mov edx, 0x74726853
00AEF380  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEF388  E8 53 85 80 FF                  call 0x1402f78e0
00AEF38D  8B C3                           mov eax, ebx
00AEF38F  E9 71 11 00 00                  jmp 0x140af0505
00AEF394  8B D8                           mov ebx, eax
00AEF396  BA 53 68 72 74                  mov edx, 0x74726853
00AEF39B  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEF3A3  E8 38 85 80 FF                  call 0x1402f78e0
00AEF3A8  8B C3                           mov eax, ebx
00AEF3AA  E9 56 11 00 00                  jmp 0x140af0505
00AEF3AF  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF3B7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF3BC  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF3C4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF3C9  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF3D1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF3D6  45 8A C5                        mov r8b, r13b
00AEF3D9  BE 08 00 00 00                  mov esi, 8
00AEF3DE  8B D6                           mov edx, esi
00AEF3E0  48 8B CB                        mov rcx, rbx
00AEF3E3  E8 E8 E6 8F FF                  call 0x1403edad0
00AEF3E8  85 C0                           test eax, eax
00AEF3EA  0F 88 15 11 00 00               js 0x140af0505
00AEF3F0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF3F9  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF400  90                              nop
00AEF401  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEF409  8D 56 F9                        lea edx, [rsi - 7]
00AEF40C  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEF410  E8 AB 27 72 FF                  call 0x140211bc0
00AEF415  49 8B 8E 10 03 00 00            mov rcx, qword ptr [r14 + 0x310]
00AEF41C  48 85 C9                        test rcx, rcx
00AEF41F  74 0B                           je 0x140aef42c
00AEF421  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AEF425  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
00AEF42C  41 89 34 24                     mov dword ptr [r12], esi
00AEF430  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AEF437  0F 82 5F E4 FF FF               jb 0x140aed89c
00AEF43D  49 8D 57 08                     lea rdx, [r15 + 8]
00AEF441  48 85 C9                        test rcx, rcx
00AEF444  48 0F 44 D1                     cmove rdx, rcx
00AEF448  49 89 17                        mov qword ptr [r15], rdx
00AEF44B  48 85 D2                        test rdx, rdx
00AEF44E  74 0F                           je 0x140aef45f
00AEF450  8D 4E F8                        lea ecx, [rsi - 8]
00AEF453  4D 8B 86 10 03 00 00            mov r8, qword ptr [r14 + 0x310]
00AEF45A  E8 F1 A5 EB FF                  call 0x1409a9a50
00AEF45F  E9 74 E4 FF FF                  jmp 0x140aed8d8
00AEF464  8B F8                           mov edi, eax
00AEF466  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF46E  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF472  E8 99 05 77 FF                  call 0x14025fa10
00AEF477  E8 34 E4 76 FF                  call 0x14025d8b0
00AEF47C  BA 53 68 72 74                  mov edx, 0x74726853
00AEF481  48 8B CB                        mov rcx, rbx
00AEF484  E8 57 84 80 FF                  call 0x1402f78e0
00AEF489  8B C7                           mov eax, edi
00AEF48B  E9 75 10 00 00                  jmp 0x140af0505
00AEF490  8B F8                           mov edi, eax
00AEF492  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF49A  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF49E  E8 6D 05 77 FF                  call 0x14025fa10
00AEF4A3  E8 08 E4 76 FF                  call 0x14025d8b0
00AEF4A8  BA 53 68 72 74                  mov edx, 0x74726853
00AEF4AD  48 8B CB                        mov rcx, rbx
00AEF4B0  E8 2B 84 80 FF                  call 0x1402f78e0
00AEF4B5  8B C7                           mov eax, edi
00AEF4B7  E9 49 10 00 00                  jmp 0x140af0505
00AEF4BC  41 8B CE                        mov ecx, r14d
00AEF4BF  83 E9 20                        sub ecx, 0x20
00AEF4C2  0F 84 AB 04 00 00               je 0x140aef973
00AEF4C8  83 E9 01                        sub ecx, 1
00AEF4CB  0F 84 E8 02 00 00               je 0x140aef7b9
00AEF4D1  83 E9 01                        sub ecx, 1
00AEF4D4  0F 84 DF 02 00 00               je 0x140aef7b9
00AEF4DA  83 E9 03                        sub ecx, 3
00AEF4DD  0F 84 4B 01 00 00               je 0x140aef62e
00AEF4E3  83 F9 02                        cmp ecx, 2
00AEF4E6  0F 85 D8 E2 FF FF               jne 0x140aed7c4
00AEF4EC  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF4F4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF4F9  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF501  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF506  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF50E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF513  45 8A C5                        mov r8b, r13b
00AEF516  8D 51 06                        lea edx, [rcx + 6]
00AEF519  48 8B CB                        mov rcx, rbx
00AEF51C  E8 AF E5 8F FF                  call 0x1403edad0
00AEF521  85 C0                           test eax, eax
00AEF523  0F 88 DC 0F 00 00               js 0x140af0505
00AEF529  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF532  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF539  90                              nop
00AEF53A  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEF542  BA 01 00 00 00                  mov edx, 1
00AEF547  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF54B  E8 70 26 72 FF                  call 0x140211bc0
00AEF550  48 8B 8E 08 03 00 00            mov rcx, qword ptr [rsi + 0x308]
00AEF557  48 85 C9                        test rcx, rcx
00AEF55A  75 06                           jne 0x140aef562
00AEF55C  44 8D 61 10                     lea r12d, [rcx + 0x10]
00AEF560  EB 26                           jmp 0x140aef588
00AEF562  48 8D 84 24 9C 00 00 00         lea rax, [rsp + 0x9c]
00AEF56A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF56F  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AEF573  45 33 C9                        xor r9d, r9d
00AEF576  45 33 C0                        xor r8d, r8d
00AEF579  33 D2                           xor edx, edx
00AEF57B  E8 00 88 8B FF                  call 0x1403a7d80
00AEF580  44 8B A4 24 9C 00 00 00         mov r12d, dword ptr [rsp + 0x9c]
00AEF588  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEF590  44 89 20                        mov dword ptr [rax], r12d
00AEF593  8B 94 24 18 02 00 00            mov edx, dword ptr [rsp + 0x218]
00AEF59A  41 3B D4                        cmp edx, r12d
00AEF59D  0F 82 89 E4 FF FF               jb 0x140aeda2c
00AEF5A3  48 8D 84 24 9C 00 00 00         lea rax, [rsp + 0x9c]
00AEF5AB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF5B0  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00AEF5B4  4D 8B CF                        mov r9, r15
00AEF5B7  45 33 C0                        xor r8d, r8d
00AEF5BA  33 D2                           xor edx, edx
00AEF5BC  48 8B 8E 08 03 00 00            mov rcx, qword ptr [rsi + 0x308]
00AEF5C3  E8 B8 87 8B FF                  call 0x1403a7d80
00AEF5C8  8B D8                           mov ebx, eax
00AEF5CA  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AEF5D1  E9 2F 03 00 00                  jmp 0x140aef905
00AEF5D6  8B F8                           mov edi, eax
00AEF5D8  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF5E0  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF5E4  E8 27 04 77 FF                  call 0x14025fa10
00AEF5E9  E8 C2 E2 76 FF                  call 0x14025d8b0
00AEF5EE  BA 53 68 72 74                  mov edx, 0x74726853
00AEF5F3  48 8B CB                        mov rcx, rbx
00AEF5F6  E8 E5 82 80 FF                  call 0x1402f78e0
00AEF5FB  8B C7                           mov eax, edi
00AEF5FD  E9 03 0F 00 00                  jmp 0x140af0505
00AEF602  8B F8                           mov edi, eax
00AEF604  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF60C  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF610  E8 FB 03 77 FF                  call 0x14025fa10
00AEF615  E8 96 E2 76 FF                  call 0x14025d8b0
00AEF61A  BA 53 68 72 74                  mov edx, 0x74726853
00AEF61F  48 8B CB                        mov rcx, rbx
00AEF622  E8 B9 82 80 FF                  call 0x1402f78e0
00AEF627  8B C7                           mov eax, edi
00AEF629  E9 D7 0E 00 00                  jmp 0x140af0505
00AEF62E  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF636  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF63B  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF643  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF648  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF650  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF655  45 8A C5                        mov r8b, r13b
00AEF658  BE 08 00 00 00                  mov esi, 8
00AEF65D  8B D6                           mov edx, esi
00AEF65F  48 8B CB                        mov rcx, rbx
00AEF662  E8 69 E4 8F FF                  call 0x1403edad0
00AEF667  85 C0                           test eax, eax
00AEF669  0F 88 96 0E 00 00               js 0x140af0505
00AEF66F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF678  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF67F  90                              nop
00AEF680  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEF688  8D 5E F9                        lea ebx, [rsi - 7]
00AEF68B  8A D3                           mov dl, bl
00AEF68D  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEF691  E8 2A 25 72 FF                  call 0x140211bc0
00AEF696  49 8B 86 48 04 00 00            mov rax, qword ptr [r14 + 0x448]
00AEF69D  48 85 C0                        test rax, rax
00AEF6A0  74 14                           je 0x140aef6b6
00AEF6A2  44 8B 18                        mov r11d, dword ptr [rax]
00AEF6A5  45 85 DB                        test r11d, r11d
00AEF6A8  74 0C                           je 0x140aef6b6
00AEF6AA  45 8B C3                        mov r8d, r11d
00AEF6AD  41 C1 E0 04                     shl r8d, 4
00AEF6B1  44 03 C6                        add r8d, esi
00AEF6B4  EB 09                           jmp 0x140aef6bf
00AEF6B6  44 8B DF                        mov r11d, edi
00AEF6B9  41 B8 18 00 00 00               mov r8d, 0x18
00AEF6BF  41 BC 10 00 00 00               mov r12d, 0x10
00AEF6C5  45 85 DB                        test r11d, r11d
00AEF6C8  74 1D                           je 0x140aef6e7
00AEF6CA  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00AEF6CE  45 8B CB                        mov r9d, r11d
00AEF6D1  48 8B 02                        mov rax, qword ptr [rdx]
00AEF6D4  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AEF6D8  45 8D 04 88                     lea r8d, [r8 + rcx*4]
00AEF6DC  44 03 C6                        add r8d, esi
00AEF6DF  49 03 D4                        add rdx, r12
00AEF6E2  4C 2B CB                        sub r9, rbx
00AEF6E5  75 EA                           jne 0x140aef6d1
00AEF6E7  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEF6EF  44 89 00                        mov dword ptr [rax], r8d
00AEF6F2  44 39 84 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r8d
00AEF6FA  0F 82 9C E1 FF FF               jb 0x140aed89c
00AEF700  0F 57 C0                        xorps xmm0, xmm0
00AEF703  33 C0                           xor eax, eax
00AEF705  41 0F 11 07                     movups xmmword ptr [r15], xmm0
00AEF709  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
00AEF70D  45 89 1F                        mov dword ptr [r15], r11d
00AEF710  45 85 DB                        test r11d, r11d
00AEF713  74 47                           je 0x140aef75c
00AEF715  45 8B D3                        mov r10d, r11d
00AEF718  41 C1 E2 04                     shl r10d, 4
00AEF71C  45 2B D4                        sub r10d, r12d
00AEF71F  49 83 C2 18                     add r10, 0x18
00AEF723  4D 03 D7                        add r10, r15
00AEF726  4D 8D 4F 08                     lea r9, [r15 + 8]
00AEF72A  49 8B 96 48 04 00 00            mov rdx, qword ptr [r14 + 0x448]
00AEF731  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEF739  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF73E  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AEF746  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF74B  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00AEF750  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00AEF754  41 8B CB                        mov ecx, r11d
00AEF757  E8 84 94 EB FF                  call 0x1409a8be0
00AEF75C  E9 77 E1 FF FF                  jmp 0x140aed8d8
00AEF761  8B F8                           mov edi, eax
00AEF763  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF76B  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF76F  E8 9C 02 77 FF                  call 0x14025fa10
00AEF774  E8 37 E1 76 FF                  call 0x14025d8b0
00AEF779  BA 53 68 72 74                  mov edx, 0x74726853
00AEF77E  48 8B CB                        mov rcx, rbx
00AEF781  E8 5A 81 80 FF                  call 0x1402f78e0
00AEF786  8B C7                           mov eax, edi
00AEF788  E9 78 0D 00 00                  jmp 0x140af0505
00AEF78D  8B F8                           mov edi, eax
00AEF78F  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF797  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF79B  E8 70 02 77 FF                  call 0x14025fa10
00AEF7A0  E8 0B E1 76 FF                  call 0x14025d8b0
00AEF7A5  BA 53 68 72 74                  mov edx, 0x74726853
00AEF7AA  48 8B CB                        mov rcx, rbx
00AEF7AD  E8 2E 81 80 FF                  call 0x1402f78e0
00AEF7B2  8B C7                           mov eax, edi
00AEF7B4  E9 4C 0D 00 00                  jmp 0x140af0505
00AEF7B9  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF7C1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF7C6  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF7CE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF7D3  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF7DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF7E0  45 8A C5                        mov r8b, r13b
00AEF7E3  BA 08 00 00 00                  mov edx, 8
00AEF7E8  48 8B CB                        mov rcx, rbx
00AEF7EB  E8 E0 E2 8F FF                  call 0x1403edad0
00AEF7F0  85 C0                           test eax, eax
00AEF7F2  0F 88 0D 0D 00 00               js 0x140af0505
00AEF7F8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF801  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF808  90                              nop
00AEF809  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEF811  BA 01 00 00 00                  mov edx, 1
00AEF816  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF81A  E8 A1 23 72 FF                  call 0x140211bc0
00AEF81F  48 8B 9E 48 04 00 00            mov rbx, qword ptr [rsi + 0x448]
00AEF826  48 85 DB                        test rbx, rbx
00AEF829  74 4B                           je 0x140aef876
00AEF82B  48 8B 83 40 02 00 00            mov rax, qword ptr [rbx + 0x240]
00AEF832  48 85 C0                        test rax, rax
00AEF835  75 06                           jne 0x140aef83d
00AEF837  41 83 FE 21                     cmp r14d, 0x21
00AEF83B  74 39                           je 0x140aef876
00AEF83D  48 8B 9B 48 02 00 00            mov rbx, qword ptr [rbx + 0x248]
00AEF844  48 85 DB                        test rbx, rbx
00AEF847  75 06                           jne 0x140aef84f
00AEF849  41 83 FE 22                     cmp r14d, 0x22
00AEF84D  74 27                           je 0x140aef876
00AEF84F  41 83 FE 21                     cmp r14d, 0x21
00AEF853  48 0F 44 D8                     cmove rbx, rax
00AEF857  4C 8D 8C 24 9C 00 00 00         lea r9, [rsp + 0x9c]
00AEF85F  45 33 C0                        xor r8d, r8d
00AEF862  33 D2                           xor edx, edx
00AEF864  48 8B CB                        mov rcx, rbx
00AEF867  E8 A0 8A F2 FF                  call 0x140a1830c
00AEF86C  44 8B A4 24 9C 00 00 00         mov r12d, dword ptr [rsp + 0x9c]
00AEF874  EB 55                           jmp 0x140aef8cb
00AEF876  41 BC 10 00 00 00               mov r12d, 0x10
00AEF87C  48 8D 84 24 48 01 00 00         lea rax, [rsp + 0x148]
00AEF884  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00AEF88C  48 8D 84 24 48 01 00 00         lea rax, [rsp + 0x148]
00AEF894  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00AEF89C  89 BC 24 58 01 00 00            mov dword ptr [rsp + 0x158], edi
00AEF8A3  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
00AEF8AB  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
00AEF8B3  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
00AEF8BB  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
00AEF8C3  48 8D 9C 24 40 01 00 00         lea rbx, [rsp + 0x140]
00AEF8CB  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEF8D3  44 89 20                        mov dword ptr [rax], r12d
00AEF8D6  8B 94 24 18 02 00 00            mov edx, dword ptr [rsp + 0x218]
00AEF8DD  41 3B D4                        cmp edx, r12d
00AEF8E0  0F 82 46 E1 FF FF               jb 0x140aeda2c
00AEF8E6  4C 8D 8C 24 9C 00 00 00         lea r9, [rsp + 0x9c]
00AEF8EE  44 8B C2                        mov r8d, edx
00AEF8F1  49 8B D7                        mov rdx, r15
00AEF8F4  48 8B CB                        mov rcx, rbx
00AEF8F7  E8 10 8A F2 FF                  call 0x140a1830c
00AEF8FC  8B D8                           mov ebx, eax
00AEF8FE  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AEF905  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF909  E8 02 01 77 FF                  call 0x14025fa10
00AEF90E  E8 9D DF 76 FF                  call 0x14025d8b0
00AEF913  48 8B CE                        mov rcx, rsi
00AEF916  E9 E6 F0 FF FF                  jmp 0x140aeea01
00AEF91B  8B F8                           mov edi, eax
00AEF91D  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF925  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF929  E8 E2 00 77 FF                  call 0x14025fa10
00AEF92E  E8 7D DF 76 FF                  call 0x14025d8b0
00AEF933  BA 53 68 72 74                  mov edx, 0x74726853
00AEF938  48 8B CB                        mov rcx, rbx
00AEF93B  E8 A0 7F 80 FF                  call 0x1402f78e0
00AEF940  8B C7                           mov eax, edi
00AEF942  E9 BE 0B 00 00                  jmp 0x140af0505
00AEF947  8B F8                           mov edi, eax
00AEF949  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEF951  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEF955  E8 B6 00 77 FF                  call 0x14025fa10
00AEF95A  E8 51 DF 76 FF                  call 0x14025d8b0
00AEF95F  BA 53 68 72 74                  mov edx, 0x74726853
00AEF964  48 8B CB                        mov rcx, rbx
00AEF967  E8 74 7F 80 FF                  call 0x1402f78e0
00AEF96C  8B C7                           mov eax, edi
00AEF96E  E9 92 0B 00 00                  jmp 0x140af0505
00AEF973  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEF97B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEF980  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEF988  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEF98D  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEF995  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEF99A  45 8A C5                        mov r8b, r13b
00AEF99D  BA 08 00 00 00                  mov edx, 8
00AEF9A2  48 8B CB                        mov rcx, rbx
00AEF9A5  E8 26 E1 8F FF                  call 0x1403edad0
00AEF9AA  85 C0                           test eax, eax
00AEF9AC  0F 88 53 0B 00 00               js 0x140af0505
00AEF9B2  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00AEF9BA  83 BC 24 18 02 00 00 04         cmp dword ptr [rsp + 0x218], 4
00AEF9C2  0F 82 4B E4 FF FF               jb 0x140aede13
00AEF9C8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEF9D1  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEF9D8  90                              nop
00AEF9D9  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEF9E1  BA 01 00 00 00                  mov edx, 1
00AEF9E6  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEF9EA  E8 D1 21 72 FF                  call 0x140211bc0
00AEF9EF  48 8B 86 38 04 00 00            mov rax, qword ptr [rsi + 0x438]
00AEF9F6  48 85 C0                        test rax, rax
00AEF9F9  74 03                           je 0x140aef9fe
00AEF9FB  8B 78 28                        mov edi, dword ptr [rax + 0x28]
00AEF9FE  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEFA02  E8 09 00 77 FF                  call 0x14025fa10
00AEFA07  E8 A4 DE 76 FF                  call 0x14025d8b0
00AEFA0C  90                              nop
00AEFA0D  41 89 3F                        mov dword ptr [r15], edi
00AEFA10  E9 86 E0 FF FF                  jmp 0x140aeda9b
00AEFA15  8B D8                           mov ebx, eax
00AEFA17  BA 53 68 72 74                  mov edx, 0x74726853
00AEFA1C  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEFA24  E8 B7 7E 80 FF                  call 0x1402f78e0
00AEFA29  8B C3                           mov eax, ebx
00AEFA2B  E9 D5 0A 00 00                  jmp 0x140af0505
00AEFA30  8B D8                           mov ebx, eax
00AEFA32  BA 53 68 72 74                  mov edx, 0x74726853
00AEFA37  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AEFA3F  E8 9C 7E 80 FF                  call 0x1402f78e0
00AEFA44  8B C3                           mov eax, ebx
00AEFA46  E9 BA 0A 00 00                  jmp 0x140af0505
00AEFA4B  41 83 FE 30                     cmp r14d, 0x30
00AEFA4F  0F 8F 70 03 00 00               jg 0x140aefdc5
00AEFA55  0F 84 32 F0 FF FF               je 0x140aeea8d
00AEFA5B  41 8B CE                        mov ecx, r14d
00AEFA5E  83 E9 29                        sub ecx, 0x29
00AEFA61  0F 84 32 02 00 00               je 0x140aefc99
00AEFA67  83 E9 01                        sub ecx, 1
00AEFA6A  0F 84 1D F0 FF FF               je 0x140aeea8d
00AEFA70  83 E9 01                        sub ecx, 1
00AEFA73  0F 84 45 01 00 00               je 0x140aefbbe
00AEFA79  83 E9 01                        sub ecx, 1
00AEFA7C  74 0E                           je 0x140aefa8c
00AEFA7E  83 F9 03                        cmp ecx, 3
00AEFA81  0F 84 06 F0 FF FF               je 0x140aeea8d
00AEFA87  E9 38 DD FF FF                  jmp 0x140aed7c4
00AEFA8C  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEFA94  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEFA99  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEFAA1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEFAA6  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEFAAE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEFAB3  45 8A C5                        mov r8b, r13b
00AEFAB6  BA 08 00 00 00                  mov edx, 8
00AEFABB  48 8B CB                        mov rcx, rbx
00AEFABE  E8 0D E0 8F FF                  call 0x1403edad0
00AEFAC3  85 C0                           test eax, eax
00AEFAC5  0F 88 3A 0A 00 00               js 0x140af0505
00AEFACB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEFAD4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEFADB  90                              nop
00AEFADC  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEFAE4  BB 01 00 00 00                  mov ebx, 1
00AEFAE9  8A D3                           mov dl, bl
00AEFAEB  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEFAEF  E8 CC 20 72 FF                  call 0x140211bc0
00AEFAF4  44 8D 63 0F                     lea r12d, [rbx + 0xf]
00AEFAF8  49 8B 86 80 04 00 00            mov rax, qword ptr [r14 + 0x480]
00AEFAFF  48 85 C0                        test rax, rax
00AEFB02  74 07                           je 0x140aefb0b
00AEFB04  0F B7 40 2A                     movzx eax, word ptr [rax + 0x2a]
00AEFB08  44 03 E0                        add r12d, eax
00AEFB0B  48 8B 84 24 20 02 00 00         mov rax, qword ptr [rsp + 0x220]
00AEFB13  44 89 20                        mov dword ptr [rax], r12d
00AEFB16  44 39 A4 24 18 02 00 00         cmp dword ptr [rsp + 0x218], r12d
00AEFB1E  0F 82 78 DD FF FF               jb 0x140aed89c
00AEFB24  49 39 BE 80 04 00 00            cmp qword ptr [r14 + 0x480], rdi
00AEFB2B  74 22                           je 0x140aefb4f
00AEFB2D  41 88 5F 08                     mov byte ptr [r15 + 8], bl
00AEFB31  49 8D 4F 10                     lea rcx, [r15 + 0x10]
00AEFB35  49 89 0F                        mov qword ptr [r15], rcx
00AEFB38  49 8B 96 80 04 00 00            mov rdx, qword ptr [r14 + 0x480]
00AEFB3F  44 0F B7 42 2A                  movzx r8d, word ptr [rdx + 0x2a]
00AEFB44  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
00AEFB48  E8 F3 6C BD FF                  call 0x1406c6840
00AEFB4D  EB 07                           jmp 0x140aefb56
00AEFB4F  41 88 7F 08                     mov byte ptr [r15 + 8], dil
00AEFB53  49 89 3F                        mov qword ptr [r15], rdi
00AEFB56  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEFB5A  E8 B1 FE 76 FF                  call 0x14025fa10
00AEFB5F  33 FF                           xor edi, edi
00AEFB61  E9 40 08 00 00                  jmp 0x140af03a6
00AEFB66  8B F8                           mov edi, eax
00AEFB68  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFB70  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFB74  E8 97 FE 76 FF                  call 0x14025fa10
00AEFB79  E8 32 DD 76 FF                  call 0x14025d8b0
00AEFB7E  BA 53 68 72 74                  mov edx, 0x74726853
00AEFB83  48 8B CB                        mov rcx, rbx
00AEFB86  E8 55 7D 80 FF                  call 0x1402f78e0
00AEFB8B  8B C7                           mov eax, edi
00AEFB8D  E9 73 09 00 00                  jmp 0x140af0505
00AEFB92  8B F8                           mov edi, eax
00AEFB94  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFB9C  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFBA0  E8 6B FE 76 FF                  call 0x14025fa10
00AEFBA5  E8 06 DD 76 FF                  call 0x14025d8b0
00AEFBAA  BA 53 68 72 74                  mov edx, 0x74726853
00AEFBAF  48 8B CB                        mov rcx, rbx
00AEFBB2  E8 29 7D 80 FF                  call 0x1402f78e0
00AEFBB7  8B C7                           mov eax, edi
00AEFBB9  E9 47 09 00 00                  jmp 0x140af0505
00AEFBBE  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEFBC6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEFBCB  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEFBD3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEFBD8  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEFBE0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEFBE5  45 8A C5                        mov r8b, r13b
00AEFBE8  BA 08 00 00 00                  mov edx, 8
00AEFBED  48 8B CB                        mov rcx, rbx
00AEFBF0  E8 DB DE 8F FF                  call 0x1403edad0
00AEFBF5  85 C0                           test eax, eax
00AEFBF7  0F 88 08 09 00 00               js 0x140af0505
00AEFBFD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEFC06  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEFC0D  90                              nop
00AEFC0E  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00AEFC16  BB 01 00 00 00                  mov ebx, 1
00AEFC1B  8A D3                           mov dl, bl
00AEFC1D  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEFC21  E8 9A 1F 72 FF                  call 0x140211bc0
00AEFC26  90                              nop
00AEFC27  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00AEFC2C  8B 94 24 18 02 00 00            mov edx, dword ptr [rsp + 0x218]
00AEFC33  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00AEFC37  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00AEFC3C  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
00AEFC40  45 33 C9                        xor r9d, r9d
00AEFC43  45 33 C0                        xor r8d, r8d
00AEFC46  48 8B CF                        mov rcx, rdi
00AEFC49  E8 62 7B 8B FF                  call 0x1403a77b0
00AEFC4E  8B D8                           mov ebx, eax
00AEFC50  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AEFC57  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00AEFC5B  E8 B0 FD 76 FF                  call 0x14025fa10
00AEFC60  E8 4B DC 76 FF                  call 0x14025d8b0
00AEFC65  48 8B CF                        mov rcx, rdi
00AEFC68  E9 94 ED FF FF                  jmp 0x140aeea01
00AEFC6D  8B F8                           mov edi, eax
00AEFC6F  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFC77  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFC7B  E8 90 FD 76 FF                  call 0x14025fa10
00AEFC80  E8 2B DC 76 FF                  call 0x14025d8b0
00AEFC85  BA 53 68 72 74                  mov edx, 0x74726853
00AEFC8A  48 8B CB                        mov rcx, rbx
00AEFC8D  E8 4E 7C 80 FF                  call 0x1402f78e0
00AEFC92  8B C7                           mov eax, edi
00AEFC94  E9 6C 08 00 00                  jmp 0x140af0505
00AEFC99  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEFCA1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEFCA6  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEFCAE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEFCB3  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEFCBB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEFCC0  45 8A C5                        mov r8b, r13b
00AEFCC3  BE 08 00 00 00                  mov esi, 8
00AEFCC8  8B D6                           mov edx, esi
00AEFCCA  48 8B CB                        mov rcx, rbx
00AEFCCD  E8 FE DD 8F FF                  call 0x1403edad0
00AEFCD2  85 C0                           test eax, eax
00AEFCD4  0F 88 2B 08 00 00               js 0x140af0505
00AEFCDA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEFCE3  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEFCEA  90                              nop
00AEFCEB  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEFCF3  8D 56 F9                        lea edx, [rsi - 7]
00AEFCF6  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEFCFA  E8 C1 1E 72 FF                  call 0x140211bc0
00AEFCFF  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
00AEFD07  40 38 BC 24 80 00 00 00         cmp byte ptr [rsp + 0x80], dil
00AEFD0F  49 8B C8                        mov rcx, r8
00AEFD12  75 07                           jne 0x140aefd1b
00AEFD14  49 8B 8E 50 04 00 00            mov rcx, qword ptr [r14 + 0x450]
00AEFD1B  48 85 C9                        test rcx, rcx
00AEFD1E  74 0B                           je 0x140aefd2b
00AEFD20  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AEFD24  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
00AEFD2B  41 89 34 24                     mov dword ptr [r12], esi
00AEFD2F  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AEFD36  0F 82 60 DB FF FF               jb 0x140aed89c
00AEFD3C  49 8D 57 08                     lea rdx, [r15 + 8]
00AEFD40  48 85 C9                        test rcx, rcx
00AEFD43  48 0F 44 D1                     cmove rdx, rcx
00AEFD47  49 89 17                        mov qword ptr [r15], rdx
00AEFD4A  48 85 D2                        test rdx, rdx
00AEFD4D  74 19                           je 0x140aefd68
00AEFD4F  40 38 BC 24 80 00 00 00         cmp byte ptr [rsp + 0x80], dil
00AEFD57  75 07                           jne 0x140aefd60
00AEFD59  4D 8B 86 50 04 00 00            mov r8, qword ptr [r14 + 0x450]
00AEFD60  8D 4E F8                        lea ecx, [rsi - 8]
00AEFD63  E8 E8 9C EB FF                  call 0x1409a9a50
00AEFD68  E9 6B DB FF FF                  jmp 0x140aed8d8
00AEFD6D  8B F8                           mov edi, eax
00AEFD6F  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFD77  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFD7B  E8 90 FC 76 FF                  call 0x14025fa10
00AEFD80  E8 2B DB 76 FF                  call 0x14025d8b0
00AEFD85  BA 53 68 72 74                  mov edx, 0x74726853
00AEFD8A  48 8B CB                        mov rcx, rbx
00AEFD8D  E8 4E 7B 80 FF                  call 0x1402f78e0
00AEFD92  8B C7                           mov eax, edi
00AEFD94  E9 6C 07 00 00                  jmp 0x140af0505
00AEFD99  8B F8                           mov edi, eax
00AEFD9B  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFDA3  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFDA7  E8 64 FC 76 FF                  call 0x14025fa10
00AEFDAC  E8 FF DA 76 FF                  call 0x14025d8b0
00AEFDB1  BA 53 68 72 74                  mov edx, 0x74726853
00AEFDB6  48 8B CB                        mov rcx, rbx
00AEFDB9  E8 22 7B 80 FF                  call 0x1402f78e0
00AEFDBE  8B C7                           mov eax, edi
00AEFDC0  E9 40 07 00 00                  jmp 0x140af0505
00AEFDC5  41 8B CE                        mov ecx, r14d
00AEFDC8  83 E9 35                        sub ecx, 0x35
00AEFDCB  0F 84 BC EC FF FF               je 0x140aeea8d
00AEFDD1  83 E9 01                        sub ecx, 1
00AEFDD4  0F 84 81 04 00 00               je 0x140af025b
00AEFDDA  83 E9 01                        sub ecx, 1
00AEFDDD  0F 84 3F 03 00 00               je 0x140af0122
00AEFDE3  83 E9 01                        sub ecx, 1
00AEFDE6  0F 84 94 01 00 00               je 0x140aeff80
00AEFDEC  83 F9 02                        cmp ecx, 2
00AEFDEF  0F 85 CF D9 FF FF               jne 0x140aed7c4
00AEFDF5  0F 57 C0                        xorps xmm0, xmm0
00AEFDF8  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
00AEFE00  E8 C7 68 B1 FF                  call 0x1406066cc
00AEFE05  85 C0                           test eax, eax
00AEFE07  0F 84 B7 D9 FF FF               je 0x140aed7c4
00AEFE0D  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEFE15  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEFE1A  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEFE22  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEFE27  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEFE2F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEFE34  45 8A C5                        mov r8b, r13b
00AEFE37  BA 08 00 00 00                  mov edx, 8
00AEFE3C  48 8B CB                        mov rcx, rbx
00AEFE3F  E8 8C DC 8F FF                  call 0x1403edad0
00AEFE44  85 C0                           test eax, eax
00AEFE46  0F 88 B9 06 00 00               js 0x140af0505
00AEFE4C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEFE55  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEFE5C  90                              nop
00AEFE5D  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AEFE65  BA 01 00 00 00                  mov edx, 1
00AEFE6A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AEFE6E  E8 4D 1D 72 FF                  call 0x140211bc0
00AEFE73  8B 86 90 04 00 00               mov eax, dword ptr [rsi + 0x490]
00AEFE79  A8 02                           test al, 2
00AEFE7B  75 0A                           jne 0x140aefe87
00AEFE7D  BB 25 02 00 C0                  mov ebx, 0xc0000225
00AEFE82  E9 7E FA FF FF                  jmp 0x140aef905
00AEFE87  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
00AEFE8F  48 8B CE                        mov rcx, rsi
00AEFE92  E8 45 11 CB FF                  call 0x1407a0fdc
00AEFE97  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AEFE9E  BB 25 02 00 C0                  mov ebx, 0xc0000225
00AEFEA3  3B C3                           cmp eax, ebx
00AEFEA5  75 1D                           jne 0x140aefec4
00AEFEA7  48 8D 15 42 5F 01 00            lea rdx, [rip + 0x15f42]
00AEFEAE  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
00AEFEB6  E8 C5 A8 93 FF                  call 0x14042a780
00AEFEBB  8B C7                           mov eax, edi
00AEFEBD  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AEFEC4  85 C0                           test eax, eax
00AEFEC6  79 07                           jns 0x140aefecf
00AEFEC8  8B D8                           mov ebx, eax
00AEFECA  E9 36 FA FF FF                  jmp 0x140aef905
00AEFECF  44 0F B7 B4 24 00 01 00 00      movzx r14d, word ptr [rsp + 0x100]
00AEFED8  41 8D 5E 02                     lea ebx, [r14 + 2]
00AEFEDC  89 9C 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], ebx
00AEFEE3  45 84 ED                        test r13b, r13b
00AEFEE6  74 0C                           je 0x140aefef4
00AEFEE8  8B D3                           mov edx, ebx
00AEFEEA  49 8B CC                        mov rcx, r12
00AEFEED  E8 9A 5F C1 FF                  call 0x140705e8c
00AEFEF2  EB 04                           jmp 0x140aefef8
00AEFEF4  41 89 1C 24                     mov dword ptr [r12], ebx
00AEFEF8  39 9C 24 18 02 00 00            cmp dword ptr [rsp + 0x218], ebx
00AEFEFF  0F 82 27 DB FF FF               jb 0x140aeda2c
00AEFF05  49 8B DE                        mov rbx, r14
00AEFF08  4D 8B C6                        mov r8, r14
00AEFF0B  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
00AEFF13  49 8B CF                        mov rcx, r15
00AEFF16  E8 25 69 BD FF                  call 0x1406c6840
00AEFF1B  48 D1 EB                        shr rbx, 1
00AEFF1E  66 41 89 3C 5F                  mov word ptr [r15 + rbx*2], di
00AEFF23  E9 65 DB FF FF                  jmp 0x140aeda8d
00AEFF28  8B F8                           mov edi, eax
00AEFF2A  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFF32  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFF36  E8 D5 FA 76 FF                  call 0x14025fa10
00AEFF3B  E8 70 D9 76 FF                  call 0x14025d8b0
00AEFF40  BA 53 68 72 74                  mov edx, 0x74726853
00AEFF45  48 8B CB                        mov rcx, rbx
00AEFF48  E8 93 79 80 FF                  call 0x1402f78e0
00AEFF4D  8B C7                           mov eax, edi
00AEFF4F  E9 B1 05 00 00                  jmp 0x140af0505
00AEFF54  8B F8                           mov edi, eax
00AEFF56  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AEFF5E  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AEFF62  E8 A9 FA 76 FF                  call 0x14025fa10
00AEFF67  E8 44 D9 76 FF                  call 0x14025d8b0
00AEFF6C  BA 53 68 72 74                  mov edx, 0x74726853
00AEFF71  48 8B CB                        mov rcx, rbx
00AEFF74  E8 67 79 80 FF                  call 0x1402f78e0
00AEFF79  8B C7                           mov eax, edi
00AEFF7B  E9 85 05 00 00                  jmp 0x140af0505
00AEFF80  E8 E3 D9 AD FF                  call 0x1405cd968
00AEFF85  85 C0                           test eax, eax
00AEFF87  0F 84 37 D8 FF FF               je 0x140aed7c4
00AEFF8D  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AEFF95  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEFF9A  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AEFFA2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEFFA7  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AEFFAF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEFFB4  45 8A C5                        mov r8b, r13b
00AEFFB7  BE 08 00 00 00                  mov esi, 8
00AEFFBC  8B D6                           mov edx, esi
00AEFFBE  48 8B CB                        mov rcx, rbx
00AEFFC1  E8 0A DB 8F FF                  call 0x1403edad0
00AEFFC6  85 C0                           test eax, eax
00AEFFC8  0F 88 37 05 00 00               js 0x140af0505
00AEFFCE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEFFD7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AEFFDE  90                              nop
00AEFFDF  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AEFFE7  8D 5E F9                        lea ebx, [rsi - 7]
00AEFFEA  8A D3                           mov dl, bl
00AEFFEC  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AEFFF0  E8 CB 1B 72 FF                  call 0x140211bc0
00AEFFF5  49 8B 8E 98 04 00 00            mov rcx, qword ptr [r14 + 0x498]
00AEFFFC  48 85 C9                        test rcx, rcx
00AEFFFF  0F 84 93 03 00 00               je 0x140af0398
00AF0005  41 83 BE A0 04 00 00 03         cmp dword ptr [r14 + 0x4a0], 3
00AF000D  72 28                           jb 0x140af0037
00AF000F  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00AF0013  E8 88 83 B1 FF                  call 0x1406083a0
00AF0018  84 C0                           test al, al
00AF001A  74 1B                           je 0x140af0037
00AF001C  49 8B 86 98 04 00 00            mov rax, qword ptr [r14 + 0x498]
00AF0023  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00AF0027  44 8A C3                        mov r8b, bl
00AF002A  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AF002E  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
00AF0035  EB 08                           jmp 0x140af003f
00AF0037  44 8A 84 24 98 00 00 00         mov r8b, byte ptr [rsp + 0x98]
00AF003F  41 89 34 24                     mov dword ptr [r12], esi
00AF0043  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AF004A  0F 82 4C D8 FF FF               jb 0x140aed89c
00AF0050  45 84 C0                        test r8b, r8b
00AF0053  75 51                           jne 0x140af00a6
00AF0055  49 89 3F                        mov qword ptr [r15], rdi
00AF0058  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF005C  E8 AF F9 76 FF                  call 0x14025fa10
00AF0061  E8 4A D8 76 FF                  call 0x14025d8b0
00AF0066  BA 53 68 72 74                  mov edx, 0x74726853
00AF006B  49 8B CE                        mov rcx, r14
00AF006E  E8 6D 78 80 FF                  call 0x1402f78e0
00AF0073  33 C0                           xor eax, eax
00AF0075  E9 8B 04 00 00                  jmp 0x140af0505
00AF007A  8B F8                           mov edi, eax
00AF007C  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF0084  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0088  E8 83 F9 76 FF                  call 0x14025fa10
00AF008D  E8 1E D8 76 FF                  call 0x14025d8b0
00AF0092  BA 53 68 72 74                  mov edx, 0x74726853
00AF0097  48 8B CB                        mov rcx, rbx
00AF009A  E8 41 78 80 FF                  call 0x1402f78e0
00AF009F  8B C7                           mov eax, edi
00AF00A1  E9 5F 04 00 00                  jmp 0x140af0505
00AF00A6  49 8D 57 08                     lea rdx, [r15 + 8]
00AF00AA  49 89 17                        mov qword ptr [r15], rdx
00AF00AD  48 85 D2                        test rdx, rdx
00AF00B0  74 13                           je 0x140af00c5
00AF00B2  4D 8B 86 98 04 00 00            mov r8, qword ptr [r14 + 0x498]
00AF00B9  8D 4E F8                        lea ecx, [rsi - 8]
00AF00BC  4D 8B 40 20                     mov r8, qword ptr [r8 + 0x20]
00AF00C0  E8 8B 99 EB FF                  call 0x1409a9a50
00AF00C5  E9 0E D8 FF FF                  jmp 0x140aed8d8
00AF00CA  8B F8                           mov edi, eax
00AF00CC  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF00D4  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF00D8  E8 33 F9 76 FF                  call 0x14025fa10
00AF00DD  E8 CE D7 76 FF                  call 0x14025d8b0
00AF00E2  BA 53 68 72 74                  mov edx, 0x74726853
00AF00E7  48 8B CB                        mov rcx, rbx
00AF00EA  E8 F1 77 80 FF                  call 0x1402f78e0
00AF00EF  8B C7                           mov eax, edi
00AF00F1  E9 0F 04 00 00                  jmp 0x140af0505
00AF00F6  8B F8                           mov edi, eax
00AF00F8  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF0100  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0104  E8 07 F9 76 FF                  call 0x14025fa10
00AF0109  E8 A2 D7 76 FF                  call 0x14025d8b0
00AF010E  BA 53 68 72 74                  mov edx, 0x74726853
00AF0113  48 8B CB                        mov rcx, rbx
00AF0116  E8 C5 77 80 FF                  call 0x1402f78e0
00AF011B  8B C7                           mov eax, edi
00AF011D  E9 E3 03 00 00                  jmp 0x140af0505
00AF0122  E8 41 D8 AD FF                  call 0x1405cd968
00AF0127  85 C0                           test eax, eax
00AF0129  0F 84 95 D6 FF FF               je 0x140aed7c4
00AF012F  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AF0137  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF013C  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AF0144  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF0149  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AF0151  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF0156  45 8A C5                        mov r8b, r13b
00AF0159  BE 08 00 00 00                  mov esi, 8
00AF015E  8B D6                           mov edx, esi
00AF0160  48 8B CB                        mov rcx, rbx
00AF0163  E8 68 D9 8F FF                  call 0x1403edad0
00AF0168  85 C0                           test eax, eax
00AF016A  0F 88 95 03 00 00               js 0x140af0505
00AF0170  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0179  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0180  90                              nop
00AF0181  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AF0189  8D 56 F9                        lea edx, [rsi - 7]
00AF018C  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF0190  E8 2B 1A 72 FF                  call 0x140211bc0
00AF0195  49 8B 8E 98 04 00 00            mov rcx, qword ptr [r14 + 0x498]
00AF019C  48 85 C9                        test rcx, rcx
00AF019F  0F 84 F3 01 00 00               je 0x140af0398
00AF01A5  41 83 BE A0 04 00 00 02         cmp dword ptr [r14 + 0x4a0], 2
00AF01AD  0F 82 E5 01 00 00               jb 0x140af0398
00AF01B3  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00AF01B7  48 85 C9                        test rcx, rcx
00AF01BA  74 0B                           je 0x140af01c7
00AF01BC  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AF01C0  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
00AF01C7  41 89 34 24                     mov dword ptr [r12], esi
00AF01CB  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AF01D2  0F 82 C4 D6 FF FF               jb 0x140aed89c
00AF01D8  49 8D 57 08                     lea rdx, [r15 + 8]
00AF01DC  48 85 C9                        test rcx, rcx
00AF01DF  48 0F 44 D1                     cmove rdx, rcx
00AF01E3  49 89 17                        mov qword ptr [r15], rdx
00AF01E6  48 85 D2                        test rdx, rdx
00AF01E9  74 13                           je 0x140af01fe
00AF01EB  4D 8B 86 98 04 00 00            mov r8, qword ptr [r14 + 0x498]
00AF01F2  8D 4E F8                        lea ecx, [rsi - 8]
00AF01F5  4D 8B 40 10                     mov r8, qword ptr [r8 + 0x10]
00AF01F9  E8 52 98 EB FF                  call 0x1409a9a50
00AF01FE  E9 32 01 00 00                  jmp 0x140af0335
00AF0203  8B F8                           mov edi, eax
00AF0205  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF020D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0211  E8 FA F7 76 FF                  call 0x14025fa10
00AF0216  E8 95 D6 76 FF                  call 0x14025d8b0
00AF021B  BA 53 68 72 74                  mov edx, 0x74726853
00AF0220  48 8B CB                        mov rcx, rbx
00AF0223  E8 B8 76 80 FF                  call 0x1402f78e0
00AF0228  8B C7                           mov eax, edi
00AF022A  E9 D6 02 00 00                  jmp 0x140af0505
00AF022F  8B F8                           mov edi, eax
00AF0231  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF0239  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF023D  E8 CE F7 76 FF                  call 0x14025fa10
00AF0242  E8 69 D6 76 FF                  call 0x14025d8b0
00AF0247  BA 53 68 72 74                  mov edx, 0x74726853
00AF024C  48 8B CB                        mov rcx, rbx
00AF024F  E8 8C 76 80 FF                  call 0x1402f78e0
00AF0254  8B C7                           mov eax, edi
00AF0256  E9 AA 02 00 00                  jmp 0x140af0505
00AF025B  E8 08 D7 AD FF                  call 0x1405cd968
00AF0260  85 C0                           test eax, eax
00AF0262  0F 84 5C D5 FF FF               je 0x140aed7c4
00AF0268  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AF0270  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF0275  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00AF027D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF0282  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AF028A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF028F  45 8A C5                        mov r8b, r13b
00AF0292  BE 08 00 00 00                  mov esi, 8
00AF0297  8B D6                           mov edx, esi
00AF0299  48 8B CB                        mov rcx, rbx
00AF029C  E8 2F D8 8F FF                  call 0x1403edad0
00AF02A1  85 C0                           test eax, eax
00AF02A3  0F 88 5C 02 00 00               js 0x140af0505
00AF02A9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF02B2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF02B9  90                              nop
00AF02BA  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00AF02C2  8D 56 F9                        lea edx, [rsi - 7]
00AF02C5  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF02C9  E8 F2 18 72 FF                  call 0x140211bc0
00AF02CE  49 8B 8E 98 04 00 00            mov rcx, qword ptr [r14 + 0x498]
00AF02D5  48 85 C9                        test rcx, rcx
00AF02D8  0F 84 BA 00 00 00               je 0x140af0398
00AF02DE  41 39 BE A0 04 00 00            cmp dword ptr [r14 + 0x4a0], edi
00AF02E5  0F 84 AD 00 00 00               je 0x140af0398
00AF02EB  48 8B 09                        mov rcx, qword ptr [rcx]
00AF02EE  48 85 C9                        test rcx, rcx
00AF02F1  74 0B                           je 0x140af02fe
00AF02F3  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AF02F7  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
00AF02FE  41 89 34 24                     mov dword ptr [r12], esi
00AF0302  39 B4 24 18 02 00 00            cmp dword ptr [rsp + 0x218], esi
00AF0309  0F 82 8D D5 FF FF               jb 0x140aed89c
00AF030F  49 8D 57 08                     lea rdx, [r15 + 8]
00AF0313  48 85 C9                        test rcx, rcx
00AF0316  48 0F 44 D1                     cmove rdx, rcx
00AF031A  49 89 17                        mov qword ptr [r15], rdx
00AF031D  48 85 D2                        test rdx, rdx
00AF0320  74 13                           je 0x140af0335
00AF0322  4D 8B 86 98 04 00 00            mov r8, qword ptr [r14 + 0x498]
00AF0329  8D 4E F8                        lea ecx, [rsi - 8]
00AF032C  4D 8B 00                        mov r8, qword ptr [r8]
00AF032F  E8 1C 97 EB FF                  call 0x1409a9a50
00AF0334  90                              nop
00AF0335  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF0339  E8 D2 F6 76 FF                  call 0x14025fa10
00AF033E  EB 66                           jmp 0x140af03a6
00AF0340  8B F8                           mov edi, eax
00AF0342  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF034A  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF034E  E8 BD F6 76 FF                  call 0x14025fa10
00AF0353  E8 58 D5 76 FF                  call 0x14025d8b0
00AF0358  BA 53 68 72 74                  mov edx, 0x74726853
00AF035D  48 8B CB                        mov rcx, rbx
00AF0360  E8 7B 75 80 FF                  call 0x1402f78e0
00AF0365  8B C7                           mov eax, edi
00AF0367  E9 99 01 00 00                  jmp 0x140af0505
00AF036C  8B F8                           mov edi, eax
00AF036E  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AF0376  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF037A  E8 91 F6 76 FF                  call 0x14025fa10
00AF037F  E8 2C D5 76 FF                  call 0x14025d8b0
00AF0384  BA 53 68 72 74                  mov edx, 0x74726853
00AF0389  48 8B CB                        mov rcx, rbx
00AF038C  E8 4F 75 80 FF                  call 0x1402f78e0
00AF0391  8B C7                           mov eax, edi
00AF0393  E9 6D 01 00 00                  jmp 0x140af0505
00AF0398  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF039C  E8 6F F6 76 FF                  call 0x14025fa10
00AF03A1  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AF03A6  E8 05 D5 76 FF                  call 0x14025d8b0
00AF03AB  49 8B CE                        mov rcx, r14
00AF03AE  E9 24 DC FF FF                  jmp 0x140aedfd7
00AF03B3  41 83 FE 17                     cmp r14d, 0x17
00AF03B7  75 16                           jne 0x140af03cf
00AF03B9  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF03C1  8B BE C8 00 00 00               mov edi, dword ptr [rsi + 0xc8]
00AF03C7  C1 EF 09                        shr edi, 9
00AF03CA  E9 FD 00 00 00                  jmp 0x140af04cc
00AF03CF  41 B8 18 00 00 00               mov r8d, 0x18
00AF03D5  45 3B F0                        cmp r14d, r8d
00AF03D8  75 16                           jne 0x140af03f0
00AF03DA  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF03E2  8B BE C8 00 00 00               mov edi, dword ptr [rsi + 0xc8]
00AF03E8  C1 EF 0A                        shr edi, 0xa
00AF03EB  E9 DC 00 00 00                  jmp 0x140af04cc
00AF03F0  41 83 FE 1A                     cmp r14d, 0x1a
00AF03F4  75 16                           jne 0x140af040c
00AF03F6  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF03FE  8B BE C8 00 00 00               mov edi, dword ptr [rsi + 0xc8]
00AF0404  C1 EF 0C                        shr edi, 0xc
00AF0407  E9 C0 00 00 00                  jmp 0x140af04cc
00AF040C  41 83 FE 28                     cmp r14d, 0x28
00AF0410  75 1A                           jne 0x140af042c
00AF0412  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF041A  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
00AF0420  41 84 C0                        test r8b, al
00AF0423  40 0F 95 C7                     setne dil
00AF0427  E9 A3 00 00 00                  jmp 0x140af04cf
00AF042C  41 83 FE 2A                     cmp r14d, 0x2a
00AF0430  75 14                           jne 0x140af0446
00AF0432  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF043A  0F B7 BE CA 00 00 00            movzx edi, word ptr [rsi + 0xca]
00AF0441  E9 86 00 00 00                  jmp 0x140af04cc
00AF0446  41 83 FE 2F                     cmp r14d, 0x2f
00AF044A  75 15                           jne 0x140af0461
00AF044C  41 8A D5                        mov dl, r13b
00AF044F  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF0457  48 8B CE                        mov rcx, rsi
00AF045A  E8 A5 82 96 FF                  call 0x140458704
00AF045F  EB 55                           jmp 0x140af04b6
00AF0461  41 83 FE 30                     cmp r14d, 0x30
00AF0465  75 2C                           jne 0x140af0493
00AF0467  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF046F  48 8D 8E 28 03 00 00            lea rcx, [rsi + 0x328]
00AF0476  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AF047B  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AF0480  45 33 C9                        xor r9d, r9d
00AF0483  4C 8B 05 4E 77 37 00            mov r8, qword ptr [rip + 0x37774e]
00AF048A  33 D2                           xor edx, edx
00AF048C  E8 4F 81 8D FF                  call 0x1403c85e0
00AF0491  EB 23                           jmp 0x140af04b6
00AF0493  41 83 FE 35                     cmp r14d, 0x35
00AF0497  75 22                           jne 0x140af04bb
00AF0499  E8 CA D4 AD FF                  call 0x1405cd968
00AF049E  85 C0                           test eax, eax
00AF04A0  0F 84 28 D3 FF FF               je 0x140aed7ce
00AF04A6  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF04AE  48 8B CE                        mov rcx, rsi
00AF04B1  E8 C6 72 B1 FF                  call 0x14060777c
00AF04B6  0F B6 F8                        movzx edi, al
00AF04B9  EB 14                           jmp 0x140af04cf
00AF04BB  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00AF04C3  8B BE C8 00 00 00               mov edi, dword ptr [rsi + 0xc8]
00AF04C9  C1 EF 0E                        shr edi, 0xe
00AF04CC  83 E7 01                        and edi, 1
00AF04CF  41 89 3F                        mov dword ptr [r15], edi
00AF04D2  E9 C4 D5 FF FF                  jmp 0x140aeda9b
00AF04D7  8B D8                           mov ebx, eax
00AF04D9  BA 53 68 72 74                  mov edx, 0x74726853
00AF04DE  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF04E6  E8 F5 73 80 FF                  call 0x1402f78e0
00AF04EB  8B C3                           mov eax, ebx
00AF04ED  EB 16                           jmp 0x140af0505
00AF04EF  8B D8                           mov ebx, eax
00AF04F1  BA 53 68 72 74                  mov edx, 0x74726853
00AF04F6  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF04FE  E8 DD 73 80 FF                  call 0x1402f78e0
00AF0503  8B C3                           mov eax, ebx
00AF0505  4C 8D 9C 24 D0 01 00 00         lea r11, [rsp + 0x1d0]
00AF050D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00AF0511  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00AF0515  49 8B E3                        mov rsp, r11
00AF0518  41 5F                           pop r15
00AF051A  41 5E                           pop r14
00AF051C  41 5D                           pop r13
00AF051E  41 5C                           pop r12
00AF0520  5F                              pop rdi
00AF0521  C3                              ret
00AF0522  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryInformationToken(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned __int8 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int8 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_mFC;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (464);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 368) = 0;
    *(unsigned int *)(v_rsp - 348) = 0;
    *(unsigned int *)(v_rsp - 252) = 0;
    *(unsigned int *)(v_rsp - 256) = 0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    *(unsigned int *)(v_rsp - 320) = 0;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 336) = 0;
    *(unsigned int *)(v_rsp - 324) = 0;
    *(unsigned __int8 *)(v_rsp - 296) = 0;
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 184) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 168) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 152) = v_xmm1;
    v_stack_m160 = 0;
    *(unsigned __int8 *)(v_rsp - 376) = 0;
    *(unsigned __int64 *)(v_rsp - 360) = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AECEBB;
    result = ProbeForWrite(a3, (unsigned int)((unsigned int)((unsigned int)(a4))), v_rdi + 4, a4);
    if (a5 < a3) { a3 = a5; }
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_00AECEC3;
loc_00AECEBB:
loc_00AECEC3:
    if (((unsigned int)((unsigned int)(a2))) > 25) goto loc_00AEEFB4;
    if (((unsigned int)((unsigned int)(a2))) == 25) goto loc_00AEEE78;
    if (((unsigned int)((unsigned int)(a2))) > 12) goto loc_00AEDF2B;
    if (((unsigned int)((unsigned int)(a2))) == 12) goto loc_00AEDE6B;
    if (((unsigned int)((unsigned int)(a2))) > 6) goto loc_00AED946;
    if (((unsigned int)((unsigned int)(a2))) == 6) goto loc_00AED7FB;
    if (((unsigned int)((unsigned int)(a2))) == -2) goto loc_00AED51B;
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_00AED3BB;
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_00AED24F;
    if (((unsigned int)((unsigned int)(a2))) == 3) goto loc_00AED147;
    if (((unsigned int)((unsigned int)(a2))) == 4) goto loc_00AED02F;
    if (((unsigned int)((unsigned int)(a2))) != 5) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 1 + 7, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    *(unsigned int *)(a5) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m170 + 168) + 1) * 4 + 16);
    if (v_stack_p20 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m170 + 168) + 1) * 4 + 16))) goto loc_00AED447;
    *(unsigned __int64 *)(a3) = a3 + 8;
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m170 + 168) + 1) * 4 + 16) + (-8));
    result = RtlCopySid(a1, a3 + 8, *(unsigned __int64 *)(v_stack_m170 + 168), a4);
    goto loc_00AED4A1;
loc_00AED02F:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m170 + 144))) + ((unsigned int)(*(unsigned int *)(v_stack_m170 + 144)));
    *(unsigned int *)(a5) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a1 * 8) + 1) * 4 + 16);
    if (v_stack_p20 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a1 * 8) + 1) * 4 + 16))) goto loc_00AED447;
    *(unsigned __int64 *)(a3) = a3 + 8;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m170 + 144))) + ((unsigned int)(*(unsigned int *)(v_stack_m170 + 144)));
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a1 * 8) + 1) * 4 + 16) + (-8));
    result = RtlCopySid(a1, a3 + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + result * 8), a4);
    goto loc_00AED4A1;
loc_00AED147:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = SepTokenPrivilegeCount(v_stack_m170, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (((unsigned int)(result)) <= 1) goto loc_00AED1C8;
    goto loc_00AED1CE;
loc_00AED1C8:
loc_00AED1CE:
    *(unsigned int *)(a5) = 16;
    if (v_stack_p20 < 16) goto loc_00AED447;
    result = SepConvertTokenPrivileges(v_stack_m170, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    goto loc_00AED4A1;
loc_00AED24F:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))))) << (4));
    a3 = (unsigned int)((a3) + (-8));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124)))) <= 1) goto loc_00AED2F4;
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 152)) + (16);
loc_00AED2DD:
    a3 = (unsigned int)((a3 + *(unsigned __int8 *)(*(unsigned __int64 *)(a2) + 1) * 4) + (8));
    a2 = (a2) + (16);
    a4 = ((unsigned int)(*(unsigned int *)(v_stack_m170 + 124)) - 1) - (1);
    if (condition_is_not_equal) goto loc_00AED2DD;
loc_00AED2F4:
    *(unsigned int *)(a5) = (unsigned int)(a3);
    if (v_stack_p20 < ((unsigned int)(a3))) goto loc_00AED447;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))) - (1));
    *(unsigned int *)(a3) = (unsigned int)(result);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))))) << (4));
    v_r10 = (unsigned int)((v_r10) - (32));
    v_r10 = (v_r10) + (24);
    v_r10 = (v_r10) + (a3);
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 152)) + (16);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))) - 1);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = v_r10;
    result = RtlCopySidAndAttributesArray(a1, a2, a3, a3 + 8);
    goto loc_00AED4A1;
loc_00AED3BB:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3 + 8);
    *(unsigned int *)(16) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24);
    if (v_stack_p20 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24))) goto loc_00AED46C;
loc_00AED447:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3 + 8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), 1, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3 + 8);
loc_00AED458:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3 + 8);
loc_00AED462:
    goto loc_00AF0505;
loc_00AED46C:
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = a3 + 16;
    result = RtlCopySidAndAttributesArray(1, *(unsigned __int64 *)(v_stack_m170 + 152), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3);
loc_00AED4A1:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(v_stack_m170 + 152), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(v_stack_m170 + 152), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3);
loc_00AED4AF:
loc_00AED4B2:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3);
    result = 0;
    goto loc_00AF0505;
loc_00AED51B:
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(v_stack_m170, (unsigned int)(0x74726853ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3);
    if ((unsigned int)(result) == 0) goto loc_00AED7C4;
    v_stack_m138 = v_stack_m170;
    v_stack_m130 = v_stack_m170;
    v_stack_m158 = v_stack_m170;
    v_stack_mE4 = (unsigned int)(v_stack_m170);
    v_stack_mCC = (unsigned int)(v_stack_m170);
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5162272), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 24, a3);
    if ((unsigned __int8)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 8;
    if (v_stack_p20 != 8) goto loc_00AEE54A;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(1, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3);
    if ((unsigned int)(result) == 0) goto loc_00AED7CE;
    v_stack_m148 = (unsigned int)(v_stack_m170);
    result = RtlQueryElevationFlags(v_stack_m148, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3);
    result = (unsigned __int8)(((unsigned int)(v_stack_m148)) & (24));
    if (((unsigned __int8)(result)) != 16) goto loc_00AED7B2;
    result = SepGetTokenElevationType(v_stack_m170, v_stack_m170, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3);
    if (((unsigned int)(result)) != 2) goto loc_00AED7B2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 28))) | (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 24)));
    if (condition_is_equal) goto loc_00AED7B2;
    result = SepReferenceLogonSessionSilo(*(unsigned __int64 *)(v_stack_m170 + 216) + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 168), v_stack_m138, a3);
    if (sign_flag) goto loc_00AEE9F9;
    v_stack_mE8 = 48;
    v_stack_mE0 = v_stack_m170;
    v_r13 = (unsigned __int8)(-(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (512));
    v_stack_mD0 = (unsigned int)(result);
    v_stack_mD8 = v_stack_m170;
    v_stack_mC8 = v_xmm0;
    result = SeQuerySessionIdToken(v_stack_m170, v_stack_m144, v_stack_m138, a3);
    result = SeSetSessionIdToken(*(unsigned __int64 *)(v_stack_m138 + 56), (unsigned int)(v_stack_m144), v_stack_m138, a3);
    if (!sign_flag) goto loc_00AED6B7;
    result = SepDeReferenceLogonSessionDirect(v_stack_m138, (unsigned int)(v_stack_m144), v_stack_m138, a3);
    goto loc_00AEE9F9;
loc_00AED6B7:
    v_stack_m1C0 = v_stack_m158;
    v_stack_m1C8 = (unsigned __int8)(v_stack_m170);
    v_stack_m1D0 = (unsigned __int8)(v_stack_m170);
    v_stack_m1D8 = 1;
    a3 = 0;
    result = SepDuplicateToken(*(unsigned __int64 *)(v_stack_m138 + 56), v_stack_mE8, a3, 1);
    result = SepDeReferenceLogonSessionDirect(v_stack_m138, v_stack_mE8, a3, 1);
    if (sign_flag) goto loc_00AEE9F9;
    a1 = (*(unsigned __int64 *)(v_stack_m158 + 216)) + (16);
    result = SepReferenceLogonSession(a1, v_stack_m138, a3, 1);
    if (sign_flag) goto loc_00AED769;
    v_stack_m1C8 = v_stack_m130;
    v_stack_m1D0 = v_stack_m170;
    v_stack_m1D8 = (unsigned int)(v_stack_m170);
    a4 = 0;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_m158, a2, (unsigned int)(0xF01FFULL), a4);
    if (!sign_flag) goto loc_00AED77B;
loc_00AED769:
    result = ObfDereferenceObject(v_stack_m158, a2, (unsigned int)(0xF01FFULL), a4);
    goto loc_00AEE9F9;
loc_00AED77B:
    *(unsigned __int64 *)(a3) = v_stack_m130;
    v_rdi = 0;
    goto loc_00AED7D3;
loc_00AED7B2:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), (unsigned int)(0xF01FFULL), a4);
loc_00AED7C4:
    goto loc_00AF0505;
loc_00AED7CE:
loc_00AED7D3:
    goto loc_00AEDFD7;
loc_00AED7FB:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    v_stack_m15C = 8;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 8 - 7, (unsigned __int8)(v_r13), a4);
    result = *(unsigned __int64 *)(v_stack_m170 + 184);
    if (*(unsigned __int64 *)(v_stack_m170 + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 184) + 2);
        result = (unsigned int)((result) + (8));
        v_stack_m15C = (unsigned int)(result);
    }
    *(unsigned int *)(16) = (unsigned int)((unsigned int)(v_stack_m15C));
    if (((unsigned int)((unsigned int)(v_stack_p20))) >= v_stack_m15C) goto loc_00AED8B2;
loc_00AED89C:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned int)(v_stack_p20), (unsigned __int8)(v_r13), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned int)(v_stack_p20), (unsigned __int8)(v_r13), a4);
    goto loc_00AED458;
loc_00AED8B2:
    if ((*(unsigned __int64 *)(v_stack_m170 + 184)) == ((unsigned int)(0xC0000003ULL))) goto loc_00AED8D5;
    *(unsigned __int64 *)(a3) = a3 + 8;
    result = memcpy(a3 + 8, *(unsigned __int64 *)(v_stack_m170 + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 184) + 2), a4);
    goto loc_00AED8D8;
loc_00AED8D5:
    *(unsigned __int64 *)(a3) = (unsigned int)(0xC0000003ULL);
loc_00AED8D8:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(v_stack_m170 + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 184) + 2), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(v_stack_m170 + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 184) + 2), a4);
    goto loc_00AED4B2;
loc_00AED946:
    v_r14 = (unsigned int)((v_stack_m170) - (7));
    if (condition_is_equal) goto loc_00AEDDC0;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00AEDD1F;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00AEDC62;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00AEDAFB;
    if (((unsigned int)(v_r14)) != 1) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), v_r14 + 7, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned __int8)((unsigned int)((unsigned int)(v_r14))), (unsigned __int8)(v_r13), a4);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))))) << (4));
    a3 = (unsigned int)((a3) + (8));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))) == 0) goto loc_00AEDA17;
loc_00AEDA00:
    a3 = (unsigned int)((a3 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 160)) + 1) * 4) + (8));
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 160)) + (v_r14 + 15);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))))) - ((unsigned int)((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_00AEDA00;
loc_00AEDA17:
    *(unsigned int *)(a5) = (unsigned int)(a3);
    if (v_stack_p20 >= ((unsigned int)(a3))) goto loc_00AEDA42;
loc_00AEDA2C:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), a2, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), a2, a3, a4);
    goto loc_00AED458;
loc_00AEDA42:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))))) << (4));
    a2 = (a2) + (8);
    a2 = (a2) + (a3);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = a2;
    result = RtlCopySidAndAttributesArray((unsigned int)(*(unsigned int *)(v_stack_m170 + 128)), *(unsigned __int64 *)(v_stack_m170 + 160), a3, a3 + 8);
loc_00AEDA8D:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(v_stack_m170 + 160), a3, a3 + 8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(v_stack_m170 + 160), a3, a3 + 8);
loc_00AEDA9B:
    goto loc_00AED4B2;
loc_00AEDAFB:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(v_r14)), 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(v_r14 + 15) = 56;
    if (v_stack_p20 < 56) goto loc_00AEDE13;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a3 + 8);
    v_stack_m124 = (unsigned int)((unsigned int)(0xC0000003ULL));
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_stack_m170 + 16);
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(v_stack_m170 + 24);
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(v_stack_m170 + 40);
    *(unsigned int *)(a3 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 192)));
    *(unsigned int *)(a3 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 196)));
    *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 136)));
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m170 + 168) + 1)) << (2));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 136))) - ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) - (8));
    v_stack_m124 = a2;
    result = *(unsigned __int64 *)(v_stack_m170 + 184);
    if (*(unsigned __int64 *)(v_stack_m170 + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 184) + 2);
        a2 = (unsigned int)((a2) - ((unsigned int)(result)));
        v_stack_m124 = a2;
    }
    *(unsigned int *)(a3 + 36) = a2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))) - (1));
    *(unsigned int *)(a3 + 40) = (unsigned int)(result);
    result = SepTokenPrivilegeCount(v_stack_m170, a2, (unsigned __int8)(v_r13), a3 + 8);
    *(unsigned int *)(a3 + 44) = (unsigned int)(result);
    *(unsigned __int64 *)(a3 + 48) = *(unsigned __int64 *)(v_stack_m170 + 56);
    goto loc_00AED8D8;
loc_00AEDC62:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    if ((*(unsigned int *)(v_stack_m170 + 192)) == 2) goto loc_00AEDCBD;
    goto loc_00AEDFD4;
loc_00AEDCBD:
    *(unsigned int *)(v_r14 + 15) = 4;
    if (v_stack_p20 >= 4) goto loc_00AEDCD7;
    goto loc_00AED458;
loc_00AEDCD7:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 196)));
    goto loc_00AED4B2;
loc_00AEDD1F:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(v_r14 + 15) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 192)));
    goto loc_00AED4B2;
loc_00AEDDC0:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 16, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(a5) = 16;
    if (8 >= 16) goto loc_00AEDE20;
loc_00AEDE13:
    goto loc_00AED458;
loc_00AEDE20:
    *(unsigned __int64 *)(a3) = v_xmm0;
    goto loc_00AED4B2;
loc_00AEDE6B:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AED458;
    result = SeQuerySessionIdToken(v_stack_m170, v_stack_m144, (unsigned __int8)(v_r13), a3 + 8);
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(v_stack_m144));
    *(unsigned int *)(16) = 4;
loc_00AEDEE8:
    goto loc_00AED4B2;
loc_00AEDF2B:
    if (((unsigned int)(v_stack_m170)) > 19) goto loc_00AEEA65;
    if (((unsigned int)(v_stack_m170)) == 19) goto loc_00AEE4CB;
    v_r14 = (unsigned int)((v_stack_m170) - (13));
    if (condition_is_equal) goto loc_00AEE25E;
    v_r14 = (unsigned int)((v_r14) - (2));
    if (condition_is_equal) goto loc_00AEE1CD;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00AEE0BD;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00AEE01E;
    if (((unsigned int)(v_r14)) != 1) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, v_r14 + 7, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    result = SepGetTokenElevationType(v_stack_m170, v_r14 + 7, v_stack_m170, a3 + 8);
    *(unsigned int *)(a3) = (unsigned int)(result);
loc_00AEDFD4:
loc_00AEDFD7:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), v_stack_m170, a3 + 8);
    goto loc_00AF0505;
loc_00AEE01E:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 8;
    if (v_stack_p20 < 8) goto loc_00AEDE13;
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_stack_m170 + 224);
    goto loc_00AED4B2;
loc_00AEE0BD:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5159481), (unsigned __int8)(v_r13), (unsigned __int8)(v_r13), a3 + 8);
    if ((unsigned __int8)(result) != 0) goto loc_00AEE0DA;
    goto loc_00AF0505;
loc_00AEE0DA:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 31;
    if (v_stack_p20 < 31) goto loc_00AEDE13;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a3 + 8);
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm1;
    *(unsigned int *)(a3 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 112)));
    *(unsigned __int16 *)(a3 + 28) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m170 + 116));
    *(unsigned __int8 *)(a3 + 30) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m170 + 118));
    goto loc_00AED4A1;
loc_00AEE1CD:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AED462;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 200))) >> (6));
    result = (unsigned int)((result) & (1));
    *(unsigned int *)(a3) = (unsigned int)(result);
    goto loc_00AED4B2;
loc_00AEE25E:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a3 + 8);
    result = SepTokenPrivilegeCount(v_stack_m170, 1, (unsigned __int8)(v_r13), a3 + 8);
    v_stack_m140 = (unsigned int)(result);
    v_r11 = (unsigned int)((result + result * 2) << (2));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))))) << (4));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))) == 0) goto loc_00AEE318;
loc_00AEE2FC:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)) + 1) * 4 + 15) & (0xFFFFFFF8ULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + ((unsigned int)(a1)));
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 152)) + (1 + 15);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))))) - (1);
    if (condition_is_not_equal) goto loc_00AEE2FC;
loc_00AEE318:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))))) << (4));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))) == 0) goto loc_00AEE358;
loc_00AEE339:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 160)) + 1) * 4 + 15) & (0xFFFFFFF8ULL));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) + ((unsigned int)(a1)));
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 160)) + (1 + 15);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128))))) - (1);
    if (condition_is_not_equal) goto loc_00AEE339;
loc_00AEE358:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) + (56));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r11)));
    a1 = (unsigned int)((a1) + ((unsigned int)(a3)));
    *(unsigned int *)(a5) = (unsigned int)(a1);
    if (v_stack_p20 < ((unsigned int)(a1))) goto loc_00AEDA2C;
    *(unsigned __int64 *)(a3 + 48) = *(unsigned __int64 *)(v_stack_m170 + 24);
    *(unsigned int *)(a3 + 4) = (unsigned int)(a3);
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124)));
    *(unsigned __int64 *)(a3 + 8) = a3 + 56;
    *(unsigned int *)(a3 + 20) = (unsigned int)(v_r14);
    *(unsigned int *)(a3 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 128)));
    if ((*(unsigned int *)(v_stack_m170 + 128)) == ((unsigned int)(v_stack_m170))) goto loc_00AEE3BC;
    v_rbx = ((unsigned int)((unsigned int)(a3))) + (7);
    v_rbx = (v_rbx) & (-8);
    v_rbx = (v_rbx) + (a3 + 56);
    *(unsigned __int64 *)(a3 + 24) = v_rbx;
    goto loc_00AEE3C8;
loc_00AEE3BC:
    *(unsigned __int64 *)(a3 + 24) = v_stack_m170;
loc_00AEE3C8:
    *(unsigned int *)(a3 + 36) = (unsigned int)(v_r11);
    *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)(v_stack_m140));
    result = ((unsigned int)((unsigned int)(v_r14))) + (a3 + 56);
    v_r12 = ((unsigned int)((unsigned int)(a3))) + (result);
    *(unsigned __int64 *)(a3 + 40) = v_r12;
    result = ((unsigned int)((unsigned int)(v_r10))) + (a3 + 56);
    a3 = (unsigned int)((a3) - ((unsigned int)(v_r10)));
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = result;
    result = RtlCopySidAndAttributesArray((unsigned int)(*(unsigned int *)(v_stack_m170 + 124)), *(unsigned __int64 *)(v_stack_m170 + 152), a3, a3 + 56);
    result = ((unsigned int)((unsigned int)(v_r13))) + (v_stack_m88);
    if (v_stack_m88 != 0) {
        v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_r13)));
        a1 = v_stack_m150;
        v_stack_m1C8 = a1;
        a1 = v_stack_m150;
        v_stack_m1D0 = a1;
        v_stack_m1D8 = result;
        a4 = v_stack_m88;
        a3 = (unsigned int)(v_r14);
        a2 = *(unsigned __int64 *)(v_stack_m170 + 160);
        a1 = *(unsigned int *)(v_stack_m170 + 128);
        result = RtlCopySidAndAttributesArray(a1, a2, a3, a4);
    }
    result = SepConvertTokenPrivilegesToLuidAndAttributes(v_stack_m170, v_r12, a3, a4);
    goto loc_00AEDA8D;
loc_00AEE4CB:
    v_stack_m158 = v_stack_m170;
    v_stack_m138 = v_stack_m170;
    v_stack_m118 = v_stack_m170;
    v_stack_m6C = (unsigned int)(v_stack_m170);
    v_stack_m54 = (unsigned int)(v_stack_m170);
    v_stack_m160 = (unsigned __int8)(v_stack_m170);
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_m88, 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(v_r12) = 8;
    if (v_stack_p20 == 8) goto loc_00AEE554;
loc_00AEE54A:
    goto loc_00AEE9F9;
loc_00AEE554:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(v_stack_m88, 8, (unsigned __int8)(v_r13), a4);
    v_r14 = (unsigned __int8)(v_stack_m170);
    if ((unsigned int)(result) != 0) {
        v_stack_m148 = (unsigned int)(v_stack_m170);
        a1 = v_stack_m148;
        result = RtlQueryElevationFlags(a1, 8, (unsigned __int8)(v_r13), a4);
        result = v_stack_m148;
        result = (unsigned __int8)((result) & (24));
        v_r12 = 16;
        v_r14 = (((unsigned __int8)(result)) == ((unsigned __int8)(v_r12))) ? 1 : 0;
        v_stack_m160 = (unsigned __int8)(v_r14);
    }
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5158111), (unsigned __int8)(v_r13), (unsigned __int8)(v_r13), a4);
    v_stack_m178 = (unsigned __int8)(result);
    a1 = (unsigned __int8)(-((unsigned __int8)(result)));
    result = (unsigned int)((result) + (2));
    v_stack_m140 = (unsigned int)(result);
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(a1, (unsigned __int8)(v_r13), (unsigned __int8)(v_r13), a4);
    if ((unsigned int)(result) == 0) goto loc_00AEE726;
    if ((unsigned __int8)(v_r14) == 0) goto loc_00AEE726;
    result = SepGetTokenElevationType(v_stack_m170, (unsigned __int8)(v_r13), (unsigned __int8)(v_r13), a4);
    if (((unsigned int)(result)) != 3) goto loc_00AEE726;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 20))) | (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 16)));
    if (condition_is_not_equal) goto loc_00AEE726;
    v_stack_m130 = v_stack_m170;
    result = SepLogonSystemManagedAdmin(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 8), v_stack_m130, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AEE9F7;
    v_stack_m110 = v_stack_m170;
    v_stack_m1D0 = v_stack_m170;
    v_stack_m1D8 = v_stack_m110;
    a4 = 0;
    result = ObReferenceObjectByHandle(v_stack_m130, 8, *(unsigned __int64 *)(v_rip + 5151231), a4);
    a2 = 0;
    result = ObCloseHandle(v_stack_m130, a2, *(unsigned __int64 *)(v_rip + 5151231), a4);
    if (sign_flag) goto loc_00AEE9F9;
    result = SepReferenceLogonSessionSilo(v_stack_m110 + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 168), v_stack_m158, a4);
    result = ObfDereferenceObject(v_stack_m110, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 168), v_stack_m158, a4);
    if (!sign_flag) goto loc_00AEE6A5;
loc_00AEE69D:
    goto loc_00AEE9F9;
loc_00AEE6A5:
    result = SeQuerySessionIdToken(v_stack_m170, v_stack_m144, v_stack_m158, a4);
    result = SeSetSessionIdToken(*(unsigned __int64 *)(v_stack_m158 + 56), (unsigned int)(v_stack_m144), v_stack_m158, a4);
    if (!sign_flag) goto loc_00AEE6E3;
    result = SepDeReferenceLogonSessionDirect(v_stack_m158, (unsigned int)(v_stack_m144), v_stack_m158, a4);
    goto loc_00AEE69D;
loc_00AEE6E3:
    *(unsigned __int64 *)(v_stack_m158 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 8);
    a1 = (*(unsigned __int64 *)(v_stack_m170 + 216)) + (8);
    result = SepReferenceLogonSession(a1, v_stack_m110, v_stack_m158, a4);
    if (!sign_flag) goto loc_00AEE756;
    result = SepDeReferenceLogonSessionDirect(v_stack_m158, v_stack_m110, v_stack_m158, a4);
    goto loc_00AEE9F9;
loc_00AEE726:
    result = SepReferenceLogonSessionSilo(*(unsigned __int64 *)(v_stack_m170 + 216) + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 168), v_stack_m158, a4);
    if (!sign_flag) goto loc_00AEE75D;
    goto loc_00AEE9F7;
loc_00AEE756:
loc_00AEE75D:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_stack_m170 + 216) + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 168), v_stack_m158, a4);
    if ((unsigned int)(result) == 0) goto loc_00AEE928;
    if (v_stack_m160 == ((unsigned __int8)(v_stack_m170))) goto loc_00AEE928;
    if ((unsigned __int8)(v_stack_m178) != 0) goto loc_00AEE928;
    result = v_stack_m170;
    v_r14 = (unsigned int)((unsigned int)(v_stack_m170));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 56) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 56) + 48);
        result = ExAcquireResourceSharedLite(a1, a2, v_stack_m158, a4);
        v_r14 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 56) + 200);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 216) + 56) + 48);
        result = ExReleaseResourceLite(a1, a2, v_stack_m158, a4);
        result = KeLeaveCriticalRegion(a1, a2, v_stack_m158, a4);
    }
    if (condition_is_above_or_equal) goto loc_00AEE92D;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_mE8, a2, v_stack_m158, a4);
    result = *(unsigned __int64 *)(v_stack_mD8 + 216);
    v_r12 = (unsigned int)((unsigned int)(v_stack_m170));
    v_r14 = v_stack_mD8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 216) + 56) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 216) + 56) + 48);
        result = ExAcquireResourceSharedLite(a1, a2, v_stack_m158, a4);
        v_r12 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 216) + 56) + 200);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 216) + 56) + 48);
        result = ExReleaseResourceLite(a1, a2, v_stack_m158, a4);
        result = KeLeaveCriticalRegion(a1, a2, v_stack_m158, a4);
        v_r14 = v_stack_mD8;
    }
    if (condition_is_above_or_equal) goto loc_00AEE919;
    result = RtlEqualSid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 152)), v_stack_m158, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AEE919;
    v_stack_m110 = v_xmm0;
    result = SeQueryTokenIntegrity(v_r14, v_stack_m110, v_stack_m158, a4);
    if (v_stack_m108 != 96) goto loc_00AEE919;
    result = RtlSubAuthorityCountSid(v_stack_m110, v_stack_m110, v_stack_m158, a4);
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_00AEE919;
    a2 = 0;
    result = RtlSubAuthoritySid(v_stack_m110, a2, v_stack_m158, a4);
    if ((*(unsigned int *)(result)) != 0x3000ULL) goto loc_00AEE919;
loc_00AEE8EE:
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m170))))) << (4);
    a1 = (a1) + (v_rip - 11415835);
    result = RtlSuffixUnicodeString(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848), 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AEE917;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m170))) + (1));
    if (((unsigned int)(v_rsi)) < 1) goto loc_00AEE8EE;
    goto loc_00AEE919;
loc_00AEE917:
loc_00AEE919:
    result = SeReleaseSubjectContext(v_stack_mE8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848), 1, a4);
    goto loc_00AEE92D;
loc_00AEE928:
loc_00AEE92D:
    v_stack_m70 = 48;
    v_stack_m68 = v_stack_m170;
    v_r13 = (unsigned __int8)(-(v_r13));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (512));
    v_stack_m58 = (unsigned int)(result);
    v_stack_m60 = v_stack_m170;
    v_stack_m50 = v_xmm0;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(v_stack_mE8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848), 1, a4);
    v_rbx = 1;
    if ((unsigned int)(result) != 0) {
        v_rbx = 1 + 1;
    }
    v_stack_m1C0 = v_stack_m118;
    v_stack_m1C8 = (unsigned __int8)(v_stack_m170);
    v_stack_m1D0 = (unsigned __int8)(v_stack_m170);
    v_stack_m1D8 = (unsigned int)(v_rbx);
    a3 = 0;
    result = SepDuplicateToken(*(unsigned __int64 *)(v_stack_m158 + 56), v_stack_m70, a3, (unsigned int)(v_stack_m140));
    result = SepDeReferenceLogonSessionDirect(v_stack_m158, v_stack_m70, a3, (unsigned int)(v_stack_m140));
    if (sign_flag) goto loc_00AEE9F9;
    v_stack_m1C8 = v_stack_m138;
    v_stack_m1D0 = v_stack_m170;
    v_stack_m1D8 = (unsigned int)(v_stack_m170);
    a4 = 0;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_m118, a2, (unsigned int)(0xF01FFULL), a4);
    if (!sign_flag) goto loc_00AEEA12;
loc_00AEE9F7:
loc_00AEE9F9:
loc_00AEEA01:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), (unsigned int)(0xF01FFULL), a4);
    goto loc_00AF0505;
loc_00AEEA12:
    *(unsigned __int64 *)(a3) = v_stack_m138;
    goto loc_00AEDEE8;
loc_00AEEA65:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848)))) - (20));
    if (condition_is_equal) goto loc_00AEEDBA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEED12;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEEAEC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEEA8D;
    if (((unsigned int)(a1)) != 1) goto loc_00AED7C4;
loc_00AEEA8D:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(v_r12) = 4;
    if (v_stack_p20 >= 4) goto loc_00AF03B3;
    goto loc_00AED7D3;
loc_00AEEAEC:
    v_stack_m158 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m130 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m138 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m110 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m118 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m120 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m148 = (unsigned int)((unsigned int)(0xC0000023ULL));
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a4);
    v_stack_m198 = v_stack_m148;
    v_stack_m1A0 = v_stack_m120;
    v_stack_m1A8 = v_stack_m118;
    v_stack_m1B0 = v_stack_m110;
    v_stack_m1B8 = v_stack_m138;
    v_stack_m1C0 = v_stack_m130;
    v_stack_m1C8 = v_stack_m100;
    v_stack_m1D0 = v_stack_m158;
    v_stack_m1D8 = v_stack_mFC;
    result = SepGetTokenAccessInformationBufferSize(v_stack_m170, (unsigned __int8)(v_stack_m178), v_stack_m168, v_stack_m140);
    *(unsigned int *)(v_r12) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_p20))) < ((unsigned int)(result))) goto loc_00AED447;
    v_stack_m188 = v_stack_m168;
    v_stack_m190 = (unsigned __int8)(v_stack_m178);
    v_stack_m198 = (unsigned int)((unsigned int)(v_stack_m148));
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m120));
    v_stack_m1A8 = (unsigned int)((unsigned int)(v_stack_m118));
    v_stack_m1B0 = (unsigned int)((unsigned int)(v_stack_m110));
    v_stack_m1B8 = (unsigned int)((unsigned int)(v_stack_m138));
    v_stack_m1C0 = (unsigned int)((unsigned int)(v_stack_m130));
    v_stack_m1C8 = (unsigned int)((unsigned int)(v_stack_m100));
    v_stack_m1D0 = (unsigned int)((unsigned int)(v_stack_m158));
    v_stack_m1D8 = (unsigned int)((unsigned int)(v_stack_mFC));
    result = SepCopyTokenAccessInformation(v_stack_m170, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), (unsigned int)(v_stack_m140));
    goto loc_00AED4A1;
loc_00AEED12:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_m168, 8, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(v_r12) = 1;
    if (v_stack_p20 < 1) goto loc_00AEDE13;
    result = (((*(unsigned int *)(v_stack_m170 + 200)) & (0x810ULL)) != 0) ? 1 : 0;
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    goto loc_00AED4B2;
loc_00AEEDBA:
    *(unsigned int *)(v_r12) = 4;
    if (((unsigned int)(v_stack_m178)) == 4) goto loc_00AEEDD1;
    goto loc_00AF0505;
loc_00AEEDD1:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    result = SepGetTokenElevation(v_stack_m170, 1, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00AED4AF;
loc_00AEEE78:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    result = SepCopyTokenIntegrity(v_stack_m170, v_stack_m80, (unsigned __int8)(v_r13), (unsigned int)(v_stack_m140));
    *(unsigned int *)(v_r12) = (unsigned int)(*(unsigned __int8 *)(v_stack_m80 + 1) * 4 + 24);
    if (v_stack_p20 < ((unsigned int)(*(unsigned __int8 *)(v_stack_m80 + 1) * 4 + 24))) goto loc_00AED447;
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = a3 + 16;
    result = RtlCopySidAndAttributesArray(1, v_stack_m80, *(unsigned __int8 *)(v_stack_m80 + 1) * 4 + 8, 0);
    goto loc_00AED4A1;
loc_00AEEFB4:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848))) > 40) goto loc_00AEFA4B;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848))) == 40) goto loc_00AEEA8D;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848))) > 31) goto loc_00AEF4BC;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848))) == 31) goto loc_00AEF3AF;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 848)))) - (26));
    if (condition_is_equal) goto loc_00AEEA8D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEF306;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEF164;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEEA8D;
    if (((unsigned int)(a1)) != 1) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, a1 + 7, (unsigned __int8)(v_r13), 0);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), 0);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 800))))) << (4));
    a3 = (unsigned int)((a3) + (8));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 800))) == 0) goto loc_00AEF0A4;
loc_00AEF08D:
    a3 = (unsigned int)((a3 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 792)) + 1) * 4) + (8));
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 792)) + (1 + 15);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 800))))) - (1);
    if (condition_is_not_equal) goto loc_00AEF08D;
loc_00AEF0A4:
    *(unsigned int *)(a5) = (unsigned int)(a3);
    if (v_stack_p20 < ((unsigned int)(a3))) goto loc_00AEDA2C;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 800)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 800))))) << (4));
    a2 = (a2) + (8);
    a2 = (a2) + (a3);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = a2;
    result = RtlCopySidAndAttributesArray((unsigned int)(*(unsigned int *)(v_stack_m170 + 800)), *(unsigned __int64 *)(v_stack_m170 + 792), a3, a3 + 8);
    goto loc_00AEDA8D;
loc_00AEF164:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a3 + 8);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))) == 0) goto loc_00AEF206;
loc_00AEF1E7:
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m170))))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m170)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a2 * 8 + 8))) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_00AEF202;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m170))) + (1));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 124))))) goto loc_00AEF1E7;
    goto loc_00AEF206;
loc_00AEF202:
loc_00AEF206:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a2 * 8) != 0) goto loc_00AEF230;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), a2, *(unsigned __int64 *)(v_stack_m170 + 152), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a2 * 8));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), a2, *(unsigned __int64 *)(v_stack_m170 + 152), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a2 * 8));
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), *(unsigned __int64 *)(v_stack_m170 + 152), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 152) + a2 * 8));
    goto loc_00AF0505;
loc_00AEF230:
    a3 = ((unsigned int)((unsigned int)(v_stack_m170))) << (4);
    *(unsigned int *)(1 + 15) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3 + *(unsigned __int64 *)(v_stack_m170 + 152) * 1) + 1) * 4 + 32);
    if (v_stack_p20 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3 + *(unsigned __int64 *)(v_stack_m170 + 152) * 1) + 1) * 4 + 32))) goto loc_00AEDA2C;
    *(unsigned int *)(a3) = 1;
    a2 = (*(unsigned __int64 *)(v_stack_m170 + 152)) + (a3);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = a3 + 24;
    result = RtlCopySidAndAttributesArray(1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a2) + 1) * 4 + 8, a3 + 8);
    goto loc_00AEDA8D;
loc_00AEF306:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(1 + 15) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    result = SeQueryMandatoryPolicyToken(v_stack_m170, a3, (unsigned __int8)(v_r13), a3 + 8);
    v_stack_m13C = (unsigned int)(result);
    goto loc_00AEEA01;
loc_00AEF3AF:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 8 - 7, (unsigned __int8)(v_r13), a3 + 8);
    v_rsi = 8;
    if (*(unsigned __int64 *)(v_stack_m170 + 784) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m170 + 784) + 1);
        v_rsi = result * 4 + 16;
    }
    *(unsigned int *)(1 + 15) = (unsigned int)(v_rsi);
    if (v_stack_p20 < ((unsigned int)(v_rsi))) goto loc_00AED89C;
    a2 = a3 + 8;
    if (*(unsigned __int64 *)(v_stack_m170 + 784) == 0) { a2 = *(unsigned __int64 *)(v_stack_m170 + 784); }
    *(unsigned __int64 *)(a3) = a2;
    if (a2 != 0) {
        a1 = v_rsi - 8;
        a3 = *(unsigned __int64 *)(v_stack_m170 + 784);
        result = RtlCopySid(a1, a2, a3, a3 + 8);
    }
    goto loc_00AED8D8;
loc_00AEF4BC:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m170))) - (32));
    if (condition_is_equal) goto loc_00AEF973;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEF7B9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEF7B9;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00AEF62E;
    if (((unsigned int)(a1)) != 2) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), a1 + 6, (unsigned __int8)(v_r13), a3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a3 + 8);
    if (*(unsigned __int64 *)(v_stack_m170 + 776) != 0) goto loc_00AEF562;
    goto loc_00AEF588;
loc_00AEF562:
    v_stack_m1D0 = v_stack_m15C;
    v_stack_m1D8 = (unsigned int)(v_stack_m170);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = AuthzBasepQuerySecurityAttributesToken(*(unsigned __int64 *)(v_stack_m170 + 776), a2, a3, a4);
loc_00AEF588:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_m15C));
    if (((unsigned int)((unsigned int)(v_stack_p20))) < ((unsigned int)((unsigned int)(v_stack_m15C)))) goto loc_00AEDA2C;
    v_stack_m1D0 = v_stack_m15C;
    v_stack_m1D8 = (unsigned int)((unsigned int)(v_stack_p20));
    a3 = 0;
    a2 = 0;
    result = AuthzBasepQuerySecurityAttributesToken(*(unsigned __int64 *)(v_stack_m170 + 776), a2, a3, 0);
    v_stack_m13C = (unsigned int)(result);
    goto loc_00AEF905;
loc_00AEF62E:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), 0);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned __int8)(8 - 7), (unsigned __int8)(v_r13), 0);
    if (*(unsigned __int64 *)(v_stack_m170 + 1096) == 0) goto loc_00AEF6B6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 1096)))) == 0) goto loc_00AEF6B6;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 1096)))))) << (4));
    a3 = (unsigned int)((a3) + (8));
    goto loc_00AEF6BF;
loc_00AEF6B6:
loc_00AEF6BF:
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_m170))) == 0) goto loc_00AEF6E7;
loc_00AEF6D1:
    a3 = (unsigned int)((24 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1096) + 8)) + 1) * 4) + (8));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1096) + 8)) + (16);
    a4 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m170))))) - (8 - 7);
    if (condition_is_not_equal) goto loc_00AEF6D1;
loc_00AEF6E7:
    *(unsigned int *)(a5) = (unsigned int)(a3);
    if (v_stack_p20 < ((unsigned int)(a3))) goto loc_00AED89C;
    result = 0;
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = 0;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)((unsigned int)(v_stack_m170)));
    v_r10 = (unsigned int)(*(unsigned int *)(v_stack_m170 + 124));
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_m170))) != 0) {
        v_r10 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m170)));
        v_r10 = (unsigned int)((v_r10) << (4));
        v_r10 = (unsigned int)((v_r10) - (16));
        v_r10 = (v_r10) + (24);
        v_r10 = (v_r10) + (a3);
        a4 = a3 + 8;
        a2 = *(unsigned __int64 *)(v_stack_m170 + 1096);
        result = v_stack_m150;
        v_stack_m1C8 = result;
        result = v_stack_m150;
        v_stack_m1D0 = result;
        v_stack_m1D8 = v_r10;
        a2 = *(unsigned __int64 *)(a2 + 8);
        a1 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m170)));
        result = RtlCopySidAndAttributesArray(a1, a2, a3, a4);
    }
    goto loc_00AED8D8;
loc_00AEF7B9:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(8 - 7, 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a4);
    if (*(unsigned __int64 *)(v_stack_m170 + 1096) == 0) goto loc_00AEF876;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1096) + 576) != 0) goto loc_00AEF83D;
    if (((unsigned int)(v_stack_m170)) == 33) goto loc_00AEF876;
loc_00AEF83D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1096) + 584) != 0) goto loc_00AEF84F;
    if (((unsigned int)(v_stack_m170)) == 34) goto loc_00AEF876;
loc_00AEF84F:
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1096) + 584);
    if (((unsigned int)(v_stack_m170)) == 33) { v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1096) + 576); }
    a3 = 0;
    a2 = 0;
    result = AuthzBasepQueryClaimAttributesToken(v_rbx, a2, a3, v_stack_m15C);
    goto loc_00AEF8CB;
loc_00AEF876:
    v_stack_mA8 = v_stack_mB0;
    v_stack_mB0 = v_stack_mB0;
    v_stack_mA0 = (unsigned int)(v_stack_m170);
    v_stack_m90 = v_stack_m98;
    v_stack_m98 = v_stack_m98;
loc_00AEF8CB:
    *(unsigned int *)(a5) = 16;
    if (((unsigned int)((unsigned int)(v_stack_p20))) < 16) goto loc_00AEDA2C;
    result = AuthzBasepQueryClaimAttributesToken(v_stack_mB8, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_stack_m15C);
    v_stack_m13C = (unsigned int)(result);
loc_00AEF905:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_stack_m15C);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_stack_m15C);
    goto loc_00AEEA01;
loc_00AEF973:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), v_stack_m15C);
    if (sign_flag) goto loc_00AF0505;
    *(unsigned int *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), v_stack_m15C);
    v_rdi = v_stack_m170;
    if (*(unsigned __int64 *)(v_stack_m170 + 1080) != 0) {
        v_rdi = *(unsigned int *)(*(unsigned __int64 *)(v_stack_m170 + 1080) + 40);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), v_stack_m15C);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), v_stack_m15C);
    *(unsigned int *)(a3) = (unsigned int)(v_rdi);
    goto loc_00AEDA9B;
loc_00AEFA4B:
    if (((unsigned int)(v_stack_m170)) > 48) goto loc_00AEFDC5;
    if (((unsigned int)(v_stack_m170)) == 48) goto loc_00AEEA8D;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m170))) - (41));
    if (condition_is_equal) goto loc_00AEFC99;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEEA8D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEFBBE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEFA8C;
    if (((unsigned int)(a1)) == 3) goto loc_00AEEA8D;
    goto loc_00AED7C4;
loc_00AEFA8C:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), v_stack_m15C);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), v_stack_m15C);
    result = *(unsigned __int64 *)(v_stack_m170 + 1152);
    v_r12 = 1 + 15;
    if (*(unsigned __int64 *)(v_stack_m170 + 1152) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 1152) + 42);
        v_r12 = (unsigned int)((1 + 15) + ((unsigned int)(result)));
    }
    *(unsigned int *)(a5) = (unsigned int)(v_r12);
    if (v_stack_p20 < ((unsigned int)(v_r12))) goto loc_00AED89C;
    if ((*(unsigned __int64 *)(v_stack_m170 + 1152)) == v_rdi) goto loc_00AEFB4F;
    *(unsigned __int8 *)(a3 + 8) = 1;
    *(unsigned __int64 *)(a3) = a3 + 16;
    result = memcpy(a3 + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1152) + 48), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 1152) + 42), v_stack_m15C);
    goto loc_00AEFB56;
loc_00AEFB4F:
    *(unsigned __int8 *)(a3 + 8) = (unsigned __int8)(v_rdi);
    *(unsigned __int64 *)(a3) = v_rdi;
loc_00AEFB56:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1152) + 48), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m170 + 1152) + 42), v_stack_m15C);
    v_rdi = 0;
    goto loc_00AF03A6;
loc_00AEFBBE:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (unsigned __int8)(v_r13), v_stack_m15C);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), v_stack_m15C);
    v_stack_m1C0 = v_r12;
    v_stack_m1C8 = (unsigned int)((unsigned int)(v_stack_p20));
    v_stack_m1D0 = 0;
    v_stack_m1D8 = 1;
    a4 = 0;
    a3 = 0;
    result = SepInternalQuerySecurityAttributesTokenEx(v_stack_m170, (unsigned int)(v_stack_p20), a3, a4);
    v_stack_m13C = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned int)(v_stack_p20), a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned int)(v_stack_p20), a3, a4);
    goto loc_00AEEA01;
loc_00AEFC99:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 8 - 7, (unsigned __int8)(v_r13), a4);
    if (v_stack_m178 == ((unsigned __int8)(v_stack_m170))) {
        a1 = *(unsigned __int64 *)(v_stack_m170 + 1104);
    }
    v_rsi = 8;
    if (a1 != 0) {
        result = *(unsigned __int8 *)(a1 + 1);
        v_rsi = result * 4 + 16;
    }
    *(unsigned int *)(v_r12) = (unsigned int)(v_rsi);
    if (v_stack_p20 < ((unsigned int)(v_rsi))) goto loc_00AED89C;
    a2 = a3 + 8;
    if (a1 == 0) { a2 = a1; }
    *(unsigned __int64 *)(a3) = a2;
    if (a2 == 0) goto loc_00AEFD68;
    if (v_stack_m178 == ((unsigned __int8)(v_stack_m170))) {
        a3 = *(unsigned __int64 *)(v_stack_m170 + 1104);
    }
    result = RtlCopySid(v_rsi - 8, a2, a3, a4);
loc_00AEFD68:
    goto loc_00AED8D8;
loc_00AEFDC5:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m170))) - (53));
    if (condition_is_equal) goto loc_00AEEA8D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF025B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF0122;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AEFF80;
    if (((unsigned int)(a1)) != 2) goto loc_00AED7C4;
    v_stack_mF8 = v_xmm0;
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((unsigned int)((unsigned int)(result)), 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 1, (unsigned __int8)(v_r13), a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m170 + 1168)))) & (2)) != 0) goto loc_00AEFE87;
    goto loc_00AEF905;
loc_00AEFE87:
    result = SepGetAgentIdClaimValue(v_stack_m170, v_stack_mF8, (unsigned __int8)(v_r13), a4);
    v_stack_m13C = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000225ULL)))) {
        a2 = v_rip + 89922;
        a1 = v_stack_mF8;
        result = RtlInitUnicodeString(a1, a2, (unsigned __int8)(v_r13), a4);
        result = (unsigned int)(v_stack_m170);
        v_stack_m13C = (unsigned int)(result);
    }
    if (!sign_flag) goto loc_00AEFECF;
    goto loc_00AEF905;
loc_00AEFECF:
    v_stack_m15C = (unsigned int)(v_stack_mF8 + 2);
    if ((unsigned __int8)(v_r13) == 0) goto loc_00AEFEF4;
    result = RtlWriteULongToUser(v_r12, (unsigned int)((unsigned int)(v_stack_mF8 + 2)), (unsigned __int8)(v_r13), a4);
    goto loc_00AEFEF8;
loc_00AEFEF4:
    *(unsigned int *)(v_r12) = (unsigned int)(v_stack_mF8 + 2);
loc_00AEFEF8:
    if (v_stack_p20 < ((unsigned int)(v_stack_mF8 + 2))) goto loc_00AEDA2C;
    result = memcpy(a3, v_stack_mF0, v_stack_mF8, a4);
    v_rbx = (v_stack_mF8) >> (1);
    *(unsigned __int16 *)(a3 + v_rbx * 2) = (unsigned __int16)(v_stack_m170);
    goto loc_00AEDA8D;
loc_00AEFF80:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a3, v_stack_mF0, v_stack_mF8, a4);
    if ((unsigned int)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_rbx, 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned __int8)(8 - 7), (unsigned __int8)(v_r13), a4);
    if (*(unsigned __int64 *)(v_stack_m170 + 1176) == 0) goto loc_00AF0398;
    if ((*(unsigned int *)(v_stack_m170 + 1184)) < 3) goto loc_00AF0037;
    result = SepIsAppSuiteSid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 32), (unsigned __int8)(8 - 7), (unsigned __int8)(v_r13), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0037;
    goto loc_00AF003F;
loc_00AF0037:
loc_00AF003F:
    *(unsigned int *)(v_r12) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 32) + 1) * 4 + 16);
    if (v_stack_p20 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 32) + 1) * 4 + 16))) goto loc_00AED89C;
    if ((unsigned __int8)(v_stack_m160) != 0) goto loc_00AF00A6;
    *(unsigned __int64 *)(a3) = v_stack_m170;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned __int8)(8 - 7), v_stack_m160, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), (unsigned __int8)(8 - 7), v_stack_m160, a4);
    result = ObfDereferenceObjectWithTag(v_stack_m170, (unsigned int)(0x74726853ULL), v_stack_m160, a4);
    result = 0;
    goto loc_00AF0505;
loc_00AF00A6:
    *(unsigned __int64 *)(a3) = a3 + 8;
    if (a3 + 8 != 0) {
        a3 = *(unsigned __int64 *)(v_stack_m170 + 1176);
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 32) + 1) * 4 + 16 - 8;
        a3 = *(unsigned __int64 *)(a3 + 32);
        result = RtlCopySid(a1, a3 + 8, a3, a4);
    }
    goto loc_00AED8D8;
loc_00AF0122:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a3 + 8, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(8 - 7, 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 8 - 7, (unsigned __int8)(v_r13), a4);
    if (*(unsigned __int64 *)(v_stack_m170 + 1176) == 0) goto loc_00AF0398;
    if ((*(unsigned int *)(v_stack_m170 + 1184)) < 2) goto loc_00AF0398;
    v_rsi = 8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 16) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 16) + 1);
        v_rsi = result * 4 + 16;
    }
    *(unsigned int *)(v_r12) = (unsigned int)(v_rsi);
    if (v_stack_p20 < ((unsigned int)(v_rsi))) goto loc_00AED89C;
    a2 = a3 + 8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 16) == 0) { a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176) + 16); }
    *(unsigned __int64 *)(a3) = a2;
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(v_stack_m170 + 1176);
        a1 = v_rsi - 8;
        a3 = *(unsigned __int64 *)(a3 + 16);
        result = RtlCopySid(a1, a2, a3, a4);
    }
    goto loc_00AF0335;
loc_00AF025B:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(8 - 7, 8, (unsigned __int8)(v_r13), a4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m170 + 48), 8 - 7, (unsigned __int8)(v_r13), a4);
    if (*(unsigned __int64 *)(v_stack_m170 + 1176) == 0) goto loc_00AF0398;
    if ((*(unsigned int *)(v_stack_m170 + 1184)) == ((unsigned int)(v_stack_m170))) goto loc_00AF0398;
    v_rsi = 8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176)) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176)) + 1);
        v_rsi = result * 4 + 16;
    }
    *(unsigned int *)(v_r12) = (unsigned int)(v_rsi);
    if (v_stack_p20 < ((unsigned int)(v_rsi))) goto loc_00AED89C;
    a2 = a3 + 8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176)) == 0) { a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 1176)); }
    *(unsigned __int64 *)(a3) = a2;
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(v_stack_m170 + 1176);
        a1 = v_rsi - 8;
        a3 = *(unsigned __int64 *)(a3);
        result = RtlCopySid(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), a2, a3, a4);
    goto loc_00AF03A6;
loc_00AF0398:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m170 + 48), a2, a3, a4);
loc_00AF03A6:
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m170 + 48), a2, a3, a4);
    goto loc_00AEDFD7;
loc_00AF03B3:
    if (((unsigned int)(v_stack_m170)) != 23) goto loc_00AF03CF;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 200))) >> (9));
    goto loc_00AF04CC;
loc_00AF03CF:
    if (((unsigned int)(v_stack_m170)) != 24) goto loc_00AF03F0;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 200))) >> (10));
    goto loc_00AF04CC;
loc_00AF03F0:
    if (((unsigned int)(v_stack_m170)) != 26) goto loc_00AF040C;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 200))) >> (12));
    goto loc_00AF04CC;
loc_00AF040C:
    if (((unsigned int)(v_stack_m170)) != 40) goto loc_00AF042C;
    v_rdi = (((24) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m170 + 200))))) != 0) ? 1 : 0;
    goto loc_00AF04CF;
loc_00AF042C:
    if (((unsigned int)(v_stack_m170)) != 42) goto loc_00AF0446;
    goto loc_00AF04CC;
loc_00AF0446:
    if (((unsigned int)(v_stack_m170)) != 47) goto loc_00AF0461;
    result = SepIsSandboxedToken(v_stack_m170, (unsigned __int8)(v_r13), 24, a4);
    goto loc_00AF04B6;
loc_00AF0461:
    if (((unsigned int)(v_stack_m170)) != 48) goto loc_00AF0493;
    v_stack_m1D0 = (unsigned __int8)(*(unsigned __int16 *)(v_stack_m170 + 202));
    v_stack_m1D8 = 1;
    a4 = 0;
    a2 = 0;
    result = SepSidInTokenSidHash(v_stack_m170 + 808, a2, *(unsigned __int64 *)(v_rip + 3635022), a4);
    goto loc_00AF04B6;
loc_00AF0493:
    if (((unsigned int)(v_stack_m170)) != 53) goto loc_00AF04BB;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m170 + 808, a2, *(unsigned __int64 *)(v_rip + 3635022), a4);
    if ((unsigned int)(result) == 0) goto loc_00AED7CE;
    result = SeHasTamperProtection(v_stack_m170, a2, *(unsigned __int64 *)(v_rip + 3635022), a4);
loc_00AF04B6:
    goto loc_00AF04CF;
loc_00AF04BB:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 200))) >> (14));
loc_00AF04CC:
    v_rdi = (unsigned int)((v_rdi) & (1));
loc_00AF04CF:
    *(unsigned int *)(a3) = (unsigned int)(v_rdi);
    goto loc_00AEDA9B;
loc_00AF0505:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryInformationToken(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m140;
    uint64_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint8_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint8_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m28;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_mFC;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (464);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x170) = 0;
    *(uint32_t *)(local_rsp - 0x15C) = 0;
    *(uint32_t *)(local_rsp - 0xFC) = 0;
    *(uint32_t *)(local_rsp - 0x100) = 0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    *(uint32_t *)(local_rsp - 0x140) = 0;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x150) = 0;
    *(uint32_t *)(local_rsp - 0x144) = 0;
    *(uint8_t *)(local_rsp - 0x128) = 0;
    *(uint64_t *)(local_rsp - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xB8) = v_xmm1;
    *(uint64_t *)(local_rsp - 0xA8) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x98) = v_xmm1;
    v_stack_m160 = 0;
    *(uint8_t *)(local_rsp - 0x178) = 0;
    *(uint64_t *)(local_rsp - 0x168) = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AECEBB;
    result = ProbeForWrite(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), local_rdi + 4, Arg4);
    if (Arg5 < Arg3) { Arg3 = Arg5; }
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    goto loc_00AECEC3;
loc_00AECEBB:
loc_00AECEC3:
    if (((uint32_t)((uint32_t)(Arg2))) > 25) goto loc_00AEEFB4;
    if (((uint32_t)((uint32_t)(Arg2))) == 25) goto loc_00AEEE78;
    if (((uint32_t)((uint32_t)(Arg2))) > 12) goto loc_00AEDF2B;
    if (((uint32_t)((uint32_t)(Arg2))) == 12) goto loc_00AEDE6B;
    if (((uint32_t)((uint32_t)(Arg2))) > 6) goto loc_00AED946;
    if (((uint32_t)((uint32_t)(Arg2))) == 6) goto loc_00AED7FB;
    if (((uint32_t)((uint32_t)(Arg2))) == -2) goto loc_00AED51B;
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_00AED3BB;
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_00AED24F;
    if (((uint32_t)((uint32_t)(Arg2))) == 3) goto loc_00AED147;
    if (((uint32_t)((uint32_t)(Arg2))) == 4) goto loc_00AED02F;
    if (((uint32_t)((uint32_t)(Arg2))) != 5) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 1 + 7, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    *(uint32_t *)(arg5) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m170 + 0xA8) + 0x1) * 4 + 16);
    if (v_stack_p20 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m170 + 0xA8) + 0x1) * 4 + 16))) goto loc_00AED447;
    *(void **)(arg3) = Arg3 + 8;
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m170 + 0xA8) + 0x1) * 4 + 16) + (-8));
    result = RtlCopySid(Arg1, Arg3 + 8, *(uint64_t *)(v_stack_m170 + 0xA8), Arg4);
    goto loc_00AED4A1;
loc_00AED02F:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x90))) + ((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x90)));
    *(uint32_t *)(arg5) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg1 * 8) + 0x1) * 4 + 16);
    if (v_stack_p20 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg1 * 8) + 0x1) * 4 + 16))) goto loc_00AED447;
    *(void **)(arg3) = Arg3 + 8;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x90))) + ((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x90)));
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg1 * 8) + 0x1) * 4 + 16) + (-8));
    result = RtlCopySid(Arg1, Arg3 + 8, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + result * 8), Arg4);
    goto loc_00AED4A1;
loc_00AED147:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = SepTokenPrivilegeCount(v_stack_m170, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (((uint32_t)(result)) <= 1) goto loc_00AED1C8;
    goto loc_00AED1CE;
loc_00AED1C8:
loc_00AED1CE:
    *(uint32_t *)(arg5) = 16;
    if (v_stack_p20 < 16) goto loc_00AED447;
    result = SepConvertTokenPrivileges(v_stack_m170, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    goto loc_00AED4A1;
loc_00AED24F:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))))) << (4));
    Arg3 = (uint32_t)((Arg3) + (-8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C)))) <= 1) goto loc_00AED2F4;
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0x98)) + (16);
loc_00AED2DD:
    Arg3 = (uint32_t)((Arg3 + *(uint8_t *)(*(uint64_t *)(Arg2) + 0x1) * 4) + (8));
    Arg2 = (Arg2) + (16);
    Arg4 = ((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C)) - 1) - (1);
    if (condition_is_not_equal) goto loc_00AED2DD;
loc_00AED2F4:
    *(uint32_t *)(arg5) = (uint32_t)(Arg3);
    if (v_stack_p20 < ((uint32_t)(Arg3))) goto loc_00AED447;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))) - (1));
    *(uint32_t *)(arg3) = (uint32_t)(result);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))))) << (4));
    local_r10 = (uint32_t)((local_r10) - (32));
    local_r10 = (local_r10) + (24);
    local_r10 = (local_r10) + (Arg3);
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0x98)) + (16);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))) - 1);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = local_r10;
    result = RtlCopySidAndAttributesArray(Arg1, Arg2, Arg3, Arg3 + 8);
    goto loc_00AED4A1;
loc_00AED3BB:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_p8, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3 + 8);
    *(uint32_t *)(16) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24);
    if (v_stack_p20 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24))) goto loc_00AED46C;
loc_00AED447:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3 + 8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), 1, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3 + 8);
loc_00AED458:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3 + 8);
loc_00AED462:
    goto loc_00AF0505;
loc_00AED46C:
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = Arg3 + 16;
    result = RtlCopySidAndAttributesArray(1, *(uint64_t *)(v_stack_m170 + 0x98), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3);
loc_00AED4A1:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(v_stack_m170 + 0x98), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(v_stack_m170 + 0x98), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3);
loc_00AED4AF:
loc_00AED4B2:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3);
    result = 0;
    goto loc_00AF0505;
loc_00AED51B:
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(v_stack_m170, (uint32_t)(0x74726853ULL), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3);
    if ((uint32_t)(result) == 0) goto loc_00AED7C4;
    v_stack_m138 = v_stack_m170;
    v_stack_m130 = v_stack_m170;
    v_stack_m158 = v_stack_m170;
    v_stack_mE4 = (uint32_t)(v_stack_m170);
    v_stack_mCC = (uint32_t)(v_stack_m170);
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4EC520), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 24, Arg3);
    if ((uint8_t)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 8;
    if (v_stack_p20 != 8) goto loc_00AEE54A;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(1, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3);
    if ((uint32_t)(result) == 0) goto loc_00AED7CE;
    v_stack_m148 = (uint32_t)(v_stack_m170);
    result = RtlQueryElevationFlags(v_stack_m148, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3);
    result = (uint8_t)(((uint32_t)(v_stack_m148)) & (24));
    if (((uint8_t)(result)) != 16) goto loc_00AED7B2;
    result = SepGetTokenElevationType(v_stack_m170, v_stack_m170, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3);
    if (((uint32_t)(result)) != 2) goto loc_00AED7B2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x1C))) | (*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x18)));
    if (condition_is_equal) goto loc_00AED7B2;
    result = SepReferenceLogonSessionSilo(*(uint64_t *)(v_stack_m170 + 0xD8) + 24, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0xA8), v_stack_m138, Arg3);
    if (sign_flag) goto loc_00AEE9F9;
    v_stack_mE8 = 48;
    v_stack_mE0 = v_stack_m170;
    local_r13 = (uint8_t)(-(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (512));
    v_stack_mD0 = (uint32_t)(result);
    v_stack_mD8 = v_stack_m170;
    v_stack_mC8 = v_xmm0;
    result = SeQuerySessionIdToken(v_stack_m170, v_stack_m144, v_stack_m138, Arg3);
    result = SeSetSessionIdToken(*(uint64_t *)(v_stack_m138 + 0x38), (uint32_t)(v_stack_m144), v_stack_m138, Arg3);
    if (!sign_flag) goto loc_00AED6B7;
    result = SepDeReferenceLogonSessionDirect(v_stack_m138, (uint32_t)(v_stack_m144), v_stack_m138, Arg3);
    goto loc_00AEE9F9;
loc_00AED6B7:
    v_stack_m1C0 = v_stack_m158;
    v_stack_m1C8 = (uint8_t)(v_stack_m170);
    v_stack_m1D0 = (uint8_t)(v_stack_m170);
    v_stack_m1D8 = 1;
    Arg3 = 0;
    result = SepDuplicateToken(*(uint64_t *)(v_stack_m138 + 0x38), v_stack_mE8, Arg3, 1);
    result = SepDeReferenceLogonSessionDirect(v_stack_m138, v_stack_mE8, Arg3, 1);
    if (sign_flag) goto loc_00AEE9F9;
    Arg1 = (*(uint64_t *)(v_stack_m158 + 0xD8)) + (16);
    result = SepReferenceLogonSession(Arg1, v_stack_m138, Arg3, 1);
    if (sign_flag) goto loc_00AED769;
    v_stack_m1C8 = v_stack_m130;
    v_stack_m1D0 = v_stack_m170;
    v_stack_m1D8 = (uint32_t)(v_stack_m170);
    Arg4 = 0;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_m158, Arg2, (uint32_t)(0xF01FFULL), Arg4);
    if (!sign_flag) goto loc_00AED77B;
loc_00AED769:
    result = ObfDereferenceObject(v_stack_m158, Arg2, (uint32_t)(0xF01FFULL), Arg4);
    goto loc_00AEE9F9;
loc_00AED77B:
    *(uint64_t *)(arg3) = v_stack_m130;
    local_rdi = 0;
    goto loc_00AED7D3;
loc_00AED7B2:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), (uint32_t)(0xF01FFULL), Arg4);
loc_00AED7C4:
    goto loc_00AF0505;
loc_00AED7CE:
loc_00AED7D3:
    goto loc_00AEDFD7;
loc_00AED7FB:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    v_stack_m15C = 8;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 8 - 7, (uint8_t)(local_r13), Arg4);
    result = *(uint64_t *)(v_stack_m170 + 0xB8);
    if (*(uint64_t *)(v_stack_m170 + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0xB8) + 0x2);
        result = (uint32_t)((result) + (8));
        v_stack_m15C = (uint32_t)(result);
    }
    *(uint32_t *)(16) = (uint32_t)((uint32_t)(v_stack_m15C));
    if (((uint32_t)((uint32_t)(v_stack_p20))) >= v_stack_m15C) goto loc_00AED8B2;
loc_00AED89C:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), (uint32_t)(v_stack_p20), (uint8_t)(local_r13), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), (uint32_t)(v_stack_p20), (uint8_t)(local_r13), Arg4);
    goto loc_00AED458;
loc_00AED8B2:
    if ((*(uint64_t *)(v_stack_m170 + 0xB8)) == ((uint32_t)(0xC0000003ULL))) goto loc_00AED8D5;
    *(void **)(arg3) = Arg3 + 8;
    result = memcpy(Arg3 + 8, *(uint64_t *)(v_stack_m170 + 0xB8), *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0xB8) + 0x2), Arg4);
    goto loc_00AED8D8;
loc_00AED8D5:
    *(uint64_t *)(arg3) = (uint32_t)(0xC0000003ULL);
loc_00AED8D8:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(v_stack_m170 + 0xB8), *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0xB8) + 0x2), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(v_stack_m170 + 0xB8), *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0xB8) + 0x2), Arg4);
    goto loc_00AED4B2;
loc_00AED946:
    local_r14 = (uint32_t)((v_stack_m170) - (7));
    if (condition_is_equal) goto loc_00AEDDC0;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00AEDD1F;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00AEDC62;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00AEDAFB;
    if (((uint32_t)(local_r14)) != 1) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), local_r14 + 7, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), (uint8_t)((uint32_t)((uint32_t)(local_r14))), (uint8_t)(local_r13), Arg4);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))))) << (4));
    Arg3 = (uint32_t)((Arg3) + (8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))) == 0) goto loc_00AEDA17;
loc_00AEDA00:
    Arg3 = (uint32_t)((Arg3 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xA0)) + 0x1) * 4) + (8));
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0xA0)) + (local_r14 + 15);
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))))) - ((uint32_t)((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_00AEDA00;
loc_00AEDA17:
    *(uint32_t *)(arg5) = (uint32_t)(Arg3);
    if (v_stack_p20 >= ((uint32_t)(Arg3))) goto loc_00AEDA42;
loc_00AEDA2C:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, Arg3, Arg4);
    goto loc_00AED458;
loc_00AEDA42:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))))) << (4));
    Arg2 = (Arg2) + (8);
    Arg2 = (Arg2) + (Arg3);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = Arg2;
    result = RtlCopySidAndAttributesArray((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80)), *(uint64_t *)(v_stack_m170 + 0xA0), Arg3, Arg3 + 8);
loc_00AEDA8D:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(v_stack_m170 + 0xA0), Arg3, Arg3 + 8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(v_stack_m170 + 0xA0), Arg3, Arg3 + 8);
loc_00AEDA9B:
    goto loc_00AED4B2;
loc_00AEDAFB:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(local_r14)), 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(local_r14 + 0xF) = 56;
    if (v_stack_p20 < 56) goto loc_00AEDE13;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg3 + 8);
    v_stack_m124 = (uint32_t)((uint32_t)(0xC0000003ULL));
    *(uint64_t *)(arg3) = *(uint64_t *)(v_stack_m170 + 0x10);
    *(uint64_t *)(arg3 + 0x8) = *(uint64_t *)(v_stack_m170 + 0x18);
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(v_stack_m170 + 0x28);
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC0)));
    *(uint32_t *)(arg3 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC4)));
    *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x88)));
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m170 + 0xA8) + 0x1)) << (2));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x88))) - ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_m124 = Arg2;
    result = *(uint64_t *)(v_stack_m170 + 0xB8);
    if (*(uint64_t *)(v_stack_m170 + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0xB8) + 0x2);
        Arg2 = (uint32_t)((Arg2) - ((uint32_t)(result)));
        v_stack_m124 = Arg2;
    }
    *(uint32_t *)(arg3 + 0x24) = Arg2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))) - (1));
    *(uint32_t *)(arg3 + 0x28) = (uint32_t)(result);
    result = SepTokenPrivilegeCount(v_stack_m170, Arg2, (uint8_t)(local_r13), Arg3 + 8);
    *(uint32_t *)(arg3 + 0x2C) = (uint32_t)(result);
    *(uint64_t *)(arg3 + 0x30) = *(uint64_t *)(v_stack_m170 + 0x38);
    goto loc_00AED8D8;
loc_00AEDC62:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    if ((*(uint32_t *)(v_stack_m170 + 0xC0)) == 2) goto loc_00AEDCBD;
    goto loc_00AEDFD4;
loc_00AEDCBD:
    *(uint32_t *)(local_r14 + 0xF) = 4;
    if (v_stack_p20 >= 4) goto loc_00AEDCD7;
    goto loc_00AED458;
loc_00AEDCD7:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC4)));
    goto loc_00AED4B2;
loc_00AEDD1F:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(local_r14 + 0xF) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC0)));
    goto loc_00AED4B2;
loc_00AEDDC0:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 16, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(arg5) = 16;
    if (8 >= 16) goto loc_00AEDE20;
loc_00AEDE13:
    goto loc_00AED458;
loc_00AEDE20:
    *(uint64_t *)(arg3) = v_xmm0;
    goto loc_00AED4B2;
loc_00AEDE6B:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AED458;
    result = SeQuerySessionIdToken(v_stack_m170, v_stack_m144, (uint8_t)(local_r13), Arg3 + 8);
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(v_stack_m144));
    *(uint32_t *)(16) = 4;
loc_00AEDEE8:
    goto loc_00AED4B2;
loc_00AEDF2B:
    if (((uint32_t)(v_stack_m170)) > 19) goto loc_00AEEA65;
    if (((uint32_t)(v_stack_m170)) == 19) goto loc_00AEE4CB;
    local_r14 = (uint32_t)((v_stack_m170) - (13));
    if (condition_is_equal) goto loc_00AEE25E;
    local_r14 = (uint32_t)((local_r14) - (2));
    if (condition_is_equal) goto loc_00AEE1CD;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00AEE0BD;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00AEE01E;
    if (((uint32_t)(local_r14)) != 1) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, local_r14 + 7, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    result = SepGetTokenElevationType(v_stack_m170, local_r14 + 7, v_stack_m170, Arg3 + 8);
    *(uint32_t *)(arg3) = (uint32_t)(result);
loc_00AEDFD4:
loc_00AEDFD7:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), v_stack_m170, Arg3 + 8);
    goto loc_00AF0505;
loc_00AEE01E:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 8;
    if (v_stack_p20 < 8) goto loc_00AEDE13;
    *(uint64_t *)(arg3) = *(uint64_t *)(v_stack_m170 + 0xE0);
    goto loc_00AED4B2;
loc_00AEE0BD:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4EBA39), (uint8_t)(local_r13), (uint8_t)(local_r13), Arg3 + 8);
    if ((uint8_t)(result) != 0) goto loc_00AEE0DA;
    goto loc_00AF0505;
loc_00AEE0DA:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 31;
    if (v_stack_p20 < 31) goto loc_00AEDE13;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg3 + 8);
    *(uint64_t *)(arg3) = v_xmm0;
    *(uint64_t *)(arg3 + 0x10) = v_xmm1;
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x70)));
    *(uint16_t *)(arg3 + 0x1C) = (uint16_t)(*(uint16_t *)(v_stack_m170 + 0x74));
    *(uint8_t *)(arg3 + 0x1E) = (uint8_t)(*(uint8_t *)(v_stack_m170 + 0x76));
    goto loc_00AED4A1;
loc_00AEE1CD:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AED462;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC8))) >> (6));
    result = (uint32_t)((result) & (1));
    *(uint32_t *)(arg3) = (uint32_t)(result);
    goto loc_00AED4B2;
loc_00AEE25E:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg3 + 8);
    result = SepTokenPrivilegeCount(v_stack_m170, 1, (uint8_t)(local_r13), Arg3 + 8);
    v_stack_m140 = (uint32_t)(result);
    local_r11 = (uint32_t)((result + result * 2) << (2));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))))) << (4));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))) == 0) goto loc_00AEE318;
loc_00AEE2FC:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)) + 0x1) * 4 + 15) & (0xFFFFFFF8ULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + ((uint32_t)(Arg1)));
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0x98)) + (1 + 15);
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))))) - (1);
    if (condition_is_not_equal) goto loc_00AEE2FC;
loc_00AEE318:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))))) << (4));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))) == 0) goto loc_00AEE358;
loc_00AEE339:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xA0)) + 0x1) * 4 + 15) & (0xFFFFFFF8ULL));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) + ((uint32_t)(Arg1)));
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0xA0)) + (1 + 15);
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80))))) - (1);
    if (condition_is_not_equal) goto loc_00AEE339;
loc_00AEE358:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) + (56));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r11)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg3)));
    *(uint32_t *)(arg5) = (uint32_t)(Arg1);
    if (v_stack_p20 < ((uint32_t)(Arg1))) goto loc_00AEDA2C;
    *(uint64_t *)(arg3 + 0x30) = *(uint64_t *)(v_stack_m170 + 0x18);
    *(uint32_t *)(arg3 + 0x4) = (uint32_t)(Arg3);
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C)));
    *(void **)(arg3 + 0x8) = Arg3 + 56;
    *(uint32_t *)(arg3 + 0x14) = (uint32_t)(local_r14);
    *(uint32_t *)(arg3 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x80)));
    if ((*(uint32_t *)(v_stack_m170 + 0x80)) == ((uint32_t)(v_stack_m170))) goto loc_00AEE3BC;
    local_rbx = ((uint32_t)((uint32_t)(Arg3))) + (7);
    local_rbx = (local_rbx) & (-8);
    local_rbx = (local_rbx) + (Arg3 + 56);
    *(uint64_t *)(arg3 + 0x18) = local_rbx;
    goto loc_00AEE3C8;
loc_00AEE3BC:
    *(uint64_t *)(arg3 + 0x18) = v_stack_m170;
loc_00AEE3C8:
    *(uint32_t *)(arg3 + 0x24) = (uint32_t)(local_r11);
    *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint32_t)(v_stack_m140));
    result = ((uint32_t)((uint32_t)(local_r14))) + (Arg3 + 56);
    local_r12 = ((uint32_t)((uint32_t)(Arg3))) + (result);
    *(uint64_t *)(arg3 + 0x28) = local_r12;
    result = ((uint32_t)((uint32_t)(local_r10))) + (Arg3 + 56);
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(local_r10)));
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = result;
    result = RtlCopySidAndAttributesArray((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C)), *(uint64_t *)(v_stack_m170 + 0x98), Arg3, Arg3 + 56);
    result = ((uint32_t)((uint32_t)(local_r13))) + (v_stack_m88);
    if (v_stack_m88 != 0) {
        local_r14 = (uint32_t)((local_r14) - ((uint32_t)(local_r13)));
        Arg1 = v_stack_m150;
        v_stack_m1C8 = Arg1;
        Arg1 = v_stack_m150;
        v_stack_m1D0 = Arg1;
        v_stack_m1D8 = result;
        Arg4 = v_stack_m88;
        Arg3 = (uint32_t)(local_r14);
        Arg2 = *(uint64_t *)(v_stack_m170 + 0xA0);
        Arg1 = *(uint32_t *)(v_stack_m170 + 0x80);
        result = RtlCopySidAndAttributesArray(Arg1, Arg2, Arg3, Arg4);
    }
    result = SepConvertTokenPrivilegesToLuidAndAttributes(v_stack_m170, local_r12, Arg3, Arg4);
    goto loc_00AEDA8D;
loc_00AEE4CB:
    v_stack_m158 = v_stack_m170;
    v_stack_m138 = v_stack_m170;
    v_stack_m118 = v_stack_m170;
    v_stack_m6C = (uint32_t)(v_stack_m170);
    v_stack_m54 = (uint32_t)(v_stack_m170);
    v_stack_m160 = (uint8_t)(v_stack_m170);
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_m88, 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(local_r12) = 8;
    if (v_stack_p20 == 8) goto loc_00AEE554;
loc_00AEE54A:
    goto loc_00AEE9F9;
loc_00AEE554:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(v_stack_m88, 8, (uint8_t)(local_r13), Arg4);
    local_r14 = (uint8_t)(v_stack_m170);
    if ((uint32_t)(result) != 0) {
        v_stack_m148 = (uint32_t)(v_stack_m170);
        Arg1 = v_stack_m148;
        result = RtlQueryElevationFlags(Arg1, 8, (uint8_t)(local_r13), Arg4);
        result = v_stack_m148;
        result = (uint8_t)((result) & (24));
        local_r12 = 16;
        local_r14 = (((uint8_t)(result)) == ((uint8_t)(local_r12))) ? 1 : 0;
        v_stack_m160 = (uint8_t)(local_r14);
    }
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4EB4DF), (uint8_t)(local_r13), (uint8_t)(local_r13), Arg4);
    v_stack_m178 = (uint8_t)(result);
    Arg1 = (uint8_t)(-((uint8_t)(result)));
    result = (uint32_t)((result) + (2));
    v_stack_m140 = (uint32_t)(result);
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(Arg1, (uint8_t)(local_r13), (uint8_t)(local_r13), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AEE726;
    if ((uint8_t)(local_r14) == 0) goto loc_00AEE726;
    result = SepGetTokenElevationType(v_stack_m170, (uint8_t)(local_r13), (uint8_t)(local_r13), Arg4);
    if (((uint32_t)(result)) != 3) goto loc_00AEE726;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x14))) | (*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x10)));
    if (condition_is_not_equal) goto loc_00AEE726;
    v_stack_m130 = v_stack_m170;
    result = SepLogonSystemManagedAdmin(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x8), v_stack_m130, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AEE9F7;
    v_stack_m110 = v_stack_m170;
    v_stack_m1D0 = v_stack_m170;
    v_stack_m1D8 = v_stack_m110;
    Arg4 = 0;
    result = ObReferenceObjectByHandle(v_stack_m130, 8, *(uint64_t *)(v_rip + 0x4E99FF), Arg4);
    Arg2 = 0;
    result = ObCloseHandle(v_stack_m130, Arg2, *(uint64_t *)(v_rip + 0x4E99FF), Arg4);
    if (sign_flag) goto loc_00AEE9F9;
    result = SepReferenceLogonSessionSilo(v_stack_m110 + 24, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0xA8), v_stack_m158, Arg4);
    result = ObfDereferenceObject(v_stack_m110, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0xA8), v_stack_m158, Arg4);
    if (!sign_flag) goto loc_00AEE6A5;
loc_00AEE69D:
    goto loc_00AEE9F9;
loc_00AEE6A5:
    result = SeQuerySessionIdToken(v_stack_m170, v_stack_m144, v_stack_m158, Arg4);
    result = SeSetSessionIdToken(*(uint64_t *)(v_stack_m158 + 0x38), (uint32_t)(v_stack_m144), v_stack_m158, Arg4);
    if (!sign_flag) goto loc_00AEE6E3;
    result = SepDeReferenceLogonSessionDirect(v_stack_m158, (uint32_t)(v_stack_m144), v_stack_m158, Arg4);
    goto loc_00AEE69D;
loc_00AEE6E3:
    *(uint64_t *)(v_stack_m158 + 0x10) = *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x8);
    Arg1 = (*(uint64_t *)(v_stack_m170 + 0xD8)) + (8);
    result = SepReferenceLogonSession(Arg1, v_stack_m110, v_stack_m158, Arg4);
    if (!sign_flag) goto loc_00AEE756;
    result = SepDeReferenceLogonSessionDirect(v_stack_m158, v_stack_m110, v_stack_m158, Arg4);
    goto loc_00AEE9F9;
loc_00AEE726:
    result = SepReferenceLogonSessionSilo(*(uint64_t *)(v_stack_m170 + 0xD8) + 16, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0xA8), v_stack_m158, Arg4);
    if (!sign_flag) goto loc_00AEE75D;
    goto loc_00AEE9F7;
loc_00AEE756:
loc_00AEE75D:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_stack_m170 + 0xD8) + 16, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0xA8), v_stack_m158, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AEE928;
    if (v_stack_m160 == ((uint8_t)(v_stack_m170))) goto loc_00AEE928;
    if ((uint8_t)(v_stack_m178) != 0) goto loc_00AEE928;
    result = v_stack_m170;
    local_r14 = (uint32_t)((uint32_t)(v_stack_m170));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x38) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x38) + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, v_stack_m158, Arg4);
        local_r14 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x38) + 0xC8);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0xD8) + 0x38) + 0x30);
        result = ExReleaseResourceLite(Arg1, Arg2, v_stack_m158, Arg4);
        result = KeLeaveCriticalRegion(Arg1, Arg2, v_stack_m158, Arg4);
    }
    if (condition_is_above_or_equal) goto loc_00AEE92D;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_mE8, Arg2, v_stack_m158, Arg4);
    result = *(uint64_t *)(v_stack_mD8 + 0xD8);
    local_r12 = (uint32_t)((uint32_t)(v_stack_m170));
    local_r14 = v_stack_mD8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0xD8) + 0x38) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0xD8) + 0x38) + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, v_stack_m158, Arg4);
        local_r12 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0xD8) + 0x38) + 0xC8);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0xD8) + 0x38) + 0x30);
        result = ExReleaseResourceLite(Arg1, Arg2, v_stack_m158, Arg4);
        result = KeLeaveCriticalRegion(Arg1, Arg2, v_stack_m158, Arg4);
        local_r14 = v_stack_mD8;
    }
    if (condition_is_above_or_equal) goto loc_00AEE919;
    result = RtlEqualSid(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98)), *(uint64_t *)(*(uint64_t *)(local_r14 + 0x98)), v_stack_m158, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AEE919;
    v_stack_m110 = v_xmm0;
    result = SeQueryTokenIntegrity(local_r14, v_stack_m110, v_stack_m158, Arg4);
    if (v_stack_m108 != 96) goto loc_00AEE919;
    result = RtlSubAuthorityCountSid(v_stack_m110, v_stack_m110, v_stack_m158, Arg4);
    if ((*(uint8_t *)(result)) != 1) goto loc_00AEE919;
    Arg2 = 0;
    result = RtlSubAuthoritySid(v_stack_m110, Arg2, v_stack_m158, Arg4);
    if ((*(uint32_t *)(result)) != 0x3000ULL) goto loc_00AEE919;
loc_00AEE8EE:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m170))))) << (4);
    Arg1 = (Arg1) + (v_rip - 11415835);
    result = RtlSuffixUnicodeString(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350), 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AEE917;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m170))) + (1));
    if (((uint32_t)(local_rsi)) < 1) goto loc_00AEE8EE;
    goto loc_00AEE919;
loc_00AEE917:
loc_00AEE919:
    result = SeReleaseSubjectContext(v_stack_mE8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350), 1, Arg4);
    goto loc_00AEE92D;
loc_00AEE928:
loc_00AEE92D:
    v_stack_m70 = 48;
    v_stack_m68 = v_stack_m170;
    local_r13 = (uint8_t)(-(local_r13));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (512));
    v_stack_m58 = (uint32_t)(result);
    v_stack_m60 = v_stack_m170;
    v_stack_m50 = v_xmm0;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(v_stack_mE8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350), 1, Arg4);
    local_rbx = 1;
    if ((uint32_t)(result) != 0) {
        local_rbx = 1 + 1;
    }
    v_stack_m1C0 = v_stack_m118;
    v_stack_m1C8 = (uint8_t)(v_stack_m170);
    v_stack_m1D0 = (uint8_t)(v_stack_m170);
    v_stack_m1D8 = (uint32_t)(local_rbx);
    Arg3 = 0;
    result = SepDuplicateToken(*(uint64_t *)(v_stack_m158 + 0x38), v_stack_m70, Arg3, (uint32_t)(v_stack_m140));
    result = SepDeReferenceLogonSessionDirect(v_stack_m158, v_stack_m70, Arg3, (uint32_t)(v_stack_m140));
    if (sign_flag) goto loc_00AEE9F9;
    v_stack_m1C8 = v_stack_m138;
    v_stack_m1D0 = v_stack_m170;
    v_stack_m1D8 = (uint32_t)(v_stack_m170);
    Arg4 = 0;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_m118, Arg2, (uint32_t)(0xF01FFULL), Arg4);
    if (!sign_flag) goto loc_00AEEA12;
loc_00AEE9F7:
loc_00AEE9F9:
loc_00AEEA01:
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), (uint32_t)(0xF01FFULL), Arg4);
    goto loc_00AF0505;
loc_00AEEA12:
    *(uint64_t *)(arg3) = v_stack_m138;
    goto loc_00AEDEE8;
loc_00AEEA65:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350)))) - (20));
    if (condition_is_equal) goto loc_00AEEDBA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEED12;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEEAEC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEEA8D;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AED7C4;
loc_00AEEA8D:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(local_r12) = 4;
    if (v_stack_p20 >= 4) goto loc_00AF03B3;
    goto loc_00AED7D3;
loc_00AEEAEC:
    v_stack_m158 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m130 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m138 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m110 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m118 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m120 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m148 = (uint32_t)((uint32_t)(0xC0000023ULL));
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg4);
    v_stack_m198 = v_stack_m148;
    v_stack_m1A0 = v_stack_m120;
    v_stack_m1A8 = v_stack_m118;
    v_stack_m1B0 = v_stack_m110;
    v_stack_m1B8 = v_stack_m138;
    v_stack_m1C0 = v_stack_m130;
    v_stack_m1C8 = v_stack_m100;
    v_stack_m1D0 = v_stack_m158;
    v_stack_m1D8 = v_stack_mFC;
    result = SepGetTokenAccessInformationBufferSize(v_stack_m170, (uint8_t)(v_stack_m178), v_stack_m168, v_stack_m140);
    *(uint32_t *)(local_r12) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_p20))) < ((uint32_t)(result))) goto loc_00AED447;
    v_stack_m188 = v_stack_m168;
    v_stack_m190 = (uint8_t)(v_stack_m178);
    v_stack_m198 = (uint32_t)((uint32_t)(v_stack_m148));
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m120));
    v_stack_m1A8 = (uint32_t)((uint32_t)(v_stack_m118));
    v_stack_m1B0 = (uint32_t)((uint32_t)(v_stack_m110));
    v_stack_m1B8 = (uint32_t)((uint32_t)(v_stack_m138));
    v_stack_m1C0 = (uint32_t)((uint32_t)(v_stack_m130));
    v_stack_m1C8 = (uint32_t)((uint32_t)(v_stack_m100));
    v_stack_m1D0 = (uint32_t)((uint32_t)(v_stack_m158));
    v_stack_m1D8 = (uint32_t)((uint32_t)(v_stack_mFC));
    result = SepCopyTokenAccessInformation(v_stack_m170, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), (uint32_t)(v_stack_m140));
    goto loc_00AED4A1;
loc_00AEED12:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(v_stack_m168, 8, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(local_r12) = 1;
    if (v_stack_p20 < 1) goto loc_00AEDE13;
    result = (((*(uint32_t *)(v_stack_m170 + 0xC8)) & (0x810ULL)) != 0) ? 1 : 0;
    *(uint8_t *)(arg3) = (uint8_t)(result);
    goto loc_00AED4B2;
loc_00AEEDBA:
    *(uint32_t *)(local_r12) = 4;
    if (((uint32_t)(v_stack_m178)) == 4) goto loc_00AEEDD1;
    goto loc_00AF0505;
loc_00AEEDD1:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    result = SepGetTokenElevation(v_stack_m170, 1, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00AED4AF;
loc_00AEEE78:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    result = SepCopyTokenIntegrity(v_stack_m170, v_stack_m80, (uint8_t)(local_r13), (uint32_t)(v_stack_m140));
    *(uint32_t *)(local_r12) = (uint32_t)(*(uint8_t *)(v_stack_m80 + 0x1) * 4 + 24);
    if (v_stack_p20 < ((uint32_t)(*(uint8_t *)(v_stack_m80 + 0x1) * 4 + 24))) goto loc_00AED447;
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = Arg3 + 16;
    result = RtlCopySidAndAttributesArray(1, v_stack_m80, *(uint8_t *)(v_stack_m80 + 0x1) * 4 + 8, 0);
    goto loc_00AED4A1;
loc_00AEEFB4:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350))) > 40) goto loc_00AEFA4B;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350))) == 40) goto loc_00AEEA8D;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350))) > 31) goto loc_00AEF4BC;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350))) == 31) goto loc_00AEF3AF;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x350)))) - (26));
    if (condition_is_equal) goto loc_00AEEA8D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEF306;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEF164;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEEA8D;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, Arg1 + 7, (uint8_t)(local_r13), 0);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), 0);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x320))))) << (4));
    Arg3 = (uint32_t)((Arg3) + (8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x320))) == 0) goto loc_00AEF0A4;
loc_00AEF08D:
    Arg3 = (uint32_t)((Arg3 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x318)) + 0x1) * 4) + (8));
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0x318)) + (1 + 15);
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x320))))) - (1);
    if (condition_is_not_equal) goto loc_00AEF08D;
loc_00AEF0A4:
    *(uint32_t *)(arg5) = (uint32_t)(Arg3);
    if (v_stack_p20 < ((uint32_t)(Arg3))) goto loc_00AEDA2C;
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x320)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x320))))) << (4));
    Arg2 = (Arg2) + (8);
    Arg2 = (Arg2) + (Arg3);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = Arg2;
    result = RtlCopySidAndAttributesArray((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x320)), *(uint64_t *)(v_stack_m170 + 0x318), Arg3, Arg3 + 8);
    goto loc_00AEDA8D;
loc_00AEF164:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg3 + 8);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))) == 0) goto loc_00AEF206;
loc_00AEF1E7:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m170))))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m170)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg2 * 8 + 0x8))) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_00AEF202;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m170))) + (1));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C))))) goto loc_00AEF1E7;
    goto loc_00AEF206;
loc_00AEF202:
loc_00AEF206:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg2 * 8) != 0) goto loc_00AEF230;
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, *(uint64_t *)(v_stack_m170 + 0x98), *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg2 * 8));
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, *(uint64_t *)(v_stack_m170 + 0x98), *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg2 * 8));
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), *(uint64_t *)(v_stack_m170 + 0x98), *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x98) + Arg2 * 8));
    goto loc_00AF0505;
loc_00AEF230:
    Arg3 = ((uint32_t)((uint32_t)(v_stack_m170))) << (4);
    *(uint32_t *)(1 + 0xF) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(arg3 + *(uint64_t *)(v_stack_m170 + 0x98) * 1) + 0x1) * 4 + 32);
    if (v_stack_p20 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg3 + *(uint64_t *)(v_stack_m170 + 0x98) * 1) + 0x1) * 4 + 32))) goto loc_00AEDA2C;
    *(uint32_t *)(arg3) = 1;
    Arg2 = (*(uint64_t *)(v_stack_m170 + 0x98)) + (Arg3);
    v_stack_m1C8 = v_stack_m150;
    v_stack_m1D0 = v_stack_m150;
    v_stack_m1D8 = Arg3 + 24;
    result = RtlCopySidAndAttributesArray(1, Arg2, *(uint8_t *)(*(uint64_t *)(Arg2) + 0x1) * 4 + 8, Arg3 + 8);
    goto loc_00AEDA8D;
loc_00AEF306:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(1 + 0xF) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    result = SeQueryMandatoryPolicyToken(v_stack_m170, Arg3, (uint8_t)(local_r13), Arg3 + 8);
    v_stack_m13C = (uint32_t)(result);
    goto loc_00AEEA01;
loc_00AEF3AF:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 8 - 7, (uint8_t)(local_r13), Arg3 + 8);
    local_rsi = 8;
    if (*(uint64_t *)(v_stack_m170 + 0x310) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(v_stack_m170 + 0x310) + 0x1);
        local_rsi = result * 4 + 16;
    }
    *(uint32_t *)(1 + 0xF) = (uint32_t)(local_rsi);
    if (v_stack_p20 < ((uint32_t)(local_rsi))) goto loc_00AED89C;
    Arg2 = Arg3 + 8;
    if (*(uint64_t *)(v_stack_m170 + 0x310) == 0) { Arg2 = *(uint64_t *)(v_stack_m170 + 0x310); }
    *(uint64_t *)(arg3) = Arg2;
    if (Arg2 != 0) {
        Arg1 = local_rsi - 8;
        Arg3 = *(uint64_t *)(v_stack_m170 + 0x310);
        result = RtlCopySid(Arg1, Arg2, Arg3, Arg3 + 8);
    }
    goto loc_00AED8D8;
loc_00AEF4BC:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m170))) - (32));
    if (condition_is_equal) goto loc_00AEF973;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEF7B9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEF7B9;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00AEF62E;
    if (((uint32_t)(Arg1)) != 2) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), Arg1 + 6, (uint8_t)(local_r13), Arg3 + 8);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg3 + 8);
    if (*(uint64_t *)(v_stack_m170 + 0x308) != 0) goto loc_00AEF562;
    goto loc_00AEF588;
loc_00AEF562:
    v_stack_m1D0 = v_stack_m15C;
    v_stack_m1D8 = (uint32_t)(v_stack_m170);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = AuthzBasepQuerySecurityAttributesToken(*(uint64_t *)(v_stack_m170 + 0x308), Arg2, Arg3, Arg4);
loc_00AEF588:
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(v_stack_m15C));
    if (((uint32_t)((uint32_t)(v_stack_p20))) < ((uint32_t)((uint32_t)(v_stack_m15C)))) goto loc_00AEDA2C;
    v_stack_m1D0 = v_stack_m15C;
    v_stack_m1D8 = (uint32_t)((uint32_t)(v_stack_p20));
    Arg3 = 0;
    Arg2 = 0;
    result = AuthzBasepQuerySecurityAttributesToken(*(uint64_t *)(v_stack_m170 + 0x308), Arg2, Arg3, 0);
    v_stack_m13C = (uint32_t)(result);
    goto loc_00AEF905;
loc_00AEF62E:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), 0);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), (uint8_t)(8 - 7), (uint8_t)(local_r13), 0);
    if (*(uint64_t *)(v_stack_m170 + 0x448) == 0) goto loc_00AEF6B6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0x448)))) == 0) goto loc_00AEF6B6;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0x448)))))) << (4));
    Arg3 = (uint32_t)((Arg3) + (8));
    goto loc_00AEF6BF;
loc_00AEF6B6:
loc_00AEF6BF:
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_m170))) == 0) goto loc_00AEF6E7;
loc_00AEF6D1:
    Arg3 = (uint32_t)((24 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x448) + 0x8)) + 0x1) * 4) + (8));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x448) + 0x8)) + (16);
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m170))))) - (8 - 7);
    if (condition_is_not_equal) goto loc_00AEF6D1;
loc_00AEF6E7:
    *(uint32_t *)(arg5) = (uint32_t)(Arg3);
    if (v_stack_p20 < ((uint32_t)(Arg3))) goto loc_00AED89C;
    result = 0;
    *(uint64_t *)(arg3) = v_xmm0;
    *(uint64_t *)(arg3 + 0x10) = 0;
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)((uint32_t)(v_stack_m170)));
    local_r10 = (uint32_t)(*(uint32_t *)(v_stack_m170 + 0x7C));
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_m170))) != 0) {
        local_r10 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m170)));
        local_r10 = (uint32_t)((local_r10) << (4));
        local_r10 = (uint32_t)((local_r10) - (16));
        local_r10 = (local_r10) + (24);
        local_r10 = (local_r10) + (Arg3);
        Arg4 = Arg3 + 8;
        Arg2 = *(uint64_t *)(v_stack_m170 + 0x448);
        result = v_stack_m150;
        v_stack_m1C8 = result;
        result = v_stack_m150;
        v_stack_m1D0 = result;
        v_stack_m1D8 = local_r10;
        Arg2 = *(uint64_t *)(Arg2 + 0x8);
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m170)));
        result = RtlCopySidAndAttributesArray(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00AED8D8;
loc_00AEF7B9:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(8 - 7, 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg4);
    if (*(uint64_t *)(v_stack_m170 + 0x448) == 0) goto loc_00AEF876;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x448) + 0x240) != 0) goto loc_00AEF83D;
    if (((uint32_t)(v_stack_m170)) == 33) goto loc_00AEF876;
loc_00AEF83D:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x448) + 0x248) != 0) goto loc_00AEF84F;
    if (((uint32_t)(v_stack_m170)) == 34) goto loc_00AEF876;
loc_00AEF84F:
    local_rbx = *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x448) + 0x248);
    if (((uint32_t)(v_stack_m170)) == 33) { local_rbx = *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x448) + 0x240); }
    Arg3 = 0;
    Arg2 = 0;
    result = AuthzBasepQueryClaimAttributesToken(local_rbx, Arg2, Arg3, v_stack_m15C);
    goto loc_00AEF8CB;
loc_00AEF876:
    v_stack_mA8 = v_stack_mB0;
    v_stack_mB0 = v_stack_mB0;
    v_stack_mA0 = (uint32_t)(v_stack_m170);
    v_stack_m90 = v_stack_m98;
    v_stack_m98 = v_stack_m98;
loc_00AEF8CB:
    *(uint32_t *)(arg5) = 16;
    if (((uint32_t)((uint32_t)(v_stack_p20))) < 16) goto loc_00AEDA2C;
    result = AuthzBasepQueryClaimAttributesToken(v_stack_mB8, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), v_stack_m15C);
    v_stack_m13C = (uint32_t)(result);
loc_00AEF905:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), v_stack_m15C);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), v_stack_m15C);
    goto loc_00AEEA01;
loc_00AEF973:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), v_stack_m15C);
    if (sign_flag) goto loc_00AF0505;
    *(uint32_t *)(16) = 4;
    if (v_stack_p20 < 4) goto loc_00AEDE13;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), v_stack_m15C);
    local_rdi = v_stack_m170;
    if (*(uint64_t *)(v_stack_m170 + 0x438) != 0) {
        local_rdi = *(uint32_t *)(*(uint64_t *)(v_stack_m170 + 0x438) + 0x28);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), v_stack_m15C);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), v_stack_m15C);
    *(uint32_t *)(arg3) = (uint32_t)(local_rdi);
    goto loc_00AEDA9B;
loc_00AEFA4B:
    if (((uint32_t)(v_stack_m170)) > 48) goto loc_00AEFDC5;
    if (((uint32_t)(v_stack_m170)) == 48) goto loc_00AEEA8D;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m170))) - (41));
    if (condition_is_equal) goto loc_00AEFC99;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEEA8D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEFBBE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEFA8C;
    if (((uint32_t)(Arg1)) == 3) goto loc_00AEEA8D;
    goto loc_00AED7C4;
loc_00AEFA8C:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), v_stack_m15C);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), v_stack_m15C);
    result = *(uint64_t *)(v_stack_m170 + 0x480);
    local_r12 = 1 + 15;
    if (*(uint64_t *)(v_stack_m170 + 0x480) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0x480) + 0x2A);
        local_r12 = (uint32_t)((1 + 15) + ((uint32_t)(result)));
    }
    *(uint32_t *)(arg5) = (uint32_t)(local_r12);
    if (v_stack_p20 < ((uint32_t)(local_r12))) goto loc_00AED89C;
    if ((*(uint64_t *)(v_stack_m170 + 0x480)) == local_rdi) goto loc_00AEFB4F;
    *(uint8_t *)(arg3 + 0x8) = 1;
    *(void **)(arg3) = Arg3 + 16;
    result = memcpy(Arg3 + 16, *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x480) + 0x30), *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0x480) + 0x2A), v_stack_m15C);
    goto loc_00AEFB56;
loc_00AEFB4F:
    *(uint8_t *)(arg3 + 0x8) = (uint8_t)(local_rdi);
    *(uint64_t *)(arg3) = local_rdi;
loc_00AEFB56:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x480) + 0x30), *(uint16_t *)(*(uint64_t *)(v_stack_m170 + 0x480) + 0x2A), v_stack_m15C);
    local_rdi = 0;
    goto loc_00AF03A6;
loc_00AEFBBE:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(1, 8, (uint8_t)(local_r13), v_stack_m15C);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), v_stack_m15C);
    v_stack_m1C0 = local_r12;
    v_stack_m1C8 = (uint32_t)((uint32_t)(v_stack_p20));
    v_stack_m1D0 = 0;
    v_stack_m1D8 = 1;
    Arg4 = 0;
    Arg3 = 0;
    result = SepInternalQuerySecurityAttributesTokenEx(v_stack_m170, (uint32_t)(v_stack_p20), Arg3, Arg4);
    v_stack_m13C = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), (uint32_t)(v_stack_p20), Arg3, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), (uint32_t)(v_stack_p20), Arg3, Arg4);
    goto loc_00AEEA01;
loc_00AEFC99:
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 8 - 7, (uint8_t)(local_r13), Arg4);
    if (v_stack_m178 == ((uint8_t)(v_stack_m170))) {
        Arg1 = *(uint64_t *)(v_stack_m170 + 0x450);
    }
    local_rsi = 8;
    if (Arg1 != 0) {
        result = *(uint8_t *)(Arg1 + 0x1);
        local_rsi = result * 4 + 16;
    }
    *(uint32_t *)(local_r12) = (uint32_t)(local_rsi);
    if (v_stack_p20 < ((uint32_t)(local_rsi))) goto loc_00AED89C;
    Arg2 = Arg3 + 8;
    if (Arg1 == 0) { Arg2 = Arg1; }
    *(uint64_t *)(arg3) = Arg2;
    if (Arg2 == 0) goto loc_00AEFD68;
    if (v_stack_m178 == ((uint8_t)(v_stack_m170))) {
        Arg3 = *(uint64_t *)(v_stack_m170 + 0x450);
    }
    result = RtlCopySid(local_rsi - 8, Arg2, Arg3, Arg4);
loc_00AEFD68:
    goto loc_00AED8D8;
loc_00AEFDC5:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m170))) - (53));
    if (condition_is_equal) goto loc_00AEEA8D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF025B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF0122;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AEFF80;
    if (((uint32_t)(Arg1)) != 2) goto loc_00AED7C4;
    v_stack_mF8 = v_xmm0;
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle((uint32_t)((uint32_t)(result)), 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 1, (uint8_t)(local_r13), Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x490)))) & (2)) != 0) goto loc_00AEFE87;
    goto loc_00AEF905;
loc_00AEFE87:
    result = SepGetAgentIdClaimValue(v_stack_m170, v_stack_mF8, (uint8_t)(local_r13), Arg4);
    v_stack_m13C = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000225ULL)))) {
        Arg2 = v_rip + 89922;
        Arg1 = v_stack_mF8;
        result = RtlInitUnicodeString(Arg1, Arg2, (uint8_t)(local_r13), Arg4);
        result = (uint32_t)(v_stack_m170);
        v_stack_m13C = (uint32_t)(result);
    }
    if (!sign_flag) goto loc_00AEFECF;
    goto loc_00AEF905;
loc_00AEFECF:
    v_stack_m15C = (uint32_t)(v_stack_mF8 + 2);
    if ((uint8_t)(local_r13) == 0) goto loc_00AEFEF4;
    result = RtlWriteULongToUser(local_r12, (uint32_t)((uint32_t)(v_stack_mF8 + 2)), (uint8_t)(local_r13), Arg4);
    goto loc_00AEFEF8;
loc_00AEFEF4:
    *(uint32_t *)(local_r12) = (uint32_t)(v_stack_mF8 + 2);
loc_00AEFEF8:
    if (v_stack_p20 < ((uint32_t)(v_stack_mF8 + 2))) goto loc_00AEDA2C;
    result = memcpy(Arg3, v_stack_mF0, v_stack_mF8, Arg4);
    local_rbx = (v_stack_mF8) >> (1);
    *(uint16_t *)(arg3 + local_rbx * 2) = (uint16_t)(v_stack_m170);
    goto loc_00AEDA8D;
loc_00AEFF80:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg3, v_stack_mF0, v_stack_mF8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(local_rbx, 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), (uint8_t)(8 - 7), (uint8_t)(local_r13), Arg4);
    if (*(uint64_t *)(v_stack_m170 + 0x498) == 0) goto loc_00AF0398;
    if ((*(uint32_t *)(v_stack_m170 + 0x4A0)) < 3) goto loc_00AF0037;
    result = SepIsAppSuiteSid(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x20), (uint8_t)(8 - 7), (uint8_t)(local_r13), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AF0037;
    goto loc_00AF003F;
loc_00AF0037:
loc_00AF003F:
    *(uint32_t *)(local_r12) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x20) + 0x1) * 4 + 16);
    if (v_stack_p20 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x20) + 0x1) * 4 + 16))) goto loc_00AED89C;
    if ((uint8_t)(v_stack_m160) != 0) goto loc_00AF00A6;
    *(uint64_t *)(arg3) = v_stack_m170;
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), (uint8_t)(8 - 7), v_stack_m160, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), (uint8_t)(8 - 7), v_stack_m160, Arg4);
    result = ObfDereferenceObjectWithTag(v_stack_m170, (uint32_t)(0x74726853ULL), v_stack_m160, Arg4);
    result = 0;
    goto loc_00AF0505;
loc_00AF00A6:
    *(void **)(arg3) = Arg3 + 8;
    if (Arg3 + 8 != 0) {
        Arg3 = *(uint64_t *)(v_stack_m170 + 0x498);
        Arg1 = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x20) + 0x1) * 4 + 16 - 8;
        Arg3 = *(uint64_t *)(arg3 + 0x20);
        result = RtlCopySid(Arg1, Arg3 + 8, Arg3, Arg4);
    }
    goto loc_00AED8D8;
loc_00AF0122:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, Arg3 + 8, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(8 - 7, 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 8 - 7, (uint8_t)(local_r13), Arg4);
    if (*(uint64_t *)(v_stack_m170 + 0x498) == 0) goto loc_00AF0398;
    if ((*(uint32_t *)(v_stack_m170 + 0x4A0)) < 2) goto loc_00AF0398;
    local_rsi = 8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x10) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x10) + 0x1);
        local_rsi = result * 4 + 16;
    }
    *(uint32_t *)(local_r12) = (uint32_t)(local_rsi);
    if (v_stack_p20 < ((uint32_t)(local_rsi))) goto loc_00AED89C;
    Arg2 = Arg3 + 8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x10) == 0) { Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498) + 0x10); }
    *(uint64_t *)(arg3) = Arg2;
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(v_stack_m170 + 0x498);
        Arg1 = local_rsi - 8;
        Arg3 = *(uint64_t *)(arg3 + 0x10);
        result = RtlCopySid(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00AF0335;
loc_00AF025B:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AED7C4;
    v_stack_m1C8 = v_stack_m168;
    v_stack_m1D0 = v_stack_m178;
    v_stack_m1D8 = v_stack_m170;
    result = SepReferenceTokenByHandle(8 - 7, 8, (uint8_t)(local_r13), Arg4);
    if (sign_flag) goto loc_00AF0505;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m170 + 0x30), 8 - 7, (uint8_t)(local_r13), Arg4);
    if (*(uint64_t *)(v_stack_m170 + 0x498) == 0) goto loc_00AF0398;
    if ((*(uint32_t *)(v_stack_m170 + 0x4A0)) == ((uint32_t)(v_stack_m170))) goto loc_00AF0398;
    local_rsi = 8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498)) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498)) + 0x1);
        local_rsi = result * 4 + 16;
    }
    *(uint32_t *)(local_r12) = (uint32_t)(local_rsi);
    if (v_stack_p20 < ((uint32_t)(local_rsi))) goto loc_00AED89C;
    Arg2 = Arg3 + 8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498)) == 0) { Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x498)); }
    *(uint64_t *)(arg3) = Arg2;
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(v_stack_m170 + 0x498);
        Arg1 = local_rsi - 8;
        Arg3 = *(uint64_t *)(arg3);
        result = RtlCopySid(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, Arg3, Arg4);
    goto loc_00AF03A6;
loc_00AF0398:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, Arg3, Arg4);
loc_00AF03A6:
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m170 + 0x30), Arg2, Arg3, Arg4);
    goto loc_00AEDFD7;
loc_00AF03B3:
    if (((uint32_t)(v_stack_m170)) != 23) goto loc_00AF03CF;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC8))) >> (9));
    goto loc_00AF04CC;
loc_00AF03CF:
    if (((uint32_t)(v_stack_m170)) != 24) goto loc_00AF03F0;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC8))) >> (10));
    goto loc_00AF04CC;
loc_00AF03F0:
    if (((uint32_t)(v_stack_m170)) != 26) goto loc_00AF040C;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC8))) >> (12));
    goto loc_00AF04CC;
loc_00AF040C:
    if (((uint32_t)(v_stack_m170)) != 40) goto loc_00AF042C;
    local_rdi = (((24) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC8))))) != 0) ? 1 : 0;
    goto loc_00AF04CF;
loc_00AF042C:
    if (((uint32_t)(v_stack_m170)) != 42) goto loc_00AF0446;
    goto loc_00AF04CC;
loc_00AF0446:
    if (((uint32_t)(v_stack_m170)) != 47) goto loc_00AF0461;
    result = SepIsSandboxedToken(v_stack_m170, (uint8_t)(local_r13), 24, Arg4);
    goto loc_00AF04B6;
loc_00AF0461:
    if (((uint32_t)(v_stack_m170)) != 48) goto loc_00AF0493;
    v_stack_m1D0 = (uint8_t)(*(uint16_t *)(v_stack_m170 + 0xCA));
    v_stack_m1D8 = 1;
    Arg4 = 0;
    Arg2 = 0;
    result = SepSidInTokenSidHash(v_stack_m170 + 808, Arg2, *(uint64_t *)(v_rip + 0x37774E), Arg4);
    goto loc_00AF04B6;
loc_00AF0493:
    if (((uint32_t)(v_stack_m170)) != 53) goto loc_00AF04BB;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m170 + 808, Arg2, *(uint64_t *)(v_rip + 0x37774E), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AED7CE;
    result = SeHasTamperProtection(v_stack_m170, Arg2, *(uint64_t *)(v_rip + 0x37774E), Arg4);
loc_00AF04B6:
    goto loc_00AF04CF;
loc_00AF04BB:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0xC8))) >> (14));
loc_00AF04CC:
    local_rdi = (uint32_t)((local_rdi) & (1));
loc_00AF04CF:
    *(uint32_t *)(arg3) = (uint32_t)(local_rdi);
    goto loc_00AEDA9B;
loc_00AF0505:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `8` | `W` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x0` | `128` | `W` |
| `Arg3` | `+ 0x0 + rbx*2` | `16` | `W` |
| `Arg3` | `+ 0x4` | `32` | `W` |
| `Arg3` | `+ 0x8` | `8` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `32` | `W` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0x14` | `32` | `W` |
| `Arg3` | `+ 0x18` | `32` | `W` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `W` |
| `Arg3` | `+ 0x1C` | `16` | `W` |
| `Arg3` | `+ 0x1C` | `32` | `W` |
| `Arg3` | `+ 0x1E` | `8` | `W` |
| `Arg3` | `+ 0x20` | `32` | `W` |
| `Arg3` | `+ 0x24` | `32` | `W` |
| `Arg3` | `+ 0x28` | `32` | `W` |
| `Arg3` | `+ 0x28` | `64` | `W` |
| `Arg3` | `+ 0x2C` | `32` | `W` |
| `Arg3` | `+ 0x30` | `64` | `W` |
| `Arg3` | `+ 0x38` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AECDD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
