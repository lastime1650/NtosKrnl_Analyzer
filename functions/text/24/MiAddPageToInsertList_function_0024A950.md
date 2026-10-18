# MiAddPageToInsertList

- RVA: `0x0024A950`–`0x0024ADF8` (길이 `1,192` bytes)
- VA: `0x000000014024A950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062B78`
- 디코드: `279`개 명령, `1,192/1,192` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0024A9C2` → [MiCanBatchHardFaultPages](MiCanBatchHardFaultPages_function_0024AE00.md) (function, `0x0024AE00`)
- `0x0024A9F1` → [MiEnqueuePageList](MiEnqueuePageList_function_0024AF40.md) (function, `0x0024AF40`)
- `0x0024AAB4` → [MiSignalCommitSignals](MiSignalCommitSignals_function_00249090.md) (function, `0x00249090`)
- `0x0024AB24` → [MiInsertPagesInList](../33/MiInsertPagesInList_function_0033E270.md) (function, `0x0033E270`)
- `0x0024AC35` → [MiInsertPagesInList](../33/MiInsertPagesInList_function_0033E270.md) (function, `0x0033E270`)
- `0x0024AC51` → [MiHardFaultPageRelease](../2B/MiHardFaultPageRelease_function_002B5728.md) (function, `0x002B5728`)
- `0x0024ACD6` → [MiCanBatchSystemCacheUnmapPages](../3F/MiCanBatchSystemCacheUnmapPages_function_003FE680.md) (function, `0x003FE680`)
- `0x0024AD04` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0024AD14` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024AD23` → [MiDecrementShareCountEx](../33/MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x0024AD30` → [MiCanPfnOriginalPteBeLost](../37/MiCanPfnOriginalPteBeLost_function_00373D3C.md) (function, `0x00373D3C`)
- `0x0024AD76` → [ExAcquireSpinLockExclusive](ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0024AD85` → [MiRestockOverCommit](../40/MiRestockOverCommit_function_00407D94.md) (function, `0x00407D94`)
- `0x0024AD98` → [MiReleaseSpinLockExclusive](MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0024ADAE` → [ExAcquireSpinLockExclusiveAtDpcLevel](ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0024ADD4` → [MiReleaseWriteInProgressCharges](../40/MiReleaseWriteInProgressCharges_function_00407B4C.md) (function, `0x00407B4C`)
- `0x0024ADDF` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)

### Direct callers
- [MiUnlockMdlWritePages](MiUnlockMdlWritePages_function_0024A7C0.md) at `0x0024A880`
- [sub_00293C9B](../29/Unknown_function_00293C9B.md) at `0x00293E67`
- [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) at `0x002B7178`
- [MiInsertProtectedStandbyPage](../45/MiInsertProtectedStandbyPage_function_004527D8.md) at `0x004528CE`

### Static image references
- `0x0024AA20` → RVA `0x00E38D00` (`.data`; read)
- `0x0024AA27` → RVA `0x00E30088` (`.data`; read)
- `0x0024ABCC` → RVA `0x00E3CBE6` (`.data`; read)
- `0x0024ABE7` → RVA `0x00E3D240` (`.data`; read)
- `0x0024AC19` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0024ACF6` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0024A950  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0024A955  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0024A95A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0024A95F  57                              push rdi
0024A960  41 54                           push r12
0024A962  41 55                           push r13
0024A964  41 56                           push r14
0024A966  41 57                           push r15
0024A968  48 83 EC 20                     sub rsp, 0x20
0024A96C  8B 71 60                        mov esi, dword ptr [rcx + 0x60]
0024A96F  4F 8D 34 40                     lea r14, [r8 + r8*2]
0024A973  49 C1 E6 04                     shl r14, 4
0024A977  4D 8B F8                        mov r15, r8
0024A97A  4C 8B EA                        mov r13, rdx
0024A97D  48 8B F9                        mov rdi, rcx
0024A980  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0024A98A  49 8D 1C 06                     lea rbx, [r14 + rax]
0024A98E  BD 01 00 00 00                  mov ebp, 1
0024A993  83 FE 03                        cmp esi, 3
0024A996  0F 84 63 02 00 00               je 0x14024abff
0024A99C  48 83 3F 00                     cmp qword ptr [rdi], 0
0024A9A0  0F 84 60 02 00 00               je 0x14024ac06
0024A9A6  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
0024A9AD  0F 82 6C 01 00 00               jb 0x14024ab1f
0024A9B3  83 FE 02                        cmp esi, 2
0024A9B6  0F 85 72 01 00 00               jne 0x14024ab2e
0024A9BC  48 8B D3                        mov rdx, rbx
0024A9BF  49 8B CD                        mov rcx, r13
0024A9C2  E8 39 04 00 00                  call 0x14024ae00
0024A9C7  8B C8                           mov ecx, eax
0024A9C9  85 C0                           test eax, eax
0024A9CB  74 47                           je 0x14024aa14
0024A9CD  48 83 3F 00                     cmp qword ptr [rdi], 0
0024A9D1  75 10                           jne 0x14024a9e3
0024A9D3  0F B6 43 22                     movzx eax, byte ptr [rbx + 0x22]
0024A9D7  83 E0 10                        and eax, 0x10
0024A9DA  83 C8 20                        or eax, 0x20
0024A9DD  C1 E8 04                        shr eax, 4
0024A9E0  89 47 0C                        mov dword ptr [rdi + 0xc], eax
0024A9E3  3B CD                           cmp ecx, ebp
0024A9E5  48 8B CF                        mov rcx, rdi
0024A9E8  0F 85 45 02 00 00               jne 0x14024ac33
0024A9EE  49 8B D7                        mov rdx, r15
0024A9F1  E8 4A 05 00 00                  call 0x14024af40
0024A9F6  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0024A9FB  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0024AA00  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0024AA05  48 83 C4 20                     add rsp, 0x20
0024AA09  41 5F                           pop r15
0024AA0B  41 5E                           pop r14
0024AA0D  41 5D                           pop r13
0024AA0F  41 5C                           pop r12
0024AA11  5F                              pop rdi
0024AA12  C3                              ret
0024AA13  CC                              int3
0024AA14  3B F5                           cmp esi, ebp
0024AA16  0F 85 EF 00 00 00               jne 0x14024ab0b
0024AA1C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0024AA20  4C 8D 25 D9 E2 BE 00            lea r12, [rip + 0xbee2d9]
0024AA27  48 8B 0D 5A 56 BE 00            mov rcx, qword ptr [rip + 0xbe565a]
0024AA2E  48 8B F5                        mov rsi, rbp
0024AA31  48 C1 E8 2B                     shr rax, 0x2b
0024AA35  25 FF 03 00 00                  and eax, 0x3ff
0024AA3A  48 8B 3C C1                     mov rdi, qword ptr [rcx + rax*8]
0024AA3E  48 83 BF 08 42 00 00 00         cmp qword ptr [rdi + 0x4208], 0
0024AA46  0F 85 1B 03 00 00               jne 0x14024ad67
0024AA4C  49 3B FC                        cmp rdi, r12
0024AA4F  75 43                           jne 0x14024aa94
0024AA51  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0024AA5A  41 0F 0D 88 98 8B 00 00         prefetchw byte ptr [r8 + 0x8b98]
0024AA62  41 8B 90 98 8B 00 00            mov edx, dword ptr [r8 + 0x8b98]
0024AA69  48 8D 04 32                     lea rax, [rdx + rsi]
0024AA6D  48 3D 00 01 00 00               cmp rax, 0x100
0024AA73  77 1F                           ja 0x14024aa94
0024AA75  8D 0C 32                        lea ecx, [rdx + rsi]
0024AA78  8B C2                           mov eax, edx
0024AA7A  F0 41 0F B1 88 98 8B 00 00      lock cmpxchg dword ptr [r8 + 0x8b98], ecx
0024AA83  48 63 C8                        movsxd rcx, eax
0024AA86  48 3B CA                        cmp rcx, rdx
0024AA89  0F 85 5F 02 00 00               jne 0x14024acee
0024AA8F  48 8B D5                        mov rdx, rbp
0024AA92  EB 31                           jmp 0x14024aac5
0024AA94  4C 8B C6                        mov r8, rsi
0024AA97  49 F7 D8                        neg r8
0024AA9A  F0 4C 01 87 80 4B 00 00         lock add qword ptr [rdi + 0x4b80], r8
0024AAA2  F0 4C 0F C1 87 40 4B 00 00      lock xadd qword ptr [rdi + 0x4b40], r8
0024AAAB  49 8B D0                        mov rdx, r8
0024AAAE  48 8B CF                        mov rcx, rdi
0024AAB1  48 2B D6                        sub rdx, rsi
0024AAB4  E8 D7 E5 FF FF                  call 0x140249090
0024AAB9  48 8B D5                        mov rdx, rbp
0024AABC  49 3B FC                        cmp rdi, r12
0024AABF  0F 85 DC 01 00 00               jne 0x14024aca1
0024AAC5  65 4C 8B 0C 25 20 00 00 00      mov r9, qword ptr gs:[0x20]
0024AACE  45 8B 81 9C 8B 00 00            mov r8d, dword ptr [r9 + 0x8b9c]
0024AAD5  41 83 F8 FF                     cmp r8d, -1
0024AAD9  0F 84 C2 01 00 00               je 0x14024aca1
0024AADF  49 63 C8                        movsxd rcx, r8d
0024AAE2  48 FF C1                        inc rcx
0024AAE5  48 81 F9 00 01 00 00            cmp rcx, 0x100
0024AAEC  0F 87 78 01 00 00               ja 0x14024ac6a
0024AAF2  41 8D 48 01                     lea ecx, [r8 + 1]
0024AAF6  41 8B C0                        mov eax, r8d
0024AAF9  F0 41 0F B1 89 9C 8B 00 00      lock cmpxchg dword ptr [r9 + 0x8b9c], ecx
0024AB02  44 8B C0                        mov r8d, eax
0024AB05  0F 85 D5 01 00 00               jne 0x14024ace0
0024AB0B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0024AB15  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0024AB1A  E9 D7 FE FF FF                  jmp 0x14024a9f6
0024AB1F  33 D2                           xor edx, edx
0024AB21  48 8B CF                        mov rcx, rdi
0024AB24  E8 47 37 0F 00                  call 0x14033e270
0024AB29  E9 6E FE FF FF                  jmp 0x14024a99c
0024AB2E  85 F6                           test esi, esi
0024AB30  0F 84 9A 01 00 00               je 0x14024acd0
0024AB36  83 FE 03                        cmp esi, 3
0024AB39  0F 84 C0 00 00 00               je 0x14024abff
0024AB3F  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0024AB42  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0024AB46  C1 E8 10                        shr eax, 0x10
0024AB49  24 F7                           and al, 0xf7
0024AB4B  88 44 24 52                     mov byte ptr [rsp + 0x52], al
0024AB4F  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0024AB53  89 43 20                        mov dword ptr [rbx + 0x20], eax
0024AB56  49 8B 45 00                     mov rax, qword ptr [r13]
0024AB5A  A8 42                           test al, 0x42
0024AB5C  74 2B                           je 0x14024ab89
0024AB5E  44 8B 63 20                     mov r12d, dword ptr [rbx + 0x20]
0024AB62  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0024AB67  41 C1 EC 10                     shr r12d, 0x10
0024AB6B  45 0F B6 DC                     movzx r11d, r12b
0024AB6F  41 F6 C4 08                     test r12b, 8
0024AB73  0F 85 B4 01 00 00               jne 0x14024ad2d
0024AB79  41 80 CB 10                     or r11b, 0x10
0024AB7D  44 88 5C 24 52                  mov byte ptr [rsp + 0x52], r11b
0024AB82  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0024AB86  89 43 20                        mov dword ptr [rbx + 0x20], eax
0024AB89  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0024AB8C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0024AB90  66 2B C5                        sub ax, bp
0024AB93  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
0024AB98  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0024AB9C  89 43 20                        mov dword ptr [rbx + 0x20], eax
0024AB9F  0F 85 6F FE FF FF               jne 0x14024aa14
0024ABA5  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0024ABA9  48 0F BA E0 3E                  bt rax, 0x3e
0024ABAE  0F 82 12 01 00 00               jb 0x14024acc6
0024ABB4  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0024ABB7  C1 E8 18                        shr eax, 0x18
0024ABBA  A8 40                           test al, 0x40
0024ABBC  0F 85 04 01 00 00               jne 0x14024acc6
0024ABC2  F6 43 23 10                     test byte ptr [rbx + 0x23], 0x10
0024ABC6  0F 85 FA 00 00 00               jne 0x14024acc6
0024ABCC  80 3D 13 20 BF 00 00            cmp byte ptr [rip + 0xbf2013], 0
0024ABD3  74 2A                           je 0x14024abff
0024ABD5  49 C1 FE 04                     sar r14, 4
0024ABD9  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0024ABE3  4C 0F AF F0                     imul r14, rax
0024ABE7  48 8B 05 52 26 BF 00            mov rax, qword ptr [rip + 0xbf2652]
0024ABEE  49 C1 EE 09                     shr r14, 9
0024ABF2  42 0F B6 0C 70                  movzx ecx, byte ptr [rax + r14*2]
0024ABF7  84 C9                           test cl, cl
0024ABF9  0F 85 BE 00 00 00               jne 0x14024acbd
0024ABFF  8B CD                           mov ecx, ebp
0024AC01  E9 C7 FD FF FF                  jmp 0x14024a9cd
0024AC06  45 33 E4                        xor r12d, r12d
0024AC09  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
0024AC10  0F 83 9D FD FF FF               jae 0x14024a9b3
0024AC16  41 FF C4                        inc r12d
0024AC19  44 85 25 8C A6 D7 00            test dword ptr [rip + 0xd7a68c], r12d
0024AC20  0F 84 D0 00 00 00               je 0x14024acf6
0024AC26  F3 90                           pause
0024AC28  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0024AC2C  48 85 C0                        test rax, rax
0024AC2F  79 D8                           jns 0x14024ac09
0024AC31  EB E3                           jmp 0x14024ac16
0024AC33  8B D5                           mov edx, ebp
0024AC35  E8 36 36 0F 00                  call 0x14033e270
0024AC3A  85 F6                           test esi, esi
0024AC3C  0F 84 DC 00 00 00               je 0x14024ad1e
0024AC42  83 FE 02                        cmp esi, 2
0024AC45  0F 85 6A 01 00 00               jne 0x14024adb5
0024AC4B  48 8B D3                        mov rdx, rbx
0024AC4E  49 8B CD                        mov rcx, r13
0024AC51  E8 D2 AA 06 00                  call 0x1402b5728
0024AC56  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0024AC60  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0024AC65  E9 8C FD FF FF                  jmp 0x14024a9f6
0024AC6A  B9 C0 00 00 00                  mov ecx, 0xc0
0024AC6F  44 3B C1                        cmp r8d, ecx
0024AC72  7E 21                           jle 0x14024ac95
0024AC74  41 83 F8 FF                     cmp r8d, -1
0024AC78  74 1B                           je 0x14024ac95
0024AC7A  41 8B C0                        mov eax, r8d
0024AC7D  F0 41 0F B1 89 9C 8B 00 00      lock cmpxchg dword ptr [r9 + 0x8b9c], ecx
0024AC86  75 0D                           jne 0x14024ac95
0024AC88  41 8D 80 40 FF FF FF            lea eax, [r8 - 0xc0]
0024AC8F  48 63 D0                        movsxd rdx, eax
0024AC92  48 FF C2                        inc rdx
0024AC95  48 8B EA                        mov rbp, rdx
0024AC98  48 85 D2                        test rdx, rdx
0024AC9B  0F 84 6A FE FF FF               je 0x14024ab0b
0024ACA1  F0 48 01 AF 40 49 00 00         lock add qword ptr [rdi + 0x4940], rbp
0024ACA9  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0024ACB3  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0024ACB8  E9 39 FD FF FF                  jmp 0x14024a9f6
0024ACBD  80 F9 0A                        cmp cl, 0xa
0024ACC0  0F 84 39 FF FF FF               je 0x14024abff
0024ACC6  B9 02 00 00 00                  mov ecx, 2
0024ACCB  E9 FD FC FF FF                  jmp 0x14024a9cd
0024ACD0  48 8B D3                        mov rdx, rbx
0024ACD3  49 8B CD                        mov rcx, r13
0024ACD6  E8 A5 39 1B 00                  call 0x1403fe680
0024ACDB  E9 E7 FC FF FF                  jmp 0x14024a9c7
0024ACE0  83 F8 FF                        cmp eax, -1
0024ACE3  0F 85 F6 FD FF FF               jne 0x14024aadf
0024ACE9  E9 7C FF FF FF                  jmp 0x14024ac6a
0024ACEE  48 8B D1                        mov rdx, rcx
0024ACF1  E9 73 FD FF FF                  jmp 0x14024aa69
0024ACF6  8B 05 BC BD D7 00               mov eax, dword ptr [rip + 0xd7bdbc]
0024ACFC  A8 40                           test al, 0x40
0024ACFE  0F 84 22 FF FF FF               je 0x14024ac26
0024AD04  E8 87 47 0C 00                  call 0x14030f490
0024AD09  84 C0                           test al, al
0024AD0B  0F 84 15 FF FF FF               je 0x14024ac26
0024AD11  41 8B CC                        mov ecx, r12d
0024AD14  E8 47 47 0C 00                  call 0x14030f460
0024AD19  E9 0A FF FF FF                  jmp 0x14024ac28
0024AD1E  33 D2                           xor edx, edx
0024AD20  48 8B CB                        mov rcx, rbx
0024AD23  E8 48 92 0E 00                  call 0x140333f70
0024AD28  E9 DE FD FF FF                  jmp 0x14024ab0b
0024AD2D  48 8B CB                        mov rcx, rbx
0024AD30  E8 07 90 12 00                  call 0x140373d3c
0024AD35  85 C0                           test eax, eax
0024AD37  0F 84 3C FE FF FF               je 0x14024ab79
0024AD3D  F6 43 22 10                     test byte ptr [rbx + 0x22], 0x10
0024AD41  0F 85 32 FE FF FF               jne 0x14024ab79
0024AD47  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0024AD4A  C0 E8 02                        shr al, 2
0024AD4D  40 84 C5                        test bpl, al
0024AD50  0F 84 23 FE FF FF               je 0x14024ab79
0024AD56  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0024AD5A  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0024AD5E  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0024AD62  E9 12 FE FF FF                  jmp 0x14024ab79
0024AD67  44 0F 20 C0                     mov rax, cr8
0024AD6B  48 8D 8F F8 41 00 00            lea rcx, [rdi + 0x41f8]
0024AD72  3C 02                           cmp al, 2
0024AD74  74 35                           je 0x14024adab
0024AD76  E8 15 D9 FF FF                  call 0x140248690
0024AD7B  44 0F B6 F8                     movzx r15d, al
0024AD7F  48 8B D5                        mov rdx, rbp
0024AD82  48 8B CF                        mov rcx, rdi
0024AD85  E8 0A D0 1B 00                  call 0x140407d94
0024AD8A  41 0F B6 D7                     movzx edx, r15b
0024AD8E  48 8D 8F F8 41 00 00            lea rcx, [rdi + 0x41f8]
0024AD95  48 8B F0                        mov rsi, rax
0024AD98  E8 23 D5 FF FF                  call 0x1402482c0
0024AD9D  48 85 F6                        test rsi, rsi
0024ADA0  0F 84 13 FD FF FF               je 0x14024aab9
0024ADA6  E9 A1 FC FF FF                  jmp 0x14024aa4c
0024ADAB  41 B7 11                        mov r15b, 0x11
0024ADAE  E8 CD E0 FF FF                  call 0x140248e80
0024ADB3  EB CA                           jmp 0x14024ad7f
0024ADB5  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0024ADB9  44 8B C5                        mov r8d, ebp
0024ADBC  48 8B 05 C5 52 BE 00            mov rax, qword ptr [rip + 0xbe52c5]
0024ADC3  48 8B D5                        mov rdx, rbp
0024ADC6  48 C1 E9 2B                     shr rcx, 0x2b
0024ADCA  81 E1 FF 03 00 00               and ecx, 0x3ff
0024ADD0  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0024ADD4  E8 73 CD 1B 00                  call 0x140407b4c
0024ADD9  49 8B D7                        mov rdx, r15
0024ADDC  48 8B CB                        mov rcx, rbx
0024ADDF  E8 5C F0 06 00                  call 0x1402b9e40
0024ADE4  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0024ADEE  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0024ADF3  E9 FE FB FF FF                  jmp 0x14024a9f6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddPageToInsertList(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p50;
    unsigned __int8 v_stack_p52;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r14 = (a3 + a3 * 2) << (4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)))) == 3) goto loc_0024ABFF;
loc_0024A99C:
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_0024AC06;
    if ((*(unsigned __int64 *)(a1)) < 0) goto loc_0024AB1F;
loc_0024A9B3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)))) != 2) goto loc_0024AB2E;
    result = MiCanBatchHardFaultPages(a2, v_r14 + result * 1, a3, a4);
loc_0024A9C7:
    if ((unsigned int)(result) == 0) goto loc_0024AA14;
loc_0024A9CD:
    if ((*(unsigned __int64 *)(a1)) == 0) {
        result = *(unsigned __int8 *)(v_r14 + result * 1 + 34);
        result = (unsigned int)((result) & (16));
        result = (unsigned int)((result) | (32));
        result = (unsigned int)((result) >> (4));
        *(unsigned int *)(a1 + 12) = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 1) goto loc_0024AC33;
    result = MiEnqueuePageList(a1, a3, a3, a4);
loc_0024A9F6:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0024AA14:
    if (((unsigned int)(v_stack_p20)) != ((unsigned int)(v_stack_p18))) goto loc_0024AB0B;
    result = (*(unsigned __int64 *)(v_stack_p10 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8) + 16904)) != 0) goto loc_0024AD67;
loc_0024AA4C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8)) != (v_rip + 12509913)) goto loc_0024AA94;
loc_0024AA69:
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736)) + v_stack_p18 * 1) > 256) goto loc_0024AA94;
    if (((int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736))))))) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736)))) goto loc_0024ACEE;
    goto loc_0024AAC5;
loc_0024AA94:
    a3 = -(v_stack_p18);
    a2 = (a3) - (v_stack_p18);
    result = MiSignalCommitSignals(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8), a2, a3, a4);
loc_0024AAB9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8)) != (v_rip + 12509913)) goto loc_0024ACA1;
loc_0024AAC5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))) == -1) goto loc_0024ACA1;
loc_0024AADF:
    a1 = ((int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740))))) + 1;
    if (a1 > 256) goto loc_0024AC6A;
    if (a1 != 256) goto loc_0024ACE0;
loc_0024AB0B:
    goto loc_0024A9F6;
loc_0024AB1F:
    a2 = 0;
    result = MiInsertPagesInList(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024A99C;
loc_0024AB2E:
    if ((unsigned int)(v_stack_p18) == 0) goto loc_0024ACD0;
    if (((unsigned int)(v_stack_p18)) == 3) goto loc_0024ABFF;
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 32))) >> (16));
    result = (unsigned __int8)((result) & (247));
    v_stack_p52 = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_p10 + 32) = (unsigned int)((unsigned int)(v_stack_p50));
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (66)) == 0) goto loc_0024AB89;
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 32))) >> (16));
    if ((((unsigned __int8)(v_r12)) & (8)) != 0) goto loc_0024AD2D;
loc_0024AB79:
    v_r11 = (unsigned __int8)(((unsigned __int8)(v_r12)) | (16));
    v_stack_p52 = (unsigned __int8)(v_r11);
    *(unsigned int *)(v_stack_p10 + 32) = (unsigned int)((unsigned int)(v_stack_p50));
loc_0024AB89:
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 32))) - ((unsigned __int16)(v_stack_p18)));
    v_stack_p50 = (unsigned __int16)(result);
    *(unsigned int *)(v_stack_p10 + 32) = (unsigned int)((unsigned int)(v_stack_p50));
    if (condition_is_not_equal) goto loc_0024AA14;
    if (condition_is_below) goto loc_0024ACC6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_0024ACC6;
    if (((*(unsigned __int8 *)(v_stack_p10 + 35)) & (16)) != 0) goto loc_0024ACC6;
    if ((*(unsigned __int8 *)(v_rip + 12525587)) == 0) goto loc_0024ABFF;
    v_r14 = (v_r14) >> (4);
    v_r14 = (v_r14) * (result);
    v_r14 = (v_r14) >> (9);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12527186) + v_r14 * 2)) != 0) goto loc_0024ACBD;
loc_0024ABFF:
    goto loc_0024A9CD;
loc_0024AC06:
    v_r12 = 0;
loc_0024AC09:
    if (condition_is_above_or_equal) goto loc_0024A9B3;
loc_0024AC16:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 14132876)) & ((unsigned int)(v_r12))) == 0) goto loc_0024ACF6;
loc_0024AC26:
loc_0024AC28:
    if (!sign_flag) goto loc_0024AC09;
    goto loc_0024AC16;
loc_0024AC33:
    result = MiInsertPagesInList((unsigned int)((unsigned int)(v_stack_p18)), (unsigned int)((unsigned int)(v_stack_p18)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    if ((unsigned int)(v_stack_p18) == 0) goto loc_0024AD1E;
    if (((unsigned int)(v_stack_p18)) != 2) goto loc_0024ADB5;
    result = MiHardFaultPageRelease(0, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024A9F6;
loc_0024AC6A:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))))) <= 192) goto loc_0024AC95;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))))) == -1) goto loc_0024AC95;
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740))))))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))))) == -1) {
        result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))) - 192;
        a2 = (int)((unsigned int)(result));
        a2 = (a2) + 1;
    }
    if (a2 == 0) goto loc_0024AB0B;
loc_0024ACA1:
    goto loc_0024A9F6;
loc_0024ACBD:
    if (192 == 10) goto loc_0024ABFF;
loc_0024ACC6:
    goto loc_0024A9CD;
loc_0024ACD0:
    result = MiCanBatchSystemCacheUnmapPages(a2, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024A9C7;
loc_0024ACE0:
    if (((unsigned int)(result)) != -1) goto loc_0024AADF;
    goto loc_0024AC6A;
loc_0024ACEE:
    goto loc_0024AA69;
loc_0024ACF6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14138812)))) & (64)) == 0) goto loc_0024AC26;
    result = KiCheckVpBackingLongSpinWaitHypercall(a2, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    if ((unsigned __int8)(result) == 0) goto loc_0024AC26;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024AC28;
loc_0024AD1E:
    a2 = 0;
    result = MiDecrementShareCountEx(v_stack_p10, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024AB0B;
loc_0024AD2D:
    result = MiCanPfnOriginalPteBeLost(v_stack_p10, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    if ((unsigned int)(result) == 0) goto loc_0024AB79;
    if (((*(unsigned __int8 *)(v_stack_p10 + 34)) & (16)) != 0) goto loc_0024AB79;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 16))) >> (2));
    if (((0) & ((unsigned __int8)(result))) == 0) goto loc_0024AB79;
    result = (*(unsigned __int64 *)(v_stack_p10 + 16)) & (-5);
    *(unsigned __int64 *)(v_stack_p10 + 16) = result;
    goto loc_0024AB79;
loc_0024AD67:
    if (((unsigned __int8)(v_cr8)) == 2) goto loc_0024ADAB;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8) + 16888, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
loc_0024AD7F:
    result = MiRestockOverCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8), 0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8) + 16888, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    if (result == 0) goto loc_0024AAB9;
    goto loc_0024AA4C;
loc_0024ADAB:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473946) + result * 8) + 16888, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)))))), *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024AD7F;
loc_0024ADB5:
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = MiReleaseWriteInProgressCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12473029) + a1 * 8), 0, 0, *(unsigned __int64 *)(gs_base + (0 + 32)));
    result = MiPfnReferenceCountIsZero(v_stack_p10, 17, 0, *(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0024A9F6;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddPageToInsertList(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p50;
    uint8_t v_stack_p52;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r14 = (Arg3 + Arg3 * 2) << (4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)))) == 3) goto loc_0024ABFF;
loc_0024A99C:
    if ((*(uint64_t *)(arg1)) == 0) goto loc_0024AC06;
    if ((*(uint64_t *)(arg1)) < 0) goto loc_0024AB1F;
loc_0024A9B3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)))) != 2) goto loc_0024AB2E;
    result = MiCanBatchHardFaultPages(Arg2, local_r14 + result * 1, Arg3, a4);
loc_0024A9C7:
    if ((uint32_t)(result) == 0) goto loc_0024AA14;
loc_0024A9CD:
    if ((*(uint64_t *)(arg1)) == 0) {
        result = *(uint8_t *)(local_r14 + result * 1 + 0x22);
        result = (uint32_t)((result) & (16));
        result = (uint32_t)((result) | (32));
        result = (uint32_t)((result) >> (4));
        *(uint32_t *)(arg1 + 0xC) = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 1) goto loc_0024AC33;
    result = MiEnqueuePageList(Arg1, Arg3, Arg3, a4);
loc_0024A9F6:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0024AA14:
    if (((uint32_t)(v_stack_p20)) != ((uint32_t)(v_stack_p18))) goto loc_0024AB0B;
    result = (*(uint64_t *)(v_stack_p10 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8) + 0x4208)) != 0) goto loc_0024AD67;
loc_0024AA4C:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8)) != (v_rip + 12509913)) goto loc_0024AA94;
loc_0024AA69:
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98)) + v_stack_p18 * 1) > 256) goto loc_0024AA94;
    if (((int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98))))))) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98)))) goto loc_0024ACEE;
    goto loc_0024AAC5;
loc_0024AA94:
    Arg3 = -(v_stack_p18);
    Arg2 = (Arg3) - (v_stack_p18);
    result = MiSignalCommitSignals(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8), Arg2, Arg3, a4);
loc_0024AAB9:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8)) != (v_rip + 12509913)) goto loc_0024ACA1;
loc_0024AAC5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))) == -1) goto loc_0024ACA1;
loc_0024AADF:
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C))))) + 1;
    if (Arg1 > 256) goto loc_0024AC6A;
    if (Arg1 != 256) goto loc_0024ACE0;
loc_0024AB0B:
    goto loc_0024A9F6;
loc_0024AB1F:
    Arg2 = 0;
    result = MiInsertPagesInList(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024A99C;
loc_0024AB2E:
    if ((uint32_t)(v_stack_p18) == 0) goto loc_0024ACD0;
    if (((uint32_t)(v_stack_p18)) == 3) goto loc_0024ABFF;
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20))) >> (16));
    result = (uint8_t)((result) & (247));
    v_stack_p52 = (uint8_t)(result);
    *(uint32_t *)(v_stack_p10 + 0x20) = (uint32_t)((uint32_t)(v_stack_p50));
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (66)) == 0) goto loc_0024AB89;
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20))) >> (16));
    if ((((uint8_t)(local_r12)) & (8)) != 0) goto loc_0024AD2D;
loc_0024AB79:
    local_r11 = (uint8_t)(((uint8_t)(local_r12)) | (16));
    v_stack_p52 = (uint8_t)(local_r11);
    *(uint32_t *)(v_stack_p10 + 0x20) = (uint32_t)((uint32_t)(v_stack_p50));
loc_0024AB89:
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20))) - ((uint16_t)(v_stack_p18)));
    v_stack_p50 = (uint16_t)(result);
    *(uint32_t *)(v_stack_p10 + 0x20) = (uint32_t)((uint32_t)(v_stack_p50));
    if (condition_is_not_equal) goto loc_0024AA14;
    if (condition_is_below) goto loc_0024ACC6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_0024ACC6;
    if (((*(uint8_t *)(v_stack_p10 + 0x23)) & (16)) != 0) goto loc_0024ACC6;
    if ((*(uint8_t *)(v_rip + 0xBF2013)) == 0) goto loc_0024ABFF;
    local_r14 = (local_r14) >> (4);
    local_r14 = (local_r14) * (result);
    local_r14 = (local_r14) >> (9);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xBF2652) + local_r14 * 2)) != 0) goto loc_0024ACBD;
loc_0024ABFF:
    goto loc_0024A9CD;
loc_0024AC06:
    local_r12 = 0;
loc_0024AC09:
    if (condition_is_above_or_equal) goto loc_0024A9B3;
loc_0024AC16:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD7A68C)) & ((uint32_t)(local_r12))) == 0) goto loc_0024ACF6;
loc_0024AC26:
loc_0024AC28:
    if (!sign_flag) goto loc_0024AC09;
    goto loc_0024AC16;
loc_0024AC33:
    result = MiInsertPagesInList((uint32_t)((uint32_t)(v_stack_p18)), (uint32_t)((uint32_t)(v_stack_p18)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    if ((uint32_t)(v_stack_p18) == 0) goto loc_0024AD1E;
    if (((uint32_t)(v_stack_p18)) != 2) goto loc_0024ADB5;
    result = MiHardFaultPageRelease(0, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024A9F6;
loc_0024AC6A:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))))) <= 192) goto loc_0024AC95;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))))) == -1) goto loc_0024AC95;
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C))))))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))))) == -1) {
        result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))) - 192;
        Arg2 = (int32_t)((uint32_t)(result));
        Arg2 = (Arg2) + 1;
    }
    if (Arg2 == NULL) goto loc_0024AB0B;
loc_0024ACA1:
    goto loc_0024A9F6;
loc_0024ACBD:
    if (192 == 10) goto loc_0024ABFF;
loc_0024ACC6:
    goto loc_0024A9CD;
loc_0024ACD0:
    result = MiCanBatchSystemCacheUnmapPages(Arg2, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024A9C7;
loc_0024ACE0:
    if (((uint32_t)(result)) != -1) goto loc_0024AADF;
    goto loc_0024AC6A;
loc_0024ACEE:
    goto loc_0024AA69;
loc_0024ACF6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD7BDBC)))) & (64)) == 0) goto loc_0024AC26;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg2, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    if ((uint8_t)(result) == 0) goto loc_0024AC26;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024AC28;
loc_0024AD1E:
    Arg2 = 0;
    result = MiDecrementShareCountEx(v_stack_p10, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024AB0B;
loc_0024AD2D:
    result = MiCanPfnOriginalPteBeLost(v_stack_p10, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    if ((uint32_t)(result) == 0) goto loc_0024AB79;
    if (((*(uint8_t *)(v_stack_p10 + 0x22)) & (16)) != 0) goto loc_0024AB79;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10))) >> (2));
    if (((0) & ((uint8_t)(result))) == 0) goto loc_0024AB79;
    result = (*(uint64_t *)(v_stack_p10 + 0x10)) & (-5);
    *(uint64_t *)(v_stack_p10 + 0x10) = result;
    goto loc_0024AB79;
loc_0024AD67:
    if (((uint8_t)(v_cr8)) == 2) goto loc_0024ADAB;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8) + 16888, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
loc_0024AD7F:
    result = MiRestockOverCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8), 0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8) + 16888, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    if (result == 0) goto loc_0024AAB9;
    goto loc_0024AA4C;
loc_0024ADAB:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE565A) + result * 8) + 16888, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)))))), *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024AD7F;
loc_0024ADB5:
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = MiReleaseWriteInProgressCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE52C5) + arg1 * 8), 0, 0, *(uint64_t *)(gs_base + (0 + 0x20)));
    result = MiPfnReferenceCountIsZero(v_stack_p10, 17, 0, *(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0024A9F6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0 + r8*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024A950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
