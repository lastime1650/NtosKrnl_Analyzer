# MiDecommitAddToList

- RVA: `0x00242264`–`0x00242A53` (길이 `2,031` bytes)
- VA: `0x0000000140242264`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00061994`
- 디코드: `443`개 명령, `2,031/2,031` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x002422C3` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002423C5` → [MiTerminateWsle](../23/MiTerminateWsle_function_0023EDF0.md) (function, `0x0023EDF0`)
- `0x002423FB` → [MiUnlockWsle](../40/MiUnlockWsle_function_00407F84.md) (function, `0x00407F84`)
- `0x00242434` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x00242544` → [MiInitializeTbFlushStamps](../44/MiInitializeTbFlushStamps_function_004499EC.md) (function, `0x004499EC`)
- `0x002425B3` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x002425F2` → [MiLogRemoveWsleEvent](../4D/MiLogRemoveWsleEvent_function_004D64BC.md) (function, `0x004D64BC`)
- `0x00242627` → [MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED](MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED_function_002400C0.md) (function, `0x002400C0`)
- `0x002426B0` → [MiVmAccessLoggingEnabled](../36/MiVmAccessLoggingEnabled_function_003629D4.md) (function, `0x003629D4`)
- `0x00242932` → [MI_WSLE_LOG_ACCESS](../29/MI_WSLE_LOG_ACCESS_function_00294400.md) (function, `0x00294400`)
- `0x00242951` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00242964` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024297F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00242992` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002429AD` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002429BF` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00242A12` → [MiWriteWsle](../29/MiWriteWsle_function_00292CA0.md) (function, `0x00292CA0`)
- `0x00242A3F` → [MI_FLUSH_ENTIRE_TB](../31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (function, `0x00314110`)

### Direct callers
- [sub_00241A6E](Unknown_function_00241A6E.md) at `0x00241AB6`
- [sub_00241C55](Unknown_function_00241C55.md) at `0x00241D51`
- [MiDeleteVa](../27/MiDeleteVa_function_002789E0.md) at `0x00278B8D`

### Static image references
- `0x00242549` → RVA `0x00E2DC80` (`.data`; read)
- `0x002425DF` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0024261A` → RVA `0x00010880` (`.rdata`; read)
- `0x00242826` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0024290F` → RVA `0x00E30088` (`.data`; read)
- `0x00242943` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00242800` → [sub_006D7C5C + 0x62](../6D/Unknown_function_006D7C5C.md) (`tail-transfer`)
  - `0x002428A0` → [sub_006D7C5C](../6D/Unknown_function_006D7C5C.md) (`tail-transfer`)
  - `0x002428B3` → [sub_006D7C5C](../6D/Unknown_function_006D7C5C.md) (`tail-transfer`)
  - `0x002428BD` → [sub_006D7C5C](../6D/Unknown_function_006D7C5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00242264  40 53                           push rbx
00242266  55                              push rbp
00242267  56                              push rsi
00242268  57                              push rdi
00242269  41 54                           push r12
0024226B  41 55                           push r13
0024226D  41 56                           push r14
0024226F  41 57                           push r15
00242271  48 83 EC 58                     sub rsp, 0x58
00242275  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00242279  48 8B DA                        mov rbx, rdx
0024227C  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
00242283  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00242288  4C 8B EB                        mov r13, rbx
0024228B  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
00242293  49 C1 ED 09                     shr r13, 9
00242297  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002422A1  4C 23 E8                        and r13, rax
002422A4  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
002422AE  48 8B E9                        mov rbp, rcx
002422B1  48 8B C6                        mov rax, rsi
002422B4  4C 03 E8                        add r13, rax
002422B7  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
002422BB  49 8B CD                        mov rcx, r13
002422BE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002422C3  E8 D8 05 04 00                  call 0x1402828a0
002422C8  45 33 D2                        xor r10d, r10d
002422CB  48 8B F8                        mov rdi, rax
002422CE  45 8D 5A 01                     lea r11d, [r10 + 1]
002422D2  84 C0                           test al, al
002422D4  78 0C                           js 0x1402422e2
002422D6  48 8B C6                        mov rax, rsi
002422D9  48 3B D8                        cmp rbx, rax
002422DC  0F 83 CB 04 00 00               jae 0x1402427ad
002422E2  45 8B FA                        mov r15d, r10d
002422E5  48 8B C7                        mov rax, rdi
002422E8  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
002422ED  48 C1 E8 0C                     shr rax, 0xc
002422F1  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002422FB  48 23 C1                        and rax, rcx
002422FE  44 89 9C 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r11d
00242306  45 8B C3                        mov r8d, r11d
00242309  48 8D 34 40                     lea rsi, [rax + rax*2]
0024230D  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00242317  48 C1 E6 04                     shl rsi, 4
0024231B  48 8B C0                        mov rax, rax
0024231E  48 03 F0                        add rsi, rax
00242321  45 85 FF                        test r15d, r15d
00242324  0F 84 E5 00 00 00               je 0x14024240f
0024232A  48 8B 1E                        mov rbx, qword ptr [rsi]
0024232D  48 C1 EB 2A                     shr rbx, 0x2a
00242331  80 E3 07                        and bl, 7
00242334  41 8B D3                        mov edx, r11d
00242337  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0024233B  48 85 C9                        test rcx, rcx
0024233E  41 0F 48 D2                     cmovs edx, r10d
00242342  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
00242349  8B 45 28                        mov eax, dword ptr [rbp + 0x28]
0024234C  45 8B E0                        mov r12d, r8d
0024234F  B9 03 00 00 00                  mov ecx, 3
00242354  85 C0                           test eax, eax
00242356  0F 85 2C 03 00 00               jne 0x140242688
0024235C  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00242364  8A C3                           mov al, bl
00242366  44 89 94 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r10d
0024236E  24 0F                           and al, 0xf
00242370  45 8B F2                        mov r14d, r10d
00242373  3C 08                           cmp al, 8
00242375  74 70                           je 0x1402423e7
00242377  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
0024237C  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00242384  B9 02 00 00 00                  mov ecx, 2
00242389  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
00242393  45 85 C0                        test r8d, r8d
00242396  0F 84 60 02 00 00               je 0x1402425fc
0024239C  45 85 F6                        test r14d, r14d
0024239F  0F 85 A1 00 00 00               jne 0x140242446
002423A5  44 8B 45 60                     mov r8d, dword ptr [rbp + 0x60]
002423A9  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
002423B1  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
002423B9  44 8D 49 04                     lea r9d, [rcx + 4]
002423BD  49 8B CC                        mov rcx, r12
002423C0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002423C5  E8 26 CA FF FF                  call 0x14023edf0
002423CA  45 33 D2                        xor r10d, r10d
002423CD  85 C0                           test eax, eax
002423CF  0F 85 56 06 00 00               jne 0x140242a2b
002423D5  48 83 C4 58                     add rsp, 0x58
002423D9  41 5F                           pop r15
002423DB  41 5E                           pop r14
002423DD  41 5D                           pop r13
002423DF  41 5C                           pop r12
002423E1  5F                              pop rdi
002423E2  5E                              pop rsi
002423E3  5D                              pop rbp
002423E4  5B                              pop rbx
002423E5  C3                              ret
002423E6  CC                              int3
002423E7  49 8B D4                        mov rdx, r12
002423EA  45 8B CB                        mov r9d, r11d
002423ED  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002423F2  4C 8B C6                        mov r8, rsi
002423F5  49 8B CC                        mov rcx, r12
002423F8  45 8B F3                        mov r14d, r11d
002423FB  E8 84 5B 1C 00                  call 0x140407f84
00242400  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
00242407  45 33 D2                        xor r10d, r10d
0024240A  E9 6D FF FF FF                  jmp 0x14024237c
0024240F  8B 85 A0 00 00 00               mov eax, dword ptr [rbp + 0xa0]
00242415  0F BA E0 08                     bt eax, 8
00242419  0F 82 AD 05 00 00               jb 0x1402429cc
0024241F  A8 60                           test al, 0x60
00242421  0F 85 B8 05 00 00               jne 0x1402429df
00242427  83 7D 28 06                     cmp dword ptr [rbp + 0x28], 6
0024242B  0F 84 62 04 00 00               je 0x140242893
00242431  48 8B D3                        mov rdx, rbx
00242434  E8 07 41 0D 00                  call 0x140316540
00242439  41 8B D3                        mov edx, r11d
0024243C  8A D8                           mov bl, al
0024243E  44 8B C2                        mov r8d, edx
00242441  E9 F1 FE FF FF                  jmp 0x140242337
00242446  45 85 FF                        test r15d, r15d
00242449  0F 85 BB 02 00 00               jne 0x14024270a
0024244F  44 8B BC 24 B8 00 00 00         mov r15d, dword ptr [rsp + 0xb8]
00242457  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0024245C  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00242464  45 39 91 58 30 00 00            cmp dword ptr [r9 + 0x3058], r10d
0024246B  0F 84 FA 01 00 00               je 0x14024266b
00242471  41 8B 81 58 30 00 00            mov eax, dword ptr [r9 + 0x3058]
00242478  49 89 BC C1 60 30 00 00         mov qword ptr [r9 + rax*8 + 0x3060], rdi
00242480  BF 01 00 00 00                  mov edi, 1
00242485  41 01 B9 58 30 00 00            add dword ptr [r9 + 0x3058], edi
0024248C  33 C0                           xor eax, eax
0024248E  41 8B 91 68 40 00 00            mov edx, dword ptr [r9 + 0x4068]
00242495  44 8D 77 02                     lea r14d, [rdi + 2]
00242499  41 89 84 D1 70 40 00 00         mov dword ptr [r9 + rdx*8 + 0x4070], eax
002424A1  41 8A 8C D1 71 40 00 00         mov cl, byte ptr [r9 + rdx*8 + 0x4071]
002424A9  41 22 CE                        and cl, r14b
002424AC  41 88 9C D1 70 40 00 00         mov byte ptr [r9 + rdx*8 + 0x4070], bl
002424B4  45 85 C0                        test r8d, r8d
002424B7  0F 85 B7 01 00 00               jne 0x140242674
002424BD  80 E1 FD                        and cl, 0xfd
002424C0  41 8A C7                        mov al, r15b
002424C3  02 C0                           add al, al
002424C5  0A C8                           or cl, al
002424C7  41 8B C5                        mov eax, r13d
002424CA  C1 E8 03                        shr eax, 3
002424CD  41 88 8C D1 71 40 00 00         mov byte ptr [r9 + rdx*8 + 0x4071], cl
002424D5  B9 FF 01 00 00                  mov ecx, 0x1ff
002424DA  66 23 C1                        and ax, cx
002424DD  66 41 89 84 D1 72 40 00 00      mov word ptr [r9 + rdx*8 + 0x4072], ax
002424E6  41 8B 81 68 40 00 00            mov eax, dword ptr [r9 + 0x4068]
002424ED  85 C0                           test eax, eax
002424EF  0F 84 87 01 00 00               je 0x14024267c
002424F5  FF C0                           inc eax
002424F7  41 89 81 68 40 00 00            mov dword ptr [r9 + 0x4068], eax
002424FE  48 8B 9D B0 00 00 00            mov rbx, qword ptr [rbp + 0xb0]
00242505  48 85 DB                        test rbx, rbx
00242508  0F 85 81 00 00 00               jne 0x14024258f
0024250E  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00242518  4C 3B E8                        cmp r13, rax
0024251B  0F 83 B2 03 00 00               jae 0x1402428d3
00242521  01 7D 70                        add dword ptr [rbp + 0x70], edi
00242524  8B 85 9C 00 00 00               mov eax, dword ptr [rbp + 0x9c]
0024252A  A8 10                           test al, 0x10
0024252C  74 6E                           je 0x14024259c
0024252E  44 39 55 60                     cmp dword ptr [rbp + 0x60], r10d
00242532  75 68                           jne 0x14024259c
00242534  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
0024253C  4C 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r10
00242544  E8 A3 74 20 00                  call 0x1404499ec
00242549  4C 8B 05 30 B7 BE 00            mov r8, qword ptr [rip + 0xbeb730]
00242550  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00242558  48 8B C1                        mov rax, rcx
0024255B  4D 85 C0                        test r8, r8
0024255E  74 0E                           je 0x14024256e
00242560  F6 C1 10                        test cl, 0x10
00242563  75 09                           jne 0x14024256e
00242565  49 8B C0                        mov rax, r8
00242568  48 F7 D0                        not rax
0024256B  48 23 C1                        and rax, rcx
0024256E  48 BA 00 00 00 00 FF FF FF FF   movabs rdx, 0xffffffff00000000
00242578  48 85 C2                        test rdx, rax
0024257B  0F 84 B7 04 00 00               je 0x140242a38
00242581  83 A4 24 B0 00 00 00 00         and dword ptr [rsp + 0xb0], 0
00242589  49 89 4D 00                     mov qword ptr [r13], rcx
0024258D  EB 0D                           jmp 0x14024259c
0024258F  45 85 FF                        test r15d, r15d
00242592  0F 85 30 02 00 00               jne 0x1402427c8
00242598  49 89 5D 00                     mov qword ptr [r13], rbx
0024259C  83 BC 24 B0 00 00 00 00         cmp dword ptr [rsp + 0xb0], 0
002425A4  74 12                           je 0x1402425b8
002425A6  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
002425AA  45 33 C9                        xor r9d, r9d
002425AD  4C 8B C7                        mov r8, rdi
002425B0  49 8B D4                        mov rdx, r12
002425B3  E8 B8 10 05 00                  call 0x140293670
002425B8  8B 55 28                        mov edx, dword ptr [rbp + 0x28]
002425BB  41 3B D6                        cmp edx, r14d
002425BE  74 1F                           je 0x1402425df
002425C0  8B 85 9C 00 00 00               mov eax, dword ptr [rbp + 0x9c]
002425C6  A8 20                           test al, 0x20
002425C8  0F 85 07 FE FF FF               jne 0x1402423d5
002425CE  85 D2                           test edx, edx
002425D0  0F 84 FF FD FF FF               je 0x1402423d5
002425D6  83 FA 06                        cmp edx, 6
002425D9  0F 84 F6 FD FF FF               je 0x1402423d5
002425DF  F7 05 1B 45 D8 00 00 00 00 08   test dword ptr [rip + 0xd8451b], 0x8000000
002425E9  0F 84 E6 FD FF FF               je 0x1402423d5
002425EF  49 8B CC                        mov rcx, r12
002425F2  E8 C5 3E 29 00                  call 0x1404d64bc
002425F7  E9 D9 FD FF FF                  jmp 0x1402423d5
002425FC  44 8B BC 24 B8 00 00 00         mov r15d, dword ptr [rsp + 0xb8]
00242604  45 8B F2                        mov r14d, r10d
00242607  45 85 FF                        test r15d, r15d
0024260A  0F 85 41 01 00 00               jne 0x140242751
00242610  83 7D 28 06                     cmp dword ptr [rbp + 0x28], 6
00242614  0F 84 80 02 00 00               je 0x14024289a
0024261A  48 8B 15 5F E2 DC FF            mov rdx, qword ptr [rip - 0x231da1]
00242621  45 8B C6                        mov r8d, r14d
00242624  49 8B CD                        mov rcx, r13
00242627  E8 94 DA FF FF                  call 0x1402400c0
0024262C  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
00242633  45 33 D2                        xor r10d, r10d
00242636  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
0024263E  85 C0                           test eax, eax
00242640  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
0024264A  41 8D 42 01                     lea eax, [r10 + 1]
0024264E  0F 45 C8                        cmovne ecx, eax
00242651  89 8C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ecx
00242658  45 85 F6                        test r14d, r14d
0024265B  0F 84 F6 FD FF FF               je 0x140242457
00242661  F0 4C 21 4E 18                  lock and qword ptr [rsi + 0x18], r9
00242666  E9 EC FD FF FF                  jmp 0x140242457
0024266B  4C 89 65 68                     mov qword ptr [rbp + 0x68], r12
0024266F  E9 FD FD FF FF                  jmp 0x140242471
00242674  40 0A CF                        or cl, dil
00242677  E9 41 FE FF FF                  jmp 0x1402424bd
0024267C  4D 89 A1 60 40 00 00            mov qword ptr [r9 + 0x4060], r12
00242683  E9 6D FE FF FF                  jmp 0x1402424f5
00242688  45 85 FF                        test r15d, r15d
0024268B  75 59                           jne 0x1402426e6
0024268D  44 8A F3                        mov r14b, bl
00242690  41 80 E6 0F                     and r14b, 0xf
00242694  41 80 FE 09                     cmp r14b, 9
00242698  0F 84 60 03 00 00               je 0x1402429fe
0024269E  83 C0 FE                        add eax, -2
002426A1  A9 FD FF FF FF                  test eax, 0xfffffffd
002426A6  75 1A                           jne 0x1402426c2
002426A8  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
002426AD  49 8B C8                        mov rcx, r8
002426B0  E8 1F 03 12 00                  call 0x1403629d4
002426B5  85 C0                           test eax, eax
002426B7  0F 85 6F 02 00 00               jne 0x14024292c
002426BD  B9 03 00 00 00                  mov ecx, 3
002426C2  83 7D 28 06                     cmp dword ptr [rbp + 0x28], 6
002426C6  0F 84 78 01 00 00               je 0x140242844
002426CC  44 89 A4 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r12d
002426D4  41 80 FE 08                     cmp r14b, 8
002426D8  0F 84 80 01 00 00               je 0x14024285e
002426DE  44 89 A4 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r12d
002426E6  8B 85 9C 00 00 00               mov eax, dword ptr [rbp + 0x9c]
002426EC  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
002426F4  A8 20                           test al, 0x20
002426F6  0F 84 68 FC FF FF               je 0x140242364
002426FC  39 4D 28                        cmp dword ptr [rbp + 0x28], ecx
002426FF  0F 84 5F FC FF FF               je 0x140242364
00242705  E9 5C 01 00 00                  jmp 0x140242866
0024270A  45 8B F2                        mov r14d, r10d
0024270D  41 BF 01 00 00 00               mov r15d, 1
00242713  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
0024271A  0F 82 03 01 00 00               jb 0x140242823
00242720  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00242724  48 B9 00 00 00 00 00 00 00 40   movabs rcx, 0x4000000000000000
0024272E  48 0B C1                        or rax, rcx
00242731  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00242735  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0024273F  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00242744  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
0024274C  E9 FE FC FF FF                  jmp 0x14024244f
00242751  44 39 54 24 30                  cmp dword ptr [rsp + 0x30], r10d
00242756  0F 85 B4 FE FF FF               jne 0x140242610
0024275C  41 BF 01 00 00 00               mov r15d, 1
00242762  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
00242769  0F 82 03 01 00 00               jb 0x140242872
0024276F  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00242773  48 B9 00 00 00 00 00 00 00 40   movabs rcx, 0x4000000000000000
0024277D  44 8B BC 24 B8 00 00 00         mov r15d, dword ptr [rsp + 0xb8]
00242785  48 0B C1                        or rax, rcx
00242788  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00242790  41 BE 40 00 00 00               mov r14d, 0x40
00242796  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
0024279A  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
002427A4  41 8D 4E C2                     lea ecx, [r14 - 0x3e]
002427A8  E9 63 FE FF FF                  jmp 0x140242610
002427AD  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002427B7  45 8B FB                        mov r15d, r11d
002427BA  48 3B D8                        cmp rbx, rax
002427BD  0F 87 1F FB FF FF               ja 0x1402422e2
002427C3  E9 1D FB FF FF                  jmp 0x1402422e5
002427C8  44 39 54 24 30                  cmp dword ptr [rsp + 0x30], r10d
002427CD  0F 85 C5 FD FF FF               jne 0x140242598
002427D3  4C 8B 75 08                     mov r14, qword ptr [rbp + 8]
002427D7  41 8B FA                        mov edi, r10d
002427DA  41 BC 01 00 00 00               mov r12d, 1
002427E0  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
002427E7  0F 82 FE 00 00 00               jb 0x1402428eb
002427ED  48 8D 7E 10                     lea rdi, [rsi + 0x10]
002427F1  8B 07                           mov eax, dword ptr [rdi]
002427F3  D0 E8                           shr al, 1
002427F5  41 84 C4                        test r12b, al
002427F8  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00242800  0F 85 B8 54 49 00               jne 0x1406d7cbe
00242806  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00242810  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00242815  BF 01 00 00 00                  mov edi, 1
0024281A  44 8D 77 02                     lea r14d, [rdi + 2]
0024281E  E9 75 FD FF FF                  jmp 0x140242598
00242823  45 03 F7                        add r14d, r15d
00242826  44 85 35 7F 2A D8 00            test dword ptr [rip + 0xd82a7f], r14d
0024282D  0F 84 10 01 00 00               je 0x140242943
00242833  F3 90                           pause
00242835  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00242839  48 85 C0                        test rax, rax
0024283C  0F 89 D1 FE FF FF               jns 0x140242713
00242842  EB DF                           jmp 0x140242823
00242844  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00242849  44 89 94 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r10d
00242851  44 39 90 58 30 00 00            cmp dword ptr [rax + 0x3058], r10d
00242858  0F 84 AD 00 00 00               je 0x14024290b
0024285E  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00242866  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0024286A  4C 01 18                        add qword ptr [rax], r11
0024286D  E9 F2 FA FF FF                  jmp 0x140242364
00242872  45 03 F7                        add r14d, r15d
00242875  44 85 35 30 2A D8 00            test dword ptr [rip + 0xd82a30], r14d
0024287C  0F 84 EF 00 00 00               je 0x140242971
00242882  F3 90                           pause
00242884  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00242888  48 85 C0                        test rax, rax
0024288B  0F 89 D1 FE FF FF               jns 0x140242762
00242891  EB DF                           jmp 0x140242872
00242893  B3 4A                           mov bl, 0x4a
00242895  E9 9A FA FF FF                  jmp 0x140242334
0024289A  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0024289D  66 85 C0                        test ax, ax
002428A0  0F 84 B6 53 49 00               je 0x1406d7c5c
002428A6  66 3B C1                        cmp ax, cx
002428A9  76 18                           jbe 0x1402428c3
002428AB  B9 03 00 00 00                  mov ecx, 3
002428B0  66 3B C1                        cmp ax, cx
002428B3  0F 85 A3 53 49 00               jne 0x1406d7c5c
002428B9  F6 46 22 08                     test byte ptr [rsi + 0x22], 8
002428BD  0F 84 99 53 49 00               je 0x1406d7c5c
002428C3  48 8B 05 B6 DF DC FF            mov rax, qword ptr [rip - 0x23204a]
002428CA  49 89 45 00                     mov qword ptr [r13], rax
002428CE  E9 85 FD FF FF                  jmp 0x140242658
002428D3  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
002428DD  4C 3B E8                        cmp r13, rax
002428E0  0F 86 B6 FC FF FF               jbe 0x14024259c
002428E6  E9 36 FC FF FF                  jmp 0x140242521
002428EB  41 03 FC                        add edi, r12d
002428EE  85 3D B8 29 D8 00               test dword ptr [rip + 0xd829b8], edi
002428F4  0F 84 A5 00 00 00               je 0x14024299f
002428FA  F3 90                           pause
002428FC  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00242900  48 85 C0                        test rax, rax
00242903  0F 89 D7 FE FF FF               jns 0x1402427e0
00242909  EB E0                           jmp 0x1402428eb
0024290B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0024290F  48 8B 0D 72 D7 BE 00            mov rcx, qword ptr [rip + 0xbed772]
00242916  48 C1 E8 2B                     shr rax, 0x2b
0024291A  25 FF 03 00 00                  and eax, 0x3ff
0024291F  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00242923  48 89 55 08                     mov qword ptr [rbp + 8], rdx
00242927  E9 32 FF FF FF                  jmp 0x14024285e
0024292C  49 8B D5                        mov rdx, r13
0024292F  49 8B C8                        mov rcx, r8
00242932  E8 C9 1A 05 00                  call 0x140294400
00242937  45 33 D2                        xor r10d, r10d
0024293A  45 8D 5A 01                     lea r11d, [r10 + 1]
0024293E  E9 7A FD FF FF                  jmp 0x1402426bd
00242943  8B 05 6F 41 D8 00               mov eax, dword ptr [rip + 0xd8416f]
00242949  A8 40                           test al, 0x40
0024294B  0F 84 E2 FE FF FF               je 0x140242833
00242951  E8 3A CB 0C 00                  call 0x14030f490
00242956  45 33 D2                        xor r10d, r10d
00242959  84 C0                           test al, al
0024295B  0F 84 D2 FE FF FF               je 0x140242833
00242961  41 8B CE                        mov ecx, r14d
00242964  E8 F7 CA 0C 00                  call 0x14030f460
00242969  45 33 D2                        xor r10d, r10d
0024296C  E9 C4 FE FF FF                  jmp 0x140242835
00242971  8B 05 41 41 D8 00               mov eax, dword ptr [rip + 0xd84141]
00242977  A8 40                           test al, 0x40
00242979  0F 84 03 FF FF FF               je 0x140242882
0024297F  E8 0C CB 0C 00                  call 0x14030f490
00242984  45 33 D2                        xor r10d, r10d
00242987  84 C0                           test al, al
00242989  0F 84 F3 FE FF FF               je 0x140242882
0024298F  41 8B CE                        mov ecx, r14d
00242992  E8 C9 CA 0C 00                  call 0x14030f460
00242997  45 33 D2                        xor r10d, r10d
0024299A  E9 E5 FE FF FF                  jmp 0x140242884
0024299F  8B 05 13 41 D8 00               mov eax, dword ptr [rip + 0xd84113]
002429A5  A8 40                           test al, 0x40
002429A7  0F 84 4D FF FF FF               je 0x1402428fa
002429AD  E8 DE CA 0C 00                  call 0x14030f490
002429B2  45 33 D2                        xor r10d, r10d
002429B5  84 C0                           test al, al
002429B7  0F 84 3D FF FF FF               je 0x1402428fa
002429BD  8B CF                           mov ecx, edi
002429BF  E8 9C CA 0C 00                  call 0x14030f460
002429C4  45 33 D2                        xor r10d, r10d
002429C7  E9 30 FF FF FF                  jmp 0x1402428fc
002429CC  45 8B C2                        mov r8d, r10d
002429CF  44 89 94 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r10d
002429D7  41 8A DA                        mov bl, r10b
002429DA  E9 55 F9 FF FF                  jmp 0x140242334
002429DF  B3 4A                           mov bl, 0x4a
002429E1  44 89 94 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r10d
002429E9  45 8B C2                        mov r8d, r10d
002429EC  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
002429F1  44 89 9C 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r11d
002429F9  E9 4B F9 FF FF                  jmp 0x140242349
002429FE  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00242A06  80 E3 FA                        and bl, 0xfa
00242A09  80 CB 0A                        or bl, 0xa
00242A0C  49 8B D4                        mov rdx, r12
00242A0F  44 8A C3                        mov r8b, bl
00242A12  E8 89 02 05 00                  call 0x140292ca0
00242A17  45 33 D2                        xor r10d, r10d
00242A1A  44 89 94 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r10d
00242A22  45 8D 5A 01                     lea r11d, [r10 + 1]
00242A26  E9 3B FE FF FF                  jmp 0x140242866
00242A2B  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00242A33  E9 0E FA FF FF                  jmp 0x140242446
00242A38  8B D7                           mov edx, edi
00242A3A  B9 02 00 00 00                  mov ecx, 2
00242A3F  E8 CC 16 0D 00                  call 0x140314110
00242A44  33 C9                           xor ecx, ecx
00242A46  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
00242A4E  E9 36 FB FF FF                  jmp 0x140242589
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecommitAddToList(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p8;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pB8;

    v_rsp = (v_rsp) - (88);
    v_rbx = (a2) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 16);
    v_stack_p10 = v_rbx;
    v_r13 = (v_rbx) >> (9);
    v_r13 = (v_r13) & (*(unsigned __int64 *)(a1 + 16));
    v_r13 = (v_r13) + (v_rsi);
    v_stack_m60 = *(unsigned __int64 *)(a1 + 32);
    result = MI_READ_PTE_LOCK_FREE(v_r13, a2, a3, a4);
    v_r10 = 0;
    if (sign_flag) goto loc_002422E2;
    if (v_rbx >= v_rsi) goto loc_002427AD;
loc_002422E2:
loc_002422E5:
    v_stack_m68 = 0;
    result = (result) >> (12);
    result = (result) & (v_r13);
    v_stack_p8 = (unsigned int)(v_r10 + 1);
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result);
    if (0 == 0) goto loc_0024240F;
    v_rbx = (*(unsigned __int64 *)(v_rsi)) >> (42);
    v_rbx = (unsigned __int8)((v_rbx) & (7));
loc_00242334:
loc_00242337:
    a2 = (unsigned int)((unsigned int)(v_r10 + 1));
    if (sign_flag) { a2 = 0; }
    v_stack_p20 = (unsigned int)(a2);
loc_00242349:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))) != 0) goto loc_00242688;
loc_00242364:
    v_stack_p18 = 0;
    result = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_002423E7;
loc_0024237C:
    if ((unsigned int)((unsigned int)(v_stack_p8)) == 0) goto loc_002425FC;
    if (0 != 0) goto loc_00242446;
    v_stack_m78 = v_stack_p18;
    result = MiTerminateWsle(v_stack_m60, v_stack_p10, (unsigned int)(*(unsigned int *)(a1 + 96)), 2 + 4);
    v_r10 = 0;
    if ((unsigned int)(result) != 0) goto loc_00242A2B;
loc_002423D5:
    v_rsp = (v_rsp) + (88);
    return result;
loc_002423E7:
    result = MiUnlockWsle(v_stack_p38, v_stack_m60, v_rsi, (unsigned int)((unsigned int)(v_r10 + 1)));
    v_stack_pB0 = (unsigned int)(result);
    v_r10 = 0;
    goto loc_0024237C;
loc_0024240F:
    if (condition_is_below) goto loc_002429CC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 160)))) & (96)) != 0) goto loc_002429DF;
    if ((*(unsigned int *)(a1 + 40)) == 6) goto loc_00242893;
    result = MiGetWsleContents(v_stack_p38, v_rbx, v_rsi, (unsigned int)((unsigned int)(v_r10 + 1)));
    goto loc_00242337;
loc_00242446:
    if (0 != 0) goto loc_0024270A;
loc_0024244F:
loc_00242457:
    if ((*(unsigned int *)(v_stack_p40 + 12376)) == 0) goto loc_0024266B;
loc_00242471:
    *(unsigned __int64 *)(v_stack_p40 + (unsigned int)(*(unsigned int *)(v_stack_p40 + 12376)) * 8 + 12384) = result;
    result = 0;
    *(unsigned int *)(v_stack_p40 + (unsigned int)(*(unsigned int *)(v_stack_p40 + 16488)) * 8 + 16496) = 0;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p40 + (unsigned int)(*(unsigned int *)(v_stack_p40 + 16488)) * 8 + 16497)) & ((unsigned __int8)(1 + 2)));
    *(unsigned __int8 *)(v_stack_p40 + (unsigned int)(*(unsigned int *)(v_stack_p40 + 16488)) * 8 + 16496) = (unsigned __int8)((unsigned __int8)(result));
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10 + 1))))) != 0) goto loc_00242674;
loc_002424BD:
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_pB8))) + ((unsigned __int8)((unsigned __int8)((unsigned int)(v_stack_pB8)))));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (3));
    *(unsigned __int8 *)(v_stack_p40 + (unsigned int)(*(unsigned int *)(v_stack_p40 + 16488)) * 8 + 16497) = (unsigned __int8)(a1);
    result = (unsigned __int16)((result) & (511));
    *(unsigned __int16 *)(v_stack_p40 + (unsigned int)(*(unsigned int *)(v_stack_p40 + 16488)) * 8 + 16498) = (unsigned __int16)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 16488))) == 0) goto loc_0024267C;
loc_002424F5:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 16488))) + 1);
    *(unsigned int *)(v_stack_p40 + 16488) = (unsigned int)(result);
    if (*(unsigned __int64 *)(a1 + 176) != 0) goto loc_0024258F;
    if (v_r13 >= result) goto loc_002428D3;
loc_00242521:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (16)) == 0) goto loc_0024259C;
    if ((*(unsigned int *)(a1 + 96)) != 0) goto loc_0024259C;
    v_stack_pA8 = 0;
    result = MiInitializeTbFlushStamps(v_stack_pA8, (unsigned int)(*(unsigned int *)(v_stack_p40 + 16488)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10 + 1)))), v_stack_p40);
    if (*(unsigned __int64 *)(v_rip + 12498736) == 0) goto loc_0024256E;
    result = v_stack_pA8;
    if ((((unsigned __int8)(v_stack_pA8)) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 12498736);
        result = ~(result);
        result = (result) & (v_stack_pA8);
    }
    if ((((unsigned int)(*(unsigned int *)(v_stack_p40 + 16488))) & (result)) == 0) goto loc_00242A38;
loc_00242589:
    *(unsigned __int64 *)(v_r13) = v_stack_pA8;
    goto loc_0024259C;
loc_0024258F:
    if ((unsigned int)((unsigned int)(v_stack_pB8)) != 0) goto loc_002427C8;
loc_00242598:
    *(unsigned __int64 *)(v_r13) = *(unsigned __int64 *)(a1 + 176);
loc_0024259C:
    if (v_stack_pB0 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 16);
        a4 = 0;
        a3 = 1;
        a2 = v_stack_pA8;
        result = MiInsertTbFlushEntry(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) == ((unsigned int)(1 + 2))) goto loc_002425DF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (32)) != 0) goto loc_002423D5;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))) == 0) goto loc_002423D5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) == 6) goto loc_002423D5;
loc_002425DF:
    if (((*(unsigned int *)(v_rip + 14173467)) & (0x8000000ULL)) == 0) goto loc_002423D5;
    result = MiLogRemoveWsleEvent(v_stack_pA8, (unsigned int)(*(unsigned int *)(a1 + 40)), a3, a4);
    goto loc_002423D5;
loc_002425FC:
    if ((unsigned int)((unsigned int)(v_stack_pB8)) != 0) goto loc_00242751;
loc_00242610:
    if ((*(unsigned int *)(a1 + 40)) == 6) goto loc_0024289A;
    result = MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED(v_r13, *(unsigned __int64 *)(v_rip - 2301345), 0, a4);
    v_r10 = 0;
    a1 = (unsigned int)(v_stack_pB0);
    if ((unsigned int)(result) != 0) { a1 = (unsigned int)(v_r10 + 1); }
    v_stack_pB0 = (unsigned int)(a1);
loc_00242658:
    if (0 == 0) goto loc_00242457;
    goto loc_00242457;
loc_0024266B:
    *(unsigned __int64 *)(a1 + 104) = v_stack_pA8;
    goto loc_00242471;
loc_00242674:
    a1 = (unsigned __int8)((a1) | (1));
    goto loc_002424BD;
loc_0024267C:
    *(unsigned __int64 *)(a4 + 16480) = v_stack_pA8;
    goto loc_002424F5;
loc_00242688:
    if ((unsigned int)((unsigned int)(v_stack_pB8)) != 0) goto loc_002426E6;
    v_r14 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))) & (15));
    if (((unsigned __int8)(v_r14)) == 9) goto loc_002429FE;
    result = (unsigned int)((v_r10 + 1) + (-2));
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_002426C2;
    result = MiVmAccessLoggingEnabled(v_stack_p38, *(unsigned __int64 *)(v_rip - 2301345), v_stack_p38, a4);
    if ((unsigned int)(result) != 0) goto loc_0024292C;
loc_002426BD:
loc_002426C2:
    if ((*(unsigned int *)(a1 + 40)) == 6) goto loc_00242844;
    v_stack_pA0 = (unsigned int)(v_stack_pA8);
    if (((unsigned __int8)(v_r14)) == 8) goto loc_0024285E;
    v_stack_pA0 = (unsigned int)(v_stack_pA8);
loc_002426E6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (32)) == 0) goto loc_00242364;
    if ((*(unsigned int *)(a1 + 40)) == 3) goto loc_00242364;
    goto loc_00242866;
loc_0024270A:
loc_00242713:
    if ((*(unsigned int *)(a1 + 40)) < 3) goto loc_00242823;
    result = (*(unsigned __int64 *)(v_rsi + 24)) | (3);
    *(unsigned __int64 *)(v_rsi + 24) = result;
    goto loc_0024244F;
loc_00242751:
    if (v_stack_p30 != 0) goto loc_00242610;
loc_00242762:
    if (v_stack_p30 < 0) goto loc_00242872;
    result = (*(unsigned __int64 *)(v_rsi + 24)) | (3);
    *(unsigned __int64 *)(v_rsi + 24) = result;
    goto loc_00242610;
loc_002427AD:
    if ((*(unsigned __int64 *)(a1 + 176)) > result) goto loc_002422E2;
    goto loc_002422E5;
loc_002427C8:
    if (v_stack_p30 != 0) goto loc_00242598;
loc_002427E0:
    if (v_stack_p30 < 0) goto loc_002428EB;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rsi + 16))) >> (1));
    goto loc_00242598;
loc_00242823:
    v_r14 = (unsigned int)((1 + 2) + ((unsigned int)((unsigned int)((unsigned int)(v_r10 + 1)))));
    if (((*(unsigned int *)(v_rip + 14166655)) & ((unsigned int)(v_r14))) == 0) goto loc_00242943;
loc_00242833:
loc_00242835:
    if (!sign_flag) goto loc_00242713;
    goto loc_00242823;
loc_00242844:
    v_stack_pA0 = 0;
    if ((*(unsigned int *)(v_stack_p40 + 12376)) == 0) goto loc_0024290B;
loc_0024285E:
loc_00242866:
    goto loc_00242364;
loc_00242872:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)((unsigned int)(v_r10 + 1)))));
    if (((*(unsigned int *)(v_rip + 14166576)) & ((unsigned int)(v_r14))) == 0) goto loc_00242971;
loc_00242882:
loc_00242884:
    if (!sign_flag) goto loc_00242762;
    goto loc_00242872;
loc_00242893:
    goto loc_00242334;
loc_0024289A:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) <= ((unsigned __int16)(64 - 62))) goto loc_002428C3;
loc_002428C3:
    *(unsigned __int64 *)(v_r13) = *(unsigned __int64 *)(v_rip - 2302026);
    goto loc_00242658;
loc_002428D3:
    if (v_r13 <= (*(unsigned __int64 *)(v_rip - 2302026))) goto loc_0024259C;
    goto loc_00242521;
loc_002428EB:
    v_rdi = (unsigned int)((1) + ((unsigned int)(v_stack_pA8)));
    if (((*(unsigned int *)(v_rip + 14166456)) & ((unsigned int)(v_rdi))) == 0) goto loc_0024299F;
loc_002428FA:
loc_002428FC:
    if (!sign_flag) goto loc_002427E0;
    goto loc_002428EB;
loc_0024290B:
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12506994) + result * 8);
    goto loc_0024285E;
loc_0024292C:
    result = MI_WSLE_LOG_ACCESS((unsigned int)(v_stack_pA0), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    goto loc_002426BD;
loc_00242943:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14172527)))) & (64)) == 0) goto loc_00242833;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(v_stack_pA0), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00242833;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    goto loc_00242835;
loc_00242971:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14172481)))) & (64)) == 0) goto loc_00242882;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00242882;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    goto loc_00242884;
loc_0024299F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14172435)))) & (64)) == 0) goto loc_002428FA;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_002428FA;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), v_r13, (unsigned int)(v_stack_pA0), a4);
    v_r10 = 0;
    goto loc_002428FC;
loc_002429CC:
    v_stack_pA0 = 0;
    goto loc_00242334;
loc_002429DF:
    v_stack_pA0 = 0;
    v_stack_p30 = (unsigned int)(v_r10 + 1);
    v_stack_pB8 = (unsigned int)(v_r10 + 1);
    goto loc_00242349;
loc_002429FE:
    v_rbx = (unsigned __int8)((74) & (250));
    v_rbx = (unsigned __int8)((v_rbx) | (10));
    result = MiWriteWsle((unsigned int)((unsigned int)(v_rdi)), v_stack_pA8, (unsigned __int8)(v_rbx), a4);
    v_r10 = 0;
    v_stack_pA0 = 0;
    goto loc_00242866;
loc_00242A2B:
    goto loc_00242446;
loc_00242A38:
    result = MI_FLUSH_ENTIRE_TB(2, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(v_stack_pA0), a4);
    a1 = 0;
    v_stack_pA8 = 0;
    goto loc_00242589;
}
```

## 5. (Beta) C Style

```c
int64_t MiDecommitAddToList(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p8;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pB8;

    local_rsp = (local_rsp) - (88);
    local_rbx = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m58 = *(uint64_t *)(arg1 + 0x10);
    v_stack_p10 = local_rbx;
    local_r13 = (local_rbx) >> (9);
    local_r13 = (local_r13) & (*(uint64_t *)(arg1 + 0x10));
    local_r13 = (local_r13) + (local_rsi);
    v_stack_m60 = *(uint64_t *)(arg1 + 0x20);
    result = MI_READ_PTE_LOCK_FREE(local_r13, Arg2, a3, a4);
    local_r10 = 0;
    if (sign_flag) goto loc_002422E2;
    if (local_rbx >= local_rsi) goto loc_002427AD;
loc_002422E2:
loc_002422E5:
    v_stack_m68 = 0;
    result = (result) >> (12);
    result = (result) & (local_r13);
    v_stack_p8 = (uint32_t)(local_r10 + 1);
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result);
    if (0 == 0) goto loc_0024240F;
    local_rbx = (*(uint64_t *)(local_rsi)) >> (42);
    local_rbx = (uint8_t)((local_rbx) & (7));
loc_00242334:
loc_00242337:
    Arg2 = (uint32_t)((uint32_t)(local_r10 + 1));
    if (sign_flag) { Arg2 = 0; }
    v_stack_p20 = (uint32_t)(Arg2);
loc_00242349:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))) != 0) goto loc_00242688;
loc_00242364:
    v_stack_p18 = 0;
    result = (uint8_t)(((uint8_t)(local_rbx)) & (15));
    if (((uint8_t)(result)) == 8) goto loc_002423E7;
loc_0024237C:
    if ((uint32_t)((uint32_t)(v_stack_p8)) == 0) goto loc_002425FC;
    if (0 != 0) goto loc_00242446;
    v_stack_m78 = v_stack_p18;
    result = MiTerminateWsle(v_stack_m60, v_stack_p10, (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 2 + 4);
    local_r10 = 0;
    if ((uint32_t)(result) != 0) goto loc_00242A2B;
loc_002423D5:
    local_rsp = (local_rsp) + (88);
    return result;
loc_002423E7:
    result = MiUnlockWsle(v_stack_p38, v_stack_m60, local_rsi, (uint32_t)((uint32_t)(local_r10 + 1)));
    v_stack_pB0 = (uint32_t)(result);
    local_r10 = 0;
    goto loc_0024237C;
loc_0024240F:
    if (condition_is_below) goto loc_002429CC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0)))) & (96)) != 0) goto loc_002429DF;
    if ((*(uint32_t *)(arg1 + 0x28)) == 6) goto loc_00242893;
    result = MiGetWsleContents(v_stack_p38, local_rbx, local_rsi, (uint32_t)((uint32_t)(local_r10 + 1)));
    goto loc_00242337;
loc_00242446:
    if (0 != 0) goto loc_0024270A;
loc_0024244F:
loc_00242457:
    if ((*(uint32_t *)(v_stack_p40 + 0x3058)) == 0) goto loc_0024266B;
loc_00242471:
    *(uint64_t *)(v_stack_p40 + (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x3058)) * 8 + 0x3060) = result;
    result = 0;
    *(uint32_t *)(v_stack_p40 + (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068)) * 8 + 0x4070) = 0;
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_p40 + (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068)) * 8 + 0x4071)) & ((uint8_t)(1 + 2)));
    *(uint8_t *)(v_stack_p40 + (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068)) * 8 + 0x4070) = (uint8_t)((uint8_t)(result));
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10 + 1))))) != 0) goto loc_00242674;
loc_002424BD:
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_pB8))) + ((uint8_t)((uint8_t)((uint32_t)(v_stack_pB8)))));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (3));
    *(uint8_t *)(v_stack_p40 + (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068)) * 8 + 0x4071) = (uint8_t)(Arg1);
    result = (uint16_t)((result) & (511));
    *(uint16_t *)(v_stack_p40 + (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068)) * 8 + 0x4072) = (uint16_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068))) == 0) goto loc_0024267C;
loc_002424F5:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068))) + 1);
    *(uint32_t *)(v_stack_p40 + 0x4068) = (uint32_t)(result);
    if (*(uint64_t *)(arg1 + 0xB0) != 0) goto loc_0024258F;
    if (local_r13 >= result) goto loc_002428D3;
loc_00242521:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (16)) == 0) goto loc_0024259C;
    if ((*(uint32_t *)(arg1 + 0x60)) != 0) goto loc_0024259C;
    v_stack_pA8 = 0;
    result = MiInitializeTbFlushStamps(v_stack_pA8, (uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10 + 1)))), v_stack_p40);
    if (*(uint64_t *)(v_rip + 0xBEB730) == 0) goto loc_0024256E;
    result = v_stack_pA8;
    if ((((uint8_t)(v_stack_pA8)) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xBEB730);
        result = ~(result);
        result = (result) & (v_stack_pA8);
    }
    if ((((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x4068))) & (result)) == 0) goto loc_00242A38;
loc_00242589:
    *(uint64_t *)(local_r13) = v_stack_pA8;
    goto loc_0024259C;
loc_0024258F:
    if ((uint32_t)((uint32_t)(v_stack_pB8)) != 0) goto loc_002427C8;
loc_00242598:
    *(uint64_t *)(local_r13) = *(uint64_t *)(arg1 + 0xB0);
loc_0024259C:
    if (v_stack_pB0 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        a4 = 0;
        a3 = 1;
        Arg2 = v_stack_pA8;
        result = MiInsertTbFlushEntry(Arg1, Arg2, a3, a4);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) == ((uint32_t)(1 + 2))) goto loc_002425DF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (32)) != 0) goto loc_002423D5;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))) == 0) goto loc_002423D5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) == 6) goto loc_002423D5;
loc_002425DF:
    if (((*(uint32_t *)(v_rip + 0xD8451B)) & (0x8000000ULL)) == 0) goto loc_002423D5;
    result = MiLogRemoveWsleEvent(v_stack_pA8, (uint32_t)(*(uint32_t *)(arg1 + 0x28)), a3, a4);
    goto loc_002423D5;
loc_002425FC:
    if ((uint32_t)((uint32_t)(v_stack_pB8)) != 0) goto loc_00242751;
loc_00242610:
    if ((*(uint32_t *)(arg1 + 0x28)) == 6) goto loc_0024289A;
    result = MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED(local_r13, *(uint64_t *)(v_rip - 0x231DA1), 0, a4);
    local_r10 = 0;
    Arg1 = (uint32_t)(v_stack_pB0);
    if ((uint32_t)(result) != 0) { Arg1 = (uint32_t)(local_r10 + 1); }
    v_stack_pB0 = (uint32_t)(Arg1);
loc_00242658:
    if (0 == 0) goto loc_00242457;
    goto loc_00242457;
loc_0024266B:
    *(uint64_t *)(arg1 + 0x68) = v_stack_pA8;
    goto loc_00242471;
loc_00242674:
    Arg1 = (uint8_t)((Arg1) | (1));
    goto loc_002424BD;
loc_0024267C:
    *(uint64_t *)(a4 + 0x4060) = v_stack_pA8;
    goto loc_002424F5;
loc_00242688:
    if ((uint32_t)((uint32_t)(v_stack_pB8)) != 0) goto loc_002426E6;
    local_r14 = (uint8_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xB0))) & (15));
    if (((uint8_t)(local_r14)) == 9) goto loc_002429FE;
    result = (uint32_t)((local_r10 + 1) + (-2));
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_002426C2;
    result = MiVmAccessLoggingEnabled(v_stack_p38, *(uint64_t *)(v_rip - 0x231DA1), v_stack_p38, a4);
    if ((uint32_t)(result) != 0) goto loc_0024292C;
loc_002426BD:
loc_002426C2:
    if ((*(uint32_t *)(arg1 + 0x28)) == 6) goto loc_00242844;
    v_stack_pA0 = (uint32_t)(v_stack_pA8);
    if (((uint8_t)(local_r14)) == 8) goto loc_0024285E;
    v_stack_pA0 = (uint32_t)(v_stack_pA8);
loc_002426E6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (32)) == 0) goto loc_00242364;
    if ((*(uint32_t *)(arg1 + 0x28)) == 3) goto loc_00242364;
    goto loc_00242866;
loc_0024270A:
loc_00242713:
    if ((*(uint32_t *)(arg1 + 0x28)) < 3) goto loc_00242823;
    result = (*(uint64_t *)(local_rsi + 0x18)) | (3);
    *(uint64_t *)(local_rsi + 0x18) = result;
    goto loc_0024244F;
loc_00242751:
    if (v_stack_p30 != 0) goto loc_00242610;
loc_00242762:
    if (v_stack_p30 < 0) goto loc_00242872;
    result = (*(uint64_t *)(local_rsi + 0x18)) | (3);
    *(uint64_t *)(local_rsi + 0x18) = result;
    goto loc_00242610;
loc_002427AD:
    if ((*(uint64_t *)(arg1 + 0xB0)) > result) goto loc_002422E2;
    goto loc_002422E5;
loc_002427C8:
    if (v_stack_p30 != 0) goto loc_00242598;
loc_002427E0:
    if (v_stack_p30 < 0) goto loc_002428EB;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x10))) >> (1));
    goto loc_00242598;
loc_00242823:
    local_r14 = (uint32_t)((1 + 2) + ((uint32_t)((uint32_t)((uint32_t)(local_r10 + 1)))));
    if (((*(uint32_t *)(v_rip + 0xD82A7F)) & ((uint32_t)(local_r14))) == 0) goto loc_00242943;
loc_00242833:
loc_00242835:
    if (!sign_flag) goto loc_00242713;
    goto loc_00242823;
loc_00242844:
    v_stack_pA0 = 0;
    if ((*(uint32_t *)(v_stack_p40 + 0x3058)) == 0) goto loc_0024290B;
loc_0024285E:
loc_00242866:
    goto loc_00242364;
loc_00242872:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)((uint32_t)(local_r10 + 1)))));
    if (((*(uint32_t *)(v_rip + 0xD82A30)) & ((uint32_t)(local_r14))) == 0) goto loc_00242971;
loc_00242882:
loc_00242884:
    if (!sign_flag) goto loc_00242762;
    goto loc_00242872;
loc_00242893:
    goto loc_00242334;
loc_0024289A:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) <= ((uint16_t)(64 - 62))) goto loc_002428C3;
loc_002428C3:
    *(uint64_t *)(local_r13) = *(uint64_t *)(v_rip - 0x23204A);
    goto loc_00242658;
loc_002428D3:
    if (local_r13 <= (*(uint64_t *)(v_rip - 0x23204A))) goto loc_0024259C;
    goto loc_00242521;
loc_002428EB:
    local_rdi = (uint32_t)((1) + ((uint32_t)(v_stack_pA8)));
    if (((*(uint32_t *)(v_rip + 0xD829B8)) & ((uint32_t)(local_rdi))) == 0) goto loc_0024299F;
loc_002428FA:
loc_002428FC:
    if (!sign_flag) goto loc_002427E0;
    goto loc_002428EB;
loc_0024290B:
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBED772) + result * 8);
    goto loc_0024285E;
loc_0024292C:
    result = MI_WSLE_LOG_ACCESS((uint32_t)(v_stack_pA0), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    goto loc_002426BD;
loc_00242943:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD8416F)))) & (64)) == 0) goto loc_00242833;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(v_stack_pA0), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00242833;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    goto loc_00242835;
loc_00242971:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD84141)))) & (64)) == 0) goto loc_00242882;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00242882;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    goto loc_00242884;
loc_0024299F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD84113)))) & (64)) == 0) goto loc_002428FA;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_002428FA;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), local_r13, (uint32_t)(v_stack_pA0), a4);
    local_r10 = 0;
    goto loc_002428FC;
loc_002429CC:
    v_stack_pA0 = 0;
    goto loc_00242334;
loc_002429DF:
    v_stack_pA0 = 0;
    v_stack_p30 = (uint32_t)(local_r10 + 1);
    v_stack_pB8 = (uint32_t)(local_r10 + 1);
    goto loc_00242349;
loc_002429FE:
    local_rbx = (uint8_t)((74) & (250));
    local_rbx = (uint8_t)((local_rbx) | (10));
    result = MiWriteWsle((uint32_t)((uint32_t)(local_rdi)), v_stack_pA8, (uint8_t)(local_rbx), a4);
    local_r10 = 0;
    v_stack_pA0 = 0;
    goto loc_00242866;
loc_00242A2B:
    goto loc_00242446;
loc_00242A38:
    result = MI_FLUSH_ENTIRE_TB(2, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(v_stack_pA0), a4);
    Arg1 = 0;
    v_stack_pA8 = 0;
    goto loc_00242589;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x68` | `64` | `W` |
| `Arg1` | `+ 0x70` | `32` | `R/W` |
| `Arg1` | `+ 0x9C` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00242264&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
