# MiDbgTranslatePhysicalAddress

- RVA: `0x00685760`–`0x00685AEF` (길이 `911` bytes)
- VA: `0x0000000140685760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE7D0`
- 디코드: `257`개 명령, `911/911` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x006857A3` → [MiCheckPhysicalAddressRange](../22/MiCheckPhysicalAddressRange_function_00228474.md) (function, `0x00228474`)
- `0x00685817` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x006858C6` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x006858E0` → [MiDbgPatchIdentity](MiDbgPatchIdentity_function_00685470.md) (function, `0x00685470`)
- `0x0068592C` → [MiMakeProtectionPfnCompatible](../22/MiMakeProtectionPfnCompatible_function_00229CD0.md) (function, `0x00229CD0`)
- `0x00685971` → [MiFreezeIoPfnNode](../67/MiFreezeIoPfnNode_function_0067BDAC.md) (function, `0x0067BDAC`)
- `0x00685988` → [MiFreezeIoPfnNode](../67/MiFreezeIoPfnNode_function_0067BDAC.md) (function, `0x0067BDAC`)
- `0x00685A84` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00685AB7` → [KeFlushSingleTb](../5B/KeFlushSingleTb_function_005BDE84.md) (function, `0x005BDE84`)
- `0x00685ABE` → [KeFlushSingleCurrentTb](../5B/KeFlushSingleCurrentTb_function_005BDC9C.md) (function, `0x005BDC9C`)
- `0x00685AD2` → [MiDbgUnTranslatePhysicalAddress](MiDbgUnTranslatePhysicalAddress_function_00685AF8.md) (function, `0x00685AF8`)

### Direct callers
- [MiDbgCopyMemory](MiDbgCopyMemory_function_00684A18.md) at `0x00684B0B`
- [MiDbgCopyMemory](MiDbgCopyMemory_function_00684A18.md) at `0x00684CA4`
- [MiDbgPteWriteInProgress](MiDbgPteWriteInProgress_function_00685528.md) at `0x00685606`

### Static image references
- `0x00685774` → RVA `0x00E302D8` (`.data`; read)
- `0x0068578E` → RVA `0x00E302D0` (`.data`; read)
- `0x00685808` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00685833` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00685898` → RVA `0x00F4754C` (`.data`; read)
- `0x006858A6` → RVA `0x00E302E0` (`.data`; read/write)
- `0x006859A3` → RVA `0x00E2DC38` (`.data`; read)
- `0x00685A92` → RVA `0x00E302C8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00685760  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00685765  55                              push rbp
00685766  56                              push rsi
00685767  57                              push rdi
00685768  41 54                           push r12
0068576A  41 55                           push r13
0068576C  41 56                           push r14
0068576E  41 57                           push r15
00685770  48 83 EC 30                     sub rsp, 0x30
00685774  4C 8B 25 5D AB 7A 00            mov r12, qword ptr [rip + 0x7aab5d]
0068577B  8B EA                           mov ebp, edx
0068577D  41 BA 04 00 00 00               mov r10d, 4
00685783  4D 8B F8                        mov r15, r8
00685786  41 23 EA                        and ebp, r10d
00685789  8B FA                           mov edi, edx
0068578B  48 8B D9                        mov rbx, rcx
0068578E  4C 0F 45 25 3A AB 7A 00         cmovne r12, qword ptr [rip + 0x7aab3a]
00685796  4D 85 E4                        test r12, r12
00685799  0F 84 38 03 00 00               je 0x140685ad7
0068579F  41 8D 52 FD                     lea edx, [r10 - 3]
006857A3  E8 CC 2C BA FF                  call 0x140228474
006857A8  85 C0                           test eax, eax
006857AA  0F 84 27 03 00 00               je 0x140685ad7
006857B0  4D 8B EC                        mov r13, r12
006857B3  49 C1 E5 19                     shl r13, 0x19
006857B7  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
006857C1  48 C1 E0 19                     shl rax, 0x19
006857C5  49 8D 57 28                     lea rdx, [r15 + 0x28]
006857C9  4C 2B E8                        sub r13, rax
006857CC  48 C1 E9 0C                     shr rcx, 0xc
006857D0  49 C1 FD 10                     sar r13, 0x10
006857D4  45 8D 42 FE                     lea r8d, [r10 - 2]
006857D8  8B C7                           mov eax, edi
006857DA  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
006857DF  24 40                           and al, 0x40
006857E1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006857E6  F6 D8                           neg al
006857E8  1B F6                           sbb esi, esi
006857EA  41 83 27 00                     and dword ptr [r15], 0
006857EE  48 83 22 00                     and qword ptr [rdx], 0
006857F2  83 E6 03                        and esi, 3
006857F5  FF C6                           inc esi
006857F7  85 ED                           test ebp, ebp
006857F9  74 05                           je 0x140685800
006857FB  41 B6 11                        mov r14b, 0x11
006857FE  EB 2F                           jmp 0x14068582f
00685800  45 0F 20 C6                     mov r14, cr8
00685804  45 0F 22 C0                     mov cr8, r8
00685808  83 3D 11 15 94 00 00            cmp dword ptr [rip + 0x941511], 0
0068580F  74 1E                           je 0x14068582f
00685811  41 8A D0                        mov dl, r8b
00685814  41 8A CE                        mov cl, r14b
00685817  E8 E0 FE E6 FF                  call 0x1404f56fc
0068581C  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00685821  49 8D 57 28                     lea rdx, [r15 + 0x28]
00685825  41 BA 04 00 00 00               mov r10d, 4
0068582B  45 8D 42 FE                     lea r8d, [r10 - 2]
0068582F  45 88 77 04                     mov byte ptr [r15 + 4], r14b
00685833  48 3B 0D A6 84 7A 00            cmp rcx, qword ptr [rip + 0x7a84a6]
0068583A  0F 87 1A 01 00 00               ja 0x14068595a
00685840  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00685844  48 03 C9                        add rcx, rcx
00685847  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00685851  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00685855  48 C1 E8 36                     shr rax, 0x36
00685859  0F BA E0 00                     bt eax, 0
0068585D  0F 83 F2 00 00 00               jae 0x140685955
00685863  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0068586D  4C 8D 2C C8                     lea r13, [rax + rcx*8]
00685871  4D 8D 75 18                     lea r14, [r13 + 0x18]
00685875  0F BA E7 1E                     bt edi, 0x1e
00685879  72 31                           jb 0x1406858ac
0068587B  85 ED                           test ebp, ebp
0068587D  74 32                           je 0x1406858b1
0068587F  41 C7 07 01 00 00 00            mov dword ptr [r15], 1
00685886  F0 49 0F BA 2E 3F               lock bts qword ptr [r14], 0x3f
0068588C  73 4B                           jae 0x1406858d9
0068588E  40 F6 C7 41                     test dil, 0x41
00685892  0F 85 3F 02 00 00               jne 0x140685ad7
00685898  8B 05 AE 1C 8C 00               mov eax, dword ptr [rip + 0x8c1cae]
0068589E  A8 03                           test al, 3
006858A0  0F 84 31 02 00 00               je 0x140685ad7
006858A6  FF 05 34 AA 7A 00               inc dword ptr [rip + 0x7aaa34]
006858AC  45 89 17                        mov dword ptr [r15], r10d
006858AF  EB 28                           jmp 0x1406858d9
006858B1  83 64 24 78 00                  and dword ptr [rsp + 0x78], 0
006858B6  45 89 07                        mov dword ptr [r15], r8d
006858B9  F0 49 0F BA 2E 3F               lock bts qword ptr [r14], 0x3f
006858BF  73 14                           jae 0x1406858d5
006858C1  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
006858C6  E8 35 64 D7 FF                  call 0x1403fbd00
006858CB  49 8B 06                        mov rax, qword ptr [r14]
006858CE  48 85 C0                        test rax, rax
006858D1  78 EE                           js 0x1406858c1
006858D3  EB E4                           jmp 0x1406858b9
006858D5  49 8D 57 28                     lea rdx, [r15 + 0x28]
006858D9  4D 8D 47 30                     lea r8, [r15 + 0x30]
006858DD  49 8B CD                        mov rcx, r13
006858E0  E8 8B FB FF FF                  call 0x140685470
006858E5  85 C0                           test eax, eax
006858E7  74 3A                           je 0x140685923
006858E9  41 8A 45 22                     mov al, byte ptr [r13 + 0x22]
006858ED  24 07                           and al, 7
006858EF  3C 06                           cmp al, 6
006858F1  74 24                           je 0x140685917
006858F3  41 8B 07                        mov eax, dword ptr [r15]
006858F6  83 F8 01                        cmp eax, 1
006858F9  74 09                           je 0x140685904
006858FB  83 F8 02                        cmp eax, 2
006858FE  0F 85 D3 01 00 00               jne 0x140685ad7
00685904  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0068590E  F0 49 21 06                     lock and qword ptr [r14], rax
00685912  E9 C0 01 00 00                  jmp 0x140685ad7
00685917  40 F6 C7 01                     test dil, 1
0068591B  B8 04 00 00 00                  mov eax, 4
00685920  0F 45 F0                        cmovne esi, eax
00685923  49 8B D5                        mov rdx, r13
00685926  4D 89 6F 10                     mov qword ptr [r15 + 0x10], r13
0068592A  8B CE                           mov ecx, esi
0068592C  E8 9F 43 BA FF                  call 0x140229cd0
00685931  41 8B 4D 20                     mov ecx, dword ptr [r13 + 0x20]
00685935  8B F0                           mov esi, eax
00685937  4C 8B 6C 24 28                  mov r13, qword ptr [rsp + 0x28]
0068593C  83 CE 08                        or esi, 8
0068593F  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
00685944  C1 E9 10                        shr ecx, 0x10
00685947  80 E1 C0                        and cl, 0xc0
0068594A  80 F9 C0                        cmp cl, 0xc0
0068594D  0F 45 F0                        cmovne esi, eax
00685950  E9 20 01 00 00                  jmp 0x140685a75
00685955  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
0068595A  4D 8D 77 18                     lea r14, [r15 + 0x18]
0068595E  4D 8B C6                        mov r8, r14
00685961  85 ED                           test ebp, ebp
00685963  74 1A                           je 0x14068597f
00685965  BA 01 00 00 00                  mov edx, 1
0068596A  41 C7 07 08 00 00 00            mov dword ptr [r15], 8
00685971  E8 36 64 FF FF                  call 0x14067bdac
00685976  85 C0                           test eax, eax
00685978  75 13                           jne 0x14068598d
0068597A  E9 58 01 00 00                  jmp 0x140685ad7
0068597F  33 D2                           xor edx, edx
00685981  41 C7 07 10 00 00 00            mov dword ptr [r15], 0x10
00685988  E8 1F 64 FF FF                  call 0x14067bdac
0068598D  4D 8B 06                        mov r8, qword ptr [r14]
00685990  41 BA 03 00 00 00               mov r10d, 3
00685996  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
0068599B  41 8B D2                        mov edx, r10d
0068599E  4D 85 C0                        test r8, r8
006859A1  74 2E                           je 0x1406859d1
006859A3  8A 0D 8F 82 7A 00               mov cl, byte ptr [rip + 0x7a828f]
006859A9  41 8D 42 FE                     lea eax, [r10 - 2]
006859AD  80 C1 F4                        add cl, 0xf4
006859B0  48 D3 E0                        shl rax, cl
006859B3  FF C8                           dec eax
006859B5  41 23 C1                        and eax, r9d
006859B8  41 2B 40 18                     sub eax, dword ptr [r8 + 0x18]
006859BC  03 C0                           add eax, eax
006859BE  8B C8                           mov ecx, eax
006859C0  48 C1 E8 05                     shr rax, 5
006859C4  83 E1 1F                        and ecx, 0x1f
006859C7  41 8B 54 80 2C                  mov edx, dword ptr [r8 + rax*4 + 0x2c]
006859CC  D3 EA                           shr edx, cl
006859CE  41 23 D2                        and edx, r10d
006859D1  8B C2                           mov eax, edx
006859D3  41 3B D2                        cmp edx, r10d
006859D6  75 3B                           jne 0x140685a13
006859D8  33 D2                           xor edx, edx
006859DA  85 ED                           test ebp, ebp
006859DC  0F 44 D0                        cmove edx, eax
006859DF  40 F6 C7 28                     test dil, 0x28
006859E3  74 06                           je 0x1406859eb
006859E5  83 E7 D7                        and edi, 0xffffffd7
006859E8  83 CF 10                        or edi, 0x10
006859EB  40 F6 C7 08                     test dil, 8
006859EF  75 79                           jne 0x140685a6a
006859F1  40 F6 C7 10                     test dil, 0x10
006859F5  74 44                           je 0x140685a3b
006859F7  0F 20 E1                        mov rcx, cr4
006859FA  48 F7 C1 80 00 02 00            test rcx, 0x20080
00685A01  74 2D                           je 0x140685a30
00685A03  48 8B C1                        mov rax, rcx
00685A06  48 0F BA F8 07                  btc rax, 7
00685A0B  0F 22 E0                        mov cr4, rax
00685A0E  0F 22 E1                        mov cr4, rcx
00685A11  EB 23                           jmp 0x140685a36
00685A13  83 E7 C7                        and edi, 0xffffffc7
00685A16  8B CA                           mov ecx, edx
00685A18  85 D2                           test edx, edx
00685A1A  74 CC                           je 0x1406859e8
00685A1C  83 E9 01                        sub ecx, 1
00685A1F  74 0A                           je 0x140685a2b
00685A21  83 F9 01                        cmp ecx, 1
00685A24  75 05                           jne 0x140685a2b
00685A26  83 CF 20                        or edi, 0x20
00685A29  EB C0                           jmp 0x1406859eb
00685A2B  83 CF 08                        or edi, 8
00685A2E  EB BB                           jmp 0x1406859eb
00685A30  0F 20 D8                        mov rax, cr3
00685A33  0F 22 D8                        mov cr3, rax
00685A36  83 CE 10                        or esi, 0x10
00685A39  EB 2F                           jmp 0x140685a6a
00685A3B  40 F6 C7 20                     test dil, 0x20
00685A3F  0F 84 8A 00 00 00               je 0x140685acf
00685A45  0F 20 E1                        mov rcx, cr4
00685A48  48 F7 C1 80 00 02 00            test rcx, 0x20080
00685A4F  74 10                           je 0x140685a61
00685A51  48 8B C1                        mov rax, rcx
00685A54  48 0F BA F8 07                  btc rax, 7
00685A59  0F 22 E0                        mov cr4, rax
00685A5C  0F 22 E1                        mov cr4, rcx
00685A5F  EB 06                           jmp 0x140685a67
00685A61  0F 20 D8                        mov rax, cr3
00685A64  0F 22 D8                        mov cr3, rax
00685A67  83 CE 18                        or esi, 0x18
00685A6A  41 3B D2                        cmp edx, r10d
00685A6D  75 06                           jne 0x140685a75
00685A6F  FF 05 6B A8 7A 00               inc dword ptr [rip + 0x7aa86b]
00685A75  81 CE 00 00 00 A0               or esi, 0xa0000000
00685A7B  49 8B D1                        mov rdx, r9
00685A7E  44 8B C6                        mov r8d, esi
00685A81  49 8B CC                        mov rcx, r12
00685A84  E8 07 FB C3 FF                  call 0x1402c5590
00685A89  48 8B C8                        mov rcx, rax
00685A8C  40 F6 C7 41                     test dil, 0x41
00685A90  74 07                           je 0x140685a99
00685A92  C6 05 2F A8 7A 00 01            mov byte ptr [rip + 0x7aa82f], 1
00685A99  33 C0                           xor eax, eax
00685A9B  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
00685AA1  75 2C                           jne 0x140685acf
00685AA3  41 8B 07                        mov eax, dword ptr [r15]
00685AA6  33 D2                           xor edx, edx
00685AA8  4D 89 67 08                     mov qword ptr [r15 + 8], r12
00685AAC  49 8B CD                        mov rcx, r13
00685AAF  A8 12                           test al, 0x12
00685AB1  74 0B                           je 0x140685abe
00685AB3  44 8D 42 02                     lea r8d, [rdx + 2]
00685AB7  E8 C8 83 F3 FF                  call 0x1405bde84
00685ABC  EB 05                           jmp 0x140685ac3
00685ABE  E8 D9 81 F3 FF                  call 0x1405bdc9c
00685AC3  81 E3 FF 0F 00 00               and ebx, 0xfff
00685AC9  4A 8D 04 2B                     lea rax, [rbx + r13]
00685ACD  EB 0A                           jmp 0x140685ad9
00685ACF  49 8B CF                        mov rcx, r15
00685AD2  E8 21 00 00 00                  call 0x140685af8
00685AD7  33 C0                           xor eax, eax
00685AD9  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00685ADE  48 83 C4 30                     add rsp, 0x30
00685AE2  41 5F                           pop r15
00685AE4  41 5E                           pop r14
00685AE6  41 5D                           pop r13
00685AE8  41 5C                           pop r12
00685AEA  5F                              pop rdi
00685AEB  5E                              pop rsi
00685AEC  5D                              pop rbp
00685AED  C3                              ret
00685AEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDbgTranslatePhysicalAddress(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rbp = (unsigned int)(((unsigned int)(a2)) & (4));
    v_r12 = *(unsigned __int64 *)(v_rip + 8039261);
    if (condition_is_not_equal) { v_r12 = *(unsigned __int64 *)(v_rip + 8039226); }
    if (v_r12 == 0) goto loc_00685AD7;
    result = MiCheckPhysicalAddressRange(a1, 4 - 3, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00685AD7;
    v_r13 = (v_r12) << (25);
    result = (result) << (25);
    v_r13 = (v_r13) - (result);
    a1 = (a1) >> (12);
    v_r13 = (v_r13) >> (16);
    v_stack_m40 = v_r13;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (64));
    v_stack_m48 = a1;
    result = (unsigned __int8)(-(result));
    v_rsi = (unsigned int)((v_rsi) & (3));
    v_rsi = (unsigned int)((v_rsi) + 1);
    if ((unsigned int)(v_rbp) == 0) goto loc_00685800;
    goto loc_0068582F;
loc_00685800:
    v_r10 = 4;
    if ((*(unsigned int *)(v_rip + 9704721)) != 0) {
        a2 = (unsigned __int8)(4 - 2);
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, 4 - 2, a4);
        a1 = v_stack_m48;
        a2 = a3 + 40;
        v_r10 = 4;
        a3 = v_r10 - 2;
    }
    *(unsigned __int8 *)(a3 + 4) = (unsigned __int8)(v_cr8);
    if (a1 > (*(unsigned __int64 *)(v_rip + 8029350))) goto loc_0068595A;
    a1 = (a1 + a1 * 2) + (a1 + a1 * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00685955;
    if (condition_is_below) goto loc_006858AC;
    if ((unsigned int)(v_rbp) == 0) goto loc_006858B1;
    *(unsigned int *)(a3) = 1;
    if (condition_is_above_or_equal) goto loc_006858D9;
    if ((((unsigned __int8)((unsigned int)(a2))) & (65)) != 0) goto loc_00685AD7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9182382)))) & (3)) == 0) goto loc_00685AD7;
loc_006858AC:
    *(unsigned int *)(a3) = (unsigned int)(v_r10);
    goto loc_006858D9;
loc_006858B1:
    *(unsigned int *)(a3) = (unsigned int)(a3);
loc_006858B9:
    if (condition_is_above_or_equal) goto loc_006858D5;
loc_006858C1:
    result = KeYieldProcessorEx(v_stack_p10, a2, a3, a4);
    if (sign_flag) goto loc_006858C1;
    goto loc_006858B9;
loc_006858D5:
loc_006858D9:
    result = MiDbgPatchIdentity(result + a1 * 8, a3 + 40, a3 + 48, a4);
    if ((unsigned int)(result) == 0) goto loc_00685923;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + a1 * 8 + 34)) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_00685917;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == 1) goto loc_00685904;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) != 2) goto loc_00685AD7;
loc_00685904:
    goto loc_00685AD7;
loc_00685917:
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) != 0) { v_rsi = 4; }
loc_00685923:
    *(unsigned __int64 *)(a3 + 16) = result + a1 * 8;
    result = MiMakeProtectionPfnCompatible((unsigned int)((unsigned int)(v_rsi)), result + a1 * 8, a3 + 48, a4);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) | (8));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32))) >> (16));
    a1 = (unsigned __int8)((a1) & (192));
    if (((unsigned __int8)(a1)) != 192) { v_rsi = (unsigned int)(result); }
    goto loc_00685A75;
loc_00685955:
loc_0068595A:
    if ((unsigned int)(v_rbp) == 0) goto loc_0068597F;
    *(unsigned int *)(a3) = 8;
    result = MiFreezeIoPfnNode(v_stack_m48, 1, a3 + 24, v_stack_m48);
    if ((unsigned int)(result) != 0) goto loc_0068598D;
    goto loc_00685AD7;
loc_0068597F:
    a2 = 0;
    *(unsigned int *)(a3) = 16;
    result = MiFreezeIoPfnNode(v_stack_m48, a2, a3 + 24, v_stack_m48);
loc_0068598D:
    if (*(unsigned __int64 *)(a3 + 24) != 0) {
        a1 = *(unsigned __int8 *)(v_rip + 8028815);
        result = 3 - 2;
        a1 = (unsigned __int8)((a1) + (244));
        result = (result) << ((unsigned __int8)(a1));
        result = (unsigned int)((result) - 1);
        result = (unsigned int)((result) & ((unsigned int)(v_stack_m48)));
        result = (unsigned int)((result) - (*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 24)));
        result = (unsigned int)((result) + ((unsigned int)(result)));
        a1 = (unsigned int)(result);
        result = (result) >> (5);
        a1 = (unsigned int)((a1) & (31));
        a2 = *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + result * 4 + 44);
        a2 = (unsigned int)((a2) >> ((unsigned __int8)(a1)));
        a2 = (unsigned int)((a2) & (3));
    }
    if (a2 != 3) goto loc_00685A13;
    a2 = 0;
    if ((unsigned int)(v_rbp) == 0) { a2 = (unsigned int)((unsigned int)(a2)); }
    if ((((unsigned __int8)((unsigned int)(a2))) & (40)) == 0) goto loc_006859EB;
    v_rdi = (unsigned int)(((unsigned int)(a2)) & (0xFFFFFFD7ULL));
loc_006859E8:
    v_rdi = (unsigned int)((v_rdi) | (16));
loc_006859EB:
    if ((((unsigned __int8)(v_rdi)) & (8)) != 0) goto loc_00685A6A;
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_00685A3B;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00685A30;
    goto loc_00685A36;
loc_00685A13:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFC7ULL));
    if (a2 == 0) goto loc_006859E8;
    a1 = (unsigned int)(((unsigned int)(a2)) - (1));
    if (condition_is_equal) goto loc_00685A2B;
    if (((unsigned int)(a1)) != 1) goto loc_00685A2B;
    v_rdi = (unsigned int)((v_rdi) | (32));
    goto loc_006859EB;
loc_00685A2B:
    v_rdi = (unsigned int)((v_rdi) | (8));
    goto loc_006859EB;
loc_00685A30:
loc_00685A36:
    v_rsi = (unsigned int)((v_rsi) | (16));
    goto loc_00685A6A;
loc_00685A3B:
    if ((((unsigned __int8)(v_rdi)) & (32)) == 0) goto loc_00685ACF;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00685A61;
    goto loc_00685A67;
loc_00685A61:
loc_00685A67:
    v_rsi = (unsigned int)((v_rsi) | (24));
loc_00685A6A:
    if (a2 == 3) {
    }
    v_rsi = (unsigned int)((v_rsi) | (0xA0000000ULL));
    result = MiMakeValidPte(v_r12, v_stack_m48, (unsigned int)((unsigned int)(v_rsi)), v_stack_m48);
    if ((((unsigned __int8)(v_rdi)) & (65)) != 0) {
        *(unsigned __int8 *)(v_rip + 8038447) = 1;
    }
    result = 0;
    if (condition_is_not_equal) goto loc_00685ACF;
    a2 = 0;
    *(unsigned __int64 *)(a3 + 8) = v_r12;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (18)) == 0) goto loc_00685ABE;
    result = KeFlushSingleTb(v_stack_m40, a2, a2 + 2, v_stack_m48);
    goto loc_00685AC3;
loc_00685ABE:
    result = KeFlushSingleCurrentTb(v_stack_m40, a2, a2 + 2, v_stack_m48);
loc_00685AC3:
    v_rbx = (unsigned int)((a1) & (0xFFFULL));
    goto loc_00685AD9;
loc_00685ACF:
    result = MiDbgUnTranslatePhysicalAddress(a3, a2, a2 + 2, v_stack_m48);
loc_00685AD7:
    result = 0;
loc_00685AD9:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDbgTranslatePhysicalAddress(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rbp = (uint32_t)(((uint32_t)(Arg2)) & (4));
    local_r12 = *(uint64_t *)(v_rip + 0x7AAB5D);
    if (condition_is_not_equal) { local_r12 = *(uint64_t *)(v_rip + 0x7AAB3A); }
    if (local_r12 == 0) goto loc_00685AD7;
    result = MiCheckPhysicalAddressRange(Arg1, 4 - 3, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00685AD7;
    local_r13 = (local_r12) << (25);
    result = (result) << (25);
    local_r13 = (local_r13) - (result);
    Arg1 = (Arg1) >> (12);
    local_r13 = (local_r13) >> (16);
    v_stack_m40 = local_r13;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (64));
    v_stack_m48 = Arg1;
    result = (uint8_t)(-(result));
    local_rsi = (uint32_t)((local_rsi) & (3));
    local_rsi = (uint32_t)((local_rsi) + 1);
    if ((uint32_t)(local_rbp) == 0) goto loc_00685800;
    goto loc_0068582F;
loc_00685800:
    local_r10 = 4;
    if ((*(uint32_t *)(v_rip + 0x941511)) != 0) {
        Arg2 = (uint8_t)(4 - 2);
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, 4 - 2, a4);
        Arg1 = v_stack_m48;
        Arg2 = Arg3 + 40;
        local_r10 = 4;
        Arg3 = local_r10 - 2;
    }
    *(uint8_t *)(arg3 + 0x4) = (uint8_t)(v_cr8);
    if (Arg1 > (*(uint64_t *)(v_rip + 0x7A84A6))) goto loc_0068595A;
    Arg1 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00685955;
    if (condition_is_below) goto loc_006858AC;
    if ((uint32_t)(local_rbp) == 0) goto loc_006858B1;
    *(uint32_t *)(arg3) = 1;
    if (condition_is_above_or_equal) goto loc_006858D9;
    if ((((uint8_t)((uint32_t)(Arg2))) & (65)) != 0) goto loc_00685AD7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8C1CAE)))) & (3)) == 0) goto loc_00685AD7;
loc_006858AC:
    *(uint32_t *)(arg3) = (uint32_t)(local_r10);
    goto loc_006858D9;
loc_006858B1:
    *(uint32_t *)(arg3) = (uint32_t)(Arg3);
loc_006858B9:
    if (condition_is_above_or_equal) goto loc_006858D5;
loc_006858C1:
    result = KeYieldProcessorEx(v_stack_p10, Arg2, Arg3, a4);
    if (sign_flag) goto loc_006858C1;
    goto loc_006858B9;
loc_006858D5:
loc_006858D9:
    result = MiDbgPatchIdentity(result + Arg1 * 8, Arg3 + 40, Arg3 + 48, a4);
    if ((uint32_t)(result) == 0) goto loc_00685923;
    result = (uint8_t)((*(uint8_t *)(result + arg1 * 8 + 0x22)) & (7));
    if (((uint8_t)(result)) == 6) goto loc_00685917;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))) == 1) goto loc_00685904;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))) != 2) goto loc_00685AD7;
loc_00685904:
    goto loc_00685AD7;
loc_00685917:
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) != 0) { local_rsi = 4; }
loc_00685923:
    *(uint64_t *)(arg3 + 0x10) = result + Arg1 * 8;
    result = MiMakeProtectionPfnCompatible((uint32_t)((uint32_t)(local_rsi)), result + Arg1 * 8, Arg3 + 48, a4);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) | (8));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20))) >> (16));
    Arg1 = (uint8_t)((Arg1) & (192));
    if (((uint8_t)(Arg1)) != 192) { local_rsi = (uint32_t)(result); }
    goto loc_00685A75;
loc_00685955:
loc_0068595A:
    if ((uint32_t)(local_rbp) == 0) goto loc_0068597F;
    *(uint32_t *)(arg3) = 8;
    result = MiFreezeIoPfnNode(v_stack_m48, 1, Arg3 + 24, v_stack_m48);
    if ((uint32_t)(result) != 0) goto loc_0068598D;
    goto loc_00685AD7;
loc_0068597F:
    Arg2 = 0;
    *(uint32_t *)(arg3) = 16;
    result = MiFreezeIoPfnNode(v_stack_m48, Arg2, Arg3 + 24, v_stack_m48);
loc_0068598D:
    if (*(uint64_t *)(arg3 + 0x18) != 0) {
        Arg1 = *(uint8_t *)(v_rip + 0x7A828F);
        result = 3 - 2;
        Arg1 = (uint8_t)((Arg1) + (244));
        result = (result) << ((uint8_t)(Arg1));
        result = (uint32_t)((result) - 1);
        result = (uint32_t)((result) & ((uint32_t)(v_stack_m48)));
        result = (uint32_t)((result) - (*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x18)));
        result = (uint32_t)((result) + ((uint32_t)(result)));
        Arg1 = (uint32_t)(result);
        result = (result) >> (5);
        Arg1 = (uint32_t)((Arg1) & (31));
        Arg2 = *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + result * 4 + 0x2C);
        Arg2 = (uint32_t)((Arg2) >> ((uint8_t)(Arg1)));
        Arg2 = (uint32_t)((Arg2) & (3));
    }
    if (Arg2 != 3) goto loc_00685A13;
    Arg2 = 0;
    if ((uint32_t)(local_rbp) == 0) { Arg2 = (uint32_t)((uint32_t)(Arg2)); }
    if ((((uint8_t)((uint32_t)(Arg2))) & (40)) == 0) goto loc_006859EB;
    local_rdi = (uint32_t)(((uint32_t)(Arg2)) & (0xFFFFFFD7ULL));
loc_006859E8:
    local_rdi = (uint32_t)((local_rdi) | (16));
loc_006859EB:
    if ((((uint8_t)(local_rdi)) & (8)) != 0) goto loc_00685A6A;
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_00685A3B;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00685A30;
    goto loc_00685A36;
loc_00685A13:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFC7ULL));
    if (Arg2 == 0) goto loc_006859E8;
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) - (1));
    if (condition_is_equal) goto loc_00685A2B;
    if (((uint32_t)(Arg1)) != 1) goto loc_00685A2B;
    local_rdi = (uint32_t)((local_rdi) | (32));
    goto loc_006859EB;
loc_00685A2B:
    local_rdi = (uint32_t)((local_rdi) | (8));
    goto loc_006859EB;
loc_00685A30:
loc_00685A36:
    local_rsi = (uint32_t)((local_rsi) | (16));
    goto loc_00685A6A;
loc_00685A3B:
    if ((((uint8_t)(local_rdi)) & (32)) == 0) goto loc_00685ACF;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00685A61;
    goto loc_00685A67;
loc_00685A61:
loc_00685A67:
    local_rsi = (uint32_t)((local_rsi) | (24));
loc_00685A6A:
    if (Arg2 == 3) {
    }
    local_rsi = (uint32_t)((local_rsi) | (0xA0000000ULL));
    result = MiMakeValidPte(local_r12, v_stack_m48, (uint32_t)((uint32_t)(local_rsi)), v_stack_m48);
    if ((((uint8_t)(local_rdi)) & (65)) != 0) {
        *(uint8_t *)(v_rip + 0x7AA82F) = 1;
    }
    result = 0;
    if (condition_is_not_equal) goto loc_00685ACF;
    Arg2 = 0;
    *(uint64_t *)(arg3 + 0x8) = local_r12;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (18)) == 0) goto loc_00685ABE;
    result = KeFlushSingleTb(v_stack_m40, Arg2, Arg2 + 2, v_stack_m48);
    goto loc_00685AC3;
loc_00685ABE:
    result = KeFlushSingleCurrentTb(v_stack_m40, Arg2, Arg2 + 2, v_stack_m48);
loc_00685AC3:
    local_rbx = (uint32_t)((Arg1) & (0xFFFULL));
    goto loc_00685AD9;
loc_00685ACF:
    result = MiDbgUnTranslatePhysicalAddress(Arg3, Arg2, Arg2 + 2, v_stack_m48);
loc_00685AD7:
    result = 0;
loc_00685AD9:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + r13*1` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R/W` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R/W` |
| `Arg3` | `+ 0x4` | `8` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00685760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
