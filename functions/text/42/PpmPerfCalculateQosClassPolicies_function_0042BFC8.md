# PpmPerfCalculateQosClassPolicies

- RVA: `0x0042BFC8`–`0x0042C864` (길이 `2,204` bytes)
- VA: `0x000000014042BFC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A1950`
- 디코드: `514`개 명령, `2,204/2,204` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x0042C007` → [PpmGetPerfPolicyClass](PpmGetPerfPolicyClass_function_0042CF54.md) (function, `0x0042CF54`)
- `0x0042C399` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0042C464` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0042C492` → [PpmEventQosClassPolicy](../../page/A7/PpmEventQosClassPolicy_function_00A76108.md) (function, `0x00A76108`)
- `0x0042C4A1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0042C4E6` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0042C665` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)

### Direct callers
- [PpmPerfUpdateDomainPolicy](../../page/A9/PpmPerfUpdateDomainPolicy_function_00A97030.md) at `0x00A970AB`

### Static image references
- `0x0042BFEB` → RVA `0x00E0A740` (`.data`; read)
- `0x0042BFF9` → RVA `0x00E08380` (`.data`; read)
- `0x0042C00C` → RVA `0x00F0CE0C` (`.data`; read)
- `0x0042C012` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0042C09D` → RVA `0x00F07798` (`.data`; read)
- `0x0042C103` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x0042C114` → RVA `0x00FC6DA8` (`ALMOSTRO`; read)
- `0x0042C12E` → RVA `0x00FC6ADC` (`ALMOSTRO`; read)
- `0x0042C140` → RVA `0x00014518` (`.rdata`; read)
- `0x0042C161` → RVA `0x00014528` (`.rdata`; read)
- `0x0042C195` → RVA `0x00014508` (`.rdata`; read)
- `0x0042C1A2` → RVA `0x00014510` (`.rdata`; read)
- `0x0042C1B1` → RVA `0x00F0E0F0` (`.data`; read)
- `0x0042C1BE` → RVA `0x00FC6CD0` (`ALMOSTRO`; read)
- `0x0042C212` → RVA `0x00FC6AF7` (`ALMOSTRO`; read)
- `0x0042C247` → RVA `0x00F0E17C` (`.data`; read)
- `0x0042C283` → RVA `0x00FC6AFB` (`ALMOSTRO`; read)
- `0x0042C5C9` → RVA `0x00F07788` (`.data`; read)
- `0x0042C645` → RVA `0x00F077A0` (`.data`; read)
- `0x0042C69E` → RVA `0x00F07790` (`.data`; read)
- `0x0042C704` → RVA `0x00F07780` (`.data`; read)
- `0x0042C777` → RVA `0x00F077E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0042C492` → [PpmEventQosClassPolicy](../../page/A7/PpmEventQosClassPolicy_function_00A76108.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0042C84A` → [sub_006EE428](../6E/Unknown_function_006EE428.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042BFC8  48 8B C4                        mov rax, rsp
0042BFCB  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0042BFCF  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0042BFD3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0042BFD7  55                              push rbp
0042BFD8  41 54                           push r12
0042BFDA  41 55                           push r13
0042BFDC  41 56                           push r14
0042BFDE  41 57                           push r15
0042BFE0  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0042BFE4  48 81 EC 90 00 00 00            sub rsp, 0x90
0042BFEB  48 8B 05 4E E7 9D 00            mov rax, qword ptr [rip + 0x9de74e]
0042BFF2  48 33 C4                        xor rax, rsp
0042BFF5  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0042BFF9  48 8B 05 80 C3 9D 00            mov rax, qword ptr [rip + 0x9dc380]
0042C000  4C 8B F9                        mov r15, rcx
0042C003  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0042C007  E8 48 0F 00 00                  call 0x14042cf54
0042C00C  8B 0D FA 0D AE 00               mov ecx, dword ptr [rip + 0xae0dfa]
0042C012  4C 8D 05 E7 3F BD FF            lea r8, [rip - 0x42c019]
0042C019  45 33 D2                        xor r10d, r10d
0042C01C  44 0F B6 E0                     movzx r12d, al
0042C020  41 8A C2                        mov al, r10b
0042C023  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
0042C027  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0042C02A  45 8A EA                        mov r13b, r10b
0042C02D  41 8B C2                        mov eax, r10d
0042C030  44 89 6D CB                     mov dword ptr [rbp - 0x35], r13d
0042C034  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0042C038  41 8D 7A 40                     lea edi, [r10 + 0x40]
0042C03C  45 8B F2                        mov r14d, r10d
0042C03F  89 4D DB                        mov dword ptr [rbp - 0x25], ecx
0042C042  44 89 55 D3                     mov dword ptr [rbp - 0x2d], r10d
0042C046  EB 03                           jmp 0x14042c04b
0042C048  45 33 D2                        xor r10d, r10d
0042C04B  45 8B 84 C0 F0 B3 E0 00         mov r8d, dword ptr [r8 + rax*8 + 0xe0b3f0]
0042C053  0F 57 C0                        xorps xmm0, xmm0
0042C056  44 89 45 D7                     mov dword ptr [rbp - 0x29], r8d
0042C05A  41 BB 01 00 00 00               mov r11d, 1
0042C060  41 8B C0                        mov eax, r8d
0042C063  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0042C067  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0042C06B  45 85 C0                        test r8d, r8d
0042C06E  74 49                           je 0x14042c0b9
0042C070  41 2B C3                        sub eax, r11d
0042C073  0F 84 25 06 00 00               je 0x14042c69e
0042C079  41 2B C3                        sub eax, r11d
0042C07C  0F 84 47 05 00 00               je 0x14042c5c9
0042C082  41 2B C3                        sub eax, r11d
0042C085  0F 84 79 06 00 00               je 0x14042c704
0042C08B  41 2B C3                        sub eax, r11d
0042C08E  0F 84 C5 06 00 00               je 0x14042c759
0042C094  41 2B C3                        sub eax, r11d
0042C097  0F 85 9F 05 00 00               jne 0x14042c63c
0042C09D  48 8B 15 F4 B6 AD 00            mov rdx, qword ptr [rip + 0xadb6f4]
0042C0A4  4D 8D B7 D8 02 00 00            lea r14, [r15 + 0x2d8]
0042C0AB  48 85 D2                        test rdx, rdx
0042C0AE  0F 85 E1 04 00 00               jne 0x14042c595
0042C0B4  4D 8B CA                        mov r9, r10
0042C0B7  EB 1C                           jmp 0x14042c0d5
0042C0B9  4C 8B 0D C0 C2 9D 00            mov r9, qword ptr [rip + 0x9dc2c0]
0042C0C0  48 63 05 45 0D AE 00            movsxd rax, dword ptr [rip + 0xae0d45]
0042C0C7  49 83 C1 28                     add r9, 0x28
0042C0CB  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
0042C0D2  4C 03 C9                        add r9, rcx
0042C0D5  4D 85 C9                        test r9, r9
0042C0D8  0F 84 5B 04 00 00               je 0x14042c539
0042C0DE  41 0F 10 11                     movups xmm2, xmmword ptr [r9]
0042C0E2  49 8B C4                        mov rax, r12
0042C0E5  48 03 C0                        add rax, rax
0042C0E8  41 0F 10 1C C1                  movups xmm3, xmmword ptr [r9 + rax*8]
0042C0ED  49 8B CE                        mov rcx, r14
0042C0F0  F3 0F 7F 5D 07                  movdqu xmmword ptr [rbp + 7], xmm3
0042C0F5  F3 0F 7F 55 17                  movdqu xmmword ptr [rbp + 0x17], xmm2
0042C0FA  4D 85 F6                        test r14, r14
0042C0FD  0F 84 D0 00 00 00               je 0x14042c1d3
0042C103  44 39 15 36 AA B9 00            cmp dword ptr [rip + 0xb9aa36], r10d
0042C10A  41 8B F2                        mov esi, r10d
0042C10D  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
0042C111  0F 44 F7                        cmove esi, edi
0042C114  44 39 15 8D AC B9 00            cmp dword ptr [rip + 0xb9ac8d], r10d
0042C11B  41 0F 10 4E 10                  movups xmm1, xmmword ptr [r14 + 0x10]
0042C120  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0042C124  0F 11 4D F7                     movups xmmword ptr [rbp - 9], xmm1
0042C128  0F 85 B6 06 00 00               jne 0x14042c7e4
0042C12E  44 38 15 A7 A9 B9 00            cmp byte ptr [rip + 0xb9a9a7], r10b
0042C135  0F 84 B2 06 00 00               je 0x14042c7ed
0042C13B  4D 85 C9                        test r9, r9
0042C13E  74 47                           je 0x14042c187
0042C140  F3 0F 6F 05 D0 83 BE FF         movdqu xmm0, xmmword ptr [rip - 0x417c30]
0042C148  0F 54 D0                        andps xmm2, xmm0
0042C14B  66 0F 6F C2                     movdqa xmm0, xmm2
0042C14F  66 0F 73 D8 08                  psrldq xmm0, 8
0042C154  0F 56 D0                        orps xmm2, xmm0
0042C157  66 48 0F 7E D0                  movq rax, xmm2
0042C15C  48 85 C0                        test rax, rax
0042C15F  75 29                           jne 0x14042c18a
0042C161  F3 0F 6F 0D BF 83 BE FF         movdqu xmm1, xmmword ptr [rip - 0x417c41]
0042C169  0F 54 CB                        andps xmm1, xmm3
0042C16C  66 0F 6F C1                     movdqa xmm0, xmm1
0042C170  66 0F 73 D8 08                  psrldq xmm0, 8
0042C175  0F 56 C8                        orps xmm1, xmm0
0042C178  66 48 0F 7E C8                  movq rax, xmm1
0042C17D  48 85 C0                        test rax, rax
0042C180  75 08                           jne 0x14042c18a
0042C182  83 CE 04                        or esi, 4
0042C185  EB 03                           jmp 0x14042c18a
0042C187  83 CE 02                        or esi, 2
0042C18A  48 8B 15 EF C1 9D 00            mov rdx, qword ptr [rip + 0x9dc1ef]
0042C191  48 8B 42 0C                     mov rax, qword ptr [rdx + 0xc]
0042C195  48 2B 05 6C 83 BE FF            sub rax, qword ptr [rip - 0x417c94]
0042C19C  75 0B                           jne 0x14042c1a9
0042C19E  48 8B 42 14                     mov rax, qword ptr [rdx + 0x14]
0042C1A2  48 2B 05 67 83 BE FF            sub rax, qword ptr [rip - 0x417c99]
0042C1A9  48 85 C0                        test rax, rax
0042C1AC  75 03                           jne 0x14042c1b1
0042C1AE  83 CE 20                        or esi, 0x20
0042C1B1  44 38 15 38 1F AE 00            cmp byte ptr [rip + 0xae1f38], r10b
0042C1B8  0F 85 1E 06 00 00               jne 0x14042c7dc
0042C1BE  44 39 15 0B AB B9 00            cmp dword ptr [rip + 0xb9ab0b], r10d
0042C1C5  0F 87 2B 06 00 00               ja 0x14042c7f6
0042C1CB  85 F6                           test esi, esi
0042C1CD  0F 85 F5 02 00 00               jne 0x14042c4c8
0042C1D3  41 83 F8 03                     cmp r8d, 3
0042C1D7  0F 85 CE 03 00 00               jne 0x14042c5ab
0042C1DD  F3 0F 6F 05 33 83 BE FF         movdqu xmm0, xmmword ptr [rip - 0x417ccd]
0042C1E5  4C 8B 1D 3C 83 BE FF            mov r11, qword ptr [rip - 0x417cc4]
0042C1EC  4D 8B F2                        mov r14, r10
0042C1EF  F3 0F 7F 45 17                  movdqu xmmword ptr [rbp + 0x17], xmm0
0042C1F4  43 0F B6 5C 0C 2C               movzx ebx, byte ptr [r12 + r9 + 0x2c]
0042C1FA  89 5D E7                        mov dword ptr [rbp - 0x19], ebx
0042C1FD  4D 85 F6                        test r14, r14
0042C200  0F 84 A4 05 00 00               je 0x14042c7aa
0042C206  44 84 DF                        test dil, r11b
0042C209  0F 85 8B 05 00 00               jne 0x14042c79a
0042C20F  8B 7D EF                        mov edi, dword ptr [rbp - 0x11]
0042C212  44 8A 2D DE A8 B9 00            mov r13b, byte ptr [rip + 0xb9a8de]
0042C219  45 84 ED                        test r13b, r13b
0042C21C  0F 84 31 03 00 00               je 0x14042c553
0042C222  4D 85 F6                        test r14, r14
0042C225  0F 85 4C 03 00 00               jne 0x14042c577
0042C22B  43 8B 74 A1 50                  mov esi, dword ptr [r9 + r12*4 + 0x50]
0042C230  89 75 F7                        mov dword ptr [rbp - 9], esi
0042C233  4D 85 F6                        test r14, r14
0042C236  0F 84 10 05 00 00               je 0x14042c74c
0042C23C  49 0F BA E3 0F                  bt r11, 0xf
0042C241  0F 82 F6 04 00 00               jb 0x14042c73d
0042C247  8B 0D 2F 1F AE 00               mov ecx, dword ptr [rip + 0xae1f2f]
0042C24D  85 C9                           test ecx, ecx
0042C24F  0F 85 A9 05 00 00               jne 0x14042c7fe
0042C255  43 8B 4C A1 3C                  mov ecx, dword ptr [r9 + r12*4 + 0x3c]
0042C25A  45 8B 97 C4 01 00 00            mov r10d, dword ptr [r15 + 0x1c4]
0042C261  85 C9                           test ecx, ecx
0042C263  0F 85 73 03 00 00               jne 0x14042c5dc
0042C269  33 C9                           xor ecx, ecx
0042C26B  4D 85 F6                        test r14, r14
0042C26E  0F 84 BF 03 00 00               je 0x14042c633
0042C274  49 0F BA E3 25                  bt r11, 0x25
0042C279  0F 82 AA 03 00 00               jb 0x14042c629
0042C27F  44 8B 55 EB                     mov r10d, dword ptr [rbp - 0x15]
0042C283  38 0D 72 A8 B9 00               cmp byte ptr [rip + 0xb9a872], cl
0042C289  48 8B 55 17                     mov rdx, qword ptr [rbp + 0x17]
0042C28D  0F 85 C8 02 00 00               jne 0x14042c55b
0042C293  4D 85 F6                        test r14, r14
0042C296  74 13                           je 0x14042c2ab
0042C298  48 0F BA E2 0A                  bt rdx, 0xa
0042C29D  73 18                           jae 0x14042c2b7
0042C29F  41 38 4E 16                     cmp byte ptr [r14 + 0x16], cl
0042C2A3  74 12                           je 0x14042c2b7
0042C2A5  41 39 49 48                     cmp dword ptr [r9 + 0x48], ecx
0042C2A9  75 0C                           jne 0x14042c2b7
0042C2AB  41 8A 41 48                     mov al, byte ptr [r9 + 0x48]
0042C2AF  88 45 FD                        mov byte ptr [rbp - 3], al
0042C2B2  4D 85 F6                        test r14, r14
0042C2B5  74 12                           je 0x14042c2c9
0042C2B7  49 0F BA E3 0E                  bt r11, 0xe
0042C2BC  73 1C                           jae 0x14042c2da
0042C2BE  43 8A 44 0C 5D                  mov al, byte ptr [r12 + r9 + 0x5d]
0042C2C3  41 38 46 17                     cmp byte ptr [r14 + 0x17], al
0042C2C7  76 11                           jbe 0x14042c2da
0042C2C9  43 8A 44 0C 5D                  mov al, byte ptr [r12 + r9 + 0x5d]
0042C2CE  88 45 FE                        mov byte ptr [rbp - 2], al
0042C2D1  4D 85 F6                        test r14, r14
0042C2D4  0F 84 50 04 00 00               je 0x14042c72a
0042C2DA  49 0F BA E3 32                  bt r11, 0x32
0042C2DF  0F 82 32 04 00 00               jb 0x14042c717
0042C2E5  41 8A 41 20                     mov al, byte ptr [r9 + 0x20]
0042C2E9  41 BB 01 00 00 00               mov r11d, 1
0042C2EF  41 3A C3                        cmp al, r11b
0042C2F2  0F 85 4C 02 00 00               jne 0x14042c544
0042C2F8  41 8A C3                        mov al, r11b
0042C2FB  4D 85 F6                        test r14, r14
0042C2FE  0F 84 84 03 00 00               je 0x14042c688
0042C304  48 0F BA E2 0B                  bt rdx, 0xb
0042C309  0F 82 79 03 00 00               jb 0x14042c688
0042C30F  41 80 BF 09 02 00 00 02         cmp byte ptr [r15 + 0x209], 2
0042C317  0F 84 11 02 00 00               je 0x14042c52e
0042C31D  41 38 49 5C                     cmp byte ptr [r9 + 0x5c], cl
0042C321  0F 84 91 04 00 00               je 0x14042c7b8
0042C327  44 8A C1                        mov r8b, cl
0042C32A  41 38 8F 08 02 00 00            cmp byte ptr [r15 + 0x208], cl
0042C331  0F 84 81 04 00 00               je 0x14042c7b8
0042C337  4D 85 F6                        test r14, r14
0042C33A  0F 84 D0 02 00 00               je 0x14042c610
0042C340  48 0F BA E2 23                  bt rdx, 0x23
0042C345  0F 82 C5 02 00 00               jb 0x14042c610
0042C34B  44 8B 4D D7                     mov r9d, dword ptr [rbp - 0x29]
0042C34F  3B DF                           cmp ebx, edi
0042C351  0F 42 DF                        cmovb ebx, edi
0042C354  44 3B D7                        cmp r10d, edi
0042C357  89 5D E7                        mov dword ptr [rbp - 0x19], ebx
0042C35A  44 0F 42 D7                     cmovb r10d, edi
0042C35E  44 89 55 EB                     mov dword ptr [rbp - 0x15], r10d
0042C362  41 83 F9 04                     cmp r9d, 4
0042C366  0F 84 45 03 00 00               je 0x14042c6b1
0042C36C  49 8B F3                        mov rsi, r11
0042C36F  45 84 C0                        test r8b, r8b
0042C372  0F 85 48 04 00 00               jne 0x14042c7c0
0042C378  88 4D 00                        mov byte ptr [rbp], cl
0042C37B  49 8B D9                        mov rbx, r9
0042C37E  49 8D 8F 18 02 00 00            lea rcx, [r15 + 0x218]
0042C385  48 C1 E3 05                     shl rbx, 5
0042C389  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0042C38D  48 03 CB                        add rcx, rbx
0042C390  41 B8 20 00 00 00               mov r8d, 0x20
0042C396  49 8B F9                        mov rdi, r9
0042C399  E8 D2 E2 28 00                  call 0x1406ba670
0042C39E  44 0F B6 6D CB                  movzx r13d, byte ptr [rbp - 0x35]
0042C3A3  48 83 F8 20                     cmp rax, 0x20
0042C3A7  0F 10 45 E7                     movups xmm0, xmmword ptr [rbp - 0x19]
0042C3AB  44 0F 45 EE                     cmovne r13d, esi
0042C3AF  41 83 A4 BF F8 02 00 00 00      and dword ptr [r15 + rdi*4 + 0x2f8], 0
0042C3B8  0F 10 4D F7                     movups xmm1, xmmword ptr [rbp - 9]
0042C3BC  44 89 6D CB                     mov dword ptr [rbp - 0x35], r13d
0042C3C0  42 0F 11 84 3B 18 02 00 00      movups xmmword ptr [rbx + r15 + 0x218], xmm0
0042C3C9  42 0F 11 8C 3B 28 02 00 00      movups xmmword ptr [rbx + r15 + 0x228], xmm1
0042C3D2  33 DB                           xor ebx, ebx
0042C3D4  4D 85 F6                        test r14, r14
0042C3D7  0F 85 7B 02 00 00               jne 0x14042c658
0042C3DD  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
0042C3E0  03 D6                           add edx, esi
0042C3E2  89 55 C7                        mov dword ptr [rbp - 0x39], edx
0042C3E5  44 8B 4D D3                     mov r9d, dword ptr [rbp - 0x2d]
0042C3E9  4C 8D 05 10 3C BD FF            lea r8, [rip - 0x42c3f0]
0042C3F0  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0042C3F4  44 03 CE                        add r9d, esi
0042C3F7  8B 4D DB                        mov ecx, dword ptr [rbp - 0x25]
0042C3FA  48 03 C6                        add rax, rsi
0042C3FD  44 89 4D D3                     mov dword ptr [rbp - 0x2d], r9d
0042C401  BF 40 00 00 00                  mov edi, 0x40
0042C406  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0042C40A  41 83 F9 07                     cmp r9d, 7
0042C40E  0F 82 34 FC FF FF               jb 0x14042c048
0042C414  3B D6                           cmp edx, esi
0042C416  8B FB                           mov edi, ebx
0042C418  49 8D B7 14 03 00 00            lea rsi, [r15 + 0x314]
0042C41F  0F 97 C0                        seta al
0042C422  41 88 87 22 03 00 00            mov byte ptr [r15 + 0x322], al
0042C429  8B 45 CF                        mov eax, dword ptr [rbp - 0x31]
0042C42C  41 88 87 0A 02 00 00            mov byte ptr [r15 + 0x20a], al
0042C433  66 89 1E                        mov word ptr [rsi], bx
0042C436  3B FB                           cmp edi, ebx
0042C438  0F 84 52 02 00 00               je 0x14042c690
0042C43E  8B D3                           mov edx, ebx
0042C440  41 B8 20 00 00 00               mov r8d, 0x20
0042C446  48 C1 E2 05                     shl rdx, 5
0042C44A  48 81 C2 18 02 00 00            add rdx, 0x218
0042C451  8B CF                           mov ecx, edi
0042C453  48 C1 E1 05                     shl rcx, 5
0042C457  49 03 D7                        add rdx, r15
0042C45A  48 81 C1 18 02 00 00            add rcx, 0x218
0042C461  49 03 CF                        add rcx, r15
0042C464  E8 07 E2 28 00                  call 0x1406ba670
0042C469  48 83 F8 20                     cmp rax, 0x20
0042C46D  0F 84 1D 02 00 00               je 0x14042c690
0042C473  B8 01 00 00 00                  mov eax, 1
0042C478  03 D8                           add ebx, eax
0042C47A  83 FB 07                        cmp ebx, 7
0042C47D  72 B7                           jb 0x14042c436
0042C47F  03 F8                           add edi, eax
0042C481  8D 58 FF                        lea ebx, [rax - 1]
0042C484  48 83 C6 02                     add rsi, 2
0042C488  83 FF 07                        cmp edi, 7
0042C48B  72 A6                           jb 0x14042c433
0042C48D  33 D2                           xor edx, edx
0042C48F  49 8B CF                        mov rcx, r15
0042C492  E8 71 9C 64 00                  call 0x140a76108
0042C497  41 8A C5                        mov al, r13b
0042C49A  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
0042C49E  48 33 CC                        xor rcx, rsp
0042C4A1  E8 9A 01 28 00                  call 0x1406ac640
0042C4A6  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
0042C4AE  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0042C4B2  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0042C4B6  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0042C4BA  49 8B E3                        mov rsp, r11
0042C4BD  41 5F                           pop r15
0042C4BF  41 5E                           pop r14
0042C4C1  41 5D                           pop r13
0042C4C3  41 5C                           pop r12
0042C4C5  5D                              pop rbp
0042C4C6  C3                              ret
0042C4C7  CC                              int3
0042C4C8  49 8B D8                        mov rbx, r8
0042C4CB  49 8D 8F 18 02 00 00            lea rcx, [r15 + 0x218]
0042C4D2  49 8B F8                        mov rdi, r8
0042C4D5  48 C1 E3 05                     shl rbx, 5
0042C4D9  48 03 CB                        add rcx, rbx
0042C4DC  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0042C4E0  41 B8 20 00 00 00               mov r8d, 0x20
0042C4E6  E8 85 E1 28 00                  call 0x1406ba670
0042C4EB  0F 10 45 E7                     movups xmm0, xmmword ptr [rbp - 0x19]
0042C4EF  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
0042C4F2  48 83 F8 20                     cmp rax, 0x20
0042C4F6  0F 10 4D F7                     movups xmm1, xmmword ptr [rbp - 9]
0042C4FA  B8 01 00 00 00                  mov eax, 1
0042C4FF  45 0F B6 ED                     movzx r13d, r13b
0042C503  42 0F 11 84 3B 18 02 00 00      movups xmmword ptr [rbx + r15 + 0x218], xmm0
0042C50C  44 0F 44 E8                     cmove r13d, eax
0042C510  42 0F 11 8C 3B 28 02 00 00      movups xmmword ptr [rbx + r15 + 0x228], xmm1
0042C519  41 89 B4 BF F8 02 00 00         mov dword ptr [r15 + rdi*4 + 0x2f8], esi
0042C521  33 DB                           xor ebx, ebx
0042C523  8B F0                           mov esi, eax
0042C525  44 89 6D CB                     mov dword ptr [rbp - 0x35], r13d
0042C529  E9 B7 FE FF FF                  jmp 0x14042c3e5
0042C52E  44 8A C1                        mov r8b, cl
0042C531  E9 01 FE FF FF                  jmp 0x14042c337
0042C536  4D 8B CA                        mov r9, r10
0042C539  0F 57 D2                        xorps xmm2, xmm2
0042C53C  0F 57 DB                        xorps xmm3, xmm3
0042C53F  E9 A9 FB FF FF                  jmp 0x14042c0ed
0042C544  3C 02                           cmp al, 2
0042C546  0F 84 B2 00 00 00               je 0x14042c5fe
0042C54C  8A C1                           mov al, cl
0042C54E  E9 A8 FD FF FF                  jmp 0x14042c2fb
0042C553  8B 75 F7                        mov esi, dword ptr [rbp - 9]
0042C556  E9 EC FC FF FF                  jmp 0x14042c247
0042C55B  4D 85 F6                        test r14, r14
0042C55E  74 0B                           je 0x14042c56b
0042C560  48 0F BA E2 22                  bt rdx, 0x22
0042C565  0F 83 2D FD FF FF               jae 0x14042c298
0042C56B  41 8B 41 58                     mov eax, dword ptr [r9 + 0x58]
0042C56F  89 45 F3                        mov dword ptr [rbp - 0xd], eax
0042C572  E9 1C FD FF FF                  jmp 0x14042c293
0042C577  49 0F BA E3 21                  bt r11, 0x21
0042C57C  73 0F                           jae 0x14042c58d
0042C57E  43 8B 44 A1 50                  mov eax, dword ptr [r9 + r12*4 + 0x50]
0042C583  41 39 46 10                     cmp dword ptr [r14 + 0x10], eax
0042C587  0F 82 9E FC FF FF               jb 0x14042c22b
0042C58D  8B 75 F7                        mov esi, dword ptr [rbp - 9]
0042C590  E9 A7 FC FF FF                  jmp 0x14042c23c
0042C595  48 63 C1                        movsxd rax, ecx
0042C598  4C 69 C8 E8 01 00 00            imul r9, rax, 0x1e8
0042C59F  49 83 C1 28                     add r9, 0x28
0042C5A3  4C 03 CA                        add r9, rdx
0042C5A6  E9 2A FB FF FF                  jmp 0x14042c0d5
0042C5AB  4C 8B 5D 07                     mov r11, qword ptr [rbp + 7]
0042C5AF  48 85 C9                        test rcx, rcx
0042C5B2  0F 84 3C FC FF FF               je 0x14042c1f4
0042C5B8  45 84 DB                        test r11b, r11b
0042C5BB  0F 88 C5 01 00 00               js 0x14042c786
0042C5C1  8B 5D E7                        mov ebx, dword ptr [rbp - 0x19]
0042C5C4  E9 3D FC FF FF                  jmp 0x14042c206
0042C5C9  48 8B 15 B8 B1 AD 00            mov rdx, qword ptr [rip + 0xadb1b8]
0042C5D0  4D 8D B7 38 02 00 00            lea r14, [r15 + 0x238]
0042C5D7  E9 CF FA FF FF                  jmp 0x14042c0ab
0042C5DC  45 8B 87 C0 01 00 00            mov r8d, dword ptr [r15 + 0x1c0]
0042C5E3  33 D2                           xor edx, edx
0042C5E5  6B C9 64                        imul ecx, ecx, 0x64
0042C5E8  41 8B C0                        mov eax, r8d
0042C5EB  D1 E8                           shr eax, 1
0042C5ED  03 C1                           add eax, ecx
0042C5EF  41 F7 F0                        div r8d
0042C5F2  41 3B C2                        cmp eax, r10d
0042C5F5  44 0F 42 D0                     cmovb r10d, eax
0042C5F9  E9 6B FC FF FF                  jmp 0x14042c269
0042C5FE  41 38 8F EC 01 00 00            cmp byte ptr [r15 + 0x1ec], cl
0042C605  0F 85 ED FC FF FF               jne 0x14042c2f8
0042C60B  E9 3C FF FF FF                  jmp 0x14042c54c
0042C610  8B 45 CF                        mov eax, dword ptr [rbp - 0x31]
0042C613  45 84 C0                        test r8b, r8b
0042C616  0F B6 C0                        movzx eax, al
0042C619  41 0F 45 C3                     cmovne eax, r11d
0042C61D  44 88 45 FB                     mov byte ptr [rbp - 5], r8b
0042C621  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0042C624  E9 22 FD FF FF                  jmp 0x14042c34b
0042C629  45 39 56 04                     cmp dword ptr [r14 + 4], r10d
0042C62D  0F 86 4C FC FF FF               jbe 0x14042c27f
0042C633  44 89 55 EB                     mov dword ptr [rbp - 0x15], r10d
0042C637  E9 47 FC FF FF                  jmp 0x14042c283
0042C63C  83 F8 01                        cmp eax, 1
0042C63F  0F 85 74 FA FF FF               jne 0x14042c0b9
0042C645  48 8B 15 54 B1 AD 00            mov rdx, qword ptr [rip + 0xadb154]
0042C64C  4D 8D B7 58 02 00 00            lea r14, [r15 + 0x258]
0042C653  E9 53 FA FF FF                  jmp 0x14042c0ab
0042C658  41 B8 20 00 00 00               mov r8d, 0x20
0042C65E  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0042C662  49 8B CE                        mov rcx, r14
0042C665  E8 06 E0 28 00                  call 0x1406ba670
0042C66A  48 83 F8 20                     cmp rax, 0x20
0042C66E  0F 85 69 FD FF FF               jne 0x14042c3dd
0042C674  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
0042C677  41 C7 84 BF F8 02 00 00 08 00 00 00  mov dword ptr [r15 + rdi*4 + 0x2f8], 8
0042C683  E9 5D FD FF FF                  jmp 0x14042c3e5
0042C688  88 45 FC                        mov byte ptr [rbp - 4], al
0042C68B  E9 7F FC FF FF                  jmp 0x14042c30f
0042C690  0F B7 06                        movzx eax, word ptr [rsi]
0042C693  0F AB D8                        bts eax, ebx
0042C696  66 89 06                        mov word ptr [rsi], ax
0042C699  E9 D5 FD FF FF                  jmp 0x14042c473
0042C69E  48 8B 15 EB B0 AD 00            mov rdx, qword ptr [rip + 0xadb0eb]
0042C6A5  4D 8D B7 18 02 00 00            lea r14, [r15 + 0x218]
0042C6AC  E9 FA F9 FF FF                  jmp 0x14042c0ab
0042C6B1  41 0F B6 97 8F 02 00 00         movzx edx, byte ptr [r15 + 0x28f]
0042C6B9  41 3B DA                        cmp ebx, r10d
0042C6BC  41 8B C2                        mov eax, r10d
0042C6BF  0F 42 C3                        cmovb eax, ebx
0042C6C2  3B C2                           cmp eax, edx
0042C6C4  0F 82 5F 01 00 00               jb 0x14042c829
0042C6CA  8B C2                           mov eax, edx
0042C6CC  3B F8                           cmp edi, eax
0042C6CE  77 16                           ja 0x14042c6e6
0042C6D0  41 3B DA                        cmp ebx, r10d
0042C6D3  41 8B CA                        mov ecx, r10d
0042C6D6  0F 42 CB                        cmovb ecx, ebx
0042C6D9  3B CA                           cmp ecx, edx
0042C6DB  0F 82 56 01 00 00               jb 0x14042c837
0042C6E1  89 55 EF                        mov dword ptr [rbp - 0x11], edx
0042C6E4  33 C9                           xor ecx, ecx
0042C6E6  45 84 ED                        test r13b, r13b
0042C6E9  0F 84 7D FC FF FF               je 0x14042c36c
0042C6EF  41 0F B6 87 90 02 00 00         movzx eax, byte ptr [r15 + 0x290]
0042C6F7  3B F0                           cmp esi, eax
0042C6F9  0F 43 F0                        cmovae esi, eax
0042C6FC  89 75 F7                        mov dword ptr [rbp - 9], esi
0042C6FF  E9 68 FC FF FF                  jmp 0x14042c36c
0042C704  48 8B 15 75 B0 AD 00            mov rdx, qword ptr [rip + 0xadb075]
0042C70B  4D 8D B7 18 02 00 00            lea r14, [r15 + 0x218]
0042C712  E9 94 F9 FF FF                  jmp 0x14042c0ab
0042C717  43 0F B6 84 0C AF 00 00 00      movzx eax, byte ptr [r12 + r9 + 0xaf]
0042C720  41 39 46 1C                     cmp dword ptr [r14 + 0x1c], eax
0042C724  0F 86 BB FB FF FF               jbe 0x14042c2e5
0042C72A  43 0F B6 8C 0C AF 00 00 00      movzx ecx, byte ptr [r12 + r9 + 0xaf]
0042C733  89 4D 03                        mov dword ptr [rbp + 3], ecx
0042C736  33 C9                           xor ecx, ecx
0042C738  E9 A8 FB FF FF                  jmp 0x14042c2e5
0042C73D  43 8A 44 0C 5F                  mov al, byte ptr [r12 + r9 + 0x5f]
0042C742  41 38 46 18                     cmp byte ptr [r14 + 0x18], al
0042C746  0F 83 FB FA FF FF               jae 0x14042c247
0042C74C  43 8A 44 0C 5F                  mov al, byte ptr [r12 + r9 + 0x5f]
0042C751  88 45 FF                        mov byte ptr [rbp - 1], al
0042C754  E9 EE FA FF FF                  jmp 0x14042c247
0042C759  4C 39 15 20 B0 AD 00            cmp qword ptr [rip + 0xadb020], r10
0042C760  4D 8D B7 18 02 00 00            lea r14, [r15 + 0x218]
0042C767  0F 84 C9 FD FF FF               je 0x14042c536
0042C76D  48 63 C1                        movsxd rax, ecx
0042C770  4C 69 C8 E8 01 00 00            imul r9, rax, 0x1e8
0042C777  48 8D 05 6A B0 AD 00            lea rax, [rip + 0xadb06a]
0042C77E  4C 03 C8                        add r9, rax
0042C781  E9 4F F9 FF FF                  jmp 0x14042c0d5
0042C786  43 0F B6 44 0C 2C               movzx eax, byte ptr [r12 + r9 + 0x2c]
0042C78C  41 39 06                        cmp dword ptr [r14], eax
0042C78F  0F 86 2C FE FF FF               jbe 0x14042c5c1
0042C795  E9 5A FA FF FF                  jmp 0x14042c1f4
0042C79A  43 0F B6 44 0C 2A               movzx eax, byte ptr [r12 + r9 + 0x2a]
0042C7A0  41 39 46 08                     cmp dword ptr [r14 + 8], eax
0042C7A4  0F 86 65 FA FF FF               jbe 0x14042c20f
0042C7AA  43 0F B6 7C 0C 2A               movzx edi, byte ptr [r12 + r9 + 0x2a]
0042C7B0  89 7D EF                        mov dword ptr [rbp - 0x11], edi
0042C7B3  E9 5A FA FF FF                  jmp 0x14042c212
0042C7B8  45 8A C3                        mov r8b, r11b
0042C7BB  E9 77 FB FF FF                  jmp 0x14042c337
0042C7C0  48 8D 0D 39 38 BD FF            lea rcx, [rip - 0x42c7c7]
0042C7C7  42 8B 8C 89 18 75 FC 00         mov ecx, dword ptr [rcx + r9*4 + 0xfc7518]
0042C7CF  3B CE                           cmp ecx, esi
0042C7D1  75 74                           jne 0x14042c847
0042C7D3  40 88 75 00                     mov byte ptr [rbp], sil
0042C7D7  E9 9F FB FF FF                  jmp 0x14042c37b
0042C7DC  83 CE 10                        or esi, 0x10
0042C7DF  E9 DA F9 FF FF                  jmp 0x14042c1be
0042C7E4  0F BA EE 08                     bts esi, 8
0042C7E8  E9 41 F9 FF FF                  jmp 0x14042c12e
0042C7ED  0F BA EE 07                     bts esi, 7
0042C7F1  E9 45 F9 FF FF                  jmp 0x14042c13b
0042C7F6  41 0B F3                        or esi, r11d
0042C7F9  E9 CD F9 FF FF                  jmp 0x14042c1cb
0042C7FE  45 8B 87 C0 01 00 00            mov r8d, dword ptr [r15 + 0x1c0]
0042C805  33 D2                           xor edx, edx
0042C807  6B C9 64                        imul ecx, ecx, 0x64
0042C80A  41 8B C0                        mov eax, r8d
0042C80D  D1 E8                           shr eax, 1
0042C80F  03 C1                           add eax, ecx
0042C811  41 F7 F0                        div r8d
0042C814  3B C3                           cmp eax, ebx
0042C816  0F 42 D8                        cmovb ebx, eax
0042C819  3B C7                           cmp eax, edi
0042C81B  89 5D E7                        mov dword ptr [rbp - 0x19], ebx
0042C81E  0F 42 F8                        cmovb edi, eax
0042C821  89 7D EF                        mov dword ptr [rbp - 0x11], edi
0042C824  E9 2C FA FF FF                  jmp 0x14042c255
0042C829  41 3B DA                        cmp ebx, r10d
0042C82C  41 8B C2                        mov eax, r10d
0042C82F  0F 42 C3                        cmovb eax, ebx
0042C832  E9 95 FE FF FF                  jmp 0x14042c6cc
0042C837  41 3B DA                        cmp ebx, r10d
0042C83A  44 0F 42 D3                     cmovb r10d, ebx
0042C83E  44 89 55 EF                     mov dword ptr [rbp - 0x11], r10d
0042C842  E9 9D FE FF FF                  jmp 0x14042c6e4
0042C847  83 F9 03                        cmp ecx, 3
0042C84A  0F 85 D8 1B 2C 00               jne 0x1406ee428
0042C850  33 C9                           xor ecx, ecx
0042C852  41 38 8F 2C 01 00 00            cmp byte ptr [r15 + 0x12c], cl
0042C859  0F 87 74 FF FF FF               ja 0x14042c7d3
0042C85F  E9 14 FB FF FF                  jmp 0x14042c378
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfCalculateQosClassPolicies(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 10348366)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    result = PpmGetPerfPolicyClass(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
    v_r10 = 0;
    *(unsigned int *)(v_rsp - 95 - 57) = 0;
    *(unsigned int *)(v_rsp - 95 - 49) = 0;
    *(unsigned int *)(v_rsp - 95 - 53) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned int *)(v_rsp - 95 - 37) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11406842)));
    *(unsigned int *)(v_rsp - 95 - 45) = 0;
    goto loc_0042C04B;
loc_0042C048:
    v_r10 = 0;
loc_0042C04B:
    *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4374553 + 0 * 8 + 14726128)));
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4374553 + 0 * 8 + 14726128))) == 0) goto loc_0042C0B9;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4374553 + 0 * 8 + 14726128))))) - (1));
    if (condition_is_equal) goto loc_0042C69E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0042C5C9;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0042C704;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0042C759;
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_0042C63C;
loc_0042C0AB:
    if (*(unsigned __int64 *)(v_rip + 11384564) != 0) goto loc_0042C595;
    goto loc_0042C0D5;
loc_0042C0B9:
    a4 = (*(unsigned __int64 *)(v_rip + 10339008)) + (40);
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 11406842))) * ((int)(*(unsigned int *)(v_rip + 11406661)));
    a4 = (a4) + (a1);
loc_0042C0D5:
    if (a4 == 0) goto loc_0042C539;
    result = ((unsigned __int8)(result)) + ((unsigned __int8)(result));
loc_0042C0ED:
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm3;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm2;
    if (a1 + 728 == 0) goto loc_0042C1D3;
    v_rsi = 0;
    if ((*(unsigned int *)(v_rip + 12167734)) == 0) { v_rsi = (unsigned int)(v_r10 + 64); }
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm1;
    if ((*(unsigned int *)(v_rip + 12168333)) != 0) goto loc_0042C7E4;
loc_0042C12E:
    if ((*(unsigned __int8 *)(v_rip + 12167591)) == 0) goto loc_0042C7ED;
loc_0042C13B:
    if (a4 == 0) goto loc_0042C187;
    if (result != 0) goto loc_0042C18A;
    if (result != 0) goto loc_0042C18A;
    v_rsi = (unsigned int)((v_rsi) | (4));
    goto loc_0042C18A;
loc_0042C187:
    v_rsi = (unsigned int)((v_rsi) | (2));
loc_0042C18A:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10338799) + 12)) - (*(unsigned __int64 *)(v_rip - 4291732));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10338799) + 20);
        result = (result) - (*(unsigned __int64 *)(v_rip - 4291737));
    }
    if (result == 0) {
        v_rsi = (unsigned int)((v_rsi) | (32));
    }
    if ((*(unsigned __int8 *)(v_rip + 11411256)) != 0) goto loc_0042C7DC;
loc_0042C1BE:
    if ((*(unsigned int *)(v_rip + 12167947)) > 0) goto loc_0042C7F6;
loc_0042C1CB:
    if ((unsigned int)(v_rsi) != 0) goto loc_0042C4C8;
loc_0042C1D3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4374553 + 0 * 8 + 14726128)))) != 3) goto loc_0042C5AB;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
loc_0042C1F4:
    *(unsigned int *)(v_rsp - 95 - 25) = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 44));
    if (0 == 0) goto loc_0042C7AA;
loc_0042C206:
    if ((((unsigned __int8)(v_r10 + 64)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 4291780)))) != 0) goto loc_0042C79A;
loc_0042C20F:
loc_0042C212:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12167390)) == 0) goto loc_0042C553;
    if (0 != 0) goto loc_0042C577;
loc_0042C22B:
    *(unsigned int *)(v_rsp - 95 - 9) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + (unsigned __int8)(result) * 4 + 80)));
    if (0 == 0) goto loc_0042C74C;
loc_0042C23C:
    if (condition_is_below) goto loc_0042C73D;
loc_0042C247:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11411247))) != 0) goto loc_0042C7FE;
loc_0042C255:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + (unsigned __int8)(result) * 4 + 60))) != 0) goto loc_0042C5DC;
loc_0042C269:
    a1 = 0;
    if (0 == 0) goto loc_0042C633;
    if (condition_is_below) goto loc_0042C629;
loc_0042C27F:
loc_0042C283:
    if ((*(unsigned __int8 *)(v_rip + 12167282)) != 0) goto loc_0042C55B;
loc_0042C293:
    if (0 == 0) goto loc_0042C2AB;
loc_0042C298:
    if (condition_is_above_or_equal) goto loc_0042C2B7;
    if ((*(unsigned __int8 *)(0 + 22)) == 0) goto loc_0042C2B7;
    if ((*(unsigned int *)(a4 + 72)) != 0) goto loc_0042C2B7;
loc_0042C2AB:
    *(unsigned __int8 *)(v_rsp - 95 - 3) = (unsigned __int8)(*(unsigned __int8 *)(a4 + 72));
    if (0 == 0) goto loc_0042C2C9;
loc_0042C2B7:
    if (condition_is_above_or_equal) goto loc_0042C2DA;
    if ((*(unsigned __int8 *)(0 + 23)) <= ((unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 93)))) goto loc_0042C2DA;
loc_0042C2C9:
    *(unsigned __int8 *)(v_rsp - 95 - 2) = (unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 93));
    if (0 == 0) goto loc_0042C72A;
loc_0042C2DA:
    if (condition_is_below) goto loc_0042C717;
loc_0042C2E5:
    if (((unsigned __int8)(*(unsigned __int8 *)(a4 + 32))) != 1) goto loc_0042C544;
loc_0042C2F8:
loc_0042C2FB:
    if (0 == 0) goto loc_0042C688;
    if (condition_is_below) goto loc_0042C688;
loc_0042C30F:
    if ((*(unsigned __int8 *)(a1 + 521)) == 2) goto loc_0042C52E;
    if ((*(unsigned __int8 *)(a4 + 92)) == 0) goto loc_0042C7B8;
    if ((*(unsigned __int8 *)(a1 + 520)) == 0) goto loc_0042C7B8;
loc_0042C337:
    if (0 == 0) goto loc_0042C610;
    if (condition_is_below) goto loc_0042C610;
loc_0042C34B:
    v_rbx = *(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 44);
    if (((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 44))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))))) { v_rbx = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))); }
    *(unsigned int *)(v_rsp - 95 - 25) = (unsigned int)(v_rbx);
    v_r10 = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 21));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 21)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))))) { v_r10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))); }
    *(unsigned int *)(v_rsp - 95 - 21) = (unsigned int)(v_r10);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 41)))) == 4) goto loc_0042C6B1;
loc_0042C36C:
    if (0 != 0) goto loc_0042C7C0;
loc_0042C378:
    *(unsigned __int8 *)(v_rsp - 95) = 0;
loc_0042C37B:
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rsp - 95 - 41))) << (5);
    a1 = (a1 + 536) + (v_rbx);
    result = RtlCompareMemory(a1, v_rsp - 95 - 25, 32, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 41)));
    v_r13 = *(unsigned __int8 *)(v_rsp - 95 - 53);
    if (result != 32) { v_r13 = 1; }
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_rbx + a1 * 1 + 536) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + a1 * 1 + 552) = v_xmm1;
    v_rbx = 0;
    if (0 != 0) goto loc_0042C658;
loc_0042C3DD:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))) + (1));
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(a2);
loc_0042C3E5:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 45))) + (1));
    result = (*(unsigned __int64 *)(v_rsp - 95 - 33)) + (1);
    *(unsigned int *)(v_rsp - 95 - 45) = (unsigned int)(a4);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = result;
    if (((unsigned int)(a4)) < 7) goto loc_0042C048;
    result = (((unsigned int)(a2)) > 1) ? 1 : 0;
    *(unsigned __int8 *)(a1 + 802) = (unsigned __int8)(result);
    *(unsigned __int8 *)(a1 + 522) = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 49)));
loc_0042C433:
    *(unsigned __int16 *)(a1 + 788) = 0;
loc_0042C436:
    if (0 == 0) goto loc_0042C690;
    a2 = (0) << (5);
    a2 = (a2) + (536);
    a1 = (0) << (5);
    a2 = (a2) + (a1);
    a1 = (a1) + (536);
    a1 = (a1) + (a1);
    result = RtlCompareMemory(a1, a2, 32, a4);
    if (result == 32) goto loc_0042C690;
loc_0042C473:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((unsigned int)(v_rbx)) < 7) goto loc_0042C436;
    v_rdi = (unsigned int)((0) + (1));
    v_rsi = (a1 + 788) + (2);
    if (((unsigned int)(v_rdi)) < 7) goto loc_0042C433;
    a2 = 0;
    result = PpmEventQosClassPolicy(a1, a2, 32, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 32, a4);
    return result;
loc_0042C4C8:
    v_rbx = (32) << (5);
    a1 = (a1 + 536) + (v_rbx);
    result = RtlCompareMemory(a1, v_rsp - 95 - 25, 32, a4);
    *(unsigned __int64 *)(v_rbx + a1 * 1 + 536) = v_xmm0;
    v_r13 = (unsigned __int8)(v_r13);
    if (result == 32) { v_r13 = 1; }
    *(unsigned __int64 *)(v_rbx + a1 * 1 + 552) = v_xmm1;
    *(unsigned int *)(a1 + 32 * 4 + 760) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    v_rbx = 0;
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(v_r13);
    goto loc_0042C3E5;
loc_0042C52E:
    goto loc_0042C337;
loc_0042C536:
loc_0042C539:
    goto loc_0042C0ED;
loc_0042C544:
    if (1 == 2) goto loc_0042C5FE;
loc_0042C54C:
    goto loc_0042C2FB;
loc_0042C553:
    goto loc_0042C247;
loc_0042C55B:
    if (0 == 0) goto loc_0042C56B;
    if (condition_is_above_or_equal) goto loc_0042C298;
loc_0042C56B:
    *(unsigned int *)(v_rsp - 95 - 13) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 88)));
    goto loc_0042C293;
loc_0042C577:
    if (condition_is_above_or_equal) goto loc_0042C58D;
    if ((*(unsigned int *)(0 + 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + (unsigned __int8)(result) * 4 + 80))))) goto loc_0042C22B;
loc_0042C58D:
    goto loc_0042C23C;
loc_0042C595:
    a4 = (v_r10) * ((int)((unsigned int)(a1)));
    a4 = (a4) + (40);
    a4 = (a4) + ((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)));
    goto loc_0042C0D5;
loc_0042C5AB:
    if (a1 == 0) goto loc_0042C1F4;
    if (sign_flag) goto loc_0042C786;
loc_0042C5C1:
    goto loc_0042C206;
loc_0042C5C9:
    goto loc_0042C0AB;
loc_0042C5DC:
    a2 = 0;
    a1 = (unsigned int)((a1) * ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 448))))) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    if (((unsigned int)(result)) < ((unsigned int)(v_r10))) { v_r10 = (unsigned int)(result); }
    goto loc_0042C269;
loc_0042C5FE:
    if ((*(unsigned __int8 *)(a1 + 492)) != ((unsigned __int8)(a1))) goto loc_0042C2F8;
    goto loc_0042C54C;
loc_0042C610:
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 49)));
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 448))) != 0) { result = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 7)); }
    *(unsigned __int8 *)(v_rsp - 95 - 5) = (unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 448)));
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(result);
    goto loc_0042C34B;
loc_0042C629:
    if ((*(unsigned int *)(a1 + 568 + 4)) <= ((unsigned int)(v_r10))) goto loc_0042C27F;
loc_0042C633:
    *(unsigned int *)(v_rsp - 95 - 21) = (unsigned int)(v_r10);
    goto loc_0042C283;
loc_0042C63C:
    if (((unsigned int)(result)) != 1) goto loc_0042C0B9;
    goto loc_0042C0AB;
loc_0042C658:
    result = RtlCompareMemory(a1 + 600, v_rsp - 95 - 25, 32, a4);
    if (result != 32) goto loc_0042C3DD;
    *(unsigned int *)(a1 + 32 * 4 + 760) = 8;
    goto loc_0042C3E5;
loc_0042C688:
    *(unsigned __int8 *)(v_rsp - 95 - 4) = (unsigned __int8)(result);
    goto loc_0042C30F;
loc_0042C690:
    *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 9))) = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 9))));
    goto loc_0042C473;
loc_0042C69E:
    goto loc_0042C0AB;
loc_0042C6B1:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 25)))) < ((unsigned int)(v_r10))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 25))); }
    if (((unsigned int)(result)) < ((unsigned int)(*(unsigned __int8 *)(a1 + 655)))) goto loc_0042C829;
loc_0042C6CC:
    if (32 > ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 655)))))) goto loc_0042C6E6;
    a1 = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 25)))) < ((unsigned int)(v_r10))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 25))); }
    if (((unsigned int)(a1)) < ((unsigned int)(*(unsigned __int8 *)(a1 + 655)))) goto loc_0042C837;
    *(unsigned int *)(v_rsp - 95 - 17) = (unsigned int)(*(unsigned __int8 *)(a1 + 655));
loc_0042C6E4:
    a1 = 0;
loc_0042C6E6:
    if ((unsigned __int8)(v_r13) == 0) goto loc_0042C36C;
    v_rsi = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 9));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 9)))) >= ((unsigned int)(*(unsigned __int8 *)(a1 + 656)))) { v_rsi = (unsigned int)(*(unsigned __int8 *)(a1 + 656)); }
    *(unsigned int *)(v_rsp - 95 - 9) = (unsigned int)(v_rsi);
    goto loc_0042C36C;
loc_0042C704:
    goto loc_0042C0AB;
loc_0042C717:
    if ((*(unsigned int *)(a1 + 536 + 28)) <= ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 175)))) goto loc_0042C2E5;
loc_0042C72A:
    *(unsigned int *)(v_rsp - 95 + 3) = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 175));
    a1 = 0;
    goto loc_0042C2E5;
loc_0042C73D:
    if ((*(unsigned __int8 *)(a1 + 536 + 24)) >= ((unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 95)))) goto loc_0042C247;
loc_0042C74C:
    *(unsigned __int8 *)(v_rsp - 95 - 1) = (unsigned __int8)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 95));
    goto loc_0042C247;
loc_0042C759:
    if ((*(unsigned __int64 *)(v_rip + 11382816)) == v_r10) goto loc_0042C536;
    a4 = (a4) * ((int)(0));
    a4 = (a4) + (v_rip + 11382890);
    goto loc_0042C0D5;
loc_0042C786:
    if ((*(unsigned int *)(a1 + 536)) <= ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 44)))) goto loc_0042C5C1;
    goto loc_0042C1F4;
loc_0042C79A:
    if ((*(unsigned int *)(a1 + 536 + 8)) <= ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 42)))) goto loc_0042C20F;
loc_0042C7AA:
    *(unsigned int *)(v_rsp - 95 - 17) = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 42));
    goto loc_0042C212;
loc_0042C7B8:
    goto loc_0042C337;
loc_0042C7C0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4376519 + a4 * 4 + 16545048)))) != ((unsigned int)(v_rsi))) goto loc_0042C847;
loc_0042C7D3:
    *(unsigned __int8 *)(v_rsp - 95) = (unsigned __int8)(v_rsi);
    goto loc_0042C37B;
loc_0042C7DC:
    v_rsi = (unsigned int)((v_rsi) | (16));
    goto loc_0042C1BE;
loc_0042C7E4:
    goto loc_0042C12E;
loc_0042C7ED:
    goto loc_0042C13B;
loc_0042C7F6:
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 7))));
    goto loc_0042C1CB;
loc_0042C7FE:
    a2 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 4376519 + a4 * 4 + 16545048))) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4376519 + a4 * 4 + 16545048)))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 448))))) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    v_rbx = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 25));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 25))))) { v_rbx = (unsigned int)(result); }
    *(unsigned int *)(v_rsp - 95 - 25) = (unsigned int)(v_rbx);
    v_rdi = *(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 42);
    if (((unsigned int)(result)) < ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(result) + a4 * 1 + 42)))) { v_rdi = (unsigned int)(result); }
    *(unsigned int *)(v_rsp - 95 - 17) = (unsigned int)(v_rdi);
    goto loc_0042C255;
loc_0042C829:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rbx)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rbx); }
    goto loc_0042C6CC;
loc_0042C837:
    if (((unsigned int)(v_rbx)) < ((unsigned int)(v_r10))) { v_r10 = (unsigned int)(v_rbx); }
    *(unsigned int *)(v_rsp - 95 - 17) = (unsigned int)(v_r10);
    goto loc_0042C6E4;
loc_0042C847:
    a1 = 0;
    if ((*(unsigned __int8 *)(a1 + 300)) > 0) goto loc_0042C7D3;
    goto loc_0042C378;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfCalculateQosClassPolicies(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x9DE74E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    result = PpmGetPerfPolicyClass(*(uint64_t *)(arg1 + 0x10), a2, a3, a4);
    local_r10 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAE0DFA)));
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = 0;
    goto loc_0042C04B;
loc_0042C048:
    local_r10 = 0;
loc_0042C04B:
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x42C019 + 0x0 * 8 + 0xE0B3F0)));
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x42C019 + 0x0 * 8 + 0xE0B3F0))) == 0) goto loc_0042C0B9;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x42C019 + 0x0 * 8 + 0xE0B3F0))))) - (1));
    if (condition_is_equal) goto loc_0042C69E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0042C5C9;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0042C704;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0042C759;
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_0042C63C;
loc_0042C0AB:
    if (*(uint64_t *)(v_rip + 0xADB6F4) != 0) goto loc_0042C595;
    goto loc_0042C0D5;
loc_0042C0B9:
    a4 = (*(uint64_t *)(v_rip + 0x9DC2C0)) + (40);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0xAE0DFA))) * ((int32_t)(*(uint32_t *)(v_rip + 0xAE0D45)));
    a4 = (a4) + (Arg1);
loc_0042C0D5:
    if (a4 == 0) goto loc_0042C539;
    result = ((uint8_t)(result)) + ((uint8_t)(result));
loc_0042C0ED:
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm3;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm2;
    if (Arg1 + 728 == 0) goto loc_0042C1D3;
    local_rsi = 0;
    if ((*(uint32_t *)(v_rip + 0xB9AA36)) == 0) { local_rsi = (uint32_t)(local_r10 + 64); }
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm1;
    if ((*(uint32_t *)(v_rip + 0xB9AC8D)) != 0) goto loc_0042C7E4;
loc_0042C12E:
    if ((*(uint8_t *)(v_rip + 0xB9A9A7)) == 0) goto loc_0042C7ED;
loc_0042C13B:
    if (a4 == 0) goto loc_0042C187;
    if (result != 0) goto loc_0042C18A;
    if (result != 0) goto loc_0042C18A;
    local_rsi = (uint32_t)((local_rsi) | (4));
    goto loc_0042C18A;
loc_0042C187:
    local_rsi = (uint32_t)((local_rsi) | (2));
loc_0042C18A:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9DC1EF) + 0xC)) - (*(uint64_t *)(v_rip - 0x417C94));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x9DC1EF) + 0x14);
        result = (result) - (*(uint64_t *)(v_rip - 0x417C99));
    }
    if (result == 0) {
        local_rsi = (uint32_t)((local_rsi) | (32));
    }
    if ((*(uint8_t *)(v_rip + 0xAE1F38)) != 0) goto loc_0042C7DC;
loc_0042C1BE:
    if ((*(uint32_t *)(v_rip + 0xB9AB0B)) > 0) goto loc_0042C7F6;
loc_0042C1CB:
    if ((uint32_t)(local_rsi) != 0) goto loc_0042C4C8;
loc_0042C1D3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x42C019 + 0x0 * 8 + 0xE0B3F0)))) != 3) goto loc_0042C5AB;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
loc_0042C1F4:
    *(uint32_t *)(local_rsp - 0x5F - 0x19) = (uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2C));
    if (0 == 0) goto loc_0042C7AA;
loc_0042C206:
    if ((((uint8_t)(local_r10 + 64)) & ((uint8_t)(*(uint64_t *)(v_rip - 0x417CC4)))) != 0) goto loc_0042C79A;
loc_0042C20F:
loc_0042C212:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xB9A8DE)) == 0) goto loc_0042C553;
    if (0 != 0) goto loc_0042C577;
loc_0042C22B:
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + (uint8_t)(result) * 4 + 0x50)));
    if (0 == 0) goto loc_0042C74C;
loc_0042C23C:
    if (condition_is_below) goto loc_0042C73D;
loc_0042C247:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAE1F2F))) != 0) goto loc_0042C7FE;
loc_0042C255:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(a4 + (uint8_t)(result) * 4 + 0x3C))) != 0) goto loc_0042C5DC;
loc_0042C269:
    Arg1 = 0;
    if (0 == 0) goto loc_0042C633;
    if (condition_is_below) goto loc_0042C629;
loc_0042C27F:
loc_0042C283:
    if ((*(uint8_t *)(v_rip + 0xB9A872)) != 0) goto loc_0042C55B;
loc_0042C293:
    if (0 == 0) goto loc_0042C2AB;
loc_0042C298:
    if (condition_is_above_or_equal) goto loc_0042C2B7;
    if ((*(uint8_t *)(0 + 0x16)) == 0) goto loc_0042C2B7;
    if ((*(uint32_t *)(a4 + 0x48)) != 0) goto loc_0042C2B7;
loc_0042C2AB:
    *(uint8_t *)(local_rsp - 0x5F - 0x3) = (uint8_t)(*(uint8_t *)(a4 + 0x48));
    if (0 == 0) goto loc_0042C2C9;
loc_0042C2B7:
    if (condition_is_above_or_equal) goto loc_0042C2DA;
    if ((*(uint8_t *)(0 + 0x17)) <= ((uint8_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x5D)))) goto loc_0042C2DA;
loc_0042C2C9:
    *(uint8_t *)(local_rsp - 0x5F - 0x2) = (uint8_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x5D));
    if (0 == 0) goto loc_0042C72A;
loc_0042C2DA:
    if (condition_is_below) goto loc_0042C717;
loc_0042C2E5:
    if (((uint8_t)(*(uint8_t *)(a4 + 0x20))) != 1) goto loc_0042C544;
loc_0042C2F8:
loc_0042C2FB:
    if (0 == 0) goto loc_0042C688;
    if (condition_is_below) goto loc_0042C688;
loc_0042C30F:
    if ((*(uint8_t *)(arg1 + 0x209)) == 2) goto loc_0042C52E;
    if ((*(uint8_t *)(a4 + 0x5C)) == 0) goto loc_0042C7B8;
    if ((*(uint8_t *)(arg1 + 0x208)) == 0) goto loc_0042C7B8;
loc_0042C337:
    if (0 == 0) goto loc_0042C610;
    if (condition_is_below) goto loc_0042C610;
loc_0042C34B:
    local_rbx = *(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2C);
    if (((uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2C))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))))) { local_rbx = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))); }
    *(uint32_t *)(local_rsp - 0x5F - 0x19) = (uint32_t)(local_rbx);
    local_r10 = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x15));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x15)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))))) { local_r10 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))); }
    *(uint32_t *)(local_rsp - 0x5F - 0x15) = (uint32_t)(local_r10);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x29)))) == 4) goto loc_0042C6B1;
loc_0042C36C:
    if (0 != 0) goto loc_0042C7C0;
loc_0042C378:
    *(uint8_t *)(local_rsp - 0x5F) = 0;
loc_0042C37B:
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x29))) << (5);
    Arg1 = (Arg1 + 536) + (local_rbx);
    result = RtlCompareMemory(Arg1, local_rsp - 95 - 25, 32, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x29)));
    local_r13 = *(uint8_t *)(local_rsp - 0x5F - 0x35);
    if (result != 32) { local_r13 = 1; }
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(local_r13);
    *(uint64_t *)(local_rbx + arg1 * 1 + 0x218) = v_xmm0;
    *(uint64_t *)(local_rbx + arg1 * 1 + 0x228) = v_xmm1;
    local_rbx = 0;
    if (0 != 0) goto loc_0042C658;
loc_0042C3DD:
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))) + (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(a2);
loc_0042C3E5:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x2D))) + (1));
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x21)) + (1);
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = (uint32_t)(a4);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = result;
    if (((uint32_t)(a4)) < 7) goto loc_0042C048;
    result = (((uint32_t)(a2)) > 1) ? 1 : 0;
    *(uint8_t *)(arg1 + 0x322) = (uint8_t)(result);
    *(uint8_t *)(arg1 + 0x20A) = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x31)));
loc_0042C433:
    *(uint16_t *)(arg1 + 0x314) = 0;
loc_0042C436:
    if (0 == 0) goto loc_0042C690;
    a2 = (0) << (5);
    a2 = (a2) + (536);
    Arg1 = (0) << (5);
    a2 = (a2) + (Arg1);
    Arg1 = (Arg1) + (536);
    Arg1 = (Arg1) + (Arg1);
    result = RtlCompareMemory(Arg1, a2, 32, a4);
    if (result == 32) goto loc_0042C690;
loc_0042C473:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((uint32_t)(local_rbx)) < 7) goto loc_0042C436;
    local_rdi = (uint32_t)((0) + (1));
    local_rsi = (Arg1 + 788) + (2);
    if (((uint32_t)(local_rdi)) < 7) goto loc_0042C433;
    a2 = 0;
    result = PpmEventQosClassPolicy(Arg1, a2, 32, a4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, 32, a4);
    return result;
loc_0042C4C8:
    local_rbx = (32) << (5);
    Arg1 = (Arg1 + 536) + (local_rbx);
    result = RtlCompareMemory(Arg1, local_rsp - 95 - 25, 32, a4);
    *(uint64_t *)(local_rbx + arg1 * 1 + 0x218) = v_xmm0;
    local_r13 = (uint8_t)(local_r13);
    if (result == 32) { local_r13 = 1; }
    *(uint64_t *)(local_rbx + arg1 * 1 + 0x228) = v_xmm1;
    *(uint32_t *)(arg1 + 0x20 * 4 + 0x2F8) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    local_rbx = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(local_r13);
    goto loc_0042C3E5;
loc_0042C52E:
    goto loc_0042C337;
loc_0042C536:
loc_0042C539:
    goto loc_0042C0ED;
loc_0042C544:
    if (1 == 2) goto loc_0042C5FE;
loc_0042C54C:
    goto loc_0042C2FB;
loc_0042C553:
    goto loc_0042C247;
loc_0042C55B:
    if (0 == 0) goto loc_0042C56B;
    if (condition_is_above_or_equal) goto loc_0042C298;
loc_0042C56B:
    *(uint32_t *)(local_rsp - 0x5F - 0xD) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x58)));
    goto loc_0042C293;
loc_0042C577:
    if (condition_is_above_or_equal) goto loc_0042C58D;
    if ((*(uint32_t *)(0 + 0x10)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + (uint8_t)(result) * 4 + 0x50))))) goto loc_0042C22B;
loc_0042C58D:
    goto loc_0042C23C;
loc_0042C595:
    a4 = (local_r10) * ((int32_t)((uint32_t)(Arg1)));
    a4 = (a4) + (40);
    a4 = (a4) + ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)));
    goto loc_0042C0D5;
loc_0042C5AB:
    if (Arg1 == NULL) goto loc_0042C1F4;
    if (sign_flag) goto loc_0042C786;
loc_0042C5C1:
    goto loc_0042C206;
loc_0042C5C9:
    goto loc_0042C0AB;
loc_0042C5DC:
    a2 = 0;
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C0))))) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) < ((uint32_t)(local_r10))) { local_r10 = (uint32_t)(result); }
    goto loc_0042C269;
loc_0042C5FE:
    if ((*(uint8_t *)(arg1 + 0x1EC)) != ((uint8_t)(Arg1))) goto loc_0042C2F8;
    goto loc_0042C54C;
loc_0042C610:
    result = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x31)));
    if ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C0))) != 0) { result = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x7)); }
    *(uint8_t *)(local_rsp - 0x5F - 0x5) = (uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C0)));
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(result);
    goto loc_0042C34B;
loc_0042C629:
    if ((*(uint32_t *)(arg1 + 0x238 + 0x4)) <= ((uint32_t)(local_r10))) goto loc_0042C27F;
loc_0042C633:
    *(uint32_t *)(local_rsp - 0x5F - 0x15) = (uint32_t)(local_r10);
    goto loc_0042C283;
loc_0042C63C:
    if (((uint32_t)(result)) != 1) goto loc_0042C0B9;
    goto loc_0042C0AB;
loc_0042C658:
    result = RtlCompareMemory(Arg1 + 600, local_rsp - 95 - 25, 32, a4);
    if (result != 32) goto loc_0042C3DD;
    *(uint32_t *)(arg1 + 0x20 * 4 + 0x2F8) = 8;
    goto loc_0042C3E5;
loc_0042C688:
    *(uint8_t *)(local_rsp - 0x5F - 0x4) = (uint8_t)(result);
    goto loc_0042C30F;
loc_0042C690:
    *(uint16_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x9))) = (uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x9))));
    goto loc_0042C473;
loc_0042C69E:
    goto loc_0042C0AB;
loc_0042C6B1:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19)))) < ((uint32_t)(local_r10))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19))); }
    if (((uint32_t)(result)) < ((uint32_t)(*(uint8_t *)(arg1 + 0x28F)))) goto loc_0042C829;
loc_0042C6CC:
    if (32 > ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x28F)))))) goto loc_0042C6E6;
    Arg1 = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19)))) < ((uint32_t)(local_r10))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19))); }
    if (((uint32_t)(Arg1)) < ((uint32_t)(*(uint8_t *)(arg1 + 0x28F)))) goto loc_0042C837;
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = (uint32_t)(*(uint8_t *)(arg1 + 0x28F));
loc_0042C6E4:
    Arg1 = 0;
loc_0042C6E6:
    if ((uint8_t)(local_r13) == 0) goto loc_0042C36C;
    local_rsi = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x9));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x9)))) >= ((uint32_t)(*(uint8_t *)(arg1 + 0x290)))) { local_rsi = (uint32_t)(*(uint8_t *)(arg1 + 0x290)); }
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = (uint32_t)(local_rsi);
    goto loc_0042C36C;
loc_0042C704:
    goto loc_0042C0AB;
loc_0042C717:
    if ((*(uint32_t *)(arg1 + 0x218 + 0x1C)) <= ((uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0xAF)))) goto loc_0042C2E5;
loc_0042C72A:
    *(uint32_t *)(local_rsp - 0x5F + 0x3) = (uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0xAF));
    Arg1 = 0;
    goto loc_0042C2E5;
loc_0042C73D:
    if ((*(uint8_t *)(arg1 + 0x218 + 0x18)) >= ((uint8_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x5F)))) goto loc_0042C247;
loc_0042C74C:
    *(uint8_t *)(local_rsp - 0x5F - 0x1) = (uint8_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x5F));
    goto loc_0042C247;
loc_0042C759:
    if ((*(uint64_t *)(v_rip + 0xADB020)) == local_r10) goto loc_0042C536;
    a4 = (a4) * ((int32_t)(0));
    a4 = (a4) + (v_rip + 11382890);
    goto loc_0042C0D5;
loc_0042C786:
    if ((*(uint32_t *)(arg1 + 0x218)) <= ((uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2C)))) goto loc_0042C5C1;
    goto loc_0042C1F4;
loc_0042C79A:
    if ((*(uint32_t *)(arg1 + 0x218 + 0x8)) <= ((uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2A)))) goto loc_0042C20F;
loc_0042C7AA:
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = (uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2A));
    goto loc_0042C212;
loc_0042C7B8:
    goto loc_0042C337;
loc_0042C7C0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x42C7C7 + a4 * 4 + 0xFC7518)))) != ((uint32_t)(local_rsi))) goto loc_0042C847;
loc_0042C7D3:
    *(uint8_t *)(local_rsp - 0x5F) = (uint8_t)(local_rsi);
    goto loc_0042C37B;
loc_0042C7DC:
    local_rsi = (uint32_t)((local_rsi) | (16));
    goto loc_0042C1BE;
loc_0042C7E4:
    goto loc_0042C12E;
loc_0042C7ED:
    goto loc_0042C13B;
loc_0042C7F6:
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x7))));
    goto loc_0042C1CB;
loc_0042C7FE:
    a2 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x42C7C7 + a4 * 4 + 0xFC7518))) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x42C7C7 + a4 * 4 + 0xFC7518)))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C0))))) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    local_rbx = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19))))) { local_rbx = (uint32_t)(result); }
    *(uint32_t *)(local_rsp - 0x5F - 0x19) = (uint32_t)(local_rbx);
    local_rdi = *(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2A);
    if (((uint32_t)(result)) < ((uint32_t)(*(uint8_t *)((uint8_t)(result) + a4 * 1 + 0x2A)))) { local_rdi = (uint32_t)(result); }
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = (uint32_t)(local_rdi);
    goto loc_0042C255;
loc_0042C829:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rbx)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rbx); }
    goto loc_0042C6CC;
loc_0042C837:
    if (((uint32_t)(local_rbx)) < ((uint32_t)(local_r10))) { local_r10 = (uint32_t)(local_rbx); }
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = (uint32_t)(local_r10);
    goto loc_0042C6E4;
loc_0042C847:
    Arg1 = 0;
    if ((*(uint8_t *)(arg1 + 0x12C)) > 0) goto loc_0042C7D3;
    goto loc_0042C378;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x12C` | `8` | `R` |
| `Arg1` | `+ 0x1C0` | `32` | `R` |
| `Arg1` | `+ 0x1C4` | `32` | `R` |
| `Arg1` | `+ 0x1EC` | `8` | `R` |
| `Arg1` | `+ 0x208` | `8` | `R` |
| `Arg1` | `+ 0x209` | `8` | `R` |
| `Arg1` | `+ 0x20A` | `8` | `W` |
| `Arg1` | `+ 0x218` | `64` | `R` |
| `Arg1` | `+ 0x238` | `64` | `R` |
| `Arg1` | `+ 0x258` | `64` | `R` |
| `Arg1` | `+ 0x28F` | `8` | `R` |
| `Arg1` | `+ 0x290` | `8` | `R` |
| `Arg1` | `+ 0x2D8` | `64` | `R` |
| `Arg1` | `+ 0x2F8 + rdi*4` | `32` | `R/W` |
| `Arg1` | `+ 0x2F8 + rdi*4` | `32` | `W` |
| `Arg1` | `+ 0x314` | `64` | `R` |
| `Arg1` | `+ 0x322` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042BFC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
