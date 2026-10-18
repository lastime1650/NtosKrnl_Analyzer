# CmpFindNameInListWithStatus

- RVA: `0x00846B80`–`0x00846EB9` (길이 `825` bytes)
- VA: `0x0000000140846B80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069278`
- 디코드: `237`개 명령, `825/825` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00846BBF` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00846BDC` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00846BF5` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00846C2F` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00846C4F` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00846C7D` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00846D43` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00846D61` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00846D70` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00846D7A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00846DD0` → [CmpCompareTwoCompressedNames](CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x00846DF7` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00846DFE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00846E8D` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00846E9F` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00846EAF` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- [CmpMergeKeyValues](../7F/CmpMergeKeyValues_function_007F2304.md) at `0x007F2449`
- [CmpFindValueByName](CmpFindValueByName_function_00844E1C.md) at `0x00844E3C`
- [CmpFindNameInList](CmpFindNameInList_function_00844E54.md) at `0x00844E6C`
- [CmSetValueKey](CmSetValueKey_function_008457C0.md) at `0x00845D64`
- [CmSetValueKey](CmSetValueKey_function_008457C0.md) at `0x0084625B`
- [CmpCompareNewValueDataAgainstKCBCache](CmpCompareNewValueDataAgainstKCBCache_function_00846920.md) at `0x00846985`
- [CmQueryMultipleValueKey](CmQueryMultipleValueKey_function_00846EC0.md) at `0x008470E3`
- [CmDeleteValueKey](CmDeleteValueKey_function_008476E8.md) at `0x00847929`
- [CmDeleteValueKey](CmDeleteValueKey_function_008476E8.md) at `0x00847EE0`
- [CmpGetSymbolicLinkTarget](../85/CmpGetSymbolicLinkTarget_function_008570A0.md) at `0x00857731`
- [sub_00857A33](../85/Unknown_function_00857A33.md) at `0x00857BA0`
- [CmpLightWeightPrepareSetValueKeyUoW](../A0/CmpLightWeightPrepareSetValueKeyUoW_function_00A0EF28.md) at `0x00A0F312`
- [CmpLightWeightPrepareDeleteValueKeyUoW](../A0/CmpLightWeightPrepareDeleteValueKeyUoW_function_00A0F3D8.md) at `0x00A0F4D8`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7D85F`
- [CmQueryMultipleValueForLayeredKey](../A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) at `0x00A8E208`
- [sub_00B16BE8](../B1/Unknown_function_00B16BE8.md) at `0x00B16C0B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00846B80  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00846B85  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00846B8A  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00846B8F  55                              push rbp
00846B90  56                              push rsi
00846B91  57                              push rdi
00846B92  41 54                           push r12
00846B94  41 55                           push r13
00846B96  41 56                           push r14
00846B98  41 57                           push r15
00846B9A  48 8B EC                        mov rbp, rsp
00846B9D  48 83 EC 50                     sub rsp, 0x50
00846BA1  45 33 F6                        xor r14d, r14d
00846BA4  48 8B F9                        mov rdi, rcx
00846BA7  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00846BAB  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
00846BAF  45 8B FE                        mov r15d, r14d
00846BB2  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
00846BB6  45 8B E1                        mov r12d, r9d
00846BB9  49 8B F0                        mov rsi, r8
00846BBC  48 8B DA                        mov rbx, rdx
00846BBF  E8 4C F3 00 00                  call 0x140855f10
00846BC4  44 39 32                        cmp dword ptr [rdx], r14d
00846BC7  74 1F                           je 0x140846be8
00846BC9  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00846BD0  4C 8D 45 F0                     lea r8, [rbp - 0x10]
00846BD4  8B 52 04                        mov edx, dword ptr [rdx + 4]
00846BD7  48 8B CF                        mov rcx, rdi
00846BDA  74 73                           je 0x140846c4f
00846BDC  E8 7F E0 00 00                  call 0x140854c60
00846BE1  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00846BE5  4C 8B F8                        mov r15, rax
00846BE8  8B 13                           mov edx, dword ptr [rbx]
00846BEA  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00846BEE  89 55 48                        mov dword ptr [rbp + 0x48], edx
00846BF1  4C 89 75 E8                     mov qword ptr [rbp - 0x18], r14
00846BF5  E8 16 F3 00 00                  call 0x140855f10
00846BFA  85 D2                           test edx, edx
00846BFC  75 58                           jne 0x140846c56
00846BFE  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00846C02  BB 34 00 00 C0                  mov ebx, 0xc0000034
00846C07  83 08 FF                        or dword ptr [rax], 0xffffffff
00846C0A  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00846C0E  48 85 C0                        test rax, rax
00846C11  74 03                           je 0x140846c16
00846C13  44 89 30                        mov dword ptr [rax], r14d
00846C16  4D 85 FF                        test r15, r15
00846C19  74 19                           je 0x140846c34
00846C1B  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00846C22  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00846C26  48 8B CF                        mov rcx, rdi
00846C29  0F 85 CF 01 00 00               jne 0x140846dfe
00846C2F  E8 0C F3 00 00                  call 0x140855f40
00846C34  8B C3                           mov eax, ebx
00846C36  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00846C3E  48 83 C4 50                     add rsp, 0x50
00846C42  41 5F                           pop r15
00846C44  41 5E                           pop r14
00846C46  41 5D                           pop r13
00846C48  41 5C                           pop r12
00846C4A  5F                              pop rdi
00846C4B  5E                              pop rsi
00846C4C  5D                              pop rbp
00846C4D  C3                              ret
00846C4E  CC                              int3
00846C4F  E8 5C E0 00 00                  call 0x140854cb0
00846C54  EB 8B                           jmp 0x140846be1
00846C56  45 8B EE                        mov r13d, r14d
00846C59  44 3B EA                        cmp r13d, edx
00846C5C  0F 83 44 01 00 00               jae 0x140846da6
00846C62  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00846C69  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00846C6D  41 8B C5                        mov eax, r13d
00846C70  48 8B CF                        mov rcx, rdi
00846C73  41 8B 14 87                     mov edx, dword ptr [r15 + rax*4]
00846C77  0F 84 F3 00 00 00               je 0x140846d70
00846C7D  E8 DE DF 00 00                  call 0x140854c60
00846C82  44 0F B7 70 02                  movzx r14d, word ptr [rax + 2]
00846C87  4C 8D 40 14                     lea r8, [rax + 0x14]
00846C8B  41 8B CC                        mov ecx, r12d
00846C8E  81 E1 00 00 01 00               and ecx, 0x10000
00846C94  F6 40 10 01                     test byte ptr [rax + 0x10], 1
00846C98  0F 84 3E 01 00 00               je 0x140846ddc
00846C9E  33 C0                           xor eax, eax
00846CA0  85 C9                           test ecx, ecx
00846CA2  0F 85 1E 01 00 00               jne 0x140846dc6
00846CA8  44 0F B7 3E                     movzx r15d, word ptr [rsi]
00846CAC  4C 8B 66 08                     mov r12, qword ptr [rsi + 8]
00846CB0  66 41 D1 EF                     shr r15w, 1
00846CB4  66 45 85 FF                     test r15w, r15w
00846CB8  74 67                           je 0x140846d21
00846CBA  66 45 85 F6                     test r14w, r14w
00846CBE  74 61                           je 0x140846d21
00846CC0  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
00846CC5  49 83 C4 02                     add r12, 2
00846CC9  41 0F B6 30                     movzx esi, byte ptr [r8]
00846CCD  49 FF C0                        inc r8
00846CD0  4C 89 45 F8                     mov qword ptr [rbp - 8], r8
00846CD4  66 3B DE                        cmp bx, si
00846CD7  74 39                           je 0x140846d12
00846CD9  66 83 FB 61                     cmp bx, 0x61
00846CDD  0F 82 86 00 00 00               jb 0x140846d69
00846CE3  66 83 FB 7A                     cmp bx, 0x7a
00846CE7  77 75                           ja 0x140846d5e
00846CE9  B8 E0 FF 00 00                  mov eax, 0xffe0
00846CEE  66 03 D8                        add bx, ax
00846CF1  83 FE 61                        cmp esi, 0x61
00846CF4  72 0C                           jb 0x140846d02
00846CF6  83 FE 7A                        cmp esi, 0x7a
00846CF9  0F 87 9D 01 00 00               ja 0x140846e9c
00846CFF  66 03 F0                        add si, ax
00846D02  0F B7 C6                        movzx eax, si
00846D05  0F B7 DB                        movzx ebx, bx
00846D08  2B D8                           sub ebx, eax
00846D0A  75 1F                           jne 0x140846d2b
00846D0C  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
00846D10  33 C0                           xor eax, eax
00846D12  BB FF FF 00 00                  mov ebx, 0xffff
00846D17  66 44 03 FB                     add r15w, bx
00846D1B  66 44 03 F3                     add r14w, bx
00846D1F  EB 93                           jmp 0x140846cb4
00846D21  41 0F B7 C6                     movzx eax, r14w
00846D25  41 0F B7 DF                     movzx ebx, r15w
00846D29  2B D8                           sub ebx, eax
00846D2B  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
00846D2F  44 8B 65 58                     mov r12d, dword ptr [rbp + 0x58]
00846D33  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00846D3A  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00846D3E  48 8B CF                        mov rcx, rdi
00846D41  75 37                           jne 0x140846d7a
00846D43  E8 F8 F1 00 00                  call 0x140855f40
00846D48  45 33 F6                        xor r14d, r14d
00846D4B  85 DB                           test ebx, ebx
00846D4D  74 32                           je 0x140846d81
00846D4F  8B 55 48                        mov edx, dword ptr [rbp + 0x48]
00846D52  41 FF C5                        inc r13d
00846D55  48 8B 75 50                     mov rsi, qword ptr [rbp + 0x50]
00846D59  E9 FB FE FF FF                  jmp 0x140846c59
00846D5E  0F B7 CB                        movzx ecx, bx
00846D61  E8 8A 83 01 00                  call 0x14085f0f0
00846D66  0F B7 D8                        movzx ebx, ax
00846D69  B8 E0 FF 00 00                  mov eax, 0xffe0
00846D6E  EB 81                           jmp 0x140846cf1
00846D70  E8 3B DF 00 00                  call 0x140854cb0
00846D75  E9 08 FF FF FF                  jmp 0x140846c82
00846D7A  E8 A1 5E 01 00                  call 0x14085cc20
00846D7F  EB C7                           jmp 0x140846d48
00846D81  41 8B C5                        mov eax, r13d
00846D84  41 8B DE                        mov ebx, r14d
00846D87  41 8B 0C 87                     mov ecx, dword ptr [r15 + rax*4]
00846D8B  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00846D8F  89 08                           mov dword ptr [rax], ecx
00846D91  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00846D95  48 85 C0                        test rax, rax
00846D98  0F 84 78 FE FF FF               je 0x140846c16
00846D9E  44 89 28                        mov dword ptr [rax], r13d
00846DA1  E9 70 FE FF FF                  jmp 0x140846c16
00846DA6  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00846DAA  BB 34 00 00 C0                  mov ebx, 0xc0000034
00846DAF  83 08 FF                        or dword ptr [rax], 0xffffffff
00846DB2  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00846DB6  48 85 C0                        test rax, rax
00846DB9  0F 84 57 FE FF FF               je 0x140846c16
00846DBF  89 10                           mov dword ptr [rax], edx
00846DC1  E9 50 FE FF FF                  jmp 0x140846c16
00846DC6  0F B7 16                        movzx edx, word ptr [rsi]
00846DC9  45 8B CE                        mov r9d, r14d
00846DCC  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00846DD0  E8 3B 08 00 00                  call 0x140847610
00846DD5  8B D8                           mov ebx, eax
00846DD7  E9 57 FF FF FF                  jmp 0x140846d33
00846DDC  33 C0                           xor eax, eax
00846DDE  85 C9                           test ecx, ecx
00846DE0  75 26                           jne 0x140846e08
00846DE2  0F B7 16                        movzx edx, word ptr [rsi]
00846DE5  4D 8B CE                        mov r9, r14
00846DE8  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00846DEC  49 D1 E9                        shr r9, 1
00846DEF  48 D1 EA                        shr rdx, 1
00846DF2  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00846DF7  E8 E4 B9 12 00                  call 0x1409727e0
00846DFC  EB D7                           jmp 0x140846dd5
00846DFE  E8 1D 5E 01 00                  call 0x14085cc20
00846E03  E9 2C FE FF FF                  jmp 0x140846c34
00846E08  4C 8B 66 08                     mov r12, qword ptr [rsi + 8]
00846E0C  44 0F B7 3E                     movzx r15d, word ptr [rsi]
00846E10  66 41 D1 EE                     shr r14w, 1
00846E14  66 45 85 F6                     test r14w, r14w
00846E18  74 5F                           je 0x140846e79
00846E1A  66 45 85 FF                     test r15w, r15w
00846E1E  74 59                           je 0x140846e79
00846E20  41 0F B7 18                     movzx ebx, word ptr [r8]
00846E24  49 83 C0 02                     add r8, 2
00846E28  41 0F B6 34 24                  movzx esi, byte ptr [r12]
00846E2D  49 FF C4                        inc r12
00846E30  4C 89 45 F8                     mov qword ptr [rbp - 8], r8
00846E34  66 3B DE                        cmp bx, si
00846E37  74 31                           je 0x140846e6a
00846E39  66 83 FB 61                     cmp bx, 0x61
00846E3D  72 56                           jb 0x140846e95
00846E3F  66 83 FB 7A                     cmp bx, 0x7a
00846E43  77 45                           ja 0x140846e8a
00846E45  B8 E0 FF 00 00                  mov eax, 0xffe0
00846E4A  66 03 D8                        add bx, ax
00846E4D  83 FE 61                        cmp esi, 0x61
00846E50  72 08                           jb 0x140846e5a
00846E52  83 FE 7A                        cmp esi, 0x7a
00846E55  77 55                           ja 0x140846eac
00846E57  66 03 F0                        add si, ax
00846E5A  0F B7 C6                        movzx eax, si
00846E5D  0F B7 DB                        movzx ebx, bx
00846E60  2B D8                           sub ebx, eax
00846E62  75 1F                           jne 0x140846e83
00846E64  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
00846E68  33 C0                           xor eax, eax
00846E6A  BB FF FF 00 00                  mov ebx, 0xffff
00846E6F  66 44 03 F3                     add r14w, bx
00846E73  66 44 03 FB                     add r15w, bx
00846E77  EB 9B                           jmp 0x140846e14
00846E79  41 0F B7 C7                     movzx eax, r15w
00846E7D  41 0F B7 DE                     movzx ebx, r14w
00846E81  2B D8                           sub ebx, eax
00846E83  F7 DB                           neg ebx
00846E85  E9 A1 FE FF FF                  jmp 0x140846d2b
00846E8A  0F B7 CB                        movzx ecx, bx
00846E8D  E8 5E 82 01 00                  call 0x14085f0f0
00846E92  0F B7 D8                        movzx ebx, ax
00846E95  B8 E0 FF 00 00                  mov eax, 0xffe0
00846E9A  EB B1                           jmp 0x140846e4d
00846E9C  0F B7 CE                        movzx ecx, si
00846E9F  E8 4C 82 01 00                  call 0x14085f0f0
00846EA4  0F B7 F0                        movzx esi, ax
00846EA7  E9 56 FE FF FF                  jmp 0x140846d02
00846EAC  0F B7 CE                        movzx ecx, si
00846EAF  E8 3C 82 01 00                  call 0x14085f0f0
00846EB4  0F B7 F0                        movzx esi, ax
00846EB7  EB A1                           jmp 0x140846e5a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFindNameInListWithStatus(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    v_r14 = 0;
    v_stack_m48 = 0;
    v_stack_m58 = 0;
    result = HvpGetCellContextInitialize(v_stack_m48, a2, a3, a4);
    if ((*(unsigned int *)(a2)) == 0) goto loc_00846BE8;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00846C4F;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(a2 + 4)), v_stack_m48, a4);
loc_00846BE1:
    v_stack_m58 = result;
loc_00846BE8:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    v_stack_m50 = 0;
    result = HvpGetCellContextInitialize(v_stack_m50, (unsigned int)(*(unsigned int *)(a2)), v_stack_m48, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) != 0) goto loc_00846C56;
    if (a5 != 0) {
        *(unsigned int *)(a5) = 0;
    }
    if (result == 0) goto loc_00846C34;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00846DFE;
    result = HvpReleaseCellPaged(a1, v_stack_m48, v_stack_m48, a4);
loc_00846C34:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL)));
loc_00846C4F:
    result = HvpGetCellPaged(a1, v_stack_m48, v_stack_m48, a4);
    goto loc_00846BE1;
loc_00846C56:
loc_00846C59:
    if (0 >= ((unsigned int)(v_stack_m48))) goto loc_00846DA6;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00846D70;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + 0 * 4)), v_stack_m50, a4);
loc_00846C82:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0x10000ULL));
    if (((*(unsigned __int8 *)(result + 16)) & (1)) == 0) goto loc_00846DDC;
    result = 0;
    if ((unsigned int)(a1) != 0) goto loc_00846DC6;
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(a3)) >> (1));
loc_00846CB4:
    if ((unsigned __int16)(v_r15) == 0) goto loc_00846D21;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 2)) == 0) goto loc_00846D21;
    v_r12 = (*(unsigned __int64 *)(a3 + 8)) + (2);
    a3 = (result + 20) + 1;
    v_stack_m40 = a3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 20)))) goto loc_00846D12;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8)))) < 97) goto loc_00846D69;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8)))) > 122) goto loc_00846D5E;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00846CF1:
    if (((unsigned int)(*(unsigned __int8 *)(result + 20))) < 97) goto loc_00846D02;
    if (((unsigned int)(*(unsigned __int8 *)(result + 20))) > 122) goto loc_00846E9C;
    v_rsi = (unsigned __int16)((*(unsigned __int8 *)(result + 20)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00846D02:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rsi))));
    if (condition_is_not_equal) goto loc_00846D2B;
    result = 0;
loc_00846D12:
    v_r15 = (unsigned __int16)((v_r15) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(result + 2)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00846CB4;
loc_00846D21:
    v_rbx = (unsigned int)(((unsigned __int16)(v_r15)) - ((unsigned int)((unsigned __int16)(v_r14))));
loc_00846D2B:
loc_00846D33:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00846D7A;
    result = HvpReleaseCellPaged(a1, v_stack_m50, v_stack_m40, a4);
loc_00846D48:
    v_r14 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_00846D81;
    v_r13 = (unsigned int)((0) + 1);
    goto loc_00846C59;
loc_00846D5E:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rbx), (unsigned int)(v_stack_p10), v_stack_m40, a4);
loc_00846D69:
    goto loc_00846CF1;
loc_00846D70:
    result = HvpGetCellPaged((unsigned __int16)(v_rbx), (unsigned int)(v_stack_p10), v_stack_m40, a4);
    goto loc_00846C82;
loc_00846D7A:
    result = HvpReleaseCellFlat((unsigned __int16)(v_rbx), (unsigned int)(v_stack_p10), v_stack_m40, a4);
    goto loc_00846D48;
loc_00846D81:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + (unsigned int)((unsigned int)(v_r13)) * 4)));
    if (a5 == 0) goto loc_00846C16;
    *(unsigned int *)(a5) = (unsigned int)(v_r13);
    goto loc_00846C16;
loc_00846DA6:
    if (a5 == 0) goto loc_00846C16;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_p10));
    goto loc_00846C16;
loc_00846DC6:
    result = CmpCompareTwoCompressedNames(*(unsigned __int64 *)(v_stack_p18 + 8), *(unsigned __int16 *)(v_stack_p18), v_stack_m40, 0);
loc_00846DD5:
    goto loc_00846D33;
loc_00846DDC:
    result = 0;
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_p18 + 8)) != 0) goto loc_00846E08;
    a4 = (0) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_p18)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_p18 + 8), a2, v_stack_m40, a4);
    goto loc_00846DD5;
loc_00846DFE:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_stack_p18 + 8), a2, v_stack_m40, a4);
    goto loc_00846C34;
loc_00846E08:
    v_r14 = (unsigned __int16)((v_r14) >> (1));
loc_00846E14:
    if ((unsigned __int16)(v_r14) == 0) goto loc_00846E79;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p18)) == 0) goto loc_00846E79;
    a3 = (v_stack_m40) + (2);
    v_r12 = (*(unsigned __int64 *)(v_stack_p18 + 8)) + 1;
    v_stack_m40 = a3;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m40))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18 + 8))))) goto loc_00846E6A;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m40))) < 97) goto loc_00846E95;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m40))) > 122) goto loc_00846E8A;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m40)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00846E4D:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18 + 8)))) < 97) goto loc_00846E5A;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18 + 8)))) > 122) goto loc_00846EAC;
    v_rsi = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00846E5A:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rsi))));
    if (condition_is_not_equal) goto loc_00846E83;
    result = 0;
loc_00846E6A:
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p18)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00846E14;
loc_00846E79:
    v_rbx = (unsigned int)(((unsigned __int16)(v_r14)) - ((unsigned int)((unsigned __int16)(v_r15))));
loc_00846E83:
    v_rbx = (unsigned int)(-(v_rbx));
    goto loc_00846D2B;
loc_00846E8A:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rbx), a2, v_stack_m40, a4);
loc_00846E95:
    goto loc_00846E4D;
loc_00846E9C:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rsi), a2, v_stack_m40, a4);
    goto loc_00846D02;
loc_00846EAC:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), a2, v_stack_m40, a4);
    goto loc_00846E5A;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFindNameInListWithStatus(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    local_r14 = 0;
    v_stack_m48 = 0;
    v_stack_m58 = 0;
    result = HvpGetCellContextInitialize(v_stack_m48, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(arg2)) == 0) goto loc_00846BE8;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00846C4F;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x4)), v_stack_m48, Arg4);
loc_00846BE1:
    v_stack_m58 = result;
loc_00846BE8:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    v_stack_m50 = 0;
    result = HvpGetCellContextInitialize(v_stack_m50, (uint32_t)(*(uint32_t *)(arg2)), v_stack_m48, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))) != 0) goto loc_00846C56;
    if (Arg5 != 0) {
        *(uint32_t *)(Arg5) = 0;
    }
    if (result == 0) goto loc_00846C34;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00846DFE;
    result = HvpReleaseCellPaged(Arg1, v_stack_m48, v_stack_m48, Arg4);
loc_00846C34:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL)));
loc_00846C4F:
    result = HvpGetCellPaged(Arg1, v_stack_m48, v_stack_m48, Arg4);
    goto loc_00846BE1;
loc_00846C56:
loc_00846C59:
    if (0 >= ((uint32_t)(v_stack_m48))) goto loc_00846DA6;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00846D70;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + 0x0 * 4)), v_stack_m50, Arg4);
loc_00846C82:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0x10000ULL));
    if (((*(uint8_t *)(result + 0x10)) & (1)) == 0) goto loc_00846DDC;
    result = 0;
    if ((uint32_t)(Arg1) != 0) goto loc_00846DC6;
    local_r15 = (uint16_t)((*(uint16_t *)(Arg3)) >> (1));
loc_00846CB4:
    if ((uint16_t)(local_r15) == 0) goto loc_00846D21;
    if ((uint16_t)(*(uint16_t *)(result + 0x2)) == 0) goto loc_00846D21;
    local_r12 = (*(uint64_t *)(Arg3 + 0x8)) + (2);
    Arg3 = (result + 20) + 1;
    v_stack_m40 = Arg3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x14)))) goto loc_00846D12;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8)))) < 97) goto loc_00846D69;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8)))) > 122) goto loc_00846D5E;
    local_rbx = (uint16_t)((*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00846CF1:
    if (((uint32_t)(*(uint8_t *)(result + 0x14))) < 97) goto loc_00846D02;
    if (((uint32_t)(*(uint8_t *)(result + 0x14))) > 122) goto loc_00846E9C;
    local_rsi = (uint16_t)((*(uint8_t *)(result + 0x14)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00846D02:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rsi))));
    if (condition_is_not_equal) goto loc_00846D2B;
    result = 0;
loc_00846D12:
    local_r15 = (uint16_t)((local_r15) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(result + 0x2)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00846CB4;
loc_00846D21:
    local_rbx = (uint32_t)(((uint16_t)(local_r15)) - ((uint32_t)((uint16_t)(local_r14))));
loc_00846D2B:
loc_00846D33:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00846D7A;
    result = HvpReleaseCellPaged(Arg1, v_stack_m50, v_stack_m40, Arg4);
loc_00846D48:
    local_r14 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_00846D81;
    local_r13 = (uint32_t)((0) + 1);
    goto loc_00846C59;
loc_00846D5E:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rbx), (uint32_t)(v_stack_p10), v_stack_m40, Arg4);
loc_00846D69:
    goto loc_00846CF1;
loc_00846D70:
    result = HvpGetCellPaged((uint16_t)(local_rbx), (uint32_t)(v_stack_p10), v_stack_m40, Arg4);
    goto loc_00846C82;
loc_00846D7A:
    result = HvpReleaseCellFlat((uint16_t)(local_rbx), (uint32_t)(v_stack_p10), v_stack_m40, Arg4);
    goto loc_00846D48;
loc_00846D81:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + (uint32_t)((uint32_t)(local_r13)) * 4)));
    if (Arg5 == 0) goto loc_00846C16;
    *(uint32_t *)(Arg5) = (uint32_t)(local_r13);
    goto loc_00846C16;
loc_00846DA6:
    if (Arg5 == 0) goto loc_00846C16;
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(v_stack_p10));
    goto loc_00846C16;
loc_00846DC6:
    result = CmpCompareTwoCompressedNames(*(uint64_t *)(v_stack_p18 + 0x8), *(uint16_t *)(v_stack_p18), v_stack_m40, 0);
loc_00846DD5:
    goto loc_00846D33;
loc_00846DDC:
    result = 0;
    if ((uint32_t)(*(uint64_t *)(v_stack_p18 + 0x8)) != 0) goto loc_00846E08;
    Arg4 = (0) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_p18)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_p18 + 0x8), Arg2, v_stack_m40, Arg4);
    goto loc_00846DD5;
loc_00846DFE:
    result = HvpReleaseCellFlat(*(uint64_t *)(v_stack_p18 + 0x8), Arg2, v_stack_m40, Arg4);
    goto loc_00846C34;
loc_00846E08:
    local_r14 = (uint16_t)((local_r14) >> (1));
loc_00846E14:
    if ((uint16_t)(local_r14) == 0) goto loc_00846E79;
    if ((uint16_t)(*(uint16_t *)(v_stack_p18)) == 0) goto loc_00846E79;
    Arg3 = (v_stack_m40) + (2);
    local_r12 = (*(uint64_t *)(v_stack_p18 + 0x8)) + 1;
    v_stack_m40 = Arg3;
    if (((uint16_t)(*(uint16_t *)(v_stack_m40))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p18 + 0x8))))) goto loc_00846E6A;
    if (((uint16_t)(*(uint16_t *)(v_stack_m40))) < 97) goto loc_00846E95;
    if (((uint16_t)(*(uint16_t *)(v_stack_m40))) > 122) goto loc_00846E8A;
    local_rbx = (uint16_t)((*(uint16_t *)(v_stack_m40)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00846E4D:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p18 + 0x8)))) < 97) goto loc_00846E5A;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p18 + 0x8)))) > 122) goto loc_00846EAC;
    local_rsi = (uint16_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p18 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00846E5A:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rsi))));
    if (condition_is_not_equal) goto loc_00846E83;
    result = 0;
loc_00846E6A:
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r15 = (uint16_t)((*(uint16_t *)(v_stack_p18)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00846E14;
loc_00846E79:
    local_rbx = (uint32_t)(((uint16_t)(local_r14)) - ((uint32_t)((uint16_t)(local_r15))));
loc_00846E83:
    local_rbx = (uint32_t)(-(local_rbx));
    goto loc_00846D2B;
loc_00846E8A:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rbx), Arg2, v_stack_m40, Arg4);
loc_00846E95:
    goto loc_00846E4D;
loc_00846E9C:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rsi), Arg2, v_stack_m40, Arg4);
    goto loc_00846D02;
loc_00846EAC:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), Arg2, v_stack_m40, Arg4);
    goto loc_00846E5A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R/W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00846B80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
