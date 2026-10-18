# SepCreateImpersonationTokenDacl

- RVA: `0x008B8140`–`0x008B87E5` (길이 `1,701` bytes)
- VA: `0x00000001408B8140`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082C0C`
- 디코드: `448`개 명령, `1,701/1,701` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008B8207` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B822A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B8272` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B82F8` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B837B` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B840E` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B847D` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B84C1` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B8537` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B86B0` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x008B86DC` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B870F` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B8742` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B8775` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B87A8` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B87D4` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)

### Direct callers
- [NtOpenThreadTokenEx](NtOpenThreadTokenEx_function_008B7840.md) at `0x008B7AB8`

### Static image references
- `0x008B81A7` → RVA `0x00FD9B10` (`PAGEDATA`; read)
- `0x008B81B2` → RVA `0x00FD9A68` (`PAGEDATA`; read)
- `0x008B81BD` → RVA `0x00E67D58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008B8207` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B822A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B87D4` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B8140  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008B8145  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
008B814A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008B814F  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
008B8154  57                              push rdi
008B8155  41 54                           push r12
008B8157  41 55                           push r13
008B8159  41 56                           push r14
008B815B  41 57                           push r15
008B815D  48 83 EC 30                     sub rsp, 0x30
008B8161  48 8B 82 98 00 00 00            mov rax, qword ptr [rdx + 0x98]
008B8168  33 DB                           xor ebx, ebx
008B816A  F7 82 C8 00 00 00 00 40 00 00   test dword ptr [rdx + 0xc8], 0x4000
008B8174  4C 8B E2                        mov r12, rdx
008B8177  4C 8B E9                        mov r13, rcx
008B817A  8B FB                           mov edi, ebx
008B817C  8B F3                           mov esi, ebx
008B817E  4C 8B 38                        mov r15, qword ptr [rax]
008B8181  74 07                           je 0x1408b818a
008B8183  48 8B B2 10 03 00 00            mov rsi, qword ptr [rdx + 0x310]
008B818A  F7 81 C8 00 00 00 00 40 00 00   test dword ptr [rcx + 0xc8], 0x4000
008B8194  48 8B 81 98 00 00 00            mov rax, qword ptr [rcx + 0x98]
008B819B  4C 8B 30                        mov r14, qword ptr [rax]
008B819E  74 07                           je 0x1408b81a7
008B81A0  48 8B B9 10 03 00 00            mov rdi, qword ptr [rcx + 0x310]
008B81A7  48 8B 05 62 19 72 00            mov rax, qword ptr [rip + 0x721962]
008B81AE  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
008B81B2  48 8B 05 AF 18 72 00            mov rax, qword ptr [rip + 0x7218af]
008B81B9  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B81BD  48 8B 05 94 FB 5A 00            mov rax, qword ptr [rip + 0x5afb94]
008B81C4  03 D1                           add edx, ecx
008B81C6  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B81CA  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
008B81CF  03 D1                           add edx, ecx
008B81D1  03 D0                           add edx, eax
008B81D3  41 0F B6 47 01                  movzx eax, byte ptr [r15 + 1]
008B81D8  03 D0                           add edx, eax
008B81DA  8D 2C 95 58 00 00 00            lea ebp, [rdx*4 + 0x58]
008B81E1  48 85 FF                        test rdi, rdi
008B81E4  74 0B                           je 0x1408b81f1
008B81E6  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
008B81EA  8D 6C 85 00                     lea ebp, [rbp + rax*4]
008B81EE  83 C5 10                        add ebp, 0x10
008B81F1  48 85 F6                        test rsi, rsi
008B81F4  0F 85 BF 05 00 00               jne 0x1408b87b9
008B81FA  8B D5                           mov edx, ebp
008B81FC  B9 00 01 00 00                  mov ecx, 0x100
008B8201  41 B8 53 65 20 20               mov r8d, 0x20206553
008B8207  E8 E4 9E 2C 00                  call 0x140b820f0
008B820C  48 8B D8                        mov rbx, rax
008B820F  48 85 C0                        test rax, rax
008B8212  0F 84 B1 03 00 00               je 0x1408b85c9
008B8218  8D 45 F8                        lea eax, [rbp - 8]
008B821B  3D F4 FF 00 00                  cmp eax, 0xfff4
008B8220  77 1B                           ja 0x1408b823d
008B8222  44 8B C5                        mov r8d, ebp
008B8225  33 D2                           xor edx, edx
008B8227  48 8B CB                        mov rcx, rbx
008B822A  E8 11 EA E0 FF                  call 0x1406c6c40
008B822F  33 C0                           xor eax, eax
008B8231  66 C7 03 02 00                  mov word ptr [rbx], 2
008B8236  89 43 04                        mov dword ptr [rbx + 4], eax
008B8239  66 89 6B 02                     mov word ptr [rbx + 2], bp
008B823D  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
008B8247  4C 3B F8                        cmp r15, rax
008B824A  76 77                           jbe 0x1408b82c3
008B824C  41 0F B6 07                     movzx eax, byte ptr [r15]
008B8250  24 0F                           and al, 0xf
008B8252  3C 01                           cmp al, 1
008B8254  75 6D                           jne 0x1408b82c3
008B8256  41 80 7F 01 0F                  cmp byte ptr [r15 + 1], 0xf
008B825B  77 66                           ja 0x1408b82c3
008B825D  0F B6 2B                        movzx ebp, byte ptr [rbx]
008B8260  40 80 FD 04                     cmp bpl, 4
008B8264  77 5D                           ja 0x1408b82c3
008B8266  40 80 FD 02                     cmp bpl, 2
008B826A  77 03                           ja 0x1408b826f
008B826C  40 B5 02                        mov bpl, 2
008B826F  48 8B CB                        mov rcx, rbx
008B8272  E8 29 25 07 00                  call 0x14092a7a0
008B8277  84 C0                           test al, al
008B8279  74 48                           je 0x1408b82c3
008B827B  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
008B8280  48 8D 53 08                     lea rdx, [rbx + 8]
008B8284  45 33 C9                        xor r9d, r9d
008B8287  41 8B C9                        mov ecx, r9d
008B828A  41 3B C8                        cmp ecx, r8d
008B828D  0F 82 48 03 00 00               jb 0x1408b85db
008B8293  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
008B8298  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
008B829D  4C 03 C3                        add r8, rbx
008B82A0  49 3B D0                        cmp rdx, r8
008B82A3  49 0F 47 D1                     cmova rdx, r9
008B82A7  66 83 C1 04                     add cx, 4
008B82AB  66 C1 E1 02                     shl cx, 2
008B82AF  48 85 D2                        test rdx, rdx
008B82B2  74 0F                           je 0x1408b82c3
008B82B4  0F B7 C1                        movzx eax, cx
008B82B7  48 03 C2                        add rax, rdx
008B82BA  49 3B C0                        cmp rax, r8
008B82BD  0F 86 F7 03 00 00               jbe 0x1408b86ba
008B82C3  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
008B82CD  4D 3B F7                        cmp r14, r15
008B82D0  76 77                           jbe 0x1408b8349
008B82D2  41 0F B6 06                     movzx eax, byte ptr [r14]
008B82D6  24 0F                           and al, 0xf
008B82D8  3C 01                           cmp al, 1
008B82DA  75 6D                           jne 0x1408b8349
008B82DC  41 80 7E 01 0F                  cmp byte ptr [r14 + 1], 0xf
008B82E1  77 66                           ja 0x1408b8349
008B82E3  0F B6 2B                        movzx ebp, byte ptr [rbx]
008B82E6  40 80 FD 04                     cmp bpl, 4
008B82EA  77 5D                           ja 0x1408b8349
008B82EC  40 80 FD 02                     cmp bpl, 2
008B82F0  77 03                           ja 0x1408b82f5
008B82F2  40 B5 02                        mov bpl, 2
008B82F5  48 8B CB                        mov rcx, rbx
008B82F8  E8 A3 24 07 00                  call 0x14092a7a0
008B82FD  84 C0                           test al, al
008B82FF  74 48                           je 0x1408b8349
008B8301  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
008B8306  48 8D 53 08                     lea rdx, [rbx + 8]
008B830A  45 33 C9                        xor r9d, r9d
008B830D  41 8B C9                        mov ecx, r9d
008B8310  41 3B C8                        cmp ecx, r8d
008B8313  0F 82 E0 02 00 00               jb 0x1408b85f9
008B8319  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
008B831E  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B8323  4C 03 C3                        add r8, rbx
008B8326  49 3B D0                        cmp rdx, r8
008B8329  49 0F 47 D1                     cmova rdx, r9
008B832D  66 83 C1 04                     add cx, 4
008B8331  66 C1 E1 02                     shl cx, 2
008B8335  48 85 D2                        test rdx, rdx
008B8338  74 0F                           je 0x1408b8349
008B833A  0F B7 C1                        movzx eax, cx
008B833D  48 03 C2                        add rax, rdx
008B8340  49 3B C0                        cmp rax, r8
008B8343  0F 86 A4 03 00 00               jbe 0x1408b86ed
008B8349  4C 8B 35 18 17 72 00            mov r14, qword ptr [rip + 0x721718]
008B8350  4D 3B F7                        cmp r14, r15
008B8353  76 77                           jbe 0x1408b83cc
008B8355  41 0F B6 06                     movzx eax, byte ptr [r14]
008B8359  24 0F                           and al, 0xf
008B835B  3C 01                           cmp al, 1
008B835D  75 6D                           jne 0x1408b83cc
008B835F  41 80 7E 01 0F                  cmp byte ptr [r14 + 1], 0xf
008B8364  77 66                           ja 0x1408b83cc
008B8366  0F B6 2B                        movzx ebp, byte ptr [rbx]
008B8369  40 80 FD 04                     cmp bpl, 4
008B836D  77 5D                           ja 0x1408b83cc
008B836F  40 80 FD 02                     cmp bpl, 2
008B8373  77 03                           ja 0x1408b8378
008B8375  40 B5 02                        mov bpl, 2
008B8378  48 8B CB                        mov rcx, rbx
008B837B  E8 20 24 07 00                  call 0x14092a7a0
008B8380  84 C0                           test al, al
008B8382  74 48                           je 0x1408b83cc
008B8384  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
008B8389  48 8D 53 08                     lea rdx, [rbx + 8]
008B838D  45 33 C9                        xor r9d, r9d
008B8390  41 8B C9                        mov ecx, r9d
008B8393  41 3B C8                        cmp ecx, r8d
008B8396  0F 82 7B 02 00 00               jb 0x1408b8617
008B839C  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
008B83A1  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B83A6  4C 03 C3                        add r8, rbx
008B83A9  49 3B D0                        cmp rdx, r8
008B83AC  49 0F 47 D1                     cmova rdx, r9
008B83B0  66 83 C1 04                     add cx, 4
008B83B4  66 C1 E1 02                     shl cx, 2
008B83B8  48 85 D2                        test rdx, rdx
008B83BB  74 0F                           je 0x1408b83cc
008B83BD  0F B7 C1                        movzx eax, cx
008B83C0  48 03 C2                        add rax, rdx
008B83C3  49 3B C0                        cmp rax, r8
008B83C6  0F 86 54 03 00 00               jbe 0x1408b8720
008B83CC  4C 8B 35 85 F9 5A 00            mov r14, qword ptr [rip + 0x5af985]
008B83D3  4D 3B F7                        cmp r14, r15
008B83D6  0F 86 AF 00 00 00               jbe 0x1408b848b
008B83DC  41 0F B6 06                     movzx eax, byte ptr [r14]
008B83E0  24 0F                           and al, 0xf
008B83E2  3C 01                           cmp al, 1
008B83E4  0F 85 A1 00 00 00               jne 0x1408b848b
008B83EA  41 80 7E 01 0F                  cmp byte ptr [r14 + 1], 0xf
008B83EF  0F 87 96 00 00 00               ja 0x1408b848b
008B83F5  0F B6 2B                        movzx ebp, byte ptr [rbx]
008B83F8  40 80 FD 04                     cmp bpl, 4
008B83FC  0F 87 89 00 00 00               ja 0x1408b848b
008B8402  40 80 FD 02                     cmp bpl, 2
008B8406  77 03                           ja 0x1408b840b
008B8408  40 B5 02                        mov bpl, 2
008B840B  48 8B CB                        mov rcx, rbx
008B840E  E8 8D 23 07 00                  call 0x14092a7a0
008B8413  45 33 FF                        xor r15d, r15d
008B8416  84 C0                           test al, al
008B8418  74 74                           je 0x1408b848e
008B841A  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
008B841F  48 8D 53 08                     lea rdx, [rbx + 8]
008B8423  41 8B CF                        mov ecx, r15d
008B8426  41 3B C8                        cmp ecx, r8d
008B8429  0F 82 06 02 00 00               jb 0x1408b8635
008B842F  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
008B8434  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B8439  4C 03 C3                        add r8, rbx
008B843C  49 3B D0                        cmp rdx, r8
008B843F  49 0F 47 D7                     cmova rdx, r15
008B8443  66 83 C1 04                     add cx, 4
008B8447  66 C1 E1 02                     shl cx, 2
008B844B  48 85 D2                        test rdx, rdx
008B844E  74 3E                           je 0x1408b848e
008B8450  0F B7 C1                        movzx eax, cx
008B8453  48 03 C2                        add rax, rdx
008B8456  49 3B C0                        cmp rax, r8
008B8459  77 33                           ja 0x1408b848e
008B845B  66 89 4A 02                     mov word ptr [rdx + 2], cx
008B845F  4D 8B C6                        mov r8, r14
008B8462  66 44 89 3A                     mov word ptr [rdx], r15w
008B8466  C7 42 04 FF 01 0F 00            mov dword ptr [rdx + 4], 0xf01ff
008B846D  48 83 C2 08                     add rdx, 8
008B8471  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B8476  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B847D  E8 CE 15 0F 00                  call 0x1409a9a50
008B8482  66 FF 43 04                     inc word ptr [rbx + 4]
008B8486  40 88 2B                        mov byte ptr [rbx], bpl
008B8489  EB 03                           jmp 0x1408b848e
008B848B  45 33 FF                        xor r15d, r15d
008B848E  49 BE 01 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0001
008B8498  49 3B FE                        cmp rdi, r14
008B849B  72 71                           jb 0x1408b850e
008B849D  0F B6 07                        movzx eax, byte ptr [rdi]
008B84A0  24 0F                           and al, 0xf
008B84A2  3C 01                           cmp al, 1
008B84A4  75 68                           jne 0x1408b850e
008B84A6  80 7F 01 0F                     cmp byte ptr [rdi + 1], 0xf
008B84AA  77 62                           ja 0x1408b850e
008B84AC  0F B6 2B                        movzx ebp, byte ptr [rbx]
008B84AF  40 80 FD 04                     cmp bpl, 4
008B84B3  77 59                           ja 0x1408b850e
008B84B5  40 80 FD 02                     cmp bpl, 2
008B84B9  77 03                           ja 0x1408b84be
008B84BB  40 B5 02                        mov bpl, 2
008B84BE  48 8B CB                        mov rcx, rbx
008B84C1  E8 DA 22 07 00                  call 0x14092a7a0
008B84C6  84 C0                           test al, al
008B84C8  74 44                           je 0x1408b850e
008B84CA  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
008B84CF  48 8D 53 08                     lea rdx, [rbx + 8]
008B84D3  41 8B CF                        mov ecx, r15d
008B84D6  41 3B C8                        cmp ecx, r8d
008B84D9  0F 82 74 01 00 00               jb 0x1408b8653
008B84DF  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
008B84E4  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
008B84E8  4C 03 C3                        add r8, rbx
008B84EB  49 3B D0                        cmp rdx, r8
008B84EE  49 0F 47 D7                     cmova rdx, r15
008B84F2  66 83 C1 04                     add cx, 4
008B84F6  66 C1 E1 02                     shl cx, 2
008B84FA  48 85 D2                        test rdx, rdx
008B84FD  74 0F                           je 0x1408b850e
008B84FF  0F B7 C1                        movzx eax, cx
008B8502  48 03 C2                        add rax, rdx
008B8505  49 3B C0                        cmp rax, r8
008B8508  0F 86 45 02 00 00               jbe 0x1408b8753
008B850E  49 3B F6                        cmp rsi, r14
008B8511  72 71                           jb 0x1408b8584
008B8513  0F B6 06                        movzx eax, byte ptr [rsi]
008B8516  24 0F                           and al, 0xf
008B8518  3C 01                           cmp al, 1
008B851A  75 68                           jne 0x1408b8584
008B851C  80 7E 01 0F                     cmp byte ptr [rsi + 1], 0xf
008B8520  77 62                           ja 0x1408b8584
008B8522  0F B6 3B                        movzx edi, byte ptr [rbx]
008B8525  40 80 FF 04                     cmp dil, 4
008B8529  77 59                           ja 0x1408b8584
008B852B  40 80 FF 02                     cmp dil, 2
008B852F  77 03                           ja 0x1408b8534
008B8531  40 B7 02                        mov dil, 2
008B8534  48 8B CB                        mov rcx, rbx
008B8537  E8 64 22 07 00                  call 0x14092a7a0
008B853C  84 C0                           test al, al
008B853E  74 44                           je 0x1408b8584
008B8540  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
008B8545  48 8D 53 08                     lea rdx, [rbx + 8]
008B8549  41 8B CF                        mov ecx, r15d
008B854C  41 3B C8                        cmp ecx, r8d
008B854F  0F 82 1C 01 00 00               jb 0x1408b8671
008B8555  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
008B855A  0F B6 4E 01                     movzx ecx, byte ptr [rsi + 1]
008B855E  4C 03 C3                        add r8, rbx
008B8561  49 3B D0                        cmp rdx, r8
008B8564  49 0F 47 D7                     cmova rdx, r15
008B8568  66 83 C1 04                     add cx, 4
008B856C  66 C1 E1 02                     shl cx, 2
008B8570  48 85 D2                        test rdx, rdx
008B8573  74 0F                           je 0x1408b8584
008B8575  0F B7 C1                        movzx eax, cx
008B8578  48 03 C2                        add rax, rdx
008B857B  49 3B C0                        cmp rax, r8
008B857E  0F 86 02 02 00 00               jbe 0x1408b8786
008B8584  49 83 BC 24 A0 00 00 00 00      cmp qword ptr [r12 + 0xa0], 0
008B858D  0F 85 FC 00 00 00               jne 0x1408b868f
008B8593  49 83 BD A0 00 00 00 00         cmp qword ptr [r13 + 0xa0], 0
008B859B  0F 85 EE 00 00 00               jne 0x1408b868f
008B85A1  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008B85A6  48 89 18                        mov qword ptr [rax], rbx
008B85A9  33 C0                           xor eax, eax
008B85AB  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008B85B0  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
008B85B5  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
008B85BA  48 83 C4 30                     add rsp, 0x30
008B85BE  41 5F                           pop r15
008B85C0  41 5E                           pop r14
008B85C2  41 5D                           pop r13
008B85C4  41 5C                           pop r12
008B85C6  5F                              pop rdi
008B85C7  C3                              ret
008B85C8  CC                              int3
008B85C9  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008B85CE  45 33 C9                        xor r9d, r9d
008B85D1  4C 89 08                        mov qword ptr [rax], r9
008B85D4  B8 9A 00 00 C0                  mov eax, 0xc000009a
008B85D9  EB D0                           jmp 0x1408b85ab
008B85DB  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B85DF  48 03 C3                        add rax, rbx
008B85E2  48 3B D0                        cmp rdx, rax
008B85E5  0F 83 D8 FC FF FF               jae 0x1408b82c3
008B85EB  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008B85EF  FF C1                           inc ecx
008B85F1  48 03 D0                        add rdx, rax
008B85F4  E9 91 FC FF FF                  jmp 0x1408b828a
008B85F9  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B85FD  48 03 C3                        add rax, rbx
008B8600  48 3B D0                        cmp rdx, rax
008B8603  0F 83 40 FD FF FF               jae 0x1408b8349
008B8609  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008B860D  FF C1                           inc ecx
008B860F  48 03 D0                        add rdx, rax
008B8612  E9 F9 FC FF FF                  jmp 0x1408b8310
008B8617  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B861B  48 03 C3                        add rax, rbx
008B861E  48 3B D0                        cmp rdx, rax
008B8621  0F 83 A5 FD FF FF               jae 0x1408b83cc
008B8627  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008B862B  FF C1                           inc ecx
008B862D  48 03 D0                        add rdx, rax
008B8630  E9 5E FD FF FF                  jmp 0x1408b8393
008B8635  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B8639  48 03 C3                        add rax, rbx
008B863C  48 3B D0                        cmp rdx, rax
008B863F  0F 83 49 FE FF FF               jae 0x1408b848e
008B8645  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008B8649  FF C1                           inc ecx
008B864B  48 03 D0                        add rdx, rax
008B864E  E9 D3 FD FF FF                  jmp 0x1408b8426
008B8653  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B8657  48 03 C3                        add rax, rbx
008B865A  48 3B D0                        cmp rdx, rax
008B865D  0F 83 AB FE FF FF               jae 0x1408b850e
008B8663  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008B8667  FF C1                           inc ecx
008B8669  48 03 D0                        add rdx, rax
008B866C  E9 65 FE FF FF                  jmp 0x1408b84d6
008B8671  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B8675  48 03 C3                        add rax, rbx
008B8678  48 3B D0                        cmp rdx, rax
008B867B  0F 83 03 FF FF FF               jae 0x1408b8584
008B8681  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
008B8685  FF C1                           inc ecx
008B8687  48 03 D0                        add rdx, rax
008B868A  E9 BD FE FF FF                  jmp 0x1408b854c
008B868F  48 8B 05 7A 14 72 00            mov rax, qword ptr [rip + 0x72147a]
008B8696  45 33 C0                        xor r8d, r8d
008B8699  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
008B869E  41 B9 FF 01 0F 00               mov r9d, 0xf01ff
008B86A4  48 8B CB                        mov rcx, rbx
008B86A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B86AC  41 8D 50 02                     lea edx, [r8 + 2]
008B86B0  E8 6B 13 07 00                  call 0x140929a20
008B86B5  E9 E7 FE FF FF                  jmp 0x1408b85a1
008B86BA  66 89 4A 02                     mov word ptr [rdx + 2], cx
008B86BE  4D 8B C7                        mov r8, r15
008B86C1  66 44 89 0A                     mov word ptr [rdx], r9w
008B86C5  C7 42 04 FF 01 0F 00            mov dword ptr [rdx + 4], 0xf01ff
008B86CC  48 83 C2 08                     add rdx, 8
008B86D0  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
008B86D5  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B86DC  E8 6F 13 0F 00                  call 0x1409a9a50
008B86E1  66 FF 43 04                     inc word ptr [rbx + 4]
008B86E5  40 88 2B                        mov byte ptr [rbx], bpl
008B86E8  E9 D6 FB FF FF                  jmp 0x1408b82c3
008B86ED  66 89 4A 02                     mov word ptr [rdx + 2], cx
008B86F1  4D 8B C6                        mov r8, r14
008B86F4  66 44 89 0A                     mov word ptr [rdx], r9w
008B86F8  C7 42 04 FF 01 0F 00            mov dword ptr [rdx + 4], 0xf01ff
008B86FF  48 83 C2 08                     add rdx, 8
008B8703  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B8708  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B870F  E8 3C 13 0F 00                  call 0x1409a9a50
008B8714  66 FF 43 04                     inc word ptr [rbx + 4]
008B8718  40 88 2B                        mov byte ptr [rbx], bpl
008B871B  E9 29 FC FF FF                  jmp 0x1408b8349
008B8720  66 89 4A 02                     mov word ptr [rdx + 2], cx
008B8724  4D 8B C6                        mov r8, r14
008B8727  66 44 89 0A                     mov word ptr [rdx], r9w
008B872B  C7 42 04 FF 01 0F 00            mov dword ptr [rdx + 4], 0xf01ff
008B8732  48 83 C2 08                     add rdx, 8
008B8736  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B873B  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B8742  E8 09 13 0F 00                  call 0x1409a9a50
008B8747  66 FF 43 04                     inc word ptr [rbx + 4]
008B874B  40 88 2B                        mov byte ptr [rbx], bpl
008B874E  E9 79 FC FF FF                  jmp 0x1408b83cc
008B8753  66 89 4A 02                     mov word ptr [rdx + 2], cx
008B8757  4C 8B C7                        mov r8, rdi
008B875A  66 C7 02 00 00                  mov word ptr [rdx], 0
008B875F  C7 42 04 FF 01 0F 00            mov dword ptr [rdx + 4], 0xf01ff
008B8766  48 83 C2 08                     add rdx, 8
008B876A  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
008B876E  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B8775  E8 D6 12 0F 00                  call 0x1409a9a50
008B877A  66 FF 43 04                     inc word ptr [rbx + 4]
008B877E  40 88 2B                        mov byte ptr [rbx], bpl
008B8781  E9 88 FD FF FF                  jmp 0x1408b850e
008B8786  66 89 4A 02                     mov word ptr [rdx + 2], cx
008B878A  4C 8B C6                        mov r8, rsi
008B878D  66 C7 02 00 00                  mov word ptr [rdx], 0
008B8792  C7 42 04 FF 01 0F 00            mov dword ptr [rdx + 4], 0xf01ff
008B8799  48 83 C2 08                     add rdx, 8
008B879D  0F B6 4E 01                     movzx ecx, byte ptr [rsi + 1]
008B87A1  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B87A8  E8 A3 12 0F 00                  call 0x1409a9a50
008B87AD  66 FF 43 04                     inc word ptr [rbx + 4]
008B87B1  40 88 3B                        mov byte ptr [rbx], dil
008B87B4  E9 CB FD FF FF                  jmp 0x1408b8584
008B87B9  48 85 FF                        test rdi, rdi
008B87BC  75 10                           jne 0x1408b87ce
008B87BE  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
008B87C2  8D 6C 85 00                     lea ebp, [rbp + rax*4]
008B87C6  83 C5 10                        add ebp, 0x10
008B87C9  E9 2C FA FF FF                  jmp 0x1408b81fa
008B87CE  48 8B D7                        mov rdx, rdi
008B87D1  48 8B CE                        mov rcx, rsi
008B87D4  E8 F7 82 B4 FF                  call 0x140400ad0
008B87D9  84 C0                           test al, al
008B87DB  74 E1                           je 0x1408b87be
008B87DD  48 8B F3                        mov rsi, rbx
008B87E0  E9 15 FA FF FF                  jmp 0x1408b81fa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepCreateImpersonationTokenDacl(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p20 = v_rsi;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    v_rbx = 0;
    v_rsi = 0;
    if (((*(unsigned int *)(a2 + 200)) & (0x4000ULL)) != 0) {
        v_rsi = *(unsigned __int64 *)(a2 + 784);
    }
    v_rdi = 0;
    if (((*(unsigned int *)(a1 + 200)) & (0x4000ULL)) != 0) {
        v_rdi = *(unsigned __int64 *)(a1 + 784);
    }
    a2 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7477602) + 1)) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7477423) + 1))));
    a2 = (unsigned int)((a2) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962644) + 1))));
    a2 = (unsigned int)((a2) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1))));
    a2 = (unsigned int)((a2) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)) + 1))));
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)) + 1);
    v_rbp = a2 * 4 + 88;
    if (v_rdi != 0) {
        result = *(unsigned __int8 *)(v_rdi + 1);
        v_rbp = a2 * 4 + 88 + result * 4;
        v_rbp = (unsigned int)((v_rbp) + (16));
    }
    if (v_rsi != 0) goto loc_008B87B9;
loc_008B81FA:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B85C9;
    result = v_rbp - 8;
    if (((unsigned int)(v_rbp - 8)) <= 0xFFF4ULL) {
        a3 = (unsigned int)(v_rbp);
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, a4);
        result = 0;
        *(unsigned __int16 *)(result) = 2;
        *(unsigned int *)(result + 4) = 0;
        *(unsigned __int16 *)(result + 2) = (unsigned __int16)(v_rbp);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152))) <= 0) goto loc_008B82C3;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B82C3;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)) + 1)) > 15) goto loc_008B82C3;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 4) goto loc_008B82C3;
    v_rbp = *(unsigned __int8 *)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) <= 2) {
        v_rbp = 2;
    }
    result = RtlValidAcl(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008B82C3;
    a4 = 0;
loc_008B828A:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B85DB;
    a3 = (*(unsigned __int16 *)(result + 2)) + (result);
    a2 = result + 8;
    if ((result + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)) + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_008B82C3;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result <= a3) goto loc_008B86BA;
loc_008B82C3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152))) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)))) goto loc_008B8349;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B8349;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1)) > 15) goto loc_008B8349;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 4) goto loc_008B8349;
    v_rbp = *(unsigned __int8 *)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) <= 2) {
        v_rbp = 2;
    }
    result = RtlValidAcl(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008B8349;
    a4 = 0;
loc_008B8310:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B85F9;
    a3 = (*(unsigned __int16 *)(result + 2)) + (result);
    a2 = result + 8;
    if ((result + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_008B8349;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result <= a3) goto loc_008B86ED;
loc_008B8349:
    if ((*(unsigned __int64 *)(v_rip + 7477016)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)))) goto loc_008B83CC;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7477016))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B83CC;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7477016) + 1)) > 15) goto loc_008B83CC;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 4) goto loc_008B83CC;
    v_rbp = *(unsigned __int8 *)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) <= 2) {
        v_rbp = 2;
    }
    result = RtlValidAcl(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008B83CC;
    a4 = 0;
loc_008B8393:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B8617;
    a3 = (*(unsigned __int16 *)(result + 2)) + (result);
    a2 = result + 8;
    if ((result + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7477016) + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_008B83CC;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result <= a3) goto loc_008B8720;
loc_008B83CC:
    if ((*(unsigned __int64 *)(v_rip + 5962117)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152)))) goto loc_008B848B;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B848B;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1)) > 15) goto loc_008B848B;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 4) goto loc_008B848B;
    v_rbp = *(unsigned __int8 *)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) <= 2) {
        v_rbp = 2;
    }
    result = RtlValidAcl(result, a2, a3, a4);
    v_r15 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_008B848E;
loc_008B8426:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B8635;
    a3 = (*(unsigned __int16 *)(result + 2)) + (result);
    a2 = result + 8;
    if ((result + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_008B848E;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result > a3) goto loc_008B848E;
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(a2) = 0;
    *(unsigned int *)(a2 + 4) = 0xF01FFULL;
    a2 = (a2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1) * 4 + 8, a2, *(unsigned __int64 *)(v_rip + 5962117), a4);
    *(unsigned __int8 *)(result) = (unsigned __int8)(v_rbp);
    goto loc_008B848E;
loc_008B848B:
    v_r15 = 0;
loc_008B848E:
    if (v_rdi < (*(unsigned __int64 *)(v_rip + 5962117))) goto loc_008B850E;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B850E;
    if ((*(unsigned __int8 *)(v_rdi + 1)) > 15) goto loc_008B850E;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 4) goto loc_008B850E;
    v_rbp = *(unsigned __int8 *)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) <= 2) {
        v_rbp = 2;
    }
    result = RtlValidAcl(result, a2, *(unsigned __int64 *)(v_rip + 5962117), a4);
    if ((unsigned __int8)(result) == 0) goto loc_008B850E;
loc_008B84D6:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B8653;
    a3 = (*(unsigned __int16 *)(result + 2)) + (result);
    a2 = result + 8;
    if ((result + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(v_rdi + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_008B850E;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result <= a3) goto loc_008B8753;
loc_008B850E:
    if (v_rsi < (*(unsigned __int64 *)(v_rip + 5962117))) goto loc_008B8584;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rsi)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B8584;
    if ((*(unsigned __int8 *)(v_rsi + 1)) > 15) goto loc_008B8584;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 4) goto loc_008B8584;
    v_rdi = *(unsigned __int8 *)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) <= 2) {
        v_rdi = 2;
    }
    result = RtlValidAcl(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008B8584;
loc_008B854C:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B8671;
    a3 = (*(unsigned __int16 *)(result + 2)) + (result);
    a2 = result + 8;
    if ((result + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(v_rsi + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_008B8584;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result <= a3) goto loc_008B8786;
loc_008B8584:
    if ((*(unsigned __int64 *)(a2 + 160)) != 0) goto loc_008B868F;
    if ((*(unsigned __int64 *)(a1 + 160)) != 0) goto loc_008B868F;
loc_008B85A1:
    *(unsigned __int64 *)(v_stack_p18) = result;
    result = 0;
loc_008B85AB:
    v_rsp = (v_rsp) + (48);
    return result;
loc_008B85C9:
    a4 = 0;
    *(unsigned __int64 *)(v_stack_p70) = 0;
    goto loc_008B85AB;
loc_008B85DB:
    result = (*(unsigned __int16 *)(v_stack_p8 + 2)) + (v_stack_p8);
    if (a2 >= result) goto loc_008B82C3;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_008B828A;
loc_008B85F9:
    result = (*(unsigned __int16 *)(v_stack_p8 + 2)) + (v_stack_p8);
    if (a2 >= result) goto loc_008B8349;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_008B8310;
loc_008B8617:
    result = (*(unsigned __int16 *)(v_stack_p8 + 2)) + (v_stack_p8);
    if (a2 >= result) goto loc_008B83CC;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_008B8393;
loc_008B8635:
    result = (*(unsigned __int16 *)(v_stack_p8 + 2)) + (v_stack_p8);
    if (a2 >= result) goto loc_008B848E;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_008B8426;
loc_008B8653:
    result = (*(unsigned __int16 *)(v_stack_p8 + 2)) + (v_stack_p8);
    if (a2 >= result) goto loc_008B850E;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_008B84D6;
loc_008B8671:
    result = (*(unsigned __int16 *)(v_stack_p8 + 2)) + (v_stack_p8);
    if (a2 >= result) goto loc_008B8584;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_008B854C;
loc_008B868F:
    a3 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(v_rip + 7476346);
    result = RtlpAddKnownAce(v_stack_p8, a3 + 2, a3, (unsigned int)(0xF01FFULL));
    goto loc_008B85A1;
loc_008B86BA:
    *(unsigned __int16 *)(a3 + 2 + 2) = (unsigned __int16)(v_stack_p8);
    *(unsigned __int16 *)(a3 + 2) = (unsigned __int16)((unsigned int)(0xF01FFULL));
    *(unsigned int *)(a3 + 2 + 4) = 0xF01FFULL;
    a2 = (a3 + 2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(v_r15 + 1) * 4 + 8, a2, 0, (unsigned int)(0xF01FFULL));
    *(unsigned __int8 *)(v_stack_p8) = (unsigned __int8)(v_stack_p10);
    goto loc_008B82C3;
loc_008B86ED:
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(*(unsigned __int8 *)(v_r15 + 1) * 4 + 8);
    *(unsigned __int16 *)(a2) = (unsigned __int16)((unsigned int)(0xF01FFULL));
    *(unsigned int *)(a2 + 4) = 0xF01FFULL;
    a2 = (a2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1) * 4 + 8, a2, *(unsigned __int64 *)(v_rip + 5962117), (unsigned int)(0xF01FFULL));
    *(unsigned __int8 *)(v_stack_p8) = (unsigned __int8)(v_stack_p10);
    goto loc_008B8349;
loc_008B8720:
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1) * 4 + 8);
    *(unsigned __int16 *)(a2) = (unsigned __int16)((unsigned int)(0xF01FFULL));
    *(unsigned int *)(a2 + 4) = 0xF01FFULL;
    a2 = (a2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1) * 4 + 8, a2, *(unsigned __int64 *)(v_rip + 5962117), (unsigned int)(0xF01FFULL));
    *(unsigned __int8 *)(v_stack_p8) = (unsigned __int8)(v_stack_p10);
    goto loc_008B83CC;
loc_008B8753:
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5962117) + 1) * 4 + 8);
    *(unsigned __int16 *)(a2) = 0;
    *(unsigned int *)(a2 + 4) = 0xF01FFULL;
    a2 = (a2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(v_rdi + 1) * 4 + 8, a2, v_rdi, (unsigned int)(0xF01FFULL));
    *(unsigned __int8 *)(v_stack_p8) = (unsigned __int8)(v_stack_p10);
    goto loc_008B850E;
loc_008B8786:
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(*(unsigned __int8 *)(v_rdi + 1) * 4 + 8);
    *(unsigned __int16 *)(a2) = 0;
    *(unsigned int *)(a2 + 4) = 0xF01FFULL;
    a2 = (a2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(v_stack_p20 + 1) * 4 + 8, a2, v_stack_p20, (unsigned int)(0xF01FFULL));
    *(unsigned __int8 *)(v_stack_p8) = (unsigned __int8)(v_rdi);
    goto loc_008B8584;
loc_008B87B9:
    if (v_rdi != 0) goto loc_008B87CE;
loc_008B87BE:
    v_rbp = (unsigned int)((v_stack_p10 + *(unsigned __int8 *)(v_stack_p20 + 1) * 4) + (16));
    goto loc_008B81FA;
loc_008B87CE:
    result = RtlEqualSid(v_stack_p20, v_rdi, v_stack_p20, (unsigned int)(0xF01FFULL));
    if ((unsigned __int8)(result) == 0) goto loc_008B87BE;
    goto loc_008B81FA;
}
```

## 5. (Beta) C Style

```c
int64_t SepCreateImpersonationTokenDacl(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p20 = local_rsi;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    local_rbx = 0;
    local_rsi = 0;
    if (((*(uint32_t *)(arg2 + 0xC8)) & (0x4000ULL)) != 0) {
        local_rsi = *(uint64_t *)(arg2 + 0x310);
    }
    local_rdi = 0;
    if (((*(uint32_t *)(arg1 + 0xC8)) & (0x4000ULL)) != 0) {
        local_rdi = *(uint64_t *)(arg1 + 0x310);
    }
    Arg2 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x721962) + 0x1)) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x7218AF) + 0x1))));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AFB94) + 0x1))));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1))));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)) + 0x1))));
    result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)) + 0x1);
    local_rbp = Arg2 * 4 + 88;
    if (local_rdi != 0) {
        result = *(uint8_t *)(local_rdi + 0x1);
        local_rbp = Arg2 * 4 + 88 + result * 4;
        local_rbp = (uint32_t)((local_rbp) + (16));
    }
    if (local_rsi != 0) goto loc_008B87B9;
loc_008B81FA:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0x20206553ULL), Arg4);
    if (result == 0) goto loc_008B85C9;
    result = local_rbp - 8;
    if (((uint32_t)(local_rbp - 8)) <= 0xFFF4ULL) {
        Arg3 = (uint32_t)(local_rbp);
        Arg2 = 0;
        Arg1 = result;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        result = 0;
        *(uint16_t *)(result) = 2;
        *(uint32_t *)(result + 0x4) = 0;
        *(uint16_t *)(result + 0x2) = (uint16_t)(local_rbp);
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x98))) <= 0) goto loc_008B82C3;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B82C3;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)) + 0x1)) > 15) goto loc_008B82C3;
    if (((uint8_t)(*(uint8_t *)(result))) > 4) goto loc_008B82C3;
    local_rbp = *(uint8_t *)(result);
    if (((uint8_t)(*(uint8_t *)(result))) <= 2) {
        local_rbp = 2;
    }
    result = RtlValidAcl(result, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008B82C3;
    Arg4 = 0;
loc_008B828A:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B85DB;
    Arg3 = (*(uint16_t *)(result + 0x2)) + (result);
    Arg2 = result + 8;
    if ((result + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)) + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == NULL) goto loc_008B82C3;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result <= Arg3) goto loc_008B86BA;
loc_008B82C3:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x98))) <= (*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)))) goto loc_008B8349;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B8349;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1)) > 15) goto loc_008B8349;
    if (((uint8_t)(*(uint8_t *)(result))) > 4) goto loc_008B8349;
    local_rbp = *(uint8_t *)(result);
    if (((uint8_t)(*(uint8_t *)(result))) <= 2) {
        local_rbp = 2;
    }
    result = RtlValidAcl(result, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008B8349;
    Arg4 = 0;
loc_008B8310:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B85F9;
    Arg3 = (*(uint16_t *)(result + 0x2)) + (result);
    Arg2 = result + 8;
    if ((result + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == NULL) goto loc_008B8349;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result <= Arg3) goto loc_008B86ED;
loc_008B8349:
    if ((*(uint64_t *)(v_rip + 0x721718)) <= (*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)))) goto loc_008B83CC;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x721718))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B83CC;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x721718) + 0x1)) > 15) goto loc_008B83CC;
    if (((uint8_t)(*(uint8_t *)(result))) > 4) goto loc_008B83CC;
    local_rbp = *(uint8_t *)(result);
    if (((uint8_t)(*(uint8_t *)(result))) <= 2) {
        local_rbp = 2;
    }
    result = RtlValidAcl(result, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008B83CC;
    Arg4 = 0;
loc_008B8393:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B8617;
    Arg3 = (*(uint16_t *)(result + 0x2)) + (result);
    Arg2 = result + 8;
    if ((result + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x721718) + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == NULL) goto loc_008B83CC;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result <= Arg3) goto loc_008B8720;
loc_008B83CC:
    if ((*(uint64_t *)(v_rip + 0x5AF985)) <= (*(uint64_t *)(*(uint64_t *)(arg2 + 0x98)))) goto loc_008B848B;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B848B;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1)) > 15) goto loc_008B848B;
    if (((uint8_t)(*(uint8_t *)(result))) > 4) goto loc_008B848B;
    local_rbp = *(uint8_t *)(result);
    if (((uint8_t)(*(uint8_t *)(result))) <= 2) {
        local_rbp = 2;
    }
    result = RtlValidAcl(result, Arg2, Arg3, Arg4);
    local_r15 = 0;
    if ((uint8_t)(result) == 0) goto loc_008B848E;
loc_008B8426:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B8635;
    Arg3 = (*(uint16_t *)(result + 0x2)) + (result);
    Arg2 = result + 8;
    if ((result + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == NULL) goto loc_008B848E;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result > Arg3) goto loc_008B848E;
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(Arg1);
    *(uint16_t *)(arg2) = 0;
    *(uint32_t *)(arg2 + 0x4) = 0xF01FFULL;
    Arg2 = (Arg2) + (8);
    result = RtlCopySid(*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1) * 4 + 8, Arg2, *(uint64_t *)(v_rip + 0x5AF985), Arg4);
    *(uint8_t *)(result) = (uint8_t)(local_rbp);
    goto loc_008B848E;
loc_008B848B:
    local_r15 = 0;
loc_008B848E:
    if (local_rdi < (*(uint64_t *)(v_rip + 0x5AF985))) goto loc_008B850E;
    result = (uint8_t)((*(uint8_t *)(local_rdi)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B850E;
    if ((*(uint8_t *)(local_rdi + 0x1)) > 15) goto loc_008B850E;
    if (((uint8_t)(*(uint8_t *)(result))) > 4) goto loc_008B850E;
    local_rbp = *(uint8_t *)(result);
    if (((uint8_t)(*(uint8_t *)(result))) <= 2) {
        local_rbp = 2;
    }
    result = RtlValidAcl(result, Arg2, *(uint64_t *)(v_rip + 0x5AF985), Arg4);
    if ((uint8_t)(result) == 0) goto loc_008B850E;
loc_008B84D6:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B8653;
    Arg3 = (*(uint16_t *)(result + 0x2)) + (result);
    Arg2 = result + 8;
    if ((result + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(local_rdi + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == NULL) goto loc_008B850E;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result <= Arg3) goto loc_008B8753;
loc_008B850E:
    if (local_rsi < (*(uint64_t *)(v_rip + 0x5AF985))) goto loc_008B8584;
    result = (uint8_t)((*(uint8_t *)(local_rsi)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B8584;
    if ((*(uint8_t *)(local_rsi + 0x1)) > 15) goto loc_008B8584;
    if (((uint8_t)(*(uint8_t *)(result))) > 4) goto loc_008B8584;
    local_rdi = *(uint8_t *)(result);
    if (((uint8_t)(*(uint8_t *)(result))) <= 2) {
        local_rdi = 2;
    }
    result = RtlValidAcl(result, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008B8584;
loc_008B854C:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B8671;
    Arg3 = (*(uint16_t *)(result + 0x2)) + (result);
    Arg2 = result + 8;
    if ((result + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(local_rsi + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == NULL) goto loc_008B8584;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result <= Arg3) goto loc_008B8786;
loc_008B8584:
    if ((*(uint64_t *)(arg2 + 0xA0)) != 0) goto loc_008B868F;
    if ((*(uint64_t *)(arg1 + 0xA0)) != 0) goto loc_008B868F;
loc_008B85A1:
    *(uint64_t *)(v_stack_p18) = result;
    result = 0;
loc_008B85AB:
    local_rsp = (local_rsp) + (48);
    return result;
loc_008B85C9:
    Arg4 = 0;
    *(uint64_t *)(v_stack_p70) = 0;
    goto loc_008B85AB;
loc_008B85DB:
    result = (*(uint16_t *)(v_stack_p8 + 0x2)) + (v_stack_p8);
    if (Arg2 >= result) goto loc_008B82C3;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(arg2 + 0x2));
    goto loc_008B828A;
loc_008B85F9:
    result = (*(uint16_t *)(v_stack_p8 + 0x2)) + (v_stack_p8);
    if (Arg2 >= result) goto loc_008B8349;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(arg2 + 0x2));
    goto loc_008B8310;
loc_008B8617:
    result = (*(uint16_t *)(v_stack_p8 + 0x2)) + (v_stack_p8);
    if (Arg2 >= result) goto loc_008B83CC;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(arg2 + 0x2));
    goto loc_008B8393;
loc_008B8635:
    result = (*(uint16_t *)(v_stack_p8 + 0x2)) + (v_stack_p8);
    if (Arg2 >= result) goto loc_008B848E;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(arg2 + 0x2));
    goto loc_008B8426;
loc_008B8653:
    result = (*(uint16_t *)(v_stack_p8 + 0x2)) + (v_stack_p8);
    if (Arg2 >= result) goto loc_008B850E;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(arg2 + 0x2));
    goto loc_008B84D6;
loc_008B8671:
    result = (*(uint16_t *)(v_stack_p8 + 0x2)) + (v_stack_p8);
    if (Arg2 >= result) goto loc_008B8584;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(arg2 + 0x2));
    goto loc_008B854C;
loc_008B868F:
    Arg3 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(v_rip + 0x72147A);
    result = RtlpAddKnownAce(v_stack_p8, Arg3 + 2, Arg3, (uint32_t)(0xF01FFULL));
    goto loc_008B85A1;
loc_008B86BA:
    *(uint16_t *)(Arg3 + 0x2 + 0x2) = (uint16_t)(v_stack_p8);
    *(uint16_t *)(Arg3 + 0x2) = (uint16_t)((uint32_t)(0xF01FFULL));
    *(uint32_t *)(Arg3 + 0x2 + 0x4) = 0xF01FFULL;
    Arg2 = (Arg3 + 2) + (8);
    result = RtlCopySid(*(uint8_t *)(local_r15 + 0x1) * 4 + 8, Arg2, 0, (uint32_t)(0xF01FFULL));
    *(uint8_t *)(v_stack_p8) = (uint8_t)(v_stack_p10);
    goto loc_008B82C3;
loc_008B86ED:
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(*(uint8_t *)(local_r15 + 0x1) * 4 + 8);
    *(uint16_t *)(arg2) = (uint16_t)((uint32_t)(0xF01FFULL));
    *(uint32_t *)(arg2 + 0x4) = 0xF01FFULL;
    Arg2 = (Arg2) + (8);
    result = RtlCopySid(*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1) * 4 + 8, Arg2, *(uint64_t *)(v_rip + 0x5AF985), (uint32_t)(0xF01FFULL));
    *(uint8_t *)(v_stack_p8) = (uint8_t)(v_stack_p10);
    goto loc_008B8349;
loc_008B8720:
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1) * 4 + 8);
    *(uint16_t *)(arg2) = (uint16_t)((uint32_t)(0xF01FFULL));
    *(uint32_t *)(arg2 + 0x4) = 0xF01FFULL;
    Arg2 = (Arg2) + (8);
    result = RtlCopySid(*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1) * 4 + 8, Arg2, *(uint64_t *)(v_rip + 0x5AF985), (uint32_t)(0xF01FFULL));
    *(uint8_t *)(v_stack_p8) = (uint8_t)(v_stack_p10);
    goto loc_008B83CC;
loc_008B8753:
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x5AF985) + 0x1) * 4 + 8);
    *(uint16_t *)(arg2) = 0;
    *(uint32_t *)(arg2 + 0x4) = 0xF01FFULL;
    Arg2 = (Arg2) + (8);
    result = RtlCopySid(*(uint8_t *)(local_rdi + 0x1) * 4 + 8, Arg2, local_rdi, (uint32_t)(0xF01FFULL));
    *(uint8_t *)(v_stack_p8) = (uint8_t)(v_stack_p10);
    goto loc_008B850E;
loc_008B8786:
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(*(uint8_t *)(local_rdi + 0x1) * 4 + 8);
    *(uint16_t *)(arg2) = 0;
    *(uint32_t *)(arg2 + 0x4) = 0xF01FFULL;
    Arg2 = (Arg2) + (8);
    result = RtlCopySid(*(uint8_t *)(v_stack_p20 + 0x1) * 4 + 8, Arg2, v_stack_p20, (uint32_t)(0xF01FFULL));
    *(uint8_t *)(v_stack_p8) = (uint8_t)(local_rdi);
    goto loc_008B8584;
loc_008B87B9:
    if (local_rdi != 0) goto loc_008B87CE;
loc_008B87BE:
    local_rbp = (uint32_t)((v_stack_p10 + *(uint8_t *)(v_stack_p20 + 0x1) * 4) + (16));
    goto loc_008B81FA;
loc_008B87CE:
    result = RtlEqualSid(v_stack_p20, local_rdi, v_stack_p20, (uint32_t)(0xF01FFULL));
    if ((uint8_t)(result) == 0) goto loc_008B87BE;
    goto loc_008B81FA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0x310` | `64` | `R` |
| `Arg2` | `+ 0x98` | `64` | `R` |
| `Arg2` | `+ 0xA0` | `64` | `R` |
| `Arg2` | `+ 0xC8` | `32` | `R` |
| `Arg2` | `+ 0x310` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B8140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
