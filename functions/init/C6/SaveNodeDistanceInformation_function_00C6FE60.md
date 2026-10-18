# SaveNodeDistanceInformation

- RVA: `0x00C6FE60`–`0x00C7044F` (길이 `1,519` bytes)
- VA: `0x0000000140C6FE60`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008A8D4`
- 디코드: `428`개 명령, `1,519/1,519` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00C6FEF7` → [KeQueryNumaCosts](../C3/KeQueryNumaCosts_function_00C36F18.md) (function, `0x00C36F18`)
- `0x00C6FF89` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C701CC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C701DC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C70221` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00C7024B` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x00C70326` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C70346` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x00C703FE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C7040D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C7041C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C70428` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Phase1InitializationIoReady](../C7/Phase1InitializationIoReady_function_00C70458.md) at `0x00C705C8`

### Static image references
- `0x00C6FE83` → RVA `0x00E0A740` (`.data`; read)
- `0x00C6FE98` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00C6FEAB` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x00C701BE` → RVA `0x00C79310` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C701D1` → RVA `0x00C79380` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C702CA` → RVA `0x00FC50A8` (`ALMOSTRO`; read)
- `0x00C7031B` → RVA `0x00C793B0` (` ?? ::PBOPGDP::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00C6FF89` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C701CC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C701DC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C70221` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`INIT` → `.text`)
  - `0x00C7024B` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`INIT` → `.text`)
  - `0x00C70326` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C70346` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`INIT` → `.text`)
  - `0x00C703FE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C7040D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C7041C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C70428` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6FE60  48 8B C4                        mov rax, rsp
00C6FE63  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C6FE67  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C6FE6B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00C6FE6F  55                              push rbp
00C6FE70  41 54                           push r12
00C6FE72  41 55                           push r13
00C6FE74  41 56                           push r14
00C6FE76  41 57                           push r15
00C6FE78  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00C6FE7C  48 81 EC E0 00 00 00            sub rsp, 0xe0
00C6FE83  48 8B 05 B6 A8 19 00            mov rax, qword ptr [rip + 0x19a8b6]
00C6FE8A  48 33 C4                        xor rax, rsp
00C6FE8D  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
00C6FE91  48 83 4D 97 FF                  or qword ptr [rbp - 0x69], 0xffffffffffffffff
00C6FE96  33 C0                           xor eax, eax
00C6FE98  0F B7 1D 61 51 35 00            movzx ebx, word ptr [rip + 0x355161]
00C6FE9F  0F 57 C0                        xorps xmm0, xmm0
00C6FEA2  33 FF                           xor edi, edi
00C6FEA4  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00C6FEA8  89 45 FF                        mov dword ptr [rbp - 1], eax
00C6FEAB  48 8D 05 0E F8 35 00            lea rax, [rip + 0x35f80e]
00C6FEB2  89 7D A3                        mov dword ptr [rbp - 0x5d], edi
00C6FEB5  8B F7                           mov esi, edi
00C6FEB7  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00C6FEBB  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00C6FEBF  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00C6FEC3  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00C6FEC7  85 DB                           test ebx, ebx
00C6FEC9  74 2C                           je 0x140c6fef7
00C6FECB  4C 8B C0                        mov r8, rax
00C6FECE  44 8B CB                        mov r9d, ebx
00C6FED1  49 8B 00                        mov rax, qword ptr [r8]
00C6FED4  8B FE                           mov edi, esi
00C6FED6  FF C6                           inc esi
00C6FED8  4D 8D 40 08                     lea r8, [r8 + 8]
00C6FEDC  0F B7 10                        movzx edx, word ptr [rax]
00C6FEDF  66 3B 50 02                     cmp dx, word ptr [rax + 2]
00C6FEE3  0F 45 F7                        cmovne esi, edi
00C6FEE6  49 83 E9 01                     sub r9, 1
00C6FEEA  75 E5                           jne 0x140c6fed1
00C6FEEC  83 FE 01                        cmp esi, 1
00C6FEEF  0F 84 2C 05 00 00               je 0x140c70421
00C6FEF5  33 FF                           xor edi, edi
00C6FEF7  E8 1C 70 FC FF                  call 0x140c36f18
00C6FEFC  4C 8B E8                        mov r13, rax
00C6FEFF  48 85 C0                        test rax, rax
00C6FF02  0F 84 0A 05 00 00               je 0x140c70412
00C6FF08  44 8D 5B FF                     lea r11d, [rbx - 1]
00C6FF0C  44 8B C7                        mov r8d, edi
00C6FF0F  45 85 DB                        test r11d, r11d
00C6FF12  74 55                           je 0x140c6ff69
00C6FF14  45 8D 48 01                     lea r9d, [r8 + 1]
00C6FF18  45 8B D1                        mov r10d, r9d
00C6FF1B  44 3B CB                        cmp r9d, ebx
00C6FF1E  73 41                           jae 0x140c6ff61
00C6FF20  8B FB                           mov edi, ebx
00C6FF22  41 0F AF F8                     imul edi, r8d
00C6FF26  41 03 F9                        add edi, r9d
00C6FF29  49 8B 4C FD 00                  mov rcx, qword ptr [r13 + rdi*8]
00C6FF2E  48 83 F9 FF                     cmp rcx, -1
00C6FF32  74 23                           je 0x140c6ff57
00C6FF34  8B C3                           mov eax, ebx
00C6FF36  48 D1 E9                        shr rcx, 1
00C6FF39  41 0F AF C2                     imul eax, r10d
00C6FF3D  41 03 C0                        add eax, r8d
00C6FF40  8B D0                           mov edx, eax
00C6FF42  49 8B 44 C5 00                  mov rax, qword ptr [r13 + rax*8]
00C6FF47  48 D1 E8                        shr rax, 1
00C6FF4A  48 03 C8                        add rcx, rax
00C6FF4D  49 89 4C FD 00                  mov qword ptr [r13 + rdi*8], rcx
00C6FF52  49 89 4C D5 00                  mov qword ptr [r13 + rdx*8], rcx
00C6FF57  41 FF C2                        inc r10d
00C6FF5A  FF C7                           inc edi
00C6FF5C  44 3B D3                        cmp r10d, ebx
00C6FF5F  72 C8                           jb 0x140c6ff29
00C6FF61  45 8B C1                        mov r8d, r9d
00C6FF64  45 3B CB                        cmp r9d, r11d
00C6FF67  72 AB                           jb 0x140c6ff14
00C6FF69  8D 46 02                        lea eax, [rsi + 2]
00C6FF6C  B9 00 01 00 00                  mov ecx, 0x100
00C6FF71  0F AF C6                        imul eax, esi
00C6FF74  41 B8 4B 65 20 20               mov r8d, 0x2020654b
00C6FF7A  44 8D 34 45 04 00 00 00         lea r14d, [rax*2 + 4]
00C6FF82  41 8B D6                        mov edx, r14d
00C6FF85  44 89 75 9F                     mov dword ptr [rbp - 0x61], r14d
00C6FF89  E8 62 21 F1 FF                  call 0x140b820f0
00C6FF8E  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00C6FF92  4C 8B E0                        mov r12, rax
00C6FF95  48 85 C0                        test rax, rax
00C6FF98  0F 84 5B 04 00 00               je 0x140c703f9
00C6FF9E  89 30                           mov dword ptr [rax], esi
00C6FFA0  44 8D 56 01                     lea r10d, [rsi + 1]
00C6FFA4  4E 8D 3C 90                     lea r15, [rax + r10*4]
00C6FFA8  41 B8 01 00 00 00               mov r8d, 1
00C6FFAE  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
00C6FFB2  85 DB                           test ebx, ebx
00C6FFB4  74 2D                           je 0x140c6ffe3
00C6FFB6  48 8D 15 03 F7 35 00            lea rdx, [rip + 0x35f703]
00C6FFBD  4C 8B CB                        mov r9, rbx
00C6FFC0  48 8B 3A                        mov rdi, qword ptr [rdx]
00C6FFC3  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00C6FFC7  66 39 07                        cmp word ptr [rdi], ax
00C6FFCA  75 0D                           jne 0x140c6ffd9
00C6FFCC  8B 47 04                        mov eax, dword ptr [rdi + 4]
00C6FFCF  41 8B C8                        mov ecx, r8d
00C6FFD2  41 FF C0                        inc r8d
00C6FFD5  41 89 04 8C                     mov dword ptr [r12 + rcx*4], eax
00C6FFD9  48 83 C2 08                     add rdx, 8
00C6FFDD  49 83 E9 01                     sub r9, 1
00C6FFE1  75 DD                           jne 0x140c6ffc0
00C6FFE3  8B C6                           mov eax, esi
00C6FFE5  BA FF FF 00 00                  mov edx, 0xffff
00C6FFEA  0F AF C6                        imul eax, esi
00C6FFED  85 C0                           test eax, eax
00C6FFEF  74 0A                           je 0x140c6fffb
00C6FFF1  8B C8                           mov ecx, eax
00C6FFF3  49 8B FF                        mov rdi, r15
00C6FFF6  8B C2                           mov eax, edx
00C6FFF8  66 F3 AB                        rep stosw word ptr [rdi], ax
00C6FFFB  8B FB                           mov edi, ebx
00C6FFFD  B9 01 00 00 00                  mov ecx, 1
00C70002  0F AF FB                        imul edi, ebx
00C70005  85 FF                           test edi, edi
00C70007  74 67                           je 0x140c70070
00C70009  49 8B C5                        mov rax, r13
00C7000C  44 8B C7                        mov r8d, edi
00C7000F  44 8B CF                        mov r9d, edi
00C70012  48 8B 10                        mov rdx, qword ptr [rax]
00C70015  48 3B CA                        cmp rcx, rdx
00C70018  73 08                           jae 0x140c70022
00C7001A  48 83 FA FF                     cmp rdx, -1
00C7001E  48 0F 45 CA                     cmovne rcx, rdx
00C70022  48 83 C0 08                     add rax, 8
00C70026  49 83 E9 01                     sub r9, 1
00C7002A  75 E6                           jne 0x140c70012
00C7002C  48 B8 00 00 00 00 00 00 01 00   movabs rax, 0x1000000000000
00C70036  48 3B C8                        cmp rcx, rax
00C70039  76 35                           jbe 0x140c70070
00C7003B  48 C1 E9 10                     shr rcx, 0x10
00C7003F  49 8B C5                        mov rax, r13
00C70042  48 8B 10                        mov rdx, qword ptr [rax]
00C70045  48 83 FA FF                     cmp rdx, -1
00C70049  74 07                           je 0x140c70052
00C7004B  48 C1 EA 10                     shr rdx, 0x10
00C7004F  48 89 10                        mov qword ptr [rax], rdx
00C70052  48 83 C0 08                     add rax, 8
00C70056  49 83 E8 01                     sub r8, 1
00C7005A  75 E6                           jne 0x140c70042
00C7005C  33 D2                           xor edx, edx
00C7005E  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00C70068  48 F7 F1                        div rcx
00C7006B  4C 8B C0                        mov r8, rax
00C7006E  EB 16                           jmp 0x140c70086
00C70070  33 D2                           xor edx, edx
00C70072  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00C7007C  48 F7 F1                        div rcx
00C7007F  4C 8B C0                        mov r8, rax
00C70082  85 FF                           test edi, edi
00C70084  74 2A                           je 0x140c700b0
00C70086  49 8B CD                        mov rcx, r13
00C70089  8B D7                           mov edx, edi
00C7008B  48 8B 01                        mov rax, qword ptr [rcx]
00C7008E  48 83 F8 FF                     cmp rax, -1
00C70092  74 0A                           je 0x140c7009e
00C70094  49 0F AF C0                     imul rax, r8
00C70098  48 C1 E8 30                     shr rax, 0x30
00C7009C  EB 05                           jmp 0x140c700a3
00C7009E  B8 FF FF 00 00                  mov eax, 0xffff
00C700A3  48 89 01                        mov qword ptr [rcx], rax
00C700A6  48 83 C1 08                     add rcx, 8
00C700AA  48 83 EA 01                     sub rdx, 1
00C700AE  75 DB                           jne 0x140c7008b
00C700B0  33 FF                           xor edi, edi
00C700B2  85 DB                           test ebx, ebx
00C700B4  0F 84 E7 00 00 00               je 0x140c701a1
00C700BA  4C 8D 1D FF F5 35 00            lea r11, [rip + 0x35f5ff]
00C700C1  48 89 5D B7                     mov qword ptr [rbp - 0x49], rbx
00C700C5  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
00C700C9  4C 8B D3                        mov r10, rbx
00C700CC  48 8B CB                        mov rcx, rbx
00C700CF  4D 8B 0B                        mov r9, qword ptr [r11]
00C700D2  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
00C700D7  66 41 39 01                     cmp word ptr [r9], ax
00C700DB  0F 85 A2 00 00 00               jne 0x140c70183
00C700E1  44 8B C7                        mov r8d, edi
00C700E4  8B D7                           mov edx, edi
00C700E6  3B D6                           cmp edx, esi
00C700E8  73 14                           jae 0x140c700fe
00C700EA  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00C700EE  8D 7A 01                        lea edi, [rdx + 1]
00C700F1  41 39 04 BC                     cmp dword ptr [r12 + rdi*4], eax
00C700F5  75 ED                           jne 0x140c700e4
00C700F7  44 8B C2                        mov r8d, edx
00C700FA  44 0F AF C6                     imul r8d, esi
00C700FE  48 8D 3D BB F5 35 00            lea rdi, [rip + 0x35f5bb]
00C70105  4D 8B F2                        mov r14, r10
00C70108  45 33 DB                        xor r11d, r11d
00C7010B  48 8B 17                        mov rdx, qword ptr [rdi]
00C7010E  0F B7 02                        movzx eax, word ptr [rdx]
00C70111  66 3B 42 02                     cmp ax, word ptr [rdx + 2]
00C70115  75 55                           jne 0x140c7016c
00C70117  41 0F B7 09                     movzx ecx, word ptr [r9]
00C7011B  0F AF CB                        imul ecx, ebx
00C7011E  03 C8                           add ecx, eax
00C70120  44 8B F9                        mov r15d, ecx
00C70123  49 81 7C CD 00 FF FF 00 00      cmp qword ptr [r13 + rcx*8], 0xffff
00C7012C  74 3A                           je 0x140c70168
00C7012E  41 8B CB                        mov ecx, r11d
00C70131  85 F6                           test esi, esi
00C70133  74 13                           je 0x140c70148
00C70135  44 8B 52 04                     mov r10d, dword ptr [rdx + 4]
00C70139  8D 51 01                        lea edx, [rcx + 1]
00C7013C  45 39 14 94                     cmp dword ptr [r12 + rdx*4], r10d
00C70140  74 06                           je 0x140c70148
00C70142  8B CA                           mov ecx, edx
00C70144  3B D6                           cmp edx, esi
00C70146  72 F1                           jb 0x140c70139
00C70148  43 0F B7 44 FD 00               movzx eax, word ptr [r13 + r15*8]
00C7014E  41 03 C8                        add ecx, r8d
00C70151  4C 8B 7D A7                     mov r15, qword ptr [rbp - 0x59]
00C70155  66 41 89 04 4F                  mov word ptr [r15 + rcx*2], ax
00C7015A  66 85 C0                        test ax, ax
00C7015D  75 0D                           jne 0x140c7016c
00C7015F  66 41 C7 04 4F 02 00            mov word ptr [r15 + rcx*2], 2
00C70166  EB 04                           jmp 0x140c7016c
00C70168  4C 8B 7D A7                     mov r15, qword ptr [rbp - 0x59]
00C7016C  48 83 C7 08                     add rdi, 8
00C70170  49 83 EE 01                     sub r14, 1
00C70174  75 95                           jne 0x140c7010b
00C70176  4C 8B 5D AF                     mov r11, qword ptr [rbp - 0x51]
00C7017A  4C 8B D3                        mov r10, rbx
00C7017D  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00C70181  33 FF                           xor edi, edi
00C70183  49 83 C3 08                     add r11, 8
00C70187  48 83 E9 01                     sub rcx, 1
00C7018B  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
00C7018F  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
00C70193  0F 85 36 FF FF FF               jne 0x140c700cf
00C70199  44 8B 75 9F                     mov r14d, dword ptr [rbp - 0x61]
00C7019D  44 8D 56 01                     lea r10d, [rsi + 1]
00C701A1  8B D7                           mov edx, edi
00C701A3  85 F6                           test esi, esi
00C701A5  74 11                           je 0x140c701b8
00C701A7  41 8B C2                        mov eax, r10d
00C701AA  0F AF C2                        imul eax, edx
00C701AD  FF C2                           inc edx
00C701AF  66 41 89 3C 47                  mov word ptr [r15 + rax*2], di
00C701B4  3B D6                           cmp edx, esi
00C701B6  72 EF                           jb 0x140c701a7
00C701B8  41 BF 0A 00 00 00               mov r15d, 0xa
00C701BE  48 8D 15 4B 91 00 00            lea rdx, [rip + 0x914b]
00C701C5  48 8D 4D 07                     lea rcx, [rbp + 7]
00C701C9  41 8B F7                        mov esi, r15d
00C701CC  E8 AF A5 7B FF                  call 0x14042a780
00C701D1  48 8D 15 A8 91 00 00            lea rdx, [rip + 0x91a8]
00C701D8  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00C701DC  E8 9F A5 7B FF                  call 0x14042a780
00C701E1  48 8D 45 07                     lea rax, [rbp + 7]
00C701E5  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00C701EA  0F 57 C0                        xorps xmm0, xmm0
00C701ED  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00C701F1  45 33 C9                        xor r9d, r9d
00C701F4  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00C701F8  4C 8D 45 D7                     lea r8, [rbp - 0x29]
00C701FC  C7 45 D7 30 00 00 00            mov dword ptr [rbp - 0x29], 0x30
00C70203  BA 3F 00 0F 00                  mov edx, 0xf003f
00C70208  48 89 7D DF                     mov qword ptr [rbp - 0x21], rdi
00C7020C  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00C70210  C7 45 EF 40 02 00 00            mov dword ptr [rbp - 0x11], 0x240
00C70217  F3 0F 7F 45 F7                  movdqu xmmword ptr [rbp - 9], xmm0
00C7021C  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C70221  E8 4A D2 A3 FF                  call 0x1406ad470
00C70226  85 C0                           test eax, eax
00C70228  78 46                           js 0x140c70270
00C7022A  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00C7022E  48 8D 45 A3                     lea rax, [rbp - 0x5d]
00C70232  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C70237  4C 8D 4D 17                     lea r9, [rbp + 0x17]
00C7023B  45 8D 47 F8                     lea r8d, [r15 - 8]
00C7023F  C7 44 24 20 14 00 00 00         mov dword ptr [rsp + 0x20], 0x14
00C70247  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00C7024B  E8 60 D1 A3 FF                  call 0x1406ad3b0
00C70250  85 C0                           test eax, eax
00C70252  78 21                           js 0x140c70275
00C70254  83 7D 1B 04                     cmp dword ptr [rbp + 0x1b], 4
00C70258  75 1B                           jne 0x140c70275
00C7025A  83 7D 1F 04                     cmp dword ptr [rbp + 0x1f], 4
00C7025E  75 15                           jne 0x140c70275
00C70260  8B 75 23                        mov esi, dword ptr [rbp + 0x23]
00C70263  8D 46 FF                        lea eax, [rsi - 1]
00C70266  83 F8 31                        cmp eax, 0x31
00C70269  76 0A                           jbe 0x140c70275
00C7026B  41 8B F7                        mov esi, r15d
00C7026E  EB 05                           jmp 0x140c70275
00C70270  48 83 4D 97 FF                  or qword ptr [rbp - 0x69], 0xffffffffffffffff
00C70275  44 8B CF                        mov r9d, edi
00C70278  85 DB                           test ebx, ebx
00C7027A  0F 84 79 01 00 00               je 0x140c703f9
00C70280  48 8D 15 39 F4 35 00            lea rdx, [rip + 0x35f439]
00C70287  4C 8B D2                        mov r10, rdx
00C7028A  49 8B 0A                        mov rcx, qword ptr [r10]
00C7028D  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
00C70291  66 39 01                        cmp word ptr [rcx], ax
00C70294  75 69                           jne 0x140c702ff
00C70296  44 8B DB                        mov r11d, ebx
00C70299  44 8B C7                        mov r8d, edi
00C7029C  45 0F AF D9                     imul r11d, r9d
00C702A0  44 3B C3                        cmp r8d, ebx
00C702A3  73 58                           jae 0x140c702fd
00C702A5  41 8B C0                        mov eax, r8d
00C702A8  48 8B 0C C2                     mov rcx, qword ptr [rdx + rax*8]
00C702AC  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
00C702B0  66 39 01                        cmp word ptr [rcx], ax
00C702B3  75 43                           jne 0x140c702f8
00C702B5  45 3B C8                        cmp r9d, r8d
00C702B8  74 3E                           je 0x140c702f8
00C702BA  0F B7 0D 3F 4D 35 00            movzx ecx, word ptr [rip + 0x354d3f]
00C702C1  43 8D 04 03                     lea eax, [r11 + r8]
00C702C5  41 8B 54 C5 00                  mov edx, dword ptr [r13 + rax*8]
00C702CA  48 8B 05 D7 4D 35 00            mov rax, qword ptr [rip + 0x354dd7]
00C702D1  41 0F AF C9                     imul ecx, r9d
00C702D5  41 03 C8                        add ecx, r8d
00C702D8  8B 3C 88                        mov edi, dword ptr [rax + rcx*4]
00C702DB  8B CA                           mov ecx, edx
00C702DD  8B C7                           mov eax, edi
00C702DF  2B C2                           sub eax, edx
00C702E1  2B CF                           sub ecx, edi
00C702E3  0F 49 C1                        cmovns eax, ecx
00C702E6  33 D2                           xor edx, edx
00C702E8  6B C0 64                        imul eax, eax, 0x64
00C702EB  F7 F6                           div esi
00C702ED  3B C7                           cmp eax, edi
00C702EF  77 23                           ja 0x140c70314
00C702F1  48 8D 15 C8 F3 35 00            lea rdx, [rip + 0x35f3c8]
00C702F8  41 FF C0                        inc r8d
00C702FB  EB A3                           jmp 0x140c702a0
00C702FD  33 FF                           xor edi, edi
00C702FF  41 FF C1                        inc r9d
00C70302  49 83 C2 08                     add r10, 8
00C70306  44 3B CB                        cmp r9d, ebx
00C70309  0F 82 7B FF FF FF               jb 0x140c7028a
00C7030F  E9 E5 00 00 00                  jmp 0x140c703f9
00C70314  48 83 7D 97 FF                  cmp qword ptr [rbp - 0x69], -1
00C70319  74 30                           je 0x140c7034b
00C7031B  48 8D 15 8E 90 00 00            lea rdx, [rip + 0x908e]
00C70322  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00C70326  E8 55 A4 7B FF                  call 0x14042a780
00C7032B  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00C7032F  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00C70333  41 B9 03 00 00 00               mov r9d, 3
00C70339  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00C7033E  45 33 C0                        xor r8d, r8d
00C70341  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C70346  E8 85 D9 A3 FF                  call 0x1406adcd0
00C7034B  44 0F B7 3D AD 4C 35 00         movzx r15d, word ptr [rip + 0x354cad]
00C70353  48 8D 0D 66 F3 35 00            lea rcx, [rip + 0x35f366]
00C7035A  4C 8B D9                        mov r11, rcx
00C7035D  33 FF                           xor edi, edi
00C7035F  4C 8B E3                        mov r12, rbx
00C70362  4D 8B 03                        mov r8, qword ptr [r11]
00C70365  41 0F B7 40 02                  movzx eax, word ptr [r8 + 2]
00C7036A  66 41 39 00                     cmp word ptr [r8], ax
00C7036E  74 04                           je 0x140c70374
00C70370  4C 8B 04 C1                     mov r8, qword ptr [rcx + rax*8]
00C70374  41 8B D7                        mov edx, r15d
00C70377  4D 8B F4                        mov r14, r12
00C7037A  0F AF D7                        imul edx, edi
00C7037D  4C 8D 25 3C F3 35 00            lea r12, [rip + 0x35f33c]
00C70384  48 8B F1                        mov rsi, rcx
00C70387  48 8B 06                        mov rax, qword ptr [rsi]
00C7038A  44 0F B7 10                     movzx r10d, word ptr [rax]
00C7038E  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
00C70392  66 44 3B D1                     cmp r10w, cx
00C70396  74 08                           je 0x140c703a0
00C70398  49 8B 04 CC                     mov rax, qword ptr [r12 + rcx*8]
00C7039C  44 0F B7 10                     movzx r10d, word ptr [rax]
00C703A0  41 0F B7 00                     movzx eax, word ptr [r8]
00C703A4  66 41 3B C2                     cmp ax, r10w
00C703A8  75 0D                           jne 0x140c703b7
00C703AA  48 8B 05 F7 4C 35 00            mov rax, qword ptr [rip + 0x354cf7]
00C703B1  83 24 90 00                     and dword ptr [rax + rdx*4], 0
00C703B5  EB 1A                           jmp 0x140c703d1
00C703B7  8B C8                           mov ecx, eax
00C703B9  41 0F B7 C2                     movzx eax, r10w
00C703BD  0F AF CB                        imul ecx, ebx
00C703C0  03 C8                           add ecx, eax
00C703C2  48 8B 05 DF 4C 35 00            mov rax, qword ptr [rip + 0x354cdf]
00C703C9  41 8B 4C CD 00                  mov ecx, dword ptr [r13 + rcx*8]
00C703CE  89 0C 90                        mov dword ptr [rax + rdx*4], ecx
00C703D1  FF C2                           inc edx
00C703D3  48 83 C6 08                     add rsi, 8
00C703D7  49 83 EE 01                     sub r14, 1
00C703DB  75 AA                           jne 0x140c70387
00C703DD  FF C7                           inc edi
00C703DF  48 8D 0D DA F2 35 00            lea rcx, [rip + 0x35f2da]
00C703E6  49 83 C3 08                     add r11, 8
00C703EA  4C 8B E3                        mov r12, rbx
00C703ED  3B FB                           cmp edi, ebx
00C703EF  0F 82 6D FF FF FF               jb 0x140c70362
00C703F5  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
00C703F9  33 D2                           xor edx, edx
00C703FB  49 8B CD                        mov rcx, r13
00C703FE  E8 6D 24 F1 FF                  call 0x140b82870
00C70403  4D 85 E4                        test r12, r12
00C70406  74 0A                           je 0x140c70412
00C70408  33 D2                           xor edx, edx
00C7040A  49 8B CC                        mov rcx, r12
00C7040D  E8 5E 24 F1 FF                  call 0x140b82870
00C70412  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00C70416  48 83 F9 FF                     cmp rcx, -1
00C7041A  74 05                           je 0x140c70421
00C7041C  E8 8F CE A3 FF                  call 0x1406ad2b0
00C70421  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
00C70425  48 33 CC                        xor rcx, rsp
00C70428  E8 13 C2 A3 FF                  call 0x1406ac640
00C7042D  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00C70435  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00C70439  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00C7043D  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00C70441  49 8B E3                        mov rsp, r11
00C70444  41 5F                           pop r15
00C70446  41 5E                           pop r14
00C70448  41 5D                           pop r13
00C7044A  41 5C                           pop r12
00C7044C  5D                              pop rbp
00C7044D  C3                              ret
00C7044E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SaveNodeDistanceInformation(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 1681590)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    result = 0;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = 0;
    *(unsigned int *)(v_rsp - 95 - 1) = 0;
    *(unsigned int *)(v_rsp - 95 - 93) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = v_xmm0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)) == 0) goto loc_00C6FEF7;
loc_00C6FED1:
    v_rsi = (unsigned int)((0) + 1);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536910)))) != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536910) + 2))) { v_rsi = 0; }
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) - (1);
    if (condition_is_not_equal) goto loc_00C6FED1;
    if (((unsigned int)(v_rsi)) == 1) goto loc_00C70421;
    v_rdi = 0;
loc_00C6FEF7:
    result = KeQueryNumaCosts(a1, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536910)), v_rip + 3536910 + 8, a4);
    if (result == 0) goto loc_00C70412;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241) - 1) == 0) goto loc_00C6FF69;
loc_00C6FF14:
    if (((unsigned int)(0 + 1)) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) goto loc_00C6FF61;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) * (0));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(0 + 1)));
loc_00C6FF29:
    if ((*(unsigned __int64 *)(result + v_rdi * 8)) != -1) {
        result = (unsigned int)(*(unsigned __int16 *)(v_rip + 3494241));
        a1 = (*(unsigned __int64 *)(result + v_rdi * 8)) >> (1);
        result = (unsigned int)((result) * ((unsigned int)((unsigned int)((unsigned int)(0 + 1)))));
        result = (unsigned int)((result) + (0));
        a2 = (unsigned int)(result);
        result = *(unsigned __int64 *)(result + result * 8);
        result = (result) >> (1);
        a1 = (a1) + (result);
        *(unsigned __int64 *)(result + v_rdi * 8) = a1;
        *(unsigned __int64 *)(result + a2 * 8) = a1;
    }
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(0 + 1))) + 1);
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_r10)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) goto loc_00C6FF29;
loc_00C6FF61:
    if (((unsigned int)(0 + 1)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241) - 1))) goto loc_00C6FF14;
loc_00C6FF69:
    result = (unsigned int)((v_rsi + 2) * ((unsigned int)(v_rsi)));
    *(unsigned int *)(v_rsp - 95 - 97) = (unsigned int)(result * 2 + 4);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result * 2 + 4)), (unsigned int)(0x2020654BULL), 0 + 1);
    *(unsigned __int64 *)(v_rsp - 95 - 49) = result;
    if (result == 0) goto loc_00C703F9;
    *(unsigned int *)(result) = (unsigned int)(v_rsi);
    *(unsigned __int64 *)(v_rsp - 95 - 89) = result + v_rsi + 1 * 4;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)) == 0) goto loc_00C6FFE3;
loc_00C6FFC0:
    result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536643) + 2);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536643))) == ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536643) + 2)))) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3536643) + 4);
        a1 = 1;
        a3 = (unsigned int)((1) + 1);
        *(unsigned int *)(result + a1 * 4) = (unsigned int)(result);
    }
    a2 = (v_rip + 3536643) + (8);
    a4 = (*(unsigned __int16 *)(v_rip + 3494241)) - (1);
    if (condition_is_not_equal) goto loc_00C6FFC0;
loc_00C6FFE3:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) * ((unsigned int)(v_rsi)));
    v_rdi = *(unsigned __int64 *)(v_rip + 3536643);
    if ((unsigned int)(result) != 0) {
        a1 = (unsigned int)(result);
        v_rdi = result + v_rsi + 1 * 4;
        result = (unsigned int)((unsigned int)(0xFFFFULL));
    }
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) * ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241))));
    if ((unsigned int)(v_rdi) == 0) goto loc_00C70070;
loc_00C70012:
    if (1 < (*(unsigned __int64 *)(result))) {
        a1 = 1;
        if ((*(unsigned __int64 *)(result)) != -1) { a1 = *(unsigned __int64 *)(result); }
    }
    result = (result) + (8);
    a4 = ((unsigned int)((unsigned int)(v_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00C70012;
    if (a1 <= result) goto loc_00C70070;
    a1 = (a1) >> (16);
loc_00C70042:
    if ((*(unsigned __int64 *)(result)) != -1) {
        a2 = (*(unsigned __int64 *)(result)) >> (16);
        *(unsigned __int64 *)(result) = a2;
    }
    result = (result) + (8);
    a3 = ((unsigned int)((unsigned int)(v_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00C70042;
    a2 = 0;
    goto loc_00C70086;
loc_00C70070:
    a2 = 0;
    if ((unsigned int)(v_rdi) == 0) goto loc_00C700B0;
loc_00C70086:
loc_00C7008B:
    if ((*(unsigned __int64 *)(result)) == -1) goto loc_00C7009E;
    result = (*(unsigned __int64 *)(result)) * (result);
    result = (result) >> (48);
    goto loc_00C700A3;
loc_00C7009E:
loc_00C700A3:
    *(unsigned __int64 *)(result) = (unsigned int)(0xFFFFULL);
    a1 = (result) + (8);
    a2 = ((unsigned int)((unsigned int)(v_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00C7008B;
loc_00C700B0:
    v_rdi = 0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)) == 0) goto loc_00C701A1;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = *(unsigned __int16 *)(v_rip + 3494241);
    *(unsigned __int64 *)(v_rsp - 95 - 81) = v_rip + 3536383;
loc_00C700CF:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536383))) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536383) + 2)))) goto loc_00C70183;
loc_00C700E4:
    if (0 >= ((unsigned int)(v_rsi))) goto loc_00C700FE;
    if ((*(unsigned int *)(result + 0 + 1 * 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3536383) + 4))))) goto loc_00C700E4;
    a3 = (unsigned int)((0) * ((unsigned int)(v_rsi)));
loc_00C700FE:
    v_r11 = 0;
loc_00C7010B:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536315)))) != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536315) + 2))) goto loc_00C7016C;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536383))) * ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241))));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3536315)))));
    if ((*(unsigned __int64 *)(result + a1 * 8)) == 0xFFFFULL) goto loc_00C70168;
    if ((unsigned int)(v_rsi) == 0) goto loc_00C70148;
loc_00C70139:
    if ((*(unsigned int *)(result + 0 + 1 * 4)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3536315) + 4))))) goto loc_00C70148;
    if (((unsigned int)(0 + 1)) < ((unsigned int)(v_rsi))) goto loc_00C70139;
loc_00C70148:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(0 + 1))) + ((unsigned int)(a3)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(result + (unsigned int)((unsigned int)(a1)) * 8));
    if ((unsigned __int16)(*(unsigned __int16 *)(result + (unsigned int)((unsigned int)(a1)) * 8)) != 0) goto loc_00C7016C;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89) + a1 * 2) = 2;
    goto loc_00C7016C;
loc_00C70168:
loc_00C7016C:
    v_rdi = (v_rip + 3536315) + (8);
    v_r14 = (*(unsigned __int16 *)(v_rip + 3494241)) - (1);
    if (condition_is_not_equal) goto loc_00C7010B;
    v_rdi = 0;
loc_00C70183:
    v_r11 = (*(unsigned __int64 *)(v_rsp - 95 - 81)) + (8);
    a1 = (*(unsigned __int64 *)(v_rsp - 95 - 73)) - (1);
    *(unsigned __int64 *)(v_rsp - 95 - 81) = v_r11;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = a1;
    if (condition_is_not_equal) goto loc_00C700CF;
loc_00C701A1:
    if ((unsigned int)(v_rsi) == 0) goto loc_00C701B8;
loc_00C701A7:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + 1))) * (0));
    a2 = (unsigned int)((0) + 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89) + result * 2) = 0;
    if (((unsigned int)(a2)) < ((unsigned int)(v_rsi))) goto loc_00C701A7;
loc_00C701B8:
    result = RtlInitUnicodeString(v_rsp - 95 + 7, v_rip + 37195, a3, *(unsigned __int64 *)(v_rip + 3536383));
    result = RtlInitUnicodeString(v_rsp - 95 - 65, v_rip + 37288, a3, *(unsigned __int64 *)(v_rip + 3536383));
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_rsp - 95 + 7;
    *(unsigned int *)(v_rsp - 95 - 41) = 48;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned int *)(v_rsp - 95 - 17) = 576;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    v_stack_mE8 = 0;
    result = ZwCreateKey(v_rsp - 95 - 105, (unsigned int)(0xF003FULL), v_rsp - 95 - 41, a4);
    if (sign_flag) goto loc_00C70270;
    v_stack_mE0 = v_rsp - 95 - 93;
    v_stack_mE8 = 20;
    result = ZwQueryValueKey(*(unsigned __int64 *)(v_rsp - 95 - 105), v_rsp - 95 - 65, 10 - 8, v_rsp - 95 + 23);
    if (sign_flag) goto loc_00C70275;
    if ((*(unsigned int *)(v_rsp - 95 + 27)) != 4) goto loc_00C70275;
    if ((*(unsigned int *)(v_rsp - 95 + 31)) != 4) goto loc_00C70275;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 35)) - 1)) <= 49) goto loc_00C70275;
    goto loc_00C70275;
loc_00C70270:
loc_00C70275:
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)) == 0) goto loc_00C703F9;
loc_00C7028A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535929))) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535929) + 2)))) goto loc_00C702FF;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) * (0));
loc_00C702A0:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) goto loc_00C702FD;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535929 + 0 * 8))) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535929 + 0 * 8) + 2)))) goto loc_00C702F8;
    if (0 == 0) goto loc_00C702F8;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 3493183)) * (0));
    a1 = (unsigned int)((a1) + (0));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3493335) + a1 * 4))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_r11 + 0 * 1 * 8)))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + v_r11 + 0 * 1 * 8))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3493335) + a1 * 4)))));
    if (!sign_flag) { result = (unsigned int)(a1); }
    a2 = 0;
    result = (unsigned int)((result) * ((unsigned int)(result)));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3493335) + a1 * 4))))) goto loc_00C70314;
loc_00C702F8:
    a3 = (unsigned int)((0) + 1);
    goto loc_00C702A0;
loc_00C702FD:
    v_rdi = 0;
loc_00C702FF:
    a4 = (unsigned int)((0) + 1);
    v_r10 = (v_rip + 3535929) + (8);
    if (((unsigned int)(a4)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) goto loc_00C7028A;
    goto loc_00C703F9;
loc_00C70314:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 105)) != -1) {
        a2 = v_rip + 37006;
        a1 = v_rsp - 95 - 65;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 105);
        a2 = v_rsp - 95 - 65;
        a4 = 3;
        v_stack_mE0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)));
        a3 = 0;
        v_stack_mE8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
    }
    v_rdi = 0;
loc_00C70362:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718))) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718) + 2)))) {
        a3 = *(unsigned __int64 *)(v_rip + 3535718 + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718) + 2) * 8);
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3493037)))) * (0));
loc_00C70387:
    result = *(unsigned __int64 *)(v_rip + 3535718);
    v_r10 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718)))) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718) + 2)))) {
        result = *(unsigned __int64 *)(v_rip + 3535676 + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3535718) + 2) * 8);
        v_r10 = *(unsigned __int16 *)(result);
    }
    if (((unsigned __int16)(*(unsigned __int16 *)(a3))) != ((unsigned __int16)(v_r10))) goto loc_00C703B7;
    goto loc_00C703D1;
loc_00C703B7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 3493111)))) * ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241))));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int16)(v_r10))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3493087) + a2 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 8)));
loc_00C703D1:
    a2 = (unsigned int)((a2) + 1);
    v_rsi = (v_rip + 3535718) + (8);
    v_r14 = (*(unsigned __int16 *)(v_rip + 3494241)) - (1);
    if (condition_is_not_equal) goto loc_00C70387;
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_r11 = (v_rip + 3535718) + (8);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3494241)))) goto loc_00C70362;
loc_00C703F9:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rsp - 95 - 49) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 49);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(v_rsp - 95 - 105)) != -1) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 95 - 105), a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
void SaveNodeDistanceInformation(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x19A8B6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    result = 0;
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = v_xmm0;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)) == 0) goto loc_00C6FEF7;
loc_00C6FED1:
    local_rsi = (uint32_t)((0) + 1);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F80E)))) != (*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F80E) + 0x2))) { local_rsi = 0; }
    a4 = ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) - (1);
    if (condition_is_not_equal) goto loc_00C6FED1;
    if (((uint32_t)(local_rsi)) == 1) goto loc_00C70421;
    local_rdi = 0;
loc_00C6FEF7:
    result = KeQueryNumaCosts(a1, *(uint16_t *)(*(uint64_t *)(v_rip + 0x35F80E)), v_rip + 3536910 + 8, a4);
    if (result == 0) goto loc_00C70412;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x355161) - 1) == 0) goto loc_00C6FF69;
loc_00C6FF14:
    if (((uint32_t)(0 + 1)) >= ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) goto loc_00C6FF61;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) * (0));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(0 + 1)));
loc_00C6FF29:
    if ((*(uint64_t *)(result + local_rdi * 8)) != -1) {
        result = (uint32_t)(*(uint16_t *)(v_rip + 0x355161));
        a1 = (*(uint64_t *)(result + local_rdi * 8)) >> (1);
        result = (uint32_t)((result) * ((uint32_t)((uint32_t)((uint32_t)(0 + 1)))));
        result = (uint32_t)((result) + (0));
        a2 = (uint32_t)(result);
        result = *(uint64_t *)(result + result * 8);
        result = (result) >> (1);
        a1 = (a1) + (result);
        *(uint64_t *)(result + local_rdi * 8) = a1;
        *(uint64_t *)(result + a2 * 8) = a1;
    }
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(0 + 1))) + 1);
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_r10)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) goto loc_00C6FF29;
loc_00C6FF61:
    if (((uint32_t)(0 + 1)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x355161) - 1))) goto loc_00C6FF14;
loc_00C6FF69:
    result = (uint32_t)((local_rsi + 2) * ((uint32_t)(local_rsi)));
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = (uint32_t)(result * 2 + 4);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result * 2 + 4)), (uint32_t)(0x2020654BULL), 0 + 1);
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = result;
    if (result == 0) goto loc_00C703F9;
    *(uint32_t *)(result) = (uint32_t)(local_rsi);
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = result + local_rsi + 1 * 4;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)) == 0) goto loc_00C6FFE3;
loc_00C6FFC0:
    result = *(uint16_t *)(*(uint64_t *)(v_rip + 0x35F703) + 0x2);
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F703))) == ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F703) + 0x2)))) {
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x35F703) + 0x4);
        a1 = 1;
        a3 = (uint32_t)((1) + 1);
        *(uint32_t *)(result + a1 * 4) = (uint32_t)(result);
    }
    a2 = (v_rip + 3536643) + (8);
    a4 = (*(uint16_t *)(v_rip + 0x355161)) - (1);
    if (condition_is_not_equal) goto loc_00C6FFC0;
loc_00C6FFE3:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) * ((uint32_t)(local_rsi)));
    local_rdi = *(uint64_t *)(v_rip + 0x35F703);
    if ((uint32_t)(result) != 0) {
        a1 = (uint32_t)(result);
        local_rdi = result + local_rsi + 1 * 4;
        result = (uint32_t)((uint32_t)(0xFFFFULL));
    }
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) * ((uint32_t)(*(uint16_t *)(v_rip + 0x355161))));
    if ((uint32_t)(local_rdi) == 0) goto loc_00C70070;
loc_00C70012:
    if (1 < (*(uint64_t *)(result))) {
        a1 = 1;
        if ((*(uint64_t *)(result)) != -1) { a1 = *(uint64_t *)(result); }
    }
    result = (result) + (8);
    a4 = ((uint32_t)((uint32_t)(local_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00C70012;
    if (a1 <= result) goto loc_00C70070;
    a1 = (a1) >> (16);
loc_00C70042:
    if ((*(uint64_t *)(result)) != -1) {
        a2 = (*(uint64_t *)(result)) >> (16);
        *(uint64_t *)(result) = a2;
    }
    result = (result) + (8);
    a3 = ((uint32_t)((uint32_t)(local_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00C70042;
    a2 = 0;
    goto loc_00C70086;
loc_00C70070:
    a2 = 0;
    if ((uint32_t)(local_rdi) == 0) goto loc_00C700B0;
loc_00C70086:
loc_00C7008B:
    if ((*(uint64_t *)(result)) == -1) goto loc_00C7009E;
    result = (*(uint64_t *)(result)) * (result);
    result = (result) >> (48);
    goto loc_00C700A3;
loc_00C7009E:
loc_00C700A3:
    *(uint64_t *)(result) = (uint32_t)(0xFFFFULL);
    a1 = (result) + (8);
    a2 = ((uint32_t)((uint32_t)(local_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00C7008B;
loc_00C700B0:
    local_rdi = 0;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)) == 0) goto loc_00C701A1;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = *(uint16_t *)(v_rip + 0x355161);
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = v_rip + 3536383;
loc_00C700CF:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F5FF))) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F5FF) + 0x2)))) goto loc_00C70183;
loc_00C700E4:
    if (0 >= ((uint32_t)(local_rsi))) goto loc_00C700FE;
    if ((*(uint32_t *)(result + 0x0 + 0x1 * 4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x35F5FF) + 0x4))))) goto loc_00C700E4;
    a3 = (uint32_t)((0) * ((uint32_t)(local_rsi)));
loc_00C700FE:
    local_r11 = 0;
loc_00C7010B:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F5BB)))) != (*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F5BB) + 0x2))) goto loc_00C7016C;
    a1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F5FF))) * ((uint32_t)(*(uint16_t *)(v_rip + 0x355161))));
    a1 = (uint32_t)((a1) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F5BB)))));
    if ((*(uint64_t *)(result + a1 * 8)) == 0xFFFFULL) goto loc_00C70168;
    if ((uint32_t)(local_rsi) == 0) goto loc_00C70148;
loc_00C70139:
    if ((*(uint32_t *)(result + 0x0 + 0x1 * 4)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x35F5BB) + 0x4))))) goto loc_00C70148;
    if (((uint32_t)(0 + 1)) < ((uint32_t)(local_rsi))) goto loc_00C70139;
loc_00C70148:
    a1 = (uint32_t)(((uint32_t)((uint32_t)(0 + 1))) + ((uint32_t)(a3)));
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59) + a1 * 2) = (uint16_t)(*(uint16_t *)(result + (uint32_t)((uint32_t)(a1)) * 8));
    if ((uint16_t)(*(uint16_t *)(result + (uint32_t)((uint32_t)(a1)) * 8)) != 0) goto loc_00C7016C;
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59) + a1 * 2) = 2;
    goto loc_00C7016C;
loc_00C70168:
loc_00C7016C:
    local_rdi = (v_rip + 3536315) + (8);
    local_r14 = (*(uint16_t *)(v_rip + 0x355161)) - (1);
    if (condition_is_not_equal) goto loc_00C7010B;
    local_rdi = 0;
loc_00C70183:
    local_r11 = (*(uint64_t *)(local_rsp - 0x5F - 0x51)) + (8);
    a1 = (*(uint64_t *)(local_rsp - 0x5F - 0x49)) - (1);
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = local_r11;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = a1;
    if (condition_is_not_equal) goto loc_00C700CF;
loc_00C701A1:
    if ((uint32_t)(local_rsi) == 0) goto loc_00C701B8;
loc_00C701A7:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + 1))) * (0));
    a2 = (uint32_t)((0) + 1);
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59) + result * 2) = 0;
    if (((uint32_t)(a2)) < ((uint32_t)(local_rsi))) goto loc_00C701A7;
loc_00C701B8:
    result = RtlInitUnicodeString(local_rsp - 95 + 7, v_rip + 37195, a3, *(uint64_t *)(v_rip + 0x35F5FF));
    result = RtlInitUnicodeString(local_rsp - 95 - 65, v_rip + 37288, a3, *(uint64_t *)(v_rip + 0x35F5FF));
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    a4 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = local_rsp - 95 + 7;
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = 48;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = 576;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    v_stack_mE8 = 0;
    result = ZwCreateKey(local_rsp - 95 - 105, (uint32_t)(0xF003FULL), local_rsp - 95 - 41, a4);
    if (sign_flag) goto loc_00C70270;
    v_stack_mE0 = local_rsp - 95 - 93;
    v_stack_mE8 = 20;
    result = ZwQueryValueKey(*(uint64_t *)(local_rsp - 0x5F - 0x69), local_rsp - 95 - 65, 10 - 8, local_rsp - 95 + 23);
    if (sign_flag) goto loc_00C70275;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1B)) != 4) goto loc_00C70275;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1F)) != 4) goto loc_00C70275;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x23)) - 1)) <= 49) goto loc_00C70275;
    goto loc_00C70275;
loc_00C70270:
loc_00C70275:
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)) == 0) goto loc_00C703F9;
loc_00C7028A:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F439))) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F439) + 0x2)))) goto loc_00C702FF;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) * (0));
loc_00C702A0:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) goto loc_00C702FD;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F439 + 0x0 * 8))) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F439 + 0x0 * 8) + 0x2)))) goto loc_00C702F8;
    if (0 == 0) goto loc_00C702F8;
    a1 = (uint32_t)((*(uint16_t *)(v_rip + 0x354D3F)) * (0));
    a1 = (uint32_t)((a1) + (0));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x354DD7) + a1 * 4))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + local_r11 + 0x0 * 1 * 8)))));
    a1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + local_r11 + 0x0 * 1 * 8))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x354DD7) + a1 * 4)))));
    if (!sign_flag) { result = (uint32_t)(a1); }
    a2 = 0;
    result = (uint32_t)((result) * ((uint32_t)(result)));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x354DD7) + a1 * 4))))) goto loc_00C70314;
loc_00C702F8:
    a3 = (uint32_t)((0) + 1);
    goto loc_00C702A0;
loc_00C702FD:
    local_rdi = 0;
loc_00C702FF:
    a4 = (uint32_t)((0) + 1);
    local_r10 = (v_rip + 3535929) + (8);
    if (((uint32_t)(a4)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) goto loc_00C7028A;
    goto loc_00C703F9;
loc_00C70314:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x69)) != -1) {
        a2 = v_rip + 37006;
        a1 = local_rsp - 95 - 65;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
        a1 = *(uint64_t *)(local_rsp - 0x5F - 0x69);
        a2 = local_rsp - 95 - 65;
        a4 = 3;
        v_stack_mE0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)));
        a3 = 0;
        v_stack_mE8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
    }
    local_rdi = 0;
loc_00C70362:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366))) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366) + 0x2)))) {
        a3 = *(uint64_t *)(v_rip + 0x35F366 + *(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366) + 0x2) * 8);
    }
    a2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x354CAD)))) * (0));
loc_00C70387:
    result = *(uint64_t *)(v_rip + 0x35F366);
    local_r10 = *(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366)))) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366) + 0x2)))) {
        result = *(uint64_t *)(v_rip + 0x35F33C + *(uint16_t *)(*(uint64_t *)(v_rip + 0x35F366) + 0x2) * 8);
        local_r10 = *(uint16_t *)(result);
    }
    if (((uint16_t)(*(uint16_t *)(a3))) != ((uint16_t)(local_r10))) goto loc_00C703B7;
    goto loc_00C703D1;
loc_00C703B7:
    a1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x354CF7)))) * ((uint32_t)(*(uint16_t *)(v_rip + 0x355161))));
    a1 = (uint32_t)((a1) + ((uint32_t)((uint16_t)(local_r10))));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x354CDF) + a2 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(result + a1 * 8)));
loc_00C703D1:
    a2 = (uint32_t)((a2) + 1);
    local_rsi = (v_rip + 3535718) + (8);
    local_r14 = (*(uint16_t *)(v_rip + 0x355161)) - (1);
    if (condition_is_not_equal) goto loc_00C70387;
    local_rdi = (uint32_t)((local_rdi) + 1);
    local_r11 = (v_rip + 3535718) + (8);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x355161)))) goto loc_00C70362;
loc_00C703F9:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x31) != 0) {
        a2 = 0;
        a1 = *(uint64_t *)(local_rsp - 0x5F - 0x31);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x69)) != -1) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x5F - 0x69), a2, a3, a4);
    }
    a1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6FE60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
