# SeQuerySigningPolicyWorker

- RVA: `0x00A13788`–`0x00A13B33` (길이 `939` bytes)
- VA: `0x0000000140A13788`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `287`개 명령, `939/939` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A137E3` → [AppModelPolicy_GetPolicy_Internal](../../text/49/AppModelPolicy_GetPolicy_Internal_function_0049FAEC.md) (function, `0x0049FAEC`)
- `0x00A137F2` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline_function_004F5968.md) (function, `0x004F5968`)
- `0x00A13818` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A138EE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A13910` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline_function_004F5968.md) (function, `0x004F5968`)
- `0x00A1393D` → [SepSetTrustedLaunchSigningLevel](../79/SepSetTrustedLaunchSigningLevel_function_0079C22C.md) (function, `0x0079C22C`)
- `0x00A139C0` → [SepIsNgenImage](../A5/SepIsNgenImage_function_00A557B4.md) (function, `0x00A557B4`)
- `0x00A139DF` → [SeQueryInformationToken](../8B/SeQueryInformationToken_function_008B5090.md) (function, `0x008B5090`)
- `0x00A13A28` → [SepIsLockedDown](../79/SepIsLockedDown_function_0079BC28.md) (function, `0x0079BC28`)
- `0x00A13AC1` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline_function_004F5968.md) (function, `0x004F5968`)
- `0x00A13ADD` → [SepSetTrustedLaunchSigningLevel](../79/SepSetTrustedLaunchSigningLevel_function_0079C22C.md) (function, `0x0079C22C`)

### Direct callers
- [SeQuerySigningPolicy](SeQuerySigningPolicy_function_00A12F44.md) at `0x00A13034`

### Static image references
- `0x00A13805` → RVA `0x00F04F40` (`.data`; read)
- `0x00A138DE` → RVA `0x00F04F30` (`.data`; read)
- `0x00A13A87` → RVA `0x00B4AEE8` (`SeProtectedMapping`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00A137E3` → [AppModelPolicy_GetPolicy_Internal](../../text/49/AppModelPolicy_GetPolicy_Internal_function_0049FAEC.md) (`PAGE` → `.text`)
  - `0x00A137F2` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline_function_004F5968.md) (`PAGE` → `.text`)
  - `0x00A13818` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A138EE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A13910` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline_function_004F5968.md) (`PAGE` → `.text`)
  - `0x00A13AC1` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline_function_004F5968.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A13788  4C 8B DC                        mov r11, rsp
00A1378B  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00A1378F  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00A13793  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
00A13797  55                              push rbp
00A13798  41 54                           push r12
00A1379A  41 55                           push r13
00A1379C  41 56                           push r14
00A1379E  41 57                           push r15
00A137A0  48 8B EC                        mov rbp, rsp
00A137A3  48 83 EC 50                     sub rsp, 0x50
00A137A7  45 33 FF                        xor r15d, r15d
00A137AA  41 0F B6 F9                     movzx edi, r9b
00A137AE  45 8B F0                        mov r14d, r8d
00A137B1  44 88 7D E2                     mov byte ptr [rbp - 0x1e], r15b
00A137B5  4C 8B EA                        mov r13, rdx
00A137B8  44 88 7D E1                     mov byte ptr [rbp - 0x1f], r15b
00A137BC  48 8D 45 F8                     lea rax, [rbp - 8]
00A137C0  44 88 7D E0                     mov byte ptr [rbp - 0x20], r15b
00A137C4  41 8D 57 2E                     lea edx, [r15 + 0x2e]
00A137C8  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
00A137CC  4C 8D 4D F0                     lea r9, [rbp - 0x10]
00A137D0  44 89 7D E8                     mov dword ptr [rbp - 0x18], r15d
00A137D4  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00A137D8  4C 89 7D F8                     mov qword ptr [rbp - 8], r15
00A137DC  4C 8B E1                        mov r12, rcx
00A137DF  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
00A137E3  E8 04 C3 A8 FF                  call 0x14049faec
00A137E8  8B C8                           mov ecx, eax
00A137EA  85 C0                           test eax, eax
00A137EC  0F 88 20 03 00 00               js 0x140a13b12
00A137F2  E8 71 21 AE FF                  call 0x1404f5968
00A137F7  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
00A137FB  85 C0                           test eax, eax
00A137FD  74 26                           je 0x140a13825
00A137FF  0F BA E3 15                     bt ebx, 0x15
00A13803  73 20                           jae 0x140a13825
00A13805  48 8B 05 34 17 4F 00            mov rax, qword ptr [rip + 0x4f1734]
00A1380C  48 85 C0                        test rax, rax
00A1380F  74 10                           je 0x140a13821
00A13811  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00A13815  49 8B CC                        mov rcx, r12
00A13818  E8 B3 72 CA FF                  call 0x1406baad0
00A1381D  85 C0                           test eax, eax
00A1381F  79 04                           jns 0x140a13825
00A13821  44 88 7D E0                     mov byte ptr [rbp - 0x20], r15b
00A13825  8B 4D E8                        mov ecx, dword ptr [rbp - 0x18]
00A13828  BE 01 00 00 00                  mov esi, 1
00A1382D  8D 81 FF FF D1 FF               lea eax, [rcx - 0x2e0001]
00A13833  3B C6                           cmp eax, esi
00A13835  0F 87 72 01 00 00               ja 0x140a139ad
00A1383B  81 F9 02 00 2E 00               cmp ecx, 0x2e0002
00A13841  75 0F                           jne 0x140a13852
00A13843  0F B6 45 F4                     movzx eax, byte ptr [rbp - 0xc]
00A13847  83 E8 04                        sub eax, 4
00A1384A  3B C6                           cmp eax, esi
00A1384C  0F 87 5B 01 00 00               ja 0x140a139ad
00A13852  44 23 F6                        and r14d, esi
00A13855  74 26                           je 0x140a1387d
00A13857  40 84 FF                        test dil, dil
00A1385A  0F 85 50 01 00 00               jne 0x140a139b0
00A13860  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A13864  41 8B CF                        mov ecx, r15d
00A13867  C6 00 04                        mov byte ptr [rax], 4
00A1386A  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A1386E  C6 00 04                        mov byte ptr [rax], 4
00A13871  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00A13875  C6 00 12                        mov byte ptr [rax], 0x12
00A13878  E9 95 02 00 00                  jmp 0x140a13b12
00A1387D  44 0F B6 75 F4                  movzx r14d, byte ptr [rbp - 0xc]
00A13882  41 8B C6                        mov eax, r14d
00A13885  45 85 F6                        test r14d, r14d
00A13888  0F 84 FB 00 00 00               je 0x140a13989
00A1388E  2B C6                           sub eax, esi
00A13890  0F 84 F3 00 00 00               je 0x140a13989
00A13896  2B C6                           sub eax, esi
00A13898  0F 84 D9 00 00 00               je 0x140a13977
00A1389E  2B C6                           sub eax, esi
00A138A0  0F 84 CD 00 00 00               je 0x140a13973
00A138A6  2B C6                           sub eax, esi
00A138A8  74 2B                           je 0x140a138d5
00A138AA  2B C6                           sub eax, esi
00A138AC  74 27                           je 0x140a138d5
00A138AE  3B C6                           cmp eax, esi
00A138B0  0F 85 EF 00 00 00               jne 0x140a139a5
00A138B6  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00A138B9  0F BA E3 15                     bt ebx, 0x15
00A138BD  73 06                           jae 0x140a138c5
00A138BF  3C 02                           cmp al, 2
00A138C1  74 04                           je 0x140a138c7
00A138C3  EB 60                           jmp 0x140a13925
00A138C5  3C 02                           cmp al, 2
00A138C7  0F 95 C1                        setne cl
00A138CA  40 2A CE                        sub cl, sil
00A138CD  80 E1 02                        and cl, 2
00A138D0  E9 BD 00 00 00                  jmp 0x140a13992
00A138D5  40 8A 7D 50                     mov dil, byte ptr [rbp + 0x50]
00A138D9  40 84 FF                        test dil, dil
00A138DC  74 32                           je 0x140a13910
00A138DE  48 8B 05 4B 16 4F 00            mov rax, qword ptr [rip + 0x4f164b]
00A138E5  48 85 C0                        test rax, rax
00A138E8  74 26                           je 0x140a13910
00A138EA  48 8D 4D E1                     lea rcx, [rbp - 0x1f]
00A138EE  E8 DD 71 CA FF                  call 0x1406baad0
00A138F3  85 C0                           test eax, eax
00A138F5  78 19                           js 0x140a13910
00A138F7  44 38 7D E1                     cmp byte ptr [rbp - 0x1f], r15b
00A138FB  74 13                           je 0x140a13910
00A138FD  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A13901  C6 00 03                        mov byte ptr [rax], 3
00A13904  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A13908  C6 00 03                        mov byte ptr [rax], 3
00A1390B  E9 8E 00 00 00                  jmp 0x140a1399e
00A13910  E8 53 20 AE FF                  call 0x1404f5968
00A13915  85 C0                           test eax, eax
00A13917  74 34                           je 0x140a1394d
00A13919  0F BA E3 15                     bt ebx, 0x15
00A1391D  73 25                           jae 0x140a13944
00A1391F  41 83 FE 04                     cmp r14d, 4
00A13923  75 0A                           jne 0x140a1392f
00A13925  B9 22 00 00 C0                  mov ecx, 0xc0000022
00A1392A  E9 E3 01 00 00                  jmp 0x140a13b12
00A1392F  4C 8B 4D 60                     mov r9, qword ptr [rbp + 0x60]
00A13933  40 8A CF                        mov cl, dil
00A13936  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
00A1393A  8A 55 E0                        mov dl, byte ptr [rbp - 0x20]
00A1393D  E8 EA 88 D8 FF                  call 0x14079c22c
00A13942  EB 5A                           jmp 0x140a1399e
00A13944  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A13948  40 88 38                        mov byte ptr [rax], dil
00A1394B  EB 1D                           jmp 0x140a1396a
00A1394D  0F BA E3 15                     bt ebx, 0x15
00A13951  73 0D                           jae 0x140a13960
00A13953  40 84 FF                        test dil, dil
00A13956  75 08                           jne 0x140a13960
00A13958  41 83 FE 04                     cmp r14d, 4
00A1395C  75 05                           jne 0x140a13963
00A1395E  EB C5                           jmp 0x140a13925
00A13960  40 8A F7                        mov sil, dil
00A13963  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A13967  40 88 30                        mov byte ptr [rax], sil
00A1396A  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A1396E  40 88 38                        mov byte ptr [rax], dil
00A13971  EB 2B                           jmp 0x140a1399e
00A13973  B1 06                           mov cl, 6
00A13975  EB 1B                           jmp 0x140a13992
00A13977  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A1397B  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00A1397F  C6 00 08                        mov byte ptr [rax], 8
00A13982  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00A13985  88 01                           mov byte ptr [rcx], al
00A13987  EB 15                           jmp 0x140a1399e
00A13989  0F BA E3 15                     bt ebx, 0x15
00A1398D  72 96                           jb 0x140a13925
00A1398F  8A 4D 50                        mov cl, byte ptr [rbp + 0x50]
00A13992  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A13996  88 08                           mov byte ptr [rax], cl
00A13998  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A1399C  88 08                           mov byte ptr [rax], cl
00A1399E  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00A139A2  44 88 38                        mov byte ptr [rax], r15b
00A139A5  41 8B CF                        mov ecx, r15d
00A139A8  E9 65 01 00 00                  jmp 0x140a13b12
00A139AD  44 23 F6                        and r14d, esi
00A139B0  4C 8B 7D 58                     mov r15, qword ptr [rbp + 0x58]
00A139B4  4D 85 ED                        test r13, r13
00A139B7  0F 84 B4 00 00 00               je 0x140a13a71
00A139BD  49 8B CD                        mov rcx, r13
00A139C0  E8 EF 1D 04 00                  call 0x140a557b4
00A139C5  45 33 ED                        xor r13d, r13d
00A139C8  84 C0                           test al, al
00A139CA  0F 84 A1 00 00 00               je 0x140a13a71
00A139D0  4C 8D 45 E4                     lea r8, [rbp - 0x1c]
00A139D4  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00A139D8  41 8D 55 1D                     lea edx, [r13 + 0x1d]
00A139DC  49 8B CC                        mov rcx, r12
00A139DF  E8 AC 16 EA FF                  call 0x1408b5090
00A139E4  8B C8                           mov ecx, eax
00A139E6  85 C0                           test eax, eax
00A139E8  0F 88 24 01 00 00               js 0x140a13b12
00A139EE  41 C6 07 0B                     mov byte ptr [r15], 0xb
00A139F2  45 85 F6                        test r14d, r14d
00A139F5  74 24                           je 0x140a13a1b
00A139F7  40 84 FF                        test dil, dil
00A139FA  75 7A                           jne 0x140a13a76
00A139FC  8B 45 E4                        mov eax, dword ptr [rbp - 0x1c]
00A139FF  F7 D8                           neg eax
00A13A01  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A13A05  1A C9                           sbb cl, cl
00A13A07  80 E1 FE                        and cl, 0xfe
00A13A0A  80 C1 08                        add cl, 8
00A13A0D  88 08                           mov byte ptr [rax], cl
00A13A0F  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00A13A13  C6 00 21                        mov byte ptr [rax], 0x21
00A13A16  E9 F4 00 00 00                  jmp 0x140a13b0f
00A13A1B  8A 4D 50                        mov cl, byte ptr [rbp + 0x50]
00A13A1E  44 39 6D E4                     cmp dword ptr [rbp - 0x1c], r13d
00A13A22  74 32                           je 0x140a13a56
00A13A24  48 8D 55 E2                     lea rdx, [rbp - 0x1e]
00A13A28  E8 FB 81 D8 FF                  call 0x14079bc28
00A13A2D  8B C8                           mov ecx, eax
00A13A2F  85 C0                           test eax, eax
00A13A31  0F 88 DB 00 00 00               js 0x140a13b12
00A13A37  44 38 6D E2                     cmp byte ptr [rbp - 0x1e], r13b
00A13A3B  74 07                           je 0x140a13a44
00A13A3D  B1 06                           mov cl, 6
00A13A3F  E9 BE 00 00 00                  jmp 0x140a13b02
00A13A44  80 7D 50 02                     cmp byte ptr [rbp + 0x50], 2
00A13A48  0F 95 C1                        setne cl
00A13A4B  40 2A CE                        sub cl, sil
00A13A4E  80 E1 02                        and cl, 2
00A13A51  E9 AC 00 00 00                  jmp 0x140a13b02
00A13A56  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A13A5A  80 F9 02                        cmp cl, 2
00A13A5D  88 08                           mov byte ptr [rax], cl
00A13A5F  1A C9                           sbb cl, cl
00A13A61  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00A13A65  F6 D1                           not cl
00A13A67  80 E1 21                        and cl, 0x21
00A13A6A  88 08                           mov byte ptr [rax], cl
00A13A6C  E9 9E 00 00 00                  jmp 0x140a13b0f
00A13A71  45 85 F6                        test r14d, r14d
00A13A74  74 4B                           je 0x140a13ac1
00A13A76  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00A13A7A  40 84 FF                        test dil, dil
00A13A7D  8B C7                           mov eax, edi
00A13A7F  BA 12 00 00 00                  mov edx, 0x12
00A13A84  0F 44 C2                        cmove eax, edx
00A13A87  48 8D 15 5A 74 13 00            lea rdx, [rip + 0x13745a]
00A13A8E  0F B6 C0                        movzx eax, al
00A13A91  88 01                           mov byte ptr [rcx], al
00A13A93  48 C1 E8 04                     shr rax, 4
00A13A97  8A 04 42                        mov al, byte ptr [rdx + rax*2]
00A13A9A  41 88 07                        mov byte ptr [r15], al
00A13A9D  0F B6 01                        movzx eax, byte ptr [rcx]
00A13AA0  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00A13AA4  48 C1 E8 04                     shr rax, 4
00A13AA8  8A 44 42 01                     mov al, byte ptr [rdx + rax*2 + 1]
00A13AAC  88 01                           mov byte ptr [rcx], al
00A13AAE  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00A13AB1  41 3A 07                        cmp al, byte ptr [r15]
00A13AB4  76 03                           jbe 0x140a13ab9
00A13AB6  41 88 07                        mov byte ptr [r15], al
00A13AB9  3A 01                           cmp al, byte ptr [rcx]
00A13ABB  76 52                           jbe 0x140a13b0f
00A13ABD  88 01                           mov byte ptr [rcx], al
00A13ABF  EB 4E                           jmp 0x140a13b0f
00A13AC1  E8 A2 1E AE FF                  call 0x1404f5968
00A13AC6  8A 4D 50                        mov cl, byte ptr [rbp + 0x50]
00A13AC9  85 C0                           test eax, eax
00A13ACB  74 17                           je 0x140a13ae4
00A13ACD  0F BA E3 15                     bt ebx, 0x15
00A13AD1  73 2A                           jae 0x140a13afd
00A13AD3  4C 8B 4D 60                     mov r9, qword ptr [rbp + 0x60]
00A13AD7  4D 8B C7                        mov r8, r15
00A13ADA  8A 55 E0                        mov dl, byte ptr [rbp - 0x20]
00A13ADD  E8 4A 87 D8 FF                  call 0x14079c22c
00A13AE2  EB 24                           jmp 0x140a13b08
00A13AE4  0F BA E3 15                     bt ebx, 0x15
00A13AE8  73 13                           jae 0x140a13afd
00A13AEA  84 C9                           test cl, cl
00A13AEC  75 0F                           jne 0x140a13afd
00A13AEE  49 8B C7                        mov rax, r15
00A13AF1  40 88 30                        mov byte ptr [rax], sil
00A13AF4  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A13AF8  44 88 28                        mov byte ptr [rax], r13b
00A13AFB  EB 0B                           jmp 0x140a13b08
00A13AFD  49 8B C7                        mov rax, r15
00A13B00  88 08                           mov byte ptr [rax], cl
00A13B02  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A13B06  88 08                           mov byte ptr [rax], cl
00A13B08  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00A13B0C  44 88 28                        mov byte ptr [rax], r13b
00A13B0F  41 8B CD                        mov ecx, r13d
00A13B12  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00A13B17  8B C1                           mov eax, ecx
00A13B19  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00A13B1D  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00A13B21  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00A13B25  49 8B E3                        mov rsp, r11
00A13B28  41 5F                           pop r15
00A13B2A  41 5E                           pop r14
00A13B2C  41 5D                           pop r13
00A13B2E  41 5C                           pop r12
00A13B30  5D                              pop rbp
00A13B31  C3                              ret
00A13B32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeQuerySigningPolicyWorker(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, unsigned __int8 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int8 v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m44;
    unsigned __int8 v_stack_m46;
    unsigned __int8 v_stack_m47;
    unsigned __int8 v_stack_m48;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (80);
    v_r15 = 0;
    v_stack_m46 = 0;
    v_stack_m47 = 0;
    v_stack_m48 = 0;
    v_stack_m38 = 0;
    v_stack_m40 = 0;
    v_stack_m30 = 0;
    *(unsigned __int64 *)(v_rsp - 88) = v_stack_m30;
    result = AppModelPolicy_GetPolicy_Internal(a1, v_r15 + 46, v_stack_m40, v_stack_m38);
    if (sign_flag) goto loc_00A13B12;
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)(result)), v_r15 + 46, v_stack_m40, v_stack_m38);
    if ((unsigned int)(result) == 0) goto loc_00A13825;
    if (condition_is_above_or_equal) goto loc_00A13825;
    if (*(unsigned __int64 *)(v_rip + 5183284) == 0) goto loc_00A13821;
    result = guard_dispatch_icall(a1, v_stack_m48, v_stack_m40, v_stack_m38);
    if (sign_flag) {
        v_stack_m48 = 0;
    }
    if (((unsigned int)((unsigned int)(v_stack_m40) - 3014657)) > 1) goto loc_00A139AD;
    if (((unsigned int)((unsigned int)(v_stack_m40))) != 0x2E0002ULL) goto loc_00A13852;
    result = (unsigned int)((v_stack_m34) - (4));
    if (((unsigned int)(result)) > 1) goto loc_00A139AD;
loc_00A13852:
    v_r14 = (unsigned int)(((unsigned int)(a3)) & (1));
    if (condition_is_equal) goto loc_00A1387D;
    if (a4 != 0) goto loc_00A139B0;
    *(unsigned __int8 *)(a6) = 4;
    *(unsigned __int8 *)(a7) = 4;
    *(unsigned __int8 *)(a8) = 18;
    goto loc_00A13B12;
loc_00A1387D:
    if ((unsigned int)(v_stack_m34) == 0) goto loc_00A13989;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m34))) - (1));
    if (condition_is_equal) goto loc_00A13989;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A13977;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A13973;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A138D5;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A138D5;
    if (((unsigned int)(result)) != 1) goto loc_00A139A5;
    if (((unsigned int)(result)) >= 1) goto loc_00A138C5;
    if (a5 == 2) goto loc_00A138C7;
    goto loc_00A13925;
loc_00A138C5:
loc_00A138C7:
    a1 = (a5 != 2) ? 1 : 0;
    a1 = (unsigned __int8)((a1) - (1));
    a1 = (unsigned __int8)((a1) & (2));
    goto loc_00A13992;
loc_00A138D5:
    if (a5 == 0) goto loc_00A13910;
    if (*(unsigned __int64 *)(v_rip + 5183051) == 0) goto loc_00A13910;
    result = guard_dispatch_icall(v_stack_m47, v_stack_m48, v_stack_m40, v_stack_m38);
    if (sign_flag) goto loc_00A13910;
    if (v_stack_m47 == 0) goto loc_00A13910;
    *(unsigned __int8 *)(a6) = 3;
    *(unsigned __int8 *)(a7) = 3;
    goto loc_00A1399E;
loc_00A13910:
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline(v_stack_m47, v_stack_m48, v_stack_m40, v_stack_m38);
    if ((unsigned int)(result) == 0) goto loc_00A1394D;
    if (condition_is_above_or_equal) goto loc_00A13944;
    if (((unsigned int)(v_stack_m34)) != 4) goto loc_00A1392F;
loc_00A13925:
    goto loc_00A13B12;
loc_00A1392F:
    result = SepSetTrustedLaunchSigningLevel(a5, v_stack_m48, a6, a7);
    goto loc_00A1399E;
loc_00A13944:
    *(unsigned __int8 *)(a6) = a5;
    goto loc_00A1396A;
loc_00A1394D:
    if (((unsigned int)(v_stack_m34)) >= 4) goto loc_00A13960;
    if (a5 != 0) goto loc_00A13960;
    if (((unsigned int)(v_stack_m34)) != 4) goto loc_00A13963;
    goto loc_00A13925;
loc_00A13960:
loc_00A13963:
    *(unsigned __int8 *)(a6) = a5;
loc_00A1396A:
    *(unsigned __int8 *)(a7) = a5;
    goto loc_00A1399E;
loc_00A13973:
    goto loc_00A13992;
loc_00A13977:
    *(unsigned __int8 *)(a6) = 8;
    *(unsigned __int8 *)(a7) = a5;
    goto loc_00A1399E;
loc_00A13989:
    if (((unsigned int)(v_stack_m34)) < 4) goto loc_00A13925;
loc_00A13992:
    *(unsigned __int8 *)(a6) = a5;
    *(unsigned __int8 *)(a7) = a5;
loc_00A1399E:
    *(unsigned __int8 *)(a8) = 0;
loc_00A139A5:
    goto loc_00A13B12;
loc_00A139AD:
    v_r14 = (unsigned int)((v_stack_m34) & (a5));
loc_00A139B0:
    if (a2 == 0) goto loc_00A13A71;
    result = SepIsNgenImage(a2, v_stack_m48, a6, a7);
    v_r13 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A13A71;
    v_stack_m44 = 0;
    result = SeQueryInformationToken(a1, v_r13 + 29, v_stack_m44, a7);
    if (sign_flag) goto loc_00A13B12;
    *(unsigned __int8 *)(a6) = 11;
    if ((unsigned int)(v_r14) == 0) goto loc_00A13A1B;
    if (a5 != 0) goto loc_00A13A76;
    result = (unsigned int)(-((unsigned int)(v_stack_m44)));
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)(result))) & (254));
    a1 = (unsigned __int8)((a1) + (8));
    *(unsigned __int8 *)(a7) = (unsigned __int8)(a1);
    *(unsigned __int8 *)(a8) = 33;
    goto loc_00A13B0F;
loc_00A13A1B:
    if (v_stack_m44 == 0) goto loc_00A13A56;
    result = SepIsLockedDown(a5, v_stack_m46, v_stack_m44, a7);
    if (sign_flag) goto loc_00A13B12;
    if (v_stack_m46 == 0) goto loc_00A13A44;
    goto loc_00A13B02;
loc_00A13A44:
    a1 = (a5 != 2) ? 1 : 0;
    a1 = (unsigned __int8)((a1) - (a5));
    a1 = (unsigned __int8)((a1) & (2));
    goto loc_00A13B02;
loc_00A13A56:
    *(unsigned __int8 *)(a7) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)(~(a1));
    a1 = (unsigned __int8)((a1) & (33));
    *(unsigned __int8 *)(a8) = (unsigned __int8)(a1);
    goto loc_00A13B0F;
loc_00A13A71:
    if ((unsigned int)(v_r14) == 0) goto loc_00A13AC1;
loc_00A13A76:
    result = (unsigned int)(a5);
    if (a5 == 0) { result = 18; }
    *(unsigned __int8 *)(a8) = (unsigned __int8)((unsigned __int8)(result));
    result = ((unsigned __int8)(result)) >> (4);
    *(unsigned __int8 *)(a6) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 1274970 + result * 2));
    result = (*(unsigned __int8 *)(a8)) >> (4);
    *(unsigned __int8 *)(a7) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 1274970 + result * 2 + 1));
    if (a5 >= = (*(unsigned __int8 *)(a6))) {
        *(unsigned __int8 *)(a6) = a5;
    }
    if (a5 <= (*(unsigned __int8 *)(a7))) goto loc_00A13B0F;
    *(unsigned __int8 *)(a7) = a5;
    goto loc_00A13B0F;
loc_00A13AC1:
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline(a7, v_rip + 1274970, v_stack_m44, a7);
    if ((unsigned int)(result) == 0) goto loc_00A13AE4;
    if (condition_is_above_or_equal) goto loc_00A13AFD;
    result = SepSetTrustedLaunchSigningLevel(a5, v_stack_m48, a6, a7);
    goto loc_00A13B08;
loc_00A13AE4:
    if (condition_is_above_or_equal) goto loc_00A13AFD;
    if (a5 != 0) goto loc_00A13AFD;
    *(unsigned __int8 *)(a6) = a5;
    *(unsigned __int8 *)(a7) = 0;
    goto loc_00A13B08;
loc_00A13AFD:
    *(unsigned __int8 *)(a6) = a5;
loc_00A13B02:
    *(unsigned __int8 *)(a7) = a5;
loc_00A13B08:
    *(unsigned __int8 *)(a8) = 0;
loc_00A13B0F:
loc_00A13B12:
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t SeQuerySigningPolicyWorker(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, uint8_t Arg5, void *Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint8_t v_stack_m34;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m44;
    uint8_t v_stack_m46;
    uint8_t v_stack_m47;
    uint8_t v_stack_m48;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (80);
    local_r15 = 0;
    v_stack_m46 = 0;
    v_stack_m47 = 0;
    v_stack_m48 = 0;
    v_stack_m38 = 0;
    v_stack_m40 = 0;
    v_stack_m30 = 0;
    *(uint64_t *)(local_rsp - 0x58) = v_stack_m30;
    result = AppModelPolicy_GetPolicy_Internal(Arg1, local_r15 + 46, v_stack_m40, v_stack_m38);
    if (sign_flag) goto loc_00A13B12;
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)(result)), local_r15 + 46, v_stack_m40, v_stack_m38);
    if ((uint32_t)(result) == 0) goto loc_00A13825;
    if (condition_is_above_or_equal) goto loc_00A13825;
    if (*(uint64_t *)(v_rip + 0x4F1734) == 0) goto loc_00A13821;
    result = guard_dispatch_icall(Arg1, v_stack_m48, v_stack_m40, v_stack_m38);
    if (sign_flag) {
        v_stack_m48 = 0;
    }
    if (((uint32_t)((uint32_t)(v_stack_m40) - 3014657)) > 1) goto loc_00A139AD;
    if (((uint32_t)((uint32_t)(v_stack_m40))) != 0x2E0002ULL) goto loc_00A13852;
    result = (uint32_t)((v_stack_m34) - (4));
    if (((uint32_t)(result)) > 1) goto loc_00A139AD;
loc_00A13852:
    local_r14 = (uint32_t)(((uint32_t)(Arg3)) & (1));
    if (condition_is_equal) goto loc_00A1387D;
    if (Arg4 != 0) goto loc_00A139B0;
    *(uint8_t *)(arg6) = 4;
    *(uint8_t *)(arg7) = 4;
    *(uint8_t *)(arg8) = 18;
    goto loc_00A13B12;
loc_00A1387D:
    if ((uint32_t)(v_stack_m34) == 0) goto loc_00A13989;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m34))) - (1));
    if (condition_is_equal) goto loc_00A13989;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A13977;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A13973;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A138D5;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A138D5;
    if (((uint32_t)(result)) != 1) goto loc_00A139A5;
    if (((uint32_t)(result)) >= 1) goto loc_00A138C5;
    if (Arg5 == 2) goto loc_00A138C7;
    goto loc_00A13925;
loc_00A138C5:
loc_00A138C7:
    Arg1 = (Arg5 != 2) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) - (1));
    Arg1 = (uint8_t)((Arg1) & (2));
    goto loc_00A13992;
loc_00A138D5:
    if (Arg5 == 0) goto loc_00A13910;
    if (*(uint64_t *)(v_rip + 0x4F164B) == 0) goto loc_00A13910;
    result = guard_dispatch_icall(v_stack_m47, v_stack_m48, v_stack_m40, v_stack_m38);
    if (sign_flag) goto loc_00A13910;
    if (v_stack_m47 == 0) goto loc_00A13910;
    *(uint8_t *)(arg6) = 3;
    *(uint8_t *)(arg7) = 3;
    goto loc_00A1399E;
loc_00A13910:
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline(v_stack_m47, v_stack_m48, v_stack_m40, v_stack_m38);
    if ((uint32_t)(result) == 0) goto loc_00A1394D;
    if (condition_is_above_or_equal) goto loc_00A13944;
    if (((uint32_t)(v_stack_m34)) != 4) goto loc_00A1392F;
loc_00A13925:
    goto loc_00A13B12;
loc_00A1392F:
    result = SepSetTrustedLaunchSigningLevel(Arg5, v_stack_m48, Arg6, Arg7);
    goto loc_00A1399E;
loc_00A13944:
    *(uint8_t *)(arg6) = Arg5;
    goto loc_00A1396A;
loc_00A1394D:
    if (((uint32_t)(v_stack_m34)) >= 4) goto loc_00A13960;
    if (Arg5 != 0) goto loc_00A13960;
    if (((uint32_t)(v_stack_m34)) != 4) goto loc_00A13963;
    goto loc_00A13925;
loc_00A13960:
loc_00A13963:
    *(uint8_t *)(arg6) = Arg5;
loc_00A1396A:
    *(uint8_t *)(arg7) = Arg5;
    goto loc_00A1399E;
loc_00A13973:
    goto loc_00A13992;
loc_00A13977:
    *(uint8_t *)(arg6) = 8;
    *(uint8_t *)(arg7) = Arg5;
    goto loc_00A1399E;
loc_00A13989:
    if (((uint32_t)(v_stack_m34)) < 4) goto loc_00A13925;
loc_00A13992:
    *(uint8_t *)(arg6) = Arg5;
    *(uint8_t *)(arg7) = Arg5;
loc_00A1399E:
    *(uint8_t *)(arg8) = 0;
loc_00A139A5:
    goto loc_00A13B12;
loc_00A139AD:
    local_r14 = (uint32_t)((v_stack_m34) & (Arg5));
loc_00A139B0:
    if (Arg2 == 0) goto loc_00A13A71;
    result = SepIsNgenImage(Arg2, v_stack_m48, Arg6, Arg7);
    local_r13 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A13A71;
    v_stack_m44 = 0;
    result = SeQueryInformationToken(Arg1, local_r13 + 29, v_stack_m44, Arg7);
    if (sign_flag) goto loc_00A13B12;
    *(uint8_t *)(arg6) = 11;
    if ((uint32_t)(local_r14) == 0) goto loc_00A13A1B;
    if (Arg5 != 0) goto loc_00A13A76;
    result = (uint32_t)(-((uint32_t)(v_stack_m44)));
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)(result))) & (254));
    Arg1 = (uint8_t)((Arg1) + (8));
    *(uint8_t *)(arg7) = (uint8_t)(Arg1);
    *(uint8_t *)(arg8) = 33;
    goto loc_00A13B0F;
loc_00A13A1B:
    if (v_stack_m44 == 0) goto loc_00A13A56;
    result = SepIsLockedDown(Arg5, v_stack_m46, v_stack_m44, Arg7);
    if (sign_flag) goto loc_00A13B12;
    if (v_stack_m46 == 0) goto loc_00A13A44;
    goto loc_00A13B02;
loc_00A13A44:
    Arg1 = (Arg5 != 2) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) - (Arg5));
    Arg1 = (uint8_t)((Arg1) & (2));
    goto loc_00A13B02;
loc_00A13A56:
    *(uint8_t *)(arg7) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)(~(Arg1));
    Arg1 = (uint8_t)((Arg1) & (33));
    *(uint8_t *)(arg8) = (uint8_t)(Arg1);
    goto loc_00A13B0F;
loc_00A13A71:
    if ((uint32_t)(local_r14) == 0) goto loc_00A13AC1;
loc_00A13A76:
    result = (uint32_t)(Arg5);
    if (Arg5 == 0) { result = 18; }
    *(uint8_t *)(arg8) = (uint8_t)((uint8_t)(result));
    result = ((uint8_t)(result)) >> (4);
    *(uint8_t *)(arg6) = (uint8_t)(*(uint8_t *)(v_rip + 0x13745A + result * 2));
    result = (*(uint8_t *)(arg8)) >> (4);
    *(uint8_t *)(arg7) = (uint8_t)(*(uint8_t *)(v_rip + 0x13745A + result * 2 + 0x1));
    if (Arg5 >= = (*(uint8_t *)(arg6))) {
        *(uint8_t *)(arg6) = Arg5;
    }
    if (Arg5 <= (*(uint8_t *)(arg7))) goto loc_00A13B0F;
    *(uint8_t *)(arg7) = Arg5;
    goto loc_00A13B0F;
loc_00A13AC1:
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline(Arg7, v_rip + 1274970, v_stack_m44, Arg7);
    if ((uint32_t)(result) == 0) goto loc_00A13AE4;
    if (condition_is_above_or_equal) goto loc_00A13AFD;
    result = SepSetTrustedLaunchSigningLevel(Arg5, v_stack_m48, Arg6, Arg7);
    goto loc_00A13B08;
loc_00A13AE4:
    if (condition_is_above_or_equal) goto loc_00A13AFD;
    if (Arg5 != 0) goto loc_00A13AFD;
    *(uint8_t *)(arg6) = Arg5;
    *(uint8_t *)(arg7) = 0;
    goto loc_00A13B08;
loc_00A13AFD:
    *(uint8_t *)(arg6) = Arg5;
loc_00A13B02:
    *(uint8_t *)(arg7) = Arg5;
loc_00A13B08:
    *(uint8_t *)(arg8) = 0;
loc_00A13B0F:
loc_00A13B12:
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `8` | `R` |
| `Arg6` | `+ 0x0` | `8` | `W` |
| `Arg7` | `+ 0x0` | `8` | `R` |
| `Arg7` | `+ 0x0` | `8` | `W` |
| `Arg8` | `+ 0x0` | `8` | `R` |
| `Arg8` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A13788&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
