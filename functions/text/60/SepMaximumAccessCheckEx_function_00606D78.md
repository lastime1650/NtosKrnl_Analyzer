# SepMaximumAccessCheckEx

- RVA: `0x00606D78`–`0x00607502` (길이 `1,930` bytes)
- VA: `0x0000000140606D78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D0F2C`
- 디코드: `469`개 명령, `1,930/1,930` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00606DFC` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x00606E5F` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00606E84` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x00606EC7` → [SepMatchPackage](../2F/SepMatchPackage_function_002FFDC0.md) (function, `0x002FFDC0`)
- `0x00606EDA` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x00606F06` → [SepMatchCapability](../3D/SepMatchCapability_function_003D0C70.md) (function, `0x003D0C70`)
- `0x00606F28` → [SepIsPackageSid](../30/SepIsPackageSid_function_00301120.md) (function, `0x00301120`)
- `0x00606F90` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00607010` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x0060702E` → [AuthzBasepObjectInTypeList](../4B/AuthzBasepObjectInTypeList_function_004B8FF4.md) (function, `0x004B8FF4`)
- `0x00607081` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x006070C4` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00607112` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x0060716F` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x006071B9` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x006071D1` → [AuthzBasepObjectInTypeList](../4B/AuthzBasepObjectInTypeList_function_004B8FF4.md) (function, `0x004B8FF4`)
- `0x00607226` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x006072B4` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x006072C4` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x006072F9` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00607320` → [AuthzBasepAddAccessTypeList](../3D/AuthzBasepAddAccessTypeList_function_003D196C.md) (function, `0x003D196C`)
- `0x00607349` → [SepIsCapabilitySid](../3D/SepIsCapabilitySid_function_003D0DF0.md) (function, `0x003D0DF0`)
- `0x006073B0` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x0060743E` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x0060746C` → [SepSidInToken](../3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x0060748F` → [AuthzBasepAddAccessTypeList](../3D/AuthzBasepAddAccessTypeList_function_003D196C.md) (function, `0x003D196C`)

### Direct callers
- [sub_006E89DA](../6E/Unknown_function_006E89DA.md) at `0x006E8BEF`
- [sub_006E89DA](../6E/Unknown_function_006E89DA.md) at `0x006E8CB6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00606D78  48 8B C4                        mov rax, rsp
00606D7B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00606D7F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00606D83  53                              push rbx
00606D84  55                              push rbp
00606D85  56                              push rsi
00606D86  57                              push rdi
00606D87  41 54                           push r12
00606D89  41 55                           push r13
00606D8B  41 56                           push r14
00606D8D  41 57                           push r15
00606D8F  48 83 EC 78                     sub rsp, 0x78
00606D93  83 60 18 00                     and dword ptr [rax + 0x18], 0
00606D97  49 8B F8                        mov rdi, r8
00606D9A  83 60 A8 00                     and dword ptr [rax - 0x58], 0
00606D9E  4C 8B F9                        mov r15, rcx
00606DA1  8B 99 C8 00 00 00               mov ebx, dword ptr [rcx + 0xc8]
00606DA7  8B C3                           mov eax, ebx
00606DA9  44 8A B4 24 10 01 00 00         mov r14b, byte ptr [rsp + 0x110]
00606DB1  25 00 40 00 00                  and eax, 0x4000
00606DB6  4C 8B AC 24 F8 00 00 00         mov r13, qword ptr [rsp + 0xf8]
00606DBE  81 E3 00 20 00 00               and ebx, 0x2000
00606DC4  8B AC 24 F0 00 00 00            mov ebp, dword ptr [rsp + 0xf0]
00606DCB  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
00606DD2  89 9C 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], ebx
00606DD9  45 84 F6                        test r14b, r14b
00606DDC  74 46                           je 0x140606e24
00606DDE  85 ED                           test ebp, ebp
00606DE0  74 42                           je 0x140606e24
00606DE2  4D 8D 5D 1C                     lea r11, [r13 + 0x1c]
00606DE6  8B DD                           mov ebx, ebp
00606DE8  4D 8B 4B 0C                     mov r9, qword ptr [r11 + 0xc]
00606DEC  45 33 C0                        xor r8d, r8d
00606DEF  41 8B 0B                        mov ecx, dword ptr [r11]
00606DF2  BA 00 00 80 00                  mov edx, 0x800000
00606DF7  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00606DFC  E8 7F 8B E2 FF                  call 0x14042f980
00606E01  41 8B 0B                        mov ecx, dword ptr [r11]
00606E04  45 21 03                        and dword ptr [r11], r8d
00606E07  41 89 4B FC                     mov dword ptr [r11 - 4], ecx
00606E0B  4D 8D 5B 30                     lea r11, [r11 + 0x30]
00606E0F  48 83 EB 01                     sub rbx, 1
00606E13  75 D3                           jne 0x140606de8
00606E15  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00606E1C  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
00606E24  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
00606E28  45 33 E4                        xor r12d, r12d
00606E2B  48 83 C7 08                     add rdi, 8
00606E2F  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00606E33  44 89 A4 24 10 01 00 00         mov dword ptr [rsp + 0x110], r12d
00606E3B  85 C0                           test eax, eax
00606E3D  0F 84 81 06 00 00               je 0x1406074c4
00606E43  48 8B B4 24 28 01 00 00         mov rsi, qword ptr [rsp + 0x128]
00606E4B  F6 47 01 08                     test byte ptr [rdi + 1], 8
00606E4F  0F 85 46 06 00 00               jne 0x14060749b
00606E55  8A 07                           mov al, byte ptr [rdi]
00606E57  84 C0                           test al, al
00606E59  0F 85 53 01 00 00               jne 0x140606fb2
00606E5F  E8 24 89 EE FF                  call 0x1404ef788
00606E64  85 C0                           test eax, eax
00606E66  0F 85 A1 00 00 00               jne 0x140606f0d
00606E6C  85 DB                           test ebx, ebx
00606E6E  0F 85 69 04 00 00               jne 0x1406072dd
00606E74  45 84 F6                        test r14b, r14b
00606E77  0F 85 60 04 00 00               jne 0x1406072dd
00606E7D  4C 8D 67 08                     lea r12, [rdi + 8]
00606E81  49 8B CC                        mov rcx, r12
00606E84  E8 97 A2 CF FF                  call 0x140301120
00606E89  84 C0                           test al, al
00606E8B  74 4A                           je 0x140606ed7
00606E8D  4C 8D 46 15                     lea r8, [rsi + 0x15]
00606E91  48 8D 46 18                     lea rax, [rsi + 0x18]
00606E95  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00606E9A  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00606E9E  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00606EA3  48 8D 56 14                     lea rdx, [rsi + 0x14]
00606EA7  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00606EAC  48 8D 5E 04                     lea rbx, [rsi + 4]
00606EB0  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00606EB5  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00606EBA  4D 8B C4                        mov r8, r12
00606EBD  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
00606EC1  83 CA FF                        or edx, 0xffffffff
00606EC4  49 8B CF                        mov rcx, r15
00606EC7  E8 F4 8E CF FF                  call 0x1402ffdc0
00606ECC  8B 03                           mov eax, dword ptr [rbx]
00606ECE  F7 D0                           not eax
00606ED0  21 06                           and dword ptr [rsi], eax
00606ED2  E9 BD 05 00 00                  jmp 0x140607494
00606ED7  49 8B CC                        mov rcx, r12
00606EDA  E8 11 9F DC FF                  call 0x1403d0df0
00606EDF  84 C0                           test al, al
00606EE1  0F 84 EE 03 00 00               je 0x1406072d5
00606EE7  4D 8B C4                        mov r8, r12
00606EEA  44 8B 4F 04                     mov r9d, dword ptr [rdi + 4]
00606EEE  48 8D 46 16                     lea rax, [rsi + 0x16]
00606EF2  48 8D 5E 08                     lea rbx, [rsi + 8]
00606EF6  83 CA FF                        or edx, 0xffffffff
00606EF9  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00606EFE  49 8B CF                        mov rcx, r15
00606F01  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00606F06  E8 65 9D DC FF                  call 0x1403d0c70
00606F0B  EB BF                           jmp 0x140606ecc
00606F0D  85 DB                           test ebx, ebx
00606F0F  74 0A                           je 0x140606f1b
00606F11  83 BC 24 E8 00 00 00 00         cmp dword ptr [rsp + 0xe8], 0
00606F19  74 59                           je 0x140606f74
00606F1B  45 84 F6                        test r14b, r14b
00606F1E  0F 85 06 04 00 00               jne 0x14060732a
00606F24  48 8D 4F 08                     lea rcx, [rdi + 8]
00606F28  E8 F3 A1 CF FF                  call 0x140301120
00606F2D  84 C0                           test al, al
00606F2F  0F 84 F5 03 00 00               je 0x14060732a
00606F35  48 8D 46 18                     lea rax, [rsi + 0x18]
00606F39  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00606F3E  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00606F42  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00606F47  48 8D 56 14                     lea rdx, [rsi + 0x14]
00606F4B  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00606F50  48 8D 5E 04                     lea rbx, [rsi + 4]
00606F54  4C 8D 4E 15                     lea r9, [rsi + 0x15]
00606F58  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00606F5D  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00606F62  4C 8D 47 08                     lea r8, [rdi + 8]
00606F66  E9 52 FF FF FF                  jmp 0x140606ebd
00606F6B  4C 8D 47 08                     lea r8, [rdi + 8]
00606F6F  E9 76 FF FF FF                  jmp 0x140606eea
00606F74  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00606F7B  4C 8D 47 08                     lea r8, [rdi + 8]
00606F7F  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00606F83  45 33 C9                        xor r9d, r9d
00606F86  33 D2                           xor edx, edx
00606F88  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00606F8D  49 8B CF                        mov rcx, r15
00606F90  E8 9B 94 DC FF                  call 0x1403d0430
00606F95  84 C0                           test al, al
00606F97  0F 84 FE 04 00 00               je 0x14060749b
00606F9D  44 8B 8C 24 10 01 00 00         mov r9d, dword ptr [rsp + 0x110]
00606FA5  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00606FAD  E9 5F 03 00 00                  jmp 0x140607311
00606FB2  3C 05                           cmp al, 5
00606FB4  0F 85 E1 00 00 00               jne 0x14060709b
00606FBA  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00606FBD  8B C1                           mov eax, ecx
00606FBF  83 E0 01                        and eax, 1
00606FC2  0F 84 88 00 00 00               je 0x140607050
00606FC8  48 8D 5F 0C                     lea rbx, [rdi + 0xc]
00606FCC  48 85 DB                        test rbx, rbx
00606FCF  74 7F                           je 0x140607050
00606FD1  83 BC 24 00 01 00 00 00         cmp dword ptr [rsp + 0x100], 0
00606FD9  0F 84 B5 04 00 00               je 0x140607494
00606FDF  83 E1 02                        and ecx, 2
00606FE2  44 8B C0                        mov r8d, eax
00606FE5  48 C1 E1 03                     shl rcx, 3
00606FE9  45 33 C9                        xor r9d, r9d
00606FEC  48 83 C9 0C                     or rcx, 0xc
00606FF0  49 C1 E0 04                     shl r8, 4
00606FF4  33 D2                           xor edx, edx
00606FF6  48 8D 04 0F                     lea rax, [rdi + rcx]
00606FFA  49 8B CF                        mov rcx, r15
00606FFD  4C 03 C0                        add r8, rax
00607000  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00607007  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0060700B  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00607010  E8 1B 94 DC FF                  call 0x1403d0430
00607015  84 C0                           test al, al
00607017  0F 84 77 04 00 00               je 0x140607494
0060701D  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
00607025  44 8B C5                        mov r8d, ebp
00607028  49 8B D5                        mov rdx, r13
0060702B  48 8B CB                        mov rcx, rbx
0060702E  E8 C1 1F EB FF                  call 0x1404b8ff4
00607033  84 C0                           test al, al
00607035  0F 84 59 04 00 00               je 0x140607494
0060703B  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00607043  44 8B 84 24 D0 00 00 00         mov r8d, dword ptr [rsp + 0xd0]
0060704B  E9 30 04 00 00                  jmp 0x140607480
00607050  83 E1 02                        and ecx, 2
00607053  44 8B C0                        mov r8d, eax
00607056  48 C1 E1 03                     shl rcx, 3
0060705A  45 33 C9                        xor r9d, r9d
0060705D  48 83 C9 0C                     or rcx, 0xc
00607061  49 C1 E0 04                     shl r8, 4
00607065  33 D2                           xor edx, edx
00607067  48 8D 04 0F                     lea rax, [rdi + rcx]
0060706B  49 8B CF                        mov rcx, r15
0060706E  4C 03 C0                        add r8, rax
00607071  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00607078  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0060707C  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00607081  E8 AA 93 DC FF                  call 0x1403d0430
00607086  84 C0                           test al, al
00607088  0F 84 06 04 00 00               je 0x140607494
0060708E  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00607096  E9 E2 03 00 00                  jmp 0x14060747d
0060709B  3C 04                           cmp al, 4
0060709D  75 53                           jne 0x1406070f2
0060709F  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
006070A6  45 33 C9                        xor r9d, r9d
006070A9  44 0F B6 47 0D                  movzx r8d, byte ptr [rdi + 0xd]
006070AE  33 D2                           xor edx, edx
006070B0  49 83 C0 05                     add r8, 5
006070B4  88 44 24 28                     mov byte ptr [rsp + 0x28], al
006070B8  49 8B CF                        mov rcx, r15
006070BB  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
006070C0  4E 8D 04 87                     lea r8, [rdi + r8*4]
006070C4  E8 67 93 DC FF                  call 0x1403d0430
006070C9  84 C0                           test al, al
006070CB  0F 84 CA 03 00 00               je 0x14060749b
006070D1  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
006070D8  4C 8D 47 0C                     lea r8, [rdi + 0xc]
006070DC  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
006070E4  88 44 24 28                     mov byte ptr [rsp + 0x28], al
006070E8  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
006070ED  E9 02 02 00 00                  jmp 0x1406072f4
006070F2  3C 01                           cmp al, 1
006070F4  75 36                           jne 0x14060712c
006070F6  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
006070FD  4C 8D 47 08                     lea r8, [rdi + 8]
00607101  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00607105  41 B1 01                        mov r9b, 1
00607108  33 D2                           xor edx, edx
0060710A  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
0060710F  49 8B CF                        mov rcx, r15
00607112  E8 19 93 DC FF                  call 0x1403d0430
00607117  84 C0                           test al, al
00607119  0F 84 7C 03 00 00               je 0x14060749b
0060711F  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00607127  E9 E2 01 00 00                  jmp 0x14060730e
0060712C  3C 06                           cmp al, 6
0060712E  0F 85 B7 00 00 00               jne 0x1406071eb
00607134  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00607137  41 B1 01                        mov r9b, 1
0060713A  8B C1                           mov eax, ecx
0060713C  33 D2                           xor edx, edx
0060713E  83 E0 01                        and eax, 1
00607141  83 E1 02                        and ecx, 2
00607144  44 8B C0                        mov r8d, eax
00607147  48 C1 E1 03                     shl rcx, 3
0060714B  48 83 C9 0C                     or rcx, 0xc
0060714F  8B D8                           mov ebx, eax
00607151  49 C1 E0 04                     shl r8, 4
00607155  48 8D 04 0F                     lea rax, [rdi + rcx]
00607159  49 8B CF                        mov rcx, r15
0060715C  4C 03 C0                        add r8, rax
0060715F  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00607166  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0060716A  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
0060716F  E8 BC 92 DC FF                  call 0x1403d0430
00607174  84 C0                           test al, al
00607176  0F 84 18 03 00 00               je 0x140607494
0060717C  85 DB                           test ebx, ebx
0060717E  0F 84 F1 02 00 00               je 0x140607475
00607184  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
00607188  48 85 C9                        test rcx, rcx
0060718B  0F 84 E4 02 00 00               je 0x140607475
00607191  83 BC 24 00 01 00 00 00         cmp dword ptr [rsp + 0x100], 0
00607199  75 28                           jne 0x1406071c3
0060719B  41 8B 4D 1C                     mov ecx, dword ptr [r13 + 0x1c]
0060719F  45 8B C4                        mov r8d, r12d
006071A2  4D 8B 4D 28                     mov r9, qword ptr [r13 + 0x28]
006071A6  F7 D1                           not ecx
006071A8  23 4F 04                        and ecx, dword ptr [rdi + 4]
006071AB  BA 00 00 02 00                  mov edx, 0x20000
006071B0  41 09 4D 20                     or dword ptr [r13 + 0x20], ecx
006071B4  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
006071B9  E8 C2 87 E2 FF                  call 0x14042f980
006071BE  E9 D1 02 00 00                  jmp 0x140607494
006071C3  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
006071CB  44 8B C5                        mov r8d, ebp
006071CE  49 8B D5                        mov rdx, r13
006071D1  E8 1E 1E EB FF                  call 0x1404b8ff4
006071D6  84 C0                           test al, al
006071D8  0F 84 B6 02 00 00               je 0x140607494
006071DE  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
006071E6  E9 58 FE FF FF                  jmp 0x140607043
006071EB  3C 09                           cmp al, 9
006071ED  0F 85 68 01 00 00               jne 0x14060735b
006071F3  0F B6 47 09                     movzx eax, byte ptr [rdi + 9]
006071F7  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
006071FE  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00607202  2B C3                           sub eax, ebx
00607204  83 F8 08                        cmp eax, 8
00607207  0F 84 87 02 00 00               je 0x140607494
0060720D  4D 85 C9                        test r9, r9
00607210  74 19                           je 0x14060722b
00607212  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
0060721A  48 83 38 00                     cmp qword ptr [rax], 0
0060721E  75 0B                           jne 0x14060722b
00607220  48 8B D0                        mov rdx, rax
00607223  49 8B C9                        mov rcx, r9
00607226  E8 59 BC CF FF                  call 0x140302e84
0060722B  49 8B 87 48 04 00 00            mov rax, qword ptr [r15 + 0x448]
00607232  48 85 C0                        test rax, rax
00607235  74 1E                           je 0x140607255
00607237  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
0060723E  4C 8B 80 50 02 00 00            mov r8, qword ptr [rax + 0x250]
00607245  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
0060724C  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
00607253  EB 0C                           jmp 0x140607261
00607255  45 33 C9                        xor r9d, r9d
00607258  45 33 C0                        xor r8d, r8d
0060725B  45 33 D2                        xor r10d, r10d
0060725E  45 33 DB                        xor r11d, r11d
00607261  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
00607265  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0060726A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0060726F  2B D3                           sub edx, ebx
00607271  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00607279  83 EA 08                        sub edx, 8
0060727C  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
00607281  C6 44 24 48 00                  mov byte ptr [rsp + 0x48], 0
00607286  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
0060728A  49 8B 97 08 03 00 00            mov rdx, qword ptr [r15 + 0x308]
00607291  8B CB                           mov ecx, ebx
00607293  48 83 C1 08                     add rcx, 8
00607297  48 03 CF                        add rcx, rdi
0060729A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0060729F  49 8B CF                        mov rcx, r15
006072A2  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
006072A7  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
006072AC  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
006072B1  4C 8B 00                        mov r8, qword ptr [rax]
006072B4  E8 17 79 CF FF                  call 0x1402febd0
006072B9  83 7C 24 60 01                  cmp dword ptr [rsp + 0x60], 1
006072BE  0F 85 D0 01 00 00               jne 0x140607494
006072C4  E8 BF 84 EE FF                  call 0x1404ef788
006072C9  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
006072D0  E9 8F FB FF FF                  jmp 0x140606e64
006072D5  44 8B A4 24 10 01 00 00         mov r12d, dword ptr [rsp + 0x110]
006072DD  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
006072E4  4C 8D 47 08                     lea r8, [rdi + 8]
006072E8  88 44 24 28                     mov byte ptr [rsp + 0x28], al
006072EC  49 8B CF                        mov rcx, r15
006072EF  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
006072F4  45 33 C9                        xor r9d, r9d
006072F7  33 D2                           xor edx, edx
006072F9  E8 32 91 DC FF                  call 0x1403d0430
006072FE  84 C0                           test al, al
00607300  0F 84 95 01 00 00               je 0x14060749b
00607306  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0060730E  45 8B CC                        mov r9d, r12d
00607311  8B 47 04                        mov eax, dword ptr [rdi + 4]
00607314  45 33 C0                        xor r8d, r8d
00607317  8B D5                           mov edx, ebp
00607319  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0060731D  49 8B CD                        mov rcx, r13
00607320  E8 47 A6 DC FF                  call 0x1403d196c
00607325  E9 71 01 00 00                  jmp 0x14060749b
0060732A  85 DB                           test ebx, ebx
0060732C  74 0E                           je 0x14060733c
0060732E  83 BC 24 E8 00 00 00 00         cmp dword ptr [rsp + 0xe8], 0
00607336  0F 84 38 FC FF FF               je 0x140606f74
0060733C  45 84 F6                        test r14b, r14b
0060733F  0F 85 2F FC FF FF               jne 0x140606f74
00607345  48 8D 4F 08                     lea rcx, [rdi + 8]
00607349  E8 A2 9A DC FF                  call 0x1403d0df0
0060734E  84 C0                           test al, al
00607350  0F 85 15 FC FF FF               jne 0x140606f6b
00607356  E9 19 FC FF FF                  jmp 0x140606f74
0060735B  80 BC 24 20 01 00 00 00         cmp byte ptr [rsp + 0x120], 0
00607363  0F 84 32 01 00 00               je 0x14060749b
00607369  3C 0A                           cmp al, 0xa
0060736B  0F 85 2A 01 00 00               jne 0x14060749b
00607371  44 0F 20 C0                     mov rax, cr8
00607375  3C 02                           cmp al, 2
00607377  0F 83 1E 01 00 00               jae 0x14060749b
0060737D  0F B6 47 09                     movzx eax, byte ptr [rdi + 9]
00607381  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
00607388  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0060738C  2B C3                           sub eax, ebx
0060738E  83 F8 08                        cmp eax, 8
00607391  0F 84 FD 00 00 00               je 0x140607494
00607397  4D 85 C9                        test r9, r9
0060739A  74 19                           je 0x1406073b5
0060739C  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
006073A4  48 83 38 00                     cmp qword ptr [rax], 0
006073A8  75 0B                           jne 0x1406073b5
006073AA  48 8B D0                        mov rdx, rax
006073AD  49 8B C9                        mov rcx, r9
006073B0  E8 CF BA CF FF                  call 0x140302e84
006073B5  49 8B 87 48 04 00 00            mov rax, qword ptr [r15 + 0x448]
006073BC  48 85 C0                        test rax, rax
006073BF  74 1E                           je 0x1406073df
006073C1  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
006073C8  4C 8B 80 50 02 00 00            mov r8, qword ptr [rax + 0x250]
006073CF  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
006073D6  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
006073DD  EB 0C                           jmp 0x1406073eb
006073DF  45 33 C9                        xor r9d, r9d
006073E2  45 33 C0                        xor r8d, r8d
006073E5  45 33 D2                        xor r10d, r10d
006073E8  45 33 DB                        xor r11d, r11d
006073EB  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
006073EF  48 8D 44 24 60                  lea rax, [rsp + 0x60]
006073F4  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
006073F9  2B D3                           sub edx, ebx
006073FB  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00607403  83 EA 08                        sub edx, 8
00607406  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
0060740B  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
00607410  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00607414  49 8B 97 08 03 00 00            mov rdx, qword ptr [r15 + 0x308]
0060741B  8B CB                           mov ecx, ebx
0060741D  48 83 C1 08                     add rcx, 8
00607421  48 03 CF                        add rcx, rdi
00607424  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00607429  49 8B CF                        mov rcx, r15
0060742C  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00607431  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
00607436  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0060743B  4C 8B 00                        mov r8, qword ptr [rax]
0060743E  E8 8D 77 CF FF                  call 0x1402febd0
00607443  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00607447  FF C0                           inc eax
00607449  A9 FD FF FF FF                  test eax, 0xfffffffd
0060744E  75 44                           jne 0x140607494
00607450  8A 84 24 18 01 00 00            mov al, byte ptr [rsp + 0x118]
00607457  4C 8D 47 08                     lea r8, [rdi + 8]
0060745B  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0060745F  41 B1 01                        mov r9b, 1
00607462  33 D2                           xor edx, edx
00607464  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00607469  49 8B CF                        mov rcx, r15
0060746C  E8 BF 8F DC FF                  call 0x1403d0430
00607471  84 C0                           test al, al
00607473  74 1F                           je 0x140607494
00607475  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
0060747D  45 33 C0                        xor r8d, r8d
00607480  8B 47 04                        mov eax, dword ptr [rdi + 4]
00607483  45 8B CC                        mov r9d, r12d
00607486  8B D5                           mov edx, ebp
00607488  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0060748C  49 8B CD                        mov rcx, r13
0060748F  E8 D8 A4 DC FF                  call 0x1403d196c
00607494  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
0060749B  FF 84 24 10 01 00 00            inc dword ptr [rsp + 0x110]
006074A2  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
006074A6  44 8B A4 24 10 01 00 00         mov r12d, dword ptr [rsp + 0x110]
006074AE  48 03 F8                        add rdi, rax
006074B1  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
006074B9  44 3B 64 24 64                  cmp r12d, dword ptr [rsp + 0x64]
006074BE  0F 82 87 F9 FF FF               jb 0x140606e4b
006074C4  45 84 F6                        test r14b, r14b
006074C7  74 27                           je 0x1406074f0
006074C9  85 ED                           test ebp, ebp
006074CB  74 23                           je 0x1406074f0
006074CD  8B 94 24 08 01 00 00            mov edx, dword ptr [rsp + 0x108]
006074D4  49 8D 4D 1C                     lea rcx, [r13 + 0x1c]
006074D8  F7 D2                           not edx
006074DA  4C 8B C5                        mov r8, rbp
006074DD  8B C2                           mov eax, edx
006074DF  0B 01                           or eax, dword ptr [rcx]
006074E1  23 41 FC                        and eax, dword ptr [rcx - 4]
006074E4  89 01                           mov dword ptr [rcx], eax
006074E6  48 8D 49 30                     lea rcx, [rcx + 0x30]
006074EA  49 83 E8 01                     sub r8, 1
006074EE  75 ED                           jne 0x1406074dd
006074F0  48 83 C4 78                     add rsp, 0x78
006074F4  41 5F                           pop r15
006074F6  41 5E                           pop r14
006074F8  41 5D                           pop r13
006074FA  41 5C                           pop r12
006074FC  5F                              pop rdi
006074FD  5E                              pop rsi
006074FE  5D                              pop rbp
006074FF  5B                              pop rbx
00607500  C3                              ret
00607501  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepMaximumAccessCheckEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8, unsigned int a9, unsigned int a10, unsigned __int8 a11, unsigned __int8 a12, unsigned __int8 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int8 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p58;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (120);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 200))))) & (0x4000ULL));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) & (0x2000ULL));
    v_stack_p30 = (unsigned int)(result);
    v_stack_p8 = (unsigned int)(v_rbx);
    if (a11 == 0) goto loc_00606E24;
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_00606E24;
loc_00606DE8:
    a3 = 0;
    v_stack_m98 = 1;
    result = AuthzBasepSetAccessReasons((unsigned int)(*(unsigned int *)(a8 + 28)), (unsigned int)(0x800000ULL), a3, *(unsigned __int64 *)(a8 + 28 + 12));
    *(unsigned int *)(a8 + 28 - 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 28)));
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(a7)))) - (1);
    if (condition_is_not_equal) goto loc_00606DE8;
loc_00606E24:
    v_r12 = 0;
    v_rdi = (a3) + (8);
    v_stack_m54 = (unsigned int)(*(unsigned __int16 *)(a3 + 4));
    v_stack_p58 = 0;
    if ((unsigned int)(*(unsigned __int16 *)(a3 + 4)) == 0) goto loc_006074C4;
loc_00606E4B:
    if (((*(unsigned __int8 *)(v_rdi + 1)) & (8)) != 0) goto loc_0060749B;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) != 0) goto loc_00606FB2;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(a8 + 28)), (unsigned int)(0x800000ULL), a3, v_stack_p20);
loc_00606E64:
    if ((unsigned int)(result) != 0) goto loc_00606F0D;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) goto loc_006072DD;
    if (a11 != 0) goto loc_006072DD;
    result = SepIsPackageSid(v_rdi + 8, (unsigned int)(0x800000ULL), a3, v_stack_p20);
    if ((unsigned __int8)(result) == 0) goto loc_00606ED7;
    v_stack_m78 = a14 + 24;
    v_stack_m80 = a14 + 16;
    v_stack_m88 = a14 + 20;
    v_stack_m90 = a14 + 4;
    v_stack_m98 = a14 + 21;
loc_00606EBD:
    a2 = (unsigned int)((a14 + 20) | (0xFFFFFFFFULL));
    result = SepMatchPackage(a1, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
loc_00606ECC:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a14 + 4))));
    goto loc_00607494;
loc_00606ED7:
    result = SepIsCapabilitySid(v_rdi + 8, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    if ((unsigned __int8)(result) == 0) goto loc_006072D5;
loc_00606EEA:
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_m90 = a14 + 8;
    v_stack_m98 = a14 + 22;
    result = SepMatchCapability(a1, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    goto loc_00606ECC;
loc_00606F0D:
    if ((unsigned int)(a14 + 8) == 0) goto loc_00606F1B;
    if (a6 == 0) goto loc_00606F74;
loc_00606F1B:
    if (a11 != 0) goto loc_0060732A;
    result = SepIsPackageSid(v_rdi + 8, a2, v_rdi + 8, (unsigned int)(*(unsigned int *)(v_rdi + 4)));
    if ((unsigned __int8)(result) == 0) goto loc_0060732A;
    v_stack_m78 = a14 + 24;
    v_stack_m80 = a14 + 16;
    v_stack_m88 = a14 + 20;
    v_stack_m90 = a14 + 4;
    v_stack_m98 = a14 + 21;
    goto loc_00606EBD;
loc_00606F6B:
    goto loc_00606EEA;
loc_00606F74:
    v_stack_m90 = a12;
    a4 = 0;
    a2 = 0;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0060749B;
    v_stack_m90 = 1;
    goto loc_00607311;
loc_00606FB2:
    if (((unsigned __int8)(result)) != 5) goto loc_0060709B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) & (1));
    if (condition_is_equal) goto loc_00607050;
    if (v_rdi + 12 == 0) goto loc_00607050;
    if (a9 == 0) goto loc_00607494;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (2));
    a1 = (a1) << (3);
    a4 = 0;
    a1 = (a1) | (12);
    a3 = ((unsigned int)((unsigned int)(result))) << (4);
    a2 = 0;
    a3 = (a3) + (v_rdi + a1 * 1);
    v_stack_m90 = a12;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00607494;
    result = AuthzBasepObjectInTypeList(v_rdi + 12, a8, (unsigned int)((unsigned int)((unsigned int)(a7))), v_stack_p18);
    if ((unsigned __int8)(result) == 0) goto loc_00607494;
    v_stack_m90 = 1;
loc_00607043:
    goto loc_00607480;
loc_00607050:
    a1 = (unsigned int)((v_rdi + 12) & (2));
    a1 = (a1) << (3);
    a4 = 0;
    a1 = (a1) | (12);
    a3 = ((unsigned int)((unsigned int)(result))) << (4);
    a2 = 0;
    a3 = (a3) + (v_rdi + a1 * 1);
    v_stack_m90 = a12;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00607494;
    v_stack_m90 = 1;
    goto loc_0060747D;
loc_0060709B:
    if (((unsigned __int8)(result)) != 4) goto loc_006070F2;
    a4 = 0;
    a2 = 0;
    a3 = (*(unsigned __int8 *)(v_rdi + 13)) + (5);
    v_stack_m90 = a12;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, v_rdi + a3 * 4, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0060749B;
    v_stack_m90 = a12;
    v_stack_m98 = 0;
    goto loc_006072F4;
loc_006070F2:
    if (a12 != 1) goto loc_0060712C;
    v_stack_m90 = a12;
    a2 = 0;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0060749B;
    v_stack_m90 = 2;
    goto loc_0060730E;
loc_0060712C:
    if (((unsigned __int8)(result)) != 6) goto loc_006071EB;
    a2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) & (1));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (2));
    a1 = (a1) << (3);
    a1 = (a1) | (12);
    a3 = ((unsigned int)((unsigned int)(result))) << (4);
    a3 = (a3) + (v_rdi + a1 * 1);
    v_stack_m90 = a12;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, a3, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00607494;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00607475;
    if (v_rdi + 12 == 0) goto loc_00607475;
    if (a9 != 0) goto loc_006071C3;
    a1 = (unsigned int)(~((unsigned int)(*(unsigned int *)(a8 + 28))));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(v_rdi + 4)));
    v_stack_m98 = 0;
    result = AuthzBasepSetAccessReasons(a1, (unsigned int)(0x20000ULL), (unsigned int)((unsigned int)(v_rdi + 8)), *(unsigned __int64 *)(a8 + 40));
    goto loc_00607494;
loc_006071C3:
    result = AuthzBasepObjectInTypeList(a1, a8, (unsigned int)((unsigned int)((unsigned int)(a7))), v_stack_p18);
    if ((unsigned __int8)(result) == 0) goto loc_00607494;
    v_stack_m90 = 2;
    goto loc_00607043;
loc_006071EB:
    if (((unsigned __int8)(result)) != 9) goto loc_0060735B;
    result = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    if (((unsigned int)(result)) == 8) goto loc_00607494;
    if (v_stack_p18 == 0) goto loc_0060722B;
    result = a5;
    if ((*(unsigned __int64 *)(a5)) == 0) {
        a2 = a5;
        a1 = v_stack_p18;
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a7))), v_stack_p18);
    }
    if (*(unsigned __int64 *)(a1 + 1096) == 0) goto loc_00607255;
    goto loc_00607261;
loc_00607255:
    a4 = 0;
    a3 = 0;
    v_r10 = 0;
    v_r11 = 0;
loc_00607261:
    v_stack_m60 = v_stack_m58;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    a2 = (unsigned int)((a2) - (8));
    v_stack_m68 = a11;
    v_stack_m70 = 0;
    v_stack_m78 = (unsigned int)(a2);
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8))) + (8);
    a1 = (a1) + (v_rdi);
    v_stack_m80 = a1;
    v_stack_m88 = 0;
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    result = AuthzBasepEvaluateAceCondition(a1, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), a4);
    if (v_stack_m58 != 1) goto loc_00607494;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), a4);
    goto loc_00606E64;
loc_006072D5:
loc_006072DD:
    v_stack_m90 = a12;
    v_stack_m98 = a11;
loc_006072F4:
    a4 = 0;
    a2 = 0;
    result = SepSidInToken(a1, a2, v_rdi + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0060749B;
    v_stack_m90 = 1;
loc_0060730E:
loc_00607311:
    a3 = 0;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = AuthzBasepAddAccessTypeList(a8, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, (unsigned int)((unsigned int)((unsigned int)(a11))));
    goto loc_0060749B;
loc_0060732A:
    if ((unsigned int)((unsigned int)(v_stack_p8)) == 0) goto loc_0060733C;
    if (a6 == 0) goto loc_00606F74;
loc_0060733C:
    if (a11 != 0) goto loc_00606F74;
    result = SepIsCapabilitySid(v_rdi + 8, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, (unsigned int)((unsigned int)((unsigned int)(a11))));
    if ((unsigned __int8)(result) != 0) goto loc_00606F6B;
    goto loc_00606F74;
loc_0060735B:
    if (a13 == 0) goto loc_0060749B;
    if (((unsigned __int8)(result)) != 10) goto loc_0060749B;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_0060749B;
    result = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    if (((unsigned int)(result)) == 8) goto loc_00607494;
    if ((unsigned int)((unsigned int)((unsigned int)(a11))) == 0) goto loc_006073B5;
    result = a5;
    if ((*(unsigned __int64 *)(a5)) == 0) {
        a2 = a5;
        a1 = (unsigned int)((unsigned int)((unsigned int)(a11)));
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a11))));
    }
    if (*(unsigned __int64 *)(a1 + 1096) == 0) goto loc_006073DF;
    goto loc_006073EB;
loc_006073DF:
    a4 = 0;
    a3 = 0;
    v_r10 = 0;
    v_r11 = 0;
loc_006073EB:
    v_stack_m60 = v_stack_m58;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8)));
    a2 = (unsigned int)((a2) - (8));
    v_stack_m68 = a11;
    v_stack_m70 = 1;
    v_stack_m78 = (unsigned int)(a2);
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi + 9) * 4 + 8))) + (8);
    a1 = (a1) + (v_rdi);
    v_stack_m80 = a1;
    v_stack_m88 = 0;
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    result = AuthzBasepEvaluateAceCondition(a1, *(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(a5), a4);
    result = (unsigned int)(((unsigned int)(v_stack_m58)) + 1);
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_00607494;
    v_stack_m90 = a12;
    a2 = 0;
    v_stack_m98 = a11;
    result = SepSidInToken(a1, a2, v_rdi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00607494;
loc_00607475:
    v_stack_m90 = 2;
loc_0060747D:
    a3 = 0;
loc_00607480:
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = AuthzBasepAddAccessTypeList(a8, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, (unsigned int)((unsigned int)((unsigned int)(a11))));
loc_00607494:
loc_0060749B:
    v_rdi = (v_rdi) + (*(unsigned __int16 *)(v_rdi + 2));
    if (((unsigned int)((unsigned int)(a11))) < v_stack_m54) goto loc_00606E4B;
loc_006074C4:
    if (a11 == 0) goto loc_006074F0;
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_006074F0;
    a2 = (unsigned int)(~((unsigned int)(a10)));
loc_006074DD:
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (*(unsigned int *)(a8 + 28)));
    result = (unsigned int)((result) & (*(unsigned int *)(a8 + 28 - 4)));
    *(unsigned int *)(a8 + 28) = (unsigned int)(result);
    a3 = ((unsigned int)(a7)) - (1);
    if (condition_is_not_equal) goto loc_006074DD;
loc_006074F0:
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepMaximumAccessCheckEx(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6, uint32_t Arg7, void *Arg8, uint32_t Arg9, uint32_t Arg10, uint8_t Arg11, uint8_t Arg12, uint8_t Arg13, void *Arg14)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg14 = (uint8_t *)Arg14;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint8_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p58;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (120);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8))))) & (0x4000ULL));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) & (0x2000ULL));
    v_stack_p30 = (uint32_t)(result);
    v_stack_p8 = (uint32_t)(local_rbx);
    if (Arg11 == 0) goto loc_00606E24;
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_00606E24;
loc_00606DE8:
    Arg3 = 0;
    v_stack_m98 = 1;
    result = AuthzBasepSetAccessReasons((uint32_t)(*(uint32_t *)(arg8 + 0x1C)), (uint32_t)(0x800000ULL), Arg3, *(uint64_t *)(arg8 + 0x1C + 0xC));
    *(uint32_t *)(arg8 + 0x1C - 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg8 + 0x1C)));
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(Arg7)))) - (1);
    if (condition_is_not_equal) goto loc_00606DE8;
loc_00606E24:
    local_r12 = 0;
    local_rdi = (Arg3) + (8);
    v_stack_m54 = (uint32_t)(*(uint16_t *)(arg3 + 0x4));
    v_stack_p58 = 0;
    if ((uint32_t)(*(uint16_t *)(arg3 + 0x4)) == 0) goto loc_006074C4;
loc_00606E4B:
    if (((*(uint8_t *)(local_rdi + 0x1)) & (8)) != 0) goto loc_0060749B;
    if ((uint8_t)(*(uint8_t *)(local_rdi)) != 0) goto loc_00606FB2;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(arg8 + 0x1C)), (uint32_t)(0x800000ULL), Arg3, v_stack_p20);
loc_00606E64:
    if ((uint32_t)(result) != 0) goto loc_00606F0D;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) goto loc_006072DD;
    if (Arg11 != 0) goto loc_006072DD;
    result = SepIsPackageSid(local_rdi + 8, (uint32_t)(0x800000ULL), Arg3, v_stack_p20);
    if ((uint8_t)(result) == 0) goto loc_00606ED7;
    v_stack_m78 = Arg14 + 24;
    v_stack_m80 = Arg14 + 16;
    v_stack_m88 = Arg14 + 20;
    v_stack_m90 = Arg14 + 4;
    v_stack_m98 = Arg14 + 21;
loc_00606EBD:
    Arg2 = (uint32_t)((Arg14 + 20) | (0xFFFFFFFFULL));
    result = SepMatchPackage(Arg1, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
loc_00606ECC:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg14 + 0x4))));
    goto loc_00607494;
loc_00606ED7:
    result = SepIsCapabilitySid(local_rdi + 8, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    if ((uint8_t)(result) == 0) goto loc_006072D5;
loc_00606EEA:
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_m90 = Arg14 + 8;
    v_stack_m98 = Arg14 + 22;
    result = SepMatchCapability(Arg1, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    goto loc_00606ECC;
loc_00606F0D:
    if ((uint32_t)(Arg14 + 8) == 0) goto loc_00606F1B;
    if (Arg6 == 0) goto loc_00606F74;
loc_00606F1B:
    if (Arg11 != 0) goto loc_0060732A;
    result = SepIsPackageSid(local_rdi + 8, Arg2, local_rdi + 8, (uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    if ((uint8_t)(result) == 0) goto loc_0060732A;
    v_stack_m78 = Arg14 + 24;
    v_stack_m80 = Arg14 + 16;
    v_stack_m88 = Arg14 + 20;
    v_stack_m90 = Arg14 + 4;
    v_stack_m98 = Arg14 + 21;
    goto loc_00606EBD;
loc_00606F6B:
    goto loc_00606EEA;
loc_00606F74:
    v_stack_m90 = Arg12;
    Arg4 = 0;
    Arg2 = 0;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0060749B;
    v_stack_m90 = 1;
    goto loc_00607311;
loc_00606FB2:
    if (((uint8_t)(result)) != 5) goto loc_0060709B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) & (1));
    if (condition_is_equal) goto loc_00607050;
    if (local_rdi + 12 == 0) goto loc_00607050;
    if (Arg9 == 0) goto loc_00607494;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (2));
    Arg1 = (Arg1) << (3);
    Arg4 = 0;
    Arg1 = (Arg1) | (12);
    Arg3 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg2 = 0;
    Arg3 = (Arg3) + (local_rdi + Arg1 * 1);
    v_stack_m90 = Arg12;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00607494;
    result = AuthzBasepObjectInTypeList(local_rdi + 12, Arg8, (uint32_t)((uint32_t)((uint32_t)(Arg7))), v_stack_p18);
    if ((uint8_t)(result) == 0) goto loc_00607494;
    v_stack_m90 = 1;
loc_00607043:
    goto loc_00607480;
loc_00607050:
    Arg1 = (uint32_t)((local_rdi + 12) & (2));
    Arg1 = (Arg1) << (3);
    Arg4 = 0;
    Arg1 = (Arg1) | (12);
    Arg3 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg2 = 0;
    Arg3 = (Arg3) + (local_rdi + Arg1 * 1);
    v_stack_m90 = Arg12;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00607494;
    v_stack_m90 = 1;
    goto loc_0060747D;
loc_0060709B:
    if (((uint8_t)(result)) != 4) goto loc_006070F2;
    Arg4 = 0;
    Arg2 = 0;
    Arg3 = (*(uint8_t *)(local_rdi + 0xD)) + (5);
    v_stack_m90 = Arg12;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, local_rdi + Arg3 * 4, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0060749B;
    v_stack_m90 = Arg12;
    v_stack_m98 = 0;
    goto loc_006072F4;
loc_006070F2:
    if (Arg12 != 1) goto loc_0060712C;
    v_stack_m90 = Arg12;
    Arg2 = 0;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_0060749B;
    v_stack_m90 = 2;
    goto loc_0060730E;
loc_0060712C:
    if (((uint8_t)(result)) != 6) goto loc_006071EB;
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) & (1));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (2));
    Arg1 = (Arg1) << (3);
    Arg1 = (Arg1) | (12);
    Arg3 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg3 = (Arg3) + (local_rdi + Arg1 * 1);
    v_stack_m90 = Arg12;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, Arg3, 1);
    if ((uint8_t)(result) == 0) goto loc_00607494;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00607475;
    if (local_rdi + 12 == 0) goto loc_00607475;
    if (Arg9 != 0) goto loc_006071C3;
    Arg1 = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg8 + 0x1C))));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(local_rdi + 0x4)));
    v_stack_m98 = 0;
    result = AuthzBasepSetAccessReasons(Arg1, (uint32_t)(0x20000ULL), (uint32_t)((uint32_t)(local_rdi + 8)), *(uint64_t *)(arg8 + 0x28));
    goto loc_00607494;
loc_006071C3:
    result = AuthzBasepObjectInTypeList(Arg1, Arg8, (uint32_t)((uint32_t)((uint32_t)(Arg7))), v_stack_p18);
    if ((uint8_t)(result) == 0) goto loc_00607494;
    v_stack_m90 = 2;
    goto loc_00607043;
loc_006071EB:
    if (((uint8_t)(result)) != 9) goto loc_0060735B;
    result = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    if (((uint32_t)(result)) == 8) goto loc_00607494;
    if (v_stack_p18 == 0) goto loc_0060722B;
    result = Arg5;
    if ((*(uint64_t *)(arg5)) == 0) {
        Arg2 = Arg5;
        Arg1 = v_stack_p18;
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg7))), v_stack_p18);
    }
    if (*(uint64_t *)(arg1 + 0x448) == 0) goto loc_00607255;
    goto loc_00607261;
loc_00607255:
    Arg4 = 0;
    Arg3 = 0;
    local_r10 = 0;
    local_r11 = 0;
loc_00607261:
    v_stack_m60 = v_stack_m58;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_m68 = Arg11;
    v_stack_m70 = 0;
    v_stack_m78 = (uint32_t)(Arg2);
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8))) + (8);
    Arg1 = (Arg1) + (local_rdi);
    v_stack_m80 = Arg1;
    v_stack_m88 = 0;
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    result = AuthzBasepEvaluateAceCondition(Arg1, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), Arg4);
    if (v_stack_m58 != 1) goto loc_00607494;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), Arg4);
    goto loc_00606E64;
loc_006072D5:
loc_006072DD:
    v_stack_m90 = Arg12;
    v_stack_m98 = Arg11;
loc_006072F4:
    Arg4 = 0;
    Arg2 = 0;
    result = SepSidInToken(Arg1, Arg2, local_rdi + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0060749B;
    v_stack_m90 = 1;
loc_0060730E:
loc_00607311:
    Arg3 = 0;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = AuthzBasepAddAccessTypeList(Arg8, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg11))));
    goto loc_0060749B;
loc_0060732A:
    if ((uint32_t)((uint32_t)(v_stack_p8)) == 0) goto loc_0060733C;
    if (Arg6 == 0) goto loc_00606F74;
loc_0060733C:
    if (Arg11 != 0) goto loc_00606F74;
    result = SepIsCapabilitySid(local_rdi + 8, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg11))));
    if ((uint8_t)(result) != 0) goto loc_00606F6B;
    goto loc_00606F74;
loc_0060735B:
    if (Arg13 == 0) goto loc_0060749B;
    if (((uint8_t)(result)) != 10) goto loc_0060749B;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_0060749B;
    result = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    if (((uint32_t)(result)) == 8) goto loc_00607494;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg11))) == 0) goto loc_006073B5;
    result = Arg5;
    if ((*(uint64_t *)(arg5)) == 0) {
        Arg2 = Arg5;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(Arg11)));
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg11))));
    }
    if (*(uint64_t *)(arg1 + 0x448) == 0) goto loc_006073DF;
    goto loc_006073EB;
loc_006073DF:
    Arg4 = 0;
    Arg3 = 0;
    local_r10 = 0;
    local_r11 = 0;
loc_006073EB:
    v_stack_m60 = v_stack_m58;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8)));
    Arg2 = (uint32_t)((Arg2) - (8));
    v_stack_m68 = Arg11;
    v_stack_m70 = 1;
    v_stack_m78 = (uint32_t)(Arg2);
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi + 0x9) * 4 + 8))) + (8);
    Arg1 = (Arg1) + (local_rdi);
    v_stack_m80 = Arg1;
    v_stack_m88 = 0;
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    result = AuthzBasepEvaluateAceCondition(Arg1, *(uint64_t *)(arg1 + 0x308), *(uint64_t *)(arg5), Arg4);
    result = (uint32_t)(((uint32_t)(v_stack_m58)) + 1);
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_00607494;
    v_stack_m90 = Arg12;
    Arg2 = 0;
    v_stack_m98 = Arg11;
    result = SepSidInToken(Arg1, Arg2, local_rdi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_00607494;
loc_00607475:
    v_stack_m90 = 2;
loc_0060747D:
    Arg3 = 0;
loc_00607480:
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = AuthzBasepAddAccessTypeList(Arg8, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg11))));
loc_00607494:
loc_0060749B:
    local_rdi = (local_rdi) + (*(uint16_t *)(local_rdi + 0x2));
    if (((uint32_t)((uint32_t)(Arg11))) < v_stack_m54) goto loc_00606E4B;
loc_006074C4:
    if (Arg11 == 0) goto loc_006074F0;
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_006074F0;
    Arg2 = (uint32_t)(~((uint32_t)(Arg10)));
loc_006074DD:
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (*(uint32_t *)(arg8 + 0x1C)));
    result = (uint32_t)((result) & (*(uint32_t *)(arg8 + 0x1C - 0x4)));
    *(uint32_t *)(arg8 + 0x1C) = (uint32_t)(result);
    Arg3 = ((uint32_t)(Arg7)) - (1);
    if (condition_is_not_equal) goto loc_006074DD;
loc_006074F0:
    local_rsp = (local_rsp) + (120);
    return result;
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
| `Arg3` | `+ 0x0 + rcx*1` | `64` | `R` |
| `Arg3` | `+ 0x1` | `8` | `R` |
| `Arg3` | `+ 0x2` | `16` | `R` |
| `Arg3` | `+ 0x4` | `16` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x9` | `8` | `R` |
| `Arg3` | `+ 0xC` | `64` | `R` |
| `Arg3` | `+ 0xD` | `8` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg8` | `- 0x4` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x1C` | `32` | `R` |
| `Arg8` | `+ 0x1C` | `64` | `R` |
| `Arg8` | `+ 0x20` | `32` | `R/W` |
| `Arg8` | `+ 0x28` | `64` | `R` |
| `Arg8` | `+ 0x30` | `64` | `R` |
| `Arg14` | `+ 0x0` | `32` | `R` |
| `Arg14` | `+ 0x0` | `32` | `R/W` |
| `Arg14` | `+ 0x4` | `64` | `R` |
| `Arg14` | `+ 0x8` | `64` | `R` |
| `Arg14` | `+ 0x10` | `64` | `R` |
| `Arg14` | `+ 0x14` | `64` | `R` |
| `Arg14` | `+ 0x15` | `64` | `R` |
| `Arg14` | `+ 0x16` | `64` | `R` |

추가 오프셋 1개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00606D78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
