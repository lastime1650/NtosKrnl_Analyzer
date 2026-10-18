# VmpSplitMemoryRange

- RVA: `0x00429754`–`0x00429B9E` (길이 `1,098` bytes)
- VA: `0x0000000140429754`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A0F10`
- 디코드: `282`개 명령, `1,098/1,098` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004297AC` → [VmpProcessContextLockShared](VmpProcessContextLockShared_function_00429DB0.md) (function, `0x00429DB0`)
- `0x004297F6` → [VmpVaRangeNumberOfGpaRanges](VmpVaRangeNumberOfGpaRanges_function_00429E34.md) (function, `0x00429E34`)
- `0x00429804` → [VmpProcessContextUnlockShared](VmpProcessContextUnlockShared_function_00429DFC.md) (function, `0x00429DFC`)
- `0x00429814` → [VmpAllocateMemoryRanges](../../page/A7/VmpAllocateMemoryRanges_function_00A75660.md) (function, `0x00A75660`)
- `0x0042983E` → [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) (function, `0x003147A4`)
- `0x004298F4` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00429985` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00429AD0` → [VmpFindNextPinnedPageStateHelper](../64/VmpFindNextPinnedPageStateHelper_function_0064C7E4.md) (function, `0x0064C7E4`)
- `0x00429AFC` → [VmpVaRangeCheckPinnedGpaRanges](../64/VmpVaRangeCheckPinnedGpaRanges_function_0064D8AC.md) (function, `0x0064D8AC`)
- `0x00429B07` → [VmpVaRangeCheckPinnedGpaRanges](../64/VmpVaRangeCheckPinnedGpaRanges_function_0064D8AC.md) (function, `0x0064D8AC`)
- `0x00429B3D` → [VmpProcessContextUnlockShared](VmpProcessContextUnlockShared_function_00429DFC.md) (function, `0x00429DFC`)
- `0x00429B62` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (function, `0x007AE05C`)
- `0x00429B87` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (function, `0x007AE05C`)
- `0x00429B94` → [VmpFreeMemoryRanges](../../page/A7/VmpFreeMemoryRanges_function_00A75744.md) (function, `0x00A75744`)

### Direct callers
- [VmSplitMemoryRange](../../page/A9/VmSplitMemoryRange_function_00A922A0.md) at `0x00A92309`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00429814` → [VmpAllocateMemoryRanges](../../page/A7/VmpAllocateMemoryRanges_function_00A75660.md) (`.text` → `PAGE`)
  - `0x00429B62` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (`.text` → `PAGE`)
  - `0x00429B87` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (`.text` → `PAGE`)
  - `0x00429B94` → [VmpFreeMemoryRanges](../../page/A7/VmpFreeMemoryRanges_function_00A75744.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x004297C9` → [sub_006EE148](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x004297D2` → [sub_006EE148](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x004297DB` → [sub_006EE148](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x0042982D` → [sub_006EE148 + 0x3C](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x00429AD9` → [sub_006EE148 + 0xA2](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x00429AE3` → [sub_006EE148 + 0xA2](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x00429B1C` → [sub_006EE148 + 0xCB](../6E/Unknown_function_006EE148.md) (`tail-transfer`)
  - `0x00429B37` → [sub_006EE148 + 0xD8](../6E/Unknown_function_006EE148.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00429754  48 8B C4                        mov rax, rsp
00429757  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0042975B  55                              push rbp
0042975C  56                              push rsi
0042975D  57                              push rdi
0042975E  41 54                           push r12
00429760  41 55                           push r13
00429762  41 56                           push r14
00429764  41 57                           push r15
00429766  48 83 EC 70                     sub rsp, 0x70
0042976A  4C 8B F1                        mov r14, rcx
0042976D  49 8B D8                        mov rbx, r8
00429770  33 C9                           xor ecx, ecx
00429772  4C 8B FA                        mov r15, rdx
00429775  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
00429779  8B F1                           mov esi, ecx
0042977B  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00429780  44 8B E1                        mov r12d, ecx
00429783  48 89 48 A0                     mov qword ptr [rax - 0x60], rcx
00429787  44 8B E9                        mov r13d, ecx
0042978A  8D 69 01                        lea ebp, [rcx + 1]
0042978D  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00429792  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00429797  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
0042979F  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
004297A4  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
004297A9  49 8B CE                        mov rcx, r14
004297AC  E8 FF 05 00 00                  call 0x140429db0
004297B1  4C 8B C0                        mov r8, rax
004297B4  49 39 5E 68                     cmp qword ptr [r14 + 0x68], rbx
004297B8  0F 85 E8 02 00 00               jne 0x140429aa6
004297BE  49 8D 76 18                     lea rsi, [r14 + 0x18]
004297C2  48 8B 3E                        mov rdi, qword ptr [rsi]
004297C5  40 84 6E 08                     test byte ptr [rsi + 8], bpl
004297C9  0F 84 79 49 2C 00               je 0x1406ee148
004297CF  48 85 FF                        test rdi, rdi
004297D2  0F 84 70 49 2C 00               je 0x1406ee148
004297D8  48 33 FE                        xor rdi, rsi
004297DB  E9 68 49 2C 00                  jmp 0x1406ee148
004297E0  48 85 FF                        test rdi, rdi
004297E3  0F 84 4A 02 00 00               je 0x140429a33
004297E9  4C 3B 7F 20                     cmp r15, qword ptr [rdi + 0x20]
004297ED  0F 84 C6 02 00 00               je 0x140429ab9
004297F3  48 8B CF                        mov rcx, rdi
004297F6  E8 39 06 00 00                  call 0x140429e34
004297FB  49 8B D0                        mov rdx, r8
004297FE  49 8B CE                        mov rcx, r14
00429801  48 8B D8                        mov rbx, rax
00429804  E8 F3 05 00 00                  call 0x140429dfc
00429809  44 21 A4 24 B0 00 00 00         and dword ptr [rsp + 0xb0], r12d
00429811  48 8B CB                        mov rcx, rbx
00429814  E8 47 BE 64 00                  call 0x140a75660
00429819  48 8B E8                        mov rbp, rax
0042981C  48 85 C0                        test rax, rax
0042981F  0F 84 62 02 00 00               je 0x140429a87
00429825  4D 8D 67 01                     lea r12, [r15 + 1]
00429829  4C 39 6F 38                     cmp qword ptr [rdi + 0x38], r13
0042982D  0F 85 51 49 2C 00               jne 0x1406ee184
00429833  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0042983B  49 8B CE                        mov rcx, r14
0042983E  E8 61 AF EE FF                  call 0x1403147a4
00429843  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00429848  49 8B C7                        mov rax, r15
0042984B  48 2B 47 18                     sub rax, qword ptr [rdi + 0x18]
0042984F  48 FF C0                        inc rax
00429852  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00429857  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0042985B  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0042985F  4C 89 65 18                     mov qword ptr [rbp + 0x18], r12
00429863  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00429866  4C 89 7F 20                     mov qword ptr [rdi + 0x20], r15
0042986A  83 E0 02                        and eax, 2
0042986D  8B 4D 48                        mov ecx, dword ptr [rbp + 0x48]
00429870  83 E1 FC                        and ecx, 0xfffffffc
00429873  48 89 5D 38                     mov qword ptr [rbp + 0x38], rbx
00429877  33 C8                           xor ecx, eax
00429879  33 DB                           xor ebx, ebx
0042987B  41 0B CD                        or ecx, r13d
0042987E  48 89 9C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rbx
00429886  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
00429889  F6 46 08 01                     test byte ptr [rsi + 8], 1
0042988D  48 8B 16                        mov rdx, qword ptr [rsi]
00429890  0F 85 D3 01 00 00               jne 0x140429a69
00429896  0F B6 4E 08                     movzx ecx, byte ptr [rsi + 8]
0042989A  45 32 C0                        xor r8b, r8b
0042989D  83 E1 01                        and ecx, 1
004298A0  48 85 D2                        test rdx, rdx
004298A3  74 49                           je 0x1404298ee
004298A5  4C 8B 45 18                     mov r8, qword ptr [rbp + 0x18]
004298A9  4C 3B 42 20                     cmp r8, qword ptr [rdx + 0x20]
004298AD  77 27                           ja 0x1404298d6
004298AF  4C 3B 42 18                     cmp r8, qword ptr [rdx + 0x18]
004298B3  73 21                           jae 0x1404298d6
004298B5  48 8B 02                        mov rax, qword ptr [rdx]
004298B8  85 C9                           test ecx, ecx
004298BA  74 0C                           je 0x1404298c8
004298BC  48 85 C0                        test rax, rax
004298BF  0F 84 CC 01 00 00               je 0x140429a91
004298C5  48 33 C2                        xor rax, rdx
004298C8  48 85 C0                        test rax, rax
004298CB  0F 84 C0 01 00 00               je 0x140429a91
004298D1  48 8B D0                        mov rdx, rax
004298D4  EB D3                           jmp 0x1404298a9
004298D6  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
004298DA  85 C9                           test ecx, ecx
004298DC  0F 84 6C 01 00 00               je 0x140429a4e
004298E2  48 85 C0                        test rax, rax
004298E5  0F 85 60 01 00 00               jne 0x140429a4b
004298EB  41 B0 01                        mov r8b, 1
004298EE  4C 8B CD                        mov r9, rbp
004298F1  48 8B CE                        mov rcx, rsi
004298F4  E8 77 AC EB FF                  call 0x1402e4570
004298F9  48 8B 5D 28                     mov rbx, qword ptr [rbp + 0x28]
004298FD  4C 8D 67 28                     lea r12, [rdi + 0x28]
00429901  49 8B 34 24                     mov rsi, qword ptr [r12]
00429905  4D 8D 7E 08                     lea r15, [r14 + 8]
00429909  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0042990E  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00429912  49 03 CD                        add rcx, r13
00429915  48 89 4B 30                     mov qword ptr [rbx + 0x30], rcx
00429919  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
0042991D  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
00429921  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00429924  4C 8D 41 FF                     lea r8, [rcx - 1]
00429928  4C 89 46 38                     mov qword ptr [rsi + 0x38], r8
0042992C  A8 01                           test al, 1
0042992E  0F 85 8F 01 00 00               jne 0x140429ac3
00429934  41 F6 47 08 01                  test byte ptr [r15 + 8], 1
00429939  49 8B 17                        mov rdx, qword ptr [r15]
0042993C  0F 85 38 01 00 00               jne 0x140429a7a
00429942  41 0F B6 4F 08                  movzx ecx, byte ptr [r15 + 8]
00429947  45 32 C0                        xor r8b, r8b
0042994A  83 E1 01                        and ecx, 1
0042994D  48 85 D2                        test rdx, rdx
00429950  74 2C                           je 0x14042997e
00429952  4C 8B 43 30                     mov r8, qword ptr [rbx + 0x30]
00429956  4C 3B 42 20                     cmp r8, qword ptr [rdx + 0x20]
0042995A  77 0A                           ja 0x140429966
0042995C  4C 3B 42 18                     cmp r8, qword ptr [rdx + 0x18]
00429960  0F 82 B1 00 00 00               jb 0x140429a17
00429966  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0042996A  85 C9                           test ecx, ecx
0042996C  0F 84 ED 00 00 00               je 0x140429a5f
00429972  48 85 C0                        test rax, rax
00429975  0F 85 E1 00 00 00               jne 0x140429a5c
0042997B  41 B0 01                        mov r8b, 1
0042997E  4C 8D 4B 18                     lea r9, [rbx + 0x18]
00429982  49 8B CF                        mov rcx, r15
00429985  E8 E6 AB EB FF                  call 0x1402e4570
0042998A  48 8B 36                        mov rsi, qword ptr [rsi]
0042998D  49 3B F4                        cmp rsi, r12
00429990  0F 85 52 01 00 00               jne 0x140429ae8
00429996  48 83 7D 38 00                  cmp qword ptr [rbp + 0x38], 0
0042999B  0F 85 4F 01 00 00               jne 0x140429af0
004299A1  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
004299A6  48 8B B4 24 C8 00 00 00         mov rsi, qword ptr [rsp + 0xc8]
004299AE  4D 8B EF                        mov r13, r15
004299B1  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
004299B9  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
004299BE  49 FF 46 48                     inc qword ptr [r14 + 0x48]
004299C2  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
004299C7  33 DB                           xor ebx, ebx
004299C9  8B AC 24 B0 00 00 00            mov ebp, dword ptr [rsp + 0xb0]
004299D0  49 83 F8 FF                     cmp r8, -1
004299D4  0F 85 55 01 00 00               jne 0x140429b2f
004299DA  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004299DF  33 ED                           xor ebp, ebp
004299E1  48 85 C0                        test rax, rax
004299E4  0F 85 5D 01 00 00               jne 0x140429b47
004299EA  48 85 F6                        test rsi, rsi
004299ED  0F 85 79 01 00 00               jne 0x140429b6c
004299F3  48 85 ED                        test rbp, rbp
004299F6  0F 85 95 01 00 00               jne 0x140429b91
004299FC  8B C3                           mov eax, ebx
004299FE  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
00429A06  48 83 C4 70                     add rsp, 0x70
00429A0A  41 5F                           pop r15
00429A0C  41 5E                           pop r14
00429A0E  41 5D                           pop r13
00429A10  41 5C                           pop r12
00429A12  5F                              pop rdi
00429A13  5E                              pop rsi
00429A14  5D                              pop rbp
00429A15  C3                              ret
00429A16  CC                              int3
00429A17  48 8B 02                        mov rax, qword ptr [rdx]
00429A1A  85 C9                           test ecx, ecx
00429A1C  74 08                           je 0x140429a26
00429A1E  48 85 C0                        test rax, rax
00429A21  74 76                           je 0x140429a99
00429A23  48 33 C2                        xor rax, rdx
00429A26  48 85 C0                        test rax, rax
00429A29  74 6E                           je 0x140429a99
00429A2B  48 8B D0                        mov rdx, rax
00429A2E  E9 23 FF FF FF                  jmp 0x140429956
00429A33  BB 8C 02 00 C0                  mov ebx, 0xc000028c
00429A38  48 8B B4 24 C8 00 00 00         mov rsi, qword ptr [rsp + 0xc8]
00429A40  49 8B FC                        mov rdi, r12
00429A43  4D 8B FC                        mov r15, r12
00429A46  4D 8B EC                        mov r13, r12
00429A49  EB 85                           jmp 0x1404299d0
00429A4B  48 33 C2                        xor rax, rdx
00429A4E  48 85 C0                        test rax, rax
00429A51  0F 85 7A FE FF FF               jne 0x1404298d1
00429A57  E9 8F FE FF FF                  jmp 0x1404298eb
00429A5C  48 33 C2                        xor rax, rdx
00429A5F  48 85 C0                        test rax, rax
00429A62  75 C7                           jne 0x140429a2b
00429A64  E9 12 FF FF FF                  jmp 0x14042997b
00429A69  48 85 D2                        test rdx, rdx
00429A6C  0F 84 24 FE FF FF               je 0x140429896
00429A72  48 33 D6                        xor rdx, rsi
00429A75  E9 1C FE FF FF                  jmp 0x140429896
00429A7A  48 85 D2                        test rdx, rdx
00429A7D  74 22                           je 0x140429aa1
00429A7F  49 33 D7                        xor rdx, r15
00429A82  E9 BB FE FF FF                  jmp 0x140429942
00429A87  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00429A8C  E9 6B FF FF FF                  jmp 0x1404299fc
00429A91  45 32 C0                        xor r8b, r8b
00429A94  E9 55 FE FF FF                  jmp 0x1404298ee
00429A99  45 32 C0                        xor r8b, r8b
00429A9C  E9 DD FE FF FF                  jmp 0x14042997e
00429AA1  E9 9C FE FF FF                  jmp 0x140429942
00429AA6  BB 19 07 00 C0                  mov ebx, 0xc0000719
00429AAB  48 8B FE                        mov rdi, rsi
00429AAE  4C 8B FE                        mov r15, rsi
00429AB1  4C 8B EE                        mov r13, rsi
00429AB4  E9 17 FF FF FF                  jmp 0x1404299d0
00429AB9  BB 41 01 00 C0                  mov ebx, 0xc0000141
00429ABE  E9 75 FF FF FF                  jmp 0x140429a38
00429AC3  48 8B 56 30                     mov rdx, qword ptr [rsi + 0x30]
00429AC7  41 B9 01 00 00 00               mov r9d, 1
00429ACD  49 8B CE                        mov rcx, r14
00429AD0  E8 0F 2D 22 00                  call 0x14064c7e4
00429AD5  48 83 F8 FF                     cmp rax, -1
00429AD9  0F 85 0B 47 2C 00               jne 0x1406ee1ea
00429ADF  83 66 40 FE                     and dword ptr [rsi + 0x40], 0xfffffffe
00429AE3  E9 02 47 2C 00                  jmp 0x1406ee1ea
00429AE8  48 8B 1B                        mov rbx, qword ptr [rbx]
00429AEB  E9 1E FE FF FF                  jmp 0x14042990e
00429AF0  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00429AF4  48 8B CD                        mov rcx, rbp
00429AF7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00429AFC  E8 AB 3D 22 00                  call 0x14064d8ac
00429B01  48 8B CF                        mov rcx, rdi
00429B04  48 8B F0                        mov rsi, rax
00429B07  E8 A0 3D 22 00                  call 0x14064d8ac
00429B0C  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
00429B11  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
00429B19  48 85 C0                        test rax, rax
00429B1C  0F 84 F1 46 2C 00               je 0x1406ee213
00429B22  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
00429B27  4D 8B FC                        mov r15, r12
00429B2A  E9 8F FE FF FF                  jmp 0x1404299be
00429B2F  49 8B D0                        mov rdx, r8
00429B32  49 8B CE                        mov rcx, r14
00429B35  85 ED                           test ebp, ebp
00429B37  0F 84 E3 46 2C 00               je 0x1406ee220
00429B3D  E8 BA 02 00 00                  call 0x140429dfc
00429B42  E9 93 FE FF FF                  jmp 0x1404299da
00429B47  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00429B4C  4D 8B CF                        mov r9, r15
00429B4F  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00429B54  4D 8B C5                        mov r8, r13
00429B57  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00429B5C  48 8B D0                        mov rdx, rax
00429B5F  49 8B CE                        mov rcx, r14
00429B62  E8 F5 44 38 00                  call 0x1407ae05c
00429B67  E9 7E FE FF FF                  jmp 0x1404299ea
00429B6C  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00429B71  4C 8B C7                        mov r8, rdi
00429B74  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00429B79  4C 8B C8                        mov r9, rax
00429B7C  48 8B D6                        mov rdx, rsi
00429B7F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00429B84  49 8B CE                        mov rcx, r14
00429B87  E8 D0 44 38 00                  call 0x1407ae05c
00429B8C  E9 62 FE FF FF                  jmp 0x1404299f3
00429B91  48 8B CD                        mov rcx, rbp
00429B94  E8 AB BB 64 00                  call 0x140a75744
00429B99  E9 5E FE FF FF                  jmp 0x1404299fc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpSplitMemoryRange(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    v_rsp = (v_rsp) - (112);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp + 32) = 0;
    v_stack_m48 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    v_stack_m58 = 0;
    v_stack_m78 = 0;
    v_stack_p18 = 0;
    v_stack_m50 = 0;
    v_stack_m70 = 0;
    result = VmpProcessContextLockShared(0, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 104)) != a3) goto loc_00429AA6;
    v_rdi = (*(unsigned __int64 *)(a1 + 24)) ^ (a1 + 24);
loc_004299D0:
    if (result != -1) goto loc_00429B2F;
loc_004299DA:
    v_rbp = 0;
    if (v_stack_m48 != 0) goto loc_00429B47;
loc_004299EA:
    if (a1 + 24 != 0) goto loc_00429B6C;
loc_004299F3:
    if (0 != 0) goto loc_00429B91;
loc_004299FC:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)(a3));
loc_00429AA6:
    goto loc_004299D0;
loc_00429B2F:
    result = VmpProcessContextUnlockShared(0, result, result, a4);
    goto loc_004299DA;
loc_00429B47:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p50;
    result = VmpUnsecureMemoryForPin(0, result, a1 + 24, a1 + 24);
    goto loc_004299EA;
loc_00429B6C:
    v_stack_p28 = v_stack_p58;
    v_stack_p20 = a1 + 24;
    result = VmpUnsecureMemoryForPin(0, a1 + 24, a1 + 24, v_stack_p58);
    goto loc_004299F3;
loc_00429B91:
    result = VmpFreeMemoryRanges(0, a1 + 24, a1 + 24, v_stack_p58);
    goto loc_004299FC;
}
```

## 5. (Beta) C Style

```c
int64_t VmpSplitMemoryRange(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    local_rsp = (local_rsp) - (112);
    Arg1 = 0;
    *(uint64_t *)(local_rsp + 0x20) = 0;
    v_stack_m48 = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    v_stack_m58 = 0;
    v_stack_m78 = 0;
    v_stack_p18 = 0;
    v_stack_m50 = 0;
    v_stack_m70 = 0;
    result = VmpProcessContextLockShared(0, Arg2, Arg3, a4);
    if ((*(uint64_t *)(arg1 + 0x68)) != Arg3) goto loc_00429AA6;
    local_rdi = (*(uint64_t *)(arg1 + 0x18)) ^ (Arg1 + 24);
loc_004299D0:
    if (result != -1) goto loc_00429B2F;
loc_004299DA:
    local_rbp = 0;
    if (v_stack_m48 != 0) goto loc_00429B47;
loc_004299EA:
    if (Arg1 + 24 != 0) goto loc_00429B6C;
loc_004299F3:
    if (0 != 0) goto loc_00429B91;
loc_004299FC:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)(Arg3));
loc_00429AA6:
    goto loc_004299D0;
loc_00429B2F:
    result = VmpProcessContextUnlockShared(0, result, result, a4);
    goto loc_004299DA;
loc_00429B47:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p50;
    result = VmpUnsecureMemoryForPin(0, result, Arg1 + 24, Arg1 + 24);
    goto loc_004299EA;
loc_00429B6C:
    v_stack_p28 = v_stack_p58;
    v_stack_p20 = Arg1 + 24;
    result = VmpUnsecureMemoryForPin(0, Arg1 + 24, Arg1 + 24, v_stack_p58);
    goto loc_004299F3;
loc_00429B91:
    result = VmpFreeMemoryRanges(0, Arg1 + 24, Arg1 + 24, v_stack_p58);
    goto loc_004299FC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00429754&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
