# EtwpAddRegEntryToGroup

- RVA: `0x009F39D4`–`0x009F42A5` (길이 `2,257` bytes)
- VA: `0x00000001409F39D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A62AC`
- 디코드: `568`개 명령, `2,257/2,257` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **59**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x009F3A52` → [EtwpFindOrCreateGuidEntry](../8C/EtwpFindOrCreateGuidEntry_function_008C1B70.md) (function, `0x008C1B70`)
- `0x009F3A8D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F3AA6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009F3AED` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F3B06` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009F3B3E` → [EtwpGetSchematizedFilterSize](EtwpGetSchematizedFilterSize_function_009FE308.md) (function, `0x009FE308`)
- `0x009F3B6E` → [EtwpReferenceGuidEntry](../8C/EtwpReferenceGuidEntry_function_008C1ED0.md) (function, `0x008C1ED0`)
- `0x009F3BE1` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x009F3BF4` → [EtwpIsGuidAllowed](../9E/EtwpIsGuidAllowed_function_009EB45C.md) (function, `0x009EB45C`)
- `0x009F3C10` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F3C2F` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009F3C52` → [EtwpAccessCheckFromState](../8C/EtwpAccessCheckFromState_function_008C0350.md) (function, `0x008C0350`)
- `0x009F3C73` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009F3C7B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F3C99` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x009F3CD5` → [EtwpApplyScopeFilters](../8C/EtwpApplyScopeFilters_function_008C3470.md) (function, `0x008C3470`)
- `0x009F3D26` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x009F3D39` → [EtwpIsGuidAllowed](../9E/EtwpIsGuidAllowed_function_009EB45C.md) (function, `0x009EB45C`)
- `0x009F3D55` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F3D74` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009F3D97` → [EtwpAccessCheckFromState](../8C/EtwpAccessCheckFromState_function_008C0350.md) (function, `0x008C0350`)
- `0x009F3DB8` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009F3DC0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F3DDE` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x009F3E1A` → [EtwpApplyScopeFilters](../8C/EtwpApplyScopeFilters_function_008C3470.md) (function, `0x008C3470`)
- `0x009F3E80` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x009F3EB1` → [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) (function, `0x00A03F94`)
- `0x009F3EC3` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009F3EE5` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009F3EF3` → [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) (function, `0x00A03F94`)
- `0x009F3EFE` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009F3F0E` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009F3F18` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x009F3F7A` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x009F3FAB` → [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) (function, `0x00A03F94`)
- `0x009F3FBD` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009F3FDF` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009F3FED` → [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) (function, `0x00A03F94`)
- `0x009F3FF8` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009F4008` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009F4012` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x009F4061` → [EtwpComputeRegEntryEnableInfo](../8C/EtwpComputeRegEntryEnableInfo_function_008C0FE0.md) (function, `0x008C0FE0`)
- `0x009F407E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F40AF` → [EtwpCopySchematizedFilters](../8C/EtwpCopySchematizedFilters_function_008C380C.md) (function, `0x008C380C`)
- `0x009F40E6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009F40F5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F4107` → [EtwpComputeRegEntryEnableInfo](../8C/EtwpComputeRegEntryEnableInfo_function_008C0FE0.md) (function, `0x008C0FE0`)
- `0x009F411F` → [EtwpGetSchematizedFilterSize](EtwpGetSchematizedFilterSize_function_009FE308.md) (function, `0x009FE308`)
- `0x009F415A` → [EtwpCopySchematizedFilters](../8C/EtwpCopySchematizedFilters_function_008C380C.md) (function, `0x008C380C`)
- `0x009F41A6` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x009F41AE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F41B3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009F41F2` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x009F41FA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F41FF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009F420E` → [EtwpUnreferenceGuidEntry](../8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x009F4225` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009F4276` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x009F4284` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpSetProviderTraitsCommon](EtwpSetProviderTraitsCommon_function_009F36EC.md) at `0x009F38B2`

### Static image references
- `0x009F39F0` → RVA `0x00E0A740` (`.data`; read)
- `0x009F3D1F` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x009F40DF` → RVA `0x000112D0` (`.rdata`; read)
- `0x009F4217` → RVA `0x00EFF840` (`.data`; read)
- `0x009F421E` → RVA `0x0001A820` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x009F3A8D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F3AA6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009F3AED` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F3B06` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009F3C10` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F3C2F` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009F3C73` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009F3C7B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F3D55` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F3D74` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009F3DB8` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009F3DC0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F3EC3` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009F3EE5` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009F3EFE` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009F3F0E` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009F3FBD` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009F3FDF` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009F3FF8` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009F4008` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009F407E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F40E6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009F40F5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F41A6` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x009F41AE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F41B3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009F41F2` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x009F41FA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F41FF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009F4225` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009F4276` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x009F4284` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F39D4  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009F39D9  55                              push rbp
009F39DA  56                              push rsi
009F39DB  57                              push rdi
009F39DC  41 54                           push r12
009F39DE  41 55                           push r13
009F39E0  41 56                           push r14
009F39E2  41 57                           push r15
009F39E4  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
009F39E9  48 81 EC 30 01 00 00            sub rsp, 0x130
009F39F0  48 8B 05 49 6D 41 00            mov rax, qword ptr [rip + 0x416d49]
009F39F7  48 33 C4                        xor rax, rsp
009F39FA  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
009F39FE  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
009F3A02  45 8B F1                        mov r14d, r9d
009F3A05  44 8A 49 62                     mov r9b, byte ptr [rcx + 0x62]
009F3A09  45 33 E4                        xor r12d, r12d
009F3A0C  4C 8B BD 90 00 00 00            mov r15, qword ptr [rbp + 0x90]
009F3A13  48 8B D9                        mov rbx, rcx
009F3A16  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
009F3A1B  41 D0 E9                        shr r9b, 1
009F3A1E  48 8B 80 88 02 00 00            mov rax, qword ptr [rax + 0x288]
009F3A25  41 80 E1 01                     and r9b, 1
009F3A29  4C 89 45 98                     mov qword ptr [rbp - 0x68], r8
009F3A2D  45 0F B7 EC                     movzx r13d, r12w
009F3A31  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009F3A36  45 8D 44 24 02                  lea r8d, [r12 + 2]
009F3A3B  48 8B C8                        mov rcx, rax
009F3A3E  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
009F3A43  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
009F3A48  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
009F3A4D  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009F3A52  E8 19 E1 EC FF                  call 0x1408c1b70
009F3A57  8B F0                           mov esi, eax
009F3A59  85 C0                           test eax, eax
009F3A5B  0F 85 A3 07 00 00               jne 0x1409f4204
009F3A61  41 C7 07 78 00 00 00            mov dword ptr [r15], 0x78
009F3A68  45 33 C0                        xor r8d, r8d
009F3A6B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009F3A74  33 D2                           xor edx, edx
009F3A76  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
009F3A7B  48 81 C7 98 02 00 00            add rdi, 0x298
009F3A82  48 8B CF                        mov rcx, rdi
009F3A85  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009F3A8C  90                              nop
009F3A8D  E8 9E C7 81 FF                  call 0x140210230
009F3A92  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
009F3A98  48 8B F0                        mov rsi, rax
009F3A9B  73 0E                           jae 0x1409f3aab
009F3A9D  4C 8B C7                        mov r8, rdi
009F3AA0  48 8B D0                        mov rdx, rax
009F3AA3  48 8B CF                        mov rcx, rdi
009F3AA6  E8 E5 C1 81 FF                  call 0x14020fc90
009F3AAB  48 85 F6                        test rsi, rsi
009F3AAE  74 04                           je 0x1409f3ab4
009F3AB0  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
009F3AB4  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009F3ABD  45 33 C0                        xor r8d, r8d
009F3AC0  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F3AC5  33 D2                           xor edx, edx
009F3AC7  48 89 88 A0 02 00 00            mov qword ptr [rax + 0x2a0], rcx
009F3ACE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009F3AD7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009F3ADE  90                              nop
009F3ADF  48 8B 7B 20                     mov rdi, qword ptr [rbx + 0x20]
009F3AE3  48 81 C7 98 02 00 00            add rdi, 0x298
009F3AEA  48 8B CF                        mov rcx, rdi
009F3AED  E8 3E C7 81 FF                  call 0x140210230
009F3AF2  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
009F3AF8  48 8B F0                        mov rsi, rax
009F3AFB  73 0E                           jae 0x1409f3b0b
009F3AFD  4C 8B C7                        mov r8, rdi
009F3B00  48 8B D0                        mov rdx, rax
009F3B03  48 8B CF                        mov rcx, rdi
009F3B06  E8 85 C1 81 FF                  call 0x14020fc90
009F3B0B  48 85 F6                        test rsi, rsi
009F3B0E  74 04                           je 0x1409f3b14
009F3B10  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
009F3B14  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009F3B1D  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
009F3B21  48 89 88 A0 02 00 00            mov qword ptr [rax + 0x2a0], rcx
009F3B28  4C 39 63 28                     cmp qword ptr [rbx + 0x28], r12
009F3B2C  74 08                           je 0x1409f3b36
009F3B2E  41 8B F4                        mov esi, r12d
009F3B31  E9 33 06 00 00                  jmp 0x1409f4169
009F3B36  0F B7 53 64                     movzx edx, word ptr [rbx + 0x64]
009F3B3A  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009F3B3E  E8 C5 A7 00 00                  call 0x1409fe308
009F3B43  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009F3B47  85 C0                           test eax, eax
009F3B49  74 06                           je 0x1409f3b51
009F3B4B  8D 48 10                        lea ecx, [rax + 0x10]
009F3B4E  41 01 0F                        add dword ptr [r15], ecx
009F3B51  F6 43 62 02                     test byte ptr [rbx + 0x62], 2
009F3B55  74 0F                           je 0x1409f3b66
009F3B57  45 39 37                        cmp dword ptr [r15], r14d
009F3B5A  76 0A                           jbe 0x1409f3b66
009F3B5C  BE 23 00 00 C0                  mov esi, 0xc0000023
009F3B61  E9 03 06 00 00                  jmp 0x1409f4169
009F3B66  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
009F3B6B  48 8B CF                        mov rcx, rdi
009F3B6E  E8 5D E3 EC FF                  call 0x1408c1ed0
009F3B73  48 8D 4F 38                     lea rcx, [rdi + 0x38]
009F3B77  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
009F3B7B  48 8B 11                        mov rdx, qword ptr [rcx]
009F3B7E  48 8D 43 10                     lea rax, [rbx + 0x10]
009F3B82  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
009F3B86  74 07                           je 0x1409f3b8f
009F3B88  B9 03 00 00 00                  mov ecx, 3
009F3B8D  CD 29                           int 0x29
009F3B8F  48 89 10                        mov qword ptr [rax], rdx
009F3B92  48 89 48 08                     mov qword ptr [rax + 8], rcx
009F3B96  48 89 42 08                     mov qword ptr [rdx + 8], rax
009F3B9A  48 89 01                        mov qword ptr [rcx], rax
009F3B9D  44 39 67 60                     cmp dword ptr [rdi + 0x60], r12d
009F3BA1  75 1A                           jne 0x1409f3bbd
009F3BA3  48 8B 87 90 02 00 00            mov rax, qword ptr [rdi + 0x290]
009F3BAA  48 85 C0                        test rax, rax
009F3BAD  74 06                           je 0x1409f3bb5
009F3BAF  44 39 60 60                     cmp dword ptr [rax + 0x60], r12d
009F3BB3  75 08                           jne 0x1409f3bbd
009F3BB5  45 89 27                        mov dword ptr [r15], r12d
009F3BB8  E9 71 FF FF FF                  jmp 0x1409f3b2e
009F3BBD  45 8A FC                        mov r15b, r12b
009F3BC0  4C 8D A7 86 00 00 00            lea r12, [rdi + 0x86]
009F3BC7  33 FF                           xor edi, edi
009F3BC9  41 39 7C 24 FA                  cmp dword ptr [r12 - 6], edi
009F3BCE  0F 84 CA 00 00 00               je 0x1409f3c9e
009F3BD4  41 0F B7 14 24                  movzx edx, word ptr [r12]
009F3BD9  45 33 C0                        xor r8d, r8d
009F3BDC  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009F3BE1  E8 3A ED F3 FF                  call 0x140932920
009F3BE6  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
009F3BEA  48 8B C8                        mov rcx, rax
009F3BED  48 83 C2 28                     add rdx, 0x28
009F3BF1  48 8B F0                        mov rsi, rax
009F3BF4  E8 63 78 FF FF                  call 0x1409eb45c
009F3BF9  84 C0                           test al, al
009F3BFB  0F 84 93 00 00 00               je 0x1409f3c94
009F3C01  48 8D BE B0 02 00 00            lea rdi, [rsi + 0x2b0]
009F3C08  45 33 C0                        xor r8d, r8d
009F3C0B  48 8B CF                        mov rcx, rdi
009F3C0E  33 D2                           xor edx, edx
009F3C10  E8 1B C6 81 FF                  call 0x140210230
009F3C15  4C 8B F0                        mov r14, rax
009F3C18  33 C0                           xor eax, eax
009F3C1A  8D 48 11                        lea ecx, [rax + 0x11]
009F3C1D  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
009F3C22  74 10                           je 0x1409f3c34
009F3C24  4C 8B CF                        mov r9, rdi
009F3C27  4D 8B C6                        mov r8, r14
009F3C2A  33 D2                           xor edx, edx
009F3C2C  48 8B CF                        mov rcx, rdi
009F3C2F  E8 18 C8 81 FF                  call 0x14021044c
009F3C34  4D 85 F6                        test r14, r14
009F3C37  74 05                           je 0x1409f3c3e
009F3C39  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
009F3C3E  4C 8B 86 08 03 00 00            mov r8, qword ptr [rsi + 0x308]
009F3C45  4D 85 C0                        test r8, r8
009F3C48  74 12                           je 0x1409f3c5c
009F3C4A  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009F3C4E  48 83 C1 28                     add rcx, 0x28
009F3C52  E8 F9 C6 EC FF                  call 0x1408c0350
009F3C57  44 8B F0                        mov r14d, eax
009F3C5A  EB 06                           jmp 0x1409f3c62
009F3C5C  41 BE 22 00 00 C0               mov r14d, 0xc0000022
009F3C62  B8 11 00 00 00                  mov eax, 0x11
009F3C67  33 C9                           xor ecx, ecx
009F3C69  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
009F3C6E  74 08                           je 0x1409f3c78
009F3C70  48 8B CF                        mov rcx, rdi
009F3C73  E8 C8 F7 86 FF                  call 0x140263440
009F3C78  48 8B CF                        mov rcx, rdi
009F3C7B  E8 80 D9 8E FF                  call 0x1402e1600
009F3C80  33 FF                           xor edi, edi
009F3C82  45 85 F6                        test r14d, r14d
009F3C85  78 0D                           js 0x1409f3c94
009F3C87  41 8A CF                        mov cl, r15b
009F3C8A  8D 47 01                        lea eax, [rdi + 1]
009F3C8D  66 D3 E0                        shl ax, cl
009F3C90  66 44 03 E8                     add r13w, ax
009F3C94  33 D2                           xor edx, edx
009F3C96  48 8B CE                        mov rcx, rsi
009F3C99  E8 C2 04 01 00                  call 0x140a04160
009F3C9E  41 FE C7                        inc r15b
009F3CA1  49 83 C4 20                     add r12, 0x20
009F3CA5  41 80 FF 10                     cmp r15b, 0x10
009F3CA9  0F 82 1A FF FF FF               jb 0x1409f3bc9
009F3CAF  45 33 E4                        xor r12d, r12d
009F3CB2  66 44 89 6C 24 40               mov word ptr [rsp + 0x40], r13w
009F3CB8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009F3CBD  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009F3CC2  45 33 C9                        xor r9d, r9d
009F3CC5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F3CCA  41 B0 02                        mov r8b, 2
009F3CCD  33 D2                           xor edx, edx
009F3CCF  48 8B CB                        mov rcx, rbx
009F3CD2  41 8B F4                        mov esi, r12d
009F3CD5  E8 96 F7 EC FF                  call 0x1408c3470
009F3CDA  0F B7 44 24 40                  movzx eax, word ptr [rsp + 0x40]
009F3CDF  66 41 23 C5                     and ax, r13w
009F3CE3  66 89 43 66                     mov word ptr [rbx + 0x66], ax
009F3CE7  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F3CEC  48 8B 88 90 02 00 00            mov rcx, qword ptr [rax + 0x290]
009F3CF3  48 85 C9                        test rcx, rcx
009F3CF6  0F 84 30 01 00 00               je 0x1409f3e2c
009F3CFC  45 0F B7 EC                     movzx r13d, r12w
009F3D00  45 8A FC                        mov r15b, r12b
009F3D03  4C 8D A1 86 00 00 00            lea r12, [rcx + 0x86]
009F3D0A  33 FF                           xor edi, edi
009F3D0C  41 39 7C 24 FA                  cmp dword ptr [r12 - 6], edi
009F3D11  0F 84 CC 00 00 00               je 0x1409f3de3
009F3D17  41 0F B7 14 24                  movzx edx, word ptr [r12]
009F3D1C  45 33 C0                        xor r8d, r8d
009F3D1F  48 8B 0D 82 2D 5D 00            mov rcx, qword ptr [rip + 0x5d2d82]
009F3D26  E8 F5 EB F3 FF                  call 0x140932920
009F3D2B  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
009F3D2F  48 8B C8                        mov rcx, rax
009F3D32  48 83 C2 28                     add rdx, 0x28
009F3D36  48 8B F0                        mov rsi, rax
009F3D39  E8 1E 77 FF FF                  call 0x1409eb45c
009F3D3E  84 C0                           test al, al
009F3D40  0F 84 93 00 00 00               je 0x1409f3dd9
009F3D46  48 8D BE B0 02 00 00            lea rdi, [rsi + 0x2b0]
009F3D4D  45 33 C0                        xor r8d, r8d
009F3D50  48 8B CF                        mov rcx, rdi
009F3D53  33 D2                           xor edx, edx
009F3D55  E8 D6 C4 81 FF                  call 0x140210230
009F3D5A  4C 8B F0                        mov r14, rax
009F3D5D  33 C0                           xor eax, eax
009F3D5F  8D 48 11                        lea ecx, [rax + 0x11]
009F3D62  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
009F3D67  74 10                           je 0x1409f3d79
009F3D69  4C 8B CF                        mov r9, rdi
009F3D6C  4D 8B C6                        mov r8, r14
009F3D6F  33 D2                           xor edx, edx
009F3D71  48 8B CF                        mov rcx, rdi
009F3D74  E8 D3 C6 81 FF                  call 0x14021044c
009F3D79  4D 85 F6                        test r14, r14
009F3D7C  74 05                           je 0x1409f3d83
009F3D7E  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
009F3D83  4C 8B 86 08 03 00 00            mov r8, qword ptr [rsi + 0x308]
009F3D8A  4D 85 C0                        test r8, r8
009F3D8D  74 12                           je 0x1409f3da1
009F3D8F  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009F3D93  48 83 C1 28                     add rcx, 0x28
009F3D97  E8 B4 C5 EC FF                  call 0x1408c0350
009F3D9C  44 8B F0                        mov r14d, eax
009F3D9F  EB 06                           jmp 0x1409f3da7
009F3DA1  41 BE 22 00 00 C0               mov r14d, 0xc0000022
009F3DA7  B8 11 00 00 00                  mov eax, 0x11
009F3DAC  33 C9                           xor ecx, ecx
009F3DAE  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
009F3DB3  74 08                           je 0x1409f3dbd
009F3DB5  48 8B CF                        mov rcx, rdi
009F3DB8  E8 83 F6 86 FF                  call 0x140263440
009F3DBD  48 8B CF                        mov rcx, rdi
009F3DC0  E8 3B D8 8E FF                  call 0x1402e1600
009F3DC5  33 FF                           xor edi, edi
009F3DC7  45 85 F6                        test r14d, r14d
009F3DCA  78 0D                           js 0x1409f3dd9
009F3DCC  41 8A CF                        mov cl, r15b
009F3DCF  8D 47 01                        lea eax, [rdi + 1]
009F3DD2  66 D3 E0                        shl ax, cl
009F3DD5  66 44 03 E8                     add r13w, ax
009F3DD9  33 D2                           xor edx, edx
009F3DDB  48 8B CE                        mov rcx, rsi
009F3DDE  E8 7D 03 01 00                  call 0x140a04160
009F3DE3  41 FE C7                        inc r15b
009F3DE6  49 83 C4 20                     add r12, 0x20
009F3DEA  41 80 FF 10                     cmp r15b, 0x10
009F3DEE  0F 82 18 FF FF FF               jb 0x1409f3d0c
009F3DF4  45 33 E4                        xor r12d, r12d
009F3DF7  66 44 89 6C 24 40               mov word ptr [rsp + 0x40], r13w
009F3DFD  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009F3E02  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
009F3E07  41 B1 01                        mov r9b, 1
009F3E0A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F3E0F  41 B0 02                        mov r8b, 2
009F3E12  33 D2                           xor edx, edx
009F3E14  48 8B CB                        mov rcx, rbx
009F3E17  41 8B F4                        mov esi, r12d
009F3E1A  E8 51 F6 EC FF                  call 0x1408c3470
009F3E1F  0F B7 44 24 40                  movzx eax, word ptr [rsp + 0x40]
009F3E24  66 41 23 C5                     and ax, r13w
009F3E28  66 89 43 6A                     mov word ptr [rbx + 0x6a], ax
009F3E2C  66 44 39 63 66                  cmp word ptr [rbx + 0x66], r12w
009F3E31  75 18                           jne 0x1409f3e4b
009F3E33  66 44 39 63 6A                  cmp word ptr [rbx + 0x6a], r12w
009F3E38  0F 85 F6 00 00 00               jne 0x1409f3f34
009F3E3E  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
009F3E43  44 89 27                        mov dword ptr [rdi], r12d
009F3E46  E9 E3 FC FF FF                  jmp 0x1409f3b2e
009F3E4B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
009F3E50  41 8A FC                        mov dil, r12b
009F3E53  4D 8B FC                        mov r15, r12
009F3E56  41 BD 01 00 00 00               mov r13d, 1
009F3E5C  0F B7 43 66                     movzx eax, word ptr [rbx + 0x66]
009F3E60  40 0F B6 CF                     movzx ecx, dil
009F3E64  0F A3 C8                        bt eax, ecx
009F3E67  0F 83 B0 00 00 00               jae 0x1409f3f1d
009F3E6D  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
009F3E71  45 33 C0                        xor r8d, r8d
009F3E74  48 8B CE                        mov rcx, rsi
009F3E77  41 0F B7 94 07 86 00 00 00      movzx edx, word ptr [r15 + rax + 0x86]
009F3E80  E8 9B EA F3 FF                  call 0x140932920
009F3E85  4C 8B F0                        mov r14, rax
009F3E88  0F B7 43 62                     movzx eax, word ptr [rbx + 0x62]
009F3E8C  A8 10                           test al, 0x10
009F3E8E  75 14                           jne 0x1409f3ea4
009F3E90  66 0F BA E0 0A                  bt ax, 0xa
009F3E95  72 0D                           jb 0x1409f3ea4
009F3E97  41 F7 86 30 03 00 00 00 00 00 02  test dword ptr [r14 + 0x330], 0x2000000
009F3EA2  74 6F                           je 0x1409f3f13
009F3EA4  41 84 C5                        test r13b, al
009F3EA7  74 0F                           je 0x1409f3eb8
009F3EA9  4C 8B C3                        mov r8, rbx
009F3EAC  33 D2                           xor edx, edx
009F3EAE  49 8B CE                        mov rcx, r14
009F3EB1  E8 DE 00 01 00                  call 0x140a03f94
009F3EB6  EB 5B                           jmp 0x1409f3f13
009F3EB8  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F3EBC  48 81 C1 E8 01 00 00            add rcx, 0x1e8
009F3EC3  E8 58 27 82 FF                  call 0x140216620
009F3EC8  84 C0                           test al, al
009F3ECA  74 47                           je 0x1409f3f13
009F3ECC  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F3ED0  4C 8D 45 A8                     lea r8, [rbp - 0x58]
009F3ED4  0F 57 C0                        xorps xmm0, xmm0
009F3ED7  33 D2                           xor edx, edx
009F3ED9  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
009F3EDD  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
009F3EE1  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
009F3EE5  E8 36 29 82 FF                  call 0x140216820
009F3EEA  4C 8B C3                        mov r8, rbx
009F3EED  41 8A D5                        mov dl, r13b
009F3EF0  49 8B CE                        mov rcx, r14
009F3EF3  E8 9C 00 01 00                  call 0x140a03f94
009F3EF8  33 D2                           xor edx, edx
009F3EFA  48 8D 4D A8                     lea rcx, [rbp - 0x58]
009F3EFE  E8 2D 3E 82 FF                  call 0x140217d30
009F3F03  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F3F07  48 81 C1 E8 01 00 00            add rcx, 0x1e8
009F3F0E  E8 6D 5F 95 FF                  call 0x140349e80
009F3F13  33 D2                           xor edx, edx
009F3F15  49 8B CE                        mov rcx, r14
009F3F18  E8 43 02 01 00                  call 0x140a04160
009F3F1D  41 02 FD                        add dil, r13b
009F3F20  49 83 C7 20                     add r15, 0x20
009F3F24  40 80 FF 10                     cmp dil, 0x10
009F3F28  0F 82 2E FF FF FF               jb 0x1409f3e5c
009F3F2E  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
009F3F32  EB 06                           jmp 0x1409f3f3a
009F3F34  41 BD 01 00 00 00               mov r13d, 1
009F3F3A  66 44 39 63 6A                  cmp word ptr [rbx + 0x6a], r12w
009F3F3F  0F 84 E7 00 00 00               je 0x1409f402c
009F3F45  41 8A FC                        mov dil, r12b
009F3F48  4D 8B FC                        mov r15, r12
009F3F4B  0F B7 43 6A                     movzx eax, word ptr [rbx + 0x6a]
009F3F4F  40 0F B6 CF                     movzx ecx, dil
009F3F53  0F A3 C8                        bt eax, ecx
009F3F56  0F 83 BB 00 00 00               jae 0x1409f4017
009F3F5C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
009F3F60  45 33 C0                        xor r8d, r8d
009F3F63  48 8B 88 90 02 00 00            mov rcx, qword ptr [rax + 0x290]
009F3F6A  42 0F B7 94 39 86 00 00 00      movzx edx, word ptr [rcx + r15 + 0x86]
009F3F73  48 8B 0D 2E 2B 5D 00            mov rcx, qword ptr [rip + 0x5d2b2e]
009F3F7A  E8 A1 E9 F3 FF                  call 0x140932920
009F3F7F  4C 8B F0                        mov r14, rax
009F3F82  0F B7 43 62                     movzx eax, word ptr [rbx + 0x62]
009F3F86  A8 10                           test al, 0x10
009F3F88  75 14                           jne 0x1409f3f9e
009F3F8A  66 0F BA E0 0A                  bt ax, 0xa
009F3F8F  72 0D                           jb 0x1409f3f9e
009F3F91  41 F7 86 30 03 00 00 00 00 00 02  test dword ptr [r14 + 0x330], 0x2000000
009F3F9C  74 6F                           je 0x1409f400d
009F3F9E  41 84 C5                        test r13b, al
009F3FA1  74 0F                           je 0x1409f3fb2
009F3FA3  4C 8B C3                        mov r8, rbx
009F3FA6  33 D2                           xor edx, edx
009F3FA8  49 8B CE                        mov rcx, r14
009F3FAB  E8 E4 FF 00 00                  call 0x140a03f94
009F3FB0  EB 5B                           jmp 0x1409f400d
009F3FB2  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F3FB6  48 81 C1 E8 01 00 00            add rcx, 0x1e8
009F3FBD  E8 5E 26 82 FF                  call 0x140216620
009F3FC2  84 C0                           test al, al
009F3FC4  74 47                           je 0x1409f400d
009F3FC6  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F3FCA  4C 8D 45 D8                     lea r8, [rbp - 0x28]
009F3FCE  0F 57 C0                        xorps xmm0, xmm0
009F3FD1  33 D2                           xor edx, edx
009F3FD3  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
009F3FD7  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
009F3FDB  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
009F3FDF  E8 3C 28 82 FF                  call 0x140216820
009F3FE4  4C 8B C3                        mov r8, rbx
009F3FE7  41 8A D5                        mov dl, r13b
009F3FEA  49 8B CE                        mov rcx, r14
009F3FED  E8 A2 FF 00 00                  call 0x140a03f94
009F3FF2  33 D2                           xor edx, edx
009F3FF4  48 8D 4D D8                     lea rcx, [rbp - 0x28]
009F3FF8  E8 33 3D 82 FF                  call 0x140217d30
009F3FFD  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F4001  48 81 C1 E8 01 00 00            add rcx, 0x1e8
009F4008  E8 73 5E 95 FF                  call 0x140349e80
009F400D  33 D2                           xor edx, edx
009F400F  49 8B CE                        mov rcx, r14
009F4012  E8 49 01 01 00                  call 0x140a04160
009F4017  41 02 FD                        add dil, r13b
009F401A  49 83 C7 20                     add r15, 0x20
009F401E  40 80 FF 10                     cmp dil, 0x10
009F4022  0F 82 23 FF FF FF               jb 0x1409f3f4b
009F4028  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
009F402C  44 84 6B 62                     test byte ptr [rbx + 0x62], r13b
009F4030  0F 84 C6 00 00 00               je 0x1409f40fc
009F4036  4C 8B 73 58                     mov r14, qword ptr [rbx + 0x58]
009F403A  4D 85 F6                        test r14, r14
009F403D  0F 84 26 01 00 00               je 0x1409f4169
009F4043  0F 57 C9                        xorps xmm1, xmm1
009F4046  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
009F404B  0F 57 C0                        xorps xmm0, xmm0
009F404E  48 8B CB                        mov rcx, rbx
009F4051  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
009F4055  49 8B FC                        mov rdi, r12
009F4058  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
009F405D  0F 11 4D 88                     movups xmmword ptr [rbp - 0x78], xmm1
009F4061  E8 7A CF EC FF                  call 0x1408c0fe0
009F4066  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
009F406B  45 85 FF                        test r15d, r15d
009F406E  74 44                           je 0x1409f40b4
009F4070  41 8B D7                        mov edx, r15d
009F4073  B9 00 01 00 00                  mov ecx, 0x100
009F4078  41 B8 45 74 77 46               mov r8d, 0x46777445
009F407E  E8 6D E0 18 00                  call 0x140b820f0
009F4083  48 8B F8                        mov rdi, rax
009F4086  48 85 C0                        test rax, rax
009F4089  74 29                           je 0x1409f40b4
009F408B  44 0F B7 43 64                  movzx r8d, word ptr [rbx + 0x64]
009F4090  48 8D 45 98                     lea rax, [rbp - 0x68]
009F4094  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
009F4098  48 8B CF                        mov rcx, rdi
009F409B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009F40A0  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
009F40A4  44 89 7D A0                     mov dword ptr [rbp - 0x60], r15d
009F40A8  C7 45 A4 00 00 00 80            mov dword ptr [rbp - 0x5c], 0x80000000
009F40AF  E8 58 F7 EC FF                  call 0x1408c380c
009F40B4  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
009F40B8  41 8B D5                        mov edx, r13d
009F40BB  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009F40C0  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
009F40C4  44 8A 44 24 7C                  mov r8b, byte ptr [rsp + 0x7c]
009F40C9  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
009F40CE  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
009F40D2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009F40D7  49 8B C6                        mov rax, r14
009F40DA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009F40DF  48 8D 0D EA D1 61 FF            lea rcx, [rip - 0x9e2e16]
009F40E6  E8 E5 69 CC FF                  call 0x1406baad0
009F40EB  48 85 FF                        test rdi, rdi
009F40EE  74 79                           je 0x1409f4169
009F40F0  33 D2                           xor edx, edx
009F40F2  48 8B CF                        mov rcx, rdi
009F40F5  E8 76 E7 18 00                  call 0x140b82870
009F40FA  EB 6D                           jmp 0x1409f4169
009F40FC  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
009F4100  48 8B CB                        mov rcx, rbx
009F4103  49 8D 56 48                     lea rdx, [r14 + 0x48]
009F4107  E8 D4 CE EC FF                  call 0x1408c0fe0
009F410C  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
009F4111  C7 07 78 00 00 00               mov dword ptr [rdi], 0x78
009F4117  0F B7 53 64                     movzx edx, word ptr [rbx + 0x64]
009F411B  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009F411F  E8 E4 A1 00 00                  call 0x1409fe308
009F4124  85 C0                           test eax, eax
009F4126  74 3D                           je 0x1409f4165
009F4128  8D 88 88 00 00 00               lea ecx, [rax + 0x88]
009F412E  89 0F                           mov dword ptr [rdi], ecx
009F4130  49 8D 8E 88 00 00 00            lea rcx, [r14 + 0x88]
009F4137  41 C7 86 84 00 00 00 00 00 00 80  mov dword ptr [r14 + 0x84], 0x80000000
009F4142  41 89 86 80 00 00 00            mov dword ptr [r14 + 0x80], eax
009F4149  49 C7 46 78 88 00 00 00         mov qword ptr [r14 + 0x78], 0x88
009F4151  44 0F B7 43 64                  movzx r8d, word ptr [rbx + 0x64]
009F4156  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
009F415A  E8 AD F6 EC FF                  call 0x1408c380c
009F415F  45 89 6E 74                     mov dword ptr [r14 + 0x74], r13d
009F4163  EB 04                           jmp 0x1409f4169
009F4165  45 89 66 74                     mov dword ptr [r14 + 0x74], r12d
009F4169  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
009F416D  4C 89 A0 A0 02 00 00            mov qword ptr [rax + 0x2a0], r12
009F4174  48 8B 7B 20                     mov rdi, qword ptr [rbx + 0x20]
009F4178  48 81 C7 98 02 00 00            add rdi, 0x298
009F417F  0F 0D 0F                        prefetchw byte ptr [rdi]
009F4182  48 8B 07                        mov rax, qword ptr [rdi]
009F4185  48 8B C8                        mov rcx, rax
009F4188  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
009F418C  48 83 F9 10                     cmp rcx, 0x10
009F4190  48 8D 50 F0                     lea rdx, [rax - 0x10]
009F4194  49 0F 46 D4                     cmovbe rdx, r12
009F4198  A8 02                           test al, 2
009F419A  75 07                           jne 0x1409f41a3
009F419C  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
009F41A1  74 08                           je 0x1409f41ab
009F41A3  48 8B CF                        mov rcx, rdi
009F41A6  E8 25 F7 86 FF                  call 0x1402638d0
009F41AB  48 8B CF                        mov rcx, rdi
009F41AE  E8 4D D4 8E FF                  call 0x1402e1600
009F41B3  E8 F8 96 86 FF                  call 0x14025d8b0
009F41B8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F41BD  4C 89 A0 A0 02 00 00            mov qword ptr [rax + 0x2a0], r12
009F41C4  48 8D B8 98 02 00 00            lea rdi, [rax + 0x298]
009F41CB  0F 0D 0F                        prefetchw byte ptr [rdi]
009F41CE  48 8B 07                        mov rax, qword ptr [rdi]
009F41D1  48 8B C8                        mov rcx, rax
009F41D4  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
009F41D8  48 83 F9 10                     cmp rcx, 0x10
009F41DC  48 8D 50 F0                     lea rdx, [rax - 0x10]
009F41E0  49 0F 46 D4                     cmovbe rdx, r12
009F41E4  A8 02                           test al, 2
009F41E6  75 07                           jne 0x1409f41ef
009F41E8  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
009F41ED  74 08                           je 0x1409f41f7
009F41EF  48 8B CF                        mov rcx, rdi
009F41F2  E8 D9 F6 86 FF                  call 0x1402638d0
009F41F7  48 8B CF                        mov rcx, rdi
009F41FA  E8 01 D4 8E FF                  call 0x1402e1600
009F41FF  E8 AC 96 86 FF                  call 0x14025d8b0
009F4204  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009F4209  48 85 C9                        test rcx, rcx
009F420C  74 05                           je 0x1409f4213
009F420E  E8 0D F1 EC FF                  call 0x1408c3320
009F4213  85 F6                           test esi, esi
009F4215  78 64                           js 0x1409f427b
009F4217  48 8B 0D 22 B6 50 00            mov rcx, qword ptr [rip + 0x50b622]
009F421E  48 8D 15 FB 65 62 FF            lea rdx, [rip - 0x9d9a05]
009F4225  E8 26 E2 99 FF                  call 0x140392450
009F422A  84 C0                           test al, al
009F422C  74 4D                           je 0x1409f427b
009F422E  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
009F4232  48 8D 15 E7 65 62 FF            lea rdx, [rip - 0x9d9a19]
009F4239  48 8B 0D 00 B6 50 00            mov rcx, qword ptr [rip + 0x50b600]
009F4240  48 83 C0 28                     add rax, 0x28
009F4244  48 89 45 08                     mov qword ptr [rbp + 8], rax
009F4248  41 B9 02 00 00 00               mov r9d, 2
009F424E  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
009F4252  45 33 C0                        xor r8d, r8d
009F4255  48 83 C0 28                     add rax, 0x28
009F4259  48 C7 45 10 10 00 00 00         mov qword ptr [rbp + 0x10], 0x10
009F4261  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
009F4265  48 8D 45 08                     lea rax, [rbp + 8]
009F4269  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F426E  48 C7 45 20 10 00 00 00         mov qword ptr [rbp + 0x20], 0x10
009F4276  E8 A5 84 A2 FF                  call 0x14041c720
009F427B  8B C6                           mov eax, esi
009F427D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
009F4281  48 33 CC                        xor rcx, rsp
009F4284  E8 B7 83 CB FF                  call 0x1406ac640
009F4289  48 8B 9C 24 88 01 00 00         mov rbx, qword ptr [rsp + 0x188]
009F4291  48 81 C4 30 01 00 00            add rsp, 0x130
009F4298  41 5F                           pop r15
009F429A  41 5E                           pop r14
009F429C  41 5D                           pop r13
009F429E  41 5C                           pop r12
009F42A0  5F                              pop rdi
009F42A1  5E                              pop rsi
009F42A2  5D                              pop rbp
009F42A3  C3                              ret
009F42A4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpAddRegEntryToGroup(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int16 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mEC;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 4287817)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r12 = 0;
    a4 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 98)) >> (1));
    a4 = (unsigned __int8)((a4) & (1));
    v_stack_mD0 = a3;
    v_stack_m148 = v_stack_m118;
    v_stack_mF8 = a5;
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 648);
    result = EtwpFindOrCreateGuidEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 648), a2, v_r12 + 2, a4);
    if ((unsigned int)(result) != 0) goto loc_009F4204;
    *(unsigned int *)(a5) = 120;
    a3 = 0;
    a2 = 0;
    v_rdi = (v_stack_m118) + (664);
    result = KeAbPreAcquire(v_rdi, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_stack_m118 + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_rdi = (*(unsigned __int64 *)(a1 + 32)) + (664);
    result = KeAbPreAcquire(v_rdi, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(a1 + 40)) == 0) goto loc_009F3B36;
loc_009F3B2E:
    goto loc_009F4169;
loc_009F3B36:
    result = EtwpGetSchematizedFilterSize(*(unsigned __int64 *)(a1 + 32), *(unsigned __int16 *)(a1 + 100), a3, a4);
    v_stack_m110 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) {
        a1 = result + 16;
    }
    if (((*(unsigned __int8 *)(a1 + 98)) & (2)) == 0) goto loc_009F3B66;
    if ((*(unsigned int *)(a5)) <= ((unsigned int)((unsigned int)(a4)))) goto loc_009F3B66;
    goto loc_009F4169;
loc_009F3B66:
    result = EtwpReferenceGuidEntry(v_stack_m118, *(unsigned __int16 *)(a1 + 100), a3, a4);
    *(unsigned __int64 *)(a1 + 40) = v_stack_m118;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m118 + 56) + 8)) != (v_stack_m118 + 56)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(v_stack_m118 + 56);
    *(unsigned __int64 *)(a1 + 16 + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m118 + 56) + 8) = a1 + 16;
    *(unsigned __int64 *)(a1) = a1 + 16;
    if ((*(unsigned int *)(v_stack_m118 + 96)) != 0) goto loc_009F3BBD;
    if (*(unsigned __int64 *)(v_stack_m118 + 656) == 0) goto loc_009F3BB5;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m118 + 656) + 96)) != 0) goto loc_009F3BBD;
loc_009F3BB5:
    *(unsigned int *)(a5) = 0;
    goto loc_009F3B2E;
loc_009F3BBD:
    v_rdi = 0;
loc_009F3BC9:
    if ((*(unsigned int *)(v_stack_m118 + 134 - 6)) == 0) goto loc_009F3C9E;
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(v_stack_m108, *(unsigned __int16 *)(v_stack_m118 + 134), a3, a4);
    a2 = (*(unsigned __int64 *)(a1 + 32)) + (40);
    result = EtwpIsGuidAllowed(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009F3C94;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 688, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 688;
        a3 = 0;
        a2 = 0;
        a1 = result + 688;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(result + 776) == 0) goto loc_009F3C5C;
    a1 = (*(unsigned __int64 *)(a1 + 32)) + (40);
    result = EtwpAccessCheckFromState(a1, a2, *(unsigned __int64 *)(result + 776), a4);
    goto loc_009F3C62;
loc_009F3C5C:
loc_009F3C62:
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = result + 688;
        result = ExfReleasePushLockShared(a1, a2, *(unsigned __int64 *)(result + 776), a4);
    }
    result = KeAbPostRelease(result + 688, a2, *(unsigned __int64 *)(result + 776), a4);
    v_rdi = 0;
    v_r13 = 0;
    if (!(sign_flag)) {
        a1 = 0;
        result = v_rdi + 1;
        result = (unsigned __int16)((result) << ((unsigned __int8)(a1)));
        v_r13 = (unsigned __int16)((0) + ((unsigned __int16)(result)));
    }
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, *(unsigned __int64 *)(result + 776), a4);
loc_009F3C9E:
    v_r15 = (unsigned __int8)((0) + 1);
    v_r12 = (v_stack_m118 + 134) + (32);
    if (((unsigned __int8)(v_r15)) < 16) goto loc_009F3BC9;
    v_r12 = 0;
    v_stack_m128 = (unsigned __int16)(v_r13);
    v_stack_m120 = 0;
    a4 = 0;
    v_stack_m148 = v_stack_m128;
    a2 = 0;
    result = EtwpApplyScopeFilters(a1, a2, 2, a4);
    result = (unsigned __int16)((v_stack_m128) & ((unsigned __int16)(v_r13)));
    *(unsigned __int16 *)(a1 + 102) = (unsigned __int16)(result);
    if (*(unsigned __int64 *)(v_stack_m118 + 656) == 0) goto loc_009F3E2C;
    v_rdi = 0;
loc_009F3D0C:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m118 + 656) + 134 - 6)) == 0) goto loc_009F3DE3;
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(unsigned __int64 *)(v_rip + 6106498), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m118 + 656) + 134), a3, a4);
    a2 = (*(unsigned __int64 *)(a1 + 32)) + (40);
    result = EtwpIsGuidAllowed(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009F3DD9;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 688, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 688;
        a3 = 0;
        a2 = 0;
        a1 = result + 688;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(result + 776) == 0) goto loc_009F3DA1;
    a1 = (*(unsigned __int64 *)(a1 + 32)) + (40);
    result = EtwpAccessCheckFromState(a1, a2, *(unsigned __int64 *)(result + 776), a4);
    goto loc_009F3DA7;
loc_009F3DA1:
loc_009F3DA7:
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = result + 688;
        result = ExfReleasePushLockShared(a1, a2, *(unsigned __int64 *)(result + 776), a4);
    }
    result = KeAbPostRelease(result + 688, a2, *(unsigned __int64 *)(result + 776), a4);
    v_rdi = 0;
    v_r13 = 0;
    if (!(sign_flag)) {
        a1 = 0;
        result = v_rdi + 1;
        result = (unsigned __int16)((result) << ((unsigned __int8)(a1)));
        v_r13 = (unsigned __int16)((0) + ((unsigned __int16)(result)));
    }
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, *(unsigned __int64 *)(result + 776), a4);
loc_009F3DE3:
    v_r15 = (unsigned __int8)((0) + 1);
    v_r12 = (*(unsigned __int64 *)(v_stack_m118 + 656) + 134) + (32);
    if (((unsigned __int8)(v_r15)) < 16) goto loc_009F3D0C;
    v_r12 = 0;
    v_stack_m128 = (unsigned __int16)(v_r13);
    v_stack_m120 = 0;
    v_stack_m148 = v_stack_m128;
    a2 = 0;
    result = EtwpApplyScopeFilters(a1, a2, 2, 1);
    result = (unsigned __int16)((v_stack_m128) & ((unsigned __int16)(v_r13)));
    *(unsigned __int16 *)(a1 + 106) = (unsigned __int16)(result);
loc_009F3E2C:
    if ((*(unsigned __int16 *)(a1 + 102)) != 0) goto loc_009F3E4B;
    if ((*(unsigned __int16 *)(a1 + 106)) != 0) goto loc_009F3F34;
    *(unsigned int *)(v_stack_mF8) = 0;
    goto loc_009F3B2E;
loc_009F3E4B:
loc_009F3E5C:
    if ((*(unsigned __int16 *)(a1 + 106)) >= 0) goto loc_009F3F1D;
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(v_stack_m108, *(unsigned __int16 *)(0 + *(unsigned __int64 *)(a1 + 40) * 1 + 134), a3, 1);
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 98))) & (16)) != 0) goto loc_009F3EA4;
    if (condition_is_below) goto loc_009F3EA4;
    if (((*(unsigned int *)(result + 816)) & (0x2000000ULL)) == 0) goto loc_009F3F13;
loc_009F3EA4:
    if (((1) & ((unsigned __int8)(*(unsigned __int16 *)(a1 + 98)))) == 0) goto loc_009F3EB8;
    a2 = 0;
    result = EtwpProviderArrivalCallback(result, a2, a1, 1);
    goto loc_009F3F13;
loc_009F3EB8:
    a1 = (*(unsigned __int64 *)(a1 + 80)) + (488);
    result = ExAcquireRundownProtection(a1, a2, a1, 1);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 80);
        a3 = v_stack_mC0;
        a2 = 0;
        v_stack_mC0 = v_xmm0;
        v_stack_mB0 = v_xmm0;
        v_stack_mA0 = v_xmm0;
        result = KiStackAttachProcess(a1, a2, a3, 1);
        a3 = a1;
        a2 = 1;
        a1 = result;
        result = EtwpProviderArrivalCallback(a1, a2, a3, 1);
        a2 = 0;
        a1 = v_stack_mC0;
        result = KiUnstackDetachProcess(a1, a2, a3, 1);
        a1 = *(unsigned __int64 *)(a1 + 80);
        a1 = (a1) + (488);
        result = ExReleaseRundownProtection(a1, a2, a3, 1);
    }
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, 1);
loc_009F3F1D:
    v_rdi = (unsigned __int8)((0) + (1));
    v_r15 = (0) + (32);
    if (((unsigned __int8)(v_rdi)) < 16) goto loc_009F3E5C;
    goto loc_009F3F3A;
loc_009F3F34:
loc_009F3F3A:
    if ((*(unsigned __int16 *)(a1 + 106)) == 0) goto loc_009F402C;
loc_009F3F4B:
    if ((*(unsigned __int16 *)(a1 + 106)) >= 0) goto loc_009F4017;
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(unsigned __int64 *)(v_rip + 6105902), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 656) + 0 * 1 + 134), a3, 1);
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 98))) & (16)) != 0) goto loc_009F3F9E;
    if (condition_is_below) goto loc_009F3F9E;
    if (((*(unsigned int *)(result + 816)) & (0x2000000ULL)) == 0) goto loc_009F400D;
loc_009F3F9E:
    if (((1) & ((unsigned __int8)(*(unsigned __int16 *)(a1 + 98)))) == 0) goto loc_009F3FB2;
    a2 = 0;
    result = EtwpProviderArrivalCallback(result, a2, a1, 1);
    goto loc_009F400D;
loc_009F3FB2:
    a1 = (*(unsigned __int64 *)(a1 + 80)) + (488);
    result = ExAcquireRundownProtection(a1, a2, a1, 1);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 80);
        a3 = v_stack_m90;
        a2 = 0;
        v_stack_m90 = v_xmm0;
        v_stack_m80 = v_xmm0;
        v_stack_m70 = v_xmm0;
        result = KiStackAttachProcess(a1, a2, a3, 1);
        a3 = a1;
        a2 = 1;
        a1 = result;
        result = EtwpProviderArrivalCallback(a1, a2, a3, 1);
        a2 = 0;
        a1 = v_stack_m90;
        result = KiUnstackDetachProcess(a1, a2, a3, 1);
        a1 = *(unsigned __int64 *)(a1 + 80);
        a1 = (a1) + (488);
        result = ExReleaseRundownProtection(a1, a2, a3, 1);
    }
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, 1);
loc_009F4017:
    v_rdi = (unsigned __int8)((0) + (1));
    v_r15 = (0) + (32);
    if (((unsigned __int8)(v_rdi)) < 16) goto loc_009F3F4B;
loc_009F402C:
    if (((*(unsigned __int8 *)(a1 + 98)) & (1)) == 0) goto loc_009F40FC;
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_009F4169;
    v_stack_mD0 = v_xmm0;
    v_stack_mF0 = v_xmm1;
    v_stack_mE0 = v_xmm1;
    result = EtwpComputeRegEntryEnableInfo(a1, v_stack_mF0, a3, 1);
    if ((unsigned int)((unsigned int)(v_stack_m110)) == 0) goto loc_009F40B4;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_m110))), (unsigned int)(0x46777445ULL), 1);
    if (result != 0) {
        a3 = *(unsigned __int16 *)(a1 + 100);
        result = v_stack_mD0;
        a2 = *(unsigned __int64 *)(a1 + 32);
        a1 = result;
        v_stack_m100 = result;
        v_stack_mD0 = result;
        v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_m110));
        v_stack_mC4 = 0x80000000ULL;
        result = EtwpCopySchematizedFilters(a1, a2, a3, 1);
    }
    v_stack_m138 = *(unsigned __int64 *)(a1 + 80);
    v_stack_m140 = v_stack_m100;
    v_stack_m148 = v_stack_mD8;
    result = guard_dispatch_icall(v_rip - 10366486, 1, v_stack_mEC, v_stack_mE0);
    if (result == 0) goto loc_009F4169;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_mEC, v_stack_mE0);
    goto loc_009F4169;
loc_009F40FC:
    result = EtwpComputeRegEntryEnableInfo(a1, v_stack_mD0 + 72, v_stack_mEC, v_stack_mE0);
    *(unsigned int *)(v_stack_mF8) = 120;
    result = EtwpGetSchematizedFilterSize(*(unsigned __int64 *)(a1 + 32), *(unsigned __int16 *)(a1 + 100), v_stack_mEC, v_stack_mE0);
    if ((unsigned int)(result) == 0) goto loc_009F4165;
    *(unsigned int *)(v_stack_mF8) = (unsigned int)(result + 136);
    *(unsigned int *)(v_stack_mD0 + 132) = 0x80000000ULL;
    *(unsigned int *)(v_stack_mD0 + 128) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_mD0 + 120) = 136;
    result = EtwpCopySchematizedFilters(v_stack_mD0 + 136, *(unsigned __int64 *)(a1 + 32), *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    *(unsigned int *)(v_stack_mD0 + 116) = 1;
    goto loc_009F4169;
loc_009F4165:
    *(unsigned int *)(v_stack_mD0 + 116) = 0;
loc_009F4169:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 672) = 0;
    v_rdi = (*(unsigned __int64 *)(a1 + 32)) + (664);
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    a2 = *(unsigned __int64 *)(v_rdi) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_009F41A3;
    result = *(unsigned __int64 *)(v_rdi);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) {
        a1 = v_rdi;
        result = ExfReleasePushLock(a1, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    }
    result = KeAbPostRelease(v_rdi, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    result = KeLeaveCriticalRegion(v_rdi, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    *(unsigned __int64 *)(v_stack_m118 + 672) = 0;
    a1 = (*(unsigned __int64 *)(v_stack_m118 + 664)) & (-16);
    a2 = *(unsigned __int64 *)(v_stack_m118 + 664) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m118 + 664))) & (2)) != 0) goto loc_009F41EF;
    result = *(unsigned __int64 *)(v_stack_m118 + 664);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m118 + 664))) & (2)) != 0) {
        a1 = v_stack_m118 + 664;
        result = ExfReleasePushLock(a1, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    }
    result = KeAbPostRelease(v_stack_m118 + 664, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    result = KeLeaveCriticalRegion(v_stack_m118 + 664, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
loc_009F4204:
    if (v_stack_m118 != 0) {
        result = EtwpUnreferenceGuidEntry(v_stack_m118, a2, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    }
    if (sign_flag) goto loc_009F427B;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5289506), v_rip - 10328581, *(unsigned __int16 *)(a1 + 100), v_stack_mE0);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(a1 + 32);
        a2 = v_rip - 10328601;
        a1 = *(unsigned __int64 *)(v_rip + 5289472);
        result = (result) + (40);
        v_stack_m60 = result;
        a4 = 2;
        result = *(unsigned __int64 *)(a1 + 40);
        a3 = 0;
        result = (result) + (40);
        v_stack_m58 = 16;
        v_stack_m50 = result;
        result = v_stack_m60;
        v_stack_m148 = result;
        v_stack_m48 = 16;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (304);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpAddRegEntryToGroup(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint16_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mEC;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x416D49)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r12 = 0;
    Arg4 = (uint8_t)((*(uint8_t *)(arg1 + 0x62)) >> (1));
    Arg4 = (uint8_t)((Arg4) & (1));
    v_stack_mD0 = Arg3;
    v_stack_m148 = v_stack_m118;
    v_stack_mF8 = Arg5;
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x288);
    result = EtwpFindOrCreateGuidEntry(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x288), Arg2, local_r12 + 2, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009F4204;
    *(uint32_t *)(arg5) = 120;
    Arg3 = 0;
    Arg2 = 0;
    local_rdi = (v_stack_m118) + (664);
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    *(uint64_t *)(v_stack_m118 + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    local_rdi = (*(uint64_t *)(arg1 + 0x20)) + (664);
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(arg1 + 0x28)) == 0) goto loc_009F3B36;
loc_009F3B2E:
    goto loc_009F4169;
loc_009F3B36:
    result = EtwpGetSchematizedFilterSize(*(uint64_t *)(arg1 + 0x20), *(uint16_t *)(arg1 + 0x64), Arg3, Arg4);
    v_stack_m110 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) {
        Arg1 = result + 16;
    }
    if (((*(uint8_t *)(arg1 + 0x62)) & (2)) == 0) goto loc_009F3B66;
    if ((*(uint32_t *)(arg5)) <= ((uint32_t)((uint32_t)(Arg4)))) goto loc_009F3B66;
    goto loc_009F4169;
loc_009F3B66:
    result = EtwpReferenceGuidEntry(v_stack_m118, *(uint16_t *)(arg1 + 0x64), Arg3, Arg4);
    *(uint64_t *)(arg1 + 0x28) = v_stack_m118;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m118 + 0x38) + 0x8)) != (v_stack_m118 + 56)) {
        Arg1 = 3;
    }
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(v_stack_m118 + 0x38);
    *(void **)(arg1 + 0x10 + 0x8) = Arg1;
    *(void **)(*(uint64_t *)(v_stack_m118 + 0x38) + 0x8) = Arg1 + 16;
    *(void **)(arg1) = Arg1 + 16;
    if ((*(uint32_t *)(v_stack_m118 + 0x60)) != 0) goto loc_009F3BBD;
    if (*(uint64_t *)(v_stack_m118 + 0x290) == 0) goto loc_009F3BB5;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m118 + 0x290) + 0x60)) != 0) goto loc_009F3BBD;
loc_009F3BB5:
    *(uint32_t *)(arg5) = 0;
    goto loc_009F3B2E;
loc_009F3BBD:
    local_rdi = 0;
loc_009F3BC9:
    if ((*(uint32_t *)(v_stack_m118 + 0x86 - 0x6)) == 0) goto loc_009F3C9E;
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(v_stack_m108, *(uint16_t *)(v_stack_m118 + 0x86), Arg3, Arg4);
    Arg2 = (*(uint64_t *)(arg1 + 0x20)) + (40);
    result = EtwpIsGuidAllowed(result, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009F3C94;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 688, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = result + 688;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 688;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(result + 0x308) == 0) goto loc_009F3C5C;
    Arg1 = (*(uint64_t *)(arg1 + 0x20)) + (40);
    result = EtwpAccessCheckFromState(Arg1, Arg2, *(uint64_t *)(result + 0x308), Arg4);
    goto loc_009F3C62;
loc_009F3C5C:
loc_009F3C62:
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = result + 688;
        result = ExfReleasePushLockShared(Arg1, Arg2, *(uint64_t *)(result + 0x308), Arg4);
    }
    result = KeAbPostRelease(result + 688, Arg2, *(uint64_t *)(result + 0x308), Arg4);
    local_rdi = 0;
    local_r13 = 0;
    if (!(sign_flag)) {
        Arg1 = 0;
        result = local_rdi + 1;
        result = (uint16_t)((result) << ((uint8_t)(Arg1)));
        local_r13 = (uint16_t)((0) + ((uint16_t)(result)));
    }
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, *(uint64_t *)(result + 0x308), Arg4);
loc_009F3C9E:
    local_r15 = (uint8_t)((0) + 1);
    local_r12 = (v_stack_m118 + 134) + (32);
    if (((uint8_t)(local_r15)) < 16) goto loc_009F3BC9;
    local_r12 = 0;
    v_stack_m128 = (uint16_t)(local_r13);
    v_stack_m120 = 0;
    Arg4 = 0;
    v_stack_m148 = v_stack_m128;
    Arg2 = 0;
    result = EtwpApplyScopeFilters(Arg1, Arg2, 2, Arg4);
    result = (uint16_t)((v_stack_m128) & ((uint16_t)(local_r13)));
    *(uint16_t *)(arg1 + 0x66) = (uint16_t)(result);
    if (*(uint64_t *)(v_stack_m118 + 0x290) == 0) goto loc_009F3E2C;
    local_rdi = 0;
loc_009F3D0C:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m118 + 0x290) + 0x86 - 0x6)) == 0) goto loc_009F3DE3;
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(uint64_t *)(v_rip + 0x5D2D82), *(uint16_t *)(*(uint64_t *)(v_stack_m118 + 0x290) + 0x86), Arg3, Arg4);
    Arg2 = (*(uint64_t *)(arg1 + 0x20)) + (40);
    result = EtwpIsGuidAllowed(result, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009F3DD9;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 688, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = result + 688;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 688;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(result + 0x308) == 0) goto loc_009F3DA1;
    Arg1 = (*(uint64_t *)(arg1 + 0x20)) + (40);
    result = EtwpAccessCheckFromState(Arg1, Arg2, *(uint64_t *)(result + 0x308), Arg4);
    goto loc_009F3DA7;
loc_009F3DA1:
loc_009F3DA7:
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = result + 688;
        result = ExfReleasePushLockShared(Arg1, Arg2, *(uint64_t *)(result + 0x308), Arg4);
    }
    result = KeAbPostRelease(result + 688, Arg2, *(uint64_t *)(result + 0x308), Arg4);
    local_rdi = 0;
    local_r13 = 0;
    if (!(sign_flag)) {
        Arg1 = 0;
        result = local_rdi + 1;
        result = (uint16_t)((result) << ((uint8_t)(Arg1)));
        local_r13 = (uint16_t)((0) + ((uint16_t)(result)));
    }
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, *(uint64_t *)(result + 0x308), Arg4);
loc_009F3DE3:
    local_r15 = (uint8_t)((0) + 1);
    local_r12 = (*(uint64_t *)(v_stack_m118 + 0x290) + 134) + (32);
    if (((uint8_t)(local_r15)) < 16) goto loc_009F3D0C;
    local_r12 = 0;
    v_stack_m128 = (uint16_t)(local_r13);
    v_stack_m120 = 0;
    v_stack_m148 = v_stack_m128;
    Arg2 = 0;
    result = EtwpApplyScopeFilters(Arg1, Arg2, 2, 1);
    result = (uint16_t)((v_stack_m128) & ((uint16_t)(local_r13)));
    *(uint16_t *)(arg1 + 0x6A) = (uint16_t)(result);
loc_009F3E2C:
    if ((*(uint16_t *)(arg1 + 0x66)) != 0) goto loc_009F3E4B;
    if ((*(uint16_t *)(arg1 + 0x6A)) != 0) goto loc_009F3F34;
    *(uint32_t *)(v_stack_mF8) = 0;
    goto loc_009F3B2E;
loc_009F3E4B:
loc_009F3E5C:
    if ((*(uint16_t *)(arg1 + 0x6A)) >= 0) goto loc_009F3F1D;
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(v_stack_m108, *(uint16_t *)(0 + *(uint64_t *)(arg1 + 0x28) * 1 + 0x86), Arg3, 1);
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0x62))) & (16)) != 0) goto loc_009F3EA4;
    if (condition_is_below) goto loc_009F3EA4;
    if (((*(uint32_t *)(result + 0x330)) & (0x2000000ULL)) == 0) goto loc_009F3F13;
loc_009F3EA4:
    if (((1) & ((uint8_t)(*(uint16_t *)(arg1 + 0x62)))) == 0) goto loc_009F3EB8;
    Arg2 = 0;
    result = EtwpProviderArrivalCallback(result, Arg2, Arg1, 1);
    goto loc_009F3F13;
loc_009F3EB8:
    Arg1 = (*(uint64_t *)(arg1 + 0x50)) + (488);
    result = ExAcquireRundownProtection(Arg1, Arg2, Arg1, 1);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x50);
        Arg3 = v_stack_mC0;
        Arg2 = 0;
        v_stack_mC0 = v_xmm0;
        v_stack_mB0 = v_xmm0;
        v_stack_mA0 = v_xmm0;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, 1);
        Arg3 = Arg1;
        Arg2 = 1;
        Arg1 = result;
        result = EtwpProviderArrivalCallback(Arg1, Arg2, Arg3, 1);
        Arg2 = 0;
        Arg1 = v_stack_mC0;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, 1);
        Arg1 = *(uint64_t *)(arg1 + 0x50);
        Arg1 = (Arg1) + (488);
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, 1);
    }
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, Arg3, 1);
loc_009F3F1D:
    local_rdi = (uint8_t)((0) + (1));
    local_r15 = (0) + (32);
    if (((uint8_t)(local_rdi)) < 16) goto loc_009F3E5C;
    goto loc_009F3F3A;
loc_009F3F34:
loc_009F3F3A:
    if ((*(uint16_t *)(arg1 + 0x6A)) == 0) goto loc_009F402C;
loc_009F3F4B:
    if ((*(uint16_t *)(arg1 + 0x6A)) >= 0) goto loc_009F4017;
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(uint64_t *)(v_rip + 0x5D2B2E), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x290) + 0x0 * 1 + 0x86), Arg3, 1);
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0x62))) & (16)) != 0) goto loc_009F3F9E;
    if (condition_is_below) goto loc_009F3F9E;
    if (((*(uint32_t *)(result + 0x330)) & (0x2000000ULL)) == 0) goto loc_009F400D;
loc_009F3F9E:
    if (((1) & ((uint8_t)(*(uint16_t *)(arg1 + 0x62)))) == 0) goto loc_009F3FB2;
    Arg2 = 0;
    result = EtwpProviderArrivalCallback(result, Arg2, Arg1, 1);
    goto loc_009F400D;
loc_009F3FB2:
    Arg1 = (*(uint64_t *)(arg1 + 0x50)) + (488);
    result = ExAcquireRundownProtection(Arg1, Arg2, Arg1, 1);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x50);
        Arg3 = v_stack_m90;
        Arg2 = 0;
        v_stack_m90 = v_xmm0;
        v_stack_m80 = v_xmm0;
        v_stack_m70 = v_xmm0;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, 1);
        Arg3 = Arg1;
        Arg2 = 1;
        Arg1 = result;
        result = EtwpProviderArrivalCallback(Arg1, Arg2, Arg3, 1);
        Arg2 = 0;
        Arg1 = v_stack_m90;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, 1);
        Arg1 = *(uint64_t *)(arg1 + 0x50);
        Arg1 = (Arg1) + (488);
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, 1);
    }
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, Arg3, 1);
loc_009F4017:
    local_rdi = (uint8_t)((0) + (1));
    local_r15 = (0) + (32);
    if (((uint8_t)(local_rdi)) < 16) goto loc_009F3F4B;
loc_009F402C:
    if (((*(uint8_t *)(arg1 + 0x62)) & (1)) == 0) goto loc_009F40FC;
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_009F4169;
    v_stack_mD0 = v_xmm0;
    v_stack_mF0 = v_xmm1;
    v_stack_mE0 = v_xmm1;
    result = EtwpComputeRegEntryEnableInfo(Arg1, v_stack_mF0, Arg3, 1);
    if ((uint32_t)((uint32_t)(v_stack_m110)) == 0) goto loc_009F40B4;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_m110))), (uint32_t)(0x46777445ULL), 1);
    if (result != 0) {
        Arg3 = *(uint16_t *)(arg1 + 0x64);
        result = v_stack_mD0;
        Arg2 = *(uint64_t *)(arg1 + 0x20);
        Arg1 = result;
        v_stack_m100 = result;
        v_stack_mD0 = result;
        v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_m110));
        v_stack_mC4 = 0x80000000ULL;
        result = EtwpCopySchematizedFilters(Arg1, Arg2, Arg3, 1);
    }
    v_stack_m138 = *(uint64_t *)(arg1 + 0x50);
    v_stack_m140 = v_stack_m100;
    v_stack_m148 = v_stack_mD8;
    result = guard_dispatch_icall(v_rip - 10366486, 1, v_stack_mEC, v_stack_mE0);
    if (result == 0) goto loc_009F4169;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_mEC, v_stack_mE0);
    goto loc_009F4169;
loc_009F40FC:
    result = EtwpComputeRegEntryEnableInfo(Arg1, v_stack_mD0 + 72, v_stack_mEC, v_stack_mE0);
    *(uint32_t *)(v_stack_mF8) = 120;
    result = EtwpGetSchematizedFilterSize(*(uint64_t *)(arg1 + 0x20), *(uint16_t *)(arg1 + 0x64), v_stack_mEC, v_stack_mE0);
    if ((uint32_t)(result) == 0) goto loc_009F4165;
    *(uint32_t *)(v_stack_mF8) = (uint32_t)(result + 136);
    *(uint32_t *)(v_stack_mD0 + 0x84) = 0x80000000ULL;
    *(uint32_t *)(v_stack_mD0 + 0x80) = (uint32_t)(result);
    *(uint64_t *)(v_stack_mD0 + 0x78) = 136;
    result = EtwpCopySchematizedFilters(v_stack_mD0 + 136, *(uint64_t *)(arg1 + 0x20), *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    *(uint32_t *)(v_stack_mD0 + 0x74) = 1;
    goto loc_009F4169;
loc_009F4165:
    *(uint32_t *)(v_stack_mD0 + 0x74) = 0;
loc_009F4169:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x2A0) = 0;
    local_rdi = (*(uint64_t *)(arg1 + 0x20)) + (664);
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    Arg2 = *(uint64_t *)(local_rdi) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_009F41A3;
    result = *(uint64_t *)(local_rdi);
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) {
        Arg1 = local_rdi;
        result = ExfReleasePushLock(Arg1, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    }
    result = KeAbPostRelease(local_rdi, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    result = KeLeaveCriticalRegion(local_rdi, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    *(uint64_t *)(v_stack_m118 + 0x2A0) = 0;
    Arg1 = (*(uint64_t *)(v_stack_m118 + 0x298)) & (-16);
    Arg2 = *(uint64_t *)(v_stack_m118 + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_stack_m118 + 0x298))) & (2)) != 0) goto loc_009F41EF;
    result = *(uint64_t *)(v_stack_m118 + 0x298);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m118 + 0x298))) & (2)) != 0) {
        Arg1 = v_stack_m118 + 664;
        result = ExfReleasePushLock(Arg1, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    }
    result = KeAbPostRelease(v_stack_m118 + 664, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    result = KeLeaveCriticalRegion(v_stack_m118 + 664, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
loc_009F4204:
    if (v_stack_m118 != 0) {
        result = EtwpUnreferenceGuidEntry(v_stack_m118, Arg2, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    }
    if (sign_flag) goto loc_009F427B;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x50B622), v_rip - 10328581, *(uint16_t *)(arg1 + 0x64), v_stack_mE0);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(arg1 + 0x20);
        Arg2 = v_rip - 10328601;
        Arg1 = *(uint64_t *)(v_rip + 0x50B600);
        result = (result) + (40);
        v_stack_m60 = result;
        Arg4 = 2;
        result = *(uint64_t *)(arg1 + 0x28);
        Arg3 = 0;
        result = (result) + (40);
        v_stack_m58 = 16;
        v_stack_m50 = result;
        result = v_stack_m60;
        v_stack_m148 = result;
        v_stack_m48 = 16;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x62` | `8` | `R` |
| `Arg1` | `+ 0x62` | `16` | `R` |
| `Arg1` | `+ 0x64` | `16` | `R` |
| `Arg1` | `+ 0x66` | `16` | `R` |
| `Arg1` | `+ 0x66` | `16` | `W` |
| `Arg1` | `+ 0x6A` | `16` | `R` |
| `Arg1` | `+ 0x6A` | `16` | `W` |
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R/W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F39D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
