# MiLogHotPatchRundown

- RVA: `0x008057A4`–`0x008062FA` (길이 `2,902` bytes)
- VA: `0x00000001408057A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BF04`
- 디코드: `623`개 명령, `2,902/2,902` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x00805835` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00805859` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0080589C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00805939` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x008059CE` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00805A90` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x00805B2A` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00805B32` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00805B4F` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00805B54` → [MmAcquireLoadLock](../../text/4D/MmAcquireLoadLock_function_004DC2A0.md) (function, `0x004DC2A0`)
- `0x00805B92` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00805C67` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x00805CC4` → [MiIsActiveSystemHotPatch](MiIsActiveSystemHotPatch_function_008045D8.md) (function, `0x008045D8`)
- `0x00805CD4` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x00805CFC` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00805DF8` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x00805E0C` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (function, `0x004D36D0`)
- `0x00805E13` → [PsGetNextProcess](../91/PsGetNextProcess_function_0091C900.md) (function, `0x0091C900`)
- `0x00805E27` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00805E3D` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00805E5F` → [VslQueryActiveSecurePatches](../../text/58/VslQueryActiveSecurePatches_function_0058ED14.md) (function, `0x0058ED14`)
- `0x00805EA8` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00805EB8` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x00805EE7` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00806025` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x00806048` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00806057` → [MiGetProcessHotPatchContext](MiGetProcessHotPatchContext_function_00803948.md) (function, `0x00803948`)
- `0x00806077` → [MiFillLogProcessInfo](../../text/44/MiFillLogProcessInfo_function_00448110.md) (function, `0x00448110`)
- `0x00806091` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008060B0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008060E4` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x008060F4` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x0080611D` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00806246` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x0080626D` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00806275` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00806297` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x008062A2` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008062AA` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008062B2` → [PsGetNextProcess](../91/PsGetNextProcess_function_0091C900.md) (function, `0x0091C900`)
- `0x008062D3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiTracingEnabledCallback](../AB/MiTracingEnabledCallback_function_00AB6510.md) at `0x00AB6528`

### Static image references
- `0x008057CA` → RVA `0x00E0A740` (`.data`; read)
- `0x008057E1` → RVA `0x00E37618` (`.data`; read)
- `0x00805803` → RVA `0x00E375AC` (`.data`; read)
- `0x0080581D` → RVA `0x00E37590` (`.data`; read)
- `0x00805867` → RVA `0x00E37578` (`.data`; read)
- `0x008058AC` → RVA `0x0005900B` (`.rdata`; read)
- `0x00805980` → RVA `0x00E37570` (`.data`; read)
- `0x008059DE` → RVA `0x0005905E` (`.rdata`; read)
- `0x00805B59` → RVA `0x00E37588` (`.data`; read)
- `0x00805BA2` → RVA `0x00058EE8` (`.rdata`; read)
- `0x00805CAE` → RVA `0x00EF54C0` (`.data`; read)
- `0x00805D0D` → RVA `0x00058F7E` (`.rdata`; read)
- `0x00805FE3` → RVA `0x00059160` (`.rdata`; read)
- `0x00806130` → RVA `0x00059233` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **37**
  - `0x00805835` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00805859` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0080589C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00805939` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x008059CE` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00805A90` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x00805B2A` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00805B32` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00805B4F` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00805B54` → [MmAcquireLoadLock](../../text/4D/MmAcquireLoadLock_function_004DC2A0.md) (`PAGE` → `.text`)
  - `0x00805B92` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00805C67` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x00805CD4` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x00805CFC` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00805DF8` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x00805E0C` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (`PAGE` → `.text`)
  - `0x00805E27` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00805E3D` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00805E5F` → [VslQueryActiveSecurePatches](../../text/58/VslQueryActiveSecurePatches_function_0058ED14.md) (`PAGE` → `.text`)
  - `0x00805EA8` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00805EB8` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x00805EE7` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00806025` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x00806048` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00806077` → [MiFillLogProcessInfo](../../text/44/MiFillLogProcessInfo_function_00448110.md) (`PAGE` → `.text`)
  - `0x00806091` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008060B0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008060E4` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x008060F4` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x0080611D` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00806246` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x0080626D` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00806275` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00806297` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x008062A2` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008062AA` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008062D3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008057A4  48 8B C4                        mov rax, rsp
008057A7  48 89 58 08                     mov qword ptr [rax + 8], rbx
008057AB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
008057AF  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
008057B3  55                              push rbp
008057B4  41 54                           push r12
008057B6  41 55                           push r13
008057B8  41 56                           push r14
008057BA  41 57                           push r15
008057BC  48 8D A8 28 FC FF FF            lea rbp, [rax - 0x3d8]
008057C3  48 81 EC B0 04 00 00            sub rsp, 0x4b0
008057CA  48 8B 05 6F 4F 60 00            mov rax, qword ptr [rip + 0x604f6f]
008057D1  48 33 C4                        xor rax, rsp
008057D4  48 89 85 A0 03 00 00            mov qword ptr [rbp + 0x3a0], rax
008057DB  45 33 ED                        xor r13d, r13d
008057DE  0F 57 C0                        xorps xmm0, xmm0
008057E1  4C 39 2D 30 1E 63 00            cmp qword ptr [rip + 0x631e30], r13
008057E8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
008057EC  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
008057F1  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
008057F5  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
008057F9  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
008057FD  0F 84 C6 0A 00 00               je 0x1408062c9
00805803  44 39 2D A2 1D 63 00            cmp dword ptr [rip + 0x631da2], r13d
0080580A  0F 84 B9 0A 00 00               je 0x1408062c9
00805810  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
00805819  45 8D 75 01                     lea r14d, [r13 + 1]
0080581D  4C 8D 25 6C 1D 63 00            lea r12, [rip + 0x631d6c]
00805824  45 33 C0                        xor r8d, r8d
00805827  33 D2                           xor edx, edx
00805829  49 8B CC                        mov rcx, r12
0080582C  66 45 29 B7 E6 01 00 00         sub word ptr [r15 + 0x1e6], r14w
00805834  90                              nop
00805835  E8 F6 A9 A0 FF                  call 0x140210230
0080583A  48 8B D8                        mov rbx, rax
0080583D  41 8D 4D 11                     lea ecx, [r13 + 0x11]
00805841  33 C0                           xor eax, eax
00805843  F0 48 0F B1 0D 44 1D 63 00      lock cmpxchg qword ptr [rip + 0x631d44], rcx
0080584C  74 10                           je 0x14080585e
0080584E  4D 8B CC                        mov r9, r12
00805851  4C 8B C3                        mov r8, rbx
00805854  33 D2                           xor edx, edx
00805856  49 8B CC                        mov rcx, r12
00805859  E8 EE AB A0 FF                  call 0x14021044c
0080585E  48 85 DB                        test rbx, rbx
00805861  74 04                           je 0x140805867
00805863  44 88 73 0A                     mov byte ptr [rbx + 0xa], r14b
00805867  48 8B 05 0A 1D 63 00            mov rax, qword ptr [rip + 0x631d0a]
0080586E  49 8B DD                        mov rbx, r13
00805871  EB 06                           jmp 0x140805879
00805873  48 8B D8                        mov rbx, rax
00805876  48 8B 00                        mov rax, qword ptr [rax]
00805879  48 85 C0                        test rax, rax
0080587C  75 F5                           jne 0x140805873
0080587E  E9 F4 00 00 00                  jmp 0x140805977
00805883  4C 8B 05 8E 1D 63 00            mov r8, qword ptr [rip + 0x631d8e]
0080588A  41 83 38 05                     cmp dword ptr [r8], 5
0080588E  0F 86 AA 00 00 00               jbe 0x14080593e
00805894  BA 20 00 00 00                  mov edx, 0x20
00805899  49 8B C8                        mov rcx, r8
0080589C  E8 FF 91 C2 FF                  call 0x14042eaa0
008058A1  84 C0                           test al, al
008058A3  0F 84 95 00 00 00               je 0x14080593e
008058A9  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
008058AC  48 8D 15 58 37 85 FF            lea rdx, [rip - 0x7ac8a8]
008058B3  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
008058B6  45 8B CE                        mov r9d, r14d
008058B9  48 8D 45 C4                     lea rax, [rbp - 0x3c]
008058BD  48 C7 85 68 03 00 00 04 00 00 00  mov qword ptr [rbp + 0x368], 4
008058C8  48 89 85 60 03 00 00            mov qword ptr [rbp + 0x360], rax
008058CF  49 8B C8                        mov rcx, r8
008058D2  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008058D5  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008058D9  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008058DE  48 89 85 70 03 00 00            mov qword ptr [rbp + 0x370], rax
008058E5  48 8D 85 98 03 00 00            lea rax, [rbp + 0x398]
008058EC  48 89 85 80 03 00 00            mov qword ptr [rbp + 0x380], rax
008058F3  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008058F7  48 89 85 90 03 00 00            mov qword ptr [rbp + 0x390], rax
008058FE  0F B7 43 28                     movzx eax, word ptr [rbx + 0x28]
00805902  89 85 98 03 00 00               mov dword ptr [rbp + 0x398], eax
00805908  48 8D 85 40 03 00 00            lea rax, [rbp + 0x340]
0080590F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00805914  C7 44 24 30 06 00 00 00         mov dword ptr [rsp + 0x30], 6
0080591C  48 C7 85 78 03 00 00 04 00 00 00  mov qword ptr [rbp + 0x378], 4
00805927  48 C7 85 88 03 00 00 02 00 00 00  mov qword ptr [rbp + 0x388], 2
00805932  44 89 AD 9C 03 00 00            mov dword ptr [rbp + 0x39c], r13d
00805939  E8 0A 4A CA FF                  call 0x1404aa348
0080593E  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00805942  48 8B CB                        mov rcx, rbx
00805945  48 85 C0                        test rax, rax
00805948  74 23                           je 0x14080596d
0080594A  48 8B 08                        mov rcx, qword ptr [rax]
0080594D  48 8B D8                        mov rbx, rax
00805950  48 85 C9                        test rcx, rcx
00805953  74 22                           je 0x140805977
00805955  48 8B 01                        mov rax, qword ptr [rcx]
00805958  48 8B D9                        mov rbx, rcx
0080595B  48 8B C8                        mov rcx, rax
0080595E  48 85 C0                        test rax, rax
00805961  75 F2                           jne 0x140805955
00805963  EB 12                           jmp 0x140805977
00805965  48 39 0B                        cmp qword ptr [rbx], rcx
00805968  74 0D                           je 0x140805977
0080596A  48 8B CB                        mov rcx, rbx
0080596D  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00805971  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00805975  75 EE                           jne 0x140805965
00805977  48 85 DB                        test rbx, rbx
0080597A  0F 85 03 FF FF FF               jne 0x140805883
00805980  48 8B 05 E9 1B 63 00            mov rax, qword ptr [rip + 0x631be9]
00805987  49 8B FD                        mov rdi, r13
0080598A  EB 06                           jmp 0x140805992
0080598C  48 8B F8                        mov rdi, rax
0080598F  48 8B 00                        mov rax, qword ptr [rax]
00805992  48 85 C0                        test rax, rax
00805995  75 F5                           jne 0x14080598c
00805997  E9 74 01 00 00                  jmp 0x140805b10
0080599C  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008059A0  49 8B DD                        mov rbx, r13
008059A3  EB 06                           jmp 0x1408059ab
008059A5  48 8B D8                        mov rbx, rax
008059A8  48 8B 00                        mov rax, qword ptr [rax]
008059AB  48 85 C0                        test rax, rax
008059AE  75 F5                           jne 0x1408059a5
008059B0  E9 19 01 00 00                  jmp 0x140805ace
008059B5  4C 8B 05 5C 1C 63 00            mov r8, qword ptr [rip + 0x631c5c]
008059BC  41 83 38 05                     cmp dword ptr [r8], 5
008059C0  0F 86 CF 00 00 00               jbe 0x140805a95
008059C6  BA 20 00 00 00                  mov edx, 0x20
008059CB  49 8B C8                        mov rcx, r8
008059CE  E8 CD 90 C2 FF                  call 0x14042eaa0
008059D3  84 C0                           test al, al
008059D5  0F 84 BA 00 00 00               je 0x140805a95
008059DB  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
008059DE  48 8D 15 79 36 85 FF            lea rdx, [rip - 0x7ac987]
008059E5  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
008059E9  45 8B CE                        mov r9d, r14d
008059EC  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
008059F1  48 C7 85 F8 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x2f8], 4
008059FC  48 89 85 F0 02 00 00            mov qword ptr [rbp + 0x2f0], rax
00805A03  49 8B C8                        mov rcx, r8
00805A06  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00805A09  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00805A0D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00805A12  48 89 85 00 03 00 00            mov qword ptr [rbp + 0x300], rax
00805A19  48 8D 85 28 03 00 00            lea rax, [rbp + 0x328]
00805A20  48 89 85 10 03 00 00            mov qword ptr [rbp + 0x310], rax
00805A27  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00805A2B  48 89 85 20 03 00 00            mov qword ptr [rbp + 0x320], rax
00805A32  0F B7 43 28                     movzx eax, word ptr [rbx + 0x28]
00805A36  89 85 28 03 00 00               mov dword ptr [rbp + 0x328], eax
00805A3C  48 8D 47 28                     lea rax, [rdi + 0x28]
00805A40  48 89 85 30 03 00 00            mov qword ptr [rbp + 0x330], rax
00805A47  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
00805A4B  48 C7 85 08 03 00 00 04 00 00 00  mov qword ptr [rbp + 0x308], 4
00805A56  48 C7 85 18 03 00 00 02 00 00 00  mov qword ptr [rbp + 0x318], 2
00805A61  44 89 AD 2C 03 00 00            mov dword ptr [rbp + 0x32c], r13d
00805A68  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
00805A6F  44 89 AD 3C 03 00 00            mov dword ptr [rbp + 0x33c], r13d
00805A76  89 85 38 03 00 00               mov dword ptr [rbp + 0x338], eax
00805A7C  48 8D 85 D0 02 00 00            lea rax, [rbp + 0x2d0]
00805A83  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00805A88  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00805A90  E8 B3 48 CA FF                  call 0x1404aa348
00805A95  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00805A99  48 8B CB                        mov rcx, rbx
00805A9C  48 85 C0                        test rax, rax
00805A9F  74 23                           je 0x140805ac4
00805AA1  48 8B 08                        mov rcx, qword ptr [rax]
00805AA4  48 8B D8                        mov rbx, rax
00805AA7  48 85 C9                        test rcx, rcx
00805AAA  74 22                           je 0x140805ace
00805AAC  48 8B 01                        mov rax, qword ptr [rcx]
00805AAF  48 8B D9                        mov rbx, rcx
00805AB2  48 8B C8                        mov rcx, rax
00805AB5  48 85 C0                        test rax, rax
00805AB8  75 F2                           jne 0x140805aac
00805ABA  EB 12                           jmp 0x140805ace
00805ABC  48 39 0B                        cmp qword ptr [rbx], rcx
00805ABF  74 0D                           je 0x140805ace
00805AC1  48 8B CB                        mov rcx, rbx
00805AC4  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00805AC8  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00805ACC  75 EE                           jne 0x140805abc
00805ACE  48 85 DB                        test rbx, rbx
00805AD1  0F 85 DE FE FF FF               jne 0x1408059b5
00805AD7  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00805ADB  48 8B CF                        mov rcx, rdi
00805ADE  48 85 C0                        test rax, rax
00805AE1  74 23                           je 0x140805b06
00805AE3  48 8B 08                        mov rcx, qword ptr [rax]
00805AE6  48 8B F8                        mov rdi, rax
00805AE9  48 85 C9                        test rcx, rcx
00805AEC  74 22                           je 0x140805b10
00805AEE  48 8B 01                        mov rax, qword ptr [rcx]
00805AF1  48 8B F9                        mov rdi, rcx
00805AF4  48 8B C8                        mov rcx, rax
00805AF7  48 85 C0                        test rax, rax
00805AFA  75 F2                           jne 0x140805aee
00805AFC  EB 12                           jmp 0x140805b10
00805AFE  48 39 0F                        cmp qword ptr [rdi], rcx
00805B01  74 0D                           je 0x140805b10
00805B03  48 8B CF                        mov rcx, rdi
00805B06  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
00805B0A  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
00805B0E  75 EE                           jne 0x140805afe
00805B10  48 85 FF                        test rdi, rdi
00805B13  0F 85 83 FE FF FF               jne 0x14080599c
00805B19  8D 47 11                        lea eax, [rdi + 0x11]
00805B1C  F0 4C 0F B1 2D 6B 1A 63 00      lock cmpxchg qword ptr [rip + 0x631a6b], r13
00805B25  74 08                           je 0x140805b2f
00805B27  49 8B CC                        mov rcx, r12
00805B2A  E8 11 D9 A5 FF                  call 0x140263440
00805B2F  49 8B CC                        mov rcx, r12
00805B32  E8 C9 BA AD FF                  call 0x1402e1600
00805B37  90                              nop
00805B38  66 45 01 B7 E6 01 00 00         add word ptr [r15 + 0x1e6], r14w
00805B40  75 12                           jne 0x140805b54
00805B42  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
00805B49  90                              nop
00805B4A  48 39 00                        cmp qword ptr [rax], rax
00805B4D  74 05                           je 0x140805b54
00805B4F  E8 2C D1 AD FF                  call 0x1402e2c80
00805B54  E8 47 67 CD FF                  call 0x1404dc2a0
00805B59  48 8B 05 28 1A 63 00            mov rax, qword ptr [rip + 0x631a28]
00805B60  49 8B DD                        mov rbx, r13
00805B63  EB 06                           jmp 0x140805b6b
00805B65  48 8B D8                        mov rbx, rax
00805B68  48 8B 00                        mov rax, qword ptr [rax]
00805B6B  48 85 C0                        test rax, rax
00805B6E  75 F5                           jne 0x140805b65
00805B70  44 8D 60 09                     lea r12d, [rax + 9]
00805B74  E9 2C 01 00 00                  jmp 0x140805ca5
00805B79  4C 8B 05 98 1A 63 00            mov r8, qword ptr [rip + 0x631a98]
00805B80  41 83 38 05                     cmp dword ptr [r8], 5
00805B84  0F 86 E2 00 00 00               jbe 0x140805c6c
00805B8A  BA 20 00 00 00                  mov edx, 0x20
00805B8F  49 8B C8                        mov rcx, r8
00805B92  E8 09 8F C2 FF                  call 0x14042eaa0
00805B97  84 C0                           test al, al
00805B99  0F 84 CD 00 00 00               je 0x140805c6c
00805B9F  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00805BA2  48 8D 15 3F 33 85 FF            lea rdx, [rip - 0x7accc1]
00805BA9  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00805BAD  45 8B CE                        mov r9d, r14d
00805BB0  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00805BB5  48 C7 45 38 04 00 00 00         mov qword ptr [rbp + 0x38], 4
00805BBD  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00805BC1  49 8B C8                        mov rcx, r8
00805BC4  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00805BC7  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00805BCB  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00805BD0  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00805BD4  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00805BD7  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00805BDB  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00805BE0  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00805BE4  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00805BE7  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00805BEB  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00805BF0  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00805BF4  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
00805BF7  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00805BFB  48 8D 44 24 74                  lea rax, [rsp + 0x74]
00805C00  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00805C04  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00805C0B  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00805C12  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
00805C16  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00805C1D  0F B7 43 30                     movzx eax, word ptr [rbx + 0x30]
00805C21  89 85 98 00 00 00               mov dword ptr [rbp + 0x98], eax
00805C27  48 8D 45 10                     lea rax, [rbp + 0x10]
00805C2B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00805C30  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00805C35  48 C7 45 48 04 00 00 00         mov qword ptr [rbp + 0x48], 4
00805C3D  48 C7 45 58 04 00 00 00         mov qword ptr [rbp + 0x58], 4
00805C45  48 C7 45 68 04 00 00 00         mov qword ptr [rbp + 0x68], 4
00805C4D  48 C7 45 78 04 00 00 00         mov qword ptr [rbp + 0x78], 4
00805C55  48 C7 85 88 00 00 00 02 00 00 00  mov qword ptr [rbp + 0x88], 2
00805C60  44 89 AD 9C 00 00 00            mov dword ptr [rbp + 0x9c], r13d
00805C67  E8 DC 46 CA FF                  call 0x1404aa348
00805C6C  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00805C70  48 8B CB                        mov rcx, rbx
00805C73  48 85 C0                        test rax, rax
00805C76  74 23                           je 0x140805c9b
00805C78  48 8B 08                        mov rcx, qword ptr [rax]
00805C7B  48 8B D8                        mov rbx, rax
00805C7E  48 85 C9                        test rcx, rcx
00805C81  74 22                           je 0x140805ca5
00805C83  48 8B 01                        mov rax, qword ptr [rcx]
00805C86  48 8B D9                        mov rbx, rcx
00805C89  48 8B C8                        mov rcx, rax
00805C8C  48 85 C0                        test rax, rax
00805C8F  75 F2                           jne 0x140805c83
00805C91  EB 12                           jmp 0x140805ca5
00805C93  48 39 0B                        cmp qword ptr [rbx], rcx
00805C96  74 0D                           je 0x140805ca5
00805C98  48 8B CB                        mov rcx, rbx
00805C9B  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00805C9F  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00805CA3  75 EE                           jne 0x140805c93
00805CA5  48 85 DB                        test rbx, rbx
00805CA8  0F 85 CB FE FF FF               jne 0x140805b79
00805CAE  48 8B 1D 0B F8 6E 00            mov rbx, qword ptr [rip + 0x6ef80b]
00805CB5  48 8D 3D 04 F8 6E 00            lea rdi, [rip + 0x6ef804]
00805CBC  E9 3F 01 00 00                  jmp 0x140805e00
00805CC1  48 8B CB                        mov rcx, rbx
00805CC4  E8 0F E9 FF FF                  call 0x1408045d8
00805CC9  85 C0                           test eax, eax
00805CCB  0F 84 2C 01 00 00               je 0x140805dfd
00805CD1  48 8B CB                        mov rcx, rbx
00805CD4  E8 5B 40 CD FF                  call 0x1404d9d34
00805CD9  4C 8B 05 38 19 63 00            mov r8, qword ptr [rip + 0x631938]
00805CE0  4C 8B C8                        mov r9, rax
00805CE3  4C 8B 90 F8 00 00 00            mov r10, qword ptr [rax + 0xf8]
00805CEA  41 83 38 05                     cmp dword ptr [r8], 5
00805CEE  0F 86 09 01 00 00               jbe 0x140805dfd
00805CF4  BA 20 00 00 00                  mov edx, 0x20
00805CF9  49 8B C8                        mov rcx, r8
00805CFC  E8 9F 8D C2 FF                  call 0x14042eaa0
00805D01  84 C0                           test al, al
00805D03  0F 84 F4 00 00 00               je 0x140805dfd
00805D09  41 8B 42 78                     mov eax, dword ptr [r10 + 0x78]
00805D0D  48 8D 15 6A 32 85 FF            lea rdx, [rip - 0x7acd96]
00805D14  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00805D18  49 8B C8                        mov rcx, r8
00805D1B  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00805D20  48 C7 85 C8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xc8], 4
00805D2B  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00805D32  41 8B 82 9C 00 00 00            mov eax, dword ptr [r10 + 0x9c]
00805D39  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00805D3D  48 8D 44 24 7C                  lea rax, [rsp + 0x7c]
00805D42  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00805D49  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
00805D4C  89 45 80                        mov dword ptr [rbp - 0x80], eax
00805D4F  48 8D 45 80                     lea rax, [rbp - 0x80]
00805D53  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00805D5A  8B 83 9C 00 00 00               mov eax, dword ptr [rbx + 0x9c]
00805D60  89 45 84                        mov dword ptr [rbp - 0x7c], eax
00805D63  48 8D 45 84                     lea rax, [rbp - 0x7c]
00805D67  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00805D6E  41 8B 81 10 01 00 00            mov eax, dword ptr [r9 + 0x110]
00805D75  45 8B CE                        mov r9d, r14d
00805D78  89 45 88                        mov dword ptr [rbp - 0x78], eax
00805D7B  48 8D 45 88                     lea rax, [rbp - 0x78]
00805D7F  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00805D86  48 8D 85 28 01 00 00            lea rax, [rbp + 0x128]
00805D8D  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00805D94  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
00805D98  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00805D9F  0F B7 43 48                     movzx eax, word ptr [rbx + 0x48]
00805DA3  89 85 28 01 00 00               mov dword ptr [rbp + 0x128], eax
00805DA9  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00805DB0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00805DB5  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00805DBA  48 C7 85 D8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xd8], 4
00805DC5  48 C7 85 E8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xe8], 4
00805DD0  48 C7 85 F8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xf8], 4
00805DDB  48 C7 85 08 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x108], 4
00805DE6  48 C7 85 18 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x118], 2
00805DF1  44 89 AD 2C 01 00 00            mov dword ptr [rbp + 0x12c], r13d
00805DF8  E8 4B 45 CA FF                  call 0x1404aa348
00805DFD  48 8B 1B                        mov rbx, qword ptr [rbx]
00805E00  48 3B DF                        cmp rbx, rdi
00805E03  0F 85 B8 FE FF FF               jne 0x140805cc1
00805E09  49 8B CF                        mov rcx, r15
00805E0C  E8 BF D8 CC FF                  call 0x1404d36d0
00805E11  33 C9                           xor ecx, ecx
00805E13  E8 E8 6A 11 00                  call 0x14091c900
00805E18  E9 A0 04 00 00                  jmp 0x1408062bd
00805E1D  4C 8D A3 E8 01 00 00            lea r12, [rbx + 0x1e8]
00805E24  49 8B CC                        mov rcx, r12
00805E27  E8 F4 07 A1 FF                  call 0x140216620
00805E2C  84 C0                           test al, al
00805E2E  0F 84 7B 04 00 00               je 0x1408062af
00805E34  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00805E38  33 D2                           xor edx, edx
00805E3A  48 8B CB                        mov rcx, rbx
00805E3D  E8 DE 09 A1 FF                  call 0x140216820
00805E42  48 8B 8B 70 01 00 00            mov rcx, qword ptr [rbx + 0x170]
00805E49  41 84 CE                        test r14b, cl
00805E4C  0F 84 00 02 00 00               je 0x140806052
00805E52  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00805E57  4C 89 6D C8                     mov qword ptr [rbp - 0x38], r13
00805E5B  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00805E5F  E8 B0 8E D8 FF                  call 0x14058ed14
00805E64  85 C0                           test eax, eax
00805E66  0F 88 30 04 00 00               js 0x14080629c
00805E6C  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00805E70  85 C0                           test eax, eax
00805E72  0F 84 24 04 00 00               je 0x14080629c
00805E78  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
00805E7C  49 8B F5                        mov rsi, r13
00805E7F  49 8B FD                        mov rdi, r13
00805E82  44 8B E8                        mov r13d, eax
00805E85  4C 8B 25 8C 17 63 00            mov r12, qword ptr [rip + 0x63178c]
00805E8C  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00805E90  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00805E95  41 83 3C 24 05                  cmp dword ptr [r12], 5
00805E9A  0F 86 8A 01 00 00               jbe 0x14080602a
00805EA0  BA 20 00 00 00                  mov edx, 0x20
00805EA5  49 8B CC                        mov rcx, r12
00805EA8  E8 F3 8B C2 FF                  call 0x14042eaa0
00805EAD  84 C0                           test al, al
00805EAF  0F 84 75 01 00 00               je 0x14080602a
00805EB5  48 8B CB                        mov rcx, rbx
00805EB8  E8 53 7A C3 FF                  call 0x14043d910
00805EBD  89 45 8C                        mov dword ptr [rbp - 0x74], eax
00805EC0  48 8D 93 38 03 00 00            lea rdx, [rbx + 0x338]
00805EC7  48 8D 45 8C                     lea rax, [rbp - 0x74]
00805ECB  48 C7 85 28 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x228], 4
00805ED6  48 8D 8D 30 02 00 00            lea rcx, [rbp + 0x230]
00805EDD  48 89 85 20 02 00 00            mov qword ptr [rbp + 0x220], rax
00805EE4  45 33 C9                        xor r9d, r9d
00805EE7  E8 18 14 C2 FF                  call 0x140427304
00805EEC  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00805EF1  48 8D 45 90                     lea rax, [rbp - 0x70]
00805EF5  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
00805EFC  48 C7 85 48 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x248], 4
00805F07  48 C7 85 58 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x258], 4
00805F12  42 8B 44 07 04                  mov eax, dword ptr [rdi + r8 + 4]
00805F17  42 8B 0C 07                     mov ecx, dword ptr [rdi + r8]
00805F1B  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00805F1E  48 8D 45 94                     lea rax, [rbp - 0x6c]
00805F22  48 89 85 50 02 00 00            mov qword ptr [rbp + 0x250], rax
00805F29  42 8B 44 07 0C                  mov eax, dword ptr [rdi + r8 + 0xc]
00805F2E  89 45 98                        mov dword ptr [rbp - 0x68], eax
00805F31  48 8D 45 98                     lea rax, [rbp - 0x68]
00805F35  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00805F3C  42 8B 44 07 10                  mov eax, dword ptr [rdi + r8 + 0x10]
00805F41  89 45 9C                        mov dword ptr [rbp - 0x64], eax
00805F44  48 8D 45 9C                     lea rax, [rbp - 0x64]
00805F48  48 89 85 70 02 00 00            mov qword ptr [rbp + 0x270], rax
00805F4F  42 8B 44 07 18                  mov eax, dword ptr [rdi + r8 + 0x18]
00805F54  89 45 A0                        mov dword ptr [rbp - 0x60], eax
00805F57  48 8D 45 A0                     lea rax, [rbp - 0x60]
00805F5B  48 89 85 80 02 00 00            mov qword ptr [rbp + 0x280], rax
00805F62  89 4D 90                        mov dword ptr [rbp - 0x70], ecx
00805F65  48 C7 85 68 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x268], 4
00805F70  48 C7 85 78 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x278], 4
00805F7B  48 C7 85 88 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x288], 4
00805F86  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00805F8A  0F B7 14 06                     movzx edx, word ptr [rsi + rax]
00805F8E  48 8B 4C 06 08                  mov rcx, qword ptr [rsi + rax + 8]
00805F93  48 8D 85 A8 02 00 00            lea rax, [rbp + 0x2a8]
00805F9A  48 89 85 90 02 00 00            mov qword ptr [rbp + 0x290], rax
00805FA1  42 8B 44 07 08                  mov eax, dword ptr [rdi + r8 + 8]
00805FA6  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00805FA9  48 8D 45 A4                     lea rax, [rbp - 0x5c]
00805FAD  48 89 85 B0 02 00 00            mov qword ptr [rbp + 0x2b0], rax
00805FB4  0F B7 83 EC 06 00 00            movzx eax, word ptr [rbx + 0x6ec]
00805FBB  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00805FC0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00805FC5  48 89 85 C0 02 00 00            mov qword ptr [rbp + 0x2c0], rax
00805FCC  48 8D 85 00 02 00 00            lea rax, [rbp + 0x200]
00805FD3  48 89 8D A0 02 00 00            mov qword ptr [rbp + 0x2a0], rcx
00805FDA  49 8B CC                        mov rcx, r12
00805FDD  89 95 A8 02 00 00               mov dword ptr [rbp + 0x2a8], edx
00805FE3  48 8D 15 76 31 85 FF            lea rdx, [rip - 0x7ace8a]
00805FEA  44 89 8D AC 02 00 00            mov dword ptr [rbp + 0x2ac], r9d
00805FF1  41 B9 01 00 00 00               mov r9d, 1
00805FF7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00805FFC  C7 44 24 30 0D 00 00 00         mov dword ptr [rsp + 0x30], 0xd
00806004  48 C7 85 98 02 00 00 02 00 00 00  mov qword ptr [rbp + 0x298], 2
0080600F  48 C7 85 B8 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x2b8], 4
0080601A  48 C7 85 C8 02 00 00 02 00 00 00  mov qword ptr [rbp + 0x2c8], 2
00806025  E8 1E 43 CA FF                  call 0x1404aa348
0080602A  48 83 C7 1C                     add rdi, 0x1c
0080602E  48 83 C6 10                     add rsi, 0x10
00806032  49 83 ED 01                     sub r13, 1
00806036  0F 85 49 FE FF FF               jne 0x140805e85
0080603C  33 D2                           xor edx, edx
0080603E  4C 8D A3 E8 01 00 00            lea r12, [rbx + 0x1e8]
00806045  49 8B CE                        mov rcx, r14
00806048  E8 23 C8 37 00                  call 0x140b82870
0080604D  E9 4A 02 00 00                  jmp 0x14080629c
00806052  33 D2                           xor edx, edx
00806054  48 8B CB                        mov rcx, rbx
00806057  E8 EC D8 FF FF                  call 0x140803948
0080605C  4C 8B F0                        mov r14, rax
0080605F  48 85 C0                        test rax, rax
00806062  0F 84 34 02 00 00               je 0x14080629c
00806068  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
0080606F  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00806073  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00806077  E8 94 20 C4 FF                  call 0x140448110
0080607C  66 41 FF 8F E6 01 00 00         dec word ptr [r15 + 0x1e6]
00806084  49 8D 7E 10                     lea rdi, [r14 + 0x10]
00806088  48 8B CF                        mov rcx, rdi
0080608B  45 33 C0                        xor r8d, r8d
0080608E  33 D2                           xor edx, edx
00806090  90                              nop
00806091  E8 9A A1 A0 FF                  call 0x140210230
00806096  48 8B F0                        mov rsi, rax
00806099  33 C0                           xor eax, eax
0080609B  8D 48 11                        lea ecx, [rax + 0x11]
0080609E  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
008060A3  74 10                           je 0x1408060b5
008060A5  4C 8B CF                        mov r9, rdi
008060A8  4C 8B C6                        mov r8, rsi
008060AB  33 D2                           xor edx, edx
008060AD  48 8B CF                        mov rcx, rdi
008060B0  E8 97 A3 A0 FF                  call 0x14021044c
008060B5  48 85 F6                        test rsi, rsi
008060B8  74 04                           je 0x1408060be
008060BA  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
008060BE  49 8B 36                        mov rsi, qword ptr [r14]
008060C1  49 3B F6                        cmp rsi, r14
008060C4  0F 84 94 01 00 00               je 0x14080625e
008060CA  4C 8B 25 47 15 63 00            mov r12, qword ptr [rip + 0x631547]
008060D1  41 83 3C 24 05                  cmp dword ptr [r12], 5
008060D6  0F 86 6F 01 00 00               jbe 0x14080624b
008060DC  BA 20 00 00 00                  mov edx, 0x20
008060E1  49 8B CC                        mov rcx, r12
008060E4  E8 B7 89 C2 FF                  call 0x14042eaa0
008060E9  84 C0                           test al, al
008060EB  0F 84 5A 01 00 00               je 0x14080624b
008060F1  48 8B CB                        mov rcx, rbx
008060F4  E8 17 78 C3 FF                  call 0x14043d910
008060F9  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008060FD  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
00806104  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00806107  48 8D 45 A8                     lea rax, [rbp - 0x58]
0080610B  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00806112  48 C7 85 58 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x158], 4
0080611D  E8 E2 11 C2 FF                  call 0x140427304
00806122  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
00806125  48 8D 45 AC                     lea rax, [rbp - 0x54]
00806129  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00806130  48 8D 15 FC 30 85 FF            lea rdx, [rip - 0x7acf04]
00806137  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0080613A  41 B9 01 00 00 00               mov r9d, 1
00806140  89 45 B0                        mov dword ptr [rbp - 0x50], eax
00806143  48 8D 45 B0                     lea rax, [rbp - 0x50]
00806147  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
0080614E  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
00806151  89 45 B4                        mov dword ptr [rbp - 0x4c], eax
00806154  48 8D 45 B4                     lea rax, [rbp - 0x4c]
00806158  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
0080615F  8B 46 3C                        mov eax, dword ptr [rsi + 0x3c]
00806162  89 45 B8                        mov dword ptr [rbp - 0x48], eax
00806165  48 8D 45 B8                     lea rax, [rbp - 0x48]
00806169  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00806170  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00806173  89 45 BC                        mov dword ptr [rbp - 0x44], eax
00806176  48 8D 45 BC                     lea rax, [rbp - 0x44]
0080617A  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
00806181  48 8D 85 D8 01 00 00            lea rax, [rbp + 0x1d8]
00806188  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
0080618F  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00806193  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
0080619A  0F B7 46 28                     movzx eax, word ptr [rsi + 0x28]
0080619E  89 85 D8 01 00 00               mov dword ptr [rbp + 0x1d8], eax
008061A4  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
008061A7  89 45 C0                        mov dword ptr [rbp - 0x40], eax
008061AA  48 8D 45 C0                     lea rax, [rbp - 0x40]
008061AE  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
008061B5  0F B7 83 EC 06 00 00            movzx eax, word ptr [rbx + 0x6ec]
008061BC  66 89 44 24 44                  mov word ptr [rsp + 0x44], ax
008061C1  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008061C6  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
008061CD  48 8D 85 30 01 00 00            lea rax, [rbp + 0x130]
008061D4  89 4D AC                        mov dword ptr [rbp - 0x54], ecx
008061D7  49 8B CC                        mov rcx, r12
008061DA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008061DF  C7 44 24 30 0D 00 00 00         mov dword ptr [rsp + 0x30], 0xd
008061E7  48 C7 85 78 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x178], 4
008061F2  48 C7 85 88 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x188], 4
008061FD  48 C7 85 98 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x198], 4
00806208  48 C7 85 A8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1a8], 4
00806213  48 C7 85 B8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1b8], 4
0080621E  48 C7 85 C8 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x1c8], 2
00806229  44 89 AD DC 01 00 00            mov dword ptr [rbp + 0x1dc], r13d
00806230  48 C7 85 E8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1e8], 4
0080623B  48 C7 85 F8 01 00 00 02 00 00 00  mov qword ptr [rbp + 0x1f8], 2
00806246  E8 FD 40 CA FF                  call 0x1404aa348
0080624B  48 8B 36                        mov rsi, qword ptr [rsi]
0080624E  49 3B F6                        cmp rsi, r14
00806251  0F 85 73 FE FF FF               jne 0x1408060ca
00806257  4C 8D A3 E8 01 00 00            lea r12, [rbx + 0x1e8]
0080625E  B8 11 00 00 00                  mov eax, 0x11
00806263  F0 4C 0F B1 2F                  lock cmpxchg qword ptr [rdi], r13
00806268  74 08                           je 0x140806272
0080626A  48 8B CF                        mov rcx, rdi
0080626D  E8 CE D1 A5 FF                  call 0x140263440
00806272  48 8B CF                        mov rcx, rdi
00806275  E8 86 B3 AD FF                  call 0x1402e1600
0080627A  B8 01 00 00 00                  mov eax, 1
0080627F  90                              nop
00806280  66 41 01 87 E6 01 00 00         add word ptr [r15 + 0x1e6], ax
00806288  75 12                           jne 0x14080629c
0080628A  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
00806291  90                              nop
00806292  48 39 00                        cmp qword ptr [rax], rax
00806295  74 05                           je 0x14080629c
00806297  E8 E4 C9 AD FF                  call 0x1402e2c80
0080629C  33 D2                           xor edx, edx
0080629E  48 8D 4D E0                     lea rcx, [rbp - 0x20]
008062A2  E8 89 1A A1 FF                  call 0x140217d30
008062A7  49 8B CC                        mov rcx, r12
008062AA  E8 D1 3B B4 FF                  call 0x140349e80
008062AF  48 8B CB                        mov rcx, rbx
008062B2  E8 49 66 11 00                  call 0x14091c900
008062B7  41 BE 01 00 00 00               mov r14d, 1
008062BD  48 8B D8                        mov rbx, rax
008062C0  48 85 C0                        test rax, rax
008062C3  0F 85 54 FB FF FF               jne 0x140805e1d
008062C9  48 8B 8D A0 03 00 00            mov rcx, qword ptr [rbp + 0x3a0]
008062D0  48 33 CC                        xor rcx, rsp
008062D3  E8 68 63 EA FF                  call 0x1406ac640
008062D8  4C 8D 9C 24 B0 04 00 00         lea r11, [rsp + 0x4b0]
008062E0  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008062E4  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
008062E8  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
008062EC  49 8B E3                        mov rsp, r11
008062EF  41 5F                           pop r15
008062F1  41 5E                           pop r14
008062F3  41 5D                           pop r13
008062F5  41 5C                           pop r12
008062F7  5D                              pop rbp
008062F8  C3                              ret
008062F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLogHotPatchRundown(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m45C;
    unsigned int v_stack_m460;
    unsigned int v_stack_m464;
    unsigned int v_stack_m468;
    unsigned int v_stack_m46C;
    unsigned int v_stack_m470;
    unsigned int v_stack_m474;
    unsigned int v_stack_m478;
    unsigned int v_stack_m47C;
    unsigned int v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned int v_stack_m490;
    unsigned __int16 v_stack_m494;
    unsigned __int16 v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned int v_stack_m4A8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x4B0ULL);
    result = (*(unsigned __int64 *)(v_rip + 6311791)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 984 + 928) = result;
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 984 - 32) = v_xmm0;
    v_stack_m490 = 0;
    *(unsigned __int64 *)(v_rsp - 984 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 984 - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 984) = v_xmm0;
    if ((*(unsigned __int64 *)(v_rip + 6495792)) == 0) goto loc_008062C9;
    if ((*(unsigned int *)(v_rip + 6495650)) == 0) goto loc_008062C9;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6495596, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6495596;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6495596;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r13 + 1);
    }
    goto loc_00805879;
loc_00805873:
loc_00805879:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498)) != 0) goto loc_00805873;
    goto loc_00805977;
loc_00805883:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6495630))) <= 5) goto loc_0080593E;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 6495630), 32, *(unsigned __int64 *)(v_rip + 6495630), a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6495498) + 24);
        a2 = v_rip - 8046760;
        *(unsigned int *)(v_rsp - 984 - 60) = (unsigned int)(result);
        a4 = (unsigned int)(v_r13 + 1);
        result = v_rsp - 984 - 60;
        *(unsigned __int64 *)(v_rsp - 984 + 872) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 864) = result;
        a1 = *(unsigned __int64 *)(v_rip + 6495630);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6495498) + 28);
        v_stack_m480 = (unsigned int)(result);
        result = v_stack_m480;
        *(unsigned __int64 *)(v_rsp - 984 + 880) = result;
        result = v_rsp - 984 + 920;
        *(unsigned __int64 *)(v_rsp - 984 + 896) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 48);
        *(unsigned __int64 *)(v_rsp - 984 + 912) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6495498) + 40);
        *(unsigned int *)(v_rsp - 984 + 920) = (unsigned int)(result);
        result = v_rsp - 984 + 832;
        v_stack_m4A0 = result;
        v_stack_m4A8 = 6;
        *(unsigned __int64 *)(v_rsp - 984 + 888) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 904) = 2;
        *(unsigned int *)(v_rsp - 984 + 924) = 0;
        result = tlgWriteEx_EtwWriteEx(a1, a2, *(unsigned __int64 *)(v_rip + 6495630), a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 8) == 0) goto loc_0080596D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 8)) == 0) goto loc_00805977;
loc_00805955:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 8))) != 0) goto loc_00805955;
    goto loc_00805977;
loc_00805965:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 8))))) goto loc_00805977;
loc_0080596D:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495498) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00805965;
loc_00805977:
    if (v_rbx != 0) goto loc_00805883;
    goto loc_00805992;
loc_0080598C:
loc_00805992:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209)) != 0) goto loc_0080598C;
    goto loc_00805B10;
loc_0080599C:
    goto loc_008059AB;
loc_008059A5:
loc_008059AB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24)) != 0) goto loc_008059A5;
    goto loc_00805ACE;
loc_008059B5:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6495324))) <= 5) goto loc_00805A95;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 6495324), 32, *(unsigned __int64 *)(v_rip + 6495324), a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 24);
        a2 = v_rip - 8046983;
        v_stack_m47C = (unsigned int)(result);
        a4 = (unsigned int)(v_r13 + 1);
        result = v_stack_m47C;
        *(unsigned __int64 *)(v_rsp - 984 + 760) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 752) = result;
        a1 = *(unsigned __int64 *)(v_rip + 6495324);
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 28);
        v_stack_m478 = (unsigned int)(result);
        result = v_stack_m478;
        *(unsigned __int64 *)(v_rsp - 984 + 768) = result;
        result = v_rsp - 984 + 808;
        *(unsigned __int64 *)(v_rsp - 984 + 784) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 48);
        *(unsigned __int64 *)(v_rsp - 984 + 800) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 40);
        *(unsigned int *)(v_rsp - 984 + 808) = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_rip + 6495209) + 40;
        *(unsigned __int64 *)(v_rsp - 984 + 816) = result;
        result = *(unsigned __int8 *)(result + 1);
        *(unsigned __int64 *)(v_rsp - 984 + 776) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 792) = 2;
        *(unsigned int *)(v_rsp - 984 + 812) = 0;
        result = result * 4 + 8;
        *(unsigned int *)(v_rsp - 984 + 828) = 0;
        *(unsigned int *)(v_rsp - 984 + 824) = (unsigned int)(result);
        result = v_rsp - 984 + 720;
        v_stack_m4A0 = result;
        v_stack_m4A8 = 7;
        result = tlgWriteEx_EtwWriteEx(a1, a2, *(unsigned __int64 *)(v_rip + 6495324), a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 8) == 0) goto loc_00805AC4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 8)) == 0) goto loc_00805ACE;
loc_00805AAC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 8))) != 0) goto loc_00805AAC;
    goto loc_00805ACE;
loc_00805ABC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 8))))) goto loc_00805ACE;
loc_00805AC4:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 24) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00805ABC;
loc_00805ACE:
    if (v_rbx != 0) goto loc_008059B5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 8) == 0) goto loc_00805B06;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 8)) == 0) goto loc_00805B10;
loc_00805AEE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 8))) != 0) goto loc_00805AEE;
    goto loc_00805B10;
loc_00805AFE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 8))))) goto loc_00805B10;
loc_00805B06:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6495209) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00805AFE;
loc_00805B10:
    if (v_rdi != 0) goto loc_0080599C;
    result = v_rdi + 17;
    if (v_rdi != 0) {
        a1 = v_rip + 6495596;
        result = ExfReleasePushLockShared(a1, a2, *(unsigned __int64 *)(v_rip + 6495324), a4);
    }
    result = KeAbPostRelease(v_rip + 6495596, a2, *(unsigned __int64 *)(v_rip + 6495324), a4);
    if (v_rdi != 0) goto loc_00805B54;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 6495596, a2, *(unsigned __int64 *)(v_rip + 6495324), a4);
    }
    result = MmAcquireLoadLock(v_rip + 6495596, a2, *(unsigned __int64 *)(v_rip + 6495324), a4);
    goto loc_00805B6B;
loc_00805B65:
loc_00805B6B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760)) != 0) goto loc_00805B65;
    goto loc_00805CA5;
loc_00805B79:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494872))) <= 5) goto loc_00805C6C;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 6494872), 32, *(unsigned __int64 *)(v_rip + 6494872), a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494760) + 24);
        a2 = v_rip - 8047809;
        v_stack_m474 = (unsigned int)(result);
        a4 = (unsigned int)(v_r13 + 1);
        result = v_stack_m474;
        *(unsigned __int64 *)(v_rsp - 984 + 56) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 48) = result;
        a1 = *(unsigned __int64 *)(v_rip + 6494872);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494760) + 28);
        v_stack_m470 = (unsigned int)(result);
        result = v_stack_m470;
        *(unsigned __int64 *)(v_rsp - 984 + 64) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494760) + 32);
        v_stack_m46C = (unsigned int)(result);
        result = v_stack_m46C;
        *(unsigned __int64 *)(v_rsp - 984 + 80) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494760) + 36);
        v_stack_m468 = (unsigned int)(result);
        result = v_stack_m468;
        *(unsigned __int64 *)(v_rsp - 984 + 96) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494760) + 40);
        v_stack_m464 = (unsigned int)(result);
        result = v_stack_m464;
        *(unsigned __int64 *)(v_rsp - 984 + 112) = result;
        result = v_rsp - 984 + 152;
        *(unsigned __int64 *)(v_rsp - 984 + 128) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 56);
        *(unsigned __int64 *)(v_rsp - 984 + 144) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6494760) + 48);
        *(unsigned int *)(v_rsp - 984 + 152) = (unsigned int)(result);
        result = v_rsp - 984 + 16;
        v_stack_m4A0 = result;
        v_stack_m4A8 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760)) + 9);
        *(unsigned __int64 *)(v_rsp - 984 + 72) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 88) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 104) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 120) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 136) = 2;
        *(unsigned int *)(v_rsp - 984 + 156) = 0;
        result = tlgWriteEx_EtwWriteEx(a1, a2, *(unsigned __int64 *)(v_rip + 6494872), a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 8) == 0) goto loc_00805C9B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 8)) == 0) goto loc_00805CA5;
loc_00805C83:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 8))) != 0) goto loc_00805C83;
    goto loc_00805CA5;
loc_00805C93:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 8))))) goto loc_00805CA5;
loc_00805C9B:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00805C93;
loc_00805CA5:
    if (v_rbx != 0) goto loc_00805B79;
    goto loc_00805E00;
loc_00805CC1:
    result = MiIsActiveSystemHotPatch(*(unsigned __int64 *)(v_rip + 7272459), a2, *(unsigned __int64 *)(v_rip + 6494872), a4);
    if ((unsigned int)(result) == 0) goto loc_00805DFD;
    result = MiGetBaseLoaderPortion(*(unsigned __int64 *)(v_rip + 7272459), a2, *(unsigned __int64 *)(v_rip + 6494872), a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494520))) <= 5) goto loc_00805DFD;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 6494520), 32, *(unsigned __int64 *)(v_rip + 6494520), result);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(result + 248) + 120);
        a2 = v_rip - 8048022;
        v_stack_m460 = (unsigned int)(result);
        a1 = *(unsigned __int64 *)(v_rip + 6494520);
        result = v_stack_m460;
        *(unsigned __int64 *)(v_rsp - 984 + 200) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 192) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(result + 248) + 156);
        v_stack_m45C = (unsigned int)(result);
        result = v_stack_m45C;
        *(unsigned __int64 *)(v_rsp - 984 + 208) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7272459) + 120);
        *(unsigned int *)(v_rsp - 984 - 128) = (unsigned int)(result);
        result = v_rsp - 984 - 128;
        *(unsigned __int64 *)(v_rsp - 984 + 224) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7272459) + 156);
        *(unsigned int *)(v_rsp - 984 - 124) = (unsigned int)(result);
        result = v_rsp - 984 - 124;
        *(unsigned __int64 *)(v_rsp - 984 + 240) = result;
        result = *(unsigned int *)(result + 272);
        a4 = (unsigned int)(v_r13 + 1);
        *(unsigned int *)(v_rsp - 984 - 120) = (unsigned int)(result);
        result = v_rsp - 984 - 120;
        *(unsigned __int64 *)(v_rsp - 984 + 256) = result;
        result = v_rsp - 984 + 296;
        *(unsigned __int64 *)(v_rsp - 984 + 272) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459) + 80);
        *(unsigned __int64 *)(v_rsp - 984 + 288) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 7272459) + 72);
        *(unsigned int *)(v_rsp - 984 + 296) = (unsigned int)(result);
        result = v_rsp - 984 + 160;
        v_stack_m4A0 = result;
        v_stack_m4A8 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6494760)) + 9);
        *(unsigned __int64 *)(v_rsp - 984 + 216) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 232) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 248) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 264) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 280) = 2;
        *(unsigned int *)(v_rsp - 984 + 300) = 0;
        result = tlgWriteEx_EtwWriteEx(a1, a2, *(unsigned __int64 *)(v_rip + 6494520), a4);
    }
loc_00805E00:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459))) != (v_rip + 7272452)) goto loc_00805CC1;
    result = MmReleaseLoadLock(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(v_rip + 6494520), a4);
    a1 = 0;
    result = PsGetNextProcess(a1, a2, *(unsigned __int64 *)(v_rip + 6494520), a4);
    goto loc_008062BD;
loc_00805E1D:
    result = ExAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 488, a2, *(unsigned __int64 *)(v_rip + 6494520), a4);
    if ((unsigned __int8)(result) == 0) goto loc_008062AF;
    a2 = 0;
    result = KiStackAttachProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)), a2, v_rsp - 984 - 32, a4);
    if ((((unsigned __int8)(v_r13 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 368)))) == 0) goto loc_00806052;
    *(unsigned __int64 *)(v_rsp - 984 - 56) = 0;
    result = VslQueryActiveSecurePatches(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 368), v_rsp - 984 - 56, v_stack_m490, a4);
    if (sign_flag) goto loc_0080629C;
    if ((unsigned int)((unsigned int)(v_stack_m490)) == 0) goto loc_0080629C;
loc_00805E85:
    v_stack_m488 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 984 - 56) + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6494092))) <= 5) goto loc_0080602A;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 6494092), 32, v_stack_m490, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459));
        result = PsGetProcessId(a1, 32, v_stack_m490, a4);
        *(unsigned int *)(v_rsp - 984 - 116) = (unsigned int)(result);
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 824;
        result = v_rsp - 984 - 116;
        *(unsigned __int64 *)(v_rsp - 984 + 552) = 4;
        a1 = v_rsp - 984 + 560;
        *(unsigned __int64 *)(v_rsp - 984 + 544) = result;
        a4 = 0;
        result = tlgCreate1Sz_char(a1, a2, v_stack_m490, a4);
        a3 = v_stack_m488;
        result = v_rsp - 984 - 112;
        *(unsigned __int64 *)(v_rsp - 984 + 576) = result;
        *(unsigned __int64 *)(v_rsp - 984 + 584) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 600) = 4;
        result = *(unsigned int *)(0 + a3 * 1 + 4);
        a1 = *(unsigned int *)(0 + a3 * 1);
        *(unsigned int *)(v_rsp - 984 - 108) = (unsigned int)(result);
        result = v_rsp - 984 - 108;
        *(unsigned __int64 *)(v_rsp - 984 + 592) = result;
        result = *(unsigned int *)(0 + a3 * 1 + 12);
        *(unsigned int *)(v_rsp - 984 - 104) = (unsigned int)(result);
        result = v_rsp - 984 - 104;
        *(unsigned __int64 *)(v_rsp - 984 + 608) = result;
        result = *(unsigned int *)(0 + a3 * 1 + 16);
        *(unsigned int *)(v_rsp - 984 - 100) = (unsigned int)(result);
        result = v_rsp - 984 - 100;
        *(unsigned __int64 *)(v_rsp - 984 + 624) = result;
        result = *(unsigned int *)(0 + a3 * 1 + 24);
        *(unsigned int *)(v_rsp - 984 - 96) = (unsigned int)(result);
        result = v_rsp - 984 - 96;
        *(unsigned __int64 *)(v_rsp - 984 + 640) = result;
        *(unsigned int *)(v_rsp - 984 - 112) = (unsigned int)(a1);
        *(unsigned __int64 *)(v_rsp - 984 + 616) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 632) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 648) = 4;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 984 - 56) + 8);
        a2 = *(unsigned __int16 *)(0 + result * 1);
        a1 = *(unsigned __int64 *)(0 + result * 1 + 8);
        result = v_rsp - 984 + 680;
        *(unsigned __int64 *)(v_rsp - 984 + 656) = result;
        result = *(unsigned int *)(0 + a3 * 1 + 8);
        *(unsigned int *)(v_rsp - 984 - 92) = (unsigned int)(result);
        result = v_rsp - 984 - 92;
        *(unsigned __int64 *)(v_rsp - 984 + 688) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 1772);
        v_stack_m498 = (unsigned __int16)(result);
        result = v_stack_m498;
        *(unsigned __int64 *)(v_rsp - 984 + 704) = result;
        result = v_rsp - 984 + 512;
        *(unsigned __int64 *)(v_rsp - 984 + 672) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 6494092);
        *(unsigned int *)(v_rsp - 984 + 680) = a2;
        a2 = v_rip - 8048266;
        *(unsigned int *)(v_rsp - 984 + 684) = 0;
        a4 = 1;
        v_stack_m4A0 = result;
        v_stack_m4A8 = 13;
        *(unsigned __int64 *)(v_rsp - 984 + 664) = 2;
        *(unsigned __int64 *)(v_rsp - 984 + 696) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 712) = 2;
        result = tlgWriteEx_EtwWriteEx(a1, a2, a3, a4);
    }
    v_rdi = (0) + (28);
    v_rsi = (0) + (16);
    v_r13 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m490)))) - (1);
    if (condition_is_not_equal) goto loc_00805E85;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 984 - 56), a2, a3, a4);
    goto loc_0080629C;
loc_00806052:
    a2 = 0;
    result = MiGetProcessHotPatchContext(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)), a2, a3, a4);
    if (result == 0) goto loc_0080629C;
    result = MiFillLogProcessInfo(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 1024, v_rsp - 984 - 40, v_rsp - 984 - 48, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 16, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 16;
        a3 = 0;
        a2 = 0;
        a1 = result + 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(result)) == result) goto loc_0080625E;
loc_008060CA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6493511))) <= 5) goto loc_0080624B;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 6493511), 32, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459));
        result = PsGetProcessId(a1, 32, a3, a4);
        a2 = *(unsigned __int64 *)(v_rsp - 984 - 48);
        a1 = v_rsp - 984 + 352;
        *(unsigned int *)(v_rsp - 984 - 88) = (unsigned int)(result);
        result = v_rsp - 984 - 88;
        *(unsigned __int64 *)(v_rsp - 984 + 336) = result;
        *(unsigned __int64 *)(v_rsp - 984 + 344) = 4;
        result = tlgCreate1Sz_char(a1, a2, a3, a4);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(result) + 32);
        result = v_rsp - 984 - 84;
        *(unsigned __int64 *)(v_rsp - 984 + 368) = result;
        a2 = v_rip - 8048388;
        result = *(unsigned int *)(*(unsigned __int64 *)(result) + 36);
        a4 = 1;
        *(unsigned int *)(v_rsp - 984 - 80) = (unsigned int)(result);
        result = v_rsp - 984 - 80;
        *(unsigned __int64 *)(v_rsp - 984 + 384) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(result) + 56);
        *(unsigned int *)(v_rsp - 984 - 76) = (unsigned int)(result);
        result = v_rsp - 984 - 76;
        *(unsigned __int64 *)(v_rsp - 984 + 400) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(result) + 60);
        *(unsigned int *)(v_rsp - 984 - 72) = (unsigned int)(result);
        result = v_rsp - 984 - 72;
        *(unsigned __int64 *)(v_rsp - 984 + 416) = result;
        result = *(unsigned int *)(*(unsigned __int64 *)(result) + 64);
        *(unsigned int *)(v_rsp - 984 - 68) = (unsigned int)(result);
        result = v_rsp - 984 - 68;
        *(unsigned __int64 *)(v_rsp - 984 + 432) = result;
        result = v_rsp - 984 + 472;
        *(unsigned __int64 *)(v_rsp - 984 + 448) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48);
        *(unsigned __int64 *)(v_rsp - 984 + 464) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(result) + 40);
        *(unsigned int *)(v_rsp - 984 + 472) = (unsigned int)(result);
        result = *(unsigned int *)(*(unsigned __int64 *)(result) + 16);
        *(unsigned int *)(v_rsp - 984 - 64) = (unsigned int)(result);
        result = v_rsp - 984 - 64;
        *(unsigned __int64 *)(v_rsp - 984 + 480) = result;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 1772);
        v_stack_m494 = (unsigned __int16)(result);
        result = v_stack_m494;
        *(unsigned __int64 *)(v_rsp - 984 + 496) = result;
        result = v_rsp - 984 + 304;
        *(unsigned int *)(v_rsp - 984 - 84) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 6493511);
        v_stack_m4A0 = result;
        v_stack_m4A8 = 13;
        *(unsigned __int64 *)(v_rsp - 984 + 376) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 392) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 408) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 424) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 440) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 456) = 2;
        *(unsigned int *)(v_rsp - 984 + 476) = (unsigned int)(v_r13);
        *(unsigned __int64 *)(v_rsp - 984 + 488) = 4;
        *(unsigned __int64 *)(v_rsp - 984 + 504) = 2;
        result = tlgWriteEx_EtwWriteEx(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result))) != result) goto loc_008060CA;
loc_0080625E:
    result = 17;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result))) != result) {
        a1 = result + 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(result + 16, a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result))) != result) goto loc_0080629C;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(result + 16, a2, a3, a4);
    }
    a2 = 0;
    result = KiUnstackDetachProcess(v_rsp - 984 - 32, a2, a3, a4);
    result = ExReleaseRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)) + 488, a2, a3, a4);
loc_008062AF:
    result = PsGetNextProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7272459)), a2, a3, a4);
loc_008062BD:
    if (result != 0) goto loc_00805E1D;
loc_008062C9:
    a1 = (*(unsigned __int64 *)(v_rsp - 984 + 928)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLogHotPatchRundown(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m45C;
    uint32_t v_stack_m460;
    uint32_t v_stack_m464;
    uint32_t v_stack_m468;
    uint32_t v_stack_m46C;
    uint32_t v_stack_m470;
    uint32_t v_stack_m474;
    uint32_t v_stack_m478;
    uint32_t v_stack_m47C;
    uint32_t v_stack_m480;
    uint64_t v_stack_m488;
    uint32_t v_stack_m490;
    uint16_t v_stack_m494;
    uint16_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint32_t v_stack_m4A8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x4B0ULL);
    result = (*(uint64_t *)(v_rip + 0x604F6F)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x3D8 + 0x3A0) = result;
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x3D8 - 0x20) = v_xmm0;
    v_stack_m490 = 0;
    *(uint64_t *)(local_rsp - 0x3D8 - 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3D8 - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x3D8) = v_xmm0;
    if ((*(uint64_t *)(v_rip + 0x631E30)) == 0) goto loc_008062C9;
    if ((*(uint32_t *)(v_rip + 0x631DA2)) == 0) goto loc_008062C9;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6495596, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6495596;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6495596;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r13 + 1);
    }
    goto loc_00805879;
loc_00805873:
loc_00805879:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A)) != 0) goto loc_00805873;
    goto loc_00805977;
loc_00805883:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x631D8E))) <= 5) goto loc_0080593E;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x631D8E), 32, *(uint64_t *)(v_rip + 0x631D8E), a4);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x18);
        Arg2 = v_rip - 8046760;
        *(uint32_t *)(local_rsp - 0x3D8 - 0x3C) = (uint32_t)(result);
        a4 = (uint32_t)(local_r13 + 1);
        result = local_rsp - 984 - 60;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x368) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x360) = result;
        Arg1 = *(uint64_t *)(v_rip + 0x631D8E);
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x1C);
        v_stack_m480 = (uint32_t)(result);
        result = v_stack_m480;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x370) = result;
        result = local_rsp - 984 + 920;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x380) = result;
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x30);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x390) = result;
        result = *(uint16_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x28);
        *(uint32_t *)(local_rsp - 0x3D8 + 0x398) = (uint32_t)(result);
        result = local_rsp - 984 + 832;
        v_stack_m4A0 = result;
        v_stack_m4A8 = 6;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x378) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x388) = 2;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x39C) = 0;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, *(uint64_t *)(v_rip + 0x631D8E), a4);
    }
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x8) == 0) goto loc_0080596D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x8)) == 0) goto loc_00805977;
loc_00805955:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x8))) != 0) goto loc_00805955;
    goto loc_00805977;
loc_00805965:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x8))))) goto loc_00805977;
loc_0080596D:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631D0A) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00805965;
loc_00805977:
    if (local_rbx != 0) goto loc_00805883;
    goto loc_00805992;
loc_0080598C:
loc_00805992:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9)) != 0) goto loc_0080598C;
    goto loc_00805B10;
loc_0080599C:
    goto loc_008059AB;
loc_008059A5:
loc_008059AB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18)) != 0) goto loc_008059A5;
    goto loc_00805ACE;
loc_008059B5:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x631C5C))) <= 5) goto loc_00805A95;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x631C5C), 32, *(uint64_t *)(v_rip + 0x631C5C), a4);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x18);
        Arg2 = v_rip - 8046983;
        v_stack_m47C = (uint32_t)(result);
        a4 = (uint32_t)(local_r13 + 1);
        result = v_stack_m47C;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2F8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2F0) = result;
        Arg1 = *(uint64_t *)(v_rip + 0x631C5C);
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x1C);
        v_stack_m478 = (uint32_t)(result);
        result = v_stack_m478;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x300) = result;
        result = local_rsp - 984 + 808;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x310) = result;
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x30);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x320) = result;
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x28);
        *(uint32_t *)(local_rsp - 0x3D8 + 0x328) = (uint32_t)(result);
        result = *(uint64_t *)(v_rip + 0x631BE9) + 40;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x330) = result;
        result = *(uint8_t *)(result + 0x1);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x308) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x318) = 2;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x32C) = 0;
        result = result * 4 + 8;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x33C) = 0;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x338) = (uint32_t)(result);
        result = local_rsp - 984 + 720;
        v_stack_m4A0 = result;
        v_stack_m4A8 = 7;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, *(uint64_t *)(v_rip + 0x631C5C), a4);
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x8) == 0) goto loc_00805AC4;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x8)) == 0) goto loc_00805ACE;
loc_00805AAC:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x8))) != 0) goto loc_00805AAC;
    goto loc_00805ACE;
loc_00805ABC:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x8))))) goto loc_00805ACE;
loc_00805AC4:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x18) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00805ABC;
loc_00805ACE:
    if (local_rbx != 0) goto loc_008059B5;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x8) == 0) goto loc_00805B06;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x8)) == 0) goto loc_00805B10;
loc_00805AEE:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x8))) != 0) goto loc_00805AEE;
    goto loc_00805B10;
loc_00805AFE:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x8))))) goto loc_00805B10;
loc_00805B06:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631BE9) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00805AFE;
loc_00805B10:
    if (local_rdi != 0) goto loc_0080599C;
    result = local_rdi + 17;
    if (local_rdi != 0) {
        Arg1 = v_rip + 6495596;
        result = ExfReleasePushLockShared(Arg1, Arg2, *(uint64_t *)(v_rip + 0x631C5C), a4);
    }
    result = KeAbPostRelease(v_rip + 6495596, Arg2, *(uint64_t *)(v_rip + 0x631C5C), a4);
    if (local_rdi != 0) goto loc_00805B54;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 6495596, Arg2, *(uint64_t *)(v_rip + 0x631C5C), a4);
    }
    result = MmAcquireLoadLock(v_rip + 6495596, Arg2, *(uint64_t *)(v_rip + 0x631C5C), a4);
    goto loc_00805B6B;
loc_00805B65:
loc_00805B6B:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28)) != 0) goto loc_00805B65;
    goto loc_00805CA5;
loc_00805B79:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x631A98))) <= 5) goto loc_00805C6C;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x631A98), 32, *(uint64_t *)(v_rip + 0x631A98), a4);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x18);
        Arg2 = v_rip - 8047809;
        v_stack_m474 = (uint32_t)(result);
        a4 = (uint32_t)(local_r13 + 1);
        result = v_stack_m474;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x38) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x30) = result;
        Arg1 = *(uint64_t *)(v_rip + 0x631A98);
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x1C);
        v_stack_m470 = (uint32_t)(result);
        result = v_stack_m470;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x40) = result;
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x20);
        v_stack_m46C = (uint32_t)(result);
        result = v_stack_m46C;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x50) = result;
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x24);
        v_stack_m468 = (uint32_t)(result);
        result = v_stack_m468;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x60) = result;
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x28);
        v_stack_m464 = (uint32_t)(result);
        result = v_stack_m464;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x70) = result;
        result = local_rsp - 984 + 152;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x80) = result;
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x38);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x90) = result;
        result = *(uint16_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x30);
        *(uint32_t *)(local_rsp - 0x3D8 + 0x98) = (uint32_t)(result);
        result = local_rsp - 984 + 16;
        v_stack_m4A0 = result;
        v_stack_m4A8 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28)) + 9);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x48) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x58) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x68) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x78) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x88) = 2;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x9C) = 0;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, *(uint64_t *)(v_rip + 0x631A98), a4);
    }
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x8) == 0) goto loc_00805C9B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x8)) == 0) goto loc_00805CA5;
loc_00805C83:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x8))) != 0) goto loc_00805C83;
    goto loc_00805CA5;
loc_00805C93:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x8))))) goto loc_00805CA5;
loc_00805C9B:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00805C93;
loc_00805CA5:
    if (local_rbx != 0) goto loc_00805B79;
    goto loc_00805E00;
loc_00805CC1:
    result = MiIsActiveSystemHotPatch(*(uint64_t *)(v_rip + 0x6EF80B), Arg2, *(uint64_t *)(v_rip + 0x631A98), a4);
    if ((uint32_t)(result) == 0) goto loc_00805DFD;
    result = MiGetBaseLoaderPortion(*(uint64_t *)(v_rip + 0x6EF80B), Arg2, *(uint64_t *)(v_rip + 0x631A98), a4);
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x631938))) <= 5) goto loc_00805DFD;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x631938), 32, *(uint64_t *)(v_rip + 0x631938), result);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(result + 0xF8) + 0x78);
        Arg2 = v_rip - 8048022;
        v_stack_m460 = (uint32_t)(result);
        Arg1 = *(uint64_t *)(v_rip + 0x631938);
        result = v_stack_m460;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xC8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xC0) = result;
        result = *(uint32_t *)(*(uint64_t *)(result + 0xF8) + 0x9C);
        v_stack_m45C = (uint32_t)(result);
        result = v_stack_m45C;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xD0) = result;
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x6EF80B) + 0x78);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x80) = (uint32_t)(result);
        result = local_rsp - 984 - 128;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xE0) = result;
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x6EF80B) + 0x9C);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x7C) = (uint32_t)(result);
        result = local_rsp - 984 - 124;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xF0) = result;
        result = *(uint32_t *)(result + 0x110);
        a4 = (uint32_t)(local_r13 + 1);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x78) = (uint32_t)(result);
        result = local_rsp - 984 - 120;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x100) = result;
        result = local_rsp - 984 + 296;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x110) = result;
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B) + 0x50);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x120) = result;
        result = *(uint16_t *)(*(uint64_t *)(v_rip + 0x6EF80B) + 0x48);
        *(uint32_t *)(local_rsp - 0x3D8 + 0x128) = (uint32_t)(result);
        result = local_rsp - 984 + 160;
        v_stack_m4A0 = result;
        v_stack_m4A8 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x631A28)) + 9);
        *(uint64_t *)(local_rsp - 0x3D8 + 0xD8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xE8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0xF8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x108) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x118) = 2;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x12C) = 0;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, *(uint64_t *)(v_rip + 0x631938), a4);
    }
loc_00805E00:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B))) != (v_rip + 7272452)) goto loc_00805CC1;
    result = MmReleaseLoadLock(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(v_rip + 0x631938), a4);
    Arg1 = 0;
    result = PsGetNextProcess(Arg1, Arg2, *(uint64_t *)(v_rip + 0x631938), a4);
    goto loc_008062BD;
loc_00805E1D:
    result = ExAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 488, Arg2, *(uint64_t *)(v_rip + 0x631938), a4);
    if ((uint8_t)(result) == 0) goto loc_008062AF;
    Arg2 = 0;
    result = KiStackAttachProcess(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)), Arg2, local_rsp - 984 - 32, a4);
    if ((((uint8_t)(local_r13 + 1)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 0x170)))) == 0) goto loc_00806052;
    *(uint64_t *)(local_rsp - 0x3D8 - 0x38) = 0;
    result = VslQueryActiveSecurePatches(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 0x170), local_rsp - 984 - 56, v_stack_m490, a4);
    if (sign_flag) goto loc_0080629C;
    if ((uint32_t)((uint32_t)(v_stack_m490)) == 0) goto loc_0080629C;
loc_00805E85:
    v_stack_m488 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x38) + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x63178C))) <= 5) goto loc_0080602A;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x63178C), 32, v_stack_m490, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B));
        result = PsGetProcessId(Arg1, 32, v_stack_m490, a4);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x74) = (uint32_t)(result);
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 824;
        result = local_rsp - 984 - 116;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x228) = 4;
        Arg1 = local_rsp - 984 + 560;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x220) = result;
        a4 = 0;
        result = tlgCreate1Sz_char(Arg1, Arg2, v_stack_m490, a4);
        Arg3 = v_stack_m488;
        result = local_rsp - 984 - 112;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x240) = result;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x248) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x258) = 4;
        result = *(uint32_t *)(0 + Arg3 * 1 + 0x4);
        Arg1 = *(uint32_t *)(0 + Arg3 * 1);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x6C) = (uint32_t)(result);
        result = local_rsp - 984 - 108;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x250) = result;
        result = *(uint32_t *)(0 + Arg3 * 1 + 0xC);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x68) = (uint32_t)(result);
        result = local_rsp - 984 - 104;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x260) = result;
        result = *(uint32_t *)(0 + Arg3 * 1 + 0x10);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x64) = (uint32_t)(result);
        result = local_rsp - 984 - 100;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x270) = result;
        result = *(uint32_t *)(0 + Arg3 * 1 + 0x18);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x60) = (uint32_t)(result);
        result = local_rsp - 984 - 96;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x280) = result;
        *(uint32_t *)(local_rsp - 0x3D8 - 0x70) = (uint32_t)(Arg1);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x268) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x278) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x288) = 4;
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x38) + 0x8);
        Arg2 = *(uint16_t *)(0 + result * 1);
        Arg1 = *(uint64_t *)(0 + result * 1 + 0x8);
        result = local_rsp - 984 + 680;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x290) = result;
        result = *(uint32_t *)(0 + Arg3 * 1 + 0x8);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x5C) = (uint32_t)(result);
        result = local_rsp - 984 - 92;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2B0) = result;
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 0x6EC);
        v_stack_m498 = (uint16_t)(result);
        result = v_stack_m498;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2C0) = result;
        result = local_rsp - 984 + 512;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2A0) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x63178C);
        *(uint32_t *)(local_rsp - 0x3D8 + 0x2A8) = Arg2;
        Arg2 = v_rip - 8048266;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x2AC) = 0;
        a4 = 1;
        v_stack_m4A0 = result;
        v_stack_m4A8 = 13;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x298) = 2;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2B8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x2C8) = 2;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, Arg3, a4);
    }
    local_rdi = (0) + (28);
    local_rsi = (0) + (16);
    local_r13 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m490)))) - (1);
    if (condition_is_not_equal) goto loc_00805E85;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x3D8 - 0x38), Arg2, Arg3, a4);
    goto loc_0080629C;
loc_00806052:
    Arg2 = 0;
    result = MiGetProcessHotPatchContext(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)), Arg2, Arg3, a4);
    if (result == 0) goto loc_0080629C;
    result = MiFillLogProcessInfo(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 1024, local_rsp - 984 - 40, local_rsp - 984 - 48, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 16, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(result)) == result) goto loc_0080625E;
loc_008060CA:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x631547))) <= 5) goto loc_0080624B;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x631547), 32, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B));
        result = PsGetProcessId(Arg1, 32, Arg3, a4);
        Arg2 = *(uint64_t *)(local_rsp - 0x3D8 - 0x30);
        Arg1 = local_rsp - 984 + 352;
        *(uint32_t *)(local_rsp - 0x3D8 - 0x58) = (uint32_t)(result);
        result = local_rsp - 984 - 88;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x150) = result;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x158) = 4;
        result = tlgCreate1Sz_char(Arg1, Arg2, Arg3, a4);
        Arg1 = *(uint32_t *)(*(uint64_t *)(result) + 0x20);
        result = local_rsp - 984 - 84;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x170) = result;
        Arg2 = v_rip - 8048388;
        result = *(uint32_t *)(*(uint64_t *)(result) + 0x24);
        a4 = 1;
        *(uint32_t *)(local_rsp - 0x3D8 - 0x50) = (uint32_t)(result);
        result = local_rsp - 984 - 80;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x180) = result;
        result = *(uint32_t *)(*(uint64_t *)(result) + 0x38);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x4C) = (uint32_t)(result);
        result = local_rsp - 984 - 76;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x190) = result;
        result = *(uint32_t *)(*(uint64_t *)(result) + 0x3C);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x48) = (uint32_t)(result);
        result = local_rsp - 984 - 72;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1A0) = result;
        result = *(uint32_t *)(*(uint64_t *)(result) + 0x40);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x44) = (uint32_t)(result);
        result = local_rsp - 984 - 68;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1B0) = result;
        result = local_rsp - 984 + 472;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1C0) = result;
        result = *(uint64_t *)(*(uint64_t *)(result) + 0x30);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1D0) = result;
        result = *(uint16_t *)(*(uint64_t *)(result) + 0x28);
        *(uint32_t *)(local_rsp - 0x3D8 + 0x1D8) = (uint32_t)(result);
        result = *(uint32_t *)(*(uint64_t *)(result) + 0x10);
        *(uint32_t *)(local_rsp - 0x3D8 - 0x40) = (uint32_t)(result);
        result = local_rsp - 984 - 64;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1E0) = result;
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 0x6EC);
        v_stack_m494 = (uint16_t)(result);
        result = v_stack_m494;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1F0) = result;
        result = local_rsp - 984 + 304;
        *(uint32_t *)(local_rsp - 0x3D8 - 0x54) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x631547);
        v_stack_m4A0 = result;
        v_stack_m4A8 = 13;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x178) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x188) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x198) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1A8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1B8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1C8) = 2;
        *(uint32_t *)(local_rsp - 0x3D8 + 0x1DC) = (uint32_t)(local_r13);
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1E8) = 4;
        *(uint64_t *)(local_rsp - 0x3D8 + 0x1F8) = 2;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(result))) != result) goto loc_008060CA;
loc_0080625E:
    result = 17;
    if ((*(uint64_t *)(*(uint64_t *)(result))) != result) {
        Arg1 = result + 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(result + 16, Arg2, Arg3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(result))) != result) goto loc_0080629C;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(result + 16, Arg2, Arg3, a4);
    }
    Arg2 = 0;
    result = KiUnstackDetachProcess(local_rsp - 984 - 32, Arg2, Arg3, a4);
    result = ExReleaseRundownProtection(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)) + 488, Arg2, Arg3, a4);
loc_008062AF:
    result = PsGetNextProcess(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6EF80B)), Arg2, Arg3, a4);
loc_008062BD:
    if (result != 0) goto loc_00805E1D;
loc_008062C9:
    Arg1 = (*(uint64_t *)(local_rsp - 0x3D8 + 0x3A0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008057A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
