# EtwpEnableGuid

- RVA: `0x00A5CD28`–`0x00A5DA00` (길이 `3,288` bytes)
- VA: `0x0000000140A5CD28`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B27E0`
- 디코드: `828`개 명령, `3,288/3,288` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **66**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00A5CDBC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A5CDFC` → [EtwpValidateEnableNotification](../8C/EtwpValidateEnableNotification_function_008C779C.md) (function, `0x008C779C`)
- `0x00A5CE25` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A5CE38` → [EtwpEventWriteCaptureState](../AA/EtwpEventWriteCaptureState_function_00AA23F8.md) (function, `0x00AA23F8`)
- `0x00A5CEEF` → [EtwpEnableDisableSpecialGuids](../9E/EtwpEnableDisableSpecialGuids_function_009E3A88.md) (function, `0x009E3A88`)
- `0x00A5CEF6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A5CF2C` → [EtwpEnableMetaProviderGuid](../../text/43/EtwpEnableMetaProviderGuid_function_00437AE0.md) (function, `0x00437AE0`)
- `0x00A5CF51` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x00A5CF7D` → [EtwpFindGuidEntryByGuid](../8C/EtwpFindGuidEntryByGuid_function_008C1DB0.md) (function, `0x008C1DB0`)
- `0x00A5CFB7` → [EtwpAddGuidEntry](../8B/EtwpAddGuidEntry_function_008BFC80.md) (function, `0x008BFC80`)
- `0x00A5D032` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A5D079` → [EtwpEventWriteProviderEnabled](../A8/EtwpEventWriteProviderEnabled_function_00A85D74.md) (function, `0x00A85D74`)
- `0x00A5D097` → [EtwpEventWriteTemplateSessAndProv](../86/EtwpEventWriteTemplateSessAndProv_function_00863D18.md) (function, `0x00863D18`)
- `0x00A5D0C0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A5D0D9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A5D16A` → [EtwpAcquireTokenAccessInformation](../A8/EtwpAcquireTokenAccessInformation_function_00A83AC0.md) (function, `0x00A83AC0`)
- `0x00A5D1F2` → [EtwpUpdateGuidEnableInfo](../9F/EtwpUpdateGuidEnableInfo_function_009FCF48.md) (function, `0x009FCF48`)
- `0x00A5D224` → [EtwpPreallocateApcPool](../A6/EtwpPreallocateApcPool_function_00A67908.md) (function, `0x00A67908`)
- `0x00A5D24D` → [EtwpReferenceStackLookasideList](../A7/EtwpReferenceStackLookasideList_function_00A7EF68.md) (function, `0x00A7EF68`)
- `0x00A5D28E` → [EtwpCreateUmReplyObject](../A8/EtwpCreateUmReplyObject_function_00A8DBE4.md) (function, `0x00A8DBE4`)
- `0x00A5D2B8` → [EtwpBuildNotificationPacket](../9E/EtwpBuildNotificationPacket_function_009EB13C.md) (function, `0x009EB13C`)
- `0x00A5D2DD` → [EtwpAllocDataBlock](../9F/EtwpAllocDataBlock_function_009FEE38.md) (function, `0x009FEE38`)
- `0x00A5D3B0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A5D3C9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A5D42A` → [EtwpIsRegEntryAllowed](../9E/EtwpIsRegEntryAllowed_function_009EB2D0.md) (function, `0x009EB2D0`)
- `0x00A5D4A0` → [EtwpUpdateRegEntryEnableMask](../8C/EtwpUpdateRegEntryEnableMask_function_008C1990.md) (function, `0x008C1990`)
- `0x00A5D4D6` → [EtwpCalculateUpdateNotification](../8C/EtwpCalculateUpdateNotification_function_008C0BE0.md) (function, `0x008C0BE0`)
- `0x00A5D518` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x00A5D561` → [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) (function, `0x00A03F94`)
- `0x00A5D56D` → [EtwpSendDataBlock](../8C/EtwpSendDataBlock_function_008C8530.md) (function, `0x008C8530`)
- `0x00A5D5C8` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00A5D5D0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A5D5D5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A5D63C` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00A5D644` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A5D649` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A5D690` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A5D6A9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A5D701` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00A5D724` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00A5D72C` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x00A5D73E` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00A5D74B` → [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) (function, `0x00A03F94`)
- `0x00A5D756` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00A5D75E` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x00A5D76E` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00A5D77C` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x00A5D795` → [EtwpDemuxPrivateTraceHandle](../AC/EtwpDemuxPrivateTraceHandle_function_00ACDB1C.md) (function, `0x00ACDB1C`)
- `0x00A5D7C5` → [EtwpAllocDataBlock](../9F/EtwpAllocDataBlock_function_009FEE38.md) (function, `0x009FEE38`)
- `0x00A5D7D5` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x00A5D851` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00A5D859` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A5D85E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A5D8B2` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A5D8F9` → [EtwpEventWriteProviderEnabled](../A8/EtwpEventWriteProviderEnabled_function_00A85D74.md) (function, `0x00A85D74`)
- `0x00A5D91E` → [EtwpEventWriteTemplateSessAndProv](../86/EtwpEventWriteTemplateSessAndProv_function_00863D18.md) (function, `0x00863D18`)
- `0x00A5D934` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x00A5D945` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x00A5D989` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00A5D991` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A5D996` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A5D9AA` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00A5D9B8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A5D9C5` → [EtwpUnreferenceGuidEntry](../8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x00A5D9CE` → [EtwpFreeFilterInfo](../8C/EtwpFreeFilterInfo_function_008C8A24.md) (function, `0x008C8A24`)
- `0x00A5D9DF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpEnableTrace](EtwpEnableTrace_function_00A5C8EC.md) at `0x00A5CA50`
- [NtTraceControl](../A9/NtTraceControl_function_00A9ED40.md) at `0x00A9F1F4`

### Static image references
- `0x00A5CD47` → RVA `0x00E0A740` (`.data`; read)
- `0x00A5CE17` → RVA `0x00EFF840` (`.data`; read)
- `0x00A5CE1E` → RVA `0x0001C7E0` (`.rdata`; read)
- `0x00A5CF5A` → RVA `0x00011380` (`.rdata`; read)
- `0x00A5CFF0` → RVA `0x00013050` (`.rdata`; read)
- `0x00A5D001` → RVA `0x00013058` (`.rdata`; read)
- `0x00A5D019` → RVA `0x00021330` (`.rdata`; read)
- `0x00A5D024` → RVA `0x00020D60` (`.rdata`; read)
- `0x00A5D120` → RVA `0x0001A698` (`.rdata`; read)
- `0x00A5D12D` → RVA `0x0001A6A0` (`.rdata`; read)
- `0x00A5D89D` → RVA `0x00020F70` (`.rdata`; read)
- `0x00A5D8A4` → RVA `0x000213D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **35**
  - `0x00A5CDBC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A5CE25` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A5CEF6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A5CF2C` → [EtwpEnableMetaProviderGuid](../../text/43/EtwpEnableMetaProviderGuid_function_00437AE0.md) (`PAGE` → `.text`)
  - `0x00A5CF51` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x00A5D032` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A5D0C0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A5D0D9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A5D3B0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A5D3C9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A5D5C8` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00A5D5D0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A5D5D5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A5D63C` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00A5D644` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A5D649` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A5D690` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A5D6A9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A5D701` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00A5D724` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00A5D72C` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x00A5D73E` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00A5D756` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00A5D75E` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x00A5D76E` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00A5D77C` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x00A5D851` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00A5D859` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A5D85E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A5D8B2` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A5D989` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00A5D991` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A5D996` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A5D9B8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A5D9DF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A5CD28  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A5CD2D  55                              push rbp
00A5CD2E  56                              push rsi
00A5CD2F  57                              push rdi
00A5CD30  41 54                           push r12
00A5CD32  41 55                           push r13
00A5CD34  41 56                           push r14
00A5CD36  41 57                           push r15
00A5CD38  48 8D AC 24 40 FF FF FF         lea rbp, [rsp - 0xc0]
00A5CD40  48 81 EC C0 01 00 00            sub rsp, 0x1c0
00A5CD47  48 8B 05 F2 D9 3A 00            mov rax, qword ptr [rip + 0x3ad9f2]
00A5CD4E  48 33 C4                        xor rax, rsp
00A5CD51  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00A5CD58  45 33 E4                        xor r12d, r12d
00A5CD5B  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
00A5CD5F  41 8A D8                        mov bl, r8b
00A5CD62  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00A5CD66  4C 8B EA                        mov r13, rdx
00A5CD69  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
00A5CD6D  4C 8B F9                        mov r15, rcx
00A5CD70  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
00A5CD74  0F 57 C0                        xorps xmm0, xmm0
00A5CD77  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
00A5CD7C  33 C0                           xor eax, eax
00A5CD7E  44 88 64 24 54                  mov byte ptr [rsp + 0x54], r12b
00A5CD83  4C 8D 72 48                     lea r14, [rdx + 0x48]
00A5CD87  44 88 64 24 52                  mov byte ptr [rsp + 0x52], r12b
00A5CD8C  45 8D 44 24 68                  lea r8d, [r12 + 0x68]
00A5CD91  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00A5CD94  33 D2                           xor edx, edx
00A5CD96  66 44 89 64 24 74               mov word ptr [rsp + 0x74], r12w
00A5CD9C  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00A5CDA0  66 44 89 64 24 5C               mov word ptr [rsp + 0x5c], r12w
00A5CDA6  41 8B F4                        mov esi, r12d
00A5CDA9  44 88 64 24 53                  mov byte ptr [rsp + 0x53], r12b
00A5CDAE  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00A5CDB2  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
00A5CDB7  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00A5CDBC  E8 7F 9E C6 FF                  call 0x1406c6c40
00A5CDC1  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00A5CDC5  4C 8D 4D C0                     lea r9, [rbp - 0x40]
00A5CDC9  83 E0 20                        and eax, 0x20
00A5CDCC  66 44 89 64 24 70               mov word ptr [rsp + 0x70], r12w
00A5CDD2  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A5CDD6  44 8A C3                        mov r8b, bl
00A5CDD9  F7 D8                           neg eax
00A5CDDB  49 8B D5                        mov rdx, r13
00A5CDDE  49 8B CF                        mov rcx, r15
00A5CDE1  1A C0                           sbb al, al
00A5CDE3  24 02                           and al, 2
00A5CDE5  88 44 24 51                     mov byte ptr [rsp + 0x51], al
00A5CDE9  48 8D 45 F0                     lea rax, [rbp - 0x10]
00A5CDED  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A5CDF2  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A5CDF7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5CDFC  E8 9B A9 E6 FF                  call 0x1408c779c
00A5CE01  45 33 DB                        xor r11d, r11d
00A5CE04  8B D8                           mov ebx, eax
00A5CE06  85 C0                           test eax, eax
00A5CE08  0F 88 8D 0B 00 00               js 0x140a5d99b
00A5CE0E  45 8B 26                        mov r12d, dword ptr [r14]
00A5CE11  41 83 FC 02                     cmp r12d, 2
00A5CE15  75 29                           jne 0x140a5ce40
00A5CE17  48 8B 0D 22 2A 4A 00            mov rcx, qword ptr [rip + 0x4a2a22]
00A5CE1E  48 8D 15 BB F9 5B FF            lea rdx, [rip - 0xa40645]
00A5CE25  E8 26 56 93 FF                  call 0x140392450
00A5CE2A  45 33 DB                        xor r11d, r11d
00A5CE2D  84 C0                           test al, al
00A5CE2F  74 0F                           je 0x140a5ce40
00A5CE31  4D 8D 45 28                     lea r8, [r13 + 0x28]
00A5CE35  49 8B D6                        mov rdx, r14
00A5CE38  E8 BB 55 04 00                  call 0x140aa23f8
00A5CE3D  45 33 DB                        xor r11d, r11d
00A5CE40  41 8B 7D 74                     mov edi, dword ptr [r13 + 0x74]
00A5CE44  8D 47 FF                        lea eax, [rdi - 1]
00A5CE47  83 F8 01                        cmp eax, 1
00A5CE4A  77 48                           ja 0x140a5ce94
00A5CE4C  49 8D 45 78                     lea rax, [r13 + 0x78]
00A5CE50  85 FF                           test edi, edi
00A5CE52  74 4A                           je 0x140a5ce9e
00A5CE54  4C 8D 8D 94 00 00 00            lea r9, [rbp + 0x94]
00A5CE5B  44 8B D7                        mov r10d, edi
00A5CE5E  4C 2B C8                        sub r9, rax
00A5CE61  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
00A5CE68  4C 2B C0                        sub r8, rax
00A5CE6B  48 8D 50 08                     lea rdx, [rax + 8]
00A5CE6F  8B 42 04                        mov eax, dword ptr [rdx + 4]
00A5CE72  48 8B 4A F8                     mov rcx, qword ptr [rdx - 8]
00A5CE76  49 03 CD                        add rcx, r13
00A5CE79  41 89 04 11                     mov dword ptr [r9 + rdx], eax
00A5CE7D  8B 02                           mov eax, dword ptr [rdx]
00A5CE7F  49 89 4C 10 F8                  mov qword ptr [r8 + rdx - 8], rcx
00A5CE84  41 89 04 10                     mov dword ptr [r8 + rdx], eax
00A5CE88  48 8D 52 10                     lea rdx, [rdx + 0x10]
00A5CE8C  49 83 EA 01                     sub r10, 1
00A5CE90  75 DD                           jne 0x140a5ce6f
00A5CE92  EB 0A                           jmp 0x140a5ce9e
00A5CE94  41 8B FB                        mov edi, r11d
00A5CE97  44 89 9D 9C 00 00 00            mov dword ptr [rbp + 0x9c], r11d
00A5CE9E  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A5CEA2  44 39 5C 24 58                  cmp dword ptr [rsp + 0x58], r11d
00A5CEA7  0F 85 F2 00 00 00               jne 0x140a5cf9f
00A5CEAD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5CEB6  49 8D 55 28                     lea rdx, [r13 + 0x28]
00A5CEBA  45 8B CC                        mov r9d, r12d
00A5CEBD  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
00A5CEC4  90                              nop
00A5CEC5  45 0F B7 46 06                  movzx r8d, word ptr [r14 + 6]
00A5CECA  48 8D 44 24 53                  lea rax, [rsp + 0x53]
00A5CECF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A5CED4  49 8B CF                        mov rcx, r15
00A5CED7  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00A5CEDE  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00A5CEE2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A5CEE7  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00A5CEEB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A5CEEF  E8 94 6B F8 FF                  call 0x1409e3a88
00A5CEF4  8B D8                           mov ebx, eax
00A5CEF6  E8 B5 09 80 FF                  call 0x14025d8b0
00A5CEFB  45 33 DB                        xor r11d, r11d
00A5CEFE  44 38 5C 24 53                  cmp byte ptr [rsp + 0x53], r11b
00A5CF03  0F 85 92 0A 00 00               jne 0x140a5d99b
00A5CF09  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
00A5CF0D  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00A5CF14  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00A5CF18  49 8D 55 28                     lea rdx, [r13 + 0x28]
00A5CF1C  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5CF21  45 8B C4                        mov r8d, r12d
00A5CF24  48 8B CF                        mov rcx, rdi
00A5CF27  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5CF2C  E8 AF AB 9D FF                  call 0x140437ae0
00A5CF31  8B D8                           mov ebx, eax
00A5CF33  3D 95 02 00 C0                  cmp eax, 0xc0000295
00A5CF38  0F 85 62 0A 00 00               jne 0x140a5d9a0
00A5CF3E  45 33 DB                        xor r11d, r11d
00A5CF41  B9 FD FF 00 00                  mov ecx, 0xfffd
00A5CF46  66 41 85 4E 06                  test word ptr [r14 + 6], cx
00A5CF4B  0F 84 D4 09 00 00               je 0x140a5d925
00A5CF51  E8 0A 66 9D FF                  call 0x140433560
00A5CF56  40 8A 75 D2                     mov sil, byte ptr [rbp - 0x2e]
00A5CF5A  48 8D 15 1F 44 5B FF            lea rdx, [rip - 0xa4bbe1]
00A5CF61  44 0F B6 7C 24 51               movzx r15d, byte ptr [rsp + 0x51]
00A5CF67  40 84 F6                        test sil, sil
00A5CF6A  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A5CF6E  45 8B C7                        mov r8d, r15d
00A5CF71  41 89 45 24                     mov dword ptr [r13 + 0x24], eax
00A5CF75  49 8D 45 28                     lea rax, [r13 + 0x28]
00A5CF79  48 0F 44 D0                     cmove rdx, rax
00A5CF7D  E8 2E 4E E6 FF                  call 0x1408c1db0
00A5CF82  45 33 DB                        xor r11d, r11d
00A5CF85  48 8B D8                        mov rbx, rax
00A5CF88  48 85 C0                        test rax, rax
00A5CF8B  75 45                           jne 0x140a5cfd2
00A5CF8D  40 84 F6                        test sil, sil
00A5CF90  74 14                           je 0x140a5cfa6
00A5CF92  BB 95 02 00 C0                  mov ebx, 0xc0000295
00A5CF97  49 8B F3                        mov rsi, r11
00A5CF9A  E9 01 0A 00 00                  jmp 0x140a5d9a0
00A5CF9F  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5CFA4  EB 9B                           jmp 0x140a5cf41
00A5CFA6  41 83 FC 01                     cmp r12d, 1
00A5CFAA  75 E6                           jne 0x140a5cf92
00A5CFAC  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A5CFB0  49 8D 55 28                     lea rdx, [r13 + 0x28]
00A5CFB4  45 8B C7                        mov r8d, r15d
00A5CFB7  E8 C4 2C E6 FF                  call 0x1408bfc80
00A5CFBC  48 8B F0                        mov rsi, rax
00A5CFBF  48 85 C0                        test rax, rax
00A5CFC2  0F 85 D4 00 00 00               jne 0x140a5d09c
00A5CFC8  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A5CFCD  E9 CE 09 00 00                  jmp 0x140a5d9a0
00A5CFD2  41 83 FC 01                     cmp r12d, 1
00A5CFD6  74 0C                           je 0x140a5cfe4
00A5CFD8  48 8B F3                        mov rsi, rbx
00A5CFDB  45 85 E4                        test r12d, r12d
00A5CFDE  0F 85 B8 00 00 00               jne 0x140a5d09c
00A5CFE4  48 8B F3                        mov rsi, rbx
00A5CFE7  48 85 FF                        test rdi, rdi
00A5CFEA  0F 84 AC 00 00 00               je 0x140a5d09c
00A5CFF0  48 8B 05 59 60 5B FF            mov rax, qword ptr [rip - 0xa49fa7]
00A5CFF7  49 3B 45 28                     cmp rax, qword ptr [r13 + 0x28]
00A5CFFB  0F 85 9B 00 00 00               jne 0x140a5d09c
00A5D001  48 8B 05 50 60 5B FF            mov rax, qword ptr [rip - 0xa49fb0]
00A5D008  49 3B 45 30                     cmp rax, qword ptr [r13 + 0x30]
00A5D00C  0F 85 8A 00 00 00               jne 0x140a5d09c
00A5D012  48 8B 0D 27 28 4A 00            mov rcx, qword ptr [rip + 0x4a2827]
00A5D019  48 8D 05 10 43 5C FF            lea rax, [rip - 0xa3bcf0]
00A5D020  41 83 FC 01                     cmp r12d, 1
00A5D024  4C 8D 3D 35 3D 5C FF            lea r15, [rip - 0xa3c2cb]
00A5D02B  4C 0F 45 F8                     cmovne r15, rax
00A5D02F  49 8B D7                        mov rdx, r15
00A5D032  E8 19 54 93 FF                  call 0x140392450
00A5D037  84 C0                           test al, al
00A5D039  74 61                           je 0x140a5d09c
00A5D03B  48 8D 0D 0E 60 5B FF            lea rcx, [rip - 0xa49ff2]
00A5D042  49 8B D7                        mov rdx, r15
00A5D045  41 83 FC 01                     cmp r12d, 1
00A5D049  75 35                           jne 0x140a5d080
00A5D04B  41 8A 46 04                     mov al, byte ptr [r14 + 4]
00A5D04F  4C 8D 8F 88 00 00 00            lea r9, [rdi + 0x88]
00A5D056  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A5D05A  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00A5D05E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A5D062  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00A5D066  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A5D06B  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00A5D06F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A5D074  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A5D079  E8 F6 8C 02 00                  call 0x140a85d74
00A5D07E  EB 1C                           jmp 0x140a5d09c
00A5D080  48 8D 87 88 00 00 00            lea rax, [rdi + 0x88]
00A5D087  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A5D08C  41 B9 02 00 00 00               mov r9d, 2
00A5D092  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5D097  E8 7C 6C E0 FF                  call 0x140863d18
00A5D09C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5D0A5  48 8D 9E 98 02 00 00            lea rbx, [rsi + 0x298]
00A5D0AC  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A5D0B0  45 33 C0                        xor r8d, r8d
00A5D0B3  33 D2                           xor edx, edx
00A5D0B5  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
00A5D0BC  48 8B CB                        mov rcx, rbx
00A5D0BF  90                              nop
00A5D0C0  E8 6B 31 7B FF                  call 0x140210230
00A5D0C5  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00A5D0CB  48 8B F8                        mov rdi, rax
00A5D0CE  73 0E                           jae 0x140a5d0de
00A5D0D0  4C 8B C3                        mov r8, rbx
00A5D0D3  48 8B D0                        mov rdx, rax
00A5D0D6  48 8B CB                        mov rcx, rbx
00A5D0D9  E8 B2 2B 7B FF                  call 0x14020fc90
00A5D0DE  45 33 DB                        xor r11d, r11d
00A5D0E1  48 85 FF                        test rdi, rdi
00A5D0E4  74 04                           je 0x140a5d0ea
00A5D0E6  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00A5D0EA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5D0F3  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00A5D0F8  48 89 86 A0 02 00 00            mov qword ptr [rsi + 0x2a0], rax
00A5D0FF  C6 44 24 54 01                  mov byte ptr [rsp + 0x54], 1
00A5D104  41 83 FC 01                     cmp r12d, 1
00A5D108  75 3A                           jne 0x140a5d144
00A5D10A  44 84 66 5B                     test byte ptr [rsi + 0x5b], r12b
00A5D10E  74 34                           je 0x140a5d144
00A5D110  45 85 FF                        test r15d, r15d
00A5D113  75 2F                           jne 0x140a5d144
00A5D115  0F B7 46 58                     movzx eax, word ptr [rsi + 0x58]
00A5D119  66 41 39 46 06                  cmp word ptr [r14 + 6], ax
00A5D11E  74 24                           je 0x140a5d144
00A5D120  48 8B 05 71 D5 5B FF            mov rax, qword ptr [rip - 0xa42a8f]
00A5D127  48 3B 46 28                     cmp rax, qword ptr [rsi + 0x28]
00A5D12B  75 17                           jne 0x140a5d144
00A5D12D  48 8B 05 6C D5 5B FF            mov rax, qword ptr [rip - 0xa42a94]
00A5D134  48 3B 46 30                     cmp rax, qword ptr [rsi + 0x30]
00A5D138  75 0A                           jne 0x140a5d144
00A5D13A  BB 03 03 00 C0                  mov ebx, 0xc0000303
00A5D13F  E9 10 08 00 00                  jmp 0x140a5d954
00A5D144  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D149  48 85 FF                        test rdi, rdi
00A5D14C  74 14                           je 0x140a5d162
00A5D14E  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
00A5D154  A8 40                           test al, 0x40
00A5D156  74 0A                           je 0x140a5d162
00A5D158  BB 96 02 00 C0                  mov ebx, 0xc0000296
00A5D15D  E9 F2 07 00 00                  jmp 0x140a5d954
00A5D162  45 85 FF                        test r15d, r15d
00A5D165  74 15                           je 0x140a5d17c
00A5D167  48 8B CF                        mov rcx, rdi
00A5D16A  E8 51 69 02 00                  call 0x140a83ac0
00A5D16F  45 33 DB                        xor r11d, r11d
00A5D172  8B D8                           mov ebx, eax
00A5D174  85 C0                           test eax, eax
00A5D176  0F 85 D8 07 00 00               jne 0x140a5d954
00A5D17C  45 89 65 70                     mov dword ptr [r13 + 0x70], r12d
00A5D180  BA FF 7F 00 00                  mov edx, 0x7fff
00A5D185  41 0F B7 4E 06                  movzx ecx, word ptr [r14 + 6]
00A5D18A  66 41 89 4D 68                  mov word ptr [r13 + 0x68], cx
00A5D18F  41 8A 46 04                     mov al, byte ptr [r14 + 4]
00A5D193  41 88 45 6A                     mov byte ptr [r13 + 0x6a], al
00A5D197  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00A5D19B  41 89 45 6C                     mov dword ptr [r13 + 0x6c], eax
00A5D19F  8A 45 D2                        mov al, byte ptr [rbp - 0x2e]
00A5D1A2  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
00A5D1A6  84 C0                           test al, al
00A5D1A8  74 0D                           je 0x140a5d1b7
00A5D1AA  66 23 CA                        and cx, dx
00A5D1AD  41 C6 45 6B 01                  mov byte ptr [r13 + 0x6b], 1
00A5D1B2  66 41 89 4D 68                  mov word ptr [r13 + 0x68], cx
00A5D1B7  4D 39 5E 10                     cmp qword ptr [r14 + 0x10], r11
00A5D1BB  75 08                           jne 0x140a5d1c5
00A5D1BD  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A5D1C1  49 89 4E 10                     mov qword ptr [r14 + 0x10], rcx
00A5D1C5  45 38 5E 04                     cmp byte ptr [r14 + 4], r11b
00A5D1C9  75 05                           jne 0x140a5d1d0
00A5D1CB  41 C6 46 04 FF                  mov byte ptr [r14 + 4], 0xff
00A5D1D0  41 83 FC 02                     cmp r12d, 2
00A5D1D4  0F 84 80 00 00 00               je 0x140a5d25a
00A5D1DA  84 C0                           test al, al
00A5D1DC  75 7C                           jne 0x140a5d25a
00A5D1DE  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
00A5D1E3  49 8B D5                        mov rdx, r13
00A5D1E6  4C 8D 4D F0                     lea r9, [rbp - 0x10]
00A5D1EA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5D1EF  48 8B CE                        mov rcx, rsi
00A5D1F2  E8 51 FD F9 FF                  call 0x1409fcf48
00A5D1F7  45 33 DB                        xor r11d, r11d
00A5D1FA  8B D8                           mov ebx, eax
00A5D1FC  85 C0                           test eax, eax
00A5D1FE  0F 88 50 07 00 00               js 0x140a5d954
00A5D204  0F 10 46 60                     movups xmm0, xmmword ptr [rsi + 0x60]
00A5D208  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00A5D20C  0F 10 4E 70                     movups xmm1, xmmword ptr [rsi + 0x70]
00A5D210  41 0F 11 4E 10                  movups xmmword ptr [r14 + 0x10], xmm1
00A5D215  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00A5D219  A8 04                           test al, 4
00A5D21B  74 3D                           je 0x140a5d25a
00A5D21D  48 8D 8F 40 03 00 00            lea rcx, [rdi + 0x340]
00A5D224  E8 DF A6 00 00                  call 0x140a67908
00A5D229  0F 0D 8F 30 03 00 00            prefetchw byte ptr [rdi + 0x330]
00A5D230  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
00A5D236  BA 00 20 00 00                  mov edx, 0x2000
00A5D23B  8B C8                           mov ecx, eax
00A5D23D  0B CA                           or ecx, edx
00A5D23F  F0 0F B1 8F 30 03 00 00         lock cmpxchg dword ptr [rdi + 0x330], ecx
00A5D247  75 F2                           jne 0x140a5d23b
00A5D249  85 C2                           test edx, eax
00A5D24B  75 05                           jne 0x140a5d252
00A5D24D  E8 16 1D 02 00                  call 0x140a7ef68
00A5D252  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D257  45 33 DB                        xor r11d, r11d
00A5D25A  48 8D 46 38                     lea rax, [rsi + 0x38]
00A5D25E  48 39 00                        cmp qword ptr [rax], rax
00A5D261  75 1A                           jne 0x140a5d27d
00A5D263  4C 39 9E 90 02 00 00            cmp qword ptr [rsi + 0x290], r11
00A5D26A  75 09                           jne 0x140a5d275
00A5D26C  48 8D 46 10                     lea rax, [rsi + 0x10]
00A5D270  48 39 00                        cmp qword ptr [rax], rax
00A5D273  75 08                           jne 0x140a5d27d
00A5D275  41 8B DB                        mov ebx, r11d
00A5D278  E9 D7 06 00 00                  jmp 0x140a5d954
00A5D27D  45 38 5D 0C                     cmp byte ptr [r13 + 0xc], r11b
00A5D281  74 25                           je 0x140a5d2a8
00A5D283  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00A5D287  48 8B CE                        mov rcx, rsi
00A5D28A  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00A5D28E  E8 51 09 03 00                  call 0x140a8dbe4
00A5D293  45 33 DB                        xor r11d, r11d
00A5D296  8B D8                           mov ebx, eax
00A5D298  85 C0                           test eax, eax
00A5D29A  0F 88 B4 06 00 00               js 0x140a5d954
00A5D2A0  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00A5D2A4  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
00A5D2A8  41 B8 FF 00 00 00               mov r8d, 0xff
00A5D2AE  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00A5D2B2  49 8B D5                        mov rdx, r13
00A5D2B5  48 8B CE                        mov rcx, rsi
00A5D2B8  E8 7F DE F8 FF                  call 0x1409eb13c
00A5D2BD  45 33 DB                        xor r11d, r11d
00A5D2C0  85 C0                           test eax, eax
00A5D2C2  79 0A                           jns 0x140a5d2ce
00A5D2C4  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A5D2C9  E9 6E 06 00 00                  jmp 0x140a5d93c
00A5D2CE  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00A5D2D2  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00A5D2D7  48 8B D1                        mov rdx, rcx
00A5D2DA  8B 49 04                        mov ecx, dword ptr [rcx + 4]
00A5D2DD  E8 56 1B FA FF                  call 0x1409fee38
00A5D2E2  45 33 DB                        xor r11d, r11d
00A5D2E5  85 C0                           test eax, eax
00A5D2E7  79 0A                           jns 0x140a5d2f3
00A5D2E9  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A5D2EE  E9 37 06 00 00                  jmp 0x140a5d92a
00A5D2F3  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A5D2F8  48 8D 96 80 00 00 00            lea rdx, [rsi + 0x80]
00A5D2FF  44 8B 74 24 74                  mov r14d, dword ptr [rsp + 0x74]
00A5D304  41 8A CB                        mov cl, r11b
00A5D307  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00A5D30B  44 39 1A                        cmp dword ptr [rdx], r11d
00A5D30E  74 0B                           je 0x140a5d31b
00A5D310  45 0F B7 F6                     movzx r14d, r14w
00A5D314  0F B6 C1                        movzx eax, cl
00A5D317  41 0F AB C6                     bts r14d, eax
00A5D31B  FE C1                           inc cl
00A5D31D  48 83 C2 20                     add rdx, 0x20
00A5D321  80 F9 10                        cmp cl, 0x10
00A5D324  72 E5                           jb 0x140a5d30b
00A5D326  41 8A DB                        mov bl, r11b
00A5D329  44 89 74 24 74                  mov dword ptr [rsp + 0x74], r14d
00A5D32E  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
00A5D332  4C 89 5D A8                     mov qword ptr [rbp - 0x58], r11
00A5D336  4C 39 9E 90 02 00 00            cmp qword ptr [rsi + 0x290], r11
00A5D33D  75 14                           jne 0x140a5d353
00A5D33F  48 8D 46 10                     lea rax, [rsi + 0x10]
00A5D343  48 8B 08                        mov rcx, qword ptr [rax]
00A5D346  48 3B C8                        cmp rcx, rax
00A5D349  74 08                           je 0x140a5d353
00A5D34B  48 83 C1 F0                     add rcx, -0x10
00A5D34F  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
00A5D353  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00A5D357  48 8B C6                        mov rax, rsi
00A5D35A  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00A5D35E  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
00A5D362  48 8D 50 38                     lea rdx, [rax + 0x38]
00A5D366  48 8B 0A                        mov rcx, qword ptr [rdx]
00A5D369  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
00A5D36D  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00A5D371  48 3B CA                        cmp rcx, rdx
00A5D374  0F 84 88 02 00 00               je 0x140a5d602
00A5D37A  45 85 FF                        test r15d, r15d
00A5D37D  75 05                           jne 0x140a5d384
00A5D37F  4C 8B F9                        mov r15, rcx
00A5D382  EB 7D                           jmp 0x140a5d401
00A5D384  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5D38D  4C 8D 79 F0                     lea r15, [rcx - 0x10]
00A5D391  48 83 CA FF                     or rdx, 0xffffffffffffffff
00A5D395  45 33 C0                        xor r8d, r8d
00A5D398  66 01 90 E4 01 00 00            add word ptr [rax + 0x1e4], dx
00A5D39F  90                              nop
00A5D3A0  48 8B 59 10                     mov rbx, qword ptr [rcx + 0x10]
00A5D3A4  33 D2                           xor edx, edx
00A5D3A6  48 81 C3 98 02 00 00            add rbx, 0x298
00A5D3AD  48 8B CB                        mov rcx, rbx
00A5D3B0  E8 7B 2E 7B FF                  call 0x140210230
00A5D3B5  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00A5D3BB  48 8B F8                        mov rdi, rax
00A5D3BE  73 0E                           jae 0x140a5d3ce
00A5D3C0  4C 8B C3                        mov r8, rbx
00A5D3C3  48 8B D0                        mov rdx, rax
00A5D3C6  48 8B CB                        mov rcx, rbx
00A5D3C9  E8 C2 28 7B FF                  call 0x14020fc90
00A5D3CE  48 85 FF                        test rdi, rdi
00A5D3D1  74 04                           je 0x140a5d3d7
00A5D3D3  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00A5D3D7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A5D3E0  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00A5D3E4  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D3E9  8A 5C 24 50                     mov bl, byte ptr [rsp + 0x50]
00A5D3ED  C6 44 24 52 01                  mov byte ptr [rsp + 0x52], 1
00A5D3F2  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00A5D3F6  48 89 88 A0 02 00 00            mov qword ptr [rax + 0x2a0], rcx
00A5D3FD  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00A5D401  48 8B 09                        mov rcx, qword ptr [rcx]
00A5D404  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00A5D408  8A 44 24 51                     mov al, byte ptr [rsp + 0x51]
00A5D40C  4D 8B CD                        mov r9, r13
00A5D40F  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00A5D413  48 8B D7                        mov rdx, rdi
00A5D416  48 8D 45 F0                     lea rax, [rbp - 0x10]
00A5D41A  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00A5D41E  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00A5D422  49 8B CF                        mov rcx, r15
00A5D425  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5D42A  E8 A1 DE F8 FF                  call 0x1409eb2d0
00A5D42F  45 33 DB                        xor r11d, r11d
00A5D432  84 C0                           test al, al
00A5D434  0F 84 4A 01 00 00               je 0x140a5d584
00A5D43A  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00A5D43E  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00A5D442  44 38 5D D2                     cmp byte ptr [rbp - 0x2e], r11b
00A5D446  0F 85 2C 03 00 00               jne 0x140a5d778
00A5D44C  41 83 FC 02                     cmp r12d, 2
00A5D450  0F 84 D8 00 00 00               je 0x140a5d52e
00A5D456  84 DB                           test bl, bl
00A5D458  74 15                           je 0x140a5d46f
00A5D45A  44 39 5C 24 58                  cmp dword ptr [rsp + 0x58], r11d
00A5D45F  75 07                           jne 0x140a5d468
00A5D461  41 0F B7 5F 68                  movzx ebx, word ptr [r15 + 0x68]
00A5D466  EB 1A                           jmp 0x140a5d482
00A5D468  41 0F B7 5F 6A                  movzx ebx, word ptr [r15 + 0x6a]
00A5D46D  EB 13                           jmp 0x140a5d482
00A5D46F  44 39 5C 24 58                  cmp dword ptr [rsp + 0x58], r11d
00A5D474  75 07                           jne 0x140a5d47d
00A5D476  41 0F B7 5F 64                  movzx ebx, word ptr [r15 + 0x64]
00A5D47B  EB 05                           jmp 0x140a5d482
00A5D47D  41 0F B7 5F 66                  movzx ebx, word ptr [r15 + 0x66]
00A5D482  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
00A5D486  48 8B D7                        mov rdx, rdi
00A5D489  44 8A 4C 24 51                  mov r9b, byte ptr [rsp + 0x51]
00A5D48E  49 8B CF                        mov rcx, r15
00A5D491  44 0F B7 44 24 5C               movzx r8d, word ptr [rsp + 0x5c]
00A5D497  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00A5D49C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00A5D4A0  E8 EB 44 E6 FF                  call 0x1408c1990
00A5D4A5  44 0F B7 4C 24 74               movzx r9d, word ptr [rsp + 0x74]
00A5D4AB  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00A5D4B0  0F B7 54 24 5C                  movzx edx, word ptr [rsp + 0x5c]
00A5D4B5  44 0F B7 C3                     movzx r8d, bx
00A5D4B9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A5D4BE  49 8B CF                        mov rcx, r15
00A5D4C1  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
00A5D4C5  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00A5D4CA  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A5D4CE  8A 44 24 51                     mov al, byte ptr [rsp + 0x51]
00A5D4D2  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00A5D4D6  E8 05 37 E6 FF                  call 0x1408c0be0
00A5D4DB  45 33 DB                        xor r11d, r11d
00A5D4DE  84 C0                           test al, al
00A5D4E0  75 19                           jne 0x140a5d4fb
00A5D4E2  4C 39 5C 24 68                  cmp qword ptr [rsp + 0x68], r11
00A5D4E7  0F 85 97 00 00 00               jne 0x140a5d584
00A5D4ED  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00A5D4F1  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A5D4F6  E9 89 00 00 00                  jmp 0x140a5d584
00A5D4FB  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00A5D500  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00A5D504  48 85 C9                        test rcx, rcx
00A5D507  74 1A                           je 0x140a5d523
00A5D509  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00A5D50D  48 8B D9                        mov rbx, rcx
00A5D510  48 3B C8                        cmp rcx, rax
00A5D513  74 13                           je 0x140a5d528
00A5D515  48 8B C8                        mov rcx, rax
00A5D518  E8 3F 27 E6 FF                  call 0x1408bfc5c
00A5D51D  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00A5D521  EB 05                           jmp 0x140a5d528
00A5D523  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A5D528  41 83 FC 01                     cmp r12d, 1
00A5D52C  75 38                           jne 0x140a5d566
00A5D52E  41 0F B7 4F 62                  movzx ecx, word ptr [r15 + 0x62]
00A5D533  F6 C1 08                        test cl, 8
00A5D536  75 18                           jne 0x140a5d550
00A5D538  F6 C1 10                        test cl, 0x10
00A5D53B  75 13                           jne 0x140a5d550
00A5D53D  66 0F BA E1 0A                  bt cx, 0xa
00A5D542  72 0C                           jb 0x140a5d550
00A5D544  F7 87 30 03 00 00 00 00 00 02   test dword ptr [rdi + 0x330], 0x2000000
00A5D54E  74 16                           je 0x140a5d566
00A5D550  F6 C1 01                        test cl, 1
00A5D553  0F 84 9D 01 00 00               je 0x140a5d6f6
00A5D559  4D 8B C7                        mov r8, r15
00A5D55C  33 D2                           xor edx, edx
00A5D55E  48 8B CF                        mov rcx, rdi
00A5D561  E8 2E 6A FA FF                  call 0x140a03f94
00A5D566  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
00A5D56A  49 8B CF                        mov rcx, r15
00A5D56D  E8 BE AF E6 FF                  call 0x1408c8530
00A5D572  45 33 DB                        xor r11d, r11d
00A5D575  85 C0                           test eax, eax
00A5D577  78 0B                           js 0x140a5d584
00A5D579  41 F6 47 62 02                  test byte ptr [r15 + 0x62], 2
00A5D57E  74 04                           je 0x140a5d584
00A5D580  FF 44 24 78                     inc dword ptr [rsp + 0x78]
00A5D584  44 38 5C 24 52                  cmp byte ptr [rsp + 0x52], r11b
00A5D589  74 5C                           je 0x140a5d5e7
00A5D58B  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00A5D58F  4C 89 98 A0 02 00 00            mov qword ptr [rax + 0x2a0], r11
00A5D596  49 8B 5F 20                     mov rbx, qword ptr [r15 + 0x20]
00A5D59A  48 81 C3 98 02 00 00            add rbx, 0x298
00A5D5A1  0F 0D 0B                        prefetchw byte ptr [rbx]
00A5D5A4  48 8B 03                        mov rax, qword ptr [rbx]
00A5D5A7  48 8B C8                        mov rcx, rax
00A5D5AA  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00A5D5AE  48 83 F9 10                     cmp rcx, 0x10
00A5D5B2  48 8D 50 F0                     lea rdx, [rax - 0x10]
00A5D5B6  49 0F 46 D3                     cmovbe rdx, r11
00A5D5BA  A8 02                           test al, 2
00A5D5BC  75 07                           jne 0x140a5d5c5
00A5D5BE  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
00A5D5C3  74 08                           je 0x140a5d5cd
00A5D5C5  48 8B CB                        mov rcx, rbx
00A5D5C8  E8 03 63 80 FF                  call 0x1402638d0
00A5D5CD  48 8B CB                        mov rcx, rbx
00A5D5D0  E8 2B 40 88 FF                  call 0x1402e1600
00A5D5D5  E8 D6 02 80 FF                  call 0x14025d8b0
00A5D5DA  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D5DF  45 33 DB                        xor r11d, r11d
00A5D5E2  44 88 5C 24 52                  mov byte ptr [rsp + 0x52], r11b
00A5D5E7  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00A5D5EB  8A 5C 24 50                     mov bl, byte ptr [rsp + 0x50]
00A5D5EF  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00A5D5F4  48 3B 4D E0                     cmp rcx, qword ptr [rbp - 0x20]
00A5D5F8  0F 85 7C FD FF FF               jne 0x140a5d37a
00A5D5FE  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00A5D602  48 3B C6                        cmp rax, rsi
00A5D605  74 4F                           je 0x140a5d656
00A5D607  4C 89 98 A0 02 00 00            mov qword ptr [rax + 0x2a0], r11
00A5D60E  48 8D 98 98 02 00 00            lea rbx, [rax + 0x298]
00A5D615  0F 0D 0B                        prefetchw byte ptr [rbx]
00A5D618  48 8B 03                        mov rax, qword ptr [rbx]
00A5D61B  48 8B C8                        mov rcx, rax
00A5D61E  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00A5D622  48 83 F9 10                     cmp rcx, 0x10
00A5D626  48 8D 50 F0                     lea rdx, [rax - 0x10]
00A5D62A  49 0F 46 D3                     cmovbe rdx, r11
00A5D62E  A8 02                           test al, 2
00A5D630  75 07                           jne 0x140a5d639
00A5D632  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
00A5D637  74 08                           je 0x140a5d641
00A5D639  48 8B CB                        mov rcx, rbx
00A5D63C  E8 8F 62 80 FF                  call 0x1402638d0
00A5D641  48 8B CB                        mov rcx, rbx
00A5D644  E8 B7 3F 88 FF                  call 0x1402e1600
00A5D649  E8 62 02 80 FF                  call 0x14025d8b0
00A5D64E  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D653  45 33 DB                        xor r11d, r11d
00A5D656  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00A5D65A  4D 85 FF                        test r15, r15
00A5D65D  0F 84 0D 02 00 00               je 0x140a5d870
00A5D663  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5D66C  49 8D 9F 98 02 00 00            lea rbx, [r15 + 0x298]
00A5D673  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A5D677  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
00A5D67C  45 33 C0                        xor r8d, r8d
00A5D67F  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
00A5D683  33 D2                           xor edx, edx
00A5D685  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
00A5D68C  48 8B CB                        mov rcx, rbx
00A5D68F  90                              nop
00A5D690  E8 9B 2B 7B FF                  call 0x140210230
00A5D695  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00A5D69B  48 8B F8                        mov rdi, rax
00A5D69E  73 0E                           jae 0x140a5d6ae
00A5D6A0  4C 8B C3                        mov r8, rbx
00A5D6A3  48 8B D0                        mov rdx, rax
00A5D6A6  48 8B CB                        mov rcx, rbx
00A5D6A9  E8 E2 25 7B FF                  call 0x14020fc90
00A5D6AE  45 33 DB                        xor r11d, r11d
00A5D6B1  48 85 FF                        test rdi, rdi
00A5D6B4  74 04                           je 0x140a5d6ba
00A5D6B6  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00A5D6BA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5D6C3  49 8B D3                        mov rdx, r11
00A5D6C6  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D6CB  8A 5C 24 50                     mov bl, byte ptr [rsp + 0x50]
00A5D6CF  49 89 87 A0 02 00 00            mov qword ptr [r15 + 0x2a0], rax
00A5D6D6  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
00A5D6DA  48 83 C0 F0                     add rax, -0x10
00A5D6DE  48 3B C6                        cmp rax, rsi
00A5D6E1  48 0F 45 D0                     cmovne rdx, rax
00A5D6E5  49 8B C7                        mov rax, r15
00A5D6E8  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00A5D6ED  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
00A5D6F1  E9 6C FC FF FF                  jmp 0x140a5d362
00A5D6F6  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
00A5D6FA  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00A5D701  E8 1A 8F 7B FF                  call 0x140216620
00A5D706  84 C0                           test al, al
00A5D708  0F 84 58 FE FF FF               je 0x140a5d566
00A5D70E  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
00A5D712  0F 57 C0                        xorps xmm0, xmm0
00A5D715  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
00A5D719  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
00A5D71D  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
00A5D724  E8 B7 E7 9E FF                  call 0x14044bee0
00A5D729  48 8B C8                        mov rcx, rax
00A5D72C  E8 8F 51 9E FF                  call 0x1404428c0
00A5D731  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
00A5D735  4C 8D 45 60                     lea r8, [rbp + 0x60]
00A5D739  33 D2                           xor edx, edx
00A5D73B  48 8B D8                        mov rbx, rax
00A5D73E  E8 DD 90 7B FF                  call 0x140216820
00A5D743  4D 8B C7                        mov r8, r15
00A5D746  B2 01                           mov dl, 1
00A5D748  48 8B CF                        mov rcx, rdi
00A5D74B  E8 44 68 FA FF                  call 0x140a03f94
00A5D750  33 D2                           xor edx, edx
00A5D752  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00A5D756  E8 D5 A5 7B FF                  call 0x140217d30
00A5D75B  48 8B CB                        mov rcx, rbx
00A5D75E  E8 5D C3 9E FF                  call 0x140449ac0
00A5D763  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
00A5D767  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00A5D76E  E8 0D C7 8E FF                  call 0x140349e80
00A5D773  E9 EE FD FF FF                  jmp 0x140a5d566
00A5D778  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
00A5D77C  E8 8F 01 9E FF                  call 0x14043d910
00A5D781  41 0F B7 55 4E                  movzx edx, word ptr [r13 + 0x4e]
00A5D786  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00A5D78B  B9 FF 7F 00 00                  mov ecx, 0x7fff
00A5D790  66 23 D1                        and dx, cx
00A5D793  8B C8                           mov ecx, eax
00A5D795  E8 82 03 07 00                  call 0x140acdb1c
00A5D79A  45 33 DB                        xor r11d, r11d
00A5D79D  85 C0                           test eax, eax
00A5D79F  0F 85 DF FD FF FF               jne 0x140a5d584
00A5D7A5  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A5D7AA  0F B7 5C 24 70                  movzx ebx, word ptr [rsp + 0x70]
00A5D7AF  66 3B 58 4E                     cmp bx, word ptr [rax + 0x4e]
00A5D7B3  74 41                           je 0x140a5d7f6
00A5D7B5  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00A5D7B9  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00A5D7BE  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00A5D7C2  8B 48 04                        mov ecx, dword ptr [rax + 4]
00A5D7C5  E8 6E 16 FA FF                  call 0x1409fee38
00A5D7CA  45 33 DB                        xor r11d, r11d
00A5D7CD  85 C0                           test eax, eax
00A5D7CF  78 2F                           js 0x140a5d800
00A5D7D1  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00A5D7D5  E8 82 24 E6 FF                  call 0x1408bfc5c
00A5D7DA  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00A5D7DF  BA 00 80 00 00                  mov edx, 0x8000
00A5D7E4  0F B7 C3                        movzx eax, bx
00A5D7E7  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
00A5D7EB  66 0B C2                        or ax, dx
00A5D7EE  66 89 41 4E                     mov word ptr [rcx + 0x4e], ax
00A5D7F2  66 89 59 68                     mov word ptr [rcx + 0x68], bx
00A5D7F6  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00A5D7FB  E9 6A FD FF FF                  jmp 0x140a5d56a
00A5D800  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00A5D804  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A5D809  44 38 5C 24 52                  cmp byte ptr [rsp + 0x52], r11b
00A5D80E  0F 84 D5 FA FF FF               je 0x140a5d2e9
00A5D814  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00A5D818  4C 89 98 A0 02 00 00            mov qword ptr [rax + 0x2a0], r11
00A5D81F  49 8B 5F 20                     mov rbx, qword ptr [r15 + 0x20]
00A5D823  48 81 C3 98 02 00 00            add rbx, 0x298
00A5D82A  0F 0D 0B                        prefetchw byte ptr [rbx]
00A5D82D  48 8B 03                        mov rax, qword ptr [rbx]
00A5D830  48 8B C8                        mov rcx, rax
00A5D833  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00A5D837  48 83 F9 10                     cmp rcx, 0x10
00A5D83B  48 8D 50 F0                     lea rdx, [rax - 0x10]
00A5D83F  49 0F 46 D3                     cmovbe rdx, r11
00A5D843  A8 02                           test al, 2
00A5D845  75 07                           jne 0x140a5d84e
00A5D847  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
00A5D84C  74 08                           je 0x140a5d856
00A5D84E  48 8B CB                        mov rcx, rbx
00A5D851  E8 7A 60 80 FF                  call 0x1402638d0
00A5D856  48 8B CB                        mov rcx, rbx
00A5D859  E8 A2 3D 88 FF                  call 0x1402e1600
00A5D85E  E8 4D 00 80 FF                  call 0x14025d8b0
00A5D863  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D868  45 33 DB                        xor r11d, r11d
00A5D86B  E9 79 FA FF FF                  jmp 0x140a5d2e9
00A5D870  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00A5D874  41 8B DB                        mov ebx, r11d
00A5D877  41 89 45 14                     mov dword ptr [r13 + 0x14], eax
00A5D87B  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00A5D87F  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
00A5D883  48 85 FF                        test rdi, rdi
00A5D886  0F 84 9E 00 00 00               je 0x140a5d92a
00A5D88C  41 83 FC 01                     cmp r12d, 1
00A5D890  0F 87 94 00 00 00               ja 0x140a5d92a
00A5D896  48 8B 0D A3 1F 4A 00            mov rcx, qword ptr [rip + 0x4a1fa3]
00A5D89D  48 8D 05 CC 36 5C FF            lea rax, [rip - 0xa3c934]
00A5D8A4  4C 8D 3D 25 3B 5C FF            lea r15, [rip - 0xa3c4db]
00A5D8AB  4C 0F 45 F8                     cmovne r15, rax
00A5D8AF  49 8B D7                        mov rdx, r15
00A5D8B2  E8 99 4B 93 FF                  call 0x140392450
00A5D8B7  45 33 DB                        xor r11d, r11d
00A5D8BA  84 C0                           test al, al
00A5D8BC  74 6C                           je 0x140a5d92a
00A5D8BE  49 8B D7                        mov rdx, r15
00A5D8C1  41 83 FC 01                     cmp r12d, 1
00A5D8C5  75 3C                           jne 0x140a5d903
00A5D8C7  41 8A 45 4C                     mov al, byte ptr [r13 + 0x4c]
00A5D8CB  4C 8D 8F 88 00 00 00            lea r9, [rdi + 0x88]
00A5D8D2  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A5D8D6  41 8B 45 50                     mov eax, dword ptr [r13 + 0x50]
00A5D8DA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A5D8DE  49 8B 45 60                     mov rax, qword ptr [r13 + 0x60]
00A5D8E2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A5D8E7  49 8B 45 58                     mov rax, qword ptr [r13 + 0x58]
00A5D8EB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A5D8F0  49 8D 45 28                     lea rax, [r13 + 0x28]
00A5D8F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5D8F9  E8 76 84 02 00                  call 0x140a85d74
00A5D8FE  45 33 DB                        xor r11d, r11d
00A5D901  EB 27                           jmp 0x140a5d92a
00A5D903  49 8D 4D 28                     lea rcx, [r13 + 0x28]
00A5D907  41 B9 02 00 00 00               mov r9d, 2
00A5D90D  48 8D 87 88 00 00 00            lea rax, [rdi + 0x88]
00A5D914  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A5D919  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5D91E  E8 F5 63 E0 FF                  call 0x140863d18
00A5D923  EB D9                           jmp 0x140a5d8fe
00A5D925  BB 22 00 00 C0                  mov ebx, 0xc0000022
00A5D92A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00A5D92F  48 85 C9                        test rcx, rcx
00A5D932  74 08                           je 0x140a5d93c
00A5D934  E8 23 23 E6 FF                  call 0x1408bfc5c
00A5D939  45 33 DB                        xor r11d, r11d
00A5D93C  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00A5D940  48 85 C9                        test rcx, rcx
00A5D943  74 08                           je 0x140a5d94d
00A5D945  E8 12 23 E6 FF                  call 0x1408bfc5c
00A5D94A  45 33 DB                        xor r11d, r11d
00A5D94D  44 38 5C 24 54                  cmp byte ptr [rsp + 0x54], r11b
00A5D952  74 4C                           je 0x140a5d9a0
00A5D954  4C 89 9E A0 02 00 00            mov qword ptr [rsi + 0x2a0], r11
00A5D95B  48 8D BE 98 02 00 00            lea rdi, [rsi + 0x298]
00A5D962  0F 0D 0F                        prefetchw byte ptr [rdi]
00A5D965  48 8B 07                        mov rax, qword ptr [rdi]
00A5D968  48 8B C8                        mov rcx, rax
00A5D96B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00A5D96F  48 83 F9 10                     cmp rcx, 0x10
00A5D973  48 8D 50 F0                     lea rdx, [rax - 0x10]
00A5D977  49 0F 46 D3                     cmovbe rdx, r11
00A5D97B  A8 02                           test al, 2
00A5D97D  75 07                           jne 0x140a5d986
00A5D97F  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
00A5D984  74 08                           je 0x140a5d98e
00A5D986  48 8B CF                        mov rcx, rdi
00A5D989  E8 42 5F 80 FF                  call 0x1402638d0
00A5D98E  48 8B CF                        mov rcx, rdi
00A5D991  E8 6A 3C 88 FF                  call 0x1402e1600
00A5D996  E8 15 FF 7F FF                  call 0x14025d8b0
00A5D99B  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A5D9A0  48 85 FF                        test rdi, rdi
00A5D9A3  74 0A                           je 0x140a5d9af
00A5D9A5  33 D2                           xor edx, edx
00A5D9A7  48 8B CF                        mov rcx, rdi
00A5D9AA  E8 B1 67 FA FF                  call 0x140a04160
00A5D9AF  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00A5D9B3  48 85 C9                        test rcx, rcx
00A5D9B6  74 05                           je 0x140a5d9bd
00A5D9B8  E8 93 B9 89 FF                  call 0x1402f9350
00A5D9BD  48 85 F6                        test rsi, rsi
00A5D9C0  74 08                           je 0x140a5d9ca
00A5D9C2  48 8B CE                        mov rcx, rsi
00A5D9C5  E8 56 59 E6 FF                  call 0x1408c3320
00A5D9CA  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00A5D9CE  E8 51 B0 E6 FF                  call 0x1408c8a24
00A5D9D3  8B C3                           mov eax, ebx
00A5D9D5  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
00A5D9DC  48 33 CC                        xor rcx, rsp
00A5D9DF  E8 5C EC C4 FF                  call 0x1406ac640
00A5D9E4  48 8B 9C 24 10 02 00 00         mov rbx, qword ptr [rsp + 0x210]
00A5D9EC  48 81 C4 C0 01 00 00            add rsp, 0x1c0
00A5D9F3  41 5F                           pop r15
00A5D9F5  41 5E                           pop r14
00A5D9F7  41 5D                           pop r13
00A5D9F9  41 5C                           pop r12
00A5D9FB  5F                              pop rdi
00A5D9FC  5E                              pop rsi
00A5D9FD  5D                              pop rbp
00A5D9FE  C3                              ret
00A5D9FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEnableGuid(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int8 v_stack_m126;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int16 v_stack_m184;
    unsigned __int16 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int16 v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int8 v_stack_m1A4;
    unsigned __int8 v_stack_m1A5;
    unsigned __int8 v_stack_m1A6;
    unsigned __int8 v_stack_m1A7;
    unsigned __int8 v_stack_m1A8;
    unsigned __int8 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 3856882)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_stack_m160 = a1;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    v_stack_m168 = 0;
    v_stack_m180 = 0;
    result = 0;
    v_stack_m1A4 = 0;
    v_stack_m1A6 = 0;
    v_stack_m128 = 0;
    a2 = 0;
    v_stack_m184 = 0;
    v_stack_m19C = 0;
    v_stack_m1A5 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m198 = 0;
    v_stack_m190 = 0;
    result = memset(v_stack_m108, a2, v_r12 + 104, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 72 + 8))) & (32));
    v_stack_m188 = 0;
    v_stack_m1A0 = (unsigned int)(result);
    result = (unsigned int)(-(result));
    result = (unsigned __int8)((result) & (2));
    v_stack_m1A7 = (unsigned __int8)(result);
    v_stack_m1D0 = v_stack_m108;
    v_stack_m1D8 = v_stack_m198;
    result = EtwpValidateEnableNotification(a1, 0, a3, v_stack_m138);
    v_r11 = 0;
    if (sign_flag) goto loc_00A5D99B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 2) goto loc_00A5CE40;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4860450), v_rip - 10749509, a3, v_stack_m138);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) {
        a3 = a2 + 40;
        a2 = a2 + 72;
        result = EtwpEventWriteCaptureState(*(unsigned __int64 *)(v_rip + 4860450), a2, a3, v_stack_m138);
        v_r11 = 0;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 116)) - 1)) > 1) goto loc_00A5CE94;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 116))) == 0) goto loc_00A5CE9E;
    a4 = (v_stack_m64) - (a2 + 120);
    a3 = (v_stack_m68) - (a2 + 120);
loc_00A5CE6F:
    a1 = (*(unsigned __int64 *)(a2 + 120 + 8 - 8)) + (a2);
    *(unsigned int *)(a4 + a2 + 120 + 8 * 1) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 120 + 8 + 4)));
    *(unsigned __int64 *)(a3 + a2 + 120 + 8 * 1 - 8) = a1;
    *(unsigned int *)(a3 + a2 + 120 + 8 * 1) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 120 + 8)));
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 116))))) - (1);
    if (condition_is_not_equal) goto loc_00A5CE6F;
    goto loc_00A5CE9E;
loc_00A5CE94:
    v_stack_m5C = 0;
loc_00A5CE9E:
    a1 = (a1) | (-1);
    if (v_stack_m1A0 != 0) goto loc_00A5CF9F;
    v_stack_m1C0 = v_stack_m1A5;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = v_stack_m68;
    v_stack_m1D8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72 + 16)));
    result = EtwpEnableDisableSpecialGuids(a1, a2 + 40, *(unsigned __int16 *)(a2 + 72 + 6), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))));
    result = KeLeaveCriticalRegion(a1, a2 + 40, *(unsigned __int16 *)(a2 + 72 + 6), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))));
    v_r11 = 0;
    if (v_stack_m1A5 != 0) goto loc_00A5D99B;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m68;
    result = EtwpEnableMetaProviderGuid(v_stack_m198, a2 + 40, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))), *(unsigned __int64 *)(a2 + 72 + 16));
    if (((unsigned int)(result)) != 0xC0000295ULL) goto loc_00A5D9A0;
    v_r11 = 0;
loc_00A5CF41:
    if (((*(unsigned __int16 *)(a2 + 72 + 6)) & ((unsigned __int16)((unsigned int)(0xFFFDULL)))) == 0) goto loc_00A5D925;
    result = PsGetCurrentProcessId((unsigned int)(0xFFFDULL), a2 + 40, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))), *(unsigned __int64 *)(a2 + 72 + 16));
    *(unsigned int *)(a2 + 36) = (unsigned int)(result);
    a2 = v_rip - 10796001;
    if ((unsigned __int8)(v_stack_m126) == 0) { a2 = a2 + 40; }
    result = EtwpFindGuidEntryByGuid(v_stack_m160, a2, (unsigned int)((unsigned int)(v_stack_m1A7)), *(unsigned __int64 *)(a2 + 72 + 16));
    v_r11 = 0;
    if (result != 0) goto loc_00A5CFD2;
    if ((unsigned __int8)(v_stack_m126) == 0) goto loc_00A5CFA6;
loc_00A5CF92:
    goto loc_00A5D9A0;
loc_00A5CF9F:
    goto loc_00A5CF41;
loc_00A5CFA6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) goto loc_00A5CF92;
    result = EtwpAddGuidEntry(v_stack_m160, a2 + 40, (unsigned int)((unsigned int)(v_stack_m1A7)), *(unsigned __int64 *)(a2 + 72 + 16));
    if (result != 0) goto loc_00A5D09C;
    goto loc_00A5D9A0;
loc_00A5CFD2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) == 1) goto loc_00A5CFE4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72))) != 0) goto loc_00A5D09C;
loc_00A5CFE4:
    if (v_stack_m198 == 0) goto loc_00A5D09C;
    if ((*(unsigned __int64 *)(v_rip - 10788775)) != (*(unsigned __int64 *)(a2 + 40))) goto loc_00A5D09C;
    if ((*(unsigned __int64 *)(v_rip - 10788784)) != (*(unsigned __int64 *)(a2 + 48))) goto loc_00A5D09C;
    v_r15 = v_rip - 10732235;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) { v_r15 = v_rip - 10730736; }
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4859943), v_r15, (unsigned int)((unsigned int)(v_stack_m1A7)), *(unsigned __int64 *)(a2 + 72 + 16));
    if ((unsigned __int8)(result) == 0) goto loc_00A5D09C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) goto loc_00A5D080;
    v_stack_m1B8 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 72 + 4));
    v_stack_m1C0 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72 + 8)));
    v_stack_m1C8 = *(unsigned __int64 *)(a2 + 72 + 24);
    v_stack_m1D0 = *(unsigned __int64 *)(a2 + 72 + 16);
    v_stack_m1D8 = v_rip - 10788850;
    result = EtwpEventWriteProviderEnabled(v_rip - 10788850, v_r15, (unsigned int)((unsigned int)(v_stack_m1A7)), v_stack_m198 + 136);
    goto loc_00A5D09C;
loc_00A5D080:
    v_stack_m1D0 = v_rip - 10788850;
    v_stack_m1D8 = v_stack_m198 + 136;
    result = EtwpEventWriteTemplateSessAndProv(v_rip - 10788850, v_r15, (unsigned int)((unsigned int)(v_stack_m1A7)), 2);
loc_00A5D09C:
    a1 = (v_rip - 10788850) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire((unsigned int)(0xC0000017ULL) + 664, a2, a3, 2);
    if (!(condition_is_above_or_equal)) {
        a3 = (unsigned int)(0xC0000017ULL) + 664;
        a2 = result;
        a1 = (unsigned int)(0xC0000017ULL) + 664;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 2);
    }
    v_r11 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1A4 = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) goto loc_00A5D144;
    if (((*(unsigned __int8 *)((unsigned int)(0xC0000017ULL) + 91)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 72))))) == 0) goto loc_00A5D144;
    if ((unsigned int)((unsigned int)(v_stack_m1A0)) != 0) goto loc_00A5D144;
    if ((*(unsigned __int16 *)(a2 + 72 + 6)) == ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC0000017ULL) + 88)))) goto loc_00A5D144;
    if ((*(unsigned __int64 *)(v_rip - 10758799)) != (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 40))) goto loc_00A5D144;
    if ((*(unsigned __int64 *)(v_rip - 10758804)) != (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 48))) goto loc_00A5D144;
    goto loc_00A5D954;
loc_00A5D144:
    if (v_stack_m198 == 0) goto loc_00A5D162;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m198 + 816)))) & (64)) == 0) goto loc_00A5D162;
    goto loc_00A5D954;
loc_00A5D162:
    if ((unsigned int)((unsigned int)(v_stack_m1A0)) == 0) goto loc_00A5D17C;
    result = EtwpAcquireTokenAccessInformation(v_stack_m198, a2, a3, 2);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00A5D954;
loc_00A5D17C:
    *(unsigned int *)(a2 + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)));
    *(unsigned __int16 *)(a2 + 104) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 72 + 6));
    *(unsigned __int8 *)(a2 + 106) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 72 + 4));
    *(unsigned int *)(a2 + 108) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72 + 16)));
    if ((unsigned __int8)(v_stack_m126) != 0) {
        a1 = (unsigned __int16)((*(unsigned __int16 *)(a2 + 72 + 6)) & ((unsigned __int16)((unsigned int)(0x7FFFULL))));
        *(unsigned __int8 *)(a2 + 107) = 1;
        *(unsigned __int16 *)(a2 + 104) = (unsigned __int16)(a1);
    }
    if ((*(unsigned __int64 *)(a2 + 72 + 16)) == 0) {
        a1 = (a1) | (-1);
        *(unsigned __int64 *)(a2 + 72 + 16) = a1;
    }
    if ((*(unsigned __int8 *)(a2 + 72 + 4)) == 0) {
        *(unsigned __int8 *)(a2 + 72 + 4) = 255;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) == 2) goto loc_00A5D25A;
    if ((unsigned __int8)(v_stack_m126) != 0) goto loc_00A5D25A;
    v_stack_m1D8 = v_stack_m19C;
    result = EtwpUpdateGuidEnableInfo((unsigned int)(0xC0000017ULL), a2, *(unsigned __int64 *)(a2 + 72 + 16), v_stack_m108);
    v_r11 = 0;
    if (sign_flag) goto loc_00A5D954;
    *(unsigned __int64 *)(a2 + 72) = v_xmm0;
    *(unsigned __int64 *)(a2 + 72 + 16) = v_xmm1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 72 + 8)))) & (4)) == 0) goto loc_00A5D25A;
    result = EtwpPreallocateApcPool(v_stack_m198 + 832, a2, *(unsigned __int64 *)(a2 + 72 + 16), v_stack_m108);
loc_00A5D23B:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m198 + 816))))) | ((unsigned int)((unsigned int)(0x2000ULL))));
    if (condition_is_not_equal) goto loc_00A5D23B;
    result = (unsigned int)(*(unsigned int *)(v_stack_m198 + 816));
    if ((((unsigned int)((unsigned int)(0x2000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m198 + 816))))) == 0) {
        result = EtwpReferenceStackLookasideList(a1, (unsigned int)(0x2000ULL), *(unsigned __int64 *)(a2 + 72 + 16), v_stack_m108);
    }
    v_r11 = 0;
loc_00A5D25A:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56)) != ((unsigned int)(0xC0000017ULL) + 56)) goto loc_00A5D27D;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 656)) != 0) goto loc_00A5D275;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 16)) != ((unsigned int)(0xC0000017ULL) + 16)) goto loc_00A5D27D;
loc_00A5D275:
    goto loc_00A5D954;
loc_00A5D27D:
    if ((*(unsigned __int8 *)(a2 + 12)) == 0) goto loc_00A5D2A8;
    result = EtwpCreateUmReplyObject((unsigned int)(0xC0000017ULL), v_stack_m140, v_stack_m148, v_stack_m108);
    v_r11 = 0;
    if (sign_flag) goto loc_00A5D954;
    *(unsigned __int64 *)(a2 + 24) = v_stack_m148;
loc_00A5D2A8:
    result = EtwpBuildNotificationPacket((unsigned int)(0xC0000017ULL), a2, 255, v_stack_m168);
    v_r11 = 0;
    if (!sign_flag) goto loc_00A5D2CE;
    goto loc_00A5D93C;
loc_00A5D2CE:
    result = EtwpAllocDataBlock((unsigned int)(*(unsigned int *)(v_stack_m168 + 4)), v_stack_m168, v_stack_m190, v_stack_m168);
    v_r11 = 0;
    if (!sign_flag) goto loc_00A5D2F3;
loc_00A5D2E9:
    goto loc_00A5D92A;
loc_00A5D2F3:
    v_stack_m178 = v_stack_m190;
loc_00A5D30B:
    result = v_stack_m190;
    v_r14 = (unsigned int)(v_stack_m184);
    if ((*(unsigned int *)((unsigned int)(0xC0000017ULL) + 128)) != 0) {
        v_r14 = (unsigned __int16)((unsigned int)(v_stack_m184));
        result = 0;
    }
    a1 = (unsigned __int8)((0) + 1);
    a2 = ((unsigned int)(0xC0000017ULL) + 128) + (32);
    if (((unsigned __int8)(a1)) < 16) goto loc_00A5D30B;
    v_stack_m184 = (unsigned int)(v_r14);
    v_stack_m1A8 = 0;
    v_stack_m150 = 0;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 656)) != 0) goto loc_00A5D353;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 16)) != ((unsigned int)(0xC0000017ULL) + 16)) {
        a1 = (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 16)) + (-16);
        v_stack_m150 = a1;
    }
    v_stack_m160 = (unsigned int)(0xC0000017ULL);
    v_stack_m120 = v_stack_m168;
loc_00A5D362:
    v_stack_m118 = (unsigned int)(0xC0000017ULL) + 56;
    v_stack_m158 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56);
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56)) == ((unsigned int)(0xC0000017ULL) + 56)) goto loc_00A5D602;
loc_00A5D37A:
    if ((unsigned int)((unsigned int)(v_stack_m1A0)) != 0) goto loc_00A5D384;
    goto loc_00A5D401;
loc_00A5D384:
    a2 = ((unsigned int)(0xC0000017ULL) + 56) | (-1);
    a3 = 0;
    a2 = 0;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) + 16)) + (664);
    result = KeAbPreAcquire(v_rbx, a2, a3, v_stack_m168);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m168);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m1A6 = 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 16) + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_00A5D401:
    v_stack_m1C8 = (unsigned __int8)(v_stack_m1A7);
    v_stack_m158 = *(unsigned __int64 *)(v_stack_m158);
    v_stack_m1D0 = (unsigned __int8)(v_stack_m1A8);
    v_stack_m1D8 = v_stack_m108;
    result = EtwpIsRegEntryAllowed(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m198, v_stack_m138, a2);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A5D584;
    v_stack_m170 = v_stack_m168;
    if (v_stack_m126 != 0) goto loc_00A5D778;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) == 2) goto loc_00A5D52E;
    if ((unsigned __int8)(v_stack_m1A8) == 0) goto loc_00A5D46F;
    if (v_stack_m1A0 != 0) goto loc_00A5D468;
    goto loc_00A5D482;
loc_00A5D468:
    goto loc_00A5D482;
loc_00A5D46F:
    if (v_stack_m1A0 != 0) goto loc_00A5D47D;
    goto loc_00A5D482;
loc_00A5D47D:
loc_00A5D482:
    v_stack_m1D0 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)));
    v_stack_m1D8 = (unsigned __int8)(v_stack_m1A8);
    result = EtwpUpdateRegEntryEnableMask(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m198, v_stack_m19C, v_stack_m1A7);
    v_stack_m1C0 = v_stack_m190;
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)));
    v_stack_m1D0 = (unsigned __int8)(v_stack_m1A8);
    v_stack_m1D8 = (unsigned __int8)(v_stack_m1A7);
    result = EtwpCalculateUpdateNotification(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m19C, (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 102)), v_stack_m184);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A5D4FB;
    if (v_stack_m190 != 0) goto loc_00A5D584;
    v_stack_m190 = v_stack_m178;
    goto loc_00A5D584;
loc_00A5D4FB:
    if (v_stack_m190 == 0) goto loc_00A5D523;
    v_stack_m170 = v_stack_m190;
    if (v_stack_m190 == v_stack_m178) goto loc_00A5D528;
    result = EtwpUnreferenceDataBlock(v_stack_m178, v_stack_m19C, (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 102)), v_stack_m184);
    v_stack_m178 = v_stack_m190;
    goto loc_00A5D528;
loc_00A5D523:
    v_stack_m190 = result;
loc_00A5D528:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) goto loc_00A5D566;
loc_00A5D52E:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 98))) & (8)) != 0) goto loc_00A5D550;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 98))) & (16)) != 0) goto loc_00A5D550;
    if (condition_is_below) goto loc_00A5D550;
    if (((*(unsigned int *)(v_stack_m198 + 816)) & (0x2000000ULL)) == 0) goto loc_00A5D566;
loc_00A5D550:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 98))) & (1)) == 0) goto loc_00A5D6F6;
    a2 = 0;
    result = EtwpProviderArrivalCallback(v_stack_m198, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
loc_00A5D566:
loc_00A5D56A:
    result = EtwpSendDataBlock(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m170, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    v_r11 = 0;
    if (sign_flag) goto loc_00A5D584;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 98)) & (2)) != 0) {
    }
    if (v_stack_m1A6 == 0) goto loc_00A5D5E7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 32) + 672) = 0;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16 + 32)) + (664);
    a1 = (*(unsigned __int64 *)(v_rbx)) & (-16);
    a2 = *(unsigned __int64 *)(v_rbx) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_00A5D5C5;
    result = *(unsigned __int64 *)(v_rbx);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) {
        a1 = v_rbx;
        result = ExfReleasePushLock(a1, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    }
    result = KeAbPostRelease(v_rbx, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    result = KeLeaveCriticalRegion(v_rbx, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    v_r11 = 0;
    v_stack_m1A6 = 0;
loc_00A5D5E7:
    if (v_stack_m158 != v_stack_m118) goto loc_00A5D37A;
loc_00A5D602:
    if (v_stack_m160 == ((unsigned int)(0xC0000017ULL))) goto loc_00A5D656;
    *(unsigned __int64 *)(v_stack_m160 + 672) = 0;
    a1 = (*(unsigned __int64 *)(v_stack_m160 + 664)) & (-16);
    a2 = *(unsigned __int64 *)(v_stack_m160 + 664) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m160 + 664))) & (2)) != 0) goto loc_00A5D639;
    result = *(unsigned __int64 *)(v_stack_m160 + 664);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m160 + 664))) & (2)) != 0) {
        a1 = v_stack_m160 + 664;
        result = ExfReleasePushLock(a1, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    }
    result = KeAbPostRelease(v_stack_m160 + 664, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    result = KeLeaveCriticalRegion(v_stack_m160 + 664, a2, *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 56) - 16, v_stack_m184);
    v_r11 = 0;
loc_00A5D656:
    if (v_stack_m150 == 0) goto loc_00A5D870;
    a1 = (v_stack_m160 + 664) | (-1);
    v_stack_m1A8 = 1;
    a3 = 0;
    v_stack_m160 = v_stack_m150;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m150 + 664, a2, a3, v_stack_m184);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_m150 + 664;
        a2 = result;
        a1 = v_stack_m150 + 664;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m184);
    }
    v_r11 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_stack_m150 + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (*(unsigned __int64 *)(v_stack_m150 + 16)) + (-16);
    a2 = 0;
    if (result != ((unsigned int)(0xC0000017ULL))) { a2 = result; }
    v_stack_m150 = a2;
    goto loc_00A5D362;
loc_00A5D6F6:
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 80)) + (488);
    result = ExAcquireRundownProtection(a1, a2, a3, v_stack_m184);
    if ((unsigned __int8)(result) == 0) goto loc_00A5D566;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    result = PsGetProcessServerSilo(*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 80), a2, a3, v_stack_m184);
    result = PsAttachSiloToCurrentThread(result, a2, a3, v_stack_m184);
    a2 = 0;
    result = KiStackAttachProcess(*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 80), a2, v_stack_m98, v_stack_m184);
    result = EtwpProviderArrivalCallback(v_stack_m198, 1, (unsigned int)(v_stack_m1A0), v_stack_m184);
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m98, a2, (unsigned int)(v_stack_m1A0), v_stack_m184);
    result = PsDetachSiloFromCurrentThread(result, a2, (unsigned int)(v_stack_m1A0), v_stack_m184);
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 80)) + (488);
    result = ExReleaseRundownProtection(a1, a2, (unsigned int)(v_stack_m1A0), v_stack_m184);
    goto loc_00A5D566;
loc_00A5D778:
    result = PsGetProcessId(*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 80), a2, (unsigned int)(v_stack_m1A0), v_stack_m184);
    a2 = (unsigned __int16)((*(unsigned __int16 *)(a2 + 78)) & ((unsigned __int16)((unsigned int)(0x7FFFULL))));
    result = EtwpDemuxPrivateTraceHandle((unsigned int)((unsigned int)(result)), a2, v_stack_m188, v_stack_m184);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00A5D584;
    if (((unsigned __int16)(v_stack_m188)) == (*(unsigned __int16 *)(v_stack_m190 + 78))) goto loc_00A5D7F6;
    result = EtwpAllocDataBlock((unsigned int)(*(unsigned int *)(v_stack_m120 + 4)), v_stack_m168, v_stack_m190, v_stack_m184);
    v_r11 = 0;
    if (sign_flag) goto loc_00A5D800;
    result = EtwpUnreferenceDataBlock(v_stack_m178, v_stack_m168, v_stack_m190, v_stack_m184);
    v_stack_m178 = v_stack_m190;
    result = (unsigned __int16)(((unsigned __int16)(v_stack_m188)) | ((unsigned __int16)((unsigned int)(0x8000ULL))));
    *(unsigned __int16 *)(v_stack_m190 + 78) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_stack_m190 + 104) = (unsigned __int16)(v_stack_m188);
loc_00A5D7F6:
    goto loc_00A5D56A;
loc_00A5D800:
    v_stack_m190 = v_stack_m178;
    if (v_stack_m1A6 == 0) goto loc_00A5D2E9;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 32) + 672) = 0;
    v_rbx = (*(unsigned __int64 *)((unsigned int)(v_stack_m1A0) + 32)) + (664);
    a1 = (*(unsigned __int64 *)(v_rbx)) & (-16);
    a2 = *(unsigned __int64 *)(v_rbx) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_00A5D84E;
    result = *(unsigned __int64 *)(v_rbx);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) {
        a1 = v_rbx;
        result = ExfReleasePushLock(a1, a2, v_stack_m190, v_stack_m184);
    }
    result = KeAbPostRelease(v_rbx, a2, v_stack_m190, v_stack_m184);
    result = KeLeaveCriticalRegion(v_rbx, a2, v_stack_m190, v_stack_m184);
    v_r11 = 0;
    goto loc_00A5D2E9;
loc_00A5D870:
    *(unsigned int *)(a2 + 20) = (unsigned int)((unsigned int)(v_stack_m180));
    *(unsigned __int64 *)(a2 + 24) = v_stack_m140;
    if (v_stack_m198 == 0) goto loc_00A5D92A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) > 1) goto loc_00A5D92A;
    v_r15 = v_rip - 10732763;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) { v_r15 = v_rip - 10733876; }
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4857763), v_r15, v_stack_m190, v_stack_m184);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A5D92A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) != 1) goto loc_00A5D903;
    v_stack_m1B8 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 76));
    v_stack_m1C0 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)));
    v_stack_m1C8 = *(unsigned __int64 *)(a2 + 96);
    v_stack_m1D0 = *(unsigned __int64 *)(a2 + 88);
    v_stack_m1D8 = a2 + 40;
    result = EtwpEventWriteProviderEnabled(*(unsigned __int64 *)(v_rip + 4857763), v_r15, v_stack_m190, v_stack_m198 + 136);
loc_00A5D8FE:
    v_r11 = 0;
    goto loc_00A5D92A;
loc_00A5D903:
    v_stack_m1D0 = a2 + 40;
    v_stack_m1D8 = v_stack_m198 + 136;
    result = EtwpEventWriteTemplateSessAndProv(a2 + 40, v_r15, v_stack_m190, 2);
    goto loc_00A5D8FE;
loc_00A5D925:
loc_00A5D92A:
    if (v_stack_m190 != 0) {
        result = EtwpUnreferenceDataBlock(v_stack_m190, v_r15, v_stack_m190, 2);
        v_r11 = 0;
    }
    if (v_stack_m168 != 0) {
        result = EtwpUnreferenceDataBlock(v_stack_m168, v_r15, v_stack_m190, 2);
        v_r11 = 0;
    }
    if (v_stack_m1A4 == 0) goto loc_00A5D9A0;
loc_00A5D954:
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 672) = 0;
    a1 = (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 664)) & (-16);
    a2 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 664) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 664))) & (2)) != 0) goto loc_00A5D986;
    result = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 664);
    if ((((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 664))) & (2)) != 0) {
        a1 = (unsigned int)(0xC0000017ULL) + 664;
        result = ExfReleasePushLock(a1, a2, v_stack_m190, 2);
    }
    result = KeAbPostRelease((unsigned int)(0xC0000017ULL) + 664, a2, v_stack_m190, 2);
    result = KeLeaveCriticalRegion((unsigned int)(0xC0000017ULL) + 664, a2, v_stack_m190, 2);
loc_00A5D99B:
loc_00A5D9A0:
    if (v_stack_m198 != 0) {
        a2 = 0;
        a1 = v_stack_m198;
        result = EtwpReleaseLoggerContext(a1, a2, v_stack_m190, 2);
    }
    if (v_stack_m148 != 0) {
        result = ObfDereferenceObject(v_stack_m148, a2, v_stack_m190, 2);
    }
    if ((unsigned int)(0xC0000017ULL) != 0) {
        a1 = (unsigned int)(0xC0000017ULL);
        result = EtwpUnreferenceGuidEntry(a1, a2, v_stack_m190, 2);
    }
    result = EtwpFreeFilterInfo(v_stack_m108, a2, v_stack_m190, 2);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m190, 2);
    v_rsp = (v_rsp) + (448);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEnableGuid(int64_t Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint8_t v_stack_m126;
    uint32_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint16_t v_stack_m184;
    uint16_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint16_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint8_t v_stack_m1A4;
    uint8_t v_stack_m1A5;
    uint8_t v_stack_m1A6;
    uint8_t v_stack_m1A7;
    uint8_t v_stack_m1A8;
    uint8_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m48;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x3AD9F2)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    v_stack_m160 = Arg1;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    v_stack_m168 = 0;
    v_stack_m180 = 0;
    result = 0;
    v_stack_m1A4 = 0;
    v_stack_m1A6 = 0;
    v_stack_m128 = 0;
    Arg2 = 0;
    v_stack_m184 = 0;
    v_stack_m19C = 0;
    v_stack_m1A5 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m198 = 0;
    v_stack_m190 = 0;
    result = memset(v_stack_m108, Arg2, local_r12 + 104, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x48 + 0x8))) & (32));
    v_stack_m188 = 0;
    v_stack_m1A0 = (uint32_t)(result);
    result = (uint32_t)(-(result));
    result = (uint8_t)((result) & (2));
    v_stack_m1A7 = (uint8_t)(result);
    v_stack_m1D0 = v_stack_m108;
    v_stack_m1D8 = v_stack_m198;
    result = EtwpValidateEnableNotification(Arg1, 0, Arg3, v_stack_m138);
    local_r11 = 0;
    if (sign_flag) goto loc_00A5D99B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 2) goto loc_00A5CE40;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4A2A22), v_rip - 10749509, Arg3, v_stack_m138);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) {
        Arg3 = Arg2 + 40;
        Arg2 = Arg2 + 72;
        result = EtwpEventWriteCaptureState(*(uint64_t *)(v_rip + 0x4A2A22), Arg2, Arg3, v_stack_m138);
        local_r11 = 0;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x74)) - 1)) > 1) goto loc_00A5CE94;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x74))) == 0) goto loc_00A5CE9E;
    a4 = (v_stack_m64) - (Arg2 + 120);
    Arg3 = (v_stack_m68) - (Arg2 + 120);
loc_00A5CE6F:
    Arg1 = (*(uint64_t *)(arg2 + 0x78 + 0x8 - 0x8)) + (Arg2);
    *(uint32_t *)(a4 + arg2 + 0x78 + 0x8 * 1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x78 + 0x8 + 0x4)));
    *(uint64_t *)(Arg3 + arg2 + 0x78 + 0x8 * 1 - 0x8) = Arg1;
    *(uint32_t *)(Arg3 + arg2 + 0x78 + 0x8 * 1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x78 + 0x8)));
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x74))))) - (1);
    if (condition_is_not_equal) goto loc_00A5CE6F;
    goto loc_00A5CE9E;
loc_00A5CE94:
    v_stack_m5C = 0;
loc_00A5CE9E:
    Arg1 = (Arg1) | (-1);
    if (v_stack_m1A0 != 0) goto loc_00A5CF9F;
    v_stack_m1C0 = v_stack_m1A5;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = v_stack_m68;
    v_stack_m1D8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48 + 0x10)));
    result = EtwpEnableDisableSpecialGuids(Arg1, Arg2 + 40, *(uint16_t *)(arg2 + 0x48 + 0x6), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))));
    result = KeLeaveCriticalRegion(Arg1, Arg2 + 40, *(uint16_t *)(arg2 + 0x48 + 0x6), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))));
    local_r11 = 0;
    if (v_stack_m1A5 != 0) goto loc_00A5D99B;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m68;
    result = EtwpEnableMetaProviderGuid(v_stack_m198, Arg2 + 40, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))), *(uint64_t *)(arg2 + 0x48 + 0x10));
    if (((uint32_t)(result)) != 0xC0000295ULL) goto loc_00A5D9A0;
    local_r11 = 0;
loc_00A5CF41:
    if (((*(uint16_t *)(arg2 + 0x48 + 0x6)) & ((uint16_t)((uint32_t)(0xFFFDULL)))) == 0) goto loc_00A5D925;
    result = PsGetCurrentProcessId((uint32_t)(0xFFFDULL), Arg2 + 40, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))), *(uint64_t *)(arg2 + 0x48 + 0x10));
    *(uint32_t *)(arg2 + 0x24) = (uint32_t)(result);
    Arg2 = v_rip - 10796001;
    if ((uint8_t)(v_stack_m126) == 0) { Arg2 = Arg2 + 40; }
    result = EtwpFindGuidEntryByGuid(v_stack_m160, Arg2, (uint32_t)((uint32_t)(v_stack_m1A7)), *(uint64_t *)(arg2 + 0x48 + 0x10));
    local_r11 = 0;
    if (result != 0) goto loc_00A5CFD2;
    if ((uint8_t)(v_stack_m126) == 0) goto loc_00A5CFA6;
loc_00A5CF92:
    goto loc_00A5D9A0;
loc_00A5CF9F:
    goto loc_00A5CF41;
loc_00A5CFA6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) goto loc_00A5CF92;
    result = EtwpAddGuidEntry(v_stack_m160, Arg2 + 40, (uint32_t)((uint32_t)(v_stack_m1A7)), *(uint64_t *)(arg2 + 0x48 + 0x10));
    if (result != 0) goto loc_00A5D09C;
    goto loc_00A5D9A0;
loc_00A5CFD2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) == 1) goto loc_00A5CFE4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48))) != 0) goto loc_00A5D09C;
loc_00A5CFE4:
    if (v_stack_m198 == 0) goto loc_00A5D09C;
    if ((*(uint64_t *)(v_rip - 0xA49FA7)) != (*(uint64_t *)(arg2 + 0x28))) goto loc_00A5D09C;
    if ((*(uint64_t *)(v_rip - 0xA49FB0)) != (*(uint64_t *)(arg2 + 0x30))) goto loc_00A5D09C;
    local_r15 = v_rip - 10732235;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) { local_r15 = v_rip - 10730736; }
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4A2827), local_r15, (uint32_t)((uint32_t)(v_stack_m1A7)), *(uint64_t *)(arg2 + 0x48 + 0x10));
    if ((uint8_t)(result) == 0) goto loc_00A5D09C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) goto loc_00A5D080;
    v_stack_m1B8 = (uint8_t)(*(uint8_t *)(arg2 + 0x48 + 0x4));
    v_stack_m1C0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48 + 0x8)));
    v_stack_m1C8 = *(uint64_t *)(arg2 + 0x48 + 0x18);
    v_stack_m1D0 = *(uint64_t *)(arg2 + 0x48 + 0x10);
    v_stack_m1D8 = v_rip - 10788850;
    result = EtwpEventWriteProviderEnabled(v_rip - 10788850, local_r15, (uint32_t)((uint32_t)(v_stack_m1A7)), v_stack_m198 + 136);
    goto loc_00A5D09C;
loc_00A5D080:
    v_stack_m1D0 = v_rip - 10788850;
    v_stack_m1D8 = v_stack_m198 + 136;
    result = EtwpEventWriteTemplateSessAndProv(v_rip - 10788850, local_r15, (uint32_t)((uint32_t)(v_stack_m1A7)), 2);
loc_00A5D09C:
    Arg1 = (v_rip - 10788850) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire((uint32_t)(0xC0000017ULL) + 664, Arg2, Arg3, 2);
    if (!(condition_is_above_or_equal)) {
        Arg3 = (uint32_t)(0xC0000017ULL) + 664;
        Arg2 = result;
        Arg1 = (uint32_t)(0xC0000017ULL) + 664;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 2);
    }
    local_r11 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1A4 = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) goto loc_00A5D144;
    if (((*(uint8_t *)((uint32_t)(0xC0000017ULL) + 0x5B)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48))))) == 0) goto loc_00A5D144;
    if ((uint32_t)((uint32_t)(v_stack_m1A0)) != 0) goto loc_00A5D144;
    if ((*(uint16_t *)(arg2 + 0x48 + 0x6)) == ((uint16_t)(*(uint16_t *)((uint32_t)(0xC0000017ULL) + 0x58)))) goto loc_00A5D144;
    if ((*(uint64_t *)(v_rip - 0xA42A8F)) != (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x28))) goto loc_00A5D144;
    if ((*(uint64_t *)(v_rip - 0xA42A94)) != (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x30))) goto loc_00A5D144;
    goto loc_00A5D954;
loc_00A5D144:
    if (v_stack_m198 == 0) goto loc_00A5D162;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x330)))) & (64)) == 0) goto loc_00A5D162;
    goto loc_00A5D954;
loc_00A5D162:
    if ((uint32_t)((uint32_t)(v_stack_m1A0)) == 0) goto loc_00A5D17C;
    result = EtwpAcquireTokenAccessInformation(v_stack_m198, Arg2, Arg3, 2);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00A5D954;
loc_00A5D17C:
    *(uint32_t *)(arg2 + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)));
    *(uint16_t *)(arg2 + 0x68) = (uint16_t)(*(uint16_t *)(arg2 + 0x48 + 0x6));
    *(uint8_t *)(arg2 + 0x6A) = (uint8_t)(*(uint8_t *)(arg2 + 0x48 + 0x4));
    *(uint32_t *)(arg2 + 0x6C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48 + 0x10)));
    if ((uint8_t)(v_stack_m126) != 0) {
        Arg1 = (uint16_t)((*(uint16_t *)(arg2 + 0x48 + 0x6)) & ((uint16_t)((uint32_t)(0x7FFFULL))));
        *(uint8_t *)(arg2 + 0x6B) = 1;
        *(uint16_t *)(arg2 + 0x68) = (uint16_t)(Arg1);
    }
    if ((*(uint64_t *)(arg2 + 0x48 + 0x10)) == 0) {
        Arg1 = (Arg1) | (-1);
        *(uint64_t *)(arg2 + 0x48 + 0x10) = Arg1;
    }
    if ((*(uint8_t *)(arg2 + 0x48 + 0x4)) == 0) {
        *(uint8_t *)(arg2 + 0x48 + 0x4) = 255;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) == 2) goto loc_00A5D25A;
    if ((uint8_t)(v_stack_m126) != 0) goto loc_00A5D25A;
    v_stack_m1D8 = v_stack_m19C;
    result = EtwpUpdateGuidEnableInfo((uint32_t)(0xC0000017ULL), Arg2, *(uint64_t *)(arg2 + 0x48 + 0x10), v_stack_m108);
    local_r11 = 0;
    if (sign_flag) goto loc_00A5D954;
    *(uint64_t *)(arg2 + 0x48) = v_xmm0;
    *(uint64_t *)(arg2 + 0x48 + 0x10) = v_xmm1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48 + 0x8)))) & (4)) == 0) goto loc_00A5D25A;
    result = EtwpPreallocateApcPool(v_stack_m198 + 832, Arg2, *(uint64_t *)(arg2 + 0x48 + 0x10), v_stack_m108);
loc_00A5D23B:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x330))))) | ((uint32_t)((uint32_t)(0x2000ULL))));
    if (condition_is_not_equal) goto loc_00A5D23B;
    result = (uint32_t)(*(uint32_t *)(v_stack_m198 + 0x330));
    if ((((uint32_t)((uint32_t)(0x2000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x330))))) == 0) {
        result = EtwpReferenceStackLookasideList(Arg1, (uint32_t)(0x2000ULL), *(uint64_t *)(arg2 + 0x48 + 0x10), v_stack_m108);
    }
    local_r11 = 0;
loc_00A5D25A:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38)) != ((uint32_t)(0xC0000017ULL) + 56)) goto loc_00A5D27D;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x290)) != 0) goto loc_00A5D275;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x10)) != ((uint32_t)(0xC0000017ULL) + 16)) goto loc_00A5D27D;
loc_00A5D275:
    goto loc_00A5D954;
loc_00A5D27D:
    if ((*(uint8_t *)(arg2 + 0xC)) == 0) goto loc_00A5D2A8;
    result = EtwpCreateUmReplyObject((uint32_t)(0xC0000017ULL), v_stack_m140, v_stack_m148, v_stack_m108);
    local_r11 = 0;
    if (sign_flag) goto loc_00A5D954;
    *(uint64_t *)(arg2 + 0x18) = v_stack_m148;
loc_00A5D2A8:
    result = EtwpBuildNotificationPacket((uint32_t)(0xC0000017ULL), Arg2, 255, v_stack_m168);
    local_r11 = 0;
    if (!sign_flag) goto loc_00A5D2CE;
    goto loc_00A5D93C;
loc_00A5D2CE:
    result = EtwpAllocDataBlock((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4)), v_stack_m168, v_stack_m190, v_stack_m168);
    local_r11 = 0;
    if (!sign_flag) goto loc_00A5D2F3;
loc_00A5D2E9:
    goto loc_00A5D92A;
loc_00A5D2F3:
    v_stack_m178 = v_stack_m190;
loc_00A5D30B:
    result = v_stack_m190;
    local_r14 = (uint32_t)(v_stack_m184);
    if ((*(uint32_t *)((uint32_t)(0xC0000017ULL) + 0x80)) != 0) {
        local_r14 = (uint16_t)((uint32_t)(v_stack_m184));
        result = 0;
    }
    Arg1 = (uint8_t)((0) + 1);
    Arg2 = ((uint32_t)(0xC0000017ULL) + 128) + (32);
    if (((uint8_t)(Arg1)) < 16) goto loc_00A5D30B;
    v_stack_m184 = (uint32_t)(local_r14);
    v_stack_m1A8 = 0;
    v_stack_m150 = 0;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x290)) != 0) goto loc_00A5D353;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x10)) != ((uint32_t)(0xC0000017ULL) + 16)) {
        Arg1 = (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x10)) + (-16);
        v_stack_m150 = Arg1;
    }
    v_stack_m160 = (uint32_t)(0xC0000017ULL);
    v_stack_m120 = v_stack_m168;
loc_00A5D362:
    v_stack_m118 = (uint32_t)(0xC0000017ULL) + 56;
    v_stack_m158 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38);
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38)) == ((uint32_t)(0xC0000017ULL) + 56)) goto loc_00A5D602;
loc_00A5D37A:
    if ((uint32_t)((uint32_t)(v_stack_m1A0)) != 0) goto loc_00A5D384;
    goto loc_00A5D401;
loc_00A5D384:
    Arg2 = ((uint32_t)(0xC0000017ULL) + 56) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    local_rbx = (*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) + 0x10)) + (664);
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, v_stack_m168);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m168);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m1A6 = 1;
    *(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x10) + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
loc_00A5D401:
    v_stack_m1C8 = (uint8_t)(v_stack_m1A7);
    v_stack_m158 = *(uint64_t *)(v_stack_m158);
    v_stack_m1D0 = (uint8_t)(v_stack_m1A8);
    v_stack_m1D8 = v_stack_m108;
    result = EtwpIsRegEntryAllowed(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m198, v_stack_m138, Arg2);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A5D584;
    v_stack_m170 = v_stack_m168;
    if (v_stack_m126 != 0) goto loc_00A5D778;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) == 2) goto loc_00A5D52E;
    if ((uint8_t)(v_stack_m1A8) == 0) goto loc_00A5D46F;
    if (v_stack_m1A0 != 0) goto loc_00A5D468;
    goto loc_00A5D482;
loc_00A5D468:
    goto loc_00A5D482;
loc_00A5D46F:
    if (v_stack_m1A0 != 0) goto loc_00A5D47D;
    goto loc_00A5D482;
loc_00A5D47D:
loc_00A5D482:
    v_stack_m1D0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)));
    v_stack_m1D8 = (uint8_t)(v_stack_m1A8);
    result = EtwpUpdateRegEntryEnableMask(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m198, v_stack_m19C, v_stack_m1A7);
    v_stack_m1C0 = v_stack_m190;
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)));
    v_stack_m1D0 = (uint8_t)(v_stack_m1A8);
    v_stack_m1D8 = (uint8_t)(v_stack_m1A7);
    result = EtwpCalculateUpdateNotification(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m19C, (uint16_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x66)), v_stack_m184);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_00A5D4FB;
    if (v_stack_m190 != 0) goto loc_00A5D584;
    v_stack_m190 = v_stack_m178;
    goto loc_00A5D584;
loc_00A5D4FB:
    if (v_stack_m190 == 0) goto loc_00A5D523;
    v_stack_m170 = v_stack_m190;
    if (v_stack_m190 == v_stack_m178) goto loc_00A5D528;
    result = EtwpUnreferenceDataBlock(v_stack_m178, v_stack_m19C, (uint16_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x66)), v_stack_m184);
    v_stack_m178 = v_stack_m190;
    goto loc_00A5D528;
loc_00A5D523:
    v_stack_m190 = result;
loc_00A5D528:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) goto loc_00A5D566;
loc_00A5D52E:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x62))) & (8)) != 0) goto loc_00A5D550;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x62))) & (16)) != 0) goto loc_00A5D550;
    if (condition_is_below) goto loc_00A5D550;
    if (((*(uint32_t *)(v_stack_m198 + 0x330)) & (0x2000000ULL)) == 0) goto loc_00A5D566;
loc_00A5D550:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x62))) & (1)) == 0) goto loc_00A5D6F6;
    Arg2 = 0;
    result = EtwpProviderArrivalCallback(v_stack_m198, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
loc_00A5D566:
loc_00A5D56A:
    result = EtwpSendDataBlock(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m170, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    local_r11 = 0;
    if (sign_flag) goto loc_00A5D584;
    if (((*(uint8_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x62)) & (2)) != 0) {
    }
    if (v_stack_m1A6 == 0) goto loc_00A5D5E7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x20) + 0x2A0) = 0;
    local_rbx = (*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 0x10 + 0x20)) + (664);
    Arg1 = (*(uint64_t *)(local_rbx)) & (-16);
    Arg2 = *(uint64_t *)(local_rbx) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_00A5D5C5;
    result = *(uint64_t *)(local_rbx);
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) {
        Arg1 = local_rbx;
        result = ExfReleasePushLock(Arg1, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    }
    result = KeAbPostRelease(local_rbx, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    result = KeLeaveCriticalRegion(local_rbx, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    local_r11 = 0;
    v_stack_m1A6 = 0;
loc_00A5D5E7:
    if (v_stack_m158 != v_stack_m118) goto loc_00A5D37A;
loc_00A5D602:
    if (v_stack_m160 == ((uint32_t)(0xC0000017ULL))) goto loc_00A5D656;
    *(uint64_t *)(v_stack_m160 + 0x2A0) = 0;
    Arg1 = (*(uint64_t *)(v_stack_m160 + 0x298)) & (-16);
    Arg2 = *(uint64_t *)(v_stack_m160 + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_stack_m160 + 0x298))) & (2)) != 0) goto loc_00A5D639;
    result = *(uint64_t *)(v_stack_m160 + 0x298);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m160 + 0x298))) & (2)) != 0) {
        Arg1 = v_stack_m160 + 664;
        result = ExfReleasePushLock(Arg1, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    }
    result = KeAbPostRelease(v_stack_m160 + 664, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    result = KeLeaveCriticalRegion(v_stack_m160 + 664, Arg2, *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x38) - 16, v_stack_m184);
    local_r11 = 0;
loc_00A5D656:
    if (v_stack_m150 == 0) goto loc_00A5D870;
    Arg1 = (v_stack_m160 + 664) | (-1);
    v_stack_m1A8 = 1;
    Arg3 = 0;
    v_stack_m160 = v_stack_m150;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m150 + 664, Arg2, Arg3, v_stack_m184);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_m150 + 664;
        Arg2 = result;
        Arg1 = v_stack_m150 + 664;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m184);
    }
    local_r11 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(v_stack_m150 + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (*(uint64_t *)(v_stack_m150 + 0x10)) + (-16);
    Arg2 = 0;
    if (result != ((uint32_t)(0xC0000017ULL))) { Arg2 = result; }
    v_stack_m150 = Arg2;
    goto loc_00A5D362;
loc_00A5D6F6:
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x50)) + (488);
    result = ExAcquireRundownProtection(Arg1, Arg2, Arg3, v_stack_m184);
    if ((uint8_t)(result) == 0) goto loc_00A5D566;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    result = PsGetProcessServerSilo(*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x50), Arg2, Arg3, v_stack_m184);
    result = PsAttachSiloToCurrentThread(result, Arg2, Arg3, v_stack_m184);
    Arg2 = 0;
    result = KiStackAttachProcess(*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x50), Arg2, v_stack_m98, v_stack_m184);
    result = EtwpProviderArrivalCallback(v_stack_m198, 1, (uint32_t)(v_stack_m1A0), v_stack_m184);
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m98, Arg2, (uint32_t)(v_stack_m1A0), v_stack_m184);
    result = PsDetachSiloFromCurrentThread(result, Arg2, (uint32_t)(v_stack_m1A0), v_stack_m184);
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x50)) + (488);
    result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)(v_stack_m1A0), v_stack_m184);
    goto loc_00A5D566;
loc_00A5D778:
    result = PsGetProcessId(*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x50), Arg2, (uint32_t)(v_stack_m1A0), v_stack_m184);
    Arg2 = (uint16_t)((*(uint16_t *)(arg2 + 0x4E)) & ((uint16_t)((uint32_t)(0x7FFFULL))));
    result = EtwpDemuxPrivateTraceHandle((uint32_t)((uint32_t)(result)), Arg2, v_stack_m188, v_stack_m184);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00A5D584;
    if (((uint16_t)(v_stack_m188)) == (*(uint16_t *)(v_stack_m190 + 0x4E))) goto loc_00A5D7F6;
    result = EtwpAllocDataBlock((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x4)), v_stack_m168, v_stack_m190, v_stack_m184);
    local_r11 = 0;
    if (sign_flag) goto loc_00A5D800;
    result = EtwpUnreferenceDataBlock(v_stack_m178, v_stack_m168, v_stack_m190, v_stack_m184);
    v_stack_m178 = v_stack_m190;
    result = (uint16_t)(((uint16_t)(v_stack_m188)) | ((uint16_t)((uint32_t)(0x8000ULL))));
    *(uint16_t *)(v_stack_m190 + 0x4E) = (uint16_t)(result);
    *(uint16_t *)(v_stack_m190 + 0x68) = (uint16_t)(v_stack_m188);
loc_00A5D7F6:
    goto loc_00A5D56A;
loc_00A5D800:
    v_stack_m190 = v_stack_m178;
    if (v_stack_m1A6 == 0) goto loc_00A5D2E9;
    *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x20) + 0x2A0) = 0;
    local_rbx = (*(uint64_t *)((uint32_t)(v_stack_m1A0) + 0x20)) + (664);
    Arg1 = (*(uint64_t *)(local_rbx)) & (-16);
    Arg2 = *(uint64_t *)(local_rbx) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_00A5D84E;
    result = *(uint64_t *)(local_rbx);
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) {
        Arg1 = local_rbx;
        result = ExfReleasePushLock(Arg1, Arg2, v_stack_m190, v_stack_m184);
    }
    result = KeAbPostRelease(local_rbx, Arg2, v_stack_m190, v_stack_m184);
    result = KeLeaveCriticalRegion(local_rbx, Arg2, v_stack_m190, v_stack_m184);
    local_r11 = 0;
    goto loc_00A5D2E9;
loc_00A5D870:
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)((uint32_t)(v_stack_m180));
    *(uint64_t *)(arg2 + 0x18) = v_stack_m140;
    if (v_stack_m198 == 0) goto loc_00A5D92A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) > 1) goto loc_00A5D92A;
    local_r15 = v_rip - 10732763;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) { local_r15 = v_rip - 10733876; }
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4A1FA3), local_r15, v_stack_m190, v_stack_m184);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A5D92A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) != 1) goto loc_00A5D903;
    v_stack_m1B8 = (uint8_t)(*(uint8_t *)(arg2 + 0x4C));
    v_stack_m1C0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)));
    v_stack_m1C8 = *(uint64_t *)(arg2 + 0x60);
    v_stack_m1D0 = *(uint64_t *)(arg2 + 0x58);
    v_stack_m1D8 = Arg2 + 40;
    result = EtwpEventWriteProviderEnabled(*(uint64_t *)(v_rip + 0x4A1FA3), local_r15, v_stack_m190, v_stack_m198 + 136);
loc_00A5D8FE:
    local_r11 = 0;
    goto loc_00A5D92A;
loc_00A5D903:
    v_stack_m1D0 = Arg2 + 40;
    v_stack_m1D8 = v_stack_m198 + 136;
    result = EtwpEventWriteTemplateSessAndProv(Arg2 + 40, local_r15, v_stack_m190, 2);
    goto loc_00A5D8FE;
loc_00A5D925:
loc_00A5D92A:
    if (v_stack_m190 != 0) {
        result = EtwpUnreferenceDataBlock(v_stack_m190, local_r15, v_stack_m190, 2);
        local_r11 = 0;
    }
    if (v_stack_m168 != 0) {
        result = EtwpUnreferenceDataBlock(v_stack_m168, local_r15, v_stack_m190, 2);
        local_r11 = 0;
    }
    if (v_stack_m1A4 == 0) goto loc_00A5D9A0;
loc_00A5D954:
    *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x2A0) = 0;
    Arg1 = (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x298)) & (-16);
    Arg2 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x298))) & (2)) != 0) goto loc_00A5D986;
    result = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x298);
    if ((((uint8_t)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x298))) & (2)) != 0) {
        Arg1 = (uint32_t)(0xC0000017ULL) + 664;
        result = ExfReleasePushLock(Arg1, Arg2, v_stack_m190, 2);
    }
    result = KeAbPostRelease((uint32_t)(0xC0000017ULL) + 664, Arg2, v_stack_m190, 2);
    result = KeLeaveCriticalRegion((uint32_t)(0xC0000017ULL) + 664, Arg2, v_stack_m190, 2);
loc_00A5D99B:
loc_00A5D9A0:
    if (v_stack_m198 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m198;
        result = EtwpReleaseLoggerContext(Arg1, Arg2, v_stack_m190, 2);
    }
    if (v_stack_m148 != 0) {
        result = ObfDereferenceObject(v_stack_m148, Arg2, v_stack_m190, 2);
    }
    if ((uint32_t)(0xC0000017ULL) != 0) {
        Arg1 = (uint32_t)(0xC0000017ULL);
        result = EtwpUnreferenceGuidEntry(Arg1, Arg2, v_stack_m190, 2);
    }
    result = EtwpFreeFilterInfo(v_stack_m108, Arg2, v_stack_m190, 2);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m190, 2);
    local_rsp = (local_rsp) + (448);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x4` | `8` | `W` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x6` | `16` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0xC` | `8` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x14` | `32` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x24` | `32` | `W` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x4C` | `8` | `R` |
| `Arg2` | `+ 0x4E` | `16` | `R` |
| `Arg2` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x68` | `16` | `W` |
| `Arg2` | `+ 0x6A` | `8` | `W` |
| `Arg2` | `+ 0x6B` | `8` | `W` |
| `Arg2` | `+ 0x6C` | `32` | `W` |
| `Arg2` | `+ 0x70` | `32` | `W` |
| `Arg2` | `+ 0x74` | `32` | `R` |

추가 오프셋 1개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A5CD28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
