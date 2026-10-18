# MiComputeSystemTrimCriteria

- RVA: `0x0034E184`–`0x0034E6FE` (길이 `1,402` bytes)
- VA: `0x000000014034E184`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00078B68`
- 디코드: `332`개 명령, `1,402/1,402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0034E1B4` → [MiGetAvailablePagesForTrimPass](MiGetAvailablePagesForTrimPass_function_0034D324.md) (function, `0x0034D324`)
- `0x0034E367` → [MiComputeAgeDistribution](../40/MiComputeAgeDistribution_function_0040A360.md) (function, `0x0040A360`)
- `0x0034E3F7` → [MiPulseLowAvailableEvent](MiPulseLowAvailableEvent_function_0034F694.md) (function, `0x0034F694`)
- `0x0034E6F4` → [MiPruneProcessLargePageCaches](../2D/MiPruneProcessLargePageCaches_function_002DBD60.md) (function, `0x002DBD60`)

### Direct callers
- [MiProcessWorkingSets](MiProcessWorkingSets_function_0034E710.md) at `0x0034E772`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0034E588` → [sub_006E2286 + 0x1A](../6E/Unknown_function_006E2286.md) (`tail-transfer`)
  - `0x0034E64B` → [sub_006E2286](../6E/Unknown_function_006E2286.md) (`tail-transfer`)
  - `0x0034E65F` → [sub_006E2286](../6E/Unknown_function_006E2286.md) (`tail-transfer`)
  - `0x0034E67F` → [sub_006E2286 + 0x9](../6E/Unknown_function_006E2286.md) (`tail-transfer`)
  - `0x0034E6C5` → [sub_006E2286 + 0x1A](../6E/Unknown_function_006E2286.md) (`tail-transfer`)
  - `0x0034E6DD` → [sub_006E2286 + 0x26](../6E/Unknown_function_006E2286.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0034E184  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0034E189  55                              push rbp
0034E18A  56                              push rsi
0034E18B  57                              push rdi
0034E18C  41 54                           push r12
0034E18E  41 55                           push r13
0034E190  41 56                           push r14
0034E192  41 57                           push r15
0034E194  48 83 EC 20                     sub rsp, 0x20
0034E198  48 8B 99 C0 44 00 00            mov rbx, qword ptr [rcx + 0x44c0]
0034E19F  45 33 DB                        xor r11d, r11d
0034E1A2  48 8B F2                        mov rsi, rdx
0034E1A5  44 89 5C 24 60                  mov dword ptr [rsp + 0x60], r11d
0034E1AA  4C 8B F9                        mov r15, rcx
0034E1AD  45 8B CB                        mov r9d, r11d
0034E1B0  44 8B 73 28                     mov r14d, dword ptr [rbx + 0x28]
0034E1B4  E8 6B F1 FF FF                  call 0x14034d324
0034E1B9  48 8B E8                        mov rbp, rax
0034E1BC  41 8D 4B 07                     lea ecx, [r11 + 7]
0034E1C0  49 8D 87 24 1C 00 00            lea rax, [r15 + 0x1c24]
0034E1C7  41 8B D3                        mov edx, r11d
0034E1CA  45 8D 63 01                     lea r12d, [r11 + 1]
0034E1CE  03 10                           add edx, dword ptr [rax]
0034E1D0  48 8D 40 04                     lea rax, [rax + 4]
0034E1D4  49 2B CC                        sub rcx, r12
0034E1D7  75 F5                           jne 0x14034e1ce
0034E1D9  8B 4B 2C                        mov ecx, dword ptr [rbx + 0x2c]
0034E1DC  8B C2                           mov eax, edx
0034E1DE  2B C1                           sub eax, ecx
0034E1E0  89 53 2C                        mov dword ptr [rbx + 0x2c], edx
0034E1E3  3B CA                           cmp ecx, edx
0034E1E5  45 8A EB                        mov r13b, r11b
0034E1E8  48 8B 8B 48 01 00 00            mov rcx, qword ptr [rbx + 0x148]
0034E1EF  49 8B FB                        mov rdi, r11
0034E1F2  8B 53 78                        mov edx, dword ptr [rbx + 0x78]
0034E1F5  45 1B D2                        sbb r10d, r10d
0034E1F8  44 23 D0                        and r10d, eax
0034E1FB  4C 8B C1                        mov r8, rcx
0034E1FE  4C 2B C5                        sub r8, rbp
0034E201  44 89 54 24 70                  mov dword ptr [rsp + 0x70], r10d
0034E206  48 8B C5                        mov rax, rbp
0034E209  48 2B C1                        sub rax, rcx
0034E20C  48 3B E9                        cmp rbp, rcx
0034E20F  4C 0F 47 C0                     cmova r8, rax
0034E213  83 E2 07                        and edx, 7
0034E216  49 8B C8                        mov rcx, r8
0034E219  48 C1 E9 03                     shr rcx, 3
0034E21D  48 8B 84 D3 88 00 00 00         mov rax, qword ptr [rbx + rdx*8 + 0x88]
0034E225  48 C1 E8 03                     shr rax, 3
0034E229  48 2B C8                        sub rcx, rax
0034E22C  48 01 8B 80 00 00 00            add qword ptr [rbx + 0x80], rcx
0034E233  4C 89 84 D3 88 00 00 00         mov qword ptr [rbx + rdx*8 + 0x88], r8
0034E23B  83 7B 50 04                     cmp dword ptr [rbx + 0x50], 4
0034E23F  0F 84 93 03 00 00               je 0x14034e5d8
0034E245  48 81 FD 20 01 00 00            cmp rbp, 0x120
0034E24C  45 8B C3                        mov r8d, r11d
0034E24F  45 0F 46 C4                     cmovbe r8d, r12d
0034E253  48 8B 8B 48 01 00 00            mov rcx, qword ptr [rbx + 0x148]
0034E25A  48 8B C1                        mov rax, rcx
0034E25D  45 85 C0                        test r8d, r8d
0034E260  0F 85 A4 02 00 00               jne 0x14034e50a
0034E266  48 8B D5                        mov rdx, rbp
0034E269  48 2B 93 28 01 00 00            sub rdx, qword ptr [rbx + 0x128]
0034E270  48 C1 E8 02                     shr rax, 2
0034E274  48 3B E8                        cmp rbp, rax
0034E277  0F 82 28 03 00 00               jb 0x14034e5a5
0034E27D  48 8D 04 8D 00 00 00 00         lea rax, [rcx*4]
0034E285  48 3B E8                        cmp rbp, rax
0034E288  0F 82 FF 02 00 00               jb 0x14034e58d
0034E28E  41 8B CA                        mov ecx, r10d
0034E291  48 8B C5                        mov rax, rbp
0034E294  48 C1 E8 02                     shr rax, 2
0034E298  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0034E29D  48 3B C8                        cmp rcx, rax
0034E2A0  0F 83 62 03 00 00               jae 0x14034e608
0034E2A6  B9 04 00 00 00                  mov ecx, 4
0034E2AB  49 8D 87 30 1C 00 00            lea rax, [r15 + 0x1c30]
0034E2B2  45 8B E3                        mov r12d, r11d
0034E2B5  8D 51 FD                        lea edx, [rcx - 3]
0034E2B8  44 03 20                        add r12d, dword ptr [rax]
0034E2BB  48 8D 40 04                     lea rax, [rax + 4]
0034E2BF  48 2B CA                        sub rcx, rdx
0034E2C2  75 F4                           jne 0x14034e2b8
0034E2C4  48 85 FF                        test rdi, rdi
0034E2C7  0F 84 E2 00 00 00               je 0x14034e3af
0034E2CD  B9 00 10 00 00                  mov ecx, 0x1000
0034E2D2  48 81 FD 20 01 00 00            cmp rbp, 0x120
0034E2D9  0F 86 93 03 00 00               jbe 0x14034e672
0034E2DF  48 8B C7                        mov rax, rdi
0034E2E2  48 85 FF                        test rdi, rdi
0034E2E5  0F 85 A9 03 00 00               jne 0x14034e694
0034E2EB  48 8B 8B 48 01 00 00            mov rcx, qword ptr [rbx + 0x148]
0034E2F2  48 8D 04 8D 00 00 00 00         lea rax, [rcx*4]
0034E2FA  48 3B E8                        cmp rbp, rax
0034E2FD  0F 82 44 02 00 00               jb 0x14034e547
0034E303  48 C1 E1 04                     shl rcx, 4
0034E307  48 3B E9                        cmp rbp, rcx
0034E30A  76 0E                           jbe 0x14034e31a
0034E30C  48 8B 83 40 01 00 00            mov rax, qword ptr [rbx + 0x140]
0034E313  48 89 83 48 01 00 00            mov qword ptr [rbx + 0x148], rax
0034E31A  48 89 AB 28 01 00 00            mov qword ptr [rbx + 0x128], rbp
0034E321  48 85 FF                        test rdi, rdi
0034E324  0F 85 CA 00 00 00               jne 0x14034e3f4
0034E32A  48 8B 83 20 01 00 00            mov rax, qword ptr [rbx + 0x120]
0034E331  41 8A CB                        mov cl, r11b
0034E334  BF 0A 00 00 00                  mov edi, 0xa
0034E339  48 85 C0                        test rax, rax
0034E33C  0F 85 94 03 00 00               jne 0x14034e6d6
0034E342  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
0034E349  48 C1 E0 02                     shl rax, 2
0034E34D  48 39 83 50 01 00 00            cmp qword ptr [rbx + 0x150], rax
0034E354  0F 83 08 01 00 00               jae 0x14034e462
0034E35A  66 44 39 9B 12 01 00 00         cmp word ptr [rbx + 0x112], r11w
0034E362  74 23                           je 0x14034e387
0034E364  49 8B CF                        mov rcx, r15
0034E367  E8 F4 BF 0B 00                  call 0x14040a360
0034E36C  45 33 DB                        xor r11d, r11d
0034E36F  66 89 83 12 01 00 00            mov word ptr [rbx + 0x112], ax
0034E376  66 85 C0                        test ax, ax
0034E379  0F 85 E1 00 00 00               jne 0x14034e460
0034E37F  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
0034E384  41 8A CB                        mov cl, r11b
0034E387  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0034E38C  48 8B C5                        mov rax, rbp
0034E38F  48 C1 E8 04                     shr rax, 4
0034E393  48 3B D0                        cmp rdx, rax
0034E396  0F 83 35 02 00 00               jae 0x14034e5d1
0034E39C  45 85 C9                        test r9d, r9d
0034E39F  0F B6 C9                        movzx ecx, cl
0034E3A2  B8 08 00 00 00                  mov eax, 8
0034E3A7  0F 45 C8                        cmovne ecx, eax
0034E3AA  E9 B8 00 00 00                  jmp 0x14034e467
0034E3AF  45 85 C0                        test r8d, r8d
0034E3B2  0F 85 15 FF FF FF               jne 0x14034e2cd
0034E3B8  41 8B C4                        mov eax, r12d
0034E3BB  B9 00 00 02 00                  mov ecx, 0x20000
0034E3C0  2B 43 30                        sub eax, dword ptr [rbx + 0x30]
0034E3C3  3B C1                           cmp eax, ecx
0034E3C5  0F 87 72 02 00 00               ja 0x14034e63d
0034E3CB  45 85 D2                        test r10d, r10d
0034E3CE  0F 84 F9 FE FF FF               je 0x14034e2cd
0034E3D4  3D 00 80 01 00                  cmp eax, 0x18000
0034E3D9  0F 86 EE FE FF FF               jbe 0x14034e2cd
0034E3DF  48 39 8B 50 01 00 00            cmp qword ptr [rbx + 0x150], rcx
0034E3E6  44 0F 42 CA                     cmovb r9d, edx
0034E3EA  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
0034E3EF  E9 D9 FE FF FF                  jmp 0x14034e2cd
0034E3F4  49 8B CF                        mov rcx, r15
0034E3F7  E8 98 12 00 00                  call 0x14034f694
0034E3FC  41 8D 45 FE                     lea eax, [r13 - 2]
0034E400  41 B8 01 00 00 00               mov r8d, 1
0034E406  41 3A C0                        cmp al, r8b
0034E409  0F 86 BB 02 00 00               jbe 0x14034e6ca
0034E40F  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0034E414  45 33 DB                        xor r11d, r11d
0034E417  44 88 1E                        mov byte ptr [rsi], r11b
0034E41A  0F 57 C0                        xorps xmm0, xmm0
0034E41D  4C 89 5E 60                     mov qword ptr [rsi + 0x60], r11
0034E421  45 0B F0                        or r14d, r8d
0034E424  48 89 7E 50                     mov qword ptr [rsi + 0x50], rdi
0034E428  49 8B 8F 00 49 00 00            mov rcx, qword ptr [r15 + 0x4900]
0034E42F  4C 89 5E 68                     mov qword ptr [rsi + 0x68], r11
0034E433  48 03 CF                        add rcx, rdi
0034E436  48 89 4E 48                     mov qword ptr [rsi + 0x48], rcx
0034E43A  44 88 6E 02                     mov byte ptr [rsi + 2], r13b
0034E43E  0F 11 46 08                     movups xmmword ptr [rsi + 8], xmm0
0034E442  41 0F B6 C5                     movzx eax, r13b
0034E446  0F 11 46 18                     movups xmmword ptr [rsi + 0x18], xmm0
0034E44A  0F 11 46 28                     movups xmmword ptr [rsi + 0x28], xmm0
0034E44E  0F 11 46 38                     movups xmmword ptr [rsi + 0x38], xmm0
0034E452  44 89 63 30                     mov dword ptr [rbx + 0x30], r12d
0034E456  44 01 84 83 A0 01 00 00         add dword ptr [rbx + rax*4 + 0x1a0], r8d
0034E45E  EB 79                           jmp 0x14034e4d9
0034E460  B1 0B                           mov cl, 0xb
0034E462  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0034E467  0F B7 83 14 01 00 00            movzx eax, word ptr [rbx + 0x114]
0034E46E  66 85 C0                        test ax, ax
0034E471  74 1D                           je 0x14034e490
0034E473  66 39 83 12 01 00 00            cmp word ptr [rbx + 0x112], ax
0034E47A  73 07                           jae 0x14034e483
0034E47C  66 89 83 12 01 00 00            mov word ptr [rbx + 0x112], ax
0034E483  84 C9                           test cl, cl
0034E485  75 09                           jne 0x14034e490
0034E487  B1 0C                           mov cl, 0xc
0034E489  66 89 83 12 01 00 00            mov word ptr [rbx + 0x112], ax
0034E490  44 88 1E                        mov byte ptr [rsi], r11b
0034E493  0F 57 C0                        xorps xmm0, xmm0
0034E496  4C 89 5E 60                     mov qword ptr [rsi + 0x60], r11
0034E49A  41 B8 01 00 00 00               mov r8d, 1
0034E4A0  4C 89 5E 50                     mov qword ptr [rsi + 0x50], r11
0034E4A4  49 8B 87 00 49 00 00            mov rax, qword ptr [r15 + 0x4900]
0034E4AB  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
0034E4AF  4C 89 5E 68                     mov qword ptr [rsi + 0x68], r11
0034E4B3  88 4E 02                        mov byte ptr [rsi + 2], cl
0034E4B6  0F 11 46 08                     movups xmmword ptr [rsi + 8], xmm0
0034E4BA  0F 11 46 18                     movups xmmword ptr [rsi + 0x18], xmm0
0034E4BE  0F 11 46 28                     movups xmmword ptr [rsi + 0x28], xmm0
0034E4C2  0F 11 46 38                     movups xmmword ptr [rsi + 0x38], xmm0
0034E4C6  84 C9                           test cl, cl
0034E4C8  74 65                           je 0x14034e52f
0034E4CA  0F B6 C1                        movzx eax, cl
0034E4CD  44 01 84 83 A0 01 00 00         add dword ptr [rbx + rax*4 + 0x1a0], r8d
0034E4D5  41 83 CE 02                     or r14d, 2
0034E4D9  48 85 ED                        test rbp, rbp
0034E4DC  75 34                           jne 0x14034e512
0034E4DE  B0 64                           mov al, 0x64
0034E4E0  88 46 03                        mov byte ptr [rsi + 3], al
0034E4E3  45 84 F0                        test r8b, r14b
0034E4E6  74 3B                           je 0x14034e523
0034E4E8  45 84 ED                        test r13b, r13b
0034E4EB  0F 85 FE 01 00 00               jne 0x14034e6ef
0034E4F1  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0034E4F6  41 8B C6                        mov eax, r14d
0034E4F9  48 83 C4 20                     add rsp, 0x20
0034E4FD  41 5F                           pop r15
0034E4FF  41 5E                           pop r14
0034E501  41 5D                           pop r13
0034E503  41 5C                           pop r12
0034E505  5F                              pop rdi
0034E506  5E                              pop rsi
0034E507  5D                              pop rbp
0034E508  C3                              ret
0034E509  CC                              int3
0034E50A  49 8B D3                        mov rdx, r11
0034E50D  E9 62 FD FF FF                  jmp 0x14034e274
0034E512  48 3B D5                        cmp rdx, rbp
0034E515  73 C7                           jae 0x14034e4de
0034E517  6B 44 24 70 64                  imul eax, dword ptr [rsp + 0x70], 0x64
0034E51C  33 D2                           xor edx, edx
0034E51E  48 F7 F5                        div rbp
0034E521  EB BD                           jmp 0x14034e4e0
0034E523  80 7E 04 02                     cmp byte ptr [rsi + 4], 2
0034E527  75 BF                           jne 0x14034e4e8
0034E529  44 88 46 04                     mov byte ptr [rsi + 4], r8b
0034E52D  EB B9                           jmp 0x14034e4e8
0034E52F  44 38 5B 37                     cmp byte ptr [rbx + 0x37], r11b
0034E533  0F 85 88 00 00 00               jne 0x14034e5c1
0034E539  45 85 F6                        test r14d, r14d
0034E53C  B8 20 00 00 00                  mov eax, 0x20
0034E541  44 0F 44 F0                     cmove r14d, eax
0034E545  EB 92                           jmp 0x14034e4d9
0034E547  48 8B 93 80 00 00 00            mov rdx, qword ptr [rbx + 0x80]
0034E54E  48 8D 04 95 00 00 00 00         lea rax, [rdx*4]
0034E556  48 3B C1                        cmp rax, rcx
0034E559  0F 82 4A 01 00 00               jb 0x14034e6a9
0034E55F  48 8D 04 12                     lea rax, [rdx + rdx]
0034E563  BA 01 00 00 00                  mov edx, 1
0034E568  48 3B C1                        cmp rax, rcx
0034E56B  0F 86 A9 FD FF FF               jbe 0x14034e31a
0034E571  48 8B 8B 38 01 00 00            mov rcx, qword ptr [rbx + 0x138]
0034E578  48 89 83 48 01 00 00            mov qword ptr [rbx + 0x148], rax
0034E57F  48 3B C1                        cmp rax, rcx
0034E582  0F 86 92 FD FF FF               jbe 0x14034e31a
0034E588  E9 13 3D 39 00                  jmp 0x1406e22a0
0034E58D  48 85 D2                        test rdx, rdx
0034E590  0F 89 F8 FC FF FF               jns 0x14034e28e
0034E596  48 8B C1                        mov rax, rcx
0034E599  48 2B C2                        sub rax, rdx
0034E59C  48 3B E8                        cmp rbp, rax
0034E59F  0F 83 E9 FC FF FF               jae 0x14034e28e
0034E5A5  48 8B BB 38 01 00 00            mov rdi, qword ptr [rbx + 0x138]
0034E5AC  48 2B CA                        sub rcx, rdx
0034E5AF  48 2B CD                        sub rcx, rbp
0034E5B2  45 8A EC                        mov r13b, r12b
0034E5B5  48 3B CF                        cmp rcx, rdi
0034E5B8  48 0F 46 F9                     cmovbe rdi, rcx
0034E5BC  E9 CD FC FF FF                  jmp 0x14034e28e
0034E5C1  41 83 CE 40                     or r14d, 0x40
0034E5C5  66 89 BB 12 01 00 00            mov word ptr [rbx + 0x112], di
0034E5CC  E9 08 FF FF FF                  jmp 0x14034e4d9
0034E5D1  B1 09                           mov cl, 9
0034E5D3  E9 8F FE FF FF                  jmp 0x14034e467
0034E5D8  66 44 39 9B 14 01 00 00         cmp word ptr [rbx + 0x114], r11w
0034E5E0  0F 84 5F FC FF FF               je 0x14034e245
0034E5E6  44 38 9B 16 01 00 00            cmp byte ptr [rbx + 0x116], r11b
0034E5ED  0F 84 52 FC FF FF               je 0x14034e245
0034E5F3  44 38 9B 17 01 00 00            cmp byte ptr [rbx + 0x117], r11b
0034E5FA  0F 84 45 FC FF FF               je 0x14034e245
0034E600  45 8B C4                        mov r8d, r12d
0034E603  E9 4B FC FF FF                  jmp 0x14034e253
0034E608  48 2B C8                        sub rcx, rax
0034E60B  48 3B CF                        cmp rcx, rdi
0034E60E  0F 86 92 FC FF FF               jbe 0x14034e2a6
0034E614  B8 00 20 00 00                  mov eax, 0x2000
0034E619  48 3B F8                        cmp rdi, rax
0034E61C  0F 83 84 FC FF FF               jae 0x14034e2a6
0034E622  45 85 C0                        test r8d, r8d
0034E625  0F 85 7B FC FF FF               jne 0x14034e2a6
0034E62B  48 3B C8                        cmp rcx, rax
0034E62E  48 8B F9                        mov rdi, rcx
0034E631  41 B5 03                        mov r13b, 3
0034E634  48 0F 47 F8                     cmova rdi, rax
0034E638  E9 69 FC FF FF                  jmp 0x14034e2a6
0034E63D  49 8B 8F 00 49 00 00            mov rcx, qword ptr [r15 + 0x4900]
0034E644  48 81 F9 00 00 10 00            cmp rcx, 0x100000
0034E64B  0F 83 35 3C 39 00               jae 0x1406e2286
0034E651  49 8B 87 50 48 00 00            mov rax, qword ptr [r15 + 0x4850]
0034E658  48 C1 E8 02                     shr rax, 2
0034E65C  48 3B C8                        cmp rcx, rax
0034E65F  0F 83 21 3C 39 00               jae 0x1406e2286
0034E665  BF 00 80 00 00                  mov edi, 0x8000
0034E66A  41 B5 02                        mov r13b, 2
0034E66D  E9 5B FC FF FF                  jmp 0x14034e2cd
0034E672  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
0034E679  48 D1 E8                        shr rax, 1
0034E67C  48 3B C1                        cmp rax, rcx
0034E67F  0F 83 0A 3C 39 00               jae 0x1406e228f
0034E685  48 3B F8                        cmp rdi, rax
0034E688  48 0F 43 C7                     cmovae rax, rdi
0034E68C  48 8B F8                        mov rdi, rax
0034E68F  E9 4B FC FF FF                  jmp 0x14034e2df
0034E694  48 3B C1                        cmp rax, rcx
0034E697  0F 83 4E FC FF FF               jae 0x14034e2eb
0034E69D  45 85 C0                        test r8d, r8d
0034E6A0  48 0F 44 F9                     cmove rdi, rcx
0034E6A4  E9 42 FC FF FF                  jmp 0x14034e2eb
0034E6A9  48 8B 8B 30 01 00 00            mov rcx, qword ptr [rbx + 0x130]
0034E6B0  BA 01 00 00 00                  mov edx, 1
0034E6B5  48 89 83 48 01 00 00            mov qword ptr [rbx + 0x148], rax
0034E6BC  48 3B C1                        cmp rax, rcx
0034E6BF  0F 83 55 FC FF FF               jae 0x14034e31a
0034E6C5  E9 D6 3B 39 00                  jmp 0x1406e22a0
0034E6CA  48 89 BB 20 01 00 00            mov qword ptr [rbx + 0x120], rdi
0034E6D1  E9 39 FD FF FF                  jmp 0x14034e40f
0034E6D6  48 3B 83 50 01 00 00            cmp rax, qword ptr [rbx + 0x150]
0034E6DD  0F 87 C9 3B 39 00               ja 0x1406e22ac
0034E6E3  4C 89 9B 20 01 00 00            mov qword ptr [rbx + 0x120], r11
0034E6EA  E9 53 FC FF FF                  jmp 0x14034e342
0034E6EF  33 D2                           xor edx, edx
0034E6F1  49 8B CF                        mov rcx, r15
0034E6F4  E8 67 D6 F8 FF                  call 0x1402dbd60
0034E6F9  E9 F3 FD FF FF                  jmp 0x14034e4f1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiComputeSystemTrimCriteria(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p70;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_r11 = 0;
    v_stack_p8 = 0;
    result = MiGetAvailablePagesForTrimPass(a1, a2, a3, 0);
loc_0034E1CE:
    a2 = (unsigned int)((0) + (*(unsigned int *)(a1 + 7204)));
    a1 = (v_r11 + 7) - (v_r11 + 1);
    if (condition_is_not_equal) goto loc_0034E1CE;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 44)))));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 44) = (unsigned int)(a2);
    v_r10 = (unsigned int)((v_r10) & ((unsigned int)(result)));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328)) - (result);
    v_stack_p18 = (unsigned int)(v_r10);
    result = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328));
    if (result > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328))) { a3 = result; }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 120))) & (7));
    a1 = (a3) >> (3);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + a2 * 8 + 136)) >> (3);
    a1 = (a1) - (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + a2 * 8 + 136) = a3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 80)) == 4) goto loc_0034E5D8;
loc_0034E245:
    a3 = 0;
    if (result <= 288) { a3 = (unsigned int)(v_r11 + 1); }
loc_0034E253:
    if ((unsigned int)(a3) != 0) goto loc_0034E50A;
    a2 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 296));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328)) >> (2);
loc_0034E274:
    if (result < result) goto loc_0034E5A5;
    if (result < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328) * 4)) goto loc_0034E58D;
loc_0034E28E:
    result = (result) >> (2);
    v_stack_p20 = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)((unsigned int)(v_r10))) >= result) goto loc_0034E608;
loc_0034E2A6:
loc_0034E2B8:
    v_r12 = (unsigned int)((0) + (*(unsigned int *)(a1 + 7216)));
    a1 = (4) - (4 - 3);
    if (condition_is_not_equal) goto loc_0034E2B8;
    if (0 == 0) goto loc_0034E3AF;
loc_0034E2CD:
    if (result <= 288) goto loc_0034E672;
loc_0034E2DF:
    if (0 != 0) goto loc_0034E694;
loc_0034E2EB:
    if (result < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328) * 4)) goto loc_0034E547;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328)) << (4);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328) * 4;
    if (result >= = a1) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 320);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 328) = result;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 296) = result;
    if (0 != 0) goto loc_0034E3F4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 288) != 0) goto loc_0034E6D6;
loc_0034E342:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 312)) << (2);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 336)) >= result) goto loc_0034E462;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274)) == 0) goto loc_0034E387;
    result = MiComputeAgeDistribution(a1, 4 - 3, a3, 0);
    v_r11 = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274) = (unsigned __int16)(result);
    if ((unsigned __int16)(result) != 0) goto loc_0034E460;
loc_0034E387:
    result = (result) >> (4);
    if (v_stack_p20 >= result) goto loc_0034E5D1;
    a1 = 0;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) { a1 = 8; }
    goto loc_0034E467;
loc_0034E3AF:
    if ((unsigned int)(a3) != 0) goto loc_0034E2CD;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - (*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 48)));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(0x20000ULL)))) goto loc_0034E63D;
    if ((unsigned int)(v_r10) == 0) goto loc_0034E2CD;
    if (((unsigned int)(result)) <= 0x18000ULL) goto loc_0034E2CD;
    a4 = (unsigned int)(v_stack_p8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 17600) + 336)) < ((unsigned int)(0x20000ULL))) { a4 = (unsigned int)(v_stack_p20); }
    v_stack_p8 = (unsigned int)(a4);
    goto loc_0034E2CD;
loc_0034E3F4:
    result = MiPulseLowAvailableEvent(a1, v_stack_p20, a3, a4);
    if (((unsigned __int8)(0 - 2)) <= 1) goto loc_0034E6CA;
loc_0034E40F:
    v_r11 = 0;
    *(unsigned __int8 *)(a2) = 0;
    *(unsigned __int64 *)(a2 + 96) = 0;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 40))) | (1));
    *(unsigned __int64 *)(a2 + 80) = 10;
    *(unsigned __int64 *)(a2 + 104) = 0;
    a1 = (*(unsigned __int64 *)(a1 + 18688)) + (10);
    *(unsigned __int64 *)(a2 + 72) = a1;
    *(unsigned __int8 *)(a2 + 2) = 0;
    *(unsigned __int64 *)(a2 + 8) = v_xmm0;
    *(unsigned __int64 *)(a2 + 24) = v_xmm0;
    *(unsigned __int64 *)(a2 + 40) = v_xmm0;
    *(unsigned __int64 *)(a2 + 56) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 17600) + 48) = (unsigned int)(v_r12);
    goto loc_0034E4D9;
loc_0034E460:
loc_0034E462:
loc_0034E467:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 276)) == 0) goto loc_0034E490;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 276)))) {
        *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 276));
    }
    if (11 == 0) {
        a1 = 12;
        *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 274) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 17600) + 276));
    }
    *(unsigned __int8 *)(a2) = 0;
    *(unsigned __int64 *)(a2 + 96) = 0;
    *(unsigned __int64 *)(a2 + 80) = 0;
    *(unsigned __int64 *)(a2 + 72) = *(unsigned __int64 *)(a1 + 18688);
    *(unsigned __int64 *)(a2 + 104) = 0;
    *(unsigned __int8 *)(a2 + 2) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(a2 + 8) = v_xmm0;
    *(unsigned __int64 *)(a2 + 24) = v_xmm0;
    *(unsigned __int64 *)(a2 + 40) = v_xmm0;
    *(unsigned __int64 *)(a2 + 56) = v_xmm0;
    if ((unsigned __int8)(a1) == 0) goto loc_0034E52F;
    v_r14 = (unsigned int)((v_r14) | (2));
loc_0034E4D9:
    if (result != 0) goto loc_0034E512;
loc_0034E4DE:
loc_0034E4E0:
    *(unsigned __int8 *)(a2 + 3) = 100;
    if (((1) & ((unsigned __int8)(v_r14))) == 0) goto loc_0034E523;
loc_0034E4E8:
    if (0 != 0) goto loc_0034E6EF;
loc_0034E4F1:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_r14));
loc_0034E50A:
    goto loc_0034E274;
loc_0034E512:
    if (0 >= result) goto loc_0034E4DE;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) * (v_stack_p70));
    a2 = 0;
    goto loc_0034E4E0;
loc_0034E523:
    if ((*(unsigned __int8 *)(a2 + 4)) != 2) goto loc_0034E4E8;
    *(unsigned __int8 *)(a2 + 4) = 1;
    goto loc_0034E4E8;
loc_0034E52F:
    if ((*(unsigned __int8 *)(v_stack_p10 + 55)) != 0) goto loc_0034E5C1;
    if ((unsigned int)(v_r14) == 0) { v_r14 = 32; }
    goto loc_0034E4D9;
loc_0034E547:
    if ((*(unsigned __int64 *)(v_stack_p10 + 128) * 4) < a1) goto loc_0034E6A9;
    if ((*(unsigned __int64 *)(v_stack_p10 + 128) + *(unsigned __int64 *)(v_stack_p10 + 128) * 1) <= a1) goto loc_0034E31A;
    *(unsigned __int64 *)(v_stack_p10 + 328) = *(unsigned __int64 *)(v_stack_p10 + 128) + *(unsigned __int64 *)(v_stack_p10 + 128) * 1;
    if ((*(unsigned __int64 *)(v_stack_p10 + 128) + *(unsigned __int64 *)(v_stack_p10 + 128) * 1) <= (*(unsigned __int64 *)(v_stack_p10 + 312))) goto loc_0034E31A;
loc_0034E58D:
    if (!sign_flag) goto loc_0034E28E;
    result = (*(unsigned __int64 *)(v_stack_p10 + 312)) - (1);
    if (result >= result) goto loc_0034E28E;
loc_0034E5A5:
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 312)) - (1);
    a1 = (a1) - (result);
    v_rdi = *(unsigned __int64 *)(v_stack_p10 + 312);
    if (a1 <= (*(unsigned __int64 *)(v_stack_p10 + 312))) { v_rdi = a1; }
    goto loc_0034E28E;
loc_0034E5C1:
    v_r14 = (unsigned int)((v_r14) | (64));
    *(unsigned __int16 *)(v_stack_p10 + 274) = (unsigned __int16)(v_rdi);
    goto loc_0034E4D9;
loc_0034E5D1:
    goto loc_0034E467;
loc_0034E5D8:
    if ((*(unsigned __int16 *)(v_stack_p10 + 276)) == 0) goto loc_0034E245;
    if ((*(unsigned __int8 *)(v_stack_p10 + 278)) == 0) goto loc_0034E245;
    if ((*(unsigned __int8 *)(v_stack_p10 + 279)) == 0) goto loc_0034E245;
    goto loc_0034E253;
loc_0034E608:
    a1 = (9) - (result);
    if (a1 <= v_rdi) goto loc_0034E2A6;
    if (v_rdi >= ((unsigned int)(0x2000ULL))) goto loc_0034E2A6;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12))) != 0) goto loc_0034E2A6;
    if (a1 > ((unsigned int)(0x2000ULL))) { a1 = (unsigned int)(0x2000ULL); }
    goto loc_0034E2A6;
loc_0034E63D:
    result = (*(unsigned __int64 *)(a1 + 18512)) >> (2);
    goto loc_0034E2CD;
loc_0034E672:
    result = (*(unsigned __int64 *)(v_stack_p10 + 312)) >> (1);
    if (((unsigned int)(0x8000ULL)) >= result) { result = (unsigned int)(0x8000ULL); }
    goto loc_0034E2DF;
loc_0034E694:
    if (result >= (*(unsigned __int64 *)(a1 + 18688))) goto loc_0034E2EB;
    v_rdi = result;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12))) == 0) { v_rdi = *(unsigned __int64 *)(a1 + 18688); }
    goto loc_0034E2EB;
loc_0034E6A9:
    *(unsigned __int64 *)(v_stack_p10 + 328) = result;
    if (result >= (*(unsigned __int64 *)(v_stack_p10 + 304))) goto loc_0034E31A;
loc_0034E6CA:
    *(unsigned __int64 *)(v_stack_p10 + 288) = v_rdi;
    goto loc_0034E40F;
loc_0034E6D6:
    *(unsigned __int64 *)(v_stack_p10 + 288) = 0;
    goto loc_0034E342;
loc_0034E6EF:
    a2 = 0;
    result = MiPruneProcessLargePageCaches(a1, a2, (unsigned int)((unsigned int)(v_r12)), a4);
    goto loc_0034E4F1;
}
```

## 5. (Beta) C Style

```c
int64_t MiComputeSystemTrimCriteria(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p70;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_r11 = 0;
    v_stack_p8 = 0;
    result = MiGetAvailablePagesForTrimPass(Arg1, Arg2, a3, 0);
loc_0034E1CE:
    Arg2 = (uint32_t)((0) + (*(uint32_t *)(arg1 + 0x1C24)));
    Arg1 = (local_r11 + 7) - (local_r11 + 1);
    if (condition_is_not_equal) goto loc_0034E1CE;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x2C)))));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x2C) = (uint32_t)(Arg2);
    local_r10 = (uint32_t)((local_r10) & ((uint32_t)(result)));
    a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148)) - (result);
    v_stack_p18 = (uint32_t)(local_r10);
    result = (result) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148));
    if (result > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148))) { a3 = result; }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x78))) & (7));
    Arg1 = (a3) >> (3);
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + arg2 * 8 + 0x88)) >> (3);
    Arg1 = (Arg1) - (result);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + arg2 * 8 + 0x88) = a3;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x50)) == 4) goto loc_0034E5D8;
loc_0034E245:
    a3 = 0;
    if (result <= 288) { a3 = (uint32_t)(local_r11 + 1); }
loc_0034E253:
    if ((uint32_t)(a3) != 0) goto loc_0034E50A;
    Arg2 = (result) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x128));
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148)) >> (2);
loc_0034E274:
    if (result < result) goto loc_0034E5A5;
    if (result < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148) * 4)) goto loc_0034E58D;
loc_0034E28E:
    result = (result) >> (2);
    v_stack_p20 = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)((uint32_t)(local_r10))) >= result) goto loc_0034E608;
loc_0034E2A6:
loc_0034E2B8:
    local_r12 = (uint32_t)((0) + (*(uint32_t *)(arg1 + 0x1C30)));
    Arg1 = (4) - (4 - 3);
    if (condition_is_not_equal) goto loc_0034E2B8;
    if (0 == 0) goto loc_0034E3AF;
loc_0034E2CD:
    if (result <= 288) goto loc_0034E672;
loc_0034E2DF:
    if (0 != 0) goto loc_0034E694;
loc_0034E2EB:
    if (result < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148) * 4)) goto loc_0034E547;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148)) << (4);
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148) * 4;
    if (result >= = Arg1) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x140);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x148) = result;
    }
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x128) = result;
    if (0 != 0) goto loc_0034E3F4;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x120) != 0) goto loc_0034E6D6;
loc_0034E342:
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x138)) << (2);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x150)) >= result) goto loc_0034E462;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112)) == 0) goto loc_0034E387;
    result = MiComputeAgeDistribution(Arg1, 4 - 3, a3, 0);
    local_r11 = 0;
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112) = (uint16_t)(result);
    if ((uint16_t)(result) != 0) goto loc_0034E460;
loc_0034E387:
    result = (result) >> (4);
    if (v_stack_p20 >= result) goto loc_0034E5D1;
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) { Arg1 = 8; }
    goto loc_0034E467;
loc_0034E3AF:
    if ((uint32_t)(a3) != 0) goto loc_0034E2CD;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - (*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x30)));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(0x20000ULL)))) goto loc_0034E63D;
    if ((uint32_t)(local_r10) == 0) goto loc_0034E2CD;
    if (((uint32_t)(result)) <= 0x18000ULL) goto loc_0034E2CD;
    a4 = (uint32_t)(v_stack_p8);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x150)) < ((uint32_t)(0x20000ULL))) { a4 = (uint32_t)(v_stack_p20); }
    v_stack_p8 = (uint32_t)(a4);
    goto loc_0034E2CD;
loc_0034E3F4:
    result = MiPulseLowAvailableEvent(Arg1, v_stack_p20, a3, a4);
    if (((uint8_t)(0 - 2)) <= 1) goto loc_0034E6CA;
loc_0034E40F:
    local_r11 = 0;
    *(uint8_t *)(arg2) = 0;
    *(uint64_t *)(arg2 + 0x60) = 0;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x28))) | (1));
    *(uint64_t *)(arg2 + 0x50) = 10;
    *(uint64_t *)(arg2 + 0x68) = 0;
    Arg1 = (*(uint64_t *)(arg1 + 0x4900)) + (10);
    *(void **)(arg2 + 0x48) = Arg1;
    *(uint8_t *)(arg2 + 0x2) = 0;
    *(uint64_t *)(arg2 + 0x8) = v_xmm0;
    *(uint64_t *)(arg2 + 0x18) = v_xmm0;
    *(uint64_t *)(arg2 + 0x28) = v_xmm0;
    *(uint64_t *)(arg2 + 0x38) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x30) = (uint32_t)(local_r12);
    goto loc_0034E4D9;
loc_0034E460:
loc_0034E462:
loc_0034E467:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x114)) == 0) goto loc_0034E490;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x114)))) {
        *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x114));
    }
    if (11 == 0) {
        Arg1 = 12;
        *(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x112) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x44C0) + 0x114));
    }
    *(uint8_t *)(arg2) = 0;
    *(uint64_t *)(arg2 + 0x60) = 0;
    *(uint64_t *)(arg2 + 0x50) = 0;
    *(uint64_t *)(arg2 + 0x48) = *(uint64_t *)(arg1 + 0x4900);
    *(uint64_t *)(arg2 + 0x68) = 0;
    *(uint8_t *)(arg2 + 0x2) = (uint8_t)(Arg1);
    *(uint64_t *)(arg2 + 0x8) = v_xmm0;
    *(uint64_t *)(arg2 + 0x18) = v_xmm0;
    *(uint64_t *)(arg2 + 0x28) = v_xmm0;
    *(uint64_t *)(arg2 + 0x38) = v_xmm0;
    if ((uint8_t)(Arg1) == 0) goto loc_0034E52F;
    local_r14 = (uint32_t)((local_r14) | (2));
loc_0034E4D9:
    if (result != 0) goto loc_0034E512;
loc_0034E4DE:
loc_0034E4E0:
    *(uint8_t *)(arg2 + 0x3) = 100;
    if (((1) & ((uint8_t)(local_r14))) == 0) goto loc_0034E523;
loc_0034E4E8:
    if (0 != 0) goto loc_0034E6EF;
loc_0034E4F1:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_r14));
loc_0034E50A:
    goto loc_0034E274;
loc_0034E512:
    if (0 >= result) goto loc_0034E4DE;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) * (v_stack_p70));
    Arg2 = 0;
    goto loc_0034E4E0;
loc_0034E523:
    if ((*(uint8_t *)(arg2 + 0x4)) != 2) goto loc_0034E4E8;
    *(uint8_t *)(arg2 + 0x4) = 1;
    goto loc_0034E4E8;
loc_0034E52F:
    if ((*(uint8_t *)(v_stack_p10 + 0x37)) != 0) goto loc_0034E5C1;
    if ((uint32_t)(local_r14) == 0) { local_r14 = 32; }
    goto loc_0034E4D9;
loc_0034E547:
    if ((*(uint64_t *)(v_stack_p10 + 0x80) * 4) < Arg1) goto loc_0034E6A9;
    if ((*(uint64_t *)(v_stack_p10 + 0x80) + *(uint64_t *)(v_stack_p10 + 0x80) * 1) <= Arg1) goto loc_0034E31A;
    *(uint64_t *)(v_stack_p10 + 0x148) = *(uint64_t *)(v_stack_p10 + 0x80) + *(uint64_t *)(v_stack_p10 + 0x80) * 1;
    if ((*(uint64_t *)(v_stack_p10 + 0x80) + *(uint64_t *)(v_stack_p10 + 0x80) * 1) <= (*(uint64_t *)(v_stack_p10 + 0x138))) goto loc_0034E31A;
loc_0034E58D:
    if (!sign_flag) goto loc_0034E28E;
    result = (*(uint64_t *)(v_stack_p10 + 0x138)) - (1);
    if (result >= result) goto loc_0034E28E;
loc_0034E5A5:
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x138)) - (1);
    Arg1 = (Arg1) - (result);
    local_rdi = *(uint64_t *)(v_stack_p10 + 0x138);
    if (Arg1 <= (*(uint64_t *)(v_stack_p10 + 0x138))) { local_rdi = Arg1; }
    goto loc_0034E28E;
loc_0034E5C1:
    local_r14 = (uint32_t)((local_r14) | (64));
    *(uint16_t *)(v_stack_p10 + 0x112) = (uint16_t)(local_rdi);
    goto loc_0034E4D9;
loc_0034E5D1:
    goto loc_0034E467;
loc_0034E5D8:
    if ((*(uint16_t *)(v_stack_p10 + 0x114)) == 0) goto loc_0034E245;
    if ((*(uint8_t *)(v_stack_p10 + 0x116)) == 0) goto loc_0034E245;
    if ((*(uint8_t *)(v_stack_p10 + 0x117)) == 0) goto loc_0034E245;
    goto loc_0034E253;
loc_0034E608:
    Arg1 = (9) - (result);
    if (Arg1 <= local_rdi) goto loc_0034E2A6;
    if (local_rdi >= ((uint32_t)(0x2000ULL))) goto loc_0034E2A6;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12))) != 0) goto loc_0034E2A6;
    if (Arg1 > ((uint32_t)(0x2000ULL))) { Arg1 = (uint32_t)(0x2000ULL); }
    goto loc_0034E2A6;
loc_0034E63D:
    result = (*(uint64_t *)(arg1 + 0x4850)) >> (2);
    goto loc_0034E2CD;
loc_0034E672:
    result = (*(uint64_t *)(v_stack_p10 + 0x138)) >> (1);
    if (((uint32_t)(0x8000ULL)) >= result) { result = (uint32_t)(0x8000ULL); }
    goto loc_0034E2DF;
loc_0034E694:
    if (result >= (*(uint64_t *)(arg1 + 0x4900))) goto loc_0034E2EB;
    local_rdi = result;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12))) == 0) { local_rdi = *(uint64_t *)(arg1 + 0x4900); }
    goto loc_0034E2EB;
loc_0034E6A9:
    *(uint64_t *)(v_stack_p10 + 0x148) = result;
    if (result >= (*(uint64_t *)(v_stack_p10 + 0x130))) goto loc_0034E31A;
loc_0034E6CA:
    *(uint64_t *)(v_stack_p10 + 0x120) = local_rdi;
    goto loc_0034E40F;
loc_0034E6D6:
    *(uint64_t *)(v_stack_p10 + 0x120) = 0;
    goto loc_0034E342;
loc_0034E6EF:
    Arg2 = 0;
    result = MiPruneProcessLargePageCaches(Arg1, Arg2, (uint32_t)((uint32_t)(local_r12)), a4);
    goto loc_0034E4F1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg1` | `+ 0x1C24` | `64` | `R` |
| `Arg1` | `+ 0x1C30` | `64` | `R` |
| `Arg1` | `+ 0x44C0` | `64` | `R` |
| `Arg1` | `+ 0x4850` | `64` | `R` |
| `Arg1` | `+ 0x4900` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `W` |
| `Arg2` | `+ 0x2` | `8` | `W` |
| `Arg2` | `+ 0x3` | `8` | `W` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x4` | `8` | `W` |
| `Arg2` | `+ 0x8` | `128` | `R` |
| `Arg2` | `+ 0x18` | `128` | `R` |
| `Arg2` | `+ 0x28` | `128` | `R` |
| `Arg2` | `+ 0x38` | `128` | `R` |
| `Arg2` | `+ 0x48` | `64` | `W` |
| `Arg2` | `+ 0x50` | `64` | `W` |
| `Arg2` | `+ 0x60` | `64` | `W` |
| `Arg2` | `+ 0x68` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034E184&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
