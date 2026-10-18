# IoSetIoCompletionEx3

- RVA: `0x0024EEE0`–`0x0024F326` (길이 `1,094` bytes)
- VA: `0x000000014024EEE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000632DC`
- 디코드: `251`개 명령, `1,094/1,094` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0024EFC5` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0024F06B` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x0024F139` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (function, `0x009DA2E0`)
- `0x0024F1DA` → [KiWakeOtherQueueWaiters](../39/KiWakeOtherQueueWaiters_function_003964D0.md) (function, `0x003964D0`)
- `0x0024F20D` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x0024F258` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0024F27D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0024F28C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024F299` → [KeIsThreadRunning](../39/KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x0024F2A8` → [EtwTraceEnqueueWork](../39/EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)

### Direct callers
- [ExpShutdownWorkerFactory](../2A/ExpShutdownWorkerFactory_function_002A4F70.md) at `0x002A50AB`
- [ExpWorkerFactoryCompletionPacketRoutine](../34/ExpWorkerFactoryCompletionPacketRoutine_function_00344810.md) at `0x00344927`

### Static image references
- `0x0024EF56` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0024EF6C` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0024F17F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0024F26F` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0024F139` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0024EEE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0024EEE5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0024EEEA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0024EEEF  57                              push rdi
0024EEF0  41 54                           push r12
0024EEF2  41 55                           push r13
0024EEF4  41 56                           push r14
0024EEF6  41 57                           push r15
0024EEF8  48 83 EC 40                     sub rsp, 0x40
0024EEFC  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0024EF04  41 8B D9                        mov ebx, r9d
0024EF07  49 8B F8                        mov rdi, r8
0024EF0A  48 8B F2                        mov rsi, rdx
0024EF0D  4C 8B F1                        mov r14, rcx
0024EF10  4D 85 FF                        test r15, r15
0024EF13  0F 84 16 02 00 00               je 0x14024f12f
0024EF19  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0024EF21  49 89 7F 20                     mov qword ptr [r15 + 0x20], rdi
0024EF25  0F BE BC 24 B0 00 00 00         movsx edi, byte ptr [rsp + 0xb0]
0024EF2D  49 89 77 18                     mov qword ptr [r15 + 0x18], rsi
0024EF31  49 8D 76 08                     lea rsi, [r14 + 8]
0024EF35  89 BC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edi
0024EF3C  41 89 5F 28                     mov dword ptr [r15 + 0x28], ebx
0024EF40  49 89 47 30                     mov qword ptr [r15 + 0x30], rax
0024EF44  44 0F 20 C0                     mov rax, cr8
0024EF48  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0024EF4D  B9 02 00 00 00                  mov ecx, 2
0024EF52  44 0F 22 C1                     mov cr8, rcx
0024EF56  83 3D C3 7D D7 00 00            cmp dword ptr [rip + 0xd77dc3], 0
0024EF5D  0F 85 EF 02 00 00               jne 0x14024f252
0024EF63  65 48 8B 2C 25 20 00 00 00      mov rbp, qword ptr gs:[0x20]
0024EF6C  F7 05 8E 7B D7 00 00 00 00 01   test dword ptr [rip + 0xd77b8e], 0x1000000
0024EF76  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
0024EF7B  48 8B 5D 08                     mov rbx, qword ptr [rbp + 8]
0024EF7F  0F 85 11 03 00 00               jne 0x14024f296
0024EF85  85 FF                           test edi, edi
0024EF87  0F 85 87 01 00 00               jne 0x14024f114
0024EF8D  45 33 ED                        xor r13d, r13d
0024EF90  48 8B 83 50 06 00 00            mov rax, qword ptr [rbx + 0x650]
0024EF97  48 85 C0                        test rax, rax
0024EF9A  48 0F 44 C3                     cmove rax, rbx
0024EF9E  80 BC 24 A8 00 00 00 00         cmp byte ptr [rsp + 0xa8], 0
0024EFA6  74 17                           je 0x14024efbf
0024EFA8  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
0024EFAF  8B 80 88 00 00 00               mov eax, dword ptr [rax + 0x88]
0024EFB5  0F BA E0 0D                     bt eax, 0xd
0024EFB9  0F 82 0E 03 00 00               jb 0x14024f2cd
0024EFBF  40 32 FF                        xor dil, dil
0024EFC2  49 8B CE                        mov rcx, r14
0024EFC5  E8 C6 2C 00 00                  call 0x140251c90
0024EFCA  48 39 36                        cmp qword ptr [rsi], rsi
0024EFCD  0F 84 CE 01 00 00               je 0x14024f1a1
0024EFD3  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0024EFD7  41 3B 46 2C                     cmp eax, dword ptr [r14 + 0x2c]
0024EFDB  0F 83 B7 01 00 00               jae 0x14024f198
0024EFE1  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
0024EFE8  49 3B C6                        cmp rax, r14
0024EFEB  0F 84 CA 02 00 00               je 0x14024f2bb
0024EFF1  48 8B 36                        mov rsi, qword ptr [rsi]
0024EFF4  0F 1F 40 00                     nop dword ptr [rax]
0024EFF8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0024F000  48 8B FE                        mov rdi, rsi
0024F003  48 8B 36                        mov rsi, qword ptr [rsi]
0024F006  80 7F 10 03                     cmp byte ptr [rdi + 0x10], 3
0024F00A  0F 85 ED 00 00 00               jne 0x14024f0fd
0024F010  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0024F014  48 39 7E 08                     cmp qword ptr [rsi + 8], rdi
0024F018  75 09                           jne 0x14024f023
0024F01A  48 39 38                        cmp qword ptr [rax], rdi
0024F01D  0F 84 32 01 00 00               je 0x14024f155
0024F023  B9 03 00 00 00                  mov ecx, 3
0024F028  CD 29                           int 0x29
0024F02A  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
0024F031  3C 05                           cmp al, 5
0024F033  0F 85 A1 00 00 00               jne 0x14024f0da
0024F039  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
0024F03D  8B C1                           mov eax, ecx
0024F03F  83 E0 07                        and eax, 7
0024F042  83 F8 01                        cmp eax, 1
0024F045  0F 85 8A 02 00 00               jne 0x14024f2d5
0024F04B  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
0024F052  48 85 D2                        test rdx, rdx
0024F055  74 11                           je 0x14024f068
0024F057  0F B6 02                        movzx eax, byte ptr [rdx]
0024F05A  24 7F                           and al, 0x7f
0024F05C  3C 15                           cmp al, 0x15
0024F05E  0F 84 D2 01 00 00               je 0x14024f236
0024F064  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
0024F068  48 8B CB                        mov rcx, rbx
0024F06B  E8 60 12 00 00                  call 0x1402502d0
0024F070  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
0024F077  3C 01                           cmp al, 1
0024F079  0F 84 33 02 00 00               je 0x14024f2b2
0024F07F  3C 05                           cmp al, 5
0024F081  75 22                           jne 0x14024f0a5
0024F083  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0024F08D  8B 08                           mov ecx, dword ptr [rax]
0024F08F  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
0024F095  44 38 A3 87 01 00 00            cmp byte ptr [rbx + 0x187], r12b
0024F09C  74 6D                           je 0x14024f10b
0024F09E  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
0024F0A5  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0024F0AA  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
0024F0B1  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
0024F0B8  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
0024F0BF  48 89 01                        mov qword ptr [rcx], rax
0024F0C2  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
0024F0C9  4C 89 BB C8 00 00 00            mov qword ptr [rbx + 0xc8], r15
0024F0D0  4C 89 AB D0 03 00 00            mov qword ptr [rbx + 0x3d0], r13
0024F0D7  41 B4 01                        mov r12b, 1
0024F0DA  4C 89 6B 40                     mov qword ptr [rbx + 0x40], r13
0024F0DE  0F B6 47 11                     movzx eax, byte ptr [rdi + 0x11]
0024F0E2  FE C0                           inc al
0024F0E4  88 47 11                        mov byte ptr [rdi + 0x11], al
0024F0E7  45 84 E4                        test r12b, r12b
0024F0EA  0F 85 72 01 00 00               jne 0x14024f262
0024F0F0  49 8D 46 08                     lea rax, [r14 + 8]
0024F0F4  48 3B F0                        cmp rsi, rax
0024F0F7  0F 85 03 FF FF FF               jne 0x14024f000
0024F0FD  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
0024F102  49 8D 76 08                     lea rsi, [r14 + 8]
0024F106  E9 96 00 00 00                  jmp 0x14024f1a1
0024F10B  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
0024F112  EB 91                           jmp 0x14024f0a5
0024F114  41 F6 46 01 02                  test byte ptr [r14 + 1], 2
0024F119  41 BD 00 00 00 00               mov r13d, 0
0024F11F  41 0F 45 FD                     cmovne edi, r13d
0024F123  89 BC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edi
0024F12A  E9 61 FE FF FF                  jmp 0x14024ef90
0024F12F  0F B6 94 24 98 00 00 00         movzx edx, byte ptr [rsp + 0x98]
0024F137  B1 01                           mov cl, 1
0024F139  E8 A2 B1 78 00                  call 0x1409da2e0
0024F13E  4C 8B F8                        mov r15, rax
0024F141  48 85 C0                        test rax, rax
0024F144  0F 85 CF FD FF FF               jne 0x14024ef19
0024F14A  41 BD 9A 00 00 C0               mov r13d, 0xc000009a
0024F150  E9 BD 00 00 00                  jmp 0x14024f212
0024F155  48 89 30                        mov qword ptr [rax], rsi
0024F158  45 32 E4                        xor r12b, r12b
0024F15B  48 89 46 08                     mov qword ptr [rsi + 8], rax
0024F15F  41 8B ED                        mov ebp, r13d
0024F162  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
0024F166  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
0024F170  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0024F177  0F 83 AD FE FF FF               jae 0x14024f02a
0024F17D  FF C5                           inc ebp
0024F17F  85 2D 27 61 D7 00               test dword ptr [rip + 0xd76127], ebp
0024F185  0F 84 E4 00 00 00               je 0x14024f26f
0024F18B  F3 90                           pause
0024F18D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0024F191  48 85 C0                        test rax, rax
0024F194  74 DA                           je 0x14024f170
0024F196  EB E5                           jmp 0x14024f17d
0024F198  40 84 FF                        test dil, dil
0024F19B  0F 85 40 FE FF FF               jne 0x14024efe1
0024F1A1  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0024F1A5  8D 41 01                        lea eax, [rcx + 1]
0024F1A8  41 89 46 04                     mov dword ptr [r14 + 4], eax
0024F1AC  49 8D 46 18                     lea rax, [r14 + 0x18]
0024F1B0  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0024F1B4  48 39 02                        cmp qword ptr [rdx], rax
0024F1B7  0F 85 66 FE FF FF               jne 0x14024f023
0024F1BD  49 89 07                        mov qword ptr [r15], rax
0024F1C0  49 89 57 08                     mov qword ptr [r15 + 8], rdx
0024F1C4  4C 89 3A                        mov qword ptr [rdx], r15
0024F1C7  4C 89 78 08                     mov qword ptr [rax + 8], r15
0024F1CB  85 C9                           test ecx, ecx
0024F1CD  75 10                           jne 0x14024f1df
0024F1CF  48 39 36                        cmp qword ptr [rsi], rsi
0024F1D2  74 0B                           je 0x14024f1df
0024F1D4  49 8B D6                        mov rdx, r14
0024F1D7  48 8B CD                        mov rcx, rbp
0024F1DA  E8 F1 72 14 00                  call 0x1403964d0
0024F1DF  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0024F1E7  F6 9C 24 A8 00 00 00            neg byte ptr [rsp + 0xa8]
0024F1EE  41 B8 01 00 00 00               mov r8d, 1
0024F1F4  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0024F1F9  48 8B CD                        mov rcx, rbp
0024F1FC  44 8B 8C 24 A0 00 00 00         mov r9d, dword ptr [rsp + 0xa0]
0024F204  1B D2                           sbb edx, edx
0024F206  83 E2 03                        and edx, 3
0024F209  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0024F20D  E8 DE 2A 00 00                  call 0x140251cf0
0024F212  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0024F217  41 8B C5                        mov eax, r13d
0024F21A  48 8B 6C 24 78                  mov rbp, qword ptr [rsp + 0x78]
0024F21F  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0024F227  48 83 C4 40                     add rsp, 0x40
0024F22B  41 5F                           pop r15
0024F22D  41 5E                           pop r14
0024F22F  41 5D                           pop r13
0024F231  41 5C                           pop r12
0024F233  5F                              pop rdi
0024F234  C3                              ret
0024F235  CC                              int3
0024F236  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
0024F23C  0F B6 C0                        movzx eax, al
0024F23F  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
0024F245  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
0024F24D  E9 16 FE FF FF                  jmp 0x14024f068
0024F252  0F B6 D1                        movzx edx, cl
0024F255  0F B6 C8                        movzx ecx, al
0024F258  E8 9F 64 2A 00                  call 0x1404f56fc
0024F25D  E9 01 FD FF FF                  jmp 0x14024ef63
0024F262  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
0024F267  4D 89 2F                        mov qword ptr [r15], r13
0024F26A  E9 70 FF FF FF                  jmp 0x14024f1df
0024F26F  8B 05 43 78 D7 00               mov eax, dword ptr [rip + 0xd77843]
0024F275  A8 40                           test al, 0x40
0024F277  0F 84 0E FF FF FF               je 0x14024f18b
0024F27D  E8 0E 02 0C 00                  call 0x14030f490
0024F282  84 C0                           test al, al
0024F284  0F 84 01 FF FF FF               je 0x14024f18b
0024F28A  8B CD                           mov ecx, ebp
0024F28C  E8 CF 01 0C 00                  call 0x14030f460
0024F291  E9 F7 FE FF FF                  jmp 0x14024f18d
0024F296  48 8B CB                        mov rcx, rbx
0024F299  E8 82 74 14 00                  call 0x140396720
0024F29E  44 0F B6 C0                     movzx r8d, al
0024F2A2  48 8B CB                        mov rcx, rbx
0024F2A5  49 8B D7                        mov rdx, r15
0024F2A8  E8 9F 74 14 00                  call 0x14039674c
0024F2AD  E9 D3 FC FF FF                  jmp 0x14024ef85
0024F2B2  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
0024F2B6  E9 EA FD FF FF                  jmp 0x14024f0a5
0024F2BB  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
0024F2C2  0F 85 29 FD FF FF               jne 0x14024eff1
0024F2C8  E9 D4 FE FF FF                  jmp 0x14024f1a1
0024F2CD  40 B7 01                        mov dil, 1
0024F2D0  E9 ED FC FF FF                  jmp 0x14024efc2
0024F2D5  83 F8 04                        cmp eax, 4
0024F2D8  0F 84 6D FD FF FF               je 0x14024f04b
0024F2DE  85 C0                           test eax, eax
0024F2E0  75 1F                           jne 0x14024f301
0024F2E2  80 E1 FA                        and cl, 0xfa
0024F2E5  80 C9 02                        or cl, 2
0024F2E8  88 4B 70                        mov byte ptr [rbx + 0x70], cl
0024F2EB  4C 89 BB C8 00 00 00            mov qword ptr [rbx + 0xc8], r15
0024F2F2  4C 89 AB D0 03 00 00            mov qword ptr [rbx + 0x3d0], r13
0024F2F9  88 47 11                        mov byte ptr [rdi + 0x11], al
0024F2FC  E9 D6 FD FF FF                  jmp 0x14024f0d7
0024F301  83 F8 05                        cmp eax, 5
0024F304  75 0E                           jne 0x14024f314
0024F306  80 E1 FE                        and cl, 0xfe
0024F309  80 C9 06                        or cl, 6
0024F30C  88 4B 70                        mov byte ptr [rbx + 0x70], cl
0024F30F  E9 C6 FD FF FF                  jmp 0x14024f0da
0024F314  83 F8 03                        cmp eax, 3
0024F317  0F 85 BD FD FF FF               jne 0x14024f0da
0024F31D  C6 47 11 02                     mov byte ptr [rdi + 0x11], 2
0024F321  E9 B4 FD FF FF                  jmp 0x14024f0da
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetIoCompletionEx3(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned __int8 a6, unsigned int a7, unsigned __int8 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    if (a7 == 0) goto loc_0024F12F;
loc_0024EF19:
    *(unsigned __int64 *)(a7 + 32) = a3;
    *(unsigned __int64 *)(a7 + 24) = a2;
    v_stack_p38 = (unsigned int)((__int8)(a9));
    *(unsigned int *)(a7 + 40) = (unsigned int)((unsigned int)(a4));
    *(unsigned __int64 *)(a7 + 48) = a5;
    v_stack_m30 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14122435)) != 0) goto loc_0024F252;
loc_0024EF63:
    v_stack_m38 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (((*(unsigned int *)(v_rip + 14121870)) & (0x1000000ULL)) != 0) goto loc_0024F296;
loc_0024EF85:
    if ((unsigned int)((__int8)(a9)) != 0) goto loc_0024F114;
    v_r13 = 0;
loc_0024EF90:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616) == 0) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8); }
    if (a8 == 0) goto loc_0024EFBF;
    if (a8 < 0) goto loc_0024F2CD;
loc_0024EFBF:
    v_rdi = 0;
loc_0024EFC2:
    result = KiAcquireKobjectLockSafe(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_0024F1A1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) >= (*(unsigned int *)(a1 + 44))) goto loc_0024F198;
loc_0024EFE1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232)) == a1) goto loc_0024F2BB;
loc_0024EFF1:
loc_0024F000:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16)) != 3) goto loc_0024F0FD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_0024F023;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 8))) goto loc_0024F155;
loc_0024F023:
loc_0024F02A:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_0024F0DA;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_0024F2D5;
loc_0024F04B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232) == 0) goto loc_0024F068;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_0024F236;
loc_0024F068:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232), a3, a4);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) == 1) goto loc_0024F2B2;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_0024F0A5;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388)))) - (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 436)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 391)) == ((unsigned __int8)(v_r12))) goto loc_0024F10B;
loc_0024F0A5:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216) = *(unsigned __int64 *)(v_stack_m38 + 11528);
    *(unsigned __int64 *)(v_stack_m38 + 11528) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 200) = a7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 976) = 0;
loc_0024F0D7:
loc_0024F0DA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = (unsigned __int8)(result);
    if (1 != 0) goto loc_0024F262;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != (a1 + 8)) goto loc_0024F000;
loc_0024F0FD:
    goto loc_0024F1A1;
loc_0024F10B:
    goto loc_0024F0A5;
loc_0024F114:
    v_rdi = *(unsigned __int64 *)(a1 + 8);
    if (((*(unsigned __int8 *)(a1 + 1)) & (2)) != 0) { v_rdi = 0; }
    v_stack_p38 = (unsigned int)(v_rdi);
    goto loc_0024EF90;
loc_0024F12F:
    result = IopAllocateMiniCompletionPacket(1, a6, a3, a4);
    if (result != 0) goto loc_0024EF19;
    goto loc_0024F212;
loc_0024F155:
    *(unsigned __int64 *)(result) = a1 + 8;
    v_r12 = 0;
    *(unsigned __int64 *)(a1 + 8 + 8) = result;
loc_0024F170:
    if (condition_is_above_or_equal) goto loc_0024F02A;
loc_0024F17D:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))) + 1);
    if (((*(unsigned int *)(v_rip + 14115111)) & ((unsigned int)(v_rbp))) == 0) goto loc_0024F26F;
loc_0024F18B:
loc_0024F18D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 64) == 0) goto loc_0024F170;
    goto loc_0024F17D;
loc_0024F198:
    if ((unsigned __int8)(v_rdi) != 0) goto loc_0024EFE1;
loc_0024F1A1:
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) != (a1 + 24)) goto loc_0024F023;
    *(unsigned __int64 *)(result) = a1 + 24;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8)) = result;
    *(unsigned __int64 *)(a1 + 24 + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) goto loc_0024F1DF;
    result = a1 + 24;
    if ((*(unsigned __int64 *)(a1 + 8)) != (a1 + 8)) {
        a2 = a1;
        a1 = v_rbp;
        result = KiWakeOtherQueueWaiters(a1, a2, a3, a4);
    }
    a2 = (unsigned int)((a2) & (3));
    v_stack_m48 = (unsigned __int8)(v_stack_m30);
    result = KiExitDispatcher(v_rbp, a2, 1, (unsigned int)(a7));
loc_0024F212:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
loc_0024F236:
    *(unsigned int *)(v_stack_p8 + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540))));
    goto loc_0024F068;
loc_0024F252:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540)))), (unsigned __int8)(v_rbp), 1, (unsigned int)(a7));
    goto loc_0024EF63;
loc_0024F262:
    *(unsigned __int64 *)(result) = (unsigned int)(0xC000009AULL);
    goto loc_0024F1DF;
loc_0024F26F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14121027)))) & (64)) == 0) goto loc_0024F18B;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540)))), (unsigned __int8)(v_rbp), 1, (unsigned int)(a7));
    if ((unsigned __int8)(result) == 0) goto loc_0024F18B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p30)), (unsigned __int8)(v_rbp), 1, (unsigned int)(a7));
    goto loc_0024F18D;
loc_0024F296:
    result = KeIsThreadRunning(v_stack_p8, (unsigned __int8)(v_rbp), 1, (unsigned int)(a7));
    result = EtwTraceEnqueueWork(v_stack_p8, result, (unsigned __int8)(result), (unsigned int)(a7));
    goto loc_0024EF85;
loc_0024F2B2:
    goto loc_0024F0A5;
loc_0024F2BB:
    if ((*(unsigned __int8 *)(v_stack_p8 + 643)) != 15) goto loc_0024EFF1;
    goto loc_0024F1A1;
loc_0024F2CD:
    goto loc_0024EFC2;
loc_0024F2D5:
    if (((unsigned int)(result)) == 4) goto loc_0024F04B;
    if ((unsigned int)(result) != 0) goto loc_0024F301;
    a1 = (unsigned __int8)((v_stack_p8) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p8 + 112) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(v_stack_p8 + 200) = result;
    *(unsigned __int64 *)(v_stack_p8 + 976) = (unsigned int)(0xC000009AULL);
    *(unsigned __int8 *)(1 + 17) = (unsigned __int8)(result);
    goto loc_0024F0D7;
loc_0024F301:
    if (((unsigned int)(result)) != 5) goto loc_0024F314;
    a1 = (unsigned __int8)((a1) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_stack_p8 + 112) = (unsigned __int8)(a1);
    goto loc_0024F0DA;
loc_0024F314:
    if (((unsigned int)(result)) != 3) goto loc_0024F0DA;
    *(unsigned __int8 *)(1 + 17) = 2;
    goto loc_0024F0DA;
}
```

## 5. (Beta) C Style

```c
int64_t IoSetIoCompletionEx3(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint8_t Arg6, uint32_t Arg7, uint8_t Arg8, uint8_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint8_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    if (Arg7 == 0) goto loc_0024F12F;
loc_0024EF19:
    *(uint64_t *)(Arg7 + 0x20) = Arg3;
    *(uint64_t *)(Arg7 + 0x18) = Arg2;
    v_stack_p38 = (uint32_t)((int8_t)(Arg9));
    *(uint32_t *)(Arg7 + 0x28) = (uint32_t)((uint32_t)(Arg4));
    *(uint64_t *)(Arg7 + 0x30) = Arg5;
    v_stack_m30 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD77DC3)) != 0) goto loc_0024F252;
loc_0024EF63:
    v_stack_m38 = *(uint64_t *)(gs_base + (0 + 0x20));
    if (((*(uint32_t *)(v_rip + 0xD77B8E)) & (0x1000000ULL)) != 0) goto loc_0024F296;
loc_0024EF85:
    if ((uint32_t)((int8_t)(Arg9)) != 0) goto loc_0024F114;
    local_r13 = 0;
loc_0024EF90:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650) == 0) { result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8); }
    if (Arg8 == 0) goto loc_0024EFBF;
    if (Arg8 < 0) goto loc_0024F2CD;
loc_0024EFBF:
    local_rdi = 0;
loc_0024EFC2:
    result = KiAcquireKobjectLockSafe(Arg1, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_0024F1A1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) >= (*(uint32_t *)(arg1 + 0x2C))) goto loc_0024F198;
loc_0024EFE1:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8)) == Arg1) goto loc_0024F2BB;
loc_0024EFF1:
loc_0024F000:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)) != 3) goto loc_0024F0FD;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_0024F023;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x8))) goto loc_0024F155;
loc_0024F023:
loc_0024F02A:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_0024F0DA;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_0024F2D5;
loc_0024F04B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8) == 0) goto loc_0024F068;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_0024F236;
loc_0024F068:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8), Arg3, Arg4);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) == 1) goto loc_0024F2B2;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_0024F0A5;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184)))) - (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x1B4)));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x187)) == ((uint8_t)(local_r12))) goto loc_0024F10B;
loc_0024F0A5:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184) = 7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xD8) = *(uint64_t *)(v_stack_m38 + 0x2D08);
    *(uint64_t *)(v_stack_m38 + 0x2D08) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 216;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xC8) = Arg7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x3D0) = 0;
loc_0024F0D7:
loc_0024F0DA:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11)) + 1);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = (uint8_t)(result);
    if (1 != 0) goto loc_0024F262;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != (Arg1 + 8)) goto loc_0024F000;
loc_0024F0FD:
    goto loc_0024F1A1;
loc_0024F10B:
    goto loc_0024F0A5;
loc_0024F114:
    local_rdi = *(uint64_t *)(arg1 + 0x8);
    if (((*(uint8_t *)(arg1 + 0x1)) & (2)) != 0) { local_rdi = 0; }
    v_stack_p38 = (uint32_t)(local_rdi);
    goto loc_0024EF90;
loc_0024F12F:
    result = IopAllocateMiniCompletionPacket(1, Arg6, Arg3, Arg4);
    if (result != 0) goto loc_0024EF19;
    goto loc_0024F212;
loc_0024F155:
    *(void **)(result) = Arg1 + 8;
    local_r12 = 0;
    *(uint64_t *)(arg1 + 0x8 + 0x8) = result;
loc_0024F170:
    if (condition_is_above_or_equal) goto loc_0024F02A;
loc_0024F17D:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD76127)) & ((uint32_t)(local_rbp))) == 0) goto loc_0024F26F;
loc_0024F18B:
loc_0024F18D:
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x40) == 0) goto loc_0024F170;
    goto loc_0024F17D;
loc_0024F198:
    if ((uint8_t)(local_rdi) != 0) goto loc_0024EFE1;
loc_0024F1A1:
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) != (Arg1 + 24)) goto loc_0024F023;
    *(void **)(result) = Arg1 + 24;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0x18 + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) goto loc_0024F1DF;
    result = Arg1 + 24;
    if ((*(uint64_t *)(arg1 + 0x8)) != (Arg1 + 8)) {
        Arg2 = Arg1;
        Arg1 = local_rbp;
        result = KiWakeOtherQueueWaiters(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = (uint32_t)((Arg2) & (3));
    v_stack_m48 = (uint8_t)(v_stack_m30);
    result = KiExitDispatcher(local_rbp, Arg2, 1, (uint32_t)(Arg7));
loc_0024F212:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
loc_0024F236:
    *(uint32_t *)(v_stack_p8 + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C))));
    goto loc_0024F068;
loc_0024F252:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C)))), (uint8_t)(local_rbp), 1, (uint32_t)(Arg7));
    goto loc_0024EF63;
loc_0024F262:
    *(uint64_t *)(result) = (uint32_t)(0xC000009AULL);
    goto loc_0024F1DF;
loc_0024F26F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD77843)))) & (64)) == 0) goto loc_0024F18B;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C)))), (uint8_t)(local_rbp), 1, (uint32_t)(Arg7));
    if ((uint8_t)(result) == 0) goto loc_0024F18B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p30)), (uint8_t)(local_rbp), 1, (uint32_t)(Arg7));
    goto loc_0024F18D;
loc_0024F296:
    result = KeIsThreadRunning(v_stack_p8, (uint8_t)(local_rbp), 1, (uint32_t)(Arg7));
    result = EtwTraceEnqueueWork(v_stack_p8, result, (uint8_t)(result), (uint32_t)(Arg7));
    goto loc_0024EF85;
loc_0024F2B2:
    goto loc_0024F0A5;
loc_0024F2BB:
    if ((*(uint8_t *)(v_stack_p8 + 0x283)) != 15) goto loc_0024EFF1;
    goto loc_0024F1A1;
loc_0024F2CD:
    goto loc_0024EFC2;
loc_0024F2D5:
    if (((uint32_t)(result)) == 4) goto loc_0024F04B;
    if ((uint32_t)(result) != 0) goto loc_0024F301;
    Arg1 = (uint8_t)((v_stack_p8) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p8 + 0x70) = (uint8_t)(Arg1);
    *(uint64_t *)(v_stack_p8 + 0xC8) = result;
    *(uint64_t *)(v_stack_p8 + 0x3D0) = (uint32_t)(0xC000009AULL);
    *(uint8_t *)(1 + 0x11) = (uint8_t)(result);
    goto loc_0024F0D7;
loc_0024F301:
    if (((uint32_t)(result)) != 5) goto loc_0024F314;
    Arg1 = (uint8_t)((Arg1) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(v_stack_p8 + 0x70) = (uint8_t)(Arg1);
    goto loc_0024F0DA;
loc_0024F314:
    if (((uint32_t)(result)) != 3) goto loc_0024F0DA;
    *(uint8_t *)(1 + 0x11) = 2;
    goto loc_0024F0DA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024EEE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
