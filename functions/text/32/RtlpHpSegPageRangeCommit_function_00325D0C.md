# RtlpHpSegPageRangeCommit

- RVA: `0x00325D0C`–`0x003261CD` (길이 `1,217` bytes)
- VA: `0x0000000140325D0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075C38`
- 디코드: `343`개 명령, `1,217/1,217` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00325F72` → [RtlpHpSegMgrCommit](RtlpHpSegMgrCommit_function_00326BE4.md) (function, `0x00326BE4`)
- `0x0032615E` → [RtlpLogHeapDecommit](../4F/RtlpLogHeapDecommit_function_004F9EF4.md) (function, `0x004F9EF4`)
- `0x00326176` → [RtlpLogHeapCommit](../4F/RtlpLogHeapCommit_function_004F9F74.md) (function, `0x004F9F74`)

### Direct callers
- [RtlpHpSegLfhVsDecommit](RtlpHpSegLfhVsDecommit_function_003243F0.md) at `0x003244AF`
- [RtlpHpSegLfhVsCommit](RtlpHpSegLfhVsCommit_function_00325750.md) at `0x0032581F`
- [RtlpHpSegPageRangeCoalesce](RtlpHpSegPageRangeCoalesce_function_00325860.md) at `0x00325A47`
- [RtlpHpSegAlloc](RtlpHpSegAlloc_function_003265BC.md) at `0x00326674`
- [RtlpHpSegAlloc](RtlpHpSegAlloc_function_003265BC.md) at `0x003266F5`
- [RtlpHpMetadataCommit](../60/RtlpHpMetadataCommit_function_00603540.md) at `0x0060365B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00325D0C  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00325D11  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00325D16  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00325D1B  53                              push rbx
00325D1C  55                              push rbp
00325D1D  56                              push rsi
00325D1E  57                              push rdi
00325D1F  41 54                           push r12
00325D21  41 55                           push r13
00325D23  41 56                           push r14
00325D25  41 57                           push r15
00325D27  48 83 EC 68                     sub rsp, 0x68
00325D2B  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
00325D32  45 8B F8                        mov r15d, r8d
00325D35  C1 E8 16                        shr eax, 0x16
00325D38  4C 8B D2                        mov r10, rdx
00325D3B  83 E0 02                        and eax, 2
00325D3E  41 8B E9                        mov ebp, r9d
00325D41  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00325D45  4C 8B E1                        mov r12, rcx
00325D48  8A 41 0D                        mov al, byte ptr [rcx + 0xd]
00325D4B  24 07                           and al, 7
00325D4D  3C 01                           cmp al, 1
00325D4F  48 8B 01                        mov rax, qword ptr [rcx]
00325D52  8A 49 09                        mov cl, byte ptr [rcx + 9]
00325D55  45 1B C0                        sbb r8d, r8d
00325D58  48 23 C2                        and rax, rdx
00325D5B  48 2B D0                        sub rdx, rax
00325D5E  41 81 E0 00 7E 00 00            and r8d, 0x7e00
00325D65  48 C1 FA 05                     sar rdx, 5
00325D69  41 81 C0 FF 01 00 00            add r8d, 0x1ff
00325D70  D3 E2                           shl edx, cl
00325D72  41 8B C7                        mov eax, r15d
00325D75  41 2B C1                        sub eax, r9d
00325D78  44 89 44 24 4C                  mov dword ptr [rsp + 0x4c], r8d
00325D7D  45 03 CF                        add r9d, r15d
00325D80  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00325D85  85 ED                           test ebp, ebp
00325D87  44 0F 4E C8                     cmovle r9d, eax
00325D8B  33 C9                           xor ecx, ecx
00325D8D  41 83 CD FF                     or r13d, 0xffffffff
00325D91  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
00325D96  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
00325D9A  45 3B F9                        cmp r15d, r9d
00325D9D  72 23                           jb 0x140325dc2
00325D9F  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00325DA7  48 85 C0                        test rax, rax
00325DAA  74 02                           je 0x140325dae
00325DAC  89 08                           mov dword ptr [rax], ecx
00325DAE  33 C0                           xor eax, eax
00325DB0  48 83 C4 68                     add rsp, 0x68
00325DB4  41 5F                           pop r15
00325DB6  41 5E                           pop r14
00325DB8  41 5D                           pop r13
00325DBA  41 5C                           pop r12
00325DBC  5F                              pop rdi
00325DBD  5E                              pop rsi
00325DBE  5D                              pop rbp
00325DBF  5B                              pop rbx
00325DC0  C3                              ret
00325DC1  CC                              int3
00325DC2  41 8B D8                        mov ebx, r8d
00325DC5  41 8D 0C 17                     lea ecx, [r15 + rdx]
00325DC9  41 0F B6 54 24 09               movzx edx, byte ptr [r12 + 9]
00325DCF  41 23 C8                        and ecx, r8d
00325DD2  2B D9                           sub ebx, ecx
00325DD4  45 8B C7                        mov r8d, r15d
00325DD7  41 8B C1                        mov eax, r9d
00325DDA  FF C3                           inc ebx
00325DDC  41 2B C7                        sub eax, r15d
00325DDF  8B CA                           mov ecx, edx
00325DE1  3B D8                           cmp ebx, eax
00325DE3  41 BB 01 00 00 00               mov r11d, 1
00325DE9  41 8B FD                        mov edi, r13d
00325DEC  0F 43 D8                        cmovae ebx, eax
00325DEF  41 D3 E3                        shl r11d, cl
00325DF2  8B CA                           mov ecx, edx
00325DF4  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00325DF8  49 D3 E8                        shr r8, cl
00325DFB  4D 8B C8                        mov r9, r8
00325DFE  49 D3 E0                        shl r8, cl
00325E01  49 C1 E1 05                     shl r9, 5
00325E05  45 8D 73 FF                     lea r14d, [r11 - 1]
00325E09  4D 03 CA                        add r9, r10
00325E0C  45 8B D6                        mov r10d, r14d
00325E0F  45 23 D7                        and r10d, r15d
00325E12  41 8D 42 FF                     lea eax, [r10 - 1]
00325E16  03 C3                           add eax, ebx
00325E18  33 DB                           xor ebx, ebx
00325E1A  44 23 F0                        and r14d, eax
00325E1D  8B F0                           mov esi, eax
00325E1F  48 D3 EE                        shr rsi, cl
00325E22  41 FF C6                        inc r14d
00325E25  48 C1 E6 05                     shl rsi, 5
00325E29  41 8B CD                        mov ecx, r13d
00325E2C  49 03 F1                        add rsi, r9
00325E2F  45 85 D2                        test r10d, r10d
00325E32  74 5B                           je 0x140325e8f
00325E34  41 0F B6 41 19                  movzx eax, byte ptr [r9 + 0x19]
00325E39  4C 3B CE                        cmp r9, rsi
00325E3C  41 8B D3                        mov edx, r11d
00325E3F  41 0F 44 D6                     cmove edx, r14d
00325E43  85 ED                           test ebp, ebp
00325E45  0F 8E 69 03 00 00               jle 0x1403261b4
00325E4B  3B C2                           cmp eax, edx
00325E4D  73 39                           jae 0x140325e88
00325E4F  42 8D 0C 00                     lea ecx, [rax + r8]
00325E53  8B DA                           mov ebx, edx
00325E55  41 8D 3C 10                     lea edi, [r8 + rdx]
00325E59  2B D8                           sub ebx, eax
00325E5B  85 DB                           test ebx, ebx
00325E5D  74 29                           je 0x140325e88
00325E5F  85 ED                           test ebp, ebp
00325E61  7F 25                           jg 0x140325e88
00325E63  02 C3                           add al, bl
00325E65  41 88 41 19                     mov byte ptr [r9 + 0x19], al
00325E69  EB 1D                           jmp 0x140325e88
00325E6B  41 3B CD                        cmp ecx, r13d
00325E6E  75 04                           jne 0x140325e74
00325E70  43 8D 0C 02                     lea ecx, [r10 + r8]
00325E74  41 8B D3                        mov edx, r11d
00325E77  43 8D 3C 18                     lea edi, [r8 + r11]
00325E7B  41 2B D2                        sub edx, r10d
00325E7E  85 D2                           test edx, edx
00325E80  0F 85 83 00 00 00               jne 0x140325f09
00325E86  03 DA                           add ebx, edx
00325E88  49 83 C1 20                     add r9, 0x20
00325E8C  45 03 C3                        add r8d, r11d
00325E8F  4C 3B CE                        cmp r9, rsi
00325E92  73 16                           jae 0x140325eaa
00325E94  45 0F B6 51 19                  movzx r10d, byte ptr [r9 + 0x19]
00325E99  33 D2                           xor edx, edx
00325E9B  85 ED                           test ebp, ebp
00325E9D  0F 8E 66 02 00 00               jle 0x140326109
00325EA3  45 3B D3                        cmp r10d, r11d
00325EA6  73 DE                           jae 0x140325e86
00325EA8  EB C1                           jmp 0x140325e6b
00325EAA  75 1A                           jne 0x140325ec6
00325EAC  45 0F B6 51 19                  movzx r10d, byte ptr [r9 + 0x19]
00325EB1  33 D2                           xor edx, edx
00325EB3  85 ED                           test ebp, ebp
00325EB5  0F 8E 70 02 00 00               jle 0x14032612b
00325EBB  45 3B D6                        cmp r10d, r14d
00325EBE  0F 82 C0 01 00 00               jb 0x140326084
00325EC4  03 DA                           add ebx, edx
00325EC6  85 DB                           test ebx, ebx
00325EC8  44 8B F1                        mov r14d, ecx
00325ECB  45 0F 44 F7                     cmove r14d, r15d
00325ECF  2B F9                           sub edi, ecx
00325ED1  85 DB                           test ebx, ebx
00325ED3  0F 44 7C 24 40                  cmove edi, dword ptr [rsp + 0x40]
00325ED8  75 44                           jne 0x140325f1e
00325EDA  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
00325EE2  44 03 7C 24 40                  add r15d, dword ptr [rsp + 0x40]
00325EE7  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00325EEB  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00325EF0  03 CB                           add ecx, ebx
00325EF2  44 8B 44 24 4C                  mov r8d, dword ptr [rsp + 0x4c]
00325EF7  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
00325EFC  44 89 BC 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r15d
00325F04  E9 8D FE FF FF                  jmp 0x140325d96
00325F09  85 ED                           test ebp, ebp
00325F0B  0F 8F 75 FF FF FF               jg 0x140325e86
00325F11  41 8D 04 12                     lea eax, [r10 + rdx]
00325F15  41 88 41 19                     mov byte ptr [r9 + 0x19], al
00325F19  E9 68 FF FF FF                  jmp 0x140325e86
00325F1E  4D 8B 2C 24                     mov r13, qword ptr [r12]
00325F22  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00325F27  4C 23 AC 24 B8 00 00 00         and r13, qword ptr [rsp + 0xb8]
00325F2F  41 03 F6                        add esi, r14d
00325F32  89 B4 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], esi
00325F39  85 DB                           test ebx, ebx
00325F3B  0F 8E 73 01 00 00               jle 0x1403260b4
00325F41  F6 84 24 D0 00 00 00 02         test byte ptr [rsp + 0xd0], 2
00325F49  B8 00 10 00 00                  mov eax, 0x1000
00325F4E  B9 00 10 00 40                  mov ecx, 0x40001000
00325F53  0F 45 C1                        cmovne eax, ecx
00325F56  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00325F5A  44 8B CF                        mov r9d, edi
00325F5D  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00325F61  44 8B C6                        mov r8d, esi
00325F64  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00325F68  49 8B CC                        mov rcx, r12
00325F6B  49 8B D5                        mov rdx, r13
00325F6E  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00325F72  E8 6D 0C 00 00                  call 0x140326be4
00325F77  85 C0                           test eax, eax
00325F79  0F 88 31 FE FF FF               js 0x140325db0
00325F7F  85 DB                           test ebx, ebx
00325F81  0F 8E BA 00 00 00               jle 0x140326041
00325F87  41 0F B6 54 24 09               movzx edx, byte ptr [r12 + 9]
00325F8D  BE 01 00 00 00                  mov esi, 1
00325F92  8B CA                           mov ecx, edx
00325F94  45 8B CE                        mov r9d, r14d
00325F97  D3 E6                           shl esi, cl
00325F99  8B CA                           mov ecx, edx
00325F9B  49 D3 E9                        shr r9, cl
00325F9E  33 D2                           xor edx, edx
00325FA0  4D 8B C1                        mov r8, r9
00325FA3  49 D3 E1                        shl r9, cl
00325FA6  49 C1 E0 05                     shl r8, 5
00325FAA  4C 03 84 24 B8 00 00 00         add r8, qword ptr [rsp + 0xb8]
00325FB2  8D 46 FF                        lea eax, [rsi - 1]
00325FB5  44 23 F0                        and r14d, eax
00325FB8  45 8D 7E FF                     lea r15d, [r14 - 1]
00325FBC  44 03 FF                        add r15d, edi
00325FBF  41 8B EF                        mov ebp, r15d
00325FC2  44 23 F8                        and r15d, eax
00325FC5  48 D3 ED                        shr rbp, cl
00325FC8  41 FF C7                        inc r15d
00325FCB  48 C1 E5 05                     shl rbp, 5
00325FCF  83 C9 FF                        or ecx, 0xffffffff
00325FD2  49 03 E8                        add rbp, r8
00325FD5  44 0B D9                        or r11d, ecx
00325FD8  45 85 F6                        test r14d, r14d
00325FDB  0F 85 9C 01 00 00               jne 0x14032617d
00325FE1  4C 3B C5                        cmp r8, rbp
00325FE4  73 26                           jae 0x14032600c
00325FE6  45 0F B6 70 19                  movzx r14d, byte ptr [r8 + 0x19]
00325FEB  45 33 D2                        xor r10d, r10d
00325FEE  44 3B F6                        cmp r14d, esi
00325FF1  0F 82 D4 00 00 00               jb 0x1403260cb
00325FF7  45 85 D2                        test r10d, r10d
00325FFA  0F 85 BE 00 00 00               jne 0x1403260be
00326000  41 03 D2                        add edx, r10d
00326003  49 83 C0 20                     add r8, 0x20
00326007  44 03 CE                        add r9d, esi
0032600A  EB D5                           jmp 0x140325fe1
0032600C  75 14                           jne 0x140326022
0032600E  41 0F B6 70 19                  movzx esi, byte ptr [r8 + 0x19]
00326013  45 33 D2                        xor r10d, r10d
00326016  41 3B F7                        cmp esi, r15d
00326019  0F 82 C4 00 00 00               jb 0x1403260e3
0032601F  41 03 D2                        add edx, r10d
00326022  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
00326029  8B AC 24 C8 00 00 00            mov ebp, dword ptr [rsp + 0xc8]
00326030  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00326038  85 D2                           test edx, edx
0032603A  74 05                           je 0x140326041
0032603C  41 8B FB                        mov edi, r11d
0032603F  2B F9                           sub edi, ecx
00326041  49 0F BF 44 24 16               movsx rax, word ptr [r12 + 0x16]
00326047  48 63 CB                        movsxd rcx, ebx
0032604A  F0 4A 01 4C 20 08               lock add qword ptr [rax + r12 + 8], rcx
00326050  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
00326058  41 0F B7 42 1C                  movzx eax, word ptr [r10 + 0x1c]
0032605D  66 F7 D0                        not ax
00326060  66 03 C3                        add ax, bx
00326063  66 F7 D0                        not ax
00326066  66 41 89 42 1C                  mov word ptr [r10 + 0x1c], ax
0032606B  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
00326070  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00326073  84 C0                           test al, al
00326075  0F 88 D1 00 00 00               js 0x14032614c
0032607B  41 83 CD FF                     or r13d, 0xffffffff
0032607F  E9 5E FE FF FF                  jmp 0x140325ee2
00326084  41 3B CD                        cmp ecx, r13d
00326087  75 04                           jne 0x14032608d
00326089  43 8D 0C 02                     lea ecx, [r10 + r8]
0032608D  41 8B D6                        mov edx, r14d
00326090  43 8D 3C 30                     lea edi, [r8 + r14]
00326094  41 2B D2                        sub edx, r10d
00326097  85 D2                           test edx, edx
00326099  0F 84 25 FE FF FF               je 0x140325ec4
0032609F  85 ED                           test ebp, ebp
003260A1  0F 8F 1D FE FF FF               jg 0x140325ec4
003260A7  41 8D 04 12                     lea eax, [r10 + rdx]
003260AB  41 88 41 19                     mov byte ptr [r9 + 0x19], al
003260AF  E9 10 FE FF FF                  jmp 0x140325ec4
003260B4  B8 00 40 00 00                  mov eax, 0x4000
003260B9  E9 98 FE FF FF                  jmp 0x140325f56
003260BE  43 8D 04 16                     lea eax, [r14 + r10]
003260C2  41 88 40 19                     mov byte ptr [r8 + 0x19], al
003260C6  E9 35 FF FF FF                  jmp 0x140326000
003260CB  83 F9 FF                        cmp ecx, -1
003260CE  75 04                           jne 0x1403260d4
003260D0  43 8D 0C 0E                     lea ecx, [r14 + r9]
003260D4  44 8B D6                        mov r10d, esi
003260D7  45 8D 1C 31                     lea r11d, [r9 + rsi]
003260DB  45 2B D6                        sub r10d, r14d
003260DE  E9 14 FF FF FF                  jmp 0x140325ff7
003260E3  83 F9 FF                        cmp ecx, -1
003260E6  75 04                           jne 0x1403260ec
003260E8  42 8D 0C 0E                     lea ecx, [rsi + r9]
003260EC  45 8B D7                        mov r10d, r15d
003260EF  47 8D 1C 39                     lea r11d, [r9 + r15]
003260F3  44 2B D6                        sub r10d, esi
003260F6  0F 84 23 FF FF FF               je 0x14032601f
003260FC  42 8D 04 16                     lea eax, [rsi + r10]
00326100  41 88 40 19                     mov byte ptr [r8 + 0x19], al
00326104  E9 16 FF FF FF                  jmp 0x14032601f
00326109  45 85 D2                        test r10d, r10d
0032610C  0F 84 74 FD FF FF               je 0x140325e86
00326112  41 8B D2                        mov edx, r10d
00326115  43 8D 3C 02                     lea edi, [r10 + r8]
00326119  F7 DA                           neg edx
0032611B  41 8B C0                        mov eax, r8d
0032611E  41 3B CD                        cmp ecx, r13d
00326121  0F 45 C1                        cmovne eax, ecx
00326124  8B C8                           mov ecx, eax
00326126  E9 53 FD FF FF                  jmp 0x140325e7e
0032612B  45 85 D2                        test r10d, r10d
0032612E  0F 84 90 FD FF FF               je 0x140325ec4
00326134  41 8B D2                        mov edx, r10d
00326137  43 8D 3C 02                     lea edi, [r10 + r8]
0032613B  F7 DA                           neg edx
0032613D  41 3B CD                        cmp ecx, r13d
00326140  44 0F 45 C1                     cmovne r8d, ecx
00326144  41 8B C8                        mov ecx, r8d
00326147  E9 4B FF FF FF                  jmp 0x140326097
0032614C  C1 E6 0C                        shl esi, 0xc
0032614F  C1 E7 0C                        shl edi, 0xc
00326152  8B D6                           mov edx, esi
00326154  49 03 D5                        add rdx, r13
00326157  44 8B C7                        mov r8d, edi
0032615A  85 DB                           test ebx, ebx
0032615C  7F 12                           jg 0x140326170
0032615E  E8 91 3D 1D 00                  call 0x1404f9ef4
00326163  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
0032616B  E9 0B FF FF FF                  jmp 0x14032607b
00326170  41 B9 0A 00 00 00               mov r9d, 0xa
00326176  E8 F9 3D 1D 00                  call 0x1404f9f74
0032617B  EB E6                           jmp 0x140326163
0032617D  45 0F B6 50 19                  movzx r10d, byte ptr [r8 + 0x19]
00326182  4C 3B C5                        cmp r8, rbp
00326185  8B C6                           mov eax, esi
00326187  41 0F 44 C7                     cmove eax, r15d
0032618B  44 3B D0                        cmp r10d, eax
0032618E  0F 83 6F FE FF FF               jae 0x140326003
00326194  8B D0                           mov edx, eax
00326196  43 8D 0C 0A                     lea ecx, [r10 + r9]
0032619A  45 8D 1C 01                     lea r11d, [r9 + rax]
0032619E  41 2B D2                        sub edx, r10d
003261A1  0F 84 5C FE FF FF               je 0x140326003
003261A7  41 8D 04 12                     lea eax, [r10 + rdx]
003261AB  41 88 40 19                     mov byte ptr [r8 + 0x19], al
003261AF  E9 4F FE FF FF                  jmp 0x140326003
003261B4  41 3B C2                        cmp eax, r10d
003261B7  0F 86 CB FC FF FF               jbe 0x140325e88
003261BD  43 8D 0C 10                     lea ecx, [r8 + r10]
003261C1  41 8B DA                        mov ebx, r10d
003261C4  42 8D 3C 00                     lea edi, [rax + r8]
003261C8  E9 8C FC FF FF                  jmp 0x140325e59
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpSegPageRangeCommit(__int64 a1, __int64 a2, int a3, int a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned int v_stack_pC0;
    unsigned int v_stack_pC8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (104);
    result = (unsigned int)(((unsigned int)(a5)) >> (22));
    result = (unsigned int)((result) & (2));
    v_stack_m60 = (unsigned int)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 13)) & (7));
    result = (*(unsigned __int64 *)(a1)) & (a2);
    a2 = (a2) - (result);
    a3 = (unsigned int)((a3) & (0x7E00ULL));
    a2 = (a2) >> (5);
    a3 = (unsigned int)((a3) + (511));
    a2 = (unsigned int)((a2) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 9))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) - (a4));
    v_stack_m5C = a3;
    a4 = (unsigned int)((a4) + ((unsigned int)((unsigned int)(a3))));
    v_stack_m50 = a2;
    if (condition_is_less_or_equal) { a4 = (unsigned int)(result); }
    a1 = 0;
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    v_stack_m58 = a4;
loc_00325D96:
    v_stack_m64 = 0;
    if (((unsigned int)((unsigned int)(a3))) < a4) goto loc_00325DC2;
    if (a6 != 0) {
        *(unsigned int *)(a6) = 0;
    }
    result = 0;
loc_00325DB0:
    v_rsp = (v_rsp) + (104);
    return result;
loc_00325DC2:
    a1 = (unsigned int)(((unsigned int)(a3) + a2 * 1) & (a3));
    v_rbx = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) + 1);
    result = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)((unsigned int)(a3))));
    if (((unsigned int)(v_rbx)) >= ((unsigned int)(result))) { v_rbx = (unsigned int)(result); }
    v_r11 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9))))));
    v_stack_p40 = (unsigned int)(v_rbx);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(a3)))) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))));
    a3 = (a3) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))));
    a4 = (a3) << (5);
    a4 = (a4) + (a2);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r11 - 1))) & ((unsigned int)((unsigned int)(a3))));
    result = (unsigned int)((v_r10 - 1) + ((unsigned int)(v_rbx)));
    v_rbx = 0;
    v_r14 = (unsigned int)((v_r11 - 1) & ((unsigned int)(result)));
    v_rsi = ((unsigned int)((unsigned int)(result))) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))));
    v_r14 = (unsigned int)((v_r14) + 1);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (a4);
    if ((unsigned int)(v_r10) == 0) goto loc_00325E8F;
    a2 = (unsigned int)((unsigned int)(v_r11));
    if (a4 == v_rsi) { a2 = (unsigned int)(v_r14); }
    if (condition_is_less_or_equal) goto loc_003261B4;
    if (((unsigned int)(*(unsigned __int8 *)(a4 + 25))) >= ((unsigned int)(a2))) goto loc_00325E88;
loc_00325E59:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(*(unsigned __int8 *)(a4 + 25))));
    if ((unsigned int)(v_rbx) == 0) goto loc_00325E88;
    if (condition_is_greater) goto loc_00325E88;
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 25)) + ((unsigned __int8)(v_rbx)));
    *(unsigned __int8 *)(a4 + 25) = (unsigned __int8)(result);
    goto loc_00325E88;
loc_00325E6B:
    if (((unsigned int)(*(unsigned __int8 *)(a4 + 25) + a3 * 1)) == ((unsigned int)(v_r13))) {
        a1 = v_r10 + a3 * 1;
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) - ((unsigned int)(v_r10)));
loc_00325E7E:
    if ((unsigned int)(a2) != 0) goto loc_00325F09;
loc_00325E86:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(a2)));
loc_00325E88:
    a4 = (a4) + (32);
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r11)));
loc_00325E8F:
    if (a4 >= v_rsi) goto loc_00325EAA;
    a2 = 0;
    if (condition_is_less_or_equal) goto loc_00326109;
    if (((unsigned int)(*(unsigned __int8 *)(a4 + 25))) >= ((unsigned int)(v_r11))) goto loc_00325E86;
    goto loc_00325E6B;
loc_00325EAA:
    if (((unsigned int)(*(unsigned __int8 *)(a4 + 25))) != ((unsigned int)(v_r11))) goto loc_00325EC6;
    a2 = 0;
    if (condition_is_less_or_equal) goto loc_0032612B;
    if (((unsigned int)(*(unsigned __int8 *)(a4 + 25))) < ((unsigned int)(v_r14))) goto loc_00326084;
loc_00325EC4:
    v_rbx = (unsigned int)((v_rbx) + (0));
loc_00325EC6:
    v_r14 = (unsigned int)((unsigned int)(a1));
    if ((unsigned int)(v_rbx) == 0) { v_r14 = (unsigned int)((unsigned int)(a3)); }
    v_rdi = (unsigned int)((a3 + v_r11 * 1) - ((unsigned int)(a1)));
    if ((unsigned int)(v_rbx) == 0) { v_rdi = v_stack_p40; }
    if ((unsigned int)(v_rbx) != 0) goto loc_00325F1E;
loc_00325EE2:
    v_r15 = (unsigned int)(((unsigned int)(a3)) + (v_stack_p40));
    a1 = (unsigned int)(((unsigned int)(v_stack_p44)) + ((unsigned int)(v_rbx)));
    v_stack_pC0 = (unsigned int)(v_r15);
    goto loc_00325D96;
loc_00325F09:
    if (condition_is_greater) goto loc_00325E86;
    *(unsigned __int8 *)((unsigned int)(v_stack_p50) + 25) = (unsigned __int8)(v_stack_pB8 + v_stack_p58 * 1);
    goto loc_00325E86;
loc_00325F1E:
    v_r13 = (*(unsigned __int64 *)(a1)) & (v_stack_pB8);
    v_rsi = (unsigned int)((v_stack_p58) + ((unsigned int)(v_r14)));
    v_stack_pB0 = (unsigned int)(v_rsi);
    if (condition_is_less_or_equal) goto loc_003260B4;
    result = (unsigned int)(0x1000ULL);
    if (((a5) & (2)) != 0) { result = (unsigned int)((unsigned int)(0x40001000ULL)); }
loc_00325F56:
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_p48));
    v_stack_p28 = (unsigned int)(result);
    v_stack_p20 = (unsigned int)(v_rbx);
    result = RtlpHpSegMgrCommit(a1, v_r13, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_rdi)));
    if (sign_flag) goto loc_00325DB0;
    if (condition_is_less_or_equal) goto loc_00326041;
    v_rsi = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9))))));
    a4 = ((unsigned int)((unsigned int)(v_r14))) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))));
    a2 = 0;
    a4 = (a4) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))));
    a3 = (a4) << (5);
    a3 = (a3) + (v_stack_pB8);
    v_r14 = (unsigned int)((v_r14) & ((unsigned int)(v_rsi - 1)));
    v_r15 = (unsigned int)((v_r14 - 1) + ((unsigned int)(v_rdi)));
    v_r15 = (unsigned int)((v_r15) & ((unsigned int)(v_rsi - 1)));
    v_rbp = ((unsigned int)((unsigned int)(v_r15))) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))));
    v_r15 = (unsigned int)((v_r15) + 1);
    v_rbp = (v_rbp) << (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 9)))) | (0xFFFFFFFFULL));
    v_rbp = (v_rbp) + (a3);
    v_r11 = (unsigned int)((v_r11) | ((unsigned int)(a1)));
    if ((unsigned int)(v_r14) != 0) goto loc_0032617D;
loc_00325FE1:
    if (a3 >= v_rbp) goto loc_0032600C;
    v_r10 = 0;
    if (((unsigned int)(*(unsigned __int8 *)(a3 + 25))) < ((unsigned int)(v_rsi))) goto loc_003260CB;
loc_00325FF7:
    if (0 != 0) goto loc_003260BE;
loc_00326000:
    a2 = (unsigned int)((a2) + (0));
loc_00326003:
    a3 = (a3) + (32);
    a4 = (unsigned int)((a4) + ((unsigned int)(v_rsi)));
    goto loc_00325FE1;
loc_0032600C:
    if (condition_is_not_equal) goto loc_00326022;
    v_r10 = 0;
    if (((unsigned int)(*(unsigned __int8 *)(a3 + 25))) < ((unsigned int)(v_r15))) goto loc_003260E3;
loc_0032601F:
    a2 = (unsigned int)((a2) + (0));
loc_00326022:
    if ((unsigned int)(a2) != 0) {
        v_rdi = (unsigned int)(v_r11);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(a1)));
    }
    result = (unsigned __int16)(~(*(unsigned __int16 *)(v_stack_pB8 + 28)));
    result = (unsigned __int16)((result) + ((unsigned __int16)(v_rbx)));
    result = (unsigned __int16)(~(result));
    *(unsigned __int16 *)(v_stack_pB8 + 28) = (unsigned __int16)(result);
    if (sign_flag) goto loc_0032614C;
loc_0032607B:
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    goto loc_00325EE2;
loc_00326084:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 56))) == ((unsigned int)(v_r13))) {
        a1 = v_stack_pB8 + a3 * 1;
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a3 + 25)))) - ((unsigned int)(v_stack_pB8)));
loc_00326097:
    if ((unsigned int)(a2) == 0) goto loc_00325EC4;
    if (condition_is_greater) goto loc_00325EC4;
    *(unsigned __int8 *)(a4 + 25) = (unsigned __int8)(v_stack_pB8 + a2 * 1);
    goto loc_00325EC4;
loc_003260B4:
    goto loc_00325F56;
loc_003260BE:
    *(unsigned __int8 *)(a3 + 25) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 25) + v_stack_pB8 * 1);
    goto loc_00326000;
loc_003260CB:
    if (((unsigned int)(a1)) == -1) {
        a1 = *(unsigned __int8 *)(a3 + 25) + a4 * 1;
    }
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_pB0)))) - ((unsigned int)(*(unsigned __int8 *)(a3 + 25))));
    goto loc_00325FF7;
loc_003260E3:
    if (((unsigned int)(a1)) == -1) {
        a1 = (unsigned int)(v_stack_pB0) + a4 * 1;
    }
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_pC0)))) - ((unsigned int)((unsigned int)(v_stack_pB0))));
    if (condition_is_equal) goto loc_0032601F;
    *(unsigned __int8 *)(a3 + 25) = (unsigned __int8)((unsigned int)(v_stack_pB0) + v_r10 * 1);
    goto loc_0032601F;
loc_00326109:
    if ((unsigned int)(v_r10) == 0) goto loc_00325E86;
    a2 = (unsigned int)(-((unsigned int)((unsigned int)(v_r10))));
    result = (unsigned int)(a3);
    if (((unsigned int)(a1)) != ((unsigned int)(v_r13))) { result = (unsigned int)(a1); }
    goto loc_00325E7E;
loc_0032612B:
    if ((unsigned int)(v_r10) == 0) goto loc_00325EC4;
    a2 = (unsigned int)(-((unsigned int)((unsigned int)(v_r10))));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) { a3 = (unsigned int)((unsigned int)((unsigned int)(result))); }
    goto loc_00326097;
loc_0032614C:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_pB0)) << (12));
    v_rdi = (unsigned int)((v_r10 + a3 * 1) << (12));
    a2 = ((unsigned int)((unsigned int)(v_rsi))) + (v_r13);
    if (condition_is_greater) goto loc_00326170;
    result = RtlpLogHeapDecommit((unsigned int)(a3), a2, (unsigned int)((unsigned int)(v_rdi)), a4);
loc_00326163:
    goto loc_0032607B;
loc_00326170:
    result = RtlpLogHeapCommit((unsigned int)(a3), a2, (unsigned int)((unsigned int)(v_rdi)), 10);
    goto loc_00326163;
loc_0032617D:
    result = (unsigned int)((unsigned int)(v_rsi));
    if (((unsigned int)((unsigned int)(v_rdi))) == ((unsigned int)(v_stack_pC8))) { result = (unsigned int)((unsigned int)(v_stack_pC0)); }
    if (((unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 25))) >= ((unsigned int)(result))) goto loc_00326003;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 25))));
    if (condition_is_equal) goto loc_00326003;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 25) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 25) + a2 * 1);
    goto loc_00326003;
loc_003261B4:
    if (((unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 25) + a2 * 1)) <= ((unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 25)))) goto loc_00325E88;
    goto loc_00325E59;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpSegPageRangeCommit(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint32_t v_stack_pC0;
    uint32_t v_stack_pC8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (104);
    result = (uint32_t)(((uint32_t)(Arg5)) >> (22));
    result = (uint32_t)((result) & (2));
    v_stack_m60 = (uint32_t)(result);
    result = (uint8_t)((*(uint8_t *)(arg1 + 0xD)) & (7));
    result = (*(uint64_t *)(arg1)) & (Arg2);
    Arg2 = (Arg2) - (result);
    Arg3 = (uint32_t)((Arg3) & (0x7E00ULL));
    Arg2 = (Arg2) >> (5);
    Arg3 = (uint32_t)((Arg3) + (511));
    Arg2 = (uint32_t)((Arg2) << ((uint8_t)(*(uint8_t *)(arg1 + 0x9))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) - (Arg4));
    v_stack_m5C = Arg3;
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)((uint32_t)(Arg3))));
    v_stack_m50 = Arg2;
    if (condition_is_less_or_equal) { Arg4 = (uint32_t)(result); }
    Arg1 = 0;
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    v_stack_m58 = Arg4;
loc_00325D96:
    v_stack_m64 = 0;
    if (((uint32_t)((uint32_t)(Arg3))) < Arg4) goto loc_00325DC2;
    if (Arg6 != 0) {
        *(uint32_t *)(Arg6) = 0;
    }
    result = 0;
loc_00325DB0:
    local_rsp = (local_rsp) + (104);
    return result;
loc_00325DC2:
    Arg1 = (uint32_t)(((uint32_t)(Arg3) + Arg2 * 1) & (Arg3));
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(Arg1)));
    local_rbx = (uint32_t)((local_rbx) + 1);
    result = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)((uint32_t)(Arg3))));
    if (((uint32_t)(local_rbx)) >= ((uint32_t)(result))) { local_rbx = (uint32_t)(result); }
    local_r11 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9))))));
    v_stack_p40 = (uint32_t)(local_rbx);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))));
    Arg3 = (Arg3) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))));
    Arg4 = (Arg3) << (5);
    Arg4 = (Arg4) + (Arg2);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r11 - 1))) & ((uint32_t)((uint32_t)(Arg3))));
    result = (uint32_t)((local_r10 - 1) + ((uint32_t)(local_rbx)));
    local_rbx = 0;
    local_r14 = (uint32_t)((local_r11 - 1) & ((uint32_t)(result)));
    local_rsi = ((uint32_t)((uint32_t)(result))) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))));
    local_r14 = (uint32_t)((local_r14) + 1);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (Arg4);
    if ((uint32_t)(local_r10) == 0) goto loc_00325E8F;
    Arg2 = (uint32_t)((uint32_t)(local_r11));
    if (Arg4 == local_rsi) { Arg2 = (uint32_t)(local_r14); }
    if (condition_is_less_or_equal) goto loc_003261B4;
    if (((uint32_t)(*(uint8_t *)(Arg4 + 0x19))) >= ((uint32_t)(Arg2))) goto loc_00325E88;
loc_00325E59:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(*(uint8_t *)(Arg4 + 0x19))));
    if ((uint32_t)(local_rbx) == 0) goto loc_00325E88;
    if (condition_is_greater) goto loc_00325E88;
    result = (uint8_t)((*(uint8_t *)(Arg4 + 0x19)) + ((uint8_t)(local_rbx)));
    *(uint8_t *)(Arg4 + 0x19) = (uint8_t)(result);
    goto loc_00325E88;
loc_00325E6B:
    if (((uint32_t)(*(uint8_t *)(Arg4 + 0x19) + Arg3 * 1)) == ((uint32_t)(local_r13))) {
        Arg1 = local_r10 + Arg3 * 1;
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) - ((uint32_t)(local_r10)));
loc_00325E7E:
    if ((uint32_t)(Arg2) != 0) goto loc_00325F09;
loc_00325E86:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(Arg2)));
loc_00325E88:
    Arg4 = (Arg4) + (32);
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r11)));
loc_00325E8F:
    if (Arg4 >= local_rsi) goto loc_00325EAA;
    Arg2 = 0;
    if (condition_is_less_or_equal) goto loc_00326109;
    if (((uint32_t)(*(uint8_t *)(Arg4 + 0x19))) >= ((uint32_t)(local_r11))) goto loc_00325E86;
    goto loc_00325E6B;
loc_00325EAA:
    if (((uint32_t)(*(uint8_t *)(Arg4 + 0x19))) != ((uint32_t)(local_r11))) goto loc_00325EC6;
    Arg2 = 0;
    if (condition_is_less_or_equal) goto loc_0032612B;
    if (((uint32_t)(*(uint8_t *)(Arg4 + 0x19))) < ((uint32_t)(local_r14))) goto loc_00326084;
loc_00325EC4:
    local_rbx = (uint32_t)((local_rbx) + (0));
loc_00325EC6:
    local_r14 = (uint32_t)((uint32_t)(Arg1));
    if ((uint32_t)(local_rbx) == 0) { local_r14 = (uint32_t)((uint32_t)(Arg3)); }
    local_rdi = (uint32_t)((Arg3 + local_r11 * 1) - ((uint32_t)(Arg1)));
    if ((uint32_t)(local_rbx) == 0) { local_rdi = v_stack_p40; }
    if ((uint32_t)(local_rbx) != 0) goto loc_00325F1E;
loc_00325EE2:
    local_r15 = (uint32_t)(((uint32_t)(Arg3)) + (v_stack_p40));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p44)) + ((uint32_t)(local_rbx)));
    v_stack_pC0 = (uint32_t)(local_r15);
    goto loc_00325D96;
loc_00325F09:
    if (condition_is_greater) goto loc_00325E86;
    *(uint8_t *)((uint32_t)(v_stack_p50) + 0x19) = (uint8_t)(v_stack_pB8 + v_stack_p58 * 1);
    goto loc_00325E86;
loc_00325F1E:
    local_r13 = (*(uint64_t *)(arg1)) & (v_stack_pB8);
    local_rsi = (uint32_t)((v_stack_p58) + ((uint32_t)(local_r14)));
    v_stack_pB0 = (uint32_t)(local_rsi);
    if (condition_is_less_or_equal) goto loc_003260B4;
    result = (uint32_t)(0x1000ULL);
    if (((Arg5) & (2)) != 0) { result = (uint32_t)((uint32_t)(0x40001000ULL)); }
loc_00325F56:
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_p48));
    v_stack_p28 = (uint32_t)(result);
    v_stack_p20 = (uint32_t)(local_rbx);
    result = RtlpHpSegMgrCommit(Arg1, local_r13, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_rdi)));
    if (sign_flag) goto loc_00325DB0;
    if (condition_is_less_or_equal) goto loc_00326041;
    local_rsi = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9))))));
    Arg4 = ((uint32_t)((uint32_t)(local_r14))) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))));
    Arg2 = 0;
    Arg4 = (Arg4) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))));
    Arg3 = (Arg4) << (5);
    Arg3 = (Arg3) + (v_stack_pB8);
    local_r14 = (uint32_t)((local_r14) & ((uint32_t)(local_rsi - 1)));
    local_r15 = (uint32_t)((local_r14 - 1) + ((uint32_t)(local_rdi)));
    local_r15 = (uint32_t)((local_r15) & ((uint32_t)(local_rsi - 1)));
    local_rbp = ((uint32_t)((uint32_t)(local_r15))) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))));
    local_r15 = (uint32_t)((local_r15) + 1);
    local_rbp = (local_rbp) << (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x9)))) | (0xFFFFFFFFULL));
    local_rbp = (local_rbp) + (Arg3);
    local_r11 = (uint32_t)((local_r11) | ((uint32_t)(Arg1)));
    if ((uint32_t)(local_r14) != 0) goto loc_0032617D;
loc_00325FE1:
    if (Arg3 >= local_rbp) goto loc_0032600C;
    local_r10 = 0;
    if (((uint32_t)(*(uint8_t *)(Arg3 + 0x19))) < ((uint32_t)(local_rsi))) goto loc_003260CB;
loc_00325FF7:
    if (0 != 0) goto loc_003260BE;
loc_00326000:
    Arg2 = (uint32_t)((Arg2) + (0));
loc_00326003:
    Arg3 = (Arg3) + (32);
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(local_rsi)));
    goto loc_00325FE1;
loc_0032600C:
    if (condition_is_not_equal) goto loc_00326022;
    local_r10 = 0;
    if (((uint32_t)(*(uint8_t *)(Arg3 + 0x19))) < ((uint32_t)(local_r15))) goto loc_003260E3;
loc_0032601F:
    Arg2 = (uint32_t)((Arg2) + (0));
loc_00326022:
    if ((uint32_t)(Arg2) != 0) {
        local_rdi = (uint32_t)(local_r11);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(Arg1)));
    }
    result = (uint16_t)(~(*(uint16_t *)(v_stack_pB8 + 0x1C)));
    result = (uint16_t)((result) + ((uint16_t)(local_rbx)));
    result = (uint16_t)(~(result));
    *(uint16_t *)(v_stack_pB8 + 0x1C) = (uint16_t)(result);
    if (sign_flag) goto loc_0032614C;
loc_0032607B:
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    goto loc_00325EE2;
loc_00326084:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x38))) == ((uint32_t)(local_r13))) {
        Arg1 = v_stack_pB8 + Arg3 * 1;
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg3 + 0x19)))) - ((uint32_t)(v_stack_pB8)));
loc_00326097:
    if ((uint32_t)(Arg2) == 0) goto loc_00325EC4;
    if (condition_is_greater) goto loc_00325EC4;
    *(uint8_t *)(Arg4 + 0x19) = (uint8_t)(v_stack_pB8 + Arg2 * 1);
    goto loc_00325EC4;
loc_003260B4:
    goto loc_00325F56;
loc_003260BE:
    *(uint8_t *)(Arg3 + 0x19) = (uint8_t)(*(uint8_t *)(Arg3 + 0x19) + v_stack_pB8 * 1);
    goto loc_00326000;
loc_003260CB:
    if (((uint32_t)(Arg1)) == -1) {
        Arg1 = *(uint8_t *)(Arg3 + 0x19) + Arg4 * 1;
    }
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_pB0)))) - ((uint32_t)(*(uint8_t *)(Arg3 + 0x19))));
    goto loc_00325FF7;
loc_003260E3:
    if (((uint32_t)(Arg1)) == -1) {
        Arg1 = (uint32_t)(v_stack_pB0) + Arg4 * 1;
    }
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_pC0)))) - ((uint32_t)((uint32_t)(v_stack_pB0))));
    if (condition_is_equal) goto loc_0032601F;
    *(uint8_t *)(Arg3 + 0x19) = (uint8_t)((uint32_t)(v_stack_pB0) + local_r10 * 1);
    goto loc_0032601F;
loc_00326109:
    if ((uint32_t)(local_r10) == 0) goto loc_00325E86;
    Arg2 = (uint32_t)(-((uint32_t)((uint32_t)(local_r10))));
    result = (uint32_t)(Arg3);
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r13))) { result = (uint32_t)(Arg1); }
    goto loc_00325E7E;
loc_0032612B:
    if ((uint32_t)(local_r10) == 0) goto loc_00325EC4;
    Arg2 = (uint32_t)(-((uint32_t)((uint32_t)(local_r10))));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) { Arg3 = (uint32_t)((uint32_t)((uint32_t)(result))); }
    goto loc_00326097;
loc_0032614C:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_pB0)) << (12));
    local_rdi = (uint32_t)((local_r10 + Arg3 * 1) << (12));
    Arg2 = ((uint32_t)((uint32_t)(local_rsi))) + (local_r13);
    if (condition_is_greater) goto loc_00326170;
    result = RtlpLogHeapDecommit((uint32_t)(Arg3), Arg2, (uint32_t)((uint32_t)(local_rdi)), Arg4);
loc_00326163:
    goto loc_0032607B;
loc_00326170:
    result = RtlpLogHeapCommit((uint32_t)(Arg3), Arg2, (uint32_t)((uint32_t)(local_rdi)), 10);
    goto loc_00326163;
loc_0032617D:
    result = (uint32_t)((uint32_t)(local_rsi));
    if (((uint32_t)((uint32_t)(local_rdi))) == ((uint32_t)(v_stack_pC8))) { result = (uint32_t)((uint32_t)(v_stack_pC0)); }
    if (((uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0x19))) >= ((uint32_t)(result))) goto loc_00326003;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0x19))));
    if (condition_is_equal) goto loc_00326003;
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0x19) = (uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0x19) + Arg2 * 1);
    goto loc_00326003;
loc_003261B4:
    if (((uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0x19) + Arg2 * 1)) <= ((uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0x19)))) goto loc_00325E88;
    goto loc_00325E59;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R` |
| `Arg1` | `+ 0x16` | `16` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00325D0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
