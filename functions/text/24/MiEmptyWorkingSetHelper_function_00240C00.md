# MiEmptyWorkingSetHelper

- RVA: `0x00240C00`–`0x00241162` (길이 `1,378` bytes)
- VA: `0x0000000140240C00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000617B0`
- 디코드: `333`개 명령, `1,378/1,378` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00240D32` → [MiGetVaAge](MiGetVaAge_function_00240AC0.md) (function, `0x00240AC0`)
- `0x00240D42` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00240D74` → [MiLogPageAccess](MiLogPageAccess_function_00240870.md) (function, `0x00240870`)
- `0x00240E0A` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00240F33` → [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) (function, `0x0022ABAC`)
- `0x00240F9A` → [MiFreeWsleList](MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x00240FF1` → [MiIsPageTableLocked](../22/MiIsPageTableLocked_function_0022A5B0.md) (function, `0x0022A5B0`)
- `0x002410A8` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x002410B0` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x00241116` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)

### Direct callers
- [MiUpdateOldPteWorker](../49/MiUpdateOldPteWorker_function_0049CFD4.md) at `0x0049D038`

### Static image references
- `0x00240D09` → RVA `0x00E30088` (`.data`; read)
- `0x00240F48` → RVA `0x00E38D00` (`.data`; read)
- `0x0024104F` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0024109B` → RVA `0x00695890` (`MiTbFlushSort`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00240C00  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00240C05  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00240C0A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00240C0F  57                              push rdi
00240C10  41 54                           push r12
00240C12  41 55                           push r13
00240C14  41 56                           push r14
00240C16  41 57                           push r15
00240C18  48 83 EC 20                     sub rsp, 0x20
00240C1C  48 8B FA                        mov rdi, rdx
00240C1F  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
00240C29  48 C1 E7 19                     shl rdi, 0x19
00240C2D  45 8B F9                        mov r15d, r9d
00240C30  49 8B D8                        mov rbx, r8
00240C33  4C 8B F2                        mov r14, rdx
00240C36  48 8B E9                        mov rbp, rcx
00240C39  49 8B C4                        mov rax, r12
00240C3C  4C 8B 02                        mov r8, qword ptr [rdx]
00240C3F  48 C1 E0 19                     shl rax, 0x19
00240C43  48 2B F8                        sub rdi, rax
00240C46  48 C1 FF 10                     sar rdi, 0x10
00240C4A  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00240C54  48 3B D0                        cmp rdx, rax
00240C57  72 2E                           jb 0x140240c87
00240C59  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00240C63  48 3B D0                        cmp rdx, rax
00240C66  77 1F                           ja 0x140240c87
00240C68  49 8B D0                        mov rdx, r8
00240C6B  41 F6 C0 01                     test r8b, 1
00240C6F  74 16                           je 0x140240c87
00240C71  41 F6 C0 42                     test r8b, 0x42
00240C75  0F 95 C1                        setne cl
00240C78  41 F6 C0 20                     test r8b, 0x20
00240C7C  0F 95 C0                        setne al
00240C7F  84 C8                           test al, cl
00240C81  0F 84 83 01 00 00               je 0x140240e0a
00240C87  49 C1 E8 0C                     shr r8, 0xc
00240C8B  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00240C95  4C 23 C0                        and r8, rax
00240C98  49 BD 00 00 00 00 00 DE FF FF   movabs r13, 0xffffde0000000000
00240CA2  4B 8D 34 40                     lea rsi, [r8 + r8*2]
00240CA6  48 C1 E6 04                     shl rsi, 4
00240CAA  49 8B C5                        mov rax, r13
00240CAD  48 03 F0                        add rsi, rax
00240CB0  49 8B C4                        mov rax, r12
00240CB3  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
00240CBD  48 3B F8                        cmp rdi, rax
00240CC0  0F 83 3A 03 00 00               jae 0x140241000
00240CC6  33 C9                           xor ecx, ecx
00240CC8  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00240CCE  85 C9                           test ecx, ecx
00240CD0  0F 85 FE 02 00 00               jne 0x140240fd4
00240CD6  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00240CDA  48 0F BA E0 28                  bt rax, 0x28
00240CDF  0F 83 1D 02 00 00               jae 0x140240f02
00240CE5  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00240CE8  66 83 F8 01                     cmp ax, 1
00240CEC  0F 87 D0 02 00 00               ja 0x140240fc2
00240CF2  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00240CF8  24 0F                           and al, 0xf
00240CFA  3C 01                           cmp al, 1
00240CFC  0F 84 46 02 00 00               je 0x140240f48
00240D02  0F B7 8D AE 00 00 00            movzx ecx, word ptr [rbp + 0xae]
00240D09  48 8B 05 78 F3 BE 00            mov rax, qword ptr [rip + 0xbef378]
00240D10  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00240D14  8B 80 2C 44 00 00               mov eax, dword ptr [rax + 0x442c]
00240D1A  85 C0                           test eax, eax
00240D1C  74 5B                           je 0x140240d79
00240D1E  BE FF FF FF FF                  mov esi, 0xffffffff
00240D23  49 8B C4                        mov rax, r12
00240D26  48 3B F8                        cmp rdi, rax
00240D29  0F 83 25 02 00 00               jae 0x140240f54
00240D2F  48 8B D7                        mov rdx, rdi
00240D32  E8 89 FD FF FF                  call 0x140240ac0
00240D37  0F B6 F0                        movzx esi, al
00240D3A  83 FE 07                        cmp esi, 7
00240D3D  74 3A                           je 0x140240d79
00240D3F  49 8B CE                        mov rcx, r14
00240D42  E8 59 1B 04 00                  call 0x1402828a0
00240D47  A8 20                           test al, 0x20
00240D49  74 2E                           je 0x140240d79
00240D4B  8B 8D B8 00 00 00               mov ecx, dword ptr [rbp + 0xb8]
00240D51  F6 C1 0F                        test cl, 0xf
00240D54  0F 85 F5 02 00 00               jne 0x14024104f
00240D5A  33 C9                           xor ecx, ecx
00240D5C  48 39 8D 70 02 00 00            cmp qword ptr [rbp + 0x270], rcx
00240D63  0F 95 C1                        setne cl
00240D66  85 C9                           test ecx, ecx
00240D68  0F 85 77 03 00 00               jne 0x1402410e5
00240D6E  49 8B D6                        mov rdx, r14
00240D71  48 8B CD                        mov rcx, rbp
00240D74  E8 F7 FA FF FF                  call 0x140240870
00240D79  BE 01 00 00 00                  mov esi, 1
00240D7E  39 73 08                        cmp dword ptr [rbx + 8], esi
00240D81  0F 85 8F 02 00 00               jne 0x140241016
00240D87  45 33 D2                        xor r10d, r10d
00240D8A  44 8B 4B 1C                     mov r9d, dword ptr [rbx + 0x1c]
00240D8E  45 85 C9                        test r9d, r9d
00240D91  0F 84 00 01 00 00               je 0x140240e97
00240D97  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00240D9A  A8 02                           test al, 2
00240D9C  0F 85 B0 00 00 00               jne 0x140240e52
00240DA2  41 8D 41 FF                     lea eax, [r9 - 1]
00240DA6  4C 8D 1C C3                     lea r11, [rbx + rax*8]
00240DAA  48 8B 44 C3 28                  mov rax, qword ptr [rbx + rax*8 + 0x28]
00240DAF  48 A9 00 0C 00 00               test rax, 0xc00
00240DB5  0F 85 DC 00 00 00               jne 0x140240e97
00240DBB  4C 8B C0                        mov r8, rax
00240DBE  48 8B C8                        mov rcx, rax
00240DC1  41 81 E0 FF 03 00 00            and r8d, 0x3ff
00240DC8  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00240DCF  49 8D 50 01                     lea rdx, [r8 + 1]
00240DD3  48 C1 E2 0C                     shl rdx, 0xc
00240DD7  48 03 D1                        add rdx, rcx
00240DDA  48 3B D7                        cmp rdx, rdi
00240DDD  75 16                           jne 0x140240df5
00240DDF  49 8D 0C 30                     lea rcx, [r8 + rsi]
00240DE3  49 3B C8                        cmp rcx, r8
00240DE6  76 0D                           jbe 0x140240df5
00240DE8  48 81 F9 FF 03 00 00            cmp rcx, 0x3ff
00240DEF  0F 86 50 03 00 00               jbe 0x140241145
00240DF5  41 8D 49 FF                     lea ecx, [r9 - 1]
00240DF9  48 8D 49 05                     lea rcx, [rcx + 5]
00240DFD  48 8B 04 CB                     mov rax, qword ptr [rbx + rcx*8]
00240E01  4C 8D 1C CB                     lea r11, [rbx + rcx*8]
00240E05  48 8B C8                        mov rcx, rax
00240E08  EB 6F                           jmp 0x140240e79
00240E0A  E8 89 AB 0E 00                  call 0x14032b998
00240E0F  48 85 C0                        test rax, rax
00240E12  0F 84 6F FE FF FF               je 0x140240c87
00240E18  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00240E1F  48 85 C9                        test rcx, rcx
00240E22  0F 84 5F FE FF FF               je 0x140240c87
00240E28  49 8B C6                        mov rax, r14
00240E2B  48 C1 E8 03                     shr rax, 3
00240E2F  25 FF 01 00 00                  and eax, 0x1ff
00240E34  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00240E38  A8 20                           test al, 0x20
00240E3A  74 04                           je 0x140240e40
00240E3C  48 83 CA 20                     or rdx, 0x20
00240E40  4C 8B C2                        mov r8, rdx
00240E43  49 83 C8 42                     or r8, 0x42
00240E47  A8 42                           test al, 0x42
00240E49  4C 0F 44 C2                     cmove r8, rdx
00240E4D  E9 35 FE FF FF                  jmp 0x140240c87
00240E52  45 85 C9                        test r9d, r9d
00240E55  74 40                           je 0x140240e97
00240E57  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00240E5A  A8 02                           test al, 2
00240E5C  75 39                           jne 0x140240e97
00240E5E  41 8D 49 FF                     lea ecx, [r9 - 1]
00240E62  48 8D 49 05                     lea rcx, [rcx + 5]
00240E66  48 8B 04 CB                     mov rax, qword ptr [rbx + rcx*8]
00240E6A  4C 8D 1C CB                     lea r11, [rbx + rcx*8]
00240E6E  48 8B C8                        mov rcx, rax
00240E71  48 A9 00 0C 00 00               test rax, 0xc00
00240E77  75 1E                           jne 0x140240e97
00240E79  4C 8B F6                        mov r14, rsi
00240E7C  48 8B D1                        mov rdx, rcx
00240E7F  49 C1 E6 0C                     shl r14, 0xc
00240E83  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00240E8A  4E 8D 04 37                     lea r8, [rdi + r14]
00240E8E  49 3B D0                        cmp rdx, r8
00240E91  0F 84 29 02 00 00               je 0x1402410c0
00240E97  44 3B 4B 0C                     cmp r9d, dword ptr [rbx + 0xc]
00240E9B  0F 84 D1 01 00 00               je 0x140241072
00240EA1  48 85 F6                        test rsi, rsi
00240EA4  0F 84 DF 00 00 00               je 0x140240f89
00240EAA  48 8D 46 FF                     lea rax, [rsi - 1]
00240EAE  48 8B CF                        mov rcx, rdi
00240EB1  48 3D FF 03 00 00               cmp rax, 0x3ff
00240EB7  BA 00 04 00 00                  mov edx, 0x400
00240EBC  48 0F 46 D6                     cmovbe rdx, rsi
00240EC0  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00240EC7  48 8D 42 FF                     lea rax, [rdx - 1]
00240ECB  25 FF 03 00 00                  and eax, 0x3ff
00240ED0  48 0B C1                        or rax, rcx
00240ED3  48 8B CA                        mov rcx, rdx
00240ED6  4A 89 44 CB 28                  mov qword ptr [rbx + r9*8 + 0x28], rax
00240EDB  44 8B 4B 1C                     mov r9d, dword ptr [rbx + 0x1c]
00240EDF  48 01 53 20                     add qword ptr [rbx + 0x20], rdx
00240EE3  41 FF C1                        inc r9d
00240EE6  48 C1 E1 0C                     shl rcx, 0xc
00240EEA  48 03 F9                        add rdi, rcx
00240EED  44 89 4B 1C                     mov dword ptr [rbx + 0x1c], r9d
00240EF1  48 2B F2                        sub rsi, rdx
00240EF4  74 AB                           je 0x140240ea1
00240EF6  44 3B 4B 0C                     cmp r9d, dword ptr [rbx + 0xc]
00240EFA  0F 84 87 FE FF FF               je 0x140240d87
00240F00  EB 9F                           jmp 0x140240ea1
00240F02  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00240F06  48 85 C0                        test rax, rax
00240F09  0F 88 D6 FD FF FF               js 0x140240ce5
00240F0F  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00240F13  48 85 C0                        test rax, rax
00240F16  0F 84 C9 FD FF FF               je 0x140240ce5
00240F1C  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
00240F20  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00240F2A  4C 0B C0                        or r8, rax
00240F2D  49 8B D6                        mov rdx, r14
00240F30  48 8B CD                        mov rcx, rbp
00240F33  E8 74 9C FE FF                  call 0x14022abac
00240F38  85 C0                           test eax, eax
00240F3A  0F 84 A5 FD FF FF               je 0x140240ce5
00240F40  49 8B 06                        mov rax, qword ptr [r14]
00240F43  E9 9D FD FF FF                  jmp 0x140240ce5
00240F48  48 8D 05 B1 7D BF 00            lea rax, [rip + 0xbf7db1]
00240F4F  E9 C0 FD FF FF                  jmp 0x140240d14
00240F54  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00240F5E  48 8B C0                        mov rax, rax
00240F61  48 3B F8                        cmp rdi, rax
00240F64  0F 86 D5 FD FF FF               jbe 0x140240d3f
00240F6A  E9 C0 FD FF FF                  jmp 0x140240d2f
00240F6F  48 01 73 20                     add qword ptr [rbx + 0x20], rsi
00240F73  49 2B C6                        sub rax, r14
00240F76  48 8D 0C 30                     lea rcx, [rax + rsi]
00240F7A  48 33 C1                        xor rax, rcx
00240F7D  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00240F83  48 33 C1                        xor rax, rcx
00240F86  49 89 03                        mov qword ptr [r11], rax
00240F89  8B 4B 0C                        mov ecx, dword ptr [rbx + 0xc]
00240F8C  39 4B 1C                        cmp dword ptr [rbx + 0x1c], ecx
00240F8F  75 0E                           jne 0x140240f9f
00240F91  45 8B C7                        mov r8d, r15d
00240F94  48 8B D3                        mov rdx, rbx
00240F97  48 8B CD                        mov rcx, rbp
00240F9A  E8 C9 01 00 00                  call 0x140241168
00240F9F  B8 01 00 00 00                  mov eax, 1
00240FA4  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00240FA9  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00240FAE  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00240FB3  48 83 C4 20                     add rsp, 0x20
00240FB7  41 5F                           pop r15
00240FB9  41 5E                           pop r14
00240FBB  41 5D                           pop r13
00240FBD  41 5C                           pop r12
00240FBF  5F                              pop rdi
00240FC0  C3                              ret
00240FC1  CC                              int3
00240FC2  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00240FC8  A8 0F                           test al, 0xf
00240FCA  0F 84 22 FD FF FF               je 0x140240cf2
00240FD0  33 C0                           xor eax, eax
00240FD2  EB D0                           jmp 0x140240fa4
00240FD4  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00240FD8  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00240FE2  48 23 C1                        and rax, rcx
00240FE5  48 83 F8 01                     cmp rax, 1
00240FE9  75 E5                           jne 0x140240fd0
00240FEB  49 8B D6                        mov rdx, r14
00240FEE  48 8B CD                        mov rcx, rbp
00240FF1  E8 BA 95 FE FF                  call 0x14022a5b0
00240FF6  85 C0                           test eax, eax
00240FF8  0F 84 D8 FC FF FF               je 0x140240cd6
00240FFE  EB D0                           jmp 0x140240fd0
00241000  48 8B C1                        mov rax, rcx
00241003  48 3B F8                        cmp rdi, rax
00241006  0F 87 BA FC FF FF               ja 0x140240cc6
0024100C  B9 01 00 00 00                  mov ecx, 1
00241011  E9 B2 FC FF FF                  jmp 0x140240cc8
00241016  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00241019  F6 C1 04                        test cl, 4
0024101C  0F 85 65 FD FF FF               jne 0x140240d87
00241022  49 8B C4                        mov rax, r12
00241025  48 3B F8                        cmp rdi, rax
00241028  0F 82 59 FD FF FF               jb 0x140240d87
0024102E  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00241038  48 8B C0                        mov rax, rax
0024103B  48 3B F8                        cmp rdi, rax
0024103E  0F 87 43 FD FF FF               ja 0x140240d87
00241044  83 C9 04                        or ecx, 4
00241047  89 4B 10                        mov dword ptr [rbx + 0x10], ecx
0024104A  E9 38 FD FF FF                  jmp 0x140240d87
0024104F  48 0F BA 25 30 5A D8 00 24      bt qword ptr [rip + 0xd85a30], 0x24
00241058  0F 83 10 FD FF FF               jae 0x140240d6e
0024105E  8B 8D B8 00 00 00               mov ecx, dword ptr [rbp + 0xb8]
00241064  C1 E9 08                        shr ecx, 8
00241067  C1 E9 03                        shr ecx, 3
0024106A  83 E1 01                        and ecx, 1
0024106D  E9 F4 FC FF FF                  jmp 0x140240d66
00241072  45 85 D2                        test r10d, r10d
00241075  74 13                           je 0x14024108a
00241077  80 7B 19 00                     cmp byte ptr [rbx + 0x19], 0
0024107B  0F 85 08 FF FF FF               jne 0x140240f89
00241081  C6 43 19 01                     mov byte ptr [rbx + 0x19], 1
00241085  E9 FF FE FF FF                  jmp 0x140240f89
0024108A  80 7B 19 00                     cmp byte ptr [rbx + 0x19], 0
0024108E  0F 85 F5 FE FF FF               jne 0x140240f89
00241094  49 8B D1                        mov rdx, r9
00241097  48 8D 4B 28                     lea rcx, [rbx + 0x28]
0024109B  4C 8D 0D EE 47 45 00            lea r9, [rip + 0x4547ee]
002410A2  41 B8 08 00 00 00               mov r8d, 8
002410A8  E8 43 F9 2B 00                  call 0x1405009f0
002410AD  48 8B CB                        mov rcx, rbx
002410B0  E8 F3 82 06 00                  call 0x1402a93a8
002410B5  41 BA 01 00 00 00               mov r10d, 1
002410BB  E9 CA FC FF FF                  jmp 0x140240d8a
002410C0  81 E1 FF 03 00 00               and ecx, 0x3ff
002410C6  48 8D 14 0E                     lea rdx, [rsi + rcx]
002410CA  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
002410D1  0F 87 C0 FD FF FF               ja 0x140240e97
002410D7  48 3B D1                        cmp rdx, rcx
002410DA  0F 86 B7 FD FF FF               jbe 0x140240e97
002410E0  E9 8A FE FF FF                  jmp 0x140240f6f
002410E5  8B 8D B8 00 00 00               mov ecx, dword ptr [rbp + 0xb8]
002410EB  F6 C1 0F                        test cl, 0xf
002410EE  74 40                           je 0x140241130
002410F0  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002410FA  48 C1 E8 0C                     shr rax, 0xc
002410FE  48 23 C1                        and rax, rcx
00241101  48 8D 0C 40                     lea rcx, [rax + rax*2]
00241105  48 C1 E1 04                     shl rcx, 4
00241109  49 8B C5                        mov rax, r13
0024110C  45 33 C0                        xor r8d, r8d
0024110F  48 03 C8                        add rcx, rax
00241112  41 8D 50 02                     lea edx, [r8 + 2]
00241116  E8 05 43 04 00                  call 0x140285420
0024111B  A8 41                           test al, 0x41
0024111D  0F 84 4B FC FF FF               je 0x140240d6e
00241123  85 F6                           test esi, esi
00241125  0F 85 4E FC FF FF               jne 0x140240d79
0024112B  E9 3E FC FF FF                  jmp 0x140240d6e
00241130  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0024113A  48 3B F8                        cmp rdi, rax
0024113D  0F 87 2B FC FF FF               ja 0x140240d6e
00241143  EB DE                           jmp 0x140241123
00241145  48 01 73 20                     add qword ptr [rbx + 0x20], rsi
00241149  48 8D 0C 30                     lea rcx, [rax + rsi]
0024114D  48 33 C1                        xor rax, rcx
00241150  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00241156  48 33 C1                        xor rax, rcx
00241159  49 89 43 28                     mov qword ptr [r11 + 0x28], rax
0024115D  E9 27 FE FF FF                  jmp 0x140240f89
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiEmptyWorkingSetHelper(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = (a2) << (25);
    result = (v_r12) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    if (a2 < result) goto loc_00240C87;
    if (a2 > result) goto loc_00240C87;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_00240C87;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00240E0A;
loc_00240C87:
    a3 = (*(unsigned __int64 *)(a2)) >> (12);
    a3 = (a3) & (result);
    v_rsi = (a3 + a3 * 2) << (4);
    v_rsi = (v_rsi) + (v_r13);
    if (v_rdi >= v_r12) goto loc_00241000;
loc_00240CC6:
    a1 = 0;
loc_00240CC8:
    if (0 != 0) goto loc_00240FD4;
loc_00240CD6:
    if (condition_is_above_or_equal) goto loc_00240F02;
loc_00240CE5:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) > 1) goto loc_00240FC2;
loc_00240CF2:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_00240F48;
loc_00240D14:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12514168) + *(unsigned __int16 *)(a1 + 174) * 8) + 17452))) == 0) goto loc_00240D79;
    if (v_rdi >= v_r12) goto loc_00240F54;
loc_00240D2F:
    result = MiGetVaAge(*(unsigned __int16 *)(a1 + 174), v_rdi, a3, a4);
    if (((unsigned int)((unsigned __int8)(result))) == 7) goto loc_00240D79;
loc_00240D3F:
    result = MI_READ_PTE_LOCK_FREE(a2, v_rdi, a3, a4);
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_00240D79;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_0024104F;
    a1 = 0;
    a1 = ((*(unsigned __int64 *)(a1 + 624)) != 0) ? 1 : 0;
loc_00240D66:
    if ((unsigned int)(a1) != 0) goto loc_002410E5;
loc_00240D6E:
    result = MiLogPageAccess(a1, a2, a3, a4);
loc_00240D79:
    if ((*(unsigned int *)(a3 + 8)) != 1) goto loc_00241016;
loc_00240D87:
    v_r10 = 0;
loc_00240D8A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 28))) == 0) goto loc_00240E97;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 16)))) & (2)) != 0) goto loc_00240E52;
    if (((*(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 * 8 + 40)) & (0xC00ULL)) != 0) goto loc_00240E97;
    a3 = (unsigned int)((*(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 * 8 + 40)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 * 8 + 40)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_rdi) goto loc_00240DF5;
    if ((a3 + 1 * 1) <= a3) goto loc_00240DF5;
    if ((a3 + 1 * 1) <= 0x3FFULL) goto loc_00241145;
loc_00240DF5:
    goto loc_00240E79;
loc_00240E0A:
    result = MiPteHasShadow(*(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 + 5 * 8), a2, a3, (unsigned int)(*(unsigned int *)(a3 + 28)));
    if (result == 0) goto loc_00240C87;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00240C87;
    result = (a2) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    a3 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a3 = a2; }
    goto loc_00240C87;
loc_00240E52:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 28))) == 0) goto loc_00240E97;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 16)))) & (2)) != 0) goto loc_00240E97;
    if (((*(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 + 5 * 8)) & (0xC00ULL)) != 0) goto loc_00240E97;
loc_00240E79:
    v_r14 = (1) << (12);
    a2 = (*(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 + 5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (v_rdi + v_r14 * 1)) goto loc_002410C0;
loc_00240E97:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 28)))) == (*(unsigned int *)(a3 + 12))) goto loc_00241072;
loc_00240EA1:
    if (1 == 0) goto loc_00240F89;
    a2 = (unsigned int)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { a2 = 1; }
    a1 = (v_rdi) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) * 8 + 40) = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 28))) + 1);
    a1 = (a2) << (12);
    v_rdi = (v_rdi) + (a1);
    *(unsigned int *)(a3 + 28) = a4;
    v_rsi = (1) - (a2);
    if (condition_is_equal) goto loc_00240EA1;
    if (a4 == (*(unsigned int *)(a3 + 12))) goto loc_00240D87;
    goto loc_00240EA1;
loc_00240F02:
    if (sign_flag) goto loc_00240CE5;
    if (*(unsigned __int64 *)(v_rsi + 8) == 0) goto loc_00240CE5;
    a3 = (*(unsigned __int64 *)(v_rsi + 8)) | (*(unsigned __int64 *)(v_rsi + 8));
    result = MiDemoteCombinedPte(a1, v_r14, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00240CE5;
    goto loc_00240CE5;
loc_00240F48:
    goto loc_00240D14;
loc_00240F54:
    if (v_rdi <= (v_rip + 12549553)) goto loc_00240D3F;
    goto loc_00240D2F;
loc_00240F6F:
    result = (v_rip + 12549553) - (v_r14);
    result = (result) ^ (result + v_rsi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + v_rsi * 1);
    *(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 + 5 * 8) = result;
loc_00240F89:
    if ((*(unsigned int *)(a3 + 28)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) {
        a3 = (unsigned int)((unsigned int)(a4));
        a2 = a3;
        a1 = a1;
        result = MiFreeWsleList(a1, a2, a3, a4);
    }
loc_00240FA4:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_00240FC2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 184)))) & (15)) == 0) goto loc_00240CF2;
loc_00240FD0:
    result = 0;
    goto loc_00240FA4;
loc_00240FD4:
    result = (*(unsigned __int64 *)(v_stack_p18 + 24)) & (a1);
    if (result != 1) goto loc_00240FD0;
    result = MiIsPageTableLocked(v_stack_p10, v_r14, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00240CD6;
    goto loc_00240FD0;
loc_00241000:
    if (v_rdi > v_stack_p10) goto loc_00240CC6;
    goto loc_00240CC8;
loc_00241016:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) & (4)) != 0) goto loc_00240D87;
    if (v_rdi < v_r12) goto loc_00240D87;
    if (v_rdi > v_r12) goto loc_00240D87;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 16))) | (4));
    *(unsigned int *)(v_stack_p8 + 16) = (unsigned int)(a1);
    goto loc_00240D87;
loc_0024104F:
    if (condition_is_above_or_equal) goto loc_00240D6E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 184))) >> (8));
    a1 = (unsigned int)((a1) >> (3));
    a1 = (unsigned int)((a1) & (1));
    goto loc_00240D66;
loc_00241072:
    if (0 == 0) goto loc_0024108A;
    if ((*(unsigned __int8 *)(v_stack_p8 + 25)) != 0) goto loc_00240F89;
    *(unsigned __int8 *)(v_stack_p8 + 25) = 1;
    goto loc_00240F89;
loc_0024108A:
    if ((*(unsigned __int8 *)(v_stack_p8 + 25)) != 0) goto loc_00240F89;
    result = qsort(v_stack_p8 + 40, a4, 8, v_rip + 4540398);
    result = MiCompressTbFlushList(v_stack_p8, a4, 8, v_rip + 4540398);
    goto loc_00240D8A;
loc_002410C0:
    a1 = (unsigned int)((v_stack_p8) & (0x3FFULL));
    if ((v_stack_p18 + a1 * 1) > 0x3FFULL) goto loc_00240E97;
    if ((v_stack_p18 + a1 * 1) <= a1) goto loc_00240E97;
    goto loc_00240F6F;
loc_002410E5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 184)))) & (15)) == 0) goto loc_00241130;
    result = (result) >> (12);
    result = (result) & ((unsigned int)(*(unsigned int *)(v_stack_p10 + 184)));
    a1 = (result + result * 2) << (4);
    a3 = 0;
    a1 = (a1) + (v_r13);
    result = MiGetPagePrivilege(a1, a3 + 2, a3, v_rip + 4540398);
    if ((((unsigned __int8)(result)) & (65)) == 0) goto loc_00240D6E;
loc_00241123:
    if ((unsigned int)(v_stack_p18) != 0) goto loc_00240D79;
    goto loc_00240D6E;
loc_00241130:
    if (v_rdi > result) goto loc_00240D6E;
    goto loc_00241123;
loc_00241145:
    result = (result) ^ (result + v_stack_p18 * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + v_stack_p18 * 1);
    *(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 28)) - 1 + 5 * 8 + 40) = result;
    goto loc_00240F89;
}
```

## 5. (Beta) C Style

```c
int64_t MiEmptyWorkingSetHelper(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = (Arg2) << (25);
    result = (local_r12) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    if (Arg2 < result) goto loc_00240C87;
    if (Arg2 > result) goto loc_00240C87;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) == 0) goto loc_00240C87;
    Arg1 = ((((uint8_t)(*(uint64_t *)(arg2))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(arg2))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00240E0A;
loc_00240C87:
    Arg3 = (*(uint64_t *)(arg2)) >> (12);
    Arg3 = (Arg3) & (result);
    local_rsi = (Arg3 + Arg3 * 2) << (4);
    local_rsi = (local_rsi) + (local_r13);
    if (local_rdi >= local_r12) goto loc_00241000;
loc_00240CC6:
    Arg1 = 0;
loc_00240CC8:
    if (0 != 0) goto loc_00240FD4;
loc_00240CD6:
    if (condition_is_above_or_equal) goto loc_00240F02;
loc_00240CE5:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) > 1) goto loc_00240FC2;
loc_00240CF2:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) goto loc_00240F48;
loc_00240D14:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBEF378) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x442C))) == 0) goto loc_00240D79;
    if (local_rdi >= local_r12) goto loc_00240F54;
loc_00240D2F:
    result = MiGetVaAge(*(uint16_t *)(arg1 + 0xAE), local_rdi, Arg3, Arg4);
    if (((uint32_t)((uint8_t)(result))) == 7) goto loc_00240D79;
loc_00240D3F:
    result = MI_READ_PTE_LOCK_FREE(Arg2, local_rdi, Arg3, Arg4);
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_00240D79;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_0024104F;
    Arg1 = 0;
    Arg1 = ((*(uint64_t *)(arg1 + 0x270)) != 0) ? 1 : 0;
loc_00240D66:
    if ((uint32_t)(Arg1) != 0) goto loc_002410E5;
loc_00240D6E:
    result = MiLogPageAccess(Arg1, Arg2, Arg3, Arg4);
loc_00240D79:
    if ((*(uint32_t *)(arg3 + 0x8)) != 1) goto loc_00241016;
loc_00240D87:
    local_r10 = 0;
loc_00240D8A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x1C))) == 0) goto loc_00240E97;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10)))) & (2)) != 0) goto loc_00240E52;
    if (((*(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 * 8 + 0x28)) & (0xC00ULL)) != 0) goto loc_00240E97;
    Arg3 = (uint32_t)((*(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 * 8 + 0x28)) & (0x3FFULL));
    Arg1 = (*(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 * 8 + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg3 + 1) << (12);
    Arg2 = (Arg2) + (Arg1);
    if (Arg2 != local_rdi) goto loc_00240DF5;
    if ((Arg3 + 1 * 1) <= Arg3) goto loc_00240DF5;
    if ((Arg3 + 1 * 1) <= 0x3FFULL) goto loc_00241145;
loc_00240DF5:
    goto loc_00240E79;
loc_00240E0A:
    result = MiPteHasShadow(*(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 + 0x5 * 8), Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg3 + 0x1C)));
    if (result == 0) goto loc_00240C87;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00240C87;
    result = (Arg2) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    Arg3 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { Arg3 = Arg2; }
    goto loc_00240C87;
loc_00240E52:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x1C))) == 0) goto loc_00240E97;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10)))) & (2)) != 0) goto loc_00240E97;
    if (((*(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 + 0x5 * 8)) & (0xC00ULL)) != 0) goto loc_00240E97;
loc_00240E79:
    local_r14 = (1) << (12);
    Arg2 = (*(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 + 0x5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg2 == (local_rdi + local_r14 * 1)) goto loc_002410C0;
loc_00240E97:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x1C)))) == (*(uint32_t *)(arg3 + 0xC))) goto loc_00241072;
loc_00240EA1:
    if (1 == 0) goto loc_00240F89;
    Arg2 = (uint32_t)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { Arg2 = 1; }
    Arg1 = (local_rdi) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((Arg2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    *(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) * 8 + 0x28) = result;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x1C))) + 1);
    Arg1 = (Arg2) << (12);
    local_rdi = (local_rdi) + (Arg1);
    *(uint32_t *)(arg3 + 0x1C) = Arg4;
    local_rsi = (1) - (Arg2);
    if (condition_is_equal) goto loc_00240EA1;
    if (Arg4 == (*(uint32_t *)(arg3 + 0xC))) goto loc_00240D87;
    goto loc_00240EA1;
loc_00240F02:
    if (sign_flag) goto loc_00240CE5;
    if (*(uint64_t *)(local_rsi + 0x8) == 0) goto loc_00240CE5;
    Arg3 = (*(uint64_t *)(local_rsi + 0x8)) | (*(uint64_t *)(local_rsi + 0x8));
    result = MiDemoteCombinedPte(Arg1, local_r14, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00240CE5;
    goto loc_00240CE5;
loc_00240F48:
    goto loc_00240D14;
loc_00240F54:
    if (local_rdi <= (v_rip + 12549553)) goto loc_00240D3F;
    goto loc_00240D2F;
loc_00240F6F:
    result = (v_rip + 12549553) - (local_r14);
    result = (result) ^ (result + local_rsi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + local_rsi * 1);
    *(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 + 0x5 * 8) = result;
loc_00240F89:
    if ((*(uint32_t *)(arg3 + 0x1C)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) {
        Arg3 = (uint32_t)((uint32_t)(Arg4));
        Arg2 = Arg3;
        Arg1 = Arg1;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, Arg4);
    }
loc_00240FA4:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_00240FC2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xB8)))) & (15)) == 0) goto loc_00240CF2;
loc_00240FD0:
    result = 0;
    goto loc_00240FA4;
loc_00240FD4:
    result = (*(uint64_t *)(v_stack_p18 + 0x18)) & (Arg1);
    if (result != 1) goto loc_00240FD0;
    result = MiIsPageTableLocked(v_stack_p10, local_r14, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00240CD6;
    goto loc_00240FD0;
loc_00241000:
    if (local_rdi > v_stack_p10) goto loc_00240CC6;
    goto loc_00240CC8;
loc_00241016:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) & (4)) != 0) goto loc_00240D87;
    if (local_rdi < local_r12) goto loc_00240D87;
    if (local_rdi > local_r12) goto loc_00240D87;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10))) | (4));
    *(uint32_t *)(v_stack_p8 + 0x10) = (uint32_t)(Arg1);
    goto loc_00240D87;
loc_0024104F:
    if (condition_is_above_or_equal) goto loc_00240D6E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xB8))) >> (8));
    Arg1 = (uint32_t)((Arg1) >> (3));
    Arg1 = (uint32_t)((Arg1) & (1));
    goto loc_00240D66;
loc_00241072:
    if (0 == 0) goto loc_0024108A;
    if ((*(uint8_t *)(v_stack_p8 + 0x19)) != 0) goto loc_00240F89;
    *(uint8_t *)(v_stack_p8 + 0x19) = 1;
    goto loc_00240F89;
loc_0024108A:
    if ((*(uint8_t *)(v_stack_p8 + 0x19)) != 0) goto loc_00240F89;
    result = qsort(v_stack_p8 + 40, Arg4, 8, v_rip + 4540398);
    result = MiCompressTbFlushList(v_stack_p8, Arg4, 8, v_rip + 4540398);
    goto loc_00240D8A;
loc_002410C0:
    Arg1 = (uint32_t)((v_stack_p8) & (0x3FFULL));
    if ((v_stack_p18 + Arg1 * 1) > 0x3FFULL) goto loc_00240E97;
    if ((v_stack_p18 + Arg1 * 1) <= Arg1) goto loc_00240E97;
    goto loc_00240F6F;
loc_002410E5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xB8)))) & (15)) == 0) goto loc_00241130;
    result = (result) >> (12);
    result = (result) & ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xB8)));
    Arg1 = (result + result * 2) << (4);
    Arg3 = 0;
    Arg1 = (Arg1) + (local_r13);
    result = MiGetPagePrivilege(Arg1, Arg3 + 2, Arg3, v_rip + 4540398);
    if ((((uint8_t)(result)) & (65)) == 0) goto loc_00240D6E;
loc_00241123:
    if ((uint32_t)(v_stack_p18) != 0) goto loc_00240D79;
    goto loc_00240D6E;
loc_00241130:
    if (local_rdi > result) goto loc_00240D6E;
    goto loc_00241123;
loc_00241145:
    result = (result) ^ (result + v_stack_p18 * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + v_stack_p18 * 1);
    *(uint64_t *)(arg3 + (uint32_t)(*(uint32_t *)(arg3 + 0x1C)) - 0x1 + 0x5 * 8 + 0x28) = result;
    goto loc_00240F89;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xAE` | `16` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0x270` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg3` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x10` | `32` | `W` |
| `Arg3` | `+ 0x19` | `8` | `R` |
| `Arg3` | `+ 0x19` | `8` | `W` |
| `Arg3` | `+ 0x1C` | `32` | `R` |
| `Arg3` | `+ 0x1C` | `32` | `W` |
| `Arg3` | `+ 0x20` | `64` | `R/W` |
| `Arg3` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `W` |
| `Arg3` | `+ 0x28 + r9*8` | `64` | `W` |
| `Arg3` | `+ 0x28 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00240C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
