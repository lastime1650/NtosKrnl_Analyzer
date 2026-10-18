# ST_STORE&lt;SM_TRAITS&gt;::StStart

- RVA: `0x003B1BBC`–`0x003B2005` (길이 `1,097` bytes)
- VA: `0x00000001403B1BBC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008C358`
- 디코드: `296`개 명령, `1,097/1,097` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003B1D52` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003B1D6C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003B1DA8` → [RtlGetCompressionWorkSpaceSize](RtlGetCompressionWorkSpaceSize_function_003B2560.md) (function, `0x003B2560`)
- `0x003B1E07` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003B1E63` → [ST_STORE<SM_TRAITS>::StDmStart](ST_STORE_SM_TRAITS_StDmStart_function_003B25C8.md) (function, `0x003B25C8`)
- `0x003B1EA1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003B1F2E` → [StEtaHelper::StartHelper](../4A/StEtaHelper_StartHelper_function_004A0194.md) (function, `0x004A0194`)
- `0x003B1F4B` → [SmCrEncStart](../../page/7A/SmCrEncStart_function_007AA208.md) (function, `0x007AA208`)
- `0x003B1F7F` → [RtlNumberOfSetBits](../43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x003B1FF3` → [ST_STORE<SM_TRAITS>::StDmStart](ST_STORE_SM_TRAITS_StDmStart_function_003B25C8.md) (function, `0x003B25C8`)

### Direct callers
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStStart](SMKM_STORE_SM_TRAITS_SmStStart_function_003B14DC.md) at `0x003B18F4`

### Static image references
- `0x003B1D90` → RVA `0x00011C18` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x003B1D52` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x003B1E07` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x003B1EA1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x003B1F4B` → [SmCrEncStart](../../page/7A/SmCrEncStart_function_007AA208.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003B1D76` → [sub_006E708E](../6E/Unknown_function_006E708E.md) (`tail-transfer`)
  - `0x003B1FC0` → [sub_006E708E + 0x5E](../6E/Unknown_function_006E708E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003B1BBC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003B1BC1  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003B1BC6  57                              push rdi
003B1BC7  41 54                           push r12
003B1BC9  41 55                           push r13
003B1BCB  41 56                           push r14
003B1BCD  41 57                           push r15
003B1BCF  48 83 EC 30                     sub rsp, 0x30
003B1BD3  48 8B F9                        mov rdi, rcx
003B1BD6  48 8B DA                        mov rbx, rdx
003B1BD9  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
003B1BDC  85 C9                           test ecx, ecx
003B1BDE  0F 84 8A 03 00 00               je 0x1403b1f6e
003B1BE4  8D 41 FF                        lea eax, [rcx - 1]
003B1BE7  85 C1                           test ecx, eax
003B1BE9  0F 85 7F 03 00 00               jne 0x1403b1f6e
003B1BEF  8D 81 00 F0 FF FF               lea eax, [rcx - 0x1000]
003B1BF5  3D 00 F0 01 00                  cmp eax, 0x1f000
003B1BFA  0F 87 6E 03 00 00               ja 0x1403b1f6e
003B1C00  44 8B 4A 0C                     mov r9d, dword ptr [rdx + 0xc]
003B1C04  41 8D 41 FF                     lea eax, [r9 - 1]
003B1C08  3D FF FF 03 00                  cmp eax, 0x3ffff
003B1C0D  77 3A                           ja 0x1403b1c49
003B1C0F  8B 12                           mov edx, dword ptr [rdx]
003B1C11  0F BA E2 08                     bt edx, 8
003B1C15  72 32                           jb 0x1403b1c49
003B1C17  0F B6 C2                        movzx eax, dl
003B1C1A  41 BF 01 00 00 00               mov r15d, 1
003B1C20  41 3B C7                        cmp eax, r15d
003B1C23  0F 84 A5 02 00 00               je 0x1403b1ece
003B1C29  84 D2                           test dl, dl
003B1C2B  0F 84 4E 02 00 00               je 0x1403b1e7f
003B1C31  80 FA 02                        cmp dl, 2
003B1C34  73 13                           jae 0x1403b1c49
003B1C36  80 7B 03 00                     cmp byte ptr [rbx + 3], 0
003B1C3A  75 0D                           jne 0x1403b1c49
003B1C3C  B9 00 06 00 00                  mov ecx, 0x600
003B1C41  8B C2                           mov eax, edx
003B1C43  23 C1                           and eax, ecx
003B1C45  3B C1                           cmp eax, ecx
003B1C47  75 1E                           jne 0x1403b1c67
003B1C49  B8 0D 00 00 C0                  mov eax, 0xc000000d
003B1C4E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
003B1C53  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
003B1C58  48 83 C4 30                     add rsp, 0x30
003B1C5C  41 5F                           pop r15
003B1C5E  41 5E                           pop r14
003B1C60  41 5D                           pop r13
003B1C62  41 5C                           pop r12
003B1C64  5F                              pop rdi
003B1C65  C3                              ret
003B1C66  CC                              int3
003B1C67  33 C9                           xor ecx, ecx
003B1C69  39 4B 28                        cmp dword ptr [rbx + 0x28], ecx
003B1C6C  0F 94 C1                        sete cl
003B1C6F  33 C0                           xor eax, eax
003B1C71  48 39 43 20                     cmp qword ptr [rbx + 0x20], rax
003B1C75  0F 94 C0                        sete al
003B1C78  3B C1                           cmp eax, ecx
003B1C7A  75 CD                           jne 0x1403b1c49
003B1C7C  84 D2                           test dl, dl
003B1C7E  0F 95 C1                        setne cl
003B1C81  0F BA E2 14                     bt edx, 0x14
003B1C85  0F 92 C0                        setb al
003B1C88  84 C1                           test cl, al
003B1C8A  75 BD                           jne 0x1403b1c49
003B1C8C  0F BA E2 15                     bt edx, 0x15
003B1C90  0F 92 C0                        setb al
003B1C93  84 C1                           test cl, al
003B1C95  75 B2                           jne 0x1403b1c49
003B1C97  8B C2                           mov eax, edx
003B1C99  25 00 00 30 00                  and eax, 0x300000
003B1C9E  3D 00 00 10 00                  cmp eax, 0x100000
003B1CA3  74 A4                           je 0x1403b1c49
003B1CA5  8B C2                           mov eax, edx
003B1CA7  25 00 00 A0 00                  and eax, 0xa00000
003B1CAC  3D 00 00 80 00                  cmp eax, 0x800000
003B1CB1  74 96                           je 0x1403b1c49
003B1CB3  81 E2 00 00 42 00               and edx, 0x420000
003B1CB9  81 FA 00 00 40 00               cmp edx, 0x400000
003B1CBF  74 88                           je 0x1403b1c49
003B1CC1  44 8B 43 08                     mov r8d, dword ptr [rbx + 8]
003B1CC5  33 D2                           xor edx, edx
003B1CC7  41 83 F8 10                     cmp r8d, 0x10
003B1CCB  76 11                           jbe 0x1403b1cde
003B1CCD  41 03 D7                        add edx, r15d
003B1CD0  B8 10 00 00 00                  mov eax, 0x10
003B1CD5  8B CA                           mov ecx, edx
003B1CD7  D3 E0                           shl eax, cl
003B1CD9  41 3B C0                        cmp eax, r8d
003B1CDC  72 EF                           jb 0x1403b1ccd
003B1CDE  8B CA                           mov ecx, edx
003B1CE0  89 57 24                        mov dword ptr [rdi + 0x24], edx
003B1CE3  41 8B C7                        mov eax, r15d
003B1CE6  D3 E0                           shl eax, cl
003B1CE8  89 47 28                        mov dword ptr [rdi + 0x28], eax
003B1CEB  8D 48 FF                        lea ecx, [rax - 1]
003B1CEE  89 4F 20                        mov dword ptr [rdi + 0x20], ecx
003B1CF1  81 7B 08 00 00 02 00            cmp dword ptr [rbx + 8], 0x20000
003B1CF8  75 03                           jne 0x1403b1cfd
003B1CFA  89 4F 28                        mov dword ptr [rdi + 0x28], ecx
003B1CFD  80 3B 00                        cmp byte ptr [rbx], 0
003B1D00  0F 85 FD 01 00 00               jne 0x1403b1f03
003B1D06  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
003B1D09  B9 20 00 00 00                  mov ecx, 0x20
003B1D0E  05 0F 10 00 00                  add eax, 0x100f
003B1D13  2A CA                           sub cl, dl
003B1D15  C1 E8 04                        shr eax, 4
003B1D18  89 47 2C                        mov dword ptr [rdi + 0x2c], eax
003B1D1B  41 8B C7                        mov eax, r15d
003B1D1E  D3 E0                           shl eax, cl
003B1D20  39 43 0C                        cmp dword ptr [rbx + 0xc], eax
003B1D23  0F 87 EF 01 00 00               ja 0x1403b1f18
003B1D29  0F 28 03                        movaps xmm0, xmmword ptr [rbx]
003B1D2C  41 BC 73 6D 53 74               mov r12d, 0x74536d73
003B1D32  0F 11 07                        movups xmmword ptr [rdi], xmm0
003B1D35  41 BD 40 00 00 00               mov r13d, 0x40
003B1D3B  45 8B C4                        mov r8d, r12d
003B1D3E  0F 28 4B 10                     movaps xmm1, xmmword ptr [rbx + 0x10]
003B1D42  41 8B CD                        mov ecx, r13d
003B1D45  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
003B1D49  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
003B1D4C  03 C0                           add eax, eax
003B1D4E  8B D0                           mov edx, eax
003B1D50  8B F0                           mov esi, eax
003B1D52  E8 99 03 7D 00                  call 0x140b820f0
003B1D57  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
003B1D5B  48 85 C0                        test rax, rax
003B1D5E  0F 84 52 01 00 00               je 0x1403b1eb6
003B1D64  44 8B C6                        mov r8d, esi
003B1D67  33 D2                           xor edx, edx
003B1D69  48 8B C8                        mov rcx, rax
003B1D6C  E8 CF 4E 31 00                  call 0x1406c6c40
003B1D71  8B 03                           mov eax, dword ptr [rbx]
003B1D73  41 3A C7                        cmp al, r15b
003B1D76  0F 84 12 53 33 00               je 0x1406e708e
003B1D7C  48 63 43 40                     movsxd rax, dword ptr [rbx + 0x40]
003B1D80  48 8D B7 B8 12 00 00            lea rsi, [rdi + 0x12b8]
003B1D87  48 8B C8                        mov rcx, rax
003B1D8A  89 87 C0 12 00 00               mov dword ptr [rdi + 0x12c0], eax
003B1D90  48 8D 05 81 FE C5 FF            lea rax, [rip - 0x3a017f]
003B1D97  4C 8B C6                        mov r8, rsi
003B1D9A  4C 8D B7 BC 12 00 00            lea r14, [rdi + 0x12bc]
003B1DA1  49 8B D6                        mov rdx, r14
003B1DA4  0F B7 0C 48                     movzx ecx, word ptr [rax + rcx*2]
003B1DA8  E8 B3 07 00 00                  call 0x1403b2560
003B1DAD  85 C0                           test eax, eax
003B1DAF  0F 88 99 FE FF FF               js 0x1403b1c4e
003B1DB5  41 8B 0E                        mov ecx, dword ptr [r14]
003B1DB8  8B 06                           mov eax, dword ptr [rsi]
003B1DBA  3B C8                           cmp ecx, eax
003B1DBC  0F 46 C8                        cmovbe ecx, eax
003B1DBF  85 C9                           test ecx, ecx
003B1DC1  0F 85 D2 00 00 00               jne 0x1403b1e99
003B1DC7  48 8B 73 30                     mov rsi, qword ptr [rbx + 0x30]
003B1DCB  48 85 F6                        test rsi, rsi
003B1DCE  0F 84 4E 01 00 00               je 0x1403b1f22
003B1DD4  48 89 B7 70 12 00 00            mov qword ptr [rdi + 0x1270], rsi
003B1DDB  44 8B 43 28                     mov r8d, dword ptr [rbx + 0x28]
003B1DDF  8B 03                           mov eax, dword ptr [rbx]
003B1DE1  45 85 C0                        test r8d, r8d
003B1DE4  0F 85 D6 00 00 00               jne 0x1403b1ec0
003B1DEA  8B 03                           mov eax, dword ptr [rbx]
003B1DEC  45 8B C4                        mov r8d, r12d
003B1DEF  25 00 80 00 00                  and eax, 0x8000
003B1DF4  49 8B CD                        mov rcx, r13
003B1DF7  F7 D8                           neg eax
003B1DF9  B8 00 10 00 00                  mov eax, 0x1000
003B1DFE  48 1B D2                        sbb rdx, rdx
003B1E01  48 23 D0                        and rdx, rax
003B1E04  48 03 D0                        add rdx, rax
003B1E07  E8 E4 02 7D 00                  call 0x140b820f0
003B1E0C  48 89 87 70 13 00 00            mov qword ptr [rdi + 0x1370], rax
003B1E13  48 85 C0                        test rax, rax
003B1E16  0F 84 9A 00 00 00               je 0x1403b1eb6
003B1E1C  8B 03                           mov eax, dword ptr [rbx]
003B1E1E  41 3A C7                        cmp al, r15b
003B1E21  0F 84 51 01 00 00               je 0x1403b1f78
003B1E27  44 8B 43 0C                     mov r8d, dword ptr [rbx + 0xc]
003B1E2B  33 F6                           xor esi, esi
003B1E2D  8B 13                           mov edx, dword ptr [rbx]
003B1E2F  8B CA                           mov ecx, edx
003B1E31  C1 E9 08                        shr ecx, 8
003B1E34  41 23 CF                        and ecx, r15d
003B1E37  85 F6                           test esi, esi
003B1E39  0F 85 56 01 00 00               jne 0x1403b1f95
003B1E3F  33 C0                           xor eax, eax
003B1E41  0B C1                           or eax, ecx
003B1E43  84 D2                           test dl, dl
003B1E45  0F 84 5E 01 00 00               je 0x1403b1fa9
003B1E4B  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
003B1E4F  44 2B C6                        sub r8d, esi
003B1E52  48 8D 57 50                     lea rdx, [rdi + 0x50]
003B1E56  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
003B1E5B  48 8B CF                        mov rcx, rdi
003B1E5E  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
003B1E63  E8 60 07 00 00                  call 0x1403b25c8
003B1E68  85 C0                           test eax, eax
003B1E6A  0F 88 DE FD FF FF               js 0x1403b1c4e
003B1E70  85 F6                           test esi, esi
003B1E72  0F 85 5A 01 00 00               jne 0x1403b1fd2
003B1E78  33 C0                           xor eax, eax
003B1E7A  E9 CF FD FF FF                  jmp 0x1403b1c4e
003B1E7F  83 7B 10 00                     cmp dword ptr [rbx + 0x10], 0
003B1E83  0F 85 C0 FD FF FF               jne 0x1403b1c49
003B1E89  48 83 7B 38 00                  cmp qword ptr [rbx + 0x38], 0
003B1E8E  0F 84 A2 FD FF FF               je 0x1403b1c36
003B1E94  E9 B0 FD FF FF                  jmp 0x1403b1c49
003B1E99  8B D1                           mov edx, ecx
003B1E9B  45 8B C4                        mov r8d, r12d
003B1E9E  49 8B CD                        mov rcx, r13
003B1EA1  E8 4A 02 7D 00                  call 0x140b820f0
003B1EA6  48 89 87 B0 12 00 00            mov qword ptr [rdi + 0x12b0], rax
003B1EAD  48 85 C0                        test rax, rax
003B1EB0  0F 85 11 FF FF FF               jne 0x1403b1dc7
003B1EB6  B8 9A 00 00 C0                  mov eax, 0xc000009a
003B1EBB  E9 8E FD FF FF                  jmp 0x1403b1c4e
003B1EC0  84 C0                           test al, al
003B1EC2  75 7C                           jne 0x1403b1f40
003B1EC4  B8 F6 02 00 C0                  mov eax, 0xc00002f6
003B1EC9  E9 80 FD FF FF                  jmp 0x1403b1c4e
003B1ECE  44 8B 43 10                     mov r8d, dword ptr [rbx + 0x10]
003B1ED2  45 85 C0                        test r8d, r8d
003B1ED5  0F 84 6E FD FF FF               je 0x1403b1c49
003B1EDB  41 8D 40 FF                     lea eax, [r8 - 1]
003B1EDF  41 85 C0                        test r8d, eax
003B1EE2  0F 85 61 FD FF FF               jne 0x1403b1c49
003B1EE8  44 3B C1                        cmp r8d, ecx
003B1EEB  0F 87 58 FD FF FF               ja 0x1403b1c49
003B1EF1  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
003B1EF5  48 85 C0                        test rax, rax
003B1EF8  0F 84 4B FD FF FF               je 0x1403b1c49
003B1EFE  44 39 08                        cmp dword ptr [rax], r9d
003B1F01  EB 8B                           jmp 0x1403b1e8e
003B1F03  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
003B1F06  F7 D8                           neg eax
003B1F08  1B C9                           sbb ecx, ecx
003B1F0A  83 E1 0C                        and ecx, 0xc
003B1F0D  83 C1 04                        add ecx, 4
003B1F10  89 4F 30                        mov dword ptr [rdi + 0x30], ecx
003B1F13  E9 EE FD FF FF                  jmp 0x1403b1d06
003B1F18  B8 06 02 00 C0                  mov eax, 0xc0000206
003B1F1D  E9 2C FD FF FF                  jmp 0x1403b1c4e
003B1F22  48 8D B7 78 12 00 00            lea rsi, [rdi + 0x1278]
003B1F29  33 D2                           xor edx, edx
003B1F2B  48 8B CE                        mov rcx, rsi
003B1F2E  E8 61 E2 0E 00                  call 0x1404a0194
003B1F33  85 C0                           test eax, eax
003B1F35  0F 88 13 FD FF FF               js 0x1403b1c4e
003B1F3B  E9 94 FE FF FF                  jmp 0x1403b1dd4
003B1F40  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
003B1F44  48 8D 8F E0 12 00 00            lea rcx, [rdi + 0x12e0]
003B1F4B  E8 B8 82 3F 00                  call 0x1407aa208
003B1F50  85 C0                           test eax, eax
003B1F52  0F 88 F6 FC FF FF               js 0x1403b1c4e
003B1F58  8B 8F E8 12 00 00               mov ecx, dword ptr [rdi + 0x12e8]
003B1F5E  8D 41 0F                        lea eax, [rcx + 0xf]
003B1F61  F7 D9                           neg ecx
003B1F63  23 C1                           and eax, ecx
003B1F65  83 F8 10                        cmp eax, 0x10
003B1F68  0F 84 7C FE FF FF               je 0x1403b1dea
003B1F6E  B8 73 01 00 C0                  mov eax, 0xc0000173
003B1F73  E9 D6 FC FF FF                  jmp 0x1403b1c4e
003B1F78  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
003B1F7C  41 8B F7                        mov esi, r15d
003B1F7F  E8 EC 1F 08 00                  call 0x140433f70
003B1F84  44 8B C0                        mov r8d, eax
003B1F87  41 3B C7                        cmp eax, r15d
003B1F8A  0F 87 9D FE FF FF               ja 0x1403b1e2d
003B1F90  E9 B4 FC FF FF                  jmp 0x1403b1c49
003B1F95  0F BA E2 0E                     bt edx, 0xe
003B1F99  0F 82 A0 FE FF FF               jb 0x1403b1e3f
003B1F9F  B8 08 00 00 00                  mov eax, 8
003B1FA4  E9 98 FE FF FF                  jmp 0x1403b1e41
003B1FA9  8B C8                           mov ecx, eax
003B1FAB  41 0B CD                        or ecx, r13d
003B1FAE  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
003B1FB2  0F BA E2 11                     bt edx, 0x11
003B1FB6  0F 83 93 FE FF FF               jae 0x1403b1e4f
003B1FBC  0F BA E2 16                     bt edx, 0x16
003B1FC0  0F 83 26 51 33 00               jae 0x1406e70ec
003B1FC6  83 E1 9F                        and ecx, 0xffffff9f
003B1FC9  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
003B1FCD  E9 7D FE FF FF                  jmp 0x1403b1e4f
003B1FD2  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
003B1FD6  48 8D 97 60 09 00 00            lea rdx, [rdi + 0x960]
003B1FDD  83 E0 F6                        and eax, 0xfffffff6
003B1FE0  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
003B1FE4  83 C8 16                        or eax, 0x16
003B1FE7  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
003B1FEC  48 8B CF                        mov rcx, rdi
003B1FEF  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
003B1FF3  E8 D0 05 00 00                  call 0x1403b25c8
003B1FF8  85 C0                           test eax, eax
003B1FFA  0F 88 4E FC FF FF               js 0x1403b1c4e
003B2000  E9 73 FE FF FF                  jmp 0x1403b1e78
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StStart(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p28;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))) == 0) goto loc_003B1F6E;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)) - 1))) != 0) goto loc_003B1F6E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)) - 4096)) > 0x1F000ULL) goto loc_003B1F6E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)) - 1)) > 0x3FFFFULL) goto loc_003B1C49;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)) - 1)) < 0x3FFFFULL) goto loc_003B1C49;
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(a2))))) == 1) goto loc_003B1ECE;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_003B1E7F;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) >= 2) goto loc_003B1C49;
loc_003B1C36:
    if ((*(unsigned __int8 *)(a2 + 3)) != 0) goto loc_003B1C49;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) & ((unsigned int)((unsigned int)(0x600ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x600ULL)))) goto loc_003B1C67;
loc_003B1C49:
loc_003B1C4E:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(0xC000000DULL);
loc_003B1C67:
    a1 = 0;
    a1 = ((*(unsigned int *)(v_stack_p8 + 40)) == 0) ? 1 : 0;
    result = 0;
    result = ((*(unsigned __int64 *)(v_stack_p8 + 32)) == 0) ? 1 : 0;
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_003B1C49;
    a1 = ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2))) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(result))) != 0) goto loc_003B1C49;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(result))) != 0) goto loc_003B1C49;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) & (0x300000ULL));
    if (((unsigned int)(result)) == 0x100000ULL) goto loc_003B1C49;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) & (0xA00000ULL));
    if (((unsigned int)(result)) == 0x800000ULL) goto loc_003B1C49;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (0x420000ULL));
    if (((unsigned int)(a2)) == 0x400000ULL) goto loc_003B1C49;
    a2 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)))) <= 16) goto loc_003B1CDE;
loc_003B1CCD:
    a2 = (unsigned int)((a2) + (1));
    result = (unsigned int)((16) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8))))) goto loc_003B1CCD;
loc_003B1CDE:
    *(unsigned int *)(a1 + 36) = (unsigned int)(a2);
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    *(unsigned int *)(a1 + 40) = (unsigned int)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)(result - 1);
    if ((*(unsigned int *)(v_stack_p8 + 8)) == 0x20000ULL) {
        *(unsigned int *)(a1 + 40) = (unsigned int)(result - 1);
    }
    if ((*(unsigned __int8 *)(v_stack_p8)) != 0) goto loc_003B1F03;
loc_003B1D06:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) + (0x100FULL));
    a1 = (unsigned __int8)((32) - ((unsigned __int8)(a2)));
    result = (unsigned int)((result) >> (4));
    *(unsigned int *)(a1 + 44) = (unsigned int)(result);
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    if ((*(unsigned int *)(v_stack_p8 + 12)) > ((unsigned int)(result))) goto loc_003B1F18;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 12))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 12)))));
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x74536D73ULL))), (unsigned int)(*(unsigned int *)(a2 + 12)));
    *(unsigned __int64 *)(a1 + 56) = result;
    if (result == 0) goto loc_003B1EB6;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(*(unsigned int *)(a2 + 12)));
    *(unsigned int *)(a1 + 4800) = (unsigned int)((int)(*(unsigned int *)(v_stack_p8 + 64)));
    result = RtlGetCompressionWorkSpaceSize(*(unsigned __int16 *)(v_rip - 3801471 + (int)(*(unsigned int *)(v_stack_p8 + 64)) * 2), a1 + 4796, a1 + 4792, (unsigned int)(*(unsigned int *)(a2 + 12)));
    if (sign_flag) goto loc_003B1C4E;
    a1 = (unsigned int)(*(unsigned int *)(a1 + 4796));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4796)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4792))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4792))); }
    if ((unsigned int)(a1) != 0) goto loc_003B1E99;
loc_003B1DC7:
    if (*(unsigned __int64 *)(v_stack_p8 + 48) == 0) goto loc_003B1F22;
loc_003B1DD4:
    *(unsigned __int64 *)(a1 + 4720) = *(unsigned __int64 *)(v_stack_p8 + 48);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 40))) != 0) goto loc_003B1EC0;
loc_003B1DEA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8))) & (0x8000ULL));
    result = (unsigned int)(-(result));
    a2 = (a1 + 4796) & ((unsigned int)(0x1000ULL));
    a2 = (a2) + ((unsigned int)(0x1000ULL));
    result = ExAllocatePool2(64, a2, (unsigned int)((unsigned int)((unsigned int)(0x74536D73ULL))), (unsigned int)(*(unsigned int *)(a2 + 12)));
    *(unsigned __int64 *)(a1 + 4976) = result;
    if (result == 0) goto loc_003B1EB6;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) == 1) goto loc_003B1F78;
    v_rsi = 0;
loc_003B1E2D:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8))))) >> (8));
    a1 = (unsigned int)((a1) & (1));
    if (0 != 0) goto loc_003B1F95;
loc_003B1E3F:
    result = 0;
loc_003B1E41:
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8))) == 0) goto loc_003B1FA9;
    v_stack_p68 = (unsigned int)(result);
loc_003B1E4F:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 12))) - (0));
    v_stack_p28 = (unsigned int)(a3);
    result = ST_STORE_SM_TRAITS___StDmStart(a1, a1 + 80, v_stack_p68, (unsigned int)(*(unsigned int *)(a2 + 12)));
    if (sign_flag) goto loc_003B1C4E;
    if (0 != 0) goto loc_003B1FD2;
loc_003B1E78:
    result = 0;
    goto loc_003B1C4E;
loc_003B1E7F:
    if ((*(unsigned int *)(v_stack_p8 + 16)) != 0) goto loc_003B1C49;
loc_003B1E8E:
    if ((*(unsigned __int64 *)(v_stack_p8 + 56)) == 0) goto loc_003B1C36;
    goto loc_003B1C49;
loc_003B1E99:
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(a1)), (unsigned int)((unsigned int)((unsigned int)(0x74536D73ULL))), (unsigned int)(*(unsigned int *)(a2 + 12)));
    *(unsigned __int64 *)(a1 + 4784) = result;
    if (result != 0) goto loc_003B1DC7;
loc_003B1EB6:
    goto loc_003B1C4E;
loc_003B1EC0:
    if ((unsigned __int8)((unsigned int)(0xC000009AULL)) != 0) goto loc_003B1F40;
    goto loc_003B1C4E;
loc_003B1ECE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16))) == 0) goto loc_003B1C49;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)) - 1))) != 0) goto loc_003B1C49;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) > 64) goto loc_003B1C49;
    if (*(unsigned __int64 *)(v_stack_p8 + 56) == 0) goto loc_003B1C49;
    goto loc_003B1E8E;
loc_003B1F03:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_p8 + 40))));
    a1 = (unsigned int)((64) & (12));
    a1 = (unsigned int)((a1) + (4));
    *(unsigned int *)(a1 + 48) = (unsigned int)(a1);
    goto loc_003B1D06;
loc_003B1F18:
    goto loc_003B1C4E;
loc_003B1F22:
    a2 = 0;
    result = StEtaHelper__StartHelper(a1 + 4728, a2, (unsigned int)(*(unsigned int *)(v_stack_p8 + 16)), (unsigned int)(*(unsigned int *)(a2 + 12)));
    if (sign_flag) goto loc_003B1C4E;
    goto loc_003B1DD4;
loc_003B1F40:
    result = SmCrEncStart(a1 + 4832, *(unsigned __int64 *)(v_stack_p8 + 32), (unsigned int)(*(unsigned int *)(v_stack_p8 + 16)), (unsigned int)(*(unsigned int *)(a2 + 12)));
    if (sign_flag) goto loc_003B1C4E;
    a1 = (unsigned int)(-((unsigned int)(*(unsigned int *)(a1 + 4840))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4840)) + 15) & ((unsigned int)(a1)));
    if (((unsigned int)(result)) == 16) goto loc_003B1DEA;
loc_003B1F6E:
    goto loc_003B1C4E;
loc_003B1F78:
    result = RtlNumberOfSetBits(*(unsigned __int64 *)(v_stack_p8 + 56), *(unsigned __int64 *)(v_stack_p8 + 32), (unsigned int)(*(unsigned int *)(v_stack_p8 + 16)), (unsigned int)(*(unsigned int *)(a2 + 12)));
    if (((unsigned int)(result)) > 1) goto loc_003B1E2D;
    goto loc_003B1C49;
loc_003B1F95:
    if (((unsigned int)(result)) < 1) goto loc_003B1E3F;
    goto loc_003B1E41;
loc_003B1FA9:
    a1 = (unsigned int)((8) | (64));
    v_stack_p68 = (unsigned int)(a1);
    if (condition_is_above_or_equal) goto loc_003B1E4F;
    a1 = (unsigned int)((a1) & (0xFFFFFF9FULL));
    v_stack_p68 = (unsigned int)(a1);
    goto loc_003B1E4F;
loc_003B1FD2:
    result = (unsigned int)(((unsigned int)(v_stack_p68)) & (0xFFFFFFF6ULL));
    v_stack_p28 = 1;
    result = (unsigned int)((result) | (22));
    v_stack_p68 = (unsigned int)(result);
    result = ST_STORE_SM_TRAITS___StDmStart(a1, a1 + 2400, v_stack_p68, (unsigned int)(*(unsigned int *)(a2 + 12)));
    if (sign_flag) goto loc_003B1C4E;
    goto loc_003B1E78;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StStart(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint32_t v_stack_p28;
    uint32_t v_stack_p68;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))) == 0) goto loc_003B1F6E;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)) - 1))) != 0) goto loc_003B1F6E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)) - 4096)) > 0x1F000ULL) goto loc_003B1F6E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC)) - 1)) > 0x3FFFFULL) goto loc_003B1C49;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC)) - 1)) < 0x3FFFFULL) goto loc_003B1C49;
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(arg2))))) == 1) goto loc_003B1ECE;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(arg2))) == 0) goto loc_003B1E7F;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) >= 2) goto loc_003B1C49;
loc_003B1C36:
    if ((*(uint8_t *)(arg2 + 0x3)) != 0) goto loc_003B1C49;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) & ((uint32_t)((uint32_t)(0x600ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x600ULL)))) goto loc_003B1C67;
loc_003B1C49:
loc_003B1C4E:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(0xC000000DULL);
loc_003B1C67:
    Arg1 = 0;
    Arg1 = ((*(uint32_t *)(v_stack_p8 + 0x28)) == 0) ? 1 : 0;
    result = 0;
    result = ((*(uint64_t *)(v_stack_p8 + 0x20)) == 0) ? 1 : 0;
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_003B1C49;
    Arg1 = ((uint8_t)((uint32_t)(*(uint32_t *)(arg2))) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(result))) != 0) goto loc_003B1C49;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(result))) != 0) goto loc_003B1C49;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) & (0x300000ULL));
    if (((uint32_t)(result)) == 0x100000ULL) goto loc_003B1C49;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) & (0xA00000ULL));
    if (((uint32_t)(result)) == 0x800000ULL) goto loc_003B1C49;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (0x420000ULL));
    if (((uint32_t)(Arg2)) == 0x400000ULL) goto loc_003B1C49;
    Arg2 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)))) <= 16) goto loc_003B1CDE;
loc_003B1CCD:
    Arg2 = (uint32_t)((Arg2) + (1));
    result = (uint32_t)((16) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8))))) goto loc_003B1CCD;
loc_003B1CDE:
    *(uint32_t *)(arg1 + 0x24) = (uint32_t)(Arg2);
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    *(uint32_t *)(arg1 + 0x28) = (uint32_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)(result - 1);
    if ((*(uint32_t *)(v_stack_p8 + 0x8)) == 0x20000ULL) {
        *(uint32_t *)(arg1 + 0x28) = (uint32_t)(result - 1);
    }
    if ((*(uint8_t *)(v_stack_p8)) != 0) goto loc_003B1F03;
loc_003B1D06:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) + (0x100FULL));
    Arg1 = (uint8_t)((32) - ((uint8_t)(Arg2)));
    result = (uint32_t)((result) >> (4));
    *(uint32_t *)(arg1 + 0x2C) = (uint32_t)(result);
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    if ((*(uint32_t *)(v_stack_p8 + 0xC)) > ((uint32_t)(result))) goto loc_003B1F18;
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC))) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC)))));
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x74536D73ULL))), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    *(uint64_t *)(arg1 + 0x38) = result;
    if (result == 0) goto loc_003B1EB6;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    *(uint32_t *)(arg1 + 0x12C0) = (uint32_t)((int32_t)(*(uint32_t *)(v_stack_p8 + 0x40)));
    result = RtlGetCompressionWorkSpaceSize(*(uint16_t *)(v_rip - 0x3A017F + (int32_t)(*(uint32_t *)(v_stack_p8 + 0x40)) * 2), Arg1 + 4796, Arg1 + 4792, (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    if (sign_flag) goto loc_003B1C4E;
    Arg1 = (uint32_t)(*(uint32_t *)(arg1 + 0x12BC));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12BC)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12B8))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12B8))); }
    if ((uint32_t)(Arg1) != 0) goto loc_003B1E99;
loc_003B1DC7:
    if (*(uint64_t *)(v_stack_p8 + 0x30) == 0) goto loc_003B1F22;
loc_003B1DD4:
    *(uint64_t *)(arg1 + 0x1270) = *(uint64_t *)(v_stack_p8 + 0x30);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28))) != 0) goto loc_003B1EC0;
loc_003B1DEA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8))) & (0x8000ULL));
    result = (uint32_t)(-(result));
    Arg2 = (Arg1 + 4796) & ((uint32_t)(0x1000ULL));
    Arg2 = (Arg2) + ((uint32_t)(0x1000ULL));
    result = ExAllocatePool2(64, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x74536D73ULL))), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    *(uint64_t *)(arg1 + 0x1370) = result;
    if (result == 0) goto loc_003B1EB6;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) == 1) goto loc_003B1F78;
    local_rsi = 0;
loc_003B1E2D:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8))))) >> (8));
    Arg1 = (uint32_t)((Arg1) & (1));
    if (0 != 0) goto loc_003B1F95;
loc_003B1E3F:
    result = 0;
loc_003B1E41:
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    if ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8))) == 0) goto loc_003B1FA9;
    v_stack_p68 = (uint32_t)(result);
loc_003B1E4F:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC))) - (0));
    v_stack_p28 = (uint32_t)(a3);
    result = ST_STORE_SM_TRAITS___StDmStart(Arg1, Arg1 + 80, v_stack_p68, (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    if (sign_flag) goto loc_003B1C4E;
    if (0 != 0) goto loc_003B1FD2;
loc_003B1E78:
    result = 0;
    goto loc_003B1C4E;
loc_003B1E7F:
    if ((*(uint32_t *)(v_stack_p8 + 0x10)) != 0) goto loc_003B1C49;
loc_003B1E8E:
    if ((*(uint64_t *)(v_stack_p8 + 0x38)) == 0) goto loc_003B1C36;
    goto loc_003B1C49;
loc_003B1E99:
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)((uint32_t)(0x74536D73ULL))), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    *(uint64_t *)(arg1 + 0x12B0) = result;
    if (result != 0) goto loc_003B1DC7;
loc_003B1EB6:
    goto loc_003B1C4E;
loc_003B1EC0:
    if ((uint8_t)((uint32_t)(0xC000009AULL)) != 0) goto loc_003B1F40;
    goto loc_003B1C4E;
loc_003B1ECE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10))) == 0) goto loc_003B1C49;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)) - 1))) != 0) goto loc_003B1C49;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) > 64) goto loc_003B1C49;
    if (*(uint64_t *)(v_stack_p8 + 0x38) == 0) goto loc_003B1C49;
    goto loc_003B1E8E;
loc_003B1F03:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28))));
    Arg1 = (uint32_t)((64) & (12));
    Arg1 = (uint32_t)((Arg1) + (4));
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)(Arg1);
    goto loc_003B1D06;
loc_003B1F18:
    goto loc_003B1C4E;
loc_003B1F22:
    Arg2 = 0;
    result = StEtaHelper__StartHelper(Arg1 + 4728, Arg2, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    if (sign_flag) goto loc_003B1C4E;
    goto loc_003B1DD4;
loc_003B1F40:
    result = SmCrEncStart(Arg1 + 4832, *(uint64_t *)(v_stack_p8 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    if (sign_flag) goto loc_003B1C4E;
    Arg1 = (uint32_t)(-((uint32_t)(*(uint32_t *)(arg1 + 0x12E8))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x12E8)) + 15) & ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) == 16) goto loc_003B1DEA;
loc_003B1F6E:
    goto loc_003B1C4E;
loc_003B1F78:
    result = RtlNumberOfSetBits(*(uint64_t *)(v_stack_p8 + 0x38), *(uint64_t *)(v_stack_p8 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)), (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    if (((uint32_t)(result)) > 1) goto loc_003B1E2D;
    goto loc_003B1C49;
loc_003B1F95:
    if (((uint32_t)(result)) < 1) goto loc_003B1E3F;
    goto loc_003B1E41;
loc_003B1FA9:
    Arg1 = (uint32_t)((8) | (64));
    v_stack_p68 = (uint32_t)(Arg1);
    if (condition_is_above_or_equal) goto loc_003B1E4F;
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFF9FULL));
    v_stack_p68 = (uint32_t)(Arg1);
    goto loc_003B1E4F;
loc_003B1FD2:
    result = (uint32_t)(((uint32_t)(v_stack_p68)) & (0xFFFFFFF6ULL));
    v_stack_p28 = 1;
    result = (uint32_t)((result) | (22));
    v_stack_p68 = (uint32_t)(result);
    result = ST_STORE_SM_TRAITS___StDmStart(Arg1, Arg1 + 2400, v_stack_p68, (uint32_t)(*(uint32_t *)(arg2 + 0xC)));
    if (sign_flag) goto loc_003B1C4E;
    goto loc_003B1E78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x24` | `32` | `W` |
| `Arg1` | `+ 0x28` | `32` | `W` |
| `Arg1` | `+ 0x2C` | `32` | `W` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x960` | `64` | `R` |
| `Arg1` | `+ 0x1270` | `64` | `W` |
| `Arg1` | `+ 0x1278` | `64` | `R` |
| `Arg1` | `+ 0x12B0` | `64` | `W` |
| `Arg1` | `+ 0x12B8` | `64` | `R` |
| `Arg1` | `+ 0x12BC` | `64` | `R` |
| `Arg1` | `+ 0x12C0` | `32` | `W` |
| `Arg1` | `+ 0x12E0` | `64` | `R` |
| `Arg1` | `+ 0x12E8` | `32` | `R` |
| `Arg1` | `+ 0x1370` | `64` | `W` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x3` | `8` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0xC` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |

추가 오프셋 2개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B1BBC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
