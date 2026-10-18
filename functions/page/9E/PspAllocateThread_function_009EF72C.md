# PspAllocateThread

- RVA: `0x009EF72C`–`0x009F030B` (길이 `3,039` bytes)
- VA: `0x00000001409EF72C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A5CD0`
- 디코드: `607`개 명령, `3,039/3,039` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x009EF94F` → [PoEnergyEstimationEnabled](../../text/45/PoEnergyEstimationEnabled_function_00450000.md) (function, `0x00450000`)
- `0x009EF968` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (function, `0x0048B760`)
- `0x009EFA0E` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x009EFA33` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009EFAC1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009EFAF3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009EFB59` → [KeInitializeSemaphore](../../text/46/KeInitializeSemaphore_function_004660D0.md) (function, `0x004660D0`)
- `0x009EFBD6` → [KeQuerySystemTimeUnsafe](../../text/48/KeQuerySystemTimeUnsafe_function_00484438.md) (function, `0x00484438`)
- `0x009EFBEB` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (function, `0x0037DA40`)
- `0x009EFC29` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009EFC43` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009EFC59` → [PsAssignThreadId](../../text/47/PsAssignThreadId_function_004745F0.md) (function, `0x004745F0`)
- `0x009EFD16` → [PspSetupUserStack](../8C/PspSetupUserStack_function_008CD794.md) (function, `0x008CD794`)
- `0x009EFD58` → [MmCreateTeb](../98/MmCreateTeb_function_009818E4.md) (function, `0x009818E4`)
- `0x009EFE20` → [KeInitThread](../../pagelk/B7/KeInitThread_function_00B78450.md) (function, `0x00B78450`)
- `0x009EFE37` → [PsInitializeThreadRngState](../../text/48/PsInitializeThreadRngState_function_0048975C.md) (function, `0x0048975C`)
- `0x009EFE46` → [ObInitializeFastReference](../9F/ObInitializeFastReference_function_009F0D24.md) (function, `0x009F0D24`)
- `0x009EFE63` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009EFEB9` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009EFF62` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009EFFA6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009EFFE8` → [KeGetProcessorNodeNumber](../../text/43/KeGetProcessorNodeNumber_function_0043F210.md) (function, `0x0043F210`)
- `0x009F00D5` → [PspSetupUserStack](../8C/PspSetupUserStack_function_008CD794.md) (function, `0x008CD794`)
- `0x009F0112` → [PspWow64SetupUserStack](../9F/PspWow64SetupUserStack_function_009F1250.md) (function, `0x009F1250`)
- `0x009F01C4` → [KeSelectInitialIdealProcessorForThread](../../text/3C/KeSelectInitialIdealProcessorForThread_function_003C294C.md) (function, `0x003C294C`)
- `0x009F01D3` → [KeGetProcessorNodeNumberByIndex](../../text/44/KeGetProcessorNodeNumberByIndex_function_004402A0.md) (function, `0x004402A0`)
- `0x009F0260` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F028C` → [PspSetupUserShadowStack](../88/PspSetupUserShadowStack_function_008825D4.md) (function, `0x008825D4`)
- `0x009F02A4` → [PspWow64InitThread](../8C/PspWow64InitThread_function_008CDC98.md) (function, `0x008CDC98`)
- `0x009F02FD` → [MmDeleteTeb](../87/MmDeleteTeb_function_0087FAC0.md) (function, `0x0087FAC0`)

### Direct callers
- [PspCreateThread](PspCreateThread_function_009EF034.md) at `0x009EF2B2`
- [PspCreatePicoThread](../9F/PspCreatePicoThread_function_009F0D70.md) at `0x009F104F`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB47C`

### Static image references
- `0x009EF743` → RVA `0x00E0A740` (`.data`; read)
- `0x009EF8B0` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009EF8C0` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x009EF9DE` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)
- `0x009EFA57` → RVA `0x00FC6DC4` (`ALMOSTRO`; read)
- `0x009EFDAD` → RVA `0x008D5B10` (`PspUserThreadStartup`; read)
- `0x009EFF75` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x009F0075` → RVA `0x004932C0` (`PspSystemThreadStartup`; read)
- `0x009F02C4` → RVA `0x00AABDF0` (`PspSecureThreadStartup`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x009EF94F` → [PoEnergyEstimationEnabled](../../text/45/PoEnergyEstimationEnabled_function_00450000.md) (`PAGE` → `.text`)
  - `0x009EF968` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (`PAGE` → `.text`)
  - `0x009EFA33` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009EFAC1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009EFAF3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009EFB59` → [KeInitializeSemaphore](../../text/46/KeInitializeSemaphore_function_004660D0.md) (`PAGE` → `.text`)
  - `0x009EFBD6` → [KeQuerySystemTimeUnsafe](../../text/48/KeQuerySystemTimeUnsafe_function_00484438.md) (`PAGE` → `.text`)
  - `0x009EFBEB` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (`PAGE` → `.text`)
  - `0x009EFC29` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009EFC43` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009EFC59` → [PsAssignThreadId](../../text/47/PsAssignThreadId_function_004745F0.md) (`PAGE` → `.text`)
  - `0x009EFE20` → [KeInitThread](../../pagelk/B7/KeInitThread_function_00B78450.md) (`PAGE` → `PAGELK`)
  - `0x009EFE37` → [PsInitializeThreadRngState](../../text/48/PsInitializeThreadRngState_function_0048975C.md) (`PAGE` → `.text`)
  - `0x009EFE63` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009EFEB9` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009EFF62` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009EFFA6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009EFFE8` → [KeGetProcessorNodeNumber](../../text/43/KeGetProcessorNodeNumber_function_0043F210.md) (`PAGE` → `.text`)
  - `0x009F01C4` → [KeSelectInitialIdealProcessorForThread](../../text/3C/KeSelectInitialIdealProcessorForThread_function_003C294C.md) (`PAGE` → `.text`)
  - `0x009F01D3` → [KeGetProcessorNodeNumberByIndex](../../text/44/KeGetProcessorNodeNumberByIndex_function_004402A0.md) (`PAGE` → `.text`)
  - `0x009F0260` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x009EF929` → [sub_00B30C5A + 0x3D](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009EFCDF` → [sub_00B30C5A + 0x187](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009F0179` → [sub_00B30C5A](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009F0194` → [sub_00B30C5A + 0x33](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009F01B3` → [sub_00B30C5A + 0x33](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009F0257` → [sub_00B30C5A + 0xD7](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009F0266` → [sub_00B30C5A + 0xD7](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)
  - `0x009F0306` → [sub_00B30C5A + 0xE9](../B3/Unknown_function_00B30C5A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009EF72C  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
009EF731  53                              push rbx
009EF732  56                              push rsi
009EF733  57                              push rdi
009EF734  41 54                           push r12
009EF736  41 55                           push r13
009EF738  41 56                           push r14
009EF73A  41 57                           push r15
009EF73C  48 81 EC E0 01 00 00            sub rsp, 0x1e0
009EF743  48 8B 05 F6 AF 41 00            mov rax, qword ptr [rip + 0x41aff6]
009EF74A  48 33 C4                        xor rax, rsp
009EF74D  48 89 84 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rax
009EF755  49 8B D9                        mov rbx, r9
009EF758  4C 8B CA                        mov r9, rdx
009EF75B  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
009EF763  4C 8B F9                        mov r15, rcx
009EF766  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
009EF76E  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
009EF776  4C 8B AC 24 40 02 00 00         mov r13, qword ptr [rsp + 0x240]
009EF77E  4C 89 AC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r13
009EF786  4C 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r13
009EF78E  4C 89 AC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r13
009EF796  48 8B 8C 24 48 02 00 00         mov rcx, qword ptr [rsp + 0x248]
009EF79E  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
009EF7A6  4C 8B 94 24 50 02 00 00         mov r10, qword ptr [rsp + 0x250]
009EF7AE  4C 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r10
009EF7B6  4C 8B 94 24 58 02 00 00         mov r10, qword ptr [rsp + 0x258]
009EF7BE  4C 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r10
009EF7C6  48 8B 84 24 68 02 00 00         mov rax, qword ptr [rsp + 0x268]
009EF7CE  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
009EF7D6  4C 8B 84 24 70 02 00 00         mov r8, qword ptr [rsp + 0x270]
009EF7DE  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
009EF7E3  4C 8B 9C 24 78 02 00 00         mov r11, qword ptr [rsp + 0x278]
009EF7EB  4C 89 9C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r11
009EF7F3  0F 57 C0                        xorps xmm0, xmm0
009EF7F6  0F 11 84 24 A8 01 00 00         movups xmmword ptr [rsp + 0x1a8], xmm0
009EF7FE  0F 11 84 24 B8 01 00 00         movups xmmword ptr [rsp + 0x1b8], xmm0
009EF806  0F 11 84 24 C8 01 00 00         movups xmmword ptr [rsp + 0x1c8], xmm0
009EF80E  33 FF                           xor edi, edi
009EF810  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
009EF815  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
009EF81A  89 BC 24 F9 00 00 00            mov dword ptr [rsp + 0xf9], edi
009EF821  66 89 BC 24 FD 00 00 00         mov word ptr [rsp + 0xfd], di
009EF829  40 88 BC 24 FF 00 00 00         mov byte ptr [rsp + 0xff], dil
009EF831  89 BC 24 90 00 00 00            mov dword ptr [rsp + 0x90], edi
009EF838  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009EF841  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
009EF849  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
009EF84D  44 8B E7                        mov r12d, edi
009EF850  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
009EF858  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
009EF860  45 8A 87 70 01 00 00            mov r8b, byte ptr [r15 + 0x170]
009EF867  44 8D 77 01                     lea r14d, [rdi + 1]
009EF86B  45 22 C6                        and r8b, r14b
009EF86E  44 88 44 24 50                  mov byte ptr [rsp + 0x50], r8b
009EF873  44 88 44 24 58                  mov byte ptr [rsp + 0x58], r8b
009EF878  48 85 C9                        test rcx, rcx
009EF87B  0F 84 FB 05 00 00               je 0x1409efe7c
009EF881  48 8B 31                        mov rsi, qword ptr [rcx]
009EF884  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
009EF88C  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
009EF891  48 85 DB                        test rbx, rbx
009EF894  74 63                           je 0x1409ef8f9
009EF896  48 8B D7                        mov rdx, rdi
009EF899  48 8B CF                        mov rcx, rdi
009EF89C  4C 8B 43 08                     mov r8, qword ptr [rbx + 8]
009EF8A0  49 0F BA E0 0C                  bt r8, 0xc
009EF8A5  0F 82 78 08 00 00               jb 0x1409f0123
009EF8AB  BE 00 40 00 00                  mov esi, 0x4000
009EF8B0  4C 8D 15 49 07 61 FF            lea r10, [rip - 0x9ef8b7]
009EF8B7  4C 85 C6                        test rsi, r8
009EF8BA  0F 85 6F 08 00 00               jne 0x1409f012f
009EF8C0  48 0F BA 25 67 72 5D 00 37      bt qword ptr [rip + 0x5d7267], 0x37
009EF8C9  0F 82 70 08 00 00               jb 0x1409f013f
009EF8CF  49 0F BA E0 1E                  bt r8, 0x1e
009EF8D4  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
009EF8DC  0F 82 90 08 00 00               jb 0x1409f0172
009EF8E2  48 85 C9                        test rcx, rcx
009EF8E5  0F 85 C7 06 00 00               jne 0x1409effb2
009EF8EB  48 85 D2                        test rdx, rdx
009EF8EE  0F 85 C4 08 00 00               jne 0x1409f01b8
009EF8F4  44 8A 44 24 50                  mov r8b, byte ptr [rsp + 0x50]
009EF8F9  41 89 BB 80 01 00 00            mov dword ptr [r11 + 0x180], edi
009EF900  8A 94 24 30 02 00 00            mov dl, byte ptr [rsp + 0x230]
009EF907  41 88 93 84 01 00 00            mov byte ptr [r11 + 0x184], dl
009EF90E  8B DF                           mov ebx, edi
009EF910  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
009EF914  4D 85 ED                        test r13, r13
009EF917  0F 85 58 06 00 00               jne 0x1409eff75
009EF91D  4D 85 C9                        test r9, r9
009EF920  0F 84 79 05 00 00               je 0x1409efe9f
009EF926  41 3A D6                        cmp dl, r14b
009EF929  0F 84 68 13 14 00               je 0x140b30c97
009EF92F  41 8B 41 18                     mov eax, dword ptr [r9 + 0x18]
009EF933  25 F2 1F 01 00                  and eax, 0x11ff2
009EF938  41 89 83 80 01 00 00            mov dword ptr [r11 + 0x180], eax
009EF93F  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
009EF947  85 DB                           test ebx, ebx
009EF949  0F 88 4F 06 00 00               js 0x1409eff9e
009EF94F  E8 AC 06 A6 FF                  call 0x140450000
009EF954  88 44 24 58                     mov byte ptr [rsp + 0x58], al
009EF958  F6 D8                           neg al
009EF95A  1B DB                           sbb ebx, ebx
009EF95C  81 E3 C8 00 00 00               and ebx, 0xc8
009EF962  81 C3 98 07 00 00               add ebx, 0x798
009EF968  E8 F3 BD A9 FF                  call 0x14048b760
009EF96D  44 0F B7 E0                     movzx r12d, ax
009EF971  44 8B F7                        mov r14d, edi
009EF974  B8 01 00 00 00                  mov eax, 1
009EF979  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
009EF97E  66 44 3B E0                     cmp r12w, ax
009EF982  41 8B C4                        mov eax, r12d
009EF985  0F 87 6C 08 00 00               ja 0x1409f01f7
009EF98B  8D 53 07                        lea edx, [rbx + 7]
009EF98E  23 D1                           and edx, ecx
009EF990  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
009EF997  C1 E0 04                        shl eax, 4
009EF99A  83 C0 17                        add eax, 0x17
009EF99D  03 D0                           add edx, eax
009EF99F  23 D1                           and edx, ecx
009EF9A1  89 94 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edx
009EF9A8  8D 82 20 02 00 00               lea eax, [rdx + 0x220]
009EF9AE  48 F7 9C 24 98 00 00 00         neg qword ptr [rsp + 0x98]
009EF9B6  1B C9                           sbb ecx, ecx
009EF9B8  23 C8                           and ecx, eax
009EF9BA  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
009EF9C1  48 F7 9C 24 D0 00 00 00         neg qword ptr [rsp + 0xd0]
009EF9C9  1B C0                           sbb eax, eax
009EF9CB  25 D0 02 00 00                  and eax, 0x2d0
009EF9D0  05 20 02 00 00                  add eax, 0x220
009EF9D5  03 C2                           add eax, edx
009EF9D7  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
009EF9DE  48 8B 15 E3 70 5D 00            mov rdx, qword ptr [rip + 0x5d70e3]
009EF9E5  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
009EF9EA  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
009EF9EF  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009EF9F4  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
009EF9F8  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009EF9FC  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009EFA00  44 8A 8C 24 30 02 00 00         mov r9b, byte ptr [rsp + 0x230]
009EFA08  4C 8B C6                        mov r8, rsi
009EFA0B  41 8A C9                        mov cl, r9b
009EFA0E  E8 CD B7 EA FF                  call 0x14089b1e0
009EFA13  8B D8                           mov ebx, eax
009EFA15  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009EFA19  85 C0                           test eax, eax
009EFA1B  0F 88 7D 05 00 00               js 0x1409eff9e
009EFA21  44 8B 84 24 98 00 00 00         mov r8d, dword ptr [rsp + 0x98]
009EFA29  33 D2                           xor edx, edx
009EFA2B  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009EFA30  48 8B CE                        mov rcx, rsi
009EFA33  E8 08 72 CD FF                  call 0x1406c6c40
009EFA38  40 38 7C 24 58                  cmp byte ptr [rsp + 0x58], dil
009EFA3D  74 18                           je 0x1409efa57
009EFA3F  48 8D 86 98 07 00 00            lea rax, [rsi + 0x798]
009EFA46  48 89 86 88 06 00 00            mov qword ptr [rsi + 0x688], rax
009EFA4D  F0 0F BA 2E 15                  lock bts dword ptr [rsi], 0x15
009EFA52  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009EFA57  83 3D 66 73 5D 00 00            cmp dword ptr [rip + 0x5d7366], 0
009EFA5E  0F 85 A3 07 00 00               jne 0x1409f0207
009EFA64  45 85 F6                        test r14d, r14d
009EFA67  0F 85 A9 07 00 00               jne 0x1409f0216
009EFA6D  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
009EFA74  48 03 C6                        add rax, rsi
009EFA77  48 89 30                        mov qword ptr [rax], rsi
009EFA7A  C6 40 0C 06                     mov byte ptr [rax + 0xc], 6
009EFA7E  48 89 86 70 04 00 00            mov qword ptr [rsi + 0x470], rax
009EFA85  4D 85 ED                        test r13, r13
009EFA88  0F 85 6E 05 00 00               jne 0x1409efffc
009EFA8E  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
009EFA95  48 03 CE                        add rcx, rsi
009EFA98  48 89 8E 40 02 00 00            mov qword ptr [rsi + 0x240], rcx
009EFA9F  41 BE 01 00 00 00               mov r14d, 1
009EFAA5  66 44 89 31                     mov word ptr [rcx], r14w
009EFAA9  66 44 89 61 02                  mov word ptr [rcx + 2], r12w
009EFAAE  89 79 04                        mov dword ptr [rcx + 4], edi
009EFAB1  49 8B DC                        mov rbx, r12
009EFAB4  48 C1 E3 03                     shl rbx, 3
009EFAB8  48 83 C1 08                     add rcx, 8
009EFABC  4C 8B C3                        mov r8, rbx
009EFABF  33 D2                           xor edx, edx
009EFAC1  E8 7A 71 CD FF                  call 0x1406c6c40
009EFAC6  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
009EFACD  83 C2 08                        add edx, 8
009EFAD0  42 8D 0C E2                     lea ecx, [rdx + r12*8]
009EFAD4  48 03 CE                        add rcx, rsi
009EFAD7  48 89 8E 28 02 00 00            mov qword ptr [rsi + 0x228], rcx
009EFADE  66 44 89 31                     mov word ptr [rcx], r14w
009EFAE2  66 44 89 61 02                  mov word ptr [rcx + 2], r12w
009EFAE7  89 79 04                        mov dword ptr [rcx + 4], edi
009EFAEA  48 83 C1 08                     add rcx, 8
009EFAEE  4C 8B C3                        mov r8, rbx
009EFAF1  33 D2                           xor edx, edx
009EFAF3  E8 48 71 CD FF                  call 0x1406c6c40
009EFAF8  48 89 BE 88 05 00 00            mov qword ptr [rsi + 0x588], rdi
009EFAFF  49 8B 87 D0 01 00 00            mov rax, qword ptr [r15 + 0x1d0]
009EFB06  48 89 86 08 05 00 00            mov qword ptr [rsi + 0x508], rax
009EFB0D  48 8B 8C 24 60 02 00 00         mov rcx, qword ptr [rsp + 0x260]
009EFB15  8B 01                           mov eax, dword ptr [rcx]
009EFB17  A8 04                           test al, 4
009EFB19  0F 85 11 07 00 00               jne 0x1409f0230
009EFB1F  F7 01 00 02 00 00               test dword ptr [rcx], 0x200
009EFB25  0F 85 11 07 00 00               jne 0x1409f023c
009EFB2B  C7 86 04 04 00 00 20 00 00 00   mov dword ptr [rsi + 0x404], 0x20
009EFB35  48 89 BE 90 05 00 00            mov qword ptr [rsi + 0x590], rdi
009EFB3C  C7 86 98 05 00 00 0F 00 00 00   mov dword ptr [rsi + 0x598], 0xf
009EFB46  C6 86 27 07 00 00 FF            mov byte ptr [rsi + 0x727], 0xff
009EFB4D  48 8D 8E 18 05 00 00            lea rcx, [rsi + 0x518]
009EFB54  45 8B C6                        mov r8d, r14d
009EFB57  33 D2                           xor edx, edx
009EFB59  E8 72 65 A7 FF                  call 0x1404660d0
009EFB5E  48 8D 86 C8 04 00 00            lea rax, [rsi + 0x4c8]
009EFB65  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFB69  48 89 00                        mov qword ptr [rax], rax
009EFB6C  48 8D 86 F0 05 00 00            lea rax, [rsi + 0x5f0]
009EFB73  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFB77  48 89 00                        mov qword ptr [rax], rax
009EFB7A  48 8D 86 00 06 00 00            lea rax, [rsi + 0x600]
009EFB81  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFB85  48 89 00                        mov qword ptr [rax], rax
009EFB88  48 89 BE 10 06 00 00            mov qword ptr [rsi + 0x610], rdi
009EFB8F  48 8D 86 58 06 00 00            lea rax, [rsi + 0x658]
009EFB96  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFB9A  48 89 00                        mov qword ptr [rax], rax
009EFB9D  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
009EFBA1  48 8D 86 40 05 00 00            lea rax, [rsi + 0x540]
009EFBA8  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFBAC  48 89 00                        mov qword ptr [rax], rax
009EFBAF  48 89 BE 18 06 00 00            mov qword ptr [rsi + 0x618], rdi
009EFBB6  48 89 BE F0 04 00 00            mov qword ptr [rsi + 0x4f0], rdi
009EFBBD  48 8D 86 F8 04 00 00            lea rax, [rsi + 0x4f8]
009EFBC4  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFBC8  48 89 00                        mov qword ptr [rax], rax
009EFBCB  48 C7 86 98 06 00 00 FD FF FF FF  mov qword ptr [rsi + 0x698], 0xfffffffffffffffd
009EFBD6  E8 5D 48 A9 FF                  call 0x140484438
009EFBDB  48 85 C0                        test rax, rax
009EFBDE  0F 84 A0 02 00 00               je 0x1409efe84
009EFBE4  48 8D 8E C0 04 00 00            lea rcx, [rsi + 0x4c0]
009EFBEB  E8 50 DE 98 FF                  call 0x14037da40
009EFBF0  48 8D 86 B8 06 00 00            lea rax, [rsi + 0x6b8]
009EFBF7  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFBFB  48 89 00                        mov qword ptr [rax], rax
009EFBFE  48 89 BE C8 06 00 00            mov qword ptr [rsi + 0x6c8], rdi
009EFC05  48 8D 86 D0 06 00 00            lea rax, [rsi + 0x6d0]
009EFC0C  48 89 40 08                     mov qword ptr [rax + 8], rax
009EFC10  48 89 00                        mov qword ptr [rax], rax
009EFC13  48 89 BE 78 07 00 00            mov qword ptr [rsi + 0x778], rdi
009EFC1A  4C 8D A6 90 05 00 00            lea r12, [rsi + 0x590]
009EFC21  45 33 C0                        xor r8d, r8d
009EFC24  33 D2                           xor edx, edx
009EFC26  49 8B CC                        mov rcx, r12
009EFC29  E8 02 06 82 FF                  call 0x140210230
009EFC2E  48 8B D8                        mov rbx, rax
009EFC31  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
009EFC38  73 0E                           jae 0x1409efc48
009EFC3A  4D 8B C4                        mov r8, r12
009EFC3D  48 8B D0                        mov rdx, rax
009EFC40  49 8B CC                        mov rcx, r12
009EFC43  E8 48 00 82 FF                  call 0x14020fc90
009EFC48  48 85 DB                        test rbx, rbx
009EFC4B  74 04                           je 0x1409efc51
009EFC4D  44 88 73 0A                     mov byte ptr [rbx + 0xa], r14b
009EFC51  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009EFC56  48 8B CE                        mov rcx, rsi
009EFC59  E8 92 49 A8 FF                  call 0x1404745f0
009EFC5E  44 8B F0                        mov r14d, eax
009EFC61  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009EFC65  85 C0                           test eax, eax
009EFC67  0F 88 D9 05 00 00               js 0x1409f0246
009EFC6D  4D 85 ED                        test r13, r13
009EFC70  0F 84 A3 03 00 00               je 0x1409f0019
009EFC76  48 8B 84 24 60 02 00 00         mov rax, qword ptr [rsp + 0x260]
009EFC7E  44 8B 00                        mov r8d, dword ptr [rax]
009EFC81  41 0F B7 C8                     movzx ecx, r8w
009EFC85  41 BA 40 00 00 00               mov r10d, 0x40
009EFC8B  66 41 23 CA                     and cx, r10w
009EFC8F  66 C1 E1 04                     shl cx, 4
009EFC93  0F B7 D1                        movzx edx, cx
009EFC96  66 83 CA 08                     or dx, 8
009EFC9A  41 F6 C0 02                     test r8b, 2
009EFC9E  66 0F 44 D1                     cmove dx, cx
009EFCA2  41 B9 00 20 00 00               mov r9d, 0x2000
009EFCA8  0F B7 CA                        movzx ecx, dx
009EFCAB  66 41 0B C9                     or cx, r9w
009EFCAF  41 F6 C0 80                     test r8b, 0x80
009EFCB3  66 0F 44 CA                     cmove cx, dx
009EFCB7  BB 00 01 00 00                  mov ebx, 0x100
009EFCBC  44 0F B7 E1                     movzx r12d, cx
009EFCC0  BA 00 40 00 00                  mov edx, 0x4000
009EFCC5  66 44 0B E2                     or r12w, dx
009EFCC9  44 85 C3                        test ebx, r8d
009EFCCC  66 44 0F 44 E1                  cmove r12w, cx
009EFCD1  66 44 89 64 24 58               mov word ptr [rsp + 0x58], r12w
009EFCD7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009EFCDC  48 85 C9                        test rcx, rcx
009EFCDF  0F 84 FC 10 14 00               je 0x140b30de1
009EFCE5  41 85 97 54 07 00 00            test dword ptr [r15 + 0x754], edx
009EFCEC  0F 85 79 05 00 00               jne 0x1409f026b
009EFCF2  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
009EFCF6  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
009EFCFB  49 8B D5                        mov rdx, r13
009EFCFE  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009EFD02  49 83 BF 10 03 00 00 00         cmp qword ptr [r15 + 0x310], 0
009EFD0A  0F 85 92 03 00 00               jne 0x1409f00a2
009EFD10  4C 8B C9                        mov r9, rcx
009EFD13  49 8B CF                        mov rcx, r15
009EFD16  E8 79 DA ED FF                  call 0x1408cd794
009EFD1B  44 8B F0                        mov r14d, eax
009EFD1E  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009EFD22  85 C0                           test eax, eax
009EFD24  78 0D                           js 0x1409efd33
009EFD26  F7 46 74 00 00 10 00            test dword ptr [rsi + 0x74], 0x100000
009EFD2D  0F 85 42 05 00 00               jne 0x1409f0275
009EFD33  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EFD38  45 85 F6                        test r14d, r14d
009EFD3B  0F 88 C1 05 00 00               js 0x1409f0302
009EFD41  4C 8D 86 08 05 00 00            lea r8, [rsi + 0x508]
009EFD48  48 8D 44 24 78                  lea rax, [rsp + 0x78]
009EFD4D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009EFD52  48 8B D3                        mov rdx, rbx
009EFD55  49 8B CF                        mov rcx, r15
009EFD58  E8 87 1B F9 FF                  call 0x1409818e4
009EFD5D  44 8B F0                        mov r14d, eax
009EFD60  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009EFD64  85 C0                           test eax, eax
009EFD66  0F 88 96 05 00 00               js 0x1409f0302
009EFD6C  49 8B 85 F8 00 00 00            mov rax, qword ptr [r13 + 0xf8]
009EFD73  48 89 86 E0 04 00 00            mov qword ptr [rsi + 0x4e0], rax
009EFD7A  49 8B 85 80 00 00 00            mov rax, qword ptr [r13 + 0x80]
009EFD81  48 89 86 60 05 00 00            mov qword ptr [rsi + 0x560], rax
009EFD88  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
009EFD8D  49 83 BF 10 03 00 00 00         cmp qword ptr [r15 + 0x310], 0
009EFD95  0F 85 FB 04 00 00               jne 0x1409f0296
009EFD9B  66 45 85 E4                     test r12w, r12w
009EFD9F  0F 85 07 01 00 00               jne 0x1409efeac
009EFDA5  48 89 BC 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdi
009EFDAD  48 8D 05 5C 5D EE FF            lea rax, [rip - 0x11a2a4]
009EFDB4  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
009EFDBC  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009EFDC4  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
009EFDCC  48 8B 86 E0 04 00 00            mov rax, qword ptr [rsi + 0x4e0]
009EFDD3  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
009EFDDB  4C 89 AC 24 40 01 00 00         mov qword ptr [rsp + 0x140], r13
009EFDE3  48 89 9C 24 48 01 00 00         mov qword ptr [rsp + 0x148], rbx
009EFDEB  4C 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r15
009EFDF3  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
009EFDF7  89 84 24 58 01 00 00            mov dword ptr [rsp + 0x158], eax
009EFDFE  89 BC 24 5C 01 00 00            mov dword ptr [rsp + 0x15c], edi
009EFE05  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009EFE0D  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009EFE15  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
009EFE1D  48 8B CE                        mov rcx, rsi
009EFE20  E8 2B 86 18 00                  call 0x140b78450
009EFE25  44 8B F0                        mov r14d, eax
009EFE28  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009EFE2C  85 C0                           test eax, eax
009EFE2E  0F 88 B7 04 00 00               js 0x1409f02eb
009EFE34  48 8B CE                        mov rcx, rsi
009EFE37  E8 20 99 A9 FF                  call 0x14048975c
009EFE3C  48 8D 8E 90 07 00 00            lea rcx, [rsi + 0x790]
009EFE43  49 8B D7                        mov rdx, r15
009EFE46  E8 D9 0E 00 00                  call 0x1409f0d24
009EFE4B  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
009EFE53  48 89 30                        mov qword ptr [rax], rsi
009EFE56  33 C0                           xor eax, eax
009EFE58  48 8B 8C 24 D8 01 00 00         mov rcx, qword ptr [rsp + 0x1d8]
009EFE60  48 33 CC                        xor rcx, rsp
009EFE63  E8 D8 C7 CB FF                  call 0x1406ac640
009EFE68  48 81 C4 E0 01 00 00            add rsp, 0x1e0
009EFE6F  41 5F                           pop r15
009EFE71  41 5E                           pop r14
009EFE73  41 5D                           pop r13
009EFE75  41 5C                           pop r12
009EFE77  5F                              pop rdi
009EFE78  5E                              pop rsi
009EFE79  5B                              pop rbx
009EFE7A  C3                              ret
009EFE7B  CC                              int3
009EFE7C  48 8B F7                        mov rsi, rdi
009EFE7F  E9 00 FA FF FF                  jmp 0x1409ef884
009EFE84  48 A1 14 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000014]
009EFE8E  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009EFE93  48 89 86 C0 04 00 00            mov qword ptr [rsi + 0x4c0], rax
009EFE9A  E9 51 FD FF FF                  jmp 0x1409efbf0
009EFE9F  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
009EFEA7  E9 A3 FA FF FF                  jmp 0x1409ef94f
009EFEAC  4C 8D 84 24 A8 01 00 00         lea r8, [rsp + 0x1a8]
009EFEB4  33 D2                           xor edx, edx
009EFEB6  49 8B CF                        mov rcx, r15
009EFEB9  E8 62 69 82 FF                  call 0x140216820
009EFEBE  90                              nop
009EFEBF  66 44 89 A3 EE 17 00 00         mov word ptr [rbx + 0x17ee], r12w
009EFEC7  49 39 BF 10 03 00 00            cmp qword ptr [r15 + 0x310], rdi
009EFECE  74 3F                           je 0x1409eff0f
009EFED0  41 BC 64 86 00 00               mov r12d, 0x8664
009EFED6  48 8D 83 00 20 00 00            lea rax, [rbx + 0x2000]
009EFEDD  44 0F B7 44 24 58               movzx r8d, word ptr [rsp + 0x58]
009EFEE3  66 45 39 A7 EC 06 00 00         cmp word ptr [r15 + 0x6ec], r12w
009EFEEB  75 12                           jne 0x1409efeff
009EFEED  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
009EFEF5  66 44 89 80 EE 17 00 00         mov word ptr [rax + 0x17ee], r8w
009EFEFD  EB 10                           jmp 0x1409eff0f
009EFEFF  48 89 84 24 98 01 00 00         mov qword ptr [rsp + 0x198], rax
009EFF07  66 44 89 80 CA 0F 00 00         mov word ptr [rax + 0xfca], r8w
009EFF0F  44 8B F7                        mov r14d, edi
009EFF12  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
009EFF16  EB 40                           jmp 0x1409eff58
009EFF18  44 8B F0                        mov r14d, eax
009EFF1B  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009EFF1F  33 FF                           xor edi, edi
009EFF21  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
009EFF29  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009EFF2E  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009EFF36  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009EFF3E  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
009EFF43  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009EFF48  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
009EFF50  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
009EFF58  33 D2                           xor edx, edx
009EFF5A  48 8D 8C 24 A8 01 00 00         lea rcx, [rsp + 0x1a8]
009EFF62  E8 C9 7D 82 FF                  call 0x140217d30
009EFF67  45 85 F6                        test r14d, r14d
009EFF6A  0F 89 35 FE FF FF               jns 0x1409efda5
009EFF70  E9 8D 03 00 00                  jmp 0x1409f0302
009EFF75  4C 3B 3D 34 6B 5D 00            cmp r15, qword ptr [rip + 0x5d6b34]
009EFF7C  0F 84 6B 02 00 00               je 0x1409f01ed
009EFF82  41 8A C0                        mov al, r8b
009EFF85  F6 D8                           neg al
009EFF87  1B C9                           sbb ecx, ecx
009EFF89  81 E1 0D 00 00 C0               and ecx, 0xc000000d
009EFF8F  8B D9                           mov ebx, ecx
009EFF91  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
009EFF95  45 84 C0                        test r8b, r8b
009EFF98  0F 84 7F F9 FF FF               je 0x1409ef91d
009EFF9E  BA 50 73 43 72                  mov edx, 0x72437350
009EFFA3  49 8B CF                        mov rcx, r15
009EFFA6  E8 35 79 90 FF                  call 0x1402f78e0
009EFFAB  8B C3                           mov eax, ebx
009EFFAD  E9 A6 FE FF FF                  jmp 0x1409efe58
009EFFB2  48 85 D2                        test rdx, rdx
009EFFB5  0F 85 CE 01 00 00               jne 0x1409f0189
009EFFBB  49 0F BA E8 0C                  bts r8, 0xc
009EFFC0  4C 89 43 08                     mov qword ptr [rbx + 8], r8
009EFFC4  0F B6 81 D0 00 00 00            movzx eax, byte ptr [rcx + 0xd0]
009EFFCB  66 89 83 48 01 00 00            mov word ptr [rbx + 0x148], ax
009EFFD2  0F B6 81 D0 00 00 00            movzx eax, byte ptr [rcx + 0xd0]
009EFFD9  49 8B 84 C2 28 71 FC 00         mov rax, qword ptr [r10 + rax*8 + 0xfc7128]
009EFFE1  48 89 83 40 01 00 00            mov qword ptr [rbx + 0x140], rax
009EFFE8  E8 23 F2 A4 FF                  call 0x14043f210
009EFFED  0F B7 D0                        movzx edx, ax
009EFFF0  41 03 D6                        add edx, r14d
009EFFF3  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
009EFFF7  E9 F8 F8 FF FF                  jmp 0x1409ef8f4
009EFFFC  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
009F0003  48 03 C6                        add rax, rsi
009F0006  48 89 30                        mov qword ptr [rax], rsi
009F0009  C6 40 0C 08                     mov byte ptr [rax + 0xc], 8
009F000D  48 89 86 78 04 00 00            mov qword ptr [rsi + 0x478], rax
009F0014  E9 75 FA FF FF                  jmp 0x1409efa8e
009F0019  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009F0021  48 89 86 E0 04 00 00            mov qword ptr [rsi + 0x4e0], rax
009F0028  48 89 86 60 05 00 00            mov qword ptr [rsi + 0x560], rax
009F002F  48 89 BC 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdi
009F0037  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
009F003F  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
009F0047  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
009F004F  0F 57 C0                        xorps xmm0, xmm0
009F0052  66 0F 7F 84 24 40 01 00 00      movdqa xmmword ptr [rsp + 0x140], xmm0
009F005B  4C 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r15
009F0063  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
009F0067  89 84 24 58 01 00 00            mov dword ptr [rsp + 0x158], eax
009F006E  89 BC 24 5C 01 00 00            mov dword ptr [rsp + 0x15c], edi
009F0075  48 8D 05 44 32 AA FF            lea rax, [rip - 0x55cdbc]
009F007C  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
009F0084  48 8B 84 24 60 02 00 00         mov rax, qword ptr [rsp + 0x260]
009F008C  F7 00 00 04 00 00               test dword ptr [rax], 0x400
009F0092  0F 85 21 02 00 00               jne 0x1409f02b9
009F0098  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
009F009D  E9 63 FD FF FF                  jmp 0x1409efe05
009F00A2  40 88 BC 24 F8 00 00 00         mov byte ptr [rsp + 0xf8], dil
009F00AA  48 C7 84 24 08 01 00 00 00 80 00 00  mov qword ptr [rsp + 0x108], 0x8000
009F00B6  48 C7 84 24 10 01 00 00 00 00 04 00  mov qword ptr [rsp + 0x110], 0x40000
009F00C2  48 89 BC 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdi
009F00CA  4C 8D 8C 24 F8 00 00 00         lea r9, [rsp + 0xf8]
009F00D2  49 8B CF                        mov rcx, r15
009F00D5  E8 BA D6 ED FF                  call 0x1408cd794
009F00DA  44 8B F0                        mov r14d, eax
009F00DD  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009F00E1  85 C0                           test eax, eax
009F00E3  0F 88 4A FC FF FF               js 0x1409efd33
009F00E9  8A 8C 24 F8 00 00 00            mov cl, byte ptr [rsp + 0xf8]
009F00F0  80 E1 02                        and cl, 2
009F00F3  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
009F00F8  8A 02                           mov al, byte ptr [rdx]
009F00FA  24 FD                           and al, 0xfd
009F00FC  0A C8                           or cl, al
009F00FE  88 0A                           mov byte ptr [rdx], cl
009F0100  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009F0104  4C 8B CA                        mov r9, rdx
009F0107  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009F010C  4C 8B C3                        mov r8, rbx
009F010F  49 8B CF                        mov rcx, r15
009F0112  E8 39 11 00 00                  call 0x1409f1250
009F0117  44 8B F0                        mov r14d, eax
009F011A  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009F011E  E9 15 FC FF FF                  jmp 0x1409efd38
009F0123  48 8D 93 40 01 00 00            lea rdx, [rbx + 0x140]
009F012A  E9 7C F7 FF FF                  jmp 0x1409ef8ab
009F012F  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
009F0132  49 8B 8C C2 40 8C FC 00         mov rcx, qword ptr [r10 + rax*8 + 0xfc8c40]
009F013A  E9 81 F7 FF FF                  jmp 0x1409ef8c0
009F013F  4D 8B A7 98 01 00 00            mov r12, qword ptr [r15 + 0x198]
009F0146  49 F7 D4                        not r12
009F0149  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
009F0153  44 23 20                        and r12d, dword ptr [rax]
009F0156  41 81 E4 00 00 04 00            and r12d, 0x40000
009F015D  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
009F0165  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
009F016D  E9 5D F7 FF FF                  jmp 0x1409ef8cf
009F0172  49 39 BF 10 03 00 00            cmp qword ptr [r15 + 0x310], rdi
009F0179  0F 84 DB 0A 14 00               je 0x140b30c5a
009F017F  B8 0D 00 00 C0                  mov eax, 0xc000000d
009F0184  E9 CF FC FF FF                  jmp 0x1409efe58
009F0189  0F B6 81 D0 00 00 00            movzx eax, byte ptr [rcx + 0xd0]
009F0190  66 3B 42 08                     cmp ax, word ptr [rdx + 8]
009F0194  0F 85 F3 0A 14 00               jne 0x140b30c8d
009F019A  4C 8B 02                        mov r8, qword ptr [rdx]
009F019D  4D 85 C0                        test r8, r8
009F01A0  0F 84 42 FE FF FF               je 0x1409effe8
009F01A6  4C 85 81 C8 00 00 00            test qword ptr [rcx + 0xc8], r8
009F01AD  0F 85 35 FE FF FF               jne 0x1409effe8
009F01B3  E9 D5 0A 14 00                  jmp 0x140b30c8d
009F01B8  48 39 3A                        cmp qword ptr [rdx], rdi
009F01BB  0F 84 33 F7 FF FF               je 0x1409ef8f4
009F01C1  49 8B CF                        mov rcx, r15
009F01C4  E8 83 27 9D FF                  call 0x1403c294c
009F01C9  0F B7 C8                        movzx ecx, ax
009F01CC  89 4B 14                        mov dword ptr [rbx + 0x14], ecx
009F01CF  48 09 73 08                     or qword ptr [rbx + 8], rsi
009F01D3  E8 C8 00 A5 FF                  call 0x1404402a0
009F01D8  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
009F01E0  4C 8B 9C 24 C8 00 00 00         mov r11, qword ptr [rsp + 0xc8]
009F01E8  E9 00 FE FF FF                  jmp 0x1409effed
009F01ED  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009F01F2  E9 A7 FD FF FF                  jmp 0x1409eff9e
009F01F7  44 8D 73 07                     lea r14d, [rbx + 7]
009F01FB  44 23 F1                        and r14d, ecx
009F01FE  43 8D 1C E6                     lea ebx, [r14 + r12*8]
009F0202  E9 84 F7 FF FF                  jmp 0x1409ef98b
009F0207  F0 0F BA 2E 16                  lock bts dword ptr [rsi], 0x16
009F020C  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009F0211  E9 4E F8 FF FF                  jmp 0x1409efa64
009F0216  0F BA AE A0 05 00 00 11         bts dword ptr [rsi + 0x5a0], 0x11
009F021E  41 8B C6                        mov eax, r14d
009F0221  48 03 C6                        add rax, rsi
009F0224  48 89 86 90 06 00 00            mov qword ptr [rsi + 0x690], rax
009F022B  E9 3D F8 FF FF                  jmp 0x1409efa6d
009F0230  83 8E A0 05 00 00 04            or dword ptr [rsi + 0x5a0], 4
009F0237  E9 E3 F8 FF FF                  jmp 0x1409efb1f
009F023C  0F BA 6E 74 15                  bts dword ptr [rsi + 0x74], 0x15
009F0241  E9 E5 F8 FF FF                  jmp 0x1409efb2b
009F0246  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F024A  48 8B C3                        mov rax, rbx
009F024D  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
009F0253  24 06                           and al, 6
009F0255  3C 02                           cmp al, 2
009F0257  0F 85 D4 0A 14 00               jne 0x140b30d31
009F025D  49 8B CC                        mov rcx, r12
009F0260  E8 6B 5B 87 FF                  call 0x140265dd0
009F0265  90                              nop
009F0266  E9 C6 0A 14 00                  jmp 0x140b30d31
009F026B  0F BA 6E 74 14                  bts dword ptr [rsi + 0x74], 0x14
009F0270  E9 7D FA FF FF                  jmp 0x1409efcf2
009F0275  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009F0279  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
009F027E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009F0283  4C 8B C3                        mov r8, rbx
009F0286  49 8B D5                        mov rdx, r13
009F0289  49 8B CF                        mov rcx, r15
009F028C  E8 43 23 E9 FF                  call 0x1408825d4
009F0291  E9 81 FE FF FF                  jmp 0x1409f0117
009F0296  4C 8B CB                        mov r9, rbx
009F0299  4D 8B C5                        mov r8, r13
009F029C  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009F02A1  49 8B CF                        mov rcx, r15
009F02A4  E8 EF D9 ED FF                  call 0x1408cdc98
009F02A9  44 8B F0                        mov r14d, eax
009F02AC  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009F02B0  85 C0                           test eax, eax
009F02B2  78 4E                           js 0x1409f0302
009F02B4  E9 E2 FA FF FF                  jmp 0x1409efd9b
009F02B9  40 38 7C 24 50                  cmp byte ptr [rsp + 0x50], dil
009F02BE  0F 84 D4 FD FF FF               je 0x1409f0098
009F02C4  48 8D 05 25 BB 0B 00            lea rax, [rip + 0xbbb25]
009F02CB  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
009F02D3  C7 84 24 5C 01 00 00 10 00 00 00  mov dword ptr [rsp + 0x15c], 0x10
009F02DE  0F BA AE A4 05 00 00 09         bts dword ptr [rsi + 0x5a4], 9
009F02E6  E9 AD FD FF FF                  jmp 0x1409f0098
009F02EB  48 85 DB                        test rbx, rbx
009F02EE  74 12                           je 0x1409f0302
009F02F0  48 39 7C 24 70                  cmp qword ptr [rsp + 0x70], rdi
009F02F5  74 0B                           je 0x1409f0302
009F02F7  48 8B D3                        mov rdx, rbx
009F02FA  49 8B CF                        mov rcx, r15
009F02FD  E8 BE F7 E8 FF                  call 0x14087fac0
009F0302  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F0306  E9 38 0A 14 00                  jmp 0x140b30d43
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAllocateThread(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m119;
    unsigned __int16 v_stack_m11B;
    unsigned int v_stack_m11F;
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
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1BC;
    unsigned __int8 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned int v_stack_m1F0;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p150;
    unsigned int v_stack_p158;
    unsigned int v_stack_p15C;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1A8;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int16 v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;
    unsigned __int8 v_stack_pF8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 4304886)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m198 = a2;
    v_stack_m140 = a1;
    v_stack_m160 = a2;
    v_stack_m138 = a5;
    v_stack_m180 = a5;
    v_stack_m148 = a5;
    v_stack_m130 = a6;
    v_stack_m170 = a7;
    v_stack_m128 = a8;
    v_stack_m78 = a10;
    v_stack_m1A8 = a11;
    v_stack_m150 = a12;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_rdi = 0;
    v_stack_m1A0 = 0;
    v_stack_m1B0 = 0;
    v_stack_m11F = 0;
    v_stack_m11B = 0;
    v_stack_m119 = 0;
    v_stack_m188 = 0;
    v_stack_m168 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1BC = 0;
    v_stack_m190 = 0;
    v_stack_m178 = 0;
    a3 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 368)) & ((unsigned __int8)(v_rdi + 1)));
    v_stack_m1C8 = a3;
    v_stack_m1C0 = a3;
    if (a6 == 0) goto loc_009EFE7C;
loc_009EF884:
    v_stack_m158 = *(unsigned __int64 *)(a6);
    v_stack_m1B8 = *(unsigned __int64 *)(a6);
    if (a4 == 0) goto loc_009EF8F9;
    if (condition_is_below) goto loc_009F0123;
loc_009EF8AB:
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(a4 + 8))) != 0) goto loc_009F012F;
loc_009EF8C0:
    if (condition_is_below) goto loc_009F013F;
loc_009EF8CF:
    if (condition_is_below) goto loc_009F0172;
    if (0 != 0) goto loc_009EFFB2;
    if (0 != 0) goto loc_009F01B8;
loc_009EF8F4:
loc_009EF8F9:
    *(unsigned int *)(a12 + 384) = 0;
    *(unsigned __int8 *)(a12 + 388) = (unsigned __int8)(v_stack_p18);
    v_stack_m1C4 = 0;
    if (a5 != 0) goto loc_009EFF75;
loc_009EF91D:
    if (v_stack_m198 == 0) goto loc_009EFE9F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m198 + 24))) & (0x11FF2ULL));
    *(unsigned int *)(a12 + 384) = (unsigned int)(result);
    if (sign_flag) goto loc_009EFF9E;
loc_009EF94F:
    result = PoEnergyEstimationEnabled(0, v_stack_p18, v_stack_m1C8, v_stack_m198);
    v_stack_m1C0 = (unsigned __int8)(result);
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)((0) & (200));
    v_rbx = (unsigned int)((v_rbx) + (0x798ULL));
    result = KeQueryMaximumGroupCount(0, v_stack_p18, v_stack_m1C8, v_stack_m198);
    if (((unsigned __int16)((unsigned __int16)(result))) > 1) goto loc_009F01F7;
loc_009EF98B:
    a2 = (unsigned int)((v_rbx + 7) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_stack_m160 = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int16)(result)))) << (4));
    result = (unsigned int)((result) + (23));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_stack_m150 = (unsigned int)(a2);
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFF8ULL)) & ((unsigned int)(a2 + 544)));
    v_stack_m198 = (unsigned int)(a1);
    result = (unsigned int)((a2 + 544) & (720));
    result = (unsigned int)((result) + (544));
    result = (unsigned int)((result) + ((unsigned int)(a2)));
    v_stack_m180 = (unsigned int)(result);
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m1B0;
    v_stack_m1E0 = (unsigned int)(result);
    v_stack_m1E8 = 0;
    v_stack_m1F0 = (unsigned int)(result);
    result = ObCreateObjectEx((unsigned __int8)(v_stack_p18), *(unsigned __int64 *)(v_rip + 6123747), v_stack_m198, v_stack_p18);
    v_stack_m1C4 = (unsigned int)(result);
    if (sign_flag) goto loc_009EFF9E;
    a2 = 0;
    result = memset(v_stack_m1B0, a2, (unsigned int)(v_stack_m180), v_stack_p18);
    v_rsi = v_stack_m1B0;
    if (v_stack_m1C0 != 0) {
        result = v_stack_m1B0 + 1944;
        *(unsigned __int64 *)(v_stack_m1B0 + 1672) = result;
        v_rsi = v_stack_m1B0;
    }
    if ((*(unsigned int *)(v_rip + 6124390)) != 0) goto loc_009F0207;
loc_009EFA64:
    if (0 != 0) goto loc_009F0216;
loc_009EFA6D:
    result = ((unsigned int)(v_stack_m150)) + (v_rsi);
    *(unsigned __int64 *)(result) = v_rsi;
    *(unsigned __int8 *)(result + 12) = 6;
    *(unsigned __int64 *)(v_rsi + 1136) = result;
    if (a5 != 0) goto loc_009EFFFC;
loc_009EFA8E:
    a1 = ((unsigned int)(v_stack_m160)) + (v_rsi);
    *(unsigned __int64 *)(v_rsi + 576) = a1;
    *(unsigned __int16 *)(a1) = 1;
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)((unsigned __int16)(result));
    *(unsigned int *)(a1 + 4) = 0;
    v_rbx = ((unsigned __int16)(result)) << (3);
    a1 = (a1) + (8);
    a2 = 0;
    result = memset(a1, a2, v_rbx, v_stack_p18);
    a2 = (unsigned int)(((unsigned int)(v_stack_m160)) + (8));
    a1 = (a2 + (unsigned __int16)(result) * 8) + (v_rsi);
    *(unsigned __int64 *)(v_rsi + 552) = a1;
    *(unsigned __int16 *)(a1) = 1;
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)((unsigned __int16)(result));
    *(unsigned int *)(a1 + 4) = 0;
    a1 = (a1) + (8);
    a2 = 0;
    result = memset(a1, a2, v_rbx, v_stack_p18);
    *(unsigned __int64 *)(v_rsi + 1416) = 0;
    *(unsigned __int64 *)(v_rsi + 1288) = *(unsigned __int64 *)(a1 + 464);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a9)))) & (4)) != 0) goto loc_009F0230;
loc_009EFB1F:
    if (((*(unsigned int *)(a9)) & (512)) != 0) goto loc_009F023C;
loc_009EFB2B:
    *(unsigned int *)(v_rsi + 1028) = 32;
    *(unsigned __int64 *)(v_rsi + 1424) = 0;
    *(unsigned int *)(v_rsi + 1432) = 15;
    *(unsigned __int8 *)(v_rsi + 1831) = 255;
    a2 = 0;
    result = KeInitializeSemaphore(v_rsi + 1304, a2, 1, v_stack_p18);
    *(unsigned __int64 *)(v_rsi + 1224 + 8) = v_rsi + 1224;
    *(unsigned __int64 *)(v_rsi + 1224) = v_rsi + 1224;
    *(unsigned __int64 *)(v_rsi + 1520 + 8) = v_rsi + 1520;
    *(unsigned __int64 *)(v_rsi + 1520) = v_rsi + 1520;
    *(unsigned __int64 *)(v_rsi + 1536 + 8) = v_rsi + 1536;
    *(unsigned __int64 *)(v_rsi + 1536) = v_rsi + 1536;
    *(unsigned __int64 *)(v_rsi + 1552) = 0;
    *(unsigned __int64 *)(v_rsi + 1624 + 8) = v_rsi + 1624;
    *(unsigned __int64 *)(v_rsi + 1624) = v_rsi + 1624;
    *(unsigned __int64 *)(v_rsi + 1624 + 16) = 0;
    *(unsigned __int64 *)(v_rsi + 1344 + 8) = v_rsi + 1344;
    *(unsigned __int64 *)(v_rsi + 1344) = v_rsi + 1344;
    *(unsigned __int64 *)(v_rsi + 1560) = 0;
    *(unsigned __int64 *)(v_rsi + 1264) = 0;
    *(unsigned __int64 *)(v_rsi + 1272 + 8) = v_rsi + 1272;
    *(unsigned __int64 *)(v_rsi + 1272) = v_rsi + 1272;
    *(unsigned __int64 *)(v_rsi + 1688) = -3;
    result = KeQuerySystemTimeUnsafe(v_rsi + 1304, a2, 1, v_stack_p18);
    if (result == 0) goto loc_009EFE84;
    result = KeQuerySystemTimePrecise(v_rsi + 1216, a2, 1, v_stack_p18);
loc_009EFBF0:
    *(unsigned __int64 *)(v_rsi + 1720 + 8) = v_rsi + 1720;
    *(unsigned __int64 *)(v_rsi + 1720) = v_rsi + 1720;
    *(unsigned __int64 *)(v_rsi + 1736) = 0;
    *(unsigned __int64 *)(v_rsi + 1744 + 8) = v_rsi + 1744;
    *(unsigned __int64 *)(v_rsi + 1744) = v_rsi + 1744;
    *(unsigned __int64 *)(v_rsi + 1912) = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rsi + 1424, a2, a3, v_stack_p18);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rsi + 1424;
        a2 = result;
        a1 = v_rsi + 1424;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_p18);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = PsAssignThreadId(v_stack_m1B0, a2, a3, v_stack_p18);
    v_stack_m1C4 = (unsigned int)(result);
    if (sign_flag) goto loc_009F0246;
    if (a5 == 0) goto loc_009F0019;
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)(a9)))) & (64));
    a1 = (unsigned __int16)((a1) << (4));
    a2 = (unsigned __int16)(((unsigned __int16)(a1)) | (8));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a9)))) & (2)) == 0) { a2 = (unsigned __int16)(a1); }
    a1 = (unsigned __int16)(((unsigned __int16)(a2)) | ((unsigned __int16)((unsigned int)(0x2000ULL))));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a9)))) & (128)) == 0) { a1 = (unsigned __int16)(a2); }
    v_r12 = (unsigned __int16)(((unsigned __int16)(a1)) | ((unsigned __int16)((unsigned int)(0x4000ULL))));
    if (((256) & ((unsigned int)((unsigned int)(*(unsigned int *)(a9))))) == 0) { v_r12 = (unsigned __int16)(a1); }
    v_stack_m1C0 = (unsigned __int16)(v_r12);
    if (((*(unsigned int *)(a1 + 1876)) & ((unsigned int)((unsigned int)(0x4000ULL)))) != 0) goto loc_009F026B;
loc_009EFCF2:
    v_stack_m1F8 = (unsigned int)((unsigned int)(v_stack_m1BC));
    if ((*(unsigned __int64 *)(a1 + 784)) != 0) goto loc_009F00A2;
    result = PspSetupUserStack(a1, a5, v_stack_m1B8, v_stack_m1A8);
    v_stack_m1C4 = (unsigned int)(result);
    if (sign_flag) goto loc_009EFD33;
    if (((*(unsigned int *)(v_stack_m1B0 + 116)) & (0x100000ULL)) != 0) goto loc_009F0275;
loc_009EFD33:
loc_009EFD38:
    if (sign_flag) goto loc_009F0302;
    v_stack_m1F8 = v_stack_m1A0;
    result = MmCreateTeb(a1, v_stack_m1B8, v_stack_m1B0 + 1288, v_stack_m1A8);
    v_stack_m1C4 = (unsigned int)(result);
    if (sign_flag) goto loc_009F0302;
    *(unsigned __int64 *)(v_stack_m1B0 + 1248) = *(unsigned __int64 *)(a5 + 248);
    *(unsigned __int64 *)(v_stack_m1B0 + 1376) = *(unsigned __int64 *)(a5 + 128);
    if ((*(unsigned __int64 *)(a1 + 784)) != 0) goto loc_009F0296;
loc_009EFD9B:
    if ((unsigned __int16)(v_r12) != 0) goto loc_009EFEAC;
loc_009EFDA5:
    v_stack_mF8 = 0;
    v_stack_mF0 = v_rip - 1155748;
    v_stack_mE8 = v_stack_m170;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m1B0 + 1248);
    v_stack_mD8 = a5;
    v_stack_mD0 = v_stack_m1A0;
    v_stack_mC8 = a1;
    v_stack_mC0 = (unsigned int)((unsigned int)(v_stack_m1BC));
    v_stack_mBC = 0;
loc_009EFE05:
    v_stack_mB8 = v_stack_m190;
    result = KeInitThread(v_stack_m1B0, v_stack_mF8, v_stack_m1B0 + 1288, v_stack_m1A8);
    v_stack_m1C4 = (unsigned int)(result);
    if (sign_flag) goto loc_009F02EB;
    result = PsInitializeThreadRngState(v_stack_m1B0, v_stack_mF8, v_stack_m1B0 + 1288, v_stack_m1A8);
    result = ObInitializeFastReference(v_stack_m1B0 + 1936, a1, v_stack_m1B0 + 1288, v_stack_m1A8);
    *(unsigned __int64 *)(v_stack_m78) = v_stack_m1B0;
    result = 0;
loc_009EFE58:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a1, v_stack_m1B0 + 1288, v_stack_m1A8);
    v_rsp = (v_rsp) + (480);
    return result;
loc_009EFE7C:
    goto loc_009EF884;
loc_009EFE84:
    *(unsigned __int64 *)(v_stack_p68 + 1216) = result;
    goto loc_009EFBF0;
loc_009EFE9F:
    goto loc_009EF94F;
loc_009EFEAC:
    a2 = 0;
    result = KiStackAttachProcess(a1, a2, v_stack_p1A8, v_stack_m1A8);
    *(unsigned __int16 *)(v_stack_m1A0 + 6126) = (unsigned __int16)(v_r12);
    if ((*(unsigned __int64 *)(a1 + 784)) == 0) goto loc_009EFF0F;
    if ((*(unsigned __int16 *)(a1 + 1772)) != ((unsigned __int16)((unsigned int)(0x8664ULL)))) goto loc_009EFEFF;
    v_stack_p190 = v_stack_m1A0 + 8192;
    *(unsigned __int16 *)(v_stack_m1A0 + 8192 + 6126) = (unsigned __int16)(v_stack_p58);
    goto loc_009EFF0F;
loc_009EFEFF:
    v_stack_p198 = v_stack_m1A0 + 8192;
    *(unsigned __int16 *)(v_stack_m1A0 + 8192 + 4042) = (unsigned __int16)(v_stack_p58);
loc_009EFF0F:
    v_stack_p54 = 0;
    goto loc_009EFF58;
loc_009EFF58:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_p1A8, a2, v_stack_p58, v_stack_m1A8);
    if (!sign_flag) goto loc_009EFDA5;
    goto loc_009F0302;
loc_009EFF75:
    if (a1 == (*(unsigned __int64 *)(v_rip + 6122292))) goto loc_009F01ED;
    result = (unsigned __int8)(-((unsigned __int8)(v_stack_p58)));
    a1 = (unsigned int)((v_stack_p1A8) & (0xC000000DULL));
    v_stack_p54 = (unsigned int)(a1);
    if ((unsigned __int8)(v_stack_p58) == 0) goto loc_009EF91D;
loc_009EFF9E:
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x72437350ULL), v_stack_p58, v_stack_m1A8);
    goto loc_009EFE58;
loc_009EFFB2:
    if ((unsigned int)(0x72437350ULL) != 0) goto loc_009F0189;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(a1)) + 8) = v_stack_p58;
    *(unsigned __int16 *)((unsigned int)((unsigned int)(a1)) + 328) = (unsigned __int16)(*(unsigned __int8 *)(a1 + 208));
    *(unsigned __int64 *)((unsigned int)((unsigned int)(a1)) + 320) = *(unsigned __int64 *)(64 + *(unsigned __int8 *)(a1 + 208) * 8 + 16544040);
loc_009EFFE8:
    result = KeGetProcessorNodeNumber(a1, (unsigned int)(0x72437350ULL), v_stack_p58, v_stack_m1A8);
loc_009EFFED:
    a2 = (unsigned int)(((unsigned __int16)(result)) + (0));
    v_stack_p5C = (unsigned int)(a2);
    goto loc_009EF8F4;
loc_009EFFFC:
    result = ((unsigned int)(v_stack_p80)) + (v_stack_p80);
    *(unsigned __int64 *)(result) = v_stack_p80;
    *(unsigned __int8 *)(result + 12) = 8;
    *(unsigned __int64 *)(v_stack_p80 + 1144) = result;
    goto loc_009EFA8E;
loc_009F0019:
    *(unsigned __int64 *)(v_stack_p80 + 1248) = v_stack_pA8;
    *(unsigned __int64 *)(v_stack_p80 + 1376) = v_stack_pA8;
    v_stack_p120 = 0;
    v_stack_p130 = v_stack_pA8;
    v_stack_p138 = v_stack_pF0;
    v_stack_p140 = v_xmm0;
    v_stack_p150 = a1;
    v_stack_p158 = (unsigned int)((unsigned int)(v_stack_p5C));
    v_stack_p15C = 0;
    v_stack_p128 = v_rip - 5623228;
    if (((*(unsigned int *)(a9)) & (0x400ULL)) != 0) goto loc_009F02B9;
loc_009F0098:
    goto loc_009EFE05;
loc_009F00A2:
    v_stack_pF8 = 0;
    v_stack_p108 = 0x8000ULL;
    v_stack_p110 = 0x40000ULL;
    v_stack_p100 = 0;
    result = PspSetupUserStack(a1, a2, v_stack_p58, v_stack_pF8);
    v_stack_p54 = (unsigned int)(result);
    if (sign_flag) goto loc_009EFD33;
    a1 = (unsigned __int8)((v_stack_pF8) & (2));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p70)) & (253));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_stack_p70) = (unsigned __int8)(a1);
    v_stack_p20 = (unsigned int)(v_stack_p78);
    result = PspWow64SetupUserStack(a1, v_stack_p70, v_stack_p60, v_stack_p70);
loc_009F0117:
    v_stack_p54 = (unsigned int)(result);
    goto loc_009EFD38;
loc_009F0123:
    goto loc_009EF8AB;
loc_009F012F:
    goto loc_009EF8C0;
loc_009F013F:
    v_r12 = ~(*(unsigned __int64 *)(a1 + 408));
    v_r12 = (unsigned int)((v_r12) & (*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p60 + 20)))));
    v_r12 = (unsigned int)((v_r12) & (0x40000ULL));
    v_stack_p88 = v_r12;
    v_stack_pA0 = v_r12;
    goto loc_009EF8CF;
loc_009F0172:
    goto loc_009EFE58;
loc_009F0189:
    if (*(unsigned __int64 *)(v_stack_p60 + 320) == 0) goto loc_009EFFE8;
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(64 + (unsigned int)(*(unsigned int *)(v_stack_p60 + 20)) * 8 + 16550976) + 200)) & (*(unsigned __int64 *)(v_stack_p60 + 320))) != 0) goto loc_009EFFE8;
loc_009F01B8:
    if ((*(unsigned __int64 *)(v_stack_p60 + 320)) == 0) goto loc_009EF8F4;
    result = KeSelectInitialIdealProcessorForThread(a1, v_stack_p60 + 320, *(unsigned __int64 *)(v_stack_p60 + 320), v_stack_p70);
    *(unsigned int *)(v_stack_p60 + 20) = (unsigned int)((unsigned __int16)(result));
    result = KeGetProcessorNodeNumberByIndex((unsigned __int16)(result), v_stack_p60 + 320, *(unsigned __int64 *)(v_stack_p60 + 320), v_stack_p70);
    goto loc_009EFFED;
loc_009F01ED:
    goto loc_009EFF9E;
loc_009F01F7:
    v_r14 = (unsigned int)(((unsigned int)(0xC000000DULL) + 7) & ((unsigned int)((unsigned __int16)(result))));
    goto loc_009EF98B;
loc_009F0207:
    goto loc_009EFA64;
loc_009F0216:
    result = ((unsigned int)((unsigned int)(v_r14))) + (v_stack_p68);
    *(unsigned __int64 *)(v_stack_p68 + 1680) = result;
    goto loc_009EFA6D;
loc_009F0230:
    goto loc_009EFB1F;
loc_009F023C:
    goto loc_009EFB2B;
loc_009F0246:
    v_rbx = (v_r14 + v_r12 * 8) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    result = ExfTryToWakePushLock(v_r12, v_stack_p60 + 320, *(unsigned __int64 *)(v_stack_p60 + 320), v_stack_p80);
loc_009F026B:
    goto loc_009EFCF2;
loc_009F0275:
    v_stack_p20 = (unsigned int)(v_rbx);
    result = PspSetupUserShadowStack(a1, a5, v_stack_p60, v_stack_p70);
    goto loc_009F0117;
loc_009F0296:
    result = PspWow64InitThread(a1, v_stack_p60, a5, v_stack_p60);
    v_stack_p54 = (unsigned int)(result);
    if (sign_flag) goto loc_009F0302;
    goto loc_009EFD9B;
loc_009F02B9:
    if (v_stack_p50 == 0) goto loc_009F0098;
    v_stack_p128 = v_rip + 768805;
    v_stack_p15C = 16;
    goto loc_009F0098;
loc_009F02EB:
    if (v_stack_p60 == 0) goto loc_009F0302;
    result = v_rip + 768805;
    if (v_stack_p70 != 0) {
        a2 = v_stack_p60;
        a1 = a1;
        result = MmDeleteTeb(a1, a2, a5, v_stack_p60);
    }
    v_rbx = (v_stack_p60) | (-1);
}
```

## 5. (Beta) C Style

```c
int64_t PspAllocateThread(void *Arg1, int64_t Arg2, uint8_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, void *Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m119;
    uint16_t v_stack_m11B;
    uint32_t v_stack_m11F;
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
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1BC;
    uint8_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint32_t v_stack_m1F0;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p150;
    uint32_t v_stack_p158;
    uint32_t v_stack_p15C;
    uint8_t v_stack_p18;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1A8;
    uint32_t v_stack_p20;
    uint8_t v_stack_p50;
    uint32_t v_stack_p54;
    uint16_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;
    uint8_t v_stack_pF8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0x41AFF6)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m198 = Arg2;
    v_stack_m140 = Arg1;
    v_stack_m160 = Arg2;
    v_stack_m138 = Arg5;
    v_stack_m180 = Arg5;
    v_stack_m148 = Arg5;
    v_stack_m130 = Arg6;
    v_stack_m170 = Arg7;
    v_stack_m128 = Arg8;
    v_stack_m78 = Arg10;
    v_stack_m1A8 = Arg11;
    v_stack_m150 = Arg12;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    local_rdi = 0;
    v_stack_m1A0 = 0;
    v_stack_m1B0 = 0;
    v_stack_m11F = 0;
    v_stack_m11B = 0;
    v_stack_m119 = 0;
    v_stack_m188 = 0;
    v_stack_m168 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1BC = 0;
    v_stack_m190 = 0;
    v_stack_m178 = 0;
    Arg3 = (uint8_t)((*(uint8_t *)(arg1 + 0x170)) & ((uint8_t)(local_rdi + 1)));
    v_stack_m1C8 = Arg3;
    v_stack_m1C0 = Arg3;
    if (Arg6 == 0) goto loc_009EFE7C;
loc_009EF884:
    v_stack_m158 = *(uint64_t *)(Arg6);
    v_stack_m1B8 = *(uint64_t *)(Arg6);
    if (Arg4 == 0) goto loc_009EF8F9;
    if (condition_is_below) goto loc_009F0123;
loc_009EF8AB:
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(Arg4 + 0x8))) != 0) goto loc_009F012F;
loc_009EF8C0:
    if (condition_is_below) goto loc_009F013F;
loc_009EF8CF:
    if (condition_is_below) goto loc_009F0172;
    if (0 != 0) goto loc_009EFFB2;
    if (0 != 0) goto loc_009F01B8;
loc_009EF8F4:
loc_009EF8F9:
    *(uint32_t *)(Arg12 + 0x180) = 0;
    *(uint8_t *)(Arg12 + 0x184) = (uint8_t)(v_stack_p18);
    v_stack_m1C4 = 0;
    if (Arg5 != 0) goto loc_009EFF75;
loc_009EF91D:
    if (v_stack_m198 == 0) goto loc_009EFE9F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x18))) & (0x11FF2ULL));
    *(uint32_t *)(Arg12 + 0x180) = (uint32_t)(result);
    if (sign_flag) goto loc_009EFF9E;
loc_009EF94F:
    result = PoEnergyEstimationEnabled(0, v_stack_p18, v_stack_m1C8, v_stack_m198);
    v_stack_m1C0 = (uint8_t)(result);
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)((0) & (200));
    local_rbx = (uint32_t)((local_rbx) + (0x798ULL));
    result = KeQueryMaximumGroupCount(0, v_stack_p18, v_stack_m1C8, v_stack_m198);
    if (((uint16_t)((uint16_t)(result))) > 1) goto loc_009F01F7;
loc_009EF98B:
    Arg2 = (uint32_t)((local_rbx + 7) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    v_stack_m160 = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint16_t)(result)))) << (4));
    result = (uint32_t)((result) + (23));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    v_stack_m150 = (uint32_t)(Arg2);
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFF8ULL)) & ((uint32_t)(Arg2 + 544)));
    v_stack_m198 = (uint32_t)(Arg1);
    result = (uint32_t)((Arg2 + 544) & (720));
    result = (uint32_t)((result) + (544));
    result = (uint32_t)((result) + ((uint32_t)(Arg2)));
    v_stack_m180 = (uint32_t)(result);
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m1B0;
    v_stack_m1E0 = (uint32_t)(result);
    v_stack_m1E8 = 0;
    v_stack_m1F0 = (uint32_t)(result);
    result = ObCreateObjectEx((uint8_t)(v_stack_p18), *(uint64_t *)(v_rip + 0x5D70E3), v_stack_m198, v_stack_p18);
    v_stack_m1C4 = (uint32_t)(result);
    if (sign_flag) goto loc_009EFF9E;
    Arg2 = 0;
    result = memset(v_stack_m1B0, Arg2, (uint32_t)(v_stack_m180), v_stack_p18);
    local_rsi = v_stack_m1B0;
    if (v_stack_m1C0 != 0) {
        result = v_stack_m1B0 + 1944;
        *(uint64_t *)(v_stack_m1B0 + 0x688) = result;
        local_rsi = v_stack_m1B0;
    }
    if ((*(uint32_t *)(v_rip + 0x5D7366)) != 0) goto loc_009F0207;
loc_009EFA64:
    if (0 != 0) goto loc_009F0216;
loc_009EFA6D:
    result = ((uint32_t)(v_stack_m150)) + (local_rsi);
    *(uint64_t *)(result) = local_rsi;
    *(uint8_t *)(result + 0xC) = 6;
    *(uint64_t *)(local_rsi + 0x470) = result;
    if (Arg5 != 0) goto loc_009EFFFC;
loc_009EFA8E:
    Arg1 = ((uint32_t)(v_stack_m160)) + (local_rsi);
    *(void **)(local_rsi + 0x240) = Arg1;
    *(uint16_t *)(arg1) = 1;
    *(uint16_t *)(arg1 + 0x2) = (uint16_t)((uint16_t)(result));
    *(uint32_t *)(arg1 + 0x4) = 0;
    local_rbx = ((uint16_t)(result)) << (3);
    Arg1 = (Arg1) + (8);
    Arg2 = 0;
    result = memset(Arg1, Arg2, local_rbx, v_stack_p18);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m160)) + (8));
    Arg1 = (Arg2 + (uint16_t)(result) * 8) + (local_rsi);
    *(void **)(local_rsi + 0x228) = Arg1;
    *(uint16_t *)(arg1) = 1;
    *(uint16_t *)(arg1 + 0x2) = (uint16_t)((uint16_t)(result));
    *(uint32_t *)(arg1 + 0x4) = 0;
    Arg1 = (Arg1) + (8);
    Arg2 = 0;
    result = memset(Arg1, Arg2, local_rbx, v_stack_p18);
    *(uint64_t *)(local_rsi + 0x588) = 0;
    *(uint64_t *)(local_rsi + 0x508) = *(uint64_t *)(arg1 + 0x1D0);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg9)))) & (4)) != 0) goto loc_009F0230;
loc_009EFB1F:
    if (((*(uint32_t *)(arg9)) & (512)) != 0) goto loc_009F023C;
loc_009EFB2B:
    *(uint32_t *)(local_rsi + 0x404) = 32;
    *(uint64_t *)(local_rsi + 0x590) = 0;
    *(uint32_t *)(local_rsi + 0x598) = 15;
    *(uint8_t *)(local_rsi + 0x727) = 255;
    Arg2 = 0;
    result = KeInitializeSemaphore(local_rsi + 1304, Arg2, 1, v_stack_p18);
    *(uint64_t *)(local_rsi + 0x4C8 + 0x8) = local_rsi + 1224;
    *(uint64_t *)(local_rsi + 0x4C8) = local_rsi + 1224;
    *(uint64_t *)(local_rsi + 0x5F0 + 0x8) = local_rsi + 1520;
    *(uint64_t *)(local_rsi + 0x5F0) = local_rsi + 1520;
    *(uint64_t *)(local_rsi + 0x600 + 0x8) = local_rsi + 1536;
    *(uint64_t *)(local_rsi + 0x600) = local_rsi + 1536;
    *(uint64_t *)(local_rsi + 0x610) = 0;
    *(uint64_t *)(local_rsi + 0x658 + 0x8) = local_rsi + 1624;
    *(uint64_t *)(local_rsi + 0x658) = local_rsi + 1624;
    *(uint64_t *)(local_rsi + 0x658 + 0x10) = 0;
    *(uint64_t *)(local_rsi + 0x540 + 0x8) = local_rsi + 1344;
    *(uint64_t *)(local_rsi + 0x540) = local_rsi + 1344;
    *(uint64_t *)(local_rsi + 0x618) = 0;
    *(uint64_t *)(local_rsi + 0x4F0) = 0;
    *(uint64_t *)(local_rsi + 0x4F8 + 0x8) = local_rsi + 1272;
    *(uint64_t *)(local_rsi + 0x4F8) = local_rsi + 1272;
    *(uint64_t *)(local_rsi + 0x698) = -3;
    result = KeQuerySystemTimeUnsafe(local_rsi + 1304, Arg2, 1, v_stack_p18);
    if (result == 0) goto loc_009EFE84;
    result = KeQuerySystemTimePrecise(local_rsi + 1216, Arg2, 1, v_stack_p18);
loc_009EFBF0:
    *(uint64_t *)(local_rsi + 0x6B8 + 0x8) = local_rsi + 1720;
    *(uint64_t *)(local_rsi + 0x6B8) = local_rsi + 1720;
    *(uint64_t *)(local_rsi + 0x6C8) = 0;
    *(uint64_t *)(local_rsi + 0x6D0 + 0x8) = local_rsi + 1744;
    *(uint64_t *)(local_rsi + 0x6D0) = local_rsi + 1744;
    *(uint64_t *)(local_rsi + 0x778) = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rsi + 1424, Arg2, Arg3, v_stack_p18);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rsi + 1424;
        Arg2 = result;
        Arg1 = local_rsi + 1424;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_p18);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = PsAssignThreadId(v_stack_m1B0, Arg2, Arg3, v_stack_p18);
    v_stack_m1C4 = (uint32_t)(result);
    if (sign_flag) goto loc_009F0246;
    if (Arg5 == 0) goto loc_009F0019;
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)(arg9)))) & (64));
    Arg1 = (uint16_t)((Arg1) << (4));
    Arg2 = (uint16_t)(((uint16_t)(Arg1)) | (8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg9)))) & (2)) == 0) { Arg2 = (uint16_t)(Arg1); }
    Arg1 = (uint16_t)(((uint16_t)(Arg2)) | ((uint16_t)((uint32_t)(0x2000ULL))));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg9)))) & (128)) == 0) { Arg1 = (uint16_t)(Arg2); }
    local_r12 = (uint16_t)(((uint16_t)(Arg1)) | ((uint16_t)((uint32_t)(0x4000ULL))));
    if (((256) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg9))))) == 0) { local_r12 = (uint16_t)(Arg1); }
    v_stack_m1C0 = (uint16_t)(local_r12);
    if (((*(uint32_t *)(arg1 + 0x754)) & ((uint32_t)((uint32_t)(0x4000ULL)))) != 0) goto loc_009F026B;
loc_009EFCF2:
    v_stack_m1F8 = (uint32_t)((uint32_t)(v_stack_m1BC));
    if ((*(uint64_t *)(arg1 + 0x310)) != 0) goto loc_009F00A2;
    result = PspSetupUserStack(Arg1, Arg5, v_stack_m1B8, v_stack_m1A8);
    v_stack_m1C4 = (uint32_t)(result);
    if (sign_flag) goto loc_009EFD33;
    if (((*(uint32_t *)(v_stack_m1B0 + 0x74)) & (0x100000ULL)) != 0) goto loc_009F0275;
loc_009EFD33:
loc_009EFD38:
    if (sign_flag) goto loc_009F0302;
    v_stack_m1F8 = v_stack_m1A0;
    result = MmCreateTeb(Arg1, v_stack_m1B8, v_stack_m1B0 + 1288, v_stack_m1A8);
    v_stack_m1C4 = (uint32_t)(result);
    if (sign_flag) goto loc_009F0302;
    *(uint64_t *)(v_stack_m1B0 + 0x4E0) = *(uint64_t *)(Arg5 + 0xF8);
    *(uint64_t *)(v_stack_m1B0 + 0x560) = *(uint64_t *)(Arg5 + 0x80);
    if ((*(uint64_t *)(arg1 + 0x310)) != 0) goto loc_009F0296;
loc_009EFD9B:
    if ((uint16_t)(local_r12) != 0) goto loc_009EFEAC;
loc_009EFDA5:
    v_stack_mF8 = 0;
    v_stack_mF0 = v_rip - 1155748;
    v_stack_mE8 = v_stack_m170;
    v_stack_mE0 = *(uint64_t *)(v_stack_m1B0 + 0x4E0);
    v_stack_mD8 = Arg5;
    v_stack_mD0 = v_stack_m1A0;
    v_stack_mC8 = Arg1;
    v_stack_mC0 = (uint32_t)((uint32_t)(v_stack_m1BC));
    v_stack_mBC = 0;
loc_009EFE05:
    v_stack_mB8 = v_stack_m190;
    result = KeInitThread(v_stack_m1B0, v_stack_mF8, v_stack_m1B0 + 1288, v_stack_m1A8);
    v_stack_m1C4 = (uint32_t)(result);
    if (sign_flag) goto loc_009F02EB;
    result = PsInitializeThreadRngState(v_stack_m1B0, v_stack_mF8, v_stack_m1B0 + 1288, v_stack_m1A8);
    result = ObInitializeFastReference(v_stack_m1B0 + 1936, Arg1, v_stack_m1B0 + 1288, v_stack_m1A8);
    *(uint64_t *)(v_stack_m78) = v_stack_m1B0;
    result = 0;
loc_009EFE58:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1, v_stack_m1B0 + 1288, v_stack_m1A8);
    local_rsp = (local_rsp) + (480);
    return result;
loc_009EFE7C:
    goto loc_009EF884;
loc_009EFE84:
    *(uint64_t *)(v_stack_p68 + 0x4C0) = result;
    goto loc_009EFBF0;
loc_009EFE9F:
    goto loc_009EF94F;
loc_009EFEAC:
    Arg2 = 0;
    result = KiStackAttachProcess(Arg1, Arg2, v_stack_p1A8, v_stack_m1A8);
    *(uint16_t *)(v_stack_m1A0 + 0x17EE) = (uint16_t)(local_r12);
    if ((*(uint64_t *)(arg1 + 0x310)) == 0) goto loc_009EFF0F;
    if ((*(uint16_t *)(arg1 + 0x6EC)) != ((uint16_t)((uint32_t)(0x8664ULL)))) goto loc_009EFEFF;
    v_stack_p190 = v_stack_m1A0 + 8192;
    *(uint16_t *)(v_stack_m1A0 + 0x2000 + 0x17EE) = (uint16_t)(v_stack_p58);
    goto loc_009EFF0F;
loc_009EFEFF:
    v_stack_p198 = v_stack_m1A0 + 8192;
    *(uint16_t *)(v_stack_m1A0 + 0x2000 + 0xFCA) = (uint16_t)(v_stack_p58);
loc_009EFF0F:
    v_stack_p54 = 0;
    goto loc_009EFF58;
loc_009EFF58:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_p1A8, Arg2, v_stack_p58, v_stack_m1A8);
    if (!sign_flag) goto loc_009EFDA5;
    goto loc_009F0302;
loc_009EFF75:
    if (Arg1 == (*(uint64_t *)(v_rip + 0x5D6B34))) goto loc_009F01ED;
    result = (uint8_t)(-((uint8_t)(v_stack_p58)));
    Arg1 = (uint32_t)((v_stack_p1A8) & (0xC000000DULL));
    v_stack_p54 = (uint32_t)(Arg1);
    if ((uint8_t)(v_stack_p58) == 0) goto loc_009EF91D;
loc_009EFF9E:
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x72437350ULL), v_stack_p58, v_stack_m1A8);
    goto loc_009EFE58;
loc_009EFFB2:
    if ((uint32_t)(0x72437350ULL) != 0) goto loc_009F0189;
    *(uint64_t *)((uint32_t)((uint32_t)(arg1)) + 0x8) = v_stack_p58;
    *(uint16_t *)((uint32_t)((uint32_t)(arg1)) + 0x148) = (uint16_t)(*(uint8_t *)(arg1 + 0xD0));
    *(uint64_t *)((uint32_t)((uint32_t)(arg1)) + 0x140) = *(uint64_t *)(64 + *(uint8_t *)(arg1 + 0xD0) * 8 + 0xFC7128);
loc_009EFFE8:
    result = KeGetProcessorNodeNumber(Arg1, (uint32_t)(0x72437350ULL), v_stack_p58, v_stack_m1A8);
loc_009EFFED:
    Arg2 = (uint32_t)(((uint16_t)(result)) + (0));
    v_stack_p5C = (uint32_t)(Arg2);
    goto loc_009EF8F4;
loc_009EFFFC:
    result = ((uint32_t)(v_stack_p80)) + (v_stack_p80);
    *(uint64_t *)(result) = v_stack_p80;
    *(uint8_t *)(result + 0xC) = 8;
    *(uint64_t *)(v_stack_p80 + 0x478) = result;
    goto loc_009EFA8E;
loc_009F0019:
    *(uint64_t *)(v_stack_p80 + 0x4E0) = v_stack_pA8;
    *(uint64_t *)(v_stack_p80 + 0x560) = v_stack_pA8;
    v_stack_p120 = 0;
    v_stack_p130 = v_stack_pA8;
    v_stack_p138 = v_stack_pF0;
    v_stack_p140 = v_xmm0;
    v_stack_p150 = Arg1;
    v_stack_p158 = (uint32_t)((uint32_t)(v_stack_p5C));
    v_stack_p15C = 0;
    v_stack_p128 = v_rip - 5623228;
    if (((*(uint32_t *)(arg9)) & (0x400ULL)) != 0) goto loc_009F02B9;
loc_009F0098:
    goto loc_009EFE05;
loc_009F00A2:
    v_stack_pF8 = 0;
    v_stack_p108 = 0x8000ULL;
    v_stack_p110 = 0x40000ULL;
    v_stack_p100 = 0;
    result = PspSetupUserStack(Arg1, Arg2, v_stack_p58, v_stack_pF8);
    v_stack_p54 = (uint32_t)(result);
    if (sign_flag) goto loc_009EFD33;
    Arg1 = (uint8_t)((v_stack_pF8) & (2));
    result = (uint8_t)((*(uint8_t *)(v_stack_p70)) & (253));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    *(uint8_t *)(v_stack_p70) = (uint8_t)(Arg1);
    v_stack_p20 = (uint32_t)(v_stack_p78);
    result = PspWow64SetupUserStack(Arg1, v_stack_p70, v_stack_p60, v_stack_p70);
loc_009F0117:
    v_stack_p54 = (uint32_t)(result);
    goto loc_009EFD38;
loc_009F0123:
    goto loc_009EF8AB;
loc_009F012F:
    goto loc_009EF8C0;
loc_009F013F:
    local_r12 = ~(*(uint64_t *)(arg1 + 0x198));
    local_r12 = (uint32_t)((local_r12) & (*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x14)))));
    local_r12 = (uint32_t)((local_r12) & (0x40000ULL));
    v_stack_p88 = local_r12;
    v_stack_pA0 = local_r12;
    goto loc_009EF8CF;
loc_009F0172:
    goto loc_009EFE58;
loc_009F0189:
    if (*(uint64_t *)(v_stack_p60 + 0x140) == 0) goto loc_009EFFE8;
    if (((*(uint64_t *)(*(uint64_t *)(64 + (uint32_t)(*(uint32_t *)(v_stack_p60 + 0x14)) * 8 + 0xFC8C40) + 0xC8)) & (*(uint64_t *)(v_stack_p60 + 0x140))) != 0) goto loc_009EFFE8;
loc_009F01B8:
    if ((*(uint64_t *)(v_stack_p60 + 0x140)) == 0) goto loc_009EF8F4;
    result = KeSelectInitialIdealProcessorForThread(Arg1, v_stack_p60 + 320, *(uint64_t *)(v_stack_p60 + 0x140), v_stack_p70);
    *(uint32_t *)(v_stack_p60 + 0x14) = (uint32_t)((uint16_t)(result));
    result = KeGetProcessorNodeNumberByIndex((uint16_t)(result), v_stack_p60 + 320, *(uint64_t *)(v_stack_p60 + 0x140), v_stack_p70);
    goto loc_009EFFED;
loc_009F01ED:
    goto loc_009EFF9E;
loc_009F01F7:
    local_r14 = (uint32_t)(((uint32_t)(0xC000000DULL) + 7) & ((uint32_t)((uint16_t)(result))));
    goto loc_009EF98B;
loc_009F0207:
    goto loc_009EFA64;
loc_009F0216:
    result = ((uint32_t)((uint32_t)(local_r14))) + (v_stack_p68);
    *(uint64_t *)(v_stack_p68 + 0x690) = result;
    goto loc_009EFA6D;
loc_009F0230:
    goto loc_009EFB1F;
loc_009F023C:
    goto loc_009EFB2B;
loc_009F0246:
    local_rbx = (local_r14 + local_r12 * 8) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    result = ExfTryToWakePushLock(local_r12, v_stack_p60 + 320, *(uint64_t *)(v_stack_p60 + 0x140), v_stack_p80);
loc_009F026B:
    goto loc_009EFCF2;
loc_009F0275:
    v_stack_p20 = (uint32_t)(local_rbx);
    result = PspSetupUserShadowStack(Arg1, Arg5, v_stack_p60, v_stack_p70);
    goto loc_009F0117;
loc_009F0296:
    result = PspWow64InitThread(Arg1, v_stack_p60, Arg5, v_stack_p60);
    v_stack_p54 = (uint32_t)(result);
    if (sign_flag) goto loc_009F0302;
    goto loc_009EFD9B;
loc_009F02B9:
    if (v_stack_p50 == 0) goto loc_009F0098;
    v_stack_p128 = v_rip + 768805;
    v_stack_p15C = 16;
    goto loc_009F0098;
loc_009F02EB:
    if (v_stack_p60 == 0) goto loc_009F0302;
    result = v_rip + 768805;
    if (v_stack_p70 != 0) {
        Arg2 = v_stack_p60;
        Arg1 = Arg1;
        result = MmDeleteTeb(Arg1, Arg2, Arg5, v_stack_p60);
    }
    local_rbx = (v_stack_p60) | (-1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `8` | `R` |
| `Arg1` | `+ 0x198` | `64` | `R` |
| `Arg1` | `+ 0x310` | `64` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009EF72C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
