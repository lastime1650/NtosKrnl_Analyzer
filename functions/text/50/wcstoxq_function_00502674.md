# wcstoxq

- RVA: `0x00502674`–`0x005028C8` (길이 `596` bytes)
- VA: `0x0000000140502674`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097FE8`
- 디코드: `190`개 명령, `596/596` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005026DE` → [iswctype_l](iswctype_l_function_005028D0.md) (function, `0x005028D0`)
- `0x00502733` → [wchartodigit](wchartodigit_function_005042EC.md) (function, `0x005042EC`)
- `0x0050276A` → [wchartodigit](wchartodigit_function_005042EC.md) (function, `0x005042EC`)
- `0x0050279A` → [wchartodigit](wchartodigit_function_005042EC.md) (function, `0x005042EC`)
- `0x005028AB` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)

### Direct callers
- [wcstoi64](wcstoi64_function_00502644.md) at `0x00502663`
- [RtlUnicodeStringToInt64](../../page/78/RtlUnicodeStringToInt64_function_0078F7E0.md) at `0x0078F893`
- [LocalpConvertStringSidToSid](../../page/A1/LocalpConvertStringSidToSid_function_00A17490.md) at `0x00A175CD`
- [LocalGetRelativeAttributeForString](../../page/AC/LocalGetRelativeAttributeForString_function_00AC74E4.md) at `0x00AC7A38`
- [LocalGetRelativeAttributeForString](../../page/AC/LocalGetRelativeAttributeForString_function_00AC74E4.md) at `0x00AC7AFC`
- [LocalGetRelativeAttributeForString](../../page/AC/LocalGetRelativeAttributeForString_function_00AC74E4.md) at `0x00AC7F09`
- [LocalGetRelativeAttributeForString](../../page/AC/LocalGetRelativeAttributeForString_function_00AC74E4.md) at `0x00AC7FAB`
- [sub_00B32FE4](../../page/B3/Unknown_function_00B32FE4.md) at `0x00B33371`
- [sub_00B32FE4](../../page/B3/Unknown_function_00B32FE4.md) at `0x00B333D4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00502674  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00502679  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0050267E  55                              push rbp
0050267F  56                              push rsi
00502680  57                              push rdi
00502681  41 54                           push r12
00502683  41 55                           push r13
00502685  41 56                           push r14
00502687  41 57                           push r15
00502689  48 83 EC 30                     sub rsp, 0x30
0050268D  45 8B F1                        mov r14d, r9d
00502690  4D 8B F8                        mov r15, r8
00502693  4C 8B E2                        mov r12, rdx
00502696  4D 85 C0                        test r8, r8
00502699  74 03                           je 0x14050269e
0050269B  49 89 10                        mov qword ptr [r8], rdx
0050269E  4D 85 E4                        test r12, r12
005026A1  0F 84 F4 01 00 00               je 0x14050289b
005026A7  45 85 F6                        test r14d, r14d
005026AA  74 0D                           je 0x1405026b9
005026AC  41 8D 41 FE                     lea eax, [r9 - 2]
005026B0  83 F8 22                        cmp eax, 0x22
005026B3  0F 87 E2 01 00 00               ja 0x14050289b
005026B9  0F B7 2A                        movzx ebp, word ptr [rdx]
005026BC  48 8D 5A 02                     lea rbx, [rdx + 2]
005026C0  33 FF                           xor edi, edi
005026C2  0F B7 CD                        movzx ecx, bp
005026C5  8D 77 08                        lea esi, [rdi + 8]
005026C8  EB 0F                           jmp 0x1405026d9
005026CA  0F B7 0B                        movzx ecx, word ptr [rbx]
005026CD  48 83 C3 02                     add rbx, 2
005026D1  66 3B CD                        cmp cx, bp
005026D4  74 F4                           je 0x1405026ca
005026D6  0F B7 E9                        movzx ebp, cx
005026D9  45 33 C0                        xor r8d, r8d
005026DC  8B D6                           mov edx, esi
005026DE  E8 ED 01 00 00                  call 0x1405028d0
005026E3  85 C0                           test eax, eax
005026E5  75 E3                           jne 0x1405026ca
005026E7  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
005026EE  66 83 FD 2D                     cmp bp, 0x2d
005026F2  75 05                           jne 0x1405026f9
005026F4  83 CE 02                        or esi, 2
005026F7  EB 06                           jmp 0x1405026ff
005026F9  66 83 FD 2B                     cmp bp, 0x2b
005026FD  75 07                           jne 0x140502706
005026FF  0F B7 2B                        movzx ebp, word ptr [rbx]
00502702  48 83 C3 02                     add rbx, 2
00502706  45 85 F6                        test r14d, r14d
00502709  74 1A                           je 0x140502725
0050270B  41 8D 46 FE                     lea eax, [r14 - 2]
0050270F  83 F8 22                        cmp eax, 0x22
00502712  76 11                           jbe 0x140502725
00502714  4D 85 FF                        test r15, r15
00502717  0F 84 93 01 00 00               je 0x1405028b0
0050271D  4D 89 27                        mov qword ptr [r15], r12
00502720  E9 8B 01 00 00                  jmp 0x1405028b0
00502725  41 BD DF FF 00 00               mov r13d, 0xffdf
0050272B  45 85 F6                        test r14d, r14d
0050272E  75 31                           jne 0x140502761
00502730  0F B7 CD                        movzx ecx, bp
00502733  E8 B4 1B 00 00                  call 0x1405042ec
00502738  85 C0                           test eax, eax
0050273A  74 08                           je 0x140502744
0050273C  41 BE 0A 00 00 00               mov r14d, 0xa
00502742  EB 44                           jmp 0x140502788
00502744  0F B7 03                        movzx eax, word ptr [rbx]
00502747  66 83 E8 58                     sub ax, 0x58
0050274B  66 41 85 C5                     test r13w, ax
0050274F  74 08                           je 0x140502759
00502751  41 BE 08 00 00 00               mov r14d, 8
00502757  EB 2F                           jmp 0x140502788
00502759  41 BE 10 00 00 00               mov r14d, 0x10
0050275F  EB 06                           jmp 0x140502767
00502761  41 83 FE 10                     cmp r14d, 0x10
00502765  75 21                           jne 0x140502788
00502767  0F B7 CD                        movzx ecx, bp
0050276A  E8 7D 1B 00 00                  call 0x1405042ec
0050276F  85 C0                           test eax, eax
00502771  75 15                           jne 0x140502788
00502773  0F B7 03                        movzx eax, word ptr [rbx]
00502776  66 83 E8 58                     sub ax, 0x58
0050277A  66 41 85 C5                     test r13w, ax
0050277E  75 08                           jne 0x140502788
00502780  0F B7 6B 02                     movzx ebp, word ptr [rbx + 2]
00502784  48 83 C3 04                     add rbx, 4
00502788  45 8B EE                        mov r13d, r14d
0050278B  33 D2                           xor edx, edx
0050278D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00502791  49 F7 F5                        div r13
00502794  4C 8B E0                        mov r12, rax
00502797  0F B7 CD                        movzx ecx, bp
0050279A  E8 4D 1B 00 00                  call 0x1405042ec
0050279F  8B C8                           mov ecx, eax
005027A1  83 F8 FF                        cmp eax, -1
005027A4  75 26                           jne 0x1405027cc
005027A6  8D 4D BF                        lea ecx, [rbp - 0x41]
005027A9  66 83 F9 19                     cmp cx, 0x19
005027AD  76 09                           jbe 0x1405027b8
005027AF  8D 45 9F                        lea eax, [rbp - 0x61]
005027B2  66 83 F8 19                     cmp ax, 0x19
005027B6  77 3C                           ja 0x1405027f4
005027B8  0F B7 C5                        movzx eax, bp
005027BB  66 83 ED 61                     sub bp, 0x61
005027BF  66 83 FD 19                     cmp bp, 0x19
005027C3  8D 48 E0                        lea ecx, [rax - 0x20]
005027C6  0F 47 C8                        cmova ecx, eax
005027C9  83 E9 37                        sub ecx, 0x37
005027CC  41 3B CE                        cmp ecx, r14d
005027CF  73 23                           jae 0x1405027f4
005027D1  83 CE 08                        or esi, 8
005027D4  49 3B FC                        cmp rdi, r12
005027D7  72 35                           jb 0x14050280e
005027D9  75 11                           jne 0x1405027ec
005027DB  33 D2                           xor edx, edx
005027DD  44 8B C1                        mov r8d, ecx
005027E0  48 83 C8 FF                     or rax, 0xffffffffffffffff
005027E4  49 F7 F5                        div r13
005027E7  4C 3B C2                        cmp r8, rdx
005027EA  76 25                           jbe 0x140502811
005027EC  83 CE 04                        or esi, 4
005027EF  4D 85 FF                        test r15, r15
005027F2  75 24                           jne 0x140502818
005027F4  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
005027F9  48 83 EB 02                     sub rbx, 2
005027FD  40 F6 C6 08                     test sil, 8
00502801  75 21                           jne 0x140502824
00502803  4D 85 FF                        test r15, r15
00502806  49 0F 45 DC                     cmovne rbx, r12
0050280A  33 FF                           xor edi, edi
0050280C  EB 77                           jmp 0x140502885
0050280E  44 8B C1                        mov r8d, ecx
00502811  49 0F AF FD                     imul rdi, r13
00502815  49 03 F8                        add rdi, r8
00502818  0F B7 2B                        movzx ebp, word ptr [rbx]
0050281B  48 83 C3 02                     add rbx, 2
0050281F  E9 73 FF FF FF                  jmp 0x140502797
00502824  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0050282E  40 F6 C6 04                     test sil, 4
00502832  75 22                           jne 0x140502856
00502834  40 F6 C6 01                     test sil, 1
00502838  75 4B                           jne 0x140502885
0050283A  40 F6 C6 02                     test sil, 2
0050283E  74 11                           je 0x140502851
00502840  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0050284A  48 3B F8                        cmp rdi, rax
0050284D  77 07                           ja 0x140502856
0050284F  EB 34                           jmp 0x140502885
00502851  48 3B F9                        cmp rdi, rcx
00502854  76 2F                           jbe 0x140502885
00502856  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0050285E  48 85 C0                        test rax, rax
00502861  74 06                           je 0x140502869
00502863  C7 00 22 00 00 00               mov dword ptr [rax], 0x22
00502869  40 F6 C6 01                     test sil, 1
0050286D  74 06                           je 0x140502875
0050286F  48 83 CF FF                     or rdi, 0xffffffffffffffff
00502873  EB 10                           jmp 0x140502885
00502875  40 8A C6                        mov al, sil
00502878  24 02                           and al, 2
0050287A  F6 D8                           neg al
0050287C  48 1B FF                        sbb rdi, rdi
0050287F  48 F7 DF                        neg rdi
00502882  48 03 F9                        add rdi, rcx
00502885  4D 85 FF                        test r15, r15
00502888  74 03                           je 0x14050288d
0050288A  49 89 1F                        mov qword ptr [r15], rbx
0050288D  40 F6 C6 02                     test sil, 2
00502891  74 03                           je 0x140502896
00502893  48 F7 DF                        neg rdi
00502896  48 8B C7                        mov rax, rdi
00502899  EB 17                           jmp 0x1405028b2
0050289B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005028A1  45 33 C9                        xor r9d, r9d
005028A4  45 33 C0                        xor r8d, r8d
005028A7  33 D2                           xor edx, edx
005028A9  33 C9                           xor ecx, ecx
005028AB  E8 A0 BC F9 FF                  call 0x14049e550
005028B0  33 C0                           xor eax, eax
005028B2  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
005028B7  48 83 C4 30                     add rsp, 0x30
005028BB  41 5F                           pop r15
005028BD  41 5E                           pop r14
005028BF  41 5D                           pop r13
005028C1  41 5C                           pop r12
005028C3  5F                              pop rdi
005028C4  5E                              pop rsi
005028C5  5D                              pop rbp
005028C6  C3                              ret
005028C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wcstoxq(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (48);
    if (a3 != 0) {
        *(unsigned __int64 *)(a3) = a2;
    }
    if (a2 == 0) goto loc_0050289B;
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) == 0) goto loc_005026B9;
    if (((unsigned int)(a4 - 2)) > 34) goto loc_0050289B;
loc_005026B9:
    v_rdi = 0;
    goto loc_005026D9;
loc_005026CA:
    v_rbx = (a2 + 2) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) == ((unsigned __int16)(*(unsigned __int16 *)(a2)))) goto loc_005026CA;
loc_005026D9:
    a3 = 0;
    result = iswctype_l(*(unsigned __int16 *)(a2 + 2), (unsigned int)((unsigned int)(v_rdi + 8)), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_005026CA;
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) != 45) goto loc_005026F9;
    v_rsi = (unsigned int)(((unsigned int)(a5)) | (2));
    goto loc_005026FF;
loc_005026F9:
    v_rbp = (unsigned __int16)(*(unsigned __int16 *)(a2 + 2));
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) == 43) {
        v_rbp = *(unsigned __int16 *)(v_rbx);
        v_rbx = (v_rbx) + (2);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) == 0) goto loc_00502725;
    if (((unsigned int)((unsigned int)((unsigned int)(a4)) - 2)) <= 34) goto loc_00502725;
    if (0 == 0) goto loc_005028B0;
    *(unsigned __int64 *)(a3) = a2;
    goto loc_005028B0;
loc_00502725:
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) != 0) goto loc_00502761;
    result = wchartodigit((unsigned __int16)(v_rbp), (unsigned int)((unsigned int)(v_rdi + 8)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00502744;
    goto loc_00502788;
loc_00502744:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx)) - (88));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)(result))) == 0) goto loc_00502759;
    goto loc_00502788;
loc_00502759:
    goto loc_00502767;
loc_00502761:
    if (16 != 16) goto loc_00502788;
loc_00502767:
    result = wchartodigit((unsigned __int16)(v_rbp), (unsigned int)((unsigned int)(v_rdi + 8)), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00502788;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx)) - (88));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)(result))) == 0) {
        v_rbp = *(unsigned __int16 *)(v_rbx + 2);
        v_rbx = (v_rbx) + (4);
    }
    a2 = 0;
    result = (result) | (-1);
loc_00502797:
    result = wchartodigit((unsigned __int16)(v_rbp), a2, a3, a4);
    if (((unsigned int)(result)) != -1) goto loc_005027CC;
    if (((unsigned __int16)(v_rbp - 65)) <= 25) goto loc_005027B8;
    if (((unsigned __int16)(v_rbp - 97)) > 25) goto loc_005027F4;
loc_005027B8:
    v_rbp = (unsigned __int16)((v_rbp) - (97));
    a1 = (unsigned __int16)(v_rbp) - 32;
    if (((unsigned __int16)(v_rbp)) > 25) { a1 = (unsigned int)((unsigned __int16)(v_rbp)); }
    a1 = (unsigned int)((a1) - (55));
loc_005027CC:
    if (((unsigned int)(a1)) >= 16) goto loc_005027F4;
    v_rsi = (unsigned int)((v_rsi) | (8));
    if (0 < result) goto loc_0050280E;
    if (0 != result) goto loc_005027EC;
    a2 = 0;
    result = ((unsigned __int16)(v_rbp)) | (-1);
    if (((unsigned int)((unsigned int)(a1))) <= 0) goto loc_00502811;
loc_005027EC:
    v_rsi = (unsigned int)((v_rsi) | (4));
    if (0 != 0) goto loc_00502818;
loc_005027F4:
    v_rbx = (v_rbx) - (2);
    if ((((unsigned __int8)(v_rsi)) & (8)) != 0) goto loc_00502824;
    if (0 != 0) { v_rbx = v_stack_p10; }
    v_rdi = 0;
    goto loc_00502885;
loc_0050280E:
loc_00502811:
    v_rdi = (v_rdi) * (16);
    v_rdi = (v_rdi) + ((unsigned int)((unsigned int)(a1)));
loc_00502818:
    v_rbx = (v_rbx) + (2);
    goto loc_00502797;
loc_00502824:
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_00502856;
    if ((((unsigned __int8)(v_rsi)) & (1)) != 0) goto loc_00502885;
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_00502851;
    if (v_rdi > result) goto loc_00502856;
    goto loc_00502885;
loc_00502851:
    if (v_rdi <= a1) goto loc_00502885;
loc_00502856:
    if (a6 != 0) {
        *(unsigned int *)(a6) = 34;
    }
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_00502875;
    v_rdi = (v_rdi) | (-1);
    goto loc_00502885;
loc_00502875:
    result = (unsigned __int8)(((unsigned __int8)(v_rsi)) & (2));
    result = (unsigned __int8)(-(result));
    v_rdi = -(v_rdi);
    v_rdi = (v_rdi) + (a1);
loc_00502885:
    if (0 != 0) {
        *(unsigned __int64 *)(a3) = v_rbx;
    }
    if ((((unsigned __int8)(v_rsi)) & (2)) != 0) {
        v_rdi = -(v_rdi);
    }
    goto loc_005028B2;
loc_0050289B:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
loc_005028B0:
    result = 0;
loc_005028B2:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t wcstoxq(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (48);
    if (Arg3 != 0) {
        *(void **)(Arg3) = Arg2;
    }
    if (Arg2 == NULL) goto loc_0050289B;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg4))) == 0) goto loc_005026B9;
    if (((uint32_t)(Arg4 - 2)) > 34) goto loc_0050289B;
loc_005026B9:
    local_rdi = 0;
    goto loc_005026D9;
loc_005026CA:
    local_rbx = (Arg2 + 2) + (2);
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x2))) == ((uint16_t)(*(uint16_t *)(arg2)))) goto loc_005026CA;
loc_005026D9:
    Arg3 = 0;
    result = iswctype_l(*(uint16_t *)(arg2 + 0x2), (uint32_t)((uint32_t)(local_rdi + 8)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005026CA;
    if (((uint16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) != 45) goto loc_005026F9;
    local_rsi = (uint32_t)(((uint32_t)(Arg5)) | (2));
    goto loc_005026FF;
loc_005026F9:
    local_rbp = (uint16_t)(*(uint16_t *)(arg2 + 0x2));
    if (((uint16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) == 43) {
        local_rbp = *(uint16_t *)(local_rbx);
        local_rbx = (local_rbx) + (2);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(Arg4))) == 0) goto loc_00502725;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)) - 2)) <= 34) goto loc_00502725;
    if (0 == 0) goto loc_005028B0;
    *(void **)(Arg3) = Arg2;
    goto loc_005028B0;
loc_00502725:
    if ((uint32_t)((uint32_t)((uint32_t)(Arg4))) != 0) goto loc_00502761;
    result = wchartodigit((uint16_t)(local_rbp), (uint32_t)((uint32_t)(local_rdi + 8)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00502744;
    goto loc_00502788;
loc_00502744:
    result = (uint16_t)((*(uint16_t *)(local_rbx)) - (88));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)(result))) == 0) goto loc_00502759;
    goto loc_00502788;
loc_00502759:
    goto loc_00502767;
loc_00502761:
    if (16 != 16) goto loc_00502788;
loc_00502767:
    result = wchartodigit((uint16_t)(local_rbp), (uint32_t)((uint32_t)(local_rdi + 8)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00502788;
    result = (uint16_t)((*(uint16_t *)(local_rbx)) - (88));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)(result))) == 0) {
        local_rbp = *(uint16_t *)(local_rbx + 0x2);
        local_rbx = (local_rbx) + (4);
    }
    Arg2 = 0;
    result = (result) | (-1);
loc_00502797:
    result = wchartodigit((uint16_t)(local_rbp), Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != -1) goto loc_005027CC;
    if (((uint16_t)(local_rbp - 65)) <= 25) goto loc_005027B8;
    if (((uint16_t)(local_rbp - 97)) > 25) goto loc_005027F4;
loc_005027B8:
    local_rbp = (uint16_t)((local_rbp) - (97));
    Arg1 = (uint16_t)(local_rbp) - 32;
    if (((uint16_t)(local_rbp)) > 25) { Arg1 = (uint32_t)((uint16_t)(local_rbp)); }
    Arg1 = (uint32_t)((Arg1) - (55));
loc_005027CC:
    if (((uint32_t)(Arg1)) >= 16) goto loc_005027F4;
    local_rsi = (uint32_t)((local_rsi) | (8));
    if (0 < result) goto loc_0050280E;
    if (0 != result) goto loc_005027EC;
    Arg2 = 0;
    result = ((uint16_t)(local_rbp)) | (-1);
    if (((uint32_t)((uint32_t)(Arg1))) <= 0) goto loc_00502811;
loc_005027EC:
    local_rsi = (uint32_t)((local_rsi) | (4));
    if (0 != 0) goto loc_00502818;
loc_005027F4:
    local_rbx = (local_rbx) - (2);
    if ((((uint8_t)(local_rsi)) & (8)) != 0) goto loc_00502824;
    if (0 != 0) { local_rbx = v_stack_p10; }
    local_rdi = 0;
    goto loc_00502885;
loc_0050280E:
loc_00502811:
    local_rdi = (local_rdi) * (16);
    local_rdi = (local_rdi) + ((uint32_t)((uint32_t)(Arg1)));
loc_00502818:
    local_rbx = (local_rbx) + (2);
    goto loc_00502797;
loc_00502824:
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_00502856;
    if ((((uint8_t)(local_rsi)) & (1)) != 0) goto loc_00502885;
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_00502851;
    if (local_rdi > result) goto loc_00502856;
    goto loc_00502885;
loc_00502851:
    if (local_rdi <= Arg1) goto loc_00502885;
loc_00502856:
    if (Arg6 != 0) {
        *(uint32_t *)(Arg6) = 34;
    }
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_00502875;
    local_rdi = (local_rdi) | (-1);
    goto loc_00502885;
loc_00502875:
    result = (uint8_t)(((uint8_t)(local_rsi)) & (2));
    result = (uint8_t)(-(result));
    local_rdi = -(local_rdi);
    local_rdi = (local_rdi) + (Arg1);
loc_00502885:
    if (0 != 0) {
        *(uint64_t *)(Arg3) = local_rbx;
    }
    if ((((uint8_t)(local_rsi)) & (2)) != 0) {
        local_rdi = -(local_rdi);
    }
    goto loc_005028B2;
loc_0050289B:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
loc_005028B0:
    result = 0;
loc_005028B2:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x2` | `64` | `R` |
| `Arg4` | `- 0x2` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00502674&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
