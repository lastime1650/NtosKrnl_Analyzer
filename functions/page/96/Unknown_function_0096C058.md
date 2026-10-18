# sub_0096C058

- RVA: `0x0096C058`–`0x0096C41B` (길이 `963` bytes)
- VA: `0x000000014096C058`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000952D8`
- 디코드: `276`개 명령, `963/963` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0096C105` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0096C138` → [sub_0096BFF0](Unknown_function_0096BFF0.md) (function, `0x0096BFF0`)
- `0x0096C14C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096C17E` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0096C1A5` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0096C1D6` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0096C1FF` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)
- `0x0096C24A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [sub_00968AF6](Unknown_function_00968AF6.md) at `0x0096A396`

### Static image references
- `0x0096C0E7` → RVA `0x00B57960` (` ?? ::LBKOJDO::`string'`; read)
- `0x0096C10A` → RVA `0x00FD8448` (`PAGEDATA`; read)
- `0x0096C111` → RVA `0x0096BFF0` (`PAGE`; read)
- `0x0096C177` → RVA `0x00EF0DC0` (`.data`; read)
- `0x0096C183` → RVA `0x00FD8184` (`PAGEDATA`; write)
- `0x0096C1C4` → RVA `0x00EF0DE0` (`.data`; read)
- `0x0096C370` → RVA `0x00FD8058` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0096C105` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0096C14C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0096C17E` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x0096C1A5` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0096C1D6` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0096C1FF` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
  - `0x0096C24A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0096C058  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0096C05D  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0096C062  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0096C067  55                              push rbp
0096C068  57                              push rdi
0096C069  41 57                           push r15
0096C06B  48 8B EC                        mov rbp, rsp
0096C06E  48 83 EC 50                     sub rsp, 0x50
0096C072  49 8B F9                        mov rdi, r9
0096C075  48 8B DA                        mov rbx, rdx
0096C078  48 85 C9                        test rcx, rcx
0096C07B  75 0B                           jne 0x14096c088
0096C07D  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
0096C083  E9 7A 03 00 00                  jmp 0x14096c402
0096C088  48 85 DB                        test rbx, rbx
0096C08B  74 F0                           je 0x14096c07d
0096C08D  48 85 FF                        test rdi, rdi
0096C090  74 EB                           je 0x14096c07d
0096C092  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0096C096  48 85 C0                        test rax, rax
0096C099  74 E2                           je 0x14096c07d
0096C09B  83 39 03                        cmp dword ptr [rcx], 3
0096C09E  76 DD                           jbe 0x14096c07d
0096C0A0  33 D2                           xor edx, edx
0096C0A2  44 8B 00                        mov r8d, dword ptr [rax]
0096C0A5  48 8D 48 04                     lea rcx, [rax + 4]
0096C0A9  83 FA 03                        cmp edx, 3
0096C0AC  73 1A                           jae 0x14096c0c8
0096C0AE  48 3B C8                        cmp rcx, rax
0096C0B1  0F 82 45 03 00 00               jb 0x14096c3fc
0096C0B7  4A 8D 04 01                     lea rax, [rcx + r8]
0096C0BB  48 3B C1                        cmp rax, rcx
0096C0BE  0F 82 38 03 00 00               jb 0x14096c3fc
0096C0C4  FF C2                           inc edx
0096C0C6  EB DA                           jmp 0x14096c0a2
0096C0C8  48 3B C8                        cmp rcx, rax
0096C0CB  0F 82 2B 03 00 00               jb 0x14096c3fc
0096C0D1  33 C0                           xor eax, eax
0096C0D3  45 85 C0                        test r8d, r8d
0096C0D6  48 0F 45 C1                     cmovne rax, rcx
0096C0DA  41 83 F8 08                     cmp r8d, 8
0096C0DE  0F 85 72 02 00 00               jne 0x14096c356
0096C0E4  4C 8B 38                        mov r15, qword ptr [rax]
0096C0E7  48 8D 15 72 B8 1E 00            lea rdx, [rip + 0x1eb872]
0096C0EE  83 65 30 00                     and dword ptr [rbp + 0x30], 0
0096C0F2  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0096C0F6  83 65 20 00                     and dword ptr [rbp + 0x20], 0
0096C0FA  0F 57 C0                        xorps xmm0, xmm0
0096C0FD  83 65 E0 00                     and dword ptr [rbp - 0x20], 0
0096C101  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
0096C105  E8 76 E6 AB FF                  call 0x14042a780
0096C10A  48 8B 05 37 C3 66 00            mov rax, qword ptr [rip + 0x66c337]
0096C111  48 8D 0D D8 FE FF FF            lea rcx, [rip - 0x128]
0096C118  4C 8D 45 20                     lea r8, [rbp + 0x20]
0096C11C  41 B9 04 00 00 00               mov r9d, 4
0096C122  48 8D 55 30                     lea rdx, [rbp + 0x30]
0096C126  48 3B C1                        cmp rax, rcx
0096C129  75 14                           jne 0x14096c13f
0096C12B  48 8D 45 E0                     lea rax, [rbp - 0x20]
0096C12F  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0096C133  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096C138  E8 B3 FE FF FF                  call 0x14096bff0
0096C13D  EB 12                           jmp 0x14096c151
0096C13F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0096C143  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096C148  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0096C14C  E8 7F E9 D4 FF                  call 0x1406baad0
0096C151  44 8B C0                        mov r8d, eax
0096C154  3D 34 00 00 C0                  cmp eax, 0xc0000034
0096C159  74 28                           je 0x14096c183
0096C15B  85 C0                           test eax, eax
0096C15D  0F 88 9F 02 00 00               js 0x14096c402
0096C163  83 7D 30 04                     cmp dword ptr [rbp + 0x30], 4
0096C167  75 1A                           jne 0x14096c183
0096C169  83 7D 20 00                     cmp dword ptr [rbp + 0x20], 0
0096C16D  74 14                           je 0x14096c183
0096C16F  85 C0                           test eax, eax
0096C171  0F 88 8B 02 00 00               js 0x14096c402
0096C177  48 8D 0D 42 4C 58 00            lea rcx, [rip + 0x584c42]
0096C17E  E8 CD C1 8D FF                  call 0x140248350
0096C183  C7 05 F7 BF 66 00 01 00 00 00   mov dword ptr [rip + 0x66bff7], 1
0096C18D  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0096C193  48 8D 0D 26 4C 58 00            lea rcx, [rip + 0x584c26]
0096C19A  41 B1 01                        mov r9b, 1
0096C19D  BA 06 00 00 00                  mov edx, 6
0096C1A2  45 8A C1                        mov r8b, r9b
0096C1A5  E8 06 25 8A FF                  call 0x14020e6b0
0096C1AA  8B F0                           mov esi, eax
0096C1AC  3D 01 01 00 00                  cmp eax, 0x101
0096C1B1  74 DA                           je 0x14096c18d
0096C1B3  85 C0                           test eax, eax
0096C1B5  78 4D                           js 0x14096c204
0096C1B7  3D C0 00 00 00                  cmp eax, 0xc0
0096C1BC  74 46                           je 0x14096c204
0096C1BE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0096C1C4  48 8D 0D 15 4C 58 00            lea rcx, [rip + 0x584c15]
0096C1CB  41 B1 01                        mov r9b, 1
0096C1CE  BA 06 00 00 00                  mov edx, 6
0096C1D3  45 8A C1                        mov r8b, r9b
0096C1D6  E8 D5 24 8A FF                  call 0x14020e6b0
0096C1DB  8B F0                           mov esi, eax
0096C1DD  3D 01 01 00 00                  cmp eax, 0x101
0096C1E2  74 DA                           je 0x14096c1be
0096C1E4  85 C0                           test eax, eax
0096C1E6  78 1C                           js 0x14096c204
0096C1E8  3D C0 00 00 00                  cmp eax, 0xc0
0096C1ED  74 15                           je 0x14096c204
0096C1EF  3D 02 01 00 00                  cmp eax, 0x102
0096C1F4  74 0E                           je 0x14096c204
0096C1F6  33 D2                           xor edx, edx
0096C1F8  48 8D 0D E1 4B 58 00            lea rcx, [rip + 0x584be1]
0096C1FF  E8 0C A6 A2 FF                  call 0x140396810
0096C204  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0096C207  8B 53 20                        mov edx, dword ptr [rbx + 0x20]
0096C20A  83 C0 38                        add eax, 0x38
0096C20D  83 F8 38                        cmp eax, 0x38
0096C210  0F 82 E6 01 00 00               jb 0x14096c3fc
0096C216  8D 48 04                        lea ecx, [rax + 4]
0096C219  3B C8                           cmp ecx, eax
0096C21B  0F 82 DB 01 00 00               jb 0x14096c3fc
0096C221  8D 04 11                        lea eax, [rcx + rdx]
0096C224  BB 95 00 00 C0                  mov ebx, 0xc0000095
0096C229  3B C1                           cmp eax, ecx
0096C22B  45 1B C0                        sbb r8d, r8d
0096C22E  44 23 C3                        and r8d, ebx
0096C231  0F 8C CB 01 00 00               jl 0x14096c402
0096C237  BA 1C 00 00 00                  mov edx, 0x1c
0096C23C  B9 00 01 00 00                  mov ecx, 0x100
0096C241  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096C247  89 57 04                        mov dword ptr [rdi + 4], edx
0096C24A  E8 A1 5E 21 00                  call 0x140b820f0
0096C24F  48 85 C0                        test rax, rax
0096C252  75 09                           jne 0x14096c25d
0096C254  44 8D 43 82                     lea r8d, [rbx - 0x7e]
0096C258  E9 A5 01 00 00                  jmp 0x14096c402
0096C25D  48 89 47 08                     mov qword ptr [rdi + 8], rax
0096C261  83 27 00                        and dword ptr [rdi], 0
0096C264  0F BA EE 1C                     bts esi, 0x1c
0096C268  48 8B D0                        mov rdx, rax
0096C26B  48 85 C0                        test rax, rax
0096C26E  75 1B                           jne 0x14096c28b
0096C270  8B 47 04                        mov eax, dword ptr [rdi + 4]
0096C273  8D 48 08                        lea ecx, [rax + 8]
0096C276  3B C8                           cmp ecx, eax
0096C278  72 05                           jb 0x14096c27f
0096C27A  89 4F 04                        mov dword ptr [rdi + 4], ecx
0096C27D  EB 58                           jmp 0x14096c2d7
0096C27F  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
0096C283  44 8B C3                        mov r8d, ebx
0096C286  E9 77 01 00 00                  jmp 0x14096c402
0096C28B  44 8B 0F                        mov r9d, dword ptr [rdi]
0096C28E  33 C9                           xor ecx, ecx
0096C290  41 3B C9                        cmp ecx, r9d
0096C293  73 1C                           jae 0x14096c2b1
0096C295  8B 02                           mov eax, dword ptr [rdx]
0096C297  83 C0 04                        add eax, 4
0096C29A  83 F8 04                        cmp eax, 4
0096C29D  72 E4                           jb 0x14096c283
0096C29F  44 8B C0                        mov r8d, eax
0096C2A2  4C 03 C2                        add r8, rdx
0096C2A5  4C 3B C2                        cmp r8, rdx
0096C2A8  72 D9                           jb 0x14096c283
0096C2AA  49 8B D0                        mov rdx, r8
0096C2AD  FF C1                           inc ecx
0096C2AF  EB DF                           jmp 0x14096c290
0096C2B1  4C 8D 42 04                     lea r8, [rdx + 4]
0096C2B5  4C 3B C2                        cmp r8, rdx
0096C2B8  72 C9                           jb 0x14096c283
0096C2BA  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
0096C2BD  48 8D 42 08                     lea rax, [rdx + 8]
0096C2C1  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
0096C2C5  48 3B C1                        cmp rax, rcx
0096C2C8  0F 87 88 00 00 00               ja 0x14096c356
0096C2CE  C7 02 04 00 00 00               mov dword ptr [rdx], 4
0096C2D4  41 89 30                        mov dword ptr [r8], esi
0096C2D7  FF 07                           inc dword ptr [rdi]
0096C2D9  41 83 C9 FF                     or r9d, 0xffffffff
0096C2DD  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0096C2E1  48 85 D2                        test rdx, rdx
0096C2E4  75 25                           jne 0x14096c30b
0096C2E6  8B 57 04                        mov edx, dword ptr [rdi + 4]
0096C2E9  41 8B C1                        mov eax, r9d
0096C2EC  8D 4A 0C                        lea ecx, [rdx + 0xc]
0096C2EF  3B CA                           cmp ecx, edx
0096C2F1  0F 43 C1                        cmovae eax, ecx
0096C2F4  45 1B C0                        sbb r8d, r8d
0096C2F7  44 23 C3                        and r8d, ebx
0096C2FA  89 47 04                        mov dword ptr [rdi + 4], eax
0096C2FD  3B CA                           cmp ecx, edx
0096C2FF  73 69                           jae 0x14096c36a
0096C301  45 85 C0                        test r8d, r8d
0096C304  79 66                           jns 0x14096c36c
0096C306  E9 F7 00 00 00                  jmp 0x14096c402
0096C30B  44 8B 17                        mov r10d, dword ptr [rdi]
0096C30E  33 C9                           xor ecx, ecx
0096C310  41 3B CA                        cmp ecx, r10d
0096C313  73 24                           jae 0x14096c339
0096C315  8B 02                           mov eax, dword ptr [rdx]
0096C317  83 C0 04                        add eax, 4
0096C31A  83 F8 04                        cmp eax, 4
0096C31D  0F 82 60 FF FF FF               jb 0x14096c283
0096C323  44 8B C0                        mov r8d, eax
0096C326  4C 03 C2                        add r8, rdx
0096C329  4C 3B C2                        cmp r8, rdx
0096C32C  0F 82 51 FF FF FF               jb 0x14096c283
0096C332  49 8B D0                        mov rdx, r8
0096C335  FF C1                           inc ecx
0096C337  EB D7                           jmp 0x14096c310
0096C339  4C 8D 42 04                     lea r8, [rdx + 4]
0096C33D  4C 3B C2                        cmp r8, rdx
0096C340  0F 82 3D FF FF FF               jb 0x14096c283
0096C346  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
0096C349  48 8D 42 0C                     lea rax, [rdx + 0xc]
0096C34D  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
0096C351  48 3B C1                        cmp rax, rcx
0096C354  76 0B                           jbe 0x14096c361
0096C356  41 B8 23 00 00 C0               mov r8d, 0xc0000023
0096C35C  E9 A1 00 00 00                  jmp 0x14096c402
0096C361  C7 02 08 00 00 00               mov dword ptr [rdx], 8
0096C367  4D 89 38                        mov qword ptr [r8], r15
0096C36A  FF 07                           inc dword ptr [rdi]
0096C36C  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0096C370  44 8B 15 E1 BC 66 00            mov r10d, dword ptr [rip + 0x66bce1]
0096C377  48 85 D2                        test rdx, rdx
0096C37A  75 21                           jne 0x14096c39d
0096C37C  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
0096C37F  8D 41 08                        lea eax, [rcx + 8]
0096C382  3B C1                           cmp eax, ecx
0096C384  44 0F 43 C8                     cmovae r9d, eax
0096C388  45 1B C0                        sbb r8d, r8d
0096C38B  44 23 C3                        and r8d, ebx
0096C38E  44 89 4F 04                     mov dword ptr [rdi + 4], r9d
0096C392  3B C1                           cmp eax, ecx
0096C394  72 6C                           jb 0x14096c402
0096C396  FF 07                           inc dword ptr [rdi]
0096C398  45 33 C0                        xor r8d, r8d
0096C39B  EB 65                           jmp 0x14096c402
0096C39D  44 8B 0F                        mov r9d, dword ptr [rdi]
0096C3A0  33 C9                           xor ecx, ecx
0096C3A2  41 3B C9                        cmp ecx, r9d
0096C3A5  73 24                           jae 0x14096c3cb
0096C3A7  8B 02                           mov eax, dword ptr [rdx]
0096C3A9  83 C0 04                        add eax, 4
0096C3AC  83 F8 04                        cmp eax, 4
0096C3AF  0F 82 CE FE FF FF               jb 0x14096c283
0096C3B5  44 8B C0                        mov r8d, eax
0096C3B8  4C 03 C2                        add r8, rdx
0096C3BB  4C 3B C2                        cmp r8, rdx
0096C3BE  0F 82 BF FE FF FF               jb 0x14096c283
0096C3C4  49 8B D0                        mov rdx, r8
0096C3C7  FF C1                           inc ecx
0096C3C9  EB D7                           jmp 0x14096c3a2
0096C3CB  4C 8D 4A 04                     lea r9, [rdx + 4]
0096C3CF  4C 3B CA                        cmp r9, rdx
0096C3D2  0F 82 AB FE FF FF               jb 0x14096c283
0096C3D8  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
0096C3DB  48 8D 42 08                     lea rax, [rdx + 8]
0096C3DF  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
0096C3E3  45 33 C0                        xor r8d, r8d
0096C3E6  48 3B C1                        cmp rax, rcx
0096C3E9  0F 87 67 FF FF FF               ja 0x14096c356
0096C3EF  C7 02 04 00 00 00               mov dword ptr [rdx], 4
0096C3F5  45 89 11                        mov dword ptr [r9], r10d
0096C3F8  FF 07                           inc dword ptr [rdi]
0096C3FA  EB 06                           jmp 0x14096c402
0096C3FC  41 B8 95 00 00 C0               mov r8d, 0xc0000095
0096C402  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0096C407  41 8B C0                        mov eax, r8d
0096C40A  49 8B 5B 28                     mov rbx, qword ptr [r11 + 0x28]
0096C40E  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0096C412  49 8B E3                        mov rsp, r11
0096C415  41 5F                           pop r15
0096C417  5F                              pop rdi
0096C418  5D                              pop rbp
0096C419  C3                              ret
0096C41A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0096C058(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    if (a1 != 0) goto loc_0096C088;
loc_0096C07D:
    goto loc_0096C402;
loc_0096C088:
    if (a2 == 0) goto loc_0096C07D;
    if (a4 == 0) goto loc_0096C07D;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_0096C07D;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_0096C07D;
    a2 = 0;
loc_0096C0A2:
    if (0 >= 3) goto loc_0096C0C8;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_0096C3FC;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_0096C3FC;
    a2 = (unsigned int)((a2) + 1);
    goto loc_0096C0A2;
loc_0096C0C8:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_0096C3FC;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_0096C356;
    v_stack_m30 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m30, v_rip + 2013298, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), a4);
    if ((*(unsigned __int64 *)(v_rip + 6734647)) != (v_rip - 296)) goto loc_0096C13F;
    v_stack_m48 = v_stack_m38;
    result = sub_0096BFF0(v_stack_m30, v_stack_p18, v_stack_p8, 4);
    goto loc_0096C151;
loc_0096C13F:
    v_stack_m48 = v_stack_m38;
    result = guard_dispatch_icall(v_stack_m30, v_stack_p18, v_stack_p8, 4);
loc_0096C151:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_0096C183;
    if (sign_flag) goto loc_0096C402;
    if (v_stack_p18 != 4) goto loc_0096C183;
    if (v_stack_p8 == 0) goto loc_0096C183;
    if (sign_flag) goto loc_0096C402;
    result = KeResetEvent(v_rip + 5786690, v_stack_p18, (unsigned int)((unsigned int)(result)), 4);
loc_0096C183:
    *(unsigned int *)(v_rip + 6733815) = 1;
loc_0096C18D:
    result = KeWaitForSingleObject(v_rip + 5786662, 6, 1, 1);
    if (((unsigned int)(result)) == 257) goto loc_0096C18D;
    if (sign_flag) goto loc_0096C204;
    if (((unsigned int)(result)) == 192) goto loc_0096C204;
loc_0096C1BE:
    result = KeWaitForSingleObject(v_rip + 5786645, 6, 1, 1);
    if (((unsigned int)(result)) == 257) goto loc_0096C1BE;
    if (sign_flag) goto loc_0096C204;
    if (((unsigned int)(result)) == 192) goto loc_0096C204;
    if (((unsigned int)(result)) != 258) {
        a2 = 0;
        a1 = v_rip + 5786593;
        result = KeReleaseMutex(a1, a2, 1, 1);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (56));
    if (((unsigned int)(result)) < 56) goto loc_0096C3FC;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_0096C3FC;
    a3 = (unsigned int)((1) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (condition_is_less) goto loc_0096C402;
    *(unsigned int *)(a4 + 4) = 28;
    result = ExAllocatePool2(256, 28, (unsigned int)(0x20534C53ULL), 1);
    if (result != 0) goto loc_0096C25D;
    goto loc_0096C402;
loc_0096C25D:
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result != 0) goto loc_0096C28B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096C27F;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_0096C2D7;
loc_0096C27F:
loc_0096C283:
    goto loc_0096C402;
loc_0096C28B:
    a1 = 0;
loc_0096C290:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096C2B1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_0096C283;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_0096C283;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096C290;
loc_0096C2B1:
    if ((a3 + 4) < a3) goto loc_0096C283;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_0096C356;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_0096C2D7:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_0096C30B;
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    a3 = (unsigned int)((a3 + 4) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096C36A;
    if (!sign_flag) goto loc_0096C36C;
    goto loc_0096C402;
loc_0096C30B:
    a1 = 0;
loc_0096C310:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096C339;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a4 + 4))))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_0096C283;
    a3 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)(*(unsigned int *)(a4 + 4)));
    if (a3 < ((unsigned int)(*(unsigned int *)(a4 + 4)))) goto loc_0096C283;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096C310;
loc_0096C339:
    if ((a3 + 4) < a3) goto loc_0096C283;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) <= a1) goto loc_0096C361;
loc_0096C356:
    goto loc_0096C402;
loc_0096C361:
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)((unsigned int)(0xC0000023ULL)) = *(unsigned __int64 *)(result);
loc_0096C36A:
loc_0096C36C:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_0096C39D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8); }
    a3 = (unsigned int)(((unsigned int)(0xC0000023ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096C402;
    a3 = 0;
    goto loc_0096C402;
loc_0096C39D:
    a1 = 0;
loc_0096C3A2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096C3CB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_0096C283;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096C283;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096C3A2;
loc_0096C3CB:
    if ((a3 + 4) < a3) goto loc_0096C283;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    a3 = 0;
    if ((a3 + 8) > a1) goto loc_0096C356;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6733025)));
    goto loc_0096C402;
loc_0096C3FC:
loc_0096C402:
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_0096C058(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    if (Arg1 != 0) goto loc_0096C088;
loc_0096C07D:
    goto loc_0096C402;
loc_0096C088:
    if (Arg2 == 0) goto loc_0096C07D;
    if (Arg4 == 0) goto loc_0096C07D;
    if (*(uint64_t *)(Arg1 + 0x8) == 0) goto loc_0096C07D;
    if ((*(uint32_t *)(Arg1)) <= 3) goto loc_0096C07D;
    Arg2 = 0;
loc_0096C0A2:
    if (0 >= 3) goto loc_0096C0C8;
    if ((*(uint64_t *)(Arg1 + 0x8) + 4) < (*(uint64_t *)(Arg1 + 0x8))) goto loc_0096C3FC;
    if ((*(uint64_t *)(Arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8))) * 1) < (*(uint64_t *)(Arg1 + 0x8) + 4)) goto loc_0096C3FC;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0096C0A2;
loc_0096C0C8:
    if ((*(uint64_t *)(Arg1 + 0x8) + 4) < (*(uint64_t *)(Arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8))) * 1)) goto loc_0096C3FC;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8)))) != 0) { result = *(uint64_t *)(Arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8))))) != 8) goto loc_0096C356;
    v_stack_m30 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m30, v_rip + 2013298, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8))), Arg4);
    if ((*(uint64_t *)(v_rip + 0x66C337)) != (v_rip - 296)) goto loc_0096C13F;
    v_stack_m48 = v_stack_m38;
    result = sub_0096BFF0(v_stack_m30, v_stack_p18, v_stack_p8, 4);
    goto loc_0096C151;
loc_0096C13F:
    v_stack_m48 = v_stack_m38;
    result = guard_dispatch_icall(v_stack_m30, v_stack_p18, v_stack_p8, 4);
loc_0096C151:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_0096C183;
    if (sign_flag) goto loc_0096C402;
    if (v_stack_p18 != 4) goto loc_0096C183;
    if (v_stack_p8 == 0) goto loc_0096C183;
    if (sign_flag) goto loc_0096C402;
    result = KeResetEvent(v_rip + 5786690, v_stack_p18, (uint32_t)((uint32_t)(result)), 4);
loc_0096C183:
    *(uint32_t *)(v_rip + 0x66BFF7) = 1;
loc_0096C18D:
    result = KeWaitForSingleObject(v_rip + 5786662, 6, 1, 1);
    if (((uint32_t)(result)) == 257) goto loc_0096C18D;
    if (sign_flag) goto loc_0096C204;
    if (((uint32_t)(result)) == 192) goto loc_0096C204;
loc_0096C1BE:
    result = KeWaitForSingleObject(v_rip + 5786645, 6, 1, 1);
    if (((uint32_t)(result)) == 257) goto loc_0096C1BE;
    if (sign_flag) goto loc_0096C204;
    if (((uint32_t)(result)) == 192) goto loc_0096C204;
    if (((uint32_t)(result)) != 258) {
        Arg2 = 0;
        Arg1 = v_rip + 5786593;
        result = KeReleaseMutex(Arg1, Arg2, 1, 1);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x10))) + (56));
    if (((uint32_t)(result)) < 56) goto loc_0096C3FC;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_0096C3FC;
    Arg3 = (uint32_t)((1) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (condition_is_less) goto loc_0096C402;
    *(uint32_t *)(Arg4 + 0x4) = 28;
    result = ExAllocatePool2(256, 28, (uint32_t)(0x20534C53ULL), 1);
    if (result != 0) goto loc_0096C25D;
    goto loc_0096C402;
loc_0096C25D:
    *(uint64_t *)(Arg4 + 0x8) = result;
    if (result != 0) goto loc_0096C28B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_0096C27F;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_0096C2D7;
loc_0096C27F:
loc_0096C283:
    goto loc_0096C402;
loc_0096C28B:
    Arg1 = 0;
loc_0096C290:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_0096C2B1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_0096C283;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_0096C283;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096C290;
loc_0096C2B1:
    if ((Arg3 + 4) < Arg3) goto loc_0096C283;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_0096C356;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_0096C2D7:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4))) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_0096C30B;
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    Arg3 = (uint32_t)((Arg3 + 4) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_0096C36A;
    if (!sign_flag) goto loc_0096C36C;
    goto loc_0096C402;
loc_0096C30B:
    Arg1 = 0;
loc_0096C310:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_0096C339;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_0096C283;
    Arg3 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)));
    if (Arg3 < ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) goto loc_0096C283;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096C310;
loc_0096C339:
    if ((Arg3 + 4) < Arg3) goto loc_0096C283;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) <= Arg1) goto loc_0096C361;
loc_0096C356:
    goto loc_0096C402;
loc_0096C361:
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)((uint32_t)(0xC0000023ULL)) = *(uint64_t *)(result);
loc_0096C36A:
loc_0096C36C:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_0096C39D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8); }
    Arg3 = (uint32_t)(((uint32_t)(0xC0000023ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_0096C402;
    Arg3 = 0;
    goto loc_0096C402;
loc_0096C39D:
    Arg1 = 0;
loc_0096C3A2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_0096C3CB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_0096C283;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_0096C283;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096C3A2;
loc_0096C3CB:
    if ((Arg3 + 4) < Arg3) goto loc_0096C283;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    Arg3 = 0;
    if ((Arg3 + 8) > Arg1) goto loc_0096C356;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x66BCE1)));
    goto loc_0096C402;
loc_0096C3FC:
loc_0096C402:
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096C058&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
