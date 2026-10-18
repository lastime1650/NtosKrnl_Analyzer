# VmpInsertMemoryRange

- RVA: `0x0064C9F0`–`0x0064CCC9` (길이 `729` bytes)
- VA: `0x000000014064C9F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FEF8`
- 디코드: `232`개 명령, `729/729` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0064CA20` → [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) (function, `0x003147A4`)
- `0x0064CC09` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x0064CC82` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x0064CC95` → [VmpProcessContextUnlockExclusive](../48/VmpProcessContextUnlockExclusive_function_004894C8.md) (function, `0x004894C8`)
- `0x0064CCA2` → [VmpFreeMemoryRanges](../../page/A7/VmpFreeMemoryRanges_function_00A75744.md) (function, `0x00A75744`)

### Direct callers
- [VmCreateMemoryRange](../../page/7A/VmCreateMemoryRange_function_007AD1D0.md) at `0x007AD324`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0064CCA2` → [VmpFreeMemoryRanges](../../page/A7/VmpFreeMemoryRanges_function_00A75744.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064C9F0  48 8B C4                        mov rax, rsp
0064C9F3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0064C9F7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064C9FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064C9FF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064CA03  41 54                           push r12
0064CA05  41 56                           push r14
0064CA07  41 57                           push r15
0064CA09  48 83 EC 20                     sub rsp, 0x20
0064CA0D  48 8B 7A 28                     mov rdi, qword ptr [rdx + 0x28]
0064CA11  49 8B D8                        mov rbx, r8
0064CA14  48 8B F2                        mov rsi, rdx
0064CA17  48 8B E9                        mov rbp, rcx
0064CA1A  45 33 F6                        xor r14d, r14d
0064CA1D  45 33 FF                        xor r15d, r15d
0064CA20  E8 7F 7D CC FF                  call 0x1403147a4
0064CA25  4C 8B 45 68                     mov r8, qword ptr [rbp + 0x68]
0064CA29  4C 8B E0                        mov r12, rax
0064CA2C  49 83 F8 FF                     cmp r8, -1
0064CA30  75 39                           jne 0x14064ca6b
0064CA32  48 89 5D 68                     mov qword ptr [rbp + 0x68], rbx
0064CA36  4C 8D 55 08                     lea r10, [rbp + 8]
0064CA3A  BB 01 00 00 00                  mov ebx, 1
0064CA3F  49 8B 0A                        mov rcx, qword ptr [r10]
0064CA42  41 84 5A 08                     test byte ptr [r10 + 8], bl
0064CA46  74 08                           je 0x14064ca50
0064CA48  48 85 C9                        test rcx, rcx
0064CA4B  74 03                           je 0x14064ca50
0064CA4D  49 33 CA                        xor rcx, r10
0064CA50  41 0F B6 52 08                  movzx edx, byte ptr [r10 + 8]
0064CA55  23 D3                           and edx, ebx
0064CA57  48 85 C9                        test rcx, rcx
0064CA5A  74 51                           je 0x14064caad
0064CA5C  4C 8B 47 38                     mov r8, qword ptr [rdi + 0x38]
0064CA60  4C 3B 41 18                     cmp r8, qword ptr [rcx + 0x18]
0064CA64  73 14                           jae 0x14064ca7a
0064CA66  48 8B 01                        mov rax, qword ptr [rcx]
0064CA69  EB 1D                           jmp 0x14064ca88
0064CA6B  4C 3B C3                        cmp r8, rbx
0064CA6E  74 C6                           je 0x14064ca36
0064CA70  BB 19 07 00 C0                  mov ebx, 0xc0000719
0064CA75  E9 0F 02 00 00                  jmp 0x14064cc89
0064CA7A  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0064CA7E  48 39 47 30                     cmp qword ptr [rdi + 0x30], rax
0064CA82  76 1A                           jbe 0x14064ca9e
0064CA84  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0064CA88  85 D2                           test edx, edx
0064CA8A  74 0A                           je 0x14064ca96
0064CA8C  48 85 C0                        test rax, rax
0064CA8F  74 05                           je 0x14064ca96
0064CA91  48 33 C8                        xor rcx, rax
0064CA94  EB 03                           jmp 0x14064ca99
0064CA96  48 8B C8                        mov rcx, rax
0064CA99  48 85 C9                        test rcx, rcx
0064CA9C  75 C2                           jne 0x14064ca60
0064CA9E  48 85 C9                        test rcx, rcx
0064CAA1  74 0A                           je 0x14064caad
0064CAA3  BB 18 00 00 C0                  mov ebx, 0xc0000018
0064CAA8  E9 DC 01 00 00                  jmp 0x14064cc89
0064CAAD  48 8D 4D 18                     lea rcx, [rbp + 0x18]
0064CAB1  48 8B 11                        mov rdx, qword ptr [rcx]
0064CAB4  84 59 08                        test byte ptr [rcx + 8], bl
0064CAB7  74 08                           je 0x14064cac1
0064CAB9  48 85 D2                        test rdx, rdx
0064CABC  74 03                           je 0x14064cac1
0064CABE  48 33 D1                        xor rdx, rcx
0064CAC1  44 0F B6 41 08                  movzx r8d, byte ptr [rcx + 8]
0064CAC6  44 23 C3                        and r8d, ebx
0064CAC9  48 85 D2                        test rdx, rdx
0064CACC  0F 84 C3 00 00 00               je 0x14064cb95
0064CAD2  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0064CAD6  48 3B 4A 18                     cmp rcx, qword ptr [rdx + 0x18]
0064CADA  73 05                           jae 0x14064cae1
0064CADC  48 8B 02                        mov rax, qword ptr [rdx]
0064CADF  EB 0E                           jmp 0x14064caef
0064CAE1  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
0064CAE5  48 39 46 18                     cmp qword ptr [rsi + 0x18], rax
0064CAE9  76 1B                           jbe 0x14064cb06
0064CAEB  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0064CAEF  45 85 C0                        test r8d, r8d
0064CAF2  74 0A                           je 0x14064cafe
0064CAF4  48 85 C0                        test rax, rax
0064CAF7  74 05                           je 0x14064cafe
0064CAF9  48 33 D0                        xor rdx, rax
0064CAFC  EB 03                           jmp 0x14064cb01
0064CAFE  48 8B D0                        mov rdx, rax
0064CB01  48 85 D2                        test rdx, rdx
0064CB04  75 D0                           jne 0x14064cad6
0064CB06  48 85 D2                        test rdx, rdx
0064CB09  0F 84 86 00 00 00               je 0x14064cb95
0064CB0F  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0064CB13  4C 8B FA                        mov r15, rdx
0064CB16  48 39 42 18                     cmp qword ptr [rdx + 0x18], rax
0064CB1A  75 87                           jne 0x14064caa3
0064CB1C  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0064CB20  48 39 42 20                     cmp qword ptr [rdx + 0x20], rax
0064CB24  0F 85 79 FF FF FF               jne 0x14064caa3
0064CB2A  8B 4A 48                        mov ecx, dword ptr [rdx + 0x48]
0064CB2D  33 4E 48                        xor ecx, dword ptr [rsi + 0x48]
0064CB30  F6 C1 02                        test cl, 2
0064CB33  0F 85 6A FF FF FF               jne 0x14064caa3
0064CB39  48 8B 07                        mov rax, qword ptr [rdi]
0064CB3C  48 39 78 08                     cmp qword ptr [rax + 8], rdi
0064CB40  0F 85 98 00 00 00               jne 0x14064cbde
0064CB46  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0064CB4A  48 39 39                        cmp qword ptr [rcx], rdi
0064CB4D  0F 85 8B 00 00 00               jne 0x14064cbde
0064CB53  48 89 01                        mov qword ptr [rcx], rax
0064CB56  48 89 48 08                     mov qword ptr [rax + 8], rcx
0064CB5A  48 89 57 10                     mov qword ptr [rdi + 0x10], rdx
0064CB5E  48 83 C2 28                     add rdx, 0x28
0064CB62  48 8B 0A                        mov rcx, qword ptr [rdx]
0064CB65  48 3B CA                        cmp rcx, rdx
0064CB68  74 12                           je 0x14064cb7c
0064CB6A  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0064CB6E  48 39 41 30                     cmp qword ptr [rcx + 0x30], rax
0064CB72  77 08                           ja 0x14064cb7c
0064CB74  48 8B 09                        mov rcx, qword ptr [rcx]
0064CB77  48 3B CA                        cmp rcx, rdx
0064CB7A  75 F2                           jne 0x14064cb6e
0064CB7C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0064CB80  4C 8B F6                        mov r14, rsi
0064CB83  48 89 38                        mov qword ptr [rax], rdi
0064CB86  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0064CB8A  48 89 47 08                     mov qword ptr [rdi + 8], rax
0064CB8E  48 89 79 08                     mov qword ptr [rcx + 8], rdi
0064CB92  48 89 0F                        mov qword ptr [rdi], rcx
0064CB95  49 8B 12                        mov rdx, qword ptr [r10]
0064CB98  41 84 5A 08                     test byte ptr [r10 + 8], bl
0064CB9C  74 08                           je 0x14064cba6
0064CB9E  48 85 D2                        test rdx, rdx
0064CBA1  74 03                           je 0x14064cba6
0064CBA3  49 33 D2                        xor rdx, r10
0064CBA6  41 0F B6 4A 08                  movzx ecx, byte ptr [r10 + 8]
0064CBAB  45 32 C0                        xor r8b, r8b
0064CBAE  23 CB                           and ecx, ebx
0064CBB0  48 85 D2                        test rdx, rdx
0064CBB3  74 4D                           je 0x14064cc02
0064CBB5  4C 8B 47 30                     mov r8, qword ptr [rdi + 0x30]
0064CBB9  4C 3B 42 20                     cmp r8, qword ptr [rdx + 0x20]
0064CBBD  77 26                           ja 0x14064cbe5
0064CBBF  4C 3B 42 18                     cmp r8, qword ptr [rdx + 0x18]
0064CBC3  73 20                           jae 0x14064cbe5
0064CBC5  48 8B 02                        mov rax, qword ptr [rdx]
0064CBC8  85 C9                           test ecx, ecx
0064CBCA  74 08                           je 0x14064cbd4
0064CBCC  48 85 C0                        test rax, rax
0064CBCF  74 08                           je 0x14064cbd9
0064CBD1  48 33 C2                        xor rax, rdx
0064CBD4  48 85 C0                        test rax, rax
0064CBD7  75 21                           jne 0x14064cbfa
0064CBD9  45 32 C0                        xor r8b, r8b
0064CBDC  EB 24                           jmp 0x14064cc02
0064CBDE  B9 03 00 00 00                  mov ecx, 3
0064CBE3  CD 29                           int 0x29
0064CBE5  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0064CBE9  85 C9                           test ecx, ecx
0064CBEB  74 08                           je 0x14064cbf5
0064CBED  48 85 C0                        test rax, rax
0064CBF0  74 0D                           je 0x14064cbff
0064CBF2  48 33 C2                        xor rax, rdx
0064CBF5  48 85 C0                        test rax, rax
0064CBF8  74 05                           je 0x14064cbff
0064CBFA  48 8B D0                        mov rdx, rax
0064CBFD  EB BA                           jmp 0x14064cbb9
0064CBFF  44 8A C3                        mov r8b, bl
0064CC02  4C 8D 4F 18                     lea r9, [rdi + 0x18]
0064CC06  49 8B CA                        mov rcx, r10
0064CC09  E8 62 79 C9 FF                  call 0x1402e4570
0064CC0E  4D 85 FF                        test r15, r15
0064CC11  75 74                           jne 0x14064cc87
0064CC13  48 8D 4D 18                     lea rcx, [rbp + 0x18]
0064CC17  48 8B 11                        mov rdx, qword ptr [rcx]
0064CC1A  84 59 08                        test byte ptr [rcx + 8], bl
0064CC1D  74 08                           je 0x14064cc27
0064CC1F  48 85 D2                        test rdx, rdx
0064CC22  74 03                           je 0x14064cc27
0064CC24  48 33 D1                        xor rdx, rcx
0064CC27  44 0F B6 49 08                  movzx r9d, byte ptr [rcx + 8]
0064CC2C  45 32 C0                        xor r8b, r8b
0064CC2F  44 23 CB                        and r9d, ebx
0064CC32  48 85 D2                        test rdx, rdx
0064CC35  74 48                           je 0x14064cc7f
0064CC37  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
0064CC3B  4C 3B 42 20                     cmp r8, qword ptr [rdx + 0x20]
0064CC3F  77 20                           ja 0x14064cc61
0064CC41  4C 3B 42 18                     cmp r8, qword ptr [rdx + 0x18]
0064CC45  73 1A                           jae 0x14064cc61
0064CC47  48 8B 02                        mov rax, qword ptr [rdx]
0064CC4A  45 85 C9                        test r9d, r9d
0064CC4D  74 08                           je 0x14064cc57
0064CC4F  48 85 C0                        test rax, rax
0064CC52  74 08                           je 0x14064cc5c
0064CC54  48 33 C2                        xor rax, rdx
0064CC57  48 85 C0                        test rax, rax
0064CC5A  75 1B                           jne 0x14064cc77
0064CC5C  45 32 C0                        xor r8b, r8b
0064CC5F  EB 1E                           jmp 0x14064cc7f
0064CC61  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0064CC65  45 85 C9                        test r9d, r9d
0064CC68  74 08                           je 0x14064cc72
0064CC6A  48 85 C0                        test rax, rax
0064CC6D  74 0D                           je 0x14064cc7c
0064CC6F  48 33 C2                        xor rax, rdx
0064CC72  48 85 C0                        test rax, rax
0064CC75  74 05                           je 0x14064cc7c
0064CC77  48 8B D0                        mov rdx, rax
0064CC7A  EB BF                           jmp 0x14064cc3b
0064CC7C  44 8A C3                        mov r8b, bl
0064CC7F  4C 8B CE                        mov r9, rsi
0064CC82  E8 E9 78 C9 FF                  call 0x1402e4570
0064CC87  33 DB                           xor ebx, ebx
0064CC89  49 83 FC FF                     cmp r12, -1
0064CC8D  74 0B                           je 0x14064cc9a
0064CC8F  49 8B D4                        mov rdx, r12
0064CC92  48 8B CD                        mov rcx, rbp
0064CC95  E8 2E C8 E3 FF                  call 0x1404894c8
0064CC9A  4D 85 F6                        test r14, r14
0064CC9D  74 08                           je 0x14064cca7
0064CC9F  49 8B CE                        mov rcx, r14
0064CCA2  E8 9D 8A 42 00                  call 0x140a75744
0064CCA7  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0064CCAC  8B C3                           mov eax, ebx
0064CCAE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0064CCB3  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0064CCB8  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0064CCBD  48 83 C4 20                     add rsp, 0x20
0064CCC1  41 5F                           pop r15
0064CCC3  41 5E                           pop r14
0064CCC5  41 5C                           pop r12
0064CCC7  C3                              ret
0064CCC8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpInsertMemoryRange(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    v_r14 = 0;
    v_r15 = 0;
    result = VmpProcessContextLockExclusive(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 104)) != -1) goto loc_0064CA6B;
    *(unsigned __int64 *)(a1 + 104) = a3;
loc_0064CA36:
    if (((*(unsigned __int8 *)(a1 + 8 + 8)) & (1)) == 0) goto loc_0064CA50;
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 8)) ^ (a1 + 8);
    }
    a2 = (unsigned int)((*(unsigned __int8 *)(a1 + 8 + 8)) & (1));
    if (a1 == 0) goto loc_0064CAAD;
loc_0064CA60:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 56)) >= (*(unsigned __int64 *)(a1 + 24))) goto loc_0064CA7A;
    goto loc_0064CA88;
loc_0064CA6B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 56)) == 1) goto loc_0064CA36;
    goto loc_0064CC89;
loc_0064CA7A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 48)) <= (*(unsigned __int64 *)(a1 + 32))) goto loc_0064CA9E;
loc_0064CA88:
    if ((unsigned int)(a2) == 0) goto loc_0064CA96;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_0064CA96;
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 8));
    goto loc_0064CA99;
loc_0064CA96:
loc_0064CA99:
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_0064CA60;
loc_0064CA9E:
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_0064CAAD;
loc_0064CAA3:
    goto loc_0064CC89;
loc_0064CAAD:
    if (((*(unsigned __int8 *)(a1 + 24 + 8)) & ((unsigned __int8)((unsigned int)(0xC0000018ULL)))) == 0) goto loc_0064CAC1;
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        a2 = (*(unsigned __int64 *)(a1 + 24)) ^ (a1 + 24);
    }
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 24 + 8)) & ((unsigned int)((unsigned int)(0xC0000018ULL))));
    if (a2 == 0) goto loc_0064CB95;
loc_0064CAD6:
    if ((*(unsigned __int64 *)(a2 + 32)) >= (*(unsigned __int64 *)(a2 + 24))) goto loc_0064CAE1;
    goto loc_0064CAEF;
loc_0064CAE1:
    if ((*(unsigned __int64 *)(a2 + 24)) <= (*(unsigned __int64 *)(a2 + 32))) goto loc_0064CB06;
loc_0064CAEF:
    if ((unsigned int)(a3) == 0) goto loc_0064CAFE;
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_0064CAFE;
    a2 = (a2) ^ (*(unsigned __int64 *)(a2 + 8));
    goto loc_0064CB01;
loc_0064CAFE:
loc_0064CB01:
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_0064CAD6;
loc_0064CB06:
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_0064CB95;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 24)) != (*(unsigned __int64 *)(a2 + 24))) goto loc_0064CAA3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32)) != (*(unsigned __int64 *)(a2 + 32))) goto loc_0064CAA3;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 72))) ^ (*(unsigned int *)(a2 + 72)));
    if ((((unsigned __int8)(a1)) & (2)) != 0) goto loc_0064CAA3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40)) + 8)) != (*(unsigned __int64 *)(a2 + 40))) goto loc_0064CBDE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 8))) != (*(unsigned __int64 *)(a2 + 40))) goto loc_0064CBDE;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 16) = *(unsigned __int64 *)(a2 + 8);
    a2 = (*(unsigned __int64 *)(a2 + 8)) + (40);
    if ((*(unsigned __int64 *)(a2)) == a2) goto loc_0064CB7C;
loc_0064CB6E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 48)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 48))) goto loc_0064CB7C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) != a2) goto loc_0064CB6E;
loc_0064CB7C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8)) = *(unsigned __int64 *)(a2 + 40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8) = *(unsigned __int64 *)(a2 + 40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2));
loc_0064CB95:
    if (((*(unsigned __int8 *)(a1 + 8 + 8)) & ((unsigned __int8)((unsigned int)(0xC0000018ULL)))) == 0) goto loc_0064CBA6;
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a2 = (*(unsigned __int64 *)(a1 + 8)) ^ (a1 + 8);
    }
    a3 = 0;
    a1 = (unsigned int)((*(unsigned __int8 *)(a1 + 8 + 8)) & ((unsigned int)((unsigned int)(0xC0000018ULL))));
    if (a2 == 0) goto loc_0064CC02;
loc_0064CBB9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 48)) > (*(unsigned __int64 *)(a2 + 32))) goto loc_0064CBE5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40) + 48)) >= (*(unsigned __int64 *)(a2 + 24))) goto loc_0064CBE5;
    if ((unsigned int)(a1) == 0) goto loc_0064CBD4;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0064CBD9;
    result = (*(unsigned __int64 *)(a2)) ^ (a2);
loc_0064CBD4:
    if (result != 0) goto loc_0064CBFA;
loc_0064CBD9:
    a3 = 0;
    goto loc_0064CC02;
loc_0064CBDE:
loc_0064CBE5:
    if (3 == 0) goto loc_0064CBF5;
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_0064CBFF;
    result = (*(unsigned __int64 *)(a2 + 8)) ^ (a2);
loc_0064CBF5:
    if (result == 0) goto loc_0064CBFF;
loc_0064CBFA:
    goto loc_0064CBB9;
loc_0064CBFF:
loc_0064CC02:
    result = RtlRbInsertNodeEx(a1 + 8, result, (unsigned __int8)((unsigned int)(0xC0000018ULL)), *(unsigned __int64 *)(a2 + 40) + 24);
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_0064CC87;
    if (((*(unsigned __int8 *)(a1 + 24 + 8)) & ((unsigned __int8)((unsigned int)(0xC0000018ULL)))) == 0) goto loc_0064CC27;
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        a2 = (*(unsigned __int64 *)(a1 + 24)) ^ (a1 + 24);
    }
    a3 = 0;
    a4 = (unsigned int)((*(unsigned __int8 *)(a1 + 24 + 8)) & ((unsigned int)((unsigned int)(0xC0000018ULL))));
    if (a2 == 0) goto loc_0064CC7F;
loc_0064CC3B:
    if ((*(unsigned __int64 *)(a2 + 24)) > (*(unsigned __int64 *)(a2 + 32))) goto loc_0064CC61;
    if ((*(unsigned __int64 *)(a2 + 24)) >= (*(unsigned __int64 *)(a2 + 24))) goto loc_0064CC61;
    if ((unsigned int)(a4) == 0) goto loc_0064CC57;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0064CC5C;
    result = (*(unsigned __int64 *)(a2)) ^ (a2);
loc_0064CC57:
    if (result != 0) goto loc_0064CC77;
loc_0064CC5C:
    a3 = 0;
    goto loc_0064CC7F;
loc_0064CC61:
    if ((unsigned int)(a4) == 0) goto loc_0064CC72;
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_0064CC7C;
    result = (*(unsigned __int64 *)(a2 + 8)) ^ (a2);
loc_0064CC72:
    if (result == 0) goto loc_0064CC7C;
loc_0064CC77:
    goto loc_0064CC3B;
loc_0064CC7C:
loc_0064CC7F:
    result = RtlRbInsertNodeEx(a1 + 24, result, (unsigned __int8)((unsigned int)(0xC0000018ULL)), a2);
loc_0064CC87:
    v_rbx = 0;
loc_0064CC89:
    if (result != -1) {
        a2 = result;
        a1 = a1;
        result = VmpProcessContextUnlockExclusive(a1, a2, (unsigned __int8)((unsigned int)(0xC0000018ULL)), a2);
    }
    if (a2 != 0) {
        a1 = a2;
        result = VmpFreeMemoryRanges(a1, a2, (unsigned __int8)((unsigned int)(0xC0000018ULL)), a2);
    }
    v_rsp = (v_rsp) + (32);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t VmpInsertMemoryRange(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    local_r14 = 0;
    local_r15 = 0;
    result = VmpProcessContextLockExclusive(Arg1, Arg2, Arg3, a4);
    if ((*(uint64_t *)(arg1 + 0x68)) != -1) goto loc_0064CA6B;
    *(uint64_t *)(arg1 + 0x68) = Arg3;
loc_0064CA36:
    if (((*(uint8_t *)(arg1 + 0x8 + 0x8)) & (1)) == 0) goto loc_0064CA50;
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x8)) ^ (Arg1 + 8);
    }
    Arg2 = (uint32_t)((*(uint8_t *)(arg1 + 0x8 + 0x8)) & (1));
    if (Arg1 == NULL) goto loc_0064CAAD;
loc_0064CA60:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x38)) >= (*(uint64_t *)(arg1 + 0x18))) goto loc_0064CA7A;
    goto loc_0064CA88;
loc_0064CA6B:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x38)) == 1) goto loc_0064CA36;
    goto loc_0064CC89;
loc_0064CA7A:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x30)) <= (*(uint64_t *)(arg1 + 0x20))) goto loc_0064CA9E;
loc_0064CA88:
    if ((uint32_t)(Arg2) == 0) goto loc_0064CA96;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_0064CA96;
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x8));
    goto loc_0064CA99;
loc_0064CA96:
loc_0064CA99:
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_0064CA60;
loc_0064CA9E:
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_0064CAAD;
loc_0064CAA3:
    goto loc_0064CC89;
loc_0064CAAD:
    if (((*(uint8_t *)(arg1 + 0x18 + 0x8)) & ((uint8_t)((uint32_t)(0xC0000018ULL)))) == 0) goto loc_0064CAC1;
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        Arg2 = (*(uint64_t *)(arg1 + 0x18)) ^ (Arg1 + 24);
    }
    Arg3 = (uint32_t)((*(uint8_t *)(arg1 + 0x18 + 0x8)) & ((uint32_t)((uint32_t)(0xC0000018ULL))));
    if (Arg2 == NULL) goto loc_0064CB95;
loc_0064CAD6:
    if ((*(uint64_t *)(arg2 + 0x20)) >= (*(uint64_t *)(arg2 + 0x18))) goto loc_0064CAE1;
    goto loc_0064CAEF;
loc_0064CAE1:
    if ((*(uint64_t *)(arg2 + 0x18)) <= (*(uint64_t *)(arg2 + 0x20))) goto loc_0064CB06;
loc_0064CAEF:
    if ((uint32_t)(Arg3) == 0) goto loc_0064CAFE;
    if (*(uint64_t *)(arg2 + 0x8) == 0) goto loc_0064CAFE;
    Arg2 = (Arg2) ^ (*(uint64_t *)(arg2 + 0x8));
    goto loc_0064CB01;
loc_0064CAFE:
loc_0064CB01:
    if (*(uint64_t *)(arg2 + 0x8) != 0) goto loc_0064CAD6;
loc_0064CB06:
    if (*(uint64_t *)(arg2 + 0x8) == 0) goto loc_0064CB95;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x18)) != (*(uint64_t *)(arg2 + 0x18))) goto loc_0064CAA3;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20)) != (*(uint64_t *)(arg2 + 0x20))) goto loc_0064CAA3;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x48))) ^ (*(uint32_t *)(arg2 + 0x48)));
    if ((((uint8_t)(Arg1)) & (2)) != 0) goto loc_0064CAA3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x28)) + 0x8)) != (*(uint64_t *)(arg2 + 0x28))) goto loc_0064CBDE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x8))) != (*(uint64_t *)(arg2 + 0x28))) goto loc_0064CBDE;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x28));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x28)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x10) = *(uint64_t *)(arg2 + 0x8);
    Arg2 = (*(uint64_t *)(arg2 + 0x8)) + (40);
    if ((*(uint64_t *)(arg2)) == Arg2) goto loc_0064CB7C;
loc_0064CB6E:
    if ((*(uint64_t *)(*(uint64_t *)(arg2) + 0x30)) > (*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x30))) goto loc_0064CB7C;
    if ((*(uint64_t *)(*(uint64_t *)(arg2))) != Arg2) goto loc_0064CB6E;
loc_0064CB7C:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2)) + 0x8)) = *(uint64_t *)(arg2 + 0x28);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2)) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2)) + 0x8) = *(uint64_t *)(arg2 + 0x28);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x28)) = *(uint64_t *)(*(uint64_t *)(arg2));
loc_0064CB95:
    if (((*(uint8_t *)(arg1 + 0x8 + 0x8)) & ((uint8_t)((uint32_t)(0xC0000018ULL)))) == 0) goto loc_0064CBA6;
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        Arg2 = (*(uint64_t *)(arg1 + 0x8)) ^ (Arg1 + 8);
    }
    Arg3 = 0;
    Arg1 = (uint32_t)((*(uint8_t *)(arg1 + 0x8 + 0x8)) & ((uint32_t)((uint32_t)(0xC0000018ULL))));
    if (Arg2 == NULL) goto loc_0064CC02;
loc_0064CBB9:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x30)) > (*(uint64_t *)(arg2 + 0x20))) goto loc_0064CBE5;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x28) + 0x30)) >= (*(uint64_t *)(arg2 + 0x18))) goto loc_0064CBE5;
    if ((uint32_t)(Arg1) == 0) goto loc_0064CBD4;
    if (*(uint64_t *)(arg2) == 0) goto loc_0064CBD9;
    result = (*(uint64_t *)(arg2)) ^ (Arg2);
loc_0064CBD4:
    if (result != 0) goto loc_0064CBFA;
loc_0064CBD9:
    Arg3 = 0;
    goto loc_0064CC02;
loc_0064CBDE:
loc_0064CBE5:
    if (3 == 0) goto loc_0064CBF5;
    if (*(uint64_t *)(arg2 + 0x8) == 0) goto loc_0064CBFF;
    result = (*(uint64_t *)(arg2 + 0x8)) ^ (Arg2);
loc_0064CBF5:
    if (result == 0) goto loc_0064CBFF;
loc_0064CBFA:
    goto loc_0064CBB9;
loc_0064CBFF:
loc_0064CC02:
    result = RtlRbInsertNodeEx(Arg1 + 8, result, (uint8_t)((uint32_t)(0xC0000018ULL)), *(uint64_t *)(arg2 + 0x28) + 24);
    if (*(uint64_t *)(arg2 + 0x8) != 0) goto loc_0064CC87;
    if (((*(uint8_t *)(arg1 + 0x18 + 0x8)) & ((uint8_t)((uint32_t)(0xC0000018ULL)))) == 0) goto loc_0064CC27;
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        Arg2 = (*(uint64_t *)(arg1 + 0x18)) ^ (Arg1 + 24);
    }
    Arg3 = 0;
    a4 = (uint32_t)((*(uint8_t *)(arg1 + 0x18 + 0x8)) & ((uint32_t)((uint32_t)(0xC0000018ULL))));
    if (Arg2 == NULL) goto loc_0064CC7F;
loc_0064CC3B:
    if ((*(uint64_t *)(arg2 + 0x18)) > (*(uint64_t *)(arg2 + 0x20))) goto loc_0064CC61;
    if ((*(uint64_t *)(arg2 + 0x18)) >= (*(uint64_t *)(arg2 + 0x18))) goto loc_0064CC61;
    if ((uint32_t)(a4) == 0) goto loc_0064CC57;
    if (*(uint64_t *)(arg2) == 0) goto loc_0064CC5C;
    result = (*(uint64_t *)(arg2)) ^ (Arg2);
loc_0064CC57:
    if (result != 0) goto loc_0064CC77;
loc_0064CC5C:
    Arg3 = 0;
    goto loc_0064CC7F;
loc_0064CC61:
    if ((uint32_t)(a4) == 0) goto loc_0064CC72;
    if (*(uint64_t *)(arg2 + 0x8) == 0) goto loc_0064CC7C;
    result = (*(uint64_t *)(arg2 + 0x8)) ^ (Arg2);
loc_0064CC72:
    if (result == 0) goto loc_0064CC7C;
loc_0064CC77:
    goto loc_0064CC3B;
loc_0064CC7C:
loc_0064CC7F:
    result = RtlRbInsertNodeEx(Arg1 + 24, result, (uint8_t)((uint32_t)(0xC0000018ULL)), Arg2);
loc_0064CC87:
    local_rbx = 0;
loc_0064CC89:
    if (result != -1) {
        Arg2 = result;
        Arg1 = Arg1;
        result = VmpProcessContextUnlockExclusive(Arg1, Arg2, (uint8_t)((uint32_t)(0xC0000018ULL)), Arg2);
    }
    if (Arg2 != NULL) {
        Arg1 = Arg2;
        result = VmpFreeMemoryRanges(Arg1, Arg2, (uint8_t)((uint32_t)(0xC0000018ULL)), Arg2);
    }
    local_rsp = (local_rsp) + (32);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x48` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064C9F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
