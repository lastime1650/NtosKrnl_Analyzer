# MiDeleteVa

- RVA: `0x002789E0`–`0x00279081` (길이 `1,697` bytes)
- VA: `0x00000001402789E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00065F8C`
- 디코드: `398`개 명령, `1,697/1,697` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00278B8D` → [MiDecommitAddToList](../24/MiDecommitAddToList_function_00242264.md) (function, `0x00242264`)
- `0x00278C32` → [MiDecommitHandleProtoFormatPte](../24/MiDecommitHandleProtoFormatPte_function_00242D54.md) (function, `0x00242D54`)
- `0x00278C4B` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00278D17` → [MI_WSLE_LOG_ACCESS](../29/MI_WSLE_LOG_ACCESS_function_00294400.md) (function, `0x00294400`)
- `0x00278D21` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00278DD3` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00278DDB` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00278E38` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00278E6A` → [MiDecommitHandlePageFileFormatPte](../24/MiDecommitHandlePageFileFormatPte_function_00242A5C.md) (function, `0x00242A5C`)
- `0x00278E8B` → [MiReturnPagedPoolLockCharge](../24/MiReturnPagedPoolLockCharge_function_00240780.md) (function, `0x00240780`)
- `0x00278ED1` → [MiDecommitHandleTransitionPte](../24/MiDecommitHandleTransitionPte_function_0024037C.md) (function, `0x0024037C`)
- `0x00278F0E` → [MiDeleteRotateVa](../2C/MiDeleteRotateVa_function_002C79D4.md) (function, `0x002C79D4`)
- `0x00278F44` → [MiDeleteLargeUserPde](../4C/MiDeleteLargeUserPde_function_004C4D54.md) (function, `0x004C4D54`)
- `0x00278FA0` → [MiIsLazyStampedPte](../22/MiIsLazyStampedPte_function_00227B10.md) (function, `0x00227B10`)
- `0x00278FB8` → [MiDeleteVadAwePtes](../4C/MiDeleteVadAwePtes_function_004C4F3C.md) (function, `0x004C4F3C`)
- `0x00278FC9` → [MiDecommitAddTbFlushEntries](../4F/MiDecommitAddTbFlushEntries_function_004FB798.md) (function, `0x004FB798`)
- `0x00279001` → [MiDeleteVadAwePtes](../4C/MiDeleteVadAwePtes_function_004C4F3C.md) (function, `0x004C4F3C`)
- `0x0027902E` → [MiDeleteLargeUserPde](../4C/MiDeleteLargeUserPde_function_004C4D54.md) (function, `0x004C4D54`)
- `0x0027904E` → [MiDecommitLargePte](../4D/MiDecommitLargePte_function_004D1ED4.md) (function, `0x004D1ED4`)

### Direct callers
- [MiDeleteVaDirect](MiDeleteVaDirect_function_00277560.md) at `0x0027780C`

### Static image references
- `0x00278BB6` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00278CFB` → RVA `0x00E30088` (`.data`; read)
- `0x00278E9B` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0027906B` → [sub_006DA0C8](../6D/Unknown_function_006DA0C8.md) (`tail-transfer`)
  - `0x0027907C` → [sub_006DA0C8](../6D/Unknown_function_006DA0C8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002789E0  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002789E5  53                              push rbx
002789E6  55                              push rbp
002789E7  56                              push rsi
002789E8  57                              push rdi
002789E9  41 54                           push r12
002789EB  41 55                           push r13
002789ED  41 56                           push r14
002789EF  41 57                           push r15
002789F1  48 83 EC 28                     sub rsp, 0x28
002789F5  48 8B B9 B8 00 00 00            mov rdi, qword ptr [rcx + 0xb8]
002789FC  45 8B F8                        mov r15d, r8d
002789FF  4C 8B C2                        mov r8, rdx
00278A02  48 8B F2                        mov rsi, rdx
00278A05  41 BC 01 00 00 00               mov r12d, 1
00278A0B  49 C1 E0 19                     shl r8, 0x19
00278A0F  48 8B 3F                        mov rdi, qword ptr [rdi]
00278A12  44 8B B7 A0 00 00 00            mov r14d, dword ptr [rdi + 0xa0]
00278A19  44 89 B4 24 80 00 00 00         mov dword ptr [rsp + 0x80], r14d
00278A21  48 89 57 48                     mov qword ptr [rdi + 0x48], rdx
00278A25  48 89 57 58                     mov qword ptr [rdi + 0x58], rdx
00278A29  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00278A33  48 C1 E0 19                     shl rax, 0x19
00278A37  BD 00 00 00 00                  mov ebp, 0
00278A3C  4C 2B C0                        sub r8, rax
00278A3F  44 89 7F 60                     mov dword ptr [rdi + 0x60], r15d
00278A43  49 C1 F8 10                     sar r8, 0x10
00278A47  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
00278A4B  4C 8B 49 20                     mov r9, qword ptr [rcx + 0x20]
00278A4F  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
00278A57  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00278A5E  4D 8D A9 00 FC FF FF            lea r13, [r9 - 0x400]
00278A65  A8 0F                           test al, 0xf
00278A67  4C 0F 45 ED                     cmovne r13, rbp
00278A6B  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00278A75  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00278A7F  90                              nop
00278A80  48 8B 1E                        mov rbx, qword ptr [rsi]
00278A83  48 8B C0                        mov rax, rax
00278A86  48 3B F0                        cmp rsi, rax
00278A89  72 24                           jb 0x140278aaf
00278A8B  48 8B C1                        mov rax, rcx
00278A8E  48 3B F0                        cmp rsi, rax
00278A91  77 1C                           ja 0x140278aaf
00278A93  48 8B C3                        mov rax, rbx
00278A96  F6 C3 01                        test bl, 1
00278A99  74 14                           je 0x140278aaf
00278A9B  F6 C3 42                        test bl, 0x42
00278A9E  0F 95 C2                        setne dl
00278AA1  F6 C3 20                        test bl, 0x20
00278AA4  0F 95 C1                        setne cl
00278AA7  84 D1                           test cl, dl
00278AA9  0F 84 07 01 00 00               je 0x140278bb6
00278AAF  48 85 DB                        test rbx, rbx
00278AB2  75 19                           jne 0x140278acd
00278AB4  48 83 47 58 08                  add qword ptr [rdi + 0x58], 8
00278AB9  33 C0                           xor eax, eax
00278ABB  48 83 C4 28                     add rsp, 0x28
00278ABF  41 5F                           pop r15
00278AC1  41 5E                           pop r14
00278AC3  41 5D                           pop r13
00278AC5  41 5C                           pop r12
00278AC7  5F                              pop rdi
00278AC8  5E                              pop rsi
00278AC9  5D                              pop rbp
00278ACA  5B                              pop rbx
00278ACB  C3                              ret
00278ACC  CC                              int3
00278ACD  F6 C3 01                        test bl, 1
00278AD0  0F 84 4B 01 00 00               je 0x140278c21
00278AD6  48 39 6F 10                     cmp qword ptr [rdi + 0x10], rbp
00278ADA  0F 84 41 02 00 00               je 0x140278d21
00278AE0  41 83 FF 01                     cmp r15d, 1
00278AE4  0F 8D C2 02 00 00               jge 0x140278dac
00278AEA  F7 87 A0 00 00 00 10 08 00 00   test dword ptr [rdi + 0xa0], 0x810
00278AF4  0F 85 20 05 00 00               jne 0x14027901a
00278AFA  4D 85 ED                        test r13, r13
00278AFD  74 35                           je 0x140278b34
00278AFF  45 85 FF                        test r15d, r15d
00278B02  75 30                           jne 0x140278b34
00278B04  41 F6 C6 08                     test r14b, 8
00278B08  0F 85 F5 03 00 00               jne 0x140278f03
00278B0E  41 81 E6 92 00 00 00            and r14d, 0x92
00278B15  41 80 FE 82                     cmp r14b, 0x82
00278B19  75 19                           jne 0x140278b34
00278B1B  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00278B23  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00278B29  C1 E8 18                        shr eax, 0x18
00278B2C  A8 01                           test al, 1
00278B2E  0F 84 B0 01 00 00               je 0x140278ce4
00278B34  8B 87 9C 00 00 00               mov eax, dword ptr [rdi + 0x9c]
00278B3A  A8 08                           test al, 8
00278B3C  0F 85 43 03 00 00               jne 0x140278e85
00278B42  48 39 6F 10                     cmp qword ptr [rdi + 0x10], rbp
00278B46  0F 84 FF 00 00 00               je 0x140278c4b
00278B4C  41 BE 01 00 00 00               mov r14d, 1
00278B52  84 DB                           test bl, bl
00278B54  0F 88 4D 03 00 00               js 0x140278ea7
00278B5A  48 83 BF C0 00 00 00 01         cmp qword ptr [rdi + 0xc0], 1
00278B62  0F 85 6E 01 00 00               jne 0x140278cd6
00278B68  39 6F 60                        cmp dword ptr [rdi + 0x60], ebp
00278B6B  40 0F 95 C5                     setne bpl
00278B6F  FF C5                           inc ebp
00278B71  83 BF 88 00 00 00 00            cmp dword ptr [rdi + 0x88], 0
00278B78  0F 85 DA 04 00 00               jne 0x140279058
00278B7E  85 ED                           test ebp, ebp
00278B80  0F 84 C5 04 00 00               je 0x14027904b
00278B86  48 8B 57 38                     mov rdx, qword ptr [rdi + 0x38]
00278B8A  48 8B CF                        mov rcx, rdi
00278B8D  E8 D2 96 FC FF                  call 0x140242264
00278B92  45 85 FF                        test r15d, r15d
00278B95  0F 85 53 03 00 00               jne 0x140278eee
00278B9B  44 8B A7 C0 00 00 00            mov r12d, dword ptr [rdi + 0xc0]
00278BA2  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00278BA6  41 8B CC                        mov ecx, r12d
00278BA9  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00278BAD  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00278BB1  E9 03 FF FF FF                  jmp 0x140278ab9
00278BB6  48 F7 05 C7 DE D4 00 00 00 60 00  test qword ptr [rip + 0xd4dec7], 0x600000
00278BC1  0F 84 E8 FE FF FF               je 0x140278aaf
00278BC7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00278BD0  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00278BD7  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00278BDE  0F 84 CB FE FF FF               je 0x140278aaf
00278BE4  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
00278BEB  4D 85 C0                        test r8, r8
00278BEE  0F 84 BB FE FF FF               je 0x140278aaf
00278BF4  48 8B CE                        mov rcx, rsi
00278BF7  48 C1 E9 03                     shr rcx, 3
00278BFB  81 E1 FF 01 00 00               and ecx, 0x1ff
00278C01  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
00278C05  F6 C1 20                        test cl, 0x20
00278C08  74 04                           je 0x140278c0e
00278C0A  48 83 C8 20                     or rax, 0x20
00278C0E  48 8B D8                        mov rbx, rax
00278C11  48 83 CB 42                     or rbx, 0x42
00278C15  F6 C1 42                        test cl, 0x42
00278C18  48 0F 44 D8                     cmove rbx, rax
00278C1C  E9 8E FE FF FF                  jmp 0x140278aaf
00278C21  48 0F BA E3 0A                  bt rbx, 0xa
00278C26  0F 83 27 02 00 00               jae 0x140278e53
00278C2C  48 8B D3                        mov rdx, rbx
00278C2F  48 8B CF                        mov rcx, rdi
00278C32  E8 1D A1 FC FF                  call 0x140242d54
00278C37  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00278C3B  41 8B CC                        mov ecx, r12d
00278C3E  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00278C42  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00278C46  E9 6E FE FF FF                  jmp 0x140278ab9
00278C4B  E8 40 A0 FC FF                  call 0x140242c90
00278C50  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
00278C54  41 BE 01 00 00 00               mov r14d, 1
00278C5A  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00278C5E  48 8B D0                        mov rdx, rax
00278C61  89 68 10                        mov dword ptr [rax + 0x10], ebp
00278C64  44 89 70 14                     mov dword ptr [rax + 0x14], r14d
00278C68  4C 89 00                        mov qword ptr [rax], r8
00278C6B  41 8B 88 B8 00 00 00            mov ecx, dword ptr [r8 + 0xb8]
00278C72  C1 E9 08                        shr ecx, 8
00278C75  C0 E9 03                        shr cl, 3
00278C78  41 22 CE                        and cl, r14b
00278C7B  88 48 18                        mov byte ptr [rax + 0x18], cl
00278C7E  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00278C85  A8 0F                           test al, 0xf
00278C87  75 20                           jne 0x140278ca9
00278C89  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00278C92  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00278C99  48 81 C1 00 04 00 00            add rcx, 0x400
00278CA0  4C 3B C1                        cmp r8, rcx
00278CA3  0F 85 7A 02 00 00               jne 0x140278f23
00278CA9  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00278CB0  A8 0F                           test al, 0xf
00278CB2  0F 85 6F 02 00 00               jne 0x140278f27
00278CB8  41 8B C6                        mov eax, r14d
00278CBB  83 62 10 DB                     and dword ptr [rdx + 0x10], 0xffffffdb
00278CBF  89 42 08                        mov dword ptr [rdx + 8], eax
00278CC2  66 89 6A 19                     mov word ptr [rdx + 0x19], bp
00278CC6  89 6A 1C                        mov dword ptr [rdx + 0x1c], ebp
00278CC9  48 89 6A 20                     mov qword ptr [rdx + 0x20], rbp
00278CCD  48 89 6A 28                     mov qword ptr [rdx + 0x28], rbp
00278CD1  E9 7C FE FF FF                  jmp 0x140278b52
00278CD6  39 6F 60                        cmp dword ptr [rdi + 0x60], ebp
00278CD9  0F 84 92 FE FF FF               je 0x140278b71
00278CDF  E9 84 FE FF FF                  jmp 0x140278b68
00278CE4  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00278CEA  24 0F                           and al, 0xf
00278CEC  3C 01                           cmp al, 1
00278CEE  0F 84 A7 01 00 00               je 0x140278e9b
00278CF4  0F B7 91 AE 00 00 00            movzx edx, word ptr [rcx + 0xae]
00278CFB  48 8B 05 86 73 BB 00            mov rax, qword ptr [rip + 0xbb7386]
00278D02  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
00278D06  8B 80 2C 44 00 00               mov eax, dword ptr [rax + 0x442c]
00278D0C  85 C0                           test eax, eax
00278D0E  0F 84 20 FE FF FF               je 0x140278b34
00278D14  48 8B D6                        mov rdx, rsi
00278D17  E8 E4 B6 01 00                  call 0x140294400
00278D1C  E9 13 FE FF FF                  jmp 0x140278b34
00278D21  E8 6A 9F FC FF                  call 0x140242c90
00278D26  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
00278D2A  41 BB 01 00 00 00               mov r11d, 1
00278D30  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00278D34  48 8B D0                        mov rdx, rax
00278D37  89 68 10                        mov dword ptr [rax + 0x10], ebp
00278D3A  44 89 58 14                     mov dword ptr [rax + 0x14], r11d
00278D3E  4C 89 00                        mov qword ptr [rax], r8
00278D41  41 8B 88 B8 00 00 00            mov ecx, dword ptr [r8 + 0xb8]
00278D48  C1 E9 08                        shr ecx, 8
00278D4B  C0 E9 03                        shr cl, 3
00278D4E  41 22 CB                        and cl, r11b
00278D51  88 48 18                        mov byte ptr [rax + 0x18], cl
00278D54  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00278D5B  A8 0F                           test al, 0xf
00278D5D  75 20                           jne 0x140278d7f
00278D5F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00278D68  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00278D6F  48 81 C1 00 04 00 00            add rcx, 0x400
00278D76  4C 3B C1                        cmp r8, rcx
00278D79  0F 85 AF 01 00 00               jne 0x140278f2e
00278D7F  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00278D86  A8 0F                           test al, 0xf
00278D88  0F 85 A4 01 00 00               jne 0x140278f32
00278D8E  41 8B C3                        mov eax, r11d
00278D91  83 62 10 DB                     and dword ptr [rdx + 0x10], 0xffffffdb
00278D95  89 42 08                        mov dword ptr [rdx + 8], eax
00278D98  66 89 6A 19                     mov word ptr [rdx + 0x19], bp
00278D9C  89 6A 1C                        mov dword ptr [rdx + 0x1c], ebp
00278D9F  48 89 6A 20                     mov qword ptr [rdx + 0x20], rbp
00278DA3  48 89 6A 28                     mov qword ptr [rdx + 0x28], rbp
00278DA7  E9 34 FD FF FF                  jmp 0x140278ae0
00278DAC  48 8B C3                        mov rax, rbx
00278DAF  48 C1 E8 07                     shr rax, 7
00278DB3  0F BA E0 00                     bt eax, 0
00278DB7  0F 82 66 02 00 00               jb 0x140279023
00278DBD  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00278DC2  8B 00                           mov eax, dword ptr [rax]
00278DC4  A8 04                           test al, 4
00278DC6  74 10                           je 0x140278dd8
00278DC8  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00278DD0  48 8B D6                        mov rdx, rsi
00278DD3  E8 B8 5A FC FF                  call 0x14023e890
00278DD8  48 8B CE                        mov rcx, rsi
00278DDB  E8 C0 9A 00 00                  call 0x1402828a0
00278DE0  48 C1 E8 0C                     shr rax, 0xc
00278DE4  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00278DEE  48 23 C1                        and rax, rcx
00278DF1  4C 8D 34 40                     lea r14, [rax + rax*2]
00278DF5  49 C1 E6 04                     shl r14, 4
00278DF9  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00278E03  4C 03 F0                        add r14, rax
00278E06  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
00278E0A  0F BA E0 1A                     bt eax, 0x1a
00278E0E  0F 83 E2 00 00 00               jae 0x140278ef6
00278E14  4D 8B 36                        mov r14, qword ptr [r14]
00278E17  49 C1 EE 20                     shr r14, 0x20
00278E1B  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00278E20  41 81 E6 FF 03 00 00            and r14d, 0x3ff
00278E27  8B 00                           mov eax, dword ptr [rax]
00278E29  A8 04                           test al, 4
00278E2B  74 10                           je 0x140278e3d
00278E2D  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00278E35  48 8B D6                        mov rdx, rsi
00278E38  E8 83 E0 F9 FF                  call 0x140216ec0
00278E3D  45 85 F6                        test r14d, r14d
00278E40  0F 85 6E FC FF FF               jne 0x140278ab4
00278E46  44 8B B4 24 80 00 00 00         mov r14d, dword ptr [rsp + 0x80]
00278E4E  E9 A7 FC FF FF                  jmp 0x140278afa
00278E53  41 83 E6 10                     and r14d, 0x10
00278E57  0F 85 40 01 00 00               jne 0x140278f9d
00278E5D  48 0F BA E3 0B                  bt rbx, 0xb
00278E62  72 51                           jb 0x140278eb5
00278E64  48 8B D3                        mov rdx, rbx
00278E67  48 8B CF                        mov rcx, rdi
00278E6A  E8 ED 9B FC FF                  call 0x140242a5c
00278E6F  8B C8                           mov ecx, eax
00278E71  44 8B E0                        mov r12d, eax
00278E74  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00278E78  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00278E7C  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00278E80  E9 34 FC FF FF                  jmp 0x140278ab9
00278E85  48 8B D3                        mov rdx, rbx
00278E88  48 8B CF                        mov rcx, rdi
00278E8B  E8 F0 78 FC FF                  call 0x140240780
00278E90  41 BE 01 00 00 00               mov r14d, 1
00278E96  E9 F7 FC FF FF                  jmp 0x140278b92
00278E9B  48 8D 05 5E FE BB 00            lea rax, [rip + 0xbbfe5e]
00278EA2  E9 5F FE FF FF                  jmp 0x140278d06
00278EA7  39 6F 60                        cmp dword ptr [rdi + 0x60], ebp
00278EAA  0F 85 C1 FC FF FF               jne 0x140278b71
00278EB0  E9 A5 FC FF FF                  jmp 0x140278b5a
00278EB5  F7 84 24 80 00 00 00 00 08 00 00  test dword ptr [rsp + 0x80], 0x800
00278EC0  75 77                           jne 0x140278f39
00278EC2  45 85 F6                        test r14d, r14d
00278EC5  0F 85 17 01 00 00               jne 0x140278fe2
00278ECB  48 8B D3                        mov rdx, rbx
00278ECE  48 8B CF                        mov rcx, rdi
00278ED1  E8 A6 74 FC FF                  call 0x14024037c
00278ED6  44 8B E0                        mov r12d, eax
00278ED9  85 C0                           test eax, eax
00278EDB  0F 85 C1 FC FF FF               jne 0x140278ba2
00278EE1  44 8B B4 24 80 00 00 00         mov r14d, dword ptr [rsp + 0x80]
00278EE9  E9 7D FB FF FF                  jmp 0x140278a6b
00278EEE  45 8B E6                        mov r12d, r14d
00278EF1  E9 AC FC FF FF                  jmp 0x140278ba2
00278EF6  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
00278EFA  49 C1 EE 10                     shr r14, 0x10
00278EFE  E9 18 FF FF FF                  jmp 0x140278e1b
00278F03  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00278F08  45 33 C0                        xor r8d, r8d
00278F0B  48 8B D6                        mov rdx, rsi
00278F0E  E8 C1 EA 04 00                  call 0x1402c79d4
00278F13  85 C0                           test eax, eax
00278F15  0F 84 F3 FB FF FF               je 0x140278b0e
00278F1B  41 BE 01 00 00 00               mov r14d, 1
00278F21  EB 3D                           jmp 0x140278f60
00278F23  83 4A 10 09                     or dword ptr [rdx + 0x10], 9
00278F27  8B C5                           mov eax, ebp
00278F29  E9 8D FD FF FF                  jmp 0x140278cbb
00278F2E  83 4A 10 09                     or dword ptr [rdx + 0x10], 9
00278F32  8B C5                           mov eax, ebp
00278F34  E9 58 FE FF FF                  jmp 0x140278d91
00278F39  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00278F3E  45 8B C7                        mov r8d, r15d
00278F41  48 8B D6                        mov rdx, rsi
00278F44  E8 0B BE 24 00                  call 0x1404c4d54
00278F49  44 8B E0                        mov r12d, eax
00278F4C  45 85 F6                        test r14d, r14d
00278F4F  0F 85 4D FC FF FF               jne 0x140278ba2
00278F55  44 8B F0                        mov r14d, eax
00278F58  85 C0                           test eax, eax
00278F5A  0F 84 42 FC FF FF               je 0x140278ba2
00278F60  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00278F6A  48 8B C0                        mov rax, rax
00278F6D  48 3B F0                        cmp rsi, rax
00278F70  72 13                           jb 0x140278f85
00278F72  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00278F7C  48 3B F0                        cmp rsi, rax
00278F7F  0F 86 1D FC FF FF               jbe 0x140278ba2
00278F85  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00278F89  44 01 77 70                     add dword ptr [rdi + 0x70], r14d
00278F8D  41 8B CC                        mov ecx, r12d
00278F90  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00278F94  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00278F98  E9 1C FB FF FF                  jmp 0x140278ab9
00278F9D  48 8B CB                        mov rcx, rbx
00278FA0  E8 6B EB FA FF                  call 0x140227b10
00278FA5  85 C0                           test eax, eax
00278FA7  0F 84 B0 FE FF FF               je 0x140278e5d
00278FAD  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00278FB2  45 8B C7                        mov r8d, r15d
00278FB5  48 8B D6                        mov rdx, rsi
00278FB8  E8 7F BF 24 00                  call 0x1404c4f3c
00278FBD  4C 8B C8                        mov r9, rax
00278FC0  45 8B C7                        mov r8d, r15d
00278FC3  48 8B D6                        mov rdx, rsi
00278FC6  48 8B CF                        mov rcx, rdi
00278FC9  E8 CA 27 28 00                  call 0x1404fb798
00278FCE  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00278FD2  41 8B CC                        mov ecx, r12d
00278FD5  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00278FD9  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00278FDD  E9 D7 FA FF FF                  jmp 0x140278ab9
00278FE2  48 8B C3                        mov rax, rbx
00278FE5  25 E0 03 00 00                  and eax, 0x3e0
00278FEA  48 3D 00 03 00 00               cmp rax, 0x300
00278FF0  0F 85 D5 FE FF FF               jne 0x140278ecb
00278FF6  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00278FFB  45 8B C7                        mov r8d, r15d
00278FFE  48 8B D6                        mov rdx, rsi
00279001  E8 36 BF 24 00                  call 0x1404c4f3c
00279006  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
0027900A  41 8B CC                        mov ecx, r12d
0027900D  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00279011  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00279015  E9 9F FA FF FF                  jmp 0x140278ab9
0027901A  4D 85 ED                        test r13, r13
0027901D  0F 84 11 FB FF FF               je 0x140278b34
00279023  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00279028  45 8B C7                        mov r8d, r15d
0027902B  48 8B D6                        mov rdx, rsi
0027902E  E8 21 BD 24 00                  call 0x1404c4d54
00279033  41 F6 C6 10                     test r14b, 0x10
00279037  75 03                           jne 0x14027903c
00279039  01 47 70                        add dword ptr [rdi + 0x70], eax
0027903C  8B C0                           mov eax, eax
0027903E  48 C1 E0 03                     shl rax, 3
00279042  48 01 47 58                     add qword ptr [rdi + 0x58], rax
00279046  E9 6E FA FF FF                  jmp 0x140278ab9
0027904B  48 8B CF                        mov rcx, rdi
0027904E  E8 81 8E 25 00                  call 0x1404d1ed4
00279053  E9 3A FB FF FF                  jmp 0x140278b92
00279058  83 FD 02                        cmp ebp, 2
0027905B  0F 84 25 FB FF FF               je 0x140278b86
00279061  4C 8B 87 D0 00 00 00            mov r8, qword ptr [rdi + 0xd0]
00279068  4D 85 C0                        test r8, r8
0027906B  0F 85 57 10 46 00               jne 0x1406da0c8
00279071  4C 8B 47 58                     mov r8, qword ptr [rdi + 0x58]
00279075  4C 89 87 D0 00 00 00            mov qword ptr [rdi + 0xd0], r8
0027907C  E9 47 10 46 00                  jmp 0x1406da0c8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteVa(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p88;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (40);
    a3 = (a2) << (25);
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 160)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 72) = a2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = a2;
    result = (result) << (25);
    a3 = (a3) - (result);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 96) = (unsigned int)((unsigned int)(a3));
    a3 = (a3) >> (16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 56) = a3;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 32);
    v_r13 = *(unsigned __int64 *)(a1 + 32) - 1024;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) != 0) { v_r13 = 0; }
loc_00278A6B:
    if (a2 < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) goto loc_00278AAF;
    if (a2 > a1) goto loc_00278AAF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_00278AAF;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_00278BB6;
loc_00278AAF:
    if (*(unsigned __int64 *)(a2) != 0) goto loc_00278ACD;
loc_00278AB4:
loc_00278AB9:
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
loc_00278ACD:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_00278C21;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16)) == 0) goto loc_00278D21;
loc_00278AE0:
    if (((unsigned int)((unsigned int)(a3))) >= 1) goto loc_00278DAC;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 160)) & (0x810ULL)) != 0) goto loc_0027901A;
loc_00278AFA:
    if (v_r13 == 0) goto loc_00278B34;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_00278B34;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 160)))) & (8)) != 0) goto loc_00278F03;
loc_00278B0E:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 160))) & (146));
    if (((unsigned __int8)(v_r14)) != 130) goto loc_00278B34;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p88 + 184))) >> (24));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00278CE4;
loc_00278B34:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 156)))) & (8)) != 0) goto loc_00278E85;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16)) == 0) goto loc_00278C4B;
loc_00278B52:
    if (sign_flag) goto loc_00278EA7;
loc_00278B5A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 192)) != 1) goto loc_00278CD6;
loc_00278B68:
    v_rbp = ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 96)) != 0) ? 1 : 0;
    v_rbp = (unsigned int)((v_rbp) + 1);
loc_00278B71:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 136)) != 0) goto loc_00279058;
    if ((unsigned int)(v_rbp) == 0) goto loc_0027904B;
loc_00278B86:
    result = MiDecommitAddToList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 56), a3, *(unsigned __int64 *)(a1 + 32));
loc_00278B92:
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_00278EEE;
loc_00278BA2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 192)))) * 8;
    goto loc_00278AB9;
loc_00278BB6:
    if (((*(unsigned __int64 *)(v_rip + 13950663)) & (0x600000ULL)) == 0) goto loc_00278AAF;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00278AAF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00278AAF;
    a1 = (a2) >> (3);
    a1 = (unsigned int)((a1) & (511));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88)) | (32);
    }
    v_rbx = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { v_rbx = result; }
    goto loc_00278AAF;
loc_00278C21:
    if (condition_is_above_or_equal) goto loc_00278E53;
    result = MiDecommitHandleProtoFormatPte(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), *(unsigned __int64 *)(a1 + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 192)))) * 8;
    goto loc_00278AB9;
loc_00278C4B:
    result = MiGetProcessorFlushList(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 192)))) * 8, v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), *(unsigned __int64 *)(a1 + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16) = result;
    *(unsigned int *)(result + 16) = (unsigned int)(v_rbp);
    *(unsigned int *)(result + 20) = 1;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32) + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32) + 184)))) & (15)) != 0) goto loc_00278CA9;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32)) != a1) goto loc_00278F23;
loc_00278CA9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32) + 184)))) & (15)) != 0) goto loc_00278F27;
loc_00278CBB:
    *(unsigned int *)(result + 8) = 1;
    *(unsigned __int16 *)(result + 25) = (unsigned __int16)(v_rbp);
    *(unsigned int *)(result + 28) = (unsigned int)(v_rbp);
    *(unsigned __int64 *)(result + 32) = v_rbp;
    *(unsigned __int64 *)(result + 40) = v_rbp;
    goto loc_00278B52;
loc_00278CD6:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 96)) == ((unsigned int)(v_rbp))) goto loc_00278B71;
    goto loc_00278B68;
loc_00278CE4:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_00278E9B;
loc_00278D06:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12284806) + *(unsigned __int16 *)(a1 + 174) * 8) + 17452))) == 0) goto loc_00278B34;
    result = MI_WSLE_LOG_ACCESS(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    goto loc_00278B34;
loc_00278D21:
    result = MiGetProcessorFlushList(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16) = result;
    *(unsigned int *)(result + 16) = (unsigned int)(v_rbp);
    *(unsigned int *)(result + 20) = 1;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32) + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32) + 184)))) & (15)) != 0) goto loc_00278D7F;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32)) != a1) goto loc_00278F2E;
loc_00278D7F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32) + 184)))) & (15)) != 0) goto loc_00278F32;
loc_00278D91:
    *(unsigned int *)(result + 8) = 1;
    *(unsigned __int16 *)(result + 25) = (unsigned __int16)(v_rbp);
    *(unsigned int *)(result + 28) = (unsigned int)(v_rbp);
    *(unsigned __int64 *)(result + 32) = v_rbp;
    *(unsigned __int64 *)(result + 40) = v_rbp;
    goto loc_00278AE0;
loc_00278DAC:
    result = (v_rbx) >> (7);
    if (condition_is_below) goto loc_00279023;
    result = (unsigned int)(*(unsigned int *)(v_stack_p70));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p70)))) & (4)) != 0) {
        a1 = v_stack_p88;
        a2 = a2;
        result = MiLockNestedPageTable(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    }
    result = MI_READ_PTE_LOCK_FREE(a2, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    result = (result) >> (12);
    result = (result) & (a2);
    v_r14 = (result + result * 2) << (4);
    v_r14 = (v_r14) + (result);
    if (condition_is_above_or_equal) goto loc_00278EF6;
    v_r14 = (*(unsigned __int64 *)(v_r14)) >> (32);
loc_00278E1B:
    v_r14 = (unsigned int)((v_r14) & (0x3FFULL));
    result = (unsigned int)(*(unsigned int *)(v_stack_p70));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p70)))) & (4)) != 0) {
        a1 = v_stack_p88;
        a2 = a2;
        result = MiUnlockPageTable(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    }
    if ((unsigned int)(v_r14) != 0) goto loc_00278AB4;
    goto loc_00278AFA;
loc_00278E53:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p80)) & (16));
    if (condition_is_not_equal) goto loc_00278F9D;
loc_00278E5D:
    if (condition_is_below) goto loc_00278EB5;
    result = MiDecommitHandlePageFileFormatPte(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)(result)) * 8;
    goto loc_00278AB9;
loc_00278E85:
    result = MiReturnPagedPoolLockCharge(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    goto loc_00278B92;
loc_00278E9B:
    goto loc_00278D06;
loc_00278EA7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 96)) != ((unsigned int)(v_rbp))) goto loc_00278B71;
    goto loc_00278B5A;
loc_00278EB5:
    if (((v_stack_p80) & (0x800ULL)) != 0) goto loc_00278F39;
    if (1 != 0) goto loc_00278FE2;
loc_00278ECB:
    result = MiDecommitHandleTransitionPte(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 32), *(unsigned __int64 *)(a1 + 32));
    if ((unsigned int)(result) != 0) goto loc_00278BA2;
    goto loc_00278A6B;
loc_00278EEE:
    goto loc_00278BA2;
loc_00278EF6:
    v_r14 = (*(unsigned __int64 *)((unsigned int)(v_stack_p80) + 16)) >> (16);
    goto loc_00278E1B;
loc_00278F03:
    a3 = 0;
    result = MiDeleteRotateVa(v_stack_p70, a2, a3, *(unsigned __int64 *)(a1 + 32));
    if ((unsigned int)(result) == 0) goto loc_00278B0E;
    goto loc_00278F60;
loc_00278F23:
loc_00278F27:
    goto loc_00278CBB;
loc_00278F2E:
loc_00278F32:
    goto loc_00278D91;
loc_00278F39:
    result = MiDeleteLargeUserPde(v_stack_p70, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int64 *)(a1 + 32));
    if (1 != 0) goto loc_00278BA2;
    if ((unsigned int)(result) == 0) goto loc_00278BA2;
loc_00278F60:
    if (a2 < result) goto loc_00278F85;
    if (a2 <= result) goto loc_00278BA2;
loc_00278F85:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8;
    goto loc_00278AB9;
loc_00278F9D:
    result = MiIsLazyStampedPte(v_rbx, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int64 *)(a1 + 32));
    if ((unsigned int)(result) == 0) goto loc_00278E5D;
    result = MiDeleteVadAwePtes(v_stack_p70, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int64 *)(a1 + 32));
    result = MiDecommitAddTbFlushEntries(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8;
    goto loc_00278AB9;
loc_00278FE2:
    result = (unsigned int)((v_rbx) & (992));
    if (result != 768) goto loc_00278ECB;
    result = MiDeleteVadAwePtes(v_stack_p70, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8;
    goto loc_00278AB9;
loc_0027901A:
    if (v_r13 == 0) goto loc_00278B34;
loc_00279023:
    result = MiDeleteLargeUserPde(v_stack_p70, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), result);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (16)) == 0) {
    }
    result = ((unsigned int)((unsigned int)(result))) << (3);
    goto loc_00278AB9;
loc_0027904B:
    result = MiDecommitLargePte(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), result);
    goto loc_00278B92;
loc_00279058:
    if (((unsigned int)(v_rbp)) == 2) goto loc_00278B86;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 208) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88);
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteVa(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint32_t v_stack_p80;
    uint64_t v_stack_p88;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (40);
    Arg3 = (Arg2) << (25);
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xA0)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x48) = Arg2;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = Arg2;
    result = (result) << (25);
    Arg3 = (Arg3) - (result);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x60) = (uint32_t)((uint32_t)(Arg3));
    Arg3 = (Arg3) >> (16);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x38) = Arg3;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x20);
    local_r13 = *(uint64_t *)(arg1 + 0x20) - 1024;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) != 0) { local_r13 = 0; }
loc_00278A6B:
    if (Arg2 < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) goto loc_00278AAF;
    if (Arg2 > Arg1) goto loc_00278AAF;
    if ((((uint8_t)(*(uint64_t *)(Arg2))) & (1)) == 0) goto loc_00278AAF;
    Arg2 = ((((uint8_t)(*(uint64_t *)(Arg2))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg2))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_00278BB6;
loc_00278AAF:
    if (*(uint64_t *)(Arg2) != 0) goto loc_00278ACD;
loc_00278AB4:
loc_00278AB9:
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
loc_00278ACD:
    if ((((uint8_t)(*(uint64_t *)(Arg2))) & (1)) == 0) goto loc_00278C21;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10)) == 0) goto loc_00278D21;
loc_00278AE0:
    if (((uint32_t)((uint32_t)(Arg3))) >= 1) goto loc_00278DAC;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xA0)) & (0x810ULL)) != 0) goto loc_0027901A;
loc_00278AFA:
    if (local_r13 == 0) goto loc_00278B34;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_00278B34;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xA0)))) & (8)) != 0) goto loc_00278F03;
loc_00278B0E:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xA0))) & (146));
    if (((uint8_t)(local_r14)) != 130) goto loc_00278B34;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p88 + 0xB8))) >> (24));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00278CE4;
loc_00278B34:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x9C)))) & (8)) != 0) goto loc_00278E85;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10)) == 0) goto loc_00278C4B;
loc_00278B52:
    if (sign_flag) goto loc_00278EA7;
loc_00278B5A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xC0)) != 1) goto loc_00278CD6;
loc_00278B68:
    local_rbp = ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x60)) != 0) ? 1 : 0;
    local_rbp = (uint32_t)((local_rbp) + 1);
loc_00278B71:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x88)) != 0) goto loc_00279058;
    if ((uint32_t)(local_rbp) == 0) goto loc_0027904B;
loc_00278B86:
    result = MiDecommitAddToList(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x38), Arg3, *(uint64_t *)(arg1 + 0x20));
loc_00278B92:
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_00278EEE;
loc_00278BA2:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xC0)))) * 8;
    goto loc_00278AB9;
loc_00278BB6:
    if (((*(uint64_t *)(v_rip + 0xD4DEC7)) & (0x600000ULL)) == 0) goto loc_00278AAF;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00278AAF;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00278AAF;
    Arg1 = (Arg2) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58)) | (32);
    }
    local_rbx = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { local_rbx = result; }
    goto loc_00278AAF;
loc_00278C21:
    if (condition_is_above_or_equal) goto loc_00278E53;
    result = MiDecommitHandleProtoFormatPte(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), *(uint64_t *)(arg1 + 0x20));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xC0)))) * 8;
    goto loc_00278AB9;
loc_00278C4B:
    result = MiGetProcessorFlushList(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xC0)))) * 8, local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), *(uint64_t *)(arg1 + 0x20));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10) = result;
    *(uint32_t *)(result + 0x10) = (uint32_t)(local_rbp);
    *(uint32_t *)(result + 0x14) = 1;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20) + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    *(uint8_t *)(result + 0x18) = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20) + 0xB8)))) & (15)) != 0) goto loc_00278CA9;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20)) != Arg1) goto loc_00278F23;
loc_00278CA9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20) + 0xB8)))) & (15)) != 0) goto loc_00278F27;
loc_00278CBB:
    *(uint32_t *)(result + 0x8) = 1;
    *(uint16_t *)(result + 0x19) = (uint16_t)(local_rbp);
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_rbp);
    *(uint64_t *)(result + 0x20) = local_rbp;
    *(uint64_t *)(result + 0x28) = local_rbp;
    goto loc_00278B52;
loc_00278CD6:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x60)) == ((uint32_t)(local_rbp))) goto loc_00278B71;
    goto loc_00278B68;
loc_00278CE4:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) goto loc_00278E9B;
loc_00278D06:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB7386) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x442C))) == 0) goto loc_00278B34;
    result = MI_WSLE_LOG_ACCESS(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    goto loc_00278B34;
loc_00278D21:
    result = MiGetProcessorFlushList(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10) = result;
    *(uint32_t *)(result + 0x10) = (uint32_t)(local_rbp);
    *(uint32_t *)(result + 0x14) = 1;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20) + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    *(uint8_t *)(result + 0x18) = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20) + 0xB8)))) & (15)) != 0) goto loc_00278D7F;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20)) != Arg1) goto loc_00278F2E;
loc_00278D7F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20) + 0xB8)))) & (15)) != 0) goto loc_00278F32;
loc_00278D91:
    *(uint32_t *)(result + 0x8) = 1;
    *(uint16_t *)(result + 0x19) = (uint16_t)(local_rbp);
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_rbp);
    *(uint64_t *)(result + 0x20) = local_rbp;
    *(uint64_t *)(result + 0x28) = local_rbp;
    goto loc_00278AE0;
loc_00278DAC:
    result = (local_rbx) >> (7);
    if (condition_is_below) goto loc_00279023;
    result = (uint32_t)(*(uint32_t *)(v_stack_p70));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p70)))) & (4)) != 0) {
        Arg1 = v_stack_p88;
        Arg2 = Arg2;
        result = MiLockNestedPageTable(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    }
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    result = (result) >> (12);
    result = (result) & (Arg2);
    local_r14 = (result + result * 2) << (4);
    local_r14 = (local_r14) + (result);
    if (condition_is_above_or_equal) goto loc_00278EF6;
    local_r14 = (*(uint64_t *)(local_r14)) >> (32);
loc_00278E1B:
    local_r14 = (uint32_t)((local_r14) & (0x3FFULL));
    result = (uint32_t)(*(uint32_t *)(v_stack_p70));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p70)))) & (4)) != 0) {
        Arg1 = v_stack_p88;
        Arg2 = Arg2;
        result = MiUnlockPageTable(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    }
    if ((uint32_t)(local_r14) != 0) goto loc_00278AB4;
    goto loc_00278AFA;
loc_00278E53:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p80)) & (16));
    if (condition_is_not_equal) goto loc_00278F9D;
loc_00278E5D:
    if (condition_is_below) goto loc_00278EB5;
    result = MiDecommitHandlePageFileFormatPte(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)(result)) * 8;
    goto loc_00278AB9;
loc_00278E85:
    result = MiReturnPagedPoolLockCharge(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    goto loc_00278B92;
loc_00278E9B:
    goto loc_00278D06;
loc_00278EA7:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x60)) != ((uint32_t)(local_rbp))) goto loc_00278B71;
    goto loc_00278B5A;
loc_00278EB5:
    if (((v_stack_p80) & (0x800ULL)) != 0) goto loc_00278F39;
    if (1 != 0) goto loc_00278FE2;
loc_00278ECB:
    result = MiDecommitHandleTransitionPte(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x20), *(uint64_t *)(arg1 + 0x20));
    if ((uint32_t)(result) != 0) goto loc_00278BA2;
    goto loc_00278A6B;
loc_00278EEE:
    goto loc_00278BA2;
loc_00278EF6:
    local_r14 = (*(uint64_t *)((uint32_t)(v_stack_p80) + 0x10)) >> (16);
    goto loc_00278E1B;
loc_00278F03:
    Arg3 = 0;
    result = MiDeleteRotateVa(v_stack_p70, Arg2, Arg3, *(uint64_t *)(arg1 + 0x20));
    if ((uint32_t)(result) == 0) goto loc_00278B0E;
    goto loc_00278F60;
loc_00278F23:
loc_00278F27:
    goto loc_00278CBB;
loc_00278F2E:
loc_00278F32:
    goto loc_00278D91;
loc_00278F39:
    result = MiDeleteLargeUserPde(v_stack_p70, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint64_t *)(arg1 + 0x20));
    if (1 != 0) goto loc_00278BA2;
    if ((uint32_t)(result) == 0) goto loc_00278BA2;
loc_00278F60:
    if (Arg2 < result) goto loc_00278F85;
    if (Arg2 <= result) goto loc_00278BA2;
loc_00278F85:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8;
    goto loc_00278AB9;
loc_00278F9D:
    result = MiIsLazyStampedPte(local_rbx, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint64_t *)(arg1 + 0x20));
    if ((uint32_t)(result) == 0) goto loc_00278E5D;
    result = MiDeleteVadAwePtes(v_stack_p70, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint64_t *)(arg1 + 0x20));
    result = MiDecommitAddTbFlushEntries(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), result);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8;
    goto loc_00278AB9;
loc_00278FE2:
    result = (uint32_t)((local_rbx) & (992));
    if (result != 768) goto loc_00278ECB;
    result = MiDeleteVadAwePtes(v_stack_p70, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), result);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8;
    goto loc_00278AB9;
loc_0027901A:
    if (local_r13 == 0) goto loc_00278B34;
loc_00279023:
    result = MiDeleteLargeUserPde(v_stack_p70, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), result);
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (16)) == 0) {
    }
    result = ((uint32_t)((uint32_t)(result))) << (3);
    goto loc_00278AB9;
loc_0027904B:
    result = MiDecommitLargePte(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), result);
    goto loc_00278B92;
loc_00279058:
    if (((uint32_t)(local_rbp)) == 2) goto loc_00278B86;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xD0) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002789E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
