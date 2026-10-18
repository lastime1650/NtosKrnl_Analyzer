# PpmSnapPerformanceAccumulation

- RVA: `0x002DE090`–`0x002DE578` (길이 `1,256` bytes)
- VA: `0x00000001402DE090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070988`
- 디코드: `307`개 명령, `1,256/1,256` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002DE0FB` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x002DE23E` → [PpmUpdatePerformanceFeedback](PpmUpdatePerformanceFeedback_function_002DE580.md) (function, `0x002DE580`)
- `0x002DE268` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002DE369` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x002DE3D1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002DE438` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002DE52B` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)

### Direct callers
- [PpmPerfSnapDeliveredPerformance](PpmPerfSnapDeliveredPerformance_function_002D7F30.md) at `0x002D7FAF`
- [PpmGetThroughputInfoCallback](PpmGetThroughputInfoCallback_function_002DDC70.md) at `0x002DDCC8`
- [PpmResetPerfTimes](../44/PpmResetPerfTimes_function_0044F8EC.md) at `0x0044F943`
- [PpmCapturePerformanceDistributionCallback](../48/PpmCapturePerformanceDistributionCallback_function_00489F30.md) at `0x00489FDA`

### Static image references
- `0x002DE0A4` → RVA `0x00E0A740` (`.data`; read)
- `0x002DE252` → RVA `0x00F0EFE0` (`.data`; read)
- `0x002DE328` → RVA `0x00E3EDD8` (`.data`; read)
- `0x002DE498` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DE090  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
002DE095  55                              push rbp
002DE096  56                              push rsi
002DE097  57                              push rdi
002DE098  41 54                           push r12
002DE09A  41 55                           push r13
002DE09C  41 56                           push r14
002DE09E  41 57                           push r15
002DE0A0  48 83 EC 70                     sub rsp, 0x70
002DE0A4  48 8B 05 95 C6 B2 00            mov rax, qword ptr [rip + 0xb2c695]
002DE0AB  48 33 C4                        xor rax, rsp
002DE0AE  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002DE0B3  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
002DE0BB  33 FF                           xor edi, edi
002DE0BD  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
002DE0C5  33 C0                           xor eax, eax
002DE0C7  44 88 4C 24 31                  mov byte ptr [rsp + 0x31], r9b
002DE0CC  0F 57 C0                        xorps xmm0, xmm0
002DE0CF  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
002DE0D3  45 0F B6 E8                     movzx r13d, r8b
002DE0D7  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002DE0DC  0F B6 EA                        movzx ebp, dl
002DE0DF  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
002DE0E4  48 8B D9                        mov rbx, rcx
002DE0E7  44 8B FF                        mov r15d, edi
002DE0EA  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
002DE0EF  45 84 C0                        test r8b, r8b
002DE0F2  0F 85 6F 02 00 00               jne 0x1402de367
002DE0F8  FA                              cli
002DE0F9  33 C9                           xor ecx, ecx
002DE0FB  E8 E0 06 0A 00                  call 0x14037e7e0
002DE100  4C 8B E0                        mov r12, rax
002DE103  0F 31                           rdtsc
002DE105  48 C1 E2 20                     shl rdx, 0x20
002DE109  49 BB 00 00 00 00 80 00 00 00   movabs r11, 0x8000000000
002DE113  48 0B C2                        or rax, rdx
002DE116  4C 8B C0                        mov r8, rax
002DE119  4C 85 9B A0 8F 00 00            test qword ptr [rbx + 0x8fa0], r11
002DE120  0F 85 C9 02 00 00               jne 0x1402de3ef
002DE126  44 8B CF                        mov r9d, edi
002DE129  4D 8B D4                        mov r10, r12
002DE12C  4C 2B 93 B8 88 00 00            sub r10, qword ptr [rbx + 0x88b8]
002DE133  F0 4C 01 93 C8 88 00 00         lock add qword ptr [rbx + 0x88c8], r10
002DE13B  4C 85 9B A0 8F 00 00            test qword ptr [rbx + 0x8fa0], r11
002DE142  74 5C                           je 0x1402de1a0
002DE144  4D 8B D9                        mov r11, r9
002DE147  49 8B C8                        mov rcx, r8
002DE14A  4C 2B 9B 08 89 00 00            sub r11, qword ptr [rbx + 0x8908]
002DE151  48 2B 8B 98 88 00 00            sub rcx, qword ptr [rbx + 0x8898]
002DE158  4D 85 D2                        test r10, r10
002DE15B  0F 84 79 03 00 00               je 0x1402de4da
002DE161  48 85 C9                        test rcx, rcx
002DE164  0F 84 70 03 00 00               je 0x1402de4da
002DE16A  49 3B CB                        cmp rcx, r11
002DE16D  0F 84 67 03 00 00               je 0x1402de4da
002DE173  49 8B C3                        mov rax, r11
002DE176  49 F7 E2                        mul r10
002DE179  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
002DE17E  48 85 D2                        test rdx, rdx
002DE181  0F 85 B5 03 00 00               jne 0x1402de53c
002DE187  48 F7 F1                        div rcx
002DE18A  48 8B F8                        mov rdi, rax
002DE18D  48 01 BB 10 89 00 00            add qword ptr [rbx + 0x8910], rdi
002DE194  49 BB 00 00 00 00 80 00 00 00   movabs r11, 0x8000000000
002DE19E  33 FF                           xor edi, edi
002DE1A0  48 8B 8B 98 88 00 00            mov rcx, qword ptr [rbx + 0x8898]
002DE1A7  4C 89 A3 B8 88 00 00            mov qword ptr [rbx + 0x88b8], r12
002DE1AE  4C 3B C1                        cmp r8, rcx
002DE1B1  76 0D                           jbe 0x1402de1c0
002DE1B3  49 8B C0                        mov rax, r8
002DE1B6  48 2B C1                        sub rax, rcx
002DE1B9  48 01 83 A0 88 00 00            add qword ptr [rbx + 0x88a0], rax
002DE1C0  4C 89 83 98 88 00 00            mov qword ptr [rbx + 0x8898], r8
002DE1C7  4C 85 9B A0 8F 00 00            test qword ptr [rbx + 0x8fa0], r11
002DE1CE  74 07                           je 0x1402de1d7
002DE1D0  4C 89 8B 08 89 00 00            mov qword ptr [rbx + 0x8908], r9
002DE1D7  0F 57 C0                        xorps xmm0, xmm0
002DE1DA  33 C0                           xor eax, eax
002DE1DC  41 0F 11 06                     movups xmmword ptr [r14], xmm0
002DE1E0  41 0F 11 46 10                  movups xmmword ptr [r14 + 0x10], xmm0
002DE1E5  41 0F 11 46 20                  movups xmmword ptr [r14 + 0x20], xmm0
002DE1EA  49 89 46 30                     mov qword ptr [r14 + 0x30], rax
002DE1EE  48 85 F6                        test rsi, rsi
002DE1F1  0F 85 30 02 00 00               jne 0x1402de427
002DE1F7  45 84 ED                        test r13b, r13b
002DE1FA  75 1A                           jne 0x1402de216
002DE1FC  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002DE205  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002DE20C  4D 85 C0                        test r8, r8
002DE20F  0F 85 F8 02 00 00               jne 0x1402de50d
002DE215  FB                              sti
002DE216  83 BB 20 89 00 00 03            cmp dword ptr [rbx + 0x8920], 3
002DE21D  48 8D 7C 24 48                  lea rdi, [rsp + 0x48]
002DE222  B8 00 00 00 00                  mov eax, 0
002DE227  45 0F B6 C5                     movzx r8d, r13b
002DE22B  48 0F 45 F8                     cmovne rdi, rax
002DE22F  40 0F B6 D5                     movzx edx, bpl
002DE233  45 33 C9                        xor r9d, r9d
002DE236  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002DE23B  48 8B CB                        mov rcx, rbx
002DE23E  E8 3D 03 00 00                  call 0x1402de580
002DE243  84 C0                           test al, al
002DE245  0F 84 7E 01 00 00               je 0x1402de3c9
002DE24B  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
002DE250  74 1B                           je 0x1402de26d
002DE252  48 8B 05 87 0D C3 00            mov rax, qword ptr [rip + 0xc30d87]
002DE259  48 85 C0                        test rax, rax
002DE25C  74 0F                           je 0x1402de26d
002DE25E  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
002DE261  41 B0 01                        mov r8b, 1
002DE264  41 0F B6 D5                     movzx edx, r13b
002DE268  E8 63 C8 3D 00                  call 0x1406baad0
002DE26D  48 85 FF                        test rdi, rdi
002DE270  0F 84 78 02 00 00               je 0x1402de4ee
002DE276  4C 8B 27                        mov r12, qword ptr [rdi]
002DE279  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
002DE27D  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
002DE281  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
002DE286  48 83 BB A8 88 00 00 00         cmp qword ptr [rbx + 0x88a8], 0
002DE28E  0F 85 4E 02 00 00               jne 0x1402de4e2
002DE294  48 83 BB B0 88 00 00 00         cmp qword ptr [rbx + 0x88b0], 0
002DE29C  0F 84 C4 02 00 00               je 0x1402de566
002DE2A2  48 8B 83 D8 88 00 00            mov rax, qword ptr [rbx + 0x88d8]
002DE2A9  48 8B D0                        mov rdx, rax
002DE2AC  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
002DE2B0  48 83 BB B0 88 00 00 00         cmp qword ptr [rbx + 0x88b0], 0
002DE2B8  49 8B D6                        mov rdx, r14
002DE2BB  B9 20 00 00 00                  mov ecx, 0x20
002DE2C0  74 07                           je 0x1402de2c9
002DE2C2  48 8B 83 D8 88 00 00            mov rax, qword ptr [rbx + 0x88d8]
002DE2C9  48 89 04 0A                     mov qword ptr [rdx + rcx], rax
002DE2CD  48 8B 83 E8 88 00 00            mov rax, qword ptr [rbx + 0x88e8]
002DE2D4  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
002DE2D8  48 8B 83 10 89 00 00            mov rax, qword ptr [rbx + 0x8910]
002DE2DF  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
002DE2E3  8B 83 5C 38 00 00               mov eax, dword ptr [rbx + 0x385c]
002DE2E9  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
002DE2ED  45 84 ED                        test r13b, r13b
002DE2F0  0F 84 0F 01 00 00               je 0x1402de405
002DE2F6  0F 0D 8B 60 88 00 00            prefetchw byte ptr [rbx + 0x8860]
002DE2FD  48 8B 83 60 88 00 00            mov rax, qword ptr [rbx + 0x8860]
002DE304  48 8B C8                        mov rcx, rax
002DE307  F0 48 0F B1 8B 60 88 00 00      lock cmpxchg qword ptr [rbx + 0x8860], rcx
002DE310  75 F2                           jne 0x1402de304
002DE312  A8 01                           test al, 1
002DE314  0F 84 1B 02 00 00               je 0x1402de535
002DE31A  48 85 C0                        test rax, rax
002DE31D  74 2C                           je 0x1402de34b
002DE31F  83 BB 20 89 00 00 03            cmp dword ptr [rbx + 0x8920], 3
002DE326  75 23                           jne 0x1402de34b
002DE328  8B 0D AA 0A B6 00               mov ecx, dword ptr [rip + 0xb60aaa]
002DE32E  48 8B 83 D0 8B 00 00            mov rax, qword ptr [rbx + 0x8bd0]
002DE335  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002DE339  B9 00 00 00 00                  mov ecx, 0
002DE33E  48 8B C2                        mov rax, rdx
002DE341  48 D1 E8                        shr rax, 1
002DE344  F6 C2 01                        test dl, 1
002DE347  48 0F 44 C1                     cmove rax, rcx
002DE34B  4C 3B F8                        cmp r15, rax
002DE34E  75 77                           jne 0x1402de3c7
002DE350  48 85 FF                        test rdi, rdi
002DE353  0F 85 B8 00 00 00               jne 0x1402de411
002DE359  49 8B C4                        mov rax, r12
002DE35C  49 2B C2                        sub rax, r10
002DE35F  4C 03 C0                        add r8, rax
002DE362  E9 AA 00 00 00                  jmp 0x1402de411
002DE367  33 C9                           xor ecx, ecx
002DE369  E8 72 04 0A 00                  call 0x14037e7e0
002DE36E  4C 8B E0                        mov r12, rax
002DE371  0F 0D 8B 60 88 00 00            prefetchw byte ptr [rbx + 0x8860]
002DE378  48 8B 83 60 88 00 00            mov rax, qword ptr [rbx + 0x8860]
002DE37F  48 8B C8                        mov rcx, rax
002DE382  F0 48 0F B1 8B 60 88 00 00      lock cmpxchg qword ptr [rbx + 0x8860], rcx
002DE38B  75 F2                           jne 0x1402de37f
002DE38D  4C 8B F8                        mov r15, rax
002DE390  A8 01                           test al, 1
002DE392  74 33                           je 0x1402de3c7
002DE394  48 85 C0                        test rax, rax
002DE397  74 25                           je 0x1402de3be
002DE399  83 BB 20 89 00 00 03            cmp dword ptr [rbx + 0x8920], 3
002DE3A0  75 1C                           jne 0x1402de3be
002DE3A2  8B 0D 30 0A B6 00               mov ecx, dword ptr [rip + 0xb60a30]
002DE3A8  48 8B 83 D0 8B 00 00            mov rax, qword ptr [rbx + 0x8bd0]
002DE3AF  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002DE3B3  4C 8B FA                        mov r15, rdx
002DE3B6  49 D1 EF                        shr r15, 1
002DE3B9  F6 C2 01                        test dl, 1
002DE3BC  74 09                           je 0x1402de3c7
002DE3BE  4D 85 FF                        test r15, r15
002DE3C1  0F 85 10 FE FF FF               jne 0x1402de1d7
002DE3C7  32 C0                           xor al, al
002DE3C9  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002DE3CE  48 33 CC                        xor rcx, rsp
002DE3D1  E8 6A E2 3C 00                  call 0x1406ac640
002DE3D6  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
002DE3DE  48 83 C4 70                     add rsp, 0x70
002DE3E2  41 5F                           pop r15
002DE3E4  41 5E                           pop r14
002DE3E6  41 5D                           pop r13
002DE3E8  41 5C                           pop r12
002DE3EA  5F                              pop rdi
002DE3EB  5E                              pop rsi
002DE3EC  5D                              pop rbp
002DE3ED  C3                              ret
002DE3EE  CC                              int3
002DE3EF  B9 B2 0D 00 00                  mov ecx, 0xdb2
002DE3F4  0F 32                           rdmsr
002DE3F6  48 C1 E2 20                     shl rdx, 0x20
002DE3FA  48 0B C2                        or rax, rdx
002DE3FD  4C 8B C8                        mov r9, rax
002DE400  E9 24 FD FF FF                  jmp 0x1402de129
002DE405  48 85 FF                        test rdi, rdi
002DE408  75 07                           jne 0x1402de411
002DE40A  4C 03 83 50 88 00 00            add r8, qword ptr [rbx + 0x8850]
002DE411  4D 89 26                        mov qword ptr [r14], r12
002DE414  4D 2B E0                        sub r12, r8
002DE417  4D 89 66 08                     mov qword ptr [r14 + 8], r12
002DE41B  48 85 F6                        test rsi, rsi
002DE41E  74 03                           je 0x1402de423
002DE420  4C 89 0E                        mov qword ptr [rsi], r9
002DE423  B0 01                           mov al, 1
002DE425  EB A2                           jmp 0x1402de3c9
002DE427  8B 6E 30                        mov ebp, dword ptr [rsi + 0x30]
002DE42A  33 D2                           xor edx, edx
002DE42C  6B C5 70                        imul eax, ebp, 0x70
002DE42F  48 8B CE                        mov rcx, rsi
002DE432  83 C0 38                        add eax, 0x38
002DE435  4C 63 C0                        movsxd r8, eax
002DE438  E8 03 88 3E 00                  call 0x1406c6c40
002DE43D  89 6E 30                        mov dword ptr [rsi + 0x30], ebp
002DE440  48 8B 8B 78 87 00 00            mov rcx, qword ptr [rbx + 0x8778]
002DE447  48 03 8B A8 86 00 00            add rcx, qword ptr [rbx + 0x86a8]
002DE44E  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
002DE452  48 8B 83 88 86 00 00            mov rax, qword ptr [rbx + 0x8688]
002DE459  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
002DE45D  48 8B 83 90 86 00 00            mov rax, qword ptr [rbx + 0x8690]
002DE464  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
002DE468  48 8B 83 98 86 00 00            mov rax, qword ptr [rbx + 0x8698]
002DE46F  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
002DE473  48 8B 83 A0 86 00 00            mov rax, qword ptr [rbx + 0x86a0]
002DE47A  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
002DE47E  33 C0                           xor eax, eax
002DE480  44 8B D8                        mov r11d, eax
002DE483  44 8B C8                        mov r9d, eax
002DE486  85 ED                           test ebp, ebp
002DE488  74 36                           je 0x1402de4c0
002DE48A  45 8D 14 7B                     lea r10d, [r11 + rdi*2]
002DE48E  48 8B 83 B0 86 00 00            mov rax, qword ptr [rbx + 0x86b0]
002DE495  41 8B CA                        mov ecx, r10d
002DE498  0F AF 0D 41 6F CE 00            imul ecx, dword ptr [rip + 0xce6f41]
002DE49F  45 8B C2                        mov r8d, r10d
002DE4A2  44 0F AF 46 30                  imul r8d, dword ptr [rsi + 0x30]
002DE4A7  41 03 C9                        add ecx, r9d
002DE4AA  45 03 C1                        add r8d, r9d
002DE4AD  41 FF C1                        inc r9d
002DE4B0  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002DE4B4  4A 89 54 C6 38                  mov qword ptr [rsi + r8*8 + 0x38], rdx
002DE4B9  44 3B CD                        cmp r9d, ebp
002DE4BC  72 D0                           jb 0x1402de48e
002DE4BE  33 C0                           xor eax, eax
002DE4C0  41 FF C3                        inc r11d
002DE4C3  41 83 FB 02                     cmp r11d, 2
002DE4C7  72 BA                           jb 0x1402de483
002DE4C9  FF C7                           inc edi
002DE4CB  83 FF 07                        cmp edi, 7
002DE4CE  72 B0                           jb 0x1402de480
002DE4D0  0F B6 6C 24 30                  movzx ebp, byte ptr [rsp + 0x30]
002DE4D5  E9 1D FD FF FF                  jmp 0x1402de1f7
002DE4DA  49 8B FA                        mov rdi, r10
002DE4DD  E9 AB FC FF FF                  jmp 0x1402de18d
002DE4E2  48 8B 83 D0 88 00 00            mov rax, qword ptr [rbx + 0x88d0]
002DE4E9  E9 BB FD FF FF                  jmp 0x1402de2a9
002DE4EE  4C 8B 93 68 88 00 00            mov r10, qword ptr [rbx + 0x8868]
002DE4F5  4D 3B E2                        cmp r12, r10
002DE4F8  76 79                           jbe 0x1402de573
002DE4FA  4C 8B 83 58 88 00 00            mov r8, qword ptr [rbx + 0x8858]
002DE501  4C 8B 8B A0 88 00 00            mov r9, qword ptr [rbx + 0x88a0]
002DE508  E9 79 FD FF FF                  jmp 0x1402de286
002DE50D  41 0F 0D 08                     prefetchw byte ptr [r8]
002DE511  41 8B 00                        mov eax, dword ptr [r8]
002DE514  8B D0                           mov edx, eax
002DE516  0F BA F2 15                     btr edx, 0x15
002DE51A  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
002DE51F  75 F3                           jne 0x1402de514
002DE521  0F BA E0 15                     bt eax, 0x15
002DE525  0F 83 EA FC FF FF               jae 0x1402de215
002DE52B  E8 A0 4C F8 FF                  call 0x1402631d0
002DE530  E9 E0 FC FF FF                  jmp 0x1402de215
002DE535  33 C0                           xor eax, eax
002DE537  E9 0F FE FF FF                  jmp 0x1402de34b
002DE53C  33 D2                           xor edx, edx
002DE53E  49 8B C2                        mov rax, r10
002DE541  48 F7 F1                        div rcx
002DE544  33 D2                           xor edx, edx
002DE546  48 8B F8                        mov rdi, rax
002DE549  48 0F AF C1                     imul rax, rcx
002DE54D  49 0F AF FB                     imul rdi, r11
002DE551  4C 2B D0                        sub r10, rax
002DE554  4D 0F AF D3                     imul r10, r11
002DE558  49 8B C2                        mov rax, r10
002DE55B  48 F7 F1                        div rcx
002DE55E  48 03 F8                        add rdi, rax
002DE561  E9 27 FC FF FF                  jmp 0x1402de18d
002DE566  48 6B 83 C0 88 00 00 64         imul rax, qword ptr [rbx + 0x88c0], 0x64
002DE56E  E9 36 FD FF FF                  jmp 0x1402de2a9
002DE573  4D 8B E2                        mov r12, r10
002DE576  EB 82                           jmp 0x1402de4fa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmSnapPerformanceAccumulation(__int64 a1, __int64 a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m77;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 11716245)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    result = 0;
    v_stack_m77 = a4;
    v_stack_m78 = (unsigned __int8)(a2);
    v_stack_m50 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    if (a3 != 0) goto loc_002DE367;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    a2 = (a2) << (32);
    result = (result) | (a2);
    if (((*(unsigned __int64 *)(a1 + 36768)) & (v_r11)) != 0) goto loc_002DE3EF;
loc_002DE129:
    v_r10 = (result) - (*(unsigned __int64 *)(a1 + 35000));
    if (((*(unsigned __int64 *)(a1 + 36768)) & (v_r11)) == 0) goto loc_002DE1A0;
    v_r11 = (0) - (*(unsigned __int64 *)(a1 + 35080));
    a1 = (result) - (*(unsigned __int64 *)(a1 + 34968));
    if (v_r10 == 0) goto loc_002DE4DA;
    if (a1 == 0) goto loc_002DE4DA;
    if (a1 == v_r11) goto loc_002DE4DA;
    v_stack_m70 = a2;
    if (a2 != 0) goto loc_002DE53C;
loc_002DE18D:
    v_rdi = 0;
loc_002DE1A0:
    *(unsigned __int64 *)(a1 + 35000) = result;
    result = v_r11;
    if (result >= = (*(unsigned __int64 *)(a1 + 34968))) {
        result = result;
        result = (result) - (*(unsigned __int64 *)(a1 + 34968));
    }
    *(unsigned __int64 *)(a1 + 34968) = result;
    if (((*(unsigned __int64 *)(a1 + 36768)) & (v_r11)) != 0) {
        *(unsigned __int64 *)(a1 + 35080) = 0;
    }
    result = 0;
    *(unsigned __int64 *)(a5) = v_xmm0;
    *(unsigned __int64 *)(a5 + 16) = v_xmm0;
    *(unsigned __int64 *)(a5 + 32) = v_xmm0;
    *(unsigned __int64 *)(a5 + 48) = 0;
    if (a6 != 0) goto loc_002DE427;
loc_002DE1F7:
    if (a3 != 0) goto loc_002DE216;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_002DE50D;
loc_002DE215:
loc_002DE216:
    v_rdi = v_stack_m60;
    if ((*(unsigned int *)(a1 + 35104)) != 3) { v_rdi = 0; }
    a4 = 0;
    v_stack_m88 = v_rdi;
    result = PpmUpdatePerformanceFeedback(a1, (unsigned __int8)((unsigned __int8)(a2)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002DE3C9;
    if (v_stack_m77 == 0) goto loc_002DE26D;
    result = *(unsigned __int64 *)(v_rip + 12782983);
    if (*(unsigned __int64 *)(v_rip + 12782983) != 0) {
        a1 = *(unsigned int *)(a1 + 36);
        a3 = 1;
        a2 = a3;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    if (v_rdi == 0) goto loc_002DE4EE;
loc_002DE286:
    if ((*(unsigned __int64 *)(a1 + 34984)) != 0) goto loc_002DE4E2;
    if ((*(unsigned __int64 *)(a1 + 34992)) == 0) goto loc_002DE566;
loc_002DE2A9:
    *(unsigned __int64 *)(a5 + 24) = *(unsigned __int64 *)(a1 + 35032);
    result = *(unsigned __int64 *)(a1 + 35032);
    if ((*(unsigned __int64 *)(a1 + 34992)) != 0) {
        result = *(unsigned __int64 *)(a1 + 35032);
    }
    *(unsigned __int64 *)(a5 + 32 * 1) = result;
    *(unsigned __int64 *)(a5 + 40) = *(unsigned __int64 *)(a1 + 35048);
    *(unsigned __int64 *)(a5 + 16) = *(unsigned __int64 *)(a1 + 35088);
    *(unsigned int *)(a5 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 14428)));
    if (a3 == 0) goto loc_002DE405;
loc_002DE304:
    if (a3 != 0) goto loc_002DE304;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 34912))) & (1)) == 0) goto loc_002DE535;
    if (*(unsigned __int64 *)(a1 + 34912) == 0) goto loc_002DE34B;
    result = *(unsigned __int64 *)(a1 + 34912);
    if ((*(unsigned int *)(a1 + 35104)) == 3) {
        a1 = *(unsigned int *)(v_rip + 11930282);
        result = *(unsigned __int64 *)(a1 + 35792);
        a2 = *(unsigned __int64 *)(result + a1 * 8);
        a1 = 0;
        result = a2;
        result = (result) >> (1);
        if ((((unsigned __int8)(a2)) & (1)) == 0) { result = a1; }
    }
    if (0 != result) goto loc_002DE3C7;
    if (v_rdi != 0) goto loc_002DE411;
    result = (*(unsigned __int64 *)(v_rdi)) - (v_stack_m68);
    a3 = (*(unsigned __int64 *)(v_rdi + 8)) + (result);
    goto loc_002DE411;
loc_002DE367:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, *(unsigned __int64 *)(v_rdi + 16));
loc_002DE37F:
    if (condition_is_not_equal) goto loc_002DE37F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 34912))) & (1)) == 0) goto loc_002DE3C7;
    if (*(unsigned __int64 *)(a1 + 34912) == 0) goto loc_002DE3BE;
    if ((*(unsigned int *)(a1 + 35104)) != 3) goto loc_002DE3BE;
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11930160)) * 8)) >> (1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11930160)) * 8))) & (1)) == 0) goto loc_002DE3C7;
loc_002DE3BE:
    if (v_r15 != 0) goto loc_002DE1D7;
loc_002DE3C7:
    result = 0;
loc_002DE3C9:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11930160)) * 8), a3, *(unsigned __int64 *)(v_rdi + 16));
    v_rsp = (v_rsp) + (112);
    return result;
loc_002DE3EF:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11930160)) * 8)) << (32);
    result = (result) | (a2);
    goto loc_002DE129;
loc_002DE405:
    if (v_rdi == 0) {
        a3 = (a3) + (*(unsigned __int64 *)(v_stack_p20 + 34896));
    }
    *(unsigned __int64 *)(a5) = result;
    v_r12 = (result) - (a3);
    *(unsigned __int64 *)(a5 + 8) = v_r12;
    if (a6 != 0) {
        *(unsigned __int64 *)(a6) = result;
    }
    goto loc_002DE3C9;
loc_002DE427:
    a2 = 0;
    result = (unsigned int)((1) * ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 48)))));
    result = (unsigned int)((result) + (56));
    result = memset(a6, a2, (int)((unsigned int)(result)), result);
    *(unsigned int *)(a6 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a6 + 48)));
    a1 = (*(unsigned __int64 *)(v_stack_p20 + 34680)) + (*(unsigned __int64 *)(v_stack_p20 + 34472));
    *(unsigned __int64 *)(a6 + 8) = a1;
    *(unsigned __int64 *)(a6 + 16) = *(unsigned __int64 *)(v_stack_p20 + 34440);
    *(unsigned __int64 *)(a6 + 24) = *(unsigned __int64 *)(v_stack_p20 + 34448);
    *(unsigned __int64 *)(a6 + 32) = *(unsigned __int64 *)(v_stack_p20 + 34456);
    *(unsigned __int64 *)(a6 + 40) = *(unsigned __int64 *)(v_stack_p20 + 34464);
    result = 0;
loc_002DE480:
loc_002DE483:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 48))) == 0) goto loc_002DE4C0;
loc_002DE48E:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(0 + v_rdi * 2))) * (*(unsigned int *)(v_rip + 13528897)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(0 + v_rdi * 2))) * (*(unsigned int *)(a6 + 48)));
    a1 = (unsigned int)((a1) + (0));
    a3 = (unsigned int)((a3) + (0));
    a4 = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(a6 + a3 * 8 + 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 34480) + a1 * 8);
    if (a4 < ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 48))))) goto loc_002DE48E;
    result = 0;
loc_002DE4C0:
    v_r11 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r11)) < 2) goto loc_002DE483;
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < 7) goto loc_002DE480;
    goto loc_002DE1F7;
loc_002DE4DA:
    goto loc_002DE18D;
loc_002DE4E2:
    goto loc_002DE2A9;
loc_002DE4EE:
    if (v_r12 <= (*(unsigned __int64 *)(v_stack_p20 + 34920))) goto loc_002DE573;
loc_002DE4FA:
    goto loc_002DE286;
loc_002DE50D:
loc_002DE514:
    if (v_r12 != (*(unsigned __int64 *)(v_stack_p20 + 34920))) goto loc_002DE514;
    if (v_r12 >= (*(unsigned __int64 *)(v_stack_p20 + 34920))) goto loc_002DE215;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 34904))))), *(unsigned __int64 *)(v_stack_p20 + 34904), *(unsigned __int64 *)(v_stack_p20 + 34976));
    goto loc_002DE215;
loc_002DE535:
    result = 0;
    goto loc_002DE34B;
loc_002DE53C:
    a2 = 0;
    a2 = 0;
    result = (*(unsigned __int64 *)(v_stack_p20 + 34920)) * (a1);
    v_rdi = (*(unsigned __int64 *)(v_stack_p20 + 34920)) * (v_r11);
    v_r10 = (*(unsigned __int64 *)(v_stack_p20 + 34920)) - (result);
    v_r10 = (v_r10) * (v_r11);
    v_rdi = (v_rdi) + (v_r10);
    goto loc_002DE18D;
loc_002DE566:
    result = (v_r10) * (*(unsigned __int64 *)(v_stack_p20 + 35008));
    goto loc_002DE2A9;
loc_002DE573:
    goto loc_002DE4FA;
}
```

## 5. (Beta) C Style

```c
int64_t PpmSnapPerformanceAccumulation(void *Arg1, int64_t Arg2, uint8_t Arg3, uint8_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m77;
    uint8_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0xB2C695)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    result = 0;
    v_stack_m77 = Arg4;
    v_stack_m78 = (uint8_t)(Arg2);
    v_stack_m50 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    if (Arg3 != 0) goto loc_002DE367;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, Arg4);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    if (((*(uint64_t *)(arg1 + 0x8FA0)) & (local_r11)) != 0) goto loc_002DE3EF;
loc_002DE129:
    local_r10 = (result) - (*(uint64_t *)(arg1 + 0x88B8));
    if (((*(uint64_t *)(arg1 + 0x8FA0)) & (local_r11)) == 0) goto loc_002DE1A0;
    local_r11 = (0) - (*(uint64_t *)(arg1 + 0x8908));
    Arg1 = (result) - (*(uint64_t *)(arg1 + 0x8898));
    if (local_r10 == 0) goto loc_002DE4DA;
    if (Arg1 == NULL) goto loc_002DE4DA;
    if (Arg1 == local_r11) goto loc_002DE4DA;
    v_stack_m70 = Arg2;
    if (Arg2 != 0) goto loc_002DE53C;
loc_002DE18D:
    local_rdi = 0;
loc_002DE1A0:
    *(uint64_t *)(arg1 + 0x88B8) = result;
    result = local_r11;
    if (result >= = (*(uint64_t *)(arg1 + 0x8898))) {
        result = result;
        result = (result) - (*(uint64_t *)(arg1 + 0x8898));
    }
    *(uint64_t *)(arg1 + 0x8898) = result;
    if (((*(uint64_t *)(arg1 + 0x8FA0)) & (local_r11)) != 0) {
        *(uint64_t *)(arg1 + 0x8908) = 0;
    }
    result = 0;
    *(uint64_t *)(arg5) = v_xmm0;
    *(uint64_t *)(arg5 + 0x10) = v_xmm0;
    *(uint64_t *)(arg5 + 0x20) = v_xmm0;
    *(uint64_t *)(arg5 + 0x30) = 0;
    if (Arg6 != 0) goto loc_002DE427;
loc_002DE1F7:
    if (Arg3 != 0) goto loc_002DE216;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_002DE50D;
loc_002DE215:
loc_002DE216:
    local_rdi = v_stack_m60;
    if ((*(uint32_t *)(arg1 + 0x8920)) != 3) { local_rdi = 0; }
    Arg4 = 0;
    v_stack_m88 = local_rdi;
    result = PpmUpdatePerformanceFeedback(Arg1, (uint8_t)((uint8_t)(Arg2)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002DE3C9;
    if (v_stack_m77 == 0) goto loc_002DE26D;
    result = *(uint64_t *)(v_rip + 0xC30D87);
    if (*(uint64_t *)(v_rip + 0xC30D87) != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x24);
        Arg3 = 1;
        Arg2 = Arg3;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
    if (local_rdi == 0) goto loc_002DE4EE;
loc_002DE286:
    if ((*(uint64_t *)(arg1 + 0x88A8)) != 0) goto loc_002DE4E2;
    if ((*(uint64_t *)(arg1 + 0x88B0)) == 0) goto loc_002DE566;
loc_002DE2A9:
    *(uint64_t *)(arg5 + 0x18) = *(uint64_t *)(arg1 + 0x88D8);
    result = *(uint64_t *)(arg1 + 0x88D8);
    if ((*(uint64_t *)(arg1 + 0x88B0)) != 0) {
        result = *(uint64_t *)(arg1 + 0x88D8);
    }
    *(uint64_t *)(arg5 + 0x20 * 1) = result;
    *(uint64_t *)(arg5 + 0x28) = *(uint64_t *)(arg1 + 0x88E8);
    *(uint64_t *)(arg5 + 0x10) = *(uint64_t *)(arg1 + 0x8910);
    *(uint32_t *)(arg5 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x385C)));
    if (Arg3 == 0) goto loc_002DE405;
loc_002DE304:
    if (Arg3 != 0) goto loc_002DE304;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x8860))) & (1)) == 0) goto loc_002DE535;
    if (*(uint64_t *)(arg1 + 0x8860) == 0) goto loc_002DE34B;
    result = *(uint64_t *)(arg1 + 0x8860);
    if ((*(uint32_t *)(arg1 + 0x8920)) == 3) {
        Arg1 = *(uint32_t *)(v_rip + 0xB60AAA);
        result = *(uint64_t *)(arg1 + 0x8BD0);
        Arg2 = *(uint64_t *)(result + arg1 * 8);
        Arg1 = 0;
        result = Arg2;
        result = (result) >> (1);
        if ((((uint8_t)(Arg2)) & (1)) == 0) { result = Arg1; }
    }
    if (0 != result) goto loc_002DE3C7;
    if (local_rdi != 0) goto loc_002DE411;
    result = (*(uint64_t *)(local_rdi)) - (v_stack_m68);
    Arg3 = (*(uint64_t *)(local_rdi + 0x8)) + (result);
    goto loc_002DE411;
loc_002DE367:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, *(uint64_t *)(local_rdi + 0x10));
loc_002DE37F:
    if (condition_is_not_equal) goto loc_002DE37F;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x8860))) & (1)) == 0) goto loc_002DE3C7;
    if (*(uint64_t *)(arg1 + 0x8860) == 0) goto loc_002DE3BE;
    if ((*(uint32_t *)(arg1 + 0x8920)) != 3) goto loc_002DE3BE;
    local_r15 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60A30)) * 8)) >> (1);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60A30)) * 8))) & (1)) == 0) goto loc_002DE3C7;
loc_002DE3BE:
    if (local_r15 != 0) goto loc_002DE1D7;
loc_002DE3C7:
    result = 0;
loc_002DE3C9:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60A30)) * 8), Arg3, *(uint64_t *)(local_rdi + 0x10));
    local_rsp = (local_rsp) + (112);
    return result;
loc_002DE3EF:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60A30)) * 8)) << (32);
    result = (result) | (Arg2);
    goto loc_002DE129;
loc_002DE405:
    if (local_rdi == 0) {
        Arg3 = (Arg3) + (*(uint64_t *)(v_stack_p20 + 0x8850));
    }
    *(uint64_t *)(arg5) = result;
    local_r12 = (result) - (Arg3);
    *(uint64_t *)(arg5 + 0x8) = local_r12;
    if (Arg6 != 0) {
        *(uint64_t *)(Arg6) = result;
    }
    goto loc_002DE3C9;
loc_002DE427:
    Arg2 = 0;
    result = (uint32_t)((1) * ((uint32_t)((uint32_t)(*(uint32_t *)(Arg6 + 0x30)))));
    result = (uint32_t)((result) + (56));
    result = memset(Arg6, Arg2, (int32_t)((uint32_t)(result)), result);
    *(uint32_t *)(Arg6 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg6 + 0x30)));
    Arg1 = (*(uint64_t *)(v_stack_p20 + 0x8778)) + (*(uint64_t *)(v_stack_p20 + 0x86A8));
    *(void **)(Arg6 + 0x8) = Arg1;
    *(uint64_t *)(Arg6 + 0x10) = *(uint64_t *)(v_stack_p20 + 0x8688);
    *(uint64_t *)(Arg6 + 0x18) = *(uint64_t *)(v_stack_p20 + 0x8690);
    *(uint64_t *)(Arg6 + 0x20) = *(uint64_t *)(v_stack_p20 + 0x8698);
    *(uint64_t *)(Arg6 + 0x28) = *(uint64_t *)(v_stack_p20 + 0x86A0);
    result = 0;
loc_002DE480:
loc_002DE483:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg6 + 0x30))) == 0) goto loc_002DE4C0;
loc_002DE48E:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(0 + local_rdi * 2))) * (*(uint32_t *)(v_rip + 0xCE6F41)));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(0 + local_rdi * 2))) * (*(uint32_t *)(Arg6 + 0x30)));
    Arg1 = (uint32_t)((Arg1) + (0));
    Arg3 = (uint32_t)((Arg3) + (0));
    Arg4 = (uint32_t)((0) + 1);
    *(uint64_t *)(Arg6 + Arg3 * 8 + 0x38) = *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x86B0) + arg1 * 8);
    if (Arg4 < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg6 + 0x30))))) goto loc_002DE48E;
    result = 0;
loc_002DE4C0:
    local_r11 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r11)) < 2) goto loc_002DE483;
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < 7) goto loc_002DE480;
    goto loc_002DE1F7;
loc_002DE4DA:
    goto loc_002DE18D;
loc_002DE4E2:
    goto loc_002DE2A9;
loc_002DE4EE:
    if (local_r12 <= (*(uint64_t *)(v_stack_p20 + 0x8868))) goto loc_002DE573;
loc_002DE4FA:
    goto loc_002DE286;
loc_002DE50D:
loc_002DE514:
    if (local_r12 != (*(uint64_t *)(v_stack_p20 + 0x8868))) goto loc_002DE514;
    if (local_r12 >= (*(uint64_t *)(v_stack_p20 + 0x8868))) goto loc_002DE215;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x8858))))), *(uint64_t *)(v_stack_p20 + 0x8858), *(uint64_t *)(v_stack_p20 + 0x88A0));
    goto loc_002DE215;
loc_002DE535:
    result = 0;
    goto loc_002DE34B;
loc_002DE53C:
    Arg2 = 0;
    Arg2 = 0;
    result = (*(uint64_t *)(v_stack_p20 + 0x8868)) * (Arg1);
    local_rdi = (*(uint64_t *)(v_stack_p20 + 0x8868)) * (local_r11);
    local_r10 = (*(uint64_t *)(v_stack_p20 + 0x8868)) - (result);
    local_r10 = (local_r10) * (local_r11);
    local_rdi = (local_rdi) + (local_r10);
    goto loc_002DE18D;
loc_002DE566:
    result = (local_r10) * (*(uint64_t *)(v_stack_p20 + 0x88C0));
    goto loc_002DE2A9;
loc_002DE573:
    goto loc_002DE4FA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x385C` | `32` | `R` |
| `Arg1` | `+ 0x8688` | `64` | `R` |
| `Arg1` | `+ 0x8690` | `64` | `R` |
| `Arg1` | `+ 0x8698` | `64` | `R` |
| `Arg1` | `+ 0x86A0` | `64` | `R` |
| `Arg1` | `+ 0x86A8` | `64` | `R` |
| `Arg1` | `+ 0x86B0` | `64` | `R` |
| `Arg1` | `+ 0x8778` | `64` | `R` |
| `Arg1` | `+ 0x8850` | `64` | `R` |
| `Arg1` | `+ 0x8858` | `64` | `R` |
| `Arg1` | `+ 0x8860` | `8` | `R` |
| `Arg1` | `+ 0x8860` | `64` | `R` |
| `Arg1` | `+ 0x8868` | `64` | `R` |
| `Arg1` | `+ 0x8898` | `64` | `R` |
| `Arg1` | `+ 0x8898` | `64` | `W` |
| `Arg1` | `+ 0x88A0` | `64` | `R` |
| `Arg1` | `+ 0x88A0` | `64` | `R/W` |
| `Arg1` | `+ 0x88A8` | `64` | `R` |
| `Arg1` | `+ 0x88B0` | `64` | `R` |
| `Arg1` | `+ 0x88B8` | `64` | `R` |
| `Arg1` | `+ 0x88B8` | `64` | `W` |
| `Arg1` | `+ 0x88C0` | `64` | `R` |
| `Arg1` | `+ 0x88C8` | `64` | `R/W` |
| `Arg1` | `+ 0x88D0` | `64` | `R` |
| `Arg1` | `+ 0x88D8` | `64` | `R` |
| `Arg1` | `+ 0x88E8` | `64` | `R` |
| `Arg1` | `+ 0x8908` | `64` | `R` |
| `Arg1` | `+ 0x8908` | `64` | `W` |
| `Arg1` | `+ 0x8910` | `64` | `R` |
| `Arg1` | `+ 0x8910` | `64` | `R/W` |
| `Arg1` | `+ 0x8920` | `32` | `R` |

추가 오프셋 13개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DE090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
