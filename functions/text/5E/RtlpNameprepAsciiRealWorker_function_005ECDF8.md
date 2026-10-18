# RtlpNameprepAsciiRealWorker

- RVA: `0x005ECDF8`–`0x005ED14B` (길이 `851` bytes)
- VA: `0x00000001405ECDF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFD80`
- 디코드: `253`개 명령, `851/851` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005ECEA4` → [RtlStringCchLengthW](../43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)
- `0x005ECEDC` → [RtlpValidateAsciiStd3AndLength](../../page/79/RtlpValidateAsciiStd3AndLength_function_00791F68.md) (function, `0x00791F68`)
- `0x005ECF1C` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005ECF47` → [FindEmailAt](FindEmailAt_function_005ECA74.md) (function, `0x005ECA74`)
- `0x005ECF75` → [RtlNormalizeString](../../page/79/RtlNormalizeString_function_00794640.md) (function, `0x00794640`)
- `0x005ECFCB` → [RtlNormalizeString](../../page/79/RtlNormalizeString_function_00794640.md) (function, `0x00794640`)
- `0x005ED08F` → [punycode_encode](../../page/79/punycode_encode_function_007926F4.md) (function, `0x007926F4`)
- `0x005ED11B` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [RtlpNameprepAsciiWorker](../../page/79/RtlpNameprepAsciiWorker_function_00791E8C.md) at `0x00791F17`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x005ECEDC` → [RtlpValidateAsciiStd3AndLength](../../page/79/RtlpValidateAsciiStd3AndLength_function_00791F68.md) (`.text` → `PAGE`)
  - `0x005ECF75` → [RtlNormalizeString](../../page/79/RtlNormalizeString_function_00794640.md) (`.text` → `PAGE`)
  - `0x005ECFCB` → [RtlNormalizeString](../../page/79/RtlNormalizeString_function_00794640.md) (`.text` → `PAGE`)
  - `0x005ED08F` → [punycode_encode](../../page/79/punycode_encode_function_007926F4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005ECDF8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005ECDFD  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005ECE02  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005ECE07  55                              push rbp
005ECE08  41 54                           push r12
005ECE0A  41 55                           push r13
005ECE0C  41 56                           push r14
005ECE0E  41 57                           push r15
005ECE10  48 8B EC                        mov rbp, rsp
005ECE13  48 83 EC 40                     sub rsp, 0x40
005ECE17  45 33 D2                        xor r10d, r10d
005ECE1A  4D 8B E1                        mov r12, r9
005ECE1D  41 8B D8                        mov ebx, r8d
005ECE20  4C 8B FA                        mov r15, rdx
005ECE23  44 8B E9                        mov r13d, ecx
005ECE26  48 85 D2                        test rdx, rdx
005ECE29  0F 84 F8 02 00 00               je 0x1405ed127
005ECE2F  83 FB FF                        cmp ebx, -1
005ECE32  0F 8C EF 02 00 00               jl 0x1405ed127
005ECE38  48 8B 75 50                     mov rsi, qword ptr [rbp + 0x50]
005ECE3C  48 85 F6                        test rsi, rsi
005ECE3F  0F 84 E2 02 00 00               je 0x1405ed127
005ECE45  44 8B 36                        mov r14d, dword ptr [rsi]
005ECE48  45 85 F6                        test r14d, r14d
005ECE4B  0F 88 D6 02 00 00               js 0x1405ed127
005ECE51  7E 09                           jle 0x1405ece5c
005ECE53  4D 85 C9                        test r9, r9
005ECE56  0F 84 CB 02 00 00               je 0x1405ed127
005ECE5C  41 F7 C5 F8 FF FF FF            test r13d, 0xfffffff8
005ECE63  0F 85 BE 02 00 00               jne 0x1405ed127
005ECE69  41 8B C5                        mov eax, r13d
005ECE6C  44 88 55 68                     mov byte ptr [rbp + 0x68], r10b
005ECE70  83 E0 01                        and eax, 1
005ECE73  41 8A FA                        mov dil, r10b
005ECE76  89 45 F8                        mov dword ptr [rbp - 8], eax
005ECE79  41 8B C5                        mov eax, r13d
005ECE7C  83 E0 04                        and eax, 4
005ECE7F  89 45 38                        mov dword ptr [rbp + 0x38], eax
005ECE82  0F 95 C2                        setne dl
005ECE85  41 D1 ED                        shr r13d, 1
005ECE88  41 80 E5 01                     and r13b, 1
005ECE8C  88 55 78                        mov byte ptr [rbp + 0x78], dl
005ECE8F  83 FB FF                        cmp ebx, -1
005ECE92  75 25                           jne 0x1405eceb9
005ECE94  4C 8D 45 F0                     lea r8, [rbp - 0x10]
005ECE98  4C 89 55 F0                     mov qword ptr [rbp - 0x10], r10
005ECE9C  BA FF FF FF 7F                  mov edx, 0x7fffffff
005ECEA1  49 8B CF                        mov rcx, r15
005ECEA4  E8 C7 8B E4 FF                  call 0x140435a70
005ECEA9  85 C0                           test eax, eax
005ECEAB  0F 88 76 02 00 00               js 0x1405ed127
005ECEB1  8B 5D F0                        mov ebx, dword ptr [rbp - 0x10]
005ECEB4  8A 55 78                        mov dl, byte ptr [rbp + 0x78]
005ECEB7  FF C3                           inc ebx
005ECEB9  85 DB                           test ebx, ebx
005ECEBB  7E 14                           jle 0x1405eced1
005ECEBD  48 63 C3                        movsxd rax, ebx
005ECEC0  66 45 39 54 47 FE               cmp word ptr [r15 + rax*2 - 2], r10w
005ECEC6  75 09                           jne 0x1405eced1
005ECEC8  40 B7 01                        mov dil, 1
005ECECB  FF CB                           dec ebx
005ECECD  40 88 7D 68                     mov byte ptr [rbp + 0x68], dil
005ECED1  44 8A C2                        mov r8b, dl
005ECED4  45 8A CD                        mov r9b, r13b
005ECED7  8B D3                           mov edx, ebx
005ECED9  49 8B CF                        mov rcx, r15
005ECEDC  E8 87 50 1A 00                  call 0x140791f68
005ECEE1  45 33 DB                        xor r11d, r11d
005ECEE4  84 C0                           test al, al
005ECEE6  74 42                           je 0x1405ecf2a
005ECEE8  85 DB                           test ebx, ebx
005ECEEA  75 0A                           jne 0x1405ecef6
005ECEEC  B8 16 07 00 C0                  mov eax, 0xc0000716
005ECEF1  E9 36 02 00 00                  jmp 0x1405ed12c
005ECEF6  40 84 FF                        test dil, dil
005ECEF9  74 02                           je 0x1405ecefd
005ECEFB  FF C3                           inc ebx
005ECEFD  4D 85 E4                        test r12, r12
005ECF00  74 1F                           je 0x1405ecf21
005ECF02  45 85 F6                        test r14d, r14d
005ECF05  74 1A                           je 0x1405ecf21
005ECF07  41 3B DE                        cmp ebx, r14d
005ECF0A  0F 8F F5 01 00 00               jg 0x1405ed105
005ECF10  49 8B D7                        mov rdx, r15
005ECF13  4C 63 C3                        movsxd r8, ebx
005ECF16  49 8B CC                        mov rcx, r12
005ECF19  4D 03 C0                        add r8, r8
005ECF1C  E8 1F 99 0D 00                  call 0x1406c6840
005ECF21  89 1E                           mov dword ptr [rsi], ebx
005ECF23  33 C0                           xor eax, eax
005ECF25  E9 02 02 00 00                  jmp 0x1405ed12c
005ECF2A  41 8B C3                        mov eax, r11d
005ECF2D  4C 8B 55 60                     mov r10, qword ptr [rbp + 0x60]
005ECF31  4D 8B CA                        mov r9, r10
005ECF34  B9 FF 01 00 00                  mov ecx, 0x1ff
005ECF39  41 8B FB                        mov edi, r11d
005ECF3C  44 39 5D 38                     cmp dword ptr [rbp + 0x38], r11d
005ECF40  74 61                           je 0x1405ecfa3
005ECF42  8B D3                           mov edx, ebx
005ECF44  49 8B CF                        mov rcx, r15
005ECF47  E8 28 FB FF FF                  call 0x1405eca74
005ECF4C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
005ECF4F  85 C0                           test eax, eax
005ECF51  0F 84 E9 00 00 00               je 0x1405ed040
005ECF57  48 8D 4D 38                     lea rcx, [rbp + 0x38]
005ECF5B  C7 45 38 FF 01 00 00            mov dword ptr [rbp + 0x38], 0x1ff
005ECF62  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005ECF67  4D 8B CA                        mov r9, r10
005ECF6A  B9 01 00 00 00                  mov ecx, 1
005ECF6F  44 8B C0                        mov r8d, eax
005ECF72  49 8B D7                        mov rdx, r15
005ECF75  E8 C6 76 1A 00                  call 0x140794640
005ECF7A  48 63 7D 38                     movsxd rdi, dword ptr [rbp + 0x38]
005ECF7E  45 33 DB                        xor r11d, r11d
005ECF81  85 C0                           test eax, eax
005ECF83  0F 88 A3 00 00 00               js 0x1405ed02c
005ECF89  85 FF                           test edi, edi
005ECF8B  0F 84 99 00 00 00               je 0x1405ed02a
005ECF91  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
005ECF95  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
005ECF98  4C 8D 0C 79                     lea r9, [rcx + rdi*2]
005ECF9C  B9 FF 01 00 00                  mov ecx, 0x1ff
005ECFA1  2B CF                           sub ecx, edi
005ECFA3  3B C3                           cmp eax, ebx
005ECFA5  7D 39                           jge 0x1405ecfe0
005ECFA7  89 4D 38                        mov dword ptr [rbp + 0x38], ecx
005ECFAA  44 8B C3                        mov r8d, ebx
005ECFAD  44 2B C0                        sub r8d, eax
005ECFB0  48 8D 4D 38                     lea rcx, [rbp + 0x38]
005ECFB4  48 98                           cdqe
005ECFB6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005ECFBB  49 8D 14 47                     lea rdx, [r15 + rax*2]
005ECFBF  8B 45 F8                        mov eax, dword ptr [rbp - 8]
005ECFC2  83 F0 01                        xor eax, 1
005ECFC5  C1 E0 08                        shl eax, 8
005ECFC8  8D 48 0D                        lea ecx, [rax + 0xd]
005ECFCB  E8 70 76 1A 00                  call 0x140794640
005ECFD0  8B 4D 38                        mov ecx, dword ptr [rbp + 0x38]
005ECFD3  45 33 DB                        xor r11d, r11d
005ECFD6  85 C0                           test eax, eax
005ECFD8  78 75                           js 0x1405ed04f
005ECFDA  85 C9                           test ecx, ecx
005ECFDC  74 6F                           je 0x1405ed04d
005ECFDE  03 F9                           add edi, ecx
005ECFE0  85 FF                           test edi, edi
005ECFE2  0F 8E 80 00 00 00               jle 0x1405ed068
005ECFE8  8D 47 FF                        lea eax, [rdi - 1]
005ECFEB  48 63 C8                        movsxd rcx, eax
005ECFEE  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
005ECFF2  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
005ECFF6  66 83 FA 2E                     cmp dx, 0x2e
005ECFFA  75 67                           jne 0x1405ed063
005ECFFC  48 63 C3                        movsxd rax, ebx
005ECFFF  41 0F B7 4C 47 FE               movzx ecx, word ptr [r15 + rax*2 - 2]
005ED005  66 3B CA                        cmp cx, dx
005ED008  74 5E                           je 0x1405ed068
005ED00A  B8 02 30 00 00                  mov eax, 0x3002
005ED00F  66 3B C8                        cmp cx, ax
005ED012  74 54                           je 0x1405ed068
005ED014  B8 0E FF 00 00                  mov eax, 0xff0e
005ED019  66 3B C8                        cmp cx, ax
005ED01C  74 4A                           je 0x1405ed068
005ED01E  B8 61 FF 00 00                  mov eax, 0xff61
005ED023  66 3B C8                        cmp cx, ax
005ED026  74 40                           je 0x1405ed068
005ED028  EB 16                           jmp 0x1405ed040
005ED02A  85 C0                           test eax, eax
005ED02C  74 12                           je 0x1405ed040
005ED02E  3D 23 00 00 C0                  cmp eax, 0xc0000023
005ED033  74 0B                           je 0x1405ed040
005ED035  3D 17 07 00 C0                  cmp eax, 0xc0000717
005ED03A  74 04                           je 0x1405ed040
005ED03C  85 FF                           test edi, edi
005ED03E  7E 05                           jle 0x1405ed045
005ED040  B8 16 07 00 C0                  mov eax, 0xc0000716
005ED045  44 89 1E                        mov dword ptr [rsi], r11d
005ED048  E9 DF 00 00 00                  jmp 0x1405ed12c
005ED04D  85 C0                           test eax, eax
005ED04F  74 EF                           je 0x1405ed040
005ED051  3D 23 00 00 C0                  cmp eax, 0xc0000023
005ED056  74 E8                           je 0x1405ed040
005ED058  3D 17 07 00 C0                  cmp eax, 0xc0000717
005ED05D  74 E1                           je 0x1405ed040
005ED05F  85 C9                           test ecx, ecx
005ED061  EB DB                           jmp 0x1405ed03e
005ED063  66 85 D2                        test dx, dx
005ED066  74 D8                           je 0x1405ed040
005ED068  8A 45 78                        mov al, byte ptr [rbp + 0x78]
005ED06B  4C 8D 4D 38                     lea r9, [rbp + 0x38]
005ED06F  4C 8B 7D 60                     mov r15, qword ptr [rbp + 0x60]
005ED073  8B D7                           mov edx, edi
005ED075  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
005ED07A  49 8B CF                        mov rcx, r15
005ED07D  4C 8B 6D 70                     mov r13, qword ptr [rbp + 0x70]
005ED081  4D 8B C5                        mov r8, r13
005ED084  C7 45 38 03 02 00 00            mov dword ptr [rbp + 0x38], 0x203
005ED08B  88 44 24 20                     mov byte ptr [rsp + 0x20], al
005ED08F  E8 60 56 1A 00                  call 0x1407926f4
005ED094  48 63 5D 38                     movsxd rbx, dword ptr [rbp + 0x38]
005ED098  45 33 DB                        xor r11d, r11d
005ED09B  85 DB                           test ebx, ebx
005ED09D  74 A6                           je 0x1405ed045
005ED09F  44 38 5D 58                     cmp byte ptr [rbp + 0x58], r11b
005ED0A3  74 35                           je 0x1405ed0da
005ED0A5  44 38 5D 68                     cmp byte ptr [rbp + 0x68], r11b
005ED0A9  74 10                           je 0x1405ed0bb
005ED0AB  81 FB 03 02 00 00               cmp ebx, 0x203
005ED0B1  7D 8D                           jge 0x1405ed040
005ED0B3  66 45 89 5C 5D 00               mov word ptr [r13 + rbx*2], r11w
005ED0B9  FF C3                           inc ebx
005ED0BB  4D 85 E4                        test r12, r12
005ED0BE  0F 84 5D FE FF FF               je 0x1405ecf21
005ED0C4  45 85 F6                        test r14d, r14d
005ED0C7  0F 84 54 FE FF FF               je 0x1405ecf21
005ED0CD  41 3B DE                        cmp ebx, r14d
005ED0D0  7F 33                           jg 0x1405ed105
005ED0D2  49 8B D5                        mov rdx, r13
005ED0D5  E9 39 FE FF FF                  jmp 0x1405ecf13
005ED0DA  44 38 5D 68                     cmp byte ptr [rbp + 0x68], r11b
005ED0DE  74 16                           je 0x1405ed0f6
005ED0E0  81 FF FF 01 00 00               cmp edi, 0x1ff
005ED0E6  0F 8F 54 FF FF FF               jg 0x1405ed040
005ED0EC  48 63 C7                        movsxd rax, edi
005ED0EF  FF C7                           inc edi
005ED0F1  66 45 89 1C 47                  mov word ptr [r15 + rax*2], r11w
005ED0F6  4D 85 E4                        test r12, r12
005ED0F9  74 25                           je 0x1405ed120
005ED0FB  45 85 F6                        test r14d, r14d
005ED0FE  74 20                           je 0x1405ed120
005ED100  41 3B FE                        cmp edi, r14d
005ED103  7E 0A                           jle 0x1405ed10f
005ED105  B8 23 00 00 C0                  mov eax, 0xc0000023
005ED10A  E9 36 FF FF FF                  jmp 0x1405ed045
005ED10F  4C 63 C7                        movsxd r8, edi
005ED112  49 8B D7                        mov rdx, r15
005ED115  4D 03 C0                        add r8, r8
005ED118  49 8B CC                        mov rcx, r12
005ED11B  E8 20 97 0D 00                  call 0x1406c6840
005ED120  89 3E                           mov dword ptr [rsi], edi
005ED122  E9 FC FD FF FF                  jmp 0x1405ecf23
005ED127  B8 0D 00 00 C0                  mov eax, 0xc000000d
005ED12C  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
005ED131  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005ED135  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
005ED139  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
005ED13D  49 8B E3                        mov rsp, r11
005ED140  41 5F                           pop r15
005ED142  41 5E                           pop r14
005ED144  41 5D                           pop r13
005ED146  41 5C                           pop r12
005ED148  5D                              pop rbp
005ED149  C3                              ret
005ED14A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpNameprepAsciiRealWorker(int a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned __int8 a6, __int64 a7, unsigned __int8 a8, __int64 a9, unsigned __int8 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (64);
    v_r10 = 0;
    if (a2 == 0) goto loc_005ED127;
    if (((unsigned int)((unsigned int)(a3))) < -1) goto loc_005ED127;
    if (a5 == 0) goto loc_005ED127;
    if (sign_flag) goto loc_005ED127;
    if (condition_is_less_or_equal) goto loc_005ECE5C;
    if (a4 == 0) goto loc_005ED127;
loc_005ECE5C:
    if ((((unsigned int)((unsigned int)(a1))) & (0xFFFFFFF8ULL)) != 0) goto loc_005ED127;
    v_stack_p40 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) & (1));
    v_stack_m30 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) & (4));
    v_stack_p10 = (unsigned int)(result);
    a2 = (condition_is_not_equal) ? 1 : 0;
    v_r13 = (unsigned int)(((unsigned int)(a1)) >> (1));
    v_r13 = (unsigned __int8)((v_r13) & (1));
    v_stack_p50 = (unsigned __int8)(a2);
    if (((unsigned int)((unsigned int)(a3))) != -1) goto loc_005ECEB9;
    v_stack_m38 = 0;
    result = RtlStringCchLengthW(a2, (unsigned int)(0x7FFFFFFFULL), v_stack_m38, a4);
    if (sign_flag) goto loc_005ED127;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m38)) + 1);
loc_005ECEB9:
    if (condition_is_less_or_equal) goto loc_005ECED1;
    v_rdi = 0;
    if ((*(unsigned __int16 *)(a2 + (int)((unsigned int)(v_rbx)) * 2 - 2)) == 0) {
        v_rdi = 1;
        v_rbx = (unsigned int)((v_rbx) - 1);
        v_stack_p40 = (unsigned __int8)(v_rdi);
    }
    result = RtlpValidateAsciiStd3AndLength(a2, (unsigned int)((unsigned int)(v_rbx)), a10, (unsigned __int8)(v_r13));
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_005ECF2A;
    if ((unsigned int)(v_rbx) != 0) goto loc_005ECEF6;
    goto loc_005ED12C;
loc_005ECEF6:
    if ((unsigned __int8)(v_rdi) != 0) {
        v_rbx = (unsigned int)((v_rbx) + 1);
    }
    if (a4 == 0) goto loc_005ECF21;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5))) == 0) goto loc_005ECF21;
    if (((unsigned int)(v_rbx)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) goto loc_005ED105;
loc_005ECF13:
    a3 = ((int)((unsigned int)(v_rbx))) + ((int)((unsigned int)(v_rbx)));
    result = memcpy(a4, a2, a3, (unsigned __int8)(v_r13));
loc_005ECF21:
    *(unsigned int *)(a5) = (unsigned int)(v_rbx);
loc_005ECF23:
    result = 0;
    goto loc_005ED12C;
loc_005ECF2A:
    if (v_stack_p10 == 0) goto loc_005ECFA3;
    result = FindEmailAt(a2, (unsigned int)((unsigned int)(v_rbx)), a3, a7);
    v_stack_m38 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_005ED040;
    v_stack_p10 = 511;
    v_stack_m48 = v_stack_p10;
    result = RtlNormalizeString(1, a2, (unsigned int)((unsigned int)(result)), a7);
    v_r11 = 0;
    if (sign_flag) goto loc_005ED02C;
    if ((unsigned int)((int)(v_stack_p10)) == 0) goto loc_005ED02A;
    a1 = (unsigned int)((511) - ((unsigned int)((int)(v_stack_p10))));
loc_005ECFA3:
    if (((unsigned int)((unsigned int)(v_stack_m38))) >= ((unsigned int)(v_rbx))) goto loc_005ECFE0;
    v_stack_p10 = a1;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)((unsigned int)(v_stack_m38))));
    v_stack_m48 = v_stack_p10;
    result = (unsigned int)(((unsigned int)(v_stack_m30)) ^ (1));
    result = (unsigned int)((result) << (8));
    result = RtlNormalizeString(result + 13, a2 + (unsigned int)(v_stack_m38) * 2, a3, a7 + (int)(v_stack_p10) * 2);
    v_r11 = 0;
    if (sign_flag) goto loc_005ED04F;
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_005ED04D;
    v_rdi = (unsigned int)(((int)(v_stack_p10)) + ((unsigned int)((unsigned int)(v_stack_p10))));
loc_005ECFE0:
    if (condition_is_less_or_equal) goto loc_005ED068;
    if (((unsigned __int16)(*(unsigned __int16 *)(a7 + (int)((unsigned int)(v_rdi - 1)) * 2))) != 46) goto loc_005ED063;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + (int)((unsigned int)(v_rbx)) * 2 - 2))) == ((unsigned __int16)(*(unsigned __int16 *)(a7 + (int)((unsigned int)(v_rdi - 1)) * 2)))) goto loc_005ED068;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + (int)((unsigned int)(v_rbx)) * 2 - 2))) == ((unsigned __int16)((unsigned int)(0x3002ULL)))) goto loc_005ED068;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + (int)((unsigned int)(v_rbx)) * 2 - 2))) == ((unsigned __int16)((unsigned int)(0xFF0EULL)))) goto loc_005ED068;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + (int)((unsigned int)(v_rbx)) * 2 - 2))) == ((unsigned __int16)((unsigned int)(0xFF61ULL)))) goto loc_005ED068;
    goto loc_005ED040;
loc_005ED02A:
loc_005ED02C:
    if ((unsigned int)((unsigned int)(0xFF61ULL)) == 0) goto loc_005ED040;
    if (((unsigned int)((unsigned int)(0xFF61ULL))) == 0xC0000023ULL) goto loc_005ED040;
    if (((unsigned int)((unsigned int)(0xFF61ULL))) == 0xC0000717ULL) goto loc_005ED040;
loc_005ED03E:
    result = (unsigned int)(0xFF61ULL);
    if (!(condition_is_less_or_equal)) {
        result = 0xC0000716ULL;
    }
    *(unsigned int *)(a5) = 0;
    goto loc_005ED12C;
loc_005ED04D:
loc_005ED04F:
    if ((unsigned int)(result) == 0) goto loc_005ED040;
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_005ED040;
    if (((unsigned int)(result)) == 0xC0000717ULL) goto loc_005ED040;
    goto loc_005ED03E;
loc_005ED063:
    if ((unsigned __int16)(*(unsigned __int16 *)(a7 + (int)((unsigned int)(v_rdi - 1)) * 2)) == 0) goto loc_005ED040;
loc_005ED068:
    v_stack_m40 = (unsigned __int8)(v_r13);
    v_stack_p10 = 515;
    v_stack_m48 = a10;
    result = punycode_encode(a7, (unsigned int)((unsigned int)(v_rdi)), a9, v_stack_p10);
    v_r11 = 0;
    if ((unsigned int)((int)(v_stack_p10)) == 0) goto loc_005ED045;
    if (a6 == 0) goto loc_005ED0DA;
    if (a8 == 0) goto loc_005ED0BB;
    if (((unsigned int)((int)(v_stack_p10))) >= 515) goto loc_005ED040;
    *(unsigned __int16 *)(a9 + (int)(v_stack_p10) * 2) = 0;
    v_rbx = (unsigned int)(((int)(v_stack_p10)) + 1);
loc_005ED0BB:
    if (a4 == 0) goto loc_005ECF21;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5))) == 0) goto loc_005ECF21;
    if (((unsigned int)(v_rbx)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) goto loc_005ED105;
    goto loc_005ECF13;
loc_005ED0DA:
    if (a8 == 0) goto loc_005ED0F6;
    if (((unsigned int)(v_rdi)) > 511) goto loc_005ED040;
    v_rdi = (unsigned int)((v_rdi) + 1);
    *(unsigned __int16 *)(a7 + (int)((unsigned int)(v_rdi)) * 2) = 0;
loc_005ED0F6:
    if (a4 == 0) goto loc_005ED120;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5))) == 0) goto loc_005ED120;
    if (((unsigned int)(v_rdi)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) goto loc_005ED10F;
loc_005ED105:
    goto loc_005ED045;
loc_005ED10F:
    a3 = ((int)((unsigned int)(v_rdi))) + ((int)((unsigned int)(v_rdi)));
    result = memcpy(a4, a7, a3, v_stack_p10);
loc_005ED120:
    *(unsigned int *)(a5) = (unsigned int)(v_rdi);
    goto loc_005ECF23;
loc_005ED127:
loc_005ED12C:
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t RtlpNameprepAsciiRealWorker(int32_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6, void *Arg7, uint8_t Arg8, void *Arg9, uint8_t Arg10)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint8_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p40;
    uint8_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (64);
    local_r10 = 0;
    if (Arg2 == NULL) goto loc_005ED127;
    if (((uint32_t)((uint32_t)(Arg3))) < -1) goto loc_005ED127;
    if (Arg5 == 0) goto loc_005ED127;
    if (sign_flag) goto loc_005ED127;
    if (condition_is_less_or_equal) goto loc_005ECE5C;
    if (Arg4 == 0) goto loc_005ED127;
loc_005ECE5C:
    if ((((uint32_t)((uint32_t)(Arg1))) & (0xFFFFFFF8ULL)) != 0) goto loc_005ED127;
    v_stack_p40 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) & (1));
    v_stack_m30 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) & (4));
    v_stack_p10 = (uint32_t)(result);
    Arg2 = (condition_is_not_equal) ? 1 : 0;
    local_r13 = (uint32_t)(((uint32_t)(Arg1)) >> (1));
    local_r13 = (uint8_t)((local_r13) & (1));
    v_stack_p50 = (uint8_t)(Arg2);
    if (((uint32_t)((uint32_t)(Arg3))) != -1) goto loc_005ECEB9;
    v_stack_m38 = 0;
    result = RtlStringCchLengthW(Arg2, (uint32_t)(0x7FFFFFFFULL), v_stack_m38, Arg4);
    if (sign_flag) goto loc_005ED127;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m38)) + 1);
loc_005ECEB9:
    if (condition_is_less_or_equal) goto loc_005ECED1;
    local_rdi = 0;
    if ((*(uint16_t *)(arg2 + (int32_t)((uint32_t)(local_rbx)) * 2 - 0x2)) == 0) {
        local_rdi = 1;
        local_rbx = (uint32_t)((local_rbx) - 1);
        v_stack_p40 = (uint8_t)(local_rdi);
    }
    result = RtlpValidateAsciiStd3AndLength(Arg2, (uint32_t)((uint32_t)(local_rbx)), Arg10, (uint8_t)(local_r13));
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_005ECF2A;
    if ((uint32_t)(local_rbx) != 0) goto loc_005ECEF6;
    goto loc_005ED12C;
loc_005ECEF6:
    if ((uint8_t)(local_rdi) != 0) {
        local_rbx = (uint32_t)((local_rbx) + 1);
    }
    if (Arg4 == 0) goto loc_005ECF21;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5))) == 0) goto loc_005ECF21;
    if (((uint32_t)(local_rbx)) > ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5))))) goto loc_005ED105;
loc_005ECF13:
    Arg3 = ((int32_t)((uint32_t)(local_rbx))) + ((int32_t)((uint32_t)(local_rbx)));
    result = memcpy(Arg4, Arg2, Arg3, (uint8_t)(local_r13));
loc_005ECF21:
    *(uint32_t *)(Arg5) = (uint32_t)(local_rbx);
loc_005ECF23:
    result = 0;
    goto loc_005ED12C;
loc_005ECF2A:
    if (v_stack_p10 == 0) goto loc_005ECFA3;
    result = FindEmailAt(Arg2, (uint32_t)((uint32_t)(local_rbx)), Arg3, Arg7);
    v_stack_m38 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_005ED040;
    v_stack_p10 = 511;
    v_stack_m48 = v_stack_p10;
    result = RtlNormalizeString(1, Arg2, (uint32_t)((uint32_t)(result)), Arg7);
    local_r11 = 0;
    if (sign_flag) goto loc_005ED02C;
    if ((uint32_t)((int32_t)(v_stack_p10)) == 0) goto loc_005ED02A;
    Arg1 = (uint32_t)((511) - ((uint32_t)((int32_t)(v_stack_p10))));
loc_005ECFA3:
    if (((uint32_t)((uint32_t)(v_stack_m38))) >= ((uint32_t)(local_rbx))) goto loc_005ECFE0;
    v_stack_p10 = Arg1;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)((uint32_t)(v_stack_m38))));
    v_stack_m48 = v_stack_p10;
    result = (uint32_t)(((uint32_t)(v_stack_m30)) ^ (1));
    result = (uint32_t)((result) << (8));
    result = RtlNormalizeString(result + 13, Arg2 + (uint32_t)(v_stack_m38) * 2, Arg3, Arg7 + (int32_t)(v_stack_p10) * 2);
    local_r11 = 0;
    if (sign_flag) goto loc_005ED04F;
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_005ED04D;
    local_rdi = (uint32_t)(((int32_t)(v_stack_p10)) + ((uint32_t)((uint32_t)(v_stack_p10))));
loc_005ECFE0:
    if (condition_is_less_or_equal) goto loc_005ED068;
    if (((uint16_t)(*(uint16_t *)(arg7 + (int32_t)((uint32_t)(local_rdi - 0x1)) * 2))) != 46) goto loc_005ED063;
    if (((uint16_t)(*(uint16_t *)(arg2 + (int32_t)((uint32_t)(local_rbx)) * 2 - 0x2))) == ((uint16_t)(*(uint16_t *)(arg7 + (int32_t)((uint32_t)(local_rdi - 0x1)) * 2)))) goto loc_005ED068;
    if (((uint16_t)(*(uint16_t *)(arg2 + (int32_t)((uint32_t)(local_rbx)) * 2 - 0x2))) == ((uint16_t)((uint32_t)(0x3002ULL)))) goto loc_005ED068;
    if (((uint16_t)(*(uint16_t *)(arg2 + (int32_t)((uint32_t)(local_rbx)) * 2 - 0x2))) == ((uint16_t)((uint32_t)(0xFF0EULL)))) goto loc_005ED068;
    if (((uint16_t)(*(uint16_t *)(arg2 + (int32_t)((uint32_t)(local_rbx)) * 2 - 0x2))) == ((uint16_t)((uint32_t)(0xFF61ULL)))) goto loc_005ED068;
    goto loc_005ED040;
loc_005ED02A:
loc_005ED02C:
    if ((uint32_t)((uint32_t)(0xFF61ULL)) == 0) goto loc_005ED040;
    if (((uint32_t)((uint32_t)(0xFF61ULL))) == 0xC0000023ULL) goto loc_005ED040;
    if (((uint32_t)((uint32_t)(0xFF61ULL))) == 0xC0000717ULL) goto loc_005ED040;
loc_005ED03E:
    result = (uint32_t)(0xFF61ULL);
    if (!(condition_is_less_or_equal)) {
        result = 0xC0000716ULL;
    }
    *(uint32_t *)(Arg5) = 0;
    goto loc_005ED12C;
loc_005ED04D:
loc_005ED04F:
    if ((uint32_t)(result) == 0) goto loc_005ED040;
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_005ED040;
    if (((uint32_t)(result)) == 0xC0000717ULL) goto loc_005ED040;
    goto loc_005ED03E;
loc_005ED063:
    if ((uint16_t)(*(uint16_t *)(arg7 + (int32_t)((uint32_t)(local_rdi - 0x1)) * 2)) == 0) goto loc_005ED040;
loc_005ED068:
    v_stack_m40 = (uint8_t)(local_r13);
    v_stack_p10 = 515;
    v_stack_m48 = Arg10;
    result = punycode_encode(Arg7, (uint32_t)((uint32_t)(local_rdi)), Arg9, v_stack_p10);
    local_r11 = 0;
    if ((uint32_t)((int32_t)(v_stack_p10)) == 0) goto loc_005ED045;
    if (Arg6 == 0) goto loc_005ED0DA;
    if (Arg8 == 0) goto loc_005ED0BB;
    if (((uint32_t)((int32_t)(v_stack_p10))) >= 515) goto loc_005ED040;
    *(uint16_t *)(arg9 + (int32_t)(v_stack_p10) * 2) = 0;
    local_rbx = (uint32_t)(((int32_t)(v_stack_p10)) + 1);
loc_005ED0BB:
    if (Arg4 == 0) goto loc_005ECF21;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5))) == 0) goto loc_005ECF21;
    if (((uint32_t)(local_rbx)) > ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5))))) goto loc_005ED105;
    goto loc_005ECF13;
loc_005ED0DA:
    if (Arg8 == 0) goto loc_005ED0F6;
    if (((uint32_t)(local_rdi)) > 511) goto loc_005ED040;
    local_rdi = (uint32_t)((local_rdi) + 1);
    *(uint16_t *)(arg7 + (int32_t)((uint32_t)(local_rdi)) * 2) = 0;
loc_005ED0F6:
    if (Arg4 == 0) goto loc_005ED120;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5))) == 0) goto loc_005ED120;
    if (((uint32_t)(local_rdi)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5))))) goto loc_005ED10F;
loc_005ED105:
    goto loc_005ED045;
loc_005ED10F:
    Arg3 = ((int32_t)((uint32_t)(local_rdi))) + ((int32_t)((uint32_t)(local_rdi)));
    result = memcpy(Arg4, Arg7, Arg3, v_stack_p10);
loc_005ED120:
    *(uint32_t *)(Arg5) = (uint32_t)(local_rdi);
    goto loc_005ECF23;
loc_005ED127:
loc_005ED12C:
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x2 + rax*2` | `16` | `R` |
| `Arg2` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg7` | `+ 0x0 + rax*2` | `16` | `W` |
| `Arg7` | `+ 0x0 + rcx*2` | `16` | `R` |
| `Arg7` | `+ 0x0 + rdi*2` | `64` | `R` |
| `Arg9` | `+ 0x0 + rbx*2` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005ECDF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
