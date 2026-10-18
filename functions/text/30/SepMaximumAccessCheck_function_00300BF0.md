# SepMaximumAccessCheck

- RVA: `0x00300BF0`–`0x0030110E` (길이 `1,310` bytes)
- VA: `0x0000000140300BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000730C0`
- 디코드: `310`개 명령, `1,310/1,310` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00300C92` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00300CB4` → [SepIsPackageSid](SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x00300CFC` → [SepMatchPackage](../2F/SepMatchPackage_function_002FFDC0.md) (function, `0x002FFDC0`)
- `0x00300D7D` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00300DC6` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00300E24` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00300ECC` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00300F62` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00300F72` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00300F9E` → [SepIsPackageSid](SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x00300FAE` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x00301035` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x00301062` → [SepMatchCapability](../3D/SepMatchCapability_function_003D0C70.md) (function, `0x003D0C70`)
- `0x0030107C` → [SepIsPackageSid](SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x0030108C` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003010C6` → [AuthzBasepAddAccessTypeList](../3D/AuthzBasepAddAccessTypeList_function_003D196C.md) (function, `0x003D196C`)
- `0x003010F8` → [AuthzBasepInitializeResourceClaimsFromSacl](AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)

### Direct callers
- [SepAccessCheck](../3D/SepAccessCheck_function_003D0E54.md) at `0x003D1196`
- [SepAccessCheck](../3D/SepAccessCheck_function_003D0E54.md) at `0x003D150B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x00300D94` → [sub_006E0188 + 0x45](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300DEF` → [sub_006E0188 + 0x4D](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300E5D` → [sub_006E0188 + 0x13F](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300EDD` → [sub_006E0188 + 0x3D](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300F80` → [sub_006E0188 + 0x213](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300F88` → [sub_006E0188 + 0x1DF](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300F91` → [sub_006E0188 + 0x1DF](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300FA5` → [sub_006E0188](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300FB5` → [sub_006E0188 + 0x35](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00300FC3` → [sub_006E0188 + 0x1DF](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00301083` → [sub_006E0188](../6E/Unknown_function_006E0188.md) (`tail-transfer`)
  - `0x00301093` → [sub_006E0188 + 0x35](../6E/Unknown_function_006E0188.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00300BF0  48 8B C4                        mov rax, rsp
00300BF3  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00300BF7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00300BFB  53                              push rbx
00300BFC  55                              push rbp
00300BFD  56                              push rsi
00300BFE  57                              push rdi
00300BFF  41 54                           push r12
00300C01  41 55                           push r13
00300C03  41 56                           push r14
00300C05  41 57                           push r15
00300C07  48 83 EC 78                     sub rsp, 0x78
00300C0B  83 60 18 00                     and dword ptr [rax + 0x18], 0
00300C0F  4C 8B E9                        mov r13, rcx
00300C12  8B 99 C8 00 00 00               mov ebx, dword ptr [rcx + 0xc8]
00300C18  8B C3                           mov eax, ebx
00300C1A  83 4C 24 64 FF                  or dword ptr [rsp + 0x64], 0xffffffff
00300C1F  25 00 40 00 00                  and eax, 0x4000
00300C24  44 8A A4 24 10 01 00 00         mov r12b, byte ptr [rsp + 0x110]
00300C2C  81 E3 00 20 00 00               and ebx, 0x2000
00300C32  48 8B B4 24 F8 00 00 00         mov rsi, qword ptr [rsp + 0xf8]
00300C3A  44 8B B4 24 F0 00 00 00         mov r14d, dword ptr [rsp + 0xf0]
00300C42  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00300C46  89 9C 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], ebx
00300C4D  45 84 E4                        test r12b, r12b
00300C50  0F 85 72 03 00 00               jne 0x140300fc8
00300C56  41 0F B7 40 04                  movzx eax, word ptr [r8 + 4]
00300C5B  49 8D 78 08                     lea rdi, [r8 + 8]
00300C5F  45 33 FF                        xor r15d, r15d
00300C62  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00300C66  44 89 BC 24 10 01 00 00         mov dword ptr [rsp + 0x110], r15d
00300C6E  85 C0                           test eax, eax
00300C70  0F 84 C2 00 00 00               je 0x140300d38
00300C76  48 8B AC 24 20 01 00 00         mov rbp, qword ptr [rsp + 0x120]
00300C7E  F6 47 01 08                     test byte ptr [rdi + 1], 8
00300C82  0F 85 8F 00 00 00               jne 0x140300d17
00300C88  8A 07                           mov al, byte ptr [rdi]
00300C8A  84 C0                           test al, al
00300C8C  0F 85 5B 01 00 00               jne 0x140300ded
00300C92  E8 F1 EA 1E 00                  call 0x1404ef788
00300C97  85 C0                           test eax, eax
00300C99  0F 84 B4 00 00 00               je 0x140300d53
00300C9F  85 DB                           test ebx, ebx
00300CA1  0F 85 F2 00 00 00               jne 0x140300d99
00300CA7  45 84 E4                        test r12b, r12b
00300CAA  0F 85 70 03 00 00               jne 0x140301020
00300CB0  48 8D 4F 08                     lea rcx, [rdi + 8]
00300CB4  E8 67 04 00 00                  call 0x140301120
00300CB9  84 C0                           test al, al
00300CBB  0F 84 5F 03 00 00               je 0x140301020
00300CC1  48 8D 45 18                     lea rax, [rbp + 0x18]
00300CC5  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00300CCA  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00300CCE  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00300CD3  48 8D 55 14                     lea rdx, [rbp + 0x14]
00300CD7  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00300CDC  48 8D 5D 04                     lea rbx, [rbp + 4]
00300CE0  4C 8D 4D 15                     lea r9, [rbp + 0x15]
00300CE4  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00300CE9  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00300CEE  4C 8D 47 08                     lea r8, [rdi + 8]
00300CF2  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
00300CF6  83 CA FF                        or edx, 0xffffffff
00300CF9  49 8B CD                        mov rcx, r13
00300CFC  E8 BF F0 FF FF                  call 0x1402ffdc0
00300D01  8B 03                           mov eax, dword ptr [rbx]
00300D03  F7 D0                           not eax
00300D05  21 45 00                        and dword ptr [rbp], eax
00300D08  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00300D0F  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
00300D17  FF 84 24 10 01 00 00            inc dword ptr [rsp + 0x110]
00300D1E  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00300D22  44 8B BC 24 10 01 00 00         mov r15d, dword ptr [rsp + 0x110]
00300D2A  48 03 F8                        add rdi, rax
00300D2D  44 3B 7C 24 68                  cmp r15d, dword ptr [rsp + 0x68]
00300D32  0F 82 46 FF FF FF               jb 0x140300c7e
00300D38  45 84 E4                        test r12b, r12b
00300D3B  0F 85 AE 02 00 00               jne 0x140300fef
00300D41  48 83 C4 78                     add rsp, 0x78
00300D45  41 5F                           pop r15
00300D47  41 5E                           pop r14
00300D49  41 5D                           pop r13
00300D4B  41 5C                           pop r12
00300D4D  5F                              pop rdi
00300D4E  5E                              pop rsi
00300D4F  5D                              pop rbp
00300D50  5B                              pop rbx
00300D51  C3                              ret
00300D52  CC                              int3
00300D53  85 DB                           test ebx, ebx
00300D55  0F 84 11 03 00 00               je 0x14030106c
00300D5B  4C 8D 47 08                     lea r8, [rdi + 8]
00300D5F  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00300D66  49 8B CD                        mov rcx, r13
00300D69  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00300D71  45 33 C9                        xor r9d, r9d
00300D74  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00300D78  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00300D7D  E8 AE F6 0C 00                  call 0x1403d0430
00300D82  84 C0                           test al, al
00300D84  74 89                           je 0x140300d0f
00300D86  41 83 FE 01                     cmp r14d, 1
00300D8A  74 51                           je 0x140300ddd
00300D8C  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00300D94  E9 34 F4 3D 00                  jmp 0x1406e01cd
00300D99  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
00300D9E  0F 85 03 FF FF FF               jne 0x140300ca7
00300DA4  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00300DAB  4C 8D 47 08                     lea r8, [rdi + 8]
00300DAF  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00300DB7  45 33 C9                        xor r9d, r9d
00300DBA  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00300DBE  49 8B CD                        mov rcx, r13
00300DC1  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00300DC6  E8 65 F6 0C 00                  call 0x1403d0430
00300DCB  84 C0                           test al, al
00300DCD  0F 84 3C FF FF FF               je 0x140300d0f
00300DD3  41 83 FE 01                     cmp r14d, 1
00300DD7  0F 85 C9 02 00 00               jne 0x1403010a6
00300DDD  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00300DE0  F7 D0                           not eax
00300DE2  23 47 04                        and eax, dword ptr [rdi + 4]
00300DE5  09 46 1C                        or dword ptr [rsi + 0x1c], eax
00300DE8  E9 22 FF FF FF                  jmp 0x140300d0f
00300DED  3C 05                           cmp al, 5
00300DEF  0F 84 E0 F3 3D 00               je 0x1406e01d5
00300DF5  3C 04                           cmp al, 4
00300DF7  75 5E                           jne 0x140300e57
00300DF9  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00300E00  45 33 C9                        xor r9d, r9d
00300E03  44 0F B6 47 0D                  movzx r8d, byte ptr [rdi + 0xd]
00300E08  49 8B CD                        mov rcx, r13
00300E0B  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00300E13  49 83 C0 05                     add r8, 5
00300E17  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00300E1B  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00300E20  4E 8D 04 87                     lea r8, [rdi + r8*4]
00300E24  E8 07 F6 0C 00                  call 0x1403d0430
00300E29  84 C0                           test al, al
00300E2B  0F 84 DE FE FF FF               je 0x140300d0f
00300E31  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00300E38  4C 8D 47 0C                     lea r8, [rdi + 0xc]
00300E3C  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00300E44  45 33 C9                        xor r9d, r9d
00300E47  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00300E4B  33 D2                           xor edx, edx
00300E4D  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00300E52  E9 26 FF FF FF                  jmp 0x140300d7d
00300E57  3C 01                           cmp al, 1
00300E59  74 4F                           je 0x140300eaa
00300E5B  3C 06                           cmp al, 6
00300E5D  0F 84 64 F4 3D 00               je 0x1406e02c7
00300E63  3C 09                           cmp al, 9
00300E65  0F 85 AC FE FF FF               jne 0x140300d17
00300E6B  0F B6 47 09                     movzx eax, byte ptr [rdi + 9]
00300E6F  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
00300E76  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00300E7A  2B C3                           sub eax, ebx
00300E7C  83 E8 08                        sub eax, 8
00300E7F  85 C0                           test eax, eax
00300E81  0F 8E 7B 02 00 00               jle 0x140301102
00300E87  4D 85 C9                        test r9, r9
00300E8A  0F 85 50 02 00 00               jne 0x1403010e0
00300E90  49 8B 85 48 04 00 00            mov rax, qword ptr [r13 + 0x448]
00300E97  48 85 C0                        test rax, rax
00300E9A  75 57                           jne 0x140300ef3
00300E9C  45 33 C9                        xor r9d, r9d
00300E9F  45 33 C0                        xor r8d, r8d
00300EA2  45 33 D2                        xor r10d, r10d
00300EA5  45 33 DB                        xor r11d, r11d
00300EA8  EB 65                           jmp 0x140300f0f
00300EAA  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00300EB1  4C 8D 47 08                     lea r8, [rdi + 8]
00300EB5  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00300EBD  41 B1 01                        mov r9b, 1
00300EC0  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00300EC4  49 8B CD                        mov rcx, r13
00300EC7  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00300ECC  E8 5F F5 0C 00                  call 0x1403d0430
00300ED1  84 C0                           test al, al
00300ED3  0F 84 36 FE FF FF               je 0x140300d0f
00300ED9  41 83 FE 01                     cmp r14d, 1
00300EDD  0F 85 E2 F2 3D 00               jne 0x1406e01c5
00300EE3  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
00300EE6  F7 D0                           not eax
00300EE8  23 47 04                        and eax, dword ptr [rdi + 4]
00300EEB  09 46 20                        or dword ptr [rsi + 0x20], eax
00300EEE  E9 1C FE FF FF                  jmp 0x140300d0f
00300EF3  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00300EFA  4C 8B 80 50 02 00 00            mov r8, qword ptr [rax + 0x250]
00300F01  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
00300F08  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
00300F0F  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
00300F13  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00300F18  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00300F1D  2B D3                           sub edx, ebx
00300F1F  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00300F27  83 EA 08                        sub edx, 8
00300F2A  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
00300F2F  C6 44 24 48 00                  mov byte ptr [rsp + 0x48], 0
00300F34  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00300F38  49 8B 95 08 03 00 00            mov rdx, qword ptr [r13 + 0x308]
00300F3F  8B CB                           mov ecx, ebx
00300F41  48 83 C1 08                     add rcx, 8
00300F45  48 03 CF                        add rcx, rdi
00300F48  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00300F4D  49 8B CD                        mov rcx, r13
00300F50  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00300F55  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
00300F5A  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00300F5F  4C 8B 00                        mov r8, qword ptr [rax]
00300F62  E8 69 DC FF FF                  call 0x1402febd0
00300F67  83 7C 24 64 01                  cmp dword ptr [rsp + 0x64], 1
00300F6C  0F 85 96 FD FF FF               jne 0x140300d08
00300F72  E8 11 E8 1E 00                  call 0x1404ef788
00300F77  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00300F7E  85 C0                           test eax, eax
00300F80  0F 85 15 F4 3D 00               jne 0x1406e039b
00300F86  85 DB                           test ebx, ebx
00300F88  0F 85 D9 F3 3D 00               jne 0x1406e0367
00300F8E  45 84 E4                        test r12b, r12b
00300F91  0F 85 D0 F3 3D 00               jne 0x1406e0367
00300F97  4C 8D 7F 08                     lea r15, [rdi + 8]
00300F9B  49 8B CF                        mov rcx, r15
00300F9E  E8 7D 01 00 00                  call 0x140301120
00300FA3  84 C0                           test al, al
00300FA5  0F 85 DD F1 3D 00               jne 0x1406e0188
00300FAB  49 8B CF                        mov rcx, r15
00300FAE  E8 3D FE 0C 00                  call 0x1403d0df0
00300FB3  84 C0                           test al, al
00300FB5  0F 85 02 F2 3D 00               jne 0x1406e01bd
00300FBB  44 8B BC 24 10 01 00 00         mov r15d, dword ptr [rsp + 0x110]
00300FC3  E9 9F F3 3D 00                  jmp 0x1406e0367
00300FC8  45 85 F6                        test r14d, r14d
00300FCB  0F 84 85 FC FF FF               je 0x140300c56
00300FD1  48 8D 4E 1C                     lea rcx, [rsi + 0x1c]
00300FD5  49 8B D6                        mov rdx, r14
00300FD8  8B 01                           mov eax, dword ptr [rcx]
00300FDA  83 21 00                        and dword ptr [rcx], 0
00300FDD  89 41 FC                        mov dword ptr [rcx - 4], eax
00300FE0  48 8D 49 30                     lea rcx, [rcx + 0x30]
00300FE4  48 83 EA 01                     sub rdx, 1
00300FE8  75 EE                           jne 0x140300fd8
00300FEA  E9 67 FC FF FF                  jmp 0x140300c56
00300FEF  45 85 F6                        test r14d, r14d
00300FF2  0F 84 49 FD FF FF               je 0x140300d41
00300FF8  8B 8C 24 08 01 00 00            mov ecx, dword ptr [rsp + 0x108]
00300FFF  48 83 C6 1C                     add rsi, 0x1c
00301003  F7 D1                           not ecx
00301005  49 8B D6                        mov rdx, r14
00301008  8B C1                           mov eax, ecx
0030100A  0B 06                           or eax, dword ptr [rsi]
0030100C  23 46 FC                        and eax, dword ptr [rsi - 4]
0030100F  89 06                           mov dword ptr [rsi], eax
00301011  48 8D 76 30                     lea rsi, [rsi + 0x30]
00301015  48 83 EA 01                     sub rdx, 1
00301019  75 ED                           jne 0x140301008
0030101B  E9 21 FD FF FF                  jmp 0x140300d41
00301020  85 DB                           test ebx, ebx
00301022  0F 85 A8 00 00 00               jne 0x1403010d0
00301028  45 84 E4                        test r12b, r12b
0030102B  0F 85 73 FD FF FF               jne 0x140300da4
00301031  48 8D 4F 08                     lea rcx, [rdi + 8]
00301035  E8 B6 FD 0C 00                  call 0x1403d0df0
0030103A  84 C0                           test al, al
0030103C  0F 84 62 FD FF FF               je 0x140300da4
00301042  4C 8D 47 08                     lea r8, [rdi + 8]
00301046  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
0030104A  48 8D 45 16                     lea rax, [rbp + 0x16]
0030104E  48 8D 5D 08                     lea rbx, [rbp + 8]
00301052  83 CA FF                        or edx, 0xffffffff
00301055  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0030105A  49 8B CD                        mov rcx, r13
0030105D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00301062  E8 09 FC 0C 00                  call 0x1403d0c70
00301067  E9 95 FC FF FF                  jmp 0x140300d01
0030106C  45 84 E4                        test r12b, r12b
0030106F  0F 85 E6 FC FF FF               jne 0x140300d5b
00301075  4C 8D 7F 08                     lea r15, [rdi + 8]
00301079  49 8B CF                        mov rcx, r15
0030107C  E8 9F 00 00 00                  call 0x140301120
00301081  84 C0                           test al, al
00301083  0F 85 FF F0 3D 00               jne 0x1406e0188
00301089  49 8B CF                        mov rcx, r15
0030108C  E8 5F FD 0C 00                  call 0x1403d0df0
00301091  84 C0                           test al, al
00301093  0F 85 24 F1 3D 00               jne 0x1406e01bd
00301099  44 8B BC 24 10 01 00 00         mov r15d, dword ptr [rsp + 0x110]
003010A1  E9 B5 FC FF FF                  jmp 0x140300d5b
003010A6  44 8B 8C 24 10 01 00 00         mov r9d, dword ptr [rsp + 0x110]
003010AE  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
003010B6  8B 47 04                        mov eax, dword ptr [rdi + 4]
003010B9  45 33 C0                        xor r8d, r8d
003010BC  41 8B D6                        mov edx, r14d
003010BF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003010C3  48 8B CE                        mov rcx, rsi
003010C6  E8 A1 08 0D 00                  call 0x1403d196c
003010CB  E9 3F FC FF FF                  jmp 0x140300d0f
003010D0  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
003010D5  0F 84 C9 FC FF FF               je 0x140300da4
003010DB  E9 48 FF FF FF                  jmp 0x140301028
003010E0  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
003010E8  48 83 38 00                     cmp qword ptr [rax], 0
003010EC  0F 85 9E FD FF FF               jne 0x140300e90
003010F2  48 8B D0                        mov rdx, rax
003010F5  49 8B C9                        mov rcx, r9
003010F8  E8 87 1D 00 00                  call 0x140302e84
003010FD  E9 8E FD FF FF                  jmp 0x140300e90
00301102  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00301109  E9 09 FC FF FF                  jmp 0x140300d17
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepMaximumAccessCheck(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, unsigned int a10, unsigned __int8 a11, unsigned __int8 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned int v_stack_p8;
    unsigned int v_stack_pC0;
    unsigned __int64 v_stack_pC8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (120);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 200))))) & (0x4000ULL));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) & (0x2000ULL));
    v_stack_m58 = (unsigned int)(result);
    v_stack_p8 = (unsigned int)(v_rbx);
    if (a11 != 0) goto loc_00300FC8;
loc_00300C56:
    v_r15 = 0;
    v_stack_m50 = (unsigned int)(*(unsigned __int16 *)(a3 + 4));
    v_stack_p58 = 0;
    if ((unsigned int)(*(unsigned __int16 *)(a3 + 4)) == 0) goto loc_00300D38;
loc_00300C7E:
    if (((*(unsigned __int8 *)(a3 + 8 + 1)) & (8)) != 0) goto loc_00300D17;
    if ((unsigned __int8)(*(unsigned __int8 *)(a3 + 8)) != 0) goto loc_00300DED;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00300D53;
    if ((unsigned int)(v_rbx) != 0) goto loc_00300D99;
loc_00300CA7:
    if (a11 != 0) goto loc_00301020;
    result = SepIsPackageSid(a3 + 8 + 8, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00301020;
    v_stack_m78 = a13 + 24;
    v_stack_m80 = a13 + 16;
    v_stack_m88 = a13 + 20;
    v_stack_m90 = a13 + 4;
    v_stack_m98 = a13 + 21;
    a2 = (unsigned int)((a13 + 20) | (0xFFFFFFFFULL));
    result = SepMatchPackage(a1, a2, a3 + 8 + 8, (unsigned int)(*(unsigned int *)(a3 + 8 + 4)));
loc_00300D01:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a13 + 4))));
loc_00300D08:
loc_00300D0F:
loc_00300D17:
    v_rdi = (a3 + 8) + (*(unsigned __int16 *)(a3 + 8 + 2));
    if (((unsigned int)((unsigned int)(a11))) < v_stack_m50) goto loc_00300C7E;
loc_00300D38:
    if (a11 != 0) goto loc_00300FEF;
loc_00300D41:
    v_rsp = (v_rsp) + (120);
    return *(unsigned __int16 *)(a3 + 8 + 2);
loc_00300D53:
    if ((unsigned int)((unsigned int)(v_stack_p8)) == 0) goto loc_0030106C;
loc_00300D5B:
    a4 = 0;
    v_stack_p28 = a12;
    v_stack_p20 = a11;
loc_00300D7D:
    result = SepSidInToken(a1, a6, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00300D0F;
    if (((unsigned int)((unsigned int)(a7))) == 1) goto loc_00300DDD;
    v_stack_p28 = 1;
loc_00300D99:
    if (v_stack_p60 != 0) goto loc_00300CA7;
loc_00300DA4:
    a4 = 0;
    v_stack_p28 = a12;
    v_stack_p20 = a11;
    result = SepSidInToken(a1, a6, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00300D0F;
    if (((unsigned int)((unsigned int)(a7))) != 1) goto loc_003010A6;
loc_00300DDD:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a8 + 32))));
    result = (unsigned int)((result) & (*(unsigned int *)(v_rdi + 4)));
    goto loc_00300D0F;
loc_00300DED:
    if (((unsigned __int8)(result)) != 4) goto loc_00300E57;
    a4 = 0;
    a3 = (*(unsigned __int8 *)(v_rdi + 13)) + (5);
    v_stack_p28 = a12;
    v_stack_p20 = a11;
    result = SepSidInToken(a1, a6, v_rdi + a3 * 4, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00300D0F;
    a4 = 0;
    v_stack_p28 = a12;
    a2 = 0;
    v_stack_p20 = 0;
    goto loc_00300D7D;
loc_00300E57:
    if (a12 == 1) goto loc_00300EAA;
    if (a12 != 9) goto loc_00300D17;
    result = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    result = (unsigned int)((result) - (8));
    if (condition_is_less_or_equal) goto loc_00301102;
    if (0 != 0) goto loc_003010E0;
loc_00300E90:
    if (*(unsigned __int64 *)(a1 + 1096) != 0) goto loc_00300EF3;
    a4 = 0;
    a3 = 0;
    v_r10 = 0;
    v_r11 = 0;
    goto loc_00300F0F;
loc_00300EAA:
    v_stack_p28 = a12;
    v_stack_p20 = a11;
    result = SepSidInToken(a1, a6, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00300D0F;
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a8 + 28))));
    result = (unsigned int)((result) & (*(unsigned int *)(v_rdi + 4)));
    goto loc_00300D0F;
loc_00300EF3:
loc_00300F0F:
    v_stack_p58 = v_stack_p64;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    a2 = (unsigned int)((a2) - (8));
    v_stack_p50 = a11;
    v_stack_p48 = 0;
    v_stack_p40 = (unsigned int)(a2);
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8))) + (8);
    a1 = (a1) + (v_rdi);
    v_stack_p38 = a1;
    v_stack_p30 = *(unsigned __int64 *)(result + 600);
    v_stack_p28 = *(unsigned __int64 *)(result + 584);
    v_stack_p20 = *(unsigned __int64 *)(result + 592);
    result = AuthzBasepEvaluateAceCondition(a1, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), *(unsigned __int64 *)(result + 576));
    if (v_stack_p64 != 1) goto loc_00300D08;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), *(unsigned __int64 *)(result + 576));
    result = SepIsPackageSid(v_rdi + 8, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), *(unsigned __int64 *)(result + 576));
    result = SepIsCapabilitySid(v_rdi + 8, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), *(unsigned __int64 *)(result + 576));
loc_00300FC8:
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_00300C56;
loc_00300FD8:
    *(unsigned int *)(a8 + 28 - 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 28)));
    a2 = ((unsigned int)(a7)) - (1);
    if (condition_is_not_equal) goto loc_00300FD8;
    goto loc_00300C56;
loc_00300FEF:
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_00300D41;
    v_rsi = (a8) + (28);
    a1 = (unsigned int)(~((unsigned int)(a10)));
loc_00301008:
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (*(unsigned int *)(v_rsi)));
    result = (unsigned int)((result) & (*(unsigned int *)(v_rsi - 4)));
    *(unsigned int *)(v_rsi) = (unsigned int)(result);
    a2 = ((unsigned int)(a7)) - (1);
    if (condition_is_not_equal) goto loc_00301008;
    goto loc_00300D41;
loc_00301020:
    if ((unsigned int)((unsigned int)(v_stack_pC0)) != 0) goto loc_003010D0;
loc_00301028:
    if (a11 != 0) goto loc_00300DA4;
    result = SepIsCapabilitySid(v_rdi + 8, a2, *(unsigned __int64 *)(a5), *(unsigned __int64 *)(result + 576));
    if ((unsigned __int8)(result) == 0) goto loc_00300DA4;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_p28 = a13 + 8;
    v_stack_p20 = a13 + 22;
    result = SepMatchCapability(a1, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    goto loc_00300D01;
loc_0030106C:
    if (a11 != 0) goto loc_00300D5B;
    result = SepIsPackageSid(v_rdi + 8, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = SepIsCapabilitySid(v_rdi + 8, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    goto loc_00300D5B;
loc_003010A6:
    v_stack_p28 = 1;
    a3 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = AuthzBasepAddAccessTypeList(v_rsi + 48, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, (unsigned int)(a11));
    goto loc_00300D0F;
loc_003010D0:
    if (v_stack_p60 == 0) goto loc_00300DA4;
    goto loc_00301028;
loc_003010E0:
    if ((*(unsigned __int64 *)(a5)) != 0) goto loc_00300E90;
    result = AuthzBasepInitializeResourceClaimsFromSacl((unsigned int)(a11), a5, a3, (unsigned int)(a11));
    goto loc_00300E90;
loc_00301102:
    goto loc_00300D17;
}
```

## 5. (Beta) C Style

```c
int64_t SepMaximumAccessCheck(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8, uint64_t Arg9, uint32_t Arg10, uint8_t Arg11, uint8_t Arg12, void *Arg13)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint8_t v_stack_p48;
    uint8_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p64;
    uint32_t v_stack_p8;
    uint32_t v_stack_pC0;
    uint64_t v_stack_pC8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (120);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8))))) & (0x4000ULL));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) & (0x2000ULL));
    v_stack_m58 = (uint32_t)(result);
    v_stack_p8 = (uint32_t)(local_rbx);
    if (Arg11 != 0) goto loc_00300FC8;
loc_00300C56:
    local_r15 = 0;
    v_stack_m50 = (uint32_t)(*(uint16_t *)(arg3 + 0x4));
    v_stack_p58 = 0;
    if ((uint32_t)(*(uint16_t *)(arg3 + 0x4)) == 0) goto loc_00300D38;
loc_00300C7E:
    if (((*(uint8_t *)(arg3 + 0x8 + 0x1)) & (8)) != 0) goto loc_00300D17;
    if ((uint8_t)(*(uint8_t *)(arg3 + 0x8)) != 0) goto loc_00300DED;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00300D53;
    if ((uint32_t)(local_rbx) != 0) goto loc_00300D99;
loc_00300CA7:
    if (Arg11 != 0) goto loc_00301020;
    result = SepIsPackageSid(Arg3 + 8 + 8, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00301020;
    v_stack_m78 = Arg13 + 24;
    v_stack_m80 = Arg13 + 16;
    v_stack_m88 = Arg13 + 20;
    v_stack_m90 = Arg13 + 4;
    v_stack_m98 = Arg13 + 21;
    Arg2 = (uint32_t)((Arg13 + 20) | (0xFFFFFFFFULL));
    result = SepMatchPackage(Arg1, Arg2, Arg3 + 8 + 8, (uint32_t)(*(uint32_t *)(arg3 + 0x8 + 0x4)));
loc_00300D01:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg13 + 0x4))));
loc_00300D08:
loc_00300D0F:
loc_00300D17:
    local_rdi = (Arg3 + 8) + (*(uint16_t *)(arg3 + 0x8 + 0x2));
    if (((uint32_t)((uint32_t)(Arg11))) < v_stack_m50) goto loc_00300C7E;
loc_00300D38:
    if (Arg11 != 0) goto loc_00300FEF;
loc_00300D41:
    local_rsp = (local_rsp) + (120);
    return *(uint16_t *)(arg3 + 0x8 + 0x2);
loc_00300D53:
    if ((uint32_t)((uint32_t)(v_stack_p8)) == 0) goto loc_0030106C;
loc_00300D5B:
    Arg4 = 0;
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
loc_00300D7D:
    result = SepSidInToken(Arg1, Arg6, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00300D0F;
    if (((uint32_t)((uint32_t)(Arg7))) == 1) goto loc_00300DDD;
    v_stack_p28 = 1;
loc_00300D99:
    if (v_stack_p60 != 0) goto loc_00300CA7;
loc_00300DA4:
    Arg4 = 0;
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
    result = SepSidInToken(Arg1, Arg6, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00300D0F;
    if (((uint32_t)((uint32_t)(Arg7))) != 1) goto loc_003010A6;
loc_00300DDD:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg8 + 0x20))));
    result = (uint32_t)((result) & (*(uint32_t *)(local_rdi + 0x4)));
    goto loc_00300D0F;
loc_00300DED:
    if (((uint8_t)(result)) != 4) goto loc_00300E57;
    Arg4 = 0;
    Arg3 = (*(uint8_t *)(local_rdi + 0xD)) + (5);
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
    result = SepSidInToken(Arg1, Arg6, local_rdi + Arg3 * 4, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00300D0F;
    Arg4 = 0;
    v_stack_p28 = Arg12;
    Arg2 = 0;
    v_stack_p20 = 0;
    goto loc_00300D7D;
loc_00300E57:
    if (Arg12 == 1) goto loc_00300EAA;
    if (Arg12 != 9) goto loc_00300D17;
    result = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    result = (uint32_t)((result) - (8));
    if (condition_is_less_or_equal) goto loc_00301102;
    if (0 != 0) goto loc_003010E0;
loc_00300E90:
    if (*(uint64_t *)(arg1 + 0x448) != 0) goto loc_00300EF3;
    Arg4 = 0;
    Arg3 = 0;
    local_r10 = 0;
    local_r11 = 0;
    goto loc_00300F0F;
loc_00300EAA:
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
    result = SepSidInToken(Arg1, Arg6, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_00300D0F;
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg8 + 0x1C))));
    result = (uint32_t)((result) & (*(uint32_t *)(local_rdi + 0x4)));
    goto loc_00300D0F;
loc_00300EF3:
loc_00300F0F:
    v_stack_p58 = v_stack_p64;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_p50 = Arg11;
    v_stack_p48 = 0;
    v_stack_p40 = (uint32_t)(Arg2);
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8))) + (8);
    Arg1 = (Arg1) + (local_rdi);
    v_stack_p38 = Arg1;
    v_stack_p30 = *(uint64_t *)(result + 0x258);
    v_stack_p28 = *(uint64_t *)(result + 0x248);
    v_stack_p20 = *(uint64_t *)(result + 0x250);
    result = AuthzBasepEvaluateAceCondition(Arg1, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), *(uint64_t *)(result + 0x240));
    if (v_stack_p64 != 1) goto loc_00300D08;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), *(uint64_t *)(result + 0x240));
    result = SepIsPackageSid(local_rdi + 8, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), *(uint64_t *)(result + 0x240));
    result = SepIsCapabilitySid(local_rdi + 8, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), *(uint64_t *)(result + 0x240));
loc_00300FC8:
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_00300C56;
loc_00300FD8:
    *(uint32_t *)(arg8 + 0x1C - 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg8 + 0x1C)));
    Arg2 = ((uint32_t)(Arg7)) - (1);
    if (condition_is_not_equal) goto loc_00300FD8;
    goto loc_00300C56;
loc_00300FEF:
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_00300D41;
    local_rsi = (Arg8) + (28);
    Arg1 = (uint32_t)(~((uint32_t)(Arg10)));
loc_00301008:
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (*(uint32_t *)(local_rsi)));
    result = (uint32_t)((result) & (*(uint32_t *)(local_rsi - 0x4)));
    *(uint32_t *)(local_rsi) = (uint32_t)(result);
    Arg2 = ((uint32_t)(Arg7)) - (1);
    if (condition_is_not_equal) goto loc_00301008;
    goto loc_00300D41;
loc_00301020:
    if ((uint32_t)((uint32_t)(v_stack_pC0)) != 0) goto loc_003010D0;
loc_00301028:
    if (Arg11 != 0) goto loc_00300DA4;
    result = SepIsCapabilitySid(local_rdi + 8, Arg2, *(uint64_t *)(arg5), *(uint64_t *)(result + 0x240));
    if ((uint8_t)(result) == 0) goto loc_00300DA4;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_p28 = Arg13 + 8;
    v_stack_p20 = Arg13 + 22;
    result = SepMatchCapability(Arg1, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    goto loc_00300D01;
loc_0030106C:
    if (Arg11 != 0) goto loc_00300D5B;
    result = SepIsPackageSid(local_rdi + 8, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = SepIsCapabilitySid(local_rdi + 8, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    goto loc_00300D5B;
loc_003010A6:
    v_stack_p28 = 1;
    Arg3 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = AuthzBasepAddAccessTypeList(local_rsi + 48, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, (uint32_t)(Arg11));
    goto loc_00300D0F;
loc_003010D0:
    if (v_stack_p60 == 0) goto loc_00300DA4;
    goto loc_00301028;
loc_003010E0:
    if ((*(uint64_t *)(arg5)) != 0) goto loc_00300E90;
    result = AuthzBasepInitializeResourceClaimsFromSacl((uint32_t)(Arg11), Arg5, Arg3, (uint32_t)(Arg11));
    goto loc_00300E90;
loc_00301102:
    goto loc_00300D17;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0x308` | `64` | `R` |
| `Arg1` | `+ 0x448` | `64` | `R` |
| `Arg3` | `+ 0x0` | `8` | `R` |
| `Arg3` | `+ 0x0 + r8*4` | `64` | `R` |
| `Arg3` | `+ 0x1` | `8` | `R` |
| `Arg3` | `+ 0x2` | `16` | `R` |
| `Arg3` | `+ 0x4` | `16` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x9` | `8` | `R` |
| `Arg3` | `+ 0xC` | `64` | `R` |
| `Arg3` | `+ 0xD` | `8` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg8` | `- 0x4` | `32` | `R` |
| `Arg8` | `- 0x4` | `32` | `W` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R/W` |
| `Arg8` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x1C` | `32` | `R` |
| `Arg8` | `+ 0x1C` | `32` | `R/W` |
| `Arg8` | `+ 0x1C` | `64` | `R` |
| `Arg8` | `+ 0x20` | `32` | `R` |
| `Arg8` | `+ 0x20` | `32` | `R/W` |
| `Arg8` | `+ 0x30` | `64` | `R` |
| `Arg13` | `+ 0x0` | `32` | `R` |
| `Arg13` | `+ 0x0` | `32` | `R/W` |
| `Arg13` | `+ 0x4` | `64` | `R` |
| `Arg13` | `+ 0x8` | `64` | `R` |
| `Arg13` | `+ 0x10` | `64` | `R` |
| `Arg13` | `+ 0x14` | `64` | `R` |
| `Arg13` | `+ 0x15` | `64` | `R` |

추가 오프셋 2개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00300BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
