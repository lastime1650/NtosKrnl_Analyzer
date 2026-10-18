# MiDemoteLocalLargePage

- RVA: `0x0028A4F0`–`0x0028A996` (길이 `1,190` bytes)
- VA: `0x000000014028A4F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066EB8`
- 디코드: `300`개 명령, `1,190/1,190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0028A589` → [MiPreemptivePageDemoteAmount](MiPreemptivePageDemoteAmount_function_0028B338.md) (function, `0x0028B338`)
- `0x0028A5FE` → [MiCacheAttributeHasValue](MiCacheAttributeHasValue_function_0028A14C.md) (function, `0x0028A14C`)
- `0x0028A67A` → [MiGetPage](MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0028A6EB` → [MiCacheAttributeHasValue](MiCacheAttributeHasValue_function_0028A14C.md) (function, `0x0028A14C`)
- `0x0028A702` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0028A755` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0028A788` → [MiIsFreeZeroPfnCold](../31/MiIsFreeZeroPfnCold_function_0031E5E4.md) (function, `0x0031E5E4`)
- `0x0028A80C` → [MiInsertDemotedPages](../43/MiInsertDemotedPages_function_004354B8.md) (function, `0x004354B8`)
- `0x0028A814` → [MiGetPfnPageSizeIndex](../31/MiGetPfnPageSizeIndex_function_0031C710.md) (function, `0x0031C710`)
- `0x0028A898` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0028A8CB` → [MiGetPage](MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0028A923` → [MiChangePageHeatImmediate](../44/MiChangePageHeatImmediate_function_00445F5C.md) (function, `0x00445F5C`)
- `0x0028A92D` → [MiSetFreeZeroPfnCold](../37/MiSetFreeZeroPfnCold_function_00379428.md) (function, `0x00379428`)
- `0x0028A950` → [MiCacheAttributeHasValue](MiCacheAttributeHasValue_function_0028A14C.md) (function, `0x0028A14C`)
- `0x0028A96E` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x0028A98C` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)

### Direct callers
- [MiGetPage](MiGetPage_function_002884C0.md) at `0x002889E2`
- [MiGetPage](MiGetPage_function_002884C0.md) at `0x00289271`
- [MiGetFreeOrZeroPageAnyColor](../43/MiGetFreeOrZeroPageAnyColor_function_004352D8.md) at `0x004353E7`

### Static image references
- `0x0028A5EB` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0028A607` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0028A90B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0028A4F0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0028A4F5  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0028A4FA  55                              push rbp
0028A4FB  56                              push rsi
0028A4FC  57                              push rdi
0028A4FD  41 54                           push r12
0028A4FF  41 55                           push r13
0028A501  41 56                           push r14
0028A503  41 57                           push r15
0028A505  48 83 EC 40                     sub rsp, 0x40
0028A509  8B FA                           mov edi, edx
0028A50B  41 8B D8                        mov ebx, r8d
0028A50E  41 0F BA E0 0E                  bt r8d, 0xe
0028A513  0F 82 A7 01 00 00               jb 0x14028a6c0
0028A519  44 8B E7                        mov r12d, edi
0028A51C  33 D2                           xor edx, edx
0028A51E  41 C1 EC 10                     shr r12d, 0x10
0028A522  45 8B F4                        mov r14d, r12d
0028A525  41 83 E6 03                     and r14d, 3
0028A529  41 8B F6                        mov esi, r14d
0028A52C  0F 84 8E 01 00 00               je 0x14028a6c0
0028A532  8B C7                           mov eax, edi
0028A534  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
0028A538  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0028A53D  4F 8D 1C B6                     lea r11, [r14 + r14*4]
0028A541  48 C1 E8 09                     shr rax, 9
0028A545  44 8B EF                        mov r13d, edi
0028A548  83 E0 3F                        and eax, 0x3f
0028A54B  41 C1 ED 12                     shr r13d, 0x12
0028A54F  4C 69 C0 80 DF 00 00            imul r8, rax, 0xdf80
0028A556  49 C1 E3 08                     shl r11, 8
0028A55A  41 83 E5 03                     and r13d, 3
0028A55E  4C 03 41 10                     add r8, qword ptr [rcx + 0x10]
0028A562  44 8B D7                        mov r10d, edi
0028A565  41 C1 EA 0F                     shr r10d, 0xf
0028A569  4D 03 D8                        add r11, r8
0028A56C  41 83 E2 01                     and r10d, 1
0028A570  44 89 AC 24 90 00 00 00         mov dword ptr [rsp + 0x90], r13d
0028A578  83 FE 03                        cmp esi, 3
0028A57B  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0028A580  49 8B C8                        mov rcx, r8
0028A583  44 0F 44 D2                     cmove r10d, edx
0028A587  8B D7                           mov edx, edi
0028A589  E8 AA 0D 00 00                  call 0x14028b338
0028A58E  4A 8D 0C 95 00 00 00 00         lea rcx, [r10*4]
0028A596  49 03 CD                        add rcx, r13
0028A599  49 8B 4C CB 18                  mov rcx, qword ptr [r11 + rcx*8 + 0x18]
0028A59E  48 3B C8                        cmp rcx, rax
0028A5A1  0F 83 19 01 00 00               jae 0x14028a6c0
0028A5A7  B8 02 00 00 00                  mov eax, 2
0028A5AC  0F BA E3 0F                     bt ebx, 0xf
0028A5B0  0F 83 78 01 00 00               jae 0x14028a72e
0028A5B6  44 8D 78 01                     lea r15d, [rax + 1]
0028A5BA  45 33 C9                        xor r9d, r9d
0028A5BD  44 3B FE                        cmp r15d, esi
0028A5C0  0F 83 FA 00 00 00               jae 0x14028a6c0
0028A5C6  83 E3 DF                        and ebx, 0xffffffdf
0028A5C9  44 89 8C 24 98 00 00 00         mov dword ptr [rsp + 0x98], r9d
0028A5D1  81 CB 04 76 03 00               or ebx, 0x37604
0028A5D7  F6 C3 01                        test bl, 1
0028A5DA  0F 85 FB 00 00 00               jne 0x14028a6db
0028A5E0  83 CB 01                        or ebx, 1
0028A5E3  44 0F 20 C5                     mov rbp, cr8
0028A5E7  44 0F 22 C0                     mov cr8, rax
0028A5EB  44 39 0D 2E C7 D3 00            cmp dword ptr [rip + 0xd3c72e], r9d
0028A5F2  0F 85 05 01 00 00               jne 0x14028a6fd
0028A5F8  41 8B CD                        mov ecx, r13d
0028A5FB  45 8B C5                        mov r8d, r13d
0028A5FE  E8 49 FB FF FF                  call 0x14028a14c
0028A603  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0028A607  4C 8D 1D F2 59 D7 FF            lea r11, [rip - 0x28a60e]
0028A60E  85 C0                           test eax, eax
0028A610  0F 84 D6 02 00 00               je 0x14028a8ec
0028A616  83 FE 03                        cmp esi, 3
0028A619  75 04                           jne 0x14028a61f
0028A61B  0F BA F7 0F                     btr edi, 0xf
0028A61F  FF CE                           dec esi
0028A621  41 BA 01 00 00 00               mov r10d, 1
0028A627  8B C6                           mov eax, esi
0028A629  C1 E0 10                        shl eax, 0x10
0028A62C  33 C7                           xor eax, edi
0028A62E  25 00 00 03 00                  and eax, 0x30000
0028A633  48 8D 0C B6                     lea rcx, [rsi + rsi*4]
0028A637  33 F8                           xor edi, eax
0028A639  48 C1 E1 08                     shl rcx, 8
0028A63D  48 03 4C 24 28                  add rcx, qword ptr [rsp + 0x28]
0028A642  41 8B C2                        mov eax, r10d
0028A645  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
0028A649  33 D2                           xor edx, edx
0028A64B  8B CF                           mov ecx, edi
0028A64D  48 C1 E9 10                     shr rcx, 0x10
0028A651  83 E3 F7                        and ebx, 0xfffffff7
0028A654  83 E1 03                        and ecx, 3
0028A657  41 F7 B4 8B C0 DC E2 00         div dword ptr [r11 + rcx*4 + 0xe2dcc0]
0028A65F  33 D7                           xor edx, edi
0028A661  0F B6 C2                        movzx eax, dl
0028A664  33 F8                           xor edi, eax
0028A666  85 F6                           test esi, esi
0028A668  75 79                           jne 0x14028a6e3
0028A66A  83 CB 08                        or ebx, 8
0028A66D  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0028A675  44 8B C3                        mov r8d, ebx
0028A678  8B D7                           mov edx, edi
0028A67A  E8 41 DE FF FF                  call 0x1402884c0
0028A67F  4C 8B C8                        mov r9, rax
0028A682  48 83 F8 FF                     cmp rax, -1
0028A686  0F 85 DB 00 00 00               jne 0x14028a767
0028A68C  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
0028A694  4C 8D 1D 65 59 D7 FF            lea r11, [rip - 0x28a69b]
0028A69B  41 3B F7                        cmp esi, r15d
0028A69E  0F 85 7B FF FF FF               jne 0x14028a61f
0028A6A4  41 83 FE 03                     cmp r14d, 3
0028A6A8  0F 94 C1                        sete cl
0028A6AB  0F BA E7 0F                     bt edi, 0xf
0028A6AF  0F 93 C0                        setae al
0028A6B2  84 C8                           test al, cl
0028A6B4  75 56                           jne 0x14028a70c
0028A6B6  40 80 FD 02                     cmp bpl, 2
0028A6BA  0F 82 84 00 00 00               jb 0x14028a744
0028A6C0  33 C0                           xor eax, eax
0028A6C2  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0028A6CA  48 83 C4 40                     add rsp, 0x40
0028A6CE  41 5F                           pop r15
0028A6D0  41 5E                           pop r14
0028A6D2  41 5D                           pop r13
0028A6D4  41 5C                           pop r12
0028A6D6  5F                              pop rdi
0028A6D7  5E                              pop rsi
0028A6D8  5D                              pop rbp
0028A6D9  C3                              ret
0028A6DA  CC                              int3
0028A6DB  40 B5 11                        mov bpl, 0x11
0028A6DE  E9 15 FF FF FF                  jmp 0x14028a5f8
0028A6E3  41 3B F2                        cmp esi, r10d
0028A6E6  75 85                           jne 0x14028a66d
0028A6E8  41 8B C8                        mov ecx, r8d
0028A6EB  E8 5C FA FF FF                  call 0x14028a14c
0028A6F0  85 C0                           test eax, eax
0028A6F2  0F 84 72 FF FF FF               je 0x14028a66a
0028A6F8  E9 70 FF FF FF                  jmp 0x14028a66d
0028A6FD  8A D0                           mov dl, al
0028A6FF  40 8A CD                        mov cl, bpl
0028A702  E8 F5 AF 26 00                  call 0x1404f56fc
0028A707  E9 EC FE FF FF                  jmp 0x14028a5f8
0028A70C  41 8B C4                        mov eax, r12d
0028A70F  4C 8D 1D EA 58 D7 FF            lea r11, [rip - 0x28a716]
0028A716  C1 E0 10                        shl eax, 0x10
0028A719  41 8B F6                        mov esi, r14d
0028A71C  33 C7                           xor eax, edi
0028A71E  25 00 00 03 00                  and eax, 0x30000
0028A723  33 F8                           xor edi, eax
0028A725  0F BA EF 0F                     bts edi, 0xf
0028A729  E9 F1 FE FF FF                  jmp 0x14028a61f
0028A72E  41 B9 00 00 00 00               mov r9d, 0
0028A734  0F BA E3 0B                     bt ebx, 0xb
0028A738  45 8B F9                        mov r15d, r9d
0028A73B  44 0F 42 F8                     cmovb r15d, eax
0028A73F  E9 79 FE FF FF                  jmp 0x14028a5bd
0028A744  33 D2                           xor edx, edx
0028A746  39 15 D4 C5 D3 00               cmp dword ptr [rip + 0xd3c5d4], edx
0028A74C  74 0C                           je 0x14028a75a
0028A74E  44 0F 20 C1                     mov rcx, cr8
0028A752  40 8A D5                        mov dl, bpl
0028A755  E8 3E AF 26 00                  call 0x1404f5698
0028A75A  40 0F B6 C5                     movzx eax, bpl
0028A75E  44 0F 22 C0                     mov cr8, rax
0028A762  E9 59 FF FF FF                  jmp 0x14028a6c0
0028A767  41 BC 01 00 00 00               mov r12d, 1
0028A76D  45 8B F4                        mov r14d, r12d
0028A770  4B 8D 1C 49                     lea rbx, [r9 + r9*2]
0028A774  48 C1 E3 04                     shl rbx, 4
0028A778  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028A782  48 03 D8                        add rbx, rax
0028A785  48 8B CB                        mov rcx, rbx
0028A788  E8 57 3E 09 00                  call 0x14031e5e4
0028A78D  45 33 FF                        xor r15d, r15d
0028A790  85 C0                           test eax, eax
0028A792  0F 85 73 01 00 00               jne 0x14028a90b
0028A798  48 8B FB                        mov rdi, rbx
0028A79B  45 85 F6                        test r14d, r14d
0028A79E  74 79                           je 0x14028a819
0028A7A0  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0028A7A3  C1 E8 10                        shr eax, 0x10
0028A7A6  0F B6 C8                        movzx ecx, al
0028A7A9  C1 E9 06                        shr ecx, 6
0028A7AC  85 F6                           test esi, esi
0028A7AE  0F 84 83 01 00 00               je 0x14028a937
0028A7B4  41 3B CD                        cmp ecx, r13d
0028A7B7  8B D1                           mov edx, ecx
0028A7B9  41 0F 45 D5                     cmovne edx, r13d
0028A7BD  41 3B F4                        cmp esi, r12d
0028A7C0  0F 84 7F 01 00 00               je 0x14028a945
0028A7C6  41 3B CD                        cmp ecx, r13d
0028A7C9  0F 85 96 01 00 00               jne 0x14028a965
0028A7CF  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0028A7D4  4C 8D 05 25 58 D7 FF            lea r8, [rip - 0x28a7db]
0028A7DB  44 8B 4C 24 24                  mov r9d, dword ptr [rsp + 0x24]
0028A7E0  8D 4E 01                        lea ecx, [rsi + 1]
0028A7E3  49 0F AF 84 C8 60 1C 01 00      imul rax, qword ptr [r8 + rcx*8 + 0x11c60]
0028A7EC  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
0028A7F1  33 D2                           xor edx, edx
0028A7F3  49 F7 B4 F0 60 1C 01 00         div qword ptr [r8 + rsi*8 + 0x11c60]
0028A7FB  48 8D 3C 52                     lea rdi, [rdx + rdx*2]
0028A7FF  48 8B D3                        mov rdx, rbx
0028A802  48 C1 E7 04                     shl rdi, 4
0028A806  48 03 FB                        add rdi, rbx
0028A809  4C 8B C7                        mov r8, rdi
0028A80C  E8 A7 AC 1A 00                  call 0x1404354b8
0028A811  48 8B CF                        mov rcx, rdi
0028A814  E8 F7 1E 09 00                  call 0x14031c710
0028A819  83 FE 02                        cmp esi, 2
0028A81C  49 C7 C1 00 00 FF FF            mov r9, 0xffffffffffff0000
0028A823  4D 1B C0                        sbb r8, r8
0028A826  41 83 E0 08                     and r8d, 8
0028A82A  49 81 C0 58 3B 00 00            add r8, 0x3b58
0028A831  4C 03 44 24 28                  add r8, qword ptr [rsp + 0x28]
0028A836  49 8B 00                        mov rax, qword ptr [r8]
0028A839  48 8D 50 FF                     lea rdx, [rax - 1]
0028A83D  48 8B C8                        mov rcx, rax
0028A840  48 33 CA                        xor rcx, rdx
0028A843  49 23 C9                        and rcx, r9
0028A846  48 33 CA                        xor rcx, rdx
0028A849  66 85 C9                        test cx, cx
0028A84C  75 10                           jne 0x14028a85e
0028A84E  48 8D 91 00 00 01 00            lea rdx, [rcx + 0x10000]
0028A855  48 33 D1                        xor rdx, rcx
0028A858  49 23 D1                        and rdx, r9
0028A85B  48 33 CA                        xor rcx, rdx
0028A85E  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
0028A863  75 D4                           jne 0x14028a839
0028A865  40 80 FD 02                     cmp bpl, 2
0028A869  72 1D                           jb 0x14028a888
0028A86B  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0028A86E  C1 E8 10                        shr eax, 0x10
0028A871  0F B6 C8                        movzx ecx, al
0028A874  C1 E9 06                        shr ecx, 6
0028A877  41 3B CD                        cmp ecx, r13d
0028A87A  0F 85 F8 00 00 00               jne 0x14028a978
0028A880  48 8B C7                        mov rax, rdi
0028A883  E9 3A FE FF FF                  jmp 0x14028a6c2
0028A888  44 39 3D 91 C4 D3 00            cmp dword ptr [rip + 0xd3c491], r15d
0028A88F  74 0C                           je 0x14028a89d
0028A891  44 0F 20 C1                     mov rcx, cr8
0028A895  40 8A D5                        mov dl, bpl
0028A898  E8 FB AD 26 00                  call 0x1404f5698
0028A89D  40 0F B6 C5                     movzx eax, bpl
0028A8A1  44 0F 22 C0                     mov cr8, rax
0028A8A5  EB C4                           jmp 0x14028a86b
0028A8A7  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0028A8AF  44 8B C3                        mov r8d, ebx
0028A8B2  0F BA F7 13                     btr edi, 0x13
0028A8B6  C7 84 24 90 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x90], 1
0028A8C1  0F BA EF 12                     bts edi, 0x12
0028A8C5  41 83 C8 08                     or r8d, 8
0028A8C9  8B D7                           mov edx, edi
0028A8CB  E8 F0 DB FF FF                  call 0x1402884c0
0028A8D0  4C 8B C8                        mov r9, rax
0028A8D3  48 83 F8 FF                     cmp rax, -1
0028A8D7  74 1E                           je 0x14028a8f7
0028A8D9  44 8B B4 24 98 00 00 00         mov r14d, dword ptr [rsp + 0x98]
0028A8E1  41 BC 01 00 00 00               mov r12d, 1
0028A8E7  E9 84 FE FF FF                  jmp 0x14028a770
0028A8EC  83 FE 03                        cmp esi, 3
0028A8EF  0F 84 26 FD FF FF               je 0x14028a61b
0028A8F5  EB B0                           jmp 0x14028a8a7
0028A8F7  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
0028A8FF  4C 8D 1D FA 56 D7 FF            lea r11, [rip - 0x28a906]
0028A906  E9 0B FD FF FF                  jmp 0x14028a616
0028A90B  F7 05 A3 C1 D3 00 00 00 20 00   test dword ptr [rip + 0xd3c1a3], 0x200000
0028A915  0F 84 7D FE FF FF               je 0x14028a798
0028A91B  45 8B C4                        mov r8d, r12d
0028A91E  8B D6                           mov edx, esi
0028A920  49 8B C9                        mov rcx, r9
0028A923  E8 34 B6 1B 00                  call 0x140445f5c
0028A928  33 D2                           xor edx, edx
0028A92A  48 8B CB                        mov rcx, rbx
0028A92D  E8 F6 EA 0E 00                  call 0x140379428
0028A932  E9 61 FE FF FF                  jmp 0x14028a798
0028A937  41 3B CC                        cmp ecx, r12d
0028A93A  0F 84 8F FE FF FF               je 0x14028a7cf
0028A940  E9 6F FE FF FF                  jmp 0x14028a7b4
0028A945  44 39 7C 24 20                  cmp dword ptr [rsp + 0x20], r15d
0028A94A  0F 85 76 FE FF FF               jne 0x14028a7c6
0028A950  E8 F7 F7 FF FF                  call 0x14028a14c
0028A955  85 C0                           test eax, eax
0028A957  0F 85 72 FE FF FF               jne 0x14028a7cf
0028A95D  41 8B D4                        mov edx, r12d
0028A960  E9 61 FE FF FF                  jmp 0x14028a7c6
0028A965  41 B8 10 00 00 00               mov r8d, 0x10
0028A96B  48 8B CB                        mov rcx, rbx
0028A96E  E8 59 85 0A 00                  call 0x140332ecc
0028A973  E9 57 FE FF FF                  jmp 0x14028a7cf
0028A978  40 80 FD 02                     cmp bpl, 2
0028A97C  41 8B D5                        mov edx, r13d
0028A97F  48 8B CF                        mov rcx, rdi
0028A982  45 1B C0                        sbb r8d, r8d
0028A985  41 F7 D0                        not r8d
0028A988  41 83 E0 10                     and r8d, 0x10
0028A98C  E8 3B 85 0A 00                  call 0x140332ecc
0028A991  E9 EA FE FF FF                  jmp 0x14028a880
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDemoteLocalLargePage(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p90;
    unsigned int v_stack_p98;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    if (condition_is_below) goto loc_0028A6C0;
    a2 = 0;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (16));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (3));
    if (condition_is_equal) goto loc_0028A6C0;
    v_stack_m54 = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    v_stack_m48 = (unsigned int)((unsigned int)((unsigned int)(a2)));
    result = ((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (9);
    result = (unsigned int)((result) & (63));
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (18));
    a3 = (a3) * (result);
    v_r11 = (v_r14 + v_r14 * 4) << (8);
    v_r13 = (unsigned int)((v_r13) & (3));
    a3 = (a3) + (*(unsigned __int64 *)(a1 + 16));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (15));
    v_r11 = (v_r11) + (a3);
    v_r10 = (unsigned int)((v_r10) & (1));
    v_stack_p18 = (unsigned int)(v_r13);
    v_stack_m50 = a3;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) == 3) { v_r10 = 0; }
    result = MiPreemptivePageDemoteAmount(a3, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    a1 = (v_r10 * 4) + (v_r13);
    if ((*(unsigned __int64 *)(v_r11 + a1 * 8 + 24)) >= result) goto loc_0028A6C0;
    if ((*(unsigned __int64 *)(v_r11 + a1 * 8 + 24)) >= result) goto loc_0028A72E;
    a4 = 0;
loc_0028A5BD:
    if (((unsigned int)(2 + 1)) >= ((unsigned int)((unsigned int)((unsigned int)(v_r14))))) goto loc_0028A6C0;
    v_rbx = (unsigned int)(((unsigned int)(a3)) & (0xFFFFFFDFULL));
    v_stack_p20 = 0;
    v_rbx = (unsigned int)((v_rbx) | (0x37604ULL));
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_0028A6DB;
    v_rbx = (unsigned int)((v_rbx) | (1));
    if ((*(unsigned int *)(v_rip + 13879086)) != 0) goto loc_0028A6FD;
loc_0028A5F8:
    result = MiCacheAttributeHasValue((unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)(v_r13)), a4);
    v_stack_m58 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_0028A8EC;
loc_0028A616:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) == 3) {
    }
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - 1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) << (16));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(a2))));
    result = (unsigned int)((result) & (0x30000ULL));
    v_rdi = (unsigned int)(((unsigned int)(a2)) ^ ((unsigned int)(result)));
    a1 = (v_rsi + v_rsi * 4) << (8);
    a1 = (a1) + (v_stack_m50);
    a2 = 0;
    a1 = ((unsigned int)((unsigned int)(v_rdi))) >> (16);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF7ULL));
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_rdi)));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned __int8)(a2))));
    if ((unsigned int)(v_rsi) != 0) goto loc_0028A6E3;
loc_0028A66A:
    v_rbx = (unsigned int)((v_rbx) | (8));
loc_0028A66D:
    result = MiGetPage(v_stack_p8, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_rbx)), a4);
    if (result != -1) goto loc_0028A767;
    if (((unsigned int)(v_rsi)) != ((unsigned int)(2 + 1))) goto loc_0028A61F;
    a1 = (((unsigned int)(v_r14)) == 3) ? 1 : 0;
    result = (((unsigned int)(v_r14)) >= 3) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0028A70C;
    if (((unsigned __int8)(v_cr8)) < 2) goto loc_0028A744;
loc_0028A6C0:
    result = 0;
loc_0028A6C2:
    v_rsp = (v_rsp) + (64);
    return result;
loc_0028A6DB:
    goto loc_0028A5F8;
loc_0028A6E3:
    if (((unsigned int)(v_rsi)) != 1) goto loc_0028A66D;
    result = MiCacheAttributeHasValue((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(v_stack_p18), result);
    if ((unsigned int)(result) == 0) goto loc_0028A66A;
    goto loc_0028A66D;
loc_0028A6FD:
    result = KiRaiseIrqlProcessIrqlFlags(17, (unsigned __int8)(result), (unsigned int)(v_stack_p18), result);
    goto loc_0028A5F8;
loc_0028A70C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) << (16));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rdi)));
    result = (unsigned int)((result) & (0x30000ULL));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(result)));
    goto loc_0028A61F;
loc_0028A72E:
    v_r15 = 0;
    if (condition_is_below) { v_r15 = (unsigned int)(result); }
    goto loc_0028A5BD;
loc_0028A744:
    a2 = 0;
    if ((*(unsigned int *)(v_rip + 13878740)) != 0) {
        a1 = 2;
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(v_stack_p18), 0);
    }
    goto loc_0028A6C0;
loc_0028A767:
loc_0028A770:
    v_rbx = (0 + 0 * 2) << (4);
    v_rbx = (v_rbx) + (17);
    result = MiIsFreeZeroPfnCold(v_rbx, a2, (unsigned int)(v_stack_p18), 0);
    v_r15 = 0;
    if ((unsigned int)(result) != 0) goto loc_0028A90B;
loc_0028A798:
    if (1 == 0) goto loc_0028A819;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if ((unsigned int)((unsigned int)((unsigned int)(v_r14))) == 0) goto loc_0028A937;
loc_0028A7B4:
    a2 = (unsigned int)((unsigned int)(a1));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r13))) { a2 = (unsigned int)(v_r13); }
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) == 1) goto loc_0028A945;
loc_0028A7C6:
    if (((unsigned int)(a1)) != ((unsigned int)(v_r13))) goto loc_0028A965;
loc_0028A7CF:
    result = (v_stack_p30) * (*(unsigned __int64 *)(v_rip - 2664411 + (unsigned int)((unsigned int)(v_r14)) + 1 * 8 + 72800));
    a2 = 0;
    v_rdi = (a2 + a2 * 2) << (4);
    v_rdi = (v_rdi) + (v_rbx);
    result = MiInsertDemotedPages(v_stack_p28, v_rbx, v_rdi, (unsigned int)(v_stack_p24));
    result = MiGetPfnPageSizeIndex(v_rdi, v_rbx, v_rdi, (unsigned int)(v_stack_p24));
loc_0028A819:
    a3 = (unsigned int)((v_rdi) & (8));
    a3 = (a3) + (0x3B58ULL);
    a3 = (a3) + (v_stack_p28);
loc_0028A839:
    a1 = (*(unsigned __int64 *)(a3)) ^ (*(unsigned __int64 *)(a3) - 1);
    a1 = (a1) & (0xFFFFFFFFFFFF0000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(a3) - 1);
    if ((unsigned __int16)(a1) == 0) {
        a2 = a1 + 65536;
        a2 = (a2) ^ (a1);
        a2 = (a2) & (0xFFFFFFFFFFFF0000ULL);
        a1 = (a1) ^ (a2);
    }
    if (condition_is_not_equal) goto loc_0028A839;
    if (17 < 2) goto loc_0028A888;
loc_0028A86B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r13))) goto loc_0028A978;
loc_0028A880:
    goto loc_0028A6C2;
loc_0028A888:
    result = v_rdi;
    if ((*(unsigned int *)(v_rip + 13878417)) != 0) {
        a1 = 17;
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, 0xFFFFFFFFFFFF0000ULL);
    }
    goto loc_0028A86B;
loc_0028A8A7:
    v_stack_p90 = 1;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) | (8));
    result = MiGetPage(v_stack_p80, (unsigned int)((unsigned int)(v_rdi)), a3, 0xFFFFFFFFFFFF0000ULL);
    if (result == -1) goto loc_0028A8F7;
    goto loc_0028A770;
loc_0028A8EC:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) == 3) goto loc_0028A61B;
    goto loc_0028A8A7;
loc_0028A8F7:
    goto loc_0028A616;
loc_0028A90B:
    if (((*(unsigned int *)(v_rip + 13877667)) & (0x200000ULL)) == 0) goto loc_0028A798;
    result = MiChangePageHeatImmediate(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14)))), 1, result);
    a2 = 0;
    result = MiSetFreeZeroPfnCold(v_rbx, a2, 1, result);
    goto loc_0028A798;
loc_0028A937:
    if (((unsigned int)(v_rbx)) == 1) goto loc_0028A7CF;
    goto loc_0028A7B4;
loc_0028A945:
    if (v_stack_p20 != 0) goto loc_0028A7C6;
    result = MiCacheAttributeHasValue(v_rbx, a2, 1, result);
    if ((unsigned int)(result) != 0) goto loc_0028A7CF;
    goto loc_0028A7C6;
loc_0028A965:
    result = MiChangePageAttribute(v_rbx, 1, 16, result);
    goto loc_0028A7CF;
loc_0028A978:
    a3 = (unsigned int)(~(16));
    a3 = (unsigned int)((a3) & (16));
    result = MiChangePageAttribute(v_rdi, (unsigned int)((unsigned int)(v_r13)), a3, result);
    goto loc_0028A880;
}
```

## 5. (Beta) C Style

```c
int64_t MiDemoteLocalLargePage(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_p90;
    uint32_t v_stack_p98;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    if (condition_is_below) goto loc_0028A6C0;
    Arg2 = 0;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (16));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (3));
    if (condition_is_equal) goto loc_0028A6C0;
    v_stack_m54 = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    v_stack_m48 = (uint32_t)((uint32_t)((uint32_t)(Arg2)));
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (9);
    result = (uint32_t)((result) & (63));
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (18));
    Arg3 = (Arg3) * (result);
    local_r11 = (local_r14 + local_r14 * 4) << (8);
    local_r13 = (uint32_t)((local_r13) & (3));
    Arg3 = (Arg3) + (*(uint64_t *)(arg1 + 0x10));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (15));
    local_r11 = (local_r11) + (Arg3);
    local_r10 = (uint32_t)((local_r10) & (1));
    v_stack_p18 = (uint32_t)(local_r13);
    v_stack_m50 = Arg3;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) == 3) { local_r10 = 0; }
    result = MiPreemptivePageDemoteAmount(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    Arg1 = (local_r10 * 4) + (local_r13);
    if ((*(uint64_t *)(local_r11 + arg1 * 8 + 0x18)) >= result) goto loc_0028A6C0;
    if ((*(uint64_t *)(local_r11 + arg1 * 8 + 0x18)) >= result) goto loc_0028A72E;
    Arg4 = 0;
loc_0028A5BD:
    if (((uint32_t)(2 + 1)) >= ((uint32_t)((uint32_t)((uint32_t)(local_r14))))) goto loc_0028A6C0;
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) & (0xFFFFFFDFULL));
    v_stack_p20 = 0;
    local_rbx = (uint32_t)((local_rbx) | (0x37604ULL));
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_0028A6DB;
    local_rbx = (uint32_t)((local_rbx) | (1));
    if ((*(uint32_t *)(v_rip + 0xD3C72E)) != 0) goto loc_0028A6FD;
loc_0028A5F8:
    result = MiCacheAttributeHasValue((uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)(local_r13)), Arg4);
    v_stack_m58 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_0028A8EC;
loc_0028A616:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) == 3) {
    }
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - 1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) << (16));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) & (0x30000ULL));
    local_rdi = (uint32_t)(((uint32_t)(Arg2)) ^ ((uint32_t)(result)));
    Arg1 = (local_rsi + local_rsi * 4) << (8);
    Arg1 = (Arg1) + (v_stack_m50);
    Arg2 = 0;
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) >> (16);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF7ULL));
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(local_rdi)));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint8_t)(Arg2))));
    if ((uint32_t)(local_rsi) != 0) goto loc_0028A6E3;
loc_0028A66A:
    local_rbx = (uint32_t)((local_rbx) | (8));
loc_0028A66D:
    result = MiGetPage(v_stack_p8, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(local_rbx)), Arg4);
    if (result != -1) goto loc_0028A767;
    if (((uint32_t)(local_rsi)) != ((uint32_t)(2 + 1))) goto loc_0028A61F;
    Arg1 = (((uint32_t)(local_r14)) == 3) ? 1 : 0;
    result = (((uint32_t)(local_r14)) >= 3) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0028A70C;
    if (((uint8_t)(v_cr8)) < 2) goto loc_0028A744;
loc_0028A6C0:
    result = 0;
loc_0028A6C2:
    local_rsp = (local_rsp) + (64);
    return result;
loc_0028A6DB:
    goto loc_0028A5F8;
loc_0028A6E3:
    if (((uint32_t)(local_rsi)) != 1) goto loc_0028A66D;
    result = MiCacheAttributeHasValue((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(v_stack_p18), result);
    if ((uint32_t)(result) == 0) goto loc_0028A66A;
    goto loc_0028A66D;
loc_0028A6FD:
    result = KiRaiseIrqlProcessIrqlFlags(17, (uint8_t)(result), (uint32_t)(v_stack_p18), result);
    goto loc_0028A5F8;
loc_0028A70C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) << (16));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rdi)));
    result = (uint32_t)((result) & (0x30000ULL));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(result)));
    goto loc_0028A61F;
loc_0028A72E:
    local_r15 = 0;
    if (condition_is_below) { local_r15 = (uint32_t)(result); }
    goto loc_0028A5BD;
loc_0028A744:
    Arg2 = 0;
    if ((*(uint32_t *)(v_rip + 0xD3C5D4)) != 0) {
        Arg1 = 2;
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(v_stack_p18), 0);
    }
    goto loc_0028A6C0;
loc_0028A767:
loc_0028A770:
    local_rbx = (0 + 0 * 2) << (4);
    local_rbx = (local_rbx) + (17);
    result = MiIsFreeZeroPfnCold(local_rbx, Arg2, (uint32_t)(v_stack_p18), 0);
    local_r15 = 0;
    if ((uint32_t)(result) != 0) goto loc_0028A90B;
loc_0028A798:
    if (1 == 0) goto loc_0028A819;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if ((uint32_t)((uint32_t)((uint32_t)(local_r14))) == 0) goto loc_0028A937;
loc_0028A7B4:
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r13))) { Arg2 = (uint32_t)(local_r13); }
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) == 1) goto loc_0028A945;
loc_0028A7C6:
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r13))) goto loc_0028A965;
loc_0028A7CF:
    result = (v_stack_p30) * (*(uint64_t *)(v_rip - 0x28A7DB + (uint32_t)((uint32_t)(local_r14)) + 0x1 * 8 + 0x11C60));
    Arg2 = 0;
    local_rdi = (Arg2 + Arg2 * 2) << (4);
    local_rdi = (local_rdi) + (local_rbx);
    result = MiInsertDemotedPages(v_stack_p28, local_rbx, local_rdi, (uint32_t)(v_stack_p24));
    result = MiGetPfnPageSizeIndex(local_rdi, local_rbx, local_rdi, (uint32_t)(v_stack_p24));
loc_0028A819:
    Arg3 = (uint32_t)((local_rdi) & (8));
    Arg3 = (Arg3) + (0x3B58ULL);
    Arg3 = (Arg3) + (v_stack_p28);
loc_0028A839:
    Arg1 = (*(uint64_t *)(Arg3)) ^ (*(uint64_t *)(Arg3) - 1);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(Arg3) - 1);
    if ((uint16_t)(Arg1) == 0) {
        Arg2 = Arg1 + 65536;
        Arg2 = (Arg2) ^ (Arg1);
        Arg2 = (Arg2) & (0xFFFFFFFFFFFF0000ULL);
        Arg1 = (Arg1) ^ (Arg2);
    }
    if (condition_is_not_equal) goto loc_0028A839;
    if (17 < 2) goto loc_0028A888;
loc_0028A86B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r13))) goto loc_0028A978;
loc_0028A880:
    goto loc_0028A6C2;
loc_0028A888:
    result = local_rdi;
    if ((*(uint32_t *)(v_rip + 0xD3C491)) != 0) {
        Arg1 = 17;
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, 0xFFFFFFFFFFFF0000ULL);
    }
    goto loc_0028A86B;
loc_0028A8A7:
    v_stack_p90 = 1;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) | (8));
    result = MiGetPage(v_stack_p80, (uint32_t)((uint32_t)(local_rdi)), Arg3, 0xFFFFFFFFFFFF0000ULL);
    if (result == -1) goto loc_0028A8F7;
    goto loc_0028A770;
loc_0028A8EC:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) == 3) goto loc_0028A61B;
    goto loc_0028A8A7;
loc_0028A8F7:
    goto loc_0028A616;
loc_0028A90B:
    if (((*(uint32_t *)(v_rip + 0xD3C1A3)) & (0x200000ULL)) == 0) goto loc_0028A798;
    result = MiChangePageHeatImmediate(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14)))), 1, result);
    Arg2 = 0;
    result = MiSetFreeZeroPfnCold(local_rbx, Arg2, 1, result);
    goto loc_0028A798;
loc_0028A937:
    if (((uint32_t)(local_rbx)) == 1) goto loc_0028A7CF;
    goto loc_0028A7B4;
loc_0028A945:
    if (v_stack_p20 != 0) goto loc_0028A7C6;
    result = MiCacheAttributeHasValue(local_rbx, Arg2, 1, result);
    if ((uint32_t)(result) != 0) goto loc_0028A7CF;
    goto loc_0028A7C6;
loc_0028A965:
    result = MiChangePageAttribute(local_rbx, 1, 16, result);
    goto loc_0028A7CF;
loc_0028A978:
    Arg3 = (uint32_t)(~(16));
    Arg3 = (uint32_t)((Arg3) & (16));
    result = MiChangePageAttribute(local_rdi, (uint32_t)((uint32_t)(local_r13)), Arg3, result);
    goto loc_0028A880;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0028A4F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
