# Amd64OverflowHandlerInternal

- RVA: `0x0056D330`–`0x0056D7B9` (길이 `1,161` bytes)
- VA: `0x000000014056D330`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE498`
- 디코드: `292`개 명령, `1,161/1,161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0056D4F6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056D4FF` → [KeProfileInterruptWithSource](../4A/KeProfileInterruptWithSource_function_004A34D0.md) (function, `0x004A34D0`)
- `0x0056D569` → [PoGetProcessorIdleAccounting](../4F/PoGetProcessorIdleAccounting_function_004FBEA0.md) (function, `0x004FBEA0`)
- `0x0056D57A` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0056D62B` → [PoGetProcessorIdleAccounting](../4F/PoGetProcessorIdleAccounting_function_004FBEA0.md) (function, `0x004FBEA0`)
- `0x0056D643` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0056D674` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0056D6E5` → [KeProfileInterruptWithSource](../4A/KeProfileInterruptWithSource_function_004A34D0.md) (function, `0x004A34D0`)
- `0x0056D776` → [Amd64IsModifiedByBadActorInternal](../49/Amd64IsModifiedByBadActorInternal_function_0049EB64.md) (function, `0x0049EB64`)

### Direct callers
- [Amd64OverflowHandler](Amd64OverflowHandler_function_0056D310.md) at `0x0056D31F`

### Static image references
- `0x0056D34D` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0056D4EA` → RVA `0x00E10360` (`.data`; read)
- `0x0056D50C` → RVA `0x00FC21E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056D330  48 8B C4                        mov rax, rsp
0056D333  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0056D337  89 48 08                        mov dword ptr [rax + 8], ecx
0056D33A  53                              push rbx
0056D33B  55                              push rbp
0056D33C  56                              push rsi
0056D33D  57                              push rdi
0056D33E  41 54                           push r12
0056D340  41 55                           push r13
0056D342  41 56                           push r14
0056D344  41 57                           push r15
0056D346  48 83 EC 58                     sub rsp, 0x58
0056D34A  44 8B F2                        mov r14d, edx
0056D34D  48 8D 3D AC 2C A9 FF            lea rdi, [rip - 0x56d354]
0056D354  C6 40 08 00                     mov byte ptr [rax + 8], 0
0056D358  45 33 ED                        xor r13d, r13d
0056D35B  4D 8B D8                        mov r11, r8
0056D35E  41 BF FF FF FF 7F               mov r15d, 0x7fffffff
0056D364  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D36C  48 8B 68 58                     mov rbp, qword ptr [rax + 0x58]
0056D370  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
0056D375  48 8B 5D 10                     mov rbx, qword ptr [rbp + 0x10]
0056D379  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0056D37E  44 39 6D 04                     cmp dword ptr [rbp + 4], r13d
0056D382  0F 86 1F 04 00 00               jbe 0x14056d7a7
0056D388  4E 8D 24 6D 00 00 00 00         lea r12, [r13*2]
0056D390  4D 03 E5                        add r12, r13
0056D393  4D 03 E4                        add r12, r12
0056D396  42 83 7C E3 18 00               cmp dword ptr [rbx + r12*8 + 0x18], 0
0056D39C  0F 85 F8 03 00 00               jne 0x14056d79a
0056D3A2  8B 55 00                        mov edx, dword ptr [rbp]
0056D3A5  45 33 C0                        xor r8d, r8d
0056D3A8  46 8B 4C E3 24                  mov r9d, dword ptr [rbx + r12*8 + 0x24]
0056D3AD  8B CA                           mov ecx, edx
0056D3AF  83 E9 01                        sub ecx, 1
0056D3B2  74 38                           je 0x14056d3ec
0056D3B4  83 E9 63                        sub ecx, 0x63
0056D3B7  74 1B                           je 0x14056d3d4
0056D3B9  83 F9 01                        cmp ecx, 1
0056D3BC  75 45                           jne 0x14056d403
0056D3BE  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D3C6  4C 8B 40 58                     mov r8, qword ptr [rax + 0x58]
0056D3CA  49 83 C0 30                     add r8, 0x30
0056D3CE  74 04                           je 0x14056d3d4
0056D3D0  45 8B 40 04                     mov r8d, dword ptr [r8 + 4]
0056D3D4  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D3DC  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056D3E0  48 83 C0 18                     add rax, 0x18
0056D3E4  74 03                           je 0x14056d3e9
0056D3E6  8B 40 04                        mov eax, dword ptr [rax + 4]
0056D3E9  44 03 C0                        add r8d, eax
0056D3EC  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D3F4  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056D3F8  48 85 C0                        test rax, rax
0056D3FB  74 03                           je 0x14056d400
0056D3FD  8B 40 04                        mov eax, dword ptr [rax + 4]
0056D400  44 03 C0                        add r8d, eax
0056D403  43 8D 04 28                     lea eax, [r8 + r13]
0056D407  45 33 C0                        xor r8d, r8d
0056D40A  44 8B 94 87 40 F9 F8 00         mov r10d, dword ptr [rdi + rax*4 + 0xf8f940]
0056D412  44 89 94 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r10d
0056D41A  83 EA 01                        sub edx, 1
0056D41D  74 38                           je 0x14056d457
0056D41F  83 EA 63                        sub edx, 0x63
0056D422  74 1B                           je 0x14056d43f
0056D424  83 FA 01                        cmp edx, 1
0056D427  75 45                           jne 0x14056d46e
0056D429  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D431  4C 8B 40 58                     mov r8, qword ptr [rax + 0x58]
0056D435  49 83 C0 30                     add r8, 0x30
0056D439  74 04                           je 0x14056d43f
0056D43B  45 8B 40 04                     mov r8d, dword ptr [r8 + 4]
0056D43F  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D447  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056D44B  48 83 C0 18                     add rax, 0x18
0056D44F  74 03                           je 0x14056d454
0056D451  8B 40 04                        mov eax, dword ptr [rax + 4]
0056D454  44 03 C0                        add r8d, eax
0056D457  4A 8B 84 F7 40 8C FC 00         mov rax, qword ptr [rdi + r14*8 + 0xfc8c40]
0056D45F  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056D463  48 85 C0                        test rax, rax
0056D466  74 03                           je 0x14056d46b
0056D468  8B 40 04                        mov eax, dword ptr [rax + 4]
0056D46B  44 03 C0                        add r8d, eax
0056D46E  43 8D 04 28                     lea eax, [r8 + r13]
0056D472  8B B4 87 C0 F8 F8 00            mov esi, dword ptr [rdi + rax*4 + 0xf8f8c0]
0056D479  8B CE                           mov ecx, esi
0056D47B  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
0056D482  0F 32                           rdmsr
0056D484  48 C1 E2 20                     shl rdx, 0x20
0056D488  48 B9 FF FF FF FF FF FF 00 00   movabs rcx, 0xffffffffffff
0056D492  48 0B C2                        or rax, rdx
0056D495  48 23 C1                        and rax, rcx
0056D498  48 B9 01 00 00 80 FF FF 00 00   movabs rcx, 0xffff80000001
0056D4A2  48 3B C1                        cmp rax, rcx
0056D4A5  0F 83 EF 02 00 00               jae 0x14056d79a
0056D4AB  41 8B CA                        mov ecx, r10d
0056D4AE  0F 32                           rdmsr
0056D4B0  48 C1 E2 20                     shl rdx, 0x20
0056D4B4  48 0B C2                        or rax, rdx
0056D4B7  48 8B D0                        mov rdx, rax
0056D4BA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0056D4BF  48 81 E2 FF FF AF FF            and rdx, 0xffffffffffafffff
0056D4C6  48 8B F8                        mov rdi, rax
0056D4C9  48 8B C2                        mov rax, rdx
0056D4CC  48 C1 EA 20                     shr rdx, 0x20
0056D4D0  0F 30                           wrmsr
0056D4D2  49 8B CB                        mov rcx, r11
0056D4D5  45 85 C9                        test r9d, r9d
0056D4D8  0F 85 04 02 00 00               jne 0x14056d6e2
0056D4DE  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0056D4E4  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
0056D4EA  48 8B 05 6F 2E 8A 00            mov rax, qword ptr [rip + 0x8a2e6f]
0056D4F1  48 85 C0                        test rax, rax
0056D4F4  74 07                           je 0x14056d4fd
0056D4F6  E8 D5 D5 14 00                  call 0x1406baad0
0056D4FB  EB 07                           jmp 0x14056d504
0056D4FD  33 D2                           xor edx, edx
0056D4FF  E8 CC 5F F3 FF                  call 0x1404a34d0
0056D504  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0056D50C  48 8B 3D D5 4C A5 00            mov rdi, qword ptr [rip + 0xa54cd5]
0056D513  8B C8                           mov ecx, eax
0056D515  48 69 D9 28 01 00 00            imul rbx, rcx, 0x128
0056D51C  8B 4C 3B 18                     mov ecx, dword ptr [rbx + rdi + 0x18]
0056D520  85 C9                           test ecx, ecx
0056D522  74 7B                           je 0x14056d59f
0056D524  8B 44 3B 20                     mov eax, dword ptr [rbx + rdi + 0x20]
0056D528  44 8B 7C 3B 10                  mov r15d, dword ptr [rbx + rdi + 0x10]
0056D52D  8B F0                           mov esi, eax
0056D52F  48 C1 E6 04                     shl rsi, 4
0056D533  48 03 F3                        add rsi, rbx
0056D536  FF C0                           inc eax
0056D538  83 E0 0F                        and eax, 0xf
0056D53B  89 44 3B 20                     mov dword ptr [rbx + rdi + 0x20], eax
0056D53F  8B 44 3B 14                     mov eax, dword ptr [rbx + rdi + 0x14]
0056D543  85 C0                           test eax, eax
0056D545  0F 85 B6 00 00 00               jne 0x14056d601
0056D54B  33 D2                           xor edx, edx
0056D54D  B8 10 27 00 00                  mov eax, 0x2710
0056D552  F7 F1                           div ecx
0056D554  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0056D558  85 C0                           test eax, eax
0056D55A  75 08                           jne 0x14056d564
0056D55C  C7 44 3B 14 01 00 00 00         mov dword ptr [rbx + rdi + 0x14], 1
0056D564  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0056D569  E8 32 E9 F8 FF                  call 0x1404fbea0
0056D56E  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0056D573  33 C9                           xor ecx, ecx
0056D575  48 89 44 3B 08                  mov qword ptr [rbx + rdi + 8], rax
0056D57A  E8 61 12 E1 FF                  call 0x14037e7e0
0056D57F  48 8B 0D 62 4C A5 00            mov rcx, qword ptr [rip + 0xa54c62]
0056D586  48 89 04 0B                     mov qword ptr [rbx + rcx], rax
0056D58A  44 89 7C 3E 28                  mov dword ptr [rsi + rdi + 0x28], r15d
0056D58F  48 8B 04 0B                     mov rax, qword ptr [rbx + rcx]
0056D593  48 89 44 3E 30                  mov qword ptr [rsi + rdi + 0x30], rax
0056D598  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
0056D59F  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
0056D5A4  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
0056D5A9  8B 4D 00                        mov ecx, dword ptr [rbp]
0056D5AC  85 C9                           test ecx, ecx
0056D5AE  0F 85 86 01 00 00               jne 0x14056d73a
0056D5B4  4A 8B 44 E3 10                  mov rax, qword ptr [rbx + r12*8 + 0x10]
0056D5B9  38 48 08                        cmp byte ptr [rax + 8], cl
0056D5BC  0F 84 78 01 00 00               je 0x14056d73a
0056D5C2  33 D2                           xor edx, edx
0056D5C4  4C 8D 05 35 2A A9 FF            lea r8, [rip - 0x56d5cb]
0056D5CB  83 E9 01                        sub ecx, 1
0056D5CE  0F 84 39 01 00 00               je 0x14056d70d
0056D5D4  83 E9 63                        sub ecx, 0x63
0056D5D7  0F 84 19 01 00 00               je 0x14056d6f6
0056D5DD  83 F9 01                        cmp ecx, 1
0056D5E0  0F 85 3D 01 00 00               jne 0x14056d723
0056D5E6  4B 8B 84 F0 40 8C FC 00         mov rax, qword ptr [r8 + r14*8 + 0xfc8c40]
0056D5EE  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
0056D5F2  48 83 C2 30                     add rdx, 0x30
0056D5F6  0F 85 F7 00 00 00               jne 0x14056d6f3
0056D5FC  E9 F5 00 00 00                  jmp 0x14056d6f6
0056D601  83 E8 01                        sub eax, 1
0056D604  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0056D608  75 8E                           jne 0x14056d598
0056D60A  33 D2                           xor edx, edx
0056D60C  B8 10 27 00 00                  mov eax, 0x2710
0056D611  F7 F1                           div ecx
0056D613  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0056D617  8B E8                           mov ebp, eax
0056D619  85 C0                           test eax, eax
0056D61B  75 09                           jne 0x14056d626
0056D61D  8D 45 01                        lea eax, [rbp + 1]
0056D620  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0056D624  8B E8                           mov ebp, eax
0056D626  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0056D62B  E8 70 E8 F8 FF                  call 0x1404fbea0
0056D630  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0056D635  48 3B 44 3B 08                  cmp rax, qword ptr [rbx + rdi + 8]
0056D63A  74 2F                           je 0x14056d66b
0056D63C  33 C9                           xor ecx, ecx
0056D63E  48 89 44 3B 08                  mov qword ptr [rbx + rdi + 8], rax
0056D643  E8 98 11 E1 FF                  call 0x14037e7e0
0056D648  48 8B 0D 99 4B A5 00            mov rcx, qword ptr [rip + 0xa54b99]
0056D64F  48 89 04 0B                     mov qword ptr [rbx + rcx], rax
0056D653  44 89 7C 3E 28                  mov dword ptr [rsi + rdi + 0x28], r15d
0056D658  48 8B 04 0B                     mov rax, qword ptr [rbx + rcx]
0056D65C  48 89 44 3E 30                  mov qword ptr [rsi + rdi + 0x30], rax
0056D661  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0056D666  E9 2D FF FF FF                  jmp 0x14056d598
0056D66B  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0056D670  41 0F AF EF                     imul ebp, r15d
0056D674  E8 67 11 E1 FF                  call 0x14037e7e0
0056D679  4C 8B 05 68 4B A5 00            mov r8, qword ptr [rip + 0xa54b68]
0056D680  48 8B C8                        mov rcx, rax
0056D683  4C 8B C8                        mov r9, rax
0056D686  4A 2B 0C 03                     sub rcx, qword ptr [rbx + r8]
0056D68A  75 0C                           jne 0x14056d698
0056D68C  44 89 7C 3E 28                  mov dword ptr [rsi + rdi + 0x28], r15d
0056D691  4C 89 4C 3E 30                  mov qword ptr [rsi + rdi + 0x30], r9
0056D696  EB C9                           jmp 0x14056d661
0056D698  42 8B 44 03 18                  mov eax, dword ptr [rbx + r8 + 0x18]
0056D69D  33 D2                           xor edx, edx
0056D69F  48 0F AF C5                     imul rax, rbp
0056D6A3  48 F7 F1                        div rcx
0056D6A6  48 8B C8                        mov rcx, rax
0056D6A9  48 B8 BD 42 7A E5 D5 94 BF D6   movabs rax, 0xd6bf94d5e57a42bd
0056D6B3  48 0F AF 4C 24 40               imul rcx, qword ptr [rsp + 0x40]
0056D6B9  48 F7 E1                        mul rcx
0056D6BC  4C 8B FA                        mov r15, rdx
0056D6BF  49 C1 EF 17                     shr r15, 0x17
0056D6C3  49 8D 87 00 F0 FF FF            lea rax, [r15 - 0x1000]
0056D6CA  48 3D FF EF FF 7F               cmp rax, 0x7fffefff
0056D6D0  76 05                           jbe 0x14056d6d7
0056D6D2  46 8B 7C 03 1C                  mov r15d, dword ptr [rbx + r8 + 0x1c]
0056D6D7  46 89 7C 03 10                  mov dword ptr [rbx + r8 + 0x10], r15d
0056D6DC  4E 89 0C 03                     mov qword ptr [rbx + r8], r9
0056D6E0  EB AA                           jmp 0x14056d68c
0056D6E2  41 8B D1                        mov edx, r9d
0056D6E5  E8 E6 5D F3 FF                  call 0x1404a34d0
0056D6EA  46 8B 3C E3                     mov r15d, dword ptr [rbx + r12*8]
0056D6EE  E9 B6 FE FF FF                  jmp 0x14056d5a9
0056D6F3  8B 52 04                        mov edx, dword ptr [rdx + 4]
0056D6F6  4B 8B 84 F0 40 8C FC 00         mov rax, qword ptr [r8 + r14*8 + 0xfc8c40]
0056D6FE  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056D702  48 83 C0 18                     add rax, 0x18
0056D706  74 03                           je 0x14056d70b
0056D708  8B 40 04                        mov eax, dword ptr [rax + 4]
0056D70B  03 D0                           add edx, eax
0056D70D  4B 8B 84 F0 40 8C FC 00         mov rax, qword ptr [r8 + r14*8 + 0xfc8c40]
0056D715  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056D719  48 85 C0                        test rax, rax
0056D71C  74 03                           je 0x14056d721
0056D71E  8B 40 04                        mov eax, dword ptr [rax + 4]
0056D721  03 D0                           add edx, eax
0056D723  8D 4A 01                        lea ecx, [rdx + 1]
0056D726  B8 FF FF 00 00                  mov eax, 0xffff
0056D72B  41 03 CD                        add ecx, r13d
0056D72E  33 D2                           xor edx, edx
0056D730  41 8B 8C 88 C0 F8 F8 00         mov ecx, dword ptr [r8 + rcx*4 + 0xf8f8c0]
0056D738  0F 30                           wrmsr
0056D73A  41 8B D7                        mov edx, r15d
0056D73D  8B CE                           mov ecx, esi
0056D73F  48 F7 DA                        neg rdx
0056D742  48 8B C2                        mov rax, rdx
0056D745  48 C1 EA 20                     shr rdx, 0x20
0056D749  0F 30                           wrmsr
0056D74B  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
0056D752  48 8B D7                        mov rdx, rdi
0056D755  48 81 CA 00 00 50 00            or rdx, 0x500000
0056D75C  48 8B C2                        mov rax, rdx
0056D75F  48 C1 EA 20                     shr rdx, 0x20
0056D763  0F 30                           wrmsr
0056D765  8B 55 00                        mov edx, dword ptr [rbp]
0056D768  4C 8D 8C 24 A0 00 00 00         lea r9, [rsp + 0xa0]
0056D770  4C 8B C7                        mov r8, rdi
0056D773  41 8B CD                        mov ecx, r13d
0056D776  E8 E9 13 F3 FF                  call 0x14049eb64
0056D77B  80 BC 24 A0 00 00 00 00         cmp byte ptr [rsp + 0xa0], 0
0056D783  48 8D 3D 76 28 A9 FF            lea rdi, [rip - 0x56d78a]
0056D78A  4C 8B 9C 24 B0 00 00 00         mov r11, qword ptr [rsp + 0xb0]
0056D792  74 06                           je 0x14056d79a
0056D794  42 C6 44 E3 28 01               mov byte ptr [rbx + r12*8 + 0x28], 1
0056D79A  41 FF C5                        inc r13d
0056D79D  44 3B 6D 04                     cmp r13d, dword ptr [rbp + 4]
0056D7A1  0F 82 E1 FB FF FF               jb 0x14056d388
0056D7A7  48 83 C4 58                     add rsp, 0x58
0056D7AB  41 5F                           pop r15
0056D7AD  41 5E                           pop r14
0056D7AF  41 5D                           pop r13
0056D7B1  41 5C                           pop r12
0056D7B3  5F                              pop rdi
0056D7B4  5E                              pop rsi
0056D7B5  5D                              pop rbp
0056D7B6  5B                              pop rbx
0056D7B7  C3                              ret
0056D7B8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64OverflowHandlerInternal(int a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (88);
    *(unsigned __int8 *)(v_rsp + 8) = 0;
    v_r13 = 0;
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88);
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 4)) <= 0) goto loc_0056D7A7;
loc_0056D388:
    v_r12 = (v_r13 * 2) + (0);
    v_r12 = (v_r12) + (v_r12);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 24)) != 0) goto loc_0056D79A;
    a3 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)))))) - (1));
    if (condition_is_equal) goto loc_0056D3EC;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056D3D4;
    if (a1 != 1) goto loc_0056D403;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)) + (48);
    if (!(condition_is_equal)) {
        a3 = *(unsigned int *)(a3 + 4);
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)) + (24);
    if (!(condition_is_equal)) {
        result = *(unsigned int *)(result + 4);
    }
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
loc_0056D3EC:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 4);
    }
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
loc_0056D403:
    a3 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 5690196 + a3 + v_r13 * 1 * 4 + 16316736)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056D457;
    a2 = (unsigned int)((a2) - (99));
    if (condition_is_equal) goto loc_0056D43F;
    if (a2 != 1) goto loc_0056D46E;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)) + (48);
    if (!(condition_is_equal)) {
        a3 = *(unsigned int *)(a3 + 4);
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)) + (24);
    if (!(condition_is_equal)) {
        result = *(unsigned int *)(result + 4);
    }
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
loc_0056D457:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 4);
    }
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
loc_0056D46E:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 5690196 + a3 + v_r13 * 1 * 4 + 16316608)));
    a2 = (a2) << (32);
    result = (a3 + v_r13 * 1) | (a2);
    result = (result) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 5690196 + a3 + v_r13 * 1 * 4 + 16316608)))));
    if (result >= ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 5690196 + a3 + v_r13 * 1 * 4 + 16316608)))))) goto loc_0056D79A;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_m70 = result;
    a2 = (result) & (0xFFFFFFFFFFAFFFFFULL);
    a2 = (a2) >> (32);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36))) != 0) goto loc_0056D6E2;
    if (*(unsigned __int64 *)(v_rip + 9055855) == 0) goto loc_0056D4FD;
    result = guard_dispatch_icall(a3, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
    goto loc_0056D504;
loc_0056D4FD:
    a2 = 0;
    result = KeProfileInterruptWithSource(a3, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
loc_0056D504:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16)) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 24))) == 0) goto loc_0056D59F;
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 32))))) << (4);
    v_rsi = (v_rsi) + (v_rbx);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 32))) + 1);
    result = (unsigned int)((result) & (15));
    *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 32) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 20))) != 0) goto loc_0056D601;
    a2 = 0;
    *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 20) = (unsigned int)((unsigned int)(0x2710ULL));
    if ((unsigned int)((unsigned int)(0x2710ULL)) == 0) {
        *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 20) = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m68, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
    a1 = 0;
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 8) = v_stack_m68;
    result = KeQueryPerformanceCounter(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10832994) * 1) = result;
    *(unsigned int *)(v_rsi + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 16)));
    *(unsigned __int64 *)(v_rsi + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 48) = *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10832994) * 1);
loc_0056D598:
loc_0056D59F:
loc_0056D5A9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)))) != 0) goto loc_0056D73A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m78 + v_r12 * 8 + 16) + 8)) == ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)))))) goto loc_0056D73A;
    a2 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056D70D;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056D6F6;
    if (a1 != 1) goto loc_0056D723;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690827 + (unsigned int)(a2) * 8 + 16550976) + 88)) + (48);
    if (condition_is_not_equal) goto loc_0056D6F3;
    goto loc_0056D6F6;
loc_0056D601:
    result = (unsigned int)((*(unsigned __int64 *)(v_rip - 5690827 + (unsigned int)(a2) * 8 + 16550976)) - (1));
    *(unsigned int *)(v_stack_m78 + v_stack_m70 * 1 + 20) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0056D598;
    a2 = 0;
    *(unsigned int *)(v_stack_m78 + v_stack_m70 * 1 + 20) = (unsigned int)((unsigned int)(0x2710ULL));
    result = (unsigned int)(0x2710ULL);
    v_rbp = (unsigned int)((unsigned int)((unsigned int)(0x2710ULL)));
    if ((unsigned int)((unsigned int)(0x2710ULL)) == 0) {
        result = (unsigned int)((unsigned int)((unsigned int)(0x2710ULL))) + 1;
        *(unsigned int *)(v_stack_m78 + v_stack_m70 * 1 + 20) = (unsigned int)(result);
        v_rbp = (unsigned int)(result);
    }
    result = PoGetProcessorIdleAccounting(v_stack_m68, a2, v_rip - 5690827, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
    if (v_stack_m68 == (*(unsigned __int64 *)(v_stack_m78 + v_stack_m70 * 1 + 8))) goto loc_0056D66B;
    a1 = 0;
    *(unsigned __int64 *)(v_stack_m78 + v_stack_m70 * 1 + 8) = v_stack_m68;
    result = KeQueryPerformanceCounter(a1, a2, v_rip - 5690827, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
    *(unsigned __int64 *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832793) * 1) = result;
    *(unsigned int *)((unsigned int)(v_stack_p10) + v_stack_m70 * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 16)));
    *(unsigned __int64 *)((unsigned int)(v_stack_p10) + v_stack_m70 * 1 + 48) = *(unsigned __int64 *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832793) * 1);
loc_0056D661:
    goto loc_0056D598;
loc_0056D66B:
    v_rbp = (unsigned int)((v_stack_m60) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 16)))));
    result = KeQueryPerformanceCounter(v_stack_m58, a2, v_rip - 5690827, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5690196 + (unsigned int)(a2) * 8 + 16550976) + 88) + 16) + v_r12 * 8 + 36)));
    a1 = (result) - (*(unsigned __int64 *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832744) * 1));
    if (condition_is_not_equal) goto loc_0056D698;
loc_0056D68C:
    *(unsigned int *)((unsigned int)(v_stack_p10) + v_stack_m70 * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10833109) * 1 + 16)));
    *(unsigned __int64 *)((unsigned int)(v_stack_p10) + v_stack_m70 * 1 + 48) = result;
    goto loc_0056D661;
loc_0056D698:
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832744) * 1 + 24))) * (v_rbp);
    a1 = (result) * (v_stack_m58);
    v_r15 = (0) >> (23);
    if ((v_r15 - 4096) >= = 0x7FFFEFFFULL) {
        v_r15 = *(unsigned int *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832744) * 1 + 28);
    }
    *(unsigned int *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832744) * 1 + 16) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_stack_m78 + *(unsigned __int64 *)(v_rip + 10832744) * 1) = result;
    goto loc_0056D68C;
loc_0056D6E2:
    result = KeProfileInterruptWithSource(a1, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rip + 10832744), result);
    goto loc_0056D5A9;
loc_0056D6F3:
loc_0056D6F6:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10832744) + (unsigned int)(a2) * 8 + 16550976) + 88)) + (24);
    if (!(condition_is_equal)) {
        result = *(unsigned int *)(result + 4);
    }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 4))) + ((unsigned int)(result)));
loc_0056D70D:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10832744) + (unsigned int)(a2) * 8 + 16550976) + 88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10832744) + (unsigned int)(a2) * 8 + 16550976) + 88) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10832744) + (unsigned int)(a2) * 8 + 16550976) + 88) + 4);
    }
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
loc_0056D723:
    a1 = (unsigned int)((a2 + 1) + (0));
    a2 = 0;
loc_0056D73A:
    a2 = -((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m78 + v_r12 * 8)))));
    a2 = (a2) >> (32);
    a2 = (v_stack_m70) | (0x500000ULL);
    a2 = (a2) >> (32);
    result = Amd64IsModifiedByBadActorInternal(0, (unsigned int)(*(unsigned int *)(v_rbp)), v_stack_m70, v_stack_p8);
    if (v_stack_p8 != 0) {
        *(unsigned __int8 *)(v_stack_m78 + v_r12 * 8 + 40) = 1;
    }
    v_r13 = (unsigned int)((v_r13) + 1);
    if (((unsigned int)(v_r13)) < (*(unsigned int *)(v_rbp + 4))) goto loc_0056D388;
loc_0056D7A7:
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Amd64OverflowHandlerInternal(int32_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (88);
    *(uint8_t *)(local_rsp + 0x8) = 0;
    local_r13 = 0;
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58);
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x4)) <= 0) goto loc_0056D7A7;
loc_0056D388:
    local_r12 = (local_r13 * 2) + (0);
    local_r12 = (local_r12) + (local_r12);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x18)) != 0) goto loc_0056D79A;
    Arg3 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)))))) - (1));
    if (condition_is_equal) goto loc_0056D3EC;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056D3D4;
    if (Arg1 != 1) goto loc_0056D403;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (!(condition_is_equal)) {
        Arg3 = *(uint32_t *)(Arg3 + 0x4);
    }
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (!(condition_is_equal)) {
        result = *(uint32_t *)(result + 0x4);
    }
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result)));
loc_0056D3EC:
    result = *(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58);
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result)));
loc_0056D403:
    Arg3 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x56D354 + Arg3 + local_r13 * 1 * 4 + 0xF8F940)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056D457;
    Arg2 = (uint32_t)((Arg2) - (99));
    if (condition_is_equal) goto loc_0056D43F;
    if (Arg2 != 1) goto loc_0056D46E;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (!(condition_is_equal)) {
        Arg3 = *(uint32_t *)(Arg3 + 0x4);
    }
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (!(condition_is_equal)) {
        result = *(uint32_t *)(result + 0x4);
    }
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result)));
loc_0056D457:
    result = *(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58);
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result)));
loc_0056D46E:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x56D354 + Arg3 + local_r13 * 1 * 4 + 0xF8F8C0)));
    Arg2 = (Arg2) << (32);
    result = (Arg3 + local_r13 * 1) | (Arg2);
    result = (result) & ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x56D354 + Arg3 + local_r13 * 1 * 4 + 0xF8F8C0)))));
    if (result >= ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x56D354 + Arg3 + local_r13 * 1 * 4 + 0xF8F8C0)))))) goto loc_0056D79A;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_m70 = result;
    Arg2 = (result) & (0xFFFFFFFFFFAFFFFFULL);
    Arg2 = (Arg2) >> (32);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24))) != 0) goto loc_0056D6E2;
    if (*(uint64_t *)(v_rip + 0x8A2E6F) == 0) goto loc_0056D4FD;
    result = guard_dispatch_icall(Arg3, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
    goto loc_0056D504;
loc_0056D4FD:
    Arg2 = 0;
    result = KeProfileInterruptWithSource(Arg3, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
loc_0056D504:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10)) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x18))) == 0) goto loc_0056D59F;
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x20))))) << (4);
    local_rsi = (local_rsi) + (local_rbx);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x20))) + 1);
    result = (uint32_t)((result) & (15));
    *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x20) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x14))) != 0) goto loc_0056D601;
    Arg2 = 0;
    *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x14) = (uint32_t)((uint32_t)(0x2710ULL));
    if ((uint32_t)((uint32_t)(0x2710ULL)) == 0) {
        *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x14) = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m68, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
    Arg1 = 0;
    *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x8) = v_stack_m68;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
    *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54C62) * 1) = result;
    *(uint32_t *)(local_rsi + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x10)));
    *(uint64_t *)(local_rsi + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x30) = *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54C62) * 1);
loc_0056D598:
loc_0056D59F:
loc_0056D5A9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)))) != 0) goto loc_0056D73A;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m78 + local_r12 * 8 + 0x10) + 0x8)) == ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)))))) goto loc_0056D73A;
    Arg2 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056D70D;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056D6F6;
    if (Arg1 != 1) goto loc_0056D723;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D5CB + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (condition_is_not_equal) goto loc_0056D6F3;
    goto loc_0056D6F6;
loc_0056D601:
    result = (uint32_t)((*(uint64_t *)(v_rip - 0x56D5CB + (uint32_t)(Arg2) * 8 + 0xFC8C40)) - (1));
    *(uint32_t *)(v_stack_m78 + v_stack_m70 * 1 + 0x14) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0056D598;
    Arg2 = 0;
    *(uint32_t *)(v_stack_m78 + v_stack_m70 * 1 + 0x14) = (uint32_t)((uint32_t)(0x2710ULL));
    result = (uint32_t)(0x2710ULL);
    local_rbp = (uint32_t)((uint32_t)((uint32_t)(0x2710ULL)));
    if ((uint32_t)((uint32_t)(0x2710ULL)) == 0) {
        result = (uint32_t)((uint32_t)((uint32_t)(0x2710ULL))) + 1;
        *(uint32_t *)(v_stack_m78 + v_stack_m70 * 1 + 0x14) = (uint32_t)(result);
        local_rbp = (uint32_t)(result);
    }
    result = PoGetProcessorIdleAccounting(v_stack_m68, Arg2, v_rip - 5690827, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
    if (v_stack_m68 == (*(uint64_t *)(v_stack_m78 + v_stack_m70 * 1 + 0x8))) goto loc_0056D66B;
    Arg1 = 0;
    *(uint64_t *)(v_stack_m78 + v_stack_m70 * 1 + 0x8) = v_stack_m68;
    result = KeQueryPerformanceCounter(Arg1, Arg2, v_rip - 5690827, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
    *(uint64_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B99) * 1) = result;
    *(uint32_t *)((uint32_t)(v_stack_p10) + v_stack_m70 * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x10)));
    *(uint64_t *)((uint32_t)(v_stack_p10) + v_stack_m70 * 1 + 0x30) = *(uint64_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B99) * 1);
loc_0056D661:
    goto loc_0056D598;
loc_0056D66B:
    local_rbp = (uint32_t)((v_stack_m60) * ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x10)))));
    result = KeQueryPerformanceCounter(v_stack_m58, Arg2, v_rip - 5690827, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56D354 + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x10) + local_r12 * 8 + 0x24)));
    Arg1 = (result) - (*(uint64_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B68) * 1));
    if (condition_is_not_equal) goto loc_0056D698;
loc_0056D68C:
    *(uint32_t *)((uint32_t)(v_stack_p10) + v_stack_m70 * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA54CD5) * 1 + 0x10)));
    *(uint64_t *)((uint32_t)(v_stack_p10) + v_stack_m70 * 1 + 0x30) = result;
    goto loc_0056D661;
loc_0056D698:
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B68) * 1 + 0x18))) * (local_rbp);
    Arg1 = (result) * (v_stack_m58);
    local_r15 = (0) >> (23);
    if ((local_r15 - 4096) >= = 0x7FFFEFFFULL) {
        local_r15 = *(uint32_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B68) * 1 + 0x1C);
    }
    *(uint32_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B68) * 1 + 0x10) = (uint32_t)(local_r15);
    *(uint64_t *)(v_stack_m78 + *(uint64_t *)(v_rip + 0xA54B68) * 1) = result;
    goto loc_0056D68C;
loc_0056D6E2:
    result = KeProfileInterruptWithSource(Arg1, (uint32_t)((uint32_t)(result)), *(uint64_t *)(v_rip + 0xA54B68), result);
    goto loc_0056D5A9;
loc_0056D6F3:
loc_0056D6F6:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA54B68) + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (!(condition_is_equal)) {
        result = *(uint32_t *)(result + 0x4);
    }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x4))) + ((uint32_t)(result)));
loc_0056D70D:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA54B68) + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA54B68) + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA54B68) + (uint32_t)(Arg2) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
loc_0056D723:
    Arg1 = (uint32_t)((Arg2 + 1) + (0));
    Arg2 = 0;
loc_0056D73A:
    Arg2 = -((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m78 + local_r12 * 8)))));
    Arg2 = (Arg2) >> (32);
    Arg2 = (v_stack_m70) | (0x500000ULL);
    Arg2 = (Arg2) >> (32);
    result = Amd64IsModifiedByBadActorInternal(0, (uint32_t)(*(uint32_t *)(local_rbp)), v_stack_m70, v_stack_p8);
    if (v_stack_p8 != 0) {
        *(uint8_t *)(v_stack_m78 + local_r12 * 8 + 0x28) = 1;
    }
    local_r13 = (uint32_t)((local_r13) + 1);
    if (((uint32_t)(local_r13)) < (*(uint32_t *)(local_rbp + 0x4))) goto loc_0056D388;
loc_0056D7A7:
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056D330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
