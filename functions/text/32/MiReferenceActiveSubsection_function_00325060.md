# MiReferenceActiveSubsection

- RVA: `0x00325060`–`0x00325744` (길이 `1,764` bytes)
- VA: `0x0000000140325060`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00075BB4`
- 디코드: `394`개 명령, `1,764/1,764` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0032511E` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00325126` → [MiUnlinkUnusedSubsection](../24/MiUnlinkUnusedSubsection_function_002496F4.md) (function, `0x002496F4`)
- `0x00325132` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00325214` → [MiGetSubsectionHoldingCrossPartitionReferences](../45/MiGetSubsectionHoldingCrossPartitionReferences_function_004589E4.md) (function, `0x004589E4`)
- `0x0032521F` → [MiGetSubsectionHoldingCrossPartitionReferences](../45/MiGetSubsectionHoldingCrossPartitionReferences_function_004589E4.md) (function, `0x004589E4`)
- `0x0032526E` → [MiComputeCrossPartitionSectionCharges](MiComputeCrossPartitionSectionCharges_function_00325BBC.md) (function, `0x00325BBC`)
- `0x003252B1` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003252EE` → [MiGetCrossPartitionCharges](MiGetCrossPartitionCharges_function_00325BFC.md) (function, `0x00325BFC`)
- `0x0032534E` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00325371` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)
- `0x00325388` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003253E3` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00325402` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00325424` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0032546E` → [ExpWaitForSpinLockExclusiveAndAcquire](ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x003254EE` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0032550A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00325537` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x0032554C` → [MiReturnCrossPartitionCharges](../28/MiReturnCrossPartitionCharges_function_002867D0.md) (function, `0x002867D0`)
- `0x0032557E` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x0032558F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003255A7` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003255B6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003255C3` → [MiGetCommittedPages](MiGetCommittedPages_function_00325CE0.md) (function, `0x00325CE0`)
- `0x00325615` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0032565B` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x00325673` → [MiReturnCrossPartitionCharges](../28/MiReturnCrossPartitionCharges_function_002867D0.md) (function, `0x002867D0`)
- `0x0032568F` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003256C0` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003256D3` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x003256E0` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003256ED` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003256FF` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00325722` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)
- `0x00325739` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)

### Direct callers
- [MiAddViewsForSection](MiAddViewsForSection_function_00324990.md) at `0x00324ABA`
- [MiUpControlAreaRefs](../3B/MiUpControlAreaRefs_function_003B2BF0.md) at `0x003B2DFD`
- [MiUpControlAreaRefs](../3B/MiUpControlAreaRefs_function_003B2BF0.md) at `0x003B2E5D`
- [MiInsertInSystemSpace](../3B/MiInsertInSystemSpace_function_003B2F5C.md) at `0x003B33BF`
- [MiMapImageInSystemSpace](../../page/94/MiMapImageInSystemSpace_function_00941DD8.md) at `0x00941FFD`
- [MiMapViewOfImageSection](../../page/97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F862`
- [MmLoadSystemImageEx](../../page/99/MmLoadSystemImageEx_function_00999B8C.md) at `0x00999DFE`

### Static image references
- `0x00325106` → RVA `0x00E30088` (`.data`; read)
- `0x0032528D` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003252A0` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00325392` → RVA `0x00E38D00` (`.data`; read)
- `0x003253CA` → RVA `0x00F0DE58` (`.data`; read)
- `0x00325494` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00325599` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0032563C` → RVA `0x00E30090` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0032564C` → [sub_006E1B8C](../6E/Unknown_function_006E1B8C.md) (`tail-transfer`)
  - `0x00325662` → [sub_006E1B8C](../6E/Unknown_function_006E1B8C.md) (`tail-transfer`)
  - `0x003256A4` → [sub_006E1B8C + 0x44](../6E/Unknown_function_006E1B8C.md) (`tail-transfer`)
  - `0x003256AF` → [sub_006E1B8C + 0x44](../6E/Unknown_function_006E1B8C.md) (`tail-transfer`)
  - `0x0032572F` → [sub_006E1B8C + 0x54](../6E/Unknown_function_006E1B8C.md) (`tail-transfer`)
  - `0x0032573F` → [sub_006E1B8C + 0x54](../6E/Unknown_function_006E1B8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00325060  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
00325065  53                              push rbx
00325066  55                              push rbp
00325067  56                              push rsi
00325068  57                              push rdi
00325069  41 54                           push r12
0032506B  41 55                           push r13
0032506D  41 56                           push r14
0032506F  41 57                           push r15
00325071  48 83 EC 58                     sub rsp, 0x58
00325075  48 8B 31                        mov rsi, qword ptr [rcx]
00325078  33 C0                           xor eax, eax
0032507A  45 33 ED                        xor r13d, r13d
0032507D  C7 84 24 A8 00 00 00 00 00 00 00  mov dword ptr [rsp + 0xa8], 0
00325088  45 0F B6 F8                     movzx r15d, r8b
0032508C  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00325091  44 8B E2                        mov r12d, edx
00325094  4C 8B F1                        mov r14, rcx
00325097  48 8B 6E 40                     mov rbp, qword ptr [rsi + 0x40]
0032509B  48 85 ED                        test rbp, rbp
0032509E  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
003250A3  0F 95 C0                        setne al
003250A6  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
003250AD  41 80 F8 11                     cmp r8b, 0x11
003250B1  0F 84 4F 05 00 00               je 0x140325606
003250B7  41 B9 02 00 00 00               mov r9d, 2
003250BD  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
003250C2  49 83 7E 08 00                  cmp qword ptr [r14 + 8], 0
003250C7  49 8B 3E                        mov rdi, qword ptr [r14]
003250CA  0F 84 91 01 00 00               je 0x140325261
003250D0  48 8B 6F 40                     mov rbp, qword ptr [rdi + 0x40]
003250D4  4D 8B FE                        mov r15, r14
003250D7  41 F6 C4 08                     test r12b, 8
003250DB  0F 85 B3 00 00 00               jne 0x140325194
003250E1  41 B9 02 00 00 00               mov r9d, 2
003250E7  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
003250EA  A8 20                           test al, 0x20
003250EC  75 71                           jne 0x14032515f
003250EE  48 83 7F 40 00                  cmp qword ptr [rdi + 0x40], 0
003250F3  74 6A                           je 0x14032515f
003250F5  41 8B 5F 20                     mov ebx, dword ptr [r15 + 0x20]
003250F9  0F BA E3 13                     bt ebx, 0x13
003250FD  73 42                           jae 0x140325141
003250FF  49 8B 07                        mov rax, qword ptr [r15]
00325102  0F B7 48 3C                     movzx ecx, word ptr [rax + 0x3c]
00325106  48 8B 05 7B AF B0 00            mov rax, qword ptr [rip + 0xb0af7b]
0032510D  81 E1 FF 03 00 00               and ecx, 0x3ff
00325113  48 8B 34 C8                     mov rsi, qword ptr [rax + rcx*8]
00325117  48 8D 8E C0 06 00 00            lea rcx, [rsi + 0x6c0]
0032511E  E8 5D 3D F2 FF                  call 0x140248e80
00325123  49 8B CF                        mov rcx, r15
00325126  E8 C9 45 F2 FF                  call 0x1402496f4
0032512B  48 8D 8E C0 06 00 00            lea rcx, [rsi + 0x6c0]
00325132  E8 A9 46 F2 FF                  call 0x1402497e0
00325137  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0032513C  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00325141  0F BA E3 10                     bt ebx, 0x10
00325145  72 18                           jb 0x14032515f
00325147  49 FF 47 50                     inc qword ptr [r15 + 0x50]
0032514B  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00325155  49 85 4F 50                     test qword ptr [r15 + 0x50], rcx
00325159  0F 84 AD 02 00 00               je 0x14032540c
0032515F  48 85 ED                        test rbp, rbp
00325162  0F 85 AC 01 00 00               jne 0x140325314
00325168  41 83 F9 02                     cmp r9d, 2
0032516C  0F 84 BD 01 00 00               je 0x14032532f
00325172  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
0032517A  0F 85 34 05 00 00               jne 0x1403256b4
00325180  33 C0                           xor eax, eax
00325182  48 83 C4 58                     add rsp, 0x58
00325186  41 5F                           pop r15
00325188  41 5E                           pop r14
0032518A  41 5D                           pop r13
0032518C  41 5C                           pop r12
0032518E  5F                              pop rdi
0032518F  5E                              pop rsi
00325190  5D                              pop rbp
00325191  5B                              pop rbx
00325192  C3                              ret
00325193  CC                              int3
00325194  44 0F B6 47 3E                  movzx r8d, byte ptr [rdi + 0x3e]
00325199  41 F6 C0 0C                     test r8b, 0xc
0032519D  0F 85 3E FF FF FF               jne 0x1403250e1
003251A3  48 85 ED                        test rbp, rbp
003251A6  75 0D                           jne 0x1403251b5
003251A8  F7 47 5C 00 00 01 00            test dword ptr [rdi + 0x5c], 0x10000
003251AF  0F 85 2C FF FF FF               jne 0x1403250e1
003251B5  0F B7 47 3C                     movzx eax, word ptr [rdi + 0x3c]
003251B9  48 8B 0D C8 AE B0 00            mov rcx, qword ptr [rip + 0xb0aec8]
003251C0  25 FF 03 00 00                  and eax, 0x3ff
003251C5  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
003251C9  45 84 E4                        test r12b, r12b
003251CC  0F 88 C0 01 00 00               js 0x140325392
003251D2  41 F6 C4 10                     test r12b, 0x10
003251D6  0F 85 4E 04 00 00               jne 0x14032562a
003251DC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003251E5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003251EC  0F B7 81 AE 04 00 00            movzx eax, word ptr [rcx + 0x4ae]
003251F3  48 8B 0D 8E AE B0 00            mov rcx, qword ptr [rip + 0xb0ae8e]
003251FA  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003251FE  48 3B C2                        cmp rax, rdx
00325201  0F 84 DA FE FF FF               je 0x1403250e1
00325207  41 F6 C0 01                     test r8b, 1
0032520B  0F 85 20 04 00 00               jne 0x140325631
00325211  49 8B CE                        mov rcx, r14
00325214  E8 CB 37 13 00                  call 0x1404589e4
00325219  48 8B C8                        mov rcx, rax
0032521C  4C 8B F8                        mov r15, rax
0032521F  E8 C0 37 13 00                  call 0x1404589e4
00325224  8B 50 30                        mov edx, dword ptr [rax + 0x30]
00325227  81 E2 FF FF FF 3F               and edx, 0x3fffffff
0032522D  81 FA FF FF FF 3F               cmp edx, 0x3fffffff
00325233  0F 84 A8 FE FF FF               je 0x1403250e1
00325239  85 D2                           test edx, edx
0032523B  0F 85 68 04 00 00               jne 0x1403256a9
00325241  41 F6 C4 20                     test r12b, 0x20
00325245  0F 85 4E 04 00 00               jne 0x140325699
0032524B  B8 01 00 00 00                  mov eax, 1
00325250  85 C0                           test eax, eax
00325252  0F 84 5A 01 00 00               je 0x1403253b2
00325258  44 0F B6 BC 24 B0 00 00 00      movzx r15d, byte ptr [rsp + 0xb0]
00325261  41 F6 C4 20                     test r12b, 0x20
00325265  0F 85 8C 04 00 00               jne 0x1403256f7
0032526B  49 8B CE                        mov rcx, r14
0032526E  E8 49 09 00 00                  call 0x140325bbc
00325273  4C 8B E8                        mov r13, rax
00325276  48 85 C0                        test rax, rax
00325279  0F 84 AB 01 00 00               je 0x14032542a
0032527F  48 8D 5E 48                     lea rbx, [rsi + 0x48]
00325283  41 80 FF 11                     cmp r15b, 0x11
00325287  0F 84 11 01 00 00               je 0x14032539e
0032528D  F6 05 72 18 CA 00 01            test byte ptr [rip + 0xca1872], 1
00325294  0F 85 30 01 00 00               jne 0x1403253ca
0032529A  C7 03 00 00 00 00               mov dword ptr [rbx], 0
003252A0  83 3D 79 1A CA 00 00            cmp dword ptr [rip + 0xca1a79], 0
003252A7  74 0D                           je 0x1403252b6
003252A9  44 0F 20 C1                     mov rcx, cr8
003252AD  41 0F B6 D7                     movzx edx, r15b
003252B1  E8 E2 03 1D 00                  call 0x1404f5698
003252B6  41 0F B6 C7                     movzx eax, r15b
003252BA  44 0F 22 C0                     mov cr8, rax
003252BE  49 8B 06                        mov rax, qword ptr [r14]
003252C1  33 FF                           xor edi, edi
003252C3  4D 8B CD                        mov r9, r13
003252C6  0F B7 48 3C                     movzx ecx, word ptr [rax + 0x3c]
003252CA  48 8B 68 40                     mov rbp, qword ptr [rax + 0x40]
003252CE  48 8B 05 B3 AD B0 00            mov rax, qword ptr [rip + 0xb0adb3]
003252D5  48 85 ED                        test rbp, rbp
003252D8  40 0F 95 C7                     setne dil
003252DC  81 E1 FF 03 00 00               and ecx, 0x3ff
003252E2  44 8B C7                        mov r8d, edi
003252E5  33 D2                           xor edx, edx
003252E7  48 8B 34 C8                     mov rsi, qword ptr [rax + rcx*8]
003252EB  48 8B CE                        mov rcx, rsi
003252EE  E8 09 09 00 00                  call 0x140325bfc
003252F3  44 8B F8                        mov r15d, eax
003252F6  85 C0                           test eax, eax
003252F8  0F 89 4B 03 00 00               jns 0x140325649
003252FE  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
00325306  0F 84 DE 03 00 00               je 0x1403256ea
0032530C  41 8B C7                        mov eax, r15d
0032530F  E9 6E FE FF FF                  jmp 0x140325182
00325314  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
00325317  A8 20                           test al, 0x20
00325319  0F 85 49 FE FF FF               jne 0x140325168
0032531F  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00325323  83 C8 01                        or eax, 1
00325326  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0032532A  E9 39 FE FF FF                  jmp 0x140325168
0032532F  41 F6 C4 20                     test r12b, 0x20
00325333  0F 84 39 FE FF FF               je 0x140325172
00325339  4D 85 ED                        test r13, r13
0032533C  0F 84 30 FE FF FF               je 0x140325172
00325342  0F B6 94 24 B0 00 00 00         movzx edx, byte ptr [rsp + 0xb0]
0032534A  48 8D 4E 48                     lea rcx, [rsi + 0x48]
0032534E  E8 6D 2F F2 FF                  call 0x1402482c0
00325353  0F B7 46 3C                     movzx eax, word ptr [rsi + 0x3c]
00325357  4D 8B C5                        mov r8, r13
0032535A  48 8B 0D 27 AD B0 00            mov rcx, qword ptr [rip + 0xb0ad27]
00325361  25 FF 03 00 00                  and eax, 0x3ff
00325366  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
0032536D  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00325371  E8 A6 52 19 00                  call 0x1404ba61c
00325376  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
0032537E  0F 85 FC FD FF FF               jne 0x140325180
00325384  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00325388  E8 03 33 F2 FF                  call 0x140248690
0032538D  E9 EE FD FF FF                  jmp 0x140325180
00325392  48 8D 05 67 39 B1 00            lea rax, [rip + 0xb13967]
00325399  E9 60 FE FF FF                  jmp 0x1403251fe
0032539E  F6 05 61 17 CA 00 01            test byte ptr [rip + 0xca1761], 1
003253A5  75 46                           jne 0x1403253ed
003253A7  C7 03 00 00 00 00               mov dword ptr [rbx], 0
003253AD  E9 0C FF FF FF                  jmp 0x1403252be
003253B2  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
003253BA  0F 85 C3 02 00 00               jne 0x140325683
003253C0  B8 0B 06 00 C0                  mov eax, 0xc000060b
003253C5  E9 B8 FD FF FF                  jmp 0x140325182
003253CA  8B 05 88 8A BE 00               mov eax, dword ptr [rip + 0xbe8a88]
003253D0  85 C0                           test eax, eax
003253D2  0F 85 C2 FE FF FF               jne 0x14032529a
003253D8  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
003253E0  48 8B CB                        mov rcx, rbx
003253E3  E8 5C BB F9 FF                  call 0x1402c0f44
003253E8  E9 B3 FE FF FF                  jmp 0x1403252a0
003253ED  8B 05 65 8A BE 00               mov eax, dword ptr [rip + 0xbe8a65]
003253F3  85 C0                           test eax, eax
003253F5  75 B0                           jne 0x1403253a7
003253F7  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
003253FF  48 8B CB                        mov rcx, rbx
00325402  E8 3D BB F9 FF                  call 0x1402c0f44
00325407  E9 B2 FE FF FF                  jmp 0x1403252be
0032540C  45 33 C9                        xor r9d, r9d
0032540F  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00325418  4D 8B C7                        mov r8, r15
0032541B  BA 00 20 04 00                  mov edx, 0x42000
00325420  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
00325424  E8 37 82 1D 00                  call 0x1404fd660
00325429  CC                              int3
0032542A  41 83 CC 20                     or r12d, 0x20
0032542E  E9 8F FC FF FF                  jmp 0x1403250c2
00325433  41 83 CC 20                     or r12d, 0x20
00325437  44 0F 20 C6                     mov rsi, cr8
0032543B  B8 02 00 00 00                  mov eax, 2
00325440  44 0F 22 C0                     mov cr8, rax
00325444  83 3D D5 18 CA 00 00            cmp dword ptr [rip + 0xca18d5], 0
0032544B  0F 85 37 01 00 00               jne 0x140325588
00325451  F6 05 AE 16 CA 00 21            test byte ptr [rip + 0xca16ae], 0x21
00325458  0F 85 0B 01 00 00               jne 0x140325569
0032545E  33 FF                           xor edi, edi
00325460  F0 0F BA 2B 1F                  lock bts dword ptr [rbx], 0x1f
00325465  73 0E                           jae 0x140325475
00325467  40 0F B6 D6                     movzx edx, sil
0032546B  48 8B CB                        mov rcx, rbx
0032546E  E8 2D E5 FF FF                  call 0x1403239a0
00325473  8B F8                           mov edi, eax
00325475  8B 13                           mov edx, dword ptr [rbx]
00325477  8B CA                           mov ecx, edx
00325479  0F BA F1 1E                     btr ecx, 0x1e
0032547D  81 F9 00 00 00 80               cmp ecx, 0x80000000
00325483  74 2C                           je 0x1403254b1
00325485  0F BA E2 1E                     bt edx, 0x1e
00325489  72 07                           jb 0x140325492
0032548B  F0 81 0B 00 00 00 40            lock or dword ptr [rbx], 0x40000000
00325492  FF C7                           inc edi
00325494  85 3D 12 FE C9 00               test dword ptr [rip + 0xc9fe12], edi
0032549A  0F 84 F9 00 00 00               je 0x140325599
003254A0  F3 90                           pause
003254A2  8B 13                           mov edx, dword ptr [rbx]
003254A4  8B C2                           mov eax, edx
003254A6  0F BA F0 1E                     btr eax, 0x1e
003254AA  3D 00 00 00 80                  cmp eax, 0x80000000
003254AF  75 D4                           jne 0x140325485
003254B1  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
003254B6  44 0F B6 BC 24 B0 00 00 00      movzx r15d, byte ptr [rsp + 0xb0]
003254BF  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
003254C2  A8 20                           test al, 0x20
003254C4  0F 85 F8 FB FF FF               jne 0x1403250c2
003254CA  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
003254CF  48 85 ED                        test rbp, rbp
003254D2  0F 84 E8 00 00 00               je 0x1403255c0
003254D8  49 83 7E 08 00                  cmp qword ptr [r14 + 8], 0
003254DD  0F 85 FC 00 00 00               jne 0x1403255df
003254E3  0F B6 BC 24 B0 00 00 00         movzx edi, byte ptr [rsp + 0xb0]
003254EB  48 8B CB                        mov rcx, rbx
003254EE  E8 ED 42 F2 FF                  call 0x1402497e0
003254F3  40 80 FF 11                     cmp dil, 0x11
003254F7  74 1A                           je 0x140325513
003254F9  83 3D 20 18 CA 00 00            cmp dword ptr [rip + 0xca1820], 0
00325500  74 0D                           je 0x14032550f
00325502  44 0F 20 C1                     mov rcx, cr8
00325506  40 0F B6 D7                     movzx edx, dil
0032550A  E8 89 01 1D 00                  call 0x1404f5698
0032550F  44 0F 22 C7                     mov cr8, rdi
00325513  0F B7 4E 3C                     movzx ecx, word ptr [rsi + 0x3c]
00325517  48 8B 05 6A AB B0 00            mov rax, qword ptr [rip + 0xb0ab6a]
0032551E  81 E1 FF 03 00 00               and ecx, 0x3ff
00325524  48 8B 3C C8                     mov rdi, qword ptr [rax + rcx*8]
00325528  48 85 ED                        test rbp, rbp
0032552B  0F 85 99 01 00 00               jne 0x1403256ca
00325531  49 8B D5                        mov rdx, r13
00325534  48 8B CF                        mov rcx, rdi
00325537  E8 54 13 F6 FF                  call 0x140286890
0032553C  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00325544  4D 8B CD                        mov r9, r13
00325547  33 D2                           xor edx, edx
00325549  48 8B CF                        mov rcx, rdi
0032554C  E8 7F 12 F6 FF                  call 0x1402867d0
00325551  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
00325559  0F 84 7E 01 00 00               je 0x1403256dd
0032555F  B8 0A 02 00 C0                  mov eax, 0xc000020a
00325564  E9 19 FC FF FF                  jmp 0x140325182
00325569  8B 05 E9 88 BE 00               mov eax, dword ptr [rip + 0xbe88e9]
0032556F  85 C0                           test eax, eax
00325571  0F 85 E7 FE FF FF               jne 0x14032545e
00325577  40 0F B6 D6                     movzx edx, sil
0032557B  48 8B CB                        mov rcx, rbx
0032557E  E8 ED E4 FF FF                  call 0x140323a70
00325583  E9 29 FF FF FF                  jmp 0x1403254b1
00325588  0F B6 D0                        movzx edx, al
0032558B  40 0F B6 CE                     movzx ecx, sil
0032558F  E8 68 01 1D 00                  call 0x1404f56fc
00325594  E9 B8 FE FF FF                  jmp 0x140325451
00325599  8B 05 19 15 CA 00               mov eax, dword ptr [rip + 0xca1519]
0032559F  A8 40                           test al, 0x40
003255A1  0F 84 F9 FE FF FF               je 0x1403254a0
003255A7  E8 E4 9E FE FF                  call 0x14030f490
003255AC  84 C0                           test al, al
003255AE  0F 84 EC FE FF FF               je 0x1403254a0
003255B4  8B CF                           mov ecx, edi
003255B6  E8 A5 9E FE FF                  call 0x14030f460
003255BB  E9 E2 FE FF FF                  jmp 0x1403254a2
003255C0  48 8B CE                        mov rcx, rsi
003255C3  E8 18 07 00 00                  call 0x140325ce0
003255C8  4C 3B E8                        cmp r13, rax
003255CB  0F 85 12 FF FF FF               jne 0x1403254e3
003255D1  44 0F B6 BC 24 B0 00 00 00      movzx r15d, byte ptr [rsp + 0xb0]
003255DA  E9 E3 FA FF FF                  jmp 0x1403250c2
003255DF  41 8B 46 2C                     mov eax, dword ptr [r14 + 0x2c]
003255E3  41 8B 4E 34                     mov ecx, dword ptr [r14 + 0x34]
003255E7  81 E1 FF FF FF 3F               and ecx, 0x3fffffff
003255ED  2B C1                           sub eax, ecx
003255EF  4C 3B E8                        cmp r13, rax
003255F2  0F 85 EB FE FF FF               jne 0x1403254e3
003255F8  44 0F B6 BC 24 B0 00 00 00      movzx r15d, byte ptr [rsp + 0xb0]
00325601  E9 BC FA FF FF                  jmp 0x1403250c2
00325606  48 8D 4E 48                     lea rcx, [rsi + 0x48]
0032560A  C7 84 24 A8 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xa8], 1
00325615  E8 76 30 F2 FF                  call 0x140248690
0032561A  44 0F B6 F8                     movzx r15d, al
0032561E  88 84 24 B0 00 00 00            mov byte ptr [rsp + 0xb0], al
00325625  E9 8D FA FF FF                  jmp 0x1403250b7
0032562A  33 C0                           xor eax, eax
0032562C  E9 CD FB FF FF                  jmp 0x1403251fe
00325631  41 0F BA E4 08                  bt r12d, 8
00325636  0F 82 D5 FB FF FF               jb 0x140325211
0032563C  FF 05 4E AA B0 00               inc dword ptr [rip + 0xb0aa4e]
00325642  33 C0                           xor eax, eax
00325644  E9 07 FC FF FF                  jmp 0x140325250
00325649  48 85 ED                        test rbp, rbp
0032564C  0F 84 3A C5 3B 00               je 0x1406e1b8c
00325652  45 33 C0                        xor r8d, r8d
00325655  49 8B D5                        mov rdx, r13
00325658  48 8B CE                        mov rcx, rsi
0032565B  E8 50 18 F6 FF                  call 0x140286eb0
00325660  85 C0                           test eax, eax
00325662  0F 85 24 C5 3B 00               jne 0x1406e1b8c
00325668  4D 8B CD                        mov r9, r13
0032566B  44 8B C7                        mov r8d, edi
0032566E  33 D2                           xor edx, edx
00325670  48 8B CE                        mov rcx, rsi
00325673  E8 58 11 F6 FF                  call 0x1402867d0
00325678  41 BF 2D 01 00 C0               mov r15d, 0xc000012d
0032567E  E9 7B FC FF FF                  jmp 0x1403252fe
00325683  0F B6 94 24 B0 00 00 00         movzx edx, byte ptr [rsp + 0xb0]
0032568B  48 8D 4E 48                     lea rcx, [rsi + 0x48]
0032568F  E8 2C 2C F2 FF                  call 0x1402482c0
00325694  E9 27 FD FF FF                  jmp 0x1403253c0
00325699  41 B9 03 00 00 00               mov r9d, 3
0032569F  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
003256A4  E9 27 C5 3B 00                  jmp 0x1406e1bd0
003256A9  41 B9 02 00 00 00               mov r9d, 2
003256AF  E9 1C C5 3B 00                  jmp 0x1406e1bd0
003256B4  0F B6 94 24 B0 00 00 00         movzx edx, byte ptr [rsp + 0xb0]
003256BC  48 8D 4E 48                     lea rcx, [rsi + 0x48]
003256C0  E8 FB 2B F2 FF                  call 0x1402482c0
003256C5  E9 B6 FA FF FF                  jmp 0x140325180
003256CA  45 33 C0                        xor r8d, r8d
003256CD  49 8B D5                        mov rdx, r13
003256D0  48 8B CF                        mov rcx, rdi
003256D3  E8 38 2D F2 FF                  call 0x140248410
003256D8  E9 54 FE FF FF                  jmp 0x140325531
003256DD  48 8B CB                        mov rcx, rbx
003256E0  E8 AB 2F F2 FF                  call 0x140248690
003256E5  E9 75 FE FF FF                  jmp 0x14032555f
003256EA  48 8B CB                        mov rcx, rbx
003256ED  E8 9E 2F F2 FF                  call 0x140248690
003256F2  E9 15 FC FF FF                  jmp 0x14032530c
003256F7  41 0F B6 D7                     movzx edx, r15b
003256FB  48 8D 4E 48                     lea rcx, [rsi + 0x48]
003256FF  E8 BC 2B F2 FF                  call 0x1402482c0
00325704  0F B7 46 3C                     movzx eax, word ptr [rsi + 0x3c]
00325708  4D 8B C5                        mov r8, r13
0032570B  48 8B 0D 76 A9 B0 00            mov rcx, qword ptr [rip + 0xb0a976]
00325712  25 FF 03 00 00                  and eax, 0x3ff
00325717  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
0032571E  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00325722  E8 F5 4E 19 00                  call 0x1404ba61c
00325727  83 BC 24 A8 00 00 00 00         cmp dword ptr [rsp + 0xa8], 0
0032572F  0F 85 AB C4 3B 00               jne 0x1406e1be0
00325735  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00325739  E8 52 2F F2 FF                  call 0x140248690
0032573E  90                              nop
0032573F  E9 9C C4 3B 00                  jmp 0x1406e1be0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReferenceActiveSubsection(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pA8;
    unsigned __int8 v_stack_pB0;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (88);
    result = 0;
    v_r13 = 0;
    v_stack_p10 = 0;
    v_stack_m68 = *(unsigned __int64 *)(a1);
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64) != 0) ? 1 : 0;
    v_stack_p8 = (unsigned int)(result);
    if (a3 == 17) goto loc_00325606;
loc_003250B7:
    v_stack_m60 = 2;
loc_003250C2:
    if ((*(unsigned __int64 *)(a1 + 8)) == 0) goto loc_00325261;
    if ((((unsigned __int8)((unsigned int)(a2))) & (8)) != 0) goto loc_00325194;
loc_003250E1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) != 0) goto loc_0032515F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64)) == 0) goto loc_0032515F;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56));
    v_rsi = *(unsigned __int64 *)(a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64)) < 0) {
        result = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int16 *)(result + 60);
        result = *(unsigned __int64 *)(v_rip + 11579259);
        a1 = (unsigned int)((a1) & (0x3FFULL));
        v_rsi = *(unsigned __int64 *)(result + a1 * 8);
        a1 = v_rsi + 1728;
        result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, a2, a3, 2);
        a1 = a1;
        result = MiUnlinkUnusedSubsection(a1, a2, a3, 2);
        a1 = v_rsi + 1728;
        result = ExReleaseSpinLockExclusiveFromDpcLevel(a1, a2, a3, 2);
        a4 = v_stack_m60;
        v_rsi = v_stack_m68;
    }
    if (condition_is_below) goto loc_0032515F;
    if (((*(unsigned __int64 *)(a1 + 80)) & (a1)) == 0) goto loc_0032540C;
loc_0032515F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64) != 0) goto loc_00325314;
loc_00325168:
    if (((unsigned int)(a4)) == 2) goto loc_0032532F;
loc_00325172:
    if (v_stack_p10 != 0) goto loc_003256B4;
loc_00325180:
    result = 0;
loc_00325182:
    v_rsp = (v_rsp) + (88);
    return result;
loc_00325194:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62))) & (12)) != 0) goto loc_003250E1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64) != 0) goto loc_003251B5;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1) + 92)) & (0x10000ULL)) != 0) goto loc_003250E1;
loc_003251B5:
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60)) & (0x3FFULL));
    if (sign_flag) goto loc_00325392;
    if ((((unsigned __int8)((unsigned int)(a2))) & (16)) != 0) goto loc_0032562A;
loc_003251FE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11579022) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11579080) + result * 8))) goto loc_003250E1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62))) & (1)) != 0) goto loc_00325631;
loc_00325211:
    result = MiGetSubsectionHoldingCrossPartitionReferences(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11579080) + result * 8), *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62), a4);
    result = MiGetSubsectionHoldingCrossPartitionReferences(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11579080) + result * 8), *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62), a4);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0x3FFFFFFFULL));
    if (a2 == 0x3FFFFFFFULL) goto loc_003250E1;
    if (a2 != 0) goto loc_003256A9;
    if ((((unsigned __int8)((unsigned int)(a2))) & (32)) != 0) goto loc_00325699;
loc_00325250:
    if (1 == 0) goto loc_003253B2;
loc_00325261:
    if ((((unsigned __int8)((unsigned int)(a2))) & (32)) != 0) goto loc_003256F7;
    result = MiComputeCrossPartitionSectionCharges(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62), a4);
    if (result == 0) goto loc_0032542A;
    if (((unsigned __int8)(v_stack_pB0)) == 17) goto loc_0032539E;
    if (((*(unsigned __int8 *)(v_rip + 13244530)) & (1)) != 0) goto loc_003253CA;
loc_0032529A:
    *(unsigned int *)(v_rsi + 72) = 0;
loc_003252A0:
    if ((*(unsigned int *)(v_rip + 13245049)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_pB0);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62), a4);
    }
loc_003252BE:
    v_rdi = 0;
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64) != 0) ? 1 : 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60)) & (0x3FFULL));
    a2 = 0;
    result = MiGetCrossPartitionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8), a2, (unsigned int)((unsigned int)(v_rdi)), result);
    if (!sign_flag) goto loc_00325649;
loc_003252FE:
    if (v_stack_pA8 == 0) goto loc_003256EA;
loc_0032530C:
    goto loc_00325182;
loc_00325314:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 56)))) & (32)) != 0) goto loc_00325168;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) | (1));
    *(unsigned int *)(a1 + 32) = (unsigned int)(result);
    goto loc_00325168;
loc_0032532F:
    if ((((unsigned __int8)((unsigned int)(a2))) & (32)) == 0) goto loc_00325172;
    if (result == 0) goto loc_00325172;
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, v_stack_pB0, (unsigned int)((unsigned int)(v_rdi)), result);
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 60)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578663) + result * 8), (unsigned int)(v_stack_pA0), result, result);
    if (v_stack_pA8 != 0) goto loc_00325180;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, (unsigned int)(v_stack_pA0), result, result);
    goto loc_00325180;
loc_00325392:
    goto loc_003251FE;
loc_0032539E:
    if (((*(unsigned __int8 *)(v_rip + 13244257)) & (1)) != 0) goto loc_003253ED;
loc_003253A7:
    *(unsigned int *)(v_rsi + 72) = 0;
    goto loc_003252BE;
loc_003253B2:
    if (v_stack_pA8 != 0) goto loc_00325683;
loc_003253C0:
    goto loc_00325182;
loc_003253CA:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12487304))) != 0) goto loc_0032529A;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rsi + 72, v_stack_p98, result, result);
    goto loc_003252A0;
loc_003253ED:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12487269))) != 0) goto loc_003253A7;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rsi + 72, v_stack_p98, result, result);
    goto loc_003252BE;
loc_0032540C:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x42000ULL), (unsigned int)((unsigned int)(result)), a4);
loc_0032542A:
    v_r12 = (unsigned int)(((unsigned int)(a2)) | (32));
    goto loc_003250C2;
loc_00325606:
    v_stack_pA8 = 1;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, (unsigned int)(0x42000ULL), (unsigned int)((unsigned int)(result)), a4);
    v_stack_pB0 = (unsigned __int8)(result);
    goto loc_003250B7;
loc_0032562A:
    result = 0;
    goto loc_003251FE;
loc_00325631:
    if (condition_is_below) goto loc_00325211;
    result = 0;
    goto loc_00325250;
loc_00325649:
    a3 = 0;
    result = MiChargeCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8), 0, a3, a4);
    a2 = 0;
    result = MiReturnCrossPartitionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8), a2, (unsigned int)((unsigned int)(v_rdi)), result);
    goto loc_003252FE;
loc_00325683:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, v_stack_pB0, (unsigned int)((unsigned int)(v_rdi)), result);
    goto loc_003253C0;
loc_00325699:
    v_stack_p38 = 3;
loc_003256A9:
loc_003256B4:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, v_stack_pB0, (unsigned int)((unsigned int)(v_rdi)), 2);
    goto loc_00325180;
loc_003256EA:
    result = ExAcquireSpinLockExclusive(v_rsi + 72, v_stack_pB0, (unsigned int)((unsigned int)(v_rdi)), 2);
    goto loc_0032530C;
loc_003256F7:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, (unsigned __int8)((unsigned int)(0xC000012DULL)), (unsigned int)((unsigned int)(v_rdi)), 2);
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 60)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11577718) + result * 8), (unsigned int)(v_stack_pA0), result, 2);
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11578803) + a1 * 8) + 72, (unsigned int)(v_stack_pA0), result, 2);
}
```

## 5. (Beta) C Style

```c
int64_t MiReferenceActiveSubsection(void *Arg1, int32_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p8;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pA8;
    uint8_t v_stack_pB0;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (88);
    result = 0;
    local_r13 = 0;
    v_stack_p10 = 0;
    v_stack_m68 = *(uint64_t *)(arg1);
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x40);
    result = (*(uint64_t *)(*(uint64_t *)(arg1) + 0x40) != 0) ? 1 : 0;
    v_stack_p8 = (uint32_t)(result);
    if (Arg3 == 17) goto loc_00325606;
loc_003250B7:
    v_stack_m60 = 2;
loc_003250C2:
    if ((*(uint64_t *)(arg1 + 0x8)) == 0) goto loc_00325261;
    if ((((uint8_t)((uint32_t)(Arg2))) & (8)) != 0) goto loc_00325194;
loc_003250E1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) != 0) goto loc_0032515F;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x40)) == 0) goto loc_0032515F;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38));
    local_rsi = *(uint64_t *)(arg1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x40)) < 0) {
        result = *(uint64_t *)(arg1);
        Arg1 = *(uint16_t *)(result + 0x3C);
        result = *(uint64_t *)(v_rip + 0xB0AF7B);
        Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
        local_rsi = *(uint64_t *)(result + arg1 * 8);
        Arg1 = local_rsi + 1728;
        result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, Arg2, Arg3, 2);
        Arg1 = Arg1;
        result = MiUnlinkUnusedSubsection(Arg1, Arg2, Arg3, 2);
        Arg1 = local_rsi + 1728;
        result = ExReleaseSpinLockExclusiveFromDpcLevel(Arg1, Arg2, Arg3, 2);
        a4 = v_stack_m60;
        local_rsi = v_stack_m68;
    }
    if (condition_is_below) goto loc_0032515F;
    if (((*(uint64_t *)(arg1 + 0x50)) & (Arg1)) == 0) goto loc_0032540C;
loc_0032515F:
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x40) != 0) goto loc_00325314;
loc_00325168:
    if (((uint32_t)(a4)) == 2) goto loc_0032532F;
loc_00325172:
    if (v_stack_p10 != 0) goto loc_003256B4;
loc_00325180:
    result = 0;
loc_00325182:
    local_rsp = (local_rsp) + (88);
    return result;
loc_00325194:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E))) & (12)) != 0) goto loc_003250E1;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x40) != 0) goto loc_003251B5;
    if (((*(uint32_t *)(*(uint64_t *)(arg1) + 0x5C)) & (0x10000ULL)) != 0) goto loc_003250E1;
loc_003251B5:
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1) + 0x3C)) & (0x3FFULL));
    if (sign_flag) goto loc_00325392;
    if ((((uint8_t)((uint32_t)(Arg2))) & (16)) != 0) goto loc_0032562A;
loc_003251FE:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0AE8E) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8)) == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0AEC8) + result * 8))) goto loc_003250E1;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E))) & (1)) != 0) goto loc_00325631;
loc_00325211:
    result = MiGetSubsectionHoldingCrossPartitionReferences(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0AEC8) + result * 8), *(uint8_t *)(*(uint64_t *)(arg1) + 0x3E), a4);
    result = MiGetSubsectionHoldingCrossPartitionReferences(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0AEC8) + result * 8), *(uint8_t *)(*(uint64_t *)(arg1) + 0x3E), a4);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0x3FFFFFFFULL));
    if (Arg2 == 0x3FFFFFFFULL) goto loc_003250E1;
    if (Arg2 != 0) goto loc_003256A9;
    if ((((uint8_t)((uint32_t)(Arg2))) & (32)) != 0) goto loc_00325699;
loc_00325250:
    if (1 == 0) goto loc_003253B2;
loc_00325261:
    if ((((uint8_t)((uint32_t)(Arg2))) & (32)) != 0) goto loc_003256F7;
    result = MiComputeCrossPartitionSectionCharges(Arg1, Arg2, *(uint8_t *)(*(uint64_t *)(arg1) + 0x3E), a4);
    if (result == 0) goto loc_0032542A;
    if (((uint8_t)(v_stack_pB0)) == 17) goto loc_0032539E;
    if (((*(uint8_t *)(v_rip + 0xCA1872)) & (1)) != 0) goto loc_003253CA;
loc_0032529A:
    *(uint32_t *)(local_rsi + 0x48) = 0;
loc_003252A0:
    if ((*(uint32_t *)(v_rip + 0xCA1A79)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_pB0);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint8_t *)(*(uint64_t *)(arg1) + 0x3E), a4);
    }
loc_003252BE:
    local_rdi = 0;
    local_rdi = (*(uint64_t *)(*(uint64_t *)(arg1) + 0x40) != 0) ? 1 : 0;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1) + 0x3C)) & (0x3FFULL));
    Arg2 = 0;
    result = MiGetCrossPartitionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8), Arg2, (uint32_t)((uint32_t)(local_rdi)), result);
    if (!sign_flag) goto loc_00325649;
loc_003252FE:
    if (v_stack_pA8 == 0) goto loc_003256EA;
loc_0032530C:
    goto loc_00325182;
loc_00325314:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x38)))) & (32)) != 0) goto loc_00325168;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) | (1));
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)(result);
    goto loc_00325168;
loc_0032532F:
    if ((((uint8_t)((uint32_t)(Arg2))) & (32)) == 0) goto loc_00325172;
    if (result == 0) goto loc_00325172;
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, v_stack_pB0, (uint32_t)((uint32_t)(local_rdi)), result);
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 0x3C)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0AD27) + result * 8), (uint32_t)(v_stack_pA0), result, result);
    if (v_stack_pA8 != 0) goto loc_00325180;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, (uint32_t)(v_stack_pA0), result, result);
    goto loc_00325180;
loc_00325392:
    goto loc_003251FE;
loc_0032539E:
    if (((*(uint8_t *)(v_rip + 0xCA1761)) & (1)) != 0) goto loc_003253ED;
loc_003253A7:
    *(uint32_t *)(local_rsi + 0x48) = 0;
    goto loc_003252BE;
loc_003253B2:
    if (v_stack_pA8 != 0) goto loc_00325683;
loc_003253C0:
    goto loc_00325182;
loc_003253CA:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE8A88))) != 0) goto loc_0032529A;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(local_rsi + 72, v_stack_p98, result, result);
    goto loc_003252A0;
loc_003253ED:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE8A65))) != 0) goto loc_003253A7;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(local_rsi + 72, v_stack_p98, result, result);
    goto loc_003252BE;
loc_0032540C:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x42000ULL), (uint32_t)((uint32_t)(result)), a4);
loc_0032542A:
    local_r12 = (uint32_t)(((uint32_t)(Arg2)) | (32));
    goto loc_003250C2;
loc_00325606:
    v_stack_pA8 = 1;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, (uint32_t)(0x42000ULL), (uint32_t)((uint32_t)(result)), a4);
    v_stack_pB0 = (uint8_t)(result);
    goto loc_003250B7;
loc_0032562A:
    result = 0;
    goto loc_003251FE;
loc_00325631:
    if (condition_is_below) goto loc_00325211;
    result = 0;
    goto loc_00325250;
loc_00325649:
    Arg3 = 0;
    result = MiChargeCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8), 0, Arg3, a4);
    Arg2 = 0;
    result = MiReturnCrossPartitionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8), Arg2, (uint32_t)((uint32_t)(local_rdi)), result);
    goto loc_003252FE;
loc_00325683:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, v_stack_pB0, (uint32_t)((uint32_t)(local_rdi)), result);
    goto loc_003253C0;
loc_00325699:
    v_stack_p38 = 3;
loc_003256A9:
loc_003256B4:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, v_stack_pB0, (uint32_t)((uint32_t)(local_rdi)), 2);
    goto loc_00325180;
loc_003256EA:
    result = ExAcquireSpinLockExclusive(local_rsi + 72, v_stack_pB0, (uint32_t)((uint32_t)(local_rdi)), 2);
    goto loc_0032530C;
loc_003256F7:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, (uint8_t)((uint32_t)(0xC000012DULL)), (uint32_t)((uint32_t)(local_rdi)), 2);
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 0x3C)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0A976) + result * 8), (uint32_t)(v_stack_pA0), result, 2);
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0ADB3) + arg1 * 8) + 72, (uint32_t)(v_stack_pA0), result, 2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00325060&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
