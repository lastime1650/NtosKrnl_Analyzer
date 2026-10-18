# PopConfigureHeteroPolicies

- RVA: `0x00A35B30`–`0x00A36280` (길이 `1,872` bytes)
- VA: `0x0000000140A35B30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AD96C`
- 디코드: `439`개 명령, `1,872/1,872` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **33**

### Outgoing calls
- `0x00A35BB1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A35E37` → [PopConfigureHeteroThresholds](PopConfigureHeteroThresholds_function_00A36288.md) (function, `0x00A36288`)
- `0x00A35E40` → [KeConfigureHeteroPolicy](KeConfigureHeteroPolicy_function_00A36548.md) (function, `0x00A36548`)
- `0x00A35E7A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A35F7C` → [PpmHeteroComputeBias](PpmHeteroComputeBias_function_00A366EC.md) (function, `0x00A366EC`)
- `0x00A35FD5` → [PpmHeteroComputeBias](PpmHeteroComputeBias_function_00A366EC.md) (function, `0x00A366EC`)
- `0x00A360AE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A360E8` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00A36118` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A3612C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00A3613C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A36166` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x00A3617D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A361A3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A361C9` → [PopCapturePlatformRole](../A8/PopCapturePlatformRole_function_00A864AC.md) (function, `0x00A864AC`)

### Direct callers
- [PopInitializeHeteroProcessors](../A5/PopInitializeHeteroProcessors_function_00A53570.md) at `0x00A537AF`

### Static image references
- `0x00A35B54` → RVA `0x00E0A740` (`.data`; read)
- `0x00A35C11` → RVA `0x0001A390` (`.rdata`; read)
- `0x00A35C37` → RVA `0x00E0B3F4` (`.data`; read)
- `0x00A35C97` → RVA `0x00F07798` (`.data`; read)
- `0x00A35CA7` → RVA `0x00F0CE0C` (`.data`; read)
- `0x00A35D08` → RVA `0x00E08380` (`.data`; read)
- `0x00A35D3B` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00A35D69` → RVA `0x00F09100` (`.data`; read)
- `0x00A35D70` → RVA `0x00F0913C` (`.data`; read)
- `0x00A35D8D` → RVA `0x00F09140` (`.data`; read)
- `0x00A35DA1` → RVA `0x00F09144` (`.data`; read)
- `0x00A35DB5` → RVA `0x00FC5180` (`ALMOSTRO`; read)
- `0x00A35DC4` → RVA `0x00FC5050` (`ALMOSTRO`; read)
- `0x00A35DCC` → RVA `0x00FC506C` (`ALMOSTRO`; read)
- `0x00A35DFF` → RVA `0x00FC6F58` (`ALMOSTRO`; write)
- `0x00A35E15` → RVA `0x0001A380` (`.rdata`; read)
- `0x00A35E45` → RVA `0x00FC6DAC` (`ALMOSTRO`; read)
- `0x00A35EA1` → RVA `0x00F07780` (`.data`; read)
- `0x00A35EE4` → RVA `0x00F077A0` (`.data`; read)
- `0x00A35EFB` → RVA `0x00F07790` (`.data`; read)
- `0x00A35F16` → RVA `0x00F07788` (`.data`; read)
- `0x00A3604D` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x00A36066` → RVA `0x0001A3A0` (`.rdata`; read)
- `0x00A3606E` → RVA `0x00B02490` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A36075` → RVA `0x00F09144` (`.data`; read/write)
- `0x00A36080` → RVA `0x00F09104` (`.data`; read)
- `0x00A36087` → RVA `0x00F09100` (`.data`; write)
- `0x00A36091` → RVA `0x00F09114` (`.data`; read)
- `0x00A36098` → RVA `0x00F0913C` (`.data`; write)
- `0x00A3609F` → RVA `0x00F09124` (`.data`; read)
- `0x00A360A6` → RVA `0x00F09134` (`.data`; read)
- `0x00A360FA` → RVA `0x00B4D128` (`PAGE`; read)
- `0x00A36265` → RVA `0x00FC6DAC` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00A35BB1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A35E7A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A360AE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A360E8` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00A36118` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A3612C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00A3613C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A36166` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x00A3617D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A361A3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00A361D7` → [sub_00B3A01A](../B3/Unknown_function_00B3A01A.md) (`tail-transfer`)
  - `0x00A361E0` → [sub_00B3A01A](../B3/Unknown_function_00B3A01A.md) (`tail-transfer`)
  - `0x00A361E6` → [sub_00B3A01A + 0x7](../B3/Unknown_function_00B3A01A.md) (`tail-transfer`)
  - `0x00A3622C` → [sub_00B3A01A + 0x1A](../B3/Unknown_function_00B3A01A.md) (`tail-transfer`)
  - `0x00A3624A` → [sub_00B3A01A + 0x40](../B3/Unknown_function_00B3A01A.md) (`tail-transfer`)
  - `0x00A36260` → [sub_00B3A01A + 0x40](../B3/Unknown_function_00B3A01A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A35B30  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A35B35  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A35B3A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00A35B3F  55                              push rbp
00A35B40  41 54                           push r12
00A35B42  41 55                           push r13
00A35B44  41 56                           push r14
00A35B46  41 57                           push r15
00A35B48  48 8D 6C 24 A0                  lea rbp, [rsp - 0x60]
00A35B4D  48 81 EC 60 01 00 00            sub rsp, 0x160
00A35B54  48 8B 05 E5 4B 3D 00            mov rax, qword ptr [rip + 0x3d4be5]
00A35B5B  48 33 C4                        xor rax, rsp
00A35B5E  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00A35B62  0F 57 C0                        xorps xmm0, xmm0
00A35B65  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
00A35B6A  33 DB                           xor ebx, ebx
00A35B6C  33 C0                           xor eax, eax
00A35B6E  40 8A F2                        mov sil, dl
00A35B71  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00A35B76  44 8B F1                        mov r14d, ecx
00A35B79  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00A35B7D  0F 57 C9                        xorps xmm1, xmm1
00A35B80  89 45 88                        mov dword ptr [rbp - 0x78], eax
00A35B83  44 8D 43 68                     lea r8d, [rbx + 0x68]
00A35B87  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00A35B8B  33 D2                           xor edx, edx
00A35B8D  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00A35B92  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A35B96  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00A35B9A  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00A35B9F  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00A35BA4  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
00A35BA8  0F 11 4D A0                     movups xmmword ptr [rbp - 0x60], xmm1
00A35BAC  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00A35BB1  E8 8A 10 C9 FF                  call 0x1406c6c40
00A35BB6  44 8D 43 03                     lea r8d, [rbx + 3]
00A35BBA  C7 45 B0 05 00 00 00            mov dword ptr [rbp - 0x50], 5
00A35BC1  44 8D 63 07                     lea r12d, [rbx + 7]
00A35BC5  45 3B F0                        cmp r14d, r8d
00A35BC8  0F 84 F4 05 00 00               je 0x140a361c2
00A35BCE  41 8D 46 FB                     lea eax, [r14 - 5]
00A35BD2  C7 45 F0 64 00 00 00            mov dword ptr [rbp - 0x10], 0x64
00A35BD9  83 F8 01                        cmp eax, 1
00A35BDC  C7 45 EC 0A 00 00 00            mov dword ptr [rbp - 0x14], 0xa
00A35BE3  41 8B C8                        mov ecx, r8d
00A35BE6  8D 53 13                        lea edx, [rbx + 0x13]
00A35BE9  0F 46 CA                        cmovbe ecx, edx
00A35BEC  44 8D 7B 02                     lea r15d, [rbx + 2]
00A35BF0  89 4D F4                        mov dword ptr [rbp - 0xc], ecx
00A35BF3  41 8B CE                        mov ecx, r14d
00A35BF6  83 E9 01                        sub ecx, 1
00A35BF9  0F 84 16 04 00 00               je 0x140a36015
00A35BFF  83 E9 01                        sub ecx, 1
00A35C02  0F 84 0D 04 00 00               je 0x140a36015
00A35C08  83 E9 01                        sub ecx, 1
00A35C0B  0F 85 11 03 00 00               jne 0x140a35f22
00A35C11  66 0F 6F 05 77 47 5E FF         movdqa xmm0, xmmword ptr [rip - 0xa1b889]
00A35C19  0F 11 45 B4                     movups xmmword ptr [rbp - 0x4c], xmm0
00A35C1D  44 89 7D C0                     mov dword ptr [rbp - 0x40], r15d
00A35C21  44 89 7D B8                     mov dword ptr [rbp - 0x48], r15d
00A35C25  0F 11 45 C4                     movups xmmword ptr [rbp - 0x3c], xmm0
00A35C29  0F 11 45 D4                     movups xmmword ptr [rbp - 0x2c], xmm0
00A35C2D  66 0F D6 45 E4                  movq qword ptr [rbp - 0x1c], xmm0
00A35C32  B9 05 00 00 00                  mov ecx, 5
00A35C37  4C 8D 05 B6 57 3D 00            lea r8, [rip + 0x3d57b6]
00A35C3E  44 8B C9                        mov r9d, ecx
00A35C41  8B F9                           mov edi, ecx
00A35C43  4D 8B DC                        mov r11, r12
00A35C46  49 BD 00 00 00 00 00 00 00 06   movabs r13, 0x600000000000000
00A35C50  45 8B 50 FC                     mov r10d, dword ptr [r8 - 4]
00A35C54  41 38 18                        cmp byte ptr [r8], bl
00A35C57  75 05                           jne 0x140a35c5e
00A35C59  44 8B C9                        mov r9d, ecx
00A35C5C  8B F9                           mov edi, ecx
00A35C5E  41 8B C2                        mov eax, r10d
00A35C61  45 85 D2                        test r10d, r10d
00A35C64  0F 84 47 02 00 00               je 0x140a35eb1
00A35C6A  83 E8 01                        sub eax, 1
00A35C6D  0F 84 88 02 00 00               je 0x140a35efb
00A35C73  83 E8 01                        sub eax, 1
00A35C76  0F 84 9A 02 00 00               je 0x140a35f16
00A35C7C  83 E8 01                        sub eax, 1
00A35C7F  0F 84 1C 02 00 00               je 0x140a35ea1
00A35C85  83 E8 01                        sub eax, 1
00A35C88  0F 84 23 02 00 00               je 0x140a35eb1
00A35C8E  83 E8 01                        sub eax, 1
00A35C91  0F 85 48 02 00 00               jne 0x140a35edf
00A35C97  48 8B 15 FA 1A 4D 00            mov rdx, qword ptr [rip + 0x4d1afa]
00A35C9E  48 85 D2                        test rdx, rdx
00A35CA1  0F 84 49 02 00 00               je 0x140a35ef0
00A35CA7  48 63 05 5E 71 4D 00            movsxd rax, dword ptr [rip + 0x4d715e]
00A35CAE  48 83 C2 28                     add rdx, 0x28
00A35CB2  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
00A35CB9  48 03 D1                        add rdx, rcx
00A35CBC  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00A35CBF  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00A35CC4  66 48 0F 7E C0                  movq rax, xmm0
00A35CC9  48 0F BA E0 3A                  bt rax, 0x3a
00A35CCE  73 07                           jae 0x140a35cd7
00A35CD0  44 8B 8A BC 01 00 00            mov r9d, dword ptr [rdx + 0x1bc]
00A35CD7  48 0F BA E0 39                  bt rax, 0x39
00A35CDC  73 06                           jae 0x140a35ce4
00A35CDE  8B BA C0 01 00 00               mov edi, dword ptr [rdx + 0x1c0]
00A35CE4  B9 05 00 00 00                  mov ecx, 5
00A35CE9  44 3B C9                        cmp r9d, ecx
00A35CEC  0F 85 F9 04 00 00               jne 0x140a361eb
00A35CF2  3B F9                           cmp edi, ecx
00A35CF4  0F 85 FB 04 00 00               jne 0x140a361f5
00A35CFA  49 83 C0 08                     add r8, 8
00A35CFE  49 83 EB 01                     sub r11, 1
00A35D02  0F 85 48 FF FF FF               jne 0x140a35c50
00A35D08  48 8B 15 71 26 3D 00            mov rdx, qword ptr [rip + 0x3d2671]
00A35D0F  48 63 05 F6 70 4D 00            movsxd rax, dword ptr [rip + 0x4d70f6]
00A35D16  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
00A35D1D  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00A35D20  8B 8C 11 E0 01 00 00            mov ecx, dword ptr [rcx + rdx + 0x1e0]
00A35D27  85 C9                           test ecx, ecx
00A35D29  0F 45 C1                        cmovne eax, ecx
00A35D2C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00A35D2F  40 84 F6                        test sil, sil
00A35D32  0F 85 2E 03 00 00               jne 0x140a36066
00A35D38  48 8B C3                        mov rax, rbx
00A35D3B  4C 8D 2D BE A2 5C FF            lea r13, [rip - 0xa35d42]
00A35D42  49 8B FC                        mov rdi, r12
00A35D45  49 8B CF                        mov rcx, r15
00A35D48  42 8B 94 28 04 91 F0 00         mov edx, dword ptr [rax + r13 + 0xf09104]
00A35D50  83 FA 05                        cmp edx, 5
00A35D53  0F 85 C3 04 00 00               jne 0x140a3621c
00A35D59  48 83 C0 04                     add rax, 4
00A35D5D  48 83 E9 01                     sub rcx, 1
00A35D61  75 E5                           jne 0x140a35d48
00A35D63  48 83 EF 01                     sub rdi, 1
00A35D67  75 DC                           jne 0x140a35d45
00A35D69  83 3D 90 33 4D 00 05            cmp dword ptr [rip + 0x4d3390], 5
00A35D70  8B 05 C6 33 4D 00               mov eax, dword ptr [rip + 0x4d33c6]
00A35D76  8B 55 B0                        mov edx, dword ptr [rbp - 0x50]
00A35D79  0F 45 15 80 33 4D 00            cmovne edx, dword ptr [rip + 0x4d3380]
00A35D80  85 C0                           test eax, eax
00A35D82  8B 4D EC                        mov ecx, dword ptr [rbp - 0x14]
00A35D85  44 8A 6C 24 30                  mov r13b, byte ptr [rsp + 0x30]
00A35D8A  0F 45 C8                        cmovne ecx, eax
00A35D8D  8B 05 AD 33 4D 00               mov eax, dword ptr [rip + 0x4d33ad]
00A35D93  85 C0                           test eax, eax
00A35D95  89 4D EC                        mov dword ptr [rbp - 0x14], ecx
00A35D98  8B 4D F0                        mov ecx, dword ptr [rbp - 0x10]
00A35D9B  0F 45 C8                        cmovne ecx, eax
00A35D9E  89 55 B0                        mov dword ptr [rbp - 0x50], edx
00A35DA1  83 3D 9C 33 4D 00 FF            cmp dword ptr [rip + 0x4d339c], -1
00A35DA8  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00A35DAB  8B 4D F4                        mov ecx, dword ptr [rbp - 0xc]
00A35DAE  0F 45 0D 8F 33 4D 00            cmovne ecx, dword ptr [rip + 0x4d338f]
00A35DB5  39 1D C5 F3 58 00               cmp dword ptr [rip + 0x58f3c5], ebx
00A35DBB  89 4D F4                        mov dword ptr [rbp - 0xc], ecx
00A35DBE  0F 85 61 04 00 00               jne 0x140a36225
00A35DC4  8B 3D 86 F2 58 00               mov edi, dword ptr [rip + 0x58f286]
00A35DCA  8B C7                           mov eax, edi
00A35DCC  44 8B 05 99 F2 58 00            mov r8d, dword ptr [rip + 0x58f299]
00A35DD3  83 FF FF                        cmp edi, -1
00A35DD6  41 0F 44 C0                     cmove eax, r8d
00A35DDA  85 C0                           test eax, eax
00A35DDC  0F 85 6B 02 00 00               jne 0x140a3604d
00A35DE2  83 FF FF                        cmp edi, -1
00A35DE5  8B C7                           mov eax, edi
00A35DE7  B9 F4 01 00 00                  mov ecx, 0x1f4
00A35DEC  41 0F 44 C0                     cmove eax, r8d
00A35DF0  3B C1                           cmp eax, ecx
00A35DF2  0F 87 39 04 00 00               ja 0x140a36231
00A35DF8  8B F9                           mov edi, ecx
00A35DFA  8D 04 BF                        lea eax, [rdi + rdi*4]
00A35DFD  03 C0                           add eax, eax
00A35DFF  48 89 05 52 11 59 00            mov qword ptr [rip + 0x591152], rax
00A35E06  41 8D 46 FF                     lea eax, [r14 - 1]
00A35E0A  A9 FA FF FF FF                  test eax, 0xfffffffa
00A35E0F  0F 84 39 01 00 00               je 0x140a35f4e
00A35E15  66 0F 6F 05 63 45 5E FF         movdqa xmm0, xmmword ptr [rip - 0xa1ba9d]
00A35E1D  BE 01 00 00 00                  mov esi, 1
00A35E22  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00A35E26  66 0F D6 45 40                  movq qword ptr [rbp + 0x40], xmm0
00A35E2B  66 0F 7E 45 48                  movd dword ptr [rbp + 0x48], xmm0
00A35E30  41 8A D5                        mov dl, r13b
00A35E33  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A35E37  E8 4C 04 00 00                  call 0x140a36288
00A35E3C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A35E40  E8 03 07 00 00                  call 0x140a36548
00A35E45  39 35 61 0F 59 00               cmp dword ptr [rip + 0x590f61], esi
00A35E4B  0F 85 14 04 00 00               jne 0x140a36265
00A35E51  48 8D 15 A8 A1 5C FF            lea rdx, [rip - 0xa35e58]
00A35E58  8B 4C 1D 30                     mov ecx, dword ptr [rbp + rbx + 0x30]
00A35E5C  39 8C 13 18 75 FC 00            cmp dword ptr [rbx + rdx + 0xfc7518], ecx
00A35E63  0F 85 09 04 00 00               jne 0x140a36272
00A35E69  48 83 C3 04                     add rbx, 4
00A35E6D  49 83 EC 01                     sub r12, 1
00A35E71  75 E5                           jne 0x140a35e58
00A35E73  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00A35E77  48 33 CC                        xor rcx, rsp
00A35E7A  E8 C1 67 C7 FF                  call 0x1406ac640
00A35E7F  4C 8D 9C 24 60 01 00 00         lea r11, [rsp + 0x160]
00A35E87  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00A35E8B  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00A35E8F  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00A35E93  49 8B E3                        mov rsp, r11
00A35E96  41 5F                           pop r15
00A35E98  41 5E                           pop r14
00A35E9A  41 5D                           pop r13
00A35E9C  41 5C                           pop r12
00A35E9E  5D                              pop rbp
00A35E9F  C3                              ret
00A35EA0  CC                              int3
00A35EA1  48 8B 15 D8 18 4D 00            mov rdx, qword ptr [rip + 0x4d18d8]
00A35EA8  48 85 D2                        test rdx, rdx
00A35EAB  0F 85 3D 01 00 00               jne 0x140a35fee
00A35EB1  48 8B 15 C8 24 3D 00            mov rdx, qword ptr [rip + 0x3d24c8]
00A35EB8  48 63 05 4D 6F 4D 00            movsxd rax, dword ptr [rip + 0x4d6f4d]
00A35EBF  48 83 C2 28                     add rdx, 0x28
00A35EC3  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
00A35ECA  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00A35ECF  48 03 D1                        add rdx, rcx
00A35ED2  49 0B C5                        or rax, r13
00A35ED5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A35EDA  E9 EA FD FF FF                  jmp 0x140a35cc9
00A35EDF  83 F8 01                        cmp eax, 1
00A35EE2  75 CD                           jne 0x140a35eb1
00A35EE4  48 8B 15 B5 18 4D 00            mov rdx, qword ptr [rip + 0x4d18b5]
00A35EEB  E9 AE FD FF FF                  jmp 0x140a35c9e
00A35EF0  48 8B D3                        mov rdx, rbx
00A35EF3  0F 57 C0                        xorps xmm0, xmm0
00A35EF6  E9 C4 FD FF FF                  jmp 0x140a35cbf
00A35EFB  48 8B 15 8E 18 4D 00            mov rdx, qword ptr [rip + 0x4d188e]
00A35F02  48 85 D2                        test rdx, rdx
00A35F05  0F 85 9C FD FF FF               jne 0x140a35ca7
00A35F0B  48 8B D3                        mov rdx, rbx
00A35F0E  0F 57 C0                        xorps xmm0, xmm0
00A35F11  E9 F0 00 00 00                  jmp 0x140a36006
00A35F16  48 8B 15 6B 18 4D 00            mov rdx, qword ptr [rip + 0x4d186b]
00A35F1D  E9 7C FD FF FF                  jmp 0x140a35c9e
00A35F22  41 2B CF                        sub ecx, r15d
00A35F25  0F 84 EA 00 00 00               je 0x140a36015
00A35F2B  83 F9 01                        cmp ecx, 1
00A35F2E  0F 84 E1 00 00 00               je 0x140a36015
00A35F34  0F 57 C0                        xorps xmm0, xmm0
00A35F37  33 C0                           xor eax, eax
00A35F39  0F 11 45 B4                     movups xmmword ptr [rbp - 0x4c], xmm0
00A35F3D  48 89 45 E4                     mov qword ptr [rbp - 0x1c], rax
00A35F41  0F 11 45 C4                     movups xmmword ptr [rbp - 0x3c], xmm0
00A35F45  0F 11 45 D4                     movups xmmword ptr [rbp - 0x2c], xmm0
00A35F49  E9 E4 FC FF FF                  jmp 0x140a35c32
00A35F4E  44 8A C3                        mov r8b, bl
00A35F51  44 8A CB                        mov r9b, bl
00A35F54  40 8A FB                        mov dil, bl
00A35F57  85 D2                           test edx, edx
00A35F59  0F 84 FB 02 00 00               je 0x140a3625a
00A35F5F  41 2B D7                        sub edx, r15d
00A35F62  0F 84 E7 02 00 00               je 0x140a3624f
00A35F68  41 2B D7                        sub edx, r15d
00A35F6B  0F 84 D6 02 00 00               je 0x140a36247
00A35F71  83 FA 01                        cmp edx, 1
00A35F74  74 28                           je 0x140a35f9e
00A35F76  41 8A D1                        mov dl, r9b
00A35F79  41 8A C8                        mov cl, r8b
00A35F7C  E8 6B 07 00 00                  call 0x140a366ec
00A35F81  48 63 F0                        movsxd rsi, eax
00A35F84  40 84 FF                        test dil, dil
00A35F87  0F 84 A3 FE FF FF               je 0x140a35e30
00A35F8D  48 8B C6                        mov rax, rsi
00A35F90  48 8D 7D 30                     lea rdi, [rbp + 0x30]
00A35F94  49 8B CC                        mov rcx, r12
00A35F97  F3 AB                           rep stosd dword ptr [rdi], eax
00A35F99  E9 92 FE FF FF                  jmp 0x140a35e30
00A35F9E  48 8D 75 30                     lea rsi, [rbp + 0x30]
00A35FA2  4D 8B F4                        mov r14, r12
00A35FA5  4C 8D 55 B4                     lea r10, [rbp - 0x4c]
00A35FA9  8A CB                           mov cl, bl
00A35FAB  44 8A DB                        mov r11b, bl
00A35FAE  49 8B D7                        mov rdx, r15
00A35FB1  41 8B 02                        mov eax, dword ptr [r10]
00A35FB4  85 C0                           test eax, eax
00A35FB6  0F 84 81 02 00 00               je 0x140a3623d
00A35FBC  41 3B C7                        cmp eax, r15d
00A35FBF  0F 85 ED 01 00 00               jne 0x140a361b2
00A35FC5  41 B3 01                        mov r11b, 1
00A35FC8  49 83 C2 04                     add r10, 4
00A35FCC  48 83 EA 01                     sub rdx, 1
00A35FD0  75 DF                           jne 0x140a35fb1
00A35FD2  41 8A D3                        mov dl, r11b
00A35FD5  E8 12 07 00 00                  call 0x140a366ec
00A35FDA  89 06                           mov dword ptr [rsi], eax
00A35FDC  44 0A C1                        or r8b, cl
00A35FDF  48 83 C6 04                     add rsi, 4
00A35FE3  45 0A CB                        or r9b, r11b
00A35FE6  49 83 EE 01                     sub r14, 1
00A35FEA  74 8A                           je 0x140a35f76
00A35FEC  EB BB                           jmp 0x140a35fa9
00A35FEE  48 63 05 17 6E 4D 00            movsxd rax, dword ptr [rip + 0x4d6e17]
00A35FF5  48 83 C2 28                     add rdx, 0x28
00A35FF9  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
00A36000  48 03 D1                        add rdx, rcx
00A36003  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00A36006  66 48 0F 7E C0                  movq rax, xmm0
00A3600B  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00A36010  E9 B4 FC FF FF                  jmp 0x140a35cc9
00A36015  8B C3                           mov eax, ebx
00A36017  48 8D 4D B4                     lea rcx, [rbp - 0x4c]
00A3601B  49 8B FF                        mov rdi, r15
00A3601E  41 3B C4                        cmp eax, r12d
00A36021  73 25                           jae 0x140a36048
00A36023  83 F8 01                        cmp eax, 1
00A36026  76 20                           jbe 0x140a36048
00A36028  41 8B D0                        mov edx, r8d
00A3602B  83 F8 04                        cmp eax, 4
00A3602E  74 18                           je 0x140a36048
00A36030  89 11                           mov dword ptr [rcx], edx
00A36032  48 83 C1 04                     add rcx, 4
00A36036  48 83 EF 01                     sub rdi, 1
00A3603A  75 E2                           jne 0x140a3601e
00A3603C  FF C0                           inc eax
00A3603E  41 3B C4                        cmp eax, r12d
00A36041  72 D8                           jb 0x140a3601b
00A36043  E9 EA FB FF FF                  jmp 0x140a35c32
00A36048  41 8B D7                        mov edx, r15d
00A3604B  EB E3                           jmp 0x140a36030
00A3604D  8B 05 E9 0A 59 00               mov eax, dword ptr [rip + 0x590ae9]
00A36053  43 8D 0C 80                     lea ecx, [r8 + r8*4]
00A36057  03 C9                           add ecx, ecx
00A36059  3B C8                           cmp ecx, eax
00A3605B  0F 47 C1                        cmova eax, ecx
00A3605E  89 45 F8                        mov dword ptr [rbp - 8], eax
00A36061  E9 7C FD FF FF                  jmp 0x140a35de2
00A36066  66 0F 6F 05 32 43 5E FF         movdqa xmm0, xmmword ptr [rip - 0xa1bcce]
00A3606E  48 8D 15 1B C4 0C 00            lea rdx, [rip + 0xcc41b]
00A36075  83 0D C8 30 4D 00 FF            or dword ptr [rip + 0x4d30c8], 0xffffffff
00A3607C  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00A36080  0F 11 05 7D 30 4D 00            movups xmmword ptr [rip + 0x4d307d], xmm0
00A36087  C7 05 6F 30 4D 00 05 00 00 00   mov dword ptr [rip + 0x4d306f], 5
00A36091  0F 11 05 7C 30 4D 00            movups xmmword ptr [rip + 0x4d307c], xmm0
00A36098  48 89 1D 9D 30 4D 00            mov qword ptr [rip + 0x4d309d], rbx
00A3609F  0F 11 05 7E 30 4D 00            movups xmmword ptr [rip + 0x4d307e], xmm0
00A360A6  66 0F D6 05 86 30 4D 00         movq qword ptr [rip + 0x4d3086], xmm0
00A360AE  E8 CD 46 9F FF                  call 0x14042a780
00A360B3  48 8D 45 90                     lea rax, [rbp - 0x70]
00A360B7  C7 44 24 60 30 00 00 00         mov dword ptr [rsp + 0x60], 0x30
00A360BF  0F 57 C0                        xorps xmm0, xmm0
00A360C2  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A360C7  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00A360CC  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00A360D1  BA 08 00 00 00                  mov edx, 8
00A360D6  C7 44 24 78 40 02 00 00         mov dword ptr [rsp + 0x78], 0x240
00A360DE  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A360E3  F3 0F 7F 45 80                  movdqu xmmword ptr [rbp - 0x80], xmm0
00A360E8  E8 23 72 C7 FF                  call 0x1406ad310
00A360ED  85 C0                           test eax, eax
00A360EF  0F 88 43 FC FF FF               js 0x140a35d38
00A360F5  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00A360FA  48 8D 3D 27 70 11 00            lea rdi, [rip + 0x117027]
00A36101  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A36106  4C 8D 2D F3 9E 5C FF            lea r13, [rip - 0xa3610d]
00A3610D  49 8B F4                        mov rsi, r12
00A36110  48 8B 57 F8                     mov rdx, qword ptr [rdi - 8]
00A36114  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00A36118  E8 63 46 9F FF                  call 0x14042a780
00A3611D  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00A36122  BA 01 00 00 00                  mov edx, 1
00A36127  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00A3612C  E8 DF 71 C7 FF                  call 0x1406ad310
00A36131  85 C0                           test eax, eax
00A36133  78 52                           js 0x140a36187
00A36135  48 8B 17                        mov rdx, qword ptr [rdi]
00A36138  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00A3613C  E8 3F 46 9F FF                  call 0x14042a780
00A36141  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A36146  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00A3614B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A36150  4C 8D 4D 20                     lea r9, [rbp + 0x20]
00A36154  41 B8 04 00 00 00               mov r8d, 4
00A3615A  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00A36162  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00A36166  E8 45 72 C7 FF                  call 0x1406ad3b0
00A3616B  85 C0                           test eax, eax
00A3616D  0F 89 8C 00 00 00               jns 0x140a361ff
00A36173  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A36178  48 85 C9                        test rcx, rcx
00A3617B  74 0A                           je 0x140a36187
00A3617D  E8 2E 71 C7 FF                  call 0x1406ad2b0
00A36182  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00A36187  48 83 C7 18                     add rdi, 0x18
00A3618B  48 83 EE 01                     sub rsi, 1
00A3618F  0F 85 7B FF FF FF               jne 0x140a36110
00A36195  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00A3619A  48 85 C9                        test rcx, rcx
00A3619D  0F 84 95 FB FF FF               je 0x140a35d38
00A361A3  E8 08 71 C7 FF                  call 0x1406ad2b0
00A361A8  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00A361AD  E9 86 FB FF FF                  jmp 0x140a35d38
00A361B2  83 F8 04                        cmp eax, 4
00A361B5  0F 85 0D FE FF FF               jne 0x140a35fc8
00A361BB  B1 01                           mov cl, 1
00A361BD  E9 06 FE FF FF                  jmp 0x140a35fc8
00A361C2  C7 45 EC 08 00 00 00            mov dword ptr [rbp - 0x14], 8
00A361C9  E8 DE 02 05 00                  call 0x140a864ac
00A361CE  41 BF 02 00 00 00               mov r15d, 2
00A361D4  41 3B C7                        cmp eax, r15d
00A361D7  0F 84 3D 3E 10 00               je 0x140b3a01a
00A361DD  83 F8 08                        cmp eax, 8
00A361E0  0F 84 34 3E 10 00               je 0x140b3a01a
00A361E6  E9 36 3E 10 00                  jmp 0x140b3a021
00A361EB  46 89 4C D5 B4                  mov dword ptr [rbp + r10*8 - 0x4c], r9d
00A361F0  E9 FD FA FF FF                  jmp 0x140a35cf2
00A361F5  42 89 7C D5 B8                  mov dword ptr [rbp + r10*8 - 0x48], edi
00A361FA  E9 FB FA FF FF                  jmp 0x140a35cfa
00A361FF  83 7D 20 04                     cmp dword ptr [rbp + 0x20], 4
00A36203  0F 85 6A FF FF FF               jne 0x140a36173
00A36209  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A3620C  8B 45 28                        mov eax, dword ptr [rbp + 0x28]
00A3620F  42 89 84 29 00 91 F0 00         mov dword ptr [rcx + r13 + 0xf09100], eax
00A36217  E9 57 FF FF FF                  jmp 0x140a36173
00A3621C  89 54 05 B4                     mov dword ptr [rbp + rax - 0x4c], edx
00A36220  E9 34 FB FF FF                  jmp 0x140a35d59
00A36225  48 8D 45 B4                     lea rax, [rbp - 0x4c]
00A36229  49 8B D4                        mov rdx, r12
00A3622C  E9 03 3E 10 00                  jmp 0x140b3a034
00A36231  83 FF FF                        cmp edi, -1
00A36234  41 0F 44 F8                     cmove edi, r8d
00A36238  E9 BD FB FF FF                  jmp 0x140a35dfa
00A3623D  B1 01                           mov cl, 1
00A3623F  44 8A D9                        mov r11b, cl
00A36242  E9 81 FD FF FF                  jmp 0x140a35fc8
00A36247  41 B0 01                        mov r8b, 1
00A3624A  E9 0B 3E 10 00                  jmp 0x140b3a05a
00A3624F  41 B1 01                        mov r9b, 1
00A36252  41 8A F9                        mov dil, r9b
00A36255  E9 1C FD FF FF                  jmp 0x140a35f76
00A3625A  41 B0 01                        mov r8b, 1
00A3625D  45 8A C8                        mov r9b, r8b
00A36260  E9 F5 3D 10 00                  jmp 0x140b3a05a
00A36265  89 35 41 0B 59 00               mov dword ptr [rip + 0x590b41], esi
00A3626B  B0 01                           mov al, 1
00A3626D  E9 DF FB FF FF                  jmp 0x140a35e51
00A36272  89 8C 13 18 75 FC 00            mov dword ptr [rbx + rdx + 0xfc7518], ecx
00A36279  B0 01                           mov al, 1
00A3627B  E9 E9 FB FF FF                  jmp 0x140a35e69
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopConfigureHeteroPolicies(int a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned __int64 v_stack_mA4;
    unsigned __int64 v_stack_mB4;
    unsigned __int64 v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD4;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (352);
    result = (*(unsigned __int64 *)(v_rip + 4017125)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m158 = a3;
    v_rbx = 0;
    result = 0;
    v_stack_m138 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    v_stack_m130 = 0;
    a2 = 0;
    v_stack_m140 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_m128 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_m150 = v_xmm0;
    result = memset(v_stack_mD8, a2, v_rbx + 104, a4);
    v_stack_mD8 = 5;
    if (((unsigned int)((unsigned int)(a1))) == ((unsigned int)(v_rbx + 3))) goto loc_00A361C2;
    v_stack_m98 = 100;
    v_stack_m9C = 10;
    a1 = (unsigned int)((unsigned int)(v_rbx + 3));
    if (((unsigned int)((unsigned int)(a1) - 5)) <= 1) { a1 = (unsigned int)(v_rbx + 19); }
    v_stack_m94 = a1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (1));
    if (condition_is_equal) goto loc_00A36015;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A36015;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00A35F22;
    v_stack_mD4 = v_xmm0;
    v_stack_mC8 = (unsigned int)(v_rbx + 2);
    v_stack_mD0 = (unsigned int)(v_rbx + 2);
    v_stack_mC4 = v_xmm0;
    v_stack_mB4 = v_xmm0;
    v_stack_mA4 = v_xmm0;
loc_00A35C32:
loc_00A35C50:
    v_rdi = 5;
    if ((*(unsigned __int8 *)(v_rip + 4020150)) == 0) {
        a4 = 5;
        v_rdi = 5;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4020150 - 4))) == 0) goto loc_00A35EB1;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4020150 - 4))))) - (1));
    if (condition_is_equal) goto loc_00A35EFB;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A35F16;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A35EA1;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A35EB1;
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_00A35EDF;
loc_00A35C9E:
    if (*(unsigned __int64 *)(v_rip + 5053178) == 0) goto loc_00A35EF0;
loc_00A35CA7:
    a2 = (*(unsigned __int64 *)(v_rip + 5053178)) + (40);
    a1 = (5) * ((int)(*(unsigned int *)(v_rip + 5075294)));
    a2 = (a2) + (a1);
loc_00A35CBF:
    v_stack_m150 = v_xmm0;
loc_00A35CC9:
    if (!(condition_is_above_or_equal)) {
        a4 = *(unsigned int *)(a2 + 444);
    }
    if (!(condition_is_above_or_equal)) {
        v_rdi = *(unsigned int *)(a2 + 448);
    }
    if (((unsigned int)(a4)) != 5) goto loc_00A361EB;
loc_00A35CF2:
    if (((unsigned int)(v_rdi)) != 5) goto loc_00A361F5;
loc_00A35CFA:
    a3 = (v_rip + 4020150) + (8);
    v_r11 = (v_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_00A35C50;
    a1 = (5) * ((int)(*(unsigned int *)(v_rip + 5075190)));
    result = (unsigned int)(v_stack_m98);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_rip + 4007537) * 1 + 480))) != 0) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_rip + 4007537) * 1 + 480))); }
    v_stack_m98 = (unsigned int)(result);
    if ((unsigned __int8)((unsigned __int8)(a2)) != 0) goto loc_00A36066;
loc_00A35D38:
loc_00A35D45:
loc_00A35D48:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + v_rip - 10706242 * 1 + 15765764)))) != 5) goto loc_00A3621C;
loc_00A35D59:
    result = (0) + (4);
    a1 = (v_rbx + 2) - (1);
    if (condition_is_not_equal) goto loc_00A35D48;
    v_rdi = (v_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_00A35D45;
    a2 = (unsigned int)(v_stack_mD8);
    if ((*(unsigned int *)(v_rip + 5059472)) != 5) { a2 = *(unsigned int *)(v_rip + 5059456); }
    a1 = (unsigned int)(v_stack_m9C);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5059526))) != 0) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5059526))); }
    v_stack_m9C = a1;
    a1 = (unsigned int)(v_stack_m98);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5059501))) != 0) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5059501))); }
    v_stack_mD8 = a2;
    v_stack_m98 = a1;
    a1 = (unsigned int)(v_stack_m94);
    if ((*(unsigned int *)(v_rip + 5059484)) != -1) { a1 = *(unsigned int *)(v_rip + 5059471); }
    v_stack_m94 = a1;
    if ((*(unsigned int *)(v_rip + 5829573)) != 0) goto loc_00A36225;
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5829254))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5829254)))) == -1) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5829273))); }
    if ((unsigned int)(result) != 0) goto loc_00A3604D;
loc_00A35DE2:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5829254))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5829254)))) == -1) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5829273))); }
    if (((unsigned int)(result)) > 500) goto loc_00A36231;
loc_00A35DFA:
    result = (unsigned int)((500 + 500 * 4) + ((unsigned int)(500 + 500 * 4)));
    *(unsigned __int64 *)(v_rip + 5837138) = result;
    if ((((unsigned int)((unsigned int)(a1) - 1)) & (0xFFFFFFFAULL)) == 0) goto loc_00A35F4E;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m40 = v_xmm0;
loc_00A35E30:
    result = PopConfigureHeteroThresholds(v_stack_mD8, (unsigned __int8)(v_stack_m158), (unsigned int)(*(unsigned int *)(v_rip + 5829273)), a4);
    result = KeConfigureHeteroPolicy(v_stack_mD8, (unsigned __int8)(v_stack_m158), (unsigned int)(*(unsigned int *)(v_rip + 5829273)), a4);
    if ((*(unsigned int *)(v_rip + 5836641)) != 1) goto loc_00A36265;
loc_00A35E51:
loc_00A35E58:
    if ((*(unsigned int *)(v_rbx + v_rip - 10706520 * 1 + 16545048)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + v_rbx * 1 + 48))))) goto loc_00A36272;
loc_00A35E69:
    v_rbx = (v_rbx) + (4);
    v_r12 = (v_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_00A35E58;
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 10706520, (unsigned int)(*(unsigned int *)(v_rip + 5829273)), a4);
    return result;
loc_00A35EA1:
    if (*(unsigned __int64 *)(v_rip + 5052632) != 0) goto loc_00A35FEE;
loc_00A35EB1:
    a2 = (*(unsigned __int64 *)(v_rip + 4007112)) + (40);
    a1 = (a1) * ((int)(*(unsigned int *)(v_rip + 5074765)));
    a2 = (a2) + (a1);
    result = (v_stack_m128) | (v_stack_m158);
    v_stack_m128 = result;
    goto loc_00A35CC9;
loc_00A35EDF:
    if (((unsigned int)(result)) != 1) goto loc_00A35EB1;
    goto loc_00A35C9E;
loc_00A35EF0:
    goto loc_00A35CBF;
loc_00A35EFB:
    if (*(unsigned __int64 *)(v_rip + 5052558) != 0) goto loc_00A35CA7;
    goto loc_00A36006;
loc_00A35F16:
    goto loc_00A35C9E;
loc_00A35F22:
    a1 = (unsigned int)((a1) - ((unsigned int)(v_rbx + 2)));
    if (condition_is_equal) goto loc_00A36015;
    if (a1 == 1) goto loc_00A36015;
    result = 0;
    v_stack_mD4 = v_xmm0;
    v_stack_mA4 = 0;
    v_stack_mC4 = v_xmm0;
    v_stack_mB4 = v_xmm0;
    goto loc_00A35C32;
loc_00A35F4E:
    if ((unsigned int)(*(unsigned __int64 *)(v_rip + 5052523)) == 0) goto loc_00A3625A;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rip + 5052523)) - ((unsigned int)(v_rbx + 2)));
    if (condition_is_equal) goto loc_00A3624F;
    a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx + 2)));
    if (condition_is_equal) goto loc_00A36247;
    if (a2 == 1) goto loc_00A35F9E;
loc_00A35F76:
    result = PpmHeteroComputeBias((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48))), (unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48))), (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)), (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)));
    if ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48))) == 0) goto loc_00A35E30;
    goto loc_00A35E30;
loc_00A35F9E:
loc_00A35FA9:
loc_00A35FB1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD4))) == 0) goto loc_00A3623D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD4)))) != ((unsigned int)(v_rbx + 2))) goto loc_00A361B2;
loc_00A35FC8:
    v_r10 = (v_stack_mD4) + (4);
    a2 = (v_rbx + 2) - (1);
    if (condition_is_not_equal) goto loc_00A35FB1;
    result = PpmHeteroComputeBias((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)), 1, (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)), (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)));
    *(unsigned int *)(v_stack_m58) = (unsigned int)(result);
    a3 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48))) | ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48)))));
    v_rsi = (v_stack_m58) + (4);
    a4 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48))) | (1));
    v_r14 = (v_r12) - (1);
    if (condition_is_equal) goto loc_00A35F76;
    goto loc_00A35FA9;
loc_00A35FEE:
    a2 = (1) + (40);
    a1 = ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 48))) * ((int)(*(unsigned int *)(v_rip + 5074455)));
    a2 = (a2) + (a1);
loc_00A36006:
    v_stack_m128 = v_xmm0;
    goto loc_00A35CC9;
loc_00A36015:
loc_00A3601B:
loc_00A3601E:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))))) >= ((unsigned int)(v_r12))) goto loc_00A36048;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))))) <= 1) goto loc_00A36048;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))))) == 4) goto loc_00A36048;
loc_00A36030:
    *(unsigned int *)(v_stack_mD4) = (unsigned int)((unsigned int)(a3));
    a1 = (v_stack_mD4) + (4);
    v_rdi = (v_rbx + 2) - (1);
    if (condition_is_not_equal) goto loc_00A3601E;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)))) + 1);
    if (((unsigned int)(result)) < ((unsigned int)(v_r12))) goto loc_00A3601B;
    goto loc_00A35C32;
loc_00A36048:
    goto loc_00A36030;
loc_00A3604D:
    a1 = (unsigned int)((a3 + a3 * 4) + ((unsigned int)(a3 + a3 * 4)));
    result = (unsigned int)(*(unsigned int *)(v_rip + 5835497));
    if (a1 > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5835497))))) { result = a1; }
    v_stack_m90 = (unsigned int)(result);
    goto loc_00A35DE2;
loc_00A36066:
    *(unsigned __int64 *)(v_rip + 5058685) = v_xmm0;
    *(unsigned int *)(v_rip + 5058671) = 5;
    *(unsigned __int64 *)(v_rip + 5058684) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5058717) = *(unsigned __int64 *)(v_stack_m28 + 48);
    *(unsigned __int64 *)(v_rip + 5058686) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5058694) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 836635, a3, a4);
    v_stack_m100 = 48;
    v_stack_mF0 = v_stack_mF8;
    v_stack_mF8 = *(unsigned __int64 *)(v_stack_m28 + 48);
    v_stack_mE8 = 576;
    v_stack_m108 = v_xmm0;
    result = ZwOpenKey(v_stack_m110, 8, v_stack_m100, a4);
    if (sign_flag) goto loc_00A35D38;
    v_stack_mF8 = v_stack_m110;
loc_00A36110:
    result = RtlInitUnicodeString(v_stack_mF8, *(unsigned __int64 *)(v_rip + 1142823 - 8), v_stack_m100, a4);
    result = ZwOpenKey(v_stack_m118, 1, v_stack_m100, a4);
    if (sign_flag) goto loc_00A36187;
    result = RtlInitUnicodeString(v_stack_mE8, *(unsigned __int64 *)(v_rip + 1142823), v_stack_m100, a4);
    v_stack_m138 = v_stack_m108;
    v_stack_m140 = 16;
    result = ZwQueryValueKey(v_stack_m118, v_stack_mE8, 4, v_stack_m68);
    if (!sign_flag) goto loc_00A361FF;
loc_00A36173:
    if (v_stack_m118 != 0) {
        result = ZwClose(v_stack_m118, v_stack_mE8, 4, v_stack_m68);
        v_stack_m118 = *(unsigned __int64 *)(v_stack_m28 + 48);
    }
    v_rdi = (v_rip + 1142823) + (24);
    v_rsi = (v_r12) - (1);
    if (condition_is_not_equal) goto loc_00A36110;
    if (v_stack_m110 == 0) goto loc_00A35D38;
    result = ZwClose(v_stack_m110, v_stack_mE8, 4, v_stack_m68);
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m28 + 48);
    goto loc_00A35D38;
loc_00A361B2:
    if (((unsigned int)(result)) != 4) goto loc_00A35FC8;
    goto loc_00A35FC8;
loc_00A361C2:
    v_stack_m9C = 8;
    result = PopCapturePlatformRole(1, v_stack_mE8, 4, v_stack_m68);
loc_00A361EB:
    *(unsigned int *)(v_stack_m88 + v_r10 * 8 - 76) = (unsigned int)(v_stack_m68);
    goto loc_00A35CF2;
loc_00A361F5:
    *(unsigned int *)(v_stack_m88 + v_r10 * 8 - 72) = (unsigned int)(v_rdi);
    goto loc_00A35CFA;
loc_00A361FF:
    if (v_stack_m68 != 4) goto loc_00A36173;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 8)) + v_rip - 10707213 * 1 + 15765760) = (unsigned int)((unsigned int)(v_stack_m60));
    goto loc_00A36173;
loc_00A3621C:
    *(unsigned int *)(v_stack_m88 + (unsigned int)(v_stack_m60) * 1 - 76) = (unsigned int)(v_stack_mE8);
    goto loc_00A35D59;
loc_00A36225:
loc_00A36231:
    if (((unsigned int)(v_rdi)) == -1) { v_rdi = 4; }
    goto loc_00A35DFA;
loc_00A3623D:
    goto loc_00A35FC8;
loc_00A36247:
loc_00A3624F:
    goto loc_00A35F76;
loc_00A3625A:
loc_00A36265:
    *(unsigned int *)(v_rip + 5835585) = (unsigned int)(v_rsi);
    goto loc_00A35E51;
loc_00A36272:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + v_r12 * 1 + 16545048) = 1;
    goto loc_00A35E69;
}
```

## 5. (Beta) C Style

```c
int64_t PopConfigureHeteroPolicies(int32_t Arg1, int32_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m150;
    uint8_t v_stack_m158;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint64_t v_stack_mA4;
    uint64_t v_stack_mB4;
    uint64_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD4;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (352);
    result = (*(uint64_t *)(v_rip + 0x3D4BE5)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m158 = Arg3;
    local_rbx = 0;
    result = 0;
    v_stack_m138 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    v_stack_m130 = 0;
    Arg2 = 0;
    v_stack_m140 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_m128 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_m150 = v_xmm0;
    result = memset(v_stack_mD8, Arg2, local_rbx + 104, a4);
    v_stack_mD8 = 5;
    if (((uint32_t)((uint32_t)(Arg1))) == ((uint32_t)(local_rbx + 3))) goto loc_00A361C2;
    v_stack_m98 = 100;
    v_stack_m9C = 10;
    Arg1 = (uint32_t)((uint32_t)(local_rbx + 3));
    if (((uint32_t)((uint32_t)(Arg1) - 5)) <= 1) { Arg1 = (uint32_t)(local_rbx + 19); }
    v_stack_m94 = Arg1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (1));
    if (condition_is_equal) goto loc_00A36015;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A36015;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00A35F22;
    v_stack_mD4 = v_xmm0;
    v_stack_mC8 = (uint32_t)(local_rbx + 2);
    v_stack_mD0 = (uint32_t)(local_rbx + 2);
    v_stack_mC4 = v_xmm0;
    v_stack_mB4 = v_xmm0;
    v_stack_mA4 = v_xmm0;
loc_00A35C32:
loc_00A35C50:
    local_rdi = 5;
    if ((*(uint8_t *)(v_rip + 0x3D57B6)) == 0) {
        a4 = 5;
        local_rdi = 5;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3D57B6 - 0x4))) == 0) goto loc_00A35EB1;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3D57B6 - 0x4))))) - (1));
    if (condition_is_equal) goto loc_00A35EFB;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A35F16;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A35EA1;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A35EB1;
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_00A35EDF;
loc_00A35C9E:
    if (*(uint64_t *)(v_rip + 0x4D1AFA) == 0) goto loc_00A35EF0;
loc_00A35CA7:
    Arg2 = (*(uint64_t *)(v_rip + 0x4D1AFA)) + (40);
    Arg1 = (5) * ((int32_t)(*(uint32_t *)(v_rip + 0x4D715E)));
    Arg2 = (Arg2) + (Arg1);
loc_00A35CBF:
    v_stack_m150 = v_xmm0;
loc_00A35CC9:
    if (!(condition_is_above_or_equal)) {
        a4 = *(uint32_t *)(Arg2 + 0x1BC);
    }
    if (!(condition_is_above_or_equal)) {
        local_rdi = *(uint32_t *)(Arg2 + 0x1C0);
    }
    if (((uint32_t)(a4)) != 5) goto loc_00A361EB;
loc_00A35CF2:
    if (((uint32_t)(local_rdi)) != 5) goto loc_00A361F5;
loc_00A35CFA:
    Arg3 = (v_rip + 4020150) + (8);
    local_r11 = (local_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_00A35C50;
    Arg1 = (5) * ((int32_t)(*(uint32_t *)(v_rip + 0x4D70F6)));
    result = (uint32_t)(v_stack_m98);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + *(uint64_t *)(v_rip + 0x3D2671) * 1 + 0x1E0))) != 0) { result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + *(uint64_t *)(v_rip + 0x3D2671) * 1 + 0x1E0))); }
    v_stack_m98 = (uint32_t)(result);
    if ((uint8_t)((uint8_t)(Arg2)) != 0) goto loc_00A36066;
loc_00A35D38:
loc_00A35D45:
loc_00A35D48:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + v_rip - 0xA35D42 * 1 + 0xF09104)))) != 5) goto loc_00A3621C;
loc_00A35D59:
    result = (0) + (4);
    Arg1 = (local_rbx + 2) - (1);
    if (condition_is_not_equal) goto loc_00A35D48;
    local_rdi = (local_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_00A35D45;
    Arg2 = (uint32_t)(v_stack_mD8);
    if ((*(uint32_t *)(v_rip + 0x4D3390)) != 5) { Arg2 = *(uint32_t *)(v_rip + 0x4D3380); }
    Arg1 = (uint32_t)(v_stack_m9C);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D33C6))) != 0) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D33C6))); }
    v_stack_m9C = Arg1;
    Arg1 = (uint32_t)(v_stack_m98);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D33AD))) != 0) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D33AD))); }
    v_stack_mD8 = Arg2;
    v_stack_m98 = Arg1;
    Arg1 = (uint32_t)(v_stack_m94);
    if ((*(uint32_t *)(v_rip + 0x4D339C)) != -1) { Arg1 = *(uint32_t *)(v_rip + 0x4D338F); }
    v_stack_m94 = Arg1;
    if ((*(uint32_t *)(v_rip + 0x58F3C5)) != 0) goto loc_00A36225;
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58F286))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58F286)))) == -1) { result = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58F299))); }
    if ((uint32_t)(result) != 0) goto loc_00A3604D;
loc_00A35DE2:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58F286))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58F286)))) == -1) { result = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58F299))); }
    if (((uint32_t)(result)) > 500) goto loc_00A36231;
loc_00A35DFA:
    result = (uint32_t)((500 + 500 * 4) + ((uint32_t)(500 + 500 * 4)));
    *(uint64_t *)(v_rip + 0x591152) = result;
    if ((((uint32_t)((uint32_t)(Arg1) - 1)) & (0xFFFFFFFAULL)) == 0) goto loc_00A35F4E;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m40 = v_xmm0;
loc_00A35E30:
    result = PopConfigureHeteroThresholds(v_stack_mD8, (uint8_t)(v_stack_m158), (uint32_t)(*(uint32_t *)(v_rip + 0x58F299)), a4);
    result = KeConfigureHeteroPolicy(v_stack_mD8, (uint8_t)(v_stack_m158), (uint32_t)(*(uint32_t *)(v_rip + 0x58F299)), a4);
    if ((*(uint32_t *)(v_rip + 0x590F61)) != 1) goto loc_00A36265;
loc_00A35E51:
loc_00A35E58:
    if ((*(uint32_t *)(local_rbx + v_rip - 0xA35E58 * 1 + 0xFC7518)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + local_rbx * 1 + 0x30))))) goto loc_00A36272;
loc_00A35E69:
    local_rbx = (local_rbx) + (4);
    local_r12 = (local_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_00A35E58;
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 10706520, (uint32_t)(*(uint32_t *)(v_rip + 0x58F299)), a4);
    return result;
loc_00A35EA1:
    if (*(uint64_t *)(v_rip + 0x4D18D8) != 0) goto loc_00A35FEE;
loc_00A35EB1:
    Arg2 = (*(uint64_t *)(v_rip + 0x3D24C8)) + (40);
    Arg1 = (Arg1) * ((int32_t)(*(uint32_t *)(v_rip + 0x4D6F4D)));
    Arg2 = (Arg2) + (Arg1);
    result = (v_stack_m128) | (v_stack_m158);
    v_stack_m128 = result;
    goto loc_00A35CC9;
loc_00A35EDF:
    if (((uint32_t)(result)) != 1) goto loc_00A35EB1;
    goto loc_00A35C9E;
loc_00A35EF0:
    goto loc_00A35CBF;
loc_00A35EFB:
    if (*(uint64_t *)(v_rip + 0x4D188E) != 0) goto loc_00A35CA7;
    goto loc_00A36006;
loc_00A35F16:
    goto loc_00A35C9E;
loc_00A35F22:
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_rbx + 2)));
    if (condition_is_equal) goto loc_00A36015;
    if (Arg1 == 1) goto loc_00A36015;
    result = 0;
    v_stack_mD4 = v_xmm0;
    v_stack_mA4 = 0;
    v_stack_mC4 = v_xmm0;
    v_stack_mB4 = v_xmm0;
    goto loc_00A35C32;
loc_00A35F4E:
    if ((uint32_t)(*(uint64_t *)(v_rip + 0x4D186B)) == 0) goto loc_00A3625A;
    Arg2 = (uint32_t)((*(uint64_t *)(v_rip + 0x4D186B)) - ((uint32_t)(local_rbx + 2)));
    if (condition_is_equal) goto loc_00A3624F;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_rbx + 2)));
    if (condition_is_equal) goto loc_00A36247;
    if (Arg2 == 1) goto loc_00A35F9E;
loc_00A35F76:
    result = PpmHeteroComputeBias((uint8_t)((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30))), (uint8_t)((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30))), (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)), (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)));
    if ((uint8_t)((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30))) == 0) goto loc_00A35E30;
    goto loc_00A35E30;
loc_00A35F9E:
loc_00A35FA9:
loc_00A35FB1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD4))) == 0) goto loc_00A3623D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD4)))) != ((uint32_t)(local_rbx + 2))) goto loc_00A361B2;
loc_00A35FC8:
    local_r10 = (v_stack_mD4) + (4);
    Arg2 = (local_rbx + 2) - (1);
    if (condition_is_not_equal) goto loc_00A35FB1;
    result = PpmHeteroComputeBias((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)), 1, (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)), (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)));
    *(uint32_t *)(v_stack_m58) = (uint32_t)(result);
    Arg3 = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30))) | ((uint8_t)((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30)))));
    local_rsi = (v_stack_m58) + (4);
    a4 = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30))) | (1));
    local_r14 = (local_r12) - (1);
    if (condition_is_equal) goto loc_00A35F76;
    goto loc_00A35FA9;
loc_00A35FEE:
    Arg2 = (1) + (40);
    Arg1 = ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x30))) * ((int32_t)(*(uint32_t *)(v_rip + 0x4D6E17)));
    Arg2 = (Arg2) + (Arg1);
loc_00A36006:
    v_stack_m128 = v_xmm0;
    goto loc_00A35CC9;
loc_00A36015:
loc_00A3601B:
loc_00A3601E:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))))) >= ((uint32_t)(local_r12))) goto loc_00A36048;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))))) <= 1) goto loc_00A36048;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))))) == 4) goto loc_00A36048;
loc_00A36030:
    *(uint32_t *)(v_stack_mD4) = (uint32_t)((uint32_t)(Arg3));
    Arg1 = (v_stack_mD4) + (4);
    local_rdi = (local_rbx + 2) - (1);
    if (condition_is_not_equal) goto loc_00A3601E;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)))) + 1);
    if (((uint32_t)(result)) < ((uint32_t)(local_r12))) goto loc_00A3601B;
    goto loc_00A35C32;
loc_00A36048:
    goto loc_00A36030;
loc_00A3604D:
    Arg1 = (uint32_t)((Arg3 + Arg3 * 4) + ((uint32_t)(Arg3 + Arg3 * 4)));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x590AE9));
    if (Arg1 > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x590AE9))))) { result = Arg1; }
    v_stack_m90 = (uint32_t)(result);
    goto loc_00A35DE2;
loc_00A36066:
    *(uint64_t *)(v_rip + 0x4D307D) = v_xmm0;
    *(uint32_t *)(v_rip + 0x4D306F) = 5;
    *(uint64_t *)(v_rip + 0x4D307C) = v_xmm0;
    *(uint64_t *)(v_rip + 0x4D309D) = *(uint64_t *)(v_stack_m28 + 0x30);
    *(uint64_t *)(v_rip + 0x4D307E) = v_xmm0;
    *(uint64_t *)(v_rip + 0x4D3086) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 836635, Arg3, a4);
    v_stack_m100 = 48;
    v_stack_mF0 = v_stack_mF8;
    v_stack_mF8 = *(uint64_t *)(v_stack_m28 + 0x30);
    v_stack_mE8 = 576;
    v_stack_m108 = v_xmm0;
    result = ZwOpenKey(v_stack_m110, 8, v_stack_m100, a4);
    if (sign_flag) goto loc_00A35D38;
    v_stack_mF8 = v_stack_m110;
loc_00A36110:
    result = RtlInitUnicodeString(v_stack_mF8, *(uint64_t *)(v_rip + 0x117027 - 0x8), v_stack_m100, a4);
    result = ZwOpenKey(v_stack_m118, 1, v_stack_m100, a4);
    if (sign_flag) goto loc_00A36187;
    result = RtlInitUnicodeString(v_stack_mE8, *(uint64_t *)(v_rip + 0x117027), v_stack_m100, a4);
    v_stack_m138 = v_stack_m108;
    v_stack_m140 = 16;
    result = ZwQueryValueKey(v_stack_m118, v_stack_mE8, 4, v_stack_m68);
    if (!sign_flag) goto loc_00A361FF;
loc_00A36173:
    if (v_stack_m118 != 0) {
        result = ZwClose(v_stack_m118, v_stack_mE8, 4, v_stack_m68);
        v_stack_m118 = *(uint64_t *)(v_stack_m28 + 0x30);
    }
    local_rdi = (v_rip + 1142823) + (24);
    local_rsi = (local_r12) - (1);
    if (condition_is_not_equal) goto loc_00A36110;
    if (v_stack_m110 == 0) goto loc_00A35D38;
    result = ZwClose(v_stack_m110, v_stack_mE8, 4, v_stack_m68);
    v_stack_m110 = *(uint64_t *)(v_stack_m28 + 0x30);
    goto loc_00A35D38;
loc_00A361B2:
    if (((uint32_t)(result)) != 4) goto loc_00A35FC8;
    goto loc_00A35FC8;
loc_00A361C2:
    v_stack_m9C = 8;
    result = PopCapturePlatformRole(1, v_stack_mE8, 4, v_stack_m68);
loc_00A361EB:
    *(uint32_t *)(v_stack_m88 + local_r10 * 8 - 0x4C) = (uint32_t)(v_stack_m68);
    goto loc_00A35CF2;
loc_00A361F5:
    *(uint32_t *)(v_stack_m88 + local_r10 * 8 - 0x48) = (uint32_t)(local_rdi);
    goto loc_00A35CFA;
loc_00A361FF:
    if (v_stack_m68 != 4) goto loc_00A36173;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) + v_rip - 0xA3610D * 1 + 0xF09100) = (uint32_t)((uint32_t)(v_stack_m60));
    goto loc_00A36173;
loc_00A3621C:
    *(uint32_t *)(v_stack_m88 + (uint32_t)(v_stack_m60) * 1 - 0x4C) = (uint32_t)(v_stack_mE8);
    goto loc_00A35D59;
loc_00A36225:
loc_00A36231:
    if (((uint32_t)(local_rdi)) == -1) { local_rdi = 4; }
    goto loc_00A35DFA;
loc_00A3623D:
    goto loc_00A35FC8;
loc_00A36247:
loc_00A3624F:
    goto loc_00A35F76;
loc_00A3625A:
loc_00A36265:
    *(uint32_t *)(v_rip + 0x590B41) = (uint32_t)(local_rsi);
    goto loc_00A35E51;
loc_00A36272:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + local_r12 * 1 + 0xFC7518) = 1;
    goto loc_00A35E69;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A35B30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
