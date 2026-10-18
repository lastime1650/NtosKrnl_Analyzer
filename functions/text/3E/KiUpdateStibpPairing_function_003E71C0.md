# KiUpdateStibpPairing

- RVA: `0x003E71C0`–`0x003E76DA` (길이 `1,306` bytes)
- VA: `0x00000001403E71C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000956C8`
- 디코드: `281`개 명령, `1,306/1,306` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **30**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003E7273` → [KiFlushCurrentRsb](../6C/KiFlushCurrentRsb_function_006C6540.md) (function, `0x006C6540`)
- `0x003E733F` → [KiFlushCurrentRsb](../6C/KiFlushCurrentRsb_function_006C6540.md) (function, `0x006C6540`)

### Direct callers
- [sub_003E6B14](Unknown_function_003E6B14.md) at `0x003E6B17`
- [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) at `0x005C07CF`
- [NtContinueEx](../6B/NtContinueEx_function_006B10D0.md) at `0x006B1256`
- [NtRaiseException](../6B/NtRaiseException_function_006B1560.md) at `0x006B16F6`
- [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) at `0x006B1DB2`
- [KxStartUserThread](../6B/KxStartUserThread_function_006B2E50.md) at `0x006B2F91`
- [KiChainedDispatch](../6B/KiChainedDispatch_function_006B3480.md) at `0x006B3563`
- [KiInterruptDispatch](../6B/KiInterruptDispatch_function_006B3B30.md) at `0x006B3C13`
- [KiInterruptDispatchNoLock](../6B/KiInterruptDispatchNoLock_function_006B3F10.md) at `0x006B3FF3`
- [KiInterruptDispatchNoLockNoEtw](../6B/KiInterruptDispatchNoLockNoEtw_function_006B42F0.md) at `0x006B43D3`
- [KiInterruptDispatchNoEOI](../6B/KiInterruptDispatchNoEOI_function_006B46D0.md) at `0x006B47AB`
- [KiSpuriousDispatchNoEOI](../6B/KiSpuriousDispatchNoEOI_function_006B4AA0.md) at `0x006B4B70`
- [KxIsrLinkage](../6B/KxIsrLinkage_function_006B5680.md) at `0x006B5B1F`
- [KiApcInterrupt](../6B/KiApcInterrupt_function_006B5E20.md) at `0x006B624C`
- [KiHvInterruptDispatch](../6B/KiHvInterruptDispatch_function_006B7750.md) at `0x006B7841`
- [KiVmbusInterruptDispatch](../6B/KiVmbusInterruptDispatch_function_006B7B40.md) at `0x006B7C1D`
- [KiSwInterrupt](../6B/KiSwInterrupt_function_006B8070.md) at `0x006B84B8`
- [KiDpcInterrupt](../6B/KiDpcInterrupt_function_006B87C0.md) at `0x006B8BE0`
- [KiIpiInterrupt](../6B/KiIpiInterrupt_function_006B8F20.md) at `0x006B9361`
- [NtCallEnclave](../6B/NtCallEnclave_function_006BABA0.md) at `0x006BAC68`
- [KiBoundFault](../6B/KiBoundFault_function_006BE040.md) at `0x006BE43B`
- [KiInvalidOpcodeFault](../6B/KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEAF1`
- [KiPageFault](../6C/KiPageFault_function_006C0740.md) at `0x006C0C52`
- [KxMcheckAlternateReturn](../6C/KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C21E0`
- [KiVirtualizationException](../6C/KiVirtualizationException_function_006C2900.md) at `0x006C2D02`
- [KiControlProtectionFault](../6C/KiControlProtectionFault_function_006C3040.md) at `0x006C34A4`
- [KiSystemCall64](../6C/KiSystemCall64_function_006C4A40.md) at `0x006C503F`
- [KiSystemCall64](../6C/KiSystemCall64_function_006C4A40.md) at `0x006C5418`
- [KiExceptionDispatch](../6C/KiExceptionDispatch_function_006C5900.md) at `0x006C5B14`
- [KiFastFailDispatch](../6C/KiFastFailDispatch_function_006C5E40.md) at `0x006C5FD5`
- [sub_006F0CB7](../6F/Unknown_function_006F0CB7.md) at `0x006F0CCD`

### Static image references
- `0x003E7268` → RVA `0x00FC6B48` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E71C0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003E71C5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
003E71CA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003E71CF  57                              push rdi
003E71D0  41 54                           push r12
003E71D2  41 55                           push r13
003E71D4  41 56                           push r14
003E71D6  41 57                           push r15
003E71D8  48 83 EC 20                     sub rsp, 0x20
003E71DC  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
003E71E5  33 FF                           xor edi, edi
003E71E7  41 B8 01 00 00 00               mov r8d, 1
003E71ED  44 8B E7                        mov r12d, edi
003E71F0  41 8B E8                        mov ebp, r8d
003E71F3  48 85 C9                        test rcx, rcx
003E71F6  75 12                           jne 0x1403e720a
003E71F8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003E7201  8B EF                           mov ebp, edi
003E7203  48 8B 88 20 02 00 00            mov rcx, qword ptr [rax + 0x220]
003E720A  8B B1 FC 05 00 00               mov esi, dword ptr [rcx + 0x5fc]
003E7210  44 8B DF                        mov r11d, edi
003E7213  4C 8B B9 60 07 00 00            mov r15, qword ptr [rcx + 0x760]
003E721A  8B C6                           mov eax, esi
003E721C  4C 8B B3 B0 2D 00 00            mov r14, qword ptr [rbx + 0x2db0]
003E7223  44 8B EE                        mov r13d, esi
003E7226  25 00 00 40 00                  and eax, 0x400000
003E722B  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
003E722F  41 81 E5 00 00 80 00            and r13d, 0x800000
003E7236  81 E6 00 00 C0 00               and esi, 0xc00000
003E723C  85 ED                           test ebp, ebp
003E723E  0F 84 92 00 00 00               je 0x1403e72d6
003E7244  85 C0                           test eax, eax
003E7246  0F 84 0D 01 00 00               je 0x1403e7359
003E724C  48 8B 83 D0 06 00 00            mov rax, qword ptr [rbx + 0x6d0]
003E7253  48 85 C0                        test rax, rax
003E7256  0F 84 FD 00 00 00               je 0x1403e7359
003E725C  41 8B C0                        mov eax, r8d
003E725F  33 D2                           xor edx, edx
003E7261  B9 49 00 00 00                  mov ecx, 0x49
003E7266  0F 30                           wrmsr
003E7268  48 8B 05 D9 F8 BD 00            mov rax, qword ptr [rip + 0xbdf8d9]
003E726F  A8 08                           test al, 8
003E7271  75 23                           jne 0x1403e7296
003E7273  E8 C8 F2 2D 00                  call 0x1406c6540
003E7278  B9 DF FF 00 00                  mov ecx, 0xffdf
003E727D  41 B8 01 00 00 00               mov r8d, 1
003E7283  66 21 8B D8 06 00 00            and word ptr [rbx + 0x6d8], cx
003E728A  B9 BF FF 00 00                  mov ecx, 0xffbf
003E728F  66 21 8B DA 06 00 00            and word ptr [rbx + 0x6da], cx
003E7296  B8 FB FF 00 00                  mov eax, 0xfffb
003E729B  66 21 83 D8 06 00 00            and word ptr [rbx + 0x6d8], ax
003E72A2  66 F0 41 83 8E E0 06 00 00 20   lock or word ptr [r14 + 0x6e0], 0x20
003E72AC  4C 89 BB D0 06 00 00            mov qword ptr [rbx + 0x6d0], r15
003E72B3  B8 EF FF 00 00                  mov eax, 0xffef
003E72B8  80 8B DE 06 00 00 02            or byte ptr [rbx + 0x6de], 2
003E72BF  45 8B E0                        mov r12d, r8d
003E72C2  66 21 83 DA 06 00 00            and word ptr [rbx + 0x6da], ax
003E72C9  45 8B D8                        mov r11d, r8d
003E72CC  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
003E72D1  E9 83 00 00 00                  jmp 0x1403e7359
003E72D6  48 8B 83 D0 06 00 00            mov rax, qword ptr [rbx + 0x6d0]
003E72DD  4C 3B F8                        cmp r15, rax
003E72E0  74 2F                           je 0x1403e7311
003E72E2  66 F0 41 83 8E E0 06 00 00 20   lock or word ptr [r14 + 0x6e0], 0x20
003E72EC  4C 89 BB D0 06 00 00            mov qword ptr [rbx + 0x6d0], r15
003E72F3  45 8B E0                        mov r12d, r8d
003E72F6  66 83 8B D8 06 00 00 04         or word ptr [rbx + 0x6d8], 4
003E72FE  48 8B 05 43 F8 BD 00            mov rax, qword ptr [rip + 0xbdf843]
003E7305  A8 08                           test al, 8
003E7307  75 08                           jne 0x1403e7311
003E7309  66 83 8B D8 06 00 00 20         or word ptr [rbx + 0x6d8], 0x20
003E7311  0F B7 83 D8 06 00 00            movzx eax, word ptr [rbx + 0x6d8]
003E7318  A8 04                           test al, 4
003E731A  74 1F                           je 0x1403e733b
003E731C  41 8B C0                        mov eax, r8d
003E731F  33 D2                           xor edx, edx
003E7321  B9 49 00 00 00                  mov ecx, 0x49
003E7326  0F 30                           wrmsr
003E7328  B8 FB FF 00 00                  mov eax, 0xfffb
003E732D  66 21 83 D8 06 00 00            and word ptr [rbx + 0x6d8], ax
003E7334  0F B7 83 D8 06 00 00            movzx eax, word ptr [rbx + 0x6d8]
003E733B  A8 20                           test al, 0x20
003E733D  74 1A                           je 0x1403e7359
003E733F  E8 FC F1 2D 00                  call 0x1406c6540
003E7344  B9 DF FF 00 00                  mov ecx, 0xffdf
003E7349  44 8B DF                        mov r11d, edi
003E734C  66 21 8B D8 06 00 00            and word ptr [rbx + 0x6d8], cx
003E7353  41 B8 01 00 00 00               mov r8d, 1
003E7359  81 FE 00 00 40 00               cmp esi, 0x400000
003E735F  0F 85 0F 03 00 00               jne 0x1403e7674
003E7365  BA FD FE FF FF                  mov edx, 0xfffffefd
003E736A  0F 0D 8B E0 06 00 00            prefetchw byte ptr [rbx + 0x6e0]
003E7371  0F B7 83 E0 06 00 00            movzx eax, word ptr [rbx + 0x6e0]
003E7378  85 ED                           test ebp, ebp
003E737A  0F 85 30 02 00 00               jne 0x1403e75b0
003E7380  0F B7 C8                        movzx ecx, ax
003E7383  66 23 CA                        and cx, dx
003E7386  66 F0 0F B1 8B E0 06 00 00      lock cmpxchg word ptr [rbx + 0x6e0], cx
003E738F  75 EF                           jne 0x1403e7380
003E7391  44 0F B7 D0                     movzx r10d, ax
003E7395  49 8B 86 D0 06 00 00            mov rax, qword ptr [r14 + 0x6d0]
003E739C  44 8B CF                        mov r9d, edi
003E739F  48 85 C0                        test rax, rax
003E73A2  75 12                           jne 0x1403e73b6
003E73A4  41 F6 C2 10                     test r10b, 0x10
003E73A8  74 0C                           je 0x1403e73b6
003E73AA  49 8B C0                        mov rax, r8
003E73AD  66 F0 83 8B E0 06 00 00 02      lock or word ptr [rbx + 0x6e0], 2
003E73B6  4C 3B F8                        cmp r15, rax
003E73B9  0F 84 25 01 00 00               je 0x1403e74e4
003E73BF  41 F6 C2 08                     test r10b, 8
003E73C3  0F 85 1B 01 00 00               jne 0x1403e74e4
003E73C9  BE 01 00 00 00                  mov esi, 1
003E73CE  B9 FD FF 00 00                  mov ecx, 0xfffd
003E73D3  49 3B C7                        cmp rax, r15
003E73D6  0F 84 94 01 00 00               je 0x1403e7570
003E73DC  41 F6 C2 08                     test r10b, 8
003E73E0  0F 85 8A 01 00 00               jne 0x1403e7570
003E73E6  41 0F B7 86 E0 06 00 00         movzx eax, word ptr [r14 + 0x6e0]
003E73EE  41 0F B6 CA                     movzx ecx, r10b
003E73F2  0A C8                           or cl, al
003E73F4  F6 C1 01                        test cl, 1
003E73F7  0F 85 3F 02 00 00               jne 0x1403e763c
003E73FD  66 83 8B EC 06 00 00 02         or word ptr [rbx + 0x6ec], 2
003E7405  49 B8 00 00 00 00 00 02 00 00   movabs r8, 0x20000000000
003E740F  48 8B 05 32 F7 BD 00            mov rax, qword ptr [rip + 0xbdf732]
003E7416  49 85 C0                        test r8, rax
003E7419  74 14                           je 0x1403e742f
003E741B  66 83 8B E8 06 00 00 02         or word ptr [rbx + 0x6e8], 2
003E7423  EB 0A                           jmp 0x1403e742f
003E7425  66 21 8B E8 06 00 00            and word ptr [rbx + 0x6e8], cx
003E742C  44 8B CE                        mov r9d, esi
003E742F  B8 E0 06 00 00                  mov eax, 0x6e0
003E7434  49 8D 14 06                     lea rdx, [r14 + rax]
003E7438  45 85 E4                        test r12d, r12d
003E743B  0F 85 7F 02 00 00               jne 0x1403e76c0
003E7441  45 85 C9                        test r9d, r9d
003E7444  0F 84 7D 01 00 00               je 0x1403e75c7
003E744A  48 8B 05 F7 F6 BD 00            mov rax, qword ptr [rip + 0xbdf6f7]
003E7451  0F B7 93 E8 06 00 00            movzx edx, word ptr [rbx + 0x6e8]
003E7458  49 85 C0                        test r8, rax
003E745B  74 07                           je 0x1403e7464
003E745D  0F B7 93 E2 06 00 00            movzx edx, word ptr [rbx + 0x6e2]
003E7464  4D 85 FF                        test r15, r15
003E7467  0F 84 99 01 00 00               je 0x1403e7606
003E746D  F6 C2 03                        test dl, 3
003E7470  75 3A                           jne 0x1403e74ac
003E7472  B8 FD FF 00 00                  mov eax, 0xfffd
003E7477  66 23 D0                        and dx, ax
003E747A  66 83 CA 01                     or dx, 1
003E747E  66 89 93 E2 06 00 00            mov word ptr [rbx + 0x6e2], dx
003E7485  48 8B 0D BC F6 BD 00            mov rcx, qword ptr [rip + 0xbdf6bc]
003E748C  49 85 C8                        test r8, rcx
003E748F  0F 84 D3 01 00 00               je 0x1403e7668
003E7495  EB 15                           jmp 0x1403e74ac
003E7497  66 21 83 E8 06 00 00            and word ptr [rbx + 0x6e8], ax
003E749E  66 21 83 EC 06 00 00            and word ptr [rbx + 0x6ec], ax
003E74A5  48 8B 05 9C F6 BD 00            mov rax, qword ptr [rip + 0xbdf69c]
003E74AC  45 85 DB                        test r11d, r11d
003E74AF  74 13                           je 0x1403e74c4
003E74B1  B8 EF FF 00 00                  mov eax, 0xffef
003E74B6  66 89 93 E4 06 00 00            mov word ptr [rbx + 0x6e4], dx
003E74BD  66 21 83 DA 06 00 00            and word ptr [rbx + 0x6da], ax
003E74C4  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
003E74C9  8B C7                           mov eax, edi
003E74CB  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
003E74D0  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
003E74D5  48 83 C4 20                     add rsp, 0x20
003E74D9  41 5F                           pop r15
003E74DB  41 5E                           pop r14
003E74DD  41 5D                           pop r13
003E74DF  41 5C                           pop r12
003E74E1  5F                              pop rdi
003E74E2  C3                              ret
003E74E3  CC                              int3
003E74E4  45 0F B7 C2                     movzx r8d, r10w
003E74E8  BE 01 00 00 00                  mov esi, 1
003E74ED  66 41 83 E0 01                  and r8w, 1
003E74F2  41 0F B7 96 E0 06 00 00         movzx edx, word ptr [r14 + 0x6e0]
003E74FA  4D 85 FF                        test r15, r15
003E74FD  B9 11 00 00 00                  mov ecx, 0x11
003E7502  0F B7 C2                        movzx eax, dx
003E7505  66 0F 44 CE                     cmove cx, si
003E7509  66 83 E0 EF                     and ax, 0xffef
003E750D  66 0B C8                        or cx, ax
003E7510  66 45 85 C0                     test r8w, r8w
003E7514  75 04                           jne 0x1403e751a
003E7516  66 83 C9 02                     or cx, 2
003E751A  66 0F BA E1 08                  bt cx, 8
003E751F  72 14                           jb 0x1403e7535
003E7521  66 3B CA                        cmp cx, dx
003E7524  74 0F                           je 0x1403e7535
003E7526  0F B7 C2                        movzx eax, dx
003E7529  66 F0 41 0F B1 8E E0 06 00 00   lock cmpxchg word ptr [r14 + 0x6e0], cx
003E7533  75 BD                           jne 0x1403e74f2
003E7535  66 0F BA E2 08                  bt dx, 8
003E753A  44 8B 5C 24 50                  mov r11d, dword ptr [rsp + 0x50]
003E753F  0F 82 47 01 00 00               jb 0x1403e768c
003E7545  49 8B 86 D0 06 00 00            mov rax, qword ptr [r14 + 0x6d0]
003E754C  48 85 C0                        test rax, rax
003E754F  0F 85 79 FE FF FF               jne 0x1403e73ce
003E7555  41 F6 C2 10                     test r10b, 0x10
003E7559  0F 84 6F FE FF FF               je 0x1403e73ce
003E755F  48 8B C6                        mov rax, rsi
003E7562  66 F0 83 8B E0 06 00 00 02      lock or word ptr [rbx + 0x6e0], 2
003E756B  E9 5E FE FF FF                  jmp 0x1403e73ce
003E7570  45 85 ED                        test r13d, r13d
003E7573  0F 85 6D FE FF FF               jne 0x1403e73e6
003E7579  48 83 F8 01                     cmp rax, 1
003E757D  0F 84 63 FE FF FF               je 0x1403e73e6
003E7583  66 21 8B EC 06 00 00            and word ptr [rbx + 0x6ec], cx
003E758A  49 B8 00 00 00 00 00 02 00 00   movabs r8, 0x20000000000
003E7594  48 8B 05 AD F5 BD 00            mov rax, qword ptr [rip + 0xbdf5ad]
003E759B  49 85 C0                        test r8, rax
003E759E  0F 85 81 FE FF FF               jne 0x1403e7425
003E75A4  E9 83 FE FF FF                  jmp 0x1403e742c
003E75A9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
003E75B0  0F B7 C8                        movzx ecx, ax
003E75B3  66 23 CA                        and cx, dx
003E75B6  66 F0 0F B1 8B E0 06 00 00      lock cmpxchg word ptr [rbx + 0x6e0], cx
003E75BF  0F 84 CC FD FF FF               je 0x1403e7391
003E75C5  EB E9                           jmp 0x1403e75b0
003E75C7  45 85 ED                        test r13d, r13d
003E75CA  0F 84 7A FE FF FF               je 0x1403e744a
003E75D0  0F 0D 8B E0 06 00 00            prefetchw byte ptr [rbx + 0x6e0]
003E75D7  0F B7 83 E0 06 00 00            movzx eax, word ptr [rbx + 0x6e0]
003E75DE  BA 00 01 00 00                  mov edx, 0x100
003E75E3  0F B7 C8                        movzx ecx, ax
003E75E6  66 0B CA                        or cx, dx
003E75E9  66 F0 0F B1 8B E0 06 00 00      lock cmpxchg word ptr [rbx + 0x6e0], cx
003E75F2  75 EF                           jne 0x1403e75e3
003E75F4  A8 01                           test al, 1
003E75F6  0F 84 4E FE FF FF               je 0x1403e744a
003E75FC  85 ED                           test ebp, ebp
003E75FE  0F 45 FE                        cmovne edi, esi
003E7601  E9 44 FE FF FF                  jmp 0x1403e744a
003E7606  41 F6 C2 10                     test r10b, 0x10
003E760A  75 50                           jne 0x1403e765c
003E760C  B8 FC FF 00 00                  mov eax, 0xfffc
003E7611  66 23 D0                        and dx, ax
003E7614  66 89 93 E2 06 00 00            mov word ptr [rbx + 0x6e2], dx
003E761B  48 8B 05 26 F5 BD 00            mov rax, qword ptr [rip + 0xbdf526]
003E7622  49 85 C0                        test r8, rax
003E7625  B8 FD FF 00 00                  mov eax, 0xfffd
003E762A  0F 85 67 FE FF FF               jne 0x1403e7497
003E7630  66 89 93 E8 06 00 00            mov word ptr [rbx + 0x6e8], dx
003E7637  E9 62 FE FF FF                  jmp 0x1403e749e
003E763C  0F B7 C8                        movzx ecx, ax
003E763F  66 83 E1 EE                     and cx, 0xffee
003E7643  66 83 C9 02                     or cx, 2
003E7647  66 F0 41 0F B1 8E E0 06 00 00   lock cmpxchg word ptr [r14 + 0x6e0], cx
003E7651  0F 84 A6 FD FF FF               je 0x1403e73fd
003E7657  E9 8A FD FF FF                  jmp 0x1403e73e6
003E765C  B8 FE FF 00 00                  mov eax, 0xfffe
003E7661  66 23 D0                        and dx, ax
003E7664  66 83 CA 02                     or dx, 2
003E7668  66 89 93 E8 06 00 00            mov word ptr [rbx + 0x6e8], dx
003E766F  E9 38 FE FF FF                  jmp 0x1403e74ac
003E7674  45 85 ED                        test r13d, r13d
003E7677  74 1B                           je 0x1403e7694
003E7679  44 0F B7 93 E0 06 00 00         movzx r10d, word ptr [rbx + 0x6e0]
003E7681  41 BF 02 00 00 00               mov r15d, 2
003E7687  E9 09 FD FF FF                  jmp 0x1403e7395
003E768C  48 8B C6                        mov rax, rsi
003E768F  E9 3A FD FF FF                  jmp 0x1403e73ce
003E7694  B9 FF FE FF FF                  mov ecx, 0xfffffeff
003E7699  0F B7 83 E0 06 00 00            movzx eax, word ptr [rbx + 0x6e0]
003E76A0  44 0F B7 D0                     movzx r10d, ax
003E76A4  66 44 23 D1                     and r10w, cx
003E76A8  66 41 83 CA 02                  or r10w, 2
003E76AD  66 F0 44 0F B1 93 E0 06 00 00   lock cmpxchg word ptr [rbx + 0x6e0], r10w
003E76B7  74 C8                           je 0x1403e7681
003E76B9  EB DE                           jmp 0x1403e7699
003E76BB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003E76C0  0F B7 02                        movzx eax, word ptr [rdx]
003E76C3  0F B7 C8                        movzx ecx, ax
003E76C6  66 83 E1 DF                     and cx, 0xffdf
003E76CA  66 83 C9 02                     or cx, 2
003E76CE  66 F0 0F B1 0A                  lock cmpxchg word ptr [rdx], cx
003E76D3  75 EB                           jne 0x1403e76c0
003E76D5  E9 67 FD FF FF                  jmp 0x1403e7441
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiUpdateStibpPairing(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p50;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    v_rbp = 1;
    if (a1 == 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        v_rbp = 0;
        a1 = *(unsigned __int64 *)(result + 544);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1532))))) & (0x400000ULL));
    v_stack_p8 = 0;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1532))))) & (0x800000ULL));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1532))) & (0xC00000ULL));
    if ((unsigned int)(v_rbp) == 0) goto loc_003E72D6;
    if ((unsigned int)(result) == 0) goto loc_003E7359;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1744) == 0) goto loc_003E7359;
    a2 = 0;
    result = *(unsigned __int64 *)(v_rip + 12450009);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 12450009))) & (8)) == 0) {
        result = KiFlushCurrentRsb(73, a2, 1, a4);
        a1 = 0xFFDFULL;
        a3 = 1;
        a1 = 0xFFBFULL;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1744) = *(unsigned __int64 *)(a1 + 1888);
    v_stack_p8 = (unsigned int)(a3);
    goto loc_003E7359;
loc_003E72D6:
    if ((*(unsigned __int64 *)(a1 + 1888)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1744))) goto loc_003E7311;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1744) = *(unsigned __int64 *)(a1 + 1888);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 12449859))) & (8)) == 0) {
    }
    result = *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1752);
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1752))) & (4)) != 0) {
        result = (unsigned int)(a3);
        a2 = 0;
        a1 = 73;
        result = 0xFFFBULL;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1752);
    }
    v_r11 = (unsigned int)((unsigned int)(a3));
    if ((((unsigned __int8)(result)) & (32)) != 0) {
        result = KiFlushCurrentRsb(a1, a2, a3, a4);
        a1 = 0xFFDFULL;
        v_r11 = 0;
        a3 = 1;
    }
    if (((unsigned int)(v_rsi)) != 0x400000ULL) goto loc_003E7674;
    if ((unsigned int)(v_rbp) != 0) goto loc_003E75B0;
loc_003E7380:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760))) & ((unsigned __int16)((unsigned int)(0xFFFFFEFDULL))));
    if (condition_is_not_equal) goto loc_003E7380;
loc_003E7391:
loc_003E7395:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1744) != 0) goto loc_003E73B6;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1744);
    if ((((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) & (16)) != 0) {
        result = a3;
    }
    if ((*(unsigned __int64 *)(a1 + 1888)) == result) goto loc_003E74E4;
    if ((((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) & (8)) != 0) goto loc_003E74E4;
loc_003E73CE:
    if (result == (*(unsigned __int64 *)(a1 + 1888))) goto loc_003E7570;
    if ((((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) & (8)) != 0) goto loc_003E7570;
loc_003E73E6:
    a1 = (unsigned __int8)(((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) | ((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1760))));
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_003E763C;
loc_003E73FD:
    if (((a3) & (*(unsigned __int64 *)(v_rip + 12449586))) == 0) goto loc_003E742F;
    goto loc_003E742F;
loc_003E7425:
loc_003E742C:
loc_003E742F:
    if ((unsigned int)((unsigned int)((unsigned int)(a3))) != 0) goto loc_003E76C0;
loc_003E7441:
    if (1 == 0) goto loc_003E75C7;
loc_003E744A:
    if (((a3) & (*(unsigned __int64 *)(v_rip + 12449527))) != 0) {
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1762);
    }
    if (*(unsigned __int64 *)(a1 + 1888) == 0) goto loc_003E7606;
    if ((((unsigned __int8)(a2)) & (3)) != 0) goto loc_003E74AC;
    a2 = (unsigned __int16)((a2) & ((unsigned __int16)((unsigned int)(0xFFFDULL))));
    a2 = (unsigned __int16)((a2) | (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1762) = (unsigned __int16)(a2);
    if (((a3) & (*(unsigned __int64 *)(v_rip + 12449468))) == 0) goto loc_003E7668;
    goto loc_003E74AC;
loc_003E7497:
loc_003E749E:
loc_003E74AC:
    result = *(unsigned __int64 *)(v_rip + 12449436);
    if ((unsigned int)(v_r11) != 0) {
        result = 0xFFEFULL;
        *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1764) = (unsigned __int16)(a2);
    }
    v_rsp = (v_rsp) + (32);
    return 0;
loc_003E74E4:
    a3 = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) & (1));
loc_003E74F2:
    a1 = 17;
    if (*(unsigned __int64 *)(a1 + 1888) == 0) { a1 = 1; }
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1760))) & (0xFFEFULL));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(result)));
    if ((unsigned __int16)(a3) == 0) {
        a1 = (unsigned __int16)((a1) | (2));
    }
    if (condition_is_below) goto loc_003E7535;
    if (((unsigned __int16)(a1)) == ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1760)))) goto loc_003E7535;
    if (((unsigned __int16)(a1)) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1760)))) goto loc_003E74F2;
loc_003E7535:
    if (((unsigned __int16)(a1)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1760)))) goto loc_003E768C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1744) != 0) goto loc_003E73CE;
    if ((((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) & (16)) == 0) goto loc_003E73CE;
    goto loc_003E73CE;
loc_003E7570:
    if ((unsigned int)(v_r13) != 0) goto loc_003E73E6;
    if (1 == 1) goto loc_003E73E6;
    if (((a3) & (*(unsigned __int64 *)(v_rip + 12449197))) != 0) goto loc_003E7425;
    goto loc_003E742C;
loc_003E75B0:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int64 *)(v_rip + 12449197))) & ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11696) + 1760))));
    if (condition_is_equal) goto loc_003E7391;
    goto loc_003E75B0;
loc_003E75C7:
    if ((unsigned int)(v_r13) == 0) goto loc_003E744A;
loc_003E75E3:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_p10 + 1760))) | (256));
    if (condition_is_not_equal) goto loc_003E75E3;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_p10 + 1760))) & (1)) == 0) goto loc_003E744A;
    if ((unsigned int)(v_stack_p18) != 0) { v_rdi = 1; }
    goto loc_003E744A;
loc_003E7606:
    if ((((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1760)))) & (16)) != 0) goto loc_003E765C;
    a2 = (unsigned __int16)((256) & ((unsigned __int16)((unsigned int)(0xFFFCULL))));
    *(unsigned __int16 *)(v_stack_p10 + 1762) = (unsigned __int16)(a2);
    if (((a3) & (*(unsigned __int64 *)(v_rip + 12449062))) != 0) goto loc_003E7497;
    *(unsigned __int16 *)(v_stack_p10 + 1768) = (unsigned __int16)(a2);
    goto loc_003E749E;
loc_003E763C:
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)(0xFFFDULL))) & (0xFFEEULL));
    a1 = (unsigned __int16)((a1) | (2));
    if (condition_is_equal) goto loc_003E73FD;
    goto loc_003E73E6;
loc_003E765C:
    a2 = (unsigned __int16)((a2) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    a2 = (unsigned __int16)((a2) | (2));
loc_003E7668:
    *(unsigned __int16 *)(v_stack_p10 + 1768) = (unsigned __int16)(a2);
    goto loc_003E74AC;
loc_003E7674:
    if ((unsigned int)(v_r13) == 0) goto loc_003E7694;
loc_003E7681:
    goto loc_003E7395;
loc_003E768C:
    goto loc_003E73CE;
loc_003E7694:
loc_003E7699:
    v_r10 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_p10 + 1760))) & ((unsigned __int16)((unsigned int)(0xFFFFFEFFULL))));
    v_r10 = (unsigned __int16)((v_r10) | (2));
    if (condition_is_equal) goto loc_003E7681;
    goto loc_003E7699;
loc_003E76C0:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) & (0xFFDFULL));
    a1 = (unsigned __int16)((a1) | (2));
    if (condition_is_not_equal) goto loc_003E76C0;
    goto loc_003E7441;
}
```

## 5. (Beta) C Style

```c
int64_t KiUpdateStibpPairing(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p50;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    local_rbp = 1;
    if (Arg1 == 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        local_rbp = 0;
        Arg1 = *(uint64_t *)(result + 0x220);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x5FC))))) & (0x400000ULL));
    v_stack_p8 = 0;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x5FC))))) & (0x800000ULL));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x5FC))) & (0xC00000ULL));
    if ((uint32_t)(local_rbp) == 0) goto loc_003E72D6;
    if ((uint32_t)(result) == 0) goto loc_003E7359;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D0) == 0) goto loc_003E7359;
    Arg2 = 0;
    result = *(uint64_t *)(v_rip + 0xBDF8D9);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xBDF8D9))) & (8)) == 0) {
        result = KiFlushCurrentRsb(73, Arg2, 1, a4);
        Arg1 = 0xFFDFULL;
        a3 = 1;
        Arg1 = 0xFFBFULL;
    }
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D0) = *(uint64_t *)(Arg1 + 0x760);
    v_stack_p8 = (uint32_t)(a3);
    goto loc_003E7359;
loc_003E72D6:
    if ((*(uint64_t *)(Arg1 + 0x760)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D0))) goto loc_003E7311;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D0) = *(uint64_t *)(Arg1 + 0x760);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xBDF843))) & (8)) == 0) {
    }
    result = *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D8);
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D8))) & (4)) != 0) {
        result = (uint32_t)(a3);
        Arg2 = 0;
        Arg1 = 73;
        result = 0xFFFBULL;
        result = *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6D8);
    }
    local_r11 = (uint32_t)((uint32_t)(a3));
    if ((((uint8_t)(result)) & (32)) != 0) {
        result = KiFlushCurrentRsb(Arg1, Arg2, a3, a4);
        Arg1 = 0xFFDFULL;
        local_r11 = 0;
        a3 = 1;
    }
    if (((uint32_t)(local_rsi)) != 0x400000ULL) goto loc_003E7674;
    if ((uint32_t)(local_rbp) != 0) goto loc_003E75B0;
loc_003E7380:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0))) & ((uint16_t)((uint32_t)(0xFFFFFEFDULL))));
    if (condition_is_not_equal) goto loc_003E7380;
loc_003E7391:
loc_003E7395:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6D0) != 0) goto loc_003E73B6;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6D0);
    if ((((uint8_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) & (16)) != 0) {
        result = a3;
    }
    if ((*(uint64_t *)(Arg1 + 0x760)) == result) goto loc_003E74E4;
    if ((((uint8_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) & (8)) != 0) goto loc_003E74E4;
loc_003E73CE:
    if (result == (*(uint64_t *)(Arg1 + 0x760))) goto loc_003E7570;
    if ((((uint8_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) & (8)) != 0) goto loc_003E7570;
loc_003E73E6:
    Arg1 = (uint8_t)(((uint8_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) | ((uint8_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6E0))));
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_003E763C;
loc_003E73FD:
    if (((a3) & (*(uint64_t *)(v_rip + 0xBDF732))) == 0) goto loc_003E742F;
    goto loc_003E742F;
loc_003E7425:
loc_003E742C:
loc_003E742F:
    if ((uint32_t)((uint32_t)((uint32_t)(a3))) != 0) goto loc_003E76C0;
loc_003E7441:
    if (1 == 0) goto loc_003E75C7;
loc_003E744A:
    if (((a3) & (*(uint64_t *)(v_rip + 0xBDF6F7))) != 0) {
        Arg2 = *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E2);
    }
    if (*(uint64_t *)(Arg1 + 0x760) == 0) goto loc_003E7606;
    if ((((uint8_t)(Arg2)) & (3)) != 0) goto loc_003E74AC;
    Arg2 = (uint16_t)((Arg2) & ((uint16_t)((uint32_t)(0xFFFDULL))));
    Arg2 = (uint16_t)((Arg2) | (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E2) = (uint16_t)(Arg2);
    if (((a3) & (*(uint64_t *)(v_rip + 0xBDF6BC))) == 0) goto loc_003E7668;
    goto loc_003E74AC;
loc_003E7497:
loc_003E749E:
loc_003E74AC:
    result = *(uint64_t *)(v_rip + 0xBDF69C);
    if ((uint32_t)(local_r11) != 0) {
        result = 0xFFEFULL;
        *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E4) = (uint16_t)(Arg2);
    }
    local_rsp = (local_rsp) + (32);
    return 0;
loc_003E74E4:
    a3 = (uint16_t)(((uint16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) & (1));
loc_003E74F2:
    Arg1 = 17;
    if (*(uint64_t *)(Arg1 + 0x760) == 0) { Arg1 = 1; }
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6E0))) & (0xFFEFULL));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(result)));
    if ((uint16_t)(a3) == 0) {
        Arg1 = (uint16_t)((Arg1) | (2));
    }
    if (condition_is_below) goto loc_003E7535;
    if (((uint16_t)(Arg1)) == ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6E0)))) goto loc_003E7535;
    if (((uint16_t)(Arg1)) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6E0)))) goto loc_003E74F2;
loc_003E7535:
    if (((uint16_t)(Arg1)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6E0)))) goto loc_003E768C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6D0) != 0) goto loc_003E73CE;
    if ((((uint8_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) & (16)) == 0) goto loc_003E73CE;
    goto loc_003E73CE;
loc_003E7570:
    if ((uint32_t)(local_r13) != 0) goto loc_003E73E6;
    if (1 == 1) goto loc_003E73E6;
    if (((a3) & (*(uint64_t *)(v_rip + 0xBDF5AD))) != 0) goto loc_003E7425;
    goto loc_003E742C;
loc_003E75B0:
    Arg1 = (uint16_t)(((uint16_t)(*(uint64_t *)(v_rip + 0xBDF5AD))) & ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2DB0) + 0x6E0))));
    if (condition_is_equal) goto loc_003E7391;
    goto loc_003E75B0;
loc_003E75C7:
    if ((uint32_t)(local_r13) == 0) goto loc_003E744A;
loc_003E75E3:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_p10 + 0x6E0))) | (256));
    if (condition_is_not_equal) goto loc_003E75E3;
    if ((((uint8_t)(*(uint16_t *)(v_stack_p10 + 0x6E0))) & (1)) == 0) goto loc_003E744A;
    if ((uint32_t)(v_stack_p18) != 0) { local_rdi = 1; }
    goto loc_003E744A;
loc_003E7606:
    if ((((uint8_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E0)))) & (16)) != 0) goto loc_003E765C;
    Arg2 = (uint16_t)((256) & ((uint16_t)((uint32_t)(0xFFFCULL))));
    *(uint16_t *)(v_stack_p10 + 0x6E2) = (uint16_t)(Arg2);
    if (((a3) & (*(uint64_t *)(v_rip + 0xBDF526))) != 0) goto loc_003E7497;
    *(uint16_t *)(v_stack_p10 + 0x6E8) = (uint16_t)(Arg2);
    goto loc_003E749E;
loc_003E763C:
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)(0xFFFDULL))) & (0xFFEEULL));
    Arg1 = (uint16_t)((Arg1) | (2));
    if (condition_is_equal) goto loc_003E73FD;
    goto loc_003E73E6;
loc_003E765C:
    Arg2 = (uint16_t)((Arg2) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    Arg2 = (uint16_t)((Arg2) | (2));
loc_003E7668:
    *(uint16_t *)(v_stack_p10 + 0x6E8) = (uint16_t)(Arg2);
    goto loc_003E74AC;
loc_003E7674:
    if ((uint32_t)(local_r13) == 0) goto loc_003E7694;
loc_003E7681:
    goto loc_003E7395;
loc_003E768C:
    goto loc_003E73CE;
loc_003E7694:
loc_003E7699:
    local_r10 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_p10 + 0x6E0))) & ((uint16_t)((uint32_t)(0xFFFFFEFFULL))));
    local_r10 = (uint16_t)((local_r10) | (2));
    if (condition_is_equal) goto loc_003E7681;
    goto loc_003E7699;
loc_003E76C0:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2))) & (0xFFDFULL));
    Arg1 = (uint16_t)((Arg1) | (2));
    if (condition_is_not_equal) goto loc_003E76C0;
    goto loc_003E7441;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E71C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
