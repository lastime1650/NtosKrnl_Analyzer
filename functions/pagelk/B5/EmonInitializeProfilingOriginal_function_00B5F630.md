# EmonInitializeProfilingOriginal

- RVA: `0x00B5F630`–`0x00B5FA49` (길이 `1,049` bytes)
- VA: `0x0000000140B5F630`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF128`
- 디코드: `278`개 명령, `1,049/1,049` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x00B5F6DB` → [HalpQueryMaximumRegisteredProcessorCount](../../text/54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (function, `0x00543BE8`)
- `0x00B5F712` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B5F735` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B5F77A` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B5F79B` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B5F927` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00B5F957` → [EmonFreeCounterOriginal](../../text/55/EmonFreeCounterOriginal_function_0055CEDC.md) (function, `0x0055CEDC`)
- `0x00B5F993` → [EmonFreeCounterOriginal](../../text/55/EmonFreeCounterOriginal_function_0055CEDC.md) (function, `0x0055CEDC`)
- `0x00B5F9B7` → [EmonInitializePebs](EmonInitializePebs_function_00B5F230.md) (function, `0x00B5F230`)
- `0x00B5FA25` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B5F64C` → RVA `0x00E0A740` (`.data`; read)
- `0x00B5F6B2` → RVA `0x00F8FE10` (`.data`; write)
- `0x00B5F6B8` → RVA `0x00F8FDF8` (`.data`; write)
- `0x00B5F6BF` → RVA `0x00F8FDE0` (`.data`; write)
- `0x00B5F6D5` → RVA `0x00F8FE14` (`.data`; write)
- `0x00B5F7FC` → RVA `0x00FC2BD0` (`.data`; read/write)
- `0x00B5F804` → RVA `0x00025D68` (`.rdata`; read)
- `0x00B5F80B` → RVA `0x00F8FDE8` (`.data`; read/write)
- `0x00B5F813` → RVA `0x00FC2C40` (`.data`; read)
- `0x00B5F81A` → RVA `0x00FC2BC8` (`.data`; write)
- `0x00B5F821` → RVA `0x00F8FE00` (`.data`; read)
- `0x00B5F828` → RVA `0x00F8FE08` (`.data`; write)
- `0x00B5F82F` → RVA `0x00F8FE00` (`.data`; write)
- `0x00B5F836` → RVA `0x00FC2C48` (`.data`; write)
- `0x00B5F83D` → RVA `0x00FC2C40` (`.data`; write)
- `0x00B5F853` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B5F86E` → RVA `0x00FC2C48` (`.data`; read)
- `0x00B5F87A` → RVA `0x00FC2C20` (`.data`; read/write)
- `0x00B5F8D6` → RVA `0x00E03DC4` (`.data`; read)
- `0x00B5F8DF` → RVA `0x00E03CB0` (`.data`; read)
- `0x00B5F910` → RVA `0x00F8F980` (`.data`; read)
- `0x00B5F9DB` → RVA `0x00F8FDF8` (`.data`; read)
- `0x00B5F9E2` → RVA `0x00F8FE28` (`.data`; write)
- `0x00B5F9FF` → RVA `0x00F8FDE0` (`.data`; read)
- `0x00B5FA08` → RVA `0x00F8FE28` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00B5F6DB` → [HalpQueryMaximumRegisteredProcessorCount](../../text/54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (`PAGELK` → `.text`)
  - `0x00B5F712` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B5F735` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B5F77A` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B5F79B` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B5F927` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGELK` → `.text`)
  - `0x00B5F957` → [EmonFreeCounterOriginal](../../text/55/EmonFreeCounterOriginal_function_0055CEDC.md) (`PAGELK` → `.text`)
  - `0x00B5F993` → [EmonFreeCounterOriginal](../../text/55/EmonFreeCounterOriginal_function_0055CEDC.md) (`PAGELK` → `.text`)
  - `0x00B5FA25` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5F630  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B5F635  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00B5F63A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00B5F63F  57                              push rdi
00B5F640  41 54                           push r12
00B5F642  41 55                           push r13
00B5F644  41 56                           push r14
00B5F646  41 57                           push r15
00B5F648  48 83 EC 50                     sub rsp, 0x50
00B5F64C  48 8B 05 ED B0 2A 00            mov rax, qword ptr [rip + 0x2ab0ed]
00B5F653  48 33 C4                        xor rax, rsp
00B5F656  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B5F65B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B5F664  45 33 FF                        xor r15d, r15d
00B5F667  65 44 8B 2C 25 A4 01 00 00      mov r13d, dword ptr gs:[0x1a4]
00B5F670  33 C9                           xor ecx, ecx
00B5F672  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B5F677  40 32 F6                        xor sil, sil
00B5F67A  41 8D 47 0A                     lea eax, [r15 + 0xa]
00B5F67E  0F A2                           cpuid
00B5F680  44 8B C0                        mov r8d, eax
00B5F683  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00B5F687  C1 E8 18                        shr eax, 0x18
00B5F68A  44 8B CB                        mov r9d, ebx
00B5F68D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B5F691  45 85 ED                        test r13d, r13d
00B5F694  0F 85 03 02 00 00               jne 0x140b5f89d
00B5F69A  41 0F B6 C8                     movzx ecx, r8b
00B5F69E  41 8B C0                        mov eax, r8d
00B5F6A1  C1 E8 08                        shr eax, 8
00B5F6A4  33 FF                           xor edi, edi
00B5F6A6  41 C1 E8 10                     shr r8d, 0x10
00B5F6AA  44 0F B6 F0                     movzx r14d, al
00B5F6AE  41 0F B6 C0                     movzx eax, r8b
00B5F6B2  89 05 58 07 43 00               mov dword ptr [rip + 0x430758], eax
00B5F6B8  40 88 35 39 07 43 00            mov byte ptr [rip + 0x430739], sil
00B5F6BF  89 0D 1B 07 43 00               mov dword ptr [rip + 0x43071b], ecx
00B5F6C5  83 F9 02                        cmp ecx, 2
00B5F6C8  72 11                           jb 0x140b5f6db
00B5F6CA  8B FA                           mov edi, edx
00B5F6CC  83 E7 0F                        and edi, 0xf
00B5F6CF  C1 EA 05                        shr edx, 5
00B5F6D2  0F B6 C2                        movzx eax, dl
00B5F6D5  89 05 39 07 43 00               mov dword ptr [rip + 0x430739], eax
00B5F6DB  E8 08 45 9E FF                  call 0x140543be8
00B5F6E0  44 8B E0                        mov r12d, eax
00B5F6E3  33 ED                           xor ebp, ebp
00B5F6E5  41 3B EC                        cmp ebp, r12d
00B5F6E8  0F 83 0E 01 00 00               jae 0x140b5f7fc
00B5F6EE  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00B5F6F3  48 8D 1C 6D 00 00 00 00         lea rbx, [rbp*2]
00B5F6FB  48 03 DD                        add rbx, rbp
00B5F6FE  42 8D 0C B5 00 00 00 00         lea ecx, [r14*4]
00B5F706  48 C1 E3 05                     shl rbx, 5
00B5F70A  48 03 58 58                     add rbx, qword ptr [rax + 0x58]
00B5F70E  85 C9                           test ecx, ecx
00B5F710  74 08                           je 0x140b5f71a
00B5F712  E8 5D 52 9E FF                  call 0x140544974
00B5F717  4C 8B F8                        mov r15, rax
00B5F71A  4D 85 FF                        test r15, r15
00B5F71D  0F 84 D6 00 00 00               je 0x140b5f7f9
00B5F723  83 23 00                        and dword ptr [rbx], 0
00B5F726  43 8D 0C 76                     lea ecx, [r14 + r14*2]
00B5F72A  C1 E1 04                        shl ecx, 4
00B5F72D  44 89 73 04                     mov dword ptr [rbx + 4], r14d
00B5F731  85 C9                           test ecx, ecx
00B5F733  74 09                           je 0x140b5f73e
00B5F735  E8 3A 52 9E FF                  call 0x140544974
00B5F73A  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00B5F73E  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00B5F742  48 85 C0                        test rax, rax
00B5F745  0F 84 AE 00 00 00               je 0x140b5f7f9
00B5F74B  45 85 F6                        test r14d, r14d
00B5F74E  74 1F                           je 0x140b5f76f
00B5F750  48 83 C0 10                     add rax, 0x10
00B5F754  49 8B CF                        mov rcx, r15
00B5F757  49 8B D6                        mov rdx, r14
00B5F75A  83 60 0C 00                     and dword ptr [rax + 0xc], 0
00B5F75E  48 89 08                        mov qword ptr [rax], rcx
00B5F761  48 83 C1 04                     add rcx, 4
00B5F765  48 8D 40 30                     lea rax, [rax + 0x30]
00B5F769  48 83 EA 01                     sub rdx, 1
00B5F76D  75 EB                           jne 0x140b5f75a
00B5F76F  8D 0C BD 00 00 00 00            lea ecx, [rdi*4]
00B5F776  85 C9                           test ecx, ecx
00B5F778  74 0D                           je 0x140b5f787
00B5F77A  E8 F5 51 9E FF                  call 0x140544974
00B5F77F  4C 8B F8                        mov r15, rax
00B5F782  48 85 C0                        test rax, rax
00B5F785  74 72                           je 0x140b5f7f9
00B5F787  8D 0C 7F                        lea ecx, [rdi + rdi*2]
00B5F78A  C7 43 18 01 00 00 00            mov dword ptr [rbx + 0x18], 1
00B5F791  C1 E1 04                        shl ecx, 4
00B5F794  89 7B 1C                        mov dword ptr [rbx + 0x1c], edi
00B5F797  85 C9                           test ecx, ecx
00B5F799  74 09                           je 0x140b5f7a4
00B5F79B  E8 D4 51 9E FF                  call 0x140544974
00B5F7A0  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00B5F7A4  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00B5F7A8  48 85 C0                        test rax, rax
00B5F7AB  74 4C                           je 0x140b5f7f9
00B5F7AD  85 FF                           test edi, edi
00B5F7AF  74 21                           je 0x140b5f7d2
00B5F7B1  48 83 C0 10                     add rax, 0x10
00B5F7B5  8B D7                           mov edx, edi
00B5F7B7  49 8B CF                        mov rcx, r15
00B5F7BA  48 89 08                        mov qword ptr [rax], rcx
00B5F7BD  48 83 C1 04                     add rcx, 4
00B5F7C1  C7 40 0C 01 00 00 00            mov dword ptr [rax + 0xc], 1
00B5F7C8  48 8D 40 30                     lea rax, [rax + 0x30]
00B5F7CC  48 83 EA 01                     sub rdx, 1
00B5F7D0  75 E8                           jne 0x140b5f7ba
00B5F7D2  83 63 34 00                     and dword ptr [rbx + 0x34], 0
00B5F7D6  48 83 63 40 00                  and qword ptr [rbx + 0x40], 0
00B5F7DB  83 63 4C 00                     and dword ptr [rbx + 0x4c], 0
00B5F7DF  48 83 63 58 00                  and qword ptr [rbx + 0x58], 0
00B5F7E4  FF C5                           inc ebp
00B5F7E6  C7 43 30 64 00 00 00            mov dword ptr [rbx + 0x30], 0x64
00B5F7ED  C7 43 48 65 00 00 00            mov dword ptr [rbx + 0x48], 0x65
00B5F7F4  E9 EC FE FF FF                  jmp 0x140b5f6e5
00B5F7F9  40 B6 01                        mov sil, 1
00B5F7FC  48 83 25 CC 33 46 00 00         and qword ptr [rip + 0x4633cc], 0
00B5F804  48 8D 05 5D 65 4C FF            lea rax, [rip - 0xb39aa3]
00B5F80B  48 83 25 D5 05 43 00 00         and qword ptr [rip + 0x4305d5], 0
00B5F813  48 8D 1D 26 34 46 00            lea rbx, [rip + 0x463426]
00B5F81A  48 89 05 A7 33 46 00            mov qword ptr [rip + 0x4633a7], rax
00B5F821  48 8D 05 D8 05 43 00            lea rax, [rip + 0x4305d8]
00B5F828  48 89 05 D9 05 43 00            mov qword ptr [rip + 0x4305d9], rax
00B5F82F  48 89 05 CA 05 43 00            mov qword ptr [rip + 0x4305ca], rax
00B5F836  48 89 1D 0B 34 46 00            mov qword ptr [rip + 0x46340b], rbx
00B5F83D  48 89 1D FC 33 46 00            mov qword ptr [rip + 0x4633fc], rbx
00B5F844  40 84 F6                        test sil, sil
00B5F847  75 4F                           jne 0x140b5f898
00B5F849  33 C9                           xor ecx, ecx
00B5F84B  48 8D 14 89                     lea rdx, [rcx + rcx*4]
00B5F84F  48 C1 E2 06                     shl rdx, 6
00B5F853  48 8D 05 A6 07 4A FF            lea rax, [rip - 0xb5f85a]
00B5F85A  80 BC 02 AD 3C E0 00 00         cmp byte ptr [rdx + rax + 0xe03cad], 0
00B5F862  75 2D                           jne 0x140b5f891
00B5F864  48 8D 80 98 3C E0 00            lea rax, [rax + 0xe03c98]
00B5F86B  48 03 C2                        add rax, rdx
00B5F86E  48 8B 15 D3 33 46 00            mov rdx, qword ptr [rip + 0x4633d3]
00B5F875  48 39 1A                        cmp qword ptr [rdx], rbx
00B5F878  75 3D                           jne 0x140b5f8b7
00B5F87A  FF 05 A0 33 46 00               inc dword ptr [rip + 0x4633a0]
00B5F880  48 89 18                        mov qword ptr [rax], rbx
00B5F883  48 89 50 08                     mov qword ptr [rax + 8], rdx
00B5F887  48 89 02                        mov qword ptr [rdx], rax
00B5F88A  48 89 05 B7 33 46 00            mov qword ptr [rip + 0x4633b7], rax
00B5F891  FF C1                           inc ecx
00B5F893  83 F9 12                        cmp ecx, 0x12
00B5F896  72 B3                           jb 0x140b5f84b
00B5F898  44 8B 4C 24 20                  mov r9d, dword ptr [rsp + 0x20]
00B5F89D  48 8D 3D 5C 07 4A FF            lea rdi, [rip - 0xb5f8a4]
00B5F8A4  4A 8B BC EF 40 8C FC 00         mov rdi, qword ptr [rdi + r13*8 + 0xfc8c40]
00B5F8AC  48 8B 6F 58                     mov rbp, qword ptr [rdi + 0x58]
00B5F8B0  48 85 ED                        test rbp, rbp
00B5F8B3  75 09                           jne 0x140b5f8be
00B5F8B5  EB 0A                           jmp 0x140b5f8c1
00B5F8B7  B9 03 00 00 00                  mov ecx, 3
00B5F8BC  CD 29                           int 0x29
00B5F8BE  8B 6D 04                        mov ebp, dword ptr [rbp + 4]
00B5F8C1  48 8B 7F 58                     mov rdi, qword ptr [rdi + 0x58]
00B5F8C5  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
00B5F8C9  48 83 C7 18                     add rdi, 0x18
00B5F8CD  74 03                           je 0x140b5f8d2
00B5F8CF  8B 7F 04                        mov edi, dword ptr [rdi + 4]
00B5F8D2  8B 6C 24 30                     mov ebp, dword ptr [rsp + 0x30]
00B5F8D6  48 8D 1D E7 44 2A 00            lea rbx, [rip + 0x2a44e7]
00B5F8DD  33 F6                           xor esi, esi
00B5F8DF  4C 8D 3D CA 43 2A 00            lea r15, [rip + 0x2a43ca]
00B5F8E6  44 8D 76 20                     lea r14d, [rsi + 0x20]
00B5F8EA  80 7B 08 00                     cmp byte ptr [rbx + 8], 0
00B5F8EE  0F B6 03                        movzx eax, byte ptr [rbx]
00B5F8F1  74 06                           je 0x140b5f8f9
00B5F8F3  3B C7                           cmp eax, edi
00B5F8F5  73 35                           jae 0x140b5f92c
00B5F8F7  EB 20                           jmp 0x140b5f919
00B5F8F9  3C FF                           cmp al, 0xff
00B5F8FB  74 0A                           je 0x140b5f907
00B5F8FD  3B C5                           cmp eax, ebp
00B5F8FF  73 06                           jae 0x140b5f907
00B5F901  41 0F A3 C1                     bt r9d, eax
00B5F905  73 12                           jae 0x140b5f919
00B5F907  44 39 B3 CC FE FF FF            cmp dword ptr [rbx - 0x134], r14d
00B5F90E  75 1C                           jne 0x140b5f92c
00B5F910  80 3D 69 00 43 00 00            cmp byte ptr [rip + 0x430069], 0
00B5F917  74 13                           je 0x140b5f92c
00B5F919  48 8D 0C B6                     lea rcx, [rsi + rsi*4]
00B5F91D  41 8B D5                        mov edx, r13d
00B5F920  48 C1 E1 06                     shl rcx, 6
00B5F924  49 03 CF                        add rcx, r15
00B5F927  E8 C4 BD 6F FF                  call 0x14025b6f0
00B5F92C  44 8B 4C 24 20                  mov r9d, dword ptr [rsp + 0x20]
00B5F931  FF C6                           inc esi
00B5F933  48 81 C3 40 01 00 00            add rbx, 0x140
00B5F93A  83 FE 12                        cmp esi, 0x12
00B5F93D  72 AB                           jb 0x140b5f8ea
00B5F93F  8B 6C 24 28                     mov ebp, dword ptr [rsp + 0x28]
00B5F943  33 DB                           xor ebx, ebx
00B5F945  85 ED                           test ebp, ebp
00B5F947  74 19                           je 0x140b5f962
00B5F949  33 C0                           xor eax, eax
00B5F94B  8D 8B 86 01 00 00               lea ecx, [rbx + 0x186]
00B5F951  33 D2                           xor edx, edx
00B5F953  0F 30                           wrmsr
00B5F955  8B CB                           mov ecx, ebx
00B5F957  E8 80 D5 9F FF                  call 0x14055cedc
00B5F95C  FF C3                           inc ebx
00B5F95E  3B DD                           cmp ebx, ebp
00B5F960  72 E7                           jb 0x140b5f949
00B5F962  85 FF                           test edi, edi
00B5F964  74 4C                           je 0x140b5f9b2
00B5F966  33 C0                           xor eax, eax
00B5F968  B9 8D 03 00 00                  mov ecx, 0x38d
00B5F96D  33 D2                           xor edx, edx
00B5F96F  0F 30                           wrmsr
00B5F971  44 8D 51 02                     lea r10d, [rcx + 2]
00B5F975  41 8B CA                        mov ecx, r10d
00B5F978  0F 32                           rdmsr
00B5F97A  48 C1 E2 20                     shl rdx, 0x20
00B5F97E  48 0B C2                        or rax, rdx
00B5F981  48 8B D8                        mov rbx, rax
00B5F984  45 33 C9                        xor r9d, r9d
00B5F987  BA 01 00 00 00                  mov edx, 1
00B5F98C  4C 0F B3 F3                     btr rbx, r14
00B5F990  41 8B C9                        mov ecx, r9d
00B5F993  E8 44 D5 9F FF                  call 0x14055cedc
00B5F998  41 FF C1                        inc r9d
00B5F99B  49 FF C6                        inc r14
00B5F99E  44 3B CF                        cmp r9d, edi
00B5F9A1  72 E4                           jb 0x140b5f987
00B5F9A3  48 8B D3                        mov rdx, rbx
00B5F9A6  48 8B C3                        mov rax, rbx
00B5F9A9  48 C1 EA 20                     shr rdx, 0x20
00B5F9AD  41 8B CA                        mov ecx, r10d
00B5F9B0  0F 30                           wrmsr
00B5F9B2  45 85 ED                        test r13d, r13d
00B5F9B5  75 48                           jne 0x140b5f9ff
00B5F9B7  E8 74 F8 FF FF                  call 0x140b5f230
00B5F9BC  8B CF                           mov ecx, edi
00B5F9BE  41 8D 55 01                     lea edx, [r13 + 1]
00B5F9C2  48 D3 E2                        shl rdx, cl
00B5F9C5  41 8D 45 01                     lea eax, [r13 + 1]
00B5F9C9  48 FF CA                        dec rdx
00B5F9CC  8B CD                           mov ecx, ebp
00B5F9CE  48 D3 E0                        shl rax, cl
00B5F9D1  48 FF C8                        dec rax
00B5F9D4  48 C1 E2 20                     shl rdx, 0x20
00B5F9D8  48 0B D0                        or rdx, rax
00B5F9DB  44 38 2D 16 04 43 00            cmp byte ptr [rip + 0x430416], r13b
00B5F9E2  48 89 15 3F 04 43 00            mov qword ptr [rip + 0x43043f], rdx
00B5F9E9  74 14                           je 0x140b5f9ff
00B5F9EB  48 B8 00 00 00 00 00 00 00 40   movabs rax, 0x4000000000000000
00B5F9F5  48 0B D0                        or rdx, rax
00B5F9F8  48 89 15 29 04 43 00            mov qword ptr [rip + 0x430429], rdx
00B5F9FF  83 3D DA 03 43 00 02            cmp dword ptr [rip + 0x4303da], 2
00B5FA06  72 15                           jb 0x140b5fa1d
00B5FA08  48 8B 15 19 04 43 00            mov rdx, qword ptr [rip + 0x430419]
00B5FA0F  B9 90 03 00 00                  mov ecx, 0x390
00B5FA14  48 8B C2                        mov rax, rdx
00B5FA17  48 C1 EA 20                     shr rdx, 0x20
00B5FA1B  0F 30                           wrmsr
00B5FA1D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B5FA22  48 33 CC                        xor rcx, rsp
00B5FA25  E8 16 CC B4 FF                  call 0x1406ac640
00B5FA2A  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00B5FA2F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00B5FA33  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00B5FA37  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B5FA3B  49 8B E3                        mov rsp, r11
00B5FA3E  41 5F                           pop r15
00B5FA40  41 5E                           pop r14
00B5FA42  41 5D                           pop r13
00B5FA44  41 5C                           pop r12
00B5FA46  5F                              pop rdi
00B5FA47  C3                              ret
00B5FA48  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonInitializeProfilingOriginal(int a1, int a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 2797805)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r15 = 0;
    a1 = 0;
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_rsi = 0;
    v_stack_m58 = (unsigned int)(v_rbx);
    result = (unsigned int)((v_r15 + 10) >> (24));
    v_stack_m48 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) != 0) goto loc_00B5F89D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15 + 10))))) >> (8));
    v_rdi = 0;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + 10))) >> (16));
    *(unsigned int *)(v_rip + 4392792) = (unsigned int)((unsigned __int8)(a3));
    *(unsigned __int8 *)(v_rip + 4392761) = 0;
    *(unsigned int *)(v_rip + 4392731) = (unsigned int)((unsigned __int8)((unsigned int)((unsigned int)(v_r15 + 10))));
    result = (unsigned __int8)(a3);
    if (((unsigned int)((unsigned __int8)((unsigned int)((unsigned int)(v_r15 + 10))))) >= 2) {
        v_rdi = a2;
        v_rdi = (unsigned int)((v_rdi) & (15));
        a2 = (unsigned int)((a2) >> (5));
        result = (unsigned __int8)(a2);
        *(unsigned int *)(v_rip + 4392761) = (unsigned int)(result);
    }
    result = HalpQueryMaximumRegisteredProcessorCount((unsigned __int8)((unsigned int)((unsigned int)(v_r15 + 10))), a2, a3, (unsigned int)((unsigned int)(v_rbx)));
    v_rbp = 0;
loc_00B5F6E5:
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00B5F7FC;
    v_rbx = (v_rbp * 2) + (0);
    v_rbx = (v_rbx) << (5);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_stack_m50 + 88));
    result = v_stack_m50;
    if ((unsigned int)((unsigned __int8)(result) * 4) != 0) {
        result = HalpMmAllocateMemory((unsigned __int8)(result) * 4, a2, a3, (unsigned int)((unsigned int)(v_rbx)));
        v_r15 = result;
    }
    if (v_r15 == 0) goto loc_00B5F7F9;
    a1 = (unsigned int)(((unsigned __int8)(result) + (unsigned __int8)(result) * 2) << (4));
    *(unsigned int *)(v_rbx + 4) = (unsigned int)((unsigned __int8)(result));
    if (a1 != 0) {
        result = HalpMmAllocateMemory(a1, a2, a3, (unsigned int)((unsigned int)(v_rbx)));
        *(unsigned __int64 *)(v_rbx + 16) = result;
    }
    if (*(unsigned __int64 *)(v_rbx + 16) == 0) goto loc_00B5F7F9;
    if ((unsigned int)((unsigned __int8)(result)) == 0) goto loc_00B5F76F;
    result = (*(unsigned __int64 *)(v_rbx + 16)) + (16);
loc_00B5F75A:
    *(unsigned __int64 *)(result) = v_r15;
    a1 = (v_r15) + (4);
    a2 = ((unsigned __int8)(result)) - (1);
    if (condition_is_not_equal) goto loc_00B5F75A;
loc_00B5F76F:
    if ((unsigned int)(v_rdi * 4) == 0) goto loc_00B5F787;
    result = HalpMmAllocateMemory(v_rdi * 4, a2, a3, (unsigned int)((unsigned int)(v_rbx)));
    if (result == 0) goto loc_00B5F7F9;
loc_00B5F787:
    *(unsigned int *)(v_rbx + 24) = 1;
    a1 = (unsigned int)((v_rdi + v_rdi * 2) << (4));
    *(unsigned int *)(v_rbx + 28) = (unsigned int)(v_rdi);
    if (a1 != 0) {
        result = HalpMmAllocateMemory(a1, a2, a3, (unsigned int)((unsigned int)(v_rbx)));
        *(unsigned __int64 *)(v_rbx + 40) = result;
    }
    if (*(unsigned __int64 *)(v_rbx + 40) == 0) goto loc_00B5F7F9;
    if ((unsigned int)(v_rdi) == 0) goto loc_00B5F7D2;
    result = (*(unsigned __int64 *)(v_rbx + 40)) + (16);
loc_00B5F7BA:
    *(unsigned __int64 *)(result) = result;
    a1 = (result) + (4);
    *(unsigned int *)(result + 12) = 1;
    a2 = ((unsigned int)((unsigned int)(v_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00B5F7BA;
loc_00B5F7D2:
    v_rbp = (unsigned int)((v_rbp) + 1);
    *(unsigned int *)(v_rbx + 48) = 100;
    *(unsigned int *)(v_rbx + 72) = 101;
    goto loc_00B5F6E5;
loc_00B5F7F9:
loc_00B5F7FC:
    *(unsigned __int64 *)(v_rip + 4600743) = v_rip - 11770531;
    *(unsigned __int64 *)(v_rip + 4392409) = v_rip + 4392408;
    *(unsigned __int64 *)(v_rip + 4392394) = v_rip + 4392408;
    *(unsigned __int64 *)(v_rip + 4600843) = v_rip + 4600870;
    *(unsigned __int64 *)(v_rip + 4600828) = v_rip + 4600870;
    if (1 != 0) goto loc_00B5F898;
    a1 = 0;
loc_00B5F84B:
    a2 = (a1 + a1 * 4) << (6);
    if ((*(unsigned __int8 *)(a2 + v_rip - 11925594 * 1 + 14695597)) != 0) goto loc_00B5F891;
    result = (v_rip - 11925594 + 14695576) + (a2);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4600787))) != (v_rip + 4600870)) goto loc_00B5F8B7;
    *(unsigned __int64 *)(result) = v_rip + 4600870;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 4600787);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4600787)) = result;
    *(unsigned __int64 *)(v_rip + 4600759) = result;
loc_00B5F891:
    a1 = (unsigned int)((a1) + 1);
    if (a1 < 18) goto loc_00B5F84B;
loc_00B5F898:
loc_00B5F89D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11925668 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) != 0) goto loc_00B5F8BE;
    goto loc_00B5F8C1;
loc_00B5F8B7:
loc_00B5F8BE:
loc_00B5F8C1:
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11925668 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 4)));
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11925668 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)) + (24);
    if (!(condition_is_equal)) {
        v_rdi = *(unsigned int *)(v_rdi + 4);
    }
    v_rsi = 0;
loc_00B5F8EA:
    if ((*(unsigned __int8 *)(v_rip + 2770151 + 8)) == 0) goto loc_00B5F8F9;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 2770151))) >= ((unsigned int)(v_rdi))) goto loc_00B5F92C;
    goto loc_00B5F919;
loc_00B5F8F9:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 2770151))) == 255) goto loc_00B5F907;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 2770151))) >= ((unsigned int)((unsigned int)(v_stack_m48)))) goto loc_00B5F907;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 2770151))) >= ((unsigned int)((unsigned int)(v_stack_m48)))) goto loc_00B5F919;
loc_00B5F907:
    if ((*(unsigned int *)(v_rip + 2770151 - 308)) != ((unsigned int)(v_rsi + 32))) goto loc_00B5F92C;
    result = *(unsigned __int8 *)(v_rip + 2770151);
    if ((*(unsigned __int8 *)(v_rip + 4391017)) != 0) {
        a1 = v_rsi + v_rsi * 4;
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
        a1 = (a1) << (6);
        a1 = (a1) + (v_rip + 2769866);
        result = KeAddProcessorAffinityEx(a1, a2, a3, (unsigned int)(v_stack_m58));
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_rbx = (v_rip + 2770151) + (320);
    if (((unsigned int)(v_rsi)) < 18) goto loc_00B5F8EA;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00B5F962;
loc_00B5F949:
    result = 0;
    a2 = 0;
    result = EmonFreeCounterOriginal(0, a2, a3, (unsigned int)(v_stack_m58));
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(v_stack_m50)))) goto loc_00B5F949;
loc_00B5F962:
    if ((unsigned int)(v_rdi) == 0) goto loc_00B5F9B2;
    result = 0;
    a2 = 0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a4 = 0;
loc_00B5F987:
    result = EmonFreeCounterOriginal(0, 1, a3, a4);
    a4 = (unsigned int)((a4) + 1);
    v_r14 = (v_rsi + 32) + 1;
    if (((unsigned int)(a4)) < ((unsigned int)(v_rdi))) goto loc_00B5F987;
    a2 = (result) >> (32);
loc_00B5F9B2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) != 0) goto loc_00B5F9FF;
    result = EmonInitializePebs((unsigned int)((unsigned int)(909 + 2)), a2, a3, a4);
    a2 = ((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) + 1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (a2) - 1;
    result = ((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) + 1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))));
    result = (result) - 1;
    a2 = (a2) << (32);
    a2 = (a2) | (result);
    *(unsigned __int64 *)(v_rip + 4391999) = a2;
    if ((*(unsigned __int8 *)(v_rip + 4391958)) != ((unsigned __int8)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) {
        a2 = (a2) | (result);
        *(unsigned __int64 *)(v_rip + 4391977) = a2;
    }
    if ((*(unsigned int *)(v_rip + 4391898)) >= 2) {
        a2 = *(unsigned __int64 *)(v_rip + 4391961);
        a1 = 912;
        result = a2;
        a2 = (a2) >> (32);
    }
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EmonInitializeProfilingOriginal(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x2AB0ED)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r15 = 0;
    Arg1 = 0;
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x20));
    local_rsi = 0;
    v_stack_m58 = (uint32_t)(local_rbx);
    result = (uint32_t)((local_r15 + 10) >> (24));
    v_stack_m48 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) != 0) goto loc_00B5F89D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15 + 10))))) >> (8));
    local_rdi = 0;
    a3 = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + 10))) >> (16));
    *(uint32_t *)(v_rip + 0x430758) = (uint32_t)((uint8_t)(a3));
    *(uint8_t *)(v_rip + 0x430739) = 0;
    *(uint32_t *)(v_rip + 0x43071B) = (uint32_t)((uint8_t)((uint32_t)((uint32_t)(local_r15 + 10))));
    result = (uint8_t)(a3);
    if (((uint32_t)((uint8_t)((uint32_t)((uint32_t)(local_r15 + 10))))) >= 2) {
        local_rdi = Arg2;
        local_rdi = (uint32_t)((local_rdi) & (15));
        Arg2 = (uint32_t)((Arg2) >> (5));
        result = (uint8_t)(Arg2);
        *(uint32_t *)(v_rip + 0x430739) = (uint32_t)(result);
    }
    result = HalpQueryMaximumRegisteredProcessorCount((uint8_t)((uint32_t)((uint32_t)(local_r15 + 10))), Arg2, a3, (uint32_t)((uint32_t)(local_rbx)));
    local_rbp = 0;
loc_00B5F6E5:
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00B5F7FC;
    local_rbx = (local_rbp * 2) + (0);
    local_rbx = (local_rbx) << (5);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_stack_m50 + 0x58));
    result = v_stack_m50;
    if ((uint32_t)((uint8_t)(result) * 4) != 0) {
        result = HalpMmAllocateMemory((uint8_t)(result) * 4, Arg2, a3, (uint32_t)((uint32_t)(local_rbx)));
        local_r15 = result;
    }
    if (local_r15 == 0) goto loc_00B5F7F9;
    Arg1 = (uint32_t)(((uint8_t)(result) + (uint8_t)(result) * 2) << (4));
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)((uint8_t)(result));
    if (Arg1 != 0) {
        result = HalpMmAllocateMemory(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rbx)));
        *(uint64_t *)(local_rbx + 0x10) = result;
    }
    if (*(uint64_t *)(local_rbx + 0x10) == 0) goto loc_00B5F7F9;
    if ((uint32_t)((uint8_t)(result)) == 0) goto loc_00B5F76F;
    result = (*(uint64_t *)(local_rbx + 0x10)) + (16);
loc_00B5F75A:
    *(uint64_t *)(result) = local_r15;
    Arg1 = (local_r15) + (4);
    Arg2 = ((uint8_t)(result)) - (1);
    if (condition_is_not_equal) goto loc_00B5F75A;
loc_00B5F76F:
    if ((uint32_t)(local_rdi * 4) == 0) goto loc_00B5F787;
    result = HalpMmAllocateMemory(local_rdi * 4, Arg2, a3, (uint32_t)((uint32_t)(local_rbx)));
    if (result == 0) goto loc_00B5F7F9;
loc_00B5F787:
    *(uint32_t *)(local_rbx + 0x18) = 1;
    Arg1 = (uint32_t)((local_rdi + local_rdi * 2) << (4));
    *(uint32_t *)(local_rbx + 0x1C) = (uint32_t)(local_rdi);
    if (Arg1 != 0) {
        result = HalpMmAllocateMemory(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rbx)));
        *(uint64_t *)(local_rbx + 0x28) = result;
    }
    if (*(uint64_t *)(local_rbx + 0x28) == 0) goto loc_00B5F7F9;
    if ((uint32_t)(local_rdi) == 0) goto loc_00B5F7D2;
    result = (*(uint64_t *)(local_rbx + 0x28)) + (16);
loc_00B5F7BA:
    *(uint64_t *)(result) = result;
    Arg1 = (result) + (4);
    *(uint32_t *)(result + 0xC) = 1;
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) - (1);
    if (condition_is_not_equal) goto loc_00B5F7BA;
loc_00B5F7D2:
    local_rbp = (uint32_t)((local_rbp) + 1);
    *(uint32_t *)(local_rbx + 0x30) = 100;
    *(uint32_t *)(local_rbx + 0x48) = 101;
    goto loc_00B5F6E5;
loc_00B5F7F9:
loc_00B5F7FC:
    *(uint64_t *)(v_rip + 0x4633A7) = v_rip - 11770531;
    *(uint64_t *)(v_rip + 0x4305D9) = v_rip + 4392408;
    *(uint64_t *)(v_rip + 0x4305CA) = v_rip + 4392408;
    *(uint64_t *)(v_rip + 0x46340B) = v_rip + 4600870;
    *(uint64_t *)(v_rip + 0x4633FC) = v_rip + 4600870;
    if (1 != 0) goto loc_00B5F898;
    Arg1 = 0;
loc_00B5F84B:
    Arg2 = (Arg1 + Arg1 * 4) << (6);
    if ((*(uint8_t *)(Arg2 + v_rip - 0xB5F85A * 1 + 0xE03CAD)) != 0) goto loc_00B5F891;
    result = (v_rip - 11925594 + 14695576) + (Arg2);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x4633D3))) != (v_rip + 4600870)) goto loc_00B5F8B7;
    *(uint64_t *)(result) = v_rip + 4600870;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0x4633D3);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x4633D3)) = result;
    *(uint64_t *)(v_rip + 0x4633B7) = result;
loc_00B5F891:
    Arg1 = (uint32_t)((Arg1) + 1);
    if (Arg1 < 18) goto loc_00B5F84B;
loc_00B5F898:
loc_00B5F89D:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0xB5F8A4 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) != 0) goto loc_00B5F8BE;
    goto loc_00B5F8C1;
loc_00B5F8B7:
loc_00B5F8BE:
loc_00B5F8C1:
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0xB5F8A4 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 0x4)));
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_rip - 0xB5F8A4 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (!(condition_is_equal)) {
        local_rdi = *(uint32_t *)(local_rdi + 0x4);
    }
    local_rsi = 0;
loc_00B5F8EA:
    if ((*(uint8_t *)(v_rip + 0x2A44E7 + 0x8)) == 0) goto loc_00B5F8F9;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x2A44E7))) >= ((uint32_t)(local_rdi))) goto loc_00B5F92C;
    goto loc_00B5F919;
loc_00B5F8F9:
    if (((uint8_t)(*(uint8_t *)(v_rip + 0x2A44E7))) == 255) goto loc_00B5F907;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x2A44E7))) >= ((uint32_t)((uint32_t)(v_stack_m48)))) goto loc_00B5F907;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x2A44E7))) >= ((uint32_t)((uint32_t)(v_stack_m48)))) goto loc_00B5F919;
loc_00B5F907:
    if ((*(uint32_t *)(v_rip + 0x2A44E7 - 0x134)) != ((uint32_t)(local_rsi + 32))) goto loc_00B5F92C;
    result = *(uint8_t *)(v_rip + 0x2A44E7);
    if ((*(uint8_t *)(v_rip + 0x430069)) != 0) {
        Arg1 = local_rsi + local_rsi * 4;
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
        Arg1 = (Arg1) << (6);
        Arg1 = (Arg1) + (v_rip + 2769866);
        result = KeAddProcessorAffinityEx(Arg1, Arg2, a3, (uint32_t)(v_stack_m58));
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    local_rbx = (v_rip + 2770151) + (320);
    if (((uint32_t)(local_rsi)) < 18) goto loc_00B5F8EA;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00B5F962;
loc_00B5F949:
    result = 0;
    Arg2 = 0;
    result = EmonFreeCounterOriginal(0, Arg2, a3, (uint32_t)(v_stack_m58));
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(v_stack_m50)))) goto loc_00B5F949;
loc_00B5F962:
    if ((uint32_t)(local_rdi) == 0) goto loc_00B5F9B2;
    result = 0;
    Arg2 = 0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    a4 = 0;
loc_00B5F987:
    result = EmonFreeCounterOriginal(0, 1, a3, a4);
    a4 = (uint32_t)((a4) + 1);
    local_r14 = (local_rsi + 32) + 1;
    if (((uint32_t)(a4)) < ((uint32_t)(local_rdi))) goto loc_00B5F987;
    Arg2 = (result) >> (32);
loc_00B5F9B2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) != 0) goto loc_00B5F9FF;
    result = EmonInitializePebs((uint32_t)((uint32_t)(909 + 2)), Arg2, a3, a4);
    Arg2 = ((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) + 1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (Arg2) - 1;
    result = ((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) + 1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))));
    result = (result) - 1;
    Arg2 = (Arg2) << (32);
    Arg2 = (Arg2) | (result);
    *(uint64_t *)(v_rip + 0x43043F) = Arg2;
    if ((*(uint8_t *)(v_rip + 0x430416)) != ((uint8_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) {
        Arg2 = (Arg2) | (result);
        *(uint64_t *)(v_rip + 0x430429) = Arg2;
    }
    if ((*(uint32_t *)(v_rip + 0x4303DA)) >= 2) {
        Arg2 = *(uint64_t *)(v_rip + 0x430419);
        Arg1 = 912;
        result = Arg2;
        Arg2 = (Arg2) >> (32);
    }
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5F630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
