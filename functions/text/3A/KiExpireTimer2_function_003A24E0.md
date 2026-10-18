# KiExpireTimer2

- RVA: `0x003A24E0`–`0x003A2C8D` (길이 `1,965` bytes)
- VA: `0x00000001403A24E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008209C`
- 디코드: `496`개 명령, `1,965/1,965` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x003A25F8` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x003A26AC` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)
- `0x003A271F` → [ExpHpGCTimerCallback](ExpHpGCTimerCallback_function_003A3040.md) (function, `0x003A3040`)
- `0x003A2761` → [KiFinalizeTimer2Disablement](KiFinalizeTimer2Disablement_function_003A2198.md) (function, `0x003A2198`)
- `0x003A278E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003A27A7` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x003A27F2` → [KiUpdateTimer2Collections](KiUpdateTimer2Collections_function_003A2408.md) (function, `0x003A2408`)
- `0x003A2821` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x003A2833` → [KiInsertTimer2WithCollectionLockHeld](KiInsertTimer2WithCollectionLockHeld_function_003A2CA0.md) (function, `0x003A2CA0`)
- `0x003A2842` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x003A2888` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x003A28C6` → [PsTimerResolutionActive](PsTimerResolutionActive_function_003A3010.md) (function, `0x003A3010`)
- `0x003A295A` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x003A29C4` → [EtwGetKernelTraceTimestamp](../39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x003A29F5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003A2A07` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003A2A2B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003A2AF8` → [EtwGetKernelTraceTimestamp](../39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x003A2B22` → [EtwTraceTimedEvent](EtwTraceTimedEvent_function_003A3430.md) (function, `0x003A3430`)
- `0x003A2B78` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x003A2BC3` → [KiFinalizeTimer2Disablement](KiFinalizeTimer2Disablement_function_003A2198.md) (function, `0x003A2198`)
- `0x003A2BE2` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x003A2C1E` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x003A2C3C` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x003A2C58` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x003A2C83` → [KiHvEnlightenedGuestPriorityKick](../44/KiHvEnlightenedGuestPriorityKick_function_00443880.md) (function, `0x00443880`)

### Direct callers
- [sub_003A18D4](Unknown_function_003A18D4.md) at `0x003A1957`

### Static image references
- `0x003A24FC` → RVA `0x00E0A740` (`.data`; read)
- `0x003A251C` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x003A2607` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x003A2617` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x003A2707` → RVA `0x003A3040` (`ExpHpGCTimerCallback`; read)
- `0x003A27D4` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x003A2816` → RVA `0x00FCF600` (`CACHEALI`; read)
- `0x003A2C62` → RVA `0x00F21FB0` (`.data`; read)
- `0x003A2C68` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x003A2C7C` → RVA `0x00FC504C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A24E0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003A24E5  55                              push rbp
003A24E6  56                              push rsi
003A24E7  57                              push rdi
003A24E8  41 54                           push r12
003A24EA  41 55                           push r13
003A24EC  41 56                           push r14
003A24EE  41 57                           push r15
003A24F0  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
003A24F5  48 81 EC B0 00 00 00            sub rsp, 0xb0
003A24FC  48 8B 05 3D 82 A6 00            mov rax, qword ptr [rip + 0xa6823d]
003A2503  48 33 C4                        xor rax, rsp
003A2506  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
003A250A  48 8B 72 08                     mov rsi, qword ptr [rdx + 8]
003A250E  48 8D B9 81 00 00 00            lea rdi, [rcx + 0x81]
003A2515  45 33 E4                        xor r12d, r12d
003A2518  4C 89 4D B7                     mov qword ptr [rbp - 0x49], r9
003A251C  F7 05 E2 45 C2 00 00 00 02 00   test dword ptr [rip + 0xc245e2], 0x20000
003A2526  0F 57 C0                        xorps xmm0, xmm0
003A2529  4D 8B D0                        mov r10, r8
003A252C  4C 89 65 C7                     mov qword ptr [rbp - 0x39], r12
003A2530  4C 8B EA                        mov r13, rdx
003A2533  4C 89 65 CF                     mov qword ptr [rbp - 0x31], r12
003A2537  48 8B D9                        mov rbx, rcx
003A253A  4C 89 65 DF                     mov qword ptr [rbp - 0x21], r12
003A253E  4C 89 65 E7                     mov qword ptr [rbp - 0x19], r12
003A2542  45 8B FC                        mov r15d, r12d
003A2545  4C 89 65 EF                     mov qword ptr [rbp - 0x11], r12
003A2549  4C 89 65 F7                     mov qword ptr [rbp - 9], r12
003A254D  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
003A2551  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
003A2555  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
003A2559  44 88 65 AA                     mov byte ptr [rbp - 0x56], r12b
003A255D  44 88 65 A9                     mov byte ptr [rbp - 0x57], r12b
003A2561  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
003A2565  0F 84 DC 05 00 00               je 0x1403a2b47
003A256B  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
003A256F  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
003A2573  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
003A2577  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
003A257B  48 8B 41 58                     mov rax, qword ptr [rcx + 0x58]
003A257F  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
003A2583  0F B6 07                        movzx eax, byte ptr [rdi]
003A2586  88 45 A9                        mov byte ptr [rbp - 0x57], al
003A2589  C6 45 A7 01                     mov byte ptr [rbp - 0x59], 1
003A258D  4C 39 61 58                     cmp qword ptr [rcx + 0x58], r12
003A2591  0F 85 FD 01 00 00               jne 0x1403a2794
003A2597  0F B6 03                        movzx eax, byte ptr [rbx]
003A259A  4C 8D 73 08                     lea r14, [rbx + 8]
003A259E  49 8B 3E                        mov rdi, qword ptr [r14]
003A25A1  24 7F                           and al, 0x7f
003A25A3  C7 43 04 01 00 00 00            mov dword ptr [rbx + 4], 1
003A25AA  3C 19                           cmp al, 0x19
003A25AC  0F 85 7E 03 00 00               jne 0x1403a2930
003A25B2  49 3B FE                        cmp rdi, r14
003A25B5  74 50                           je 0x1403a2607
003A25B7  48 8B 0F                        mov rcx, qword ptr [rdi]
003A25BA  48 8B C7                        mov rax, rdi
003A25BD  48 8B F9                        mov rdi, rcx
003A25C0  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003A25C4  48 39 41 08                     cmp qword ptr [rcx + 8], rax
003A25C8  75 05                           jne 0x1403a25cf
003A25CA  48 39 02                        cmp qword ptr [rdx], rax
003A25CD  74 07                           je 0x1403a25d6
003A25CF  B9 03 00 00 00                  mov ecx, 3
003A25D4  CD 29                           int 0x29
003A25D6  48 89 0A                        mov qword ptr [rdx], rcx
003A25D9  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003A25DD  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
003A25E1  80 F9 01                        cmp cl, 1
003A25E4  0F 85 8A 02 00 00               jne 0x1403a2874
003A25EA  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
003A25EF  45 33 C9                        xor r9d, r9d
003A25F2  48 8B D0                        mov rdx, rax
003A25F5  49 8B CD                        mov rcx, r13
003A25F8  E8 D3 E0 FA FF                  call 0x1403506d0
003A25FD  84 C0                           test al, al
003A25FF  74 B1                           je 0x1403a25b2
003A2601  83 6B 04 01                     sub dword ptr [rbx + 4], 1
003A2605  75 AB                           jne 0x1403a25b2
003A2607  48 8B 05 6A 49 C2 00            mov rax, qword ptr [rip + 0xc2496a]
003A260E  4D 8B CC                        mov r9, r12
003A2611  48 8B 7B 60                     mov rdi, qword ptr [rbx + 0x60]
003A2615  8B C8                           mov ecx, eax
003A2617  48 8B 15 32 4C C2 00            mov rdx, qword ptr [rip + 0xc24c32]
003A261E  48 33 F8                        xor rdi, rax
003A2621  44 8B B6 E4 01 00 00            mov r14d, dword ptr [rsi + 0x1e4]
003A2628  48 D3 C7                        rol rdi, cl
003A262B  48 33 FB                        xor rdi, rbx
003A262E  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
003A2632  44 0F B6 A6 32 02 00 00         movzx r12d, byte ptr [rsi + 0x232]
003A263A  48 0F CF                        bswap rdi
003A263D  48 33 FA                        xor rdi, rdx
003A2640  0F 84 3C 05 00 00               je 0x1403a2b82
003A2646  4C 8B 43 68                     mov r8, qword ptr [rbx + 0x68]
003A264A  41 83 CF 10                     or r15d, 0x10
003A264E  4C 33 C0                        xor r8, rax
003A2651  41 C1 E7 08                     shl r15d, 8
003A2655  49 D3 C0                        rol r8, cl
003A2658  4C 33 C3                        xor r8, rbx
003A265B  49 0F C8                        bswap r8
003A265E  4C 33 C2                        xor r8, rdx
003A2661  8B 13                           mov edx, dword ptr [rbx]
003A2663  8B CA                           mov ecx, edx
003A2665  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
003A2669  81 E1 7F F0 FF FF               and ecx, 0xfffff07f
003A266F  8B C2                           mov eax, edx
003A2671  41 0B CF                        or ecx, r15d
003A2674  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
003A2678  3B D0                           cmp edx, eax
003A267A  74 17                           je 0x1403a2693
003A267C  8B C8                           mov ecx, eax
003A267E  44 8B C0                        mov r8d, eax
003A2681  81 E1 7F F0 FF FF               and ecx, 0xfffff07f
003A2687  41 0B CF                        or ecx, r15d
003A268A  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
003A268E  44 3B C0                        cmp r8d, eax
003A2691  75 E9                           jne 0x1403a267c
003A2693  4D 39 8D 08 2D 00 00            cmp qword ptr [r13 + 0x2d08], r9
003A269A  74 15                           je 0x1403a26b1
003A269C  41 B9 02 00 00 00               mov r9d, 2
003A26A2  45 33 C0                        xor r8d, r8d
003A26A5  49 8B CD                        mov rcx, r13
003A26A8  41 8D 51 FF                     lea edx, [r9 - 1]
003A26AC  E8 0F 06 EB FF                  call 0x140252cc0
003A26B1  44 0F B6 7D A7                  movzx r15d, byte ptr [rbp - 0x59]
003A26B6  45 84 FF                        test r15b, r15b
003A26B9  0F 85 FC 02 00 00               jne 0x1403a29bb
003A26BF  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
003A26C3  8B 02                           mov eax, dword ptr [rdx]
003A26C5  8B C8                           mov ecx, eax
003A26C7  83 E1 0F                        and ecx, 0xf
003A26CA  FF C0                           inc eax
003A26CC  89 02                           mov dword ptr [rdx], eax
003A26CE  8B C1                           mov eax, ecx
003A26D0  48 FF C1                        inc rcx
003A26D3  48 8D 0C 48                     lea rcx, [rax + rcx*2]
003A26D7  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003A26E1  48 8D 0C CA                     lea rcx, [rdx + rcx*8]
003A26E5  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
003A26E9  48 89 39                        mov qword ptr [rcx], rdi
003A26EC  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
003A26F0  48 8B 00                        mov rax, qword ptr [rax]
003A26F3  48 89 41 08                     mov qword ptr [rcx + 8], rax
003A26F7  33 C0                           xor eax, eax
003A26F9  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
003A26FD  48 8B CB                        mov rcx, rbx
003A2700  41 89 85 5C 86 00 00            mov dword ptr [r13 + 0x865c], eax
003A2707  48 8D 05 32 09 00 00            lea rax, [rip + 0x932]
003A270E  41 C6 85 BA 38 00 00 01         mov byte ptr [r13 + 0x38ba], 1
003A2716  48 3B F8                        cmp rdi, rax
003A2719  0F 85 09 03 00 00               jne 0x1403a2a28
003A271F  E8 1C 09 00 00                  call 0x1403a3040
003A2724  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
003A2728  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003A2732  41 C6 85 BA 38 00 00 00         mov byte ptr [r13 + 0x38ba], 0
003A273A  48 8B 00                        mov rax, qword ptr [rax]
003A273D  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
003A2741  0F 0D 0B                        prefetchw byte ptr [rbx]
003A2744  8B 03                           mov eax, dword ptr [rbx]
003A2746  8B C8                           mov ecx, eax
003A2748  0F BA F1 0C                     btr ecx, 0xc
003A274C  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
003A2750  75 F4                           jne 0x1403a2746
003A2752  25 00 2F 00 00                  and eax, 0x2f00
003A2757  3D 00 20 00 00                  cmp eax, 0x2000
003A275C  75 08                           jne 0x1403a2766
003A275E  48 8B CB                        mov rcx, rbx
003A2761  E8 32 FA FF FF                  call 0x1403a2198
003A2766  4C 8B 4D AF                     mov r9, qword ptr [rbp - 0x51]
003A276A  8B 86 E4 01 00 00               mov eax, dword ptr [rsi + 0x1e4]
003A2770  44 3B F0                        cmp r14d, eax
003A2773  0F 84 55 02 00 00               je 0x1403a29ce
003A2779  45 8B CE                        mov r9d, r14d
003A277C  4C 8B C7                        mov r8, rdi
003A277F  BA 05 00 00 00                  mov edx, 5
003A2784  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A2789  B9 C7 00 00 00                  mov ecx, 0xc7
003A278E  E8 CD AE 15 00                  call 0x1404fd660
003A2793  CC                              int3
003A2794  F6 41 01 20                     test byte ptr [rcx + 1], 0x20
003A2798  0F 85 F9 FD FF FF               jne 0x1403a2597
003A279E  F6 07 04                        test byte ptr [rdi], 4
003A27A1  74 0C                           je 0x1403a27af
003A27A3  48 8D 4D BF                     lea rcx, [rbp - 0x41]
003A27A7  E8 14 7D E6 FF                  call 0x14020a4c0
003A27AC  4C 8B D0                        mov r10, rax
003A27AF  4C 8B 5B 58                     mov r11, qword ptr [rbx + 0x58]
003A27B3  0F B6 0F                        movzx ecx, byte ptr [rdi]
003A27B6  4D 03 DA                        add r11, r10
003A27B9  4D 3B DA                        cmp r11, r10
003A27BC  0F 82 A3 00 00 00               jb 0x1403a2865
003A27C2  49 83 FB FF                     cmp r11, -1
003A27C6  0F 84 99 00 00 00               je 0x1403a2865
003A27CC  45 32 F6                        xor r14b, r14b
003A27CF  F6 C1 2E                        test cl, 0x2e
003A27D2  75 23                           jne 0x1403a27f7
003A27D4  44 39 25 6D 44 C2 00            cmp dword ptr [rip + 0xc2446d], r12d
003A27DB  0F 84 BB 00 00 00               je 0x1403a289c
003A27E1  F6 C1 10                        test cl, 0x10
003A27E4  75 11                           jne 0x1403a27f7
003A27E6  80 C9 10                        or cl, 0x10
003A27E9  88 8B 81 00 00 00               mov byte ptr [rbx + 0x81], cl
003A27EF  48 8B CB                        mov rcx, rbx
003A27F2  E8 11 FC FF FF                  call 0x1403a2408
003A27F7  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
003A27FB  48 83 F8 FF                     cmp rax, -1
003A27FF  74 11                           je 0x1403a2812
003A2801  48 2B 43 48                     sub rax, qword ptr [rbx + 0x48]
003A2805  0F 85 E6 00 00 00               jne 0x1403a28f1
003A280B  49 8B C3                        mov rax, r11
003A280E  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
003A2812  4C 89 5B 48                     mov qword ptr [rbx + 0x48], r11
003A2816  48 8D 0D E3 CD C2 00            lea rcx, [rip + 0xc2cde3]
003A281D  44 88 65 A8                     mov byte ptr [rbp - 0x58], r12b
003A2821  E8 0A 5C E6 FF                  call 0x140208430
003A2826  4C 8D 4D A8                     lea r9, [rbp - 0x58]
003A282A  33 D2                           xor edx, edx
003A282C  4C 8D 45 AA                     lea r8, [rbp - 0x56]
003A2830  48 8B CB                        mov rcx, rbx
003A2833  E8 68 04 00 00                  call 0x1403a2ca0
003A2838  48 8D 0D C1 CD C2 00            lea rcx, [rip + 0xc2cdc1]
003A283F  0F B6 F8                        movzx edi, al
003A2842  E8 29 3E E6 FF                  call 0x140206670
003A2847  44 38 65 A8                     cmp byte ptr [rbp - 0x58], r12b
003A284B  0F 85 11 04 00 00               jne 0x1403a2c62
003A2851  40 84 FF                        test dil, dil
003A2854  0F 84 07 01 00 00               je 0x1403a2961
003A285A  41 BF 01 00 00 00               mov r15d, 1
003A2860  E9 32 FD FF FF                  jmp 0x1403a2597
003A2865  41 B6 01                        mov r14b, 1
003A2868  49 C7 C3 FE FF FF FF            mov r11, 0xfffffffffffffffe
003A286F  E9 5B FF FF FF                  jmp 0x1403a27cf
003A2874  80 F9 02                        cmp cl, 2
003A2877  0F 85 E3 02 00 00               jne 0x1403a2b60
003A287D  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
003A2881  48 8B D0                        mov rdx, rax
003A2884  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
003A2888  E8 A3 72 E7 FF                  call 0x140219b30
003A288D  83 6B 04 01                     sub dword ptr [rbx + 4], 1
003A2891  0F 84 70 FD FF FF               je 0x1403a2607
003A2897  E9 16 FD FF FF                  jmp 0x1403a25b2
003A289C  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
003A28A0  4C 8D 43 08                     lea r8, [rbx + 8]
003A28A4  49 3B D0                        cmp rdx, r8
003A28A7  0F 84 3F 03 00 00               je 0x1403a2bec
003A28AD  48 8B CA                        mov rcx, rdx
003A28B0  48 8B 12                        mov rdx, qword ptr [rdx]
003A28B3  0F B6 41 10                     movzx eax, byte ptr [rcx + 0x10]
003A28B7  84 C0                           test al, al
003A28B9  75 30                           jne 0x1403a28eb
003A28BB  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
003A28BF  48 8B 88 20 02 00 00            mov rcx, qword ptr [rax + 0x220]
003A28C6  E8 45 07 00 00                  call 0x1403a3010
003A28CB  84 C0                           test al, al
003A28CD  74 D5                           je 0x1403a28a4
003A28CF  0F B6 83 81 00 00 00            movzx eax, byte ptr [rbx + 0x81]
003A28D6  A8 10                           test al, 0x10
003A28D8  0F 85 19 FF FF FF               jne 0x1403a27f7
003A28DE  0C 10                           or al, 0x10
003A28E0  88 83 81 00 00 00               mov byte ptr [rbx + 0x81], al
003A28E6  E9 04 FF FF FF                  jmp 0x1403a27ef
003A28EB  3C 01                           cmp al, 1
003A28ED  75 B5                           jne 0x1403a28a4
003A28EF  EB CA                           jmp 0x1403a28bb
003A28F1  4A 8D 0C 10                     lea rcx, [rax + r10]
003A28F5  49 3B CA                        cmp rcx, r10
003A28F8  72 28                           jb 0x1403a2922
003A28FA  48 83 F9 FF                     cmp rcx, -1
003A28FE  74 22                           je 0x1403a2922
003A2900  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
003A2904  48 03 C1                        add rax, rcx
003A2907  48 3B C1                        cmp rax, rcx
003A290A  72 0A                           jb 0x1403a2916
003A290C  48 83 F8 FF                     cmp rax, -1
003A2910  0F 85 F8 FE FF FF               jne 0x1403a280e
003A2916  48 C7 C0 FE FF FF FF            mov rax, 0xfffffffffffffffe
003A291D  E9 EC FE FF FF                  jmp 0x1403a280e
003A2922  48 C7 C1 FE FF FF FF            mov rcx, 0xfffffffffffffffe
003A2929  EB D5                           jmp 0x1403a2900
003A292B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003A2930  49 3B FE                        cmp rdi, r14
003A2933  0F 84 17 02 00 00               je 0x1403a2b50
003A2939  48 8B C7                        mov rax, rdi
003A293C  48 8B 3F                        mov rdi, qword ptr [rdi]
003A293F  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
003A2943  80 F9 01                        cmp cl, 1
003A2946  0F 85 86 02 00 00               jne 0x1403a2bd2
003A294C  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
003A2951  45 33 C9                        xor r9d, r9d
003A2954  48 8B D0                        mov rdx, rax
003A2957  49 8B CD                        mov rcx, r13
003A295A  E8 71 DD FA FF                  call 0x1403506d0
003A295F  EB CF                           jmp 0x1403a2930
003A2961  45 84 F6                        test r14b, r14b
003A2964  0F 85 2D FC FF FF               jne 0x1403a2597
003A296A  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
003A296E  48 8B 53 58                     mov rdx, qword ptr [rbx + 0x58]
003A2972  48 8D 0C 10                     lea rcx, [rax + rdx]
003A2976  48 3B C8                        cmp rcx, rax
003A2979  0F 82 AD 01 00 00               jb 0x1403a2b2c
003A297F  48 83 F9 FF                     cmp rcx, -1
003A2983  0F 84 A3 01 00 00               je 0x1403a2b2c
003A2989  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
003A298D  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
003A2991  48 83 F9 FF                     cmp rcx, -1
003A2995  0F 84 7B FE FF FF               je 0x1403a2816
003A299B  48 8D 04 11                     lea rax, [rcx + rdx]
003A299F  48 3B C1                        cmp rax, rcx
003A29A2  0F 82 93 01 00 00               jb 0x1403a2b3b
003A29A8  48 83 F8 FF                     cmp rax, -1
003A29AC  0F 84 89 01 00 00               je 0x1403a2b3b
003A29B2  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
003A29B6  E9 5B FE FF FF                  jmp 0x1403a2816
003A29BB  BA 00 00 02 40                  mov edx, 0x40020000
003A29C0  48 8D 4D FF                     lea rcx, [rbp - 1]
003A29C4  E8 87 D2 FF FF                  call 0x14039fc50
003A29C9  E9 F1 FC FF FF                  jmp 0x1403a26bf
003A29CE  48 0F BE 86 32 02 00 00         movsx rax, byte ptr [rsi + 0x232]
003A29D6  44 3A E0                        cmp r12b, al
003A29D9  74 20                           je 0x1403a29fb
003A29DB  4C 8B C0                        mov r8, rax
003A29DE  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
003A29E7  41 B9 05 00 00 00               mov r9d, 5
003A29ED  48 8B D7                        mov rdx, rdi
003A29F0  B9 F9 01 00 00                  mov ecx, 0x1f9
003A29F5  E8 66 AC 15 00                  call 0x1404fd660
003A29FA  CC                              int3
003A29FB  45 84 FF                        test r15b, r15b
003A29FE  75 35                           jne 0x1403a2a35
003A2A00  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
003A2A04  48 33 CC                        xor rcx, rsp
003A2A07  E8 34 9C 30 00                  call 0x1406ac640
003A2A0C  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
003A2A14  48 81 C4 B0 00 00 00            add rsp, 0xb0
003A2A1B  41 5F                           pop r15
003A2A1D  41 5E                           pop r14
003A2A1F  41 5D                           pop r13
003A2A21  41 5C                           pop r12
003A2A23  5F                              pop rdi
003A2A24  5E                              pop rsi
003A2A25  5D                              pop rbp
003A2A26  C3                              ret
003A2A27  CC                              int3
003A2A28  48 8B C7                        mov rax, rdi
003A2A2B  E8 A0 80 31 00                  call 0x1406baad0
003A2A30  E9 EF FC FF FF                  jmp 0x1403a2724
003A2A35  4C 33 0D 14 48 C2 00            xor r9, qword ptr [rip + 0xc24814]
003A2A3C  49 BA 77 72 DD F3 C7 C6 35 7E   movabs r10, 0x7e35c6c7f3dd7277
003A2A46  4C 8B 05 2B 45 C2 00            mov r8, qword ptr [rip + 0xc2452b]
003A2A4D  48 8B C3                        mov rax, rbx
003A2A50  48 33 05 F9 47 C2 00            xor rax, qword ptr [rip + 0xc247f9]
003A2A57  41 8B C8                        mov ecx, r8d
003A2A5A  48 0F C8                        bswap rax
003A2A5D  48 33 C7                        xor rax, rdi
003A2A60  48 89 7D E7                     mov qword ptr [rbp - 0x19], rdi
003A2A64  48 D3 C8                        ror rax, cl
003A2A67  49 33 C0                        xor rax, r8
003A2A6A  49 0F AF C2                     imul rax, r10
003A2A6E  49 0F C9                        bswap r9
003A2A71  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
003A2A75  4C 33 CB                        xor r9, rbx
003A2A78  49 D3 C9                        ror r9, cl
003A2A7B  4D 33 C8                        xor r9, r8
003A2A7E  4D 0F AF CA                     imul r9, r10
003A2A82  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
003A2A86  44 0F B6 4D A9                  movzx r9d, byte ptr [rbp - 0x57]
003A2A8B  41 0F B6 C1                     movzx eax, r9b
003A2A8F  24 20                           and al, 0x20
003A2A91  02 C0                           add al, al
003A2A93  44 0F B6 C0                     movzx r8d, al
003A2A97  41 0F B6 C0                     movzx eax, r8b
003A2A9B  0C 04                           or al, 4
003A2A9D  0F B6 C8                        movzx ecx, al
003A2AA0  41 F6 C1 02                     test r9b, 2
003A2AA4  41 0F 44 C8                     cmove ecx, r8d
003A2AA8  44 0F B6 C1                     movzx r8d, cl
003A2AAC  41 0F B6 C0                     movzx eax, r8b
003A2AB0  0C 08                           or al, 8
003A2AB2  41 F6 C1 04                     test r9b, 4
003A2AB6  0F B6 C8                        movzx ecx, al
003A2AB9  41 0F 44 C8                     cmove ecx, r8d
003A2ABD  0F B6 D1                        movzx edx, cl
003A2AC0  0F B6 C2                        movzx eax, dl
003A2AC3  0C 10                           or al, 0x10
003A2AC5  41 F6 C1 08                     test r9b, 8
003A2AC9  0F B6 C8                        movzx ecx, al
003A2ACC  0F 44 CA                        cmove ecx, edx
003A2ACF  88 4D F7                        mov byte ptr [rbp - 9], cl
003A2AD2  48 85 FF                        test rdi, rdi
003A2AD5  74 06                           je 0x1403a2add
003A2AD7  80 C9 01                        or cl, 1
003A2ADA  88 4D F7                        mov byte ptr [rbp - 9], cl
003A2ADD  48 83 7D D7 00                  cmp qword ptr [rbp - 0x29], 0
003A2AE2  74 06                           je 0x1403a2aea
003A2AE4  80 C9 02                        or cl, 2
003A2AE7  88 4D F7                        mov byte ptr [rbp - 9], cl
003A2AEA  48 85 FF                        test rdi, rdi
003A2AED  75 0E                           jne 0x1403a2afd
003A2AEF  BA 00 00 02 40                  mov edx, 0x40020000
003A2AF4  48 8D 4D FF                     lea rcx, [rbp - 1]
003A2AF8  E8 53 D1 FF FF                  call 0x14039fc50
003A2AFD  48 8D 45 FF                     lea rax, [rbp - 1]
003A2B01  B9 69 0F 00 00                  mov ecx, 0xf69
003A2B06  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003A2B0B  4C 8D 45 C7                     lea r8, [rbp - 0x39]
003A2B0F  41 B9 38 00 00 00               mov r9d, 0x38
003A2B15  C7 44 24 20 02 0E 50 00         mov dword ptr [rsp + 0x20], 0x500e02
003A2B1D  BA 00 00 02 40                  mov edx, 0x40020000
003A2B22  E8 09 09 00 00                  call 0x1403a3430
003A2B27  E9 D4 FE FF FF                  jmp 0x1403a2a00
003A2B2C  41 B6 01                        mov r14b, 1
003A2B2F  48 C7 C1 FE FF FF FF            mov rcx, 0xfffffffffffffffe
003A2B36  E9 4E FE FF FF                  jmp 0x1403a2989
003A2B3B  48 C7 C0 FE FF FF FF            mov rax, 0xfffffffffffffffe
003A2B42  E9 6B FE FF FF                  jmp 0x1403a29b2
003A2B47  44 88 65 A7                     mov byte ptr [rbp - 0x59], r12b
003A2B4B  E9 3D FA FF FF                  jmp 0x1403a258d
003A2B50  48 8D 43 08                     lea rax, [rbx + 8]
003A2B54  48 89 40 08                     mov qword ptr [rax + 8], rax
003A2B58  48 89 00                        mov qword ptr [rax], rax
003A2B5B  E9 A7 FA FF FF                  jmp 0x1403a2607
003A2B60  80 F9 04                        cmp cl, 4
003A2B63  0F 84 A3 00 00 00               je 0x1403a2c0c
003A2B69  45 33 C9                        xor r9d, r9d
003A2B6C  41 B8 00 01 00 00               mov r8d, 0x100
003A2B72  48 8B D0                        mov rdx, rax
003A2B75  49 8B CD                        mov rcx, r13
003A2B78  E8 53 DB FA FF                  call 0x1403506d0
003A2B7D  E9 30 FA FF FF                  jmp 0x1403a25b2
003A2B82  8B 0B                           mov ecx, dword ptr [rbx]
003A2B84  8B D1                           mov edx, ecx
003A2B86  81 E2 7F F0 FF FF               and edx, 0xfffff07f
003A2B8C  41 C1 E7 08                     shl r15d, 8
003A2B90  41 0B D7                        or edx, r15d
003A2B93  8B C1                           mov eax, ecx
003A2B95  F0 0F B1 13                     lock cmpxchg dword ptr [rbx], edx
003A2B99  3B C8                           cmp ecx, eax
003A2B9B  74 15                           je 0x1403a2bb2
003A2B9D  8B D0                           mov edx, eax
003A2B9F  8B C8                           mov ecx, eax
003A2BA1  81 E2 7F F0 FF FF               and edx, 0xfffff07f
003A2BA7  41 0B D7                        or edx, r15d
003A2BAA  F0 0F B1 13                     lock cmpxchg dword ptr [rbx], edx
003A2BAE  3B C8                           cmp ecx, eax
003A2BB0  75 EB                           jne 0x1403a2b9d
003A2BB2  81 E2 00 3F 00 00               and edx, 0x3f00
003A2BB8  81 FA 00 20 00 00               cmp edx, 0x2000
003A2BBE  75 42                           jne 0x1403a2c02
003A2BC0  48 8B CB                        mov rcx, rbx
003A2BC3  E8 D0 F5 FF FF                  call 0x1403a2198
003A2BC8  44 0F B6 7D A7                  movzx r15d, byte ptr [rbp - 0x59]
003A2BCD  E9 94 FB FF FF                  jmp 0x1403a2766
003A2BD2  80 F9 02                        cmp cl, 2
003A2BD5  75 51                           jne 0x1403a2c28
003A2BD7  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
003A2BDB  48 8B D0                        mov rdx, rax
003A2BDE  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
003A2BE2  E8 49 6F E7 FF                  call 0x140219b30
003A2BE7  E9 44 FD FF FF                  jmp 0x1403a2930
003A2BEC  0F B6 83 81 00 00 00            movzx eax, byte ptr [rbx + 0x81]
003A2BF3  A8 10                           test al, 0x10
003A2BF5  0F 84 FC FB FF FF               je 0x1403a27f7
003A2BFB  24 EF                           and al, 0xef
003A2BFD  E9 DE FC FF FF                  jmp 0x1403a28e0
003A2C02  44 0F B6 7D A7                  movzx r15d, byte ptr [rbp - 0x59]
003A2C07  E9 5E FB FF FF                  jmp 0x1403a276a
003A2C0C  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
003A2C10  4C 8B C0                        mov r8, rax
003A2C13  44 89 63 04                     mov dword ptr [rbx + 4], r12d
003A2C17  48 8B D3                        mov rdx, rbx
003A2C1A  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
003A2C1E  E8 2D 50 E6 FF                  call 0x140207c50
003A2C23  E9 8A F9 FF FF                  jmp 0x1403a25b2
003A2C28  80 F9 04                        cmp cl, 4
003A2C2B  74 19                           je 0x1403a2c46
003A2C2D  45 33 C9                        xor r9d, r9d
003A2C30  41 B8 00 01 00 00               mov r8d, 0x100
003A2C36  48 8B D0                        mov rdx, rax
003A2C39  49 8B CD                        mov rcx, r13
003A2C3C  E8 8F DA FA FF                  call 0x1403506d0
003A2C41  E9 EA FC FF FF                  jmp 0x1403a2930
003A2C46  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
003A2C4A  4C 8B C0                        mov r8, rax
003A2C4D  44 89 63 04                     mov dword ptr [rbx + 4], r12d
003A2C51  48 8B D3                        mov rdx, rbx
003A2C54  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
003A2C58  E8 F3 4F E6 FF                  call 0x140207c50
003A2C5D  E9 CE FC FF FF                  jmp 0x1403a2930
003A2C62  8B 0D 48 F3 B7 00               mov ecx, dword ptr [rip + 0xb7f348]
003A2C68  48 8D 05 D1 5F C2 00            lea rax, [rip + 0xc25fd1]
003A2C6F  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
003A2C73  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003A2C7C  44 8B 05 C9 23 C2 00            mov r8d, dword ptr [rip + 0xc223c9]
003A2C83  E8 F8 0B 0A 00                  call 0x140443880
003A2C88  E9 C4 FB FF FF                  jmp 0x1403a2851
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiExpireTimer2(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int8 v_stack_mB5;
    unsigned __int8 v_stack_mB6;
    unsigned __int8 v_stack_mB7;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 10912317)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r12 = 0;
    v_stack_mA8 = a4;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mA0 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_mB5 = 0;
    v_stack_mB6 = 0;
    v_stack_m88 = 0;
    if (((*(unsigned int *)(v_rip + 12731874)) & (0x20000ULL)) == 0) goto loc_003A2B47;
    v_stack_m98 = *(unsigned __int64 *)(a1 + 72);
    v_stack_m90 = *(unsigned __int64 *)(a1 + 80);
    v_stack_m88 = *(unsigned __int64 *)(a1 + 88);
    v_stack_mB6 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 129));
    v_stack_mB8 = 1;
loc_003A258D:
    if ((*(unsigned __int64 *)(a1 + 88)) != 0) goto loc_003A2794;
loc_003A2597:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1)) & (127));
    *(unsigned int *)(a1 + 4) = 1;
    if (((unsigned __int8)(result)) != 25) goto loc_003A2930;
loc_003A25B2:
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_003A2607;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_003A25CF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) != (*(unsigned __int64 *)(a1 + 8))) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8)) = a1;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16))) != 1) goto loc_003A2874;
    a4 = 0;
    result = KiTryUnwaitThread(a2, *(unsigned __int64 *)(a1 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003A25B2;
    if ((unsigned __int8)(result) != 0) goto loc_003A25B2;
loc_003A2607:
    v_rdi = (*(unsigned __int64 *)(a1 + 96)) ^ (*(unsigned __int64 *)(v_rip + 12732778));
    v_rdi = (v_rdi) ^ (a1);
    v_stack_mB0 = 0;
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(v_rip + 12733490));
    if (condition_is_equal) goto loc_003A2B82;
    v_r15 = (unsigned int)((0) | (16));
    a3 = (*(unsigned __int64 *)(a1 + 104)) ^ (*(unsigned __int64 *)(v_rip + 12732778));
    v_r15 = (unsigned int)((v_r15) << (8));
    a3 = (a3) ^ (a1);
    a3 = (a3) ^ (*(unsigned __int64 *)(v_rip + 12733490));
    v_stack_mB0 = a3;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (0xFFFFF07FULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(v_r15)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_003A2693;
loc_003A267C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) & (0xFFFFF07FULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(v_r15)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_003A267C;
loc_003A2693:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))));
    if ((*(unsigned __int64 *)(a2 + 11528)) != 0) {
        a4 = 2;
        a3 = 0;
        a1 = a2;
        a2 = a4 - 1;
        result = KiProcessThreadWaitList(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_stack_mB8) != 0) goto loc_003A29BB;
loc_003A26BF:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8))))) & (15));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA8))) + 1);
    *(unsigned int *)(v_stack_mA8) = (unsigned int)(result);
    a1 = (a1) + 1;
    *(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8) = v_rdi;
    v_stack_mA8 = v_stack_mA8 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8;
    *(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8 + 8) = *(unsigned __int64 *)((unsigned int)((unsigned int)(a1)));
    result = 0;
    *(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8 + 16) = 0;
    *(unsigned int *)(a2 + 34396) = 0;
    *(unsigned __int8 *)(a2 + 14522) = 1;
    if (v_rdi != (v_rip + 2354)) goto loc_003A2A28;
    result = ExpHpGCTimerCallback(a1, v_stack_mB0, a3, a4);
loc_003A2724:
    *(unsigned __int8 *)(a2 + 14522) = 0;
    *(unsigned __int64 *)(v_stack_mA8 + 16) = *(unsigned __int64 *)(result);
loc_003A2746:
    if (v_rdi != (v_rip + 2354)) goto loc_003A2746;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0x2F00ULL));
    if (((unsigned int)(result)) == 0x2000ULL) {
        a1 = a1;
        result = KiFinalizeTimer2Disablement(a1, v_stack_mB0, a3, a4);
    }
loc_003A276A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484))))) goto loc_003A29CE;
    v_stack_mC8 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484));
    result = KeBugCheckEx(199, 5, v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484)))));
loc_003A2794:
    if (((*(unsigned __int8 *)(199 + 1)) & (32)) != 0) goto loc_003A2597;
    v_r10 = a3;
    if (((*(unsigned __int8 *)(v_rdi)) & (4)) != 0) {
        a1 = v_stack_mA0;
        result = RtlGetInterruptTimePrecise(a1, 5, v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484)))));
        v_r10 = result;
    }
    v_r11 = (*(unsigned __int64 *)(a1 + 88)) + (v_r10);
    if (v_r11 < v_r10) goto loc_003A2865;
    if (v_r11 == -1) goto loc_003A2865;
    v_r14 = 0;
loc_003A27CF:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) & (46)) != 0) goto loc_003A27F7;
    if ((*(unsigned int *)(v_rip + 12731501)) == ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562)))) goto loc_003A289C;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) & (16)) != 0) goto loc_003A27F7;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rdi)) | (16));
    *(unsigned __int8 *)(a1 + 129) = (unsigned __int8)(a1);
loc_003A27EF:
    result = KiUpdateTimer2Collections(a1, 5, v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484)))));
loc_003A27F7:
    if ((*(unsigned __int64 *)(a1 + 80)) == -1) goto loc_003A2812;
    result = (*(unsigned __int64 *)(a1 + 80)) - (*(unsigned __int64 *)(a1 + 72));
    if (condition_is_not_equal) goto loc_003A28F1;
loc_003A280E:
    *(unsigned __int64 *)(a1 + 80) = v_r11;
loc_003A2812:
    *(unsigned __int64 *)(a1 + 72) = v_r11;
loc_003A2816:
    v_stack_mB7 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562));
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 12766691, 5, v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 484)))));
    a2 = 0;
    result = KiInsertTimer2WithCollectionLockHeld(a1, a2, v_stack_mB5, v_stack_mB7);
    result = KxReleaseSpinLock(v_rip + 12766657, a2, v_stack_mB5, v_stack_mB7);
    if (v_stack_mB7 != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562)))) goto loc_003A2C62;
loc_003A2851:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_003A2961;
    goto loc_003A2597;
loc_003A2865:
    goto loc_003A27CF;
loc_003A2874:
    if (((unsigned __int8)(v_rip + 12766657)) != 2) goto loc_003A2B60;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, v_stack_mB5, v_stack_mB7);
    if (((unsigned __int8)(v_rip + 12766657)) == 2) goto loc_003A2607;
    goto loc_003A25B2;
loc_003A289C:
loc_003A28A4:
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_003A2BEC;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16)) != 0) goto loc_003A28EB;
loc_003A28BB:
    result = PsTimerResolutionActive(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)), a1 + 8, v_stack_mB7);
    if ((unsigned __int8)(result) == 0) goto loc_003A28A4;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 129))) & (16)) != 0) goto loc_003A27F7;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 129)) | (16));
loc_003A28E0:
    *(unsigned __int8 *)(a1 + 129) = (unsigned __int8)(result);
    goto loc_003A27EF;
loc_003A28EB:
    if (((unsigned __int8)(result)) != 1) goto loc_003A28A4;
    goto loc_003A28BB;
loc_003A28F1:
    if ((result + v_r10 * 1) < v_r10) goto loc_003A2922;
    if ((result + v_r10 * 1) == -1) goto loc_003A2922;
loc_003A2900:
    result = (*(unsigned __int64 *)(a1 + 88)) + (result + v_r10 * 1);
    if (result < (result + v_r10 * 1)) goto loc_003A2916;
    if (result != -1) goto loc_003A280E;
loc_003A2916:
    goto loc_003A280E;
loc_003A2922:
    goto loc_003A2900;
loc_003A2930:
    if (((unsigned __int8)(result)) == 1) goto loc_003A2B50;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + 16))) != 1) goto loc_003A2BD2;
    a4 = 0;
    result = KiTryUnwaitThread(0, (unsigned __int8)(result), *(unsigned __int16 *)((unsigned __int8)(result) + 18), a4);
    goto loc_003A2930;
loc_003A2961:
    if (1 != 0) goto loc_003A2597;
    if ((*(unsigned __int64 *)(a1 + 72) + *(unsigned __int64 *)(a1 + 88) * 1) < (*(unsigned __int64 *)(a1 + 72))) goto loc_003A2B2C;
    if ((*(unsigned __int64 *)(a1 + 72) + *(unsigned __int64 *)(a1 + 88) * 1) == -1) goto loc_003A2B2C;
loc_003A2989:
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72) + *(unsigned __int64 *)(a1 + 88) * 1;
    if ((*(unsigned __int64 *)(a1 + 80)) == -1) goto loc_003A2816;
    if ((*(unsigned __int64 *)(a1 + 80) + *(unsigned __int64 *)(a1 + 88) * 1) < (*(unsigned __int64 *)(a1 + 80))) goto loc_003A2B3B;
    if ((*(unsigned __int64 *)(a1 + 80) + *(unsigned __int64 *)(a1 + 88) * 1) == -1) goto loc_003A2B3B;
loc_003A29B2:
    *(unsigned __int64 *)(a1 + 80) = *(unsigned __int64 *)(a1 + 80) + *(unsigned __int64 *)(a1 + 88) * 1;
    goto loc_003A2816;
loc_003A29BB:
    result = EtwGetKernelTraceTimestamp(v_stack_m60, (unsigned int)(0x40020000ULL), *(unsigned __int16 *)((unsigned __int8)(result) + 18), a4);
    goto loc_003A26BF;
loc_003A29CE:
    result = (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562))) != ((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562))))) {
        a3 = (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562));
        v_stack_mC8 = 0;
        a4 = 5;
        a2 = *(unsigned __int64 *)((unsigned __int8)(result));
        a1 = 505;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (1 != 0) goto loc_003A2A35;
loc_003A2A00:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
loc_003A2A28:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_003A2724;
loc_003A2A35:
    a4 = (a4) ^ (*(unsigned __int64 *)(v_rip + 12732436));
    result = (v_stack_p18) ^ (*(unsigned __int64 *)(v_rip + 12732409));
    result = (result) ^ (*(unsigned __int64 *)((unsigned __int8)(result)));
    v_stack_m78 = *(unsigned __int64 *)((unsigned __int8)(result));
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 12731691));
    result = (result) * (v_r10);
    v_stack_m80 = result;
    a4 = (a4) ^ (v_stack_p18);
    a4 = (a4) ^ (*(unsigned __int64 *)(v_rip + 12731691));
    a4 = (a4) * (v_r10);
    v_stack_m70 = a4;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_mB6)) & (32));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(result))) | (4));
    a1 = (unsigned __int8)(result);
    if ((((unsigned __int8)(v_stack_mB6)) & (2)) == 0) { a1 = (unsigned int)((unsigned __int8)(result)); }
    result = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(a1))) | (8));
    a1 = (unsigned __int8)(result);
    if ((((unsigned __int8)(v_stack_mB6)) & (4)) == 0) { a1 = (unsigned int)((unsigned __int8)(a1)); }
    result = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(a1))) | (16));
    a1 = (unsigned __int8)(result);
    if ((((unsigned __int8)(v_stack_mB6)) & (8)) == 0) { a1 = (unsigned int)((unsigned __int8)(a1)); }
    v_stack_m68 = (unsigned __int8)(a1);
    if (*(unsigned __int64 *)((unsigned __int8)(result)) != 0) {
        a1 = (unsigned __int8)((a1) | (1));
        v_stack_m68 = (unsigned __int8)(a1);
    }
    if (v_stack_m88 != 0) {
        a1 = (unsigned __int8)((a1) | (2));
        v_stack_m68 = (unsigned __int8)(a1);
    }
    if (*(unsigned __int64 *)((unsigned __int8)(result)) == 0) {
        a2 = 0x40020000ULL;
        a1 = v_stack_m60;
        result = EtwGetKernelTraceTimestamp(a1, a2, (unsigned __int8)(a1), v_stack_mB6);
    }
    v_stack_p28 = v_stack_m60;
    v_stack_p20 = 0x500E02ULL;
    result = EtwTraceTimedEvent((unsigned int)(0xF69ULL), (unsigned int)(0x40020000ULL), v_stack_m98, 56);
    goto loc_003A2A00;
loc_003A2B2C:
    goto loc_003A2989;
loc_003A2B3B:
    goto loc_003A29B2;
loc_003A2B47:
    v_stack_mB8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562));
    goto loc_003A258D;
loc_003A2B50:
    *(unsigned __int64 *)(v_stack_p18 + 8 + 8) = v_stack_p18 + 8;
    *(unsigned __int64 *)(v_stack_p18 + 8) = v_stack_p18 + 8;
    goto loc_003A2607;
loc_003A2B60:
    if (-2 == 4) goto loc_003A2C0C;
    a4 = 0;
    result = KiTryUnwaitThread(a2, v_stack_p18 + 8, 256, a4);
    goto loc_003A25B2;
loc_003A2B82:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18))))) & (0xFFFFF07FULL));
    v_r15 = (unsigned int)((1) << (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_r15)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18))))))) goto loc_003A2BB2;
loc_003A2B9D:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18))))))) & (0xFFFFF07FULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_r15)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18))))))) goto loc_003A2B9D;
loc_003A2BB2:
    a2 = (unsigned int)((a2) & (0x3F00ULL));
    if (((unsigned int)(a2)) != 0x2000ULL) goto loc_003A2C02;
    result = KiFinalizeTimer2Disablement(v_stack_p18, a2, 256, a4);
    goto loc_003A2766;
loc_003A2BD2:
    if (((unsigned __int8)(v_stack_p18)) != 2) goto loc_003A2C28;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, 256, a4);
    goto loc_003A2930;
loc_003A2BEC:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18 + 129))) & (16)) == 0) goto loc_003A27F7;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p18 + 129)) & (239));
    goto loc_003A28E0;
loc_003A2C02:
    goto loc_003A276A;
loc_003A2C0C:
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(v_stack_p18 + 4) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562));
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), v_stack_p18, result, a4);
    goto loc_003A25B2;
loc_003A2C28:
    if (((unsigned __int8)(*(unsigned __int64 *)(result + 24))) == 4) goto loc_003A2C46;
    a4 = 0;
    result = KiTryUnwaitThread(a2, result, 256, a4);
    goto loc_003A2930;
loc_003A2C46:
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(v_stack_p18 + 4) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 562));
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), v_stack_p18, result, a4);
    goto loc_003A2930;
loc_003A2C62:
    result = KiHvEnlightenedGuestPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_rip + 12738513 + (unsigned int)(*(unsigned int *)(v_rip + 12055368)) * 8), (unsigned int)(*(unsigned int *)(v_rip + 12723145)), a4);
    goto loc_003A2851;
}
```

## 5. (Beta) C Style

```c
int64_t KiExpireTimer2(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint8_t v_stack_mB5;
    uint8_t v_stack_mB6;
    uint8_t v_stack_mB7;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0xA6823D)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r12 = 0;
    v_stack_mA8 = Arg4;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mA0 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_mB5 = 0;
    v_stack_mB6 = 0;
    v_stack_m88 = 0;
    if (((*(uint32_t *)(v_rip + 0xC245E2)) & (0x20000ULL)) == 0) goto loc_003A2B47;
    v_stack_m98 = *(uint64_t *)(arg1 + 0x48);
    v_stack_m90 = *(uint64_t *)(arg1 + 0x50);
    v_stack_m88 = *(uint64_t *)(arg1 + 0x58);
    v_stack_mB6 = (uint8_t)(*(uint8_t *)(arg1 + 0x81));
    v_stack_mB8 = 1;
loc_003A258D:
    if ((*(uint64_t *)(arg1 + 0x58)) != 0) goto loc_003A2794;
loc_003A2597:
    result = (uint8_t)((*(uint8_t *)(arg1)) & (127));
    *(uint32_t *)(arg1 + 0x4) = 1;
    if (((uint8_t)(result)) != 25) goto loc_003A2930;
loc_003A25B2:
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_003A2607;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_003A25CF;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) != (*(uint64_t *)(arg1 + 0x8))) {
        Arg1 = 3;
    }
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8)) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10))) != 1) goto loc_003A2874;
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg2, *(uint64_t *)(arg1 + 0x8), *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003A25B2;
    if ((uint8_t)(result) != 0) goto loc_003A25B2;
loc_003A2607:
    local_rdi = (*(uint64_t *)(arg1 + 0x60)) ^ (*(uint64_t *)(v_rip + 0xC2496A));
    local_rdi = (local_rdi) ^ (Arg1);
    v_stack_mB0 = 0;
    local_rdi = (local_rdi) ^ (*(uint64_t *)(v_rip + 0xC24C32));
    if (condition_is_equal) goto loc_003A2B82;
    local_r15 = (uint32_t)((0) | (16));
    Arg3 = (*(uint64_t *)(arg1 + 0x68)) ^ (*(uint64_t *)(v_rip + 0xC2496A));
    local_r15 = (uint32_t)((local_r15) << (8));
    Arg3 = (Arg3) ^ (Arg1);
    Arg3 = (Arg3) ^ (*(uint64_t *)(v_rip + 0xC24C32));
    v_stack_mB0 = Arg3;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) & (0xFFFFF07FULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_r15)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))))) goto loc_003A2693;
loc_003A267C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))))) & (0xFFFFF07FULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_r15)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))))) goto loc_003A267C;
loc_003A2693:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))));
    if ((*(uint64_t *)(arg2 + 0x2D08)) != 0) {
        Arg4 = 2;
        Arg3 = 0;
        Arg1 = Arg2;
        Arg2 = Arg4 - 1;
        result = KiProcessThreadWaitList(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)(v_stack_mB8) != 0) goto loc_003A29BB;
loc_003A26BF:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8))))) & (15));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA8))) + 1);
    *(uint32_t *)(v_stack_mA8) = (uint32_t)(result);
    Arg1 = (Arg1) + 1;
    *(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)(arg1)) + arg1 * 2 * 8) = local_rdi;
    v_stack_mA8 = v_stack_mA8 + (uint32_t)((uint32_t)(Arg1)) + Arg1 * 2 * 8;
    *(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)(arg1)) + arg1 * 2 * 8 + 0x8) = *(uint64_t *)((uint32_t)((uint32_t)(arg1)));
    result = 0;
    *(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)(arg1)) + arg1 * 2 * 8 + 0x10) = 0;
    *(uint32_t *)(arg2 + 0x865C) = 0;
    *(uint8_t *)(arg2 + 0x38BA) = 1;
    if (local_rdi != (v_rip + 2354)) goto loc_003A2A28;
    result = ExpHpGCTimerCallback(Arg1, v_stack_mB0, Arg3, Arg4);
loc_003A2724:
    *(uint8_t *)(arg2 + 0x38BA) = 0;
    *(uint64_t *)(v_stack_mA8 + 0x10) = *(uint64_t *)(result);
loc_003A2746:
    if (local_rdi != (v_rip + 2354)) goto loc_003A2746;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (0x2F00ULL));
    if (((uint32_t)(result)) == 0x2000ULL) {
        Arg1 = Arg1;
        result = KiFinalizeTimer2Disablement(Arg1, v_stack_mB0, Arg3, Arg4);
    }
loc_003A276A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4))))) goto loc_003A29CE;
    v_stack_mC8 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4));
    result = KeBugCheckEx(199, 5, local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4)))));
loc_003A2794:
    if (((*(uint8_t *)(199 + 0x1)) & (32)) != 0) goto loc_003A2597;
    local_r10 = Arg3;
    if (((*(uint8_t *)(local_rdi)) & (4)) != 0) {
        Arg1 = v_stack_mA0;
        result = RtlGetInterruptTimePrecise(Arg1, 5, local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4)))));
        local_r10 = result;
    }
    local_r11 = (*(uint64_t *)(arg1 + 0x58)) + (local_r10);
    if (local_r11 < local_r10) goto loc_003A2865;
    if (local_r11 == -1) goto loc_003A2865;
    local_r14 = 0;
loc_003A27CF:
    if ((((uint8_t)(*(uint8_t *)(local_rdi))) & (46)) != 0) goto loc_003A27F7;
    if ((*(uint32_t *)(v_rip + 0xC2446D)) == ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232)))) goto loc_003A289C;
    if ((((uint8_t)(*(uint8_t *)(local_rdi))) & (16)) != 0) goto loc_003A27F7;
    Arg1 = (uint8_t)((*(uint8_t *)(local_rdi)) | (16));
    *(uint8_t *)(arg1 + 0x81) = (uint8_t)(Arg1);
loc_003A27EF:
    result = KiUpdateTimer2Collections(Arg1, 5, local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4)))));
loc_003A27F7:
    if ((*(uint64_t *)(arg1 + 0x50)) == -1) goto loc_003A2812;
    result = (*(uint64_t *)(arg1 + 0x50)) - (*(uint64_t *)(arg1 + 0x48));
    if (condition_is_not_equal) goto loc_003A28F1;
loc_003A280E:
    *(uint64_t *)(arg1 + 0x50) = local_r11;
loc_003A2812:
    *(uint64_t *)(arg1 + 0x48) = local_r11;
loc_003A2816:
    v_stack_mB7 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232));
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 12766691, 5, local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1E4)))));
    Arg2 = 0;
    result = KiInsertTimer2WithCollectionLockHeld(Arg1, Arg2, v_stack_mB5, v_stack_mB7);
    result = KxReleaseSpinLock(v_rip + 12766657, Arg2, v_stack_mB5, v_stack_mB7);
    if (v_stack_mB7 != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232)))) goto loc_003A2C62;
loc_003A2851:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_003A2961;
    goto loc_003A2597;
loc_003A2865:
    goto loc_003A27CF;
loc_003A2874:
    if (((uint8_t)(v_rip + 12766657)) != 2) goto loc_003A2B60;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, v_stack_mB5, v_stack_mB7);
    if (((uint8_t)(v_rip + 12766657)) == 2) goto loc_003A2607;
    goto loc_003A25B2;
loc_003A289C:
loc_003A28A4:
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_003A2BEC;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)) != 0) goto loc_003A28EB;
loc_003A28BB:
    result = PsTimerResolutionActive(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x220), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)), Arg1 + 8, v_stack_mB7);
    if ((uint8_t)(result) == 0) goto loc_003A28A4;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x81))) & (16)) != 0) goto loc_003A27F7;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x81)) | (16));
loc_003A28E0:
    *(uint8_t *)(arg1 + 0x81) = (uint8_t)(result);
    goto loc_003A27EF;
loc_003A28EB:
    if (((uint8_t)(result)) != 1) goto loc_003A28A4;
    goto loc_003A28BB;
loc_003A28F1:
    if ((result + local_r10 * 1) < local_r10) goto loc_003A2922;
    if ((result + local_r10 * 1) == -1) goto loc_003A2922;
loc_003A2900:
    result = (*(uint64_t *)(arg1 + 0x58)) + (result + local_r10 * 1);
    if (result < (result + local_r10 * 1)) goto loc_003A2916;
    if (result != -1) goto loc_003A280E;
loc_003A2916:
    goto loc_003A280E;
loc_003A2922:
    goto loc_003A2900;
loc_003A2930:
    if (((uint8_t)(result)) == 1) goto loc_003A2B50;
    if (((uint8_t)(*(uint8_t *)((uint8_t)(result) + 0x10))) != 1) goto loc_003A2BD2;
    Arg4 = 0;
    result = KiTryUnwaitThread(0, (uint8_t)(result), *(uint16_t *)((uint8_t)(result) + 0x12), Arg4);
    goto loc_003A2930;
loc_003A2961:
    if (1 != 0) goto loc_003A2597;
    if ((*(uint64_t *)(arg1 + 0x48) + *(uint64_t *)(arg1 + 0x58) * 1) < (*(uint64_t *)(arg1 + 0x48))) goto loc_003A2B2C;
    if ((*(uint64_t *)(arg1 + 0x48) + *(uint64_t *)(arg1 + 0x58) * 1) == -1) goto loc_003A2B2C;
loc_003A2989:
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48) + *(uint64_t *)(arg1 + 0x58) * 1;
    if ((*(uint64_t *)(arg1 + 0x50)) == -1) goto loc_003A2816;
    if ((*(uint64_t *)(arg1 + 0x50) + *(uint64_t *)(arg1 + 0x58) * 1) < (*(uint64_t *)(arg1 + 0x50))) goto loc_003A2B3B;
    if ((*(uint64_t *)(arg1 + 0x50) + *(uint64_t *)(arg1 + 0x58) * 1) == -1) goto loc_003A2B3B;
loc_003A29B2:
    *(uint64_t *)(arg1 + 0x50) = *(uint64_t *)(arg1 + 0x50) + *(uint64_t *)(arg1 + 0x58) * 1;
    goto loc_003A2816;
loc_003A29BB:
    result = EtwGetKernelTraceTimestamp(v_stack_m60, (uint32_t)(0x40020000ULL), *(uint16_t *)((uint8_t)(result) + 0x12), Arg4);
    goto loc_003A26BF;
loc_003A29CE:
    result = (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232))) != ((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232))))) {
        Arg3 = (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232));
        v_stack_mC8 = 0;
        Arg4 = 5;
        Arg2 = *(uint64_t *)((uint8_t)(result));
        Arg1 = 505;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (1 != 0) goto loc_003A2A35;
loc_003A2A00:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
loc_003A2A28:
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    goto loc_003A2724;
loc_003A2A35:
    Arg4 = (Arg4) ^ (*(uint64_t *)(v_rip + 0xC24814));
    result = (v_stack_p18) ^ (*(uint64_t *)(v_rip + 0xC247F9));
    result = (result) ^ (*(uint64_t *)((uint8_t)(result)));
    v_stack_m78 = *(uint64_t *)((uint8_t)(result));
    result = (result) ^ (*(uint64_t *)(v_rip + 0xC2452B));
    result = (result) * (local_r10);
    v_stack_m80 = result;
    Arg4 = (Arg4) ^ (v_stack_p18);
    Arg4 = (Arg4) ^ (*(uint64_t *)(v_rip + 0xC2452B));
    Arg4 = (Arg4) * (local_r10);
    v_stack_m70 = Arg4;
    result = (uint8_t)(((uint8_t)(v_stack_mB6)) & (32));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)(((uint8_t)((uint8_t)(result))) | (4));
    Arg1 = (uint8_t)(result);
    if ((((uint8_t)(v_stack_mB6)) & (2)) == 0) { Arg1 = (uint32_t)((uint8_t)(result)); }
    result = (uint8_t)(((uint8_t)((uint8_t)(Arg1))) | (8));
    Arg1 = (uint8_t)(result);
    if ((((uint8_t)(v_stack_mB6)) & (4)) == 0) { Arg1 = (uint32_t)((uint8_t)(Arg1)); }
    result = (uint8_t)(((uint8_t)((uint8_t)(Arg1))) | (16));
    Arg1 = (uint8_t)(result);
    if ((((uint8_t)(v_stack_mB6)) & (8)) == 0) { Arg1 = (uint32_t)((uint8_t)(Arg1)); }
    v_stack_m68 = (uint8_t)(Arg1);
    if (*(uint64_t *)((uint8_t)(result)) != 0) {
        Arg1 = (uint8_t)((Arg1) | (1));
        v_stack_m68 = (uint8_t)(Arg1);
    }
    if (v_stack_m88 != 0) {
        Arg1 = (uint8_t)((Arg1) | (2));
        v_stack_m68 = (uint8_t)(Arg1);
    }
    if (*(uint64_t *)((uint8_t)(result)) == 0) {
        Arg2 = 0x40020000ULL;
        Arg1 = v_stack_m60;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, (uint8_t)(Arg1), v_stack_mB6);
    }
    v_stack_p28 = v_stack_m60;
    v_stack_p20 = 0x500E02ULL;
    result = EtwTraceTimedEvent((uint32_t)(0xF69ULL), (uint32_t)(0x40020000ULL), v_stack_m98, 56);
    goto loc_003A2A00;
loc_003A2B2C:
    goto loc_003A2989;
loc_003A2B3B:
    goto loc_003A29B2;
loc_003A2B47:
    v_stack_mB8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232));
    goto loc_003A258D;
loc_003A2B50:
    *(uint64_t *)(v_stack_p18 + 0x8 + 0x8) = v_stack_p18 + 8;
    *(uint64_t *)(v_stack_p18 + 0x8) = v_stack_p18 + 8;
    goto loc_003A2607;
loc_003A2B60:
    if (-2 == 4) goto loc_003A2C0C;
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg2, v_stack_p18 + 8, 256, Arg4);
    goto loc_003A25B2;
loc_003A2B82:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18))))) & (0xFFFFF07FULL));
    local_r15 = (uint32_t)((1) << (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_r15)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18))))))) goto loc_003A2BB2;
loc_003A2B9D:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18))))))) & (0xFFFFF07FULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_r15)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18))))))) goto loc_003A2B9D;
loc_003A2BB2:
    Arg2 = (uint32_t)((Arg2) & (0x3F00ULL));
    if (((uint32_t)(Arg2)) != 0x2000ULL) goto loc_003A2C02;
    result = KiFinalizeTimer2Disablement(v_stack_p18, Arg2, 256, Arg4);
    goto loc_003A2766;
loc_003A2BD2:
    if (((uint8_t)(v_stack_p18)) != 2) goto loc_003A2C28;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, 256, Arg4);
    goto loc_003A2930;
loc_003A2BEC:
    if ((((uint8_t)(*(uint8_t *)(v_stack_p18 + 0x81))) & (16)) == 0) goto loc_003A27F7;
    result = (uint8_t)((*(uint8_t *)(v_stack_p18 + 0x81)) & (239));
    goto loc_003A28E0;
loc_003A2C02:
    goto loc_003A276A;
loc_003A2C0C:
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(v_stack_p18 + 0x4) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232));
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), v_stack_p18, result, Arg4);
    goto loc_003A25B2;
loc_003A2C28:
    if (((uint8_t)(*(uint64_t *)(result + 0x18))) == 4) goto loc_003A2C46;
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg2, result, 256, Arg4);
    goto loc_003A2930;
loc_003A2C46:
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(v_stack_p18 + 0x4) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x232));
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), v_stack_p18, result, Arg4);
    goto loc_003A2930;
loc_003A2C62:
    result = KiHvEnlightenedGuestPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(v_rip + 0xC25FD1 + (uint32_t)(*(uint32_t *)(v_rip + 0xB7F348)) * 8), (uint32_t)(*(uint32_t *)(v_rip + 0xC223C9)), Arg4);
    goto loc_003A2851;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x81` | `8` | `R` |
| `Arg1` | `+ 0x81` | `8` | `W` |
| `Arg1` | `+ 0x81` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x2D08` | `64` | `R` |
| `Arg2` | `+ 0x38BA` | `8` | `W` |
| `Arg2` | `+ 0x865C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A24E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
