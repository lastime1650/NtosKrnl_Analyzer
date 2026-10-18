# MiBackgroundZeroLocalPages

- RVA: `0x0031EF30`–`0x0031F858` (길이 `2,344` bytes)
- VA: `0x000000014031EF30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00075328`
- 디코드: `525`개 명령, `2,344/2,344` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0031EF7E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0031EFF9` → [MiSetZeroPageThreadPriority](MiSetZeroPageThreadPriority_function_0031E620.md) (function, `0x0031E620`)
- `0x0031F013` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0031F1CA` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0031F2B1` → [MiGetBestPageToZero](../32/MiGetBestPageToZero_function_003200A0.md) (function, `0x003200A0`)
- `0x0031F2CC` → [MiMapBackgroundPagesToZero](MiMapBackgroundPagesToZero_function_0031E940.md) (function, `0x0031E940`)
- `0x0031F35E` → [MiTryZeroMemory](MiTryZeroMemory_function_0031E720.md) (function, `0x0031E720`)
- `0x0031F375` → [MiLockMultipleZeroChunks](MiLockMultipleZeroChunks_function_0031F860.md) (function, `0x0031F860`)
- `0x0031F384` → [MiExamineZeroChunks](MiExamineZeroChunks_function_0031FE50.md) (function, `0x0031FE50`)
- `0x0031F38D` → [MiMoveZeroedPages](MiMoveZeroedPages_function_0031FD30.md) (function, `0x0031FD30`)
- `0x0031F3B1` → [MiUnlockMultipleZeroChunks](MiUnlockMultipleZeroChunks_function_0031FB00.md) (function, `0x0031FB00`)
- `0x0031F423` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0031F451` → [MiReassessZeroThreads](../2C/MiReassessZeroThreads_function_002CB0C0.md) (function, `0x002CB0C0`)
- `0x0031F467` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0031F4AE` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0031F4C7` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0031F4E3` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0031F509` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0031F514` → [MiZeroThreadContextSetExiting](../2C/MiZeroThreadContextSetExiting_function_002CC590.md) (function, `0x002CC590`)
- `0x0031F523` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0031F53F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0031F553` → [MiZeroThreadContextPrepareToWait](MiZeroThreadContextPrepareToWait_function_0031E6D8.md) (function, `0x0031E6D8`)
- `0x0031F577` → [MiSetZeroPageThreadPriority](MiSetZeroPageThreadPriority_function_0031E620.md) (function, `0x0031E620`)
- `0x0031F586` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0031F5C5` → [MiZeroThreadContextPrepareToWait](MiZeroThreadContextPrepareToWait_function_0031E6D8.md) (function, `0x0031E6D8`)
- `0x0031F5EB` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0031F605` → [MiAssignDefaultChannel](MiAssignDefaultChannel_function_0031E5B0.md) (function, `0x0031E5B0`)
- `0x0031F622` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0031F669` → [MiGetBackgroundHugePageToZero](MiGetBackgroundHugePageToZero_function_0031DD8C.md) (function, `0x0031DD8C`)
- `0x0031F687` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0031F69C` → [MiUnlinkZeroThreadFromActiveDomain](../2C/MiUnlinkZeroThreadFromActiveDomain_function_002CCB9C.md) (function, `0x002CCB9C`)
- `0x0031F6B1` → [MiFindBestZeroingProcessor](../2C/MiFindBestZeroingProcessor_function_002CC73C.md) (function, `0x002CC73C`)
- `0x0031F6DC` → [MiAssignBackgroundZeroThreadToProcessor](../2C/MiAssignBackgroundZeroThreadToProcessor_function_002CCAAC.md) (function, `0x002CCAAC`)
- `0x0031F6F2` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0031F733` → [MiZeroPageMakeHot](../69/MiZeroPageMakeHot_function_00696C08.md) (function, `0x00696C08`)
- `0x0031F740` → [MiGetZeroingContext](../43/MiGetZeroingContext_function_00434FB0.md) (function, `0x00434FB0`)
- `0x0031F76D` → [MiDecrementZeroEngineThread](../2C/MiDecrementZeroEngineThread_function_002CBC3C.md) (function, `0x002CBC3C`)
- `0x0031F77A` → [MiZeroThreadContextPrepareToWait](MiZeroThreadContextPrepareToWait_function_0031E6D8.md) (function, `0x0031E6D8`)
- `0x0031F7B5` → [KeWaitForMultipleObjects](../20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x0031F7DB` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0031F7E6` → [MiZeroThreadContextSetExiting](../2C/MiZeroThreadContextSetExiting_function_002CC590.md) (function, `0x002CC590`)
- `0x0031F7FC` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0031F818` → [MiInitializePageHeatList](../44/MiInitializePageHeatList_function_00446000.md) (function, `0x00446000`)

### Direct callers
- [MiBackgroundZeroNodePages](../2C/MiBackgroundZeroNodePages_function_002CB9B0.md) at `0x002CBA68`

### Static image references
- `0x0031EF57` → RVA `0x00E0A740` (`.data`; read)
- `0x0031EFAC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0031F0B1` → RVA `0x00E37610` (`.data`; read)
- `0x0031F0C6` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0031F11A` → RVA `0x00EF5080` (`.data`; read/write)
- `0x0031F26D` → RVA `0x00FC5002` (`ALMOSTRO`; read)
- `0x0031F4D2` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0031F548` → RVA `0x00EF502C` (`.data`; read/write)
- `0x0031F5CE` → RVA `0x00010AA0` (`.rdata`; read)
- `0x0031F673` → RVA `0x00EF5084` (`.data`; read/write)
- `0x0031F7C7` → RVA `0x00EF5030` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0031F848` → [sub_006E182C + 0x8E](../6E/Unknown_function_006E182C.md) (`tail-transfer`)
  - `0x0031F853` → [sub_006E182C](../6E/Unknown_function_006E182C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031EF30  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0031EF35  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0031EF3A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0031EF3F  55                              push rbp
0031EF40  41 54                           push r12
0031EF42  41 55                           push r13
0031EF44  41 56                           push r14
0031EF46  41 57                           push r15
0031EF48  48 8D AC 24 A0 FE FF FF         lea rbp, [rsp - 0x160]
0031EF50  48 81 EC 60 02 00 00            sub rsp, 0x260
0031EF57  48 8B 05 E2 B7 AE 00            mov rax, qword ptr [rip + 0xaeb7e2]
0031EF5E  48 33 C4                        xor rax, rsp
0031EF61  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
0031EF68  48 8B F9                        mov rdi, rcx
0031EF6B  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
0031EF6F  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
0031EF76  33 D2                           xor edx, edx
0031EF78  41 B8 90 00 00 00               mov r8d, 0x90
0031EF7E  E8 BD 7C 3A 00                  call 0x1406c6c40
0031EF83  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0031EF8C  45 33 E4                        xor r12d, r12d
0031EF8F  41 8B DC                        mov ebx, r12d
0031EF92  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
0031EF96  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
0031EF9A  45 8B EC                        mov r13d, r12d
0031EF9D  81 89 A4 05 00 00 00 04 00 00   or dword ptr [rcx + 0x5a4], 0x400
0031EFA7  41 8D 54 24 01                  lea edx, [r12 + 1]
0031EFAC  F7 05 02 7B CA 00 00 00 40 08   test dword ptr [rip + 0xca7b02], 0x8400000
0031EFB6  48 8B B7 50 01 00 00            mov rsi, qword ptr [rdi + 0x150]
0031EFBD  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0031EFC2  48 8B 86 B0 00 00 00            mov rax, qword ptr [rsi + 0xb0]
0031EFC9  48 8B 8E D0 00 00 00            mov rcx, qword ptr [rsi + 0xd0]
0031EFD0  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
0031EFD4  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0031EFD8  74 17                           je 0x14031eff1
0031EFDA  48 85 C9                        test rcx, rcx
0031EFDD  0F 84 23 08 00 00               je 0x14031f806
0031EFE3  8B 81 50 3B 00 00               mov eax, dword ptr [rcx + 0x3b50]
0031EFE9  A8 02                           test al, 2
0031EFEB  0F 84 15 08 00 00               je 0x14031f806
0031EFF1  45 33 C0                        xor r8d, r8d
0031EFF4  33 D2                           xor edx, edx
0031EFF6  48 8B CF                        mov rcx, rdi
0031EFF9  E8 22 F6 FF FF                  call 0x14031e620
0031EFFE  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0031F002  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0031F006  41 8B C4                        mov eax, r12d
0031F009  87 87 84 01 00 00               xchg dword ptr [rdi + 0x184], eax
0031F00F  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
0031F013  E8 C8 F7 05 00                  call 0x14037e7e0
0031F018  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0031F01C  4C 8B F0                        mov r14, rax
0031F01F  48 81 F9 80 96 98 00            cmp rcx, 0x989680
0031F026  74 0F                           je 0x14031f037
0031F028  49 69 C6 80 96 98 00            imul rax, r14, 0x989680
0031F02F  48 99                           cqo
0031F031  48 F7 F9                        idiv rcx
0031F034  4C 8B F0                        mov r14, rax
0031F037  F0 09 1C 24                     lock or dword ptr [rsp], ebx
0031F03B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0031F040  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
0031F045  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0031F04A  85 DB                           test ebx, ebx
0031F04C  0F 85 75 07 00 00               jne 0x14031f7c7
0031F052  4C 8B AF 50 01 00 00            mov r13, qword ptr [rdi + 0x150]
0031F059  41 8B F4                        mov esi, r12d
0031F05C  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
0031F061  49 8B 85 B0 00 00 00            mov rax, qword ptr [r13 + 0xb0]
0031F068  49 8D 9D D0 00 00 00            lea rbx, [r13 + 0xd0]
0031F06F  4C 8B 78 30                     mov r15, qword ptr [rax + 0x30]
0031F073  49 8D 47 58                     lea rax, [r15 + 0x58]
0031F077  48 89 45 00                     mov qword ptr [rbp], rax
0031F07B  48 8D 87 88 01 00 00            lea rax, [rdi + 0x188]
0031F082  48 89 45 08                     mov qword ptr [rbp + 8], rax
0031F086  8B 87 80 01 00 00               mov eax, dword ptr [rdi + 0x180]
0031F08C  A8 02                           test al, 2
0031F08E  0F 85 09 04 00 00               jne 0x14031f49d
0031F094  48 8B 45 00                     mov rax, qword ptr [rbp]
0031F098  83 78 04 00                     cmp dword ptr [rax + 4], 0
0031F09C  0F 85 5D 04 00 00               jne 0x14031f4ff
0031F0A2  41 8B 87 30 42 00 00            mov eax, dword ptr [r15 + 0x4230]
0031F0A9  85 C0                           test eax, eax
0031F0AB  0F 85 11 05 00 00               jne 0x14031f5c2
0031F0B1  8B 05 59 85 B1 00               mov eax, dword ptr [rip + 0xb18559]
0031F0B7  85 C0                           test eax, eax
0031F0B9  0F 85 03 05 00 00               jne 0x14031f5c2
0031F0BF  48 8B 8F 60 01 00 00            mov rcx, qword ptr [rdi + 0x160]
0031F0C6  4C 8D 25 33 0F CE FF            lea r12, [rip - 0x31f0cd]
0031F0CD  0F 57 C0                        xorps xmm0, xmm0
0031F0D0  33 C0                           xor eax, eax
0031F0D2  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
0031F0D6  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0031F0DA  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
0031F0DE  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
0031F0E2  48 3B 8F 70 01 00 00            cmp rcx, qword ptr [rdi + 0x170]
0031F0E9  0F 85 84 05 00 00               jne 0x14031f673
0031F0EF  0F B7 87 68 01 00 00            movzx eax, word ptr [rdi + 0x168]
0031F0F6  66 3B 87 78 01 00 00            cmp ax, word ptr [rdi + 0x178]
0031F0FD  0F 85 70 05 00 00               jne 0x14031f673
0031F103  48 85 C9                        test rcx, rcx
0031F106  0F 84 67 05 00 00               je 0x14031f673
0031F10C  49 85 8C C4 50 ED E2 00         test qword ptr [r12 + rax*8 + 0xe2ed50], rcx
0031F114  0F 85 59 05 00 00               jne 0x14031f673
0031F11A  FF 05 60 5F BD 00               inc dword ptr [rip + 0xbd5f60]
0031F120  33 DB                           xor ebx, ebx
0031F122  85 F6                           test esi, esi
0031F124  0F 85 E5 04 00 00               jne 0x14031f60f
0031F12A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0031F12F  44 8B 6C 24 70                  mov r13d, dword ptr [rsp + 0x70]
0031F134  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0031F139  4D 8B FE                        mov r15, r14
0031F13C  FF 86 1C 01 00 00               inc dword ptr [rsi + 0x11c]
0031F142  45 85 ED                        test r13d, r13d
0031F145  0F 84 17 05 00 00               je 0x14031f662
0031F14B  48 89 9F 20 01 00 00            mov qword ptr [rdi + 0x120], rbx
0031F152  8B C3                           mov eax, ebx
0031F154  B9 20 00 00 00                  mov ecx, 0x20
0031F159  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0031F15E  66 90                           nop
0031F160  48 89 5C 38 18                  mov qword ptr [rax + rdi + 0x18], rbx
0031F165  48 8D 40 08                     lea rax, [rax + 8]
0031F169  48 83 E9 01                     sub rcx, 1
0031F16D  75 F1                           jne 0x14031f160
0031F16F  89 9F 18 01 00 00               mov dword ptr [rdi + 0x118], ebx
0031F175  44 8B E3                        mov r12d, ebx
0031F178  41 8B D5                        mov edx, r13d
0031F17B  41 83 FC 01                     cmp r12d, 1
0031F17F  0F 83 44 01 00 00               jae 0x14031f2c9
0031F185  48 8B 87 50 01 00 00            mov rax, qword ptr [rdi + 0x150]
0031F18C  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
0031F191  0F 57 C0                        xorps xmm0, xmm0
0031F194  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0031F199  48 8B 88 D0 00 00 00            mov rcx, qword ptr [rax + 0xd0]
0031F1A0  4C 8B C1                        mov r8, rcx
0031F1A3  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0031F1A8  48 8B 81 88 3A 00 00            mov rax, qword ptr [rcx + 0x3a88]
0031F1AF  33 C9                           xor ecx, ecx
0031F1B1  4C 2B 40 10                     sub r8, qword ptr [rax + 0x10]
0031F1B5  48 B8 3F EE A0 D9 7C 5A 1E F5   movabs rax, 0xf51e5a7cd9a0ee3f
0031F1BF  49 C1 F8 07                     sar r8, 7
0031F1C3  4C 0F AF C0                     imul r8, rax
0031F1C7  41 FF C0                        inc r8d
0031F1CA  E8 41 12 00 00                  call 0x140320410
0031F1CF  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
0031F1D4  49 8D 85 94 00 00 00            lea rax, [r13 + 0x94]
0031F1DB  48 8D 04 87                     lea rax, [rdi + rax*4]
0031F1DF  41 BF 03 00 00 00               mov r15d, 3
0031F1E5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0031F1EA  45 85 FF                        test r15d, r15d
0031F1ED  0F 84 44 06 00 00               je 0x14031f837
0031F1F3  41 8B C1                        mov eax, r9d
0031F1F6  41 FF CF                        dec r15d
0031F1F9  41 8B CF                        mov ecx, r15d
0031F1FC  25 FF FF F3 FF                  and eax, 0xfff3ffff
0031F201  83 E1 03                        and ecx, 3
0031F204  8B F3                           mov esi, ebx
0031F206  C1 E1 12                        shl ecx, 0x12
0031F209  44 8B C9                        mov r9d, ecx
0031F20C  44 0B C8                        or r9d, eax
0031F20F  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
0031F214  BB 00 00 00 00                  mov ebx, 0
0031F219  83 FE 01                        cmp esi, 1
0031F21C  7F CC                           jg 0x14031f1ea
0031F21E  8B C6                           mov eax, esi
0031F220  41 B8 01 00 00 00               mov r8d, 1
0031F226  C1 E0 0F                        shl eax, 0xf
0031F229  41 33 C1                        xor eax, r9d
0031F22C  25 00 80 00 00                  and eax, 0x8000
0031F231  44 33 C8                        xor r9d, eax
0031F234  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0031F239  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
0031F23E  F0 44 0F C1 00                  lock xadd dword ptr [rax], r8d
0031F243  33 D2                           xor edx, edx
0031F245  41 8B C0                        mov eax, r8d
0031F248  41 8B C9                        mov ecx, r9d
0031F24B  4C 8D 05 AE 0D CE FF            lea r8, [rip - 0x31f252]
0031F252  48 C1 E9 10                     shr rcx, 0x10
0031F256  83 E1 03                        and ecx, 3
0031F259  41 F7 B4 88 C0 DC E2 00         div dword ptr [r8 + rcx*4 + 0xe2dcc0]
0031F261  41 33 D1                        xor edx, r9d
0031F264  0F B6 DA                        movzx ebx, dl
0031F267  41 33 D9                        xor ebx, r9d
0031F26A  45 32 F6                        xor r14b, r14b
0031F26D  44 3A 35 8E 5D CA 00            cmp r14b, byte ptr [rip + 0xca5d8e]
0031F274  72 13                           jb 0x14031f289
0031F276  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
0031F27B  41 83 FD 03                     cmp r13d, 3
0031F27F  0F 84 AB 05 00 00               je 0x14031f830
0031F285  FF C6                           inc esi
0031F287  EB 8B                           jmp 0x14031f214
0031F289  41 0F B6 C6                     movzx eax, r14b
0031F28D  41 80 FE 02                     cmp r14b, 2
0031F291  0F 84 66 03 00 00               je 0x14031f5fd
0031F297  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0031F29C  48 8B CF                        mov rcx, rdi
0031F29F  0F B6 C0                        movzx eax, al
0031F2A2  C1 E0 08                        shl eax, 8
0031F2A5  33 C3                           xor eax, ebx
0031F2A7  25 00 01 00 00                  and eax, 0x100
0031F2AC  33 D8                           xor ebx, eax
0031F2AE  44 8B C3                        mov r8d, ebx
0031F2B1  E8 EA 0D 00 00                  call 0x1403200a0
0031F2B6  48 85 C0                        test rax, rax
0031F2B9  0F 84 D6 01 00 00               je 0x14031f495
0031F2BF  41 FF C4                        inc r12d
0031F2C2  33 DB                           xor ebx, ebx
0031F2C4  E9 AF FE FF FF                  jmp 0x14031f178
0031F2C9  48 8B CF                        mov rcx, rdi
0031F2CC  E8 6F F6 FF FF                  call 0x14031e940
0031F2D1  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0031F2D6  4C 8D 25 23 0D CE FF            lea r12, [rip - 0x31f2dd]
0031F2DD  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0031F2E2  4D 8B FE                        mov r15, r14
0031F2E5  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0031F2EA  85 C0                           test eax, eax
0031F2EC  0F 84 BB 02 00 00               je 0x14031f5ad
0031F2F2  48 8B 87 50 01 00 00            mov rax, qword ptr [rdi + 0x150]
0031F2F9  0F 57 C0                        xorps xmm0, xmm0
0031F2FC  89 5D B9                        mov dword ptr [rbp - 0x47], ebx
0031F2FF  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
0031F303  48 89 5D B1                     mov qword ptr [rbp - 0x4f], rbx
0031F307  48 8B 88 B0 00 00 00            mov rcx, qword ptr [rax + 0xb0]
0031F30E  89 5D C4                        mov dword ptr [rbp - 0x3c], ebx
0031F311  C6 45 BF 00                     mov byte ptr [rbp - 0x41], 0
0031F315  66 0F 7F 45 E0                  movdqa xmmword ptr [rbp - 0x20], xmm0
0031F31A  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
0031F31D  89 45 C0                        mov dword ptr [rbp - 0x40], eax
0031F320  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0031F329  8B 9F 40 01 00 00               mov ebx, dword ptr [rdi + 0x140]
0031F32F  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0031F333  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0031F337  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0031F33B  C6 45 B0 11                     mov byte ptr [rbp - 0x50], 0x11
0031F33F  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
0031F343  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
0031F347  89 5D BC                        mov dword ptr [rbp - 0x44], ebx
0031F34A  83 FB 03                        cmp ebx, 3
0031F34D  0F 82 C0 03 00 00               jb 0x14031f713
0031F353  41 FF 84 9C 94 50 EF 00         inc dword ptr [r12 + rbx*4 + 0xef5094]
0031F35B  48 8B CF                        mov rcx, rdi
0031F35E  E8 BD F3 FF FF                  call 0x14031e720
0031F363  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0031F367  49 BC FF FF FF FF 3F 00 00 00   movabs r12, 0x3fffffffff
0031F371  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0031F375  E8 E6 04 00 00                  call 0x14031f860
0031F37A  83 7D B8 00                     cmp dword ptr [rbp - 0x48], 0
0031F37E  74 49                           je 0x14031f3c9
0031F380  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0031F384  E8 C7 0A 00 00                  call 0x14031fe50
0031F389  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0031F38D  E8 9E 09 00 00                  call 0x14031fd30
0031F392  83 BF 40 01 00 00 00            cmp dword ptr [rdi + 0x140], 0
0031F399  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0031F39D  8B B1 18 01 00 00               mov esi, dword ptr [rcx + 0x118]
0031F3A3  48 8D 59 18                     lea rbx, [rcx + 0x18]
0031F3A7  0F 84 B0 03 00 00               je 0x14031f75d
0031F3AD  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0031F3B1  E8 4A 07 00 00                  call 0x14031fb00
0031F3B6  80 7D B3 00                     cmp byte ptr [rbp - 0x4d], 0
0031F3BA  0F 85 86 04 00 00               jne 0x14031f846
0031F3C0  83 BF 40 01 00 00 00            cmp dword ptr [rdi + 0x140], 0
0031F3C7  75 A8                           jne 0x14031f371
0031F3C9  4C 8D 25 30 0C CE FF            lea r12, [rip - 0x31f3d0]
0031F3D0  B9 01 00 00 00                  mov ecx, 1
0031F3D5  41 83 FD 03                     cmp r13d, 3
0031F3D9  0F 85 1D 03 00 00               jne 0x14031f6fc
0031F3DF  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0031F3E4  F0 48 01 8E B8 00 00 00         lock add qword ptr [rsi + 0xb8], rcx
0031F3EC  8B C1                           mov eax, ecx
0031F3EE  F0 0F C1 87 84 01 00 00         lock xadd dword ptr [rdi + 0x184], eax
0031F3F6  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0031F3FB  41 BC 00 00 00 00               mov r12d, 0
0031F401  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
0031F405  48 98                           cdqe
0031F407  48 03 C1                        add rax, rcx
0031F40A  48 3D 00 10 00 00               cmp rax, 0x1000
0031F410  0F 82 2A FC FF FF               jb 0x14031f040
0031F416  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
0031F41B  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0031F41F  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
0031F423  E8 B8 F3 05 00                  call 0x14037e7e0
0031F428  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
0031F42C  48 81 F9 80 96 98 00            cmp rcx, 0x989680
0031F433  74 0C                           je 0x14031f441
0031F435  48 69 C0 80 96 98 00            imul rax, rax, 0x989680
0031F43C  48 99                           cqo
0031F43E  48 F7 F9                        idiv rcx
0031F441  49 3B C6                        cmp rax, r14
0031F444  48 8B CF                        mov rcx, rdi
0031F447  4C 0F 43 F8                     cmovae r15, rax
0031F44B  4D 2B FE                        sub r15, r14
0031F44E  49 8B D7                        mov rdx, r15
0031F451  E8 6A BC FA FF                  call 0x1402cb0c0
0031F456  41 8B C4                        mov eax, r12d
0031F459  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0031F45D  87 87 84 01 00 00               xchg dword ptr [rdi + 0x184], eax
0031F463  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
0031F467  E8 74 F3 05 00                  call 0x14037e7e0
0031F46C  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
0031F470  4C 8B F0                        mov r14, rax
0031F473  48 81 F9 80 96 98 00            cmp rcx, 0x989680
0031F47A  74 0F                           je 0x14031f48b
0031F47C  49 69 C6 80 96 98 00            imul rax, r14, 0x989680
0031F483  48 99                           cqo
0031F485  48 F7 F9                        idiv rcx
0031F488  4C 8B F0                        mov r14, rax
0031F48B  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
0031F490  E9 AB FB FF FF                  jmp 0x14031f040
0031F495  41 FE C6                        inc r14b
0031F498  E9 D0 FD FF FF                  jmp 0x14031f26d
0031F49D  49 8D 9D D0 00 00 00            lea rbx, [r13 + 0xd0]
0031F4A4  48 8B 0B                        mov rcx, qword ptr [rbx]
0031F4A7  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F4AE  E8 DD 91 F2 FF                  call 0x140248690
0031F4B3  44 8B B7 80 01 00 00            mov r14d, dword ptr [rdi + 0x180]
0031F4BA  48 8B 0B                        mov rcx, qword ptr [rbx]
0031F4BD  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F4C4  0F B6 F0                        movzx esi, al
0031F4C7  E8 14 A3 F2 FF                  call 0x1402497e0
0031F4CC  40 80 FE 11                     cmp sil, 0x11
0031F4D0  74 1A                           je 0x14031f4ec
0031F4D2  83 3D 47 78 CA 00 00            cmp dword ptr [rip + 0xca7847], 0
0031F4D9  74 0D                           je 0x14031f4e8
0031F4DB  44 0F 20 C1                     mov rcx, cr8
0031F4DF  40 0F B6 D6                     movzx edx, sil
0031F4E3  E8 B0 61 1D 00                  call 0x1404f5698
0031F4E8  44 0F 22 C6                     mov cr8, rsi
0031F4EC  41 F6 C6 02                     test r14b, 2
0031F4F0  0F 85 81 02 00 00               jne 0x14031f777
0031F4F6  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
0031F4FA  E9 95 FB FF FF                  jmp 0x14031f094
0031F4FF  48 8B 0B                        mov rcx, qword ptr [rbx]
0031F502  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F509  E8 82 91 F2 FF                  call 0x140248690
0031F50E  48 8B CF                        mov rcx, rdi
0031F511  0F B6 F0                        movzx esi, al
0031F514  E8 77 D0 FA FF                  call 0x1402cc590
0031F519  48 8B 0B                        mov rcx, qword ptr [rbx]
0031F51C  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F523  E8 B8 A2 F2 FF                  call 0x1402497e0
0031F528  40 80 FE 11                     cmp sil, 0x11
0031F52C  74 1A                           je 0x14031f548
0031F52E  83 3D EB 77 CA 00 00            cmp dword ptr [rip + 0xca77eb], 0
0031F535  74 0D                           je 0x14031f544
0031F537  44 0F 20 C1                     mov rcx, cr8
0031F53B  40 0F B6 D6                     movzx edx, sil
0031F53F  E8 54 61 1D 00                  call 0x1404f5698
0031F544  44 0F 22 C6                     mov cr8, rsi
0031F548  FF 05 DE 5A BD 00               inc dword ptr [rip + 0xbd5ade]
0031F54E  33 DB                           xor ebx, ebx
0031F550  48 8B CF                        mov rcx, rdi
0031F553  E8 80 F1 FF FF                  call 0x14031e6d8
0031F558  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0031F55C  45 33 C0                        xor r8d, r8d
0031F55F  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
0031F563  48 89 9F A0 02 00 00            mov qword ptr [rdi + 0x2a0], rbx
0031F56A  81 A1 A4 05 00 00 FF FB FF FF   and dword ptr [rcx + 0x5a4], 0xfffffbff
0031F574  48 8B CF                        mov rcx, rdi
0031F577  E8 A4 F0 FF FF                  call 0x14031e620
0031F57C  48 8B 8D 50 01 00 00            mov rcx, qword ptr [rbp + 0x150]
0031F583  48 33 CC                        xor rcx, rsp
0031F586  E8 B5 D0 38 00                  call 0x1406ac640
0031F58B  4C 8D 9C 24 60 02 00 00         lea r11, [rsp + 0x260]
0031F593  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0031F597  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0031F59B  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0031F59F  49 8B E3                        mov rsp, r11
0031F5A2  41 5F                           pop r15
0031F5A4  41 5E                           pop r14
0031F5A6  41 5D                           pop r13
0031F5A8  41 5C                           pop r12
0031F5AA  5D                              pop rbp
0031F5AB  C3                              ret
0031F5AC  CC                              int3
0031F5AD  41 83 FD 03                     cmp r13d, 3
0031F5B1  73 9D                           jae 0x14031f550
0031F5B3  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
0031F5B7  41 FF C5                        inc r13d
0031F5BA  45 33 E4                        xor r12d, r12d
0031F5BD  E9 7E FA FF FF                  jmp 0x14031f040
0031F5C2  48 8B CF                        mov rcx, rdi
0031F5C5  E8 0E F1 FF FF                  call 0x14031e6d8
0031F5CA  48 8B 4D 00                     mov rcx, qword ptr [rbp]
0031F5CE  48 8D 05 CB 14 CF FF            lea rax, [rip - 0x30eb35]
0031F5D5  45 33 C9                        xor r9d, r9d
0031F5D8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0031F5DD  45 33 C0                        xor r8d, r8d
0031F5E0  49 8D 9D D0 00 00 00            lea rbx, [r13 + 0xd0]
0031F5E7  41 8D 51 08                     lea edx, [r9 + 8]
0031F5EB  E8 C0 F0 EE FF                  call 0x14020e6b0
0031F5F0  85 C0                           test eax, eax
0031F5F2  0F 85 AA FA FF FF               jne 0x14031f0a2
0031F5F8  E9 02 FF FF FF                  jmp 0x14031f4ff
0031F5FD  8B CB                           mov ecx, ebx
0031F5FF  C1 E9 09                        shr ecx, 9
0031F602  83 E1 3F                        and ecx, 0x3f
0031F605  E8 A6 EF FF FF                  call 0x14031e5b0
0031F60A  E9 88 FC FF FF                  jmp 0x14031f297
0031F60F  8B C3                           mov eax, ebx
0031F611  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0031F615  87 87 84 01 00 00               xchg dword ptr [rdi + 0x184], eax
0031F61B  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0031F61F  44 8B EB                        mov r13d, ebx
0031F622  E8 B9 F1 05 00                  call 0x14037e7e0
0031F627  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0031F62B  4C 8B F0                        mov r14, rax
0031F62E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0031F633  48 81 F9 80 96 98 00            cmp rcx, 0x989680
0031F63A  74 14                           je 0x14031f650
0031F63C  49 69 C6 80 96 98 00            imul rax, r14, 0x989680
0031F643  48 99                           cqo
0031F645  48 F7 F9                        idiv rcx
0031F648  4C 8B F0                        mov r14, rax
0031F64B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0031F650  F0 09 1C 24                     lock or dword ptr [rsp], ebx
0031F654  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0031F659  4D 8B FE                        mov r15, r14
0031F65C  FF 86 1C 01 00 00               inc dword ptr [rsi + 0x11c]
0031F662  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0031F666  48 8B D7                        mov rdx, rdi
0031F669  E8 1E E7 FF FF                  call 0x14031dd8c
0031F66E  E9 77 FC FF FF                  jmp 0x14031f2ea
0031F673  FF 05 0B 5A BD 00               inc dword ptr [rip + 0xbd5a0b]
0031F679  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
0031F680  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F687  E8 04 90 F2 FF                  call 0x140248690
0031F68C  48 83 BF 60 01 00 00 00         cmp qword ptr [rdi + 0x160], 0
0031F694  0F B6 D8                        movzx ebx, al
0031F697  74 08                           je 0x14031f6a1
0031F699  48 8B CF                        mov rcx, rdi
0031F69C  E8 FB D4 FA FF                  call 0x1402ccb9c
0031F6A1  41 B9 01 00 00 00               mov r9d, 1
0031F6A7  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0031F6AB  45 33 C0                        xor r8d, r8d
0031F6AE  49 8B D5                        mov rdx, r13
0031F6B1  E8 86 D0 FA FF                  call 0x1402cc73c
0031F6B6  48 63 4D 48                     movsxd rcx, dword ptr [rbp + 0x48]
0031F6BA  41 FF 84 8C 68 50 EF 00         inc dword ptr [r12 + rcx*4 + 0xef5068]
0031F6C2  83 F9 05                        cmp ecx, 5
0031F6C5  48 8B CF                        mov rcx, rdi
0031F6C8  0F 84 9F 00 00 00               je 0x14031f76d
0031F6CE  41 FF 85 14 01 00 00            inc dword ptr [r13 + 0x114]
0031F6D5  4C 8D 45 20                     lea r8, [rbp + 0x20]
0031F6D9  49 8B D5                        mov rdx, r13
0031F6DC  E8 CB D3 FA FF                  call 0x1402ccaac
0031F6E1  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
0031F6E8  0F B6 D3                        movzx edx, bl
0031F6EB  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F6F2  E8 C9 8B F2 FF                  call 0x1402482c0
0031F6F7  E9 24 FA FF FF                  jmp 0x14031f120
0031F6FC  41 8B C5                        mov eax, r13d
0031F6FF  41 83 FD 01                     cmp r13d, 1
0031F703  0F 42 C1                        cmovb eax, ecx
0031F706  49 8B 8C C4 60 1C 01 00         mov rcx, qword ptr [r12 + rax*8 + 0x11c60]
0031F70E  E9 CC FC FF FF                  jmp 0x14031f3df
0031F713  85 DB                           test ebx, ebx
0031F715  74 26                           je 0x14031f73d
0031F717  83 FB 01                        cmp ebx, 1
0031F71A  0F 82 33 FC FF FF               jb 0x14031f353
0031F720  F7 05 8E 73 CA 00 00 00 20 00   test dword ptr [rip + 0xca738e], 0x200000
0031F72A  0F 84 23 FC FF FF               je 0x14031f353
0031F730  48 8B CF                        mov rcx, rdi
0031F733  E8 D0 74 37 00                  call 0x140696c08
0031F738  E9 16 FC FF FF                  jmp 0x14031f353
0031F73D  48 8B CF                        mov rcx, rdi
0031F740  E8 6B 58 11 00                  call 0x140434fb0
0031F745  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0031F749  48 8B 87 48 02 00 00            mov rax, qword ptr [rdi + 0x248]
0031F750  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0031F754  C6 45 B2 01                     mov byte ptr [rbp - 0x4e], 1
0031F758  E9 F6 FB FF FF                  jmp 0x14031f353
0031F75D  48 8B 03                        mov rax, qword ptr [rbx]
0031F760  48 8D 5D 98                     lea rbx, [rbp - 0x68]
0031F764  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0031F768  E9 40 FC FF FF                  jmp 0x14031f3ad
0031F76D  E8 CA C4 FA FF                  call 0x1402cbc3c
0031F772  E9 6A FF FF FF                  jmp 0x14031f6e1
0031F777  48 8B CF                        mov rcx, rdi
0031F77A  E8 59 EF FF FF                  call 0x14031e6d8
0031F77F  B9 01 00 00 00                  mov ecx, 1
0031F784  48 8D 45 60                     lea rax, [rbp + 0x60]
0031F788  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0031F78D  48 8D 55 00                     lea rdx, [rbp]
0031F791  8B F1                           mov esi, ecx
0031F793  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0031F797  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
0031F7A0  44 8B C1                        mov r8d, ecx
0031F7A3  44 8D 49 07                     lea r9d, [rcx + 7]
0031F7A7  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0031F7AC  41 8D 49 FA                     lea ecx, [r9 - 6]
0031F7B0  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0031F7B5  E8 56 D9 EE FF                  call 0x14020d110
0031F7BA  85 C0                           test eax, eax
0031F7BC  0F 85 C4 F8 FF FF               jne 0x14031f086
0031F7C2  E9 38 FD FF FF                  jmp 0x14031f4ff
0031F7C7  FF 05 63 58 BD 00               inc dword ptr [rip + 0xbd5863]
0031F7CD  48 8B 8E D0 00 00 00            mov rcx, qword ptr [rsi + 0xd0]
0031F7D4  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F7DB  E8 B0 8E F2 FF                  call 0x140248690
0031F7E0  48 8B CF                        mov rcx, rdi
0031F7E3  0F B6 D8                        movzx ebx, al
0031F7E6  E8 A5 CD FA FF                  call 0x1402cc590
0031F7EB  48 8B 8E D0 00 00 00            mov rcx, qword ptr [rsi + 0xd0]
0031F7F2  0F B6 D3                        movzx edx, bl
0031F7F5  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
0031F7FC  E8 BF 8A F2 FF                  call 0x1402482c0
0031F801  E9 48 FD FF FF                  jmp 0x14031f54e
0031F806  44 8B C2                        mov r8d, edx
0031F809  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
0031F810  33 D2                           xor edx, edx
0031F812  41 B9 10 00 00 00               mov r9d, 0x10
0031F818  E8 E3 67 12 00                  call 0x140446000
0031F81D  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
0031F824  48 89 8F A0 02 00 00            mov qword ptr [rdi + 0x2a0], rcx
0031F82B  E9 C1 F7 FF FF                  jmp 0x14031eff1
0031F830  33 DB                           xor ebx, ebx
0031F832  E9 B3 F9 FF FF                  jmp 0x14031f1ea
0031F837  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0031F83C  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0031F841  E9 67 FD FF FF                  jmp 0x14031f5ad
0031F846  85 F6                           test esi, esi
0031F848  0F 84 6C 20 3C 00               je 0x1406e18ba
0031F84E  4C 8B F6                        mov r14, rsi
0031F851  33 FF                           xor edi, edi
0031F853  E9 D4 1F 3C 00                  jmp 0x1406e182c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBackgroundZeroLocalPages(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int8 v_stack_m1C9;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1CF;
    unsigned int v_stack_m1D0;
    unsigned __int8 v_stack_m1D5;
    unsigned __int8 v_stack_m1D6;
    unsigned __int64 v_stack_m1D7;
    unsigned __int8 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned int v_stack_m218;
    unsigned int v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned int v_stack_m248;
    unsigned int v_stack_m260;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (608);
    result = (*(unsigned __int64 *)(v_rip + 11450338)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m178 = a1;
    a2 = 0;
    result = memset(v_stack_mC8, a2, 144, a4);
    v_r12 = 0;
    v_stack_m170 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m248 = 0;
    v_stack_m238 = *(unsigned __int64 *)(a1 + 336);
    v_stack_m1F8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 176) + 48);
    if (((*(unsigned int *)(v_rip + 13269762)) & (0x8400000ULL)) == 0) goto loc_0031EFF1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 208) == 0) goto loc_0031F806;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 208) + 15184)))) & (2)) == 0) goto loc_0031F806;
loc_0031EFF1:
    a3 = 0;
    a2 = 0;
    result = MiSetZeroPageThreadPriority(a1, a2, a3, a4);
    v_stack_m210 = (unsigned int)(result);
    v_stack_m208 = 0;
    result = KeQueryPerformanceCounter(v_stack_m208, a2, a3, a4);
    v_r14 = result;
    if (v_stack_m208 != 0x989680ULL) {
        result = (result) * (result);
        v_r14 = result;
    }
loc_0031F040:
    v_stack_m218 = 0;
    v_stack_m240 = v_r14;
    if (0 != 0) goto loc_0031F7C7;
    v_stack_m230 = 0;
    v_stack_m188 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 176) + 48) + 88;
    v_stack_m180 = a1 + 392;
loc_0031F086:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 384)))) & (2)) != 0) goto loc_0031F49D;
loc_0031F094:
    if ((*(unsigned int *)(v_stack_m188 + 4)) != 0) goto loc_0031F4FF;
loc_0031F0A2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 176) + 48) + 16944))) != 0) goto loc_0031F5C2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11634009))) != 0) goto loc_0031F5C2;
    result = 0;
    v_stack_m168 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    if ((*(unsigned __int64 *)(a1 + 352)) != (*(unsigned __int64 *)(a1 + 368))) goto loc_0031F673;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 360))) != (*(unsigned __int16 *)(a1 + 376))) goto loc_0031F673;
    if (*(unsigned __int64 *)(a1 + 352) == 0) goto loc_0031F673;
    if (((*(unsigned __int64 *)(v_rip - 3272909 + *(unsigned __int16 *)(a1 + 360) * 8 + 14871888)) & (*(unsigned __int64 *)(a1 + 352))) != 0) goto loc_0031F673;
loc_0031F120:
    v_rbx = 0;
    if (0 != 0) goto loc_0031F60F;
    if ((unsigned int)((unsigned int)(v_stack_m218)) == 0) goto loc_0031F662;
    *(unsigned __int64 *)(a1 + 288) = 0;
    v_stack_m240 = v_stack_m240;
loc_0031F160:
    *(unsigned __int64 *)(0 + a1 * 1 + 24) = 0;
    a1 = (32) - (1);
    if (condition_is_not_equal) goto loc_0031F160;
    *(unsigned int *)(a1 + 280) = 0;
loc_0031F178:
    if (0 >= 1) goto loc_0031F2C9;
    v_stack_m228 = v_xmm0;
    v_stack_m218 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 208);
    a1 = 0;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 208)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 208) + 14984) + 16));
    a3 = (a3) >> (7);
    a3 = (a3) * (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 208) + 14984));
    a3 = (unsigned int)((a3) + 1);
    result = MiInitializePageColorBase(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m218))), a3, v_stack_m228);
    v_stack_m228 = a1 + (unsigned int)(v_stack_m218) + 148 * 4;
loc_0031F1EA:
    if (3 == 0) goto loc_0031F837;
    v_r15 = (unsigned int)((3) - 1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m220)))) & (0xFFF3FFFFULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (3));
    a1 = (unsigned int)((a1) << (18));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | ((unsigned int)(result)));
    v_stack_m220 = (unsigned int)(a4);
loc_0031F214:
    if (0 > 1) goto loc_0031F1EA;
    result = (unsigned int)((0) << (15));
    result = (unsigned int)((result) ^ ((unsigned int)(a4)));
    result = (unsigned int)((result) & (0x8000ULL));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(result)));
    v_stack_m220 = (unsigned int)(a4);
    a2 = 0;
    a1 = ((unsigned int)((unsigned int)(a4))) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a4)));
    v_rbx = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(a4)));
    v_r14 = 0;
loc_0031F26D:
    if (0 < (*(unsigned __int8 *)(v_rip + 13262222))) goto loc_0031F289;
    if (((unsigned int)((unsigned int)(v_stack_m218))) == 3) goto loc_0031F830;
    v_rsi = (unsigned int)((0) + 1);
    goto loc_0031F214;
loc_0031F289:
    if (0 == 2) goto loc_0031F5FD;
loc_0031F297:
    result = (unsigned int)((0) << (8));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (256));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    result = MiGetBestPageToZero(a1, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if (result == 0) goto loc_0031F495;
    v_r12 = (unsigned int)((0) + 1);
    v_rbx = 0;
    goto loc_0031F178;
loc_0031F2C9:
    result = MiMapBackgroundPagesToZero(a1, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    v_stack_m240 = v_stack_m240;
loc_0031F2EA:
    if ((unsigned int)(result) == 0) goto loc_0031F5AD;
    v_stack_m1CF = 0;
    v_stack_m1F0 = 0;
    v_stack_m1D7 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1C9 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336) + 176) + 56)));
    v_stack_m1C0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1B8 = v_stack_m1F8;
    v_stack_m1D8 = 17;
    v_stack_m1B0 = a1;
    v_stack_m198 = a1;
    v_stack_m1CC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 320)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 320)))) < 3) goto loc_0031F713;
loc_0031F353:
    result = MiTryZeroMemory(a1, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    v_stack_m248 = (unsigned int)(result);
loc_0031F371:
    result = MiLockMultipleZeroChunks(v_stack_m1D8, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if (v_stack_m1D0 == 0) goto loc_0031F3C9;
    result = MiExamineZeroChunks(v_stack_m1D8, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    result = MiMoveZeroedPages(v_stack_m1D8, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if ((*(unsigned int *)(a1 + 320)) == 0) goto loc_0031F75D;
loc_0031F3AD:
    result = MiUnlockMultipleZeroChunks(v_stack_m1D8, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if (v_stack_m1D5 != 0) goto loc_0031F846;
    if ((*(unsigned int *)(a1 + 320)) != 0) goto loc_0031F371;
loc_0031F3C9:
    if (((unsigned int)((unsigned int)(v_stack_m218))) != 3) goto loc_0031F6FC;
loc_0031F3DF:
    result = (1) + (1);
    if (result < 0x1000ULL) goto loc_0031F040;
    v_stack_m1E8 = 0;
    result = KeQueryPerformanceCounter(v_stack_m1E8, v_stack_m218, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if (v_stack_m1E8 != 0x989680ULL) {
        result = (result) * (result);
    }
    v_r15 = v_stack_m240;
    if (result >= v_stack_m240) { v_r15 = result; }
    v_r15 = (v_r15) - (v_stack_m240);
    result = MiReassessZeroThreads(a1, v_r15, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    v_stack_m1E0 = 0;
    result = KeQueryPerformanceCounter(v_stack_m1E0, v_r15, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    v_r14 = result;
    if (v_stack_m1E0 != 0x989680ULL) {
        result = (result) * (result);
        v_r14 = result;
    }
    goto loc_0031F040;
loc_0031F495:
    v_r14 = (unsigned __int8)((v_r14) + 1);
    goto loc_0031F26D;
loc_0031F49D:
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m218) + 208)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(a1, v_r15, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m218) + 208)) + (0x3BB0ULL);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(a1, v_r15, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_0031F4EC;
    if ((*(unsigned int *)(v_rip + 13269063)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    }
loc_0031F4EC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 384)))) & (2)) != 0) goto loc_0031F777;
    goto loc_0031F094;
loc_0031F4FF:
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m218) + 208)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(a1, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    result = MiZeroThreadContextSetExiting(a1, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m218) + 208)) + (0x3BB0ULL);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(a1, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_0031F548;
    if ((*(unsigned int *)(v_rip + 13268971)) != 0) {
        a1 = (unsigned __int8)(result);
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    }
loc_0031F548:
loc_0031F54E:
    v_rbx = 0;
loc_0031F550:
    result = MiZeroThreadContextPrepareToWait(a1, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m220));
    a3 = 0;
    *(unsigned __int64 *)(a1 + 672) = 0;
    result = MiSetZeroPageThreadPriority(a1, (unsigned int)(v_stack_m210), a3, (unsigned int)(v_stack_m220));
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(v_stack_m210), a3, (unsigned int)(v_stack_m220));
    return result;
loc_0031F5AD:
    if (((unsigned int)((unsigned int)(v_stack_m218))) >= 3) goto loc_0031F550;
    v_r13 = (unsigned int)(((unsigned int)(v_stack_m218)) + 1);
    v_r12 = 0;
    goto loc_0031F040;
loc_0031F5C2:
    result = MiZeroThreadContextPrepareToWait(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(v_stack_m210), a3, (unsigned int)(v_stack_m220));
    a4 = 0;
    v_stack_m240 = v_rip - 3205941;
    a3 = 0;
    result = KeWaitForSingleObject(v_stack_m188, a4 + 8, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0031F0A2;
    goto loc_0031F4FF;
loc_0031F5FD:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13 + 208))) >> (9));
    a1 = (unsigned int)((a1) & (63));
    result = MiAssignDefaultChannel(a1, a4 + 8, a3, a4);
    goto loc_0031F297;
loc_0031F60F:
    v_stack_m200 = v_r13 + 208;
    result = KeQueryPerformanceCounter(v_stack_m200, a4 + 8, a3, a4);
    v_stack_m218 = result;
    v_r14 = result;
    if (v_stack_m200 != 0x989680ULL) {
        result = (result) * (result);
        v_r14 = result;
        v_stack_m218 = result;
    }
loc_0031F662:
    result = MiGetBackgroundHugePageToZero(v_stack_m1F8, *(unsigned __int64 *)(v_stack_m28 + 72), a3, a4);
    goto loc_0031F2EA;
loc_0031F673:
    a1 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r13 + 208)) + 208)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(a1, *(unsigned __int64 *)(v_stack_m28 + 72), a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 352)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 72);
        result = MiUnlinkZeroThreadFromActiveDomain(a1, *(unsigned __int64 *)(v_stack_m28 + 72), a3, a4);
    }
    a3 = 0;
    result = MiFindBestZeroingProcessor(v_stack_m168, (unsigned int)((unsigned int)(v_r13 + 208)), a3, 1);
    if (((unsigned int)((int)(v_stack_m140))) == 5) goto loc_0031F76D;
    result = MiAssignBackgroundZeroThreadToProcessor(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(v_r13 + 208)), v_stack_m168, 1);
loc_0031F6E1:
    a1 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r13 + 208)) + 208)) + (0x3BB0ULL);
    result = MiReleaseSpinLockExclusive(a1, (unsigned __int8)((unsigned __int8)(result)), v_stack_m168, 1);
    goto loc_0031F120;
loc_0031F6FC:
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13 + 208))));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r13 + 208)))) < 1) { result = (unsigned int)(a1); }
    goto loc_0031F3DF;
loc_0031F713:
    if ((unsigned int)((unsigned __int8)(result)) == 0) goto loc_0031F73D;
    if (((unsigned int)((unsigned __int8)(result))) < 1) goto loc_0031F353;
    if (((*(unsigned int *)(v_rip + 13267854)) & (0x200000ULL)) == 0) goto loc_0031F353;
    result = MiZeroPageMakeHot(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)((unsigned __int8)(result)), v_stack_m168, 1);
    goto loc_0031F353;
loc_0031F73D:
    result = MiGetZeroingContext(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)((unsigned __int8)(result)), v_stack_m168, 1);
    v_stack_m198 = result;
    v_stack_m1A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 584);
    v_stack_m1D6 = 1;
    goto loc_0031F353;
loc_0031F75D:
    v_stack_m1F0 = *(unsigned __int64 *)((unsigned __int8)(result));
    goto loc_0031F3AD;
loc_0031F76D:
    result = MiDecrementZeroEngineThread(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)((unsigned __int8)(result)), v_stack_m168, 1);
    goto loc_0031F6E1;
loc_0031F777:
    result = MiZeroThreadContextPrepareToWait(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)((unsigned __int8)(result)), v_stack_m168, 1);
    v_stack_m228 = v_stack_m128;
    v_stack_m208 = 1;
    v_stack_m230 = 0;
    v_stack_m238 = 0;
    v_stack_m240 = 0;
    result = KeWaitForMultipleObjects(1 + 7 - 6, v_stack_m188, 1, 1 + 7);
    if ((unsigned int)(result) != 0) goto loc_0031F086;
    goto loc_0031F4FF;
loc_0031F7C7:
    a1 = (*(unsigned __int64 *)(1 + 208)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(a1, v_stack_m188, 1, 1 + 7);
    result = MiZeroThreadContextSetExiting(*(unsigned __int64 *)(v_stack_m28 + 72), v_stack_m188, 1, 1 + 7);
    a1 = (*(unsigned __int64 *)(1 + 208)) + (0x3BB0ULL);
    result = MiReleaseSpinLockExclusive(a1, (unsigned __int8)((unsigned __int8)(result)), 1, 1 + 7);
    goto loc_0031F54E;
loc_0031F806:
    a2 = 0;
    result = MiInitializePageHeatList(v_stack_mC8, a2, (unsigned int)((unsigned int)((unsigned __int8)((unsigned __int8)(result)))), 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 672) = v_stack_mC8;
    goto loc_0031EFF1;
loc_0031F830:
    v_rbx = 0;
    goto loc_0031F1EA;
loc_0031F837:
    goto loc_0031F5AD;
loc_0031F846:
    v_rdi = 0;
}
```

## 5. (Beta) C Style

```c
int64_t MiBackgroundZeroLocalPages(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint8_t v_stack_m1C9;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1CF;
    uint32_t v_stack_m1D0;
    uint8_t v_stack_m1D5;
    uint8_t v_stack_m1D6;
    uint64_t v_stack_m1D7;
    uint8_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint32_t v_stack_m218;
    uint32_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint32_t v_stack_m248;
    uint32_t v_stack_m260;
    uint64_t v_stack_m28;
    uint32_t v_stack_m288;
    uint64_t v_stack_m38;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (608);
    result = (*(uint64_t *)(v_rip + 0xAEB7E2)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m178 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 144, a4);
    local_r12 = 0;
    v_stack_m170 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m248 = 0;
    v_stack_m238 = *(uint64_t *)(arg1 + 0x150);
    v_stack_m1F8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xB0) + 0x30);
    if (((*(uint32_t *)(v_rip + 0xCA7B02)) & (0x8400000ULL)) == 0) goto loc_0031EFF1;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xD0) == 0) goto loc_0031F806;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xD0) + 0x3B50)))) & (2)) == 0) goto loc_0031F806;
loc_0031EFF1:
    a3 = 0;
    Arg2 = 0;
    result = MiSetZeroPageThreadPriority(Arg1, Arg2, a3, a4);
    v_stack_m210 = (uint32_t)(result);
    v_stack_m208 = 0;
    result = KeQueryPerformanceCounter(v_stack_m208, Arg2, a3, a4);
    local_r14 = result;
    if (v_stack_m208 != 0x989680ULL) {
        result = (result) * (result);
        local_r14 = result;
    }
loc_0031F040:
    v_stack_m218 = 0;
    v_stack_m240 = local_r14;
    if (0 != 0) goto loc_0031F7C7;
    v_stack_m230 = 0;
    v_stack_m188 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xB0) + 0x30) + 88;
    v_stack_m180 = Arg1 + 392;
loc_0031F086:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x180)))) & (2)) != 0) goto loc_0031F49D;
loc_0031F094:
    if ((*(uint32_t *)(v_stack_m188 + 0x4)) != 0) goto loc_0031F4FF;
loc_0031F0A2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xB0) + 0x30) + 0x4230))) != 0) goto loc_0031F5C2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB18559))) != 0) goto loc_0031F5C2;
    result = 0;
    v_stack_m168 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    if ((*(uint64_t *)(arg1 + 0x160)) != (*(uint64_t *)(arg1 + 0x170))) goto loc_0031F673;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x168))) != (*(uint16_t *)(arg1 + 0x178))) goto loc_0031F673;
    if (*(uint64_t *)(arg1 + 0x160) == 0) goto loc_0031F673;
    if (((*(uint64_t *)(v_rip - 0x31F0CD + *(uint16_t *)(arg1 + 0x168) * 8 + 0xE2ED50)) & (*(uint64_t *)(arg1 + 0x160))) != 0) goto loc_0031F673;
loc_0031F120:
    local_rbx = 0;
    if (0 != 0) goto loc_0031F60F;
    if ((uint32_t)((uint32_t)(v_stack_m218)) == 0) goto loc_0031F662;
    *(uint64_t *)(arg1 + 0x120) = 0;
    v_stack_m240 = v_stack_m240;
loc_0031F160:
    *(uint64_t *)(0 + arg1 * 1 + 0x18) = 0;
    Arg1 = (32) - (1);
    if (condition_is_not_equal) goto loc_0031F160;
    *(uint32_t *)(arg1 + 0x118) = 0;
loc_0031F178:
    if (0 >= 1) goto loc_0031F2C9;
    v_stack_m228 = v_xmm0;
    v_stack_m218 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xD0);
    Arg1 = 0;
    a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xD0)) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xD0) + 0x3A88) + 0x10));
    a3 = (a3) >> (7);
    a3 = (a3) * (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xD0) + 0x3A88));
    a3 = (uint32_t)((a3) + 1);
    result = MiInitializePageColorBase(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m218))), a3, v_stack_m228);
    v_stack_m228 = Arg1 + (uint32_t)(v_stack_m218) + 148 * 4;
loc_0031F1EA:
    if (3 == 0) goto loc_0031F837;
    local_r15 = (uint32_t)((3) - 1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m220)))) & (0xFFF3FFFFULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (3));
    Arg1 = (uint32_t)((Arg1) << (18));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | ((uint32_t)(result)));
    v_stack_m220 = (uint32_t)(a4);
loc_0031F214:
    if (0 > 1) goto loc_0031F1EA;
    result = (uint32_t)((0) << (15));
    result = (uint32_t)((result) ^ ((uint32_t)(a4)));
    result = (uint32_t)((result) & (0x8000ULL));
    a4 = (uint32_t)((a4) ^ ((uint32_t)(result)));
    v_stack_m220 = (uint32_t)(a4);
    Arg2 = 0;
    Arg1 = ((uint32_t)((uint32_t)(a4))) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(a4)));
    local_rbx = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(a4)));
    local_r14 = 0;
loc_0031F26D:
    if (0 < (*(uint8_t *)(v_rip + 0xCA5D8E))) goto loc_0031F289;
    if (((uint32_t)((uint32_t)(v_stack_m218))) == 3) goto loc_0031F830;
    local_rsi = (uint32_t)((0) + 1);
    goto loc_0031F214;
loc_0031F289:
    if (0 == 2) goto loc_0031F5FD;
loc_0031F297:
    result = (uint32_t)((0) << (8));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (256));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    result = MiGetBestPageToZero(Arg1, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if (result == 0) goto loc_0031F495;
    local_r12 = (uint32_t)((0) + 1);
    local_rbx = 0;
    goto loc_0031F178;
loc_0031F2C9:
    result = MiMapBackgroundPagesToZero(Arg1, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    v_stack_m240 = v_stack_m240;
loc_0031F2EA:
    if ((uint32_t)(result) == 0) goto loc_0031F5AD;
    v_stack_m1CF = 0;
    v_stack_m1F0 = 0;
    v_stack_m1D7 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1C9 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150) + 0xB0) + 0x38)));
    v_stack_m1C0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1B8 = v_stack_m1F8;
    v_stack_m1D8 = 17;
    v_stack_m1B0 = Arg1;
    v_stack_m198 = Arg1;
    v_stack_m1CC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x140)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x140)))) < 3) goto loc_0031F713;
loc_0031F353:
    result = MiTryZeroMemory(Arg1, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    v_stack_m248 = (uint32_t)(result);
loc_0031F371:
    result = MiLockMultipleZeroChunks(v_stack_m1D8, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if (v_stack_m1D0 == 0) goto loc_0031F3C9;
    result = MiExamineZeroChunks(v_stack_m1D8, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    result = MiMoveZeroedPages(v_stack_m1D8, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if ((*(uint32_t *)(arg1 + 0x140)) == 0) goto loc_0031F75D;
loc_0031F3AD:
    result = MiUnlockMultipleZeroChunks(v_stack_m1D8, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if (v_stack_m1D5 != 0) goto loc_0031F846;
    if ((*(uint32_t *)(arg1 + 0x140)) != 0) goto loc_0031F371;
loc_0031F3C9:
    if (((uint32_t)((uint32_t)(v_stack_m218))) != 3) goto loc_0031F6FC;
loc_0031F3DF:
    result = (1) + (1);
    if (result < 0x1000ULL) goto loc_0031F040;
    v_stack_m1E8 = 0;
    result = KeQueryPerformanceCounter(v_stack_m1E8, v_stack_m218, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if (v_stack_m1E8 != 0x989680ULL) {
        result = (result) * (result);
    }
    local_r15 = v_stack_m240;
    if (result >= v_stack_m240) { local_r15 = result; }
    local_r15 = (local_r15) - (v_stack_m240);
    result = MiReassessZeroThreads(Arg1, local_r15, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    v_stack_m1E0 = 0;
    result = KeQueryPerformanceCounter(v_stack_m1E0, local_r15, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    local_r14 = result;
    if (v_stack_m1E0 != 0x989680ULL) {
        result = (result) * (result);
        local_r14 = result;
    }
    goto loc_0031F040;
loc_0031F495:
    local_r14 = (uint8_t)((local_r14) + 1);
    goto loc_0031F26D;
loc_0031F49D:
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m218) + 0xD0)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(Arg1, local_r15, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m218) + 0xD0)) + (0x3BB0ULL);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(Arg1, local_r15, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_0031F4EC;
    if ((*(uint32_t *)(v_rip + 0xCA7847)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    }
loc_0031F4EC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x180)))) & (2)) != 0) goto loc_0031F777;
    goto loc_0031F094;
loc_0031F4FF:
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m218) + 0xD0)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    result = MiZeroThreadContextSetExiting(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m218) + 0xD0)) + (0x3BB0ULL);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_0031F548;
    if ((*(uint32_t *)(v_rip + 0xCA77EB)) != 0) {
        Arg1 = (uint8_t)(result);
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    }
loc_0031F548:
loc_0031F54E:
    local_rbx = 0;
loc_0031F550:
    result = MiZeroThreadContextPrepareToWait(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m220));
    a3 = 0;
    *(uint64_t *)(arg1 + 0x2A0) = 0;
    result = MiSetZeroPageThreadPriority(Arg1, (uint32_t)(v_stack_m210), a3, (uint32_t)(v_stack_m220));
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(v_stack_m210), a3, (uint32_t)(v_stack_m220));
    return result;
loc_0031F5AD:
    if (((uint32_t)((uint32_t)(v_stack_m218))) >= 3) goto loc_0031F550;
    local_r13 = (uint32_t)(((uint32_t)(v_stack_m218)) + 1);
    local_r12 = 0;
    goto loc_0031F040;
loc_0031F5C2:
    result = MiZeroThreadContextPrepareToWait(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(v_stack_m210), a3, (uint32_t)(v_stack_m220));
    a4 = 0;
    v_stack_m240 = v_rip - 3205941;
    a3 = 0;
    result = KeWaitForSingleObject(v_stack_m188, a4 + 8, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0031F0A2;
    goto loc_0031F4FF;
loc_0031F5FD:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13 + 208))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (63));
    result = MiAssignDefaultChannel(Arg1, a4 + 8, a3, a4);
    goto loc_0031F297;
loc_0031F60F:
    v_stack_m200 = local_r13 + 208;
    result = KeQueryPerformanceCounter(v_stack_m200, a4 + 8, a3, a4);
    v_stack_m218 = result;
    local_r14 = result;
    if (v_stack_m200 != 0x989680ULL) {
        result = (result) * (result);
        local_r14 = result;
        v_stack_m218 = result;
    }
loc_0031F662:
    result = MiGetBackgroundHugePageToZero(v_stack_m1F8, *(uint64_t *)(v_stack_m28 + 0x48), a3, a4);
    goto loc_0031F2EA;
loc_0031F673:
    Arg1 = (*(uint64_t *)((uint32_t)((uint32_t)(local_r13 + 0xD0)) + 0xD0)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(Arg1, *(uint64_t *)(v_stack_m28 + 0x48), a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x160)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x48);
        result = MiUnlinkZeroThreadFromActiveDomain(Arg1, *(uint64_t *)(v_stack_m28 + 0x48), a3, a4);
    }
    a3 = 0;
    result = MiFindBestZeroingProcessor(v_stack_m168, (uint32_t)((uint32_t)(local_r13 + 208)), a3, 1);
    if (((uint32_t)((int32_t)(v_stack_m140))) == 5) goto loc_0031F76D;
    result = MiAssignBackgroundZeroThreadToProcessor(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(local_r13 + 208)), v_stack_m168, 1);
loc_0031F6E1:
    Arg1 = (*(uint64_t *)((uint32_t)((uint32_t)(local_r13 + 0xD0)) + 0xD0)) + (0x3BB0ULL);
    result = MiReleaseSpinLockExclusive(Arg1, (uint8_t)((uint8_t)(result)), v_stack_m168, 1);
    goto loc_0031F120;
loc_0031F6FC:
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13 + 208))));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r13 + 208)))) < 1) { result = (uint32_t)(Arg1); }
    goto loc_0031F3DF;
loc_0031F713:
    if ((uint32_t)((uint8_t)(result)) == 0) goto loc_0031F73D;
    if (((uint32_t)((uint8_t)(result))) < 1) goto loc_0031F353;
    if (((*(uint32_t *)(v_rip + 0xCA738E)) & (0x200000ULL)) == 0) goto loc_0031F353;
    result = MiZeroPageMakeHot(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)((uint8_t)(result)), v_stack_m168, 1);
    goto loc_0031F353;
loc_0031F73D:
    result = MiGetZeroingContext(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)((uint8_t)(result)), v_stack_m168, 1);
    v_stack_m198 = result;
    v_stack_m1A0 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x248);
    v_stack_m1D6 = 1;
    goto loc_0031F353;
loc_0031F75D:
    v_stack_m1F0 = *(uint64_t *)((uint8_t)(result));
    goto loc_0031F3AD;
loc_0031F76D:
    result = MiDecrementZeroEngineThread(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)((uint8_t)(result)), v_stack_m168, 1);
    goto loc_0031F6E1;
loc_0031F777:
    result = MiZeroThreadContextPrepareToWait(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)((uint8_t)(result)), v_stack_m168, 1);
    v_stack_m228 = v_stack_m128;
    v_stack_m208 = 1;
    v_stack_m230 = 0;
    v_stack_m238 = 0;
    v_stack_m240 = 0;
    result = KeWaitForMultipleObjects(1 + 7 - 6, v_stack_m188, 1, 1 + 7);
    if ((uint32_t)(result) != 0) goto loc_0031F086;
    goto loc_0031F4FF;
loc_0031F7C7:
    Arg1 = (*(uint64_t *)(1 + 0xD0)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(Arg1, v_stack_m188, 1, 1 + 7);
    result = MiZeroThreadContextSetExiting(*(uint64_t *)(v_stack_m28 + 0x48), v_stack_m188, 1, 1 + 7);
    Arg1 = (*(uint64_t *)(1 + 0xD0)) + (0x3BB0ULL);
    result = MiReleaseSpinLockExclusive(Arg1, (uint8_t)((uint8_t)(result)), 1, 1 + 7);
    goto loc_0031F54E;
loc_0031F806:
    Arg2 = 0;
    result = MiInitializePageHeatList(v_stack_mC8, Arg2, (uint32_t)((uint32_t)((uint8_t)((uint8_t)(result)))), 16);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x2A0) = v_stack_mC8;
    goto loc_0031EFF1;
loc_0031F830:
    local_rbx = 0;
    goto loc_0031F1EA;
loc_0031F837:
    goto loc_0031F5AD;
loc_0031F846:
    local_rdi = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*4` | `64` | `R` |
| `Arg1` | `+ 0x118` | `32` | `W` |
| `Arg1` | `+ 0x120` | `64` | `W` |
| `Arg1` | `+ 0x140` | `32` | `R` |
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |
| `Arg1` | `+ 0x168` | `16` | `R` |
| `Arg1` | `+ 0x170` | `64` | `R` |
| `Arg1` | `+ 0x178` | `16` | `R` |
| `Arg1` | `+ 0x180` | `32` | `R` |
| `Arg1` | `+ 0x184` | `32` | `R/W` |
| `Arg1` | `+ 0x188` | `64` | `R` |
| `Arg1` | `+ 0x248` | `64` | `R` |
| `Arg1` | `+ 0x2A0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031EF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
