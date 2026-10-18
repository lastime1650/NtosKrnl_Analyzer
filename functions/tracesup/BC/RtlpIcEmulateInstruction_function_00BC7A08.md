# RtlpIcEmulateInstruction

- RVA: `0x00BC7A08`–`0x00BC81F3` (길이 `2,027` bytes)
- VA: `0x0000000140BC7A08`
- 실행 섹션: `TRACESUP`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D001C`
- 디코드: `539`개 명령, `2,027/2,027` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC7A51` → [RtlpIcFetchInstructionBytes](RtlpIcFetchInstructionBytes_function_00BC8454.md) (function, `0x00BC8454`)
- `0x00BC7A75` → [RtlpIcEmulateRegisterPushPop](RtlpIcEmulateRegisterPushPop_function_00BC830C.md) (function, `0x00BC830C`)
- `0x00BC7AAA` → [RtlpIcSetImmediateOperandSize](RtlpIcSetImmediateOperandSize_function_00BC88F8.md) (function, `0x00BC88F8`)
- `0x00BC7AB9` → [RtlpIcFetchImmediateOperand](RtlpIcFetchImmediateOperand_function_00BC83D8.md) (function, `0x00BC83D8`)
- `0x00BC7AEE` → [RtlpIcWriteRegisterValue](RtlpIcWriteRegisterValue_function_00BC8954.md) (function, `0x00BC8954`)
- `0x00BC7B0F` → [RtlpIcEmulateGroup0Instruction](RtlpIcEmulateGroup0Instruction_function_00BC74F8.md) (function, `0x00BC74F8`)
- `0x00BC7B74` → [RtlpIcDecodeModRm](RtlpIcDecodeModRm_function_00BC72B0.md) (function, `0x00BC72B0`)
- `0x00BC7BC9` → [RtlpIcSetImmediateOperandSize](RtlpIcSetImmediateOperandSize_function_00BC88F8.md) (function, `0x00BC88F8`)
- `0x00BC7BD8` → [RtlpIcEmulateGroup1Instruction](RtlpIcEmulateGroup1Instruction_function_00BC7818.md) (function, `0x00BC7818`)
- `0x00BC7BF0` → [RtlpIcFetchInstructionBytes](RtlpIcFetchInstructionBytes_function_00BC8454.md) (function, `0x00BC8454`)
- `0x00BC7C2C` → [RtlpIcEmulateMovzx](RtlpIcEmulateMovzx_function_00BC81FC.md) (function, `0x00BC81FC`)
- `0x00BC7C4D` → [RtlpIcDecodeModRmOperand](RtlpIcDecodeModRmOperand_function_00BC739C.md) (function, `0x00BC739C`)
- `0x00BC7C70` → [RtlpIcReadOperandValue](RtlpIcReadOperandValue_function_00BC8634.md) (function, `0x00BC8634`)
- `0x00BC7CA2` → [RtlpIcGetRegisterAddressByIndex](RtlpIcGetRegisterAddressByIndex_function_00BC8498.md) (function, `0x00BC8498`)
- `0x00BC7CAD` → [RtlpIcSignExtendOperandValue](RtlpIcSignExtendOperandValue_function_00BC8928.md) (function, `0x00BC8928`)
- `0x00BC7CCB` → [RtlpIcSetFlagsZeroSignParity](RtlpIcSetFlagsZeroSignParity_function_00BC8888.md) (function, `0x00BC8888`)
- `0x00BC7D1E` → [RtlpIcDecodeModRm](RtlpIcDecodeModRm_function_00BC72B0.md) (function, `0x00BC72B0`)
- `0x00BC7D4D` → [RtlpIcDecodeModRmOperand](RtlpIcDecodeModRmOperand_function_00BC739C.md) (function, `0x00BC739C`)
- `0x00BC7D70` → [RtlpIcReadOperandValue](RtlpIcReadOperandValue_function_00BC8634.md) (function, `0x00BC8634`)
- `0x00BC7D9B` → [RtlpIcDecodeModRm](RtlpIcDecodeModRm_function_00BC72B0.md) (function, `0x00BC72B0`)
- `0x00BC7DCA` → [RtlpIcDecodeModRmOperand](RtlpIcDecodeModRmOperand_function_00BC739C.md) (function, `0x00BC739C`)
- `0x00BC7DF2` → [RtlpIcGetRegisterAddressByIndex](RtlpIcGetRegisterAddressByIndex_function_00BC8498.md) (function, `0x00BC8498`)
- `0x00BC7DFD` → [RtlpIcSignExtendOperandValue](RtlpIcSignExtendOperandValue_function_00BC8928.md) (function, `0x00BC8928`)
- `0x00BC7E2F` → [RtlpIcAccessMemory](RtlpIcAccessMemory_function_00BC7198.md) (function, `0x00BC7198`)
- `0x00BC7E56` → [RtlpIcDecodeModRm](RtlpIcDecodeModRm_function_00BC72B0.md) (function, `0x00BC72B0`)
- `0x00BC7E85` → [RtlpIcDecodeModRmOperand](RtlpIcDecodeModRmOperand_function_00BC739C.md) (function, `0x00BC739C`)
- `0x00BC7EAA` → [RtlpIcReadOperandValue](RtlpIcReadOperandValue_function_00BC8634.md) (function, `0x00BC8634`)
- `0x00BC7EDC` → [RtlpIcGetRegisterAddressByIndex](RtlpIcGetRegisterAddressByIndex_function_00BC8498.md) (function, `0x00BC8498`)
- `0x00BC7EE7` → [RtlpIcSignExtendOperandValue](RtlpIcSignExtendOperandValue_function_00BC8928.md) (function, `0x00BC8928`)
- `0x00BC7F17` → [RtlpIcAccessMemory](RtlpIcAccessMemory_function_00BC7198.md) (function, `0x00BC7198`)
- `0x00BC7F4D` → [RtlpIcWriteRegisterValue](RtlpIcWriteRegisterValue_function_00BC8954.md) (function, `0x00BC8954`)
- `0x00BC7F61` → [RtlpIcDecodeModRm](RtlpIcDecodeModRm_function_00BC72B0.md) (function, `0x00BC72B0`)
- `0x00BC7F90` → [RtlpIcDecodeModRmOperand](RtlpIcDecodeModRmOperand_function_00BC739C.md) (function, `0x00BC739C`)
- `0x00BC8018` → [RtlpIcSetImmediateOperandSize](RtlpIcSetImmediateOperandSize_function_00BC88F8.md) (function, `0x00BC88F8`)
- `0x00BC8027` → [RtlpIcEmulateGroup11Instruction](RtlpIcEmulateGroup11Instruction_function_00BC7750.md) (function, `0x00BC7750`)
- `0x00BC803F` → [RtlpIcFetchInstructionBytes](RtlpIcFetchInstructionBytes_function_00BC8454.md) (function, `0x00BC8454`)
- `0x00BC807C` → [RtlpIcAccessMemory](RtlpIcAccessMemory_function_00BC7198.md) (function, `0x00BC7198`)
- `0x00BC8142` → [RtlpIcAccessMemory](RtlpIcAccessMemory_function_00BC7198.md) (function, `0x00BC7198`)

### Direct callers
- [KiTpCompletion](KiTpCompletion_function_00BC7010.md) at `0x00BC70A3`
- [RtlpIcParseInstruction](RtlpIcParseInstruction_function_00BC84F0.md) at `0x00BC8507`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC7A08  40 55                           push rbp
00BC7A0A  53                              push rbx
00BC7A0B  56                              push rsi
00BC7A0C  57                              push rdi
00BC7A0D  41 54                           push r12
00BC7A0F  41 56                           push r14
00BC7A11  48 8B EC                        mov rbp, rsp
00BC7A14  48 83 EC 68                     sub rsp, 0x68
00BC7A18  0F B6 41 15                     movzx eax, byte ptr [rcx + 0x15]
00BC7A1C  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00BC7A20  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
00BC7A25  48 8B FA                        mov rdi, rdx
00BC7A28  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
00BC7A2D  48 8D 55 48                     lea rdx, [rbp + 0x48]
00BC7A31  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
00BC7A36  41 BC 01 00 00 00               mov r12d, 1
00BC7A3C  45 8B C4                        mov r8d, r12d
00BC7A3F  C6 45 48 00                     mov byte ptr [rbp + 0x48], 0
00BC7A43  48 8B F1                        mov rsi, rcx
00BC7A46  C6 45 38 00                     mov byte ptr [rbp + 0x38], 0
00BC7A4A  C6 45 40 00                     mov byte ptr [rbp + 0x40], 0
00BC7A4E  89 45 50                        mov dword ptr [rbp + 0x50], eax
00BC7A51  E8 FE 09 00 00                  call 0x140bc8454
00BC7A56  8B D8                           mov ebx, eax
00BC7A58  85 C0                           test eax, eax
00BC7A5A  0F 88 74 07 00 00               js 0x140bc81d4
00BC7A60  0F B6 4D 48                     movzx ecx, byte ptr [rbp + 0x48]
00BC7A64  8A C1                           mov al, cl
00BC7A66  24 F0                           and al, 0xf0
00BC7A68  3C 50                           cmp al, 0x50
00BC7A6A  75 1D                           jne 0x140bc7a89
00BC7A6C  44 8B C1                        mov r8d, ecx
00BC7A6F  48 8B D7                        mov rdx, rdi
00BC7A72  48 8B CE                        mov rcx, rsi
00BC7A75  E8 92 08 00 00                  call 0x140bc830c
00BC7A7A  8B D8                           mov ebx, eax
00BC7A7C  85 C0                           test eax, eax
00BC7A7E  0F 88 50 07 00 00               js 0x140bc81d4
00BC7A84  E9 DC 06 00 00                  jmp 0x140bc8165
00BC7A89  3C B0                           cmp al, 0xb0
00BC7A8B  75 6D                           jne 0x140bc7afa
00BC7A8D  44 8B F1                        mov r14d, ecx
00BC7A90  48 85 FF                        test rdi, rdi
00BC7A93  75 1A                           jne 0x140bc7aaf
00BC7A95  41 F6 C6 08                     test r14b, 8
00BC7A99  75 04                           jne 0x140bc7a9f
00BC7A9B  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7A9F  41 B1 40                        mov r9b, 0x40
00BC7AA2  41 B0 20                        mov r8b, 0x20
00BC7AA5  B2 10                           mov dl, 0x10
00BC7AA7  48 8B CE                        mov rcx, rsi
00BC7AAA  E8 49 0E 00 00                  call 0x140bc88f8
00BC7AAF  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7AB3  48 8B D7                        mov rdx, rdi
00BC7AB6  48 8B CE                        mov rcx, rsi
00BC7AB9  E8 1A 09 00 00                  call 0x140bc83d8
00BC7ABE  8B D8                           mov ebx, eax
00BC7AC0  85 C0                           test eax, eax
00BC7AC2  0F 88 0C 07 00 00               js 0x140bc81d4
00BC7AC8  48 85 FF                        test rdi, rdi
00BC7ACB  0F 84 BB 00 00 00               je 0x140bc7b8c
00BC7AD1  44 8A 4E 19                     mov r9b, byte ptr [rsi + 0x19]
00BC7AD5  41 83 E6 07                     and r14d, 7
00BC7AD9  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00BC7ADD  45 22 CC                        and r9b, r12b
00BC7AE0  45 8B C6                        mov r8d, r14d
00BC7AE3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7AE8  48 8B D7                        mov rdx, rdi
00BC7AEB  48 8B CE                        mov rcx, rsi
00BC7AEE  E8 61 0E 00 00                  call 0x140bc8954
00BC7AF3  33 DB                           xor ebx, ebx
00BC7AF5  E9 70 06 00 00                  jmp 0x140bc816a
00BC7AFA  F7 C1 C4 FF FF FF               test ecx, 0xffffffc4
00BC7B00  75 17                           jne 0x140bc7b19
00BC7B02  44 8B C1                        mov r8d, ecx
00BC7B05  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00BC7B09  48 8B CE                        mov rcx, rsi
00BC7B0C  48 8B D7                        mov rdx, rdi
00BC7B0F  E8 E4 F9 FF FF                  call 0x140bc74f8
00BC7B14  E9 61 FF FF FF                  jmp 0x140bc7a7a
00BC7B19  B8 8D 00 00 00                  mov eax, 0x8d
00BC7B1E  3B C8                           cmp ecx, eax
00BC7B20  0F 87 91 04 00 00               ja 0x140bc7fb7
00BC7B26  0F 84 2B 04 00 00               je 0x140bc7f57
00BC7B2C  B8 85 00 00 00                  mov eax, 0x85
00BC7B31  3B C8                           cmp ecx, eax
00BC7B33  0F 87 9C 01 00 00               ja 0x140bc7cd5
00BC7B39  74 2F                           je 0x140bc7b6a
00BC7B3B  83 E9 0F                        sub ecx, 0xf
00BC7B3E  0F 84 9E 00 00 00               je 0x140bc7be2
00BC7B44  83 E9 71                        sub ecx, 0x71
00BC7B47  74 6C                           je 0x140bc7bb5
00BC7B49  41 2B CC                        sub ecx, r12d
00BC7B4C  74 60                           je 0x140bc7bae
00BC7B4E  41 2B CC                        sub ecx, r12d
00BC7B51  74 47                           je 0x140bc7b9a
00BC7B53  41 2B CC                        sub ecx, r12d
00BC7B56  74 3B                           je 0x140bc7b93
00BC7B58  41 3B CC                        cmp ecx, r12d
00BC7B5B  0F 85 6E 06 00 00               jne 0x140bc81cf
00BC7B61  48 85 FF                        test rdi, rdi
00BC7B64  75 04                           jne 0x140bc7b6a
00BC7B66  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7B6A  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7B6E  48 8B D7                        mov rdx, rdi
00BC7B71  48 8B CE                        mov rcx, rsi
00BC7B74  E8 37 F7 FF FF                  call 0x140bc72b0
00BC7B79  8B D8                           mov ebx, eax
00BC7B7B  85 C0                           test eax, eax
00BC7B7D  0F 88 51 06 00 00               js 0x140bc81d4
00BC7B83  48 85 FF                        test rdi, rdi
00BC7B86  0F 85 AA 00 00 00               jne 0x140bc7c36
00BC7B8C  33 DB                           xor ebx, ebx
00BC7B8E  E9 4A 06 00 00                  jmp 0x140bc81dd
00BC7B93  48 85 FF                        test rdi, rdi
00BC7B96  75 36                           jne 0x140bc7bce
00BC7B98  EB 09                           jmp 0x140bc7ba3
00BC7B9A  48 85 FF                        test rdi, rdi
00BC7B9D  75 2F                           jne 0x140bc7bce
00BC7B9F  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7BA3  41 B1 08                        mov r9b, 8
00BC7BA6  45 8A C1                        mov r8b, r9b
00BC7BA9  41 8A D1                        mov dl, r9b
00BC7BAC  EB 18                           jmp 0x140bc7bc6
00BC7BAE  48 85 FF                        test rdi, rdi
00BC7BB1  75 1B                           jne 0x140bc7bce
00BC7BB3  EB 09                           jmp 0x140bc7bbe
00BC7BB5  48 85 FF                        test rdi, rdi
00BC7BB8  75 14                           jne 0x140bc7bce
00BC7BBA  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7BBE  41 B1 20                        mov r9b, 0x20
00BC7BC1  B2 10                           mov dl, 0x10
00BC7BC3  45 8A C1                        mov r8b, r9b
00BC7BC6  48 8B CE                        mov rcx, rsi
00BC7BC9  E8 2A 0D 00 00                  call 0x140bc88f8
00BC7BCE  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7BD2  48 8B D7                        mov rdx, rdi
00BC7BD5  48 8B CE                        mov rcx, rsi
00BC7BD8  E8 3B FC FF FF                  call 0x140bc7818
00BC7BDD  E9 98 FE FF FF                  jmp 0x140bc7a7a
00BC7BE2  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00BC7BE6  45 8B C4                        mov r8d, r12d
00BC7BE9  48 8D 55 48                     lea rdx, [rbp + 0x48]
00BC7BED  48 8B CE                        mov rcx, rsi
00BC7BF0  E8 5F 08 00 00                  call 0x140bc8454
00BC7BF5  8B D8                           mov ebx, eax
00BC7BF7  85 C0                           test eax, eax
00BC7BF9  0F 88 D5 05 00 00               js 0x140bc81d4
00BC7BFF  44 0F B6 45 48                  movzx r8d, byte ptr [rbp + 0x48]
00BC7C04  41 8B C8                        mov ecx, r8d
00BC7C07  81 E9 B6 00 00 00               sub ecx, 0xb6
00BC7C0D  74 09                           je 0x140bc7c18
00BC7C0F  41 3B CC                        cmp ecx, r12d
00BC7C12  0F 85 B7 05 00 00               jne 0x140bc81cf
00BC7C18  45 22 C4                        and r8b, r12b
00BC7C1B  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00BC7C1F  45 02 C4                        add r8b, r12b
00BC7C22  48 8B D7                        mov rdx, rdi
00BC7C25  41 C0 E0 03                     shl r8b, 3
00BC7C29  48 8B CE                        mov rcx, rsi
00BC7C2C  E8 CB 05 00 00                  call 0x140bc81fc
00BC7C31  E9 44 FE FF FF                  jmp 0x140bc7a7a
00BC7C36  48 8D 45 40                     lea rax, [rbp + 0x40]
00BC7C3A  48 8B D7                        mov rdx, rdi
00BC7C3D  4C 8D 4D 38                     lea r9, [rbp + 0x38]
00BC7C41  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7C46  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00BC7C4A  48 8B CE                        mov rcx, rsi
00BC7C4D  E8 4A F7 FF FF                  call 0x140bc739c
00BC7C52  44 8A 4D 38                     mov r9b, byte ptr [rbp + 0x38]
00BC7C56  48 8D 45 E0                     lea rax, [rbp - 0x20]
00BC7C5A  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00BC7C5E  48 8B D7                        mov rdx, rdi
00BC7C61  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BC7C66  48 8B CE                        mov rcx, rsi
00BC7C69  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00BC7C6C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00BC7C70  E8 BF 09 00 00                  call 0x140bc8634
00BC7C75  8B D8                           mov ebx, eax
00BC7C77  85 C0                           test eax, eax
00BC7C79  0F 88 64 05 00 00               js 0x140bc81e3
00BC7C7F  44 0F B6 46 1A                  movzx r8d, byte ptr [rsi + 0x1a]
00BC7C84  48 8B D7                        mov rdx, rdi
00BC7C87  44 8A 4E 19                     mov r9b, byte ptr [rsi + 0x19]
00BC7C8B  48 8B CE                        mov rcx, rsi
00BC7C8E  41 C1 E8 03                     shr r8d, 3
00BC7C92  41 C0 E9 02                     shr r9b, 2
00BC7C96  41 83 E0 07                     and r8d, 7
00BC7C9A  45 22 CC                        and r9b, r12b
00BC7C9D  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00BC7CA2  E8 F1 07 00 00                  call 0x140bc8498
00BC7CA7  48 8B CE                        mov rcx, rsi
00BC7CAA  48 8B 10                        mov rdx, qword ptr [rax]
00BC7CAD  E8 76 0C 00 00                  call 0x140bc8928
00BC7CB2  4C 8B C0                        mov r8, rax
00BC7CB5  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00BC7CB9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00BC7CBD  48 8B D7                        mov rdx, rdi
00BC7CC0  4C 23 45 E0                     and r8, qword ptr [rbp - 0x20]
00BC7CC4  81 60 44 FE F7 FF FF            and dword ptr [rax + 0x44], 0xfffff7fe
00BC7CCB  E8 B8 0B 00 00                  call 0x140bc8888
00BC7CD0  E9 95 04 00 00                  jmp 0x140bc816a
00BC7CD5  81 E9 86 00 00 00               sub ecx, 0x86
00BC7CDB  0F 84 62 01 00 00               je 0x140bc7e43
00BC7CE1  41 2B CC                        sub ecx, r12d
00BC7CE4  0F 84 62 01 00 00               je 0x140bc7e4c
00BC7CEA  41 2B CC                        sub ecx, r12d
00BC7CED  0F 84 95 00 00 00               je 0x140bc7d88
00BC7CF3  41 2B CC                        sub ecx, r12d
00BC7CF6  0F 84 95 00 00 00               je 0x140bc7d91
00BC7CFC  41 2B CC                        sub ecx, r12d
00BC7CFF  74 0A                           je 0x140bc7d0b
00BC7D01  41 3B CC                        cmp ecx, r12d
00BC7D04  74 0E                           je 0x140bc7d14
00BC7D06  E9 C4 04 00 00                  jmp 0x140bc81cf
00BC7D0B  48 85 FF                        test rdi, rdi
00BC7D0E  75 04                           jne 0x140bc7d14
00BC7D10  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7D14  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7D18  48 8B D7                        mov rdx, rdi
00BC7D1B  48 8B CE                        mov rcx, rsi
00BC7D1E  E8 8D F5 FF FF                  call 0x140bc72b0
00BC7D23  8B D8                           mov ebx, eax
00BC7D25  85 C0                           test eax, eax
00BC7D27  0F 88 A7 04 00 00               js 0x140bc81d4
00BC7D2D  48 85 FF                        test rdi, rdi
00BC7D30  0F 84 56 FE FF FF               je 0x140bc7b8c
00BC7D36  48 8D 45 40                     lea rax, [rbp + 0x40]
00BC7D3A  48 8B D7                        mov rdx, rdi
00BC7D3D  4C 8D 4D 38                     lea r9, [rbp + 0x38]
00BC7D41  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7D46  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00BC7D4A  48 8B CE                        mov rcx, rsi
00BC7D4D  E8 4A F6 FF FF                  call 0x140bc739c
00BC7D52  44 8A 4D 38                     mov r9b, byte ptr [rbp + 0x38]
00BC7D56  48 8D 45 E8                     lea rax, [rbp - 0x18]
00BC7D5A  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00BC7D5E  48 8B D7                        mov rdx, rdi
00BC7D61  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BC7D66  48 8B CE                        mov rcx, rsi
00BC7D69  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00BC7D6C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00BC7D70  E8 BF 08 00 00                  call 0x140bc8634
00BC7D75  8B D8                           mov ebx, eax
00BC7D77  85 C0                           test eax, eax
00BC7D79  0F 88 64 04 00 00               js 0x140bc81e3
00BC7D7F  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00BC7D83  E9 A2 01 00 00                  jmp 0x140bc7f2a
00BC7D88  48 85 FF                        test rdi, rdi
00BC7D8B  75 04                           jne 0x140bc7d91
00BC7D8D  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7D91  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7D95  48 8B D7                        mov rdx, rdi
00BC7D98  48 8B CE                        mov rcx, rsi
00BC7D9B  E8 10 F5 FF FF                  call 0x140bc72b0
00BC7DA0  8B D8                           mov ebx, eax
00BC7DA2  85 C0                           test eax, eax
00BC7DA4  0F 88 2A 04 00 00               js 0x140bc81d4
00BC7DAA  48 85 FF                        test rdi, rdi
00BC7DAD  0F 84 D9 FD FF FF               je 0x140bc7b8c
00BC7DB3  48 8D 45 40                     lea rax, [rbp + 0x40]
00BC7DB7  48 8B D7                        mov rdx, rdi
00BC7DBA  4C 8D 4D 38                     lea r9, [rbp + 0x38]
00BC7DBE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7DC3  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00BC7DC7  48 8B CE                        mov rcx, rsi
00BC7DCA  E8 CD F5 FF FF                  call 0x140bc739c
00BC7DCF  44 0F B6 46 1A                  movzx r8d, byte ptr [rsi + 0x1a]
00BC7DD4  48 8B D7                        mov rdx, rdi
00BC7DD7  44 8A 4E 19                     mov r9b, byte ptr [rsi + 0x19]
00BC7DDB  48 8B CE                        mov rcx, rsi
00BC7DDE  41 C1 E8 03                     shr r8d, 3
00BC7DE2  41 C0 E9 02                     shr r9b, 2
00BC7DE6  41 83 E0 07                     and r8d, 7
00BC7DEA  45 22 CC                        and r9b, r12b
00BC7DED  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00BC7DF2  E8 A1 06 00 00                  call 0x140bc8498
00BC7DF7  48 8B CE                        mov rcx, rsi
00BC7DFA  48 8B 10                        mov rdx, qword ptr [rax]
00BC7DFD  E8 26 0B 00 00                  call 0x140bc8928
00BC7E02  44 8A 4D 38                     mov r9b, byte ptr [rbp + 0x38]
00BC7E06  48 8D 55 48                     lea rdx, [rbp + 0x48]
00BC7E0A  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00BC7E0E  48 8B CF                        mov rcx, rdi
00BC7E11  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00BC7E15  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00BC7E19  8A 46 01                        mov al, byte ptr [rsi + 1]
00BC7E1C  C0 E8 03                        shr al, 3
00BC7E1F  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
00BC7E24  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00BC7E28  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00BC7E2B  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00BC7E2F  E8 64 F3 FF FF                  call 0x140bc7198
00BC7E34  8B D8                           mov ebx, eax
00BC7E36  85 C0                           test eax, eax
00BC7E38  0F 88 A5 03 00 00               js 0x140bc81e3
00BC7E3E  E9 27 03 00 00                  jmp 0x140bc816a
00BC7E43  48 85 FF                        test rdi, rdi
00BC7E46  75 04                           jne 0x140bc7e4c
00BC7E48  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC7E4C  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7E50  48 8B D7                        mov rdx, rdi
00BC7E53  48 8B CE                        mov rcx, rsi
00BC7E56  E8 55 F4 FF FF                  call 0x140bc72b0
00BC7E5B  8B D8                           mov ebx, eax
00BC7E5D  85 C0                           test eax, eax
00BC7E5F  0F 88 6F 03 00 00               js 0x140bc81d4
00BC7E65  48 85 FF                        test rdi, rdi
00BC7E68  0F 84 1E FD FF FF               je 0x140bc7b8c
00BC7E6E  48 8D 45 40                     lea rax, [rbp + 0x40]
00BC7E72  48 8B D7                        mov rdx, rdi
00BC7E75  4C 8D 4D 38                     lea r9, [rbp + 0x38]
00BC7E79  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7E7E  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00BC7E82  48 8B CE                        mov rcx, rsi
00BC7E85  E8 12 F5 FF FF                  call 0x140bc739c
00BC7E8A  44 8A 75 40                     mov r14b, byte ptr [rbp + 0x40]
00BC7E8E  48 8D 45 E0                     lea rax, [rbp - 0x20]
00BC7E92  44 8A 4D 38                     mov r9b, byte ptr [rbp + 0x38]
00BC7E96  48 8B D7                        mov rdx, rdi
00BC7E99  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00BC7E9D  48 8B CE                        mov rcx, rsi
00BC7EA0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BC7EA5  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00BC7EAA  E8 85 07 00 00                  call 0x140bc8634
00BC7EAF  8B D8                           mov ebx, eax
00BC7EB1  85 C0                           test eax, eax
00BC7EB3  0F 88 2A 03 00 00               js 0x140bc81e3
00BC7EB9  44 0F B6 46 1A                  movzx r8d, byte ptr [rsi + 0x1a]
00BC7EBE  48 8B D7                        mov rdx, rdi
00BC7EC1  44 8A 4E 19                     mov r9b, byte ptr [rsi + 0x19]
00BC7EC5  48 8B CE                        mov rcx, rsi
00BC7EC8  41 C1 E8 03                     shr r8d, 3
00BC7ECC  41 C0 E9 02                     shr r9b, 2
00BC7ED0  41 83 E0 07                     and r8d, 7
00BC7ED4  45 22 CC                        and r9b, r12b
00BC7ED7  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00BC7EDC  E8 B7 05 00 00                  call 0x140bc8498
00BC7EE1  48 8B CE                        mov rcx, rsi
00BC7EE4  48 8B 10                        mov rdx, qword ptr [rax]
00BC7EE7  E8 3C 0A 00 00                  call 0x140bc8928
00BC7EEC  44 8A 4D 38                     mov r9b, byte ptr [rbp + 0x38]
00BC7EF0  48 8D 55 40                     lea rdx, [rbp + 0x40]
00BC7EF4  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00BC7EF8  48 8B CF                        mov rcx, rdi
00BC7EFB  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00BC7EFF  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00BC7F03  8A 46 01                        mov al, byte ptr [rsi + 1]
00BC7F06  C0 E8 03                        shr al, 3
00BC7F09  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
00BC7F0E  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00BC7F12  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00BC7F17  E8 7C F2 FF FF                  call 0x140bc7198
00BC7F1C  8B D8                           mov ebx, eax
00BC7F1E  85 C0                           test eax, eax
00BC7F20  0F 88 BD 02 00 00               js 0x140bc81e3
00BC7F26  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00BC7F2A  44 8A 4E 19                     mov r9b, byte ptr [rsi + 0x19]
00BC7F2E  48 8B D7                        mov rdx, rdi
00BC7F31  44 0F B6 46 1A                  movzx r8d, byte ptr [rsi + 0x1a]
00BC7F36  48 8B CE                        mov rcx, rsi
00BC7F39  41 C0 E9 02                     shr r9b, 2
00BC7F3D  41 C1 E8 03                     shr r8d, 3
00BC7F41  45 22 CC                        and r9b, r12b
00BC7F44  41 83 E0 07                     and r8d, 7
00BC7F48  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7F4D  E8 02 0A 00 00                  call 0x140bc8954
00BC7F52  E9 13 02 00 00                  jmp 0x140bc816a
00BC7F57  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC7F5B  48 8B D7                        mov rdx, rdi
00BC7F5E  48 8B CE                        mov rcx, rsi
00BC7F61  E8 4A F3 FF FF                  call 0x140bc72b0
00BC7F66  8B D8                           mov ebx, eax
00BC7F68  85 C0                           test eax, eax
00BC7F6A  0F 88 64 02 00 00               js 0x140bc81d4
00BC7F70  48 85 FF                        test rdi, rdi
00BC7F73  0F 84 13 FC FF FF               je 0x140bc7b8c
00BC7F79  48 8D 45 40                     lea rax, [rbp + 0x40]
00BC7F7D  48 8B D7                        mov rdx, rdi
00BC7F80  4C 8D 4D 38                     lea r9, [rbp + 0x38]
00BC7F84  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BC7F89  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00BC7F8D  48 8B CE                        mov rcx, rsi
00BC7F90  E8 07 F4 FF FF                  call 0x140bc739c
00BC7F95  80 7D 40 00                     cmp byte ptr [rbp + 0x40], 0
00BC7F99  74 13                           je 0x140bc7fae
00BC7F9B  48 8B 07                        mov rax, qword ptr [rdi]
00BC7F9E  BB 1D 00 00 C0                  mov ebx, 0xc000001d
00BC7FA3  83 60 18 00                     and dword ptr [rax + 0x18], 0
00BC7FA7  89 18                           mov dword ptr [rax], ebx
00BC7FA9  E9 35 02 00 00                  jmp 0x140bc81e3
00BC7FAE  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00BC7FB2  E9 73 FF FF FF                  jmp 0x140bc7f2a
00BC7FB7  B8 CC 00 00 00                  mov eax, 0xcc
00BC7FBC  3B C8                           cmp ecx, eax
00BC7FBE  0F 87 EE 01 00 00               ja 0x140bc81b2
00BC7FC4  0F 84 05 02 00 00               je 0x140bc81cf
00BC7FCA  81 E9 90 00 00 00               sub ecx, 0x90
00BC7FD0  0F 84 89 01 00 00               je 0x140bc815f
00BC7FD6  83 E9 0C                        sub ecx, 0xc
00BC7FD9  0F 84 1B 01 00 00               je 0x140bc80fa
00BC7FDF  41 BE 02 00 00 00               mov r14d, 2
00BC7FE5  83 E9 26                        sub ecx, 0x26
00BC7FE8  74 47                           je 0x140bc8031
00BC7FEA  41 2B CC                        sub ecx, r12d
00BC7FED  74 5F                           je 0x140bc804e
00BC7FEF  83 E9 03                        sub ecx, 3
00BC7FF2  74 10                           je 0x140bc8004
00BC7FF4  41 3B CC                        cmp ecx, r12d
00BC7FF7  0F 85 D2 01 00 00               jne 0x140bc81cf
00BC7FFD  48 85 FF                        test rdi, rdi
00BC8000  75 1B                           jne 0x140bc801d
00BC8002  EB 09                           jmp 0x140bc800d
00BC8004  48 85 FF                        test rdi, rdi
00BC8007  75 14                           jne 0x140bc801d
00BC8009  C6 46 01 08                     mov byte ptr [rsi + 1], 8
00BC800D  41 B1 20                        mov r9b, 0x20
00BC8010  B2 10                           mov dl, 0x10
00BC8012  45 8A C1                        mov r8b, r9b
00BC8015  48 8B CE                        mov rcx, rsi
00BC8018  E8 DB 08 00 00                  call 0x140bc88f8
00BC801D  4C 8D 45 50                     lea r8, [rbp + 0x50]
00BC8021  48 8B D7                        mov rdx, rdi
00BC8024  48 8B CE                        mov rcx, rsi
00BC8027  E8 24 F7 FF FF                  call 0x140bc7750
00BC802C  E9 49 FA FF FF                  jmp 0x140bc7a7a
00BC8031  48 8D 56 20                     lea rdx, [rsi + 0x20]
00BC8035  45 8B C6                        mov r8d, r14d
00BC8038  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00BC803C  48 8B CE                        mov rcx, rsi
00BC803F  E8 10 04 00 00                  call 0x140bc8454
00BC8044  8B D8                           mov ebx, eax
00BC8046  85 C0                           test eax, eax
00BC8048  0F 88 86 01 00 00               js 0x140bc81d4
00BC804E  48 85 FF                        test rdi, rdi
00BC8051  0F 84 35 FB FF FF               je 0x140bc7b8c
00BC8057  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
00BC805B  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00BC805F  44 8A 4F 10                     mov r9b, byte ptr [rdi + 0x10]
00BC8063  48 8B CF                        mov rcx, rdi
00BC8066  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
00BC806B  C6 44 24 28 08                  mov byte ptr [rsp + 0x28], 8
00BC8070  4D 8B 80 98 00 00 00            mov r8, qword ptr [r8 + 0x98]
00BC8077  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00BC807C  E8 17 F1 FF FF                  call 0x140bc7198
00BC8081  8B D8                           mov ebx, eax
00BC8083  85 C0                           test eax, eax
00BC8085  0F 88 58 01 00 00               js 0x140bc81e3
00BC808B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00BC808F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00BC8093  48 89 81 F8 00 00 00            mov qword ptr [rcx + 0xf8], rax
00BC809A  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00BC809E  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00BC80A2  48 83 C0 08                     add rax, 8
00BC80A6  48 01 81 98 00 00 00            add qword ptr [rcx + 0x98], rax
00BC80AD  B9 80 00 10 00                  mov ecx, 0x100080
00BC80B2  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00BC80B6  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
00BC80B9  23 C1                           and eax, ecx
00BC80BB  3B C1                           cmp eax, ecx
00BC80BD  75 34                           jne 0x140bc80f3
00BC80BF  48 63 8A E8 04 00 00            movsxd rcx, dword ptr [rdx + 0x4e8]
00BC80C6  41 B8 FE FF 00 00               mov r8d, 0xfffe
00BC80CC  48 8B 82 F8 00 00 00            mov rax, qword ptr [rdx + 0xf8]
00BC80D3  48 89 84 11 D8 04 00 00         mov qword ptr [rcx + rdx + 0x4d8], rax
00BC80DB  0F B7 84 11 E2 04 00 00         movzx eax, word ptr [rcx + rdx + 0x4e2]
00BC80E3  66 41 23 C0                     and ax, r8w
00BC80E7  66 41 0B C6                     or ax, r14w
00BC80EB  66 89 84 11 E2 04 00 00         mov word ptr [rcx + rdx + 0x4e2], ax
00BC80F3  33 DB                           xor ebx, ebx
00BC80F5  E9 E9 00 00 00                  jmp 0x140bc81e3
00BC80FA  F6 46 19 08                     test byte ptr [rsi + 0x19], 8
00BC80FE  0F 84 CB 00 00 00               je 0x140bc81cf
00BC8104  48 85 FF                        test rdi, rdi
00BC8107  0F 84 7F FA FF FF               je 0x140bc7b8c
00BC810D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00BC8111  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00BC8115  44 8A 4F 10                     mov r9b, byte ptr [rdi + 0x10]
00BC8119  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
00BC811E  C6 44 24 28 08                  mov byte ptr [rsp + 0x28], 8
00BC8123  8B 41 44                        mov eax, dword ptr [rcx + 0x44]
00BC8126  25 FF FF FC 00                  and eax, 0xfcffff
00BC812B  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00BC8130  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00BC8134  4C 8B 81 98 00 00 00            mov r8, qword ptr [rcx + 0x98]
00BC813B  48 8B CF                        mov rcx, rdi
00BC813E  49 83 E8 08                     sub r8, 8
00BC8142  E8 51 F0 FF FF                  call 0x140bc7198
00BC8147  8B D8                           mov ebx, eax
00BC8149  85 C0                           test eax, eax
00BC814B  0F 88 92 00 00 00               js 0x140bc81e3
00BC8151  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00BC8155  48 83 80 98 00 00 00 F8         add qword ptr [rax + 0x98], -8
00BC815D  EB 0B                           jmp 0x140bc816a
00BC815F  44 84 66 19                     test byte ptr [rsi + 0x19], r12b
00BC8163  75 6A                           jne 0x140bc81cf
00BC8165  48 85 FF                        test rdi, rdi
00BC8168  74 6F                           je 0x140bc81d9
00BC816A  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00BC816E  0F B6 46 18                     movzx eax, byte ptr [rsi + 0x18]
00BC8172  48 01 81 F8 00 00 00            add qword ptr [rcx + 0xf8], rax
00BC8179  B9 80 00 10 00                  mov ecx, 0x100080
00BC817E  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00BC8182  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
00BC8185  23 C1                           and eax, ecx
00BC8187  3B C1                           cmp eax, ecx
00BC8189  75 58                           jne 0x140bc81e3
00BC818B  48 63 8A E8 04 00 00            movsxd rcx, dword ptr [rdx + 0x4e8]
00BC8192  41 B8 FE FF 00 00               mov r8d, 0xfffe
00BC8198  48 8B 82 F8 00 00 00            mov rax, qword ptr [rdx + 0xf8]
00BC819F  66 44 21 84 11 E2 04 00 00      and word ptr [rcx + rdx + 0x4e2], r8w
00BC81A8  48 89 84 11 D8 04 00 00         mov qword ptr [rcx + rdx + 0x4d8], rax
00BC81B0  EB 31                           jmp 0x140bc81e3
00BC81B2  81 E9 CD 00 00 00               sub ecx, 0xcd
00BC81B8  74 15                           je 0x140bc81cf
00BC81BA  41 2B CC                        sub ecx, r12d
00BC81BD  74 10                           je 0x140bc81cf
00BC81BF  41 2B CC                        sub ecx, r12d
00BC81C2  74 0B                           je 0x140bc81cf
00BC81C4  83 E9 0A                        sub ecx, 0xa
00BC81C7  74 06                           je 0x140bc81cf
00BC81C9  41 BE 02 00 00 00               mov r14d, 2
00BC81CF  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00BC81D4  48 85 FF                        test rdi, rdi
00BC81D7  75 0A                           jne 0x140bc81e3
00BC81D9  85 DB                           test ebx, ebx
00BC81DB  78 06                           js 0x140bc81e3
00BC81DD  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00BC81E0  88 46 18                        mov byte ptr [rsi + 0x18], al
00BC81E3  8B C3                           mov eax, ebx
00BC81E5  48 83 C4 68                     add rsp, 0x68
00BC81E9  41 5E                           pop r14
00BC81EB  41 5C                           pop r12
00BC81ED  5F                              pop rdi
00BC81EE  5E                              pop rsi
00BC81EF  5B                              pop rbx
00BC81F0  5D                              pop rbp
00BC81F1  C3                              ret
00BC81F2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpIcEmulateInstruction(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (104);
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = (unsigned int)(*(unsigned __int8 *)(a1 + 21));
    result = RtlpIcFetchInstructionBytes(a1, v_stack_p18, 1, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p18)) & (240));
    if (((unsigned __int8)(result)) != 80) goto loc_00BC7A89;
    result = RtlpIcEmulateRegisterPushPop(a1, a2, (unsigned int)((unsigned int)(v_stack_p18)), v_stack_p20);
loc_00BC7A7A:
    if (sign_flag) goto loc_00BC81D4;
    goto loc_00BC8165;
loc_00BC7A89:
    if (((unsigned __int8)(result)) != 176) goto loc_00BC7AFA;
    if (a2 != 0) goto loc_00BC7AAF;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(a1)))) & (8)) == 0) {
        *(unsigned __int8 *)(a1 + 1) = 8;
    }
    result = RtlpIcSetImmediateOperandSize(a1, 16, 32, 64);
loc_00BC7AAF:
    result = RtlpIcFetchImmediateOperand(a1, a2, v_stack_p20, 64);
    if (sign_flag) goto loc_00BC81D4;
    if (a2 == 0) goto loc_00BC7B8C;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (7));
    a4 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 25)) & (1));
    v_stack_m78 = *(unsigned __int64 *)(a1 + 32);
    result = RtlpIcWriteRegisterValue(a1, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    v_rbx = 0;
    goto loc_00BC816A;
loc_00BC7AFA:
    if ((((unsigned int)(a1)) & (0xFFFFFFC4ULL)) != 0) goto loc_00BC7B19;
    result = RtlpIcEmulateGroup0Instruction(a1, a2, (unsigned int)((unsigned int)(a1)), v_stack_p20);
    goto loc_00BC7A7A;
loc_00BC7B19:
    if (((unsigned int)(a1)) > 141) goto loc_00BC7FB7;
    if (((unsigned int)(a1)) == 141) goto loc_00BC7F57;
    if (((unsigned int)(a1)) > 133) goto loc_00BC7CD5;
    if (((unsigned int)(a1)) == 133) goto loc_00BC7B6A;
    a1 = (unsigned int)((a1) - (15));
    if (condition_is_equal) goto loc_00BC7BE2;
    a1 = (unsigned int)((a1) - (113));
    if (condition_is_equal) goto loc_00BC7BB5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7BAE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7B9A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7B93;
    if (((unsigned int)(a1)) != 1) goto loc_00BC81CF;
    if (a2 == 0) {
        *(unsigned __int8 *)(a1 + 1) = 8;
    }
    result = RtlpIcDecodeModRm(a1, a2, v_stack_p20, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
    if (a2 != 0) goto loc_00BC7C36;
loc_00BC7B8C:
    v_rbx = 0;
    goto loc_00BC81DD;
loc_00BC7B93:
    if (a2 != 0) goto loc_00BC7BCE;
    goto loc_00BC7BA3;
loc_00BC7B9A:
    if (a2 != 0) goto loc_00BC7BCE;
    *(unsigned __int8 *)(a1 + 1) = 8;
loc_00BC7BA3:
    goto loc_00BC7BC6;
loc_00BC7BAE:
    if (a2 != 0) goto loc_00BC7BCE;
    goto loc_00BC7BBE;
loc_00BC7BB5:
    if (a2 != 0) goto loc_00BC7BCE;
    *(unsigned __int8 *)(a1 + 1) = 8;
loc_00BC7BBE:
loc_00BC7BC6:
    result = RtlpIcSetImmediateOperandSize(a1, 16, 32, 32);
loc_00BC7BCE:
    result = RtlpIcEmulateGroup1Instruction(a1, a2, v_stack_p20, 32);
    goto loc_00BC7A7A;
loc_00BC7BE2:
    result = RtlpIcFetchInstructionBytes(a1, v_stack_p18, 1, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) - (182));
    if (condition_is_equal) goto loc_00BC7C18;
    if (((unsigned int)(a1)) != 1) goto loc_00BC81CF;
loc_00BC7C18:
    a3 = (unsigned __int8)((v_stack_p18) & (1));
    a3 = (unsigned __int8)((a3) + (1));
    a3 = (unsigned __int8)((a3) << (3));
    result = RtlpIcEmulateMovzx(a1, a2, a3, v_stack_p20);
    goto loc_00BC7A7A;
loc_00BC7C36:
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(a1, a2, v_stack_m58, v_stack_p8);
    v_stack_m70 = v_stack_m50;
    v_stack_m78 = (unsigned __int8)(v_stack_p10);
    result = RtlpIcReadOperandValue(a1, a2, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) >> (3));
    a4 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 25)) >> (2));
    a3 = (unsigned int)((a3) & (7));
    a4 = (unsigned __int8)((a4) & (1));
    v_stack_m78 = 1;
    result = RtlpIcGetRegisterAddressByIndex(a1, a2, a3, a4);
    result = RtlpIcSignExtendOperandValue(a1, *(unsigned __int64 *)(result), a3, a4);
    v_stack_m48 = result;
    a3 = (result) & (v_stack_m50);
    result = RtlpIcSetFlagsZeroSignParity(a1, a2, a3, a4);
    goto loc_00BC816A;
loc_00BC7CD5:
    a1 = (unsigned int)((a1) - (134));
    if (condition_is_equal) goto loc_00BC7E43;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7E4C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7D88;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7D91;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC7D0B;
    if (((unsigned int)(a1)) == 1) goto loc_00BC7D14;
    goto loc_00BC81CF;
loc_00BC7D0B:
    if (a2 == 0) {
        *(unsigned __int8 *)(a1 + 1) = 8;
    }
    result = RtlpIcDecodeModRm(a1, a2, v_stack_p20, a4);
    if (sign_flag) goto loc_00BC81D4;
    if (a2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(a1, a2, v_stack_m58, v_stack_p8);
    v_stack_m70 = v_stack_m48;
    v_stack_m78 = (unsigned __int8)(v_stack_p10);
    result = RtlpIcReadOperandValue(a1, a2, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    goto loc_00BC7F2A;
loc_00BC7D88:
    if (a2 == 0) {
        *(unsigned __int8 *)(a1 + 1) = 8;
    }
    result = RtlpIcDecodeModRm(a1, a2, v_stack_p20, v_stack_p8);
    if (sign_flag) goto loc_00BC81D4;
    if (a2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(a1, a2, v_stack_m58, v_stack_p8);
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) >> (3));
    a4 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 25)) >> (2));
    a3 = (unsigned int)((a3) & (7));
    a4 = (unsigned __int8)((a4) & (1));
    v_stack_m78 = 1;
    result = RtlpIcGetRegisterAddressByIndex(a1, a2, a3, a4);
    result = RtlpIcSignExtendOperandValue(a1, *(unsigned __int64 *)(result), a3, a4);
    v_stack_m48 = result;
    v_stack_p18 = result;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 1)) >> (3));
    v_stack_m68 = 1;
    v_stack_m70 = (unsigned __int8)(result);
    v_stack_m78 = (unsigned __int8)(v_stack_p10);
    result = RtlpIcAccessMemory(a2, v_stack_p18, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    goto loc_00BC816A;
loc_00BC7E43:
    if (a2 == 0) {
        *(unsigned __int8 *)(a1 + 1) = 8;
    }
    result = RtlpIcDecodeModRm(a1, a2, v_stack_p20, v_stack_p8);
    if (sign_flag) goto loc_00BC81D4;
    if (a2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(a1, a2, v_stack_m58, v_stack_p8);
    v_stack_m70 = v_stack_m50;
    v_stack_m78 = (unsigned __int8)(v_stack_p10);
    result = RtlpIcReadOperandValue(a1, a2, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) >> (3));
    a4 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 25)) >> (2));
    a3 = (unsigned int)((a3) & (7));
    a4 = (unsigned __int8)((a4) & (1));
    v_stack_m78 = 1;
    result = RtlpIcGetRegisterAddressByIndex(a1, a2, a3, a4);
    result = RtlpIcSignExtendOperandValue(a1, *(unsigned __int64 *)(result), a3, a4);
    v_stack_m48 = result;
    v_stack_p10 = result;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 1)) >> (3));
    v_stack_m68 = 1;
    v_stack_m70 = (unsigned __int8)(result);
    v_stack_m78 = (unsigned __int8)(v_stack_p10);
    result = RtlpIcAccessMemory(a2, v_stack_p10, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
loc_00BC7F2A:
    a4 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 25)) >> (2));
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) >> (3));
    a4 = (unsigned __int8)((a4) & (1));
    a3 = (unsigned int)((a3) & (7));
    v_stack_m78 = v_stack_m50;
    result = RtlpIcWriteRegisterValue(a1, a2, a3, a4);
    goto loc_00BC816A;
loc_00BC7F57:
    result = RtlpIcDecodeModRm(a1, a2, v_stack_p20, a4);
    if (sign_flag) goto loc_00BC81D4;
    if (a2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(a1, a2, v_stack_m58, v_stack_p8);
    if (v_stack_p10 == 0) goto loc_00BC7FAE;
    *(unsigned int *)(*(unsigned __int64 *)(a2)) = (unsigned int)((unsigned int)(0xC000001DULL));
    goto loc_00BC81E3;
loc_00BC7FAE:
    goto loc_00BC7F2A;
loc_00BC7FB7:
    if (((unsigned int)(a1)) > 204) goto loc_00BC81B2;
    if (((unsigned int)(a1)) == 204) goto loc_00BC81CF;
    a1 = (unsigned int)((a1) - (144));
    if (condition_is_equal) goto loc_00BC815F;
    a1 = (unsigned int)((a1) - (12));
    if (condition_is_equal) goto loc_00BC80FA;
    a1 = (unsigned int)((a1) - (38));
    if (condition_is_equal) goto loc_00BC8031;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC804E;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00BC8004;
    if (((unsigned int)(a1)) != 1) goto loc_00BC81CF;
    if (a2 != 0) goto loc_00BC801D;
    goto loc_00BC800D;
loc_00BC8004:
    if (a2 != 0) goto loc_00BC801D;
    *(unsigned __int8 *)(a1 + 1) = 8;
loc_00BC800D:
    result = RtlpIcSetImmediateOperandSize(a1, 16, 32, 32);
loc_00BC801D:
    result = RtlpIcEmulateGroup11Instruction(a1, a2, v_stack_p20, 32);
    goto loc_00BC7A7A;
loc_00BC8031:
    result = RtlpIcFetchInstructionBytes(a1, a1 + 32, 2, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
loc_00BC804E:
    if (a2 == 0) goto loc_00BC7B8C;
    v_stack_m68 = 0;
    v_stack_m70 = 8;
    v_stack_m78 = 0;
    result = RtlpIcAccessMemory(a2, v_stack_m50, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 152), *(unsigned __int8 *)(a2 + 16));
    if (sign_flag) goto loc_00BC81E3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 248) = v_stack_m50;
    result = (*(unsigned __int64 *)(a1 + 32)) + (8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 48))) & ((unsigned int)((unsigned int)(0x100080ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x100080ULL)))) {
        a1 = (int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 1256));
        a3 = 0xFFFEULL;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 248);
        *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a2 + 8) * 1 + 1240) = result;
        result = *(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 8) * 1 + 1250);
        result = (unsigned __int16)((result) & ((unsigned __int16)(a3)));
        result = (unsigned __int16)((result) | (2));
        *(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 8) * 1 + 1250) = (unsigned __int16)(result);
    }
    v_rbx = 0;
    goto loc_00BC81E3;
loc_00BC80FA:
    if (((*(unsigned __int8 *)(a1 + 25)) & (8)) == 0) goto loc_00BC81CF;
    if (a2 == 0) goto loc_00BC7B8C;
    v_stack_m68 = 1;
    v_stack_m70 = 8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 68))) & (0xFCFFFFULL));
    v_stack_m78 = 0;
    v_stack_m50 = result;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 152)) - (8);
    result = RtlpIcAccessMemory(a2, v_stack_m50, a3, *(unsigned __int8 *)(a2 + 16));
    if (sign_flag) goto loc_00BC81E3;
    goto loc_00BC816A;
loc_00BC815F:
    if (((*(unsigned __int8 *)(a1 + 25)) & (1)) != 0) goto loc_00BC81CF;
loc_00BC8165:
    if (a2 == 0) goto loc_00BC81D9;
loc_00BC816A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 48))) & ((unsigned int)((unsigned int)(0x100080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x100080ULL)))) goto loc_00BC81E3;
    *(unsigned __int64 *)((int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 1256)) + *(unsigned __int64 *)(a2 + 8) * 1 + 1240) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 248);
    goto loc_00BC81E3;
loc_00BC81B2:
    a1 = (unsigned int)(((int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 1256))) - (205));
    if (condition_is_equal) goto loc_00BC81CF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC81CF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BC81CF;
    a1 = (unsigned int)((a1) - (10));
    v_r14 = 2;
    if (!(condition_is_equal)) {
        v_r14 = 2;
    }
loc_00BC81D4:
    if (a2 != 0) goto loc_00BC81E3;
loc_00BC81D9:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 248);
    if (!(sign_flag)) {
        result = v_stack_p20;
        *(unsigned __int8 *)(a1 + 24) = (unsigned __int8)(result);
    }
    v_rsp = (v_rsp) + (104);
    return (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL)));
}
```

## 5. (Beta) C Style

```c
int64_t RtlpIcEmulateInstruction(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (104);
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = (uint32_t)(*(uint8_t *)(arg1 + 0x15));
    result = RtlpIcFetchInstructionBytes(Arg1, v_stack_p18, 1, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
    result = (uint8_t)(((uint8_t)(v_stack_p18)) & (240));
    if (((uint8_t)(result)) != 80) goto loc_00BC7A89;
    result = RtlpIcEmulateRegisterPushPop(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_p18)), v_stack_p20);
loc_00BC7A7A:
    if (sign_flag) goto loc_00BC81D4;
    goto loc_00BC8165;
loc_00BC7A89:
    if (((uint8_t)(result)) != 176) goto loc_00BC7AFA;
    if (Arg2 != 0) goto loc_00BC7AAF;
    if ((((uint8_t)((uint32_t)((uint32_t)(Arg1)))) & (8)) == 0) {
        *(uint8_t *)(arg1 + 0x1) = 8;
    }
    result = RtlpIcSetImmediateOperandSize(Arg1, 16, 32, 64);
loc_00BC7AAF:
    result = RtlpIcFetchImmediateOperand(Arg1, Arg2, v_stack_p20, 64);
    if (sign_flag) goto loc_00BC81D4;
    if (Arg2 == 0) goto loc_00BC7B8C;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (7));
    a4 = (uint8_t)((*(uint8_t *)(arg1 + 0x19)) & (1));
    v_stack_m78 = *(uint64_t *)(arg1 + 0x20);
    result = RtlpIcWriteRegisterValue(Arg1, Arg2, (uint32_t)((uint32_t)(local_r14)), a4);
    local_rbx = 0;
    goto loc_00BC816A;
loc_00BC7AFA:
    if ((((uint32_t)(Arg1)) & (0xFFFFFFC4ULL)) != 0) goto loc_00BC7B19;
    result = RtlpIcEmulateGroup0Instruction(Arg1, Arg2, (uint32_t)((uint32_t)(Arg1)), v_stack_p20);
    goto loc_00BC7A7A;
loc_00BC7B19:
    if (((uint32_t)(Arg1)) > 141) goto loc_00BC7FB7;
    if (((uint32_t)(Arg1)) == 141) goto loc_00BC7F57;
    if (((uint32_t)(Arg1)) > 133) goto loc_00BC7CD5;
    if (((uint32_t)(Arg1)) == 133) goto loc_00BC7B6A;
    Arg1 = (uint32_t)((Arg1) - (15));
    if (condition_is_equal) goto loc_00BC7BE2;
    Arg1 = (uint32_t)((Arg1) - (113));
    if (condition_is_equal) goto loc_00BC7BB5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7BAE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7B9A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7B93;
    if (((uint32_t)(Arg1)) != 1) goto loc_00BC81CF;
    if (Arg2 == 0) {
        *(uint8_t *)(arg1 + 0x1) = 8;
    }
    result = RtlpIcDecodeModRm(Arg1, Arg2, v_stack_p20, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
    if (Arg2 != 0) goto loc_00BC7C36;
loc_00BC7B8C:
    local_rbx = 0;
    goto loc_00BC81DD;
loc_00BC7B93:
    if (Arg2 != 0) goto loc_00BC7BCE;
    goto loc_00BC7BA3;
loc_00BC7B9A:
    if (Arg2 != 0) goto loc_00BC7BCE;
    *(uint8_t *)(arg1 + 0x1) = 8;
loc_00BC7BA3:
    goto loc_00BC7BC6;
loc_00BC7BAE:
    if (Arg2 != 0) goto loc_00BC7BCE;
    goto loc_00BC7BBE;
loc_00BC7BB5:
    if (Arg2 != 0) goto loc_00BC7BCE;
    *(uint8_t *)(arg1 + 0x1) = 8;
loc_00BC7BBE:
loc_00BC7BC6:
    result = RtlpIcSetImmediateOperandSize(Arg1, 16, 32, 32);
loc_00BC7BCE:
    result = RtlpIcEmulateGroup1Instruction(Arg1, Arg2, v_stack_p20, 32);
    goto loc_00BC7A7A;
loc_00BC7BE2:
    result = RtlpIcFetchInstructionBytes(Arg1, v_stack_p18, 1, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) - (182));
    if (condition_is_equal) goto loc_00BC7C18;
    if (((uint32_t)(Arg1)) != 1) goto loc_00BC81CF;
loc_00BC7C18:
    a3 = (uint8_t)((v_stack_p18) & (1));
    a3 = (uint8_t)((a3) + (1));
    a3 = (uint8_t)((a3) << (3));
    result = RtlpIcEmulateMovzx(Arg1, Arg2, a3, v_stack_p20);
    goto loc_00BC7A7A;
loc_00BC7C36:
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(Arg1, Arg2, v_stack_m58, v_stack_p8);
    v_stack_m70 = v_stack_m50;
    v_stack_m78 = (uint8_t)(v_stack_p10);
    result = RtlpIcReadOperandValue(Arg1, Arg2, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    a3 = (uint32_t)((*(uint8_t *)(arg1 + 0x1A)) >> (3));
    a4 = (uint8_t)((*(uint8_t *)(arg1 + 0x19)) >> (2));
    a3 = (uint32_t)((a3) & (7));
    a4 = (uint8_t)((a4) & (1));
    v_stack_m78 = 1;
    result = RtlpIcGetRegisterAddressByIndex(Arg1, Arg2, a3, a4);
    result = RtlpIcSignExtendOperandValue(Arg1, *(uint64_t *)(result), a3, a4);
    v_stack_m48 = result;
    a3 = (result) & (v_stack_m50);
    result = RtlpIcSetFlagsZeroSignParity(Arg1, Arg2, a3, a4);
    goto loc_00BC816A;
loc_00BC7CD5:
    Arg1 = (uint32_t)((Arg1) - (134));
    if (condition_is_equal) goto loc_00BC7E43;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7E4C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7D88;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7D91;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC7D0B;
    if (((uint32_t)(Arg1)) == 1) goto loc_00BC7D14;
    goto loc_00BC81CF;
loc_00BC7D0B:
    if (Arg2 == 0) {
        *(uint8_t *)(arg1 + 0x1) = 8;
    }
    result = RtlpIcDecodeModRm(Arg1, Arg2, v_stack_p20, a4);
    if (sign_flag) goto loc_00BC81D4;
    if (Arg2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(Arg1, Arg2, v_stack_m58, v_stack_p8);
    v_stack_m70 = v_stack_m48;
    v_stack_m78 = (uint8_t)(v_stack_p10);
    result = RtlpIcReadOperandValue(Arg1, Arg2, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    goto loc_00BC7F2A;
loc_00BC7D88:
    if (Arg2 == 0) {
        *(uint8_t *)(arg1 + 0x1) = 8;
    }
    result = RtlpIcDecodeModRm(Arg1, Arg2, v_stack_p20, v_stack_p8);
    if (sign_flag) goto loc_00BC81D4;
    if (Arg2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(Arg1, Arg2, v_stack_m58, v_stack_p8);
    a3 = (uint32_t)((*(uint8_t *)(arg1 + 0x1A)) >> (3));
    a4 = (uint8_t)((*(uint8_t *)(arg1 + 0x19)) >> (2));
    a3 = (uint32_t)((a3) & (7));
    a4 = (uint8_t)((a4) & (1));
    v_stack_m78 = 1;
    result = RtlpIcGetRegisterAddressByIndex(Arg1, Arg2, a3, a4);
    result = RtlpIcSignExtendOperandValue(Arg1, *(uint64_t *)(result), a3, a4);
    v_stack_m48 = result;
    v_stack_p18 = result;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x1)) >> (3));
    v_stack_m68 = 1;
    v_stack_m70 = (uint8_t)(result);
    v_stack_m78 = (uint8_t)(v_stack_p10);
    result = RtlpIcAccessMemory(Arg2, v_stack_p18, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    goto loc_00BC816A;
loc_00BC7E43:
    if (Arg2 == 0) {
        *(uint8_t *)(arg1 + 0x1) = 8;
    }
    result = RtlpIcDecodeModRm(Arg1, Arg2, v_stack_p20, v_stack_p8);
    if (sign_flag) goto loc_00BC81D4;
    if (Arg2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(Arg1, Arg2, v_stack_m58, v_stack_p8);
    v_stack_m70 = v_stack_m50;
    v_stack_m78 = (uint8_t)(v_stack_p10);
    result = RtlpIcReadOperandValue(Arg1, Arg2, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
    a3 = (uint32_t)((*(uint8_t *)(arg1 + 0x1A)) >> (3));
    a4 = (uint8_t)((*(uint8_t *)(arg1 + 0x19)) >> (2));
    a3 = (uint32_t)((a3) & (7));
    a4 = (uint8_t)((a4) & (1));
    v_stack_m78 = 1;
    result = RtlpIcGetRegisterAddressByIndex(Arg1, Arg2, a3, a4);
    result = RtlpIcSignExtendOperandValue(Arg1, *(uint64_t *)(result), a3, a4);
    v_stack_m48 = result;
    v_stack_p10 = result;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x1)) >> (3));
    v_stack_m68 = 1;
    v_stack_m70 = (uint8_t)(result);
    v_stack_m78 = (uint8_t)(v_stack_p10);
    result = RtlpIcAccessMemory(Arg2, v_stack_p10, v_stack_m58, v_stack_p8);
    if (sign_flag) goto loc_00BC81E3;
loc_00BC7F2A:
    a4 = (uint8_t)((*(uint8_t *)(arg1 + 0x19)) >> (2));
    a3 = (uint32_t)((*(uint8_t *)(arg1 + 0x1A)) >> (3));
    a4 = (uint8_t)((a4) & (1));
    a3 = (uint32_t)((a3) & (7));
    v_stack_m78 = v_stack_m50;
    result = RtlpIcWriteRegisterValue(Arg1, Arg2, a3, a4);
    goto loc_00BC816A;
loc_00BC7F57:
    result = RtlpIcDecodeModRm(Arg1, Arg2, v_stack_p20, a4);
    if (sign_flag) goto loc_00BC81D4;
    if (Arg2 == 0) goto loc_00BC7B8C;
    v_stack_m78 = v_stack_p10;
    result = RtlpIcDecodeModRmOperand(Arg1, Arg2, v_stack_m58, v_stack_p8);
    if (v_stack_p10 == 0) goto loc_00BC7FAE;
    *(uint32_t *)(*(uint64_t *)(Arg2)) = (uint32_t)((uint32_t)(0xC000001DULL));
    goto loc_00BC81E3;
loc_00BC7FAE:
    goto loc_00BC7F2A;
loc_00BC7FB7:
    if (((uint32_t)(Arg1)) > 204) goto loc_00BC81B2;
    if (((uint32_t)(Arg1)) == 204) goto loc_00BC81CF;
    Arg1 = (uint32_t)((Arg1) - (144));
    if (condition_is_equal) goto loc_00BC815F;
    Arg1 = (uint32_t)((Arg1) - (12));
    if (condition_is_equal) goto loc_00BC80FA;
    Arg1 = (uint32_t)((Arg1) - (38));
    if (condition_is_equal) goto loc_00BC8031;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC804E;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00BC8004;
    if (((uint32_t)(Arg1)) != 1) goto loc_00BC81CF;
    if (Arg2 != 0) goto loc_00BC801D;
    goto loc_00BC800D;
loc_00BC8004:
    if (Arg2 != 0) goto loc_00BC801D;
    *(uint8_t *)(arg1 + 0x1) = 8;
loc_00BC800D:
    result = RtlpIcSetImmediateOperandSize(Arg1, 16, 32, 32);
loc_00BC801D:
    result = RtlpIcEmulateGroup11Instruction(Arg1, Arg2, v_stack_p20, 32);
    goto loc_00BC7A7A;
loc_00BC8031:
    result = RtlpIcFetchInstructionBytes(Arg1, Arg1 + 32, 2, v_stack_p20);
    if (sign_flag) goto loc_00BC81D4;
loc_00BC804E:
    if (Arg2 == 0) goto loc_00BC7B8C;
    v_stack_m68 = 0;
    v_stack_m70 = 8;
    v_stack_m78 = 0;
    result = RtlpIcAccessMemory(Arg2, v_stack_m50, *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x98), *(uint8_t *)(Arg2 + 0x10));
    if (sign_flag) goto loc_00BC81E3;
    *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0xF8) = v_stack_m50;
    result = (*(uint64_t *)(arg1 + 0x20)) + (8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x30))) & ((uint32_t)((uint32_t)(0x100080ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x100080ULL)))) {
        Arg1 = (int32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x4E8));
        a3 = 0xFFFEULL;
        result = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0xF8);
        *(uint64_t *)(arg1 + *(uint64_t *)(Arg2 + 0x8) * 1 + 0x4D8) = result;
        result = *(uint16_t *)(arg1 + *(uint64_t *)(Arg2 + 0x8) * 1 + 0x4E2);
        result = (uint16_t)((result) & ((uint16_t)(a3)));
        result = (uint16_t)((result) | (2));
        *(uint16_t *)(arg1 + *(uint64_t *)(Arg2 + 0x8) * 1 + 0x4E2) = (uint16_t)(result);
    }
    local_rbx = 0;
    goto loc_00BC81E3;
loc_00BC80FA:
    if (((*(uint8_t *)(arg1 + 0x19)) & (8)) == 0) goto loc_00BC81CF;
    if (Arg2 == 0) goto loc_00BC7B8C;
    v_stack_m68 = 1;
    v_stack_m70 = 8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x44))) & (0xFCFFFFULL));
    v_stack_m78 = 0;
    v_stack_m50 = result;
    a3 = (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x98)) - (8);
    result = RtlpIcAccessMemory(Arg2, v_stack_m50, a3, *(uint8_t *)(Arg2 + 0x10));
    if (sign_flag) goto loc_00BC81E3;
    goto loc_00BC816A;
loc_00BC815F:
    if (((*(uint8_t *)(arg1 + 0x19)) & (1)) != 0) goto loc_00BC81CF;
loc_00BC8165:
    if (Arg2 == 0) goto loc_00BC81D9;
loc_00BC816A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x30))) & ((uint32_t)((uint32_t)(0x100080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x100080ULL)))) goto loc_00BC81E3;
    *(uint64_t *)((int32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x4E8)) + *(uint64_t *)(Arg2 + 0x8) * 1 + 0x4D8) = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0xF8);
    goto loc_00BC81E3;
loc_00BC81B2:
    Arg1 = (uint32_t)(((int32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x4E8))) - (205));
    if (condition_is_equal) goto loc_00BC81CF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC81CF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BC81CF;
    Arg1 = (uint32_t)((Arg1) - (10));
    local_r14 = 2;
    if (!(condition_is_equal)) {
        local_r14 = 2;
    }
loc_00BC81D4:
    if (Arg2 != 0) goto loc_00BC81E3;
loc_00BC81D9:
    result = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0xF8);
    if (!(sign_flag)) {
        result = v_stack_p20;
        *(uint8_t *)(arg1 + 0x18) = (uint8_t)(result);
    }
    local_rsp = (local_rsp) + (104);
    return (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x1` | `8` | `W` |
| `Arg1` | `+ 0x15` | `8` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x18` | `8` | `W` |
| `Arg1` | `+ 0x19` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=tracesup&rva=0x00BC7A08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
