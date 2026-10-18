# IopMarkPagesForDpcData

- RVA: `0x005A1C90`–`0x005A20D5` (길이 `1,093` bytes)
- VA: `0x00000001405A1C90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075C18`
- 디코드: `289`개 명령, `1,093/1,093` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x005A1CF1` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1D0E` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1D3F` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1D5D` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x005A1D70` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1D8C` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x005A1D9F` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1DE0` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1E08` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1E3E` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1E66` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1EAE` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1EC7` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1EE8` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1F40` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x005A1F69` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1F8E` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x005A1FC1` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A1FDD` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A2008` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A2026` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x005A2049` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A206E` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x005A2093` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)

### Direct callers
- [IopAddMiniDumpPagesToPartialKernelDump](IopAddMiniDumpPagesToPartialKernelDump_function_005A16F8.md) at `0x005A1802`

### Static image references
- `0x005A1CB8` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x005A1CC7` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x005A1DD3` → RVA `0x00FC51D4` (`ALMOSTRO`; read)
- `0x005A1DFB` → RVA `0x00FC507C` (`ALMOSTRO`; read)
- `0x005A1E17` → RVA `0x00E0A9B4` (`.data`; read)
- `0x005A1E31` → RVA `0x00FC505C` (`ALMOSTRO`; read)
- `0x005A1E92` → RVA `0x01201840` (`CFGRO`; read)
- `0x005A1EDB` → RVA `0x00FC5060` (`ALMOSTRO`; read)
- `0x005A1F06` → RVA `0x00F10D40` (`.data`; read)
- `0x005A1F21` → RVA `0x00F10D50` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A1C90  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005A1C95  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
005A1C9A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005A1C9F  57                              push rdi
005A1CA0  41 54                           push r12
005A1CA2  41 55                           push r13
005A1CA4  41 56                           push r14
005A1CA6  41 57                           push r15
005A1CA8  48 83 EC 20                     sub rsp, 0x20
005A1CAC  33 DB                           xor ebx, ebx
005A1CAE  48 8B F1                        mov rsi, rcx
005A1CB1  45 33 E4                        xor r12d, r12d
005A1CB4  44 8D 6B 40                     lea r13d, [rbx + 0x40]
005A1CB8  8B 05 C2 4D A2 00               mov eax, dword ptr [rip + 0xa24dc2]
005A1CBE  44 3B E0                        cmp r12d, eax
005A1CC1  0F 83 3F 02 00 00               jae 0x1405a1f06
005A1CC7  48 8D 3D 72 6F A2 00            lea rdi, [rip + 0xa26f72]
005A1CCE  4A 8B 3C E7                     mov rdi, qword ptr [rdi + r12*8]
005A1CD2  48 85 FF                        test rdi, rdi
005A1CD5  0F 84 23 02 00 00               je 0x1405a1efe
005A1CDB  48 8B 97 A8 8E 00 00            mov rdx, qword ptr [rdi + 0x8ea8]
005A1CE2  48 85 D2                        test rdx, rdx
005A1CE5  74 11                           je 0x1405a1cf8
005A1CE7  44 8B 87 DC 38 00 00            mov r8d, dword ptr [rdi + 0x38dc]
005A1CEE  48 8B CE                        mov rcx, rsi
005A1CF1  E8 BA BB 0D 00                  call 0x14067d8b0
005A1CF6  8B D8                           mov ebx, eax
005A1CF8  48 8B 97 18 83 00 00            mov rdx, qword ptr [rdi + 0x8318]
005A1CFF  48 85 D2                        test rdx, rdx
005A1D02  74 11                           je 0x1405a1d15
005A1D04  44 8B 87 24 83 00 00            mov r8d, dword ptr [rdi + 0x8324]
005A1D0B  48 8B CE                        mov rcx, rsi
005A1D0E  E8 9D BB 0D 00                  call 0x14067d8b0
005A1D13  8B D8                           mov ebx, eax
005A1D15  33 ED                           xor ebp, ebp
005A1D17  83 FD 02                        cmp ebp, 2
005A1D1A  0F 83 A7 00 00 00               jae 0x1405a1dc7
005A1D20  8B C5                           mov eax, ebp
005A1D22  41 B8 30 00 00 00               mov r8d, 0x30
005A1D28  48 05 2C 01 00 00               add rax, 0x12c
005A1D2E  48 8B CE                        mov rcx, rsi
005A1D31  4C 8D 34 40                     lea r14, [rax + rax*2]
005A1D35  49 C1 E6 04                     shl r14, 4
005A1D39  4C 03 F7                        add r14, rdi
005A1D3C  49 8B D6                        mov rdx, r14
005A1D3F  E8 6C BB 0D 00                  call 0x14067d8b0
005A1D44  8B D8                           mov ebx, eax
005A1D46  85 C0                           test eax, eax
005A1D48  0F 88 69 03 00 00               js 0x1405a20b7
005A1D4E  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
005A1D52  48 85 C0                        test rax, rax
005A1D55  74 28                           je 0x1405a1d7f
005A1D57  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
005A1D5B  33 D2                           xor edx, edx
005A1D5D  E8 6E E0 CD FF                  call 0x14027fdd0
005A1D62  84 C0                           test al, al
005A1D64  74 19                           je 0x1405a1d7f
005A1D66  49 8B 56 20                     mov rdx, qword ptr [r14 + 0x20]
005A1D6A  4D 8B C5                        mov r8, r13
005A1D6D  48 8B CE                        mov rcx, rsi
005A1D70  E8 3B BB 0D 00                  call 0x14067d8b0
005A1D75  8B D8                           mov ebx, eax
005A1D77  85 C0                           test eax, eax
005A1D79  0F 88 38 03 00 00               js 0x1405a20b7
005A1D7F  4D 8B 36                        mov r14, qword ptr [r14]
005A1D82  4D 85 F6                        test r14, r14
005A1D85  74 39                           je 0x1405a1dc0
005A1D87  33 D2                           xor edx, edx
005A1D89  49 8B CE                        mov rcx, r14
005A1D8C  E8 3F E0 CD FF                  call 0x14027fdd0
005A1D91  84 C0                           test al, al
005A1D93  74 2B                           je 0x1405a1dc0
005A1D95  4D 8B C5                        mov r8, r13
005A1D98  49 8D 56 F8                     lea rdx, [r14 - 8]
005A1D9C  48 8B CE                        mov rcx, rsi
005A1D9F  E8 0C BB 0D 00                  call 0x14067d8b0
005A1DA4  8B D8                           mov ebx, eax
005A1DA6  85 C0                           test eax, eax
005A1DA8  0F 88 09 03 00 00               js 0x1405a20b7
005A1DAE  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
005A1DB2  48 83 FA 01                     cmp rdx, 1
005A1DB6  74 C7                           je 0x1405a1d7f
005A1DB8  41 B8 60 00 00 00               mov r8d, 0x60
005A1DBE  EB AD                           jmp 0x1405a1d6d
005A1DC0  FF C5                           inc ebp
005A1DC2  E9 50 FF FF FF                  jmp 0x1405a1d17
005A1DC7  48 8B 97 A0 38 00 00            mov rdx, qword ptr [rdi + 0x38a0]
005A1DCE  48 85 D2                        test rdx, rdx
005A1DD1  74 1C                           je 0x1405a1def
005A1DD3  44 8B 05 FA 33 A2 00            mov r8d, dword ptr [rip + 0xa233fa]
005A1DDA  48 8B CE                        mov rcx, rsi
005A1DDD  49 2B D0                        sub rdx, r8
005A1DE0  E8 CB BA 0D 00                  call 0x14067d8b0
005A1DE5  8B D8                           mov ebx, eax
005A1DE7  85 C0                           test eax, eax
005A1DE9  0F 88 C8 02 00 00               js 0x1405a20b7
005A1DEF  48 8B 97 68 87 00 00            mov rdx, qword ptr [rdi + 0x8768]
005A1DF6  48 85 D2                        test rdx, rdx
005A1DF9  74 1C                           je 0x1405a1e17
005A1DFB  44 8B 05 7A 32 A2 00            mov r8d, dword ptr [rip + 0xa2327a]
005A1E02  48 8B CE                        mov rcx, rsi
005A1E05  49 2B D0                        sub rdx, r8
005A1E08  E8 A3 BA 0D 00                  call 0x14067d8b0
005A1E0D  8B D8                           mov ebx, eax
005A1E0F  85 C0                           test eax, eax
005A1E11  0F 88 A0 02 00 00               js 0x1405a20b7
005A1E17  8B 05 97 8B 86 00               mov eax, dword ptr [rip + 0x868b97]
005A1E1D  A8 01                           test al, 1
005A1E1F  0F 84 D9 00 00 00               je 0x1405a1efe
005A1E25  48 8B 97 D8 8F 00 00            mov rdx, qword ptr [rdi + 0x8fd8]
005A1E2C  48 85 D2                        test rdx, rdx
005A1E2F  74 1C                           je 0x1405a1e4d
005A1E31  44 8B 05 24 32 A2 00            mov r8d, dword ptr [rip + 0xa23224]
005A1E38  48 8B CE                        mov rcx, rsi
005A1E3B  49 2B D0                        sub rdx, r8
005A1E3E  E8 6D BA 0D 00                  call 0x14067d8b0
005A1E43  8B D8                           mov ebx, eax
005A1E45  85 C0                           test eax, eax
005A1E47  0F 88 6A 02 00 00               js 0x1405a20b7
005A1E4D  48 8B 97 88 FE FF FF            mov rdx, qword ptr [rdi - 0x178]
005A1E54  48 85 D2                        test rdx, rdx
005A1E57  0F 84 A1 00 00 00               je 0x1405a1efe
005A1E5D  41 B8 68 00 00 00               mov r8d, 0x68
005A1E63  48 8B CE                        mov rcx, rsi
005A1E66  E8 45 BA 0D 00                  call 0x14067d8b0
005A1E6B  8B D8                           mov ebx, eax
005A1E6D  85 C0                           test eax, eax
005A1E6F  0F 88 42 02 00 00               js 0x1405a20b7
005A1E75  BD 01 00 00 00                  mov ebp, 1
005A1E7A  83 FD 04                        cmp ebp, 4
005A1E7D  77 7F                           ja 0x1405a1efe
005A1E7F  48 8B 87 88 FE FF FF            mov rax, qword ptr [rdi - 0x178]
005A1E86  8B CD                           mov ecx, ebp
005A1E88  48 8B 54 C8 1C                  mov rdx, qword ptr [rax + rcx*8 + 0x1c]
005A1E8D  48 85 D2                        test rdx, rdx
005A1E90  74 65                           je 0x1405a1ef7
005A1E92  80 3D A7 F9 C5 00 00            cmp byte ptr [rip + 0xc5f9a7], 0
005A1E99  74 40                           je 0x1405a1edb
005A1E9B  48 8D 5A 08                     lea rbx, [rdx + 8]
005A1E9F  48 83 3B 00                     cmp qword ptr [rbx], 0
005A1EA3  74 36                           je 0x1405a1edb
005A1EA5  41 B8 30 00 00 00               mov r8d, 0x30
005A1EAB  48 8B CE                        mov rcx, rsi
005A1EAE  E8 FD B9 0D 00                  call 0x14067d8b0
005A1EB3  85 C0                           test eax, eax
005A1EB5  0F 88 FC 01 00 00               js 0x1405a20b7
005A1EBB  48 8B 13                        mov rdx, qword ptr [rbx]
005A1EBE  41 B8 20 00 00 00               mov r8d, 0x20
005A1EC4  48 8B CE                        mov rcx, rsi
005A1EC7  E8 E4 B9 0D 00                  call 0x14067d8b0
005A1ECC  85 C0                           test eax, eax
005A1ECE  0F 88 E3 01 00 00               js 0x1405a20b7
005A1ED4  48 8B 13                        mov rdx, qword ptr [rbx]
005A1ED7  48 83 C2 20                     add rdx, 0x20
005A1EDB  44 8B 05 7E 31 A2 00            mov r8d, dword ptr [rip + 0xa2317e]
005A1EE2  48 8B CE                        mov rcx, rsi
005A1EE5  49 2B D0                        sub rdx, r8
005A1EE8  E8 C3 B9 0D 00                  call 0x14067d8b0
005A1EED  8B D8                           mov ebx, eax
005A1EEF  85 C0                           test eax, eax
005A1EF1  0F 88 C0 01 00 00               js 0x1405a20b7
005A1EF7  FF C5                           inc ebp
005A1EF9  E9 7C FF FF FF                  jmp 0x1405a1e7a
005A1EFE  41 FF C4                        inc r12d
005A1F01  E9 B2 FD FF FF                  jmp 0x1405a1cb8
005A1F06  83 3D 33 EE 96 00 00            cmp dword ptr [rip + 0x96ee33], 0
005A1F0D  0F 86 A2 01 00 00               jbe 0x1405a20b5
005A1F13  8B 05 9B 8A 86 00               mov eax, dword ptr [rip + 0x868a9b]
005A1F19  A8 01                           test al, 1
005A1F1B  0F 84 94 01 00 00               je 0x1405a20b5
005A1F21  4C 8B 35 28 EE 96 00            mov r14, qword ptr [rip + 0x96ee28]
005A1F28  45 33 E4                        xor r12d, r12d
005A1F2B  48 8D 05 1E EE 96 00            lea rax, [rip + 0x96ee1e]
005A1F32  4C 3B F0                        cmp r14, rax
005A1F35  0F 84 7A 01 00 00               je 0x1405a20b5
005A1F3B  33 D2                           xor edx, edx
005A1F3D  49 8B CE                        mov rcx, r14
005A1F40  E8 8B DE CD FF                  call 0x14027fdd0
005A1F45  84 C0                           test al, al
005A1F47  0F 84 68 01 00 00               je 0x1405a20b5
005A1F4D  41 FF C4                        inc r12d
005A1F50  44 3B 25 E9 ED 96 00            cmp r12d, dword ptr [rip + 0x96ede9]
005A1F57  0F 87 58 01 00 00               ja 0x1405a20b5
005A1F5D  41 B8 E0 00 00 00               mov r8d, 0xe0
005A1F63  49 8B D6                        mov rdx, r14
005A1F66  48 8B CE                        mov rcx, rsi
005A1F69  E8 42 B9 0D 00                  call 0x14067d8b0
005A1F6E  8B D8                           mov ebx, eax
005A1F70  85 C0                           test eax, eax
005A1F72  0F 88 3F 01 00 00               js 0x1405a20b7
005A1F78  4D 8D 6E 10                     lea r13, [r14 + 0x10]
005A1F7C  49 8B 7D 00                     mov rdi, qword ptr [r13]
005A1F80  49 3B FD                        cmp rdi, r13
005A1F83  0F 84 24 01 00 00               je 0x1405a20ad
005A1F89  33 D2                           xor edx, edx
005A1F8B  48 8B CF                        mov rcx, rdi
005A1F8E  E8 3D DE CD FF                  call 0x14027fdd0
005A1F93  84 C0                           test al, al
005A1F95  0F 84 12 01 00 00               je 0x1405a20ad
005A1F9B  48 8B 07                        mov rax, qword ptr [rdi]
005A1F9E  48 39 78 08                     cmp qword ptr [rax + 8], rdi
005A1FA2  0F 85 0D 01 00 00               jne 0x1405a20b5
005A1FA8  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
005A1FAC  48 39 38                        cmp qword ptr [rax], rdi
005A1FAF  0F 85 00 01 00 00               jne 0x1405a20b5
005A1FB5  41 B8 98 00 00 00               mov r8d, 0x98
005A1FBB  48 8B D7                        mov rdx, rdi
005A1FBE  48 8B CE                        mov rcx, rsi
005A1FC1  E8 EA B8 0D 00                  call 0x14067d8b0
005A1FC6  85 C0                           test eax, eax
005A1FC8  0F 88 E9 00 00 00               js 0x1405a20b7
005A1FCE  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
005A1FD2  48 8B CE                        mov rcx, rsi
005A1FD5  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
005A1FD9  49 C1 E0 03                     shl r8, 3
005A1FDD  E8 CE B8 0D 00                  call 0x14067d8b0
005A1FE2  8B D8                           mov ebx, eax
005A1FE4  85 C0                           test eax, eax
005A1FE6  0F 88 CB 00 00 00               js 0x1405a20b7
005A1FEC  33 ED                           xor ebp, ebp
005A1FEE  3B 6F 18                        cmp ebp, dword ptr [rdi + 0x18]
005A1FF1  0F 83 AE 00 00 00               jae 0x1405a20a5
005A1FF7  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
005A1FFB  41 B8 20 01 00 00               mov r8d, 0x120
005A2001  48 8B CE                        mov rcx, rsi
005A2004  48 8B 14 EA                     mov rdx, qword ptr [rdx + rbp*8]
005A2008  E8 A3 B8 0D 00                  call 0x14067d8b0
005A200D  8B D8                           mov ebx, eax
005A200F  85 C0                           test eax, eax
005A2011  0F 88 A0 00 00 00               js 0x1405a20b7
005A2017  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
005A201B  48 8B 0C E8                     mov rcx, qword ptr [rax + rbp*8]
005A201F  48 85 C9                        test rcx, rcx
005A2022  74 7A                           je 0x1405a209e
005A2024  33 D2                           xor edx, edx
005A2026  E8 A5 DD CD FF                  call 0x14027fdd0
005A202B  84 C0                           test al, al
005A202D  74 6F                           je 0x1405a209e
005A202F  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
005A2033  48 8B 0C E8                     mov rcx, qword ptr [rax + rbp*8]
005A2037  48 8B 51 18                     mov rdx, qword ptr [rcx + 0x18]
005A203B  48 85 D2                        test rdx, rdx
005A203E  74 14                           je 0x1405a2054
005A2040  41 B8 00 10 00 00               mov r8d, 0x1000
005A2046  48 8B CE                        mov rcx, rsi
005A2049  E8 62 B8 0D 00                  call 0x14067d8b0
005A204E  8B D8                           mov ebx, eax
005A2050  85 C0                           test eax, eax
005A2052  78 63                           js 0x1405a20b7
005A2054  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
005A2058  48 8B 0C E8                     mov rcx, qword ptr [rax + rbp*8]
005A205C  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
005A2060  48 85 D2                        test rdx, rdx
005A2063  74 14                           je 0x1405a2079
005A2065  41 B8 00 10 00 00               mov r8d, 0x1000
005A206B  48 8B CE                        mov rcx, rsi
005A206E  E8 3D B8 0D 00                  call 0x14067d8b0
005A2073  8B D8                           mov ebx, eax
005A2075  85 C0                           test eax, eax
005A2077  78 3E                           js 0x1405a20b7
005A2079  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
005A207D  48 8B 0C E8                     mov rcx, qword ptr [rax + rbp*8]
005A2081  48 8B 51 30                     mov rdx, qword ptr [rcx + 0x30]
005A2085  48 85 D2                        test rdx, rdx
005A2088  74 14                           je 0x1405a209e
005A208A  41 B8 00 10 00 00               mov r8d, 0x1000
005A2090  48 8B CE                        mov rcx, rsi
005A2093  E8 18 B8 0D 00                  call 0x14067d8b0
005A2098  8B D8                           mov ebx, eax
005A209A  85 C0                           test eax, eax
005A209C  78 19                           js 0x1405a20b7
005A209E  FF C5                           inc ebp
005A20A0  E9 49 FF FF FF                  jmp 0x1405a1fee
005A20A5  48 8B 3F                        mov rdi, qword ptr [rdi]
005A20A8  E9 D3 FE FF FF                  jmp 0x1405a1f80
005A20AD  4D 8B 36                        mov r14, qword ptr [r14]
005A20B0  E9 76 FE FF FF                  jmp 0x1405a1f2b
005A20B5  8B C3                           mov eax, ebx
005A20B7  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
005A20BC  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
005A20C1  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
005A20C6  48 83 C4 20                     add rsp, 0x20
005A20CA  41 5F                           pop r15
005A20CC  41 5E                           pop r14
005A20CE  41 5D                           pop r13
005A20D0  41 5C                           pop r12
005A20D2  5F                              pop rdi
005A20D3  C3                              ret
005A20D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopMarkPagesForDpcData(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    v_r12 = 0;
loc_005A1CB8:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10636738))))) goto loc_005A1F06;
    if (*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) == 0) goto loc_005A1EFE;
    result = (unsigned int)(*(unsigned int *)(v_rip + 10636738));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 36520) != 0) {
        a3 = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 14556);
        a1 = a1;
        result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 36520), a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 33560) != 0) {
        a3 = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 33572);
        a1 = a1;
        result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 33560), a3, a4);
        v_rbx = (unsigned int)(result);
    }
    v_rbp = 0;
loc_005A1D17:
    if (0 >= 2) goto loc_005A1DC7;
    result = (0) + (300);
    v_r14 = (result + result * 2) << (4);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8));
    result = MmAddRangeToCrashDump(a1, v_r14, 48, a4);
    if (sign_flag) goto loc_005A20B7;
    if (*(unsigned __int64 *)(v_r14 + 32) == 0) goto loc_005A1D7F;
    a2 = 0;
    result = MmIsAddressValidEx(*(unsigned __int64 *)(v_r14 + 32), a2, 48, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005A1D7F;
loc_005A1D6D:
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(v_r14 + 32), v_rbx + 64, a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1D7F:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_005A1DC0;
    a2 = 0;
    result = MmIsAddressValidEx(*(unsigned __int64 *)(v_r14), a2, v_rbx + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005A1DC0;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(v_r14) - 8, v_rbx + 64, a4);
    if (sign_flag) goto loc_005A20B7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14) + 48)) == 1) goto loc_005A1D7F;
    goto loc_005A1D6D;
loc_005A1DC0:
    v_rbp = (unsigned int)((v_rbp) + 1);
    goto loc_005A1D17;
loc_005A1DC7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 14496) == 0) goto loc_005A1DEF;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 14496)) - ((unsigned int)(*(unsigned int *)(v_rip + 10630138)));
    result = MmAddRangeToCrashDump(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 10630138)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1DEF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 34664) == 0) goto loc_005A1E17;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 34664)) - ((unsigned int)(*(unsigned int *)(v_rip + 10629754)));
    result = MmAddRangeToCrashDump(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 10629754)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1E17:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8817559)))) & (1)) == 0) goto loc_005A1EFE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 36824) == 0) goto loc_005A1E4D;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) + 36824)) - ((unsigned int)(*(unsigned int *)(v_rip + 10629668)));
    result = MmAddRangeToCrashDump(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 10629668)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1E4D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376) == 0) goto loc_005A1EFE;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376), 104, a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1E7A:
    if (1 > 4) goto loc_005A1EFE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376) + 1 * 8 + 28) == 0) goto loc_005A1EF7;
    if ((*(unsigned __int8 *)(v_rip + 12974503)) == 0) goto loc_005A1EDB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376) + 1 * 8 + 28) + 8)) == 0) goto loc_005A1EDB;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376) + 1 * 8 + 28), 48, a4);
    if (sign_flag) goto loc_005A20B7;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376) + 1 * 8 + 28) + 8), 32, a4);
    if (sign_flag) goto loc_005A20B7;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10645362 + v_r12 * 8) - 376) + 1 * 8 + 28) + 8)) + (32);
loc_005A1EDB:
    a2 = (a2) - ((unsigned int)(*(unsigned int *)(v_rip + 10629502)));
    result = MmAddRangeToCrashDump(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 10629502)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1EF7:
    v_rbp = (unsigned int)((1) + 1);
    goto loc_005A1E7A;
loc_005A1EFE:
    v_r12 = (unsigned int)((v_r12) + 1);
    goto loc_005A1CB8;
loc_005A1F06:
    if ((*(unsigned int *)(v_rip + 9891379)) <= 0) goto loc_005A20B5;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8817307)))) & (1)) == 0) goto loc_005A20B5;
    v_r12 = 0;
loc_005A1F2B:
    if ((*(unsigned __int64 *)(v_rip + 9891368)) == (v_rip + 9891358)) goto loc_005A20B5;
    a2 = 0;
    result = MmIsAddressValidEx(*(unsigned __int64 *)(v_rip + 9891368), a2, (unsigned int)(*(unsigned int *)(v_rip + 10629502)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_005A20B5;
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((unsigned int)(v_r12)) > (*(unsigned int *)(v_rip + 9891305))) goto loc_005A20B5;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(v_rip + 9891368), 224, a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1F80:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16)) == (*(unsigned __int64 *)(v_rip + 9891368) + 16)) goto loc_005A20AD;
    a2 = 0;
    result = MmIsAddressValidEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16), a2, 224, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005A20AD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16))) goto loc_005A20B5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16))) goto loc_005A20B5;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16), 152, a4);
    if (sign_flag) goto loc_005A20B7;
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 24))) << (3);
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32), a3, a4);
    if (sign_flag) goto loc_005A20B7;
    v_rbp = 0;
loc_005A1FEE:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 24))) goto loc_005A20A5;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8), 288, a4);
    if (sign_flag) goto loc_005A20B7;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) == 0) goto loc_005A209E;
    a2 = 0;
    result = MmIsAddressValidEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8), a2, 288, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005A209E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) + 24) == 0) goto loc_005A2054;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) + 24), (unsigned int)(0x1000ULL), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A2054:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) + 32) == 0) goto loc_005A2079;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) + 32), (unsigned int)(0x1000ULL), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A2079:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) + 48) == 0) goto loc_005A209E;
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891368) + 16) + 32) + v_rbp * 8) + 48), (unsigned int)(0x1000ULL), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A209E:
    v_rbp = (unsigned int)((v_rbp) + 1);
    goto loc_005A1FEE;
loc_005A20A5:
    goto loc_005A1F80;
loc_005A20AD:
    goto loc_005A1F2B;
loc_005A20B5:
loc_005A20B7:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t IopMarkPagesForDpcData(int64_t Arg1)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    local_r12 = 0;
loc_005A1CB8:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA24DC2))))) goto loc_005A1F06;
    if (*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) == 0) goto loc_005A1EFE;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA24DC2));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8EA8) != 0) {
        a3 = *(uint32_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x38DC);
        Arg1 = Arg1;
        result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8EA8), a3, a4);
        local_rbx = (uint32_t)(result);
    }
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8318) != 0) {
        a3 = *(uint32_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8324);
        Arg1 = Arg1;
        result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8318), a3, a4);
        local_rbx = (uint32_t)(result);
    }
    local_rbp = 0;
loc_005A1D17:
    if (0 >= 2) goto loc_005A1DC7;
    result = (0) + (300);
    local_r14 = (result + result * 2) << (4);
    local_r14 = (local_r14) + (*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8));
    result = MmAddRangeToCrashDump(Arg1, local_r14, 48, a4);
    if (sign_flag) goto loc_005A20B7;
    if (*(uint64_t *)(local_r14 + 0x20) == 0) goto loc_005A1D7F;
    a2 = 0;
    result = MmIsAddressValidEx(*(uint64_t *)(local_r14 + 0x20), a2, 48, a4);
    if ((uint8_t)(result) == 0) goto loc_005A1D7F;
loc_005A1D6D:
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(local_r14 + 0x20), local_rbx + 64, a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1D7F:
    if (*(uint64_t *)(local_r14) == 0) goto loc_005A1DC0;
    a2 = 0;
    result = MmIsAddressValidEx(*(uint64_t *)(local_r14), a2, local_rbx + 64, a4);
    if ((uint8_t)(result) == 0) goto loc_005A1DC0;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(local_r14) - 8, local_rbx + 64, a4);
    if (sign_flag) goto loc_005A20B7;
    if ((*(uint64_t *)(*(uint64_t *)(local_r14) + 0x30)) == 1) goto loc_005A1D7F;
    goto loc_005A1D6D;
loc_005A1DC0:
    local_rbp = (uint32_t)((local_rbp) + 1);
    goto loc_005A1D17;
loc_005A1DC7:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x38A0) == 0) goto loc_005A1DEF;
    a2 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x38A0)) - ((uint32_t)(*(uint32_t *)(v_rip + 0xA233FA)));
    result = MmAddRangeToCrashDump(Arg1, a2, (uint32_t)(*(uint32_t *)(v_rip + 0xA233FA)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1DEF:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8768) == 0) goto loc_005A1E17;
    a2 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8768)) - ((uint32_t)(*(uint32_t *)(v_rip + 0xA2327A)));
    result = MmAddRangeToCrashDump(Arg1, a2, (uint32_t)(*(uint32_t *)(v_rip + 0xA2327A)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1E17:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x868B97)))) & (1)) == 0) goto loc_005A1EFE;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8FD8) == 0) goto loc_005A1E4D;
    a2 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) + 0x8FD8)) - ((uint32_t)(*(uint32_t *)(v_rip + 0xA23224)));
    result = MmAddRangeToCrashDump(Arg1, a2, (uint32_t)(*(uint32_t *)(v_rip + 0xA23224)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1E4D:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178) == 0) goto loc_005A1EFE;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178), 104, a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1E7A:
    if (1 > 4) goto loc_005A1EFE;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178) + 0x1 * 8 + 0x1C) == 0) goto loc_005A1EF7;
    if ((*(uint8_t *)(v_rip + 0xC5F9A7)) == 0) goto loc_005A1EDB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178) + 0x1 * 8 + 0x1C) + 0x8)) == 0) goto loc_005A1EDB;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178) + 0x1 * 8 + 0x1C), 48, a4);
    if (sign_flag) goto loc_005A20B7;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178) + 0x1 * 8 + 0x1C) + 0x8), 32, a4);
    if (sign_flag) goto loc_005A20B7;
    a2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA26F72 + local_r12 * 8) - 0x178) + 0x1 * 8 + 0x1C) + 0x8)) + (32);
loc_005A1EDB:
    a2 = (a2) - ((uint32_t)(*(uint32_t *)(v_rip + 0xA2317E)));
    result = MmAddRangeToCrashDump(Arg1, a2, (uint32_t)(*(uint32_t *)(v_rip + 0xA2317E)), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1EF7:
    local_rbp = (uint32_t)((1) + 1);
    goto loc_005A1E7A;
loc_005A1EFE:
    local_r12 = (uint32_t)((local_r12) + 1);
    goto loc_005A1CB8;
loc_005A1F06:
    if ((*(uint32_t *)(v_rip + 0x96EE33)) <= 0) goto loc_005A20B5;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x868A9B)))) & (1)) == 0) goto loc_005A20B5;
    local_r12 = 0;
loc_005A1F2B:
    if ((*(uint64_t *)(v_rip + 0x96EE28)) == (v_rip + 9891358)) goto loc_005A20B5;
    a2 = 0;
    result = MmIsAddressValidEx(*(uint64_t *)(v_rip + 0x96EE28), a2, (uint32_t)(*(uint32_t *)(v_rip + 0xA2317E)), a4);
    if ((uint8_t)(result) == 0) goto loc_005A20B5;
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((uint32_t)(local_r12)) > (*(uint32_t *)(v_rip + 0x96EDE9))) goto loc_005A20B5;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(v_rip + 0x96EE28), 224, a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A1F80:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10)) == (*(uint64_t *)(v_rip + 0x96EE28) + 16)) goto loc_005A20AD;
    a2 = 0;
    result = MmIsAddressValidEx(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10), a2, 224, a4);
    if ((uint8_t)(result) == 0) goto loc_005A20AD;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10))) goto loc_005A20B5;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10))) goto loc_005A20B5;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10), 152, a4);
    if (sign_flag) goto loc_005A20B7;
    a3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x18))) << (3);
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20), a3, a4);
    if (sign_flag) goto loc_005A20B7;
    local_rbp = 0;
loc_005A1FEE:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x18))) goto loc_005A20A5;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8), 288, a4);
    if (sign_flag) goto loc_005A20B7;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) == 0) goto loc_005A209E;
    a2 = 0;
    result = MmIsAddressValidEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8), a2, 288, a4);
    if ((uint8_t)(result) == 0) goto loc_005A209E;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) + 0x18) == 0) goto loc_005A2054;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) + 0x18), (uint32_t)(0x1000ULL), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A2054:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) + 0x20) == 0) goto loc_005A2079;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) + 0x20), (uint32_t)(0x1000ULL), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A2079:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) + 0x30) == 0) goto loc_005A209E;
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96EE28) + 0x10) + 0x20) + local_rbp * 8) + 0x30), (uint32_t)(0x1000ULL), a4);
    if (sign_flag) goto loc_005A20B7;
loc_005A209E:
    local_rbp = (uint32_t)((local_rbp) + 1);
    goto loc_005A1FEE;
loc_005A20A5:
    goto loc_005A1F80;
loc_005A20AD:
    goto loc_005A1F2B;
loc_005A20B5:
loc_005A20B7:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A1C90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
