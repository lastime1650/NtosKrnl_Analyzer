# MiMakeDriverPagesPrivate

- RVA: `0x00384C60`–`0x0038513E` (길이 `1,246` bytes)
- VA: `0x0000000140384C60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007BC58`
- 디코드: `283`개 명령, `1,246/1,246` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00384CF3` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00384D90` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00384D9F` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00384DCE` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00384DE5` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00384DFD` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00384E1E` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00384E2D` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00384EBF` → [MiUseProtectedSlabAllocatorForDriverPage](MiUseProtectedSlabAllocatorForDriverPage_function_00385CB8.md) (function, `0x00385CB8`)
- `0x00384ECF` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00384EEB` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x00384EFF` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00384F0E` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00384F1D` → [MiAllocateDriverPage](../../page/A8/MiAllocateDriverPage_function_00A80128.md) (function, `0x00A80128`)
- `0x00384F2C` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00384F3B` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00384F6B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00384F94` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00384FB6` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00384FD4` → [MiCheckSlabPage](../34/MiCheckSlabPage_function_00348AC8.md) (function, `0x00348AC8`)
- `0x00385013` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x00385066` → [MiMakeDriverPageStayResident](MiMakeDriverPageStayResident_function_00385D18.md) (function, `0x00385D18`)
- `0x00385134` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)

### Direct callers
- [MiSetSystemCodeProtection](MiSetSystemCodeProtection_function_00384420.md) at `0x003844DD`
- [MiLockDriverPageRange](../67/MiLockDriverPageRange_function_00670160.md) at `0x00670540`
- [MmProtectDriverSection](../67/MmProtectDriverSection_function_00670A80.md) at `0x00670D5E`
- [sub_006E3CBA](../6E/Unknown_function_006E3CBA.md) at `0x006E3CF5`
- [MiBackSingleImageWithPagefile](../../page/7F/MiBackSingleImageWithPagefile_function_007F8664.md) at `0x007F86BE`
- [MiSplitDriverPage](../../page/7F/MiSplitDriverPage_function_007F8EB8.md) at `0x007F8F15`

### Static image references
- `0x00384C86` → RVA `0x00E37EEE` (`.data`; read)
- `0x00384C91` → RVA `0x00E30088` (`.data`; read)
- `0x00384CB2` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00384CEC` → RVA `0x00E37E40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00384F1D` → [MiAllocateDriverPage](../../page/A8/MiAllocateDriverPage_function_00A80128.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003850FC` → [sub_006E49FE](../6E/Unknown_function_006E49FE.md) (`tail-transfer`)
  - `0x00385106` → [sub_006E49FE](../6E/Unknown_function_006E49FE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00384C60  48 8B C4                        mov rax, rsp
00384C63  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00384C67  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00384C6B  48 89 48 08                     mov qword ptr [rax + 8], rcx
00384C6F  53                              push rbx
00384C70  55                              push rbp
00384C71  56                              push rsi
00384C72  57                              push rdi
00384C73  41 54                           push r12
00384C75  41 55                           push r13
00384C77  41 56                           push r14
00384C79  41 57                           push r15
00384C7B  48 83 EC 58                     sub rsp, 0x58
00384C7F  83 60 98 00                     and dword ptr [rax - 0x68], 0
00384C83  45 33 E4                        xor r12d, r12d
00384C86  44 0F B7 15 60 32 AB 00         movzx r10d, word ptr [rip + 0xab3260]
00384C8E  45 8B E9                        mov r13d, r9d
00384C91  48 8B 05 F0 B3 AA 00            mov rax, qword ptr [rip + 0xaab3f0]
00384C98  49 8B D8                        mov rbx, r8
00384C9B  41 8D 4C 24 02                  lea ecx, [r12 + 2]
00384CA0  4A 8B 04 D0                     mov rax, qword ptr [rax + r10*8]
00384CA4  45 33 D2                        xor r10d, r10d
00384CA7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00384CAC  41 F6 C1 03                     test r9b, 3
00384CB0  75 12                           jne 0x140384cc4
00384CB2  48 8B 05 CF 1D C4 00            mov rax, qword ptr [rip + 0xc41dcf]
00384CB9  48 0F BA E0 0F                  bt rax, 0xf
00384CBE  0F 82 E4 02 00 00               jb 0x140384fa8
00384CC4  41 8B CA                        mov ecx, r10d
00384CC7  41 8B C5                        mov eax, r13d
00384CCA  83 C9 01                        or ecx, 1
00384CCD  83 E0 04                        and eax, 4
00384CD0  85 C0                           test eax, eax
00384CD2  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00384CD6  48 8B FA                        mov rdi, rdx
00384CD9  41 0F 44 CA                     cmove ecx, r10d
00384CDD  33 F6                           xor esi, esi
00384CDF  48 21 74 24 40                  and qword ptr [rsp + 0x40], rsi
00384CE4  49 83 CF FF                     or r15, 0xffffffffffffffff
00384CE8  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00384CEC  48 8D 0D 4D 31 AB 00            lea rcx, [rip + 0xab314d]
00384CF3  E8 F8 7E EF FF                  call 0x14027cbf0
00384CF8  44 8A F0                        mov r14b, al
00384CFB  88 84 24 B8 00 00 00            mov byte ptr [rsp + 0xb8], al
00384D02  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00384D0C  48 BD 00 00 00 00 80 F6 FF FF   movabs rbp, 0xfffff68000000000
00384D16  48 3B FB                        cmp rdi, rbx
00384D19  0F 87 F0 00 00 00               ja 0x140384e0f
00384D1F  48 85 F6                        test rsi, rsi
00384D22  0F 84 48 02 00 00               je 0x140384f70
00384D28  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
00384D2F  0F 84 2C 02 00 00               je 0x140384f61
00384D35  48 8B 1F                        mov rbx, qword ptr [rdi]
00384D38  48 85 DB                        test rbx, rbx
00384D3B  74 34                           je 0x140384d71
00384D3D  F6 C3 01                        test bl, 1
00384D40  74 3D                           je 0x140384d7f
00384D42  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00384D4C  48 8B C3                        mov rax, rbx
00384D4F  48 C1 E8 0C                     shr rax, 0xc
00384D53  48 23 C1                        and rax, rcx
00384D56  48 8D 0C 40                     lea rcx, [rax + rax*2]
00384D5A  48 C1 E1 04                     shl rcx, 4
00384D5E  49 8B C0                        mov rax, r8
00384D61  48 03 C8                        add rcx, rax
00384D64  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00384D68  48 85 C0                        test rax, rax
00384D6B  0F 88 E0 00 00 00               js 0x140384e51
00384D71  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00384D79  48 83 C7 08                     add rdi, 8
00384D7D  EB 97                           jmp 0x140384d16
00384D7F  48 0F BA E3 0A                  bt rbx, 0xa
00384D84  73 EB                           jae 0x140384d71
00384D86  48 8B D6                        mov rdx, rsi
00384D89  48 8D 0D B0 30 AB 00            lea rcx, [rip + 0xab30b0]
00384D90  E8 2B 21 E9 FF                  call 0x140216ec0
00384D95  41 8A D6                        mov dl, r14b
00384D98  48 8D 0D A1 30 AB 00            lea rcx, [rip + 0xab30a1]
00384D9F  E8 EC 88 EF FF                  call 0x14027d690
00384DA4  48 8B EF                        mov rbp, rdi
00384DA7  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00384DB1  48 C1 E5 19                     shl rbp, 0x19
00384DB5  48 8B C0                        mov rax, rax
00384DB8  48 C1 E0 19                     shl rax, 0x19
00384DBC  45 33 C9                        xor r9d, r9d
00384DBF  48 2B E8                        sub rbp, rax
00384DC2  45 33 C0                        xor r8d, r8d
00384DC5  48 C1 FD 10                     sar rbp, 0x10
00384DC9  33 C9                           xor ecx, ecx
00384DCB  48 8B D5                        mov rdx, rbp
00384DCE  E8 AD A0 EF FF                  call 0x14027ee80
00384DD3  4C 63 F0                        movsxd r14, eax
00384DD6  85 C0                           test eax, eax
00384DD8  0F 88 16 03 00 00               js 0x1403850f4
00384DDE  48 8D 0D 5B 30 AB 00            lea rcx, [rip + 0xab305b]
00384DE5  E8 06 7E EF FF                  call 0x14027cbf0
00384DEA  45 85 F6                        test r14d, r14d
00384DED  0F 88 A2 02 00 00               js 0x140385095
00384DF3  48 8B D6                        mov rdx, rsi
00384DF6  48 8D 0D 43 30 AB 00            lea rcx, [rip + 0xab3043]
00384DFD  E8 8E 9A EB FF                  call 0x14023e890
00384E02  44 8A B4 24 B8 00 00 00         mov r14b, byte ptr [rsp + 0xb8]
00384E0A  E9 3B 01 00 00                  jmp 0x140384f4a
00384E0F  48 85 F6                        test rsi, rsi
00384E12  74 0F                           je 0x140384e23
00384E14  48 8B D6                        mov rdx, rsi
00384E17  48 8D 0D 22 30 AB 00            lea rcx, [rip + 0xab3022]
00384E1E  E8 9D 20 E9 FF                  call 0x140216ec0
00384E23  41 8A D6                        mov dl, r14b
00384E26  48 8D 0D 13 30 AB 00            lea rcx, [rip + 0xab3013]
00384E2D  E8 5E 88 EF FF                  call 0x14027d690
00384E32  49 83 FF FF                     cmp r15, -1
00384E36  0F 85 E0 02 00 00               jne 0x14038511c
00384E3C  41 8B C4                        mov eax, r12d
00384E3F  48 83 C4 58                     add rsp, 0x58
00384E43  41 5F                           pop r15
00384E45  41 5E                           pop r14
00384E47  41 5D                           pop r13
00384E49  41 5C                           pop r12
00384E4B  5F                              pop rdi
00384E4C  5E                              pop rsi
00384E4D  5D                              pop rbp
00384E4E  5B                              pop rbx
00384E4F  C3                              ret
00384E50  CC                              int3
00384E51  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00384E55  48 0F BA E0 28                  bt rax, 0x28
00384E5A  72 0D                           jb 0x140384e69
00384E5C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00384E60  48 85 C0                        test rax, rax
00384E63  0F 89 37 02 00 00               jns 0x1403850a0
00384E69  41 F6 C5 01                     test r13b, 1
00384E6D  0F 85 07 02 00 00               jne 0x14038507a
00384E73  8B 69 10                        mov ebp, dword ptr [rcx + 0x10]
00384E76  48 C1 ED 05                     shr rbp, 5
00384E7A  83 E5 1F                        and ebp, 0x1f
00384E7D  48 F7 05 00 1C C4 00 00 80 00 00  test qword ptr [rip + 0xc41c00], 0x8000
00384E88  74 0A                           je 0x140384e94
00384E8A  41 F6 C5 02                     test r13b, 2
00384E8E  0F 85 1E 02 00 00               jne 0x1403850b2
00384E94  44 39 64 24 34                  cmp dword ptr [rsp + 0x34], r12d
00384E99  0F 85 28 02 00 00               jne 0x1403850c7
00384E9F  49 83 FF FF                     cmp r15, -1
00384EA3  74 50                           je 0x140384ef5
00384EA5  4B 8D 1C 7F                     lea rbx, [r15 + r15*2]
00384EA9  48 C1 E3 04                     shl rbx, 4
00384EAD  49 8B C0                        mov rax, r8
00384EB0  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00384EB5  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00384EBA  8B D5                           mov edx, ebp
00384EBC  48 03 D8                        add rbx, rax
00384EBF  E8 F4 0D 00 00                  call 0x140385cb8
00384EC4  48 8B CB                        mov rcx, rbx
00384EC7  85 C0                           test eax, eax
00384EC9  0F 84 E7 00 00 00               je 0x140384fb6
00384ECF  E8 FC 93 F0 FF                  call 0x14028e2d0
00384ED4  83 F8 09                        cmp eax, 9
00384ED7  0F 85 EA 00 00 00               jne 0x140384fc7
00384EDD  48 39 7C 24 40                  cmp qword ptr [rsp + 0x40], rdi
00384EE2  0F 84 F9 00 00 00               je 0x140384fe1
00384EE8  48 8B CB                        mov rcx, rbx
00384EEB  E8 60 FC FA FF                  call 0x140334b50
00384EF0  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00384EF5  48 8B D6                        mov rdx, rsi
00384EF8  48 8D 0D 41 2F AB 00            lea rcx, [rip + 0xab2f41]
00384EFF  E8 BC 1F E9 FF                  call 0x140216ec0
00384F04  41 8A D6                        mov dl, r14b
00384F07  48 8D 0D 32 2F AB 00            lea rcx, [rip + 0xab2f32]
00384F0E  E8 7D 87 EF FF                  call 0x14027d690
00384F13  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00384F18  45 33 C0                        xor r8d, r8d
00384F1B  8B D5                           mov edx, ebp
00384F1D  E8 06 B2 6F 00                  call 0x140a80128
00384F22  48 8D 0D 17 2F AB 00            lea rcx, [rip + 0xab2f17]
00384F29  4C 8B F8                        mov r15, rax
00384F2C  E8 BF 7C EF FF                  call 0x14027cbf0
00384F31  48 8B D6                        mov rdx, rsi
00384F34  48 8D 0D 05 2F AB 00            lea rcx, [rip + 0xab2f05]
00384F3B  E8 50 99 EB FF                  call 0x14023e890
00384F40  49 83 FF FF                     cmp r15, -1
00384F44  0F 84 C7 01 00 00               je 0x140385111
00384F4A  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00384F54  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00384F5C  E9 AB FD FF FF                  jmp 0x140384d0c
00384F61  48 8B D6                        mov rdx, rsi
00384F64  48 8D 0D D5 2E AB 00            lea rcx, [rip + 0xab2ed5]
00384F6B  E8 50 1F E9 FF                  call 0x140216ec0
00384F70  48 8B F7                        mov rsi, rdi
00384F73  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00384F7D  48 C1 EE 09                     shr rsi, 9
00384F81  48 23 F0                        and rsi, rax
00384F84  48 8B C5                        mov rax, rbp
00384F87  48 03 F0                        add rsi, rax
00384F8A  48 8D 0D AF 2E AB 00            lea rcx, [rip + 0xab2eaf]
00384F91  48 8B D6                        mov rdx, rsi
00384F94  E8 F7 98 EB FF                  call 0x14023e890
00384F99  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00384FA3  E9 8D FD FF FF                  jmp 0x140384d35
00384FA8  48 0F BA E0 0E                  bt rax, 0xe
00384FAD  44 0F 42 D1                     cmovb r10d, ecx
00384FB1  E9 0E FD FF FF                  jmp 0x140384cc4
00384FB6  E8 15 93 F0 FF                  call 0x14028e2d0
00384FBB  83 F8 09                        cmp eax, 9
00384FBE  74 21                           je 0x140384fe1
00384FC0  BA 05 00 00 00                  mov edx, 5
00384FC5  EB 04                           jmp 0x140384fcb
00384FC7  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00384FCB  41 B8 04 00 00 00               mov r8d, 4
00384FD1  48 8B CB                        mov rcx, rbx
00384FD4  E8 EF 3A FC FF                  call 0x140348ac8
00384FD9  85 C0                           test eax, eax
00384FDB  0F 84 FC FE FF FF               je 0x140384edd
00384FE1  48 8B DF                        mov rbx, rdi
00384FE4  48 BD 00 00 00 00 80 F6 FF FF   movabs rbp, 0xfffff68000000000
00384FEE  48 C1 E3 19                     shl rbx, 0x19
00384FF2  48 8B C5                        mov rax, rbp
00384FF5  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00384FFA  4D 8B C7                        mov r8, r15
00384FFD  4C 21 64 24 20                  and qword ptr [rsp + 0x20], r12
00385002  48 8B D7                        mov rdx, rdi
00385005  48 C1 E0 19                     shl rax, 0x19
00385009  48 2B D8                        sub rbx, rax
0038500C  48 C1 FB 10                     sar rbx, 0x10
00385010  48 8B CB                        mov rcx, rbx
00385013  E8 F4 D9 FD FF                  call 0x140362a0c
00385018  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
0038501C  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00385026  48 03 C9                        add rcx, rcx
00385029  49 8B C0                        mov rax, r8
0038502C  49 83 CF FF                     or r15, 0xffffffffffffffff
00385030  48 F7 05 4D 1A C4 00 00 80 00 00  test qword ptr [rip + 0xc41a4d], 0x8000
0038503B  0F 84 30 FD FF FF               je 0x140384d71
00385041  48 8B 44 C8 28                  mov rax, qword ptr [rax + rcx*8 + 0x28]
00385046  48 C1 E8 3C                     shr rax, 0x3c
0038504A  24 07                           and al, 7
0038504C  3C 03                           cmp al, 3
0038504E  0F 85 1D FD FF FF               jne 0x140384d71
00385054  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0038505C  48 8D 15 DD 2D AB 00            lea rdx, [rip + 0xab2ddd]
00385063  4C 8B C3                        mov r8, rbx
00385066  E8 AD 0C 00 00                  call 0x140385d18
0038506B  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00385075  E9 F7 FC FF FF                  jmp 0x140384d71
0038507A  48 0F BA E3 0B                  bt rbx, 0xb
0038507F  0F 82 EC FC FF FF               jb 0x140384d71
00385085  48 0F BA E3 09                  bt rbx, 9
0038508A  0F 82 E3 FD FF FF               jb 0x140384e73
00385090  E9 DC FC FF FF                  jmp 0x140384d71
00385095  33 F6                           xor esi, esi
00385097  48 83 C7 08                     add rdi, 8
0038509B  E9 62 FD FF FF                  jmp 0x140384e02
003850A0  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003850A4  48 85 C0                        test rax, rax
003850A7  0F 85 C4 FC FF FF               jne 0x140384d71
003850AD  E9 B7 FD FF FF                  jmp 0x140384e69
003850B2  40 F6 C5 02                     test bpl, 2
003850B6  0F 84 D8 FD FF FF               je 0x140384e94
003850BC  41 BC 45 00 00 C0               mov r12d, 0xc0000045
003850C2  E9 48 FD FF FF                  jmp 0x140384e0f
003850C7  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
003850CF  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
003850D5  A8 04                           test al, 4
003850D7  0F 85 C2 FD FF FF               jne 0x140384e9f
003850DD  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
003850E0  C1 E8 18                        shr eax, 0x18
003850E3  A8 08                           test al, 8
003850E5  0F 84 B4 FD FF FF               je 0x140384e9f
003850EB  48 83 C7 08                     add rdi, 8
003850EF  E9 60 FE FF FF                  jmp 0x140384f54
003850F4  48 3B BC 24 A8 00 00 00         cmp rdi, qword ptr [rsp + 0xa8]
003850FC  0F 84 FC F8 35 00               je 0x1406e49fe
00385102  41 F6 C5 08                     test r13b, 8
00385106  0F 84 F2 F8 35 00               je 0x1406e49fe
0038510C  E9 CD FC FF FF                  jmp 0x140384dde
00385111  41 BC 17 00 00 C0               mov r12d, 0xc0000017
00385117  E9 F3 FC FF FF                  jmp 0x140384e0f
0038511C  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
00385120  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0038512A  48 C1 E1 04                     shl rcx, 4
0038512E  48 8B D0                        mov rdx, rax
00385131  48 03 CA                        add rcx, rdx
00385134  E8 A7 F9 FA FF                  call 0x140334ae0
00385139  E9 FE FC FF FF                  jmp 0x140384e3c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMakeDriverPagesPrivate(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (88);
    v_r12 = 0;
    v_r10 = 0;
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11187184) + *(unsigned __int16 *)(v_rip + 11219552) * 8);
    if ((((unsigned __int8)(a4)) & (3)) != 0) goto loc_00384CC4;
    if (condition_is_below) goto loc_00384FA8;
loc_00384CC4:
    a1 = (unsigned int)((0) | (1));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (4));
    v_stack_m64 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) { a1 = 0; }
    v_rsi = 0;
    v_r15 = (v_r15) | (-1);
    v_stack_m60 = (unsigned int)(a1);
    result = MiLockWorkingSetShared(v_rip + 11219277, a2, a3, a4);
    v_stack_p20 = (unsigned __int8)(result);
loc_00384D0C:
loc_00384D16:
    if (a2 > a3) goto loc_00384E0F;
    if (0 == 0) goto loc_00384F70;
    if (((a2) & (0xFFFULL)) == 0) goto loc_00384F61;
loc_00384D35:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00384D71;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_00384D7F;
    result = (*(unsigned __int64 *)(a2)) >> (12);
    result = (result) & (v_rip + 11219277);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (a3);
    if (sign_flag) goto loc_00384E51;
loc_00384D71:
    v_rdi = (a2) + (8);
    goto loc_00384D16;
loc_00384D7F:
    if (condition_is_above_or_equal) goto loc_00384D71;
    result = MiUnlockPageTable(v_rip + 11219120, 0, a3, a4);
    result = MiUnlockWorkingSetShared(v_rip + 11219105, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rbp = (v_rdi) << (25);
    result = (result) << (25);
    a4 = 0;
    v_rbp = (v_rbp) - (result);
    a3 = 0;
    v_rbp = (v_rbp) >> (16);
    a1 = 0;
    result = MmAccessFault(a1, v_rbp, a3, a4);
    if (sign_flag) goto loc_003850F4;
loc_00384DDE:
    result = MiLockWorkingSetShared(v_rip + 11219035, v_rbp, a3, a4);
    if (sign_flag) goto loc_00385095;
    result = MiLockNestedPageTable(v_rip + 11219011, 0, a3, a4);
loc_00384E02:
    goto loc_00384F4A;
loc_00384E0F:
    if (0 != 0) {
        a2 = 0;
        a1 = v_rip + 11218978;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(v_rip + 11218963, (unsigned __int8)(v_stack_p20), a3, a4);
    if (v_r15 != -1) goto loc_0038511C;
loc_00384E3C:
    v_rsp = (v_rsp) + (88);
    return 0;
loc_00384E51:
    if (condition_is_below) goto loc_00384E69;
    if (!sign_flag) goto loc_003850A0;
loc_00384E69:
    if ((((unsigned __int8)((unsigned int)(a4))) & (1)) != 0) goto loc_0038507A;
loc_00384E73:
    v_rbp = ((unsigned int)(*(unsigned int *)(v_rip + 11218963 + 16))) >> (5);
    v_rbp = (unsigned int)((v_rbp) & (31));
    if (((*(unsigned __int64 *)(v_rip + 12852224)) & (0x8000ULL)) == 0) goto loc_00384E94;
    if ((((unsigned __int8)((unsigned int)(a4))) & (2)) != 0) goto loc_003850B2;
loc_00384E94:
    if (v_stack_p34 != 0) goto loc_003850C7;
loc_00384E9F:
    if (v_r15 == -1) goto loc_00384EF5;
    v_rbx = (v_r15 + v_r15 * 2) << (4);
    v_rbx = (v_rbx) + (0);
    result = MiUseProtectedSlabAllocatorForDriverPage(v_stack_p48, (unsigned int)((unsigned int)(v_rbp)), v_stack_p30, a4);
    if ((unsigned int)(result) == 0) goto loc_00384FB6;
    result = MiGetPfnSlabType(v_rbx, (unsigned int)((unsigned int)(v_rbp)), v_stack_p30, a4);
    if (((unsigned int)(result)) != 9) goto loc_00384FC7;
loc_00384EDD:
    if (v_stack_p40 == v_rdi) goto loc_00384FE1;
    result = MiReleaseFreshPageAtDpc(v_rbx, (unsigned int)((unsigned int)(v_rbp)), v_stack_p30, a4);
    v_stack_p40 = v_rdi;
loc_00384EF5:
    result = MiUnlockPageTable(v_rip + 11218753, 0, v_stack_p30, a4);
    result = MiUnlockWorkingSetShared(v_rip + 11218738, (unsigned __int8)(v_stack_p20), v_stack_p30, a4);
    a3 = 0;
    result = MiAllocateDriverPage(v_stack_p48, (unsigned int)((unsigned int)(v_rbp)), a3, a4);
    result = MiLockWorkingSetShared(v_rip + 11218711, (unsigned int)((unsigned int)(v_rbp)), a3, a4);
    result = MiLockNestedPageTable(v_rip + 11218693, 0, a3, a4);
    if (result == -1) goto loc_00385111;
loc_00384F4A:
loc_00384F54:
    goto loc_00384D0C;
loc_00384F61:
    result = MiUnlockPageTable(v_rip + 11218645, 0, a3, a4);
loc_00384F70:
    v_rsi = (v_rdi) >> (9);
    v_rsi = (v_rsi) & (result);
    v_rsi = (v_rsi) + (v_rbp);
    result = MiLockNestedPageTable(v_rip + 11218607, v_rsi, a3, a4);
    goto loc_00384D35;
loc_00384FA8:
    if (condition_is_below) { v_r10 = (unsigned int)(v_rip + 11218607); }
    goto loc_00384CC4;
loc_00384FB6:
    result = MiGetPfnSlabType(v_rip + 11218607, v_rsi, a3, a4);
    if (((unsigned int)(result)) == 9) goto loc_00384FE1;
    goto loc_00384FCB;
loc_00384FC7:
loc_00384FCB:
    result = MiCheckSlabPage(v_stack_pB0, (unsigned int)(v_stack_p30), 4, a4);
    if ((unsigned int)(result) == 0) goto loc_00384EDD;
loc_00384FE1:
    v_rbx = (v_rdi) << (25);
    result = (v_rbp) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    result = MiCopyOnWrite(v_rbx, v_rdi, result, (unsigned int)(v_stack_p38));
    a1 = (result + result * 2) + (result + result * 2);
    v_r15 = (result) | (-1);
    if (((*(unsigned __int64 *)(v_rip + 12851789)) & (0x8000ULL)) == 0) goto loc_00384D71;
    result = (*(unsigned __int64 *)(result + a1 * 8 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_00384D71;
    result = MiMakeDriverPageStayResident(v_stack_pA0, v_rip + 11218397, v_rbx, (unsigned int)(v_stack_p38));
    goto loc_00384D71;
loc_0038507A:
    if (((unsigned __int8)(result)) < 3) goto loc_00384D71;
    if (((unsigned __int8)(result)) < 3) goto loc_00384E73;
    goto loc_00384D71;
loc_00385095:
    v_rsi = 0;
    v_rdi = (v_rdi) + (8);
    goto loc_00384E02;
loc_003850A0:
    if (*(unsigned __int64 *)(v_stack_pA0 + 8) != 0) goto loc_00384D71;
    goto loc_00384E69;
loc_003850B2:
    if ((((unsigned __int8)(v_rbp)) & (2)) == 0) goto loc_00384E94;
    goto loc_00384E0F;
loc_003850C7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 184)))) & (4)) != 0) goto loc_00384E9F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pA0 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00384E9F;
    v_rdi = (v_rdi) + (8);
    goto loc_00384F54;
loc_003850F4:
    goto loc_00384DDE;
loc_00385111:
    goto loc_00384E0F;
loc_0038511C:
    a1 = (v_r15 + v_r15 * 2) << (4);
    a1 = (a1) + (result);
    result = MiReleaseFreshPage(a1, result, v_rbx, (unsigned int)(v_stack_p38));
    goto loc_00384E3C;
}
```

## 5. (Beta) C Style

```c
int64_t MiMakeDriverPagesPrivate(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (88);
    local_r12 = 0;
    local_r10 = 0;
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAAB3F0) + *(uint16_t *)(v_rip + 0xAB3260) * 8);
    if ((((uint8_t)(Arg4)) & (3)) != 0) goto loc_00384CC4;
    if (condition_is_below) goto loc_00384FA8;
loc_00384CC4:
    Arg1 = (uint32_t)((0) | (1));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (4));
    v_stack_m64 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) { Arg1 = 0; }
    local_rsi = 0;
    local_r15 = (local_r15) | (-1);
    v_stack_m60 = (uint32_t)(Arg1);
    result = MiLockWorkingSetShared(v_rip + 11219277, Arg2, Arg3, Arg4);
    v_stack_p20 = (uint8_t)(result);
loc_00384D0C:
loc_00384D16:
    if (Arg2 > Arg3) goto loc_00384E0F;
    if (0 == 0) goto loc_00384F70;
    if (((Arg2) & (0xFFFULL)) == 0) goto loc_00384F61;
loc_00384D35:
    if (*(uint64_t *)(Arg2) == 0) goto loc_00384D71;
    if ((((uint8_t)(*(uint64_t *)(Arg2))) & (1)) == 0) goto loc_00384D7F;
    result = (*(uint64_t *)(Arg2)) >> (12);
    result = (result) & (v_rip + 11219277);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (Arg3);
    if (sign_flag) goto loc_00384E51;
loc_00384D71:
    local_rdi = (Arg2) + (8);
    goto loc_00384D16;
loc_00384D7F:
    if (condition_is_above_or_equal) goto loc_00384D71;
    result = MiUnlockPageTable(v_rip + 11219120, 0, Arg3, Arg4);
    result = MiUnlockWorkingSetShared(v_rip + 11219105, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    local_rbp = (local_rdi) << (25);
    result = (result) << (25);
    Arg4 = 0;
    local_rbp = (local_rbp) - (result);
    Arg3 = 0;
    local_rbp = (local_rbp) >> (16);
    Arg1 = 0;
    result = MmAccessFault(Arg1, local_rbp, Arg3, Arg4);
    if (sign_flag) goto loc_003850F4;
loc_00384DDE:
    result = MiLockWorkingSetShared(v_rip + 11219035, local_rbp, Arg3, Arg4);
    if (sign_flag) goto loc_00385095;
    result = MiLockNestedPageTable(v_rip + 11219011, 0, Arg3, Arg4);
loc_00384E02:
    goto loc_00384F4A;
loc_00384E0F:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_rip + 11218978;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockWorkingSetShared(v_rip + 11218963, (uint8_t)(v_stack_p20), Arg3, Arg4);
    if (local_r15 != -1) goto loc_0038511C;
loc_00384E3C:
    local_rsp = (local_rsp) + (88);
    return 0;
loc_00384E51:
    if (condition_is_below) goto loc_00384E69;
    if (!sign_flag) goto loc_003850A0;
loc_00384E69:
    if ((((uint8_t)((uint32_t)(Arg4))) & (1)) != 0) goto loc_0038507A;
loc_00384E73:
    local_rbp = ((uint32_t)(*(uint32_t *)(v_rip + 0xAB3013 + 0x10))) >> (5);
    local_rbp = (uint32_t)((local_rbp) & (31));
    if (((*(uint64_t *)(v_rip + 0xC41C00)) & (0x8000ULL)) == 0) goto loc_00384E94;
    if ((((uint8_t)((uint32_t)(Arg4))) & (2)) != 0) goto loc_003850B2;
loc_00384E94:
    if (v_stack_p34 != 0) goto loc_003850C7;
loc_00384E9F:
    if (local_r15 == -1) goto loc_00384EF5;
    local_rbx = (local_r15 + local_r15 * 2) << (4);
    local_rbx = (local_rbx) + (0);
    result = MiUseProtectedSlabAllocatorForDriverPage(v_stack_p48, (uint32_t)((uint32_t)(local_rbp)), v_stack_p30, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00384FB6;
    result = MiGetPfnSlabType(local_rbx, (uint32_t)((uint32_t)(local_rbp)), v_stack_p30, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_00384FC7;
loc_00384EDD:
    if (v_stack_p40 == local_rdi) goto loc_00384FE1;
    result = MiReleaseFreshPageAtDpc(local_rbx, (uint32_t)((uint32_t)(local_rbp)), v_stack_p30, Arg4);
    v_stack_p40 = local_rdi;
loc_00384EF5:
    result = MiUnlockPageTable(v_rip + 11218753, 0, v_stack_p30, Arg4);
    result = MiUnlockWorkingSetShared(v_rip + 11218738, (uint8_t)(v_stack_p20), v_stack_p30, Arg4);
    Arg3 = 0;
    result = MiAllocateDriverPage(v_stack_p48, (uint32_t)((uint32_t)(local_rbp)), Arg3, Arg4);
    result = MiLockWorkingSetShared(v_rip + 11218711, (uint32_t)((uint32_t)(local_rbp)), Arg3, Arg4);
    result = MiLockNestedPageTable(v_rip + 11218693, 0, Arg3, Arg4);
    if (result == -1) goto loc_00385111;
loc_00384F4A:
loc_00384F54:
    goto loc_00384D0C;
loc_00384F61:
    result = MiUnlockPageTable(v_rip + 11218645, 0, Arg3, Arg4);
loc_00384F70:
    local_rsi = (local_rdi) >> (9);
    local_rsi = (local_rsi) & (result);
    local_rsi = (local_rsi) + (local_rbp);
    result = MiLockNestedPageTable(v_rip + 11218607, local_rsi, Arg3, Arg4);
    goto loc_00384D35;
loc_00384FA8:
    if (condition_is_below) { local_r10 = (uint32_t)(v_rip + 11218607); }
    goto loc_00384CC4;
loc_00384FB6:
    result = MiGetPfnSlabType(v_rip + 11218607, local_rsi, Arg3, Arg4);
    if (((uint32_t)(result)) == 9) goto loc_00384FE1;
    goto loc_00384FCB;
loc_00384FC7:
loc_00384FCB:
    result = MiCheckSlabPage(v_stack_pB0, (uint32_t)(v_stack_p30), 4, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00384EDD;
loc_00384FE1:
    local_rbx = (local_rdi) << (25);
    result = (local_rbp) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    result = MiCopyOnWrite(local_rbx, local_rdi, result, (uint32_t)(v_stack_p38));
    Arg1 = (result + result * 2) + (result + result * 2);
    local_r15 = (result) | (-1);
    if (((*(uint64_t *)(v_rip + 0xC41A4D)) & (0x8000ULL)) == 0) goto loc_00384D71;
    result = (*(uint64_t *)(result + Arg1 * 8 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 3) goto loc_00384D71;
    result = MiMakeDriverPageStayResident(v_stack_pA0, v_rip + 11218397, local_rbx, (uint32_t)(v_stack_p38));
    goto loc_00384D71;
loc_0038507A:
    if (((uint8_t)(result)) < 3) goto loc_00384D71;
    if (((uint8_t)(result)) < 3) goto loc_00384E73;
    goto loc_00384D71;
loc_00385095:
    local_rsi = 0;
    local_rdi = (local_rdi) + (8);
    goto loc_00384E02;
loc_003850A0:
    if (*(uint64_t *)(v_stack_pA0 + 0x8) != 0) goto loc_00384D71;
    goto loc_00384E69;
loc_003850B2:
    if ((((uint8_t)(local_rbp)) & (2)) == 0) goto loc_00384E94;
    goto loc_00384E0F;
loc_003850C7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB8)))) & (4)) != 0) goto loc_00384E9F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00384E9F;
    local_rdi = (local_rdi) + (8);
    goto loc_00384F54;
loc_003850F4:
    goto loc_00384DDE;
loc_00385111:
    goto loc_00384E0F;
loc_0038511C:
    Arg1 = (local_r15 + local_r15 * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiReleaseFreshPage(Arg1, result, local_rbx, (uint32_t)(v_stack_p38));
    goto loc_00384E3C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00384C60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
