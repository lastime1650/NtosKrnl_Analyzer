# KeQuerySpeculationControlInformation

- RVA: `0x007468A8`–`0x00746F33` (길이 `1,675` bytes)
- VA: `0x00000001407468A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA5B4`
- 디코드: `414`개 명령, `1,675/1,675` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00746A73` → [KeIsImportOptimizationEnabled](../../text/4A/KeIsImportOptimizationEnabled_function_004A8FB8.md) (function, `0x004A8FB8`)
- `0x00746B1E` → [KeKvaShadowingActive](../../text/4B/KeKvaShadowingActive_function_004B2CA8.md) (function, `0x004B2CA8`)
- `0x00746B76` → [HvlQueryL1tfMitigationInformation](../../text/4B/HvlQueryL1tfMitigationInformation_function_004B5334.md) (function, `0x004B5334`)
- `0x00746B92` → [SpcIsFbClearSupported](../../text/6A/SpcIsFbClearSupported_function_006A7864.md) (function, `0x006A7864`)
- `0x00746F03` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00746F15` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5AE21`

### Static image references
- `0x007468F1` → RVA `0x00FC6B48` (`ALMOSTRO`; read)
- `0x00746AAC` → RVA `0x00FC6B60` (`ALMOSTRO`; read)
- `0x00746ACC` → RVA `0x01201840` (`CFGRO`; read)
- `0x00746AFB` → RVA `0x00FC6DD0` (`ALMOSTRO`; read)
- `0x00746B04` → RVA `0x00FC6E7C` (`ALMOSTRO`; read)
- `0x00746B55` → RVA `0x00FC6FE8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00746A73` → [KeIsImportOptimizationEnabled](../../text/4A/KeIsImportOptimizationEnabled_function_004A8FB8.md) (`PAGE` → `.text`)
  - `0x00746B1E` → [KeKvaShadowingActive](../../text/4B/KeKvaShadowingActive_function_004B2CA8.md) (`PAGE` → `.text`)
  - `0x00746B76` → [HvlQueryL1tfMitigationInformation](../../text/4B/HvlQueryL1tfMitigationInformation_function_004B5334.md) (`PAGE` → `.text`)
  - `0x00746B92` → [SpcIsFbClearSupported](../../text/6A/SpcIsFbClearSupported_function_006A7864.md) (`PAGE` → `.text`)
  - `0x00746F03` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00746F15` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007468A8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
007468AD  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
007468B2  57                              push rdi
007468B3  41 54                           push r12
007468B5  41 55                           push r13
007468B7  41 56                           push r14
007468B9  41 57                           push r15
007468BB  48 83 EC 30                     sub rsp, 0x30
007468BF  44 8B E2                        mov r12d, edx
007468C2  83 FA 04                        cmp edx, 4
007468C5  73 11                           jae 0x1407468d8
007468C7  41 C7 00 08 00 00 00            mov dword ptr [r8], 8
007468CE  B8 04 00 00 C0                  mov eax, 0xc0000004
007468D3  E9 47 06 00 00                  jmp 0x140746f1f
007468D8  45 8B EC                        mov r13d, r12d
007468DB  41 B9 08 00 00 00               mov r9d, 8
007468E1  45 3B E1                        cmp r12d, r9d
007468E4  45 0F 43 E9                     cmovae r13d, r9d
007468E8  45 89 28                        mov dword ptr [r8], r13d
007468EB  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
007468F1  48 8B 05 50 02 88 00            mov rax, qword ptr [rip + 0x880250]
007468F8  48 C1 E8 24                     shr rax, 0x24
007468FC  83 E0 01                        and eax, 1
007468FF  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00746903  48 8B 0D 3E 02 88 00            mov rcx, qword ptr [rip + 0x88023e]
0074690A  48 C1 E9 21                     shr rcx, 0x21
0074690E  83 E1 02                        and ecx, 2
00746911  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746915  83 E0 FD                        and eax, 0xfffffffd
00746918  0B C8                           or ecx, eax
0074691A  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0074691E  48 8B 0D 23 02 88 00            mov rcx, qword ptr [rip + 0x880223]
00746925  48 C1 E9 21                     shr rcx, 0x21
00746929  83 E1 04                        and ecx, 4
0074692C  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746930  83 E0 FB                        and eax, 0xfffffffb
00746933  0B C8                           or ecx, eax
00746935  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00746939  48 8B 05 08 02 88 00            mov rax, qword ptr [rip + 0x880208]
00746940  A8 10                           test al, 0x10
00746942  75 0B                           jne 0x14074694f
00746944  48 8B 05 FD 01 88 00            mov rax, qword ptr [rip + 0x8801fd]
0074694B  A8 40                           test al, 0x40
0074694D  74 05                           je 0x140746954
0074694F  44 09 4C 24 78                  or dword ptr [rsp + 0x78], r9d
00746954  48 8B 05 ED 01 88 00            mov rax, qword ptr [rip + 0x8801ed]
0074695B  A8 04                           test al, 4
0074695D  74 05                           je 0x140746964
0074695F  83 4C 24 78 10                  or dword ptr [rsp + 0x78], 0x10
00746964  48 8B 05 DD 01 88 00            mov rax, qword ptr [rip + 0x8801dd]
0074696B  49 BE 00 00 00 00 20 00 00 00   movabs r14, 0x2000000000
00746975  48 0F BA E0 24                  bt rax, 0x24
0074697A  73 12                           jae 0x14074698e
0074697C  48 8B 05 C5 01 88 00            mov rax, qword ptr [rip + 0x8801c5]
00746983  49 85 C6                        test r14, rax
00746986  74 06                           je 0x14074698e
00746988  0F BA 6C 24 78 0D               bts dword ptr [rsp + 0x78], 0xd
0074698E  48 8B 05 B3 01 88 00            mov rax, qword ptr [rip + 0x8801b3]
00746995  48 8D 0C 00                     lea rcx, [rax + rax]
00746999  83 E1 20                        and ecx, 0x20
0074699C  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
007469A0  83 E0 DF                        and eax, 0xffffffdf
007469A3  0B C8                           or ecx, eax
007469A5  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
007469A9  48 8B 0D 98 01 88 00            mov rcx, qword ptr [rip + 0x880198]
007469B0  83 E1 40                        and ecx, 0x40
007469B3  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
007469B7  83 E0 BF                        and eax, 0xffffffbf
007469BA  0B C8                           or ecx, eax
007469BC  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
007469C0  48 8B 05 81 01 88 00            mov rax, qword ptr [rip + 0x880181]
007469C7  48 8D 0C 85 00 00 00 00         lea rcx, [rax*4]
007469CF  41 B8 80 00 00 00               mov r8d, 0x80
007469D5  41 23 C8                        and ecx, r8d
007469D8  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
007469DC  0F BA F0 07                     btr eax, 7
007469E0  0B C8                           or ecx, eax
007469E2  0F BA E9 08                     bts ecx, 8
007469E6  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
007469EA  48 8B 05 57 01 88 00            mov rax, qword ptr [rip + 0x880157]
007469F1  48 8D 0C 85 00 00 00 00         lea rcx, [rax*4]
007469F9  81 E1 00 02 00 00               and ecx, 0x200
007469FF  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746A03  0F BA F0 09                     btr eax, 9
00746A07  0B C8                           or ecx, eax
00746A09  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00746A0D  48 8B 0D 34 01 88 00            mov rcx, qword ptr [rip + 0x880134]
00746A14  48 C1 E9 1C                     shr rcx, 0x1c
00746A18  81 E1 00 04 00 00               and ecx, 0x400
00746A1E  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746A22  0F BA F0 0A                     btr eax, 0xa
00746A26  0B C8                           or ecx, eax
00746A28  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00746A2C  48 8B 0D 15 01 88 00            mov rcx, qword ptr [rip + 0x880115]
00746A33  48 C1 E9 1C                     shr rcx, 0x1c
00746A37  81 E1 00 08 00 00               and ecx, 0x800
00746A3D  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746A41  0F BA F0 0B                     btr eax, 0xb
00746A45  0B C8                           or ecx, eax
00746A47  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00746A4B  48 8B 0D F6 00 88 00            mov rcx, qword ptr [rip + 0x8800f6]
00746A52  48 C1 E1 04                     shl rcx, 4
00746A56  F7 D1                           not ecx
00746A58  81 E1 00 10 00 00               and ecx, 0x1000
00746A5E  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746A62  0F BA F0 0C                     btr eax, 0xc
00746A66  0B C8                           or ecx, eax
00746A68  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00746A6C  48 8B 15 D5 00 88 00            mov rdx, qword ptr [rip + 0x8800d5]
00746A73  E8 40 25 D6 FF                  call 0x1404a8fb8
00746A78  0F B6 C8                        movzx ecx, al
00746A7B  48 C1 EA 1B                     shr rdx, 0x1b
00746A7F  81 E2 00 40 00 00               and edx, 0x4000
00746A85  83 E1 01                        and ecx, 1
00746A88  C1 E1 0F                        shl ecx, 0xf
00746A8B  0B D1                           or edx, ecx
00746A8D  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746A91  25 FF 3F FF FF                  and eax, 0xffff3fff
00746A96  0B D0                           or edx, eax
00746A98  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
00746A9C  48 8B 1D A5 00 88 00            mov rbx, qword ptr [rip + 0x8800a5]
00746AA3  83 E3 01                        and ebx, 1
00746AA6  41 0B D8                        or ebx, r8d
00746AA9  C1 E3 10                        shl ebx, 0x10
00746AAC  48 8B 3D AD 00 88 00            mov rdi, qword ptr [rip + 0x8800ad]
00746AB3  48 8B C7                        mov rax, rdi
00746AB6  48 C1 E0 13                     shl rax, 0x13
00746ABA  25 00 00 00 01                  and eax, 0x1000000
00746ABF  0B D8                           or ebx, eax
00746AC1  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00746AC5  25 FF FF FE FE                  and eax, 0xfefeffff
00746ACA  0B D8                           or ebx, eax
00746ACC  8A 05 6E AD AB 00               mov al, byte ptr [rip + 0xabad6e]
00746AD2  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00746AD6  84 C0                           test al, al
00746AD8  74 0A                           je 0x140746ae4
00746ADA  41 84 F9                        test r9b, dil
00746ADD  B8 00 00 00 26                  mov eax, 0x26000000
00746AE2  75 05                           jne 0x140746ae9
00746AE4  B8 00 00 00 24                  mov eax, 0x24000000
00746AE9  0F BA F3 19                     btr ebx, 0x19
00746AED  0B D8                           or ebx, eax
00746AEF  4C 8B FF                        mov r15, rdi
00746AF2  41 81 E7 00 80 00 00            and r15d, 0x8000
00746AF9  74 09                           je 0x140746b04
00746AFB  83 3D CE 02 88 00 00            cmp dword ptr [rip + 0x8802ce], 0
00746B02  75 44                           jne 0x140746b48
00746B04  83 3D 71 03 88 00 00            cmp dword ptr [rip + 0x880371], 0
00746B0B  74 3B                           je 0x140746b48
00746B0D  48 0F BA E7 10                  bt rdi, 0x10
00746B12  72 13                           jb 0x140746b27
00746B14  40 8A C7                        mov al, dil
00746B17  24 28                           and al, 0x28
00746B19  41 3A C1                        cmp al, r9b
00746B1C  75 13                           jne 0x140746b31
00746B1E  E8 85 C1 D6 FF                  call 0x1404b2ca8
00746B23  85 C0                           test eax, eax
00746B25  74 0A                           je 0x140746b31
00746B27  0F BA F3 1B                     btr ebx, 0x1b
00746B2B  0F BA EB 1C                     bts ebx, 0x1c
00746B2F  EB 1D                           jmp 0x140746b4e
00746B31  4D 85 FF                        test r15, r15
00746B34  74 0A                           je 0x140746b40
00746B36  0F BA F3 1C                     btr ebx, 0x1c
00746B3A  0F BA EB 1B                     bts ebx, 0x1b
00746B3E  EB 0E                           jmp 0x140746b4e
00746B40  81 E3 FF FF FF E7               and ebx, 0xe7ffffff
00746B46  EB 06                           jmp 0x140746b4e
00746B48  81 CB 00 00 00 18               or ebx, 0x18000000
00746B4E  48 0F BA E7 10                  bt rdi, 0x10
00746B53  72 0D                           jb 0x140746b62
00746B55  83 3D 8C 04 88 00 00            cmp dword ptr [rip + 0x88048c], 0
00746B5C  74 04                           je 0x140746b62
00746B5E  33 C0                           xor eax, eax
00746B60  EB 05                           jmp 0x140746b67
00746B62  B8 00 00 00 40                  mov eax, 0x40000000
00746B67  0F BA F3 1E                     btr ebx, 0x1e
00746B6B  0B D8                           or ebx, eax
00746B6D  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00746B71  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00746B76  E8 B9 E7 D6 FF                  call 0x1404b5334
00746B7B  48 C1 EF 13                     shr rdi, 0x13
00746B7F  83 E7 07                        and edi, 7
00746B82  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746B86  83 E0 F8                        and eax, 0xfffffff8
00746B89  0B F8                           or edi, eax
00746B8B  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
00746B90  74 0E                           je 0x140746ba0
00746B92  E8 CD 0C F6 FF                  call 0x1406a7864
00746B97  85 C0                           test eax, eax
00746B99  B8 18 04 00 00                  mov eax, 0x418
00746B9E  75 05                           jne 0x140746ba5
00746BA0  B8 10 04 00 00                  mov eax, 0x410
00746BA5  83 E7 F7                        and edi, 0xfffffff7
00746BA8  0B F8                           or edi, eax
00746BAA  89 7C 24 7C                     mov dword ptr [rsp + 0x7c], edi
00746BAE  48 8B 05 93 FF 87 00            mov rax, qword ptr [rip + 0x87ff93]
00746BB5  41 B9 00 80 00 00               mov r9d, 0x8000
00746BBB  49 B8 00 00 00 00 04 00 00 00   movabs r8, 0x400000000
00746BC5  49 85 C1                        test r9, rax
00746BC8  75 0E                           jne 0x140746bd8
00746BCA  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746BCE  0F BA F0 08                     btr eax, 8
00746BD2  0F BA E8 09                     bts eax, 9
00746BD6  EB 6A                           jmp 0x140746c42
00746BD8  48 8B 05 69 FF 87 00            mov rax, qword ptr [rip + 0x87ff69]
00746BDF  49 85 C0                        test r8, rax
00746BE2  75 52                           jne 0x140746c36
00746BE4  48 8B 05 5D FF 87 00            mov rax, qword ptr [rip + 0x87ff5d]
00746BEB  49 85 C6                        test r14, rax
00746BEE  75 46                           jne 0x140746c36
00746BF0  48 8B 05 51 FF 87 00            mov rax, qword ptr [rip + 0x87ff51]
00746BF7  48 0F BA E0 2C                  bt rax, 0x2c
00746BFC  72 38                           jb 0x140746c36
00746BFE  48 8B 05 43 FF 87 00            mov rax, qword ptr [rip + 0x87ff43]
00746C05  48 BA 00 00 00 00 08 00 00 00   movabs rdx, 0x800000000
00746C0F  48 85 C2                        test rdx, rax
00746C12  75 18                           jne 0x140746c2c
00746C14  48 8B 05 2D FF 87 00            mov rax, qword ptr [rip + 0x87ff2d]
00746C1B  48 0F BA E0 2D                  bt rax, 0x2d
00746C20  72 0A                           jb 0x140746c2c
00746C22  81 4C 24 7C 00 03 00 00         or dword ptr [rsp + 0x7c], 0x300
00746C2A  EB 24                           jmp 0x140746c50
00746C2C  81 64 24 7C FF FC FF FF         and dword ptr [rsp + 0x7c], 0xfffffcff
00746C34  EB 1A                           jmp 0x140746c50
00746C36  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746C3A  0F BA F0 09                     btr eax, 9
00746C3E  0F BA E8 08                     bts eax, 8
00746C42  48 BA 00 00 00 00 08 00 00 00   movabs rdx, 0x800000000
00746C4C  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00746C50  48 8B 05 F1 FE 87 00            mov rax, qword ptr [rip + 0x87fef1]
00746C57  48 0F BA E0 10                  bt rax, 0x10
00746C5C  73 64                           jae 0x140746cc2
00746C5E  48 8B 05 E3 FE 87 00            mov rax, qword ptr [rip + 0x87fee3]
00746C65  48 0F BA E0 34                  bt rax, 0x34
00746C6A  72 51                           jb 0x140746cbd
00746C6C  48 8B 05 D5 FE 87 00            mov rax, qword ptr [rip + 0x87fed5]
00746C73  49 85 C0                        test r8, rax
00746C76  75 45                           jne 0x140746cbd
00746C78  48 8B 05 C9 FE 87 00            mov rax, qword ptr [rip + 0x87fec9]
00746C7F  48 0F BA E0 35                  bt rax, 0x35
00746C84  72 2F                           jb 0x140746cb5
00746C86  48 8B 05 BB FE 87 00            mov rax, qword ptr [rip + 0x87febb]
00746C8D  48 85 C2                        test rdx, rax
00746C90  75 23                           jne 0x140746cb5
00746C92  48 8B 05 AF FE 87 00            mov rax, qword ptr [rip + 0x87feaf]
00746C99  48 0F BA E0 36                  bt rax, 0x36
00746C9E  72 0E                           jb 0x140746cae
00746CA0  48 8B 05 A1 FE 87 00            mov rax, qword ptr [rip + 0x87fea1]
00746CA7  48 0F BA E0 37                  bt rax, 0x37
00746CAC  73 14                           jae 0x140746cc2
00746CAE  83 4C 24 7C 20                  or dword ptr [rsp + 0x7c], 0x20
00746CB3  EB 0D                           jmp 0x140746cc2
00746CB5  0F BA 6C 24 7C 07               bts dword ptr [rsp + 0x7c], 7
00746CBB  EB 05                           jmp 0x140746cc2
00746CBD  83 4C 24 7C 40                  or dword ptr [rsp + 0x7c], 0x40
00746CC2  48 8B 0D 97 FE 87 00            mov rcx, qword ptr [rip + 0x87fe97]
00746CC9  48 C1 E1 08                     shl rcx, 8
00746CCD  81 E1 00 10 00 00               and ecx, 0x1000
00746CD3  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746CD7  0F BA F0 0C                     btr eax, 0xc
00746CDB  0B C8                           or ecx, eax
00746CDD  81 C9 00 28 00 00               or ecx, 0x2800
00746CE3  89 4C 24 7C                     mov dword ptr [rsp + 0x7c], ecx
00746CE7  48 8B 05 5A FE 87 00            mov rax, qword ptr [rip + 0x87fe5a]
00746CEE  41 BA 00 00 04 00               mov r10d, 0x40000
00746CF4  49 85 C2                        test r10, rax
00746CF7  75 0E                           jne 0x140746d07
00746CF9  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746CFD  25 FF BF FE FF                  and eax, 0xfffebfff
00746D02  41 0B C1                        or eax, r9d
00746D05  EB 5C                           jmp 0x140746d63
00746D07  48 8B 05 3A FE 87 00            mov rax, qword ptr [rip + 0x87fe3a]
00746D0E  48 0F BA E0 13                  bt rax, 0x13
00746D13  72 0B                           jb 0x140746d20
00746D15  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746D19  25 FF 3F FE FF                  and eax, 0xfffe3fff
00746D1E  EB 43                           jmp 0x140746d63
00746D20  48 8B 05 21 FE 87 00            mov rax, qword ptr [rip + 0x87fe21]
00746D27  48 0F BA E0 14                  bt rax, 0x14
00746D2C  73 0F                           jae 0x140746d3d
00746D2E  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746D32  25 FF 3F FF FF                  and eax, 0xffff3fff
00746D37  0F BA E8 10                     bts eax, 0x10
00746D3B  EB 26                           jmp 0x140746d63
00746D3D  48 8B 05 04 FE 87 00            mov rax, qword ptr [rip + 0x87fe04]
00746D44  48 0F BA E0 2E                  bt rax, 0x2e
00746D49  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746D4D  73 0B                           jae 0x140746d5a
00746D4F  25 FF 7F FE FF                  and eax, 0xfffe7fff
00746D54  0F BA E8 0E                     bts eax, 0xe
00746D58  EB 09                           jmp 0x140746d63
00746D5A  0F BA F0 10                     btr eax, 0x10
00746D5E  0D 00 C0 00 00                  or eax, 0xc000
00746D63  0F BA E8 11                     bts eax, 0x11
00746D67  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00746D6B  48 8B 05 D6 FD 87 00            mov rax, qword ptr [rip + 0x87fdd6]
00746D72  41 B9 00 00 20 00               mov r9d, 0x200000
00746D78  49 85 C1                        test r9, rax
00746D7B  75 0E                           jne 0x140746d8b
00746D7D  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746D81  0F BA F0 12                     btr eax, 0x12
00746D85  0F BA E8 13                     bts eax, 0x13
00746D89  EB 61                           jmp 0x140746dec
00746D8B  48 8B 05 B6 FD 87 00            mov rax, qword ptr [rip + 0x87fdb6]
00746D92  49 85 C0                        test r8, rax
00746D95  75 4A                           jne 0x140746de1
00746D97  48 8B 05 AA FD 87 00            mov rax, qword ptr [rip + 0x87fdaa]
00746D9E  49 85 C6                        test r14, rax
00746DA1  75 3E                           jne 0x140746de1
00746DA3  48 8B 05 9E FD 87 00            mov rax, qword ptr [rip + 0x87fd9e]
00746DAA  48 0F BA E0 2F                  bt rax, 0x2f
00746DAF  72 30                           jb 0x140746de1
00746DB1  48 8B 05 90 FD 87 00            mov rax, qword ptr [rip + 0x87fd90]
00746DB8  48 85 C2                        test rdx, rax
00746DBB  75 19                           jne 0x140746dd6
00746DBD  48 8B 05 84 FD 87 00            mov rax, qword ptr [rip + 0x87fd84]
00746DC4  48 0F BA E0 30                  bt rax, 0x30
00746DC9  72 0B                           jb 0x140746dd6
00746DCB  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746DCF  0D 00 00 0C 00                  or eax, 0xc0000
00746DD4  EB 16                           jmp 0x140746dec
00746DD6  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746DDA  25 FF FF F3 FF                  and eax, 0xfff3ffff
00746DDF  EB 0B                           jmp 0x140746dec
00746DE1  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746DE5  0F BA F0 13                     btr eax, 0x13
00746DE9  41 0B C2                        or eax, r10d
00746DEC  0F BA E8 14                     bts eax, 0x14
00746DF0  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00746DF4  48 8B 05 4D FD 87 00            mov rax, qword ptr [rip + 0x87fd4d]
00746DFB  B9 00 00 40 00                  mov ecx, 0x400000
00746E00  48 85 C1                        test rcx, rax
00746E03  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746E07  75 06                           jne 0x140746e0f
00746E09  0F BA F0 15                     btr eax, 0x15
00746E0D  EB 03                           jmp 0x140746e12
00746E0F  41 0B C1                        or eax, r9d
00746E12  0B C1                           or eax, ecx
00746E14  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00746E18  48 8B 05 29 FD 87 00            mov rax, qword ptr [rip + 0x87fd29]
00746E1F  41 B9 00 00 80 00               mov r9d, 0x800000
00746E25  49 85 C1                        test r9, rax
00746E28  75 0E                           jne 0x140746e38
00746E2A  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746E2E  0F BA F0 17                     btr eax, 0x17
00746E32  0F BA E8 18                     bts eax, 0x18
00746E36  EB 39                           jmp 0x140746e71
00746E38  48 8B 05 09 FD 87 00            mov rax, qword ptr [rip + 0x87fd09]
00746E3F  48 0F BA E0 31                  bt rax, 0x31
00746E44  73 0D                           jae 0x140746e53
00746E46  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746E4A  0F BA F0 18                     btr eax, 0x18
00746E4E  41 0B C1                        or eax, r9d
00746E51  EB 1E                           jmp 0x140746e71
00746E53  48 8B 05 EE FC 87 00            mov rax, qword ptr [rip + 0x87fcee]
00746E5A  48 0F BA E0 32                  bt rax, 0x32
00746E5F  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746E63  73 07                           jae 0x140746e6c
00746E65  25 FF FF 7F FE                  and eax, 0xfe7fffff
00746E6A  EB 05                           jmp 0x140746e71
00746E6C  0D 00 00 80 01                  or eax, 0x1800000
00746E71  0F BA E8 19                     bts eax, 0x19
00746E75  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00746E79  48 8B 05 C8 FC 87 00            mov rax, qword ptr [rip + 0x87fcc8]
00746E80  48 0F BA E0 1B                  bt rax, 0x1b
00746E85  72 0E                           jb 0x140746e95
00746E87  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746E8B  0F BA F0 1A                     btr eax, 0x1a
00746E8F  0F BA E8 1B                     bts eax, 0x1b
00746E93  EB 60                           jmp 0x140746ef5
00746E95  48 8B 05 AC FC 87 00            mov rax, qword ptr [rip + 0x87fcac]
00746E9C  49 85 C0                        test r8, rax
00746E9F  75 48                           jne 0x140746ee9
00746EA1  48 8B 05 A0 FC 87 00            mov rax, qword ptr [rip + 0x87fca0]
00746EA8  49 85 C6                        test r14, rax
00746EAB  75 3C                           jne 0x140746ee9
00746EAD  48 8B 05 94 FC 87 00            mov rax, qword ptr [rip + 0x87fc94]
00746EB4  48 0F BA E0 39                  bt rax, 0x39
00746EB9  72 2E                           jb 0x140746ee9
00746EBB  48 8B 05 86 FC 87 00            mov rax, qword ptr [rip + 0x87fc86]
00746EC2  48 85 C2                        test rdx, rax
00746EC5  75 18                           jne 0x140746edf
00746EC7  48 8B 05 7A FC 87 00            mov rax, qword ptr [rip + 0x87fc7a]
00746ECE  48 0F BA E0 3A                  bt rax, 0x3a
00746ED3  72 0A                           jb 0x140746edf
00746ED5  81 4C 24 7C 00 00 00 0C         or dword ptr [rsp + 0x7c], 0xc000000
00746EDD  EB 1A                           jmp 0x140746ef9
00746EDF  81 64 24 7C FF FF FF F3         and dword ptr [rsp + 0x7c], 0xf3ffffff
00746EE7  EB 10                           jmp 0x140746ef9
00746EE9  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00746EED  0F BA F0 1B                     btr eax, 0x1b
00746EF1  0F BA E8 1A                     bts eax, 0x1a
00746EF5  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00746EF9  4D 8B C4                        mov r8, r12
00746EFC  33 D2                           xor edx, edx
00746EFE  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00746F03  E8 38 FD F7 FF                  call 0x1406c6c40
00746F08  45 8B C5                        mov r8d, r13d
00746F0B  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00746F10  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00746F15  E8 26 F9 F7 FF                  call 0x1406c6840
00746F1A  90                              nop
00746F1B  33 C0                           xor eax, eax
00746F1D  EB 00                           jmp 0x140746f1f
00746F1F  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00746F24  48 83 C4 30                     add rsp, 0x30
00746F28  41 5F                           pop r15
00746F2A  41 5E                           pop r14
00746F2C  41 5D                           pop r13
00746F2E  41 5C                           pop r12
00746F30  5F                              pop rdi
00746F31  C3                              ret
00746F32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQuerySpeculationControlInformation(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (48);
    if (a2 >= 4) goto loc_007468D8;
    *(unsigned int *)(a3) = 8;
    goto loc_00746F1F;
loc_007468D8:
    v_r13 = (unsigned int)((unsigned int)((unsigned int)(a2)));
    if (((unsigned int)((unsigned int)(a2))) >= 8) { v_r13 = 8; }
    *(unsigned int *)(a3) = (unsigned int)(v_r13);
    result = (*(unsigned __int64 *)(v_rip + 8913488)) >> (36);
    result = (unsigned int)((result) & (1));
    v_stack_p20 = (unsigned int)(result);
    a1 = (*(unsigned __int64 *)(v_rip + 8913470)) >> (33);
    a1 = (unsigned int)((a1) & (2));
    result = (unsigned int)(((unsigned int)(v_stack_p20)) & (0xFFFFFFFDULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (*(unsigned __int64 *)(v_rip + 8913443)) >> (33);
    a1 = (unsigned int)((a1) & (4));
    result = (unsigned int)(((unsigned int)(v_stack_p20)) & (0xFFFFFFFBULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_p20 = (unsigned int)(a1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8913416))) & (16)) != 0) goto loc_0074694F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8913405))) & (64)) != 0) {
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8913389))) & (4)) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_0074698E;
    if (((v_r14) & (*(unsigned __int64 *)(v_rip + 8913349))) != 0) {
    }
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip + 8913331) + *(unsigned __int64 *)(v_rip + 8913331) * 1) & (32));
    result = (unsigned int)(((unsigned int)(v_stack_p20)) & (0xFFFFFFDFULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip + 8913304)) & (64));
    result = (unsigned int)(((unsigned int)(v_stack_p20)) & (0xFFFFFFBFULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip + 8913281) * 4) & (128));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p20))));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip + 8913239) * 4) & (512));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p20))));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (*(unsigned __int64 *)(v_rip + 8913204)) >> (28);
    a1 = (unsigned int)((a1) & (0x400ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p20))));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (*(unsigned __int64 *)(v_rip + 8913173)) >> (28);
    a1 = (unsigned int)((a1) & (0x800ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p20))));
    v_stack_p20 = (unsigned int)(a1);
    a1 = (*(unsigned __int64 *)(v_rip + 8913142)) << (4);
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & (0x1000ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p20))));
    v_stack_p20 = (unsigned int)(a1);
    result = KeIsImportOptimizationEnabled(a1, *(unsigned __int64 *)(v_rip + 8913109), 128, 8);
    a2 = (*(unsigned __int64 *)(v_rip + 8913109)) >> (27);
    a2 = (unsigned int)((a2) & (0x4000ULL));
    a1 = (unsigned int)(((unsigned __int8)(result)) & (1));
    a1 = (unsigned int)((a1) << (15));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)(v_stack_p20)) & (0xFFFF3FFFULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    v_stack_p20 = a2;
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_rip + 8913061)) & (1));
    v_rbx = (unsigned int)((v_rbx) | (128));
    v_rbx = (unsigned int)((v_rbx) << (16));
    result = (*(unsigned __int64 *)(v_rip + 8913069)) << (19);
    result = (unsigned int)((result) & (0x1000000ULL));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)(v_stack_p20)) & (0xFEFEFFFFULL));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    v_stack_p10 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 11251054));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11251054)) == 0) goto loc_00746AE4;
    result = (unsigned int)(0x26000000ULL);
    if (((8) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8913069)))) == 0) {
        result = 0x24000000ULL;
    }
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    v_r15 = (unsigned int)((*(unsigned __int64 *)(v_rip + 8913069)) & (0x8000ULL));
    if (condition_is_equal) goto loc_00746B04;
    if ((*(unsigned int *)(v_rip + 8913614)) != 0) goto loc_00746B48;
loc_00746B04:
    if ((*(unsigned int *)(v_rip + 8913777)) == 0) goto loc_00746B48;
    if ((*(unsigned int *)(v_rip + 8913777)) < 0) goto loc_00746B27;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8913069))) & (40));
    if (((unsigned __int8)(result)) != 8) goto loc_00746B31;
    result = KeKvaShadowingActive(a1, a2, 128, 8);
    if ((unsigned int)(result) == 0) goto loc_00746B31;
loc_00746B27:
    goto loc_00746B4E;
loc_00746B31:
    if (v_r15 == 0) goto loc_00746B40;
    goto loc_00746B4E;
loc_00746B40:
    v_rbx = (unsigned int)((v_rbx) & (0xE7FFFFFFULL));
    goto loc_00746B4E;
loc_00746B48:
    v_rbx = (unsigned int)((v_rbx) | (0x18000000ULL));
loc_00746B4E:
    if (condition_is_below) goto loc_00746B62;
    if ((*(unsigned int *)(v_rip + 8914060)) == 0) goto loc_00746B62;
    result = 0;
    goto loc_00746B67;
loc_00746B62:
loc_00746B67:
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    v_stack_p20 = (unsigned int)(v_rbx);
    result = HvlQueryL1tfMitigationInformation(v_stack_p20, a2, 128, 8);
    v_rdi = (*(unsigned __int64 *)(v_rip + 8913069)) >> (19);
    v_rdi = (unsigned int)((v_rdi) & (7));
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFFFFFFF8ULL));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    if (v_stack_p10 == 0) goto loc_00746BA0;
    result = SpcIsFbClearSupported(v_stack_p20, a2, 128, 8);
    result = (unsigned int)(0x418ULL);
    if ((unsigned int)(result) == 0) {
        result = 0x410ULL;
    }
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFF7ULL));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_stack_p24 = (unsigned int)(v_rdi);
    if ((((unsigned int)(0x8000ULL)) & (*(unsigned __int64 *)(v_rip + 8912787))) != 0) goto loc_00746BD8;
    goto loc_00746C42;
loc_00746BD8:
    if (((128) & (*(unsigned __int64 *)(v_rip + 8912745))) != 0) goto loc_00746C36;
    if (((v_r14) & (*(unsigned __int64 *)(v_rip + 8912733))) != 0) goto loc_00746C36;
    if (condition_is_below) goto loc_00746C36;
    if (((a2) & (*(unsigned __int64 *)(v_rip + 8912707))) != 0) goto loc_00746C2C;
    if (condition_is_below) goto loc_00746C2C;
    goto loc_00746C50;
loc_00746C2C:
    goto loc_00746C50;
loc_00746C36:
loc_00746C42:
    v_stack_p24 = (unsigned int)((unsigned int)(v_stack_p24));
loc_00746C50:
    if (condition_is_above_or_equal) goto loc_00746CC2;
    if (condition_is_below) goto loc_00746CBD;
    if (((128) & (*(unsigned __int64 *)(v_rip + 8912597))) != 0) goto loc_00746CBD;
    if (condition_is_below) goto loc_00746CB5;
    if (((a2) & (*(unsigned __int64 *)(v_rip + 8912571))) != 0) goto loc_00746CB5;
    if (condition_is_below) goto loc_00746CAE;
    if (condition_is_above_or_equal) goto loc_00746CC2;
loc_00746CAE:
    goto loc_00746CC2;
loc_00746CB5:
    goto loc_00746CC2;
loc_00746CBD:
loc_00746CC2:
    a1 = (*(unsigned __int64 *)(v_rip + 8912535)) << (8);
    a1 = (unsigned int)((a1) & (0x1000ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p24))));
    a1 = (unsigned int)((a1) | (0x2800ULL));
    v_stack_p24 = (unsigned int)(a1);
    if ((((unsigned int)(0x40000ULL)) & (*(unsigned __int64 *)(v_rip + 8912474))) != 0) goto loc_00746D07;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFFFEBFFFULL));
    result = (unsigned int)((result) | ((unsigned int)((unsigned int)(0x8000ULL))));
    goto loc_00746D63;
loc_00746D07:
    if (condition_is_below) goto loc_00746D20;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFFFE3FFFULL));
    goto loc_00746D63;
loc_00746D20:
    if (condition_is_above_or_equal) goto loc_00746D3D;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFFFF3FFFULL));
    goto loc_00746D63;
loc_00746D3D:
    if (condition_is_above_or_equal) goto loc_00746D5A;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFFFE7FFFULL));
    goto loc_00746D63;
loc_00746D5A:
    result = (unsigned int)((result) | (0xC000ULL));
loc_00746D63:
    v_stack_p24 = (unsigned int)(result);
    if ((((unsigned int)(0x200000ULL)) & (*(unsigned __int64 *)(v_rip + 8912342))) != 0) goto loc_00746D8B;
    goto loc_00746DEC;
loc_00746D8B:
    if (((128) & (*(unsigned __int64 *)(v_rip + 8912310))) != 0) goto loc_00746DE1;
    if (((v_r14) & (*(unsigned __int64 *)(v_rip + 8912298))) != 0) goto loc_00746DE1;
    if (condition_is_below) goto loc_00746DE1;
    if (((a2) & (*(unsigned __int64 *)(v_rip + 8912272))) != 0) goto loc_00746DD6;
    if (condition_is_below) goto loc_00746DD6;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) | (0xC0000ULL));
    goto loc_00746DEC;
loc_00746DD6:
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFFF3FFFFULL));
    goto loc_00746DEC;
loc_00746DE1:
    result = (unsigned int)(((unsigned int)(v_stack_p24)) | ((unsigned int)((unsigned int)(0x40000ULL))));
loc_00746DEC:
    v_stack_p24 = (unsigned int)(result);
    if ((((unsigned int)(0x400000ULL)) & (*(unsigned __int64 *)(v_rip + 8912205))) != 0) goto loc_00746E0F;
    goto loc_00746E12;
loc_00746E0F:
    result = (unsigned int)(((unsigned int)(v_stack_p24)) | ((unsigned int)((unsigned int)(0x200000ULL))));
loc_00746E12:
    result = (unsigned int)((result) | ((unsigned int)((unsigned int)(0x400000ULL))));
    v_stack_p24 = (unsigned int)(result);
    if ((((unsigned int)(0x800000ULL)) & (*(unsigned __int64 *)(v_rip + 8912169))) != 0) goto loc_00746E38;
    goto loc_00746E71;
loc_00746E38:
    if (condition_is_above_or_equal) goto loc_00746E53;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) | ((unsigned int)((unsigned int)(0x800000ULL))));
    goto loc_00746E71;
loc_00746E53:
    if (condition_is_above_or_equal) goto loc_00746E6C;
    result = (unsigned int)(((unsigned int)(v_stack_p24)) & (0xFE7FFFFFULL));
    goto loc_00746E71;
loc_00746E6C:
    result = (unsigned int)((result) | (0x1800000ULL));
loc_00746E71:
    v_stack_p24 = (unsigned int)(result);
    if (condition_is_below) goto loc_00746E95;
    goto loc_00746EF5;
loc_00746E95:
    if (((128) & (*(unsigned __int64 *)(v_rip + 8912044))) != 0) goto loc_00746EE9;
    if (((v_r14) & (*(unsigned __int64 *)(v_rip + 8912032))) != 0) goto loc_00746EE9;
    if (condition_is_below) goto loc_00746EE9;
    if (((a2) & (*(unsigned __int64 *)(v_rip + 8912006))) != 0) goto loc_00746EDF;
    if (condition_is_below) goto loc_00746EDF;
    goto loc_00746EF9;
loc_00746EDF:
    goto loc_00746EF9;
loc_00746EE9:
loc_00746EF5:
    v_stack_p24 = (unsigned int)((unsigned int)(v_stack_p24));
loc_00746EF9:
    a2 = 0;
    result = memset(v_stack_p8, a2, (unsigned int)(a2), (unsigned int)(0x800000ULL));
    result = memcpy(v_stack_p8, v_stack_p20, (unsigned int)((unsigned int)(v_r13)), (unsigned int)(0x800000ULL));
    result = 0;
    goto loc_00746F1F;
loc_00746F1F:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeQuerySpeculationControlInformation(int64_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (48);
    if (Arg2 >= 4) goto loc_007468D8;
    *(uint32_t *)(arg3) = 8;
    goto loc_00746F1F;
loc_007468D8:
    local_r13 = (uint32_t)((uint32_t)((uint32_t)(Arg2)));
    if (((uint32_t)((uint32_t)(Arg2))) >= 8) { local_r13 = 8; }
    *(uint32_t *)(arg3) = (uint32_t)(local_r13);
    result = (*(uint64_t *)(v_rip + 0x880250)) >> (36);
    result = (uint32_t)((result) & (1));
    v_stack_p20 = (uint32_t)(result);
    Arg1 = (*(uint64_t *)(v_rip + 0x88023E)) >> (33);
    Arg1 = (uint32_t)((Arg1) & (2));
    result = (uint32_t)(((uint32_t)(v_stack_p20)) & (0xFFFFFFFDULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (*(uint64_t *)(v_rip + 0x880223)) >> (33);
    Arg1 = (uint32_t)((Arg1) & (4));
    result = (uint32_t)(((uint32_t)(v_stack_p20)) & (0xFFFFFFFBULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_p20 = (uint32_t)(Arg1);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x880208))) & (16)) != 0) goto loc_0074694F;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x8801FD))) & (64)) != 0) {
    }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x8801ED))) & (4)) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_0074698E;
    if (((local_r14) & (*(uint64_t *)(v_rip + 0x8801C5))) != 0) {
    }
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip + 0x8801B3) + *(uint64_t *)(v_rip + 0x8801B3) * 1) & (32));
    result = (uint32_t)(((uint32_t)(v_stack_p20)) & (0xFFFFFFDFULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip + 0x880198)) & (64));
    result = (uint32_t)(((uint32_t)(v_stack_p20)) & (0xFFFFFFBFULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip + 0x880181) * 4) & (128));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p20))));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip + 0x880157) * 4) & (512));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p20))));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (*(uint64_t *)(v_rip + 0x880134)) >> (28);
    Arg1 = (uint32_t)((Arg1) & (0x400ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p20))));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (*(uint64_t *)(v_rip + 0x880115)) >> (28);
    Arg1 = (uint32_t)((Arg1) & (0x800ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p20))));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = (*(uint64_t *)(v_rip + 0x8800F6)) << (4);
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & (0x1000ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p20))));
    v_stack_p20 = (uint32_t)(Arg1);
    result = KeIsImportOptimizationEnabled(Arg1, *(uint64_t *)(v_rip + 0x8800D5), 128, 8);
    Arg2 = (*(uint64_t *)(v_rip + 0x8800D5)) >> (27);
    Arg2 = (uint32_t)((Arg2) & (0x4000ULL));
    Arg1 = (uint32_t)(((uint8_t)(result)) & (1));
    Arg1 = (uint32_t)((Arg1) << (15));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)(v_stack_p20)) & (0xFFFF3FFFULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    v_stack_p20 = Arg2;
    local_rbx = (uint32_t)((*(uint64_t *)(v_rip + 0x8800A5)) & (1));
    local_rbx = (uint32_t)((local_rbx) | (128));
    local_rbx = (uint32_t)((local_rbx) << (16));
    result = (*(uint64_t *)(v_rip + 0x8800AD)) << (19);
    result = (uint32_t)((result) & (0x1000000ULL));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)(v_stack_p20)) & (0xFEFEFFFFULL));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    v_stack_p10 = (uint8_t)(*(uint8_t *)(v_rip + 0xABAD6E));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xABAD6E)) == 0) goto loc_00746AE4;
    result = (uint32_t)(0x26000000ULL);
    if (((8) & ((uint8_t)(*(uint64_t *)(v_rip + 0x8800AD)))) == 0) {
        result = 0x24000000ULL;
    }
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    local_r15 = (uint32_t)((*(uint64_t *)(v_rip + 0x8800AD)) & (0x8000ULL));
    if (condition_is_equal) goto loc_00746B04;
    if ((*(uint32_t *)(v_rip + 0x8802CE)) != 0) goto loc_00746B48;
loc_00746B04:
    if ((*(uint32_t *)(v_rip + 0x880371)) == 0) goto loc_00746B48;
    if ((*(uint32_t *)(v_rip + 0x880371)) < 0) goto loc_00746B27;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(v_rip + 0x8800AD))) & (40));
    if (((uint8_t)(result)) != 8) goto loc_00746B31;
    result = KeKvaShadowingActive(Arg1, Arg2, 128, 8);
    if ((uint32_t)(result) == 0) goto loc_00746B31;
loc_00746B27:
    goto loc_00746B4E;
loc_00746B31:
    if (local_r15 == 0) goto loc_00746B40;
    goto loc_00746B4E;
loc_00746B40:
    local_rbx = (uint32_t)((local_rbx) & (0xE7FFFFFFULL));
    goto loc_00746B4E;
loc_00746B48:
    local_rbx = (uint32_t)((local_rbx) | (0x18000000ULL));
loc_00746B4E:
    if (condition_is_below) goto loc_00746B62;
    if ((*(uint32_t *)(v_rip + 0x88048C)) == 0) goto loc_00746B62;
    result = 0;
    goto loc_00746B67;
loc_00746B62:
loc_00746B67:
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    v_stack_p20 = (uint32_t)(local_rbx);
    result = HvlQueryL1tfMitigationInformation(v_stack_p20, Arg2, 128, 8);
    local_rdi = (*(uint64_t *)(v_rip + 0x8800AD)) >> (19);
    local_rdi = (uint32_t)((local_rdi) & (7));
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFFFFFFF8ULL));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    if (v_stack_p10 == 0) goto loc_00746BA0;
    result = SpcIsFbClearSupported(v_stack_p20, Arg2, 128, 8);
    result = (uint32_t)(0x418ULL);
    if ((uint32_t)(result) == 0) {
        result = 0x410ULL;
    }
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFF7ULL));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    v_stack_p24 = (uint32_t)(local_rdi);
    if ((((uint32_t)(0x8000ULL)) & (*(uint64_t *)(v_rip + 0x87FF93))) != 0) goto loc_00746BD8;
    goto loc_00746C42;
loc_00746BD8:
    if (((128) & (*(uint64_t *)(v_rip + 0x87FF69))) != 0) goto loc_00746C36;
    if (((local_r14) & (*(uint64_t *)(v_rip + 0x87FF5D))) != 0) goto loc_00746C36;
    if (condition_is_below) goto loc_00746C36;
    if (((Arg2) & (*(uint64_t *)(v_rip + 0x87FF43))) != 0) goto loc_00746C2C;
    if (condition_is_below) goto loc_00746C2C;
    goto loc_00746C50;
loc_00746C2C:
    goto loc_00746C50;
loc_00746C36:
loc_00746C42:
    v_stack_p24 = (uint32_t)((uint32_t)(v_stack_p24));
loc_00746C50:
    if (condition_is_above_or_equal) goto loc_00746CC2;
    if (condition_is_below) goto loc_00746CBD;
    if (((128) & (*(uint64_t *)(v_rip + 0x87FED5))) != 0) goto loc_00746CBD;
    if (condition_is_below) goto loc_00746CB5;
    if (((Arg2) & (*(uint64_t *)(v_rip + 0x87FEBB))) != 0) goto loc_00746CB5;
    if (condition_is_below) goto loc_00746CAE;
    if (condition_is_above_or_equal) goto loc_00746CC2;
loc_00746CAE:
    goto loc_00746CC2;
loc_00746CB5:
    goto loc_00746CC2;
loc_00746CBD:
loc_00746CC2:
    Arg1 = (*(uint64_t *)(v_rip + 0x87FE97)) << (8);
    Arg1 = (uint32_t)((Arg1) & (0x1000ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p24))));
    Arg1 = (uint32_t)((Arg1) | (0x2800ULL));
    v_stack_p24 = (uint32_t)(Arg1);
    if ((((uint32_t)(0x40000ULL)) & (*(uint64_t *)(v_rip + 0x87FE5A))) != 0) goto loc_00746D07;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFFFEBFFFULL));
    result = (uint32_t)((result) | ((uint32_t)((uint32_t)(0x8000ULL))));
    goto loc_00746D63;
loc_00746D07:
    if (condition_is_below) goto loc_00746D20;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFFFE3FFFULL));
    goto loc_00746D63;
loc_00746D20:
    if (condition_is_above_or_equal) goto loc_00746D3D;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFFFF3FFFULL));
    goto loc_00746D63;
loc_00746D3D:
    if (condition_is_above_or_equal) goto loc_00746D5A;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFFFE7FFFULL));
    goto loc_00746D63;
loc_00746D5A:
    result = (uint32_t)((result) | (0xC000ULL));
loc_00746D63:
    v_stack_p24 = (uint32_t)(result);
    if ((((uint32_t)(0x200000ULL)) & (*(uint64_t *)(v_rip + 0x87FDD6))) != 0) goto loc_00746D8B;
    goto loc_00746DEC;
loc_00746D8B:
    if (((128) & (*(uint64_t *)(v_rip + 0x87FDB6))) != 0) goto loc_00746DE1;
    if (((local_r14) & (*(uint64_t *)(v_rip + 0x87FDAA))) != 0) goto loc_00746DE1;
    if (condition_is_below) goto loc_00746DE1;
    if (((Arg2) & (*(uint64_t *)(v_rip + 0x87FD90))) != 0) goto loc_00746DD6;
    if (condition_is_below) goto loc_00746DD6;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) | (0xC0000ULL));
    goto loc_00746DEC;
loc_00746DD6:
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFFF3FFFFULL));
    goto loc_00746DEC;
loc_00746DE1:
    result = (uint32_t)(((uint32_t)(v_stack_p24)) | ((uint32_t)((uint32_t)(0x40000ULL))));
loc_00746DEC:
    v_stack_p24 = (uint32_t)(result);
    if ((((uint32_t)(0x400000ULL)) & (*(uint64_t *)(v_rip + 0x87FD4D))) != 0) goto loc_00746E0F;
    goto loc_00746E12;
loc_00746E0F:
    result = (uint32_t)(((uint32_t)(v_stack_p24)) | ((uint32_t)((uint32_t)(0x200000ULL))));
loc_00746E12:
    result = (uint32_t)((result) | ((uint32_t)((uint32_t)(0x400000ULL))));
    v_stack_p24 = (uint32_t)(result);
    if ((((uint32_t)(0x800000ULL)) & (*(uint64_t *)(v_rip + 0x87FD29))) != 0) goto loc_00746E38;
    goto loc_00746E71;
loc_00746E38:
    if (condition_is_above_or_equal) goto loc_00746E53;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) | ((uint32_t)((uint32_t)(0x800000ULL))));
    goto loc_00746E71;
loc_00746E53:
    if (condition_is_above_or_equal) goto loc_00746E6C;
    result = (uint32_t)(((uint32_t)(v_stack_p24)) & (0xFE7FFFFFULL));
    goto loc_00746E71;
loc_00746E6C:
    result = (uint32_t)((result) | (0x1800000ULL));
loc_00746E71:
    v_stack_p24 = (uint32_t)(result);
    if (condition_is_below) goto loc_00746E95;
    goto loc_00746EF5;
loc_00746E95:
    if (((128) & (*(uint64_t *)(v_rip + 0x87FCAC))) != 0) goto loc_00746EE9;
    if (((local_r14) & (*(uint64_t *)(v_rip + 0x87FCA0))) != 0) goto loc_00746EE9;
    if (condition_is_below) goto loc_00746EE9;
    if (((Arg2) & (*(uint64_t *)(v_rip + 0x87FC86))) != 0) goto loc_00746EDF;
    if (condition_is_below) goto loc_00746EDF;
    goto loc_00746EF9;
loc_00746EDF:
    goto loc_00746EF9;
loc_00746EE9:
loc_00746EF5:
    v_stack_p24 = (uint32_t)((uint32_t)(v_stack_p24));
loc_00746EF9:
    Arg2 = 0;
    result = memset(v_stack_p8, Arg2, (uint32_t)(Arg2), (uint32_t)(0x800000ULL));
    result = memcpy(v_stack_p8, v_stack_p20, (uint32_t)((uint32_t)(local_r13)), (uint32_t)(0x800000ULL));
    result = 0;
    goto loc_00746F1F;
loc_00746F1F:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007468A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
