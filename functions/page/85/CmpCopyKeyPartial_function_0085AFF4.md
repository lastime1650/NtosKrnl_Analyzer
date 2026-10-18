# CmpCopyKeyPartial

- RVA: `0x0085AFF4`–`0x0085B459` (길이 `1,125` bytes)
- VA: `0x000000014085AFF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006AD90`
- 디코드: `292`개 명령, `1,125/1,125` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085B095` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085B0B8` → [CmpCopyCell](CmpCopyCell_function_0085A608.md) (function, `0x0085A608`)
- `0x0085B101` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085B186` → [CmpLockTwoSecurityCachesExclusiveShared](../A4/CmpLockTwoSecurityCachesExclusiveShared_function_00A45A94.md) (function, `0x00A45A94`)
- `0x0085B195` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x0085B1D3` → [CmpGetSecurityDescriptorNodeEx](../94/CmpGetSecurityDescriptorNodeEx_function_00949268.md) (function, `0x00949268`)
- `0x0085B1E1` → [CmpUnlockTwoSecurityCaches](../A4/CmpUnlockTwoSecurityCaches_function_00A4ACD8.md) (function, `0x00A4ACD8`)
- `0x0085B239` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085B260` → [CmpCopyValue](CmpCopyValue_function_0085B798.md) (function, `0x0085B798`)
- `0x0085B28C` → [CmpAddValueToListEx](CmpAddValueToListEx_function_0085B460.md) (function, `0x0085B460`)
- `0x0085B2E0` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085B2FE` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085B31E` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085B360` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085B36A` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085B385` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085B398` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085B3A2` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085B3AC` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085B3CC` → [CmpCopyCell](CmpCopyCell_function_0085A608.md) (function, `0x0085A608`)
- `0x0085B42E` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085B43F` → [HvFreeCell](HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x0085B44F` → [HvFreeCell](HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)

### Direct callers
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD1C8`
- [CmSaveMergedKeys](../7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE272`
- [CmpLoadHiveVolatile](../7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DE7FB`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C16A`
- [CmpLightWeightPrepareAddKeyUoW](../A5/CmpLightWeightPrepareAddKeyUoW_function_00A547FC.md) at `0x00A54948`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B184CB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0085B195` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0085B428` → [sub_00B16D42](../B1/Unknown_function_00B16D42.md) (`tail-transfer`)
  - `0x0085B434` → [sub_00B16D42 + 0x5](../B1/Unknown_function_00B16D42.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085AFF4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0085AFF9  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0085AFFE  55                              push rbp
0085AFFF  56                              push rsi
0085B000  57                              push rdi
0085B001  41 54                           push r12
0085B003  41 55                           push r13
0085B005  41 56                           push r14
0085B007  41 57                           push r15
0085B009  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
0085B00E  48 81 EC 90 00 00 00            sub rsp, 0x90
0085B015  44 8B 6D 77                     mov r13d, dword ptr [rbp + 0x77]
0085B019  45 33 E4                        xor r12d, r12d
0085B01C  41 8B C4                        mov eax, r12d
0085B01F  44 89 65 EB                     mov dword ptr [rbp - 0x15], r12d
0085B023  48 8B F1                        mov rsi, rcx
0085B026  89 45 BF                        mov dword ptr [rbp - 0x41], eax
0085B029  83 C9 FF                        or ecx, 0xffffffff
0085B02C  89 45 EF                        mov dword ptr [rbp - 0x11], eax
0085B02F  89 4D 6F                        mov dword ptr [rbp + 0x6f], ecx
0085B032  49 8B D8                        mov rbx, r8
0085B035  89 4D 47                        mov dword ptr [rbp + 0x47], ecx
0085B038  44 8B F2                        mov r14d, edx
0085B03B  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
0085B03E  41 8B FC                        mov edi, r12d
0085B041  44 89 65 E7                     mov dword ptr [rbp - 0x19], r12d
0085B045  89 4D C7                        mov dword ptr [rbp - 0x39], ecx
0085B048  44 89 65 CB                     mov dword ptr [rbp - 0x35], r12d
0085B04C  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
0085B04F  44 89 65 D3                     mov dword ptr [rbp - 0x2d], r12d
0085B053  4C 89 65 F7                     mov qword ptr [rbp - 9], r12
0085B057  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
0085B05A  44 89 65 DB                     mov dword ptr [rbp - 0x25], r12d
0085B05E  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
0085B061  44 89 65 E3                     mov dword ptr [rbp - 0x1d], r12d
0085B065  89 4D BB                        mov dword ptr [rbp - 0x45], ecx
0085B068  89 4D F3                        mov dword ptr [rbp - 0xd], ecx
0085B06B  41 83 FD 02                     cmp r13d, 2
0085B06F  75 10                           jne 0x14085b081
0085B071  44 3B C9                        cmp r9d, ecx
0085B074  0F 84 75 03 00 00               je 0x14085b3ef
0085B07A  45 8B E9                        mov r13d, r9d
0085B07D  41 C1 ED 1F                     shr r13d, 0x1f
0085B081  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
0085B088  4C 8D 45 C7                     lea r8, [rbp - 0x39]
0085B08C  48 8B CE                        mov rcx, rsi
0085B08F  0F 84 CB 02 00 00               je 0x14085b360
0085B095  E8 C6 9B FF FF                  call 0x140854c60
0085B09A  48 8D 4D 6F                     lea rcx, [rbp + 0x6f]
0085B09E  4C 8B F8                        mov r15, rax
0085B0A1  8B 40 2C                        mov eax, dword ptr [rax + 0x2c]
0085B0A4  45 8B CD                        mov r9d, r13d
0085B0A7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0085B0AC  4C 8B C3                        mov r8, rbx
0085B0AF  48 8B CE                        mov rcx, rsi
0085B0B2  89 45 FF                        mov dword ptr [rbp - 1], eax
0085B0B5  41 8B D6                        mov edx, r14d
0085B0B8  E8 4B F5 FF FF                  call 0x14085a608
0085B0BD  44 8B F0                        mov r14d, eax
0085B0C0  85 C0                           test eax, eax
0085B0C2  0F 88 AC 02 00 00               js 0x14085b374
0085B0C8  44 8B 75 67                     mov r14d, dword ptr [rbp + 0x67]
0085B0CC  41 F6 C6 02                     test r14b, 2
0085B0D0  0F 84 B9 02 00 00               je 0x14085b38f
0085B0D6  41 0F B7 4F 4A                  movzx ecx, word ptr [r15 + 0x4a]
0085B0DB  89 4D 77                        mov dword ptr [rbp + 0x77], ecx
0085B0DE  85 C9                           test ecx, ecx
0085B0E0  0F 85 D0 02 00 00               jne 0x14085b3b6
0085B0E6  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085B0ED  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0085B0F1  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
0085B0F5  48 8B CB                        mov rcx, rbx
0085B0F8  41 8B D4                        mov edx, r12d
0085B0FB  0F 84 69 02 00 00               je 0x14085b36a
0085B101  E8 5A 9B FF FF                  call 0x140854c60
0085B106  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0085B109  48 8B F8                        mov rdi, rax
0085B10C  8B 45 47                        mov eax, dword ptr [rbp + 0x47]
0085B10F  41 83 C8 FF                     or r8d, 0xffffffff
0085B113  83 67 14 00                     and dword ptr [rdi + 0x14], 0
0085B117  83 67 18 00                     and dword ptr [rdi + 0x18], 0
0085B11B  89 47 30                        mov dword ptr [rdi + 0x30], eax
0085B11E  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
0085B121  66 89 47 4A                     mov word ptr [rdi + 0x4a], ax
0085B125  44 89 47 2C                     mov dword ptr [rdi + 0x2c], r8d
0085B129  44 89 47 1C                     mov dword ptr [rdi + 0x1c], r8d
0085B12D  44 89 47 20                     mov dword ptr [rdi + 0x20], r8d
0085B131  89 57 10                        mov dword ptr [rdi + 0x10], edx
0085B134  C6 47 0C 00                     mov byte ptr [rdi + 0xc], 0
0085B138  41 0F BA E6 08                  bt r14d, 8
0085B13D  73 04                           jae 0x14085b143
0085B13F  80 67 0D FC                     and byte ptr [rdi + 0xd], 0xfc
0085B143  45 84 F6                        test r14b, r14b
0085B146  79 04                           jns 0x14085b14c
0085B148  80 4F 0D 80                     or byte ptr [rdi + 0xd], 0x80
0085B14C  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
0085B151  66 83 E0 30                     and ax, 0x30
0085B155  66 89 47 02                     mov word ptr [rdi + 2], ax
0085B159  41 F6 C6 20                     test r14b, 0x20
0085B15D  74 0E                           je 0x14085b16d
0085B15F  B8 BF FF 00 00                  mov eax, 0xffbf
0085B164  66 41 23 47 02                  and ax, word ptr [r15 + 2]
0085B169  66 89 47 02                     mov word ptr [rdi + 2], ax
0085B16D  41 3B D0                        cmp edx, r8d
0085B170  75 08                           jne 0x14085b17a
0085B172  66 83 C8 0C                     or ax, 0xc
0085B176  66 89 47 02                     mov word ptr [rdi + 2], ax
0085B17A  41 F6 C6 10                     test r14b, 0x10
0085B17E  75 73                           jne 0x14085b1f3
0085B180  48 8B D6                        mov rdx, rsi
0085B183  48 8B CB                        mov rcx, rbx
0085B186  E8 09 A9 1E 00                  call 0x140a45a94
0085B18B  8B 55 FF                        mov edx, dword ptr [rbp - 1]
0085B18E  4C 8D 45 E7                     lea r8, [rbp - 0x19]
0085B192  48 8B CE                        mov rcx, rsi
0085B195  E8 C6 CE BC FF                  call 0x140428060
0085B19A  48 8B 86 60 07 00 00            mov rax, qword ptr [rsi + 0x760]
0085B1A1  45 8B CC                        mov r9d, r12d
0085B1A4  8B 4D E7                        mov ecx, dword ptr [rbp - 0x19]
0085B1A7  4C 8B C7                        mov r8, rdi
0085B1AA  48 03 C9                        add rcx, rcx
0085B1AD  41 C1 E9 1F                     shr r9d, 0x1f
0085B1B1  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
0085B1B6  48 8D 47 2C                     lea rax, [rdi + 0x2c]
0085B1BA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0085B1BF  48 83 C2 20                     add rdx, 0x20
0085B1C3  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0085B1C8  48 8B CB                        mov rcx, rbx
0085B1CB  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0085B1D0  41 8B D4                        mov edx, r12d
0085B1D3  E8 90 E0 0E 00                  call 0x140949268
0085B1D8  48 8B D6                        mov rdx, rsi
0085B1DB  48 8B CB                        mov rcx, rbx
0085B1DE  44 8B F0                        mov r14d, eax
0085B1E1  E8 F2 FA 1E 00                  call 0x140a4acd8
0085B1E6  45 85 F6                        test r14d, r14d
0085B1E9  0F 88 89 01 00 00               js 0x14085b378
0085B1EF  41 83 C8 FF                     or r8d, 0xffffffff
0085B1F3  41 F6 47 02 40                  test byte ptr [r15 + 2], 0x40
0085B1F8  0F 85 E9 01 00 00               jne 0x14085b3e7
0085B1FE  45 8B 77 24                     mov r14d, dword ptr [r15 + 0x24]
0085B202  83 67 24 00                     and dword ptr [rdi + 0x24], 0
0085B206  F6 45 67 04                     test byte ptr [rbp + 0x67], 4
0085B20A  44 89 75 77                     mov dword ptr [rbp + 0x77], r14d
0085B20E  44 89 47 28                     mov dword ptr [rdi + 0x28], r8d
0085B212  0F 84 9D 00 00 00               je 0x14085b2b5
0085B218  45 85 F6                        test r14d, r14d
0085B21B  0F 84 94 00 00 00               je 0x14085b2b5
0085B221  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
0085B228  4C 8D 45 D7                     lea r8, [rbp - 0x29]
0085B22C  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
0085B230  48 8B CE                        mov rcx, rsi
0085B233  0F 84 4C 01 00 00               je 0x14085b385
0085B239  E8 22 9A FF FF                  call 0x140854c60
0085B23E  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0085B242  45 33 FF                        xor r15d, r15d
0085B245  45 3B FE                        cmp r15d, r14d
0085B248  73 5F                           jae 0x14085b2a9
0085B24A  42 8B 14 B8                     mov edx, dword ptr [rax + r15*4]
0085B24E  48 8D 4D EB                     lea rcx, [rbp - 0x15]
0085B252  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0085B257  45 8B CD                        mov r9d, r13d
0085B25A  48 8B CE                        mov rcx, rsi
0085B25D  4C 8B C3                        mov r8, rbx
0085B260  E8 33 05 00 00                  call 0x14085b798
0085B265  44 8B F0                        mov r14d, eax
0085B268  85 C0                           test eax, eax
0085B26A  0F 88 94 01 00 00               js 0x14085b404
0085B270  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
0085B273  45 8B CD                        mov r9d, r13d
0085B276  8B 55 EB                        mov edx, dword ptr [rbp - 0x15]
0085B279  45 8B C7                        mov r8d, r15d
0085B27C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0085B280  48 8B CB                        mov rcx, rbx
0085B283  48 8D 45 EF                     lea rax, [rbp - 0x11]
0085B287  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085B28C  E8 CF 01 00 00                  call 0x14085b460
0085B291  44 8B F0                        mov r14d, eax
0085B294  85 C0                           test eax, eax
0085B296  0F 88 68 01 00 00               js 0x14085b404
0085B29C  44 8B 75 77                     mov r14d, dword ptr [rbp + 0x77]
0085B2A0  41 FF C7                        inc r15d
0085B2A3  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
0085B2A7  EB 9C                           jmp 0x14085b245
0085B2A9  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
0085B2AD  41 83 C8 FF                     or r8d, 0xffffffff
0085B2B1  48 89 47 24                     mov qword ptr [rdi + 0x24], rax
0085B2B5  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0085B2B9  45 8B F8                        mov r15d, r8d
0085B2BC  83 65 BF 00                     and dword ptr [rbp - 0x41], 0
0085B2C0  45 8B E8                        mov r13d, r8d
0085B2C3  45 33 F6                        xor r14d, r14d
0085B2C6  44 89 20                        mov dword ptr [rax], r12d
0085B2C9  45 8B E0                        mov r12d, r8d
0085B2CC  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
0085B2D3  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0085B2D7  48 8B CE                        mov rcx, rsi
0085B2DA  0F 85 CC 00 00 00               jne 0x14085b3ac
0085B2E0  E8 5B AC FF FF                  call 0x140855f40
0085B2E5  48 85 FF                        test rdi, rdi
0085B2E8  74 19                           je 0x14085b303
0085B2EA  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085B2F1  48 8D 55 CF                     lea rdx, [rbp - 0x31]
0085B2F5  48 8B CB                        mov rcx, rbx
0085B2F8  0F 85 9A 00 00 00               jne 0x14085b398
0085B2FE  E8 3D AC FF FF                  call 0x140855f40
0085B303  48 83 7D F7 00                  cmp qword ptr [rbp - 9], 0
0085B308  74 19                           je 0x14085b323
0085B30A  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
0085B311  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0085B315  48 8B CE                        mov rcx, rsi
0085B318  0F 85 84 00 00 00               jne 0x14085b3a2
0085B31E  E8 1D AC FF FF                  call 0x140855f40
0085B323  83 CE FF                        or esi, 0xffffffff
0085B326  44 3B FE                        cmp r15d, esi
0085B329  0F 85 E8 00 00 00               jne 0x14085b417
0085B32F  44 3B EE                        cmp r13d, esi
0085B332  0F 85 01 01 00 00               jne 0x14085b439
0085B338  44 3B E6                        cmp r12d, esi
0085B33B  0F 85 08 01 00 00               jne 0x14085b449
0085B341  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
0085B349  41 8B C6                        mov eax, r14d
0085B34C  48 81 C4 90 00 00 00            add rsp, 0x90
0085B353  41 5F                           pop r15
0085B355  41 5E                           pop r14
0085B357  41 5D                           pop r13
0085B359  41 5C                           pop r12
0085B35B  5F                              pop rdi
0085B35C  5E                              pop rsi
0085B35D  5D                              pop rbp
0085B35E  C3                              ret
0085B35F  CC                              int3
0085B360  E8 4B 99 FF FF                  call 0x140854cb0
0085B365  E9 30 FD FF FF                  jmp 0x14085b09a
0085B36A  E8 41 99 FF FF                  call 0x140854cb0
0085B36F  E9 92 FD FF FF                  jmp 0x14085b106
0085B374  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
0085B378  44 8B 6D 47                     mov r13d, dword ptr [rbp + 0x47]
0085B37C  44 8B 7D BB                     mov r15d, dword ptr [rbp - 0x45]
0085B380  E9 47 FF FF FF                  jmp 0x14085b2cc
0085B385  E8 26 99 FF FF                  call 0x140854cb0
0085B38A  E9 AF FE FF FF                  jmp 0x14085b23e
0085B38F  44 89 65 77                     mov dword ptr [rbp + 0x77], r12d
0085B393  E9 4E FD FF FF                  jmp 0x14085b0e6
0085B398  E8 83 18 00 00                  call 0x14085cc20
0085B39D  E9 61 FF FF FF                  jmp 0x14085b303
0085B3A2  E8 79 18 00 00                  call 0x14085cc20
0085B3A7  E9 77 FF FF FF                  jmp 0x14085b323
0085B3AC  E8 6F 18 00 00                  call 0x14085cc20
0085B3B1  E9 2F FF FF FF                  jmp 0x14085b2e5
0085B3B6  41 8B 57 30                     mov edx, dword ptr [r15 + 0x30]
0085B3BA  48 8D 45 B7                     lea rax, [rbp - 0x49]
0085B3BE  45 8B CD                        mov r9d, r13d
0085B3C1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085B3C6  4C 8B C3                        mov r8, rbx
0085B3C9  48 8B CE                        mov rcx, rsi
0085B3CC  E8 37 F2 FF FF                  call 0x14085a608
0085B3D1  44 8B F0                        mov r14d, eax
0085B3D4  85 C0                           test eax, eax
0085B3D6  78 1F                           js 0x14085b3f7
0085B3D8  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
0085B3DB  44 8B 75 67                     mov r14d, dword ptr [rbp + 0x67]
0085B3DF  89 45 47                        mov dword ptr [rbp + 0x47], eax
0085B3E2  E9 FF FC FF FF                  jmp 0x14085b0e6
0085B3E7  45 33 F6                        xor r14d, r14d
0085B3EA  E9 13 FE FF FF                  jmp 0x14085b202
0085B3EF  45 8B EC                        mov r13d, r12d
0085B3F2  E9 8A FC FF FF                  jmp 0x14085b081
0085B3F7  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
0085B3FB  44 8B 6D B7                     mov r13d, dword ptr [rbp - 0x49]
0085B3FF  E9 78 FF FF FF                  jmp 0x14085b37c
0085B404  8B 4D EF                        mov ecx, dword ptr [rbp - 0x11]
0085B407  44 8B 7D F3                     mov r15d, dword ptr [rbp - 0xd]
0085B40B  44 8B 6D 47                     mov r13d, dword ptr [rbp + 0x47]
0085B40F  89 4D BF                        mov dword ptr [rbp - 0x41], ecx
0085B412  E9 B5 FE FF FF                  jmp 0x14085b2cc
0085B417  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085B41E  4C 8D 45 DF                     lea r8, [rbp - 0x21]
0085B422  41 8B D7                        mov edx, r15d
0085B425  48 8B CB                        mov rcx, rbx
0085B428  0F 84 14 B9 2B 00               je 0x140b16d42
0085B42E  E8 2D 98 FF FF                  call 0x140854c60
0085B433  90                              nop
0085B434  E9 0E B9 2B 00                  jmp 0x140b16d47
0085B439  41 8B D5                        mov edx, r13d
0085B43C  48 8B CB                        mov rcx, rbx
0085B43F  E8 E8 F2 FF FF                  call 0x14085a72c
0085B444  E9 EF FE FF FF                  jmp 0x14085b338
0085B449  41 8B D4                        mov edx, r12d
0085B44C  48 8B CB                        mov rcx, rbx
0085B44F  E8 D8 F2 FF FF                  call 0x14085a72c
0085B454  E9 E8 FE FF FF                  jmp 0x14085b341
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCopyKeyPartial(__int64 a1, int a2, __int64 a3, int a4, unsigned __int8 a5, unsigned int a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int8 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (144);
    v_r12 = 0;
    v_stack_m54 = 0;
    v_stack_m80 = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    v_stack_m50 = 0;
    v_stack_p30 = (unsigned int)(a1);
    v_stack_p8 = (unsigned int)(a1);
    v_stack_m88 = (unsigned int)(a1);
    v_stack_m58 = 0;
    v_stack_m78 = (unsigned int)(a1);
    v_stack_m74 = 0;
    v_stack_m70 = (unsigned int)(a1);
    v_stack_m6C = 0;
    v_stack_m48 = 0;
    v_stack_m68 = (unsigned int)(a1);
    v_stack_m64 = 0;
    v_stack_m60 = (unsigned int)(a1);
    v_stack_m5C = 0;
    v_stack_m84 = (unsigned int)(a1);
    v_stack_m4C = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(a7))) != 2) goto loc_0085B081;
    if (a4 == ((unsigned int)(a1))) goto loc_0085B3EF;
    v_r13 = (unsigned int)(((unsigned int)(a4)) >> (31));
loc_0085B081:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085B360;
    result = HvpGetCellFlat(a1, a2, v_stack_m78, a4);
loc_0085B09A:
    v_stack_mA8 = a6;
    v_stack_m40 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 44)));
    result = CmpCopyCell(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_0085B374;
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) == 0) goto loc_0085B38F;
    v_stack_p38 = (unsigned int)(*(unsigned __int16 *)(result + 74));
    if ((unsigned int)(*(unsigned __int16 *)(result + 74)) != 0) goto loc_0085B3B6;
loc_0085B0E6:
    if (((*(unsigned __int8 *)(a3 + 140)) & (1)) == 0) goto loc_0085B36A;
    result = HvpGetCellFlat(a3, (unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m70, (unsigned int)((unsigned int)(v_r13)));
loc_0085B106:
    a3 = (unsigned int)((v_stack_m70) | (0xFFFFFFFFULL));
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(v_stack_p8));
    *(unsigned __int16 *)(result + 74) = (unsigned __int16)((unsigned int)(a7));
    *(unsigned int *)(result + 44) = (unsigned int)(a3);
    *(unsigned int *)(result + 28) = (unsigned int)(a3);
    *(unsigned int *)(result + 32) = (unsigned int)(a3);
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned __int8 *)(result + 12) = 0;
    if (!(condition_is_above_or_equal)) {
    }
    if (sign_flag) {
    }
    result = (unsigned __int16)((*(unsigned __int16 *)(result + 2)) & (48));
    *(unsigned __int16 *)(result + 2) = (unsigned __int16)(result);
    if ((((unsigned __int8)((unsigned int)(a5))) & (32)) != 0) {
        result = 0xFFBFULL;
        result = (unsigned __int16)((result) & (*(unsigned __int16 *)(result + 2)));
        *(unsigned __int16 *)(result + 2) = (unsigned __int16)(result);
    }
    if (((unsigned int)((unsigned int)(v_stack_p20))) == ((unsigned int)(a3))) {
        result = (unsigned __int16)((result) | (12));
        *(unsigned __int16 *)(result + 2) = (unsigned __int16)(result);
    }
    if ((((unsigned __int8)((unsigned int)(a5))) & (16)) != 0) goto loc_0085B1F3;
    result = CmpLockTwoSecurityCachesExclusiveShared(a3, a1, a3, (unsigned int)((unsigned int)(v_r13)));
    result = CmpFindSecurityCellCacheIndex(a1, (unsigned int)(v_stack_m40), v_stack_m58, (unsigned int)((unsigned int)(v_r13)));
    a1 = ((unsigned int)(v_stack_m58)) + ((unsigned int)(v_stack_m58));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) >> (31));
    v_stack_m98 = result + 44;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1888) + a1 * 8 + 8)) + (32);
    v_stack_mA0 = 0;
    v_stack_mA8 = a2;
    result = CmpGetSecurityDescriptorNodeEx(a3, (unsigned int)((unsigned int)((unsigned int)(a6))), result, a4);
    result = CmpUnlockTwoSecurityCaches(a3, a1, result, a4);
    if (sign_flag) goto loc_0085B378;
    a3 = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_0085B1F3:
    if (((*(unsigned __int8 *)(result + 2)) & (64)) != 0) goto loc_0085B3E7;
loc_0085B202:
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    *(unsigned int *)(result + 40) = (unsigned int)(a3);
    if (((a5) & (4)) == 0) goto loc_0085B2B5;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))) == 0) goto loc_0085B2B5;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085B385;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + 40)), v_stack_m68, a4);
loc_0085B23E:
    v_stack_m48 = result;
    v_r15 = 0;
loc_0085B245:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) goto loc_0085B2A9;
    v_stack_mA8 = v_stack_m54;
    result = CmpCopyValue(a1, (unsigned int)(*(unsigned int *)(result + v_r15 * 4)), a3, (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_0085B404;
    v_stack_mA0 = (unsigned int)((unsigned int)(a7));
    v_stack_mA8 = v_stack_m50;
    result = CmpAddValueToListEx(a3, (unsigned int)(v_stack_m54), 0, (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_0085B404;
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_0085B245;
loc_0085B2A9:
    a3 = (unsigned int)((0) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(result + 36) = v_stack_m50;
loc_0085B2B5:
    v_r14 = 0;
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(a6));
loc_0085B2CC:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085B3AC;
    result = HvpReleaseCellPaged(a1, v_stack_m78, a3, (unsigned int)((unsigned int)(v_r13)));
loc_0085B2E5:
    if (result == 0) goto loc_0085B303;
    if (((*(unsigned __int8 *)(a3 + 140)) & (1)) != 0) goto loc_0085B398;
    result = HvpReleaseCellPaged(a3, v_stack_m70, a3, (unsigned int)((unsigned int)(v_r13)));
loc_0085B303:
    if (v_stack_m48 == 0) goto loc_0085B323;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085B3A2;
    result = HvpReleaseCellPaged(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
loc_0085B323:
    v_rsi = (unsigned int)((a1) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)((unsigned int)(a3)))) != ((unsigned int)(v_rsi))) goto loc_0085B417;
    if (((unsigned int)((unsigned int)((unsigned int)(a3)))) != ((unsigned int)(v_rsi))) goto loc_0085B439;
loc_0085B338:
    if (((unsigned int)((unsigned int)((unsigned int)(a3)))) != ((unsigned int)(v_rsi))) goto loc_0085B449;
loc_0085B341:
    v_rsp = (v_rsp) + (144);
    return 0;
loc_0085B360:
    result = HvpGetCellPaged(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_0085B09A;
loc_0085B36A:
    result = HvpGetCellPaged(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_0085B106;
loc_0085B374:
loc_0085B378:
loc_0085B37C:
    goto loc_0085B2CC;
loc_0085B385:
    result = HvpGetCellPaged(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_0085B23E;
loc_0085B38F:
    v_stack_p38 = (unsigned int)((unsigned int)(a6));
    goto loc_0085B0E6;
loc_0085B398:
    result = HvpReleaseCellFlat(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_0085B303;
loc_0085B3A2:
    result = HvpReleaseCellFlat(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_0085B323;
loc_0085B3AC:
    result = HvpReleaseCellFlat(a1, v_stack_m68, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_0085B2E5;
loc_0085B3B6:
    v_stack_p20 = v_stack_m88;
    result = CmpCopyCell(v_rsi, (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m84) + 48)), v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    if (sign_flag) goto loc_0085B3F7;
    v_stack_p8 = (unsigned int)((unsigned int)(v_stack_m88));
    goto loc_0085B0E6;
loc_0085B3E7:
    v_r14 = 0;
    goto loc_0085B202;
loc_0085B3EF:
    goto loc_0085B081;
loc_0085B3F7:
    goto loc_0085B37C;
loc_0085B404:
    v_stack_m80 = (unsigned int)((unsigned int)(v_stack_m50));
    goto loc_0085B2CC;
loc_0085B417:
    result = HvpGetCellFlat(v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C))), v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
loc_0085B439:
    result = HvFreeCell(v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0085B338;
loc_0085B449:
    result = HvFreeCell(v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0085B341;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCopyKeyPartial(void *Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, uint8_t Arg5, uint32_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m98;
    uint8_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (144);
    local_r12 = 0;
    v_stack_m54 = 0;
    v_stack_m80 = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    v_stack_m50 = 0;
    v_stack_p30 = (uint32_t)(Arg1);
    v_stack_p8 = (uint32_t)(Arg1);
    v_stack_m88 = (uint32_t)(Arg1);
    v_stack_m58 = 0;
    v_stack_m78 = (uint32_t)(Arg1);
    v_stack_m74 = 0;
    v_stack_m70 = (uint32_t)(Arg1);
    v_stack_m6C = 0;
    v_stack_m48 = 0;
    v_stack_m68 = (uint32_t)(Arg1);
    v_stack_m64 = 0;
    v_stack_m60 = (uint32_t)(Arg1);
    v_stack_m5C = 0;
    v_stack_m84 = (uint32_t)(Arg1);
    v_stack_m4C = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(Arg7))) != 2) goto loc_0085B081;
    if (Arg4 == ((uint32_t)(Arg1))) goto loc_0085B3EF;
    local_r13 = (uint32_t)(((uint32_t)(Arg4)) >> (31));
loc_0085B081:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085B360;
    result = HvpGetCellFlat(Arg1, Arg2, v_stack_m78, Arg4);
loc_0085B09A:
    v_stack_mA8 = Arg6;
    v_stack_m40 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)));
    result = CmpCopyCell(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_0085B374;
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) == 0) goto loc_0085B38F;
    v_stack_p38 = (uint32_t)(*(uint16_t *)(result + 0x4A));
    if ((uint32_t)(*(uint16_t *)(result + 0x4A)) != 0) goto loc_0085B3B6;
loc_0085B0E6:
    if (((*(uint8_t *)(arg3 + 0x8C)) & (1)) == 0) goto loc_0085B36A;
    result = HvpGetCellFlat(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m70, (uint32_t)((uint32_t)(local_r13)));
loc_0085B106:
    Arg3 = (uint32_t)((v_stack_m70) | (0xFFFFFFFFULL));
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(v_stack_p8));
    *(uint16_t *)(result + 0x4A) = (uint16_t)((uint32_t)(Arg7));
    *(uint32_t *)(result + 0x2C) = (uint32_t)(Arg3);
    *(uint32_t *)(result + 0x1C) = (uint32_t)(Arg3);
    *(uint32_t *)(result + 0x20) = (uint32_t)(Arg3);
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint8_t *)(result + 0xC) = 0;
    if (!(condition_is_above_or_equal)) {
    }
    if (sign_flag) {
    }
    result = (uint16_t)((*(uint16_t *)(result + 0x2)) & (48));
    *(uint16_t *)(result + 0x2) = (uint16_t)(result);
    if ((((uint8_t)((uint32_t)(Arg5))) & (32)) != 0) {
        result = 0xFFBFULL;
        result = (uint16_t)((result) & (*(uint16_t *)(result + 0x2)));
        *(uint16_t *)(result + 0x2) = (uint16_t)(result);
    }
    if (((uint32_t)((uint32_t)(v_stack_p20))) == ((uint32_t)(Arg3))) {
        result = (uint16_t)((result) | (12));
        *(uint16_t *)(result + 0x2) = (uint16_t)(result);
    }
    if ((((uint8_t)((uint32_t)(Arg5))) & (16)) != 0) goto loc_0085B1F3;
    result = CmpLockTwoSecurityCachesExclusiveShared(Arg3, Arg1, Arg3, (uint32_t)((uint32_t)(local_r13)));
    result = CmpFindSecurityCellCacheIndex(Arg1, (uint32_t)(v_stack_m40), v_stack_m58, (uint32_t)((uint32_t)(local_r13)));
    Arg1 = ((uint32_t)(v_stack_m58)) + ((uint32_t)(v_stack_m58));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) >> (31));
    v_stack_m98 = result + 44;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x760) + arg1 * 8 + 0x8)) + (32);
    v_stack_mA0 = 0;
    v_stack_mA8 = Arg2;
    result = CmpGetSecurityDescriptorNodeEx(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg6))), result, Arg4);
    result = CmpUnlockTwoSecurityCaches(Arg3, Arg1, result, Arg4);
    if (sign_flag) goto loc_0085B378;
    Arg3 = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_0085B1F3:
    if (((*(uint8_t *)(result + 0x2)) & (64)) != 0) goto loc_0085B3E7;
loc_0085B202:
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    *(uint32_t *)(result + 0x28) = (uint32_t)(Arg3);
    if (((Arg5) & (4)) == 0) goto loc_0085B2B5;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))) == 0) goto loc_0085B2B5;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085B385;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + 0x28)), v_stack_m68, Arg4);
loc_0085B23E:
    v_stack_m48 = result;
    local_r15 = 0;
loc_0085B245:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) goto loc_0085B2A9;
    v_stack_mA8 = v_stack_m54;
    result = CmpCopyValue(Arg1, (uint32_t)(*(uint32_t *)(result + local_r15 * 4)), Arg3, (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_0085B404;
    v_stack_mA0 = (uint32_t)((uint32_t)(Arg7));
    v_stack_mA8 = v_stack_m50;
    result = CmpAddValueToListEx(Arg3, (uint32_t)(v_stack_m54), 0, (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_0085B404;
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_0085B245;
loc_0085B2A9:
    Arg3 = (uint32_t)((0) | (0xFFFFFFFFULL));
    *(uint64_t *)(result + 0x24) = v_stack_m50;
loc_0085B2B5:
    local_r14 = 0;
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(Arg6));
loc_0085B2CC:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085B3AC;
    result = HvpReleaseCellPaged(Arg1, v_stack_m78, Arg3, (uint32_t)((uint32_t)(local_r13)));
loc_0085B2E5:
    if (result == 0) goto loc_0085B303;
    if (((*(uint8_t *)(arg3 + 0x8C)) & (1)) != 0) goto loc_0085B398;
    result = HvpReleaseCellPaged(Arg3, v_stack_m70, Arg3, (uint32_t)((uint32_t)(local_r13)));
loc_0085B303:
    if (v_stack_m48 == 0) goto loc_0085B323;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085B3A2;
    result = HvpReleaseCellPaged(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
loc_0085B323:
    local_rsi = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)))) != ((uint32_t)(local_rsi))) goto loc_0085B417;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)))) != ((uint32_t)(local_rsi))) goto loc_0085B439;
loc_0085B338:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)))) != ((uint32_t)(local_rsi))) goto loc_0085B449;
loc_0085B341:
    local_rsp = (local_rsp) + (144);
    return 0;
loc_0085B360:
    result = HvpGetCellPaged(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_0085B09A;
loc_0085B36A:
    result = HvpGetCellPaged(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_0085B106;
loc_0085B374:
loc_0085B378:
loc_0085B37C:
    goto loc_0085B2CC;
loc_0085B385:
    result = HvpGetCellPaged(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_0085B23E;
loc_0085B38F:
    v_stack_p38 = (uint32_t)((uint32_t)(Arg6));
    goto loc_0085B0E6;
loc_0085B398:
    result = HvpReleaseCellFlat(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_0085B303;
loc_0085B3A2:
    result = HvpReleaseCellFlat(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_0085B323;
loc_0085B3AC:
    result = HvpReleaseCellFlat(Arg1, v_stack_m68, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_0085B2E5;
loc_0085B3B6:
    v_stack_p20 = v_stack_m88;
    result = CmpCopyCell(local_rsi, (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m84) + 0x30)), v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    if (sign_flag) goto loc_0085B3F7;
    v_stack_p8 = (uint32_t)((uint32_t)(v_stack_m88));
    goto loc_0085B0E6;
loc_0085B3E7:
    local_r14 = 0;
    goto loc_0085B202;
loc_0085B3EF:
    goto loc_0085B081;
loc_0085B3F7:
    goto loc_0085B37C;
loc_0085B404:
    v_stack_m80 = (uint32_t)((uint32_t)(v_stack_m50));
    goto loc_0085B2CC;
loc_0085B417:
    result = HvpGetCellFlat(v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C))), v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
loc_0085B439:
    result = HvFreeCell(v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0085B338;
loc_0085B449:
    result = HvFreeCell(v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0085B341;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg1` | `+ 0x760` | `64` | `R` |
| `Arg3` | `+ 0x8C` | `8` | `R` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085AFF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
