# PfPrefetchRequestVerify

- RVA: `0x009387EC`–`0x00938B8C` (길이 `928` bytes)
- VA: `0x00000001409387EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008FBD4`
- 디코드: `247`개 명령, `928/928` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0093888B` → [PfPrefetchRequestPrepareForVerify](PfPrefetchRequestPrepareForVerify_function_00938C20.md) (function, `0x00938C20`)
- `0x009389E7` → [PfPrefetchRequestVerifyPath](PfPrefetchRequestVerifyPath_function_00938B94.md) (function, `0x00938B94`)
- `0x00938A16` → [PfPrefetchRequestVerifyRanges](PfPrefetchRequestVerifyRanges_function_00939F64.md) (function, `0x00939F64`)
- `0x00938AB8` → [PfPrefetchRequestVerifyRanges](PfPrefetchRequestVerifyRanges_function_00939F64.md) (function, `0x00939F64`)

### Direct callers
- [PfpPrefetchRequest](PfpPrefetchRequest_function_009385CC.md) at `0x00938687`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009387EC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009387F1  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
009387F6  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
009387FB  55                              push rbp
009387FC  41 54                           push r12
009387FE  41 55                           push r13
00938800  41 56                           push r14
00938802  41 57                           push r15
00938804  48 8B EC                        mov rbp, rsp
00938807  48 83 EC 60                     sub rsp, 0x60
0093880B  33 C0                           xor eax, eax
0093880D  0F 57 C0                        xorps xmm0, xmm0
00938810  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00938814  48 8B D9                        mov rbx, rcx
00938817  89 45 F8                        mov dword ptr [rbp - 8], eax
0093881A  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0093881E  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00938822  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00938826  81 FA 80 00 00 00               cmp edx, 0x80
0093882C  0F 82 93 02 00 00               jb 0x140938ac5
00938832  83 39 0D                        cmp dword ptr [rcx], 0xd
00938835  0F 85 AD 02 00 00               jne 0x140938ae8
0093883B  8B 41 04                        mov eax, dword ptr [rcx + 4]
0093883E  3B D0                           cmp edx, eax
00938840  0F 85 A9 02 00 00               jne 0x140938aef
00938846  48 03 C1                        add rax, rcx
00938849  48 3B C1                        cmp rax, rcx
0093884C  0F 82 A4 02 00 00               jb 0x140938af6
00938852  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00938855  0F B7 C8                        movzx ecx, ax
00938858  B8 08 00 00 00                  mov eax, 8
0093885D  3B C8                           cmp ecx, eax
0093885F  0F 83 9B 02 00 00               jae 0x140938b00
00938865  66 39 43 1E                     cmp word ptr [rbx + 0x1e], ax
00938869  0F 83 9B 02 00 00               jae 0x140938b0a
0093886F  8B 43 50                        mov eax, dword ptr [rbx + 0x50]
00938872  A8 C0                           test al, 0xc0
00938874  0F 85 9A 02 00 00               jne 0x140938b14
0093887A  80 7B 51 06                     cmp byte ptr [rbx + 0x51], 6
0093887E  0F 83 9A 02 00 00               jae 0x140938b1e
00938884  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00938888  48 8B CB                        mov rcx, rbx
0093888B  E8 90 03 00 00                  call 0x140938c20
00938890  45 33 C9                        xor r9d, r9d
00938893  85 C0                           test eax, eax
00938895  0F 85 E0 01 00 00               jne 0x140938a7b
0093889B  8B 43 08                        mov eax, dword ptr [rbx + 8]
0093889E  8D 0C 80                        lea ecx, [rax + rax*4]
009388A1  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
009388A4  C1 E1 03                        shl ecx, 3
009388A7  3B 45 C0                        cmp eax, dword ptr [rbp - 0x40]
009388AA  0F 82 2A 02 00 00               jb 0x140938ada
009388B0  3B 45 C4                        cmp eax, dword ptr [rbp - 0x3c]
009388B3  0F 83 6F 02 00 00               jae 0x140938b28
009388B9  03 C1                           add eax, ecx
009388BB  3B 45 C0                        cmp eax, dword ptr [rbp - 0x40]
009388BE  0F 82 16 02 00 00               jb 0x140938ada
009388C4  3B 45 C4                        cmp eax, dword ptr [rbp - 0x3c]
009388C7  0F 87 0D 02 00 00               ja 0x140938ada
009388CD  A8 07                           test al, 7
009388CF  0F 85 05 02 00 00               jne 0x140938ada
009388D5  89 45 C0                        mov dword ptr [rbp - 0x40], eax
009388D8  0F AE E8                        lfence
009388DB  44 8B 73 20                     mov r14d, dword ptr [rbx + 0x20]
009388DF  45 8B E1                        mov r12d, r9d
009388E2  4C 03 F3                        add r14, rbx
009388E5  44 3B 63 08                     cmp r12d, dword ptr [rbx + 8]
009388E9  0F 83 47 01 00 00               jae 0x140938a36
009388EF  41 8B C4                        mov eax, r12d
009388F2  4C 8D 2C 80                     lea r13, [rax + rax*4]
009388F6  43 8B 54 EE 18                  mov edx, dword ptr [r14 + r13*8 + 0x18]
009388FB  43 8B 44 EE 20                  mov eax, dword ptr [r14 + r13*8 + 0x20]
00938900  81 FA FF 7F 00 00               cmp edx, 0x7fff
00938906  0F 83 69 02 00 00               jae 0x140938b75
0093890C  85 D2                           test edx, edx
0093890E  0F 84 57 02 00 00               je 0x140938b6b
00938914  85 C0                           test eax, eax
00938916  0F 84 45 02 00 00               je 0x140938b61
0093891C  8D 0C 55 02 00 00 00            lea ecx, [rdx*2 + 2]
00938923  3B 45 F0                        cmp eax, dword ptr [rbp - 0x10]
00938926  0F 82 A7 01 00 00               jb 0x140938ad3
0093892C  3B 45 F4                        cmp eax, dword ptr [rbp - 0xc]
0093892F  0F 83 FC 01 00 00               jae 0x140938b31
00938935  03 C8                           add ecx, eax
00938937  3B 4D F0                        cmp ecx, dword ptr [rbp - 0x10]
0093893A  0F 82 93 01 00 00               jb 0x140938ad3
00938940  3B 4D F4                        cmp ecx, dword ptr [rbp - 0xc]
00938943  0F 87 8A 01 00 00               ja 0x140938ad3
00938949  F6 C1 01                        test cl, 1
0093894C  0F 85 81 01 00 00               jne 0x140938ad3
00938952  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00938955  48 8D 0C 03                     lea rcx, [rbx + rax]
00938959  66 44 39 0C 51                  cmp word ptr [rcx + rdx*2], r9w
0093895E  0F 85 F3 01 00 00               jne 0x140938b57
00938964  43 8B 44 EE 0C                  mov eax, dword ptr [r14 + r13*8 + 0xc]
00938969  D1 E8                           shr eax, 1
0093896B  0F 84 DC 01 00 00               je 0x140938b4d
00938971  3B 45 D4                        cmp eax, dword ptr [rbp - 0x2c]
00938974  0F 87 C9 01 00 00               ja 0x140938b43
0093897A  43 8B 54 EE 10                  mov edx, dword ptr [r14 + r13*8 + 0x10]
0093897F  8D 0C 40                        lea ecx, [rax + rax*2]
00938982  C1 E1 04                        shl ecx, 4
00938985  8B C2                           mov eax, edx
00938987  3B 55 CC                        cmp edx, dword ptr [rbp - 0x34]
0093898A  0F 82 3C 01 00 00               jb 0x140938acc
00938990  3B 45 D0                        cmp eax, dword ptr [rbp - 0x30]
00938993  0F 83 A1 01 00 00               jae 0x140938b3a
00938999  03 C1                           add eax, ecx
0093899B  3B 45 CC                        cmp eax, dword ptr [rbp - 0x34]
0093899E  0F 82 28 01 00 00               jb 0x140938acc
009389A4  3B 45 D0                        cmp eax, dword ptr [rbp - 0x30]
009389A7  0F 87 1F 01 00 00               ja 0x140938acc
009389AD  A8 07                           test al, 7
009389AF  0F 85 17 01 00 00               jne 0x140938acc
009389B5  89 45 CC                        mov dword ptr [rbp - 0x34], eax
009389B8  4C 8D 3C 13                     lea r15, [rbx + rdx]
009389BC  41 8B F1                        mov esi, r9d
009389BF  43 8B 44 EE 0C                  mov eax, dword ptr [r14 + r13*8 + 0xc]
009389C4  D1 E8                           shr eax, 1
009389C6  3B F0                           cmp esi, eax
009389C8  73 64                           jae 0x140938a2e
009389CA  8B C6                           mov eax, esi
009389CC  48 8D 3C 40                     lea rdi, [rax + rax*2]
009389D0  48 C1 E7 04                     shl rdi, 4
009389D4  49 03 FF                        add rdi, r15
009389D7  4C 8D 47 20                     lea r8, [rdi + 0x20]
009389DB  45 39 08                        cmp dword ptr [r8], r9d
009389DE  74 46                           je 0x140938a26
009389E0  48 8D 55 C0                     lea rdx, [rbp - 0x40]
009389E4  48 8B CB                        mov rcx, rbx
009389E7  E8 A8 01 00 00                  call 0x140938b94
009389EC  85 C0                           test eax, eax
009389EE  0F 85 87 00 00 00               jne 0x140938a7b
009389F4  8B 07                           mov eax, dword ptr [rdi]
009389F6  4C 8D 47 10                     lea r8, [rdi + 0x10]
009389FA  24 01                           and al, 1
009389FC  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00938A00  F6 D8                           neg al
00938A02  48 8B CB                        mov rcx, rbx
00938A05  45 1B C9                        sbb r9d, r9d
00938A08  41 81 E1 00 F2 FF FF            and r9d, 0xfffff200
00938A0F  41 81 C1 00 10 00 00            add r9d, 0x1000
00938A16  E8 49 15 00 00                  call 0x140939f64
00938A1B  45 33 C9                        xor r9d, r9d
00938A1E  85 C0                           test eax, eax
00938A20  75 59                           jne 0x140938a7b
00938A22  FF C6                           inc esi
00938A24  EB 99                           jmp 0x1409389bf
00938A26  44 39 4F 28                     cmp dword ptr [rdi + 0x28], r9d
00938A2A  74 C8                           je 0x1409389f4
00938A2C  EB B2                           jmp 0x1409389e0
00938A2E  41 FF C4                        inc r12d
00938A31  E9 AF FE FF FF                  jmp 0x1409388e5
00938A36  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
00938A39  8B 53 38                        mov edx, dword ptr [rbx + 0x38]
00938A3C  8D 0C 80                        lea ecx, [rax + rax*4]
00938A3F  8B C2                           mov eax, edx
00938A41  C1 E1 03                        shl ecx, 3
00938A44  3B 55 E4                        cmp edx, dword ptr [rbp - 0x1c]
00938A47  0F 82 94 00 00 00               jb 0x140938ae1
00938A4D  3B 45 E8                        cmp eax, dword ptr [rbp - 0x18]
00938A50  0F 83 29 01 00 00               jae 0x140938b7f
00938A56  03 C1                           add eax, ecx
00938A58  3B 45 E4                        cmp eax, dword ptr [rbp - 0x1c]
00938A5B  0F 82 80 00 00 00               jb 0x140938ae1
00938A61  3B 45 E8                        cmp eax, dword ptr [rbp - 0x18]
00938A64  77 7B                           ja 0x140938ae1
00938A66  A8 07                           test al, 7
00938A68  75 77                           jne 0x140938ae1
00938A6A  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
00938A6D  48 8D 34 13                     lea rsi, [rbx + rdx]
00938A71  41 8B F9                        mov edi, r9d
00938A74  3B 7B 14                        cmp edi, dword ptr [rbx + 0x14]
00938A77  72 21                           jb 0x140938a9a
00938A79  33 C0                           xor eax, eax
00938A7B  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00938A80  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00938A84  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00938A88  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00938A8C  49 8B E3                        mov rsp, r11
00938A8F  41 5F                           pop r15
00938A91  41 5E                           pop r14
00938A93  41 5D                           pop r13
00938A95  41 5C                           pop r12
00938A97  5D                              pop rbp
00938A98  C3                              ret
00938A99  CC                              int3
00938A9A  8B C7                           mov eax, edi
00938A9C  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00938AA0  41 B9 00 10 00 00               mov r9d, 0x1000
00938AA6  48 8D 0C 85 03 00 00 00         lea rcx, [rax*4 + 3]
00938AAE  48 03 C8                        add rcx, rax
00938AB1  4C 8D 04 CE                     lea r8, [rsi + rcx*8]
00938AB5  48 8B CB                        mov rcx, rbx
00938AB8  E8 A7 14 00 00                  call 0x140939f64
00938ABD  85 C0                           test eax, eax
00938ABF  75 BA                           jne 0x140938a7b
00938AC1  FF C7                           inc edi
00938AC3  EB AF                           jmp 0x140938a74
00938AC5  B8 E8 03 00 00                  mov eax, 0x3e8
00938ACA  EB AF                           jmp 0x140938a7b
00938ACC  B8 98 3A 00 00                  mov eax, 0x3a98
00938AD1  EB A8                           jmp 0x140938a7b
00938AD3  B8 F8 2A 00 00                  mov eax, 0x2af8
00938AD8  EB A1                           jmp 0x140938a7b
00938ADA  B8 D4 30 00 00                  mov eax, 0x30d4
00938ADF  EB 9A                           jmp 0x140938a7b
00938AE1  B8 40 9C 00 00                  mov eax, 0x9c40
00938AE6  EB 93                           jmp 0x140938a7b
00938AE8  B8 DC 05 00 00                  mov eax, 0x5dc
00938AED  EB 8C                           jmp 0x140938a7b
00938AEF  B8 D0 07 00 00                  mov eax, 0x7d0
00938AF4  EB 85                           jmp 0x140938a7b
00938AF6  B8 C4 09 00 00                  mov eax, 0x9c4
00938AFB  E9 7B FF FF FF                  jmp 0x140938a7b
00938B00  B8 B8 0B 00 00                  mov eax, 0xbb8
00938B05  E9 71 FF FF FF                  jmp 0x140938a7b
00938B0A  B8 80 0C 00 00                  mov eax, 0xc80
00938B0F  E9 67 FF FF FF                  jmp 0x140938a7b
00938B14  B8 48 0D 00 00                  mov eax, 0xd48
00938B19  E9 5D FF FF FF                  jmp 0x140938a7b
00938B1E  B8 10 0E 00 00                  mov eax, 0xe10
00938B23  E9 53 FF FF FF                  jmp 0x140938a7b
00938B28  85 C9                           test ecx, ecx
00938B2A  75 AE                           jne 0x140938ada
00938B2C  E9 88 FD FF FF                  jmp 0x1409388b9
00938B31  85 C9                           test ecx, ecx
00938B33  75 9E                           jne 0x140938ad3
00938B35  E9 FB FD FF FF                  jmp 0x140938935
00938B3A  85 C9                           test ecx, ecx
00938B3C  75 8E                           jne 0x140938acc
00938B3E  E9 56 FE FF FF                  jmp 0x140938999
00938B43  B8 B0 36 00 00                  mov eax, 0x36b0
00938B48  E9 2E FF FF FF                  jmp 0x140938a7b
00938B4D  B8 C8 32 00 00                  mov eax, 0x32c8
00938B52  E9 24 FF FF FF                  jmp 0x140938a7b
00938B57  B8 E0 2E 00 00                  mov eax, 0x2ee0
00938B5C  E9 1A FF FF FF                  jmp 0x140938a7b
00938B61  B8 FE 29 00 00                  mov eax, 0x29fe
00938B66  E9 10 FF FF FF                  jmp 0x140938a7b
00938B6B  B8 04 29 00 00                  mov eax, 0x2904
00938B70  E9 06 FF FF FF                  jmp 0x140938a7b
00938B75  B8 10 27 00 00                  mov eax, 0x2710
00938B7A  E9 FC FE FF FF                  jmp 0x140938a7b
00938B7F  85 C9                           test ecx, ecx
00938B81  0F 85 5A FF FF FF               jne 0x140938ae1
00938B87  E9 CA FE FF FF                  jmp 0x140938a56
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfPrefetchRequestVerify(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m30 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    if (a2 < 128) goto loc_00938AC5;
    if ((*(unsigned int *)(a1)) != 13) goto loc_00938AE8;
    if (a2 != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_00938AEF;
    result = ((unsigned int)(*(unsigned int *)(a1 + 4))) + (a1);
    if (result < a1) goto loc_00938AF6;
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a1 + 28))))) >= 8) goto loc_00938B00;
    if ((*(unsigned __int16 *)(a1 + 30)) >= 8) goto loc_00938B0A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (192)) != 0) goto loc_00938B14;
    if ((*(unsigned __int8 *)(a1 + 81)) >= 6) goto loc_00938B1E;
    result = PfPrefetchRequestPrepareForVerify(a1, a2, v_stack_m68, a4);
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_00938A7B;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8)) + (unsigned int)(*(unsigned int *)(a1 + 8)) * 4) << (3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) < v_stack_m68) goto loc_00938ADA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) >= v_stack_m64) goto loc_00938B28;
loc_009388B9:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) + ((unsigned int)(a1)));
    if (((unsigned int)(result)) < v_stack_m68) goto loc_00938ADA;
    if (((unsigned int)(result)) > v_stack_m64) goto loc_00938ADA;
    if ((((unsigned __int8)(result)) & (7)) != 0) goto loc_00938ADA;
    v_stack_m68 = (unsigned int)(result);
    v_r14 = ((unsigned int)(*(unsigned int *)(a1 + 32))) + (a1);
loc_009388E5:
    if (0 >= (*(unsigned int *)(a1 + 8))) goto loc_00938A36;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 24)))) >= 0x7FFFULL) goto loc_00938B75;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 24))) == 0) goto loc_00938B6B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 32))) == 0) goto loc_00938B61;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 32)))) < v_stack_m38) goto loc_00938AD3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 32)))) >= v_stack_m34) goto loc_00938B31;
loc_00938935:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 24)) * 2 + 2) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 32)))));
    if (((unsigned int)(a1)) < v_stack_m38) goto loc_00938AD3;
    if (((unsigned int)(a1)) > v_stack_m34) goto loc_00938AD3;
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_00938AD3;
    v_stack_m38 = (unsigned int)(a1);
    if ((*(unsigned __int16 *)(a1 + (unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 32)) * 1 + (unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 24)) * 2)) != 0) goto loc_00938B57;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 12))) >> (1));
    if (condition_is_equal) goto loc_00938B4D;
    if (((unsigned int)(result)) > v_stack_m54) goto loc_00938B43;
    a1 = (unsigned int)((result + result * 2) << (4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 16)))) < v_stack_m5C) goto loc_00938ACC;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 16)))))) >= v_stack_m58) goto loc_00938B3A;
loc_00938999:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 16))))) + ((unsigned int)(a1)));
    if (((unsigned int)(result)) < v_stack_m5C) goto loc_00938ACC;
    if (((unsigned int)(result)) > v_stack_m58) goto loc_00938ACC;
    if ((((unsigned __int8)(result)) & (7)) != 0) goto loc_00938ACC;
    v_stack_m5C = (unsigned int)(result);
loc_009389BF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 12))) >> (1));
    if (0 >= ((unsigned int)(result))) goto loc_00938A2E;
    v_rdi = (0 + 0 * 2) << (4);
    v_rdi = (v_rdi) + (a1 + (unsigned int)(*(unsigned int *)(v_r14 + 0 + 0 * 4 * 8 + 16)) * 1);
    if ((*(unsigned int *)(v_rdi + 32)) == 0) goto loc_00938A26;
loc_009389E0:
    result = PfPrefetchRequestVerifyPath(a1, v_stack_m68, v_rdi + 32, a4);
    if ((unsigned int)(result) != 0) goto loc_00938A7B;
loc_009389F4:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rdi))) & (1));
    result = (unsigned __int8)(-(result));
    a4 = (unsigned int)((a4) & (0xFFFFF200ULL));
    a4 = (unsigned int)((a4) + (0x1000ULL));
    result = PfPrefetchRequestVerifyRanges(a1, v_stack_m68, v_rdi + 16, a4);
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_00938A7B;
    v_rsi = (unsigned int)((0) + 1);
    goto loc_009389BF;
loc_00938A26:
    if ((*(unsigned int *)(v_rdi + 40)) == 0) goto loc_009389F4;
    goto loc_009389E0;
loc_00938A2E:
    v_r12 = (unsigned int)((0) + 1);
    goto loc_009388E5;
loc_00938A36:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 20)) + (unsigned int)(*(unsigned int *)(a1 + 20)) * 4) << (3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) < v_stack_m44) goto loc_00938AE1;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))))) >= v_stack_m40) goto loc_00938B7F;
loc_00938A56:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56))))) + ((unsigned int)(a1)));
    if (((unsigned int)(result)) < v_stack_m44) goto loc_00938AE1;
    if (((unsigned int)(result)) > v_stack_m40) goto loc_00938AE1;
    if ((((unsigned __int8)(result)) & (7)) != 0) goto loc_00938AE1;
    v_stack_m44 = (unsigned int)(result);
loc_00938A74:
    if (0 < (*(unsigned int *)(a1 + 20))) goto loc_00938A9A;
    result = 0;
loc_00938A7B:
    return result;
loc_00938A9A:
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))) * 4 + 3) + ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))));
    result = PfPrefetchRequestVerifyRanges(*(unsigned __int64 *)(v_stack_m28 + 48), v_stack_m68, *(unsigned __int64 *)(v_stack_m28 + 56) + a1 * 8, (unsigned int)(0x1000ULL));
    if ((unsigned int)(result) != 0) goto loc_00938A7B;
    v_rdi = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 64)) + 1);
    goto loc_00938A74;
loc_00938AC5:
    goto loc_00938A7B;
loc_00938ACC:
    goto loc_00938A7B;
loc_00938AD3:
    goto loc_00938A7B;
loc_00938ADA:
    goto loc_00938A7B;
loc_00938AE1:
    goto loc_00938A7B;
loc_00938AE8:
    goto loc_00938A7B;
loc_00938AEF:
    goto loc_00938A7B;
loc_00938AF6:
    goto loc_00938A7B;
loc_00938B00:
    goto loc_00938A7B;
loc_00938B0A:
    goto loc_00938A7B;
loc_00938B14:
    goto loc_00938A7B;
loc_00938B1E:
    goto loc_00938A7B;
loc_00938B28:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)) != 0) goto loc_00938ADA;
    goto loc_009388B9;
loc_00938B31:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)) != 0) goto loc_00938AD3;
    goto loc_00938935;
loc_00938B3A:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)) != 0) goto loc_00938ACC;
    goto loc_00938999;
loc_00938B43:
    goto loc_00938A7B;
loc_00938B4D:
    goto loc_00938A7B;
loc_00938B57:
    goto loc_00938A7B;
loc_00938B61:
    goto loc_00938A7B;
loc_00938B6B:
    goto loc_00938A7B;
loc_00938B75:
    goto loc_00938A7B;
loc_00938B7F:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)) != 0) goto loc_00938AE1;
    goto loc_00938A56;
}
```

## 5. (Beta) C Style

```c
int64_t PfPrefetchRequestVerify(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m30 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    if (Arg2 < 128) goto loc_00938AC5;
    if ((*(uint32_t *)(arg1)) != 13) goto loc_00938AE8;
    if (Arg2 != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) goto loc_00938AEF;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x4))) + (Arg1);
    if (result < Arg1) goto loc_00938AF6;
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C))))) >= 8) goto loc_00938B00;
    if ((*(uint16_t *)(arg1 + 0x1E)) >= 8) goto loc_00938B0A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (192)) != 0) goto loc_00938B14;
    if ((*(uint8_t *)(arg1 + 0x51)) >= 6) goto loc_00938B1E;
    result = PfPrefetchRequestPrepareForVerify(Arg1, Arg2, v_stack_m68, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_00938A7B;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8)) + (uint32_t)(*(uint32_t *)(arg1 + 0x8)) * 4) << (3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) < v_stack_m68) goto loc_00938ADA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) >= v_stack_m64) goto loc_00938B28;
loc_009388B9:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) + ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) < v_stack_m68) goto loc_00938ADA;
    if (((uint32_t)(result)) > v_stack_m64) goto loc_00938ADA;
    if ((((uint8_t)(result)) & (7)) != 0) goto loc_00938ADA;
    v_stack_m68 = (uint32_t)(result);
    local_r14 = ((uint32_t)(*(uint32_t *)(arg1 + 0x20))) + (Arg1);
loc_009388E5:
    if (0 >= (*(uint32_t *)(arg1 + 0x8))) goto loc_00938A36;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x18)))) >= 0x7FFFULL) goto loc_00938B75;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x18))) == 0) goto loc_00938B6B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x20))) == 0) goto loc_00938B61;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x20)))) < v_stack_m38) goto loc_00938AD3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x20)))) >= v_stack_m34) goto loc_00938B31;
loc_00938935:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x18)) * 2 + 2) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x20)))));
    if (((uint32_t)(Arg1)) < v_stack_m38) goto loc_00938AD3;
    if (((uint32_t)(Arg1)) > v_stack_m34) goto loc_00938AD3;
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_00938AD3;
    v_stack_m38 = (uint32_t)(Arg1);
    if ((*(uint16_t *)(arg1 + (uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x20)) * 1 + (uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x18)) * 2)) != 0) goto loc_00938B57;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0xC))) >> (1));
    if (condition_is_equal) goto loc_00938B4D;
    if (((uint32_t)(result)) > v_stack_m54) goto loc_00938B43;
    Arg1 = (uint32_t)((result + result * 2) << (4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x10)))) < v_stack_m5C) goto loc_00938ACC;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x10)))))) >= v_stack_m58) goto loc_00938B3A;
loc_00938999:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x10))))) + ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) < v_stack_m5C) goto loc_00938ACC;
    if (((uint32_t)(result)) > v_stack_m58) goto loc_00938ACC;
    if ((((uint8_t)(result)) & (7)) != 0) goto loc_00938ACC;
    v_stack_m5C = (uint32_t)(result);
loc_009389BF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0xC))) >> (1));
    if (0 >= ((uint32_t)(result))) goto loc_00938A2E;
    local_rdi = (0 + 0 * 2) << (4);
    local_rdi = (local_rdi) + (Arg1 + (uint32_t)(*(uint32_t *)(local_r14 + 0x0 + 0x0 * 4 * 8 + 0x10)) * 1);
    if ((*(uint32_t *)(local_rdi + 0x20)) == 0) goto loc_00938A26;
loc_009389E0:
    result = PfPrefetchRequestVerifyPath(Arg1, v_stack_m68, local_rdi + 32, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00938A7B;
loc_009389F4:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rdi))) & (1));
    result = (uint8_t)(-(result));
    Arg4 = (uint32_t)((Arg4) & (0xFFFFF200ULL));
    Arg4 = (uint32_t)((Arg4) + (0x1000ULL));
    result = PfPrefetchRequestVerifyRanges(Arg1, v_stack_m68, local_rdi + 16, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_00938A7B;
    local_rsi = (uint32_t)((0) + 1);
    goto loc_009389BF;
loc_00938A26:
    if ((*(uint32_t *)(local_rdi + 0x28)) == 0) goto loc_009389F4;
    goto loc_009389E0;
loc_00938A2E:
    local_r12 = (uint32_t)((0) + 1);
    goto loc_009388E5;
loc_00938A36:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x14)) + (uint32_t)(*(uint32_t *)(arg1 + 0x14)) * 4) << (3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) < v_stack_m44) goto loc_00938AE1;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))))) >= v_stack_m40) goto loc_00938B7F;
loc_00938A56:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38))))) + ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) < v_stack_m44) goto loc_00938AE1;
    if (((uint32_t)(result)) > v_stack_m40) goto loc_00938AE1;
    if ((((uint8_t)(result)) & (7)) != 0) goto loc_00938AE1;
    v_stack_m44 = (uint32_t)(result);
loc_00938A74:
    if (0 < (*(uint32_t *)(arg1 + 0x14))) goto loc_00938A9A;
    result = 0;
loc_00938A7B:
    return result;
loc_00938A9A:
    Arg1 = ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))) * 4 + 3) + ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))));
    result = PfPrefetchRequestVerifyRanges(*(uint64_t *)(v_stack_m28 + 0x30), v_stack_m68, *(uint64_t *)(v_stack_m28 + 0x38) + Arg1 * 8, (uint32_t)(0x1000ULL));
    if ((uint32_t)(result) != 0) goto loc_00938A7B;
    local_rdi = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x40)) + 1);
    goto loc_00938A74;
loc_00938AC5:
    goto loc_00938A7B;
loc_00938ACC:
    goto loc_00938A7B;
loc_00938AD3:
    goto loc_00938A7B;
loc_00938ADA:
    goto loc_00938A7B;
loc_00938AE1:
    goto loc_00938A7B;
loc_00938AE8:
    goto loc_00938A7B;
loc_00938AEF:
    goto loc_00938A7B;
loc_00938AF6:
    goto loc_00938A7B;
loc_00938B00:
    goto loc_00938A7B;
loc_00938B0A:
    goto loc_00938A7B;
loc_00938B14:
    goto loc_00938A7B;
loc_00938B1E:
    goto loc_00938A7B;
loc_00938B28:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)) != 0) goto loc_00938ADA;
    goto loc_009388B9;
loc_00938B31:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)) != 0) goto loc_00938AD3;
    goto loc_00938935;
loc_00938B3A:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)) != 0) goto loc_00938ACC;
    goto loc_00938999;
loc_00938B43:
    goto loc_00938A7B;
loc_00938B4D:
    goto loc_00938A7B;
loc_00938B57:
    goto loc_00938A7B;
loc_00938B61:
    goto loc_00938A7B;
loc_00938B6B:
    goto loc_00938A7B;
loc_00938B75:
    goto loc_00938A7B;
loc_00938B7F:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)) != 0) goto loc_00938AE1;
    goto loc_00938A56;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg1` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdx*1` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdx*2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x1E` | `16` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x51` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009387EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
