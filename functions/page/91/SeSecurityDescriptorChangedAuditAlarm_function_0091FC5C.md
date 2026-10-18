# SeSecurityDescriptorChangedAuditAlarm

- RVA: `0x0091FC5C`–`0x00920419` (길이 `1,981` bytes)
- VA: `0x000000014091FC5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008B5F4`
- 디코드: `478`개 명령, `1,981/1,981` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0091FCE1` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0091FD10` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x0091FD3C` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x0091FE15` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0091FEE6` → [SepQueryTypeString](../92/SepQueryTypeString_function_00920420.md) (function, `0x00920420`)
- `0x0091FF19` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00920035` → [SepQueryNameString](../8F/SepQueryNameString_function_008F5DE8.md) (function, `0x008F5DE8`)
- `0x009200A7` → [SepAdtSecurityDescriptorChangedAuditAlarm](SepAdtSecurityDescriptorChangedAuditAlarm_function_0091E3E8.md) (function, `0x0091E3E8`)
- `0x009200F0` → [SepAdtSecurityDescriptorChangedAuditAlarm](SepAdtSecurityDescriptorChangedAuditAlarm_function_0091E3E8.md) (function, `0x0091E3E8`)
- `0x00920120` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x0092019D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009202EA` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x009203C5` → [SepAdtSecurityDescriptorChangedAuditAlarm](SepAdtSecurityDescriptorChangedAuditAlarm_function_0091E3E8.md) (function, `0x0091E3E8`)
- `0x00920403` → [SepAdtSecurityDescriptorChangedAuditAlarm](SepAdtSecurityDescriptorChangedAuditAlarm_function_0091E3E8.md) (function, `0x0091E3E8`)
- `0x0092040F` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)

### Direct callers
- [NtSetSecurityObject](../AD/NtSetSecurityObject_function_00ADE2B0.md) at `0x00ADE64A`

### Static image references
- `0x0092007A` → RVA `0x000013A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0091FF19` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092019D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009202EA` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **20**
  - `0x0091FE92` → [sub_00B222A0 + 0x203](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x0091FFFF` → [sub_00B222A0 + 0x203](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920158` → [sub_00B222A0 + 0x79](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920168` → [sub_00B222A0 + 0x19D](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x009201C7` → [sub_00B222A0](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x009201D0` → [sub_00B222A0 + 0x5](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x009201DB` → [sub_00B222A0](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x009201E5` → [sub_00B222A0 + 0x9](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x009201FA` → [sub_00B222A0 + 0x57](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920203` → [sub_00B222A0 + 0x5F](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x0092020F` → [sub_00B222A0 + 0x57](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920225` → [sub_00B222A0 + 0x68](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x0092022E` → [sub_00B222A0 + 0x70](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x0092023A` → [sub_00B222A0 + 0x68](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920302` → [sub_00B222A0 + 0xFF](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920362` → [sub_00B222A0 + 0x292](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x0092036C` → [sub_00B222A0 + 0x241](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920377` → [sub_00B222A0 + 0x210](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x00920383` → [sub_00B222A0 + 0x20A](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)
  - `0x0092038C` → [sub_00B222A0 + 0x214](../B2/Unknown_function_00B222A0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0091FC5C  48 8B C4                        mov rax, rsp
0091FC5F  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
0091FC63  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0091FC67  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0091FC6B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0091FC6F  55                              push rbp
0091FC70  56                              push rsi
0091FC71  57                              push rdi
0091FC72  41 54                           push r12
0091FC74  41 55                           push r13
0091FC76  41 56                           push r14
0091FC78  41 57                           push r15
0091FC7A  48 8D 68 C1                     lea rbp, [rax - 0x3f]
0091FC7E  48 81 EC F0 00 00 00            sub rsp, 0xf0
0091FC85  45 33 F6                        xor r14d, r14d
0091FC88  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0091FC8C  0F 57 C0                        xorps xmm0, xmm0
0091FC8F  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
0091FC94  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
0091FC98  41 8B DE                        mov ebx, r14d
0091FC9B  4C 89 75 97                     mov qword ptr [rbp - 0x69], r14
0091FC9F  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
0091FCA3  4C 89 75 9F                     mov qword ptr [rbp - 0x61], r14
0091FCA7  41 8B FE                        mov edi, r14d
0091FCAA  4C 89 75 C7                     mov qword ptr [rbp - 0x39], r14
0091FCAE  45 8B E6                        mov r12d, r14d
0091FCB1  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
0091FCB6  45 8B EE                        mov r13d, r14d
0091FCB9  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
0091FCBE  49 8B F0                        mov rsi, r8
0091FCC1  44 89 75 87                     mov dword ptr [rbp - 0x79], r14d
0091FCC5  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
0091FCCA  66 44 89 75 5F                  mov word ptr [rbp + 0x5f], r14w
0091FCCF  4C 89 75 BF                     mov qword ptr [rbp - 0x41], r14
0091FCD3  66 44 89 75 47                  mov word ptr [rbp + 0x47], r14w
0091FCD8  4C 89 75 B7                     mov qword ptr [rbp - 0x49], r14
0091FCDC  66 44 89 75 6F                  mov word ptr [rbp + 0x6f], r14w
0091FCE1  E8 3A BB F4 FF                  call 0x14086b820
0091FCE6  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0091FCEA  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
0091FCEE  48 85 C0                        test rax, rax
0091FCF1  48 0F 45 C8                     cmovne rcx, rax
0091FCF5  48 89 4D 8F                     mov qword ptr [rbp - 0x71], rcx
0091FCF9  48 85 C9                        test rcx, rcx
0091FCFC  0F 84 19 04 00 00               je 0x14092011b
0091FD02  4C 8D 4D CF                     lea r9, [rbp - 0x31]
0091FD06  45 33 C0                        xor r8d, r8d
0091FD09  B2 01                           mov dl, 1
0091FD0B  B9 8E 00 00 00                  mov ecx, 0x8e
0091FD10  E8 AB 0D F5 FF                  call 0x140870ac0
0091FD15  45 33 DB                        xor r11d, r11d
0091FD18  44 8A F8                        mov r15b, al
0091FD1B  84 C0                           test al, al
0091FD1D  0F 85 D7 03 00 00               jne 0x1409200fa
0091FD23  44 8B 75 77                     mov r14d, dword ptr [rbp + 0x77]
0091FD27  41 0F BA E6 18                  bt r14d, 0x18
0091FD2C  73 2B                           jae 0x14091fd59
0091FD2E  4C 8D 4D CF                     lea r9, [rbp - 0x31]
0091FD32  45 33 C0                        xor r8d, r8d
0091FD35  B2 01                           mov dl, 1
0091FD37  B9 8C 00 00 00                  mov ecx, 0x8c
0091FD3C  E8 7F 0D F5 FF                  call 0x140870ac0
0091FD41  45 33 DB                        xor r11d, r11d
0091FD44  84 C0                           test al, al
0091FD46  74 08                           je 0x14091fd50
0091FD48  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0091FD4B  83 E0 08                        and eax, 8
0091FD4E  0B F8                           or edi, eax
0091FD50  45 84 FF                        test r15b, r15b
0091FD53  0F 85 4E 04 00 00               jne 0x1409201a7
0091FD59  48 85 F6                        test rsi, rsi
0091FD5C  0F 84 70 01 00 00               je 0x14091fed2
0091FD62  66 44 39 1E                     cmp word ptr [rsi], r11w
0091FD66  0F 84 66 01 00 00               je 0x14091fed2
0091FD6C  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
0091FD71  48 8B B5 8F 00 00 00            mov rsi, qword ptr [rbp + 0x8f]
0091FD78  41 81 E6 FF FF FF FE            and r14d, 0xfeffffff
0091FD7F  0F 85 3C 04 00 00               jne 0x1409201c1
0091FD85  4C 8B BD A7 00 00 00            mov r15, qword ptr [rbp + 0xa7]
0091FD8C  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
0091FD91  A8 10                           test al, 0x10
0091FD93  0F 85 9D 00 00 00               jne 0x14091fe36
0091FD99  4D 8B C3                        mov r8, r11
0091FD9C  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0091FDA1  48 85 F6                        test rsi, rsi
0091FDA4  0F 85 AA 00 00 00               jne 0x14091fe54
0091FDAA  4C 8B B5 87 00 00 00            mov r14, qword ptr [rbp + 0x87]
0091FDB1  4D 85 F6                        test r14, r14
0091FDB4  0F 85 39 04 00 00               jne 0x1409201f3
0091FDBA  48 8B 95 97 00 00 00            mov rdx, qword ptr [rbp + 0x97]
0091FDC1  48 85 D2                        test rdx, rdx
0091FDC4  0F 85 E6 00 00 00               jne 0x14091feb0
0091FDCA  48 8B CB                        mov rcx, rbx
0091FDCD  4C 8B 8D 9F 00 00 00            mov r9, qword ptr [rbp + 0x9f]
0091FDD4  4D 85 C9                        test r9, r9
0091FDD7  0F 85 41 04 00 00               jne 0x14092021e
0091FDDD  48 8B D3                        mov rdx, rbx
0091FDE0  4D 85 C0                        test r8, r8
0091FDE3  74 7F                           je 0x14091fe64
0091FDE5  66 45 39 58 04                  cmp word ptr [r8 + 4], r11w
0091FDEA  74 78                           je 0x14091fe64
0091FDEC  85 FF                           test edi, edi
0091FDEE  0F 85 2F 01 00 00               jne 0x14091ff23
0091FDF4  4D 85 F6                        test r14, r14
0091FDF7  0F 85 5D 05 00 00               jne 0x14092035a
0091FDFD  85 DB                           test ebx, ebx
0091FDFF  0F 85 1C 02 00 00               jne 0x140920021
0091FE05  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0091FE09  85 C0                           test eax, eax
0091FE0B  0F 88 FC 05 00 00               js 0x14092040d
0091FE11  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0091FE15  E8 F6 B8 F4 FF                  call 0x14086b710
0091FE1A  48 8B 9C 24 40 01 00 00         mov rbx, qword ptr [rsp + 0x140]
0091FE22  48 81 C4 F0 00 00 00            add rsp, 0xf0
0091FE29  41 5F                           pop r15
0091FE2B  41 5E                           pop r14
0091FE2D  41 5D                           pop r13
0091FE2F  41 5C                           pop r12
0091FE31  5F                              pop rdi
0091FE32  5E                              pop rsi
0091FE33  5D                              pop rbp
0091FE34  C3                              ret
0091FE35  CC                              int3
0091FE36  66 85 C0                        test ax, ax
0091FE39  0F 89 D3 02 00 00               jns 0x140920112
0091FE3F  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
0091FE43  85 C0                           test eax, eax
0091FE45  0F 84 4E FF FF FF               je 0x14091fd99
0091FE4B  4D 8D 04 07                     lea r8, [r15 + rax]
0091FE4F  E9 48 FF FF FF                  jmp 0x14091fd9c
0091FE54  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0091FE58  A8 10                           test al, 0x10
0091FE5A  75 3B                           jne 0x14091fe97
0091FE5C  4D 8B EB                        mov r13, r11
0091FE5F  E9 46 FF FF FF                  jmp 0x14091fdaa
0091FE64  4D 85 ED                        test r13, r13
0091FE67  75 5B                           jne 0x14091fec4
0091FE69  4D 85 E4                        test r12, r12
0091FE6C  0F 85 B9 04 00 00               jne 0x14092032b
0091FE72  48 85 C9                        test rcx, rcx
0091FE75  0F 85 C8 04 00 00               jne 0x140920343
0091FE7B  48 85 D2                        test rdx, rdx
0091FE7E  0F 84 70 FF FF FF               je 0x14091fdf4
0091FE84  66 44 39 5A 04                  cmp word ptr [rdx + 4], r11w
0091FE89  0F 84 65 FF FF FF               je 0x14091fdf4
0091FE8F  83 E7 40                        and edi, 0x40
0091FE92  E9 0C 26 20 00                  jmp 0x140b224a3
0091FE97  66 85 C0                        test ax, ax
0091FE9A  0F 89 4A 03 00 00               jns 0x1409201ea
0091FEA0  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
0091FEA3  85 C0                           test eax, eax
0091FEA5  74 B5                           je 0x14091fe5c
0091FEA7  4C 8D 2C 06                     lea r13, [rsi + rax]
0091FEAB  E9 FA FE FF FF                  jmp 0x14091fdaa
0091FEB0  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0091FEB4  A8 10                           test al, 0x10
0091FEB6  0F 85 48 01 00 00               jne 0x140920004
0091FEBC  49 8B CB                        mov rcx, r11
0091FEBF  E9 09 FF FF FF                  jmp 0x14091fdcd
0091FEC4  66 45 39 5D 04                  cmp word ptr [r13 + 4], r11w
0091FEC9  74 9E                           je 0x14091fe69
0091FECB  8B DF                           mov ebx, edi
0091FECD  83 E3 08                        and ebx, 8
0091FED0  EB 97                           jmp 0x14091fe69
0091FED2  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
0091FED6  48 85 C0                        test rax, rax
0091FED9  0F 84 92 FE FF FF               je 0x14091fd71
0091FEDF  48 8D 55 9F                     lea rdx, [rbp - 0x61]
0091FEE3  48 8B C8                        mov rcx, rax
0091FEE6  E8 35 05 00 00                  call 0x140920420
0091FEEB  45 33 DB                        xor r11d, r11d
0091FEEE  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0091FEF2  85 C0                           test eax, eax
0091FEF4  0F 89 89 02 00 00               jns 0x140920183
0091FEFA  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0091FEFE  48 85 C9                        test rcx, rcx
0091FF01  0F 85 94 02 00 00               jne 0x14092019b
0091FF07  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0091FF0B  48 85 C0                        test rax, rax
0091FF0E  0F 84 F1 FE FF FF               je 0x14091fe05
0091FF14  33 D2                           xor edx, edx
0091FF16  48 8B C8                        mov rcx, rax
0091FF19  E8 52 29 26 00                  call 0x140b82870
0091FF1E  E9 E2 FE FF FF                  jmp 0x14091fe05
0091FF23  49 8D 70 08                     lea rsi, [r8 + 8]
0091FF27  4D 85 ED                        test r13, r13
0091FF2A  0F 85 19 03 00 00               jne 0x140920249
0091FF30  44 0F B7 CB                     movzx r9d, bx
0091FF34  4C 8B EB                        mov r13, rbx
0091FF37  4D 85 E4                        test r12, r12
0091FF3A  0F 85 28 03 00 00               jne 0x140920268
0091FF40  4C 8B E3                        mov r12, rbx
0091FF43  48 85 C9                        test rcx, rcx
0091FF46  0F 85 DE 01 00 00               jne 0x14092012a
0091FF4C  44 0F B7 D3                     movzx r10d, bx
0091FF50  48 85 D2                        test rdx, rdx
0091FF53  0F 85 2B 03 00 00               jne 0x140920284
0091FF59  44 0F B7 DB                     movzx r11d, bx
0091FF5D  4C 8B 7D B7                     mov r15, qword ptr [rbp - 0x49]
0091FF61  4C 8B 75 BF                     mov r14, qword ptr [rbp - 0x41]
0091FF65  0F B6 16                        movzx edx, byte ptr [rsi]
0091FF68  83 FA 0E                        cmp edx, 0xe
0091FF6B  0F 86 35 03 00 00               jbe 0x1409202a6
0091FF71  8B CA                           mov ecx, edx
0091FF73  83 E9 0F                        sub ecx, 0xf
0091FF76  74 09                           je 0x14091ff81
0091FF78  83 E9 01                        sub ecx, 1
0091FF7B  0F 85 D4 01 00 00               jne 0x140920155
0091FF81  40 F6 C7 08                     test dil, 8
0091FF85  74 1E                           je 0x14091ffa5
0091FF87  4D 85 ED                        test r13, r13
0091FF8A  0F 85 38 03 00 00               jne 0x1409202c8
0091FF90  44 0F B7 5D 6F                  movzx r11d, word ptr [rbp + 0x6f]
0091FF95  83 CB 08                        or ebx, 8
0091FF98  83 E7 F7                        and edi, 0xfffffff7
0091FF9B  44 0F B7 55 47                  movzx r10d, word ptr [rbp + 0x47]
0091FFA0  44 0F B7 4D 5F                  movzx r9d, word ptr [rbp + 0x5f]
0091FFA5  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
0091FFA9  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0091FFAD  8B 4D 87                        mov ecx, dword ptr [rbp - 0x79]
0091FFB0  48 03 F0                        add rsi, rax
0091FFB3  41 0F B7 40 04                  movzx eax, word ptr [r8 + 4]
0091FFB8  FF C1                           inc ecx
0091FFBA  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
0091FFBD  3B C8                           cmp ecx, eax
0091FFBF  0F 82 A8 01 00 00               jb 0x14092016d
0091FFC5  4C 8B B5 87 00 00 00            mov r14, qword ptr [rbp + 0x87]
0091FFCC  4C 8B BD A7 00 00 00            mov r15, qword ptr [rbp + 0xa7]
0091FFD3  66 45 85 C9                     test r9w, r9w
0091FFD7  0F 85 2A 03 00 00               jne 0x140920307
0091FFDD  66 45 85 D2                     test r10w, r10w
0091FFE1  0F 85 2C 03 00 00               jne 0x140920313
0091FFE7  66 45 85 DB                     test r11w, r11w
0091FFEB  0F 85 2E 03 00 00               jne 0x14092031f
0091FFF1  45 33 DB                        xor r11d, r11d
0091FFF4  85 D2                           test edx, edx
0091FFF6  0F 84 F8 FD FF FF               je 0x14091fdf4
0091FFFC  83 E7 10                        and edi, 0x10
0091FFFF  E9 9F 24 20 00                  jmp 0x140b224a3
00920004  66 85 C0                        test ax, ax
00920007  0F 89 3F 01 00 00               jns 0x14092014c
0092000D  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00920010  85 C0                           test eax, eax
00920012  0F 84 A4 FE FF FF               je 0x14091febc
00920018  48 8D 0C 02                     lea rcx, [rdx + rax]
0092001C  E9 AC FD FF FF                  jmp 0x14091fdcd
00920021  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
00920025  48 85 C0                        test rax, rax
00920028  0F 84 4C 01 00 00               je 0x14092017a
0092002E  48 8D 55 97                     lea rdx, [rbp - 0x69]
00920032  48 8B C8                        mov rcx, rax
00920035  E8 AE 5D FD FF                  call 0x1408f5de8
0092003A  45 33 DB                        xor r11d, r11d
0092003D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00920041  85 C0                           test eax, eax
00920043  0F 88 B1 FE FF FF               js 0x14091fefa
00920049  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0092004D  45 8B E3                        mov r12d, r11d
00920050  48 85 C9                        test rcx, rcx
00920053  4C 0F 45 E1                     cmovne r12, rcx
00920057  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
0092005B  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
0092005F  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00920064  48 8B 80 98 00 00 00            mov rax, qword ptr [rax + 0x98]
0092006B  48 8B 38                        mov rdi, qword ptr [rax]
0092006E  F6 C3 08                        test bl, 8
00920071  74 39                           je 0x1409200ac
00920073  48 8B 85 8F 00 00 00            mov rax, qword ptr [rbp + 0x8f]
0092007A  48 8D 15 27 13 6E FF            lea rdx, [rip - 0x91ecd9]
00920081  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00920086  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0092008A  C7 44 24 38 08 00 00 00         mov dword ptr [rsp + 0x38], 8
00920092  4D 8B CC                        mov r9, r12
00920095  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092009A  4D 8B C5                        mov r8, r13
0092009D  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
009200A2  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009200A7  E8 3C E3 FF FF                  call 0x14091e3e8
009200AC  F6 C3 20                        test bl, 0x20
009200AF  0F 85 DC 02 00 00               jne 0x140920391
009200B5  F6 C3 40                        test bl, 0x40
009200B8  0F 85 11 03 00 00               jne 0x1409203cf
009200BE  83 E3 97                        and ebx, 0xffffff97
009200C1  0F 84 33 FE FF FF               je 0x14091fefa
009200C7  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
009200CC  48 8D 15 D5 12 6E FF            lea rdx, [rip - 0x91ed2b]
009200D3  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
009200D7  48 8D 4D CF                     lea rcx, [rbp - 0x31]
009200DB  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
009200E0  4D 8B CC                        mov r9, r12
009200E3  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
009200E8  4D 8B C5                        mov r8, r13
009200EB  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009200F0  E8 F3 E2 FF FF                  call 0x14091e3e8
009200F5  E9 00 FE FF FF                  jmp 0x14091fefa
009200FA  48 39 9D 97 00 00 00            cmp qword ptr [rbp + 0x97], rbx
00920101  0F 84 1C FC FF FF               je 0x14091fd23
00920107  8B 7D 7F                        mov edi, dword ptr [rbp + 0x7f]
0092010A  83 E7 20                        and edi, 0x20
0092010D  E9 11 FC FF FF                  jmp 0x14091fd23
00920112  4D 8B 47 18                     mov r8, qword ptr [r15 + 0x18]
00920116  E9 81 FC FF FF                  jmp 0x14091fd9c
0092011B  B9 7C 00 00 C0                  mov ecx, 0xc000007c
00920120  E8 FB EC F4 FF                  call 0x14086ee20
00920125  E9 F0 FC FF FF                  jmp 0x14091fe1a
0092012A  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
0092012E  66 85 C0                        test ax, ax
00920131  0F 84 15 FE FF FF               je 0x14091ff4c
00920137  48 83 C1 08                     add rcx, 8
0092013B  66 89 45 47                     mov word ptr [rbp + 0x47], ax
0092013F  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00920143  44 0F B7 D0                     movzx r10d, ax
00920147  E9 04 FE FF FF                  jmp 0x14091ff50
0092014C  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
00920150  E9 78 FC FF FF                  jmp 0x14091fdcd
00920155  83 E9 01                        sub ecx, 1
00920158  0F 85 BB 21 20 00               jne 0x140b22319
0092015E  40 F6 C7 10                     test dil, 0x10
00920162  0F 84 3D FE FF FF               je 0x14091ffa5
00920168  E9 D0 22 20 00                  jmp 0x140b2243d
0092016D  85 FF                           test edi, edi
0092016F  0F 85 F0 FD FF FF               jne 0x14091ff65
00920175  E9 4B FE FF FF                  jmp 0x14091ffc5
0092017A  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
0092017E  E9 D4 FE FF FF                  jmp 0x140920057
00920183  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00920187  48 8B C3                        mov rax, rbx
0092018A  48 85 C9                        test rcx, rcx
0092018D  48 0F 45 C1                     cmovne rax, rcx
00920191  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00920196  E9 D6 FB FF FF                  jmp 0x14091fd71
0092019B  33 D2                           xor edx, edx
0092019D  E8 CE 26 26 00                  call 0x140b82870
009201A2  E9 60 FD FF FF                  jmp 0x14091ff07
009201A7  48 39 9D 9F 00 00 00            cmp qword ptr [rbp + 0x9f], rbx
009201AE  0F 84 A5 FB FF FF               je 0x14091fd59
009201B4  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
009201B7  83 E0 40                        and eax, 0x40
009201BA  0B F8                           or edi, eax
009201BC  E9 98 FB FF FF                  jmp 0x14091fd59
009201C1  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
009201C5  A8 10                           test al, 0x10
009201C7  0F 84 D3 20 20 00               je 0x140b222a0
009201CD  66 85 C0                        test ax, ax
009201D0  0F 89 CF 20 20 00               jns 0x140b222a5
009201D6  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
009201D9  85 C0                           test eax, eax
009201DB  0F 84 BF 20 20 00               je 0x140b222a0
009201E1  48 8D 0C 06                     lea rcx, [rsi + rax]
009201E5  E9 BF 20 20 00                  jmp 0x140b222a9
009201EA  4C 8B 6E 18                     mov r13, qword ptr [rsi + 0x18]
009201EE  E9 B7 FB FF FF                  jmp 0x14091fdaa
009201F3  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
009201F8  A8 10                           test al, 0x10
009201FA  0F 84 F7 20 20 00               je 0x140b222f7
00920200  66 85 C0                        test ax, ax
00920203  0F 89 F6 20 20 00               jns 0x140b222ff
00920209  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0092020D  85 C0                           test eax, eax
0092020F  0F 84 E2 20 20 00               je 0x140b222f7
00920215  4D 8D 24 06                     lea r12, [r14 + rax]
00920219  E9 9C FB FF FF                  jmp 0x14091fdba
0092021E  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
00920223  A8 10                           test al, 0x10
00920225  0F 84 DD 20 20 00               je 0x140b22308
0092022B  66 85 C0                        test ax, ax
0092022E  0F 89 DC 20 20 00               jns 0x140b22310
00920234  41 8B 41 0C                     mov eax, dword ptr [r9 + 0xc]
00920238  85 C0                           test eax, eax
0092023A  0F 84 C8 20 20 00               je 0x140b22308
00920240  49 8D 14 01                     lea rdx, [r9 + rax]
00920244  E9 97 FB FF FF                  jmp 0x14091fde0
00920249  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
0092024E  66 85 C0                        test ax, ax
00920251  0F 84 D9 FC FF FF               je 0x14091ff30
00920257  49 83 C5 08                     add r13, 8
0092025B  66 89 45 5F                     mov word ptr [rbp + 0x5f], ax
0092025F  44 0F B7 C8                     movzx r9d, ax
00920263  E9 CF FC FF FF                  jmp 0x14091ff37
00920268  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
0092026E  66 85 C0                        test ax, ax
00920271  0F 84 C9 FC FF FF               je 0x14091ff40
00920277  49 83 C4 08                     add r12, 8
0092027B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0092027F  E9 BF FC FF FF                  jmp 0x14091ff43
00920284  0F B7 42 04                     movzx eax, word ptr [rdx + 4]
00920288  66 85 C0                        test ax, ax
0092028B  0F 84 C8 FC FF FF               je 0x14091ff59
00920291  48 83 C2 08                     add rdx, 8
00920295  66 89 45 6F                     mov word ptr [rbp + 0x6f], ax
00920299  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
0092029D  44 0F B7 D8                     movzx r11d, ax
009202A1  E9 B7 FC FF FF                  jmp 0x14091ff5d
009202A6  0F 84 D5 FC FF FF               je 0x14091ff81
009202AC  8B CA                           mov ecx, edx
009202AE  83 E9 02                        sub ecx, 2
009202B1  0F 84 CA FC FF FF               je 0x14091ff81
009202B7  83 E9 01                        sub ecx, 1
009202BA  0F 84 C1 FC FF FF               je 0x14091ff81
009202C0  83 E9 04                        sub ecx, 4
009202C3  E9 B9 FC FF FF                  jmp 0x14091ff81
009202C8  41 38 55 00                     cmp byte ptr [r13], dl
009202CC  0F 85 BE FC FF FF               jne 0x14091ff90
009202D2  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
009202D7  66 39 46 02                     cmp word ptr [rsi + 2], ax
009202DB  0F 85 AF FC FF FF               jne 0x14091ff90
009202E1  44 8B C0                        mov r8d, eax
009202E4  49 8B D5                        mov rdx, r13
009202E7  48 8B CE                        mov rcx, rsi
009202EA  E8 81 A3 D9 FF                  call 0x1406ba670
009202EF  41 0F B7 4D 02                  movzx ecx, word ptr [r13 + 2]
009202F4  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
009202F9  48 3B C1                        cmp rax, rcx
009202FC  0F 85 8E FC FF FF               jne 0x14091ff90
00920302  E9 98 20 20 00                  jmp 0x140b2239f
00920307  8B C7                           mov eax, edi
00920309  83 E0 08                        and eax, 8
0092030C  0B D8                           or ebx, eax
0092030E  E9 CA FC FF FF                  jmp 0x14091ffdd
00920313  8B C7                           mov eax, edi
00920315  83 E0 20                        and eax, 0x20
00920318  0B D8                           or ebx, eax
0092031A  E9 C8 FC FF FF                  jmp 0x14091ffe7
0092031F  8B C7                           mov eax, edi
00920321  83 E0 40                        and eax, 0x40
00920324  0B D8                           or ebx, eax
00920326  E9 C6 FC FF FF                  jmp 0x14091fff1
0092032B  66 45 39 5C 24 04               cmp word ptr [r12 + 4], r11w
00920331  0F 84 3B FB FF FF               je 0x14091fe72
00920337  8B C7                           mov eax, edi
00920339  83 E0 10                        and eax, 0x10
0092033C  0B D8                           or ebx, eax
0092033E  E9 2F FB FF FF                  jmp 0x14091fe72
00920343  66 44 39 59 04                  cmp word ptr [rcx + 4], r11w
00920348  0F 84 2D FB FF FF               je 0x14091fe7b
0092034E  8B C7                           mov eax, edi
00920350  83 E0 20                        and eax, 0x20
00920353  0B D8                           or ebx, eax
00920355  E9 21 FB FF FF                  jmp 0x14091fe7b
0092035A  8B 7C 24 60                     mov edi, dword ptr [rsp + 0x60]
0092035E  0F BA E7 13                     bt edi, 0x13
00920362  0F 83 CA 21 20 00               jae 0x140b22532
00920368  F6 45 7F 01                     test byte ptr [rbp + 0x7f], 1
0092036C  0F 84 6F 21 20 00               je 0x140b224e1
00920372  66 45 39 5F 02                  cmp word ptr [r15 + 2], r11w
00920377  0F 8D 33 21 20 00               jge 0x140b224b0
0092037D  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
00920381  85 C0                           test eax, eax
00920383  0F 85 21 21 20 00               jne 0x140b224aa
00920389  49 8B D3                        mov rdx, r11
0092038C  E9 23 21 20 00                  jmp 0x140b224b4
00920391  48 8B 85 97 00 00 00            mov rax, qword ptr [rbp + 0x97]
00920398  48 8D 15 09 10 6E FF            lea rdx, [rip - 0x91eff7]
0092039F  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
009203A4  48 8D 4D CF                     lea rcx, [rbp - 0x31]
009203A8  C7 44 24 38 20 00 00 00         mov dword ptr [rsp + 0x38], 0x20
009203B0  4D 8B CC                        mov r9, r12
009203B3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009203B8  4D 8B C5                        mov r8, r13
009203BB  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
009203C0  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009203C5  E8 1E E0 FF FF                  call 0x14091e3e8
009203CA  E9 E6 FC FF FF                  jmp 0x1409200b5
009203CF  48 8B 85 9F 00 00 00            mov rax, qword ptr [rbp + 0x9f]
009203D6  48 8D 15 CB 0F 6E FF            lea rdx, [rip - 0x91f035]
009203DD  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
009203E2  48 8D 4D CF                     lea rcx, [rbp - 0x31]
009203E6  C7 44 24 38 40 00 00 00         mov dword ptr [rsp + 0x38], 0x40
009203EE  4D 8B CC                        mov r9, r12
009203F1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009203F6  4D 8B C5                        mov r8, r13
009203F9  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
009203FE  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00920403  E8 E0 DF FF FF                  call 0x14091e3e8
00920408  E9 B1 FC FF FF                  jmp 0x1409200be
0092040D  8B C8                           mov ecx, eax
0092040F  E8 0C EA F4 FF                  call 0x14086ee20
00920414  E9 F8 F9 FF FF                  jmp 0x14091fe11
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeSecurityDescriptorChangedAuditAlarm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (240);
    v_r14 = 0;
    v_stack_mC8 = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 63 - 105) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 33) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 63 - 97) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 57) = 0;
    v_stack_mC0 = 0;
    v_stack_mC4 = 0;
    *(unsigned int *)(v_rsp - 63 - 121) = 0;
    v_stack_mD8 = 0;
    *(unsigned __int16 *)(v_rsp - 63 + 95) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 65) = 0;
    *(unsigned __int16 *)(v_rsp - 63 + 71) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 73) = 0;
    *(unsigned __int16 *)(v_rsp - 63 + 111) = 0;
    result = SeCaptureSubjectContext(v_rsp - 63 - 49, a2, a3, a4);
    a1 = *(unsigned __int64 *)(v_rsp - 63 - 33);
    if (*(unsigned __int64 *)(v_rsp - 63 - 49) != 0) { a1 = *(unsigned __int64 *)(v_rsp - 63 - 49); }
    *(unsigned __int64 *)(v_rsp - 63 - 113) = a1;
    if (a1 == 0) goto loc_0092011B;
    a3 = 0;
    result = SepAdtAuditThisEventWithContext(142, 1, a3, v_rsp - 63 - 49);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_009200FA;
loc_0091FD23:
    if (condition_is_above_or_equal) goto loc_0091FD59;
    a3 = 0;
    result = SepAdtAuditThisEventWithContext(140, 1, a3, v_rsp - 63 - 49);
    v_r11 = 0;
    v_rdi = 0;
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(v_rsp - 63 + 127);
        result = (unsigned int)((result) & (8));
        v_rdi = (unsigned int)((0) | ((unsigned int)(result)));
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_009201A7;
loc_0091FD59:
    if (0 == 0) goto loc_0091FED2;
    if ((*(unsigned __int16 *)(a3)) == 0) goto loc_0091FED2;
    v_stack_mC0 = 0;
loc_0091FD71:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 + 119))) & (0xFEFFFFFFULL));
    if (condition_is_not_equal) goto loc_009201C1;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 2))) & (16)) != 0) goto loc_0091FE36;
loc_0091FD99:
loc_0091FD9C:
    v_stack_mD0 = 0;
    if (*(unsigned __int64 *)(v_rsp - 63 + 143) != 0) goto loc_0091FE54;
loc_0091FDAA:
    if (*(unsigned __int64 *)(v_rsp - 63 + 135) != 0) goto loc_009201F3;
loc_0091FDBA:
    if (*(unsigned __int64 *)(v_rsp - 63 + 151) != 0) goto loc_0091FEB0;
loc_0091FDCD:
    if (*(unsigned __int64 *)(v_rsp - 63 + 159) != 0) goto loc_0092021E;
loc_0091FDE0:
    if (0 == 0) goto loc_0091FE64;
    if ((*(unsigned __int16 *)(0 + 4)) == 0) goto loc_0091FE64;
    if ((unsigned int)(v_rdi) != 0) goto loc_0091FF23;
loc_0091FDF4:
    if (*(unsigned __int64 *)(v_rsp - 63 + 135) != 0) goto loc_0092035A;
    if (0 != 0) goto loc_00920021;
loc_0091FE05:
    if (sign_flag) goto loc_0092040D;
loc_0091FE11:
    result = SeReleaseSubjectContext(v_rsp - 63 - 49, 0, 0, *(unsigned __int64 *)(v_rsp - 63 + 159));
loc_0091FE1A:
    v_rsp = (v_rsp) + (240);
    return result;
loc_0091FE36:
    if (!sign_flag) goto loc_00920112;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12))) == 0) goto loc_0091FD99;
    goto loc_0091FD9C;
loc_0091FE54:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 143) + 2))) & (16)) != 0) goto loc_0091FE97;
loc_0091FE5C:
    goto loc_0091FDAA;
loc_0091FE64:
    if (0 != 0) goto loc_0091FEC4;
loc_0091FE69:
    if (0 != 0) goto loc_0092032B;
loc_0091FE72:
    if (v_rsp - 63 - 49 != 0) goto loc_00920343;
loc_0091FE7B:
    if (0 == 0) goto loc_0091FDF4;
    if ((*(unsigned __int16 *)(0 + 4)) == 0) goto loc_0091FDF4;
    v_rdi = (unsigned int)((v_rdi) & (64));
loc_0091FE97:
    if (!sign_flag) goto loc_009201EA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 143) + 12))) == 0) goto loc_0091FE5C;
    goto loc_0091FDAA;
loc_0091FEB0:
    if ((((unsigned __int8)(*(unsigned __int16 *)(0 + 2))) & (16)) != 0) goto loc_00920004;
loc_0091FEBC:
    goto loc_0091FDCD;
loc_0091FEC4:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 143) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 143) + 12)) * 1 + 4)) == 0) goto loc_0091FE69;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (8));
    goto loc_0091FE69;
loc_0091FED2:
    if (*(unsigned __int64 *)(v_rsp - 63 + 79) == 0) goto loc_0091FD71;
    result = SepQueryTypeString(*(unsigned __int64 *)(v_rsp - 63 + 79), v_rsp - 63 - 97, *(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1, *(unsigned __int64 *)(v_rsp - 63 + 159));
    v_r11 = 0;
    v_stack_p64 = (unsigned int)(result);
    if (!sign_flag) goto loc_00920183;
loc_0091FEFA:
    if (*(unsigned __int64 *)(v_rsp - 63 - 105) != 0) goto loc_0092019B;
loc_0091FF07:
    if (*(unsigned __int64 *)(v_rsp - 63 - 97) == 0) goto loc_0091FE05;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 63 - 97), a2, *(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1, *(unsigned __int64 *)(v_rsp - 63 + 159));
    goto loc_0091FE05;
loc_0091FF23:
    if (*(unsigned __int64 *)(v_rsp - 63 + 143) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 143) + 12)) * 1 != 0) goto loc_00920249;
loc_0091FF30:
loc_0091FF37:
    if (0 != 0) goto loc_00920268;
loc_0091FF40:
loc_0091FF43:
    if (*(unsigned __int64 *)(v_rsp - 63 - 97) != 0) goto loc_0092012A;
loc_0091FF4C:
loc_0091FF50:
    if (0 != 0) goto loc_00920284;
loc_0091FF59:
loc_0091FF5D:
loc_0091FF65:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1 + 8))) <= 14) goto loc_009202A6;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1 + 8)))) - (15));
    if (condition_is_equal) goto loc_0091FF81;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00920155;
loc_0091FF81:
    if ((((unsigned __int8)(v_rdi)) & (8)) == 0) goto loc_0091FFA5;
    if (v_rbx != 0) goto loc_009202C8;
loc_0091FF90:
    v_rbx = (unsigned int)((v_rbx) | (8));
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFF7ULL));
loc_0091FFA5:
    v_rsi = (*(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1 + 8) + (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1 + 8 + 2));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 - 121))) + 1);
    *(unsigned int *)(v_rsp - 63 - 121) = (unsigned int)(a1);
    if (((unsigned int)(a1)) < ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1 + 4)))) goto loc_0092016D;
loc_0091FFC5:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 63 + 95)) != 0) goto loc_00920307;
loc_0091FFDD:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 63 + 71)) != 0) goto loc_00920313;
loc_0091FFE7:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 63 + 111)) != 0) goto loc_0092031F;
loc_0091FFF1:
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(v_stack_p50)) == 0) goto loc_0091FDF4;
    v_rdi = (unsigned int)((v_rdi) & (16));
loc_00920004:
    if (!sign_flag) goto loc_0092014C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p50) + 12))) == 0) goto loc_0091FEBC;
    goto loc_0091FDCD;
loc_00920021:
    if (*(unsigned __int64 *)(v_rsp - 63 + 79) == 0) goto loc_0092017A;
    result = SepQueryNameString(*(unsigned __int64 *)(v_rsp - 63 + 79), v_rsp - 63 - 105, *(unsigned __int64 *)(v_rsp - 63 + 167) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 12)) * 1, *(unsigned __int16 *)(v_rsp - 63 + 95));
    v_r11 = 0;
    v_stack_p64 = (unsigned int)(result);
    if (sign_flag) goto loc_0091FEFA;
    v_r12 = 0;
    if (*(unsigned __int64 *)(v_rsp - 63 - 105) != 0) { v_r12 = *(unsigned __int64 *)(v_rsp - 63 - 105); }
loc_00920057:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 113) + 152);
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) {
        result = *(unsigned __int64 *)(v_rsp - 63 + 143);
        a2 = v_rip - 9563353;
        v_stack_p40 = *(unsigned __int64 *)(v_rsp - 63 + 167);
        a1 = v_rsp - 63 - 49;
        v_stack_p38 = 8;
        a4 = v_r12;
        v_stack_p30 = result;
        a3 = v_stack_p68;
        v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 113) + 152));
        v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
        result = SepAdtSecurityDescriptorChangedAuditAlarm(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_00920391;
loc_009200B5:
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_009203CF;
loc_009200BE:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFF97ULL));
    if (condition_is_equal) goto loc_0091FEFA;
    v_stack_p40 = *(unsigned __int64 *)(v_rsp - 63 + 167);
    v_stack_p38 = (unsigned int)(v_rbx);
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 63 + 135);
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 113) + 152));
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
    result = SepAdtSecurityDescriptorChangedAuditAlarm(v_rsp - 63 - 49, v_rip - 9563435, v_stack_p68, v_r12);
    goto loc_0091FEFA;
loc_009200FA:
    if ((*(unsigned __int64 *)(v_rsp - 63 + 151)) == v_rbx) goto loc_0091FD23;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))) & (32));
    goto loc_0091FD23;
loc_00920112:
    goto loc_0091FD9C;
loc_0092011B:
    result = SepAuditFailed((unsigned int)(0xC000007CULL), v_rip - 9563435, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 24), v_r12);
    goto loc_0091FE1A;
loc_0092012A:
    if ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC000007CULL) + 4)) == 0) goto loc_0091FF4C;
    a1 = ((unsigned int)(0xC000007CULL)) + (8);
    *(unsigned __int16 *)(v_rsp - 63 + 71) = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC000007CULL) + 4));
    *(unsigned __int64 *)(v_rsp - 63 - 65) = a1;
    goto loc_0091FF50;
loc_0092014C:
    goto loc_0091FDCD;
loc_00920155:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip - 9563435 + 24)) - (1));
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_0091FFA5;
loc_0092016D:
    if ((unsigned int)(v_rdi) != 0) goto loc_0091FF65;
    goto loc_0091FFC5;
loc_0092017A:
    goto loc_00920057;
loc_00920183:
    result = v_rbx;
    if (*(unsigned __int64 *)(v_rsp - 63 - 97) != 0) { result = *(unsigned __int64 *)(v_rsp - 63 - 97); }
    v_stack_p68 = result;
    goto loc_0091FD71;
loc_0092019B:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 63 - 97), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 167) + 24), v_r12);
    goto loc_0091FF07;
loc_009201A7:
    if ((*(unsigned __int64 *)(v_rsp - 63 + 159)) == v_rbx) goto loc_0091FD59;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))) & (64));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    goto loc_0091FD59;
loc_009201C1:
loc_009201EA:
    goto loc_0091FDAA;
loc_009201F3:
    goto loc_0091FDBA;
loc_0092021E:
    goto loc_0091FDE0;
loc_00920249:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 24) + 4)) == 0) goto loc_0091FF30;
    v_r13 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 24)) + (8);
    *(unsigned __int16 *)(v_rsp - 63 + 95) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 24) + 4));
    goto loc_0091FF37;
loc_00920268:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 135) + 12)) * 1 + 4)) == 0) goto loc_0091FF40;
    v_r12 = (*(unsigned __int64 *)(v_rsp - 63 + 135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 135) + 12)) * 1) + (8);
    v_stack_p50 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 135) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 135) + 12)) * 1 + 4));
    goto loc_0091FF43;
loc_00920284:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r12 + (unsigned int)(*(unsigned int *)(v_r12 + 12)) * 1 + 4)) == 0) goto loc_0091FF59;
    a2 = (v_r12 + (unsigned int)(*(unsigned int *)(v_r12 + 12)) * 1) + (8);
    *(unsigned __int16 *)(v_rsp - 63 + 111) = (unsigned __int16)(*(unsigned __int16 *)(v_r12 + (unsigned int)(*(unsigned int *)(v_r12 + 12)) * 1 + 4));
    *(unsigned __int64 *)(v_rsp - 63 - 73) = a2;
    goto loc_0091FF5D;
loc_009202A6:
    if (condition_is_equal) goto loc_0091FF81;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - (2));
    if (condition_is_equal) goto loc_0091FF81;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0091FF81;
    a1 = (unsigned int)((a1) - (4));
    goto loc_0091FF81;
loc_009202C8:
    if ((*(unsigned __int8 *)(v_r13)) != ((unsigned __int8)(a2))) goto loc_0091FF90;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 2)) != ((unsigned __int16)(*(unsigned __int16 *)(v_r13 + 2)))) goto loc_0091FF90;
    result = RtlCompareMemory(*(unsigned __int64 *)(v_rsp - 63 + 103), v_r13, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 2))), (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 24) + 4)));
    if (result != (*(unsigned __int16 *)(v_r13 + 2))) goto loc_0091FF90;
loc_00920307:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (8));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    goto loc_0091FFDD;
loc_00920313:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (32));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    goto loc_0091FFE7;
loc_0092031F:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (64));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    goto loc_0091FFF1;
loc_0092032B:
    if ((*(unsigned __int16 *)(v_r12 + 4)) == ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_r12 + (unsigned int)(*(unsigned int *)(v_r12 + 12)) * 1 + 4))))) goto loc_0091FE72;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (16));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    goto loc_0091FE72;
loc_00920343:
    if ((*(unsigned __int16 *)(*(unsigned __int16 *)(v_r13 + 2) + 4)) == ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_r12 + (unsigned int)(*(unsigned int *)(v_r12 + 12)) * 1 + 4))))) goto loc_0091FE7B;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (32));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    goto loc_0091FE7B;
loc_0092035A:
loc_00920391:
    v_stack_p40 = *(unsigned __int64 *)(v_rsp - 63 + 167);
    v_stack_p38 = 32;
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 63 + 151);
    v_stack_p28 = (unsigned int)(v_stack_p60);
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
    result = SepAdtSecurityDescriptorChangedAuditAlarm(v_rsp - 63 - 49, v_rip - 9564151, v_r13, v_r12);
    goto loc_009200B5;
loc_009203CF:
    v_stack_p40 = *(unsigned __int64 *)(v_rsp - 63 + 167);
    v_stack_p38 = 64;
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 63 + 159);
    v_stack_p28 = (unsigned int)(v_stack_p60);
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
    result = SepAdtSecurityDescriptorChangedAuditAlarm(v_rsp - 63 - 49, v_rip - 9564213, v_r13, v_r12);
    goto loc_009200BE;
loc_0092040D:
    result = SepAuditFailed((unsigned int)((unsigned int)(result)), v_rip - 9564213, v_r13, v_r12);
    goto loc_0091FE11;
}
```

## 5. (Beta) C Style

```c
int64_t SeSecurityDescriptorChangedAuditAlarm(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (240);
    local_r14 = 0;
    v_stack_mC8 = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3F - 0x69) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x39) = 0;
    v_stack_mC0 = 0;
    v_stack_mC4 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x79) = 0;
    v_stack_mD8 = 0;
    *(uint16_t *)(local_rsp - 0x3F + 0x5F) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = 0;
    *(uint16_t *)(local_rsp - 0x3F + 0x47) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = 0;
    *(uint16_t *)(local_rsp - 0x3F + 0x6F) = 0;
    result = SeCaptureSubjectContext(local_rsp - 63 - 49, Arg2, Arg3, Arg4);
    Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x21);
    if (*(uint64_t *)(local_rsp - 0x3F - 0x31) != 0) { Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x31); }
    *(uint64_t *)(local_rsp - 0x3F - 0x71) = Arg1;
    if (Arg1 == 0) goto loc_0092011B;
    Arg3 = 0;
    result = SepAdtAuditThisEventWithContext(142, 1, Arg3, local_rsp - 63 - 49);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_009200FA;
loc_0091FD23:
    if (condition_is_above_or_equal) goto loc_0091FD59;
    Arg3 = 0;
    result = SepAdtAuditThisEventWithContext(140, 1, Arg3, local_rsp - 63 - 49);
    local_r11 = 0;
    local_rdi = 0;
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(local_rsp - 0x3F + 0x7F);
        result = (uint32_t)((result) & (8));
        local_rdi = (uint32_t)((0) | ((uint32_t)(result)));
    }
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_009201A7;
loc_0091FD59:
    if (0 == 0) goto loc_0091FED2;
    if ((*(uint16_t *)(Arg3)) == 0) goto loc_0091FED2;
    v_stack_mC0 = 0;
loc_0091FD71:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x77))) & (0xFEFFFFFFULL));
    if (condition_is_not_equal) goto loc_009201C1;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0x2))) & (16)) != 0) goto loc_0091FE36;
loc_0091FD99:
loc_0091FD9C:
    v_stack_mD0 = 0;
    if (*(uint64_t *)(local_rsp - 0x3F + 0x8F) != 0) goto loc_0091FE54;
loc_0091FDAA:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x87) != 0) goto loc_009201F3;
loc_0091FDBA:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x97) != 0) goto loc_0091FEB0;
loc_0091FDCD:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x9F) != 0) goto loc_0092021E;
loc_0091FDE0:
    if (0 == 0) goto loc_0091FE64;
    if ((*(uint16_t *)(0 + 0x4)) == 0) goto loc_0091FE64;
    if ((uint32_t)(local_rdi) != 0) goto loc_0091FF23;
loc_0091FDF4:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x87) != 0) goto loc_0092035A;
    if (0 != 0) goto loc_00920021;
loc_0091FE05:
    if (sign_flag) goto loc_0092040D;
loc_0091FE11:
    result = SeReleaseSubjectContext(local_rsp - 63 - 49, 0, 0, *(uint64_t *)(local_rsp - 0x3F + 0x9F));
loc_0091FE1A:
    local_rsp = (local_rsp) + (240);
    return result;
loc_0091FE36:
    if (!sign_flag) goto loc_00920112;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC))) == 0) goto loc_0091FD99;
    goto loc_0091FD9C;
loc_0091FE54:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F) + 0x2))) & (16)) != 0) goto loc_0091FE97;
loc_0091FE5C:
    goto loc_0091FDAA;
loc_0091FE64:
    if (0 != 0) goto loc_0091FEC4;
loc_0091FE69:
    if (0 != 0) goto loc_0092032B;
loc_0091FE72:
    if (local_rsp - 63 - 49 != 0) goto loc_00920343;
loc_0091FE7B:
    if (0 == 0) goto loc_0091FDF4;
    if ((*(uint16_t *)(0 + 0x4)) == 0) goto loc_0091FDF4;
    local_rdi = (uint32_t)((local_rdi) & (64));
loc_0091FE97:
    if (!sign_flag) goto loc_009201EA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F) + 0xC))) == 0) goto loc_0091FE5C;
    goto loc_0091FDAA;
loc_0091FEB0:
    if ((((uint8_t)(*(uint16_t *)(0 + 0x2))) & (16)) != 0) goto loc_00920004;
loc_0091FEBC:
    goto loc_0091FDCD;
loc_0091FEC4:
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F) + 0xC)) * 1 + 0x4)) == 0) goto loc_0091FE69;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (8));
    goto loc_0091FE69;
loc_0091FED2:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x4F) == 0) goto loc_0091FD71;
    result = SepQueryTypeString(*(uint64_t *)(local_rsp - 0x3F + 0x4F), local_rsp - 63 - 97, *(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1, *(uint64_t *)(local_rsp - 0x3F + 0x9F));
    local_r11 = 0;
    v_stack_p64 = (uint32_t)(result);
    if (!sign_flag) goto loc_00920183;
loc_0091FEFA:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x69) != 0) goto loc_0092019B;
loc_0091FF07:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x61) == 0) goto loc_0091FE05;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x3F - 0x61), Arg2, *(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1, *(uint64_t *)(local_rsp - 0x3F + 0x9F));
    goto loc_0091FE05;
loc_0091FF23:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x8F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F) + 0xC)) * 1 != 0) goto loc_00920249;
loc_0091FF30:
loc_0091FF37:
    if (0 != 0) goto loc_00920268;
loc_0091FF40:
loc_0091FF43:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x61) != 0) goto loc_0092012A;
loc_0091FF4C:
loc_0091FF50:
    if (0 != 0) goto loc_00920284;
loc_0091FF59:
loc_0091FF5D:
loc_0091FF65:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1 + 0x8))) <= 14) goto loc_009202A6;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1 + 0x8)))) - (15));
    if (condition_is_equal) goto loc_0091FF81;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00920155;
loc_0091FF81:
    if ((((uint8_t)(local_rdi)) & (8)) == 0) goto loc_0091FFA5;
    if (local_rbx != 0) goto loc_009202C8;
loc_0091FF90:
    local_rbx = (uint32_t)((local_rbx) | (8));
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFF7ULL));
loc_0091FFA5:
    local_rsi = (*(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1 + 8) + (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1 + 0x8 + 0x2));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x79))) + 1);
    *(uint32_t *)(local_rsp - 0x3F - 0x79) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1 + 0x4)))) goto loc_0092016D;
loc_0091FFC5:
    if ((uint16_t)(*(uint16_t *)(local_rsp - 0x3F + 0x5F)) != 0) goto loc_00920307;
loc_0091FFDD:
    if ((uint16_t)(*(uint16_t *)(local_rsp - 0x3F + 0x47)) != 0) goto loc_00920313;
loc_0091FFE7:
    if ((uint16_t)(*(uint16_t *)(local_rsp - 0x3F + 0x6F)) != 0) goto loc_0092031F;
loc_0091FFF1:
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(v_stack_p50)) == 0) goto loc_0091FDF4;
    local_rdi = (uint32_t)((local_rdi) & (16));
loc_00920004:
    if (!sign_flag) goto loc_0092014C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p50) + 0xC))) == 0) goto loc_0091FEBC;
    goto loc_0091FDCD;
loc_00920021:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x4F) == 0) goto loc_0092017A;
    result = SepQueryNameString(*(uint64_t *)(local_rsp - 0x3F + 0x4F), local_rsp - 63 - 105, *(uint64_t *)(local_rsp - 0x3F + 0xA7) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0xC)) * 1, *(uint16_t *)(local_rsp - 0x3F + 0x5F));
    local_r11 = 0;
    v_stack_p64 = (uint32_t)(result);
    if (sign_flag) goto loc_0091FEFA;
    local_r12 = 0;
    if (*(uint64_t *)(local_rsp - 0x3F - 0x69) != 0) { local_r12 = *(uint64_t *)(local_rsp - 0x3F - 0x69); }
loc_00920057:
    result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x71) + 0x98);
    if ((((uint8_t)(local_rbx)) & (8)) != 0) {
        result = *(uint64_t *)(local_rsp - 0x3F + 0x8F);
        Arg2 = v_rip - 9563353;
        v_stack_p40 = *(uint64_t *)(local_rsp - 0x3F + 0xA7);
        Arg1 = local_rsp - 63 - 49;
        v_stack_p38 = 8;
        Arg4 = local_r12;
        v_stack_p30 = result;
        Arg3 = v_stack_p68;
        v_stack_p28 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x71) + 0x98));
        v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
        result = SepAdtSecurityDescriptorChangedAuditAlarm(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_00920391;
loc_009200B5:
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_009203CF;
loc_009200BE:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFF97ULL));
    if (condition_is_equal) goto loc_0091FEFA;
    v_stack_p40 = *(uint64_t *)(local_rsp - 0x3F + 0xA7);
    v_stack_p38 = (uint32_t)(local_rbx);
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x3F + 0x87);
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x71) + 0x98));
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    result = SepAdtSecurityDescriptorChangedAuditAlarm(local_rsp - 63 - 49, v_rip - 9563435, v_stack_p68, local_r12);
    goto loc_0091FEFA;
loc_009200FA:
    if ((*(uint64_t *)(local_rsp - 0x3F + 0x97)) == local_rbx) goto loc_0091FD23;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))) & (32));
    goto loc_0091FD23;
loc_00920112:
    goto loc_0091FD9C;
loc_0092011B:
    result = SepAuditFailed((uint32_t)(0xC000007CULL), v_rip - 9563435, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0x18), local_r12);
    goto loc_0091FE1A;
loc_0092012A:
    if ((uint16_t)(*(uint16_t *)((uint32_t)(0xC000007CULL) + 0x4)) == 0) goto loc_0091FF4C;
    Arg1 = ((uint32_t)(0xC000007CULL)) + (8);
    *(uint16_t *)(local_rsp - 0x3F + 0x47) = (uint16_t)(*(uint16_t *)((uint32_t)(0xC000007CULL) + 0x4));
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = Arg1;
    goto loc_0091FF50;
loc_0092014C:
    goto loc_0091FDCD;
loc_00920155:
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip - 0x91ED2B + 0x18)) - (1));
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_0091FFA5;
loc_0092016D:
    if ((uint32_t)(local_rdi) != 0) goto loc_0091FF65;
    goto loc_0091FFC5;
loc_0092017A:
    goto loc_00920057;
loc_00920183:
    result = local_rbx;
    if (*(uint64_t *)(local_rsp - 0x3F - 0x61) != 0) { result = *(uint64_t *)(local_rsp - 0x3F - 0x61); }
    v_stack_p68 = result;
    goto loc_0091FD71;
loc_0092019B:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x3F - 0x61), Arg2, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0xA7) + 0x18), local_r12);
    goto loc_0091FF07;
loc_009201A7:
    if ((*(uint64_t *)(local_rsp - 0x3F + 0x9F)) == local_rbx) goto loc_0091FD59;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))) & (64));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    goto loc_0091FD59;
loc_009201C1:
loc_009201EA:
    goto loc_0091FDAA;
loc_009201F3:
    goto loc_0091FDBA;
loc_0092021E:
    goto loc_0091FDE0;
loc_00920249:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x18) + 0x4)) == 0) goto loc_0091FF30;
    local_r13 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x18)) + (8);
    *(uint16_t *)(local_rsp - 0x3F + 0x5F) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x18) + 0x4));
    goto loc_0091FF37;
loc_00920268:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87) + 0xC)) * 1 + 0x4)) == 0) goto loc_0091FF40;
    local_r12 = (*(uint64_t *)(local_rsp - 0x3F + 0x87) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87) + 0xC)) * 1) + (8);
    v_stack_p50 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87) + 0xC)) * 1 + 0x4));
    goto loc_0091FF43;
loc_00920284:
    if ((uint16_t)(*(uint16_t *)(local_r12 + (uint32_t)(*(uint32_t *)(local_r12 + 0xC)) * 1 + 0x4)) == 0) goto loc_0091FF59;
    Arg2 = (local_r12 + (uint32_t)(*(uint32_t *)(local_r12 + 0xC)) * 1) + (8);
    *(uint16_t *)(local_rsp - 0x3F + 0x6F) = (uint16_t)(*(uint16_t *)(local_r12 + (uint32_t)(*(uint32_t *)(local_r12 + 0xC)) * 1 + 0x4));
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = Arg2;
    goto loc_0091FF5D;
loc_009202A6:
    if (condition_is_equal) goto loc_0091FF81;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - (2));
    if (condition_is_equal) goto loc_0091FF81;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0091FF81;
    Arg1 = (uint32_t)((Arg1) - (4));
    goto loc_0091FF81;
loc_009202C8:
    if ((*(uint8_t *)(local_r13)) != ((uint8_t)(Arg2))) goto loc_0091FF90;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x2)) != ((uint16_t)(*(uint16_t *)(local_r13 + 0x2)))) goto loc_0091FF90;
    result = RtlCompareMemory(*(uint64_t *)(local_rsp - 0x3F + 0x67), local_r13, (uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x2))), (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x18) + 0x4)));
    if (result != (*(uint16_t *)(local_r13 + 0x2))) goto loc_0091FF90;
loc_00920307:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (8));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    goto loc_0091FFDD;
loc_00920313:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (32));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    goto loc_0091FFE7;
loc_0092031F:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (64));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    goto loc_0091FFF1;
loc_0092032B:
    if ((*(uint16_t *)(local_r12 + 0x4)) == ((uint16_t)((uint16_t)(*(uint16_t *)(local_r12 + (uint32_t)(*(uint32_t *)(local_r12 + 0xC)) * 1 + 0x4))))) goto loc_0091FE72;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (16));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    goto loc_0091FE72;
loc_00920343:
    if ((*(uint16_t *)(*(uint16_t *)(local_r13 + 0x2) + 0x4)) == ((uint16_t)((uint16_t)(*(uint16_t *)(local_r12 + (uint32_t)(*(uint32_t *)(local_r12 + 0xC)) * 1 + 0x4))))) goto loc_0091FE7B;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (32));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    goto loc_0091FE7B;
loc_0092035A:
loc_00920391:
    v_stack_p40 = *(uint64_t *)(local_rsp - 0x3F + 0xA7);
    v_stack_p38 = 32;
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x3F + 0x97);
    v_stack_p28 = (uint32_t)(v_stack_p60);
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    result = SepAdtSecurityDescriptorChangedAuditAlarm(local_rsp - 63 - 49, v_rip - 9564151, local_r13, local_r12);
    goto loc_009200B5;
loc_009203CF:
    v_stack_p40 = *(uint64_t *)(local_rsp - 0x3F + 0xA7);
    v_stack_p38 = 64;
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x3F + 0x9F);
    v_stack_p28 = (uint32_t)(v_stack_p60);
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    result = SepAdtSecurityDescriptorChangedAuditAlarm(local_rsp - 63 - 49, v_rip - 9564213, local_r13, local_r12);
    goto loc_009200BE;
loc_0092040D:
    result = SepAuditFailed((uint32_t)((uint32_t)(result)), v_rip - 9564213, local_r13, local_r12);
    goto loc_0091FE11;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091FC5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
