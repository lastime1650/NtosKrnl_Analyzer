# SepAdtAuditObjectAccessWithContext

- RVA: `0x0086EEF0`–`0x0086F246` (길이 `854` bytes)
- VA: `0x000000014086EEF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C184`
- 디코드: `224`개 명령, `854/854` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0086EFEF` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x0086F024` → [SepAuditingEnabledForSubcategory](../../text/41/SepAuditingEnabledForSubcategory_function_0041C6B0.md) (function, `0x0041C6B0`)
- `0x0086F030` → [SepIsRemovableStorageDevice](../91/SepIsRemovableStorageDevice_function_0091FC24.md) (function, `0x0091FC24`)
- `0x0086F058` → [SeCaptureSubjectContext](SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0086F0CB` → [SepAuditFailed](SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x0086F0E2` → [SeReleaseSubjectContext](SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0086F128` → [SepAuditingEnabledForSubcategory](../../text/41/SepAuditingEnabledForSubcategory_function_0041C6B0.md) (function, `0x0041C6B0`)
- `0x0086F13F` → [SepIsRemovableStorageDevice](../91/SepIsRemovableStorageDevice_function_0091FC24.md) (function, `0x0091FC24`)
- `0x0086F177` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0086F192` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0086F1C2` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0086F1DD` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0086F212` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [SepAdtCloseObjectAuditAlarm](SepAdtCloseObjectAuditAlarm_function_0086B4E8.md) at `0x0086B553`
- [sub_0086E7EE](Unknown_function_0086E7EE.md) at `0x0086E84A`
- [SepAdtDeleteObjectAuditAlarm](../91/SepAdtDeleteObjectAuditAlarm_function_0091E824.md) at `0x0091E8A6`
- [SeOpenObjectForDeleteAuditAlarmWithTransaction](../97/SeOpenObjectForDeleteAuditAlarmWithTransaction_function_00973EC0.md) at `0x00974028`
- [NtOpenObjectAuditAlarm](../97/NtOpenObjectAuditAlarm_function_00974700.md) at `0x00974AE8`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1CFF2`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1D03E`

### Static image references
- `0x0086EF1E` → RVA `0x00F04B68` (`.data`; read)
- `0x0086EF61` → RVA `0x00F04BA8` (`.data`; read)
- `0x0086EFB5` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0086EFBF` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x0086EFCA` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x0086EFF6` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x0086F003` → RVA `0x00FC6EE0` (`ALMOSTRO`; read)
- `0x0086F169` → RVA `0x00002030` (`.rdata`; read)
- `0x0086F1B4` → RVA `0x00002040` (`.rdata`; read)
- `0x0086F21D` → RVA `0x000013C0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0086F024` → [SepAuditingEnabledForSubcategory](../../text/41/SepAuditingEnabledForSubcategory_function_0041C6B0.md) (`PAGE` → `.text`)
  - `0x0086F128` → [SepAuditingEnabledForSubcategory](../../text/41/SepAuditingEnabledForSubcategory_function_0041C6B0.md) (`PAGE` → `.text`)
  - `0x0086F177` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0086F192` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x0086F1C2` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0086F1DD` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x0086F212` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0086EEF0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0086EEF5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0086EEFA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0086EEFF  57                              push rdi
0086EF00  41 54                           push r12
0086EF02  41 55                           push r13
0086EF04  41 56                           push r14
0086EF06  41 57                           push r15
0086EF08  48 83 EC 40                     sub rsp, 0x40
0086EF0C  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
0086EF14  0F 57 C0                        xorps xmm0, xmm0
0086EF17  41 0F B6 C0                     movzx eax, r8b
0086EF1B  4C 8B F9                        mov r15, rcx
0086EF1E  8B 0D 44 5C 69 00               mov ecx, dword ptr [rip + 0x695c44]
0086EF24  F6 D8                           neg al
0086EF26  41 0F B6 F1                     movzx esi, r9b
0086EF2A  41 0F B6 E8                     movzx ebp, r8b
0086EF2E  45 1B D2                        sbb r10d, r10d
0086EF31  66 41 C7 06 77 00               mov word ptr [r14], 0x77
0086EF37  41 83 E2 03                     and r10d, 3
0086EF3B  4C 8B EA                        mov r13, rdx
0086EF3E  41 8B FA                        mov edi, r10d
0086EF41  83 CF 30                        or edi, 0x30
0086EF44  45 84 C9                        test r9b, r9b
0086EF47  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0086EF4C  41 0F 44 FA                     cmove edi, r10d
0086EF50  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0086EF55  85 C9                           test ecx, ecx
0086EF57  74 1D                           je 0x14086ef76
0086EF59  8B C7                           mov eax, edi
0086EF5B  23 C1                           and eax, ecx
0086EF5D  75 0E                           jne 0x14086ef6d
0086EF5F  32 DB                           xor bl, bl
0086EF61  39 05 41 5C 69 00               cmp dword ptr [rip + 0x695c41], eax
0086EF67  0F 85 D2 00 00 00               jne 0x14086f03f
0086EF6D  85 C0                           test eax, eax
0086EF6F  0F 95 C3                        setne bl
0086EF72  84 DB                           test bl, bl
0086EF74  75 23                           jne 0x14086ef99
0086EF76  32 C0                           xor al, al
0086EF78  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0086EF7D  48 8B 6C 24 78                  mov rbp, qword ptr [rsp + 0x78]
0086EF82  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0086EF8A  48 83 C4 40                     add rsp, 0x40
0086EF8E  41 5F                           pop r15
0086EF90  41 5E                           pop r14
0086EF92  41 5D                           pop r13
0086EF94  41 5C                           pop r12
0086EF96  5F                              pop rdi
0086EF97  C3                              ret
0086EF98  CC                              int3
0086EF99  4D 85 FF                        test r15, r15
0086EF9C  0F 84 AB 01 00 00               je 0x14086f14d
0086EFA2  49 8D 47 D0                     lea rax, [r15 - 0x30]
0086EFA6  48 C1 E8 08                     shr rax, 8
0086EFAA  0F B6 D0                        movzx edx, al
0086EFAD  41 0F B6 47 E8                  movzx eax, byte ptr [r15 - 0x18]
0086EFB2  48 33 D0                        xor rdx, rax
0086EFB5  0F B6 05 90 7E 75 00            movzx eax, byte ptr [rip + 0x757e90]
0086EFBC  48 33 D0                        xor rdx, rax
0086EFBF  48 8D 05 3A 88 75 00            lea rax, [rip + 0x75883a]
0086EFC6  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0086EFCA  48 3B 05 EF 7A 75 00            cmp rax, qword ptr [rip + 0x757aef]
0086EFD1  75 23                           jne 0x14086eff6
0086EFD3  B8 76 00 00 00                  mov eax, 0x76
0086EFD8  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
0086EFE0  44 0F B6 C6                     movzx r8d, sil
0086EFE4  0F B7 C8                        movzx ecx, ax
0086EFE7  40 0F B6 D5                     movzx edx, bpl
0086EFEB  66 41 89 06                     mov word ptr [r14], ax
0086EFEF  E8 CC 1A 00 00                  call 0x140870ac0
0086EFF4  EB 82                           jmp 0x14086ef78
0086EFF6  48 3B 05 E3 7A 75 00            cmp rax, qword ptr [rip + 0x757ae3]
0086EFFD  0F 84 14 01 00 00               je 0x14086f117
0086F003  48 3B 05 D6 7E 75 00            cmp rax, qword ptr [rip + 0x757ed6]
0086F00A  74 07                           je 0x14086f013
0086F00C  B8 77 00 00 00                  mov eax, 0x77
0086F011  EB C5                           jmp 0x14086efd8
0086F013  41 B9 81 00 00 00               mov r9d, 0x81
0086F019  44 0F B6 C6                     movzx r8d, sil
0086F01D  41 8B C9                        mov ecx, r9d
0086F020  40 0F B6 D5                     movzx edx, bpl
0086F024  E8 87 D6 BA FF                  call 0x14041c6b0
0086F029  3C 01                           cmp al, 1
0086F02B  75 DF                           jne 0x14086f00c
0086F02D  49 8B CF                        mov rcx, r15
0086F030  E8 EF 0B 0B 00                  call 0x14091fc24
0086F035  3C 01                           cmp al, 1
0086F037  75 D3                           jne 0x14086f00c
0086F039  41 0F B7 C1                     movzx eax, r9w
0086F03D  EB 99                           jmp 0x14086efd8
0086F03F  48 83 BC 24 90 00 00 00 00      cmp qword ptr [rsp + 0x90], 0
0086F048  0F 85 9E 00 00 00               jne 0x14086f0ec
0086F04E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0086F053  4C 8D 64 24 20                  lea r12, [rsp + 0x20]
0086F058  E8 C3 C7 FF FF                  call 0x14086b820
0086F05D  49 8B 14 24                     mov rdx, qword ptr [r12]
0086F061  48 85 D2                        test rdx, rdx
0086F064  75 0A                           jne 0x14086f070
0086F066  49 8B 54 24 10                  mov rdx, qword ptr [r12 + 0x10]
0086F06B  48 85 D2                        test rdx, rdx
0086F06E  74 56                           je 0x14086f0c6
0086F070  80 7A 77 02                     cmp byte ptr [rdx + 0x77], 2
0086F074  75 5A                           jne 0x14086f0d0
0086F076  45 33 C9                        xor r9d, r9d
0086F079  41 B8 11 00 00 00               mov r8d, 0x11
0086F07F  45 0F B7 D1                     movzx r10d, r9w
0086F083  41 83 F8 1F                     cmp r8d, 0x1f
0086F087  73 70                           jae 0x14086f0f9
0086F089  41 8B C0                        mov eax, r8d
0086F08C  41 8B C8                        mov ecx, r8d
0086F08F  48 D1 E8                        shr rax, 1
0086F092  83 E1 01                        and ecx, 1
0086F095  C1 E1 02                        shl ecx, 2
0086F098  44 0F B6 5C 10 58               movzx r11d, byte ptr [rax + rdx + 0x58]
0086F09E  41 D3 EB                        shr r11d, cl
0086F0A1  41 F6 C3 01                     test r11b, 1
0086F0A5  74 0A                           je 0x14086f0b1
0086F0A7  40 F6 C7 02                     test dil, 2
0086F0AB  75 66                           jne 0x14086f113
0086F0AD  66 41 FF C1                     inc r9w
0086F0B1  41 F6 C3 04                     test r11b, 4
0086F0B5  74 0A                           je 0x14086f0c1
0086F0B7  40 F6 C7 20                     test dil, 0x20
0086F0BB  75 56                           jne 0x14086f113
0086F0BD  66 41 FF C2                     inc r10w
0086F0C1  41 FF C0                        inc r8d
0086F0C4  EB BD                           jmp 0x14086f083
0086F0C6  B9 7C 00 00 C0                  mov ecx, 0xc000007c
0086F0CB  E8 50 FD FF FF                  call 0x14086ee20
0086F0D0  48 83 BC 24 90 00 00 00 00      cmp qword ptr [rsp + 0x90], 0
0086F0D9  0F 85 93 FE FF FF               jne 0x14086ef72
0086F0DF  49 8B CC                        mov rcx, r12
0086F0E2  E8 29 C6 FF FF                  call 0x14086b710
0086F0E7  E9 86 FE FF FF                  jmp 0x14086ef72
0086F0EC  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
0086F0F4  E9 64 FF FF FF                  jmp 0x14086f05d
0086F0F9  40 F6 C7 01                     test dil, 1
0086F0FD  74 07                           je 0x14086f106
0086F0FF  66 41 83 F9 0E                  cmp r9w, 0xe
0086F104  74 0D                           je 0x14086f113
0086F106  40 F6 C7 10                     test dil, 0x10
0086F10A  74 C4                           je 0x14086f0d0
0086F10C  66 41 83 FA 0E                  cmp r10w, 0xe
0086F111  75 BD                           jne 0x14086f0d0
0086F113  B3 01                           mov bl, 1
0086F115  EB B9                           jmp 0x14086f0d0
0086F117  41 B9 81 00 00 00               mov r9d, 0x81
0086F11D  44 0F B6 C6                     movzx r8d, sil
0086F121  41 8B C9                        mov ecx, r9d
0086F124  40 0F B6 D5                     movzx edx, bpl
0086F128  E8 83 D5 BA FF                  call 0x14041c6b0
0086F12D  3C 01                           cmp al, 1
0086F12F  74 0A                           je 0x14086f13b
0086F131  B8 75 00 00 00                  mov eax, 0x75
0086F136  E9 9D FE FF FF                  jmp 0x14086efd8
0086F13B  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0086F13F  E8 E0 0A 0B 00                  call 0x14091fc24
0086F144  3C 01                           cmp al, 1
0086F146  75 E9                           jne 0x14086f131
0086F148  E9 EC FE FF FF                  jmp 0x14086f039
0086F14D  80 BC 24 98 00 00 00 00         cmp byte ptr [rsp + 0x98], 0
0086F155  0F 84 B2 00 00 00               je 0x14086f20d
0086F15B  4D 85 ED                        test r13, r13
0086F15E  0F 84 A8 FE FF FF               je 0x14086f00c
0086F164  41 0F B7 7D 00                  movzx edi, word ptr [r13]
0086F169  4C 8B 3D C0 2E 79 FF            mov r15, qword ptr [rip - 0x86d140]
0086F170  4D 8B 65 08                     mov r12, qword ptr [r13 + 8]
0086F174  48 D1 EF                        shr rdi, 1
0086F177  E8 74 F0 A8 FF                  call 0x1402fe1f0
0086F17C  BB 04 00 00 00                  mov ebx, 4
0086F181  49 8B D7                        mov rdx, r15
0086F184  48 3B FB                        cmp rdi, rbx
0086F187  49 8B CC                        mov rcx, r12
0086F18A  48 0F 46 DF                     cmovbe rbx, rdi
0086F18E  4C 8D 04 1B                     lea r8, [rbx + rbx]
0086F192  E8 D9 B4 E4 FF                  call 0x1406ba670
0086F197  48 D1 E8                        shr rax, 1
0086F19A  48 3B C3                        cmp rax, rbx
0086F19D  73 64                           jae 0x14086f203
0086F19F  41 0F B7 0C 44                  movzx ecx, word ptr [r12 + rax*2]
0086F1A4  41 0F B7 04 47                  movzx eax, word ptr [r15 + rax*2]
0086F1A9  2B C8                           sub ecx, eax
0086F1AB  85 C9                           test ecx, ecx
0086F1AD  74 82                           je 0x14086f131
0086F1AF  41 0F B7 7D 00                  movzx edi, word ptr [r13]
0086F1B4  4C 8B 3D 85 2E 79 FF            mov r15, qword ptr [rip - 0x86d17b]
0086F1BB  4D 8B 65 08                     mov r12, qword ptr [r13 + 8]
0086F1BF  48 D1 EF                        shr rdi, 1
0086F1C2  E8 29 F0 A8 FF                  call 0x1402fe1f0
0086F1C7  BB 03 00 00 00                  mov ebx, 3
0086F1CC  49 8B D7                        mov rdx, r15
0086F1CF  48 3B FB                        cmp rdi, rbx
0086F1D2  49 8B CC                        mov rcx, r12
0086F1D5  48 0F 46 DF                     cmovbe rbx, rdi
0086F1D9  4C 8D 04 1B                     lea r8, [rbx + rbx]
0086F1DD  E8 8E B4 E4 FF                  call 0x1406ba670
0086F1E2  48 D1 E8                        shr rax, 1
0086F1E5  48 3B C3                        cmp rax, rbx
0086F1E8  73 1E                           jae 0x14086f208
0086F1EA  41 0F B7 0C 44                  movzx ecx, word ptr [r12 + rax*2]
0086F1EF  41 0F B7 04 47                  movzx eax, word ptr [r15 + rax*2]
0086F1F4  2B C8                           sub ecx, eax
0086F1F6  85 C9                           test ecx, ecx
0086F1F8  0F 84 D5 FD FF FF               je 0x14086efd3
0086F1FE  E9 09 FE FF FF                  jmp 0x14086f00c
0086F203  8D 4F FC                        lea ecx, [rdi - 4]
0086F206  EB A3                           jmp 0x14086f1ab
0086F208  8D 4F FD                        lea ecx, [rdi - 3]
0086F20B  EB E9                           jmp 0x14086f1f6
0086F20D  4D 85 ED                        test r13, r13
0086F210  74 20                           je 0x14086f232
0086F212  E8 D9 EF A8 FF                  call 0x1402fe1f0
0086F217  66 41 83 7D 00 08               cmp word ptr [r13], 8
0086F21D  48 8B 0D 9C 21 79 FF            mov rcx, qword ptr [rip - 0x86de64]
0086F224  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0086F228  72 08                           jb 0x14086f232
0086F22A  48 8B 09                        mov rcx, qword ptr [rcx]
0086F22D  48 3B 08                        cmp rcx, qword ptr [rax]
0086F230  74 0A                           je 0x14086f23c
0086F232  B8 79 00 00 00                  mov eax, 0x79
0086F237  E9 9C FD FF FF                  jmp 0x14086efd8
0086F23C  B8 78 00 00 00                  mov eax, 0x78
0086F241  E9 92 FD FF FF                  jmp 0x14086efd8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAdtAuditObjectAccessWithContext(__int64 a1, __int64 a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = (unsigned __int8)(-(a3));
    *(unsigned __int16 *)(a7) = 119;
    v_r10 = (unsigned int)((v_r10) & (3));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) | (48));
    v_stack_m48 = v_xmm0;
    if (a4 == 0) { v_rdi = (unsigned int)(v_r10); }
    v_stack_m38 = v_xmm0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6904900))) == 0) goto loc_0086EF76;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6904900)))));
    if (condition_is_not_equal) goto loc_0086EF6D;
    v_rbx = 0;
    if ((*(unsigned int *)(v_rip + 6904897)) != ((unsigned int)(result))) goto loc_0086F03F;
loc_0086EF6D:
    v_rbx = ((unsigned int)(result) != 0) ? 1 : 0;
loc_0086EF72:
    if ((unsigned __int8)(v_rbx) != 0) goto loc_0086EF99;
loc_0086EF76:
    result = 0;
loc_0086EF78:
    v_rsp = (v_rsp) + (64);
    return result;
loc_0086EF99:
    if (a1 == 0) goto loc_0086F14D;
    result = (a1 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a1 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7700112));
    if ((*(unsigned __int64 *)(v_rip + 7702586 + a2 * 8)) != (*(unsigned __int64 *)(v_rip + 7699183))) goto loc_0086EFF6;
loc_0086EFD3:
loc_0086EFD8:
    *(unsigned __int16 *)(a7) = 118;
    result = SepAdtAuditThisEventWithContext(118, (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), a5);
    goto loc_0086EF78;
loc_0086EFF6:
    if (result == (*(unsigned __int64 *)(v_rip + 7699171))) goto loc_0086F117;
    if (result == (*(unsigned __int64 *)(v_rip + 7700182))) goto loc_0086F013;
loc_0086F00C:
    goto loc_0086EFD8;
loc_0086F013:
    result = SepAuditingEnabledForSubcategory(129, (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), 129);
    if (((unsigned __int8)(result)) != 1) goto loc_0086F00C;
    result = SepIsRemovableStorageDevice(a1, (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), 129);
    if (((unsigned __int8)(result)) != 1) goto loc_0086F00C;
loc_0086F039:
    goto loc_0086EFD8;
loc_0086F03F:
    if (a5 != 0) goto loc_0086F0EC;
    result = SeCaptureSubjectContext(v_stack_p20, (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), 129);
loc_0086F05D:
    if (*(unsigned __int64 *)(v_stack_p20) != 0) goto loc_0086F070;
    if (*(unsigned __int64 *)(v_stack_p20 + 16) == 0) goto loc_0086F0C6;
loc_0086F070:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p20 + 16) + 119)) != 2) goto loc_0086F0D0;
    a4 = 0;
loc_0086F083:
    if (17 >= 31) goto loc_0086F0F9;
    result = (17) >> (1);
    a1 = (unsigned int)((17) & (1));
    a1 = (unsigned int)((a1) << (2));
    v_r11 = (unsigned int)((*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_stack_p20 + 16) * 1 + 88)) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(v_r11)) & (1)) == 0) goto loc_0086F0B1;
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_0086F113;
    a4 = (unsigned __int16)((a4) + 1);
loc_0086F0B1:
    if ((((unsigned __int8)(v_r11)) & (4)) == 0) goto loc_0086F0C1;
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_0086F113;
    v_r10 = (unsigned __int16)((0) + 1);
loc_0086F0C1:
    a3 = (unsigned int)((17) + 1);
    goto loc_0086F083;
loc_0086F0C6:
    result = SepAuditFailed((unsigned int)(0xC000007CULL), *(unsigned __int64 *)(v_stack_p20 + 16), a3, a4);
loc_0086F0D0:
    if (a5 != 0) goto loc_0086EF72;
    result = SeReleaseSubjectContext(v_stack_p20, *(unsigned __int64 *)(v_stack_p20 + 16), a3, a4);
    goto loc_0086EF72;
loc_0086F0EC:
    goto loc_0086F05D;
loc_0086F0F9:
    if ((((unsigned __int8)(v_rdi)) & (1)) == 0) goto loc_0086F106;
    if (a4 == 14) goto loc_0086F113;
loc_0086F106:
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_0086F0D0;
    if (((unsigned __int16)(v_r10)) != 14) goto loc_0086F0D0;
loc_0086F113:
    goto loc_0086F0D0;
loc_0086F117:
    result = SepAuditingEnabledForSubcategory(129, (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), 129);
    if (((unsigned __int8)(result)) == 1) goto loc_0086F13B;
loc_0086F131:
    goto loc_0086EFD8;
loc_0086F13B:
    result = SepIsRemovableStorageDevice(*(unsigned __int64 *)(a1 + 8), (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), 129);
    if (((unsigned __int8)(result)) != 1) goto loc_0086F131;
    goto loc_0086F039;
loc_0086F14D:
    if (a6 == 0) goto loc_0086F20D;
    if (a2 == 0) goto loc_0086F00C;
    v_rdi = (*(unsigned __int16 *)(a2)) >> (1);
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(a1 + 8), (unsigned __int8)(v_stack_p10), (unsigned __int8)(v_stack_p18), 129);
    v_rbx = 4;
    if (v_rdi <= 4) { v_rbx = v_rdi; }
    result = RtlCompareMemory(*(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(v_rip - 8835392), v_rbx + v_rbx * 1, 129);
    result = (result) >> (1);
    if (result >= v_rbx) goto loc_0086F203;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + result * 2)) - ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 8835392) + result * 2))));
loc_0086F1AB:
    if ((unsigned int)(a1) == 0) goto loc_0086F131;
    v_rdi = (*(unsigned __int16 *)(a2)) >> (1);
    result = PsGetCurrentServerSiloGlobals(a1, *(unsigned __int64 *)(v_rip - 8835392), v_rbx + v_rbx * 1, 129);
    v_rbx = 3;
    if (v_rdi <= 3) { v_rbx = v_rdi; }
    result = RtlCompareMemory(*(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(v_rip - 8835451), v_rbx + v_rbx * 1, 129);
    result = (result) >> (1);
    if (result >= v_rbx) goto loc_0086F208;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + result * 2)) - ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 8835451) + result * 2))));
loc_0086F1F6:
    if ((unsigned int)(a1) == 0) goto loc_0086EFD3;
    goto loc_0086F00C;
loc_0086F203:
    goto loc_0086F1AB;
loc_0086F208:
    goto loc_0086F1F6;
loc_0086F20D:
    if (a2 == 0) goto loc_0086F232;
    result = PsGetCurrentServerSiloGlobals(v_rdi - 3, *(unsigned __int64 *)(v_rip - 8835451), v_rbx + v_rbx * 1, 129);
    if ((*(unsigned __int16 *)(a2)) < 8) goto loc_0086F232;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8838756))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)))) goto loc_0086F23C;
loc_0086F232:
    goto loc_0086EFD8;
loc_0086F23C:
    goto loc_0086EFD8;
}
```

## 5. (Beta) C Style

```c
int64_t SepAdtAuditObjectAccessWithContext(int64_t Arg1, int64_t Arg2, uint8_t Arg3, uint8_t Arg4, int64_t Arg5, uint8_t Arg6, void *Arg7)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = (uint8_t)(-(Arg3));
    *(uint16_t *)(arg7) = 119;
    local_r10 = (uint32_t)((local_r10) & (3));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) | (48));
    v_stack_m48 = v_xmm0;
    if (Arg4 == 0) { local_rdi = (uint32_t)(local_r10); }
    v_stack_m38 = v_xmm0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x695C44))) == 0) goto loc_0086EF76;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x695C44)))));
    if (condition_is_not_equal) goto loc_0086EF6D;
    local_rbx = 0;
    if ((*(uint32_t *)(v_rip + 0x695C41)) != ((uint32_t)(result))) goto loc_0086F03F;
loc_0086EF6D:
    local_rbx = ((uint32_t)(result) != 0) ? 1 : 0;
loc_0086EF72:
    if ((uint8_t)(local_rbx) != 0) goto loc_0086EF99;
loc_0086EF76:
    result = 0;
loc_0086EF78:
    local_rsp = (local_rsp) + (64);
    return result;
loc_0086EF99:
    if (Arg1 == 0) goto loc_0086F14D;
    result = (Arg1 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(Arg1 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x757E90));
    if ((*(uint64_t *)(v_rip + 0x75883A + Arg2 * 8)) != (*(uint64_t *)(v_rip + 0x757AEF))) goto loc_0086EFF6;
loc_0086EFD3:
loc_0086EFD8:
    *(uint16_t *)(arg7) = 118;
    result = SepAdtAuditThisEventWithContext(118, (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), Arg5);
    goto loc_0086EF78;
loc_0086EFF6:
    if (result == (*(uint64_t *)(v_rip + 0x757AE3))) goto loc_0086F117;
    if (result == (*(uint64_t *)(v_rip + 0x757ED6))) goto loc_0086F013;
loc_0086F00C:
    goto loc_0086EFD8;
loc_0086F013:
    result = SepAuditingEnabledForSubcategory(129, (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), 129);
    if (((uint8_t)(result)) != 1) goto loc_0086F00C;
    result = SepIsRemovableStorageDevice(Arg1, (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), 129);
    if (((uint8_t)(result)) != 1) goto loc_0086F00C;
loc_0086F039:
    goto loc_0086EFD8;
loc_0086F03F:
    if (Arg5 != 0) goto loc_0086F0EC;
    result = SeCaptureSubjectContext(v_stack_p20, (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), 129);
loc_0086F05D:
    if (*(uint64_t *)(v_stack_p20) != 0) goto loc_0086F070;
    if (*(uint64_t *)(v_stack_p20 + 0x10) == 0) goto loc_0086F0C6;
loc_0086F070:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + 0x77)) != 2) goto loc_0086F0D0;
    Arg4 = 0;
loc_0086F083:
    if (17 >= 31) goto loc_0086F0F9;
    result = (17) >> (1);
    Arg1 = (uint32_t)((17) & (1));
    Arg1 = (uint32_t)((Arg1) << (2));
    local_r11 = (uint32_t)((*(uint8_t *)(result + *(uint64_t *)(v_stack_p20 + 0x10) * 1 + 0x58)) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(local_r11)) & (1)) == 0) goto loc_0086F0B1;
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_0086F113;
    Arg4 = (uint16_t)((Arg4) + 1);
loc_0086F0B1:
    if ((((uint8_t)(local_r11)) & (4)) == 0) goto loc_0086F0C1;
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_0086F113;
    local_r10 = (uint16_t)((0) + 1);
loc_0086F0C1:
    Arg3 = (uint32_t)((17) + 1);
    goto loc_0086F083;
loc_0086F0C6:
    result = SepAuditFailed((uint32_t)(0xC000007CULL), *(uint64_t *)(v_stack_p20 + 0x10), Arg3, Arg4);
loc_0086F0D0:
    if (Arg5 != 0) goto loc_0086EF72;
    result = SeReleaseSubjectContext(v_stack_p20, *(uint64_t *)(v_stack_p20 + 0x10), Arg3, Arg4);
    goto loc_0086EF72;
loc_0086F0EC:
    goto loc_0086F05D;
loc_0086F0F9:
    if ((((uint8_t)(local_rdi)) & (1)) == 0) goto loc_0086F106;
    if (Arg4 == 14) goto loc_0086F113;
loc_0086F106:
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_0086F0D0;
    if (((uint16_t)(local_r10)) != 14) goto loc_0086F0D0;
loc_0086F113:
    goto loc_0086F0D0;
loc_0086F117:
    result = SepAuditingEnabledForSubcategory(129, (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), 129);
    if (((uint8_t)(result)) == 1) goto loc_0086F13B;
loc_0086F131:
    goto loc_0086EFD8;
loc_0086F13B:
    result = SepIsRemovableStorageDevice(*(uint64_t *)(Arg1 + 0x8), (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), 129);
    if (((uint8_t)(result)) != 1) goto loc_0086F131;
    goto loc_0086F039;
loc_0086F14D:
    if (Arg6 == 0) goto loc_0086F20D;
    if (Arg2 == 0) goto loc_0086F00C;
    local_rdi = (*(uint16_t *)(Arg2)) >> (1);
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(Arg1 + 0x8), (uint8_t)(v_stack_p10), (uint8_t)(v_stack_p18), 129);
    local_rbx = 4;
    if (local_rdi <= 4) { local_rbx = local_rdi; }
    result = RtlCompareMemory(*(uint64_t *)(Arg2 + 0x8), *(uint64_t *)(v_rip - 0x86D140), local_rbx + local_rbx * 1, 129);
    result = (result) >> (1);
    if (result >= local_rbx) goto loc_0086F203;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x8) + result * 2)) - ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x86D140) + result * 2))));
loc_0086F1AB:
    if ((uint32_t)(Arg1) == 0) goto loc_0086F131;
    local_rdi = (*(uint16_t *)(Arg2)) >> (1);
    result = PsGetCurrentServerSiloGlobals(Arg1, *(uint64_t *)(v_rip - 0x86D140), local_rbx + local_rbx * 1, 129);
    local_rbx = 3;
    if (local_rdi <= 3) { local_rbx = local_rdi; }
    result = RtlCompareMemory(*(uint64_t *)(Arg2 + 0x8), *(uint64_t *)(v_rip - 0x86D17B), local_rbx + local_rbx * 1, 129);
    result = (result) >> (1);
    if (result >= local_rbx) goto loc_0086F208;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x8) + result * 2)) - ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x86D17B) + result * 2))));
loc_0086F1F6:
    if ((uint32_t)(Arg1) == 0) goto loc_0086EFD3;
    goto loc_0086F00C;
loc_0086F203:
    goto loc_0086F1AB;
loc_0086F208:
    goto loc_0086F1F6;
loc_0086F20D:
    if (Arg2 == 0) goto loc_0086F232;
    result = PsGetCurrentServerSiloGlobals(local_rdi - 3, *(uint64_t *)(v_rip - 0x86D17B), local_rbx + local_rbx * 1, 129);
    if ((*(uint16_t *)(Arg2)) < 8) goto loc_0086F232;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86DE64))) == (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8)))) goto loc_0086F23C;
loc_0086F232:
    goto loc_0086EFD8;
loc_0086F23C:
    goto loc_0086EFD8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086EEF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
