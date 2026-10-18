# ObSetSecurityDescriptorInfo

- RVA: `0x008BAE20`–`0x008BB4EE` (길이 `1,742` bytes)
- VA: `0x00000001408BAE20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E1C`
- 디코드: `434`개 명령, `1,742/1,742` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008BAE68` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008BAE87` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008BAEDF` → [RtlpSetSecurityObject](RtlpSetSecurityObject_function_008BB500.md) (function, `0x008BB500`)
- `0x008BAEFB` → [RtlLengthSecurityDescriptor](RtlLengthSecurityDescriptor_function_008BC870.md) (function, `0x008BC870`)
- `0x008BAF6B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008BAF8D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008BAFE3` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008BAFEB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008BAFF8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BB01F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008BB04E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008BB08E` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x008BB0C1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008BB0CB` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BB0E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BB1C0` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (function, `0x00390330`)
- `0x008BB1F0` → [PsReturnSharedPoolQuota](PsReturnSharedPoolQuota_function_008BCC30.md) (function, `0x008BCC30`)
- `0x008BB26D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008BB27B` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BB2BF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BB322` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008BB33B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008BB39D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008BB3A5` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BB3B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BB3E1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008BB3E9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008BB3F3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BB406` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008BB430` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008BB438` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BB499` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008BB4A6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008BB4BC` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008BB4D8` → [ObDereferenceSecurityDescriptor](../87/ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)

### Direct callers
- [WmipSecurityMethod](../9A/WmipSecurityMethod_function_009A71F0.md) at `0x009A72C2`

### Static image references
- `0x008BAF48` → RVA `0x00FD0EC0` (`CACHEALI`; read)
- `0x008BB17E` → RVA `0x00F0FF80` (`.data`; read)
- `0x008BB19F` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **31**
  - `0x008BAE68` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008BAE87` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008BAF6B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008BAF8D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008BAFE3` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008BAFEB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008BAFF8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BB01F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008BB04E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008BB08E` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x008BB0C1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008BB0CB` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BB0E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BB1C0` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (`PAGE` → `.text`)
  - `0x008BB26D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008BB27B` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BB2BF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BB322` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008BB33B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008BB39D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008BB3A5` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BB3B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BB3E1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008BB3E9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008BB3F3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BB406` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008BB430` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008BB438` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BB499` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008BB4A6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008BB4BC` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008BAE20  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008BAE25  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
008BAE2A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008BAE2F  57                              push rdi
008BAE30  41 54                           push r12
008BAE32  41 55                           push r13
008BAE34  41 56                           push r14
008BAE36  41 57                           push r15
008BAE38  48 81 EC 80 00 00 00            sub rsp, 0x80
008BAE3F  33 C0                           xor eax, eax
008BAE41  4D 8B F0                        mov r14, r8
008BAE44  8B F8                           mov edi, eax
008BAE46  8B D8                           mov ebx, eax
008BAE48  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008BAE51  4C 8B FA                        mov r15, rdx
008BAE54  4C 8B E1                        mov r12, rcx
008BAE57  45 33 C0                        xor r8d, r8d
008BAE5A  33 D2                           xor edx, edx
008BAE5C  48 83 C1 E0                     add rcx, -0x20
008BAE60  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008BAE67  90                              nop
008BAE68  E8 C3 53 95 FF                  call 0x140210230
008BAE6D  F0 49 0F BA 6C 24 E0 00         lock bts qword ptr [r12 - 0x20], 0
008BAE75  48 8B E8                        mov rbp, rax
008BAE78  73 12                           jae 0x1408bae8c
008BAE7A  4D 8D 44 24 E0                  lea r8, [r12 - 0x20]
008BAE7F  48 8B D0                        mov rdx, rax
008BAE82  49 8D 4C 24 E0                  lea rcx, [r12 - 0x20]
008BAE87  E8 04 4E 95 FF                  call 0x14020fc90
008BAE8C  48 85 ED                        test rbp, rbp
008BAE8F  74 04                           je 0x1408bae95
008BAE91  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
008BAE95  4D 8B 6C 24 F8                  mov r13, qword ptr [r12 - 8]
008BAE9A  49 83 E5 F0                     and r13, 0xfffffffffffffff0
008BAE9E  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
008BAEA3  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
008BAEA8  0F 84 5B 03 00 00               je 0x1408bb209
008BAEAE  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
008BAEB6  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
008BAEBB  41 8B 17                        mov edx, dword ptr [r15]
008BAEBE  33 F6                           xor esi, esi
008BAEC0  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
008BAEC5  4D 8B C6                        mov r8, r14
008BAEC8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008BAECD  49 8B CC                        mov rcx, r12
008BAED0  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
008BAED7  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008BAEDB  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008BAEDF  E8 1C 06 00 00                  call 0x1408bb500
008BAEE4  8B E8                           mov ebp, eax
008BAEE6  85 C0                           test eax, eax
008BAEE8  0F 88 22 03 00 00               js 0x1408bb210
008BAEEE  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
008BAEF3  48 8B CD                        mov rcx, rbp
008BAEF6  48 89 6C 24 60                  mov qword ptr [rsp + 0x60], rbp
008BAEFB  E8 70 19 00 00                  call 0x1408bc870
008BAF00  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
008BAF07  8B C0                           mov eax, eax
008BAF09  8B D0                           mov edx, eax
008BAF0B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008BAF10  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
008BAF14  48 03 D5                        add rdx, rbp
008BAF17  48 3B EA                        cmp rbp, rdx
008BAF1A  73 14                           jae 0x1408baf30
008BAF1C  48 8B CD                        mov rcx, rbp
008BAF1F  90                              nop
008BAF20  48 33 31                        xor rsi, qword ptr [rcx]
008BAF23  48 83 C1 10                     add rcx, 0x10
008BAF27  48 C1 C6 03                     rol rsi, 3
008BAF2B  48 3B CA                        cmp rcx, rdx
008BAF2E  72 F0                           jb 0x1408baf20
008BAF30  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008BAF39  33 C0                           xor eax, eax
008BAF3B  44 0F B6 EE                     movzx r13d, sil
008BAF3F  49 C1 E5 04                     shl r13, 4
008BAF43  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008BAF48  48 8D 05 71 5F 71 00            lea rax, [rip + 0x715f71]
008BAF4F  4C 03 E8                        add r13, rax
008BAF52  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
008BAF57  66 FF 89 E4 01 00 00            dec word ptr [rcx + 0x1e4]
008BAF5E  45 33 C0                        xor r8d, r8d
008BAF61  4D 8D 7D 08                     lea r15, [r13 + 8]
008BAF65  33 D2                           xor edx, edx
008BAF67  49 8B CD                        mov rcx, r13
008BAF6A  90                              nop
008BAF6B  E8 C0 52 95 FF                  call 0x140210230
008BAF70  48 8B E8                        mov rbp, rax
008BAF73  B9 11 00 00 00                  mov ecx, 0x11
008BAF78  33 C0                           xor eax, eax
008BAF7A  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
008BAF80  74 15                           je 0x1408baf97
008BAF82  4D 8B CD                        mov r9, r13
008BAF85  4C 8B C5                        mov r8, rbp
008BAF88  33 D2                           xor edx, edx
008BAF8A  49 8B CD                        mov rcx, r13
008BAF8D  E8 BA 54 95 FF                  call 0x14021044c
008BAF92  B9 11 00 00 00                  mov ecx, 0x11
008BAF97  48 85 ED                        test rbp, rbp
008BAF9A  74 04                           je 0x1408bafa0
008BAF9C  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
008BAFA0  4D 8B 37                        mov r14, qword ptr [r15]
008BAFA3  4D 85 F6                        test r14, r14
008BAFA6  74 1D                           je 0x1408bafc5
008BAFA8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
008BAFB0  49 39 76 10                     cmp qword ptr [r14 + 0x10], rsi
008BAFB4  0F 84 A5 00 00 00               je 0x1408bb05f
008BAFBA  0F 86 AC 00 00 00               jbe 0x1408bb06c
008BAFC0  B9 11 00 00 00                  mov ecx, 0x11
008BAFC5  48 8B 6C 24 50                  mov rbp, qword ptr [rsp + 0x50]
008BAFCA  48 85 ED                        test rbp, rbp
008BAFCD  0F 85 E9 03 00 00               jne 0x1408bb3bc
008BAFD3  48 8B C1                        mov rax, rcx
008BAFD6  33 C9                           xor ecx, ecx
008BAFD8  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
008BAFDE  74 08                           je 0x1408bafe8
008BAFE0  49 8B CD                        mov rcx, r13
008BAFE3  E8 58 84 9A FF                  call 0x140263440
008BAFE8  49 8B CD                        mov rcx, r13
008BAFEB  E8 10 66 A2 FF                  call 0x1402e1600
008BAFF0  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
008BAFF5  48 8B CD                        mov rcx, rbp
008BAFF8  E8 F3 3F 9A FF                  call 0x14025eff0
008BAFFD  44 8B B4 24 B0 00 00 00         mov r14d, dword ptr [rsp + 0xb0]
008BB005  41 8D 46 28                     lea eax, [r14 + 0x28]
008BB009  41 3B C6                        cmp eax, r14d
008BB00C  0F 82 B4 04 00 00               jb 0x1408bb4c6
008BB012  8B D0                           mov edx, eax
008BB014  B9 08 01 00 00                  mov ecx, 0x108
008BB019  41 B8 4F 62 53 63               mov r8d, 0x6353624f
008BB01F  E8 CC 70 2C 00                  call 0x140b820f0
008BB024  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008BB029  48 85 C0                        test rax, rax
008BB02C  0F 84 94 04 00 00               je 0x1408bb4c6
008BB032  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
008BB037  48 8D 48 20                     lea rcx, [rax + 0x20]
008BB03B  45 8B C6                        mov r8d, r14d
008BB03E  48 C7 40 08 10 00 00 00         mov qword ptr [rax + 8], 0x10
008BB046  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
008BB04A  44 89 70 18                     mov dword ptr [rax + 0x18], r14d
008BB04E  E8 ED B7 E0 FF                  call 0x1406c6840
008BB053  66 FF 8D E4 01 00 00            dec word ptr [rbp + 0x1e4]
008BB05A  E9 FF FE FF FF                  jmp 0x1408baf5e
008BB05F  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
008BB066  41 39 46 18                     cmp dword ptr [r14 + 0x18], eax
008BB06A  74 14                           je 0x1408bb080
008BB06C  4D 8B FE                        mov r15, r14
008BB06F  4D 8B 36                        mov r14, qword ptr [r14]
008BB072  4D 85 F6                        test r14, r14
008BB075  0F 84 45 FF FF FF               je 0x1408bafc0
008BB07B  E9 30 FF FF FF                  jmp 0x1408bafb0
008BB080  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
008BB085  49 8D 56 20                     lea rdx, [r14 + 0x20]
008BB089  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008BB08E  E8 7D BA E0 FF                  call 0x1406c6b10
008BB093  85 C0                           test eax, eax
008BB095  75 D5                           jne 0x1408bb06c
008BB097  B9 10 00 00 00                  mov ecx, 0x10
008BB09C  F0 49 0F C1 4E 08               lock xadd qword ptr [r14 + 8], rcx
008BB0A2  48 85 C9                        test rcx, rcx
008BB0A5  0F 8E 97 03 00 00               jle 0x1408bb442
008BB0AB  B8 11 00 00 00                  mov eax, 0x11
008BB0B0  33 C9                           xor ecx, ecx
008BB0B2  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
008BB0B8  0F 85 D8 03 00 00               jne 0x1408bb496
008BB0BE  49 8B CD                        mov rcx, r13
008BB0C1  E8 3A 65 A2 FF                  call 0x1402e1600
008BB0C6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008BB0CB  E8 20 3F 9A FF                  call 0x14025eff0
008BB0D0  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008BB0D5  49 8D 5E 20                     lea rbx, [r14 + 0x20]
008BB0D9  48 85 C0                        test rax, rax
008BB0DC  74 0D                           je 0x1408bb0eb
008BB0DE  BA 4F 62 53 63                  mov edx, 0x6353624f
008BB0E3  48 8B C8                        mov rcx, rax
008BB0E6  E8 85 77 2C 00                  call 0x140b82870
008BB0EB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
008BB0F0  45 33 ED                        xor r13d, r13d
008BB0F3  41 8B ED                        mov ebp, r13d
008BB0F6  80 38 01                        cmp byte ptr [rax], 1
008BB0F9  0F 85 74 03 00 00               jne 0x1408bb473
008BB0FF  0F B7 50 02                     movzx edx, word ptr [rax + 2]
008BB103  66 85 D2                        test dx, dx
008BB106  0F 89 79 03 00 00               jns 0x1408bb485
008BB10C  8B 48 08                        mov ecx, dword ptr [rax + 8]
008BB10F  85 C9                           test ecx, ecx
008BB111  0F 84 37 03 00 00               je 0x1408bb44e
008BB117  48 03 C8                        add rcx, rax
008BB11A  F6 C2 04                        test dl, 4
008BB11D  0F 84 48 03 00 00               je 0x1408bb46b
008BB123  66 85 D2                        test dx, dx
008BB126  0F 89 84 03 00 00               jns 0x1408bb4b0
008BB12C  8B 50 10                        mov edx, dword ptr [rax + 0x10]
008BB12F  85 D2                           test edx, edx
008BB131  0F 84 57 03 00 00               je 0x1408bb48e
008BB137  48 03 D0                        add rdx, rax
008BB13A  48 85 C9                        test rcx, rcx
008BB13D  74 0E                           je 0x1408bb14d
008BB13F  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
008BB143  8D 2C 85 0B 00 00 00            lea ebp, [rax*4 + 0xb]
008BB14A  83 E5 FC                        and ebp, 0xfffffffc
008BB14D  48 85 D2                        test rdx, rdx
008BB150  74 0C                           je 0x1408bb15e
008BB152  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008BB156  83 C0 03                        add eax, 3
008BB159  83 E0 FC                        and eax, 0xfffffffc
008BB15C  03 E8                           add ebp, eax
008BB15E  49 83 7C 24 F0 01               cmp qword ptr [r12 - 0x10], 1
008BB164  49 8D 74 24 D0                  lea rsi, [r12 - 0x30]
008BB169  0F 84 8D 00 00 00               je 0x1408bb1fc
008BB16F  0F B6 46 1A                     movzx eax, byte ptr [rsi + 0x1a]
008BB173  A8 08                           test al, 8
008BB175  0F 84 02 03 00 00               je 0x1408bb47d
008BB17B  83 E0 0F                        and eax, 0xf
008BB17E  48 8D 0D FB 4D 65 00            lea rcx, [rip + 0x654dfb]
008BB185  0F B6 04 08                     movzx eax, byte ptr [rax + rcx]
008BB189  48 2B F0                        sub rsi, rax
008BB18C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008BB195  44 8B CD                        mov r9d, ebp
008BB198  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008BB19F  48 3B 0D 0A B9 70 00            cmp rcx, qword ptr [rip + 0x70b90a]
008BB1A6  0F 84 B4 02 00 00               je 0x1408bb460
008BB1AC  4C 8B B1 F8 02 00 00            mov r14, qword ptr [rcx + 0x2f8]
008BB1B3  85 ED                           test ebp, ebp
008BB1B5  74 16                           je 0x1408bb1cd
008BB1B7  33 D2                           xor edx, edx
008BB1B9  49 8B CE                        mov rcx, r14
008BB1BC  44 8D 42 01                     lea r8d, [rdx + 1]
008BB1C0  E8 6B 51 AD FF                  call 0x140390330
008BB1C5  85 C0                           test eax, eax
008BB1C7  0F 88 89 02 00 00               js 0x1408bb456
008BB1CD  F0 41 FF 86 00 02 00 00         lock inc dword ptr [r14 + 0x200]
008BB1D5  4D 8B FE                        mov r15, r14
008BB1D8  4D 85 F6                        test r14, r14
008BB1DB  0F 84 75 02 00 00               je 0x1408bb456
008BB1E1  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
008BB1E5  48 85 C9                        test rcx, rcx
008BB1E8  74 0B                           je 0x1408bb1f5
008BB1EA  8B 56 08                        mov edx, dword ptr [rsi + 8]
008BB1ED  45 33 C0                        xor r8d, r8d
008BB1F0  E8 3B 1A 00 00                  call 0x1408bcc30
008BB1F5  89 6E 08                        mov dword ptr [rsi + 8], ebp
008BB1F8  4C 89 7E 10                     mov qword ptr [rsi + 0x10], r15
008BB1FC  41 8B ED                        mov ebp, r13d
008BB1FF  48 85 DB                        test rbx, rbx
008BB202  75 13                           jne 0x1408bb217
008BB204  49 8B DD                        mov rbx, r13
008BB207  EB 12                           jmp 0x1408bb21b
008BB209  BD D7 00 00 C0                  mov ebp, 0xc00000d7
008BB20E  33 F6                           xor esi, esi
008BB210  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008BB215  EB 19                           jmp 0x1408bb230
008BB217  48 83 CB 0F                     or rbx, 0xf
008BB21B  49 87 5C 24 F8                  xchg qword ptr [r12 - 8], rbx
008BB220  48 8B FB                        mov rdi, rbx
008BB223  49 8B DD                        mov rbx, r13
008BB226  83 E7 0F                        and edi, 0xf
008BB229  FF C7                           inc edi
008BB22B  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
008BB230  41 0F 0D 4C 24 E0               prefetchw byte ptr [r12 - 0x20]
008BB236  49 8B 44 24 E0                  mov rax, qword ptr [r12 - 0x20]
008BB23B  48 8B C8                        mov rcx, rax
008BB23E  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008BB242  48 83 F9 10                     cmp rcx, 0x10
008BB246  B9 00 00 00 00                  mov ecx, 0
008BB24B  48 8D 50 F0                     lea rdx, [rax - 0x10]
008BB24F  48 0F 46 D1                     cmovbe rdx, rcx
008BB253  A8 02                           test al, 2
008BB255  0F 85 A6 01 00 00               jne 0x1408bb401
008BB25B  F0 49 0F B1 54 24 E0            lock cmpxchg qword ptr [r12 - 0x20], rdx
008BB262  0F 85 99 01 00 00               jne 0x1408bb401
008BB268  49 8D 4C 24 E0                  lea rcx, [r12 - 0x20]
008BB26D  E8 8E 63 A2 FF                  call 0x1402e1600
008BB272  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008BB27B  E8 70 3D 9A FF                  call 0x14025eff0
008BB280  48 85 DB                        test rbx, rbx
008BB283  0F 85 47 02 00 00               jne 0x1408bb4d0
008BB289  4D 85 ED                        test r13, r13
008BB28C  74 25                           je 0x1408bb2b3
008BB28E  85 FF                           test edi, edi
008BB290  74 21                           je 0x1408bb2b3
008BB292  49 8D 5D E0                     lea rbx, [r13 - 0x20]
008BB296  0F 0D 4B 08                     prefetchw byte ptr [rbx + 8]
008BB29A  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008BB29E  8B D7                           mov edx, edi
008BB2A0  48 8B C8                        mov rcx, rax
008BB2A3  48 2B CA                        sub rcx, rdx
008BB2A6  48 85 C9                        test rcx, rcx
008BB2A9  7E 3D                           jle 0x1408bb2e8
008BB2AB  F0 48 0F B1 4B 08               lock cmpxchg qword ptr [rbx + 8], rcx
008BB2B1  75 ED                           jne 0x1408bb2a0
008BB2B3  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008BB2B8  48 85 C9                        test rcx, rcx
008BB2BB  74 07                           je 0x1408bb2c4
008BB2BD  33 D2                           xor edx, edx
008BB2BF  E8 AC 75 2C 00                  call 0x140b82870
008BB2C4  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
008BB2CC  8B C5                           mov eax, ebp
008BB2CE  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
008BB2D2  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
008BB2D6  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
008BB2DA  49 8B E3                        mov rsp, r11
008BB2DD  41 5F                           pop r15
008BB2DF  41 5E                           pop r14
008BB2E1  41 5D                           pop r13
008BB2E3  41 5C                           pop r12
008BB2E5  5F                              pop rdi
008BB2E6  C3                              ret
008BB2E7  CC                              int3
008BB2E8  0F 85 F4 01 00 00               jne 0x1408bb4e2
008BB2EE  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
008BB2F1  45 33 C0                        xor r8d, r8d
008BB2F4  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
008BB2FD  33 D2                           xor edx, edx
008BB2FF  44 0F B6 F0                     movzx r14d, al
008BB303  48 8D 05 B6 5B 71 00            lea rax, [rip + 0x715bb6]
008BB30A  49 C1 E6 04                     shl r14, 4
008BB30E  4C 03 F0                        add r14, rax
008BB311  66 41 FF 8C 24 E4 01 00 00      dec word ptr [r12 + 0x1e4]
008BB31A  49 8B CE                        mov rcx, r14
008BB31D  90                              nop
008BB31E  49 8D 76 08                     lea rsi, [r14 + 8]
008BB322  E8 09 4F 95 FF                  call 0x140210230
008BB327  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
008BB32D  4C 8B F8                        mov r15, rax
008BB330  73 0E                           jae 0x1408bb340
008BB332  4D 8B C6                        mov r8, r14
008BB335  48 8B D0                        mov rdx, rax
008BB338  49 8B CE                        mov rcx, r14
008BB33B  E8 50 49 95 FF                  call 0x14020fc90
008BB340  4D 85 FF                        test r15, r15
008BB343  74 05                           je 0x1408bb34a
008BB345  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008BB34A  8B C7                           mov eax, edi
008BB34C  F7 D8                           neg eax
008BB34E  48 63 C8                        movsxd rcx, eax
008BB351  F0 48 0F C1 4B 08               lock xadd qword ptr [rbx + 8], rcx
008BB357  8B C7                           mov eax, edi
008BB359  48 2B C8                        sub rcx, rax
008BB35C  48 85 C9                        test rcx, rcx
008BB35F  0F 8F B2 00 00 00               jg 0x1408bb417
008BB365  0F 85 A5 00 00 00               jne 0x1408bb410
008BB36B  48 8B 06                        mov rax, qword ptr [rsi]
008BB36E  48 3B C3                        cmp rax, rbx
008BB371  74 0B                           je 0x1408bb37e
008BB373  48 8B F0                        mov rsi, rax
008BB376  48 8B 00                        mov rax, qword ptr [rax]
008BB379  48 3B C3                        cmp rax, rbx
008BB37C  75 F5                           jne 0x1408bb373
008BB37E  48 8B 03                        mov rax, qword ptr [rbx]
008BB381  48 89 06                        mov qword ptr [rsi], rax
008BB384  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008BB38B  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
008BB390  24 06                           and al, 6
008BB392  3C 02                           cmp al, 2
008BB394  0F 84 09 01 00 00               je 0x1408bb4a3
008BB39A  49 8B CE                        mov rcx, r14
008BB39D  E8 5E 62 A2 FF                  call 0x1402e1600
008BB3A2  49 8B CC                        mov rcx, r12
008BB3A5  E8 46 3C 9A FF                  call 0x14025eff0
008BB3AA  BA 4F 62 53 63                  mov edx, 0x6353624f
008BB3AF  48 8B CB                        mov rcx, rbx
008BB3B2  E8 B9 74 2C 00                  call 0x140b82870
008BB3B7  E9 F7 FE FF FF                  jmp 0x1408bb2b3
008BB3BC  4C 89 75 00                     mov qword ptr [rbp], r14
008BB3C0  49 8B C6                        mov rax, r14
008BB3C3  F0 49 0F B1 2F                  lock cmpxchg qword ptr [r15], rbp
008BB3C8  4C 8B F8                        mov r15, rax
008BB3CB  0F 85 CF FB FF FF               jne 0x1408bafa0
008BB3D1  48 8B C1                        mov rax, rcx
008BB3D4  33 C9                           xor ecx, ecx
008BB3D6  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
008BB3DC  74 08                           je 0x1408bb3e6
008BB3DE  49 8B CD                        mov rcx, r13
008BB3E1  E8 5A 80 9A FF                  call 0x140263440
008BB3E6  49 8B CD                        mov rcx, r13
008BB3E9  E8 12 62 A2 FF                  call 0x1402e1600
008BB3EE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008BB3F3  E8 F8 3B 9A FF                  call 0x14025eff0
008BB3F8  48 8D 5D 20                     lea rbx, [rbp + 0x20]
008BB3FC  E9 EA FC FF FF                  jmp 0x1408bb0eb
008BB401  49 8D 4C 24 E0                  lea rcx, [r12 - 0x20]
008BB406  E8 C5 84 9A FF                  call 0x1402638d0
008BB40B  E9 58 FE FF FF                  jmp 0x1408bb268
008BB410  B9 0E 00 00 00                  mov ecx, 0xe
008BB415  CD 29                           int 0x29
008BB417  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008BB41E  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
008BB423  24 06                           and al, 6
008BB425  3C 02                           cmp al, 2
008BB427  0F 84 8C 00 00 00               je 0x1408bb4b9
008BB42D  49 8B CE                        mov rcx, r14
008BB430  E8 CB 61 A2 FF                  call 0x1402e1600
008BB435  49 8B CC                        mov rcx, r12
008BB438  E8 B3 3B 9A FF                  call 0x14025eff0
008BB43D  E9 71 FE FF FF                  jmp 0x1408bb2b3
008BB442  B9 0E 00 00 00                  mov ecx, 0xe
008BB447  CD 29                           int 0x29
008BB449  E9 5D FC FF FF                  jmp 0x1408bb0ab
008BB44E  49 8B CD                        mov rcx, r13
008BB451  E9 C4 FC FF FF                  jmp 0x1408bb11a
008BB456  BD 44 00 00 C0                  mov ebp, 0xc0000044
008BB45B  E9 CB FD FF FF                  jmp 0x1408bb22b
008BB460  41 BF 01 00 00 00               mov r15d, 1
008BB466  E9 76 FD FF FF                  jmp 0x1408bb1e1
008BB46B  49 8B D5                        mov rdx, r13
008BB46E  E9 C7 FC FF FF                  jmp 0x1408bb13a
008BB473  BD 58 00 00 C0                  mov ebp, 0xc0000058
008BB478  E9 AE FD FF FF                  jmp 0x1408bb22b
008BB47D  49 8B F5                        mov rsi, r13
008BB480  E9 07 FD FF FF                  jmp 0x1408bb18c
008BB485  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
008BB489  E9 8C FC FF FF                  jmp 0x1408bb11a
008BB48E  49 8B D5                        mov rdx, r13
008BB491  E9 A4 FC FF FF                  jmp 0x1408bb13a
008BB496  49 8B CD                        mov rcx, r13
008BB499  E8 A2 7F 9A FF                  call 0x140263440
008BB49E  E9 1B FC FF FF                  jmp 0x1408bb0be
008BB4A3  49 8B CE                        mov rcx, r14
008BB4A6  E8 25 A9 9A FF                  call 0x140265dd0
008BB4AB  E9 EA FE FF FF                  jmp 0x1408bb39a
008BB4B0  48 8B 50 20                     mov rdx, qword ptr [rax + 0x20]
008BB4B4  E9 81 FC FF FF                  jmp 0x1408bb13a
008BB4B9  49 8B CE                        mov rcx, r14
008BB4BC  E8 0F A9 9A FF                  call 0x140265dd0
008BB4C1  E9 67 FF FF FF                  jmp 0x1408bb42d
008BB4C6  BD 9A 00 00 C0                  mov ebp, 0xc000009a
008BB4CB  E9 5B FD FF FF                  jmp 0x1408bb22b
008BB4D0  BA 10 00 00 00                  mov edx, 0x10
008BB4D5  48 8B CB                        mov rcx, rbx
008BB4D8  E8 C3 8B FB FF                  call 0x1408740a0
008BB4DD  E9 A7 FD FF FF                  jmp 0x1408bb289
008BB4E2  B9 0E 00 00 00                  mov ecx, 0xe
008BB4E7  CD 29                           int 0x29
008BB4E9  E9 00 FE FF FF                  jmp 0x1408bb2ee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObSetSecurityDescriptorInfo(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (128);
    result = 0;
    a3 = 0;
    a2 = 0;
    a1 = (a1) + (-32);
    result = KeAbPreAcquire(a1, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 - 32;
        a2 = result;
        a1 = a1 - 32;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r13 = (*(unsigned __int64 *)(a1 - 8)) & (-16);
    v_stack_m60 = v_r13;
    v_stack_m68 = v_r13;
    if (condition_is_equal) goto loc_008BB209;
    v_rsi = 0;
    v_stack_m70 = 0;
    v_stack_m78 = a6;
    v_stack_m80 = (unsigned int)((unsigned int)(a5));
    v_stack_m88 = 0;
    result = RtlpSetSecurityObject(a1, (unsigned int)(*(unsigned int *)(a2)), a3, v_stack_m68);
    if (sign_flag) goto loc_008BB210;
    v_stack_m48 = v_stack_m68;
    result = RtlLengthSecurityDescriptor(v_stack_m68, (unsigned int)(*(unsigned int *)(a2)), a3, v_stack_m68);
    v_stack_p8 = (unsigned int)(result);
    v_stack_m40 = (unsigned int)((unsigned int)(result));
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (-8);
    a2 = (a2) + (v_stack_m68);
    if (v_stack_m68 >= a2) goto loc_008BAF30;
loc_008BAF20:
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(v_stack_m68));
    a1 = (v_stack_m68) + (16);
    if (a1 < a2) goto loc_008BAF20;
loc_008BAF30:
    result = 0;
    v_r13 = ((unsigned __int8)(v_rsi)) << (4);
    v_stack_m58 = 0;
    v_r13 = (v_r13) + (v_rip + 7430001);
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_008BAF5E:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r13, a2, a3, v_stack_m68);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_r13;
        a3 = 0;
        a2 = 0;
        a1 = v_r13;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_r13 + 8) == 0) goto loc_008BAFC5;
loc_008BAFB0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 8) + 16)) == v_rsi) goto loc_008BB05F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 8) + 16)) <= v_rsi) goto loc_008BB06C;
loc_008BAFC0:
loc_008BAFC5:
    if (v_stack_m58 != 0) goto loc_008BB3BC;
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_r13;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_r13, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(v_stack_m50, a2, a3, a4);
    if (((unsigned int)((unsigned int)(v_stack_p8) + 40)) < ((unsigned int)((unsigned int)(v_stack_p8)))) goto loc_008BB4C6;
    result = ExAllocatePool2(264, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8) + 40)), (unsigned int)(0x6353624FULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_008BB4C6;
    *(unsigned __int64 *)(result + 8) = 16;
    *(unsigned __int64 *)(result + 16) = v_rsi;
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(v_stack_p8));
    result = memcpy(result + 32, v_stack_m48, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), a4);
    goto loc_008BAF5E;
loc_008BB05F:
    if ((*(unsigned int *)((unsigned int)(v_stack_p8) + 24)) == ((unsigned int)((unsigned int)(v_stack_p8)))) goto loc_008BB080;
loc_008BB06C:
    if (*(unsigned __int64 *)((unsigned int)(v_stack_p8)) == 0) goto loc_008BAFC0;
    goto loc_008BAFB0;
loc_008BB080:
    result = memcmp(v_stack_m48, *(unsigned __int64 *)((unsigned int)(v_stack_p8)) + 32, v_stack_m40, a4);
    if ((unsigned int)(result) != 0) goto loc_008BB06C;
    if (condition_is_less_or_equal) goto loc_008BB442;
loc_008BB0AB:
    a1 = 0;
    if (condition_is_not_equal) goto loc_008BB496;
loc_008BB0BE:
    result = KeAbPostRelease(v_r13, *(unsigned __int64 *)((unsigned int)(v_stack_p8)) + 32, v_stack_m40, a4);
    result = KeLeaveCriticalRegionThread(v_stack_m50, *(unsigned __int64 *)((unsigned int)(v_stack_p8)) + 32, v_stack_m40, a4);
    result = v_stack_m58;
    if (v_stack_m58 != 0) {
        a2 = 0x6353624FULL;
        a1 = v_stack_m58;
        result = ExFreePoolWithTag(a1, a2, v_stack_m40, a4);
    }
    v_r13 = 0;
    if ((*(unsigned __int8 *)(v_stack_m68)) != 1) goto loc_008BB473;
    if (!sign_flag) goto loc_008BB485;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + 8))) == 0) goto loc_008BB44E;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m68 + 8))) + (v_stack_m68);
loc_008BB11A:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m68 + 2))) & (4)) == 0) goto loc_008BB46B;
    if (!sign_flag) goto loc_008BB4B0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + 16))) == 0) goto loc_008BB48E;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_m68 + 16))) + (v_stack_m68);
loc_008BB13A:
    result = v_stack_m68;
    v_rbp = 0;
    if (a1 != 0) {
        result = *(unsigned __int8 *)(a1 + 1);
        v_rbp = result * 4 + 11;
        v_rbp = (unsigned int)((v_rbp) & (0xFFFFFFFCULL));
    }
    if (a2 != 0) {
        result = *(unsigned __int16 *)(a2 + 2);
        result = (unsigned int)((result) + (3));
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(result)));
    }
    if ((*(unsigned __int64 *)(a1 - 16)) == 1) goto loc_008BB1FC;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 - 48 + 26))) & (8)) == 0) goto loc_008BB47D;
    result = (unsigned int)((*(unsigned __int8 *)(a1 - 48 + 26)) & (15));
    v_rsi = (a1 - 48) - (*(unsigned __int8 *)(result + v_rip + 6639099 * 1));
loc_008BB18C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == (*(unsigned __int64 *)(v_rip + 7387402))) goto loc_008BB460;
    if ((unsigned int)(v_rbp) == 0) goto loc_008BB1CD;
    a2 = 0;
    result = PspChargeQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 760), a2, a2 + 1, (unsigned int)((unsigned int)(v_rbp)));
    if (sign_flag) goto loc_008BB456;
loc_008BB1CD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 760) == 0) goto loc_008BB456;
loc_008BB1E1:
    if (*(unsigned __int64 *)(v_rsi + 16) != 0) {
        a2 = *(unsigned int *)(v_rsi + 8);
        a3 = 0;
        result = PsReturnSharedPoolQuota(*(unsigned __int64 *)(v_rsi + 16), a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    }
    *(unsigned int *)(v_rsi + 8) = (unsigned int)(v_rbp);
    *(unsigned __int64 *)(v_rsi + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 760);
loc_008BB1FC:
    if (*(unsigned __int64 *)((unsigned int)(v_stack_p8)) + 32 != 0) goto loc_008BB217;
    goto loc_008BB21B;
loc_008BB209:
    v_rsi = 0;
loc_008BB210:
    v_stack_m68 = 0;
    goto loc_008BB230;
loc_008BB217:
    v_rbx = (0) | (15);
loc_008BB21B:
    v_rdi = (unsigned int)((v_rbx) & (15));
    v_rdi = (unsigned int)((v_rdi) + 1);
loc_008BB22B:
loc_008BB230:
    a1 = (*(unsigned __int64 *)(a1 - 32)) & (-16);
    a2 = *(unsigned __int64 *)(a1 - 32) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 32))) & (2)) != 0) goto loc_008BB401;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 32))) & (2)) != 0) goto loc_008BB401;
loc_008BB268:
    result = KeAbPostRelease(a1 - 32, a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    if (0 != 0) goto loc_008BB4D0;
loc_008BB289:
    if (v_stack_m60 == 0) goto loc_008BB2B3;
    if ((unsigned int)(v_rdi) == 0) goto loc_008BB2B3;
loc_008BB2A0:
    a1 = (*(unsigned __int64 *)(v_stack_m60 - 32 + 8)) - ((unsigned int)((unsigned int)(v_rdi)));
    if (condition_is_less_or_equal) goto loc_008BB2E8;
    if (a1 != 0) goto loc_008BB2A0;
loc_008BB2B3:
    result = *(unsigned __int64 *)(v_stack_m60 - 32 + 8);
    if (v_stack_m68 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m68, a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    }
    return (unsigned int)((unsigned int)((unsigned int)(0xC00000D7ULL)));
loc_008BB2E8:
    if (condition_is_not_equal) goto loc_008BB4E2;
loc_008BB2EE:
    a3 = 0;
    a2 = 0;
    v_r14 = ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)))) << (4);
    v_r14 = (v_r14) + (v_rip + 7429046);
    result = KeAbPreAcquire(v_r14, a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_r14;
        a2 = result;
        a1 = v_r14;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_rdi))));
    a1 = ((int)((unsigned int)(result))) - ((unsigned int)((unsigned int)(v_rdi)));
    if (condition_is_greater) goto loc_008BB417;
    if (a1 != 0) goto loc_008BB410;
    if ((*(unsigned __int64 *)(v_r14 + 8)) == (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_008BB37E;
loc_008BB373:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8))) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_008BB373;
loc_008BB37E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56));
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008BB4A3;
loc_008BB39A:
    result = KeAbPostRelease(v_r14, a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, (unsigned int)((unsigned int)(v_rbp)));
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 56), (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB2B3;
loc_008BB3BC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)) = v_r14;
    if (((unsigned __int8)(result)) != 2) goto loc_008BAFA0;
    a1 = 0;
    result = *(unsigned __int64 *)(v_stack_m28 + 56);
    if (!(condition_is_equal)) {
        a1 = v_stack_m60;
        result = ExfReleasePushLockShared(a1, (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    }
    result = KeAbPostRelease(v_stack_m60, (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    result = KeLeaveCriticalRegionThread(v_stack_m28, (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB0EB;
loc_008BB401:
    result = ExfReleasePushLock(*(unsigned __int64 *)(gs_base + (0 + 392)) - 32, (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB268;
loc_008BB410:
loc_008BB417:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008BB4B9;
loc_008BB42D:
    result = KeAbPostRelease(v_r14, (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x6353624FULL), a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB2B3;
loc_008BB442:
    goto loc_008BB0AB;
loc_008BB44E:
    goto loc_008BB11A;
loc_008BB456:
    goto loc_008BB22B;
loc_008BB460:
    goto loc_008BB1E1;
loc_008BB46B:
    goto loc_008BB13A;
loc_008BB473:
    goto loc_008BB22B;
loc_008BB47D:
    goto loc_008BB18C;
loc_008BB485:
    goto loc_008BB11A;
loc_008BB48E:
    goto loc_008BB13A;
loc_008BB496:
    result = ExfReleasePushLockShared(v_stack_m60, v_stack_m60, a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB0BE;
loc_008BB4A3:
    result = ExfTryToWakePushLock(v_r14, v_stack_m60, a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB39A;
loc_008BB4B0:
    goto loc_008BB13A;
loc_008BB4B9:
    result = ExfTryToWakePushLock(v_r14, *(unsigned __int64 *)(result + 32), a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB42D;
loc_008BB4C6:
    goto loc_008BB22B;
loc_008BB4D0:
    result = ObDereferenceSecurityDescriptor(*(unsigned __int64 *)(v_stack_m28 + 64) + 32, 16, a3, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BB289;
loc_008BB4E2:
    goto loc_008BB2EE;
}
```

## 5. (Beta) C Style

```c
int64_t ObSetSecurityDescriptorInfo(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (128);
    result = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (Arg1) + (-32);
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 - 32;
        Arg2 = result;
        Arg1 = Arg1 - 32;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r13 = (*(uint64_t *)(arg1 - 0x8)) & (-16);
    v_stack_m60 = local_r13;
    v_stack_m68 = local_r13;
    if (condition_is_equal) goto loc_008BB209;
    local_rsi = 0;
    v_stack_m70 = 0;
    v_stack_m78 = Arg6;
    v_stack_m80 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m88 = 0;
    result = RtlpSetSecurityObject(Arg1, (uint32_t)(*(uint32_t *)(arg2)), Arg3, v_stack_m68);
    if (sign_flag) goto loc_008BB210;
    v_stack_m48 = v_stack_m68;
    result = RtlLengthSecurityDescriptor(v_stack_m68, (uint32_t)(*(uint32_t *)(arg2)), Arg3, v_stack_m68);
    v_stack_p8 = (uint32_t)(result);
    v_stack_m40 = (uint32_t)((uint32_t)(result));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (-8);
    Arg2 = (Arg2) + (v_stack_m68);
    if (v_stack_m68 >= Arg2) goto loc_008BAF30;
loc_008BAF20:
    local_rsi = (local_rsi) ^ (*(uint64_t *)(v_stack_m68));
    Arg1 = (v_stack_m68) + (16);
    if (Arg1 < Arg2) goto loc_008BAF20;
loc_008BAF30:
    result = 0;
    local_r13 = ((uint8_t)(local_rsi)) << (4);
    v_stack_m58 = 0;
    local_r13 = (local_r13) + (v_rip + 7430001);
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x188));
loc_008BAF5E:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r13, Arg2, Arg3, v_stack_m68);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_r13;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_r13;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(local_r13 + 0x8) == 0) goto loc_008BAFC5;
loc_008BAFB0:
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x8) + 0x10)) == local_rsi) goto loc_008BB05F;
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x8) + 0x10)) <= local_rsi) goto loc_008BB06C;
loc_008BAFC0:
loc_008BAFC5:
    if (v_stack_m58 != 0) goto loc_008BB3BC;
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = local_r13;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(local_r13, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(v_stack_m50, Arg2, Arg3, Arg4);
    if (((uint32_t)((uint32_t)(v_stack_p8) + 40)) < ((uint32_t)((uint32_t)(v_stack_p8)))) goto loc_008BB4C6;
    result = ExAllocatePool2(264, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8) + 40)), (uint32_t)(0x6353624FULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_008BB4C6;
    *(uint64_t *)(result + 0x8) = 16;
    *(uint64_t *)(result + 0x10) = local_rsi;
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(v_stack_p8));
    result = memcpy(result + 32, v_stack_m48, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), Arg4);
    goto loc_008BAF5E;
loc_008BB05F:
    if ((*(uint32_t *)((uint32_t)(v_stack_p8) + 0x18)) == ((uint32_t)((uint32_t)(v_stack_p8)))) goto loc_008BB080;
loc_008BB06C:
    if (*(uint64_t *)((uint32_t)(v_stack_p8)) == 0) goto loc_008BAFC0;
    goto loc_008BAFB0;
loc_008BB080:
    result = memcmp(v_stack_m48, *(uint64_t *)((uint32_t)(v_stack_p8)) + 32, v_stack_m40, Arg4);
    if ((uint32_t)(result) != 0) goto loc_008BB06C;
    if (condition_is_less_or_equal) goto loc_008BB442;
loc_008BB0AB:
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_008BB496;
loc_008BB0BE:
    result = KeAbPostRelease(local_r13, *(uint64_t *)((uint32_t)(v_stack_p8)) + 32, v_stack_m40, Arg4);
    result = KeLeaveCriticalRegionThread(v_stack_m50, *(uint64_t *)((uint32_t)(v_stack_p8)) + 32, v_stack_m40, Arg4);
    result = v_stack_m58;
    if (v_stack_m58 != 0) {
        Arg2 = 0x6353624FULL;
        Arg1 = v_stack_m58;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m40, Arg4);
    }
    local_r13 = 0;
    if ((*(uint8_t *)(v_stack_m68)) != 1) goto loc_008BB473;
    if (!sign_flag) goto loc_008BB485;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8))) == 0) goto loc_008BB44E;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8))) + (v_stack_m68);
loc_008BB11A:
    if ((((uint8_t)(*(uint16_t *)(v_stack_m68 + 0x2))) & (4)) == 0) goto loc_008BB46B;
    if (!sign_flag) goto loc_008BB4B0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x10))) == 0) goto loc_008BB48E;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x10))) + (v_stack_m68);
loc_008BB13A:
    result = v_stack_m68;
    local_rbp = 0;
    if (Arg1 != NULL) {
        result = *(uint8_t *)(arg1 + 0x1);
        local_rbp = result * 4 + 11;
        local_rbp = (uint32_t)((local_rbp) & (0xFFFFFFFCULL));
    }
    if (Arg2 != NULL) {
        result = *(uint16_t *)(arg2 + 0x2);
        result = (uint32_t)((result) + (3));
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(result)));
    }
    if ((*(uint64_t *)(arg1 - 0x10)) == 1) goto loc_008BB1FC;
    if ((((uint8_t)(*(uint8_t *)(arg1 - 0x30 + 0x1A))) & (8)) == 0) goto loc_008BB47D;
    result = (uint32_t)((*(uint8_t *)(arg1 - 0x30 + 0x1A)) & (15));
    local_rsi = (Arg1 - 48) - (*(uint8_t *)(result + v_rip + 0x654DFB * 1));
loc_008BB18C:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == (*(uint64_t *)(v_rip + 0x70B90A))) goto loc_008BB460;
    if ((uint32_t)(local_rbp) == 0) goto loc_008BB1CD;
    Arg2 = 0;
    result = PspChargeQuota(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2F8), Arg2, Arg2 + 1, (uint32_t)((uint32_t)(local_rbp)));
    if (sign_flag) goto loc_008BB456;
loc_008BB1CD:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2F8) == 0) goto loc_008BB456;
loc_008BB1E1:
    if (*(uint64_t *)(local_rsi + 0x10) != 0) {
        Arg2 = *(uint32_t *)(local_rsi + 0x8);
        Arg3 = 0;
        result = PsReturnSharedPoolQuota(*(uint64_t *)(local_rsi + 0x10), Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    }
    *(uint32_t *)(local_rsi + 0x8) = (uint32_t)(local_rbp);
    *(uint64_t *)(local_rsi + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2F8);
loc_008BB1FC:
    if (*(uint64_t *)((uint32_t)(v_stack_p8)) + 32 != 0) goto loc_008BB217;
    goto loc_008BB21B;
loc_008BB209:
    local_rsi = 0;
loc_008BB210:
    v_stack_m68 = 0;
    goto loc_008BB230;
loc_008BB217:
    local_rbx = (0) | (15);
loc_008BB21B:
    local_rdi = (uint32_t)((local_rbx) & (15));
    local_rdi = (uint32_t)((local_rdi) + 1);
loc_008BB22B:
loc_008BB230:
    Arg1 = (*(uint64_t *)(arg1 - 0x20)) & (-16);
    Arg2 = *(uint64_t *)(arg1 - 0x20) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x20))) & (2)) != 0) goto loc_008BB401;
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x20))) & (2)) != 0) goto loc_008BB401;
loc_008BB268:
    result = KeAbPostRelease(Arg1 - 32, Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    if (0 != 0) goto loc_008BB4D0;
loc_008BB289:
    if (v_stack_m60 == 0) goto loc_008BB2B3;
    if ((uint32_t)(local_rdi) == 0) goto loc_008BB2B3;
loc_008BB2A0:
    Arg1 = (*(uint64_t *)(v_stack_m60 - 0x20 + 0x8)) - ((uint32_t)((uint32_t)(local_rdi)));
    if (condition_is_less_or_equal) goto loc_008BB2E8;
    if (Arg1 != NULL) goto loc_008BB2A0;
loc_008BB2B3:
    result = *(uint64_t *)(v_stack_m60 - 0x20 + 0x8);
    if (v_stack_m68 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m68, Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    }
    return (uint32_t)((uint32_t)((uint32_t)(0xC00000D7ULL)));
loc_008BB2E8:
    if (condition_is_not_equal) goto loc_008BB4E2;
loc_008BB2EE:
    Arg3 = 0;
    Arg2 = 0;
    local_r14 = ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)))) << (4);
    local_r14 = (local_r14) + (v_rip + 7429046);
    result = KeAbPreAcquire(local_r14, Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r14;
        Arg2 = result;
        Arg1 = local_r14;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_rdi))));
    Arg1 = ((int32_t)((uint32_t)(result))) - ((uint32_t)((uint32_t)(local_rdi)));
    if (condition_is_greater) goto loc_008BB417;
    if (Arg1 != NULL) goto loc_008BB410;
    if ((*(uint64_t *)(local_r14 + 0x8)) == (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_008BB37E;
loc_008BB373:
    if ((*(uint64_t *)(*(uint64_t *)(local_r14 + 0x8))) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_008BB373;
loc_008BB37E:
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38));
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008BB4A3;
loc_008BB39A:
    result = KeAbPostRelease(local_r14, Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x38), (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB2B3;
loc_008BB3BC:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)) = local_r14;
    if (((uint8_t)(result)) != 2) goto loc_008BAFA0;
    Arg1 = 0;
    result = *(uint64_t *)(v_stack_m28 + 0x38);
    if (!(condition_is_equal)) {
        Arg1 = v_stack_m60;
        result = ExfReleasePushLockShared(Arg1, (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    }
    result = KeAbPostRelease(v_stack_m60, (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    result = KeLeaveCriticalRegionThread(v_stack_m28, (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB0EB;
loc_008BB401:
    result = ExfReleasePushLock(*(uint64_t *)(gs_base + (0 + 0x188)) - 32, (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB268;
loc_008BB410:
loc_008BB417:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008BB4B9;
loc_008BB42D:
    result = KeAbPostRelease(local_r14, (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x6353624FULL), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB2B3;
loc_008BB442:
    goto loc_008BB0AB;
loc_008BB44E:
    goto loc_008BB11A;
loc_008BB456:
    goto loc_008BB22B;
loc_008BB460:
    goto loc_008BB1E1;
loc_008BB46B:
    goto loc_008BB13A;
loc_008BB473:
    goto loc_008BB22B;
loc_008BB47D:
    goto loc_008BB18C;
loc_008BB485:
    goto loc_008BB11A;
loc_008BB48E:
    goto loc_008BB13A;
loc_008BB496:
    result = ExfReleasePushLockShared(v_stack_m60, v_stack_m60, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB0BE;
loc_008BB4A3:
    result = ExfTryToWakePushLock(local_r14, v_stack_m60, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB39A;
loc_008BB4B0:
    goto loc_008BB13A;
loc_008BB4B9:
    result = ExfTryToWakePushLock(local_r14, *(uint64_t *)(result + 0x20), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB42D;
loc_008BB4C6:
    goto loc_008BB22B;
loc_008BB4D0:
    result = ObDereferenceSecurityDescriptor(*(uint64_t *)(v_stack_m28 + 0x40) + 32, 16, Arg3, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BB289;
loc_008BB4E2:
    goto loc_008BB2EE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x20` | `8` | `R` |
| `Arg1` | `- 0x20` | `64` | `R` |
| `Arg1` | `- 0x20` | `64` | `R/W` |
| `Arg1` | `- 0x10` | `64` | `R` |
| `Arg1` | `- 0x8` | `64` | `R` |
| `Arg1` | `- 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BAE20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
