# IopLiveDumpPopulateBitmapForDump

- RVA: `0x0059D9B0`–`0x0059DD58` (길이 `936` bytes)
- VA: `0x000000014059D9B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E968`
- 디코드: `264`개 명령, `936/936` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0059D9E4` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)
- `0x0059DA0E` → [IopLiveDumpRemoveSystemCacheFromDump](IopLiveDumpRemoveSystemCacheFromDump_function_0059E1B0.md) (function, `0x0059E1B0`)
- `0x0059DB99` → [RtlSetBitsEx](../3B/RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)
- `0x0059DCB2` → [RtlSetBitsEx](../3B/RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)
- `0x0059DD26` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)
- `0x0059DD41` → [IopLiveDumpTracePopulateBitmapForDumpDuration](IopLiveDumpTracePopulateBitmapForDumpDuration_function_0059F158.md) (function, `0x0059F158`)

### Direct callers
- [IopLiveDumpCollectPages](IopLiveDumpCollectPages_function_0059B328.md) at `0x0059B5A1`
- [IopLiveDumpCollectPages](IopLiveDumpCollectPages_function_0059B328.md) at `0x0059B604`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059D9B0  48 8B C4                        mov rax, rsp
0059D9B3  53                              push rbx
0059D9B4  55                              push rbp
0059D9B5  56                              push rsi
0059D9B6  57                              push rdi
0059D9B7  41 54                           push r12
0059D9B9  41 55                           push r13
0059D9BB  41 56                           push r14
0059D9BD  41 57                           push r15
0059D9BF  48 83 EC 48                     sub rsp, 0x48
0059D9C3  48 83 60 20 00                  and qword ptr [rax + 0x20], 0
0059D9C8  0F 57 C0                        xorps xmm0, xmm0
0059D9CB  48 83 A4 24 A0 00 00 00 00      and qword ptr [rsp + 0xa0], 0
0059D9D4  48 8B F9                        mov rdi, rcx
0059D9D7  0F 11 40 A0                     movups xmmword ptr [rax - 0x60], xmm0
0059D9DB  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0059D9DE  84 C0                           test al, al
0059D9E0  79 0F                           jns 0x14059d9f1
0059D9E2  33 C9                           xor ecx, ecx
0059D9E4  E8 7B 7F E5 FF                  call 0x1403f5964
0059D9E9  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0059D9F1  4C 8D B7 20 02 00 00            lea r14, [rdi + 0x220]
0059D9F8  48 8B CF                        mov rcx, rdi
0059D9FB  49 8B 06                        mov rax, qword ptr [r14]
0059D9FE  4C 8D 84 24 A8 00 00 00         lea r8, [rsp + 0xa8]
0059DA06  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0059DA0E  E8 9D 07 00 00                  call 0x14059e1b0
0059DA13  4C 8D A7 58 02 00 00            lea r12, [rdi + 0x258]
0059DA1A  4D 85 E4                        test r12, r12
0059DA1D  0F 84 FA 02 00 00               je 0x14059dd1d
0059DA23  49 8B 14 24                     mov rdx, qword ptr [r12]
0059DA27  83 A4 24 90 00 00 00 00         and dword ptr [rsp + 0x90], 0
0059DA2F  48 FF CA                        dec rdx
0059DA32  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0059DA37  48 8D 42 01                     lea rax, [rdx + 1]
0059DA3B  48 83 F8 01                     cmp rax, 1
0059DA3F  0F 82 B1 02 00 00               jb 0x14059dcf6
0059DA45  48 8B C2                        mov rax, rdx
0059DA48  48 8B D9                        mov rbx, rcx
0059DA4B  48 C1 E8 06                     shr rax, 6
0059DA4F  4C 8D 04 C1                     lea r8, [rcx + rax*8]
0059DA53  48 8B 01                        mov rax, qword ptr [rcx]
0059DA56  48 F7 D0                        not rax
0059DA59  48 83 F8 FF                     cmp rax, -1
0059DA5D  75 12                           jne 0x14059da71
0059DA5F  48 83 C3 08                     add rbx, 8
0059DA63  49 3B D8                        cmp rbx, r8
0059DA66  0F 87 8A 02 00 00               ja 0x14059dcf6
0059DA6C  48 8B 03                        mov rax, qword ptr [rbx]
0059DA6F  EB E5                           jmp 0x14059da56
0059DA71  48 2B D9                        sub rbx, rcx
0059DA74  48 F7 D0                        not rax
0059DA77  48 C1 FB 03                     sar rbx, 3
0059DA7B  48 0F BC C0                     bsf rax, rax
0059DA7F  48 C1 E3 06                     shl rbx, 6
0059DA83  48 03 D8                        add rbx, rax
0059DA86  48 3B DA                        cmp rbx, rdx
0059DA89  0F 87 67 02 00 00               ja 0x14059dcf6
0059DA8F  48 83 FB FF                     cmp rbx, -1
0059DA93  0F 84 5D 02 00 00               je 0x14059dcf6
0059DA99  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0059DAA1  83 A4 24 90 00 00 00 00         and dword ptr [rsp + 0x90], 0
0059DAA9  45 33 FF                        xor r15d, r15d
0059DAAC  4D 8B 0C 24                     mov r9, qword ptr [r12]
0059DAB0  4C 3B CB                        cmp r9, rbx
0059DAB3  0F 86 CA 00 00 00               jbe 0x14059db83
0059DAB9  4D 8B 5C 24 08                  mov r11, qword ptr [r12 + 8]
0059DABE  49 8D 41 FF                     lea rax, [r9 - 1]
0059DAC2  48 C1 E8 06                     shr rax, 6
0059DAC6  8A CB                           mov cl, bl
0059DAC8  80 E1 3F                        and cl, 0x3f
0059DACB  4D 8D 14 C3                     lea r10, [r11 + rax*8]
0059DACF  48 8B C3                        mov rax, rbx
0059DAD2  48 C1 E8 06                     shr rax, 6
0059DAD6  49 8D 14 C3                     lea rdx, [r11 + rax*8]
0059DADA  4C 8B 02                        mov r8, qword ptr [rdx]
0059DADD  41 8D 47 01                     lea eax, [r15 + 1]
0059DAE1  48 D3 E0                        shl rax, cl
0059DAE4  48 FF C8                        dec rax
0059DAE7  4C 0B C0                        or r8, rax
0059DAEA  48 8D 42 08                     lea rax, [rdx + 8]
0059DAEE  49 F7 D0                        not r8
0059DAF1  4D 85 C0                        test r8, r8
0059DAF4  75 12                           jne 0x14059db08
0059DAF6  49 3B C2                        cmp rax, r10
0059DAF9  77 29                           ja 0x14059db24
0059DAFB  48 83 C2 08                     add rdx, 8
0059DAFF  48 83 C0 08                     add rax, 8
0059DB03  4C 8B 02                        mov r8, qword ptr [rdx]
0059DB06  EB E6                           jmp 0x14059daee
0059DB08  49 0F BC C8                     bsf rcx, r8
0059DB0C  48 8B F2                        mov rsi, rdx
0059DB0F  49 2B F3                        sub rsi, r11
0059DB12  8B C1                           mov eax, ecx
0059DB14  48 C1 FE 03                     sar rsi, 3
0059DB18  48 C1 E6 06                     shl rsi, 6
0059DB1C  48 03 F0                        add rsi, rax
0059DB1F  49 3B F1                        cmp rsi, r9
0059DB22  76 05                           jbe 0x14059db29
0059DB24  49 8B F1                        mov rsi, r9
0059DB27  EB 4D                           jmp 0x14059db76
0059DB29  B8 01 00 00 00                  mov eax, 1
0059DB2E  48 D3 E0                        shl rax, cl
0059DB31  48 FF C8                        dec rax
0059DB34  49 0B C0                        or rax, r8
0059DB37  48 F7 D0                        not rax
0059DB3A  48 85 C0                        test rax, rax
0059DB3D  75 18                           jne 0x14059db57
0059DB3F  48 8D 42 08                     lea rax, [rdx + 8]
0059DB43  49 3B C2                        cmp rax, r10
0059DB46  77 08                           ja 0x14059db50
0059DB48  48 8B D0                        mov rdx, rax
0059DB4B  48 8B 00                        mov rax, qword ptr [rax]
0059DB4E  EB EA                           jmp 0x14059db3a
0059DB50  B8 40 00 00 00                  mov eax, 0x40
0059DB55  EB 04                           jmp 0x14059db5b
0059DB57  48 0F BC C0                     bsf rax, rax
0059DB5B  4C 8B FA                        mov r15, rdx
0059DB5E  4D 2B FB                        sub r15, r11
0059DB61  49 C1 FF 03                     sar r15, 3
0059DB65  49 C1 E7 06                     shl r15, 6
0059DB69  4C 03 F8                        add r15, rax
0059DB6C  4D 3B F9                        cmp r15, r9
0059DB6F  4D 0F 47 F9                     cmova r15, r9
0059DB73  4C 2B FE                        sub r15, rsi
0059DB76  4D 85 FF                        test r15, r15
0059DB79  75 0B                           jne 0x14059db86
0059DB7B  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0059DB83  48 8B F0                        mov rsi, rax
0059DB86  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0059DB89  48 2B F3                        sub rsi, rbx
0059DB8C  A8 01                           test al, 1
0059DB8E  74 13                           je 0x14059dba3
0059DB90  4C 8B C6                        mov r8, rsi
0059DB93  48 8B D3                        mov rdx, rbx
0059DB96  49 8B CE                        mov rcx, r14
0059DB99  E8 D2 89 E1 FF                  call 0x1403b6570
0059DB9E  E9 3B 01 00 00                  jmp 0x14059dcde
0059DBA3  4C 8B 97 28 02 00 00            mov r10, qword ptr [rdi + 0x228]
0059DBAA  4C 8D 2C 33                     lea r13, [rbx + rsi]
0059DBAE  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0059DBB3  48 8B CB                        mov rcx, rbx
0059DBB6  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0059DBBB  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0059DBC0  83 A4 24 90 00 00 00 00         and dword ptr [rsp + 0x90], 0
0059DBC8  4C 3B E9                        cmp r13, rcx
0059DBCB  0F 86 06 01 00 00               jbe 0x14059dcd7
0059DBD1  33 ED                           xor ebp, ebp
0059DBD3  49 8D 45 FF                     lea rax, [r13 - 1]
0059DBD7  48 C1 E8 06                     shr rax, 6
0059DBDB  44 8D 5D 01                     lea r11d, [rbp + 1]
0059DBDF  4D 8D 0C C2                     lea r9, [r10 + rax*8]
0059DBE3  48 8B C1                        mov rax, rcx
0059DBE6  48 C1 E8 06                     shr rax, 6
0059DBEA  80 E1 3F                        and cl, 0x3f
0059DBED  49 8D 14 C2                     lea rdx, [r10 + rax*8]
0059DBF1  41 8B C3                        mov eax, r11d
0059DBF4  4C 8B 02                        mov r8, qword ptr [rdx]
0059DBF7  48 D3 E0                        shl rax, cl
0059DBFA  49 2B C3                        sub rax, r11
0059DBFD  4C 0B C0                        or r8, rax
0059DC00  48 8D 42 08                     lea rax, [rdx + 8]
0059DC04  49 F7 D0                        not r8
0059DC07  4D 85 C0                        test r8, r8
0059DC0A  75 12                           jne 0x14059dc1e
0059DC0C  49 3B C1                        cmp rax, r9
0059DC0F  77 29                           ja 0x14059dc3a
0059DC11  48 83 C2 08                     add rdx, 8
0059DC15  48 83 C0 08                     add rax, 8
0059DC19  4C 8B 02                        mov r8, qword ptr [rdx]
0059DC1C  EB E6                           jmp 0x14059dc04
0059DC1E  49 0F BC C8                     bsf rcx, r8
0059DC22  4C 8B F2                        mov r14, rdx
0059DC25  4D 2B F2                        sub r14, r10
0059DC28  8B C1                           mov eax, ecx
0059DC2A  49 C1 FE 03                     sar r14, 3
0059DC2E  49 C1 E6 06                     shl r14, 6
0059DC32  4C 03 F0                        add r14, rax
0059DC35  4D 3B F5                        cmp r14, r13
0059DC38  76 05                           jbe 0x14059dc3f
0059DC3A  4D 8B F5                        mov r14, r13
0059DC3D  EB 4B                           jmp 0x14059dc8a
0059DC3F  49 8B C3                        mov rax, r11
0059DC42  48 D3 E0                        shl rax, cl
0059DC45  49 2B C3                        sub rax, r11
0059DC48  49 0B C0                        or rax, r8
0059DC4B  48 F7 D0                        not rax
0059DC4E  48 85 C0                        test rax, rax
0059DC51  75 18                           jne 0x14059dc6b
0059DC53  48 8D 42 08                     lea rax, [rdx + 8]
0059DC57  49 3B C1                        cmp rax, r9
0059DC5A  77 08                           ja 0x14059dc64
0059DC5C  48 8B D0                        mov rdx, rax
0059DC5F  48 8B 00                        mov rax, qword ptr [rax]
0059DC62  EB EA                           jmp 0x14059dc4e
0059DC64  B8 40 00 00 00                  mov eax, 0x40
0059DC69  EB 04                           jmp 0x14059dc6f
0059DC6B  48 0F BC C0                     bsf rax, rax
0059DC6F  48 8B EA                        mov rbp, rdx
0059DC72  49 2B EA                        sub rbp, r10
0059DC75  48 C1 FD 03                     sar rbp, 3
0059DC79  48 C1 E5 06                     shl rbp, 6
0059DC7D  48 03 E8                        add rbp, rax
0059DC80  49 3B ED                        cmp rbp, r13
0059DC83  49 0F 47 ED                     cmova rbp, r13
0059DC87  49 2B EE                        sub rbp, r14
0059DC8A  48 85 ED                        test rbp, rbp
0059DC8D  74 48                           je 0x14059dcd7
0059DC8F  48 8B 87 B0 02 00 00            mov rax, qword ptr [rdi + 0x2b0]
0059DC96  48 3B E8                        cmp rbp, rax
0059DC99  76 07                           jbe 0x14059dca2
0059DC9B  83 4F 50 02                     or dword ptr [rdi + 0x50], 2
0059DC9F  48 8B E8                        mov rbp, rax
0059DCA2  48 85 ED                        test rbp, rbp
0059DCA5  74 1C                           je 0x14059dcc3
0059DCA7  4C 8B C5                        mov r8, rbp
0059DCAA  48 8D 4C 24 28                  lea rcx, [rsp + 0x28]
0059DCAF  49 8B D6                        mov rdx, r14
0059DCB2  E8 B9 88 E1 FF                  call 0x1403b6570
0059DCB7  48 29 AF B0 02 00 00            sub qword ptr [rdi + 0x2b0], rbp
0059DCBE  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
0059DCC3  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0059DCC6  A8 02                           test al, 2
0059DCC8  75 7C                           jne 0x14059dd46
0059DCCA  49 8D 0C 2E                     lea rcx, [r14 + rbp]
0059DCCE  49 3B CD                        cmp rcx, r13
0059DCD1  0F 82 E9 FE FF FF               jb 0x14059dbc0
0059DCD7  4C 8D B7 20 02 00 00            lea r14, [rdi + 0x220]
0059DCDE  49 8D 04 37                     lea rax, [r15 + rsi]
0059DCE2  48 03 D8                        add rbx, rax
0059DCE5  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0059DCED  48 3B D8                        cmp rbx, rax
0059DCF0  0F 82 AB FD FF FF               jb 0x14059daa1
0059DCF6  48 8D 87 58 02 00 00            lea rax, [rdi + 0x258]
0059DCFD  4C 3B E0                        cmp r12, rax
0059DD00  75 13                           jne 0x14059dd15
0059DD02  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0059DD05  A8 04                           test al, 4
0059DD07  74 0C                           je 0x14059dd15
0059DD09  4C 8D A7 90 02 00 00            lea r12, [rdi + 0x290]
0059DD10  E9 05 FD FF FF                  jmp 0x14059da1a
0059DD15  45 33 E4                        xor r12d, r12d
0059DD18  E9 FD FC FF FF                  jmp 0x14059da1a
0059DD1D  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0059DD20  84 C0                           test al, al
0059DD22  79 22                           jns 0x14059dd46
0059DD24  33 C9                           xor ecx, ecx
0059DD26  E8 39 7C E5 FF                  call 0x1403f5964
0059DD2B  48 2B 84 24 A0 00 00 00         sub rax, qword ptr [rsp + 0xa0]
0059DD33  48 8B CF                        mov rcx, rdi
0059DD36  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
0059DD3E  48 8B D0                        mov rdx, rax
0059DD41  E8 12 14 00 00                  call 0x14059f158
0059DD46  48 83 C4 48                     add rsp, 0x48
0059DD4A  41 5F                           pop r15
0059DD4C  41 5E                           pop r14
0059DD4E  41 5D                           pop r13
0059DD50  41 5C                           pop r12
0059DD52  5F                              pop rdi
0059DD53  5E                              pop rsi
0059DD54  5D                              pop rbp
0059DD55  5B                              pop rbx
0059DD56  C3                              ret
0059DD57  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpPopulateBitmapForDump(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (72);
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    result = (unsigned int)(*(unsigned int *)(a1 + 80));
    if (sign_flag) {
        a1 = 0;
        result = IopLiveDumpGetMillisecondCounter(a1, a2, a3, a4);
        v_stack_p18 = result;
    }
    v_stack_p10 = *(unsigned __int64 *)(a1 + 544);
    result = IopLiveDumpRemoveSystemCacheFromDump(0, a2, v_stack_p20, a4);
loc_0059DA1A:
    if (a1 + 600 == 0) goto loc_0059DD1D;
    a2 = (*(unsigned __int64 *)(a1 + 600)) - 1;
    if ((a2 + 1) < 1) goto loc_0059DCF6;
    result = (a2) >> (6);
loc_0059DA56:
    result = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 600 + 8)));
    if (result != -1) goto loc_0059DA71;
    v_rbx = (*(unsigned __int64 *)(a1 + 600 + 8)) + (8);
    if (v_rbx > (*(unsigned __int64 *)(a1 + 600 + 8) + result * 8)) goto loc_0059DCF6;
    goto loc_0059DA56;
loc_0059DA71:
    v_rbx = (v_rbx) - (*(unsigned __int64 *)(a1 + 600 + 8));
    result = ~(*(unsigned __int64 *)(v_rbx));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (result);
    if (v_rbx > a2) goto loc_0059DCF6;
    if (v_rbx == -1) goto loc_0059DCF6;
loc_0059DAA1:
    v_r15 = 0;
    if ((*(unsigned __int64 *)(a1 + 600)) <= v_rbx) goto loc_0059DB83;
    result = (*(unsigned __int64 *)(a1 + 600) - 1) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (63));
    result = (v_rbx) >> (6);
    result = (v_r15 + 1) << ((unsigned __int8)(a1));
    result = (result) - 1;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 600 + 8) + result * 8)) | (result);
loc_0059DAEE:
    a3 = ~(a3);
    if (a3 != 0) goto loc_0059DB08;
    if ((*(unsigned __int64 *)(a1 + 600 + 8) + result * 8 + 8) > (*(unsigned __int64 *)(a1 + 600 + 8) + result * 8)) goto loc_0059DB24;
    a2 = (*(unsigned __int64 *)(a1 + 600 + 8) + result * 8) + (8);
    result = (*(unsigned __int64 *)(a1 + 600 + 8) + result * 8 + 8) + (8);
    goto loc_0059DAEE;
loc_0059DB08:
    v_rsi = (a2) - (*(unsigned __int64 *)(a1 + 600 + 8));
    v_rsi = (v_rsi) >> (3);
    v_rsi = (v_rsi) << (6);
    v_rsi = (v_rsi) + ((unsigned int)((unsigned int)(a1)));
    if (v_rsi <= (*(unsigned __int64 *)(a1 + 600))) goto loc_0059DB29;
loc_0059DB24:
    goto loc_0059DB76;
loc_0059DB29:
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - 1;
    result = (result) | (*(unsigned __int64 *)(a2));
    result = ~(result);
loc_0059DB3A:
    if (result != 0) goto loc_0059DB57;
    if ((a2 + 8) > (*(unsigned __int64 *)(a1 + 600 + 8) + result * 8)) goto loc_0059DB50;
    goto loc_0059DB3A;
loc_0059DB50:
    goto loc_0059DB5B;
loc_0059DB57:
loc_0059DB5B:
    v_r15 = (a2 + 8) - (*(unsigned __int64 *)(a1 + 600 + 8));
    v_r15 = (v_r15) >> (3);
    v_r15 = (v_r15) << (6);
    v_r15 = (v_r15) + (64);
    if (v_r15 > (*(unsigned __int64 *)(a1 + 600))) { v_r15 = *(unsigned __int64 *)(a1 + 600); }
    v_r15 = (v_r15) - (*(unsigned __int64 *)(a1 + 600));
loc_0059DB76:
    if (v_r15 != 0) goto loc_0059DB86;
loc_0059DB83:
loc_0059DB86:
    v_rsi = (v_stack_p10) - (v_rbx);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (1)) == 0) goto loc_0059DBA3;
    result = RtlSetBitsEx(a1 + 544, v_rbx, v_rsi, *(unsigned __int64 *)(a1 + 600));
    goto loc_0059DCDE;
loc_0059DBA3:
    v_stack_m60 = v_rbx + v_rsi * 1;
    v_stack_m68 = *(unsigned __int64 *)(a1 + 552);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 552);
loc_0059DBC0:
    if ((v_rbx + v_rsi * 1) <= v_rbx) goto loc_0059DCD7;
    v_rbp = 0;
    result = (v_rbx + v_rsi * 1 - 1) >> (6);
    result = (v_rbx) >> (6);
    a1 = (unsigned __int8)((v_rbx) & (63));
    result = ((unsigned int)((unsigned int)(v_rbp + 1))) << ((unsigned __int8)(a1));
    result = (result) - (v_rbp + 1);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 552) + result * 8)) | (result);
loc_0059DC04:
    a3 = ~(a3);
    if (a3 != 0) goto loc_0059DC1E;
    if ((*(unsigned __int64 *)(a1 + 552) + result * 8 + 8) > (*(unsigned __int64 *)(a1 + 552) + result * 8)) goto loc_0059DC3A;
    a2 = (*(unsigned __int64 *)(a1 + 552) + result * 8) + (8);
    result = (*(unsigned __int64 *)(a1 + 552) + result * 8 + 8) + (8);
    goto loc_0059DC04;
loc_0059DC1E:
    v_r14 = (a2) - (*(unsigned __int64 *)(a1 + 552));
    v_r14 = (v_r14) >> (3);
    v_r14 = (v_r14) << (6);
    v_r14 = (v_r14) + ((unsigned int)((unsigned int)(a1)));
    if (v_r14 <= (v_rbx + v_rsi * 1)) goto loc_0059DC3F;
loc_0059DC3A:
    goto loc_0059DC8A;
loc_0059DC3F:
    result = (v_rbp + 1) << ((unsigned __int8)(a1));
    result = (result) - (v_rbp + 1);
    result = (result) | (*(unsigned __int64 *)(a2));
    result = ~(result);
loc_0059DC4E:
    if (result != 0) goto loc_0059DC6B;
    if ((a2 + 8) > (*(unsigned __int64 *)(a1 + 552) + result * 8)) goto loc_0059DC64;
    goto loc_0059DC4E;
loc_0059DC64:
    goto loc_0059DC6F;
loc_0059DC6B:
loc_0059DC6F:
    v_rbp = (a2 + 8) - (*(unsigned __int64 *)(a1 + 552));
    v_rbp = (v_rbp) >> (3);
    v_rbp = (v_rbp) << (6);
    v_rbp = (v_rbp) + (64);
    if (v_rbp > (v_rbx + v_rsi * 1)) { v_rbp = v_rbx + v_rsi * 1; }
    v_rbp = (v_rbp) - (v_rbx + v_rsi * 1);
loc_0059DC8A:
    if (v_rbp == 0) goto loc_0059DCD7;
    if (v_rbp >= = (*(unsigned __int64 *)(a1 + 688))) {
        v_rbp = *(unsigned __int64 *)(a1 + 688);
    }
    result = *(unsigned __int64 *)(a1 + 688);
    v_r10 = *(unsigned __int64 *)(a1 + 552);
    if (v_rbp != 0) {
        a3 = v_rbp;
        a1 = v_stack_m60;
        a2 = v_rbx + v_rsi * 1;
        result = RtlSetBitsEx(a1, a2, a3, *(unsigned __int64 *)(a1 + 552) + result * 8);
        v_r10 = v_stack_m68;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (2)) != 0) goto loc_0059DD46;
    if ((v_rbx + v_rsi * 1 + v_rbp * 1) < (v_rbx + v_rsi * 1)) goto loc_0059DBC0;
loc_0059DCD7:
loc_0059DCDE:
    v_rbx = (v_rbx) + (v_r15 + v_rsi * 1);
    if (v_rbx < v_stack_p10) goto loc_0059DAA1;
loc_0059DCF6:
    if ((a1 + 600) != (a1 + 600)) goto loc_0059DD15;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (4)) == 0) goto loc_0059DD15;
    goto loc_0059DA1A;
loc_0059DD15:
    v_r12 = 0;
    goto loc_0059DA1A;
loc_0059DD1D:
    result = (unsigned int)(*(unsigned int *)(a1 + 80));
    if (sign_flag) {
        a1 = 0;
        result = IopLiveDumpGetMillisecondCounter(a1, a2, a3, *(unsigned __int64 *)(a1 + 552) + result * 8);
        result = (result) - (v_stack_p18);
        a1 = 0;
        a3 = v_stack_p20;
        a2 = result;
        result = IopLiveDumpTracePopulateBitmapForDumpDuration(a1, a2, a3, *(unsigned __int64 *)(a1 + 552) + result * 8);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpPopulateBitmapForDump(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (72);
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x50));
    if (sign_flag) {
        Arg1 = 0;
        result = IopLiveDumpGetMillisecondCounter(Arg1, a2, a3, a4);
        v_stack_p18 = result;
    }
    v_stack_p10 = *(uint64_t *)(arg1 + 0x220);
    result = IopLiveDumpRemoveSystemCacheFromDump(0, a2, v_stack_p20, a4);
loc_0059DA1A:
    if (Arg1 + 600 == 0) goto loc_0059DD1D;
    a2 = (*(uint64_t *)(arg1 + 0x258)) - 1;
    if ((a2 + 1) < 1) goto loc_0059DCF6;
    result = (a2) >> (6);
loc_0059DA56:
    result = ~(*(uint64_t *)(*(uint64_t *)(arg1 + 0x258 + 0x8)));
    if (result != -1) goto loc_0059DA71;
    local_rbx = (*(uint64_t *)(arg1 + 0x258 + 0x8)) + (8);
    if (local_rbx > (*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8)) goto loc_0059DCF6;
    goto loc_0059DA56;
loc_0059DA71:
    local_rbx = (local_rbx) - (*(uint64_t *)(arg1 + 0x258 + 0x8));
    result = ~(*(uint64_t *)(local_rbx));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (result);
    if (local_rbx > a2) goto loc_0059DCF6;
    if (local_rbx == -1) goto loc_0059DCF6;
loc_0059DAA1:
    local_r15 = 0;
    if ((*(uint64_t *)(arg1 + 0x258)) <= local_rbx) goto loc_0059DB83;
    result = (*(uint64_t *)(arg1 + 0x258) - 1) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(local_rbx)) & (63));
    result = (local_rbx) >> (6);
    result = (local_r15 + 1) << ((uint8_t)(Arg1));
    result = (result) - 1;
    a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8)) | (result);
loc_0059DAEE:
    a3 = ~(a3);
    if (a3 != 0) goto loc_0059DB08;
    if ((*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8 + 8) > (*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8)) goto loc_0059DB24;
    a2 = (*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8) + (8);
    result = (*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8 + 8) + (8);
    goto loc_0059DAEE;
loc_0059DB08:
    local_rsi = (a2) - (*(uint64_t *)(arg1 + 0x258 + 0x8));
    local_rsi = (local_rsi) >> (3);
    local_rsi = (local_rsi) << (6);
    local_rsi = (local_rsi) + ((uint32_t)((uint32_t)(Arg1)));
    if (local_rsi <= (*(uint64_t *)(arg1 + 0x258))) goto loc_0059DB29;
loc_0059DB24:
    goto loc_0059DB76;
loc_0059DB29:
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - 1;
    result = (result) | (*(uint64_t *)(a2));
    result = ~(result);
loc_0059DB3A:
    if (result != 0) goto loc_0059DB57;
    if ((a2 + 8) > (*(uint64_t *)(arg1 + 0x258 + 0x8) + result * 8)) goto loc_0059DB50;
    goto loc_0059DB3A;
loc_0059DB50:
    goto loc_0059DB5B;
loc_0059DB57:
loc_0059DB5B:
    local_r15 = (a2 + 8) - (*(uint64_t *)(arg1 + 0x258 + 0x8));
    local_r15 = (local_r15) >> (3);
    local_r15 = (local_r15) << (6);
    local_r15 = (local_r15) + (64);
    if (local_r15 > (*(uint64_t *)(arg1 + 0x258))) { local_r15 = *(uint64_t *)(arg1 + 0x258); }
    local_r15 = (local_r15) - (*(uint64_t *)(arg1 + 0x258));
loc_0059DB76:
    if (local_r15 != 0) goto loc_0059DB86;
loc_0059DB83:
loc_0059DB86:
    local_rsi = (v_stack_p10) - (local_rbx);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (1)) == 0) goto loc_0059DBA3;
    result = RtlSetBitsEx(Arg1 + 544, local_rbx, local_rsi, *(uint64_t *)(arg1 + 0x258));
    goto loc_0059DCDE;
loc_0059DBA3:
    v_stack_m60 = local_rbx + local_rsi * 1;
    v_stack_m68 = *(uint64_t *)(arg1 + 0x228);
    v_stack_m58 = *(uint64_t *)(arg1 + 0x228);
loc_0059DBC0:
    if ((local_rbx + local_rsi * 1) <= local_rbx) goto loc_0059DCD7;
    local_rbp = 0;
    result = (local_rbx + local_rsi * 1 - 1) >> (6);
    result = (local_rbx) >> (6);
    Arg1 = (uint8_t)((local_rbx) & (63));
    result = ((uint32_t)((uint32_t)(local_rbp + 1))) << ((uint8_t)(Arg1));
    result = (result) - (local_rbp + 1);
    a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x228) + result * 8)) | (result);
loc_0059DC04:
    a3 = ~(a3);
    if (a3 != 0) goto loc_0059DC1E;
    if ((*(uint64_t *)(arg1 + 0x228) + result * 8 + 8) > (*(uint64_t *)(arg1 + 0x228) + result * 8)) goto loc_0059DC3A;
    a2 = (*(uint64_t *)(arg1 + 0x228) + result * 8) + (8);
    result = (*(uint64_t *)(arg1 + 0x228) + result * 8 + 8) + (8);
    goto loc_0059DC04;
loc_0059DC1E:
    local_r14 = (a2) - (*(uint64_t *)(arg1 + 0x228));
    local_r14 = (local_r14) >> (3);
    local_r14 = (local_r14) << (6);
    local_r14 = (local_r14) + ((uint32_t)((uint32_t)(Arg1)));
    if (local_r14 <= (local_rbx + local_rsi * 1)) goto loc_0059DC3F;
loc_0059DC3A:
    goto loc_0059DC8A;
loc_0059DC3F:
    result = (local_rbp + 1) << ((uint8_t)(Arg1));
    result = (result) - (local_rbp + 1);
    result = (result) | (*(uint64_t *)(a2));
    result = ~(result);
loc_0059DC4E:
    if (result != 0) goto loc_0059DC6B;
    if ((a2 + 8) > (*(uint64_t *)(arg1 + 0x228) + result * 8)) goto loc_0059DC64;
    goto loc_0059DC4E;
loc_0059DC64:
    goto loc_0059DC6F;
loc_0059DC6B:
loc_0059DC6F:
    local_rbp = (a2 + 8) - (*(uint64_t *)(arg1 + 0x228));
    local_rbp = (local_rbp) >> (3);
    local_rbp = (local_rbp) << (6);
    local_rbp = (local_rbp) + (64);
    if (local_rbp > (local_rbx + local_rsi * 1)) { local_rbp = local_rbx + local_rsi * 1; }
    local_rbp = (local_rbp) - (local_rbx + local_rsi * 1);
loc_0059DC8A:
    if (local_rbp == 0) goto loc_0059DCD7;
    if (local_rbp >= = (*(uint64_t *)(arg1 + 0x2B0))) {
        local_rbp = *(uint64_t *)(arg1 + 0x2B0);
    }
    result = *(uint64_t *)(arg1 + 0x2B0);
    local_r10 = *(uint64_t *)(arg1 + 0x228);
    if (local_rbp != 0) {
        a3 = local_rbp;
        Arg1 = v_stack_m60;
        a2 = local_rbx + local_rsi * 1;
        result = RtlSetBitsEx(Arg1, a2, a3, *(uint64_t *)(arg1 + 0x228) + result * 8);
        local_r10 = v_stack_m68;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (2)) != 0) goto loc_0059DD46;
    if ((local_rbx + local_rsi * 1 + local_rbp * 1) < (local_rbx + local_rsi * 1)) goto loc_0059DBC0;
loc_0059DCD7:
loc_0059DCDE:
    local_rbx = (local_rbx) + (local_r15 + local_rsi * 1);
    if (local_rbx < v_stack_p10) goto loc_0059DAA1;
loc_0059DCF6:
    if ((Arg1 + 600) != (Arg1 + 600)) goto loc_0059DD15;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (4)) == 0) goto loc_0059DD15;
    goto loc_0059DA1A;
loc_0059DD15:
    local_r12 = 0;
    goto loc_0059DA1A;
loc_0059DD1D:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x50));
    if (sign_flag) {
        Arg1 = 0;
        result = IopLiveDumpGetMillisecondCounter(Arg1, a2, a3, *(uint64_t *)(arg1 + 0x228) + result * 8);
        result = (result) - (v_stack_p18);
        Arg1 = 0;
        a3 = v_stack_p20;
        a2 = result;
        result = IopLiveDumpTracePopulateBitmapForDumpDuration(Arg1, a2, a3, *(uint64_t *)(arg1 + 0x228) + result * 8);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R/W` |
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x228` | `64` | `R` |
| `Arg1` | `+ 0x258` | `64` | `R` |
| `Arg1` | `+ 0x290` | `64` | `R` |
| `Arg1` | `+ 0x2B0` | `64` | `R` |
| `Arg1` | `+ 0x2B0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059D9B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
