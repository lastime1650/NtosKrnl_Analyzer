# MiUpdateLargePageBitMap

- RVA: `0x0037619C`–`0x003765D8` (길이 `1,084` bytes)
- VA: `0x000000014037619C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007AC04`
- 디코드: `300`개 명령, `1,084/1,084` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003762A9` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00376336` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0037634D` → [RtlSetBitsEx](../3B/RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)
- `0x00376435` → [RtlClearBitsEx](../29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)
- `0x00376466` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)

### Direct callers
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028CA0B`
- [MiLinkPoolCommitChain](../31/MiLinkPoolCommitChain_function_00313D20.md) at `0x00313FDE`
- [MiFreeMdlPageRun](MiFreeMdlPageRun_function_00375A4C.md) at `0x00375B96`
- [MiFreeLargePageMemory](MiFreeLargePageMemory_function_00377938.md) at `0x003779DF`
- [MiGetFastLargePages](../3B/MiGetFastLargePages_function_003B7EE0.md) at `0x003B8215`
- [MiRebuildLargePage](../3B/MiRebuildLargePage_function_003BBAEC.md) at `0x003BBF10`
- [MiFreeContiguousPages](../3F/MiFreeContiguousPages_function_003F7178.md) at `0x003F7324`
- [MiDemoteSlabEntry](../44/MiDemoteSlabEntry_function_0044CB0C.md) at `0x0044CBB5`
- [MiDeleteSubsectionLargePages](../4D/MiDeleteSubsectionLargePages_function_004D51E0.md) at `0x004D52D4`
- [MiFindLargeNodePage](../4D/MiFindLargeNodePage_function_004DB7E8.md) at `0x004DB936`
- [MiInitializeDynamicPfns](../67/MiInitializeDynamicPfns_function_00672BD0.md) at `0x00672ED3`
- [MiFreeContiguousLargePageRun](../68/MiFreeContiguousLargePageRun_function_00688A34.md) at `0x00688BA9`
- [MiDemoteValidLargePageOneLevel](../68/MiDemoteValidLargePageOneLevel_function_0068A3F4.md) at `0x0068A920`
- [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) at `0x0068FB42`
- [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) at `0x0068FBAC`
- [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) at `0x0068FBFF`
- [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) at `0x00690022`
- [MiDemotePfnListChain](../69/MiDemotePfnListChain_function_00698B5C.md) at `0x00698C26`
- [sub_006E7436](../6E/Unknown_function_006E7436.md) at `0x006E746F`
- [MiCompleteMemoryAddition](../../page/7F/MiCompleteMemoryAddition_function_007F9FAC.md) at `0x007FA033`
- [MiCompleteMemoryAddition](../../page/7F/MiCompleteMemoryAddition_function_007F9FAC.md) at `0x007FA057`
- [MiFreeBootPageTable](../../init/C5/MiFreeBootPageTable_function_00C5FC10.md) at `0x00C5FC7C`
- [MiMarkLargePagePte](../../init/C6/MiMarkLargePagePte_function_00C60C70.md) at `0x00C60CE8`
- [MiMarkLargePageRanges](../../init/C6/MiMarkLargePageRanges_function_00C60CFC.md) at `0x00C60E81`
- [MiMarkLargePageRanges](../../init/C6/MiMarkLargePageRanges_function_00C60CFC.md) at `0x00C60EFC`
- [MiCreateEnclaveRegions](../../init/C6/MiCreateEnclaveRegions_function_00C68AD4.md) at `0x00C68BE9`
- [MiCreateBootSlabEntries](../../init/C6/MiCreateBootSlabEntries_function_00C69A50.md) at `0x00C69C03`

### Static image references
- `0x003761EC` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003762A2` → RVA `0x00E2EEC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003763EA` → [sub_006E3EEA](../6E/Unknown_function_006E3EEA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0037619C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003761A1  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003761A6  55                              push rbp
003761A7  56                              push rsi
003761A8  57                              push rdi
003761A9  41 54                           push r12
003761AB  41 55                           push r13
003761AD  41 56                           push r14
003761AF  41 57                           push r15
003761B1  48 83 EC 20                     sub rsp, 0x20
003761B5  4D 8B D8                        mov r11, r8
003761B8  45 8B F1                        mov r14d, r9d
003761BB  41 8B C1                        mov eax, r9d
003761BE  41 BF 02 00 00 00               mov r15d, 2
003761C4  41 83 E6 01                     and r14d, 1
003761C8  41 23 C7                        and eax, r15d
003761CB  4C 8B C2                        mov r8, rdx
003761CE  45 8B E9                        mov r13d, r9d
003761D1  48 8B D1                        mov rdx, rcx
003761D4  49 81 FB 00 02 00 00            cmp r11, 0x200
003761DB  0F 82 CD 00 00 00               jb 0x1403762ae
003761E1  45 33 C9                        xor r9d, r9d
003761E4  C6 44 24 78 11                  mov byte ptr [rsp + 0x78], 0x11
003761E9  45 33 E4                        xor r12d, r12d
003761EC  4C 8D 15 0D 9E C8 FF            lea r10, [rip - 0x3761f3]
003761F3  85 C0                           test eax, eax
003761F5  41 0F 95 C1                     setne r9b
003761F9  41 FF CF                        dec r15d
003761FC  48 8D B2 C8 3F 00 00            lea rsi, [rdx + 0x3fc8]
00376203  41 8B C7                        mov eax, r15d
00376206  48 C1 E0 04                     shl rax, 4
0037620A  48 03 F0                        add rsi, rax
0037620D  48 83 3E 00                     cmp qword ptr [rsi], 0
00376211  0F 84 82 00 00 00               je 0x140376299
00376217  43 8B 8C BA E8 35 01 00         mov ecx, dword ptr [r10 + r15*4 + 0x135e8]
0037621F  49 8B D8                        mov rbx, r8
00376222  4B 8B 94 FA 60 1C 01 00         mov rdx, qword ptr [r10 + r15*8 + 0x11c60]
0037622A  48 D3 EB                        shr rbx, cl
0037622D  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
00376231  48 8D 6A FF                     lea rbp, [rdx - 1]
00376235  49 03 E8                        add rbp, r8
00376238  48 8D 42 FF                     lea rax, [rdx - 1]
0037623C  49 03 EB                        add rbp, r11
0037623F  48 F7 D0                        not rax
00376242  48 23 E8                        and rbp, rax
00376245  48 D3 ED                        shr rbp, cl
00376248  48 8B FD                        mov rdi, rbp
0037624B  48 2B FB                        sub rdi, rbx
0037624E  45 85 C9                        test r9d, r9d
00376251  0F 85 C3 00 00 00               jne 0x14037631a
00376257  48 8B 06                        mov rax, qword ptr [rsi]
0037625A  45 85 F6                        test r14d, r14d
0037625D  0F 85 AC 02 00 00               jne 0x14037650f
00376263  48 3B D8                        cmp rbx, rax
00376266  0F 83 4A 03 00 00               jae 0x1403765b6
0037626C  48 83 FF 01                     cmp rdi, 1
00376270  77 52                           ja 0x1403762c4
00376272  0F 85 3E 03 00 00               jne 0x1403765b6
00376278  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0037627C  48 8B D3                        mov rdx, rbx
0037627F  48 8B C3                        mov rax, rbx
00376282  83 E2 3F                        and edx, 0x3f
00376285  48 C1 E8 06                     shr rax, 6
00376289  48 0F A3 14 C1                  bt qword ptr [rcx + rax*8], rdx
0037628E  0F 93 C0                        setae al
00376291  84 C0                           test al, al
00376293  0F 84 81 00 00 00               je 0x14037631a
00376299  45 85 E4                        test r12d, r12d
0037629C  74 10                           je 0x1403762ae
0037629E  8A 54 24 78                     mov dl, byte ptr [rsp + 0x78]
003762A2  48 8D 0D 17 8C AB 00            lea rcx, [rip + 0xab8c17]
003762A9  E8 12 20 ED FF                  call 0x1402482c0
003762AE  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
003762B3  48 83 C4 20                     add rsp, 0x20
003762B7  41 5F                           pop r15
003762B9  41 5E                           pop r14
003762BB  41 5D                           pop r13
003762BD  41 5C                           pop r12
003762BF  5F                              pop rdi
003762C0  5E                              pop rsi
003762C1  5D                              pop rbp
003762C2  C3                              ret
003762C3  CC                              int3
003762C4  48 2B C3                        sub rax, rbx
003762C7  48 3B C7                        cmp rax, rdi
003762CA  0F 82 E6 02 00 00               jb 0x1403765b6
003762D0  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
003762D4  4C 8D 55 FF                     lea r10, [rbp - 1]
003762D8  48 8B C3                        mov rax, rbx
003762DB  48 C1 E8 06                     shr rax, 6
003762DF  48 8D 14 C1                     lea rdx, [rcx + rax*8]
003762E3  49 8B C2                        mov rax, r10
003762E6  4C 8B 02                        mov r8, qword ptr [rdx]
003762E9  48 C1 E8 06                     shr rax, 6
003762ED  4C 8D 0C C1                     lea r9, [rcx + rax*8]
003762F1  49 3B D1                        cmp rdx, r9
003762F4  0F 85 45 01 00 00               jne 0x14037643f
003762FA  B9 40 00 00 00                  mov ecx, 0x40
003762FF  48 83 C8 FF                     or rax, 0xffffffffffffffff
00376303  40 2A CF                        sub cl, dil
00376306  48 D3 E8                        shr rax, cl
00376309  48 8B CB                        mov rcx, rbx
0037630C  48 D3 E0                        shl rax, cl
0037630F  4C 85 C0                        test rax, r8
00376312  0F 94 C0                        sete al
00376315  E9 77 FF FF FF                  jmp 0x140376291
0037631A  45 85 E4                        test r12d, r12d
0037631D  75 1C                           jne 0x14037633b
0037631F  48 8D 0D 9A 8B AB 00            lea rcx, [rip + 0xab8b9a]
00376326  41 BC 01 00 00 00               mov r12d, 1
0037632C  41 F6 C5 04                     test r13b, 4
00376330  0F 84 30 01 00 00               je 0x140376466
00376336  E8 45 2B ED FF                  call 0x140248e80
0037633B  4C 8B C7                        mov r8, rdi
0037633E  48 8B D3                        mov rdx, rbx
00376341  48 8B CE                        mov rcx, rsi
00376344  45 85 F6                        test r14d, r14d
00376347  0F 84 E8 00 00 00               je 0x140376435
0037634D  E8 1E 02 04 00                  call 0x1403b6570
00376352  45 85 FF                        test r15d, r15d
00376355  0F 84 3E FF FF FF               je 0x140376299
0037635B  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0037635F  41 8D 47 FF                     lea eax, [r15 - 1]
00376363  48 FF CD                        dec rbp
00376366  4C 8D 15 93 9C C8 FF            lea r10, [rip - 0x37636d]
0037636D  4D 8B 84 C2 60 1C 01 00         mov r8, qword ptr [r10 + rax*8 + 0x11c60]
00376375  49 D3 E8                        shr r8, cl
00376378  49 03 E8                        add rbp, r8
0037637B  49 8D 40 FF                     lea rax, [r8 - 1]
0037637F  48 F7 D0                        not rax
00376382  48 23 E8                        and rbp, rax
00376385  48 23 D8                        and rbx, rax
00376388  4C 8B DD                        mov r11, rbp
0037638B  4C 2B DB                        sub r11, rbx
0037638E  45 85 F6                        test r14d, r14d
00376391  0F 84 84 00 00 00               je 0x14037641b
00376397  48 8B 06                        mov rax, qword ptr [rsi]
0037639A  48 3B D8                        cmp rbx, rax
0037639D  73 29                           jae 0x1403763c8
0037639F  49 83 F8 01                     cmp r8, 1
003763A3  0F 87 CB 00 00 00               ja 0x140376474
003763A9  75 1D                           jne 0x1403763c8
003763AB  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003763AF  48 8B D3                        mov rdx, rbx
003763B2  83 E2 3F                        and edx, 0x3f
003763B5  48 8B CB                        mov rcx, rbx
003763B8  48 C1 E9 06                     shr rcx, 6
003763BC  48 0F A3 14 C8                  bt qword ptr [rax + rcx*8], rdx
003763C1  0F 92 C0                        setb al
003763C4  84 C0                           test al, al
003763C6  75 0C                           jne 0x1403763d4
003763C8  4D 2B D8                        sub r11, r8
003763CB  0F 84 C8 FE FF FF               je 0x140376299
003763D1  49 03 D8                        add rbx, r8
003763D4  48 8B 06                        mov rax, qword ptr [rsi]
003763D7  4C 8B CD                        mov r9, rbp
003763DA  4D 2B C8                        sub r9, r8
003763DD  4C 3B C8                        cmp r9, rax
003763E0  0F 83 E4 01 00 00               jae 0x1403765ca
003763E6  49 83 F8 01                     cmp r8, 1
003763EA  0F 87 FA DA 36 00               ja 0x1406e3eea
003763F0  0F 85 D4 01 00 00               jne 0x1403765ca
003763F6  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003763FA  49 8B C9                        mov rcx, r9
003763FD  49 C1 E9 06                     shr r9, 6
00376401  83 E1 3F                        and ecx, 0x3f
00376404  4A 0F A3 0C C8                  bt qword ptr [rax + r9*8], rcx
00376409  0F 92 C0                        setb al
0037640C  84 C0                           test al, al
0037640E  0F 84 B6 01 00 00               je 0x1403765ca
00376414  4C 8D 15 E5 9B C8 FF            lea r10, [rip - 0x37641b]
0037641B  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0037641F  4C 8B C3                        mov r8, rbx
00376422  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00376427  45 8B CE                        mov r9d, r14d
0037642A  49 D3 E0                        shl r8, cl
0037642D  49 D3 E3                        shl r11, cl
00376430  E9 C4 FD FF FF                  jmp 0x1403761f9
00376435  E8 06 13 F2 FF                  call 0x140297740
0037643A  E9 13 FF FF FF                  jmp 0x140376352
0037643F  49 83 CB FF                     or r11, 0xffffffffffffffff
00376443  48 8B CB                        mov rcx, rbx
00376446  49 8B C3                        mov rax, r11
00376449  48 D3 E0                        shl rax, cl
0037644C  4C 85 C0                        test rax, r8
0037644F  0F 85 61 01 00 00               jne 0x1403765b6
00376455  48 83 C2 08                     add rdx, 8
00376459  4C 8B 02                        mov r8, qword ptr [rdx]
0037645C  49 3B D1                        cmp rdx, r9
0037645F  74 6C                           je 0x1403764cd
00376461  4D 85 C0                        test r8, r8
00376464  EB E9                           jmp 0x14037644f
00376466  E8 25 22 ED FF                  call 0x140248690
0037646B  88 44 24 78                     mov byte ptr [rsp + 0x78], al
0037646F  E9 C7 FE FF FF                  jmp 0x14037633b
00376474  48 2B C3                        sub rax, rbx
00376477  49 3B C0                        cmp rax, r8
0037647A  0F 82 48 FF FF FF               jb 0x1403763c8
00376480  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00376484  49 8D 78 FF                     lea rdi, [r8 - 1]
00376488  48 03 FB                        add rdi, rbx
0037648B  48 8B C3                        mov rax, rbx
0037648E  48 C1 E8 06                     shr rax, 6
00376492  48 8D 14 C1                     lea rdx, [rcx + rax*8]
00376496  48 8B C7                        mov rax, rdi
00376499  4C 8B 0A                        mov r9, qword ptr [rdx]
0037649C  48 C1 E8 06                     shr rax, 6
003764A0  4C 8D 14 C1                     lea r10, [rcx + rax*8]
003764A4  48 83 C8 FF                     or rax, 0xffffffffffffffff
003764A8  49 3B D2                        cmp rdx, r10
003764AB  75 30                           jne 0x1403764dd
003764AD  8D 48 41                        lea ecx, [rax + 0x41]
003764B0  41 2A C8                        sub cl, r8b
003764B3  48 D3 E8                        shr rax, cl
003764B6  48 8B CB                        mov rcx, rbx
003764B9  48 D3 E0                        shl rax, cl
003764BC  4C 23 C8                        and r9, rax
003764BF  4C 3B C8                        cmp r9, rax
003764C2  0F 85 00 FF FF FF               jne 0x1403763c8
003764C8  E9 07 FF FF FF                  jmp 0x1403763d4
003764CD  41 8A CA                        mov cl, r10b
003764D0  49 8B C3                        mov rax, r11
003764D3  F6 D1                           not cl
003764D5  48 D3 E8                        shr rax, cl
003764D8  E9 32 FE FF FF                  jmp 0x14037630f
003764DD  48 8B CB                        mov rcx, rbx
003764E0  48 D3 E0                        shl rax, cl
003764E3  4C 23 C8                        and r9, rax
003764E6  4C 3B C8                        cmp r9, rax
003764E9  0F 85 D9 FE FF FF               jne 0x1403763c8
003764EF  48 83 C2 08                     add rdx, 8
003764F3  4C 8B 0A                        mov r9, qword ptr [rdx]
003764F6  49 3B D2                        cmp rdx, r10
003764F9  74 06                           je 0x140376501
003764FB  49 83 F9 FF                     cmp r9, -1
003764FF  EB E8                           jmp 0x1403764e9
00376501  40 8A CF                        mov cl, dil
00376504  48 83 C8 FF                     or rax, 0xffffffffffffffff
00376508  F6 D1                           not cl
0037650A  48 D3 E8                        shr rax, cl
0037650D  EB AD                           jmp 0x1403764bc
0037650F  48 3B D8                        cmp rbx, rax
00376512  0F 83 9E 00 00 00               jae 0x1403765b6
00376518  48 83 FF 01                     cmp rdi, 1
0037651C  77 24                           ja 0x140376542
0037651E  0F 85 92 00 00 00               jne 0x1403765b6
00376524  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00376528  48 8B D3                        mov rdx, rbx
0037652B  48 8B CB                        mov rcx, rbx
0037652E  83 E2 3F                        and edx, 0x3f
00376531  48 C1 E9 06                     shr rcx, 6
00376535  48 0F A3 14 C8                  bt qword ptr [rax + rcx*8], rdx
0037653A  0F 92 C0                        setb al
0037653D  E9 4F FD FF FF                  jmp 0x140376291
00376542  48 2B C3                        sub rax, rbx
00376545  48 3B C7                        cmp rax, rdi
00376548  72 6C                           jb 0x1403765b6
0037654A  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0037654E  4C 8D 55 FF                     lea r10, [rbp - 1]
00376552  48 8B C3                        mov rax, rbx
00376555  48 C1 E8 06                     shr rax, 6
00376559  48 8D 14 C1                     lea rdx, [rcx + rax*8]
0037655D  49 8B C2                        mov rax, r10
00376560  4C 8B 02                        mov r8, qword ptr [rdx]
00376563  48 C1 E8 06                     shr rax, 6
00376567  4C 8D 0C C1                     lea r9, [rcx + rax*8]
0037656B  49 3B D1                        cmp rdx, r9
0037656E  75 20                           jne 0x140376590
00376570  B9 40 00 00 00                  mov ecx, 0x40
00376575  48 83 C8 FF                     or rax, 0xffffffffffffffff
00376579  40 2A CF                        sub cl, dil
0037657C  48 D3 E8                        shr rax, cl
0037657F  48 8B CB                        mov rcx, rbx
00376582  48 D3 E0                        shl rax, cl
00376585  4C 23 C0                        and r8, rax
00376588  4C 3B C0                        cmp r8, rax
0037658B  E9 82 FD FF FF                  jmp 0x140376312
00376590  49 83 CB FF                     or r11, 0xffffffffffffffff
00376594  48 8B CB                        mov rcx, rbx
00376597  49 8B C3                        mov rax, r11
0037659A  48 D3 E0                        shl rax, cl
0037659D  4C 23 C0                        and r8, rax
003765A0  4C 3B C0                        cmp r8, rax
003765A3  75 11                           jne 0x1403765b6
003765A5  48 83 C2 08                     add rdx, 8
003765A9  4C 8B 02                        mov r8, qword ptr [rdx]
003765AC  49 3B D1                        cmp rdx, r9
003765AF  74 0C                           je 0x1403765bd
003765B1  4D 3B C3                        cmp r8, r11
003765B4  74 EF                           je 0x1403765a5
003765B6  32 C0                           xor al, al
003765B8  E9 D4 FC FF FF                  jmp 0x140376291
003765BD  41 8A CA                        mov cl, r10b
003765C0  49 8B C3                        mov rax, r11
003765C3  F6 D1                           not cl
003765C5  48 D3 E8                        shr rax, cl
003765C8  EB BB                           jmp 0x140376585
003765CA  4D 2B D8                        sub r11, r8
003765CD  0F 84 C6 FC FF FF               je 0x140376299
003765D3  E9 3C FE FF FF                  jmp 0x140376414
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdateLargePageBitMap(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p70;
    unsigned __int8 v_stack_p78;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (32);
    v_r14 = (unsigned int)(((unsigned int)(a4)) & (1));
    result = (unsigned int)(((unsigned int)(a4)) & (2));
    if (a3 < 512) goto loc_003762AE;
    a4 = 0;
    v_stack_p20 = 17;
    v_r12 = 0;
    a4 = ((unsigned int)(result) != 0) ? 1 : 0;
loc_003761F9:
    v_r15 = (unsigned int)((2) - 1);
    result = ((unsigned int)((unsigned int)(v_r15))) << (4);
    v_rsi = (a1 + 16328) + (result);
    if ((*(unsigned __int64 *)(v_rsi)) == 0) goto loc_00376299;
    v_rbx = (a2) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 3629555 + v_r15 * 4 + 79336))));
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3629555 + v_r15 * 4 + 79336)));
    v_rbp = (*(unsigned __int64 *)(v_rip - 3629555 + v_r15 * 8 + 72800) - 1) + (a2);
    v_rbp = (v_rbp) + (a3);
    result = ~(*(unsigned __int64 *)(v_rip - 3629555 + v_r15 * 8 + 72800) - 1);
    v_rbp = (v_rbp) & (result);
    v_rbp = (v_rbp) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 3629555 + v_r15 * 4 + 79336))));
    v_rdi = (v_rbp) - (v_rbx);
    if (a4 != 0) goto loc_0037631A;
    if ((unsigned int)(v_r14) != 0) goto loc_0037650F;
    if (v_rbx >= (*(unsigned __int64 *)(v_rsi))) goto loc_003765B6;
    if (v_rdi > 1) goto loc_003762C4;
    if (v_rdi != 1) goto loc_003765B6;
    a2 = (unsigned int)((v_rbx) & (63));
    result = (v_rbx) >> (6);
    result = (condition_is_above_or_equal) ? 1 : 0;
loc_00376291:
    if ((unsigned __int8)(result) == 0) goto loc_0037631A;
loc_00376299:
    if (0 != 0) {
        a2 = v_stack_p20;
        a1 = v_rip + 11242519;
        result = MiReleaseSpinLockExclusive(a1, a2, a2, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
loc_003762C4:
    result = (result) - (v_stack_p10);
    if (result < v_rdi) goto loc_003765B6;
    result = (v_stack_p10) >> (6);
    result = (v_rbp - 1) >> (6);
    if ((*(unsigned __int64 *)(v_rsi + 8) + result * 8) != (*(unsigned __int64 *)(v_rsi + 8) + result * 8)) goto loc_0037643F;
    result = (result) | (-1);
    a1 = (unsigned __int8)((64) - ((unsigned __int8)(v_rdi)));
    result = (result) >> ((unsigned __int8)(a1));
    result = (result) << ((unsigned __int8)(v_stack_p10));
loc_0037630F:
loc_00376312:
    result = (((result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + result * 8))) == 0) ? 1 : 0;
    goto loc_00376291;
loc_0037631A:
    if (0 != 0) goto loc_0037633B;
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) == 0) goto loc_00376466;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 11242394, *(unsigned __int64 *)(v_rsi + 8) + result * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + result * 8), *(unsigned __int64 *)(v_rsi + 8) + result * 8);
loc_0037633B:
    if ((unsigned int)(v_r14) == 0) goto loc_00376435;
    result = RtlSetBitsEx(v_rsi, v_stack_p10, v_rdi, *(unsigned __int64 *)(v_rsi + 8) + result * 8);
loc_00376352:
    if ((unsigned int)(v_r15) == 0) goto loc_00376299;
    v_rbp = (v_rbp) - 1;
    a3 = (*(unsigned __int64 *)(v_rip - 3629933 + v_r15 - 1 * 8 + 72800)) >> ((unsigned __int8)((unsigned int)(v_stack_p70)));
    v_rbp = (v_rbp) + (a3);
    result = ~(a3 - 1);
    v_rbp = (v_rbp) & (result);
    v_rbx = (v_stack_p10) & (result);
    v_r11 = (v_rbp) - (v_rbx);
    if ((unsigned int)(v_r14) == 0) goto loc_0037641B;
    if (v_rbx >= (*(unsigned __int64 *)(v_rsi))) goto loc_003763C8;
    if (a3 > 1) goto loc_00376474;
    if (a3 != 1) goto loc_003763C8;
    a2 = (unsigned int)((v_rbx) & (63));
    a1 = (v_rbx) >> (6);
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_003763D4;
loc_003763C8:
    v_r11 = (v_r11) - (a3);
    if (condition_is_equal) goto loc_00376299;
    v_rbx = (v_rbx) + (a3);
loc_003763D4:
    a4 = (v_rbp) - (a3);
    if (a4 >= (*(unsigned __int64 *)(v_rsi))) goto loc_003765CA;
    if (a3 != 1) goto loc_003765CA;
    a4 = (a4) >> (6);
    a1 = (unsigned int)((a4) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_003765CA;
loc_00376414:
loc_0037641B:
    a3 = (v_rbx) << ((unsigned __int8)((unsigned int)(v_stack_p70)));
    v_r11 = (v_r11) << ((unsigned __int8)((unsigned int)(v_stack_p70)));
    goto loc_003761F9;
loc_00376435:
    result = RtlClearBitsEx((unsigned int)(v_stack_p70), v_stack_p60, a3, (unsigned int)((unsigned int)(v_r14)));
    goto loc_00376352;
loc_0037643F:
    v_r11 = (v_r11) | (-1);
    result = (v_r11) << ((unsigned __int8)(v_rbx));
loc_0037644F:
    if (((result) & (a3)) != 0) goto loc_003765B6;
    a2 = (v_stack_p60) + (8);
    if (a2 == ((unsigned int)((unsigned int)(v_r14)))) goto loc_003764CD;
    goto loc_0037644F;
loc_00376466:
    result = ExAcquireSpinLockExclusive(v_rbx, a2, *(unsigned __int64 *)(a2), (unsigned int)((unsigned int)(v_r14)));
    v_stack_p78 = (unsigned __int8)(result);
    goto loc_0037633B;
loc_00376474:
    result = (result) - (v_rbx);
    if (result < (*(unsigned __int64 *)(a2))) goto loc_003763C8;
    v_rdi = (*(unsigned __int64 *)(a2) - 1) + (v_rbx);
    result = (v_rbx) >> (6);
    result = (v_rdi) >> (6);
    result = (result) | (-1);
    if ((*(unsigned __int64 *)(v_rsi + 8) + result * 8) != (*(unsigned __int64 *)(v_rsi + 8) + result * 8)) goto loc_003764DD;
    a1 = (unsigned __int8)((result + 65) - ((unsigned __int8)(*(unsigned __int64 *)(a2))));
    result = (result) >> ((unsigned __int8)(a1));
    result = (result) << ((unsigned __int8)(v_rbx));
loc_003764BC:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + result * 8)) & (result);
    if (a4 != result) goto loc_003763C8;
    goto loc_003763D4;
loc_003764CD:
    a1 = (unsigned __int8)(~((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 8) + result * 8)));
    result = (v_r11) >> ((unsigned __int8)(a1));
    goto loc_0037630F;
loc_003764DD:
    result = (result) << ((unsigned __int8)(v_rbx));
    a4 = (a4) & (result);
loc_003764E9:
    if (a4 != result) goto loc_003763C8;
    a2 = (*(unsigned __int64 *)(v_rsi + 8) + result * 8) + (8);
    if (a2 == (*(unsigned __int64 *)(v_rsi + 8) + result * 8)) goto loc_00376501;
    goto loc_003764E9;
loc_00376501:
    result = (result) | (-1);
    a1 = (unsigned __int8)(~((unsigned __int8)(v_rdi)));
    result = (result) >> ((unsigned __int8)(a1));
    goto loc_003764BC;
loc_0037650F:
    if (v_rbx >= result) goto loc_003765B6;
    if (v_rdi > 1) goto loc_00376542;
    if (v_rdi != 1) goto loc_003765B6;
    a2 = (unsigned int)((v_rbx) & (63));
    a1 = (v_rbx) >> (6);
    result = (condition_is_below) ? 1 : 0;
    goto loc_00376291;
loc_00376542:
    result = (result) - (v_rbx);
    if (result < v_rdi) goto loc_003765B6;
    result = (v_rbx) >> (6);
    result = (v_rbp - 1) >> (6);
    if ((*(unsigned __int64 *)(v_rsi + 8) + result * 8) != (*(unsigned __int64 *)(v_rsi + 8) + result * 8)) goto loc_00376590;
    result = (result) | (-1);
    a1 = (unsigned __int8)((64) - ((unsigned __int8)(v_rdi)));
    result = (result) >> ((unsigned __int8)(a1));
    result = (result) << ((unsigned __int8)(v_rbx));
loc_00376585:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + result * 8)) & (result);
    goto loc_00376312;
loc_00376590:
    v_r11 = (v_r11) | (-1);
    result = (v_r11) << ((unsigned __int8)(v_rbx));
    a3 = (a3) & (result);
    if (a3 != result) goto loc_003765B6;
loc_003765A5:
    a2 = (*(unsigned __int64 *)(v_rsi + 8) + result * 8) + (8);
    if (a2 == (*(unsigned __int64 *)(v_rsi + 8) + result * 8)) goto loc_003765BD;
    if ((*(unsigned __int64 *)(a2)) == v_r11) goto loc_003765A5;
loc_003765B6:
    result = 0;
    goto loc_00376291;
loc_003765BD:
    a1 = (unsigned __int8)(~((unsigned __int8)(v_rbp - 1)));
    result = (v_r11) >> ((unsigned __int8)(a1));
    goto loc_00376585;
loc_003765CA:
    v_r11 = (v_r11) - (*(unsigned __int64 *)(a2));
    if (condition_is_equal) goto loc_00376299;
    goto loc_00376414;
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdateLargePageBitMap(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p60;
    uint32_t v_stack_p70;
    uint8_t v_stack_p78;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (32);
    local_r14 = (uint32_t)(((uint32_t)(Arg4)) & (1));
    result = (uint32_t)(((uint32_t)(Arg4)) & (2));
    if (Arg3 < 512) goto loc_003762AE;
    Arg4 = 0;
    v_stack_p20 = 17;
    local_r12 = 0;
    Arg4 = ((uint32_t)(result) != 0) ? 1 : 0;
loc_003761F9:
    local_r15 = (uint32_t)((2) - 1);
    result = ((uint32_t)((uint32_t)(local_r15))) << (4);
    local_rsi = (Arg1 + 16328) + (result);
    if ((*(uint64_t *)(local_rsi)) == 0) goto loc_00376299;
    local_rbx = (Arg2) >> ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3761F3 + local_r15 * 4 + 0x135E8))));
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3761F3 + local_r15 * 4 + 0x135E8)));
    local_rbp = (*(uint64_t *)(v_rip - 0x3761F3 + local_r15 * 8 + 0x11C60) - 1) + (Arg2);
    local_rbp = (local_rbp) + (Arg3);
    result = ~(*(uint64_t *)(v_rip - 0x3761F3 + local_r15 * 8 + 0x11C60) - 1);
    local_rbp = (local_rbp) & (result);
    local_rbp = (local_rbp) >> ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3761F3 + local_r15 * 4 + 0x135E8))));
    local_rdi = (local_rbp) - (local_rbx);
    if (Arg4 != 0) goto loc_0037631A;
    if ((uint32_t)(local_r14) != 0) goto loc_0037650F;
    if (local_rbx >= (*(uint64_t *)(local_rsi))) goto loc_003765B6;
    if (local_rdi > 1) goto loc_003762C4;
    if (local_rdi != 1) goto loc_003765B6;
    Arg2 = (uint32_t)((local_rbx) & (63));
    result = (local_rbx) >> (6);
    result = (condition_is_above_or_equal) ? 1 : 0;
loc_00376291:
    if ((uint8_t)(result) == 0) goto loc_0037631A;
loc_00376299:
    if (0 != 0) {
        Arg2 = v_stack_p20;
        Arg1 = v_rip + 11242519;
        result = MiReleaseSpinLockExclusive(Arg1, Arg2, Arg2, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
loc_003762C4:
    result = (result) - (v_stack_p10);
    if (result < local_rdi) goto loc_003765B6;
    result = (v_stack_p10) >> (6);
    result = (local_rbp - 1) >> (6);
    if ((*(uint64_t *)(local_rsi + 0x8) + result * 8) != (*(uint64_t *)(local_rsi + 0x8) + result * 8)) goto loc_0037643F;
    result = (result) | (-1);
    Arg1 = (uint8_t)((64) - ((uint8_t)(local_rdi)));
    result = (result) >> ((uint8_t)(Arg1));
    result = (result) << ((uint8_t)(v_stack_p10));
loc_0037630F:
loc_00376312:
    result = (((result) & (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + result * 8))) == 0) ? 1 : 0;
    goto loc_00376291;
loc_0037631A:
    if (0 != 0) goto loc_0037633B;
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) == 0) goto loc_00376466;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 11242394, *(uint64_t *)(local_rsi + 0x8) + result * 8, *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + result * 8), *(uint64_t *)(local_rsi + 0x8) + result * 8);
loc_0037633B:
    if ((uint32_t)(local_r14) == 0) goto loc_00376435;
    result = RtlSetBitsEx(local_rsi, v_stack_p10, local_rdi, *(uint64_t *)(local_rsi + 0x8) + result * 8);
loc_00376352:
    if ((uint32_t)(local_r15) == 0) goto loc_00376299;
    local_rbp = (local_rbp) - 1;
    Arg3 = (*(uint64_t *)(v_rip - 0x37636D + local_r15 - 0x1 * 8 + 0x11C60)) >> ((uint8_t)((uint32_t)(v_stack_p70)));
    local_rbp = (local_rbp) + (Arg3);
    result = ~(Arg3 - 1);
    local_rbp = (local_rbp) & (result);
    local_rbx = (v_stack_p10) & (result);
    local_r11 = (local_rbp) - (local_rbx);
    if ((uint32_t)(local_r14) == 0) goto loc_0037641B;
    if (local_rbx >= (*(uint64_t *)(local_rsi))) goto loc_003763C8;
    if (Arg3 > 1) goto loc_00376474;
    if (Arg3 != 1) goto loc_003763C8;
    Arg2 = (uint32_t)((local_rbx) & (63));
    Arg1 = (local_rbx) >> (6);
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_003763D4;
loc_003763C8:
    local_r11 = (local_r11) - (Arg3);
    if (condition_is_equal) goto loc_00376299;
    local_rbx = (local_rbx) + (Arg3);
loc_003763D4:
    Arg4 = (local_rbp) - (Arg3);
    if (Arg4 >= (*(uint64_t *)(local_rsi))) goto loc_003765CA;
    if (Arg3 != 1) goto loc_003765CA;
    Arg4 = (Arg4) >> (6);
    Arg1 = (uint32_t)((Arg4) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_003765CA;
loc_00376414:
loc_0037641B:
    Arg3 = (local_rbx) << ((uint8_t)((uint32_t)(v_stack_p70)));
    local_r11 = (local_r11) << ((uint8_t)((uint32_t)(v_stack_p70)));
    goto loc_003761F9;
loc_00376435:
    result = RtlClearBitsEx((uint32_t)(v_stack_p70), v_stack_p60, Arg3, (uint32_t)((uint32_t)(local_r14)));
    goto loc_00376352;
loc_0037643F:
    local_r11 = (local_r11) | (-1);
    result = (local_r11) << ((uint8_t)(local_rbx));
loc_0037644F:
    if (((result) & (Arg3)) != 0) goto loc_003765B6;
    Arg2 = (v_stack_p60) + (8);
    if (Arg2 == ((uint32_t)((uint32_t)(local_r14)))) goto loc_003764CD;
    goto loc_0037644F;
loc_00376466:
    result = ExAcquireSpinLockExclusive(local_rbx, Arg2, *(uint64_t *)(Arg2), (uint32_t)((uint32_t)(local_r14)));
    v_stack_p78 = (uint8_t)(result);
    goto loc_0037633B;
loc_00376474:
    result = (result) - (local_rbx);
    if (result < (*(uint64_t *)(Arg2))) goto loc_003763C8;
    local_rdi = (*(uint64_t *)(Arg2) - 1) + (local_rbx);
    result = (local_rbx) >> (6);
    result = (local_rdi) >> (6);
    result = (result) | (-1);
    if ((*(uint64_t *)(local_rsi + 0x8) + result * 8) != (*(uint64_t *)(local_rsi + 0x8) + result * 8)) goto loc_003764DD;
    Arg1 = (uint8_t)((result + 65) - ((uint8_t)(*(uint64_t *)(Arg2))));
    result = (result) >> ((uint8_t)(Arg1));
    result = (result) << ((uint8_t)(local_rbx));
loc_003764BC:
    Arg4 = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + result * 8)) & (result);
    if (Arg4 != result) goto loc_003763C8;
    goto loc_003763D4;
loc_003764CD:
    Arg1 = (uint8_t)(~((uint8_t)(*(uint64_t *)(local_rsi + 0x8) + result * 8)));
    result = (local_r11) >> ((uint8_t)(Arg1));
    goto loc_0037630F;
loc_003764DD:
    result = (result) << ((uint8_t)(local_rbx));
    Arg4 = (Arg4) & (result);
loc_003764E9:
    if (Arg4 != result) goto loc_003763C8;
    Arg2 = (*(uint64_t *)(local_rsi + 0x8) + result * 8) + (8);
    if (Arg2 == (*(uint64_t *)(local_rsi + 0x8) + result * 8)) goto loc_00376501;
    goto loc_003764E9;
loc_00376501:
    result = (result) | (-1);
    Arg1 = (uint8_t)(~((uint8_t)(local_rdi)));
    result = (result) >> ((uint8_t)(Arg1));
    goto loc_003764BC;
loc_0037650F:
    if (local_rbx >= result) goto loc_003765B6;
    if (local_rdi > 1) goto loc_00376542;
    if (local_rdi != 1) goto loc_003765B6;
    Arg2 = (uint32_t)((local_rbx) & (63));
    Arg1 = (local_rbx) >> (6);
    result = (condition_is_below) ? 1 : 0;
    goto loc_00376291;
loc_00376542:
    result = (result) - (local_rbx);
    if (result < local_rdi) goto loc_003765B6;
    result = (local_rbx) >> (6);
    result = (local_rbp - 1) >> (6);
    if ((*(uint64_t *)(local_rsi + 0x8) + result * 8) != (*(uint64_t *)(local_rsi + 0x8) + result * 8)) goto loc_00376590;
    result = (result) | (-1);
    Arg1 = (uint8_t)((64) - ((uint8_t)(local_rdi)));
    result = (result) >> ((uint8_t)(Arg1));
    result = (result) << ((uint8_t)(local_rbx));
loc_00376585:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + result * 8)) & (result);
    goto loc_00376312;
loc_00376590:
    local_r11 = (local_r11) | (-1);
    result = (local_r11) << ((uint8_t)(local_rbx));
    Arg3 = (Arg3) & (result);
    if (Arg3 != result) goto loc_003765B6;
loc_003765A5:
    Arg2 = (*(uint64_t *)(local_rsi + 0x8) + result * 8) + (8);
    if (Arg2 == (*(uint64_t *)(local_rsi + 0x8) + result * 8)) goto loc_003765BD;
    if ((*(uint64_t *)(Arg2)) == local_r11) goto loc_003765A5;
loc_003765B6:
    result = 0;
    goto loc_00376291;
loc_003765BD:
    Arg1 = (uint8_t)(~((uint8_t)(local_rbp - 1)));
    result = (local_r11) >> ((uint8_t)(Arg1));
    goto loc_00376585;
loc_003765CA:
    local_r11 = (local_r11) - (*(uint64_t *)(Arg2));
    if (condition_is_equal) goto loc_00376299;
    goto loc_00376414;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037619C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
