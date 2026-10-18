# SepNormalAccessCheckEx

- RVA: `0x003CFD8C`–`0x003D0421` (길이 `1,685` bytes)
- VA: `0x00000001403CFD8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00090FEC`
- 디코드: `388`개 명령, `1,685/1,685` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003CFDF8` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003CFECA` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003CFF27` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003CFF73` → [SepMatchPackage](../2F/SepMatchPackage_function_002FFDC0.md) (function, `0x002FFDC0`)
- `0x003CFF95` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D00FB` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x003D010B` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D013A` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003D014A` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003D018A` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003D01BB` → [SepMatchCapability](../3D/SepMatchCapability_function_003D0C70.md) (function, `0x003D0C70`)
- `0x003D02C5` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x003D02F7` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003D032B` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x003D038F` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x003D039F` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x003D03F0` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x003D0417` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)

### Direct callers
- [SepAccessCheckEx](SepAccessCheckEx_function_003CF7B0.md) at `0x003CFA0C`
- [sub_006E89DA](../6E/Unknown_function_006E89DA.md) at `0x006E8B5D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x003CFE98` → [sub_006E8E06 + 0xB3](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003CFEE2` → [sub_006E8E06 + 0x1F9](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003CFFC7` → [sub_006E8E06 + 0x4C](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D0045` → [sub_006E8E06 + 0x158](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D0141` → [sub_006E8E06](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D0157` → [sub_006E8E06 + 0x35](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D030B` → [sub_006E8E06 + 0x1F9](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D0396` → [sub_006E8E06](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D03AC` → [sub_006E8E06 + 0x35](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D03C7` → [sub_006E8E06 + 0x3D](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)
  - `0x003D03FD` → [sub_006E8E06 + 0x51](../6E/Unknown_function_006E8E06.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CFD8C  48 8B C4                        mov rax, rsp
003CFD8F  48 89 58 08                     mov qword ptr [rax + 8], rbx
003CFD93  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
003CFD97  55                              push rbp
003CFD98  56                              push rsi
003CFD99  57                              push rdi
003CFD9A  41 54                           push r12
003CFD9C  41 55                           push r13
003CFD9E  41 56                           push r14
003CFDA0  41 57                           push r15
003CFDA2  48 83 EC 70                     sub rsp, 0x70
003CFDA6  83 60 C0 00                     and dword ptr [rax - 0x40], 0
003CFDAA  8B D9                           mov ebx, ecx
003CFDAC  83 60 C4 00                     and dword ptr [rax - 0x3c], 0
003CFDB0  33 F6                           xor esi, esi
003CFDB2  8B 82 C8 00 00 00               mov eax, dword ptr [rdx + 0xc8]
003CFDB8  49 8B F9                        mov rdi, r9
003CFDBB  44 8B BC 24 E8 00 00 00         mov r15d, dword ptr [rsp + 0xe8]
003CFDC3  8B C8                           mov ecx, eax
003CFDC5  4C 8B B4 24 F0 00 00 00         mov r14, qword ptr [rsp + 0xf0]
003CFDCD  25 00 20 00 00                  and eax, 0x2000
003CFDD2  81 E1 00 40 00 00               and ecx, 0x4000
003CFDD8  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
003CFDDC  41 0F B7 41 04                  movzx eax, word ptr [r9 + 4]
003CFDE1  4C 8B EA                        mov r13, rdx
003CFDE4  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
003CFDEB  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
003CFDEF  45 85 FF                        test r15d, r15d
003CFDF2  0F 85 EB 01 00 00               jne 0x1403cffe3
003CFDF8  E8 8B F9 11 00                  call 0x1404ef788
003CFDFD  48 8B AC 24 18 01 00 00         mov rbp, qword ptr [rsp + 0x118]
003CFE05  44 8A A4 24 00 01 00 00         mov r12b, byte ptr [rsp + 0x100]
003CFE0D  85 C0                           test eax, eax
003CFE0F  0F 84 5C 05 00 00               je 0x1403d0371
003CFE15  39 74 24 60                     cmp dword ptr [rsp + 0x60], esi
003CFE19  0F 85 CD 03 00 00               jne 0x1403d01ec
003CFE1F  45 84 E4                        test r12b, r12b
003CFE22  0F 84 A4 01 00 00               je 0x1403cffcc
003CFE28  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
003CFE2F  33 C0                           xor eax, eax
003CFE31  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
003CFE38  48 83 C7 08                     add rdi, 8
003CFE3C  89 B4 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], esi
003CFE43  3B C1                           cmp eax, ecx
003CFE45  0F 83 9C 00 00 00               jae 0x1403cfee7
003CFE4B  41 8B 5E 18                     mov ebx, dword ptr [r14 + 0x18]
003CFE4F  85 DB                           test ebx, ebx
003CFE51  0F 84 7F 01 00 00               je 0x1403cffd6
003CFE57  F6 47 01 08                     test byte ptr [rdi + 1], 8
003CFE5B  74 27                           je 0x1403cfe84
003CFE5D  44 8B BC 24 B8 00 00 00         mov r15d, dword ptr [rsp + 0xb8]
003CFE65  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
003CFE69  41 FF C7                        inc r15d
003CFE6C  48 03 F8                        add rdi, rax
003CFE6F  44 89 BC 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r15d
003CFE77  41 8B C7                        mov eax, r15d
003CFE7A  44 8B BC 24 E8 00 00 00         mov r15d, dword ptr [rsp + 0xe8]
003CFE82  EB BF                           jmp 0x1403cfe43
003CFE84  85 DB                           test ebx, ebx
003CFE86  0F 84 49 03 00 00               je 0x1403d01d5
003CFE8C  8A 07                           mov al, byte ptr [rdi]
003CFE8E  84 C0                           test al, al
003CFE90  0F 84 FF 00 00 00               je 0x1403cff95
003CFE96  3C 05                           cmp al, 5
003CFE98  0F 84 1B 90 31 00               je 0x1406e8eb9
003CFE9E  3C 04                           cmp al, 4
003CFEA0  0F 84 26 05 00 00               je 0x1403d03cc
003CFEA6  3C 01                           cmp al, 1
003CFEA8  0F 85 95 01 00 00               jne 0x1403d0043
003CFEAE  8A 84 24 08 01 00 00            mov al, byte ptr [rsp + 0x108]
003CFEB5  4C 8D 47 08                     lea r8, [rdi + 8]
003CFEB9  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003CFEBD  41 B1 01                        mov r9b, 1
003CFEC0  33 D2                           xor edx, edx
003CFEC2  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003CFEC7  49 8B CD                        mov rcx, r13
003CFECA  E8 61 05 00 00                  call 0x1403d0430
003CFECF  84 C0                           test al, al
003CFED1  0F 84 AA 00 00 00               je 0x1403cff81
003CFED7  23 5F 04                        and ebx, dword ptr [rdi + 4]
003CFEDA  0F 84 A1 00 00 00               je 0x1403cff81
003CFEE0  8B CB                           mov ecx, ebx
003CFEE2  E9 18 91 31 00                  jmp 0x1406e8fff
003CFEE7  0F 84 0F 01 00 00               je 0x1403cfffc
003CFEED  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
003CFEF5  48 83 C4 70                     add rsp, 0x70
003CFEF9  41 5F                           pop r15
003CFEFB  41 5E                           pop r14
003CFEFD  41 5D                           pop r13
003CFEFF  41 5C                           pop r12
003CFF01  5F                              pop rdi
003CFF02  5E                              pop rsi
003CFF03  5D                              pop rbp
003CFF04  C3                              ret
003CFF05  CC                              int3
003CFF06  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
003CFF0A  85 DB                           test ebx, ebx
003CFF0C  0F 85 B3 02 00 00               jne 0x1403d01c5
003CFF12  45 84 E4                        test r12b, r12b
003CFF15  0F 85 52 02 00 00               jne 0x1403d016d
003CFF1B  85 F6                           test esi, esi
003CFF1D  0F 84 4A 02 00 00               je 0x1403d016d
003CFF23  48 8D 4F 08                     lea rcx, [rdi + 8]
003CFF27  E8 F4 11 F3 FF                  call 0x140301120
003CFF2C  84 C0                           test al, al
003CFF2E  0F 84 39 02 00 00               je 0x1403d016d
003CFF34  48 8D 45 18                     lea rax, [rbp + 0x18]
003CFF38  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003CFF3D  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003CFF41  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003CFF46  48 8D 55 14                     lea rdx, [rbp + 0x14]
003CFF4A  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003CFF4F  48 8D 5D 04                     lea rbx, [rbp + 4]
003CFF53  4C 8D 4D 15                     lea r9, [rbp + 0x15]
003CFF57  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
003CFF5C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003CFF61  4C 8D 47 08                     lea r8, [rdi + 8]
003CFF65  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
003CFF69  49 8B CD                        mov rcx, r13
003CFF6C  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
003CFF73  E8 48 FE F2 FF                  call 0x1402ffdc0
003CFF78  8B 03                           mov eax, dword ptr [rbx]
003CFF7A  F7 D0                           not eax
003CFF7C  23 F0                           and esi, eax
003CFF7E  21 45 00                        and dword ptr [rbp], eax
003CFF81  44 8B BC 24 B8 00 00 00         mov r15d, dword ptr [rsp + 0xb8]
003CFF89  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
003CFF90  E9 D0 FE FF FF                  jmp 0x1403cfe65
003CFF95  E8 EE F7 11 00                  call 0x1404ef788
003CFF9A  85 C0                           test eax, eax
003CFF9C  0F 85 64 FF FF FF               jne 0x1403cff06
003CFFA2  39 44 24 60                     cmp dword ptr [rsp + 0x60], eax
003CFFA6  75 09                           jne 0x1403cffb1
003CFFA8  45 84 E4                        test r12b, r12b
003CFFAB  0F 84 CF 03 00 00               je 0x1403d0380
003CFFB1  41 83 7E 18 00                  cmp dword ptr [r14 + 0x18], 0
003CFFB6  74 C9                           je 0x1403cff81
003CFFB8  8A 9C 24 08 01 00 00            mov bl, byte ptr [rsp + 0x108]
003CFFBF  4C 8D 47 08                     lea r8, [rdi + 8]
003CFFC3  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
003CFFC7  E9 86 8E 31 00                  jmp 0x1406e8e52
003CFFCC  8B F3                           mov esi, ebx
003CFFCE  0B 75 00                        or esi, dword ptr [rbp]
003CFFD1  E9 52 FE FF FF                  jmp 0x1403cfe28
003CFFD6  85 F6                           test esi, esi
003CFFD8  0F 85 79 FE FF FF               jne 0x1403cfe57
003CFFDE  E9 0A FF FF FF                  jmp 0x1403cfeed
003CFFE3  49 8D 46 18                     lea rax, [r14 + 0x18]
003CFFE7  49 8B CF                        mov rcx, r15
003CFFEA  89 18                           mov dword ptr [rax], ebx
003CFFEC  48 8D 40 30                     lea rax, [rax + 0x30]
003CFFF0  48 83 E9 01                     sub rcx, 1
003CFFF4  0F 84 FE FD FF FF               je 0x1403cfdf8
003CFFFA  EB EE                           jmp 0x1403cffea
003CFFFC  49 8D 46 18                     lea rax, [r14 + 0x18]
003D0000  83 38 00                        cmp dword ptr [rax], 0
003D0003  0F 84 E4 FE FF FF               je 0x1403cfeed
003D0009  45 85 FF                        test r15d, r15d
003D000C  0F 84 DB FE FF FF               je 0x1403cfeed
003D0012  45 8B CF                        mov r9d, r15d
003D0015  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
003D0019  33 D2                           xor edx, edx
003D001B  44 8B 18                        mov r11d, dword ptr [rax]
003D001E  B9 01 00 00 00                  mov ecx, 1
003D0023  4D 85 C0                        test r8, r8
003D0026  0F 84 32 03 00 00               je 0x1403d035e
003D002C  85 C9                           test ecx, ecx
003D002E  0F 84 2A 03 00 00               je 0x1403d035e
003D0034  41 85 CB                        test r11d, ecx
003D0037  0F 85 09 03 00 00               jne 0x1403d0346
003D003D  FF C2                           inc edx
003D003F  03 C9                           add ecx, ecx
003D0041  EB E9                           jmp 0x1403d002c
003D0043  3C 06                           cmp al, 6
003D0045  0F 84 13 8F 31 00               je 0x1406e8f5e
003D004B  3C 09                           cmp al, 9
003D004D  0F 85 A8 01 00 00               jne 0x1403d01fb
003D0053  0F B6 47 09                     movzx eax, byte ptr [rdi + 9]
003D0057  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
003D005E  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
003D0062  2B C3                           sub eax, ebx
003D0064  83 F8 08                        cmp eax, 8
003D0067  0F 84 F0 FD FF FF               je 0x1403cfe5d
003D006D  48 83 BC 24 D0 00 00 00 00      cmp qword ptr [rsp + 0xd0], 0
003D0076  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
003D007E  0F 85 92 02 00 00               jne 0x1403d0316
003D0084  49 8B 85 48 04 00 00            mov rax, qword ptr [r13 + 0x448]
003D008B  48 85 C0                        test rax, rax
003D008E  0F 84 C8 00 00 00               je 0x1403d015c
003D0094  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
003D009B  4C 8B 80 50 02 00 00            mov r8, qword ptr [rax + 0x250]
003D00A2  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
003D00A9  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
003D00B0  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
003D00B4  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
003D00B9  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003D00BE  2B D3                           sub edx, ebx
003D00C0  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
003D00C5  83 EA 08                        sub edx, 8
003D00C8  C6 44 24 48 00                  mov byte ptr [rsp + 0x48], 0
003D00CD  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
003D00D1  49 8B 95 08 03 00 00            mov rdx, qword ptr [r13 + 0x308]
003D00D8  8B CB                           mov ecx, ebx
003D00DA  48 83 C1 08                     add rcx, 8
003D00DE  48 03 CF                        add rcx, rdi
003D00E1  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003D00E6  49 8B CD                        mov rcx, r13
003D00E9  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
003D00EE  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
003D00F3  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
003D00F8  4D 8B 07                        mov r8, qword ptr [r15]
003D00FB  E8 D0 EA F2 FF                  call 0x1402febd0
003D0100  83 7C 24 6C 01                  cmp dword ptr [rsp + 0x6c], 1
003D0105  0F 85 76 FE FF FF               jne 0x1403cff81
003D010B  E8 78 F6 11 00                  call 0x1404ef788
003D0110  85 C0                           test eax, eax
003D0112  0F 85 EE FD FF FF               jne 0x1403cff06
003D0118  39 44 24 60                     cmp dword ptr [rsp + 0x60], eax
003D011C  0F 85 9A 02 00 00               jne 0x1403d03bc
003D0122  45 84 E4                        test r12b, r12b
003D0125  0F 85 91 02 00 00               jne 0x1403d03bc
003D012B  85 F6                           test esi, esi
003D012D  0F 84 89 02 00 00               je 0x1403d03bc
003D0133  4C 8D 7F 08                     lea r15, [rdi + 8]
003D0137  49 8B CF                        mov rcx, r15
003D013A  E8 E1 0F F3 FF                  call 0x140301120
003D013F  84 C0                           test al, al
003D0141  0F 85 BF 8C 31 00               jne 0x1406e8e06
003D0147  49 8B CF                        mov rcx, r15
003D014A  E8 A1 0C 00 00                  call 0x1403d0df0
003D014F  84 C0                           test al, al
003D0151  0F 84 65 02 00 00               je 0x1403d03bc
003D0157  E9 DF 8C 31 00                  jmp 0x1406e8e3b
003D015C  45 33 C9                        xor r9d, r9d
003D015F  45 33 C0                        xor r8d, r8d
003D0162  45 33 D2                        xor r10d, r10d
003D0165  45 33 DB                        xor r11d, r11d
003D0168  E9 43 FF FF FF                  jmp 0x1403d00b0
003D016D  85 DB                           test ebx, ebx
003D016F  0F 85 3C 02 00 00               jne 0x1403d03b1
003D0175  45 84 E4                        test r12b, r12b
003D0178  0F 85 3E 02 00 00               jne 0x1403d03bc
003D017E  85 F6                           test esi, esi
003D0180  0F 84 36 02 00 00               je 0x1403d03bc
003D0186  48 8D 4F 08                     lea rcx, [rdi + 8]
003D018A  E8 61 0C 00 00                  call 0x1403d0df0
003D018F  84 C0                           test al, al
003D0191  0F 84 25 02 00 00               je 0x1403d03bc
003D0197  4C 8D 47 08                     lea r8, [rdi + 8]
003D019B  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
003D019F  48 8D 45 16                     lea rax, [rbp + 0x16]
003D01A3  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
003D01AA  48 8D 5D 08                     lea rbx, [rbp + 8]
003D01AE  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
003D01B3  49 8B CD                        mov rcx, r13
003D01B6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D01BB  E8 B0 0A 00 00                  call 0x1403d0c70
003D01C0  E9 B3 FD FF FF                  jmp 0x1403cff78
003D01C5  83 7C 24 64 00                  cmp dword ptr [rsp + 0x64], 0
003D01CA  0F 84 EC 01 00 00               je 0x1403d03bc
003D01D0  E9 3D FD FF FF                  jmp 0x1403cff12
003D01D5  8A 07                           mov al, byte ptr [rdi]
003D01D7  84 C0                           test al, al
003D01D9  0F 84 AD FC FF FF               je 0x1403cfe8c
003D01DF  3C 09                           cmp al, 9
003D01E1  0F 85 76 FC FF FF               jne 0x1403cfe5d
003D01E7  E9 A0 FC FF FF                  jmp 0x1403cfe8c
003D01EC  39 74 24 64                     cmp dword ptr [rsp + 0x64], esi
003D01F0  0F 84 32 FC FF FF               je 0x1403cfe28
003D01F6  E9 24 FC FF FF                  jmp 0x1403cfe1f
003D01FB  80 BC 24 10 01 00 00 00         cmp byte ptr [rsp + 0x110], 0
003D0203  0F 84 54 FC FF FF               je 0x1403cfe5d
003D0209  3C 0A                           cmp al, 0xa
003D020B  0F 85 4C FC FF FF               jne 0x1403cfe5d
003D0211  44 0F 20 C0                     mov rax, cr8
003D0215  3C 02                           cmp al, 2
003D0217  0F 83 40 FC FF FF               jae 0x1403cfe5d
003D021D  0F B6 47 09                     movzx eax, byte ptr [rdi + 9]
003D0221  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
003D0228  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
003D022C  2B C3                           sub eax, ebx
003D022E  83 F8 08                        cmp eax, 8
003D0231  0F 84 26 FC FF FF               je 0x1403cfe5d
003D0237  48 83 BC 24 D0 00 00 00 00      cmp qword ptr [rsp + 0xd0], 0
003D0240  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
003D0248  0F 85 B4 01 00 00               jne 0x1403d0402
003D024E  49 8B 85 48 04 00 00            mov rax, qword ptr [r13 + 0x448]
003D0255  48 85 C0                        test rax, rax
003D0258  0F 84 D7 00 00 00               je 0x1403d0335
003D025E  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
003D0265  4C 8B 80 50 02 00 00            mov r8, qword ptr [rax + 0x250]
003D026C  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
003D0273  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
003D027A  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
003D027E  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
003D0283  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003D0288  2B D3                           sub edx, ebx
003D028A  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
003D028F  83 EA 08                        sub edx, 8
003D0292  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
003D0297  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
003D029B  49 8B 95 08 03 00 00            mov rdx, qword ptr [r13 + 0x308]
003D02A2  8B CB                           mov ecx, ebx
003D02A4  48 83 C1 08                     add rcx, 8
003D02A8  48 03 CF                        add rcx, rdi
003D02AB  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003D02B0  49 8B CD                        mov rcx, r13
003D02B3  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
003D02B8  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
003D02BD  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
003D02C2  4D 8B 07                        mov r8, qword ptr [r15]
003D02C5  E8 06 E9 F2 FF                  call 0x1402febd0
003D02CA  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
003D02CE  FF C0                           inc eax
003D02D0  A9 FD FF FF FF                  test eax, 0xfffffffd
003D02D5  0F 85 A6 FC FF FF               jne 0x1403cff81
003D02DB  8A 84 24 08 01 00 00            mov al, byte ptr [rsp + 0x108]
003D02E2  4C 8D 47 08                     lea r8, [rdi + 8]
003D02E6  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003D02EA  41 B1 01                        mov r9b, 1
003D02ED  33 D2                           xor edx, edx
003D02EF  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003D02F4  49 8B CD                        mov rcx, r13
003D02F7  E8 34 01 00 00                  call 0x1403d0430
003D02FC  84 C0                           test al, al
003D02FE  0F 84 7D FC FF FF               je 0x1403cff81
003D0304  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
003D0307  41 23 4E 18                     and ecx, dword ptr [r14 + 0x18]
003D030B  0F 85 EE 8C 31 00               jne 0x1406e8fff
003D0311  E9 6B FC FF FF                  jmp 0x1403cff81
003D0316  49 83 3F 00                     cmp qword ptr [r15], 0
003D031A  0F 85 64 FD FF FF               jne 0x1403d0084
003D0320  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
003D0328  49 8B D7                        mov rdx, r15
003D032B  E8 54 2B F3 FF                  call 0x140302e84
003D0330  E9 4F FD FF FF                  jmp 0x1403d0084
003D0335  45 33 C9                        xor r9d, r9d
003D0338  45 33 C0                        xor r8d, r8d
003D033B  45 33 D2                        xor r10d, r10d
003D033E  45 33 DB                        xor r11d, r11d
003D0341  E9 34 FF FF FF                  jmp 0x1403d027a
003D0346  41 83 3C 90 00                  cmp dword ptr [r8 + rdx*4], 0
003D034B  0F 85 EC FC FF FF               jne 0x1403d003d
003D0351  41 C7 04 90 00 00 80 00         mov dword ptr [r8 + rdx*4], 0x800000
003D0359  E9 DF FC FF FF                  jmp 0x1403d003d
003D035E  48 83 C0 30                     add rax, 0x30
003D0362  49 83 E9 01                     sub r9, 1
003D0366  0F 85 A9 FC FF FF               jne 0x1403d0015
003D036C  E9 7C FB FF FF                  jmp 0x1403cfeed
003D0371  39 74 24 60                     cmp dword ptr [rsp + 0x60], esi
003D0375  0F 85 AD FA FF FF               jne 0x1403cfe28
003D037B  E9 9F FA FF FF                  jmp 0x1403cfe1f
003D0380  85 F6                           test esi, esi
003D0382  0F 84 29 FC FF FF               je 0x1403cffb1
003D0388  4C 8D 7F 08                     lea r15, [rdi + 8]
003D038C  49 8B CF                        mov rcx, r15
003D038F  E8 8C 0D F3 FF                  call 0x140301120
003D0394  84 C0                           test al, al
003D0396  0F 85 6A 8A 31 00               jne 0x1406e8e06
003D039C  49 8B CF                        mov rcx, r15
003D039F  E8 4C 0A 00 00                  call 0x1403d0df0
003D03A4  84 C0                           test al, al
003D03A6  0F 84 05 FC FF FF               je 0x1403cffb1
003D03AC  E9 8A 8A 31 00                  jmp 0x1406e8e3b
003D03B1  83 7C 24 64 00                  cmp dword ptr [rsp + 0x64], 0
003D03B6  0F 85 B9 FD FF FF               jne 0x1403d0175
003D03BC  41 83 7E 18 00                  cmp dword ptr [r14 + 0x18], 0
003D03C1  0F 84 BA FB FF FF               je 0x1403cff81
003D03C7  E9 77 8A 31 00                  jmp 0x1406e8e43
003D03CC  0F B6 47 0D                     movzx eax, byte ptr [rdi + 0xd]
003D03D0  45 33 C9                        xor r9d, r9d
003D03D3  8A 9C 24 08 01 00 00            mov bl, byte ptr [rsp + 0x108]
003D03DA  48 83 C0 05                     add rax, 5
003D03DE  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
003D03E2  33 D2                           xor edx, edx
003D03E4  49 8B CD                        mov rcx, r13
003D03E7  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
003D03EC  4C 8D 04 87                     lea r8, [rdi + rax*4]
003D03F0  E8 3B 00 00 00                  call 0x1403d0430
003D03F5  84 C0                           test al, al
003D03F7  0F 84 84 FB FF FF               je 0x1403cff81
003D03FD  E9 55 8A 31 00                  jmp 0x1406e8e57
003D0402  49 83 3F 00                     cmp qword ptr [r15], 0
003D0406  0F 85 42 FE FF FF               jne 0x1403d024e
003D040C  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
003D0414  49 8B D7                        mov rdx, r15
003D0417  E8 68 2A F3 FF                  call 0x140302e84
003D041C  E9 2D FE FF FF                  jmp 0x1403d024e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepNormalAccessCheckEx(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, __int64 a9, __int64 a10, unsigned __int8 a11, unsigned __int8 a12, unsigned __int8 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int8 v_stack_m80;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p6C;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pC8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (112);
    v_rsi = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 200))) & (0x2000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 200))))) & (0x4000ULL));
    v_stack_m48 = (unsigned int)(result);
    v_stack_p20 = (unsigned int)(*(unsigned __int16 *)(a4 + 4));
    v_stack_m44 = a1;
    if ((unsigned int)((unsigned int)(a8)) != 0) goto loc_003CFFE3;
loc_003CFDF8:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_003D0371;
    if (v_stack_m48 != 0) goto loc_003D01EC;
loc_003CFE1F:
    if (a11 == 0) goto loc_003CFFCC;
loc_003CFE28:
    result = 0;
    v_stack_p10 = 0;
    v_rdi = (a4) + (8);
    v_stack_p38 = 0;
loc_003CFE43:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_003CFEE7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24))) == 0) goto loc_003CFFD6;
loc_003CFE57:
    if (((*(unsigned __int8 *)(v_rdi + 1)) & (8)) == 0) goto loc_003CFE84;
loc_003CFE5D:
loc_003CFE65:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p10)) + 1);
    v_rdi = (v_rdi) + (*(unsigned __int16 *)(v_rdi + 2));
    v_stack_p10 = (unsigned int)(v_r15);
    goto loc_003CFE43;
loc_003CFE84:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24))) == 0) goto loc_003D01D5;
loc_003CFE8C:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) == 0) goto loc_003CFF95;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) == 4) goto loc_003D03CC;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) != 1) goto loc_003D0043;
    v_stack_m80 = a12;
    a2 = 0;
    v_stack_m88 = a11;
    result = SepSidInToken(0, a2, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_003CFF81;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a9 + 24))) & (*(unsigned int *)(v_rdi + 4)));
    if (condition_is_equal) goto loc_003CFF81;
loc_003CFEE7:
    if (condition_is_equal) goto loc_003CFFFC;
loc_003CFEED:
    v_rsp = (v_rsp) + (112);
    return result;
loc_003CFF06:
    if ((unsigned int)((unsigned int)(v_stack_p60)) != 0) goto loc_003D01C5;
loc_003CFF12:
    if (a11 != 0) goto loc_003D016D;
    if (0 == 0) goto loc_003D016D;
    result = SepIsPackageSid(v_rdi + 8, a2, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_003D016D;
    v_stack_p40 = a14 + 24;
    v_stack_p38 = a14 + 16;
    v_stack_p30 = a14 + 20;
    v_stack_p28 = a14 + 4;
    v_stack_p20 = a14 + 21;
    result = SepMatchPackage(0, (unsigned int)(a7), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
loc_003CFF78:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a14 + 4))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(result)));
loc_003CFF81:
    goto loc_003CFE65;
loc_003CFF95:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)(v_stack_pC8), (unsigned int)(a7), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    if ((unsigned int)(result) != 0) goto loc_003CFF06;
    if (v_stack_p60 != ((unsigned int)(result))) goto loc_003CFFB1;
    if (a11 == 0) goto loc_003D0380;
loc_003CFFB1:
    if ((*(unsigned int *)(a9 + 24)) == 0) goto loc_003CFF81;
    v_stack_p28 = a12;
loc_003CFFCC:
    v_rsi = (unsigned int)(((unsigned int)(a12)) | (*(unsigned int *)(a14)));
    goto loc_003CFE28;
loc_003CFFD6:
    if ((unsigned int)(v_rsi) != 0) goto loc_003CFE57;
    goto loc_003CFEED;
loc_003CFFE3:
loc_003CFFEA:
    *(unsigned int *)(a9 + 24) = a12;
    a1 = ((unsigned int)(v_stack_pB8)) - (1);
    if (condition_is_equal) goto loc_003CFDF8;
    goto loc_003CFFEA;
loc_003CFFFC:
    if ((*(unsigned int *)(a9 + 24)) == 0) goto loc_003CFEED;
    if ((unsigned int)((unsigned int)(v_stack_pB8)) == 0) goto loc_003CFEED;
loc_003D0015:
    a2 = 0;
    if (*(unsigned __int64 *)(a9 + 24 + 16) == 0) goto loc_003D035E;
loc_003D002C:
    if (1 == 0) goto loc_003D035E;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a9 + 24)))) & (1)) != 0) goto loc_003D0346;
loc_003D003D:
    a2 = (unsigned int)((a2) + 1);
    a1 = (unsigned int)((1) + (1));
    goto loc_003D002C;
loc_003D0043:
    if (((unsigned __int8)(a9 + 24)) != 9) goto loc_003D01FB;
    result = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    if (((unsigned int)(result)) == 8) goto loc_003CFE5D;
    if (a5 != 0) goto loc_003D0316;
loc_003D0084:
    if (*(unsigned __int64 *)(a2 + 1096) == 0) goto loc_003D015C;
loc_003D00B0:
    v_stack_p58 = v_stack_p6C;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    v_stack_p50 = a11;
    a2 = (unsigned int)((a2) - (8));
    v_stack_p48 = 0;
    v_stack_p40 = (unsigned int)(a2);
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8))) + (8);
    a1 = (a1) + (v_rdi);
    v_stack_p38 = a1;
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 600);
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 584);
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 592);
    result = AuthzBasepEvaluateAceCondition(a2, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 576));
    if (v_stack_p6C != 1) goto loc_003CFF81;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a2, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 576));
    if ((unsigned int)(result) != 0) goto loc_003CFF06;
    if (v_stack_p60 != ((unsigned int)(result))) goto loc_003D03BC;
    if (a11 != 0) goto loc_003D03BC;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D03BC;
    result = SepIsPackageSid(v_rdi + 8, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 576));
    result = SepIsCapabilitySid(v_rdi + 8, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 576));
    if ((unsigned __int8)(result) == 0) goto loc_003D03BC;
loc_003D015C:
    a4 = 0;
    a3 = 0;
    v_r10 = 0;
    v_r11 = 0;
    goto loc_003D00B0;
loc_003D016D:
    if ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8) != 0) goto loc_003D03B1;
loc_003D0175:
    if (a11 != 0) goto loc_003D03BC;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D03BC;
    result = SepIsCapabilitySid(v_rdi + 8, *(unsigned __int64 *)(a2 + 776), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D03BC;
    v_stack_p28 = a14 + 8;
    v_stack_p20 = a14 + 22;
    result = SepMatchCapability(a2, (unsigned int)(a7), v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    goto loc_003CFF78;
loc_003D01C5:
    if (v_stack_p64 == 0) goto loc_003D03BC;
    goto loc_003CFF12;
loc_003D01D5:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) == 0) goto loc_003CFE8C;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) != 9) goto loc_003CFE5D;
    goto loc_003CFE8C;
loc_003D01EC:
    if (v_stack_p64 == ((unsigned int)(v_rsi))) goto loc_003CFE28;
    goto loc_003CFE1F;
loc_003D01FB:
    if (a13 == 0) goto loc_003CFE5D;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) != 10) goto loc_003CFE5D;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_003CFE5D;
    result = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    if (((unsigned int)(result)) == 8) goto loc_003CFE5D;
    if (a5 != 0) goto loc_003D0402;
loc_003D024E:
    if (*(unsigned __int64 *)(a2 + 1096) == 0) goto loc_003D0335;
loc_003D027A:
    v_stack_p58 = v_stack_p6C;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    v_stack_p50 = a11;
    a2 = (unsigned int)((a2) - (8));
    v_stack_p48 = 1;
    v_stack_p40 = (unsigned int)(a2);
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8))) + (8);
    a1 = (a1) + (v_rdi);
    v_stack_p38 = a1;
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 600);
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 584);
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 592);
    result = AuthzBasepEvaluateAceCondition(a2, *(unsigned __int64 *)(a2 + 776), *(unsigned __int64 *)(a6), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1096) + 576));
    result = (unsigned int)(((unsigned int)(v_stack_p6C)) + 1);
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_003CFF81;
    v_stack_p28 = a12;
    a2 = 0;
    v_stack_p20 = a11;
    result = SepSidInToken(0, a2, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_003CFF81;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 4))) & (*(unsigned int *)(a9 + 24)));
    goto loc_003CFF81;
loc_003D0316:
    if ((*(unsigned __int64 *)(a6)) != 0) goto loc_003D0084;
    result = AuthzBasepInitializeResourceClaimsFromSacl(a5, a6, v_rdi + 8, 1);
    goto loc_003D0084;
loc_003D0335:
    a4 = 0;
    a3 = 0;
    v_r10 = 0;
    v_r11 = 0;
    goto loc_003D027A;
loc_003D0346:
    if ((*(unsigned int *)(a3 + a6 * 4)) != 0) goto loc_003D003D;
    *(unsigned int *)(a3 + a6 * 4) = 0x800000ULL;
    goto loc_003D003D;
loc_003D035E:
    result = (result) + (48);
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_003D0015;
    goto loc_003CFEED;
loc_003D0371:
    if (v_stack_p60 != ((unsigned int)(v_rsi))) goto loc_003CFE28;
    goto loc_003CFE1F;
loc_003D0380:
    if ((unsigned int)(v_rsi) == 0) goto loc_003CFFB1;
    result = SepIsPackageSid(v_rdi + 8, a6, a3, a4);
    result = SepIsCapabilitySid(v_rdi + 8, a6, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003CFFB1;
loc_003D03B1:
    if (v_stack_p64 != 0) goto loc_003D0175;
loc_003D03BC:
    if ((*(unsigned int *)(a9 + 24)) == 0) goto loc_003CFF81;
loc_003D03CC:
    a4 = 0;
    result = (*(unsigned __int8 *)(v_rdi + 13)) + (5);
    v_stack_p28 = a12;
    a2 = 0;
    v_stack_p20 = a11;
    result = SepSidInToken(0, a2, v_rdi + result * 4, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003CFF81;
loc_003D0402:
    if ((*(unsigned __int64 *)(v_rdi + 8)) != 0) goto loc_003D024E;
    result = AuthzBasepInitializeResourceClaimsFromSacl(a5, v_rdi + 8, v_rdi + result * 4, a4);
    goto loc_003D024E;
}
```

## 5. (Beta) C Style

```c
int64_t SepNormalAccessCheckEx(int32_t Arg1, void *Arg2, int64_t Arg3, void *Arg4, int64_t Arg5, void *Arg6, uint32_t Arg7, uint32_t Arg8, void *Arg9, uint64_t Arg10, uint8_t Arg11, uint8_t Arg12, uint8_t Arg13, void *Arg14)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg14 = (uint8_t *)Arg14;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint8_t v_stack_m80;
    uint8_t v_stack_m88;
    uint32_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p48;
    uint8_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p6C;
    uint64_t v_stack_p8;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pC8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (112);
    local_rsi = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0xC8))) & (0x2000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC8))))) & (0x4000ULL));
    v_stack_m48 = (uint32_t)(result);
    v_stack_p20 = (uint32_t)(*(uint16_t *)(arg4 + 0x4));
    v_stack_m44 = Arg1;
    if ((uint32_t)((uint32_t)(Arg8)) != 0) goto loc_003CFFE3;
loc_003CFDF8:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003D0371;
    if (v_stack_m48 != 0) goto loc_003D01EC;
loc_003CFE1F:
    if (Arg11 == 0) goto loc_003CFFCC;
loc_003CFE28:
    result = 0;
    v_stack_p10 = 0;
    local_rdi = (Arg4) + (8);
    v_stack_p38 = 0;
loc_003CFE43:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_003CFEE7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18))) == 0) goto loc_003CFFD6;
loc_003CFE57:
    if (((*(uint8_t *)(local_rdi + 0x1)) & (8)) == 0) goto loc_003CFE84;
loc_003CFE5D:
loc_003CFE65:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p10)) + 1);
    local_rdi = (local_rdi) + (*(uint16_t *)(local_rdi + 0x2));
    v_stack_p10 = (uint32_t)(local_r15);
    goto loc_003CFE43;
loc_003CFE84:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18))) == 0) goto loc_003D01D5;
loc_003CFE8C:
    if ((uint8_t)(*(uint8_t *)(local_rdi)) == 0) goto loc_003CFF95;
    if (((uint8_t)(*(uint8_t *)(local_rdi))) == 4) goto loc_003D03CC;
    if (((uint8_t)(*(uint8_t *)(local_rdi))) != 1) goto loc_003D0043;
    v_stack_m80 = Arg12;
    Arg2 = 0;
    v_stack_m88 = Arg11;
    result = SepSidInToken(0, Arg2, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_003CFF81;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg9 + 0x18))) & (*(uint32_t *)(local_rdi + 0x4)));
    if (condition_is_equal) goto loc_003CFF81;
loc_003CFEE7:
    if (condition_is_equal) goto loc_003CFFFC;
loc_003CFEED:
    local_rsp = (local_rsp) + (112);
    return result;
loc_003CFF06:
    if ((uint32_t)((uint32_t)(v_stack_p60)) != 0) goto loc_003D01C5;
loc_003CFF12:
    if (Arg11 != 0) goto loc_003D016D;
    if (0 == 0) goto loc_003D016D;
    result = SepIsPackageSid(local_rdi + 8, Arg2, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_003D016D;
    v_stack_p40 = Arg14 + 24;
    v_stack_p38 = Arg14 + 16;
    v_stack_p30 = Arg14 + 20;
    v_stack_p28 = Arg14 + 4;
    v_stack_p20 = Arg14 + 21;
    result = SepMatchPackage(0, (uint32_t)(Arg7), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
loc_003CFF78:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg14 + 0x4))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(result)));
loc_003CFF81:
    goto loc_003CFE65;
loc_003CFF95:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)(v_stack_pC8), (uint32_t)(Arg7), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    if ((uint32_t)(result) != 0) goto loc_003CFF06;
    if (v_stack_p60 != ((uint32_t)(result))) goto loc_003CFFB1;
    if (Arg11 == 0) goto loc_003D0380;
loc_003CFFB1:
    if ((*(uint32_t *)(arg9 + 0x18)) == 0) goto loc_003CFF81;
    v_stack_p28 = Arg12;
loc_003CFFCC:
    local_rsi = (uint32_t)(((uint32_t)(Arg12)) | (*(uint32_t *)(arg14)));
    goto loc_003CFE28;
loc_003CFFD6:
    if ((uint32_t)(local_rsi) != 0) goto loc_003CFE57;
    goto loc_003CFEED;
loc_003CFFE3:
loc_003CFFEA:
    *(uint32_t *)(arg9 + 0x18) = Arg12;
    Arg1 = ((uint32_t)(v_stack_pB8)) - (1);
    if (condition_is_equal) goto loc_003CFDF8;
    goto loc_003CFFEA;
loc_003CFFFC:
    if ((*(uint32_t *)(arg9 + 0x18)) == 0) goto loc_003CFEED;
    if ((uint32_t)((uint32_t)(v_stack_pB8)) == 0) goto loc_003CFEED;
loc_003D0015:
    Arg2 = 0;
    if (*(uint64_t *)(arg9 + 0x18 + 0x10) == 0) goto loc_003D035E;
loc_003D002C:
    if (1 == 0) goto loc_003D035E;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x18)))) & (1)) != 0) goto loc_003D0346;
loc_003D003D:
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (uint32_t)((1) + (1));
    goto loc_003D002C;
loc_003D0043:
    if (((uint8_t)(Arg9 + 24)) != 9) goto loc_003D01FB;
    result = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    if (((uint32_t)(result)) == 8) goto loc_003CFE5D;
    if (Arg5 != 0) goto loc_003D0316;
loc_003D0084:
    if (*(uint64_t *)(arg2 + 0x448) == 0) goto loc_003D015C;
loc_003D00B0:
    v_stack_p58 = v_stack_p6C;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    v_stack_p50 = Arg11;
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_p48 = 0;
    v_stack_p40 = (uint32_t)(Arg2);
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8))) + (8);
    Arg1 = (Arg1) + (local_rdi);
    v_stack_p38 = Arg1;
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x258);
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x248);
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x250);
    result = AuthzBasepEvaluateAceCondition(Arg2, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x240));
    if (v_stack_p6C != 1) goto loc_003CFF81;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg2, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x240));
    if ((uint32_t)(result) != 0) goto loc_003CFF06;
    if (v_stack_p60 != ((uint32_t)(result))) goto loc_003D03BC;
    if (Arg11 != 0) goto loc_003D03BC;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D03BC;
    result = SepIsPackageSid(local_rdi + 8, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x240));
    result = SepIsCapabilitySid(local_rdi + 8, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x240));
    if ((uint8_t)(result) == 0) goto loc_003D03BC;
loc_003D015C:
    Arg4 = 0;
    Arg3 = 0;
    local_r10 = 0;
    local_r11 = 0;
    goto loc_003D00B0;
loc_003D016D:
    if ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8) != 0) goto loc_003D03B1;
loc_003D0175:
    if (Arg11 != 0) goto loc_003D03BC;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D03BC;
    result = SepIsCapabilitySid(local_rdi + 8, *(uint64_t *)(arg2 + 0x308), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003D03BC;
    v_stack_p28 = Arg14 + 8;
    v_stack_p20 = Arg14 + 22;
    result = SepMatchCapability(Arg2, (uint32_t)(Arg7), local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    goto loc_003CFF78;
loc_003D01C5:
    if (v_stack_p64 == 0) goto loc_003D03BC;
    goto loc_003CFF12;
loc_003D01D5:
    if ((uint8_t)(*(uint8_t *)(local_rdi)) == 0) goto loc_003CFE8C;
    if (((uint8_t)(*(uint8_t *)(local_rdi))) != 9) goto loc_003CFE5D;
    goto loc_003CFE8C;
loc_003D01EC:
    if (v_stack_p64 == ((uint32_t)(local_rsi))) goto loc_003CFE28;
    goto loc_003CFE1F;
loc_003D01FB:
    if (Arg13 == 0) goto loc_003CFE5D;
    if (((uint8_t)(*(uint8_t *)(local_rdi))) != 10) goto loc_003CFE5D;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_003CFE5D;
    result = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    if (((uint32_t)(result)) == 8) goto loc_003CFE5D;
    if (Arg5 != 0) goto loc_003D0402;
loc_003D024E:
    if (*(uint64_t *)(arg2 + 0x448) == 0) goto loc_003D0335;
loc_003D027A:
    v_stack_p58 = v_stack_p6C;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    v_stack_p50 = Arg11;
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_p48 = 1;
    v_stack_p40 = (uint32_t)(Arg2);
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8))) + (8);
    Arg1 = (Arg1) + (local_rdi);
    v_stack_p38 = Arg1;
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x258);
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x248);
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x250);
    result = AuthzBasepEvaluateAceCondition(Arg2, *(uint64_t *)(arg2 + 0x308), *(uint64_t *)(arg6), *(uint64_t *)(*(uint64_t *)(arg2 + 0x448) + 0x240));
    result = (uint32_t)(((uint32_t)(v_stack_p6C)) + 1);
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_003CFF81;
    v_stack_p28 = Arg12;
    Arg2 = 0;
    v_stack_p20 = Arg11;
    result = SepSidInToken(0, Arg2, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_003CFF81;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x4))) & (*(uint32_t *)(arg9 + 0x18)));
    goto loc_003CFF81;
loc_003D0316:
    if ((*(uint64_t *)(arg6)) != 0) goto loc_003D0084;
    result = AuthzBasepInitializeResourceClaimsFromSacl(Arg5, Arg6, local_rdi + 8, 1);
    goto loc_003D0084;
loc_003D0335:
    Arg4 = 0;
    Arg3 = 0;
    local_r10 = 0;
    local_r11 = 0;
    goto loc_003D027A;
loc_003D0346:
    if ((*(uint32_t *)(Arg3 + arg6 * 4)) != 0) goto loc_003D003D;
    *(uint32_t *)(Arg3 + arg6 * 4) = 0x800000ULL;
    goto loc_003D003D;
loc_003D035E:
    result = (result) + (48);
    Arg4 = (Arg4) - (1);
    if (condition_is_not_equal) goto loc_003D0015;
    goto loc_003CFEED;
loc_003D0371:
    if (v_stack_p60 != ((uint32_t)(local_rsi))) goto loc_003CFE28;
    goto loc_003CFE1F;
loc_003D0380:
    if ((uint32_t)(local_rsi) == 0) goto loc_003CFFB1;
    result = SepIsPackageSid(local_rdi + 8, Arg6, Arg3, Arg4);
    result = SepIsCapabilitySid(local_rdi + 8, Arg6, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003CFFB1;
loc_003D03B1:
    if (v_stack_p64 != 0) goto loc_003D0175;
loc_003D03BC:
    if ((*(uint32_t *)(arg9 + 0x18)) == 0) goto loc_003CFF81;
loc_003D03CC:
    Arg4 = 0;
    result = (*(uint8_t *)(local_rdi + 0xD)) + (5);
    v_stack_p28 = Arg12;
    Arg2 = 0;
    v_stack_p20 = Arg11;
    result = SepSidInToken(0, Arg2, local_rdi + result * 4, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003CFF81;
loc_003D0402:
    if ((*(uint64_t *)(local_rdi + 0x8)) != 0) goto loc_003D024E;
    result = AuthzBasepInitializeResourceClaimsFromSacl(Arg5, local_rdi + 8, local_rdi + result * 4, Arg4);
    goto loc_003D024E;
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
| `Arg4` | `+ 0xD` | `8` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R` |
| `Arg9` | `+ 0x0` | `32` | `W` |
| `Arg9` | `+ 0x10` | `64` | `R` |
| `Arg9` | `+ 0x18` | `32` | `R` |
| `Arg9` | `+ 0x18` | `64` | `R` |
| `Arg9` | `+ 0x30` | `64` | `R` |
| `Arg14` | `+ 0x0` | `32` | `R` |
| `Arg14` | `+ 0x0` | `32` | `R/W` |
| `Arg14` | `+ 0x4` | `64` | `R` |
| `Arg14` | `+ 0x8` | `64` | `R` |
| `Arg14` | `+ 0x10` | `64` | `R` |
| `Arg14` | `+ 0x14` | `64` | `R` |
| `Arg14` | `+ 0x15` | `64` | `R` |
| `Arg14` | `+ 0x16` | `64` | `R` |
| `Arg14` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CFD8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
