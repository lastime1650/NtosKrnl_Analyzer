# sub_00B38CDE

- RVA: `0x00B38CDE`–`0x00B3901F` (길이 `833` bytes)
- VA: `0x0000000140B38CDE`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC20C`
- 디코드: `250`개 명령, `833/833` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B38E73` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00B38E86` → [PnpFindBestConfiguration](../72/PnpFindBestConfiguration_function_0072B630.md) (function, `0x0072B630`)
- `0x00B38E96` → [IopCommitConfiguration](../AB/IopCommitConfiguration_function_00ABF3D4.md) (function, `0x00ABF3D4`)
- `0x00B38EB7` → [PnpBuildCmResourceLists](../73/PnpBuildCmResourceLists_function_0073E684.md) (function, `0x0073E684`)
- `0x00B38F0F` → [PnpFindBestConfiguration](../72/PnpFindBestConfiguration_function_0072B630.md) (function, `0x0072B630`)
- `0x00B38F25` → [IopCommitConfiguration](../AB/IopCommitConfiguration_function_00ABF3D4.md) (function, `0x00ABF3D4`)
- `0x00B38F3A` → [PnpBuildCmResourceLists](../73/PnpBuildCmResourceLists_function_0073E684.md) (function, `0x0073E684`)
- `0x00B38F62` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B38F75` → [PnpRebalance](../73/PnpRebalance_function_0073F508.md) (function, `0x0073F508`)
- `0x00B38F84` → [PipClearDevNodeFlags](../8F/PipClearDevNodeFlags_function_008F9F54.md) (function, `0x008F9F54`)
- `0x00B39009` → [IopReleaseFilteredBootResources](../72/IopReleaseFilteredBootResources_function_0072EBF8.md) (function, `0x0072EBF8`)
- `0x00B39014` → [PnpFreeResourceRequirementsForAssignTable](../73/PnpFreeResourceRequirementsForAssignTable_function_0073E8B8.md) (function, `0x0073E8B8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B38E69` → RVA `0x0073E880` (`PnpCompareResourceRequestPriority`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B38E73` → [qsort](../../text/50/qsort_function_005009F0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B3901A` → [PnpAllocateResources + 0x95](../A2/PnpAllocateResources_function_00A2ACC4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B38CDE  48 3B C5                        cmp rax, rbp
00B38CE1  73 18                           jae 0x140b38cfb
00B38CE3  44 39 60 38                     cmp dword ptr [rax + 0x38], r12d
00B38CE7  7C 0D                           jl 0x140b38cf6
00B38CE9  4C 39 60 18                     cmp qword ptr [rax + 0x18], r12
00B38CED  75 07                           jne 0x140b38cf6
00B38CEF  BA 01 00 00 00                  mov edx, 1
00B38CF4  EB 0A                           jmp 0x140b38d00
00B38CF6  49 03 C0                        add rax, r8
00B38CF9  EB E3                           jmp 0x140b38cde
00B38CFB  41 8B D4                        mov edx, r12d
00B38CFE  74 38                           je 0x140b38d38
00B38D00  48 3B F5                        cmp rsi, rbp
00B38D03  73 2B                           jae 0x140b38d30
00B38D05  48 8D 4F FF                     lea rcx, [rdi - 1]
00B38D09  48 C1 E9 06                     shr rcx, 6
00B38D0D  48 8D 46 08                     lea rax, [rsi + 8]
00B38D11  48 FF C1                        inc rcx
00B38D14  44 39 60 30                     cmp dword ptr [rax + 0x30], r12d
00B38D18  7C 06                           jl 0x140b38d20
00B38D1A  4C 39 60 10                     cmp qword ptr [rax + 0x10], r12
00B38D1E  74 07                           je 0x140b38d27
00B38D20  83 08 20                        or dword ptr [rax], 0x20
00B38D23  44 89 48 30                     mov dword ptr [rax + 0x30], r9d
00B38D27  49 03 C0                        add rax, r8
00B38D2A  48 83 E9 01                     sub rcx, 1
00B38D2E  75 E4                           jne 0x140b38d14
00B38D30  85 D2                           test edx, edx
00B38D32  0F 85 D6 02 00 00               jne 0x140b3900e
00B38D38  48 8B CE                        mov rcx, rsi
00B38D3B  48 3B CD                        cmp rcx, rbp
00B38D3E  73 33                           jae 0x140b38d73
00B38D40  48 8B 01                        mov rax, qword ptr [rcx]
00B38D43  48 85 C0                        test rax, rax
00B38D46  74 0D                           je 0x140b38d55
00B38D48  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00B38D4F  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00B38D53  EB 03                           jmp 0x140b38d58
00B38D55  49 8B C4                        mov rax, r12
00B38D58  8B 80 8C 01 00 00               mov eax, dword ptr [rax + 0x18c]
00B38D5E  41 84 C0                        test r8b, al
00B38D61  74 0B                           je 0x140b38d6e
00B38D63  4C 39 61 18                     cmp qword ptr [rcx + 0x18], r12
00B38D67  74 05                           je 0x140b38d6e
00B38D69  41 8B FC                        mov edi, r12d
00B38D6C  EB 0C                           jmp 0x140b38d7a
00B38D6E  49 03 C8                        add rcx, r8
00B38D71  EB C8                           jmp 0x140b38d3b
00B38D73  BF 01 00 00 00                  mov edi, 1
00B38D78  74 59                           je 0x140b38dd3
00B38D7A  48 3B F5                        cmp rsi, rbp
00B38D7D  73 54                           jae 0x140b38dd3
00B38D7F  8B 9C 24 80 00 00 00            mov ebx, dword ptr [rsp + 0x80]
00B38D86  48 8D 4E 08                     lea rcx, [rsi + 8]
00B38D8A  48 8B 41 F8                     mov rax, qword ptr [rcx - 8]
00B38D8E  48 85 C0                        test rax, rax
00B38D91  74 0D                           je 0x140b38da0
00B38D93  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00B38D9A  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00B38D9E  EB 03                           jmp 0x140b38da3
00B38DA0  49 8B C4                        mov rax, r12
00B38DA3  8B 80 8C 01 00 00               mov eax, dword ptr [rax + 0x18c]
00B38DA9  41 84 C0                        test r8b, al
00B38DAC  74 06                           je 0x140b38db4
00B38DAE  4C 39 61 10                     cmp qword ptr [rcx + 0x10], r12
00B38DB2  75 11                           jne 0x140b38dc5
00B38DB4  8B 01                           mov eax, dword ptr [rcx]
00B38DB6  A8 20                           test al, 0x20
00B38DB8  75 0B                           jne 0x140b38dc5
00B38DBA  83 C8 20                        or eax, 0x20
00B38DBD  44 89 49 30                     mov dword ptr [rcx + 0x30], r9d
00B38DC1  89 01                           mov dword ptr [rcx], eax
00B38DC3  FF CB                           dec ebx
00B38DC5  49 03 C8                        add rcx, r8
00B38DC8  48 8D 41 F8                     lea rax, [rcx - 8]
00B38DCC  48 3B C5                        cmp rax, rbp
00B38DCF  72 B9                           jb 0x140b38d8a
00B38DD1  EB 07                           jmp 0x140b38dda
00B38DD3  8B 9C 24 80 00 00 00            mov ebx, dword ptr [rsp + 0x80]
00B38DDA  85 DB                           test ebx, ebx
00B38DDC  75 0A                           jne 0x140b38de8
00B38DDE  BB 01 00 00 C0                  mov ebx, 0xc0000001
00B38DE3  E9 26 02 00 00                  jmp 0x140b3900e
00B38DE8  41 3B DE                        cmp ebx, r14d
00B38DEB  74 5F                           je 0x140b38e4c
00B38DED  48 8B CE                        mov rcx, rsi
00B38DF0  48 3B F5                        cmp rsi, rbp
00B38DF3  73 57                           jae 0x140b38e4c
00B38DF5  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00B38DF9  8B 41 08                        mov eax, dword ptr [rcx + 8]
00B38DFC  A8 20                           test al, 0x20
00B38DFE  75 05                           jne 0x140b38e05
00B38E00  49 03 C8                        add rcx, r8
00B38E03  EB 42                           jmp 0x140b38e47
00B38E05  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00B38E08  49 2B E8                        sub rbp, r8
00B38E0B  0F 10 11                        movups xmm2, xmmword ptr [rcx]
00B38E0E  0F 10 59 10                     movups xmm3, xmmword ptr [rcx + 0x10]
00B38E12  0F 10 61 20                     movups xmm4, xmmword ptr [rcx + 0x20]
00B38E16  0F 10 69 30                     movups xmm5, xmmword ptr [rcx + 0x30]
00B38E1A  0F 11 01                        movups xmmword ptr [rcx], xmm0
00B38E1D  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
00B38E21  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00B38E25  0F 10 42 20                     movups xmm0, xmmword ptr [rdx + 0x20]
00B38E29  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00B38E2D  0F 10 4A 30                     movups xmm1, xmmword ptr [rdx + 0x30]
00B38E31  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00B38E35  0F 11 12                        movups xmmword ptr [rdx], xmm2
00B38E38  0F 11 5A 10                     movups xmmword ptr [rdx + 0x10], xmm3
00B38E3C  0F 11 62 20                     movups xmmword ptr [rdx + 0x20], xmm4
00B38E40  0F 11 6A 30                     movups xmmword ptr [rdx + 0x30], xmm5
00B38E44  49 2B D0                        sub rdx, r8
00B38E47  48 3B CD                        cmp rcx, rbp
00B38E4A  72 AD                           jb 0x140b38df9
00B38E4C  83 FB 01                        cmp ebx, 1
00B38E4F  76 27                           jbe 0x140b38e78
00B38E51  41 8B C4                        mov eax, r12d
00B38E54  85 DB                           test ebx, ebx
00B38E56  74 0F                           je 0x140b38e67
00B38E58  48 8D 4E 14                     lea rcx, [rsi + 0x14]
00B38E5C  89 01                           mov dword ptr [rcx], eax
00B38E5E  FF C0                           inc eax
00B38E60  49 03 C8                        add rcx, r8
00B38E63  3B C3                           cmp eax, ebx
00B38E65  72 F5                           jb 0x140b38e5c
00B38E67  8B D3                           mov edx, ebx
00B38E69  4C 8D 0D 10 5A C0 FF            lea r9, [rip - 0x3fa5f0]
00B38E70  48 8B CE                        mov rcx, rsi
00B38E73  E8 78 7B 9C FF                  call 0x1405009f0
00B38E78  85 FF                           test edi, edi
00B38E7A  74 57                           je 0x140b38ed3
00B38E7C  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00B38E81  8B D3                           mov edx, ebx
00B38E83  48 8B CE                        mov rcx, rsi
00B38E86  E8 A5 27 BF FF                  call 0x14072b630
00B38E8B  8B D8                           mov ebx, eax
00B38E8D  85 C0                           test eax, eax
00B38E8F  78 47                           js 0x140b38ed8
00B38E91  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00B38E96  E8 39 65 F8 FF                  call 0x140abf3d4
00B38E9B  8B D8                           mov ebx, eax
00B38E9D  48 8B FE                        mov rdi, rsi
00B38EA0  48 3B F5                        cmp rsi, rbp
00B38EA3  0F 83 5A 01 00 00               jae 0x140b39003
00B38EA9  85 DB                           test ebx, ebx
00B38EAB  78 11                           js 0x140b38ebe
00B38EAD  48 8D 57 40                     lea rdx, [rdi + 0x40]
00B38EB1  45 33 C0                        xor r8d, r8d
00B38EB4  48 8B CF                        mov rcx, rdi
00B38EB7  E8 C8 57 C0 FF                  call 0x14073e684
00B38EBC  EB 07                           jmp 0x140b38ec5
00B38EBE  C7 47 38 18 00 00 C0            mov dword ptr [rdi + 0x38], 0xc0000018
00B38EC5  48 83 C7 40                     add rdi, 0x40
00B38EC9  48 3B FD                        cmp rdi, rbp
00B38ECC  72 DB                           jb 0x140b38ea9
00B38ECE  E9 30 01 00 00                  jmp 0x140b39003
00B38ED3  BB 01 00 00 C0                  mov ebx, 0xc0000001
00B38ED8  48 8B FE                        mov rdi, rsi
00B38EDB  41 BE 18 00 00 C0               mov r14d, 0xc0000018
00B38EE1  48 3B FD                        cmp rdi, rbp
00B38EE4  0F 83 11 01 00 00               jae 0x140b38ffb
00B38EEA  48 8B 07                        mov rax, qword ptr [rdi]
00B38EED  48 85 C0                        test rax, rax
00B38EF0  74 0D                           je 0x140b38eff
00B38EF2  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00B38EF9  4C 8B 78 28                     mov r15, qword ptr [rax + 0x28]
00B38EFD  EB 03                           jmp 0x140b38f02
00B38EFF  45 33 FF                        xor r15d, r15d
00B38F02  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00B38F07  BA 01 00 00 00                  mov edx, 1
00B38F0C  48 8B CF                        mov rcx, rdi
00B38F0F  E8 1C 27 BF FF                  call 0x14072b630
00B38F14  8B D8                           mov ebx, eax
00B38F16  85 C0                           test eax, eax
00B38F18  78 2D                           js 0x140b38f47
00B38F1A  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00B38F1F  41 BC 01 00 00 00               mov r12d, 1
00B38F25  E8 AA 64 F8 FF                  call 0x140abf3d4
00B38F2A  8B D8                           mov ebx, eax
00B38F2C  85 C0                           test eax, eax
00B38F2E  78 11                           js 0x140b38f41
00B38F30  48 8D 57 40                     lea rdx, [rdi + 0x40]
00B38F34  45 33 C0                        xor r8d, r8d
00B38F37  48 8B CF                        mov rcx, rdi
00B38F3A  E8 45 57 C0 FF                  call 0x14073e684
00B38F3F  EB 69                           jmp 0x140b38faa
00B38F41  44 89 77 38                     mov dword ptr [rdi + 0x38], r14d
00B38F45  EB 63                           jmp 0x140b38faa
00B38F47  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00B38F4C  74 78                           je 0x140b38fc6
00B38F4E  45 85 E4                        test r12d, r12d
00B38F51  75 4C                           jne 0x140b38f9f
00B38F53  8B 46 08                        mov eax, dword ptr [rsi + 8]
00B38F56  84 C0                           test al, al
00B38F58  78 45                           js 0x140b38f9f
00B38F5A  BA 00 00 04 00                  mov edx, 0x40000
00B38F5F  49 8B CF                        mov rcx, r15
00B38F62  E8 E1 30 DC FF                  call 0x1408fc048
00B38F67  45 33 C9                        xor r9d, r9d
00B38F6A  45 8D 44 24 01                  lea r8d, [r12 + 1]
00B38F6F  48 8B D7                        mov rdx, rdi
00B38F72  49 8B CF                        mov rcx, r15
00B38F75  E8 8E 65 C0 FF                  call 0x14073f508
00B38F7A  BA 00 00 04 00                  mov edx, 0x40000
00B38F7F  49 8B CF                        mov rcx, r15
00B38F82  8B D8                           mov ebx, eax
00B38F84  E8 CB 0F DC FF                  call 0x1408f9f54
00B38F89  85 DB                           test ebx, ebx
00B38F8B  79 26                           jns 0x140b38fb3
00B38F8D  B9 08 09 00 C0                  mov ecx, 0xc0000908
00B38F92  3B D9                           cmp ebx, ecx
00B38F94  8B C1                           mov eax, ecx
00B38F96  41 0F 45 C6                     cmovne eax, r14d
00B38F9A  89 47 38                        mov dword ptr [rdi + 0x38], eax
00B38F9D  EB 0B                           jmp 0x140b38faa
00B38F9F  83 4F 08 20                     or dword ptr [rdi + 8], 0x20
00B38FA3  C7 47 38 2D 02 00 C0            mov dword ptr [rdi + 0x38], 0xc000022d
00B38FAA  48 83 C7 40                     add rdi, 0x40
00B38FAE  E9 2E FF FF FF                  jmp 0x140b38ee1
00B38FB3  4D 85 ED                        test r13, r13
00B38FB6  74 05                           je 0x140b38fbd
00B38FB8  41 C6 45 00 01                  mov byte ptr [r13], 1
00B38FBD  48 83 C7 40                     add rdi, 0x40
00B38FC1  48 3B FD                        cmp rdi, rbp
00B38FC4  73 35                           jae 0x140b38ffb
00B38FC6  48 8B C5                        mov rax, rbp
00B38FC9  48 8D 4F 08                     lea rcx, [rdi + 8]
00B38FCD  48 2B C7                        sub rax, rdi
00B38FD0  48 FF C8                        dec rax
00B38FD3  48 C1 E8 06                     shr rax, 6
00B38FD7  48 FF C0                        inc rax
00B38FDA  81 FB 9A 00 00 C0               cmp ebx, 0xc000009a
00B38FE0  75 04                           jne 0x140b38fe6
00B38FE2  8B D3                           mov edx, ebx
00B38FE4  EB 08                           jmp 0x140b38fee
00B38FE6  83 09 20                        or dword ptr [rcx], 0x20
00B38FE9  BA 2D 02 00 C0                  mov edx, 0xc000022d
00B38FEE  89 51 30                        mov dword ptr [rcx + 0x30], edx
00B38FF1  48 83 C1 40                     add rcx, 0x40
00B38FF5  48 83 E8 01                     sub rax, 1
00B38FF9  75 DF                           jne 0x140b38fda
00B38FFB  44 8A BC 24 90 00 00 00         mov r15b, byte ptr [rsp + 0x90]
00B39003  48 8B D5                        mov rdx, rbp
00B39006  48 8B CE                        mov rcx, rsi
00B39009  E8 EA 5B BF FF                  call 0x14072ebf8
00B3900E  48 8B D5                        mov rdx, rbp
00B39011  48 8B CE                        mov rcx, rsi
00B39014  E8 9F 58 C0 FF                  call 0x14073e8b8
00B39019  90                              nop
00B3901A  E9 3A 1D EF FF                  jmp 0x140a2ad59
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B38CDE(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, unsigned int a16, __int64 a17, unsigned __int8 a18)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;

    if (result >= v_rbp) goto loc_00B38CFB;
    if ((*(unsigned int *)(result + 56)) < ((unsigned int)(v_r12))) goto loc_00B38CF6;
    if ((*(unsigned __int64 *)(result + 24)) != v_r12) goto loc_00B38CF6;
    goto loc_00B38D00;
loc_00B38CF6:
    result = (result) + (a3);
    goto loc_00B38CDE;
loc_00B38CFB:
    if (condition_is_equal) goto loc_00B38D38;
loc_00B38D00:
    if (v_rsi >= v_rbp) goto loc_00B38D30;
    a1 = (v_rdi - 1) >> (6);
    a1 = (a1) + 1;
loc_00B38D14:
    if ((*(unsigned int *)(v_rsi + 8 + 48)) < ((unsigned int)(v_r12))) goto loc_00B38D20;
    if ((*(unsigned __int64 *)(v_rsi + 8 + 16)) != v_r12) {
        *(unsigned int *)(v_rsi + 8 + 48) = a4;
    }
    result = (v_rsi + 8) + (a3);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00B38D14;
loc_00B38D30:
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12))) != 0) goto loc_00B3900E;
loc_00B38D38:
loc_00B38D3B:
    if (v_rsi >= v_rbp) goto loc_00B38D73;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00B38D55;
    goto loc_00B38D58;
loc_00B38D55:
loc_00B38D58:
    if ((((unsigned __int8)(a3)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r12 + 396))))) == 0) goto loc_00B38D6E;
    if ((*(unsigned __int64 *)(v_rsi + 24)) == v_r12) goto loc_00B38D6E;
    goto loc_00B38D7A;
loc_00B38D6E:
    a1 = (v_rsi) + (a3);
    goto loc_00B38D3B;
loc_00B38D73:
    if (condition_is_equal) goto loc_00B38DD3;
loc_00B38D7A:
    if (v_rsi >= v_rbp) goto loc_00B38DD3;
loc_00B38D8A:
    if (*(unsigned __int64 *)(v_rsi + 8 - 8) == 0) goto loc_00B38DA0;
    goto loc_00B38DA3;
loc_00B38DA0:
loc_00B38DA3:
    if ((((unsigned __int8)(a3)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r12 + 396))))) == 0) goto loc_00B38DB4;
    if ((*(unsigned __int64 *)(v_rsi + 8 + 16)) != v_r12) goto loc_00B38DC5;
loc_00B38DB4:
    result = (unsigned int)(*(unsigned int *)(v_rsi + 8));
    v_rbx = (unsigned int)(a16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 8)))) & (32)) == 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 8))) | (32));
        *(unsigned int *)(v_rsi + 8 + 48) = a4;
        *(unsigned int *)(v_rsi + 8) = (unsigned int)(result);
        v_rbx = (unsigned int)(((unsigned int)(a16)) - 1);
    }
    a1 = (v_rsi + 8) + (a3);
    if ((a1 - 8) < v_rbp) goto loc_00B38D8A;
    goto loc_00B38DDA;
loc_00B38DD3:
loc_00B38DDA:
    if ((unsigned int)((unsigned int)(a16)) != 0) goto loc_00B38DE8;
    goto loc_00B3900E;
loc_00B38DE8:
    if (((unsigned int)((unsigned int)(0xC0000001ULL))) == ((unsigned int)(v_r14))) goto loc_00B38E4C;
    if (v_rsi >= v_rbp) goto loc_00B38E4C;
loc_00B38DF9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 8)))) & (32)) != 0) goto loc_00B38E05;
    a1 = (v_rsi) + (a3);
    goto loc_00B38E47;
loc_00B38E05:
    v_rbp = (v_rbp) - (a3);
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rbp - 64) = v_xmm2;
    *(unsigned __int64 *)(v_rbp - 64 + 16) = v_xmm3;
    *(unsigned __int64 *)(v_rbp - 64 + 32) = v_xmm4;
    *(unsigned __int64 *)(v_rbp - 64 + 48) = v_xmm5;
    a2 = (v_rbp - 64) - (a3);
loc_00B38E47:
    if (a1 < v_rbp) goto loc_00B38DF9;
loc_00B38E4C:
    if (((unsigned int)((unsigned int)(0xC0000001ULL))) <= 1) goto loc_00B38E78;
    if ((unsigned int)((unsigned int)(0xC0000001ULL)) == 0) goto loc_00B38E67;
loc_00B38E5C:
    *(unsigned int *)(v_rsi + 20) = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    a1 = (v_rsi + 20) + (a3);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(0xC0000001ULL)))) goto loc_00B38E5C;
loc_00B38E67:
    result = qsort(v_rsi, (unsigned int)((unsigned int)((unsigned int)(0xC0000001ULL))), a3, v_rip - 4171248);
loc_00B38E78:
    if (1 == 0) goto loc_00B38ED3;
    result = PnpFindBestConfiguration(v_rsi, (unsigned int)((unsigned int)((unsigned int)(0xC0000001ULL))), a6, v_rip - 4171248);
    if (sign_flag) goto loc_00B38ED8;
    result = IopCommitConfiguration(a6, (unsigned int)((unsigned int)((unsigned int)(0xC0000001ULL))), a6, v_rip - 4171248);
    if (v_rsi >= v_rbp) goto loc_00B39003;
loc_00B38EA9:
    if (sign_flag) goto loc_00B38EBE;
    a3 = 0;
    result = PnpBuildCmResourceLists(v_rsi, v_rsi + 64, a3, v_rip - 4171248);
    goto loc_00B38EC5;
loc_00B38EBE:
    *(unsigned int *)(v_rsi + 56) = 0xC0000018ULL;
loc_00B38EC5:
    v_rdi = (v_rsi) + (64);
    if (v_rdi < v_rbp) goto loc_00B38EA9;
    goto loc_00B39003;
loc_00B38ED3:
loc_00B38ED8:
loc_00B38EE1:
    if (v_rsi >= v_rbp) goto loc_00B38FFB;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00B38EFF;
    goto loc_00B38F02;
loc_00B38EFF:
    v_r15 = 0;
loc_00B38F02:
    result = PnpFindBestConfiguration(v_rsi, 1, a6, v_rip - 4171248);
    if (sign_flag) goto loc_00B38F47;
    result = IopCommitConfiguration(a6, 1, a6, v_rip - 4171248);
    if (sign_flag) goto loc_00B38F41;
    a3 = 0;
    result = PnpBuildCmResourceLists(v_rsi, v_rsi + 64, a3, v_rip - 4171248);
    goto loc_00B38FAA;
loc_00B38F41:
    *(unsigned int *)(v_rsi + 56) = (unsigned int)((unsigned int)(0xC0000018ULL));
    goto loc_00B38FAA;
loc_00B38F47:
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_00B38FC6;
    if (1 != 0) goto loc_00B38F9F;
    if (sign_flag) goto loc_00B38F9F;
    result = PipSetDevNodeFlags(0, (unsigned int)(0x40000ULL), a3, v_rip - 4171248);
    a4 = 0;
    result = PnpRebalance(0, v_rsi, 1 + 1, a4);
    result = PipClearDevNodeFlags(0, (unsigned int)(0x40000ULL), 1 + 1, a4);
    if (!sign_flag) goto loc_00B38FB3;
    result = (unsigned int)((unsigned int)((unsigned int)(0xC0000908ULL)));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000908ULL)))) { result = (unsigned int)((unsigned int)(0xC0000018ULL)); }
    *(unsigned int *)(v_rsi + 56) = (unsigned int)(result);
    goto loc_00B38FAA;
loc_00B38F9F:
    *(unsigned int *)(v_rsi + 56) = 0xC000022DULL;
loc_00B38FAA:
    v_rdi = (v_rsi) + (64);
    goto loc_00B38EE1;
loc_00B38FB3:
    if (v_r13 != 0) {
        *(unsigned __int8 *)(v_r13) = 1;
    }
    v_rdi = (v_rdi) + (64);
    if (v_rdi >= v_rbp) goto loc_00B38FFB;
loc_00B38FC6:
    result = (v_rbp) - (v_rdi);
    result = (result) - 1;
    result = (result) >> (6);
    result = (result) + 1;
loc_00B38FDA:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC000009AULL) goto loc_00B38FE6;
    goto loc_00B38FEE;
loc_00B38FE6:
loc_00B38FEE:
    *(unsigned int *)(v_rdi + 8 + 48) = (unsigned int)((unsigned int)(0xC000022DULL));
    a1 = (v_rdi + 8) + (64);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00B38FDA;
loc_00B38FFB:
loc_00B39003:
    result = IopReleaseFilteredBootResources(v_rsi, v_rbp, 1 + 1, a4);
loc_00B3900E:
    result = PnpFreeResourceRequirementsForAssignTable(v_rsi, v_rbp, 1 + 1, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B38CDE(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, int64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint32_t Arg16, uint64_t Arg17, uint8_t Arg18)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;

    if (result >= local_rbp) goto loc_00B38CFB;
    if ((*(uint32_t *)(result + 0x38)) < ((uint32_t)(local_r12))) goto loc_00B38CF6;
    if ((*(uint64_t *)(result + 0x18)) != local_r12) goto loc_00B38CF6;
    goto loc_00B38D00;
loc_00B38CF6:
    result = (result) + (Arg3);
    goto loc_00B38CDE;
loc_00B38CFB:
    if (condition_is_equal) goto loc_00B38D38;
loc_00B38D00:
    if (local_rsi >= local_rbp) goto loc_00B38D30;
    Arg1 = (local_rdi - 1) >> (6);
    Arg1 = (Arg1) + 1;
loc_00B38D14:
    if ((*(uint32_t *)(local_rsi + 0x8 + 0x30)) < ((uint32_t)(local_r12))) goto loc_00B38D20;
    if ((*(uint64_t *)(local_rsi + 0x8 + 0x10)) != local_r12) {
        *(uint32_t *)(local_rsi + 0x8 + 0x30) = Arg4;
    }
    result = (local_rsi + 8) + (Arg3);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00B38D14;
loc_00B38D30:
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12))) != 0) goto loc_00B3900E;
loc_00B38D38:
loc_00B38D3B:
    if (local_rsi >= local_rbp) goto loc_00B38D73;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00B38D55;
    goto loc_00B38D58;
loc_00B38D55:
loc_00B38D58:
    if ((((uint8_t)(Arg3)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x18C))))) == 0) goto loc_00B38D6E;
    if ((*(uint64_t *)(local_rsi + 0x18)) == local_r12) goto loc_00B38D6E;
    goto loc_00B38D7A;
loc_00B38D6E:
    Arg1 = (local_rsi) + (Arg3);
    goto loc_00B38D3B;
loc_00B38D73:
    if (condition_is_equal) goto loc_00B38DD3;
loc_00B38D7A:
    if (local_rsi >= local_rbp) goto loc_00B38DD3;
loc_00B38D8A:
    if (*(uint64_t *)(local_rsi + 0x8 - 0x8) == 0) goto loc_00B38DA0;
    goto loc_00B38DA3;
loc_00B38DA0:
loc_00B38DA3:
    if ((((uint8_t)(Arg3)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x18C))))) == 0) goto loc_00B38DB4;
    if ((*(uint64_t *)(local_rsi + 0x8 + 0x10)) != local_r12) goto loc_00B38DC5;
loc_00B38DB4:
    result = (uint32_t)(*(uint32_t *)(local_rsi + 0x8));
    local_rbx = (uint32_t)(Arg16);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)))) & (32)) == 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x8))) | (32));
        *(uint32_t *)(local_rsi + 0x8 + 0x30) = Arg4;
        *(uint32_t *)(local_rsi + 0x8) = (uint32_t)(result);
        local_rbx = (uint32_t)(((uint32_t)(Arg16)) - 1);
    }
    Arg1 = (local_rsi + 8) + (Arg3);
    if ((Arg1 - 8) < local_rbp) goto loc_00B38D8A;
    goto loc_00B38DDA;
loc_00B38DD3:
loc_00B38DDA:
    if ((uint32_t)((uint32_t)(Arg16)) != 0) goto loc_00B38DE8;
    goto loc_00B3900E;
loc_00B38DE8:
    if (((uint32_t)((uint32_t)(0xC0000001ULL))) == ((uint32_t)(local_r14))) goto loc_00B38E4C;
    if (local_rsi >= local_rbp) goto loc_00B38E4C;
loc_00B38DF9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)))) & (32)) != 0) goto loc_00B38E05;
    Arg1 = (local_rsi) + (Arg3);
    goto loc_00B38E47;
loc_00B38E05:
    local_rbp = (local_rbp) - (Arg3);
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x30) = v_xmm1;
    *(uint64_t *)(local_rbp - 0x40) = v_xmm2;
    *(uint64_t *)(local_rbp - 0x40 + 0x10) = v_xmm3;
    *(uint64_t *)(local_rbp - 0x40 + 0x20) = v_xmm4;
    *(uint64_t *)(local_rbp - 0x40 + 0x30) = v_xmm5;
    Arg2 = (local_rbp - 64) - (Arg3);
loc_00B38E47:
    if (Arg1 < local_rbp) goto loc_00B38DF9;
loc_00B38E4C:
    if (((uint32_t)((uint32_t)(0xC0000001ULL))) <= 1) goto loc_00B38E78;
    if ((uint32_t)((uint32_t)(0xC0000001ULL)) == 0) goto loc_00B38E67;
loc_00B38E5C:
    *(uint32_t *)(local_rsi + 0x14) = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    Arg1 = (local_rsi + 20) + (Arg3);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(0xC0000001ULL)))) goto loc_00B38E5C;
loc_00B38E67:
    result = qsort(local_rsi, (uint32_t)((uint32_t)((uint32_t)(0xC0000001ULL))), Arg3, v_rip - 4171248);
loc_00B38E78:
    if (1 == 0) goto loc_00B38ED3;
    result = PnpFindBestConfiguration(local_rsi, (uint32_t)((uint32_t)((uint32_t)(0xC0000001ULL))), Arg6, v_rip - 4171248);
    if (sign_flag) goto loc_00B38ED8;
    result = IopCommitConfiguration(Arg6, (uint32_t)((uint32_t)((uint32_t)(0xC0000001ULL))), Arg6, v_rip - 4171248);
    if (local_rsi >= local_rbp) goto loc_00B39003;
loc_00B38EA9:
    if (sign_flag) goto loc_00B38EBE;
    Arg3 = 0;
    result = PnpBuildCmResourceLists(local_rsi, local_rsi + 64, Arg3, v_rip - 4171248);
    goto loc_00B38EC5;
loc_00B38EBE:
    *(uint32_t *)(local_rsi + 0x38) = 0xC0000018ULL;
loc_00B38EC5:
    local_rdi = (local_rsi) + (64);
    if (local_rdi < local_rbp) goto loc_00B38EA9;
    goto loc_00B39003;
loc_00B38ED3:
loc_00B38ED8:
loc_00B38EE1:
    if (local_rsi >= local_rbp) goto loc_00B38FFB;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00B38EFF;
    goto loc_00B38F02;
loc_00B38EFF:
    local_r15 = 0;
loc_00B38F02:
    result = PnpFindBestConfiguration(local_rsi, 1, Arg6, v_rip - 4171248);
    if (sign_flag) goto loc_00B38F47;
    result = IopCommitConfiguration(Arg6, 1, Arg6, v_rip - 4171248);
    if (sign_flag) goto loc_00B38F41;
    Arg3 = 0;
    result = PnpBuildCmResourceLists(local_rsi, local_rsi + 64, Arg3, v_rip - 4171248);
    goto loc_00B38FAA;
loc_00B38F41:
    *(uint32_t *)(local_rsi + 0x38) = (uint32_t)((uint32_t)(0xC0000018ULL));
    goto loc_00B38FAA;
loc_00B38F47:
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_00B38FC6;
    if (1 != 0) goto loc_00B38F9F;
    if (sign_flag) goto loc_00B38F9F;
    result = PipSetDevNodeFlags(0, (uint32_t)(0x40000ULL), Arg3, v_rip - 4171248);
    Arg4 = 0;
    result = PnpRebalance(0, local_rsi, 1 + 1, Arg4);
    result = PipClearDevNodeFlags(0, (uint32_t)(0x40000ULL), 1 + 1, Arg4);
    if (!sign_flag) goto loc_00B38FB3;
    result = (uint32_t)((uint32_t)((uint32_t)(0xC0000908ULL)));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000908ULL)))) { result = (uint32_t)((uint32_t)(0xC0000018ULL)); }
    *(uint32_t *)(local_rsi + 0x38) = (uint32_t)(result);
    goto loc_00B38FAA;
loc_00B38F9F:
    *(uint32_t *)(local_rsi + 0x38) = 0xC000022DULL;
loc_00B38FAA:
    local_rdi = (local_rsi) + (64);
    goto loc_00B38EE1;
loc_00B38FB3:
    if (local_r13 != 0) {
        *(uint8_t *)(local_r13) = 1;
    }
    local_rdi = (local_rdi) + (64);
    if (local_rdi >= local_rbp) goto loc_00B38FFB;
loc_00B38FC6:
    result = (local_rbp) - (local_rdi);
    result = (result) - 1;
    result = (result) >> (6);
    result = (result) + 1;
loc_00B38FDA:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC000009AULL) goto loc_00B38FE6;
    goto loc_00B38FEE;
loc_00B38FE6:
loc_00B38FEE:
    *(uint32_t *)(local_rdi + 0x8 + 0x30) = (uint32_t)((uint32_t)(0xC000022DULL));
    Arg1 = (local_rdi + 8) + (64);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00B38FDA;
loc_00B38FFB:
loc_00B39003:
    result = IopReleaseFilteredBootResources(local_rsi, local_rbp, 1 + 1, Arg4);
loc_00B3900E:
    result = PnpFreeResourceRequirementsForAssignTable(local_rsi, local_rbp, 1 + 1, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B38CDE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
