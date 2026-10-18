# SepNormalAccessCheck

- RVA: `0x003D0688`–`0x003D0C60` (길이 `1,496` bytes)
- VA: `0x00000001403D0688`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000910CC`
- 디코드: `349`개 명령, `1,496/1,496` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003D0708` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D077B` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D07C3` → [SepSidInToken](SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003D0800` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003D084C` → [SepMatchPackage](../2F/SepMatchPackage_function_002FFDC0.md) (function, `0x002FFDC0`)
- `0x003D08BD` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003D08CD` → [SepIsCapabilitySid](SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003D0941` → [SepSidInToken](SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003D09EB` → [SepIsCapabilitySid](SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003D0A1C` → [SepMatchCapability](SepMatchCapability_function_003D0C70.md) (function, `0x003D0C70`)
- `0x003D0A95` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x003D0AA5` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D0ADA` → [SepIsCapabilitySid](SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003D0B1F` → [SepSidInToken](SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003D0B4D` → [AuthzBasepAddAccessTypeList](AuthzBasepAddAccessTypeList_function_003D196C.md) (function, `0x003D196C`)
- `0x003D0B74` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x003D0B97` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003D0BF1` → [SepSidInToken](SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003D0C31` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003D0C41` → [SepIsCapabilitySid](SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)

### Direct callers
- [SepAccessCheck](SepAccessCheck_function_003D0E54.md) at `0x003D104F`
- [SepAccessCheck](SepAccessCheck_function_003D0E54.md) at `0x003D142F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x003D08C4` → [sub_006E9020](../6E/Unknown_function_006E9020.md) (`tail-transfer`)
  - `0x003D08DA` → [sub_006E9020 + 0x35](../6E/Unknown_function_006E9020.md) (`tail-transfer`)
  - `0x003D090D` → [sub_006E9020 + 0x3D](../6E/Unknown_function_006E9020.md) (`tail-transfer`)
  - `0x003D095E` → [sub_006E9020 + 0xFA](../6E/Unknown_function_006E9020.md) (`tail-transfer`)
  - `0x003D0C38` → [sub_006E9020](../6E/Unknown_function_006E9020.md) (`tail-transfer`)
  - `0x003D0C48` → [sub_006E9020 + 0x35](../6E/Unknown_function_006E9020.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D0688  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003D068D  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003D0692  55                              push rbp
003D0693  56                              push rsi
003D0694  57                              push rdi
003D0695  41 54                           push r12
003D0697  41 55                           push r13
003D0699  41 56                           push r14
003D069B  41 57                           push r15
003D069D  48 81 EC 80 00 00 00            sub rsp, 0x80
003D06A4  44 8B B2 C8 00 00 00            mov r14d, dword ptr [rdx + 0xc8]
003D06AB  33 F6                           xor esi, esi
003D06AD  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
003D06B2  41 8B C6                        mov eax, r14d
003D06B5  83 4C 24 6C FF                  or dword ptr [rsp + 0x6c], 0xffffffff
003D06BA  25 00 40 00 00                  and eax, 0x4000
003D06BF  4C 8B BC 24 00 01 00 00         mov r15, qword ptr [rsp + 0x100]
003D06C7  41 81 E6 00 20 00 00            and r14d, 0x2000
003D06CE  49 8B F9                        mov rdi, r9
003D06D1  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
003D06D5  4C 8B EA                        mov r13, rdx
003D06D8  41 0F B7 41 04                  movzx eax, word ptr [r9 + 4]
003D06DD  8B D9                           mov ebx, ecx
003D06DF  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
003D06E3  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
003D06E8  39 B4 24 F8 00 00 00            cmp dword ptr [rsp + 0xf8], esi
003D06EF  76 17                           jbe 0x1403d0708
003D06F1  8B 8C 24 F8 00 00 00            mov ecx, dword ptr [rsp + 0xf8]
003D06F8  49 8D 47 18                     lea rax, [r15 + 0x18]
003D06FC  89 18                           mov dword ptr [rax], ebx
003D06FE  48 8D 40 30                     lea rax, [rax + 0x30]
003D0702  48 83 E9 01                     sub rcx, 1
003D0706  75 F4                           jne 0x1403d06fc
003D0708  E8 7B F0 11 00                  call 0x1404ef788
003D070D  48 8B AC 24 20 01 00 00         mov rbp, qword ptr [rsp + 0x120]
003D0715  44 8A A4 24 10 01 00 00         mov r12b, byte ptr [rsp + 0x110]
003D071D  85 C0                           test eax, eax
003D071F  0F 85 C4 01 00 00               jne 0x1403d08e9
003D0725  45 85 F6                        test r14d, r14d
003D0728  0F 84 CA 01 00 00               je 0x1403d08f8
003D072E  83 A4 24 C8 00 00 00 00         and dword ptr [rsp + 0xc8], 0
003D0736  48 83 C7 08                     add rdi, 8
003D073A  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
003D073F  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
003D0746  0F 86 34 01 00 00               jbe 0x1403d0880
003D074C  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
003D0753  41 8B 5F 18                     mov ebx, dword ptr [r15 + 0x18]
003D0757  85 DB                           test ebx, ebx
003D0759  0F 84 80 01 00 00               je 0x1403d08df
003D075F  F6 47 01 08                     test byte ptr [rdi + 1], 8
003D0763  0F 85 F8 00 00 00               jne 0x1403d0861
003D0769  85 DB                           test ebx, ebx
003D076B  0F 84 45 02 00 00               je 0x1403d09b6
003D0771  8A 07                           mov al, byte ptr [rdi]
003D0773  84 C0                           test al, al
003D0775  0F 85 90 01 00 00               jne 0x1403d090b
003D077B  E8 08 F0 11 00                  call 0x1404ef788
003D0780  85 C0                           test eax, eax
003D0782  0F 84 14 01 00 00               je 0x1403d089c
003D0788  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
003D078C  45 85 F6                        test r14d, r14d
003D078F  74 5A                           je 0x1403d07eb
003D0791  85 DB                           test ebx, ebx
003D0793  75 56                           jne 0x1403d07eb
003D0795  41 8B 5F 18                     mov ebx, dword ptr [r15 + 0x18]
003D0799  85 DB                           test ebx, ebx
003D079B  0F 84 B9 00 00 00               je 0x1403d085a
003D07A1  4C 8D 47 08                     lea r8, [rdi + 8]
003D07A5  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
003D07AC  49 8B CD                        mov rcx, r13
003D07AF  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
003D07B7  45 33 C9                        xor r9d, r9d
003D07BA  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003D07BE  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003D07C3  E8 68 FC FF FF                  call 0x1403d0430
003D07C8  84 C0                           test al, al
003D07CA  0F 84 8A 00 00 00               je 0x1403d085a
003D07D0  83 BC 24 F8 00 00 00 01         cmp dword ptr [rsp + 0xf8], 1
003D07D8  8B 47 04                        mov eax, dword ptr [rdi + 4]
003D07DB  0F 85 4E 03 00 00               jne 0x1403d0b2f
003D07E1  F7 D0                           not eax
003D07E3  23 C3                           and eax, ebx
003D07E5  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
003D07E9  EB 6F                           jmp 0x1403d085a
003D07EB  45 84 E4                        test r12b, r12b
003D07EE  0F 85 D9 01 00 00               jne 0x1403d09cd
003D07F4  85 F6                           test esi, esi
003D07F6  0F 84 D1 01 00 00               je 0x1403d09cd
003D07FC  48 8D 4F 08                     lea rcx, [rdi + 8]
003D0800  E8 1B 09 F3 FF                  call 0x140301120
003D0805  84 C0                           test al, al
003D0807  0F 84 A1 03 00 00               je 0x1403d0bae
003D080D  48 8D 45 18                     lea rax, [rbp + 0x18]
003D0811  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003D0816  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003D081A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003D081F  48 8D 55 14                     lea rdx, [rbp + 0x14]
003D0823  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003D0828  48 8D 5D 04                     lea rbx, [rbp + 4]
003D082C  4C 8D 4D 15                     lea r9, [rbp + 0x15]
003D0830  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
003D0835  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003D083A  4C 8D 47 08                     lea r8, [rdi + 8]
003D083E  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
003D0842  49 8B CD                        mov rcx, r13
003D0845  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
003D084C  E8 6F F5 F2 FF                  call 0x1402ffdc0
003D0851  8B 03                           mov eax, dword ptr [rbx]
003D0853  F7 D0                           not eax
003D0855  23 F0                           and esi, eax
003D0857  21 45 00                        and dword ptr [rbp], eax
003D085A  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
003D0861  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
003D0865  FF C1                           inc ecx
003D0867  44 8B 74 24 68                  mov r14d, dword ptr [rsp + 0x68]
003D086C  48 03 F8                        add rdi, rax
003D086F  89 8C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ecx
003D0876  3B 4C 24 70                     cmp ecx, dword ptr [rsp + 0x70]
003D087A  0F 82 D3 FE FF FF               jb 0x1403d0753
003D0880  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
003D0888  48 81 C4 80 00 00 00            add rsp, 0x80
003D088F  41 5F                           pop r15
003D0891  41 5E                           pop r14
003D0893  41 5D                           pop r13
003D0895  41 5C                           pop r12
003D0897  5F                              pop rdi
003D0898  5E                              pop rsi
003D0899  5D                              pop rbp
003D089A  C3                              ret
003D089B  CC                              int3
003D089C  45 85 F6                        test r14d, r14d
003D089F  0F 85 F0 FE FF FF               jne 0x1403d0795
003D08A5  45 84 E4                        test r12b, r12b
003D08A8  0F 85 E7 FE FF FF               jne 0x1403d0795
003D08AE  85 F6                           test esi, esi
003D08B0  0F 84 DF FE FF FF               je 0x1403d0795
003D08B6  4C 8D 77 08                     lea r14, [rdi + 8]
003D08BA  49 8B CE                        mov rcx, r14
003D08BD  E8 5E 08 F3 FF                  call 0x140301120
003D08C2  84 C0                           test al, al
003D08C4  0F 85 56 87 31 00               jne 0x1406e9020
003D08CA  49 8B CE                        mov rcx, r14
003D08CD  E8 1E 05 00 00                  call 0x1403d0df0
003D08D2  84 C0                           test al, al
003D08D4  0F 84 BB FE FF FF               je 0x1403d0795
003D08DA  E9 76 87 31 00                  jmp 0x1406e9055
003D08DF  85 F6                           test esi, esi
003D08E1  0F 85 78 FE FF FF               jne 0x1403d075f
003D08E7  EB 97                           jmp 0x1403d0880
003D08E9  45 85 F6                        test r14d, r14d
003D08EC  74 0A                           je 0x1403d08f8
003D08EE  39 74 24 60                     cmp dword ptr [rsp + 0x60], esi
003D08F2  0F 84 36 FE FF FF               je 0x1403d072e
003D08F8  45 84 E4                        test r12b, r12b
003D08FB  0F 85 2D FE FF FF               jne 0x1403d072e
003D0901  8B F3                           mov esi, ebx
003D0903  0B 75 00                        or esi, dword ptr [rbp]
003D0906  E9 23 FE FF FF                  jmp 0x1403d072e
003D090B  3C 05                           cmp al, 5
003D090D  0F 84 4A 87 31 00               je 0x1406e905d
003D0913  3C 04                           cmp al, 4
003D0915  0F 84 AA 02 00 00               je 0x1403d0bc5
003D091B  3C 01                           cmp al, 1
003D091D  75 3D                           jne 0x1403d095c
003D091F  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
003D0926  4C 8D 47 08                     lea r8, [rdi + 8]
003D092A  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
003D0932  41 B1 01                        mov r9b, 1
003D0935  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003D0939  49 8B CD                        mov rcx, r13
003D093C  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003D0941  E8 EA FA FF FF                  call 0x1403d0430
003D0946  84 C0                           test al, al
003D0948  0F 84 0C FF FF FF               je 0x1403d085a
003D094E  85 5F 04                        test dword ptr [rdi + 4], ebx
003D0951  0F 85 29 FF FF FF               jne 0x1403d0880
003D0957  E9 FE FE FF FF                  jmp 0x1403d085a
003D095C  3C 06                           cmp al, 6
003D095E  0F 84 B6 87 31 00               je 0x1406e911a
003D0964  3C 09                           cmp al, 9
003D0966  0F 85 F5 FE FF FF               jne 0x1403d0861
003D096C  0F B6 47 09                     movzx eax, byte ptr [rdi + 9]
003D0970  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
003D0977  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
003D097B  2B C3                           sub eax, ebx
003D097D  83 F8 08                        cmp eax, 8
003D0980  0F 84 DB FE FF FF               je 0x1403d0861
003D0986  48 83 BC 24 E0 00 00 00 00      cmp qword ptr [rsp + 0xe0], 0
003D098F  0F 85 C2 01 00 00               jne 0x1403d0b57
003D0995  49 8B 85 48 04 00 00            mov rax, qword ptr [r13 + 0x448]
003D099C  48 85 C0                        test rax, rax
003D099F  0F 85 81 00 00 00               jne 0x1403d0a26
003D09A5  45 33 C9                        xor r9d, r9d
003D09A8  45 33 C0                        xor r8d, r8d
003D09AB  45 33 D2                        xor r10d, r10d
003D09AE  45 33 DB                        xor r11d, r11d
003D09B1  E9 8C 00 00 00                  jmp 0x1403d0a42
003D09B6  8A 07                           mov al, byte ptr [rdi]
003D09B8  84 C0                           test al, al
003D09BA  0F 84 B1 FD FF FF               je 0x1403d0771
003D09C0  3C 09                           cmp al, 9
003D09C2  0F 85 99 FE FF FF               jne 0x1403d0861
003D09C8  E9 A4 FD FF FF                  jmp 0x1403d0771
003D09CD  45 85 F6                        test r14d, r14d
003D09D0  0F 85 E2 01 00 00               jne 0x1403d0bb8
003D09D6  45 84 E4                        test r12b, r12b
003D09D9  0F 85 B6 FD FF FF               jne 0x1403d0795
003D09DF  85 F6                           test esi, esi
003D09E1  0F 84 AE FD FF FF               je 0x1403d0795
003D09E7  48 8D 4F 08                     lea rcx, [rdi + 8]
003D09EB  E8 00 04 00 00                  call 0x1403d0df0
003D09F0  84 C0                           test al, al
003D09F2  0F 84 9D FD FF FF               je 0x1403d0795
003D09F8  4C 8D 47 08                     lea r8, [rdi + 8]
003D09FC  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
003D0A00  48 8D 45 16                     lea rax, [rbp + 0x16]
003D0A04  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
003D0A0B  48 8D 5D 08                     lea rbx, [rbp + 8]
003D0A0F  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
003D0A14  49 8B CD                        mov rcx, r13
003D0A17  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D0A1C  E8 4F 02 00 00                  call 0x1403d0c70
003D0A21  E9 2B FE FF FF                  jmp 0x1403d0851
003D0A26  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
003D0A2D  4C 8B 80 50 02 00 00            mov r8, qword ptr [rax + 0x250]
003D0A34  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
003D0A3B  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
003D0A42  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
003D0A46  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
003D0A4B  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003D0A50  2B D3                           sub edx, ebx
003D0A52  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
003D0A5A  83 EA 08                        sub edx, 8
003D0A5D  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
003D0A62  C6 44 24 48 00                  mov byte ptr [rsp + 0x48], 0
003D0A67  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
003D0A6B  49 8B 95 08 03 00 00            mov rdx, qword ptr [r13 + 0x308]
003D0A72  8B CB                           mov ecx, ebx
003D0A74  48 83 C1 08                     add rcx, 8
003D0A78  48 03 CF                        add rcx, rdi
003D0A7B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003D0A80  49 8B CD                        mov rcx, r13
003D0A83  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
003D0A88  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
003D0A8D  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
003D0A92  4C 8B 00                        mov r8, qword ptr [rax]
003D0A95  E8 36 E1 F2 FF                  call 0x1402febd0
003D0A9A  83 7C 24 6C 01                  cmp dword ptr [rsp + 0x6c], 1
003D0A9F  0F 85 B5 FD FF FF               jne 0x1403d085a
003D0AA5  E8 DE EC 11 00                  call 0x1404ef788
003D0AAA  85 C0                           test eax, eax
003D0AAC  74 3B                           je 0x1403d0ae9
003D0AAE  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
003D0AB2  45 85 F6                        test r14d, r14d
003D0AB5  0F 85 C3 00 00 00               jne 0x1403d0b7e
003D0ABB  45 84 E4                        test r12b, r12b
003D0ABE  0F 84 C7 00 00 00               je 0x1403d0b8b
003D0AC4  45 85 F6                        test r14d, r14d
003D0AC7  0F 85 86 01 00 00               jne 0x1403d0c53
003D0ACD  45 84 E4                        test r12b, r12b
003D0AD0  75 20                           jne 0x1403d0af2
003D0AD2  85 F6                           test esi, esi
003D0AD4  74 1C                           je 0x1403d0af2
003D0AD6  48 8D 4F 08                     lea rcx, [rdi + 8]
003D0ADA  E8 11 03 00 00                  call 0x1403d0df0
003D0ADF  84 C0                           test al, al
003D0AE1  0F 85 11 FF FF FF               jne 0x1403d09f8
003D0AE7  EB 09                           jmp 0x1403d0af2
003D0AE9  45 85 F6                        test r14d, r14d
003D0AEC  0F 84 27 01 00 00               je 0x1403d0c19
003D0AF2  41 83 7F 18 00                  cmp dword ptr [r15 + 0x18], 0
003D0AF7  0F 84 5D FD FF FF               je 0x1403d085a
003D0AFD  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
003D0B04  4C 8D 47 08                     lea r8, [rdi + 8]
003D0B08  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
003D0B10  45 33 C9                        xor r9d, r9d
003D0B13  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003D0B17  49 8B CD                        mov rcx, r13
003D0B1A  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003D0B1F  E8 0C F9 FF FF                  call 0x1403d0430
003D0B24  84 C0                           test al, al
003D0B26  0F 84 2E FD FF FF               je 0x1403d085a
003D0B2C  8B 47 04                        mov eax, dword ptr [rdi + 4]
003D0B2F  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
003D0B34  45 33 C0                        xor r8d, r8d
003D0B37  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
003D0B3F  49 8B CF                        mov rcx, r15
003D0B42  8B 94 24 F8 00 00 00            mov edx, dword ptr [rsp + 0xf8]
003D0B49  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003D0B4D  E8 1A 0E 00 00                  call 0x1403d196c
003D0B52  E9 03 FD FF FF                  jmp 0x1403d085a
003D0B57  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
003D0B5F  48 83 38 00                     cmp qword ptr [rax], 0
003D0B63  0F 85 2C FE FF FF               jne 0x1403d0995
003D0B69  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
003D0B71  48 8B D0                        mov rdx, rax
003D0B74  E8 0B 23 F3 FF                  call 0x140302e84
003D0B79  E9 17 FE FF FF                  jmp 0x1403d0995
003D0B7E  85 DB                           test ebx, ebx
003D0B80  0F 84 6C FF FF FF               je 0x1403d0af2
003D0B86  E9 30 FF FF FF                  jmp 0x1403d0abb
003D0B8B  85 F6                           test esi, esi
003D0B8D  0F 84 31 FF FF FF               je 0x1403d0ac4
003D0B93  48 8D 4F 08                     lea rcx, [rdi + 8]
003D0B97  E8 84 05 F3 FF                  call 0x140301120
003D0B9C  84 C0                           test al, al
003D0B9E  0F 85 69 FC FF FF               jne 0x1403d080d
003D0BA4  44 8B 74 24 68                  mov r14d, dword ptr [rsp + 0x68]
003D0BA9  E9 16 FF FF FF                  jmp 0x1403d0ac4
003D0BAE  44 8B 74 24 68                  mov r14d, dword ptr [rsp + 0x68]
003D0BB3  E9 15 FE FF FF                  jmp 0x1403d09cd
003D0BB8  85 DB                           test ebx, ebx
003D0BBA  0F 84 D5 FB FF FF               je 0x1403d0795
003D0BC0  E9 11 FE FF FF                  jmp 0x1403d09d6
003D0BC5  0F B6 47 0D                     movzx eax, byte ptr [rdi + 0xd]
003D0BC9  45 33 C9                        xor r9d, r9d
003D0BCC  44 8A B4 24 18 01 00 00         mov r14b, byte ptr [rsp + 0x118]
003D0BD4  48 83 C0 05                     add rax, 5
003D0BD8  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
003D0BE0  49 8B CD                        mov rcx, r13
003D0BE3  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
003D0BE8  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003D0BED  4C 8D 04 87                     lea r8, [rdi + rax*4]
003D0BF1  E8 3A F8 FF FF                  call 0x1403d0430
003D0BF6  84 C0                           test al, al
003D0BF8  0F 84 5C FC FF FF               je 0x1403d085a
003D0BFE  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
003D0C06  4C 8D 47 0C                     lea r8, [rdi + 0xc]
003D0C0A  45 33 C9                        xor r9d, r9d
003D0C0D  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
003D0C12  33 D2                           xor edx, edx
003D0C14  E9 A5 FB FF FF                  jmp 0x1403d07be
003D0C19  45 84 E4                        test r12b, r12b
003D0C1C  0F 85 D0 FE FF FF               jne 0x1403d0af2
003D0C22  85 F6                           test esi, esi
003D0C24  0F 84 C8 FE FF FF               je 0x1403d0af2
003D0C2A  4C 8D 77 08                     lea r14, [rdi + 8]
003D0C2E  49 8B CE                        mov rcx, r14
003D0C31  E8 EA 04 F3 FF                  call 0x140301120
003D0C36  84 C0                           test al, al
003D0C38  0F 85 E2 83 31 00               jne 0x1406e9020
003D0C3E  49 8B CE                        mov rcx, r14
003D0C41  E8 AA 01 00 00                  call 0x1403d0df0
003D0C46  84 C0                           test al, al
003D0C48  0F 85 07 84 31 00               jne 0x1406e9055
003D0C4E  E9 9F FE FF FF                  jmp 0x1403d0af2
003D0C53  85 DB                           test ebx, ebx
003D0C55  0F 84 97 FE FF FF               je 0x1403d0af2
003D0C5B  E9 6D FE FF FF                  jmp 0x1403d0acd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepNormalAccessCheck(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10, unsigned __int8 a11, unsigned __int8 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int8 v_stack_m90;
    unsigned __int8 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (128);
    v_rsi = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 200))))) & (0x4000ULL));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 200))) & (0x2000ULL));
    v_stack_m58 = (unsigned int)(result);
    v_stack_m48 = (unsigned int)(*(unsigned __int16 *)(a4 + 4));
    v_stack_m50 = (unsigned int)(v_r14);
    if (a8 <= 0) goto loc_003D0708;
loc_003D06FC:
    *(unsigned int *)(a9 + 24) = (unsigned int)((unsigned int)(a1));
    a1 = ((unsigned int)(a8)) - (1);
    if (condition_is_not_equal) goto loc_003D06FC;
loc_003D0708:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_003D08E9;
    if ((unsigned int)(v_r14) == 0) goto loc_003D08F8;
loc_003D072E:
    v_rdi = (a4) + (8);
    v_stack_p20 = 0;
    if (v_stack_m48 <= 0) goto loc_003D0880;
loc_003D0753:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24))) == 0) goto loc_003D08DF;
loc_003D075F:
    if (((*(unsigned __int8 *)(v_rdi + 1)) & (8)) != 0) goto loc_003D0861;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24))) == 0) goto loc_003D09B6;
loc_003D0771:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) != 0) goto loc_003D090B;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)(v_stack_p10), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_003D089C;
    if ((unsigned int)(v_r14) == 0) goto loc_003D07EB;
    if ((unsigned int)((unsigned int)(v_stack_m58)) != 0) goto loc_003D07EB;
loc_003D0795:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24))) == 0) goto loc_003D085A;
    a4 = 0;
    v_stack_m90 = a12;
loc_003D07BE:
    v_stack_m98 = a11;
    result = SepSidInToken(a2, a7, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D085A;
    if (a8 != 1) goto loc_003D0B2F;
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_rdi + 4))));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24)))));
    *(unsigned int *)(a9 + 24) = (unsigned int)(result);
    goto loc_003D085A;
loc_003D07EB:
    if (a11 != 0) goto loc_003D09CD;
    if (0 == 0) goto loc_003D09CD;
    result = SepIsPackageSid(v_rdi + 8, a7, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D0BAE;
loc_003D080D:
    v_stack_m78 = a13 + 24;
    v_stack_m80 = a13 + 16;
    v_stack_m88 = a13 + 20;
    v_stack_m90 = a13 + 4;
    v_stack_m98 = a13 + 21;
    result = SepMatchPackage(a2, (unsigned int)(v_stack_p20), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
loc_003D0851:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a13 + 4))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(result)));
loc_003D085A:
loc_003D0861:
    a1 = (unsigned int)(((unsigned int)(v_stack_p10)) + 1);
    v_rdi = (v_rdi) + (*(unsigned __int16 *)(v_rdi + 2));
    v_stack_p10 = a1;
    if (a1 < v_stack_m48) goto loc_003D0753;
loc_003D0880:
    v_rsp = (v_rsp) + (128);
    return *(unsigned __int16 *)(v_rdi + 2);
loc_003D089C:
    if ((unsigned int)((unsigned int)(v_stack_m50)) != 0) goto loc_003D0795;
    if (a11 != 0) goto loc_003D0795;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D0795;
    result = SepIsPackageSid(v_rdi + 8, (unsigned int)(v_stack_p20), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = SepIsCapabilitySid(v_rdi + 8, (unsigned int)(v_stack_p20), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    if ((unsigned __int8)(result) == 0) goto loc_003D0795;
loc_003D08DF:
    if ((unsigned int)(v_rsi) != 0) goto loc_003D075F;
    goto loc_003D0880;
loc_003D08E9:
    if ((unsigned int)(v_rdi + 8) == 0) goto loc_003D08F8;
    if (v_stack_p60 == ((unsigned int)(v_rsi))) goto loc_003D072E;
loc_003D08F8:
    if (a11 != 0) goto loc_003D072E;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) | (*(unsigned int *)(a13)));
    goto loc_003D072E;
loc_003D090B:
    if (((unsigned __int8)(result)) == 4) goto loc_003D0BC5;
    if (((unsigned __int8)(result)) != 1) goto loc_003D095C;
    v_stack_p28 = a12;
    v_stack_p20 = a11;
    result = SepSidInToken(a2, a7, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_003D085A;
    if (((*(unsigned int *)(v_rdi + 4)) & ((unsigned int)(v_stack_p8))) != 0) goto loc_003D0880;
    goto loc_003D085A;
loc_003D095C:
    if (((unsigned __int8)(result)) != 9) goto loc_003D0861;
    result = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    if (((unsigned int)(result)) == 8) goto loc_003D0861;
    if (a5 != 0) goto loc_003D0B57;
loc_003D0995:
    if (*(unsigned __int64 *)(a2 + 1096) != 0) goto loc_003D0A26;
    a4 = 0;
    a3 = 0;
    v_r10 = 0;
    v_r11 = 0;
    goto loc_003D0A42;
loc_003D09B6:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) == 0) goto loc_003D0771;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) != 9) goto loc_003D0861;
    goto loc_003D0771;
loc_003D09CD:
    if ((unsigned int)(v_rdi + 8) != 0) goto loc_003D0BB8;
loc_003D09D6:
    if (a11 != 0) goto loc_003D0795;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D0795;
    result = SepIsCapabilitySid(v_rdi + 8, a7, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D0795;
loc_003D09F8:
    v_stack_p28 = a13 + 8;
    v_stack_p20 = a13 + 22;
    result = SepMatchCapability(a2, (unsigned int)(v_stack_pD8), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    goto loc_003D0851;
loc_003D0A26:
loc_003D0A42:
    v_stack_p58 = v_stack_p6C;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(a13 + 8)));
    a2 = (unsigned int)((a2) - (8));
    v_stack_p50 = a11;
    v_stack_p48 = 0;
    v_stack_p40 = (unsigned int)(a2);
    a1 = ((unsigned int)((unsigned int)(a13 + 8))) + (8);
    a1 = (a1) + (v_rdi);
    v_stack_p38 = a1;
    v_stack_p30 = *(unsigned __int64 *)(result + 600);
    v_stack_p28 = *(unsigned __int64 *)(result + 584);
    v_stack_p20 = *(unsigned __int64 *)(result + 592);
    result = AuthzBasepEvaluateAceCondition(a2, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(result + 576));
    if (v_stack_p6C != 1) goto loc_003D085A;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a2, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(result + 576));
    if ((unsigned int)(result) == 0) goto loc_003D0AE9;
    if ((unsigned int)(v_rdi + 8) != 0) goto loc_003D0B7E;
loc_003D0ABB:
    if (a11 == 0) goto loc_003D0B8B;
loc_003D0AC4:
    if ((unsigned int)(v_rdi + 8) != 0) goto loc_003D0C53;
loc_003D0ACD:
    if (a11 != 0) goto loc_003D0AF2;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D0AF2;
    result = SepIsCapabilitySid(v_rdi + 8, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(result + 576));
    if ((unsigned __int8)(result) != 0) goto loc_003D09F8;
    goto loc_003D0AF2;
loc_003D0AE9:
    if ((unsigned int)(v_rdi + 8) == 0) goto loc_003D0C19;
loc_003D0AF2:
    if ((*(unsigned int *)(a9 + 24)) == 0) goto loc_003D085A;
    a4 = 0;
    v_stack_p28 = a12;
    v_stack_p20 = a11;
    result = SepSidInToken(a2, a7, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D085A;
loc_003D0B2F:
    a3 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = AuthzBasepAddAccessTypeList(a9, (unsigned int)(a8), a3, (unsigned int)(v_stack_pC8));
    goto loc_003D085A;
loc_003D0B57:
    if ((*(unsigned __int64 *)(a6)) != 0) goto loc_003D0995;
    result = AuthzBasepInitializeResourceClaimsFromSacl(a5, a6, a3, (unsigned int)(v_stack_pC8));
    goto loc_003D0995;
loc_003D0B7E:
    if ((unsigned int)((unsigned int)(v_stack_p60)) == 0) goto loc_003D0AF2;
    goto loc_003D0ABB;
loc_003D0B8B:
    if ((unsigned int)(v_rsi) == 0) goto loc_003D0AC4;
    result = SepIsPackageSid(v_rdi + 8, a6, a3, (unsigned int)(v_stack_pC8));
    if ((unsigned __int8)(result) != 0) goto loc_003D080D;
    goto loc_003D0AC4;
loc_003D0BAE:
    goto loc_003D09CD;
loc_003D0BB8:
    if ((unsigned int)((unsigned int)(v_stack_p60)) == 0) goto loc_003D0795;
    goto loc_003D09D6;
loc_003D0BC5:
    a4 = 0;
    result = (*(unsigned __int8 *)(v_rdi + 13)) + (5);
    v_stack_p28 = a12;
    v_stack_p20 = a11;
    result = SepSidInToken(a2, a7, v_rdi + result * 4, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D085A;
    a4 = 0;
    v_stack_p28 = a12;
    a2 = 0;
    goto loc_003D07BE;
loc_003D0C19:
    if (a11 != 0) goto loc_003D0AF2;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D0AF2;
    result = SepIsPackageSid(v_rdi + 8, a2, v_rdi + 12, a4);
    result = SepIsCapabilitySid(v_rdi + 8, a2, v_rdi + 12, a4);
    goto loc_003D0AF2;
loc_003D0C53:
    if ((unsigned int)((unsigned int)(v_stack_p60)) == 0) goto loc_003D0AF2;
    goto loc_003D0ACD;
}
```

## 5. (Beta) C Style

```c
int64_t SepNormalAccessCheck(int32_t Arg1, void *Arg2, int64_t Arg3, void *Arg4, int64_t Arg5, void *Arg6, int64_t Arg7, uint32_t Arg8, void *Arg9, uint64_t Arg10, uint8_t Arg11, uint8_t Arg12, void *Arg13)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint8_t v_stack_m90;
    uint8_t v_stack_m98;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint8_t v_stack_p48;
    uint8_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint64_t v_stack_p8;
    uint32_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (128);
    local_rsi = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC8))))) & (0x4000ULL));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0xC8))) & (0x2000ULL));
    v_stack_m58 = (uint32_t)(result);
    v_stack_m48 = (uint32_t)(*(uint16_t *)(arg4 + 0x4));
    v_stack_m50 = (uint32_t)(local_r14);
    if (Arg8 <= 0) goto loc_003D0708;
loc_003D06FC:
    *(uint32_t *)(arg9 + 0x18) = (uint32_t)((uint32_t)(Arg1));
    Arg1 = ((uint32_t)(Arg8)) - (1);
    if (condition_is_not_equal) goto loc_003D06FC;
loc_003D0708:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_003D08E9;
    if ((uint32_t)(local_r14) == 0) goto loc_003D08F8;
loc_003D072E:
    local_rdi = (Arg4) + (8);
    v_stack_p20 = 0;
    if (v_stack_m48 <= 0) goto loc_003D0880;
loc_003D0753:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18))) == 0) goto loc_003D08DF;
loc_003D075F:
    if (((*(uint8_t *)(local_rdi + 0x1)) & (8)) != 0) goto loc_003D0861;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18))) == 0) goto loc_003D09B6;
loc_003D0771:
    if ((uint8_t)(*(uint8_t *)(local_rdi)) != 0) goto loc_003D090B;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)(v_stack_p10), Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003D089C;
    if ((uint32_t)(local_r14) == 0) goto loc_003D07EB;
    if ((uint32_t)((uint32_t)(v_stack_m58)) != 0) goto loc_003D07EB;
loc_003D0795:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18))) == 0) goto loc_003D085A;
    Arg4 = 0;
    v_stack_m90 = Arg12;
loc_003D07BE:
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg2, Arg7, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003D085A;
    if (Arg8 != 1) goto loc_003D0B2F;
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(local_rdi + 0x4))));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18)))));
    *(uint32_t *)(arg9 + 0x18) = (uint32_t)(result);
    goto loc_003D085A;
loc_003D07EB:
    if (Arg11 != 0) goto loc_003D09CD;
    if (0 == 0) goto loc_003D09CD;
    result = SepIsPackageSid(local_rdi + 8, Arg7, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003D0BAE;
loc_003D080D:
    v_stack_m78 = Arg13 + 24;
    v_stack_m80 = Arg13 + 16;
    v_stack_m88 = Arg13 + 20;
    v_stack_m90 = Arg13 + 4;
    v_stack_m98 = Arg13 + 21;
    result = SepMatchPackage(Arg2, (uint32_t)(v_stack_p20), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
loc_003D0851:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg13 + 0x4))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(result)));
loc_003D085A:
loc_003D0861:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p10)) + 1);
    local_rdi = (local_rdi) + (*(uint16_t *)(local_rdi + 0x2));
    v_stack_p10 = Arg1;
    if (Arg1 < v_stack_m48) goto loc_003D0753;
loc_003D0880:
    local_rsp = (local_rsp) + (128);
    return *(uint16_t *)(local_rdi + 0x2);
loc_003D089C:
    if ((uint32_t)((uint32_t)(v_stack_m50)) != 0) goto loc_003D0795;
    if (Arg11 != 0) goto loc_003D0795;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D0795;
    result = SepIsPackageSid(local_rdi + 8, (uint32_t)(v_stack_p20), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = SepIsCapabilitySid(local_rdi + 8, (uint32_t)(v_stack_p20), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    if ((uint8_t)(result) == 0) goto loc_003D0795;
loc_003D08DF:
    if ((uint32_t)(local_rsi) != 0) goto loc_003D075F;
    goto loc_003D0880;
loc_003D08E9:
    if ((uint32_t)(local_rdi + 8) == 0) goto loc_003D08F8;
    if (v_stack_p60 == ((uint32_t)(local_rsi))) goto loc_003D072E;
loc_003D08F8:
    if (Arg11 != 0) goto loc_003D072E;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) | (*(uint32_t *)(arg13)));
    goto loc_003D072E;
loc_003D090B:
    if (((uint8_t)(result)) == 4) goto loc_003D0BC5;
    if (((uint8_t)(result)) != 1) goto loc_003D095C;
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
    result = SepSidInToken(Arg2, Arg7, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_003D085A;
    if (((*(uint32_t *)(local_rdi + 0x4)) & ((uint32_t)(v_stack_p8))) != 0) goto loc_003D0880;
    goto loc_003D085A;
loc_003D095C:
    if (((uint8_t)(result)) != 9) goto loc_003D0861;
    result = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    if (((uint32_t)(result)) == 8) goto loc_003D0861;
    if (Arg5 != 0) goto loc_003D0B57;
loc_003D0995:
    if (*(uint64_t *)(arg2 + 0x448) != 0) goto loc_003D0A26;
    Arg4 = 0;
    Arg3 = 0;
    local_r10 = 0;
    local_r11 = 0;
    goto loc_003D0A42;
loc_003D09B6:
    if ((uint8_t)(*(uint8_t *)(local_rdi)) == 0) goto loc_003D0771;
    if (((uint8_t)(*(uint8_t *)(local_rdi))) != 9) goto loc_003D0861;
    goto loc_003D0771;
loc_003D09CD:
    if ((uint32_t)(local_rdi + 8) != 0) goto loc_003D0BB8;
loc_003D09D6:
    if (Arg11 != 0) goto loc_003D0795;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D0795;
    result = SepIsCapabilitySid(local_rdi + 8, Arg7, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003D0795;
loc_003D09F8:
    v_stack_p28 = Arg13 + 8;
    v_stack_p20 = Arg13 + 22;
    result = SepMatchCapability(Arg2, (uint32_t)(v_stack_pD8), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    goto loc_003D0851;
loc_003D0A26:
loc_003D0A42:
    v_stack_p58 = v_stack_p6C;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(Arg13 + 8)));
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_p50 = Arg11;
    v_stack_p48 = 0;
    v_stack_p40 = (uint32_t)(Arg2);
    Arg1 = ((uint32_t)((uint32_t)(Arg13 + 8))) + (8);
    Arg1 = (Arg1) + (local_rdi);
    v_stack_p38 = Arg1;
    v_stack_p30 = *(uint64_t *)(result + 0x258);
    v_stack_p28 = *(uint64_t *)(result + 0x248);
    v_stack_p20 = *(uint64_t *)(result + 0x250);
    result = AuthzBasepEvaluateAceCondition(Arg2, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(result + 0x240));
    if (v_stack_p6C != 1) goto loc_003D085A;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg2, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(result + 0x240));
    if ((uint32_t)(result) == 0) goto loc_003D0AE9;
    if ((uint32_t)(local_rdi + 8) != 0) goto loc_003D0B7E;
loc_003D0ABB:
    if (Arg11 == 0) goto loc_003D0B8B;
loc_003D0AC4:
    if ((uint32_t)(local_rdi + 8) != 0) goto loc_003D0C53;
loc_003D0ACD:
    if (Arg11 != 0) goto loc_003D0AF2;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D0AF2;
    result = SepIsCapabilitySid(local_rdi + 8, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(result + 0x240));
    if ((uint8_t)(result) != 0) goto loc_003D09F8;
    goto loc_003D0AF2;
loc_003D0AE9:
    if ((uint32_t)(local_rdi + 8) == 0) goto loc_003D0C19;
loc_003D0AF2:
    if ((*(uint32_t *)(arg9 + 0x18)) == 0) goto loc_003D085A;
    Arg4 = 0;
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
    result = SepSidInToken(Arg2, Arg7, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003D085A;
loc_003D0B2F:
    Arg3 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = AuthzBasepAddAccessTypeList(Arg9, (uint32_t)(Arg8), Arg3, (uint32_t)(v_stack_pC8));
    goto loc_003D085A;
loc_003D0B57:
    if ((*(uint64_t *)(arg6)) != 0) goto loc_003D0995;
    result = AuthzBasepInitializeResourceClaimsFromSacl(Arg5, Arg6, Arg3, (uint32_t)(v_stack_pC8));
    goto loc_003D0995;
loc_003D0B7E:
    if ((uint32_t)((uint32_t)(v_stack_p60)) == 0) goto loc_003D0AF2;
    goto loc_003D0ABB;
loc_003D0B8B:
    if ((uint32_t)(local_rsi) == 0) goto loc_003D0AC4;
    result = SepIsPackageSid(local_rdi + 8, Arg6, Arg3, (uint32_t)(v_stack_pC8));
    if ((uint8_t)(result) != 0) goto loc_003D080D;
    goto loc_003D0AC4;
loc_003D0BAE:
    goto loc_003D09CD;
loc_003D0BB8:
    if ((uint32_t)((uint32_t)(v_stack_p60)) == 0) goto loc_003D0795;
    goto loc_003D09D6;
loc_003D0BC5:
    Arg4 = 0;
    result = (*(uint8_t *)(local_rdi + 0xD)) + (5);
    v_stack_p28 = Arg12;
    v_stack_p20 = Arg11;
    result = SepSidInToken(Arg2, Arg7, local_rdi + result * 4, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003D085A;
    Arg4 = 0;
    v_stack_p28 = Arg12;
    Arg2 = 0;
    goto loc_003D07BE;
loc_003D0C19:
    if (Arg11 != 0) goto loc_003D0AF2;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D0AF2;
    result = SepIsPackageSid(local_rdi + 8, Arg2, local_rdi + 12, Arg4);
    result = SepIsCapabilitySid(local_rdi + 8, Arg2, local_rdi + 12, Arg4);
    goto loc_003D0AF2;
loc_003D0C53:
    if ((uint32_t)((uint32_t)(v_stack_p60)) == 0) goto loc_003D0AF2;
    goto loc_003D0ACD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xC8` | `32` | `R` |
| `Arg2` | `+ 0x308` | `64` | `R` |
| `Arg2` | `+ 0x448` | `64` | `R` |
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x0 + rax*4` | `64` | `R` |
| `Arg4` | `+ 0x1` | `8` | `R` |
| `Arg4` | `+ 0x2` | `16` | `R` |
| `Arg4` | `+ 0x4` | `16` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x9` | `8` | `R` |
| `Arg4` | `+ 0xC` | `64` | `R` |
| `Arg4` | `+ 0xD` | `8` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg9` | `+ 0x0` | `32` | `W` |
| `Arg9` | `+ 0x18` | `32` | `R` |
| `Arg9` | `+ 0x18` | `32` | `W` |
| `Arg9` | `+ 0x18` | `64` | `R` |
| `Arg9` | `+ 0x30` | `64` | `R` |
| `Arg13` | `+ 0x0` | `32` | `R` |
| `Arg13` | `+ 0x0` | `32` | `R/W` |
| `Arg13` | `+ 0x4` | `64` | `R` |
| `Arg13` | `+ 0x8` | `64` | `R` |
| `Arg13` | `+ 0x10` | `64` | `R` |
| `Arg13` | `+ 0x14` | `64` | `R` |
| `Arg13` | `+ 0x15` | `64` | `R` |
| `Arg13` | `+ 0x16` | `64` | `R` |
| `Arg13` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D0688&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
