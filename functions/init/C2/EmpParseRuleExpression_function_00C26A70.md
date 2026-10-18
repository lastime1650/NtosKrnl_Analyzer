# EmpParseRuleExpression

- RVA: `0x00C26A70`–`0x00C26FB8` (길이 `1,352` bytes)
- VA: `0x0000000140C26A70`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5BB4`
- 디코드: `362`개 명령, `1,352/1,352` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C26AC5` → [EmpInfParseGetValueFromSectionAndKeyName](EmpInfParseGetValueFromSectionAndKeyName_function_00C264B4.md) (function, `0x00C264B4`)
- `0x00C26AF0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26B3F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26B5E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26B75` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26BCF` → [EmpRuleParserStackPop](EmpRuleParserStackPop_function_00C27ED4.md) (function, `0x00C27ED4`)
- `0x00C26BF4` → [EmpRuleParserStackPop](EmpRuleParserStackPop_function_00C27ED4.md) (function, `0x00C27ED4`)
- `0x00C26C13` → [EmpRuleParserStackPush](EmpRuleParserStackPush_function_00C27F2C.md) (function, `0x00C27F2C`)
- `0x00C26C35` → [EmpParseRuleTerm](EmpParseRuleTerm_function_00C26FC0.md) (function, `0x00C26FC0`)
- `0x00C26D14` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26D3E` → [EmpInfParseSearchDependencyList](EmpInfParseSearchDependencyList_function_00C26558.md) (function, `0x00C26558`)
- `0x00C26D57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26D80` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26DAA` → [EmpInfParseSearchDependencyList](EmpInfParseSearchDependencyList_function_00C26558.md) (function, `0x00C26558`)
- `0x00C26DC3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26DF9` → [EmpRuleParserStackPush](EmpRuleParserStackPush_function_00C27F2C.md) (function, `0x00C27F2C`)
- `0x00C26E1E` → [CmpGetSectionLineIndex](CmpGetSectionLineIndex_function_00C283C4.md) (function, `0x00C283C4`)
- `0x00C26E40` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C26E5F` → [EmpRuleParserStackPop](EmpRuleParserStackPop_function_00C27ED4.md) (function, `0x00C27ED4`)
- `0x00C26EA9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26EBA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26EDC` → [EmpRuleParserStackPop](EmpRuleParserStackPop_function_00C27ED4.md) (function, `0x00C27ED4`)
- `0x00C26EF4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26F27` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26F34` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26F70` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26F7D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C26F98` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EmpParseRules](EmpParseRules_function_00C2745C.md) at `0x00C27701`

### Static image references
- `0x00C26AB0` → RVA `0x00C796A0` (` ?? ::PBOPGDP::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00C26AF0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26B3F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26B5E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26B75` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26D14` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26D57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26D80` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26DC3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26E40` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C26EA9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26EBA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26EF4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26F27` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26F34` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26F70` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26F7D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C26F98` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C26A70  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C26A75  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00C26A7A  55                              push rbp
00C26A7B  56                              push rsi
00C26A7C  57                              push rdi
00C26A7D  41 54                           push r12
00C26A7F  41 55                           push r13
00C26A81  41 56                           push r14
00C26A83  41 57                           push r15
00C26A85  48 8B EC                        mov rbp, rsp
00C26A88  48 83 EC 50                     sub rsp, 0x50
00C26A8C  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
00C26A90  48 8B C1                        mov rax, rcx
00C26A93  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
00C26A98  48 8D 4D E4                     lea rcx, [rbp - 0x1c]
00C26A9C  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
00C26AA1  49 8B F0                        mov rsi, r8
00C26AA4  83 65 58 00                     and dword ptr [rbp + 0x58], 0
00C26AA8  4C 8B C2                        mov r8, rdx
00C26AAB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C26AB0  48 8D 15 E9 2B 05 00            lea rdx, [rip + 0x52be9]
00C26AB7  33 DB                           xor ebx, ebx
00C26AB9  48 8B C8                        mov rcx, rax
00C26ABC  21 5D E0                        and dword ptr [rbp - 0x20], ebx
00C26ABF  45 33 F6                        xor r14d, r14d
00C26AC2  45 33 ED                        xor r13d, r13d
00C26AC5  E8 EA F9 FF FF                  call 0x140c264b4
00C26ACA  4C 8B E0                        mov r12, rax
00C26ACD  48 85 C0                        test rax, rax
00C26AD0  75 0A                           jne 0x140c26adc
00C26AD2  BB 25 02 00 C0                  mov ebx, 0xc0000225
00C26AD7  E9 5D 04 00 00                  jmp 0x140c26f39
00C26ADC  41 BF 00 01 00 00               mov r15d, 0x100
00C26AE2  BA 10 00 00 00                  mov edx, 0x10
00C26AE7  41 8B CF                        mov ecx, r15d
00C26AEA  41 B8 45 4D 73 74               mov r8d, 0x74734d45
00C26AF0  E8 FB B5 F5 FF                  call 0x140b820f0
00C26AF5  48 8B F8                        mov rdi, rax
00C26AF8  48 85 C0                        test rax, rax
00C26AFB  74 06                           je 0x140c26b03
00C26AFD  21 18                           and dword ptr [rax], ebx
00C26AFF  48 21 58 08                     and qword ptr [rax + 8], rbx
00C26B03  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
00C26B08  83 E9 25                        sub ecx, 0x25
00C26B0B  0F 84 0C 01 00 00               je 0x140c26c1d
00C26B11  83 E9 01                        sub ecx, 1
00C26B14  74 12                           je 0x140c26b28
00C26B16  83 E9 19                        sub ecx, 0x19
00C26B19  0F 84 FE 00 00 00               je 0x140c26c1d
00C26B1F  83 F9 3D                        cmp ecx, 0x3d
00C26B22  0F 85 54 03 00 00               jne 0x140c26e7c
00C26B28  83 3F 02                        cmp dword ptr [rdi], 2
00C26B2B  0F 82 4B 03 00 00               jb 0x140c26e7c
00C26B31  BA 38 00 00 00                  mov edx, 0x38
00C26B36  41 B8 45 4D 73 74               mov r8d, 0x74734d45
00C26B3C  49 8B CF                        mov rcx, r15
00C26B3F  E8 AC B5 F5 FF                  call 0x140b820f0
00C26B44  4C 8B F0                        mov r14, rax
00C26B47  48 85 C0                        test rax, rax
00C26B4A  0F 84 25 03 00 00               je 0x140c26e75
00C26B50  BA 20 00 00 00                  mov edx, 0x20
00C26B55  41 B8 45 4D 73 74               mov r8d, 0x74734d45
00C26B5B  49 8B CF                        mov rcx, r15
00C26B5E  E8 8D B5 F5 FF                  call 0x140b820f0
00C26B63  BA 20 00 00 00                  mov edx, 0x20
00C26B68  49 89 46 08                     mov qword ptr [r14 + 8], rax
00C26B6C  41 B8 45 4D 73 74               mov r8d, 0x74734d45
00C26B72  49 8B CF                        mov rcx, r15
00C26B75  E8 76 B5 F5 FF                  call 0x140b820f0
00C26B7A  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00C26B7E  49 89 46 20                     mov qword ptr [r14 + 0x20], rax
00C26B82  48 85 C9                        test rcx, rcx
00C26B85  0F 84 EA 02 00 00               je 0x140c26e75
00C26B8B  48 85 C0                        test rax, rax
00C26B8E  0F 84 E1 02 00 00               je 0x140c26e75
00C26B94  41 8A 04 24                     mov al, byte ptr [r12]
00C26B98  4D 8D 4E 30                     lea r9, [r14 + 0x30]
00C26B9C  41 88 06                        mov byte ptr [r14], al
00C26B9F  44 21 69 10                     and dword ptr [rcx + 0x10], r13d
00C26BA3  48 8B CF                        mov rcx, rdi
00C26BA6  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00C26BAA  4C 21 68 18                     and qword ptr [rax + 0x18], r13
00C26BAE  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00C26BB2  44 21 68 10                     and dword ptr [rax + 0x10], r13d
00C26BB6  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00C26BBA  4C 21 68 18                     and qword ptr [rax + 0x18], r13
00C26BBE  49 8D 46 28                     lea rax, [r14 + 0x28]
00C26BC2  49 8B 56 20                     mov rdx, qword ptr [r14 + 0x20]
00C26BC6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C26BCB  4C 8D 42 08                     lea r8, [rdx + 8]
00C26BCF  E8 00 13 00 00                  call 0x140c27ed4
00C26BD4  84 C0                           test al, al
00C26BD6  0F 84 92 02 00 00               je 0x140c26e6e
00C26BDC  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00C26BE0  49 8D 46 10                     lea rax, [r14 + 0x10]
00C26BE4  4D 8D 4E 18                     lea r9, [r14 + 0x18]
00C26BE8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C26BED  48 8B CF                        mov rcx, rdi
00C26BF0  4C 8D 42 08                     lea r8, [rdx + 8]
00C26BF4  E8 DB 12 00 00                  call 0x140c27ed4
00C26BF9  84 C0                           test al, al
00C26BFB  0F 84 6D 02 00 00               je 0x140c26e6e
00C26C01  44 21 6C 24 20                  and dword ptr [rsp + 0x20], r13d
00C26C06  45 33 C9                        xor r9d, r9d
00C26C09  4D 8B C6                        mov r8, r14
00C26C0C  48 8B CF                        mov rcx, rdi
00C26C0F  41 8D 51 02                     lea edx, [r9 + 2]
00C26C13  E8 14 13 00 00                  call 0x140c27f2c
00C26C18  E9 E7 01 00 00                  jmp 0x140c26e04
00C26C1D  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00C26C21  48 8D 45 58                     lea rax, [rbp + 0x58]
00C26C25  4C 8D 4D E8                     lea r9, [rbp - 0x18]
00C26C29  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C26C2E  4C 8D 45 F0                     lea r8, [rbp - 0x10]
00C26C32  49 8B D4                        mov rdx, r12
00C26C35  E8 86 03 00 00                  call 0x140c26fc0
00C26C3A  8B D8                           mov ebx, eax
00C26C3C  85 C0                           test eax, eax
00C26C3E  0F 88 3D 02 00 00               js 0x140c26e81
00C26C44  41 80 3C 24 3F                  cmp byte ptr [r12], 0x3f
00C26C49  4C 8B 7D F0                     mov r15, qword ptr [rbp - 0x10]
00C26C4D  75 0A                           jne 0x140c26c59
00C26C4F  41 8B 57 38                     mov edx, dword ptr [r15 + 0x38]
00C26C53  45 8B 4F 3C                     mov r9d, dword ptr [r15 + 0x3c]
00C26C57  EB 08                           jmp 0x140c26c61
00C26C59  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
00C26C5D  45 8B 4F 2C                     mov r9d, dword ptr [r15 + 0x2c]
00C26C61  41 8D 04 11                     lea eax, [r9 + rdx]
00C26C65  3B 45 58                        cmp eax, dword ptr [rbp + 0x58]
00C26C68  0F 87 0E 02 00 00               ja 0x140c26e7c
00C26C6E  4C 8B 5D E8                     mov r11, qword ptr [rbp - 0x18]
00C26C72  45 33 C0                        xor r8d, r8d
00C26C75  44 3B C2                        cmp r8d, edx
00C26C78  73 12                           jae 0x140c26c8c
00C26C7A  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
00C26C7D  43 39 04 83                     cmp dword ptr [r11 + r8*4], eax
00C26C81  0F 83 F5 01 00 00               jae 0x140c26e7c
00C26C87  41 FF C0                        inc r8d
00C26C8A  EB E9                           jmp 0x140c26c75
00C26C8C  44 8B C2                        mov r8d, edx
00C26C8F  45 8D 14 11                     lea r10d, [r9 + rdx]
00C26C93  45 3B C2                        cmp r8d, r10d
00C26C96  73 15                           jae 0x140c26cad
00C26C98  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
00C26C9B  41 8B C8                        mov ecx, r8d
00C26C9E  41 39 04 8B                     cmp dword ptr [r11 + rcx*4], eax
00C26CA2  0F 83 D4 01 00 00               jae 0x140c26e7c
00C26CA8  41 FF C0                        inc r8d
00C26CAB  EB E6                           jmp 0x140c26c93
00C26CAD  45 8A 1C 24                     mov r11b, byte ptr [r12]
00C26CB1  45 8D 04 11                     lea r8d, [r9 + rdx]
00C26CB5  45 8D 14 11                     lea r10d, [r9 + rdx]
00C26CB9  44 3B 45 58                     cmp r8d, dword ptr [rbp + 0x58]
00C26CBD  73 3F                           jae 0x140c26cfe
00C26CBF  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00C26CC3  42 8B 0C 81                     mov ecx, dword ptr [rcx + r8*4]
00C26CC7  3B 4E 30                        cmp ecx, dword ptr [rsi + 0x30]
00C26CCA  0F 83 AC 01 00 00               jae 0x140c26e7c
00C26CD0  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
00C26CD4  41 8B D0                        mov edx, r8d
00C26CD7  41 2B D2                        sub edx, r10d
00C26CDA  4C 8B 0C C8                     mov r9, qword ptr [rax + rcx*8]
00C26CDE  41 80 FB 3F                     cmp r11b, 0x3f
00C26CE2  75 07                           jne 0x140c26ceb
00C26CE4  4D 3B 4C D7 48                  cmp r9, qword ptr [r15 + rdx*8 + 0x48]
00C26CE9  EB 08                           jmp 0x140c26cf3
00C26CEB  49 8B 47 38                     mov rax, qword ptr [r15 + 0x38]
00C26CEF  4C 3B 0C D0                     cmp r9, qword ptr [rax + rdx*8]
00C26CF3  0F 85 83 01 00 00               jne 0x140c26e7c
00C26CF9  41 FF C0                        inc r8d
00C26CFC  EB BB                           jmp 0x140c26cb9
00C26CFE  B9 00 01 00 00                  mov ecx, 0x100
00C26D03  41 B8 45 4D 69 74               mov r8d, 0x74694d45
00C26D09  41 80 FB 3F                     cmp r11b, 0x3f
00C26D0D  75 6C                           jne 0x140c26d7b
00C26D0F  BA 10 00 00 00                  mov edx, 0x10
00C26D14  E8 D7 B3 F5 FF                  call 0x140b820f0
00C26D19  48 85 C0                        test rax, rax
00C26D1C  0F 84 53 01 00 00               je 0x140c26e75
00C26D22  48 8D 48 08                     lea rcx, [rax + 8]
00C26D26  4C 89 38                        mov qword ptr [rax], r15
00C26D29  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
00C26D2D  4D 8D 67 30                     lea r12, [r15 + 0x30]
00C26D31  48 89 01                        mov qword ptr [rcx], rax
00C26D34  48 8B D6                        mov rdx, rsi
00C26D37  48 89 4E 40                     mov qword ptr [rsi + 0x40], rcx
00C26D3B  49 8B CC                        mov rcx, r12
00C26D3E  E8 15 F8 FF FF                  call 0x140c26558
00C26D43  84 C0                           test al, al
00C26D45  75 30                           jne 0x140c26d77
00C26D47  BA 18 00 00 00                  mov edx, 0x18
00C26D4C  B9 00 01 00 00                  mov ecx, 0x100
00C26D51  41 B8 45 4D 69 74               mov r8d, 0x74694d45
00C26D57  E8 94 B3 F5 FF                  call 0x140b820f0
00C26D5C  48 85 C0                        test rax, rax
00C26D5F  0F 84 10 01 00 00               je 0x140c26e75
00C26D65  48 89 30                        mov qword ptr [rax], rsi
00C26D68  48 8D 48 08                     lea rcx, [rax + 8]
00C26D6C  49 8B 04 24                     mov rax, qword ptr [r12]
00C26D70  48 89 01                        mov qword ptr [rcx], rax
00C26D73  49 89 0C 24                     mov qword ptr [r12], rcx
00C26D77  33 D2                           xor edx, edx
00C26D79  EB 6D                           jmp 0x140c26de8
00C26D7B  BA 18 00 00 00                  mov edx, 0x18
00C26D80  E8 6B B3 F5 FF                  call 0x140b820f0
00C26D85  48 85 C0                        test rax, rax
00C26D88  0F 84 E7 00 00 00               je 0x140c26e75
00C26D8E  48 8D 48 08                     lea rcx, [rax + 8]
00C26D92  4C 89 38                        mov qword ptr [rax], r15
00C26D95  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
00C26D99  4D 8D 67 20                     lea r12, [r15 + 0x20]
00C26D9D  48 89 01                        mov qword ptr [rcx], rax
00C26DA0  48 8B D6                        mov rdx, rsi
00C26DA3  48 89 4E 48                     mov qword ptr [rsi + 0x48], rcx
00C26DA7  49 8B CC                        mov rcx, r12
00C26DAA  E8 A9 F7 FF FF                  call 0x140c26558
00C26DAF  84 C0                           test al, al
00C26DB1  75 30                           jne 0x140c26de3
00C26DB3  BA 18 00 00 00                  mov edx, 0x18
00C26DB8  B9 00 01 00 00                  mov ecx, 0x100
00C26DBD  41 B8 45 4D 69 74               mov r8d, 0x74694d45
00C26DC3  E8 28 B3 F5 FF                  call 0x140b820f0
00C26DC8  48 85 C0                        test rax, rax
00C26DCB  0F 84 A4 00 00 00               je 0x140c26e75
00C26DD1  48 89 30                        mov qword ptr [rax], rsi
00C26DD4  48 8D 48 08                     lea rcx, [rax + 8]
00C26DD8  49 8B 04 24                     mov rax, qword ptr [r12]
00C26DDC  48 89 01                        mov qword ptr [rcx], rax
00C26DDF  49 89 0C 24                     mov qword ptr [r12], rcx
00C26DE3  BA 01 00 00 00                  mov edx, 1
00C26DE8  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00C26DEB  4D 8B C7                        mov r8, r15
00C26DEE  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
00C26DF2  48 8B CF                        mov rcx, rdi
00C26DF5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C26DF9  E8 2E 11 00 00                  call 0x140c27f2c
00C26DFE  41 BF 00 01 00 00               mov r15d, 0x100
00C26E04  8B 45 E0                        mov eax, dword ptr [rbp - 0x20]
00C26E07  48 8D 15 92 28 05 00            lea rdx, [rip + 0x52892]
00C26E0E  44 8B 45 E4                     mov r8d, dword ptr [rbp - 0x1c]
00C26E12  FF C0                           inc eax
00C26E14  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00C26E18  44 8B C8                        mov r9d, eax
00C26E1B  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00C26E1E  E8 A1 15 00 00                  call 0x140c283c4
00C26E23  4C 8B E0                        mov r12, rax
00C26E26  48 85 C0                        test rax, rax
00C26E29  0F 85 D4 FC FF FF               jne 0x140c26b03
00C26E2F  83 3F 01                        cmp dword ptr [rdi], 1
00C26E32  75 48                           jne 0x140c26e7c
00C26E34  8D 50 20                        lea edx, [rax + 0x20]
00C26E37  41 B8 45 4D 69 74               mov r8d, 0x74694d45
00C26E3D  49 8B CF                        mov rcx, r15
00C26E40  E8 AB B2 F5 FF                  call 0x140b820f0
00C26E45  48 8B D0                        mov rdx, rax
00C26E48  4C 8B E8                        mov r13, rax
00C26E4B  48 8D 48 10                     lea rcx, [rax + 0x10]
00C26E4F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C26E54  4C 8D 48 18                     lea r9, [rax + 0x18]
00C26E58  48 8B CF                        mov rcx, rdi
00C26E5B  4C 8D 40 08                     lea r8, [rax + 8]
00C26E5F  E8 70 10 00 00                  call 0x140c27ed4
00C26E64  84 C0                           test al, al
00C26E66  74 06                           je 0x140c26e6e
00C26E68  4C 89 6E 60                     mov qword ptr [rsi + 0x60], r13
00C26E6C  EB 13                           jmp 0x140c26e81
00C26E6E  BB 25 02 00 C0                  mov ebx, 0xc0000225
00C26E73  EB 0C                           jmp 0x140c26e81
00C26E75  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00C26E7A  EB 05                           jmp 0x140c26e81
00C26E7C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00C26E81  48 85 FF                        test rdi, rdi
00C26E84  75 5B                           jne 0x140c26ee1
00C26E86  41 BF 45 4D 73 74               mov r15d, 0x74734d45
00C26E8C  85 DB                           test ebx, ebx
00C26E8E  0F 89 09 01 00 00               jns 0x140c26f9d
00C26E94  4D 85 F6                        test r14, r14
00C26E97  0F 84 9C 00 00 00               je 0x140c26f39
00C26E9D  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00C26EA1  48 85 C9                        test rcx, rcx
00C26EA4  74 08                           je 0x140c26eae
00C26EA6  41 8B D7                        mov edx, r15d
00C26EA9  E8 C2 B9 F5 FF                  call 0x140b82870
00C26EAE  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00C26EB2  48 85 C9                        test rcx, rcx
00C26EB5  74 08                           je 0x140c26ebf
00C26EB7  41 8B D7                        mov edx, r15d
00C26EBA  E8 B1 B9 F5 FF                  call 0x140b82870
00C26EBF  41 8B D7                        mov edx, r15d
00C26EC2  49 8B CE                        mov rcx, r14
00C26EC5  EB 6D                           jmp 0x140c26f34
00C26EC7  48 8D 45 58                     lea rax, [rbp + 0x58]
00C26ECB  4C 8D 4D F0                     lea r9, [rbp - 0x10]
00C26ECF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C26ED4  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00C26ED8  48 8D 55 E4                     lea rdx, [rbp - 0x1c]
00C26EDC  E8 F3 0F 00 00                  call 0x140c27ed4
00C26EE1  48 83 7F 08 00                  cmp qword ptr [rdi + 8], 0
00C26EE6  48 8B CF                        mov rcx, rdi
00C26EE9  75 DC                           jne 0x140c26ec7
00C26EEB  41 BF 45 4D 73 74               mov r15d, 0x74734d45
00C26EF1  41 8B D7                        mov edx, r15d
00C26EF4  E8 77 B9 F5 FF                  call 0x140b82870
00C26EF9  EB 91                           jmp 0x140c26e8c
00C26EFB  48 8B 01                        mov rax, qword ptr [rcx]
00C26EFE  48 8D 79 F8                     lea rdi, [rcx - 8]
00C26F02  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
00C26F06  48 8B 17                        mov rdx, qword ptr [rdi]
00C26F09  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
00C26F0D  48 8D 48 F8                     lea rcx, [rax - 8]
00C26F11  48 39 31                        cmp qword ptr [rcx], rsi
00C26F14  75 16                           jne 0x140c26f2c
00C26F16  48 85 C0                        test rax, rax
00C26F19  74 07                           je 0x140c26f22
00C26F1B  48 8B 00                        mov rax, qword ptr [rax]
00C26F1E  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
00C26F22  BA 45 4D 69 74                  mov edx, 0x74694d45
00C26F27  E8 44 B9 F5 FF                  call 0x140b82870
00C26F2C  BA 45 4D 69 74                  mov edx, 0x74694d45
00C26F31  48 8B CF                        mov rcx, rdi
00C26F34  E8 37 B9 F5 FF                  call 0x140b82870
00C26F39  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
00C26F3D  48 85 C9                        test rcx, rcx
00C26F40  75 B9                           jne 0x140c26efb
00C26F42  EB 3E                           jmp 0x140c26f82
00C26F44  48 8B 01                        mov rax, qword ptr [rcx]
00C26F47  48 8D 79 F8                     lea rdi, [rcx - 8]
00C26F4B  48 89 46 40                     mov qword ptr [rsi + 0x40], rax
00C26F4F  48 8B 17                        mov rdx, qword ptr [rdi]
00C26F52  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00C26F56  48 8D 48 F8                     lea rcx, [rax - 8]
00C26F5A  48 39 31                        cmp qword ptr [rcx], rsi
00C26F5D  75 16                           jne 0x140c26f75
00C26F5F  48 85 C0                        test rax, rax
00C26F62  74 07                           je 0x140c26f6b
00C26F64  48 8B 00                        mov rax, qword ptr [rax]
00C26F67  48 89 42 30                     mov qword ptr [rdx + 0x30], rax
00C26F6B  BA 45 4D 69 74                  mov edx, 0x74694d45
00C26F70  E8 FB B8 F5 FF                  call 0x140b82870
00C26F75  BA 45 4D 69 74                  mov edx, 0x74694d45
00C26F7A  48 8B CF                        mov rcx, rdi
00C26F7D  E8 EE B8 F5 FF                  call 0x140b82870
00C26F82  48 8B 4E 40                     mov rcx, qword ptr [rsi + 0x40]
00C26F86  48 85 C9                        test rcx, rcx
00C26F89  75 B9                           jne 0x140c26f44
00C26F8B  4D 85 ED                        test r13, r13
00C26F8E  74 0D                           je 0x140c26f9d
00C26F90  BA 45 4D 69 74                  mov edx, 0x74694d45
00C26F95  49 8B CD                        mov rcx, r13
00C26F98  E8 D3 B8 F5 FF                  call 0x140b82870
00C26F9D  8B C3                           mov eax, ebx
00C26F9F  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00C26FA7  48 83 C4 50                     add rsp, 0x50
00C26FAB  41 5F                           pop r15
00C26FAD  41 5E                           pop r14
00C26FAF  41 5D                           pop r13
00C26FB1  41 5C                           pop r12
00C26FB3  5F                              pop rdi
00C26FB4  5E                              pop rsi
00C26FB5  5D                              pop rbp
00C26FB6  C3                              ret
00C26FB7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpParseRuleExpression(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m68 = v_stack_m54;
    v_rbx = 0;
    v_r14 = 0;
    v_r13 = 0;
    result = EmpInfParseGetValueFromSectionAndKeyName(a1, v_rip + 338921, a2, a4);
    if (result != 0) goto loc_00C26ADC;
    goto loc_00C26F39;
loc_00C26ADC:
    result = ExAllocatePool2(256, 16, (unsigned int)(0x74734D45ULL), a4);
    if (result != 0) {
    }
    a1 = (unsigned int)(((__int8)(*(unsigned __int8 *)(result))) - (37));
    if (condition_is_equal) goto loc_00C26C1D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00C26B28;
    a1 = (unsigned int)((a1) - (25));
    if (condition_is_equal) goto loc_00C26C1D;
    if (((unsigned int)(a1)) != 61) goto loc_00C26E7C;
loc_00C26B28:
    if ((*(unsigned int *)(result)) < 2) goto loc_00C26E7C;
    result = ExAllocatePool2(256, 56, (unsigned int)(0x74734D45ULL), a4);
    if (result == 0) goto loc_00C26E75;
    result = ExAllocatePool2(256, 32, (unsigned int)(0x74734D45ULL), a4);
    *(unsigned __int64 *)(result + 8) = result;
    result = ExAllocatePool2(256, 32, (unsigned int)(0x74734D45ULL), a4);
    *(unsigned __int64 *)(result + 32) = result;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00C26E75;
    if (result == 0) goto loc_00C26E75;
    *(unsigned __int8 *)(result) = (unsigned __int8)(*(unsigned __int8 *)(result));
    v_stack_m68 = result + 40;
    result = EmpRuleParserStackPop(result, *(unsigned __int64 *)(result + 32), *(unsigned __int64 *)(result + 32) + 8, result + 48);
    if ((unsigned __int8)(result) == 0) goto loc_00C26E6E;
    v_stack_m68 = result + 16;
    result = EmpRuleParserStackPop(result, *(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 8) + 8, result + 24);
    if ((unsigned __int8)(result) == 0) goto loc_00C26E6E;
    a4 = 0;
    result = EmpRuleParserStackPush(result, a4 + 2, result, a4);
    goto loc_00C26E04;
loc_00C26C1D:
    v_stack_m68 = v_stack_p20;
    result = EmpParseRuleTerm(v_stack_p8, result, v_stack_m48, v_stack_m50);
    if (sign_flag) goto loc_00C26E81;
    if ((*(unsigned __int8 *)(result)) != 63) goto loc_00C26C59;
    goto loc_00C26C61;
loc_00C26C59:
loc_00C26C61:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1)) > v_stack_p20) goto loc_00C26E7C;
    a3 = 0;
loc_00C26C75:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 40))))) goto loc_00C26C8C;
    if ((*(unsigned int *)(v_stack_m50 + a3 * 4)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40))))) goto loc_00C26E7C;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00C26C75;
loc_00C26C8C:
loc_00C26C93:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 40)))))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1))) goto loc_00C26CAD;
    if ((*(unsigned int *)(v_stack_m50 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 40)))))) * 4)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 44))))) goto loc_00C26E7C;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 40))))) + 1);
    goto loc_00C26C93;
loc_00C26CAD:
loc_00C26CB9:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1)) >= v_stack_p20) goto loc_00C26CFE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)))) >= (*(unsigned int *)(a3 + 48))) goto loc_00C26E7C;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1)));
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) != 63) goto loc_00C26CEB;
    goto loc_00C26CF3;
loc_00C26CEB:
loc_00C26CF3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48 + 56) + a2 * 8))) goto loc_00C26E7C;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1) + 1);
    goto loc_00C26CB9;
loc_00C26CFE:
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) != 63) goto loc_00C26D7B;
    result = ExAllocatePool2(256, 16, (unsigned int)(0x74694D45ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(unsigned __int64 *)(result) = v_stack_m48;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a3 + 64);
    *(unsigned __int64 *)(a3 + 64) = result + 8;
    result = EmpInfParseSearchDependencyList(v_stack_m48 + 48, a3, (unsigned int)(0x74694D45ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8));
    if ((unsigned __int8)(result) != 0) goto loc_00C26D77;
    result = ExAllocatePool2(256, 24, (unsigned int)(0x74694D45ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(unsigned __int64 *)(result) = a3;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_stack_m48 + 48);
    *(unsigned __int64 *)(v_stack_m48 + 48) = result + 8;
loc_00C26D77:
    a2 = 0;
    goto loc_00C26DE8;
loc_00C26D7B:
    result = ExAllocatePool2(result + 8, 24, (unsigned int)(0x74694D45ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(unsigned __int64 *)(result) = v_stack_m48;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a3 + 72);
    *(unsigned __int64 *)(a3 + 72) = result + 8;
    result = EmpInfParseSearchDependencyList(v_stack_m48 + 32, a3, (unsigned int)(0x74694D45ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8));
    if ((unsigned __int8)(result) != 0) goto loc_00C26DE3;
    result = ExAllocatePool2(256, 24, (unsigned int)(0x74694D45ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 56) + (unsigned int)(*(unsigned int *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m48 + 44)) + (unsigned int)(*(unsigned int *)(v_stack_m48 + 40)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(unsigned __int64 *)(result) = a3;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_stack_m48 + 32);
    *(unsigned __int64 *)(v_stack_m48 + 32) = result + 8;
loc_00C26DE3:
loc_00C26DE8:
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_p20));
    result = EmpRuleParserStackPush(result, 1, v_stack_m48, v_stack_m50);
loc_00C26E04:
    result = (unsigned int)(((unsigned int)(v_stack_m58)) + 1);
    v_stack_m58 = (unsigned int)(result);
    result = CmpGetSectionLineIndex(v_stack_p8, v_rip + 338066, (unsigned int)(v_stack_m54), (unsigned int)((unsigned int)(result)));
    if (result != 0) goto loc_00C26B03;
    if ((*(unsigned int *)(result)) != 1) goto loc_00C26E7C;
    result = ExAllocatePool2(256, result + 32, (unsigned int)(0x74694D45ULL), (unsigned int)((unsigned int)(result)));
    v_stack_m68 = result + 16;
    result = EmpRuleParserStackPop(result, result, result + 8, result + 24);
    if ((unsigned __int8)(result) == 0) goto loc_00C26E6E;
    *(unsigned __int64 *)(a3 + 96) = result;
    goto loc_00C26E81;
loc_00C26E6E:
    goto loc_00C26E81;
loc_00C26E75:
    goto loc_00C26E81;
loc_00C26E7C:
loc_00C26E81:
    if (result != 0) goto loc_00C26EE1;
loc_00C26E8C:
    if (!sign_flag) goto loc_00C26F9D;
    if (result == 0) goto loc_00C26F39;
    if (*(unsigned __int64 *)(result + 8) != 0) {
        a2 = (unsigned int)((unsigned int)(0x74734D45ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 8), a2, result + 8, result + 24);
    }
    if (*(unsigned __int64 *)(result + 32) != 0) {
        a2 = (unsigned int)((unsigned int)(0x74734D45ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 32), a2, result + 8, result + 24);
    }
    goto loc_00C26F34;
loc_00C26EC7:
    v_stack_m68 = v_stack_p20;
    result = EmpRuleParserStackPop(result, v_stack_m54, v_stack_m50, v_stack_m48);
loc_00C26EE1:
    if ((*(unsigned __int64 *)(result + 8)) != 0) goto loc_00C26EC7;
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0x74734D45ULL))), v_stack_m50, v_stack_m48);
    goto loc_00C26E8C;
loc_00C26EFB:
    *(unsigned __int64 *)(a3 + 72) = *(unsigned __int64 *)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result - 8) + 32) - 8)) != a3) goto loc_00C26F2C;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(result - 8) + 32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result - 8) + 32) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result - 8) + 32));
        *(unsigned __int64 *)(*(unsigned __int64 *)(result - 8) + 32) = result;
    }
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(result - 8) + 32) - 8, (unsigned int)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F2C:
loc_00C26F34:
    result = ExFreePoolWithTag(result - 8, (unsigned int)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F39:
    if (*(unsigned __int64 *)(a3 + 72) != 0) goto loc_00C26EFB;
    goto loc_00C26F82;
loc_00C26F44:
    *(unsigned __int64 *)(a3 + 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) - 8) + 48) - 8)) != a3) goto loc_00C26F75;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) - 8) + 48);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) - 8) + 48) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) - 8) + 48));
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) - 8) + 48) = result;
    }
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) - 8) + 48) - 8, (unsigned int)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F75:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a3 + 72) - 8, (unsigned int)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F82:
    if (*(unsigned __int64 *)(a3 + 64) != 0) goto loc_00C26F44;
    if (result != 0) {
        a2 = 0x74694D45ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m50, v_stack_m48);
    }
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t EmpParseRuleExpression(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m68 = v_stack_m54;
    local_rbx = 0;
    local_r14 = 0;
    local_r13 = 0;
    result = EmpInfParseGetValueFromSectionAndKeyName(Arg1, v_rip + 338921, Arg2, a4);
    if (result != 0) goto loc_00C26ADC;
    goto loc_00C26F39;
loc_00C26ADC:
    result = ExAllocatePool2(256, 16, (uint32_t)(0x74734D45ULL), a4);
    if (result != 0) {
    }
    Arg1 = (uint32_t)(((int8_t)(*(uint8_t *)(result))) - (37));
    if (condition_is_equal) goto loc_00C26C1D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00C26B28;
    Arg1 = (uint32_t)((Arg1) - (25));
    if (condition_is_equal) goto loc_00C26C1D;
    if (((uint32_t)(Arg1)) != 61) goto loc_00C26E7C;
loc_00C26B28:
    if ((*(uint32_t *)(result)) < 2) goto loc_00C26E7C;
    result = ExAllocatePool2(256, 56, (uint32_t)(0x74734D45ULL), a4);
    if (result == 0) goto loc_00C26E75;
    result = ExAllocatePool2(256, 32, (uint32_t)(0x74734D45ULL), a4);
    *(uint64_t *)(result + 0x8) = result;
    result = ExAllocatePool2(256, 32, (uint32_t)(0x74734D45ULL), a4);
    *(uint64_t *)(result + 0x20) = result;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00C26E75;
    if (result == 0) goto loc_00C26E75;
    *(uint8_t *)(result) = (uint8_t)(*(uint8_t *)(result));
    v_stack_m68 = result + 40;
    result = EmpRuleParserStackPop(result, *(uint64_t *)(result + 0x20), *(uint64_t *)(result + 0x20) + 8, result + 48);
    if ((uint8_t)(result) == 0) goto loc_00C26E6E;
    v_stack_m68 = result + 16;
    result = EmpRuleParserStackPop(result, *(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x8) + 8, result + 24);
    if ((uint8_t)(result) == 0) goto loc_00C26E6E;
    a4 = 0;
    result = EmpRuleParserStackPush(result, a4 + 2, result, a4);
    goto loc_00C26E04;
loc_00C26C1D:
    v_stack_m68 = v_stack_p20;
    result = EmpParseRuleTerm(v_stack_p8, result, v_stack_m48, v_stack_m50);
    if (sign_flag) goto loc_00C26E81;
    if ((*(uint8_t *)(result)) != 63) goto loc_00C26C59;
    goto loc_00C26C61;
loc_00C26C59:
loc_00C26C61:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1)) > v_stack_p20) goto loc_00C26E7C;
    Arg3 = 0;
loc_00C26C75:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28))))) goto loc_00C26C8C;
    if ((*(uint32_t *)(v_stack_m50 + arg3 * 4)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x28))))) goto loc_00C26E7C;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00C26C75;
loc_00C26C8C:
loc_00C26C93:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)))))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1))) goto loc_00C26CAD;
    if ((*(uint32_t *)(v_stack_m50 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)))))) * 4)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x2C))))) goto loc_00C26E7C;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28))))) + 1);
    goto loc_00C26C93;
loc_00C26CAD:
loc_00C26CB9:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1)) >= v_stack_p20) goto loc_00C26CFE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)))) >= (*(uint32_t *)(arg3 + 0x30))) goto loc_00C26E7C;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1)));
    if (((uint8_t)(*(uint8_t *)(result))) != 63) goto loc_00C26CEB;
    goto loc_00C26CF3;
loc_00C26CEB:
loc_00C26CF3:
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m48 + 0x38) + Arg2 * 8))) goto loc_00C26E7C;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1) + 1);
    goto loc_00C26CB9;
loc_00C26CFE:
    if (((uint8_t)(*(uint8_t *)(result))) != 63) goto loc_00C26D7B;
    result = ExAllocatePool2(256, 16, (uint32_t)(0x74694D45ULL), *(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(uint64_t *)(result) = v_stack_m48;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg3 + 0x40);
    *(uint64_t *)(arg3 + 0x40) = result + 8;
    result = EmpInfParseSearchDependencyList(v_stack_m48 + 48, Arg3, (uint32_t)(0x74694D45ULL), *(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8));
    if ((uint8_t)(result) != 0) goto loc_00C26D77;
    result = ExAllocatePool2(256, 24, (uint32_t)(0x74694D45ULL), *(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(void **)(result) = Arg3;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_stack_m48 + 0x30);
    *(uint64_t *)(v_stack_m48 + 0x30) = result + 8;
loc_00C26D77:
    Arg2 = 0;
    goto loc_00C26DE8;
loc_00C26D7B:
    result = ExAllocatePool2(result + 8, 24, (uint32_t)(0x74694D45ULL), *(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(uint64_t *)(result) = v_stack_m48;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg3 + 0x48);
    *(uint64_t *)(arg3 + 0x48) = result + 8;
    result = EmpInfParseSearchDependencyList(v_stack_m48 + 32, Arg3, (uint32_t)(0x74694D45ULL), *(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8));
    if ((uint8_t)(result) != 0) goto loc_00C26DE3;
    result = ExAllocatePool2(256, 24, (uint32_t)(0x74694D45ULL), *(uint64_t *)(*(uint64_t *)(arg3 + 0x38) + (uint32_t)(*(uint32_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x2C)) + (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x28)) * 1 * 4)) * 8));
    if (result == 0) goto loc_00C26E75;
    *(void **)(result) = Arg3;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_stack_m48 + 0x20);
    *(uint64_t *)(v_stack_m48 + 0x20) = result + 8;
loc_00C26DE3:
loc_00C26DE8:
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_p20));
    result = EmpRuleParserStackPush(result, 1, v_stack_m48, v_stack_m50);
loc_00C26E04:
    result = (uint32_t)(((uint32_t)(v_stack_m58)) + 1);
    v_stack_m58 = (uint32_t)(result);
    result = CmpGetSectionLineIndex(v_stack_p8, v_rip + 338066, (uint32_t)(v_stack_m54), (uint32_t)((uint32_t)(result)));
    if (result != 0) goto loc_00C26B03;
    if ((*(uint32_t *)(result)) != 1) goto loc_00C26E7C;
    result = ExAllocatePool2(256, result + 32, (uint32_t)(0x74694D45ULL), (uint32_t)((uint32_t)(result)));
    v_stack_m68 = result + 16;
    result = EmpRuleParserStackPop(result, result, result + 8, result + 24);
    if ((uint8_t)(result) == 0) goto loc_00C26E6E;
    *(uint64_t *)(arg3 + 0x60) = result;
    goto loc_00C26E81;
loc_00C26E6E:
    goto loc_00C26E81;
loc_00C26E75:
    goto loc_00C26E81;
loc_00C26E7C:
loc_00C26E81:
    if (result != 0) goto loc_00C26EE1;
loc_00C26E8C:
    if (!sign_flag) goto loc_00C26F9D;
    if (result == 0) goto loc_00C26F39;
    if (*(uint64_t *)(result + 0x8) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x74734D45ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x8), Arg2, result + 8, result + 24);
    }
    if (*(uint64_t *)(result + 0x20) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x74734D45ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x20), Arg2, result + 8, result + 24);
    }
    goto loc_00C26F34;
loc_00C26EC7:
    v_stack_m68 = v_stack_p20;
    result = EmpRuleParserStackPop(result, v_stack_m54, v_stack_m50, v_stack_m48);
loc_00C26EE1:
    if ((*(uint64_t *)(result + 0x8)) != 0) goto loc_00C26EC7;
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0x74734D45ULL))), v_stack_m50, v_stack_m48);
    goto loc_00C26E8C;
loc_00C26EFB:
    *(uint64_t *)(arg3 + 0x48) = *(uint64_t *)(result);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result - 0x8) + 0x20) - 0x8)) != Arg3) goto loc_00C26F2C;
    result = *(uint64_t *)(*(uint64_t *)(result - 0x8) + 0x20);
    if (*(uint64_t *)(*(uint64_t *)(result - 0x8) + 0x20) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result - 0x8) + 0x20));
        *(uint64_t *)(*(uint64_t *)(result - 0x8) + 0x20) = result;
    }
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(result - 0x8) + 0x20) - 8, (uint32_t)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F2C:
loc_00C26F34:
    result = ExFreePoolWithTag(result - 8, (uint32_t)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F39:
    if (*(uint64_t *)(arg3 + 0x48) != 0) goto loc_00C26EFB;
    goto loc_00C26F82;
loc_00C26F44:
    *(uint64_t *)(arg3 + 0x40) = *(uint64_t *)(*(uint64_t *)(arg3 + 0x48));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48) - 0x8) + 0x30) - 0x8)) != Arg3) goto loc_00C26F75;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48) - 0x8) + 0x30);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48) - 0x8) + 0x30) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48) - 0x8) + 0x30));
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48) - 0x8) + 0x30) = result;
    }
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48) - 0x8) + 0x30) - 8, (uint32_t)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F75:
    result = ExFreePoolWithTag(*(uint64_t *)(arg3 + 0x48) - 8, (uint32_t)(0x74694D45ULL), v_stack_m50, v_stack_m48);
loc_00C26F82:
    if (*(uint64_t *)(arg3 + 0x40) != 0) goto loc_00C26F44;
    if (result != 0) {
        Arg2 = 0x74694D45ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m50, v_stack_m48);
    }
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x28` | `32` | `R` |
| `Arg3` | `+ 0x2C` | `32` | `R` |
| `Arg3` | `+ 0x30` | `32` | `R` |
| `Arg3` | `+ 0x38` | `64` | `R` |
| `Arg3` | `+ 0x40` | `64` | `R` |
| `Arg3` | `+ 0x40` | `64` | `W` |
| `Arg3` | `+ 0x48` | `64` | `R` |
| `Arg3` | `+ 0x48` | `64` | `W` |
| `Arg3` | `+ 0x60` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C26A70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
