# sub_00AD3088

- RVA: `0x00AD3088`–`0x00AD343A` (길이 `946` bytes)
- VA: `0x0000000140AD3088`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEB64`
- 디코드: `265`개 명령, `946/946` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AD3191` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD31EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD341B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x00969E53`

### Static image references
- `0x00AD309F` → RVA `0x00E0A740` (`.data`; read)
- `0x00AD3169` → RVA `0x00FD83B8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AD3191` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD31EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD341B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD3088  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AD308D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00AD3092  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00AD3097  57                              push rdi
00AD3098  48 81 EC 40 01 00 00            sub rsp, 0x140
00AD309F  48 8B 05 9A 76 33 00            mov rax, qword ptr [rip + 0x33769a]
00AD30A6  48 33 C4                        xor rax, rsp
00AD30A9  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00AD30B1  49 8B F9                        mov rdi, r9
00AD30B4  48 8B DA                        mov rbx, rdx
00AD30B7  4C 8B C1                        mov r8, rcx
00AD30BA  48 85 C9                        test rcx, rcx
00AD30BD  75 0B                           jne 0x140ad30ca
00AD30BF  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
00AD30C5  E9 43 03 00 00                  jmp 0x140ad340d
00AD30CA  48 85 DB                        test rbx, rbx
00AD30CD  74 F0                           je 0x140ad30bf
00AD30CF  48 85 FF                        test rdi, rdi
00AD30D2  74 EB                           je 0x140ad30bf
00AD30D4  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AD30D8  48 85 C9                        test rcx, rcx
00AD30DB  74 E2                           je 0x140ad30bf
00AD30DD  41 83 38 03                     cmp dword ptr [r8], 3
00AD30E1  76 DC                           jbe 0x140ad30bf
00AD30E3  48 8B C1                        mov rax, rcx
00AD30E6  45 33 C9                        xor r9d, r9d
00AD30E9  44 8B 10                        mov r10d, dword ptr [rax]
00AD30EC  48 8D 50 04                     lea rdx, [rax + 4]
00AD30F0  41 83 F9 03                     cmp r9d, 3
00AD30F4  73 1B                           jae 0x140ad3111
00AD30F6  48 3B D0                        cmp rdx, rax
00AD30F9  0F 82 08 03 00 00               jb 0x140ad3407
00AD30FF  4A 8D 04 12                     lea rax, [rdx + r10]
00AD3103  48 3B C2                        cmp rax, rdx
00AD3106  0F 82 FB 02 00 00               jb 0x140ad3407
00AD310C  41 FF C1                        inc r9d
00AD310F  EB D8                           jmp 0x140ad30e9
00AD3111  48 3B D0                        cmp rdx, rax
00AD3114  0F 82 ED 02 00 00               jb 0x140ad3407
00AD311A  33 F6                           xor esi, esi
00AD311C  45 85 D2                        test r10d, r10d
00AD311F  48 0F 45 F2                     cmovne rsi, rdx
00AD3123  41 83 FA 08                     cmp r10d, 8
00AD3127  0F 85 CB 01 00 00               jne 0x140ad32f8
00AD312D  41 83 38 04                     cmp dword ptr [r8], 4
00AD3131  48 8B 36                        mov rsi, qword ptr [rsi]
00AD3134  76 89                           jbe 0x140ad30bf
00AD3136  45 33 C0                        xor r8d, r8d
00AD3139  8B 01                           mov eax, dword ptr [rcx]
00AD313B  48 8D 51 04                     lea rdx, [rcx + 4]
00AD313F  41 83 F8 04                     cmp r8d, 4
00AD3143  73 1B                           jae 0x140ad3160
00AD3145  48 3B D1                        cmp rdx, rcx
00AD3148  0F 82 B9 02 00 00               jb 0x140ad3407
00AD314E  48 8D 0C 02                     lea rcx, [rdx + rax]
00AD3152  48 3B CA                        cmp rcx, rdx
00AD3155  0F 82 AC 02 00 00               jb 0x140ad3407
00AD315B  41 FF C0                        inc r8d
00AD315E  EB D9                           jmp 0x140ad3139
00AD3160  48 3B D1                        cmp rdx, rcx
00AD3163  0F 82 9E 02 00 00               jb 0x140ad3407
00AD3169  4C 8B 15 48 52 50 00            mov r10, qword ptr [rip + 0x505248]
00AD3170  33 C9                           xor ecx, ecx
00AD3172  85 C0                           test eax, eax
00AD3174  48 0F 45 CA                     cmovne rcx, rdx
00AD3178  4D 85 D2                        test r10, r10
00AD317B  0F 84 7E 02 00 00               je 0x140ad33ff
00AD3181  8B D0                           mov edx, eax
00AD3183  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00AD3188  49 8B C2                        mov rax, r10
00AD318B  41 B9 00 01 00 00               mov r9d, 0x100
00AD3191  E8 3A 79 BE FF                  call 0x1406baad0
00AD3196  44 8B C0                        mov r8d, eax
00AD3199  85 C0                           test eax, eax
00AD319B  0F 88 6C 02 00 00               js 0x140ad340d
00AD31A1  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00AD31A4  8B 53 20                        mov edx, dword ptr [rbx + 0x20]
00AD31A7  05 30 01 00 00                  add eax, 0x130
00AD31AC  3D 30 01 00 00                  cmp eax, 0x130
00AD31B1  0F 82 50 02 00 00               jb 0x140ad3407
00AD31B7  8D 48 04                        lea ecx, [rax + 4]
00AD31BA  41 8B E8                        mov ebp, r8d
00AD31BD  3B C8                           cmp ecx, eax
00AD31BF  0F 82 42 02 00 00               jb 0x140ad3407
00AD31C5  8D 04 0A                        lea eax, [rdx + rcx]
00AD31C8  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD31CD  3B C1                           cmp eax, ecx
00AD31CF  45 1B C0                        sbb r8d, r8d
00AD31D2  44 23 C3                        and r8d, ebx
00AD31D5  0F 8C 32 02 00 00               jl 0x140ad340d
00AD31DB  BA 18 01 00 00                  mov edx, 0x118
00AD31E0  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD31E6  89 57 04                        mov dword ptr [rdi + 4], edx
00AD31E9  8D 4A E8                        lea ecx, [rdx - 0x18]
00AD31EC  E8 FF EE 0A 00                  call 0x140b820f0
00AD31F1  48 85 C0                        test rax, rax
00AD31F4  75 09                           jne 0x140ad31ff
00AD31F6  44 8D 43 82                     lea r8d, [rbx - 0x7e]
00AD31FA  E9 0E 02 00 00                  jmp 0x140ad340d
00AD31FF  48 89 47 08                     mov qword ptr [rdi + 8], rax
00AD3203  83 27 00                        and dword ptr [rdi], 0
00AD3206  0F BA ED 1C                     bts ebp, 0x1c
00AD320A  48 8B D0                        mov rdx, rax
00AD320D  48 85 C0                        test rax, rax
00AD3210  75 1B                           jne 0x140ad322d
00AD3212  8B 47 04                        mov eax, dword ptr [rdi + 4]
00AD3215  8D 48 08                        lea ecx, [rax + 8]
00AD3218  3B C8                           cmp ecx, eax
00AD321A  72 05                           jb 0x140ad3221
00AD321C  89 4F 04                        mov dword ptr [rdi + 4], ecx
00AD321F  EB 58                           jmp 0x140ad3279
00AD3221  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00AD3225  44 8B C3                        mov r8d, ebx
00AD3228  E9 E0 01 00 00                  jmp 0x140ad340d
00AD322D  44 8B 0F                        mov r9d, dword ptr [rdi]
00AD3230  33 C9                           xor ecx, ecx
00AD3232  41 3B C9                        cmp ecx, r9d
00AD3235  73 1C                           jae 0x140ad3253
00AD3237  8B 02                           mov eax, dword ptr [rdx]
00AD3239  83 C0 04                        add eax, 4
00AD323C  83 F8 04                        cmp eax, 4
00AD323F  72 E4                           jb 0x140ad3225
00AD3241  44 8B C0                        mov r8d, eax
00AD3244  4C 03 C2                        add r8, rdx
00AD3247  4C 3B C2                        cmp r8, rdx
00AD324A  72 D9                           jb 0x140ad3225
00AD324C  49 8B D0                        mov rdx, r8
00AD324F  FF C1                           inc ecx
00AD3251  EB DF                           jmp 0x140ad3232
00AD3253  4C 8D 42 04                     lea r8, [rdx + 4]
00AD3257  4C 3B C2                        cmp r8, rdx
00AD325A  72 C9                           jb 0x140ad3225
00AD325C  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD325F  48 8D 42 08                     lea rax, [rdx + 8]
00AD3263  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD3267  48 3B C1                        cmp rax, rcx
00AD326A  0F 87 88 00 00 00               ja 0x140ad32f8
00AD3270  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD3276  41 89 28                        mov dword ptr [r8], ebp
00AD3279  FF 07                           inc dword ptr [rdi]
00AD327B  41 83 C9 FF                     or r9d, 0xffffffff
00AD327F  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00AD3283  48 85 D2                        test rdx, rdx
00AD3286  75 25                           jne 0x140ad32ad
00AD3288  8B 57 04                        mov edx, dword ptr [rdi + 4]
00AD328B  41 8B C1                        mov eax, r9d
00AD328E  8D 4A 0C                        lea ecx, [rdx + 0xc]
00AD3291  3B CA                           cmp ecx, edx
00AD3293  0F 43 C1                        cmovae eax, ecx
00AD3296  45 1B C0                        sbb r8d, r8d
00AD3299  44 23 C3                        and r8d, ebx
00AD329C  89 47 04                        mov dword ptr [rdi + 4], eax
00AD329F  3B CA                           cmp ecx, edx
00AD32A1  73 69                           jae 0x140ad330c
00AD32A3  45 85 C0                        test r8d, r8d
00AD32A6  79 66                           jns 0x140ad330e
00AD32A8  E9 60 01 00 00                  jmp 0x140ad340d
00AD32AD  44 8B 17                        mov r10d, dword ptr [rdi]
00AD32B0  33 C9                           xor ecx, ecx
00AD32B2  41 3B CA                        cmp ecx, r10d
00AD32B5  73 24                           jae 0x140ad32db
00AD32B7  8B 02                           mov eax, dword ptr [rdx]
00AD32B9  83 C0 04                        add eax, 4
00AD32BC  83 F8 04                        cmp eax, 4
00AD32BF  0F 82 60 FF FF FF               jb 0x140ad3225
00AD32C5  44 8B C0                        mov r8d, eax
00AD32C8  4C 03 C2                        add r8, rdx
00AD32CB  4C 3B C2                        cmp r8, rdx
00AD32CE  0F 82 51 FF FF FF               jb 0x140ad3225
00AD32D4  49 8B D0                        mov rdx, r8
00AD32D7  FF C1                           inc ecx
00AD32D9  EB D7                           jmp 0x140ad32b2
00AD32DB  4C 8D 42 04                     lea r8, [rdx + 4]
00AD32DF  4C 3B C2                        cmp r8, rdx
00AD32E2  0F 82 3D FF FF FF               jb 0x140ad3225
00AD32E8  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD32EB  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD32EF  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD32F3  48 3B C1                        cmp rax, rcx
00AD32F6  76 0B                           jbe 0x140ad3303
00AD32F8  41 B8 23 00 00 C0               mov r8d, 0xc0000023
00AD32FE  E9 0A 01 00 00                  jmp 0x140ad340d
00AD3303  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD3309  49 89 30                        mov qword ptr [r8], rsi
00AD330C  FF 07                           inc dword ptr [rdi]
00AD330E  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00AD3312  48 85 D2                        test rdx, rdx
00AD3315  75 2B                           jne 0x140ad3342
00AD3317  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD331A  8D 81 04 01 00 00               lea eax, [rcx + 0x104]
00AD3320  3B C1                           cmp eax, ecx
00AD3322  44 0F 43 C8                     cmovae r9d, eax
00AD3326  45 1B C0                        sbb r8d, r8d
00AD3329  44 23 C3                        and r8d, ebx
00AD332C  44 89 4F 04                     mov dword ptr [rdi + 4], r9d
00AD3330  3B C1                           cmp eax, ecx
00AD3332  0F 82 D5 00 00 00               jb 0x140ad340d
00AD3338  FF 07                           inc dword ptr [rdi]
00AD333A  45 33 C0                        xor r8d, r8d
00AD333D  E9 CB 00 00 00                  jmp 0x140ad340d
00AD3342  44 8B 0F                        mov r9d, dword ptr [rdi]
00AD3345  33 C9                           xor ecx, ecx
00AD3347  41 3B C9                        cmp ecx, r9d
00AD334A  73 24                           jae 0x140ad3370
00AD334C  8B 02                           mov eax, dword ptr [rdx]
00AD334E  83 C0 04                        add eax, 4
00AD3351  83 F8 04                        cmp eax, 4
00AD3354  0F 82 CB FE FF FF               jb 0x140ad3225
00AD335A  44 8B C0                        mov r8d, eax
00AD335D  4C 03 C2                        add r8, rdx
00AD3360  4C 3B C2                        cmp r8, rdx
00AD3363  0F 82 BC FE FF FF               jb 0x140ad3225
00AD3369  49 8B D0                        mov rdx, r8
00AD336C  FF C1                           inc ecx
00AD336E  EB D7                           jmp 0x140ad3347
00AD3370  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD3374  4C 3B CA                        cmp r9, rdx
00AD3377  0F 82 A8 FE FF FF               jb 0x140ad3225
00AD337D  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD3380  48 8D 82 04 01 00 00            lea rax, [rdx + 0x104]
00AD3387  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD338B  45 33 C0                        xor r8d, r8d
00AD338E  48 3B C1                        cmp rax, rcx
00AD3391  0F 87 61 FF FF FF               ja 0x140ad32f8
00AD3397  41 8D 48 02                     lea ecx, [r8 + 2]
00AD339B  C7 02 00 01 00 00               mov dword ptr [rdx], 0x100
00AD33A1  8D 51 7E                        lea edx, [rcx + 0x7e]
00AD33A4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00AD33A9  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AD33AC  41 0F 11 01                     movups xmmword ptr [r9], xmm0
00AD33B0  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00AD33B4  41 0F 11 49 10                  movups xmmword ptr [r9 + 0x10], xmm1
00AD33B9  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00AD33BD  41 0F 11 41 20                  movups xmmword ptr [r9 + 0x20], xmm0
00AD33C2  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00AD33C6  41 0F 11 49 30                  movups xmmword ptr [r9 + 0x30], xmm1
00AD33CB  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00AD33CF  41 0F 11 41 40                  movups xmmword ptr [r9 + 0x40], xmm0
00AD33D4  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
00AD33D8  41 0F 11 49 50                  movups xmmword ptr [r9 + 0x50], xmm1
00AD33DD  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
00AD33E1  41 0F 11 41 60                  movups xmmword ptr [r9 + 0x60], xmm0
00AD33E6  4C 03 CA                        add r9, rdx
00AD33E9  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
00AD33ED  48 03 C2                        add rax, rdx
00AD33F0  41 0F 11 49 F0                  movups xmmword ptr [r9 - 0x10], xmm1
00AD33F5  48 83 E9 01                     sub rcx, 1
00AD33F9  75 AE                           jne 0x140ad33a9
00AD33FB  FF 07                           inc dword ptr [rdi]
00AD33FD  EB 0E                           jmp 0x140ad340d
00AD33FF  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
00AD3405  EB 06                           jmp 0x140ad340d
00AD3407  41 B8 95 00 00 C0               mov r8d, 0xc0000095
00AD340D  41 8B C0                        mov eax, r8d
00AD3410  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
00AD3418  48 33 CC                        xor rcx, rsp
00AD341B  E8 20 92 BD FF                  call 0x1406ac640
00AD3420  4C 8D 9C 24 40 01 00 00         lea r11, [rsp + 0x140]
00AD3428  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00AD342C  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
00AD3430  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
00AD3434  49 8B E3                        mov rsp, r11
00AD3437  5F                              pop rdi
00AD3438  C3                              ret
00AD3439  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD3088(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 3372698)) ^ (v_rsp);
    v_stack_m18 = result;
    if (a1 != 0) goto loc_00AD30CA;
loc_00AD30BF:
    goto loc_00AD340D;
loc_00AD30CA:
    if (a2 == 0) goto loc_00AD30BF;
    if (a4 == 0) goto loc_00AD30BF;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD30BF;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 3) goto loc_00AD30BF;
    a4 = 0;
loc_00AD30E9:
    if (0 >= 3) goto loc_00AD3111;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD3407;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD3407;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00AD30E9;
loc_00AD3111:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD3407;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00AD32F8;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 4) goto loc_00AD30BF;
    a3 = 0;
loc_00AD3139:
    if (0 >= 4) goto loc_00AD3160;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD3407;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD3407;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00AD3139;
loc_00AD3160:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD3407;
    a1 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a1 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (*(unsigned __int64 *)(v_rip + 5263944) == 0) goto loc_00AD33FF;
    result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))), v_stack_m118, 256);
    if (sign_flag) goto loc_00AD340D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (304));
    if (((unsigned int)(result)) < 304) goto loc_00AD3407;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00AD3407;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (condition_is_less) goto loc_00AD340D;
    *(unsigned int *)(a4 + 4) = 280;
    result = ExAllocatePool2(280 - 24, 280, (unsigned int)(0x20534C53ULL), 256);
    if (result != 0) goto loc_00AD31FF;
    goto loc_00AD340D;
loc_00AD31FF:
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result != 0) goto loc_00AD322D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD3221;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD3279;
loc_00AD3221:
loc_00AD3225:
    goto loc_00AD340D;
loc_00AD322D:
    a1 = 0;
loc_00AD3232:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD3253;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3225;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_00AD3225;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00AD3232;
loc_00AD3253:
    if ((a3 + 4) < a3) goto loc_00AD3225;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00AD32F8;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00AD3279:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD32AD;
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    a3 = (unsigned int)((a3 + 4) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD330C;
    if (!sign_flag) goto loc_00AD330E;
    goto loc_00AD340D;
loc_00AD32AD:
    a1 = 0;
loc_00AD32B2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD32DB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a4 + 4))))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3225;
    a3 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)(*(unsigned int *)(a4 + 4)));
    if (a3 < ((unsigned int)(*(unsigned int *)(a4 + 4)))) goto loc_00AD3225;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00AD32B2;
loc_00AD32DB:
    if ((a3 + 4) < a3) goto loc_00AD3225;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) <= a1) goto loc_00AD3303;
loc_00AD32F8:
    goto loc_00AD340D;
loc_00AD3303:
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)((unsigned int)(0xC0000023ULL)) = *(unsigned __int64 *)(v_rsi);
loc_00AD330C:
loc_00AD330E:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD3342;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 260)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 260); }
    a3 = (unsigned int)(((unsigned int)(0xC0000023ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 260)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD340D;
    a3 = 0;
    goto loc_00AD340D;
loc_00AD3342:
    a1 = 0;
loc_00AD3347:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD3370;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3225;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD3225;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00AD3347;
loc_00AD3370:
    if ((a3 + 4) < a3) goto loc_00AD3225;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    a3 = 0;
    if ((a3 + 260) > a1) goto loc_00AD32F8;
    *(unsigned int *)(a3) = 256;
loc_00AD33A9:
    *(unsigned __int64 *)(a3 + 4) = v_xmm0;
    *(unsigned __int64 *)(a3 + 4 + 16) = v_xmm1;
    *(unsigned __int64 *)(a3 + 4 + 32) = v_xmm0;
    *(unsigned __int64 *)(a3 + 4 + 48) = v_xmm1;
    *(unsigned __int64 *)(a3 + 4 + 64) = v_xmm0;
    *(unsigned __int64 *)(a3 + 4 + 80) = v_xmm1;
    *(unsigned __int64 *)(a3 + 4 + 96) = v_xmm0;
    a4 = (a3 + 4) + (a3 + 2 + 126);
    result = (v_stack_m118) + (a3 + 2 + 126);
    *(unsigned __int64 *)(a4 - 16) = v_xmm1;
    a1 = (a3 + 2) - (1);
    if (condition_is_not_equal) goto loc_00AD33A9;
    goto loc_00AD340D;
loc_00AD33FF:
    goto loc_00AD340D;
loc_00AD3407:
loc_00AD340D:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a3 + 2 + 126, (unsigned int)(0xC0000095ULL), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD3088(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m18;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x33769A)) ^ (local_rsp);
    v_stack_m18 = result;
    if (Arg1 != NULL) goto loc_00AD30CA;
loc_00AD30BF:
    goto loc_00AD340D;
loc_00AD30CA:
    if (Arg2 == 0) goto loc_00AD30BF;
    if (Arg4 == 0) goto loc_00AD30BF;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD30BF;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 3) goto loc_00AD30BF;
    Arg4 = 0;
loc_00AD30E9:
    if (0 >= 3) goto loc_00AD3111;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD3407;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD3407;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00AD30E9;
loc_00AD3111:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD3407;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00AD32F8;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 4) goto loc_00AD30BF;
    Arg3 = 0;
loc_00AD3139:
    if (0 >= 4) goto loc_00AD3160;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD3407;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD3407;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00AD3139;
loc_00AD3160:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD3407;
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg1 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (*(uint64_t *)(v_rip + 0x505248) == 0) goto loc_00AD33FF;
    result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))), v_stack_m118, 256);
    if (sign_flag) goto loc_00AD340D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x10))) + (304));
    if (((uint32_t)(result)) < 304) goto loc_00AD3407;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00AD3407;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (condition_is_less) goto loc_00AD340D;
    *(uint32_t *)(Arg4 + 0x4) = 280;
    result = ExAllocatePool2(280 - 24, 280, (uint32_t)(0x20534C53ULL), 256);
    if (result != 0) goto loc_00AD31FF;
    goto loc_00AD340D;
loc_00AD31FF:
    *(uint64_t *)(Arg4 + 0x8) = result;
    if (result != 0) goto loc_00AD322D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD3221;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD3279;
loc_00AD3221:
loc_00AD3225:
    goto loc_00AD340D;
loc_00AD322D:
    Arg1 = 0;
loc_00AD3232:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD3253;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3225;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_00AD3225;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00AD3232;
loc_00AD3253:
    if ((Arg3 + 4) < Arg3) goto loc_00AD3225;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00AD32F8;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00AD3279:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4))) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD32AD;
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    Arg3 = (uint32_t)((Arg3 + 4) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD330C;
    if (!sign_flag) goto loc_00AD330E;
    goto loc_00AD340D;
loc_00AD32AD:
    Arg1 = 0;
loc_00AD32B2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD32DB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3225;
    Arg3 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)));
    if (Arg3 < ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) goto loc_00AD3225;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00AD32B2;
loc_00AD32DB:
    if ((Arg3 + 4) < Arg3) goto loc_00AD3225;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) <= Arg1) goto loc_00AD3303;
loc_00AD32F8:
    goto loc_00AD340D;
loc_00AD3303:
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)((uint32_t)(0xC0000023ULL)) = *(uint64_t *)(local_rsi);
loc_00AD330C:
loc_00AD330E:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD3342;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 260)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 260); }
    Arg3 = (uint32_t)(((uint32_t)(0xC0000023ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 260)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD340D;
    Arg3 = 0;
    goto loc_00AD340D;
loc_00AD3342:
    Arg1 = 0;
loc_00AD3347:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD3370;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3225;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD3225;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00AD3347;
loc_00AD3370:
    if ((Arg3 + 4) < Arg3) goto loc_00AD3225;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    Arg3 = 0;
    if ((Arg3 + 260) > Arg1) goto loc_00AD32F8;
    *(uint32_t *)(Arg3) = 256;
loc_00AD33A9:
    *(uint64_t *)(Arg3 + 0x4) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x4 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg3 + 0x4 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x4 + 0x30) = v_xmm1;
    *(uint64_t *)(Arg3 + 0x4 + 0x40) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x4 + 0x50) = v_xmm1;
    *(uint64_t *)(Arg3 + 0x4 + 0x60) = v_xmm0;
    Arg4 = (Arg3 + 4) + (Arg3 + 2 + 126);
    result = (v_stack_m118) + (Arg3 + 2 + 126);
    *(uint64_t *)(Arg4 - 0x10) = v_xmm1;
    Arg1 = (Arg3 + 2) - (1);
    if (condition_is_not_equal) goto loc_00AD33A9;
    goto loc_00AD340D;
loc_00AD33FF:
    goto loc_00AD340D;
loc_00AD3407:
loc_00AD340D:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg3 + 2 + 126, (uint32_t)(0xC0000095ULL), Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD3088&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
