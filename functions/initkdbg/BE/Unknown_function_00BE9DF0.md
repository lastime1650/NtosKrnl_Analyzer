# sub_00BE9DF0

- RVA: `0x00BE9DF0`–`0x00BEA549` (길이 `1,881` bytes)
- VA: `0x0000000140BE9DF0`
- 실행 섹션: `INITKDBG`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2D38`
- 디코드: `439`개 명령, `1,881/1,881` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BE9F31` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE9F45` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA037` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA19A` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA20C` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA222` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA2E2` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BEA2FC` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BEA3DC` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA433` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)
- `0x00BEA51F` → [RtlMinimalBarrier](RtlMinimalBarrier_function_00BEABE4.md) (function, `0x00BEABE4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BE9DF0  40 53                           push rbx
00BE9DF2  56                              push rsi
00BE9DF3  57                              push rdi
00BE9DF4  41 54                           push r12
00BE9DF6  41 55                           push r13
00BE9DF8  41 56                           push r14
00BE9DFA  41 57                           push r15
00BE9DFC  48 83 EC 60                     sub rsp, 0x60
00BE9E00  48 8B D9                        mov rbx, rcx
00BE9E03  48 8B 89 A8 0A 00 00            mov rcx, qword ptr [rcx + 0xaa8]
00BE9E0A  83 39 2C                        cmp dword ptr [rcx], 0x2c
00BE9E0D  0F 84 28 01 00 00               je 0x140be9f3b
00BE9E13  33 F6                           xor esi, esi
00BE9E15  39 B3 18 09 00 00               cmp dword ptr [rbx + 0x918], esi
00BE9E1B  0F 85 14 07 00 00               jne 0x140bea535
00BE9E21  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE9E2B  48 C7 83 30 09 00 00 01 01 00 00  mov qword ptr [rbx + 0x930], 0x101
00BE9E36  48 03 C3                        add rax, rbx
00BE9E39  48 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], rsi
00BE9E40  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
00BE9E47  44 8D 76 01                     lea r14d, [rsi + 1]
00BE9E4B  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
00BE9E55  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
00BE9E5C  48 03 C1                        add rax, rcx
00BE9E5F  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE9E65  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
00BE9E6C  0F BA E1 1D                     bt ecx, 0x1d
00BE9E70  0F 82 BF 06 00 00               jb 0x140bea535
00BE9E76  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
00BE9E80  0F 84 AF 06 00 00               je 0x140bea535
00BE9E86  41 84 CE                        test r14b, cl
00BE9E89  0F 84 A6 06 00 00               je 0x140bea535
00BE9E8F  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
00BE9E95  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE9E9B  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
00BE9EA2  2B C1                           sub eax, ecx
00BE9EA4  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
00BE9EAB  48 8D 14 19                     lea rdx, [rcx + rbx]
00BE9EAF  8B C8                           mov ecx, eax
00BE9EB1  48 C1 E9 03                     shr rcx, 3
00BE9EB5  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE9EB9  EB 21                           jmp 0x140be9edc
00BE9EBB  4C 31 02                        xor qword ptr [rdx], r8
00BE9EBE  48 8B 02                        mov rax, qword ptr [rdx]
00BE9EC1  41 0F B6 C8                     movzx ecx, r8b
00BE9EC5  49 33 C2                        xor rax, r10
00BE9EC8  83 E1 3F                        and ecx, 0x3f
00BE9ECB  49 D3 C8                        ror r8, cl
00BE9ECE  4C 03 C0                        add r8, rax
00BE9ED1  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE9ED8  48 83 C2 08                     add rdx, 8
00BE9EDC  49 3B D1                        cmp rdx, r9
00BE9EDF  75 DA                           jne 0x140be9ebb
00BE9EE1  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
00BE9EE9  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
00BE9EF0  0F 84 3F 06 00 00               je 0x140bea535
00BE9EF6  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
00BE9EFC  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE9F03  48 89 18                        mov qword ptr [rax], rbx
00BE9F06  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE9F09  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
00BE9F10  39 B3 18 09 00 00               cmp dword ptr [rbx + 0x918], esi
00BE9F16  75 0E                           jne 0x140be9f26
00BE9F18  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE9F1F  49 33 C8                        xor rcx, r8
00BE9F22  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE9F26  33 D2                           xor edx, edx
00BE9F28  41 B9 00 01 00 00               mov r9d, 0x100
00BE9F2E  48 8B CB                        mov rcx, rbx
00BE9F31  E8 4E E4 FF FF                  call 0x140be8384
00BE9F36  E9 FA 05 00 00                  jmp 0x140bea535
00BE9F3B  48 8D 8B 88 0A 00 00            lea rcx, [rbx + 0xa88]
00BE9F42  FA                              cli
00BE9F43  33 D2                           xor edx, edx
00BE9F45  E8 9A 0C 00 00                  call 0x140beabe4
00BE9F4A  48 8B 83 B0 0A 00 00            mov rax, qword ptr [rbx + 0xab0]
00BE9F51  33 F6                           xor esi, esi
00BE9F53  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00BE9F5B  44 8D 76 01                     lea r14d, [rsi + 1]
00BE9F5F  44 8D 5E 02                     lea r11d, [rsi + 2]
00BE9F63  65 48 8B 04 25 18 00 00 00      mov rax, qword ptr gs:[0x18]
00BE9F6C  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00BE9F71  48 8B BB E0 08 00 00            mov rdi, qword ptr [rbx + 0x8e0]
00BE9F78  41 B8 10 00 00 00               mov r8d, 0x10
00BE9F7E  44 8B AB 14 09 00 00            mov r13d, dword ptr [rbx + 0x914]
00BE9F85  4D 8B CB                        mov r9, r11
00BE9F88  4C 8B 50 38                     mov r10, qword ptr [rax + 0x38]
00BE9F8C  48 8D 4F 20                     lea rcx, [rdi + 0x20]
00BE9F90  48 8B 01                        mov rax, qword ptr [rcx]
00BE9F93  41 83 C0 F8                     add r8d, -8
00BE9F97  48 89 02                        mov qword ptr [rdx], rax
00BE9F9A  48 83 C1 08                     add rcx, 8
00BE9F9E  48 83 C2 08                     add rdx, 8
00BE9FA2  4D 2B CE                        sub r9, r14
00BE9FA5  75 E9                           jne 0x140be9f90
00BE9FA7  45 85 C0                        test r8d, r8d
00BE9FAA  74 10                           je 0x140be9fbc
00BE9FAC  8A 01                           mov al, byte ptr [rcx]
00BE9FAE  49 03 CE                        add rcx, r14
00BE9FB1  88 02                           mov byte ptr [rdx], al
00BE9FB3  49 03 D6                        add rdx, r14
00BE9FB6  41 83 C0 FF                     add r8d, -1
00BE9FBA  75 F0                           jne 0x140be9fac
00BE9FBC  4C 8D BF 20 01 00 00            lea r15, [rdi + 0x120]
00BE9FC3  41 B8 10 00 00 00               mov r8d, 0x10
00BE9FC9  49 8B CF                        mov rcx, r15
00BE9FCC  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00BE9FD1  4D 8B CB                        mov r9, r11
00BE9FD4  48 8B 01                        mov rax, qword ptr [rcx]
00BE9FD7  41 83 C0 F8                     add r8d, -8
00BE9FDB  48 89 02                        mov qword ptr [rdx], rax
00BE9FDE  48 83 C1 08                     add rcx, 8
00BE9FE2  48 83 C2 08                     add rdx, 8
00BE9FE6  4D 2B CE                        sub r9, r14
00BE9FE9  75 E9                           jne 0x140be9fd4
00BE9FEB  45 85 C0                        test r8d, r8d
00BE9FEE  74 10                           je 0x140bea000
00BE9FF0  8A 01                           mov al, byte ptr [rcx]
00BE9FF2  49 03 CE                        add rcx, r14
00BE9FF5  88 02                           mov byte ptr [rdx], al
00BE9FF7  49 03 D6                        add rdx, r14
00BE9FFA  41 83 C0 FF                     add r8d, -1
00BE9FFE  75 F0                           jne 0x140be9ff0
00BEA000  41 8A 02                        mov al, byte ptr [r10]
00BEA003  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00BEA00D  49 C1 EA 09                     shr r10, 9
00BEA011  33 D2                           xor edx, edx
00BEA013  4C 23 D1                        and r10, rcx
00BEA016  48 8D 8B 88 0A 00 00            lea rcx, [rbx + 0xa88]
00BEA01D  4C 03 93 D8 05 00 00            add r10, qword ptr [rbx + 0x5d8]
00BEA024  4C 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r10
00BEA02C  49 8B 02                        mov rax, qword ptr [r10]
00BEA02F  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00BEA037  E8 A8 0B 00 00                  call 0x140beabe4
00BEA03C  84 C0                           test al, al
00BEA03E  0F 84 44 01 00 00               je 0x140bea188
00BEA044  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
00BEA04C  48 8D 43 10                     lea rax, [rbx + 0x10]
00BEA050  49 03 C5                        add rax, r13
00BEA053  48 8D 97 00 04 00 00            lea rdx, [rdi + 0x400]
00BEA05A  48 8B C8                        mov rcx, rax
00BEA05D  66 89 47 20                     mov word ptr [rdi + 0x20], ax
00BEA061  48 C1 E9 10                     shr rcx, 0x10
00BEA065  41 B8 00 10 00 00               mov r8d, 0x1000
00BEA06B  48 C1 E8 20                     shr rax, 0x20
00BEA06F  41 B9 00 02 00 00               mov r9d, 0x200
00BEA075  89 47 28                        mov dword ptr [rdi + 0x28], eax
00BEA078  48 8D 83 90 00 00 00            lea rax, [rbx + 0x90]
00BEA07F  49 03 C5                        add rax, r13
00BEA082  66 89 4F 26                     mov word ptr [rdi + 0x26], cx
00BEA086  48 8B C8                        mov rcx, rax
00BEA089  66 41 89 07                     mov word ptr [r15], ax
00BEA08D  48 C1 E9 10                     shr rcx, 0x10
00BEA091  41 BD F8 FF FF FF               mov r13d, 0xfffffff8
00BEA097  48 C1 E8 20                     shr rax, 0x20
00BEA09B  66 89 8F 26 01 00 00            mov word ptr [rdi + 0x126], cx
00BEA0A2  49 8B CA                        mov rcx, r10
00BEA0A5  89 87 28 01 00 00               mov dword ptr [rdi + 0x128], eax
00BEA0AB  48 8B 01                        mov rax, qword ptr [rcx]
00BEA0AE  45 03 C5                        add r8d, r13d
00BEA0B1  48 89 02                        mov qword ptr [rdx], rax
00BEA0B4  48 83 C1 08                     add rcx, 8
00BEA0B8  48 83 C2 08                     add rdx, 8
00BEA0BC  4D 2B CE                        sub r9, r14
00BEA0BF  75 EA                           jne 0x140bea0ab
00BEA0C1  41 83 CB FF                     or r11d, 0xffffffff
00BEA0C5  45 85 C0                        test r8d, r8d
00BEA0C8  74 0F                           je 0x140bea0d9
00BEA0CA  8A 01                           mov al, byte ptr [rcx]
00BEA0CC  49 03 CE                        add rcx, r14
00BEA0CF  88 02                           mov byte ptr [rdx], al
00BEA0D1  49 03 D6                        add rdx, r14
00BEA0D4  45 03 C3                        add r8d, r11d
00BEA0D7  75 F1                           jne 0x140bea0ca
00BEA0D9  C7 83 BE 08 00 00 4C 89 C0 F0   mov dword ptr [rbx + 0x8be], 0xf0c0894c
00BEA0E3  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00BEA0E8  C7 83 C2 08 00 00 48 0F B1 11   mov dword ptr [rbx + 0x8c2], 0x11b10f48
00BEA0F2  49 8B C2                        mov rax, r10
00BEA0F5  C7 83 C6 08 00 00 0F 94 C0 C3   mov dword ptr [rbx + 0x8c6], 0xc3c0940f
00BEA0FF  41 B8 04 00 00 00               mov r8d, 4
00BEA105  4C 89 97 08 14 00 00            mov qword ptr [rdi + 0x1408], r10
00BEA10C  41 8B D0                        mov edx, r8d
00BEA10F  4C 89 97 10 14 00 00            mov qword ptr [rdi + 0x1410], r10
00BEA116  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
00BEA120  48 C1 E8 09                     shr rax, 9
00BEA124  48 89 9F 00 14 00 00            mov qword ptr [rdi + 0x1400], rbx
00BEA12B  49 23 C2                        and rax, r10
00BEA12E  44 89 9F 34 14 00 00            mov dword ptr [rdi + 0x1434], r11d
00BEA135  44 89 87 30 14 00 00            mov dword ptr [rdi + 0x1430], r8d
00BEA13C  4C 8B 8B D8 05 00 00            mov r9, qword ptr [rbx + 0x5d8]
00BEA143  49 03 C1                        add rax, r9
00BEA146  48 89 01                        mov qword ptr [rcx], rax
00BEA149  48 8D 49 08                     lea rcx, [rcx + 8]
00BEA14D  48 C1 E8 09                     shr rax, 9
00BEA151  49 23 C2                        and rax, r10
00BEA154  49 03 C1                        add rax, r9
00BEA157  49 2B D6                        sub rdx, r14
00BEA15A  75 EA                           jne 0x140bea146
00BEA15C  45 03 C3                        add r8d, r11d
00BEA15F  74 0F                           je 0x140bea170
00BEA161  4A 8B 44 C4 40                  mov rax, qword ptr [rsp + r8*8 + 0x40]
00BEA166  8B 08                           mov ecx, dword ptr [rax]
00BEA168  C0 E9 07                        shr cl, 7
00BEA16B  41 84 CE                        test r14b, cl
00BEA16E  74 EC                           je 0x140bea15c
00BEA170  4A 8B 44 C4 40                  mov rax, qword ptr [rsp + r8*8 + 0x40]
00BEA175  48 89 87 28 14 00 00            mov qword ptr [rdi + 0x1428], rax
00BEA17C  48 8B 00                        mov rax, qword ptr [rax]
00BEA17F  48 89 87 20 14 00 00            mov qword ptr [rdi + 0x1420], rax
00BEA186  EB 06                           jmp 0x140bea18e
00BEA188  41 BD F8 FF FF FF               mov r13d, 0xfffffff8
00BEA18E  4C 8D A3 88 0A 00 00            lea r12, [rbx + 0xa88]
00BEA195  33 D2                           xor edx, edx
00BEA197  49 8B CC                        mov rcx, r12
00BEA19A  E8 45 0A 00 00                  call 0x140beabe4
00BEA19F  48 8B 8F 18 14 00 00            mov rcx, qword ptr [rdi + 0x1418]
00BEA1A6  48 BA FF 0F 00 00 00 00 F0 FF   movabs rdx, 0xfff0000000000fff
00BEA1B0  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00BEA1B8  48 C1 E1 0C                     shl rcx, 0xc
00BEA1BC  48 33 C1                        xor rax, rcx
00BEA1BF  48 23 C2                        and rax, rdx
00BEA1C2  48 33 C1                        xor rax, rcx
00BEA1C5  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00BEA1CD  48 89 01                        mov qword ptr [rcx], rax
00BEA1D0  48 8B 87 20 14 00 00            mov rax, qword ptr [rdi + 0x1420]
00BEA1D7  48 8B 8F 28 14 00 00            mov rcx, qword ptr [rdi + 0x1428]
00BEA1DE  48 83 C8 42                     or rax, 0x42
00BEA1E2  48 89 01                        mov qword ptr [rcx], rax
00BEA1E5  0F 20 E1                        mov rcx, cr4
00BEA1E8  48 F7 C1 80 00 02 00            test rcx, 0x20080
00BEA1EF  74 10                           je 0x140bea201
00BEA1F1  48 8B C1                        mov rax, rcx
00BEA1F4  48 0F BA F8 07                  btc rax, 7
00BEA1F9  0F 22 E0                        mov cr4, rax
00BEA1FC  0F 22 E1                        mov cr4, rcx
00BEA1FF  EB 06                           jmp 0x140bea207
00BEA201  0F 20 D8                        mov rax, cr3
00BEA204  0F 22 D8                        mov cr3, rax
00BEA207  33 D2                           xor edx, edx
00BEA209  49 8B CC                        mov rcx, r12
00BEA20C  E8 D3 09 00 00                  call 0x140beabe4
00BEA211  84 C0                           test al, al
00BEA213  74 08                           je 0x140bea21d
00BEA215  F0 83 A7 30 14 00 00 FB         lock and dword ptr [rdi + 0x1430], 0xfffffffb
00BEA21D  33 D2                           xor edx, edx
00BEA21F  49 8B CC                        mov rcx, r12
00BEA222  E8 BD 09 00 00                  call 0x140beabe4
00BEA227  84 C0                           test al, al
00BEA229  0F 84 A8 01 00 00               je 0x140bea3d7
00BEA22F  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00BEA237  4C 8D BF 00 04 00 00            lea r15, [rdi + 0x400]
00BEA23E  4D 8B EF                        mov r13, r15
00BEA241  89 87 34 14 00 00               mov dword ptr [rdi + 0x1434], eax
00BEA247  44 8B E6                        mov r12d, esi
00BEA24A  F7 83 DC 09 00 00 00 00 02 00   test dword ptr [rbx + 0x9dc], 0x20000
00BEA254  4C 8D 8F 10 14 00 00            lea r9, [rdi + 0x1410]
00BEA25B  4C 8B 9C 24 A0 00 00 00         mov r11, qword ptr [rsp + 0xa0]
00BEA263  4C 8D 93 BE 08 00 00            lea r10, [rbx + 0x8be]
00BEA26A  45 8B C4                        mov r8d, r12d
00BEA26D  75 46                           jne 0x140bea2b5
00BEA26F  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00BEA278  48 B9 E8 B4 C8 91 58 3F A0 A3   movabs rcx, 0xa3a03f5891c8b4e8
00BEA282  48 8B 83 B8 04 00 00            mov rax, qword ptr [rbx + 0x4b8]
00BEA289  48 03 CB                        add rcx, rbx
00BEA28C  48 89 08                        mov qword ptr [rax], rcx
00BEA28F  4B 8D 0C 18                     lea rcx, [r8 + r11]
00BEA293  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
00BEA29A  48 89 10                        mov qword ptr [rax], rdx
00BEA29D  48 8B 83 C8 04 00 00            mov rax, qword ptr [rbx + 0x4c8]
00BEA2A4  48 89 08                        mov qword ptr [rax], rcx
00BEA2A7  48 8B 83 D0 04 00 00            mov rax, qword ptr [rbx + 0x4d0]
00BEA2AE  48 C7 00 14 01 00 00            mov qword ptr [rax], 0x114
00BEA2B5  33 C0                           xor eax, eax
00BEA2B7  4B 8D 0C 18                     lea rcx, [r8 + r11]
00BEA2BB  49 89 09                        mov qword ptr [r9], rcx
00BEA2BE  8D 50 02                        lea edx, [rax + 2]
00BEA2C1  F0 0F B1 97 30 14 00 00         lock cmpxchg dword ptr [rdi + 0x1430], edx
00BEA2C9  75 62                           jne 0x140bea32d
00BEA2CB  41 F6 C4 07                     test r12b, 7
00BEA2CF  75 21                           jne 0x140bea2f2
00BEA2D1  4D 8B 45 00                     mov r8, qword ptr [r13]
00BEA2D5  48 BA C3 C3 C3 C3 C3 C3 C3 C3   movabs rdx, 0xc3c3c3c3c3c3c3c3
00BEA2DF  49 8B C2                        mov rax, r10
00BEA2E2  E8 79 07 00 00                  call 0x140beaa60
00BEA2E7  84 C0                           test al, al
00BEA2E9  74 32                           je 0x140bea31d
00BEA2EB  4C 8D 8F 10 14 00 00            lea r9, [rdi + 0x1410]
00BEA2F2  49 8B C9                        mov rcx, r9
00BEA2F5  48 8D 83 B3 08 00 00            lea rax, [rbx + 0x8b3]
00BEA2FC  E8 5F 07 00 00                  call 0x140beaa60
00BEA301  F0 83 A7 30 14 00 00 FD         lock and dword ptr [rdi + 0x1430], 0xfffffffd
00BEA309  45 03 E6                        add r12d, r14d
00BEA30C  4D 03 EE                        add r13, r14
00BEA30F  41 81 FC 00 10 00 00            cmp r12d, 0x1000
00BEA316  73 0D                           jae 0x140bea325
00BEA318  E9 2D FF FF FF                  jmp 0x140bea24a
00BEA31D  F0 83 A7 30 14 00 00 FD         lock and dword ptr [rdi + 0x1430], 0xfffffffd
00BEA325  4C 8B 9C 24 A0 00 00 00         mov r11, qword ptr [rsp + 0xa0]
00BEA32D  41 BD 00 10 00 00               mov r13d, 0x1000
00BEA333  45 3B E5                        cmp r12d, r13d
00BEA336  74 16                           je 0x140bea34e
00BEA338  F0 83 8F 30 14 00 00 08         lock or dword ptr [rdi + 0x1430], 8
00BEA340  49 8D 83 FF 0F 00 00            lea rax, [r11 + 0xfff]
00BEA347  48 89 87 10 14 00 00            mov qword ptr [rdi + 0x1410], rax
00BEA34E  41 8B D5                        mov edx, r13d
00BEA351  49 8B CB                        mov rcx, r11
00BEA354  41 BD F8 FF FF FF               mov r13d, 0xfffffff8
00BEA35A  41 B8 00 02 00 00               mov r8d, 0x200
00BEA360  49 8B 07                        mov rax, qword ptr [r15]
00BEA363  41 03 D5                        add edx, r13d
00BEA366  48 89 01                        mov qword ptr [rcx], rax
00BEA369  49 83 C7 08                     add r15, 8
00BEA36D  48 83 C1 08                     add rcx, 8
00BEA371  4D 2B C6                        sub r8, r14
00BEA374  75 EA                           jne 0x140bea360
00BEA376  85 D2                           test edx, edx
00BEA378  74 10                           je 0x140bea38a
00BEA37A  41 8A 07                        mov al, byte ptr [r15]
00BEA37D  4D 03 FE                        add r15, r14
00BEA380  88 01                           mov byte ptr [rcx], al
00BEA382  49 03 CE                        add rcx, r14
00BEA385  83 C2 FF                        add edx, -1
00BEA388  75 F0                           jne 0x140bea37a
00BEA38A  F0 83 8F 30 14 00 00 04         lock or dword ptr [rdi + 0x1430], 4
00BEA392  F7 83 DC 09 00 00 00 00 02 00   test dword ptr [rbx + 0x9dc], 0x20000
00BEA39C  4C 8D A3 88 0A 00 00            lea r12, [rbx + 0xa88]
00BEA3A3  75 32                           jne 0x140bea3d7
00BEA3A5  48 8B 83 B8 04 00 00            mov rax, qword ptr [rbx + 0x4b8]
00BEA3AC  48 B9 E8 B4 C8 91 58 3F A0 A3   movabs rcx, 0xa3a03f5891c8b4e8
00BEA3B6  48 89 08                        mov qword ptr [rax], rcx
00BEA3B9  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
00BEA3C0  48 89 30                        mov qword ptr [rax], rsi
00BEA3C3  48 8B 83 C8 04 00 00            mov rax, qword ptr [rbx + 0x4c8]
00BEA3CA  48 89 30                        mov qword ptr [rax], rsi
00BEA3CD  48 8B 83 D0 04 00 00            mov rax, qword ptr [rbx + 0x4d0]
00BEA3D4  48 89 30                        mov qword ptr [rax], rsi
00BEA3D7  33 D2                           xor edx, edx
00BEA3D9  49 8B CC                        mov rcx, r12
00BEA3DC  E8 03 08 00 00                  call 0x140beabe4
00BEA3E1  48 8B 87 28 14 00 00            mov rax, qword ptr [rdi + 0x1428]
00BEA3E8  48 8B 8F 20 14 00 00            mov rcx, qword ptr [rdi + 0x1420]
00BEA3EF  48 89 08                        mov qword ptr [rax], rcx
00BEA3F2  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00BEA3FA  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00BEA402  48 89 08                        mov qword ptr [rax], rcx
00BEA405  0F 20 E1                        mov rcx, cr4
00BEA408  48 F7 C1 80 00 02 00            test rcx, 0x20080
00BEA40F  74 10                           je 0x140bea421
00BEA411  48 8B C1                        mov rax, rcx
00BEA414  48 0F BA F8 07                  btc rax, 7
00BEA419  0F 22 E0                        mov cr4, rax
00BEA41C  0F 22 E1                        mov cr4, rcx
00BEA41F  EB 06                           jmp 0x140bea427
00BEA421  0F 20 D8                        mov rax, cr3
00BEA424  0F 22 D8                        mov cr3, rax
00BEA427  44 8B BF 30 14 00 00            mov r15d, dword ptr [rdi + 0x1430]
00BEA42E  33 D2                           xor edx, edx
00BEA430  49 8B CC                        mov rcx, r12
00BEA433  E8 AC 07 00 00                  call 0x140beabe4
00BEA438  84 C0                           test al, al
00BEA43A  0F 84 DA 00 00 00               je 0x140bea51a
00BEA440  48 89 B7 00 14 00 00            mov qword ptr [rdi + 0x1400], rsi
00BEA447  48 8D 87 00 04 00 00            lea rax, [rdi + 0x400]
00BEA44E  48 89 B7 08 14 00 00            mov qword ptr [rdi + 0x1408], rsi
00BEA455  B9 00 10 00 00                  mov ecx, 0x1000
00BEA45A  48 89 B7 10 14 00 00            mov qword ptr [rdi + 0x1410], rsi
00BEA461  BA 00 02 00 00                  mov edx, 0x200
00BEA466  48 89 B7 20 14 00 00            mov qword ptr [rdi + 0x1420], rsi
00BEA46D  48 89 B7 28 14 00 00            mov qword ptr [rdi + 0x1428], rsi
00BEA474  48 89 B7 30 14 00 00            mov qword ptr [rdi + 0x1430], rsi
00BEA47B  48 89 30                        mov qword ptr [rax], rsi
00BEA47E  41 03 CD                        add ecx, r13d
00BEA481  48 83 C0 08                     add rax, 8
00BEA485  49 2B D6                        sub rdx, r14
00BEA488  75 F1                           jne 0x140bea47b
00BEA48A  41 83 CA FF                     or r10d, 0xffffffff
00BEA48E  85 C9                           test ecx, ecx
00BEA490  74 0B                           je 0x140bea49d
00BEA492  40 88 30                        mov byte ptr [rax], sil
00BEA495  49 03 C6                        add rax, r14
00BEA498  41 03 CA                        add ecx, r10d
00BEA49B  75 F5                           jne 0x140bea492
00BEA49D  41 B8 10 00 00 00               mov r8d, 0x10
00BEA4A3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00BEA4A8  48 8D 57 20                     lea rdx, [rdi + 0x20]
00BEA4AC  45 8D 58 F2                     lea r11d, [r8 - 0xe]
00BEA4B0  45 8B CB                        mov r9d, r11d
00BEA4B3  48 8B 01                        mov rax, qword ptr [rcx]
00BEA4B6  45 03 C5                        add r8d, r13d
00BEA4B9  48 89 02                        mov qword ptr [rdx], rax
00BEA4BC  48 83 C1 08                     add rcx, 8
00BEA4C0  48 83 C2 08                     add rdx, 8
00BEA4C4  4D 2B CE                        sub r9, r14
00BEA4C7  75 EA                           jne 0x140bea4b3
00BEA4C9  45 85 C0                        test r8d, r8d
00BEA4CC  74 0F                           je 0x140bea4dd
00BEA4CE  8A 01                           mov al, byte ptr [rcx]
00BEA4D0  49 03 CE                        add rcx, r14
00BEA4D3  88 02                           mov byte ptr [rdx], al
00BEA4D5  49 03 D6                        add rdx, r14
00BEA4D8  45 03 C2                        add r8d, r10d
00BEA4DB  75 F1                           jne 0x140bea4ce
00BEA4DD  BA 10 00 00 00                  mov edx, 0x10
00BEA4E2  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00BEA4E7  48 81 C7 20 01 00 00            add rdi, 0x120
00BEA4EE  4D 8B C3                        mov r8, r11
00BEA4F1  48 8B 01                        mov rax, qword ptr [rcx]
00BEA4F4  41 03 D5                        add edx, r13d
00BEA4F7  48 89 07                        mov qword ptr [rdi], rax
00BEA4FA  48 83 C1 08                     add rcx, 8
00BEA4FE  48 83 C7 08                     add rdi, 8
00BEA502  4D 2B C6                        sub r8, r14
00BEA505  75 EA                           jne 0x140bea4f1
00BEA507  85 D2                           test edx, edx
00BEA509  74 0F                           je 0x140bea51a
00BEA50B  8A 01                           mov al, byte ptr [rcx]
00BEA50D  49 03 CE                        add rcx, r14
00BEA510  88 07                           mov byte ptr [rdi], al
00BEA512  49 03 FE                        add rdi, r14
00BEA515  41 03 D2                        add edx, r10d
00BEA518  75 F1                           jne 0x140bea50b
00BEA51A  33 D2                           xor edx, edx
00BEA51C  49 8B CC                        mov rcx, r12
00BEA51F  E8 C0 06 00 00                  call 0x140beabe4
00BEA524  41 BB 02 00 00 00               mov r11d, 2
00BEA52A  41 F6 C7 08                     test r15b, 8
00BEA52E  0F 85 2F FA FF FF               jne 0x140be9f63
00BEA534  FB                              sti
00BEA535  48 8B C3                        mov rax, rbx
00BEA538  48 83 C4 60                     add rsp, 0x60
00BEA53C  41 5F                           pop r15
00BEA53E  41 5E                           pop r14
00BEA540  41 5D                           pop r13
00BEA542  41 5C                           pop r12
00BEA544  5F                              pop rdi
00BEA545  5E                              pop rsi
00BEA546  5B                              pop rbx
00BEA547  C3                              ret
00BEA548  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BE9DF0(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (96);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 2728))) == 44) goto loc_00BE9F3B;
    v_rsi = 0;
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_00BEA535;
    *(unsigned __int64 *)(a1 + 2352) = 257;
    result = (result) + (a1);
    *(unsigned __int64 *)(a1 + 2360) = 0;
    *(unsigned __int64 *)(a1 + 2336) = result;
    *(unsigned int *)(a1 + 2328) = (unsigned int)(v_rsi + 1);
    result = (result) + (*(unsigned __int64 *)(a1 + 2728));
    *(unsigned __int64 *)(a1 + 2344) = result;
    if (condition_is_below) goto loc_00BEA535;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BEA535;
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_00BEA535;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE9EDC;
loc_00BE9EBB:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1)) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_00BE9EDC:
    if (a2 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_00BE9EBB;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_00BEA535;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1416)) = a1;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2052)));
    result = *(unsigned __int64 *)(a1 + 1416);
    if ((*(unsigned int *)(a1 + 2328)) == 0) {
        result = *(unsigned __int64 *)(a1 + 1416);
        a1 = (*(unsigned __int64 *)(a1 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(a1, a2, a3, 256);
    goto loc_00BEA535;
loc_00BE9F3B:
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, 256);
    v_rsi = 0;
    v_stack_p8 = *(unsigned __int64 *)(a1 + 2736);
loc_00BE9F63:
loc_00BE9F90:
    a3 = (unsigned int)((16) + (-8));
    *(unsigned __int64 *)(v_stack_m78) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 32);
    a1 = (*(unsigned __int64 *)(a1 + 2272) + 32) + (8);
    a2 = (v_stack_m78) + (8);
    a4 = (v_rsi + 2) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BE9F90;
    if ((unsigned int)(a3) == 0) goto loc_00BE9FBC;
loc_00BE9FAC:
    a1 = (a1) + (v_rsi + 1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a2 = (a2) + (v_rsi + 1);
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE9FAC;
loc_00BE9FBC:
loc_00BE9FD4:
    a3 = (unsigned int)((16) + (-8));
    *(unsigned __int64 *)(v_stack_m68) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 288);
    a1 = (*(unsigned __int64 *)(a1 + 2272) + 288) + (8);
    a2 = (v_stack_m68) + (8);
    a4 = (v_rsi + 2) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BE9FD4;
    if ((unsigned int)(a3) == 0) goto loc_00BEA000;
loc_00BE9FF0:
    a1 = (a1) + (v_rsi + 1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a2 = (a2) + (v_rsi + 1);
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE9FF0;
loc_00BEA000:
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 56)) >> (9);
    a2 = 0;
    v_r10 = (v_r10) & (a1);
    v_r10 = (v_r10) + (*(unsigned __int64 *)(a1 + 1496));
    v_stack_p10 = v_r10;
    v_stack_p18 = *(unsigned __int64 *)(v_r10);
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00BEA188;
    result = (a1 + 16) + ((unsigned int)(*(unsigned int *)(a1 + 2324)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 2272) + 32) = (unsigned __int16)(result);
    a1 = (result) >> (16);
    result = (result) >> (32);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 2272) + 40) = (unsigned int)(result);
    result = (a1 + 144) + ((unsigned int)(*(unsigned int *)(a1 + 2324)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 2272) + 38) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 2272) + 288) = (unsigned __int16)(result);
    a1 = (result) >> (16);
    result = (result) >> (32);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 2272) + 294) = (unsigned __int16)(a1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 2272) + 296) = (unsigned int)(result);
loc_00BEA0AB:
    a3 = (unsigned int)(((unsigned int)(0x1000ULL)) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 1024) = *(unsigned __int64 *)(v_stack_p8);
    a1 = (v_stack_p8) + (8);
    a2 = (*(unsigned __int64 *)(a1 + 2272) + 1024) + (8);
    a4 = (512) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA0AB;
    v_r11 = (unsigned int)((v_rsi + 2) | (0xFFFFFFFFULL));
    if ((unsigned int)(a3) == 0) goto loc_00BEA0D9;
loc_00BEA0CA:
    a1 = (a1) + (v_rsi + 1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a2 = (a2) + (v_rsi + 1);
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r11)));
    if (condition_is_not_equal) goto loc_00BEA0CA;
loc_00BEA0D9:
    *(unsigned int *)(a1 + 2238) = 0xF0C0894CULL;
    *(unsigned int *)(a1 + 2242) = 0x11B10F48ULL;
    *(unsigned int *)(a1 + 2246) = 0xC3C0940FULL;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5128) = v_stack_p8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5136) = v_stack_p8;
    result = (v_stack_p8) >> (9);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5120) = a1;
    result = (result) & (v_stack_p8);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 2272) + 5172) = (unsigned int)(v_r11);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 2272) + 5168) = 4;
    result = (result) + (*(unsigned __int64 *)(a1 + 1496));
loc_00BEA146:
    *(unsigned __int64 *)(v_stack_m58) = result;
    result = (result) >> (9);
    result = (result) & (v_stack_p8);
    result = (result) + (*(unsigned __int64 *)(a1 + 1496));
    a2 = (4) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA146;
loc_00BEA15C:
    a3 = (unsigned int)((4) + ((unsigned int)(v_r11)));
    if (condition_is_equal) goto loc_00BEA170;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp + a3 * 8 + 64)))) >> (7));
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)(a1))) == 0) goto loc_00BEA15C;
loc_00BEA170:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5160) = *(unsigned __int64 *)(v_rsp + a3 * 8 + 64);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5152) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + a3 * 8 + 64));
    goto loc_00BEA18E;
loc_00BEA188:
loc_00BEA18E:
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, *(unsigned __int64 *)(a1 + 1496));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5144)) << (12);
    result = (v_stack_p18) ^ (a1);
    result = (result) & (0);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_stack_p10) = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5152)) | (66);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5160)) = result;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BEA201;
    goto loc_00BEA207;
loc_00BEA201:
loc_00BEA207:
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, *(unsigned __int64 *)(a1 + 1496));
    if ((unsigned __int8)(result) != 0) {
    }
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, *(unsigned __int64 *)(a1 + 1496));
    if ((unsigned __int8)(result) == 0) goto loc_00BEA3D7;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 2272) + 5172) = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
loc_00BEA24A:
    result = (unsigned int)(*(unsigned int *)(gs_base + (0 + 420)));
    if (((*(unsigned int *)(a1 + 2524)) & (0x20000ULL)) == 0) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = *(unsigned __int64 *)(a1 + 1208);
        a1 = (a1 + 2696) + (a1);
        *(unsigned __int64 *)(result) = a1;
        a1 = 0 + v_stack_p8 * 1;
        result = *(unsigned __int64 *)(a1 + 1216);
        *(unsigned __int64 *)(result) = a2;
        result = *(unsigned __int64 *)(a1 + 1224);
        *(unsigned __int64 *)(result) = a1;
        result = *(unsigned __int64 *)(a1 + 1232);
        *(unsigned __int64 *)(result) = 276;
    }
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5136) = 0 + v_stack_p8 * 1;
    if (condition_is_not_equal) goto loc_00BEA32D;
    if (((0) & (7)) != 0) goto loc_00BEA2F2;
    result = KeGuardDispatchICall(0 + v_stack_p8 * 1, result + 2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 1024), *(unsigned __int64 *)(a1 + 2272) + 5136);
    if ((unsigned __int8)(result) == 0) goto loc_00BEA31D;
loc_00BEA2F2:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(a1 + 2272) + 5136, result + 2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 1024), *(unsigned __int64 *)(a1 + 2272) + 5136);
    v_r12 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    v_r13 = (*(unsigned __int64 *)(a1 + 2272) + 1024) + (v_rsi + 1);
    if (((unsigned int)(v_r12)) >= 0x1000ULL) goto loc_00BEA325;
    goto loc_00BEA24A;
loc_00BEA31D:
loc_00BEA325:
loc_00BEA32D:
    if (((unsigned int)(v_r12)) != ((unsigned int)((unsigned int)(0x1000ULL)))) {
        result = v_stack_p8 + 4095;
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5136) = result;
    }
loc_00BEA360:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(v_stack_p8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 1024);
    v_r15 = (*(unsigned __int64 *)(a1 + 2272) + 1024) + (8);
    a1 = (v_stack_p8) + (8);
    a3 = (512) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA360;
    if ((unsigned int)(a2) == 0) goto loc_00BEA38A;
loc_00BEA37A:
    v_r15 = (v_r15) + (v_rsi + 1);
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_r15));
    a1 = (a1) + (v_rsi + 1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BEA37A;
loc_00BEA38A:
    result = *(unsigned __int8 *)(v_r15);
    if (((*(unsigned int *)(a1 + 2524)) & (0x20000ULL)) == 0) {
        result = *(unsigned __int64 *)(a1 + 1208);
        *(unsigned __int64 *)(result) = a1;
        result = *(unsigned __int64 *)(a1 + 1216);
        *(unsigned __int64 *)(result) = 0;
        result = *(unsigned __int64 *)(a1 + 1224);
        *(unsigned __int64 *)(result) = 0;
        result = *(unsigned __int64 *)(a1 + 1232);
        *(unsigned __int64 *)(result) = 0;
    }
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, *(unsigned __int64 *)(a1 + 2272) + 5136);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5160)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5152);
    *(unsigned __int64 *)(v_stack_p10) = v_stack_p18;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BEA421;
    goto loc_00BEA427;
loc_00BEA421:
loc_00BEA427:
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, *(unsigned __int64 *)(a1 + 2272) + 5136);
    if ((unsigned __int8)(result) == 0) goto loc_00BEA51A;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5120) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5128) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5136) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5152) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5160) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 5168) = 0;
loc_00BEA47B:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 1024) = 0;
    a1 = (unsigned int)(((unsigned int)(0x1000ULL)) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (*(unsigned __int64 *)(a1 + 2272) + 1024) + (8);
    a2 = (512) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA47B;
    v_r10 = (unsigned int)((a1 + 2238) | (0xFFFFFFFFULL));
    if ((unsigned int)(a1) == 0) goto loc_00BEA49D;
loc_00BEA492:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (v_rsi + 1);
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BEA492;
loc_00BEA49D:
loc_00BEA4B3:
    a3 = (unsigned int)((16) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2272) + 32) = *(unsigned __int64 *)(v_stack_m78);
    a1 = (v_stack_m78) + (8);
    a2 = (*(unsigned __int64 *)(a1 + 2272) + 32) + (8);
    a4 = ((unsigned int)((unsigned int)(16 - 14))) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA4B3;
    if ((unsigned int)(a3) == 0) goto loc_00BEA4DD;
loc_00BEA4CE:
    a1 = (a1) + (v_rsi + 1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a2 = (a2) + (v_rsi + 1);
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BEA4CE;
loc_00BEA4DD:
    v_rdi = (*(unsigned __int64 *)(a1 + 2272)) + (288);
loc_00BEA4F1:
    a2 = (unsigned int)((16) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_stack_m68);
    a1 = (v_stack_m68) + (8);
    v_rdi = (v_rdi) + (8);
    a3 = (16 - 14) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA4F1;
    if ((unsigned int)(a2) == 0) goto loc_00BEA51A;
loc_00BEA50B:
    a1 = (a1) + (v_rsi + 1);
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    v_rdi = (v_rdi) + (v_rsi + 1);
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_00BEA50B;
loc_00BEA51A:
    a2 = 0;
    result = RtlMinimalBarrier(a1 + 2696, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 2272) + 5168)))) & (8)) != 0) goto loc_00BE9F63;
loc_00BEA535:
    v_rsp = (v_rsp) + (96);
    return a1;
}
```

## 5. (Beta) C Style

```c
void *sub_00BE9DF0(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (96);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xAA8))) == 44) goto loc_00BE9F3B;
    local_rsi = 0;
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_00BEA535;
    *(uint64_t *)(arg1 + 0x930) = 257;
    result = (result) + (Arg1);
    *(uint64_t *)(arg1 + 0x938) = 0;
    *(uint64_t *)(arg1 + 0x920) = result;
    *(uint32_t *)(arg1 + 0x918) = (uint32_t)(local_rsi + 1);
    result = (result) + (*(uint64_t *)(arg1 + 0xAA8));
    *(uint64_t *)(arg1 + 0x928) = result;
    if (condition_is_below) goto loc_00BEA535;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BEA535;
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_00BEA535;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE9EDC;
loc_00BE9EBB:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1)) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_00BE9EDC:
    if (a2 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_00BE9EBB;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_00BEA535;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    a2 = 0;
    result = sub_00BE8384(Arg1, a2, a3, 256);
    goto loc_00BEA535;
loc_00BE9F3B:
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, 256);
    local_rsi = 0;
    v_stack_p8 = *(uint64_t *)(arg1 + 0xAB0);
loc_00BE9F63:
loc_00BE9F90:
    a3 = (uint32_t)((16) + (-8));
    *(uint64_t *)(v_stack_m78) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x20);
    Arg1 = (*(uint64_t *)(arg1 + 0x8E0) + 32) + (8);
    a2 = (v_stack_m78) + (8);
    a4 = (local_rsi + 2) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BE9F90;
    if ((uint32_t)(a3) == 0) goto loc_00BE9FBC;
loc_00BE9FAC:
    Arg1 = (Arg1) + (local_rsi + 1);
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(arg1));
    a2 = (a2) + (local_rsi + 1);
    a3 = (uint32_t)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE9FAC;
loc_00BE9FBC:
loc_00BE9FD4:
    a3 = (uint32_t)((16) + (-8));
    *(uint64_t *)(v_stack_m68) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x120);
    Arg1 = (*(uint64_t *)(arg1 + 0x8E0) + 288) + (8);
    a2 = (v_stack_m68) + (8);
    a4 = (local_rsi + 2) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BE9FD4;
    if ((uint32_t)(a3) == 0) goto loc_00BEA000;
loc_00BE9FF0:
    Arg1 = (Arg1) + (local_rsi + 1);
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(arg1));
    a2 = (a2) + (local_rsi + 1);
    a3 = (uint32_t)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE9FF0;
loc_00BEA000:
    local_r10 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x38)) >> (9);
    a2 = 0;
    local_r10 = (local_r10) & (Arg1);
    local_r10 = (local_r10) + (*(uint64_t *)(arg1 + 0x5D8));
    v_stack_p10 = local_r10;
    v_stack_p18 = *(uint64_t *)(local_r10);
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00BEA188;
    result = (Arg1 + 16) + ((uint32_t)(*(uint32_t *)(arg1 + 0x914)));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x20) = (uint16_t)(result);
    Arg1 = (result) >> (16);
    result = (result) >> (32);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x28) = (uint32_t)(result);
    result = (Arg1 + 144) + ((uint32_t)(*(uint32_t *)(arg1 + 0x914)));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x26) = (uint16_t)(Arg1);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x120) = (uint16_t)(result);
    Arg1 = (result) >> (16);
    result = (result) >> (32);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x126) = (uint16_t)(Arg1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x128) = (uint32_t)(result);
loc_00BEA0AB:
    a3 = (uint32_t)(((uint32_t)(0x1000ULL)) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x400) = *(uint64_t *)(v_stack_p8);
    Arg1 = (v_stack_p8) + (8);
    a2 = (*(uint64_t *)(arg1 + 0x8E0) + 1024) + (8);
    a4 = (512) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA0AB;
    local_r11 = (uint32_t)((local_rsi + 2) | (0xFFFFFFFFULL));
    if ((uint32_t)(a3) == 0) goto loc_00BEA0D9;
loc_00BEA0CA:
    Arg1 = (Arg1) + (local_rsi + 1);
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(arg1));
    a2 = (a2) + (local_rsi + 1);
    a3 = (uint32_t)((a3) + ((uint32_t)(local_r11)));
    if (condition_is_not_equal) goto loc_00BEA0CA;
loc_00BEA0D9:
    *(uint32_t *)(arg1 + 0x8BE) = 0xF0C0894CULL;
    *(uint32_t *)(arg1 + 0x8C2) = 0x11B10F48ULL;
    *(uint32_t *)(arg1 + 0x8C6) = 0xC3C0940FULL;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1408) = v_stack_p8;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1410) = v_stack_p8;
    result = (v_stack_p8) >> (9);
    *(void **)(*(uint64_t *)(arg1 + 0x8E0) + 0x1400) = Arg1;
    result = (result) & (v_stack_p8);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1434) = (uint32_t)(local_r11);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1430) = 4;
    result = (result) + (*(uint64_t *)(arg1 + 0x5D8));
loc_00BEA146:
    *(uint64_t *)(v_stack_m58) = result;
    result = (result) >> (9);
    result = (result) & (v_stack_p8);
    result = (result) + (*(uint64_t *)(arg1 + 0x5D8));
    a2 = (4) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA146;
loc_00BEA15C:
    a3 = (uint32_t)((4) + ((uint32_t)(local_r11)));
    if (condition_is_equal) goto loc_00BEA170;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp + a3 * 8 + 0x40)))) >> (7));
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)(Arg1))) == 0) goto loc_00BEA15C;
loc_00BEA170:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1428) = *(uint64_t *)(local_rsp + a3 * 8 + 0x40);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1420) = *(uint64_t *)(*(uint64_t *)(local_rsp + a3 * 8 + 0x40));
    goto loc_00BEA18E;
loc_00BEA188:
loc_00BEA18E:
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, *(uint64_t *)(arg1 + 0x5D8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1418)) << (12);
    result = (v_stack_p18) ^ (Arg1);
    result = (result) & (0);
    result = (result) ^ (Arg1);
    *(uint64_t *)(v_stack_p10) = result;
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1420)) | (66);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1428)) = result;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BEA201;
    goto loc_00BEA207;
loc_00BEA201:
loc_00BEA207:
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, *(uint64_t *)(arg1 + 0x5D8));
    if ((uint8_t)(result) != 0) {
    }
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, *(uint64_t *)(arg1 + 0x5D8));
    if ((uint8_t)(result) == 0) goto loc_00BEA3D7;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1434) = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
loc_00BEA24A:
    result = (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)));
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x20000ULL)) == 0) {
        a2 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = *(uint64_t *)(arg1 + 0x4B8);
        Arg1 = (Arg1 + 2696) + (Arg1);
        *(void **)(result) = Arg1;
        Arg1 = 0 + v_stack_p8 * 1;
        result = *(uint64_t *)(arg1 + 0x4C0);
        *(uint64_t *)(result) = a2;
        result = *(uint64_t *)(arg1 + 0x4C8);
        *(void **)(result) = Arg1;
        result = *(uint64_t *)(arg1 + 0x4D0);
        *(uint64_t *)(result) = 276;
    }
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1410) = 0 + v_stack_p8 * 1;
    if (condition_is_not_equal) goto loc_00BEA32D;
    if (((0) & (7)) != 0) goto loc_00BEA2F2;
    result = KeGuardDispatchICall(0 + v_stack_p8 * 1, result + 2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x400), *(uint64_t *)(arg1 + 0x8E0) + 5136);
    if ((uint8_t)(result) == 0) goto loc_00BEA31D;
loc_00BEA2F2:
    result = KeGuardDispatchICall(*(uint64_t *)(arg1 + 0x8E0) + 5136, result + 2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x400), *(uint64_t *)(arg1 + 0x8E0) + 5136);
    local_r12 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    local_r13 = (*(uint64_t *)(arg1 + 0x8E0) + 1024) + (local_rsi + 1);
    if (((uint32_t)(local_r12)) >= 0x1000ULL) goto loc_00BEA325;
    goto loc_00BEA24A;
loc_00BEA31D:
loc_00BEA325:
loc_00BEA32D:
    if (((uint32_t)(local_r12)) != ((uint32_t)((uint32_t)(0x1000ULL)))) {
        result = v_stack_p8 + 4095;
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1410) = result;
    }
loc_00BEA360:
    a2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(v_stack_p8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x400);
    local_r15 = (*(uint64_t *)(arg1 + 0x8E0) + 1024) + (8);
    Arg1 = (v_stack_p8) + (8);
    a3 = (512) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA360;
    if ((uint32_t)(a2) == 0) goto loc_00BEA38A;
loc_00BEA37A:
    local_r15 = (local_r15) + (local_rsi + 1);
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(local_r15));
    Arg1 = (Arg1) + (local_rsi + 1);
    a2 = (uint32_t)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BEA37A;
loc_00BEA38A:
    result = *(uint8_t *)(local_r15);
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x20000ULL)) == 0) {
        result = *(uint64_t *)(arg1 + 0x4B8);
        *(void **)(result) = Arg1;
        result = *(uint64_t *)(arg1 + 0x4C0);
        *(uint64_t *)(result) = 0;
        result = *(uint64_t *)(arg1 + 0x4C8);
        *(uint64_t *)(result) = 0;
        result = *(uint64_t *)(arg1 + 0x4D0);
        *(uint64_t *)(result) = 0;
    }
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, *(uint64_t *)(arg1 + 0x8E0) + 5136);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1428)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1420);
    *(uint64_t *)(v_stack_p10) = v_stack_p18;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BEA421;
    goto loc_00BEA427;
loc_00BEA421:
loc_00BEA427:
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, *(uint64_t *)(arg1 + 0x8E0) + 5136);
    if ((uint8_t)(result) == 0) goto loc_00BEA51A;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1400) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1408) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1410) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1420) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1428) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1430) = 0;
loc_00BEA47B:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x400) = 0;
    Arg1 = (uint32_t)(((uint32_t)(0x1000ULL)) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (*(uint64_t *)(arg1 + 0x8E0) + 1024) + (8);
    a2 = (512) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA47B;
    local_r10 = (uint32_t)((Arg1 + 2238) | (0xFFFFFFFFULL));
    if ((uint32_t)(Arg1) == 0) goto loc_00BEA49D;
loc_00BEA492:
    *(uint8_t *)(result) = 0;
    result = (result) + (local_rsi + 1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BEA492;
loc_00BEA49D:
loc_00BEA4B3:
    a3 = (uint32_t)((16) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x20) = *(uint64_t *)(v_stack_m78);
    Arg1 = (v_stack_m78) + (8);
    a2 = (*(uint64_t *)(arg1 + 0x8E0) + 32) + (8);
    a4 = ((uint32_t)((uint32_t)(16 - 14))) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA4B3;
    if ((uint32_t)(a3) == 0) goto loc_00BEA4DD;
loc_00BEA4CE:
    Arg1 = (Arg1) + (local_rsi + 1);
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(arg1));
    a2 = (a2) + (local_rsi + 1);
    a3 = (uint32_t)((a3) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BEA4CE;
loc_00BEA4DD:
    local_rdi = (*(uint64_t *)(arg1 + 0x8E0)) + (288);
loc_00BEA4F1:
    a2 = (uint32_t)((16) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(local_rdi) = *(uint64_t *)(v_stack_m68);
    Arg1 = (v_stack_m68) + (8);
    local_rdi = (local_rdi) + (8);
    a3 = (16 - 14) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00BEA4F1;
    if ((uint32_t)(a2) == 0) goto loc_00BEA51A;
loc_00BEA50B:
    Arg1 = (Arg1) + (local_rsi + 1);
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(arg1));
    local_rdi = (local_rdi) + (local_rsi + 1);
    a2 = (uint32_t)((a2) + ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_00BEA50B;
loc_00BEA51A:
    a2 = 0;
    result = RtlMinimalBarrier(Arg1 + 2696, a2, a3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8E0) + 0x1430)))) & (8)) != 0) goto loc_00BE9F63;
loc_00BEA535:
    local_rsp = (local_rsp) + (96);
    return Arg1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0x4B8` | `64` | `R` |
| `Arg1` | `+ 0x4C0` | `64` | `R` |
| `Arg1` | `+ 0x4C8` | `64` | `R` |
| `Arg1` | `+ 0x4D0` | `64` | `R` |
| `Arg1` | `+ 0x588` | `64` | `R` |
| `Arg1` | `+ 0x5D8` | `64` | `R` |
| `Arg1` | `+ 0x804` | `32` | `R` |
| `Arg1` | `+ 0x838` | `64` | `R` |
| `Arg1` | `+ 0x8B3` | `64` | `R` |
| `Arg1` | `+ 0x8BE` | `32` | `W` |
| `Arg1` | `+ 0x8BE` | `64` | `R` |
| `Arg1` | `+ 0x8C2` | `32` | `W` |
| `Arg1` | `+ 0x8C6` | `32` | `W` |
| `Arg1` | `+ 0x8E0` | `64` | `R` |
| `Arg1` | `+ 0x914` | `32` | `R` |
| `Arg1` | `+ 0x918` | `32` | `R` |
| `Arg1` | `+ 0x918` | `32` | `W` |
| `Arg1` | `+ 0x920` | `64` | `W` |
| `Arg1` | `+ 0x928` | `64` | `W` |
| `Arg1` | `+ 0x930` | `64` | `W` |
| `Arg1` | `+ 0x938` | `64` | `W` |
| `Arg1` | `+ 0x9D8` | `32` | `R` |
| `Arg1` | `+ 0x9DC` | `32` | `R` |
| `Arg1` | `+ 0x9DC` | `32` | `R/W` |
| `Arg1` | `+ 0xA74` | `32` | `R` |
| `Arg1` | `+ 0xA78` | `64` | `R` |
| `Arg1` | `+ 0xA80` | `64` | `R` |
| `Arg1` | `+ 0xA88` | `64` | `R` |
| `Arg1` | `+ 0xAA8` | `64` | `R` |
| `Arg1` | `+ 0xAB0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=initkdbg&rva=0x00BE9DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
