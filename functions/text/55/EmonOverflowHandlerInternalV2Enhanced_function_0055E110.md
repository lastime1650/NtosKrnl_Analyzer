# EmonOverflowHandlerInternalV2Enhanced

- RVA: `0x0055E110`–`0x0055E5B4` (길이 `1,188` bytes)
- VA: `0x000000014055E110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4948`
- 디코드: `321`개 명령, `1,188/1,188` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0055E15B` → [EmonPebsOverflowHandler](EmonPebsOverflowHandler_function_0055ED7C.md) (function, `0x0055ED7C`)
- `0x0055E1A7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0055E31E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0055E327` → [KeProfileInterruptWithSource](../4A/KeProfileInterruptWithSource_function_004A34D0.md) (function, `0x004A34D0`)
- `0x0055E38D` → [PoGetProcessorIdleAccounting](../4F/PoGetProcessorIdleAccounting_function_004FBEA0.md) (function, `0x004FBEA0`)
- `0x0055E39D` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0055E41F` → [PoGetProcessorIdleAccounting](../4F/PoGetProcessorIdleAccounting_function_004FBEA0.md) (function, `0x004FBEA0`)
- `0x0055E442` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0055E4B3` → [KeProfileInterruptWithSource](../4A/KeProfileInterruptWithSource_function_004A34D0.md) (function, `0x004A34D0`)
- `0x0055E50C` → [EmonIsModifiedByBadActorInternalEnhanced](EmonIsModifiedByBadActorInternalEnhanced_function_0055D37C.md) (function, `0x0055D37C`)

### Direct callers
- [EmonOverflowHandlerEnhanced](EmonOverflowHandlerEnhanced_function_0055D850.md) at `0x0055D87B`

### Static image references
- `0x0055E146` → RVA `0x00F8FE28` (`.data`; read)
- `0x0055E16D` → RVA `0x00F8FE00` (`.data`; read)
- `0x0055E1C4` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0055E30A` → RVA `0x00E10360` (`.data`; read)
- `0x0055E334` → RVA `0x00FC21E8` (`.data`; read)
- `0x0055E3D7` → RVA `0x00F8FE14` (`.data`; read)
- `0x0055E55E` → RVA `0x00F8FE10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055E110  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0055E115  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0055E11A  55                              push rbp
0055E11B  56                              push rsi
0055E11C  57                              push rdi
0055E11D  41 54                           push r12
0055E11F  41 55                           push r13
0055E121  41 56                           push r14
0055E123  41 57                           push r15
0055E125  48 8B EC                        mov rbp, rsp
0055E128  48 83 EC 60                     sub rsp, 0x60
0055E12C  83 65 50 00                     and dword ptr [rbp + 0x50], 0
0055E130  4C 8B E1                        mov r12, rcx
0055E133  B9 8E 03 00 00                  mov ecx, 0x38e
0055E138  8B FA                           mov edi, edx
0055E13A  0F 32                           rdmsr
0055E13C  48 C1 E2 20                     shl rdx, 0x20
0055E140  48 0B C2                        or rax, rdx
0055E143  48 8B D8                        mov rbx, rax
0055E146  48 23 1D DB 1C A3 00            and rbx, qword ptr [rip + 0xa31cdb]
0055E14D  48 0F BA E3 3E                  bt rbx, 0x3e
0055E152  48 89 5D F8                     mov qword ptr [rbp - 8], rbx
0055E156  4C 8B FB                        mov r15, rbx
0055E159  73 12                           jae 0x14055e16d
0055E15B  E8 1C 0C 00 00                  call 0x14055ed7c
0055E160  48 B8 FF FF FF FF FF FF FF BF   movabs rax, 0xbfffffffffffffff
0055E16A  4C 23 F8                        and r15, rax
0055E16D  48 8B 1D 8C 1C A3 00            mov rbx, qword ptr [rip + 0xa31c8c]
0055E174  4C 8D 2D 85 1C A3 00            lea r13, [rip + 0xa31c85]
0055E17B  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
0055E17F  4C 8B F7                        mov r14, rdi
0055E182  49 3B DD                        cmp rbx, r13
0055E185  74 33                           je 0x14055e1ba
0055E187  48 8D 34 BF                     lea rsi, [rdi + rdi*4]
0055E18B  48 03 F6                        add rsi, rsi
0055E18E  48 8B 7C F3 20                  mov rdi, qword ptr [rbx + rsi*8 + 0x20]
0055E193  49 23 FF                        and rdi, r15
0055E196  74 14                           je 0x14055e1ac
0055E198  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0055E19C  48 85 C0                        test rax, rax
0055E19F  74 0B                           je 0x14055e1ac
0055E1A1  48 8B D3                        mov rdx, rbx
0055E1A4  48 8B CF                        mov rcx, rdi
0055E1A7  E8 24 C9 15 00                  call 0x1406baad0
0055E1AC  48 8B 1B                        mov rbx, qword ptr [rbx]
0055E1AF  48 F7 D7                        not rdi
0055E1B2  4C 23 FF                        and r15, rdi
0055E1B5  49 3B DD                        cmp rbx, r13
0055E1B8  75 D4                           jne 0x14055e18e
0055E1BA  49 0F BC F7                     bsf rsi, r15
0055E1BE  0F 84 6F 03 00 00               je 0x14055e533
0055E1C4  48 8D 15 75 AA A6 00            lea rdx, [rip + 0xa6aa75]
0055E1CB  45 33 DB                        xor r11d, r11d
0055E1CE  8B C6                           mov eax, esi
0055E1D0  41 8B CB                        mov ecx, r11d
0055E1D3  49 0F B3 C7                     btr r15, rax
0055E1D7  83 FE 20                        cmp esi, 0x20
0055E1DA  72 08                           jb 0x14055e1e4
0055E1DC  83 C6 E0                        add esi, -0x20
0055E1DF  B9 01 00 00 00                  mov ecx, 1
0055E1E4  4A 8B 04 F2                     mov rax, qword ptr [rdx + r14*8]
0055E1E8  4C 8B 70 58                     mov r14, qword ptr [rax + 0x58]
0055E1EC  85 C9                           test ecx, ecx
0055E1EE  74 24                           je 0x14055e214
0055E1F0  83 E9 01                        sub ecx, 1
0055E1F3  74 1B                           je 0x14055e210
0055E1F5  83 E9 63                        sub ecx, 0x63
0055E1F8  74 10                           je 0x14055e20a
0055E1FA  83 F9 01                        cmp ecx, 1
0055E1FD  74 05                           je 0x14055e204
0055E1FF  4D 8B F3                        mov r14, r11
0055E202  EB 10                           jmp 0x14055e214
0055E204  49 83 C6 48                     add r14, 0x48
0055E208  EB 0A                           jmp 0x14055e214
0055E20A  49 83 C6 30                     add r14, 0x30
0055E20E  EB 04                           jmp 0x14055e214
0055E210  49 83 C6 18                     add r14, 0x18
0055E214  4C 8D 04 76                     lea r8, [rsi + rsi*2]
0055E218  49 C1 E0 04                     shl r8, 4
0055E21C  4D 03 46 10                     add r8, qword ptr [r14 + 0x10]
0055E220  45 39 58 18                     cmp dword ptr [r8 + 0x18], r11d
0055E224  0F 85 FB 02 00 00               jne 0x14055e525
0055E22A  45 8B EB                        mov r13d, r11d
0055E22D  41 3B 76 08                     cmp esi, dword ptr [r14 + 8]
0055E231  0F 87 EE 02 00 00               ja 0x14055e525
0055E237  41 83 78 1C 03                  cmp dword ptr [r8 + 0x1c], 3
0055E23C  0F 84 E3 02 00 00               je 0x14055e525
0055E242  41 8B 16                        mov edx, dword ptr [r14]
0055E245  49 8B DB                        mov rbx, r11
0055E248  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
0055E24C  4C 89 5D D0                     mov qword ptr [rbp - 0x30], r11
0055E250  44 88 5D 50                     mov byte ptr [rbp + 0x50], r11b
0055E254  4C 89 5D E8                     mov qword ptr [rbp - 0x18], r11
0055E258  83 FA 01                        cmp edx, 1
0055E25B  74 39                           je 0x14055e296
0055E25D  89 75 58                        mov dword ptr [rbp + 0x58], esi
0055E260  44 8B D6                        mov r10d, esi
0055E263  85 D2                           test edx, edx
0055E265  74 0A                           je 0x14055e271
0055E267  83 FA 01                        cmp edx, 1
0055E26A  74 32                           je 0x14055e29e
0055E26C  E9 8B 00 00 00                  jmp 0x14055e2fc
0055E271  8D 8E 86 01 00 00               lea ecx, [rsi + 0x186]
0055E277  0F 32                           rdmsr
0055E279  48 C1 E2 20                     shl rdx, 0x20
0055E27D  48 0B C2                        or rax, rdx
0055E280  89 75 58                        mov dword ptr [rbp + 0x58], esi
0055E283  48 8B D0                        mov rdx, rax
0055E286  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0055E28A  48 81 E2 FF FF AF FF            and rdx, 0xffffffffffafffff
0055E291  48 8B C2                        mov rax, rdx
0055E294  EB 59                           jmp 0x14055e2ef
0055E296  44 8D 56 20                     lea r10d, [rsi + 0x20]
0055E29A  44 89 55 58                     mov dword ptr [rbp + 0x58], r10d
0055E29E  B9 8D 03 00 00                  mov ecx, 0x38d
0055E2A3  0F 32                           rdmsr
0055E2A5  48 C1 E2 20                     shl rdx, 0x20
0055E2A9  8D 0C B5 00 00 00 00            lea ecx, [rsi*4]
0055E2B0  48 0B C2                        or rax, rdx
0055E2B3  4C 8B C8                        mov r9, rax
0055E2B6  B8 0F 00 00 00                  mov eax, 0xf
0055E2BB  48 D3 E0                        shl rax, cl
0055E2BE  B9 8F 03 00 00                  mov ecx, 0x38f
0055E2C3  48 F7 D0                        not rax
0055E2C6  4C 23 C8                        and r9, rax
0055E2C9  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
0055E2CD  0F 32                           rdmsr
0055E2CF  48 C1 E2 20                     shl rdx, 0x20
0055E2D3  48 0B C2                        or rax, rdx
0055E2D6  41 8B CA                        mov ecx, r10d
0055E2D9  4C 8B C8                        mov r9, rax
0055E2DC  49 0F B3 C9                     btr r9, rcx
0055E2E0  B9 8F 03 00 00                  mov ecx, 0x38f
0055E2E5  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
0055E2E9  49 8B D1                        mov rdx, r9
0055E2EC  49 8B C1                        mov rax, r9
0055E2EF  48 C1 EA 20                     shr rdx, 0x20
0055E2F3  49 8B D8                        mov rbx, r8
0055E2F6  0F 30                           wrmsr
0055E2F8  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
0055E2FC  8B 53 24                        mov edx, dword ptr [rbx + 0x24]
0055E2FF  49 8B CC                        mov rcx, r12
0055E302  85 D2                           test edx, edx
0055E304  0F 85 A9 01 00 00               jne 0x14055e4b3
0055E30A  48 8B 05 4F 20 8B 00            mov rax, qword ptr [rip + 0x8b204f]
0055E311  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
0055E315  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
0055E319  48 85 C0                        test rax, rax
0055E31C  74 07                           je 0x14055e325
0055E31E  E8 AD C7 15 00                  call 0x1406baad0
0055E323  EB 07                           jmp 0x14055e32c
0055E325  33 D2                           xor edx, edx
0055E327  E8 A4 51 F4 FF                  call 0x1404a34d0
0055E32C  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0055E334  48 8B 3D AD 3E A6 00            mov rdi, qword ptr [rip + 0xa63ead]
0055E33B  8B C8                           mov ecx, eax
0055E33D  48 69 D9 28 01 00 00            imul rbx, rcx, 0x128
0055E344  8B 4C 3B 18                     mov ecx, dword ptr [rbx + rdi + 0x18]
0055E348  85 C9                           test ecx, ecx
0055E34A  74 73                           je 0x14055e3bf
0055E34C  8B 44 3B 20                     mov eax, dword ptr [rbx + rdi + 0x20]
0055E350  44 8B 6C 3B 10                  mov r13d, dword ptr [rbx + rdi + 0x10]
0055E355  44 8B E0                        mov r12d, eax
0055E358  49 C1 E4 04                     shl r12, 4
0055E35C  4C 03 E3                        add r12, rbx
0055E35F  FF C0                           inc eax
0055E361  83 E0 0F                        and eax, 0xf
0055E364  89 44 3B 20                     mov dword ptr [rbx + rdi + 0x20], eax
0055E368  8B 44 3B 14                     mov eax, dword ptr [rbx + rdi + 0x14]
0055E36C  85 C0                           test eax, eax
0055E36E  75 7F                           jne 0x14055e3ef
0055E370  33 D2                           xor edx, edx
0055E372  B8 10 27 00 00                  mov eax, 0x2710
0055E377  F7 F1                           div ecx
0055E379  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0055E37D  85 C0                           test eax, eax
0055E37F  75 08                           jne 0x14055e389
0055E381  C7 44 3B 14 01 00 00 00         mov dword ptr [rbx + rdi + 0x14], 1
0055E389  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0055E38D  E8 0E DB F9 FF                  call 0x1404fbea0
0055E392  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0055E396  33 C9                           xor ecx, ecx
0055E398  48 89 44 3B 08                  mov qword ptr [rbx + rdi + 8], rax
0055E39D  E8 3E 04 E2 FF                  call 0x14037e7e0
0055E3A2  48 8B 0D 3F 3E A6 00            mov rcx, qword ptr [rip + 0xa63e3f]
0055E3A9  48 89 04 0B                     mov qword ptr [rbx + rcx], rax
0055E3AD  45 89 6C 3C 28                  mov dword ptr [r12 + rdi + 0x28], r13d
0055E3B2  48 8B 04 0B                     mov rax, qword ptr [rbx + rcx]
0055E3B6  49 89 44 3C 30                  mov qword ptr [r12 + rdi + 0x30], rax
0055E3BB  4C 8B 65 40                     mov r12, qword ptr [rbp + 0x40]
0055E3BF  48 8B 5D C8                     mov rbx, qword ptr [rbp - 0x38]
0055E3C3  41 8B 0E                        mov ecx, dword ptr [r14]
0055E3C6  85 C9                           test ecx, ecx
0055E3C8  0F 84 90 01 00 00               je 0x14055e55e
0055E3CE  83 F9 01                        cmp ecx, 1
0055E3D1  0F 85 28 01 00 00               jne 0x14055e4ff
0055E3D7  8B 0D 37 1A A3 00               mov ecx, dword ptr [rip + 0xa31a37]
0055E3DD  83 F9 40                        cmp ecx, 0x40
0055E3E0  0F 82 DA 00 00 00               jb 0x14055e4c0
0055E3E6  48 83 C8 FF                     or rax, 0xffffffffffffffff
0055E3EA  E9 DC 00 00 00                  jmp 0x14055e4cb
0055E3EF  83 E8 01                        sub eax, 1
0055E3F2  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0055E3F6  75 C3                           jne 0x14055e3bb
0055E3F8  33 D2                           xor edx, edx
0055E3FA  B8 10 27 00 00                  mov eax, 0x2710
0055E3FF  F7 F1                           div ecx
0055E401  89 45 C0                        mov dword ptr [rbp - 0x40], eax
0055E404  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0055E408  85 C0                           test eax, eax
0055E40A  75 0F                           jne 0x14055e41b
0055E40C  C7 44 3B 14 01 00 00 00         mov dword ptr [rbx + rdi + 0x14], 1
0055E414  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
0055E41B  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0055E41F  E8 7C DA F9 FF                  call 0x1404fbea0
0055E424  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0055E428  48 3B 44 3B 08                  cmp rax, qword ptr [rbx + rdi + 8]
0055E42D  0F 85 63 FF FF FF               jne 0x14055e396
0055E433  41 8B C5                        mov eax, r13d
0055E436  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0055E43A  0F AF 45 C0                     imul eax, dword ptr [rbp - 0x40]
0055E43E  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0055E442  E8 99 03 E2 FF                  call 0x14037e7e0
0055E447  4C 8B 05 9A 3D A6 00            mov r8, qword ptr [rip + 0xa63d9a]
0055E44E  48 8B C8                        mov rcx, rax
0055E451  4C 8B C8                        mov r9, rax
0055E454  4A 2B 0C 03                     sub rcx, qword ptr [rbx + r8]
0055E458  75 0F                           jne 0x14055e469
0055E45A  45 89 6C 3C 28                  mov dword ptr [r12 + rdi + 0x28], r13d
0055E45F  4D 89 4C 3C 30                  mov qword ptr [r12 + rdi + 0x30], r9
0055E464  E9 52 FF FF FF                  jmp 0x14055e3bb
0055E469  42 8B 44 03 18                  mov eax, dword ptr [rbx + r8 + 0x18]
0055E46E  33 D2                           xor edx, edx
0055E470  48 0F AF 45 D8                  imul rax, qword ptr [rbp - 0x28]
0055E475  48 F7 F1                        div rcx
0055E478  48 8B C8                        mov rcx, rax
0055E47B  48 B8 BD 42 7A E5 D5 94 BF D6   movabs rax, 0xd6bf94d5e57a42bd
0055E485  48 0F AF 4D E0                  imul rcx, qword ptr [rbp - 0x20]
0055E48A  48 F7 E1                        mul rcx
0055E48D  4C 8B EA                        mov r13, rdx
0055E490  49 C1 ED 17                     shr r13, 0x17
0055E494  49 8D 85 00 F0 FF FF            lea rax, [r13 - 0x1000]
0055E49B  48 3D FF EF FF 7F               cmp rax, 0x7fffefff
0055E4A1  76 05                           jbe 0x14055e4a8
0055E4A3  46 8B 6C 03 1C                  mov r13d, dword ptr [rbx + r8 + 0x1c]
0055E4A8  46 89 6C 03 10                  mov dword ptr [rbx + r8 + 0x10], r13d
0055E4AD  4E 89 0C 03                     mov qword ptr [rbx + r8], r9
0055E4B1  EB A7                           jmp 0x14055e45a
0055E4B3  E8 18 50 F4 FF                  call 0x1404a34d0
0055E4B8  44 8B 2B                        mov r13d, dword ptr [rbx]
0055E4BB  E9 03 FF FF FF                  jmp 0x14055e3c3
0055E4C0  B8 01 00 00 00                  mov eax, 1
0055E4C5  48 D3 E0                        shl rax, cl
0055E4C8  48 FF C8                        dec rax
0055E4CB  41 8B D5                        mov edx, r13d
0055E4CE  8D 8E 09 03 00 00               lea ecx, [rsi + 0x309]
0055E4D4  48 F7 DA                        neg rdx
0055E4D7  48 23 D0                        and rdx, rax
0055E4DA  48 8B C2                        mov rax, rdx
0055E4DD  48 C1 EA 20                     shr rdx, 0x20
0055E4E1  0F 30                           wrmsr
0055E4E3  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0055E4E6  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0055E4EA  48 0F AB C1                     bts rcx, rax
0055E4EE  48 8B D1                        mov rdx, rcx
0055E4F1  48 8B C1                        mov rax, rcx
0055E4F4  48 C1 EA 20                     shr rdx, 0x20
0055E4F8  B9 8F 03 00 00                  mov ecx, 0x38f
0055E4FD  0F 30                           wrmsr
0055E4FF  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0055E503  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0055E507  49 8B D6                        mov rdx, r14
0055E50A  8B CE                           mov ecx, esi
0055E50C  E8 6B EE FF FF                  call 0x14055d37c
0055E511  45 33 DB                        xor r11d, r11d
0055E514  48 8D 15 25 A7 A6 00            lea rdx, [rip + 0xa6a725]
0055E51B  44 38 5D 50                     cmp byte ptr [rbp + 0x50], r11b
0055E51F  74 04                           je 0x14055e525
0055E521  C6 43 28 01                     mov byte ptr [rbx + 0x28], 1
0055E525  49 0F BC F7                     bsf rsi, r15
0055E529  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
0055E52D  0F 85 9B FC FF FF               jne 0x14055e1ce
0055E533  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
0055E537  B9 90 03 00 00                  mov ecx, 0x390
0055E53C  48 8B C2                        mov rax, rdx
0055E53F  48 C1 EA 20                     shr rdx, 0x20
0055E543  0F 30                           wrmsr
0055E545  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0055E54D  48 83 C4 60                     add rsp, 0x60
0055E551  41 5F                           pop r15
0055E553  41 5E                           pop r14
0055E555  41 5D                           pop r13
0055E557  41 5C                           pop r12
0055E559  5F                              pop rdi
0055E55A  5E                              pop rsi
0055E55B  5D                              pop rbp
0055E55C  C3                              ret
0055E55D  CC                              int3
0055E55E  8B 0D AC 18 A3 00               mov ecx, dword ptr [rip + 0xa318ac]
0055E564  83 F9 40                        cmp ecx, 0x40
0055E567  72 06                           jb 0x14055e56f
0055E569  48 83 C8 FF                     or rax, 0xffffffffffffffff
0055E56D  EB 0B                           jmp 0x14055e57a
0055E56F  B8 01 00 00 00                  mov eax, 1
0055E574  48 D3 E0                        shl rax, cl
0055E577  48 FF C8                        dec rax
0055E57A  41 8B D5                        mov edx, r13d
0055E57D  8D 8E C1 00 00 00               lea ecx, [rsi + 0xc1]
0055E583  48 F7 DA                        neg rdx
0055E586  48 23 D0                        and rdx, rax
0055E589  48 8B C2                        mov rax, rdx
0055E58C  48 C1 EA 20                     shr rdx, 0x20
0055E590  0F 30                           wrmsr
0055E592  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0055E596  8D 8E 86 01 00 00               lea ecx, [rsi + 0x186]
0055E59C  49 8B D0                        mov rdx, r8
0055E59F  48 81 CA 00 00 50 00            or rdx, 0x500000
0055E5A6  48 8B C2                        mov rax, rdx
0055E5A9  48 C1 EA 20                     shr rdx, 0x20
0055E5AD  0F 30                           wrmsr
0055E5AF  E9 4F FF FF FF                  jmp 0x14055e503
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonOverflowHandlerInternalV2Enhanced(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_rbx = (result) & (*(unsigned __int64 *)(v_rip + 10689755));
    v_stack_m40 = v_rbx;
    v_r15 = v_rbx;
    if (!(condition_is_above_or_equal)) {
        result = EmonPebsOverflowHandler(910, a2, a3, a4);
        v_r15 = (v_rbx) & (result);
    }
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int64 *)(v_rip + 10689676)) == (v_rip + 10689669)) goto loc_0055E1BA;
    v_rsi = ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4) + ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4);
loc_0055E18E:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10689676) + v_rsi * 8 + 32)) & (v_r15);
    if (condition_is_equal) goto loc_0055E1AC;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10689676) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10689676) + 16) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 10689676);
        a1 = v_rdi;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rdi = ~(v_rdi);
    v_r15 = (v_r15) & (v_rdi);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10689676))) != (v_rip + 10689669)) goto loc_0055E18E;
loc_0055E1BA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10689676))) == (v_rip + 10689669)) goto loc_0055E533;
    v_r11 = 0;
loc_0055E1CE:
    if (((unsigned int)(v_rsi)) >= 32) {
        v_rsi = (unsigned int)((v_rsi) + (-32));
        a1 = 1;
    }
    if ((unsigned int)(a1) == 0) goto loc_0055E214;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0055E210;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0055E20A;
    if (((unsigned int)(a1)) == 1) goto loc_0055E204;
    goto loc_0055E214;
loc_0055E204:
    v_r14 = (0) + (72);
    goto loc_0055E214;
loc_0055E20A:
    v_r14 = (v_r14) + (48);
    goto loc_0055E214;
loc_0055E210:
    v_r14 = (v_r14) + (24);
loc_0055E214:
    a3 = (v_rsi + v_rsi * 2) << (4);
    a3 = (a3) + (*(unsigned __int64 *)(v_r14 + 16));
    if ((*(unsigned int *)(a3 + 24)) != 0) goto loc_0055E525;
    if (((unsigned int)(v_rsi)) > (*(unsigned int *)(v_r14 + 8))) goto loc_0055E525;
    if ((*(unsigned int *)(a3 + 28)) == 3) goto loc_0055E525;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_p18 = 0;
    v_stack_m50 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14)))) == 1) goto loc_0055E296;
    v_stack_p20 = (unsigned int)(v_rsi);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))) == 0) goto loc_0055E271;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14)))) == 1) goto loc_0055E29E;
    goto loc_0055E2FC;
loc_0055E271:
    a2 = ((unsigned int)(*(unsigned int *)(v_r14))) << (32);
    result = (*(unsigned __int64 *)(v_rip + 10922613 + (unsigned int)((unsigned int)(a2)) * 8)) | (a2);
    v_stack_p20 = (unsigned int)(v_rsi);
    v_stack_m68 = result;
    a2 = (result) & (0xFFFFFFFFFFAFFFFFULL);
    goto loc_0055E2EF;
loc_0055E296:
    v_stack_p20 = (unsigned int)(v_rsi + 32);
loc_0055E29E:
    a2 = (a2) << (32);
    result = (a2) | (a2);
    result = (15) << ((unsigned __int8)(v_rsi * 4));
    result = ~(result);
    a4 = (result) & (result);
    v_stack_m68 = a4;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_m50 = result;
loc_0055E2EF:
    a2 = (result) >> (32);
    v_stack_m70 = a3;
loc_0055E2FC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 36))) != 0) goto loc_0055E4B3;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (*(unsigned __int64 *)(v_rip + 9117775) == 0) goto loc_0055E325;
    result = guard_dispatch_icall(a1, (unsigned int)(*(unsigned int *)(a3 + 36)), a3, result);
    goto loc_0055E32C;
loc_0055E325:
    a2 = 0;
    result = KeProfileInterruptWithSource(a1, a2, a3, result);
loc_0055E32C:
    v_rbx = (a3) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 24))) == 0) goto loc_0055E3BF;
    v_r12 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 32))))) << (4);
    v_r12 = (v_r12) + (v_rbx);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 32))) + 1);
    result = (unsigned int)((result) & (15));
    *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 32) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 20))) != 0) goto loc_0055E3EF;
    a2 = 0;
    *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 20) = (unsigned int)((unsigned int)(0x2710ULL));
    if ((unsigned int)((unsigned int)(0x2710ULL)) == 0) {
        *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 20) = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, a2, a3, result);
loc_0055E396:
    a1 = 0;
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 8) = v_stack_m60;
    result = KeQueryPerformanceCounter(a1, a2, a3, result);
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10894911) * 1) = result;
    *(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 16)));
    *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 48) = *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10894911) * 1);
loc_0055E3BB:
loc_0055E3BF:
loc_0055E3C3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))) == 0) goto loc_0055E55E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14)))) != 1) goto loc_0055E4FF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10689079)))) < 64) goto loc_0055E4C0;
    result = (*(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10894911) * 1)) | (-1);
    goto loc_0055E4CB;
loc_0055E3EF:
    result = (unsigned int)((result) - (1));
    *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 20) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0055E3BB;
    a2 = 0;
    v_stack_m78 = (unsigned int)((unsigned int)(0x2710ULL));
    *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 20) = (unsigned int)((unsigned int)(0x2710ULL));
    if ((unsigned int)((unsigned int)(0x2710ULL)) == 0) {
        *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 20) = 1;
        v_stack_m78 = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, a2, a3, result);
    if (v_stack_m60 != (*(unsigned __int64 *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 8))) goto loc_0055E396;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 16))))) * (v_stack_m78));
    v_stack_m60 = result;
    result = KeQueryPerformanceCounter(v_stack_m58, a2, a3, result);
    a1 = (result) - (*(unsigned __int64 *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10894746) * 1));
    if (condition_is_not_equal) goto loc_0055E469;
loc_0055E45A:
    *(unsigned int *)(v_stack_p8 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 16)));
    *(unsigned __int64 *)(v_stack_p8 + *(unsigned __int64 *)(v_rip + 10895021) * 1 + 48) = result;
    goto loc_0055E3BB;
loc_0055E469:
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10894746) * 1 + 24))) * (v_stack_m60);
    a1 = (result) * (v_stack_m58);
    v_r13 = (0) >> (23);
    if ((v_r13 - 4096) >= = 0x7FFFEFFFULL) {
        v_r13 = *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10894746) * 1 + 28);
    }
    *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10894746) * 1 + 16) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10894746) * 1) = result;
    goto loc_0055E45A;
loc_0055E4B3:
    result = KeProfileInterruptWithSource(a1, a2, *(unsigned __int64 *)(v_rip + 10894746), result);
    goto loc_0055E3C3;
loc_0055E4C0:
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - 1;
loc_0055E4CB:
    a2 = -((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)))));
    a2 = (a2) & (result);
    a2 = (a2) >> (32);
    a2 = (v_stack_m50) >> (32);
loc_0055E4FF:
loc_0055E503:
    result = EmonIsModifiedByBadActorInternalEnhanced((unsigned int)((unsigned int)(v_rsi)), v_r14, v_stack_m68, v_stack_p18);
    v_r11 = 0;
    if (v_stack_p18 != 0) {
        *(unsigned __int8 *)(v_stack_m70 + 40) = 1;
    }
    if (v_stack_p18 != 0) goto loc_0055E1CE;
loc_0055E533:
    a2 = (v_stack_m40) >> (32);
    v_rsp = (v_rsp) + (96);
    return v_stack_m40;
loc_0055E55E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10688684)))) < 64) goto loc_0055E56F;
    result = (v_stack_m40) | (-1);
    goto loc_0055E57A;
loc_0055E56F:
    result = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10688684))));
    result = (result) - 1;
loc_0055E57A:
    a2 = -((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)))));
    a2 = (a2) & (result);
    a2 = (a2) >> (32);
    a2 = (v_stack_m68) | (0x500000ULL);
    a2 = (a2) >> (32);
    goto loc_0055E503;
}
```

## 5. (Beta) C Style

```c
int64_t EmonOverflowHandlerInternalV2Enhanced(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    local_rbx = (result) & (*(uint64_t *)(v_rip + 0xA31CDB));
    v_stack_m40 = local_rbx;
    local_r15 = local_rbx;
    if (!(condition_is_above_or_equal)) {
        result = EmonPebsOverflowHandler(910, Arg2, a3, a4);
        local_r15 = (local_rbx) & (result);
    }
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint64_t *)(v_rip + 0xA31C8C)) == (v_rip + 10689669)) goto loc_0055E1BA;
    local_rsi = ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4) + ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4);
loc_0055E18E:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA31C8C) + local_rsi * 8 + 0x20)) & (local_r15);
    if (condition_is_equal) goto loc_0055E1AC;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA31C8C) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA31C8C) + 0x10) != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0xA31C8C);
        Arg1 = local_rdi;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
    local_rdi = ~(local_rdi);
    local_r15 = (local_r15) & (local_rdi);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA31C8C))) != (v_rip + 10689669)) goto loc_0055E18E;
loc_0055E1BA:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA31C8C))) == (v_rip + 10689669)) goto loc_0055E533;
    local_r11 = 0;
loc_0055E1CE:
    if (((uint32_t)(local_rsi)) >= 32) {
        local_rsi = (uint32_t)((local_rsi) + (-32));
        Arg1 = 1;
    }
    if ((uint32_t)(Arg1) == 0) goto loc_0055E214;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0055E210;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0055E20A;
    if (((uint32_t)(Arg1)) == 1) goto loc_0055E204;
    goto loc_0055E214;
loc_0055E204:
    local_r14 = (0) + (72);
    goto loc_0055E214;
loc_0055E20A:
    local_r14 = (local_r14) + (48);
    goto loc_0055E214;
loc_0055E210:
    local_r14 = (local_r14) + (24);
loc_0055E214:
    a3 = (local_rsi + local_rsi * 2) << (4);
    a3 = (a3) + (*(uint64_t *)(local_r14 + 0x10));
    if ((*(uint32_t *)(a3 + 0x18)) != 0) goto loc_0055E525;
    if (((uint32_t)(local_rsi)) > (*(uint32_t *)(local_r14 + 0x8))) goto loc_0055E525;
    if ((*(uint32_t *)(a3 + 0x1C)) == 3) goto loc_0055E525;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_p18 = 0;
    v_stack_m50 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14)))) == 1) goto loc_0055E296;
    v_stack_p20 = (uint32_t)(local_rsi);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))) == 0) goto loc_0055E271;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14)))) == 1) goto loc_0055E29E;
    goto loc_0055E2FC;
loc_0055E271:
    Arg2 = ((uint32_t)(*(uint32_t *)(local_r14))) << (32);
    result = (*(uint64_t *)(v_rip + 0xA6AA75 + (uint32_t)((uint32_t)(arg2)) * 8)) | (Arg2);
    v_stack_p20 = (uint32_t)(local_rsi);
    v_stack_m68 = result;
    Arg2 = (result) & (0xFFFFFFFFFFAFFFFFULL);
    goto loc_0055E2EF;
loc_0055E296:
    v_stack_p20 = (uint32_t)(local_rsi + 32);
loc_0055E29E:
    Arg2 = (Arg2) << (32);
    result = (Arg2) | (Arg2);
    result = (15) << ((uint8_t)(local_rsi * 4));
    result = ~(result);
    a4 = (result) & (result);
    v_stack_m68 = a4;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_m50 = result;
loc_0055E2EF:
    Arg2 = (result) >> (32);
    v_stack_m70 = a3;
loc_0055E2FC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(a3 + 0x24))) != 0) goto loc_0055E4B3;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (*(uint64_t *)(v_rip + 0x8B204F) == 0) goto loc_0055E325;
    result = guard_dispatch_icall(Arg1, (uint32_t)(*(uint32_t *)(a3 + 0x24)), a3, result);
    goto loc_0055E32C;
loc_0055E325:
    Arg2 = 0;
    result = KeProfileInterruptWithSource(Arg1, Arg2, a3, result);
loc_0055E32C:
    local_rbx = (a3) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x18))) == 0) goto loc_0055E3BF;
    local_r12 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x20))))) << (4);
    local_r12 = (local_r12) + (local_rbx);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x20))) + 1);
    result = (uint32_t)((result) & (15));
    *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x20) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x14))) != 0) goto loc_0055E3EF;
    Arg2 = 0;
    *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x14) = (uint32_t)((uint32_t)(0x2710ULL));
    if ((uint32_t)((uint32_t)(0x2710ULL)) == 0) {
        *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x14) = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, Arg2, a3, result);
loc_0055E396:
    Arg1 = 0;
    *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x8) = v_stack_m60;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, result);
    *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63E3F) * 1) = result;
    *(uint32_t *)(local_r12 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x10)));
    *(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x30) = *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63E3F) * 1);
loc_0055E3BB:
loc_0055E3BF:
loc_0055E3C3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))) == 0) goto loc_0055E55E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14)))) != 1) goto loc_0055E4FF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA31A37)))) < 64) goto loc_0055E4C0;
    result = (*(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63E3F) * 1)) | (-1);
    goto loc_0055E4CB;
loc_0055E3EF:
    result = (uint32_t)((result) - (1));
    *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x14) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0055E3BB;
    Arg2 = 0;
    v_stack_m78 = (uint32_t)((uint32_t)(0x2710ULL));
    *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x14) = (uint32_t)((uint32_t)(0x2710ULL));
    if ((uint32_t)((uint32_t)(0x2710ULL)) == 0) {
        *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x14) = 1;
        v_stack_m78 = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, Arg2, a3, result);
    if (v_stack_m60 != (*(uint64_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x8))) goto loc_0055E396;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x10))))) * (v_stack_m78));
    v_stack_m60 = result;
    result = KeQueryPerformanceCounter(v_stack_m58, Arg2, a3, result);
    Arg1 = (result) - (*(uint64_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63D9A) * 1));
    if (condition_is_not_equal) goto loc_0055E469;
loc_0055E45A:
    *(uint32_t *)(v_stack_p8 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x10)));
    *(uint64_t *)(v_stack_p8 + *(uint64_t *)(v_rip + 0xA63EAD) * 1 + 0x30) = result;
    goto loc_0055E3BB;
loc_0055E469:
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63D9A) * 1 + 0x18))) * (v_stack_m60);
    Arg1 = (result) * (v_stack_m58);
    local_r13 = (0) >> (23);
    if ((local_r13 - 4096) >= = 0x7FFFEFFFULL) {
        local_r13 = *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63D9A) * 1 + 0x1C);
    }
    *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63D9A) * 1 + 0x10) = (uint32_t)(local_r13);
    *(uint64_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63D9A) * 1) = result;
    goto loc_0055E45A;
loc_0055E4B3:
    result = KeProfileInterruptWithSource(Arg1, Arg2, *(uint64_t *)(v_rip + 0xA63D9A), result);
    goto loc_0055E3C3;
loc_0055E4C0:
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - 1;
loc_0055E4CB:
    Arg2 = -((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)))));
    Arg2 = (Arg2) & (result);
    Arg2 = (Arg2) >> (32);
    Arg2 = (v_stack_m50) >> (32);
loc_0055E4FF:
loc_0055E503:
    result = EmonIsModifiedByBadActorInternalEnhanced((uint32_t)((uint32_t)(local_rsi)), local_r14, v_stack_m68, v_stack_p18);
    local_r11 = 0;
    if (v_stack_p18 != 0) {
        *(uint8_t *)(v_stack_m70 + 0x28) = 1;
    }
    if (v_stack_p18 != 0) goto loc_0055E1CE;
loc_0055E533:
    Arg2 = (v_stack_m40) >> (32);
    local_rsp = (local_rsp) + (96);
    return v_stack_m40;
loc_0055E55E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA318AC)))) < 64) goto loc_0055E56F;
    result = (v_stack_m40) | (-1);
    goto loc_0055E57A;
loc_0055E56F:
    result = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA318AC))));
    result = (result) - 1;
loc_0055E57A:
    Arg2 = -((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)))));
    Arg2 = (Arg2) & (result);
    Arg2 = (Arg2) >> (32);
    Arg2 = (v_stack_m68) | (0x500000ULL);
    Arg2 = (Arg2) >> (32);
    goto loc_0055E503;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rdi*4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055E110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
