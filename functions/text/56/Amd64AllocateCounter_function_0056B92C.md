# Amd64AllocateCounter

- RVA: `0x0056B92C`–`0x0056BC4E` (길이 `802` bytes)
- VA: `0x000000014056B92C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095AEC`
- 디코드: `216`개 명령, `802/802` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0056B95A` → [HalpAllocateHalCounters](../53/HalpAllocateHalCounters_function_0053FF88.md) (function, `0x0053FF88`)
- `0x0056BB19` → [Amd64CheckCoreEventConstraints](Amd64CheckCoreEventConstraints_function_0056BC54.md) (function, `0x0056BC54`)
- `0x0056BB5F` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0056BBDD` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)

### Direct callers
- [Amd64EnableMonitoring](Amd64EnableMonitoring_function_0056C360.md) at `0x0056C431`

### Static image references
- `0x0056B99C` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056B92C  48 8B C4                        mov rax, rsp
0056B92F  48 89 58 08                     mov qword ptr [rax + 8], rbx
0056B933  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0056B937  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0056B93B  55                              push rbp
0056B93C  56                              push rsi
0056B93D  57                              push rdi
0056B93E  41 54                           push r12
0056B940  41 55                           push r13
0056B942  41 56                           push r14
0056B944  41 57                           push r15
0056B946  48 83 EC 30                     sub rsp, 0x30
0056B94A  4C 8B FA                        mov r15, rdx
0056B94D  C6 40 B8 00                     mov byte ptr [rax - 0x48], 0
0056B951  44 8B E1                        mov r12d, ecx
0056B954  41 C6 01 00                     mov byte ptr [r9], 0
0056B958  33 F6                           xor esi, esi
0056B95A  E8 29 46 FD FF                  call 0x14053ff88
0056B95F  85 C0                           test eax, eax
0056B961  79 0A                           jns 0x14056b96d
0056B963  B8 11 00 00 80                  mov eax, 0x80000011
0056B968  E9 CB 02 00 00                  jmp 0x14056bc38
0056B96D  4D 85 FF                        test r15, r15
0056B970  0F 84 BD 02 00 00               je 0x14056bc33
0056B976  8B 8A 38 01 00 00               mov ecx, dword ptr [rdx + 0x138]
0056B97C  85 C9                           test ecx, ecx
0056B97E  74 14                           je 0x14056b994
0056B980  83 E9 01                        sub ecx, 1
0056B983  74 0A                           je 0x14056b98f
0056B985  83 F9 01                        cmp ecx, 1
0056B988  75 0A                           jne 0x14056b994
0056B98A  8D 71 64                        lea esi, [rcx + 0x64]
0056B98D  EB 05                           jmp 0x14056b994
0056B98F  BE 64 00 00 00                  mov esi, 0x64
0056B994  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0056B99C  4C 8D 15 5D 46 A9 FF            lea r10, [rip - 0x56b9a3]
0056B9A3  44 8B C8                        mov r9d, eax
0056B9A6  8B CE                           mov ecx, esi
0056B9A8  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0056B9AD  49 8B 84 C2 40 8C FC 00         mov rax, qword ptr [r10 + rax*8 + 0xfc8c40]
0056B9B5  48 8B 68 58                     mov rbp, qword ptr [rax + 0x58]
0056B9B9  85 F6                           test esi, esi
0056B9BB  74 23                           je 0x14056b9e0
0056B9BD  83 E9 01                        sub ecx, 1
0056B9C0  74 1A                           je 0x14056b9dc
0056B9C2  83 E9 63                        sub ecx, 0x63
0056B9C5  74 0F                           je 0x14056b9d6
0056B9C7  83 F9 01                        cmp ecx, 1
0056B9CA  74 04                           je 0x14056b9d0
0056B9CC  33 ED                           xor ebp, ebp
0056B9CE  EB 10                           jmp 0x14056b9e0
0056B9D0  48 83 C5 48                     add rbp, 0x48
0056B9D4  EB 0A                           jmp 0x14056b9e0
0056B9D6  48 83 C5 30                     add rbp, 0x30
0056B9DA  EB 04                           jmp 0x14056b9e0
0056B9DC  48 83 C5 18                     add rbp, 0x18
0056B9E0  48 8B 7D 10                     mov rdi, qword ptr [rbp + 0x10]
0056B9E4  45 33 ED                        xor r13d, r13d
0056B9E7  44 8B 45 04                     mov r8d, dword ptr [rbp + 4]
0056B9EB  45 3B E8                        cmp r13d, r8d
0056B9EE  0F 83 2C 02 00 00               jae 0x14056bc20
0056B9F4  8D 46 9C                        lea eax, [rsi - 0x64]
0056B9F7  83 F8 01                        cmp eax, 1
0056B9FA  77 73                           ja 0x14056ba6f
0056B9FC  41 83 FC 01                     cmp r12d, 1
0056BA00  0F 85 48 01 00 00               jne 0x14056bb4e
0056BA06  33 C9                           xor ecx, ecx
0056BA08  41 3B C8                        cmp ecx, r8d
0056BA0B  73 62                           jae 0x14056ba6f
0056BA0D  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0056BA11  48 03 D2                        add rdx, rdx
0056BA14  8B 44 D7 24                     mov eax, dword ptr [rdi + rdx*8 + 0x24]
0056BA18  41 39 07                        cmp dword ptr [r15], eax
0056BA1B  74 04                           je 0x14056ba21
0056BA1D  FF C1                           inc ecx
0056BA1F  EB E7                           jmp 0x14056ba08
0056BA21  48 8B 54 D7 10                  mov rdx, qword ptr [rdi + rdx*8 + 0x10]
0056BA26  0F 0D 4A 10                     prefetchw byte ptr [rdx + 0x10]
0056BA2A  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0056BA2E  4C 8D 40 01                     lea r8, [rax + 1]
0056BA32  49 83 F8 01                     cmp r8, 1
0056BA36  76 2E                           jbe 0x14056ba66
0056BA38  F0 4C 0F B1 42 10               lock cmpxchg qword ptr [rdx + 0x10], r8
0056BA3E  75 EE                           jne 0x14056ba2e
0056BA40  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0056BA48  89 08                           mov dword ptr [rax], ecx
0056BA4A  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0056BA52  89 30                           mov dword ptr [rax], esi
0056BA54  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0056BA5C  C6 00 01                        mov byte ptr [rax], 1
0056BA5F  33 C0                           xor eax, eax
0056BA61  E9 D2 01 00 00                  jmp 0x14056bc38
0056BA66  74 07                           je 0x14056ba6f
0056BA68  B9 0E 00 00 00                  mov ecx, 0xe
0056BA6D  CD 29                           int 0x29
0056BA6F  4A 8D 1C 6D 00 00 00 00         lea rbx, [r13*2]
0056BA77  49 03 DD                        add rbx, r13
0056BA7A  48 03 DB                        add rbx, rbx
0056BA7D  83 7C DF 18 03                  cmp dword ptr [rdi + rbx*8 + 0x18], 3
0056BA82  0F 85 BE 00 00 00               jne 0x14056bb46
0056BA88  33 D2                           xor edx, edx
0056BA8A  8B CE                           mov ecx, esi
0056BA8C  83 E9 01                        sub ecx, 1
0056BA8F  74 36                           je 0x14056bac7
0056BA91  83 E9 63                        sub ecx, 0x63
0056BA94  74 1A                           je 0x14056bab0
0056BA96  83 F9 01                        cmp ecx, 1
0056BA99  75 42                           jne 0x14056badd
0056BA9B  4B 8B 84 CA 40 8C FC 00         mov rax, qword ptr [r10 + r9*8 + 0xfc8c40]
0056BAA3  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
0056BAA7  48 83 C2 30                     add rdx, 0x30
0056BAAB  74 03                           je 0x14056bab0
0056BAAD  8B 52 04                        mov edx, dword ptr [rdx + 4]
0056BAB0  4B 8B 84 CA 40 8C FC 00         mov rax, qword ptr [r10 + r9*8 + 0xfc8c40]
0056BAB8  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056BABC  48 83 C0 18                     add rax, 0x18
0056BAC0  74 03                           je 0x14056bac5
0056BAC2  8B 40 04                        mov eax, dword ptr [rax + 4]
0056BAC5  03 D0                           add edx, eax
0056BAC7  4B 8B 84 CA 40 8C FC 00         mov rax, qword ptr [r10 + r9*8 + 0xfc8c40]
0056BACF  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056BAD3  48 85 C0                        test rax, rax
0056BAD6  74 03                           je 0x14056badb
0056BAD8  8B 40 04                        mov eax, dword ptr [rax + 4]
0056BADB  03 D0                           add edx, eax
0056BADD  42 8D 04 2A                     lea eax, [rdx + r13]
0056BAE1  41 8B 8C 82 40 F9 F8 00         mov ecx, dword ptr [r10 + rax*4 + 0xf8f940]
0056BAE9  0F 32                           rdmsr
0056BAEB  48 C1 E2 20                     shl rdx, 0x20
0056BAEF  48 B9 FF 00 40 00 0F 00 00 00   movabs rcx, 0xf004000ff
0056BAF9  48 0B C2                        or rax, rdx
0056BAFC  48 85 C1                        test rcx, rax
0056BAFF  75 45                           jne 0x14056bb46
0056BB01  4D 8D B7 30 01 00 00            lea r14, [r15 + 0x130]
0056BB08  85 F6                           test esi, esi
0056BB0A  75 24                           jne 0x14056bb30
0056BB0C  4D 8B 06                        mov r8, qword ptr [r14]
0056BB0F  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0056BB14  33 D2                           xor edx, edx
0056BB16  41 8B CD                        mov ecx, r13d
0056BB19  E8 36 01 00 00                  call 0x14056bc54
0056BB1E  84 C0                           test al, al
0056BB20  75 36                           jne 0x14056bb58
0056BB22  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0056BB27  4C 8D 15 D2 44 A9 FF            lea r10, [rip - 0x56bb2e]
0056BB2E  EB 16                           jmp 0x14056bb46
0056BB30  8D 46 9C                        lea eax, [rsi - 0x64]
0056BB33  83 F8 01                        cmp eax, 1
0056BB36  77 20                           ja 0x14056bb58
0056BB38  B8 03 00 00 00                  mov eax, 3
0056BB3D  F0 44 0F B1 64 DF 18            lock cmpxchg dword ptr [rdi + rbx*8 + 0x18], r12d
0056BB44  74 12                           je 0x14056bb58
0056BB46  41 FF C5                        inc r13d
0056BB49  E9 99 FE FF FF                  jmp 0x14056b9e7
0056BB4E  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0056BB53  E9 E0 00 00 00                  jmp 0x14056bc38
0056BB58  33 C9                           xor ecx, ecx
0056BB5A  C6 44 DF 28 00                  mov byte ptr [rdi + rbx*8 + 0x28], 0
0056BB5F  E8 7C 2C E1 FF                  call 0x14037e7e0
0056BB64  48 89 44 DF 08                  mov qword ptr [rdi + rbx*8 + 8], rax
0056BB69  44 89 64 DF 18                  mov dword ptr [rdi + rbx*8 + 0x18], r12d
0056BB6E  41 83 FC 02                     cmp r12d, 2
0056BB72  75 18                           jne 0x14056bb8c
0056BB74  48 8B 44 DF 10                  mov rax, qword ptr [rdi + rbx*8 + 0x10]
0056BB79  48 83 24 DF 00                  and qword ptr [rdi + rbx*8], 0
0056BB7E  C7 44 DF 24 18 00 00 00         mov dword ptr [rdi + rbx*8 + 0x24], 0x18
0056BB86  48 83 20 00                     and qword ptr [rax], 0
0056BB8A  EB 7A                           jmp 0x14056bc06
0056BB8C  41 8B 07                        mov eax, dword ptr [r15]
0056BB8F  48 8B 4C DF 10                  mov rcx, qword ptr [rdi + rbx*8 + 0x10]
0056BB94  89 44 DF 24                     mov dword ptr [rdi + rbx*8 + 0x24], eax
0056BB98  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
0056BB9C  48 89 04 DF                     mov qword ptr [rdi + rbx*8], rax
0056BBA0  49 8B 06                        mov rax, qword ptr [r14]
0056BBA3  48 89 01                        mov qword ptr [rcx], rax
0056BBA6  8D 46 9C                        lea eax, [rsi - 0x64]
0056BBA9  83 F8 01                        cmp eax, 1
0056BBAC  77 0D                           ja 0x14056bbbb
0056BBAE  48 8B 44 DF 10                  mov rax, qword ptr [rdi + rbx*8 + 0x10]
0056BBB3  48 C7 40 10 01 00 00 00         mov qword ptr [rax + 0x10], 1
0056BBBB  80 7C 24 20 00                  cmp byte ptr [rsp + 0x20], 0
0056BBC0  74 44                           je 0x14056bc06
0056BBC2  48 8B 44 DF 10                  mov rax, qword ptr [rdi + rbx*8 + 0x10]
0056BBC7  33 C9                           xor ecx, ecx
0056BBC9  C6 40 08 01                     mov byte ptr [rax + 8], 1
0056BBCD  41 8D 45 01                     lea eax, [r13 + 1]
0056BBD1  48 8D 1C 40                     lea rbx, [rax + rax*2]
0056BBD5  48 03 DB                        add rbx, rbx
0056BBD8  C6 44 DF 28 00                  mov byte ptr [rdi + rbx*8 + 0x28], 0
0056BBDD  E8 FE 2B E1 FF                  call 0x14037e7e0
0056BBE2  48 89 44 DF 08                  mov qword ptr [rdi + rbx*8 + 8], rax
0056BBE7  48 B9 FF 00 00 00 0F 00 00 00   movabs rcx, 0xf000000ff
0056BBF1  48 8B 44 DF 10                  mov rax, qword ptr [rdi + rbx*8 + 0x10]
0056BBF6  44 89 64 DF 18                  mov dword ptr [rdi + rbx*8 + 0x18], r12d
0056BBFB  C7 44 DF 24 21 00 00 00         mov dword ptr [rdi + rbx*8 + 0x24], 0x21
0056BC03  48 89 08                        mov qword ptr [rax], rcx
0056BC06  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0056BC0E  44 89 28                        mov dword ptr [rax], r13d
0056BC11  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0056BC19  89 30                           mov dword ptr [rax], esi
0056BC1B  E9 3F FE FF FF                  jmp 0x14056ba5f
0056BC20  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0056BC29  F0 83 40 60 FE                  lock add dword ptr [rax + 0x60], -2
0056BC2E  E9 30 FD FF FF                  jmp 0x14056b963
0056BC33  B8 0D 00 00 C0                  mov eax, 0xc000000d
0056BC38  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0056BC3D  48 83 C4 30                     add rsp, 0x30
0056BC41  41 5F                           pop r15
0056BC43  41 5E                           pop r14
0056BC45  41 5D                           pop r13
0056BC47  41 5C                           pop r12
0056BC49  5F                              pop rdi
0056BC4A  5E                              pop rsi
0056BC4B  5D                              pop rbp
0056BC4C  C3                              ret
0056BC4D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64AllocateCounter(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(v_rsp - 72) = 0;
    *(unsigned __int8 *)(a4) = 0;
    v_rsi = 0;
    result = HalpAllocateHalCounters(a1, a2, a3, a4);
    if (!sign_flag) goto loc_0056B96D;
loc_0056B963:
    goto loc_0056BC38;
loc_0056B96D:
    if (a2 == 0) goto loc_0056BC33;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 312))) == 0) goto loc_0056B994;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 312))) - (1));
    if (condition_is_equal) goto loc_0056B98F;
    if (a1 != 1) goto loc_0056B994;
    goto loc_0056B994;
loc_0056B98F:
loc_0056B994:
    v_stack_m40 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))));
    if (100 == 0) goto loc_0056B9E0;
    a1 = (unsigned int)((100) - (1));
    if (condition_is_equal) goto loc_0056B9DC;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056B9D6;
    if (a1 == 1) goto loc_0056B9D0;
    v_rbp = 0;
    goto loc_0056B9E0;
loc_0056B9D0:
    v_rbp = (v_rbp) + (72);
    goto loc_0056B9E0;
loc_0056B9D6:
    v_rbp = (v_rbp) + (48);
    goto loc_0056B9E0;
loc_0056B9DC:
    v_rbp = (v_rbp) + (24);
loc_0056B9E0:
    v_r13 = 0;
loc_0056B9E7:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 4))))) goto loc_0056BC20;
    if (((unsigned int)(100 - 100)) > 1) goto loc_0056BA6F;
    if (((unsigned int)((unsigned int)(a1))) != 1) goto loc_0056BB4E;
    a1 = 0;
loc_0056BA08:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 4))))) goto loc_0056BA6F;
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + a2 * 8 + 36))))) goto loc_0056BA21;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0056BA08;
loc_0056BA21:
loc_0056BA2E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + a2 * 8 + 16) + 16) + 1) <= 1) goto loc_0056BA66;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + a2 * 8 + 16) + 16) + 1) != 1) goto loc_0056BA2E;
    *(unsigned int *)(v_stack_p18) = a1;
    *(unsigned int *)(a5) = 100;
    *(unsigned __int8 *)(v_stack_p20) = 1;
loc_0056BA5F:
    result = 0;
    goto loc_0056BC38;
loc_0056BA66:
    if (!(condition_is_equal)) {
        a1 = 14;
    }
    v_rbx = (v_r13 * 2) + (0);
    v_rbx = (v_rbx) + (v_rbx);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 24)) != 3) goto loc_0056BB46;
    a2 = 0;
    a1 = (unsigned int)((100) - (1));
    if (condition_is_equal) goto loc_0056BAC7;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056BAB0;
    if (a1 != 1) goto loc_0056BADD;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5683619 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (48);
    if (!(condition_is_equal)) {
        a2 = *(unsigned int *)(a2 + 4);
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5683619 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (24);
    if (!(condition_is_equal)) {
        result = *(unsigned int *)(result + 4);
    }
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
loc_0056BAC7:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5683619 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5683619 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5683619 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) + 4);
    }
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
loc_0056BADD:
    a2 = (a2) << (32);
    result = (a2 + v_r13 * 1) | (a2);
    if ((((unsigned int)(*(unsigned int *)(v_rip - 5683619 + a2 + v_r13 * 1 * 4 + 16316736))) & (result)) != 0) goto loc_0056BB46;
    if (100 != 0) goto loc_0056BB30;
    a2 = 0;
    result = Amd64CheckCoreEventConstraints(0, a2, *(unsigned __int64 *)(a2 + 304), v_stack_m48);
    if ((unsigned __int8)(result) != 0) goto loc_0056BB58;
    goto loc_0056BB46;
loc_0056BB30:
    if (((unsigned int)(100 - 100)) > 1) goto loc_0056BB58;
    if (((unsigned int)(100 - 100)) == 1) goto loc_0056BB58;
loc_0056BB46:
    v_r13 = (unsigned int)((v_r13) + 1);
    goto loc_0056B9E7;
loc_0056BB4E:
    goto loc_0056BC38;
loc_0056BB58:
    a1 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 40) = 0;
    result = KeQueryPerformanceCounter(a1, a2, *(unsigned __int64 *)(a2 + 304), v_stack_m40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 8) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 24) = (unsigned int)((unsigned int)(a1));
    if (((unsigned int)((unsigned int)(a1))) != 2) goto loc_0056BB8C;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 36) = 24;
    goto loc_0056BC06;
loc_0056BB8C:
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8) = (unsigned int)(*(unsigned int *)(a2 + 24));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 16)) = *(unsigned __int64 *)(a2 + 304);
    result = 100 - 100;
    if (((unsigned int)(100 - 100)) <= 1) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 16);
        *(unsigned __int64 *)(result + 16) = 1;
    }
    if (v_stack_m48 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 16);
        a1 = 0;
        *(unsigned __int8 *)(result + 8) = 1;
        result = v_r13 + 1;
        v_rbx = result + result * 2;
        v_rbx = (v_rbx) + (v_rbx);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 40) = 0;
        result = KeQueryPerformanceCounter(a1, a2, *(unsigned __int64 *)(a2 + 304), v_stack_m40);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 8) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 16);
        *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 24) = (unsigned int)((unsigned int)(a1));
        *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 16) + v_rbx * 8 + 36) = 33;
        *(unsigned __int64 *)(result) = 0;
    }
    *(unsigned int *)(v_stack_p18) = (unsigned int)(v_r13);
    *(unsigned int *)(a5) = 100;
    goto loc_0056BA5F;
loc_0056BC20:
    goto loc_0056B963;
loc_0056BC33:
loc_0056BC38:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t Amd64AllocateCounter(int32_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(local_rsp - 0x48) = 0;
    *(uint8_t *)(arg4) = 0;
    local_rsi = 0;
    result = HalpAllocateHalCounters(Arg1, Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_0056B96D;
loc_0056B963:
    goto loc_0056BC38;
loc_0056B96D:
    if (Arg2 == 0) goto loc_0056BC33;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x138))) == 0) goto loc_0056B994;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x138))) - (1));
    if (condition_is_equal) goto loc_0056B98F;
    if (Arg1 != 1) goto loc_0056B994;
    goto loc_0056B994;
loc_0056B98F:
loc_0056B994:
    v_stack_m40 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))));
    if (100 == 0) goto loc_0056B9E0;
    Arg1 = (uint32_t)((100) - (1));
    if (condition_is_equal) goto loc_0056B9DC;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056B9D6;
    if (Arg1 == 1) goto loc_0056B9D0;
    local_rbp = 0;
    goto loc_0056B9E0;
loc_0056B9D0:
    local_rbp = (local_rbp) + (72);
    goto loc_0056B9E0;
loc_0056B9D6:
    local_rbp = (local_rbp) + (48);
    goto loc_0056B9E0;
loc_0056B9DC:
    local_rbp = (local_rbp) + (24);
loc_0056B9E0:
    local_r13 = 0;
loc_0056B9E7:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x4))))) goto loc_0056BC20;
    if (((uint32_t)(100 - 100)) > 1) goto loc_0056BA6F;
    if (((uint32_t)((uint32_t)(Arg1))) != 1) goto loc_0056BB4E;
    Arg1 = 0;
loc_0056BA08:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x4))))) goto loc_0056BA6F;
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if ((*(uint32_t *)(Arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + Arg2 * 8 + 0x24))))) goto loc_0056BA21;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0056BA08;
loc_0056BA21:
loc_0056BA2E:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + Arg2 * 8 + 0x10) + 0x10) + 1) <= 1) goto loc_0056BA66;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + Arg2 * 8 + 0x10) + 0x10) + 1) != 1) goto loc_0056BA2E;
    *(uint32_t *)(v_stack_p18) = Arg1;
    *(uint32_t *)(arg5) = 100;
    *(uint8_t *)(v_stack_p20) = 1;
loc_0056BA5F:
    result = 0;
    goto loc_0056BC38;
loc_0056BA66:
    if (!(condition_is_equal)) {
        Arg1 = 14;
    }
    local_rbx = (local_r13 * 2) + (0);
    local_rbx = (local_rbx) + (local_rbx);
    if ((*(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x18)) != 3) goto loc_0056BB46;
    Arg2 = 0;
    Arg1 = (uint32_t)((100) - (1));
    if (condition_is_equal) goto loc_0056BAC7;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056BAB0;
    if (Arg1 != 1) goto loc_0056BADD;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56B9A3 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (!(condition_is_equal)) {
        Arg2 = *(uint32_t *)(Arg2 + 0x4);
    }
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56B9A3 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (!(condition_is_equal)) {
        result = *(uint32_t *)(result + 0x4);
    }
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
loc_0056BAC7:
    result = *(uint64_t *)(*(uint64_t *)(v_rip - 0x56B9A3 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58);
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56B9A3 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56B9A3 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
loc_0056BADD:
    Arg2 = (Arg2) << (32);
    result = (Arg2 + local_r13 * 1) | (Arg2);
    if ((((uint32_t)(*(uint32_t *)(v_rip - 0x56B9A3 + Arg2 + local_r13 * 1 * 4 + 0xF8F940))) & (result)) != 0) goto loc_0056BB46;
    if (100 != 0) goto loc_0056BB30;
    Arg2 = 0;
    result = Amd64CheckCoreEventConstraints(0, Arg2, *(uint64_t *)(Arg2 + 0x130), v_stack_m48);
    if ((uint8_t)(result) != 0) goto loc_0056BB58;
    goto loc_0056BB46;
loc_0056BB30:
    if (((uint32_t)(100 - 100)) > 1) goto loc_0056BB58;
    if (((uint32_t)(100 - 100)) == 1) goto loc_0056BB58;
loc_0056BB46:
    local_r13 = (uint32_t)((local_r13) + 1);
    goto loc_0056B9E7;
loc_0056BB4E:
    goto loc_0056BC38;
loc_0056BB58:
    Arg1 = 0;
    *(uint8_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x28) = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, *(uint64_t *)(Arg2 + 0x130), v_stack_m40);
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x8) = result;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x18) = (uint32_t)((uint32_t)(Arg1));
    if (((uint32_t)((uint32_t)(Arg1))) != 2) goto loc_0056BB8C;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x24) = 24;
    goto loc_0056BC06;
loc_0056BB8C:
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2)));
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8) = (uint32_t)(*(uint32_t *)(Arg2 + 0x18));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x10)) = *(uint64_t *)(Arg2 + 0x130);
    result = 100 - 100;
    if (((uint32_t)(100 - 100)) <= 1) {
        result = *(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x10);
        *(uint64_t *)(result + 0x10) = 1;
    }
    if (v_stack_m48 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x10);
        Arg1 = 0;
        *(uint8_t *)(result + 0x8) = 1;
        result = local_r13 + 1;
        local_rbx = result + result * 2;
        local_rbx = (local_rbx) + (local_rbx);
        *(uint8_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x28) = 0;
        result = KeQueryPerformanceCounter(Arg1, Arg2, *(uint64_t *)(Arg2 + 0x130), v_stack_m40);
        *(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x8) = result;
        result = *(uint64_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x10);
        *(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x18) = (uint32_t)((uint32_t)(Arg1));
        *(uint32_t *)(*(uint64_t *)(local_rbp + 0x10) + local_rbx * 8 + 0x24) = 33;
        *(uint64_t *)(result) = 0;
    }
    *(uint32_t *)(v_stack_p18) = (uint32_t)(local_r13);
    *(uint32_t *)(arg5) = 100;
    goto loc_0056BA5F;
loc_0056BC20:
    goto loc_0056B963;
loc_0056BC33:
loc_0056BC38:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `8` | `W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056B92C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
