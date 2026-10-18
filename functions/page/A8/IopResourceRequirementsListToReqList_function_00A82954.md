# IopResourceRequirementsListToReqList

- RVA: `0x00A82954`–`0x00A82E62` (길이 `1,294` bytes)
- VA: `0x0000000140A82954`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B7334`
- 디코드: `338`개 명령, `1,294/1,294` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A82A65` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A82A7E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A82A97` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A82AAD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A82B01` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A82C9C` → [IopSetupArbiterAndTranslators](IopSetupArbiterAndTranslators_function_00A82E68.md) (function, `0x00A82E68`)
- `0x00A82CC8` → [IopFreeReqAlternative](../70/IopFreeReqAlternative_function_007027B4.md) (function, `0x007027B4`)
- `0x00A82D5D` → [IopFreeReqList](../72/IopFreeReqList_function_0072ADAC.md) (function, `0x0072ADAC`)

### Direct callers
- [PnpReleaseBootResourcesForFilteredRequirements](../../text/5A/PnpReleaseBootResourcesForFilteredRequirements_function_005A79D4.md) at `0x005A7AAD`
- [IopAllocateBootResourcesInternal](../72/IopAllocateBootResourcesInternal_function_0072E708.md) at `0x0072E783`
- [PnpRestoreResourcesInternal](../73/PnpRestoreResourcesInternal_function_0073EB10.md) at `0x0073EB88`
- [sub_00B39020](../B3/Unknown_function_00B39020.md) at `0x00B39049`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00A82A65` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A82A7E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A82A97` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A82AAD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A82B01` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00A82D0C` → [sub_00B43A94 + 0x83](../B4/Unknown_function_00B43A94.md) (`tail-transfer`)
  - `0x00A82DFE` → [sub_00B43A94 + 0x79](../B4/Unknown_function_00B43A94.md) (`tail-transfer`)
  - `0x00A82E07` → [sub_00B43A94 + 0x79](../B4/Unknown_function_00B43A94.md) (`tail-transfer`)
  - `0x00A82E10` → [sub_00B43A94 + 0x79](../B4/Unknown_function_00B43A94.md) (`tail-transfer`)
  - `0x00A82E1A` → [sub_00B43A94](../B4/Unknown_function_00B43A94.md) (`tail-transfer`)
  - `0x00A82E24` → [sub_00B43A94](../B4/Unknown_function_00B43A94.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A82954  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00A82959  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00A8295E  53                              push rbx
00A8295F  55                              push rbp
00A82960  56                              push rsi
00A82961  57                              push rdi
00A82962  41 54                           push r12
00A82964  41 55                           push r13
00A82966  41 56                           push r14
00A82968  41 57                           push r15
00A8296A  48 83 EC 78                     sub rsp, 0x78
00A8296E  48 83 22 00                     and qword ptr [rdx], 0
00A82972  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00A82976  83 A4 24 D0 00 00 00 00         and dword ptr [rsp + 0xd0], 0
00A8297E  8B 78 1C                        mov edi, dword ptr [rax + 0x1c]
00A82981  85 FF                           test edi, edi
00A82983  0F 84 50 03 00 00               je 0x140a82cd9
00A82989  8B 18                           mov ebx, dword ptr [rax]
00A8298B  4C 8D 68 20                     lea r13, [rax + 0x20]
00A8298F  33 D2                           xor edx, edx
00A82991  48 03 D8                        add rbx, rax
00A82994  4D 8B C5                        mov r8, r13
00A82997  33 F6                           xor esi, esi
00A82999  44 8D 52 01                     lea r10d, [rdx + 1]
00A8299D  41 2B FA                        sub edi, r10d
00A829A0  0F 89 40 04 00 00               jns 0x140a82de6
00A829A6  44 8B 60 1C                     mov r12d, dword ptr [rax + 0x1c]
00A829AA  2B D6                           sub edx, esi
00A829AC  83 64 24 48 00                  and dword ptr [rsp + 0x48], 0
00A829B1  4C 8B F8                        mov r15, rax
00A829B4  8B C2                           mov eax, edx
00A829B6  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00A829BC  4C 69 F0 28 01 00 00            imul r14, rax, 0x128
00A829C3  C7 44 24 28 01 00 00 C0         mov dword ptr [rsp + 0x28], 0xc0000001
00A829CB  4D 3B F0                        cmp r14, r8
00A829CE  77 3A                           ja 0x140a82a0a
00A829D0  41 3B D2                        cmp edx, r10d
00A829D3  76 4C                           jbe 0x140a82a21
00A829D5  8D 4A FF                        lea ecx, [rdx - 1]
00A829D8  41 8B C0                        mov eax, r8d
00A829DB  48 C1 E1 03                     shl rcx, 3
00A829DF  49 3B C8                        cmp rcx, r8
00A829E2  0F 46 C1                        cmovbe eax, ecx
00A829E5  77 23                           ja 0x140a82a0a
00A829E7  8D 48 20                        lea ecx, [rax + 0x20]
00A829EA  8B D1                           mov edx, ecx
00A829EC  3B C8                           cmp ecx, eax
00A829EE  72 1A                           jb 0x140a82a0a
00A829F0  EB 36                           jmp 0x140a82a28
00A829F2  41 8D 4C 24 FF                  lea ecx, [r12 - 1]
00A829F7  41 8B C0                        mov eax, r8d
00A829FA  48 C1 E1 03                     shl rcx, 3
00A829FE  49 3B C8                        cmp rcx, r8
00A82A01  0F 46 C1                        cmovbe eax, ecx
00A82A04  0F 86 1F 04 00 00               jbe 0x140a82e29
00A82A0A  B8 05 00 00 80                  mov eax, 0x80000005
00A82A0F  48 83 C4 78                     add rsp, 0x78
00A82A13  41 5F                           pop r15
00A82A15  41 5E                           pop r14
00A82A17  41 5D                           pop r13
00A82A19  41 5C                           pop r12
00A82A1B  5F                              pop rdi
00A82A1C  5E                              pop rsi
00A82A1D  5D                              pop rbp
00A82A1E  5B                              pop rbx
00A82A1F  C3                              ret
00A82A20  CC                              int3
00A82A21  33 C0                           xor eax, eax
00A82A23  8D 48 20                        lea ecx, [rax + 0x20]
00A82A26  8B D1                           mov edx, ecx
00A82A28  3B D0                           cmp edx, eax
00A82A2A  72 DE                           jb 0x140a82a0a
00A82A2C  8B F1                           mov esi, ecx
00A82A2E  49 0F AF F4                     imul rsi, r12
00A82A32  49 3B F0                        cmp rsi, r8
00A82A35  77 D3                           ja 0x140a82a0a
00A82A37  45 3B E2                        cmp r12d, r10d
00A82A3A  77 B6                           ja 0x140a829f2
00A82A3C  33 C0                           xor eax, eax
00A82A3E  8D 58 30                        lea ebx, [rax + 0x30]
00A82A41  8B CB                           mov ecx, ebx
00A82A43  3B C8                           cmp ecx, eax
00A82A45  72 C3                           jb 0x140a82a0a
00A82A47  8D 04 1E                        lea eax, [rsi + rbx]
00A82A4A  3B C3                           cmp eax, ebx
00A82A4C  72 BC                           jb 0x140a82a0a
00A82A4E  42 8D 0C 30                     lea ecx, [rax + r14]
00A82A52  3B C8                           cmp ecx, eax
00A82A54  72 B4                           jb 0x140a82a0a
00A82A56  8B E9                           mov ebp, ecx
00A82A58  41 B8 50 70 20 20               mov r8d, 0x20207050
00A82A5E  8B D1                           mov edx, ecx
00A82A60  B9 00 01 00 00                  mov ecx, 0x100
00A82A65  E8 86 F6 0F 00                  call 0x140b820f0
00A82A6A  48 8B F8                        mov rdi, rax
00A82A6D  48 85 C0                        test rax, rax
00A82A70  0F 84 C5 03 00 00               je 0x140a82e3b
00A82A76  44 8B C5                        mov r8d, ebp
00A82A79  33 D2                           xor edx, edx
00A82A7B  48 8B C8                        mov rcx, rax
00A82A7E  E8 BD 41 C4 FF                  call 0x1406c6c40
00A82A83  8B EB                           mov ebp, ebx
00A82A85  33 D2                           xor edx, edx
00A82A87  48 03 EF                        add rbp, rdi
00A82A8A  44 8B C6                        mov r8d, esi
00A82A8D  48 8B CD                        mov rcx, rbp
00A82A90  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
00A82A95  8B DE                           mov ebx, esi
00A82A97  E8 A4 41 C4 FF                  call 0x1406c6c40
00A82A9C  48 8D 04 2B                     lea rax, [rbx + rbp]
00A82AA0  45 8B C6                        mov r8d, r14d
00A82AA3  48 8B C8                        mov rcx, rax
00A82AA6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A82AAB  33 D2                           xor edx, edx
00A82AAD  E8 8E 41 C4 FF                  call 0x1406c6c40
00A82AB2  49 8B C7                        mov rax, r15
00A82AB5  48 8D 5F 28                     lea rbx, [rdi + 0x28]
00A82AB9  B9 01 00 00 00                  mov ecx, 1
00A82ABE  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00A82AC3  4E 8D 04 E5 00 00 00 00         lea r8, [r12*8]
00A82ACB  8B 70 04                        mov esi, dword ptr [rax + 4]
00A82ACE  83 FE FF                        cmp esi, -1
00A82AD1  8B 40 08                        mov eax, dword ptr [rax + 8]
00A82AD4  0F 44 F1                        cmove esi, ecx
00A82AD7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A82ADB  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00A82AE3  33 D2                           xor edx, edx
00A82AE5  48 83 67 10 00                  and qword ptr [rdi + 0x10], 0
00A82AEA  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
00A82AEE  48 8B CB                        mov rcx, rbx
00A82AF1  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
00A82AF8  44 89 67 20                     mov dword ptr [rdi + 0x20], r12d
00A82AFC  89 47 04                        mov dword ptr [rdi + 4], eax
00A82AFF  89 37                           mov dword ptr [rdi], esi
00A82B01  E8 3A 41 C4 FF                  call 0x1406c6c40
00A82B06  45 33 D2                        xor r10d, r10d
00A82B09  45 8B F2                        mov r14d, r10d
00A82B0C  45 8D 5A 01                     lea r11d, [r10 + 1]
00A82B10  45 2B E3                        sub r12d, r11d
00A82B13  0F 88 3B 02 00 00               js 0x140a82d54
00A82B19  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00A82B1E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00A82B23  49 8B D0                        mov rdx, r8
00A82B26  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00A82B2B  49 8B E8                        mov rbp, r8
00A82B2E  49 8D 5D 08                     lea rbx, [r13 + 8]
00A82B32  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00A82B37  45 8B 6D 04                     mov r13d, dword ptr [r13 + 4]
00A82B3B  49 83 C0 18                     add r8, 0x18
00A82B3F  48 89 10                        mov qword ptr [rax], rdx
00A82B42  48 83 C0 08                     add rax, 8
00A82B46  49 C1 E5 05                     shl r13, 5
00A82B4A  44 89 72 10                     mov dword ptr [rdx + 0x10], r14d
00A82B4E  4C 03 EB                        add r13, rbx
00A82B51  45 03 F3                        add r14d, r11d
00A82B54  48 89 7A 08                     mov qword ptr [rdx + 8], rdi
00A82B58  44 89 52 14                     mov dword ptr [rdx + 0x14], r10d
00A82B5C  80 7B 01 80                     cmp byte ptr [rbx + 1], 0x80
00A82B60  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00A82B65  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A82B6A  0F 84 67 02 00 00               je 0x140a82dd7
00A82B70  B9 00 30 00 00                  mov ecx, 0x3000
00A82B75  89 0A                           mov dword ptr [rdx], ecx
00A82B77  49 8B C0                        mov rax, r8
00A82B7A  41 8B D2                        mov edx, r10d
00A82B7D  49 3B DD                        cmp rbx, r13
00A82B80  0F 83 5A 01 00 00               jae 0x140a82ce0
00A82B86  80 7B 01 F0                     cmp byte ptr [rbx + 1], 0xf0
00A82B8A  0F 84 B5 02 00 00               je 0x140a82e45
00A82B90  44 01 5D 14                     add dword ptr [rbp + 0x14], r11d
00A82B94  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00A82B99  49 8B C9                        mov rcx, r9
00A82B9C  49 81 C1 28 01 00 00            add r9, 0x128
00A82BA3  48 89 08                        mov qword ptr [rax], rcx
00A82BA6  48 83 C0 08                     add rax, 8
00A82BAA  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A82BAF  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00A82BB3  89 51 18                        mov dword ptr [rcx + 0x18], edx
00A82BB6  41 03 D3                        add edx, r11d
00A82BB9  89 41 04                        mov dword ptr [rcx + 4], eax
00A82BBC  48 89 69 10                     mov qword ptr [rcx + 0x10], rbp
00A82BC0  48 89 49 20                     mov qword ptr [rcx + 0x20], rcx
00A82BC4  44 89 91 14 01 00 00            mov dword ptr [rcx + 0x114], r10d
00A82BCB  4C 89 91 18 01 00 00            mov qword ptr [rcx + 0x118], r10
00A82BD2  89 31                           mov dword ptr [rcx], esi
00A82BD4  8A 43 01                        mov al, byte ptr [rbx + 1]
00A82BD7  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00A82BDC  89 54 24 24                     mov dword ptr [rsp + 0x24], edx
00A82BE0  84 C0                           test al, al
00A82BE2  0F 88 85 01 00 00               js 0x140a82d6d
00A82BE8  41 8A C3                        mov al, r11b
00A82BEB  0F 84 7C 01 00 00               je 0x140a82d6d
00A82BF1  88 41 08                        mov byte ptr [rcx + 8], al
00A82BF4  48 8D 51 28                     lea rdx, [rcx + 0x28]
00A82BF8  48 89 52 08                     mov qword ptr [rdx + 8], rdx
00A82BFC  49 83 C0 08                     add r8, 8
00A82C00  48 89 12                        mov qword ptr [rdx], rdx
00A82C03  44 89 52 10                     mov dword ptr [rdx + 0x10], r10d
00A82C07  48 89 5A 18                     mov qword ptr [rdx + 0x18], rbx
00A82C0B  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00A82C10  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00A82C18  49 8B 00                        mov rax, qword ptr [r8]
00A82C1B  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
00A82C1F  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00A82C23  4C 8D 81 88 00 00 00            lea r8, [rcx + 0x88]
00A82C2A  89 42 28                        mov dword ptr [rdx + 0x28], eax
00A82C2D  4C 89 52 30                     mov qword ptr [rdx + 0x30], r10
00A82C31  89 72 38                        mov dword ptr [rdx + 0x38], esi
00A82C34  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00A82C38  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00A82C3B  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A82C3F  83 4A 58 FF                     or dword ptr [rdx + 0x58], 0xffffffff
00A82C43  89 42 40                        mov dword ptr [rdx + 0x40], eax
00A82C46  4C 89 42 48                     mov qword ptr [rdx + 0x48], r8
00A82C4A  44 89 52 2C                     mov dword ptr [rdx + 0x2c], r10d
00A82C4E  44 38 51 08                     cmp byte ptr [rcx + 8], r10b
00A82C52  0F 84 1D 01 00 00               je 0x140a82d75
00A82C58  41 C6 00 08                     mov byte ptr [r8], 8
00A82C5C  44 01 5A 10                     add dword ptr [rdx + 0x10], r11d
00A82C60  44 8B 42 10                     mov r8d, dword ptr [rdx + 0x10]
00A82C64  44 89 9C 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r11d
00A82C6C  48 83 C3 20                     add rbx, 0x20
00A82C70  49 3B DD                        cmp rbx, r13
00A82C73  73 27                           jae 0x140a82c9c
00A82C75  80 7B 01 81                     cmp byte ptr [rbx + 1], 0x81
00A82C79  0F 85 A0 00 00 00               jne 0x140a82d1f
00A82C7F  48 89 99 18 01 00 00            mov qword ptr [rcx + 0x118], rbx
00A82C86  80 7B 01 81                     cmp byte ptr [rbx + 1], 0x81
00A82C8A  75 10                           jne 0x140a82c9c
00A82C8C  44 01 99 14 01 00 00            add dword ptr [rcx + 0x114], r11d
00A82C93  48 83 C3 20                     add rbx, 0x20
00A82C97  49 3B DD                        cmp rbx, r13
00A82C9A  72 EA                           jb 0x140a82c86
00A82C9C  E8 C7 01 00 00                  call 0x140a82e68
00A82CA1  45 33 D2                        xor r10d, r10d
00A82CA4  8B F0                           mov esi, eax
00A82CA6  85 C0                           test eax, eax
00A82CA8  0F 89 86 00 00 00               jns 0x140a82d34
00A82CAE  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00A82CB3  B8 FF FF FF FF                  mov eax, 0xffffffff
00A82CB8  01 47 20                        add dword ptr [rdi + 0x20], eax
00A82CBB  48 8B CD                        mov rcx, rbp
00A82CBE  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00A82CC3  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00A82CC8  E8 E7 FA C7 FF                  call 0x1407027b4
00A82CCD  41 BB 01 00 00 00               mov r11d, 1
00A82CD3  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00A82CD7  EB 0C                           jmp 0x140a82ce5
00A82CD9  33 C0                           xor eax, eax
00A82CDB  E9 2F FD FF FF                  jmp 0x140a82a0f
00A82CE0  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A82CE5  45 2B E3                        sub r12d, r11d
00A82CE8  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
00A82CEF  41 BA 00 00 00 00               mov r10d, 0
00A82CF5  0F 89 1E FE FF FF               jns 0x140a82b19
00A82CFB  45 85 F6                        test r14d, r14d
00A82CFE  74 54                           je 0x140a82d54
00A82D00  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
00A82D04  83 BC 24 D0 00 00 00 00         cmp dword ptr [rsp + 0xd0], 0
00A82D0C  0F 84 05 0E 0C 00               je 0x140b43b17
00A82D12  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00A82D1A  48 89 38                        mov qword ptr [rax], rdi
00A82D1D  EB 47                           jmp 0x140a82d66
00A82D1F  F6 03 08                        test byte ptr [rbx], 8
00A82D22  0F 84 74 FF FF FF               je 0x140a82c9c
00A82D28  41 FF C0                        inc r8d
00A82D2B  44 89 42 10                     mov dword ptr [rdx + 0x10], r8d
00A82D2F  E9 38 FF FF FF                  jmp 0x140a82c6c
00A82D34  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
00A82D3B  41 BB 01 00 00 00               mov r11d, 1
00A82D41  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00A82D46  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A82D4B  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
00A82D4F  E9 29 FE FF FF                  jmp 0x140a82b7d
00A82D54  8B 5C 24 28                     mov ebx, dword ptr [rsp + 0x28]
00A82D58  48 8B CF                        mov rcx, rdi
00A82D5B  8B F3                           mov esi, ebx
00A82D5D  E8 4A 80 CA FF                  call 0x14072adac
00A82D62  85 DB                           test ebx, ebx
00A82D64  74 9E                           je 0x140a82d04
00A82D66  8B C6                           mov eax, esi
00A82D68  E9 A2 FC FF FF                  jmp 0x140a82a0f
00A82D6D  41 8A C2                        mov al, r10b
00A82D70  E9 7C FE FF FF                  jmp 0x140a82bf1
00A82D75  8A 43 01                        mov al, byte ptr [rbx + 1]
00A82D78  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
00A82D7C  41 88 00                        mov byte ptr [r8], al
00A82D7F  8A 43 02                        mov al, byte ptr [rbx + 2]
00A82D82  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00A82D87  88 81 89 00 00 00               mov byte ptr [rcx + 0x89], al
00A82D8D  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
00A82D91  66 89 81 8A 00 00 00            mov word ptr [rcx + 0x8a], ax
00A82D98  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A82D9B  89 81 8C 00 00 00               mov dword ptr [rcx + 0x8c], eax
00A82DA1  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
00A82DA4  89 81 90 00 00 00               mov dword ptr [rcx + 0x90], eax
00A82DAA  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A82DAD  89 81 94 00 00 00               mov dword ptr [rcx + 0x94], eax
00A82DB3  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
00A82DBA  80 7B 01 84                     cmp byte ptr [rbx + 1], 0x84
00A82DBE  41 0F 44 C3                     cmove eax, r11d
00A82DC2  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00A82DC9  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A82DCE  48 83 C3 20                     add rbx, 0x20
00A82DD2  E9 A6 FD FF FF                  jmp 0x140a82b7d
00A82DD7  48 8D 43 08                     lea rax, [rbx + 8]
00A82DDB  48 83 C3 20                     add rbx, 0x20
00A82DDF  8B 08                           mov ecx, dword ptr [rax]
00A82DE1  E9 8F FD FF FF                  jmp 0x140a82b75
00A82DE6  49 8D 48 08                     lea rcx, [r8 + 8]
00A82DEA  45 8B 40 04                     mov r8d, dword ptr [r8 + 4]
00A82DEE  49 C1 E0 05                     shl r8, 5
00A82DF2  4C 03 C1                        add r8, rcx
00A82DF5  49 3B C8                        cmp rcx, r8
00A82DF8  0F 84 DB FE FF FF               je 0x140a82cd9
00A82DFE  0F 87 09 0D 0C 00               ja 0x140b43b0d
00A82E04  48 3B CB                        cmp rcx, rbx
00A82E07  0F 87 00 0D 0C 00               ja 0x140b43b0d
00A82E0D  4C 3B C3                        cmp r8, rbx
00A82E10  0F 87 F7 0C 0C 00               ja 0x140b43b0d
00A82E16  80 79 01 80                     cmp byte ptr [rcx + 1], 0x80
00A82E1A  0F 85 74 0C 0C 00               jne 0x140b43a94
00A82E20  48 83 C1 20                     add rcx, 0x20
00A82E24  E9 6B 0C 0C 00                  jmp 0x140b43a94
00A82E29  8D 58 30                        lea ebx, [rax + 0x30]
00A82E2C  8B CB                           mov ecx, ebx
00A82E2E  3B D8                           cmp ebx, eax
00A82E30  0F 82 D4 FB FF FF               jb 0x140a82a0a
00A82E36  E9 08 FC FF FF                  jmp 0x140a82a43
00A82E3B  B8 9A 00 00 C0                  mov eax, 0xc000009a
00A82E40  E9 CA FB FF FF                  jmp 0x140a82a0f
00A82E45  8B 73 08                        mov esi, dword ptr [rbx + 8]
00A82E48  83 FE FF                        cmp esi, -1
00A82E4B  8B 4B 0C                        mov ecx, dword ptr [rbx + 0xc]
00A82E4E  41 0F 44 F3                     cmove esi, r11d
00A82E52  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00A82E56  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
00A82E5D  E9 6C FF FF FF                  jmp 0x140a82dce
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopResourceRequirementsListToReqList(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m70;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pD0;
    unsigned int v_stack_pD8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28))) == 0) goto loc_00A82CD9;
    a2 = 0;
    v_rbx = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24)))) + (*(unsigned __int64 *)(a1 + 24));
    v_rsi = 0;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28))) - ((unsigned int)(a2 + 1)));
    if (!sign_flag) goto loc_00A82DE6;
    a2 = (unsigned int)((a2) - (0));
    v_r14 = (v_r14) * ((unsigned int)((unsigned int)(a2)));
    v_stack_m90 = 0xC0000001ULL;
    if (v_r14 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A82A0A;
    if (((unsigned int)(a2)) <= ((unsigned int)(a2 + 1))) goto loc_00A82A21;
    a1 = (a2 - 1) << (3);
    result = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (a1 <= ((unsigned int)(0xFFFFFFFFULL))) { result = (unsigned int)(a1); }
    if (a1 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A82A0A;
    if (((unsigned int)(result + 32)) < ((unsigned int)(result))) goto loc_00A82A0A;
    goto loc_00A82A28;
loc_00A829F2:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28)) - 1) << (3);
    result = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (a1 <= ((unsigned int)(0xFFFFFFFFULL))) { result = (unsigned int)(a1); }
    if (a1 <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A82E29;
loc_00A82A0A:
loc_00A82A0F:
    v_rsp = (v_rsp) + (120);
    return (unsigned int)(0x80000005ULL);
loc_00A82A21:
    result = 0;
loc_00A82A28:
    if (((unsigned int)((unsigned int)((unsigned int)(result + 32)))) < 0) goto loc_00A82A0A;
    v_rsi = ((unsigned int)((unsigned int)(result + 32))) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28)));
    if (v_rsi > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A82A0A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28)))) > ((unsigned int)(a2 + 1))) goto loc_00A829F2;
    result = 0;
loc_00A82A43:
    if (((unsigned int)((unsigned int)((unsigned int)(result + 48)))) < 0) goto loc_00A82A0A;
    if (((unsigned int)(v_rsi + result + 48 * 1)) < ((unsigned int)(result + 48))) goto loc_00A82A0A;
    if (((unsigned int)(v_rsi + result + 48 * 1 + v_r14 * 1)) < ((unsigned int)(v_rsi + result + 48 * 1))) goto loc_00A82A0A;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rsi + result + 48 * 1 + v_r14 * 1)), (unsigned int)(0x20207050ULL), a4);
    if (result == 0) goto loc_00A82E3B;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi + result + 48 * 1 + v_r14 * 1)))), a4);
    a2 = 0;
    v_rbp = ((unsigned int)((unsigned int)(result + 48))) + (result);
    v_stack_p38 = v_rbp;
    result = memset(v_rbp, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    v_stack_p50 = (unsigned int)((unsigned int)(v_rsi)) + v_rbp * 1;
    a2 = 0;
    result = memset((unsigned int)((unsigned int)(v_rsi)) + v_rbp * 1, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    v_stack_p40 = result + 40;
    v_rsi = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 4)))) == -1) { v_rsi = 1; }
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 8)));
    a2 = 0;
    *(unsigned __int64 *)(result + 8) = v_stack_pC0;
    v_stack_pD8 = (unsigned int)(v_rsi);
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28)));
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 8)));
    *(unsigned int *)(result) = (unsigned int)(v_rsi);
    result = memset(result + 40, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28)) * 8, a4);
    v_r10 = 0;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 28))) - ((unsigned int)(v_r10 + 1)));
    if (sign_flag) goto loc_00A82D54;
loc_00A82B19:
    v_stack_p60 = result + 40;
    v_stack_p30 = 0;
    a3 = (v_stack_p38) + (24);
    *(unsigned __int64 *)(v_stack_p40) = v_stack_p38;
    result = (v_stack_p40) + (8);
    v_r13 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 32 + 4))) << (5);
    *(unsigned int *)(v_stack_p38 + 16) = 0;
    v_r13 = (v_r13) + (*(unsigned __int64 *)(a1 + 24) + 32 + 8);
    v_r14 = (unsigned int)((0) + ((unsigned int)(v_r10 + 1)));
    *(unsigned __int64 *)(v_stack_p38 + 8) = result;
    *(unsigned int *)(v_stack_p38 + 20) = 0;
    v_stack_p38 = a3;
    v_stack_p40 = result;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 32 + 8 + 1)) == 128) goto loc_00A82DD7;
loc_00A82B75:
    *(unsigned int *)(v_stack_p38) = (unsigned int)((unsigned int)(0x3000ULL));
loc_00A82B7D:
    if ((*(unsigned __int64 *)(a1 + 24) + 32 + 8) >= v_r13) goto loc_00A82CE0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 32 + 8 + 1)) == 240) goto loc_00A82E45;
    a4 = (v_stack_p50) + (296);
    *(unsigned __int64 *)(a3) = v_stack_p50;
    result = (a3) + (8);
    v_stack_p58 = result;
    *(unsigned int *)(v_stack_p50 + 24) = 0;
    a2 = (unsigned int)((0) + ((unsigned int)(v_r10 + 1)));
    *(unsigned int *)(v_stack_p50 + 4) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned __int64 *)(v_stack_p50 + 16) = v_stack_p38;
    *(unsigned __int64 *)(v_stack_p50 + 32) = v_stack_p50;
    *(unsigned int *)(v_stack_p50 + 276) = 0;
    *(unsigned __int64 *)(v_stack_p50 + 280) = 0;
    *(unsigned int *)(v_stack_p50) = (unsigned int)(v_rsi);
    v_stack_p50 = a4;
    v_stack_p24 = (unsigned int)(a2);
    if (sign_flag) goto loc_00A82D6D;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 32 + 8 + 1)) == 0) goto loc_00A82D6D;
loc_00A82BF1:
    *(unsigned __int8 *)(v_stack_p50 + 8) = (unsigned __int8)((unsigned __int8)(v_r10 + 1));
    *(unsigned __int64 *)(v_stack_p50 + 40 + 8) = v_stack_p50 + 40;
    a3 = (a3) + (8);
    *(unsigned __int64 *)(v_stack_p50 + 40) = v_stack_p50 + 40;
    *(unsigned int *)(v_stack_p50 + 40 + 16) = 0;
    *(unsigned __int64 *)(v_stack_p50 + 40 + 24) = *(unsigned __int64 *)(a1 + 24) + 32 + 8;
    v_stack_p38 = a3;
    *(unsigned __int64 *)(v_stack_p50 + 40 + 32) = *(unsigned __int64 *)(v_stack_pC0);
    *(unsigned int *)(v_stack_p50 + 40 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pC0 + 12)));
    *(unsigned __int64 *)(v_stack_p50 + 40 + 48) = 0;
    *(unsigned int *)(v_stack_p50 + 40 + 56) = (unsigned int)(v_rsi);
    *(unsigned int *)(v_stack_p50 + 40 + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 12)));
    *(unsigned int *)(v_stack_p50 + 40 + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 8)));
    *(unsigned __int64 *)(v_stack_p50 + 40 + 72) = v_stack_p50 + 136;
    *(unsigned int *)(v_stack_p50 + 40 + 44) = 0;
    if ((*(unsigned __int8 *)(v_stack_p50 + 8)) == 0) goto loc_00A82D75;
    *(unsigned __int8 *)(v_stack_p50 + 136) = 8;
    v_stack_pD0 = (unsigned int)(v_r10 + 1);
loc_00A82C6C:
    v_rbx = (*(unsigned __int64 *)(a1 + 24) + 32 + 8) + (32);
    if (v_rbx >= v_r13) goto loc_00A82C9C;
    if ((*(unsigned __int8 *)(v_rbx + 1)) != 129) goto loc_00A82D1F;
    *(unsigned __int64 *)(v_stack_p50 + 280) = v_rbx;
loc_00A82C86:
    if ((*(unsigned __int8 *)(v_rbx + 1)) != 129) goto loc_00A82C9C;
    v_rbx = (v_rbx) + (32);
    if (v_rbx < v_r13) goto loc_00A82C86;
loc_00A82C9C:
    result = IopSetupArbiterAndTranslators(v_stack_p50, v_stack_p50 + 40, (unsigned int)(*(unsigned int *)(v_stack_p50 + 40 + 16)), a4);
    v_r10 = 0;
    if (!sign_flag) goto loc_00A82D34;
    v_stack_p40 = v_stack_p60;
    result = IopFreeReqAlternative(v_stack_p38, v_stack_p50 + 40, (unsigned int)(*(unsigned int *)(v_stack_p50 + 40 + 16)), a4);
    v_stack_p28 = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00A82CE5;
loc_00A82CD9:
    result = 0;
    goto loc_00A82A0F;
loc_00A82CE0:
loc_00A82CE5:
    v_r12 = (unsigned int)((v_r12) - (1));
    if (!sign_flag) goto loc_00A82B19;
    if ((unsigned int)((unsigned int)(v_stack_p30)) == 0) goto loc_00A82D54;
loc_00A82D04:
    *(unsigned __int64 *)(v_stack_pC8) = 0;
    goto loc_00A82D66;
loc_00A82D1F:
    if (((*(unsigned __int8 *)(v_stack_p40)) & (8)) == 0) goto loc_00A82C9C;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 40 + 16))) + 1);
    *(unsigned int *)(v_stack_p50 + 40 + 16) = (unsigned int)(a3);
    goto loc_00A82C6C;
loc_00A82D34:
    goto loc_00A82B7D;
loc_00A82D54:
    result = IopFreeReqList(0, (unsigned int)(v_stack_p24), v_stack_p38, a4);
    if ((unsigned int)((unsigned int)(v_stack_p28)) == 0) goto loc_00A82D04;
loc_00A82D66:
    goto loc_00A82A0F;
loc_00A82D6D:
    goto loc_00A82BF1;
loc_00A82D75:
    *(unsigned __int8 *)(v_stack_p38) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_p28) + 1));
    *(unsigned __int8 *)(0 + 137) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_p28) + 2));
    *(unsigned __int16 *)(0 + 138) = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(v_stack_p28) + 4));
    *(unsigned int *)(0 + 140) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p28) + 8)));
    *(unsigned int *)(0 + 144) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p28) + 12)));
    *(unsigned int *)(0 + 148) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p28) + 16)));
    result = (unsigned int)(v_stack_pD0);
    if ((*(unsigned __int8 *)((unsigned int)(v_stack_p28) + 1)) == 132) { result = 1; }
    v_stack_pD0 = (unsigned int)(result);
loc_00A82DCE:
    v_rbx = ((unsigned int)(v_stack_p28)) + (32);
    goto loc_00A82B7D;
loc_00A82DD7:
    v_rbx = (v_rbx) + (32);
    goto loc_00A82B75;
loc_00A82DE6:
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_p38 + 4))) << (5);
    a3 = (a3) + (v_stack_p38 + 8);
    if ((v_stack_p38 + 8) == a3) goto loc_00A82CD9;
    a1 = (v_stack_p38 + 8) + (32);
loc_00A82E29:
    if (((unsigned int)(v_rbx + 8 + 48)) < ((unsigned int)(v_rbx + 8))) goto loc_00A82A0A;
    goto loc_00A82A43;
loc_00A82E3B:
    goto loc_00A82A0F;
loc_00A82E45:
    v_rsi = (unsigned int)(*(unsigned int *)(v_rbx + 8 + 48 + 8));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8 + 48 + 8)))) == -1) { v_rsi = 1; }
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8 + 48 + 12)));
    v_stack_pD8 = (unsigned int)(v_rsi);
    goto loc_00A82DCE;
}
```

## 5. (Beta) C Style

```c
int64_t IopResourceRequirementsListToReqList(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m70;
    uint32_t v_stack_m90;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pD0;
    uint32_t v_stack_pD8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C))) == 0) goto loc_00A82CD9;
    Arg2 = 0;
    local_rbx = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18)))) + (*(uint64_t *)(arg1 + 0x18));
    local_rsi = 0;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C))) - ((uint32_t)(Arg2 + 1)));
    if (!sign_flag) goto loc_00A82DE6;
    Arg2 = (uint32_t)((Arg2) - (0));
    local_r14 = (local_r14) * ((uint32_t)((uint32_t)(Arg2)));
    v_stack_m90 = 0xC0000001ULL;
    if (local_r14 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A82A0A;
    if (((uint32_t)(Arg2)) <= ((uint32_t)(Arg2 + 1))) goto loc_00A82A21;
    Arg1 = (Arg2 - 1) << (3);
    result = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (Arg1 <= ((uint32_t)(0xFFFFFFFFULL))) { result = (uint32_t)(Arg1); }
    if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A82A0A;
    if (((uint32_t)(result + 32)) < ((uint32_t)(result))) goto loc_00A82A0A;
    goto loc_00A82A28;
loc_00A829F2:
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C)) - 1) << (3);
    result = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (Arg1 <= ((uint32_t)(0xFFFFFFFFULL))) { result = (uint32_t)(Arg1); }
    if (Arg1 <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A82E29;
loc_00A82A0A:
loc_00A82A0F:
    local_rsp = (local_rsp) + (120);
    return (uint32_t)(0x80000005ULL);
loc_00A82A21:
    result = 0;
loc_00A82A28:
    if (((uint32_t)((uint32_t)((uint32_t)(result + 32)))) < 0) goto loc_00A82A0A;
    local_rsi = ((uint32_t)((uint32_t)(result + 32))) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C)));
    if (local_rsi > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A82A0A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C)))) > ((uint32_t)(Arg2 + 1))) goto loc_00A829F2;
    result = 0;
loc_00A82A43:
    if (((uint32_t)((uint32_t)((uint32_t)(result + 48)))) < 0) goto loc_00A82A0A;
    if (((uint32_t)(local_rsi + result + 48 * 1)) < ((uint32_t)(result + 48))) goto loc_00A82A0A;
    if (((uint32_t)(local_rsi + result + 48 * 1 + local_r14 * 1)) < ((uint32_t)(local_rsi + result + 48 * 1))) goto loc_00A82A0A;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rsi + result + 48 * 1 + local_r14 * 1)), (uint32_t)(0x20207050ULL), a4);
    if (result == 0) goto loc_00A82E3B;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi + result + 48 * 1 + local_r14 * 1)))), a4);
    Arg2 = 0;
    local_rbp = ((uint32_t)((uint32_t)(result + 48))) + (result);
    v_stack_p38 = local_rbp;
    result = memset(local_rbp, Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    v_stack_p50 = (uint32_t)((uint32_t)(local_rsi)) + local_rbp * 1;
    Arg2 = 0;
    result = memset((uint32_t)((uint32_t)(local_rsi)) + local_rbp * 1, Arg2, (uint32_t)((uint32_t)(local_r14)), a4);
    v_stack_p40 = result + 40;
    local_rsi = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x4)))) == -1) { local_rsi = 1; }
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)));
    Arg2 = 0;
    *(uint64_t *)(result + 0x8) = v_stack_pC0;
    v_stack_pD8 = (uint32_t)(local_rsi);
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C)));
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)));
    *(uint32_t *)(result) = (uint32_t)(local_rsi);
    result = memset(result + 40, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C)) * 8, a4);
    local_r10 = 0;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x1C))) - ((uint32_t)(local_r10 + 1)));
    if (sign_flag) goto loc_00A82D54;
loc_00A82B19:
    v_stack_p60 = result + 40;
    v_stack_p30 = 0;
    a3 = (v_stack_p38) + (24);
    *(uint64_t *)(v_stack_p40) = v_stack_p38;
    result = (v_stack_p40) + (8);
    local_r13 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20 + 0x4))) << (5);
    *(uint32_t *)(v_stack_p38 + 0x10) = 0;
    local_r13 = (local_r13) + (*(uint64_t *)(arg1 + 0x18) + 32 + 8);
    local_r14 = (uint32_t)((0) + ((uint32_t)(local_r10 + 1)));
    *(uint64_t *)(v_stack_p38 + 0x8) = result;
    *(uint32_t *)(v_stack_p38 + 0x14) = 0;
    v_stack_p38 = a3;
    v_stack_p40 = result;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20 + 0x8 + 0x1)) == 128) goto loc_00A82DD7;
loc_00A82B75:
    *(uint32_t *)(v_stack_p38) = (uint32_t)((uint32_t)(0x3000ULL));
loc_00A82B7D:
    if ((*(uint64_t *)(arg1 + 0x18) + 32 + 8) >= local_r13) goto loc_00A82CE0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20 + 0x8 + 0x1)) == 240) goto loc_00A82E45;
    a4 = (v_stack_p50) + (296);
    *(uint64_t *)(a3) = v_stack_p50;
    result = (a3) + (8);
    v_stack_p58 = result;
    *(uint32_t *)(v_stack_p50 + 0x18) = 0;
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r10 + 1)));
    *(uint32_t *)(v_stack_p50 + 0x4) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint64_t *)(v_stack_p50 + 0x10) = v_stack_p38;
    *(uint64_t *)(v_stack_p50 + 0x20) = v_stack_p50;
    *(uint32_t *)(v_stack_p50 + 0x114) = 0;
    *(uint64_t *)(v_stack_p50 + 0x118) = 0;
    *(uint32_t *)(v_stack_p50) = (uint32_t)(local_rsi);
    v_stack_p50 = a4;
    v_stack_p24 = (uint32_t)(Arg2);
    if (sign_flag) goto loc_00A82D6D;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20 + 0x8 + 0x1)) == 0) goto loc_00A82D6D;
loc_00A82BF1:
    *(uint8_t *)(v_stack_p50 + 0x8) = (uint8_t)((uint8_t)(local_r10 + 1));
    *(uint64_t *)(v_stack_p50 + 0x28 + 0x8) = v_stack_p50 + 40;
    a3 = (a3) + (8);
    *(uint64_t *)(v_stack_p50 + 0x28) = v_stack_p50 + 40;
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x10) = 0;
    *(uint64_t *)(v_stack_p50 + 0x28 + 0x18) = *(uint64_t *)(arg1 + 0x18) + 32 + 8;
    v_stack_p38 = a3;
    *(uint64_t *)(v_stack_p50 + 0x28 + 0x20) = *(uint64_t *)(v_stack_pC0);
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pC0 + 0xC)));
    *(uint64_t *)(v_stack_p50 + 0x28 + 0x30) = 0;
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x38) = (uint32_t)(local_rsi);
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0xC)));
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)));
    *(uint64_t *)(v_stack_p50 + 0x28 + 0x48) = v_stack_p50 + 136;
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x2C) = 0;
    if ((*(uint8_t *)(v_stack_p50 + 0x8)) == 0) goto loc_00A82D75;
    *(uint8_t *)(v_stack_p50 + 0x88) = 8;
    v_stack_pD0 = (uint32_t)(local_r10 + 1);
loc_00A82C6C:
    local_rbx = (*(uint64_t *)(arg1 + 0x18) + 32 + 8) + (32);
    if (local_rbx >= local_r13) goto loc_00A82C9C;
    if ((*(uint8_t *)(local_rbx + 0x1)) != 129) goto loc_00A82D1F;
    *(uint64_t *)(v_stack_p50 + 0x118) = local_rbx;
loc_00A82C86:
    if ((*(uint8_t *)(local_rbx + 0x1)) != 129) goto loc_00A82C9C;
    local_rbx = (local_rbx) + (32);
    if (local_rbx < local_r13) goto loc_00A82C86;
loc_00A82C9C:
    result = IopSetupArbiterAndTranslators(v_stack_p50, v_stack_p50 + 40, (uint32_t)(*(uint32_t *)(v_stack_p50 + 0x28 + 0x10)), a4);
    local_r10 = 0;
    if (!sign_flag) goto loc_00A82D34;
    v_stack_p40 = v_stack_p60;
    result = IopFreeReqAlternative(v_stack_p38, v_stack_p50 + 40, (uint32_t)(*(uint32_t *)(v_stack_p50 + 0x28 + 0x10)), a4);
    v_stack_p28 = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00A82CE5;
loc_00A82CD9:
    result = 0;
    goto loc_00A82A0F;
loc_00A82CE0:
loc_00A82CE5:
    local_r12 = (uint32_t)((local_r12) - (1));
    if (!sign_flag) goto loc_00A82B19;
    if ((uint32_t)((uint32_t)(v_stack_p30)) == 0) goto loc_00A82D54;
loc_00A82D04:
    *(uint64_t *)(v_stack_pC8) = 0;
    goto loc_00A82D66;
loc_00A82D1F:
    if (((*(uint8_t *)(v_stack_p40)) & (8)) == 0) goto loc_00A82C9C;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x28 + 0x10))) + 1);
    *(uint32_t *)(v_stack_p50 + 0x28 + 0x10) = (uint32_t)(a3);
    goto loc_00A82C6C;
loc_00A82D34:
    goto loc_00A82B7D;
loc_00A82D54:
    result = IopFreeReqList(0, (uint32_t)(v_stack_p24), v_stack_p38, a4);
    if ((uint32_t)((uint32_t)(v_stack_p28)) == 0) goto loc_00A82D04;
loc_00A82D66:
    goto loc_00A82A0F;
loc_00A82D6D:
    goto loc_00A82BF1;
loc_00A82D75:
    *(uint8_t *)(v_stack_p38) = (uint8_t)(*(uint8_t *)((uint32_t)(v_stack_p28) + 0x1));
    *(uint8_t *)(0 + 0x89) = (uint8_t)(*(uint8_t *)((uint32_t)(v_stack_p28) + 0x2));
    *(uint16_t *)(0 + 0x8A) = (uint16_t)(*(uint16_t *)((uint32_t)(v_stack_p28) + 0x4));
    *(uint32_t *)(0 + 0x8C) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p28) + 0x8)));
    *(uint32_t *)(0 + 0x90) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p28) + 0xC)));
    *(uint32_t *)(0 + 0x94) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p28) + 0x10)));
    result = (uint32_t)(v_stack_pD0);
    if ((*(uint8_t *)((uint32_t)(v_stack_p28) + 0x1)) == 132) { result = 1; }
    v_stack_pD0 = (uint32_t)(result);
loc_00A82DCE:
    local_rbx = ((uint32_t)(v_stack_p28)) + (32);
    goto loc_00A82B7D;
loc_00A82DD7:
    local_rbx = (local_rbx) + (32);
    goto loc_00A82B75;
loc_00A82DE6:
    a3 = ((uint32_t)(*(uint32_t *)(v_stack_p38 + 0x4))) << (5);
    a3 = (a3) + (v_stack_p38 + 8);
    if ((v_stack_p38 + 8) == a3) goto loc_00A82CD9;
    Arg1 = (v_stack_p38 + 8) + (32);
loc_00A82E29:
    if (((uint32_t)(local_rbx + 8 + 48)) < ((uint32_t)(local_rbx + 8))) goto loc_00A82A0A;
    goto loc_00A82A43;
loc_00A82E3B:
    goto loc_00A82A0F;
loc_00A82E45:
    local_rsi = (uint32_t)(*(uint32_t *)(local_rbx + 0x8 + 0x30 + 0x8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8 + 0x30 + 0x8)))) == -1) { local_rsi = 1; }
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8 + 0x30 + 0xC)));
    v_stack_pD8 = (uint32_t)(local_rsi);
    goto loc_00A82DCE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A82954&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
