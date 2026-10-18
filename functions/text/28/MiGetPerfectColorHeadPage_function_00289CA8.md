# MiGetPerfectColorHeadPage

- RVA: `0x00289CA8`–`0x0028A0E4` (길이 `1,084` bytes)
- VA: `0x0000000140289CA8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00066E5C`
- 디코드: `246`개 명령, `1,084/1,084` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00289CEE` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00289D1F` → [MiGetColorHeadBase](../3B/MiGetColorHeadBase_function_003BB8B0.md) (function, `0x003BB8B0`)
- `0x00289DB9` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00289E01` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00289E4D` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00289E8B` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00289EAF` → [MiUnlinkFreeOrZeroedPage](../33/MiUnlinkFreeOrZeroedPage_function_00336C40.md) (function, `0x00336C40`)
- `0x00289ED6` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00289EF3` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00289F1A` → [ExTryAcquireSpinLockExclusiveAtDpcLevel](../2B/ExTryAcquireSpinLockExclusiveAtDpcLevel_function_002BB800.md) (function, `0x002BB800`)
- `0x00289F69` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00289F85` → [MiColorHasSlists](MiColorHasSlists_function_0028B1D0.md) (function, `0x0028B1D0`)
- `0x00289FDB` → [MiReplenishPageSlist](../3B/MiReplenishPageSlist_function_003BADE0.md) (function, `0x003BADE0`)
- `0x00289FF0` → [MiIssuePageHeatList](../44/MiIssuePageHeatList_function_0044615C.md) (function, `0x0044615C`)
- `0x0028A00A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0028A02A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028A03A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028A061` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0028A08B` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0028A0AF` → [MiIsFreeZeroPfnCold](../31/MiIsFreeZeroPfnCold_function_0031E5E4.md) (function, `0x0031E5E4`)
- `0x0028A0CA` → [MiAddPageToHeatList](../44/MiAddPageToHeatList_function_0044603C.md) (function, `0x0044603C`)
- `0x0028A0DA` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiGetPage](MiGetPage_function_002884C0.md) at `0x002888B4`
- [MiGetPerfectFreeOrZeroPage](MiGetPerfectFreeOrZeroPage_function_002898E0.md) at `0x002899D8`
- [MiRemovePageAnyColor](MiRemovePageAnyColor_function_0028A9D8.md) at `0x0028AC3A`

### Static image references
- `0x00289CC7` → RVA `0x00E0A740` (`.data`; read)
- `0x00289DA5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00289DD9` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00289E5B` → RVA `0x00E30088` (`.data`; read)
- `0x00289F46` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00289FA9` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x00289DAC` → [sub_006DA384 + 0x37](../6D/Unknown_function_006DA384.md) (`tail-transfer`)
  - `0x00289DBF` → [sub_006DA384 + 0x37](../6D/Unknown_function_006DA384.md) (`tail-transfer`)
  - `0x00289DF4` → [sub_006DA384 + 0x15](../6D/Unknown_function_006DA384.md) (`tail-transfer`)
  - `0x00289E07` → [sub_006DA384 + 0x15](../6D/Unknown_function_006DA384.md) (`tail-transfer`)
  - `0x0028A069` → [sub_006DA384](../6D/Unknown_function_006DA384.md) (`tail-transfer`)
  - `0x0028A092` → [sub_006DA384 + 0x22](../6D/Unknown_function_006DA384.md) (`tail-transfer`)
  - `0x0028A0A7` → [sub_006DA384 + 0x2D](../6D/Unknown_function_006DA384.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00289CA8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00289CAD  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00289CB2  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00289CB7  57                              push rdi
00289CB8  41 54                           push r12
00289CBA  41 55                           push r13
00289CBC  41 56                           push r14
00289CBE  41 57                           push r15
00289CC0  48 81 EC E0 00 00 00            sub rsp, 0xe0
00289CC7  48 8B 05 72 0A B8 00            mov rax, qword ptr [rip + 0xb80a72]
00289CCE  48 33 C4                        xor rax, rsp
00289CD1  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00289CD9  48 8B F1                        mov rsi, rcx
00289CDC  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00289CE1  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00289CE6  33 D2                           xor edx, edx
00289CE8  41 B8 90 00 00 00               mov r8d, 0x90
00289CEE  E8 4D CF 43 00                  call 0x1406c6c40
00289CF3  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00289CF7  4C 8B 36                        mov r14, qword ptr [rsi]
00289CFA  8B 7E 1C                        mov edi, dword ptr [rsi + 0x1c]
00289CFD  49 8B CE                        mov rcx, r14
00289D00  8B 56 1C                        mov edx, dword ptr [rsi + 0x1c]
00289D03  44 8B CF                        mov r9d, edi
00289D06  8B 00                           mov eax, dword ptr [rax]
00289D08  44 8B C0                        mov r8d, eax
00289D0B  8B 5E 20                        mov ebx, dword ptr [rsi + 0x20]
00289D0E  41 C1 E9 12                     shr r9d, 0x12
00289D12  41 83 E1 03                     and r9d, 3
00289D16  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00289D1A  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00289D1F  E8 8C 1B 13 00                  call 0x1403bb8b0
00289D24  4C 8B E8                        mov r13, rax
00289D27  40 0F B6 C7                     movzx eax, dil
00289D2B  48 6B C8 58                     imul rcx, rax, 0x58
00289D2F  4C 03 E9                        add r13, rcx
00289D32  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00289D3C  4D 8B 7D 10                     mov r15, qword ptr [r13 + 0x10]
00289D40  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
00289D4A  B9 02 00 00 00                  mov ecx, 2
00289D4F  4C 3B F8                        cmp r15, rax
00289D52  0F 84 E7 01 00 00               je 0x140289f3f
00289D58  4B 8D 3C 7F                     lea rdi, [r15 + r15*2]
00289D5C  48 C1 E7 04                     shl rdi, 4
00289D60  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00289D6A  48 03 F8                        add rdi, rax
00289D6D  44 8B E3                        mov r12d, ebx
00289D70  44 23 E1                        and r12d, ecx
00289D73  0F 85 CB 02 00 00               jne 0x14028a044
00289D79  F6 C3 01                        test bl, 1
00289D7C  74 46                           je 0x140289dc4
00289D7E  40 B6 11                        mov sil, 0x11
00289D81  8B EB                           mov ebp, ebx
00289D83  C1 ED 04                        shr ebp, 4
00289D86  F7 C3 40 04 00 00               test ebx, 0x440
00289D8C  75 7E                           jne 0x140289e0c
00289D8E  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
00289D95  0F 83 90 00 00 00               jae 0x140289e2b
00289D9B  40 80 FE 11                     cmp sil, 0x11
00289D9F  0F 84 9A 01 00 00               je 0x140289f3f
00289DA5  83 3D 74 CF D3 00 00            cmp dword ptr [rip + 0xd3cf74], 0
00289DAC  0F 84 09 06 45 00               je 0x1406da3bb
00289DB2  44 0F 20 C1                     mov rcx, cr8
00289DB6  40 8A D6                        mov dl, sil
00289DB9  E8 DA B8 26 00                  call 0x1404f5698
00289DBE  90                              nop
00289DBF  E9 F7 05 45 00                  jmp 0x1406da3bb
00289DC4  44 0F 20 C6                     mov rsi, cr8
00289DC8  44 0F 22 C1                     mov cr8, rcx
00289DCC  83 3D 4D CF D3 00 00            cmp dword ptr [rip + 0xd3cf4d], 0
00289DD3  0F 85 8B 01 00 00               jne 0x140289f64
00289DD9  4C 3B 3D 00 3F BA 00            cmp r15, qword ptr [rip + 0xba3f00]
00289DE0  77 0B                           ja 0x140289ded
00289DE2  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00289DE6  48 0F BA E0 36                  bt rax, 0x36
00289DEB  72 94                           jb 0x140289d81
00289DED  83 3D 2C CF D3 00 00            cmp dword ptr [rip + 0xd3cf2c], 0
00289DF4  0F 84 9F 05 45 00               je 0x1406da399
00289DFA  44 0F 20 C1                     mov rcx, cr8
00289DFE  40 8A D6                        mov dl, sil
00289E01  E8 92 B8 26 00                  call 0x1404f5698
00289E06  90                              nop
00289E07  E9 8D 05 45 00                  jmp 0x1406da399
00289E0C  45 33 F6                        xor r14d, r14d
00289E0F  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
00289E16  0F 82 27 01 00 00               jb 0x140289f43
00289E1C  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
00289E21  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00289E2B  0F B6 47 22                     movzx eax, byte ptr [rdi + 0x22]
00289E2F  83 E0 07                        and eax, 7
00289E32  3B 44 24 20                     cmp eax, dword ptr [rsp + 0x20]
00289E36  74 1F                           je 0x140289e57
00289E38  45 85 E4                        test r12d, r12d
00289E3B  74 0A                           je 0x140289e47
00289E3D  F0 4C 21 47 18                  lock and qword ptr [rdi + 0x18], r8
00289E42  E9 F5 FE FF FF                  jmp 0x140289d3c
00289E47  40 8A D6                        mov dl, sil
00289E4A  48 8B CF                        mov rcx, rdi
00289E4D  E8 8E 05 09 00                  call 0x14031a3e0
00289E52  E9 DB FE FF FF                  jmp 0x140289d32
00289E57  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00289E5B  48 8B 0D 26 62 BA 00            mov rcx, qword ptr [rip + 0xba6226]
00289E62  49 8B 96 88 3A 00 00            mov rdx, qword ptr [r14 + 0x3a88]
00289E69  48 C1 E8 2B                     shr rax, 0x2b
00289E6D  25 FF 03 00 00                  and eax, 0x3ff
00289E72  48 39 14 C1                     cmp qword ptr [rcx + rax*8], rdx
00289E76  75 C0                           jne 0x140289e38
00289E78  0B EB                           or ebp, ebx
00289E7A  4D 8D 75 20                     lea r14, [r13 + 0x20]
00289E7E  49 8B CE                        mov rcx, r14
00289E81  40 F6 C5 40                     test bpl, 0x40
00289E85  0F 84 8F 00 00 00               je 0x140289f1a
00289E8B  E8 F0 EF FB FF                  call 0x140248e80
00289E90  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00289E94  4C 3B F8                        cmp r15, rax
00289E97  0F 85 C1 01 00 00               jne 0x14028a05e
00289E9D  0F BA EB 08                     bts ebx, 8
00289EA1  49 8B D5                        mov rdx, r13
00289EA4  8B EB                           mov ebp, ebx
00289EA6  44 8B C3                        mov r8d, ebx
00289EA9  49 8B CF                        mov rcx, r15
00289EAC  83 E5 02                        and ebp, 2
00289EAF  E8 8C CD 0A 00                  call 0x140336c40
00289EB4  85 C0                           test eax, eax
00289EB6  0F 84 CC 01 00 00               je 0x14028a088
00289EBC  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00289EC6  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00289ECB  85 ED                           test ebp, ebp
00289ECD  0F 84 AA 00 00 00               je 0x140289f7d
00289ED3  49 8B CE                        mov rcx, r14
00289ED6  E8 05 F9 FB FF                  call 0x1402497e0
00289EDB  40 80 FE 11                     cmp sil, 0x11
00289EDF  0F 85 15 01 00 00               jne 0x140289ffa
00289EE5  48 8B C7                        mov rax, rdi
00289EE8  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00289EF0  48 33 CC                        xor rcx, rsp
00289EF3  E8 48 27 42 00                  call 0x1406ac640
00289EF8  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00289F00  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00289F04  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00289F08  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00289F0C  49 8B E3                        mov rsp, r11
00289F0F  41 5F                           pop r15
00289F11  41 5E                           pop r14
00289F13  41 5D                           pop r13
00289F15  41 5C                           pop r12
00289F17  5F                              pop rdi
00289F18  C3                              ret
00289F19  CC                              int3
00289F1A  E8 E1 18 03 00                  call 0x1402bb800
00289F1F  85 C0                           test eax, eax
00289F21  0F 85 69 FF FF FF               jne 0x140289e90
00289F27  45 85 E4                        test r12d, r12d
00289F2A  0F 84 A4 01 00 00               je 0x14028a0d4
00289F30  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00289F3A  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00289F3F  33 C0                           xor eax, eax
00289F41  EB A5                           jmp 0x140289ee8
00289F43  41 FF C6                        inc r14d
00289F46  44 85 35 5F B3 D3 00            test dword ptr [rip + 0xd3b35f], r14d
00289F4D  0F 84 C9 00 00 00               je 0x14028a01c
00289F53  F3 90                           pause
00289F55  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00289F59  48 85 C0                        test rax, rax
00289F5C  0F 89 AD FE FF FF               jns 0x140289e0f
00289F62  EB DF                           jmp 0x140289f43
00289F64  8A D1                           mov dl, cl
00289F66  40 8A CE                        mov cl, sil
00289F69  E8 8E B7 26 00                  call 0x1404f56fc
00289F6E  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00289F78  E9 5C FE FF FF                  jmp 0x140289dd9
00289F7D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00289F82  8B 4B 1C                        mov ecx, dword ptr [rbx + 0x1c]
00289F85  E8 46 12 00 00                  call 0x14028b1d0
00289F8A  85 C0                           test eax, eax
00289F8C  0F 84 41 FF FF FF               je 0x140289ed3
00289F92  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00289F96  48 B9 FF FF FF FF 3F 00 00 00   movabs rcx, 0x3fffffffff
00289FA0  48 3B C1                        cmp rax, rcx
00289FA3  0F 84 2A FF FF FF               je 0x140289ed3
00289FA9  F7 05 05 CB D3 00 00 00 20 00   test dword ptr [rip + 0xd3cb05], 0x200000
00289FB3  0F 57 C0                        xorps xmm0, xmm0
00289FB6  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00289FBB  C7 44 24 40 81 00 00 00         mov dword ptr [rsp + 0x40], 0x81
00289FC3  0F 85 E3 00 00 00               jne 0x14028a0ac
00289FC9  44 8B 43 1C                     mov r8d, dword ptr [rbx + 0x1c]
00289FCD  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00289FD2  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
00289FD6  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
00289FDB  E8 00 0E 13 00                  call 0x1403bade0
00289FE0  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
00289FE5  0F 84 E8 FE FF FF               je 0x140289ed3
00289FEB  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00289FF0  E8 67 C1 1B 00                  call 0x14044615c
00289FF5  E9 D9 FE FF FF                  jmp 0x140289ed3
00289FFA  83 3D 1F CD D3 00 00            cmp dword ptr [rip + 0xd3cd1f], 0
0028A001  74 0C                           je 0x14028a00f
0028A003  44 0F 20 C1                     mov rcx, cr8
0028A007  40 8A D6                        mov dl, sil
0028A00A  E8 89 B6 26 00                  call 0x1404f5698
0028A00F  40 0F B6 C6                     movzx eax, sil
0028A013  44 0F 22 C0                     mov cr8, rax
0028A017  E9 C9 FE FF FF                  jmp 0x140289ee5
0028A01C  8B 05 96 CA D3 00               mov eax, dword ptr [rip + 0xd3ca96]
0028A022  A8 40                           test al, 0x40
0028A024  0F 84 29 FF FF FF               je 0x140289f53
0028A02A  E8 61 54 08 00                  call 0x14030f490
0028A02F  84 C0                           test al, al
0028A031  0F 84 1C FF FF FF               je 0x140289f53
0028A037  41 8B CE                        mov ecx, r14d
0028A03A  E8 21 54 08 00                  call 0x14030f460
0028A03F  E9 11 FF FF FF                  jmp 0x140289f55
0028A044  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0028A04B  0F 82 EE FE FF FF               jb 0x140289f3f
0028A051  8B EB                           mov ebp, ebx
0028A053  40 B6 11                        mov sil, 0x11
0028A056  C1 ED 04                        shr ebp, 4
0028A059  E9 CD FD FF FF                  jmp 0x140289e2b
0028A05E  49 8B CE                        mov rcx, r14
0028A061  E8 7A F7 FB FF                  call 0x1402497e0
0028A066  45 85 E4                        test r12d, r12d
0028A069  0F 84 15 03 45 00               je 0x1406da384
0028A06F  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
0028A079  F0 4C 21 47 18                  lock and qword ptr [rdi + 0x18], r8
0028A07E  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
0028A083  E9 B4 FC FF FF                  jmp 0x140289d3c
0028A088  49 8B CE                        mov rcx, r14
0028A08B  E8 50 F7 FB FF                  call 0x1402497e0
0028A090  85 ED                           test ebp, ebp
0028A092  0F 84 0E 03 45 00               je 0x1406da3a6
0028A098  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0028A0A2  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
0028A0A7  E9 05 03 45 00                  jmp 0x1406da3b1
0028A0AC  48 8B CF                        mov rcx, rdi
0028A0AF  E8 30 45 09 00                  call 0x14031e5e4
0028A0B4  85 C0                           test eax, eax
0028A0B6  0F 84 0D FF FF FF               je 0x140289fc9
0028A0BC  41 B8 03 00 00 00               mov r8d, 3
0028A0C2  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0028A0C7  49 8B D7                        mov rdx, r15
0028A0CA  E8 6D BF 1B 00                  call 0x14044603c
0028A0CF  E9 F5 FE FF FF                  jmp 0x140289fc9
0028A0D4  40 8A D6                        mov dl, sil
0028A0D7  48 8B CF                        mov rcx, rdi
0028A0DA  E8 01 03 09 00                  call 0x14031a3e0
0028A0DF  E9 5B FE FF FF                  jmp 0x140289f3f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetPerfectColorHeadPage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m9C;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 12061298)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_mD8 = a1;
    a2 = 0;
    result = memset(v_stack_mC8, a2, 144, a4);
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28))))) >> (18));
    a4 = (unsigned int)((a4) & (3));
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))));
    v_stack_mE0 = *(unsigned __int64 *)(a1);
    result = MiGetColorHeadBase(*(unsigned __int64 *)(a1), (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))))), a4);
    a1 = (*(unsigned __int64 *)(a1)) * ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28))));
    v_r13 = (result) + (a1);
loc_00289D32:
loc_00289D3C:
    if ((*(unsigned __int64 *)(v_r13 + 16)) == ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28))))) goto loc_00289F3F;
    v_rdi = (*(unsigned __int64 *)(v_r13 + 16) + *(unsigned __int64 *)(v_r13 + 16) * 2) << (4);
    v_rdi = (v_rdi) + ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28))));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (2));
    if (condition_is_not_equal) goto loc_0028A044;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (1)) == 0) goto loc_00289DC4;
loc_00289D81:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) >> (4));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (0x440ULL)) != 0) goto loc_00289E0C;
    if (condition_is_above_or_equal) goto loc_00289E2B;
    if (17 == 17) goto loc_00289F3F;
    result = KiLowerIrqlProcessIrqlFlags(v_cr8, 17, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))))), a4);
loc_00289DC4:
    if ((*(unsigned int *)(v_rip + 13881165)) != 0) goto loc_00289F64;
loc_00289DD9:
    if ((*(unsigned __int64 *)(v_r13 + 16)) > (*(unsigned __int64 *)(v_rip + 12205824))) goto loc_00289DED;
    if ((*(unsigned __int64 *)(v_r13 + 16)) < (*(unsigned __int64 *)(v_rip + 12205824))) goto loc_00289D81;
loc_00289DED:
    result = KiLowerIrqlProcessIrqlFlags(v_cr8, (unsigned __int8)(v_cr8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))))), a4);
loc_00289E0C:
    v_r14 = 0;
loc_00289E0F:
    if (condition_is_below) goto loc_00289F43;
loc_00289E2B:
    result = (unsigned int)((*(unsigned __int8 *)(v_rdi + 34)) & (7));
    if (((unsigned int)(result)) == v_stack_mE8) goto loc_00289E57;
loc_00289E38:
    if ((unsigned int)(v_r12) == 0) goto loc_00289E47;
    goto loc_00289D3C;
loc_00289E47:
    result = MiUnlockPage(v_rdi, (unsigned __int8)(v_cr8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))))), a4);
    goto loc_00289D32;
loc_00289E57:
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12214822) + result * 8)) != (*(unsigned __int64 *)(v_stack_mE0 + 14984))) goto loc_00289E38;
    v_rbp = (unsigned int)((v_rbp) | ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))));
    if ((((unsigned __int8)(v_rbp)) & (64)) == 0) goto loc_00289F1A;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_r13 + 32, *(unsigned __int64 *)(v_stack_mE0 + 14984), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))))), a4);
loc_00289E90:
    if ((*(unsigned __int64 *)(v_r13 + 16)) != (*(unsigned __int64 *)(v_r13 + 16))) goto loc_0028A05E;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (2));
    result = MiUnlinkFreeOrZeroedPage(*(unsigned __int64 *)(v_r13 + 16), v_r13, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), a4);
    if ((unsigned int)(result) == 0) goto loc_0028A088;
    if ((unsigned int)(v_rbp) == 0) goto loc_00289F7D;
loc_00289ED3:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_r13 + 32, v_r13, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), a4);
    if (((unsigned __int8)(v_cr8)) != 17) goto loc_00289FFA;
loc_00289EE5:
loc_00289EE8:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_r13, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), a4);
    return result;
loc_00289F1A:
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(a1, v_r13, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), a4);
    if ((unsigned int)(result) != 0) goto loc_00289E90;
    if ((unsigned int)(v_r12) == 0) goto loc_0028A0D4;
loc_00289F3F:
    result = 0;
    goto loc_00289EE8;
loc_00289F43:
    v_r14 = (unsigned int)((v_r13 + 32) + 1);
    if (((*(unsigned int *)(v_rip + 13874015)) & ((unsigned int)(v_r14))) == 0) goto loc_0028A01C;
loc_00289F53:
loc_00289F55:
    if (!sign_flag) goto loc_00289E0F;
    goto loc_00289F43;
loc_00289F64:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)), (unsigned __int8)(a1), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), a4);
    goto loc_00289DD9;
loc_00289F7D:
    result = MiColorHasSlists((unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), (unsigned __int8)(a1), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), a4);
    if ((unsigned int)(result) == 0) goto loc_00289ED3;
    if ((*(unsigned __int64 *)(v_r13 + 16)) == ((unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)))) goto loc_00289ED3;
    v_stack_mA0 = v_xmm0;
    v_stack_mA0 = 129;
    if (((*(unsigned int *)(v_rip + 13880069)) & (0x200000ULL)) != 0) goto loc_0028A0AC;
loc_00289FC9:
    result = MiReplenishPageSlist(v_stack_mB8, (unsigned int)(v_stack_mC0), (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    if (v_stack_m9C == 0) goto loc_00289ED3;
    result = MiIssuePageHeatList(v_stack_mA0, (unsigned int)(v_stack_mC0), (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    goto loc_00289ED3;
loc_00289FFA:
    if ((*(unsigned int *)(v_rip + 13880607)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    }
    goto loc_00289EE5;
loc_0028A01C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13879958)))) & (64)) == 0) goto loc_00289F53;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    if ((unsigned __int8)(result) == 0) goto loc_00289F53;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), a2, (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    goto loc_00289F55;
loc_0028A044:
    if (condition_is_below) goto loc_00289F3F;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mB0))) >> (4));
    goto loc_00289E2B;
loc_0028A05E:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_r14, a2, (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    goto loc_00289D3C;
loc_0028A088:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_mB8, a2, (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
loc_0028A0AC:
    result = MiIsFreeZeroPfnCold(v_rdi, a2, (unsigned int)(*(unsigned int *)(v_stack_mB0 + 28)), v_stack_mA0);
    if ((unsigned int)(result) == 0) goto loc_00289FC9;
    result = MiAddPageToHeatList(v_stack_mA0, *(unsigned __int64 *)(v_r13 + 16), 3, v_stack_mA0);
    goto loc_00289FC9;
loc_0028A0D4:
    result = MiUnlockPage(v_rdi, 17, 3, v_stack_mA0);
    goto loc_00289F3F;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetPerfectColorHeadPage(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m9C;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0xB80A72)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_mD8 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 144, a4);
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C))))) >> (18));
    a4 = (uint32_t)((a4) & (3));
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))));
    v_stack_mE0 = *(uint64_t *)(arg1);
    result = MiGetColorHeadBase(*(uint64_t *)(arg1), (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))))), a4);
    Arg1 = (*(uint64_t *)(arg1)) * ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C))));
    local_r13 = (result) + (Arg1);
loc_00289D32:
loc_00289D3C:
    if ((*(uint64_t *)(local_r13 + 0x10)) == ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C))))) goto loc_00289F3F;
    local_rdi = (*(uint64_t *)(local_r13 + 0x10) + *(uint64_t *)(local_r13 + 0x10) * 2) << (4);
    local_rdi = (local_rdi) + ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C))));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (2));
    if (condition_is_not_equal) goto loc_0028A044;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (1)) == 0) goto loc_00289DC4;
loc_00289D81:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) >> (4));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (0x440ULL)) != 0) goto loc_00289E0C;
    if (condition_is_above_or_equal) goto loc_00289E2B;
    if (17 == 17) goto loc_00289F3F;
    result = KiLowerIrqlProcessIrqlFlags(v_cr8, 17, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))))), a4);
loc_00289DC4:
    if ((*(uint32_t *)(v_rip + 0xD3CF4D)) != 0) goto loc_00289F64;
loc_00289DD9:
    if ((*(uint64_t *)(local_r13 + 0x10)) > (*(uint64_t *)(v_rip + 0xBA3F00))) goto loc_00289DED;
    if ((*(uint64_t *)(local_r13 + 0x10)) < (*(uint64_t *)(v_rip + 0xBA3F00))) goto loc_00289D81;
loc_00289DED:
    result = KiLowerIrqlProcessIrqlFlags(v_cr8, (uint8_t)(v_cr8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))))), a4);
loc_00289E0C:
    local_r14 = 0;
loc_00289E0F:
    if (condition_is_below) goto loc_00289F43;
loc_00289E2B:
    result = (uint32_t)((*(uint8_t *)(local_rdi + 0x22)) & (7));
    if (((uint32_t)(result)) == v_stack_mE8) goto loc_00289E57;
loc_00289E38:
    if ((uint32_t)(local_r12) == 0) goto loc_00289E47;
    goto loc_00289D3C;
loc_00289E47:
    result = MiUnlockPage(local_rdi, (uint8_t)(v_cr8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))))), a4);
    goto loc_00289D32;
loc_00289E57:
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA6226) + result * 8)) != (*(uint64_t *)(v_stack_mE0 + 0x3A88))) goto loc_00289E38;
    local_rbp = (uint32_t)((local_rbp) | ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))));
    if ((((uint8_t)(local_rbp)) & (64)) == 0) goto loc_00289F1A;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(local_r13 + 32, *(uint64_t *)(v_stack_mE0 + 0x3A88), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))))), a4);
loc_00289E90:
    if ((*(uint64_t *)(local_r13 + 0x10)) != (*(uint64_t *)(local_r13 + 0x10))) goto loc_0028A05E;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (2));
    result = MiUnlinkFreeOrZeroedPage(*(uint64_t *)(local_r13 + 0x10), local_r13, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), a4);
    if ((uint32_t)(result) == 0) goto loc_0028A088;
    if ((uint32_t)(local_rbp) == 0) goto loc_00289F7D;
loc_00289ED3:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(local_r13 + 32, local_r13, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), a4);
    if (((uint8_t)(v_cr8)) != 17) goto loc_00289FFA;
loc_00289EE5:
loc_00289EE8:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_r13, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), a4);
    return result;
loc_00289F1A:
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(Arg1, local_r13, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), a4);
    if ((uint32_t)(result) != 0) goto loc_00289E90;
    if ((uint32_t)(local_r12) == 0) goto loc_0028A0D4;
loc_00289F3F:
    result = 0;
    goto loc_00289EE8;
loc_00289F43:
    local_r14 = (uint32_t)((local_r13 + 32) + 1);
    if (((*(uint32_t *)(v_rip + 0xD3B35F)) & ((uint32_t)(local_r14))) == 0) goto loc_0028A01C;
loc_00289F53:
loc_00289F55:
    if (!sign_flag) goto loc_00289E0F;
    goto loc_00289F43;
loc_00289F64:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)), (uint8_t)(Arg1), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), a4);
    goto loc_00289DD9;
loc_00289F7D:
    result = MiColorHasSlists((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), (uint8_t)(Arg1), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), a4);
    if ((uint32_t)(result) == 0) goto loc_00289ED3;
    if ((*(uint64_t *)(local_r13 + 0x10)) == ((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)))) goto loc_00289ED3;
    v_stack_mA0 = v_xmm0;
    v_stack_mA0 = 129;
    if (((*(uint32_t *)(v_rip + 0xD3CB05)) & (0x200000ULL)) != 0) goto loc_0028A0AC;
loc_00289FC9:
    result = MiReplenishPageSlist(v_stack_mB8, (uint32_t)(v_stack_mC0), (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    if (v_stack_m9C == 0) goto loc_00289ED3;
    result = MiIssuePageHeatList(v_stack_mA0, (uint32_t)(v_stack_mC0), (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    goto loc_00289ED3;
loc_00289FFA:
    if ((*(uint32_t *)(v_rip + 0xD3CD1F)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    }
    goto loc_00289EE5;
loc_0028A01C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD3CA96)))) & (64)) == 0) goto loc_00289F53;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    if ((uint8_t)(result) == 0) goto loc_00289F53;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), Arg2, (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    goto loc_00289F55;
loc_0028A044:
    if (condition_is_below) goto loc_00289F3F;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mB0))) >> (4));
    goto loc_00289E2B;
loc_0028A05E:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(local_r14, Arg2, (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    goto loc_00289D3C;
loc_0028A088:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_mB8, Arg2, (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
loc_0028A0AC:
    result = MiIsFreeZeroPfnCold(local_rdi, Arg2, (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x1C)), v_stack_mA0);
    if ((uint32_t)(result) == 0) goto loc_00289FC9;
    result = MiAddPageToHeatList(v_stack_mA0, *(uint64_t *)(local_r13 + 0x10), 3, v_stack_mA0);
    goto loc_00289FC9;
loc_0028A0D4:
    result = MiUnlockPage(local_rdi, 17, 3, v_stack_mA0);
    goto loc_00289F3F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00289CA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
