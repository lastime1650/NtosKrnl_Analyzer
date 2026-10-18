# CmpFullPromoteSingleKeyFromKeyNodeStacks

- RVA: `0x008B1A40`–`0x008B1EFD` (길이 `1,213` bytes)
- VA: `0x00000001408B1A40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082564`
- 디코드: `322`개 명령, `1,213/1,213` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008B1A9C` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x008B1AAB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B1AC2` → [CmpValueEnumStackEntryInitialize](../../text/49/CmpValueEnumStackEntryInitialize_function_0049D4C4.md) (function, `0x0049D4C4`)
- `0x008B1ADC` → [CmpKeyNodeStackGetEntryAtLayerHeight](../94/CmpKeyNodeStackGetEntryAtLayerHeight_function_00946ABC.md) (function, `0x00946ABC`)
- `0x008B1AF0` → [CmpKeyNodeStackGetEntryAtLayerHeight](../94/CmpKeyNodeStackGetEntryAtLayerHeight_function_00946ABC.md) (function, `0x00946ABC`)
- `0x008B1B20` → [CmpKeyNodeStackGetEntryAtLayerHeight](../94/CmpKeyNodeStackGetEntryAtLayerHeight_function_00946ABC.md) (function, `0x00946ABC`)
- `0x008B1B52` → [CmpValueEnumStackStartFromKeyNodeStack](../../text/46/CmpValueEnumStackStartFromKeyNodeStack_function_0046B2E0.md) (function, `0x0046B2E0`)
- `0x008B1B75` → [CmpValueEnumStackAdvance](CmpValueEnumStackAdvance_function_008B256C.md) (function, `0x008B256C`)
- `0x008B1B9A` → [CmpValueEnumStackGetCurrentValueHive](../../text/4A/CmpValueEnumStackGetCurrentValueHive_function_004A7A60.md) (function, `0x004A7A60`)
- `0x008B1BB5` → [CmpCopyValue](../85/CmpCopyValue_function_0085B798.md) (function, `0x0085B798`)
- `0x008B1BDD` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008B1C36` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008B1C5D` → [CmpAddValueToListEx](../85/CmpAddValueToListEx_function_0085B460.md) (function, `0x0085B460`)
- `0x008B1C99` → [CmpConcatenateValueLists](CmpConcatenateValueLists_function_008B0ECC.md) (function, `0x008B0ECC`)
- `0x008B1CC6` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008B1D06` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008B1DA9` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x008B1DBC` → [CmpValueEnumStackCleanup](CmpValueEnumStackCleanup_function_008B1F04.md) (function, `0x008B1F04`)
- `0x008B1DE8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B1E09` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008B1E23` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008B1E36` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008B1E5A` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008B1E8C` → [CmpCopyCell](../85/CmpCopyCell_function_0085A608.md) (function, `0x0085A608`)
- `0x008B1EC1` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x008B1ED3` → [CmpFreeKeyValueList](../7F/CmpFreeKeyValueList_function_007F2250.md) (function, `0x007F2250`)
- `0x008B1EE3` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x008B1EF3` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)

### Direct callers
- [CmSaveKey](../7D/CmSaveKey_function_007DDBDC.md) at `0x007DDF2D`
- [CmpFullPromoteHiveRootFromKcbStack](../7F/CmpFullPromoteHiveRootFromKcbStack_function_007F3F90.md) at `0x007F4005`
- [CmpPromoteSingleKeyFromParentKcbAndChildKeyNode](../7F/CmpPromoteSingleKeyFromParentKcbAndChildKeyNode_function_007F426C.md) at `0x007F4331`
- [CmpPromoteSingleKeyFromKcbStacks](../94/CmpPromoteSingleKeyFromKcbStacks_function_009446E8.md) at `0x009448C3`
- [CmpPromoteSubtree](../94/CmpPromoteSubtree_function_00944D60.md) at `0x00944E60`

### Static image references
- `0x008B1A5C` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x008B1AAB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B1AC2` → [CmpValueEnumStackEntryInitialize](../../text/49/CmpValueEnumStackEntryInitialize_function_0049D4C4.md) (`PAGE` → `.text`)
  - `0x008B1B52` → [CmpValueEnumStackStartFromKeyNodeStack](../../text/46/CmpValueEnumStackStartFromKeyNodeStack_function_0046B2E0.md) (`PAGE` → `.text`)
  - `0x008B1B9A` → [CmpValueEnumStackGetCurrentValueHive](../../text/4A/CmpValueEnumStackGetCurrentValueHive_function_004A7A60.md) (`PAGE` → `.text`)
  - `0x008B1DE8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B1A40  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008B1A45  55                              push rbp
008B1A46  56                              push rsi
008B1A47  57                              push rdi
008B1A48  41 54                           push r12
008B1A4A  41 55                           push r13
008B1A4C  41 56                           push r14
008B1A4E  41 57                           push r15
008B1A50  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
008B1A55  48 81 EC E0 00 00 00            sub rsp, 0xe0
008B1A5C  48 8B 05 DD 8C 55 00            mov rax, qword ptr [rip + 0x558cdd]
008B1A63  48 33 C4                        xor rax, rsp
008B1A66  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
008B1A6A  83 CF FF                        or edi, 0xffffffff
008B1A6D  33 F6                           xor esi, esi
008B1A6F  48 8B D9                        mov rbx, rcx
008B1A72  48 89 75 9F                     mov qword ptr [rbp - 0x61], rsi
008B1A76  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
008B1A7A  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
008B1A7E  44 8B E7                        mov r12d, edi
008B1A81  66 89 74 24 30                  mov word ptr [rsp + 0x30], si
008B1A86  89 7D 83                        mov dword ptr [rbp - 0x7d], edi
008B1A89  44 8B F7                        mov r14d, edi
008B1A8C  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
008B1A90  4C 8B EA                        mov r13, rdx
008B1A93  89 7D AB                        mov dword ptr [rbp - 0x55], edi
008B1A96  89 75 A7                        mov dword ptr [rbp - 0x59], esi
008B1A99  89 7D 87                        mov dword ptr [rbp - 0x79], edi
008B1A9C  E8 6F 44 FA FF                  call 0x140855f10
008B1AA1  48 8D 4D BB                     lea rcx, [rbp - 0x45]
008B1AA5  33 D2                           xor edx, edx
008B1AA7  44 8D 46 54                     lea r8d, [rsi + 0x54]
008B1AAB  E8 90 51 E1 FF                  call 0x1406c6c40
008B1AB0  48 8D 55 C7                     lea rdx, [rbp - 0x39]
008B1AB4  89 7D B7                        mov dword ptr [rbp - 0x49], edi
008B1AB7  44 8D 46 02                     lea r8d, [rsi + 2]
008B1ABB  44 8D 5E 01                     lea r11d, [rsi + 1]
008B1ABF  48 8B CA                        mov rcx, rdx
008B1AC2  E8 FD B9 BE FF                  call 0x14049d4c4
008B1AC7  48 83 C2 20                     add rdx, 0x20
008B1ACB  4D 2B C3                        sub r8, r11
008B1ACE  75 EF                           jne 0x1408b1abf
008B1AD0  41 0F B7 55 00                  movzx edx, word ptr [r13]
008B1AD5  49 8B CD                        mov rcx, r13
008B1AD8  66 89 55 8B                     mov word ptr [rbp - 0x75], dx
008B1ADC  E8 DB 4F 09 00                  call 0x140946abc
008B1AE1  48 8B F8                        mov rdi, rax
008B1AE4  48 85 DB                        test rbx, rbx
008B1AE7  0F 84 2E 03 00 00               je 0x1408b1e1b
008B1AED  48 8B CB                        mov rcx, rbx
008B1AF0  E8 C7 4F 09 00                  call 0x140946abc
008B1AF5  4C 8B F8                        mov r15, rax
008B1AF8  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1AFC  45 33 D2                        xor r10d, r10d
008B1AFF  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
008B1B03  48 8B 37                        mov rsi, qword ptr [rdi]
008B1B06  41 C1 E9 1F                     shr r9d, 0x1f
008B1B0A  44 89 4D 97                     mov dword ptr [rbp - 0x69], r9d
008B1B0E  44 38 50 0D                     cmp byte ptr [rax + 0xd], r10b
008B1B12  7D 37                           jge 0x1408b1b4b
008B1B14  66 41 2B D3                     sub dx, r11w
008B1B18  66 85 D2                        test dx, dx
008B1B1B  78 2E                           js 0x1408b1b4b
008B1B1D  49 8B CD                        mov rcx, r13
008B1B20  E8 97 4F 09 00                  call 0x140946abc
008B1B25  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
008B1B29  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
008B1B2D  48 85 C9                        test rcx, rcx
008B1B30  0F 84 DD 02 00 00               je 0x1408b1e13
008B1B36  44 38 51 0D                     cmp byte ptr [rcx + 0xd], r10b
008B1B3A  0F 8C D3 02 00 00               jl 0x1408b1e13
008B1B40  66 44 39 51 4A                  cmp word ptr [rcx + 0x4a], r10w
008B1B45  0F 85 2E 03 00 00               jne 0x1408b1e79
008B1B4B  49 8B D5                        mov rdx, r13
008B1B4E  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008B1B52  E8 89 97 BB FF                  call 0x14046b2e0
008B1B57  8B D8                           mov ebx, eax
008B1B59  85 C0                           test eax, eax
008B1B5B  0F 88 57 02 00 00               js 0x1408b1db8
008B1B61  44 0F B7 6D 8B                  movzx r13d, word ptr [rbp - 0x75]
008B1B66  33 C9                           xor ecx, ecx
008B1B68  33 D2                           xor edx, edx
008B1B6A  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
008B1B6E  89 55 8F                        mov dword ptr [rbp - 0x71], edx
008B1B71  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008B1B75  E8 F2 09 00 00                  call 0x1408b256c
008B1B7A  8B D8                           mov ebx, eax
008B1B7C  3D 1A 00 00 80                  cmp eax, 0x8000001a
008B1B81  0F 84 EE 00 00 00               je 0x1408b1c75
008B1B87  85 C0                           test eax, eax
008B1B89  0F 88 29 02 00 00               js 0x1408b1db8
008B1B8F  66 44 39 6D BD                  cmp word ptr [rbp - 0x43], r13w
008B1B94  74 DB                           je 0x1408b1b71
008B1B96  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008B1B9A  E8 C1 5E BF FF                  call 0x1404a7a60
008B1B9F  44 8B 4D 97                     mov r9d, dword ptr [rbp - 0x69]
008B1BA3  48 8D 4D 87                     lea rcx, [rbp - 0x79]
008B1BA7  8B 55 B7                        mov edx, dword ptr [rbp - 0x49]
008B1BAA  4C 8B C6                        mov r8, rsi
008B1BAD  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008B1BB2  48 8B C8                        mov rcx, rax
008B1BB5  E8 DE 9B FA FF                  call 0x14085b798
008B1BBA  8B D8                           mov ebx, eax
008B1BBC  85 C0                           test eax, eax
008B1BBE  0F 88 F4 01 00 00               js 0x1408b1db8
008B1BC4  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
008B1BCB  4C 8D 45 9F                     lea r8, [rbp - 0x61]
008B1BCF  8B 5D 87                        mov ebx, dword ptr [rbp - 0x79]
008B1BD2  48 8B CE                        mov rcx, rsi
008B1BD5  8B D3                           mov edx, ebx
008B1BD7  0F 84 2C 02 00 00               je 0x1408b1e09
008B1BDD  E8 7E 30 FA FF                  call 0x140854c60
008B1BE2  0F B7 50 02                     movzx edx, word ptr [rax + 2]
008B1BE6  4C 8B C0                        mov r8, rax
008B1BE9  0F B7 CA                        movzx ecx, dx
008B1BEC  66 03 C9                        add cx, cx
008B1BEF  F6 40 10 01                     test byte ptr [rax + 0x10], 1
008B1BF3  8B 40 04                        mov eax, dword ptr [rax + 4]
008B1BF6  66 0F 44 CA                     cmove cx, dx
008B1BFA  3D 00 00 00 80                  cmp eax, 0x80000000
008B1BFF  0F B7 D1                        movzx edx, cx
008B1C02  8D 88 00 00 00 80               lea ecx, [rax - 0x80000000]
008B1C08  0F 42 C8                        cmovb ecx, eax
008B1C0B  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
008B1C0F  3B C8                           cmp ecx, eax
008B1C11  0F 47 C1                        cmova eax, ecx
008B1C14  3B 55 8F                        cmp edx, dword ptr [rbp - 0x71]
008B1C17  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
008B1C1B  48 8B CE                        mov rcx, rsi
008B1C1E  0F 46 55 8F                     cmovbe edx, dword ptr [rbp - 0x71]
008B1C22  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
008B1C29  89 55 8F                        mov dword ptr [rbp - 0x71], edx
008B1C2C  48 8D 55 9F                     lea rdx, [rbp - 0x61]
008B1C30  0F 85 ED 01 00 00               jne 0x1408b1e23
008B1C36  E8 05 43 FA FF                  call 0x140855f40
008B1C3B  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
008B1C40  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008B1C45  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
008B1C4D  41 B9 01 00 00 00               mov r9d, 1
008B1C53  8B D3                           mov edx, ebx
008B1C55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B1C5A  48 8B CE                        mov rcx, rsi
008B1C5D  E8 FE 97 FA FF                  call 0x14085b460
008B1C62  8B D8                           mov ebx, eax
008B1C64  85 C0                           test eax, eax
008B1C66  0F 88 4C 01 00 00               js 0x1408b1db8
008B1C6C  83 4D 87 FF                     or dword ptr [rbp - 0x79], 0xffffffff
008B1C70  E9 FC FE FF FF                  jmp 0x1408b1b71
008B1C75  83 7C 24 38 00                  cmp dword ptr [rsp + 0x38], 0
008B1C7A  74 30                           je 0x1408b1cac
008B1C7C  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
008B1C80  48 8D 45 A7                     lea rax, [rbp - 0x59]
008B1C84  44 8B 4D 97                     mov r9d, dword ptr [rbp - 0x69]
008B1C88  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
008B1C8D  48 83 C2 24                     add rdx, 0x24
008B1C91  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B1C96  48 8B CE                        mov rcx, rsi
008B1C99  E8 2E F2 FF FF                  call 0x1408b0ecc
008B1C9E  44 8B 75 AB                     mov r14d, dword ptr [rbp - 0x55]
008B1CA2  8B D8                           mov ebx, eax
008B1CA4  85 C0                           test eax, eax
008B1CA6  0F 88 0C 01 00 00               js 0x1408b1db8
008B1CAC  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1CB0  80 78 0D 00                     cmp byte ptr [rax + 0xd], 0
008B1CB4  0F 8D B4 01 00 00               jge 0x1408b1e6e
008B1CBA  8B 57 08                        mov edx, dword ptr [rdi + 8]
008B1CBD  45 33 C9                        xor r9d, r9d
008B1CC0  48 8B 0F                        mov rcx, qword ptr [rdi]
008B1CC3  45 33 C0                        xor r8d, r8d
008B1CC6  E8 B5 63 FA FF                  call 0x140858080
008B1CCB  8B D8                           mov ebx, eax
008B1CCD  85 C0                           test eax, eax
008B1CCF  0F 88 E3 00 00 00               js 0x1408b1db8
008B1CD5  4D 85 FF                        test r15, r15
008B1CD8  0F 84 90 01 00 00               je 0x1408b1e6e
008B1CDE  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
008B1CE2  44 0F B7 6C 24 30               movzx r13d, word ptr [rsp + 0x30]
008B1CE8  44 39 69 38                     cmp dword ptr [rcx + 0x38], r13d
008B1CEC  0F 82 5B 01 00 00               jb 0x1408b1e4d
008B1CF2  83 CB FF                        or ebx, 0xffffffff
008B1CF5  44 3B F3                        cmp r14d, ebx
008B1CF8  74 2D                           je 0x1408b1d27
008B1CFA  8B 57 08                        mov edx, dword ptr [rdi + 8]
008B1CFD  45 33 C9                        xor r9d, r9d
008B1D00  48 8B 0F                        mov rcx, qword ptr [rdi]
008B1D03  45 33 C0                        xor r8d, r8d
008B1D06  E8 75 63 FA FF                  call 0x140858080
008B1D0B  8B D8                           mov ebx, eax
008B1D0D  85 C0                           test eax, eax
008B1D0F  0F 88 A3 00 00 00               js 0x1408b1db8
008B1D15  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1D19  83 CB FF                        or ebx, 0xffffffff
008B1D1C  8B 50 28                        mov edx, dword ptr [rax + 0x28]
008B1D1F  3B D3                           cmp edx, ebx
008B1D21  0F 85 06 01 00 00               jne 0x1408b1e2d
008B1D27  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
008B1D2B  8A 41 0D                        mov al, byte ptr [rcx + 0xd]
008B1D2E  84 C0                           test al, al
008B1D30  79 2F                           jns 0x1408b1d61
008B1D32  24 7F                           and al, 0x7f
008B1D34  88 41 0D                        mov byte ptr [rcx + 0xd], al
008B1D37  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1D3B  44 89 60 30                     mov dword ptr [rax + 0x30], r12d
008B1D3F  44 8B E3                        mov r12d, ebx
008B1D42  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1D46  66 44 89 68 4A                  mov word ptr [rax + 0x4a], r13w
008B1D4B  4D 85 FF                        test r15, r15
008B1D4E  74 11                           je 0x1408b1d61
008B1D50  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
008B1D54  41 0F B7 CD                     movzx ecx, r13w
008B1D58  39 48 38                        cmp dword ptr [rax + 0x38], ecx
008B1D5B  0F 82 55 01 00 00               jb 0x1408b1eb6
008B1D61  44 3B F3                        cmp r14d, ebx
008B1D64  74 50                           je 0x1408b1db6
008B1D66  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1D6A  8B 50 28                        mov edx, dword ptr [rax + 0x28]
008B1D6D  3B D3                           cmp edx, ebx
008B1D6F  0F 85 49 01 00 00               jne 0x1408b1ebe
008B1D75  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
008B1D79  44 8B F3                        mov r14d, ebx
008B1D7C  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
008B1D80  48 89 41 24                     mov qword ptr [rcx + 0x24], rax
008B1D84  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1D88  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
008B1D8C  39 48 40                        cmp dword ptr [rax + 0x40], ecx
008B1D8F  73 03                           jae 0x1408b1d94
008B1D91  89 48 40                        mov dword ptr [rax + 0x40], ecx
008B1D94  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B1D98  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
008B1D9B  39 50 3C                        cmp dword ptr [rax + 0x3c], edx
008B1D9E  73 03                           jae 0x1408b1da3
008B1DA0  89 50 3C                        mov dword ptr [rax + 0x3c], edx
008B1DA3  8B 55 83                        mov edx, dword ptr [rbp - 0x7d]
008B1DA6  48 8B CE                        mov rcx, rsi
008B1DA9  E8 7E 89 FA FF                  call 0x14085a72c
008B1DAE  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
008B1DB3  89 5D 83                        mov dword ptr [rbp - 0x7d], ebx
008B1DB6  33 DB                           xor ebx, ebx
008B1DB8  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008B1DBC  E8 43 01 00 00                  call 0x1408b1f04
008B1DC1  83 CF FF                        or edi, 0xffffffff
008B1DC4  39 7D 83                        cmp dword ptr [rbp - 0x7d], edi
008B1DC7  0F 85 FE 00 00 00               jne 0x1408b1ecb
008B1DCD  44 3B F7                        cmp r14d, edi
008B1DD0  0F 85 07 01 00 00               jne 0x1408b1edd
008B1DD6  44 3B E7                        cmp r12d, edi
008B1DD9  0F 85 0E 01 00 00               jne 0x1408b1eed
008B1DDF  8B C3                           mov eax, ebx
008B1DE1  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
008B1DE5  48 33 CC                        xor rcx, rsp
008B1DE8  E8 53 A8 DF FF                  call 0x1406ac640
008B1DED  48 8B 9C 24 30 01 00 00         mov rbx, qword ptr [rsp + 0x130]
008B1DF5  48 81 C4 E0 00 00 00            add rsp, 0xe0
008B1DFC  41 5F                           pop r15
008B1DFE  41 5E                           pop r14
008B1E00  41 5D                           pop r13
008B1E02  41 5C                           pop r12
008B1E04  5F                              pop rdi
008B1E05  5E                              pop rsi
008B1E06  5D                              pop rbp
008B1E07  C3                              ret
008B1E08  CC                              int3
008B1E09  E8 A2 2E FA FF                  call 0x140854cb0
008B1E0E  E9 CF FD FF FF                  jmp 0x1408b1be2
008B1E13  66 FF CA                        dec dx
008B1E16  E9 FD FC FF FF                  jmp 0x1408b1b18
008B1E1B  4C 8B FE                        mov r15, rsi
008B1E1E  E9 D5 FC FF FF                  jmp 0x1408b1af8
008B1E23  E8 F8 AD FA FF                  call 0x14085cc20
008B1E28  E9 0E FE FF FF                  jmp 0x1408b1c3b
008B1E2D  48 8B 0F                        mov rcx, qword ptr [rdi]
008B1E30  45 33 C9                        xor r9d, r9d
008B1E33  45 33 C0                        xor r8d, r8d
008B1E36  E8 45 62 FA FF                  call 0x140858080
008B1E3B  8B D8                           mov ebx, eax
008B1E3D  85 C0                           test eax, eax
008B1E3F  0F 88 73 FF FF FF               js 0x1408b1db8
008B1E45  83 CB FF                        or ebx, 0xffffffff
008B1E48  E9 DA FE FF FF                  jmp 0x1408b1d27
008B1E4D  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
008B1E51  45 33 C9                        xor r9d, r9d
008B1E54  49 8B 0F                        mov rcx, qword ptr [r15]
008B1E57  45 33 C0                        xor r8d, r8d
008B1E5A  E8 21 62 FA FF                  call 0x140858080
008B1E5F  8B D8                           mov ebx, eax
008B1E61  85 C0                           test eax, eax
008B1E63  0F 88 4F FF FF FF               js 0x1408b1db8
008B1E69  E9 84 FE FF FF                  jmp 0x1408b1cf2
008B1E6E  44 0F B7 6C 24 30               movzx r13d, word ptr [rsp + 0x30]
008B1E74  E9 79 FE FF FF                  jmp 0x1408b1cf2
008B1E79  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
008B1E7E  4C 8B C6                        mov r8, rsi
008B1E81  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
008B1E86  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
008B1E89  48 8B 08                        mov rcx, qword ptr [rax]
008B1E8C  E8 77 87 FA FF                  call 0x14085a608
008B1E91  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
008B1E96  8B D8                           mov ebx, eax
008B1E98  85 C0                           test eax, eax
008B1E9A  0F 88 18 FF FF FF               js 0x1408b1db8
008B1EA0  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
008B1EA4  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
008B1EA8  0F B7 40 4A                     movzx eax, word ptr [rax + 0x4a]
008B1EAC  66 89 44 24 30                  mov word ptr [rsp + 0x30], ax
008B1EB1  E9 95 FC FF FF                  jmp 0x1408b1b4b
008B1EB6  89 48 38                        mov dword ptr [rax + 0x38], ecx
008B1EB9  E9 A3 FE FF FF                  jmp 0x1408b1d61
008B1EBE  48 8B 0F                        mov rcx, qword ptr [rdi]
008B1EC1  E8 66 88 FA FF                  call 0x14085a72c
008B1EC6  E9 AA FE FF FF                  jmp 0x1408b1d75
008B1ECB  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
008B1ED0  48 8B CE                        mov rcx, rsi
008B1ED3  E8 78 03 F4 FF                  call 0x1407f2250
008B1ED8  E9 F0 FE FF FF                  jmp 0x1408b1dcd
008B1EDD  41 8B D6                        mov edx, r14d
008B1EE0  48 8B CE                        mov rcx, rsi
008B1EE3  E8 44 88 FA FF                  call 0x14085a72c
008B1EE8  E9 E9 FE FF FF                  jmp 0x1408b1dd6
008B1EED  41 8B D4                        mov edx, r12d
008B1EF0  48 8B CE                        mov rcx, rsi
008B1EF3  E8 34 88 FA FF                  call 0x14085a72c
008B1EF8  E9 E2 FE FF FF                  jmp 0x1408b1ddf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFullPromoteSingleKeyFromKeyNodeStacks(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m98;
    unsigned __int16 v_stack_mA2;
    unsigned __int64 v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int16 v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int16 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int16 v_stack_p30;
    unsigned __int64 v_stack_p34;
    unsigned __int64 v_stack_p38;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 5606621)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = (unsigned int)((v_rdi) | (0xFFFFFFFFULL));
    v_rsi = 0;
    v_stack_mC0 = 0;
    v_stack_mE4 = (unsigned int)(v_rdi);
    v_stack_mE8 = 0;
    v_stack_mDC = (unsigned int)(v_rdi);
    v_stack_mE0 = 0;
    v_stack_mB4 = (unsigned int)(v_rdi);
    v_stack_mB8 = 0;
    v_stack_mD8 = (unsigned int)(v_rdi);
    result = HvpGetCellContextInitialize(v_stack_mC0, a2, a3, a4);
    a2 = 0;
    result = memset(v_stack_mA4, a2, v_rsi + 84, a4);
    v_stack_mA8 = (unsigned int)(v_rdi);
loc_008B1ABF:
    result = CmpValueEnumStackEntryInitialize(v_stack_m98, v_stack_m98, v_rsi + 2, a4);
    a2 = (v_stack_m98) + (32);
    a3 = (v_rsi + 2) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_008B1ABF;
    v_stack_mD4 = (unsigned __int16)(*(unsigned __int16 *)(a2));
    result = CmpKeyNodeStackGetEntryAtLayerHeight(a2, *(unsigned __int16 *)(a2), a3, a4);
    if (a1 == 0) goto loc_008B1E1B;
    result = CmpKeyNodeStackGetEntryAtLayerHeight(a1, *(unsigned __int16 *)(a2), a3, a4);
loc_008B1AF8:
    v_r10 = 0;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) >> (31));
    v_stack_mC8 = (unsigned int)(a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 16) + 13)) >= 0) goto loc_008B1B4B;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(a2)) - ((unsigned __int16)(v_rsi + 1)));
loc_008B1B18:
    if (sign_flag) goto loc_008B1B4B;
    result = CmpKeyNodeStackGetEntryAtLayerHeight(a2, a2, a3, a4);
    v_stack_mD0 = result;
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_008B1E13;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 16) + 13)) < 0) goto loc_008B1E13;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result + 16) + 74)) != 0) goto loc_008B1E79;
loc_008B1B4B:
    result = CmpValueEnumStackStartFromKeyNodeStack(v_stack_mA8, a2, a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    a1 = 0;
    a2 = 0;
    v_stack_mE4 = 0;
    v_stack_mD0 = 0;
loc_008B1B71:
    result = CmpValueEnumStackAdvance(v_stack_mA8, a2, a3, a4);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_008B1C75;
    if (sign_flag) goto loc_008B1DB8;
    if (v_stack_mA2 == ((unsigned __int16)(v_stack_mD4))) goto loc_008B1B71;
    result = CmpValueEnumStackGetCurrentValueHive(v_stack_mA8, a2, a3, a4);
    v_stack_mF8 = v_stack_mD8;
    result = CmpCopyValue(result, (unsigned int)(v_stack_mA8), *(unsigned __int64 *)(result), (unsigned int)(v_stack_mC8));
    if (sign_flag) goto loc_008B1DB8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 140)) & (1)) == 0) goto loc_008B1E09;
    result = HvpGetCellFlat(*(unsigned __int64 *)(result), (unsigned int)((unsigned int)((unsigned int)(v_stack_mD8))), v_stack_mC0, (unsigned int)(v_stack_mC8));
loc_008B1BE2:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 2))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(result + 2)))));
    if (((*(unsigned __int8 *)(result + 16)) & (1)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(result + 2)); }
    a1 = (unsigned int)(*(unsigned int *)(result + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < 0x80000000ULL) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4))); }
    result = (unsigned int)(v_stack_mE4);
    if (((unsigned int)(a1)) > ((unsigned int)((unsigned int)(v_stack_mE4)))) { result = (unsigned int)(a1); }
    v_stack_mE4 = (unsigned int)(result);
    a2 = (unsigned __int16)(a1);
    if (((unsigned int)((unsigned __int16)(a1))) <= v_stack_mD0) { a2 = v_stack_mD0; }
    v_stack_mD0 = (unsigned int)(a2);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 140)) & (1)) != 0) goto loc_008B1E23;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(result), v_stack_mC0, result, (unsigned int)(v_stack_mC8));
loc_008B1C3B:
    v_stack_mF0 = 1;
    v_stack_mF8 = v_stack_mE0;
    result = CmpAddValueToListEx(*(unsigned __int64 *)(result), (unsigned int)((unsigned int)((unsigned int)(v_stack_mD8))), (unsigned int)(v_stack_mE0), 1);
    if (sign_flag) goto loc_008B1DB8;
    goto loc_008B1B71;
loc_008B1C75:
    if (v_stack_mE0 == 0) goto loc_008B1CAC;
    a2 = (*(unsigned __int64 *)(result + 16)) + (36);
    v_stack_mF8 = v_stack_mB8;
    result = CmpConcatenateValueLists(*(unsigned __int64 *)(result), a2, v_stack_mE0, (unsigned int)(v_stack_mC8));
    if (sign_flag) goto loc_008B1DB8;
loc_008B1CAC:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 16) + 13)) >= 0) goto loc_008B1E6E;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(result), (unsigned int)(*(unsigned int *)(result + 8)), a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    if (result == 0) goto loc_008B1E6E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 56)) < ((unsigned int)(v_stack_mE8))) goto loc_008B1E4D;
loc_008B1CF2:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(v_stack_mB4))) == ((unsigned int)(v_rbx))) goto loc_008B1D27;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(result), (unsigned int)(*(unsigned int *)(result + 8)), a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 40)))) != ((unsigned int)(v_rbx))) goto loc_008B1E2D;
loc_008B1D27:
    if (!sign_flag) goto loc_008B1D61;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 16) + 13)) & (127));
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 16) + 13) = (unsigned __int8)(result);
    *(unsigned int *)(*(unsigned __int64 *)(result + 16) + 48) = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(result + 16) + 74) = (unsigned __int16)(v_stack_mE8);
    if (result == 0) goto loc_008B1D61;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 56)) < ((unsigned int)((unsigned __int16)(v_stack_mE8)))) goto loc_008B1EB6;
loc_008B1D61:
    if (((unsigned int)((unsigned int)(v_stack_mB4))) == ((unsigned int)(v_rbx))) goto loc_008B1DB6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 40)))) != ((unsigned int)(v_rbx))) goto loc_008B1EBE;
loc_008B1D75:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 36) = v_stack_mB8;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 64)) < ((unsigned int)((unsigned int)(v_stack_mE4)))) {
        *(unsigned int *)(*(unsigned __int64 *)(result + 16) + 64) = (unsigned int)((unsigned int)(v_stack_mE4));
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 60)) < ((unsigned int)((unsigned int)(v_stack_mD0)))) {
        *(unsigned int *)(*(unsigned __int64 *)(result + 16) + 60) = (unsigned int)((unsigned int)(v_stack_mD0));
    }
    result = HvFreeCell(*(unsigned __int64 *)(result), (unsigned int)(v_stack_mDC), a3, a4);
    v_stack_mDC = (unsigned int)(v_rbx);
loc_008B1DB6:
    v_rbx = 0;
loc_008B1DB8:
    result = CmpValueEnumStackCleanup(v_stack_mA8, (unsigned int)(v_stack_mDC), a3, a4);
    v_rdi = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (v_stack_mDC != ((unsigned int)(v_rdi))) goto loc_008B1ECB;
loc_008B1DCD:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != ((unsigned int)(v_rdi))) goto loc_008B1EDD;
loc_008B1DD6:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != ((unsigned int)(v_rdi))) goto loc_008B1EED;
loc_008B1DDF:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(v_stack_mDC), a3, a4);
    v_rsp = (v_rsp) + (224);
    return result;
loc_008B1E09:
    result = HvpGetCellPaged(a1, (unsigned int)(v_stack_mDC), a3, a4);
    goto loc_008B1BE2;
loc_008B1E13:
    a2 = (unsigned __int16)(((unsigned int)(v_stack_mDC)) - 1);
    goto loc_008B1B18;
loc_008B1E1B:
    goto loc_008B1AF8;
loc_008B1E23:
    result = HvpReleaseCellFlat(a1, a2, a3, a4);
    goto loc_008B1C3B;
loc_008B1E2D:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(v_rdi), a2, a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) | (0xFFFFFFFFULL));
    goto loc_008B1D27;
loc_008B1E4D:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + 8)), a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    goto loc_008B1CF2;
loc_008B1E6E:
    goto loc_008B1CF2;
loc_008B1E79:
    v_stack_p20 = v_stack_p34;
    result = CmpCopyCell(*(unsigned __int64 *)(result), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result)) + 48)), *(unsigned __int64 *)(result), a4);
    if (sign_flag) goto loc_008B1DB8;
    v_stack_p30 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mD0 + 16) + 74));
    goto loc_008B1B4B;
loc_008B1EB6:
    *(unsigned int *)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mD0 + 16) + 74) + 56) = (unsigned int)(*(unsigned __int64 *)(result));
    goto loc_008B1D61;
loc_008B1EBE:
    result = HvFreeCell(*(unsigned __int64 *)(v_rdi), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result)) + 48)), *(unsigned __int64 *)(result), a4);
    goto loc_008B1D75;
loc_008B1ECB:
    result = CmpFreeKeyValueList(*(unsigned __int64 *)(result), v_stack_p38, *(unsigned __int64 *)(result), a4);
    goto loc_008B1DCD;
loc_008B1EDD:
    result = HvFreeCell(*(unsigned __int64 *)(result), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))), *(unsigned __int64 *)(result), a4);
    goto loc_008B1DD6;
loc_008B1EED:
    result = HvFreeCell(*(unsigned __int64 *)(result), (unsigned int)((unsigned int)((unsigned int)(v_stack_p34))), *(unsigned __int64 *)(result), a4);
    goto loc_008B1DDF;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFullPromoteSingleKeyFromKeyNodeStacks(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m98;
    uint16_t v_stack_mA2;
    uint64_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint16_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint16_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint16_t v_stack_p30;
    uint64_t v_stack_p34;
    uint64_t v_stack_p38;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x558CDD)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = (uint32_t)((local_rdi) | (0xFFFFFFFFULL));
    local_rsi = 0;
    v_stack_mC0 = 0;
    v_stack_mE4 = (uint32_t)(local_rdi);
    v_stack_mE8 = 0;
    v_stack_mDC = (uint32_t)(local_rdi);
    v_stack_mE0 = 0;
    v_stack_mB4 = (uint32_t)(local_rdi);
    v_stack_mB8 = 0;
    v_stack_mD8 = (uint32_t)(local_rdi);
    result = HvpGetCellContextInitialize(v_stack_mC0, Arg2, a3, a4);
    Arg2 = 0;
    result = memset(v_stack_mA4, Arg2, local_rsi + 84, a4);
    v_stack_mA8 = (uint32_t)(local_rdi);
loc_008B1ABF:
    result = CmpValueEnumStackEntryInitialize(v_stack_m98, v_stack_m98, local_rsi + 2, a4);
    Arg2 = (v_stack_m98) + (32);
    a3 = (local_rsi + 2) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_008B1ABF;
    v_stack_mD4 = (uint16_t)(*(uint16_t *)(arg2));
    result = CmpKeyNodeStackGetEntryAtLayerHeight(Arg2, *(uint16_t *)(arg2), a3, a4);
    if (Arg1 == 0) goto loc_008B1E1B;
    result = CmpKeyNodeStackGetEntryAtLayerHeight(Arg1, *(uint16_t *)(arg2), a3, a4);
loc_008B1AF8:
    local_r10 = 0;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) >> (31));
    v_stack_mC8 = (uint32_t)(a4);
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x10) + 0xD)) >= 0) goto loc_008B1B4B;
    Arg2 = (uint16_t)((*(uint16_t *)(arg2)) - ((uint16_t)(local_rsi + 1)));
loc_008B1B18:
    if (sign_flag) goto loc_008B1B4B;
    result = CmpKeyNodeStackGetEntryAtLayerHeight(Arg2, Arg2, a3, a4);
    v_stack_mD0 = result;
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_008B1E13;
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x10) + 0xD)) < 0) goto loc_008B1E13;
    if ((*(uint16_t *)(*(uint64_t *)(result + 0x10) + 0x4A)) != 0) goto loc_008B1E79;
loc_008B1B4B:
    result = CmpValueEnumStackStartFromKeyNodeStack(v_stack_mA8, Arg2, a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    Arg1 = 0;
    Arg2 = 0;
    v_stack_mE4 = 0;
    v_stack_mD0 = 0;
loc_008B1B71:
    result = CmpValueEnumStackAdvance(v_stack_mA8, Arg2, a3, a4);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_008B1C75;
    if (sign_flag) goto loc_008B1DB8;
    if (v_stack_mA2 == ((uint16_t)(v_stack_mD4))) goto loc_008B1B71;
    result = CmpValueEnumStackGetCurrentValueHive(v_stack_mA8, Arg2, a3, a4);
    v_stack_mF8 = v_stack_mD8;
    result = CmpCopyValue(result, (uint32_t)(v_stack_mA8), *(uint64_t *)(result), (uint32_t)(v_stack_mC8));
    if (sign_flag) goto loc_008B1DB8;
    if (((*(uint8_t *)(*(uint64_t *)(result) + 0x8C)) & (1)) == 0) goto loc_008B1E09;
    result = HvpGetCellFlat(*(uint64_t *)(result), (uint32_t)((uint32_t)((uint32_t)(v_stack_mD8))), v_stack_mC0, (uint32_t)(v_stack_mC8));
loc_008B1BE2:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x2))) + ((uint16_t)((uint16_t)(*(uint16_t *)(result + 0x2)))));
    if (((*(uint8_t *)(result + 0x10)) & (1)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(result + 0x2)); }
    Arg1 = (uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < 0x80000000ULL) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))); }
    result = (uint32_t)(v_stack_mE4);
    if (((uint32_t)(Arg1)) > ((uint32_t)((uint32_t)(v_stack_mE4)))) { result = (uint32_t)(Arg1); }
    v_stack_mE4 = (uint32_t)(result);
    Arg2 = (uint16_t)(Arg1);
    if (((uint32_t)((uint16_t)(Arg1))) <= v_stack_mD0) { Arg2 = v_stack_mD0; }
    v_stack_mD0 = (uint32_t)(Arg2);
    if (((*(uint8_t *)(*(uint64_t *)(result) + 0x8C)) & (1)) != 0) goto loc_008B1E23;
    result = HvpReleaseCellPaged(*(uint64_t *)(result), v_stack_mC0, result, (uint32_t)(v_stack_mC8));
loc_008B1C3B:
    v_stack_mF0 = 1;
    v_stack_mF8 = v_stack_mE0;
    result = CmpAddValueToListEx(*(uint64_t *)(result), (uint32_t)((uint32_t)((uint32_t)(v_stack_mD8))), (uint32_t)(v_stack_mE0), 1);
    if (sign_flag) goto loc_008B1DB8;
    goto loc_008B1B71;
loc_008B1C75:
    if (v_stack_mE0 == 0) goto loc_008B1CAC;
    Arg2 = (*(uint64_t *)(result + 0x10)) + (36);
    v_stack_mF8 = v_stack_mB8;
    result = CmpConcatenateValueLists(*(uint64_t *)(result), Arg2, v_stack_mE0, (uint32_t)(v_stack_mC8));
    if (sign_flag) goto loc_008B1DB8;
loc_008B1CAC:
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x10) + 0xD)) >= 0) goto loc_008B1E6E;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(result), (uint32_t)(*(uint32_t *)(result + 0x8)), a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    if (result == 0) goto loc_008B1E6E;
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x38)) < ((uint32_t)(v_stack_mE8))) goto loc_008B1E4D;
loc_008B1CF2:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(v_stack_mB4))) == ((uint32_t)(local_rbx))) goto loc_008B1D27;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(result), (uint32_t)(*(uint32_t *)(result + 0x8)), a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x28)))) != ((uint32_t)(local_rbx))) goto loc_008B1E2D;
loc_008B1D27:
    if (!sign_flag) goto loc_008B1D61;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(result + 0x10) + 0xD)) & (127));
    *(uint8_t *)(*(uint64_t *)(result + 0x10) + 0xD) = (uint8_t)(result);
    *(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x30) = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    *(uint16_t *)(*(uint64_t *)(result + 0x10) + 0x4A) = (uint16_t)(v_stack_mE8);
    if (result == 0) goto loc_008B1D61;
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x38)) < ((uint32_t)((uint16_t)(v_stack_mE8)))) goto loc_008B1EB6;
loc_008B1D61:
    if (((uint32_t)((uint32_t)(v_stack_mB4))) == ((uint32_t)(local_rbx))) goto loc_008B1DB6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x28)))) != ((uint32_t)(local_rbx))) goto loc_008B1EBE;
loc_008B1D75:
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x24) = v_stack_mB8;
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x40)) < ((uint32_t)((uint32_t)(v_stack_mE4)))) {
        *(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x40) = (uint32_t)((uint32_t)(v_stack_mE4));
    }
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x3C)) < ((uint32_t)((uint32_t)(v_stack_mD0)))) {
        *(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x3C) = (uint32_t)((uint32_t)(v_stack_mD0));
    }
    result = HvFreeCell(*(uint64_t *)(result), (uint32_t)(v_stack_mDC), a3, a4);
    v_stack_mDC = (uint32_t)(local_rbx);
loc_008B1DB6:
    local_rbx = 0;
loc_008B1DB8:
    result = CmpValueEnumStackCleanup(v_stack_mA8, (uint32_t)(v_stack_mDC), a3, a4);
    local_rdi = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (v_stack_mDC != ((uint32_t)(local_rdi))) goto loc_008B1ECB;
loc_008B1DCD:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != ((uint32_t)(local_rdi))) goto loc_008B1EDD;
loc_008B1DD6:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != ((uint32_t)(local_rdi))) goto loc_008B1EED;
loc_008B1DDF:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(v_stack_mDC), a3, a4);
    local_rsp = (local_rsp) + (224);
    return result;
loc_008B1E09:
    result = HvpGetCellPaged(Arg1, (uint32_t)(v_stack_mDC), a3, a4);
    goto loc_008B1BE2;
loc_008B1E13:
    Arg2 = (uint16_t)(((uint32_t)(v_stack_mDC)) - 1);
    goto loc_008B1B18;
loc_008B1E1B:
    goto loc_008B1AF8;
loc_008B1E23:
    result = HvpReleaseCellFlat(Arg1, Arg2, a3, a4);
    goto loc_008B1C3B;
loc_008B1E2D:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(local_rdi), Arg2, a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) | (0xFFFFFFFFULL));
    goto loc_008B1D27;
loc_008B1E4D:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + 0x8)), a3, a4);
    if (sign_flag) goto loc_008B1DB8;
    goto loc_008B1CF2;
loc_008B1E6E:
    goto loc_008B1CF2;
loc_008B1E79:
    v_stack_p20 = v_stack_p34;
    result = CmpCopyCell(*(uint64_t *)(result), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result)) + 0x30)), *(uint64_t *)(result), a4);
    if (sign_flag) goto loc_008B1DB8;
    v_stack_p30 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_mD0 + 0x10) + 0x4A));
    goto loc_008B1B4B;
loc_008B1EB6:
    *(uint32_t *)(*(uint16_t *)(*(uint64_t *)(v_stack_mD0 + 0x10) + 0x4A) + 0x38) = (uint32_t)(*(uint64_t *)(result));
    goto loc_008B1D61;
loc_008B1EBE:
    result = HvFreeCell(*(uint64_t *)(local_rdi), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result)) + 0x30)), *(uint64_t *)(result), a4);
    goto loc_008B1D75;
loc_008B1ECB:
    result = CmpFreeKeyValueList(*(uint64_t *)(result), v_stack_p38, *(uint64_t *)(result), a4);
    goto loc_008B1DCD;
loc_008B1EDD:
    result = HvFreeCell(*(uint64_t *)(result), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))), *(uint64_t *)(result), a4);
    goto loc_008B1DD6;
loc_008B1EED:
    result = HvFreeCell(*(uint64_t *)(result), (uint32_t)((uint32_t)((uint32_t)(v_stack_p34))), *(uint64_t *)(result), a4);
    goto loc_008B1DDF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B1A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
