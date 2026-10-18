# KeQueryLogicalProcessorRelationship

- RVA: `0x002CEA60`–`0x002CF6A9` (길이 `3,145` bytes)
- VA: `0x00000001402CEA60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006F634`
- 디코드: `748`개 명령, `3,145/3,145` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002CEA9D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002CED25` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002CED55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x002CED88` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002CEDCC` → [KeAndGroupAffinityEx](KeAndGroupAffinityEx_function_002CF6B0.md) (function, `0x002CF6B0`)
- `0x002CEDED` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x002CEE4D` → [KeQueryNodeActiveAffinityEx](../25/KeQueryNodeActiveAffinityEx_function_00256740.md) (function, `0x00256740`)
- `0x002CEEF1` → [KiCopyAffinityEx](KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x002CEF41` → [KiTryPopulateLogicalProcessorInformation](KiTryPopulateLogicalProcessorInformation_function_002CF724.md) (function, `0x002CF724`)
- `0x002CF000` → [KeQueryMaximumProcessorCountEx](../26/KeQueryMaximumProcessorCountEx_function_00264D60.md) (function, `0x00264D60`)
- `0x002CF00B` → [KeQueryActiveProcessorCountEx](../24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x002CF14E` → [KeGetProcessorIndexFromNumber](../2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x002CF17E` → [KiCopyAffinityEx](KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x002CF1CC` → [KiTryPopulateLogicalProcessorInformation](KiTryPopulateLogicalProcessorInformation_function_002CF724.md) (function, `0x002CF724`)
- `0x002CF23F` → [KiCopyAffinityEx](KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x002CF24C` → [KiAndAffinityExNoResult](KiAndAffinityExNoResult_function_002CF84C.md) (function, `0x002CF84C`)
- `0x002CF26C` → [KeOrAffinityEx2](KeOrAffinityEx2_function_002CF930.md) (function, `0x002CF930`)
- `0x002CF50C` → [KeOrAffinityEx2](KeOrAffinityEx2_function_002CF930.md) (function, `0x002CF930`)
- `0x002CF59C` → [KeGetNodePrimarySubNode](../43/KeGetNodePrimarySubNode_function_0043EFF4.md) (function, `0x0043EFF4`)
- `0x002CF5DB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002CF5F1` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)

### Direct callers
- [ExpQuerySystemInformation](../../page/A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A596EB`

### Static image references
- `0x002CEAA6` → RVA `0x00FC5014` (`ALMOSTRO`; read)
- `0x002CEBCB` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x002CEBE6` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002CEE23` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x002CEF8A` → RVA `0x00FC5018` (`ALMOSTRO`; read)
- `0x002CF22A` → RVA `0x00FC6FF4` (`ALMOSTRO`; read)
- `0x002CF37A` → RVA `0x00F231B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002CED25` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002CED55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002CEC78` → [sub_006DCD34](../6D/Unknown_function_006DCD34.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002CEA60  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002CEA65  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
002CEA6A  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
002CEA6E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002CEA73  55                              push rbp
002CEA74  53                              push rbx
002CEA75  56                              push rsi
002CEA76  57                              push rdi
002CEA77  41 54                           push r12
002CEA79  41 55                           push r13
002CEA7B  41 56                           push r14
002CEA7D  41 57                           push r15
002CEA7F  48 8D 6C 24 E8                  lea rbp, [rsp - 0x18]
002CEA84  48 81 EC 18 01 00 00            sub rsp, 0x118
002CEA8B  8B DA                           mov ebx, edx
002CEA8D  4C 8B E1                        mov r12, rcx
002CEA90  33 D2                           xor edx, edx
002CEA92  48 8D 4D C0                     lea rcx, [rbp - 0x40]
002CEA96  49 8B F9                        mov rdi, r9
002CEA99  44 8D 42 50                     lea r8d, [rdx + 0x50]
002CEA9D  E8 9E 81 3F 00                  call 0x1406c6c40
002CEAA2  8B 07                           mov eax, dword ptr [rdi]
002CEAA4  33 F6                           xor esi, esi
002CEAA6  44 0F B7 35 66 65 CF 00         movzx r14d, word ptr [rip + 0xcf6566]
002CEAAE  44 8B EE                        mov r13d, esi
002CEAB1  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
002CEAB5  8B C6                           mov eax, esi
002CEAB7  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
002CEABB  B9 EC 00 00 00                  mov ecx, 0xec
002CEAC0  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
002CEAC4  8D 56 01                        lea edx, [rsi + 1]
002CEAC7  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
002CEACB  4E 8D 3C F5 00 00 00 00         lea r15, [r14*8]
002CEAD3  49 8D 7F 08                     lea rdi, [r15 + 8]
002CEAD7  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEADD  0F 85 2E 0B 00 00               jne 0x1402cf611
002CEAE3  B8 06 00 00 00                  mov eax, 6
002CEAE8  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEAEE  74 15                           je 0x1402ceb05
002CEAF0  EB 0F                           jmp 0x1402ceb01
002CEAF2  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEAF8  74 E9                           je 0x1402ceae3
002CEAFA  8B C2                           mov eax, edx
002CEAFC  83 FB 02                        cmp ebx, 2
002CEAFF  74 E2                           je 0x1402ceae3
002CEB01  85 DB                           test ebx, ebx
002CEB03  75 0E                           jne 0x1402ceb13
002CEB05  FF C0                           inc eax
002CEB07  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEB0D  0F 84 0A 0A 00 00               je 0x1402cf51d
002CEB13  83 FB 03                        cmp ebx, 3
002CEB16  0F 84 01 0A 00 00               je 0x1402cf51d
002CEB1C  83 FB 05                        cmp ebx, 5
002CEB1F  0F 85 A6 05 00 00               jne 0x1402cf0cb
002CEB25  FF C0                           inc eax
002CEB27  85 C0                           test eax, eax
002CEB29  0F 85 12 02 00 00               jne 0x1402ced41
002CEB2F  49 8B C5                        mov rax, r13
002CEB32  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEB38  74 0A                           je 0x1402ceb44
002CEB3A  83 FB 07                        cmp ebx, 7
002CEB3D  77 45                           ja 0x1402ceb84
002CEB3F  0F A3 D9                        bt ecx, ebx
002CEB42  73 40                           jae 0x1402ceb84
002CEB44  4C 89 6D C0                     mov qword ptr [rbp - 0x40], r13
002CEB48  4A 8D 04 2F                     lea rax, [rdi + r13]
002CEB4C  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEB52  74 05                           je 0x1402ceb59
002CEB54  83 FB 02                        cmp ebx, 2
002CEB57  75 2B                           jne 0x1402ceb84
002CEB59  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
002CEB5D  48 03 C7                        add rax, rdi
002CEB60  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
002CEB64  48 03 C7                        add rax, rdi
002CEB67  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
002CEB6B  48 03 C7                        add rax, rdi
002CEB6E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
002CEB72  48 03 C7                        add rax, rdi
002CEB75  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
002CEB79  48 03 C7                        add rax, rdi
002CEB7C  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEB82  74 04                           je 0x1402ceb88
002CEB84  85 DB                           test ebx, ebx
002CEB86  75 13                           jne 0x1402ceb9b
002CEB88  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
002CEB8C  48 03 C7                        add rax, rdi
002CEB8F  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEB95  0F 84 47 09 00 00               je 0x1402cf4e2
002CEB9B  83 FB 03                        cmp ebx, 3
002CEB9E  0F 84 3E 09 00 00               je 0x1402cf4e2
002CEBA4  83 FB 05                        cmp ebx, 5
002CEBA7  0F 84 7B 0A 00 00               je 0x1402cf628
002CEBAD  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEBB3  0F 84 6B 09 00 00               je 0x1402cf524
002CEBB9  83 FB 07                        cmp ebx, 7
002CEBBC  0F 84 62 09 00 00               je 0x1402cf524
002CEBC2  4D 85 E4                        test r12, r12
002CEBC5  0F 85 80 05 00 00               jne 0x1402cf14b
002CEBCB  44 8B 25 AE 7E CF 00            mov r12d, dword ptr [rip + 0xcf7eae]
002CEBD2  8B FE                           mov edi, esi
002CEBD4  41 FF CC                        dec r12d
002CEBD7  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
002CEBDB  4C 8B 7D C0                     mov r15, qword ptr [rbp - 0x40]
002CEBDF  0F 57 C0                        xorps xmm0, xmm0
002CEBE2  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
002CEBE6  48 8D 15 13 14 D3 FF            lea rdx, [rip - 0x2cebed]
002CEBED  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
002CEBF2  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
002CEBF6  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
002CEBFA  41 3B FC                        cmp edi, r12d
002CEBFD  0F 87 C7 00 00 00               ja 0x1402cecca
002CEC03  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
002CEC07  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
002CEC0B  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
002CEC10  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002CEC14  48 8B 45 00                     mov rax, qword ptr [rbp]
002CEC18  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
002CEC1C  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
002CEC20  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
002CEC24  0F B7 45 98                     movzx eax, word ptr [rbp - 0x68]
002CEC28  66 89 44 24 54                  mov word ptr [rsp + 0x54], ax
002CEC2D  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002CEC32  EB 0E                           jmp 0x1402cec42
002CEC34  0F 1F 40 00                     nop dword ptr [rax]
002CEC38  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002CEC40  33 F6                           xor esi, esi
002CEC42  8B C7                           mov eax, edi
002CEC44  4C 8B AC C2 40 8C FC 00         mov r13, qword ptr [rdx + rax*8 + 0xfc8c40]
002CEC4C  83 FB 03                        cmp ebx, 3
002CEC4F  0F 84 8D 02 00 00               je 0x1402ceee2
002CEC55  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEC5B  0F 84 81 02 00 00               je 0x1402ceee2
002CEC61  85 DB                           test ebx, ebx
002CEC63  0F 84 40 01 00 00               je 0x1402ceda9
002CEC69  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEC6F  0F 84 34 01 00 00               je 0x1402ceda9
002CEC75  83 FB 05                        cmp ebx, 5
002CEC78  0F 84 B6 E0 40 00               je 0x1406dcd34
002CEC7E  83 FB 07                        cmp ebx, 7
002CEC81  0F 84 E8 04 00 00               je 0x1402cf16f
002CEC87  81 FB FF FF 00 00               cmp ebx, 0xffff
002CEC8D  0F 84 DC 04 00 00               je 0x1402cf16f
002CEC93  83 FB 02                        cmp ebx, 2
002CEC96  0F 84 61 05 00 00               je 0x1402cf1fd
002CEC9C  81 FB FF FF 00 00               cmp ebx, 0xffff
002CECA2  0F 84 55 05 00 00               je 0x1402cf1fd
002CECA8  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002CECAD  48 8D 15 4C 13 D3 FF            lea rdx, [rip - 0x2cecb4]
002CECB4  FF C7                           inc edi
002CECB6  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
002CECBA  41 3B FC                        cmp edi, r12d
002CECBD  76 81                           jbe 0x1402cec40
002CECBF  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
002CECC3  48 8D 15 36 13 D3 FF            lea rdx, [rip - 0x2cecca]
002CECCA  83 FB 01                        cmp ebx, 1
002CECCD  0F 84 59 06 00 00               je 0x1402cf32c
002CECD3  83 FB 06                        cmp ebx, 6
002CECD6  0F 84 41 01 00 00               je 0x1402cee1d
002CECDC  81 FB FF FF 00 00               cmp ebx, 0xffff
002CECE2  0F 84 35 01 00 00               je 0x1402cee1d
002CECE8  4C 8B 75 60                     mov r14, qword ptr [rbp + 0x60]
002CECEC  33 F6                           xor esi, esi
002CECEE  83 FB 04                        cmp ebx, 4
002CECF1  0F 84 8E 02 00 00               je 0x1402cef85
002CECF7  81 FB FF FF 00 00               cmp ebx, 0xffff
002CECFD  0F 84 56 08 00 00               je 0x1402cf559
002CED03  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
002CED08  8B 5C 24 64                     mov ebx, dword ptr [rsp + 0x64]
002CED0C  85 DB                           test ebx, ebx
002CED0E  0F 84 5E 02 00 00               je 0x1402cef72
002CED14  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
002CED18  44 89 00                        mov dword ptr [rax], r8d
002CED1B  4D 85 ED                        test r13, r13
002CED1E  74 0A                           je 0x1402ced2a
002CED20  33 D2                           xor edx, edx
002CED22  49 8B CD                        mov rcx, r13
002CED25  E8 46 3B 8B 00                  call 0x140b82870
002CED2A  8B C3                           mov eax, ebx
002CED2C  48 81 C4 18 01 00 00            add rsp, 0x118
002CED33  41 5F                           pop r15
002CED35  41 5E                           pop r14
002CED37  41 5D                           pop r13
002CED39  41 5C                           pop r12
002CED3B  5F                              pop rdi
002CED3C  5E                              pop rsi
002CED3D  5B                              pop rbx
002CED3E  5D                              pop rbp
002CED3F  C3                              ret
002CED40  CC                              int3
002CED41  8B D0                           mov edx, eax
002CED43  B9 40 00 00 00                  mov ecx, 0x40
002CED48  48 0F AF D7                     imul rdx, rdi
002CED4C  41 B8 4B 51 4C 50               mov r8d, 0x504c514b
002CED52  44 8B E0                        mov r12d, eax
002CED55  E8 96 33 8B 00                  call 0x140b820f0
002CED5A  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
002CED5E  4C 8B E8                        mov r13, rax
002CED61  48 85 C0                        test rax, rax
002CED64  0F 84 28 08 00 00               je 0x1402cf592
002CED6A  48 8D 70 04                     lea rsi, [rax + 4]
002CED6E  48 8D 4E 04                     lea rcx, [rsi + 4]
002CED72  66 C7 46 FC 01 00               mov word ptr [rsi - 4], 1
002CED78  4D 8B C7                        mov r8, r15
002CED7B  66 44 89 76 FE                  mov word ptr [rsi - 2], r14w
002CED80  33 D2                           xor edx, edx
002CED82  C7 06 00 00 00 00               mov dword ptr [rsi], 0
002CED88  E8 B3 7E 3F 00                  call 0x1406c6c40
002CED8D  48 03 F7                        add rsi, rdi
002CED90  49 83 EC 01                     sub r12, 1
002CED94  75 D8                           jne 0x1402ced6e
002CED96  8B 5D 68                        mov ebx, dword ptr [rbp + 0x68]
002CED99  33 F6                           xor esi, esi
002CED9B  4C 8B 65 60                     mov r12, qword ptr [rbp + 0x60]
002CED9F  B9 EC 00 00 00                  mov ecx, 0xec
002CEDA4  E9 86 FD FF FF                  jmp 0x1402ceb2f
002CEDA9  41 0F B6 85 D0 00 00 00         movzx eax, byte ptr [r13 + 0xd0]
002CEDB1  48 8D 55 90                     lea rdx, [rbp - 0x70]
002CEDB5  49 8B B5 60 8E 00 00            mov rsi, qword ptr [r13 + 0x8e60]
002CEDBC  45 33 C0                        xor r8d, r8d
002CEDBF  66 89 44 24 54                  mov word ptr [rsp + 0x54], ax
002CEDC4  66 89 45 98                     mov word ptr [rbp - 0x68], ax
002CEDC8  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
002CEDCC  E8 DF 08 00 00                  call 0x1402cf6b0
002CEDD1  48 83 7D 60 00                  cmp qword ptr [rbp + 0x60], 0
002CEDD6  75 08                           jne 0x1402cede0
002CEDD8  85 C0                           test eax, eax
002CEDDA  0F 85 95 FE FF FF               jne 0x1402cec75
002CEDE0  0F B7 54 24 54                  movzx edx, word ptr [rsp + 0x54]
002CEDE5  4C 8B C6                        mov r8, rsi
002CEDE8  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002CEDED  E8 CE C8 F8 FF                  call 0x14025b6c0
002CEDF2  49 39 B5 C8 00 00 00            cmp qword ptr [r13 + 0xc8], rsi
002CEDF9  0F 95 C0                        setne al
002CEDFC  41 83 C6 30                     add r14d, 0x30
002CEE00  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
002CEE05  44 3B 74 24 60                  cmp r14d, dword ptr [rsp + 0x60]
002CEE0A  0F 86 DF 02 00 00               jbe 0x1402cf0ef
002CEE10  C7 44 24 64 04 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000004
002CEE18  E9 58 FE FF FF                  jmp 0x1402cec75
002CEE1D  4C 8B 75 60                     mov r14, qword ptr [rbp + 0x60]
002CEE21  33 F6                           xor esi, esi
002CEE23  66 3B 35 D6 61 CF 00            cmp si, word ptr [rip + 0xcf61d6]
002CEE2A  8B FE                           mov edi, esi
002CEE2C  0F 83 BC FE FF FF               jae 0x1402cecee
002CEE32  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
002CEE37  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
002CEE3B  4D 85 F6                        test r14, r14
002CEE3E  0F 85 23 07 00 00               jne 0x1402cf567
002CEE44  45 33 C0                        xor r8d, r8d
002CEE47  49 8B D7                        mov rdx, r15
002CEE4A  0F B7 CF                        movzx ecx, di
002CEE4D  E8 EE 78 F8 FF                  call 0x140256740
002CEE52  45 0F B7 0F                     movzx r9d, word ptr [r15]
002CEE56  4C 8D 25 A3 11 D3 FF            lea r12, [rip - 0x2cee5d]
002CEE5D  8B C7                           mov eax, edi
002CEE5F  44 0F B7 C6                     movzx r8d, si
002CEE63  0F B7 D6                        movzx edx, si
002CEE66  49 8B 84 C4 C0 F6 FC 00         mov rax, qword ptr [r12 + rax*8 + 0xfcf6c0]
002CEE6E  44 0F B6 50 0C                  movzx r10d, byte ptr [rax + 0xc]
002CEE73  66 41 3B F1                     cmp si, r9w
002CEE77  73 40                           jae 0x1402ceeb9
002CEE79  0F B7 C2                        movzx eax, dx
002CEE7C  49 39 74 C7 08                  cmp qword ptr [r15 + rax*8 + 8], rsi
002CEE81  74 04                           je 0x1402cee87
002CEE83  66 41 FF C0                     inc r8w
002CEE87  66 FF C2                        inc dx
002CEE8A  66 41 3B D1                     cmp dx, r9w
002CEE8E  72 E9                           jb 0x1402cee79
002CEE90  66 45 85 C0                     test r8w, r8w
002CEE94  74 23                           je 0x1402ceeb9
002CEE96  41 0F B7 D0                     movzx edx, r8w
002CEE9A  C1 E2 04                        shl edx, 4
002CEE9D  83 C2 27                        add edx, 0x27
002CEEA0  83 E2 F8                        and edx, 0xfffffff8
002CEEA3  44 03 EA                        add r13d, edx
002CEEA6  44 3B 6C 24 60                  cmp r13d, dword ptr [rsp + 0x60]
002CEEAB  0F 86 98 01 00 00               jbe 0x1402cf049
002CEEB1  C7 44 24 64 04 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000004
002CEEB9  48 8D 15 40 11 D3 FF            lea rdx, [rip - 0x2ceec0]
002CEEC0  0F B7 05 39 61 CF 00            movzx eax, word ptr [rip + 0xcf6139]
002CEEC7  FF C7                           inc edi
002CEEC9  3B F8                           cmp edi, eax
002CEECB  0F 82 6A FF FF FF               jb 0x1402cee3b
002CEED1  8B 5D 68                        mov ebx, dword ptr [rbp + 0x68]
002CEED4  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
002CEED9  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
002CEEDD  E9 0C FE FF FF                  jmp 0x1402cecee
002CEEE2  41 0F B7 57 02                  movzx edx, word ptr [r15 + 2]
002CEEE7  4D 8D 85 10 8C 00 00            lea r8, [r13 + 0x8c10]
002CEEEE  49 8B CF                        mov rcx, r15
002CEEF1  E8 6A F9 FF FF                  call 0x1402ce860
002CEEF6  48 83 7D 60 00                  cmp qword ptr [rbp + 0x60], 0
002CEEFB  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
002CEF00  4C 8B 75 70                     mov r14, qword ptr [rbp + 0x70]
002CEF04  41 B9 03 00 00 00               mov r9d, 3
002CEF0A  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
002CEF0E  41 0F 95 C0                     setne r8b
002CEF12  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002CEF17  49 8B CF                        mov rcx, r15
002CEF1A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
002CEF1F  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
002CEF23  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002CEF28  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
002CEF2C  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
002CEF30  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
002CEF34  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
002CEF38  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002CEF3C  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
002CEF41  E8 DE 07 00 00                  call 0x1402cf724
002CEF46  03 74 24 58                     add esi, dword ptr [rsp + 0x58]
002CEF4A  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
002CEF4E  85 C0                           test eax, eax
002CEF50  0F 88 96 02 00 00               js 0x1402cf1ec
002CEF56  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
002CEF5A  85 C0                           test eax, eax
002CEF5C  74 07                           je 0x1402cef65
002CEF5E  4C 03 F0                        add r14, rax
002CEF61  4C 89 75 70                     mov qword ptr [rbp + 0x70], r14
002CEF65  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002CEF6A  44 8B F6                        mov r14d, esi
002CEF6D  E9 EF FC FF FF                  jmp 0x1402cec61
002CEF72  45 85 C0                        test r8d, r8d
002CEF75  0F 85 99 FD FF FF               jne 0x1402ced14
002CEF7B  BB 01 00 00 C0                  mov ebx, 0xc0000001
002CEF80  E9 8F FD FF FF                  jmp 0x1402ced14
002CEF85  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
002CEF8A  0F B7 15 87 60 CF 00            movzx edx, word ptr [rip + 0xcf6087]
002CEF91  8D 04 52                        lea eax, [rdx + rdx*2]
002CEF94  C1 E0 04                        shl eax, 4
002CEF97  83 C0 27                        add eax, 0x27
002CEF9A  83 E0 F8                        and eax, 0xfffffff8
002CEF9D  44 03 C0                        add r8d, eax
002CEFA0  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
002CEFA5  44 3B 44 24 60                  cmp r8d, dword ptr [rsp + 0x60]
002CEFAA  0F 87 35 01 00 00               ja 0x1402cf0e5
002CEFB0  4C 8B 4D 70                     mov r9, qword ptr [rbp + 0x70]
002CEFB4  0F 57 C0                        xorps xmm0, xmm0
002CEFB7  41 89 41 04                     mov dword ptr [r9 + 4], eax
002CEFBB  41 C7 01 04 00 00 00            mov dword ptr [r9], 4
002CEFC2  0F B7 05 4B 60 CF 00            movzx eax, word ptr [rip + 0xcf604b]
002CEFC9  66 41 89 41 08                  mov word ptr [r9 + 8], ax
002CEFCE  33 C0                           xor eax, eax
002CEFD0  66 41 89 51 0A                  mov word ptr [r9 + 0xa], dx
002CEFD5  41 0F 11 41 0C                  movups xmmword ptr [r9 + 0xc], xmm0
002CEFDA  41 89 41 1C                     mov dword ptr [r9 + 0x1c], eax
002CEFDE  85 D2                           test edx, edx
002CEFE0  0F 84 22 FD FF FF               je 0x1402ced08
002CEFE6  4D 8B E9                        mov r13, r9
002CEFE9  4C 8D 25 10 10 D3 FF            lea r12, [rip - 0x2ceff0]
002CEFF0  8B DE                           mov ebx, esi
002CEFF2  0F B7 CE                        movzx ecx, si
002CEFF5  48 8D 3C 5B                     lea rdi, [rbx + rbx*2]
002CEFF9  48 C1 E7 04                     shl rdi, 4
002CEFFD  49 03 FD                        add rdi, r13
002CF000  E8 5B 5D F9 FF                  call 0x140264d60
002CF005  0F B7 CE                        movzx ecx, si
002CF008  88 47 20                        mov byte ptr [rdi + 0x20], al
002CF00B  E8 E0 AE F7 FF                  call 0x140249ef0
002CF010  88 47 21                        mov byte ptr [rdi + 0x21], al
002CF013  0F 57 C0                        xorps xmm0, xmm0
002CF016  49 8B 84 DC 28 71 FC 00         mov rax, qword ptr [r12 + rbx*8 + 0xfc7128]
002CF01E  FF C6                           inc esi
002CF020  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
002CF024  33 C0                           xor eax, eax
002CF026  0F 11 47 22                     movups xmmword ptr [rdi + 0x22], xmm0
002CF02A  0F 11 47 32                     movups xmmword ptr [rdi + 0x32], xmm0
002CF02E  89 47 42                        mov dword ptr [rdi + 0x42], eax
002CF031  66 89 47 46                     mov word ptr [rdi + 0x46], ax
002CF035  0F B7 05 DC 5F CF 00            movzx eax, word ptr [rip + 0xcf5fdc]
002CF03C  3B F0                           cmp esi, eax
002CF03E  72 B0                           jb 0x1402ceff0
002CF040  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
002CF044  E9 BA FC FF FF                  jmp 0x1402ced03
002CF049  4C 8B 65 70                     mov r12, qword ptr [rbp + 0x70]
002CF04D  33 C0                           xor eax, eax
002CF04F  41 B9 01 00 00 00               mov r9d, 1
002CF055  0F 57 C0                        xorps xmm0, xmm0
002CF058  45 89 0C 24                     mov dword ptr [r12], r9d
002CF05C  41 89 54 24 04                  mov dword ptr [r12 + 4], edx
002CF061  41 89 7C 24 08                  mov dword ptr [r12 + 8], edi
002CF066  66 45 89 44 24 1E               mov word ptr [r12 + 0x1e], r8w
002CF06C  41 0F 11 44 24 0C               movups xmmword ptr [r12 + 0xc], xmm0
002CF072  66 41 89 44 24 1C               mov word ptr [r12 + 0x1c], ax
002CF078  66 45 3B 17                     cmp r10w, word ptr [r15]
002CF07C  0F 83 28 05 00 00               jae 0x1402cf5aa
002CF082  4B 8B 4C D7 08                  mov rcx, qword ptr [r15 + r10*8 + 8]
002CF087  41 0F 11 44 24 20               movups xmmword ptr [r12 + 0x20], xmm0
002CF08D  66 45 89 54 24 28               mov word ptr [r12 + 0x28], r10w
002CF093  44 0F B7 C6                     movzx r8d, si
002CF097  49 89 4C 24 20                  mov qword ptr [r12 + 0x20], rcx
002CF09C  41 0F B7 07                     movzx eax, word ptr [r15]
002CF0A0  66 3B F0                        cmp si, ax
002CF0A3  73 18                           jae 0x1402cf0bd
002CF0A5  66 45 3B C2                     cmp r8w, r10w
002CF0A9  0F 85 B8 05 00 00               jne 0x1402cf667
002CF0AF  41 0F B7 07                     movzx eax, word ptr [r15]
002CF0B3  66 41 FF C0                     inc r8w
002CF0B7  66 44 3B C0                     cmp r8w, ax
002CF0BB  72 E8                           jb 0x1402cf0a5
002CF0BD  8B C2                           mov eax, edx
002CF0BF  4C 03 E0                        add r12, rax
002CF0C2  4C 89 65 70                     mov qword ptr [rbp + 0x70], r12
002CF0C6  E9 EE FD FF FF                  jmp 0x1402ceeb9
002CF0CB  81 FB FF FF 00 00               cmp ebx, 0xffff
002CF0D1  0F 84 4E FA FF FF               je 0x1402ceb25
002CF0D7  83 FB 07                        cmp ebx, 7
002CF0DA  0F 85 47 FA FF FF               jne 0x1402ceb27
002CF0E0  E9 40 FA FF FF                  jmp 0x1402ceb25
002CF0E5  BB 04 00 00 C0                  mov ebx, 0xc0000004
002CF0EA  E9 25 FC FF FF                  jmp 0x1402ced14
002CF0EF  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
002CF0F3  0F 57 C0                        xorps xmm0, xmm0
002CF0F6  88 41 08                        mov byte ptr [rcx + 8], al
002CF0F9  C7 01 00 00 00 00               mov dword ptr [rcx], 0
002CF0FF  C7 41 04 30 00 00 00            mov dword ptr [rcx + 4], 0x30
002CF106  41 80 BD 08 8A 00 00 00         cmp byte ptr [r13 + 0x8a08], 0
002CF10E  66 C7 41 1E 01 00               mov word ptr [rcx + 0x1e], 1
002CF114  0F 95 C0                        setne al
002CF117  88 41 09                        mov byte ptr [rcx + 9], al
002CF11A  33 C0                           xor eax, eax
002CF11C  0F 11 41 0A                     movups xmmword ptr [rcx + 0xa], xmm0
002CF120  89 41 1A                        mov dword ptr [rcx + 0x1a], eax
002CF123  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
002CF127  41 0F B6 85 D0 00 00 00         movzx eax, byte ptr [r13 + 0xd0]
002CF12F  66 89 41 28                     mov word ptr [rcx + 0x28], ax
002CF133  49 8B 85 60 8E 00 00            mov rax, qword ptr [r13 + 0x8e60]
002CF13A  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
002CF13E  48 83 C1 30                     add rcx, 0x30
002CF142  48 89 4D 70                     mov qword ptr [rbp + 0x70], rcx
002CF146  E9 2A FB FF FF                  jmp 0x1402cec75
002CF14B  49 8B CC                        mov rcx, r12
002CF14E  E8 7D E1 00 00                  call 0x1402dd2d0
002CF153  8B F8                           mov edi, eax
002CF155  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
002CF159  8B 05 21 79 CF 00               mov eax, dword ptr [rip + 0xcf7921]
002CF15F  3B F8                           cmp edi, eax
002CF161  0F 83 CA 04 00 00               jae 0x1402cf631
002CF167  44 8B E7                        mov r12d, edi
002CF16A  E9 6C FA FF FF                  jmp 0x1402cebdb
002CF16F  41 0F B7 57 02                  movzx edx, word ptr [r15 + 2]
002CF174  4D 8D 85 10 9F 00 00            lea r8, [r13 + 0x9f10]
002CF17B  49 8B CF                        mov rcx, r15
002CF17E  E8 DD F6 FF FF                  call 0x1402ce860
002CF183  48 8B 75 70                     mov rsi, qword ptr [rbp + 0x70]
002CF187  33 C0                           xor eax, eax
002CF189  48 39 45 60                     cmp qword ptr [rbp + 0x60], rax
002CF18D  41 B9 07 00 00 00               mov r9d, 7
002CF193  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
002CF197  49 8B CF                        mov rcx, r15
002CF19A  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
002CF19E  41 0F 95 C0                     setne r8b
002CF1A2  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
002CF1A6  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
002CF1AB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002CF1B0  48 8D 44 24 58                  lea rax, [rsp + 0x58]
002CF1B5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002CF1BA  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
002CF1BE  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
002CF1C3  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002CF1C7  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002CF1CC  E8 53 05 00 00                  call 0x1402cf724
002CF1D1  44 03 74 24 58                  add r14d, dword ptr [rsp + 0x58]
002CF1D6  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
002CF1DB  85 C0                           test eax, eax
002CF1DD  0F 89 0B 03 00 00               jns 0x1402cf4ee
002CF1E3  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
002CF1E7  E9 A7 FA FF FF                  jmp 0x1402cec93
002CF1EC  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002CF1F1  44 8B F6                        mov r14d, esi
002CF1F4  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
002CF1F8  E9 64 FA FF FF                  jmp 0x1402cec61
002CF1FD  33 F6                           xor esi, esi
002CF1FF  41 39 B5 94 8B 00 00            cmp dword ptr [r13 + 0x8b94], esi
002CF206  0F 86 9C FA FF FF               jbe 0x1402ceca8
002CF20C  44 8B 64 24 50                  mov r12d, dword ptr [rsp + 0x50]
002CF211  0F B7 7C 24 54                  movzx edi, word ptr [rsp + 0x54]
002CF216  44 8B F6                        mov r14d, esi
002CF219  4D 69 C6 08 01 00 00            imul r8, r14, 0x108
002CF220  49 81 C0 00 AF 00 00            add r8, 0xaf00
002CF227  4D 03 C5                        add r8, r13
002CF22A  83 3D C3 7D CF 00 00            cmp dword ptr [rip + 0xcf7dc3], 0
002CF231  0F 85 7B 03 00 00               jne 0x1402cf5b2
002CF237  41 0F B7 57 02                  movzx edx, word ptr [r15 + 2]
002CF23C  49 8B CF                        mov rcx, r15
002CF23F  E8 1C F6 FF FF                  call 0x1402ce860
002CF244  48 8B 54 F5 C8                  mov rdx, qword ptr [rbp + rsi*8 - 0x38]
002CF249  49 8B CF                        mov rcx, r15
002CF24C  E8 FB 05 00 00                  call 0x1402cf84c
002CF251  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
002CF255  48 85 DB                        test rbx, rbx
002CF258  0F 85 A8 02 00 00               jne 0x1402cf506
002CF25E  85 C0                           test eax, eax
002CF260  0F 85 97 00 00 00               jne 0x1402cf2fd
002CF266  4C 8B C2                        mov r8, rdx
002CF269  49 8B CF                        mov rcx, r15
002CF26C  E8 BF 06 00 00                  call 0x1402cf930
002CF271  45 0F B7 07                     movzx r8d, word ptr [r15]
002CF275  45 33 D2                        xor r10d, r10d
002CF278  41 0F B7 CA                     movzx ecx, r10w
002CF27C  66 41 3B C8                     cmp cx, r8w
002CF280  73 1F                           jae 0x1402cf2a1
002CF282  0F B7 C1                        movzx eax, cx
002CF285  49 8B 54 C7 08                  mov rdx, qword ptr [r15 + rax*8 + 8]
002CF28A  48 85 D2                        test rdx, rdx
002CF28D  0F 84 F7 02 00 00               je 0x1402cf58a
002CF293  0F 57 C0                        xorps xmm0, xmm0
002CF296  0F B7 F9                        movzx edi, cx
002CF299  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
002CF29D  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
002CF2A1  44 0F B7 FF                     movzx r15d, di
002CF2A5  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
002CF2A9  45 0F B7 CA                     movzx r9d, r10w
002CF2AD  41 0F B7 D2                     movzx edx, r10w
002CF2B1  44 0F B7 03                     movzx r8d, word ptr [rbx]
002CF2B5  66 45 3B D0                     cmp r10w, r8w
002CF2B9  73 18                           jae 0x1402cf2d3
002CF2BB  0F B7 C2                        movzx eax, dx
002CF2BE  48 83 7C C3 08 00               cmp qword ptr [rbx + rax*8 + 8], 0
002CF2C4  74 04                           je 0x1402cf2ca
002CF2C6  66 41 FF C1                     inc r9w
002CF2CA  66 FF C2                        inc dx
002CF2CD  66 41 3B D0                     cmp dx, r8w
002CF2D1  72 E8                           jb 0x1402cf2bb
002CF2D3  45 0F B7 C1                     movzx r8d, r9w
002CF2D7  41 C1 E0 04                     shl r8d, 4
002CF2DB  41 83 C0 2F                     add r8d, 0x2f
002CF2DF  41 83 E0 F8                     and r8d, 0xfffffff8
002CF2E3  45 03 E0                        add r12d, r8d
002CF2E6  44 3B 64 24 60                  cmp r12d, dword ptr [rsp + 0x60]
002CF2EB  0F 86 17 01 00 00               jbe 0x1402cf408
002CF2F1  C7 44 24 64 04 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000004
002CF2F9  4C 8B 7D 80                     mov r15, qword ptr [rbp - 0x80]
002CF2FD  FF C6                           inc esi
002CF2FF  41 3B B5 94 8B 00 00            cmp esi, dword ptr [r13 + 0x8b94]
002CF306  0F 82 0A FF FF FF               jb 0x1402cf216
002CF30C  8B 5D 68                        mov ebx, dword ptr [rbp + 0x68]
002CF30F  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
002CF314  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
002CF319  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
002CF31E  66 89 7C 24 54                  mov word ptr [rsp + 0x54], di
002CF323  8B 7C 24 6C                     mov edi, dword ptr [rsp + 0x6c]
002CF327  E9 7C F9 FF FF                  jmp 0x1402ceca8
002CF32C  48 8B 7D 70                     mov rdi, qword ptr [rbp + 0x70]
002CF330  45 33 ED                        xor r13d, r13d
002CF333  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
002CF337  41 8B DD                        mov ebx, r13d
002CF33A  48 83 C7 08                     add rdi, 8
002CF33E  8B C3                           mov eax, ebx
002CF340  48 8B 8C C2 C0 F6 FC 00         mov rcx, qword ptr [rdx + rax*8 + 0xfcf6c0]
002CF348  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
002CF34C  48 85 D2                        test rdx, rdx
002CF34F  0F 84 47 02 00 00               je 0x1402cf59c
002CF355  0F B7 02                        movzx eax, word ptr [rdx]
002CF358  48 8B 44 C1 20                  mov rax, qword ptr [rcx + rax*8 + 0x20]
002CF35D  48 85 C0                        test rax, rax
002CF360  0F 84 80 00 00 00               je 0x1402cf3e6
002CF366  4C 8B 88 80 00 00 00            mov r9, qword ptr [rax + 0x80]
002CF36D  44 0F B7 90 88 00 00 00         movzx r10d, word ptr [rax + 0x88]
002CF375  48 85 D2                        test rdx, rdx
002CF378  74 27                           je 0x1402cf3a1
002CF37A  48 8B 05 2F 3E C5 00            mov rax, qword ptr [rip + 0xc53e2f]
002CF381  41 8B D5                        mov edx, r13d
002CF384  8B 0C B0                        mov ecx, dword ptr [rax + rsi*4]
002CF387  44 8B C1                        mov r8d, ecx
002CF38A  83 E1 3F                        and ecx, 0x3f
002CF38D  41 C1 E8 06                     shr r8d, 6
002CF391  45 3B C2                        cmp r8d, r10d
002CF394  49 8B C1                        mov rax, r9
002CF397  0F 94 C2                        sete dl
002CF39A  48 D3 E8                        shr rax, cl
002CF39D  85 D0                           test eax, edx
002CF39F  74 45                           je 0x1402cf3e6
002CF3A1  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
002CF3A5  83 C0 30                        add eax, 0x30
002CF3A8  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
002CF3AC  3B 44 24 60                     cmp eax, dword ptr [rsp + 0x60]
002CF3B0  0F 87 1F 01 00 00               ja 0x1402cf4d5
002CF3B6  C7 47 FC 30 00 00 00            mov dword ptr [rdi - 4], 0x30
002CF3BD  0F 57 C0                        xorps xmm0, xmm0
002CF3C0  89 1F                           mov dword ptr [rdi], ebx
002CF3C2  B8 01 00 00 00                  mov eax, 1
002CF3C7  89 47 F8                        mov dword ptr [rdi - 8], eax
002CF3CA  C7 47 14 00 00 01 00            mov dword ptr [rdi + 0x14], 0x10000
002CF3D1  0F 11 47 04                     movups xmmword ptr [rdi + 4], xmm0
002CF3D5  0F 11 47 18                     movups xmmword ptr [rdi + 0x18], xmm0
002CF3D9  66 44 89 57 20                  mov word ptr [rdi + 0x20], r10w
002CF3DE  4C 89 4F 18                     mov qword ptr [rdi + 0x18], r9
002CF3E2  48 83 C7 30                     add rdi, 0x30
002CF3E6  B8 01 00 00 00                  mov eax, 1
002CF3EB  48 8D 15 0E 0C D3 FF            lea rdx, [rip - 0x2cf3f2]
002CF3F2  03 D8                           add ebx, eax
002CF3F4  0F B7 05 05 5C CF 00            movzx eax, word ptr [rip + 0xcf5c05]
002CF3FB  3B D8                           cmp ebx, eax
002CF3FD  0F 83 3D FC FF FF               jae 0x1402cf040
002CF403  E9 36 FF FF FF                  jmp 0x1402cf33e
002CF408  4C 8B 5D 70                     mov r11, qword ptr [rbp + 0x70]
002CF40C  48 8D 04 76                     lea rax, [rsi + rsi*2]
002CF410  48 8D 14 85 00 00 00 00         lea rdx, [rax*4]
002CF418  0F 57 C0                        xorps xmm0, xmm0
002CF41B  49 03 D5                        add rdx, r13
002CF41E  41 0F B7 FF                     movzx edi, r15w
002CF422  41 C7 03 02 00 00 00            mov dword ptr [r11], 2
002CF429  45 89 43 04                     mov dword ptr [r11 + 4], r8d
002CF42D  0F B6 82 58 8B 00 00            movzx eax, byte ptr [rdx + 0x8b58]
002CF434  41 88 43 08                     mov byte ptr [r11 + 8], al
002CF438  0F B6 82 59 8B 00 00            movzx eax, byte ptr [rdx + 0x8b59]
002CF43F  41 88 43 09                     mov byte ptr [r11 + 9], al
002CF443  0F B7 82 5A 8B 00 00            movzx eax, word ptr [rdx + 0x8b5a]
002CF44A  66 41 89 43 0A                  mov word ptr [r11 + 0xa], ax
002CF44F  48 8D 04 76                     lea rax, [rsi + rsi*2]
002CF453  41 8B 8C 85 5C 8B 00 00         mov ecx, dword ptr [r13 + rax*4 + 0x8b5c]
002CF45B  41 89 4B 0C                     mov dword ptr [r11 + 0xc], ecx
002CF45F  8B 82 60 8B 00 00               mov eax, dword ptr [rdx + 0x8b60]
002CF465  41 89 43 10                     mov dword ptr [r11 + 0x10], eax
002CF469  33 C0                           xor eax, eax
002CF46B  66 45 89 4B 26                  mov word ptr [r11 + 0x26], r9w
002CF470  41 0F 11 43 14                  movups xmmword ptr [r11 + 0x14], xmm0
002CF475  66 41 89 43 24                  mov word ptr [r11 + 0x24], ax
002CF47A  66 44 3B 3B                     cmp r15w, word ptr [rbx]
002CF47E  0F 83 77 01 00 00               jae 0x1402cf5fb
002CF484  41 0F B7 C7                     movzx eax, r15w
002CF488  48 8B 4C C3 08                  mov rcx, qword ptr [rbx + rax*8 + 8]
002CF48D  41 0F 11 43 28                  movups xmmword ptr [r11 + 0x28], xmm0
002CF492  66 45 89 7B 30                  mov word ptr [r11 + 0x30], r15w
002CF497  45 0F B7 CA                     movzx r9d, r10w
002CF49B  49 89 4B 28                     mov qword ptr [r11 + 0x28], rcx
002CF49F  41 BB 01 00 00 00               mov r11d, 1
002CF4A5  0F B7 03                        movzx eax, word ptr [rbx]
002CF4A8  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
002CF4AC  66 44 3B D0                     cmp r10w, ax
002CF4B0  73 17                           jae 0x1402cf4c9
002CF4B2  4C 8B 75 70                     mov r14, qword ptr [rbp + 0x70]
002CF4B6  66 45 3B CF                     cmp r9w, r15w
002CF4BA  75 71                           jne 0x1402cf52d
002CF4BC  0F B7 03                        movzx eax, word ptr [rbx]
002CF4BF  66 41 FF C1                     inc r9w
002CF4C3  66 44 3B C8                     cmp r9w, ax
002CF4C7  72 ED                           jb 0x1402cf4b6
002CF4C9  41 8B C0                        mov eax, r8d
002CF4CC  48 01 45 70                     add qword ptr [rbp + 0x70], rax
002CF4D0  E9 24 FE FF FF                  jmp 0x1402cf2f9
002CF4D5  C7 44 24 64 04 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000004
002CF4DD  E9 04 FF FF FF                  jmp 0x1402cf3e6
002CF4E2  48 89 45 F8                     mov qword ptr [rbp - 8], rax
002CF4E6  48 03 C7                        add rax, rdi
002CF4E9  E9 B6 F6 FF FF                  jmp 0x1402ceba4
002CF4EE  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
002CF4F2  85 C0                           test eax, eax
002CF4F4  0F 84 99 F7 FF FF               je 0x1402cec93
002CF4FA  48 03 F0                        add rsi, rax
002CF4FD  48 89 75 70                     mov qword ptr [rbp + 0x70], rsi
002CF501  E9 8D F7 FF FF                  jmp 0x1402cec93
002CF506  4C 8B C2                        mov r8, rdx
002CF509  49 8B CF                        mov rcx, r15
002CF50C  E8 1F 04 00 00                  call 0x1402cf930
002CF511  44 0F B7 3B                     movzx r15d, word ptr [rbx]
002CF515  45 33 D2                        xor r10d, r10d
002CF518  E9 88 FD FF FF                  jmp 0x1402cf2a5
002CF51D  FF C0                           inc eax
002CF51F  E9 F8 F5 FF FF                  jmp 0x1402ceb1c
002CF524  48 89 45 08                     mov qword ptr [rbp + 8], rax
002CF528  E9 95 F6 FF FF                  jmp 0x1402cebc2
002CF52D  41 0F B7 F9                     movzx edi, r9w
002CF531  66 44 3B C8                     cmp r9w, ax
002CF535  0F 83 C8 00 00 00               jae 0x1402cf603
002CF53B  41 0F B7 C1                     movzx eax, r9w
002CF53F  4C 8B 54 C3 08                  mov r10, qword ptr [rbx + rax*8 + 8]
002CF544  4C 89 55 90                     mov qword ptr [rbp - 0x70], r10
002CF548  4D 85 D2                        test r10, r10
002CF54B  0F 85 EA 00 00 00               jne 0x1402cf63b
002CF551  45 33 D2                        xor r10d, r10d
002CF554  E9 63 FF FF FF                  jmp 0x1402cf4bc
002CF559  4D 85 F6                        test r14, r14
002CF55C  0F 85 A1 F7 FF FF               jne 0x1402ced03
002CF562  E9 1E FA FF FF                  jmp 0x1402cef85
002CF567  48 8B 84 DA 40 8C FC 00         mov rax, qword ptr [rdx + rbx*8 + 0xfc8c40]
002CF56F  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
002CF576  0F B7 81 8A 00 00 00            movzx eax, word ptr [rcx + 0x8a]
002CF57D  3B C7                           cmp eax, edi
002CF57F  0F 85 3B F9 FF FF               jne 0x1402ceec0
002CF585  E9 BA F8 FF FF                  jmp 0x1402cee44
002CF58A  66 FF C1                        inc cx
002CF58D  E9 EA FC FF FF                  jmp 0x1402cf27c
002CF592  B8 9A 00 00 C0                  mov eax, 0xc000009a
002CF597  E9 90 F7 FF FF                  jmp 0x1402ced2c
002CF59C  E8 53 FA 16 00                  call 0x14043eff4
002CF5A1  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
002CF5A5  E9 B3 FD FF FF                  jmp 0x1402cf35d
002CF5AA  48 8B CE                        mov rcx, rsi
002CF5AD  E9 D5 FA FF FF                  jmp 0x1402cf087
002CF5B2  41 0F B6 BD D0 00 00 00         movzx edi, byte ptr [r13 + 0xd0]
002CF5BA  66 41 3B 38                     cmp di, word ptr [r8]
002CF5BE  73 4C                           jae 0x1402cf60c
002CF5C0  4D 8B 7C F8 08                  mov r15, qword ptr [r8 + rdi*8 + 8]
002CF5C5  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
002CF5C9  33 D2                           xor edx, edx
002CF5CB  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
002CF5CF  44 0F B7 03                     movzx r8d, word ptr [rbx]
002CF5D3  48 8D 4B 08                     lea rcx, [rbx + 8]
002CF5D7  49 C1 E0 03                     shl r8, 3
002CF5DB  E8 60 76 3F 00                  call 0x1406c6c40
002CF5E0  4D 8B C7                        mov r8, r15
002CF5E3  66 C7 03 01 00                  mov word ptr [rbx], 1
002CF5E8  0F B7 D7                        movzx edx, di
002CF5EB  48 8B CB                        mov rcx, rbx
002CF5EE  4C 8B FB                        mov r15, rbx
002CF5F1  E8 CA C0 F8 FF                  call 0x14025b6c0
002CF5F6  E9 49 FC FF FF                  jmp 0x1402cf244
002CF5FB  49 8B CA                        mov rcx, r10
002CF5FE  E9 8A FE FF FF                  jmp 0x1402cf48d
002CF603  4C 89 55 90                     mov qword ptr [rbp - 0x70], r10
002CF607  E9 B0 FE FF FF                  jmp 0x1402cf4bc
002CF60C  45 33 FF                        xor r15d, r15d
002CF60F  EB B4                           jmp 0x1402cf5c5
002CF611  83 FB 07                        cmp ebx, 7
002CF614  0F 87 E7 F4 FF FF               ja 0x1402ceb01
002CF61A  0F A3 D9                        bt ecx, ebx
002CF61D  0F 83 DE F4 FF FF               jae 0x1402ceb01
002CF623  E9 CA F4 FF FF                  jmp 0x1402ceaf2
002CF628  48 89 45 00                     mov qword ptr [rbp], rax
002CF62C  E9 91 F5 FF FF                  jmp 0x1402cebc2
002CF631  BB 0D 00 00 C0                  mov ebx, 0xc000000d
002CF636  E9 E0 F6 FF FF                  jmp 0x1402ced1b
002CF63B  41 0F B7 CB                     movzx ecx, r11w
002CF63F  8B D1                           mov edx, ecx
002CF641  48 03 D2                        add rdx, rdx
002CF644  48 8D 41 03                     lea rax, [rcx + 3]
002CF648  48 03 C0                        add rax, rax
002CF64B  49 C7 44 D6 30 00 00 00 00      mov qword ptr [r14 + rdx*8 + 0x30], 0
002CF654  66 41 FF C3                     inc r11w
002CF658  4D 89 54 D6 28                  mov qword ptr [r14 + rdx*8 + 0x28], r10
002CF65D  66 45 89 0C C6                  mov word ptr [r14 + rax*8], r9w
002CF662  E9 EA FE FF FF                  jmp 0x1402cf551
002CF667  66 44 3B C0                     cmp r8w, ax
002CF66B  0F 83 3E FA FF FF               jae 0x1402cf0af
002CF671  41 0F B7 C0                     movzx eax, r8w
002CF675  4D 8B 5C C7 08                  mov r11, qword ptr [r15 + rax*8 + 8]
002CF67A  4D 85 DB                        test r11, r11
002CF67D  0F 84 2C FA FF FF               je 0x1402cf0af
002CF683  41 0F B7 C9                     movzx ecx, r9w
002CF687  48 8D 41 02                     lea rax, [rcx + 2]
002CF68B  48 03 C9                        add rcx, rcx
002CF68E  48 03 C0                        add rax, rax
002CF691  66 41 FF C1                     inc r9w
002CF695  49 89 74 C4 08                  mov qword ptr [r12 + rax*8 + 8], rsi
002CF69A  66 45 89 44 CC 28               mov word ptr [r12 + rcx*8 + 0x28], r8w
002CF6A0  4D 89 1C C4                     mov qword ptr [r12 + rax*8], r11
002CF6A4  E9 06 FA FF FF                  jmp 0x1402cf0af
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryLogicalProcessorRelationship(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int16 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p50;
    unsigned __int16 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p5C;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (280);
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 80, a4);
    v_rsi = 0;
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    v_stack_mF4 = 0;
    v_stack_m108 = 0;
    v_stack_mD0 = 0;
    if (((unsigned int)((unsigned int)(a2))) != 0xFFFFULL) goto loc_002CF611;
loc_002CEAE3:
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEB05;
    goto loc_002CEB01;
loc_002CEAF2:
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEAE3;
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_002CEAE3;
loc_002CEB01:
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_002CEB13;
loc_002CEB05:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + 1))) + 1);
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CF51D;
loc_002CEB13:
    if (((unsigned int)((unsigned int)(a2))) == 3) goto loc_002CF51D;
loc_002CEB1C:
    if (((unsigned int)((unsigned int)(a2))) != 5) goto loc_002CF0CB;
loc_002CEB25:
    result = (unsigned int)((result) + 1);
loc_002CEB27:
    if ((unsigned int)(result) != 0) goto loc_002CED41;
loc_002CEB2F:
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEB44;
    if (((unsigned int)((unsigned int)(a2))) > 7) goto loc_002CEB84;
    if (((unsigned int)((unsigned int)(a2))) >= 7) goto loc_002CEB84;
loc_002CEB44:
    v_stack_m98 = 0;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEB59;
    if (((unsigned int)((unsigned int)(a2))) != 2) goto loc_002CEB84;
loc_002CEB59:
    v_stack_m90 = *(unsigned __int16 *)(v_rip + 13591910) * 8 + 8 + 0 * 1;
    result = (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8 + 0 * 1) + (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8);
    v_stack_m88 = result;
    result = (result) + (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8);
    v_stack_m80 = result;
    result = (result) + (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8);
    v_stack_m78 = result;
    result = (result) + (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8);
    v_stack_m70 = result;
    result = (result) + (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8);
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEB88;
loc_002CEB84:
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_002CEB9B;
loc_002CEB88:
    v_stack_m68 = result;
    result = (result) + (*(unsigned __int16 *)(v_rip + 13591910) * 8 + 8);
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CF4E2;
loc_002CEB9B:
    if (((unsigned int)((unsigned int)(a2))) == 3) goto loc_002CF4E2;
loc_002CEBA4:
    if (((unsigned int)((unsigned int)(a2))) == 5) goto loc_002CF628;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CF524;
    if (((unsigned int)((unsigned int)(a2))) == 7) goto loc_002CF524;
loc_002CEBC2:
    if (a1 != 0) goto loc_002CF14B;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13598382))) - 1);
    v_stack_mEC = 0;
loc_002CEBDB:
    v_stack_mD8 = v_stack_m98;
    v_stack_mE0 = (unsigned int)(v_r12);
    v_stack_mF0 = 0;
    v_stack_mC8 = v_xmm0;
    if (0 > ((unsigned int)(v_r12))) goto loc_002CECCA;
    v_stack_mA8 = v_stack_m50;
    v_stack_mB0 = v_stack_m58;
    v_stack_mB8 = v_stack_m60;
    v_stack_m104 = (unsigned __int16)(v_stack_mC0);
    v_stack_mE8 = v_stack_m68;
    goto loc_002CEC42;
loc_002CEC40:
    v_rsi = 0;
loc_002CEC42:
    if (((unsigned int)((unsigned int)(a2))) == 3) goto loc_002CEEE2;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEEE2;
loc_002CEC61:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_002CEDA9;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEDA9;
loc_002CEC75:
    if (((unsigned int)((unsigned int)(a2))) == 7) goto loc_002CF16F;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CF16F;
loc_002CEC93:
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_002CF1FD;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CF1FD;
loc_002CECA8:
    v_rdi = (unsigned int)((0) + 1);
    v_stack_mEC = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) <= ((unsigned int)(v_r12))) goto loc_002CEC40;
loc_002CECCA:
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_002CF32C;
    if (((unsigned int)((unsigned int)(a2))) == 6) goto loc_002CEE1D;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CEE1D;
    v_rsi = 0;
loc_002CECEE:
    if (((unsigned int)((unsigned int)(a2))) == 4) goto loc_002CEF85;
    if (((unsigned int)((unsigned int)(a2))) == 0xFFFFULL) goto loc_002CF559;
loc_002CED03:
loc_002CED08:
    if ((unsigned int)((unsigned int)(v_stack_mF4)) == 0) goto loc_002CEF72;
loc_002CED14:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(v_stack_m108));
loc_002CED1B:
    result = v_stack_p20;
    if (v_stack_mD0 != 0) {
        a2 = 0;
        a1 = v_stack_mD0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_m108), a4);
    }
loc_002CED2C:
    v_rsp = (v_rsp) + (280);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)));
loc_002CED41:
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))))) * (v_rdi);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x504C514BULL), a4);
    v_stack_mD0 = result;
    if (result == 0) goto loc_002CF592;
loc_002CED6E:
    *(unsigned __int16 *)(result + 4 - 4) = 1;
    *(unsigned __int16 *)(result + 4 - 2) = (unsigned __int16)(v_stack_p8);
    a2 = 0;
    *(unsigned int *)(result + 4) = 0;
    result = memset(result + 4 + 4, a2, v_stack_m98, a4);
    v_rsi = (result + 4) + (v_rdi);
    v_r12 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))))) - (1);
    if (condition_is_not_equal) goto loc_002CED6E;
    v_rsi = 0;
    goto loc_002CEB2F;
loc_002CEDA9:
    a3 = 0;
    v_stack_p54 = (unsigned __int16)(*(unsigned __int8 *)(result + 208));
    v_stack_mC0 = (unsigned __int16)(*(unsigned __int8 *)(result + 208));
    v_stack_mC8 = *(unsigned __int64 *)(result + 36448);
    result = KeAndGroupAffinityEx(236, v_stack_mC8, a3, a4);
    if (v_stack_p8 != 0) goto loc_002CEDE0;
    if ((unsigned int)(result) != 0) goto loc_002CEC75;
loc_002CEDE0:
    result = KeAddGroupAffinityEx(v_stack_p70, v_stack_p54, *(unsigned __int64 *)(result + 36448), a4);
    result = ((*(unsigned __int64 *)(result + 200)) != (*(unsigned __int64 *)(result + 36448))) ? 1 : 0;
    v_r14 = (unsigned int)((v_stack_p8) + (48));
    v_stack_p50 = (unsigned int)(v_r14);
    if (((unsigned int)(v_r14)) <= v_stack_p60) goto loc_002CF0EF;
    v_stack_p64 = 0xC0000004ULL;
    goto loc_002CEC75;
loc_002CEE1D:
    v_rsi = 0;
    if (0 >= (*(unsigned __int16 *)(v_rip + 13590998))) goto loc_002CECEE;
loc_002CEE3B:
    if (v_stack_p8 != 0) goto loc_002CF567;
loc_002CEE44:
    a3 = 0;
    result = KeQueryNodeActiveAffinityEx(0, v_stack_m98, a3, a4);
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m98)))) goto loc_002CEEB9;
loc_002CEE79:
    if ((*(unsigned __int64 *)(v_stack_m98 + 0 * 8 + 8)) != 0) {
        a3 = (unsigned __int16)((0) + 1);
    }
    a2 = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(a2)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m98)))) goto loc_002CEE79;
    if ((unsigned __int16)(a3) == 0) goto loc_002CEEB9;
    a2 = (unsigned int)(((unsigned __int16)(a3)) << (4));
    a2 = (unsigned int)((a2) + (39));
    a2 = (unsigned int)((a2) & (0xFFFFFFF8ULL));
    v_r13 = (unsigned int)(((unsigned int)(v_stack_p50)) + (a2));
    if (((unsigned int)(v_r13)) <= v_stack_p60) goto loc_002CF049;
    v_stack_p64 = 0xC0000004ULL;
loc_002CEEB9:
loc_002CEEC0:
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 13590841)))) goto loc_002CEE3B;
    v_stack_p50 = (unsigned int)(v_r13);
    goto loc_002CECEE;
loc_002CEEE2:
    result = KiCopyAffinityEx(v_stack_m98, *(unsigned __int16 *)(v_stack_m98 + 2), v_stack_mD0 + 35856, *(unsigned __int16 *)(v_stack_m98));
    a3 = (v_stack_p8 != 0) ? 1 : 0;
    v_stack_p40 = v_stack_p5C;
    v_stack_p58 = 0;
    v_stack_p38 = v_stack_p58;
    v_stack_p5C = 0;
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_p50));
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p60));
    v_stack_p20 = v_stack_p18;
    result = KiTryPopulateLogicalProcessorInformation(v_stack_m98, v_stack_mB8, a3, 3);
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p50)) + (v_stack_p58));
    v_stack_p50 = (unsigned int)(v_rsi);
    if (sign_flag) goto loc_002CF1EC;
    v_r14 = v_stack_p18;
    if ((unsigned int)((unsigned int)(v_stack_p5C)) != 0) {
        v_r14 = (v_stack_p18) + ((unsigned int)(v_stack_p5C));
        v_stack_p18 = v_r14;
    }
    goto loc_002CEC61;
loc_002CEF72:
    if ((unsigned int)(a3) != 0) goto loc_002CED14;
    goto loc_002CED14;
loc_002CEF85:
    result = (unsigned int)((*(unsigned __int16 *)(v_rip + 13590663) + *(unsigned __int16 *)(v_rip + 13590663) * 2) << (4));
    result = (unsigned int)((result) + (39));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    a3 = (unsigned int)(((unsigned int)(v_stack_p50)) + ((unsigned int)(result)));
    v_stack_p50 = (unsigned int)(a3);
    if (((unsigned int)(a3)) > v_stack_p60) goto loc_002CF0E5;
    *(unsigned int *)(v_stack_p18 + 4) = (unsigned int)(result);
    *(unsigned int *)(v_stack_p18) = 4;
    *(unsigned __int16 *)(v_stack_p18 + 8) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 13590603));
    result = 0;
    *(unsigned __int16 *)(v_stack_p18 + 10) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 13590663));
    *(unsigned __int64 *)(v_stack_p18 + 12) = v_xmm0;
    *(unsigned int *)(v_stack_p18 + 28) = 0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 13590663)) == 0) goto loc_002CED08;
loc_002CEFF0:
    v_rdi = ((unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 2) << (4);
    v_rdi = (v_rdi) + (v_stack_p18);
    result = KeQueryMaximumProcessorCountEx((unsigned __int16)(v_rsi), *(unsigned __int16 *)(v_rip + 13590663), a3, v_stack_p18);
    *(unsigned __int8 *)(v_rdi + 32) = (unsigned __int8)(result);
    result = KeQueryActiveProcessorCountEx((unsigned __int16)(v_rsi), *(unsigned __int16 *)(v_rip + 13590663), a3, v_stack_p18);
    *(unsigned __int8 *)(v_rdi + 33) = (unsigned __int8)(result);
    v_rsi = (unsigned int)((v_rsi) + 1);
    *(unsigned __int64 *)(v_rdi + 72) = *(unsigned __int64 *)(v_rip - 2945008 + (unsigned int)((unsigned int)(v_rsi)) * 8 + 16544040);
    result = 0;
    *(unsigned __int64 *)(v_rdi + 34) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 50) = v_xmm0;
    *(unsigned int *)(v_rdi + 66) = 0;
    *(unsigned __int16 *)(v_rdi + 70) = 0;
    if (((unsigned int)(v_rsi)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 13590492)))) goto loc_002CEFF0;
loc_002CF040:
    goto loc_002CED03;
loc_002CF049:
    result = 0;
    *(unsigned int *)(v_stack_p18) = 1;
    *(unsigned int *)(v_stack_p18 + 4) = (unsigned int)(*(unsigned __int16 *)(v_rip + 13590663));
    *(unsigned int *)(v_stack_p18 + 8) = (unsigned int)(v_rdi);
    *(unsigned __int16 *)(v_stack_p18 + 30) = (unsigned __int16)(a3);
    *(unsigned __int64 *)(v_stack_p18 + 12) = v_xmm0;
    *(unsigned __int16 *)(v_stack_p18 + 28) = 0;
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2944605 + 0 * 8 + 16578240) + 12))) >= (*(unsigned __int16 *)(v_stack_m98))) goto loc_002CF5AA;
loc_002CF087:
    *(unsigned __int64 *)(v_stack_p18 + 32) = v_xmm0;
    *(unsigned __int16 *)(v_stack_p18 + 40) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2944605 + 0 * 8 + 16578240) + 12));
    *(unsigned __int64 *)(v_stack_p18 + 32) = *(unsigned __int64 *)(v_stack_m98 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2944605 + 0 * 8 + 16578240) + 12) * 8 + 8);
    if (((unsigned __int16)(v_rsi)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m98)))) goto loc_002CF0BD;
loc_002CF0A5:
    if (((unsigned __int16)((unsigned __int16)(v_rsi))) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2944605 + 0 * 8 + 16578240) + 12)))) goto loc_002CF667;
loc_002CF0AF:
    a3 = (unsigned __int16)(((unsigned __int16)(v_rsi)) + 1);
    if (((unsigned __int16)(a3)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m98)))) goto loc_002CF0A5;
loc_002CF0BD:
    v_r12 = (v_stack_p18) + ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13590663))));
    v_stack_p18 = v_r12;
    goto loc_002CEEB9;
loc_002CF0CB:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) == 0xFFFFULL) goto loc_002CEB25;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) != 7) goto loc_002CEB27;
    goto loc_002CEB25;
loc_002CF0E5:
    goto loc_002CED14;
loc_002CF0EF:
    *(unsigned __int8 *)(v_stack_p18 + 8) = (unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13590663))));
    *(unsigned int *)(v_stack_p18) = 0;
    *(unsigned int *)(v_stack_p18 + 4) = 48;
    *(unsigned __int16 *)(v_stack_p18 + 30) = 1;
    result = ((*(unsigned __int8 *)(v_stack_mD0 + 35336)) != 0) ? 1 : 0;
    *(unsigned __int8 *)(v_stack_p18 + 9) = (unsigned __int8)(result);
    result = 0;
    *(unsigned __int64 *)(v_stack_p18 + 10) = v_xmm0;
    *(unsigned int *)(v_stack_p18 + 26) = 0;
    *(unsigned __int64 *)(v_stack_p18 + 32) = v_xmm0;
    *(unsigned __int16 *)(v_stack_p18 + 40) = (unsigned __int16)(*(unsigned __int8 *)(v_stack_mD0 + 208));
    *(unsigned __int64 *)(v_stack_p18 + 32) = *(unsigned __int64 *)(v_stack_mD0 + 36448);
    a1 = (v_stack_p18) + (48);
    v_stack_p18 = a1;
    goto loc_002CEC75;
loc_002CF14B:
    result = KeGetProcessorIndexFromNumber(v_r12, *(unsigned __int16 *)(v_rip + 13590663), a3, 1);
    v_stack_p6C = (unsigned int)(result);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13596961))))) goto loc_002CF631;
    goto loc_002CEBDB;
loc_002CF16F:
    result = KiCopyAffinityEx(v_stack_m98, *(unsigned __int16 *)(v_stack_m98 + 2), v_stack_mD0 + 40720, 1);
    result = 0;
    v_stack_p58 = 0;
    a3 = (v_stack_p8 != 0) ? 1 : 0;
    v_stack_p5C = 0;
    v_stack_p40 = v_stack_p5C;
    v_stack_p38 = v_stack_p58;
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(v_rsi)));
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p60));
    v_stack_p20 = v_stack_p18;
    result = KiTryPopulateLogicalProcessorInformation(v_stack_m98, v_stack_mA8, a3, 7);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + (v_stack_p58));
    v_stack_p50 = (unsigned int)(v_r14);
    if (!sign_flag) goto loc_002CF4EE;
    v_stack_p64 = (unsigned int)(result);
    goto loc_002CEC93;
loc_002CF1EC:
    v_stack_p64 = (unsigned int)(result);
    goto loc_002CEC61;
loc_002CF1FD:
    v_rsi = 0;
    if ((*(unsigned int *)(v_stack_mD0 + 35732)) <= 0) goto loc_002CECA8;
loc_002CF216:
    a3 = (a3) * (0);
    a3 = (a3) + (0xAF00ULL);
    a3 = (a3) + (v_stack_mD0);
    if ((*(unsigned int *)(v_rip + 13598147)) != 0) goto loc_002CF5B2;
    result = KiCopyAffinityEx(v_stack_m98, *(unsigned __int16 *)(v_stack_m98 + 2), a3, 7);
loc_002CF244:
    result = KiAndAffinityExNoResult(v_stack_m98, *(unsigned __int64 *)(v_stack_m58 + v_rsi * 8 - 56), a3, 7);
    if (v_stack_p8 != 0) goto loc_002CF506;
    if ((unsigned int)(result) != 0) goto loc_002CF2FD;
    result = KeOrAffinityEx2(v_stack_m98, *(unsigned __int64 *)(v_stack_m58 + v_rsi * 8 - 56), *(unsigned __int64 *)(v_stack_m58 + v_rsi * 8 - 56), 7);
    v_r10 = 0;
loc_002CF27C:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m98)))) goto loc_002CF2A1;
    if (*(unsigned __int64 *)(v_stack_m98 + 0 * 8 + 8) == 0) goto loc_002CF58A;
    v_stack_mC8 = v_xmm0;
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_m98 + 0 * 8 + 8);
loc_002CF2A1:
loc_002CF2A5:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mD8)))) goto loc_002CF2D3;
loc_002CF2BB:
    if ((*(unsigned __int64 *)(v_stack_mD8 + 0 * 8 + 8)) != 0) {
        a4 = (unsigned __int16)((0) + 1);
    }
    a2 = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(a2)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mD8)))) goto loc_002CF2BB;
loc_002CF2D3:
    a3 = (unsigned int)(((unsigned __int16)(a4)) << (4));
    a3 = (unsigned int)((a3) + (47));
    a3 = (unsigned int)((a3) & (0xFFFFFFF8ULL));
    v_r12 = (unsigned int)(((unsigned int)(v_stack_p50)) + ((unsigned int)(a3)));
    if (((unsigned int)(v_r12)) <= v_stack_p60) goto loc_002CF408;
    v_stack_p64 = 0xC0000004ULL;
loc_002CF2F9:
loc_002CF2FD:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(v_stack_mD0 + 35732))) goto loc_002CF216;
    v_stack_p50 = (unsigned int)(v_r12);
    v_stack_p54 = 0;
    goto loc_002CECA8;
loc_002CF32C:
    v_r13 = 0;
    v_rdi = (v_stack_p18) + (8);
loc_002CF33E:
    if (v_stack_p8 == 0) goto loc_002CF59C;
loc_002CF35D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) == 0) goto loc_002CF3E6;
    if (v_stack_p8 == 0) goto loc_002CF3A1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12926511) + (unsigned int)(v_stack_p68) * 4))) & (63));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12926511) + (unsigned int)(v_stack_p68) * 4))))) >> (6));
    a2 = (((unsigned int)(a3)) == ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 136)))) ? 1 : 0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 128)) >> ((unsigned __int8)(a1));
    if ((((unsigned int)(result)) & (a2)) == 0) goto loc_002CF3E6;
loc_002CF3A1:
    result = (unsigned int)(((unsigned int)(v_stack_p50)) + (48));
    v_stack_p50 = (unsigned int)(result);
    if (((unsigned int)(result)) > v_stack_p60) goto loc_002CF4D5;
    *(unsigned int *)(v_rdi - 4) = 48;
    *(unsigned int *)(v_rdi) = 0;
    *(unsigned int *)(v_rdi - 8) = 1;
    *(unsigned int *)(v_rdi + 20) = 0x10000ULL;
    *(unsigned __int64 *)(v_rdi + 4) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 24) = v_xmm0;
    *(unsigned __int16 *)(v_rdi + 32) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 136));
    *(unsigned __int64 *)(v_rdi + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 128);
    v_rdi = (v_rdi) + (48);
loc_002CF3E6:
    v_rbx = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rbx)) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13589509)))) goto loc_002CF040;
    goto loc_002CF33E;
loc_002CF408:
    a2 = ((unsigned int)(v_stack_p68) + (unsigned int)(v_stack_p68) * 2 * 4) + (0);
    *(unsigned int *)(v_stack_p18) = 2;
    *(unsigned int *)(v_stack_p18 + 4) = (unsigned int)(a3);
    *(unsigned __int8 *)(v_stack_p18 + 8) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 35672));
    *(unsigned __int8 *)(v_stack_p18 + 9) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 35673));
    *(unsigned __int16 *)(v_stack_p18 + 10) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 35674));
    *(unsigned int *)(v_stack_p18 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + (unsigned int)(v_stack_p68) + (unsigned int)(v_stack_p68) * 2 * 4 + 35676)));
    *(unsigned int *)(v_stack_p18 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 35680)));
    result = 0;
    *(unsigned __int16 *)(v_stack_p18 + 38) = (unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 128));
    *(unsigned __int64 *)(v_stack_p18 + 20) = v_xmm0;
    *(unsigned __int16 *)(v_stack_p18 + 36) = 0;
    if (((unsigned __int16)(v_stack_mD8)) >= (*(unsigned __int16 *)(v_rbx))) goto loc_002CF5FB;
loc_002CF48D:
    *(unsigned __int64 *)(v_stack_p18 + 40) = v_xmm0;
    *(unsigned __int16 *)(v_stack_p18 + 48) = (unsigned __int16)(v_stack_mD8);
    *(unsigned __int64 *)(v_stack_p18 + 40) = *(unsigned __int64 *)(v_rbx + (unsigned __int16)(v_stack_mD8) * 8 + 8);
    v_stack_mC8 = *(unsigned __int64 *)(v_rbx + (unsigned __int16)(v_stack_mD8) * 8 + 8);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 136))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)))) goto loc_002CF4C9;
loc_002CF4B6:
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 136)))) != ((unsigned __int16)(v_stack_mD8))) goto loc_002CF52D;
loc_002CF4BC:
    a4 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 0 * 8 + 16578240) + *(unsigned __int16 *)(v_stack_p8) * 8 + 32) + 136))) + 1);
    if (((unsigned __int16)(a4)) < ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)))) goto loc_002CF4B6;
loc_002CF4C9:
    goto loc_002CF2F9;
loc_002CF4D5:
    v_stack_p64 = 0xC0000004ULL;
    goto loc_002CF3E6;
loc_002CF4E2:
    v_stack_m60 = (unsigned int)((unsigned int)(a3));
    result = ((unsigned int)((unsigned int)(a3))) + ((unsigned __int16)(v_stack_mD8));
    goto loc_002CEBA4;
loc_002CF4EE:
    if ((unsigned int)((unsigned int)(v_stack_p5C)) == 0) goto loc_002CEC93;
    v_rsi = ((unsigned int)(v_stack_p68)) + ((unsigned int)(v_stack_p5C));
    v_stack_p18 = v_rsi;
    goto loc_002CEC93;
loc_002CF506:
    result = KeOrAffinityEx2(v_stack_mD8, a2, a2, a4);
    v_r10 = 0;
    goto loc_002CF2A5;
loc_002CF51D:
    result = (unsigned int)((result) + 1);
    goto loc_002CEB1C;
loc_002CF524:
    v_stack_m50 = result;
    goto loc_002CEBC2;
loc_002CF52D:
    if (((unsigned __int16)(a4)) >= ((unsigned __int16)(result))) goto loc_002CF603;
    v_stack_mC8 = *(unsigned __int64 *)(v_rbx + (unsigned __int16)(a4) * 8 + 8);
    if (*(unsigned __int64 *)(v_rbx + (unsigned __int16)(a4) * 8 + 8) != 0) goto loc_002CF63B;
loc_002CF551:
    v_r10 = 0;
    goto loc_002CF4BC;
loc_002CF559:
    if (v_stack_p18 != 0) goto loc_002CED03;
    goto loc_002CEF85;
loc_002CF567:
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + v_rbx * 8 + 16550976) + 192) + 138))) != ((unsigned int)((unsigned __int16)(a4)))) goto loc_002CEEC0;
    goto loc_002CEE44;
loc_002CF58A:
    a1 = (unsigned __int16)((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + v_rbx * 8 + 16550976) + 192)) + 1);
    goto loc_002CF27C;
loc_002CF592:
    goto loc_002CED2C;
loc_002CF59C:
    result = KeGetNodePrimarySubNode(a1, a2, a2, a4);
    goto loc_002CF35D;
loc_002CF5AA:
    goto loc_002CF087;
loc_002CF5B2:
    if (((unsigned __int16)(*(unsigned __int8 *)(v_r13 + 208))) >= (*(unsigned __int16 *)(a2))) goto loc_002CF60C;
loc_002CF5C5:
    a2 = 0;
    v_stack_mC8 = *(unsigned __int64 *)(a2 + *(unsigned __int8 *)(v_r13 + 208) * 8 + 8);
    a3 = (*(unsigned __int16 *)(v_stack_mD8)) << (3);
    result = memset(v_stack_mD8 + 8, a2, a3, a4);
    *(unsigned __int16 *)(v_stack_mD8) = 1;
    result = KeAddGroupAffinityEx(v_stack_mD8, (unsigned __int16)(*(unsigned __int8 *)(v_r13 + 208)), *(unsigned __int64 *)(a2 + *(unsigned __int8 *)(v_r13 + 208) * 8 + 8), a4);
    goto loc_002CF244;
loc_002CF5FB:
    goto loc_002CF48D;
loc_002CF603:
    v_stack_mC8 = 0;
    goto loc_002CF4BC;
loc_002CF60C:
    v_r15 = 0;
    goto loc_002CF5C5;
loc_002CF611:
    if (((unsigned int)(v_stack_mD8)) > 7) goto loc_002CEB01;
    if (((unsigned int)(v_stack_mD8)) >= 7) goto loc_002CEB01;
    goto loc_002CEAF2;
loc_002CF628:
    v_stack_m58 = result;
    goto loc_002CEBC2;
loc_002CF631:
    goto loc_002CED1B;
loc_002CF63B:
    a2 = (1) + (1);
    result = (1 + 3) + (1 + 3);
    *(unsigned __int64 *)(v_stack_p18 + a2 * 8 + 48) = 0;
    v_r11 = (unsigned __int16)((1) + 1);
    *(unsigned __int64 *)(v_stack_p18 + a2 * 8 + 40) = 0;
    *(unsigned __int16 *)(v_stack_p18 + result * 8) = (unsigned __int16)(a4);
    goto loc_002CF551;
loc_002CF667:
    if (((unsigned __int16)(*(unsigned __int64 *)(a2 + *(unsigned __int8 *)(v_r13 + 208) * 8 + 8))) >= ((unsigned __int16)(result))) goto loc_002CF0AF;
    if (*(unsigned __int64 *)(v_r15 + (unsigned __int16)(*(unsigned __int64 *)(a2 + *(unsigned __int8 *)(v_r13 + 208) * 8 + 8)) * 8 + 8) == 0) goto loc_002CF0AF;
    a1 = ((unsigned __int16)(a4)) + ((unsigned __int16)(a4));
    result = ((unsigned __int16)(a4) + 2) + ((unsigned __int16)(a4) + 2);
    a4 = (unsigned __int16)((a4) + 1);
    *(unsigned __int64 *)((unsigned int)(v_stack_p78) + result * 8 + 8) = v_rsi;
    *(unsigned __int16 *)((unsigned int)(v_stack_p78) + a1 * 8 + 40) = (unsigned __int16)(*(unsigned __int64 *)(a2 + *(unsigned __int8 *)(v_r13 + 208) * 8 + 8));
    *(unsigned __int64 *)((unsigned int)(v_stack_p78) + result * 8) = *(unsigned __int64 *)(v_r15 + (unsigned __int16)(*(unsigned __int64 *)(a2 + *(unsigned __int8 *)(v_r13 + 208) * 8 + 8)) * 8 + 8);
    goto loc_002CF0AF;
}
```

## 5. (Beta) C Style

```c
int64_t KeQueryLogicalProcessorRelationship(int64_t Arg1, int32_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint16_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p50;
    uint16_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p5C;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (280);
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 80, Arg4);
    local_rsi = 0;
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    v_stack_mF4 = 0;
    v_stack_m108 = 0;
    v_stack_mD0 = 0;
    if (((uint32_t)((uint32_t)(Arg2))) != 0xFFFFULL) goto loc_002CF611;
loc_002CEAE3:
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEB05;
    goto loc_002CEB01;
loc_002CEAF2:
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEAE3;
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_002CEAE3;
loc_002CEB01:
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_002CEB13;
loc_002CEB05:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + 1))) + 1);
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CF51D;
loc_002CEB13:
    if (((uint32_t)((uint32_t)(Arg2))) == 3) goto loc_002CF51D;
loc_002CEB1C:
    if (((uint32_t)((uint32_t)(Arg2))) != 5) goto loc_002CF0CB;
loc_002CEB25:
    result = (uint32_t)((result) + 1);
loc_002CEB27:
    if ((uint32_t)(result) != 0) goto loc_002CED41;
loc_002CEB2F:
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEB44;
    if (((uint32_t)((uint32_t)(Arg2))) > 7) goto loc_002CEB84;
    if (((uint32_t)((uint32_t)(Arg2))) >= 7) goto loc_002CEB84;
loc_002CEB44:
    v_stack_m98 = 0;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEB59;
    if (((uint32_t)((uint32_t)(Arg2))) != 2) goto loc_002CEB84;
loc_002CEB59:
    v_stack_m90 = *(uint16_t *)(v_rip + 0xCF6566) * 8 + 8 + 0 * 1;
    result = (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8 + 0 * 1) + (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8);
    v_stack_m88 = result;
    result = (result) + (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8);
    v_stack_m80 = result;
    result = (result) + (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8);
    v_stack_m78 = result;
    result = (result) + (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8);
    v_stack_m70 = result;
    result = (result) + (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8);
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEB88;
loc_002CEB84:
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_002CEB9B;
loc_002CEB88:
    v_stack_m68 = result;
    result = (result) + (*(uint16_t *)(v_rip + 0xCF6566) * 8 + 8);
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CF4E2;
loc_002CEB9B:
    if (((uint32_t)((uint32_t)(Arg2))) == 3) goto loc_002CF4E2;
loc_002CEBA4:
    if (((uint32_t)((uint32_t)(Arg2))) == 5) goto loc_002CF628;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CF524;
    if (((uint32_t)((uint32_t)(Arg2))) == 7) goto loc_002CF524;
loc_002CEBC2:
    if (Arg1 != 0) goto loc_002CF14B;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCF7EAE))) - 1);
    v_stack_mEC = 0;
loc_002CEBDB:
    v_stack_mD8 = v_stack_m98;
    v_stack_mE0 = (uint32_t)(local_r12);
    v_stack_mF0 = 0;
    v_stack_mC8 = v_xmm0;
    if (0 > ((uint32_t)(local_r12))) goto loc_002CECCA;
    v_stack_mA8 = v_stack_m50;
    v_stack_mB0 = v_stack_m58;
    v_stack_mB8 = v_stack_m60;
    v_stack_m104 = (uint16_t)(v_stack_mC0);
    v_stack_mE8 = v_stack_m68;
    goto loc_002CEC42;
loc_002CEC40:
    local_rsi = 0;
loc_002CEC42:
    if (((uint32_t)((uint32_t)(Arg2))) == 3) goto loc_002CEEE2;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEEE2;
loc_002CEC61:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_002CEDA9;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEDA9;
loc_002CEC75:
    if (((uint32_t)((uint32_t)(Arg2))) == 7) goto loc_002CF16F;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CF16F;
loc_002CEC93:
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_002CF1FD;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CF1FD;
loc_002CECA8:
    local_rdi = (uint32_t)((0) + 1);
    v_stack_mEC = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) <= ((uint32_t)(local_r12))) goto loc_002CEC40;
loc_002CECCA:
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_002CF32C;
    if (((uint32_t)((uint32_t)(Arg2))) == 6) goto loc_002CEE1D;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CEE1D;
    local_rsi = 0;
loc_002CECEE:
    if (((uint32_t)((uint32_t)(Arg2))) == 4) goto loc_002CEF85;
    if (((uint32_t)((uint32_t)(Arg2))) == 0xFFFFULL) goto loc_002CF559;
loc_002CED03:
loc_002CED08:
    if ((uint32_t)((uint32_t)(v_stack_mF4)) == 0) goto loc_002CEF72;
loc_002CED14:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(v_stack_m108));
loc_002CED1B:
    result = v_stack_p20;
    if (v_stack_mD0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_m108), Arg4);
    }
loc_002CED2C:
    local_rsp = (local_rsp) + (280);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)));
loc_002CED41:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))))) * (local_rdi);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x504C514BULL), Arg4);
    v_stack_mD0 = result;
    if (result == 0) goto loc_002CF592;
loc_002CED6E:
    *(uint16_t *)(result + 0x4 - 0x4) = 1;
    *(uint16_t *)(result + 0x4 - 0x2) = (uint16_t)(v_stack_p8);
    Arg2 = 0;
    *(uint32_t *)(result + 0x4) = 0;
    result = memset(result + 4 + 4, Arg2, v_stack_m98, Arg4);
    local_rsi = (result + 4) + (local_rdi);
    local_r12 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))))) - (1);
    if (condition_is_not_equal) goto loc_002CED6E;
    local_rsi = 0;
    goto loc_002CEB2F;
loc_002CEDA9:
    Arg3 = 0;
    v_stack_p54 = (uint16_t)(*(uint8_t *)(result + 0xD0));
    v_stack_mC0 = (uint16_t)(*(uint8_t *)(result + 0xD0));
    v_stack_mC8 = *(uint64_t *)(result + 0x8E60);
    result = KeAndGroupAffinityEx(236, v_stack_mC8, Arg3, Arg4);
    if (v_stack_p8 != 0) goto loc_002CEDE0;
    if ((uint32_t)(result) != 0) goto loc_002CEC75;
loc_002CEDE0:
    result = KeAddGroupAffinityEx(v_stack_p70, v_stack_p54, *(uint64_t *)(result + 0x8E60), Arg4);
    result = ((*(uint64_t *)(result + 0xC8)) != (*(uint64_t *)(result + 0x8E60))) ? 1 : 0;
    local_r14 = (uint32_t)((v_stack_p8) + (48));
    v_stack_p50 = (uint32_t)(local_r14);
    if (((uint32_t)(local_r14)) <= v_stack_p60) goto loc_002CF0EF;
    v_stack_p64 = 0xC0000004ULL;
    goto loc_002CEC75;
loc_002CEE1D:
    local_rsi = 0;
    if (0 >= (*(uint16_t *)(v_rip + 0xCF61D6))) goto loc_002CECEE;
loc_002CEE3B:
    if (v_stack_p8 != 0) goto loc_002CF567;
loc_002CEE44:
    Arg3 = 0;
    result = KeQueryNodeActiveAffinityEx(0, v_stack_m98, Arg3, Arg4);
    if (0 >= ((uint16_t)(*(uint16_t *)(v_stack_m98)))) goto loc_002CEEB9;
loc_002CEE79:
    if ((*(uint64_t *)(v_stack_m98 + 0x0 * 8 + 0x8)) != 0) {
        Arg3 = (uint16_t)((0) + 1);
    }
    Arg2 = (uint16_t)((0) + 1);
    if (((uint16_t)(Arg2)) < ((uint16_t)(*(uint16_t *)(v_stack_m98)))) goto loc_002CEE79;
    if ((uint16_t)(Arg3) == 0) goto loc_002CEEB9;
    Arg2 = (uint32_t)(((uint16_t)(Arg3)) << (4));
    Arg2 = (uint32_t)((Arg2) + (39));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFF8ULL));
    local_r13 = (uint32_t)(((uint32_t)(v_stack_p50)) + (Arg2));
    if (((uint32_t)(local_r13)) <= v_stack_p60) goto loc_002CF049;
    v_stack_p64 = 0xC0000004ULL;
loc_002CEEB9:
loc_002CEEC0:
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint16_t *)(v_rip + 0xCF6139)))) goto loc_002CEE3B;
    v_stack_p50 = (uint32_t)(local_r13);
    goto loc_002CECEE;
loc_002CEEE2:
    result = KiCopyAffinityEx(v_stack_m98, *(uint16_t *)(v_stack_m98 + 0x2), v_stack_mD0 + 35856, *(uint16_t *)(v_stack_m98));
    Arg3 = (v_stack_p8 != 0) ? 1 : 0;
    v_stack_p40 = v_stack_p5C;
    v_stack_p58 = 0;
    v_stack_p38 = v_stack_p58;
    v_stack_p5C = 0;
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_p50));
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p60));
    v_stack_p20 = v_stack_p18;
    result = KiTryPopulateLogicalProcessorInformation(v_stack_m98, v_stack_mB8, Arg3, 3);
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p50)) + (v_stack_p58));
    v_stack_p50 = (uint32_t)(local_rsi);
    if (sign_flag) goto loc_002CF1EC;
    local_r14 = v_stack_p18;
    if ((uint32_t)((uint32_t)(v_stack_p5C)) != 0) {
        local_r14 = (v_stack_p18) + ((uint32_t)(v_stack_p5C));
        v_stack_p18 = local_r14;
    }
    goto loc_002CEC61;
loc_002CEF72:
    if ((uint32_t)(Arg3) != 0) goto loc_002CED14;
    goto loc_002CED14;
loc_002CEF85:
    result = (uint32_t)((*(uint16_t *)(v_rip + 0xCF6087) + *(uint16_t *)(v_rip + 0xCF6087) * 2) << (4));
    result = (uint32_t)((result) + (39));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p50)) + ((uint32_t)(result)));
    v_stack_p50 = (uint32_t)(Arg3);
    if (((uint32_t)(Arg3)) > v_stack_p60) goto loc_002CF0E5;
    *(uint32_t *)(v_stack_p18 + 0x4) = (uint32_t)(result);
    *(uint32_t *)(v_stack_p18) = 4;
    *(uint16_t *)(v_stack_p18 + 0x8) = (uint16_t)(*(uint16_t *)(v_rip + 0xCF604B));
    result = 0;
    *(uint16_t *)(v_stack_p18 + 0xA) = (uint16_t)(*(uint16_t *)(v_rip + 0xCF6087));
    *(uint64_t *)(v_stack_p18 + 0xC) = v_xmm0;
    *(uint32_t *)(v_stack_p18 + 0x1C) = 0;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0xCF6087)) == 0) goto loc_002CED08;
loc_002CEFF0:
    local_rdi = ((uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 2) << (4);
    local_rdi = (local_rdi) + (v_stack_p18);
    result = KeQueryMaximumProcessorCountEx((uint16_t)(local_rsi), *(uint16_t *)(v_rip + 0xCF6087), Arg3, v_stack_p18);
    *(uint8_t *)(local_rdi + 0x20) = (uint8_t)(result);
    result = KeQueryActiveProcessorCountEx((uint16_t)(local_rsi), *(uint16_t *)(v_rip + 0xCF6087), Arg3, v_stack_p18);
    *(uint8_t *)(local_rdi + 0x21) = (uint8_t)(result);
    local_rsi = (uint32_t)((local_rsi) + 1);
    *(uint64_t *)(local_rdi + 0x48) = *(uint64_t *)(v_rip - 0x2CEFF0 + (uint32_t)((uint32_t)(local_rsi)) * 8 + 0xFC7128);
    result = 0;
    *(uint64_t *)(local_rdi + 0x22) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x32) = v_xmm0;
    *(uint32_t *)(local_rdi + 0x42) = 0;
    *(uint16_t *)(local_rdi + 0x46) = 0;
    if (((uint32_t)(local_rsi)) < ((uint32_t)(*(uint16_t *)(v_rip + 0xCF5FDC)))) goto loc_002CEFF0;
loc_002CF040:
    goto loc_002CED03;
loc_002CF049:
    result = 0;
    *(uint32_t *)(v_stack_p18) = 1;
    *(uint32_t *)(v_stack_p18 + 0x4) = (uint32_t)(*(uint16_t *)(v_rip + 0xCF6087));
    *(uint32_t *)(v_stack_p18 + 0x8) = (uint32_t)(local_rdi);
    *(uint16_t *)(v_stack_p18 + 0x1E) = (uint16_t)(Arg3);
    *(uint64_t *)(v_stack_p18 + 0xC) = v_xmm0;
    *(uint16_t *)(v_stack_p18 + 0x1C) = 0;
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x2CEE5D + 0x0 * 8 + 0xFCF6C0) + 0xC))) >= (*(uint16_t *)(v_stack_m98))) goto loc_002CF5AA;
loc_002CF087:
    *(uint64_t *)(v_stack_p18 + 0x20) = v_xmm0;
    *(uint16_t *)(v_stack_p18 + 0x28) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x2CEE5D + 0x0 * 8 + 0xFCF6C0) + 0xC));
    *(uint64_t *)(v_stack_p18 + 0x20) = *(uint64_t *)(v_stack_m98 + *(uint8_t *)(*(uint64_t *)(v_rip - 0x2CEE5D + 0x0 * 8 + 0xFCF6C0) + 0xC) * 8 + 0x8);
    if (((uint16_t)(local_rsi)) >= ((uint16_t)(*(uint16_t *)(v_stack_m98)))) goto loc_002CF0BD;
loc_002CF0A5:
    if (((uint16_t)((uint16_t)(local_rsi))) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x2CEE5D + 0x0 * 8 + 0xFCF6C0) + 0xC)))) goto loc_002CF667;
loc_002CF0AF:
    Arg3 = (uint16_t)(((uint16_t)(local_rsi)) + 1);
    if (((uint16_t)(Arg3)) < ((uint16_t)(*(uint16_t *)(v_stack_m98)))) goto loc_002CF0A5;
loc_002CF0BD:
    local_r12 = (v_stack_p18) + ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xCF6087))));
    v_stack_p18 = local_r12;
    goto loc_002CEEB9;
loc_002CF0CB:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) == 0xFFFFULL) goto loc_002CEB25;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) != 7) goto loc_002CEB27;
    goto loc_002CEB25;
loc_002CF0E5:
    goto loc_002CED14;
loc_002CF0EF:
    *(uint8_t *)(v_stack_p18 + 0x8) = (uint8_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xCF6087))));
    *(uint32_t *)(v_stack_p18) = 0;
    *(uint32_t *)(v_stack_p18 + 0x4) = 48;
    *(uint16_t *)(v_stack_p18 + 0x1E) = 1;
    result = ((*(uint8_t *)(v_stack_mD0 + 0x8A08)) != 0) ? 1 : 0;
    *(uint8_t *)(v_stack_p18 + 0x9) = (uint8_t)(result);
    result = 0;
    *(uint64_t *)(v_stack_p18 + 0xA) = v_xmm0;
    *(uint32_t *)(v_stack_p18 + 0x1A) = 0;
    *(uint64_t *)(v_stack_p18 + 0x20) = v_xmm0;
    *(uint16_t *)(v_stack_p18 + 0x28) = (uint16_t)(*(uint8_t *)(v_stack_mD0 + 0xD0));
    *(uint64_t *)(v_stack_p18 + 0x20) = *(uint64_t *)(v_stack_mD0 + 0x8E60);
    Arg1 = (v_stack_p18) + (48);
    v_stack_p18 = Arg1;
    goto loc_002CEC75;
loc_002CF14B:
    result = KeGetProcessorIndexFromNumber(local_r12, *(uint16_t *)(v_rip + 0xCF6087), Arg3, 1);
    v_stack_p6C = (uint32_t)(result);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF7921))))) goto loc_002CF631;
    goto loc_002CEBDB;
loc_002CF16F:
    result = KiCopyAffinityEx(v_stack_m98, *(uint16_t *)(v_stack_m98 + 0x2), v_stack_mD0 + 40720, 1);
    result = 0;
    v_stack_p58 = 0;
    Arg3 = (v_stack_p8 != 0) ? 1 : 0;
    v_stack_p5C = 0;
    v_stack_p40 = v_stack_p5C;
    v_stack_p38 = v_stack_p58;
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(local_rsi)));
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p60));
    v_stack_p20 = v_stack_p18;
    result = KiTryPopulateLogicalProcessorInformation(v_stack_m98, v_stack_mA8, Arg3, 7);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + (v_stack_p58));
    v_stack_p50 = (uint32_t)(local_r14);
    if (!sign_flag) goto loc_002CF4EE;
    v_stack_p64 = (uint32_t)(result);
    goto loc_002CEC93;
loc_002CF1EC:
    v_stack_p64 = (uint32_t)(result);
    goto loc_002CEC61;
loc_002CF1FD:
    local_rsi = 0;
    if ((*(uint32_t *)(v_stack_mD0 + 0x8B94)) <= 0) goto loc_002CECA8;
loc_002CF216:
    Arg3 = (Arg3) * (0);
    Arg3 = (Arg3) + (0xAF00ULL);
    Arg3 = (Arg3) + (v_stack_mD0);
    if ((*(uint32_t *)(v_rip + 0xCF7DC3)) != 0) goto loc_002CF5B2;
    result = KiCopyAffinityEx(v_stack_m98, *(uint16_t *)(v_stack_m98 + 0x2), Arg3, 7);
loc_002CF244:
    result = KiAndAffinityExNoResult(v_stack_m98, *(uint64_t *)(v_stack_m58 + local_rsi * 8 - 0x38), Arg3, 7);
    if (v_stack_p8 != 0) goto loc_002CF506;
    if ((uint32_t)(result) != 0) goto loc_002CF2FD;
    result = KeOrAffinityEx2(v_stack_m98, *(uint64_t *)(v_stack_m58 + local_rsi * 8 - 0x38), *(uint64_t *)(v_stack_m58 + local_rsi * 8 - 0x38), 7);
    local_r10 = 0;
loc_002CF27C:
    if (0 >= ((uint16_t)(*(uint16_t *)(v_stack_m98)))) goto loc_002CF2A1;
    if (*(uint64_t *)(v_stack_m98 + 0x0 * 8 + 0x8) == 0) goto loc_002CF58A;
    v_stack_mC8 = v_xmm0;
    v_stack_mC8 = *(uint64_t *)(v_stack_m98 + 0x0 * 8 + 0x8);
loc_002CF2A1:
loc_002CF2A5:
    if (0 >= ((uint16_t)(*(uint16_t *)(v_stack_mD8)))) goto loc_002CF2D3;
loc_002CF2BB:
    if ((*(uint64_t *)(v_stack_mD8 + 0x0 * 8 + 0x8)) != 0) {
        Arg4 = (uint16_t)((0) + 1);
    }
    Arg2 = (uint16_t)((0) + 1);
    if (((uint16_t)(Arg2)) < ((uint16_t)(*(uint16_t *)(v_stack_mD8)))) goto loc_002CF2BB;
loc_002CF2D3:
    Arg3 = (uint32_t)(((uint16_t)(Arg4)) << (4));
    Arg3 = (uint32_t)((Arg3) + (47));
    Arg3 = (uint32_t)((Arg3) & (0xFFFFFFF8ULL));
    local_r12 = (uint32_t)(((uint32_t)(v_stack_p50)) + ((uint32_t)(Arg3)));
    if (((uint32_t)(local_r12)) <= v_stack_p60) goto loc_002CF408;
    v_stack_p64 = 0xC0000004ULL;
loc_002CF2F9:
loc_002CF2FD:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(v_stack_mD0 + 0x8B94))) goto loc_002CF216;
    v_stack_p50 = (uint32_t)(local_r12);
    v_stack_p54 = 0;
    goto loc_002CECA8;
loc_002CF32C:
    local_r13 = 0;
    local_rdi = (v_stack_p18) + (8);
loc_002CF33E:
    if (v_stack_p8 == 0) goto loc_002CF59C;
loc_002CF35D:
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) == 0) goto loc_002CF3E6;
    if (v_stack_p8 == 0) goto loc_002CF3A1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC53E2F) + (uint32_t)(v_stack_p68) * 4))) & (63));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC53E2F) + (uint32_t)(v_stack_p68) * 4))))) >> (6));
    Arg2 = (((uint32_t)(Arg3)) == ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x88)))) ? 1 : 0;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x80)) >> ((uint8_t)(Arg1));
    if ((((uint32_t)(result)) & (Arg2)) == 0) goto loc_002CF3E6;
loc_002CF3A1:
    result = (uint32_t)(((uint32_t)(v_stack_p50)) + (48));
    v_stack_p50 = (uint32_t)(result);
    if (((uint32_t)(result)) > v_stack_p60) goto loc_002CF4D5;
    *(uint32_t *)(local_rdi - 0x4) = 48;
    *(uint32_t *)(local_rdi) = 0;
    *(uint32_t *)(local_rdi - 0x8) = 1;
    *(uint32_t *)(local_rdi + 0x14) = 0x10000ULL;
    *(uint64_t *)(local_rdi + 0x4) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x18) = v_xmm0;
    *(uint16_t *)(local_rdi + 0x20) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x88));
    *(uint64_t *)(local_rdi + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x80);
    local_rdi = (local_rdi) + (48);
loc_002CF3E6:
    local_rbx = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rbx)) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xCF5C05)))) goto loc_002CF040;
    goto loc_002CF33E;
loc_002CF408:
    Arg2 = ((uint32_t)(v_stack_p68) + (uint32_t)(v_stack_p68) * 2 * 4) + (0);
    *(uint32_t *)(v_stack_p18) = 2;
    *(uint32_t *)(v_stack_p18 + 0x4) = (uint32_t)(Arg3);
    *(uint8_t *)(v_stack_p18 + 0x8) = (uint8_t)(*(uint8_t *)(Arg2 + 0x8B58));
    *(uint8_t *)(v_stack_p18 + 0x9) = (uint8_t)(*(uint8_t *)(Arg2 + 0x8B59));
    *(uint16_t *)(v_stack_p18 + 0xA) = (uint16_t)(*(uint16_t *)(Arg2 + 0x8B5A));
    *(uint32_t *)(v_stack_p18 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + (uint32_t)(v_stack_p68) + (uint32_t)(v_stack_p68) * 2 * 4 + 0x8B5C)));
    *(uint32_t *)(v_stack_p18 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8B60)));
    result = 0;
    *(uint16_t *)(v_stack_p18 + 0x26) = (uint16_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x80));
    *(uint64_t *)(v_stack_p18 + 0x14) = v_xmm0;
    *(uint16_t *)(v_stack_p18 + 0x24) = 0;
    if (((uint16_t)(v_stack_mD8)) >= (*(uint16_t *)(local_rbx))) goto loc_002CF5FB;
loc_002CF48D:
    *(uint64_t *)(v_stack_p18 + 0x28) = v_xmm0;
    *(uint16_t *)(v_stack_p18 + 0x30) = (uint16_t)(v_stack_mD8);
    *(uint64_t *)(v_stack_p18 + 0x28) = *(uint64_t *)(local_rbx + (uint16_t)(v_stack_mD8) * 8 + 0x8);
    v_stack_mC8 = *(uint64_t *)(local_rbx + (uint16_t)(v_stack_mD8) * 8 + 0x8);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x88))) >= ((uint16_t)(*(uint16_t *)(local_rbx)))) goto loc_002CF4C9;
loc_002CF4B6:
    if (((uint16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x88)))) != ((uint16_t)(v_stack_mD8))) goto loc_002CF52D;
loc_002CF4BC:
    Arg4 = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x0 * 8 + 0xFCF6C0) + *(uint16_t *)(v_stack_p8) * 8 + 0x20) + 0x88))) + 1);
    if (((uint16_t)(Arg4)) < ((uint16_t)(*(uint16_t *)(local_rbx)))) goto loc_002CF4B6;
loc_002CF4C9:
    goto loc_002CF2F9;
loc_002CF4D5:
    v_stack_p64 = 0xC0000004ULL;
    goto loc_002CF3E6;
loc_002CF4E2:
    v_stack_m60 = (uint32_t)((uint32_t)(Arg3));
    result = ((uint32_t)((uint32_t)(Arg3))) + ((uint16_t)(v_stack_mD8));
    goto loc_002CEBA4;
loc_002CF4EE:
    if ((uint32_t)((uint32_t)(v_stack_p5C)) == 0) goto loc_002CEC93;
    local_rsi = ((uint32_t)(v_stack_p68)) + ((uint32_t)(v_stack_p5C));
    v_stack_p18 = local_rsi;
    goto loc_002CEC93;
loc_002CF506:
    result = KeOrAffinityEx2(v_stack_mD8, Arg2, Arg2, Arg4);
    local_r10 = 0;
    goto loc_002CF2A5;
loc_002CF51D:
    result = (uint32_t)((result) + 1);
    goto loc_002CEB1C;
loc_002CF524:
    v_stack_m50 = result;
    goto loc_002CEBC2;
loc_002CF52D:
    if (((uint16_t)(Arg4)) >= ((uint16_t)(result))) goto loc_002CF603;
    v_stack_mC8 = *(uint64_t *)(local_rbx + (uint16_t)(arg4) * 8 + 0x8);
    if (*(uint64_t *)(local_rbx + (uint16_t)(arg4) * 8 + 0x8) != 0) goto loc_002CF63B;
loc_002CF551:
    local_r10 = 0;
    goto loc_002CF4BC;
loc_002CF559:
    if (v_stack_p18 != 0) goto loc_002CED03;
    goto loc_002CEF85;
loc_002CF567:
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + local_rbx * 8 + 0xFC8C40) + 0xC0) + 0x8A))) != ((uint32_t)((uint16_t)(Arg4)))) goto loc_002CEEC0;
    goto loc_002CEE44;
loc_002CF58A:
    Arg1 = (uint16_t)((*(uint64_t *)(*(uint64_t *)(Arg2 + local_rbx * 8 + 0xFC8C40) + 0xC0)) + 1);
    goto loc_002CF27C;
loc_002CF592:
    goto loc_002CED2C;
loc_002CF59C:
    result = KeGetNodePrimarySubNode(Arg1, Arg2, Arg2, Arg4);
    goto loc_002CF35D;
loc_002CF5AA:
    goto loc_002CF087;
loc_002CF5B2:
    if (((uint16_t)(*(uint8_t *)(local_r13 + 0xD0))) >= (*(uint16_t *)(Arg2))) goto loc_002CF60C;
loc_002CF5C5:
    Arg2 = 0;
    v_stack_mC8 = *(uint64_t *)(Arg2 + *(uint8_t *)(local_r13 + 0xD0) * 8 + 0x8);
    Arg3 = (*(uint16_t *)(v_stack_mD8)) << (3);
    result = memset(v_stack_mD8 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(v_stack_mD8) = 1;
    result = KeAddGroupAffinityEx(v_stack_mD8, (uint16_t)(*(uint8_t *)(local_r13 + 0xD0)), *(uint64_t *)(Arg2 + *(uint8_t *)(local_r13 + 0xD0) * 8 + 0x8), Arg4);
    goto loc_002CF244;
loc_002CF5FB:
    goto loc_002CF48D;
loc_002CF603:
    v_stack_mC8 = 0;
    goto loc_002CF4BC;
loc_002CF60C:
    local_r15 = 0;
    goto loc_002CF5C5;
loc_002CF611:
    if (((uint32_t)(v_stack_mD8)) > 7) goto loc_002CEB01;
    if (((uint32_t)(v_stack_mD8)) >= 7) goto loc_002CEB01;
    goto loc_002CEAF2;
loc_002CF628:
    v_stack_m58 = result;
    goto loc_002CEBC2;
loc_002CF631:
    goto loc_002CED1B;
loc_002CF63B:
    Arg2 = (1) + (1);
    result = (1 + 3) + (1 + 3);
    *(uint64_t *)(v_stack_p18 + Arg2 * 8 + 0x30) = 0;
    local_r11 = (uint16_t)((1) + 1);
    *(uint64_t *)(v_stack_p18 + Arg2 * 8 + 0x28) = 0;
    *(uint16_t *)(v_stack_p18 + result * 8) = (uint16_t)(Arg4);
    goto loc_002CF551;
loc_002CF667:
    if (((uint16_t)(*(uint64_t *)(Arg2 + *(uint8_t *)(local_r13 + 0xD0) * 8 + 0x8))) >= ((uint16_t)(result))) goto loc_002CF0AF;
    if (*(uint64_t *)(local_r15 + (uint16_t)(*(uint64_t *)(Arg2 + *(uint8_t *)(local_r13 + 0xD0) * 8 + 0x8)) * 8 + 0x8) == 0) goto loc_002CF0AF;
    Arg1 = ((uint16_t)(Arg4)) + ((uint16_t)(Arg4));
    result = ((uint16_t)(Arg4) + 2) + ((uint16_t)(Arg4) + 2);
    Arg4 = (uint16_t)((Arg4) + 1);
    *(uint64_t *)((uint32_t)(v_stack_p78) + result * 8 + 0x8) = local_rsi;
    *(uint16_t *)((uint32_t)(v_stack_p78) + Arg1 * 8 + 0x28) = (uint16_t)(*(uint64_t *)(Arg2 + *(uint8_t *)(local_r13 + 0xD0) * 8 + 0x8));
    *(uint64_t *)((uint32_t)(v_stack_p78) + result * 8) = *(uint64_t *)(local_r15 + (uint16_t)(*(uint64_t *)(Arg2 + *(uint8_t *)(local_r13 + 0xD0) * 8 + 0x8)) * 8 + 0x8);
    goto loc_002CF0AF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CEA60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
