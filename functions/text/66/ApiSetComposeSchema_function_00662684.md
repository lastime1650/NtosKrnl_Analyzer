# ApiSetComposeSchema

- RVA: `0x00662684`–`0x00662D41` (길이 `1,725` bytes)
- VA: `0x0000000140662684`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6130`
- 디코드: `495`개 명령, `1,725/1,725` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066271D` → [ApiSetValidateSchemaFormat](ApiSetValidateSchemaFormat_function_0066228C.md) (function, `0x0066228C`)
- `0x00662733` → [ApiSetValidateSchemaFormat](ApiSetValidateSchemaFormat_function_0066228C.md) (function, `0x0066228C`)
- `0x006627DA` → [ApiSetpSearchForApiSet](../4B/ApiSetpSearchForApiSet_function_004B8048.md) (function, `0x004B8048`)
- `0x006628AA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006628DC` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006628FF` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0066290E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0066292C` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006629C3` → [ApiSetValidateSchemaFormat](ApiSetValidateSchemaFormat_function_0066228C.md) (function, `0x0066228C`)
- `0x00662A6D` → [AsiAddDataToSchema](AsiAddDataToSchema_function_00662D78.md) (function, `0x00662D78`)
- `0x00662AEF` → [ApiSetpSearchForApiSet](../4B/ApiSetpSearchForApiSet_function_004B8048.md) (function, `0x004B8048`)
- `0x00662B5E` → [AsiAddDataToSchema](AsiAddDataToSchema_function_00662D78.md) (function, `0x00662D78`)
- `0x00662B97` → [AsiAddDataToSchema](AsiAddDataToSchema_function_00662D78.md) (function, `0x00662D78`)
- `0x00662BD9` → [AsiAddDataToSchema](AsiAddDataToSchema_function_00662D78.md) (function, `0x00662D78`)
- `0x00662C29` → [AsiAddDataToSchema](AsiAddDataToSchema_function_00662D78.md) (function, `0x00662D78`)
- `0x00662C62` → [AsiAddDataToSchema](AsiAddDataToSchema_function_00662D78.md) (function, `0x00662D78`)
- `0x00662C76` → [AsiSortValueList](AsiSortValueList_function_00662F60.md) (function, `0x00662F60`)
- `0x00662CC5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00662CE5` → [AsiPopulateHashes](AsiPopulateHashes_function_00662E10.md) (function, `0x00662E10`)
- `0x00662CFB` → [ApiSetValidateSchemaFormat](ApiSetValidateSchemaFormat_function_0066228C.md) (function, `0x0066228C`)
- `0x00662D20` → [ApiSetComposeSchema_V7](ApiSetComposeSchema_V7_function_00663CCC.md) (function, `0x00663CCC`)

### Direct callers
- [ApiSetpLoadSchemaExtension](../../page/7D/ApiSetpLoadSchemaExtension_function_007D9A0C.md) at `0x007D9ADD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x006628AA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00662CC5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00662684  48 8B C4                        mov rax, rsp
00662687  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
0066268B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0066268F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00662693  55                              push rbp
00662694  56                              push rsi
00662695  57                              push rdi
00662696  41 54                           push r12
00662698  41 55                           push r13
0066269A  41 56                           push r14
0066269C  41 57                           push r15
0066269E  48 8D 68 A1                     lea rbp, [rax - 0x5f]
006626A2  48 81 EC B0 00 00 00            sub rsp, 0xb0
006626A9  4C 8B 21                        mov r12, qword ptr [rcx]
006626AC  4D 8B F8                        mov r15, r8
006626AF  41 80 3C 24 07                  cmp byte ptr [r12], 7
006626B4  0F 84 66 06 00 00               je 0x140662d20
006626BA  41 8B 04 24                     mov eax, dword ptr [r12]
006626BE  83 F8 06                        cmp eax, 6
006626C1  75 14                           jne 0x1406626d7
006626C3  41 83 7C 24 10 08               cmp dword ptr [r12 + 0x10], 8
006626C9  76 15                           jbe 0x1406626e0
006626CB  41 80 7C 24 1C 07               cmp byte ptr [r12 + 0x1c], 7
006626D1  0F 84 49 06 00 00               je 0x140662d20
006626D7  83 F8 05                        cmp eax, 5
006626DA  0F 82 39 06 00 00               jb 0x140662d19
006626E0  41 83 38 05                     cmp dword ptr [r8], 5
006626E4  0F 82 2F 06 00 00               jb 0x140662d19
006626EA  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
006626EF  A8 01                           test al, 1
006626F1  74 0A                           je 0x1406626fd
006626F3  B8 0D 00 00 C0                  mov eax, 0xc000000d
006626F8  E9 28 06 00 00                  jmp 0x140662d25
006626FD  41 83 78 0C 00                  cmp dword ptr [r8 + 0xc], 0
00662702  75 07                           jne 0x14066270b
00662704  33 C0                           xor eax, eax
00662706  E9 1A 06 00 00                  jmp 0x140662d25
0066270B  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
00662710  45 33 ED                        xor r13d, r13d
00662713  49 8B CC                        mov rcx, r12
00662716  44 89 6D 9F                     mov dword ptr [rbp - 0x61], r13d
0066271A  45 33 F6                        xor r14d, r14d
0066271D  E8 6A FB FF FF                  call 0x14066228c
00662722  8B D8                           mov ebx, eax
00662724  85 C0                           test eax, eax
00662726  0F 88 9E 05 00 00               js 0x140662cca
0066272C  41 8B 57 04                     mov edx, dword ptr [r15 + 4]
00662730  49 8B CF                        mov rcx, r15
00662733  E8 54 FB FF FF                  call 0x14066228c
00662738  8B D8                           mov ebx, eax
0066273A  85 C0                           test eax, eax
0066273C  0F 88 88 05 00 00               js 0x140662cca
00662742  33 F6                           xor esi, esi
00662744  41 3B 77 0C                     cmp esi, dword ptr [r15 + 0xc]
00662748  0F 83 32 01 00 00               jae 0x140662880
0066274E  41 8B 7F 10                     mov edi, dword ptr [r15 + 0x10]
00662752  48 8D 1C 76                     lea rbx, [rsi + rsi*2]
00662756  49 03 FF                        add rdi, r15
00662759  8B 04 DF                        mov eax, dword ptr [rdi + rbx*8]
0066275C  A8 04                           test al, 4
0066275E  74 19                           je 0x140662779
00662760  8B 44 DF 08                     mov eax, dword ptr [rdi + rbx*8 + 8]
00662764  41 FF C5                        inc r13d
00662767  83 C0 03                        add eax, 3
0066276A  44 89 6D 9F                     mov dword ptr [rbp - 0x61], r13d
0066276E  83 E0 FC                        and eax, 0xfffffffc
00662771  44 03 F0                        add r14d, eax
00662774  E9 EC 00 00 00                  jmp 0x140662865
00662779  45 32 ED                        xor r13b, r13b
0066277C  33 C0                           xor eax, eax
0066277E  89 45 A3                        mov dword ptr [rbp - 0x5d], eax
00662781  3B 44 DF 14                     cmp eax, dword ptr [rdi + rbx*8 + 0x14]
00662785  0F 83 D6 00 00 00               jae 0x140662861
0066278B  8B 54 DF 10                     mov edx, dword ptr [rdi + rbx*8 + 0x10]
0066278F  48 8D 0C 80                     lea rcx, [rax + rax*4]
00662793  49 03 D7                        add rdx, r15
00662796  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
0066279A  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
0066279E  44 8B 4C 8A 0C                  mov r9d, dword ptr [rdx + rcx*4 + 0xc]
006627A3  44 8B 44 8A 10                  mov r8d, dword ptr [rdx + rcx*4 + 0x10]
006627A8  4D 03 CF                        add r9, r15
006627AB  4B 8D 04 01                     lea rax, [r9 + r8]
006627AF  41 83 F8 01                     cmp r8d, 1
006627B3  76 0E                           jbe 0x1406627c3
006627B5  48 83 E8 02                     sub rax, 2
006627B9  41 83 C0 FE                     add r8d, -2
006627BD  66 83 38 2D                     cmp word ptr [rax], 0x2d
006627C1  75 EC                           jne 0x1406627af
006627C3  66 41 D1 E8                     shr r8w, 1
006627C7  0F 84 A9 00 00 00               je 0x140662876
006627CD  8B 44 8A 04                     mov eax, dword ptr [rdx + rcx*4 + 4]
006627D1  49 8B D1                        mov rdx, r9
006627D4  49 8B CC                        mov rcx, r12
006627D7  89 45 A7                        mov dword ptr [rbp - 0x59], eax
006627DA  E8 69 58 E5 FF                  call 0x1404b8048
006627DF  48 8B C8                        mov rcx, rax
006627E2  48 85 C0                        test rax, rax
006627E5  75 32                           jne 0x140662819
006627E7  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
006627EB  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
006627EF  FF 45 9F                        inc dword ptr [rbp - 0x61]
006627F2  8B 44 81 10                     mov eax, dword ptr [rcx + rax*4 + 0x10]
006627F6  83 C0 03                        add eax, 3
006627F9  83 E0 FC                        and eax, 0xfffffffc
006627FC  83 C0 14                        add eax, 0x14
006627FF  44 03 F0                        add r14d, eax
00662802  45 84 ED                        test r13b, r13b
00662805  75 50                           jne 0x140662857
00662807  8B 44 DF 08                     mov eax, dword ptr [rdi + rbx*8 + 8]
0066280B  41 B5 01                        mov r13b, 1
0066280E  83 C0 03                        add eax, 3
00662811  83 E0 FC                        and eax, 0xfffffffc
00662814  44 03 F0                        add r14d, eax
00662817  EB 3E                           jmp 0x140662857
00662819  8B 00                           mov eax, dword ptr [rax]
0066281B  A8 01                           test al, 1
0066281D  75 38                           jne 0x140662857
0066281F  45 84 ED                        test r13b, r13b
00662822  75 10                           jne 0x140662834
00662824  8B 44 DF 08                     mov eax, dword ptr [rdi + rbx*8 + 8]
00662828  41 B5 01                        mov r13b, 1
0066282B  83 C0 03                        add eax, 3
0066282E  83 E0 FC                        and eax, 0xfffffffc
00662831  44 03 F0                        add r14d, eax
00662834  8B 51 14                        mov edx, dword ptr [rcx + 0x14]
00662837  85 D2                           test edx, edx
00662839  74 31                           je 0x14066286c
0066283B  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0066283E  42 83 7C 20 10 00               cmp dword ptr [rax + r12 + 0x10], 0
00662844  74 11                           je 0x140662857
00662846  83 7D A7 00                     cmp dword ptr [rbp - 0x59], 0
0066284A  74 0B                           je 0x140662857
0066284C  8D 04 92                        lea eax, [rdx + rdx*4]
0066284F  45 8D 34 86                     lea r14d, [r14 + rax*4]
00662853  41 83 C6 14                     add r14d, 0x14
00662857  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
0066285A  FF C0                           inc eax
0066285C  E9 1D FF FF FF                  jmp 0x14066277e
00662861  44 8B 6D 9F                     mov r13d, dword ptr [rbp - 0x61]
00662865  FF C6                           inc esi
00662867  E9 D8 FE FF FF                  jmp 0x140662744
0066286C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00662871  E9 54 04 00 00                  jmp 0x140662cca
00662876  BB 82 04 00 C0                  mov ebx, 0xc0000482
0066287B  E9 4A 04 00 00                  jmp 0x140662cca
00662880  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00662885  47 8D 6C 6D 00                  lea r13d, [r13 + r13*2]
0066288A  8B 4D 9F                        mov ecx, dword ptr [rbp - 0x61]
0066288D  41 B8 41 53 63 68               mov r8d, 0x68635341
00662893  41 C1 E5 03                     shl r13d, 3
00662897  8D 04 C8                        lea eax, [rax + rcx*8]
0066289A  B9 00 01 00 00                  mov ecx, 0x100
0066289F  41 03 C5                        add eax, r13d
006628A2  41 03 C6                        add eax, r14d
006628A5  8B D0                           mov edx, eax
006628A7  89 45 A7                        mov dword ptr [rbp - 0x59], eax
006628AA  E8 41 F8 51 00                  call 0x140b820f0
006628AF  48 8B F0                        mov rsi, rax
006628B2  48 85 C0                        test rax, rax
006628B5  75 0A                           jne 0x1406628c1
006628B7  BB 17 00 00 C0                  mov ebx, 0xc0000017
006628BC  E9 09 04 00 00                  jmp 0x140662cca
006628C1  41 8B 44 24 0C                  mov eax, dword ptr [r12 + 0xc]
006628C6  49 8B D4                        mov rdx, r12
006628C9  8D 0C 40                        lea ecx, [rax + rax*2]
006628CC  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
006628D1  8D 1C C8                        lea ebx, [rax + rcx*8]
006628D4  48 8B CE                        mov rcx, rsi
006628D7  44 8B C3                        mov r8d, ebx
006628DA  8B FB                           mov edi, ebx
006628DC  E8 5F 3F 06 00                  call 0x1406c6840
006628E1  41 8B 44 24 14                  mov eax, dword ptr [r12 + 0x14]
006628E6  42 8D 0C 2B                     lea ecx, [rbx + r13]
006628EA  2B C3                           sub eax, ebx
006628EC  4A 8D 14 27                     lea rdx, [rdi + r12]
006628F0  44 8B C0                        mov r8d, eax
006628F3  8D 1C 08                        lea ebx, [rax + rcx]
006628F6  48 03 CE                        add rcx, rsi
006628F9  89 5D 9B                        mov dword ptr [rbp - 0x65], ebx
006628FC  89 5D 97                        mov dword ptr [rbp - 0x69], ebx
006628FF  E8 3C 3F 06 00                  call 0x1406c6840
00662904  8B CB                           mov ecx, ebx
00662906  33 D2                           xor edx, edx
00662908  48 03 CE                        add rcx, rsi
0066290B  45 8B C6                        mov r8d, r14d
0066290E  E8 2D 43 06 00                  call 0x1406c6c40
00662913  45 8B 44 24 0C                  mov r8d, dword ptr [r12 + 0xc]
00662918  41 03 DE                        add ebx, r14d
0066291B  41 8B 54 24 14                  mov edx, dword ptr [r12 + 0x14]
00662920  8B CB                           mov ecx, ebx
00662922  49 03 D4                        add rdx, r12
00662925  48 03 CE                        add rcx, rsi
00662928  41 C1 E0 03                     shl r8d, 3
0066292C  E8 0F 3F 06 00                  call 0x1406c6840
00662931  44 8B 75 A7                     mov r14d, dword ptr [rbp - 0x59]
00662935  44 89 76 04                     mov dword ptr [rsi + 4], r14d
00662939  89 5E 14                        mov dword ptr [rsi + 0x14], ebx
0066293C  45 85 ED                        test r13d, r13d
0066293F  74 7C                           je 0x1406629bd
00662941  45 33 DB                        xor r11d, r11d
00662944  44 39 5E 0C                     cmp dword ptr [rsi + 0xc], r11d
00662948  76 73                           jbe 0x1406629bd
0066294A  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
0066294D  4B 8D 0C 5B                     lea rcx, [r11 + r11*2]
00662951  48 03 D6                        add rdx, rsi
00662954  8B 44 CA 04                     mov eax, dword ptr [rdx + rcx*8 + 4]
00662958  85 C0                           test eax, eax
0066295A  74 07                           je 0x140662963
0066295C  41 03 C5                        add eax, r13d
0066295F  89 44 CA 04                     mov dword ptr [rdx + rcx*8 + 4], eax
00662963  8B 44 CA 10                     mov eax, dword ptr [rdx + rcx*8 + 0x10]
00662967  85 C0                           test eax, eax
00662969  74 07                           je 0x140662972
0066296B  41 03 C5                        add eax, r13d
0066296E  89 44 CA 10                     mov dword ptr [rdx + rcx*8 + 0x10], eax
00662972  45 33 C0                        xor r8d, r8d
00662975  44 39 44 CA 14                  cmp dword ptr [rdx + rcx*8 + 0x14], r8d
0066297A  76 38                           jbe 0x1406629b4
0066297C  44 8B 54 CA 10                  mov r10d, dword ptr [rdx + rcx*8 + 0x10]
00662981  4F 8D 0C 80                     lea r9, [r8 + r8*4]
00662985  4C 03 D6                        add r10, rsi
00662988  43 8B 44 8A 04                  mov eax, dword ptr [r10 + r9*4 + 4]
0066298D  85 C0                           test eax, eax
0066298F  74 08                           je 0x140662999
00662991  41 03 C5                        add eax, r13d
00662994  43 89 44 8A 04                  mov dword ptr [r10 + r9*4 + 4], eax
00662999  43 8B 44 8A 0C                  mov eax, dword ptr [r10 + r9*4 + 0xc]
0066299E  85 C0                           test eax, eax
006629A0  74 08                           je 0x1406629aa
006629A2  41 03 C5                        add eax, r13d
006629A5  43 89 44 8A 0C                  mov dword ptr [r10 + r9*4 + 0xc], eax
006629AA  41 FF C0                        inc r8d
006629AD  44 3B 44 CA 14                  cmp r8d, dword ptr [rdx + rcx*8 + 0x14]
006629B2  72 C8                           jb 0x14066297c
006629B4  41 FF C3                        inc r11d
006629B7  44 3B 5E 0C                     cmp r11d, dword ptr [rsi + 0xc]
006629BB  72 8D                           jb 0x14066294a
006629BD  41 8B D6                        mov edx, r14d
006629C0  48 8B CE                        mov rcx, rsi
006629C3  E8 C4 F8 FF FF                  call 0x14066228c
006629C8  8B D8                           mov ebx, eax
006629CA  85 C0                           test eax, eax
006629CC  0F 88 EE 02 00 00               js 0x140662cc0
006629D2  33 C9                           xor ecx, ecx
006629D4  89 4D A3                        mov dword ptr [rbp - 0x5d], ecx
006629D7  33 FF                           xor edi, edi
006629D9  89 7D A7                        mov dword ptr [rbp - 0x59], edi
006629DC  41 3B 7F 0C                     cmp edi, dword ptr [r15 + 0xc]
006629E0  0F 83 F6 02 00 00               jae 0x140662cdc
006629E6  45 8B 4F 10                     mov r9d, dword ptr [r15 + 0x10]
006629EA  4C 8D 04 7F                     lea r8, [rdi + rdi*2]
006629EE  4D 03 CF                        add r9, r15
006629F1  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
006629F5  4C 89 4D E7                     mov qword ptr [rbp - 0x19], r9
006629F9  43 8B 5C C1 04                  mov ebx, dword ptr [r9 + r8*8 + 4]
006629FE  43 8B 04 C1                     mov eax, dword ptr [r9 + r8*8]
00662A02  49 03 DF                        add rbx, r15
00662A05  47 8B 5C C1 08                  mov r11d, dword ptr [r9 + r8*8 + 8]
00662A0A  44 89 5D AB                     mov dword ptr [rbp - 0x55], r11d
00662A0E  48 89 5D D7                     mov qword ptr [rbp - 0x29], rbx
00662A12  A8 04                           test al, 4
00662A14  74 71                           je 0x140662a87
00662A16  3B 4D 9F                        cmp ecx, dword ptr [rbp - 0x61]
00662A19  0F 83 9C 02 00 00               jae 0x140662cbb
00662A1F  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
00662A22  FF C1                           inc ecx
00662A24  48 03 D6                        add rdx, rsi
00662A27  89 4D A3                        mov dword ptr [rbp - 0x5d], ecx
00662A2A  8B 4E 0C                        mov ecx, dword ptr [rsi + 0xc]
00662A2D  0F 57 C0                        xorps xmm0, xmm0
00662A30  4C 8D 14 49                     lea r10, [rcx + rcx*2]
00662A34  8D 41 01                        lea eax, [rcx + 1]
00662A37  48 8B CE                        mov rcx, rsi
00662A3A  89 46 0C                        mov dword ptr [rsi + 0xc], eax
00662A3D  33 C0                           xor eax, eax
00662A3F  42 0F 11 04 D2                  movups xmmword ptr [rdx + r10*8], xmm0
00662A44  4A 89 44 D2 10                  mov qword ptr [rdx + r10*8 + 0x10], rax
00662A49  43 8B 04 C1                     mov eax, dword ptr [r9 + r8*8]
00662A4D  45 8B CB                        mov r9d, r11d
00662A50  42 89 04 D2                     mov dword ptr [rdx + r10*8], eax
00662A54  4C 8B C3                        mov r8, rbx
00662A57  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00662A5A  42 89 44 D2 04                  mov dword ptr [rdx + r10*8 + 4], eax
00662A5F  46 89 5C D2 08                  mov dword ptr [rdx + r10*8 + 8], r11d
00662A64  46 89 5C D2 0C                  mov dword ptr [rdx + r10*8 + 0xc], r11d
00662A69  48 8D 55 97                     lea rdx, [rbp - 0x69]
00662A6D  E8 06 03 00 00                  call 0x140662d78
00662A72  8B D8                           mov ebx, eax
00662A74  85 C0                           test eax, eax
00662A76  0F 88 44 02 00 00               js 0x140662cc0
00662A7C  8B 55 97                        mov edx, dword ptr [rbp - 0x69]
00662A7F  89 55 9B                        mov dword ptr [rbp - 0x65], edx
00662A82  E9 2A 02 00 00                  jmp 0x140662cb1
00662A87  45 33 ED                        xor r13d, r13d
00662A8A  44 89 6D AF                     mov dword ptr [rbp - 0x51], r13d
00662A8E  33 C0                           xor eax, eax
00662A90  89 45 B7                        mov dword ptr [rbp - 0x49], eax
00662A93  43 3B 44 C1 14                  cmp eax, dword ptr [r9 + r8*8 + 0x14]
00662A98  0F 83 10 02 00 00               jae 0x140662cae
00662A9E  43 8B 54 C1 10                  mov edx, dword ptr [r9 + r8*8 + 0x10]
00662AA3  48 8D 0C 80                     lea rcx, [rax + rax*4]
00662AA7  49 03 D7                        add rdx, r15
00662AAA  48 89 4D C7                     mov qword ptr [rbp - 0x39], rcx
00662AAE  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00662AB2  44 8B 6C 8A 0C                  mov r13d, dword ptr [rdx + rcx*4 + 0xc]
00662AB7  8B 5C 8A 10                     mov ebx, dword ptr [rdx + rcx*4 + 0x10]
00662ABB  4D 03 EF                        add r13, r15
00662ABE  4A 8D 04 2B                     lea rax, [rbx + r13]
00662AC2  83 FB 01                        cmp ebx, 1
00662AC5  76 0D                           jbe 0x140662ad4
00662AC7  48 83 E8 02                     sub rax, 2
00662ACB  83 C3 FE                        add ebx, -2
00662ACE  66 83 38 2D                     cmp word ptr [rax], 0x2d
00662AD2  75 EE                           jne 0x140662ac2
00662AD4  44 0F B7 C3                     movzx r8d, bx
00662AD8  66 41 D1 E8                     shr r8w, 1
00662ADC  0F 84 F3 01 00 00               je 0x140662cd5
00662AE2  8B 44 8A 04                     mov eax, dword ptr [rdx + rcx*4 + 4]
00662AE6  49 8B D5                        mov rdx, r13
00662AE9  48 8B CE                        mov rcx, rsi
00662AEC  89 45 BF                        mov dword ptr [rbp - 0x41], eax
00662AEF  E8 54 55 E5 FF                  call 0x1404b8048
00662AF4  48 8B F8                        mov rdi, rax
00662AF7  48 85 C0                        test rax, rax
00662AFA  0F 85 AE 00 00 00               jne 0x140662bae
00662B00  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
00662B03  3B 45 9F                        cmp eax, dword ptr [rbp - 0x61]
00662B06  0F 83 AF 01 00 00               jae 0x140662cbb
00662B0C  44 8B 4E 0C                     mov r9d, dword ptr [rsi + 0xc]
00662B10  FF C0                           inc eax
00662B12  8B 4E 10                        mov ecx, dword ptr [rsi + 0x10]
00662B15  0F 57 C0                        xorps xmm0, xmm0
00662B18  89 45 A3                        mov dword ptr [rbp - 0x5d], eax
00662B1B  48 03 CE                        add rcx, rsi
00662B1E  4D 8B C5                        mov r8, r13
00662B21  4B 8D 14 49                     lea rdx, [r9 + r9*2]
00662B25  41 8D 41 01                     lea eax, [r9 + 1]
00662B29  4C 8B 4D C7                     mov r9, qword ptr [rbp - 0x39]
00662B2D  89 46 0C                        mov dword ptr [rsi + 0xc], eax
00662B30  48 8D 3C D1                     lea rdi, [rcx + rdx*8]
00662B34  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00662B38  48 8D 55 97                     lea rdx, [rbp - 0x69]
00662B3C  0F 11 07                        movups xmmword ptr [rdi], xmm0
00662B3F  33 C0                           xor eax, eax
00662B41  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00662B45  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00662B48  89 47 04                        mov dword ptr [rdi + 4], eax
00662B4B  42 8B 44 89 10                  mov eax, dword ptr [rcx + r9*4 + 0x10]
00662B50  89 47 08                        mov dword ptr [rdi + 8], eax
00662B53  89 5F 0C                        mov dword ptr [rdi + 0xc], ebx
00662B56  46 8B 4C 89 10                  mov r9d, dword ptr [rcx + r9*4 + 0x10]
00662B5B  48 8B CE                        mov rcx, rsi
00662B5E  E8 15 02 00 00                  call 0x140662d78
00662B63  8B D8                           mov ebx, eax
00662B65  85 C0                           test eax, eax
00662B67  0F 88 53 01 00 00               js 0x140662cc0
00662B6D  33 C0                           xor eax, eax
00662B6F  C7 47 14 01 00 00 00            mov dword ptr [rdi + 0x14], 1
00662B76  89 45 17                        mov dword ptr [rbp + 0x17], eax
00662B79  4C 8D 45 07                     lea r8, [rbp + 7]
00662B7D  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00662B80  48 8D 55 97                     lea rdx, [rbp - 0x69]
00662B84  0F 57 C0                        xorps xmm0, xmm0
00662B87  89 47 10                        mov dword ptr [rdi + 0x10], eax
00662B8A  41 B9 14 00 00 00               mov r9d, 0x14
00662B90  48 8B CE                        mov rcx, rsi
00662B93  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00662B97  E8 DC 01 00 00                  call 0x140662d78
00662B9C  8B D8                           mov ebx, eax
00662B9E  85 C0                           test eax, eax
00662BA0  0F 88 1A 01 00 00               js 0x140662cc0
00662BA6  8B 55 97                        mov edx, dword ptr [rbp - 0x69]
00662BA9  89 55 9B                        mov dword ptr [rbp - 0x65], edx
00662BAC  EB 03                           jmp 0x140662bb1
00662BAE  8B 55 9B                        mov edx, dword ptr [rbp - 0x65]
00662BB1  8B 07                           mov eax, dword ptr [rdi]
00662BB3  A8 01                           test al, 1
00662BB5  0F 85 E1 00 00 00               jne 0x140662c9c
00662BBB  44 8B 6D AF                     mov r13d, dword ptr [rbp - 0x51]
00662BBF  45 85 ED                        test r13d, r13d
00662BC2  75 2A                           jne 0x140662bee
00662BC4  44 8B 4D AB                     mov r9d, dword ptr [rbp - 0x55]
00662BC8  44 8B EA                        mov r13d, edx
00662BCB  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00662BCF  48 8B CE                        mov rcx, rsi
00662BD2  89 55 AF                        mov dword ptr [rbp - 0x51], edx
00662BD5  48 8D 55 97                     lea rdx, [rbp - 0x69]
00662BD9  E8 9A 01 00 00                  call 0x140662d78
00662BDE  8B D8                           mov ebx, eax
00662BE0  85 C0                           test eax, eax
00662BE2  0F 88 D8 00 00 00               js 0x140662cc0
00662BE8  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00662BEB  89 45 9B                        mov dword ptr [rbp - 0x65], eax
00662BEE  83 7F 14 00                     cmp dword ptr [rdi + 0x14], 0
00662BF2  0F 84 D6 00 00 00               je 0x140662cce
00662BF8  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
00662BFB  48 03 CE                        add rcx, rsi
00662BFE  83 79 10 00                     cmp dword ptr [rcx + 0x10], 0
00662C02  74 7F                           je 0x140662c83
00662C04  83 7D BF 00                     cmp dword ptr [rbp - 0x41], 0
00662C08  74 79                           je 0x140662c83
00662C0A  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00662C0D  48 8D 55 97                     lea rdx, [rbp - 0x69]
00662C11  89 41 08                        mov dword ptr [rcx + 8], eax
00662C14  4C 8B C1                        mov r8, rcx
00662C17  44 89 69 04                     mov dword ptr [rcx + 4], r13d
00662C1B  48 8B CE                        mov rcx, rsi
00662C1E  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
00662C21  44 8D 0C 80                     lea r9d, [rax + rax*4]
00662C25  41 C1 E1 02                     shl r9d, 2
00662C29  E8 4A 01 00 00                  call 0x140662d78
00662C2E  8B D8                           mov ebx, eax
00662C30  85 C0                           test eax, eax
00662C32  0F 88 88 00 00 00               js 0x140662cc0
00662C38  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00662C3B  4C 8D 45 EF                     lea r8, [rbp - 0x11]
00662C3F  48 83 65 EF 00                  and qword ptr [rbp - 0x11], 0
00662C44  48 8D 55 97                     lea rdx, [rbp - 0x69]
00662C48  83 65 F7 00                     and dword ptr [rbp - 9], 0
00662C4C  41 B9 14 00 00 00               mov r9d, 0x14
00662C52  89 47 10                        mov dword ptr [rdi + 0x10], eax
00662C55  48 8B CE                        mov rcx, rsi
00662C58  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00662C5B  89 45 FF                        mov dword ptr [rbp - 1], eax
00662C5E  44 89 6D FB                     mov dword ptr [rbp - 5], r13d
00662C62  E8 11 01 00 00                  call 0x140662d78
00662C67  8B D8                           mov ebx, eax
00662C69  85 C0                           test eax, eax
00662C6B  78 53                           js 0x140662cc0
00662C6D  FF 47 14                        inc dword ptr [rdi + 0x14]
00662C70  48 8B D7                        mov rdx, rdi
00662C73  48 8B CE                        mov rcx, rsi
00662C76  E8 E5 02 00 00                  call 0x140662f60
00662C7B  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00662C7E  89 45 9B                        mov dword ptr [rbp - 0x65], eax
00662C81  EB 19                           jmp 0x140662c9c
00662C83  83 61 04 00                     and dword ptr [rcx + 4], 0
00662C87  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00662C8A  83 61 08 00                     and dword ptr [rcx + 8], 0
00662C8E  44 89 69 0C                     mov dword ptr [rcx + 0xc], r13d
00662C92  89 41 10                        mov dword ptr [rcx + 0x10], eax
00662C95  C7 47 14 01 00 00 00            mov dword ptr [rdi + 0x14], 1
00662C9C  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
00662C9F  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
00662CA3  FF C0                           inc eax
00662CA5  4C 8B 4D E7                     mov r9, qword ptr [rbp - 0x19]
00662CA9  E9 E2 FD FF FF                  jmp 0x140662a90
00662CAE  8B 7D A7                        mov edi, dword ptr [rbp - 0x59]
00662CB1  8B 4D A3                        mov ecx, dword ptr [rbp - 0x5d]
00662CB4  FF C7                           inc edi
00662CB6  E9 1E FD FF FF                  jmp 0x1406629d9
00662CBB  BB 05 00 00 80                  mov ebx, 0x80000005
00662CC0  48 8B CE                        mov rcx, rsi
00662CC3  33 D2                           xor edx, edx
00662CC5  E8 A6 FB 51 00                  call 0x140b82870
00662CCA  8B C3                           mov eax, ebx
00662CCC  EB 57                           jmp 0x140662d25
00662CCE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00662CD3  EB EB                           jmp 0x140662cc0
00662CD5  BB 82 04 00 C0                  mov ebx, 0xc0000482
00662CDA  EB E4                           jmp 0x140662cc0
00662CDC  83 7D 9F 00                     cmp dword ptr [rbp - 0x61], 0
00662CE0  76 13                           jbe 0x140662cf5
00662CE2  48 8B CE                        mov rcx, rsi
00662CE5  E8 26 01 00 00                  call 0x140662e10
00662CEA  85 C0                           test eax, eax
00662CEC  75 07                           jne 0x140662cf5
00662CEE  BB 01 00 00 C0                  mov ebx, 0xc0000001
00662CF3  EB CB                           jmp 0x140662cc0
00662CF5  41 8B D6                        mov edx, r14d
00662CF8  48 8B CE                        mov rcx, rsi
00662CFB  E8 8C F5 FF FF                  call 0x14066228c
00662D00  8B D8                           mov ebx, eax
00662D02  85 C0                           test eax, eax
00662D04  78 BA                           js 0x140662cc0
00662D06  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00662D0A  49 8B CC                        mov rcx, r12
00662D0D  48 89 30                        mov qword ptr [rax], rsi
00662D10  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00662D14  44 89 30                        mov dword ptr [rax], r14d
00662D17  EB AA                           jmp 0x140662cc3
00662D19  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00662D1E  EB 05                           jmp 0x140662d25
00662D20  E8 A7 0F 00 00                  call 0x140663ccc
00662D25  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00662D2D  48 81 C4 B0 00 00 00            add rsp, 0xb0
00662D34  41 5F                           pop r15
00662D36  41 5E                           pop r14
00662D38  41 5D                           pop r13
00662D3A  41 5C                           pop r12
00662D3C  5F                              pop rdi
00662D3D  5E                              pop rsi
00662D3E  5D                              pop rbp
00662D3F  C3                              ret
00662D40  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ApiSetComposeSchema(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1))) == 7) goto loc_00662D20;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) != 6) goto loc_006626D7;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) <= 8) goto loc_006626E0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 28)) == 7) goto loc_00662D20;
loc_006626D7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) < 5) goto loc_00662D19;
loc_006626E0:
    if ((*(unsigned int *)(a3)) < 5) goto loc_00662D19;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)))) & (1)) == 0) goto loc_006626FD;
    goto loc_00662D25;
loc_006626FD:
    if ((*(unsigned int *)(a3 + 12)) != 0) goto loc_0066270B;
    result = 0;
    goto loc_00662D25;
loc_0066270B:
    v_r13 = 0;
    *(unsigned int *)(v_rsp - 95 - 97) = 0;
    v_r14 = 0;
    result = ApiSetValidateSchemaFormat(*(unsigned __int64 *)(a1), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 4)), a3, a4);
    if (sign_flag) goto loc_00662CCA;
    result = ApiSetValidateSchemaFormat(a3, (unsigned int)(*(unsigned int *)(a3 + 4)), a3, a4);
    if (sign_flag) goto loc_00662CCA;
    v_rsi = 0;
loc_00662744:
    if (0 >= (*(unsigned int *)(a3 + 12))) goto loc_00662880;
    v_rdi = ((unsigned int)(*(unsigned int *)(a3 + 16))) + (a3);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + v_rsi + v_rsi * 2 * 8)))) & (4)) == 0) goto loc_00662779;
    v_r13 = (unsigned int)((v_r13) + 1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + v_rsi + v_rsi * 2 * 8 + 8))) + (3));
    *(unsigned int *)(v_rsp - 95 - 97) = (unsigned int)(v_r13);
    result = (unsigned int)((result) & (0xFFFFFFFCULL));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    goto loc_00662865;
loc_00662779:
    v_r13 = 0;
    result = 0;
loc_0066277E:
    *(unsigned int *)(v_rsp - 95 - 93) = 0;
    if (0 >= (*(unsigned int *)(v_rdi + v_rsi + v_rsi * 2 * 8 + 20))) goto loc_00662861;
    a2 = ((unsigned int)(*(unsigned int *)(v_rdi + v_rsi + v_rsi * 2 * 8 + 16))) + (a3);
    *(unsigned __int64 *)(v_rsp - 95 - 65) = result + result * 4;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = a2;
    a4 = ((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 12))) + (a3);
loc_006627AF:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 16)))) <= 1) goto loc_006627C3;
    result = (a4 + (unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 16)) * 1) - (2);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 16))) + (-2));
    if ((*(unsigned __int16 *)(result)) != 45) goto loc_006627AF;
loc_006627C3:
    a3 = (unsigned __int16)((a3) >> (1));
    if (condition_is_equal) goto loc_00662876;
    *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 4)));
    result = ApiSetpSearchForApiSet(*(unsigned __int64 *)(a1), a4, a3, a4);
    if (result != 0) goto loc_00662819;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 73) + *(unsigned __int64 *)(v_rsp - 95 - 65) * 4 + 16))) + (3));
    result = (unsigned int)((result) & (0xFFFFFFFCULL));
    result = (unsigned int)((result) + (20));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    if (0 != 0) goto loc_00662857;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + v_rsi + v_rsi * 2 * 8 + 8))) + (3));
    result = (unsigned int)((result) & (0xFFFFFFFCULL));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    goto loc_00662857;
loc_00662819:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (1)) != 0) goto loc_00662857;
    result = (unsigned int)(*(unsigned int *)(result));
    v_r13 = 1;
    if (1 == 0) {
        result = *(unsigned int *)(v_rdi + v_rsi + v_rsi * 2 * 8 + 8);
        v_r13 = 1;
        result = (unsigned int)((result) + (3));
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 73) + 20))) == 0) goto loc_0066286C;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 73) + 16)) + *(unsigned __int64 *)(a1) * 1 + 16)) == 0) goto loc_00662857;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 73) + 16));
    if ((*(unsigned int *)(v_rsp - 95 - 89)) != 0) {
        result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 73) + 20)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 73) + 20)) * 4;
        v_r14 = v_r14 + result * 4;
        v_r14 = (unsigned int)((v_r14) + (20));
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93))) + 1);
    goto loc_0066277E;
loc_00662861:
loc_00662865:
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_00662744;
loc_0066286C:
    goto loc_00662CCA;
loc_00662876:
    goto loc_00662CCA;
loc_00662880:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)) * 2) << (3));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 4)) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)) * 8) + ((unsigned int)(v_r13)));
    result = (unsigned int)((result) + ((unsigned int)(v_r14)));
    *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)(result);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x68635341ULL), a4);
    if (result != 0) goto loc_006628C1;
    goto loc_00662CCA;
loc_006628C1:
    result = memcpy(result, *(unsigned __int64 *)(a1), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8)), a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 20))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8)));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8 + v_r13 * 1) + (result);
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)(result + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8 + v_r13 * 1 * 1);
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(result + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8 + v_r13 * 1 * 1);
    result = memcpy(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8)) + *(unsigned __int64 *)(a1) * 1, (unsigned int)((unsigned int)(result)), a4);
    a2 = 0;
    a1 = ((unsigned int)((unsigned int)(result + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8 + v_r13 * 1 * 1))) + (result);
    result = memset(a1, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    v_rbx = (unsigned int)((result + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) * 2 * 8 + v_r13 * 1 * 1) + ((unsigned int)(v_r14)));
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 20))) + (*(unsigned __int64 *)(a1));
    a1 = ((unsigned int)((unsigned int)(v_rbx))) + (result);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12))) << (3));
    result = memcpy(a1, a2, a3, a4);
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)));
    *(unsigned int *)(result + 20) = (unsigned int)(v_rbx);
    if ((unsigned int)(v_r13) == 0) goto loc_006629BD;
    v_r11 = 0;
    if ((*(unsigned int *)(result + 12)) <= 0) goto loc_006629BD;
loc_0066294A:
    a2 = ((unsigned int)(*(unsigned int *)(result + 16))) + (result);
    result = (unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 4));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 4))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 4))) + ((unsigned int)(v_r13)));
        *(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 4) = (unsigned int)(result);
    }
    result = (unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 16));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 16))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 16))) + ((unsigned int)(v_r13)));
        *(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 16) = (unsigned int)(result);
    }
    a3 = 0;
    if ((*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 20)) <= 0) goto loc_006629B4;
loc_0066297C:
    v_r10 = ((unsigned int)(*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 16))) + (result);
    result = (unsigned int)(*(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 4));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 4))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 4))) + ((unsigned int)(v_r13)));
        *(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 4) = (unsigned int)(result);
    }
    result = (unsigned int)(*(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 12));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 12))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 12))) + ((unsigned int)(v_r13)));
        *(unsigned int *)(v_r10 + a3 + a3 * 4 * 4 + 12) = (unsigned int)(result);
    }
    a3 = (unsigned int)((a3) + 1);
    if (((unsigned int)(a3)) < (*(unsigned int *)(a2 + v_r11 + v_r11 * 2 * 8 + 20))) goto loc_0066297C;
loc_006629B4:
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) < (*(unsigned int *)(result + 12))) goto loc_0066294A;
loc_006629BD:
    result = ApiSetValidateSchemaFormat(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), a3, a3 + a3 * 4);
    if (sign_flag) goto loc_00662CC0;
    a1 = 0;
    *(unsigned int *)(v_rsp - 95 - 93) = 0;
    v_rdi = 0;
loc_006629D9:
    *(unsigned int *)(v_rsp - 95 - 89) = 0;
    if (0 >= (*(unsigned int *)(a3 + 12))) goto loc_00662CDC;
    a4 = ((unsigned int)(*(unsigned int *)(a3 + 16))) + (a3);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_rdi + v_rdi * 2;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = a4;
    v_rbx = ((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 4))) + (a3);
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)));
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_rbx;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8)))) & (4)) == 0) goto loc_00662A87;
    if (0 >= (*(unsigned int *)(v_rsp - 95 - 97))) goto loc_00662CBB;
    a1 = (unsigned int)((a1) + 1);
    a2 = ((unsigned int)(*(unsigned int *)(result + 16))) + (result);
    *(unsigned int *)(v_rsp - 95 - 93) = (unsigned int)(a1);
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)) + 1);
    result = 0;
    *(unsigned __int64 *)(a2 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8) = v_xmm0;
    *(unsigned __int64 *)(a2 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 16) = 0;
    *(unsigned int *)(a2 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8)));
    *(unsigned int *)(a2 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    *(unsigned int *)(a2 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)));
    *(unsigned int *)(a2 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)));
    result = AsiAddDataToSchema(result, v_rsp - 95 - 105, v_rbx, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)))));
    if (sign_flag) goto loc_00662CC0;
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    goto loc_00662CB1;
loc_00662A87:
    v_r13 = 0;
    *(unsigned int *)(v_rsp - 95 - 81) = 0;
    result = 0;
loc_00662A90:
    *(unsigned int *)(v_rsp - 95 - 73) = 0;
    if (0 >= (*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)))) + v_rbx * 8 + 20))) goto loc_00662CAE;
    a2 = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)))) + v_rbx * 8 + 16))) + (a3);
    *(unsigned __int64 *)(v_rsp - 95 - 57) = result + result * 4;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = a2;
    v_r13 = ((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 12))) + (a3);
loc_00662AC2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 16)))) <= 1) goto loc_00662AD4;
    result = ((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 16)) + v_r13 * 1) - (2);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 16))) + (-2));
    if ((*(unsigned __int16 *)(result)) != 45) goto loc_00662AC2;
loc_00662AD4:
    a3 = (unsigned __int16)(((unsigned __int16)(v_rbx)) >> (1));
    if (condition_is_equal) goto loc_00662CD5;
    *(unsigned int *)(v_rsp - 95 - 65) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + result + result * 4 * 4 + 4)));
    result = ApiSetpSearchForApiSet(result, v_r13, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rdi + v_rdi * 2 * 8 + 8)))));
    if (result != 0) goto loc_00662BAE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)))) >= (*(unsigned int *)(v_rsp - 95 - 97))) goto loc_00662CBB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93))) + 1);
    *(unsigned int *)(v_rsp - 95 - 93) = (unsigned int)(result);
    a1 = ((unsigned int)(*(unsigned int *)(result + 16))) + (result);
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)) + 1);
    *(unsigned __int64 *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 16) = 0;
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 49) + *(unsigned __int64 *)(v_rsp - 95 - 57) * 4 + 16)));
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 12) = (unsigned int)(v_rbx);
    result = AsiAddDataToSchema(0, v_rsp - 95 - 105, v_r13, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 49) + *(unsigned __int64 *)(v_rsp - 95 - 57) * 4 + 16)));
    if (sign_flag) goto loc_00662CC0;
    result = 0;
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 20) = 1;
    *(unsigned int *)(v_rsp - 95 + 23) = 0;
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    result = AsiAddDataToSchema(0, v_rsp - 95 - 105, v_rsp - 95 + 7, 20);
    if (sign_flag) goto loc_00662CC0;
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    goto loc_00662BB1;
loc_00662BAE:
loc_00662BB1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8)))) & (1)) != 0) goto loc_00662C9C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))) != 0) goto loc_00662BEE;
    *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    result = AsiAddDataToSchema(result, v_rsp - 95 - 105, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    if (sign_flag) goto loc_00662CC0;
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
loc_00662BEE:
    if ((*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 20)) == 0) goto loc_00662CCE;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 16))) + (result);
    if ((*(unsigned int *)(a1 + 16)) == 0) goto loc_00662C83;
    if ((*(unsigned int *)(v_rsp - 95 - 65)) == 0) goto loc_00662C83;
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)))));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 20)) + (unsigned int)(*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 20)) * 4) << (2));
    result = AsiAddDataToSchema(result, v_rsp - 95 - 105, a1, a4);
    if (sign_flag) goto loc_00662CC0;
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    *(unsigned int *)(v_rsp - 95 - 1) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    *(unsigned int *)(v_rsp - 95 - 5) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)))));
    result = AsiAddDataToSchema(result, v_rsp - 95 - 105, v_rsp - 95 - 17, 20);
    if (sign_flag) goto loc_00662CC0;
    result = AsiSortValueList(result, a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8, v_rsp - 95 - 17, 20);
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    goto loc_00662C9C;
loc_00662C83:
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)))));
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    *(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(result + 12)) + (unsigned int)(*(unsigned int *)(result + 12)) * 2 * 8 + 20) = 1;
loc_00662C9C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) + 1);
    goto loc_00662A90;
loc_00662CAE:
loc_00662CB1:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89))) + 1);
    goto loc_006629D9;
loc_00662CBB:
loc_00662CC0:
loc_00662CC3:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(v_rsp - 95 - 33), *(unsigned __int64 *)(v_rsp - 95 - 25));
loc_00662CCA:
    goto loc_00662D25;
loc_00662CCE:
    goto loc_00662CC0;
loc_00662CD5:
    goto loc_00662CC0;
loc_00662CDC:
    if ((*(unsigned int *)(v_rsp - 95 - 97)) <= 0) goto loc_00662CF5;
    result = AsiPopulateHashes(result, a2, *(unsigned __int64 *)(v_rsp - 95 - 33), *(unsigned __int64 *)(v_rsp - 95 - 25));
    if ((unsigned int)(result) != 0) goto loc_00662CF5;
    goto loc_00662CC0;
loc_00662CF5:
    result = ApiSetValidateSchemaFormat(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), *(unsigned __int64 *)(v_rsp - 95 - 33), *(unsigned __int64 *)(v_rsp - 95 - 25));
    if (sign_flag) goto loc_00662CC0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103)) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)));
    goto loc_00662CC3;
loc_00662D19:
    goto loc_00662D25;
loc_00662D20:
    result = ApiSetComposeSchema_V7(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), *(unsigned __int64 *)(v_rsp - 95 - 33), *(unsigned __int64 *)(v_rsp - 95 - 25));
loc_00662D25:
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ApiSetComposeSchema(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    if ((*(uint8_t *)(*(uint64_t *)(arg1))) == 7) goto loc_00662D20;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) != 6) goto loc_006626D7;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) <= 8) goto loc_006626E0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x1C)) == 7) goto loc_00662D20;
loc_006626D7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) < 5) goto loc_00662D19;
loc_006626E0:
    if ((*(uint32_t *)(arg3)) < 5) goto loc_00662D19;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)))) & (1)) == 0) goto loc_006626FD;
    goto loc_00662D25;
loc_006626FD:
    if ((*(uint32_t *)(arg3 + 0xC)) != 0) goto loc_0066270B;
    result = 0;
    goto loc_00662D25;
loc_0066270B:
    local_r13 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = 0;
    local_r14 = 0;
    result = ApiSetValidateSchemaFormat(*(uint64_t *)(arg1), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4)), Arg3, a4);
    if (sign_flag) goto loc_00662CCA;
    result = ApiSetValidateSchemaFormat(Arg3, (uint32_t)(*(uint32_t *)(arg3 + 0x4)), Arg3, a4);
    if (sign_flag) goto loc_00662CCA;
    local_rsi = 0;
loc_00662744:
    if (0 >= (*(uint32_t *)(arg3 + 0xC))) goto loc_00662880;
    local_rdi = ((uint32_t)(*(uint32_t *)(arg3 + 0x10))) + (Arg3);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + local_rsi + local_rsi * 2 * 8)))) & (4)) == 0) goto loc_00662779;
    local_r13 = (uint32_t)((local_r13) + 1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + local_rsi + local_rsi * 2 * 8 + 0x8))) + (3));
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = (uint32_t)(local_r13);
    result = (uint32_t)((result) & (0xFFFFFFFCULL));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    goto loc_00662865;
loc_00662779:
    local_r13 = 0;
    result = 0;
loc_0066277E:
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = 0;
    if (0 >= (*(uint32_t *)(local_rdi + local_rsi + local_rsi * 2 * 8 + 0x14))) goto loc_00662861;
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rdi + local_rsi + local_rsi * 2 * 8 + 0x10))) + (Arg3);
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = result + result * 4;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = Arg2;
    a4 = ((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0xC))) + (Arg3);
loc_006627AF:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x10)))) <= 1) goto loc_006627C3;
    result = (a4 + (uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x10)) * 1) - (2);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x10))) + (-2));
    if ((*(uint16_t *)(result)) != 45) goto loc_006627AF;
loc_006627C3:
    Arg3 = (uint16_t)((Arg3) >> (1));
    if (condition_is_equal) goto loc_00662876;
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x4)));
    result = ApiSetpSearchForApiSet(*(uint64_t *)(arg1), a4, Arg3, a4);
    if (result != 0) goto loc_00662819;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x49) + *(uint64_t *)(local_rsp - 0x5F - 0x41) * 4 + 0x10))) + (3));
    result = (uint32_t)((result) & (0xFFFFFFFCULL));
    result = (uint32_t)((result) + (20));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    if (0 != 0) goto loc_00662857;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + local_rsi + local_rsi * 2 * 8 + 0x8))) + (3));
    result = (uint32_t)((result) & (0xFFFFFFFCULL));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    goto loc_00662857;
loc_00662819:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (1)) != 0) goto loc_00662857;
    result = (uint32_t)(*(uint32_t *)(result));
    local_r13 = 1;
    if (1 == 0) {
        result = *(uint32_t *)(local_rdi + local_rsi + local_rsi * 2 * 8 + 0x8);
        local_r13 = 1;
        result = (uint32_t)((result) + (3));
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x49) + 0x14))) == 0) goto loc_0066286C;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x49) + 0x10)) + *(uint64_t *)(arg1) * 1 + 0x10)) == 0) goto loc_00662857;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x49) + 0x10));
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x59)) != 0) {
        result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x49) + 0x14)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x49) + 0x14)) * 4;
        local_r14 = local_r14 + result * 4;
        local_r14 = (uint32_t)((local_r14) + (20));
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D))) + 1);
    goto loc_0066277E;
loc_00662861:
loc_00662865:
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_00662744;
loc_0066286C:
    goto loc_00662CCA;
loc_00662876:
    goto loc_00662CCA;
loc_00662880:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)) * 2) << (3));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)) * 8) + ((uint32_t)(local_r13)));
    result = (uint32_t)((result) + ((uint32_t)(local_r14)));
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)(result);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x68635341ULL), a4);
    if (result != 0) goto loc_006628C1;
    goto loc_00662CCA;
loc_006628C1:
    result = memcpy(result, *(uint64_t *)(arg1), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8)), a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x14))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8)));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8 + local_r13 * 1) + (result);
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)(result + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8 + local_r13 * 1 * 1);
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(result + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8 + local_r13 * 1 * 1);
    result = memcpy(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8)) + *(uint64_t *)(arg1) * 1, (uint32_t)((uint32_t)(result)), a4);
    Arg2 = 0;
    Arg1 = ((uint32_t)((uint32_t)(result + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8 + local_r13 * 1 * 1))) + (result);
    result = memset(Arg1, Arg2, (uint32_t)((uint32_t)(local_r14)), a4);
    local_rbx = (uint32_t)((result + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) * 2 * 8 + local_r13 * 1 * 1) + ((uint32_t)(local_r14)));
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x14))) + (*(uint64_t *)(arg1));
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) + (result);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC))) << (3));
    result = memcpy(Arg1, Arg2, Arg3, a4);
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)));
    *(uint32_t *)(result + 0x14) = (uint32_t)(local_rbx);
    if ((uint32_t)(local_r13) == 0) goto loc_006629BD;
    local_r11 = 0;
    if ((*(uint32_t *)(result + 0xC)) <= 0) goto loc_006629BD;
loc_0066294A:
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x10))) + (result);
    result = (uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x4));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x4))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x4))) + ((uint32_t)(local_r13)));
        *(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x4) = (uint32_t)(result);
    }
    result = (uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x10));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x10))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x10))) + ((uint32_t)(local_r13)));
        *(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x10) = (uint32_t)(result);
    }
    Arg3 = 0;
    if ((*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x14)) <= 0) goto loc_006629B4;
loc_0066297C:
    local_r10 = ((uint32_t)(*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x10))) + (result);
    result = (uint32_t)(*(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0x4));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0x4))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0x4))) + ((uint32_t)(local_r13)));
        *(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0x4) = (uint32_t)(result);
    }
    result = (uint32_t)(*(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0xC));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0xC))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0xC))) + ((uint32_t)(local_r13)));
        *(uint32_t *)(local_r10 + arg3 + arg3 * 4 * 4 + 0xC) = (uint32_t)(result);
    }
    Arg3 = (uint32_t)((Arg3) + 1);
    if (((uint32_t)(Arg3)) < (*(uint32_t *)(Arg2 + local_r11 + local_r11 * 2 * 8 + 0x14))) goto loc_0066297C;
loc_006629B4:
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) < (*(uint32_t *)(result + 0xC))) goto loc_0066294A;
loc_006629BD:
    result = ApiSetValidateSchemaFormat(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), Arg3, Arg3 + Arg3 * 4);
    if (sign_flag) goto loc_00662CC0;
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = 0;
    local_rdi = 0;
loc_006629D9:
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = 0;
    if (0 >= (*(uint32_t *)(arg3 + 0xC))) goto loc_00662CDC;
    a4 = ((uint32_t)(*(uint32_t *)(arg3 + 0x10))) + (Arg3);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = local_rdi + local_rdi * 2;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = a4;
    local_rbx = ((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x4))) + (Arg3);
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)));
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = local_rbx;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8)))) & (4)) == 0) goto loc_00662A87;
    if (0 >= (*(uint32_t *)(local_rsp - 0x5F - 0x61))) goto loc_00662CBB;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x10))) + (result);
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = (uint32_t)(Arg1);
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)) + 1);
    result = 0;
    *(uint64_t *)(Arg2 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8) = v_xmm0;
    *(uint64_t *)(Arg2 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x10) = 0;
    *(uint32_t *)(Arg2 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8)));
    *(uint32_t *)(Arg2 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    *(uint32_t *)(Arg2 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)));
    *(uint32_t *)(Arg2 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)));
    result = AsiAddDataToSchema(result, local_rsp - 95 - 105, local_rbx, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)))));
    if (sign_flag) goto loc_00662CC0;
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    goto loc_00662CB1;
loc_00662A87:
    local_r13 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = 0;
    result = 0;
loc_00662A90:
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = 0;
    if (0 >= (*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)))) + local_rbx * 8 + 0x14))) goto loc_00662CAE;
    Arg2 = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)))) + local_rbx * 8 + 0x10))) + (Arg3);
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = result + result * 4;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = Arg2;
    local_r13 = ((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0xC))) + (Arg3);
loc_00662AC2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x10)))) <= 1) goto loc_00662AD4;
    result = ((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x10)) + local_r13 * 1) - (2);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x10))) + (-2));
    if ((*(uint16_t *)(result)) != 45) goto loc_00662AC2;
loc_00662AD4:
    Arg3 = (uint16_t)(((uint16_t)(local_rbx)) >> (1));
    if (condition_is_equal) goto loc_00662CD5;
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result + result * 4 * 4 + 0x4)));
    result = ApiSetpSearchForApiSet(result, local_r13, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + local_rdi + local_rdi * 2 * 8 + 0x8)))));
    if (result != 0) goto loc_00662BAE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)))) >= (*(uint32_t *)(local_rsp - 0x5F - 0x61))) goto loc_00662CBB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D))) + 1);
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = (uint32_t)(result);
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x10))) + (result);
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)) + 1);
    *(uint64_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8) = v_xmm0;
    result = 0;
    *(uint64_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x10) = 0;
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x31) + *(uint64_t *)(local_rsp - 0x5F - 0x39) * 4 + 0x10)));
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0xC) = (uint32_t)(local_rbx);
    result = AsiAddDataToSchema(0, local_rsp - 95 - 105, local_r13, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x31) + *(uint64_t *)(local_rsp - 0x5F - 0x39) * 4 + 0x10)));
    if (sign_flag) goto loc_00662CC0;
    result = 0;
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x14) = 1;
    *(uint32_t *)(local_rsp - 0x5F + 0x17) = 0;
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    result = AsiAddDataToSchema(0, local_rsp - 95 - 105, local_rsp - 95 + 7, 20);
    if (sign_flag) goto loc_00662CC0;
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    goto loc_00662BB1;
loc_00662BAE:
loc_00662BB1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8)))) & (1)) != 0) goto loc_00662C9C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))) != 0) goto loc_00662BEE;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    result = AsiAddDataToSchema(result, local_rsp - 95 - 105, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    if (sign_flag) goto loc_00662CC0;
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
loc_00662BEE:
    if ((*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x14)) == 0) goto loc_00662CCE;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x10))) + (result);
    if ((*(uint32_t *)(arg1 + 0x10)) == 0) goto loc_00662C83;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x41)) == 0) goto loc_00662C83;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)))));
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x14)) + (uint32_t)(*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x14)) * 4) << (2));
    result = AsiAddDataToSchema(result, local_rsp - 95 - 105, Arg1, a4);
    if (sign_flag) goto loc_00662CC0;
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    *(uint32_t *)(local_rsp - 0x5F - 0x5) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)))));
    result = AsiAddDataToSchema(result, local_rsp - 95 - 105, local_rsp - 95 - 17, 20);
    if (sign_flag) goto loc_00662CC0;
    result = AsiSortValueList(result, Arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8, local_rsp - 95 - 17, 20);
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    goto loc_00662C9C;
loc_00662C83:
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)))));
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    *(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(result + 0xC)) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 2 * 8 + 0x14) = 1;
loc_00662C9C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) + 1);
    goto loc_00662A90;
loc_00662CAE:
loc_00662CB1:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59))) + 1);
    goto loc_006629D9;
loc_00662CBB:
loc_00662CC0:
loc_00662CC3:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(local_rsp - 0x5F - 0x21), *(uint64_t *)(local_rsp - 0x5F - 0x19));
loc_00662CCA:
    goto loc_00662D25;
loc_00662CCE:
    goto loc_00662CC0;
loc_00662CD5:
    goto loc_00662CC0;
loc_00662CDC:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x61)) <= 0) goto loc_00662CF5;
    result = AsiPopulateHashes(result, Arg2, *(uint64_t *)(local_rsp - 0x5F - 0x21), *(uint64_t *)(local_rsp - 0x5F - 0x19));
    if ((uint32_t)(result) != 0) goto loc_00662CF5;
    goto loc_00662CC0;
loc_00662CF5:
    result = ApiSetValidateSchemaFormat(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), *(uint64_t *)(local_rsp - 0x5F - 0x21), *(uint64_t *)(local_rsp - 0x5F - 0x19));
    if (sign_flag) goto loc_00662CC0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67)) = result;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)));
    goto loc_00662CC3;
loc_00662D19:
    goto loc_00662D25;
loc_00662D20:
    result = ApiSetComposeSchema_V7(*(uint64_t *)(arg1), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), *(uint64_t *)(local_rsp - 0x5F - 0x21), *(uint64_t *)(local_rsp - 0x5F - 0x19));
loc_00662D25:
    local_rsp = (local_rsp) + (176);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00662684&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
