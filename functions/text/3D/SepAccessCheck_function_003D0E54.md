# SepAccessCheck

- RVA: `0x003D0E54`–`0x003D16EC` (길이 `2,200` bytes)
- VA: `0x00000001403D0E54`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00091160`
- 디코드: `531`개 명령, `2,200/2,200` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003D104F` → [SepNormalAccessCheck](SepNormalAccessCheck_function_003D0688.md) (function, `0x003D0688`)
- `0x003D1087` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D1196` → [SepMaximumAccessCheck](../30/SepMaximumAccessCheck_function_00300BF0.md) (function, `0x00300BF0`)
- `0x003D11AE` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D1258` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003D12AC` → [SepSinglePrivilegeCheck](SepSinglePrivilegeCheck_function_003D191C.md) (function, `0x003D191C`)
- `0x003D130A` → [SepAssemblePrivileges](../../page/A2/SepAssemblePrivileges_function_00A210BC.md) (function, `0x00A210BC`)
- `0x003D1359` → [SepSinglePrivilegeCheck](SepSinglePrivilegeCheck_function_003D191C.md) (function, `0x003D191C`)
- `0x003D139B` → [SepSinglePrivilegeCheck](SepSinglePrivilegeCheck_function_003D191C.md) (function, `0x003D191C`)
- `0x003D142F` → [SepNormalAccessCheck](SepNormalAccessCheck_function_003D0688.md) (function, `0x003D0688`)
- `0x003D146C` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003D150B` → [SepMaximumAccessCheck](../30/SepMaximumAccessCheck_function_00300BF0.md) (function, `0x00300BF0`)

### Direct callers
- [SeAccessCheckWithHint](../3A/SeAccessCheckWithHint_function_003A6C30.md) at `0x003A71EA`
- [SeAccessCheckWithHint](../3A/SeAccessCheckWithHint_function_003A6C30.md) at `0x003A7487`
- [SeAccessCheckByType](../44/SeAccessCheckByType_function_00440BC8.md) at `0x00441C8B`
- [SeAccessCheckByType](../44/SeAccessCheckByType_function_00440BC8.md) at `0x0044209B`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1BF15`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1C357`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1C7E9`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1CC0A`

### Static image references
- `0x003D0E6D` → RVA `0x00E0A740` (`.data`; read)
- `0x003D129F` → RVA `0x00FD9B00` (`PAGEDATA`; read)
- `0x003D134C` → RVA `0x00FD9B38` (`PAGEDATA`; read)
- `0x003D138E` → RVA `0x00FD9B28` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003D130A` → [SepAssemblePrivileges](../../page/A2/SepAssemblePrivileges_function_00A210BC.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x003D12D9` → [sub_006E91C2](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D1581` → [sub_006E91C2 + 0xE](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D159D` → [sub_006E91C2 + 0xE](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D15E4` → [sub_006E91C2 + 0x16](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D15F7` → [sub_006E91C2 + 0x16](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D164F` → [sub_006E91C2 + 0x51](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D166B` → [sub_006E91C2 + 0x23](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D16BB` → [sub_006E91C2 + 0x1AA](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D16D0` → [sub_006E91C2 + 0x16D](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D16D9` → [sub_006E91C2 + 0x16D](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)
  - `0x003D16DF` → [sub_006E91C2 + 0x1AA](../6E/Unknown_function_006E91C2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D0E54  40 55                           push rbp
003D0E56  53                              push rbx
003D0E57  56                              push rsi
003D0E58  57                              push rdi
003D0E59  41 54                           push r12
003D0E5B  41 55                           push r13
003D0E5D  41 56                           push r14
003D0E5F  41 57                           push r15
003D0E61  48 8D 6C 24 E8                  lea rbp, [rsp - 0x18]
003D0E66  48 81 EC 18 01 00 00            sub rsp, 0x118
003D0E6D  48 8B 05 CC 98 A3 00            mov rax, qword ptr [rip + 0xa398cc]
003D0E74  48 33 C4                        xor rax, rsp
003D0E77  48 89 45 08                     mov qword ptr [rbp + 8], rax
003D0E7B  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
003D0E82  45 33 D2                        xor r10d, r10d
003D0E85  44 8B BD 80 00 00 00            mov r15d, dword ptr [rbp + 0x80]
003D0E8C  4D 8B E9                        mov r13, r9
003D0E8F  4C 8B B5 88 00 00 00            mov r14, qword ptr [rbp + 0x88]
003D0E96  0F 57 C0                        xorps xmm0, xmm0
003D0E99  4C 8B 8D 98 00 00 00            mov r9, qword ptr [rbp + 0x98]
003D0EA0  4D 85 ED                        test r13, r13
003D0EA3  48 8B BD D8 00 00 00            mov rdi, qword ptr [rbp + 0xd8]
003D0EAA  4C 8B D9                        mov r11, rcx
003D0EAD  48 8B 8D E8 00 00 00            mov rcx, qword ptr [rbp + 0xe8]
003D0EB4  4D 0F 44 E8                     cmove r13, r8
003D0EB8  44 8A A5 A8 00 00 00            mov r12b, byte ptr [rbp + 0xa8]
003D0EBF  41 8B DF                        mov ebx, r15d
003D0EC2  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003D0EC6  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
003D0ECD  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
003D0ED1  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
003D0ED8  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
003D0EDC  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
003D0EE3  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
003D0EE7  48 8B 85 F0 00 00 00            mov rax, qword ptr [rbp + 0xf0]
003D0EEE  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003D0EF2  41 8D 42 04                     lea eax, [r10 + 4]
003D0EF6  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
003D0EFA  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
003D0EFE  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
003D0F03  4C 89 4D 90                     mov qword ptr [rbp - 0x70], r9
003D0F07  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
003D0F0B  C6 44 24 71 01                  mov byte ptr [rsp + 0x71], 1
003D0F10  44 89 54 24 74                  mov dword ptr [rsp + 0x74], r10d
003D0F15  44 88 54 24 73                  mov byte ptr [rsp + 0x73], r10b
003D0F1A  44 88 54 24 70                  mov byte ptr [rsp + 0x70], r10b
003D0F1F  44 88 54 24 72                  mov byte ptr [rsp + 0x72], r10b
003D0F24  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
003D0F28  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
003D0F2C  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
003D0F30  41 0F BA E7 18                  bt r15d, 0x18
003D0F35  0F 82 64 03 00 00               jb 0x1403d129f
003D0F3B  8B B5 A0 00 00 00               mov esi, dword ptr [rbp + 0xa0]
003D0F41  41 0F B7 53 02                  movzx edx, word ptr [r11 + 2]
003D0F46  B9 00 80 00 00                  mov ecx, 0x8000
003D0F4B  44 0F B7 C2                     movzx r8d, dx
003D0F4F  66 44 23 C0                     and r8w, ax
003D0F53  0F B7 C2                        movzx eax, dx
003D0F56  66 23 C1                        and ax, cx
003D0F59  66 45 85 C0                     test r8w, r8w
003D0F5D  74 15                           je 0x1403d0f74
003D0F5F  66 85 C0                        test ax, ax
003D0F62  0F 84 1D 04 00 00               je 0x1403d1385
003D0F68  41 8B 4B 10                     mov ecx, dword ptr [r11 + 0x10]
003D0F6C  85 C9                           test ecx, ecx
003D0F6E  74 04                           je 0x1403d0f74
003D0F70  4D 8D 14 0B                     lea r10, [r11 + rcx]
003D0F74  33 C9                           xor ecx, ecx
003D0F76  4C 89 55 98                     mov qword ptr [rbp - 0x68], r10
003D0F7A  F6 C2 10                        test dl, 0x10
003D0F7D  0F 85 65 01 00 00               jne 0x1403d10e8
003D0F83  4C 8B D9                        mov r11, rcx
003D0F86  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
003D0F8A  66 45 85 C0                     test r8w, r8w
003D0F8E  0F 84 78 01 00 00               je 0x1403d110c
003D0F94  4D 85 D2                        test r10, r10
003D0F97  0F 84 6F 01 00 00               je 0x1403d110c
003D0F9D  41 BF 00 00 08 00               mov r15d, 0x80000
003D0FA3  41 85 DF                        test r15d, ebx
003D0FA6  0F 85 A0 03 00 00               jne 0x1403d134c
003D0FAC  44 8A 7C 24 70                  mov r15b, byte ptr [rsp + 0x70]
003D0FB1  45 33 C9                        xor r9d, r9d
003D0FB4  66 45 39 4A 04                  cmp word ptr [r10 + 4], r9w
003D0FB9  0F 84 AA 04 00 00               je 0x1403d1469
003D0FBF  8B 8D 90 00 00 00               mov ecx, dword ptr [rbp + 0x90]
003D0FC5  85 C9                           test ecx, ecx
003D0FC7  0F 85 DB 05 00 00               jne 0x1403d15a8
003D0FCD  4C 8D 75 D8                     lea r14, [rbp - 0x28]
003D0FD1  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
003D0FD5  83 4D EC FF                     or dword ptr [rbp - 0x14], 0xffffffff
003D0FD9  44 8D 79 01                     lea r15d, [rcx + 1]
003D0FDD  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
003D0FE2  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
003D0FE6  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
003D0FEA  41 BC 00 00 00 02               mov r12d, 0x2000000
003D0FF0  44 85 A5 80 00 00 00            test dword ptr [rbp + 0x80], r12d
003D0FF7  0F 85 53 01 00 00               jne 0x1403d1150
003D0FFD  44 38 8D C8 00 00 00            cmp byte ptr [rbp + 0xc8], r9b
003D1004  0F 85 46 01 00 00               jne 0x1403d1150
003D100A  8A 85 D0 00 00 00               mov al, byte ptr [rbp + 0xd0]
003D1010  49 8B D5                        mov rdx, r13
003D1013  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
003D1017  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
003D101C  88 44 24 58                     mov byte ptr [rsp + 0x58], al
003D1020  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
003D1024  44 88 4C 24 50                  mov byte ptr [rsp + 0x50], r9b
003D1029  4D 8B CA                        mov r9, r10
003D102C  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
003D1030  8B CB                           mov ecx, ebx
003D1032  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
003D1037  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
003D103C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003D1041  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003D1045  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003D104A  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003D104F  E8 34 F6 FF FF                  call 0x1403d0688
003D1054  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
003D1058  45 33 C9                        xor r9d, r9d
003D105B  89 47 0C                        mov dword ptr [rdi + 0xc], eax
003D105E  45 39 4E 18                     cmp dword ptr [r14 + 0x18], r9d
003D1062  75 77                           jne 0x1403d10db
003D1064  41 8B 85 C8 00 00 00            mov eax, dword ptr [r13 + 0xc8]
003D106B  A8 10                           test al, 0x10
003D106D  0F 85 40 03 00 00               jne 0x1403d13b3
003D1073  44 8B A5 80 00 00 00            mov r12d, dword ptr [rbp + 0x80]
003D107A  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
003D107E  89 47 0C                        mov dword ptr [rdi + 0xc], eax
003D1081  45 39 4E 18                     cmp dword ptr [r14 + 0x18], r9d
003D1085  75 54                           jne 0x1403d10db
003D1087  E8 FC E6 11 00                  call 0x1404ef788
003D108C  41 8B 95 C8 00 00 00            mov edx, dword ptr [r13 + 0xc8]
003D1093  45 33 C9                        xor r9d, r9d
003D1096  85 C0                           test eax, eax
003D1098  0F 84 EF 01 00 00               je 0x1403d128d
003D109E  8B C2                           mov eax, edx
003D10A0  25 00 60 00 00                  and eax, 0x6000
003D10A5  3D 00 20 00 00                  cmp eax, 0x2000
003D10AA  0F 84 E7 01 00 00               je 0x1403d1297
003D10B0  41 0B DC                        or ebx, r12d
003D10B3  0F BA E2 0E                     bt edx, 0xe
003D10B7  0F 83 8E 03 00 00               jae 0x1403d144b
003D10BD  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
003D10C0  0B 4F 04                        or ecx, dword ptr [rdi + 4]
003D10C3  0B 1F                           or ebx, dword ptr [rdi]
003D10C5  F7 D1                           not ecx
003D10C7  23 CB                           and ecx, ebx
003D10C9  0F 85 E1 04 00 00               jne 0x1403d15b0
003D10CF  41 89 4E 18                     mov dword ptr [r14 + 0x18], ecx
003D10D3  85 C9                           test ecx, ecx
003D10D5  0F 84 BC 01 00 00               je 0x1403d1297
003D10DB  BB 22 00 00 C0                  mov ebx, 0xc0000022
003D10E0  41 8B F1                        mov esi, r9d
003D10E3  E9 3F 01 00 00                  jmp 0x1403d1227
003D10E8  66 85 C0                        test ax, ax
003D10EB  0F 84 60 04 00 00               je 0x1403d1551
003D10F1  41 8B 43 0C                     mov eax, dword ptr [r11 + 0xc]
003D10F5  85 C0                           test eax, eax
003D10F7  0F 84 86 FE FF FF               je 0x1403d0f83
003D10FD  49 03 C3                        add rax, r11
003D1100  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
003D1104  4C 8B D8                        mov r11, rax
003D1107  E9 7E FE FF FF                  jmp 0x1403d0f8a
003D110C  41 0B F7                        or esi, r15d
003D110F  41 0F BA E7 19                  bt r15d, 0x19
003D1114  0F 82 56 05 00 00               jb 0x1403d1670
003D111A  41 8B 8D C8 00 00 00            mov ecx, dword ptr [r13 + 0xc8]
003D1121  45 33 C9                        xor r9d, r9d
003D1124  0F BA E1 0E                     bt ecx, 0xe
003D1128  0F 83 D0 00 00 00               jae 0x1403d11fe
003D112E  B8 00 00 00 03                  mov eax, 0x3000000
003D1133  23 C8                           and ecx, eax
003D1135  3B C8                           cmp ecx, eax
003D1137  0F 85 43 05 00 00               jne 0x1403d1680
003D113D  C6 47 17 01                     mov byte ptr [rdi + 0x17], 1
003D1141  89 77 04                        mov dword ptr [rdi + 4], esi
003D1144  C6 47 15 01                     mov byte ptr [rdi + 0x15], 1
003D1148  44 89 0F                        mov dword ptr [rdi], r9d
003D114B  E9 AE 00 00 00                  jmp 0x1403d11fe
003D1150  8A 85 D0 00 00 00               mov al, byte ptr [rbp + 0xd0]
003D1156  4D 8B C2                        mov r8, r10
003D1159  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
003D115D  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
003D1162  88 44 24 58                     mov byte ptr [rsp + 0x58], al
003D1166  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
003D116A  44 88 4C 24 50                  mov byte ptr [rsp + 0x50], r9b
003D116F  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
003D1174  4D 8B CB                        mov r9, r11
003D1177  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
003D117B  49 8B CD                        mov rcx, r13
003D117E  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
003D1183  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
003D1188  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003D118D  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003D1191  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D1196  E8 55 FA F2 FF                  call 0x140300bf0
003D119B  41 8B 85 C8 00 00 00            mov eax, dword ptr [r13 + 0xc8]
003D11A2  A8 10                           test al, 0x10
003D11A4  0F 85 FC 02 00 00               jne 0x1403d14a6
003D11AA  45 8B 76 1C                     mov r14d, dword ptr [r14 + 0x1c]
003D11AE  E8 D5 E5 11 00                  call 0x1404ef788
003D11B3  41 8B 95 C8 00 00 00            mov edx, dword ptr [r13 + 0xc8]
003D11BA  45 33 C9                        xor r9d, r9d
003D11BD  85 C0                           test eax, eax
003D11BF  0F 84 73 01 00 00               je 0x1403d1338
003D11C5  0F BA E2 0E                     bt edx, 0xe
003D11C9  0F 82 55 03 00 00               jb 0x1403d1524
003D11CF  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
003D11D4  0F BA E2 0D                     bt edx, 0xd
003D11D8  0F 83 23 04 00 00               jae 0x1403d1601
003D11DE  44 38 8D C8 00 00 00            cmp byte ptr [rbp + 0xc8], r9b
003D11E5  0F 85 34 04 00 00               jne 0x1403d161f
003D11EB  41 8B C6                        mov eax, r14d
003D11EE  41 0B C4                        or eax, r12d
003D11F1  F7 D0                           not eax
003D11F3  85 C3                           test ebx, eax
003D11F5  0F 85 E0 FE FF FF               jne 0x1403d10db
003D11FB  41 0B F6                        or esi, r14d
003D11FE  44 8A 7C 24 70                  mov r15b, byte ptr [rsp + 0x70]
003D1203  41 8B D9                        mov ebx, r9d
003D1206  85 F6                           test esi, esi
003D1208  0F 84 7F 04 00 00               je 0x1403d168d
003D120E  44 0F 20 C0                     mov rax, cr8
003D1212  3C 02                           cmp al, 2
003D1214  0F 82 CD 00 00 00               jb 0x1403d12e7
003D121A  44 38 8D C8 00 00 00            cmp byte ptr [rbp + 0xc8], r9b
003D1221  0F 85 70 04 00 00               jne 0x1403d1697
003D1227  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
003D122B  89 18                           mov dword ptr [rax], ebx
003D122D  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
003D1231  89 30                           mov dword ptr [rax], esi
003D1233  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
003D1237  85 DB                           test ebx, ebx
003D1239  79 3C                           jns 0x1403d1277
003D123B  48 85 C0                        test rax, rax
003D123E  75 32                           jne 0x1403d1272
003D1240  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
003D1244  48 85 C0                        test rax, rax
003D1247  0F 85 97 04 00 00               jne 0x1403d16e4
003D124D  8A 44 24 71                     mov al, byte ptr [rsp + 0x71]
003D1251  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
003D1255  48 33 CC                        xor rcx, rsp
003D1258  E8 E3 B3 2D 00                  call 0x1406ac640
003D125D  48 81 C4 18 01 00 00            add rsp, 0x118
003D1264  41 5F                           pop r15
003D1266  41 5E                           pop r14
003D1268  41 5D                           pop r13
003D126A  41 5C                           pop r12
003D126C  5F                              pop rdi
003D126D  5E                              pop rsi
003D126E  5B                              pop rbx
003D126F  5D                              pop rbp
003D1270  C3                              ret
003D1271  CC                              int3
003D1272  44 88 08                        mov byte ptr [rax], r9b
003D1275  EB C9                           jmp 0x1403d1240
003D1277  48 85 C0                        test rax, rax
003D127A  74 03                           je 0x1403d127f
003D127C  C6 00 01                        mov byte ptr [rax], 1
003D127F  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
003D1283  48 85 C0                        test rax, rax
003D1286  74 C5                           je 0x1403d124d
003D1288  44 88 08                        mov byte ptr [rax], r9b
003D128B  EB C0                           jmp 0x1403d124d
003D128D  0F BA E2 0D                     bt edx, 0xd
003D1291  0F 83 19 FE FF FF               jae 0x1403d10b0
003D1297  41 0B F4                        or esi, r12d
003D129A  E9 5F FF FF FF                  jmp 0x1403d11fe
003D129F  48 8B 0D 5A 88 C0 00            mov rcx, qword ptr [rip + 0xc0885a]
003D12A6  45 8A C4                        mov r8b, r12b
003D12A9  49 8B D5                        mov rdx, r13
003D12AC  E8 6B 06 00 00                  call 0x1403d191c
003D12B1  45 33 C9                        xor r9d, r9d
003D12B4  84 C0                           test al, al
003D12B6  0F 84 8B 02 00 00               je 0x1403d1547
003D12BC  8B B5 A0 00 00 00               mov esi, dword ptr [rbp + 0xa0]
003D12C2  0F BA EE 18                     bts esi, 0x18
003D12C6  C7 44 24 74 01 00 00 00         mov dword ptr [rsp + 0x74], 1
003D12CE  C6 44 24 73 01                  mov byte ptr [rsp + 0x73], 1
003D12D3  81 E3 FF FF FF FE               and ebx, 0xfeffffff
003D12D9  0F 85 E3 7E 31 00               jne 0x1406e91c2
003D12DF  45 8A F9                        mov r15b, r9b
003D12E2  E9 1C FF FF FF                  jmp 0x1403d1203
003D12E7  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
003D12EB  85 C0                           test eax, eax
003D12ED  0F 84 27 FF FF FF               je 0x1403d121a
003D12F3  48 8B 7D D0                     mov rdi, qword ptr [rbp - 0x30]
003D12F7  45 8A C7                        mov r8b, r15b
003D12FA  44 8A 4C 24 72                  mov r9b, byte ptr [rsp + 0x72]
003D12FF  8B C8                           mov ecx, eax
003D1301  8A 54 24 73                     mov dl, byte ptr [rsp + 0x73]
003D1305  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003D130A  E8 AD FD 64 00                  call 0x140a210bc
003D130F  45 33 C9                        xor r9d, r9d
003D1312  48 85 FF                        test rdi, rdi
003D1315  0F 84 FF FE FF FF               je 0x1403d121a
003D131B  4C 39 0F                        cmp qword ptr [rdi], r9
003D131E  0F 85 F6 FE FF FF               jne 0x1403d121a
003D1324  44 88 4C 24 71                  mov byte ptr [rsp + 0x71], r9b
003D1329  48 C7 C3 17 00 00 C0            mov rbx, 0xffffffffc0000017
003D1330  41 8B F1                        mov esi, r9d
003D1333  E9 E2 FE FF FF                  jmp 0x1403d121a
003D1338  0F BA E2 0D                     bt edx, 0xd
003D133C  0F 83 D2 02 00 00               jae 0x1403d1614
003D1342  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
003D1347  E9 92 FE FF FF                  jmp 0x1403d11de
003D134C  48 8B 0D E5 87 C0 00            mov rcx, qword ptr [rip + 0xc087e5]
003D1353  45 8A C4                        mov r8b, r12b
003D1356  49 8B D5                        mov rdx, r13
003D1359  E8 BE 05 00 00                  call 0x1403d191c
003D135E  45 33 C9                        xor r9d, r9d
003D1361  84 C0                           test al, al
003D1363  74 29                           je 0x1403d138e
003D1365  41 0B F7                        or esi, r15d
003D1368  41 B7 01                        mov r15b, 1
003D136B  44 88 7C 24 70                  mov byte ptr [rsp + 0x70], r15b
003D1370  FF 44 24 74                     inc dword ptr [rsp + 0x74]
003D1374  81 E3 FF FF F7 FF               and ebx, 0xfff7ffff
003D137A  0F 85 34 FC FF FF               jne 0x1403d0fb4
003D1380  E9 7E FE FF FF                  jmp 0x1403d1203
003D1385  4D 8B 53 20                     mov r10, qword ptr [r11 + 0x20]
003D1389  E9 E6 FB FF FF                  jmp 0x1403d0f74
003D138E  48 8B 0D 93 87 C0 00            mov rcx, qword ptr [rip + 0xc08793]
003D1395  45 8A C4                        mov r8b, r12b
003D1398  49 8B D5                        mov rdx, r13
003D139B  E8 7C 05 00 00                  call 0x1403d191c
003D13A0  45 33 C9                        xor r9d, r9d
003D13A3  84 C0                           test al, al
003D13A5  0F 85 B3 01 00 00               jne 0x1403d155e
003D13AB  45 8A F9                        mov r15b, r9b
003D13AE  E9 01 FC FF FF                  jmp 0x1403d0fb4
003D13B3  A8 08                           test al, 8
003D13B5  0F 84 81 00 00 00               je 0x1403d143c
003D13BB  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
003D13BF  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
003D13C2  0B 0A                           or ecx, dword ptr [rdx]
003D13C4  F7 D1                           not ecx
003D13C6  23 4A 04                        and ecx, dword ptr [rdx + 4]
003D13C9  81 C9 00 00 0D 01               or ecx, 0x10d0000
003D13CF  44 8B A5 80 00 00 00            mov r12d, dword ptr [rbp + 0x80]
003D13D6  41 85 CC                        test r12d, ecx
003D13D9  0F 84 9B FC FF FF               je 0x1403d107a
003D13DF  8A 85 D0 00 00 00               mov al, byte ptr [rbp + 0xd0]
003D13E5  23 CB                           and ecx, ebx
003D13E7  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
003D13EB  49 8B D5                        mov rdx, r13
003D13EE  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
003D13F2  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
003D13F7  88 44 24 58                     mov byte ptr [rsp + 0x58], al
003D13FB  8B 85 90 00 00 00               mov eax, dword ptr [rbp + 0x90]
003D1401  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
003D1406  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
003D140A  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
003D140E  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
003D1413  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
003D1418  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003D141D  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003D1421  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003D1426  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003D142B  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
003D142F  E8 54 F2 FF FF                  call 0x1403d0688
003D1434  45 33 C9                        xor r9d, r9d
003D1437  E9 3E FC FF FF                  jmp 0x1403d107a
003D143C  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
003D1440  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
003D1443  81 C9 FF FF 1F 00               or ecx, 0x1fffff
003D1449  EB 84                           jmp 0x1403d13cf
003D144B  44 38 4F 14                     cmp byte ptr [rdi + 0x14], r9b
003D144F  75 08                           jne 0x1403d1459
003D1451  41 8B C9                        mov ecx, r9d
003D1454  E9 76 FC FF FF                  jmp 0x1403d10cf
003D1459  8B 47 04                        mov eax, dword ptr [rdi + 4]
003D145C  8B CB                           mov ecx, ebx
003D145E  0B 0F                           or ecx, dword ptr [rdi]
003D1460  F7 D0                           not eax
003D1462  23 C8                           and ecx, eax
003D1464  E9 66 FC FF FF                  jmp 0x1403d10cf
003D1469  89 5F 0C                        mov dword ptr [rdi + 0xc], ebx
003D146C  E8 17 E3 11 00                  call 0x1404ef788
003D1471  41 8B 8D C8 00 00 00            mov ecx, dword ptr [r13 + 0xc8]
003D1478  0F BA E1 0E                     bt ecx, 0xe
003D147C  0F 82 EC 00 00 00               jb 0x1403d156e
003D1482  41 BC 00 00 00 02               mov r12d, 0x2000000
003D1488  45 33 C9                        xor r9d, r9d
003D148B  41 3B DC                        cmp ebx, r12d
003D148E  0F 84 E5 00 00 00               je 0x1403d1579
003D1494  85 DB                           test ebx, ebx
003D1496  0F 84 EA 00 00 00               je 0x1403d1586
003D149C  BB 22 00 00 C0                  mov ebx, 0xc0000022
003D14A1  E9 8A FE FF FF                  jmp 0x1403d1330
003D14A6  A8 08                           test al, 8
003D14A8  74 6B                           je 0x1403d1515
003D14AA  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
003D14AE  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
003D14B1  0B 0A                           or ecx, dword ptr [rdx]
003D14B3  F7 D1                           not ecx
003D14B5  23 4A 04                        and ecx, dword ptr [rdx + 4]
003D14B8  81 C9 00 00 0D 01               or ecx, 0x10d0000
003D14BE  8A 85 D0 00 00 00               mov al, byte ptr [rbp + 0xd0]
003D14C4  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
003D14C8  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
003D14CC  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
003D14D0  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
003D14D5  88 44 24 58                     mov byte ptr [rsp + 0x58], al
003D14D9  8B 85 90 00 00 00               mov eax, dword ptr [rbp + 0x90]
003D14DF  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
003D14E4  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
003D14E8  49 8B CD                        mov rcx, r13
003D14EB  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003D14EF  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
003D14F3  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
003D14F8  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
003D14FD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003D1502  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003D1506  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D150B  E8 E0 F6 F2 FF                  call 0x140300bf0
003D1510  E9 95 FC FF FF                  jmp 0x1403d11aa
003D1515  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
003D1519  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
003D151C  81 C9 FF FF 1F 00               or ecx, 0x1fffff
003D1522  EB 9A                           jmp 0x1403d14be
003D1524  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
003D1527  0B 4F 04                        or ecx, dword ptr [rdi + 4]
003D152A  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
003D152F  44 23 F1                        and r14d, ecx
003D1532  45 3B 70 1C                     cmp r14d, dword ptr [r8 + 0x1c]
003D1536  0F 85 96 00 00 00               jne 0x1403d15d2
003D153C  8B 07                           mov eax, dword ptr [rdi]
003D153E  F7 D0                           not eax
003D1540  23 F0                           and esi, eax
003D1542  E9 97 FC FF FF                  jmp 0x1403d11de
003D1547  BB 61 00 00 C0                  mov ebx, 0xc0000061
003D154C  E9 DF FD FF FF                  jmp 0x1403d1330
003D1551  4D 8B 5B 18                     mov r11, qword ptr [r11 + 0x18]
003D1555  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
003D1559  E9 2C FA FF FF                  jmp 0x1403d0f8a
003D155E  41 0B F7                        or esi, r15d
003D1561  C6 44 24 72 01                  mov byte ptr [rsp + 0x72], 1
003D1566  45 8A F9                        mov r15b, r9b
003D1569  E9 02 FE FF FF                  jmp 0x1403d1370
003D156E  8B 07                           mov eax, dword ptr [rdi]
003D1570  F7 D0                           not eax
003D1572  23 F0                           and esi, eax
003D1574  E9 09 FF FF FF                  jmp 0x1403d1482
003D1579  85 F6                           test esi, esi
003D157B  0F 84 1B FF FF FF               je 0x1403d149c
003D1581  E9 4A 7C 31 00                  jmp 0x1406e91d0
003D1586  44 39 0F                        cmp dword ptr [rdi], r9d
003D1589  0F 84 0D FF FF FF               je 0x1403d149c
003D158F  85 F6                           test esi, esi
003D1591  0F 84 05 FF FF FF               je 0x1403d149c
003D1597  F7 C1 00 60 00 00               test ecx, 0x6000
003D159D  0F 84 2D 7C 31 00               je 0x1406e91d0
003D15A3  E9 F4 FE FF FF                  jmp 0x1403d149c
003D15A8  44 8B F9                        mov r15d, ecx
003D15AB  E9 3A FA FF FF                  jmp 0x1403d0fea
003D15B0  44 39 4F 0C                     cmp dword ptr [rdi + 0xc], r9d
003D15B4  0F 85 15 FB FF FF               jne 0x1403d10cf
003D15BA  B8 00 00 00 03                  mov eax, 0x3000000
003D15BF  23 D0                           and edx, eax
003D15C1  3B D0                           cmp edx, eax
003D15C3  0F 85 06 FB FF FF               jne 0x1403d10cf
003D15C9  C6 47 17 01                     mov byte ptr [rdi + 0x17], 1
003D15CD  E9 7F FE FF FF                  jmp 0x1403d1451
003D15D2  B8 00 00 00 03                  mov eax, 0x3000000
003D15D7  23 D0                           and edx, eax
003D15D9  3B D0                           cmp edx, eax
003D15DB  0F 85 5B FF FF FF               jne 0x1403d153c
003D15E1  45 85 F6                        test r14d, r14d
003D15E4  0F 84 EE 7B 31 00               je 0x1406e91d8
003D15EA  44 85 A5 80 00 00 00            test dword ptr [rbp + 0x80], r12d
003D15F1  0F 85 45 FF FF FF               jne 0x1403d153c
003D15F7  E9 DC 7B 31 00                  jmp 0x1406e91d8
003D15FC  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
003D1601  44 38 4F 14                     cmp byte ptr [rdi + 0x14], r9b
003D1605  0F 84 D3 FB FF FF               je 0x1403d11de
003D160B  44 23 77 04                     and r14d, dword ptr [rdi + 4]
003D160F  E9 28 FF FF FF                  jmp 0x1403d153c
003D1614  0F BA E2 0E                     bt edx, 0xe
003D1618  73 E2                           jae 0x1403d15fc
003D161A  E9 05 FF FF FF                  jmp 0x1403d1524
003D161F  8B BD 80 00 00 00               mov edi, dword ptr [rbp + 0x80]
003D1625  B9 FF FF FF FD                  mov ecx, 0xfdffffff
003D162A  8B C7                           mov eax, edi
003D162C  45 8A F1                        mov r14b, r9b
003D162F  0B FE                           or edi, esi
003D1631  45 8A E9                        mov r13b, r9b
003D1634  41 85 C4                        test r12d, eax
003D1637  44 8B D7                        mov r10d, edi
003D163A  8B D7                           mov edx, edi
003D163C  44 0F 45 D1                     cmovne r10d, ecx
003D1640  23 D1                           and edx, ecx
003D1642  41 85 C4                        test r12d, eax
003D1645  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
003D1649  0F 44 D7                        cmove edx, edi
003D164C  45 85 FF                        test r15d, r15d
003D164F  0F 84 BE 7B 31 00               je 0x1406e9213
003D1655  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
003D1659  49 83 C0 1C                     add r8, 0x1c
003D165D  49 2B FC                        sub rdi, r12
003D1660  45 8B CF                        mov r9d, r15d
003D1663  49 8B CC                        mov rcx, r12
003D1666  BB 22 00 00 C0                  mov ebx, 0xc0000022
003D166B  E9 75 7B 31 00                  jmp 0x1406e91e5
003D1670  B9 FF FF FF FD                  mov ecx, 0xfdffffff
003D1675  23 F1                           and esi, ecx
003D1677  41 0B 71 0C                     or esi, dword ptr [r9 + 0xc]
003D167B  E9 9A FA FF FF                  jmp 0x1403d111a
003D1680  44 88 4F 15                     mov byte ptr [rdi + 0x15], r9b
003D1684  44 89 4F 04                     mov dword ptr [rdi + 4], r9d
003D1688  E9 0F FE FF FF                  jmp 0x1403d149c
003D168D  BB 22 00 00 C0                  mov ebx, 0xc0000022
003D1692  E9 83 FB FF FF                  jmp 0x1403d121a
003D1697  44 8B 95 90 00 00 00            mov r10d, dword ptr [rbp + 0x90]
003D169E  41 8B D1                        mov edx, r9d
003D16A1  45 85 D2                        test r10d, r10d
003D16A4  0F 84 89 FB FF FF               je 0x1403d1233
003D16AA  4C 8B 5D 80                     mov r11, qword ptr [rbp - 0x80]
003D16AE  41 BE 04 00 00 00               mov r14d, 4
003D16B4  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
003D16B8  45 3B D6                        cmp r10d, r14d
003D16BB  0F 82 AB 7C 31 00               jb 0x1406e936c
003D16C1  41 8D 42 FF                     lea eax, [r10 - 1]
003D16C5  49 8D 3C 83                     lea rdi, [r11 + rax*4]
003D16C9  49 8D 04 81                     lea rax, [r9 + rax*4]
003D16CD  4C 3B D8                        cmp r11, rax
003D16D0  0F 87 59 7C 31 00               ja 0x1406e932f
003D16D6  49 3B F9                        cmp rdi, r9
003D16D9  0F 82 50 7C 31 00               jb 0x1406e932f
003D16DF  E9 88 7C 31 00                  jmp 0x1406e936c
003D16E4  C6 00 01                        mov byte ptr [rax], 1
003D16E7  E9 61 FB FF FF                  jmp 0x1403d124d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAccessCheck(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9, unsigned __int8 a10, __int64 a11, __int64 a12, __int64 a13, unsigned __int8 a14, unsigned __int8 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m100;
    unsigned __int8 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m6C;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE5;
    unsigned __int8 v_stack_mE6;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p70;
    unsigned __int8 v_stack_p71;
    unsigned __int8 v_stack_p72;
    unsigned __int8 v_stack_p73;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (280);
    result = (*(unsigned __int64 *)(v_rip + 10721484)) ^ (v_rsp);
    v_stack_m50 = result;
    v_r10 = 0;
    if (a4 == 0) { a4 = a3; }
    v_stack_mD8 = a11;
    v_stack_mB8 = a13;
    v_stack_m88 = a12;
    v_stack_mA8 = a17;
    v_stack_m90 = a19;
    v_stack_mA0 = a3;
    v_stack_mB0 = a2;
    v_stack_mE0 = a6;
    v_stack_mC8 = a8;
    v_stack_m98 = a18;
    v_stack_mE7 = 1;
    v_stack_mE4 = 0;
    v_stack_mE5 = 0;
    v_stack_mE8 = 0;
    v_stack_mE6 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    if (condition_is_below) goto loc_003D129F;
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) & ((unsigned __int16)(v_r10 + 4)));
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) & ((unsigned __int16)((unsigned int)(0x8000ULL))));
    if ((unsigned __int16)(a3) == 0) goto loc_003D0F74;
    if ((unsigned __int16)(result) == 0) goto loc_003D1385;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) != 0) {
        v_r10 = a1 + (unsigned int)(*(unsigned int *)(a1 + 16)) * 1;
    }
    a1 = 0;
    v_stack_mC0 = v_r10;
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 2))) & (16)) != 0) goto loc_003D10E8;
loc_003D0F83:
    v_stack_mD0 = 0;
loc_003D0F8A:
    if ((unsigned __int16)(a3) == 0) goto loc_003D110C;
    if (v_r10 == 0) goto loc_003D110C;
    if ((((unsigned int)((unsigned int)(0x80000ULL))) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5)))))) != 0) goto loc_003D134C;
    a4 = 0;
loc_003D0FB4:
    if ((*(unsigned __int16 *)(v_r10 + 4)) == 0) goto loc_003D1469;
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_003D15A8;
    v_stack_m70 = v_xmm0;
    v_stack_mE0 = v_stack_m80;
    v_stack_m80 = v_xmm0;
    v_stack_m60 = v_xmm0;
loc_003D0FEA:
    if (((v_stack_p28) & ((unsigned int)((unsigned int)(0x2000000ULL)))) != 0) goto loc_003D1150;
    if (a14 != 0) goto loc_003D1150;
    v_stack_mF8 = a16;
    v_stack_m100 = a15;
    v_stack_m108 = 0;
    v_stack_m110 = (unsigned int)((unsigned int)(a7));
    v_stack_m118 = v_stack_m80;
    v_stack_m120 = (unsigned int)((unsigned int)(a7) + 1);
    v_stack_m128 = v_stack_mB0;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = 0;
    result = SepNormalAccessCheck((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5))))), 0, v_stack_mA0, v_r10);
    a4 = 0;
    *(unsigned int *)(a16 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 24)));
    if ((*(unsigned int *)(v_stack_m80 + 24)) != 0) goto loc_003D10DB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 200)))) & (16)) != 0) goto loc_003D13B3;
loc_003D107A:
    *(unsigned int *)(a16 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 24)));
    if ((*(unsigned int *)(v_stack_m80 + 24)) != 0) goto loc_003D10DB;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5))))), 0, v_stack_mA0, a4);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_003D128D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 200))))) & (0x6000ULL));
    if (((unsigned int)(result)) == 0x2000ULL) goto loc_003D1297;
loc_003D10B0:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) | ((unsigned int)((unsigned int)(a5))));
    if (condition_is_above_or_equal) goto loc_003D144B;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a16 + 8))) | (*(unsigned int *)(a16 + 4)));
    v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(a16)));
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_rbx)));
    if (condition_is_not_equal) goto loc_003D15B0;
loc_003D10CF:
    *(unsigned int *)(v_stack_m80 + 24) = (unsigned int)(a1);
    if ((unsigned int)(a1) == 0) goto loc_003D1297;
loc_003D10DB:
    goto loc_003D1227;
loc_003D10E8:
    if ((unsigned __int16)(result) == 0) goto loc_003D1551;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 12))) == 0) goto loc_003D0F83;
    result = ((unsigned int)(*(unsigned int *)(0 + 12))) + (0);
    v_stack_mD0 = result;
    goto loc_003D0F8A;
loc_003D110C:
    v_rsi = (unsigned int)((0) | ((unsigned int)((unsigned int)(a7) + 1)));
    if (condition_is_below) goto loc_003D1670;
loc_003D111A:
    a4 = 0;
    if (condition_is_above_or_equal) goto loc_003D11FE;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003D1680;
    *(unsigned __int8 *)(a16 + 23) = 1;
    *(unsigned int *)(a16 + 4) = (unsigned int)(v_rsi);
    *(unsigned __int8 *)(a16 + 21) = 1;
    *(unsigned int *)(a16) = 0;
    goto loc_003D11FE;
loc_003D1150:
    v_stack_mF8 = a16;
    v_stack_m100 = a15;
    v_stack_m108 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = (unsigned int)(a1);
    v_stack_m120 = v_stack_m80;
    v_stack_m128 = (unsigned int)((unsigned int)(a7) + 1);
    v_stack_m130 = v_stack_mB0;
    v_stack_m138 = v_stack_mA8;
    result = SepMaximumAccessCheck(0, v_stack_mA0, v_r10, result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 200)))) & (16)) != 0) goto loc_003D14A6;
loc_003D11AA:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(0, v_stack_mA0, v_r10, result);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_003D1338;
    if (condition_is_below) goto loc_003D1524;
    if (condition_is_above_or_equal) goto loc_003D1601;
loc_003D11DE:
    if (a14 != 0) goto loc_003D161F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 28))))) | ((unsigned int)((unsigned int)(a5))));
    result = (unsigned int)(~(result));
    if ((((unsigned int)((unsigned int)(0xC0000022ULL))) & ((unsigned int)(result))) != 0) goto loc_003D10DB;
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 28)))));
loc_003D11FE:
loc_003D1203:
    if ((unsigned int)(v_rsi) == 0) goto loc_003D168D;
    if (((unsigned __int8)(v_cr8)) < 2) goto loc_003D12E7;
loc_003D121A:
    if (a14 != 0) goto loc_003D1697;
loc_003D1227:
    *(unsigned int *)(v_stack_mB8) = 0;
    *(unsigned int *)(v_stack_mD8) = (unsigned int)(v_rsi);
loc_003D1233:
    if (!sign_flag) goto loc_003D1277;
    if (v_stack_m98 != 0) goto loc_003D1272;
loc_003D1240:
    if (v_stack_m90 != 0) goto loc_003D16E4;
loc_003D124D:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(a4 + 200)), v_stack_mE0, a4);
    v_rsp = (v_rsp) + (280);
    return result;
loc_003D1272:
    *(unsigned __int8 *)(result) = 0;
    goto loc_003D1240;
loc_003D1277:
    if (result != 0) {
        *(unsigned __int8 *)(result) = 1;
    }
    if (v_stack_m90 == 0) goto loc_003D124D;
    *(unsigned __int8 *)(v_stack_m90) = 0;
    goto loc_003D124D;
loc_003D128D:
    if (condition_is_above_or_equal) goto loc_003D10B0;
loc_003D1297:
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)((unsigned int)(a5))));
    goto loc_003D11FE;
loc_003D129F:
    result = SepSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 12617818), 0, (unsigned __int8)((unsigned int)(a5)), a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003D1547;
    v_stack_p74 = 1;
    v_stack_p73 = 1;
    v_rbx = (unsigned int)((0) & (0xFEFFFFFFULL));
    goto loc_003D1203;
loc_003D12E7:
    if ((unsigned int)((unsigned int)(v_stack_p74)) == 0) goto loc_003D121A;
    v_stack_p20 = v_stack_m88;
    result = SepAssemblePrivileges((unsigned int)((unsigned int)((unsigned int)(v_stack_p74))), v_stack_p73, 0, v_stack_p72);
    a4 = 0;
    if (v_stack_m88 == 0) goto loc_003D121A;
    if ((*(unsigned __int64 *)(v_stack_m88)) != 0) goto loc_003D121A;
    v_stack_p71 = 0;
loc_003D1330:
    goto loc_003D121A;
loc_003D1338:
    if ((*(unsigned __int64 *)(v_stack_m88)) >= 0) goto loc_003D1614;
    goto loc_003D11DE;
loc_003D134C:
    result = SepSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 12617701), 0, (unsigned __int8)((unsigned int)(a5)), a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003D138E;
    v_rsi = (unsigned int)((0) | (0));
    v_stack_p70 = 1;
loc_003D1370:
    v_rbx = (unsigned int)((0xFFFFFFFFC0000017ULL) & (0xFFF7FFFFULL));
    if (condition_is_not_equal) goto loc_003D0FB4;
    goto loc_003D1203;
loc_003D1385:
    goto loc_003D0F74;
loc_003D138E:
    result = SepSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 12617619), 0, (unsigned __int8)((unsigned int)(a5)), a4);
    a4 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_003D155E;
    goto loc_003D0FB4;
loc_003D13B3:
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_003D143C;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC8 + 8))) | (*(unsigned int *)(v_stack_mC8)));
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(v_stack_mC8 + 4)));
    a1 = (unsigned int)((a1) | (0x10D0000ULL));
loc_003D13CF:
    if ((((unsigned int)((unsigned int)(a5))) & ((unsigned int)(a1))) == 0) goto loc_003D107A;
    a1 = (unsigned int)((a1) & ((unsigned int)(v_rbx)));
    v_stack_p60 = v_stack_m88;
    v_stack_p58 = a15;
    v_stack_p50 = 1;
    v_stack_p48 = (unsigned int)((unsigned int)(a7));
    v_stack_p40 = (unsigned int)(*(unsigned int *)(v_stack_m80 + 28));
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_mB0;
    v_stack_p28 = v_stack_mA8;
    v_stack_p20 = v_stack_mD0;
    result = SepNormalAccessCheck(a1, 0, v_stack_mA0, v_stack_mC0);
    a4 = 0;
    goto loc_003D107A;
loc_003D143C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC8 + 12))) | (0x1FFFFFULL));
    goto loc_003D13CF;
loc_003D144B:
    if ((*(unsigned __int8 *)(v_stack_m88 + 20)) != 0) goto loc_003D1459;
loc_003D1451:
    goto loc_003D10CF;
loc_003D1459:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) | (*(unsigned int *)(v_stack_m88)));
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_stack_m88 + 4))));
    a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    goto loc_003D10CF;
loc_003D1469:
    *(unsigned int *)(v_stack_m88 + 12) = (unsigned int)(v_rbx);
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, 0, v_stack_mA0, a4);
    if (condition_is_below) goto loc_003D156E;
loc_003D1482:
    a4 = 0;
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)(0x2000000ULL)))) goto loc_003D1579;
    if ((unsigned int)(v_rbx) == 0) goto loc_003D1586;
loc_003D149C:
    goto loc_003D1330;
loc_003D14A6:
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_003D1515;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC8 + 8))) | (*(unsigned int *)(v_stack_mC8)));
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(v_stack_mC8 + 4)));
    a1 = (unsigned int)((a1) | (0x10D0000ULL));
loc_003D14BE:
    v_stack_p60 = v_stack_m88;
    v_stack_p58 = a15;
    v_stack_p50 = 1;
    v_stack_p48 = (unsigned int)(a1);
    v_stack_p40 = (unsigned int)((unsigned int)(a7));
    v_stack_p38 = (unsigned int)(*(unsigned int *)(v_stack_m80 + 28));
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = v_stack_mA8;
    result = SepMaximumAccessCheck(0, v_stack_mA0, v_stack_mC0, v_stack_mD0);
    goto loc_003D11AA;
loc_003D1515:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC8 + 12))) | (0x1FFFFFULL));
    goto loc_003D14BE;
loc_003D1524:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 8))) | (*(unsigned int *)(v_stack_m88 + 4)));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 28))) & ((unsigned int)(a1)));
    if (((unsigned int)(v_r14)) != (*(unsigned int *)(v_stack_p78 + 28))) goto loc_003D15D2;
loc_003D153C:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_stack_m88))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(result)));
    goto loc_003D11DE;
loc_003D1547:
    goto loc_003D1330;
loc_003D1551:
    v_stack_mD0 = *(unsigned __int64 *)(result + 24);
    goto loc_003D0F8A;
loc_003D155E:
    v_rsi = (unsigned int)((v_rsi) | (0));
    v_stack_p72 = 1;
    goto loc_003D1370;
loc_003D156E:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_stack_m88))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(result)));
    goto loc_003D1482;
loc_003D1579:
    if ((unsigned int)(v_rsi) == 0) goto loc_003D149C;
loc_003D1586:
    if ((*(unsigned int *)(v_stack_m88)) == ((unsigned int)(v_stack_mD0))) goto loc_003D149C;
    if ((unsigned int)(v_rsi) == 0) goto loc_003D149C;
    goto loc_003D149C;
loc_003D15A8:
    goto loc_003D0FEA;
loc_003D15B0:
    if ((*(unsigned int *)(v_stack_m88 + 12)) != ((unsigned int)(v_stack_mD0))) goto loc_003D10CF;
    a2 = (unsigned int)((v_stack_mA0) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003D10CF;
    *(unsigned __int8 *)(v_stack_m88 + 23) = 1;
    goto loc_003D1451;
loc_003D15D2:
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003D153C;
    if (((v_stack_p28) & ((unsigned int)((unsigned int)(0x2000000ULL)))) != 0) goto loc_003D153C;
loc_003D15FC:
loc_003D1601:
    if ((*(unsigned __int8 *)(v_stack_m88 + 20)) == ((unsigned __int8)(v_stack_mD0))) goto loc_003D11DE;
    v_r14 = (unsigned int)((v_r14) & (*(unsigned int *)(v_stack_m88 + 4)));
    goto loc_003D153C;
loc_003D1614:
    if (condition_is_above_or_equal) goto loc_003D15FC;
    goto loc_003D1524;
loc_003D161F:
    v_rdi = (unsigned int)(((unsigned int)(a5)) | ((unsigned int)(v_rsi)));
    v_r10 = (unsigned int)((unsigned int)(v_rdi));
    if ((((unsigned int)((unsigned int)(0x2000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5)))))) != 0) { v_r10 = (unsigned int)((unsigned int)(0xFDFFFFFFULL)); }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & ((unsigned int)((unsigned int)(0xFDFFFFFFULL))));
    if ((((unsigned int)((unsigned int)(0x2000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5)))))) == 0) { a2 = (unsigned int)(v_rdi); }
    a3 = (v_stack_p78) + (28);
    v_rdi = (v_stack_mD8) - (v_stack_mB8);
loc_003D1670:
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)((unsigned int)(0xFDFFFFFFULL))));
    v_rsi = (unsigned int)((v_rsi) | (*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 12)));
    goto loc_003D111A;
loc_003D1680:
    *(unsigned __int8 *)(v_rdi + 21) = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))));
    goto loc_003D149C;
loc_003D168D:
    goto loc_003D121A;
loc_003D1697:
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_003D1233;
loc_003D16E4:
    *(unsigned __int8 *)(v_stack_mB8 + (unsigned int)(a7) - 1 * 4) = 1;
    goto loc_003D124D;
}
```

## 5. (Beta) C Style

```c
int64_t SepAccessCheck(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8, uint32_t Arg9, uint8_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, uint8_t Arg14, uint8_t Arg15, void *Arg16, int64_t Arg17, int64_t Arg18, int64_t Arg19)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg16 = (uint8_t *)Arg16;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m100;
    uint8_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m6C;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE5;
    uint8_t v_stack_mE6;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint8_t v_stack_p50;
    uint8_t v_stack_p58;
    uint64_t v_stack_p60;
    uint8_t v_stack_p70;
    uint8_t v_stack_p71;
    uint8_t v_stack_p72;
    uint8_t v_stack_p73;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (280);
    result = (*(uint64_t *)(v_rip + 0xA398CC)) ^ (local_rsp);
    v_stack_m50 = result;
    local_r10 = 0;
    if (Arg4 == 0) { Arg4 = Arg3; }
    v_stack_mD8 = Arg11;
    v_stack_mB8 = Arg13;
    v_stack_m88 = Arg12;
    v_stack_mA8 = Arg17;
    v_stack_m90 = Arg19;
    v_stack_mA0 = Arg3;
    v_stack_mB0 = Arg2;
    v_stack_mE0 = Arg6;
    v_stack_mC8 = Arg8;
    v_stack_m98 = Arg18;
    v_stack_mE7 = 1;
    v_stack_mE4 = 0;
    v_stack_mE5 = 0;
    v_stack_mE8 = 0;
    v_stack_mE6 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    if (condition_is_below) goto loc_003D129F;
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x2))) & ((uint16_t)(local_r10 + 4)));
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x2))) & ((uint16_t)((uint32_t)(0x8000ULL))));
    if ((uint16_t)(Arg3) == 0) goto loc_003D0F74;
    if ((uint16_t)(result) == 0) goto loc_003D1385;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) != 0) {
        local_r10 = Arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 1;
    }
    Arg1 = 0;
    v_stack_mC0 = local_r10;
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0x2))) & (16)) != 0) goto loc_003D10E8;
loc_003D0F83:
    v_stack_mD0 = 0;
loc_003D0F8A:
    if ((uint16_t)(Arg3) == 0) goto loc_003D110C;
    if (local_r10 == 0) goto loc_003D110C;
    if ((((uint32_t)((uint32_t)(0x80000ULL))) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5)))))) != 0) goto loc_003D134C;
    Arg4 = 0;
loc_003D0FB4:
    if ((*(uint16_t *)(local_r10 + 0x4)) == 0) goto loc_003D1469;
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_003D15A8;
    v_stack_m70 = v_xmm0;
    v_stack_mE0 = v_stack_m80;
    v_stack_m80 = v_xmm0;
    v_stack_m60 = v_xmm0;
loc_003D0FEA:
    if (((v_stack_p28) & ((uint32_t)((uint32_t)(0x2000000ULL)))) != 0) goto loc_003D1150;
    if (Arg14 != 0) goto loc_003D1150;
    v_stack_mF8 = Arg16;
    v_stack_m100 = Arg15;
    v_stack_m108 = 0;
    v_stack_m110 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m118 = v_stack_m80;
    v_stack_m120 = (uint32_t)((uint32_t)(Arg7) + 1);
    v_stack_m128 = v_stack_mB0;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = 0;
    result = SepNormalAccessCheck((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5))))), 0, v_stack_mA0, local_r10);
    Arg4 = 0;
    *(uint32_t *)(arg16 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x18)));
    if ((*(uint32_t *)(v_stack_m80 + 0x18)) != 0) goto loc_003D10DB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0xC8)))) & (16)) != 0) goto loc_003D13B3;
loc_003D107A:
    *(uint32_t *)(arg16 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x18)));
    if ((*(uint32_t *)(v_stack_m80 + 0x18)) != 0) goto loc_003D10DB;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5))))), 0, v_stack_mA0, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_003D128D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0xC8))))) & (0x6000ULL));
    if (((uint32_t)(result)) == 0x2000ULL) goto loc_003D1297;
loc_003D10B0:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) | ((uint32_t)((uint32_t)(Arg5))));
    if (condition_is_above_or_equal) goto loc_003D144B;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg16 + 0x8))) | (*(uint32_t *)(arg16 + 0x4)));
    local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(arg16)));
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_rbx)));
    if (condition_is_not_equal) goto loc_003D15B0;
loc_003D10CF:
    *(uint32_t *)(v_stack_m80 + 0x18) = (uint32_t)(Arg1);
    if ((uint32_t)(Arg1) == 0) goto loc_003D1297;
loc_003D10DB:
    goto loc_003D1227;
loc_003D10E8:
    if ((uint16_t)(result) == 0) goto loc_003D1551;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xC))) == 0) goto loc_003D0F83;
    result = ((uint32_t)(*(uint32_t *)(0 + 0xC))) + (0);
    v_stack_mD0 = result;
    goto loc_003D0F8A;
loc_003D110C:
    local_rsi = (uint32_t)((0) | ((uint32_t)((uint32_t)(Arg7) + 1)));
    if (condition_is_below) goto loc_003D1670;
loc_003D111A:
    Arg4 = 0;
    if (condition_is_above_or_equal) goto loc_003D11FE;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003D1680;
    *(uint8_t *)(arg16 + 0x17) = 1;
    *(uint32_t *)(arg16 + 0x4) = (uint32_t)(local_rsi);
    *(uint8_t *)(arg16 + 0x15) = 1;
    *(uint32_t *)(arg16) = 0;
    goto loc_003D11FE;
loc_003D1150:
    v_stack_mF8 = Arg16;
    v_stack_m100 = Arg15;
    v_stack_m108 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = (uint32_t)(Arg1);
    v_stack_m120 = v_stack_m80;
    v_stack_m128 = (uint32_t)((uint32_t)(Arg7) + 1);
    v_stack_m130 = v_stack_mB0;
    v_stack_m138 = v_stack_mA8;
    result = SepMaximumAccessCheck(0, v_stack_mA0, local_r10, result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0xC8)))) & (16)) != 0) goto loc_003D14A6;
loc_003D11AA:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(0, v_stack_mA0, local_r10, result);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_003D1338;
    if (condition_is_below) goto loc_003D1524;
    if (condition_is_above_or_equal) goto loc_003D1601;
loc_003D11DE:
    if (Arg14 != 0) goto loc_003D161F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x1C))))) | ((uint32_t)((uint32_t)(Arg5))));
    result = (uint32_t)(~(result));
    if ((((uint32_t)((uint32_t)(0xC0000022ULL))) & ((uint32_t)(result))) != 0) goto loc_003D10DB;
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x1C)))));
loc_003D11FE:
loc_003D1203:
    if ((uint32_t)(local_rsi) == 0) goto loc_003D168D;
    if (((uint8_t)(v_cr8)) < 2) goto loc_003D12E7;
loc_003D121A:
    if (Arg14 != 0) goto loc_003D1697;
loc_003D1227:
    *(uint32_t *)(v_stack_mB8) = 0;
    *(uint32_t *)(v_stack_mD8) = (uint32_t)(local_rsi);
loc_003D1233:
    if (!sign_flag) goto loc_003D1277;
    if (v_stack_m98 != 0) goto loc_003D1272;
loc_003D1240:
    if (v_stack_m90 != 0) goto loc_003D16E4;
loc_003D124D:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(Arg4 + 0xC8)), v_stack_mE0, Arg4);
    local_rsp = (local_rsp) + (280);
    return result;
loc_003D1272:
    *(uint8_t *)(result) = 0;
    goto loc_003D1240;
loc_003D1277:
    if (result != 0) {
        *(uint8_t *)(result) = 1;
    }
    if (v_stack_m90 == 0) goto loc_003D124D;
    *(uint8_t *)(v_stack_m90) = 0;
    goto loc_003D124D;
loc_003D128D:
    if (condition_is_above_or_equal) goto loc_003D10B0;
loc_003D1297:
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)((uint32_t)(Arg5))));
    goto loc_003D11FE;
loc_003D129F:
    result = SepSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0xC0885A), 0, (uint8_t)((uint32_t)(Arg5)), Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_003D1547;
    v_stack_p74 = 1;
    v_stack_p73 = 1;
    local_rbx = (uint32_t)((0) & (0xFEFFFFFFULL));
    goto loc_003D1203;
loc_003D12E7:
    if ((uint32_t)((uint32_t)(v_stack_p74)) == 0) goto loc_003D121A;
    v_stack_p20 = v_stack_m88;
    result = SepAssemblePrivileges((uint32_t)((uint32_t)((uint32_t)(v_stack_p74))), v_stack_p73, 0, v_stack_p72);
    Arg4 = 0;
    if (v_stack_m88 == 0) goto loc_003D121A;
    if ((*(uint64_t *)(v_stack_m88)) != 0) goto loc_003D121A;
    v_stack_p71 = 0;
loc_003D1330:
    goto loc_003D121A;
loc_003D1338:
    if ((*(uint64_t *)(v_stack_m88)) >= 0) goto loc_003D1614;
    goto loc_003D11DE;
loc_003D134C:
    result = SepSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0xC087E5), 0, (uint8_t)((uint32_t)(Arg5)), Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_003D138E;
    local_rsi = (uint32_t)((0) | (0));
    v_stack_p70 = 1;
loc_003D1370:
    local_rbx = (uint32_t)((0xFFFFFFFFC0000017ULL) & (0xFFF7FFFFULL));
    if (condition_is_not_equal) goto loc_003D0FB4;
    goto loc_003D1203;
loc_003D1385:
    goto loc_003D0F74;
loc_003D138E:
    result = SepSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0xC08793), 0, (uint8_t)((uint32_t)(Arg5)), Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) != 0) goto loc_003D155E;
    goto loc_003D0FB4;
loc_003D13B3:
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_003D143C;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x8))) | (*(uint32_t *)(v_stack_mC8)));
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(v_stack_mC8 + 0x4)));
    Arg1 = (uint32_t)((Arg1) | (0x10D0000ULL));
loc_003D13CF:
    if ((((uint32_t)((uint32_t)(Arg5))) & ((uint32_t)(Arg1))) == 0) goto loc_003D107A;
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_rbx)));
    v_stack_p60 = v_stack_m88;
    v_stack_p58 = Arg15;
    v_stack_p50 = 1;
    v_stack_p48 = (uint32_t)((uint32_t)(Arg7));
    v_stack_p40 = (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x1C));
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_mB0;
    v_stack_p28 = v_stack_mA8;
    v_stack_p20 = v_stack_mD0;
    result = SepNormalAccessCheck(Arg1, 0, v_stack_mA0, v_stack_mC0);
    Arg4 = 0;
    goto loc_003D107A;
loc_003D143C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0xC))) | (0x1FFFFFULL));
    goto loc_003D13CF;
loc_003D144B:
    if ((*(uint8_t *)(v_stack_m88 + 0x14)) != 0) goto loc_003D1459;
loc_003D1451:
    goto loc_003D10CF;
loc_003D1459:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) | (*(uint32_t *)(v_stack_m88)));
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4))));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    goto loc_003D10CF;
loc_003D1469:
    *(uint32_t *)(v_stack_m88 + 0xC) = (uint32_t)(local_rbx);
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, 0, v_stack_mA0, Arg4);
    if (condition_is_below) goto loc_003D156E;
loc_003D1482:
    Arg4 = 0;
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)(0x2000000ULL)))) goto loc_003D1579;
    if ((uint32_t)(local_rbx) == 0) goto loc_003D1586;
loc_003D149C:
    goto loc_003D1330;
loc_003D14A6:
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_003D1515;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x8))) | (*(uint32_t *)(v_stack_mC8)));
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(v_stack_mC8 + 0x4)));
    Arg1 = (uint32_t)((Arg1) | (0x10D0000ULL));
loc_003D14BE:
    v_stack_p60 = v_stack_m88;
    v_stack_p58 = Arg15;
    v_stack_p50 = 1;
    v_stack_p48 = (uint32_t)(Arg1);
    v_stack_p40 = (uint32_t)((uint32_t)(Arg7));
    v_stack_p38 = (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x1C));
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = v_stack_mA8;
    result = SepMaximumAccessCheck(0, v_stack_mA0, v_stack_mC0, v_stack_mD0);
    goto loc_003D11AA;
loc_003D1515:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0xC))) | (0x1FFFFFULL));
    goto loc_003D14BE;
loc_003D1524:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8))) | (*(uint32_t *)(v_stack_m88 + 0x4)));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x1C))) & ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r14)) != (*(uint32_t *)(v_stack_p78 + 0x1C))) goto loc_003D15D2;
loc_003D153C:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_stack_m88))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(result)));
    goto loc_003D11DE;
loc_003D1547:
    goto loc_003D1330;
loc_003D1551:
    v_stack_mD0 = *(uint64_t *)(result + 0x18);
    goto loc_003D0F8A;
loc_003D155E:
    local_rsi = (uint32_t)((local_rsi) | (0));
    v_stack_p72 = 1;
    goto loc_003D1370;
loc_003D156E:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_stack_m88))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(result)));
    goto loc_003D1482;
loc_003D1579:
    if ((uint32_t)(local_rsi) == 0) goto loc_003D149C;
loc_003D1586:
    if ((*(uint32_t *)(v_stack_m88)) == ((uint32_t)(v_stack_mD0))) goto loc_003D149C;
    if ((uint32_t)(local_rsi) == 0) goto loc_003D149C;
    goto loc_003D149C;
loc_003D15A8:
    goto loc_003D0FEA;
loc_003D15B0:
    if ((*(uint32_t *)(v_stack_m88 + 0xC)) != ((uint32_t)(v_stack_mD0))) goto loc_003D10CF;
    Arg2 = (uint32_t)((v_stack_mA0) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003D10CF;
    *(uint8_t *)(v_stack_m88 + 0x17) = 1;
    goto loc_003D1451;
loc_003D15D2:
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003D153C;
    if (((v_stack_p28) & ((uint32_t)((uint32_t)(0x2000000ULL)))) != 0) goto loc_003D153C;
loc_003D15FC:
loc_003D1601:
    if ((*(uint8_t *)(v_stack_m88 + 0x14)) == ((uint8_t)(v_stack_mD0))) goto loc_003D11DE;
    local_r14 = (uint32_t)((local_r14) & (*(uint32_t *)(v_stack_m88 + 0x4)));
    goto loc_003D153C;
loc_003D1614:
    if (condition_is_above_or_equal) goto loc_003D15FC;
    goto loc_003D1524;
loc_003D161F:
    local_rdi = (uint32_t)(((uint32_t)(Arg5)) | ((uint32_t)(local_rsi)));
    local_r10 = (uint32_t)((uint32_t)(local_rdi));
    if ((((uint32_t)((uint32_t)(0x2000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5)))))) != 0) { local_r10 = (uint32_t)((uint32_t)(0xFDFFFFFFULL)); }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & ((uint32_t)((uint32_t)(0xFDFFFFFFULL))));
    if ((((uint32_t)((uint32_t)(0x2000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5)))))) == 0) { Arg2 = (uint32_t)(local_rdi); }
    Arg3 = (v_stack_p78) + (28);
    local_rdi = (v_stack_mD8) - (v_stack_mB8);
loc_003D1670:
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)((uint32_t)(0xFDFFFFFFULL))));
    local_rsi = (uint32_t)((local_rsi) | (*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(arg1)))) + 0xC)));
    goto loc_003D111A;
loc_003D1680:
    *(uint8_t *)(local_rdi + 0x15) = (uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    goto loc_003D149C;
loc_003D168D:
    goto loc_003D121A;
loc_003D1697:
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_003D1233;
loc_003D16E4:
    *(uint8_t *)(v_stack_mB8 + (uint32_t)(Arg7) - 0x1 * 4) = 1;
    goto loc_003D124D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*1` | `64` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg8` | `+ 0xC` | `32` | `R` |
| `Arg16` | `+ 0x0` | `32` | `R` |
| `Arg16` | `+ 0x0` | `32` | `W` |
| `Arg16` | `+ 0x4` | `32` | `R` |
| `Arg16` | `+ 0x4` | `32` | `W` |
| `Arg16` | `+ 0x8` | `32` | `R` |
| `Arg16` | `+ 0xC` | `32` | `R` |
| `Arg16` | `+ 0xC` | `32` | `W` |
| `Arg16` | `+ 0x14` | `8` | `R` |
| `Arg16` | `+ 0x15` | `8` | `W` |
| `Arg16` | `+ 0x17` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D0E54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
