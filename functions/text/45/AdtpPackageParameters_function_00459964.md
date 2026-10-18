# AdtpPackageParameters

- RVA: `0x00459964`–`0x0045A363` (길이 `2,559` bytes)
- VA: `0x0000000140459964`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A8F18`
- 디코드: `614`개 명령, `2,559/2,559` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00459A73` → [AdtpBuildMessageString](../../page/A1/AdtpBuildMessageString_function_00A19214.md) (function, `0x00A19214`)
- `0x00459B0C` → [RtlValidSid](../../page/92/RtlValidSid_function_00929710.md) (function, `0x00929710`)
- `0x00459B80` → [AdtpBuildSockAddrString](../../page/A2/AdtpBuildSockAddrString_function_00A2B53C.md) (function, `0x00A2B53C`)
- `0x00459C79` → [AdtpIsCorrectlyFormedUnicodeString](AdtpIsCorrectlyFormedUnicodeString_function_0045A36C.md) (function, `0x0045A36C`)
- `0x00459CA0` → [AdtpEtwBuildString](../../page/A4/AdtpEtwBuildString_function_00A4232C.md) (function, `0x00A4232C`)
- `0x00459D5B` → [AdtpBuildLogonIdStrings](../../page/A5/AdtpBuildLogonIdStrings_function_00A56DC8.md) (function, `0x00A56DC8`)
- `0x00459E76` → [AdtpIsCorrectlyFormedUnicodeString](AdtpIsCorrectlyFormedUnicodeString_function_0045A36C.md) (function, `0x0045A36C`)
- `0x00459E83` → [AdtpSubstituteDriveLetter](../../page/A4/AdtpSubstituteDriveLetter_function_00A4A7D0.md) (function, `0x00A4A7D0`)
- `0x00459F17` → [AdtpBuildSecurityDescriptorChangeString](../../page/A6/AdtpBuildSecurityDescriptorChangeString_function_00A662F0.md) (function, `0x00A662F0`)
- `0x00459F9E` → [AdtpBuildPrivilegeAuditString](../../page/A6/AdtpBuildPrivilegeAuditString_function_00A62AE8.md) (function, `0x00A62AE8`)
- `0x00459FED` → [AdtpEtwBuildDashString](../../page/AA/AdtpEtwBuildDashString_function_00AAB7B0.md) (function, `0x00AAB7B0`)
- `0x0045A030` → [AdtpEtwBuildDashString](../../page/AA/AdtpEtwBuildDashString_function_00AAB7B0.md) (function, `0x00AAB7B0`)
- `0x0045A05A` → [AdtpBuildMultiSzStringListString](AdtpBuildMultiSzStringListString_function_0045A388.md) (function, `0x0045A388`)
- `0x0045A114` → [AdtpBuildAccessesString](../../page/A8/AdtpBuildAccessesString_function_00A8898C.md) (function, `0x00A8898C`)
- `0x0045A148` → [AdtpBuildUlongString](../../page/AB/AdtpBuildUlongString_function_00AB3BA4.md) (function, `0x00AB3BA4`)
- `0x0045A1C2` → [AdtpBuildObjectTypeStrings](../../page/AD/AdtpBuildObjectTypeStrings_function_00AD0B38.md) (function, `0x00AD0B38`)
- `0x0045A228` → [AdtpBuildStringListString](../../page/AD/AdtpBuildStringListString_function_00AD5130.md) (function, `0x00AD5130`)
- `0x0045A27C` → [AdtpBuildSecurityDescriptorUnicodeString](../../page/A6/AdtpBuildSecurityDescriptorUnicodeString_function_00A663C0.md) (function, `0x00A663C0`)
- `0x0045A312` → [AdtpBuildSidListString](../../page/82/AdtpBuildSidListString_function_00822440.md) (function, `0x00822440`)
- `0x0045A333` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [AdtpWriteToEtwEx](AdtpWriteToEtwEx_function_004595EC.md) at `0x004596CD`
- [AdtpWriteToEtw](../../page/AF/AdtpWriteToEtw_function_00AF98B0.md) at `0x00AF9995`

### Static image references
- `0x004599BF` → RVA `0x00FD9EC0` (`PAGEDATA`; read)
- `0x00459FBA` → RVA `0x00FD9EC1` (`PAGEDATA`; read)
- `0x00459FFF` → RVA `0x00FDA0E8` (`PAGEDATA`; read)
- `0x0045A085` → RVA `0x00FDA4F8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00459A73` → [AdtpBuildMessageString](../../page/A1/AdtpBuildMessageString_function_00A19214.md) (`.text` → `PAGE`)
  - `0x00459B0C` → [RtlValidSid](../../page/92/RtlValidSid_function_00929710.md) (`.text` → `PAGE`)
  - `0x00459B80` → [AdtpBuildSockAddrString](../../page/A2/AdtpBuildSockAddrString_function_00A2B53C.md) (`.text` → `PAGE`)
  - `0x00459CA0` → [AdtpEtwBuildString](../../page/A4/AdtpEtwBuildString_function_00A4232C.md) (`.text` → `PAGE`)
  - `0x00459D5B` → [AdtpBuildLogonIdStrings](../../page/A5/AdtpBuildLogonIdStrings_function_00A56DC8.md) (`.text` → `PAGE`)
  - `0x00459E83` → [AdtpSubstituteDriveLetter](../../page/A4/AdtpSubstituteDriveLetter_function_00A4A7D0.md) (`.text` → `PAGE`)
  - `0x00459F17` → [AdtpBuildSecurityDescriptorChangeString](../../page/A6/AdtpBuildSecurityDescriptorChangeString_function_00A662F0.md) (`.text` → `PAGE`)
  - `0x00459F9E` → [AdtpBuildPrivilegeAuditString](../../page/A6/AdtpBuildPrivilegeAuditString_function_00A62AE8.md) (`.text` → `PAGE`)
  - `0x00459FED` → [AdtpEtwBuildDashString](../../page/AA/AdtpEtwBuildDashString_function_00AAB7B0.md) (`.text` → `PAGE`)
  - `0x0045A030` → [AdtpEtwBuildDashString](../../page/AA/AdtpEtwBuildDashString_function_00AAB7B0.md) (`.text` → `PAGE`)
  - `0x0045A114` → [AdtpBuildAccessesString](../../page/A8/AdtpBuildAccessesString_function_00A8898C.md) (`.text` → `PAGE`)
  - `0x0045A148` → [AdtpBuildUlongString](../../page/AB/AdtpBuildUlongString_function_00AB3BA4.md) (`.text` → `PAGE`)
  - `0x0045A1C2` → [AdtpBuildObjectTypeStrings](../../page/AD/AdtpBuildObjectTypeStrings_function_00AD0B38.md) (`.text` → `PAGE`)
  - `0x0045A228` → [AdtpBuildStringListString](../../page/AD/AdtpBuildStringListString_function_00AD5130.md) (`.text` → `PAGE`)
  - `0x0045A27C` → [AdtpBuildSecurityDescriptorUnicodeString](../../page/A6/AdtpBuildSecurityDescriptorUnicodeString_function_00A663C0.md) (`.text` → `PAGE`)
  - `0x0045A312` → [AdtpBuildSidListString](../../page/82/AdtpBuildSidListString_function_00822440.md) (`.text` → `PAGE`)
  - `0x0045A333` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x00459A33` → [sub_006F1C3C + 0x1E](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)
  - `0x00459CE6` → [sub_006F1C3C + 0x153](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)
  - `0x0045A2A8` → [sub_006F1C3C + 0xF7](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)
  - `0x0045A2C7` → [sub_006F1C3C](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)
  - `0x0045A31F` → [sub_006F1C3C + 0xEC](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)
  - `0x0045A328` → [sub_006F1C3C + 0xEC](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)
  - `0x0045A339` → [sub_006F1C3C + 0xEC](../6F/Unknown_function_006F1C3C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00459964  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00459969  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0045996E  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00459973  55                              push rbp
00459974  56                              push rsi
00459975  57                              push rdi
00459976  41 54                           push r12
00459978  41 55                           push r13
0045997A  41 56                           push r14
0045997C  41 57                           push r15
0045997E  48 8B EC                        mov rbp, rsp
00459981  48 81 EC 80 00 00 00            sub rsp, 0x80
00459988  49 8B F9                        mov rdi, r9
0045998B  45 33 C9                        xor r9d, r9d
0045998E  66 44 89 4D E2                  mov word ptr [rbp - 0x1e], r9w
00459993  45 0F B7 F1                     movzx r14d, r9w
00459997  44 89 4D E4                     mov dword ptr [rbp - 0x1c], r9d
0045999B  45 0F B7 D9                     movzx r11d, r9w
0045999F  41 8B F1                        mov esi, r9d
004599A2  48 85 C9                        test rcx, rcx
004599A5  0F 84 E5 04 00 00               je 0x140459e90
004599AB  48 85 D2                        test rdx, rdx
004599AE  0F 85 02 03 00 00               jne 0x140459cb6
004599B4  8B 41 08                        mov eax, dword ptr [rcx + 8]
004599B7  4C 8D 79 18                     lea r15, [rcx + 0x18]
004599BB  4C 8B 6D 68                     mov r13, qword ptr [rbp + 0x68]
004599BF  4C 8D 15 FA 04 B8 00            lea r10, [rip + 0xb804fa]
004599C6  BA 02 00 00 00                  mov edx, 2
004599CB  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
004599CF  89 45 EC                        mov dword ptr [rbp - 0x14], eax
004599D2  8B CA                           mov ecx, edx
004599D4  44 8D 42 FF                     lea r8d, [rdx - 1]
004599D8  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
004599DB  3B C8                           cmp ecx, eax
004599DD  0F 83 D8 02 00 00               jae 0x140459cbb
004599E3  66 41 83 FB 0E                  cmp r11w, 0xe
004599E8  0F 83 C8 02 00 00               jae 0x140459cb6
004599EE  66 41 83 FE 2A                  cmp r14w, 0x2a
004599F3  0F 83 BD 02 00 00               jae 0x140459cb6
004599F9  44 8B E1                        mov r12d, ecx
004599FC  49 C1 E4 05                     shl r12, 5
00459A00  43 8B 1C 3C                     mov ebx, dword ptr [r12 + r15]
00459A04  83 FB 10                        cmp ebx, 0x10
00459A07  0F 8E 9E 00 00 00               jle 0x140459aab
00459A0D  83 FB 1B                        cmp ebx, 0x1b
00459A10  0F 84 3D 02 00 00               je 0x140459c53
00459A16  0F 8F C5 02 00 00               jg 0x140459ce1
00459A1C  8B CB                           mov ecx, ebx
00459A1E  83 E9 11                        sub ecx, 0x11
00459A21  0F 84 C3 08 00 00               je 0x14045a2ea
00459A27  83 E9 01                        sub ecx, 1
00459A2A  0F 84 9C 08 00 00               je 0x14045a2cc
00459A30  83 E9 01                        sub ecx, 1
00459A33  0F 84 21 82 29 00               je 0x1406f1c5a
00459A39  83 E9 01                        sub ecx, 1
00459A3C  0F 84 80 08 00 00               je 0x14045a2c2
00459A42  83 E9 01                        sub ecx, 1
00459A45  0F 85 01 01 00 00               jne 0x140459b4c
00459A4B  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00459A4F  4C 8B CF                        mov r9, rdi
00459A52  43 8B 4C 3C 08                  mov ecx, dword ptr [r12 + r15 + 8]
00459A57  45 0F B7 C6                     movzx r8d, r14w
00459A5B  49 03 C0                        add rax, r8
00459A5E  49 C1 E0 04                     shl r8, 4
00459A62  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00459A67  4D 03 C5                        add r8, r13
00459A6A  48 8D 45 E4                     lea rax, [rbp - 0x1c]
00459A6E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00459A73  E8 9C F7 5B 00                  call 0x140a19214
00459A78  45 33 C9                        xor r9d, r9d
00459A7B  8B F0                           mov esi, eax
00459A7D  85 C0                           test eax, eax
00459A7F  0F 88 36 02 00 00               js 0x140459cbb
00459A85  44 0F B7 5D E2                  movzx r11d, word ptr [rbp - 0x1e]
00459A8A  45 8D 41 01                     lea r8d, [r9 + 1]
00459A8E  66 45 03 F0                     add r14w, r8w
00459A92  41 8D 51 02                     lea edx, [r9 + 2]
00459A96  4C 8D 15 23 04 B8 00            lea r10, [rip + 0xb80423]
00459A9D  8B 4D E8                        mov ecx, dword ptr [rbp - 0x18]
00459AA0  8B 45 EC                        mov eax, dword ptr [rbp - 0x14]
00459AA3  41 03 C8                        add ecx, r8d
00459AA6  E9 2D FF FF FF                  jmp 0x1404599d8
00459AAB  0F 84 4F 07 00 00               je 0x14045a200
00459AB1  83 FB 08                        cmp ebx, 8
00459AB4  0F 8F 4A 01 00 00               jg 0x140459c04
00459ABA  0F 84 7F 04 00 00               je 0x140459f3f
00459AC0  8B CB                           mov ecx, ebx
00459AC2  85 DB                           test ebx, ebx
00459AC4  0F 84 5B 05 00 00               je 0x14045a025
00459ACA  83 E9 01                        sub ecx, 1
00459ACD  0F 84 9E 01 00 00               je 0x140459c71
00459AD3  83 E9 01                        sub ecx, 1
00459AD6  0F 84 92 03 00 00               je 0x140459e6e
00459ADC  83 E9 01                        sub ecx, 1
00459ADF  0F 84 39 06 00 00               je 0x14045a11e
00459AE5  83 E9 01                        sub ecx, 1
00459AE8  0F 85 BA 04 00 00               jne 0x140459fa8
00459AEE  4B 8B 5C 3C 18                  mov rbx, qword ptr [r12 + r15 + 0x18]
00459AF3  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
00459AF7  8D 3C 85 08 00 00 00            lea edi, [rax*4 + 8]
00459AFE  43 39 7C 3C 04                  cmp dword ptr [r12 + r15 + 4], edi
00459B03  0F 82 50 08 00 00               jb 0x14045a359
00459B09  48 8B CB                        mov rcx, rbx
00459B0C  E8 FF FB 4C 00                  call 0x140929710
00459B11  45 33 C9                        xor r9d, r9d
00459B14  84 C0                           test al, al
00459B16  0F 84 3D 08 00 00               je 0x14045a359
00459B1C  44 0F B7 5D E2                  movzx r11d, word ptr [rbp - 0x1e]
00459B21  45 8D 41 01                     lea r8d, [r9 + 1]
00459B25  41 0F B7 C6                     movzx eax, r14w
00459B29  41 8D 51 02                     lea edx, [r9 + 2]
00459B2D  48 03 C0                        add rax, rax
00459B30  66 45 03 F0                     add r14w, r8w
00459B34  49 89 5C C5 00                  mov qword ptr [r13 + rax*8], rbx
00459B39  41 89 7C C5 08                  mov dword ptr [r13 + rax*8 + 8], edi
00459B3E  45 89 4C C5 0C                  mov dword ptr [r13 + rax*8 + 0xc], r9d
00459B43  48 8B 7D 58                     mov rdi, qword ptr [rbp + 0x58]
00459B47  E9 4A FF FF FF                  jmp 0x140459a96
00459B4C  2B CA                           sub ecx, edx
00459B4E  0F 85 51 03 00 00               jne 0x140459ea5
00459B54  4C 8B 45 78                     mov r8, qword ptr [rbp + 0x78]
00459B58  4B 8B 4C 3C 18                  mov rcx, qword ptr [r12 + r15 + 0x18]
00459B5D  41 0F B7 FB                     movzx edi, r11w
00459B61  41 0F B7 DE                     movzx ebx, r14w
00459B65  4C 03 C3                        add r8, rbx
00459B68  48 C1 E7 04                     shl rdi, 4
00459B6C  48 03 7D 60                     add rdi, qword ptr [rbp + 0x60]
00459B70  48 8B D7                        mov rdx, rdi
00459B73  49 8D 40 01                     lea rax, [r8 + 1]
00459B77  4C 8D 4F 10                     lea r9, [rdi + 0x10]
00459B7B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00459B80  E8 B7 19 5D 00                  call 0x140a2b53c
00459B85  45 33 C9                        xor r9d, r9d
00459B88  8B F0                           mov esi, eax
00459B8A  85 C0                           test eax, eax
00459B8C  0F 88 29 01 00 00               js 0x140459cbb
00459B92  0F B7 0F                        movzx ecx, word ptr [rdi]
00459B95  45 8D 41 01                     lea r8d, [r9 + 1]
00459B99  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00459B9D  48 03 DB                        add rbx, rbx
00459BA0  4C 8B 55 60                     mov r10, qword ptr [rbp + 0x60]
00459BA4  83 C1 02                        add ecx, 2
00459BA7  44 0F B7 5D E2                  movzx r11d, word ptr [rbp - 0x1e]
00459BAC  66 45 03 F0                     add r14w, r8w
00459BB0  66 45 03 D8                     add r11w, r8w
00459BB4  49 89 44 DD 00                  mov qword ptr [r13 + rbx*8], rax
00459BB9  41 89 4C DD 08                  mov dword ptr [r13 + rbx*8 + 8], ecx
00459BBE  45 89 4C DD 0C                  mov dword ptr [r13 + rbx*8 + 0xc], r9d
00459BC3  41 0F B7 C3                     movzx eax, r11w
00459BC7  48 03 C0                        add rax, rax
00459BCA  41 0F B7 CE                     movzx ecx, r14w
00459BCE  48 03 C9                        add rcx, rcx
00459BD1  41 0F B7 14 C2                  movzx edx, word ptr [r10 + rax*8]
00459BD6  49 8B 44 C2 08                  mov rax, qword ptr [r10 + rax*8 + 8]
00459BDB  83 C2 02                        add edx, 2
00459BDE  41 89 54 CD 08                  mov dword ptr [r13 + rcx*8 + 8], edx
00459BE3  66 45 03 D8                     add r11w, r8w
00459BE7  49 89 44 CD 00                  mov qword ptr [r13 + rcx*8], rax
00459BEC  45 89 4C CD 0C                  mov dword ptr [r13 + rcx*8 + 0xc], r9d
00459BF1  66 45 03 F0                     add r14w, r8w
00459BF5  BA 02 00 00 00                  mov edx, 2
00459BFA  66 44 89 5D E2                  mov word ptr [rbp - 0x1e], r11w
00459BFF  E9 3F FF FF FF                  jmp 0x140459b43
00459C04  83 EB 09                        sub ebx, 9
00459C07  0F 84 4F 05 00 00               je 0x14045a15c
00459C0D  83 EB 01                        sub ebx, 1
00459C10  74 41                           je 0x140459c53
00459C12  83 EB 01                        sub ebx, 1
00459C15  74 17                           je 0x140459c2e
00459C17  83 EB 01                        sub ebx, 1
00459C1A  74 12                           je 0x140459c2e
00459C1C  83 EB 01                        sub ebx, 1
00459C1F  0F 84 5B 04 00 00               je 0x14045a080
00459C25  83 EB 01                        sub ebx, 1
00459C28  0F 85 7F 06 00 00               jne 0x14045a2ad
00459C2E  41 0F B7 CE                     movzx ecx, r14w
00459C32  49 8D 47 08                     lea rax, [r15 + 8]
00459C36  48 03 C9                        add rcx, rcx
00459C39  49 03 C4                        add rax, r12
00459C3C  49 89 44 CD 00                  mov qword ptr [r13 + rcx*8], rax
00459C41  49 C7 44 CD 08 08 00 00 00      mov qword ptr [r13 + rcx*8 + 8], 8
00459C4A  66 45 03 F0                     add r14w, r8w
00459C4E  E9 4A FE FF FF                  jmp 0x140459a9d
00459C53  41 0F B7 CE                     movzx ecx, r14w
00459C57  49 8D 47 08                     lea rax, [r15 + 8]
00459C5B  48 03 C9                        add rcx, rcx
00459C5E  49 03 C4                        add rax, r12
00459C61  49 89 44 CD 00                  mov qword ptr [r13 + rcx*8], rax
00459C66  49 C7 44 CD 08 04 00 00 00      mov qword ptr [r13 + rcx*8 + 8], 4
00459C6F  EB D9                           jmp 0x140459c4a
00459C71  4B 8B 54 3C 18                  mov rdx, qword ptr [r12 + r15 + 0x18]
00459C76  48 8B CA                        mov rcx, rdx
00459C79  E8 EE 06 00 00                  call 0x14045a36c
00459C7E  84 C0                           test al, al
00459C80  74 34                           je 0x140459cb6
00459C82  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00459C86  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
00459C8A  41 0F B7 CE                     movzx ecx, r14w
00459C8E  4C 8B C7                        mov r8, rdi
00459C91  48 03 C1                        add rax, rcx
00459C94  48 C1 E1 04                     shl rcx, 4
00459C98  49 03 CD                        add rcx, r13
00459C9B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00459CA0  E8 87 86 5E 00                  call 0x140a4232c
00459CA5  E9 CE FD FF FF                  jmp 0x140459a78
00459CAA  43 83 7C 3C 08 20               cmp dword ptr [r12 + r15 + 8], 0x20
00459CB0  0F 84 8A 05 00 00               je 0x14045a240
00459CB6  BE 0D 00 00 C0                  mov esi, 0xc000000d
00459CBB  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00459CBF  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00459CC7  66 44 89 30                     mov word ptr [rax], r14w
00459CCB  8B C6                           mov eax, esi
00459CCD  48 81 C4 80 00 00 00            add rsp, 0x80
00459CD4  41 5F                           pop r15
00459CD6  41 5E                           pop r14
00459CD8  41 5D                           pop r13
00459CDA  41 5C                           pop r12
00459CDC  5F                              pop rdi
00459CDD  5E                              pop rsi
00459CDE  5D                              pop rbp
00459CDF  C3                              ret
00459CE0  CC                              int3
00459CE1  8B CB                           mov ecx, ebx
00459CE3  83 E9 1C                        sub ecx, 0x1c
00459CE6  0F 84 A3 80 29 00               je 0x1406f1d8f
00459CEC  83 E9 01                        sub ecx, 1
00459CEF  0F 84 9E 05 00 00               je 0x14045a293
00459CF5  83 E9 01                        sub ecx, 1
00459CF8  0F 84 40 06 00 00               je 0x14045a33e
00459CFE  83 E9 01                        sub ecx, 1
00459D01  74 A7                           je 0x140459caa
00459D03  2B CA                           sub ecx, edx
00459D05  0F 85 2F 03 00 00               jne 0x14045a03a
00459D0B  41 0F B7 FB                     movzx edi, r11w
00459D0F  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00459D13  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
00459D18  49 8D 4F 08                     lea rcx, [r15 + 8]
00459D1C  48 C1 E7 04                     shl rdi, 4
00459D20  48 8D 55 F8                     lea rdx, [rbp - 8]
00459D24  48 03 7D 60                     add rdi, qword ptr [rbp + 0x60]
00459D28  4C 8D 45 50                     lea r8, [rbp + 0x50]
00459D2C  49 03 CC                        add rcx, r12
00459D2F  44 88 4D 50                     mov byte ptr [rbp + 0x50], r9b
00459D33  44 88 4D 40                     mov byte ptr [rbp + 0x40], r9b
00459D37  83 FB 23                        cmp ebx, 0x23
00459D3A  44 88 4D E0                     mov byte ptr [rbp - 0x20], r9b
00459D3E  48 8D 47 10                     lea rax, [rdi + 0x10]
00459D42  4C 89 4D F8                     mov qword ptr [rbp - 8], r9
00459D46  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00459D4B  49 0F 45 D1                     cmovne rdx, r9
00459D4F  48 8D 45 40                     lea rax, [rbp + 0x40]
00459D53  4C 8B CF                        mov r9, rdi
00459D56  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00459D5B  E8 68 D0 5F 00                  call 0x140a56dc8
00459D60  8B F0                           mov esi, eax
00459D62  83 FB 23                        cmp ebx, 0x23
00459D65  0F 84 1B 05 00 00               je 0x14045a286
00459D6B  4D 8B 47 18                     mov r8, qword ptr [r15 + 0x18]
00459D6F  45 32 C9                        xor r9b, r9b
00459D72  85 C0                           test eax, eax
00459D74  0F 88 41 FF FF FF               js 0x140459cbb
00459D7A  43 8B 04 3C                     mov eax, dword ptr [r12 + r15]
00459D7E  83 F8 05                        cmp eax, 5
00459D81  0F 85 DD 02 00 00               jne 0x14045a064
00459D87  4D 85 C0                        test r8, r8
00459D8A  75 0A                           jne 0x140459d96
00459D8C  4C 8D 05 2D 01 B8 00            lea r8, [rip + 0xb8012d]
00459D93  45 32 C9                        xor r9b, r9b
00459D96  41 0F B6 40 01                  movzx eax, byte ptr [r8 + 1]
00459D9B  41 BA 01 00 00 00               mov r10d, 1
00459DA1  41 0F B7 D6                     movzx edx, r14w
00459DA5  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
00459DAC  8B C2                           mov eax, edx
00459DAE  48 C1 E0 04                     shl rax, 4
00459DB2  49 03 C5                        add rax, r13
00459DB5  4C 89 00                        mov qword ptr [rax], r8
00459DB8  89 48 08                        mov dword ptr [rax + 8], ecx
00459DBB  83 60 0C 00                     and dword ptr [rax + 0xc], 0
00459DBF  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00459DC3  66 45 03 F2                     add r14w, r10w
00459DC7  44 88 0C 02                     mov byte ptr [rdx + rax], r9b
00459DCB  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00459DCF  0F B7 17                        movzx edx, word ptr [rdi]
00459DD2  4C 8B 4D 78                     mov r9, qword ptr [rbp + 0x78]
00459DD6  83 C2 02                        add edx, 2
00459DD9  44 0F B7 5D E2                  movzx r11d, word ptr [rbp - 0x1e]
00459DDE  45 0F B7 C6                     movzx r8d, r14w
00459DE2  66 45 03 DA                     add r11w, r10w
00459DE6  66 45 03 F2                     add r14w, r10w
00459DEA  41 8B C8                        mov ecx, r8d
00459DED  4C 8B 55 60                     mov r10, qword ptr [rbp + 0x60]
00459DF1  48 C1 E1 04                     shl rcx, 4
00459DF5  49 03 CD                        add rcx, r13
00459DF8  83 61 0C 00                     and dword ptr [rcx + 0xc], 0
00459DFC  48 89 01                        mov qword ptr [rcx], rax
00459DFF  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00459E02  89 51 08                        mov dword ptr [rcx + 8], edx
00459E05  43 88 04 08                     mov byte ptr [r8 + r9], al
00459E09  45 0F B7 C6                     movzx r8d, r14w
00459E0D  41 0F B7 C3                     movzx eax, r11w
00459E11  41 8B C8                        mov ecx, r8d
00459E14  48 03 C0                        add rax, rax
00459E17  48 C1 E1 04                     shl rcx, 4
00459E1B  49 03 CD                        add rcx, r13
00459E1E  41 0F B7 14 C2                  movzx edx, word ptr [r10 + rax*8]
00459E23  49 8B 44 C2 08                  mov rax, qword ptr [r10 + rax*8 + 8]
00459E28  83 C2 02                        add edx, 2
00459E2B  83 61 0C 00                     and dword ptr [rcx + 0xc], 0
00459E2F  48 89 01                        mov qword ptr [rcx], rax
00459E32  8A 45 E0                        mov al, byte ptr [rbp - 0x20]
00459E35  89 51 08                        mov dword ptr [rcx + 8], edx
00459E38  49 8D 4F 08                     lea rcx, [r15 + 8]
00459E3C  43 88 04 08                     mov byte ptr [r8 + r9], al
00459E40  49 03 CC                        add rcx, r12
00459E43  41 B8 01 00 00 00               mov r8d, 1
00459E49  66 45 03 F0                     add r14w, r8w
00459E4D  66 45 03 D8                     add r11w, r8w
00459E51  41 0F B7 C6                     movzx eax, r14w
00459E55  48 03 C0                        add rax, rax
00459E58  45 33 C9                        xor r9d, r9d
00459E5B  49 89 4C C5 00                  mov qword ptr [r13 + rax*8], rcx
00459E60  49 C7 44 C5 08 08 00 00 00      mov qword ptr [r13 + rax*8 + 8], 8
00459E69  E9 83 FD FF FF                  jmp 0x140459bf1
00459E6E  4B 8B 5C 3C 18                  mov rbx, qword ptr [r12 + r15 + 0x18]
00459E73  48 8B CB                        mov rcx, rbx
00459E76  E8 F1 04 00 00                  call 0x14045a36c
00459E7B  84 C0                           test al, al
00459E7D  0F 84 33 FE FF FF               je 0x140459cb6
00459E83  E8 48 09 5F 00                  call 0x140a4a7d0
00459E88  48 8B D3                        mov rdx, rbx
00459E8B  E9 F2 FD FF FF                  jmp 0x140459c82
00459E90  48 85 D2                        test rdx, rdx
00459E93  0F 84 1D FE FF FF               je 0x140459cb6
00459E99  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00459E9C  4C 8D 7A 20                     lea r15, [rdx + 0x20]
00459EA0  E9 16 FB FF FF                  jmp 0x1404599bb
00459EA5  83 E9 01                        sub ecx, 1
00459EA8  0F 85 0D 04 00 00               jne 0x14045a2bb
00459EAE  44 8B 5D E8                     mov r11d, dword ptr [rbp - 0x18]
00459EB2  48 8B 7D 78                     mov rdi, qword ptr [rbp + 0x78]
00459EB6  41 FF C3                        inc r11d
00459EB9  43 8B 4C 3C 08                  mov ecx, dword ptr [r12 + r15 + 8]
00459EBE  45 0F B7 D6                     movzx r10d, r14w
00459EC2  45 8B C3                        mov r8d, r11d
00459EC5  44 89 5D E8                     mov dword ptr [rbp - 0x18], r11d
00459EC9  4C 8D 5D E4                     lea r11, [rbp - 0x1c]
00459ECD  4C 89 5C 24 50                  mov qword ptr [rsp + 0x50], r11
00459ED2  4D 8D 4A 01                     lea r9, [r10 + 1]
00459ED6  49 C1 E0 05                     shl r8, 5
00459EDA  49 8D 14 39                     lea rdx, [r9 + rdi]
00459EDE  49 C1 E1 04                     shl r9, 4
00459EE2  49 8D 04 3A                     lea rax, [r10 + rdi]
00459EE6  4D 03 CD                        add r9, r13
00459EE9  48 8B 7D 58                     mov rdi, qword ptr [rbp + 0x58]
00459EED  4F 8B 44 38 18                  mov r8, qword ptr [r8 + r15 + 0x18]
00459EF2  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00459EF7  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00459EFC  4B 8B 54 3C 18                  mov rdx, qword ptr [r12 + r15 + 0x18]
00459F01  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
00459F06  49 C1 E2 04                     shl r10, 4
00459F0A  4D 03 D5                        add r10, r13
00459F0D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00459F12  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00459F17  E8 D4 C3 60 00                  call 0x140a662f0
00459F1C  45 33 C9                        xor r9d, r9d
00459F1F  8B F0                           mov esi, eax
00459F21  85 C0                           test eax, eax
00459F23  0F 88 92 FD FF FF               js 0x140459cbb
00459F29  44 0F B7 5D E2                  movzx r11d, word ptr [rbp - 0x1e]
00459F2E  41 8D 51 02                     lea edx, [r9 + 2]
00459F32  66 44 03 F2                     add r14w, dx
00459F36  45 8D 41 01                     lea r8d, [r9 + 1]
00459F3A  E9 57 FB FF FF                  jmp 0x140459a96
00459F3F  4F 8B 54 3C 18                  mov r10, qword ptr [r12 + r15 + 0x18]
00459F44  4D 85 D2                        test r10, r10
00459F47  0F 84 69 FD FF FF               je 0x140459cb6
00459F4D  41 8B 0A                        mov ecx, dword ptr [r10]
00459F50  85 C9                           test ecx, ecx
00459F52  0F 84 FA 01 00 00               je 0x14045a152
00459F58  8D 04 49                        lea eax, [rcx + rcx*2]
00459F5B  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
00459F62  43 39 44 3C 04                  cmp dword ptr [r12 + r15 + 4], eax
00459F67  0F 82 49 FD FF FF               jb 0x140459cb6
00459F6D  83 F9 42                        cmp ecx, 0x42
00459F70  0F 87 40 FD FF FF               ja 0x140459cb6
00459F76  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00459F7A  4C 8B CF                        mov r9, rdi
00459F7D  45 0F B7 C6                     movzx r8d, r14w
00459F81  33 D2                           xor edx, edx
00459F83  49 03 C0                        add rax, r8
00459F86  49 8B CA                        mov rcx, r10
00459F89  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00459F8E  48 8D 45 E4                     lea rax, [rbp - 0x1c]
00459F92  49 C1 E0 04                     shl r8, 4
00459F96  4D 03 C5                        add r8, r13
00459F99  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00459F9E  E8 45 8B 60 00                  call 0x140a62ae8
00459FA3  E9 D0 FA FF FF                  jmp 0x140459a78
00459FA8  83 E9 01                        sub ecx, 1
00459FAB  0F 84 5A FD FF FF               je 0x140459d0b
00459FB1  83 E9 01                        sub ecx, 1
00459FB4  0F 85 F3 00 00 00               jne 0x14045a0ad
00459FBA  0F B6 05 00 FF B7 00            movzx eax, byte ptr [rip + 0xb7ff00]
00459FC1  41 0F B7 CE                     movzx ecx, r14w
00459FC5  48 03 C9                        add rcx, rcx
00459FC8  66 45 03 F0                     add r14w, r8w
00459FCC  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
00459FD3  4D 89 54 CD 00                  mov qword ptr [r13 + rcx*8], r10
00459FD8  41 89 44 CD 08                  mov dword ptr [r13 + rcx*8 + 8], eax
00459FDD  45 89 4C CD 0C                  mov dword ptr [r13 + rcx*8 + 0xc], r9d
00459FE2  41 0F B7 CE                     movzx ecx, r14w
00459FE6  48 C1 E1 04                     shl rcx, 4
00459FEA  49 03 CD                        add rcx, r13
00459FED  E8 BE 17 65 00                  call 0x140aab7b0
00459FF2  66 45 03 F0                     add r14w, r8w
00459FF6  49 2B D0                        sub rdx, r8
00459FF9  75 E7                           jne 0x140459fe2
00459FFB  41 0F B7 C6                     movzx eax, r14w
00459FFF  48 8D 0D E2 00 B8 00            lea rcx, [rip + 0xb800e2]
0045A006  48 03 C0                        add rax, rax
0045A009  66 45 03 F0                     add r14w, r8w
0045A00D  49 89 4C C5 00                  mov qword ptr [r13 + rax*8], rcx
0045A012  49 C7 44 C5 08 08 00 00 00      mov qword ptr [r13 + rax*8 + 8], 8
0045A01B  BA 02 00 00 00                  mov edx, 2
0045A020  E9 78 FA FF FF                  jmp 0x140459a9d
0045A025  41 0F B7 CE                     movzx ecx, r14w
0045A029  48 C1 E1 04                     shl rcx, 4
0045A02D  49 03 CD                        add rcx, r13
0045A030  E8 7B 17 65 00                  call 0x140aab7b0
0045A035  E9 10 FC FF FF                  jmp 0x140459c4a
0045A03A  83 E9 01                        sub ecx, 1
0045A03D  0F 85 EF 01 00 00               jne 0x14045a232
0045A043  4C 8B 45 78                     mov r8, qword ptr [rbp + 0x78]
0045A047  4B 8B 4C 3C 18                  mov rcx, qword ptr [r12 + r15 + 0x18]
0045A04C  41 0F B7 D6                     movzx edx, r14w
0045A050  4C 03 C2                        add r8, rdx
0045A053  48 C1 E2 04                     shl rdx, 4
0045A057  49 03 D5                        add rdx, r13
0045A05A  E8 29 03 00 00                  call 0x14045a388
0045A05F  E9 14 FA FF FF                  jmp 0x140459a78
0045A064  83 F8 23                        cmp eax, 0x23
0045A067  0F 84 1A FD FF FF               je 0x140459d87
0045A06D  83 FB 21                        cmp ebx, 0x21
0045A070  0F 85 A6 02 00 00               jne 0x14045a31c
0045A076  4F 8B 44 3C 18                  mov r8, qword ptr [r12 + r15 + 0x18]
0045A07B  E9 16 FD FF FF                  jmp 0x140459d96
0045A080  4B 8B 44 3C 18                  mov rax, qword ptr [r12 + r15 + 0x18]
0045A085  48 8D 0D 6C 04 B8 00            lea rcx, [rip + 0xb8046c]
0045A08C  48 85 C0                        test rax, rax
0045A08F  48 0F 45 C8                     cmovne rcx, rax
0045A093  41 0F B7 C6                     movzx eax, r14w
0045A097  48 03 C0                        add rax, rax
0045A09A  49 89 4C C5 00                  mov qword ptr [r13 + rax*8], rcx
0045A09F  49 C7 44 C5 08 10 00 00 00      mov qword ptr [r13 + rax*8 + 8], 0x10
0045A0A8  E9 9D FB FF FF                  jmp 0x140459c4a
0045A0AD  83 F9 01                        cmp ecx, 1
0045A0B0  0F 85 00 FC FF FF               jne 0x140459cb6
0045A0B6  43 8B 44 3C 10                  mov eax, dword ptr [r12 + r15 + 0x10]
0045A0BB  3B 45 E8                        cmp eax, dword ptr [rbp - 0x18]
0045A0BE  0F 83 F2 FB FF FF               jae 0x140459cb6
0045A0C4  8B D0                           mov edx, eax
0045A0C6  48 C1 E2 05                     shl rdx, 5
0045A0CA  46 39 04 3A                     cmp dword ptr [rdx + r15], r8d
0045A0CE  0F 85 E2 FB FF FF               jne 0x140459cb6
0045A0D4  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0045A0D8  4A 8B 54 3A 18                  mov rdx, qword ptr [rdx + r15 + 0x18]
0045A0DD  47 8B 44 3C 08                  mov r8d, dword ptr [r12 + r15 + 8]
0045A0E2  41 0F B7 CE                     movzx ecx, r14w
0045A0E6  48 03 C1                        add rax, rcx
0045A0E9  48 C1 E1 04                     shl rcx, 4
0045A0ED  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0045A0F2  49 03 CD                        add rcx, r13
0045A0F5  48 8D 45 E4                     lea rax, [rbp - 0x1c]
0045A0F9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0045A0FE  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0045A103  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0045A108  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
0045A10C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0045A111  45 33 C9                        xor r9d, r9d
0045A114  E8 73 E8 62 00                  call 0x140a8898c
0045A119  E9 5A F9 FF FF                  jmp 0x140459a78
0045A11E  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0045A122  4C 8B CF                        mov r9, rdi
0045A125  43 8B 4C 3C 08                  mov ecx, dword ptr [r12 + r15 + 8]
0045A12A  33 D2                           xor edx, edx
0045A12C  45 0F B7 C6                     movzx r8d, r14w
0045A130  49 03 C0                        add rax, r8
0045A133  49 C1 E0 04                     shl r8, 4
0045A137  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0045A13C  4D 03 C5                        add r8, r13
0045A13F  48 8D 45 E4                     lea rax, [rbp - 0x1c]
0045A143  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0045A148  E8 57 9A 65 00                  call 0x140ab3ba4
0045A14D  E9 26 F9 FF FF                  jmp 0x140459a78
0045A152  B8 08 00 00 00                  mov eax, 8
0045A157  E9 06 FE FF FF                  jmp 0x140459f62
0045A15C  43 8B 44 3C 10                  mov eax, dword ptr [r12 + r15 + 0x10]
0045A161  3B C1                           cmp eax, ecx
0045A163  0F 83 4D FB FF FF               jae 0x140459cb6
0045A169  44 8B D0                        mov r10d, eax
0045A16C  49 C1 E2 05                     shl r10, 5
0045A170  47 39 04 3A                     cmp dword ptr [r10 + r15], r8d
0045A174  0F 85 3C FB FF FF               jne 0x140459cb6
0045A17A  43 8B 4C 3C 04                  mov ecx, dword ptr [r12 + r15 + 4]
0045A17F  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0045A189  4C 8B 45 78                     mov r8, qword ptr [rbp + 0x78]
0045A18D  48 F7 E1                        mul rcx
0045A190  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
0045A194  48 C1 EA 04                     shr rdx, 4
0045A198  41 0F B7 DB                     movzx ebx, r11w
0045A19C  44 8B CA                        mov r9d, edx
0045A19F  4B 8B 54 3A 18                  mov rdx, qword ptr [r10 + r15 + 0x18]
0045A1A4  41 0F B7 FE                     movzx edi, r14w
0045A1A8  4C 03 C7                        add r8, rdi
0045A1AB  48 C1 E3 04                     shl rbx, 4
0045A1AF  48 03 5D 60                     add rbx, qword ptr [rbp + 0x60]
0045A1B3  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0045A1B8  4F 8B 44 3C 18                  mov r8, qword ptr [r12 + r15 + 0x18]
0045A1BD  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0045A1C2  E8 71 69 67 00                  call 0x140ad0b38
0045A1C7  0F B7 0B                        movzx ecx, word ptr [rbx]
0045A1CA  48 03 FF                        add rdi, rdi
0045A1CD  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0045A1D1  BA 02 00 00 00                  mov edx, 2
0045A1D6  44 0F B7 5D E2                  movzx r11d, word ptr [rbp - 0x1e]
0045A1DB  03 CA                           add ecx, edx
0045A1DD  45 33 C9                        xor r9d, r9d
0045A1E0  49 89 44 FD 00                  mov qword ptr [r13 + rdi*8], rax
0045A1E5  44 8D 42 FF                     lea r8d, [rdx - 1]
0045A1E9  41 89 4C FD 08                  mov dword ptr [r13 + rdi*8 + 8], ecx
0045A1EE  66 45 03 D8                     add r11w, r8w
0045A1F2  45 89 4C FD 0C                  mov dword ptr [r13 + rdi*8 + 0xc], r9d
0045A1F7  66 45 03 F0                     add r14w, r8w
0045A1FB  E9 FA F9 FF FF                  jmp 0x140459bfa
0045A200  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0045A204  4C 8B CF                        mov r9, rdi
0045A207  4B 8B 4C 3C 18                  mov rcx, qword ptr [r12 + r15 + 0x18]
0045A20C  45 0F B7 C6                     movzx r8d, r14w
0045A210  49 03 C0                        add rax, r8
0045A213  49 C1 E0 04                     shl r8, 4
0045A217  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0045A21C  4D 03 C5                        add r8, r13
0045A21F  48 8D 45 E4                     lea rax, [rbp - 0x1c]
0045A223  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0045A228  E8 03 AF 67 00                  call 0x140ad5130
0045A22D  E9 46 F8 FF FF                  jmp 0x140459a78
0045A232  83 F9 01                        cmp ecx, 1
0045A235  0F 85 7B FA FF FF               jne 0x140459cb6
0045A23B  E9 CB FA FF FF                  jmp 0x140459d0b
0045A240  4F 39 4C 3C 10                  cmp qword ptr [r12 + r15 + 0x10], r9
0045A245  0F 85 6B FA FF FF               jne 0x140459cb6
0045A24B  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0045A24F  45 33 C0                        xor r8d, r8d
0045A252  4B 8B 54 3C 18                  mov rdx, qword ptr [r12 + r15 + 0x18]
0045A257  45 0F B7 CE                     movzx r9d, r14w
0045A25B  49 03 C1                        add rax, r9
0045A25E  49 C1 E1 04                     shl r9, 4
0045A262  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0045A267  41 8D 48 20                     lea ecx, [r8 + 0x20]
0045A26B  48 8D 45 E4                     lea rax, [rbp - 0x1c]
0045A26F  4D 03 CD                        add r9, r13
0045A272  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0045A277  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0045A27C  E8 3F C1 60 00                  call 0x140a663c0
0045A281  E9 F2 F7 FF FF                  jmp 0x140459a78
0045A286  44 8A 4D 50                     mov r9b, byte ptr [rbp + 0x50]
0045A28A  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
0045A28E  E9 DF FA FF FF                  jmp 0x140459d72
0045A293  4F 8B 44 3C 18                  mov r8, qword ptr [r12 + r15 + 0x18]
0045A298  41 8B 80 84 00 00 00            mov eax, dword ptr [r8 + 0x84]
0045A29F  3B 45 E8                        cmp eax, dword ptr [rbp - 0x18]
0045A2A2  0F 83 0E FA FF FF               jae 0x140459cb6
0045A2A8  E9 86 7A 29 00                  jmp 0x1406f1d33
0045A2AD  83 FB 01                        cmp ebx, 1
0045A2B0  0F 85 00 FA FF FF               jne 0x140459cb6
0045A2B6  E9 73 F9 FF FF                  jmp 0x140459c2e
0045A2BB  3B CA                           cmp ecx, edx
0045A2BD  E9 73 FF FF FF                  jmp 0x14045a235
0045A2C2  BA 03 00 00 00                  mov edx, 3
0045A2C7  E9 70 79 29 00                  jmp 0x1406f1c3c
0045A2CC  41 0F B7 C6                     movzx eax, r14w
0045A2D0  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0045A2D4  48 03 C0                        add rax, rax
0045A2D7  49 89 4C C5 00                  mov qword ptr [r13 + rax*8], rcx
0045A2DC  49 C7 44 C5 08 08 00 00 00      mov qword ptr [r13 + rax*8 + 8], 8
0045A2E5  E9 60 F9 FF FF                  jmp 0x140459c4a
0045A2EA  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0045A2EE  4C 8B CF                        mov r9, rdi
0045A2F1  4B 8B 4C 3C 18                  mov rcx, qword ptr [r12 + r15 + 0x18]
0045A2F6  45 0F B7 C6                     movzx r8d, r14w
0045A2FA  49 03 C0                        add rax, r8
0045A2FD  49 C1 E0 04                     shl r8, 4
0045A301  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0045A306  4D 03 C5                        add r8, r13
0045A309  48 8D 45 E4                     lea rax, [rbp - 0x1c]
0045A30D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0045A312  E8 29 81 3C 00                  call 0x140822440
0045A317  E9 5C F7 FF FF                  jmp 0x140459a78
0045A31C  45 84 C9                        test r9b, r9b
0045A31F  0F 84 03 7A 29 00               je 0x1406f1d28
0045A325  4D 85 C0                        test r8, r8
0045A328  0F 84 FA 79 29 00               je 0x1406f1d28
0045A32E  33 D2                           xor edx, edx
0045A330  49 8B C8                        mov rcx, r8
0045A333  E8 38 85 72 00                  call 0x140b82870
0045A338  90                              nop
0045A339  E9 EA 79 29 00                  jmp 0x1406f1d28
0045A33E  4F 39 4C 3C 08                  cmp qword ptr [r12 + r15 + 8], r9
0045A343  0F 85 6D F9 FF FF               jne 0x140459cb6
0045A349  4F 39 4C 3C 10                  cmp qword ptr [r12 + r15 + 0x10], r9
0045A34E  0F 85 62 F9 FF FF               jne 0x140459cb6
0045A354  E9 3A FF FF FF                  jmp 0x14045a293
0045A359  BE 78 00 00 C0                  mov esi, 0xc0000078
0045A35E  E9 58 F9 FF FF                  jmp 0x140459cbb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AdtpPackageParameters(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int16 v_stack_m56;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (128);
    a4 = 0;
    v_stack_m56 = 0;
    v_stack_m54 = 0;
    if (a1 == 0) goto loc_00459E90;
    if (a2 != 0) goto loc_00459CB6;
loc_004599BB:
    v_stack_m48 = a1 + 24;
    v_stack_m4C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
loc_004599D8:
    v_stack_m50 = 2;
    if (2 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) goto loc_00459CBB;
    if (0 >= 14) goto loc_00459CB6;
    if (0 >= 42) goto loc_00459CB6;
    v_r12 = (2) << (5);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1)))) <= 16) goto loc_00459AAB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1)))) == 27) goto loc_00459C53;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1)))) > 27) goto loc_00459CE1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1))))) - (17));
    if (condition_is_equal) goto loc_0045A2EA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0045A2CC;
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0045A2C2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00459B4C;
    result = (a8) + (0);
    a3 = (0) << (4);
    v_stack_m90 = result;
    a3 = (a3) + (a6);
    v_stack_m98 = v_stack_m54;
    result = AdtpBuildMessageString((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1 + 8)), 2, a3, 0);
loc_00459A78:
    a4 = 0;
    if (sign_flag) goto loc_00459CBB;
    v_r14 = (unsigned __int16)((0) + ((unsigned __int16)(a4 + 1)));
loc_00459A96:
loc_00459A9D:
    a1 = (unsigned int)(((unsigned int)(v_stack_m50)) + ((unsigned int)(a4 + 1)));
    goto loc_004599D8;
loc_00459AAB:
    if (condition_is_equal) goto loc_0045A200;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1)))) > 8) goto loc_00459C04;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1)))) == 8) goto loc_00459F3F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1))) == 0) goto loc_0045A025;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1))))) - (1));
    if (condition_is_equal) goto loc_00459C71;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00459E6E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0045A11E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00459FA8;
    if ((*(unsigned int *)(v_r12 + a1 + 24 * 1 + 4)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 1) * 4 + 8))) goto loc_0045A359;
    result = RtlValidSid(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), a4 + 2, a4 + 1, a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0045A359;
    result = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a4 + 1)));
    *(unsigned __int64 *)(a6 + result * 8) = *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24);
    *(unsigned int *)(a6 + result * 8 + 8) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 1) * 4 + 8);
    *(unsigned int *)(a6 + result * 8 + 12) = 0;
loc_00459B43:
    goto loc_00459A96;
loc_00459B4C:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24)) - ((unsigned int)(a4 + 2)));
    if (condition_is_not_equal) goto loc_00459EA5;
    a3 = (a8) + ((unsigned __int16)(v_r14));
    v_rdi = ((unsigned __int16)(v_stack_m56)) << (4);
    v_rdi = (v_rdi) + (a5);
    v_stack_m98 = a3 + 1;
    result = AdtpBuildSockAddrString(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), v_rdi, a3, v_rdi + 16);
    a4 = 0;
    if (sign_flag) goto loc_00459CBB;
    v_rbx = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rdi)) + (2));
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a4 + 1)));
    v_r11 = (unsigned __int16)((v_stack_m56) + ((unsigned __int16)(a4 + 1)));
    *(unsigned __int64 *)(a6 + v_rbx * 8) = *(unsigned __int64 *)(v_rdi + 8);
    *(unsigned int *)(a6 + v_rbx * 8 + 8) = (unsigned int)(a1);
    *(unsigned int *)(a6 + v_rbx * 8 + 12) = 0;
    result = ((unsigned __int16)(v_r11)) + ((unsigned __int16)(v_r11));
    a1 = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    a2 = (unsigned int)((*(unsigned __int16 *)(a5 + result * 8)) + (2));
    *(unsigned int *)(a6 + a1 * 8 + 8) = (unsigned int)(a2);
    v_r11 = (unsigned __int16)((v_r11) + ((unsigned __int16)(a4 + 1)));
    *(unsigned __int64 *)(a6 + a1 * 8) = *(unsigned __int64 *)(a5 + result * 8 + 8);
    *(unsigned int *)(a6 + a1 * 8 + 12) = 0;
loc_00459BF1:
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a4 + 1)));
loc_00459BFA:
    v_stack_m56 = (unsigned __int16)(v_r11);
    goto loc_00459B43;
loc_00459C04:
    v_rbx = (unsigned int)((v_rbx) - (9));
    if (condition_is_equal) goto loc_0045A15C;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00459C53;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00459C2E;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00459C2E;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0045A080;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_0045A2AD;
loc_00459C2E:
    a1 = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    result = (a1 + 24 + 8) + (v_r12);
    *(unsigned __int64 *)(a6 + a1 * 8) = result;
    *(unsigned __int64 *)(a6 + a1 * 8 + 8) = 8;
loc_00459C4A:
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a4 + 1)));
    goto loc_00459A9D;
loc_00459C53:
    a1 = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    result = (a1 + 24 + 8) + (v_r12);
    *(unsigned __int64 *)(a6 + a1 * 8) = result;
    *(unsigned __int64 *)(a6 + a1 * 8 + 8) = 4;
    goto loc_00459C4A;
loc_00459C71:
    result = AdtpIsCorrectlyFormedUnicodeString(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), a4 + 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00459CB6;
loc_00459C82:
    result = (a8) + ((unsigned __int16)(v_r14));
    a1 = ((unsigned __int16)(v_r14)) << (4);
    a1 = (a1) + (a6);
    v_stack_m98 = result;
    result = AdtpEtwBuildString(a1, *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), v_rdi, v_stack_m54);
    goto loc_00459A78;
loc_00459CAA:
    if ((*(unsigned int *)(v_r12 + a1 + 24 * 1 + 8)) == 32) goto loc_0045A240;
loc_00459CB6:
loc_00459CBB:
    *(unsigned __int16 *)(a7) = (unsigned __int16)(v_r14);
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_00459CE1:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p10))) - (28));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0045A293;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0045A33E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00459CAA;
    a1 = (unsigned int)((a1) - ((unsigned int)(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24))));
    if (condition_is_not_equal) goto loc_0045A03A;
loc_00459D0B:
    v_stack_p30 = v_stack_m58;
    v_rdi = ((unsigned __int16)(v_r11)) << (4);
    v_rdi = (v_rdi) + (a5);
    a1 = (a1 + 24 + 8) + (v_r12);
    v_stack_p18 = (unsigned __int8)(v_stack_m54);
    v_stack_p8 = (unsigned __int8)(v_stack_m54);
    v_stack_m58 = (unsigned __int8)(v_stack_m54);
    v_stack_m40 = v_stack_m54;
    v_stack_p28 = v_rdi + 16;
    a2 = v_stack_m40;
    if (((unsigned int)(v_stack_p10)) != 35) { a2 = v_stack_m54; }
    v_stack_p20 = v_stack_p8;
    result = AdtpBuildLogonIdStrings(a1, a2, v_stack_p18, v_rdi);
    if (((unsigned int)(v_stack_p10)) == 35) goto loc_0045A286;
    a4 = 0;
loc_00459D72:
    if (sign_flag) goto loc_00459CBB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 + 24 * 1)))) != 5) goto loc_0045A064;
loc_00459D87:
    if (*(unsigned __int64 *)(a1 + 24 + 24) == 0) {
        a3 = v_rip + 12058925;
        a4 = 0;
    }
    result = ((unsigned int)((unsigned int)((unsigned __int16)(v_r14)))) << (4);
    result = (result) + (a6);
    *(unsigned __int64 *)(result) = a3;
    *(unsigned int *)(result + 8) = (unsigned int)(*(unsigned __int8 *)(a3 + 1) * 4 + 8);
    v_r14 = (unsigned __int16)((v_r14) + (1));
    *(unsigned __int8 *)((unsigned __int16)(v_r14) + a8 * 1) = 0;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rdi)) + (2));
    v_r11 = (unsigned __int16)((v_stack_m56) + (1));
    v_r14 = (unsigned __int16)((v_r14) + (1));
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(v_r14)))) << (4);
    a1 = (a1) + (a6);
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rdi + 8);
    *(unsigned int *)(a1 + 8) = (unsigned int)(a2);
    *(unsigned __int8 *)((unsigned __int16)(v_r14) + a8 * 1) = (unsigned __int8)(v_stack_p8);
    result = ((unsigned __int16)(v_r11)) + ((unsigned __int16)(v_r11));
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(v_r14)))) << (4);
    a1 = (a1) + (a6);
    a2 = (unsigned int)((*(unsigned __int16 *)(a5 + result * 8)) + (2));
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a5 + result * 8 + 8);
    *(unsigned int *)(a1 + 8) = (unsigned int)(a2);
    *(unsigned __int8 *)((unsigned __int16)(v_r14) + a8 * 1) = (unsigned __int8)(v_stack_m58);
    a1 = (a1 + 24 + 8) + (v_r12);
    v_r14 = (unsigned __int16)((v_r14) + (1));
    v_r11 = (unsigned __int16)((v_r11) + (1));
    result = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    a4 = 0;
    *(unsigned __int64 *)(a6 + result * 8) = a1;
    *(unsigned __int64 *)(a6 + result * 8 + 8) = 8;
    goto loc_00459BF1;
loc_00459E6E:
    result = AdtpIsCorrectlyFormedUnicodeString(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00459CB6;
    result = AdtpSubstituteDriveLetter(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24), a2, 1, a4);
    goto loc_00459C82;
loc_00459E90:
    if (*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) == 0) goto loc_00459CB6;
    goto loc_004599BB;
loc_00459EA5:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24)) - (1));
    if (condition_is_not_equal) goto loc_0045A2BB;
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m50)) + 1);
    v_stack_m50 = (unsigned int)(v_r11);
    v_stack_p50 = v_stack_m54;
    a3 = ((unsigned int)((unsigned int)(v_r11))) << (5);
    a4 = ((unsigned __int16)(v_r14) + 1) << (4);
    a4 = (a4) + (a6);
    v_stack_p48 = v_stack_p20;
    v_stack_p40 = (unsigned __int16)(v_r14) + 1 + a8 * 1;
    v_stack_p38 = a4;
    v_r10 = ((unsigned __int16)(v_r14)) << (4);
    v_r10 = (v_r10) + (a6);
    v_stack_p28 = (unsigned __int16)(v_r14) + a8 * 1;
    v_stack_p20 = v_r10;
    result = AdtpBuildSecurityDescriptorChangeString((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 8)), *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), *(unsigned __int64 *)(a3 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), a4);
    a4 = 0;
    if (sign_flag) goto loc_00459CBB;
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a4 + 2)));
    goto loc_00459A96;
loc_00459F3F:
    if (*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24) == 0) goto loc_00459CB6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24)))) == 0) goto loc_0045A152;
loc_00459F62:
    if ((*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24))) * 2 * 4 + 8))) goto loc_00459CB6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24))))) > 66) goto loc_00459CB6;
    a2 = 0;
    result = (a8) + ((unsigned __int16)(v_r14));
    v_stack_p28 = result;
    a3 = ((unsigned __int16)(v_r14)) << (4);
    a3 = (a3) + (a6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildPrivilegeAuditString(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), a2, a3, v_stack_p20);
    goto loc_00459A78;
loc_00459FA8:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24)) - (1));
    if (condition_is_equal) goto loc_00459D0B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0045A0AD;
    a1 = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a3)));
    *(unsigned __int64 *)(a6 + a1 * 8) = *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24);
    *(unsigned int *)(a6 + a1 * 8 + 8) = (unsigned int)(*(unsigned __int8 *)(v_rip + 12058368) * 4 + 8);
    *(unsigned int *)(a6 + a1 * 8 + 12) = (unsigned int)(v_stack_p20);
loc_00459FE2:
    a1 = ((unsigned __int16)(v_r14)) << (4);
    a1 = (a1) + (a6);
    result = AdtpEtwBuildDashString(a1, a2, a3, v_stack_p20);
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a3)));
    a2 = (a2) - (a3);
    if (condition_is_not_equal) goto loc_00459FE2;
    result = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(a3)));
    *(unsigned __int64 *)(a6 + result * 8) = v_rip + 12058850;
    *(unsigned __int64 *)(a6 + result * 8 + 8) = 8;
    goto loc_00459A9D;
loc_0045A025:
    a1 = ((unsigned __int16)(v_r14)) << (4);
    a1 = (a1) + (a6);
    result = AdtpEtwBuildDashString(a1, 2, a3, v_stack_p20);
    goto loc_00459C4A;
loc_0045A03A:
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0045A232;
    a3 = (a8) + ((unsigned __int16)(v_r14));
    a2 = ((unsigned __int16)(v_r14)) << (4);
    a2 = (a2) + (a6);
    result = AdtpBuildMultiSzStringListString(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), a2, a3, v_stack_p20);
    goto loc_00459A78;
loc_0045A064:
    if (((unsigned int)(result)) == 35) goto loc_00459D87;
    if (((unsigned int)(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24))) != 33) goto loc_0045A31C;
    goto loc_00459D96;
loc_0045A080:
    a1 = v_rip + 12059756;
    if (*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24) != 0) { a1 = *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24); }
    result = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    *(unsigned __int64 *)(a6 + result * 8) = a1;
    *(unsigned __int64 *)(a6 + result * 8 + 8) = 16;
    goto loc_00459C4A;
loc_0045A0AD:
    if (((unsigned int)(a1)) != 1) goto loc_00459CB6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 16)))) >= v_stack_m50) goto loc_00459CB6;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 16))))) << (5);
    if ((*(unsigned int *)(a2 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1)) != ((unsigned int)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24)))) goto loc_00459CB6;
    result = (a8) + ((unsigned __int16)(v_r14));
    a1 = ((unsigned __int16)(v_r14)) << (4);
    v_stack_p40 = result;
    a1 = (a1) + (a6);
    v_stack_p38 = v_stack_m54;
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = a1;
    v_stack_p20 = v_stack_p20;
    a4 = 0;
    result = AdtpBuildAccessesString(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 + 56), *(unsigned __int64 *)(a2 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), (unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 8)), a4);
    goto loc_00459A78;
loc_0045A11E:
    a2 = 0;
    result = (a8) + ((unsigned __int16)(v_r14));
    a3 = ((unsigned __int16)(v_r14)) << (4);
    v_stack_p28 = result;
    a3 = (a3) + (a6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildUlongString((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 8)), a2, a3, v_stack_p20);
    goto loc_00459A78;
loc_0045A152:
    goto loc_00459F62;
loc_0045A15C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 16)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 8))))) goto loc_00459CB6;
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 16))))) << (5);
    if ((*(unsigned int *)(v_r10 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1)) != a3) goto loc_00459CB6;
    a2 = (a2) >> (4);
    a3 = (a8) + ((unsigned __int16)(v_r14));
    v_rbx = ((unsigned __int16)(v_stack_m56)) << (4);
    v_rbx = (v_rbx) + (a5);
    v_stack_p28 = a3;
    v_stack_p20 = v_rbx;
    result = AdtpBuildObjectTypeStrings(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 + 56), *(unsigned __int64 *)(v_r10 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), (unsigned int)((unsigned int)(a2)));
    v_rdi = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbx)) + (2));
    a4 = 0;
    *(unsigned __int64 *)(a6 + v_rdi * 8) = *(unsigned __int64 *)(v_rbx + 8);
    *(unsigned int *)(a6 + v_rdi * 8 + 8) = (unsigned int)(a1);
    v_r11 = (unsigned __int16)((v_stack_m56) + ((unsigned __int16)(2 - 1)));
    *(unsigned int *)(a6 + v_rdi * 8 + 12) = 0;
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(2 - 1)));
    goto loc_00459BFA;
loc_0045A200:
    result = (a8) + ((unsigned __int16)(v_r14));
    a3 = ((unsigned __int16)(v_r14)) << (4);
    v_stack_p28 = result;
    a3 = (a3) + (a6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildStringListString(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), 2, a3, v_rdi);
    goto loc_00459A78;
loc_0045A232:
loc_0045A235:
    if (((unsigned int)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24))) != 1) goto loc_00459CB6;
    goto loc_00459D0B;
loc_0045A240:
    if ((*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 16)) != v_rdi) goto loc_00459CB6;
    a3 = 0;
    result = (a8) + ((unsigned __int16)(v_r14));
    a4 = ((unsigned __int16)(v_r14)) << (4);
    v_stack_p30 = result;
    a4 = (a4) + (a6);
    v_stack_p28 = v_stack_m54;
    v_stack_p20 = v_rdi;
    result = AdtpBuildSecurityDescriptorUnicodeString(a3 + 32, *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), a3, a4);
    goto loc_00459A78;
loc_0045A286:
    goto loc_00459D72;
loc_0045A293:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24) + 132)))) >= v_stack_m50) goto loc_00459CB6;
loc_0045A2AD:
    if (((unsigned int)(v_rbx)) != 1) goto loc_00459CB6;
    goto loc_00459C2E;
loc_0045A2BB:
    goto loc_0045A235;
loc_0045A2C2:
loc_0045A2CC:
    result = ((unsigned __int16)(v_r14)) + ((unsigned __int16)(v_r14));
    *(unsigned __int64 *)(a6 + result * 8) = v_stack_p8;
    *(unsigned __int64 *)(a6 + result * 8 + 8) = 8;
    goto loc_00459C4A;
loc_0045A2EA:
    result = (a8) + ((unsigned __int16)(v_r14));
    a3 = ((unsigned __int16)(v_r14)) << (4);
    v_stack_p28 = result;
    a3 = (a3) + (a6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildSidListString(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 24), 3, a3, v_rdi);
    goto loc_00459A78;
loc_0045A31C:
    a2 = 0;
    result = ExFreePoolWithTag(a3, a2, a3, v_rdi);
loc_0045A33E:
    if ((*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 8)) != v_rdi) goto loc_00459CB6;
    if ((*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_r12 + a1 + 24 * 1 + 24) + 32 * 1 + 16)) != v_rdi) goto loc_00459CB6;
    goto loc_0045A293;
loc_0045A359:
    goto loc_00459CBB;
}
```

## 5. (Beta) C Style

```c
int64_t AdtpPackageParameters(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, void *Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint16_t v_stack_m56;
    uint64_t v_stack_m58;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (128);
    Arg4 = 0;
    v_stack_m56 = 0;
    v_stack_m54 = 0;
    if (Arg1 == 0) goto loc_00459E90;
    if (Arg2 != 0) goto loc_00459CB6;
loc_004599BB:
    v_stack_m48 = Arg1 + 24;
    v_stack_m4C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)));
loc_004599D8:
    v_stack_m50 = 2;
    if (2 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8))))) goto loc_00459CBB;
    if (0 >= 14) goto loc_00459CB6;
    if (0 >= 42) goto loc_00459CB6;
    local_r12 = (2) << (5);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1)))) <= 16) goto loc_00459AAB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1)))) == 27) goto loc_00459C53;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1)))) > 27) goto loc_00459CE1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1))))) - (17));
    if (condition_is_equal) goto loc_0045A2EA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0045A2CC;
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0045A2C2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00459B4C;
    result = (Arg8) + (0);
    Arg3 = (0) << (4);
    v_stack_m90 = result;
    Arg3 = (Arg3) + (Arg6);
    v_stack_m98 = v_stack_m54;
    result = AdtpBuildMessageString((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x8)), 2, Arg3, 0);
loc_00459A78:
    Arg4 = 0;
    if (sign_flag) goto loc_00459CBB;
    local_r14 = (uint16_t)((0) + ((uint16_t)(Arg4 + 1)));
loc_00459A96:
loc_00459A9D:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m50)) + ((uint32_t)(Arg4 + 1)));
    goto loc_004599D8;
loc_00459AAB:
    if (condition_is_equal) goto loc_0045A200;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1)))) > 8) goto loc_00459C04;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1)))) == 8) goto loc_00459F3F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1))) == 0) goto loc_0045A025;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1))))) - (1));
    if (condition_is_equal) goto loc_00459C71;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00459E6E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0045A11E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00459FA8;
    if ((*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x4)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x1) * 4 + 8))) goto loc_0045A359;
    result = RtlValidSid(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), Arg4 + 2, Arg4 + 1, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_0045A359;
    result = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg4 + 1)));
    *(uint64_t *)(arg6 + result * 8) = *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18);
    *(uint32_t *)(arg6 + result * 8 + 0x8) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x1) * 4 + 8);
    *(uint32_t *)(arg6 + result * 8 + 0xC) = 0;
loc_00459B43:
    goto loc_00459A96;
loc_00459B4C:
    Arg1 = (uint32_t)((*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18)) - ((uint32_t)(Arg4 + 2)));
    if (condition_is_not_equal) goto loc_00459EA5;
    Arg3 = (Arg8) + ((uint16_t)(local_r14));
    local_rdi = ((uint16_t)(v_stack_m56)) << (4);
    local_rdi = (local_rdi) + (Arg5);
    v_stack_m98 = Arg3 + 1;
    result = AdtpBuildSockAddrString(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), local_rdi, Arg3, local_rdi + 16);
    Arg4 = 0;
    if (sign_flag) goto loc_00459CBB;
    local_rbx = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    Arg1 = (uint32_t)((*(uint16_t *)(local_rdi)) + (2));
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg4 + 1)));
    local_r11 = (uint16_t)((v_stack_m56) + ((uint16_t)(Arg4 + 1)));
    *(uint64_t *)(arg6 + local_rbx * 8) = *(uint64_t *)(local_rdi + 0x8);
    *(uint32_t *)(arg6 + local_rbx * 8 + 0x8) = (uint32_t)(Arg1);
    *(uint32_t *)(arg6 + local_rbx * 8 + 0xC) = 0;
    result = ((uint16_t)(local_r11)) + ((uint16_t)(local_r11));
    Arg1 = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    Arg2 = (uint32_t)((*(uint16_t *)(arg5 + result * 8)) + (2));
    *(uint32_t *)(arg6 + Arg1 * 8 + 0x8) = (uint32_t)(Arg2);
    local_r11 = (uint16_t)((local_r11) + ((uint16_t)(Arg4 + 1)));
    *(uint64_t *)(arg6 + Arg1 * 8) = *(uint64_t *)(arg5 + result * 8 + 0x8);
    *(uint32_t *)(arg6 + Arg1 * 8 + 0xC) = 0;
loc_00459BF1:
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg4 + 1)));
loc_00459BFA:
    v_stack_m56 = (uint16_t)(local_r11);
    goto loc_00459B43;
loc_00459C04:
    local_rbx = (uint32_t)((local_rbx) - (9));
    if (condition_is_equal) goto loc_0045A15C;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00459C53;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00459C2E;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00459C2E;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0045A080;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_0045A2AD;
loc_00459C2E:
    Arg1 = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    result = (Arg1 + 24 + 8) + (local_r12);
    *(uint64_t *)(arg6 + Arg1 * 8) = result;
    *(uint64_t *)(arg6 + Arg1 * 8 + 0x8) = 8;
loc_00459C4A:
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg4 + 1)));
    goto loc_00459A9D;
loc_00459C53:
    Arg1 = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    result = (Arg1 + 24 + 8) + (local_r12);
    *(uint64_t *)(arg6 + Arg1 * 8) = result;
    *(uint64_t *)(arg6 + Arg1 * 8 + 0x8) = 4;
    goto loc_00459C4A;
loc_00459C71:
    result = AdtpIsCorrectlyFormedUnicodeString(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), Arg4 + 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00459CB6;
loc_00459C82:
    result = (Arg8) + ((uint16_t)(local_r14));
    Arg1 = ((uint16_t)(local_r14)) << (4);
    Arg1 = (Arg1) + (Arg6);
    v_stack_m98 = result;
    result = AdtpEtwBuildString(Arg1, *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), local_rdi, v_stack_m54);
    goto loc_00459A78;
loc_00459CAA:
    if ((*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x8)) == 32) goto loc_0045A240;
loc_00459CB6:
loc_00459CBB:
    *(uint16_t *)(arg7) = (uint16_t)(local_r14);
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_00459CE1:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p10))) - (28));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0045A293;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0045A33E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00459CAA;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18))));
    if (condition_is_not_equal) goto loc_0045A03A;
loc_00459D0B:
    v_stack_p30 = v_stack_m58;
    local_rdi = ((uint16_t)(local_r11)) << (4);
    local_rdi = (local_rdi) + (Arg5);
    Arg1 = (Arg1 + 24 + 8) + (local_r12);
    v_stack_p18 = (uint8_t)(v_stack_m54);
    v_stack_p8 = (uint8_t)(v_stack_m54);
    v_stack_m58 = (uint8_t)(v_stack_m54);
    v_stack_m40 = v_stack_m54;
    v_stack_p28 = local_rdi + 16;
    Arg2 = v_stack_m40;
    if (((uint32_t)(v_stack_p10)) != 35) { Arg2 = v_stack_m54; }
    v_stack_p20 = v_stack_p8;
    result = AdtpBuildLogonIdStrings(Arg1, Arg2, v_stack_p18, local_rdi);
    if (((uint32_t)(v_stack_p10)) == 35) goto loc_0045A286;
    Arg4 = 0;
loc_00459D72:
    if (sign_flag) goto loc_00459CBB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 + 0x18 * 1)))) != 5) goto loc_0045A064;
loc_00459D87:
    if (*(uint64_t *)(Arg1 + 0x18 + 0x18) == 0) {
        Arg3 = v_rip + 12058925;
        Arg4 = 0;
    }
    result = ((uint32_t)((uint32_t)((uint16_t)(local_r14)))) << (4);
    result = (result) + (Arg6);
    *(uint64_t *)(result) = Arg3;
    *(uint32_t *)(result + 0x8) = (uint32_t)(*(uint8_t *)(Arg3 + 0x1) * 4 + 8);
    local_r14 = (uint16_t)((local_r14) + (1));
    *(uint8_t *)((uint16_t)(local_r14) + arg8 * 1) = 0;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rdi)) + (2));
    local_r11 = (uint16_t)((v_stack_m56) + (1));
    local_r14 = (uint16_t)((local_r14) + (1));
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(local_r14)))) << (4);
    Arg1 = (Arg1) + (Arg6);
    *(uint64_t *)(Arg1) = *(uint64_t *)(local_rdi + 0x8);
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)(Arg2);
    *(uint8_t *)((uint16_t)(local_r14) + arg8 * 1) = (uint8_t)(v_stack_p8);
    result = ((uint16_t)(local_r11)) + ((uint16_t)(local_r11));
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(local_r14)))) << (4);
    Arg1 = (Arg1) + (Arg6);
    Arg2 = (uint32_t)((*(uint16_t *)(arg5 + result * 8)) + (2));
    *(uint64_t *)(Arg1) = *(uint64_t *)(arg5 + result * 8 + 0x8);
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)(Arg2);
    *(uint8_t *)((uint16_t)(local_r14) + arg8 * 1) = (uint8_t)(v_stack_m58);
    Arg1 = (Arg1 + 24 + 8) + (local_r12);
    local_r14 = (uint16_t)((local_r14) + (1));
    local_r11 = (uint16_t)((local_r11) + (1));
    result = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    Arg4 = 0;
    *(uint64_t *)(arg6 + result * 8) = Arg1;
    *(uint64_t *)(arg6 + result * 8 + 0x8) = 8;
    goto loc_00459BF1;
loc_00459E6E:
    result = AdtpIsCorrectlyFormedUnicodeString(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), Arg2, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00459CB6;
    result = AdtpSubstituteDriveLetter(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18), Arg2, 1, Arg4);
    goto loc_00459C82;
loc_00459E90:
    if (*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) == 0) goto loc_00459CB6;
    goto loc_004599BB;
loc_00459EA5:
    Arg1 = (uint32_t)((*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18)) - (1));
    if (condition_is_not_equal) goto loc_0045A2BB;
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m50)) + 1);
    v_stack_m50 = (uint32_t)(local_r11);
    v_stack_p50 = v_stack_m54;
    Arg3 = ((uint32_t)((uint32_t)(local_r11))) << (5);
    Arg4 = ((uint16_t)(local_r14) + 1) << (4);
    Arg4 = (Arg4) + (Arg6);
    v_stack_p48 = v_stack_p20;
    v_stack_p40 = (uint16_t)(local_r14) + 1 + Arg8 * 1;
    v_stack_p38 = Arg4;
    local_r10 = ((uint16_t)(local_r14)) << (4);
    local_r10 = (local_r10) + (Arg6);
    v_stack_p28 = (uint16_t)(local_r14) + Arg8 * 1;
    v_stack_p20 = local_r10;
    result = AdtpBuildSecurityDescriptorChangeString((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x8)), *(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), *(uint64_t *)(Arg3 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_00459CBB;
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg4 + 2)));
    goto loc_00459A96;
loc_00459F3F:
    if (*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18) == 0) goto loc_00459CB6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18)))) == 0) goto loc_0045A152;
loc_00459F62:
    if ((*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18))) * 2 * 4 + 8))) goto loc_00459CB6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18))))) > 66) goto loc_00459CB6;
    Arg2 = 0;
    result = (Arg8) + ((uint16_t)(local_r14));
    v_stack_p28 = result;
    Arg3 = ((uint16_t)(local_r14)) << (4);
    Arg3 = (Arg3) + (Arg6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildPrivilegeAuditString(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), Arg2, Arg3, v_stack_p20);
    goto loc_00459A78;
loc_00459FA8:
    Arg1 = (uint32_t)((*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18)) - (1));
    if (condition_is_equal) goto loc_00459D0B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0045A0AD;
    Arg1 = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg3)));
    *(uint64_t *)(arg6 + Arg1 * 8) = *(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18);
    *(uint32_t *)(arg6 + Arg1 * 8 + 0x8) = (uint32_t)(*(uint8_t *)(v_rip + 0xB7FF00) * 4 + 8);
    *(uint32_t *)(arg6 + Arg1 * 8 + 0xC) = (uint32_t)(v_stack_p20);
loc_00459FE2:
    Arg1 = ((uint16_t)(local_r14)) << (4);
    Arg1 = (Arg1) + (Arg6);
    result = AdtpEtwBuildDashString(Arg1, Arg2, Arg3, v_stack_p20);
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg3)));
    Arg2 = (Arg2) - (Arg3);
    if (condition_is_not_equal) goto loc_00459FE2;
    result = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(Arg3)));
    *(uint64_t *)(arg6 + result * 8) = v_rip + 12058850;
    *(uint64_t *)(arg6 + result * 8 + 0x8) = 8;
    goto loc_00459A9D;
loc_0045A025:
    Arg1 = ((uint16_t)(local_r14)) << (4);
    Arg1 = (Arg1) + (Arg6);
    result = AdtpEtwBuildDashString(Arg1, 2, Arg3, v_stack_p20);
    goto loc_00459C4A;
loc_0045A03A:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0045A232;
    Arg3 = (Arg8) + ((uint16_t)(local_r14));
    Arg2 = ((uint16_t)(local_r14)) << (4);
    Arg2 = (Arg2) + (Arg6);
    result = AdtpBuildMultiSzStringListString(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), Arg2, Arg3, v_stack_p20);
    goto loc_00459A78;
loc_0045A064:
    if (((uint32_t)(result)) == 35) goto loc_00459D87;
    if (((uint32_t)(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18))) != 33) goto loc_0045A31C;
    goto loc_00459D96;
loc_0045A080:
    Arg1 = v_rip + 12059756;
    if (*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18) != 0) { Arg1 = *(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18); }
    result = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    *(uint64_t *)(arg6 + result * 8) = Arg1;
    *(uint64_t *)(arg6 + result * 8 + 0x8) = 16;
    goto loc_00459C4A;
loc_0045A0AD:
    if (((uint32_t)(Arg1)) != 1) goto loc_00459CB6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x10)))) >= v_stack_m50) goto loc_00459CB6;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x10))))) << (5);
    if ((*(uint32_t *)(Arg2 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1)) != ((uint32_t)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18)))) goto loc_00459CB6;
    result = (Arg8) + ((uint16_t)(local_r14));
    Arg1 = ((uint16_t)(local_r14)) << (4);
    v_stack_p40 = result;
    Arg1 = (Arg1) + (Arg6);
    v_stack_p38 = v_stack_m54;
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = Arg1;
    v_stack_p20 = v_stack_p20;
    Arg4 = 0;
    result = AdtpBuildAccessesString(*(uint64_t *)(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 + 0x38), *(uint64_t *)(Arg2 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), (uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x8)), Arg4);
    goto loc_00459A78;
loc_0045A11E:
    Arg2 = 0;
    result = (Arg8) + ((uint16_t)(local_r14));
    Arg3 = ((uint16_t)(local_r14)) << (4);
    v_stack_p28 = result;
    Arg3 = (Arg3) + (Arg6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildUlongString((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x8)), Arg2, Arg3, v_stack_p20);
    goto loc_00459A78;
loc_0045A152:
    goto loc_00459F62;
loc_0045A15C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x10)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x8))))) goto loc_00459CB6;
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x10))))) << (5);
    if ((*(uint32_t *)(local_r10 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1)) != Arg3) goto loc_00459CB6;
    Arg2 = (Arg2) >> (4);
    Arg3 = (Arg8) + ((uint16_t)(local_r14));
    local_rbx = ((uint16_t)(v_stack_m56)) << (4);
    local_rbx = (local_rbx) + (Arg5);
    v_stack_p28 = Arg3;
    v_stack_p20 = local_rbx;
    result = AdtpBuildObjectTypeStrings(*(uint64_t *)(*(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 + 0x38), *(uint64_t *)(local_r10 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), *(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), (uint32_t)((uint32_t)(Arg2)));
    local_rdi = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    Arg1 = (uint32_t)((*(uint16_t *)(local_rbx)) + (2));
    Arg4 = 0;
    *(uint64_t *)(arg6 + local_rdi * 8) = *(uint64_t *)(local_rbx + 0x8);
    *(uint32_t *)(arg6 + local_rdi * 8 + 0x8) = (uint32_t)(Arg1);
    local_r11 = (uint16_t)((v_stack_m56) + ((uint16_t)(2 - 1)));
    *(uint32_t *)(arg6 + local_rdi * 8 + 0xC) = 0;
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(2 - 1)));
    goto loc_00459BFA;
loc_0045A200:
    result = (Arg8) + ((uint16_t)(local_r14));
    Arg3 = ((uint16_t)(local_r14)) << (4);
    v_stack_p28 = result;
    Arg3 = (Arg3) + (Arg6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildStringListString(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), 2, Arg3, local_rdi);
    goto loc_00459A78;
loc_0045A232:
loc_0045A235:
    if (((uint32_t)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18))) != 1) goto loc_00459CB6;
    goto loc_00459D0B;
loc_0045A240:
    if ((*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x10)) != local_rdi) goto loc_00459CB6;
    Arg3 = 0;
    result = (Arg8) + ((uint16_t)(local_r14));
    Arg4 = ((uint16_t)(local_r14)) << (4);
    v_stack_p30 = result;
    Arg4 = (Arg4) + (Arg6);
    v_stack_p28 = v_stack_m54;
    v_stack_p20 = local_rdi;
    result = AdtpBuildSecurityDescriptorUnicodeString(Arg3 + 32, *(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), Arg3, Arg4);
    goto loc_00459A78;
loc_0045A286:
    goto loc_00459D72;
loc_0045A293:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18) + 0x84)))) >= v_stack_m50) goto loc_00459CB6;
loc_0045A2AD:
    if (((uint32_t)(local_rbx)) != 1) goto loc_00459CB6;
    goto loc_00459C2E;
loc_0045A2BB:
    goto loc_0045A235;
loc_0045A2C2:
loc_0045A2CC:
    result = ((uint16_t)(local_r14)) + ((uint16_t)(local_r14));
    *(uint64_t *)(arg6 + result * 8) = v_stack_p8;
    *(uint64_t *)(arg6 + result * 8 + 0x8) = 8;
    goto loc_00459C4A;
loc_0045A2EA:
    result = (Arg8) + ((uint16_t)(local_r14));
    Arg3 = ((uint16_t)(local_r14)) << (4);
    v_stack_p28 = result;
    Arg3 = (Arg3) + (Arg6);
    v_stack_p20 = v_stack_m54;
    result = AdtpBuildSidListString(*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x18), 3, Arg3, local_rdi);
    goto loc_00459A78;
loc_0045A31C:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg3, Arg2, Arg3, local_rdi);
loc_0045A33E:
    if ((*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x8)) != local_rdi) goto loc_00459CB6;
    if ((*(uint64_t *)(local_r12 + *(uint64_t *)(local_r12 + Arg1 + 0x18 * 1 + 0x18) + 0x20 * 1 + 0x10)) != local_rdi) goto loc_00459CB6;
    goto loc_0045A293;
loc_0045A359:
    goto loc_00459CBB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0 + rax*8` | `16` | `R` |
| `Arg5` | `+ 0x8 + rax*8` | `64` | `R` |
| `Arg6` | `+ 0x0 + rax*8` | `64` | `W` |
| `Arg6` | `+ 0x0 + rbx*8` | `64` | `W` |
| `Arg6` | `+ 0x0 + rcx*8` | `64` | `W` |
| `Arg6` | `+ 0x0 + rdi*8` | `64` | `W` |
| `Arg6` | `+ 0x8 + rax*8` | `32` | `W` |
| `Arg6` | `+ 0x8 + rax*8` | `64` | `W` |
| `Arg6` | `+ 0x8 + rbx*8` | `32` | `W` |
| `Arg6` | `+ 0x8 + rcx*8` | `32` | `W` |
| `Arg6` | `+ 0x8 + rcx*8` | `64` | `W` |
| `Arg6` | `+ 0x8 + rdi*8` | `32` | `W` |
| `Arg6` | `+ 0xC + rax*8` | `32` | `W` |
| `Arg6` | `+ 0xC + rbx*8` | `32` | `W` |
| `Arg6` | `+ 0xC + rcx*8` | `32` | `W` |
| `Arg6` | `+ 0xC + rdi*8` | `32` | `W` |
| `Arg7` | `+ 0x0` | `16` | `W` |
| `Arg8` | `+ 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00459964&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
