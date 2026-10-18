# sub_0051C138

- RVA: `0x0051C138`–`0x0051C6D2` (길이 `1,434` bytes)
- VA: `0x000000014051C138`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE7D0`
- 디코드: `358`개 명령, `1,434/1,434` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0051C2DB` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051C46B` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0051C48B` → [sub_0051AF4C](Unknown_function_0051AF4C.md) (function, `0x0051AF4C`)
- `0x0051C53D` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0051C6AE` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)

### Direct callers
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0051562A`
- [FsRtlMdlReadCompleteDevEx](../../initkdbg/BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BDB792`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0051C2DB` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051C46B` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0051C53D` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0051C6AE` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0051C138  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0051C13D  55                              push rbp
0051C13E  56                              push rsi
0051C13F  57                              push rdi
0051C140  41 54                           push r12
0051C142  41 55                           push r13
0051C144  41 56                           push r14
0051C146  41 57                           push r15
0051C148  48 83 EC 30                     sub rsp, 0x30
0051C14C  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
0051C14F  4C 8B F2                        mov r14, rdx
0051C152  48 8B D9                        mov rbx, rcx
0051C155  A8 04                           test al, 4
0051C157  0F 85 5F 05 00 00               jne 0x14051c6bc
0051C15D  4C 8B 5A 08                     mov r11, qword ptr [rdx + 8]
0051C161  44 8B 42 10                     mov r8d, dword ptr [rdx + 0x10]
0051C165  4D 8B CB                        mov r9, r11
0051C168  44 01 81 48 08 00 00            add dword ptr [rcx + 0x848], r8d
0051C16F  49 8B C3                        mov rax, r11
0051C172  44 8B 91 34 08 00 00            mov r10d, dword ptr [rcx + 0x834]
0051C179  48 8B A9 38 08 00 00            mov rbp, qword ptr [rcx + 0x838]
0051C180  4B 8D 0C 03                     lea rcx, [r11 + r8]
0051C184  4C 3B D9                        cmp r11, rcx
0051C187  73 0C                           jae 0x14051c195
0051C189  0F 18 00                        prefetchnta byte ptr [rax]
0051C18C  48 83 C0 40                     add rax, 0x40
0051C190  48 3B C1                        cmp rax, rcx
0051C193  72 F4                           jb 0x14051c189
0051C195  41 8B F0                        mov esi, r8d
0051C198  41 83 CC FF                     or r12d, 0xffffffff
0051C19C  C1 EE 07                        shr esi, 7
0051C19F  48 8B FD                        mov rdi, rbp
0051C1A2  41 BF 01 00 00 00               mov r15d, 1
0051C1A8  85 F6                           test esi, esi
0051C1AA  74 52                           je 0x14051c1fe
0051C1AC  B8 08 00 00 00                  mov eax, 8
0051C1B1  49 33 39                        xor rdi, qword ptr [r9]
0051C1B4  41 8B CA                        mov ecx, r10d
0051C1B7  48 D3 C7                        rol rdi, cl
0051C1BA  49 33 79 08                     xor rdi, qword ptr [r9 + 8]
0051C1BE  49 83 C1 10                     add r9, 0x10
0051C1C2  48 D3 C7                        rol rdi, cl
0051C1C5  49 2B C7                        sub rax, r15
0051C1C8  75 E7                           jne 0x14051c1b1
0051C1CA  49 8B C9                        mov rcx, r9
0051C1CD  49 2B CB                        sub rcx, r11
0051C1D0  48 33 CD                        xor rcx, rbp
0051C1D3  48 8B C1                        mov rax, rcx
0051C1D6  48 C1 C0 11                     rol rax, 0x11
0051C1DA  48 33 C8                        xor rcx, rax
0051C1DD  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
0051C1E7  48 F7 E1                        mul rcx
0051C1EA  33 C2                           xor eax, edx
0051C1EC  41 33 C2                        xor eax, r10d
0051C1EF  45 8B D7                        mov r10d, r15d
0051C1F2  83 E0 3F                        and eax, 0x3f
0051C1F5  44 0F 45 D0                     cmovne r10d, eax
0051C1F9  41 03 F4                        add esi, r12d
0051C1FC  75 AE                           jne 0x14051c1ac
0051C1FE  41 83 E0 7F                     and r8d, 0x7f
0051C202  41 83 F8 08                     cmp r8d, 8
0051C206  72 1D                           jb 0x14051c225
0051C208  41 8B C0                        mov eax, r8d
0051C20B  48 C1 E8 03                     shr rax, 3
0051C20F  49 33 39                        xor rdi, qword ptr [r9]
0051C212  41 8B CA                        mov ecx, r10d
0051C215  48 D3 C7                        rol rdi, cl
0051C218  49 83 C1 08                     add r9, 8
0051C21C  41 83 C0 F8                     add r8d, -8
0051C220  49 2B C7                        sub rax, r15
0051C223  75 EA                           jne 0x14051c20f
0051C225  45 85 C0                        test r8d, r8d
0051C228  74 15                           je 0x14051c23f
0051C22A  41 0F B6 01                     movzx eax, byte ptr [r9]
0051C22E  41 8B CA                        mov ecx, r10d
0051C231  48 33 F8                        xor rdi, rax
0051C234  4D 03 CF                        add r9, r15
0051C237  48 D3 C7                        rol rdi, cl
0051C23A  45 03 C4                        add r8d, r12d
0051C23D  75 EB                           jne 0x14051c22a
0051C23F  48 8B C7                        mov rax, rdi
0051C242  EB 02                           jmp 0x14051c246
0051C244  33 F8                           xor edi, eax
0051C246  48 C1 E8 1F                     shr rax, 0x1f
0051C24A  48 85 C0                        test rax, rax
0051C24D  75 F5                           jne 0x14051c244
0051C24F  0F BA F7 1F                     btr edi, 0x1f
0051C253  44 8D 40 02                     lea r8d, [rax + 2]
0051C257  33 F6                           xor esi, esi
0051C259  49 B9 E8 B4 C8 91 58 3F A0 A3   movabs r9, 0xa3a03f5891c8b4e8
0051C263  49 BB 15 34 45 E4 DE 4B B7 B3   movabs r11, 0xb3b74bdee4453415
0051C26D  41 3B 7E 14                     cmp edi, dword ptr [r14 + 0x14]
0051C271  0F 84 F9 01 00 00               je 0x14051c470
0051C277  41 39 36                        cmp dword ptr [r14], esi
0051C27A  75 08                           jne 0x14051c284
0051C27C  41 39 76 18                     cmp dword ptr [r14 + 0x18], esi
0051C280  41 0F 45 F7                     cmovne esi, r15d
0051C284  41 8B 4E 10                     mov ecx, dword ptr [r14 + 0x10]
0051C288  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0051C28C  48 85 C9                        test rcx, rcx
0051C28F  0F 84 AC 00 00 00               je 0x14051c341
0051C295  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
0051C29B  A8 40                           test al, 0x40
0051C29D  0F 84 9E 00 00 00               je 0x14051c341
0051C2A3  44 0F 20 C0                     mov rax, cr8
0051C2A7  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0051C2AC  45 0F 22 C0                     mov cr8, r8
0051C2B0  4C 8B FA                        mov r15, rdx
0051C2B3  0F B6 E8                        movzx ebp, al
0051C2B6  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
0051C2BD  4C 8D 69 FF                     lea r13, [rcx - 1]
0051C2C1  4C 03 EA                        add r13, rdx
0051C2C4  49 81 CD FF 0F 00 00            or r13, 0xfff
0051C2CB  4D 8D 67 FF                     lea r12, [r15 - 1]
0051C2CF  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0051C2D6  33 D2                           xor edx, edx
0051C2D8  49 8B CF                        mov rcx, r15
0051C2DB  E8 80 E7 6C 00                  call 0x140beaa60
0051C2E0  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0051C2E5  75 1F                           jne 0x14051c306
0051C2E7  85 F6                           test esi, esi
0051C2E9  75 38                           jne 0x14051c323
0051C2EB  80 7C 24 78 01                  cmp byte ptr [rsp + 0x78], 1
0051C2F0  77 18                           ja 0x14051c30a
0051C2F2  44 0F 22 C5                     mov cr8, rbp
0051C2F6  41 8A 07                        mov al, byte ptr [r15]
0051C2F9  44 0F 20 C0                     mov rax, cr8
0051C2FD  8D 46 02                        lea eax, [rsi + 2]
0051C300  44 0F 22 C0                     mov cr8, rax
0051C304  EB C9                           jmp 0x14051c2cf
0051C306  85 C0                           test eax, eax
0051C308  78 19                           js 0x14051c323
0051C30A  B8 00 10 00 00                  mov eax, 0x1000
0051C30F  4C 03 F8                        add r15, rax
0051C312  4C 03 E0                        add r12, rax
0051C315  4D 3B E5                        cmp r12, r13
0051C318  75 B5                           jne 0x14051c2cf
0051C31A  44 0F 22 C5                     mov cr8, rbp
0051C31E  E9 4D 01 00 00                  jmp 0x14051c470
0051C323  49 BB 15 34 45 E4 DE 4B B7 B3   movabs r11, 0xb3b74bdee4453415
0051C32D  49 B9 E8 B4 C8 91 58 3F A0 A3   movabs r9, 0xa3a03f5891c8b4e8
0051C337  41 BF 01 00 00 00               mov r15d, 1
0051C33D  44 0F 22 C5                     mov cr8, rbp
0051C341  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051C348  4C 8B D3                        mov r10, rbx
0051C34B  41 8B 46 14                     mov eax, dword ptr [r14 + 0x14]
0051C34F  BA DC 09 00 00                  mov edx, 0x9dc
0051C354  75 12                           jne 0x14051c368
0051C356  8B C8                           mov ecx, eax
0051C358  8B C7                           mov eax, edi
0051C35A  48 33 C8                        xor rcx, rax
0051C35D  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C364  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051C368  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051C36F  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0051C373  0F 85 F7 00 00 00               jne 0x14051c470
0051C379  4A 8D 04 0B                     lea rax, [rbx + r9]
0051C37D  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051C384  4B 8D 04 1E                     lea rax, [r14 + r11]
0051C388  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051C38F  49 63 06                        movsxd rax, dword ptr [r14]
0051C392  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051C399  48 89 8B 38 09 00 00            mov qword ptr [rbx + 0x938], rcx
0051C3A0  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051C3A6  44 89 BB 18 09 00 00            mov dword ptr [rbx + 0x918], r15d
0051C3AD  0F BA E1 1D                     bt ecx, 0x1d
0051C3B1  0F 82 B9 00 00 00               jb 0x14051c470
0051C3B7  42 F7 04 12 00 00 20 00         test dword ptr [rdx + r10], 0x200000
0051C3BF  0F 84 AB 00 00 00               je 0x14051c470
0051C3C5  41 84 CF                        test r15b, cl
0051C3C8  0F 84 A2 00 00 00               je 0x14051c470
0051C3CE  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051C3D4  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051C3DA  48 8B BB 38 08 00 00            mov rdi, qword ptr [rbx + 0x838]
0051C3E1  2B C1                           sub eax, ecx
0051C3E3  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051C3EA  4C 8D 0C 19                     lea r9, [rcx + rbx]
0051C3EE  8B C8                           mov ecx, eax
0051C3F0  48 C1 E9 03                     shr rcx, 3
0051C3F4  4D 8D 1C C9                     lea r11, [r9 + rcx*8]
0051C3F8  EB 21                           jmp 0x14051c41b
0051C3FA  4D 31 01                        xor qword ptr [r9], r8
0051C3FD  49 8B 01                        mov rax, qword ptr [r9]
0051C400  41 0F B6 C8                     movzx ecx, r8b
0051C404  48 33 C7                        xor rax, rdi
0051C407  83 E1 3F                        and ecx, 0x3f
0051C40A  49 D3 C8                        ror r8, cl
0051C40D  4C 03 C0                        add r8, rax
0051C410  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051C417  49 83 C1 08                     add r9, 8
0051C41B  4D 3B CB                        cmp r9, r11
0051C41E  75 DA                           jne 0x14051c3fa
0051C420  42 0F BA 34 12 15               btr dword ptr [rdx + r10], 0x15
0051C426  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051C42D  74 41                           je 0x14051c470
0051C42F  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051C435  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C43C  48 89 18                        mov qword ptr [rax], rbx
0051C43F  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051C442  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051C449  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051C450  75 0E                           jne 0x14051c460
0051C452  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C459  49 33 C8                        xor rcx, r8
0051C45C  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051C460  33 D2                           xor edx, edx
0051C462  41 B9 00 01 00 00               mov r9d, 0x100
0051C468  48 8B CB                        mov rcx, rbx
0051C46B  E8 14 BF 6C 00                  call 0x140be8384
0051C470  41 8B 76 10                     mov esi, dword ptr [r14 + 0x10]
0051C474  85 F6                           test esi, esi
0051C476  0F 84 40 02 00 00               je 0x14051c6bc
0051C47C  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0051C480  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0051C485  44 8B C6                        mov r8d, esi
0051C488  48 8B CB                        mov rcx, rbx
0051C48B  E8 BC EA FF FF                  call 0x14051af4c
0051C490  BA 10 00 00 00                  mov edx, 0x10
0051C495  4D 8D 46 18                     lea r8, [r14 + 0x18]
0051C499  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0051C49E  49 8B 09                        mov rcx, qword ptr [r9]
0051C4A1  49 83 C1 08                     add r9, 8
0051C4A5  49 8B 00                        mov rax, qword ptr [r8]
0051C4A8  49 83 C0 08                     add r8, 8
0051C4AC  48 3B C8                        cmp rcx, rax
0051C4AF  75 2A                           jne 0x14051c4db
0051C4B1  83 C2 F8                        add edx, -8
0051C4B4  83 FA 08                        cmp edx, 8
0051C4B7  73 E5                           jae 0x14051c49e
0051C4B9  85 D2                           test edx, edx
0051C4BB  0F 84 F2 01 00 00               je 0x14051c6b3
0051C4C1  41 8A 09                        mov cl, byte ptr [r9]
0051C4C4  49 FF C1                        inc r9
0051C4C7  41 8A 00                        mov al, byte ptr [r8]
0051C4CA  49 FF C0                        inc r8
0051C4CD  3A C8                           cmp cl, al
0051C4CF  75 0A                           jne 0x14051c4db
0051C4D1  83 C2 FF                        add edx, -1
0051C4D4  75 EB                           jne 0x14051c4c1
0051C4D6  E9 D8 01 00 00                  jmp 0x14051c6b3
0051C4DB  45 8B 6E 28                     mov r13d, dword ptr [r14 + 0x28]
0051C4DF  48 8D BB DC 09 00 00            lea rdi, [rbx + 0x9dc]
0051C4E6  8B 07                           mov eax, dword ptr [rdi]
0051C4E8  41 83 E5 01                     and r13d, 1
0051C4EC  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0051C4F0  A8 40                           test al, 0x40
0051C4F2  0F 84 98 00 00 00               je 0x14051c590
0051C4F8  45 0F 20 C0                     mov r8, cr8
0051C4FC  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0051C501  B8 02 00 00 00                  mov eax, 2
0051C506  44 0F 22 C0                     mov cr8, rax
0051C50A  4C 8B F9                        mov r15, rcx
0051C50D  41 0F B6 E8                     movzx ebp, r8b
0051C511  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
0051C518  48 8D 41 FF                     lea rax, [rcx - 1]
0051C51C  48 03 C6                        add rax, rsi
0051C51F  48 0D FF 0F 00 00               or rax, 0xfff
0051C525  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0051C52D  4D 8D 67 FF                     lea r12, [r15 - 1]
0051C531  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0051C538  33 D2                           xor edx, edx
0051C53A  49 8B CF                        mov rcx, r15
0051C53D  E8 1E E5 6C 00                  call 0x140beaa60
0051C542  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0051C547  75 21                           jne 0x14051c56a
0051C549  45 85 ED                        test r13d, r13d
0051C54C  75 3E                           jne 0x14051c58c
0051C54E  80 7C 24 78 01                  cmp byte ptr [rsp + 0x78], 1
0051C553  77 19                           ja 0x14051c56e
0051C555  44 0F 22 C5                     mov cr8, rbp
0051C559  41 8A 07                        mov al, byte ptr [r15]
0051C55C  44 0F 20 C0                     mov rax, cr8
0051C560  41 8D 45 02                     lea eax, [r13 + 2]
0051C564  44 0F 22 C0                     mov cr8, rax
0051C568  EB C7                           jmp 0x14051c531
0051C56A  85 C0                           test eax, eax
0051C56C  78 1E                           js 0x14051c58c
0051C56E  B8 00 10 00 00                  mov eax, 0x1000
0051C573  4C 03 F8                        add r15, rax
0051C576  4C 03 E0                        add r12, rax
0051C579  4C 3B A4 24 80 00 00 00         cmp r12, qword ptr [rsp + 0x80]
0051C581  75 AE                           jne 0x14051c531
0051C583  44 0F 22 C5                     mov cr8, rbp
0051C587  E9 27 01 00 00                  jmp 0x14051c6b3
0051C58C  44 0F 22 C5                     mov cr8, rbp
0051C590  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051C597  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0051C59B  0F 85 12 01 00 00               jne 0x14051c6b3
0051C5A1  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0051C5AB  48 03 C3                        add rax, rbx
0051C5AE  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0051C5B5  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0051C5BF  49 03 C6                        add rax, r14
0051C5C2  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0051C5C9  49 63 06                        movsxd rax, dword ptr [r14]
0051C5CC  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0051C5D3  48 89 8B 38 09 00 00            mov qword ptr [rbx + 0x938], rcx
0051C5DA  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0051C5E0  C7 83 18 09 00 00 01 00 00 00   mov dword ptr [rbx + 0x918], 1
0051C5EA  0F BA E1 1D                     bt ecx, 0x1d
0051C5EE  0F 82 BF 00 00 00               jb 0x14051c6b3
0051C5F4  F7 07 00 00 20 00               test dword ptr [rdi], 0x200000
0051C5FA  0F 84 B3 00 00 00               je 0x14051c6b3
0051C600  F6 C1 01                        test cl, 1
0051C603  0F 84 AA 00 00 00               je 0x14051c6b3
0051C609  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0051C60F  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0051C615  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0051C61C  2B C1                           sub eax, ecx
0051C61E  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0051C625  48 8D 14 19                     lea rdx, [rcx + rbx]
0051C629  8B C8                           mov ecx, eax
0051C62B  48 C1 E9 03                     shr rcx, 3
0051C62F  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0051C633  49 3B D1                        cmp rdx, r9
0051C636  74 2D                           je 0x14051c665
0051C638  4C 31 02                        xor qword ptr [rdx], r8
0051C63B  48 8B 02                        mov rax, qword ptr [rdx]
0051C63E  48 83 C2 08                     add rdx, 8
0051C642  41 0F B6 C8                     movzx ecx, r8b
0051C646  49 33 C2                        xor rax, r10
0051C649  83 E1 3F                        and ecx, 0x3f
0051C64C  49 D3 C8                        ror r8, cl
0051C64F  4C 03 C0                        add r8, rax
0051C652  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0051C659  49 3B D1                        cmp rdx, r9
0051C65C  75 DA                           jne 0x14051c638
0051C65E  48 8D BB DC 09 00 00            lea rdi, [rbx + 0x9dc]
0051C665  0F BA 37 15                     btr dword ptr [rdi], 0x15
0051C669  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0051C670  74 41                           je 0x14051c6b3
0051C672  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0051C678  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C67F  48 89 18                        mov qword ptr [rax], rbx
0051C682  89 48 10                        mov dword ptr [rax + 0x10], ecx
0051C685  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0051C68C  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0051C693  75 0E                           jne 0x14051c6a3
0051C695  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0051C69C  49 33 C8                        xor rcx, r8
0051C69F  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0051C6A3  33 D2                           xor edx, edx
0051C6A5  41 B9 00 01 00 00               mov r9d, 0x100
0051C6AB  48 8B CB                        mov rcx, rbx
0051C6AE  E8 D1 BC 6C 00                  call 0x140be8384
0051C6B3  C1 E6 04                        shl esi, 4
0051C6B6  01 B3 48 08 00 00               add dword ptr [rbx + 0x848], esi
0051C6BC  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0051C6C1  48 83 C4 30                     add rsp, 0x30
0051C6C5  41 5F                           pop r15
0051C6C7  41 5E                           pop r14
0051C6C9  41 5D                           pop r13
0051C6CB  41 5C                           pop r12
0051C6CD  5F                              pop rdi
0051C6CE  5E                              pop rsi
0051C6CF  5D                              pop rbp
0051C6D0  C3                              ret
0051C6D1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0051C138(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 40)))) & (4)) != 0) goto loc_0051C6BC;
    if ((*(unsigned __int64 *)(a2 + 8)) >= (*(unsigned __int64 *)(a2 + 8) + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1)) goto loc_0051C195;
loc_0051C189:
    result = (*(unsigned __int64 *)(a2 + 8)) + (64);
    if (result < (*(unsigned __int64 *)(a2 + 8) + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1)) goto loc_0051C189;
loc_0051C195:
    v_r12 = (unsigned int)((v_r12) | (0xFFFFFFFFULL));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) >> (7));
    if ((unsigned int)(v_rsi) == 0) goto loc_0051C1FE;
loc_0051C1AC:
loc_0051C1B1:
    v_rdi = (*(unsigned __int64 *)(a1 + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)));
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 8));
    a4 = (*(unsigned __int64 *)(a2 + 8)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0051C1B1;
    a1 = (a4) - (*(unsigned __int64 *)(a2 + 8));
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)((a1) ^ ((unsigned int)(a2)));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2100)))));
    result = (unsigned int)((result) & (63));
    v_r10 = 1;
    if (condition_is_not_equal) { v_r10 = (unsigned int)(result); }
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_r12)));
    if (condition_is_not_equal) goto loc_0051C1AC;
loc_0051C1FE:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) & (127));
    if (((unsigned int)(a3)) < 8) goto loc_0051C225;
    result = ((unsigned int)((unsigned int)(a3))) >> (3);
loc_0051C20F:
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a3 = (unsigned int)((a3) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0051C20F;
loc_0051C225:
    if ((unsigned int)(a3) == 0) goto loc_0051C23F;
loc_0051C22A:
    v_rdi = (v_rdi) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r12)));
    if (condition_is_not_equal) goto loc_0051C22A;
loc_0051C23F:
    goto loc_0051C246;
loc_0051C244:
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(v_rdi)));
loc_0051C246:
    result = (v_rdi) >> (31);
    if (result != 0) goto loc_0051C244;
    v_rsi = 0;
    if (((unsigned int)(v_rdi)) == (*(unsigned int *)(a2 + 20))) goto loc_0051C470;
    if ((*(unsigned int *)(a2)) == 0) {
        if ((*(unsigned int *)(a2 + 24)) != 0) { v_rsi = 1; }
    }
    if ((unsigned int)(*(unsigned int *)(a2 + 16)) == 0) goto loc_0051C341;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (64)) == 0) goto loc_0051C341;
    v_stack_p10 = v_cr8;
    v_r15 = (*(unsigned __int64 *)(a2 + 8)) & (0xFFFFFFFFFFFFF000ULL);
    v_r13 = ((unsigned int)(*(unsigned int *)(a2 + 16)) - 1) + (*(unsigned __int64 *)(a2 + 8));
    v_r13 = (v_r13) | (0xFFFULL);
loc_0051C2CF:
    a2 = 0;
    result = KeGuardDispatchICall(v_r15, a2, result + 2, a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0051C306;
    if ((unsigned int)(v_rsi) != 0) goto loc_0051C323;
    if (v_stack_p10 > 1) goto loc_0051C30A;
    goto loc_0051C2CF;
loc_0051C306:
    if (sign_flag) goto loc_0051C323;
loc_0051C30A:
    v_r15 = (v_r15) + ((unsigned int)(0x1000ULL));
    v_r12 = (v_r15 - 1) + ((unsigned int)(0x1000ULL));
    if (v_r12 != v_r13) goto loc_0051C2CF;
    goto loc_0051C470;
loc_0051C323:
loc_0051C341:
    result = (unsigned int)(*(unsigned int *)(a2 + 20));
    if ((*(unsigned int *)(a1 + 2328)) == 0) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 20)));
        result = (unsigned int)(v_rdi);
        a1 = (a1) ^ (result);
        result = *(unsigned __int64 *)(a1 + 1416);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051C470;
    *(unsigned __int64 *)(a1 + 2336) = a1 + a4 * 1;
    *(unsigned __int64 *)(a1 + 2344) = a2 + *(unsigned __int64 *)(a2 + 8) * 1;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(a2));
    *(unsigned __int64 *)(a1 + 2360) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned int *)(a1 + 2328) = 1;
    if ((*(unsigned int *)(a1 + 2328)) < 0) goto loc_0051C470;
    if (((*(unsigned int *)((unsigned int)(0x9DCULL) + a1 * 1)) & (0x200000ULL)) == 0) goto loc_0051C470;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520))))) == 0) goto loc_0051C470;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0051C41B;
loc_0051C3FA:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1)) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
loc_0051C41B:
    if (a4 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051C3FA;
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051C470;
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
loc_0051C470:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))) == 0) goto loc_0051C6BC;
    result = sub_0051AF4C(a1, *(unsigned __int64 *)(a2 + 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))), v_stack_m48);
loc_0051C49E:
    a4 = (v_stack_m48) + (8);
    a3 = (a2 + 24) + (8);
    if ((*(unsigned __int64 *)(v_stack_m48)) != (*(unsigned __int64 *)(a2 + 24))) goto loc_0051C4DB;
    a2 = (unsigned int)((16) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_0051C49E;
    if ((unsigned int)(a2) == 0) goto loc_0051C6B3;
loc_0051C4C1:
    a4 = (a4) + 1;
    a3 = (a3) + 1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(a3)))) goto loc_0051C4DB;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0051C4C1;
    goto loc_0051C6B3;
loc_0051C4DB:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 40))) & (1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2524)))) & (64)) == 0) goto loc_0051C590;
    v_stack_p10 = (unsigned __int8)(v_cr8);
    v_r15 = (*(unsigned __int64 *)(a2 + 8)) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(unsigned __int64 *)(a2 + 8) - 1) + ((unsigned int)(*(unsigned int *)(a2 + 16)));
    result = (result) | (0xFFFULL);
    v_stack_p18 = result;
loc_0051C531:
    a2 = 0;
    result = KeGuardDispatchICall(v_r15, a2, (unsigned __int8)(v_cr8), a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0051C56A;
    if ((unsigned int)(v_r13) != 0) goto loc_0051C58C;
    if (v_stack_p10 > 1) goto loc_0051C56E;
    goto loc_0051C531;
loc_0051C56A:
    if (sign_flag) goto loc_0051C58C;
loc_0051C56E:
    v_r15 = (v_r15) + ((unsigned int)(0x1000ULL));
    v_r12 = (v_r15 - 1) + ((unsigned int)(0x1000ULL));
    if (v_r12 != v_stack_p18) goto loc_0051C531;
    goto loc_0051C6B3;
loc_0051C58C:
loc_0051C590:
    if ((*(unsigned int *)(a1 + 2328)) != 0) goto loc_0051C6B3;
    result = ((unsigned int)(0x1000ULL)) + (a1);
    *(unsigned __int64 *)(a1 + 2336) = result;
    result = (result) + (0);
    *(unsigned __int64 *)(a1 + 2344) = result;
    *(unsigned __int64 *)(a1 + 2352) = (int)(*(unsigned int *)(a2));
    *(unsigned __int64 *)(a1 + 2360) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned int *)(a1 + 2328) = 1;
    if (condition_is_below) goto loc_0051C6B3;
    if (((*(unsigned int *)(a1 + 2524)) & (0x200000ULL)) == 0) goto loc_0051C6B3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2520)))) & (1)) == 0) goto loc_0051C6B3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    if (((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) == ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051C665;
loc_0051C638:
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1) + (8);
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1)) ^ (*(unsigned __int64 *)(a1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    if (a2 != ((unsigned int)(*(unsigned int *)(a1 + 2676)) + a1 * 1 + a1 * 8)) goto loc_0051C638;
loc_0051C665:
    if (a3 == (*(unsigned __int64 *)(a1 + 2688))) goto loc_0051C6B3;
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
loc_0051C6B3:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) << (4));
loc_0051C6BC:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0051C138(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)))) & (4)) != 0) goto loc_0051C6BC;
    if ((*(uint64_t *)(arg2 + 0x8)) >= (*(uint64_t *)(arg2 + 0x8) + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1)) goto loc_0051C195;
loc_0051C189:
    result = (*(uint64_t *)(arg2 + 0x8)) + (64);
    if (result < (*(uint64_t *)(arg2 + 0x8) + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1)) goto loc_0051C189;
loc_0051C195:
    local_r12 = (uint32_t)((local_r12) | (0xFFFFFFFFULL));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) >> (7));
    if ((uint32_t)(local_rsi) == 0) goto loc_0051C1FE;
loc_0051C1AC:
loc_0051C1B1:
    local_rdi = (*(uint64_t *)(arg1 + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)));
    local_rdi = (local_rdi) ^ (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x8));
    a4 = (*(uint64_t *)(arg2 + 0x8)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0051C1B1;
    Arg1 = (a4) - (*(uint64_t *)(arg2 + 0x8));
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)((Arg1) ^ ((uint32_t)(Arg2)));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x834)))));
    result = (uint32_t)((result) & (63));
    local_r10 = 1;
    if (condition_is_not_equal) { local_r10 = (uint32_t)(result); }
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_r12)));
    if (condition_is_not_equal) goto loc_0051C1AC;
loc_0051C1FE:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) & (127));
    if (((uint32_t)(a3)) < 8) goto loc_0051C225;
    result = ((uint32_t)((uint32_t)(a3))) >> (3);
loc_0051C20F:
    local_rdi = (local_rdi) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    a3 = (uint32_t)((a3) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0051C20F;
loc_0051C225:
    if ((uint32_t)(a3) == 0) goto loc_0051C23F;
loc_0051C22A:
    local_rdi = (local_rdi) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (1);
    a3 = (uint32_t)((a3) + ((uint32_t)(local_r12)));
    if (condition_is_not_equal) goto loc_0051C22A;
loc_0051C23F:
    goto loc_0051C246;
loc_0051C244:
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(local_rdi)));
loc_0051C246:
    result = (local_rdi) >> (31);
    if (result != 0) goto loc_0051C244;
    local_rsi = 0;
    if (((uint32_t)(local_rdi)) == (*(uint32_t *)(arg2 + 0x14))) goto loc_0051C470;
    if ((*(uint32_t *)(arg2)) == 0) {
        if ((*(uint32_t *)(arg2 + 0x18)) != 0) { local_rsi = 1; }
    }
    if ((uint32_t)(*(uint32_t *)(arg2 + 0x10)) == 0) goto loc_0051C341;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (64)) == 0) goto loc_0051C341;
    v_stack_p10 = v_cr8;
    local_r15 = (*(uint64_t *)(arg2 + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    local_r13 = ((uint32_t)(*(uint32_t *)(arg2 + 0x10)) - 1) + (*(uint64_t *)(arg2 + 0x8));
    local_r13 = (local_r13) | (0xFFFULL);
loc_0051C2CF:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_r15, Arg2, result + 2, a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0051C306;
    if ((uint32_t)(local_rsi) != 0) goto loc_0051C323;
    if (v_stack_p10 > 1) goto loc_0051C30A;
    goto loc_0051C2CF;
loc_0051C306:
    if (sign_flag) goto loc_0051C323;
loc_0051C30A:
    local_r15 = (local_r15) + ((uint32_t)(0x1000ULL));
    local_r12 = (local_r15 - 1) + ((uint32_t)(0x1000ULL));
    if (local_r12 != local_r13) goto loc_0051C2CF;
    goto loc_0051C470;
loc_0051C323:
loc_0051C341:
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x14));
    if ((*(uint32_t *)(arg1 + 0x918)) == 0) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x14)));
        result = (uint32_t)(local_rdi);
        Arg1 = (Arg1) ^ (result);
        result = *(uint64_t *)(arg1 + 0x588);
        *(void **)(result + 0x18) = Arg1;
    }
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051C470;
    *(void **)(arg1 + 0x920) = Arg1 + a4 * 1;
    *(void **)(arg1 + 0x928) = Arg2 + *(uint64_t *)(arg2 + 0x8) * 1;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(arg2));
    *(uint64_t *)(arg1 + 0x938) = *(uint64_t *)(arg2 + 0x8);
    *(uint32_t *)(arg1 + 0x918) = 1;
    if ((*(uint32_t *)(arg1 + 0x918)) < 0) goto loc_0051C470;
    if (((*(uint32_t *)((uint32_t)(0x9DCULL) + arg1 * 1)) & (0x200000ULL)) == 0) goto loc_0051C470;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))))) == 0) goto loc_0051C470;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0051C41B;
loc_0051C3FA:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1)) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
loc_0051C41B:
    if (a4 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051C3FA;
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051C470;
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
loc_0051C470:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))) == 0) goto loc_0051C6BC;
    result = sub_0051AF4C(Arg1, *(uint64_t *)(arg2 + 0x8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))), v_stack_m48);
loc_0051C49E:
    a4 = (v_stack_m48) + (8);
    a3 = (Arg2 + 24) + (8);
    if ((*(uint64_t *)(v_stack_m48)) != (*(uint64_t *)(arg2 + 0x18))) goto loc_0051C4DB;
    Arg2 = (uint32_t)((16) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_0051C49E;
    if ((uint32_t)(Arg2) == 0) goto loc_0051C6B3;
loc_0051C4C1:
    a4 = (a4) + 1;
    a3 = (a3) + 1;
    if (((uint8_t)(*(uint8_t *)(a4))) != ((uint8_t)(*(uint8_t *)(a3)))) goto loc_0051C4DB;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0051C4C1;
    goto loc_0051C6B3;
loc_0051C4DB:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x28))) & (1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)))) & (64)) == 0) goto loc_0051C590;
    v_stack_p10 = (uint8_t)(v_cr8);
    local_r15 = (*(uint64_t *)(arg2 + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(uint64_t *)(arg2 + 0x8) - 1) + ((uint32_t)(*(uint32_t *)(arg2 + 0x10)));
    result = (result) | (0xFFFULL);
    v_stack_p18 = result;
loc_0051C531:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_r15, Arg2, (uint8_t)(v_cr8), a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0051C56A;
    if ((uint32_t)(local_r13) != 0) goto loc_0051C58C;
    if (v_stack_p10 > 1) goto loc_0051C56E;
    goto loc_0051C531;
loc_0051C56A:
    if (sign_flag) goto loc_0051C58C;
loc_0051C56E:
    local_r15 = (local_r15) + ((uint32_t)(0x1000ULL));
    local_r12 = (local_r15 - 1) + ((uint32_t)(0x1000ULL));
    if (local_r12 != v_stack_p18) goto loc_0051C531;
    goto loc_0051C6B3;
loc_0051C58C:
loc_0051C590:
    if ((*(uint32_t *)(arg1 + 0x918)) != 0) goto loc_0051C6B3;
    result = ((uint32_t)(0x1000ULL)) + (Arg1);
    *(uint64_t *)(arg1 + 0x920) = result;
    result = (result) + (0);
    *(uint64_t *)(arg1 + 0x928) = result;
    *(uint64_t *)(arg1 + 0x930) = (int32_t)(*(uint32_t *)(arg2));
    *(uint64_t *)(arg1 + 0x938) = *(uint64_t *)(arg2 + 0x8);
    *(uint32_t *)(arg1 + 0x918) = 1;
    if (condition_is_below) goto loc_0051C6B3;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0051C6B3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8)))) & (1)) == 0) goto loc_0051C6B3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    if (((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) == ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051C665;
loc_0051C638:
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1) + (8);
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + arg1 * 1)) ^ (*(uint64_t *)(arg1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg1 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    if (Arg2 != ((uint32_t)(*(uint32_t *)(arg1 + 0xA74)) + Arg1 * 1 + Arg1 * 8)) goto loc_0051C638;
loc_0051C665:
    if (a3 == (*(uint64_t *)(arg1 + 0xA80))) goto loc_0051C6B3;
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
loc_0051C6B3:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) << (4));
loc_0051C6BC:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0 + r9*1` | `64` | `R` |
| `Arg1` | `+ 0x468` | `64` | `R` |
| `Arg1` | `+ 0x588` | `64` | `R` |
| `Arg1` | `+ 0x804` | `32` | `R` |
| `Arg1` | `+ 0x834` | `32` | `R` |
| `Arg1` | `+ 0x838` | `64` | `R` |
| `Arg1` | `+ 0x848` | `32` | `R/W` |
| `Arg1` | `+ 0x918` | `32` | `R` |
| `Arg1` | `+ 0x918` | `32` | `W` |
| `Arg1` | `+ 0x920` | `64` | `W` |
| `Arg1` | `+ 0x928` | `64` | `W` |
| `Arg1` | `+ 0x930` | `64` | `W` |
| `Arg1` | `+ 0x938` | `64` | `W` |
| `Arg1` | `+ 0x9D8` | `32` | `R` |
| `Arg1` | `+ 0x9DC` | `32` | `R` |
| `Arg1` | `+ 0x9DC` | `64` | `R` |
| `Arg1` | `+ 0xA74` | `32` | `R` |
| `Arg1` | `+ 0xA78` | `64` | `R` |
| `Arg1` | `+ 0xA80` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0 + r11*1` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x14` | `32` | `R` |
| `Arg2` | `+ 0x18` | `32` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0051C138&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
