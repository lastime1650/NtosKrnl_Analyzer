# ObpIncrementHandleCountEx

- RVA: `0x0086DA10`–`0x0086E3E5` (길이 `2,517` bytes)
- VA: `0x000000014086DA10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C0C4`
- 디코드: `615`개 명령, `2,517/2,517` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0086DAD9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086DAF5` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086DBAA` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (function, `0x00390330`)
- `0x0086DCBC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086DCCA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086DD55` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086DD63` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086DD75` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0086DD9A` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (function, `0x00390330`)
- `0x0086DDB7` → [PspReturnQuota](../../text/39/PspReturnQuota_function_00390C40.md) (function, `0x00390C40`)
- `0x0086DDF4` → [PsReturnSharedPoolQuota](../8B/PsReturnSharedPoolQuota_function_008BCC30.md) (function, `0x008BCC30`)
- `0x0086DE3A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086DE53` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086DE80` → [ObpLockHandleDataBaseEntry](../9C/ObpLockHandleDataBaseEntry_function_009C4E00.md) (function, `0x009C4E00`)
- `0x0086DF37` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (function, `0x00390330`)
- `0x0086DF6C` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086DFAE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086DFBC` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086E01B` → [PspProcessOpen](../AE/PspProcessOpen_function_00AE3620.md) (function, `0x00AE3620`)
- `0x0086E02E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0086E036` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x0086E055` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086E071` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086E093` → [ObpUnlockHandleDatabaseEntry](../A5/ObpUnlockHandleDatabaseEntry_function_00A54234.md) (function, `0x00A54234`)
- `0x0086E0D5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086E0E3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086E0EB` → [ObpDeleteNameCheck](../89/ObpDeleteNameCheck_function_0089A3F0.md) (function, `0x0089A3F0`)
- `0x0086E158` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086E18E` → [MiSectionOpen](../88/MiSectionOpen_function_008871E0.md) (function, `0x008871E0`)
- `0x0086E1D4` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x0086E1DC` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x0086E1EC` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x0086E254` → [OBJECT_HEADER_TO_PROCESS_INFO](../../text/4B/OBJECT_HEADER_TO_PROCESS_INFO_function_004B1364.md) (function, `0x004B1364`)
- `0x0086E270` → [OBJECT_HEADER_TO_PROCESS_INFO](../../text/4B/OBJECT_HEADER_TO_PROCESS_INFO_function_004B1364.md) (function, `0x004B1364`)
- `0x0086E2EB` → [PspThreadOpen](../A0/PspThreadOpen_function_00A0FED0.md) (function, `0x00A0FED0`)
- `0x0086E2F9` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086E338` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086E366` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0086E373` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086E3B0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086E3BE` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)

### Direct callers
- [ObpCreateHandle](ObpCreateHandle_function_0086B950.md) at `0x0086BE5B`
- [ObCaptureObjectStateForDuplication](../89/ObCaptureObjectStateForDuplication_function_00893684.md) at `0x008937D8`
- [ObCompleteObjectDuplication](../89/ObCompleteObjectDuplication_function_0089387C.md) at `0x008938F6`
- [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5324`
- [ObInheritObjectHandle](../94/ObInheritObjectHandle_function_0094D1C4.md) at `0x0094D238`
- [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) at `0x0099F6A5`

### Static image references
- `0x0086DA24` → RVA `0x00E0A740` (`.data`; read)
- `0x0086DA75` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0086DA8B` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0086DB81` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0086DFE6` → RVA `0x00AE3620` (`PspProcessOpen`; read)
- `0x0086E169` → RVA `0x008871E0` (`MiSectionOpen`; read)
- `0x0086E2C6` → RVA `0x00A0FED0` (`PspThreadOpen`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x0086DAD9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086DAF5` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086DBAA` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (`PAGE` → `.text`)
  - `0x0086DCBC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086DCCA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086DD55` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086DD63` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086DD75` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0086DD9A` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (`PAGE` → `.text`)
  - `0x0086DDB7` → [PspReturnQuota](../../text/39/PspReturnQuota_function_00390C40.md) (`PAGE` → `.text`)
  - `0x0086DE3A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086DE53` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086DF37` → [PspChargeQuota](../../text/39/PspChargeQuota_function_00390330.md) (`PAGE` → `.text`)
  - `0x0086DF6C` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086DFAE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086DFBC` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086E02E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0086E036` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x0086E055` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086E071` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086E0D5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086E0E3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086E158` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086E1D4` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x0086E1DC` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x0086E1EC` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x0086E254` → [OBJECT_HEADER_TO_PROCESS_INFO](../../text/4B/OBJECT_HEADER_TO_PROCESS_INFO_function_004B1364.md) (`PAGE` → `.text`)
  - `0x0086E270` → [OBJECT_HEADER_TO_PROCESS_INFO](../../text/4B/OBJECT_HEADER_TO_PROCESS_INFO_function_004B1364.md) (`PAGE` → `.text`)
  - `0x0086E2F9` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086E338` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086E366` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0086E373` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086E3B0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086E3BE` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0086DA10  40 53                           push rbx
0086DA12  55                              push rbp
0086DA13  56                              push rsi
0086DA14  57                              push rdi
0086DA15  41 54                           push r12
0086DA17  41 55                           push r13
0086DA19  41 56                           push r14
0086DA1B  41 57                           push r15
0086DA1D  48 81 EC B8 00 00 00            sub rsp, 0xb8
0086DA24  48 8B 05 15 CD 59 00            mov rax, qword ptr [rip + 0x59cd15]
0086DA2B  48 33 C4                        xor rax, rsp
0086DA2E  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0086DA36  4C 8B AC 24 30 01 00 00         mov r13, qword ptr [rsp + 0x130]
0086DA3E  49 8D 59 D0                     lea rbx, [r9 - 0x30]
0086DA42  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
0086DA46  0F 57 C0                        xorps xmm0, xmm0
0086DA49  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
0086DA4E  4D 8B F0                        mov r14, r8
0086DA51  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0086DA56  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
0086DA5E  48 8B C3                        mov rax, rbx
0086DA61  41 BF 01 00 00 00               mov r15d, 1
0086DA67  48 C1 E8 08                     shr rax, 8
0086DA6B  0F B6 C0                        movzx eax, al
0086DA6E  8B C8                           mov ecx, eax
0086DA70  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0086DA75  0F B6 05 D0 93 75 00            movzx eax, byte ptr [rip + 0x7593d0]
0086DA7C  48 33 C8                        xor rcx, rax
0086DA7F  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
0086DA84  0F B6 43 18                     movzx eax, byte ptr [rbx + 0x18]
0086DA88  48 33 C8                        xor rcx, rax
0086DA8B  48 8D 05 6E 25 79 FF            lea rax, [rip - 0x86da92]
0086DA92  F7 84 24 28 01 00 00 00 04 00 00  test dword ptr [rsp + 0x128], 0x400
0086DA9D  0F 11 84 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm0
0086DAA5  48 8B AC C8 00 78 FC 00         mov rbp, qword ptr [rax + rcx*8 + 0xfc7800]
0086DAAD  41 8B CF                        mov ecx, r15d
0086DAB0  0F B6 84 24 20 01 00 00         movzx eax, byte ptr [rsp + 0x120]
0086DAB8  0F 44 C8                        cmove ecx, eax
0086DABB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086DAC4  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
0086DAC8  45 33 C0                        xor r8d, r8d
0086DACB  33 D2                           xor edx, edx
0086DACD  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086DAD1  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086DAD8  90                              nop
0086DAD9  E8 52 27 9A FF                  call 0x140210230
0086DADE  F0 48 0F BA 6B 10 00            lock bts qword ptr [rbx + 0x10], 0
0086DAE5  48 8B F8                        mov rdi, rax
0086DAE8  73 10                           jae 0x14086dafa
0086DAEA  4C 8D 43 10                     lea r8, [rbx + 0x10]
0086DAEE  48 8B D0                        mov rdx, rax
0086DAF1  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086DAF5  E8 96 21 9A FF                  call 0x14020fc90
0086DAFA  48 85 FF                        test rdi, rdi
0086DAFD  74 04                           je 0x14086db03
0086DAFF  44 88 7F 0A                     mov byte ptr [rdi + 0xa], r15b
0086DB03  0F B6 4B 1B                     movzx ecx, byte ptr [rbx + 0x1b]
0086DB07  48 8D 15 F2 24 79 FF            lea rdx, [rip - 0x86db0e]
0086DB0E  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0086DB12  45 33 E4                        xor r12d, r12d
0086DB15  0F B6 F9                        movzx edi, cl
0086DB18  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
0086DB1D  41 22 FF                        and dil, r15b
0086DB20  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
0086DB25  A8 08                           test al, 8
0086DB27  74 11                           je 0x14086db3a
0086DB29  83 E0 0F                        and eax, 0xf
0086DB2C  4C 8B E3                        mov r12, rbx
0086DB2F  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
0086DB37  4C 2B E0                        sub r12, rax
0086DB3A  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
0086DB3F  40 84 FF                        test dil, dil
0086DB42  0F 84 91 00 00 00               je 0x14086dbd9
0086DB48  80 E1 FE                        and cl, 0xfe
0086DB4B  88 4B 1B                        mov byte ptr [rbx + 0x1b], cl
0086DB4E  4D 85 E4                        test r12, r12
0086DB51  0F 84 A4 06 00 00               je 0x14086e1fb
0086DB57  41 8B 3C 24                     mov edi, dword ptr [r12]
0086DB5B  41 8B 74 24 04                  mov esi, dword ptr [r12 + 4]
0086DB60  4D 85 ED                        test r13, r13
0086DB63  0F 85 2B 03 00 00               jne 0x14086de94
0086DB69  4C 8B 6B 28                     mov r13, qword ptr [rbx + 0x28]
0086DB6D  4D 85 ED                        test r13, r13
0086DB70  74 0A                           je 0x14086db7c
0086DB72  49 83 E5 F0                     and r13, 0xfffffffffffffff0
0086DB76  0F 85 18 03 00 00               jne 0x14086de94
0086DB7C  44 8B 6C 24 44                  mov r13d, dword ptr [rsp + 0x44]
0086DB81  4C 3B 35 28 8F 75 00            cmp r14, qword ptr [rip + 0x758f28]
0086DB88  44 8B E6                        mov r12d, esi
0086DB8B  8B F7                           mov esi, edi
0086DB8D  0F 84 31 02 00 00               je 0x14086ddc4
0086DB93  49 8B BE F8 02 00 00            mov rdi, qword ptr [r14 + 0x2f8]
0086DB9A  48 85 F6                        test rsi, rsi
0086DB9D  74 18                           je 0x14086dbb7
0086DB9F  44 8B CE                        mov r9d, esi
0086DBA2  45 8B C7                        mov r8d, r15d
0086DBA5  33 D2                           xor edx, edx
0086DBA7  48 8B CF                        mov rcx, rdi
0086DBAA  E8 81 27 B2 FF                  call 0x140390330
0086DBAF  85 C0                           test eax, eax
0086DBB1  0F 88 16 02 00 00               js 0x14086ddcd
0086DBB7  4D 85 E4                        test r12, r12
0086DBBA  0F 85 CF 01 00 00               jne 0x14086dd8f
0086DBC0  F0 FF 87 00 02 00 00            lock inc dword ptr [rdi + 0x200]
0086DBC7  48 89 7B 20                     mov qword ptr [rbx + 0x20], rdi
0086DBCB  48 85 FF                        test rdi, rdi
0086DBCE  0F 84 FF 01 00 00               je 0x14086ddd3
0086DBD4  0F B6 7C 24 40                  movzx edi, byte ptr [rsp + 0x40]
0086DBD9  44 0F B6 43 1B                  movzx r8d, byte ptr [rbx + 0x1b]
0086DBDE  33 C9                           xor ecx, ecx
0086DBE0  8B 94 24 28 01 00 00            mov edx, dword ptr [rsp + 0x128]
0086DBE7  41 0F B6 C0                     movzx eax, r8b
0086DBEB  24 08                           and al, 8
0086DBED  8B F1                           mov esi, ecx
0086DBEF  F6 C2 20                        test dl, 0x20
0086DBF2  0F 85 40 06 00 00               jne 0x14086e238
0086DBF8  84 C0                           test al, al
0086DBFA  0F 85 EF 00 00 00               jne 0x14086dcef
0086DC00  40 38 74 24 60                  cmp byte ptr [rsp + 0x60], sil
0086DC05  74 0A                           je 0x14086dc11
0086DC07  F6 43 1B 04                     test byte ptr [rbx + 0x1b], 4
0086DC0B  0F 85 C0 07 00 00               jne 0x14086e3d1
0086DC11  48 39 73 08                     cmp qword ptr [rbx + 8], rsi
0086DC15  75 09                           jne 0x14086dc20
0086DC17  40 84 FF                        test dil, dil
0086DC1A  0F 84 78 05 00 00               je 0x14086e198
0086DC20  F6 45 42 10                     test byte ptr [rbp + 0x42], 0x10
0086DC24  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0086DC28  0F 85 47 02 00 00               jne 0x14086de75
0086DC2E  F0 48 FF 43 08                  lock inc qword ptr [rbx + 8]
0086DC33  48 83 7D 78 00                  cmp qword ptr [rbp + 0x78], 0
0086DC38  0F 85 38 03 00 00               jne 0x14086df76
0086DC3E  F6 45 42 10                     test byte ptr [rbp + 0x42], 0x10
0086DC42  74 3F                           je 0x14086dc83
0086DC44  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0086DC48  48 8D 0D B1 23 79 FF            lea rcx, [rip - 0x86dc4f]
0086DC4F  83 E0 07                        and eax, 7
0086DC52  48 8B D3                        mov rdx, rbx
0086DC55  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0086DC5D  48 2B D0                        sub rdx, rax
0086DC60  F6 43 1B 40                     test byte ptr [rbx + 0x1b], 0x40
0086DC64  0F 84 8B 04 00 00               je 0x14086e0f5
0086DC6A  FE 4A 0B                        dec byte ptr [rdx + 0xb]
0086DC6D  8B 42 08                        mov eax, dword ptr [rdx + 8]
0086DC70  8B C8                           mov ecx, eax
0086DC72  C1 E9 18                        shr ecx, 0x18
0086DC75  FF C0                           inc eax
0086DC77  25 FF FF FF 00                  and eax, 0xffffff
0086DC7C  0F C9                           bswap ecx
0086DC7E  0B C8                           or ecx, eax
0086DC80  89 4A 08                        mov dword ptr [rdx + 8], ecx
0086DC83  0F 0D 4B 10                     prefetchw byte ptr [rbx + 0x10]
0086DC87  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0086DC8B  41 BC 00 00 00 00               mov r12d, 0
0086DC91  48 8B C8                        mov rcx, rax
0086DC94  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086DC98  48 83 F9 10                     cmp rcx, 0x10
0086DC9C  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086DCA0  49 0F 46 D4                     cmovbe rdx, r12
0086DCA4  A8 02                           test al, 2
0086DCA6  0F 85 A8 04 00 00               jne 0x14086e154
0086DCAC  F0 48 0F B1 53 10               lock cmpxchg qword ptr [rbx + 0x10], rdx
0086DCB2  0F 85 9C 04 00 00               jne 0x14086e154
0086DCB8  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086DCBC  E8 3F 39 A7 FF                  call 0x1402e1600
0086DCC1  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086DCCA  E8 21 13 9F FF                  call 0x14025eff0
0086DCCF  44 39 64 24 4C                  cmp dword ptr [rsp + 0x4c], r12d
0086DCD4  0F 84 29 01 00 00               je 0x14086de03
0086DCDA  F0 44 0F C1 7D 30               lock xadd dword ptr [rbp + 0x30], r15d
0086DCE0  41 FF C7                        inc r15d
0086DCE3  44 3B 7D 38                     cmp r15d, dword ptr [rbp + 0x38]
0086DCE7  76 7F                           jbe 0x14086dd68
0086DCE9  44 89 7D 38                     mov dword ptr [rbp + 0x38], r15d
0086DCED  EB 79                           jmp 0x14086dd68
0086DCEF  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0086DCF3  A8 10                           test al, 0x10
0086DCF5  74 18                           je 0x14086dd0f
0086DCF7  83 E0 1F                        and eax, 0x1f
0086DCFA  48 8D 0D FF 22 79 FF            lea rcx, [rip - 0x86dd01]
0086DD01  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0086DD09  48 8B CB                        mov rcx, rbx
0086DD0C  48 2B C8                        sub rcx, rax
0086DD0F  48 39 31                        cmp qword ptr [rcx], rsi
0086DD12  0F 84 96 05 00 00               je 0x14086e2ae
0086DD18  BE 22 00 00 C0                  mov esi, 0xc0000022
0086DD1D  0F 0D 4B 10                     prefetchw byte ptr [rbx + 0x10]
0086DD21  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0086DD25  48 8B C8                        mov rcx, rax
0086DD28  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086DD2C  48 83 F9 10                     cmp rcx, 0x10
0086DD30  B9 00 00 00 00                  mov ecx, 0
0086DD35  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086DD39  48 0F 46 D1                     cmovbe rdx, rcx
0086DD3D  A8 02                           test al, 2
0086DD3F  0F 85 23 02 00 00               jne 0x14086df68
0086DD45  F0 48 0F B1 53 10               lock cmpxchg qword ptr [rbx + 0x10], rdx
0086DD4B  0F 85 17 02 00 00               jne 0x14086df68
0086DD51  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086DD55  E8 A6 38 A7 FF                  call 0x1402e1600
0086DD5A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086DD63  E8 88 12 9F FF                  call 0x14025eff0
0086DD68  8B C6                           mov eax, esi
0086DD6A  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
0086DD72  48 33 CC                        xor rcx, rsp
0086DD75  E8 C6 E8 E3 FF                  call 0x1406ac640
0086DD7A  48 81 C4 B8 00 00 00            add rsp, 0xb8
0086DD81  41 5F                           pop r15
0086DD83  41 5E                           pop r14
0086DD85  41 5D                           pop r13
0086DD87  41 5C                           pop r12
0086DD89  5F                              pop rdi
0086DD8A  5E                              pop rsi
0086DD8B  5D                              pop rbp
0086DD8C  5B                              pop rbx
0086DD8D  C3                              ret
0086DD8E  CC                              int3
0086DD8F  4D 8B CC                        mov r9, r12
0086DD92  45 33 C0                        xor r8d, r8d
0086DD95  33 D2                           xor edx, edx
0086DD97  48 8B CF                        mov rcx, rdi
0086DD9A  E8 91 25 B2 FF                  call 0x140390330
0086DD9F  85 C0                           test eax, eax
0086DDA1  0F 89 19 FE FF FF               jns 0x14086dbc0
0086DDA7  48 85 F6                        test rsi, rsi
0086DDAA  74 10                           je 0x14086ddbc
0086DDAC  4C 8B CE                        mov r9, rsi
0086DDAF  45 8B C7                        mov r8d, r15d
0086DDB2  33 D2                           xor edx, edx
0086DDB4  48 8B CF                        mov rcx, rdi
0086DDB7  E8 84 2E B2 FF                  call 0x140390c40
0086DDBC  33 C0                           xor eax, eax
0086DDBE  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0086DDC2  EB 0F                           jmp 0x14086ddd3
0086DDC4  4C 89 7B 20                     mov qword ptr [rbx + 0x20], r15
0086DDC8  E9 07 FE FF FF                  jmp 0x14086dbd4
0086DDCD  33 C0                           xor eax, eax
0086DDCF  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0086DDD3  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0086DDD8  48 85 C0                        test rax, rax
0086DDDB  0F 84 DB 04 00 00               je 0x14086e2bc
0086DDE1  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
0086DDE5  48 85 C9                        test rcx, rcx
0086DDE8  0F 84 CE 04 00 00               je 0x14086e2bc
0086DDEE  41 8B D5                        mov edx, r13d
0086DDF1  45 33 C0                        xor r8d, r8d
0086DDF4  E8 37 EE 04 00                  call 0x1408bcc30
0086DDF9  BE 44 00 00 C0                  mov esi, 0xc0000044
0086DDFE  E9 1A FF FF FF                  jmp 0x14086dd1d
0086DE03  44 84 7B 1A                     test byte ptr [rbx + 0x1a], r15b
0086DE07  0F 84 CD FE FF FF               je 0x14086dcda
0086DE0D  48 8D 7B E0                     lea rdi, [rbx - 0x20]
0086DE11  48 85 FF                        test rdi, rdi
0086DE14  0F 84 C0 FE FF FF               je 0x14086dcda
0086DE1A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086DE23  48 8D 9D B8 00 00 00            lea rbx, [rbp + 0xb8]
0086DE2A  45 33 C0                        xor r8d, r8d
0086DE2D  33 D2                           xor edx, edx
0086DE2F  48 8B CB                        mov rcx, rbx
0086DE32  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0086DE39  90                              nop
0086DE3A  E8 F1 23 9A FF                  call 0x140210230
0086DE3F  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0086DE45  4C 8B F0                        mov r14, rax
0086DE48  73 0E                           jae 0x14086de58
0086DE4A  4C 8B C3                        mov r8, rbx
0086DE4D  48 8B D0                        mov rdx, rax
0086DE50  48 8B CB                        mov rcx, rbx
0086DE53  E8 38 1E 9A FF                  call 0x14020fc90
0086DE58  4D 85 F6                        test r14, r14
0086DE5B  74 04                           je 0x14086de61
0086DE5D  45 88 7E 0A                     mov byte ptr [r14 + 0xa], r15b
0086DE61  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0086DE65  48 39 28                        cmp qword ptr [rax], rbp
0086DE68  0F 84 95 04 00 00               je 0x14086e303
0086DE6E  B9 03 00 00 00                  mov ecx, 3
0086DE73  CD 29                           int 0x29
0086DE75  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
0086DE7A  49 8B D6                        mov rdx, r14
0086DE7D  48 8B CB                        mov rcx, rbx
0086DE80  E8 7B 6F 15 00                  call 0x1409c4e00
0086DE85  8B F0                           mov esi, eax
0086DE87  85 C0                           test eax, eax
0086DE89  0F 89 9F FD FF FF               jns 0x14086dc2e
0086DE8F  E9 89 FE FF FF                  jmp 0x14086dd1d
0086DE94  33 C0                           xor eax, eax
0086DE96  8B D0                           mov edx, eax
0086DE98  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0086DE9C  45 38 7D 00                     cmp byte ptr [r13], r15b
0086DEA0  0F 85 DB 04 00 00               jne 0x14086e381
0086DEA6  41 0F B7 4D 02                  movzx ecx, word ptr [r13 + 2]
0086DEAB  66 85 C9                        test cx, cx
0086DEAE  0F 89 D7 04 00 00               jns 0x14086e38b
0086DEB4  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
0086DEB8  85 C0                           test eax, eax
0086DEBA  0F 84 A2 02 00 00               je 0x14086e162
0086DEC0  49 03 C5                        add rax, r13
0086DEC3  F6 C1 04                        test cl, 4
0086DEC6  0F 84 AE 04 00 00               je 0x14086e37a
0086DECC  66 85 C9                        test cx, cx
0086DECF  0F 89 F3 04 00 00               jns 0x14086e3c8
0086DED5  41 8B 4D 10                     mov ecx, dword ptr [r13 + 0x10]
0086DED9  85 C9                           test ecx, ecx
0086DEDB  0F 84 B3 04 00 00               je 0x14086e394
0086DEE1  49 03 CD                        add rcx, r13
0086DEE4  48 85 C0                        test rax, rax
0086DEE7  74 12                           je 0x14086defb
0086DEE9  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
0086DEED  8D 14 85 0B 00 00 00            lea edx, [rax*4 + 0xb]
0086DEF4  83 E2 FC                        and edx, 0xfffffffc
0086DEF7  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0086DEFB  48 85 C9                        test rcx, rcx
0086DEFE  74 10                           je 0x14086df10
0086DF00  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
0086DF04  83 C0 03                        add eax, 3
0086DF07  83 E0 FC                        and eax, 0xfffffffc
0086DF0A  03 D0                           add edx, eax
0086DF0C  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0086DF10  85 D2                           test edx, edx
0086DF12  74 4A                           je 0x14086df5e
0086DF14  4C 3B 35 95 8B 75 00            cmp r14, qword ptr [rip + 0x758b95]
0086DF1B  44 8B CA                        mov r9d, edx
0086DF1E  0F 84 05 03 00 00               je 0x14086e229
0086DF24  4D 8B AE F8 02 00 00            mov r13, qword ptr [r14 + 0x2f8]
0086DF2B  85 D2                           test edx, edx
0086DF2D  74 19                           je 0x14086df48
0086DF2F  45 8B C7                        mov r8d, r15d
0086DF32  33 D2                           xor edx, edx
0086DF34  49 8B CD                        mov rcx, r13
0086DF37  E8 F4 23 B2 FF                  call 0x140390330
0086DF3C  85 C0                           test eax, eax
0086DF3E  0F 88 71 03 00 00               js 0x14086e2b5
0086DF44  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
0086DF48  F0 41 FF 85 00 02 00 00         lock inc dword ptr [r13 + 0x200]
0086DF50  4D 89 6C 24 10                  mov qword ptr [r12 + 0x10], r13
0086DF55  4D 85 ED                        test r13, r13
0086DF58  0F 84 5E 03 00 00               je 0x14086e2bc
0086DF5E  41 89 54 24 08                  mov dword ptr [r12 + 8], edx
0086DF63  E9 14 FC FF FF                  jmp 0x14086db7c
0086DF68  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086DF6C  E8 5F 59 9F FF                  call 0x1402638d0
0086DF71  E9 DB FD FF FF                  jmp 0x14086dd51
0086DF76  0F 0D 4B 10                     prefetchw byte ptr [rbx + 0x10]
0086DF7A  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0086DF7E  BE 00 00 00 00                  mov esi, 0
0086DF83  48 8B C8                        mov rcx, rax
0086DF86  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086DF8A  48 83 F9 10                     cmp rcx, 0x10
0086DF8E  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086DF92  48 0F 46 D6                     cmovbe rdx, rsi
0086DF96  A8 02                           test al, 2
0086DF98  0F 85 57 03 00 00               jne 0x14086e2f5
0086DF9E  F0 48 0F B1 53 10               lock cmpxchg qword ptr [rbx + 0x10], rdx
0086DFA4  0F 85 4B 03 00 00               jne 0x14086e2f5
0086DFAA  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086DFAE  E8 4D 36 A7 FF                  call 0x1402e1600
0086DFB3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086DFBC  E8 2F 10 9F FF                  call 0x14025eff0
0086DFC1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086DFCA  40 32 FF                        xor dil, dil
0086DFCD  44 8B 54 24 4C                  mov r10d, dword ptr [rsp + 0x4c]
0086DFD2  4C 8B E6                        mov r12, rsi
0086DFD5  4C 3B B0 B8 00 00 00            cmp r14, qword ptr [rax + 0xb8]
0086DFDC  0F 85 E1 01 00 00               jne 0x14086e1c3
0086DFE2  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0086DFE6  48 8D 0D 33 56 27 00            lea rcx, [rip + 0x275633]
0086DFED  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0086DFF2  4D 8B C6                        mov r8, r14
0086DFF5  0F B6 94 24 20 01 00 00         movzx edx, byte ptr [rsp + 0x120]
0086DFFD  48 3B C1                        cmp rax, rcx
0086E000  0F 85 63 01 00 00               jne 0x14086e169
0086E006  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0086E00A  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0086E00E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0086E013  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086E018  41 8B CA                        mov ecx, r10d
0086E01B  E8 00 56 27 00                  call 0x140ae3620
0086E020  8B F0                           mov esi, eax
0086E022  40 84 FF                        test dil, dil
0086E025  74 14                           je 0x14086e03b
0086E027  33 D2                           xor edx, edx
0086E029  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0086E02E  E8 FD 9C 9A FF                  call 0x140217d30
0086E033  49 8B CC                        mov rcx, r12
0086E036  E8 85 BA BD FF                  call 0x140449ac0
0086E03B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086E044  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086E048  45 33 C0                        xor r8d, r8d
0086E04B  33 D2                           xor edx, edx
0086E04D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086E054  90                              nop
0086E055  E8 D6 21 9A FF                  call 0x140210230
0086E05A  F0 48 0F BA 6B 10 00            lock bts qword ptr [rbx + 0x10], 0
0086E061  4C 8B E8                        mov r13, rax
0086E064  73 10                           jae 0x14086e076
0086E066  4C 8D 43 10                     lea r8, [rbx + 0x10]
0086E06A  48 8B D0                        mov rdx, rax
0086E06D  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086E071  E8 1A 1C 9A FF                  call 0x14020fc90
0086E076  4D 85 ED                        test r13, r13
0086E079  74 04                           je 0x14086e07f
0086E07B  45 88 7D 0A                     mov byte ptr [r13 + 0xa], r15b
0086E07F  85 F6                           test esi, esi
0086E081  0F 89 B7 FB FF FF               jns 0x14086dc3e
0086E087  F6 45 42 10                     test byte ptr [rbp + 0x42], 0x10
0086E08B  74 0B                           je 0x14086e098
0086E08D  49 8B D6                        mov rdx, r14
0086E090  48 8B CB                        mov rcx, rbx
0086E093  E8 9C 61 1E 00                  call 0x140a54234
0086E098  F0 48 FF 4B 08                  lock dec qword ptr [rbx + 8]
0086E09D  0F 0D 4B 10                     prefetchw byte ptr [rbx + 0x10]
0086E0A1  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0086E0A5  48 8B C8                        mov rcx, rax
0086E0A8  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086E0AC  48 83 F9 10                     cmp rcx, 0x10
0086E0B0  B9 00 00 00 00                  mov ecx, 0
0086E0B5  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086E0B9  48 0F 46 D1                     cmovbe rdx, rcx
0086E0BD  A8 02                           test al, 2
0086E0BF  0F 85 F5 02 00 00               jne 0x14086e3ba
0086E0C5  F0 48 0F B1 53 10               lock cmpxchg qword ptr [rbx + 0x10], rdx
0086E0CB  0F 85 E9 02 00 00               jne 0x14086e3ba
0086E0D1  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086E0D5  E8 26 35 A7 FF                  call 0x1402e1600
0086E0DA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086E0E3  E8 08 0F 9F FF                  call 0x14025eff0
0086E0E8  48 8B CB                        mov rcx, rbx
0086E0EB  E8 00 C3 02 00                  call 0x14089a3f0
0086E0F0  E9 73 FC FF FF                  jmp 0x14086dd68
0086E0F5  48 8B 02                        mov rax, qword ptr [rdx]
0086E0F8  33 D2                           xor edx, edx
0086E0FA  44 8B C2                        mov r8d, edx
0086E0FD  8B 08                           mov ecx, dword ptr [rax]
0086E0FF  48 83 C0 08                     add rax, 8
0086E103  85 C9                           test ecx, ecx
0086E105  74 1D                           je 0x14086e124
0086E107  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0086E110  4C 8B D2                        mov r10, rdx
0086E113  4C 8B CA                        mov r9, rdx
0086E116  4C 39 30                        cmp qword ptr [rax], r14
0086E119  74 24                           je 0x14086e13f
0086E11B  48 83 C0 10                     add rax, 0x10
0086E11F  83 C1 FF                        add ecx, -1
0086E122  75 EC                           jne 0x14086e110
0086E124  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
0086E127  8D 41 01                        lea eax, [rcx + 1]
0086E12A  33 C1                           xor eax, ecx
0086E12C  25 FF FF FF 00                  and eax, 0xffffff
0086E131  33 C1                           xor eax, ecx
0086E133  89 42 08                        mov dword ptr [rdx + 8], eax
0086E136  41 FE 48 0B                     dec byte ptr [r8 + 0xb]
0086E13A  E9 44 FB FF FF                  jmp 0x14086dc83
0086E13F  4D 85 C9                        test r9, r9
0086E142  48 8B D0                        mov rdx, rax
0086E145  4C 8B C0                        mov r8, rax
0086E148  49 0F 45 D2                     cmovne rdx, r10
0086E14C  80 78 0B FF                     cmp byte ptr [rax + 0xb], 0xff
0086E150  72 D2                           jb 0x14086e124
0086E152  EB C7                           jmp 0x14086e11b
0086E154  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086E158  E8 73 57 9F FF                  call 0x1402638d0
0086E15D  E9 56 FB FF FF                  jmp 0x14086dcb8
0086E162  33 C0                           xor eax, eax
0086E164  E9 5A FD FF FF                  jmp 0x14086dec3
0086E169  48 8D 0D 70 90 01 00            lea rcx, [rip + 0x19070]
0086E170  48 3B C1                        cmp rax, rcx
0086E173  0F 85 4D 01 00 00               jne 0x14086e2c6
0086E179  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0086E17E  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0086E182  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0086E186  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086E18B  41 8B CA                        mov ecx, r10d
0086E18E  E8 4D 90 01 00                  call 0x1408871e0
0086E193  E9 88 FE FF FF                  jmp 0x14086e020
0086E198  F6 45 42 10                     test byte ptr [rbp + 0x42], 0x10
0086E19C  0F 84 7E FA FF FF               je 0x14086dc20
0086E1A2  48 39 75 78                     cmp qword ptr [rbp + 0x78], rsi
0086E1A6  0F 85 74 FA FF FF               jne 0x14086dc20
0086E1AC  48 39 B5 80 00 00 00            cmp qword ptr [rbp + 0x80], rsi
0086E1B3  0F 84 67 FA FF FF               je 0x14086dc20
0086E1B9  BE 01 00 00 C0                  mov esi, 0xc0000001
0086E1BE  E9 5A FB FF FF                  jmp 0x14086dd1d
0086E1C3  41 83 FA 03                     cmp r10d, 3
0086E1C7  0F 84 15 FE FF FF               je 0x14086dfe2
0086E1CD  49 8B CE                        mov rcx, r14
0086E1D0  41 0F B6 FF                     movzx edi, r15b
0086E1D4  E8 07 DD BD FF                  call 0x14044bee0
0086E1D9  48 8B C8                        mov rcx, rax
0086E1DC  E8 DF 46 BD FF                  call 0x1404428c0
0086E1E1  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0086E1E6  49 8B CE                        mov rcx, r14
0086E1E9  4C 8B E0                        mov r12, rax
0086E1EC  E8 0F 86 9A FF                  call 0x140216800
0086E1F1  44 8B 54 24 4C                  mov r10d, dword ptr [rsp + 0x4c]
0086E1F6  E9 E7 FD FF FF                  jmp 0x14086dfe2
0086E1FB  0F B6 05 4A 8C 75 00            movzx eax, byte ptr [rip + 0x758c4a]
0086E202  0F B6 4C 24 70                  movzx ecx, byte ptr [rsp + 0x70]
0086E207  48 33 C8                        xor rcx, rax
0086E20A  0F B6 43 18                     movzx eax, byte ptr [rbx + 0x18]
0086E20E  48 33 C8                        xor rcx, rax
0086E211  48 8B 84 CA 00 78 FC 00         mov rax, qword ptr [rdx + rcx*8 + 0xfc7800]
0086E219  8B 78 68                        mov edi, dword ptr [rax + 0x68]
0086E21C  8B 70 6C                        mov esi, dword ptr [rax + 0x6c]
0086E21F  33 C0                           xor eax, eax
0086E221  44 8B E8                        mov r13d, eax
0086E224  E9 58 F9 FF FF                  jmp 0x14086db81
0086E229  4D 89 7C 24 10                  mov qword ptr [r12 + 0x10], r15
0086E22E  41 89 54 24 08                  mov dword ptr [r12 + 8], edx
0086E233  E9 44 F9 FF FF                  jmp 0x14086db7c
0086E238  84 C0                           test al, al
0086E23A  0F 95 C1                        setne cl
0086E23D  F6 C2 02                        test dl, 2
0086E240  0F 94 C0                        sete al
0086E243  84 C8                           test al, cl
0086E245  0F 84 90 01 00 00               je 0x14086e3db
0086E24B  41 80 E0 08                     and r8b, 8
0086E24F  74 0D                           je 0x14086e25e
0086E251  48 8B CB                        mov rcx, rbx
0086E254  E8 0B 31 C4 FF                  call 0x1404b1364
0086E259  48 39 30                        cmp qword ptr [rax], rsi
0086E25C  75 0F                           jne 0x14086e26d
0086E25E  48 39 73 08                     cmp qword ptr [rbx + 8], rsi
0086E262  0F 85 B0 FA FF FF               jne 0x14086dd18
0086E268  45 84 C0                        test r8b, r8b
0086E26B  74 22                           je 0x14086e28f
0086E26D  48 8B CB                        mov rcx, rbx
0086E270  E8 EF 30 C4 FF                  call 0x1404b1364
0086E275  48 8B 08                        mov rcx, qword ptr [rax]
0086E278  48 85 C9                        test rcx, rcx
0086E27B  74 12                           je 0x14086e28f
0086E27D  33 C0                           xor eax, eax
0086E27F  45 84 C0                        test r8b, r8b
0086E282  48 0F 45 C1                     cmovne rax, rcx
0086E286  49 3B C6                        cmp rax, r14
0086E289  0F 85 89 FA FF FF               jne 0x14086dd18
0086E28F  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0086E293  48 8D 0D 66 1D 79 FF            lea rcx, [rip - 0x86e29a]
0086E29A  83 E0 1F                        and eax, 0x1f
0086E29D  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0086E2A5  48 8B CB                        mov rcx, rbx
0086E2A8  48 2B C8                        sub rcx, rax
0086E2AB  4C 89 31                        mov qword ptr [rcx], r14
0086E2AE  33 C9                           xor ecx, ecx
0086E2B0  E9 4B F9 FF FF                  jmp 0x14086dc00
0086E2B5  33 C0                           xor eax, eax
0086E2B7  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
0086E2BC  BE 44 00 00 C0                  mov esi, 0xc0000044
0086E2C1  E9 57 FA FF FF                  jmp 0x14086dd1d
0086E2C6  48 8D 0D 03 1C 1A 00            lea rcx, [rip + 0x1a1c03]
0086E2CD  48 3B C1                        cmp rax, rcx
0086E2D0  0F 85 C5 00 00 00               jne 0x14086e39b
0086E2D6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0086E2DB  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0086E2DF  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0086E2E3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086E2E8  41 8B CA                        mov ecx, r10d
0086E2EB  E8 E0 1B 1A 00                  call 0x140a0fed0
0086E2F0  E9 2B FD FF FF                  jmp 0x14086e020
0086E2F5  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086E2F9  E8 D2 55 9F FF                  call 0x1402638d0
0086E2FE  E9 A7 FC FF FF                  jmp 0x14086dfaa
0086E303  48 89 2F                        mov qword ptr [rdi], rbp
0086E306  48 89 47 08                     mov qword ptr [rdi + 8], rax
0086E30A  48 89 38                        mov qword ptr [rax], rdi
0086E30D  48 89 7D 08                     mov qword ptr [rbp + 8], rdi
0086E311  0F 0D 0B                        prefetchw byte ptr [rbx]
0086E314  48 8B 03                        mov rax, qword ptr [rbx]
0086E317  48 8B C8                        mov rcx, rax
0086E31A  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086E31E  48 83 F9 10                     cmp rcx, 0x10
0086E322  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086E326  49 0F 46 D4                     cmovbe rdx, r12
0086E32A  A8 02                           test al, 2
0086E32C  75 42                           jne 0x14086e370
0086E32E  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0086E333  75 3B                           jne 0x14086e370
0086E335  48 8B CB                        mov rcx, rbx
0086E338  E8 C3 32 A7 FF                  call 0x1402e1600
0086E33D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086E346  90                              nop
0086E347  66 44 01 B9 E6 01 00 00         add word ptr [rcx + 0x1e6], r15w
0086E34F  0F 85 85 F9 FF FF               jne 0x14086dcda
0086E355  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
0086E35C  90                              nop
0086E35D  48 39 00                        cmp qword ptr [rax], rax
0086E360  0F 84 74 F9 FF FF               je 0x14086dcda
0086E366  E8 15 49 A7 FF                  call 0x1402e2c80
0086E36B  E9 6A F9 FF FF                  jmp 0x14086dcda
0086E370  48 8B CB                        mov rcx, rbx
0086E373  E8 58 55 9F FF                  call 0x1402638d0
0086E378  EB BB                           jmp 0x14086e335
0086E37A  33 C9                           xor ecx, ecx
0086E37C  E9 63 FB FF FF                  jmp 0x14086dee4
0086E381  BE 58 00 00 C0                  mov esi, 0xc0000058
0086E386  E9 92 F9 FF FF                  jmp 0x14086dd1d
0086E38B  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
0086E38F  E9 2F FB FF FF                  jmp 0x14086dec3
0086E394  33 C9                           xor ecx, ecx
0086E396  E9 49 FB FF FF                  jmp 0x14086dee4
0086E39B  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0086E39F  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0086E3A3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0086E3A8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086E3AD  41 8B CA                        mov ecx, r10d
0086E3B0  E8 1B C7 E4 FF                  call 0x1406baad0
0086E3B5  E9 66 FC FF FF                  jmp 0x14086e020
0086E3BA  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0086E3BE  E8 0D 55 9F FF                  call 0x1402638d0
0086E3C3  E9 09 FD FF FF                  jmp 0x14086e0d1
0086E3C8  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
0086E3CC  E9 13 FB FF FF                  jmp 0x14086dee4
0086E3D1  BE 22 00 00 C0                  mov esi, 0xc0000022
0086E3D6  E9 42 F9 FF FF                  jmp 0x14086dd1d
0086E3DB  BE 0D 00 00 C0                  mov esi, 0xc000000d
0086E3E0  E9 38 F9 FF FF                  jmp 0x14086dd1d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpIncrementHandleCountEx(int a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int8 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (184);
    result = (*(unsigned __int64 *)(v_rip + 5885205)) ^ (v_rsp);
    v_stack_m50 = result;
    v_stack_mAC = a1;
    v_stack_m80 = v_xmm0;
    v_stack_mA8 = a2;
    v_stack_m70 = v_xmm0;
    result = (a4 - 48) >> (8);
    v_stack_m88 = (unsigned __int8)(result);
    a1 = ((unsigned int)((unsigned int)((unsigned __int8)(result)))) ^ (*(unsigned __int8 *)(v_rip + 7705552));
    v_stack_mA0 = a4;
    a1 = (a1) ^ (*(unsigned __int8 *)(a4 - 48 + 24));
    v_stack_m60 = v_xmm0;
    a1 = 1;
    if (((a6) & (0x400ULL)) == 0) { a1 = a5; }
    v_stack_m98 = a1;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a4 - 48 + 16, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a4 - 48 + 16;
        a2 = result;
        a1 = a4 - 48 + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r12 = 0;
    v_stack_mB4 = 0;
    v_rdi = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a4 - 48 + 27))) & (1));
    v_stack_mB8 = (unsigned __int8)(v_rdi);
    result = *(unsigned __int8 *)(a4 - 48 + 26);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 - 48 + 26))) & (8)) != 0) {
        result = (unsigned int)((*(unsigned __int8 *)(a4 - 48 + 26)) & (15));
        v_r12 = a4 - 48;
        result = *(unsigned __int8 *)(result + v_rip - 8837902 * 1 + 15794048);
        v_r12 = (v_r12) - (result);
    }
    v_stack_m90 = v_r12;
    if ((unsigned __int8)(v_rdi) == 0) goto loc_0086DBD9;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 - 48 + 27)) & (254));
    *(unsigned __int8 *)(a4 - 48 + 27) = (unsigned __int8)(a1);
    if (v_r12 == 0) goto loc_0086E1FB;
    if (a7 != 0) goto loc_0086DE94;
    if (*(unsigned __int64 *)(a4 - 48 + 40) == 0) goto loc_0086DB7C;
    v_r13 = (*(unsigned __int64 *)(a4 - 48 + 40)) & (-16);
    if (condition_is_not_equal) goto loc_0086DE94;
loc_0086DB7C:
loc_0086DB81:
    if (a3 == (*(unsigned __int64 *)(v_rip + 7704360))) goto loc_0086DDC4;
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))) == 0) goto loc_0086DBB7;
    a2 = 0;
    result = PspChargeQuota(*(unsigned __int64 *)(a3 + 760), a2, 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))))));
    if (sign_flag) goto loc_0086DDCD;
loc_0086DBB7:
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 4)))) != 0) goto loc_0086DD8F;
loc_0086DBC0:
    *(unsigned __int64 *)(a4 - 48 + 32) = *(unsigned __int64 *)(a3 + 760);
    if (*(unsigned __int64 *)(a3 + 760) == 0) goto loc_0086DDD3;
loc_0086DBD4:
loc_0086DBD9:
    a1 = 0;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a4 - 48 + 27))) & (8));
    if ((((unsigned __int8)((unsigned int)(a6))) & (32)) != 0) goto loc_0086E238;
    if ((unsigned __int8)(result) != 0) goto loc_0086DCEF;
loc_0086DC00:
    if (v_stack_m98 == 0) goto loc_0086DC11;
    if (((*(unsigned __int8 *)(a4 - 48 + 27)) & (4)) != 0) goto loc_0086E3D1;
loc_0086DC11:
    if ((*(unsigned __int64 *)(a4 - 48 + 8)) != 0) goto loc_0086DC20;
    if ((unsigned __int8)(v_stack_mB8) == 0) goto loc_0086E198;
loc_0086DC20:
    v_stack_mB0 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 66)) & (16)) != 0) goto loc_0086DE75;
loc_0086DC2E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 120)) != 0) goto loc_0086DF76;
loc_0086DC3E:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 66)) & (16)) == 0) goto loc_0086DC83;
    result = (unsigned int)((*(unsigned __int8 *)(a4 - 48 + 26)) & (7));
    a2 = (a4 - 48) - (*(unsigned __int8 *)(result + v_rip - 8838223 * 1 + 15794048));
    if (((*(unsigned __int8 *)(a4 - 48 + 27)) & (64)) == 0) goto loc_0086E0F5;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))))) >> (24));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) + 1);
    result = (unsigned int)((result) & (0xFFFFFFULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(a2 + 8) = a1;
loc_0086DC83:
    a1 = (*(unsigned __int64 *)(a4 - 48 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a4 - 48 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4 - 48 + 16))) & (2)) != 0) goto loc_0086E154;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4 - 48 + 16))) & (2)) != 0) goto loc_0086E154;
loc_0086DCB8:
    result = KeAbPostRelease(a4 - 48 + 16, a2, *(unsigned __int8 *)(a4 - 48 + 27), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))))));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int8 *)(a4 - 48 + 27), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))))));
    if (v_stack_mAC == 0) goto loc_0086DE03;
loc_0086DCDA:
    v_r15 = (unsigned int)((1) + 1);
    if (((unsigned int)(v_r15)) <= (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 56))) goto loc_0086DD68;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 56) = (unsigned int)(v_r15);
    goto loc_0086DD68;
loc_0086DCEF:
    result = *(unsigned __int8 *)(a4 - 48 + 26);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 - 48 + 26))) & (16)) != 0) {
        result = (unsigned int)((*(unsigned __int8 *)(a4 - 48 + 26)) & (31));
        a1 = v_rip - 8838401;
        result = *(unsigned __int8 *)(result + a1 * 1 + 15794048);
        a1 = a4 - 48;
        a1 = (a1) - (result);
    }
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_0086E2AE;
loc_0086DD18:
loc_0086DD1D:
    a1 = (*(unsigned __int64 *)(a4 - 48 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a4 - 48 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4 - 48 + 16))) & (2)) != 0) goto loc_0086DF68;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4 - 48 + 16))) & (2)) != 0) goto loc_0086DF68;
loc_0086DD51:
    result = KeAbPostRelease(a4 - 48 + 16, a2, *(unsigned __int8 *)(a4 - 48 + 27), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))))));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int8 *)(a4 - 48 + 27), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))))));
loc_0086DD68:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int8 *)(a4 - 48 + 27), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12)))))));
    v_rsp = (v_rsp) + (184);
    return result;
loc_0086DD8F:
    a3 = 0;
    a2 = 0;
    result = PspChargeQuota(v_stack_mB8, a2, a3, 0);
    if (!sign_flag) goto loc_0086DBC0;
    if ((unsigned int)(0xC0000022ULL) != 0) {
        a4 = (unsigned int)(0xC0000022ULL);
        a3 = (unsigned int)(v_r15);
        a2 = 0;
        a1 = v_stack_mB8;
        result = PspReturnQuota(a1, a2, a3, a4);
    }
    result = 0;
    *(unsigned __int64 *)(a4 - 48 + 32) = 0;
    goto loc_0086DDD3;
loc_0086DDC4:
    *(unsigned __int64 *)(a4 - 48 + 32) = v_r15;
    goto loc_0086DBD4;
loc_0086DDCD:
    result = 0;
    *(unsigned __int64 *)(a4 - 48 + 32) = 0;
loc_0086DDD3:
    if (v_stack_p68 == 0) goto loc_0086E2BC;
    if (*(unsigned __int64 *)(v_stack_p68 + 16) == 0) goto loc_0086E2BC;
    a3 = 0;
    result = PsReturnSharedPoolQuota(*(unsigned __int64 *)(v_stack_p68 + 16), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))), a3, a4);
    goto loc_0086DD1D;
loc_0086DE03:
    if (((*(unsigned __int8 *)(a4 - 48 + 26)) & ((unsigned __int8)(v_r15))) == 0) goto loc_0086DCDA;
    if (a4 - 48 - 32 == 0) goto loc_0086DCDA;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r15);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 8))) == (*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792))) goto loc_0086E303;
loc_0086DE75:
    result = ObpLockHandleDataBaseEntry(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, result, v_stack_p48, a4);
    if (!sign_flag) goto loc_0086DC2E;
    goto loc_0086DD1D;
loc_0086DE94:
    result = 0;
    v_stack_p44 = 0;
    if ((*(unsigned __int8 *)((unsigned int)(v_stack_mB4))) != ((unsigned __int8)(v_r15))) goto loc_0086E381;
    if (!sign_flag) goto loc_0086E38B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB4) + 8))) == 0) goto loc_0086E162;
    result = ((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB4) + 8))) + ((unsigned int)(v_stack_mB4));
loc_0086DEC3:
    if ((((unsigned __int8)(*(unsigned __int16 *)((unsigned int)(v_stack_mB4) + 2))) & (4)) == 0) goto loc_0086E37A;
    if (!sign_flag) goto loc_0086E3C8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB4) + 16))) == 0) goto loc_0086E394;
    a1 = ((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB4) + 16))) + ((unsigned int)(v_stack_mB4));
loc_0086DEE4:
    if (result != 0) {
        result = *(unsigned __int8 *)(result + 1);
        a2 = result * 4 + 11;
        a2 = (unsigned int)((a2) & (0xFFFFFFFCULL));
        v_stack_p44 = (unsigned int)(a2);
    }
    if (a1 != 0) {
        result = *(unsigned __int16 *)(a1 + 2);
        result = (unsigned int)((result) + (3));
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        a2 = (unsigned int)((a2) + ((unsigned int)(result)));
        v_stack_p44 = (unsigned int)(a2);
    }
    if ((unsigned int)(a2) == 0) goto loc_0086DF5E;
    if (result == (*(unsigned __int64 *)(v_rip + 7703445))) goto loc_0086E229;
    if ((unsigned int)(a2) == 0) goto loc_0086DF48;
    a2 = 0;
    result = PspChargeQuota(*(unsigned __int64 *)(result + 760), a2, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(a2)));
    if (sign_flag) goto loc_0086E2B5;
loc_0086DF48:
    *(unsigned __int64 *)(0 + 16) = *(unsigned __int64 *)(result + 760);
    if (*(unsigned __int64 *)(result + 760) == 0) goto loc_0086E2BC;
loc_0086DF5E:
    *(unsigned int *)(0 + 8) = (unsigned int)((unsigned int)(v_stack_p44));
    goto loc_0086DB7C;
loc_0086DF68:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, (unsigned int)(v_stack_p44), (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(a2)));
    goto loc_0086DD51;
loc_0086DF76:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16))) & (2)) != 0) goto loc_0086E2F5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16))) & (2)) != 0) goto loc_0086E2F5;
loc_0086DFAA:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, a2, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(a2)));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(a2)));
    v_rdi = 0;
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_0086E1C3;
loc_0086DFE2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 120)) != (v_rip + 2577971)) goto loc_0086E169;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = PspProcessOpen((unsigned int)((unsigned int)((unsigned int)(v_stack_p4C))), a5, result, v_stack_p58);
loc_0086E020:
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_p78;
        result = KiUnstackDetachProcess(a1, a2, result, v_stack_p58);
        a1 = 0;
        result = PsDetachSiloFromCurrentThread(a1, a2, result, v_stack_p58);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, a2, a3, v_stack_p58);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_p58);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r15);
    }
    if (!sign_flag) goto loc_0086DC3E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 66)) & (16)) != 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184;
        result = ObpUnlockHandleDatabaseEntry(a1, a2, a3, v_stack_p58);
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16))) & (2)) != 0) goto loc_0086E3BA;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16))) & (2)) != 0) goto loc_0086E3BA;
loc_0086E0D1:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, a2, a3, v_stack_p58);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_p58);
    result = ObpDeleteNameCheck(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, a2, a3, v_stack_p58);
    goto loc_0086DD68;
loc_0086E0F5:
    a2 = 0;
    result = (*(unsigned __int64 *)(a2)) + (8);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) == 0) goto loc_0086E124;
loc_0086E110:
    if ((*(unsigned __int64 *)(result)) == result) goto loc_0086E13F;
loc_0086E11B:
    result = (result) + (16);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) + (-1));
    if (condition_is_not_equal) goto loc_0086E110;
loc_0086E124:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8)) + 1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))));
    *(unsigned int *)(a2 + 8) = (unsigned int)(result);
    goto loc_0086DC83;
loc_0086E13F:
    a2 = result;
    if (0 != 0) { a2 = 0; }
    if ((*(unsigned __int8 *)(result + 11)) < 255) goto loc_0086E124;
    goto loc_0086E11B;
loc_0086E154:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, a2, result, 0);
    goto loc_0086DCB8;
loc_0086E162:
    result = 0;
    goto loc_0086DEC3;
loc_0086E169:
    if (0 != (v_rip + 102512)) goto loc_0086E2C6;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = MiSectionOpen(0, a2, result, 0);
    goto loc_0086E020;
loc_0086E198:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 66)) & (16)) == 0) goto loc_0086DC20;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 120)) != ((unsigned int)((unsigned int)(result)))) goto loc_0086DC20;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 128)) == ((unsigned int)((unsigned int)(result)))) goto loc_0086DC20;
    goto loc_0086DD1D;
loc_0086E1C3:
    if (0 == 3) goto loc_0086DFE2;
    result = PsGetProcessServerSilo(result, a2, result, 0);
    result = PsAttachSiloToCurrentThread(result, a2, result, 0);
    result = KeStackAttachProcess(result, v_stack_p78, result, 0);
    goto loc_0086DFE2;
loc_0086E1FB:
    a1 = (v_stack_p70) ^ (*(unsigned __int8 *)(v_rip + 7703626));
    a1 = (a1) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 24));
    result = 0;
    goto loc_0086DB81;
loc_0086E229:
    *(unsigned __int64 *)(result + 16) = v_r15;
    *(unsigned int *)(result + 8) = (unsigned int)(v_stack_p78);
    goto loc_0086DB7C;
loc_0086E238:
    a1 = (0 != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_stack_p78)) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0086E3DB;
    a3 = (unsigned __int8)((result) & (8));
    if (condition_is_equal) goto loc_0086E25E;
    result = OBJECT_HEADER_TO_PROCESS_INFO(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, v_stack_p78, a3, 0);
    if ((*(unsigned __int64 *)(result)) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + a1 * 8 + 16545792) + 108)))) goto loc_0086E26D;
loc_0086E25E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 8)) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + a1 * 8 + 16545792) + 108)))) goto loc_0086DD18;
    if ((unsigned __int8)(a3) == 0) goto loc_0086E28F;
loc_0086E26D:
    result = OBJECT_HEADER_TO_PROCESS_INFO(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, v_stack_p78, a3, 0);
    if (*(unsigned __int64 *)(result) == 0) goto loc_0086E28F;
    result = 0;
    if ((unsigned __int8)(a3) != 0) { result = *(unsigned __int64 *)(result); }
    if (result != result) goto loc_0086DD18;
loc_0086E28F:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 26)) & (31));
    a1 = (*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184) - (*(unsigned __int8 *)(result + v_rip - 8839834 * 1 + 15794048));
    *(unsigned __int64 *)(a1) = result;
loc_0086E2AE:
    a1 = 0;
    goto loc_0086DC00;
loc_0086E2B5:
    result = 0;
    *(unsigned __int64 *)(result + 16) = 0;
loc_0086E2BC:
    goto loc_0086DD1D;
loc_0086E2C6:
    if (0 != (v_rip + 1711107)) goto loc_0086E39B;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = PspThreadOpen((unsigned int)((unsigned int)((unsigned int)(v_stack_p4C))), v_stack_p78, a3, 0);
    goto loc_0086E020;
loc_0086E2F5:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, v_stack_p78, a3, 0);
    goto loc_0086DFAA;
loc_0086E303:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + a1 * 8 + 16545792) + 104))) = *(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792);
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + a1 * 8 + 16545792) + 104)) + 8) = result;
    *(unsigned __int64 *)(result) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + a1 * 8 + 16545792) + 104));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 8) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + a1 * 8 + 16545792) + 104));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184) - 16;
    if (a1 <= 16) { a2 = result; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184))) & (2)) != 0) goto loc_0086E370;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184))) & (2)) != 0) goto loc_0086E370;
loc_0086E335:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, a2, a3, 0);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184))) & (2)) != 0) goto loc_0086DCDA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) == (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) goto loc_0086DCDA;
    result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, 0);
    goto loc_0086DCDA;
loc_0086E370:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184, a2, a3, 0);
    goto loc_0086E335;
loc_0086E37A:
    a1 = 0;
    goto loc_0086DEE4;
loc_0086E381:
    goto loc_0086DD1D;
loc_0086E38B:
    goto loc_0086DEC3;
loc_0086E394:
    a1 = 0;
    goto loc_0086DEE4;
loc_0086E39B:
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(v_stack_p4C))), a2, a3, 0);
    goto loc_0086E020;
loc_0086E3BA:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_rip - 8837778 + a1 * 8 + 16545792) + 184 + 16, a2, a3, 0);
    goto loc_0086E0D1;
loc_0086E3C8:
    goto loc_0086DEE4;
loc_0086E3D1:
    goto loc_0086DD1D;
loc_0086E3DB:
    goto loc_0086DD1D;
}
```

## 5. (Beta) C Style

```c
int64_t ObpIncrementHandleCountEx(int32_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint8_t Arg5, uint32_t Arg6, int64_t Arg7)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint8_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (184);
    result = (*(uint64_t *)(v_rip + 0x59CD15)) ^ (local_rsp);
    v_stack_m50 = result;
    v_stack_mAC = Arg1;
    v_stack_m80 = v_xmm0;
    v_stack_mA8 = Arg2;
    v_stack_m70 = v_xmm0;
    result = (Arg4 - 48) >> (8);
    v_stack_m88 = (uint8_t)(result);
    Arg1 = ((uint32_t)((uint32_t)((uint8_t)(result)))) ^ (*(uint8_t *)(v_rip + 0x7593D0));
    v_stack_mA0 = Arg4;
    Arg1 = (Arg1) ^ (*(uint8_t *)(arg4 - 0x30 + 0x18));
    v_stack_m60 = v_xmm0;
    Arg1 = 1;
    if (((Arg6) & (0x400ULL)) == 0) { Arg1 = Arg5; }
    v_stack_m98 = Arg1;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg4 - 48 + 16, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg4 - 48 + 16;
        Arg2 = result;
        Arg1 = Arg4 - 48 + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r12 = 0;
    v_stack_mB4 = 0;
    local_rdi = (uint8_t)(((uint8_t)(*(uint8_t *)(arg4 - 0x30 + 0x1B))) & (1));
    v_stack_mB8 = (uint8_t)(local_rdi);
    result = *(uint8_t *)(arg4 - 0x30 + 0x1A);
    if ((((uint8_t)(*(uint8_t *)(arg4 - 0x30 + 0x1A))) & (8)) != 0) {
        result = (uint32_t)((*(uint8_t *)(arg4 - 0x30 + 0x1A)) & (15));
        local_r12 = Arg4 - 48;
        result = *(uint8_t *)(result + v_rip - 0x86DB0E * 1 + 0xF0FF80);
        local_r12 = (local_r12) - (result);
    }
    v_stack_m90 = local_r12;
    if ((uint8_t)(local_rdi) == 0) goto loc_0086DBD9;
    Arg1 = (uint8_t)((*(uint8_t *)(arg4 - 0x30 + 0x1B)) & (254));
    *(uint8_t *)(arg4 - 0x30 + 0x1B) = (uint8_t)(Arg1);
    if (local_r12 == 0) goto loc_0086E1FB;
    if (Arg7 != 0) goto loc_0086DE94;
    if (*(uint64_t *)(arg4 - 0x30 + 0x28) == 0) goto loc_0086DB7C;
    local_r13 = (*(uint64_t *)(arg4 - 0x30 + 0x28)) & (-16);
    if (condition_is_not_equal) goto loc_0086DE94;
loc_0086DB7C:
loc_0086DB81:
    if (Arg3 == (*(uint64_t *)(v_rip + 0x758F28))) goto loc_0086DDC4;
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))) == 0) goto loc_0086DBB7;
    Arg2 = 0;
    result = PspChargeQuota(*(uint64_t *)(Arg3 + 0x2F8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))))));
    if (sign_flag) goto loc_0086DDCD;
loc_0086DBB7:
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x4)))) != 0) goto loc_0086DD8F;
loc_0086DBC0:
    *(uint64_t *)(arg4 - 0x30 + 0x20) = *(uint64_t *)(Arg3 + 0x2F8);
    if (*(uint64_t *)(Arg3 + 0x2F8) == 0) goto loc_0086DDD3;
loc_0086DBD4:
loc_0086DBD9:
    Arg1 = 0;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg4 - 0x30 + 0x1B))) & (8));
    if ((((uint8_t)((uint32_t)(Arg6))) & (32)) != 0) goto loc_0086E238;
    if ((uint8_t)(result) != 0) goto loc_0086DCEF;
loc_0086DC00:
    if (v_stack_m98 == 0) goto loc_0086DC11;
    if (((*(uint8_t *)(arg4 - 0x30 + 0x1B)) & (4)) != 0) goto loc_0086E3D1;
loc_0086DC11:
    if ((*(uint64_t *)(arg4 - 0x30 + 0x8)) != 0) goto loc_0086DC20;
    if ((uint8_t)(v_stack_mB8) == 0) goto loc_0086E198;
loc_0086DC20:
    v_stack_mB0 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x42)) & (16)) != 0) goto loc_0086DE75;
loc_0086DC2E:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x78)) != 0) goto loc_0086DF76;
loc_0086DC3E:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x42)) & (16)) == 0) goto loc_0086DC83;
    result = (uint32_t)((*(uint8_t *)(arg4 - 0x30 + 0x1A)) & (7));
    Arg2 = (Arg4 - 48) - (*(uint8_t *)(result + v_rip - 0x86DC4F * 1 + 0xF0FF80));
    if (((*(uint8_t *)(arg4 - 0x30 + 0x1B)) & (64)) == 0) goto loc_0086E0F5;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8))))) >> (24));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) + 1);
    result = (uint32_t)((result) & (0xFFFFFFULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(Arg2 + 0x8) = Arg1;
loc_0086DC83:
    Arg1 = (*(uint64_t *)(arg4 - 0x30 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg4 - 0x30 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg4 - 0x30 + 0x10))) & (2)) != 0) goto loc_0086E154;
    if ((((uint8_t)(*(uint64_t *)(arg4 - 0x30 + 0x10))) & (2)) != 0) goto loc_0086E154;
loc_0086DCB8:
    result = KeAbPostRelease(Arg4 - 48 + 16, Arg2, *(uint8_t *)(arg4 - 0x30 + 0x1B), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))))));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint8_t *)(arg4 - 0x30 + 0x1B), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))))));
    if (v_stack_mAC == 0) goto loc_0086DE03;
loc_0086DCDA:
    local_r15 = (uint32_t)((1) + 1);
    if (((uint32_t)(local_r15)) <= (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x38))) goto loc_0086DD68;
    *(uint32_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x38) = (uint32_t)(local_r15);
    goto loc_0086DD68;
loc_0086DCEF:
    result = *(uint8_t *)(arg4 - 0x30 + 0x1A);
    if ((((uint8_t)(*(uint8_t *)(arg4 - 0x30 + 0x1A))) & (16)) != 0) {
        result = (uint32_t)((*(uint8_t *)(arg4 - 0x30 + 0x1A)) & (31));
        Arg1 = v_rip - 8838401;
        result = *(uint8_t *)(result + Arg1 * 1 + 0xF0FF80);
        Arg1 = Arg4 - 48;
        Arg1 = (Arg1) - (result);
    }
    if ((*(uint64_t *)(Arg1)) == 0) goto loc_0086E2AE;
loc_0086DD18:
loc_0086DD1D:
    Arg1 = (*(uint64_t *)(arg4 - 0x30 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg4 - 0x30 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg4 - 0x30 + 0x10))) & (2)) != 0) goto loc_0086DF68;
    if ((((uint8_t)(*(uint64_t *)(arg4 - 0x30 + 0x10))) & (2)) != 0) goto loc_0086DF68;
loc_0086DD51:
    result = KeAbPostRelease(Arg4 - 48 + 16, Arg2, *(uint8_t *)(arg4 - 0x30 + 0x1B), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))))));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint8_t *)(arg4 - 0x30 + 0x1B), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))))));
loc_0086DD68:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint8_t *)(arg4 - 0x30 + 0x1B), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12)))))));
    local_rsp = (local_rsp) + (184);
    return result;
loc_0086DD8F:
    Arg3 = 0;
    Arg2 = 0;
    result = PspChargeQuota(v_stack_mB8, Arg2, Arg3, 0);
    if (!sign_flag) goto loc_0086DBC0;
    if ((uint32_t)(0xC0000022ULL) != 0) {
        Arg4 = (uint32_t)(0xC0000022ULL);
        Arg3 = (uint32_t)(local_r15);
        Arg2 = 0;
        Arg1 = v_stack_mB8;
        result = PspReturnQuota(Arg1, Arg2, Arg3, Arg4);
    }
    result = 0;
    *(uint64_t *)(arg4 - 0x30 + 0x20) = 0;
    goto loc_0086DDD3;
loc_0086DDC4:
    *(uint64_t *)(arg4 - 0x30 + 0x20) = local_r15;
    goto loc_0086DBD4;
loc_0086DDCD:
    result = 0;
    *(uint64_t *)(arg4 - 0x30 + 0x20) = 0;
loc_0086DDD3:
    if (v_stack_p68 == 0) goto loc_0086E2BC;
    if (*(uint64_t *)(v_stack_p68 + 0x10) == 0) goto loc_0086E2BC;
    Arg3 = 0;
    result = PsReturnSharedPoolQuota(*(uint64_t *)(v_stack_p68 + 0x10), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))), Arg3, Arg4);
    goto loc_0086DD1D;
loc_0086DE03:
    if (((*(uint8_t *)(arg4 - 0x30 + 0x1A)) & ((uint8_t)(local_r15))) == 0) goto loc_0086DCDA;
    if (Arg4 - 48 - 32 == 0) goto loc_0086DCDA;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184;
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r15);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x8))) == (*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800))) goto loc_0086E303;
loc_0086DE75:
    result = ObpLockHandleDataBaseEntry(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, result, v_stack_p48, Arg4);
    if (!sign_flag) goto loc_0086DC2E;
    goto loc_0086DD1D;
loc_0086DE94:
    result = 0;
    v_stack_p44 = 0;
    if ((*(uint8_t *)((uint32_t)(v_stack_mB4))) != ((uint8_t)(local_r15))) goto loc_0086E381;
    if (!sign_flag) goto loc_0086E38B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB4) + 0x8))) == 0) goto loc_0086E162;
    result = ((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB4) + 0x8))) + ((uint32_t)(v_stack_mB4));
loc_0086DEC3:
    if ((((uint8_t)(*(uint16_t *)((uint32_t)(v_stack_mB4) + 0x2))) & (4)) == 0) goto loc_0086E37A;
    if (!sign_flag) goto loc_0086E3C8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB4) + 0x10))) == 0) goto loc_0086E394;
    Arg1 = ((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB4) + 0x10))) + ((uint32_t)(v_stack_mB4));
loc_0086DEE4:
    if (result != 0) {
        result = *(uint8_t *)(result + 0x1);
        Arg2 = result * 4 + 11;
        Arg2 = (uint32_t)((Arg2) & (0xFFFFFFFCULL));
        v_stack_p44 = (uint32_t)(Arg2);
    }
    if (Arg1 != 0) {
        result = *(uint16_t *)(Arg1 + 0x2);
        result = (uint32_t)((result) + (3));
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
        v_stack_p44 = (uint32_t)(Arg2);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0086DF5E;
    if (result == (*(uint64_t *)(v_rip + 0x758B95))) goto loc_0086E229;
    if ((uint32_t)(Arg2) == 0) goto loc_0086DF48;
    Arg2 = 0;
    result = PspChargeQuota(*(uint64_t *)(result + 0x2F8), Arg2, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(Arg2)));
    if (sign_flag) goto loc_0086E2B5;
loc_0086DF48:
    *(uint64_t *)(0 + 0x10) = *(uint64_t *)(result + 0x2F8);
    if (*(uint64_t *)(result + 0x2F8) == 0) goto loc_0086E2BC;
loc_0086DF5E:
    *(uint32_t *)(0 + 0x8) = (uint32_t)((uint32_t)(v_stack_p44));
    goto loc_0086DB7C;
loc_0086DF68:
    result = ExfReleasePushLock(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, (uint32_t)(v_stack_p44), (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(Arg2)));
    goto loc_0086DD51;
loc_0086DF76:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10))) & (2)) != 0) goto loc_0086E2F5;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10))) & (2)) != 0) goto loc_0086E2F5;
loc_0086DFAA:
    result = KeAbPostRelease(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, Arg2, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(Arg2)));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(Arg2)));
    local_rdi = 0;
    if (result != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_0086E1C3;
loc_0086DFE2:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x78)) != (v_rip + 2577971)) goto loc_0086E169;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = PspProcessOpen((uint32_t)((uint32_t)((uint32_t)(v_stack_p4C))), Arg5, result, v_stack_p58);
loc_0086E020:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p78;
        result = KiUnstackDetachProcess(Arg1, Arg2, result, v_stack_p58);
        Arg1 = 0;
        result = PsDetachSiloFromCurrentThread(Arg1, Arg2, result, v_stack_p58);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, Arg2, Arg3, v_stack_p58);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16;
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_p58);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r15);
    }
    if (!sign_flag) goto loc_0086DC3E;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x42)) & (16)) != 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184;
        result = ObpUnlockHandleDatabaseEntry(Arg1, Arg2, Arg3, v_stack_p58);
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10))) & (2)) != 0) goto loc_0086E3BA;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x10))) & (2)) != 0) goto loc_0086E3BA;
loc_0086E0D1:
    result = KeAbPostRelease(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, Arg2, Arg3, v_stack_p58);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_p58);
    result = ObpDeleteNameCheck(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, Arg2, Arg3, v_stack_p58);
    goto loc_0086DD68;
loc_0086E0F5:
    Arg2 = 0;
    result = (*(uint64_t *)(Arg2)) + (8);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2)))) == 0) goto loc_0086E124;
loc_0086E110:
    if ((*(uint64_t *)(result)) == result) goto loc_0086E13F;
loc_0086E11B:
    result = (result) + (16);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2)))) + (-1));
    if (condition_is_not_equal) goto loc_0086E110;
loc_0086E124:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x8)) + 1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)))));
    *(uint32_t *)(Arg2 + 0x8) = (uint32_t)(result);
    goto loc_0086DC83;
loc_0086E13F:
    Arg2 = result;
    if (0 != 0) { Arg2 = 0; }
    if ((*(uint8_t *)(result + 0xB)) < 255) goto loc_0086E124;
    goto loc_0086E11B;
loc_0086E154:
    result = ExfReleasePushLock(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, Arg2, result, 0);
    goto loc_0086DCB8;
loc_0086E162:
    result = 0;
    goto loc_0086DEC3;
loc_0086E169:
    if (0 != (v_rip + 102512)) goto loc_0086E2C6;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = MiSectionOpen(0, Arg2, result, 0);
    goto loc_0086E020;
loc_0086E198:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x42)) & (16)) == 0) goto loc_0086DC20;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x78)) != ((uint32_t)((uint32_t)(result)))) goto loc_0086DC20;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x80)) == ((uint32_t)((uint32_t)(result)))) goto loc_0086DC20;
    goto loc_0086DD1D;
loc_0086E1C3:
    if (0 == 3) goto loc_0086DFE2;
    result = PsGetProcessServerSilo(result, Arg2, result, 0);
    result = PsAttachSiloToCurrentThread(result, Arg2, result, 0);
    result = KeStackAttachProcess(result, v_stack_p78, result, 0);
    goto loc_0086DFE2;
loc_0086E1FB:
    Arg1 = (v_stack_p70) ^ (*(uint8_t *)(v_rip + 0x758C4A));
    Arg1 = (Arg1) ^ (*(uint8_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x18));
    result = 0;
    goto loc_0086DB81;
loc_0086E229:
    *(uint64_t *)(result + 0x10) = local_r15;
    *(uint32_t *)(result + 0x8) = (uint32_t)(v_stack_p78);
    goto loc_0086DB7C;
loc_0086E238:
    Arg1 = (0 != 0) ? 1 : 0;
    result = ((((uint8_t)(v_stack_p78)) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0086E3DB;
    Arg3 = (uint8_t)((result) & (8));
    if (condition_is_equal) goto loc_0086E25E;
    result = OBJECT_HEADER_TO_PROCESS_INFO(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, v_stack_p78, Arg3, 0);
    if ((*(uint64_t *)(result)) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + Arg1 * 8 + 0xFC7800) + 0x6C)))) goto loc_0086E26D;
loc_0086E25E:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x8)) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + Arg1 * 8 + 0xFC7800) + 0x6C)))) goto loc_0086DD18;
    if ((uint8_t)(Arg3) == 0) goto loc_0086E28F;
loc_0086E26D:
    result = OBJECT_HEADER_TO_PROCESS_INFO(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, v_stack_p78, Arg3, 0);
    if (*(uint64_t *)(result) == 0) goto loc_0086E28F;
    result = 0;
    if ((uint8_t)(Arg3) != 0) { result = *(uint64_t *)(result); }
    if (result != result) goto loc_0086DD18;
loc_0086E28F:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8 + 0x1A)) & (31));
    Arg1 = (*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184) - (*(uint8_t *)(result + v_rip - 0x86E29A * 1 + 0xF0FF80));
    *(uint64_t *)(Arg1) = result;
loc_0086E2AE:
    Arg1 = 0;
    goto loc_0086DC00;
loc_0086E2B5:
    result = 0;
    *(uint64_t *)(result + 0x10) = 0;
loc_0086E2BC:
    goto loc_0086DD1D;
loc_0086E2C6:
    if (0 != (v_rip + 1711107)) goto loc_0086E39B;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = PspThreadOpen((uint32_t)((uint32_t)((uint32_t)(v_stack_p4C))), v_stack_p78, Arg3, 0);
    goto loc_0086E020;
loc_0086E2F5:
    result = ExfReleasePushLock(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, v_stack_p78, Arg3, 0);
    goto loc_0086DFAA;
loc_0086E303:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + Arg1 * 8 + 0xFC7800) + 0x68))) = *(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800);
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + Arg1 * 8 + 0xFC7800) + 0x68)) + 0x8) = result;
    *(uint64_t *)(result) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + Arg1 * 8 + 0xFC7800) + 0x68));
    *(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0x8) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + Arg1 * 8 + 0xFC7800) + 0x68));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8) - 16;
    if (Arg1 <= 16) { Arg2 = result; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8))) & (2)) != 0) goto loc_0086E370;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8))) & (2)) != 0) goto loc_0086E370;
loc_0086E335:
    result = KeAbPostRelease(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, Arg2, Arg3, 0);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 0xB8))) & (2)) != 0) goto loc_0086DCDA;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) == (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) goto loc_0086DCDA;
    result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, 0);
    goto loc_0086DCDA;
loc_0086E370:
    result = ExfReleasePushLock(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184, Arg2, Arg3, 0);
    goto loc_0086E335;
loc_0086E37A:
    Arg1 = 0;
    goto loc_0086DEE4;
loc_0086E381:
    goto loc_0086DD1D;
loc_0086E38B:
    goto loc_0086DEC3;
loc_0086E394:
    Arg1 = 0;
    goto loc_0086DEE4;
loc_0086E39B:
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p48));
    v_stack_p20 = v_stack_p50;
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(v_stack_p4C))), Arg2, Arg3, 0);
    goto loc_0086E020;
loc_0086E3BA:
    result = ExfReleasePushLock(*(uint64_t *)(v_rip - 0x86DA92 + Arg1 * 8 + 0xFC7800) + 184 + 16, Arg2, Arg3, 0);
    goto loc_0086E0D1;
loc_0086E3C8:
    goto loc_0086DEE4;
loc_0086E3D1:
    goto loc_0086DD1D;
loc_0086E3DB:
    goto loc_0086DD1D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `- 0x30` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R/W` |
| `Arg4` | `+ 0x18` | `8` | `R` |
| `Arg4` | `+ 0x1A` | `8` | `R` |
| `Arg4` | `+ 0x1B` | `8` | `R` |
| `Arg4` | `+ 0x1B` | `8` | `W` |
| `Arg4` | `+ 0x20` | `64` | `W` |
| `Arg4` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086DA10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
