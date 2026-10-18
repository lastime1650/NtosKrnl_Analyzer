# MiAddZeroingThreads

- RVA: `0x002CBF78`–`0x002CC4B4` (길이 `1,340` bytes)
- VA: `0x00000001402CBF78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F424`
- 디코드: `324`개 명령, `1,340/1,340` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002CBFBC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002CC038` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x002CC0AB` → [MiGetEngineBackgroundQualifications](MiGetEngineBackgroundQualifications_function_002CC4BC.md) (function, `0x002CC4BC`)
- `0x002CC171` → [MiFindBestZeroingProcessor](MiFindBestZeroingProcessor_function_002CC73C.md) (function, `0x002CC73C`)
- `0x002CC1E2` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002CC2DF` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002CC34E` → [MiIncrementZeroEngineThread](MiIncrementZeroEngineThread_function_002CBB80.md) (function, `0x002CBB80`)
- `0x002CC35F` → [MiUnlinkZeroThreadFromActiveDomain](MiUnlinkZeroThreadFromActiveDomain_function_002CCB9C.md) (function, `0x002CCB9C`)
- `0x002CC37A` → [MiAssignBackgroundZeroThreadToProcessor](MiAssignBackgroundZeroThreadToProcessor_function_002CCAAC.md) (function, `0x002CCAAC`)
- `0x002CC386` → [MiRestartZeroingPass](MiRestartZeroingPass_function_002CBB54.md) (function, `0x002CBB54`)
- `0x002CC428` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)

### Direct callers
- [MiReassessZeroThreads](MiReassessZeroThreads_function_002CB0C0.md) at `0x002CB31B`
- [MiWakeZeroingThreads](MiWakeZeroingThreads_function_002CBEC0.md) at `0x002CBEF9`

### Static image references
- `0x002CBF94` → RVA `0x00E0A740` (`.data`; read)
- `0x002CC019` → RVA `0x00E2DBF8` (`.data`; read)
- `0x002CC27C` → RVA `0x00EF5050` (`.data`; read)
- `0x002CC2CF` → RVA `0x00EF5004` (`.data`; read/write)
- `0x002CC3B9` → RVA `0x00EF500C` (`.data`; read/write)
- `0x002CC3E9` → RVA `0x00EF5008` (`.data`; read/write)
- `0x002CC3FC` → RVA `0x00EF5000` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CBF78  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
002CBF7D  55                              push rbp
002CBF7E  56                              push rsi
002CBF7F  57                              push rdi
002CBF80  41 54                           push r12
002CBF82  41 55                           push r13
002CBF84  41 56                           push r14
002CBF86  41 57                           push r15
002CBF88  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
002CBF8D  48 81 EC 20 01 00 00            sub rsp, 0x120
002CBF94  48 8B 05 A5 E7 B3 00            mov rax, qword ptr [rip + 0xb3e7a5]
002CBF9B  48 33 C4                        xor rax, rsp
002CBF9E  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002CBFA2  49 8B F0                        mov rsi, r8
002CBFA5  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
002CBFAA  8B DA                           mov ebx, edx
002CBFAC  4C 8B F1                        mov r14, rcx
002CBFAF  33 D2                           xor edx, edx
002CBFB1  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002CBFB6  41 B8 A8 00 00 00               mov r8d, 0xa8
002CBFBC  E8 7F AC 3F 00                  call 0x1406c6c40
002CBFC1  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
002CBFC5  33 C9                           xor ecx, ecx
002CBFC7  0F 57 C0                        xorps xmm0, xmm0
002CBFCA  66 89 4C 24 20                  mov word ptr [rsp + 0x20], cx
002CBFCF  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
002CBFD4  44 8B B8 54 42 00 00            mov r15d, dword ptr [rax + 0x4254]
002CBFDB  8D 41 02                        lea eax, [rcx + 2]
002CBFDE  41 83 FF 01                     cmp r15d, 1
002CBFE2  0F 85 18 03 00 00               jne 0x1402cc300
002CBFE8  83 FB 03                        cmp ebx, 3
002CBFEB  8B F9                           mov edi, ecx
002CBFED  0F 45 FB                        cmovne edi, ebx
002CBFF0  89 3E                           mov dword ptr [rsi], edi
002CBFF2  44 8B E1                        mov r12d, ecx
002CBFF5  48 8B F1                        mov rsi, rcx
002CBFF8  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002CBFFC  41 83 FF 01                     cmp r15d, 1
002CC000  48 0F 45 C1                     cmovne rax, rcx
002CC004  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002CC009  48 63 C7                        movsxd rax, edi
002CC00C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002CC011  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
002CC015  48 8D 0C 40                     lea rcx, [rax + rax*2]
002CC019  48 8B 05 D8 1B B6 00            mov rax, qword ptr [rip + 0xb61bd8]
002CC020  48 C1 E1 07                     shl rcx, 7
002CC024  48 8B 9C 01 78 01 00 00         mov rbx, qword ptr [rcx + rax + 0x178]
002CC02C  4C 8D 6B 40                     lea r13, [rbx + 0x40]
002CC030  49 8B CD                        mov rcx, r13
002CC033  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
002CC038  E8 F3 CD F7 FF                  call 0x140248e30
002CC03D  4C 69 5C 24 30 30 01 00 00      imul r11, qword ptr [rsp + 0x30], 0x130
002CC046  45 33 C9                        xor r9d, r9d
002CC049  4C 8D 55 88                     lea r10, [rbp - 0x78]
002CC04D  48 81 C3 87 00 00 00            add rbx, 0x87
002CC054  4D 8D 86 94 00 00 00            lea r8, [r14 + 0x94]
002CC05B  41 83 78 FC 00                  cmp dword ptr [r8 - 4], 0
002CC060  41 C7 02 05 00 00 00            mov dword ptr [r10], 5
002CC067  0F 85 32 01 00 00               jne 0x1402cc19f
002CC06D  49 FF C1                        inc r9
002CC070  49 83 C2 38                     add r10, 0x38
002CC074  49 81 C0 30 01 00 00            add r8, 0x130
002CC07B  48 81 C3 A8 00 00 00            add rbx, 0xa8
002CC082  49 83 F9 03                     cmp r9, 3
002CC086  7C D3                           jl 0x1402cc05b
002CC088  48 85 F6                        test rsi, rsi
002CC08B  0F 84 94 03 00 00               je 0x1402cc425
002CC091  49 8D 8E 88 00 00 00            lea rcx, [r14 + 0x88]
002CC098  44 03 61 0C                     add r12d, dword ptr [rcx + 0xc]
002CC09C  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
002CC0A1  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
002CC0A6  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
002CC0AB  E8 0C 04 00 00                  call 0x1402cc4bc
002CC0B0  8B 5D 88                        mov ebx, dword ptr [rbp - 0x78]
002CC0B3  48 83 C9 FF                     or rcx, 0xffffffffffffffff
002CC0B7  85 DB                           test ebx, ebx
002CC0B9  0F 84 20 01 00 00               je 0x1402cc1df
002CC0BF  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002CC0C4  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
002CC0C9  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
002CC0CE  4C 8B EB                        mov r13, rbx
002CC0D1  48 85 DB                        test rbx, rbx
002CC0D4  0F 84 AC 00 00 00               je 0x1402cc186
002CC0DA  4C 69 D3 30 01 00 00            imul r10, rbx, 0x130
002CC0E1  48 6B F3 38                     imul rsi, rbx, 0x38
002CC0E5  49 81 C2 88 00 00 00            add r10, 0x88
002CC0EC  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
002CC0F1  4D 03 D6                        add r10, r14
002CC0F4  41 8B 42 0C                     mov eax, dword ptr [r10 + 0xc]
002CC0F8  4C 03 DE                        add r11, rsi
002CC0FB  41 8B 4A 04                     mov ecx, dword ptr [r10 + 4]
002CC0FF  44 03 E0                        add r12d, eax
002CC102  41 C7 43 28 05 00 00 00         mov dword ptr [r11 + 0x28], 5
002CC10A  85 C9                           test ecx, ecx
002CC10C  74 68                           je 0x1402cc176
002CC10E  3B C8                           cmp ecx, eax
002CC110  0F 84 E6 02 00 00               je 0x1402cc3fc
002CC116  41 3B 42 08                     cmp eax, dword ptr [r10 + 8]
002CC11A  73 5A                           jae 0x1402cc176
002CC11C  49 8B 82 B0 00 00 00            mov rax, qword ptr [r10 + 0xb0]
002CC123  4D 63 0A                        movsxd r9, dword ptr [r10]
002CC126  8B 48 38                        mov ecx, dword ptr [rax + 0x38]
002CC129  48 8B 05 C8 1A B6 00            mov rax, qword ptr [rip + 0xb61ac8]
002CC130  48 8D 14 49                     lea rdx, [rcx + rcx*2]
002CC134  48 C1 E2 07                     shl rdx, 7
002CC138  49 69 C9 A8 00 00 00            imul rcx, r9, 0xa8
002CC13F  80 7C 24 20 00                  cmp byte ptr [rsp + 0x20], 0
002CC144  4C 8B 84 02 78 01 00 00         mov r8, qword ptr [rdx + rax + 0x178]
002CC14C  4A 8B 94 01 90 00 00 00         mov rdx, qword ptr [rcx + r8 + 0x90]
002CC154  0F 85 4A 02 00 00               jne 0x1402cc3a4
002CC15A  80 7C 24 21 00                  cmp byte ptr [rsp + 0x21], 0
002CC15F  0F 85 6A 02 00 00               jne 0x1402cc3cf
002CC165  45 33 C9                        xor r9d, r9d
002CC168  45 33 C0                        xor r8d, r8d
002CC16B  49 8B D2                        mov rdx, r10
002CC16E  49 8B CB                        mov rcx, r11
002CC171  E8 C6 05 00 00                  call 0x1402cc73c
002CC176  83 7C 35 88 00                  cmp dword ptr [rbp + rsi - 0x78], 0
002CC17B  74 56                           je 0x1402cc1d3
002CC17D  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
002CC182  48 83 C9 FF                     or rcx, 0xffffffffffffffff
002CC186  48 3B D8                        cmp rbx, rax
002CC189  74 48                           je 0x1402cc1d3
002CC18B  BB 01 00 00 00                  mov ebx, 1
002CC190  44 3B FB                        cmp r15d, ebx
002CC193  48 0F 45 D9                     cmovne rbx, rcx
002CC197  49 03 DD                        add rbx, r13
002CC19A  E9 2F FF FF FF                  jmp 0x1402cc0ce
002CC19F  47 03 A4 33 94 00 00 00         add r12d, dword ptr [r11 + r14 + 0x94]
002CC1A7  48 8D 73 F9                     lea rsi, [rbx - 7]
002CC1AB  41 8B 00                        mov eax, dword ptr [r8]
002CC1AE  33 D2                           xor edx, edx
002CC1B0  4D 85 C9                        test r9, r9
002CC1B3  0F 95 C2                        setne dl
002CC1B6  48 0F AF 43 09                  imul rax, qword ptr [rbx + 9]
002CC1BB  48 01 44 D4 38                  add qword ptr [rsp + rdx*8 + 0x38], rax
002CC1C0  80 3B 00                        cmp byte ptr [rbx], 0
002CC1C3  0F 84 A4 FE FF FF               je 0x1402cc06d
002CC1C9  C6 44 14 20 01                  mov byte ptr [rsp + rdx + 0x20], 1
002CC1CE  E9 9A FE FF FF                  jmp 0x1402cc06d
002CC1D3  8B 5D 88                        mov ebx, dword ptr [rbp - 0x78]
002CC1D6  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002CC1DA  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
002CC1DF  49 8B CD                        mov rcx, r13
002CC1E2  E8 A9 E3 F7 FF                  call 0x14024a590
002CC1E7  45 33 ED                        xor r13d, r13d
002CC1EA  41 8B CD                        mov ecx, r13d
002CC1ED  85 DB                           test ebx, ebx
002CC1EF  0F 84 25 02 00 00               je 0x1402cc41a
002CC1F5  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
002CC1FA  41 8D 55 05                     lea edx, [r13 + 5]
002CC1FE  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
002CC203  8D 4A FE                        lea ecx, [rdx - 2]
002CC206  41 83 FF 01                     cmp r15d, 1
002CC20A  4C 8B C6                        mov r8, rsi
002CC20D  41 0F 45 CD                     cmovne ecx, r13d
002CC211  44 8B D7                        mov r10d, edi
002CC214  4D 8B D8                        mov r11, r8
002CC217  85 FF                           test edi, edi
002CC219  74 13                           je 0x1402cc22e
002CC21B  49 6B C0 38                     imul rax, r8, 0x38
002CC21F  44 8B 4C 05 88                  mov r9d, dword ptr [rbp + rax - 0x78]
002CC224  41 83 F9 05                     cmp r9d, 5
002CC228  0F 85 D9 01 00 00               jne 0x1402cc407
002CC22E  4C 3B C3                        cmp r8, rbx
002CC231  74 25                           je 0x1402cc258
002CC233  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002CC23A  BF 01 00 00 00                  mov edi, 1
002CC23F  44 3B FF                        cmp r15d, edi
002CC242  0F 45 F8                        cmovne edi, eax
002CC245  41 03 FA                        add edi, r10d
002CC248  44 8D 40 02                     lea r8d, [rax + 2]
002CC24C  45 3B F8                        cmp r15d, r8d
002CC24F  4C 0F 45 C0                     cmovne r8, rax
002CC253  4D 03 C3                        add r8, r11
002CC256  EB B9                           jmp 0x1402cc211
002CC258  8B 5D 88                        mov ebx, dword ptr [rbp - 0x78]
002CC25B  83 FB 05                        cmp ebx, 5
002CC25E  0F 85 2E 01 00 00               jne 0x1402cc392
002CC264  45 8B CD                        mov r9d, r13d
002CC267  83 FA 05                        cmp edx, 5
002CC26A  0F 85 C7 01 00 00               jne 0x1402cc437
002CC270  B9 03 00 00 00                  mov ecx, 3
002CC275  44 8D 49 FF                     lea r9d, [rcx - 1]
002CC279  48 63 C2                        movsxd rax, edx
002CC27C  48 8D 15 CD 8D C2 00            lea rdx, [rip + 0xc28dcd]
002CC283  FF 04 82                        inc dword ptr [rdx + rax*4]
002CC286  83 F9 03                        cmp ecx, 3
002CC289  75 7C                           jne 0x1402cc307
002CC28B  41 8B C5                        mov eax, r13d
002CC28E  49 8D 96 94 00 00 00            lea rdx, [r14 + 0x94]
002CC295  49 8B CD                        mov rcx, r13
002CC298  44 39 2A                        cmp dword ptr [rdx], r13d
002CC29B  75 12                           jne 0x1402cc2af
002CC29D  FF C0                           inc eax
002CC29F  48 FF C1                        inc rcx
002CC2A2  48 81 C2 30 01 00 00            add rdx, 0x130
002CC2A9  48 83 F9 03                     cmp rcx, 3
002CC2AD  7C E9                           jl 0x1402cc298
002CC2AF  83 F8 03                        cmp eax, 3
002CC2B2  75 1B                           jne 0x1402cc2cf
002CC2B4  41 8B 4E 38                     mov ecx, dword ptr [r14 + 0x38]
002CC2B8  4C 69 C1 80 DF 00 00            imul r8, rcx, 0xdf80
002CC2BF  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
002CC2C3  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
002CC2C7  45 88 AC 10 C0 3B 00 00         mov byte ptr [r8 + rdx + 0x3bc0], r13b
002CC2CF  FF 05 2F 8D C2 00               inc dword ptr [rip + 0xc28d2f]
002CC2D5  41 8B C1                        mov eax, r9d
002CC2D8  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
002CC2DC  48 33 CC                        xor rcx, rsp
002CC2DF  E8 5C 03 3E 00                  call 0x1406ac640
002CC2E4  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
002CC2EC  48 81 C4 20 01 00 00            add rsp, 0x120
002CC2F3  41 5F                           pop r15
002CC2F5  41 5E                           pop r14
002CC2F7  41 5D                           pop r13
002CC2F9  41 5C                           pop r12
002CC2FB  5F                              pop rdi
002CC2FC  5E                              pop rsi
002CC2FD  5D                              pop rbp
002CC2FE  C3                              ret
002CC2FF  CC                              int3
002CC300  8B F8                           mov edi, eax
002CC302  E9 E9 FC FF FF                  jmp 0x1402cbff0
002CC307  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002CC30C  48 63 F1                        movsxd rsi, ecx
002CC30F  48 69 FE 30 01 00 00            imul rdi, rsi, 0x130
002CC316  89 08                           mov dword ptr [rax], ecx
002CC318  49 03 FE                        add rdi, r14
002CC31B  48 8D 97 48 01 00 00            lea rdx, [rdi + 0x148]
002CC322  48 8B 0A                        mov rcx, qword ptr [rdx]
002CC325  48 3B CA                        cmp rcx, rdx
002CC328  0F 84 96 00 00 00               je 0x1402cc3c4
002CC32E  48 8D 99 60 FE FF FF            lea rbx, [rcx - 0x1a0]
002CC335  8B 83 80 01 00 00               mov eax, dword ptr [rbx + 0x180]
002CC33B  24 06                           and al, 6
002CC33D  3C 02                           cmp al, 2
002CC33F  0F 85 AF 00 00 00               jne 0x1402cc3f4
002CC345  FF 87 A0 01 00 00               inc dword ptr [rdi + 0x1a0]
002CC34B  48 8B CB                        mov rcx, rbx
002CC34E  E8 2D F8 FF FF                  call 0x1402cbb80
002CC353  4C 39 AB B0 01 00 00            cmp qword ptr [rbx + 0x1b0], r13
002CC35A  74 08                           je 0x1402cc364
002CC35C  48 8B CB                        mov rcx, rbx
002CC35F  E8 38 08 00 00                  call 0x1402ccb9c
002CC364  48 6B C6 38                     imul rax, rsi, 0x38
002CC368  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
002CC36D  48 8B CB                        mov rcx, rbx
002CC370  4C 03 C0                        add r8, rax
002CC373  48 8D 97 88 00 00 00            lea rdx, [rdi + 0x88]
002CC37A  E8 2D 07 00 00                  call 0x1402ccaac
002CC37F  48 8D 8F 88 00 00 00            lea rcx, [rdi + 0x88]
002CC386  E8 C9 F7 FF FF                  call 0x1402cbb54
002CC38B  33 C0                           xor eax, eax
002CC38D  E9 46 FF FF FF                  jmp 0x1402cc2d8
002CC392  3B DA                           cmp ebx, edx
002CC394  0F 8F CA FE FF FF               jg 0x1402cc264
002CC39A  8B D3                           mov edx, ebx
002CC39C  41 8B CD                        mov ecx, r13d
002CC39F  E9 C0 FE FF FF                  jmp 0x1402cc264
002CC3A4  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002CC3A9  48 03 C2                        add rax, rdx
002CC3AC  49 3B 80 40 02 00 00            cmp rax, qword ptr [r8 + 0x240]
002CC3B3  0F 86 A1 FD FF FF               jbe 0x1402cc15a
002CC3B9  FF 05 4D 8C C2 00               inc dword ptr [rip + 0xc28c4d]
002CC3BF  E9 B2 FD FF FF                  jmp 0x1402cc176
002CC3C4  41 B9 02 00 00 00               mov r9d, 2
002CC3CA  E9 00 FF FF FF                  jmp 0x1402cc2cf
002CC3CF  48 8D 04 17                     lea rax, [rdi + rdx]
002CC3D3  49 3B 80 48 02 00 00            cmp rax, qword ptr [r8 + 0x248]
002CC3DA  0F 86 85 FD FF FF               jbe 0x1402cc165
002CC3E0  45 85 C9                        test r9d, r9d
002CC3E3  0F 84 7C FD FF FF               je 0x1402cc165
002CC3E9  FF 05 19 8C C2 00               inc dword ptr [rip + 0xc28c19]
002CC3EF  E9 82 FD FF FF                  jmp 0x1402cc176
002CC3F4  48 8B 09                        mov rcx, qword ptr [rcx]
002CC3F7  E9 29 FF FF FF                  jmp 0x1402cc325
002CC3FC  FF 05 FE 8B C2 00               inc dword ptr [rip + 0xc28bfe]
002CC402  E9 6F FD FF FF                  jmp 0x1402cc176
002CC407  44 3B CA                        cmp r9d, edx
002CC40A  0F 8D 1E FE FF FF               jge 0x1402cc22e
002CC410  41 8B D1                        mov edx, r9d
002CC413  8B CF                           mov ecx, edi
002CC415  E9 14 FE FF FF                  jmp 0x1402cc22e
002CC41A  41 8B D5                        mov edx, r13d
002CC41D  45 8B CD                        mov r9d, r13d
002CC420  E9 54 FE FF FF                  jmp 0x1402cc279
002CC425  49 8B CD                        mov rcx, r13
002CC428  E8 63 E1 F7 FF                  call 0x14024a590
002CC42D  B8 04 00 00 00                  mov eax, 4
002CC432  E9 A1 FE FF FF                  jmp 0x1402cc2d8
002CC437  83 FA 04                        cmp edx, 4
002CC43A  0F 85 39 FE FF FF               jne 0x1402cc279
002CC440  45 85 E4                        test r12d, r12d
002CC443  74 0A                           je 0x1402cc44f
002CC445  BA 05 00 00 00                  mov edx, 5
002CC44A  E9 21 FE FF FF                  jmp 0x1402cc270
002CC44F  41 B9 03 00 00 00               mov r9d, 3
002CC455  45 8D 59 FF                     lea r11d, [r9 - 1]
002CC459  41 83 FF 01                     cmp r15d, 1
002CC45D  0F 84 16 FE FF FF               je 0x1402cc279
002CC463  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
002CC468  49 8D 86 F4 02 00 00            lea rax, [r14 + 0x2f4]
002CC46F  45 8B C3                        mov r8d, r11d
002CC472  44 8B 50 F8                     mov r10d, dword ptr [rax - 8]
002CC476  45 85 D2                        test r10d, r10d
002CC479  74 22                           je 0x1402cc49d
002CC47B  8B 18                           mov ebx, dword ptr [rax]
002CC47D  44 3B D3                        cmp r10d, ebx
002CC480  75 25                           jne 0x1402cc4a7
002CC482  FF 05 78 8B C2 00               inc dword ptr [rip + 0xc28b78]
002CC488  4C 3B C6                        cmp r8, rsi
002CC48B  0F 84 E8 FD FF FF               je 0x1402cc279
002CC491  41 FF CB                        dec r11d
002CC494  49 FF C8                        dec r8
002CC497  48 2D 30 01 00 00               sub rax, 0x130
002CC49D  4C 3B C7                        cmp r8, rdi
002CC4A0  75 D0                           jne 0x1402cc472
002CC4A2  E9 D2 FD FF FF                  jmp 0x1402cc279
002CC4A7  3B 58 FC                        cmp ebx, dword ptr [rax - 4]
002CC4AA  73 DC                           jae 0x1402cc488
002CC4AC  41 8B CB                        mov ecx, r11d
002CC4AF  45 8B CD                        mov r9d, r13d
002CC4B2  EB D4                           jmp 0x1402cc488
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddZeroingThreads(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int8 v_stack_m137;
    unsigned __int16 v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 11790245)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m108 = a3;
    a2 = 0;
    result = memset(v_stack_mF8, a2, 168, a4);
    a1 = 0;
    v_stack_m138 = 0;
    v_stack_m120 = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) != 1) goto loc_002CC300;
    v_rdi = 0;
    if (((unsigned int)((unsigned int)(a2))) != 3) { v_rdi = (unsigned int)((unsigned int)(a2)); }
loc_002CBFF0:
    *(unsigned int *)(a3) = (unsigned int)(v_rdi);
    v_stack_m134 = (unsigned int)(v_rdi);
    result = a1 + 2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) != 1) { result = 0; }
    v_stack_m130 = result;
    v_stack_m128 = (int)((unsigned int)(v_rdi));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 56)) + (unsigned int)(*(unsigned int *)(a1 + 56)) * 2) << (7);
    v_stack_m110 = *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11934680) * 1 + 376) + 64;
    result = ExAcquireSpinLockSharedAtDpcLevel(*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11934680) * 1 + 376) + 64, a2, 168, a4);
    v_r11 = (v_r11) * (v_stack_m128);
    a4 = 0;
    v_rbx = (*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11934680) * 1 + 376)) + (135);
loc_002CC05B:
    *(unsigned int *)(v_stack_mD0) = 5;
    if ((*(unsigned int *)(a1 + 148 - 4)) != 0) goto loc_002CC19F;
loc_002CC06D:
    a4 = (a4) + 1;
    v_r10 = (v_stack_mD0) + (56);
    a3 = (a1 + 148) + (304);
    v_rbx = (v_rbx) + (168);
    if (a4 < 3) goto loc_002CC05B;
    if (0 == 0) goto loc_002CC425;
    v_r12 = (unsigned int)((0) + (*(unsigned int *)(a1 + 136 + 12)));
    result = MiGetEngineBackgroundQualifications(a1 + 136, v_stack_m138, v_stack_m120, v_stack_mF8);
    a1 = (a1 + 136) | (-1);
    if ((unsigned int)((unsigned int)(v_stack_mD0)) == 0) goto loc_002CC1DF;
loc_002CC0CE:
    if (v_stack_m128 == 0) goto loc_002CC186;
    v_r10 = (v_r10) * (v_stack_m128);
    v_rsi = (0) * (v_stack_m128);
    v_r10 = (v_r10) + (136);
    v_r10 = (v_r10) + (a1);
    v_r11 = (v_stack_mF8) + (v_rsi);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 12)))));
    *(unsigned int *)(v_r11 + 40) = 5;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 4))) == 0) goto loc_002CC176;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 4)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 12))))) goto loc_002CC3FC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 12)))) >= (*(unsigned int *)(v_r10 + 8))) goto loc_002CC176;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r10 + 176) + 56)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r10 + 176) + 56)) * 2) << (7);
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r10 + 176) + 56))) * ((int)(*(unsigned int *)(v_r10)));
    if (v_stack_m138 != 0) goto loc_002CC3A4;
loc_002CC15A:
    if (v_stack_m137 != 0) goto loc_002CC3CF;
loc_002CC165:
    a4 = 0;
    a3 = 0;
    result = MiFindBestZeroingProcessor(v_r11, v_r10, a3, a4);
loc_002CC176:
    if ((*(unsigned int *)(v_stack_m58 + v_rsi * 1 - 120)) == 0) goto loc_002CC1D3;
    a1 = (v_r11) | (-1);
loc_002CC186:
    if (v_stack_m128 == v_stack_m130) goto loc_002CC1D3;
    v_rbx = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) != 1) { v_rbx = a1; }
    v_rbx = (v_rbx) + (v_stack_m128);
    goto loc_002CC0CE;
loc_002CC19F:
    v_r12 = (unsigned int)((v_r12) + (*(unsigned int *)(v_r11 + a1 * 1 + 148)));
    a2 = 0;
    a2 = (0 != 0) ? 1 : 0;
    result = ((unsigned int)(*(unsigned int *)(a3))) * (*(unsigned __int64 *)(v_rbx + 9));
    if ((*(unsigned __int8 *)(v_rbx)) == 0) goto loc_002CC06D;
    *(unsigned __int8 *)(v_rsp + a2 * 1 + 32) = 1;
    goto loc_002CC06D;
loc_002CC1D3:
loc_002CC1DF:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_stack_m110, a2, a3, a4);
    v_r13 = 0;
    if ((unsigned int)((unsigned int)(v_stack_mD0)) == 0) goto loc_002CC41A;
    a1 = v_r13 + 5 - 2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) != 1) { a1 = 0; }
loc_002CC211:
    if ((unsigned int)((unsigned int)(v_stack_m134)) == 0) goto loc_002CC22E;
    result = (result) * (v_stack_m128);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + result * 1 - 120)))) != 5) goto loc_002CC407;
loc_002CC22E:
    if (v_stack_m128 == v_stack_m130) goto loc_002CC258;
    v_rdi = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) != 1) { v_rdi = -1; }
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m134))))));
    a3 = -1 + 2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) != ((unsigned int)(-1 + 2))) { a3 = -1; }
    a3 = (a3) + (v_stack_m128);
    goto loc_002CC211;
loc_002CC258:
    if (((unsigned int)((unsigned int)(v_stack_mD0))) != 5) goto loc_002CC392;
loc_002CC264:
    if (((unsigned int)(v_r13 + 5)) != 5) goto loc_002CC437;
loc_002CC270:
loc_002CC279:
    if (3 != 3) goto loc_002CC307;
loc_002CC298:
    if ((*(unsigned int *)(a1 + 148)) != 0) goto loc_002CC2AF;
    result = (unsigned int)((0) + 1);
    a1 = (0) + 1;
    a2 = (a1 + 148) + (304);
    if (a1 < 3) goto loc_002CC298;
loc_002CC2AF:
    if (((unsigned int)(result)) == 3) {
        a1 = *(unsigned int *)(a1 + 56);
        a3 = (a3) * (a1);
        a1 = *(unsigned __int64 *)(a1 + 48);
        a2 = *(unsigned __int64 *)(a1 + 16);
        *(unsigned __int8 *)(a3 + a2 * 1 + 15296) = 0;
    }
loc_002CC2D8:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 3 - 1);
    v_rsp = (v_rsp) + (288);
    return result;
loc_002CC300:
    goto loc_002CBFF0;
loc_002CC307:
    v_rdi = ((unsigned int)((unsigned int)(result))) * ((int)((unsigned int)(a1)));
    *(unsigned int *)(v_stack_p50) = (unsigned int)(a1);
    v_rdi = (v_rdi) + (a1);
loc_002CC325:
    if ((*(unsigned __int64 *)(v_rdi + 328)) == (v_rdi + 328)) goto loc_002CC3C4;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 328) - 416 + 384))) & (6));
    if (((unsigned __int8)(result)) != 2) goto loc_002CC3F4;
    result = MiIncrementZeroEngineThread(*(unsigned __int64 *)(v_rdi + 328) - 416, v_rdi + 328, a3, 3 - 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 328) - 416 + 432)) != 0) {
        a1 = *(unsigned __int64 *)(v_rdi + 328) - 416;
        result = MiUnlinkZeroThreadFromActiveDomain(a1, v_rdi + 328, a3, 3 - 1);
    }
    result = (result) * ((int)((unsigned int)(a1)));
    a3 = (v_stack_p60) + (result);
    result = MiAssignBackgroundZeroThreadToProcessor(*(unsigned __int64 *)(v_rdi + 328) - 416, v_rdi + 136, a3, 3 - 1);
    result = MiRestartZeroingPass(v_rdi + 136, v_rdi + 136, a3, 3 - 1);
    result = 0;
    goto loc_002CC2D8;
loc_002CC392:
    if (((unsigned int)(*(unsigned __int64 *)(v_rdi + 328) - 416)) > ((unsigned int)(v_rdi + 136))) goto loc_002CC264;
    goto loc_002CC264;
loc_002CC3A4:
    result = (v_stack_p38) + ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rdi + 328) - 416)));
    if (result <= (*(unsigned __int64 *)(a3 + 576))) goto loc_002CC15A;
    goto loc_002CC176;
loc_002CC3C4:
    goto loc_002CC2CF;
loc_002CC3CF:
    if ((v_rdi + (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rdi + 328) - 416)) * 1) <= (*(unsigned __int64 *)(a3 + 584))) goto loc_002CC165;
    if (2 == 0) goto loc_002CC165;
    goto loc_002CC176;
loc_002CC3F4:
    goto loc_002CC325;
loc_002CC3FC:
    goto loc_002CC176;
loc_002CC407:
    if (2 >= ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rdi + 328) - 416))))) goto loc_002CC22E;
    goto loc_002CC22E;
loc_002CC41A:
    goto loc_002CC279;
loc_002CC425:
    result = ExReleaseSpinLockSharedFromDpcLevel(0, 0, a3, 0);
    goto loc_002CC2D8;
loc_002CC437:
    if (0 != 4) goto loc_002CC279;
    if ((unsigned int)(v_r12) == 0) goto loc_002CC44F;
    goto loc_002CC270;
loc_002CC44F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 16980)))) == 1) goto loc_002CC279;
loc_002CC472:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 756 - 8))) == 0) goto loc_002CC49D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 756 - 8)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 756))))) goto loc_002CC4A7;
loc_002CC488:
    if (((unsigned int)((unsigned int)(3 - 1))) == ((int)((unsigned int)(a1)))) goto loc_002CC279;
    v_r11 = (unsigned int)((3 - 1) - 1);
    a3 = ((unsigned int)((unsigned int)(3 - 1))) - 1;
    result = (a1 + 756) - (304);
loc_002CC49D:
    if (a3 != v_stack_p28) goto loc_002CC472;
    goto loc_002CC279;
loc_002CC4A7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 756)))) >= (*(unsigned int *)(result - 4))) goto loc_002CC488;
    goto loc_002CC488;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddZeroingThreads(void *Arg1, int32_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint8_t v_stack_m137;
    uint16_t v_stack_m138;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p38;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0xB3E7A5)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m108 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 168, Arg4);
    Arg1 = 0;
    v_stack_m138 = 0;
    v_stack_m120 = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) != 1) goto loc_002CC300;
    local_rdi = 0;
    if (((uint32_t)((uint32_t)(Arg2))) != 3) { local_rdi = (uint32_t)((uint32_t)(Arg2)); }
loc_002CBFF0:
    *(uint32_t *)(arg3) = (uint32_t)(local_rdi);
    v_stack_m134 = (uint32_t)(local_rdi);
    result = Arg1 + 2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) != 1) { result = 0; }
    v_stack_m130 = result;
    v_stack_m128 = (int32_t)((uint32_t)(local_rdi));
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x38)) + (uint32_t)(*(uint32_t *)(arg1 + 0x38)) * 2) << (7);
    v_stack_m110 = *(uint64_t *)(arg1 + *(uint64_t *)(v_rip + 0xB61BD8) * 1 + 0x178) + 64;
    result = ExAcquireSpinLockSharedAtDpcLevel(*(uint64_t *)(arg1 + *(uint64_t *)(v_rip + 0xB61BD8) * 1 + 0x178) + 64, Arg2, 168, Arg4);
    local_r11 = (local_r11) * (v_stack_m128);
    Arg4 = 0;
    local_rbx = (*(uint64_t *)(arg1 + *(uint64_t *)(v_rip + 0xB61BD8) * 1 + 0x178)) + (135);
loc_002CC05B:
    *(uint32_t *)(v_stack_mD0) = 5;
    if ((*(uint32_t *)(arg1 + 0x94 - 0x4)) != 0) goto loc_002CC19F;
loc_002CC06D:
    Arg4 = (Arg4) + 1;
    local_r10 = (v_stack_mD0) + (56);
    Arg3 = (Arg1 + 148) + (304);
    local_rbx = (local_rbx) + (168);
    if (Arg4 < 3) goto loc_002CC05B;
    if (0 == 0) goto loc_002CC425;
    local_r12 = (uint32_t)((0) + (*(uint32_t *)(arg1 + 0x88 + 0xC)));
    result = MiGetEngineBackgroundQualifications(Arg1 + 136, v_stack_m138, v_stack_m120, v_stack_mF8);
    Arg1 = (Arg1 + 136) | (-1);
    if ((uint32_t)((uint32_t)(v_stack_mD0)) == 0) goto loc_002CC1DF;
loc_002CC0CE:
    if (v_stack_m128 == 0) goto loc_002CC186;
    local_r10 = (local_r10) * (v_stack_m128);
    local_rsi = (0) * (v_stack_m128);
    local_r10 = (local_r10) + (136);
    local_r10 = (local_r10) + (Arg1);
    local_r11 = (v_stack_mF8) + (local_rsi);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0xC)))));
    *(uint32_t *)(local_r11 + 0x28) = 5;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x4))) == 0) goto loc_002CC176;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0xC))))) goto loc_002CC3FC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0xC)))) >= (*(uint32_t *)(local_r10 + 0x8))) goto loc_002CC176;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r10 + 0xB0) + 0x38)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r10 + 0xB0) + 0x38)) * 2) << (7);
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r10 + 0xB0) + 0x38))) * ((int32_t)(*(uint32_t *)(local_r10)));
    if (v_stack_m138 != 0) goto loc_002CC3A4;
loc_002CC15A:
    if (v_stack_m137 != 0) goto loc_002CC3CF;
loc_002CC165:
    Arg4 = 0;
    Arg3 = 0;
    result = MiFindBestZeroingProcessor(local_r11, local_r10, Arg3, Arg4);
loc_002CC176:
    if ((*(uint32_t *)(v_stack_m58 + local_rsi * 1 - 0x78)) == 0) goto loc_002CC1D3;
    Arg1 = (local_r11) | (-1);
loc_002CC186:
    if (v_stack_m128 == v_stack_m130) goto loc_002CC1D3;
    local_rbx = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) != 1) { local_rbx = Arg1; }
    local_rbx = (local_rbx) + (v_stack_m128);
    goto loc_002CC0CE;
loc_002CC19F:
    local_r12 = (uint32_t)((local_r12) + (*(uint32_t *)(local_r11 + arg1 * 1 + 0x94)));
    Arg2 = 0;
    Arg2 = (0 != 0) ? 1 : 0;
    result = ((uint32_t)(*(uint32_t *)(arg3))) * (*(uint64_t *)(local_rbx + 0x9));
    if ((*(uint8_t *)(local_rbx)) == 0) goto loc_002CC06D;
    *(uint8_t *)(local_rsp + Arg2 * 1 + 0x20) = 1;
    goto loc_002CC06D;
loc_002CC1D3:
loc_002CC1DF:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_stack_m110, Arg2, Arg3, Arg4);
    local_r13 = 0;
    if ((uint32_t)((uint32_t)(v_stack_mD0)) == 0) goto loc_002CC41A;
    Arg1 = local_r13 + 5 - 2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) != 1) { Arg1 = 0; }
loc_002CC211:
    if ((uint32_t)((uint32_t)(v_stack_m134)) == 0) goto loc_002CC22E;
    result = (result) * (v_stack_m128);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + result * 1 - 0x78)))) != 5) goto loc_002CC407;
loc_002CC22E:
    if (v_stack_m128 == v_stack_m130) goto loc_002CC258;
    local_rdi = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) != 1) { local_rdi = -1; }
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m134))))));
    Arg3 = -1 + 2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) != ((uint32_t)(-1 + 2))) { Arg3 = -1; }
    Arg3 = (Arg3) + (v_stack_m128);
    goto loc_002CC211;
loc_002CC258:
    if (((uint32_t)((uint32_t)(v_stack_mD0))) != 5) goto loc_002CC392;
loc_002CC264:
    if (((uint32_t)(local_r13 + 5)) != 5) goto loc_002CC437;
loc_002CC270:
loc_002CC279:
    if (3 != 3) goto loc_002CC307;
loc_002CC298:
    if ((*(uint32_t *)(arg1 + 0x94)) != 0) goto loc_002CC2AF;
    result = (uint32_t)((0) + 1);
    Arg1 = (0) + 1;
    Arg2 = (Arg1 + 148) + (304);
    if (Arg1 < 3) goto loc_002CC298;
loc_002CC2AF:
    if (((uint32_t)(result)) == 3) {
        Arg1 = *(uint32_t *)(arg1 + 0x38);
        Arg3 = (Arg3) * (Arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        Arg2 = *(uint64_t *)(arg1 + 0x10);
        *(uint8_t *)(arg3 + Arg2 * 1 + 0x3BC0) = 0;
    }
loc_002CC2D8:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 3 - 1);
    local_rsp = (local_rsp) + (288);
    return result;
loc_002CC300:
    goto loc_002CBFF0;
loc_002CC307:
    local_rdi = ((uint32_t)((uint32_t)(result))) * ((int32_t)((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_p50) = (uint32_t)(Arg1);
    local_rdi = (local_rdi) + (Arg1);
loc_002CC325:
    if ((*(uint64_t *)(local_rdi + 0x148)) == (local_rdi + 328)) goto loc_002CC3C4;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0x148) - 0x1A0 + 0x180))) & (6));
    if (((uint8_t)(result)) != 2) goto loc_002CC3F4;
    result = MiIncrementZeroEngineThread(*(uint64_t *)(local_rdi + 0x148) - 416, local_rdi + 328, Arg3, 3 - 1);
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x148) - 0x1A0 + 0x1B0)) != 0) {
        Arg1 = *(uint64_t *)(local_rdi + 0x148) - 416;
        result = MiUnlinkZeroThreadFromActiveDomain(Arg1, local_rdi + 328, Arg3, 3 - 1);
    }
    result = (result) * ((int32_t)((uint32_t)(Arg1)));
    Arg3 = (v_stack_p60) + (result);
    result = MiAssignBackgroundZeroThreadToProcessor(*(uint64_t *)(local_rdi + 0x148) - 416, local_rdi + 136, Arg3, 3 - 1);
    result = MiRestartZeroingPass(local_rdi + 136, local_rdi + 136, Arg3, 3 - 1);
    result = 0;
    goto loc_002CC2D8;
loc_002CC392:
    if (((uint32_t)(*(uint64_t *)(local_rdi + 0x148) - 416)) > ((uint32_t)(local_rdi + 136))) goto loc_002CC264;
    goto loc_002CC264;
loc_002CC3A4:
    result = (v_stack_p38) + ((uint32_t)((uint32_t)(*(uint64_t *)(local_rdi + 0x148) - 416)));
    if (result <= (*(uint64_t *)(arg3 + 0x240))) goto loc_002CC15A;
    goto loc_002CC176;
loc_002CC3C4:
    goto loc_002CC2CF;
loc_002CC3CF:
    if ((local_rdi + (uint32_t)((uint32_t)(*(uint64_t *)(local_rdi + 0x148) - 416)) * 1) <= (*(uint64_t *)(arg3 + 0x248))) goto loc_002CC165;
    if (2 == 0) goto loc_002CC165;
    goto loc_002CC176;
loc_002CC3F4:
    goto loc_002CC325;
loc_002CC3FC:
    goto loc_002CC176;
loc_002CC407:
    if (2 >= ((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rdi + 0x148) - 416))))) goto loc_002CC22E;
    goto loc_002CC22E;
loc_002CC41A:
    goto loc_002CC279;
loc_002CC425:
    result = ExReleaseSpinLockSharedFromDpcLevel(0, 0, Arg3, 0);
    goto loc_002CC2D8;
loc_002CC437:
    if (0 != 4) goto loc_002CC279;
    if ((uint32_t)(local_r12) == 0) goto loc_002CC44F;
    goto loc_002CC270;
loc_002CC44F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x4254)))) == 1) goto loc_002CC279;
loc_002CC472:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2F4 - 0x8))) == 0) goto loc_002CC49D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2F4 - 0x8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2F4))))) goto loc_002CC4A7;
loc_002CC488:
    if (((uint32_t)((uint32_t)(3 - 1))) == ((int32_t)((uint32_t)(Arg1)))) goto loc_002CC279;
    local_r11 = (uint32_t)((3 - 1) - 1);
    Arg3 = ((uint32_t)((uint32_t)(3 - 1))) - 1;
    result = (Arg1 + 756) - (304);
loc_002CC49D:
    if (Arg3 != v_stack_p28) goto loc_002CC472;
    goto loc_002CC279;
loc_002CC4A7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2F4)))) >= (*(uint32_t *)(result - 0x4))) goto loc_002CC488;
    goto loc_002CC488;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x8` | `32` | `R` |
| `Arg1` | `- 0x4` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |
| `Arg1` | `+ 0x94` | `64` | `R` |
| `Arg1` | `+ 0x2F4` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CBF78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
