# MiAddRangeToPartitionTree

- RVA: `0x0069020C`–`0x0069060E` (길이 `1,026` bytes)
- VA: `0x000000014069020C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7A68`
- 디코드: `263`개 명령, `1,026/1,026` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0069032E` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0069037C` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0069041B` → [RtlAvlInsertNodeEx](../26/RtlAvlInsertNodeEx_function_00265790.md) (function, `0x00265790`)
- `0x00690471` → [RtlSetBitsEx](../3B/RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)
- `0x00690555` → [RtlClearBitsEx](../29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)
- `0x006905BB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiAddMdlToPartitionTree](MiAddMdlToPartitionTree_function_00690120.md) at `0x006901EA`
- [MiDuplicatePartitionNodeTree](MiDuplicatePartitionNodeTree_function_00690B54.md) at `0x00690BD2`
- [MiAcquireAddMemoryResources](../../page/7F/MiAcquireAddMemoryResources_function_007F9538.md) at `0x007F95A1`
- [MmRemovePhysicalMemory](../../page/7F/MmRemovePhysicalMemory_function_007FB560.md) at `0x007FB6F6`
- [MiAllocatePartitionPhysicalPages](../../page/80/MiAllocatePartitionPhysicalPages_function_0080C9D4.md) at `0x0080CD91`
- [MiHotAddPartitionMemory](../../page/80/MiHotAddPartitionMemory_function_0080D5B4.md) at `0x0080D6CF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006905BB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069020C  48 8B C4                        mov rax, rsp
0069020F  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00690213  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00690217  48 89 48 08                     mov qword ptr [rax + 8], rcx
0069021B  53                              push rbx
0069021C  55                              push rbp
0069021D  56                              push rsi
0069021E  57                              push rdi
0069021F  41 54                           push r12
00690221  41 55                           push r13
00690223  41 56                           push r14
00690225  41 57                           push r15
00690227  48 83 EC 68                     sub rsp, 0x68
0069022B  33 DB                           xor ebx, ebx
0069022D  0F 57 C0                        xorps xmm0, xmm0
00690230  0F 11 40 98                     movups xmmword ptr [rax - 0x68], xmm0
00690234  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00690239  4D 8B F8                        mov r15, r8
0069023C  48 8B C2                        mov rax, rdx
0069023F  49 B8 00 00 FC FF FF FF FF 3F   movabs r8, 0x3ffffffffffc0000
00690249  49 23 C0                        and rax, r8
0069024C  44 8B EB                        mov r13d, ebx
0069024F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00690254  44 8B E3                        mov r12d, ebx
00690257  49 BE FF FF FF FF FF FF FF 3F   movabs r14, 0x3fffffffffffffff
00690261  49 B8 00 00 00 00 00 00 00 C0   movabs r8, 0xc000000000000000
0069026B  49 23 F0                        and rsi, r8
0069026E  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
00690276  48 0B F0                        or rsi, rax
00690279  49 8D 87 FF FF 03 00            lea rax, [r15 + 0x3ffff]
00690280  48 03 C2                        add rax, rdx
00690283  48 25 00 00 FC FF               and rax, 0xfffffffffffc0000
00690289  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0069028E  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00690293  4D 85 FF                        test r15, r15
00690296  0F 84 58 03 00 00               je 0x1406905f4
0069029C  48 8B 39                        mov rdi, qword ptr [rcx]
0069029F  48 8B EB                        mov rbp, rbx
006902A2  48 85 FF                        test rdi, rdi
006902A5  74 66                           je 0x14069030d
006902A7  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
006902AB  4C 8B C6                        mov r8, rsi
006902AE  48 8B CA                        mov rcx, rdx
006902B1  4D 23 C6                        and r8, r14
006902B4  49 23 CE                        and rcx, r14
006902B7  4C 3B C1                        cmp r8, rcx
006902BA  73 08                           jae 0x1406902c4
006902BC  48 8B EF                        mov rbp, rdi
006902BF  48 8B 3F                        mov rdi, qword ptr [rdi]
006902C2  EB DE                           jmp 0x1406902a2
006902C4  4C 8D 77 20                     lea r14, [rdi + 0x20]
006902C8  49 03 0E                        add rcx, qword ptr [r14]
006902CB  4C 3B C1                        cmp r8, rcx
006902CE  72 10                           jb 0x1406902e0
006902D0  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
006902D4  49 BE FF FF FF FF FF FF FF 3F   movabs r14, 0x3fffffffffffffff
006902DE  EB C2                           jmp 0x1406902a2
006902E0  48 0F BA E2 3E                  bt rdx, 0x3e
006902E5  0F 92 C1                        setb cl
006902E8  41 F6 C1 01                     test r9b, 1
006902EC  0F 95 C0                        setne al
006902EF  84 C8                           test al, cl
006902F1  0F 85 31 01 00 00               jne 0x140690428
006902F7  48 B8 FF FF FF FF FF FF FF BF   movabs rax, 0xbfffffffffffffff
00690301  48 23 D0                        and rdx, rax
00690304  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
00690308  E9 1B 01 00 00                  jmp 0x140690428
0069030D  48 85 ED                        test rbp, rbp
00690310  75 07                           jne 0x140690319
00690312  48 8B 6C 24 28                  mov rbp, qword ptr [rsp + 0x28]
00690317  EB 07                           jmp 0x140690320
00690319  48 8B 6D 18                     mov rbp, qword ptr [rbp + 0x18]
0069031D  49 23 EE                        and rbp, r14
00690320  BA 30 00 00 00                  mov edx, 0x30
00690325  41 B8 4D 69 70 70               mov r8d, 0x7070694d
0069032B  8D 4A 10                        lea ecx, [rdx + 0x10]
0069032E  E8 0D B2 CC FF                  call 0x14035b540
00690333  48 8B F8                        mov rdi, rax
00690336  48 85 C0                        test rax, rax
00690339  0F 84 81 02 00 00               je 0x1406905c0
0069033F  F6 84 24 C8 00 00 00 02         test byte ptr [rsp + 0xc8], 2
00690347  74 0B                           je 0x140690354
00690349  48 8B C6                        mov rax, rsi
0069034C  49 23 C6                        and rax, r14
0069034F  48 2B E8                        sub rbp, rax
00690352  EB 05                           jmp 0x140690359
00690354  BD 00 00 04 00                  mov ebp, 0x40000
00690359  48 8B D3                        mov rdx, rbx
0069035C  40 F6 C5 3F                     test bpl, 0x3f
00690360  48 8B C5                        mov rax, rbp
00690363  B9 40 00 00 00                  mov ecx, 0x40
00690368  0F 95 C2                        setne dl
0069036B  41 B8 4D 69 70 62               mov r8d, 0x6270694d
00690371  48 C1 E8 06                     shr rax, 6
00690375  48 03 D0                        add rdx, rax
00690378  48 C1 E2 03                     shl rdx, 3
0069037C  E8 BF B1 CC FF                  call 0x14035b540
00690381  48 85 C0                        test rax, rax
00690384  0F 84 2C 02 00 00               je 0x1406905b6
0069038A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0069038E  48 8B CE                        mov rcx, rsi
00690391  49 89 46 08                     mov qword ptr [r14 + 8], rax
00690395  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
0069039F  49 89 2E                        mov qword ptr [r14], rbp
006903A2  48 33 4F 18                     xor rcx, qword ptr [rdi + 0x18]
006903A6  48 23 C8                        and rcx, rax
006903A9  48 33 CE                        xor rcx, rsi
006903AC  F6 84 24 C8 00 00 00 01         test byte ptr [rsp + 0xc8], 1
006903B4  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
006903B8  74 11                           je 0x1406903cb
006903BA  48 B8 00 00 00 00 00 00 00 40   movabs rax, 0x4000000000000000
006903C4  48 0B C8                        or rcx, rax
006903C7  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
006903CB  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
006903D3  44 8A C3                        mov r8b, bl
006903D6  49 8B 12                        mov rdx, qword ptr [r10]
006903D9  48 85 D2                        test rdx, rdx
006903DC  74 37                           je 0x140690415
006903DE  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
006903E8  49 23 C8                        and rcx, r8
006903EB  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
006903EF  49 23 C0                        and rax, r8
006903F2  48 3B C8                        cmp rcx, rax
006903F5  73 0D                           jae 0x140690404
006903F7  48 8B 02                        mov rax, qword ptr [rdx]
006903FA  48 85 C0                        test rax, rax
006903FD  75 0E                           jne 0x14069040d
006903FF  44 8A C3                        mov r8b, bl
00690402  EB 11                           jmp 0x140690415
00690404  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00690408  48 85 C0                        test rax, rax
0069040B  74 05                           je 0x140690412
0069040D  48 8B D0                        mov rdx, rax
00690410  EB D9                           jmp 0x1406903eb
00690412  41 B0 01                        mov r8b, 1
00690415  4C 8B CF                        mov r9, rdi
00690418  49 8B CA                        mov rcx, r10
0069041B  E8 70 53 BD FF                  call 0x140265790
00690420  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
00690428  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0069042C  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00690436  48 8B 6F 20                     mov rbp, qword ptr [rdi + 0x20]
0069043A  48 23 C1                        and rax, rcx
0069043D  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00690445  48 2B E9                        sub rbp, rcx
00690448  48 03 E8                        add rbp, rax
0069044B  49 3B EF                        cmp rbp, r15
0069044E  49 0F 47 EF                     cmova rbp, r15
00690452  41 F6 C1 04                     test r9b, 4
00690456  0F 85 14 01 00 00               jne 0x140690570
0069045C  48 8B D1                        mov rdx, rcx
0069045F  4C 8B C5                        mov r8, rbp
00690462  48 2B D0                        sub rdx, rax
00690465  49 8B CE                        mov rcx, r14
00690468  45 85 ED                        test r13d, r13d
0069046B  0F 85 E4 00 00 00               jne 0x140690555
00690471  E8 FA 60 D2 FF                  call 0x1403b6570
00690476  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0069047A  48 B8 FF FF FF FF FF FF FF 3F   movabs rax, 0x3fffffffffffffff
00690484  48 8B CA                        mov rcx, rdx
00690487  48 23 C8                        and rcx, rax
0069048A  48 39 8C 24 C0 00 00 00         cmp qword ptr [rsp + 0xc0], rcx
00690492  75 1C                           jne 0x1406904b0
00690494  48 3B 6F 20                     cmp rbp, qword ptr [rdi + 0x20]
00690498  75 16                           jne 0x1406904b0
0069049A  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
006904A4  48 0B D0                        or rdx, rax
006904A7  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
006904AB  E9 B8 00 00 00                  jmp 0x140690568
006904B0  49 8B 06                        mov rax, qword ptr [r14]
006904B3  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
006904B7  48 85 C0                        test rax, rax
006904BA  0F 84 8E 00 00 00               je 0x14069054e
006904C0  48 83 FA 01                     cmp rdx, 1
006904C4  77 18                           ja 0x1406904de
006904C6  0F 85 82 00 00 00               jne 0x14069054e
006904CC  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
006904D0  48 0F BA 20 00                  bt qword ptr [rax], 0
006904D5  0F 92 C0                        setb al
006904D8  84 C0                           test al, al
006904DA  74 72                           je 0x14069054e
006904DC  EB 62                           jmp 0x140690540
006904DE  48 3B C2                        cmp rax, rdx
006904E1  72 6B                           jb 0x14069054e
006904E3  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
006904E7  4C 8D 52 FF                     lea r10, [rdx - 1]
006904EB  49 8B C2                        mov rax, r10
006904EE  48 C1 E8 06                     shr rax, 6
006904F2  4C 8B 01                        mov r8, qword ptr [rcx]
006904F5  4C 8D 0C C1                     lea r9, [rcx + rax*8]
006904F9  49 3B C9                        cmp rcx, r9
006904FC  75 16                           jne 0x140690514
006904FE  48 83 C8 FF                     or rax, 0xffffffffffffffff
00690502  B9 40 00 00 00                  mov ecx, 0x40
00690507  2A CA                           sub cl, dl
00690509  48 D3 E8                        shr rax, cl
0069050C  4C 23 C0                        and r8, rax
0069050F  4C 3B C0                        cmp r8, rax
00690512  EB 2A                           jmp 0x14069053e
00690514  49 83 F8 FF                     cmp r8, -1
00690518  75 34                           jne 0x14069054e
0069051A  48 83 C1 08                     add rcx, 8
0069051E  48 8B 11                        mov rdx, qword ptr [rcx]
00690521  49 3B C9                        cmp rcx, r9
00690524  74 06                           je 0x14069052c
00690526  48 83 FA FF                     cmp rdx, -1
0069052A  EB EC                           jmp 0x140690518
0069052C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00690530  41 8A CA                        mov cl, r10b
00690533  F6 D1                           not cl
00690535  48 D3 E8                        shr rax, cl
00690538  48 23 D0                        and rdx, rax
0069053B  48 3B D0                        cmp rdx, rax
0069053E  75 0E                           jne 0x14069054e
00690540  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0069054A  48 09 4F 18                     or qword ptr [rdi + 0x18], rcx
0069054E  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00690553  EB 13                           jmp 0x140690568
00690555  E8 E6 71 C0 FF                  call 0x140297740
0069055A  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00690564  48 21 47 18                     and qword ptr [rdi + 0x18], rax
00690568  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
00690570  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
00690578  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
00690582  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0069058A  48 03 FD                        add rdi, rbp
0069058D  48 23 F0                        and rsi, rax
00690590  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
00690598  48 8B C7                        mov rax, rdi
0069059B  49 BE FF FF FF FF FF FF FF 3F   movabs r14, 0x3fffffffffffffff
006905A5  49 23 C6                        and rax, r14
006905A8  4C 2B FD                        sub r15, rbp
006905AB  4C 03 E5                        add r12, rbp
006905AE  48 0B F0                        or rsi, rax
006905B1  E9 D8 FC FF FF                  jmp 0x14069028e
006905B6  33 D2                           xor edx, edx
006905B8  48 8B CF                        mov rcx, rdi
006905BB  E8 B0 22 4F 00                  call 0x140b82870
006905C0  41 BD 01 00 00 00               mov r13d, 1
006905C6  4D 85 E4                        test r12, r12
006905C9  74 25                           je 0x1406905f0
006905CB  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
006905D3  4D 8B FC                        mov r15, r12
006905D6  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
006905DE  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
006905E6  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
006905EB  E9 71 FC FF FF                  jmp 0x140690261
006905F0  33 C0                           xor eax, eax
006905F2  EB 08                           jmp 0x1406905fc
006905F4  45 85 ED                        test r13d, r13d
006905F7  0F 94 C3                        sete bl
006905FA  8B C3                           mov eax, ebx
006905FC  48 83 C4 68                     add rsp, 0x68
00690600  41 5F                           pop r15
00690602  41 5E                           pop r14
00690604  41 5D                           pop r13
00690606  41 5C                           pop r12
00690608  5F                              pop rdi
00690609  5E                              pop rsi
0069060A  5D                              pop rbp
0069060B  5B                              pop rbx
0069060C  C3                              ret
0069060D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddRangeToPartitionTree(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (104);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    result = (a2) & (a3);
    v_stack_m88 = result;
loc_00690261:
    v_rsi = (v_stack_m60) & (a3);
    v_stack_p18 = a2;
    v_rsi = (v_rsi) | (result);
    result = (a3 + 262143) + (a2);
    result = (result) & (0xFFFFFFFFFFFC0000ULL);
    v_stack_m80 = result;
loc_0069028E:
    v_stack_m60 = v_rsi;
    if (a3 == 0) goto loc_006905F4;
loc_006902A2:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_0069030D;
    a3 = (v_rsi) & (v_r14);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) & (v_r14);
    if (a3 >= a1) goto loc_006902C4;
    goto loc_006902A2;
loc_006902C4:
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 32));
    if (a3 < a1) goto loc_006902E0;
    goto loc_006902A2;
loc_006902E0:
    a1 = (a3 < a1) ? 1 : 0;
    result = ((((unsigned __int8)(a4)) & (1)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00690428;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) & (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8) + 24) = a2;
    goto loc_00690428;
loc_0069030D:
    if (*(unsigned __int64 *)(a1) != 0) goto loc_00690319;
    goto loc_00690320;
loc_00690319:
    v_rbp = (*(unsigned __int64 *)(v_stack_m80 + 24)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 32);
loc_00690320:
    result = MiAllocatePool(48 + 16, 48, (unsigned int)(0x7070694DULL), a4);
    if (result == 0) goto loc_006905C0;
    if (((v_stack_p20) & (2)) == 0) goto loc_00690354;
    result = (v_rsi) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 32);
    v_rbp = (v_rbp) - (result);
    goto loc_00690359;
loc_00690354:
loc_00690359:
    a2 = ((((unsigned __int8)((unsigned int)(0x40000ULL))) & (63)) != 0) ? 1 : 0;
    result = ((unsigned int)(0x40000ULL)) >> (6);
    a2 = (a2) + (result);
    a2 = (a2) << (3);
    result = MiAllocatePool(64, a2, (unsigned int)(0x6270694DULL), a4);
    if (result == 0) goto loc_006905B6;
    *(unsigned __int64 *)(result + 32 + 8) = result;
    *(unsigned __int64 *)(result + 32) = (unsigned int)(0x40000ULL);
    a1 = (v_rsi) ^ (*(unsigned __int64 *)(result + 24));
    a1 = (a1) & (result);
    a1 = (a1) ^ (v_rsi);
    *(unsigned __int64 *)(result + 24) = a1;
    if (((v_stack_p20) & (1)) != 0) {
        a1 = (a1) | (result);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    if (*(unsigned __int64 *)(v_stack_p8) == 0) goto loc_00690415;
    a1 = (a1) & (0);
loc_006903EB:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8) + 24)) & (0);
    if (a1 >= result) goto loc_00690404;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)) != 0) goto loc_0069040D;
    goto loc_00690415;
loc_00690404:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8) + 8) == 0) goto loc_00690412;
loc_0069040D:
    goto loc_006903EB;
loc_00690412:
loc_00690415:
    result = RtlAvlInsertNodeEx(v_stack_p8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8) + 8), 1, result);
loc_00690428:
    result = (*(unsigned __int64 *)(result + 24)) & (v_stack_p8);
    v_rbp = (*(unsigned __int64 *)(result + 32)) - (v_stack_p18);
    v_rbp = (v_rbp) + (result);
    if (v_rbp > a3) { v_rbp = a3; }
    if ((((unsigned __int8)((unsigned int)(v_stack_p20))) & (4)) != 0) goto loc_00690570;
    a2 = (v_stack_p18) - (result);
    if (0 != 0) goto loc_00690555;
    result = RtlSetBitsEx(result + 32, a2, v_rbp, (unsigned int)(v_stack_p20));
    a1 = (*(unsigned __int64 *)(result + 24)) & (result);
    if (v_stack_p18 != a1) goto loc_006904B0;
    if (v_rbp != (*(unsigned __int64 *)(result + 32))) goto loc_006904B0;
    a2 = (*(unsigned __int64 *)(result + 24)) | (result);
    *(unsigned __int64 *)(result + 24) = a2;
    goto loc_00690568;
loc_006904B0:
    if (*(unsigned __int64 *)(result + 32) == 0) goto loc_0069054E;
    if ((*(unsigned __int64 *)(result + 32)) > 1) goto loc_006904DE;
    if ((*(unsigned __int64 *)(result + 32)) != 1) goto loc_0069054E;
    result = ((*(unsigned __int64 *)(result + 32)) < 1) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_0069054E;
    goto loc_00690540;
loc_006904DE:
    if (result < (*(unsigned __int64 *)(result + 32))) goto loc_0069054E;
    result = (*(unsigned __int64 *)(result + 32) - 1) >> (6);
    if ((*(unsigned __int64 *)(result + 32 + 8)) != (*(unsigned __int64 *)(result + 32 + 8) + result * 8)) goto loc_00690514;
    result = (result) | (-1);
    a1 = (unsigned __int8)((64) - ((unsigned __int8)(*(unsigned __int64 *)(result + 32))));
    result = (result) >> ((unsigned __int8)(a1));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32 + 8))) & (result);
    goto loc_0069053E;
loc_00690514:
loc_00690518:
    if (a3 != -1) goto loc_0069054E;
    a1 = (a1) + (8);
    if (a1 == (*(unsigned __int64 *)(result + 32 + 8) + result * 8)) goto loc_0069052C;
    goto loc_00690518;
loc_0069052C:
    result = (result) | (-1);
    a1 = (unsigned __int8)(~((unsigned __int8)(*(unsigned __int64 *)(result + 32) - 1)));
    result = (result) >> ((unsigned __int8)(a1));
    a2 = (*(unsigned __int64 *)(a1)) & (result);
loc_0069053E:
    if (a2 == result) {
    }
    goto loc_00690568;
loc_00690555:
    result = RtlClearBitsEx(a1, a2, a3, *(unsigned __int64 *)(result + 32 + 8) + result * 8);
loc_00690568:
loc_00690570:
    v_rdi = (v_stack_p18) + (v_rbp);
    v_rsi = (v_stack_m60) & (result);
    v_stack_p18 = v_rdi;
    result = (v_rdi) & (result + 32);
    v_r15 = (a3) - (v_rbp);
    v_r12 = (0) + (v_rbp);
    v_rsi = (v_rsi) | (result);
    goto loc_0069028E;
loc_006905B6:
    a2 = 0;
    result = ExFreePoolWithTag(v_rdi, a2, a3, (unsigned int)(v_stack_p20));
loc_006905C0:
    if (v_r12 == 0) goto loc_006905F0;
    goto loc_00690261;
loc_006905F0:
    result = 0;
    goto loc_006905FC;
loc_006905F4:
    v_rbx = (1 == 0) ? 1 : 0;
loc_006905FC:
    v_rsp = (v_rsp) + (104);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t MiAddRangeToPartitionTree(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (104);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    result = (Arg2) & (Arg3);
    v_stack_m88 = result;
loc_00690261:
    local_rsi = (v_stack_m60) & (Arg3);
    v_stack_p18 = Arg2;
    local_rsi = (local_rsi) | (result);
    result = (Arg3 + 262143) + (Arg2);
    result = (result) & (0xFFFFFFFFFFFC0000ULL);
    v_stack_m80 = result;
loc_0069028E:
    v_stack_m60 = local_rsi;
    if (Arg3 == 0) goto loc_006905F4;
loc_006902A2:
    if (*(uint64_t *)(Arg1) == 0) goto loc_0069030D;
    Arg3 = (local_rsi) & (local_r14);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg1) + 0x18)) & (local_r14);
    if (Arg3 >= Arg1) goto loc_006902C4;
    goto loc_006902A2;
loc_006902C4:
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1)) + 0x20));
    if (Arg3 < Arg1) goto loc_006902E0;
    goto loc_006902A2;
loc_006902E0:
    Arg1 = (Arg3 < Arg1) ? 1 : 0;
    result = ((((uint8_t)(Arg4)) & (1)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00690428;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(Arg1) + 0x18)) & (result);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1)) + 0x8) + 0x18) = Arg2;
    goto loc_00690428;
loc_0069030D:
    if (*(uint64_t *)(Arg1) != 0) goto loc_00690319;
    goto loc_00690320;
loc_00690319:
    local_rbp = (*(uint64_t *)(v_stack_m80 + 0x18)) & (*(uint64_t *)(*(uint64_t *)(Arg1)) + 32);
loc_00690320:
    result = MiAllocatePool(48 + 16, 48, (uint32_t)(0x7070694DULL), Arg4);
    if (result == 0) goto loc_006905C0;
    if (((v_stack_p20) & (2)) == 0) goto loc_00690354;
    result = (local_rsi) & (*(uint64_t *)(*(uint64_t *)(Arg1)) + 32);
    local_rbp = (local_rbp) - (result);
    goto loc_00690359;
loc_00690354:
loc_00690359:
    Arg2 = ((((uint8_t)((uint32_t)(0x40000ULL))) & (63)) != 0) ? 1 : 0;
    result = ((uint32_t)(0x40000ULL)) >> (6);
    Arg2 = (Arg2) + (result);
    Arg2 = (Arg2) << (3);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x6270694DULL), Arg4);
    if (result == 0) goto loc_006905B6;
    *(uint64_t *)(result + 0x20 + 0x8) = result;
    *(uint64_t *)(result + 0x20) = (uint32_t)(0x40000ULL);
    Arg1 = (local_rsi) ^ (*(uint64_t *)(result + 0x18));
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) ^ (local_rsi);
    *(uint64_t *)(result + 0x18) = Arg1;
    if (((v_stack_p20) & (1)) != 0) {
        Arg1 = (Arg1) | (result);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    if (*(uint64_t *)(v_stack_p8) == 0) goto loc_00690415;
    Arg1 = (Arg1) & (0);
loc_006903EB:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_p8) + 0x18)) & (0);
    if (Arg1 >= result) goto loc_00690404;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8)) != 0) goto loc_0069040D;
    goto loc_00690415;
loc_00690404:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8) + 0x8) == 0) goto loc_00690412;
loc_0069040D:
    goto loc_006903EB;
loc_00690412:
loc_00690415:
    result = RtlAvlInsertNodeEx(v_stack_p8, *(uint64_t *)(*(uint64_t *)(v_stack_p8) + 0x8), 1, result);
loc_00690428:
    result = (*(uint64_t *)(result + 0x18)) & (v_stack_p8);
    local_rbp = (*(uint64_t *)(result + 0x20)) - (v_stack_p18);
    local_rbp = (local_rbp) + (result);
    if (local_rbp > Arg3) { local_rbp = Arg3; }
    if ((((uint8_t)((uint32_t)(v_stack_p20))) & (4)) != 0) goto loc_00690570;
    Arg2 = (v_stack_p18) - (result);
    if (0 != 0) goto loc_00690555;
    result = RtlSetBitsEx(result + 32, Arg2, local_rbp, (uint32_t)(v_stack_p20));
    Arg1 = (*(uint64_t *)(result + 0x18)) & (result);
    if (v_stack_p18 != Arg1) goto loc_006904B0;
    if (local_rbp != (*(uint64_t *)(result + 0x20))) goto loc_006904B0;
    Arg2 = (*(uint64_t *)(result + 0x18)) | (result);
    *(uint64_t *)(result + 0x18) = Arg2;
    goto loc_00690568;
loc_006904B0:
    if (*(uint64_t *)(result + 0x20) == 0) goto loc_0069054E;
    if ((*(uint64_t *)(result + 0x20)) > 1) goto loc_006904DE;
    if ((*(uint64_t *)(result + 0x20)) != 1) goto loc_0069054E;
    result = ((*(uint64_t *)(result + 0x20)) < 1) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_0069054E;
    goto loc_00690540;
loc_006904DE:
    if (result < (*(uint64_t *)(result + 0x20))) goto loc_0069054E;
    result = (*(uint64_t *)(result + 0x20) - 1) >> (6);
    if ((*(uint64_t *)(result + 0x20 + 0x8)) != (*(uint64_t *)(result + 0x20 + 0x8) + result * 8)) goto loc_00690514;
    result = (result) | (-1);
    Arg1 = (uint8_t)((64) - ((uint8_t)(*(uint64_t *)(result + 0x20))));
    result = (result) >> ((uint8_t)(Arg1));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(result + 0x20 + 0x8))) & (result);
    goto loc_0069053E;
loc_00690514:
loc_00690518:
    if (Arg3 != -1) goto loc_0069054E;
    Arg1 = (Arg1) + (8);
    if (Arg1 == (*(uint64_t *)(result + 0x20 + 0x8) + result * 8)) goto loc_0069052C;
    goto loc_00690518;
loc_0069052C:
    result = (result) | (-1);
    Arg1 = (uint8_t)(~((uint8_t)(*(uint64_t *)(result + 0x20) - 1)));
    result = (result) >> ((uint8_t)(Arg1));
    Arg2 = (*(uint64_t *)(Arg1)) & (result);
loc_0069053E:
    if (Arg2 == result) {
    }
    goto loc_00690568;
loc_00690555:
    result = RtlClearBitsEx(Arg1, Arg2, Arg3, *(uint64_t *)(result + 0x20 + 0x8) + result * 8);
loc_00690568:
loc_00690570:
    local_rdi = (v_stack_p18) + (local_rbp);
    local_rsi = (v_stack_m60) & (result);
    v_stack_p18 = local_rdi;
    result = (local_rdi) & (result + 32);
    local_r15 = (Arg3) - (local_rbp);
    local_r12 = (0) + (local_rbp);
    local_rsi = (local_rsi) | (result);
    goto loc_0069028E;
loc_006905B6:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rdi, Arg2, Arg3, (uint32_t)(v_stack_p20));
loc_006905C0:
    if (local_r12 == 0) goto loc_006905F0;
    goto loc_00690261;
loc_006905F0:
    result = 0;
    goto loc_006905FC;
loc_006905F4:
    local_rbx = (1 == 0) ? 1 : 0;
loc_006905FC:
    local_rsp = (local_rsp) + (104);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069020C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
