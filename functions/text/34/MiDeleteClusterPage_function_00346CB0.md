# MiDeleteClusterPage

- RVA: `0x00346CB0`–`0x003470FC` (길이 `1,100` bytes)
- VA: `0x0000000140346CB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077FFC`
- 디코드: `290`개 명령, `1,100/1,100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00346CE1` → [MiGetContainingPageTable](MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x00346D13` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00346DD8` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00346F4B` → [MiConvertLockedSmallPageToLarge](MiConvertLockedSmallPageToLarge_function_00347110.md) (function, `0x00347110`)
- `0x00346F9E` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x00347022` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0034703A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0034704A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00347057` → [MiBadShareCount](../37/MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)
- `0x00347067` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00347073` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00347085` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x003470B3` → [MiClearPfnImageVerified](../40/MiClearPfnImageVerified_function_00407000.md) (function, `0x00407000`)

### Direct callers
- [MiDecommitFreePagesTail](../41/MiDecommitFreePagesTail_function_0041ECE0.md) at `0x0041EF8F`

### Static image references
- `0x00346CC4` → RVA `0x00E0A740` (`.data`; read)
- `0x00346E03` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00346ED4` → RVA `0x00010880` (`.rdata`; read)
- `0x0034702C` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00346CB0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00346CB5  55                              push rbp
00346CB6  56                              push rsi
00346CB7  57                              push rdi
00346CB8  41 54                           push r12
00346CBA  41 55                           push r13
00346CBC  41 56                           push r14
00346CBE  41 57                           push r15
00346CC0  48 83 EC 60                     sub rsp, 0x60
00346CC4  48 8B 05 75 3A AC 00            mov rax, qword ptr [rip + 0xac3a75]
00346CCB  48 33 C4                        xor rax, rsp
00346CCE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00346CD3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00346CD8  49 8B F8                        mov rdi, r8
00346CDB  48 8B CA                        mov rcx, rdx
00346CDE  49 8B E8                        mov rbp, r8
00346CE1  E8 0A FB FF FF                  call 0x1403467f0
00346CE6  48 8D 74 6D 00                  lea rsi, [rbp + rbp*2]
00346CEB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00346CF0  48 C1 E6 04                     shl rsi, 4
00346CF4  49 BE 00 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000000
00346CFE  49 8B CE                        mov rcx, r14
00346D01  48 03 F1                        add rsi, rcx
00346D04  4C 8D 7D 10                     lea r15, [rbp + 0x10]
00346D08  48 8B CD                        mov rcx, rbp
00346D0B  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00346D10  4C 8B EE                        mov r13, rsi
00346D13  E8 B8 1F FF FF                  call 0x140338cd0
00346D18  0F 57 C0                        xorps xmm0, xmm0
00346D1B  48 8D 5E 18                     lea rbx, [rsi + 0x18]
00346D1F  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00346D24  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
00346D2B  45 33 E4                        xor r12d, r12d
00346D2E  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00346D38  49 3B FF                        cmp rdi, r15
00346D3B  0F 83 81 00 00 00               jae 0x140346dc2
00346D41  48 3B FD                        cmp rdi, rbp
00346D44  74 65                           je 0x140346dab
00346D46  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
00346D4C  72 76                           jb 0x140346dc4
00346D4E  0F B6 43 0A                     movzx eax, byte ptr [rbx + 0xa]
00346D52  48 8B D7                        mov rdx, rdi
00346D55  24 07                           and al, 7
00346D57  3C 06                           cmp al, 6
00346D59  0F 85 F5 02 00 00               jne 0x140347054
00346D5F  8B 43 08                        mov eax, dword ptr [rbx + 8]
00346D62  66 83 F8 01                     cmp ax, 1
00346D66  75 5C                           jne 0x140346dc4
00346D68  8B 43 08                        mov eax, dword ptr [rbx + 8]
00346D6B  C1 E8 18                        shr eax, 0x18
00346D6E  A8 40                           test al, 0x40
00346D70  75 52                           jne 0x140346dc4
00346D72  8B 43 08                        mov eax, dword ptr [rbx + 8]
00346D75  C1 E8 10                        shr eax, 0x10
00346D78  24 07                           and al, 7
00346D7A  3C 05                           cmp al, 5
00346D7C  74 1E                           je 0x140346d9c
00346D7E  8B 43 08                        mov eax, dword ptr [rbx + 8]
00346D81  48 FF C7                        inc rdi
00346D84  C1 E8 10                        shr eax, 0x10
00346D87  48 83 C6 30                     add rsi, 0x30
00346D8B  0F B6 C8                        movzx ecx, al
00346D8E  48 C1 E9 06                     shr rcx, 6
00346D92  FF 44 8C 40                     inc dword ptr [rsp + rcx*4 + 0x40]
00346D96  48 83 C3 30                     add rbx, 0x30
00346D9A  EB 92                           jmp 0x140346d2e
00346D9C  48 8B 43 F0                     mov rax, qword ptr [rbx - 0x10]
00346DA0  48 0B C1                        or rax, rcx
00346DA3  48 83 F8 FC                     cmp rax, -4
00346DA7  75 D5                           jne 0x140346d7e
00346DA9  EB 19                           jmp 0x140346dc4
00346DAB  45 8B F4                        mov r14d, r12d
00346DAE  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
00346DB4  72 4A                           jb 0x140346e00
00346DB6  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00346DC0  EB 8C                           jmp 0x140346d4e
00346DC2  74 58                           je 0x140346e1c
00346DC4  48 83 FA FF                     cmp rdx, -1
00346DC8  0F 85 EF 02 00 00               jne 0x1403470bd
00346DCE  33 C0                           xor eax, eax
00346DD0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00346DD5  48 33 CC                        xor rcx, rsp
00346DD8  E8 63 58 36 00                  call 0x1406ac640
00346DDD  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
00346DE5  48 83 C4 60                     add rsp, 0x60
00346DE9  41 5F                           pop r15
00346DEB  41 5E                           pop r14
00346DED  41 5D                           pop r13
00346DEF  41 5C                           pop r12
00346DF1  5F                              pop rdi
00346DF2  5E                              pop rsi
00346DF3  5D                              pop rbp
00346DF4  C3                              ret
00346DF5  CC                              int3
00346DF6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00346E00  41 FF C6                        inc r14d
00346E03  44 85 35 A2 E4 C7 00            test dword ptr [rip + 0xc7e4a2], r14d
00346E0A  0F 84 1C 02 00 00               je 0x14034702c
00346E10  F3 90                           pause
00346E12  48 8B 03                        mov rax, qword ptr [rbx]
00346E15  48 85 C0                        test rax, rax
00346E18  79 94                           jns 0x140346dae
00346E1A  EB E4                           jmp 0x140346e00
00346E1C  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00346E20  48 8B EE                        mov rbp, rsi
00346E23  48 81 EE 00 03 00 00            sub rsi, 0x300
00346E2A  41 8B C4                        mov eax, r12d
00346E2D  BB 01 00 00 00                  mov ebx, 1
00346E32  85 C9                           test ecx, ecx
00346E34  74 05                           je 0x140346e3b
00346E36  8B C1                           mov eax, ecx
00346E38  41 8B DC                        mov ebx, r12d
00346E3B  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00346E3F  3B C1                           cmp eax, ecx
00346E41  73 07                           jae 0x140346e4a
00346E43  8B C1                           mov eax, ecx
00346E45  BB 01 00 00 00                  mov ebx, 1
00346E4A  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00346E4E  BA 02 00 00 00                  mov edx, 2
00346E53  3B C1                           cmp eax, ecx
00346E55  73 04                           jae 0x140346e5b
00346E57  8B C1                           mov eax, ecx
00346E59  8B DA                           mov ebx, edx
00346E5B  3B 44 24 4C                     cmp eax, dword ptr [rsp + 0x4c]
00346E5F  B9 03 00 00 00                  mov ecx, 3
00346E64  4C 8B 74 24 20                  mov r14, qword ptr [rsp + 0x20]
00346E69  48 BF FF FF FF FF FF FF FF 7F   movabs rdi, 0x7fffffffffffffff
00346E73  0F 42 D9                        cmovb ebx, ecx
00346E76  44 8B FA                        mov r15d, edx
00346E79  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00346E80  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00346E83  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00346E87  66 44 89 7C 24 20               mov word ptr [rsp + 0x20], r15w
00346E8D  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00346E91  89 46 20                        mov dword ptr [rsi + 0x20], eax
00346E94  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00346E98  48 C1 E8 3C                     shr rax, 0x3c
00346E9C  24 07                           and al, 7
00346E9E  3C 03                           cmp al, 3
00346EA0  0F 84 05 02 00 00               je 0x1403470ab
00346EA6  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00346EAA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00346EAF  48 0F BA E0 0A                  bt rax, 0xa
00346EB4  72 1E                           jb 0x140346ed4
00346EB6  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
00346EBB  C0 E8 02                        shr al, 2
00346EBE  A8 01                           test al, 1
00346EC0  75 09                           jne 0x140346ecb
00346EC2  0F B6 C2                        movzx eax, dl
00346EC5  D0 E8                           shr al, 1
00346EC7  A8 01                           test al, 1
00346EC9  74 09                           je 0x140346ed4
00346ECB  48 85 D2                        test rdx, rdx
00346ECE  0F 85 45 01 00 00               jne 0x140347019
00346ED4  48 8B 05 A5 99 CC FF            mov rax, qword ptr [rip - 0x33665b]
00346EDB  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00346EDF  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00346EE2  C1 E8 10                        shr eax, 0x10
00346EE5  0F B6 C8                        movzx ecx, al
00346EE8  C1 E9 06                        shr ecx, 6
00346EEB  3B CB                           cmp ecx, ebx
00346EED  0F 85 87 01 00 00               jne 0x14034707a
00346EF3  F6 46 23 10                     test byte ptr [rsi + 0x23], 0x10
00346EF7  0F 85 92 01 00 00               jne 0x14034708f
00346EFD  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
00346F00  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00346F04  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00346F08  48 23 C7                        and rax, rdi
00346F0B  80 64 24 23 D7                  and byte ptr [rsp + 0x23], 0xd7
00346F10  C1 E9 10                        shr ecx, 0x10
00346F13  80 E1 C7                        and cl, 0xc7
00346F16  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
00346F1A  88 4C 24 22                     mov byte ptr [rsp + 0x22], cl
00346F1E  41 8B CC                        mov ecx, r12d
00346F21  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00346F25  89 46 20                        mov dword ptr [rsi + 0x20], eax
00346F28  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00346F2C  48 0F BA E0 28                  bt rax, 0x28
00346F31  73 09                           jae 0x140346f3c
00346F33  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
00346F36  81 E1 00 00 00 18               and ecx, 0x18000000
00346F3C  89 4E 24                        mov dword ptr [rsi + 0x24], ecx
00346F3F  45 33 C9                        xor r9d, r9d
00346F42  48 8B CE                        mov rcx, rsi
00346F45  45 8B C7                        mov r8d, r15d
00346F48  49 8B D5                        mov rdx, r13
00346F4B  E8 C0 01 00 00                  call 0x140347110
00346F50  49 3B F5                        cmp rsi, r13
00346F53  74 05                           je 0x140346f5a
00346F55  F0 48 21 7E 18                  lock and qword ptr [rsi + 0x18], rdi
00346F5A  48 83 C6 30                     add rsi, 0x30
00346F5E  48 3B F5                        cmp rsi, rbp
00346F61  0F 82 19 FF FF FF               jb 0x140346e80
00346F67  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00346F6B  48 BE 00 00 00 00 00 00 00 C0   movabs rsi, 0xc000000000000000
00346F75  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00346F7A  48 23 C6                        and rax, rsi
00346F7D  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
00346F81  48 83 C1 F0                     add rcx, -0x10
00346F85  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00346F89  41 8B D7                        mov edx, r15d
00346F8C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00346F90  66 44 89 64 24 20               mov word ptr [rsp + 0x20], r12w
00346F96  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00346F9A  41 89 45 20                     mov dword ptr [r13 + 0x20], eax
00346F9E  E8 7D DD FE FF                  call 0x140334d20
00346FA3  F0 49 21 7D 18                  lock and qword ptr [r13 + 0x18], rdi
00346FA8  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00346FAD  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00346FB7  4B 8D 1C 76                     lea rbx, [r14 + r14*2]
00346FBB  48 C1 E3 04                     shl rbx, 4
00346FBF  48 8B C0                        mov rax, rax
00346FC2  48 03 D8                        add rbx, rax
00346FC5  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00346FCC  72 32                           jb 0x140347000
00346FCE  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00346FD2  48 8D 51 F0                     lea rdx, [rcx - 0x10]
00346FD6  4C 8B C2                        mov r8, rdx
00346FD9  4C 33 C1                        xor r8, rcx
00346FDC  4C 23 C6                        and r8, rsi
00346FDF  4C 33 C2                        xor r8, rdx
00346FE2  4C 89 43 18                     mov qword ptr [rbx + 0x18], r8
00346FE6  F0 48 21 7B 18                  lock and qword ptr [rbx + 0x18], rdi
00346FEB  B8 01 00 00 00                  mov eax, 1
00346FF0  E9 DB FD FF FF                  jmp 0x140346dd0
00346FF5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00347000  41 FF C4                        inc r12d
00347003  44 85 25 A2 E2 C7 00            test dword ptr [rip + 0xc7e2a2], r12d
0034700A  74 51                           je 0x14034705d
0034700C  F3 90                           pause
0034700E  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00347012  48 85 C0                        test rax, rax
00347015  79 AE                           jns 0x140346fc5
00347017  EB E7                           jmp 0x140347000
00347019  41 B8 01 00 00 00               mov r8d, 1
0034701F  49 8B CE                        mov rcx, r14
00347022  E8 A9 CF F3 FF                  call 0x140283fd0
00347027  E9 A8 FE FF FF                  jmp 0x140346ed4
0034702C  8B 05 86 FA C7 00               mov eax, dword ptr [rip + 0xc7fa86]
00347032  A8 40                           test al, 0x40
00347034  0F 84 D6 FD FF FF               je 0x140346e10
0034703A  E8 51 84 FC FF                  call 0x14030f490
0034703F  84 C0                           test al, al
00347041  0F 84 C9 FD FF FF               je 0x140346e10
00347047  41 8B CE                        mov ecx, r14d
0034704A  E8 11 84 FC FF                  call 0x14030f460
0034704F  E9 BE FD FF FF                  jmp 0x140346e12
00347054  48 8B CE                        mov rcx, rsi
00347057  E8 9C 9E 02 00                  call 0x140370ef8
0034705C  CC                              int3
0034705D  8B 05 55 FA C7 00               mov eax, dword ptr [rip + 0xc7fa55]
00347063  A8 40                           test al, 0x40
00347065  74 A5                           je 0x14034700c
00347067  E8 24 84 FC FF                  call 0x14030f490
0034706C  84 C0                           test al, al
0034706E  74 9C                           je 0x14034700c
00347070  41 8B CC                        mov ecx, r12d
00347073  E8 E8 83 FC FF                  call 0x14030f460
00347078  EB 94                           jmp 0x14034700e
0034707A  41 B8 01 00 00 00               mov r8d, 1
00347080  8B D3                           mov edx, ebx
00347082  48 8B CE                        mov rcx, rsi
00347085  E8 42 BE FE FF                  call 0x140332ecc
0034708A  E9 64 FE FF FF                  jmp 0x140346ef3
0034708F  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00347092  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00347096  C1 E8 18                        shr eax, 0x18
00347099  24 EF                           and al, 0xef
0034709B  88 44 24 23                     mov byte ptr [rsp + 0x23], al
0034709F  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
003470A3  89 46 20                        mov dword ptr [rsi + 0x20], eax
003470A6  E9 52 FE FF FF                  jmp 0x140346efd
003470AB  BA 0C 00 00 00                  mov edx, 0xc
003470B0  48 8B CE                        mov rcx, rsi
003470B3  E8 48 FF 0B 00                  call 0x140407000
003470B8  E9 E9 FD FF FF                  jmp 0x140346ea6
003470BD  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
003470C1  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003470CB  48 C1 E1 04                     shl rcx, 4
003470CF  48 8B C0                        mov rax, rax
003470D2  48 03 C8                        add rcx, rax
003470D5  48 BF FF FF FF FF FF FF FF 7F   movabs rdi, 0x7fffffffffffffff
003470DF  49 3B CD                        cmp rcx, r13
003470E2  74 0E                           je 0x1403470f2
003470E4  F0 48 21 79 18                  lock and qword ptr [rcx + 0x18], rdi
003470E9  48 83 E9 30                     sub rcx, 0x30
003470ED  49 3B CD                        cmp rcx, r13
003470F0  75 F2                           jne 0x1403470e4
003470F2  F0 48 21 79 18                  lock and qword ptr [rcx + 0x18], rdi
003470F7  E9 D2 FC FF FF                  jmp 0x140346dce
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteClusterPage(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p22;
    unsigned __int8 v_stack_p23;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 11287157)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m78 = a1;
    result = MiGetContainingPageTable(a2, a2, a3, a4);
    v_stack_m60 = result;
    v_rsi = (a3 + a3 * 2) << (4);
    v_rsi = (v_rsi) + (v_r14);
    v_stack_m68 = a3 + 16;
    result = MiPageToNode(a3, a2, a3, a4);
    v_stack_m58 = v_xmm0;
    v_r12 = 0;
loc_00346D2E:
    if (a3 >= (a3 + 16)) goto loc_00346DC2;
    if (a3 == a3) goto loc_00346DAB;
    if (a3 < a3) goto loc_00346DC4;
loc_00346D4E:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rsi + 24 + 10)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_00347054;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 24 + 8)))) != 1) goto loc_00346DC4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 24 + 8))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_00346DC4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 24 + 8))) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 5) goto loc_00346D9C;
loc_00346D7E:
    v_rdi = (a3) + 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 24 + 8))) >> (16));
    v_rsi = (v_rsi) + (48);
    a1 = ((unsigned __int8)(result)) >> (6);
    v_rbx = (v_rsi + 24) + (48);
    goto loc_00346D2E;
loc_00346D9C:
    result = (*(unsigned __int64 *)(v_rbx - 16)) | (a1);
    if (result != -4) goto loc_00346D7E;
    goto loc_00346DC4;
loc_00346DAB:
loc_00346DAE:
    if (result < -4) goto loc_00346E00;
    goto loc_00346D4E;
loc_00346DC2:
    if (result == -4) goto loc_00346E1C;
loc_00346DC4:
    if (a3 != -1) goto loc_003470BD;
loc_00346DCE:
    result = 0;
loc_00346DD0:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a3, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
loc_00346E00:
    v_r14 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13100194)) & ((unsigned int)(v_r14))) == 0) goto loc_0034702C;
loc_00346E10:
loc_00346E12:
    if (!sign_flag) goto loc_00346DAE;
    goto loc_00346E00;
loc_00346E1C:
    v_rsi = (v_rsi) - (768);
    result = 0;
    v_rbx = 1;
    if ((unsigned int)((unsigned int)(v_stack_p40)) != 0) {
        result = (unsigned int)((unsigned int)(v_stack_p40));
        v_rbx = 0;
    }
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(v_stack_p44)))) {
        result = (unsigned int)((unsigned int)(v_stack_p44));
        v_rbx = 1;
    }
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(v_stack_p48)))) {
        result = (unsigned int)((unsigned int)(v_stack_p48));
        v_rbx = 2;
    }
    if (((unsigned int)(result)) < v_stack_p4C) { v_rbx = 3; }
loc_00346E80:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 32)));
    v_stack_p20 = 2;
    *(unsigned int *)(v_rsi + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 3) goto loc_003470AB;
loc_00346EA6:
    v_stack_p28 = *(unsigned __int64 *)(v_rsi + 16);
    if (((unsigned __int8)(result)) < 3) goto loc_00346ED4;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rsi + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00346ECB;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p28)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00346ED4;
loc_00346ECB:
    if (v_stack_p28 != 0) goto loc_00347019;
loc_00346ED4:
    *(unsigned __int64 *)(v_rsi + 16) = *(unsigned __int64 *)(v_rip - 3368539);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)(v_rbx))) goto loc_0034707A;
loc_00346EF3:
    if (((*(unsigned __int8 *)(v_rsi + 35)) & (16)) != 0) goto loc_0034708F;
loc_00346EFD:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 32)));
    result = (*(unsigned __int64 *)(v_rsi + 40)) & (v_rdi);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (16));
    a1 = (unsigned __int8)((a1) & (199));
    *(unsigned __int64 *)(v_rsi + 40) = result;
    v_stack_p22 = (unsigned __int8)(a1);
    *(unsigned int *)(v_rsi + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    if (!(condition_is_above_or_equal)) {
        a1 = *(unsigned int *)(v_rsi + 36);
        a1 = (unsigned int)((a1) & (0x18000000ULL));
    }
    *(unsigned int *)(v_rsi + 36) = (unsigned int)(a1);
    a4 = 0;
    result = MiConvertLockedSmallPageToLarge(v_rsi, v_rsi, 2, a4);
    if (v_rsi != v_rsi) {
    }
    v_rsi = (v_rsi) + (48);
    if (v_rsi < v_rsi) goto loc_00346E80;
    result = (*(unsigned __int64 *)(v_rsi + 24)) & (v_rsi);
    *(unsigned __int64 *)(v_rsi + 24) = result;
    a1 = (v_stack_p30) + (-16);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 32)));
    v_stack_p20 = 0;
    *(unsigned int *)(v_rsi + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    result = MiInsertPageInFreeOrZeroedList(a1, 2, 2, a4);
    v_rbx = (v_stack_p38 + v_stack_p38 * 2) << (4);
    v_rbx = (v_rbx) + (result);
loc_00346FC5:
    if (condition_is_below) goto loc_00347000;
    a3 = (*(unsigned __int64 *)(v_rbx + 24) - 16) ^ (*(unsigned __int64 *)(v_rbx + 24));
    a3 = (a3) & (v_rsi);
    a3 = (a3) ^ (*(unsigned __int64 *)(v_rbx + 24) - 16);
    *(unsigned __int64 *)(v_rbx + 24) = a3;
    goto loc_00346DD0;
loc_00347000:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13099682)) & ((unsigned int)(v_r12))) == 0) goto loc_0034705D;
loc_0034700C:
loc_0034700E:
    if (!sign_flag) goto loc_00346FC5;
    goto loc_00347000;
loc_00347019:
    result = MiReleasePageFileInfo(v_stack_p38, *(unsigned __int64 *)(v_rbx + 24) - 16, 1, a4);
    goto loc_00346ED4;
loc_0034702C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13105798)))) & (64)) == 0) goto loc_00346E10;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p38, *(unsigned __int64 *)(v_rbx + 24) - 16, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00346E10;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p38)), *(unsigned __int64 *)(v_rbx + 24) - 16, 1, a4);
    goto loc_00346E12;
loc_00347054:
    result = MiBadShareCount(v_rsi, *(unsigned __int64 *)(v_rbx + 24) - 16, 1, a4);
loc_0034705D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13105749)))) & (64)) == 0) goto loc_0034700C;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rsi, *(unsigned __int64 *)(v_rbx + 24) - 16, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0034700C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rbx + 24) - 16, 1, a4);
    goto loc_0034700E;
loc_0034707A:
    result = MiChangePageAttribute(v_rsi, (unsigned int)((unsigned int)(v_rbx)), 1, a4);
    goto loc_00346EF3;
loc_0034708F:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    result = (unsigned __int8)((result) & (239));
    v_stack_p23 = (unsigned __int8)(result);
    *(unsigned int *)(v_rsi + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    goto loc_00346EFD;
loc_003470AB:
    result = MiClearPfnImageVerified(v_rsi, 12, 1, a4);
    goto loc_00346EA6;
loc_003470BD:
    a1 = (12 + 12 * 2) << (4);
    a1 = (a1) + (result);
    if (a1 == v_rsi) goto loc_003470F2;
loc_003470E4:
    a1 = (a1) - (48);
    if (a1 != v_rsi) goto loc_003470E4;
loc_003470F2:
    goto loc_00346DCE;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteClusterPage(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p20;
    uint8_t v_stack_p22;
    uint8_t v_stack_p23;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0xAC3A75)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m78 = Arg1;
    result = MiGetContainingPageTable(Arg2, Arg2, Arg3, Arg4);
    v_stack_m60 = result;
    local_rsi = (Arg3 + Arg3 * 2) << (4);
    local_rsi = (local_rsi) + (local_r14);
    v_stack_m68 = Arg3 + 16;
    result = MiPageToNode(Arg3, Arg2, Arg3, Arg4);
    v_stack_m58 = v_xmm0;
    local_r12 = 0;
loc_00346D2E:
    if (Arg3 >= (Arg3 + 16)) goto loc_00346DC2;
    if (Arg3 == Arg3) goto loc_00346DAB;
    if (Arg3 < Arg3) goto loc_00346DC4;
loc_00346D4E:
    result = (uint8_t)((*(uint8_t *)(local_rsi + 0x18 + 0xA)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_00347054;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18 + 0x8)))) != 1) goto loc_00346DC4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x18 + 0x8))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_00346DC4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x18 + 0x8))) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 5) goto loc_00346D9C;
loc_00346D7E:
    local_rdi = (Arg3) + 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x18 + 0x8))) >> (16));
    local_rsi = (local_rsi) + (48);
    Arg1 = ((uint8_t)(result)) >> (6);
    local_rbx = (local_rsi + 24) + (48);
    goto loc_00346D2E;
loc_00346D9C:
    result = (*(uint64_t *)(local_rbx - 0x10)) | (Arg1);
    if (result != -4) goto loc_00346D7E;
    goto loc_00346DC4;
loc_00346DAB:
loc_00346DAE:
    if (result < -4) goto loc_00346E00;
    goto loc_00346D4E;
loc_00346DC2:
    if (result == -4) goto loc_00346E1C;
loc_00346DC4:
    if (Arg3 != -1) goto loc_003470BD;
loc_00346DCE:
    result = 0;
loc_00346DD0:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg3, Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
loc_00346E00:
    local_r14 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC7E4A2)) & ((uint32_t)(local_r14))) == 0) goto loc_0034702C;
loc_00346E10:
loc_00346E12:
    if (!sign_flag) goto loc_00346DAE;
    goto loc_00346E00;
loc_00346E1C:
    local_rsi = (local_rsi) - (768);
    result = 0;
    local_rbx = 1;
    if ((uint32_t)((uint32_t)(v_stack_p40)) != 0) {
        result = (uint32_t)((uint32_t)(v_stack_p40));
        local_rbx = 0;
    }
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(v_stack_p44)))) {
        result = (uint32_t)((uint32_t)(v_stack_p44));
        local_rbx = 1;
    }
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(v_stack_p48)))) {
        result = (uint32_t)((uint32_t)(v_stack_p48));
        local_rbx = 2;
    }
    if (((uint32_t)(result)) < v_stack_p4C) { local_rbx = 3; }
loc_00346E80:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)));
    v_stack_p20 = 2;
    *(uint32_t *)(local_rsi + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 3) goto loc_003470AB;
loc_00346EA6:
    v_stack_p28 = *(uint64_t *)(local_rsi + 0x10);
    if (((uint8_t)(result)) < 3) goto loc_00346ED4;
    result = (uint8_t)((*(uint64_t *)(local_rsi + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00346ECB;
    result = (uint8_t)(((uint8_t)(v_stack_p28)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00346ED4;
loc_00346ECB:
    if (v_stack_p28 != 0) goto loc_00347019;
loc_00346ED4:
    *(uint64_t *)(local_rsi + 0x10) = *(uint64_t *)(v_rip - 0x33665B);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_rbx))) goto loc_0034707A;
loc_00346EF3:
    if (((*(uint8_t *)(local_rsi + 0x23)) & (16)) != 0) goto loc_0034708F;
loc_00346EFD:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)));
    result = (*(uint64_t *)(local_rsi + 0x28)) & (local_rdi);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (16));
    Arg1 = (uint8_t)((Arg1) & (199));
    *(uint64_t *)(local_rsi + 0x28) = result;
    v_stack_p22 = (uint8_t)(Arg1);
    *(uint32_t *)(local_rsi + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    if (!(condition_is_above_or_equal)) {
        Arg1 = *(uint32_t *)(local_rsi + 0x24);
        Arg1 = (uint32_t)((Arg1) & (0x18000000ULL));
    }
    *(uint32_t *)(local_rsi + 0x24) = (uint32_t)(Arg1);
    Arg4 = 0;
    result = MiConvertLockedSmallPageToLarge(local_rsi, local_rsi, 2, Arg4);
    if (local_rsi != local_rsi) {
    }
    local_rsi = (local_rsi) + (48);
    if (local_rsi < local_rsi) goto loc_00346E80;
    result = (*(uint64_t *)(local_rsi + 0x18)) & (local_rsi);
    *(uint64_t *)(local_rsi + 0x18) = result;
    Arg1 = (v_stack_p30) + (-16);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)));
    v_stack_p20 = 0;
    *(uint32_t *)(local_rsi + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    result = MiInsertPageInFreeOrZeroedList(Arg1, 2, 2, Arg4);
    local_rbx = (v_stack_p38 + v_stack_p38 * 2) << (4);
    local_rbx = (local_rbx) + (result);
loc_00346FC5:
    if (condition_is_below) goto loc_00347000;
    Arg3 = (*(uint64_t *)(local_rbx + 0x18) - 16) ^ (*(uint64_t *)(local_rbx + 0x18));
    Arg3 = (Arg3) & (local_rsi);
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_rbx + 0x18) - 16);
    *(void **)(local_rbx + 0x18) = Arg3;
    goto loc_00346DD0;
loc_00347000:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xC7E2A2)) & ((uint32_t)(local_r12))) == 0) goto loc_0034705D;
loc_0034700C:
loc_0034700E:
    if (!sign_flag) goto loc_00346FC5;
    goto loc_00347000;
loc_00347019:
    result = MiReleasePageFileInfo(v_stack_p38, *(uint64_t *)(local_rbx + 0x18) - 16, 1, Arg4);
    goto loc_00346ED4;
loc_0034702C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7FA86)))) & (64)) == 0) goto loc_00346E10;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p38, *(uint64_t *)(local_rbx + 0x18) - 16, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00346E10;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p38)), *(uint64_t *)(local_rbx + 0x18) - 16, 1, Arg4);
    goto loc_00346E12;
loc_00347054:
    result = MiBadShareCount(local_rsi, *(uint64_t *)(local_rbx + 0x18) - 16, 1, Arg4);
loc_0034705D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7FA55)))) & (64)) == 0) goto loc_0034700C;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rsi, *(uint64_t *)(local_rbx + 0x18) - 16, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0034700C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(local_rbx + 0x18) - 16, 1, Arg4);
    goto loc_0034700E;
loc_0034707A:
    result = MiChangePageAttribute(local_rsi, (uint32_t)((uint32_t)(local_rbx)), 1, Arg4);
    goto loc_00346EF3;
loc_0034708F:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    result = (uint8_t)((result) & (239));
    v_stack_p23 = (uint8_t)(result);
    *(uint32_t *)(local_rsi + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    goto loc_00346EFD;
loc_003470AB:
    result = MiClearPfnImageVerified(local_rsi, 12, 1, Arg4);
    goto loc_00346EA6;
loc_003470BD:
    Arg1 = (12 + 12 * 2) << (4);
    Arg1 = (Arg1) + (result);
    if (Arg1 == local_rsi) goto loc_003470F2;
loc_003470E4:
    Arg1 = (Arg1) - (48);
    if (Arg1 != local_rsi) goto loc_003470E4;
loc_003470F2:
    goto loc_00346DCE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + rbp*2` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00346CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
