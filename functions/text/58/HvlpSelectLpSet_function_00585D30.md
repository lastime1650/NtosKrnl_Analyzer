# HvlpSelectLpSet

- RVA: `0x00585D30`–`0x00586166` (길이 `1,078` bytes)
- VA: `0x0000000140585D30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C65C8`
- 디코드: `303`개 명령, `1,078/1,078` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x00585DEA` → [HviGetImplementationLimits](../66/HviGetImplementationLimits_function_00666708.md) (function, `0x00666708`)
- `0x00585E45` → [HalEnumerateProcessors](../54/HalEnumerateProcessors_function_00543240.md) (function, `0x00543240`)
- `0x00585E73` → [HvlpQueryApicIdAndNumaNode](HvlpQueryApicIdAndNumaNode_function_00585C60.md) (function, `0x00585C60`)
- `0x00585EB4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00585ED0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00586043` → [HvlpComputeLpComparisonMetrics](HvlpComputeLpComparisonMetrics_function_005852E4.md) (function, `0x005852E4`)
- `0x0058608A` → [HvlpLpComparison](HvlpLpComparison_function_00585AF8.md) (function, `0x00585AF8`)
- `0x00586142` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvlStartBootLogicalProcessors](HvlStartBootLogicalProcessors_function_00584E18.md) at `0x00585025`

### Static image references
- `0x00585D4F` → RVA `0x00E0A740` (`.data`; read)
- `0x00585D5D` → RVA `0x00FC6AD8` (`ALMOSTRO`; read)
- `0x00585D90` → RVA `0x00FC6D54` (`ALMOSTRO`; write)
- `0x00585D97` → RVA `0x00FC6BC0` (`ALMOSTRO`; write)
- `0x00585D9E` → RVA `0x00FC6B90` (`ALMOSTRO`; write)
- `0x00585DA5` → RVA `0x00FC6C90` (`ALMOSTRO`; write)
- `0x00585DAC` → RVA `0x00FC6C8C` (`ALMOSTRO`; write)
- `0x00585DB3` → RVA `0x00FC6AA7` (`ALMOSTRO`; write)
- `0x00585E16` → RVA `0x00FC6BC0` (`ALMOSTRO`; read)
- `0x00585E34` → RVA `0x00FC6B90` (`ALMOSTRO`; read)
- `0x00585E3F` → RVA `0x00FC6C68` (`ALMOSTRO`; read)
- `0x00585E97` → RVA `0x00FC7098` (`ALMOSTRO`; read)
- `0x00585EBD` → RVA `0x00FC7088` (`ALMOSTRO`; read)
- `0x00585F39` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00585F46` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x00585F71` → RVA `0x00FC6CF4` (`ALMOSTRO`; read)
- `0x00585F80` → RVA `0x00FC6C94` (`ALMOSTRO`; read)
- `0x00585F8F` → RVA `0x00FC6D54` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00585D30  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00585D35  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00585D3A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00585D3F  55                              push rbp
00585D40  41 54                           push r12
00585D42  41 55                           push r13
00585D44  41 56                           push r14
00585D46  41 57                           push r15
00585D48  48 8B EC                        mov rbp, rsp
00585D4B  48 83 EC 60                     sub rsp, 0x60
00585D4F  48 8B 05 EA 49 88 00            mov rax, qword ptr [rip + 0x8849ea]
00585D56  48 33 C4                        xor rax, rsp
00585D59  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00585D5D  8B 05 75 0D A4 00               mov eax, dword ptr [rip + 0xa40d75]
00585D63  45 33 E4                        xor r12d, r12d
00585D66  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
00585D6A  0F 57 C0                        xorps xmm0, xmm0
00585D6D  66 44 89 65 C0                  mov word ptr [rbp - 0x40], r12w
00585D72  48 8B F2                        mov rsi, rdx
00585D75  44 89 65 D0                     mov dword ptr [rbp - 0x30], r12d
00585D79  8B F9                           mov edi, ecx
00585D7B  66 44 89 65 C4                  mov word ptr [rbp - 0x3c], r12w
00585D80  44 89 65 D8                     mov dword ptr [rbp - 0x28], r12d
00585D84  44 89 65 CC                     mov dword ptr [rbp - 0x34], r12d
00585D88  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00585D8C  A8 01                           test al, 1
00585D8E  75 2A                           jne 0x140585dba
00585D90  44 89 25 BD 0F A4 00            mov dword ptr [rip + 0xa40fbd], r12d
00585D97  44 89 25 22 0E A4 00            mov dword ptr [rip + 0xa40e22], r12d
00585D9E  44 89 25 EB 0D A4 00            mov dword ptr [rip + 0xa40deb], r12d
00585DA5  44 89 25 E4 0E A4 00            mov dword ptr [rip + 0xa40ee4], r12d
00585DAC  44 89 25 D9 0E A4 00            mov dword ptr [rip + 0xa40ed9], r12d
00585DB3  44 88 25 ED 0C A4 00            mov byte ptr [rip + 0xa40ced], r12b
00585DBA  0F BA E0 0B                     bt eax, 0xb
00585DBE  73 26                           jae 0x140585de6
00585DC0  44 89 25 F9 0D A4 00            mov dword ptr [rip + 0xa40df9], r12d
00585DC7  44 89 25 C2 0D A4 00            mov dword ptr [rip + 0xa40dc2], r12d
00585DCE  44 89 25 BB 0E A4 00            mov dword ptr [rip + 0xa40ebb], r12d
00585DD5  C7 05 AD 0E A4 00 01 00 00 00   mov dword ptr [rip + 0xa40ead], 1
00585DDF  44 88 25 C1 0C A4 00            mov byte ptr [rip + 0xa40cc1], r12b
00585DE6  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00585DEA  E8 19 09 0E 00                  call 0x140666708
00585DEF  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00585DF8  41 BF 40 00 00 00               mov r15d, 0x40
00585DFE  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00585E07  44 8B A8 A0 00 00 00            mov r13d, dword ptr [rax + 0xa0]
00585E0E  44 0F AF A9 A4 00 00 00         imul r13d, dword ptr [rcx + 0xa4]
00585E16  8B 05 A4 0D A4 00               mov eax, dword ptr [rip + 0xa40da4]
00585E1C  41 FF CD                        dec r13d
00585E1F  44 39 7D E8                     cmp dword ptr [rbp - 0x18], r15d
00585E23  41 F7 D5                        not r13d
00585E26  44 0F 42 7D E8                  cmovb r15d, dword ptr [rbp - 0x18]
00585E2B  85 C0                           test eax, eax
00585E2D  74 10                           je 0x140585e3f
00585E2F  41 3B C7                        cmp eax, r15d
00585E32  73 0B                           jae 0x140585e3f
00585E34  44 39 25 55 0D A4 00            cmp dword ptr [rip + 0xa40d55], r12d
00585E3B  44 0F 44 F8                     cmove r15d, eax
00585E3F  8B 0D 23 0E A4 00               mov ecx, dword ptr [rip + 0xa40e23]
00585E45  E8 F6 D3 FB FF                  call 0x140543240
00585E4A  89 45 DC                        mov dword ptr [rbp - 0x24], eax
00585E4D  45 8B F4                        mov r14d, r12d
00585E50  44 3B F7                        cmp r14d, edi
00585E53  0F 83 9A 00 00 00               jae 0x140585ef3
00585E59  41 8B C6                        mov eax, r14d
00585E5C  48 8D 56 04                     lea rdx, [rsi + 4]
00585E60  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00585E64  41 8B CE                        mov ecx, r14d
00585E67  48 8D 1C 80                     lea rbx, [rax + rax*4]
00585E6B  48 8D 14 DA                     lea rdx, [rdx + rbx*8]
00585E6F  C6 04 DE 01                     mov byte ptr [rsi + rbx*8], 1
00585E73  E8 E8 FD FF FF                  call 0x140585c60
00585E78  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00585E7B  44 8B E0                        mov r12d, eax
00585E7E  3D 25 02 00 C0                  cmp eax, 0xc0000225
00585E83  75 0A                           jne 0x140585e8f
00585E85  33 C0                           xor eax, eax
00585E87  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00585E8A  88 04 DE                        mov byte ptr [rsi + rbx*8], al
00585E8D  EB 5C                           jmp 0x140585eeb
00585E8F  85 C0                           test eax, eax
00585E91  0F 88 A1 02 00 00               js 0x140586138
00585E97  48 8B 05 FA 11 A4 00            mov rax, qword ptr [rip + 0xa411fa]
00585E9E  0F B7 4D C0                     movzx ecx, word ptr [rbp - 0x40]
00585EA2  66 89 4C DE 08                  mov word ptr [rsi + rbx*8 + 8], cx
00585EA7  48 85 C0                        test rax, rax
00585EAA  74 35                           je 0x140585ee1
00585EAC  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00585EB0  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00585EB4  E8 17 4C 13 00                  call 0x1406baad0
00585EB9  85 C0                           test eax, eax
00585EBB  78 20                           js 0x140585edd
00585EBD  48 8B 05 C4 11 A4 00            mov rax, qword ptr [rip + 0xa411c4]
00585EC4  48 85 C0                        test rax, rax
00585EC7  74 14                           je 0x140585edd
00585EC9  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00585ECC  48 8D 55 C4                     lea rdx, [rbp - 0x3c]
00585ED0  E8 FB 4B 13 00                  call 0x1406baad0
00585ED5  0F B7 4D C4                     movzx ecx, word ptr [rbp - 0x3c]
00585ED9  85 C0                           test eax, eax
00585EDB  79 04                           jns 0x140585ee1
00585EDD  0F B7 4D C0                     movzx ecx, word ptr [rbp - 0x40]
00585EE1  66 89 4C DE 0A                  mov word ptr [rsi + rbx*8 + 0xa], cx
00585EE6  66 89 4C DE 0C                  mov word ptr [rsi + rbx*8 + 0xc], cx
00585EEB  41 FF C6                        inc r14d
00585EEE  E9 5D FF FF FF                  jmp 0x140585e50
00585EF3  41 BC 01 00 00 00               mov r12d, 1
00585EF9  48 8D 5E 01                     lea rbx, [rsi + 1]
00585EFD  C6 03 01                        mov byte ptr [rbx], 1
00585F00  45 8B DC                        mov r11d, r12d
00585F03  44 89 65 C8                     mov dword ptr [rbp - 0x38], r12d
00585F07  45 8B F4                        mov r14d, r12d
00585F0A  44 89 75 D4                     mov dword ptr [rbp - 0x2c], r14d
00585F0E  45 33 D2                        xor r10d, r10d
00585F11  85 FF                           test edi, edi
00585F13  0F 84 09 01 00 00               je 0x140586022
00585F19  4C 8B C6                        mov r8, rsi
00585F1C  8B 75 DC                        mov esi, dword ptr [rbp - 0x24]
00585F1F  41 80 38 00                     cmp byte ptr [r8], 0
00585F23  0F 84 CF 00 00 00               je 0x140585ff8
00585F29  41 80 78 01 00                  cmp byte ptr [r8 + 1], 0
00585F2E  0F 85 C0 00 00 00               jne 0x140585ff4
00585F34  41 0F B7 50 08                  movzx edx, word ptr [r8 + 8]
00585F39  66 3B 15 C0 F0 A3 00            cmp dx, word ptr [rip + 0xa3f0c0]
00585F40  0F 83 AE 00 00 00               jae 0x140585ff4
00585F46  48 8D 0D 73 97 A4 00            lea rcx, [rip + 0xa49773]
00585F4D  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00585F51  F6 40 0A 02                     test byte ptr [rax + 0xa], 2
00585F55  0F 84 99 00 00 00               je 0x140585ff4
00585F5B  41 81 FC 00 08 00 00            cmp r12d, 0x800
00585F62  0F 84 8C 00 00 00               je 0x140585ff4
00585F68  44 3B E6                        cmp r12d, esi
00585F6B  0F 84 83 00 00 00               je 0x140585ff4
00585F71  8B 05 7D 0D A4 00               mov eax, dword ptr [rip + 0xa40d7d]
00585F77  85 C0                           test eax, eax
00585F79  74 05                           je 0x140585f80
00585F7B  44 3B E0                        cmp r12d, eax
00585F7E  74 74                           je 0x140585ff4
00585F80  8B 05 0E 0D A4 00               mov eax, dword ptr [rip + 0xa40d0e]
00585F86  85 C0                           test eax, eax
00585F88  74 05                           je 0x140585f8f
00585F8A  44 3B D0                        cmp r10d, eax
00585F8D  73 65                           jae 0x140585ff4
00585F8F  8B 05 BF 0D A4 00               mov eax, dword ptr [rip + 0xa40dbf]
00585F95  85 C0                           test eax, eax
00585F97  74 05                           je 0x140585f9e
00585F99  44 3B E0                        cmp r12d, eax
00585F9C  74 56                           je 0x140585ff4
00585F9E  45 3B F7                        cmp r14d, r15d
00585FA1  75 1E                           jne 0x140585fc1
00585FA3  33 C9                           xor ecx, ecx
00585FA5  48 8B C3                        mov rax, rbx
00585FA8  66 39 50 07                     cmp word ptr [rax + 7], dx
00585FAC  75 05                           jne 0x140585fb3
00585FAE  80 38 00                        cmp byte ptr [rax], 0
00585FB1  75 0A                           jne 0x140585fbd
00585FB3  FF C1                           inc ecx
00585FB5  48 83 C0 28                     add rax, 0x28
00585FB9  3B CF                           cmp ecx, edi
00585FBB  72 EB                           jb 0x140585fa8
00585FBD  3B CF                           cmp ecx, edi
00585FBF  74 33                           je 0x140585ff4
00585FC1  44 3B 1D A0 0C A4 00            cmp r11d, dword ptr [rip + 0xa40ca0]
00585FC8  75 2E                           jne 0x140585ff8
00585FCA  45 8B 48 04                     mov r9d, dword ptr [r8 + 4]
00585FCE  48 8B CB                        mov rcx, rbx
00585FD1  45 23 CD                        and r9d, r13d
00585FD4  33 D2                           xor edx, edx
00585FD6  8B 41 03                        mov eax, dword ptr [rcx + 3]
00585FD9  41 23 C5                        and eax, r13d
00585FDC  44 3B C8                        cmp r9d, eax
00585FDF  75 05                           jne 0x140585fe6
00585FE1  80 39 00                        cmp byte ptr [rcx], 0
00585FE4  75 0A                           jne 0x140585ff0
00585FE6  FF C2                           inc edx
00585FE8  48 83 C1 28                     add rcx, 0x28
00585FEC  3B D7                           cmp edx, edi
00585FEE  72 E6                           jb 0x140585fd6
00585FF0  3B D7                           cmp edx, edi
00585FF2  75 04                           jne 0x140585ff8
00585FF4  41 C6 00 00                     mov byte ptr [r8], 0
00585FF8  41 FF C2                        inc r10d
00585FFB  49 83 C0 28                     add r8, 0x28
00585FFF  44 3B D7                        cmp r10d, edi
00586002  0F 82 17 FF FF FF               jb 0x140585f1f
00586008  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
0058600C  33 C0                           xor eax, eax
0058600E  48 8B CE                        mov rcx, rsi
00586011  80 39 00                        cmp byte ptr [rcx], 0
00586014  75 0E                           jne 0x140586024
00586016  FF C0                           inc eax
00586018  48 83 C1 28                     add rcx, 0x28
0058601C  3B C7                           cmp eax, edi
0058601E  72 F1                           jb 0x140586011
00586020  EB 02                           jmp 0x140586024
00586022  33 C0                           xor eax, eax
00586024  3B C7                           cmp eax, edi
00586026  0F 84 08 01 00 00               je 0x140586134
0058602C  33 DB                           xor ebx, ebx
0058602E  85 FF                           test edi, edi
00586030  74 24                           je 0x140586056
00586032  4C 8B F6                        mov r14, rsi
00586035  41 80 3E 00                     cmp byte ptr [r14], 0
00586039  74 0D                           je 0x140586048
0058603B  44 8B C3                        mov r8d, ebx
0058603E  48 8B D6                        mov rdx, rsi
00586041  8B CF                           mov ecx, edi
00586043  E8 9C F2 FF FF                  call 0x1405852e4
00586048  FF C3                           inc ebx
0058604A  49 83 C6 28                     add r14, 0x28
0058604E  3B DF                           cmp ebx, edi
00586050  72 E3                           jb 0x140586035
00586052  44 8B 75 D4                     mov r14d, dword ptr [rbp - 0x2c]
00586056  41 83 C9 FF                     or r9d, 0xffffffff
0058605A  33 D2                           xor edx, edx
0058605C  3B D7                           cmp edx, edi
0058605E  73 11                           jae 0x140586071
00586060  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
00586064  80 3C CE 00                     cmp byte ptr [rsi + rcx*8], 0
00586068  75 04                           jne 0x14058606e
0058606A  FF C2                           inc edx
0058606C  EB EE                           jmp 0x14058605c
0058606E  44 8B CA                        mov r9d, edx
00586071  45 8D 41 01                     lea r8d, [r9 + 1]
00586075  44 3B C7                        cmp r8d, edi
00586078  73 28                           jae 0x1405860a2
0058607A  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
0058607E  48 8D 1C CE                     lea rbx, [rsi + rcx*8]
00586082  80 3B 00                        cmp byte ptr [rbx], 0
00586085  74 0F                           je 0x140586096
00586087  48 8B D6                        mov rdx, rsi
0058608A  E8 69 FA FF FF                  call 0x140585af8
0058608F  83 F8 FF                        cmp eax, -1
00586092  45 0F 44 C8                     cmove r9d, r8d
00586096  41 FF C0                        inc r8d
00586099  48 83 C3 28                     add rbx, 0x28
0058609D  44 3B C7                        cmp r8d, edi
005860A0  72 E0                           jb 0x140586082
005860A2  41 8B C1                        mov eax, r9d
005860A5  41 FF C4                        inc r12d
005860A8  33 C9                           xor ecx, ecx
005860AA  4C 8D 14 80                     lea r10, [rax + rax*4]
005860AE  46 8B 44 D6 04                  mov r8d, dword ptr [rsi + r10*8 + 4]
005860B3  45 23 C5                        and r8d, r13d
005860B6  42 C6 44 D6 01 01               mov byte ptr [rsi + r10*8 + 1], 1
005860BC  85 FF                           test edi, edi
005860BE  74 23                           je 0x1405860e3
005860C0  48 8D 56 04                     lea rdx, [rsi + 4]
005860C4  41 3B C9                        cmp ecx, r9d
005860C7  74 10                           je 0x1405860d9
005860C9  80 7A FD 00                     cmp byte ptr [rdx - 3], 0
005860CD  74 0A                           je 0x1405860d9
005860CF  8B 02                           mov eax, dword ptr [rdx]
005860D1  41 23 C5                        and eax, r13d
005860D4  41 3B C0                        cmp eax, r8d
005860D7  74 0A                           je 0x1405860e3
005860D9  FF C1                           inc ecx
005860DB  48 83 C2 28                     add rdx, 0x28
005860DF  3B CF                           cmp ecx, edi
005860E1  72 E1                           jb 0x1405860c4
005860E3  44 8B 5D C8                     mov r11d, dword ptr [rbp - 0x38]
005860E7  3B CF                           cmp ecx, edi
005860E9  75 07                           jne 0x1405860f2
005860EB  41 FF C3                        inc r11d
005860EE  44 89 5D C8                     mov dword ptr [rbp - 0x38], r11d
005860F2  33 C9                           xor ecx, ecx
005860F4  85 FF                           test edi, edi
005860F6  74 24                           je 0x14058611c
005860F8  48 8D 56 08                     lea rdx, [rsi + 8]
005860FC  41 3B C9                        cmp ecx, r9d
005860FF  74 11                           je 0x140586112
00586101  80 7A F9 00                     cmp byte ptr [rdx - 7], 0
00586105  74 0B                           je 0x140586112
00586107  42 0F B7 44 D6 08               movzx eax, word ptr [rsi + r10*8 + 8]
0058610D  66 39 02                        cmp word ptr [rdx], ax
00586110  74 0A                           je 0x14058611c
00586112  FF C1                           inc ecx
00586114  48 83 C2 28                     add rdx, 0x28
00586118  3B CF                           cmp ecx, edi
0058611A  72 E0                           jb 0x1405860fc
0058611C  48 8D 5E 01                     lea rbx, [rsi + 1]
00586120  3B CF                           cmp ecx, edi
00586122  0F 85 E6 FD FF FF               jne 0x140585f0e
00586128  41 FF C6                        inc r14d
0058612B  48 8D 5E 01                     lea rbx, [rsi + 1]
0058612F  E9 D6 FD FF FF                  jmp 0x140585f0a
00586134  44 8B 65 CC                     mov r12d, dword ptr [rbp - 0x34]
00586138  41 8B C4                        mov eax, r12d
0058613B  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
0058613F  48 33 CC                        xor rcx, rsp
00586142  E8 F9 64 12 00                  call 0x1406ac640
00586147  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0058614C  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00586150  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00586154  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00586158  49 8B E3                        mov rsp, r11
0058615B  41 5F                           pop r15
0058615D  41 5E                           pop r14
0058615F  41 5D                           pop r13
00586161  41 5C                           pop r12
00586163  5D                              pop rbp
00586164  C3                              ret
00586165  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpSelectLpSet(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int16 v_stack_m64;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 8931818)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r12 = 0;
    v_stack_m48 = a2;
    v_stack_m68 = 0;
    v_stack_m58 = 0;
    v_stack_m64 = 0;
    v_stack_m50 = 0;
    v_stack_m5C = 0;
    v_stack_m40 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10751349)))) & (1)) == 0) {
        *(unsigned int *)(v_rip + 10751933) = 0;
        *(unsigned int *)(v_rip + 10751522) = 0;
        *(unsigned int *)(v_rip + 10751467) = 0;
        *(unsigned int *)(v_rip + 10751716) = 0;
        *(unsigned int *)(v_rip + 10751705) = 0;
        *(unsigned __int8 *)(v_rip + 10751213) = 0;
    }
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(v_rip + 10751481) = 0;
        *(unsigned int *)(v_rip + 10751426) = 0;
        *(unsigned int *)(v_rip + 10751675) = 0;
        *(unsigned int *)(v_rip + 10751661) = 1;
        *(unsigned __int8 *)(v_rip + 10751169) = 0;
    }
    result = HviGetImplementationLimits(v_stack_m40, a2, a3, a4);
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 160))) * (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 164)));
    v_r13 = (unsigned int)((v_r13) - 1);
    v_r13 = (unsigned int)(~(v_r13));
    v_r15 = 64;
    if (v_stack_m40 < 64) { v_r15 = v_stack_m40; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751396))) == 0) goto loc_00585E3F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751396)))) < ((unsigned int)(v_r15))) {
        if ((*(unsigned int *)(v_rip + 10751317)) == 0) { v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751396))); }
    }
    result = HalEnumerateProcessors((unsigned int)(*(unsigned int *)(v_rip + 10751523)), a2, a3, a4);
    v_stack_m4C = (unsigned int)(result);
loc_00585E50:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_00585EF3;
    *(unsigned __int8 *)(a2 + 0 + 0 * 4 * 8) = 1;
    result = HvlpQueryApicIdAndNumaNode(0, a2 + 4 + 0 + 0 * 4 * 8, v_stack_m68, a4);
    v_stack_m5C = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00585E8F;
    result = 0;
    v_stack_m5C = 0;
    *(unsigned __int8 *)(a2 + 0 + 0 * 4 * 8) = 0;
    goto loc_00585EEB;
loc_00585E8F:
    if (sign_flag) goto loc_00586138;
    *(unsigned __int16 *)(a2 + 0 + 0 * 4 * 8 + 8) = (unsigned __int16)(v_stack_m68);
    if (*(unsigned __int64 *)(v_rip + 10752506) == 0) goto loc_00585EE1;
    result = guard_dispatch_icall(v_stack_m68, v_stack_m50, v_stack_m58, a4);
    if (sign_flag) goto loc_00585EDD;
    if (*(unsigned __int64 *)(v_rip + 10752452) == 0) goto loc_00585EDD;
    result = guard_dispatch_icall((unsigned int)(v_stack_m58), v_stack_m64, v_stack_m58, a4);
    if (sign_flag) {
        a1 = v_stack_m68;
    }
    *(unsigned __int16 *)(a2 + 0 + 0 * 4 * 8 + 10) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(a2 + 0 + 0 * 4 * 8 + 12) = (unsigned __int16)(a1);
loc_00585EEB:
    v_r14 = (unsigned int)((0) + 1);
    goto loc_00585E50;
loc_00585EF3:
    *(unsigned __int8 *)(a2 + 1) = 1;
    v_stack_m60 = 1;
loc_00585F0A:
    v_stack_m54 = 1;
loc_00585F0E:
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00586022;
loc_00585F1F:
    if ((*(unsigned __int8 *)(a2)) == 0) goto loc_00585FF8;
    if ((*(unsigned __int8 *)(a2 + 1)) != 0) goto loc_00585FF4;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 8))) >= (*(unsigned __int16 *)(v_rip + 10744000))) goto loc_00585FF4;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 10786675 + *(unsigned __int16 *)(a2 + 8) * 8) + 10)) & (2)) == 0) goto loc_00585FF4;
    if (1 == 0x800ULL) goto loc_00585FF4;
    if (1 == ((unsigned int)((unsigned int)(v_stack_m4C)))) goto loc_00585FF4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751357))) == 0) goto loc_00585F80;
    if (1 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751357))))) goto loc_00585FF4;
loc_00585F80:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751246))) == 0) goto loc_00585F8F;
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751246))))) goto loc_00585FF4;
loc_00585F8F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751423))) == 0) goto loc_00585F9E;
    if (1 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10751423))))) goto loc_00585FF4;
loc_00585F9E:
    if (1 != ((unsigned int)(v_r15))) goto loc_00585FC1;
    a1 = 0;
loc_00585FA8:
    if ((*(unsigned __int16 *)(a2 + 1 + 7)) != ((unsigned __int16)(*(unsigned __int16 *)(a2 + 8)))) goto loc_00585FB3;
    if ((*(unsigned __int8 *)(a2 + 1)) != 0) goto loc_00585FBD;
loc_00585FB3:
    a1 = (unsigned int)((a1) + 1);
    result = (a2 + 1) + (40);
    if (a1 < ((unsigned int)((unsigned int)(a1)))) goto loc_00585FA8;
loc_00585FBD:
    if (a1 == ((unsigned int)((unsigned int)(a1)))) goto loc_00585FF4;
loc_00585FC1:
    if (1 != (*(unsigned int *)(v_rip + 10751136))) goto loc_00585FF8;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) & ((unsigned int)(v_r13)));
    a2 = 0;
loc_00585FD6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 1 + 3))) & ((unsigned int)(v_r13)));
    if (((unsigned int)(a4)) != ((unsigned int)(result))) goto loc_00585FE6;
    if ((*(unsigned __int8 *)(a2 + 1)) != 0) goto loc_00585FF0;
loc_00585FE6:
    a2 = (unsigned int)((a2) + 1);
    a1 = (a2 + 1) + (40);
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00585FD6;
loc_00585FF0:
    if (((unsigned int)(a2)) == ((unsigned int)((unsigned int)(a1)))) {
        *(unsigned __int8 *)(a2) = 0;
    }
    v_r10 = (unsigned int)((v_r10) + 1);
    a3 = (a2) + (40);
    if (((unsigned int)(v_r10)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00585F1F;
    result = 0;
loc_00586011:
    if ((*(unsigned __int8 *)(v_stack_m48)) != 0) goto loc_00586024;
    result = (unsigned int)((result) + 1);
    a1 = (v_stack_m48) + (40);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00586011;
    goto loc_00586024;
loc_00586022:
    result = 0;
loc_00586024:
    if (0 == ((unsigned int)((unsigned int)(a1)))) goto loc_00586134;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00586056;
loc_00586035:
    if ((*(unsigned __int8 *)(v_stack_m48)) != 0) {
        a3 = 0;
        a2 = v_stack_m48;
        a1 = (unsigned int)((unsigned int)(a1));
        result = HvlpComputeLpComparisonMetrics(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((v_rbx) + 1);
    v_r14 = (v_stack_m48) + (40);
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00586035;
loc_00586056:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    a2 = 0;
loc_0058605C:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_00586071;
    if ((*(unsigned __int8 *)(v_stack_m48 + a2 + a2 * 4 * 8)) != 0) goto loc_0058606E;
    a2 = (unsigned int)((a2) + 1);
    goto loc_0058605C;
loc_0058606E:
loc_00586071:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)) + 1)) >= ((unsigned int)((unsigned int)(a1)))) goto loc_005860A2;
loc_00586082:
    if ((*(unsigned __int8 *)(v_stack_m48 + (unsigned int)((unsigned int)(a2)) + 1 + (unsigned int)((unsigned int)(a2)) + 1 * 4 * 8)) != 0) {
        a2 = v_stack_m48;
        result = HvlpLpComparison((unsigned int)((unsigned int)(a2)) + 1 + (unsigned int)((unsigned int)(a2)) + 1 * 4, a2, (unsigned int)((unsigned int)(a2)) + 1, (unsigned int)((unsigned int)(a2)));
        a4 = (unsigned int)((unsigned int)(a2));
        if (((unsigned int)(result)) == -1) { a4 = (unsigned int)((unsigned int)((unsigned int)(a2)) + 1); }
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2)) + 1) + 1);
    v_rbx = (v_stack_m48 + (unsigned int)((unsigned int)(a2)) + 1 + (unsigned int)((unsigned int)(a2)) + 1 * 4 * 8) + (40);
    if (((unsigned int)(a3)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00586082;
loc_005860A2:
    v_r12 = (unsigned int)((1) + 1);
    a1 = 0;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + (unsigned int)((unsigned int)(a4)) + (unsigned int)((unsigned int)(a4)) * 4 * 8 + 4))) & ((unsigned int)(v_r13)));
    *(unsigned __int8 *)(v_stack_m48 + (unsigned int)((unsigned int)(a4)) + (unsigned int)((unsigned int)(a4)) * 4 * 8 + 1) = 1;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_005860E3;
loc_005860C4:
    if (0 == ((unsigned int)(a4))) goto loc_005860D9;
    if ((*(unsigned __int8 *)(v_stack_m48 + 4 - 3)) == 0) goto loc_005860D9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 4))) & ((unsigned int)(v_r13)));
    if (((unsigned int)(result)) == ((unsigned int)(a3))) goto loc_005860E3;
loc_005860D9:
    a1 = (unsigned int)((a1) + 1);
    a2 = (v_stack_m48 + 4) + (40);
    if (a1 < ((unsigned int)((unsigned int)(a1)))) goto loc_005860C4;
loc_005860E3:
    v_r11 = (unsigned int)(v_stack_m60);
    if (a1 == ((unsigned int)((unsigned int)(a1)))) {
        v_r11 = (unsigned int)(((unsigned int)(v_stack_m60)) + 1);
        v_stack_m60 = (unsigned int)(v_r11);
    }
    a1 = 0;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_0058611C;
loc_005860FC:
    if (0 == ((unsigned int)(a4))) goto loc_00586112;
    if ((*(unsigned __int8 *)(v_stack_m48 + 8 - 7)) == 0) goto loc_00586112;
    if ((*(unsigned __int16 *)(v_stack_m48 + 8)) == ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m48 + (unsigned int)((unsigned int)(a4)) + (unsigned int)((unsigned int)(a4)) * 4 * 8 + 8)))) goto loc_0058611C;
loc_00586112:
    a1 = (unsigned int)((a1) + 1);
    a2 = (v_stack_m48 + 8) + (40);
    if (a1 < ((unsigned int)((unsigned int)(a1)))) goto loc_005860FC;
loc_0058611C:
    if (a1 != ((unsigned int)((unsigned int)(a1)))) goto loc_00585F0E;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m54)) + 1);
    goto loc_00585F0A;
loc_00586134:
loc_00586138:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpSelectLpSet(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint16_t v_stack_m64;
    uint16_t v_stack_m68;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x8849EA)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r12 = 0;
    v_stack_m48 = Arg2;
    v_stack_m68 = 0;
    v_stack_m58 = 0;
    v_stack_m64 = 0;
    v_stack_m50 = 0;
    v_stack_m5C = 0;
    v_stack_m40 = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40D75)))) & (1)) == 0) {
        *(uint32_t *)(v_rip + 0xA40FBD) = 0;
        *(uint32_t *)(v_rip + 0xA40E22) = 0;
        *(uint32_t *)(v_rip + 0xA40DEB) = 0;
        *(uint32_t *)(v_rip + 0xA40EE4) = 0;
        *(uint32_t *)(v_rip + 0xA40ED9) = 0;
        *(uint8_t *)(v_rip + 0xA40CED) = 0;
    }
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(v_rip + 0xA40DF9) = 0;
        *(uint32_t *)(v_rip + 0xA40DC2) = 0;
        *(uint32_t *)(v_rip + 0xA40EBB) = 0;
        *(uint32_t *)(v_rip + 0xA40EAD) = 1;
        *(uint8_t *)(v_rip + 0xA40CC1) = 0;
    }
    result = HviGetImplementationLimits(v_stack_m40, Arg2, a3, a4);
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA0))) * (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA4)));
    local_r13 = (uint32_t)((local_r13) - 1);
    local_r13 = (uint32_t)(~(local_r13));
    local_r15 = 64;
    if (v_stack_m40 < 64) { local_r15 = v_stack_m40; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40DA4))) == 0) goto loc_00585E3F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40DA4)))) < ((uint32_t)(local_r15))) {
        if ((*(uint32_t *)(v_rip + 0xA40D55)) == 0) { local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40DA4))); }
    }
    result = HalEnumerateProcessors((uint32_t)(*(uint32_t *)(v_rip + 0xA40E23)), Arg2, a3, a4);
    v_stack_m4C = (uint32_t)(result);
loc_00585E50:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_00585EF3;
    *(uint8_t *)(arg2 + 0x0 + 0x0 * 4 * 8) = 1;
    result = HvlpQueryApicIdAndNumaNode(0, Arg2 + 4 + 0 + 0 * 4 * 8, v_stack_m68, a4);
    v_stack_m5C = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00585E8F;
    result = 0;
    v_stack_m5C = 0;
    *(uint8_t *)(arg2 + 0x0 + 0x0 * 4 * 8) = 0;
    goto loc_00585EEB;
loc_00585E8F:
    if (sign_flag) goto loc_00586138;
    *(uint16_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x8) = (uint16_t)(v_stack_m68);
    if (*(uint64_t *)(v_rip + 0xA411FA) == 0) goto loc_00585EE1;
    result = guard_dispatch_icall(v_stack_m68, v_stack_m50, v_stack_m58, a4);
    if (sign_flag) goto loc_00585EDD;
    if (*(uint64_t *)(v_rip + 0xA411C4) == 0) goto loc_00585EDD;
    result = guard_dispatch_icall((uint32_t)(v_stack_m58), v_stack_m64, v_stack_m58, a4);
    if (sign_flag) {
        Arg1 = v_stack_m68;
    }
    *(uint16_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0xA) = (uint16_t)(Arg1);
    *(uint16_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0xC) = (uint16_t)(Arg1);
loc_00585EEB:
    local_r14 = (uint32_t)((0) + 1);
    goto loc_00585E50;
loc_00585EF3:
    *(uint8_t *)(arg2 + 0x1) = 1;
    v_stack_m60 = 1;
loc_00585F0A:
    v_stack_m54 = 1;
loc_00585F0E:
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00586022;
loc_00585F1F:
    if ((*(uint8_t *)(arg2)) == 0) goto loc_00585FF8;
    if ((*(uint8_t *)(arg2 + 0x1)) != 0) goto loc_00585FF4;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x8))) >= (*(uint16_t *)(v_rip + 0xA3F0C0))) goto loc_00585FF4;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xA49773 + *(uint16_t *)(arg2 + 0x8) * 8) + 0xA)) & (2)) == 0) goto loc_00585FF4;
    if (1 == 0x800ULL) goto loc_00585FF4;
    if (1 == ((uint32_t)((uint32_t)(v_stack_m4C)))) goto loc_00585FF4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40D7D))) == 0) goto loc_00585F80;
    if (1 == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40D7D))))) goto loc_00585FF4;
loc_00585F80:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40D0E))) == 0) goto loc_00585F8F;
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40D0E))))) goto loc_00585FF4;
loc_00585F8F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40DBF))) == 0) goto loc_00585F9E;
    if (1 == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40DBF))))) goto loc_00585FF4;
loc_00585F9E:
    if (1 != ((uint32_t)(local_r15))) goto loc_00585FC1;
    Arg1 = 0;
loc_00585FA8:
    if ((*(uint16_t *)(arg2 + 0x1 + 0x7)) != ((uint16_t)(*(uint16_t *)(arg2 + 0x8)))) goto loc_00585FB3;
    if ((*(uint8_t *)(arg2 + 0x1)) != 0) goto loc_00585FBD;
loc_00585FB3:
    Arg1 = (uint32_t)((Arg1) + 1);
    result = (Arg2 + 1) + (40);
    if (Arg1 < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00585FA8;
loc_00585FBD:
    if (Arg1 == ((uint32_t)((uint32_t)(Arg1)))) goto loc_00585FF4;
loc_00585FC1:
    if (1 != (*(uint32_t *)(v_rip + 0xA40CA0))) goto loc_00585FF8;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) & ((uint32_t)(local_r13)));
    Arg2 = 0;
loc_00585FD6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x1 + 0x3))) & ((uint32_t)(local_r13)));
    if (((uint32_t)(a4)) != ((uint32_t)(result))) goto loc_00585FE6;
    if ((*(uint8_t *)(arg2 + 0x1)) != 0) goto loc_00585FF0;
loc_00585FE6:
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (Arg2 + 1) + (40);
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00585FD6;
loc_00585FF0:
    if (((uint32_t)(Arg2)) == ((uint32_t)((uint32_t)(Arg1)))) {
        *(uint8_t *)(arg2) = 0;
    }
    local_r10 = (uint32_t)((local_r10) + 1);
    a3 = (Arg2) + (40);
    if (((uint32_t)(local_r10)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00585F1F;
    result = 0;
loc_00586011:
    if ((*(uint8_t *)(v_stack_m48)) != 0) goto loc_00586024;
    result = (uint32_t)((result) + 1);
    Arg1 = (v_stack_m48) + (40);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586011;
    goto loc_00586024;
loc_00586022:
    result = 0;
loc_00586024:
    if (0 == ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586134;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00586056;
loc_00586035:
    if ((*(uint8_t *)(v_stack_m48)) != 0) {
        a3 = 0;
        Arg2 = v_stack_m48;
        Arg1 = (uint32_t)((uint32_t)(Arg1));
        result = HvlpComputeLpComparisonMetrics(Arg1, Arg2, a3, a4);
    }
    local_rbx = (uint32_t)((local_rbx) + 1);
    local_r14 = (v_stack_m48) + (40);
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586035;
loc_00586056:
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
    Arg2 = 0;
loc_0058605C:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586071;
    if ((*(uint8_t *)(v_stack_m48 + arg2 + arg2 * 4 * 8)) != 0) goto loc_0058606E;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0058605C;
loc_0058606E:
loc_00586071:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)) + 1)) >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_005860A2;
loc_00586082:
    if ((*(uint8_t *)(v_stack_m48 + (uint32_t)((uint32_t)(arg2)) + 0x1 + (uint32_t)((uint32_t)(arg2)) + 0x1 * 4 * 8)) != 0) {
        Arg2 = v_stack_m48;
        result = HvlpLpComparison((uint32_t)((uint32_t)(Arg2)) + 1 + (uint32_t)((uint32_t)(Arg2)) + 1 * 4, Arg2, (uint32_t)((uint32_t)(Arg2)) + 1, (uint32_t)((uint32_t)(Arg2)));
        a4 = (uint32_t)((uint32_t)(Arg2));
        if (((uint32_t)(result)) == -1) { a4 = (uint32_t)((uint32_t)((uint32_t)(Arg2)) + 1); }
    }
    a3 = (uint32_t)(((uint32_t)((uint32_t)(Arg2)) + 1) + 1);
    local_rbx = (v_stack_m48 + (uint32_t)((uint32_t)(Arg2)) + 1 + (uint32_t)((uint32_t)(Arg2)) + 1 * 4 * 8) + (40);
    if (((uint32_t)(a3)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586082;
loc_005860A2:
    local_r12 = (uint32_t)((1) + 1);
    Arg1 = 0;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + (uint32_t)((uint32_t)(a4)) + (uint32_t)((uint32_t)(a4)) * 4 * 8 + 0x4))) & ((uint32_t)(local_r13)));
    *(uint8_t *)(v_stack_m48 + (uint32_t)((uint32_t)(a4)) + (uint32_t)((uint32_t)(a4)) * 4 * 8 + 0x1) = 1;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_005860E3;
loc_005860C4:
    if (0 == ((uint32_t)(a4))) goto loc_005860D9;
    if ((*(uint8_t *)(v_stack_m48 + 0x4 - 0x3)) == 0) goto loc_005860D9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x4))) & ((uint32_t)(local_r13)));
    if (((uint32_t)(result)) == ((uint32_t)(a3))) goto loc_005860E3;
loc_005860D9:
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (v_stack_m48 + 4) + (40);
    if (Arg1 < ((uint32_t)((uint32_t)(Arg1)))) goto loc_005860C4;
loc_005860E3:
    local_r11 = (uint32_t)(v_stack_m60);
    if (Arg1 == ((uint32_t)((uint32_t)(Arg1)))) {
        local_r11 = (uint32_t)(((uint32_t)(v_stack_m60)) + 1);
        v_stack_m60 = (uint32_t)(local_r11);
    }
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_0058611C;
loc_005860FC:
    if (0 == ((uint32_t)(a4))) goto loc_00586112;
    if ((*(uint8_t *)(v_stack_m48 + 0x8 - 0x7)) == 0) goto loc_00586112;
    if ((*(uint16_t *)(v_stack_m48 + 0x8)) == ((uint16_t)(*(uint16_t *)(v_stack_m48 + (uint32_t)((uint32_t)(a4)) + (uint32_t)((uint32_t)(a4)) * 4 * 8 + 0x8)))) goto loc_0058611C;
loc_00586112:
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (v_stack_m48 + 8) + (40);
    if (Arg1 < ((uint32_t)((uint32_t)(Arg1)))) goto loc_005860FC;
loc_0058611C:
    if (Arg1 != ((uint32_t)((uint32_t)(Arg1)))) goto loc_00585F0E;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m54)) + 1);
    goto loc_00585F0A;
loc_00586134:
loc_00586138:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `W` |
| `Arg2` | `+ 0x0 + rbx*8` | `8` | `W` |
| `Arg2` | `+ 0x0 + rbx*8` | `64` | `R` |
| `Arg2` | `+ 0x1` | `64` | `R` |
| `Arg2` | `+ 0x4` | `64` | `R` |
| `Arg2` | `+ 0x8 + rbx*8` | `16` | `W` |
| `Arg2` | `+ 0xA + rbx*8` | `16` | `W` |
| `Arg2` | `+ 0xC + rbx*8` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00585D30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
