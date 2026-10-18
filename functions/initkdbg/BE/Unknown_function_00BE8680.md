# sub_00BE8680

- RVA: `0x00BE8680`–`0x00BE8D28` (길이 `1,704` bytes)
- VA: `0x0000000140BE8680`
- 실행 섹션: `INITKDBG`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6648`
- 디코드: `434`개 명령, `1,704/1,704` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BE8811` → [KeGuardCheckICall](KeGuardCheckICall_function_00BEAA70.md) (function, `0x00BEAA70`)
- `0x00BE881F` → [KiAccessPage](KiAccessPage_function_00BEA740.md) (function, `0x00BEA740`)
- `0x00BE895F` → [KeGuardCheckICall](KeGuardCheckICall_function_00BEAA70.md) (function, `0x00BEAA70`)
- `0x00BE896F` → [KiAccessPage](KiAccessPage_function_00BEA740.md) (function, `0x00BEA740`)
- `0x00BE8B21` → [KeGuardCheckICall](KeGuardCheckICall_function_00BEAA70.md) (function, `0x00BEAA70`)
- `0x00BE8B2F` → [KiAccessPage](KiAccessPage_function_00BEA740.md) (function, `0x00BEA740`)
- `0x00BE8C84` → [KeGuardCheckICall](KeGuardCheckICall_function_00BEAA70.md) (function, `0x00BEAA70`)
- `0x00BE8C92` → [KiAccessPage](KiAccessPage_function_00BEA740.md) (function, `0x00BEA740`)

### Direct callers
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x00519760`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BDF9C1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BE8680  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00BE8685  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00BE868A  53                              push rbx
00BE868B  55                              push rbp
00BE868C  56                              push rsi
00BE868D  57                              push rdi
00BE868E  41 54                           push r12
00BE8690  41 55                           push r13
00BE8692  41 56                           push r14
00BE8694  41 57                           push r15
00BE8696  48 83 EC 78                     sub rsp, 0x78
00BE869A  48 8B E9                        mov rbp, rcx
00BE869D  45 8B F8                        mov r15d, r8d
00BE86A0  44 01 B9 48 08 00 00            add dword ptr [rcx + 0x848], r15d
00BE86A7  4C 8B F2                        mov r14, rdx
00BE86AA  41 8B C8                        mov ecx, r8d
00BE86AD  48 8B C2                        mov rax, rdx
00BE86B0  48 03 CA                        add rcx, rdx
00BE86B3  48 3B D1                        cmp rdx, rcx
00BE86B6  73 0C                           jae 0x140be86c4
00BE86B8  0F 18 00                        prefetchnta byte ptr [rax]
00BE86BB  48 83 C0 40                     add rax, 0x40
00BE86BF  48 3B C1                        cmp rax, rcx
00BE86C2  72 F4                           jb 0x140be86b8
00BE86C4  48 8B 85 38 08 00 00            mov rax, qword ptr [rbp + 0x838]
00BE86CB  48 8D 5A FA                     lea rbx, [rdx - 6]
00BE86CF  44 8B 95 34 08 00 00            mov r10d, dword ptr [rbp + 0x834]
00BE86D6  48 8B F8                        mov rdi, rax
00BE86D9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BE86DE  41 BB 01 00 00 00               mov r11d, 1
00BE86E4  41 8B C7                        mov eax, r15d
00BE86E7  44 89 94 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r10d
00BE86EF  C1 E8 07                        shr eax, 7
00BE86F2  41 B1 FF                        mov r9b, 0xff
00BE86F5  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00BE86F9  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00BE86FE  45 8D 43 01                     lea r8d, [r11 + 1]
00BE8702  85 C0                           test eax, eax
00BE8704  0F 84 3A 03 00 00               je 0x140be8a44
00BE870A  4C 8D 63 01                     lea r12, [rbx + 1]
00BE870E  41 B8 80 00 00 00               mov r8d, 0x80
00BE8714  4C 8D 6B 02                     lea r13, [rbx + 2]
00BE8718  44 89 84 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r8d
00BE8720  8A 53 05                        mov dl, byte ptr [rbx + 5]
00BE8723  49 8B C4                        mov rax, r12
00BE8726  80 3B 4C                        cmp byte ptr [rbx], 0x4c
00BE8729  49 8B CD                        mov rcx, r13
00BE872C  0F 85 40 01 00 00               jne 0x140be8872
00BE8732  4C 8D 63 01                     lea r12, [rbx + 1]
00BE8736  41 80 3C 24 87                  cmp byte ptr [r12], 0x87
00BE873B  48 8D 4B 02                     lea rcx, [rbx + 2]
00BE873F  49 8B C4                        mov rax, r12
00BE8742  0F 85 2A 01 00 00               jne 0x140be8872
00BE8748  4C 8D 6B 02                     lea r13, [rbx + 2]
00BE874C  41 80 7D 00 00                  cmp byte ptr [r13], 0
00BE8751  49 8B CD                        mov rcx, r13
00BE8754  0F 85 18 01 00 00               jne 0x140be8872
00BE875A  80 7B 03 98                     cmp byte ptr [rbx + 3], 0x98
00BE875E  0F 85 0E 01 00 00               jne 0x140be8872
00BE8764  80 7B 04 C3                     cmp byte ptr [rbx + 4], 0xc3
00BE8768  0F 85 04 01 00 00               jne 0x140be8872
00BE876E  80 FA 90                        cmp dl, 0x90
00BE8771  74 09                           je 0x140be877c
00BE8773  80 FA F1                        cmp dl, 0xf1
00BE8776  0F 85 F6 00 00 00               jne 0x140be8872
00BE877C  44 88 4C 24 38                  mov byte ptr [rsp + 0x38], r9b
00BE8781  33 F6                           xor esi, esi
00BE8783  0F 31                           rdtsc
00BE8785  48 C1 E2 20                     shl rdx, 0x20
00BE8789  48 0B C2                        or rax, rdx
00BE878C  48 8B C8                        mov rcx, rax
00BE878F  48 C1 C8 03                     ror rax, 3
00BE8793  48 33 C8                        xor rcx, rax
00BE8796  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00BE87A0  48 F7 E1                        mul rcx
00BE87A3  33 C2                           xor eax, edx
00BE87A5  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00BE87AA  83 E0 03                        and eax, 3
00BE87AD  41 3B C3                        cmp eax, r11d
00BE87B0  77 5C                           ja 0x140be880e
00BE87B2  45 0F 20 C0                     mov r8, cr8
00BE87B6  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00BE87BB  8D 4E 02                        lea ecx, [rsi + 2]
00BE87BE  44 0F 22 C1                     mov cr8, rcx
00BE87C2  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00BE87CB  48 8B 8D 58 06 00 00            mov rcx, qword ptr [rbp + 0x658]
00BE87D2  85 C0                           test eax, eax
00BE87D4  75 06                           jne 0x140be87dc
00BE87D6  48 8B 34 11                     mov rsi, qword ptr [rcx + rdx]
00BE87DA  EB 16                           jmp 0x140be87f2
00BE87DC  48 8B 0C 11                     mov rcx, qword ptr [rcx + rdx]
00BE87E0  48 03 8D B8 06 00 00            add rcx, qword ptr [rbp + 0x6b8]
00BE87E7  48 8B 85 98 06 00 00            mov rax, qword ptr [rbp + 0x698]
00BE87EE  48 8B 34 01                     mov rsi, qword ptr [rcx + rax]
00BE87F2  8B 85 D8 09 00 00               mov eax, dword ptr [rbp + 0x9d8]
00BE87F8  C1 E8 09                        shr eax, 9
00BE87FB  83 E0 1F                        and eax, 0x1f
00BE87FE  F0 0F AB 06                     lock bts dword ptr [rsi], eax
00BE8802  73 0A                           jae 0x140be880e
00BE8804  33 F6                           xor esi, esi
00BE8806  41 0F B6 C0                     movzx eax, r8b
00BE880A  44 0F 22 C0                     mov cr8, rax
00BE880E  48 8B CB                        mov rcx, rbx
00BE8811  E8 5A 22 00 00                  call 0x140beaa70
00BE8816  4D 8B 06                        mov r8, qword ptr [r14]
00BE8819  49 8B D6                        mov rdx, r14
00BE881C  48 8B CB                        mov rcx, rbx
00BE881F  E8 1C 1F 00 00                  call 0x140bea740
00BE8824  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BE8829  48 8B D0                        mov rdx, rax
00BE882C  41 BB 01 00 00 00               mov r11d, 1
00BE8832  48 85 F6                        test rsi, rsi
00BE8835  74 24                           je 0x140be885b
00BE8837  8B 8D D8 09 00 00               mov ecx, dword ptr [rbp + 0x9d8]
00BE883D  41 8B D3                        mov edx, r11d
00BE8840  C1 E9 09                        shr ecx, 9
00BE8843  83 E1 1F                        and ecx, 0x1f
00BE8846  D3 E2                           shl edx, cl
00BE8848  F7 D2                           not edx
00BE884A  F0 21 16                        lock and dword ptr [rsi], edx
00BE884D  0F B6 44 24 38                  movzx eax, byte ptr [rsp + 0x38]
00BE8852  44 0F 22 C0                     mov cr8, rax
00BE8856  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00BE885B  44 8B 84 24 D8 00 00 00         mov r8d, dword ptr [rsp + 0xd8]
00BE8863  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
00BE8868  44 8B 94 24 C0 00 00 00         mov r10d, dword ptr [rsp + 0xc0]
00BE8870  EB 08                           jmp 0x140be887a
00BE8872  33 D2                           xor edx, edx
00BE8874  4C 8B E0                        mov r12, rax
00BE8877  4C 8B E9                        mov r13, rcx
00BE887A  8A 43 05                        mov al, byte ptr [rbx + 5]
00BE887D  48 33 D7                        xor rdx, rdi
00BE8880  41 8B CA                        mov ecx, r10d
00BE8883  48 D3 C2                        rol rdx, cl
00BE8886  80 3B 4C                        cmp byte ptr [rbx], 0x4c
00BE8889  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00BE888E  0F 85 20 01 00 00               jne 0x140be89b4
00BE8894  41 80 3C 24 87                  cmp byte ptr [r12], 0x87
00BE8899  0F 85 15 01 00 00               jne 0x140be89b4
00BE889F  41 80 7D 00 00                  cmp byte ptr [r13], 0
00BE88A4  0F 85 0A 01 00 00               jne 0x140be89b4
00BE88AA  80 7B 03 98                     cmp byte ptr [rbx + 3], 0x98
00BE88AE  0F 85 00 01 00 00               jne 0x140be89b4
00BE88B4  80 7B 04 C3                     cmp byte ptr [rbx + 4], 0xc3
00BE88B8  0F 85 F6 00 00 00               jne 0x140be89b4
00BE88BE  3C 90                           cmp al, 0x90
00BE88C0  74 08                           je 0x140be88ca
00BE88C2  3C F1                           cmp al, 0xf1
00BE88C4  0F 85 EA 00 00 00               jne 0x140be89b4
00BE88CA  44 88 4C 24 40                  mov byte ptr [rsp + 0x40], r9b
00BE88CF  33 F6                           xor esi, esi
00BE88D1  0F 31                           rdtsc
00BE88D3  48 C1 E2 20                     shl rdx, 0x20
00BE88D7  48 0B C2                        or rax, rdx
00BE88DA  48 8B C8                        mov rcx, rax
00BE88DD  48 C1 C8 03                     ror rax, 3
00BE88E1  48 33 C8                        xor rcx, rax
00BE88E4  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00BE88EE  48 F7 E1                        mul rcx
00BE88F1  33 C2                           xor eax, edx
00BE88F3  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00BE88F8  83 E0 03                        and eax, 3
00BE88FB  41 3B C3                        cmp eax, r11d
00BE88FE  77 5C                           ja 0x140be895c
00BE8900  45 0F 20 C0                     mov r8, cr8
00BE8904  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00BE8909  8D 4E 02                        lea ecx, [rsi + 2]
00BE890C  44 0F 22 C1                     mov cr8, rcx
00BE8910  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00BE8919  48 8B 8D 58 06 00 00            mov rcx, qword ptr [rbp + 0x658]
00BE8920  85 C0                           test eax, eax
00BE8922  75 06                           jne 0x140be892a
00BE8924  48 8B 34 11                     mov rsi, qword ptr [rcx + rdx]
00BE8928  EB 16                           jmp 0x140be8940
00BE892A  48 8B 0C 11                     mov rcx, qword ptr [rcx + rdx]
00BE892E  48 03 8D B8 06 00 00            add rcx, qword ptr [rbp + 0x6b8]
00BE8935  48 8B 85 98 06 00 00            mov rax, qword ptr [rbp + 0x698]
00BE893C  48 8B 34 01                     mov rsi, qword ptr [rcx + rax]
00BE8940  8B 85 D8 09 00 00               mov eax, dword ptr [rbp + 0x9d8]
00BE8946  C1 E8 09                        shr eax, 9
00BE8949  83 E0 1F                        and eax, 0x1f
00BE894C  F0 0F AB 06                     lock bts dword ptr [rsi], eax
00BE8950  73 0A                           jae 0x140be895c
00BE8952  33 F6                           xor esi, esi
00BE8954  41 0F B6 C0                     movzx eax, r8b
00BE8958  44 0F 22 C0                     mov cr8, rax
00BE895C  48 8B CB                        mov rcx, rbx
00BE895F  E8 0C 21 00 00                  call 0x140beaa70
00BE8964  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00BE8968  49 8D 56 08                     lea rdx, [r14 + 8]
00BE896C  48 8B CB                        mov rcx, rbx
00BE896F  E8 CC 1D 00 00                  call 0x140bea740
00BE8974  48 8B F8                        mov rdi, rax
00BE8977  48 85 F6                        test rsi, rsi
00BE897A  74 21                           je 0x140be899d
00BE897C  8B 8D D8 09 00 00               mov ecx, dword ptr [rbp + 0x9d8]
00BE8982  BA 01 00 00 00                  mov edx, 1
00BE8987  C1 E9 09                        shr ecx, 9
00BE898A  83 E1 1F                        and ecx, 0x1f
00BE898D  D3 E2                           shl edx, cl
00BE898F  F7 D2                           not edx
00BE8991  F0 21 16                        lock and dword ptr [rsi], edx
00BE8994  0F B6 44 24 40                  movzx eax, byte ptr [rsp + 0x40]
00BE8999  44 0F 22 C0                     mov cr8, rax
00BE899D  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00BE89A2  44 8B 84 24 D8 00 00 00         mov r8d, dword ptr [rsp + 0xd8]
00BE89AA  44 8B 94 24 C0 00 00 00         mov r10d, dword ptr [rsp + 0xc0]
00BE89B2  EB 0A                           jmp 0x140be89be
00BE89B4  33 FF                           xor edi, edi
00BE89B6  4C 8D 63 01                     lea r12, [rbx + 1]
00BE89BA  4C 8D 6B 02                     lea r13, [rbx + 2]
00BE89BE  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
00BE89C3  48 33 FA                        xor rdi, rdx
00BE89C6  41 83 C0 F0                     add r8d, -0x10
00BE89CA  41 8B CA                        mov ecx, r10d
00BE89CD  48 D3 C7                        rol rdi, cl
00BE89D0  49 83 C6 10                     add r14, 0x10
00BE89D4  44 89 84 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r8d
00BE89DC  41 BB 01 00 00 00               mov r11d, 1
00BE89E2  41 83 F8 08                     cmp r8d, 8
00BE89E6  0F 83 34 FD FF FF               jae 0x140be8720
00BE89EC  49 8B CE                        mov rcx, r14
00BE89EF  48 2B 8C 24 C8 00 00 00         sub rcx, qword ptr [rsp + 0xc8]
00BE89F7  48 33 4C 24 48                  xor rcx, qword ptr [rsp + 0x48]
00BE89FC  48 8B C1                        mov rax, rcx
00BE89FF  48 C1 C0 11                     rol rax, 0x11
00BE8A03  48 33 C8                        xor rcx, rax
00BE8A06  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00BE8A10  48 F7 E1                        mul rcx
00BE8A13  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00BE8A18  33 D0                           xor edx, eax
00BE8A1A  44 33 D2                        xor r10d, edx
00BE8A1D  41 83 E2 3F                     and r10d, 0x3f
00BE8A21  45 0F 44 D3                     cmove r10d, r11d
00BE8A25  83 44 24 28 FF                  add dword ptr [rsp + 0x28], -1
00BE8A2A  44 89 94 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r10d
00BE8A32  0F 85 D6 FC FF FF               jne 0x140be870e
00BE8A38  44 8B BC 24 D0 00 00 00         mov r15d, dword ptr [rsp + 0xd0]
00BE8A40  45 8D 43 01                     lea r8d, [r11 + 1]
00BE8A44  41 83 E7 7F                     and r15d, 0x7f
00BE8A48  41 83 FF 08                     cmp r15d, 8
00BE8A4C  0F 82 4E 01 00 00               jb 0x140be8ba0
00BE8A52  45 8B E7                        mov r12d, r15d
00BE8A55  49 C1 EC 03                     shr r12, 3
00BE8A59  8A 43 05                        mov al, byte ptr [rbx + 5]
00BE8A5C  80 3B 4C                        cmp byte ptr [rbx], 0x4c
00BE8A5F  0F 85 07 01 00 00               jne 0x140be8b6c
00BE8A65  80 7B 01 87                     cmp byte ptr [rbx + 1], 0x87
00BE8A69  0F 85 FD 00 00 00               jne 0x140be8b6c
00BE8A6F  80 7B 02 00                     cmp byte ptr [rbx + 2], 0
00BE8A73  0F 85 F3 00 00 00               jne 0x140be8b6c
00BE8A79  80 7B 03 98                     cmp byte ptr [rbx + 3], 0x98
00BE8A7D  0F 85 E9 00 00 00               jne 0x140be8b6c
00BE8A83  80 7B 04 C3                     cmp byte ptr [rbx + 4], 0xc3
00BE8A87  0F 85 DF 00 00 00               jne 0x140be8b6c
00BE8A8D  3C 90                           cmp al, 0x90
00BE8A8F  74 08                           je 0x140be8a99
00BE8A91  3C F1                           cmp al, 0xf1
00BE8A93  0F 85 D3 00 00 00               jne 0x140be8b6c
00BE8A99  45 8A E9                        mov r13b, r9b
00BE8A9C  33 F6                           xor esi, esi
00BE8A9E  0F 31                           rdtsc
00BE8AA0  48 C1 E2 20                     shl rdx, 0x20
00BE8AA4  48 0B C2                        or rax, rdx
00BE8AA7  48 8B C8                        mov rcx, rax
00BE8AAA  48 8B D0                        mov rdx, rax
00BE8AAD  48 C1 C9 03                     ror rcx, 3
00BE8AB1  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00BE8ABB  48 33 D1                        xor rdx, rcx
00BE8ABE  48 F7 E2                        mul rdx
00BE8AC1  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00BE8AC6  33 D0                           xor edx, eax
00BE8AC8  83 E2 03                        and edx, 3
00BE8ACB  41 3B D3                        cmp edx, r11d
00BE8ACE  77 4E                           ja 0x140be8b1e
00BE8AD0  45 0F 20 C5                     mov r13, cr8
00BE8AD4  45 0F 22 C0                     mov cr8, r8
00BE8AD8  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00BE8AE1  48 8B 8D 58 06 00 00            mov rcx, qword ptr [rbp + 0x658]
00BE8AE8  85 D2                           test edx, edx
00BE8AEA  74 12                           je 0x140be8afe
00BE8AEC  48 8B 0C 01                     mov rcx, qword ptr [rcx + rax]
00BE8AF0  48 03 8D B8 06 00 00            add rcx, qword ptr [rbp + 0x6b8]
00BE8AF7  48 8B 85 98 06 00 00            mov rax, qword ptr [rbp + 0x698]
00BE8AFE  48 8B 34 01                     mov rsi, qword ptr [rcx + rax]
00BE8B02  8B 85 D8 09 00 00               mov eax, dword ptr [rbp + 0x9d8]
00BE8B08  C1 E8 09                        shr eax, 9
00BE8B0B  83 E0 1F                        and eax, 0x1f
00BE8B0E  F0 0F AB 06                     lock bts dword ptr [rsi], eax
00BE8B12  73 0A                           jae 0x140be8b1e
00BE8B14  33 F6                           xor esi, esi
00BE8B16  41 0F B6 C5                     movzx eax, r13b
00BE8B1A  44 0F 22 C0                     mov cr8, rax
00BE8B1E  48 8B CB                        mov rcx, rbx
00BE8B21  E8 4A 1F 00 00                  call 0x140beaa70
00BE8B26  4D 8B 06                        mov r8, qword ptr [r14]
00BE8B29  49 8B D6                        mov rdx, r14
00BE8B2C  48 8B CB                        mov rcx, rbx
00BE8B2F  E8 0C 1C 00 00                  call 0x140bea740
00BE8B34  4C 8B C0                        mov r8, rax
00BE8B37  48 85 F6                        test rsi, rsi
00BE8B3A  74 20                           je 0x140be8b5c
00BE8B3C  8B 8D D8 09 00 00               mov ecx, dword ptr [rbp + 0x9d8]
00BE8B42  BA 01 00 00 00                  mov edx, 1
00BE8B47  C1 E9 09                        shr ecx, 9
00BE8B4A  83 E1 1F                        and ecx, 0x1f
00BE8B4D  D3 E2                           shl edx, cl
00BE8B4F  F7 D2                           not edx
00BE8B51  F0 21 16                        lock and dword ptr [rsi], edx
00BE8B54  41 0F B6 C5                     movzx eax, r13b
00BE8B58  44 0F 22 C0                     mov cr8, rax
00BE8B5C  44 8B 94 24 C0 00 00 00         mov r10d, dword ptr [rsp + 0xc0]
00BE8B64  41 BB 01 00 00 00               mov r11d, 1
00BE8B6A  EB 03                           jmp 0x140be8b6f
00BE8B6C  45 33 C0                        xor r8d, r8d
00BE8B6F  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
00BE8B74  49 33 F8                        xor rdi, r8
00BE8B77  41 8B CA                        mov ecx, r10d
00BE8B7A  49 83 C6 08                     add r14, 8
00BE8B7E  48 D3 C7                        rol rdi, cl
00BE8B81  41 83 C7 F8                     add r15d, -8
00BE8B85  41 B8 02 00 00 00               mov r8d, 2
00BE8B8B  4D 2B E3                        sub r12, r11
00BE8B8E  0F 85 C5 FE FF FF               jne 0x140be8a59
00BE8B94  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00BE8B9C  48 83 C3 FA                     add rbx, -6
00BE8BA0  41 8B C6                        mov eax, r14d
00BE8BA3  25 FF 0F 00 00                  and eax, 0xfff
00BE8BA8  3D F8 0F 00 00                  cmp eax, 0xff8
00BE8BAD  0F 87 2B 01 00 00               ja 0x140be8cde
00BE8BB3  8A 4B 05                        mov cl, byte ptr [rbx + 5]
00BE8BB6  80 3B 4C                        cmp byte ptr [rbx], 0x4c
00BE8BB9  0F 85 06 01 00 00               jne 0x140be8cc5
00BE8BBF  80 7B 01 87                     cmp byte ptr [rbx + 1], 0x87
00BE8BC3  0F 85 FC 00 00 00               jne 0x140be8cc5
00BE8BC9  80 7B 02 00                     cmp byte ptr [rbx + 2], 0
00BE8BCD  0F 85 F2 00 00 00               jne 0x140be8cc5
00BE8BD3  80 7B 03 98                     cmp byte ptr [rbx + 3], 0x98
00BE8BD7  0F 85 E8 00 00 00               jne 0x140be8cc5
00BE8BDD  80 7B 04 C3                     cmp byte ptr [rbx + 4], 0xc3
00BE8BE1  0F 85 DE 00 00 00               jne 0x140be8cc5
00BE8BE7  80 F9 90                        cmp cl, 0x90
00BE8BEA  74 09                           je 0x140be8bf5
00BE8BEC  80 F9 F1                        cmp cl, 0xf1
00BE8BEF  0F 85 D0 00 00 00               jne 0x140be8cc5
00BE8BF5  33 F6                           xor esi, esi
00BE8BF7  0F 31                           rdtsc
00BE8BF9  48 C1 E2 20                     shl rdx, 0x20
00BE8BFD  48 0B C2                        or rax, rdx
00BE8C00  48 8B C8                        mov rcx, rax
00BE8C03  48 8B D0                        mov rdx, rax
00BE8C06  48 C1 C9 03                     ror rcx, 3
00BE8C0A  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00BE8C14  48 33 D1                        xor rdx, rcx
00BE8C17  48 F7 E2                        mul rdx
00BE8C1A  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00BE8C1F  33 D0                           xor edx, eax
00BE8C21  83 E2 03                        and edx, 3
00BE8C24  41 3B D3                        cmp edx, r11d
00BE8C27  77 53                           ja 0x140be8c7c
00BE8C29  45 0F 20 C4                     mov r12, cr8
00BE8C2D  8D 46 02                        lea eax, [rsi + 2]
00BE8C30  44 0F 22 C0                     mov cr8, rax
00BE8C34  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00BE8C3D  48 8B 8D 58 06 00 00            mov rcx, qword ptr [rbp + 0x658]
00BE8C44  85 D2                           test edx, edx
00BE8C46  74 12                           je 0x140be8c5a
00BE8C48  48 8B 0C 01                     mov rcx, qword ptr [rcx + rax]
00BE8C4C  48 03 8D B8 06 00 00            add rcx, qword ptr [rbp + 0x6b8]
00BE8C53  48 8B 85 98 06 00 00            mov rax, qword ptr [rbp + 0x698]
00BE8C5A  48 8B 34 01                     mov rsi, qword ptr [rcx + rax]
00BE8C5E  8B 85 D8 09 00 00               mov eax, dword ptr [rbp + 0x9d8]
00BE8C64  C1 E8 09                        shr eax, 9
00BE8C67  83 E0 1F                        and eax, 0x1f
00BE8C6A  F0 0F AB 06                     lock bts dword ptr [rsi], eax
00BE8C6E  73 11                           jae 0x140be8c81
00BE8C70  33 F6                           xor esi, esi
00BE8C72  41 0F B6 C4                     movzx eax, r12b
00BE8C76  44 0F 22 C0                     mov cr8, rax
00BE8C7A  EB 05                           jmp 0x140be8c81
00BE8C7C  4C 8B 64 24 20                  mov r12, qword ptr [rsp + 0x20]
00BE8C81  48 8B CB                        mov rcx, rbx
00BE8C84  E8 E7 1D 00 00                  call 0x140beaa70
00BE8C89  4D 8B 06                        mov r8, qword ptr [r14]
00BE8C8C  49 8B D6                        mov rdx, r14
00BE8C8F  48 8B CB                        mov rcx, rbx
00BE8C92  E8 A9 1A 00 00                  call 0x140bea740
00BE8C97  4C 8B C0                        mov r8, rax
00BE8C9A  41 B9 01 00 00 00               mov r9d, 1
00BE8CA0  48 85 F6                        test rsi, rsi
00BE8CA3  74 27                           je 0x140be8ccc
00BE8CA5  8B 8D D8 09 00 00               mov ecx, dword ptr [rbp + 0x9d8]
00BE8CAB  41 8B D1                        mov edx, r9d
00BE8CAE  C1 E9 09                        shr ecx, 9
00BE8CB1  83 E1 1F                        and ecx, 0x1f
00BE8CB4  D3 E2                           shl edx, cl
00BE8CB6  F7 D2                           not edx
00BE8CB8  F0 21 16                        lock and dword ptr [rsi], edx
00BE8CBB  41 0F B6 C4                     movzx eax, r12b
00BE8CBF  44 0F 22 C0                     mov cr8, rax
00BE8CC3  EB 07                           jmp 0x140be8ccc
00BE8CC5  45 33 C0                        xor r8d, r8d
00BE8CC8  45 8D 48 01                     lea r9d, [r8 + 1]
00BE8CCC  4C 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r8
00BE8CD4  4C 8D B4 24 C8 00 00 00         lea r14, [rsp + 0xc8]
00BE8CDC  EB 06                           jmp 0x140be8ce4
00BE8CDE  41 B9 01 00 00 00               mov r9d, 1
00BE8CE4  45 85 FF                        test r15d, r15d
00BE8CE7  74 1A                           je 0x140be8d03
00BE8CE9  8B 8C 24 C0 00 00 00            mov ecx, dword ptr [rsp + 0xc0]
00BE8CF0  41 0F B6 06                     movzx eax, byte ptr [r14]
00BE8CF4  4D 03 F1                        add r14, r9
00BE8CF7  48 33 F8                        xor rdi, rax
00BE8CFA  48 D3 C7                        rol rdi, cl
00BE8CFD  41 83 C7 FF                     add r15d, -1
00BE8D01  75 ED                           jne 0x140be8cf0
00BE8D03  8B C7                           mov eax, edi
00BE8D05  EB 02                           jmp 0x140be8d09
00BE8D07  33 C7                           xor eax, edi
00BE8D09  48 C1 EF 1F                     shr rdi, 0x1f
00BE8D0D  48 85 FF                        test rdi, rdi
00BE8D10  75 F5                           jne 0x140be8d07
00BE8D12  0F BA F0 1F                     btr eax, 0x1f
00BE8D16  48 83 C4 78                     add rsp, 0x78
00BE8D1A  41 5F                           pop r15
00BE8D1C  41 5E                           pop r14
00BE8D1E  41 5D                           pop r13
00BE8D20  41 5C                           pop r12
00BE8D22  5F                              pop rdi
00BE8D23  5E                              pop rsi
00BE8D24  5D                              pop rbp
00BE8D25  5B                              pop rbx
00BE8D26  C3                              ret
00BE8D27  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BE8680(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_cr8;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (120);
    a1 = ((unsigned int)(a3)) + (a2);
    if (a2 >= a1) goto loc_00BE86C4;
loc_00BE86B8:
    result = (a2) + (64);
    if (result < a1) goto loc_00BE86B8;
loc_00BE86C4:
    v_stack_m70 = *(unsigned __int64 *)(a1 + 2104);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2100)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (7));
    v_stack_m90 = (unsigned int)(result);
    v_stack_m98 = 255;
    if ((unsigned int)(result) == 0) goto loc_00BE8A44;
loc_00BE870E:
    v_stack_p20 = 128;
loc_00BE8720:
    if ((*(unsigned __int8 *)(a2 - 6)) != 76) goto loc_00BE8872;
    if ((*(unsigned __int8 *)(a2 - 6 + 1)) != 135) goto loc_00BE8872;
    if ((*(unsigned __int8 *)(a2 - 6 + 2)) != 0) goto loc_00BE8872;
    if ((*(unsigned __int8 *)(a2 - 6 + 3)) != 152) goto loc_00BE8872;
    if ((*(unsigned __int8 *)(a2 - 6 + 4)) != 195) goto loc_00BE8872;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 - 6 + 5))) == 144) goto loc_00BE877C;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 - 6 + 5))) != 241) goto loc_00BE8872;
loc_00BE877C:
    v_stack_m80 = 255;
    v_rsi = 0;
    a2 = (*(unsigned __int8 *)(a2 - 6 + 5)) << (32);
    result = (a2 - 6 + 1) | (a2);
    a1 = (result) ^ (result);
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    v_stack_m68 = a2;
    result = (unsigned int)((result) & (3));
    if (((unsigned int)(result)) > 1) goto loc_00BE880E;
    v_stack_m80 = v_cr8;
    if ((unsigned int)(result) != 0) goto loc_00BE87DC;
    goto loc_00BE87F2;
loc_00BE87DC:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1624) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1)) + (*(unsigned __int64 *)(a1 + 1720));
loc_00BE87F2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2520))) >> (9));
    result = (unsigned int)((result) & (31));
    v_rsi = *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a1 + 1688) * 1);
    v_cr8 = v_rsi + 2;
    if (!(condition_is_above_or_equal)) {
        v_rsi = 0;
        result = (unsigned __int8)(v_cr8);
        v_cr8 = result;
    }
    result = KeGuardCheckICall(a2 - 6, *(unsigned __int64 *)(gs_base + (0 + 32)), v_cr8, 255);
    result = KiAccessPage(a2 - 6, a2, *(unsigned __int64 *)(a2), 255);
    v_stack_m88 = result;
    if (0 != 0) {
        a1 = *(unsigned int *)(a1 + 2520);
        a2 = 1;
        a1 = (unsigned int)((a1) >> (9));
        a1 = (unsigned int)((a1) & (31));
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        a2 = (unsigned int)(~(a2));
        result = v_stack_m80;
        v_cr8 = result;
        a2 = v_stack_m88;
    }
    goto loc_00BE887A;
loc_00BE8872:
    a2 = 0;
loc_00BE887A:
    a2 = (a2) ^ (*(unsigned __int64 *)(a1 + 2104));
    v_stack_m88 = a2;
    if ((*(unsigned __int8 *)(a2 - 6)) != 76) goto loc_00BE89B4;
    if ((*(unsigned __int8 *)(result)) != 135) goto loc_00BE89B4;
    if ((*(unsigned __int8 *)(a1)) != 0) goto loc_00BE89B4;
    if ((*(unsigned __int8 *)(a2 - 6 + 3)) != 152) goto loc_00BE89B4;
    if ((*(unsigned __int8 *)(a2 - 6 + 4)) != 195) goto loc_00BE89B4;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 - 6 + 5))) == 144) goto loc_00BE88CA;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 - 6 + 5))) != 241) goto loc_00BE89B4;
loc_00BE88CA:
    v_stack_m78 = (unsigned __int8)(v_stack_m98);
    v_rsi = 0;
    a2 = (a2) << (32);
    result = (*(unsigned __int8 *)(a2 - 6 + 5)) | (a2);
    a1 = (result) ^ (result);
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    v_stack_m60 = a2;
    result = (unsigned int)((result) & (3));
    if (((unsigned int)(result)) > 1) goto loc_00BE895C;
    v_stack_m78 = v_cr8;
    if ((unsigned int)(result) != 0) goto loc_00BE892A;
    goto loc_00BE8940;
loc_00BE892A:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1624) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1)) + (*(unsigned __int64 *)(a1 + 1720));
loc_00BE8940:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2520))) >> (9));
    result = (unsigned int)((result) & (31));
    v_rsi = *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a1 + 1688) * 1);
    v_cr8 = v_rsi + 2;
    if (!(condition_is_above_or_equal)) {
        v_rsi = 0;
        result = (unsigned __int8)(v_cr8);
        v_cr8 = result;
    }
    result = KeGuardCheckICall(a2 - 6, *(unsigned __int64 *)(gs_base + (0 + 32)), v_cr8, v_stack_m98);
    result = KiAccessPage(a2 - 6, a2 + 8, *(unsigned __int64 *)(a2 + 8), v_stack_m98);
    if (0 != 0) {
        a1 = *(unsigned int *)(a1 + 2520);
        a2 = 1;
        a1 = (unsigned int)((a1) >> (9));
        a1 = (unsigned int)((a1) & (31));
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        a2 = (unsigned int)(~(a2));
        result = v_stack_m78;
        v_cr8 = result;
    }
    goto loc_00BE89BE;
loc_00BE89B4:
    v_rdi = 0;
loc_00BE89BE:
    v_rdi = (v_rdi) ^ (v_stack_m88);
    a3 = (unsigned int)(((unsigned int)(v_stack_p20)) + (-16));
    v_r14 = (a2) + (16);
    v_stack_p20 = a3;
    if (a3 >= 8) goto loc_00BE8720;
    a1 = (v_r14) - (v_stack_p10);
    a1 = (a1) ^ (v_stack_m70);
    a1 = (a1) ^ (a1);
    v_stack_m58 = v_stack_m88;
    a2 = (unsigned int)((v_stack_m88) ^ ((unsigned int)(a1)));
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p8)) ^ ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_stack_p8 = (unsigned int)(v_r10);
    if (condition_is_not_equal) goto loc_00BE870E;
loc_00BE8A44:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p18)) & (127));
    if (((unsigned int)(v_r15)) < 8) goto loc_00BE8BA0;
    v_r12 = ((unsigned int)((unsigned int)(v_r15))) >> (3);
loc_00BE8A59:
    if ((*(unsigned __int8 *)(a2 - 6)) != 76) goto loc_00BE8B6C;
    if ((*(unsigned __int8 *)(a2 - 6 + 1)) != 135) goto loc_00BE8B6C;
    if ((*(unsigned __int8 *)(a2 - 6 + 2)) != 0) goto loc_00BE8B6C;
    if ((*(unsigned __int8 *)(a2 - 6 + 3)) != 152) goto loc_00BE8B6C;
    if ((*(unsigned __int8 *)(a2 - 6 + 4)) != 195) goto loc_00BE8B6C;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 - 6 + 5))) == 144) goto loc_00BE8A99;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 - 6 + 5))) != 241) goto loc_00BE8B6C;
loc_00BE8A99:
    v_rsi = 0;
    a2 = (a2) << (32);
    result = (*(unsigned __int8 *)(a2 - 6 + 5)) | (a2);
    a2 = (result) ^ (result);
    v_stack_m70 = a2;
    a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
    a2 = (unsigned int)((a2) & (3));
    if (((unsigned int)(a2)) > 1) goto loc_00BE8B1E;
    result = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1624) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1);
        a1 = (a1) + (*(unsigned __int64 *)(a1 + 1720));
        result = *(unsigned __int64 *)(a1 + 1688);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2520))) >> (9));
    result = (unsigned int)((result) & (31));
    v_rsi = *(unsigned __int64 *)(a1 + result * 1);
    v_cr8 = 1 + 1;
    if (!(condition_is_above_or_equal)) {
        v_rsi = 0;
        result = (unsigned __int8)(v_cr8);
        v_cr8 = result;
    }
    result = KeGuardCheckICall(a2 - 6, a2, 1 + 1, v_stack_m98);
    result = KiAccessPage(a2 - 6, v_r14, *(unsigned __int64 *)(v_r14), v_stack_m98);
    if (0 != 0) {
        a1 = *(unsigned int *)(a1 + 2520);
        a2 = 1;
        a1 = (unsigned int)((a1) >> (9));
        a1 = (unsigned int)((a1) & (31));
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        a2 = (unsigned int)(~(a2));
        result = (unsigned __int8)(v_cr8);
        v_cr8 = result;
    }
    goto loc_00BE8B6F;
loc_00BE8B6C:
    a3 = 0;
loc_00BE8B6F:
    v_rdi = (v_rdi) ^ (0);
    v_r14 = (v_r14) + (8);
    v_r15 = (unsigned int)((v_r15) + (-8));
    v_r12 = (v_r12) - (1);
    if (condition_is_not_equal) goto loc_00BE8A59;
    v_rbx = (v_stack_p10) + (-6);
loc_00BE8BA0:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (0xFFFULL));
    if (((unsigned int)(result)) > 0xFF8ULL) goto loc_00BE8CDE;
    if ((*(unsigned __int8 *)(v_rbx)) != 76) goto loc_00BE8CC5;
    if ((*(unsigned __int8 *)(v_rbx + 1)) != 135) goto loc_00BE8CC5;
    if ((*(unsigned __int8 *)(v_rbx + 2)) != 0) goto loc_00BE8CC5;
    if ((*(unsigned __int8 *)(v_rbx + 3)) != 152) goto loc_00BE8CC5;
    if ((*(unsigned __int8 *)(v_rbx + 4)) != 195) goto loc_00BE8CC5;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 5))) == 144) goto loc_00BE8BF5;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 5))) != 241) goto loc_00BE8CC5;
loc_00BE8BF5:
    v_rsi = 0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m50 = a2;
    a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
    a2 = (unsigned int)((a2) & (3));
    if (((unsigned int)(a2)) > 1) goto loc_00BE8C7C;
    result = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1624) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1);
        a1 = (a1) + (*(unsigned __int64 *)(a1 + 1720));
        result = *(unsigned __int64 *)(a1 + 1688);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2520))) >> (9));
    result = (unsigned int)((result) & (31));
    if (condition_is_above_or_equal) goto loc_00BE8C81;
    v_rsi = 0;
    goto loc_00BE8C81;
loc_00BE8C7C:
loc_00BE8C81:
    result = KeGuardCheckICall(v_rbx, a2, 2, v_stack_m98);
    result = KiAccessPage(v_rbx, v_r14, *(unsigned __int64 *)(v_r14), v_stack_m98);
    if (0 == 0) goto loc_00BE8CCC;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2520))) >> (9));
    a1 = (unsigned int)((a1) & (31));
    a2 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)(~(a2));
    goto loc_00BE8CCC;
loc_00BE8CC5:
    a3 = 0;
loc_00BE8CCC:
    v_stack_p10 = 0;
    goto loc_00BE8CE4;
loc_00BE8CDE:
loc_00BE8CE4:
    if ((unsigned int)(v_r15) == 0) goto loc_00BE8D03;
loc_00BE8CF0:
    v_r14 = (v_stack_p10) + (1);
    v_rdi = (v_rdi) ^ (*(unsigned __int8 *)(v_stack_p10));
    v_r15 = (unsigned int)((v_r15) + (-1));
    if (condition_is_not_equal) goto loc_00BE8CF0;
loc_00BE8D03:
    goto loc_00BE8D09;
loc_00BE8D07:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) ^ ((unsigned int)(v_rdi)));
loc_00BE8D09:
    v_rdi = (v_rdi) >> (31);
    if (v_rdi != 0) goto loc_00BE8D07;
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00BE8680(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t v_cr8;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m78;
    uint8_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (120);
    Arg1 = ((uint32_t)(Arg3)) + (Arg2);
    if (Arg2 >= Arg1) goto loc_00BE86C4;
loc_00BE86B8:
    result = (Arg2) + (64);
    if (result < Arg1) goto loc_00BE86B8;
loc_00BE86C4:
    v_stack_m70 = *(uint64_t *)(arg1 + 0x838);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x834)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (7));
    v_stack_m90 = (uint32_t)(result);
    v_stack_m98 = 255;
    if ((uint32_t)(result) == 0) goto loc_00BE8A44;
loc_00BE870E:
    v_stack_p20 = 128;
loc_00BE8720:
    if ((*(uint8_t *)(arg2 - 0x6)) != 76) goto loc_00BE8872;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x1)) != 135) goto loc_00BE8872;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x2)) != 0) goto loc_00BE8872;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x3)) != 152) goto loc_00BE8872;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x4)) != 195) goto loc_00BE8872;
    if (((uint8_t)(*(uint8_t *)(arg2 - 0x6 + 0x5))) == 144) goto loc_00BE877C;
    if (((uint8_t)(*(uint8_t *)(arg2 - 0x6 + 0x5))) != 241) goto loc_00BE8872;
loc_00BE877C:
    v_stack_m80 = 255;
    local_rsi = 0;
    Arg2 = (*(uint8_t *)(arg2 - 0x6 + 0x5)) << (32);
    result = (Arg2 - 6 + 1) | (Arg2);
    Arg1 = (result) ^ (result);
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    v_stack_m68 = Arg2;
    result = (uint32_t)((result) & (3));
    if (((uint32_t)(result)) > 1) goto loc_00BE880E;
    v_stack_m80 = v_cr8;
    if ((uint32_t)(result) != 0) goto loc_00BE87DC;
    goto loc_00BE87F2;
loc_00BE87DC:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x658) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1)) + (*(uint64_t *)(arg1 + 0x6B8));
loc_00BE87F2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))) >> (9));
    result = (uint32_t)((result) & (31));
    local_rsi = *(uint64_t *)(arg1 + *(uint64_t *)(arg1 + 0x698) * 1);
    v_cr8 = local_rsi + 2;
    if (!(condition_is_above_or_equal)) {
        local_rsi = 0;
        result = (uint8_t)(v_cr8);
        v_cr8 = result;
    }
    result = KeGuardCheckICall(Arg2 - 6, *(uint64_t *)(gs_base + (0 + 0x20)), v_cr8, 255);
    result = KiAccessPage(Arg2 - 6, Arg2, *(uint64_t *)(arg2), 255);
    v_stack_m88 = result;
    if (0 != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x9D8);
        Arg2 = 1;
        Arg1 = (uint32_t)((Arg1) >> (9));
        Arg1 = (uint32_t)((Arg1) & (31));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg2 = (uint32_t)(~(Arg2));
        result = v_stack_m80;
        v_cr8 = result;
        Arg2 = v_stack_m88;
    }
    goto loc_00BE887A;
loc_00BE8872:
    Arg2 = 0;
loc_00BE887A:
    Arg2 = (Arg2) ^ (*(uint64_t *)(arg1 + 0x838));
    v_stack_m88 = Arg2;
    if ((*(uint8_t *)(arg2 - 0x6)) != 76) goto loc_00BE89B4;
    if ((*(uint8_t *)(result)) != 135) goto loc_00BE89B4;
    if ((*(uint8_t *)(arg1)) != 0) goto loc_00BE89B4;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x3)) != 152) goto loc_00BE89B4;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x4)) != 195) goto loc_00BE89B4;
    if (((uint8_t)(*(uint8_t *)(arg2 - 0x6 + 0x5))) == 144) goto loc_00BE88CA;
    if (((uint8_t)(*(uint8_t *)(arg2 - 0x6 + 0x5))) != 241) goto loc_00BE89B4;
loc_00BE88CA:
    v_stack_m78 = (uint8_t)(v_stack_m98);
    local_rsi = 0;
    Arg2 = (Arg2) << (32);
    result = (*(uint8_t *)(arg2 - 0x6 + 0x5)) | (Arg2);
    Arg1 = (result) ^ (result);
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    v_stack_m60 = Arg2;
    result = (uint32_t)((result) & (3));
    if (((uint32_t)(result)) > 1) goto loc_00BE895C;
    v_stack_m78 = v_cr8;
    if ((uint32_t)(result) != 0) goto loc_00BE892A;
    goto loc_00BE8940;
loc_00BE892A:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x658) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1)) + (*(uint64_t *)(arg1 + 0x6B8));
loc_00BE8940:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))) >> (9));
    result = (uint32_t)((result) & (31));
    local_rsi = *(uint64_t *)(arg1 + *(uint64_t *)(arg1 + 0x698) * 1);
    v_cr8 = local_rsi + 2;
    if (!(condition_is_above_or_equal)) {
        local_rsi = 0;
        result = (uint8_t)(v_cr8);
        v_cr8 = result;
    }
    result = KeGuardCheckICall(Arg2 - 6, *(uint64_t *)(gs_base + (0 + 0x20)), v_cr8, v_stack_m98);
    result = KiAccessPage(Arg2 - 6, Arg2 + 8, *(uint64_t *)(arg2 + 0x8), v_stack_m98);
    if (0 != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x9D8);
        Arg2 = 1;
        Arg1 = (uint32_t)((Arg1) >> (9));
        Arg1 = (uint32_t)((Arg1) & (31));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg2 = (uint32_t)(~(Arg2));
        result = v_stack_m78;
        v_cr8 = result;
    }
    goto loc_00BE89BE;
loc_00BE89B4:
    local_rdi = 0;
loc_00BE89BE:
    local_rdi = (local_rdi) ^ (v_stack_m88);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p20)) + (-16));
    local_r14 = (Arg2) + (16);
    v_stack_p20 = Arg3;
    if (Arg3 >= 8) goto loc_00BE8720;
    Arg1 = (local_r14) - (v_stack_p10);
    Arg1 = (Arg1) ^ (v_stack_m70);
    Arg1 = (Arg1) ^ (Arg1);
    v_stack_m58 = v_stack_m88;
    Arg2 = (uint32_t)((v_stack_m88) ^ ((uint32_t)(Arg1)));
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p8)) ^ ((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    v_stack_p8 = (uint32_t)(local_r10);
    if (condition_is_not_equal) goto loc_00BE870E;
loc_00BE8A44:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p18)) & (127));
    if (((uint32_t)(local_r15)) < 8) goto loc_00BE8BA0;
    local_r12 = ((uint32_t)((uint32_t)(local_r15))) >> (3);
loc_00BE8A59:
    if ((*(uint8_t *)(arg2 - 0x6)) != 76) goto loc_00BE8B6C;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x1)) != 135) goto loc_00BE8B6C;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x2)) != 0) goto loc_00BE8B6C;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x3)) != 152) goto loc_00BE8B6C;
    if ((*(uint8_t *)(arg2 - 0x6 + 0x4)) != 195) goto loc_00BE8B6C;
    if (((uint8_t)(*(uint8_t *)(arg2 - 0x6 + 0x5))) == 144) goto loc_00BE8A99;
    if (((uint8_t)(*(uint8_t *)(arg2 - 0x6 + 0x5))) != 241) goto loc_00BE8B6C;
loc_00BE8A99:
    local_rsi = 0;
    Arg2 = (Arg2) << (32);
    result = (*(uint8_t *)(arg2 - 0x6 + 0x5)) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m70 = Arg2;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) & (3));
    if (((uint32_t)(Arg2)) > 1) goto loc_00BE8B1E;
    result = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x658) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1);
        Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x6B8));
        result = *(uint64_t *)(arg1 + 0x698);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))) >> (9));
    result = (uint32_t)((result) & (31));
    local_rsi = *(uint64_t *)(arg1 + result * 1);
    v_cr8 = 1 + 1;
    if (!(condition_is_above_or_equal)) {
        local_rsi = 0;
        result = (uint8_t)(v_cr8);
        v_cr8 = result;
    }
    result = KeGuardCheckICall(Arg2 - 6, Arg2, 1 + 1, v_stack_m98);
    result = KiAccessPage(Arg2 - 6, local_r14, *(uint64_t *)(local_r14), v_stack_m98);
    if (0 != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x9D8);
        Arg2 = 1;
        Arg1 = (uint32_t)((Arg1) >> (9));
        Arg1 = (uint32_t)((Arg1) & (31));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg2 = (uint32_t)(~(Arg2));
        result = (uint8_t)(v_cr8);
        v_cr8 = result;
    }
    goto loc_00BE8B6F;
loc_00BE8B6C:
    Arg3 = 0;
loc_00BE8B6F:
    local_rdi = (local_rdi) ^ (0);
    local_r14 = (local_r14) + (8);
    local_r15 = (uint32_t)((local_r15) + (-8));
    local_r12 = (local_r12) - (1);
    if (condition_is_not_equal) goto loc_00BE8A59;
    local_rbx = (v_stack_p10) + (-6);
loc_00BE8BA0:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (0xFFFULL));
    if (((uint32_t)(result)) > 0xFF8ULL) goto loc_00BE8CDE;
    if ((*(uint8_t *)(local_rbx)) != 76) goto loc_00BE8CC5;
    if ((*(uint8_t *)(local_rbx + 0x1)) != 135) goto loc_00BE8CC5;
    if ((*(uint8_t *)(local_rbx + 0x2)) != 0) goto loc_00BE8CC5;
    if ((*(uint8_t *)(local_rbx + 0x3)) != 152) goto loc_00BE8CC5;
    if ((*(uint8_t *)(local_rbx + 0x4)) != 195) goto loc_00BE8CC5;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x5))) == 144) goto loc_00BE8BF5;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x5))) != 241) goto loc_00BE8CC5;
loc_00BE8BF5:
    local_rsi = 0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m50 = Arg2;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) & (3));
    if (((uint32_t)(Arg2)) > 1) goto loc_00BE8C7C;
    result = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x658) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1);
        Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x6B8));
        result = *(uint64_t *)(arg1 + 0x698);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))) >> (9));
    result = (uint32_t)((result) & (31));
    if (condition_is_above_or_equal) goto loc_00BE8C81;
    local_rsi = 0;
    goto loc_00BE8C81;
loc_00BE8C7C:
loc_00BE8C81:
    result = KeGuardCheckICall(local_rbx, Arg2, 2, v_stack_m98);
    result = KiAccessPage(local_rbx, local_r14, *(uint64_t *)(local_r14), v_stack_m98);
    if (0 == 0) goto loc_00BE8CCC;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (31));
    Arg2 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)(~(Arg2));
    goto loc_00BE8CCC;
loc_00BE8CC5:
    Arg3 = 0;
loc_00BE8CCC:
    v_stack_p10 = 0;
    goto loc_00BE8CE4;
loc_00BE8CDE:
loc_00BE8CE4:
    if ((uint32_t)(local_r15) == 0) goto loc_00BE8D03;
loc_00BE8CF0:
    local_r14 = (v_stack_p10) + (1);
    local_rdi = (local_rdi) ^ (*(uint8_t *)(v_stack_p10));
    local_r15 = (uint32_t)((local_r15) + (-1));
    if (condition_is_not_equal) goto loc_00BE8CF0;
loc_00BE8D03:
    goto loc_00BE8D09;
loc_00BE8D07:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) ^ ((uint32_t)(local_rdi)));
loc_00BE8D09:
    local_rdi = (local_rdi) >> (31);
    if (local_rdi != 0) goto loc_00BE8D07;
    local_rsp = (local_rsp) + (120);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x658` | `64` | `R` |
| `Arg1` | `+ 0x698` | `64` | `R` |
| `Arg1` | `+ 0x6B8` | `64` | `R` |
| `Arg1` | `+ 0x834` | `32` | `R` |
| `Arg1` | `+ 0x838` | `64` | `R` |
| `Arg1` | `+ 0x848` | `32` | `R/W` |
| `Arg1` | `+ 0x9D8` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=initkdbg&rva=0x00BE8680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
