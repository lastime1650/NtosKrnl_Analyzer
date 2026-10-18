# MiValidateInPage

- RVA: `0x00382E0C`–`0x003833BE` (길이 `1,458` bytes)
- VA: `0x0000000140382E0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007BB5C`
- 디코드: `331`개 명령, `1,458/1,458` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00382FE4` → [MiInPageSkipPage](../2B/MiInPageSkipPage_function_002B7820.md) (function, `0x002B7820`)
- `0x0038303F` → [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) (function, `0x0093F2A8`)
- `0x00383112` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x00383142` → [MiCanPageMove](MiCanPageMove_function_00383710.md) (function, `0x00383710`)
- `0x0038316D` → [MiMarkPfnVerified](MiMarkPfnVerified_function_003833C4.md) (function, `0x003833C4`)
- `0x003831B6` → [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) (function, `0x0093EA08`)
- `0x00383224` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x0038324B` → [MiControlAreaHasHostRelocationsApplied](MiControlAreaHasHostRelocationsApplied_function_003843A4.md) (function, `0x003843A4`)
- `0x003832A6` → [SeValidateImageData](../../page/93/SeValidateImageData_function_0093ED98.md) (function, `0x0093ED98`)
- `0x003832CF` → [MiApplyDebuggerPatches](../4F/MiApplyDebuggerPatches_function_004F7BE4.md) (function, `0x004F7BE4`)
- `0x00383313` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x0038335A` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x003833AC` → [MiGetSectionStrongImageReference](../../page/93/MiGetSectionStrongImageReference_function_0093E9C0.md) (function, `0x0093E9C0`)

### Direct callers
- [MiWaitForInPageComplete](MiWaitForInPageComplete_function_00380AB8.md) at `0x00380D6D`

### Static image references
- `0x00382F48` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0038303F` → [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) (`.text` → `PAGE`)
  - `0x003831B6` → [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) (`.text` → `PAGE`)
  - `0x003832A6` → [SeValidateImageData](../../page/93/SeValidateImageData_function_0093ED98.md) (`.text` → `PAGE`)
  - `0x003833AC` → [MiGetSectionStrongImageReference](../../page/93/MiGetSectionStrongImageReference_function_0093E9C0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00383217` → [sub_006E4818 + 0x9A](../6E/Unknown_function_006E4818.md) (`tail-transfer`)
  - `0x0038322A` → [sub_006E4818 + 0x9A](../6E/Unknown_function_006E4818.md) (`tail-transfer`)
  - `0x003832F5` → [sub_006E4818](../6E/Unknown_function_006E4818.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00382E0C  40 53                           push rbx
00382E0E  55                              push rbp
00382E0F  56                              push rsi
00382E10  57                              push rdi
00382E11  41 54                           push r12
00382E13  41 55                           push r13
00382E15  41 56                           push r14
00382E17  41 57                           push r15
00382E19  48 83 EC 78                     sub rsp, 0x78
00382E1D  48 8B 81 00 01 00 00            mov rax, qword ptr [rcx + 0x100]
00382E24  48 8D A9 10 01 00 00            lea rbp, [rcx + 0x110]
00382E2B  48 8B 91 D0 00 00 00            mov rdx, qword ptr [rcx + 0xd0]
00382E32  33 DB                           xor ebx, ebx
00382E34  44 8B A1 B8 00 00 00            mov r12d, dword ptr [rcx + 0xb8]
00382E3B  48 8B F1                        mov rsi, rcx
00382E3E  41 B9 FF 0F 00 00               mov r9d, 0xfff
00382E44  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
00382E4B  4C 8B 12                        mov r10, qword ptr [rdx]
00382E4E  4C 89 54 24 58                  mov qword ptr [rsp + 0x58], r10
00382E53  4D 8B 72 60                     mov r14, qword ptr [r10 + 0x60]
00382E57  49 83 E6 F8                     and r14, 0xfffffffffffffff8
00382E5B  48 85 C0                        test rax, rax
00382E5E  48 0F 45 E8                     cmovne rbp, rax
00382E62  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00382E6B  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00382E72  4C 8D 45 30                     lea r8, [rbp + 0x30]
00382E76  8B 4D 20                        mov ecx, dword ptr [rbp + 0x20]
00382E79  4C 8D 6D 30                     lea r13, [rbp + 0x30]
00382E7D  03 4D 2C                        add ecx, dword ptr [rbp + 0x2c]
00382E80  44 8B 7D 28                     mov r15d, dword ptr [rbp + 0x28]
00382E84  49 23 C9                        and rcx, r9
00382E87  4D 03 F9                        add r15, r9
00382E8A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00382E8F  4C 03 F9                        add r15, rcx
00382E92  49 C1 EF 0C                     shr r15, 0xc
00382E96  41 8B C7                        mov eax, r15d
00382E99  4D 8D 04 C0                     lea r8, [r8 + rax*8]
00382E9D  49 8D 82 80 00 00 00            lea rax, [r10 + 0x80]
00382EA4  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00382EA9  48 3B D0                        cmp rdx, rax
00382EAC  0F 84 2A 04 00 00               je 0x1403832dc
00382EB2  41 8B C4                        mov eax, r12d
00382EB5  89 9C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ebx
00382EBC  2B 45 2C                        sub eax, dword ptr [rbp + 0x2c]
00382EBF  48 B9 F8 FF FF FF FF FF FF 7F   movabs rcx, 0x7ffffffffffffff8
00382EC9  2B 45 28                        sub eax, dword ptr [rbp + 0x28]
00382ECC  48 01 46 60                     add qword ptr [rsi + 0x60], rax
00382ED0  8B C3                           mov eax, ebx
00382ED2  44 2B 65 2C                     sub r12d, dword ptr [rbp + 0x2c]
00382ED6  44 2B 65 28                     sub r12d, dword ptr [rbp + 0x28]
00382EDA  45 85 E1                        test r9d, r12d
00382EDD  0F 95 C0                        setne al
00382EE0  41 C1 EC 0C                     shr r12d, 0xc
00382EE4  41 03 C4                        add eax, r12d
00382EE7  01 86 BC 00 00 00               add dword ptr [rsi + 0xbc], eax
00382EED  49 8B 7E 28                     mov rdi, qword ptr [r14 + 0x28]
00382EF1  48 8B C7                        mov rax, rdi
00382EF4  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00382EF8  48 3B C8                        cmp rcx, rax
00382EFB  49 8B 45 00                     mov rax, qword ptr [r13]
00382EFF  1B C9                           sbb ecx, ecx
00382F01  83 E1 02                        and ecx, 2
00382F04  48 8D 14 40                     lea rdx, [rax + rax*2]
00382F08  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00382F12  48 C1 E2 04                     shl rdx, 4
00382F16  48 8B C0                        mov rax, rax
00382F19  48 03 D0                        add rdx, rax
00382F1C  44 8B 5A 10                     mov r11d, dword ptr [rdx + 0x10]
00382F20  49 C1 EB 05                     shr r11, 5
00382F24  41 83 E3 1F                     and r11d, 0x1f
00382F28  41 F7 42 5C 00 00 0C 00         test dword ptr [r10 + 0x5c], 0xc0000
00382F30  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
00382F35  41 0F 95 C1                     setne r9b
00382F39  F6 C1 02                        test cl, 2
00382F3C  0F 95 C0                        setne al
00382F3F  41 84 C1                        test r9b, al
00382F42  0F 85 1C 04 00 00               jne 0x140383364
00382F48  48 0F BA 25 37 3B C4 00 11      bt qword ptr [rip + 0xc43b37], 0x11
00382F51  44 8B C1                        mov r8d, ecx
00382F54  0F 82 15 04 00 00               jb 0x14038336f
00382F5A  49 39 5E 20                     cmp qword ptr [r14 + 0x20], rbx
00382F5E  0F 85 C0 01 00 00               jne 0x140383124
00382F64  41 8B D8                        mov ebx, r8d
00382F67  41 8B C3                        mov eax, r11d
00382F6A  83 CB 10                        or ebx, 0x10
00382F6D  41 F6 42 60 01                  test byte ptr [r10 + 0x60], 1
00382F72  41 0F 44 D8                     cmove ebx, r8d
00382F76  83 E0 02                        and eax, 2
00382F79  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
00382F80  0F 85 7E 02 00 00               jne 0x140383204
00382F86  45 33 C0                        xor r8d, r8d
00382F89  45 8B E0                        mov r12d, r8d
00382F8C  F6 C3 02                        test bl, 2
00382F8F  0F 85 9A 02 00 00               jne 0x14038322f
00382F95  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00382F9A  49 8B F8                        mov rdi, r8
00382F9D  4C 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r8
00382FA5  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00382FAF  4C 3B 6C 24 60                  cmp r13, qword ptr [rsp + 0x60]
00382FB4  0F 83 D3 00 00 00               jae 0x14038308d
00382FBA  49 8B 45 00                     mov rax, qword ptr [r13]
00382FBE  48 8D 0C 40                     lea rcx, [rax + rax*2]
00382FC2  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00382FCC  48 C1 E1 04                     shl rcx, 4
00382FD0  48 8B C0                        mov rax, rax
00382FD3  48 03 C8                        add rcx, rax
00382FD6  8D 04 9D 00 00 00 00            lea eax, [rbx*4]
00382FDD  33 C3                           xor eax, ebx
00382FDF  83 E0 20                        and eax, 0x20
00382FE2  33 D8                           xor ebx, eax
00382FE4  E8 37 48 F3 FF                  call 0x1402b7820
00382FE9  85 C0                           test eax, eax
00382FEB  75 71                           jne 0x14038305e
00382FED  4D 85 E4                        test r12, r12
00382FF0  0F 85 70 01 00 00               jne 0x140383166
00382FF6  F6 C3 02                        test bl, 2
00382FF9  0F 85 85 01 00 00               jne 0x140383184
00382FFF  4D 8B F0                        mov r14, r8
00383002  F6 C3 30                        test bl, 0x30
00383005  74 0A                           je 0x140383011
00383007  F6 45 0A 01                     test byte ptr [rbp + 0xa], 1
0038300B  0F 85 95 00 00 00               jne 0x1403830a6
00383011  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00383016  F6 C3 20                        test bl, 0x20
00383019  0F 84 04 03 00 00               je 0x140383323
0038301F  4D 8B 4D 00                     mov r9, qword ptr [r13]
00383023  33 C9                           xor ecx, ecx
00383025  44 8B 86 BC 00 00 00            mov r8d, dword ptr [rsi + 0xbc]
0038302C  49 8B D6                        mov rdx, r14
0038302F  C7 44 24 30 21 00 00 00         mov dword ptr [rsp + 0x30], 0x21
00383037  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0038303C  49 8B CF                        mov rcx, r15
0038303F  E8 64 C2 5B 00                  call 0x14093f2a8
00383044  45 33 C0                        xor r8d, r8d
00383047  85 C0                           test eax, eax
00383049  78 3B                           js 0x140383086
0038304B  F6 C3 10                        test bl, 0x10
0038304E  0F 85 65 02 00 00               jne 0x1403832b9
00383054  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0038305E  48 81 46 60 00 10 00 00         add qword ptr [rsi + 0x60], 0x1000
00383066  48 83 C7 08                     add rdi, 8
0038306A  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0038306F  49 83 C5 08                     add r13, 8
00383073  FF 86 BC 00 00 00               inc dword ptr [rsi + 0xbc]
00383079  48 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdi
00383081  E9 29 FF FF FF                  jmp 0x140382faf
00383086  C7 46 50 9A 00 00 C0            mov dword ptr [rsi + 0x50], 0xc000009a
0038308D  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00383094  48 83 C4 78                     add rsp, 0x78
00383098  41 5F                           pop r15
0038309A  41 5E                           pop r14
0038309C  41 5D                           pop r13
0038309E  41 5C                           pop r12
003830A0  5F                              pop rdi
003830A1  5E                              pop rsi
003830A2  5D                              pop rbp
003830A3  5B                              pop rbx
003830A4  C3                              ret
003830A5  CC                              int3
003830A6  4C 8B F7                        mov r14, rdi
003830A9  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003830B3  49 C1 FE 03                     sar r14, 3
003830B7  49 C1 E6 0C                     shl r14, 0xc
003830BB  4C 03 75 18                     add r14, qword ptr [rbp + 0x18]
003830BF  4D 8B FE                        mov r15, r14
003830C2  49 C1 EF 09                     shr r15, 9
003830C6  4C 23 F8                        and r15, rax
003830C9  48 8B C2                        mov rax, rdx
003830CC  4C 03 F8                        add r15, rax
003830CF  49 8B 3F                        mov rdi, qword ptr [r15]
003830D2  40 F6 C7 42                     test dil, 0x42
003830D6  75 3F                           jne 0x140383117
003830D8  48 81 CF 42 08 00 00            or rdi, 0x842
003830DF  48 0F BA 25 A0 39 C4 00 24      bt qword ptr [rip + 0xc439a0], 0x24
003830E8  0F 82 3D 02 00 00               jb 0x14038332b
003830EE  48 8B 05 93 39 C4 00            mov rax, qword ptr [rip + 0xc43993]
003830F5  49 89 3F                        mov qword ptr [r15], rdi
003830F8  48 0F BA E0 08                  bt rax, 8
003830FD  72 18                           jb 0x140383117
003830FF  48 0F BA E0 09                  bt rax, 9
00383104  72 11                           jb 0x140383117
00383106  BA 02 00 00 00                  mov edx, 2
0038310B  49 8B CE                        mov rcx, r14
0038310E  44 8D 42 1E                     lea r8d, [rdx + 0x1e]
00383112  E8 19 B6 F0 FF                  call 0x14028e730
00383117  48 8B BC 24 C8 00 00 00         mov rdi, qword ptr [rsp + 0xc8]
0038311F  E9 ED FE FF FF                  jmp 0x140383011
00383124  48 0F BA 25 5B 39 C4 00 11      bt qword ptr [rip + 0xc4395b], 0x11
0038312D  72 20                           jb 0x14038314f
0038312F  41 F6 C3 02                     test r11b, 2
00383133  0F 95 C0                        setne al
00383136  41 84 C1                        test r9b, al
00383139  0F 85 25 FE FF FF               jne 0x140382f64
0038313F  48 8B CA                        mov rcx, rdx
00383142  E8 C9 05 00 00                  call 0x140383710
00383147  85 C0                           test eax, eax
00383149  0F 84 15 FE FF FF               je 0x140382f64
0038314F  41 83 C8 04                     or r8d, 4
00383153  41 F6 C0 01                     test r8b, 1
00383157  0F 85 2C 02 00 00               jne 0x140383389
0038315D  41 83 C8 08                     or r8d, 8
00383161  E9 FE FD FF FF                  jmp 0x140382f64
00383166  8B 94 24 D0 00 00 00            mov edx, dword ptr [rsp + 0xd0]
0038316D  E8 52 02 00 00                  call 0x1403833c4
00383172  45 33 C0                        xor r8d, r8d
00383175  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0038317F  E9 7B FE FF FF                  jmp 0x140382fff
00383184  49 8B 45 00                     mov rax, qword ptr [r13]
00383188  44 8B 8E BC 00 00 00            mov r9d, dword ptr [rsi + 0xbc]
0038318F  48 8B 56 60                     mov rdx, qword ptr [rsi + 0x60]
00383193  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00383198  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
003831A0  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
003831A5  4D 8B C6                        mov r8, r14
003831A8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003831AD  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003831B2  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003831B6  E8 4D B8 5B 00                  call 0x14093ea08
003831BB  45 33 C0                        xor r8d, r8d
003831BE  85 C0                           test eax, eax
003831C0  79 B3                           jns 0x140383175
003831C2  3D 9A 00 00 C0                  cmp eax, 0xc000009a
003831C7  0F 84 B9 FE FF FF               je 0x140383086
003831CD  8B C3                           mov eax, ebx
003831CF  C7 84 24 D8 00 00 00 34 04 00 C0  mov dword ptr [rsp + 0xd8], 0xc0000434
003831DA  83 E0 05                        and eax, 5
003831DD  3C 05                           cmp al, 5
003831DF  75 94                           jne 0x140383175
003831E1  48 F7 05 9C 38 C4 00 00 20 00 00  test qword ptr [rip + 0xc4389c], 0x2000
003831EC  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
003831F6  0F 84 03 FE FF FF               je 0x140382fff
003831FC  83 CB 20                        or ebx, 0x20
003831FF  E9 FB FD FF FF                  jmp 0x140382fff
00383204  48 0F BA 25 7B 38 C4 00 11      bt qword ptr [rip + 0xc4387b], 0x11
0038320D  0F 83 73 FD FF FF               jae 0x140382f86
00383213  F6 45 0A 01                     test byte ptr [rbp + 0xa], 1
00383217  0F 84 95 16 36 00               je 0x1406e48b2
0038321D  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
00383221  48 8B D5                        mov rdx, rbp
00383224  E8 37 3C EC FF                  call 0x140246e60
00383229  90                              nop
0038322A  E9 83 16 36 00                  jmp 0x1406e48b2
0038322F  41 83 FF 01                     cmp r15d, 1
00383233  0F 86 5C FD FF FF               jbe 0x140382f95
00383239  0F B7 55 0A                     movzx edx, word ptr [rbp + 0xa]
0038323D  66 0F BA E2 0E                  bt dx, 0xe
00383242  0F 83 4D FD FF FF               jae 0x140382f95
00383248  49 8B CA                        mov rcx, r10
0038324B  E8 54 11 00 00                  call 0x1403843a4
00383250  85 C0                           test eax, eax
00383252  0F 85 3D FD FF FF               jne 0x140382f95
00383258  F6 C2 05                        test dl, 5
0038325B  0F 84 99 00 00 00               je 0x1403832fa
00383261  4C 8B 65 18                     mov r12, qword ptr [rbp + 0x18]
00383265  4D 85 E4                        test r12, r12
00383268  0F 84 27 FD FF FF               je 0x140382f95
0038326E  48 83 E7 F8                     and rdi, 0xfffffffffffffff8
00383272  F6 C3 01                        test bl, 1
00383275  0F 85 24 01 00 00               jne 0x14038339f
0038327B  F7 9C 24 C8 00 00 00            neg dword ptr [rsp + 0xc8]
00383282  49 8B D4                        mov rdx, r12
00383285  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0038328A  48 8B CF                        mov rcx, rdi
0038328D  4C 8B 4E 60                     mov r9, qword ptr [rsi + 0x60]
00383291  1B C0                           sbb eax, eax
00383293  83 E0 02                        and eax, 2
00383296  41 C1 E7 0C                     shl r15d, 0xc
0038329A  45 8B C7                        mov r8d, r15d
0038329D  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
003832A2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003832A6  E8 ED BA 5B 00                  call 0x14093ed98
003832AB  45 33 C0                        xor r8d, r8d
003832AE  85 C0                           test eax, eax
003832B0  4D 0F 48 E0                     cmovs r12, r8
003832B4  E9 E1 FC FF FF                  jmp 0x140382f9a
003832B9  4D 8B 4D 00                     mov r9, qword ptr [r13]
003832BD  49 8B D6                        mov rdx, r14
003832C0  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
003832C5  49 8B CF                        mov rcx, r15
003832C8  44 8B 86 BC 00 00 00            mov r8d, dword ptr [rsi + 0xbc]
003832CF  E8 10 49 17 00                  call 0x1404f7be4
003832D4  45 33 C0                        xor r8d, r8d
003832D7  E9 78 FD FF FF                  jmp 0x140383054
003832DC  45 85 4E 38                     test dword ptr [r14 + 0x38], r9d
003832E0  0F 84 CC FB FF FF               je 0x140382eb2
003832E6  8B 4A 2C                        mov ecx, dword ptr [rdx + 0x2c]
003832E9  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003832ED  48 8D 51 FF                     lea rdx, [rcx - 1]
003832F1  48 8D 14 D0                     lea rdx, [rax + rdx*8]
003832F5  E9 1E 15 36 00                  jmp 0x1406e4818
003832FA  45 33 C9                        xor r9d, r9d
003832FD  C7 44 24 28 10 00 00 C0         mov dword ptr [rsp + 0x28], 0xc0000010
00383305  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0038330A  33 D2                           xor edx, edx
0038330C  48 8B CD                        mov rcx, rbp
0038330F  45 8D 41 01                     lea r8d, [r9 + 1]
00383313  E8 E8 54 F9 FF                  call 0x140318800
00383318  4C 8B E0                        mov r12, rax
0038331B  45 33 C0                        xor r8d, r8d
0038331E  E9 42 FF FF FF                  jmp 0x140383265
00383323  45 33 C0                        xor r8d, r8d
00383326  E9 20 FD FF FF                  jmp 0x14038304b
0038332B  40 F6 C7 20                     test dil, 0x20
0038332F  0F 85 B9 FD FF FF               jne 0x1403830ee
00383335  48 8B C2                        mov rax, rdx
00383338  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00383342  48 03 C1                        add rax, rcx
00383345  4C 3B F8                        cmp r15, rax
00383348  0F 82 A0 FD FF FF               jb 0x1403830ee
0038334E  41 B8 80 00 00 00               mov r8d, 0x80
00383354  48 8B D7                        mov rdx, rdi
00383357  49 8B CF                        mov rcx, r15
0038335A  E8 21 FA F0 FF                  call 0x140292d80
0038335F  E9 8A FD FF FF                  jmp 0x1403830ee
00383364  83 C9 01                        or ecx, 1
00383367  44 8B C1                        mov r8d, ecx
0038336A  E9 EB FB FF FF                  jmp 0x140382f5a
0038336F  41 F6 C3 02                     test r11b, 2
00383373  0F 84 E1 FB FF FF               je 0x140382f5a
00383379  C7 84 24 D0 00 00 00 03 00 00 00  mov dword ptr [rsp + 0xd0], 3
00383384  E9 D1 FB FF FF                  jmp 0x140382f5a
00383389  48 F7 05 F4 36 C4 00 00 20 00 00  test qword ptr [rip + 0xc436f4], 0x2000
00383394  0F 85 CA FB FF FF               jne 0x140382f64
0038339A  E9 BE FD FF FF                  jmp 0x14038315d
0038339F  4D 39 46 40                     cmp qword ptr [r14 + 0x40], r8
003833A3  0F 85 D2 FE FF FF               jne 0x14038327b
003833A9  49 8B CE                        mov rcx, r14
003833AC  E8 0F B6 5B 00                  call 0x14093e9c0
003833B1  85 C0                           test eax, eax
003833B3  0F 88 DB FC FF FF               js 0x140383094
003833B9  E9 BD FE FF FF                  jmp 0x14038327b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiValidateInPage(__int64 a1)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pD0;
    unsigned int v_stack_pD8;

    v_rsp = (v_rsp) - (120);
    v_rbx = 0;
    v_stack_p20 = 0;
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208));
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208)) + 96)) & (-8);
    v_rbp = a1 + 272;
    if (*(unsigned __int64 *)(a1 + 256) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 256); }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 32))) + (*(unsigned int *)(v_rbp + 44)));
    a1 = (a1) & ((unsigned int)(0xFFFULL));
    v_r15 = ((unsigned int)(*(unsigned int *)(v_rbp + 40))) + ((unsigned int)(0xFFFULL));
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_r15 = (v_r15) + (a1);
    v_r15 = (v_r15) >> (12);
    v_stack_m58 = v_rbp + 48 + (unsigned int)((unsigned int)(v_r15)) * 8;
    if ((*(unsigned __int64 *)(a1 + 208)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208)) + 128)) goto loc_003832DC;
loc_00382EB2:
    v_stack_p18 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184))))) - (*(unsigned int *)(v_rbp + 44)));
    result = (unsigned int)((result) - (*(unsigned int *)(v_rbp + 40)));
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 184))) - (*(unsigned int *)(v_rbp + 44)));
    v_r12 = (unsigned int)((v_r12) - (*(unsigned int *)(v_rbp + 40)));
    result = ((((unsigned int)((unsigned int)(0xFFFULL))) & ((unsigned int)(v_r12))) != 0) ? 1 : 0;
    v_r12 = (unsigned int)((v_r12) >> (12));
    result = (unsigned int)((result) + ((unsigned int)(v_r12)));
    result = (*(unsigned __int64 *)(v_r14 + 40)) & (-8);
    a1 = (unsigned int)((a1) & (2));
    a2 = (*(unsigned __int64 *)(v_rbp + 48) + *(unsigned __int64 *)(v_rbp + 48) * 2) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rbp + 48));
    v_r11 = ((unsigned int)(*(unsigned int *)(a2 + 16))) >> (5);
    v_r11 = (unsigned int)((v_r11) & (31));
    v_stack_m50 = v_r11;
    a4 = (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208)) + 92)) & (0xC0000ULL)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(a1)) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a4)) & ((unsigned __int8)(result))) != 0) goto loc_00383364;
    if (condition_is_below) goto loc_0038336F;
loc_00382F5A:
    if ((*(unsigned __int64 *)(v_r14 + 32)) != 0) goto loc_00383124;
loc_00382F64:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))) | (16));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208)) + 96)) & (1)) == 0) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(a1))); }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) & (2));
    v_stack_p10 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_00383204;
loc_00382F86:
    a3 = 0;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_0038322F;
loc_00382F95:
loc_00382F9A:
    v_stack_p10 = 0;
loc_00382FAF:
    if ((v_rbp + 48) >= v_stack_m58) goto loc_0038308D;
    a1 = (*(unsigned __int64 *)(v_rbp + 48) + *(unsigned __int64 *)(v_rbp + 48) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rbp + 48));
    result = (unsigned int)((v_rbx * 4) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (32));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    result = MiInPageSkipPage(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0038305E;
    if (0 != 0) goto loc_00383166;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00383184;
loc_00382FFF:
    if ((((unsigned __int8)(v_rbx)) & (48)) == 0) goto loc_00383011;
    if (((*(unsigned __int8 *)(v_rbp + 10)) & (1)) != 0) goto loc_003830A6;
loc_00383011:
    if ((((unsigned __int8)(v_rbx)) & (32)) == 0) goto loc_00383323;
    a1 = 0;
    v_stack_m88 = 33;
    v_stack_m98 = 0;
    result = MiRelocateImagePfn(v_stack_m60, 0, (unsigned int)(*(unsigned int *)(a1 + 188)), *(unsigned __int64 *)(v_rbp + 48));
    a3 = 0;
    if (sign_flag) goto loc_00383086;
loc_0038304B:
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_003832B9;
loc_00383054:
loc_0038305E:
    v_rdi = (0) + (8);
    v_r13 = (v_rbp + 48) + (8);
    v_stack_p10 = v_rdi;
    goto loc_00382FAF;
loc_00383086:
    *(unsigned int *)(a1 + 80) = 0xC000009AULL;
loc_0038308D:
loc_00383094:
    v_rsp = (v_rsp) + (120);
    return (unsigned int)(v_stack_p20);
loc_003830A6:
    v_r14 = (v_rdi) >> (3);
    v_r14 = (v_r14) << (12);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(v_rbp + 24));
    v_r15 = (v_r14) >> (9);
    v_r15 = (v_r15) & ((unsigned int)(v_stack_p20));
    v_r15 = (v_r15) + (0);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (66)) != 0) goto loc_00383117;
    v_rdi = (*(unsigned __int64 *)(v_r15)) | (0x842ULL);
    if (condition_is_below) goto loc_0038332B;
loc_003830EE:
    *(unsigned __int64 *)(v_r15) = v_rdi;
    if (condition_is_below) goto loc_00383117;
    result = *(unsigned __int64 *)(v_rip + 12859795);
    if (!(condition_is_below)) {
        a2 = 2;
        a1 = v_r14;
        a3 = a2 + 30;
        result = MiFlushSingleTbEntry(a1, a2, a3, *(unsigned __int64 *)(v_rbp + 48));
    }
    goto loc_00383011;
loc_00383124:
    if (condition_is_below) goto loc_0038314F;
    result = ((((unsigned __int8)(v_r11)) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbp + 48))) & ((unsigned __int8)(result))) != 0) goto loc_00382F64;
    result = MiCanPageMove(a2, a2, a3, *(unsigned __int64 *)(v_rbp + 48));
    if ((unsigned int)(result) == 0) goto loc_00382F64;
loc_0038314F:
    a3 = (unsigned int)((a3) | (4));
    if ((((unsigned __int8)(a3)) & (1)) != 0) goto loc_00383389;
loc_0038315D:
    a3 = (unsigned int)((a3) | (8));
    goto loc_00382F64;
loc_00383166:
    result = MiMarkPfnVerified(a2, (unsigned int)(v_stack_pD0), a3, *(unsigned __int64 *)(v_rbp + 48));
    a3 = 0;
loc_00383175:
    goto loc_00382FFF;
loc_00383184:
    v_stack_p40 = 1;
    v_stack_p38 = 0;
    v_stack_p30 = *(unsigned __int64 *)(v_r13);
    v_stack_p28 = (unsigned int)(v_stack_p68);
    result = MiValidateImagePfn(v_stack_p58, *(unsigned __int64 *)(a1 + 96), v_r14, (unsigned int)(*(unsigned int *)(a1 + 188)));
    a3 = 0;
    if (!sign_flag) goto loc_00383175;
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_00383086;
    v_stack_pD8 = 0xC0000434ULL;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (5));
    if (((unsigned __int8)(result)) != 5) goto loc_00383175;
    if (((*(unsigned __int64 *)(v_rip + 12859548)) & (0x2000ULL)) == 0) goto loc_00382FFF;
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_00382FFF;
loc_00383204:
    if (condition_is_above_or_equal) goto loc_00382F86;
    result = MmUnmapLockedPages(*(unsigned __int64 *)(v_rbp + 24), v_rbp, a3, (unsigned int)(*(unsigned int *)(a1 + 188)));
loc_0038322F:
    if (((unsigned int)(v_r15)) <= 1) goto loc_00382F95;
    if (((unsigned int)(v_r15)) >= 1) goto loc_00382F95;
    result = MiControlAreaHasHostRelocationsApplied(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208)), *(unsigned __int16 *)(v_rbp + 10), a3, (unsigned int)(*(unsigned int *)(a1 + 188)));
    if ((unsigned int)(result) != 0) goto loc_00382F95;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rbp + 10))) & (5)) == 0) goto loc_003832FA;
loc_00383265:
    if (*(unsigned __int64 *)(v_rbp + 24) == 0) goto loc_00382F95;
    v_rdi = (v_stack_pC8) & (-8);
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_0038339F;
loc_0038327B:
    result = (unsigned int)((result) & (2));
    v_r15 = (unsigned int)((v_r15) << (12));
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = (unsigned int)(result);
    result = SeValidateImageData(v_rdi, *(unsigned __int64 *)(v_rbp + 24), (unsigned int)((unsigned int)(v_r15)), *(unsigned __int64 *)(a1 + 96));
    a3 = 0;
    v_r12 = *(unsigned __int64 *)(v_rbp + 24);
    if (sign_flag) { v_r12 = 0; }
    goto loc_00382F9A;
loc_003832B9:
    v_stack_p20 = 0;
    result = MiApplyDebuggerPatches(v_r15, v_stack_p50, (unsigned int)(*(unsigned int *)(a1 + 188)), *(unsigned __int64 *)(v_r13));
    a3 = 0;
    goto loc_00383054;
loc_003832DC:
    if (((*(unsigned int *)(v_stack_p50 + 56)) & ((unsigned int)(*(unsigned __int64 *)(v_r13)))) == 0) goto loc_00382EB2;
loc_003832FA:
    a4 = 0;
    v_stack_p28 = 0xC0000010ULL;
    v_stack_p20 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_rbp, a2, a4 + 1, a4);
    a3 = 0;
    goto loc_00383265;
loc_00383323:
    a3 = 0;
    goto loc_0038304B;
loc_0038332B:
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_003830EE;
    result = (0) + (v_rbp);
    if (v_r15 < result) goto loc_003830EE;
    result = MiCheckLinearProtectedPteAccessedBit(v_r15, v_rdi, 128, a4);
    goto loc_003830EE;
loc_00383364:
    a1 = (unsigned int)((v_r15) | (1));
    goto loc_00382F5A;
loc_0038336F:
    if ((((unsigned __int8)(v_r11)) & (2)) == 0) goto loc_00382F5A;
    v_stack_pD0 = 3;
    goto loc_00382F5A;
loc_00383389:
    if (((*(unsigned __int64 *)(v_rip + 12859124)) & (0x2000ULL)) != 0) goto loc_00382F64;
    goto loc_0038315D;
loc_0038339F:
    if ((*(unsigned __int64 *)(v_stack_p50 + 64)) != ((unsigned int)((unsigned int)(a1)))) goto loc_0038327B;
    result = MiGetSectionStrongImageReference(v_stack_p50, v_rdi, (unsigned int)((unsigned int)(a1)), a4);
    if (sign_flag) goto loc_00383094;
    goto loc_0038327B;
}
```

## 5. (Beta) C Style

```c
int64_t MiValidateInPage(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pD0;
    uint32_t v_stack_pD8;

    local_rsp = (local_rsp) - (120);
    local_rbx = 0;
    v_stack_p20 = 0;
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xD0));
    local_r14 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0)) + 0x60)) & (-8);
    local_rbp = Arg1 + 272;
    if (*(uint64_t *)(arg1 + 0x100) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x100); }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x20))) + (*(uint32_t *)(local_rbp + 0x2C)));
    Arg1 = (Arg1) & ((uint32_t)(0xFFFULL));
    local_r15 = ((uint32_t)(*(uint32_t *)(local_rbp + 0x28))) + ((uint32_t)(0xFFFULL));
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    local_r15 = (local_r15) + (Arg1);
    local_r15 = (local_r15) >> (12);
    v_stack_m58 = local_rbp + 48 + (uint32_t)((uint32_t)(local_r15)) * 8;
    if ((*(uint64_t *)(arg1 + 0xD0)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0)) + 128)) goto loc_003832DC;
loc_00382EB2:
    v_stack_p18 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8))))) - (*(uint32_t *)(local_rbp + 0x2C)));
    result = (uint32_t)((result) - (*(uint32_t *)(local_rbp + 0x28)));
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) - (*(uint32_t *)(local_rbp + 0x2C)));
    local_r12 = (uint32_t)((local_r12) - (*(uint32_t *)(local_rbp + 0x28)));
    result = ((((uint32_t)((uint32_t)(0xFFFULL))) & ((uint32_t)(local_r12))) != 0) ? 1 : 0;
    local_r12 = (uint32_t)((local_r12) >> (12));
    result = (uint32_t)((result) + ((uint32_t)(local_r12)));
    result = (*(uint64_t *)(local_r14 + 0x28)) & (-8);
    Arg1 = (uint32_t)((Arg1) & (2));
    a2 = (*(uint64_t *)(local_rbp + 0x30) + *(uint64_t *)(local_rbp + 0x30) * 2) << (4);
    a2 = (a2) + (*(uint64_t *)(local_rbp + 0x30));
    local_r11 = ((uint32_t)(*(uint32_t *)(a2 + 0x10))) >> (5);
    local_r11 = (uint32_t)((local_r11) & (31));
    v_stack_m50 = local_r11;
    a4 = (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0)) + 0x5C)) & (0xC0000ULL)) != 0) ? 1 : 0;
    result = ((((uint8_t)(Arg1)) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(a4)) & ((uint8_t)(result))) != 0) goto loc_00383364;
    if (condition_is_below) goto loc_0038336F;
loc_00382F5A:
    if ((*(uint64_t *)(local_r14 + 0x20)) != 0) goto loc_00383124;
loc_00382F64:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))) | (16));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0)) + 0x60)) & (1)) == 0) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(Arg1))); }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) & (2));
    v_stack_p10 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_00383204;
loc_00382F86:
    a3 = 0;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_0038322F;
loc_00382F95:
loc_00382F9A:
    v_stack_p10 = 0;
loc_00382FAF:
    if ((local_rbp + 48) >= v_stack_m58) goto loc_0038308D;
    Arg1 = (*(uint64_t *)(local_rbp + 0x30) + *(uint64_t *)(local_rbp + 0x30) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(local_rbp + 0x30));
    result = (uint32_t)((local_rbx * 4) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (32));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    result = MiInPageSkipPage(Arg1, a2, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0038305E;
    if (0 != 0) goto loc_00383166;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00383184;
loc_00382FFF:
    if ((((uint8_t)(local_rbx)) & (48)) == 0) goto loc_00383011;
    if (((*(uint8_t *)(local_rbp + 0xA)) & (1)) != 0) goto loc_003830A6;
loc_00383011:
    if ((((uint8_t)(local_rbx)) & (32)) == 0) goto loc_00383323;
    Arg1 = 0;
    v_stack_m88 = 33;
    v_stack_m98 = 0;
    result = MiRelocateImagePfn(v_stack_m60, 0, (uint32_t)(*(uint32_t *)(arg1 + 0xBC)), *(uint64_t *)(local_rbp + 0x30));
    a3 = 0;
    if (sign_flag) goto loc_00383086;
loc_0038304B:
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_003832B9;
loc_00383054:
loc_0038305E:
    local_rdi = (0) + (8);
    local_r13 = (local_rbp + 48) + (8);
    v_stack_p10 = local_rdi;
    goto loc_00382FAF;
loc_00383086:
    *(uint32_t *)(arg1 + 0x50) = 0xC000009AULL;
loc_0038308D:
loc_00383094:
    local_rsp = (local_rsp) + (120);
    return (uint32_t)(v_stack_p20);
loc_003830A6:
    local_r14 = (local_rdi) >> (3);
    local_r14 = (local_r14) << (12);
    local_r14 = (local_r14) + (*(uint64_t *)(local_rbp + 0x18));
    local_r15 = (local_r14) >> (9);
    local_r15 = (local_r15) & ((uint32_t)(v_stack_p20));
    local_r15 = (local_r15) + (0);
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (66)) != 0) goto loc_00383117;
    local_rdi = (*(uint64_t *)(local_r15)) | (0x842ULL);
    if (condition_is_below) goto loc_0038332B;
loc_003830EE:
    *(uint64_t *)(local_r15) = local_rdi;
    if (condition_is_below) goto loc_00383117;
    result = *(uint64_t *)(v_rip + 0xC43993);
    if (!(condition_is_below)) {
        a2 = 2;
        Arg1 = local_r14;
        a3 = a2 + 30;
        result = MiFlushSingleTbEntry(Arg1, a2, a3, *(uint64_t *)(local_rbp + 0x30));
    }
    goto loc_00383011;
loc_00383124:
    if (condition_is_below) goto loc_0038314F;
    result = ((((uint8_t)(local_r11)) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(*(uint64_t *)(local_rbp + 0x30))) & ((uint8_t)(result))) != 0) goto loc_00382F64;
    result = MiCanPageMove(a2, a2, a3, *(uint64_t *)(local_rbp + 0x30));
    if ((uint32_t)(result) == 0) goto loc_00382F64;
loc_0038314F:
    a3 = (uint32_t)((a3) | (4));
    if ((((uint8_t)(a3)) & (1)) != 0) goto loc_00383389;
loc_0038315D:
    a3 = (uint32_t)((a3) | (8));
    goto loc_00382F64;
loc_00383166:
    result = MiMarkPfnVerified(a2, (uint32_t)(v_stack_pD0), a3, *(uint64_t *)(local_rbp + 0x30));
    a3 = 0;
loc_00383175:
    goto loc_00382FFF;
loc_00383184:
    v_stack_p40 = 1;
    v_stack_p38 = 0;
    v_stack_p30 = *(uint64_t *)(local_r13);
    v_stack_p28 = (uint32_t)(v_stack_p68);
    result = MiValidateImagePfn(v_stack_p58, *(uint64_t *)(arg1 + 0x60), local_r14, (uint32_t)(*(uint32_t *)(arg1 + 0xBC)));
    a3 = 0;
    if (!sign_flag) goto loc_00383175;
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_00383086;
    v_stack_pD8 = 0xC0000434ULL;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (5));
    if (((uint8_t)(result)) != 5) goto loc_00383175;
    if (((*(uint64_t *)(v_rip + 0xC4389C)) & (0x2000ULL)) == 0) goto loc_00382FFF;
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_00382FFF;
loc_00383204:
    if (condition_is_above_or_equal) goto loc_00382F86;
    result = MmUnmapLockedPages(*(uint64_t *)(local_rbp + 0x18), local_rbp, a3, (uint32_t)(*(uint32_t *)(arg1 + 0xBC)));
loc_0038322F:
    if (((uint32_t)(local_r15)) <= 1) goto loc_00382F95;
    if (((uint32_t)(local_r15)) >= 1) goto loc_00382F95;
    result = MiControlAreaHasHostRelocationsApplied(*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0)), *(uint16_t *)(local_rbp + 0xA), a3, (uint32_t)(*(uint32_t *)(arg1 + 0xBC)));
    if ((uint32_t)(result) != 0) goto loc_00382F95;
    if ((((uint8_t)(*(uint16_t *)(local_rbp + 0xA))) & (5)) == 0) goto loc_003832FA;
loc_00383265:
    if (*(uint64_t *)(local_rbp + 0x18) == 0) goto loc_00382F95;
    local_rdi = (v_stack_pC8) & (-8);
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_0038339F;
loc_0038327B:
    result = (uint32_t)((result) & (2));
    local_r15 = (uint32_t)((local_r15) << (12));
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = (uint32_t)(result);
    result = SeValidateImageData(local_rdi, *(uint64_t *)(local_rbp + 0x18), (uint32_t)((uint32_t)(local_r15)), *(uint64_t *)(arg1 + 0x60));
    a3 = 0;
    local_r12 = *(uint64_t *)(local_rbp + 0x18);
    if (sign_flag) { local_r12 = 0; }
    goto loc_00382F9A;
loc_003832B9:
    v_stack_p20 = 0;
    result = MiApplyDebuggerPatches(local_r15, v_stack_p50, (uint32_t)(*(uint32_t *)(arg1 + 0xBC)), *(uint64_t *)(local_r13));
    a3 = 0;
    goto loc_00383054;
loc_003832DC:
    if (((*(uint32_t *)(v_stack_p50 + 0x38)) & ((uint32_t)(*(uint64_t *)(local_r13)))) == 0) goto loc_00382EB2;
loc_003832FA:
    a4 = 0;
    v_stack_p28 = 0xC0000010ULL;
    v_stack_p20 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(local_rbp, a2, a4 + 1, a4);
    a3 = 0;
    goto loc_00383265;
loc_00383323:
    a3 = 0;
    goto loc_0038304B;
loc_0038332B:
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_003830EE;
    result = (0) + (local_rbp);
    if (local_r15 < result) goto loc_003830EE;
    result = MiCheckLinearProtectedPteAccessedBit(local_r15, local_rdi, 128, a4);
    goto loc_003830EE;
loc_00383364:
    Arg1 = (uint32_t)((local_r15) | (1));
    goto loc_00382F5A;
loc_0038336F:
    if ((((uint8_t)(local_r11)) & (2)) == 0) goto loc_00382F5A;
    v_stack_pD0 = 3;
    goto loc_00382F5A;
loc_00383389:
    if (((*(uint64_t *)(v_rip + 0xC436F4)) & (0x2000ULL)) != 0) goto loc_00382F64;
    goto loc_0038315D;
loc_0038339F:
    if ((*(uint64_t *)(v_stack_p50 + 0x40)) != ((uint32_t)((uint32_t)(Arg1)))) goto loc_0038327B;
    result = MiGetSectionStrongImageReference(v_stack_p50, local_rdi, (uint32_t)((uint32_t)(Arg1)), a4);
    if (sign_flag) goto loc_00383094;
    goto loc_0038327B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `32` | `W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R/W` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xBC` | `32` | `R` |
| `Arg1` | `+ 0xBC` | `32` | `R/W` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x110` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00382E0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
