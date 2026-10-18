# CmpCreateHive

- RVA: `0x00879DF0`–`0x0087A65E` (길이 `2,158` bytes)
- VA: `0x0000000140879DF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006CD84`
- 디코드: `499`개 명령, `2,158/2,158` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00879F2D` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00879F60` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00879F89` → [CmpAllocate](../84/CmpAllocate_function_0084DD40.md) (function, `0x0084DD40`)
- `0x00879FA0` → [CmpHiveInitialize](CmpHiveInitialize_function_0087B7AC.md) (function, `0x0087B7AC`)
- `0x00879FCD` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x0087A0B8` → [HvHiveStartMemoryBacked](HvHiveStartMemoryBacked_function_0087BF38.md) (function, `0x0087BF38`)
- `0x0087A0E4` → [CmpVolumeManagerGetContextForFile](../95/CmpVolumeManagerGetContextForFile_function_009525A8.md) (function, `0x009525A8`)
- `0x0087A0FA` → [CmpVolumeContextMustHiveFilePagesBeKeptLocal](CmpVolumeContextMustHiveFilePagesBeKeptLocal_function_0087BDC4.md) (function, `0x0087BDC4`)
- `0x0087A113` → [CmpVolumeContextCanHiveSectionBeExtended](CmpVolumeContextCanHiveSectionBeExtended_function_0087BD78.md) (function, `0x0087BD78`)
- `0x0087A183` → [HvHiveStartFileBacked](../9B/HvHiveStartFileBacked_function_009B7E20.md) (function, `0x009B7E20`)
- `0x0087A1BE` → [CmCheckRegistry](../96/CmCheckRegistry_function_0096D2F4.md) (function, `0x0096D2F4`)
- `0x0087A1F6` → [CmpReorganizeHive](CmpReorganizeHive_function_0087B92C.md) (function, `0x0087B92C`)
- `0x0087A1FB` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0087A203` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x0087A20B` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x0087A21C` → [HvCheckAndUpdateHiveBackupTimeStamp](HvCheckAndUpdateHiveBackupTimeStamp_function_0087BE90.md) (function, `0x0087BE90`)
- `0x0087A226` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x0087A22E` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0087A233` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0087A265` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x0087A284` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x0087A29F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0087A2DB` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087A2EA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087A305` → [CmpAllocateForNonPagedHive](../../text/4D/CmpAllocateForNonPagedHive_function_004D92F0.md) (function, `0x004D92F0`)
- `0x0087A344` → [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) (function, `0x008C4FA0`)
- `0x0087A36A` → [ZwSetInformationObject](../../text/6A/ZwSetInformationObject_function_006ADC50.md) (function, `0x006ADC50`)
- `0x0087A3C3` → [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) (function, `0x008C4FA0`)
- `0x0087A3E5` → [ZwSetInformationObject](../../text/6A/ZwSetInformationObject_function_006ADC50.md) (function, `0x006ADC50`)
- `0x0087A417` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087A41F` → [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) (function, `0x009B1708`)
- `0x0087A443` → [CmpGetVolumeClusterSize](CmpGetVolumeClusterSize_function_0087B3D4.md) (function, `0x0087B3D4`)
- `0x0087A516` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087A51B` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x0087A624` → [CmpLockHiveListExclusive](../A7/CmpLockHiveListExclusive_function_00A72240.md) (function, `0x00A72240`)
- `0x0087A654` → [CmpLogHiveInitializeEvent](../7E/CmpLogHiveInitializeEvent_function_007E6250.md) (function, `0x007E6250`)

### Direct callers
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD0BB`
- [CmpCreateTemporaryHive](../7D/CmpCreateTemporaryHive_function_007DE528.md) at `0x007DE5B4`
- [CmpLoadHiveVolatile](../7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DE737`
- [CmpLoadHiveVolatile](../7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DE791`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DED0E`
- [CmpHiveCachePopulateHiveEntryThread](../7F/CmpHiveCachePopulateHiveEntryThread_function_007F5FD0.md) at `0x007F6184`
- [CmpInitHiveFromFile](CmpInitHiveFromFile_function_008794D4.md) at `0x00879856`
- [CmInitSystem1](../../init/C5/CmInitSystem1_function_00C559CC.md) at `0x00C55D64`
- [CmInitSystem1](../../init/C5/CmInitSystem1_function_00C559CC.md) at `0x00C5617E`
- [CmpInitializePreloadedHive](../../init/C5/CmpInitializePreloadedHive_function_00C58070.md) at `0x00C58283`
- [CmpInitializeSystemHive](../../init/C5/CmpInitializeSystemHive_function_00C58798.md) at `0x00C58856`

### Static image references
- `0x00879E0C` → RVA `0x00E0A740` (`.data`; read)
- `0x00879FDB` → RVA `0x0084DD40` (`CmpAllocate`; read)
- `0x00879FE2` → RVA `0x004D92F0` (`CmpAllocateForNonPagedHive`; read)
- `0x00879FF1` → RVA `0x0084D8F0` (`CmpFree`; read)
- `0x00879FFC` → RVA `0x00A65840` (`CmpFileWrite`; read)
- `0x0087A007` → RVA `0x00A6DBC0` (`CmpFileRead`; read)
- `0x0087A26A` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x0087A318` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0087A629` → RVA `0x00FD9D20` (`PAGEDATA`; read)
- `0x0087A630` → RVA `0x00FD9D18` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00879F2D` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00879F60` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00879FCD` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x0087A1FB` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0087A233` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0087A265` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x0087A284` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x0087A29F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0087A2DB` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087A2EA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087A305` → [CmpAllocateForNonPagedHive](../../text/4D/CmpAllocateForNonPagedHive_function_004D92F0.md) (`PAGE` → `.text`)
  - `0x0087A36A` → [ZwSetInformationObject](../../text/6A/ZwSetInformationObject_function_006ADC50.md) (`PAGE` → `.text`)
  - `0x0087A3E5` → [ZwSetInformationObject](../../text/6A/ZwSetInformationObject_function_006ADC50.md) (`PAGE` → `.text`)
  - `0x0087A417` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087A516` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087A51B` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **20**
  - `0x0087A101` → [sub_00B1802A + 0xEE](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A1CE` → [sub_00B1802A + 0x143](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A377` → [sub_00B1802A + 0x3A](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A3FF` → [sub_00B1802A + 0x97](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A482` → [sub_00B1802A + 0xD](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A48F` → [sub_00B1802A + 0x2B](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A49F` → [sub_00B1802A + 0x23](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4A9` → [sub_00B1802A](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4BA` → [sub_00B1802A](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4C7` → [sub_00B1802A + 0x8](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4D4` → [sub_00B1802A + 0x8](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4DC` → [sub_00B1802A + 0x30](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4E5` → [sub_00B1802A + 0x30](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A4F4` → [sub_00B1802A + 0x30](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A541` → [sub_00B1802A + 0x97](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A5D2` → [sub_00B1802A + 0x139](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A5ED` → [sub_00B1802A + 0x139](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A5FA` → [sub_00B1802A + 0x2CC](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A60F` → [sub_00B1802A + 0x2CC](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)
  - `0x0087A63A` → [sub_00B1802A + 0x2EF](../B1/Unknown_function_00B1802A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00879DF0  40 55                           push rbp
00879DF2  53                              push rbx
00879DF3  56                              push rsi
00879DF4  57                              push rdi
00879DF5  41 54                           push r12
00879DF7  41 55                           push r13
00879DF9  41 56                           push r14
00879DFB  41 57                           push r15
00879DFD  48 8D AC 24 C8 FE FF FF         lea rbp, [rsp - 0x138]
00879E05  48 81 EC 38 02 00 00            sub rsp, 0x238
00879E0C  48 8B 05 2D 09 59 00            mov rax, qword ptr [rip + 0x59092d]
00879E13  48 33 C4                        xor rax, rsp
00879E16  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00879E1D  4C 8B A5 A8 01 00 00            mov r12, qword ptr [rbp + 0x1a8]
00879E24  33 DB                           xor ebx, ebx
00879E26  4C 8B B5 E0 01 00 00            mov r14, qword ptr [rbp + 0x1e0]
00879E2D  8B C2                           mov eax, edx
00879E2F  0F 57 C0                        xorps xmm0, xmm0
00879E32  89 55 90                        mov dword ptr [rbp - 0x70], edx
00879E35  48 8B 95 B0 01 00 00            mov rdx, qword ptr [rbp + 0x1b0]
00879E3C  0F 57 C9                        xorps xmm1, xmm1
00879E3F  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
00879E43  45 8B F8                        mov r15d, r8d
00879E46  48 8B 95 C0 01 00 00            mov rdx, qword ptr [rbp + 0x1c0]
00879E4D  8B FB                           mov edi, ebx
00879E4F  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
00879E53  44 8B EB                        mov r13d, ebx
00879E56  48 8B 95 C8 01 00 00            mov rdx, qword ptr [rbp + 0x1c8]
00879E5D  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
00879E61  48 8B 95 D8 01 00 00            mov rdx, qword ptr [rbp + 0x1d8]
00879E68  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
00879E6C  33 D2                           xor edx, edx
00879E6E  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00879E72  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
00879E79  44 89 4D 88                     mov dword ptr [rbp - 0x78], r9d
00879E7D  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00879E81  48 89 55 18                     mov qword ptr [rbp + 0x18], rdx
00879E85  89 5D 94                        mov dword ptr [rbp - 0x6c], ebx
00879E88  88 5D 84                        mov byte ptr [rbp - 0x7c], bl
00879E8B  88 5D 85                        mov byte ptr [rbp - 0x7b], bl
00879E8E  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
00879E92  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00879E96  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
00879E9A  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
00879E9E  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00879EA2  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
00879EA6  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00879EAA  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
00879EAE  83 F8 02                        cmp eax, 2
00879EB1  0F 87 02 04 00 00               ja 0x14087a2b9
00879EB7  41 F7 C7 EC 7C 61 F5            test r15d, 0xf5617cec
00879EBE  0F 85 A6 05 00 00               jne 0x14087a46a
00879EC4  41 83 F9 02                     cmp r9d, 2
00879EC8  0F 87 A6 05 00 00               ja 0x14087a474
00879ECE  BE 01 00 00 00                  mov esi, 1
00879ED3  48 85 C9                        test rcx, rcx
00879ED6  75 08                           jne 0x140879ee0
00879ED8  3B C6                           cmp eax, esi
00879EDA  0F 84 A7 05 00 00               je 0x14087a487
00879EE0  4D 85 E4                        test r12, r12
00879EE3  74 48                           je 0x140879f2d
00879EE5  44 84 FE                        test sil, r15b
00879EE8  0F 85 A6 05 00 00               jne 0x14087a494
00879EEE  49 8B 14 24                     mov rdx, qword ptr [r12]
00879EF2  48 85 D2                        test rdx, rdx
00879EF5  0F 84 A9 05 00 00               je 0x14087a4a4
00879EFB  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
00879F00  48 85 C9                        test rcx, rcx
00879F03  74 09                           je 0x140879f0e
00879F05  45 85 C9                        test r9d, r9d
00879F08  0F 84 B1 05 00 00               je 0x14087a4bf
00879F0E  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
00879F13  48 85 C0                        test rax, rax
00879F16  74 0A                           je 0x140879f22
00879F18  41 83 F9 02                     cmp r9d, 2
00879F1C  0F 85 AA 05 00 00               jne 0x14087a4cc
00879F22  49 39 5C 24 18                  cmp qword ptr [r12 + 0x18], rbx
00879F27  0F 85 AC 05 00 00               jne 0x14087a4d9
00879F2D  E8 CE F4 34 00                  call 0x140bc9400
00879F32  88 45 84                        mov byte ptr [rbp - 0x7c], al
00879F35  84 C0                           test al, al
00879F37  0F 84 BC 05 00 00               je 0x14087a4f9
00879F3D  89 75 8C                        mov dword ptr [rbp - 0x74], esi
00879F40  4D 85 E4                        test r12, r12
00879F43  74 0D                           je 0x140879f52
00879F45  49 8B 0C 24                     mov rcx, qword ptr [r12]
00879F49  48 85 C9                        test rcx, rcx
00879F4C  0F 85 ED 04 00 00               jne 0x14087a43f
00879F52  BA 20 00 00 00                  mov edx, 0x20
00879F57  41 B8 43 4D 39 35               mov r8d, 0x35394d43
00879F5D  8D 4A 20                        lea ecx, [rdx + 0x20]
00879F60  E8 8B 81 30 00                  call 0x140b820f0
00879F65  4C 8B E8                        mov r13, rax
00879F68  48 85 C0                        test rax, rax
00879F6B  0F 84 B4 05 00 00               je 0x14087a525
00879F71  33 D2                           xor edx, edx
00879F73  B9 D8 12 00 00                  mov ecx, 0x12d8
00879F78  41 B8 43 4D 31 30               mov r8d, 0x30314d43
00879F7E  41 0F BA E7 19                  bt r15d, 0x19
00879F83  0F 82 7C 03 00 00               jb 0x14087a305
00879F89  E8 B2 3D FD FF                  call 0x14084dd40
00879F8E  48 8B F8                        mov rdi, rax
00879F91  48 85 C0                        test rax, rax
00879F94  0F 84 BF 04 00 00               je 0x14087a459
00879F9A  49 8B D5                        mov rdx, r13
00879F9D  48 8B C8                        mov rcx, rax
00879FA0  E8 07 18 00 00                  call 0x14087b7ac
00879FA5  4D 85 E4                        test r12, r12
00879FA8  0F 85 61 03 00 00               jne 0x14087a30f
00879FAE  44 8B AD B8 01 00 00            mov r13d, dword ptr [rbp + 0x1b8]
00879FB5  41 0F BA E5 1B                  bt r13d, 0x1b
00879FBA  0F 82 86 05 00 00               jb 0x14087a546
00879FC0  45 85 ED                        test r13d, r13d
00879FC3  0F 88 8A 05 00 00               js 0x14087a553
00879FC9  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00879FCD  E8 0E F9 34 00                  call 0x140bc98e0
00879FD2  41 0F BA E7 19                  bt r15d, 0x19
00879FD7  40 88 75 85                     mov byte ptr [rbp - 0x7b], sil
00879FDB  48 8D 05 5E 3D FD FF            lea rax, [rip - 0x2c2a2]
00879FE2  48 8D 0D 07 F3 C5 FF            lea rcx, [rip - 0x3a0cf9]
00879FE9  48 0F 42 C1                     cmovb rax, rcx
00879FED  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00879FF1  48 8D 05 F8 38 FD FF            lea rax, [rip - 0x2c708]
00879FF8  48 89 45 00                     mov qword ptr [rbp], rax
00879FFC  48 8D 05 3D B8 1E 00            lea rax, [rip + 0x1eb83d]
0087A003  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0087A007  48 8D 05 B2 3B 1F 00            lea rax, [rip + 0x1f3bb2]
0087A00E  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0087A012  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
0087A015  4C 89 77 38                     mov qword ptr [rdi + 0x38], r14
0087A019  49 89 3E                        mov qword ptr [r14], rdi
0087A01C  83 F8 02                        cmp eax, 2
0087A01F  0F 84 AF 00 00 00               je 0x14087a0d4
0087A025  83 F8 05                        cmp eax, 5
0087A028  0F 84 A6 00 00 00               je 0x14087a0d4
0087A02E  85 C0                           test eax, eax
0087A030  0F 84 2A 05 00 00               je 0x14087a560
0087A036  48 8B 8D D0 01 00 00            mov rcx, qword ptr [rbp + 0x1d0]
0087A03D  48 85 C9                        test rcx, rcx
0087A040  0F 85 33 05 00 00               jne 0x14087a579
0087A046  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0087A04A  48 8B C8                        mov rcx, rax
0087A04D  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
0087A051  48 8D 55 94                     lea rdx, [rbp - 0x6c]
0087A055  44 8B 65 90                     mov r12d, dword ptr [rbp - 0x70]
0087A059  44 8B 4D 88                     mov r9d, dword ptr [rbp - 0x78]
0087A05D  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0087A062  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0087A067  41 8B D4                        mov edx, r12d
0087A06A  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
0087A06F  45 8B C7                        mov r8d, r15d
0087A072  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0087A077  48 8B CF                        mov rcx, rdi
0087A07A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0087A07F  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
0087A083  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0087A088  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0087A08C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0087A091  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0087A095  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
0087A09A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0087A09F  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
0087A0A2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0087A0A6  48 8D 45 F8                     lea rax, [rbp - 8]
0087A0AA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0087A0AF  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0087A0B3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087A0B8  E8 7B 1E 00 00                  call 0x14087bf38
0087A0BD  8B D8                           mov ebx, eax
0087A0BF  85 C0                           test eax, eax
0087A0C1  0F 89 CB 00 00 00               jns 0x14087a192
0087A0C7  C7 44 24 20 E8 00 00 00         mov dword ptr [rsp + 0x20], 0xe8
0087A0CF  E9 38 03 00 00                  jmp 0x14087a40c
0087A0D4  49 8B 14 24                     mov rdx, qword ptr [r12]
0087A0D8  4C 8D 8F B8 12 00 00            lea r9, [rdi + 0x12b8]
0087A0DF  41 0F BA EF 11                  bts r15d, 0x11
0087A0E4  E8 BF 84 0D 00                  call 0x1409525a8
0087A0E9  8B D8                           mov ebx, eax
0087A0EB  85 C0                           test eax, eax
0087A0ED  0F 88 29 03 00 00               js 0x14087a41c
0087A0F3  48 8B 8F B8 12 00 00            mov rcx, qword ptr [rdi + 0x12b8]
0087A0FA  E8 C5 1C 00 00                  call 0x14087bdc4
0087A0FF  84 C0                           test al, al
0087A101  0F 84 11 E0 29 00               je 0x140b18118
0087A107  41 0F BA EF 17                  bts r15d, 0x17
0087A10C  48 8B 8F B8 12 00 00            mov rcx, qword ptr [rdi + 0x12b8]
0087A113  E8 60 1C 00 00                  call 0x14087bd78
0087A118  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
0087A11C  41 8B CF                        mov ecx, r15d
0087A11F  44 8B 65 90                     mov r12d, dword ptr [rbp - 0x70]
0087A123  0F BA E9 1B                     bts ecx, 0x1b
0087A127  44 8B 4D 88                     mov r9d, dword ptr [rbp - 0x78]
0087A12B  84 C0                           test al, al
0087A12D  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
0087A132  48 8D 45 94                     lea rax, [rbp - 0x6c]
0087A136  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0087A13B  41 0F 45 CF                     cmovne ecx, r15d
0087A13F  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
0087A143  44 8B F9                        mov r15d, ecx
0087A146  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0087A14B  45 85 E4                        test r12d, r12d
0087A14E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0087A153  44 8B C1                        mov r8d, ecx
0087A156  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0087A15A  0F 94 C2                        sete dl
0087A15D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0087A162  48 8B CF                        mov rcx, rdi
0087A165  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0087A169  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
0087A16E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0087A173  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
0087A176  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0087A17A  48 8D 45 F8                     lea rax, [rbp - 8]
0087A17E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087A183  E8 98 DC 13 00                  call 0x1409b7e20
0087A188  8B D8                           mov ebx, eax
0087A18A  85 C0                           test eax, eax
0087A18C  0F 88 13 04 00 00               js 0x14087a5a5
0087A192  41 0F BA E7 13                  bt r15d, 0x13
0087A197  0F 82 15 04 00 00               jb 0x14087a5b2
0087A19D  41 BF 02 00 00 00               mov r15d, 2
0087A1A3  41 8D 44 24 FF                  lea eax, [r12 - 1]
0087A1A8  A9 FA FF FF FF                  test eax, 0xfffffffa
0087A1AD  75 2D                           jne 0x14087a1dc
0087A1AF  41 83 FC 06                     cmp r12d, 6
0087A1B3  74 27                           je 0x14087a1dc
0087A1B5  4D 8B C6                        mov r8, r14
0087A1B8  41 8B D5                        mov edx, r13d
0087A1BB  48 8B CF                        mov rcx, rdi
0087A1BE  E8 31 31 0F 00                  call 0x14096d2f4
0087A1C3  41 B8 2A 00 00 80               mov r8d, 0x8000002a
0087A1C9  8B D8                           mov ebx, eax
0087A1CB  41 3B C0                        cmp eax, r8d
0087A1CE  0F 84 99 DF 29 00               je 0x140b1816d
0087A1D4  85 C0                           test eax, eax
0087A1D6  0F 88 28 02 00 00               js 0x14087a404
0087A1DC  33 DB                           xor ebx, ebx
0087A1DE  41 0F BA E5 17                  bt r13d, 0x17
0087A1E3  0F 82 09 04 00 00               jb 0x14087a5f2
0087A1E9  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
0087A1ED  45 8B C5                        mov r8d, r13d
0087A1F0  49 8B D7                        mov rdx, r15
0087A1F3  48 8B CF                        mov rcx, rdi
0087A1F6  E8 31 17 00 00                  call 0x14087b92c
0087A1FB  E8 34 F9 34 00                  call 0x140bc9b34
0087A200  48 8B CF                        mov rcx, rdi
0087A203  E8 54 57 FD FF                  call 0x14084f95c
0087A208  48 8B CF                        mov rcx, rdi
0087A20B  E8 84 F6 FD FF                  call 0x140859894
0087A210  45 85 E4                        test r12d, r12d
0087A213  0F 84 1A 02 00 00               je 0x14087a433
0087A219  48 8B CF                        mov rcx, rdi
0087A21C  E8 6F 1C 00 00                  call 0x14087be90
0087A221  8B D8                           mov ebx, eax
0087A223  48 8B CF                        mov rcx, rdi
0087A226  E8 B9 F6 FD FF                  call 0x1408598e4
0087A22B  48 8B CF                        mov rcx, rdi
0087A22E  E8 05 E5 FC FF                  call 0x140848738
0087A233  E8 4C F8 34 00                  call 0x140bc9a84
0087A238  85 DB                           test ebx, ebx
0087A23A  0F 88 D4 03 00 00               js 0x14087a614
0087A240  48 8D 9F 48 06 00 00            lea rbx, [rdi + 0x648]
0087A247  41 0F BA E5 18                  bt r13d, 0x18
0087A24C  0F 83 D2 03 00 00               jae 0x14087a624
0087A252  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
0087A256  48 89 1B                        mov qword ptr [rbx], rbx
0087A259  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0087A25D  48 83 67 38 00                  and qword ptr [rdi + 0x38], 0
0087A262  48 89 38                        mov qword ptr [rax], rdi
0087A265  E8 16 F6 34 00                  call 0x140bc9880
0087A26A  F7 05 94 C8 74 00 00 00 00 01   test dword ptr [rip + 0x74c894], 0x1000000
0087A274  C6 45 84 00                     mov byte ptr [rbp - 0x7c], 0
0087A278  0F 85 C9 03 00 00               jne 0x14087a647
0087A27E  33 DB                           xor ebx, ebx
0087A280  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0087A284  E8 97 F6 34 00                  call 0x140bc9920
0087A289  80 7D 84 00                     cmp byte ptr [rbp - 0x7c], 0
0087A28D  0F 85 88 02 00 00               jne 0x14087a51b
0087A293  8B C3                           mov eax, ebx
0087A295  48 8B 8D 20 01 00 00            mov rcx, qword ptr [rbp + 0x120]
0087A29C  48 33 CC                        xor rcx, rsp
0087A29F  E8 9C 23 E3 FF                  call 0x1406ac640
0087A2A4  48 81 C4 38 02 00 00            add rsp, 0x238
0087A2AB  41 5F                           pop r15
0087A2AD  41 5E                           pop r14
0087A2AF  41 5D                           pop r13
0087A2B1  41 5C                           pop r12
0087A2B3  5F                              pop rdi
0087A2B4  5E                              pop rsi
0087A2B5  5B                              pop rbx
0087A2B6  5D                              pop rbp
0087A2B7  C3                              ret
0087A2B8  CC                              int3
0087A2B9  83 F8 05                        cmp eax, 5
0087A2BC  0F 84 F5 FB FF FF               je 0x140879eb7
0087A2C2  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0087A2C7  BE 01 00 00 00                  mov esi, 1
0087A2CC  33 C0                           xor eax, eax
0087A2CE  44 8B CB                        mov r9d, ebx
0087A2D1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0087A2D5  44 8B C6                        mov r8d, esi
0087A2D8  49 8B CE                        mov rcx, r14
0087A2DB  E8 74 4C BF FF                  call 0x14046ef54
0087A2E0  4D 85 ED                        test r13, r13
0087A2E3  74 A4                           je 0x14087a289
0087A2E5  33 D2                           xor edx, edx
0087A2E7  49 8B CD                        mov rcx, r13
0087A2EA  E8 81 85 30 00                  call 0x140b82870
0087A2EF  40 8A 75 84                     mov sil, byte ptr [rbp - 0x7c]
0087A2F3  40 88 75 84                     mov byte ptr [rbp - 0x7c], sil
0087A2F7  C6 45 85 00                     mov byte ptr [rbp - 0x7b], 0
0087A2FB  48 85 FF                        test rdi, rdi
0087A2FE  74 89                           je 0x14087a289
0087A300  E9 17 01 00 00                  jmp 0x14087a41c
0087A305  E8 E6 EF C5 FF                  call 0x1404d92f0
0087A30A  E9 7F FC FF FF                  jmp 0x140879f8e
0087A30F  49 8B 14 24                     mov rdx, qword ptr [r12]
0087A313  48 85 D2                        test rdx, rdx
0087A316  74 57                           je 0x14087a36f
0087A318  48 8B 0D 91 C7 74 00            mov rcx, qword ptr [rip + 0x74c791]
0087A31F  4C 8D AF 08 06 00 00            lea r13, [rdi + 0x608]
0087A326  88 5C 24 38                     mov byte ptr [rsp + 0x38], bl
0087A32A  4D 8B CD                        mov r9, r13
0087A32D  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0087A335  45 33 C0                        xor r8d, r8d
0087A338  C7 44 24 28 00 02 00 00         mov dword ptr [rsp + 0x28], 0x200
0087A340  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0087A344  E8 57 AC 04 00                  call 0x1408c4fa0
0087A349  8B D8                           mov ebx, eax
0087A34B  85 C0                           test eax, eax
0087A34D  0F 88 C9 00 00 00               js 0x14087a41c
0087A353  49 8B 4D 00                     mov rcx, qword ptr [r13]
0087A357  4C 8D 45 80                     lea r8, [rbp - 0x80]
0087A35B  33 DB                           xor ebx, ebx
0087A35D  66 C7 45 80 00 01               mov word ptr [rbp - 0x80], 0x100
0087A363  44 8D 4B 02                     lea r9d, [rbx + 2]
0087A367  8D 53 04                        lea edx, [rbx + 4]
0087A36A  E8 E1 38 E3 FF                  call 0x1406adc50
0087A36F  49 8B 54 24 18                  mov rdx, qword ptr [r12 + 0x18]
0087A374  48 85 D2                        test rdx, rdx
0087A377  0F 85 E7 DC 29 00               jne 0x140b18064
0087A37D  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
0087A380  3B C6                           cmp eax, esi
0087A382  0F 84 A4 01 00 00               je 0x14087a52c
0087A388  83 F8 02                        cmp eax, 2
0087A38B  0F 85 1D FC FF FF               jne 0x140879fae
0087A391  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
0087A396  48 85 D2                        test rdx, rdx
0087A399  74 4F                           je 0x14087a3ea
0087A39B  48 8B 0D 0E C7 74 00            mov rcx, qword ptr [rip + 0x74c70e]
0087A3A2  4C 8D AF 28 06 00 00            lea r13, [rdi + 0x628]
0087A3A9  88 5C 24 38                     mov byte ptr [rsp + 0x38], bl
0087A3AD  4D 8B CD                        mov r9, r13
0087A3B0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0087A3B4  45 33 C0                        xor r8d, r8d
0087A3B7  C7 44 24 28 00 02 00 00         mov dword ptr [rsp + 0x28], 0x200
0087A3BF  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0087A3C3  E8 D8 AB 04 00                  call 0x1408c4fa0
0087A3C8  8B D8                           mov ebx, eax
0087A3CA  85 C0                           test eax, eax
0087A3CC  78 4E                           js 0x14087a41c
0087A3CE  49 8B 4D 00                     mov rcx, qword ptr [r13]
0087A3D2  4C 8D 45 80                     lea r8, [rbp - 0x80]
0087A3D6  33 DB                           xor ebx, ebx
0087A3D8  66 C7 45 80 00 01               mov word ptr [rbp - 0x80], 0x100
0087A3DE  44 8D 4B 02                     lea r9d, [rbx + 2]
0087A3E2  8D 53 04                        lea edx, [rbx + 4]
0087A3E5  E8 66 38 E3 FF                  call 0x1406adc50
0087A3EA  49 8B 54 24 10                  mov rdx, qword ptr [r12 + 0x10]
0087A3EF  48 85 D2                        test rdx, rdx
0087A3F2  0F 84 B6 FB FF FF               je 0x140879fae
0087A3F8  4C 8D AF 30 06 00 00            lea r13, [rdi + 0x630]
0087A3FF  E9 BD DC 29 00                  jmp 0x140b180c1
0087A404  C7 44 24 20 F0 00 00 00         mov dword ptr [rsp + 0x20], 0xf0
0087A40C  44 8B C8                        mov r9d, eax
0087A40F  44 8B C6                        mov r8d, esi
0087A412  33 D2                           xor edx, edx
0087A414  49 8B CE                        mov rcx, r14
0087A417  E8 38 4B BF FF                  call 0x14046ef54
0087A41C  48 8B CF                        mov rcx, rdi
0087A41F  E8 E4 72 13 00                  call 0x1409b1708
0087A424  80 7D 85 00                     cmp byte ptr [rbp - 0x7b], 0
0087A428  0F 85 52 FE FF FF               jne 0x14087a280
0087A42E  E9 56 FE FF FF                  jmp 0x14087a289
0087A433  40 88 B7 C3 00 00 00            mov byte ptr [rdi + 0xc3], sil
0087A43A  E9 E4 FD FF FF                  jmp 0x14087a223
0087A43F  48 8D 55 8C                     lea rdx, [rbp - 0x74]
0087A443  E8 8C 0F 00 00                  call 0x14087b3d4
0087A448  8B D8                           mov ebx, eax
0087A44A  85 C0                           test eax, eax
0087A44C  0F 88 B1 00 00 00               js 0x14087a503
0087A452  33 DB                           xor ebx, ebx
0087A454  E9 F9 FA FF FF                  jmp 0x140879f52
0087A459  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0087A45E  33 D2                           xor edx, edx
0087A460  B8 B0 00 00 00                  mov eax, 0xb0
0087A465  E9 64 FE FF FF                  jmp 0x14087a2ce
0087A46A  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
0087A472  EB 08                           jmp 0x14087a47c
0087A474  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0087A47C  41 B8 01 00 00 00               mov r8d, 1
0087A482  E9 B0 DB 29 00                  jmp 0x140b18037
0087A487  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
0087A48F  E9 C1 DB 29 00                  jmp 0x140b18055
0087A494  41 0F BA E7 0F                  bt r15d, 0xf
0087A499  0F 82 4F FA FF FF               jb 0x140879eee
0087A49F  E9 A9 DB 29 00                  jmp 0x140b1804d
0087A4A4  49 39 5C 24 08                  cmp qword ptr [r12 + 8], rbx
0087A4A9  0F 85 7B DB 29 00               jne 0x140b1802a
0087A4AF  49 39 5C 24 10                  cmp qword ptr [r12 + 0x10], rbx
0087A4B4  0F 84 41 FA FF FF               je 0x140879efb
0087A4BA  E9 6B DB 29 00                  jmp 0x140b1802a
0087A4BF  C7 44 24 20 60 00 00 00         mov dword ptr [rsp + 0x20], 0x60
0087A4C7  E9 66 DB 29 00                  jmp 0x140b18032
0087A4CC  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
0087A4D4  E9 59 DB 29 00                  jmp 0x140b18032
0087A4D9  48 85 D2                        test rdx, rdx
0087A4DC  0F 85 78 DB 29 00               jne 0x140b1805a
0087A4E2  48 85 C9                        test rcx, rcx
0087A4E5  0F 85 6F DB 29 00               jne 0x140b1805a
0087A4EB  48 85 C0                        test rax, rax
0087A4EE  0F 84 39 FA FF FF               je 0x140879f2d
0087A4F4  E9 61 DB 29 00                  jmp 0x140b1805a
0087A4F9  BB 89 01 00 C0                  mov ebx, 0xc0000189
0087A4FE  E9 90 FD FF FF                  jmp 0x14087a293
0087A503  44 8B C8                        mov r9d, eax
0087A506  C7 44 24 20 A0 00 00 00         mov dword ptr [rsp + 0x20], 0xa0
0087A50E  44 8B C6                        mov r8d, esi
0087A511  33 D2                           xor edx, edx
0087A513  49 8B CE                        mov rcx, r14
0087A516  E8 39 4A BF FF                  call 0x14046ef54
0087A51B  E8 60 F3 34 00                  call 0x140bc9880
0087A520  E9 6E FD FF FF                  jmp 0x14087a293
0087A525  BB 17 00 00 C0                  mov ebx, 0xc0000017
0087A52A  EB EF                           jmp 0x14087a51b
0087A52C  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
0087A531  48 85 D2                        test rdx, rdx
0087A534  0F 84 74 FA FF FF               je 0x140879fae
0087A53A  4C 8D AF 10 06 00 00            lea r13, [rdi + 0x610]
0087A541  E9 7B DB 29 00                  jmp 0x140b180c1
0087A546  0F BA AF 10 10 00 00 07         bts dword ptr [rdi + 0x1010], 7
0087A54E  E9 6D FA FF FF                  jmp 0x140879fc0
0087A553  0F BA AF 10 10 00 00 0B         bts dword ptr [rdi + 0x1010], 0xb
0087A55B  E9 69 FA FF FF                  jmp 0x140879fc9
0087A560  4D 85 E4                        test r12, r12
0087A563  0F 84 CD FA FF FF               je 0x14087a036
0087A569  49 83 3C 24 00                  cmp qword ptr [r12], 0
0087A56E  0F 85 60 FB FF FF               jne 0x14087a0d4
0087A574  E9 BD FA FF FF                  jmp 0x14087a036
0087A579  8B 41 70                        mov eax, dword ptr [rcx + 0x70]
0087A57C  89 45 D8                        mov dword ptr [rbp - 0x28], eax
0087A57F  48 8B 41 68                     mov rax, qword ptr [rcx + 0x68]
0087A583  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0087A587  8B 81 80 00 00 00               mov eax, dword ptr [rcx + 0x80]
0087A58D  89 45 E8                        mov dword ptr [rbp - 0x18], eax
0087A590  48 8B 41 78                     mov rax, qword ptr [rcx + 0x78]
0087A594  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0087A598  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0087A59C  48 8D 45 D8                     lea rax, [rbp - 0x28]
0087A5A0  E9 A8 FA FF FF                  jmp 0x14087a04d
0087A5A5  C7 44 24 20 E4 00 00 00         mov dword ptr [rsp + 0x20], 0xe4
0087A5AD  E9 5A FE FF FF                  jmp 0x14087a40c
0087A5B2  41 0F BA E7 14                  bt r15d, 0x14
0087A5B7  0F 93 C1                        setae cl
0087A5BA  41 0F BA E5 17                  bt r13d, 0x17
0087A5BF  0F 93 C0                        setae al
0087A5C2  84 C8                           test al, cl
0087A5C4  0F 84 D3 FB FF FF               je 0x14087a19d
0087A5CA  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0087A5CE  83 78 18 06                     cmp dword ptr [rax + 0x18], 6
0087A5D2  0F 82 8B DB 29 00               jb 0x140b18163
0087A5D8  8B 80 90 00 00 00               mov eax, dword ptr [rax + 0x90]
0087A5DE  41 BF 02 00 00 00               mov r15d, 2
0087A5E4  41 84 C7                        test r15b, al
0087A5E7  0F 85 B6 FB FF FF               jne 0x14087a1a3
0087A5ED  E9 71 DB 29 00                  jmp 0x140b18163
0087A5F2  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0087A5F6  83 78 18 06                     cmp dword ptr [rax + 0x18], 6
0087A5FA  0F 82 F6 DC 29 00               jb 0x140b182f6
0087A600  8B 80 90 00 00 00               mov eax, dword ptr [rax + 0x90]
0087A606  41 84 C7                        test r15b, al
0087A609  0F 85 DA FB FF FF               jne 0x14087a1e9
0087A60F  E9 E2 DC 29 00                  jmp 0x140b182f6
0087A614  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
0087A61C  44 8B CB                        mov r9d, ebx
0087A61F  E9 EB FD FF FF                  jmp 0x14087a40f
0087A624  E8 17 7C 1F 00                  call 0x140a72240
0087A629  48 8B 05 F0 F6 75 00            mov rax, qword ptr [rip + 0x75f6f0]
0087A630  48 8D 0D E1 F6 75 00            lea rcx, [rip + 0x75f6e1]
0087A637  48 39 08                        cmp qword ptr [rax], rcx
0087A63A  0F 84 D9 DC 29 00               je 0x140b18319
0087A640  B9 03 00 00 00                  mov ecx, 3
0087A645  CD 29                           int 0x29
0087A647  44 8B 4D 94                     mov r9d, dword ptr [rbp - 0x6c]
0087A64B  4D 8B C7                        mov r8, r15
0087A64E  41 8B D4                        mov edx, r12d
0087A651  48 8B CF                        mov rcx, rdi
0087A654  E8 F7 BB F6 FF                  call 0x1407e6250
0087A659  E9 20 FC FF FF                  jmp 0x14087a27e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCreateHive(__int64 a1, int a2, int a3, int a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned int v_stack_m1E8;
    unsigned int v_stack_m1EC;
    unsigned int v_stack_m1F0;
    unsigned __int8 v_stack_m1F3;
    unsigned __int8 v_stack_m1F4;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned int v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p38;

    v_rsp = (v_rsp) - (568);
    result = (*(unsigned __int64 *)(v_rip + 5835053)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rbx = 0;
    v_stack_m1E8 = a2;
    v_stack_m1E0 = a7;
    v_stack_m1C0 = a9;
    v_stack_m1C8 = a10;
    v_stack_m1D0 = a12;
    a2 = 0;
    v_stack_m1A8 = a1;
    v_stack_m1F0 = a4;
    v_stack_m1D8 = a5;
    v_stack_m160 = 0;
    v_stack_m1E4 = 0;
    v_stack_m1F4 = 0;
    v_stack_m1F3 = 0;
    v_stack_m1B8 = 0;
    v_stack_m180 = v_xmm0;
    v_stack_m170 = v_xmm0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    v_stack_m138 = v_xmm0;
    v_stack_m1A0 = v_xmm0;
    v_stack_m190 = v_xmm1;
    if (((unsigned int)((unsigned int)(a2))) > 2) goto loc_0087A2B9;
loc_00879EB7:
    if ((((unsigned int)((unsigned int)(a3))) & (0xF5617CECULL)) != 0) goto loc_0087A46A;
    if (a4 > 2) goto loc_0087A474;
    if (a5 != 0) goto loc_00879EE0;
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_0087A487;
loc_00879EE0:
    if (a6 == 0) goto loc_00879F2D;
    if (((1) & ((unsigned __int8)((unsigned int)(a3)))) != 0) goto loc_0087A494;
loc_00879EEE:
    if (*(unsigned __int64 *)(a6) == 0) goto loc_0087A4A4;
loc_00879EFB:
    if (*(unsigned __int64 *)(a6 + 8) == 0) goto loc_00879F0E;
    if (a4 == 0) goto loc_0087A4BF;
loc_00879F0E:
    if (*(unsigned __int64 *)(a6 + 16) == 0) goto loc_00879F22;
    if (a4 != 2) goto loc_0087A4CC;
loc_00879F22:
    if ((*(unsigned __int64 *)(a6 + 24)) != 0) goto loc_0087A4D9;
loc_00879F2D:
    result = CmpAcquireShutdownRundown(*(unsigned __int64 *)(a6 + 8), *(unsigned __int64 *)(a6), a3, a4);
    v_stack_m1F4 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_0087A4F9;
    v_stack_m1EC = 1;
    if (a6 == 0) goto loc_00879F52;
    if (*(unsigned __int64 *)(a6) != 0) goto loc_0087A43F;
loc_00879F52:
    result = ExAllocatePool2(32 + 32, 32, (unsigned int)(0x35394D43ULL), a4);
    if (result == 0) goto loc_0087A525;
    a2 = 0;
    if (condition_is_below) goto loc_0087A305;
    result = CmpAllocate((unsigned int)(0x12D8ULL), a2, (unsigned int)(0x30314D43ULL), a4);
loc_00879F8E:
    if (result == 0) goto loc_0087A459;
    result = CmpHiveInitialize(result, result, (unsigned int)(0x30314D43ULL), a4);
    if (a6 != 0) goto loc_0087A30F;
loc_00879FAE:
    if (condition_is_below) goto loc_0087A546;
loc_00879FC0:
    if (sign_flag) goto loc_0087A553;
loc_00879FC9:
    result = CmpAttachToRegistryProcess(v_stack_m158, result, (unsigned int)(0x30314D43ULL), a4);
    v_stack_m1F3 = 1;
    result = v_rip - 180898;
    if (condition_is_below) { result = v_rip - 3804409; }
    v_stack_m180 = result;
    v_stack_m178 = v_rip - 182024;
    v_stack_m168 = v_rip + 2013245;
    v_stack_m160 = v_rip + 2046898;
    *(unsigned __int64 *)(result + 56) = a13;
    *(unsigned __int64 *)(a13) = result;
    if (((unsigned int)((unsigned int)(v_stack_m1E8))) == 2) goto loc_0087A0D4;
    if (((unsigned int)((unsigned int)(v_stack_m1E8))) == 5) goto loc_0087A0D4;
    if ((unsigned int)((unsigned int)(v_stack_m1E8)) == 0) goto loc_0087A560;
loc_0087A036:
    if (a11 != 0) goto loc_0087A579;
loc_0087A04D:
    v_stack_m200 = a13;
    v_stack_m208 = v_stack_m1E4;
    v_stack_m210 = v_stack_m1D0;
    v_stack_m218 = v_stack_m1B8;
    v_stack_m220 = v_stack_m1B8;
    v_stack_m228 = v_stack_m1C8;
    v_stack_m230 = v_stack_m1C0;
    v_stack_m238 = (unsigned int)((unsigned int)(a8));
    v_stack_m240 = v_stack_m1E0;
    v_stack_m248 = (unsigned int)((unsigned int)(v_stack_m1EC));
    v_stack_m250 = v_stack_m180;
    v_stack_m258 = v_stack_m1D8;
    result = HvHiveStartMemoryBacked(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1E8))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(v_stack_m1F0));
    if (!sign_flag) goto loc_0087A192;
    v_stack_m258 = 232;
    goto loc_0087A40C;
loc_0087A0D4:
    result = CmpVolumeManagerGetContextForFile(result, *(unsigned __int64 *)((unsigned int)(v_stack_m1E8)), (unsigned int)((unsigned int)((unsigned int)(a3))), result + 4792);
    if (sign_flag) goto loc_0087A41C;
    result = CmpVolumeContextMustHiveFilePagesBeKeptLocal(*(unsigned __int64 *)(result + 4792), *(unsigned __int64 *)((unsigned int)(v_stack_m1E8)), (unsigned int)((unsigned int)((unsigned int)(a3))), result + 4792);
    result = CmpVolumeContextCanHiveSectionBeExtended(*(unsigned __int64 *)(result + 4792), *(unsigned __int64 *)((unsigned int)(v_stack_m1E8)), (unsigned int)((unsigned int)((unsigned int)(a3))), result + 4792);
    v_stack_m210 = a13;
    v_stack_m218 = v_stack_m1E4;
    a1 = (unsigned int)((unsigned int)((unsigned int)(a3)));
    if ((unsigned __int8)(result) != 0) { a1 = (unsigned int)((unsigned int)(a3)); }
    v_stack_m220 = v_stack_m1D0;
    v_stack_m228 = v_stack_m1C8;
    a2 = ((unsigned int)((unsigned int)(v_stack_m1E8)) == 0) ? 1 : 0;
    v_stack_m230 = v_stack_m1C0;
    v_stack_m238 = (unsigned int)((unsigned int)(a8));
    v_stack_m240 = v_stack_m1E0;
    v_stack_m250 = (unsigned int)((unsigned int)(v_stack_m1EC));
    v_stack_m258 = v_stack_m180;
    result = HvHiveStartFileBacked(result, a2, (unsigned int)((unsigned int)(a1)), (unsigned int)(v_stack_m1F0));
    if (sign_flag) goto loc_0087A5A5;
loc_0087A192:
    if (condition_is_below) goto loc_0087A5B2;
loc_0087A19D:
loc_0087A1A3:
    if ((((unsigned int)((unsigned int)(v_stack_m1E8) - 1)) & (0xFFFFFFFAULL)) != 0) goto loc_0087A1DC;
    if (((unsigned int)((unsigned int)(v_stack_m1E8))) == 6) goto loc_0087A1DC;
    result = CmCheckRegistry(result, (unsigned int)((unsigned int)((unsigned int)(a8))), a13, (unsigned int)(v_stack_m1F0));
    if (sign_flag) goto loc_0087A404;
loc_0087A1DC:
    v_rbx = 0;
    if (condition_is_below) goto loc_0087A5F2;
loc_0087A1E9:
    result = CmpReorganizeHive(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    result = CmpLockRegistry(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    result = HvLockHiveFlusherShared(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    result = HvLockHiveWriter(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    if ((unsigned int)((unsigned int)(v_stack_m1E8)) == 0) goto loc_0087A433;
    result = HvCheckAndUpdateHiveBackupTimeStamp(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
loc_0087A223:
    result = HvUnlockHiveWriter(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    result = HvUnlockHiveFlusherShared(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    result = CmpUnlockRegistry(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    if (sign_flag) goto loc_0087A614;
    if (condition_is_above_or_equal) goto loc_0087A624;
    *(unsigned __int64 *)(result + 1608 + 8) = result + 1608;
    *(unsigned __int64 *)(result + 1608) = result + 1608;
    *(unsigned __int64 *)(v_stack_m1A8) = result;
    result = CmpReleaseShutdownRundown(result, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    v_stack_m1F4 = 0;
    if (((*(unsigned int *)(v_rip + 7653524)) & (0x1000000ULL)) != 0) goto loc_0087A647;
loc_0087A27E:
    v_rbx = 0;
loc_0087A280:
    result = CmpDetachFromRegistryProcess(v_stack_m158, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
loc_0087A289:
    if (v_stack_m1F4 != 0) goto loc_0087A51B;
loc_0087A293:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1E0, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(v_stack_m1F0));
    v_rsp = (v_rsp) + (568);
    return result;
loc_0087A2B9:
    if (((unsigned int)(result)) == 5) goto loc_00879EB7;
    result = 0;
loc_0087A2CE:
    v_stack_p20 = 0;
    result = SetFailureLocation(a13, v_stack_m1E0, 1, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    if ((unsigned int)(a8) == 0) goto loc_0087A289;
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(a8), a2, 1, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    v_stack_m1F4 = (unsigned __int8)(v_stack_m1F4);
    v_stack_m1F3 = 0;
    if (result == 0) goto loc_0087A289;
    goto loc_0087A41C;
loc_0087A305:
    result = CmpAllocateForNonPagedHive((unsigned int)(a8), a2, 1, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_00879F8E;
loc_0087A30F:
    if (*(unsigned __int64 *)((unsigned int)(v_stack_m1E8)) == 0) goto loc_0087A36F;
    v_stack_p38 = (unsigned __int8)((unsigned int)(0xC000000DULL));
    v_stack_p30 = 2;
    a3 = 0;
    v_stack_p28 = 512;
    v_stack_p20 = (unsigned int)((unsigned int)(0xC000000DULL));
    result = ObDuplicateObject(*(unsigned __int64 *)(v_rip + 7653265), *(unsigned __int64 *)((unsigned int)(v_stack_m1E8)), a3, result + 1544);
    if (sign_flag) goto loc_0087A41C;
    v_rbx = 0;
    v_stack_m1F8 = 256;
    result = ZwSetInformationObject(*(unsigned __int64 *)(result + 1544), v_rbx + 4, v_stack_m1F8, v_rbx + 2);
loc_0087A36F:
    if (((unsigned int)((unsigned int)(v_stack_m1F0))) == ((unsigned int)(v_stack_m1F4))) goto loc_0087A52C;
    if (((unsigned int)((unsigned int)(v_stack_m1F0))) != 2) goto loc_00879FAE;
    if (*(unsigned __int64 *)((unsigned int)(v_stack_m1E8) + 8) == 0) goto loc_0087A3EA;
    v_stack_p38 = 0;
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_m1F0));
    a3 = 0;
    v_stack_p28 = 512;
    v_stack_p20 = 0;
    result = ObDuplicateObject(*(unsigned __int64 *)(v_rip + 7653134), *(unsigned __int64 *)((unsigned int)(v_stack_m1E8) + 8), a3, result + 1576);
    if (sign_flag) goto loc_0087A41C;
    v_rbx = 0;
    v_stack_m1F8 = 256;
    result = ZwSetInformationObject(*(unsigned __int64 *)(result + 1576), v_rbx + 4, v_stack_m1F8, v_rbx + 2);
loc_0087A3EA:
    if (*(unsigned __int64 *)((unsigned int)(v_stack_m1E8) + 16) == 0) goto loc_00879FAE;
loc_0087A404:
    v_stack_p20 = 240;
loc_0087A40C:
loc_0087A40F:
    a2 = 0;
    result = SetFailureLocation(a13, a2, (unsigned int)((unsigned int)(v_stack_m1F4)), (unsigned int)((unsigned int)(result)));
loc_0087A41C:
    result = CmpDestroyHive(result, a2, (unsigned int)((unsigned int)(v_stack_m1F4)), (unsigned int)((unsigned int)(result)));
    if (v_stack_m1F3 != 0) goto loc_0087A280;
    goto loc_0087A289;
loc_0087A433:
    *(unsigned __int8 *)(result + 195) = (unsigned __int8)(v_stack_m1F4);
    goto loc_0087A223;
loc_0087A43F:
    result = CmpGetVolumeClusterSize(result, v_stack_m1EC, (unsigned int)((unsigned int)(v_stack_m1F4)), (unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_0087A503;
    v_rbx = 0;
    goto loc_00879F52;
loc_0087A459:
    a2 = 0;
    goto loc_0087A2CE;
loc_0087A46A:
    v_stack_p20 = 16;
    goto loc_0087A47C;
loc_0087A474:
    v_stack_p20 = 32;
loc_0087A47C:
loc_0087A487:
    v_stack_p20 = 48;
loc_0087A494:
    if (condition_is_below) goto loc_00879EEE;
loc_0087A4A4:
    if ((*(unsigned __int64 *)((unsigned int)(v_stack_m1E8) + 16)) == ((unsigned int)(0xC000009AULL))) goto loc_00879EFB;
loc_0087A4BF:
    v_stack_p20 = 96;
loc_0087A4CC:
    v_stack_p20 = 112;
loc_0087A4D9:
    if (176 == 0) goto loc_00879F2D;
loc_0087A4F9:
    goto loc_0087A293;
loc_0087A503:
    v_stack_p20 = 160;
    a2 = 0;
    result = SetFailureLocation(a13, a2, (unsigned int)((unsigned int)(v_stack_m1F4)), 176);
loc_0087A51B:
    result = CmpReleaseShutdownRundown(a13, a2, (unsigned int)((unsigned int)(v_stack_m1F4)), 176);
    goto loc_0087A293;
loc_0087A525:
    goto loc_0087A51B;
loc_0087A52C:
    if (*(unsigned __int64 *)((unsigned int)(v_stack_m1E8) + 8) == 0) goto loc_00879FAE;
loc_0087A546:
    goto loc_00879FC0;
loc_0087A553:
    goto loc_00879FC9;
loc_0087A560:
    if ((unsigned int)(v_stack_m1E8) == 0) goto loc_0087A036;
    if ((*(unsigned __int64 *)((unsigned int)(v_stack_m1E8))) != 0) goto loc_0087A0D4;
    goto loc_0087A036;
loc_0087A579:
    v_stack_m1A0 = (unsigned int)((unsigned int)(*(unsigned int *)(a13 + 112)));
    v_stack_m198 = *(unsigned __int64 *)(a13 + 104);
    v_stack_m190 = (unsigned int)((unsigned int)(*(unsigned int *)(a13 + 128)));
    v_stack_m188 = *(unsigned __int64 *)(a13 + 120);
    goto loc_0087A04D;
loc_0087A5A5:
    v_stack_p20 = 228;
    goto loc_0087A40C;
loc_0087A5B2:
    a1 = ((*(unsigned __int64 *)((unsigned int)(v_stack_m1E8))) >= 0) ? 1 : 0;
    result = ((*(unsigned __int64 *)((unsigned int)(v_stack_m1E8))) >= 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0087A19D;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 64) + 144))))) != 0) goto loc_0087A1A3;
loc_0087A5F2:
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 64) + 144))))) != 0) goto loc_0087A1E9;
loc_0087A614:
    v_stack_p20 = 256;
    goto loc_0087A40F;
loc_0087A624:
    result = CmpLockHiveListExclusive(a1, *(unsigned __int64 *)((unsigned int)(v_stack_m1E8) + 8), (unsigned int)((unsigned int)(v_stack_m1F4)), (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))));
loc_0087A647:
    result = CmpLogHiveInitializeEvent(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1E8))), 2, (unsigned int)(v_stack_m1E4));
    goto loc_0087A27E;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCreateHive(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, void *Arg13)
{
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint32_t v_stack_m1E8;
    uint32_t v_stack_m1EC;
    uint32_t v_stack_m1F0;
    uint8_t v_stack_m1F3;
    uint8_t v_stack_m1F4;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint32_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m58;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p38;

    local_rsp = (local_rsp) - (568);
    result = (*(uint64_t *)(v_rip + 0x59092D)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rbx = 0;
    v_stack_m1E8 = Arg2;
    v_stack_m1E0 = Arg7;
    v_stack_m1C0 = Arg9;
    v_stack_m1C8 = Arg10;
    v_stack_m1D0 = Arg12;
    Arg2 = 0;
    v_stack_m1A8 = Arg1;
    v_stack_m1F0 = Arg4;
    v_stack_m1D8 = Arg5;
    v_stack_m160 = 0;
    v_stack_m1E4 = 0;
    v_stack_m1F4 = 0;
    v_stack_m1F3 = 0;
    v_stack_m1B8 = 0;
    v_stack_m180 = v_xmm0;
    v_stack_m170 = v_xmm0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    v_stack_m138 = v_xmm0;
    v_stack_m1A0 = v_xmm0;
    v_stack_m190 = v_xmm1;
    if (((uint32_t)((uint32_t)(Arg2))) > 2) goto loc_0087A2B9;
loc_00879EB7:
    if ((((uint32_t)((uint32_t)(Arg3))) & (0xF5617CECULL)) != 0) goto loc_0087A46A;
    if (Arg4 > 2) goto loc_0087A474;
    if (Arg5 != 0) goto loc_00879EE0;
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_0087A487;
loc_00879EE0:
    if (Arg6 == 0) goto loc_00879F2D;
    if (((1) & ((uint8_t)((uint32_t)(Arg3)))) != 0) goto loc_0087A494;
loc_00879EEE:
    if (*(uint64_t *)(Arg6) == 0) goto loc_0087A4A4;
loc_00879EFB:
    if (*(uint64_t *)(Arg6 + 0x8) == 0) goto loc_00879F0E;
    if (Arg4 == 0) goto loc_0087A4BF;
loc_00879F0E:
    if (*(uint64_t *)(Arg6 + 0x10) == 0) goto loc_00879F22;
    if (Arg4 != 2) goto loc_0087A4CC;
loc_00879F22:
    if ((*(uint64_t *)(Arg6 + 0x18)) != 0) goto loc_0087A4D9;
loc_00879F2D:
    result = CmpAcquireShutdownRundown(*(uint64_t *)(Arg6 + 0x8), *(uint64_t *)(Arg6), Arg3, Arg4);
    v_stack_m1F4 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_0087A4F9;
    v_stack_m1EC = 1;
    if (Arg6 == 0) goto loc_00879F52;
    if (*(uint64_t *)(Arg6) != 0) goto loc_0087A43F;
loc_00879F52:
    result = ExAllocatePool2(32 + 32, 32, (uint32_t)(0x35394D43ULL), Arg4);
    if (result == 0) goto loc_0087A525;
    Arg2 = 0;
    if (condition_is_below) goto loc_0087A305;
    result = CmpAllocate((uint32_t)(0x12D8ULL), Arg2, (uint32_t)(0x30314D43ULL), Arg4);
loc_00879F8E:
    if (result == 0) goto loc_0087A459;
    result = CmpHiveInitialize(result, result, (uint32_t)(0x30314D43ULL), Arg4);
    if (Arg6 != 0) goto loc_0087A30F;
loc_00879FAE:
    if (condition_is_below) goto loc_0087A546;
loc_00879FC0:
    if (sign_flag) goto loc_0087A553;
loc_00879FC9:
    result = CmpAttachToRegistryProcess(v_stack_m158, result, (uint32_t)(0x30314D43ULL), Arg4);
    v_stack_m1F3 = 1;
    result = v_rip - 180898;
    if (condition_is_below) { result = v_rip - 3804409; }
    v_stack_m180 = result;
    v_stack_m178 = v_rip - 182024;
    v_stack_m168 = v_rip + 2013245;
    v_stack_m160 = v_rip + 2046898;
    *(void **)(result + 0x38) = Arg13;
    *(uint64_t *)(arg13) = result;
    if (((uint32_t)((uint32_t)(v_stack_m1E8))) == 2) goto loc_0087A0D4;
    if (((uint32_t)((uint32_t)(v_stack_m1E8))) == 5) goto loc_0087A0D4;
    if ((uint32_t)((uint32_t)(v_stack_m1E8)) == 0) goto loc_0087A560;
loc_0087A036:
    if (Arg11 != 0) goto loc_0087A579;
loc_0087A04D:
    v_stack_m200 = Arg13;
    v_stack_m208 = v_stack_m1E4;
    v_stack_m210 = v_stack_m1D0;
    v_stack_m218 = v_stack_m1B8;
    v_stack_m220 = v_stack_m1B8;
    v_stack_m228 = v_stack_m1C8;
    v_stack_m230 = v_stack_m1C0;
    v_stack_m238 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m240 = v_stack_m1E0;
    v_stack_m248 = (uint32_t)((uint32_t)(v_stack_m1EC));
    v_stack_m250 = v_stack_m180;
    v_stack_m258 = v_stack_m1D8;
    result = HvHiveStartMemoryBacked(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1E8))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(v_stack_m1F0));
    if (!sign_flag) goto loc_0087A192;
    v_stack_m258 = 232;
    goto loc_0087A40C;
loc_0087A0D4:
    result = CmpVolumeManagerGetContextForFile(result, *(uint64_t *)((uint32_t)(v_stack_m1E8)), (uint32_t)((uint32_t)((uint32_t)(Arg3))), result + 4792);
    if (sign_flag) goto loc_0087A41C;
    result = CmpVolumeContextMustHiveFilePagesBeKeptLocal(*(uint64_t *)(result + 0x12B8), *(uint64_t *)((uint32_t)(v_stack_m1E8)), (uint32_t)((uint32_t)((uint32_t)(Arg3))), result + 4792);
    result = CmpVolumeContextCanHiveSectionBeExtended(*(uint64_t *)(result + 0x12B8), *(uint64_t *)((uint32_t)(v_stack_m1E8)), (uint32_t)((uint32_t)((uint32_t)(Arg3))), result + 4792);
    v_stack_m210 = Arg13;
    v_stack_m218 = v_stack_m1E4;
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(Arg3)));
    if ((uint8_t)(result) != 0) { Arg1 = (uint32_t)((uint32_t)(Arg3)); }
    v_stack_m220 = v_stack_m1D0;
    v_stack_m228 = v_stack_m1C8;
    Arg2 = ((uint32_t)((uint32_t)(v_stack_m1E8)) == 0) ? 1 : 0;
    v_stack_m230 = v_stack_m1C0;
    v_stack_m238 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m240 = v_stack_m1E0;
    v_stack_m250 = (uint32_t)((uint32_t)(v_stack_m1EC));
    v_stack_m258 = v_stack_m180;
    result = HvHiveStartFileBacked(result, Arg2, (uint32_t)((uint32_t)(Arg1)), (uint32_t)(v_stack_m1F0));
    if (sign_flag) goto loc_0087A5A5;
loc_0087A192:
    if (condition_is_below) goto loc_0087A5B2;
loc_0087A19D:
loc_0087A1A3:
    if ((((uint32_t)((uint32_t)(v_stack_m1E8) - 1)) & (0xFFFFFFFAULL)) != 0) goto loc_0087A1DC;
    if (((uint32_t)((uint32_t)(v_stack_m1E8))) == 6) goto loc_0087A1DC;
    result = CmCheckRegistry(result, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg13, (uint32_t)(v_stack_m1F0));
    if (sign_flag) goto loc_0087A404;
loc_0087A1DC:
    local_rbx = 0;
    if (condition_is_below) goto loc_0087A5F2;
loc_0087A1E9:
    result = CmpReorganizeHive(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    result = CmpLockRegistry(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    result = HvLockHiveFlusherShared(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    result = HvLockHiveWriter(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    if ((uint32_t)((uint32_t)(v_stack_m1E8)) == 0) goto loc_0087A433;
    result = HvCheckAndUpdateHiveBackupTimeStamp(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
loc_0087A223:
    result = HvUnlockHiveWriter(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    result = HvUnlockHiveFlusherShared(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    result = CmpUnlockRegistry(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    if (sign_flag) goto loc_0087A614;
    if (condition_is_above_or_equal) goto loc_0087A624;
    *(uint64_t *)(result + 0x648 + 0x8) = result + 1608;
    *(uint64_t *)(result + 0x648) = result + 1608;
    *(uint64_t *)(v_stack_m1A8) = result;
    result = CmpReleaseShutdownRundown(result, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    v_stack_m1F4 = 0;
    if (((*(uint32_t *)(v_rip + 0x74C894)) & (0x1000000ULL)) != 0) goto loc_0087A647;
loc_0087A27E:
    local_rbx = 0;
loc_0087A280:
    result = CmpDetachFromRegistryProcess(v_stack_m158, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
loc_0087A289:
    if (v_stack_m1F4 != 0) goto loc_0087A51B;
loc_0087A293:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1E0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(v_stack_m1F0));
    local_rsp = (local_rsp) + (568);
    return result;
loc_0087A2B9:
    if (((uint32_t)(result)) == 5) goto loc_00879EB7;
    result = 0;
loc_0087A2CE:
    v_stack_p20 = 0;
    result = SetFailureLocation(Arg13, v_stack_m1E0, 1, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    if ((uint32_t)(Arg8) == 0) goto loc_0087A289;
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(Arg8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    v_stack_m1F4 = (uint8_t)(v_stack_m1F4);
    v_stack_m1F3 = 0;
    if (result == 0) goto loc_0087A289;
    goto loc_0087A41C;
loc_0087A305:
    result = CmpAllocateForNonPagedHive((uint32_t)(Arg8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_00879F8E;
loc_0087A30F:
    if (*(uint64_t *)((uint32_t)(v_stack_m1E8)) == 0) goto loc_0087A36F;
    v_stack_p38 = (uint8_t)((uint32_t)(0xC000000DULL));
    v_stack_p30 = 2;
    Arg3 = 0;
    v_stack_p28 = 512;
    v_stack_p20 = (uint32_t)((uint32_t)(0xC000000DULL));
    result = ObDuplicateObject(*(uint64_t *)(v_rip + 0x74C791), *(uint64_t *)((uint32_t)(v_stack_m1E8)), Arg3, result + 1544);
    if (sign_flag) goto loc_0087A41C;
    local_rbx = 0;
    v_stack_m1F8 = 256;
    result = ZwSetInformationObject(*(uint64_t *)(result + 0x608), local_rbx + 4, v_stack_m1F8, local_rbx + 2);
loc_0087A36F:
    if (((uint32_t)((uint32_t)(v_stack_m1F0))) == ((uint32_t)(v_stack_m1F4))) goto loc_0087A52C;
    if (((uint32_t)((uint32_t)(v_stack_m1F0))) != 2) goto loc_00879FAE;
    if (*(uint64_t *)((uint32_t)(v_stack_m1E8) + 0x8) == 0) goto loc_0087A3EA;
    v_stack_p38 = 0;
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_m1F0));
    Arg3 = 0;
    v_stack_p28 = 512;
    v_stack_p20 = 0;
    result = ObDuplicateObject(*(uint64_t *)(v_rip + 0x74C70E), *(uint64_t *)((uint32_t)(v_stack_m1E8) + 0x8), Arg3, result + 1576);
    if (sign_flag) goto loc_0087A41C;
    local_rbx = 0;
    v_stack_m1F8 = 256;
    result = ZwSetInformationObject(*(uint64_t *)(result + 0x628), local_rbx + 4, v_stack_m1F8, local_rbx + 2);
loc_0087A3EA:
    if (*(uint64_t *)((uint32_t)(v_stack_m1E8) + 0x10) == 0) goto loc_00879FAE;
loc_0087A404:
    v_stack_p20 = 240;
loc_0087A40C:
loc_0087A40F:
    Arg2 = 0;
    result = SetFailureLocation(Arg13, Arg2, (uint32_t)((uint32_t)(v_stack_m1F4)), (uint32_t)((uint32_t)(result)));
loc_0087A41C:
    result = CmpDestroyHive(result, Arg2, (uint32_t)((uint32_t)(v_stack_m1F4)), (uint32_t)((uint32_t)(result)));
    if (v_stack_m1F3 != 0) goto loc_0087A280;
    goto loc_0087A289;
loc_0087A433:
    *(uint8_t *)(result + 0xC3) = (uint8_t)(v_stack_m1F4);
    goto loc_0087A223;
loc_0087A43F:
    result = CmpGetVolumeClusterSize(result, v_stack_m1EC, (uint32_t)((uint32_t)(v_stack_m1F4)), (uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_0087A503;
    local_rbx = 0;
    goto loc_00879F52;
loc_0087A459:
    Arg2 = 0;
    goto loc_0087A2CE;
loc_0087A46A:
    v_stack_p20 = 16;
    goto loc_0087A47C;
loc_0087A474:
    v_stack_p20 = 32;
loc_0087A47C:
loc_0087A487:
    v_stack_p20 = 48;
loc_0087A494:
    if (condition_is_below) goto loc_00879EEE;
loc_0087A4A4:
    if ((*(uint64_t *)((uint32_t)(v_stack_m1E8) + 0x10)) == ((uint32_t)(0xC000009AULL))) goto loc_00879EFB;
loc_0087A4BF:
    v_stack_p20 = 96;
loc_0087A4CC:
    v_stack_p20 = 112;
loc_0087A4D9:
    if (176 == 0) goto loc_00879F2D;
loc_0087A4F9:
    goto loc_0087A293;
loc_0087A503:
    v_stack_p20 = 160;
    Arg2 = 0;
    result = SetFailureLocation(Arg13, Arg2, (uint32_t)((uint32_t)(v_stack_m1F4)), 176);
loc_0087A51B:
    result = CmpReleaseShutdownRundown(Arg13, Arg2, (uint32_t)((uint32_t)(v_stack_m1F4)), 176);
    goto loc_0087A293;
loc_0087A525:
    goto loc_0087A51B;
loc_0087A52C:
    if (*(uint64_t *)((uint32_t)(v_stack_m1E8) + 0x8) == 0) goto loc_00879FAE;
loc_0087A546:
    goto loc_00879FC0;
loc_0087A553:
    goto loc_00879FC9;
loc_0087A560:
    if ((uint32_t)(v_stack_m1E8) == 0) goto loc_0087A036;
    if ((*(uint64_t *)((uint32_t)(v_stack_m1E8))) != 0) goto loc_0087A0D4;
    goto loc_0087A036;
loc_0087A579:
    v_stack_m1A0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg13 + 0x70)));
    v_stack_m198 = *(uint64_t *)(arg13 + 0x68);
    v_stack_m190 = (uint32_t)((uint32_t)(*(uint32_t *)(arg13 + 0x80)));
    v_stack_m188 = *(uint64_t *)(arg13 + 0x78);
    goto loc_0087A04D;
loc_0087A5A5:
    v_stack_p20 = 228;
    goto loc_0087A40C;
loc_0087A5B2:
    Arg1 = ((*(uint64_t *)((uint32_t)(v_stack_m1E8))) >= 0) ? 1 : 0;
    result = ((*(uint64_t *)((uint32_t)(v_stack_m1E8))) >= 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0087A19D;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x90))))) != 0) goto loc_0087A1A3;
loc_0087A5F2:
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x90))))) != 0) goto loc_0087A1E9;
loc_0087A614:
    v_stack_p20 = 256;
    goto loc_0087A40F;
loc_0087A624:
    result = CmpLockHiveListExclusive(Arg1, *(uint64_t *)((uint32_t)(v_stack_m1E8) + 0x8), (uint32_t)((uint32_t)(v_stack_m1F4)), (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))));
loc_0087A647:
    result = CmpLogHiveInitializeEvent(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1E8))), 2, (uint32_t)(v_stack_m1E4));
    goto loc_0087A27E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg13` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00879DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
