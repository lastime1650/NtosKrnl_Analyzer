# sub_006FF210

- RVA: `0x006FF210`–`0x006FF5D8` (길이 `968` bytes)
- VA: `0x00000001406FF210`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060300`
- 디코드: `287`개 명령, `968/968` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006FF301` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006FF32B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006FF396` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006FF516` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006FF5B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A8B3`

### Static image references
- `0x006FF318` → RVA `0x00FD8430` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x006FF301` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x006FF32B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x006FF396` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x006FF516` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x006FF5B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006FF210  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006FF215  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
006FF21A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
006FF21F  57                              push rdi
006FF220  41 56                           push r14
006FF222  41 57                           push r15
006FF224  48 83 EC 20                     sub rsp, 0x20
006FF228  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
006FF22C  49 8B F9                        mov rdi, r9
006FF22F  48 8B F2                        mov rsi, rdx
006FF232  4C 8B C9                        mov r9, rcx
006FF235  4D 85 C0                        test r8, r8
006FF238  74 52                           je 0x1406ff28c
006FF23A  83 39 03                        cmp dword ptr [rcx], 3
006FF23D  76 4D                           jbe 0x1406ff28c
006FF23F  49 8B C0                        mov rax, r8
006FF242  33 D2                           xor edx, edx
006FF244  44 8B 10                        mov r10d, dword ptr [rax]
006FF247  48 8D 48 04                     lea rcx, [rax + 4]
006FF24B  83 FA 03                        cmp edx, 3
006FF24E  73 1A                           jae 0x1406ff26a
006FF250  48 3B C8                        cmp rcx, rax
006FF253  0F 82 5E 03 00 00               jb 0x1406ff5b7
006FF259  4A 8D 04 11                     lea rax, [rcx + r10]
006FF25D  48 3B C1                        cmp rax, rcx
006FF260  0F 82 51 03 00 00               jb 0x1406ff5b7
006FF266  FF C2                           inc edx
006FF268  EB DA                           jmp 0x1406ff244
006FF26A  48 3B C8                        cmp rcx, rax
006FF26D  0F 82 44 03 00 00               jb 0x1406ff5b7
006FF273  33 ED                           xor ebp, ebp
006FF275  45 85 D2                        test r10d, r10d
006FF278  48 0F 45 E9                     cmovne rbp, rcx
006FF27C  41 83 FA 08                     cmp r10d, 8
006FF280  75 54                           jne 0x1406ff2d6
006FF282  41 83 39 04                     cmp dword ptr [r9], 4
006FF286  48 8B 6D 00                     mov rbp, qword ptr [rbp]
006FF28A  77 0A                           ja 0x1406ff296
006FF28C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
006FF291  E9 26 03 00 00                  jmp 0x1406ff5bc
006FF296  33 D2                           xor edx, edx
006FF298  45 8B 08                        mov r9d, dword ptr [r8]
006FF29B  49 8D 48 04                     lea rcx, [r8 + 4]
006FF29F  83 FA 04                        cmp edx, 4
006FF2A2  73 1A                           jae 0x1406ff2be
006FF2A4  49 3B C8                        cmp rcx, r8
006FF2A7  0F 82 0A 03 00 00               jb 0x1406ff5b7
006FF2AD  4E 8D 04 09                     lea r8, [rcx + r9]
006FF2B1  4C 3B C1                        cmp r8, rcx
006FF2B4  0F 82 FD 02 00 00               jb 0x1406ff5b7
006FF2BA  FF C2                           inc edx
006FF2BC  EB DA                           jmp 0x1406ff298
006FF2BE  49 3B C8                        cmp rcx, r8
006FF2C1  0F 82 F0 02 00 00               jb 0x1406ff5b7
006FF2C7  33 C0                           xor eax, eax
006FF2C9  45 85 C9                        test r9d, r9d
006FF2CC  48 0F 45 C1                     cmovne rax, rcx
006FF2D0  41 83 F9 04                     cmp r9d, 4
006FF2D4  74 0A                           je 0x1406ff2e0
006FF2D6  BB 23 00 00 C0                  mov ebx, 0xc0000023
006FF2DB  E9 DC 02 00 00                  jmp 0x1406ff5bc
006FF2E0  B9 00 08 00 00                  mov ecx, 0x800
006FF2E5  39 08                           cmp dword ptr [rax], ecx
006FF2E7  74 0A                           je 0x1406ff2f3
006FF2E9  BB 3E 00 00 C0                  mov ebx, 0xc000003e
006FF2EE  E9 C9 02 00 00                  jmp 0x1406ff5bc
006FF2F3  48 8B D1                        mov rdx, rcx
006FF2F6  41 B8 53 4C 53 20               mov r8d, 0x20534c53
006FF2FC  B9 00 01 00 00                  mov ecx, 0x100
006FF301  E8 EA 2D 48 00                  call 0x140b820f0
006FF306  4C 8B F8                        mov r15, rax
006FF309  48 85 C0                        test rax, rax
006FF30C  75 0A                           jne 0x1406ff318
006FF30E  BB 17 00 00 C0                  mov ebx, 0xc0000017
006FF313  E9 A4 02 00 00                  jmp 0x1406ff5bc
006FF318  48 8B 05 11 91 8D 00            mov rax, qword ptr [rip + 0x8d9111]
006FF31F  48 85 C0                        test rax, rax
006FF322  0F 84 7E 02 00 00               je 0x1406ff5a6
006FF328  49 8B CF                        mov rcx, r15
006FF32B  E8 A0 B7 FB FF                  call 0x1406baad0
006FF330  8B D8                           mov ebx, eax
006FF332  85 C0                           test eax, eax
006FF334  0F 88 71 02 00 00               js 0x1406ff5ab
006FF33A  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
006FF33D  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
006FF340  05 38 08 00 00                  add eax, 0x838
006FF345  3D 38 08 00 00                  cmp eax, 0x838
006FF34A  0F 82 4F 02 00 00               jb 0x1406ff59f
006FF350  8D 48 04                        lea ecx, [rax + 4]
006FF353  44 8B F3                        mov r14d, ebx
006FF356  3B C8                           cmp ecx, eax
006FF358  0F 82 41 02 00 00               jb 0x1406ff59f
006FF35E  8D 04 11                        lea eax, [rcx + rdx]
006FF361  BE 95 00 00 C0                  mov esi, 0xc0000095
006FF366  3B C1                           cmp eax, ecx
006FF368  1B DB                           sbb ebx, ebx
006FF36A  23 DE                           and ebx, esi
006FF36C  0F 8C 39 02 00 00               jl 0x1406ff5ab
006FF372  48 85 FF                        test rdi, rdi
006FF375  75 0A                           jne 0x1406ff381
006FF377  BB 0D 00 00 C0                  mov ebx, 0xc000000d
006FF37C  E9 2A 02 00 00                  jmp 0x1406ff5ab
006FF381  BA 20 08 00 00                  mov edx, 0x820
006FF386  B9 00 01 00 00                  mov ecx, 0x100
006FF38B  41 B8 53 4C 53 20               mov r8d, 0x20534c53
006FF391  89 57 04                        mov dword ptr [rdi + 4], edx
006FF394  33 DB                           xor ebx, ebx
006FF396  E8 55 2D 48 00                  call 0x140b820f0
006FF39B  48 85 C0                        test rax, rax
006FF39E  75 07                           jne 0x1406ff3a7
006FF3A0  BB 17 00 00 C0                  mov ebx, 0xc0000017
006FF3A5  EB 06                           jmp 0x1406ff3ad
006FF3A7  48 89 47 08                     mov qword ptr [rdi + 8], rax
006FF3AB  21 1F                           and dword ptr [rdi], ebx
006FF3AD  85 DB                           test ebx, ebx
006FF3AF  0F 88 F6 01 00 00               js 0x1406ff5ab
006FF3B5  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF3B9  41 0F BA EE 1C                  bts r14d, 0x1c
006FF3BE  48 85 D2                        test rdx, rdx
006FF3C1  75 13                           jne 0x1406ff3d6
006FF3C3  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF3C6  8D 48 08                        lea ecx, [rax + 8]
006FF3C9  3B C8                           cmp ecx, eax
006FF3CB  0F 82 DC 00 00 00               jb 0x1406ff4ad
006FF3D1  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF3D4  EB 58                           jmp 0x1406ff42e
006FF3D6  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF3D9  33 C9                           xor ecx, ecx
006FF3DB  41 3B C9                        cmp ecx, r9d
006FF3DE  73 24                           jae 0x1406ff404
006FF3E0  8B 02                           mov eax, dword ptr [rdx]
006FF3E2  83 C0 04                        add eax, 4
006FF3E5  83 F8 04                        cmp eax, 4
006FF3E8  0F 82 C3 00 00 00               jb 0x1406ff4b1
006FF3EE  44 8B C0                        mov r8d, eax
006FF3F1  4C 03 C2                        add r8, rdx
006FF3F4  4C 3B C2                        cmp r8, rdx
006FF3F7  0F 82 B4 00 00 00               jb 0x1406ff4b1
006FF3FD  49 8B D0                        mov rdx, r8
006FF400  FF C1                           inc ecx
006FF402  EB D7                           jmp 0x1406ff3db
006FF404  4C 8D 42 04                     lea r8, [rdx + 4]
006FF408  4C 3B C2                        cmp r8, rdx
006FF40B  0F 82 A0 00 00 00               jb 0x1406ff4b1
006FF411  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF414  48 8D 42 08                     lea rax, [rdx + 8]
006FF418  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF41C  48 3B C1                        cmp rax, rcx
006FF41F  0F 87 D5 00 00 00               ja 0x1406ff4fa
006FF425  C7 02 04 00 00 00               mov dword ptr [rdx], 4
006FF42B  45 89 30                        mov dword ptr [r8], r14d
006FF42E  FF 07                           inc dword ptr [rdi]
006FF430  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF434  48 85 D2                        test rdx, rdx
006FF437  75 0F                           jne 0x1406ff448
006FF439  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF43C  8D 48 0C                        lea ecx, [rax + 0xc]
006FF43F  3B C8                           cmp ecx, eax
006FF441  72 6A                           jb 0x1406ff4ad
006FF443  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF446  EB 48                           jmp 0x1406ff490
006FF448  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF44B  33 C9                           xor ecx, ecx
006FF44D  41 3B C9                        cmp ecx, r9d
006FF450  73 1C                           jae 0x1406ff46e
006FF452  8B 02                           mov eax, dword ptr [rdx]
006FF454  83 C0 04                        add eax, 4
006FF457  83 F8 04                        cmp eax, 4
006FF45A  72 55                           jb 0x1406ff4b1
006FF45C  44 8B C0                        mov r8d, eax
006FF45F  4C 03 C2                        add r8, rdx
006FF462  4C 3B C2                        cmp r8, rdx
006FF465  72 4A                           jb 0x1406ff4b1
006FF467  49 8B D0                        mov rdx, r8
006FF46A  FF C1                           inc ecx
006FF46C  EB DF                           jmp 0x1406ff44d
006FF46E  4C 8D 42 04                     lea r8, [rdx + 4]
006FF472  4C 3B C2                        cmp r8, rdx
006FF475  72 3A                           jb 0x1406ff4b1
006FF477  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF47A  48 8D 42 0C                     lea rax, [rdx + 0xc]
006FF47E  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF482  48 3B C1                        cmp rax, rcx
006FF485  77 73                           ja 0x1406ff4fa
006FF487  C7 02 08 00 00 00               mov dword ptr [rdx], 8
006FF48D  49 89 28                        mov qword ptr [r8], rbp
006FF490  FF 07                           inc dword ptr [rdi]
006FF492  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF496  48 85 D2                        test rdx, rdx
006FF499  75 1D                           jne 0x1406ff4b8
006FF49B  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF49E  8D 88 04 08 00 00               lea ecx, [rax + 0x804]
006FF4A4  3B C8                           cmp ecx, eax
006FF4A6  72 05                           jb 0x1406ff4ad
006FF4A8  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF4AB  EB 6E                           jmp 0x1406ff51b
006FF4AD  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
006FF4B1  8B DE                           mov ebx, esi
006FF4B3  E9 F3 00 00 00                  jmp 0x1406ff5ab
006FF4B8  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF4BB  33 C9                           xor ecx, ecx
006FF4BD  41 3B C9                        cmp ecx, r9d
006FF4C0  73 1C                           jae 0x1406ff4de
006FF4C2  8B 02                           mov eax, dword ptr [rdx]
006FF4C4  83 C0 04                        add eax, 4
006FF4C7  83 F8 04                        cmp eax, 4
006FF4CA  72 E5                           jb 0x1406ff4b1
006FF4CC  44 8B C0                        mov r8d, eax
006FF4CF  4C 03 C2                        add r8, rdx
006FF4D2  4C 3B C2                        cmp r8, rdx
006FF4D5  72 DA                           jb 0x1406ff4b1
006FF4D7  49 8B D0                        mov rdx, r8
006FF4DA  FF C1                           inc ecx
006FF4DC  EB DF                           jmp 0x1406ff4bd
006FF4DE  4C 8D 42 04                     lea r8, [rdx + 4]
006FF4E2  4C 3B C2                        cmp r8, rdx
006FF4E5  72 CA                           jb 0x1406ff4b1
006FF4E7  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF4EA  48 8D 82 04 08 00 00            lea rax, [rdx + 0x804]
006FF4F1  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF4F5  48 3B C1                        cmp rax, rcx
006FF4F8  76 0A                           jbe 0x1406ff504
006FF4FA  BB 23 00 00 C0                  mov ebx, 0xc0000023
006FF4FF  E9 A7 00 00 00                  jmp 0x1406ff5ab
006FF504  C7 02 00 08 00 00               mov dword ptr [rdx], 0x800
006FF50A  49 8B C8                        mov rcx, r8
006FF50D  49 8B D7                        mov rdx, r15
006FF510  41 B8 00 08 00 00               mov r8d, 0x800
006FF516  E8 25 73 FC FF                  call 0x1406c6840
006FF51B  FF 07                           inc dword ptr [rdi]
006FF51D  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF521  48 85 D2                        test rdx, rdx
006FF524  75 17                           jne 0x1406ff53d
006FF526  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF529  8D 48 08                        lea ecx, [rax + 8]
006FF52C  3B C8                           cmp ecx, eax
006FF52E  0F 82 79 FF FF FF               jb 0x1406ff4ad
006FF534  FF 07                           inc dword ptr [rdi]
006FF536  33 DB                           xor ebx, ebx
006FF538  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF53B  EB 6E                           jmp 0x1406ff5ab
006FF53D  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF540  33 C9                           xor ecx, ecx
006FF542  41 3B C9                        cmp ecx, r9d
006FF545  73 24                           jae 0x1406ff56b
006FF547  8B 02                           mov eax, dword ptr [rdx]
006FF549  83 C0 04                        add eax, 4
006FF54C  83 F8 04                        cmp eax, 4
006FF54F  0F 82 5C FF FF FF               jb 0x1406ff4b1
006FF555  44 8B C0                        mov r8d, eax
006FF558  4C 03 C2                        add r8, rdx
006FF55B  4C 3B C2                        cmp r8, rdx
006FF55E  0F 82 4D FF FF FF               jb 0x1406ff4b1
006FF564  49 8B D0                        mov rdx, r8
006FF567  FF C1                           inc ecx
006FF569  EB D7                           jmp 0x1406ff542
006FF56B  4C 8D 42 04                     lea r8, [rdx + 4]
006FF56F  4C 3B C2                        cmp r8, rdx
006FF572  0F 82 39 FF FF FF               jb 0x1406ff4b1
006FF578  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF57B  48 8D 42 08                     lea rax, [rdx + 8]
006FF57F  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF583  33 DB                           xor ebx, ebx
006FF585  48 3B C1                        cmp rax, rcx
006FF588  0F 87 6C FF FF FF               ja 0x1406ff4fa
006FF58E  C7 02 04 00 00 00               mov dword ptr [rdx], 4
006FF594  41 C7 00 00 08 00 00            mov dword ptr [r8], 0x800
006FF59B  FF 07                           inc dword ptr [rdi]
006FF59D  EB 0C                           jmp 0x1406ff5ab
006FF59F  BB 95 00 00 C0                  mov ebx, 0xc0000095
006FF5A4  EB 05                           jmp 0x1406ff5ab
006FF5A6  BB BB 00 00 C0                  mov ebx, 0xc00000bb
006FF5AB  33 D2                           xor edx, edx
006FF5AD  49 8B CF                        mov rcx, r15
006FF5B0  E8 BB 32 48 00                  call 0x140b82870
006FF5B5  EB 05                           jmp 0x1406ff5bc
006FF5B7  BB 95 00 00 C0                  mov ebx, 0xc0000095
006FF5BC  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
006FF5C1  8B C3                           mov eax, ebx
006FF5C3  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
006FF5C8  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
006FF5CD  48 83 C4 20                     add rsp, 0x20
006FF5D1  41 5F                           pop r15
006FF5D3  41 5E                           pop r14
006FF5D5  5F                              pop rdi
006FF5D6  C3                              ret
006FF5D7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FF210(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_006FF28C;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_006FF28C;
    a2 = 0;
loc_006FF244:
    if (0 >= 3) goto loc_006FF26A;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_006FF5B7;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_006FF5B7;
    a2 = (unsigned int)((a2) + 1);
    goto loc_006FF244;
loc_006FF26A:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_006FF5B7;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_006FF2D6;
    if ((*(unsigned int *)(a1)) > 4) goto loc_006FF296;
loc_006FF28C:
    goto loc_006FF5BC;
loc_006FF296:
    a2 = 0;
loc_006FF298:
    if (0 >= 4) goto loc_006FF2BE;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_006FF5B7;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_006FF5B7;
    a2 = (unsigned int)((a2) + 1);
    goto loc_006FF298;
loc_006FF2BE:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_006FF5B7;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_006FF2E0;
loc_006FF2D6:
    goto loc_006FF5BC;
loc_006FF2E0:
    if ((*(unsigned int *)(result)) == ((unsigned int)((unsigned int)(0x800ULL)))) goto loc_006FF2F3;
    goto loc_006FF5BC;
loc_006FF2F3:
    result = ExAllocatePool2(256, (unsigned int)(0x800ULL), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (result != 0) goto loc_006FF318;
    goto loc_006FF5BC;
loc_006FF318:
    if (*(unsigned __int64 *)(v_rip + 9277713) == 0) goto loc_006FF5A6;
    result = guard_dispatch_icall(result, (unsigned int)(0x800ULL), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (sign_flag) goto loc_006FF5AB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (0x838ULL));
    if (((unsigned int)(result)) < 0x838ULL) goto loc_006FF59F;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_006FF59F;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (condition_is_less) goto loc_006FF5AB;
    if (a4 != 0) goto loc_006FF381;
    goto loc_006FF5AB;
loc_006FF381:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(0x820ULL));
    v_rbx = 0;
    result = ExAllocatePool2(256, (unsigned int)(0x820ULL), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (result != 0) goto loc_006FF3A7;
    goto loc_006FF3AD;
loc_006FF3A7:
    *(unsigned __int64 *)(a4 + 8) = result;
loc_006FF3AD:
    if (sign_flag) goto loc_006FF5AB;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF3D6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF4AD;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_006FF42E;
loc_006FF3D6:
    a1 = 0;
loc_006FF3DB:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF404;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF4B1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF4B1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF3DB;
loc_006FF404:
    if ((a3 + 4) < a3) goto loc_006FF4B1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_006FF4FA;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_006FF42E:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF448;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF4AD;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_006FF490;
loc_006FF448:
    a1 = 0;
loc_006FF44D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF46E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF4B1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF4B1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF44D;
loc_006FF46E:
    if ((a3 + 4) < a3) goto loc_006FF4B1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_006FF4FA;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_rbp);
loc_006FF490:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF4B8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 2052)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF4AD;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 2052);
    goto loc_006FF51B;
loc_006FF4AD:
loc_006FF4B1:
    goto loc_006FF5AB;
loc_006FF4B8:
    a1 = 0;
loc_006FF4BD:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF4DE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF4B1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF4B1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF4BD;
loc_006FF4DE:
    if ((a3 + 4) < a3) goto loc_006FF4B1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 2052) <= a1) goto loc_006FF504;
loc_006FF4FA:
    goto loc_006FF5AB;
loc_006FF504:
    *(unsigned int *)(a3) = 0x800ULL;
    result = memcpy(a3 + 4, result, (unsigned int)(0x800ULL), (unsigned int)(*(unsigned int *)(a4)));
loc_006FF51B:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF53D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF4AD;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_006FF5AB;
loc_006FF53D:
    a1 = 0;
loc_006FF542:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF56B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF4B1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF4B1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF542;
loc_006FF56B:
    if ((a3 + 4) < a3) goto loc_006FF4B1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    v_rbx = 0;
    if ((a3 + 8) > a1) goto loc_006FF4FA;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = 0x800ULL;
    goto loc_006FF5AB;
loc_006FF59F:
    goto loc_006FF5AB;
loc_006FF5A6:
loc_006FF5AB:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3 + 4, (unsigned int)(*(unsigned int *)(a4)));
    goto loc_006FF5BC;
loc_006FF5B7:
loc_006FF5BC:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006FF210(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_006FF28C;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_006FF28C;
    Arg2 = 0;
loc_006FF244:
    if (0 >= 3) goto loc_006FF26A;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_006FF5B7;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_006FF5B7;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_006FF244;
loc_006FF26A:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_006FF5B7;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_006FF2D6;
    if ((*(uint32_t *)(arg1)) > 4) goto loc_006FF296;
loc_006FF28C:
    goto loc_006FF5BC;
loc_006FF296:
    Arg2 = 0;
loc_006FF298:
    if (0 >= 4) goto loc_006FF2BE;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_006FF5B7;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_006FF5B7;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_006FF298;
loc_006FF2BE:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_006FF5B7;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_006FF2E0;
loc_006FF2D6:
    goto loc_006FF5BC;
loc_006FF2E0:
    if ((*(uint32_t *)(result)) == ((uint32_t)((uint32_t)(0x800ULL)))) goto loc_006FF2F3;
    goto loc_006FF5BC;
loc_006FF2F3:
    result = ExAllocatePool2(256, (uint32_t)(0x800ULL), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (result != 0) goto loc_006FF318;
    goto loc_006FF5BC;
loc_006FF318:
    if (*(uint64_t *)(v_rip + 0x8D9111) == 0) goto loc_006FF5A6;
    result = guard_dispatch_icall(result, (uint32_t)(0x800ULL), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (sign_flag) goto loc_006FF5AB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) + (0x838ULL));
    if (((uint32_t)(result)) < 0x838ULL) goto loc_006FF59F;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_006FF59F;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (condition_is_less) goto loc_006FF5AB;
    if (Arg4 != 0) goto loc_006FF381;
    goto loc_006FF5AB;
loc_006FF381:
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(0x820ULL));
    local_rbx = 0;
    result = ExAllocatePool2(256, (uint32_t)(0x820ULL), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (result != 0) goto loc_006FF3A7;
    goto loc_006FF3AD;
loc_006FF3A7:
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_006FF3AD:
    if (sign_flag) goto loc_006FF5AB;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF3D6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF4AD;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_006FF42E;
loc_006FF3D6:
    Arg1 = 0;
loc_006FF3DB:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF404;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF4B1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF4B1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF3DB;
loc_006FF404:
    if ((Arg3 + 4) < Arg3) goto loc_006FF4B1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_006FF4FA;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_006FF42E:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF448;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF4AD;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_006FF490;
loc_006FF448:
    Arg1 = 0;
loc_006FF44D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF46E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF4B1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF4B1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF44D;
loc_006FF46E:
    if ((Arg3 + 4) < Arg3) goto loc_006FF4B1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_006FF4FA;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_rbp);
loc_006FF490:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF4B8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 2052)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF4AD;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 2052);
    goto loc_006FF51B;
loc_006FF4AD:
loc_006FF4B1:
    goto loc_006FF5AB;
loc_006FF4B8:
    Arg1 = 0;
loc_006FF4BD:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF4DE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF4B1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF4B1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF4BD;
loc_006FF4DE:
    if ((Arg3 + 4) < Arg3) goto loc_006FF4B1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 2052) <= Arg1) goto loc_006FF504;
loc_006FF4FA:
    goto loc_006FF5AB;
loc_006FF504:
    *(uint32_t *)(Arg3) = 0x800ULL;
    result = memcpy(Arg3 + 4, result, (uint32_t)(0x800ULL), (uint32_t)(*(uint32_t *)(Arg4)));
loc_006FF51B:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF53D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF4AD;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_006FF5AB;
loc_006FF53D:
    Arg1 = 0;
loc_006FF542:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF56B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF4B1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF4B1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF542;
loc_006FF56B:
    if ((Arg3 + 4) < Arg3) goto loc_006FF4B1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    local_rbx = 0;
    if ((Arg3 + 8) > Arg1) goto loc_006FF4FA;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = 0x800ULL;
    goto loc_006FF5AB;
loc_006FF59F:
    goto loc_006FF5AB;
loc_006FF5A6:
loc_006FF5AB:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3 + 4, (uint32_t)(*(uint32_t *)(Arg4)));
    goto loc_006FF5BC;
loc_006FF5B7:
loc_006FF5BC:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x006FF210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
