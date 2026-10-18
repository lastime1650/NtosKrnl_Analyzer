# MiCompressRelocations

- RVA: `0x00966600`–`0x009669BB` (길이 `955` bytes)
- VA: `0x0000000140966600`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093890`
- 디코드: `267`개 명령, `955/955` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0096674B` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0096680D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiRelocateImage](../98/MiRelocateImage_function_00988E14.md) at `0x00989620`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0096674B` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0096680D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00966600  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00966605  53                              push rbx
00966606  55                              push rbp
00966607  56                              push rsi
00966608  57                              push rdi
00966609  41 54                           push r12
0096660B  41 55                           push r13
0096660D  41 56                           push r14
0096660F  41 57                           push r15
00966611  48 83 EC 28                     sub rsp, 0x28
00966615  48 8B 69 20                     mov rbp, qword ptr [rcx + 0x20]
00966619  45 33 E4                        xor r12d, r12d
0096661C  45 32 FF                        xor r15b, r15b
0096661F  44 8B F2                        mov r14d, edx
00966622  32 DB                           xor bl, bl
00966624  41 8B F4                        mov esi, r12d
00966627  88 5C 24 78                     mov byte ptr [rsp + 0x78], bl
0096662B  41 BD FF 0F 00 00               mov r13d, 0xfff
00966631  8B 4D 04                        mov ecx, dword ptr [rbp + 4]
00966634  4C 8D 55 08                     lea r10, [rbp + 8]
00966638  BA 04 00 00 00                  mov edx, 4
0096663D  44 2B F1                        sub r14d, ecx
00966640  48 03 E9                        add rbp, rcx
00966643  45 0F B7 CC                     movzx r9d, r12w
00966647  44 0F B7 DA                     movzx r11d, dx
0096664B  41 8B FC                        mov edi, r12d
0096664E  44 8D 41 F8                     lea r8d, [rcx - 8]
00966652  41 D1 E8                        shr r8d, 1
00966655  45 85 C0                        test r8d, r8d
00966658  0F 84 AB 00 00 00               je 0x140966709
0096665E  41 0F B7 02                     movzx eax, word ptr [r10]
00966662  0F B7 D0                        movzx edx, ax
00966665  66 C1 EA 0C                     shr dx, 0xc
00966669  66 85 D2                        test dx, dx
0096666C  0F 84 2E 03 00 00               je 0x1409669a0
00966672  3A DA                           cmp bl, dl
00966674  0F 85 07 03 00 00               jne 0x140966981
0096667A  41 0F B7 CC                     movzx ecx, r12w
0096667E  66 41 23 C5                     and ax, r13w
00966682  66 03 C1                        add ax, cx
00966685  66 41 3B C1                     cmp ax, r9w
00966689  0F 86 C1 02 00 00               jbe 0x140966950
0096668F  0F B7 D0                        movzx edx, ax
00966692  66 41 2B C1                     sub ax, r9w
00966696  66 41 3B C3                     cmp ax, r11w
0096669A  75 2E                           jne 0x1409666ca
0096669C  81 FF FE 00 00 00               cmp edi, 0xfe
009666A2  48 8D 46 02                     lea rax, [rsi + 2]
009666A6  8D 4F 01                        lea ecx, [rdi + 1]
009666A9  48 0F 45 C6                     cmovne rax, rsi
009666AD  48 8B F0                        mov rsi, rax
009666B0  8B C7                           mov eax, edi
009666B2  3D FE 00 00 00                  cmp eax, 0xfe
009666B7  41 8B FC                        mov edi, r12d
009666BA  0F 45 F9                        cmovne edi, ecx
009666BD  49 83 C2 02                     add r10, 2
009666C1  44 0F B7 CA                     movzx r9d, dx
009666C5  41 FF C8                        dec r8d
009666C8  EB 8B                           jmp 0x140966655
009666CA  85 FF                           test edi, edi
009666CC  75 21                           jne 0x1409666ef
009666CE  B9 EB 00 00 00                  mov ecx, 0xeb
009666D3  44 0F B7 D8                     movzx r11d, ax
009666D7  66 3B C1                        cmp ax, cx
009666DA  73 27                           jae 0x140966703
009666DC  48 FF C6                        inc rsi
009666DF  49 83 C2 02                     add r10, 2
009666E3  41 FF C8                        dec r8d
009666E6  44 0F B7 CA                     movzx r9d, dx
009666EA  E9 66 FF FF FF                  jmp 0x140966655
009666EF  83 FF 04                        cmp edi, 4
009666F2  49 8B CC                        mov rcx, r12
009666F5  41 8B FC                        mov edi, r12d
009666F8  0F 97 C1                        seta cl
009666FB  48 FF C1                        inc rcx
009666FE  48 03 F1                        add rsi, rcx
00966701  EB CB                           jmp 0x1409666ce
00966703  48 83 C6 02                     add rsi, 2
00966707  EB B4                           jmp 0x1409666bd
00966709  85 FF                           test edi, edi
0096670B  0F 85 1B 02 00 00               jne 0x14096692c
00966711  48 8B C6                        mov rax, rsi
00966714  48 83 C6 02                     add rsi, 2
00966718  83 E0 01                        and eax, 1
0096671B  48 03 F0                        add rsi, rax
0096671E  45 85 F6                        test r14d, r14d
00966721  0F 85 0A FF FF FF               jne 0x140966631
00966727  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0096672C  45 84 FF                        test r15b, r15b
0096672F  0F 84 2A 02 00 00               je 0x14096695f
00966735  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
00966738  B9 00 01 00 00                  mov ecx, 0x100
0096673D  48 83 C0 0D                     add rax, 0xd
00966741  41 B8 4D 6D 52 65               mov r8d, 0x65526d4d
00966747  48 8D 14 C6                     lea rdx, [rsi + rax*8]
0096674B  E8 F0 4D 9F FF                  call 0x14035b540
00966750  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00966758  4C 8B E0                        mov r12, rax
0096675B  48 85 C0                        test rax, rax
0096675E  0F 84 FB 01 00 00               je 0x14096695f
00966764  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00966767  4C 8B 77 20                     mov r14, qword ptr [rdi + 0x20]
0096676B  48 8D 70 68                     lea rsi, [rax + 0x68]
0096676F  4C 2B 37                        sub r14, qword ptr [rdi]
00966772  4C 8D 7F 68                     lea r15, [rdi + 0x68]
00966776  0F 11 00                        movups xmmword ptr [rax], xmm0
00966779  49 C1 EE 03                     shr r14, 3
0096677D  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00966781  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
00966789  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
0096678D  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
00966791  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00966795  0F 10 4F 30                     movups xmm1, xmmword ptr [rdi + 0x30]
00966799  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
0096679D  0F 10 47 40                     movups xmm0, xmmword ptr [rdi + 0x40]
009667A1  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
009667A5  0F 10 4F 50                     movups xmm1, xmmword ptr [rdi + 0x50]
009667A9  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
009667AD  F2 0F 10 47 60                  movsd xmm0, qword ptr [rdi + 0x60]
009667B2  F2 0F 11 40 60                  movsd qword ptr [rax + 0x60], xmm0
009667B7  88 58 40                        mov byte ptr [rax + 0x40], bl
009667BA  33 DB                           xor ebx, ebx
009667BC  48 89 30                        mov qword ptr [rax], rsi
009667BF  8B EB                           mov ebp, ebx
009667C1  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
009667C4  48 8D 14 C6                     lea rdx, [rsi + rax*8]
009667C8  49 89 54 24 20                  mov qword ptr [r12 + 0x20], rdx
009667CD  4C 8B 6F 20                     mov r13, qword ptr [rdi + 0x20]
009667D1  45 85 F6                        test r14d, r14d
009667D4  74 32                           je 0x140966808
009667D6  41 B9 00 10 00 00               mov r9d, 0x1000
009667DC  4C 2B FE                        sub r15, rsi
009667DF  45 8D 61 FF                     lea r12d, [r9 - 1]
009667E3  3B 6F 38                        cmp ebp, dword ptr [rdi + 0x38]
009667E6  73 0D                           jae 0x1409667f5
009667E8  49 8B 04 37                     mov rax, qword ptr [r15 + rsi]
009667EC  48 83 F8 01                     cmp rax, 1
009667F0  77 35                           ja 0x140966827
009667F2  48 89 06                        mov qword ptr [rsi], rax
009667F5  FF C5                           inc ebp
009667F7  48 83 C6 08                     add rsi, 8
009667FB  41 3B EE                        cmp ebp, r14d
009667FE  72 E3                           jb 0x1409667e3
00966800  4C 8B A4 24 88 00 00 00         mov r12, qword ptr [rsp + 0x88]
00966808  33 D2                           xor edx, edx
0096680A  48 8B CF                        mov rcx, rdi
0096680D  E8 5E C0 21 00                  call 0x140b82870
00966812  49 8B C4                        mov rax, r12
00966815  48 83 C4 28                     add rsp, 0x28
00966819  41 5F                           pop r15
0096681B  41 5E                           pop r14
0096681D  41 5D                           pop r13
0096681F  41 5C                           pop r12
00966821  5F                              pop rdi
00966822  5E                              pop rsi
00966823  5D                              pop rbp
00966824  5B                              pop rbx
00966825  C3                              ret
00966826  CC                              int3
00966827  48 89 16                        mov qword ptr [rsi], rdx
0096682A  41 F6 04 37 01                  test byte ptr [r15 + rsi], 1
0096682F  0F 85 77 01 00 00               jne 0x1409669ac
00966835  41 8B 4D 04                     mov ecx, dword ptr [r13 + 4]
00966839  4D 8D 55 08                     lea r10, [r13 + 8]
0096683D  4C 03 E9                        add r13, rcx
00966840  0F B7 C3                        movzx eax, bx
00966843  BF 04 00 00 00                  mov edi, 4
00966848  44 8B C3                        mov r8d, ebx
0096684B  44 8D 59 F8                     lea r11d, [rcx - 8]
0096684F  41 D1 EB                        shr r11d, 1
00966852  74 5B                           je 0x1409668af
00966854  41 BE EB 00 00 00               mov r14d, 0xeb
0096685A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00966860  41 0F B7 0A                     movzx ecx, word ptr [r10]
00966864  66 41 3B C9                     cmp cx, r9w
00966868  72 33                           jb 0x14096689d
0096686A  66 41 23 CC                     and cx, r12w
0096686E  44 0F B7 C9                     movzx r9d, cx
00966872  66 44 2B C8                     sub r9w, ax
00966876  66 44 3B CF                     cmp r9w, di
0096687A  75 5B                           jne 0x1409668d7
0096687C  41 FF C0                        inc r8d
0096687F  41 81 F8 FF 00 00 00            cmp r8d, 0xff
00966886  75 0C                           jne 0x140966894
00966888  66 C7 02 EF FF                  mov word ptr [rdx], 0xffef
0096688D  44 8B C3                        mov r8d, ebx
00966890  48 83 C2 02                     add rdx, 2
00966894  0F B7 C1                        movzx eax, cx
00966897  41 B9 00 10 00 00               mov r9d, 0x1000
0096689D  49 83 C2 02                     add r10, 2
009668A1  41 83 C3 FF                     add r11d, -1
009668A5  75 B9                           jne 0x140966860
009668A7  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
009668AF  45 85 C0                        test r8d, r8d
009668B2  0F 85 82 00 00 00               jne 0x14096693a
009668B8  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
009668BD  66 C7 02 F0 00                  mov word ptr [rdx], 0xf0
009668C2  48 83 C2 02                     add rdx, 2
009668C6  F6 C2 01                        test dl, 1
009668C9  0F 84 26 FF FF FF               je 0x1409667f5
009668CF  48 FF C2                        inc rdx
009668D2  E9 1E FF FF FF                  jmp 0x1409667f5
009668D7  45 85 C0                        test r8d, r8d
009668DA  75 14                           jne 0x1409668f0
009668DC  41 0F B7 F9                     movzx edi, r9w
009668E0  66 45 3B CE                     cmp r9w, r14w
009668E4  73 2F                           jae 0x140966915
009668E6  44 88 0A                        mov byte ptr [rdx], r9b
009668E9  48 FF C2                        inc rdx
009668EC  33 DB                           xor ebx, ebx
009668EE  EB A4                           jmp 0x140966894
009668F0  41 83 F8 04                     cmp r8d, 4
009668F4  77 12                           ja 0x140966908
009668F6  B8 EF 00 00 00                  mov eax, 0xef
009668FB  41 2A C0                        sub al, r8b
009668FE  88 02                           mov byte ptr [rdx], al
00966900  48 FF C2                        inc rdx
00966903  45 33 C0                        xor r8d, r8d
00966906  EB D4                           jmp 0x1409668dc
00966908  C6 02 EF                        mov byte ptr [rdx], 0xef
0096690B  44 88 42 01                     mov byte ptr [rdx + 1], r8b
0096690F  48 83 C2 02                     add rdx, 2
00966913  EB EE                           jmp 0x140966903
00966915  41 0F B6 C1                     movzx eax, r9b
00966919  66 41 C1 E9 04                  shr r9w, 4
0096691E  0C F0                           or al, 0xf0
00966920  88 02                           mov byte ptr [rdx], al
00966922  44 88 4A 01                     mov byte ptr [rdx + 1], r9b
00966926  48 83 C2 02                     add rdx, 2
0096692A  EB C0                           jmp 0x1409668ec
0096692C  83 FF 04                        cmp edi, 4
0096692F  76 48                           jbe 0x140966979
00966931  48 83 C6 02                     add rsi, 2
00966935  E9 D7 FD FF FF                  jmp 0x140966711
0096693A  41 83 F8 04                     cmp r8d, 4
0096693E  76 27                           jbe 0x140966967
00966940  C6 02 EF                        mov byte ptr [rdx], 0xef
00966943  44 88 42 01                     mov byte ptr [rdx + 1], r8b
00966947  48 83 C2 02                     add rdx, 2
0096694B  E9 68 FF FF FF                  jmp 0x1409668b8
00966950  66 45 85 C9                     test r9w, r9w
00966954  0F 84 35 FD FF FF               je 0x14096668f
0096695A  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0096695F  48 8B C7                        mov rax, rdi
00966962  E9 AE FE FF FF                  jmp 0x140966815
00966967  B8 EF 00 00 00                  mov eax, 0xef
0096696C  41 2A C0                        sub al, r8b
0096696F  88 02                           mov byte ptr [rdx], al
00966971  48 FF C2                        inc rdx
00966974  E9 3F FF FF FF                  jmp 0x1409668b8
00966979  48 FF C6                        inc rsi
0096697C  E9 90 FD FF FF                  jmp 0x140966711
00966981  41 80 FF 01                     cmp r15b, 1
00966985  73 D3                           jae 0x14096695a
00966987  41 0F B6 CF                     movzx ecx, r15b
0096698B  88 54 0C 78                     mov byte ptr [rsp + rcx + 0x78], dl
0096698F  0F B6 5C 24 78                  movzx ebx, byte ptr [rsp + 0x78]
00966994  41 0F B6 CF                     movzx ecx, r15b
00966998  41 FE C7                        inc r15b
0096699B  E9 DE FC FF FF                  jmp 0x14096667e
009669A0  49 83 C2 02                     add r10, 2
009669A4  41 FF C8                        dec r8d
009669A7  E9 A9 FC FF FF                  jmp 0x140966655
009669AC  48 8B C2                        mov rax, rdx
009669AF  48 83 C8 01                     or rax, 1
009669B3  48 89 06                        mov qword ptr [rsi], rax
009669B6  E9 7A FE FF FF                  jmp 0x140966835
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCompressRelocations(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int8 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (40);
    v_r12 = 0;
    v_r15 = 0;
    v_rbx = 0;
    v_stack_p10 = 0;
loc_00966631:
    v_r14 = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4)))));
    v_rbp = (*(unsigned __int64 *)(a1 + 32)) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4)));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4)) - 8) >> (1));
loc_00966655:
    if ((unsigned int)(a3) == 0) goto loc_00966709;
    a2 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 8))) >> (12));
    if ((unsigned __int16)(a2) == 0) goto loc_009669A0;
    if (0 != ((unsigned __int8)(a2))) goto loc_00966981;
loc_0096667E:
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 8)) & ((unsigned __int16)((unsigned int)(0xFFFULL))));
    result = (unsigned __int16)((result) + (0));
    if (((unsigned __int16)(result)) <= 0) goto loc_00966950;
loc_0096668F:
    result = (unsigned __int16)((result) - (0));
    if (((unsigned __int16)(result)) != 4) goto loc_009666CA;
    result = 0 + 2;
    if (0 != 254) { result = 0; }
    v_rdi = 0;
    if (0 != 254) { v_rdi = (unsigned int)(0 + 1); }
loc_009666BD:
    v_r10 = (*(unsigned __int64 *)(a1 + 32) + 8) + (2);
    a3 = (unsigned int)((a3) - 1);
    goto loc_00966655;
loc_009666CA:
    if ((unsigned int)(v_rdi) != 0) goto loc_009666EF;
loc_009666CE:
    if (0 >= 235) goto loc_00966703;
    v_rsi = (result) + 1;
    v_r10 = (v_r10) + (2);
    a3 = (unsigned int)((a3) - 1);
    goto loc_00966655;
loc_009666EF:
    a1 = (((unsigned int)(v_rdi)) > 4) ? 1 : 0;
    a1 = (a1) + 1;
    v_rsi = (v_rsi) + (a1);
    goto loc_009666CE;
loc_00966703:
    v_rsi = (v_rsi) + (2);
    goto loc_009666BD;
loc_00966709:
    if (0 != 0) goto loc_0096692C;
loc_00966711:
    v_rsi = (v_rsi) + (2);
    result = (unsigned int)((v_rsi) & (1));
    v_rsi = (v_rsi) + (result);
    if ((unsigned int)(v_r14) != 0) goto loc_00966631;
    if (0 == 0) goto loc_0096695F;
    result = ((unsigned int)(*(unsigned int *)(v_stack_p8 + 56))) + (13);
    result = MiAllocatePool(256, v_rsi + result * 8, (unsigned int)(0x65526D4DULL), (unsigned __int16)((unsigned __int16)(result)));
    v_stack_p20 = result;
    if (result == 0) goto loc_0096695F;
    v_r14 = (*(unsigned __int64 *)(v_stack_p8 + 32)) - (*(unsigned __int64 *)(v_stack_p8));
    *(unsigned __int64 *)(result) = v_xmm0;
    v_r14 = (v_r14) >> (3);
    v_stack_p18 = v_r14;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 96) = v_xmm0;
    *(unsigned __int8 *)(result + 64) = 0;
    v_rbx = 0;
    *(unsigned __int64 *)(result) = result + 104;
    *(unsigned __int64 *)(result + 32) = result + 104 + (unsigned int)(*(unsigned int *)(v_stack_p8 + 56)) * 8;
    if ((unsigned int)(v_r14) == 0) goto loc_00966808;
    v_r15 = (v_stack_p8 + 104) - (result + 104);
loc_009667E3:
    if (0 >= (*(unsigned int *)(v_stack_p8 + 56))) goto loc_009667F5;
    if ((*(unsigned __int64 *)(v_r15 + result + 104 * 1)) > 1) goto loc_00966827;
    *(unsigned __int64 *)(result + 104) = *(unsigned __int64 *)(v_r15 + result + 104 * 1);
loc_009667F5:
    v_rbp = (unsigned int)((0) + 1);
    v_rsi = (result + 104) + (8);
    if (((unsigned int)(v_rbp)) < ((unsigned int)(v_r14))) goto loc_009667E3;
loc_00966808:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p8, a2, (unsigned int)(0x65526D4DULL), (unsigned int)(0x1000ULL));
loc_00966815:
    v_rsp = (v_rsp) + (40);
    return v_stack_p20;
loc_00966827:
    *(unsigned __int64 *)(v_rsi) = 0;
    if (((*(unsigned __int8 *)(v_r15 + v_rsi * 1)) & (1)) != 0) goto loc_009669AC;
loc_00966835:
    v_r13 = (*(unsigned __int64 *)(v_stack_p8 + 32)) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 32) + 4)));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 32) + 4)) - 8) >> (1));
    if (condition_is_equal) goto loc_009668AF;
loc_00966860:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32) + 8))) < ((unsigned __int16)((unsigned int)(0x1000ULL)))) goto loc_0096689D;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32) + 8)) & ((unsigned __int16)(v_stack_p20)));
    a4 = (unsigned __int16)(((unsigned __int16)(a1)) - (0));
    if (((unsigned __int16)(a4)) != 4) goto loc_009668D7;
    a3 = (unsigned int)((0) + 1);
    if (((unsigned int)(a3)) == 255) {
        *(unsigned __int16 *)(a2) = 0xFFEFULL;
        a3 = 0;
        a2 = (a2) + (2);
    }
loc_0096689D:
    v_r10 = (*(unsigned __int64 *)(v_stack_p8 + 32) + 8) + (2);
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00966860;
loc_009668AF:
    if ((unsigned int)(a3) != 0) goto loc_0096693A;
loc_009668B8:
    *(unsigned __int16 *)(a2) = 240;
    a2 = (a2) + (2);
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_009667F5;
    a2 = (a2) + 1;
    goto loc_009667F5;
loc_009668D7:
    if ((unsigned int)(a3) != 0) goto loc_009668F0;
loc_009668DC:
    if (((unsigned __int16)((unsigned int)(0x1000ULL))) >= ((unsigned __int16)(v_stack_p80))) goto loc_00966915;
    *(unsigned __int8 *)(a2) = (unsigned __int8)((unsigned int)(0x1000ULL));
    a2 = (a2) + 1;
loc_009668EC:
    v_rbx = 0;
    goto loc_00966894;
loc_009668F0:
    if (((unsigned int)(a3)) > 4) goto loc_00966908;
    result = (unsigned __int8)((239) - ((unsigned __int8)(a3)));
    *(unsigned __int8 *)(a2) = (unsigned __int8)(result);
    a2 = (a2) + 1;
loc_00966903:
    a3 = 0;
    goto loc_009668DC;
loc_00966908:
    *(unsigned __int8 *)(a2) = 239;
    *(unsigned __int8 *)(a2 + 1) = 0;
    a2 = (a2) + (2);
    goto loc_00966903;
loc_00966915:
    a4 = (unsigned __int16)(((unsigned int)(0x1000ULL)) >> (4));
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(0x1000ULL))) | (240));
    *(unsigned __int8 *)(a2) = (unsigned __int8)(result);
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(a4);
    a2 = (a2) + (2);
    goto loc_009668EC;
loc_0096692C:
    if (((unsigned int)((unsigned __int16)((unsigned int)(0x1000ULL)))) <= 4) goto loc_00966979;
    v_rsi = (v_rsi) + (2);
    goto loc_00966711;
loc_0096693A:
    if (0 <= 4) goto loc_00966967;
    *(unsigned __int8 *)(a2) = 239;
    *(unsigned __int8 *)(a2 + 1) = 0;
    a2 = (a2) + (2);
    goto loc_009668B8;
loc_00966950:
    if ((unsigned __int16)(a4) == 0) goto loc_0096668F;
loc_0096695A:
loc_0096695F:
    goto loc_00966815;
loc_00966967:
    result = (unsigned __int8)((239) - (0));
    *(unsigned __int8 *)(a2) = (unsigned __int8)(result);
    a2 = (a2) + 1;
    goto loc_009668B8;
loc_00966979:
    v_rsi = (v_rsi) + 1;
    goto loc_00966711;
loc_00966981:
    if (((unsigned __int8)(v_r15)) >= 1) goto loc_0096695A;
    *(unsigned __int8 *)(v_rsp + (unsigned __int8)(v_r15) * 1 + 120) = (unsigned __int8)(a2);
    v_r15 = (unsigned __int8)((v_r15) + 1);
    goto loc_0096667E;
loc_009669A0:
    v_r10 = (v_r10) + (2);
    a3 = (unsigned int)((a3) - 1);
    goto loc_00966655;
loc_009669AC:
    result = (a2) | (1);
    *(unsigned __int64 *)(v_rsi) = result;
    goto loc_00966835;
}
```

## 5. (Beta) C Style

```c
int64_t MiCompressRelocations(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint8_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (40);
    local_r12 = 0;
    local_r15 = 0;
    local_rbx = 0;
    v_stack_p10 = 0;
loc_00966631:
    local_r14 = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x4)))));
    local_rbp = (*(uint64_t *)(arg1 + 0x20)) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x4)));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x4)) - 8) >> (1));
loc_00966655:
    if ((uint32_t)(a3) == 0) goto loc_00966709;
    Arg2 = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8))) >> (12));
    if ((uint16_t)(Arg2) == 0) goto loc_009669A0;
    if (0 != ((uint8_t)(Arg2))) goto loc_00966981;
loc_0096667E:
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) & ((uint16_t)((uint32_t)(0xFFFULL))));
    result = (uint16_t)((result) + (0));
    if (((uint16_t)(result)) <= 0) goto loc_00966950;
loc_0096668F:
    result = (uint16_t)((result) - (0));
    if (((uint16_t)(result)) != 4) goto loc_009666CA;
    result = 0 + 2;
    if (0 != 254) { result = 0; }
    local_rdi = 0;
    if (0 != 254) { local_rdi = (uint32_t)(0 + 1); }
loc_009666BD:
    local_r10 = (*(uint64_t *)(arg1 + 0x20) + 8) + (2);
    a3 = (uint32_t)((a3) - 1);
    goto loc_00966655;
loc_009666CA:
    if ((uint32_t)(local_rdi) != 0) goto loc_009666EF;
loc_009666CE:
    if (0 >= 235) goto loc_00966703;
    local_rsi = (result) + 1;
    local_r10 = (local_r10) + (2);
    a3 = (uint32_t)((a3) - 1);
    goto loc_00966655;
loc_009666EF:
    Arg1 = (((uint32_t)(local_rdi)) > 4) ? 1 : 0;
    Arg1 = (Arg1) + 1;
    local_rsi = (local_rsi) + (Arg1);
    goto loc_009666CE;
loc_00966703:
    local_rsi = (local_rsi) + (2);
    goto loc_009666BD;
loc_00966709:
    if (0 != 0) goto loc_0096692C;
loc_00966711:
    local_rsi = (local_rsi) + (2);
    result = (uint32_t)((local_rsi) & (1));
    local_rsi = (local_rsi) + (result);
    if ((uint32_t)(local_r14) != 0) goto loc_00966631;
    if (0 == 0) goto loc_0096695F;
    result = ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x38))) + (13);
    result = MiAllocatePool(256, local_rsi + result * 8, (uint32_t)(0x65526D4DULL), (uint16_t)((uint16_t)(result)));
    v_stack_p20 = result;
    if (result == 0) goto loc_0096695F;
    local_r14 = (*(uint64_t *)(v_stack_p8 + 0x20)) - (*(uint64_t *)(v_stack_p8));
    *(uint64_t *)(result) = v_xmm0;
    local_r14 = (local_r14) >> (3);
    v_stack_p18 = local_r14;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x60) = v_xmm0;
    *(uint8_t *)(result + 0x40) = 0;
    local_rbx = 0;
    *(uint64_t *)(result) = result + 104;
    *(uint64_t *)(result + 0x20) = result + 104 + (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x38)) * 8;
    if ((uint32_t)(local_r14) == 0) goto loc_00966808;
    local_r15 = (v_stack_p8 + 104) - (result + 104);
loc_009667E3:
    if (0 >= (*(uint32_t *)(v_stack_p8 + 0x38))) goto loc_009667F5;
    if ((*(uint64_t *)(local_r15 + result + 0x68 * 1)) > 1) goto loc_00966827;
    *(uint64_t *)(result + 0x68) = *(uint64_t *)(local_r15 + result + 0x68 * 1);
loc_009667F5:
    local_rbp = (uint32_t)((0) + 1);
    local_rsi = (result + 104) + (8);
    if (((uint32_t)(local_rbp)) < ((uint32_t)(local_r14))) goto loc_009667E3;
loc_00966808:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p8, Arg2, (uint32_t)(0x65526D4DULL), (uint32_t)(0x1000ULL));
loc_00966815:
    local_rsp = (local_rsp) + (40);
    return v_stack_p20;
loc_00966827:
    *(uint64_t *)(local_rsi) = 0;
    if (((*(uint8_t *)(local_r15 + local_rsi * 1)) & (1)) != 0) goto loc_009669AC;
loc_00966835:
    local_r13 = (*(uint64_t *)(v_stack_p8 + 0x20)) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x20) + 0x4)));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x20) + 0x4)) - 8) >> (1));
    if (condition_is_equal) goto loc_009668AF;
loc_00966860:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20) + 0x8))) < ((uint16_t)((uint32_t)(0x1000ULL)))) goto loc_0096689D;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20) + 0x8)) & ((uint16_t)(v_stack_p20)));
    a4 = (uint16_t)(((uint16_t)(Arg1)) - (0));
    if (((uint16_t)(a4)) != 4) goto loc_009668D7;
    a3 = (uint32_t)((0) + 1);
    if (((uint32_t)(a3)) == 255) {
        *(uint16_t *)(Arg2) = 0xFFEFULL;
        a3 = 0;
        Arg2 = (Arg2) + (2);
    }
loc_0096689D:
    local_r10 = (*(uint64_t *)(v_stack_p8 + 0x20) + 8) + (2);
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00966860;
loc_009668AF:
    if ((uint32_t)(a3) != 0) goto loc_0096693A;
loc_009668B8:
    *(uint16_t *)(Arg2) = 240;
    Arg2 = (Arg2) + (2);
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_009667F5;
    Arg2 = (Arg2) + 1;
    goto loc_009667F5;
loc_009668D7:
    if ((uint32_t)(a3) != 0) goto loc_009668F0;
loc_009668DC:
    if (((uint16_t)((uint32_t)(0x1000ULL))) >= ((uint16_t)(v_stack_p80))) goto loc_00966915;
    *(uint8_t *)(Arg2) = (uint8_t)((uint32_t)(0x1000ULL));
    Arg2 = (Arg2) + 1;
loc_009668EC:
    local_rbx = 0;
    goto loc_00966894;
loc_009668F0:
    if (((uint32_t)(a3)) > 4) goto loc_00966908;
    result = (uint8_t)((239) - ((uint8_t)(a3)));
    *(uint8_t *)(Arg2) = (uint8_t)(result);
    Arg2 = (Arg2) + 1;
loc_00966903:
    a3 = 0;
    goto loc_009668DC;
loc_00966908:
    *(uint8_t *)(Arg2) = 239;
    *(uint8_t *)(Arg2 + 0x1) = 0;
    Arg2 = (Arg2) + (2);
    goto loc_00966903;
loc_00966915:
    a4 = (uint16_t)(((uint32_t)(0x1000ULL)) >> (4));
    result = (uint8_t)(((uint8_t)((uint32_t)(0x1000ULL))) | (240));
    *(uint8_t *)(Arg2) = (uint8_t)(result);
    *(uint8_t *)(Arg2 + 0x1) = (uint8_t)(a4);
    Arg2 = (Arg2) + (2);
    goto loc_009668EC;
loc_0096692C:
    if (((uint32_t)((uint16_t)((uint32_t)(0x1000ULL)))) <= 4) goto loc_00966979;
    local_rsi = (local_rsi) + (2);
    goto loc_00966711;
loc_0096693A:
    if (0 <= 4) goto loc_00966967;
    *(uint8_t *)(Arg2) = 239;
    *(uint8_t *)(Arg2 + 0x1) = 0;
    Arg2 = (Arg2) + (2);
    goto loc_009668B8;
loc_00966950:
    if ((uint16_t)(a4) == 0) goto loc_0096668F;
loc_0096695A:
loc_0096695F:
    goto loc_00966815;
loc_00966967:
    result = (uint8_t)((239) - (0));
    *(uint8_t *)(Arg2) = (uint8_t)(result);
    Arg2 = (Arg2) + 1;
    goto loc_009668B8;
loc_00966979:
    local_rsi = (local_rsi) + 1;
    goto loc_00966711;
loc_00966981:
    if (((uint8_t)(local_r15)) >= 1) goto loc_0096695A;
    *(uint8_t *)(local_rsp + (uint8_t)(local_r15) * 1 + 0x78) = (uint8_t)(Arg2);
    local_r15 = (uint8_t)((local_r15) + 1);
    goto loc_0096667E;
loc_009669A0:
    local_r10 = (local_r10) + (2);
    a3 = (uint32_t)((a3) - 1);
    goto loc_00966655;
loc_009669AC:
    result = (Arg2) | (1);
    *(uint64_t *)(local_rsi) = result;
    goto loc_00966835;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00966600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
