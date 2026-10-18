# RtlEqualSid

- RVA: `0x00400AD0`–`0x00400AFF` (길이 `47` bytes)
- VA: `0x0000000140400AD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `15`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **60**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00400AEB` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)

### Direct callers
- [SepRmReferenceFindCap](../3A/SepRmReferenceFindCap_function_003A58EC.md) at `0x003A5959`
- [SepRemoveAceFromTokenDefaultDacl](SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) at `0x004001E0`
- [SeFastTraverseCheck](SeFastTraverseCheck_function_00400234.md) at `0x004002CB`
- [RtlFindAceBySid](RtlFindAceBySid_function_004004E0.md) at `0x0040053A`
- [SepCapabilitiesHasAppSiloBaseSID](SepCapabilitiesHasAppSiloBaseSID_function_004005B0.md) at `0x004005DA`
- [SepSetTrustLevelForProcessToken](SepSetTrustLevelForProcessToken_function_00400604.md) at `0x00400661`
- [sub_00400840](Unknown_function_00400840.md) at `0x0040099E`
- [SepCreateTokenEx](../4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004E9E18`
- [SepCreateTokenEx](../4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004E9E6C`
- [SepCreateTokenEx](../4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004E9E8B`
- [SepCreateTokenEx](../4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004E9FBB`
- [SepCreateTokenEx](../4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004E9FDD`
- [SepCreateAppContainerToken](../4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F4581`
- [RtlGetAppContainerNamedObjectPath](../5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E70EB`
- [SepApplyMandatoryAccess](../60/SepApplyMandatoryAccess_function_00607FF4.md) at `0x006080A7`
- [SeSetTokenTamperProtection](../60/SeSetTokenTamperProtection_function_00609644.md) at `0x0060974A`
- [SepFindMatchingAntiTamperEntry](../60/SepFindMatchingAntiTamperEntry_function_0060ADE4.md) at `0x0060AE3C`
- [RtlpCompareKnownObjectAces](../../page/70/RtlpCompareKnownObjectAces_function_00704670.md) at `0x007047B1`
- [PiDqSameUserHive](../../page/70/PiDqSameUserHive_function_007055B0.md) at `0x0070563F`
- [RtlpSysVolCheckOwnerAndSecurity](../../page/79/RtlpSysVolCheckOwnerAndSecurity_function_00791324.md) at `0x0079146F`
- [RtlpSysVolCheckOwnerAndSecurity](../../page/79/RtlpSysVolCheckOwnerAndSecurity_function_00791324.md) at `0x007914B5`
- [SepIdAssignableAsGroup](../../page/7A/SepIdAssignableAsGroup_function_007A01A0.md) at `0x007A01FE`
- [SepCompareSidValuesBlocks](../../page/7A/SepCompareSidValuesBlocks_function_007A0BE0.md) at `0x007A0C2E`
- [SepFindSharedSidEntry](../../page/7A/SepFindSharedSidEntry_function_007A3148.md) at `0x007A31A8`
- [SepIsSidEqual](../../page/7A/SepIsSidEqual_function_007A3764.md) at `0x007A377F`
- [ObpCreateHandle](../../page/86/ObpCreateHandle_function_0086B950.md) at `0x0086CF00`
- [SepAdtPrivilegeObjectAuditAlarm](../../page/86/SepAdtPrivilegeObjectAuditAlarm_function_0086E3F0.md) at `0x0086E548`
- [sub_00871B01](../../page/87/Unknown_function_00871B01.md) at `0x00871B52`
- [sub_00871B83](../../page/87/Unknown_function_00871B83.md) at `0x00871B99`
- [sub_00871B83](../../page/87/Unknown_function_00871B83.md) at `0x00871BAC`
- [SePrivilegedServiceAuditAlarm](../../page/87/SePrivilegedServiceAuditAlarm_function_00871CB0.md) at `0x00871CEF`
- [sub_00871D0C](../../page/87/Unknown_function_00871D0C.md) at `0x00871D22`
- [sub_00871D0C](../../page/87/Unknown_function_00871D0C.md) at `0x00871D35`
- [sub_00871E5A](../../page/87/Unknown_function_00871E5A.md) at `0x00871F2C`
- [sub_00871FFC](../../page/87/Unknown_function_00871FFC.md) at `0x0087200D`
- [sub_00871FFC](../../page/87/Unknown_function_00871FFC.md) at `0x00872024`
- [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) at `0x00872F44`
- [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) at `0x00872FEC`
- [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) at `0x00873003`
- [ObCreateObjectEx](../../page/89/ObCreateObjectEx_function_0089B1E0.md) at `0x0089B4C5`
- [ObCreateObjectEx](../../page/89/ObCreateObjectEx_function_0089B1E0.md) at `0x0089B5B9`
- [ObCreateObjectEx](../../page/89/ObCreateObjectEx_function_0089B1E0.md) at `0x0089B5D4`
- [SepCreateImpersonationTokenDacl](../../page/8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B87D4`
- [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) at `0x008B94B1`
- [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) at `0x008B9563`
- [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) at `0x008B9584`
- [CmpCheckKeyOwnerForPca](../../page/8C/CmpCheckKeyOwnerForPca_function_008C7130.md) at `0x008C716F`
- [SeTokenCanImpersonate](../../page/8C/SeTokenCanImpersonate_function_008CC4C0.md) at `0x008CC561`
- [sub_008CC5C2](../../page/8C/Unknown_function_008CC5C2.md) at `0x008CC65A`
- [sub_008CC5C2](../../page/8C/Unknown_function_008CC5C2.md) at `0x008CC741`
- [SysCtxRegOpenCurrentUserKey](../../page/8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) at `0x008F46B9`
- [SeCompareTokens](../../page/8F/SeCompareTokens_function_008F6F40.md) at `0x008F6F8D`
- [SeCompareTokens](../../page/8F/SeCompareTokens_function_008F6F40.md) at `0x008F710A`
- [SeCompareTokens](../../page/8F/SeCompareTokens_function_008F6F40.md) at `0x008F713C`
- [SepCompareSidAndAttributeArrays](../../page/8F/SepCompareSidAndAttributeArrays_function_008F7284.md) at `0x008F72D3`
- [sub_0092949C](../../page/92/Unknown_function_0092949C.md) at `0x009295F0`
- [RtlpGenerateInheritedAce](../../page/92/RtlpGenerateInheritedAce_function_0092DB80.md) at `0x0092DDD6`
- [sub_0092EAA3](../../page/92/Unknown_function_0092EAA3.md) at `0x0092EB47`
- [SeCheckAuditPrivilege](../../page/97/SeCheckAuditPrivilege_function_00974E48.md) at `0x00974ED3`
- [SeCheckAuditPrivilege](../../page/97/SeCheckAuditPrivilege_function_00974E48.md) at `0x00974F18`
- [SeCheckAuditPrivilege](../../page/97/SeCheckAuditPrivilege_function_00974E48.md) at `0x00974F2B`
- [PiDevCfgGetKeySecurityDescriptor](../../page/99/PiDevCfgGetKeySecurityDescriptor_function_00996240.md) at `0x00996312`
- [PiDevCfgGetKeySecurityDescriptor](../../page/99/PiDevCfgGetKeySecurityDescriptor_function_00996240.md) at `0x00996409`
- [CmpCheckExeOwnerForPca](../../page/9A/CmpCheckExeOwnerForPca_function_009A343C.md) at `0x009A3515`
- [CmpBuildAdminInformation](../../page/9A/CmpBuildAdminInformation_function_009A8884.md) at `0x009A8926`
- [SepFindMatchingCachedHandlesEntry](../../page/9A/SepFindMatchingCachedHandlesEntry_function_009A9698.md) at `0x009A96F0`
- [SepAdjustGroups](../../page/9C/SepAdjustGroups_function_009C63A8.md) at `0x009C647B`
- [AlpcpPortQueryConnectedSidInfo](../../page/9C/AlpcpPortQueryConnectedSidInfo_function_009CAC3C.md) at `0x009CAD8F`
- [SepNewTokenAsRestrictedAsProcessToken](../../page/A2/SepNewTokenAsRestrictedAsProcessToken_function_00A20A98.md) at `0x00A20B95`
- [SepNewTokenAsRestrictedAsProcessToken](../../page/A2/SepNewTokenAsRestrictedAsProcessToken_function_00A20A98.md) at `0x00A20C13`
- [AlpcpCheckConnectionSecurity](../../page/A2/AlpcpCheckConnectionSecurity_function_00A227A0.md) at `0x00A22854`
- [SepValidOwnerSubjectContext](../../page/A3/SepValidOwnerSubjectContext_function_00A37568.md) at `0x00A375F4`
- [ObpVerifyAccessToBoundaryEntry](../../page/A5/ObpVerifyAccessToBoundaryEntry_function_00A5E500.md) at `0x00A5E6EF`
- [SepFindMatchingLowBoxNumberEntry](../../page/A7/SepFindMatchingLowBoxNumberEntry_function_00A74544.md) at `0x00A745A6`
- [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4AF4`
- [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4B31`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9E3C`
- [PspLookupProcessQuotaBlock](../../page/AE/PspLookupProcessQuotaBlock_function_00AE336C.md) at `0x00AE33F3`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE87D`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0B61`
- [sub_00B1F050](../../page/B1/Unknown_function_00B1F050.md) at `0x00B1F056`
- [sub_00B1F050](../../page/B1/Unknown_function_00B1F050.md) at `0x00B1F09F`
- [sub_00B375D4](../../page/B3/Unknown_function_00B375D4.md) at `0x00B37778`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00400AD0  48 83 EC 28                     sub rsp, 0x28
00400AD4  0F B7 01                        movzx eax, word ptr [rcx]
00400AD7  66 3B 02                        cmp ax, word ptr [rdx]
00400ADA  75 1F                           jne 0x140400afb
00400ADC  44 8B C0                        mov r8d, eax
00400ADF  49 C1 E8 08                     shr r8, 8
00400AE3  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
00400AEB  E8 20 60 2C 00                  call 0x1406c6b10
00400AF0  85 C0                           test eax, eax
00400AF2  0F 94 C0                        sete al
00400AF5  48 83 C4 28                     add rsp, 0x28
00400AF9  C3                              ret
00400AFA  CC                              int3
00400AFB  32 C0                           xor al, al
00400AFD  EB F6                           jmp 0x140400af5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlEqualSid(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) != (*(unsigned __int16 *)(a2))) goto loc_00400AFB;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1)))) >> (8);
    result = memcmp(a1, a2, a3 * 4 + 8, a4);
    result = ((unsigned int)(result) == 0) ? 1 : 0;
loc_00400AF5:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00400AFB:
    result = 0;
    goto loc_00400AF5;
}
```

## 5. (Beta) C Style

```c
int64_t RtlEqualSid(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint16_t)(*(uint16_t *)(arg1))) != (*(uint16_t *)(arg2))) goto loc_00400AFB;
    a3 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1)))) >> (8);
    result = memcmp(Arg1, Arg2, a3 * 4 + 8, a4);
    result = ((uint32_t)(result) == 0) ? 1 : 0;
loc_00400AF5:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00400AFB:
    result = 0;
    goto loc_00400AF5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00400AD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00400AD0[BB_00400AD0]
  bb_00400ADC[BB_00400ADC]
  bb_00400AF5[BB_00400AF5]
  bb_00400AFA[BB_00400AFA]
  bb_00400AFB[BB_00400AFB]
  bb_00400AD0 -->|branch| bb_00400AFB
  bb_00400AD0 -->|fallthrough| bb_00400ADC
  bb_00400ADC -->|flow| bb_00400AF5
  bb_00400AFA -->|flow| bb_00400AFB
  bb_00400AFB -->|branch| bb_00400AF5
```
