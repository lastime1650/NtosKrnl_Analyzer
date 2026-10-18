# CmLoadAppKey

- RVA: `0x00876FFC`–`0x00877C82` (길이 `3,206` bytes)
- VA: `0x0000000140876FFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006CB40`
- 디코드: `693`개 명령, `3,206/3,206` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **71**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x00877089` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0087712A` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x0087713B` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (function, `0x00BC9C6C`)
- `0x008771DD` → [CmpOpenHiveFile](CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x0087721C` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0087722B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0087724D` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00877266` → [CmpLockAppHiveLoadList](CmpLockAppHiveLoadList_function_00878768.md) (function, `0x00878768`)
- `0x008772B4` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x008772ED` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x008772F2` → [CmpUnlockAppHiveLoadList](CmpUnlockAppHiveLoadList_function_00878704.md) (function, `0x00878704`)
- `0x00877308` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00877311` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0087732F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00877339` → [CmpUnlockAppHiveLoadList](CmpUnlockAppHiveLoadList_function_00878704.md) (function, `0x00878704`)
- `0x00877347` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00877366` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x00877373` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00877383` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00877388` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (function, `0x00BC9CAC`)
- `0x00877454` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x00877484` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00877495` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008774CA` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00877670` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x008776C3` → [CmpUnlockAppHiveLoadList](CmpUnlockAppHiveLoadList_function_00878704.md) (function, `0x00878704`)
- `0x0087770D` → [CmpCmdHiveOpen](CmpCmdHiveOpen_function_00878404.md) (function, `0x00878404`)
- `0x00877748` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x00877750` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x00877755` → [CmpGetLastHive](CmpGetLastHive_function_008786B4.md) (function, `0x008786B4`)
- `0x00877779` → [CmpGetNextHive](../84/CmpGetNextHive_function_0084E330.md) (function, `0x0084E330`)
- `0x008777BF` → [CmpIsThisSameFile](CmpIsThisSameFile_function_00877CE8.md) (function, `0x00877CE8`)
- `0x00877801` → [CmpSplitParentKeyName](../../pagecmrc/BC/CmpSplitParentKeyName_function_00BC9F10.md) (function, `0x00BC9F10`)
- `0x00877826` → [CmpCheckHivePrimaryFileReadWriteAccess](../../text/66/CmpCheckHivePrimaryFileReadWriteAccess_function_0066AD0C.md) (function, `0x0066AD0C`)
- `0x00877833` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877838` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877840` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x0087789F` → [PsGetProcessImageFileName](../../text/45/PsGetProcessImageFileName_function_00453720.md) (function, `0x00453720`)
- `0x008778AE` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00877926` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x0087797B` → [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) (function, `0x0046E9F8`)
- `0x00877989` → [CmpLockAppHiveLoadList](CmpLockAppHiveLoadList_function_00878768.md) (function, `0x00878768`)
- `0x00877A2C` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00877A3C` → [CmpConstructName](../85/CmpConstructName_function_00856BE0.md) (function, `0x00856BE0`)
- `0x00877A4C` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00877A61` → [CmpReferenceKeyControlBlockUnsafe](CmpReferenceKeyControlBlockUnsafe_function_00874DA0.md) (function, `0x00874DA0`)
- `0x00877A74` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877A79` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877A84` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x00877A93` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877A98` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877AA9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877AAE` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877AD0` → [ExBlockOnAddressPushLock](../../text/2A/ExBlockOnAddressPushLock_function_002A43A0.md) (function, `0x002A43A0`)
- `0x00877AD5` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x00877ADD` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x00877AE7` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877AEC` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877AF4` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x00877B14` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00877B1E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877B23` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877B30` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x00877B3A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877B3F` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877B47` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x00877B6A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00877B7E` → [ExfWaitForRundownProtectionRelease](../../text/2A/ExfWaitForRundownProtectionRelease_function_002A4CDC.md) (function, `0x002A4CDC`)
- `0x00877C46` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00877C4B` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x00877C5B` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)

### Direct callers
- [CmLoadDifferencingKey](CmLoadDifferencingKey_function_00875670.md) at `0x00875C33`

### Static image references
- `0x0087701B` → RVA `0x00E0A740` (`.data`; read)
- `0x008771F9` → RVA `0x00EF7C68` (`.data`; read)
- `0x0087726B` → RVA `0x00EF5990` (`.data`; read)
- `0x0087727E` → RVA `0x00EF5998` (`.data`; read)
- `0x00877395` → RVA `0x00E09F58` (`.data`; read)
- `0x008773AC` → RVA `0x00E09F68` (`.data`; read)
- `0x008773D3` → RVA `0x000568B1` (`.rdata`; read)
- `0x00877470` → RVA `0x00E09F70` (`.data`; read)
- `0x008775C7` → RVA `0x000565A8` (`.rdata`; read)
- `0x008776BC` → RVA `0x00EF5998` (`.data`; write)
- `0x00877766` → RVA `0x00EF59A8` (`.data`; read)
- `0x008778C5` → RVA `0x0005640A` (`.rdata`; read)
- `0x00877AC9` → RVA `0x00EF59A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **38**
  - `0x00877089` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0087712A` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x0087713B` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (`PAGE` → `PAGECMRC`)
  - `0x0087722B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0087724D` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008772ED` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00877308` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00877311` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x0087732F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00877347` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00877373` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00877383` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00877388` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (`PAGE` → `PAGECMRC`)
  - `0x00877454` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00877484` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00877495` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008774CA` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00877670` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00877801` → [CmpSplitParentKeyName](../../pagecmrc/BC/CmpSplitParentKeyName_function_00BC9F10.md) (`PAGE` → `PAGECMRC`)
  - `0x00877826` → [CmpCheckHivePrimaryFileReadWriteAccess](../../text/66/CmpCheckHivePrimaryFileReadWriteAccess_function_0066AD0C.md) (`PAGE` → `.text`)
  - `0x00877833` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0087789F` → [PsGetProcessImageFileName](../../text/45/PsGetProcessImageFileName_function_00453720.md) (`PAGE` → `.text`)
  - `0x008778AE` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00877926` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x0087797B` → [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) (`PAGE` → `.text`)
  - `0x00877A2C` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00877A4C` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00877A74` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00877A93` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00877AA9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00877AD0` → [ExBlockOnAddressPushLock](../../text/2A/ExBlockOnAddressPushLock_function_002A43A0.md) (`PAGE` → `.text`)
  - `0x00877AE7` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00877B14` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00877B1E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00877B3A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00877B6A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00877B7E` → [ExfWaitForRundownProtectionRelease](../../text/2A/ExfWaitForRundownProtectionRelease_function_002A4CDC.md) (`PAGE` → `.text`)
  - `0x00877C46` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x008776A4` → [sub_00B179DA + 0x1AB](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)
  - `0x00877742` → [sub_00B179DA](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)
  - `0x00877799` → [sub_00B179DA + 0x90](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)
  - `0x00877852` → [sub_00B179DA + 0xF5](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)
  - `0x00877C0C` → [sub_00B179DA + 0x107](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)
  - `0x00877C16` → [sub_00B179DA + 0xFD](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)
  - `0x00877C7D` → [sub_00B179DA + 0xFD](../B1/Unknown_function_00B179DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00876FFC  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00877001  55                              push rbp
00877002  56                              push rsi
00877003  57                              push rdi
00877004  41 54                           push r12
00877006  41 55                           push r13
00877008  41 56                           push r14
0087700A  41 57                           push r15
0087700C  48 8D AC 24 00 FE FF FF         lea rbp, [rsp - 0x200]
00877014  48 81 EC 00 03 00 00            sub rsp, 0x300
0087701B  48 8B 05 1E 37 59 00            mov rax, qword ptr [rip + 0x59371e]
00877022  48 33 C4                        xor rax, rsp
00877025  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
0087702C  48 8B 85 60 02 00 00            mov rax, qword ptr [rbp + 0x260]
00877033  45 33 F6                        xor r14d, r14d
00877036  48 8B 9D 70 02 00 00            mov rbx, qword ptr [rbp + 0x270]
0087703D  48 8B F9                        mov rdi, rcx
00877040  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00877045  48 8B 85 68 02 00 00            mov rax, qword ptr [rbp + 0x268]
0087704C  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
00877050  48 8B 85 80 02 00 00            mov rax, qword ptr [rbp + 0x280]
00877057  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0087705B  48 8B 85 88 02 00 00            mov rax, qword ptr [rbp + 0x288]
00877062  44 89 44 24 6C                  mov dword ptr [rsp + 0x6c], r8d
00877067  45 8D 46 50                     lea r8d, [r14 + 0x50]
0087706B  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
0087706F  33 D2                           xor edx, edx
00877071  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
00877075  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00877079  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0087707D  48 89 5D 18                     mov qword ptr [rbp + 0x18], rbx
00877081  44 89 75 90                     mov dword ptr [rbp - 0x70], r14d
00877085  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
00877089  E8 B2 FB E4 FF                  call 0x1406c6c40
0087708E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00877092  0F 57 C0                        xorps xmm0, xmm0
00877095  44 88 74 24 64                  mov byte ptr [rsp + 0x64], r14b
0087709A  45 8A FE                        mov r15b, r14b
0087709D  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
008770A1  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
008770A6  45 8B E6                        mov r12d, r14d
008770A9  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
008770B0  44 88 74 24 66                  mov byte ptr [rsp + 0x66], r14b
008770B5  45 8B EE                        mov r13d, r14d
008770B8  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
008770BF  0F B7 08                        movzx ecx, word ptr [rax]
008770C2  41 8B F6                        mov esi, r14d
008770C5  41 8D 46 02                     lea eax, [r14 + 2]
008770C9  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
008770CD  4C 89 75 28                     mov qword ptr [rbp + 0x28], r14
008770D1  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
008770D5  66 3B C8                        cmp cx, ax
008770D8  72 20                           jb 0x1408770fa
008770DA  8B D1                           mov edx, ecx
008770DC  D1 EA                           shr edx, 1
008770DE  74 1A                           je 0x1408770fa
008770E0  4C 8B 47 10                     mov r8, qword ptr [rdi + 0x10]
008770E4  8D 42 FF                        lea eax, [rdx - 1]
008770E7  8B C8                           mov ecx, eax
008770E9  8B D0                           mov edx, eax
008770EB  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
008770EF  66 83 3C 48 5C                  cmp word ptr [rax + rcx*2], 0x5c
008770F4  0F 84 F7 0A 00 00               je 0x140877bf1
008770FA  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008770FE  48 B9 08 00 00 00 00 40 00 00   movabs rcx, 0x400000000008
00877108  BF 02 00 00 00                  mov edi, 2
0087710D  44 8D 77 FF                     lea r14d, [rdi - 1]
00877111  66 39 38                        cmp word ptr [rax], di
00877114  0F 82 ED 0A 00 00               jb 0x140877c07
0087711A  BA B0 01 00 00                  mov edx, 0x1b0
0087711F  B9 00 01 00 00                  mov ecx, 0x100
00877124  41 B8 43 4D 39 33               mov r8d, 0x33394d43
0087712A  E8 D5 63 B5 FF                  call 0x1403cd504
0087712F  48 8B F0                        mov rsi, rax
00877132  48 85 C0                        test rax, rax
00877135  0F 84 D6 0A 00 00               je 0x140877c11
0087713B  E8 2C 2B 35 00                  call 0x140bc9c6c
00877140  84 C0                           test al, al
00877142  0F 84 D3 0A 00 00               je 0x140877c1b
00877148  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
0087714D  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00877151  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
00877155  41 8B C0                        mov eax, r8d
00877158  83 E0 20                        and eax, 0x20
0087715B  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00877160  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00877163  F7 D8                           neg eax
00877165  41 8B C0                        mov eax, r8d
00877168  1B C9                           sbb ecx, ecx
0087716A  81 E1 00 00 00 04               and ecx, 0x4000000
00877170  81 C1 01 00 19 03               add ecx, 0x3190001
00877176  8B D1                           mov edx, ecx
00877178  0F BA EA 1B                     bts edx, 0x1b
0087717C  41 F6 C0 80                     test r8b, 0x80
00877180  0F 44 D1                        cmove edx, ecx
00877183  8B CA                           mov ecx, edx
00877185  0F BA E9 1C                     bts ecx, 0x1c
00877189  41 0F BA E0 09                  bt r8d, 9
0087718E  0F 43 CA                        cmovae ecx, edx
00877191  25 00 20 00 00                  and eax, 0x2000
00877196  89 4D A0                        mov dword ptr [rbp - 0x60], ecx
00877199  41 8B CC                        mov ecx, r12d
0087719C  0F 95 C1                        setne cl
0087719F  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008771A3  8B D1                           mov edx, ecx
008771A5  48 8D 45 98                     lea rax, [rbp - 0x68]
008771A9  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008771AE  83 CA 20                        or edx, 0x20
008771B1  41 0F BA E0 0F                  bt r8d, 0xf
008771B6  4C 8D 45 88                     lea r8, [rbp - 0x78]
008771BA  0F 43 D1                        cmovae edx, ecx
008771BD  4C 21 64 24 38                  and qword ptr [rsp + 0x38], r12
008771C2  4C 21 64 24 30                  and qword ptr [rsp + 0x30], r12
008771C7  48 8B CF                        mov rcx, rdi
008771CA  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
008771CE  33 D2                           xor edx, edx
008771D0  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
008771D5  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
008771DD  E8 3A 35 00 00                  call 0x14087a71c
008771E2  8B D8                           mov ebx, eax
008771E4  3D 34 00 00 C0                  cmp eax, 0xc0000034
008771E9  0F 84 39 0A 00 00               je 0x140877c28
008771EF  33 D2                           xor edx, edx
008771F1  85 C0                           test eax, eax
008771F3  0F 88 BD 02 00 00               js 0x1408774b6
008771F9  48 8B 05 68 0A 68 00            mov rax, qword ptr [rip + 0x680a68]
00877200  45 33 C9                        xor r9d, r9d
00877203  4C 21 64 24 28                  and qword ptr [rsp + 0x28], r12
00877208  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0087720C  4C 21 65 10                     and qword ptr [rbp + 0x10], r12
00877210  4C 8B 00                        mov r8, qword ptr [rax]
00877213  48 8D 45 10                     lea rax, [rbp + 0x10]
00877217  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087721C  E8 8F 1B FF FF                  call 0x140868db0
00877221  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00877225  8B D8                           mov ebx, eax
00877227  4C 8B 6D 10                     mov r13, qword ptr [rbp + 0x10]
0087722B  E8 80 60 E3 FF                  call 0x1406ad2b0
00877230  85 DB                           test ebx, ebx
00877232  0F 88 E3 00 00 00               js 0x14087731b
00877238  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
0087723C  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00877240  44 88 65 E8                     mov byte ptr [rbp - 0x18], r12b
00877244  45 33 C0                        xor r8d, r8d
00877247  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0087724B  33 D2                           xor edx, edx
0087724D  E8 BE 6A B9 FF                  call 0x14040dd10
00877252  4C 21 65 08                     and qword ptr [rbp + 8], r12
00877256  48 8D 45 D0                     lea rax, [rbp - 0x30]
0087725A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0087725E  48 8D 45 D0                     lea rax, [rbp - 0x30]
00877262  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00877266  E8 FD 14 00 00                  call 0x140878768
0087726B  48 8B 1D 1E E7 67 00            mov rbx, qword ptr [rip + 0x67e71e]
00877272  48 8D 0D 17 E7 67 00            lea rcx, [rip + 0x67e717]
00877279  48 3B D9                        cmp rbx, rcx
0087727C  75 17                           jne 0x140877295
0087727E  48 8B 05 13 E7 67 00            mov rax, qword ptr [rip + 0x67e713]
00877285  48 39 08                        cmp qword ptr [rax], rcx
00877288  0F 84 1B 04 00 00               je 0x1408776a9
0087728E  B9 03 00 00 00                  mov ecx, 3
00877293  CD 29                           int 0x29
00877295  44 38 63 28                     cmp byte ptr [rbx + 0x28], r12b
00877299  75 0F                           jne 0x1408772aa
0087729B  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0087729F  48 39 43 20                     cmp qword ptr [rbx + 0x20], rax
008772A3  74 1C                           je 0x1408772c1
008772A5  48 8B 1B                        mov rbx, qword ptr [rbx]
008772A8  EB CF                           jmp 0x140877279
008772AA  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008772AE  45 8A C6                        mov r8b, r14b
008772B1  48 8B D7                        mov rdx, rdi
008772B4  E8 67 B7 0B 00                  call 0x140932a20
008772B9  84 C0                           test al, al
008772BB  0F 84 79 09 00 00               je 0x140877c3a
008772C1  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
008772C5  48 83 C3 10                     add rbx, 0x10
008772C9  48 39 18                        cmp qword ptr [rax], rbx
008772CC  75 C0                           jne 0x14087728e
008772CE  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
008772D2  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008772D6  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
008772DA  48 89 08                        mov qword ptr [rax], rcx
008772DD  48 8D 45 D0                     lea rax, [rbp - 0x30]
008772E1  48 89 43 08                     mov qword ptr [rbx + 8], rax
008772E5  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
008772E9  48 8D 4B 38                     lea rcx, [rbx + 0x38]
008772ED  E8 2E F3 99 FF                  call 0x140216620
008772F2  E8 0D 14 00 00                  call 0x140878704
008772F7  4C 21 64 24 20                  and qword ptr [rsp + 0x20], r12
008772FC  48 8D 4B 20                     lea rcx, [rbx + 0x20]
00877300  45 33 C9                        xor r9d, r9d
00877303  45 33 C0                        xor r8d, r8d
00877306  33 D2                           xor edx, edx
00877308  E8 A3 73 99 FF                  call 0x14020e6b0
0087730D  48 8D 4B 38                     lea rcx, [rbx + 0x38]
00877311  E8 6A 2B AD FF                  call 0x140349e80
00877316  E9 AD 03 00 00                  jmp 0x1408776c8
0087731B  B8 20 00 00 00                  mov eax, 0x20
00877320  44 8B CB                        mov r9d, ebx
00877323  44 8B C0                        mov r8d, eax
00877326  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0087732A  33 D2                           xor edx, edx
0087732C  48 8B CE                        mov rcx, rsi
0087732F  E8 20 7C BF FF                  call 0x14046ef54
00877334  45 33 FF                        xor r15d, r15d
00877337  EB 32                           jmp 0x14087736b
00877339  E8 C6 13 00 00                  call 0x140878704
0087733E  45 33 C0                        xor r8d, r8d
00877341  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00877345  33 D2                           xor edx, edx
00877347  E8 C4 7F AC FF                  call 0x14033f310
0087734C  33 C0                           xor eax, eax
0087734E  F0 4C 0F B1 75 08               lock cmpxchg qword ptr [rbp + 8], r14
00877354  48 83 F8 02                     cmp rax, 2
00877358  0F 83 19 08 00 00               jae 0x140877b77
0087735E  4D 85 E4                        test r12, r12
00877361  74 08                           je 0x14087736b
00877363  49 8B CC                        mov rcx, r12
00877366  E8 45 BF FE FF                  call 0x1408632b0
0087736B  4D 85 ED                        test r13, r13
0087736E  74 08                           je 0x140877378
00877370  49 8B CD                        mov rcx, r13
00877373  E8 D8 1F A8 FF                  call 0x1402f9350
00877378  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0087737C  48 85 C9                        test rcx, rcx
0087737F  74 07                           je 0x140877388
00877381  33 D2                           xor edx, edx
00877383  E8 E8 B4 30 00                  call 0x140b82870
00877388  E8 1F 29 35 00                  call 0x140bc9cac
0087738D  85 DB                           test ebx, ebx
0087738F  0F 88 C6 00 00 00               js 0x14087745b
00877395  83 3D BC 2B 59 00 05            cmp dword ptr [rip + 0x592bbc], 5
0087739C  0F 86 DF 00 00 00               jbe 0x140877481
008773A2  48 BA 08 00 00 00 00 40 00 00   movabs rdx, 0x400000000008
008773AC  48 85 15 B5 2B 59 00            test qword ptr [rip + 0x592bb5], rdx
008773B3  0F 85 EE 07 00 00               jne 0x140877ba7
008773B9  41 8A C7                        mov al, r15b
008773BC  84 C0                           test al, al
008773BE  0F 84 BD 00 00 00               je 0x140877481
008773C4  48 8D 45 80                     lea rax, [rbp - 0x80]
008773C8  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
008773CC  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
008773D3  48 8D 15 D7 F4 7D FF            lea rdx, [rip - 0x820b29]
008773DA  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008773DF  48 C7 85 C8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xc8], 8
008773EA  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
008773F1  48 8D 0D 60 2B 59 00            lea rcx, [rip + 0x592b60]
008773F8  8A 44 24 66                     mov al, byte ptr [rsp + 0x66]
008773FC  41 B9 06 00 00 00               mov r9d, 6
00877402  88 44 24 60                     mov byte ptr [rsp + 0x60], al
00877406  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0087740B  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00877412  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00877417  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
0087741E  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00877425  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087742A  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
0087742E  48 C7 85 D8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xd8], 4
00877439  4C 89 B5 E8 00 00 00            mov qword ptr [rbp + 0xe8], r14
00877440  48 C7 44 24 78 00 00 00 01      mov qword ptr [rsp + 0x78], 0x1000000
00877449  48 C7 85 F8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xf8], 8
00877454  E8 23 9B A7 FF                  call 0x1402f0f7c
00877459  EB 26                           jmp 0x140877481
0087745B  44 0F B7 5E 08                  movzx r11d, word ptr [rsi + 8]
00877460  66 45 85 DB                     test r11w, r11w
00877464  0F 84 FB 07 00 00               je 0x140877c65
0087746A  8B 15 E8 2A 59 00               mov edx, dword ptr [rip + 0x592ae8]
00877470  48 8B 0D F9 2A 59 00            mov rcx, qword ptr [rip + 0x592af9]
00877477  83 FA 05                        cmp edx, 5
0087747A  77 5B                           ja 0x1408774d7
0087747C  48 85 F6                        test rsi, rsi
0087747F  74 08                           je 0x140877489
00877481  48 8B CE                        mov rcx, rsi
00877484  E8 F7 E8 BF FF                  call 0x140475d80
00877489  8B C3                           mov eax, ebx
0087748B  48 8B 8D F0 01 00 00            mov rcx, qword ptr [rbp + 0x1f0]
00877492  48 33 CC                        xor rcx, rsp
00877495  E8 A6 51 E3 FF                  call 0x1406ac640
0087749A  48 8B 9C 24 58 03 00 00         mov rbx, qword ptr [rsp + 0x358]
008774A2  48 81 C4 00 03 00 00            add rsp, 0x300
008774A9  41 5F                           pop r15
008774AB  41 5E                           pop r14
008774AD  41 5D                           pop r13
008774AF  41 5C                           pop r12
008774B1  5F                              pop rdi
008774B2  5E                              pop rsi
008774B3  5D                              pop rbp
008774B4  C3                              ret
008774B5  CC                              int3
008774B6  44 8B C8                        mov r9d, eax
008774B9  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
008774C1  41 B8 20 00 00 00               mov r8d, 0x20
008774C7  48 8B CE                        mov rcx, rsi
008774CA  E8 85 7A BF FF                  call 0x14046ef54
008774CF  45 33 FF                        xor r15d, r15d
008774D2  E9 A1 FE FF FF                  jmp 0x140877378
008774D7  49 B8 08 00 00 00 00 40 00 00   movabs r8, 0x400000000008
008774E1  4C 85 05 80 2A 59 00            test qword ptr [rip + 0x592a80], r8
008774E8  0F 85 D8 06 00 00               jne 0x140877bc6
008774EE  41 8A C7                        mov al, r15b
008774F1  84 C0                           test al, al
008774F3  0F 84 89 01 00 00               je 0x140877682
008774F9  48 8D 56 0A                     lea rdx, [rsi + 0xa]
008774FD  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
00877501  44 0F B7 0A                     movzx r9d, word ptr [rdx]
00877505  4C 8D 86 8A 01 00 00            lea r8, [rsi + 0x18a]
0087750C  45 0F B6 10                     movzx r10d, byte ptr [r8]
00877510  43 8D 0C 5B                     lea ecx, [r11 + r11*2]
00877514  48 8D 45 80                     lea rax, [rbp - 0x80]
00877518  C1 E1 02                        shl ecx, 2
0087751B  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00877522  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00877527  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
0087752E  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00877533  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
0087753A  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0087753F  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00877546  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
0087754B  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00877552  48 8D 46 08                     lea rax, [rsi + 8]
00877556  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
0087755D  48 8D 46 0C                     lea rax, [rsi + 0xc]
00877561  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00877568  48 8D 46 6C                     lea rax, [rsi + 0x6c]
0087756C  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
00877573  43 8D 04 49                     lea eax, [r9 + r9*2]
00877577  C1 E0 02                        shl eax, 2
0087757A  89 85 48 01 00 00               mov dword ptr [rbp + 0x148], eax
00877580  48 8D 86 8C 01 00 00            lea rax, [rsi + 0x18c]
00877587  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
0087758E  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00877593  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
0087759A  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
008775A1  66 44 89 54 24 6C               mov word ptr [rsp + 0x6c], r10w
008775A7  66 44 89 4C 24 70               mov word ptr [rsp + 0x70], r9w
008775AD  41 B9 0E 00 00 00               mov r9d, 0xe
008775B3  89 8D 28 01 00 00               mov dword ptr [rbp + 0x128], ecx
008775B9  48 8D 0D 98 29 59 00            lea rcx, [rip + 0x592998]
008775C0  48 89 95 30 01 00 00            mov qword ptr [rbp + 0x130], rdx
008775C7  48 8D 15 DA EF 7D FF            lea rdx, [rip - 0x821026]
008775CE  41 C1 E2 03                     shl r10d, 3
008775D2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008775D7  48 C7 85 C8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xc8], 8
008775E2  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
008775E6  48 C7 85 D8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xd8], 4
008775F1  66 44 89 5C 24 60               mov word ptr [rsp + 0x60], r11w
008775F7  48 C7 85 E8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xe8], 2
00877602  48 C7 85 F8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xf8], 2
0087760D  48 C7 85 08 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x108], 2
00877618  48 C7 85 18 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x118], 2
00877623  44 89 BD 2C 01 00 00            mov dword ptr [rbp + 0x12c], r15d
0087762A  48 C7 85 38 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x138], 2
00877635  44 89 BD 4C 01 00 00            mov dword ptr [rbp + 0x14c], r15d
0087763C  4C 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], r8
00877643  48 C7 85 58 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x158], 2
0087764E  44 89 95 68 01 00 00            mov dword ptr [rbp + 0x168], r10d
00877655  44 89 BD 6C 01 00 00            mov dword ptr [rbp + 0x16c], r15d
0087765C  48 C7 44 24 78 00 00 00 01      mov qword ptr [rsp + 0x78], 0x1000000
00877665  48 C7 85 78 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x178], 8
00877670  E8 07 99 A7 FF                  call 0x1402f0f7c
00877675  48 8B 0D F4 28 59 00            mov rcx, qword ptr [rip + 0x5928f4]
0087767C  8B 15 D6 28 59 00               mov edx, dword ptr [rip + 0x5928d6]
00877682  83 FA 05                        cmp edx, 5
00877685  0F 86 F1 FD FF FF               jbe 0x14087747c
0087768B  F6 05 D6 28 59 00 08            test byte ptr [rip + 0x5928d6], 8
00877692  0F 85 45 05 00 00               jne 0x140877bdd
00877698  45 8A F7                        mov r14b, r15b
0087769B  45 84 F6                        test r14b, r14b
0087769E  0F 84 D8 FD FF FF               je 0x14087747c
008776A4  E9 DC 04 2A 00                  jmp 0x140b17b85
008776A9  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
008776AD  48 8D 4D C0                     lea rcx, [rbp - 0x40]
008776B1  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008776B5  48 89 08                        mov qword ptr [rax], rcx
008776B8  48 8D 45 C0                     lea rax, [rbp - 0x40]
008776BC  48 89 05 D5 E2 67 00            mov qword ptr [rip + 0x67e2d5], rax
008776C3  E8 3C 10 00 00                  call 0x140878704
008776C8  48 83 65 38 00                  and qword ptr [rbp + 0x38], 0
008776CD  48 8D 44 24 64                  lea rax, [rsp + 0x64]
008776D2  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008776D7  4C 8D 4D 38                     lea r9, [rbp + 0x38]
008776DB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008776E0  4C 8D 44 24 65                  lea r8, [rsp + 0x65]
008776E5  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
008776E9  41 8A D6                        mov dl, r14b
008776EC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008776F1  48 8B CF                        mov rcx, rdi
008776F4  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008776F8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008776FC  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
008776FF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00877703  44 88 74 24 65                  mov byte ptr [rsp + 0x65], r14b
00877708  C6 44 24 64 00                  mov byte ptr [rsp + 0x64], 0
0087770D  E8 F2 0C 00 00                  call 0x140878404
00877712  8B D8                           mov ebx, eax
00877714  85 C0                           test eax, eax
00877716  0F 84 14 02 00 00               je 0x140877930
0087771C  3D 43 00 00 C0                  cmp eax, 0xc0000043
00877721  0F 85 2F 04 00 00               jne 0x140877b56
00877727  83 7D A4 00                     cmp dword ptr [rbp - 0x5c], 0
0087772B  0F 85 25 04 00 00               jne 0x140877b56
00877731  45 84 FF                        test r15b, r15b
00877734  0F 85 1C 04 00 00               jne 0x140877b56
0087773A  45 33 FF                        xor r15d, r15d
0087773D  44 38 7C 24 60                  cmp byte ptr [rsp + 0x60], r15b
00877742  0F 85 92 02 2A 00               jne 0x140b179da
00877748  E8 B3 AB 13 00                  call 0x1409b2300
0087774D  41 8A CE                        mov cl, r14b
00877750  E8 8F D3 13 00                  call 0x1409b4ae4
00877755  E8 5A 0F 00 00                  call 0x1408786b4
0087775A  4C 8B E0                        mov r12, rax
0087775D  48 85 C0                        test rax, rax
00877760  0F 84 E0 04 00 00               je 0x140877c46
00877766  8B 05 3C E2 67 00               mov eax, dword ptr [rip + 0x67e23c]
0087776C  89 45 94                        mov dword ptr [rbp - 0x6c], eax
0087776F  85 C0                           test eax, eax
00877771  0F 85 32 03 00 00               jne 0x140877aa9
00877777  33 C9                           xor ecx, ecx
00877779  E8 B2 6B FD FF                  call 0x14084e330
0087777E  48 8B F8                        mov rdi, rax
00877781  48 85 C0                        test rax, rax
00877784  0F 84 09 03 00 00               je 0x140877a93
0087778A  4C 8D B8 A0 12 00 00            lea r15, [rax + 0x12a0]
00877791  41 8B 07                        mov eax, dword ptr [r15]
00877794  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00877797  85 C0                           test eax, eax
00877799  0F 85 CB 02 2A 00               jne 0x140b17a6a
0087779F  48 8B 97 08 06 00 00            mov rdx, qword ptr [rdi + 0x608]
008777A6  45 33 FF                        xor r15d, r15d
008777A9  48 85 D2                        test rdx, rdx
008777AC  75 0E                           jne 0x1408777bc
008777AE  49 3B FC                        cmp rdi, r12
008777B1  0F 84 A1 04 00 00               je 0x140877c58
008777B7  48 8B CF                        mov rcx, rdi
008777BA  EB BD                           jmp 0x140877779
008777BC  49 8B CD                        mov rcx, r13
008777BF  E8 24 05 00 00                  call 0x140877ce8
008777C4  84 C0                           test al, al
008777C6  75 0A                           jne 0x1408777d2
008777C8  49 3B FC                        cmp rdi, r12
008777CB  75 EA                           jne 0x1408777b7
008777CD  E9 AF 02 00 00                  jmp 0x140877a81
008777D2  8B 9F A0 00 00 00               mov ebx, dword ptr [rdi + 0xa0]
008777D8  8B 87 10 10 00 00               mov eax, dword ptr [rdi + 0x1010]
008777DE  81 E3 00 80 00 00               and ebx, 0x8000
008777E4  A8 20                           test al, 0x20
008777E6  0F 84 4E 03 00 00               je 0x140877b3a
008777EC  A8 40                           test al, 0x40
008777EE  0F 85 46 03 00 00               jne 0x140877b3a
008777F4  48 8D 8F 30 07 00 00            lea rcx, [rdi + 0x730]
008777FB  33 D2                           xor edx, edx
008777FD  4C 8D 45 60                     lea r8, [rbp + 0x60]
00877801  E8 0A 27 35 00                  call 0x140bc9f10
00877806  83 3D 4B 27 59 00 05            cmp dword ptr [rip + 0x59274b], 5
0087780D  77 48                           ja 0x140877857
0087780F  44 39 7C 24 68                  cmp dword ptr [rsp + 0x68], r15d
00877814  0F 84 06 02 00 00               je 0x140877a20
0087781A  85 DB                           test ebx, ebx
0087781C  0F 85 06 02 00 00               jne 0x140877a28
00877822  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00877826  E8 E1 34 DF FF                  call 0x14066ad0c
0087782B  84 C0                           test al, al
0087782D  0F 85 F5 01 00 00               jne 0x140877a28
00877833  E8 4C 22 35 00                  call 0x140bc9a84
00877838  E8 7F B6 13 00                  call 0x1409b2ebc
0087783D  48 8B CF                        mov rcx, rdi
00877840  E8 6B BA FE FF                  call 0x1408632b0
00877845  BB 22 00 00 C0                  mov ebx, 0xc0000022
0087784A  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
00877852  E9 78 02 2A 00                  jmp 0x140b17acf
00877857  48 BA 08 00 00 00 00 40 00 00   movabs rdx, 0x400000000008
00877861  48 85 15 00 27 59 00            test qword ptr [rip + 0x592700], rdx
00877868  0F 85 1A 03 00 00               jne 0x140877b88
0087786E  41 8A C7                        mov al, r15b
00877871  84 C0                           test al, al
00877873  74 9A                           je 0x14087780f
00877875  48 8D 45 40                     lea rax, [rbp + 0x40]
00877879  4C 89 75 40                     mov qword ptr [rbp + 0x40], r14
0087787D  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00877884  48 C7 85 A8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1a8], 8
0087788F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00877898  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0087789F  E8 7C BE BD FF                  call 0x140453720
008778A4  48 8B D0                        mov rdx, rax
008778A7  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
008778AE  E8 51 FA BA FF                  call 0x140427304
008778B3  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
008778B7  48 8D 8D D8 01 00 00            lea rcx, [rbp + 0x1d8]
008778BE  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
008778C5  48 8D 15 3E EB 7D FF            lea rdx, [rip - 0x8214c2]
008778CC  0F B7 45 60                     movzx eax, word ptr [rbp + 0x60]
008778D0  41 B9 07 00 00 00               mov r9d, 7
008778D6  89 85 D8 01 00 00               mov dword ptr [rbp + 0x1d8], eax
008778DC  48 8D 45 48                     lea rax, [rbp + 0x48]
008778E0  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
008778E7  48 8D 85 80 01 00 00            lea rax, [rbp + 0x180]
008778EE  48 89 8D C0 01 00 00            mov qword ptr [rbp + 0x1c0], rcx
008778F5  48 8D 0D 5C 26 59 00            lea rcx, [rip + 0x59265c]
008778FC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00877901  48 C7 85 C8 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x1c8], 2
0087790C  44 89 BD DC 01 00 00            mov dword ptr [rbp + 0x1dc], r15d
00877913  48 C7 45 48 00 00 00 01         mov qword ptr [rbp + 0x48], 0x1000000
0087791B  48 C7 85 E8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1e8], 8
00877926  E8 51 96 A7 FF                  call 0x1402f0f7c
0087792B  E9 DF FE FF FF                  jmp 0x14087780f
00877930  8A 44 24 64                     mov al, byte ptr [rsp + 0x64]
00877934  45 33 FF                        xor r15d, r15d
00877937  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0087793C  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
00877941  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00877945  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00877949  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0087794E  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00877952  8A 44 24 65                     mov al, byte ptr [rsp + 0x65]
00877956  88 44 24 40                     mov byte ptr [rsp + 0x40], al
0087795A  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0087795E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00877963  8A 85 78 02 00 00               mov al, byte ptr [rbp + 0x278]
00877969  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0087796D  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00877971  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00877976  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0087797B  E8 78 70 BF FF                  call 0x14046e9f8
00877980  8B D8                           mov ebx, eax
00877982  EB 05                           jmp 0x140877989
00877984  44 88 74 24 66                  mov byte ptr [rsp + 0x66], r14b
00877989  E8 DA 0D 00 00                  call 0x140878768
0087798E  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00877992  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00877996  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0087799A  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
0087799E  0F 85 EA F8 FF FF               jne 0x14087728e
008779A4  48 8D 55 C0                     lea rdx, [rbp - 0x40]
008779A8  48 39 10                        cmp qword ptr [rax], rdx
008779AB  0F 85 DD F8 FF FF               jne 0x14087728e
008779B1  48 89 08                        mov qword ptr [rax], rcx
008779B4  48 89 41 08                     mov qword ptr [rcx + 8], rax
008779B8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008779BC  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
008779C0  48 3B C1                        cmp rax, rcx
008779C3  0F 84 70 F9 FF FF               je 0x140877339
008779C9  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
008779CD  4C 8D 45 D0                     lea r8, [rbp - 0x30]
008779D1  48 8D 48 F0                     lea rcx, [rax - 0x10]
008779D5  4C 39 40 08                     cmp qword ptr [rax + 8], r8
008779D9  0F 85 AF F8 FF FF               jne 0x14087728e
008779DF  4C 8D 45 D0                     lea r8, [rbp - 0x30]
008779E3  4C 39 02                        cmp qword ptr [rdx], r8
008779E6  0F 85 A2 F8 FF FF               jne 0x14087728e
008779EC  48 89 02                        mov qword ptr [rdx], rax
008779EF  48 89 50 08                     mov qword ptr [rax + 8], rdx
008779F3  48 8D 15 96 DF 67 00            lea rdx, [rip + 0x67df96]
008779FA  48 8B 05 97 DF 67 00            mov rax, qword ptr [rip + 0x67df97]
00877A01  48 39 10                        cmp qword ptr [rax], rdx
00877A04  0F 85 84 F8 FF FF               jne 0x14087728e
00877A0A  48 89 11                        mov qword ptr [rcx], rdx
00877A0D  48 89 41 08                     mov qword ptr [rcx + 8], rax
00877A11  48 89 08                        mov qword ptr [rax], rcx
00877A14  48 89 0D 7D DF 67 00            mov qword ptr [rip + 0x67df7d], rcx
00877A1B  E9 19 F9 FF FF                  jmp 0x140877339
00877A20  85 DB                           test ebx, ebx
00877A22  0F 85 BF 00 00 00               jne 0x140877ae7
00877A28  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00877A2C  E8 AF 1E 35 00                  call 0x140bc98e0
00877A31  48 8B 8F 78 0B 00 00            mov rcx, qword ptr [rdi + 0xb78]
00877A38  48 89 7D 28                     mov qword ptr [rbp + 0x28], rdi
00877A3C  E8 9F F1 FD FF                  call 0x140856be0
00877A41  48 8B 5D 50                     mov rbx, qword ptr [rbp + 0x50]
00877A45  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00877A49  48 89 03                        mov qword ptr [rbx], rax
00877A4C  E8 CF 1E 35 00                  call 0x140bc9920
00877A51  4C 39 3B                        cmp qword ptr [rbx], r15
00877A54  0F 84 C4 00 00 00               je 0x140877b1e
00877A5A  48 8B 8F 78 0B 00 00            mov rcx, qword ptr [rdi + 0xb78]
00877A61  E8 3A D3 FF FF                  call 0x140874da0
00877A66  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00877A6A  48 8B 87 78 0B 00 00            mov rax, qword ptr [rdi + 0xb78]
00877A71  48 89 01                        mov qword ptr [rcx], rax
00877A74  E8 0B 20 35 00                  call 0x140bc9a84
00877A79  E8 3E B4 13 00                  call 0x1409b2ebc
00877A7E  41 8B DF                        mov ebx, r15d
00877A81  48 8B CF                        mov rcx, rdi
00877A84  E8 27 B8 FE FF                  call 0x1408632b0
00877A89  4C 39 7D 28                     cmp qword ptr [rbp + 0x28], r15
00877A8D  0F 85 F1 FE FF FF               jne 0x140877984
00877A93  E8 EC 1F 35 00                  call 0x140bc9a84
00877A98  E8 1F B4 13 00                  call 0x1409b2ebc
00877A9D  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
00877AA1  45 8A FE                        mov r15b, r14b
00877AA4  E9 1F FC FF FF                  jmp 0x1408776c8
00877AA9  E8 D6 1F 35 00                  call 0x140bc9a84
00877AAE  E8 09 B4 13 00                  call 0x1409b2ebc
00877AB3  41 B9 04 00 00 00               mov r9d, 4
00877AB9  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00877ABE  4C 8D 45 94                     lea r8, [rbp - 0x6c]
00877AC2  48 8D 15 DF DE 67 00            lea rdx, [rip + 0x67dedf]
00877AC9  48 8D 0D D0 DE 67 00            lea rcx, [rip + 0x67ded0]
00877AD0  E8 CB C8 A2 FF                  call 0x1402a43a0
00877AD5  E8 26 A8 13 00                  call 0x1409b2300
00877ADA  41 8A CE                        mov cl, r14b
00877ADD  E8 02 D0 13 00                  call 0x1409b4ae4
00877AE2  E9 7F FC FF FF                  jmp 0x140877766
00877AE7  E8 98 1F 35 00                  call 0x140bc9a84
00877AEC  E8 CB B3 13 00                  call 0x1409b2ebc
00877AF1  48 8B CF                        mov rcx, rdi
00877AF4  E8 B7 B7 FE FF                  call 0x1408632b0
00877AF9  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
00877B01  B8 43 00 00 C0                  mov eax, 0xc0000043
00877B06  8B D8                           mov ebx, eax
00877B08  44 8B C8                        mov r9d, eax
00877B0B  33 D2                           xor edx, edx
00877B0D  48 8B CE                        mov rcx, rsi
00877B10  44 8D 42 20                     lea r8d, [rdx + 0x20]
00877B14  E8 3B 74 BF FF                  call 0x14046ef54
00877B19  E9 6B FE FF FF                  jmp 0x140877989
00877B1E  E8 61 1F 35 00                  call 0x140bc9a84
00877B23  E8 94 B3 13 00                  call 0x1409b2ebc
00877B28  48 8B CF                        mov rcx, rdi
00877B2B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00877B30  E8 7B B7 FE FF                  call 0x1408632b0
00877B35  E9 4F FE FF FF                  jmp 0x140877989
00877B3A  E8 45 1F 35 00                  call 0x140bc9a84
00877B3F  E8 78 B3 13 00                  call 0x1409b2ebc
00877B44  48 8B CF                        mov rcx, rdi
00877B47  E8 64 B7 FE FF                  call 0x1408632b0
00877B4C  C7 44 24 20 60 00 00 00         mov dword ptr [rsp + 0x20], 0x60
00877B54  EB AB                           jmp 0x140877b01
00877B56  33 D2                           xor edx, edx
00877B58  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
00877B60  44 8B C8                        mov r9d, eax
00877B63  48 8B CE                        mov rcx, rsi
00877B66  44 8D 42 20                     lea r8d, [rdx + 0x20]
00877B6A  E8 E5 73 BF FF                  call 0x14046ef54
00877B6F  45 33 FF                        xor r15d, r15d
00877B72  E9 12 FE FF FF                  jmp 0x140877989
00877B77  48 8B D0                        mov rdx, rax
00877B7A  48 8D 4D 08                     lea rcx, [rbp + 8]
00877B7E  E8 59 D1 A2 FF                  call 0x1402a4cdc
00877B83  E9 D6 F7 FF FF                  jmp 0x14087735e
00877B88  48 8B 05 E1 23 59 00            mov rax, qword ptr [rip + 0x5923e1]
00877B8F  48 23 C2                        and rax, rdx
00877B92  48 3B 05 D7 23 59 00            cmp rax, qword ptr [rip + 0x5923d7]
00877B99  41 8A C6                        mov al, r14b
00877B9C  0F 85 CC FC FF FF               jne 0x14087786e
00877BA2  E9 CA FC FF FF                  jmp 0x140877871
00877BA7  48 8B 05 C2 23 59 00            mov rax, qword ptr [rip + 0x5923c2]
00877BAE  48 23 C2                        and rax, rdx
00877BB1  48 3B 05 B8 23 59 00            cmp rax, qword ptr [rip + 0x5923b8]
00877BB8  41 8A C6                        mov al, r14b
00877BBB  0F 85 F8 F7 FF FF               jne 0x1408773b9
00877BC1  E9 F6 F7 FF FF                  jmp 0x1408773bc
00877BC6  48 8B C1                        mov rax, rcx
00877BC9  49 23 C0                        and rax, r8
00877BCC  48 3B C1                        cmp rax, rcx
00877BCF  41 8A C6                        mov al, r14b
00877BD2  0F 85 16 F9 FF FF               jne 0x1408774ee
00877BD8  E9 14 F9 FF FF                  jmp 0x1408774f1
00877BDD  48 8B C1                        mov rax, rcx
00877BE0  83 E0 08                        and eax, 8
00877BE3  48 3B C1                        cmp rax, rcx
00877BE6  0F 84 AF FA FF FF               je 0x14087769b
00877BEC  E9 A7 FA FF FF                  jmp 0x140877698
00877BF1  B8 FE FF 00 00                  mov eax, 0xfffe
00877BF6  66 41 01 00                     add word ptr [r8], ax
00877BFA  85 D2                           test edx, edx
00877BFC  0F 85 DE F4 FF FF               jne 0x1408770e0
00877C02  E9 F3 F4 FF FF                  jmp 0x1408770fa
00877C07  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00877C0C  E9 D0 FE 29 00                  jmp 0x140b17ae1
00877C11  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00877C16  E9 BC FE 29 00                  jmp 0x140b17ad7
00877C1B  BB 89 01 00 C0                  mov ebx, 0xc0000189
00877C20  45 33 FF                        xor r15d, r15d
00877C23  E9 33 F8 FF FF                  jmp 0x14087745b
00877C28  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
00877C2D  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
00877C31  44 88 75 E8                     mov byte ptr [rbp - 0x18], r14b
00877C35  E9 0A F6 FF FF                  jmp 0x140877244
00877C3A  48 8D 0D 4F DD 67 00            lea rcx, [rip + 0x67dd4f]
00877C41  E9 5F F6 FF FF                  jmp 0x1408772a5
00877C46  E8 39 1E 35 00                  call 0x140bc9a84
00877C4B  E8 6C B2 13 00                  call 0x1409b2ebc
00877C50  45 8A FE                        mov r15b, r14b
00877C53  E9 70 FA FF FF                  jmp 0x1408776c8
00877C58  48 8B CF                        mov rcx, rdi
00877C5B  E8 50 B6 FE FF                  call 0x1408632b0
00877C60  E9 2E FE FF FF                  jmp 0x140877a93
00877C65  66 44 39 7E 0A                  cmp word ptr [rsi + 0xa], r15w
00877C6A  0F 85 FA F7 FF FF               jne 0x14087746a
00877C70  44 38 BE 8A 01 00 00            cmp byte ptr [rsi + 0x18a], r15b
00877C77  0F 85 ED F7 FF FF               jne 0x14087746a
00877C7D  E9 55 FE 29 00                  jmp 0x140b17ad7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmLoadAppKey(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned __int8 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int8 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m288;
    unsigned int v_stack_m290;
    unsigned int v_stack_m294;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned int v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C8;
    unsigned int v_stack_m2CC;
    unsigned int v_stack_m2D0;
    unsigned __int8 v_stack_m2D2;
    unsigned __int8 v_stack_m2D4;
    unsigned __int8 v_stack_m2D8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned int v_stack_m318;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned __int64 v_stack_p65;
    unsigned __int8 v_stack_p66;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (768);
    result = (*(unsigned __int64 *)(v_rip + 5846814)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m2C0 = a5;
    v_stack_m1E0 = a6;
    v_stack_m1E8 = a9;
    v_stack_m2CC = a3;
    v_stack_m288 = a2;
    a2 = 0;
    v_stack_m2B8 = a1;
    v_stack_m208 = a10;
    v_stack_m220 = a7;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    result = memset(v_stack_m278, a2, v_r14 + 80, a4);
    v_stack_m2D4 = 0;
    v_stack_m1C8 = v_xmm0;
    v_stack_m2D8 = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m2D2 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m2A0 = 0;
    v_stack_m210 = 0;
    v_stack_m1D8 = v_xmm0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16)))) < ((unsigned __int16)(v_r14 + 2))) goto loc_008770FA;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16))))) >> (1));
    if (condition_is_equal) goto loc_008770FA;
loc_008770E0:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + (unsigned int)((unsigned int)(a2 - 1)) * 2)) == 92) goto loc_00877BF1;
loc_008770FA:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16))) < 2) goto loc_00877C07;
    result = CmpAllocatePool(256, 432, (unsigned int)(0x33394D43ULL), a4);
    if (result == 0) goto loc_00877C11;
    result = CmpAcquireHiveLoadUnloadRundown(256, 432, (unsigned int)(0x33394D43ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00877C1B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m2CC)))) & (32));
    v_stack_m2F0 = result;
    v_stack_m294 = (unsigned int)(result);
    result = (unsigned int)(-(result));
    a1 = (unsigned int)((256) & (0x4000000ULL));
    a1 = (unsigned int)((a1) + (0x3190001ULL));
    a2 = (unsigned int)((unsigned int)(a1));
    if ((((unsigned __int8)((unsigned int)(v_stack_m2CC))) & (128)) == 0) { a2 = (unsigned int)(a1); }
    a1 = (unsigned int)((unsigned int)(a2));
    if (condition_is_above_or_equal) { a1 = (unsigned int)(a2); }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m2CC)))) & (0x2000ULL));
    v_stack_m298 = (unsigned int)(a1);
    a1 = (condition_is_not_equal) ? 1 : 0;
    v_stack_m2D0 = (unsigned int)(result);
    v_stack_m2F8 = v_stack_m2A0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (32));
    if (condition_is_above_or_equal) { a2 = (unsigned int)(a1); }
    v_stack_m2C8 = (unsigned int)(a2);
    a2 = 0;
    v_stack_m310 = a7;
    v_stack_m318 = 8;
    result = CmpOpenHiveFile(v_stack_m288, a2, v_stack_m2B0, v_stack_m2A8);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00877C28;
    a2 = 0;
    if (sign_flag) goto loc_008774B6;
    a4 = 0;
    v_stack_m318 = v_stack_m228;
    result = ObReferenceObjectByHandle(v_stack_m2B0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6818408)), a4);
    result = ZwClose(v_stack_m2B0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6818408)), a4);
    if (sign_flag) goto loc_0087731B;
    v_stack_m258 = *(unsigned __int64 *)(v_stack_m228 + 40);
    v_stack_m250 = 0;
loc_00877244:
    a3 = 0;
    a2 = 0;
    result = KeInitializeEvent(v_stack_m248, a2, a3, a4);
    v_stack_m260 = v_stack_m268;
    v_stack_m268 = v_stack_m268;
    result = CmpLockAppHiveLoadList(v_stack_m248, a2, a3, a4);
loc_00877279:
    if ((*(unsigned __int64 *)(v_rip + 6809374)) != (v_rip + 6809367)) goto loc_00877295;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809363))) == (v_rip + 6809367)) goto loc_008776A9;
loc_0087728E:
loc_00877295:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 6809374) + 40)) != 0) goto loc_008772AA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809374) + 32)) == v_stack_m258) goto loc_008772C1;
loc_008772A5:
    goto loc_00877279;
loc_008772AA:
    result = RtlEqualUnicodeString(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809374)) + 32), v_stack_m288, (unsigned __int8)(2 - 1), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00877C3A;
loc_008772C1:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809374))) + (16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809374)) + 24))) != v_rbx) goto loc_0087728E;
    v_stack_m260 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809374)) + 24);
    v_stack_m268 = v_rbx;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6809374)) + 24)) = v_stack_m268;
    *(unsigned __int64 *)(v_rbx + 8) = v_stack_m268;
    result = ExAcquireRundownProtection(v_stack_m260 + 56, v_stack_m288, (unsigned __int8)(2 - 1), a4);
    result = CmpUnlockAppHiveLoadList(v_stack_m260 + 56, v_stack_m288, (unsigned __int8)(2 - 1), a4);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_m260 + 32, a2, a3, a4);
    result = ExReleaseRundownProtection(v_stack_m260 + 56, a2, a3, a4);
    goto loc_008776C8;
loc_0087731B:
    v_stack_m318 = 32;
    a2 = 0;
    result = SetFailureLocation(result, a2, 32, (unsigned int)((unsigned int)(v_stack_m260)));
    v_r15 = 0;
    goto loc_0087736B;
loc_00877339:
    result = CmpUnlockAppHiveLoadList(result, a2, 32, (unsigned int)((unsigned int)(v_stack_m260)));
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_m248, a2, a3, (unsigned int)((unsigned int)(v_stack_m260)));
    result = 0;
    if (0 >= 2) goto loc_00877B77;
loc_0087735E:
    if (0 != 0) {
        a1 = 0;
        result = CmpDereferenceHive(a1, a2, a3, (unsigned int)((unsigned int)(v_stack_m260)));
    }
    if (v_stack_m228 != 0) {
        a1 = v_stack_m228;
        result = ObfDereferenceObject(a1, a2, a3, (unsigned int)((unsigned int)(v_stack_m260)));
    }
    if (v_stack_m2A0 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m2A0, a2, a3, (unsigned int)((unsigned int)(v_stack_m260)));
    }
    result = CmpReleaseHiveLoadUnloadRundown(v_stack_m2A0, a2, a3, (unsigned int)((unsigned int)(v_stack_m260)));
    if (sign_flag) goto loc_0087745B;
    if ((*(unsigned int *)(v_rip + 5843900)) <= 5) goto loc_00877481;
    if (((*(unsigned __int64 *)(v_rip + 5843893)) & (0)) != 0) goto loc_00877BA7;
loc_008773B9:
loc_008773BC:
    if (0 == 0) goto loc_00877481;
    v_stack_m2B8 = 2 - 1;
    v_stack_m178 = v_stack_m2B8;
    v_stack_m170 = 8;
    v_stack_m168 = v_stack_m2D0;
    v_stack_m2D8 = (unsigned __int8)(v_stack_m2D2);
    v_stack_m158 = v_stack_m2D8;
    v_stack_m148 = v_stack_m2C0;
    v_stack_m318 = v_stack_m198;
    v_stack_m2D0 = (unsigned int)(v_stack_m260);
    v_stack_m160 = 4;
    v_stack_m150 = 2 - 1;
    v_stack_m2C0 = 0x1000000ULL;
    v_stack_m140 = 8;
    result = tlgWriteAgg(v_rip + 5843808, v_rip - 8522537, a3, 6);
    goto loc_00877481;
loc_0087745B:
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 8)) == 0) goto loc_00877C65;
loc_0087746A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5843688)))) > 5) goto loc_008774D7;
loc_0087747C:
    if (result != 0) {
        a1 = result;
        result = CmSiFreeMemory(a1, (unsigned int)(*(unsigned int *)(v_rip + 5843688)), a3, 6);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(v_rip + 5843688)), a3, 6);
    v_rsp = (v_rsp) + (768);
    return result;
loc_008774B6:
    v_stack_p20 = 16;
    result = SetFailureLocation(result, (unsigned int)(*(unsigned int *)(v_rip + 5843688)), 32, (unsigned int)((unsigned int)(result)));
    v_r15 = 0;
    goto loc_00877378;
loc_008774D7:
    if (((*(unsigned __int64 *)(v_rip + 5843584)) & (32)) != 0) goto loc_00877BC6;
loc_008774EE:
loc_008774F1:
    result = 0;
    if (0 != 0) {
        a2 = result + 10;
        v_stack_m2B8 = 2 - 1;
        a4 = *(unsigned __int16 *)(a2);
        a3 = result + 394;
        v_r10 = *(unsigned __int8 *)(a3);
        a1 = *(unsigned __int16 *)(result + 8) + *(unsigned __int16 *)(result + 8) * 2;
        result = v_stack_m2B8;
        a1 = (unsigned int)((a1) << (2));
        v_stack_m178 = result;
        result = v_stack_p68;
        v_stack_m168 = result;
        result = v_stack_p60;
        v_stack_m158 = result;
        result = v_stack_p70;
        v_stack_m148 = result;
        result = v_stack_p6C;
        v_stack_m138 = result;
        result = result + 8;
        v_stack_m128 = result;
        result = result + 12;
        v_stack_m118 = result;
        result = result + 108;
        v_stack_mF8 = result;
        result = a4 + a4 * 2;
        result = (unsigned int)((result) << (2));
        v_stack_mF0 = (unsigned int)(result);
        result = result + 396;
        v_stack_mD8 = result;
        result = v_stack_p78;
        v_stack_mC8 = result;
        result = v_stack_m198;
        v_stack_p6C = (unsigned __int16)(v_r10);
        v_stack_p70 = (unsigned __int16)(a4);
        a4 = 14;
        v_stack_m110 = (unsigned int)(a1);
        a1 = v_rip + 5843352;
        v_stack_m108 = a2;
        a2 = v_rip - 8523814;
        v_r10 = (unsigned int)((v_r10) << (3));
        v_stack_p20 = result;
        v_stack_m170 = 8;
        v_stack_p68 = (unsigned int)(v_stack_p20);
        v_stack_m160 = 4;
        v_stack_p60 = (unsigned __int16)(*(unsigned __int16 *)(result + 8));
        v_stack_m150 = 2;
        v_stack_m140 = 2;
        v_stack_m130 = 2;
        v_stack_m120 = 2;
        v_stack_m10C = 0;
        v_stack_m100 = 2;
        v_stack_mEC = 0;
        v_stack_mE8 = a3;
        v_stack_mE0 = 2;
        v_stack_mD0 = (unsigned int)(v_r10);
        v_stack_mCC = 0;
        v_stack_p78 = 0x1000000ULL;
        v_stack_mC0 = 8;
        result = tlgWriteAgg(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 5843188);
        a2 = *(unsigned int *)(v_rip + 5843158);
    }
    if (((unsigned int)(a2)) <= 5) goto loc_0087747C;
    if (((*(unsigned __int8 *)(v_rip + 5843158)) & (8)) != 0) goto loc_00877BDD;
loc_00877698:
loc_0087769B:
    if (0 == 0) goto loc_0087747C;
loc_008776A9:
    v_stack_m278 = a1;
    v_stack_m270 = result;
    *(unsigned __int64 *)(result) = v_stack_m278;
    *(unsigned __int64 *)(v_rip + 6808277) = v_stack_m278;
    result = CmpUnlockAppHiveLoadList(v_stack_m278, a2, a3, a4);
loc_008776C8:
    v_stack_p40 = result;
    v_stack_p38 = v_stack_p64;
    v_stack_p30 = v_stack_m220;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p70));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m298));
    v_stack_p65 = 0;
    v_stack_p64 = 0;
    result = CmpCmdHiveOpen(v_stack_m288, 0, v_stack_p65, v_stack_m200);
    if ((unsigned int)(result) == 0) goto loc_00877930;
    if (((unsigned int)(result)) != 0xC0000043ULL) goto loc_00877B56;
    if (v_stack_m294 != 0) goto loc_00877B56;
    if (0 != 0) goto loc_00877B56;
    v_r15 = 0;
    result = LOCK_HIVE_LOAD(v_stack_m288, 0, v_stack_p65, v_stack_m200);
    result = CmpLockRegistryFreezeAware(0, 0, v_stack_p65, v_stack_m200);
    result = CmpGetLastHive(0, 0, v_stack_p65, v_stack_m200);
    if (result == 0) goto loc_00877C46;
loc_00877766:
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6808124)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6808124))) != 0) goto loc_00877AA9;
    a1 = 0;
loc_00877779:
    result = CmpGetNextHive(a1, 0, v_stack_p65, v_stack_m200);
    if (result == 0) goto loc_00877A93;
    v_stack_m290 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4768)));
    v_r15 = 0;
    if (*(unsigned __int64 *)(result + 1544) != 0) goto loc_008777BC;
    if (result == result) goto loc_00877C58;
loc_008777B7:
    goto loc_00877779;
loc_008777BC:
    result = CmpIsThisSameFile(v_stack_m228, *(unsigned __int64 *)(result + 1544), v_stack_p65, v_stack_m200);
    if ((unsigned __int8)(result) != 0) goto loc_008777D2;
    if (result != result) goto loc_008777B7;
    goto loc_00877A81;
loc_008777D2:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 160))) & (0x8000ULL));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4112)))) & (32)) == 0) goto loc_00877B3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4112)))) & (64)) != 0) goto loc_00877B3A;
    a2 = 0;
    result = CmpSplitParentKeyName(result + 1840, a2, v_stack_m1D8, v_stack_m200);
    if ((*(unsigned int *)(v_rip + 5842763)) > 5) goto loc_00877857;
loc_0087780F:
    if (v_stack_p68 == 0) goto loc_00877A20;
    if ((unsigned int)(v_rbx) != 0) goto loc_00877A28;
    result = CmpCheckHivePrimaryFileReadWriteAccess(v_stack_m2A0, a2, v_stack_m1D8, v_stack_m200);
    if ((unsigned __int8)(result) != 0) goto loc_00877A28;
    result = CmpUnlockRegistry(v_stack_m2A0, a2, v_stack_m1D8, v_stack_m200);
    result = UNLOCK_HIVE_LOAD(v_stack_m2A0, a2, v_stack_m1D8, v_stack_m200);
    result = CmpDereferenceHive(result, a2, v_stack_m1D8, v_stack_m200);
    v_stack_p20 = 128;
loc_00877857:
    if (((*(unsigned __int64 *)(v_rip + 5842688)) & (0)) != 0) goto loc_00877B88;
loc_0087786E:
loc_00877871:
    if (0 == 0) goto loc_0087780F;
    v_stack_m1F8 = 0;
    v_stack_m98 = v_stack_m1F8;
    v_stack_m90 = 8;
    result = PsGetProcessImageFileName(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, v_stack_m1D8, v_stack_m200);
    result = tlgCreate1Sz_char(v_stack_m88, result, v_stack_m1D8, v_stack_m200);
    v_stack_m68 = v_stack_m1D0;
    v_stack_m60 = (unsigned int)(v_stack_m1D8);
    v_stack_m58 = v_stack_m1F0;
    v_stack_m78 = v_stack_m60;
    v_stack_p20 = v_stack_mB8;
    v_stack_m70 = 2;
    v_stack_m5C = 0;
    v_stack_m1F0 = 0x1000000ULL;
    v_stack_m50 = 8;
    result = tlgWriteAgg(v_rip + 5842524, v_rip - 8524994, v_stack_m1D8, 7);
    goto loc_0087780F;
loc_00877930:
    v_r15 = 0;
    v_stack_p50 = result;
    v_stack_p48 = (unsigned __int8)(v_stack_p64);
    v_stack_p40 = (unsigned __int8)(v_stack_p65);
    v_stack_p38 = v_stack_m208;
    v_stack_p30 = a8;
    v_stack_p28 = v_stack_m1E0;
    v_stack_p20 = 0;
    result = CmpLoadKeyCommon(v_stack_m200, v_stack_m2B8, (unsigned int)(v_stack_p6C), v_stack_p78);
    goto loc_00877989;
loc_00877984:
    v_stack_p66 = 0;
loc_00877989:
    result = CmpLockAppHiveLoadList(v_stack_m200, v_stack_m2B8, (unsigned int)(v_stack_p6C), v_stack_p78);
    if ((*(unsigned __int64 *)(v_stack_m278 + 8)) != v_stack_m278) goto loc_0087728E;
    if ((*(unsigned __int64 *)(v_stack_m270)) != v_stack_m278) goto loc_0087728E;
    *(unsigned __int64 *)(v_stack_m270) = v_stack_m278;
    *(unsigned __int64 *)(v_stack_m278 + 8) = v_stack_m270;
    if (v_stack_m268 == v_stack_m268) goto loc_00877339;
    if ((*(unsigned __int64 *)(v_stack_m268 + 8)) != v_stack_m268) goto loc_0087728E;
    if ((*(unsigned __int64 *)(v_stack_m260)) != v_stack_m268) goto loc_0087728E;
    *(unsigned __int64 *)(v_stack_m260) = v_stack_m268;
    *(unsigned __int64 *)(v_stack_m268 + 8) = v_stack_m260;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6807447))) != (v_rip + 6807446)) goto loc_0087728E;
    *(unsigned __int64 *)(v_stack_m268 - 16) = v_rip + 6807446;
    *(unsigned __int64 *)(v_stack_m268 - 16 + 8) = *(unsigned __int64 *)(v_rip + 6807447);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6807447)) = v_stack_m268 - 16;
    *(unsigned __int64 *)(v_rip + 6807421) = v_stack_m268 - 16;
    goto loc_00877339;
loc_00877A20:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00877AE7;
loc_00877A28:
    result = CmpAttachToRegistryProcess(v_stack_m1C8, v_rip + 6807446, v_stack_m268, v_stack_p78);
    v_stack_m210 = result;
    result = CmpConstructName(*(unsigned __int64 *)(result + 2936), v_rip + 6807446, v_stack_m268, v_stack_p78);
    *(unsigned __int64 *)(v_stack_m1E8) = result;
    result = CmpDetachFromRegistryProcess(v_stack_m1C8, v_rip + 6807446, v_stack_m268, v_stack_p78);
    if ((*(unsigned __int64 *)(v_stack_m1E8)) == 0) goto loc_00877B1E;
    result = CmpReferenceKeyControlBlockUnsafe(*(unsigned __int64 *)(result + 2936), v_rip + 6807446, v_stack_m268, v_stack_p78);
    *(unsigned __int64 *)(v_stack_m208) = *(unsigned __int64 *)(result + 2936);
    result = CmpUnlockRegistry(v_stack_m208, v_rip + 6807446, v_stack_m268, v_stack_p78);
    result = UNLOCK_HIVE_LOAD(v_stack_m208, v_rip + 6807446, v_stack_m268, v_stack_p78);
loc_00877A81:
    result = CmpDereferenceHive(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    if (v_stack_m210 != 0) goto loc_00877984;
loc_00877A93:
    result = CmpUnlockRegistry(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    result = UNLOCK_HIVE_LOAD(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    goto loc_008776C8;
loc_00877AA9:
    result = CmpUnlockRegistry(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    result = UNLOCK_HIVE_LOAD(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    v_stack_p20 = 0;
    result = ExBlockOnAddressPushLock(v_rip + 6807248, v_rip + 6807263, v_stack_m2A4, 4);
    result = LOCK_HIVE_LOAD(v_rip + 6807248, v_rip + 6807263, v_stack_m2A4, 4);
    result = CmpLockRegistryFreezeAware(0, v_rip + 6807263, v_stack_m2A4, 4);
    goto loc_00877766;
loc_00877AE7:
    result = CmpUnlockRegistry(0, v_rip + 6807263, v_stack_m2A4, 4);
    result = UNLOCK_HIVE_LOAD(0, v_rip + 6807263, v_stack_m2A4, 4);
    result = CmpDereferenceHive(v_stack_m288, v_rip + 6807263, v_stack_m2A4, 4);
    v_stack_p20 = 112;
loc_00877B01:
    a2 = 0;
    result = SetFailureLocation(result, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    goto loc_00877989;
loc_00877B1E:
    result = CmpUnlockRegistry(result, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    result = UNLOCK_HIVE_LOAD(result, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    result = CmpDereferenceHive(v_stack_m288, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    goto loc_00877989;
loc_00877B3A:
    result = CmpUnlockRegistry(v_stack_m288, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    result = UNLOCK_HIVE_LOAD(v_stack_m288, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    result = CmpDereferenceHive(v_stack_m288, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(0xC0000043ULL))));
    v_stack_p20 = 96;
    goto loc_00877B01;
loc_00877B56:
    a2 = 0;
    v_stack_p20 = 48;
    result = SetFailureLocation(result, a2, a2 + 32, (unsigned int)((unsigned int)(result)));
    v_r15 = 0;
    goto loc_00877989;
loc_00877B77:
    result = ExfWaitForRundownProtectionRelease(v_stack_m230, result, a2 + 32, (unsigned int)((unsigned int)(result)));
    goto loc_0087735E;
loc_00877B88:
    result = (*(unsigned __int64 *)(v_rip + 5841889)) & (result);
    if (result != (*(unsigned __int64 *)(v_rip + 5841879))) goto loc_0087786E;
    goto loc_00877871;
loc_00877BA7:
    result = (*(unsigned __int64 *)(v_rip + 5841858)) & (result);
    if (result != (*(unsigned __int64 *)(v_rip + 5841848))) goto loc_008773B9;
    goto loc_008773BC;
loc_00877BC6:
    result = (v_stack_m230) & (a2 + 32);
    if (result != v_stack_m230) goto loc_008774EE;
    goto loc_008774F1;
loc_00877BDD:
    result = (unsigned int)((v_stack_m230) & (8));
    if (result == v_stack_m230) goto loc_0087769B;
    goto loc_00877698;
loc_00877BF1:
    if ((unsigned int)(result) != 0) goto loc_008770E0;
    goto loc_008770FA;
loc_00877C07:
loc_00877C11:
loc_00877C1B:
    v_r15 = 0;
    goto loc_0087745B;
loc_00877C28:
    v_stack_p60 = 0;
    v_stack_m258 = v_stack_m288;
    v_stack_m250 = 0;
    goto loc_00877244;
loc_00877C3A:
    goto loc_008772A5;
loc_00877C46:
    result = CmpUnlockRegistry(v_rip + 6806863, result, a2 + 32, (unsigned int)((unsigned int)(result)));
    result = UNLOCK_HIVE_LOAD(v_rip + 6806863, result, a2 + 32, (unsigned int)((unsigned int)(result)));
    goto loc_008776C8;
loc_00877C58:
    result = CmpDereferenceHive(v_stack_m288, result, a2 + 32, (unsigned int)((unsigned int)(result)));
    goto loc_00877A93;
loc_00877C65:
    if ((*(unsigned __int16 *)(result + 10)) != 0) goto loc_0087746A;
    if ((*(unsigned __int8 *)(result + 394)) != 0) goto loc_0087746A;
}
```

## 5. (Beta) C Style

```c
int64_t CmLoadAppKey(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint8_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m248;
    uint8_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m288;
    uint32_t v_stack_m290;
    uint32_t v_stack_m294;
    uint32_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint32_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C8;
    uint32_t v_stack_m2CC;
    uint32_t v_stack_m2D0;
    uint8_t v_stack_m2D2;
    uint8_t v_stack_m2D4;
    uint8_t v_stack_m2D8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint32_t v_stack_m318;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p64;
    uint64_t v_stack_p65;
    uint8_t v_stack_p66;
    uint64_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (768);
    result = (*(uint64_t *)(v_rip + 0x59371E)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m2C0 = Arg5;
    v_stack_m1E0 = Arg6;
    v_stack_m1E8 = Arg9;
    v_stack_m2CC = Arg3;
    v_stack_m288 = Arg2;
    Arg2 = 0;
    v_stack_m2B8 = Arg1;
    v_stack_m208 = Arg10;
    v_stack_m220 = Arg7;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    result = memset(v_stack_m278, Arg2, local_r14 + 80, Arg4);
    v_stack_m2D4 = 0;
    v_stack_m1C8 = v_xmm0;
    v_stack_m2D8 = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m2D2 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m2A0 = 0;
    v_stack_m210 = 0;
    v_stack_m1D8 = v_xmm0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10)))) < ((uint16_t)(local_r14 + 2))) goto loc_008770FA;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10))))) >> (1));
    if (condition_is_equal) goto loc_008770FA;
loc_008770E0:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + (uint32_t)((uint32_t)(Arg2 - 0x1)) * 2)) == 92) goto loc_00877BF1;
loc_008770FA:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x10))) < 2) goto loc_00877C07;
    result = CmpAllocatePool(256, 432, (uint32_t)(0x33394D43ULL), Arg4);
    if (result == 0) goto loc_00877C11;
    result = CmpAcquireHiveLoadUnloadRundown(256, 432, (uint32_t)(0x33394D43ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00877C1B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m2CC)))) & (32));
    v_stack_m2F0 = result;
    v_stack_m294 = (uint32_t)(result);
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)((256) & (0x4000000ULL));
    Arg1 = (uint32_t)((Arg1) + (0x3190001ULL));
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if ((((uint8_t)((uint32_t)(v_stack_m2CC))) & (128)) == 0) { Arg2 = (uint32_t)(Arg1); }
    Arg1 = (uint32_t)((uint32_t)(Arg2));
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(Arg2); }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m2CC)))) & (0x2000ULL));
    v_stack_m298 = (uint32_t)(Arg1);
    Arg1 = (condition_is_not_equal) ? 1 : 0;
    v_stack_m2D0 = (uint32_t)(result);
    v_stack_m2F8 = v_stack_m2A0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (32));
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(Arg1); }
    v_stack_m2C8 = (uint32_t)(Arg2);
    Arg2 = 0;
    v_stack_m310 = Arg7;
    v_stack_m318 = 8;
    result = CmpOpenHiveFile(v_stack_m288, Arg2, v_stack_m2B0, v_stack_m2A8);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00877C28;
    Arg2 = 0;
    if (sign_flag) goto loc_008774B6;
    Arg4 = 0;
    v_stack_m318 = v_stack_m228;
    result = ObReferenceObjectByHandle(v_stack_m2B0, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x680A68)), Arg4);
    result = ZwClose(v_stack_m2B0, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x680A68)), Arg4);
    if (sign_flag) goto loc_0087731B;
    v_stack_m258 = *(uint64_t *)(v_stack_m228 + 0x28);
    v_stack_m250 = 0;
loc_00877244:
    Arg3 = 0;
    Arg2 = 0;
    result = KeInitializeEvent(v_stack_m248, Arg2, Arg3, Arg4);
    v_stack_m260 = v_stack_m268;
    v_stack_m268 = v_stack_m268;
    result = CmpLockAppHiveLoadList(v_stack_m248, Arg2, Arg3, Arg4);
loc_00877279:
    if ((*(uint64_t *)(v_rip + 0x67E71E)) != (v_rip + 6809367)) goto loc_00877295;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E713))) == (v_rip + 6809367)) goto loc_008776A9;
loc_0087728E:
loc_00877295:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x67E71E) + 0x28)) != 0) goto loc_008772AA;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E71E) + 0x20)) == v_stack_m258) goto loc_008772C1;
loc_008772A5:
    goto loc_00877279;
loc_008772AA:
    result = RtlEqualUnicodeString(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E71E)) + 0x20), v_stack_m288, (uint8_t)(2 - 1), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00877C3A;
loc_008772C1:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E71E))) + (16);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E71E)) + 0x18))) != local_rbx) goto loc_0087728E;
    v_stack_m260 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E71E)) + 0x18);
    v_stack_m268 = local_rbx;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x67E71E)) + 0x18)) = v_stack_m268;
    *(uint64_t *)(local_rbx + 0x8) = v_stack_m268;
    result = ExAcquireRundownProtection(v_stack_m260 + 56, v_stack_m288, (uint8_t)(2 - 1), Arg4);
    result = CmpUnlockAppHiveLoadList(v_stack_m260 + 56, v_stack_m288, (uint8_t)(2 - 1), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_m260 + 32, Arg2, Arg3, Arg4);
    result = ExReleaseRundownProtection(v_stack_m260 + 56, Arg2, Arg3, Arg4);
    goto loc_008776C8;
loc_0087731B:
    v_stack_m318 = 32;
    Arg2 = 0;
    result = SetFailureLocation(result, Arg2, 32, (uint32_t)((uint32_t)(v_stack_m260)));
    local_r15 = 0;
    goto loc_0087736B;
loc_00877339:
    result = CmpUnlockAppHiveLoadList(result, Arg2, 32, (uint32_t)((uint32_t)(v_stack_m260)));
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_m248, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m260)));
    result = 0;
    if (0 >= 2) goto loc_00877B77;
loc_0087735E:
    if (0 != 0) {
        Arg1 = 0;
        result = CmpDereferenceHive(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m260)));
    }
    if (v_stack_m228 != 0) {
        Arg1 = v_stack_m228;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m260)));
    }
    if (v_stack_m2A0 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m2A0, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m260)));
    }
    result = CmpReleaseHiveLoadUnloadRundown(v_stack_m2A0, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m260)));
    if (sign_flag) goto loc_0087745B;
    if ((*(uint32_t *)(v_rip + 0x592BBC)) <= 5) goto loc_00877481;
    if (((*(uint64_t *)(v_rip + 0x592BB5)) & (0)) != 0) goto loc_00877BA7;
loc_008773B9:
loc_008773BC:
    if (0 == 0) goto loc_00877481;
    v_stack_m2B8 = 2 - 1;
    v_stack_m178 = v_stack_m2B8;
    v_stack_m170 = 8;
    v_stack_m168 = v_stack_m2D0;
    v_stack_m2D8 = (uint8_t)(v_stack_m2D2);
    v_stack_m158 = v_stack_m2D8;
    v_stack_m148 = v_stack_m2C0;
    v_stack_m318 = v_stack_m198;
    v_stack_m2D0 = (uint32_t)(v_stack_m260);
    v_stack_m160 = 4;
    v_stack_m150 = 2 - 1;
    v_stack_m2C0 = 0x1000000ULL;
    v_stack_m140 = 8;
    result = tlgWriteAgg(v_rip + 5843808, v_rip - 8522537, Arg3, 6);
    goto loc_00877481;
loc_0087745B:
    if ((uint16_t)(*(uint16_t *)(result + 0x8)) == 0) goto loc_00877C65;
loc_0087746A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x592AE8)))) > 5) goto loc_008774D7;
loc_0087747C:
    if (result != 0) {
        Arg1 = result;
        result = CmSiFreeMemory(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x592AE8)), Arg3, 6);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x592AE8)), Arg3, 6);
    local_rsp = (local_rsp) + (768);
    return result;
loc_008774B6:
    v_stack_p20 = 16;
    result = SetFailureLocation(result, (uint32_t)(*(uint32_t *)(v_rip + 0x592AE8)), 32, (uint32_t)((uint32_t)(result)));
    local_r15 = 0;
    goto loc_00877378;
loc_008774D7:
    if (((*(uint64_t *)(v_rip + 0x592A80)) & (32)) != 0) goto loc_00877BC6;
loc_008774EE:
loc_008774F1:
    result = 0;
    if (0 != 0) {
        Arg2 = result + 10;
        v_stack_m2B8 = 2 - 1;
        Arg4 = *(uint16_t *)(Arg2);
        Arg3 = result + 394;
        local_r10 = *(uint8_t *)(Arg3);
        Arg1 = *(uint16_t *)(result + 0x8) + *(uint16_t *)(result + 0x8) * 2;
        result = v_stack_m2B8;
        Arg1 = (uint32_t)((Arg1) << (2));
        v_stack_m178 = result;
        result = v_stack_p68;
        v_stack_m168 = result;
        result = v_stack_p60;
        v_stack_m158 = result;
        result = v_stack_p70;
        v_stack_m148 = result;
        result = v_stack_p6C;
        v_stack_m138 = result;
        result = result + 8;
        v_stack_m128 = result;
        result = result + 12;
        v_stack_m118 = result;
        result = result + 108;
        v_stack_mF8 = result;
        result = Arg4 + Arg4 * 2;
        result = (uint32_t)((result) << (2));
        v_stack_mF0 = (uint32_t)(result);
        result = result + 396;
        v_stack_mD8 = result;
        result = v_stack_p78;
        v_stack_mC8 = result;
        result = v_stack_m198;
        v_stack_p6C = (uint16_t)(local_r10);
        v_stack_p70 = (uint16_t)(Arg4);
        Arg4 = 14;
        v_stack_m110 = (uint32_t)(Arg1);
        Arg1 = v_rip + 5843352;
        v_stack_m108 = Arg2;
        Arg2 = v_rip - 8523814;
        local_r10 = (uint32_t)((local_r10) << (3));
        v_stack_p20 = result;
        v_stack_m170 = 8;
        v_stack_p68 = (uint32_t)(v_stack_p20);
        v_stack_m160 = 4;
        v_stack_p60 = (uint16_t)(*(uint16_t *)(result + 0x8));
        v_stack_m150 = 2;
        v_stack_m140 = 2;
        v_stack_m130 = 2;
        v_stack_m120 = 2;
        v_stack_m10C = 0;
        v_stack_m100 = 2;
        v_stack_mEC = 0;
        v_stack_mE8 = Arg3;
        v_stack_mE0 = 2;
        v_stack_mD0 = (uint32_t)(local_r10);
        v_stack_mCC = 0;
        v_stack_p78 = 0x1000000ULL;
        v_stack_mC0 = 8;
        result = tlgWriteAgg(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(v_rip + 0x5928F4);
        Arg2 = *(uint32_t *)(v_rip + 0x5928D6);
    }
    if (((uint32_t)(Arg2)) <= 5) goto loc_0087747C;
    if (((*(uint8_t *)(v_rip + 0x5928D6)) & (8)) != 0) goto loc_00877BDD;
loc_00877698:
loc_0087769B:
    if (0 == 0) goto loc_0087747C;
loc_008776A9:
    v_stack_m278 = Arg1;
    v_stack_m270 = result;
    *(uint64_t *)(result) = v_stack_m278;
    *(uint64_t *)(v_rip + 0x67E2D5) = v_stack_m278;
    result = CmpUnlockAppHiveLoadList(v_stack_m278, Arg2, Arg3, Arg4);
loc_008776C8:
    v_stack_p40 = result;
    v_stack_p38 = v_stack_p64;
    v_stack_p30 = v_stack_m220;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p70));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m298));
    v_stack_p65 = 0;
    v_stack_p64 = 0;
    result = CmpCmdHiveOpen(v_stack_m288, 0, v_stack_p65, v_stack_m200);
    if ((uint32_t)(result) == 0) goto loc_00877930;
    if (((uint32_t)(result)) != 0xC0000043ULL) goto loc_00877B56;
    if (v_stack_m294 != 0) goto loc_00877B56;
    if (0 != 0) goto loc_00877B56;
    local_r15 = 0;
    result = LOCK_HIVE_LOAD(v_stack_m288, 0, v_stack_p65, v_stack_m200);
    result = CmpLockRegistryFreezeAware(0, 0, v_stack_p65, v_stack_m200);
    result = CmpGetLastHive(0, 0, v_stack_p65, v_stack_m200);
    if (result == 0) goto loc_00877C46;
loc_00877766:
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x67E23C)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x67E23C))) != 0) goto loc_00877AA9;
    Arg1 = 0;
loc_00877779:
    result = CmpGetNextHive(Arg1, 0, v_stack_p65, v_stack_m200);
    if (result == 0) goto loc_00877A93;
    v_stack_m290 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x12A0)));
    local_r15 = 0;
    if (*(uint64_t *)(result + 0x608) != 0) goto loc_008777BC;
    if (result == result) goto loc_00877C58;
loc_008777B7:
    goto loc_00877779;
loc_008777BC:
    result = CmpIsThisSameFile(v_stack_m228, *(uint64_t *)(result + 0x608), v_stack_p65, v_stack_m200);
    if ((uint8_t)(result) != 0) goto loc_008777D2;
    if (result != result) goto loc_008777B7;
    goto loc_00877A81;
loc_008777D2:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xA0))) & (0x8000ULL));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x1010)))) & (32)) == 0) goto loc_00877B3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x1010)))) & (64)) != 0) goto loc_00877B3A;
    Arg2 = 0;
    result = CmpSplitParentKeyName(result + 1840, Arg2, v_stack_m1D8, v_stack_m200);
    if ((*(uint32_t *)(v_rip + 0x59274B)) > 5) goto loc_00877857;
loc_0087780F:
    if (v_stack_p68 == 0) goto loc_00877A20;
    if ((uint32_t)(local_rbx) != 0) goto loc_00877A28;
    result = CmpCheckHivePrimaryFileReadWriteAccess(v_stack_m2A0, Arg2, v_stack_m1D8, v_stack_m200);
    if ((uint8_t)(result) != 0) goto loc_00877A28;
    result = CmpUnlockRegistry(v_stack_m2A0, Arg2, v_stack_m1D8, v_stack_m200);
    result = UNLOCK_HIVE_LOAD(v_stack_m2A0, Arg2, v_stack_m1D8, v_stack_m200);
    result = CmpDereferenceHive(result, Arg2, v_stack_m1D8, v_stack_m200);
    v_stack_p20 = 128;
loc_00877857:
    if (((*(uint64_t *)(v_rip + 0x592700)) & (0)) != 0) goto loc_00877B88;
loc_0087786E:
loc_00877871:
    if (0 == 0) goto loc_0087780F;
    v_stack_m1F8 = 0;
    v_stack_m98 = v_stack_m1F8;
    v_stack_m90 = 8;
    result = PsGetProcessImageFileName(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, v_stack_m1D8, v_stack_m200);
    result = tlgCreate1Sz_char(v_stack_m88, result, v_stack_m1D8, v_stack_m200);
    v_stack_m68 = v_stack_m1D0;
    v_stack_m60 = (uint32_t)(v_stack_m1D8);
    v_stack_m58 = v_stack_m1F0;
    v_stack_m78 = v_stack_m60;
    v_stack_p20 = v_stack_mB8;
    v_stack_m70 = 2;
    v_stack_m5C = 0;
    v_stack_m1F0 = 0x1000000ULL;
    v_stack_m50 = 8;
    result = tlgWriteAgg(v_rip + 5842524, v_rip - 8524994, v_stack_m1D8, 7);
    goto loc_0087780F;
loc_00877930:
    local_r15 = 0;
    v_stack_p50 = result;
    v_stack_p48 = (uint8_t)(v_stack_p64);
    v_stack_p40 = (uint8_t)(v_stack_p65);
    v_stack_p38 = v_stack_m208;
    v_stack_p30 = Arg8;
    v_stack_p28 = v_stack_m1E0;
    v_stack_p20 = 0;
    result = CmpLoadKeyCommon(v_stack_m200, v_stack_m2B8, (uint32_t)(v_stack_p6C), v_stack_p78);
    goto loc_00877989;
loc_00877984:
    v_stack_p66 = 0;
loc_00877989:
    result = CmpLockAppHiveLoadList(v_stack_m200, v_stack_m2B8, (uint32_t)(v_stack_p6C), v_stack_p78);
    if ((*(uint64_t *)(v_stack_m278 + 0x8)) != v_stack_m278) goto loc_0087728E;
    if ((*(uint64_t *)(v_stack_m270)) != v_stack_m278) goto loc_0087728E;
    *(uint64_t *)(v_stack_m270) = v_stack_m278;
    *(uint64_t *)(v_stack_m278 + 0x8) = v_stack_m270;
    if (v_stack_m268 == v_stack_m268) goto loc_00877339;
    if ((*(uint64_t *)(v_stack_m268 + 0x8)) != v_stack_m268) goto loc_0087728E;
    if ((*(uint64_t *)(v_stack_m260)) != v_stack_m268) goto loc_0087728E;
    *(uint64_t *)(v_stack_m260) = v_stack_m268;
    *(uint64_t *)(v_stack_m268 + 0x8) = v_stack_m260;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x67DF97))) != (v_rip + 6807446)) goto loc_0087728E;
    *(uint64_t *)(v_stack_m268 - 0x10) = v_rip + 6807446;
    *(uint64_t *)(v_stack_m268 - 0x10 + 0x8) = *(uint64_t *)(v_rip + 0x67DF97);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x67DF97)) = v_stack_m268 - 16;
    *(uint64_t *)(v_rip + 0x67DF7D) = v_stack_m268 - 16;
    goto loc_00877339;
loc_00877A20:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00877AE7;
loc_00877A28:
    result = CmpAttachToRegistryProcess(v_stack_m1C8, v_rip + 6807446, v_stack_m268, v_stack_p78);
    v_stack_m210 = result;
    result = CmpConstructName(*(uint64_t *)(result + 0xB78), v_rip + 6807446, v_stack_m268, v_stack_p78);
    *(uint64_t *)(v_stack_m1E8) = result;
    result = CmpDetachFromRegistryProcess(v_stack_m1C8, v_rip + 6807446, v_stack_m268, v_stack_p78);
    if ((*(uint64_t *)(v_stack_m1E8)) == 0) goto loc_00877B1E;
    result = CmpReferenceKeyControlBlockUnsafe(*(uint64_t *)(result + 0xB78), v_rip + 6807446, v_stack_m268, v_stack_p78);
    *(uint64_t *)(v_stack_m208) = *(uint64_t *)(result + 0xB78);
    result = CmpUnlockRegistry(v_stack_m208, v_rip + 6807446, v_stack_m268, v_stack_p78);
    result = UNLOCK_HIVE_LOAD(v_stack_m208, v_rip + 6807446, v_stack_m268, v_stack_p78);
loc_00877A81:
    result = CmpDereferenceHive(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    if (v_stack_m210 != 0) goto loc_00877984;
loc_00877A93:
    result = CmpUnlockRegistry(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    result = UNLOCK_HIVE_LOAD(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    goto loc_008776C8;
loc_00877AA9:
    result = CmpUnlockRegistry(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    result = UNLOCK_HIVE_LOAD(result, v_rip + 6807446, v_stack_m268, v_stack_p78);
    v_stack_p20 = 0;
    result = ExBlockOnAddressPushLock(v_rip + 6807248, v_rip + 6807263, v_stack_m2A4, 4);
    result = LOCK_HIVE_LOAD(v_rip + 6807248, v_rip + 6807263, v_stack_m2A4, 4);
    result = CmpLockRegistryFreezeAware(0, v_rip + 6807263, v_stack_m2A4, 4);
    goto loc_00877766;
loc_00877AE7:
    result = CmpUnlockRegistry(0, v_rip + 6807263, v_stack_m2A4, 4);
    result = UNLOCK_HIVE_LOAD(0, v_rip + 6807263, v_stack_m2A4, 4);
    result = CmpDereferenceHive(v_stack_m288, v_rip + 6807263, v_stack_m2A4, 4);
    v_stack_p20 = 112;
loc_00877B01:
    Arg2 = 0;
    result = SetFailureLocation(result, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    goto loc_00877989;
loc_00877B1E:
    result = CmpUnlockRegistry(result, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    result = UNLOCK_HIVE_LOAD(result, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    result = CmpDereferenceHive(v_stack_m288, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    goto loc_00877989;
loc_00877B3A:
    result = CmpUnlockRegistry(v_stack_m288, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    result = UNLOCK_HIVE_LOAD(v_stack_m288, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    result = CmpDereferenceHive(v_stack_m288, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(0xC0000043ULL))));
    v_stack_p20 = 96;
    goto loc_00877B01;
loc_00877B56:
    Arg2 = 0;
    v_stack_p20 = 48;
    result = SetFailureLocation(result, Arg2, Arg2 + 32, (uint32_t)((uint32_t)(result)));
    local_r15 = 0;
    goto loc_00877989;
loc_00877B77:
    result = ExfWaitForRundownProtectionRelease(v_stack_m230, result, Arg2 + 32, (uint32_t)((uint32_t)(result)));
    goto loc_0087735E;
loc_00877B88:
    result = (*(uint64_t *)(v_rip + 0x5923E1)) & (result);
    if (result != (*(uint64_t *)(v_rip + 0x5923D7))) goto loc_0087786E;
    goto loc_00877871;
loc_00877BA7:
    result = (*(uint64_t *)(v_rip + 0x5923C2)) & (result);
    if (result != (*(uint64_t *)(v_rip + 0x5923B8))) goto loc_008773B9;
    goto loc_008773BC;
loc_00877BC6:
    result = (v_stack_m230) & (Arg2 + 32);
    if (result != v_stack_m230) goto loc_008774EE;
    goto loc_008774F1;
loc_00877BDD:
    result = (uint32_t)((v_stack_m230) & (8));
    if (result == v_stack_m230) goto loc_0087769B;
    goto loc_00877698;
loc_00877BF1:
    if ((uint32_t)(result) != 0) goto loc_008770E0;
    goto loc_008770FA;
loc_00877C07:
loc_00877C11:
loc_00877C1B:
    local_r15 = 0;
    goto loc_0087745B;
loc_00877C28:
    v_stack_p60 = 0;
    v_stack_m258 = v_stack_m288;
    v_stack_m250 = 0;
    goto loc_00877244;
loc_00877C3A:
    goto loc_008772A5;
loc_00877C46:
    result = CmpUnlockRegistry(v_rip + 6806863, result, Arg2 + 32, (uint32_t)((uint32_t)(result)));
    result = UNLOCK_HIVE_LOAD(v_rip + 6806863, result, Arg2 + 32, (uint32_t)((uint32_t)(result)));
    goto loc_008776C8;
loc_00877C58:
    result = CmpDereferenceHive(v_stack_m288, result, Arg2 + 32, (uint32_t)((uint32_t)(result)));
    goto loc_00877A93;
loc_00877C65:
    if ((*(uint16_t *)(result + 0xA)) != 0) goto loc_0087746A;
    if ((*(uint8_t *)(result + 0x18A)) != 0) goto loc_0087746A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00876FFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
