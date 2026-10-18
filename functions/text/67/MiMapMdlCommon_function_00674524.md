# MiMapMdlCommon

- RVA: `0x00674524`–`0x00674B6D` (길이 `1,609` bytes)
- VA: `0x0000000140674524`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7BF0`
- 디코드: `457`개 명령, `1,609/1,609` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00674674` → [MiShowBadMapper](../2F/MiShowBadMapper_function_002F1840.md) (function, `0x002F1840`)
- `0x0067468B` → [MiAssignInitialPageAttribute](../3B/MiAssignInitialPageAttribute_function_003B472C.md) (function, `0x003B472C`)
- `0x00674696` → [MiMakeProtectionPfnCompatible](../22/MiMakeProtectionPfnCompatible_function_00229CD0.md) (function, `0x00229CD0`)
- `0x006746E8` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x006746F7` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x00674712` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x006747C7` → [MiReferenceIoPages](../23/MiReferenceIoPages_function_0023C804.md) (function, `0x0023C804`)
- `0x006748C2` → [MiMapMdlWithLargePages](../4D/MiMapMdlWithLargePages_function_004D10B8.md) (function, `0x004D10B8`)
- `0x006748E5` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)
- `0x006748EC` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0067492F` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x00674940` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00674970` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x006749BF` → [MiMakeProtectionPfnCompatible](../22/MiMakeProtectionPfnCompatible_function_00229CD0.md) (function, `0x00229CD0`)
- `0x006749FE` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00674A0D` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x00674A26` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00674A42` → [MiLookupIoPageNode](../2A/MiLookupIoPageNode_function_002AC5C8.md) (function, `0x002AC5C8`)
- `0x00674A84` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00674AD4` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00674B16` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x00674B22` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00674B2E` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)

### Direct callers
- [MmMapLockedPagesWithReservedMapping](../3E/MmMapLockedPagesWithReservedMapping_function_003E8910.md) at `0x003E8AC6`
- [MmMapLockedRestartPages](../../page/7F/MmMapLockedRestartPages_function_007F9020.md) at `0x007F90B3`

### Static image references
- `0x00674618` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0067465F` → RVA `0x00E3014C` (`.data`; read)
- `0x006746DA` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x006747E1` → RVA `0x00E2DC38` (`.data`; read)
- `0x00674A99` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00674524  48 8B C4                        mov rax, rsp
00674527  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0067452B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0067452F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00674533  48 89 48 08                     mov qword ptr [rax + 8], rcx
00674537  55                              push rbp
00674538  53                              push rbx
00674539  56                              push rsi
0067453A  57                              push rdi
0067453B  41 54                           push r12
0067453D  41 55                           push r13
0067453F  41 56                           push r14
00674541  41 57                           push r15
00674543  48 8D 68 A9                     lea rbp, [rax - 0x57]
00674547  48 81 EC 88 00 00 00            sub rsp, 0x88
0067454E  44 8B 51 20                     mov r10d, dword ptr [rcx + 0x20]
00674552  45 8B F1                        mov r14d, r9d
00674555  44 8B 59 2C                     mov r11d, dword ptr [rcx + 0x2c]
00674559  41 BD FF 0F 00 00               mov r13d, 0xfff
0067455F  44 8B 49 28                     mov r9d, dword ptr [rcx + 0x28]
00674563  4C 8B E2                        mov r12, rdx
00674566  4D 03 CD                        add r9, r13
00674569  48 8B F9                        mov rdi, rcx
0067456C  33 C0                           xor eax, eax
0067456E  45 03 D3                        add r10d, r11d
00674571  4D 23 D5                        and r10, r13
00674574  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00674578  4D 03 CA                        add r9, r10
0067457B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00674585  49 C1 E9 0C                     shr r9, 0xc
00674589  0F 57 C0                        xorps xmm0, xmm0
0067458C  33 D2                           xor edx, edx
0067458E  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
00674592  49 8B CC                        mov rcx, r12
00674595  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
00674599  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
0067459D  48 C1 E1 19                     shl rcx, 0x19
006745A1  48 8B C0                        mov rax, rax
006745A4  48 C1 E0 19                     shl rax, 0x19
006745A8  48 2B C8                        sub rcx, rax
006745AB  C7 45 C3 18 00 00 00            mov dword ptr [rbp - 0x3d], 0x18
006745B2  48 C1 F9 10                     sar rcx, 0x10
006745B6  49 03 CB                        add rcx, r11
006745B9  44 8D 5A 01                     lea r11d, [rdx + 1]
006745BD  45 33 D2                        xor r10d, r10d
006745C0  48 89 4D 07                     mov qword ptr [rbp + 7], rcx
006745C4  41 8B DA                        mov ebx, r10d
006745C7  44 89 5D C7                     mov dword ptr [rbp - 0x39], r11d
006745CB  45 8B FA                        mov r15d, r10d
006745CE  41 8B F3                        mov esi, r11d
006745D1  44 0F 20 C1                     mov rcx, cr8
006745D5  48 89 4D F7                     mov qword ptr [rbp - 9], rcx
006745D9  BA FF 01 00 00                  mov edx, 0x1ff
006745DE  4D 85 E5                        test r13, r12
006745E1  75 14                           jne 0x1406745f7
006745E3  4D 85 C0                        test r8, r8
006745E6  75 0F                           jne 0x1406745f7
006745E8  4C 85 CA                        test rdx, r9
006745EB  75 0A                           jne 0x1406745f7
006745ED  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
006745F0  48 85 C2                        test rdx, rax
006745F3  41 0F 44 DB                     cmove ebx, r11d
006745F7  49 8B D2                        mov rdx, r10
006745FA  B8 02 00 00 00                  mov eax, 2
006745FF  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00674603  4D 85 C9                        test r9, r9
00674606  0F 84 95 02 00 00               je 0x1406748a1
0067460C  44 8B 65 C3                     mov r12d, dword ptr [rbp - 0x3d]
00674610  4C 8D 6F 28                     lea r13, [rdi + 0x28]
00674614  4D 8B 75 08                     mov r14, qword ptr [r13 + 8]
00674618  4C 3B 35 C1 96 7B 00            cmp r14, qword ptr [rip + 0x7b96c1]
0067461F  0F 87 89 00 00 00               ja 0x1406746ae
00674625  4B 8D 0C 76                     lea rcx, [r14 + r14*2]
00674629  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00674633  48 03 C9                        add rcx, rcx
00674636  48 8B C0                        mov rax, rax
00674639  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0067463D  48 C1 E8 36                     shr rax, 0x36
00674641  41 85 C3                        test r11d, eax
00674644  74 5F                           je 0x1406746a5
00674646  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00674650  48 8B C0                        mov rax, rax
00674653  48 8D 3C C8                     lea rdi, [rax + rcx*8]
00674657  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0067465A  66 85 C0                        test ax, ax
0067465D  75 1A                           jne 0x140674679
0067465F  44 39 15 E6 BA 7B 00            cmp dword ptr [rip + 0x7bbae6], r10d
00674666  75 11                           jne 0x140674679
00674668  BA 02 00 00 00                  mov edx, 2
0067466D  49 8B CE                        mov rcx, r14
00674670  44 8D 42 01                     lea r8d, [rdx + 1]
00674674  E8 C7 D1 C7 FF                  call 0x1402f1840
00674679  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0067467C  C1 E8 10                        shr eax, 0x10
0067467F  24 C0                           and al, 0xc0
00674681  3C C0                           cmp al, 0xc0
00674683  75 0B                           jne 0x140674690
00674685  8B 55 7F                        mov edx, dword ptr [rbp + 0x7f]
00674688  48 8B CF                        mov rcx, rdi
0067468B  E8 9C 00 D4 FF                  call 0x1403b472c
00674690  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
00674693  48 8B D7                        mov rdx, rdi
00674696  E8 35 56 BB FF                  call 0x140229cd0
0067469B  8B D0                           mov edx, eax
0067469D  45 33 D2                        xor r10d, r10d
006746A0  E9 8A 01 00 00                  jmp 0x14067482f
006746A5  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
006746A9  B8 02 00 00 00                  mov eax, 2
006746AE  4D 85 FF                        test r15, r15
006746B1  0F 85 2A 01 00 00               jne 0x1406747e1
006746B7  44 39 55 F3                     cmp dword ptr [rbp - 0xd], r10d
006746BB  74 0C                           je 0x1406746c9
006746BD  4C 3B 75 DF                     cmp r14, qword ptr [rbp - 0x21]
006746C1  72 06                           jb 0x1406746c9
006746C3  4C 3B 75 E7                     cmp r14, qword ptr [rbp - 0x19]
006746C7  76 61                           jbe 0x14067472a
006746C9  3A C8                           cmp cl, al
006746CB  75 05                           jne 0x1406746d2
006746CD  40 B7 11                        mov dil, 0x11
006746D0  EB 1E                           jmp 0x1406746f0
006746D2  44 0F 20 C7                     mov rdi, cr8
006746D6  44 0F 22 C0                     mov cr8, rax
006746DA  44 39 15 3F 26 95 00            cmp dword ptr [rip + 0x95263f], r10d
006746E1  74 0D                           je 0x1406746f0
006746E3  8A D0                           mov dl, al
006746E5  40 8A CF                        mov cl, dil
006746E8  E8 0F 10 E8 FF                  call 0x1404f56fc
006746ED  45 33 D2                        xor r10d, r10d
006746F0  49 8B D6                        mov rdx, r14
006746F3  48 8D 4D DF                     lea rcx, [rbp - 0x21]
006746F7  E8 2C 80 C3 FF                  call 0x1402ac728
006746FC  40 80 FF 11                     cmp dil, 0x11
00674700  74 20                           je 0x140674722
00674702  44 39 15 17 26 95 00            cmp dword ptr [rip + 0x952617], r10d
00674709  74 0F                           je 0x14067471a
0067470B  44 0F 20 C1                     mov rcx, cr8
0067470F  40 8A D7                        mov dl, dil
00674712  E8 81 0F E8 FF                  call 0x1404f5698
00674717  45 33 D2                        xor r10d, r10d
0067471A  40 0F B6 C7                     movzx eax, dil
0067471E  44 0F 22 C0                     mov cr8, rax
00674722  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
00674726  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
0067472A  83 7D F3 03                     cmp dword ptr [rbp - 0xd], 3
0067472E  74 08                           je 0x140674738
00674730  8B 75 EF                        mov esi, dword ptr [rbp - 0x11]
00674733  E9 DC 00 00 00                  jmp 0x140674814
00674738  41 BB 01 00 00 00               mov r11d, 1
0067473E  49 8B C1                        mov rax, r9
00674741  48 2B C2                        sub rax, rdx
00674744  45 8B FB                        mov r15d, r11d
00674747  49 3B C3                        cmp rax, r11
0067474A  76 5E                           jbe 0x1406747aa
0067474C  4C 8D 40 FF                     lea r8, [rax - 1]
00674750  49 8D 55 10                     lea rdx, [r13 + 0x10]
00674754  4D 85 C0                        test r8, r8
00674757  74 51                           je 0x1406747aa
00674759  49 BA 28 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000028
00674763  48 8B 42 F8                     mov rax, qword ptr [rdx - 8]
00674767  48 8B 0A                        mov rcx, qword ptr [rdx]
0067476A  49 03 C3                        add rax, r11
0067476D  48 3B C8                        cmp rcx, rax
00674770  75 35                           jne 0x1406747a7
00674772  48 F7 C1 FF 01 00 00            test rcx, 0x1ff
00674779  74 2C                           je 0x1406747a7
0067477B  48 3B 0D 5E 95 7B 00            cmp rcx, qword ptr [rip + 0x7b955e]
00674782  77 17                           ja 0x14067479b
00674784  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00674788  48 03 C9                        add rcx, rcx
0067478B  49 8B C2                        mov rax, r10
0067478E  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00674792  48 C1 E8 36                     shr rax, 0x36
00674796  41 85 C3                        test r11d, eax
00674799  75 0C                           jne 0x1406747a7
0067479B  4D 03 FB                        add r15, r11
0067479E  48 83 C2 08                     add rdx, 8
006747A2  4D 2B C3                        sub r8, r11
006747A5  75 BC                           jne 0x140674763
006747A7  45 33 D2                        xor r10d, r10d
006747AA  8B 7D 7F                        mov edi, dword ptr [rbp + 0x7f]
006747AD  48 8D 45 FF                     lea rax, [rbp - 1]
006747B1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006747B6  44 8B CF                        mov r9d, edi
006747B9  4D 8B C7                        mov r8, r15
006747BC  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
006747C1  49 8B D6                        mov rdx, r14
006747C4  41 8B CB                        mov ecx, r11d
006747C7  E8 38 80 BC FF                  call 0x14023c804
006747CC  45 33 D2                        xor r10d, r10d
006747CF  45 8D 5A 01                     lea r11d, [r10 + 1]
006747D3  85 C0                           test eax, eax
006747D5  79 0A                           jns 0x1406747e1
006747D7  41 8B DA                        mov ebx, r10d
006747DA  8B F7                           mov esi, edi
006747DC  45 8B FB                        mov r15d, r11d
006747DF  EB 30                           jmp 0x140674811
006747E1  8A 0D 51 94 7B 00               mov cl, byte ptr [rip + 0x7b9451]
006747E7  49 8B C3                        mov rax, r11
006747EA  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
006747EE  80 C1 F4                        add cl, 0xf4
006747F1  48 D3 E0                        shl rax, cl
006747F4  41 2B C3                        sub eax, r11d
006747F7  41 23 C6                        and eax, r14d
006747FA  2B 46 18                        sub eax, dword ptr [rsi + 0x18]
006747FD  03 C0                           add eax, eax
006747FF  8B C8                           mov ecx, eax
00674801  48 C1 E8 05                     shr rax, 5
00674805  83 E1 1F                        and ecx, 0x1f
00674808  8B 74 86 2C                     mov esi, dword ptr [rsi + rax*4 + 0x2c]
0067480C  D3 EE                           shr esi, cl
0067480E  83 E6 03                        and esi, 3
00674811  4D 2B FB                        sub r15, r11
00674814  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
00674817  83 E2 07                        and edx, 7
0067481A  85 F6                           test esi, esi
0067481C  74 0E                           je 0x14067482c
0067481E  B8 02 00 00 00                  mov eax, 2
00674823  3B F0                           cmp esi, eax
00674825  75 08                           jne 0x14067482f
00674827  83 CA 18                        or edx, 0x18
0067482A  EB 03                           jmp 0x14067482f
0067482C  83 CA 10                        or edx, 0x10
0067482F  41 BB 01 00 00 00               mov r11d, 1
00674835  85 DB                           test ebx, ebx
00674837  74 33                           je 0x14067486c
00674839  B8 FF 01 00 00                  mov eax, 0x1ff
0067483E  48 85 45 CF                     test qword ptr [rbp - 0x31], rax
00674842  75 0B                           jne 0x14067484f
00674844  4C 85 F0                        test rax, r14
00674847  89 75 C7                        mov dword ptr [rbp - 0x39], esi
0067484A  44 8B E2                        mov r12d, edx
0067484D  EB 19                           jmp 0x140674868
0067484F  49 8B 45 00                     mov rax, qword ptr [r13]
00674853  49 03 C3                        add rax, r11
00674856  4C 3B F0                        cmp r14, rax
00674859  75 05                           jne 0x140674860
0067485B  41 3B D4                        cmp edx, r12d
0067485E  74 05                           je 0x140674865
00674860  41 8B DA                        mov ebx, r10d
00674863  EB 07                           jmp 0x14067486c
00674865  3B 75 C7                        cmp esi, dword ptr [rbp - 0x39]
00674868  41 0F 45 DA                     cmovne ebx, r10d
0067486C  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00674870  49 83 C5 08                     add r13, 8
00674874  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
00674878  49 03 D3                        add rdx, r11
0067487B  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
0067487F  B8 02 00 00 00                  mov eax, 2
00674884  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00674888  49 3B D1                        cmp rdx, r9
0067488B  0F 82 83 FD FF FF               jb 0x140674614
00674891  48 8B 7D 5F                     mov rdi, qword ptr [rbp + 0x5f]
00674895  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
00674899  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
0067489D  44 8B 75 77                     mov r14d, dword ptr [rbp + 0x77]
006748A1  44 89 55 F3                     mov dword ptr [rbp - 0xd], r10d
006748A5  85 DB                           test ebx, ebx
006748A7  74 23                           je 0x1406748cc
006748A9  48 8D 45 DF                     lea rax, [rbp - 0x21]
006748AD  45 8B CE                        mov r9d, r14d
006748B0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006748B5  49 8B D4                        mov rdx, r12
006748B8  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
006748BB  48 8B CF                        mov rcx, rdi
006748BE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006748C2  E8 F1 C7 E5 FF                  call 0x1404d10b8
006748C7  E9 6B 02 00 00                  jmp 0x140674b37
006748CC  49 8B FA                        mov rdi, r10
006748CF  45 8B F2                        mov r14d, r10d
006748D2  4D 85 C0                        test r8, r8
006748D5  74 22                           je 0x1406748f9
006748D7  3A C8                           cmp cl, al
006748D9  45 8B E3                        mov r12d, r11d
006748DC  49 8B C8                        mov rcx, r8
006748DF  75 0B                           jne 0x1406748ec
006748E1  C6 45 BF 11                     mov byte ptr [rbp - 0x41], 0x11
006748E5  E8 8A 4C BC FF                  call 0x140239574
006748EA  EB 08                           jmp 0x1406748f4
006748EC  E8 FF 82 C0 FF                  call 0x14027cbf0
006748F1  88 45 BF                        mov byte ptr [rbp - 0x41], al
006748F4  45 33 D2                        xor r10d, r10d
006748F7  EB 07                           jmp 0x140674900
006748F9  45 8B E2                        mov r12d, r10d
006748FC  C6 45 BF 11                     mov byte ptr [rbp - 0x41], 0x11
00674900  4C 8B 6D 5F                     mov r13, qword ptr [rbp + 0x5f]
00674904  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
00674908  4C 2B EE                        sub r13, rsi
0067490B  45 85 E4                        test r12d, r12d
0067490E  74 68                           je 0x140674978
00674910  48 85 FF                        test rdi, rdi
00674913  74 30                           je 0x140674945
00674915  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
0067491C  75 5A                           jne 0x140674978
0067491E  45 85 F6                        test r14d, r14d
00674921  74 16                           je 0x140674939
00674923  41 B9 02 00 00 00               mov r9d, 2
00674929  45 8B C6                        mov r8d, r14d
0067492C  48 8B D7                        mov rdx, rdi
0067492F  E8 FC EC BC FF                  call 0x140243630
00674934  33 D2                           xor edx, edx
00674936  44 8B F2                        mov r14d, edx
00674939  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
0067493D  48 8B D7                        mov rdx, rdi
00674940  E8 7B 25 BA FF                  call 0x140216ec0
00674945  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0067494F  48 8B FE                        mov rdi, rsi
00674952  48 C1 EF 09                     shr rdi, 9
00674956  48 23 F8                        and rdi, rax
00674959  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00674963  48 8B C0                        mov rax, rax
00674966  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
0067496A  48 03 F8                        add rdi, rax
0067496D  48 8B D7                        mov rdx, rdi
00674970  E8 1B 9F BC FF                  call 0x14023e890
00674975  45 33 D2                        xor r10d, r10d
00674978  4A 8B 74 2E 30                  mov rsi, qword ptr [rsi + r13 + 0x30]
0067497D  45 8B FA                        mov r15d, r10d
00674980  48 3B 35 59 93 7B 00            cmp rsi, qword ptr [rip + 0x7b9359]
00674987  77 40                           ja 0x1406749c9
00674989  48 8D 0C 76                     lea rcx, [rsi + rsi*2]
0067498D  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00674997  48 03 C9                        add rcx, rcx
0067499A  48 8B C0                        mov rax, rax
0067499D  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
006749A1  48 C1 E8 36                     shr rax, 0x36
006749A5  0F BA E0 00                     bt eax, 0
006749A9  73 1E                           jae 0x1406749c9
006749AB  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
006749B5  48 8B C0                        mov rax, rax
006749B8  48 8D 14 C8                     lea rdx, [rax + rcx*8]
006749BC  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
006749BF  E8 0C 53 BB FF                  call 0x140229cd0
006749C4  E9 A9 00 00 00                  jmp 0x140674a72
006749C9  44 39 55 F3                     cmp dword ptr [rbp - 0xd], r10d
006749CD  74 0C                           je 0x1406749db
006749CF  48 3B 75 DF                     cmp rsi, qword ptr [rbp - 0x21]
006749D3  72 06                           jb 0x1406749db
006749D5  48 3B 75 E7                     cmp rsi, qword ptr [rbp - 0x19]
006749D9  76 57                           jbe 0x140674a32
006749DB  B8 02 00 00 00                  mov eax, 2
006749E0  38 45 F7                        cmp byte ptr [rbp - 9], al
006749E3  75 04                           jne 0x1406749e9
006749E5  B3 11                           mov bl, 0x11
006749E7  EB 1D                           jmp 0x140674a06
006749E9  44 0F 20 C3                     mov rbx, cr8
006749ED  44 0F 22 C0                     mov cr8, rax
006749F1  44 39 15 28 23 95 00            cmp dword ptr [rip + 0x952328], r10d
006749F8  74 0C                           je 0x140674a06
006749FA  8A D0                           mov dl, al
006749FC  8A CB                           mov cl, bl
006749FE  E8 F9 0C E8 FF                  call 0x1404f56fc
00674A03  45 33 D2                        xor r10d, r10d
00674A06  48 8B D6                        mov rdx, rsi
00674A09  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00674A0D  E8 16 7D C3 FF                  call 0x1402ac728
00674A12  80 FB 11                        cmp bl, 0x11
00674A15  74 1B                           je 0x140674a32
00674A17  44 39 15 02 23 95 00            cmp dword ptr [rip + 0x952302], r10d
00674A1E  74 0B                           je 0x140674a2b
00674A20  44 0F 20 C1                     mov rcx, cr8
00674A24  8A D3                           mov dl, bl
00674A26  E8 6D 0C E8 FF                  call 0x1404f5698
00674A2B  0F B6 C3                        movzx eax, bl
00674A2E  44 0F 22 C0                     mov cr8, rax
00674A32  83 7D F3 03                     cmp dword ptr [rbp - 0xd], 3
00674A36  74 05                           je 0x140674a3d
00674A38  8B 4D EF                        mov ecx, dword ptr [rbp - 0x11]
00674A3B  EB 14                           jmp 0x140674a51
00674A3D  33 D2                           xor edx, edx
00674A3F  48 8B CE                        mov rcx, rsi
00674A42  E8 81 7B C3 FF                  call 0x1402ac5c8
00674A47  8B C8                           mov ecx, eax
00674A49  83 F8 03                        cmp eax, 3
00674A4C  75 09                           jne 0x140674a57
00674A4E  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00674A51  41 BF 01 00 00 00               mov r15d, 1
00674A57  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00674A5A  83 E0 07                        and eax, 7
00674A5D  85 C9                           test ecx, ecx
00674A5F  74 0E                           je 0x140674a6f
00674A61  BA 02 00 00 00                  mov edx, 2
00674A66  3B CA                           cmp ecx, edx
00674A68  75 08                           jne 0x140674a72
00674A6A  83 C8 18                        or eax, 0x18
00674A6D  EB 03                           jmp 0x140674a72
00674A6F  83 C8 10                        or eax, 0x10
00674A72  48 8B D6                        mov rdx, rsi
00674A75  0D 00 00 00 A0                  or eax, 0xa0000000
00674A7A  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
00674A7E  44 8B C0                        mov r8d, eax
00674A81  48 8B CE                        mov rcx, rsi
00674A84  E8 07 0B C5 FF                  call 0x1402c5590
00674A89  45 33 D2                        xor r10d, r10d
00674A8C  48 8B D8                        mov rbx, rax
00674A8F  45 85 FF                        test r15d, r15d
00674A92  74 05                           je 0x140674a99
00674A94  48 0F BA EB 09                  bts rbx, 9
00674A99  48 0F BA 25 E6 1F 95 00 24      bt qword ptr [rip + 0x951fe6], 0x24
00674AA2  73 38                           jae 0x140674adc
00674AA4  F6 C3 20                        test bl, 0x20
00674AA7  75 33                           jne 0x140674adc
00674AA9  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00674AB3  48 8B C0                        mov rax, rax
00674AB6  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00674AC0  48 03 C1                        add rax, rcx
00674AC3  48 3B F0                        cmp rsi, rax
00674AC6  72 14                           jb 0x140674adc
00674AC8  41 B8 80 00 00 00               mov r8d, 0x80
00674ACE  48 8B D3                        mov rdx, rbx
00674AD1  48 8B CE                        mov rcx, rsi
00674AD4  E8 A7 E2 C1 FF                  call 0x140292d80
00674AD9  45 33 D2                        xor r10d, r10d
00674ADC  B8 01 00 00 00                  mov eax, 1
00674AE1  48 89 1E                        mov qword ptr [rsi], rbx
00674AE4  48 83 C6 08                     add rsi, 8
00674AE8  44 03 F0                        add r14d, eax
00674AEB  48 29 45 D7                     sub qword ptr [rbp - 0x29], rax
00674AEF  48 89 75 67                     mov qword ptr [rbp + 0x67], rsi
00674AF3  0F 85 12 FE FF FF               jne 0x14067490b
00674AF9  44 8A 6D BF                     mov r13b, byte ptr [rbp - 0x41]
00674AFD  45 85 E4                        test r12d, r12d
00674B00  74 31                           je 0x140674b33
00674B02  48 85 FF                        test rdi, rdi
00674B05  74 20                           je 0x140674b27
00674B07  45 85 F6                        test r14d, r14d
00674B0A  74 0F                           je 0x140674b1b
00674B0C  44 8D 48 01                     lea r9d, [rax + 1]
00674B10  45 8B C6                        mov r8d, r14d
00674B13  48 8B D7                        mov rdx, rdi
00674B16  E8 15 EB BC FF                  call 0x140243630
00674B1B  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00674B1F  48 8B D7                        mov rdx, rdi
00674B22  E8 99 23 BA FF                  call 0x140216ec0
00674B27  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00674B2B  41 8A D5                        mov dl, r13b
00674B2E  E8 5D 8B C0 FF                  call 0x14027d690
00674B33  48 8B 7D 5F                     mov rdi, qword ptr [rbp + 0x5f]
00674B37  0F B7 4F 0A                     movzx ecx, word ptr [rdi + 0xa]
00674B3B  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00674B3F  66 83 C9 01                     or cx, 1
00674B43  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00674B47  66 89 4F 0A                     mov word ptr [rdi + 0xa], cx
00674B4B  F6 C1 10                        test cl, 0x10
00674B4E  74 08                           je 0x140674b58
00674B50  66 83 C9 20                     or cx, 0x20
00674B54  66 89 4F 0A                     mov word ptr [rdi + 0xa], cx
00674B58  48 81 C4 88 00 00 00            add rsp, 0x88
00674B5F  41 5F                           pop r15
00674B61  41 5E                           pop r14
00674B63  41 5D                           pop r13
00674B65  41 5C                           pop r12
00674B67  5F                              pop rdi
00674B68  5E                              pop rsi
00674B69  5B                              pop rbx
00674B6A  5D                              pop rbp
00674B6B  C3                              ret
00674B6C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMapMdlCommon(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (136);
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 40))) + ((unsigned int)(0xFFFULL));
    result = 0;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)))));
    v_r10 = (v_r10) & ((unsigned int)(0xFFFULL));
    *(unsigned __int64 *)(v_rsp - 87 - 17) = 0;
    a4 = (a4) + (v_r10);
    a4 = (a4) >> (12);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 41) = a4;
    *(unsigned __int64 *)(v_rsp - 87 - 1) = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 33) = v_xmm0;
    a1 = (0) << (25);
    result = (0) << (25);
    a1 = (a1) - (result);
    *(unsigned int *)(v_rsp - 87 - 61) = 24;
    a1 = (a1) >> (16);
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(a1 + 44)));
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 87 + 7) = a1;
    *(unsigned int *)(v_rsp - 87 - 57) = (unsigned int)(a2 + 1);
    *(unsigned __int64 *)(v_rsp - 87 - 9) = v_cr8;
    if ((((unsigned int)(0xFFFULL)) & (0)) != 0) goto loc_006745F7;
    if (a3 != 0) goto loc_006745F7;
    v_rbx = 0;
    if (((511) & (a4)) == 0) {
        result = *(unsigned int *)(a1 + 48);
        v_rbx = 0;
        if (((511) & (result)) == 0) { v_rbx = (unsigned int)(a2 + 1); }
    }
    *(unsigned __int64 *)(v_rsp - 87 - 49) = 0;
    if (a4 == 0) goto loc_006748A1;
loc_00674614:
    if ((*(unsigned __int64 *)(a1 + 40 + 8)) > (*(unsigned __int64 *)(v_rip + 8099521))) goto loc_006746AE;
    a1 = (*(unsigned __int64 *)(a1 + 40 + 8) + *(unsigned __int64 *)(a1 + 40 + 8) * 2) + (*(unsigned __int64 *)(a1 + 40 + 8) + *(unsigned __int64 *)(a1 + 40 + 8) * 2);
    result = (*(unsigned __int64 *)(2 + a1 * 8)) >> (54);
    if ((((unsigned int)(a2 + 1)) & ((unsigned int)(result))) == 0) goto loc_006746A5;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32))) != 0) goto loc_00674679;
    result = (unsigned int)(*(unsigned int *)(result + a1 * 8 + 32));
    if ((*(unsigned int *)(v_rip + 8108774)) == 0) {
        a2 = 2;
        a1 = *(unsigned __int64 *)(a1 + 40 + 8);
        a3 = a2 + 1;
        result = MiShowBadMapper(a1, a2, a3, a4);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) == 192) {
        a2 = *(unsigned int *)(v_rsp - 87 + 127);
        a1 = result + a1 * 8;
        result = MiAssignInitialPageAttribute(a1, a2, a3, a4);
    }
    result = MiMakeProtectionPfnCompatible((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119)), result + a1 * 8, a3, a4);
    v_r10 = 0;
    goto loc_0067482F;
loc_006746A5:
loc_006746AE:
    if (0 != 0) goto loc_006747E1;
    if ((*(unsigned int *)(v_rsp - 87 - 13)) == 0) goto loc_006746C9;
    if ((*(unsigned __int64 *)(a1 + 40 + 8)) < (*(unsigned __int64 *)(v_rsp - 87 - 33))) goto loc_006746C9;
    if ((*(unsigned __int64 *)(a1 + 40 + 8)) <= (*(unsigned __int64 *)(v_rsp - 87 - 25))) goto loc_0067472A;
loc_006746C9:
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 87 - 9))) != 2) goto loc_006746D2;
    goto loc_006746F0;
loc_006746D2:
    result = 2;
    if ((*(unsigned int *)(v_rip + 9774655)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
        v_r10 = 0;
    }
    result = MiIoSpaceGetBounds(v_rsp - 87 - 33, *(unsigned __int64 *)(a1 + 40 + 8), a3, a4);
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00674722;
    if ((*(unsigned int *)(v_rip + 9774615)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
        v_r10 = 0;
    }
loc_00674722:
loc_0067472A:
    if ((*(unsigned int *)(v_rsp - 87 - 13)) == 3) goto loc_00674738;
    goto loc_00674814;
loc_00674738:
    result = (*(unsigned __int64 *)(v_rsp - 87 - 41)) - (*(unsigned __int64 *)(v_rsp - 87 - 49));
    if (result <= 1) goto loc_006747AA;
    if (result - 1 == 0) goto loc_006747AA;
loc_00674763:
    result = (*(unsigned __int64 *)(a1 + 40 + 16 - 8)) + (1);
    if ((*(unsigned __int64 *)(a1 + 40 + 16)) != result) goto loc_006747A7;
    if (((*(unsigned __int64 *)(a1 + 40 + 16)) & (511)) == 0) goto loc_006747A7;
    if ((*(unsigned __int64 *)(a1 + 40 + 16)) > (*(unsigned __int64 *)(v_rip + 8099166))) goto loc_0067479B;
    a1 = (*(unsigned __int64 *)(a1 + 40 + 16) + *(unsigned __int64 *)(a1 + 40 + 16) * 2) + (*(unsigned __int64 *)(a1 + 40 + 16) + *(unsigned __int64 *)(a1 + 40 + 16) * 2);
    result = (*(unsigned __int64 *)(0 + a1 * 8)) >> (54);
    if (((1) & ((unsigned int)(result))) != 0) goto loc_006747A7;
loc_0067479B:
    v_r15 = (1) + (1);
    a2 = (a1 + 40 + 16) + (8);
    a3 = (result - 1) - (1);
    if (condition_is_not_equal) goto loc_00674763;
loc_006747A7:
    v_r10 = 0;
loc_006747AA:
    v_stack_mA0 = v_rsp - 87 - 1;
    v_stack_mA8 = 0;
    result = MiReferenceIoPages(1, *(unsigned __int64 *)(a1 + 40 + 8), v_r15, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 127)))));
    v_r10 = 0;
    if (!sign_flag) goto loc_006747E1;
    goto loc_00674811;
loc_006747E1:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 8098897)) + (244));
    result = (v_r10 + 1) << ((unsigned __int8)(a1));
    result = (unsigned int)((result) - ((unsigned int)(v_r10 + 1)));
    result = (unsigned int)((result) & ((unsigned int)(*(unsigned __int64 *)(a1 + 40 + 8))));
    result = (unsigned int)((result) - (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 87 - 1) + 24)));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    result = (result) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (31));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 87 - 1) + result * 4 + 44))) >> ((unsigned __int8)(a1)));
    v_rsi = (unsigned int)((v_rsi) & (3));
loc_00674811:
    v_r15 = ((unsigned int)((unsigned int)(v_r10 + 1))) - (v_r10 + 1);
loc_00674814:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119))) & (7));
    if ((unsigned int)(v_rsi) == 0) goto loc_0067482C;
    if (((unsigned int)(v_rsi)) != 2) goto loc_0067482F;
    a2 = (unsigned int)((a2) | (24));
    goto loc_0067482F;
loc_0067482C:
    a2 = (unsigned int)((a2) | (16));
loc_0067482F:
    if (0 == 0) goto loc_0067486C;
    if (((*(unsigned __int64 *)(v_rsp - 87 - 49)) & (511)) != 0) goto loc_0067484F;
    *(unsigned int *)(v_rsp - 87 - 57) = (unsigned int)(v_rsi);
    goto loc_00674868;
loc_0067484F:
    result = (*(unsigned __int64 *)(a1 + 40)) + (1);
    if ((*(unsigned __int64 *)(a1 + 40 + 8)) != result) goto loc_00674860;
    if (((unsigned int)(a2)) == ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00674865;
loc_00674860:
    goto loc_0067486C;
loc_00674865:
loc_00674868:
    v_rbx = 0;
    if (((unsigned int)(v_rsi)) != (*(unsigned int *)(v_rsp - 87 - 57))) { v_rbx = 0; }
loc_0067486C:
    v_r13 = (a1 + 40) + (8);
    a2 = (*(unsigned __int64 *)(v_rsp - 87 - 49)) + (1);
    *(unsigned __int64 *)(v_rsp - 87 - 49) = a2;
    if (a2 < (*(unsigned __int64 *)(v_rsp - 87 - 41))) goto loc_00674614;
loc_006748A1:
    *(unsigned int *)(v_rsp - 87 - 13) = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_006748CC;
    v_stack_mA0 = v_rsp - 87 - 33;
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 127)));
    result = MiMapMdlWithLargePages(*(unsigned __int64 *)(v_rsp - 87 + 95), *(unsigned __int64 *)(v_rsp - 87 + 103), *(unsigned __int64 *)(v_rsp - 87 + 111), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119)))));
    goto loc_00674B37;
loc_006748CC:
    if (*(unsigned __int64 *)(v_rsp - 87 + 111) == 0) goto loc_006748F9;
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 87 + 95))) != ((unsigned __int8)(result))) goto loc_006748EC;
    *(unsigned __int8 *)(v_rsp - 87 - 65) = 17;
    result = MiLockWorkingSetSharedAtDpc(*(unsigned __int64 *)(v_rsp - 87 + 111), *(unsigned __int64 *)(v_rsp - 87 + 103), *(unsigned __int64 *)(v_rsp - 87 + 111), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119)))));
    goto loc_006748F4;
loc_006748EC:
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(v_rsp - 87 + 111), *(unsigned __int64 *)(v_rsp - 87 + 103), *(unsigned __int64 *)(v_rsp - 87 + 111), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119)))));
    *(unsigned __int8 *)(v_rsp - 87 - 65) = (unsigned __int8)(result);
loc_006748F4:
    v_r10 = 0;
    goto loc_00674900;
loc_006748F9:
    *(unsigned __int8 *)(v_rsp - 87 - 65) = 17;
loc_00674900:
    v_r13 = (*(unsigned __int64 *)(v_rsp - 87 + 95)) - (*(unsigned __int64 *)(v_rsp - 87 + 103));
loc_0067490B:
    if (0 == 0) goto loc_00674978;
    if (0 == 0) goto loc_00674945;
    if (((*(unsigned __int64 *)(v_rsp - 87 + 103)) & (0xFFFULL)) != 0) goto loc_00674978;
    v_r14 = 0;
    if (0 != 0) {
        a4 = 2;
        a3 = 0;
        a2 = 0;
        result = MiIncreaseUsedPtes(*(unsigned __int64 *)(v_rsp - 87 + 111), a2, a3, a4);
        a2 = 0;
        v_r14 = 0;
    }
    result = MiUnlockPageTable(*(unsigned __int64 *)(v_rsp - 87 + 111), 0, a3, a4);
loc_00674945:
    v_rdi = (*(unsigned __int64 *)(v_rsp - 87 + 103)) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) + (result);
    result = MiLockNestedPageTable(*(unsigned __int64 *)(v_rsp - 87 + 111), v_rdi, a3, a4);
    v_r10 = 0;
loc_00674978:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48)) > (*(unsigned __int64 *)(v_rip + 8098649))) goto loc_006749C9;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48) * 2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48) * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_006749C9;
    result = MiMakeProtectionPfnCompatible((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119)), result + a1 * 8, a3, a4);
    goto loc_00674A72;
loc_006749C9:
    if ((*(unsigned int *)(v_rsp - 87 - 13)) == 0) goto loc_006749DB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48)) < (*(unsigned __int64 *)(v_rsp - 87 - 33))) goto loc_006749DB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48)) <= (*(unsigned __int64 *)(v_rsp - 87 - 25))) goto loc_00674A32;
loc_006749DB:
    if ((*(unsigned __int8 *)(v_rsp - 87 - 9)) != 2) goto loc_006749E9;
    goto loc_00674A06;
loc_006749E9:
    result = 2;
    if ((*(unsigned int *)(v_rip + 9773864)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
        v_r10 = 0;
    }
    result = MiIoSpaceGetBounds(v_rsp - 87 - 33, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48), a3, a4);
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) == 17) goto loc_00674A32;
    if ((*(unsigned int *)(v_rip + 9773826)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00674A32:
    if ((*(unsigned int *)(v_rsp - 87 - 13)) == 3) goto loc_00674A3D;
    goto loc_00674A51;
loc_00674A3D:
    a2 = 0;
    result = MiLookupIoPageNode(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48), a2, a3, a4);
    if (((unsigned int)(result)) != 3) goto loc_00674A57;
loc_00674A51:
loc_00674A57:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 87 + 119))) & (7));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 127))) == 0) goto loc_00674A6F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 87 + 127)))) != 2) goto loc_00674A72;
    result = (unsigned int)((result) | (24));
    goto loc_00674A72;
loc_00674A6F:
    result = (unsigned int)((result) | (16));
loc_00674A72:
    result = (unsigned int)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(*(unsigned __int64 *)(v_rsp - 87 + 103), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103) + v_r13 * 1 + 48), (unsigned int)((unsigned int)(result)), a4);
    v_r10 = 0;
    if (1 != 0) {
    }
    if (condition_is_above_or_equal) goto loc_00674ADC;
    if ((((unsigned __int8)(result)) & (32)) != 0) goto loc_00674ADC;
    result = (result) + (*(unsigned __int64 *)(v_rsp - 87 + 103));
    if ((*(unsigned __int64 *)(v_rsp - 87 + 103)) >= result) {
        a3 = 128;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_rsp - 87 + 103);
        result = MiCheckLinearProtectedPteAccessedBit(a1, a2, a3, a4);
        v_r10 = 0;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 103)) = result;
    v_rsi = (*(unsigned __int64 *)(v_rsp - 87 + 103)) + (8);
    v_r14 = (unsigned int)((v_r14) + (1));
    *(unsigned __int64 *)(v_rsp - 87 + 103) = v_rsi;
    if (condition_is_not_equal) goto loc_0067490B;
    if (0 == 0) goto loc_00674B33;
    if (v_rdi == 0) goto loc_00674B27;
    result = 1;
    if ((unsigned int)(v_r14) != 0) {
        a4 = 1 + 1;
        a3 = (unsigned int)(v_r14);
        a2 = v_rdi;
        result = MiIncreaseUsedPtes(a1, a2, a3, a4);
    }
    result = MiUnlockPageTable(*(unsigned __int64 *)(v_rsp - 87 + 111), v_rdi, a3, a4);
loc_00674B27:
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(v_rsp - 87 + 111), (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 87 - 65)), a3, a4);
loc_00674B33:
loc_00674B37:
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 87 + 95) + 10)) | (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 95) + 24) = *(unsigned __int64 *)(v_rsp - 87 + 7);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 87 + 95) + 10) = (unsigned __int16)(a1);
    if ((((unsigned __int8)(a1)) & (16)) != 0) {
        a1 = (unsigned __int16)((a1) | (32));
        *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 87 + 95) + 10) = (unsigned __int16)(a1);
    }
    v_rsp = (v_rsp) + (136);
    return *(unsigned __int64 *)(v_rsp - 87 + 7);
}
```

## 5. (Beta) C Style

```c
int64_t MiMapMdlCommon(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (136);
    Arg4 = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) + ((uint32_t)(0xFFFULL));
    result = 0;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)))));
    local_r10 = (local_r10) & ((uint32_t)(0xFFFULL));
    *(uint64_t *)(local_rsp - 0x57 - 0x11) = 0;
    Arg4 = (Arg4) + (local_r10);
    Arg4 = (Arg4) >> (12);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x29) = Arg4;
    *(uint64_t *)(local_rsp - 0x57 - 0x1) = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x21) = v_xmm0;
    Arg1 = (0) << (25);
    result = (0) << (25);
    Arg1 = (Arg1) - (result);
    *(uint32_t *)(local_rsp - 0x57 - 0x3D) = 24;
    Arg1 = (Arg1) >> (16);
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    local_r10 = 0;
    *(void **)(local_rsp - 0x57 + 0x7) = Arg1;
    *(uint32_t *)(local_rsp - 0x57 - 0x39) = (uint32_t)(Arg2 + 1);
    *(uint64_t *)(local_rsp - 0x57 - 0x9) = v_cr8;
    if ((((uint32_t)(0xFFFULL)) & (0)) != 0) goto loc_006745F7;
    if (Arg3 != 0) goto loc_006745F7;
    local_rbx = 0;
    if (((511) & (Arg4)) == 0) {
        result = *(uint32_t *)(arg1 + 0x30);
        local_rbx = 0;
        if (((511) & (result)) == 0) { local_rbx = (uint32_t)(Arg2 + 1); }
    }
    *(uint64_t *)(local_rsp - 0x57 - 0x31) = 0;
    if (Arg4 == 0) goto loc_006748A1;
loc_00674614:
    if ((*(uint64_t *)(arg1 + 0x28 + 0x8)) > (*(uint64_t *)(v_rip + 0x7B96C1))) goto loc_006746AE;
    Arg1 = (*(uint64_t *)(arg1 + 0x28 + 0x8) + *(uint64_t *)(arg1 + 0x28 + 0x8) * 2) + (*(uint64_t *)(arg1 + 0x28 + 0x8) + *(uint64_t *)(arg1 + 0x28 + 0x8) * 2);
    result = (*(uint64_t *)(2 + arg1 * 8)) >> (54);
    if ((((uint32_t)(Arg2 + 1)) & ((uint32_t)(result))) == 0) goto loc_006746A5;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20))) != 0) goto loc_00674679;
    result = (uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20));
    if ((*(uint32_t *)(v_rip + 0x7BBAE6)) == 0) {
        Arg2 = 2;
        Arg1 = *(uint64_t *)(arg1 + 0x28 + 0x8);
        Arg3 = Arg2 + 1;
        result = MiShowBadMapper(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) == 192) {
        Arg2 = *(uint32_t *)(local_rsp - 0x57 + 0x7F);
        Arg1 = result + Arg1 * 8;
        result = MiAssignInitialPageAttribute(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiMakeProtectionPfnCompatible((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77)), result + Arg1 * 8, Arg3, Arg4);
    local_r10 = 0;
    goto loc_0067482F;
loc_006746A5:
loc_006746AE:
    if (0 != 0) goto loc_006747E1;
    if ((*(uint32_t *)(local_rsp - 0x57 - 0xD)) == 0) goto loc_006746C9;
    if ((*(uint64_t *)(arg1 + 0x28 + 0x8)) < (*(uint64_t *)(local_rsp - 0x57 - 0x21))) goto loc_006746C9;
    if ((*(uint64_t *)(arg1 + 0x28 + 0x8)) <= (*(uint64_t *)(local_rsp - 0x57 - 0x19))) goto loc_0067472A;
loc_006746C9:
    if (((uint8_t)(*(uint64_t *)(local_rsp - 0x57 - 0x9))) != 2) goto loc_006746D2;
    goto loc_006746F0;
loc_006746D2:
    result = 2;
    if ((*(uint32_t *)(v_rip + 0x95263F)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    result = MiIoSpaceGetBounds(local_rsp - 87 - 33, *(uint64_t *)(arg1 + 0x28 + 0x8), Arg3, Arg4);
    if (((uint8_t)(v_cr8)) == 17) goto loc_00674722;
    if ((*(uint32_t *)(v_rip + 0x952617)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
loc_00674722:
loc_0067472A:
    if ((*(uint32_t *)(local_rsp - 0x57 - 0xD)) == 3) goto loc_00674738;
    goto loc_00674814;
loc_00674738:
    result = (*(uint64_t *)(local_rsp - 0x57 - 0x29)) - (*(uint64_t *)(local_rsp - 0x57 - 0x31));
    if (result <= 1) goto loc_006747AA;
    if (result - 1 == 0) goto loc_006747AA;
loc_00674763:
    result = (*(uint64_t *)(arg1 + 0x28 + 0x10 - 0x8)) + (1);
    if ((*(uint64_t *)(arg1 + 0x28 + 0x10)) != result) goto loc_006747A7;
    if (((*(uint64_t *)(arg1 + 0x28 + 0x10)) & (511)) == 0) goto loc_006747A7;
    if ((*(uint64_t *)(arg1 + 0x28 + 0x10)) > (*(uint64_t *)(v_rip + 0x7B955E))) goto loc_0067479B;
    Arg1 = (*(uint64_t *)(arg1 + 0x28 + 0x10) + *(uint64_t *)(arg1 + 0x28 + 0x10) * 2) + (*(uint64_t *)(arg1 + 0x28 + 0x10) + *(uint64_t *)(arg1 + 0x28 + 0x10) * 2);
    result = (*(uint64_t *)(0 + arg1 * 8)) >> (54);
    if (((1) & ((uint32_t)(result))) != 0) goto loc_006747A7;
loc_0067479B:
    local_r15 = (1) + (1);
    Arg2 = (Arg1 + 40 + 16) + (8);
    Arg3 = (result - 1) - (1);
    if (condition_is_not_equal) goto loc_00674763;
loc_006747A7:
    local_r10 = 0;
loc_006747AA:
    v_stack_mA0 = local_rsp - 87 - 1;
    v_stack_mA8 = 0;
    result = MiReferenceIoPages(1, *(uint64_t *)(arg1 + 0x28 + 0x8), local_r15, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x7F)))));
    local_r10 = 0;
    if (!sign_flag) goto loc_006747E1;
    goto loc_00674811;
loc_006747E1:
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0x7B9451)) + (244));
    result = (local_r10 + 1) << ((uint8_t)(Arg1));
    result = (uint32_t)((result) - ((uint32_t)(local_r10 + 1)));
    result = (uint32_t)((result) & ((uint32_t)(*(uint64_t *)(arg1 + 0x28 + 0x8))));
    result = (uint32_t)((result) - (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x57 - 0x1) + 0x18)));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    result = (result) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (31));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x57 - 0x1) + result * 4 + 0x2C))) >> ((uint8_t)(Arg1)));
    local_rsi = (uint32_t)((local_rsi) & (3));
loc_00674811:
    local_r15 = ((uint32_t)((uint32_t)(local_r10 + 1))) - (local_r10 + 1);
loc_00674814:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77))) & (7));
    if ((uint32_t)(local_rsi) == 0) goto loc_0067482C;
    if (((uint32_t)(local_rsi)) != 2) goto loc_0067482F;
    Arg2 = (uint32_t)((Arg2) | (24));
    goto loc_0067482F;
loc_0067482C:
    Arg2 = (uint32_t)((Arg2) | (16));
loc_0067482F:
    if (0 == 0) goto loc_0067486C;
    if (((*(uint64_t *)(local_rsp - 0x57 - 0x31)) & (511)) != 0) goto loc_0067484F;
    *(uint32_t *)(local_rsp - 0x57 - 0x39) = (uint32_t)(local_rsi);
    goto loc_00674868;
loc_0067484F:
    result = (*(uint64_t *)(arg1 + 0x28)) + (1);
    if ((*(uint64_t *)(arg1 + 0x28 + 0x8)) != result) goto loc_00674860;
    if (((uint32_t)(Arg2)) == ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00674865;
loc_00674860:
    goto loc_0067486C;
loc_00674865:
loc_00674868:
    local_rbx = 0;
    if (((uint32_t)(local_rsi)) != (*(uint32_t *)(local_rsp - 0x57 - 0x39))) { local_rbx = 0; }
loc_0067486C:
    local_r13 = (Arg1 + 40) + (8);
    Arg2 = (*(uint64_t *)(local_rsp - 0x57 - 0x31)) + (1);
    *(uint64_t *)(local_rsp - 0x57 - 0x31) = Arg2;
    if (Arg2 < (*(uint64_t *)(local_rsp - 0x57 - 0x29))) goto loc_00674614;
loc_006748A1:
    *(uint32_t *)(local_rsp - 0x57 - 0xD) = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_006748CC;
    v_stack_mA0 = local_rsp - 87 - 33;
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x7F)));
    result = MiMapMdlWithLargePages(*(uint64_t *)(local_rsp - 0x57 + 0x5F), *(uint64_t *)(local_rsp - 0x57 + 0x67), *(uint64_t *)(local_rsp - 0x57 + 0x6F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77)))));
    goto loc_00674B37;
loc_006748CC:
    if (*(uint64_t *)(local_rsp - 0x57 + 0x6F) == 0) goto loc_006748F9;
    if (((uint8_t)(*(uint64_t *)(local_rsp - 0x57 + 0x5F))) != ((uint8_t)(result))) goto loc_006748EC;
    *(uint8_t *)(local_rsp - 0x57 - 0x41) = 17;
    result = MiLockWorkingSetSharedAtDpc(*(uint64_t *)(local_rsp - 0x57 + 0x6F), *(uint64_t *)(local_rsp - 0x57 + 0x67), *(uint64_t *)(local_rsp - 0x57 + 0x6F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77)))));
    goto loc_006748F4;
loc_006748EC:
    result = MiLockWorkingSetShared(*(uint64_t *)(local_rsp - 0x57 + 0x6F), *(uint64_t *)(local_rsp - 0x57 + 0x67), *(uint64_t *)(local_rsp - 0x57 + 0x6F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77)))));
    *(uint8_t *)(local_rsp - 0x57 - 0x41) = (uint8_t)(result);
loc_006748F4:
    local_r10 = 0;
    goto loc_00674900;
loc_006748F9:
    *(uint8_t *)(local_rsp - 0x57 - 0x41) = 17;
loc_00674900:
    local_r13 = (*(uint64_t *)(local_rsp - 0x57 + 0x5F)) - (*(uint64_t *)(local_rsp - 0x57 + 0x67));
loc_0067490B:
    if (0 == 0) goto loc_00674978;
    if (0 == 0) goto loc_00674945;
    if (((*(uint64_t *)(local_rsp - 0x57 + 0x67)) & (0xFFFULL)) != 0) goto loc_00674978;
    local_r14 = 0;
    if (0 != 0) {
        Arg4 = 2;
        Arg3 = 0;
        Arg2 = 0;
        result = MiIncreaseUsedPtes(*(uint64_t *)(local_rsp - 0x57 + 0x6F), Arg2, Arg3, Arg4);
        Arg2 = 0;
        local_r14 = 0;
    }
    result = MiUnlockPageTable(*(uint64_t *)(local_rsp - 0x57 + 0x6F), 0, Arg3, Arg4);
loc_00674945:
    local_rdi = (*(uint64_t *)(local_rsp - 0x57 + 0x67)) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) + (result);
    result = MiLockNestedPageTable(*(uint64_t *)(local_rsp - 0x57 + 0x6F), local_rdi, Arg3, Arg4);
    local_r10 = 0;
loc_00674978:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30)) > (*(uint64_t *)(v_rip + 0x7B9359))) goto loc_006749C9;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30) * 2) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30) * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_006749C9;
    result = MiMakeProtectionPfnCompatible((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77)), result + Arg1 * 8, Arg3, Arg4);
    goto loc_00674A72;
loc_006749C9:
    if ((*(uint32_t *)(local_rsp - 0x57 - 0xD)) == 0) goto loc_006749DB;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30)) < (*(uint64_t *)(local_rsp - 0x57 - 0x21))) goto loc_006749DB;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30)) <= (*(uint64_t *)(local_rsp - 0x57 - 0x19))) goto loc_00674A32;
loc_006749DB:
    if ((*(uint8_t *)(local_rsp - 0x57 - 0x9)) != 2) goto loc_006749E9;
    goto loc_00674A06;
loc_006749E9:
    result = 2;
    if ((*(uint32_t *)(v_rip + 0x952328)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    result = MiIoSpaceGetBounds(local_rsp - 87 - 33, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30), Arg3, Arg4);
    if (((uint8_t)((uint8_t)(v_cr8))) == 17) goto loc_00674A32;
    if ((*(uint32_t *)(v_rip + 0x952302)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_00674A32:
    if ((*(uint32_t *)(local_rsp - 0x57 - 0xD)) == 3) goto loc_00674A3D;
    goto loc_00674A51;
loc_00674A3D:
    Arg2 = 0;
    result = MiLookupIoPageNode(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30), Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != 3) goto loc_00674A57;
loc_00674A51:
loc_00674A57:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x77))) & (7));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x7F))) == 0) goto loc_00674A6F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x57 + 0x7F)))) != 2) goto loc_00674A72;
    result = (uint32_t)((result) | (24));
    goto loc_00674A72;
loc_00674A6F:
    result = (uint32_t)((result) | (16));
loc_00674A72:
    result = (uint32_t)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(*(uint64_t *)(local_rsp - 0x57 + 0x67), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67) + local_r13 * 1 + 0x30), (uint32_t)((uint32_t)(result)), Arg4);
    local_r10 = 0;
    if (1 != 0) {
    }
    if (condition_is_above_or_equal) goto loc_00674ADC;
    if ((((uint8_t)(result)) & (32)) != 0) goto loc_00674ADC;
    result = (result) + (*(uint64_t *)(local_rsp - 0x57 + 0x67));
    if ((*(uint64_t *)(local_rsp - 0x57 + 0x67)) >= result) {
        Arg3 = 128;
        Arg2 = result;
        Arg1 = *(uint64_t *)(local_rsp - 0x57 + 0x67);
        result = MiCheckLinearProtectedPteAccessedBit(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x67)) = result;
    local_rsi = (*(uint64_t *)(local_rsp - 0x57 + 0x67)) + (8);
    local_r14 = (uint32_t)((local_r14) + (1));
    *(uint64_t *)(local_rsp - 0x57 + 0x67) = local_rsi;
    if (condition_is_not_equal) goto loc_0067490B;
    if (0 == 0) goto loc_00674B33;
    if (local_rdi == 0) goto loc_00674B27;
    result = 1;
    if ((uint32_t)(local_r14) != 0) {
        Arg4 = 1 + 1;
        Arg3 = (uint32_t)(local_r14);
        Arg2 = local_rdi;
        result = MiIncreaseUsedPtes(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockPageTable(*(uint64_t *)(local_rsp - 0x57 + 0x6F), local_rdi, Arg3, Arg4);
loc_00674B27:
    result = MiUnlockWorkingSetShared(*(uint64_t *)(local_rsp - 0x57 + 0x6F), (uint8_t)(*(uint8_t *)(local_rsp - 0x57 - 0x41)), Arg3, Arg4);
loc_00674B33:
loc_00674B37:
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x5F) + 0xA)) | (1));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x5F) + 0x18) = *(uint64_t *)(local_rsp - 0x57 + 0x7);
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x5F) + 0xA) = (uint16_t)(Arg1);
    if ((((uint8_t)(Arg1)) & (16)) != 0) {
        Arg1 = (uint16_t)((Arg1) | (32));
        *(uint16_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x5F) + 0xA) = (uint16_t)(Arg1);
    }
    local_rsp = (local_rsp) + (136);
    return *(uint64_t *)(local_rsp - 0x57 + 0x7);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x8` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00674524&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
