# sub_0051B034

- RVA: `0x0051B034`–`0x0051C132` (길이 `4,350` bytes)
- VA: `0x000000014051B034`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2D50`
- 디코드: `994`개 명령, `4,350/4,350` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0051B25C` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051B40A` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0051B420` → [sub_0051AF4C](Unknown_function_0051AF4C.md) (function, `0x0051AF4C`)
- `0x0051B4E0` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051B5A1` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051B720` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0051B8C2` → [sub_0051AFB0](Unknown_function_0051AFB0.md) (function, `0x0051AFB0`)
- `0x0051B94D` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051BB07` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0051BBC8` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051BD34` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0051BEAA` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051BFDF` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0051C10E` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)

### Direct callers
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0051561A`
- [FsRtlMdlReadCompleteDevEx](../../initkdbg/BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BDB782`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0051B25C` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051B40A` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0051B4E0` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051B5A1` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051B720` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0051B94D` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051BB07` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0051BBC8` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051BD34` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0051BEAA` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051BFDF` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0051C10E` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0051B034  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0051B039  53                              push rbx
0051B03A  55                              push rbp
0051B03B  56                              push rsi
0051B03C  57                              push rdi
0051B03D  41 54                           push r12
0051B03F  41 55                           push r13
0051B041  41 56                           push r14
0051B043  41 57                           push r15
0051B045  48 81 EC A8 00 00 00            sub rsp, 0xa8
0051B04C  4C 8B 52 20                     mov r10, qword ptr [rdx + 0x20]
0051B050  48 8D 72 30                     lea rsi, [rdx + 0x30]
0051B054  44 8B 4A 28                     mov r9d, dword ptr [rdx + 0x28]
0051B058  48 8B D9                        mov rbx, rcx
0051B05B  49 8B CA                        mov rcx, r10
0051B05E  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
0051B063  81 E1 FF 0F 00 00               and ecx, 0xfff
0051B069  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
0051B06E  49 81 C1 FF 0F 00 00            add r9, 0xfff
0051B075  4C 8B E2                        mov r12, rdx
0051B078  4C 03 C9                        add r9, rcx
0051B07B  41 BD 01 00 00 00               mov r13d, 1
0051B081  8B 8B 44 08 00 00               mov ecx, dword ptr [rbx + 0x844]
0051B087  49 C1 E9 0C                     shr r9, 0xc
0051B08B  45 8B D9                        mov r11d, r9d
0051B08E  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0051B093  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
0051B098  4B 8D 04 9B                     lea rax, [r11 + r11*4]
0051B09C  48 8D 3C 86                     lea rdi, [rsi + rax*4]
0051B0A0  48 8D 04 89                     lea rax, [rcx + rcx*4]
0051B0A4  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0051B0A9  C1 E1 0C                        shl ecx, 0xc
0051B0AC  4C 8D 04 86                     lea r8, [rsi + rax*4]
0051B0B0  8B E9                           mov ebp, ecx
0051B0B2  49 03 EA                        add rbp, r10
0051B0B5  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
0051B0BA  F7 83 D8 09 00 00 00 00 00 20   test dword ptr [rbx + 0x9d8], 0x20000000
0051B0C4  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
0051B0C9  74 0C                           je 0x14051b0d7
0051B0CB  F7 83 DC 09 00 00 00 10 00 00   test dword ptr [rbx + 0x9dc], 0x1000
0051B0D5  74 0E                           je 0x14051b0e5
0051B0D7  48 83 BB D0 0A 00 00 00         cmp qword ptr [rbx + 0xad0], 0
0051B0DF  0F 85 45 06 00 00               jne 0x14051b72a
0051B0E5  33 C0                           xor eax, eax
0051B0E7  49 BF 01 20 00 04 80 00 10 70   movabs r15, 0x7010008004002001
0051B0F1  89 84 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], eax
0051B0F8  8D 68 02                        lea ebp, [rax + 2]
0051B0FB  41 83 F9 10                     cmp r9d, 0x10
0051B0FF  76 26                           jbe 0x14051b127
0051B101  0F 31                           rdtsc
0051B103  48 C1 E2 20                     shl rdx, 0x20
0051B107  48 0B C2                        or rax, rdx
0051B10A  48 8B C8                        mov rcx, rax
0051B10D  48 8B D0                        mov rdx, rax
0051B110  48 C1 C9 03                     ror rcx, 3
0051B114  49 8B C7                        mov rax, r15
0051B117  48 33 D1                        xor rdx, rcx
0051B11A  48 F7 E2                        mul rdx
0051B11D  48 33 C2                        xor rax, rdx
0051B120  33 D2                           xor edx, edx
0051B122  49 F7 F3                        div r11
0051B125  EB 0B                           jmp 0x14051b132
0051B127  8B D0                           mov edx, eax
0051B129  41 3B C1                        cmp eax, r9d
0051B12C  0F 83 93 03 00 00               jae 0x14051b4c5
0051B132  8B C2                           mov eax, edx
0051B134  C1 E2 0C                        shl edx, 0xc
0051B137  44 8B F2                        mov r14d, edx
0051B13A  4D 03 F2                        add r14, r10
0051B13D  48 8D 0C 80                     lea rcx, [rax + rax*4]
0051B141  48 8D 34 8E                     lea rsi, [rsi + rcx*4]
0051B145  80 7E 0F 00                     cmp byte ptr [rsi + 0xf], 0
0051B149  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0051B14E  0F 8C 52 03 00 00               jl 0x14051b4a6
0051B154  81 83 48 08 00 00 00 10 00 00   add dword ptr [rbx + 0x848], 0x1000
0051B15E  49 8D 8E 00 10 00 00            lea rcx, [r14 + 0x1000]
0051B165  44 8B 8B 34 08 00 00            mov r9d, dword ptr [rbx + 0x834]
0051B16C  4D 8B C6                        mov r8, r14
0051B16F  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
0051B176  49 8B C6                        mov rax, r14
0051B179  4C 3B F1                        cmp r14, rcx
0051B17C  73 0C                           jae 0x14051b18a
0051B17E  0F 18 00                        prefetchnta byte ptr [rax]
0051B181  48 83 C0 40                     add rax, 0x40
0051B185  48 3B C1                        cmp rax, rcx
0051B188  72 F4                           jb 0x14051b17e
0051B18A  49 8B FB                        mov rdi, r11
0051B18D  41 BA 20 00 00 00               mov r10d, 0x20
0051B193  B8 08 00 00 00                  mov eax, 8
0051B198  49 33 38                        xor rdi, qword ptr [r8]
0051B19B  41 8B C9                        mov ecx, r9d
0051B19E  48 D3 C7                        rol rdi, cl
0051B1A1  49 33 78 08                     xor rdi, qword ptr [r8 + 8]
0051B1A5  49 83 C0 10                     add r8, 0x10
0051B1A9  48 D3 C7                        rol rdi, cl
0051B1AC  49 2B C5                        sub rax, r13
0051B1AF  75 E7                           jne 0x14051b198
0051B1B1  49 8B C8                        mov rcx, r8
0051B1B4  49 2B CE                        sub rcx, r14
0051B1B7  49 33 CB                        xor rcx, r11
0051B1BA  48 8B C1                        mov rax, rcx
0051B1BD  48 C1 C0 11                     rol rax, 0x11
0051B1C1  48 33 C8                        xor rcx, rax
0051B1C4  49 8B C7                        mov rax, r15
0051B1C7  48 F7 E1                        mul rcx
0051B1CA  33 C2                           xor eax, edx
0051B1CC  44 33 C8                        xor r9d, eax
0051B1CF  41 83 E1 3F                     and r9d, 0x3f
0051B1D3  45 0F 44 CD                     cmove r9d, r13d
0051B1D7  41 83 C2 FF                     add r10d, -1
0051B1DB  75 B6                           jne 0x14051b193
0051B1DD  48 8B C7                        mov rax, rdi
0051B1E0  EB 02                           jmp 0x14051b1e4
0051B1E2  33 F8                           xor edi, eax
0051B1E4  48 C1 E8 1F                     shr rax, 0x1f
0051B1E8  48 85 C0                        test rax, rax
0051B1EB  75 F5                           jne 0x14051b1e2
0051B1ED  48 83 C6 10                     add rsi, 0x10
0051B1F1  0F BA F7 1F                     btr edi, 0x1f
0051B1F5  48 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], rsi
0051B1FD  44 8B 3E                        mov r15d, dword ptr [rsi]
0051B200  41 8B C7                        mov eax, r15d
0051B203  0F BA F0 1F                     btr eax, 0x1f
0051B207  3B F8                           cmp edi, eax
0051B209  0F 84 00 02 00 00               je 0x14051b40f
0051B20F  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
0051B215  41 C1 EF 1F                     shr r15d, 0x1f
0051B219  A8 40                           test al, 0x40
0051B21B  0F 84 B0 00 00 00               je 0x14051b2d1
0051B221  45 0F 20 C4                     mov r12, cr8
0051B225  44 0F 22 C5                     mov cr8, rbp
0051B229  49 8B F6                        mov rsi, r14
0051B22C  49 8D 86 FF 0F 00 00            lea rax, [r14 + 0xfff]
0051B233  48 81 E6 00 F0 FF FF            and rsi, 0xfffffffffffff000
0051B23A  48 0D FF 0F 00 00               or rax, 0xfff
0051B240  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0051B248  4C 8D 6E FF                     lea r13, [rsi - 1]
0051B24C  41 0F B6 EC                     movzx ebp, r12b
0051B250  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0051B257  33 D2                           xor edx, edx
0051B259  48 8B CE                        mov rcx, rsi
0051B25C  E8 FF F7 6C 00                  call 0x140beaa60
0051B261  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0051B266  75 24                           jne 0x14051b28c
0051B268  45 85 FF                        test r15d, r15d
0051B26B  74 4A                           je 0x14051b2b7
0051B26D  41 80 FC 01                     cmp r12b, 1
0051B271  77 1D                           ja 0x14051b290
0051B273  41 0F B6 EC                     movzx ebp, r12b
0051B277  44 0F 22 C5                     mov cr8, rbp
0051B27B  8A 06                           mov al, byte ptr [rsi]
0051B27D  44 0F 20 C0                     mov rax, cr8
0051B281  B8 02 00 00 00                  mov eax, 2
0051B286  44 0F 22 C0                     mov cr8, rax
0051B28A  EB C4                           jmp 0x14051b250
0051B28C  85 C0                           test eax, eax
0051B28E  78 27                           js 0x14051b2b7
0051B290  41 B9 00 10 00 00               mov r9d, 0x1000
0051B296  49 03 F1                        add rsi, r9
0051B299  4D 03 E9                        add r13, r9
0051B29C  4C 3B AC 24 08 01 00 00         cmp r13, qword ptr [rsp + 0x108]
0051B2A4  75 A6                           jne 0x14051b24c
0051B2A6  44 0F 22 C5                     mov cr8, rbp
0051B2AA  48 8B B4 24 00 01 00 00         mov rsi, qword ptr [rsp + 0x100]
0051B2B2  E9 58 01 00 00                  jmp 0x14051b40f
0051B2B7  44 0F 22 C5                     mov cr8, rbp
0051B2BB  48 8B B4 24 00 01 00 00         mov rsi, qword ptr [rsp + 0x100]
0051B2C3  41 BD 01 00 00 00               mov r13d, 1
0051B2C9  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
0051B2D1  8B 06                           mov eax, dword ptr [rsi]
0051B2D3  0F BA F0 1F                     btr eax, 0x1f
0051B2D7  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B2DE  0F 85 2B 01 00 00               jne 0x14051b40f
0051B2E4  8B CF                           mov ecx, edi
0051B2E6  48 33 C8                        xor rcx, rax
0051B2E9  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051B2F0  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051B2F4  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B2FB  0F 85 0E 01 00 00               jne 0x14051b40f
0051B301  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051B307  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051B311  48 03 C3                        add rax, rbx
0051B314  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051B31B  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051B325  49 03 C4                        add rax, r12
0051B328  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051B32F  49 63 04 24                     movsxd rax, dword ptr [r12]
0051B333  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051B33A  4C 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], r14
0051B341  44 89 AB 18 09 00 00            mov dword ptr [rbx + 0x918], r13d
0051B348  0F BA E1 1D                     bt ecx, 0x1d
0051B34C  0F 82 BD 00 00 00               jb 0x14051b40f
0051B352  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0051B35C  0F 84 AD 00 00 00               je 0x14051b40f
0051B362  41 84 CD                        test r13b, cl
0051B365  0F 84 A4 00 00 00               je 0x14051b40f
0051B36B  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051B371  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051B377  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0051B37E  2B C1                           sub eax, ecx
0051B380  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051B387  48 8D 14 19                     lea rdx, [rcx + rbx]
0051B38B  8B C8                           mov ecx, eax
0051B38D  48 C1 E9 03                     shr rcx, 3
0051B391  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0051B395  EB 21                           jmp 0x14051b3b8
0051B397  4C 31 02                        xor qword ptr [rdx], r8
0051B39A  48 8B 02                        mov rax, qword ptr [rdx]
0051B39D  41 0F B6 C8                     movzx ecx, r8b
0051B3A1  49 33 C2                        xor rax, r10
0051B3A4  83 E1 3F                        and ecx, 0x3f
0051B3A7  49 D3 C8                        ror r8, cl
0051B3AA  4C 03 C0                        add r8, rax
0051B3AD  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051B3B4  48 83 C2 08                     add rdx, 8
0051B3B8  49 3B D1                        cmp rdx, r9
0051B3BB  75 DA                           jne 0x14051b397
0051B3BD  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0051B3C5  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051B3CC  74 41                           je 0x14051b40f
0051B3CE  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051B3D4  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051B3DB  48 89 18                        mov qword ptr [rax], rbx
0051B3DE  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051B3E1  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B3E8  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051B3EF  75 0E                           jne 0x14051b3ff
0051B3F1  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051B3F8  49 33 C8                        xor rcx, r8
0051B3FB  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051B3FF  33 D2                           xor edx, edx
0051B401  41 B9 00 01 00 00               mov r9d, 0x100
0051B407  48 8B CB                        mov rcx, rbx
0051B40A  E8 75 CF 6C 00                  call 0x140be8384
0051B40F  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
0051B414  41 B8 00 10 00 00               mov r8d, 0x1000
0051B41A  49 8B D6                        mov rdx, r14
0051B41D  48 8B CB                        mov rcx, rbx
0051B420  E8 27 FB FF FF                  call 0x14051af4c
0051B425  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0051B42A  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0051B42F  BA 10 00 00 00                  mov edx, 0x10
0051B434  49 8B 08                        mov rcx, qword ptr [r8]
0051B437  49 83 C0 08                     add r8, 8
0051B43B  49 8B 01                        mov rax, qword ptr [r9]
0051B43E  49 83 C1 08                     add r9, 8
0051B442  48 3B C8                        cmp rcx, rax
0051B445  0F 85 08 01 00 00               jne 0x14051b553
0051B44B  83 C2 F8                        add edx, -8
0051B44E  83 FA 08                        cmp edx, 8
0051B451  73 E1                           jae 0x14051b434
0051B453  41 BD 01 00 00 00               mov r13d, 1
0051B459  85 D2                           test edx, edx
0051B45B  74 19                           je 0x14051b476
0051B45D  41 8A 08                        mov cl, byte ptr [r8]
0051B460  4D 03 C5                        add r8, r13
0051B463  41 8A 01                        mov al, byte ptr [r9]
0051B466  4D 03 CD                        add r9, r13
0051B469  3A C8                           cmp cl, al
0051B46B  0F 85 E2 00 00 00               jne 0x14051b553
0051B471  83 C2 FF                        add edx, -1
0051B474  75 E7                           jne 0x14051b45d
0051B476  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
0051B47E  81 83 48 08 00 00 00 00 01 00   add dword ptr [rbx + 0x848], 0x10000
0051B488  BD 02 00 00 00                  mov ebp, 2
0051B48D  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
0051B492  49 BF 01 20 00 04 80 00 10 70   movabs r15, 0x7010008004002001
0051B49C  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0051B4A1  4C 8B 5C 24 28                  mov r11, qword ptr [rsp + 0x28]
0051B4A6  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
0051B4AD  49 8D 74 24 30                  lea rsi, [r12 + 0x30]
0051B4B2  41 03 C5                        add eax, r13d
0051B4B5  89 84 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], eax
0051B4BC  83 F8 10                        cmp eax, 0x10
0051B4BF  0F 82 36 FC FF FF               jb 0x14051b0fb
0051B4C5  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0051B4CC  45 0F 20 C6                     mov r14, cr8
0051B4D0  B8 0F 00 00 00                  mov eax, 0xf
0051B4D5  44 0F 22 C0                     mov cr8, rax
0051B4D9  48 8B 83 60 01 00 00            mov rax, qword ptr [rbx + 0x160]
0051B4E0  E8 7B F5 6C 00                  call 0x140beaa60
0051B4E5  48 8B 83 20 06 00 00            mov rax, qword ptr [rbx + 0x620]
0051B4EC  48 8B 08                        mov rcx, qword ptr [rax]
0051B4EF  8B 01                           mov eax, dword ptr [rcx]
0051B4F1  48 8D 79 10                     lea rdi, [rcx + 0x10]
0051B4F5  44 8A 79 0C                     mov r15b, byte ptr [rcx + 0xc]
0051B4F9  48 8D 0C 40                     lea rcx, [rax + rax*2]
0051B4FD  48 8D 2C CF                     lea rbp, [rdi + rcx*8]
0051B501  BA 18 00 00 00                  mov edx, 0x18
0051B506  4D 8D 44 24 18                  lea r8, [r12 + 0x18]
0051B50B  4C 8B CF                        mov r9, rdi
0051B50E  49 8B 09                        mov rcx, qword ptr [r9]
0051B511  49 83 C1 08                     add r9, 8
0051B515  49 8B 00                        mov rax, qword ptr [r8]
0051B518  49 83 C0 08                     add r8, 8
0051B51C  48 3B C8                        cmp rcx, rax
0051B51F  0F 85 6A 09 00 00               jne 0x14051be8f
0051B525  83 C2 F8                        add edx, -8
0051B528  83 FA 08                        cmp edx, 8
0051B52B  73 E1                           jae 0x14051b50e
0051B52D  85 D2                           test edx, edx
0051B52F  0F 84 67 09 00 00               je 0x14051be9c
0051B535  41 8A 09                        mov cl, byte ptr [r9]
0051B538  4D 03 CD                        add r9, r13
0051B53B  41 8A 00                        mov al, byte ptr [r8]
0051B53E  4D 03 C5                        add r8, r13
0051B541  3A C8                           cmp cl, al
0051B543  0F 85 46 09 00 00               jne 0x14051be8f
0051B549  83 C2 FF                        add edx, -1
0051B54C  75 E7                           jne 0x14051b535
0051B54E  E9 49 09 00 00                  jmp 0x14051be9c
0051B553  44 8B 3E                        mov r15d, dword ptr [rsi]
0051B556  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
0051B55C  41 C1 EF 1F                     shr r15d, 0x1f
0051B560  A8 40                           test al, 0x40
0051B562  0F 84 90 00 00 00               je 0x14051b5f8
0051B568  44 0F 20 C5                     mov rbp, cr8
0051B56C  B8 02 00 00 00                  mov eax, 2
0051B571  44 0F 22 C0                     mov cr8, rax
0051B575  49 8B FE                        mov rdi, r14
0051B578  4D 8D AE FF 0F 00 00            lea r13, [r14 + 0xfff]
0051B57F  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
0051B586  49 81 CD FF 0F 00 00            or r13, 0xfff
0051B58D  4C 8D 67 FF                     lea r12, [rdi - 1]
0051B591  40 0F B6 F5                     movzx esi, bpl
0051B595  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0051B59C  33 D2                           xor edx, edx
0051B59E  48 8B CF                        mov rcx, rdi
0051B5A1  E8 BA F4 6C 00                  call 0x140beaa60
0051B5A6  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0051B5AB  75 24                           jne 0x14051b5d1
0051B5AD  45 85 FF                        test r15d, r15d
0051B5B0  74 42                           je 0x14051b5f4
0051B5B2  40 80 FD 01                     cmp bpl, 1
0051B5B6  77 1D                           ja 0x14051b5d5
0051B5B8  40 0F B6 F5                     movzx esi, bpl
0051B5BC  44 0F 22 C6                     mov cr8, rsi
0051B5C0  8A 07                           mov al, byte ptr [rdi]
0051B5C2  44 0F 20 C0                     mov rax, cr8
0051B5C6  B8 02 00 00 00                  mov eax, 2
0051B5CB  44 0F 22 C0                     mov cr8, rax
0051B5CF  EB C4                           jmp 0x14051b595
0051B5D1  85 C0                           test eax, eax
0051B5D3  78 1F                           js 0x14051b5f4
0051B5D5  B8 00 10 00 00                  mov eax, 0x1000
0051B5DA  48 03 F8                        add rdi, rax
0051B5DD  4C 03 E0                        add r12, rax
0051B5E0  4D 3B E5                        cmp r12, r13
0051B5E3  75 AC                           jne 0x14051b591
0051B5E5  44 0F 22 C6                     mov cr8, rsi
0051B5E9  41 BD 01 00 00 00               mov r13d, 1
0051B5EF  E9 82 FE FF FF                  jmp 0x14051b476
0051B5F4  44 0F 22 C6                     mov cr8, rsi
0051B5F8  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B5FF  41 BD 01 00 00 00               mov r13d, 1
0051B605  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
0051B60D  0F 85 6B FE FF FF               jne 0x14051b47e
0051B613  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051B619  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051B623  48 03 C3                        add rax, rbx
0051B626  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051B62D  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051B637  49 03 C4                        add rax, r12
0051B63A  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051B641  49 63 04 24                     movsxd rax, dword ptr [r12]
0051B645  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051B64C  4C 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], r14
0051B653  44 89 AB 18 09 00 00            mov dword ptr [rbx + 0x918], r13d
0051B65A  0F BA E1 1D                     bt ecx, 0x1d
0051B65E  0F 82 1A FE FF FF               jb 0x14051b47e
0051B664  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0051B66E  0F 84 0A FE FF FF               je 0x14051b47e
0051B674  41 84 CD                        test r13b, cl
0051B677  0F 84 01 FE FF FF               je 0x14051b47e
0051B67D  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051B683  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051B689  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0051B690  2B C1                           sub eax, ecx
0051B692  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051B699  48 8D 14 19                     lea rdx, [rcx + rbx]
0051B69D  8B C8                           mov ecx, eax
0051B69F  48 C1 E9 03                     shr rcx, 3
0051B6A3  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0051B6A7  EB 21                           jmp 0x14051b6ca
0051B6A9  4C 31 02                        xor qword ptr [rdx], r8
0051B6AC  48 8B 02                        mov rax, qword ptr [rdx]
0051B6AF  41 0F B6 C8                     movzx ecx, r8b
0051B6B3  49 33 C2                        xor rax, r10
0051B6B6  83 E1 3F                        and ecx, 0x3f
0051B6B9  49 D3 C8                        ror r8, cl
0051B6BC  4C 03 C0                        add r8, rax
0051B6BF  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051B6C6  48 83 C2 08                     add rdx, 8
0051B6CA  49 3B D1                        cmp rdx, r9
0051B6CD  75 DA                           jne 0x14051b6a9
0051B6CF  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0051B6D7  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051B6DE  0F 84 9A FD FF FF               je 0x14051b47e
0051B6E4  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051B6EA  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051B6F1  48 89 18                        mov qword ptr [rax], rbx
0051B6F4  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051B6F7  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B6FE  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051B705  75 0E                           jne 0x14051b715
0051B707  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051B70E  49 33 C8                        xor rcx, r8
0051B711  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051B715  33 D2                           xor edx, edx
0051B717  41 B9 00 01 00 00               mov r9d, 0x100
0051B71D  48 8B CB                        mov rcx, rbx
0051B720  E8 5F CC 6C 00                  call 0x140be8384
0051B725  E9 54 FD FF FF                  jmp 0x14051b47e
0051B72A  4C 3B C7                        cmp r8, rdi
0051B72D  0F 84 92 FD FF FF               je 0x14051b4c5
0051B733  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
0051B73D  41 BE 02 00 00 00               mov r14d, 2
0051B743  8B 83 4C 08 00 00               mov eax, dword ptr [rbx + 0x84c]
0051B749  39 83 48 08 00 00               cmp dword ptr [rbx + 0x848], eax
0051B74F  0F 8D 15 07 00 00               jge 0x14051be6a
0051B755  33 D2                           xor edx, edx
0051B757  4C 3B C7                        cmp r8, rdi
0051B75A  0F 84 A8 06 00 00               je 0x14051be08
0051B760  49 8B C0                        mov rax, r8
0051B763  8D 6A 01                        lea ebp, [rdx + 1]
0051B766  80 78 0F 00                     cmp byte ptr [rax + 0xf], 0
0051B76A  7C 0F                           jl 0x14051b77b
0051B76C  03 D5                           add edx, ebp
0051B76E  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
0051B772  49 8D 04 88                     lea rax, [r8 + rcx*4]
0051B776  48 3B C7                        cmp rax, rdi
0051B779  75 EB                           jne 0x14051b766
0051B77B  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
0051B780  85 D2                           test edx, edx
0051B782  0F 84 80 06 00 00               je 0x14051be08
0051B788  4C 8B BB D0 0A 00 00            mov r15, qword ptr [rbx + 0xad0]
0051B78F  8B CA                           mov ecx, edx
0051B791  83 A4 24 08 01 00 00 00         and dword ptr [rsp + 0x108], 0
0051B799  49 8B F0                        mov rsi, r8
0051B79C  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0051B7A1  89 94 24 00 01 00 00            mov dword ptr [rsp + 0x100], edx
0051B7A8  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0051B7AD  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
0051B7B2  41 BC 08 00 00 00               mov r12d, 8
0051B7B8  41 3B CC                        cmp ecx, r12d
0051B7BB  44 0F 42 E1                     cmovb r12d, ecx
0051B7BF  33 FF                           xor edi, edi
0051B7C1  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
0051B7C6  45 85 E4                        test r12d, r12d
0051B7C9  0F 84 EA 00 00 00               je 0x14051b8b9
0051B7CF  4C 8D B4 24 80 00 00 00         lea r14, [rsp + 0x80]
0051B7D7  49 8B F7                        mov rsi, r15
0051B7DA  B8 00 10 00 00                  mov eax, 0x1000
0051B7DF  44 8B CF                        mov r9d, edi
0051B7E2  48 89 46 08                     mov qword ptr [rsi + 8], rax
0051B7E6  41 C1 E1 0C                     shl r9d, 0xc
0051B7EA  4C 03 CD                        add r9, rbp
0051B7ED  4C 89 0E                        mov qword ptr [rsi], r9
0051B7F0  4D 8B D1                        mov r10, r9
0051B7F3  01 83 48 08 00 00               add dword ptr [rbx + 0x848], eax
0051B7F9  49 8B C1                        mov rax, r9
0051B7FC  44 8B 9B 34 08 00 00            mov r11d, dword ptr [rbx + 0x834]
0051B803  4C 8B BB 38 08 00 00            mov r15, qword ptr [rbx + 0x838]
0051B80A  49 8D 89 00 10 00 00            lea rcx, [r9 + 0x1000]
0051B811  4C 3B C9                        cmp r9, rcx
0051B814  73 0C                           jae 0x14051b822
0051B816  0F 18 00                        prefetchnta byte ptr [rax]
0051B819  48 83 C0 40                     add rax, 0x40
0051B81D  48 3B C1                        cmp rax, rcx
0051B820  72 F4                           jb 0x14051b816
0051B822  4D 8B C7                        mov r8, r15
0051B825  BD 20 00 00 00                  mov ebp, 0x20
0051B82A  B8 08 00 00 00                  mov eax, 8
0051B82F  4D 33 02                        xor r8, qword ptr [r10]
0051B832  41 8B CB                        mov ecx, r11d
0051B835  49 D3 C0                        rol r8, cl
0051B838  4D 33 42 08                     xor r8, qword ptr [r10 + 8]
0051B83C  49 83 C2 10                     add r10, 0x10
0051B840  49 D3 C0                        rol r8, cl
0051B843  48 83 E8 01                     sub rax, 1
0051B847  75 E6                           jne 0x14051b82f
0051B849  49 8B CA                        mov rcx, r10
0051B84C  49 2B C9                        sub rcx, r9
0051B84F  49 33 CF                        xor rcx, r15
0051B852  48 8B C1                        mov rax, rcx
0051B855  48 C1 C0 11                     rol rax, 0x11
0051B859  48 33 C8                        xor rcx, rax
0051B85C  49 8B C5                        mov rax, r13
0051B85F  48 F7 E1                        mul rcx
0051B862  B9 01 00 00 00                  mov ecx, 1
0051B867  44 33 DA                        xor r11d, edx
0051B86A  44 33 D8                        xor r11d, eax
0051B86D  41 83 E3 3F                     and r11d, 0x3f
0051B871  44 0F 44 D9                     cmove r11d, ecx
0051B875  83 C5 FF                        add ebp, -1
0051B878  75 B0                           jne 0x14051b82a
0051B87A  49 8B C0                        mov rax, r8
0051B87D  EB 03                           jmp 0x14051b882
0051B87F  44 33 C0                        xor r8d, eax
0051B882  48 C1 E8 1F                     shr rax, 0x1f
0051B886  48 85 C0                        test rax, rax
0051B889  75 F4                           jne 0x14051b87f
0051B88B  48 8B 6C 24 20                  mov rbp, qword ptr [rsp + 0x20]
0051B890  41 0F BA F0 1F                  btr r8d, 0x1f
0051B895  45 89 06                        mov dword ptr [r14], r8d
0051B898  03 F9                           add edi, ecx
0051B89A  49 83 C6 04                     add r14, 4
0051B89E  48 83 C6 30                     add rsi, 0x30
0051B8A2  41 3B FC                        cmp edi, r12d
0051B8A5  0F 82 2F FF FF FF               jb 0x14051b7da
0051B8AB  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0051B8B0  44 8D 70 02                     lea r14d, [rax + 2]
0051B8B4  4C 8B 7C 24 28                  mov r15, qword ptr [rsp + 0x28]
0051B8B9  45 8B C4                        mov r8d, r12d
0051B8BC  49 8B D7                        mov rdx, r15
0051B8BF  48 8B CB                        mov rcx, rbx
0051B8C2  E8 E9 F6 FF FF                  call 0x14051afb0
0051B8C7  33 FF                           xor edi, edi
0051B8C9  89 BC 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], edi
0051B8D0  45 85 E4                        test r12d, r12d
0051B8D3  0F 84 B2 04 00 00               je 0x14051bd8b
0051B8D9  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
0051B8E1  48 8D 46 10                     lea rax, [rsi + 0x10]
0051B8E5  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0051B8EA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0051B8EF  8B 00                           mov eax, dword ptr [rax]
0051B8F1  44 8B 21                        mov r12d, dword ptr [rcx]
0051B8F4  0F BA F0 1F                     btr eax, 0x1f
0051B8F8  44 3B E0                        cmp r12d, eax
0051B8FB  0F 84 0D 02 00 00               je 0x14051bb0e
0051B901  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
0051B907  44 8B EF                        mov r13d, edi
0051B90A  41 C1 E5 0C                     shl r13d, 0xc
0051B90E  4C 03 ED                        add r13, rbp
0051B911  A8 40                           test al, 0x40
0051B913  0F 84 A1 00 00 00               je 0x14051b9ba
0051B919  44 0F 20 C5                     mov rbp, cr8
0051B91D  45 0F 22 C6                     mov cr8, r14
0051B921  49 8B FD                        mov rdi, r13
0051B924  4D 8D BD FF 0F 00 00            lea r15, [r13 + 0xfff]
0051B92B  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
0051B932  49 81 CF FF 0F 00 00            or r15, 0xfff
0051B939  4C 8D 77 FF                     lea r14, [rdi - 1]
0051B93D  40 0F B6 F5                     movzx esi, bpl
0051B941  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0051B948  33 D2                           xor edx, edx
0051B94A  48 8B CF                        mov rcx, rdi
0051B94D  E8 0E F1 6C 00                  call 0x140beaa60
0051B952  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0051B957  75 23                           jne 0x14051b97c
0051B959  B8 01 00 00 00                  mov eax, 1
0051B95E  40 3A E8                        cmp bpl, al
0051B961  77 1D                           ja 0x14051b980
0051B963  40 0F B6 F5                     movzx esi, bpl
0051B967  44 0F 22 C6                     mov cr8, rsi
0051B96B  8A 07                           mov al, byte ptr [rdi]
0051B96D  44 0F 20 C0                     mov rax, cr8
0051B971  B8 02 00 00 00                  mov eax, 2
0051B976  44 0F 22 C0                     mov cr8, rax
0051B97A  EB C5                           jmp 0x14051b941
0051B97C  85 C0                           test eax, eax
0051B97E  78 20                           js 0x14051b9a0
0051B980  BA 00 10 00 00                  mov edx, 0x1000
0051B985  48 03 FA                        add rdi, rdx
0051B988  4C 03 F2                        add r14, rdx
0051B98B  4D 3B F7                        cmp r14, r15
0051B98E  75 AD                           jne 0x14051b93d
0051B990  44 0F 22 C6                     mov cr8, rsi
0051B994  8B BC 24 F0 00 00 00            mov edi, dword ptr [rsp + 0xf0]
0051B99B  E9 99 03 00 00                  jmp 0x14051bd39
0051B9A0  44 0F 22 C6                     mov cr8, rsi
0051B9A4  8B BC 24 F0 00 00 00            mov edi, dword ptr [rsp + 0xf0]
0051B9AB  48 8B 6C 24 20                  mov rbp, qword ptr [rsp + 0x20]
0051B9B0  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0051B9B5  4C 8B 7C 24 28                  mov r15, qword ptr [rsp + 0x28]
0051B9BA  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0051B9BF  49 8B C4                        mov rax, r12
0051B9C2  8B 09                           mov ecx, dword ptr [rcx]
0051B9C4  0F BA F1 1F                     btr ecx, 0x1f
0051B9C8  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B9CF  0F 85 39 01 00 00               jne 0x14051bb0e
0051B9D5  48 33 C8                        xor rcx, rax
0051B9D8  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051B9DF  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051B9E3  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051B9EA  0F 85 1E 01 00 00               jne 0x14051bb0e
0051B9F0  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
0051B9F8  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051BA02  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051BA08  48 03 C3                        add rax, rbx
0051BA0B  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051BA12  41 BE 01 00 00 00               mov r14d, 1
0051BA18  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051BA22  49 03 C4                        add rax, r12
0051BA25  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051BA2C  49 63 04 24                     movsxd rax, dword ptr [r12]
0051BA30  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051BA37  4C 89 AB 38 09 00 00            mov qword ptr [rbx + 0x938], r13
0051BA3E  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
0051BA45  0F BA E1 1D                     bt ecx, 0x1d
0051BA49  0F 82 CD 00 00 00               jb 0x14051bb1c
0051BA4F  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0051BA59  0F 84 BD 00 00 00               je 0x14051bb1c
0051BA5F  41 84 CE                        test r14b, cl
0051BA62  0F 84 B4 00 00 00               je 0x14051bb1c
0051BA68  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051BA6E  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051BA74  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0051BA7B  2B C1                           sub eax, ecx
0051BA7D  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051BA84  48 8D 14 19                     lea rdx, [rcx + rbx]
0051BA88  8B C8                           mov ecx, eax
0051BA8A  48 C1 E9 03                     shr rcx, 3
0051BA8E  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0051BA92  EB 21                           jmp 0x14051bab5
0051BA94  4C 31 02                        xor qword ptr [rdx], r8
0051BA97  48 8B 02                        mov rax, qword ptr [rdx]
0051BA9A  41 0F B6 C8                     movzx ecx, r8b
0051BA9E  49 33 C2                        xor rax, r10
0051BAA1  83 E1 3F                        and ecx, 0x3f
0051BAA4  49 D3 C8                        ror r8, cl
0051BAA7  4C 03 C0                        add r8, rax
0051BAAA  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051BAB1  48 83 C2 08                     add rdx, 8
0051BAB5  49 3B D1                        cmp rdx, r9
0051BAB8  75 DA                           jne 0x14051ba94
0051BABA  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0051BAC2  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051BAC9  74 51                           je 0x14051bb1c
0051BACB  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051BAD1  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051BAD8  48 89 18                        mov qword ptr [rax], rbx
0051BADB  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051BADE  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051BAE5  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051BAEC  75 0E                           jne 0x14051bafc
0051BAEE  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051BAF5  49 33 C8                        xor rcx, r8
0051BAF8  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051BAFC  33 D2                           xor edx, edx
0051BAFE  41 B9 00 01 00 00               mov r9d, 0x100
0051BB04  48 8B CB                        mov rcx, rbx
0051BB07  E8 78 C8 6C 00                  call 0x140be8384
0051BB0C  EB 0E                           jmp 0x14051bb1c
0051BB0E  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
0051BB16  41 BE 01 00 00 00               mov r14d, 1
0051BB1C  8B CF                           mov ecx, edi
0051BB1E  4D 8D 4F 10                     lea r9, [r15 + 0x10]
0051BB22  BA 10 00 00 00                  mov edx, 0x10
0051BB27  48 8D 04 89                     lea rax, [rcx + rcx*4]
0051BB2B  4C 8D 04 86                     lea r8, [rsi + rax*4]
0051BB2F  48 8D 04 49                     lea rax, [rcx + rcx*2]
0051BB33  48 C1 E0 04                     shl rax, 4
0051BB37  4C 03 C8                        add r9, rax
0051BB3A  49 8B 09                        mov rcx, qword ptr [r9]
0051BB3D  49 83 C1 08                     add r9, 8
0051BB41  49 8B 00                        mov rax, qword ptr [r8]
0051BB44  49 83 C0 08                     add r8, 8
0051BB48  48 3B C8                        cmp rcx, rax
0051BB4B  75 2A                           jne 0x14051bb77
0051BB4D  83 C2 F8                        add edx, -8
0051BB50  83 FA 08                        cmp edx, 8
0051BB53  73 E5                           jae 0x14051bb3a
0051BB55  85 D2                           test edx, edx
0051BB57  0F 84 DC 01 00 00               je 0x14051bd39
0051BB5D  41 8A 09                        mov cl, byte ptr [r9]
0051BB60  4D 03 CE                        add r9, r14
0051BB63  41 8A 00                        mov al, byte ptr [r8]
0051BB66  4D 03 C6                        add r8, r14
0051BB69  3A C8                           cmp cl, al
0051BB6B  75 0A                           jne 0x14051bb77
0051BB6D  83 C2 FF                        add edx, -1
0051BB70  75 EB                           jne 0x14051bb5d
0051BB72  E9 C2 01 00 00                  jmp 0x14051bd39
0051BB77  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
0051BB7D  44 8B EF                        mov r13d, edi
0051BB80  41 C1 E5 0C                     shl r13d, 0xc
0051BB84  4C 03 ED                        add r13, rbp
0051BB87  A8 40                           test al, 0x40
0051BB89  0F 84 8C 00 00 00               je 0x14051bc1b
0051BB8F  44 0F 20 C5                     mov rbp, cr8
0051BB93  B8 02 00 00 00                  mov eax, 2
0051BB98  44 0F 22 C0                     mov cr8, rax
0051BB9C  49 8B FD                        mov rdi, r13
0051BB9F  4D 8D BD FF 0F 00 00            lea r15, [r13 + 0xfff]
0051BBA6  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
0051BBAD  49 81 CF FF 0F 00 00            or r15, 0xfff
0051BBB4  4C 8D 77 FF                     lea r14, [rdi - 1]
0051BBB8  40 0F B6 F5                     movzx esi, bpl
0051BBBC  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0051BBC3  33 D2                           xor edx, edx
0051BBC5  48 8B CF                        mov rcx, rdi
0051BBC8  E8 93 EE 6C 00                  call 0x140beaa60
0051BBCD  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0051BBD2  75 23                           jne 0x14051bbf7
0051BBD4  B8 01 00 00 00                  mov eax, 1
0051BBD9  40 3A E8                        cmp bpl, al
0051BBDC  77 1D                           ja 0x14051bbfb
0051BBDE  40 0F B6 F5                     movzx esi, bpl
0051BBE2  44 0F 22 C6                     mov cr8, rsi
0051BBE6  8A 07                           mov al, byte ptr [rdi]
0051BBE8  44 0F 20 C0                     mov rax, cr8
0051BBEC  B8 02 00 00 00                  mov eax, 2
0051BBF1  44 0F 22 C0                     mov cr8, rax
0051BBF5  EB C5                           jmp 0x14051bbbc
0051BBF7  85 C0                           test eax, eax
0051BBF9  78 15                           js 0x14051bc10
0051BBFB  B8 00 10 00 00                  mov eax, 0x1000
0051BC00  48 03 F8                        add rdi, rax
0051BC03  4C 03 F0                        add r14, rax
0051BC06  4D 3B F7                        cmp r14, r15
0051BC09  75 AD                           jne 0x14051bbb8
0051BC0B  E9 80 FD FF FF                  jmp 0x14051b990
0051BC10  44 0F 22 C6                     mov cr8, rsi
0051BC14  8B BC 24 F0 00 00 00            mov edi, dword ptr [rsp + 0xf0]
0051BC1B  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051BC22  0F 85 11 01 00 00               jne 0x14051bd39
0051BC28  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051BC2E  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051BC38  48 03 C3                        add rax, rbx
0051BC3B  BA 01 00 00 00                  mov edx, 1
0051BC40  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051BC47  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051BC51  49 03 C4                        add rax, r12
0051BC54  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051BC5B  49 63 04 24                     movsxd rax, dword ptr [r12]
0051BC5F  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051BC66  4C 89 AB 38 09 00 00            mov qword ptr [rbx + 0x938], r13
0051BC6D  89 93 18 09 00 00               mov dword ptr [rbx + 0x918], edx
0051BC73  0F BA E1 1D                     bt ecx, 0x1d
0051BC77  0F 82 BC 00 00 00               jb 0x14051bd39
0051BC7D  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0051BC87  0F 84 AC 00 00 00               je 0x14051bd39
0051BC8D  84 CA                           test dl, cl
0051BC8F  0F 84 A4 00 00 00               je 0x14051bd39
0051BC95  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051BC9B  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051BCA1  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
0051BCA8  2B C1                           sub eax, ecx
0051BCAA  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051BCB1  4C 8D 0C 19                     lea r9, [rcx + rbx]
0051BCB5  8B C8                           mov ecx, eax
0051BCB7  48 C1 E9 03                     shr rcx, 3
0051BCBB  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
0051BCBF  EB 21                           jmp 0x14051bce2
0051BCC1  4D 31 01                        xor qword ptr [r9], r8
0051BCC4  49 8B C3                        mov rax, r11
0051BCC7  49 33 01                        xor rax, qword ptr [r9]
0051BCCA  41 0F B6 C8                     movzx ecx, r8b
0051BCCE  83 E1 3F                        and ecx, 0x3f
0051BCD1  49 D3 C8                        ror r8, cl
0051BCD4  4C 03 C0                        add r8, rax
0051BCD7  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051BCDE  49 83 C1 08                     add r9, 8
0051BCE2  4D 3B CA                        cmp r9, r10
0051BCE5  75 DA                           jne 0x14051bcc1
0051BCE7  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0051BCEF  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051BCF6  74 41                           je 0x14051bd39
0051BCF8  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051BCFE  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051BD05  48 89 18                        mov qword ptr [rax], rbx
0051BD08  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051BD0B  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051BD12  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051BD19  75 0E                           jne 0x14051bd29
0051BD1B  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051BD22  49 33 C8                        xor rcx, r8
0051BD25  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051BD29  33 D2                           xor edx, edx
0051BD2B  41 B9 00 01 00 00               mov r9d, 0x100
0051BD31  48 8B CB                        mov rcx, rbx
0051BD34  E8 4B C6 6C 00                  call 0x140be8384
0051BD39  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0051BD3E  FF C7                           inc edi
0051BD40  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0051BD45  48 83 C1 04                     add rcx, 4
0051BD49  44 8B 64 24 58                  mov r12d, dword ptr [rsp + 0x58]
0051BD4E  48 83 C0 14                     add rax, 0x14
0051BD52  48 8B 6C 24 20                  mov rbp, qword ptr [rsp + 0x20]
0051BD57  41 BE 02 00 00 00               mov r14d, 2
0051BD5D  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0051BD62  4C 8B 7C 24 28                  mov r15, qword ptr [rsp + 0x28]
0051BD67  89 BC 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], edi
0051BD6E  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0051BD73  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0051BD78  41 3B FC                        cmp edi, r12d
0051BD7B  0F 82 6E FB FF FF               jb 0x14051b8ef
0051BD81  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
0051BD8B  8B 94 24 08 01 00 00            mov edx, dword ptr [rsp + 0x108]
0051BD92  41 8B C4                        mov eax, r12d
0051BD95  C1 E0 0C                        shl eax, 0xc
0051BD98  41 03 D4                        add edx, r12d
0051BD9B  48 03 E8                        add rbp, rax
0051BD9E  89 94 24 08 01 00 00            mov dword ptr [rsp + 0x108], edx
0051BDA5  41 8B C4                        mov eax, r12d
0051BDA8  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
0051BDAD  48 8D 0C 80                     lea rcx, [rax + rax*4]
0051BDB1  41 8B C4                        mov eax, r12d
0051BDB4  48 8D 34 8E                     lea rsi, [rsi + rcx*4]
0051BDB8  C1 E0 0F                        shl eax, 0xf
0051BDBB  8B 8C 24 00 01 00 00            mov ecx, dword ptr [rsp + 0x100]
0051BDC2  01 83 48 08 00 00               add dword ptr [rbx + 0x848], eax
0051BDC8  41 2B CC                        sub ecx, r12d
0051BDCB  8B 83 48 08 00 00               mov eax, dword ptr [rbx + 0x848]
0051BDD1  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0051BDD6  89 8C 24 00 01 00 00            mov dword ptr [rsp + 0x100], ecx
0051BDDD  3B 83 4C 08 00 00               cmp eax, dword ptr [rbx + 0x84c]
0051BDE3  7D 0E                           jge 0x14051bdf3
0051BDE5  41 BE 02 00 00 00               mov r14d, 2
0051BDEB  85 C9                           test ecx, ecx
0051BDED  0F 85 BF F9 FF FF               jne 0x14051b7b2
0051BDF3  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
0051BDF8  41 BE 02 00 00 00               mov r14d, 2
0051BDFE  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
0051BE03  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
0051BE08  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
0051BE0C  49 8D 04 88                     lea rax, [r8 + rcx*4]
0051BE10  48 3B C7                        cmp rax, rdi
0051BE13  74 1F                           je 0x14051be34
0051BE15  BD 01 00 00 00                  mov ebp, 1
0051BE1A  80 78 0F 00                     cmp byte ptr [rax + 0xf], 0
0051BE1E  7D 0F                           jge 0x14051be2f
0051BE20  03 D5                           add edx, ebp
0051BE22  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
0051BE26  49 8D 04 88                     lea rax, [r8 + rcx*4]
0051BE2A  48 3B C7                        cmp rax, rdi
0051BE2D  75 EB                           jne 0x14051be1a
0051BE2F  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
0051BE34  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
0051BE38  C1 E2 0C                        shl edx, 0xc
0051BE3B  4D 8D 04 88                     lea r8, [r8 + rcx*4]
0051BE3F  8B C2                           mov eax, edx
0051BE41  48 03 E8                        add rbp, rax
0051BE44  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
0051BE49  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
0051BE4E  4C 3B C7                        cmp r8, rdi
0051BE51  0F 85 EC F8 FF FF               jne 0x14051b743
0051BE57  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
0051BE5F  41 BD 01 00 00 00               mov r13d, 1
0051BE65  E9 5B F6 FF FF                  jmp 0x14051b4c5
0051BE6A  4C 2B 44 24 68                  sub r8, qword ptr [rsp + 0x68]
0051BE6F  48 B8 67 66 66 66 66 66 66 66   movabs rax, 0x6666666666666667
0051BE79  49 F7 E8                        imul r8
0051BE7C  48 C1 FA 03                     sar rdx, 3
0051BE80  48 8B C2                        mov rax, rdx
0051BE83  48 C1 E8 3F                     shr rax, 0x3f
0051BE87  48 03 D0                        add rdx, rax
0051BE8A  E9 86 02 00 00                  jmp 0x14051c115
0051BE8F  48 83 C7 18                     add rdi, 0x18
0051BE93  48 3B FD                        cmp rdi, rbp
0051BE96  0F 82 65 F6 FF FF               jb 0x14051b501
0051BE9C  48 8B 83 A0 01 00 00            mov rax, qword ptr [rbx + 0x1a0]
0051BEA3  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0051BEAA  E8 B1 EB 6C 00                  call 0x140beaa60
0051BEAF  41 0F B6 C6                     movzx eax, r14b
0051BEB3  44 0F 22 C0                     mov cr8, rax
0051BEB7  45 84 FF                        test r15b, r15b
0051BEBA  0F 84 2F 01 00 00               je 0x14051bfef
0051BEC0  8B 8B DC 09 00 00               mov ecx, dword ptr [rbx + 0x9dc]
0051BEC6  F6 C1 10                        test cl, 0x10
0051BEC9  0F 84 15 01 00 00               je 0x14051bfe4
0051BECF  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051BED6  0F 85 08 01 00 00               jne 0x14051bfe4
0051BEDC  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051BEE6  48 03 C3                        add rax, rbx
0051BEE9  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051BEF0  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051BEFA  49 03 C4                        add rax, r12
0051BEFD  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051BF04  49 63 04 24                     movsxd rax, dword ptr [r12]
0051BF08  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051BF0F  8B 83 D8 09 00 00               mov eax, dword ptr [rbx + 0x9d8]
0051BF15  4C 89 AB 38 09 00 00            mov qword ptr [rbx + 0x938], r13
0051BF1C  44 89 AB 18 09 00 00            mov dword ptr [rbx + 0x918], r13d
0051BF23  0F BA E0 1D                     bt eax, 0x1d
0051BF27  0F 82 B7 00 00 00               jb 0x14051bfe4
0051BF2D  0F BA E1 15                     bt ecx, 0x15
0051BF31  0F 83 AD 00 00 00               jae 0x14051bfe4
0051BF37  41 84 C5                        test r13b, al
0051BF3A  0F 84 A4 00 00 00               je 0x14051bfe4
0051BF40  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051BF46  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051BF4C  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
0051BF53  2B C1                           sub eax, ecx
0051BF55  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051BF5C  4C 8D 0C 19                     lea r9, [rcx + rbx]
0051BF60  8B C8                           mov ecx, eax
0051BF62  48 C1 E9 03                     shr rcx, 3
0051BF66  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
0051BF6A  EB 21                           jmp 0x14051bf8d
0051BF6C  4D 31 01                        xor qword ptr [r9], r8
0051BF6F  49 8B C3                        mov rax, r11
0051BF72  49 33 01                        xor rax, qword ptr [r9]
0051BF75  41 0F B6 C8                     movzx ecx, r8b
0051BF79  83 E1 3F                        and ecx, 0x3f
0051BF7C  49 D3 C8                        ror r8, cl
0051BF7F  4C 03 C0                        add r8, rax
0051BF82  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051BF89  49 83 C1 08                     add r9, 8
0051BF8D  4D 3B CA                        cmp r9, r10
0051BF90  75 DA                           jne 0x14051bf6c
0051BF92  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0051BF9A  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051BFA1  74 41                           je 0x14051bfe4
0051BFA3  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051BFA9  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051BFB0  48 89 18                        mov qword ptr [rax], rbx
0051BFB3  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051BFB6  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051BFBD  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051BFC4  75 0E                           jne 0x14051bfd4
0051BFC6  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051BFCD  49 33 C8                        xor rcx, r8
0051BFD0  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051BFD4  33 D2                           xor edx, edx
0051BFD6  41 B9 00 01 00 00               mov r9d, 0x100
0051BFDC  48 8B CB                        mov rcx, rbx
0051BFDF  E8 A0 C3 6C 00                  call 0x140be8384
0051BFE4  4D 39 6C 24 18                  cmp qword ptr [r12 + 0x18], r13
0051BFE9  0F 84 24 01 00 00               je 0x14051c113
0051BFEF  48 3B FD                        cmp rdi, rbp
0051BFF2  0F 85 1B 01 00 00               jne 0x14051c113
0051BFF8  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051BFFF  0F 85 0E 01 00 00               jne 0x14051c113
0051C005  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051C00B  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051C015  48 03 C3                        add rax, rbx
0051C018  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051C01F  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051C029  49 03 C4                        add rax, r12
0051C02C  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051C033  49 63 04 24                     movsxd rax, dword ptr [r12]
0051C037  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051C03E  48 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], rdi
0051C045  44 89 AB 18 09 00 00            mov dword ptr [rbx + 0x918], r13d
0051C04C  0F BA E1 1D                     bt ecx, 0x1d
0051C050  0F 82 BD 00 00 00               jb 0x14051c113
0051C056  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0051C060  0F 84 AD 00 00 00               je 0x14051c113
0051C066  41 84 CD                        test r13b, cl
0051C069  0F 84 A4 00 00 00               je 0x14051c113
0051C06F  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051C075  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051C07B  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
0051C082  2B C1                           sub eax, ecx
0051C084  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051C08B  4C 8D 0C 19                     lea r9, [rcx + rbx]
0051C08F  8B C8                           mov ecx, eax
0051C091  48 C1 E9 03                     shr rcx, 3
0051C095  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
0051C099  EB 21                           jmp 0x14051c0bc
0051C09B  4D 31 01                        xor qword ptr [r9], r8
0051C09E  49 8B C3                        mov rax, r11
0051C0A1  49 33 01                        xor rax, qword ptr [r9]
0051C0A4  41 0F B6 C8                     movzx ecx, r8b
0051C0A8  83 E1 3F                        and ecx, 0x3f
0051C0AB  49 D3 C8                        ror r8, cl
0051C0AE  4C 03 C0                        add r8, rax
0051C0B1  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051C0B8  49 83 C1 08                     add r9, 8
0051C0BC  4D 3B CA                        cmp r9, r10
0051C0BF  75 DA                           jne 0x14051c09b
0051C0C1  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0051C0C9  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051C0D0  74 41                           je 0x14051c113
0051C0D2  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051C0D8  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C0DF  48 89 18                        mov qword ptr [rax], rbx
0051C0E2  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051C0E5  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051C0EC  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051C0F3  75 0E                           jne 0x14051c103
0051C0F5  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C0FC  49 33 C8                        xor rcx, r8
0051C0FF  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051C103  33 D2                           xor edx, edx
0051C105  41 B9 00 01 00 00               mov r9d, 0x100
0051C10B  48 8B CB                        mov rcx, rbx
0051C10E  E8 71 C2 6C 00                  call 0x140be8384
0051C113  33 D2                           xor edx, edx
0051C115  B8 44 08 00 00                  mov eax, 0x844
0051C11A  89 14 03                        mov dword ptr [rbx + rax], edx
0051C11D  48 81 C4 A8 00 00 00            add rsp, 0xa8
0051C124  41 5F                           pop r15
0051C126  41 5E                           pop r14
0051C128  41 5D                           pop r13
0051C12A  41 5C                           pop r12
0051C12C  5F                              pop rdi
0051C12D  5E                              pop rsi
0051C12E  5D                              pop rbp
0051C12F  5B                              pop rbx
0051C130  C3                              ret
0051C131  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0051B034(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (168);
    v_stack_mB0 = *(unsigned __int64 *)(a2 + 32);
    a1 = (unsigned int)((*(unsigned __int64 *)(a2 + 32)) & (0xFFFULL));
    v_stack_m80 = a2 + 48;
    a4 = ((unsigned int)(*(unsigned int *)(a2 + 40))) + (0xFFFULL);
    a4 = (a4) + (a1);
    a4 = (a4) >> (12);
    v_stack_mA0 = a4;
    v_stack_mC0 = (unsigned int)((unsigned int)(a4));
    v_stack_m88 = a2 + 48 + (unsigned int)((unsigned int)(a4)) + (unsigned int)((unsigned int)(a4)) * 4 * 4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2116))) << (12));
    v_rbp = ((unsigned int)((unsigned int)(a1))) + (*(unsigned __int64 *)(a2 + 32));
    v_stack_m98 = a2 + 48 + (unsigned int)(*(unsigned int *)(a1 + 2116)) + (unsigned int)(*(unsigned int *)(a1 + 2116)) * 4 * 4;
    v_stack_mA8 = v_rbp;
    if (((*(unsigned int *)(a1 + 2520)) & (0x20000000ULL)) == 0) goto loc_0051B0D7;
    if (((*(unsigned int *)(a1 + 2524)) & (0x1000ULL)) == 0) goto loc_0051B0E5;
loc_0051B0D7:
    if ((*(unsigned __int64 *)(a1 + 2768)) != 0) goto loc_0051B72A;
loc_0051B0E5:
    result = 0;
    v_stack_p8 = 0;
loc_0051B0FB:
    if (((unsigned int)(a4)) <= 16) goto loc_0051B127;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    result = (v_r15) ^ (a2);
    a2 = 0;
    goto loc_0051B132;
loc_0051B127:
    if (((unsigned int)(result)) >= ((unsigned int)(a4))) goto loc_0051B4C5;
loc_0051B132:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) << (12));
    v_r14 = ((unsigned int)((unsigned int)(a2))) + (*(unsigned __int64 *)(a2 + 32));
    v_stack_m98 = a2 + 48 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 4 * 4;
    if ((*(unsigned __int8 *)(a2 + 48 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 4 * 4 + 15)) < 0) goto loc_0051B4A6;
    if (v_r14 >= (v_r14 + 4096)) goto loc_0051B18A;
loc_0051B17E:
    result = (v_r14) + (64);
    if (result < (v_r14 + 4096)) goto loc_0051B17E;
loc_0051B18A:
loc_0051B193:
loc_0051B198:
    v_rdi = (*(unsigned __int64 *)(a1 + 2104)) ^ (*(unsigned __int64 *)(v_r14));
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(v_r14 + 8));
    a3 = (v_r14) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0051B198;
    a1 = (a3) - (v_r14);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)((v_r15) ^ ((unsigned int)(a2)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2100))) ^ ((unsigned int)(result)));
    a4 = (unsigned int)((a4) & (63));
    if (condition_is_equal) { a4 = 1; }
    v_r10 = (unsigned int)((32) + (-1));
    if (condition_is_not_equal) goto loc_0051B193;
    goto loc_0051B1E4;
loc_0051B1E2:
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(v_rdi)));
loc_0051B1E4:
    result = (v_rdi) >> (31);
    if (result != 0) goto loc_0051B1E2;
    v_rsi = (a2 + 48 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 4 * 4) + (16);
    v_stack_p18 = v_rsi;
    if (((unsigned int)(v_rdi)) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_0051B40F;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) >> (31));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (64)) == 0) goto loc_0051B2D1;
    v_rsi = (v_r14) & (0xFFFFFFFFFFFFF000ULL);
    result = (v_r14 + 4095) | (0xFFFULL);
    v_stack_p20 = result;
loc_0051B24C:
loc_0051B250:
    a2 = 0;
    result = KeGuardDispatchICall(v_rsi, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0051B28C;
    if ((unsigned int)(v_r15) == 0) goto loc_0051B2B7;
    if (((unsigned __int8)(v_cr8)) > 1) goto loc_0051B290;
    goto loc_0051B250;
loc_0051B28C:
    if (sign_flag) goto loc_0051B2B7;
loc_0051B290:
    v_rsi = (v_rsi) + ((unsigned int)(0x1000ULL));
    v_r13 = (v_rsi - 1) + ((unsigned int)(0x1000ULL));
    if (v_r13 != v_stack_p20) goto loc_0051B24C;
    goto loc_0051B40F;
loc_0051B2B7:
loc_0051B2D1:
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051B40F;
    a1 = ((unsigned int)((unsigned int)(v_rdi))) ^ ((unsigned int)(*(unsigned int *)(v_stack_p18)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1416) + 24) = a1;
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051B40F;
    result = (*(unsigned __int64 *)(a1 + 1416)) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2360) = v_r14;
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051B40F;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_0051B40F;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051B40F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051B3B8;
loc_0051B397:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1)) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051B3B8:
    if (a2 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051B397;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051B40F;
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
loc_0051B40F:
    result = sub_0051AF4C(a1, v_r14, (unsigned int)(0x1000ULL), v_stack_m78);
loc_0051B434:
    a3 = (v_stack_m78) + (8);
    a4 = (v_stack_m98) + (8);
    if ((*(unsigned __int64 *)(v_stack_m78)) != (*(unsigned __int64 *)(v_stack_m98))) goto loc_0051B553;
    a2 = (unsigned int)((16) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_0051B434;
    if ((unsigned int)(a2) == 0) goto loc_0051B476;
loc_0051B45D:
    a3 = (a3) + (1);
    a4 = (a4) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a3))) != ((unsigned __int8)(*(unsigned __int8 *)(a4)))) goto loc_0051B553;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0051B45D;
loc_0051B476:
loc_0051B47E:
loc_0051B4A6:
    result = (unsigned int)(((unsigned int)(v_stack_p8)) + (1));
    v_stack_p8 = (unsigned int)(result);
    if (((unsigned int)(result)) < 16) goto loc_0051B0FB;
loc_0051B4C5:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(a1 + 1336), a2, a3, v_stack_mA0);
loc_0051B501:
loc_0051B50E:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1568)) + 16) + (8);
    a3 = (v_stack_p10 + 24) + (8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1568)) + 16)) != (*(unsigned __int64 *)(v_stack_p10 + 24))) goto loc_0051BE8F;
    a2 = (unsigned int)((24) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_0051B50E;
    if ((unsigned int)(a2) == 0) goto loc_0051BE9C;
loc_0051B535:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(a3)))) goto loc_0051BE8F;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0051B535;
    goto loc_0051BE9C;
loc_0051B553:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 48))) >> (31));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (64)) == 0) goto loc_0051B5F8;
    v_rdi = ((unsigned __int8)(v_cr8)) & (0xFFFFFFFFFFFFF000ULL);
    v_r13 = ((unsigned __int8)(v_cr8) + 4095) | (0xFFFULL);
loc_0051B591:
loc_0051B595:
    a2 = 0;
    result = KeGuardDispatchICall(v_rdi, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0051B5D1;
    if ((unsigned int)(v_r15) == 0) goto loc_0051B5F4;
    if (15 > 1) goto loc_0051B5D5;
    goto loc_0051B595;
loc_0051B5D1:
    if (sign_flag) goto loc_0051B5F4;
loc_0051B5D5:
    v_rdi = (v_rdi) + ((unsigned int)(0x1000ULL));
    v_r12 = (v_rdi - 1) + ((unsigned int)(0x1000ULL));
    if (v_r12 != v_r13) goto loc_0051B591;
    goto loc_0051B476;
loc_0051B5F4:
loc_0051B5F8:
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051B47E;
    result = ((unsigned int)(0x1000ULL)) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2360) = (unsigned __int8)(v_cr8);
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051B47E;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_0051B47E;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051B47E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051B6CA;
loc_0051B6A9:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1)) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051B6CA:
    if (a2 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051B6A9;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051B47E;
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
    goto loc_0051B47E;
loc_0051B72A:
    if (a3 == v_rdi) goto loc_0051B4C5;
loc_0051B743:
    if ((*(unsigned int *)(a1 + 2120)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2124))))) goto loc_0051BE6A;
    a2 = 0;
    if (a3 == v_rdi) goto loc_0051BE08;
loc_0051B766:
    if ((*(unsigned __int8 *)(a3 + 15)) < 0) goto loc_0051B77B;
    a2 = (unsigned int)((a2) + ((unsigned int)(a2 + 1)));
    if ((a3 + a2 + a2 * 4 * 4) != v_rdi) goto loc_0051B766;
loc_0051B77B:
    if ((unsigned int)(a2) == 0) goto loc_0051BE08;
    v_stack_mC0 = *(unsigned __int64 *)(a1 + 2768);
    v_stack_p18 = (unsigned int)(a2);
    v_stack_mB8 = a3;
    v_stack_mC8 = v_stack_mA8;
loc_0051B7B2:
    v_r12 = 8;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < 8) { v_r12 = (unsigned int)((unsigned int)((unsigned int)(a2))); }
    v_rdi = 0;
    v_stack_m90 = (unsigned int)(v_r12);
    if ((unsigned int)(v_r12) == 0) goto loc_0051B8B9;
loc_0051B7DA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2768) + 8) = (unsigned int)(0x1000ULL);
    a4 = (unsigned int)((0) << (12));
    a4 = (a4) + (v_stack_mA8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 2768)) = a4;
    if (a4 >= (a4 + 4096)) goto loc_0051B822;
loc_0051B816:
    result = (a4) + (64);
    if (result < (a4 + 4096)) goto loc_0051B816;
loc_0051B822:
loc_0051B82A:
loc_0051B82F:
    a3 = (*(unsigned __int64 *)(a1 + 2104)) ^ (*(unsigned __int64 *)(a4));
    a3 = (a3) ^ (*(unsigned __int64 *)(a4 + 8));
    v_r10 = (a4) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0051B82F;
    a1 = (v_r10) - (a4);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (a1) ^ (a1);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2100))) ^ ((unsigned int)(a2)));
    v_r11 = (unsigned int)((v_r11) ^ (1));
    v_r11 = (unsigned int)((v_r11) & (63));
    if (condition_is_equal) { v_r11 = 1; }
    v_rbp = (unsigned int)((32) + (-1));
    if (condition_is_not_equal) goto loc_0051B82A;
    goto loc_0051B882;
loc_0051B87F:
    a3 = (unsigned int)((a3) ^ ((unsigned int)(a3)));
loc_0051B882:
    result = (a3) >> (31);
    if (result != 0) goto loc_0051B87F;
    *(unsigned int *)(v_stack_m68) = (unsigned int)(a3);
    v_rdi = (unsigned int)((v_rdi) + (1));
    v_r14 = (v_stack_m68) + (4);
    v_rsi = (*(unsigned __int64 *)(a1 + 2768)) + (48);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r12))) goto loc_0051B7DA;
loc_0051B8B9:
    result = sub_0051AFB0(a1, v_stack_mC0, (unsigned int)((unsigned int)(v_r12)), a4);
    v_rdi = 0;
    v_stack_p8 = 0;
    if ((unsigned int)(v_r12) == 0) goto loc_0051BD8B;
    v_stack_mA0 = v_stack_m68;
    v_stack_mB0 = v_stack_mB8 + 16;
loc_0051B8EF:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 16))))) goto loc_0051BB0E;
    v_r13 = (unsigned int)((0) << (12));
    v_r13 = (v_r13) + (v_stack_mC8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (64)) == 0) goto loc_0051B9BA;
    v_rdi = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    v_r15 = (v_r13 + 4095) | (0xFFFULL);
loc_0051B93D:
loc_0051B941:
    a2 = 0;
    result = KeGuardDispatchICall(v_rdi, a2, (unsigned int)((unsigned int)(v_r12)), a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0051B97C;
    if (15 > 1) goto loc_0051B980;
    goto loc_0051B941;
loc_0051B97C:
    if (sign_flag) goto loc_0051B9A0;
loc_0051B980:
    v_rdi = (v_rdi) + ((unsigned int)(0x1000ULL));
    v_r14 = (v_rdi - 1) + ((unsigned int)(0x1000ULL));
    if (v_r14 != v_r15) goto loc_0051B93D;
loc_0051B990:
    goto loc_0051BD39;
loc_0051B9A0:
loc_0051B9BA:
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051BB0E;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_mB0))) ^ ((unsigned int)(*(unsigned int *)(v_stack_m68)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1416) + 24) = a1;
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051BB0E;
    result = (*(unsigned __int64 *)(a1 + 1416)) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2360) = v_r13;
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051BB1C;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_0051BB1C;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051BB1C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051BAB5;
loc_0051BA94:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1)) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051BAB5:
    if (a2 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051BA94;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051BB1C;
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
    goto loc_0051BB1C;
loc_0051BB0E:
loc_0051BB1C:
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) * 2) << (4);
    a4 = (v_stack_mC0 + 16) + (result);
loc_0051BB3A:
    a4 = (a4) + (8);
    a3 = (v_stack_mB8 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) * 4 * 4) + (8);
    if ((*(unsigned __int64 *)(a4)) != (*(unsigned __int64 *)(v_stack_mB8 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) * 4 * 4))) goto loc_0051BB77;
    a2 = (unsigned int)((16) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_0051BB3A;
    if ((unsigned int)(a2) == 0) goto loc_0051BD39;
loc_0051BB5D:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(a3)))) goto loc_0051BB77;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0051BB5D;
    goto loc_0051BD39;
loc_0051BB77:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) << (12));
    v_r13 = (v_r13) + (v_stack_mC8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (64)) == 0) goto loc_0051BC1B;
    v_rdi = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    v_r15 = (v_r13 + 4095) | (0xFFFULL);
loc_0051BBB8:
loc_0051BBBC:
    a2 = 0;
    result = KeGuardDispatchICall(v_rdi, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0051BBF7;
    if (15 > 1) goto loc_0051BBFB;
    goto loc_0051BBBC;
loc_0051BBF7:
    if (sign_flag) goto loc_0051BC10;
loc_0051BBFB:
    v_rdi = (v_rdi) + ((unsigned int)(0x1000ULL));
    v_r14 = (v_rdi - 1) + ((unsigned int)(0x1000ULL));
    if (v_r14 != v_r15) goto loc_0051BBB8;
    goto loc_0051B990;
loc_0051BC10:
loc_0051BC1B:
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051BD39;
    result = ((unsigned int)(0x1000ULL)) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2360) = v_r13;
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051BD39;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_0051BD39;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051BD39;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051BCE2;
loc_0051BCC1:
    result = (*(unsigned __int64 *)(a1 + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051BCE2:
    if (a4 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051BCC1;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051BD39;
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
loc_0051BD39:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p8)) + 1);
    a1 = (v_stack_mA0) + (4);
    result = (v_stack_mB0) + (20);
    v_stack_p8 = (unsigned int)(v_rdi);
    v_stack_mA0 = a1;
    v_stack_mB0 = result;
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(v_stack_m90)))) goto loc_0051B8EF;
loc_0051BD8B:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m90)))) << (12));
    a2 = (unsigned int)(((unsigned int)(v_stack_p20)) + ((unsigned int)((unsigned int)(v_stack_m90))));
    v_rbp = (v_stack_mC8) + (result);
    v_stack_p20 = (unsigned int)(a2);
    v_stack_mC8 = v_rbp;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m90)))) << (15));
    a1 = (unsigned int)(((unsigned int)(v_stack_p18)) - ((unsigned int)((unsigned int)(v_stack_m90))));
    v_stack_mB8 = v_stack_mB8 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))) * 4 * 4;
    v_stack_p18 = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2120)))) >= (*(unsigned int *)(a1 + 2124))) goto loc_0051BDF3;
    if ((unsigned int)(a1) != 0) goto loc_0051B7B2;
loc_0051BDF3:
loc_0051BE08:
    if ((v_stack_m98 + a2 + a2 * 4 * 4) == v_stack_m88) goto loc_0051BE34;
loc_0051BE1A:
    if ((*(unsigned __int8 *)(v_stack_m98 + a2 + a2 * 4 * 4 + 15)) >= 0) goto loc_0051BE2F;
    a2 = (unsigned int)((a2) + (1));
    if ((v_stack_m98 + a2 + a2 * 4 * 4) != v_stack_m88) goto loc_0051BE1A;
loc_0051BE2F:
loc_0051BE34:
    a2 = (unsigned int)((a2) << (12));
    v_rbp = (v_stack_mA8) + ((unsigned int)((unsigned int)(a2)));
    v_stack_m98 = v_stack_m98 + a2 + a2 * 4 * 4;
    v_stack_mA8 = v_rbp;
    if ((v_stack_m98 + a2 + a2 * 4 * 4) != v_stack_m88) goto loc_0051B743;
    goto loc_0051B4C5;
loc_0051BE6A:
    a3 = (v_stack_m98 + a2 + a2 * 4 * 4) - (v_stack_m80);
    a2 = (a2) >> (3);
    result = (a2) >> (63);
    a2 = (a2) + (result);
    goto loc_0051C115;
loc_0051BE8F:
    v_rdi = (v_stack_m88) + (24);
    if (v_rdi < v_rbp) goto loc_0051B501;
loc_0051BE9C:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(a1 + 1336), a2, a3, 256);
    if ((unsigned __int8)(v_stack_mC0) == 0) goto loc_0051BFEF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (16)) == 0) goto loc_0051BFE4;
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051BFE4;
    result = (2) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2360) = 1;
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051BFE4;
    if (condition_is_above_or_equal) goto loc_0051BFE4;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051BFE4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051BF8D;
loc_0051BF6C:
    result = (*(unsigned __int64 *)(a1 + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051BF8D:
    if (a4 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051BF6C;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051BFE4;
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
loc_0051BFE4:
    if ((*(unsigned __int64 *)(v_stack_p10 + 24)) == 1) goto loc_0051C113;
loc_0051BFEF:
    if (v_rdi != v_rbp) goto loc_0051C113;
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051C113;
    result = (result) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2360) = v_rdi;
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051C113;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_0051C113;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051C113;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051C0BC;
loc_0051C09B:
    result = (*(unsigned __int64 *)(a1 + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051C0BC:
    if (a4 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051C09B;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051C113;
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
loc_0051C113:
    a2 = 0;
loc_0051C115:
    *(unsigned int *)(a1 + (unsigned int)(0x844ULL) * 1) = 0;
    v_rsp = (v_rsp) + (168);
    return (unsigned int)(0x844ULL);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0051B034(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (168);
    v_stack_mB0 = *(uint64_t *)(arg2 + 0x20);
    Arg1 = (uint32_t)((*(uint64_t *)(arg2 + 0x20)) & (0xFFFULL));
    v_stack_m80 = Arg2 + 48;
    a4 = ((uint32_t)(*(uint32_t *)(arg2 + 0x28))) + (0xFFFULL);
    a4 = (a4) + (Arg1);
    a4 = (a4) >> (12);
    v_stack_mA0 = a4;
    v_stack_mC0 = (uint32_t)((uint32_t)(a4));
    v_stack_m88 = Arg2 + 48 + (uint32_t)((uint32_t)(a4)) + (uint32_t)((uint32_t)(a4)) * 4 * 4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x844))) << (12));
    local_rbp = ((uint32_t)((uint32_t)(Arg1))) + (*(uint64_t *)(arg2 + 0x20));
    v_stack_m98 = Arg2 + 48 + (uint32_t)(*(uint32_t *)(arg1 + 0x844)) + (uint32_t)(*(uint32_t *)(arg1 + 0x844)) * 4 * 4;
    v_stack_mA8 = local_rbp;
    if (((*(uint32_t *)(arg1 + 0x9D8)) & (0x20000000ULL)) == 0) goto loc_0051B0D7;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x1000ULL)) == 0) goto loc_0051B0E5;
loc_0051B0D7:
    if ((*(uint64_t *)(arg1 + 0xAD0)) != 0) goto loc_0051B72A;
loc_0051B0E5:
    result = 0;
    v_stack_p8 = 0;
loc_0051B0FB:
    if (((uint32_t)(a4)) <= 16) goto loc_0051B127;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    result = (local_r15) ^ (Arg2);
    Arg2 = 0;
    goto loc_0051B132;
loc_0051B127:
    if (((uint32_t)(result)) >= ((uint32_t)(a4))) goto loc_0051B4C5;
loc_0051B132:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) << (12));
    local_r14 = ((uint32_t)((uint32_t)(Arg2))) + (*(uint64_t *)(arg2 + 0x20));
    v_stack_m98 = Arg2 + 48 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 4 * 4;
    if ((*(uint8_t *)(arg2 + 0x30 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 4 * 4 + 0xF)) < 0) goto loc_0051B4A6;
    if (local_r14 >= (local_r14 + 4096)) goto loc_0051B18A;
loc_0051B17E:
    result = (local_r14) + (64);
    if (result < (local_r14 + 4096)) goto loc_0051B17E;
loc_0051B18A:
loc_0051B193:
loc_0051B198:
    local_rdi = (*(uint64_t *)(arg1 + 0x838)) ^ (*(uint64_t *)(local_r14));
    local_rdi = (local_rdi) ^ (*(uint64_t *)(local_r14 + 0x8));
    a3 = (local_r14) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0051B198;
    Arg1 = (a3) - (local_r14);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)((local_r15) ^ ((uint32_t)(Arg2)));
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x834))) ^ ((uint32_t)(result)));
    a4 = (uint32_t)((a4) & (63));
    if (condition_is_equal) { a4 = 1; }
    local_r10 = (uint32_t)((32) + (-1));
    if (condition_is_not_equal) goto loc_0051B193;
    goto loc_0051B1E4;
loc_0051B1E2:
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(local_rdi)));
loc_0051B1E4:
    result = (local_rdi) >> (31);
    if (result != 0) goto loc_0051B1E2;
    local_rsi = (Arg2 + 48 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 4 * 4) + (16);
    v_stack_p18 = local_rsi;
    if (((uint32_t)(local_rdi)) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_0051B40F;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) >> (31));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (64)) == 0) goto loc_0051B2D1;
    local_rsi = (local_r14) & (0xFFFFFFFFFFFFF000ULL);
    result = (local_r14 + 4095) | (0xFFFULL);
    v_stack_p20 = result;
loc_0051B24C:
loc_0051B250:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_rsi, Arg2, a3, a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0051B28C;
    if ((uint32_t)(local_r15) == 0) goto loc_0051B2B7;
    if (((uint8_t)(v_cr8)) > 1) goto loc_0051B290;
    goto loc_0051B250;
loc_0051B28C:
    if (sign_flag) goto loc_0051B2B7;
loc_0051B290:
    local_rsi = (local_rsi) + ((uint32_t)(0x1000ULL));
    local_r13 = (local_rsi - 1) + ((uint32_t)(0x1000ULL));
    if (local_r13 != v_stack_p20) goto loc_0051B24C;
    goto loc_0051B40F;
loc_0051B2B7:
loc_0051B2D1:
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051B40F;
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) ^ ((uint32_t)(*(uint32_t *)(v_stack_p18)));
    *(void **)(*(uint64_t *)(arg1 + 0x588) + 0x18) = Arg1;
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051B40F;
    result = (*(uint64_t *)(arg1 + 0x588)) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x938) = local_r14;
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051B40F;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0051B40F;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051B40F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051B3B8;
loc_0051B397:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1)) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051B3B8:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051B397;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051B40F;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(Arg1, Arg2, a3, 256);
loc_0051B40F:
    result = sub_0051AF4C(Arg1, local_r14, (uint32_t)(0x1000ULL), v_stack_m78);
loc_0051B434:
    a3 = (v_stack_m78) + (8);
    a4 = (v_stack_m98) + (8);
    if ((*(uint64_t *)(v_stack_m78)) != (*(uint64_t *)(v_stack_m98))) goto loc_0051B553;
    Arg2 = (uint32_t)((16) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_0051B434;
    if ((uint32_t)(Arg2) == 0) goto loc_0051B476;
loc_0051B45D:
    a3 = (a3) + (1);
    a4 = (a4) + (1);
    if (((uint8_t)(*(uint8_t *)(a3))) != ((uint8_t)(*(uint8_t *)(a4)))) goto loc_0051B553;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0051B45D;
loc_0051B476:
loc_0051B47E:
loc_0051B4A6:
    result = (uint32_t)(((uint32_t)(v_stack_p8)) + (1));
    v_stack_p8 = (uint32_t)(result);
    if (((uint32_t)(result)) < 16) goto loc_0051B0FB;
loc_0051B4C5:
    result = KeGuardDispatchICall(*(uint64_t *)(arg1 + 0x538), Arg2, a3, v_stack_mA0);
loc_0051B501:
loc_0051B50E:
    a4 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x620)) + 16) + (8);
    a3 = (v_stack_p10 + 24) + (8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x620)) + 0x10)) != (*(uint64_t *)(v_stack_p10 + 0x18))) goto loc_0051BE8F;
    Arg2 = (uint32_t)((24) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_0051B50E;
    if ((uint32_t)(Arg2) == 0) goto loc_0051BE9C;
loc_0051B535:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((uint8_t)(*(uint8_t *)(a4))) != ((uint8_t)(*(uint8_t *)(a3)))) goto loc_0051BE8F;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0051B535;
    goto loc_0051BE9C;
loc_0051B553:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x30))) >> (31));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (64)) == 0) goto loc_0051B5F8;
    local_rdi = ((uint8_t)(v_cr8)) & (0xFFFFFFFFFFFFF000ULL);
    local_r13 = ((uint8_t)(v_cr8) + 4095) | (0xFFFULL);
loc_0051B591:
loc_0051B595:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_rdi, Arg2, a3, a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0051B5D1;
    if ((uint32_t)(local_r15) == 0) goto loc_0051B5F4;
    if (15 > 1) goto loc_0051B5D5;
    goto loc_0051B595;
loc_0051B5D1:
    if (sign_flag) goto loc_0051B5F4;
loc_0051B5D5:
    local_rdi = (local_rdi) + ((uint32_t)(0x1000ULL));
    local_r12 = (local_rdi - 1) + ((uint32_t)(0x1000ULL));
    if (local_r12 != local_r13) goto loc_0051B591;
    goto loc_0051B476;
loc_0051B5F4:
loc_0051B5F8:
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051B47E;
    result = ((uint32_t)(0x1000ULL)) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x938) = (uint8_t)(v_cr8);
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051B47E;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0051B47E;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051B47E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051B6CA;
loc_0051B6A9:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1)) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051B6CA:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051B6A9;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051B47E;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(Arg1, Arg2, a3, 256);
    goto loc_0051B47E;
loc_0051B72A:
    if (a3 == local_rdi) goto loc_0051B4C5;
loc_0051B743:
    if ((*(uint32_t *)(arg1 + 0x848)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x84C))))) goto loc_0051BE6A;
    Arg2 = 0;
    if (a3 == local_rdi) goto loc_0051BE08;
loc_0051B766:
    if ((*(uint8_t *)(a3 + 0xF)) < 0) goto loc_0051B77B;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2 + 1)));
    if ((a3 + Arg2 + Arg2 * 4 * 4) != local_rdi) goto loc_0051B766;
loc_0051B77B:
    if ((uint32_t)(Arg2) == 0) goto loc_0051BE08;
    v_stack_mC0 = *(uint64_t *)(arg1 + 0xAD0);
    v_stack_p18 = (uint32_t)(Arg2);
    v_stack_mB8 = a3;
    v_stack_mC8 = v_stack_mA8;
loc_0051B7B2:
    local_r12 = 8;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < 8) { local_r12 = (uint32_t)((uint32_t)((uint32_t)(Arg2))); }
    local_rdi = 0;
    v_stack_m90 = (uint32_t)(local_r12);
    if ((uint32_t)(local_r12) == 0) goto loc_0051B8B9;
loc_0051B7DA:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xAD0) + 0x8) = (uint32_t)(0x1000ULL);
    a4 = (uint32_t)((0) << (12));
    a4 = (a4) + (v_stack_mA8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xAD0)) = a4;
    if (a4 >= (a4 + 4096)) goto loc_0051B822;
loc_0051B816:
    result = (a4) + (64);
    if (result < (a4 + 4096)) goto loc_0051B816;
loc_0051B822:
loc_0051B82A:
loc_0051B82F:
    a3 = (*(uint64_t *)(arg1 + 0x838)) ^ (*(uint64_t *)(a4));
    a3 = (a3) ^ (*(uint64_t *)(a4 + 0x8));
    local_r10 = (a4) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0051B82F;
    Arg1 = (local_r10) - (a4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x834))) ^ ((uint32_t)(Arg2)));
    local_r11 = (uint32_t)((local_r11) ^ (1));
    local_r11 = (uint32_t)((local_r11) & (63));
    if (condition_is_equal) { local_r11 = 1; }
    local_rbp = (uint32_t)((32) + (-1));
    if (condition_is_not_equal) goto loc_0051B82A;
    goto loc_0051B882;
loc_0051B87F:
    a3 = (uint32_t)((a3) ^ ((uint32_t)(a3)));
loc_0051B882:
    result = (a3) >> (31);
    if (result != 0) goto loc_0051B87F;
    *(uint32_t *)(v_stack_m68) = (uint32_t)(a3);
    local_rdi = (uint32_t)((local_rdi) + (1));
    local_r14 = (v_stack_m68) + (4);
    local_rsi = (*(uint64_t *)(arg1 + 0xAD0)) + (48);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r12))) goto loc_0051B7DA;
loc_0051B8B9:
    result = sub_0051AFB0(Arg1, v_stack_mC0, (uint32_t)((uint32_t)(local_r12)), a4);
    local_rdi = 0;
    v_stack_p8 = 0;
    if ((uint32_t)(local_r12) == 0) goto loc_0051BD8B;
    v_stack_mA0 = v_stack_m68;
    v_stack_mB0 = v_stack_mB8 + 16;
loc_0051B8EF:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x10))))) goto loc_0051BB0E;
    local_r13 = (uint32_t)((0) << (12));
    local_r13 = (local_r13) + (v_stack_mC8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (64)) == 0) goto loc_0051B9BA;
    local_rdi = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    local_r15 = (local_r13 + 4095) | (0xFFFULL);
loc_0051B93D:
loc_0051B941:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_rdi, Arg2, (uint32_t)((uint32_t)(local_r12)), a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0051B97C;
    if (15 > 1) goto loc_0051B980;
    goto loc_0051B941;
loc_0051B97C:
    if (sign_flag) goto loc_0051B9A0;
loc_0051B980:
    local_rdi = (local_rdi) + ((uint32_t)(0x1000ULL));
    local_r14 = (local_rdi - 1) + ((uint32_t)(0x1000ULL));
    if (local_r14 != local_r15) goto loc_0051B93D;
loc_0051B990:
    goto loc_0051BD39;
loc_0051B9A0:
loc_0051B9BA:
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051BB0E;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_mB0))) ^ ((uint32_t)(*(uint32_t *)(v_stack_m68)));
    *(void **)(*(uint64_t *)(arg1 + 0x588) + 0x18) = Arg1;
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051BB0E;
    result = (*(uint64_t *)(arg1 + 0x588)) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x938) = local_r13;
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051BB1C;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0051BB1C;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051BB1C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051BAB5;
loc_0051BA94:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1)) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051BAB5:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051BA94;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051BB1C;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(Arg1, Arg2, a3, 256);
    goto loc_0051BB1C;
loc_0051BB0E:
loc_0051BB1C:
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) * 2) << (4);
    a4 = (v_stack_mC0 + 16) + (result);
loc_0051BB3A:
    a4 = (a4) + (8);
    a3 = (v_stack_mB8 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) * 4 * 4) + (8);
    if ((*(uint64_t *)(a4)) != (*(uint64_t *)(v_stack_mB8 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) * 4 * 4))) goto loc_0051BB77;
    Arg2 = (uint32_t)((16) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_0051BB3A;
    if ((uint32_t)(Arg2) == 0) goto loc_0051BD39;
loc_0051BB5D:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((uint8_t)(*(uint8_t *)(a4))) != ((uint8_t)(*(uint8_t *)(a3)))) goto loc_0051BB77;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0051BB5D;
    goto loc_0051BD39;
loc_0051BB77:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) << (12));
    local_r13 = (local_r13) + (v_stack_mC8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (64)) == 0) goto loc_0051BC1B;
    local_rdi = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    local_r15 = (local_r13 + 4095) | (0xFFFULL);
loc_0051BBB8:
loc_0051BBBC:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_rdi, Arg2, a3, a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0051BBF7;
    if (15 > 1) goto loc_0051BBFB;
    goto loc_0051BBBC;
loc_0051BBF7:
    if (sign_flag) goto loc_0051BC10;
loc_0051BBFB:
    local_rdi = (local_rdi) + ((uint32_t)(0x1000ULL));
    local_r14 = (local_rdi - 1) + ((uint32_t)(0x1000ULL));
    if (local_r14 != local_r15) goto loc_0051BBB8;
    goto loc_0051B990;
loc_0051BC10:
loc_0051BC1B:
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051BD39;
    result = ((uint32_t)(0x1000ULL)) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x938) = local_r13;
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051BD39;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0051BD39;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051BD39;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051BCE2;
loc_0051BCC1:
    result = (*(uint64_t *)(arg1 + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051BCE2:
    if (a4 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051BCC1;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051BD39;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(Arg1, Arg2, a3, 256);
loc_0051BD39:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p8)) + 1);
    Arg1 = (v_stack_mA0) + (4);
    result = (v_stack_mB0) + (20);
    v_stack_p8 = (uint32_t)(local_rdi);
    v_stack_mA0 = Arg1;
    v_stack_mB0 = result;
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(v_stack_m90)))) goto loc_0051B8EF;
loc_0051BD8B:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m90)))) << (12));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p20)) + ((uint32_t)((uint32_t)(v_stack_m90))));
    local_rbp = (v_stack_mC8) + (result);
    v_stack_p20 = (uint32_t)(Arg2);
    v_stack_mC8 = local_rbp;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m90)))) << (15));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p18)) - ((uint32_t)((uint32_t)(v_stack_m90))));
    v_stack_mB8 = v_stack_mB8 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))) * 4 * 4;
    v_stack_p18 = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x848)))) >= (*(uint32_t *)(arg1 + 0x84C))) goto loc_0051BDF3;
    if ((uint32_t)(Arg1) != 0) goto loc_0051B7B2;
loc_0051BDF3:
loc_0051BE08:
    if ((v_stack_m98 + Arg2 + Arg2 * 4 * 4) == v_stack_m88) goto loc_0051BE34;
loc_0051BE1A:
    if ((*(uint8_t *)(v_stack_m98 + arg2 + arg2 * 4 * 4 + 0xF)) >= 0) goto loc_0051BE2F;
    Arg2 = (uint32_t)((Arg2) + (1));
    if ((v_stack_m98 + Arg2 + Arg2 * 4 * 4) != v_stack_m88) goto loc_0051BE1A;
loc_0051BE2F:
loc_0051BE34:
    Arg2 = (uint32_t)((Arg2) << (12));
    local_rbp = (v_stack_mA8) + ((uint32_t)((uint32_t)(Arg2)));
    v_stack_m98 = v_stack_m98 + Arg2 + Arg2 * 4 * 4;
    v_stack_mA8 = local_rbp;
    if ((v_stack_m98 + Arg2 + Arg2 * 4 * 4) != v_stack_m88) goto loc_0051B743;
    goto loc_0051B4C5;
loc_0051BE6A:
    a3 = (v_stack_m98 + Arg2 + Arg2 * 4 * 4) - (v_stack_m80);
    Arg2 = (Arg2) >> (3);
    result = (Arg2) >> (63);
    Arg2 = (Arg2) + (result);
    goto loc_0051C115;
loc_0051BE8F:
    local_rdi = (v_stack_m88) + (24);
    if (local_rdi < local_rbp) goto loc_0051B501;
loc_0051BE9C:
    result = KeGuardDispatchICall(*(uint64_t *)(arg1 + 0x538), Arg2, a3, 256);
    if ((uint8_t)(v_stack_mC0) == 0) goto loc_0051BFEF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (16)) == 0) goto loc_0051BFE4;
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051BFE4;
    result = (2) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x938) = 1;
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051BFE4;
    if (condition_is_above_or_equal) goto loc_0051BFE4;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051BFE4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051BF8D;
loc_0051BF6C:
    result = (*(uint64_t *)(arg1 + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051BF8D:
    if (a4 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051BF6C;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051BFE4;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(Arg1, Arg2, a3, 256);
loc_0051BFE4:
    if ((*(uint64_t *)(v_stack_p10 + 0x18)) == 1) goto loc_0051C113;
loc_0051BFEF:
    if (local_rdi != local_rbp) goto loc_0051C113;
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051C113;
    result = (result) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x938) = local_rdi;
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051C113;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0051C113;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051C113;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051C0BC;
loc_0051C09B:
    result = (*(uint64_t *)(arg1 + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051C0BC:
    if (a4 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051C09B;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051C113;
    *(void **)(*(uint64_t *)(arg1 + 0x588)) = Arg1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)));
    result = *(uint64_t *)(arg1 + 0x588);
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        result = *(uint64_t *)(arg1 + 0x588);
        Arg1 = (*(uint64_t *)(arg1 + 0xA80)) ^ (a3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(Arg1, Arg2, a3, 256);
loc_0051C113:
    Arg2 = 0;
loc_0051C115:
    *(uint32_t *)(arg1 + (uint32_t)(0x844ULL) * 1) = 0;
    local_rsp = (local_rsp) + (168);
    return (uint32_t)(0x844ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*1` | `32` | `W` |
| `Arg1` | `+ 0x160` | `64` | `R` |
| `Arg1` | `+ 0x1A0` | `64` | `R` |
| `Arg1` | `+ 0x468` | `64` | `R` |
| `Arg1` | `+ 0x538` | `64` | `R` |
| `Arg1` | `+ 0x588` | `64` | `R` |
| `Arg1` | `+ 0x620` | `64` | `R` |
| `Arg1` | `+ 0x804` | `32` | `R` |
| `Arg1` | `+ 0x834` | `32` | `R` |
| `Arg1` | `+ 0x838` | `64` | `R` |
| `Arg1` | `+ 0x844` | `32` | `R` |
| `Arg1` | `+ 0x848` | `32` | `R` |
| `Arg1` | `+ 0x848` | `32` | `R/W` |
| `Arg1` | `+ 0x84C` | `32` | `R` |
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
| `Arg1` | `+ 0xAD0` | `64` | `R` |
| `Arg2` | `+ 0x0 + rax*4` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0051B034&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
