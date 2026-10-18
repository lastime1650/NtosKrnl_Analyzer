# RtlpCreateSplitBlock

- RVA: `0x005E98F0`–`0x005EA008` (길이 `1,816` bytes)
- VA: `0x00000001405E98F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4294`
- 디코드: `504`개 명령, `1,816/1,816` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005E996A` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E99CC` → [RtlpAnalyzeHeapFailure](../5F/RtlpAnalyzeHeapFailure_function_005F0F9C.md) (function, `0x005F0F9C`)
- `0x005E9A03` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E9A65` → [RtlpHeapRemoveListEntry](../5F/RtlpHeapRemoveListEntry_function_005F1B90.md) (function, `0x005F1B90`)
- `0x005E9AAF` → [RtlCompareMemoryUlong](../6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x005E9ACA` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005E9B35` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005E9BB6` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E9C66` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005E9CE7` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E9D34` → [RtlpHeapAddListEntry](../5F/RtlpHeapAddListEntry_function_005F18C8.md) (function, `0x005F18C8`)
- `0x005E9D66` → [RtlpInsertFreeBlock](RtlpInsertFreeBlock_function_005EB4C0.md) (function, `0x005EB4C0`)
- `0x005E9DB3` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005E9E34` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E9EF9` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005E9F7A` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E9FC7` → [RtlpHeapAddListEntry](../5F/RtlpHeapAddListEntry_function_005F18C8.md) (function, `0x005F18C8`)

### Direct callers
- [RtlpAllocateHeap](RtlpAllocateHeap_function_005E8B1C.md) at `0x005E90B9`

### Static image references
- `0x005E9AC3` → RVA `0x006CC9E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005E9ACF` → RVA `0x00F475F8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E98F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005E98F5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
005E98FA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005E98FF  57                              push rdi
005E9900  41 54                           push r12
005E9902  41 55                           push r13
005E9904  41 56                           push r14
005E9906  41 57                           push r15
005E9908  48 83 EC 70                     sub rsp, 0x70
005E990C  0F B7 84 24 C8 00 00 00         movzx eax, word ptr [rsp + 0xc8]
005E9914  45 33 ED                        xor r13d, r13d
005E9917  45 88 68 0F                     mov byte ptr [r8 + 0xf], r13b
005E991B  48 8B F1                        mov rsi, rcx
005E991E  45 88 48 0A                     mov byte ptr [r8 + 0xa], r9b
005E9922  49 8B D8                        mov rbx, r8
005E9925  66 33 81 8C 00 00 00            xor ax, word ptr [rcx + 0x8c]
005E992C  66 41 89 40 0C                  mov word ptr [r8 + 0xc], ax
005E9931  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
005E9935  48 3B CA                        cmp rcx, rdx
005E9938  75 05                           jne 0x1405e993f
005E993A  40 32 FF                        xor dil, dil
005E993D  EB 30                           jmp 0x1405e996f
005E993F  48 8B FB                        mov rdi, rbx
005E9942  48 2B FA                        sub rdi, rdx
005E9945  48 C1 EF 10                     shr rdi, 0x10
005E9949  48 FF C7                        inc rdi
005E994C  48 81 FF FE 00 00 00            cmp rdi, 0xfe
005E9953  72 1A                           jb 0x1405e996f
005E9955  4C 21 6C 24 28                  and qword ptr [rsp + 0x28], r13
005E995A  4C 8B CA                        mov r9, rdx
005E995D  4C 21 6C 24 20                  and qword ptr [rsp + 0x20], r13
005E9962  48 8B D1                        mov rdx, rcx
005E9965  B9 03 00 00 00                  mov ecx, 3
005E996A  E8 4D 1E D7 FF                  call 0x14035b7bc
005E996F  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
005E9977  40 88 7B 0E                     mov byte ptr [rbx + 0xe], dil
005E997B  49 8B FF                        mov rdi, r15
005E997E  48 C1 E7 04                     shl rdi, 4
005E9982  45 0F B7 E7                     movzx r12d, r15w
005E9986  48 03 FB                        add rdi, rbx
005E9989  44 88 6B 0B                     mov byte ptr [rbx + 0xb], r13b
005E998D  66 44 89 63 08                  mov word ptr [rbx + 8], r12w
005E9992  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9995  8B C1                           mov eax, ecx
005E9997  C1 E8 14                        shr eax, 0x14
005E999A  22 86 8A 00 00 00               and al, byte ptr [rsi + 0x8a]
005E99A0  32 47 0A                        xor al, byte ptr [rdi + 0xa]
005E99A3  A8 01                           test al, 1
005E99A5  0F 85 CC 03 00 00               jne 0x1405e9d77
005E99AB  85 C9                           test ecx, ecx
005E99AD  74 22                           je 0x1405e99d1
005E99AF  8B 8E 88 00 00 00               mov ecx, dword ptr [rsi + 0x88]
005E99B5  31 4F 08                        xor dword ptr [rdi + 8], ecx
005E99B8  8A 4F 0A                        mov cl, byte ptr [rdi + 0xa]
005E99BB  32 4F 09                        xor cl, byte ptr [rdi + 9]
005E99BE  32 4F 08                        xor cl, byte ptr [rdi + 8]
005E99C1  38 4F 0B                        cmp byte ptr [rdi + 0xb], cl
005E99C4  74 0B                           je 0x1405e99d1
005E99C6  48 8B D7                        mov rdx, rdi
005E99C9  48 8B CE                        mov rcx, rsi
005E99CC  E8 CB 75 00 00                  call 0x1405f0f9c
005E99D1  4C 8B 77 18                     mov r14, qword ptr [rdi + 0x18]
005E99D5  4C 8D 57 10                     lea r10, [rdi + 0x10]
005E99D9  49 8B 2A                        mov rbp, qword ptr [r10]
005E99DC  49 8B 06                        mov rax, qword ptr [r14]
005E99DF  4C 8B 4D 08                     mov r9, qword ptr [rbp + 8]
005E99E3  49 3B C1                        cmp rax, r9
005E99E6  75 05                           jne 0x1405e99ed
005E99E8  49 3B C2                        cmp rax, r10
005E99EB  74 2F                           je 0x1405e9a1c
005E99ED  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E99F3  4D 8B C2                        mov r8, r10
005E99F6  48 8B D6                        mov rdx, rsi
005E99F9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005E99FE  B9 0D 00 00 00                  mov ecx, 0xd
005E9A03  E8 B4 1D D7 FF                  call 0x14035b7bc
005E9A08  45 85 ED                        test r13d, r13d
005E9A0B  0F 85 5F 03 00 00               jne 0x1405e9d70
005E9A11  41 BD 01 00 00 00               mov r13d, 1
005E9A17  E9 76 FF FF FF                  jmp 0x1405e9992
005E9A1C  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
005E9A20  48 29 86 C0 00 00 00            sub qword ptr [rsi + 0xc0], rax
005E9A27  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E9A2E  48 85 D2                        test rdx, rdx
005E9A31  74 37                           je 0x1405e9a6a
005E9A33  0F B7 4F 08                     movzx ecx, word ptr [rdi + 8]
005E9A37  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005E9A3B  49 3B C8                        cmp rcx, r8
005E9A3E  72 12                           jb 0x1405e9a52
005E9A40  48 8B 02                        mov rax, qword ptr [rdx]
005E9A43  48 85 C0                        test rax, rax
005E9A46  74 05                           je 0x1405e9a4d
005E9A48  48 8B D0                        mov rdx, rax
005E9A4B  EB EA                           jmp 0x1405e9a37
005E9A4D  41 FF C8                        dec r8d
005E9A50  EB 03                           jmp 0x1405e9a55
005E9A52  4C 8B C1                        mov r8, rcx
005E9A55  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
005E9A5A  4D 8B CA                        mov r9, r10
005E9A5D  48 8B CE                        mov rcx, rsi
005E9A60  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
005E9A65  E8 26 81 00 00                  call 0x1405f1b90
005E9A6A  44 8A A4 24 C0 00 00 00         mov r12b, byte ptr [rsp + 0xc0]
005E9A72  49 89 2E                        mov qword ptr [r14], rbp
005E9A75  4C 89 75 08                     mov qword ptr [rbp + 8], r14
005E9A79  41 BE EE FE EE FE               mov r14d, 0xfeeefeee
005E9A7F  45 84 E4                        test r12b, r12b
005E9A82  74 55                           je 0x1405e9ad9
005E9A84  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
005E9A87  A8 04                           test al, 4
005E9A89  74 4E                           je 0x1405e9ad9
005E9A8B  0F B7 6F 08                     movzx ebp, word ptr [rdi + 8]
005E9A8F  48 C1 E5 04                     shl rbp, 4
005E9A93  48 83 ED 20                     sub rbp, 0x20
005E9A97  A8 02                           test al, 2
005E9A99  74 0A                           je 0x1405e9aa5
005E9A9B  48 83 FD 04                     cmp rbp, 4
005E9A9F  76 04                           jbe 0x1405e9aa5
005E9AA1  48 83 ED 04                     sub rbp, 4
005E9AA5  48 8D 4F 20                     lea rcx, [rdi + 0x20]
005E9AA9  45 8B C6                        mov r8d, r14d
005E9AAC  48 8B D5                        mov rdx, rbp
005E9AAF  E8 3C 0C 0D 00                  call 0x1406ba6f0
005E9AB4  48 3B C5                        cmp rax, rbp
005E9AB7  74 20                           je 0x1405e9ad9
005E9AB9  4C 8D 47 20                     lea r8, [rdi + 0x20]
005E9ABD  48 8B D7                        mov rdx, rdi
005E9AC0  4C 03 C0                        add r8, rax
005E9AC3  48 8D 0D 16 2F 0E 00            lea rcx, [rip + 0xe2f16]
005E9ACA  E8 E1 F1 D6 FF                  call 0x140358cb0
005E9ACF  80 3D 22 DB 95 00 00            cmp byte ptr [rip + 0x95db22], 0
005E9AD6  74 01                           je 0x1405e9ad9
005E9AD8  CC                              int3
005E9AD9  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
005E9ADC  88 43 0A                        mov byte ptr [rbx + 0xa], al
005E9ADF  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
005E9AE3  4C 03 F8                        add r15, rax
005E9AE6  49 81 FF 00 FF 00 00            cmp r15, 0xff00
005E9AED  0F 87 6A 02 00 00               ja 0x1405e9d5d
005E9AF3  41 0F B7 EF                     movzx ebp, r15w
005E9AF7  4D 03 FF                        add r15, r15
005E9AFA  66 89 6B 08                     mov word ptr [rbx + 8], bp
005E9AFE  0F B7 C5                        movzx eax, bp
005E9B01  66 33 86 8C 00 00 00            xor ax, word ptr [rsi + 0x8c]
005E9B08  66 42 89 44 FB 0C               mov word ptr [rbx + r15*8 + 0xc], ax
005E9B0E  C6 43 0F 00                     mov byte ptr [rbx + 0xf], 0
005E9B12  45 84 E4                        test r12b, r12b
005E9B15  0F 85 DD 00 00 00               jne 0x1405e9bf8
005E9B1B  44 88 63 0A                     mov byte ptr [rbx + 0xa], r12b
005E9B1F  48 8D BE 50 01 00 00            lea rdi, [rsi + 0x150]
005E9B26  48 83 BE 38 01 00 00 00         cmp qword ptr [rsi + 0x138], 0
005E9B2E  74 0F                           je 0x1405e9b3f
005E9B30  8B D5                           mov edx, ebp
005E9B32  48 8B CE                        mov rcx, rsi
005E9B35  E8 7A 7C 00 00                  call 0x1405f17b4
005E9B3A  4C 8B C0                        mov r8, rax
005E9B3D  EB 03                           jmp 0x1405e9b42
005E9B3F  4C 8B 07                        mov r8, qword ptr [rdi]
005E9B42  49 3B F8                        cmp rdi, r8
005E9B45  74 3C                           je 0x1405e9b83
005E9B47  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9B4A  85 C9                           test ecx, ecx
005E9B4C  74 20                           je 0x1405e9b6e
005E9B4E  41 8B 40 F8                     mov eax, dword ptr [r8 - 8]
005E9B52  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9B55  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005E9B59  85 C1                           test ecx, eax
005E9B5B  74 0A                           je 0x1405e9b67
005E9B5D  33 86 88 00 00 00               xor eax, dword ptr [rsi + 0x88]
005E9B63  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005E9B67  0F B7 44 24 38                  movzx eax, word ptr [rsp + 0x38]
005E9B6C  EB 05                           jmp 0x1405e9b73
005E9B6E  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
005E9B73  0F B7 C0                        movzx eax, ax
005E9B76  48 3B E8                        cmp rbp, rax
005E9B79  76 08                           jbe 0x1405e9b83
005E9B7B  4D 8B 00                        mov r8, qword ptr [r8]
005E9B7E  49 3B F8                        cmp rdi, r8
005E9B81  75 C7                           jne 0x1405e9b4a
005E9B83  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005E9B87  48 8D 7B 10                     lea rdi, [rbx + 0x10]
005E9B8B  48 8B 08                        mov rcx, qword ptr [rax]
005E9B8E  49 3B C8                        cmp rcx, r8
005E9B91  75 10                           jne 0x1405e9ba3
005E9B93  4C 89 07                        mov qword ptr [rdi], r8
005E9B96  48 89 47 08                     mov qword ptr [rdi + 8], rax
005E9B9A  48 89 38                        mov qword ptr [rax], rdi
005E9B9D  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005E9BA1  EB 18                           jmp 0x1405e9bbb
005E9BA3  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E9BA9  33 D2                           xor edx, edx
005E9BAB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005E9BB0  45 33 C9                        xor r9d, r9d
005E9BB3  8D 4A 0D                        lea ecx, [rdx + 0xd]
005E9BB6  E8 01 1C D7 FF                  call 0x14035b7bc
005E9BBB  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9BBF  48 01 86 C0 00 00 00            add qword ptr [rsi + 0xc0], rax
005E9BC6  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E9BCD  48 85 D2                        test rdx, rdx
005E9BD0  0F 84 63 01 00 00               je 0x1405e9d39
005E9BD6  0F B7 4B 08                     movzx ecx, word ptr [rbx + 8]
005E9BDA  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005E9BDE  49 3B C8                        cmp rcx, r8
005E9BE1  0F 82 3A 01 00 00               jb 0x1405e9d21
005E9BE7  48 8B 02                        mov rax, qword ptr [rdx]
005E9BEA  48 85 C0                        test rax, rax
005E9BED  0F 84 2A 01 00 00               je 0x1405e9d1d
005E9BF3  48 8B D0                        mov rdx, rax
005E9BF6  EB E2                           jmp 0x1405e9bda
005E9BF8  80 63 0A F0                     and byte ptr [rbx + 0xa], 0xf0
005E9BFC  8B 46 70                        mov eax, dword ptr [rsi + 0x70]
005E9BFF  A8 40                           test al, 0x40
005E9C01  74 4C                           je 0x1405e9c4f
005E9C03  48 8B D5                        mov rdx, rbp
005E9C06  4C 8D 43 20                     lea r8, [rbx + 0x20]
005E9C0A  48 C1 E2 04                     shl rdx, 4
005E9C0E  48 83 EA 20                     sub rdx, 0x20
005E9C12  48 C1 EA 02                     shr rdx, 2
005E9C16  48 85 D2                        test rdx, rdx
005E9C19  74 30                           je 0x1405e9c4b
005E9C1B  41 F6 C0 04                     test r8b, 4
005E9C1F  74 0A                           je 0x1405e9c2b
005E9C21  48 FF CA                        dec rdx
005E9C24  45 89 30                        mov dword ptr [r8], r14d
005E9C27  49 83 C0 04                     add r8, 4
005E9C2B  48 8B CA                        mov rcx, rdx
005E9C2E  48 B8 EE FE EE FE EE FE EE FE   movabs rax, 0xfeeefeeefeeefeee
005E9C38  48 D1 E9                        shr rcx, 1
005E9C3B  49 8B F8                        mov rdi, r8
005E9C3E  F3 48 AB                        rep stosq qword ptr [rdi], rax
005E9C41  F6 C2 01                        test dl, 1
005E9C44  74 05                           je 0x1405e9c4b
005E9C46  45 89 74 90 FC                  mov dword ptr [r8 + rdx*4 - 4], r14d
005E9C4B  80 4B 0A 04                     or byte ptr [rbx + 0xa], 4
005E9C4F  48 83 BE 38 01 00 00 00         cmp qword ptr [rsi + 0x138], 0
005E9C57  48 8D BE 50 01 00 00            lea rdi, [rsi + 0x150]
005E9C5E  74 10                           je 0x1405e9c70
005E9C60  48 8B D5                        mov rdx, rbp
005E9C63  48 8B CE                        mov rcx, rsi
005E9C66  E8 49 7B 00 00                  call 0x1405f17b4
005E9C6B  4C 8B C0                        mov r8, rax
005E9C6E  EB 03                           jmp 0x1405e9c73
005E9C70  4C 8B 07                        mov r8, qword ptr [rdi]
005E9C73  49 3B F8                        cmp rdi, r8
005E9C76  74 3C                           je 0x1405e9cb4
005E9C78  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9C7B  85 C9                           test ecx, ecx
005E9C7D  74 20                           je 0x1405e9c9f
005E9C7F  41 8B 40 F8                     mov eax, dword ptr [r8 - 8]
005E9C83  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9C86  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005E9C8A  85 C1                           test ecx, eax
005E9C8C  74 0A                           je 0x1405e9c98
005E9C8E  33 86 88 00 00 00               xor eax, dword ptr [rsi + 0x88]
005E9C94  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005E9C98  0F B7 44 24 48                  movzx eax, word ptr [rsp + 0x48]
005E9C9D  EB 05                           jmp 0x1405e9ca4
005E9C9F  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
005E9CA4  0F B7 C0                        movzx eax, ax
005E9CA7  48 3B E8                        cmp rbp, rax
005E9CAA  76 08                           jbe 0x1405e9cb4
005E9CAC  4D 8B 00                        mov r8, qword ptr [r8]
005E9CAF  49 3B F8                        cmp rdi, r8
005E9CB2  75 C7                           jne 0x1405e9c7b
005E9CB4  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005E9CB8  48 8D 7B 10                     lea rdi, [rbx + 0x10]
005E9CBC  48 8B 08                        mov rcx, qword ptr [rax]
005E9CBF  49 3B C8                        cmp rcx, r8
005E9CC2  75 10                           jne 0x1405e9cd4
005E9CC4  4C 89 07                        mov qword ptr [rdi], r8
005E9CC7  48 89 47 08                     mov qword ptr [rdi + 8], rax
005E9CCB  48 89 38                        mov qword ptr [rax], rdi
005E9CCE  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005E9CD2  EB 18                           jmp 0x1405e9cec
005E9CD4  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E9CDA  33 D2                           xor edx, edx
005E9CDC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005E9CE1  45 33 C9                        xor r9d, r9d
005E9CE4  8D 4A 0D                        lea ecx, [rdx + 0xd]
005E9CE7  E8 D0 1A D7 FF                  call 0x14035b7bc
005E9CEC  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9CF0  48 01 86 C0 00 00 00            add qword ptr [rsi + 0xc0], rax
005E9CF7  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E9CFE  48 85 D2                        test rdx, rdx
005E9D01  74 36                           je 0x1405e9d39
005E9D03  0F B7 4B 08                     movzx ecx, word ptr [rbx + 8]
005E9D07  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005E9D0B  49 3B C8                        cmp rcx, r8
005E9D0E  72 11                           jb 0x1405e9d21
005E9D10  48 8B 02                        mov rax, qword ptr [rdx]
005E9D13  48 85 C0                        test rax, rax
005E9D16  74 05                           je 0x1405e9d1d
005E9D18  48 8B D0                        mov rdx, rax
005E9D1B  EB EA                           jmp 0x1405e9d07
005E9D1D  41 8D 48 FF                     lea ecx, [r8 - 1]
005E9D21  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9D25  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005E9D2A  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
005E9D2E  4C 8B CF                        mov r9, rdi
005E9D31  48 8B CE                        mov rcx, rsi
005E9D34  E8 8F 7B 00 00                  call 0x1405f18c8
005E9D39  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E9D3D  0F 84 A4 02 00 00               je 0x1405e9fe7
005E9D43  8A 4B 0A                        mov cl, byte ptr [rbx + 0xa]
005E9D46  32 4B 09                        xor cl, byte ptr [rbx + 9]
005E9D49  32 4B 08                        xor cl, byte ptr [rbx + 8]
005E9D4C  88 4B 0B                        mov byte ptr [rbx + 0xb], cl
005E9D4F  8B 8E 88 00 00 00               mov ecx, dword ptr [rsi + 0x88]
005E9D55  31 4B 08                        xor dword ptr [rbx + 8], ecx
005E9D58  E9 8A 02 00 00                  jmp 0x1405e9fe7
005E9D5D  4D 8B C7                        mov r8, r15
005E9D60  48 8B D3                        mov rdx, rbx
005E9D63  48 8B CE                        mov rcx, rsi
005E9D66  E8 55 17 00 00                  call 0x1405eb4c0
005E9D6B  E9 77 02 00 00                  jmp 0x1405e9fe7
005E9D70  32 C0                           xor al, al
005E9D72  E9 72 02 00 00                  jmp 0x1405e9fe9
005E9D77  41 0F B7 C4                     movzx eax, r12w
005E9D7B  66 33 86 8C 00 00 00            xor ax, word ptr [rsi + 0x8c]
005E9D82  80 BC 24 C0 00 00 00 00         cmp byte ptr [rsp + 0xc0], 0
005E9D8A  66 89 47 0C                     mov word ptr [rdi + 0xc], ax
005E9D8E  C6 43 0F 00                     mov byte ptr [rbx + 0xf], 0
005E9D92  0F 85 ED 00 00 00               jne 0x1405e9e85
005E9D98  C6 43 0A 00                     mov byte ptr [rbx + 0xa], 0
005E9D9C  48 8D BE 50 01 00 00            lea rdi, [rsi + 0x150]
005E9DA3  48 83 BE 38 01 00 00 00         cmp qword ptr [rsi + 0x138], 0
005E9DAB  74 10                           je 0x1405e9dbd
005E9DAD  49 8B D4                        mov rdx, r12
005E9DB0  48 8B CE                        mov rcx, rsi
005E9DB3  E8 FC 79 00 00                  call 0x1405f17b4
005E9DB8  4C 8B C0                        mov r8, rax
005E9DBB  EB 03                           jmp 0x1405e9dc0
005E9DBD  4C 8B 07                        mov r8, qword ptr [rdi]
005E9DC0  49 3B F8                        cmp rdi, r8
005E9DC3  74 3C                           je 0x1405e9e01
005E9DC5  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9DC8  85 C9                           test ecx, ecx
005E9DCA  74 20                           je 0x1405e9dec
005E9DCC  41 8B 40 F8                     mov eax, dword ptr [r8 - 8]
005E9DD0  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9DD3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
005E9DD7  85 C8                           test eax, ecx
005E9DD9  74 0A                           je 0x1405e9de5
005E9DDB  33 86 88 00 00 00               xor eax, dword ptr [rsi + 0x88]
005E9DE1  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
005E9DE5  0F B7 44 24 58                  movzx eax, word ptr [rsp + 0x58]
005E9DEA  EB 05                           jmp 0x1405e9df1
005E9DEC  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
005E9DF1  0F B7 C0                        movzx eax, ax
005E9DF4  4C 3B E0                        cmp r12, rax
005E9DF7  76 08                           jbe 0x1405e9e01
005E9DF9  4D 8B 00                        mov r8, qword ptr [r8]
005E9DFC  49 3B F8                        cmp rdi, r8
005E9DFF  75 C7                           jne 0x1405e9dc8
005E9E01  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005E9E05  48 8D 7B 10                     lea rdi, [rbx + 0x10]
005E9E09  48 8B 08                        mov rcx, qword ptr [rax]
005E9E0C  49 3B C8                        cmp rcx, r8
005E9E0F  75 10                           jne 0x1405e9e21
005E9E11  4C 89 07                        mov qword ptr [rdi], r8
005E9E14  48 89 47 08                     mov qword ptr [rdi + 8], rax
005E9E18  48 89 38                        mov qword ptr [rax], rdi
005E9E1B  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005E9E1F  EB 18                           jmp 0x1405e9e39
005E9E21  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E9E27  33 D2                           xor edx, edx
005E9E29  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005E9E2E  45 33 C9                        xor r9d, r9d
005E9E31  8D 4A 0D                        lea ecx, [rdx + 0xd]
005E9E34  E8 83 19 D7 FF                  call 0x14035b7bc
005E9E39  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9E3D  48 01 86 C0 00 00 00            add qword ptr [rsi + 0xc0], rax
005E9E44  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E9E4B  48 85 D2                        test rdx, rdx
005E9E4E  0F 84 E5 FE FF FF               je 0x1405e9d39
005E9E54  0F B7 4B 08                     movzx ecx, word ptr [rbx + 8]
005E9E58  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005E9E5C  49 3B C8                        cmp rcx, r8
005E9E5F  72 12                           jb 0x1405e9e73
005E9E61  48 8B 02                        mov rax, qword ptr [rdx]
005E9E64  48 85 C0                        test rax, rax
005E9E67  74 05                           je 0x1405e9e6e
005E9E69  48 8B D0                        mov rdx, rax
005E9E6C  EB EA                           jmp 0x1405e9e58
005E9E6E  41 FF C8                        dec r8d
005E9E71  EB 03                           jmp 0x1405e9e76
005E9E73  4C 8B C1                        mov r8, rcx
005E9E76  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
005E9E7B  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
005E9E80  E9 A9 FE FF FF                  jmp 0x1405e9d2e
005E9E85  80 63 0A F0                     and byte ptr [rbx + 0xa], 0xf0
005E9E89  8B 46 70                        mov eax, dword ptr [rsi + 0x70]
005E9E8C  A8 40                           test al, 0x40
005E9E8E  74 52                           je 0x1405e9ee2
005E9E90  49 8B D4                        mov rdx, r12
005E9E93  4C 8D 43 20                     lea r8, [rbx + 0x20]
005E9E97  48 C1 E2 04                     shl rdx, 4
005E9E9B  48 83 EA 20                     sub rdx, 0x20
005E9E9F  48 C1 EA 02                     shr rdx, 2
005E9EA3  48 85 D2                        test rdx, rdx
005E9EA6  74 36                           je 0x1405e9ede
005E9EA8  41 BE EE FE EE FE               mov r14d, 0xfeeefeee
005E9EAE  41 F6 C0 04                     test r8b, 4
005E9EB2  74 0A                           je 0x1405e9ebe
005E9EB4  48 FF CA                        dec rdx
005E9EB7  45 89 30                        mov dword ptr [r8], r14d
005E9EBA  49 83 C0 04                     add r8, 4
005E9EBE  48 8B CA                        mov rcx, rdx
005E9EC1  48 B8 EE FE EE FE EE FE EE FE   movabs rax, 0xfeeefeeefeeefeee
005E9ECB  48 D1 E9                        shr rcx, 1
005E9ECE  49 8B F8                        mov rdi, r8
005E9ED1  F3 48 AB                        rep stosq qword ptr [rdi], rax
005E9ED4  F6 C2 01                        test dl, 1
005E9ED7  74 05                           je 0x1405e9ede
005E9ED9  45 89 74 90 FC                  mov dword ptr [r8 + rdx*4 - 4], r14d
005E9EDE  80 4B 0A 04                     or byte ptr [rbx + 0xa], 4
005E9EE2  48 83 BE 38 01 00 00 00         cmp qword ptr [rsi + 0x138], 0
005E9EEA  48 8D BE 50 01 00 00            lea rdi, [rsi + 0x150]
005E9EF1  74 10                           je 0x1405e9f03
005E9EF3  49 8B D4                        mov rdx, r12
005E9EF6  48 8B CE                        mov rcx, rsi
005E9EF9  E8 B6 78 00 00                  call 0x1405f17b4
005E9EFE  4C 8B C0                        mov r8, rax
005E9F01  EB 03                           jmp 0x1405e9f06
005E9F03  4C 8B 07                        mov r8, qword ptr [rdi]
005E9F06  49 3B F8                        cmp rdi, r8
005E9F09  74 3C                           je 0x1405e9f47
005E9F0B  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9F0E  85 C9                           test ecx, ecx
005E9F10  74 20                           je 0x1405e9f32
005E9F12  41 8B 40 F8                     mov eax, dword ptr [r8 - 8]
005E9F16  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
005E9F19  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
005E9F1D  85 C1                           test ecx, eax
005E9F1F  74 0A                           je 0x1405e9f2b
005E9F21  33 86 88 00 00 00               xor eax, dword ptr [rsi + 0x88]
005E9F27  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
005E9F2B  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
005E9F30  EB 05                           jmp 0x1405e9f37
005E9F32  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
005E9F37  0F B7 C0                        movzx eax, ax
005E9F3A  4C 3B E0                        cmp r12, rax
005E9F3D  76 08                           jbe 0x1405e9f47
005E9F3F  4D 8B 00                        mov r8, qword ptr [r8]
005E9F42  49 3B F8                        cmp rdi, r8
005E9F45  75 C7                           jne 0x1405e9f0e
005E9F47  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005E9F4B  48 8D 7B 10                     lea rdi, [rbx + 0x10]
005E9F4F  48 8B 08                        mov rcx, qword ptr [rax]
005E9F52  49 3B C8                        cmp rcx, r8
005E9F55  75 10                           jne 0x1405e9f67
005E9F57  4C 89 07                        mov qword ptr [rdi], r8
005E9F5A  48 89 47 08                     mov qword ptr [rdi + 8], rax
005E9F5E  48 89 38                        mov qword ptr [rax], rdi
005E9F61  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005E9F65  EB 18                           jmp 0x1405e9f7f
005E9F67  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E9F6D  33 D2                           xor edx, edx
005E9F6F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005E9F74  45 33 C9                        xor r9d, r9d
005E9F77  8D 4A 0D                        lea ecx, [rdx + 0xd]
005E9F7A  E8 3D 18 D7 FF                  call 0x14035b7bc
005E9F7F  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9F83  48 01 86 C0 00 00 00            add qword ptr [rsi + 0xc0], rax
005E9F8A  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E9F91  48 85 D2                        test rdx, rdx
005E9F94  74 36                           je 0x1405e9fcc
005E9F96  0F B7 4B 08                     movzx ecx, word ptr [rbx + 8]
005E9F9A  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005E9F9E  49 3B C8                        cmp rcx, r8
005E9FA1  72 11                           jb 0x1405e9fb4
005E9FA3  48 8B 02                        mov rax, qword ptr [rdx]
005E9FA6  48 85 C0                        test rax, rax
005E9FA9  74 05                           je 0x1405e9fb0
005E9FAB  48 8B D0                        mov rdx, rax
005E9FAE  EB EA                           jmp 0x1405e9f9a
005E9FB0  41 8D 48 FF                     lea ecx, [r8 - 1]
005E9FB4  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9FB8  4C 8B CF                        mov r9, rdi
005E9FBB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005E9FC0  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
005E9FC4  48 8B CE                        mov rcx, rsi
005E9FC7  E8 FC 78 00 00                  call 0x1405f18c8
005E9FCC  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E9FD0  74 15                           je 0x1405e9fe7
005E9FD2  8A 53 0A                        mov dl, byte ptr [rbx + 0xa]
005E9FD5  32 53 09                        xor dl, byte ptr [rbx + 9]
005E9FD8  32 53 08                        xor dl, byte ptr [rbx + 8]
005E9FDB  88 53 0B                        mov byte ptr [rbx + 0xb], dl
005E9FDE  8B 96 88 00 00 00               mov edx, dword ptr [rsi + 0x88]
005E9FE4  31 53 08                        xor dword ptr [rbx + 8], edx
005E9FE7  B0 01                           mov al, 1
005E9FE9  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
005E9FEE  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005E9FF2  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
005E9FF6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
005E9FFA  49 8B E3                        mov rsp, r11
005E9FFD  41 5F                           pop r15
005E9FFF  41 5E                           pop r14
005EA001  41 5D                           pop r13
005EA003  41 5C                           pop r12
005EA005  5F                              pop rdi
005EA006  C3                              ret
005EA007  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCreateSplitBlock(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned __int8 a5, unsigned __int16 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m40;
    unsigned int v_stack_m50;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (112);
    v_r13 = 0;
    *(unsigned __int8 *)(a3 + 15) = 0;
    *(unsigned __int8 *)(a3 + 10) = a4;
    result = (unsigned __int16)((a6) ^ (*(unsigned __int16 *)(a1 + 140)));
    *(unsigned __int16 *)(a3 + 12) = (unsigned __int16)(result);
    if ((*(unsigned __int64 *)(a2 + 40)) != a2) goto loc_005E993F;
    v_rdi = 0;
    goto loc_005E996F;
loc_005E993F:
    v_rdi = (a3) - (a2);
    v_rdi = (v_rdi) >> (16);
    v_rdi = (v_rdi) + 1;
    if (v_rdi >= 254) {
        a4 = a2;
        a2 = *(unsigned __int64 *)(a2 + 40);
        a1 = 3;
        result = RtlpLogHeapFailure(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(a3 + 14) = (unsigned __int8)(v_rdi);
    v_rdi = (a7) << (4);
    v_rdi = (v_rdi) + (a3);
    *(unsigned __int8 *)(a3 + 11) = 0;
    *(unsigned __int16 *)(a3 + 8) = (unsigned __int16)((unsigned __int16)(a7));
loc_005E9992:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) >> (20));
    result = (unsigned __int8)((result) & (*(unsigned __int8 *)(a1 + 138)));
    result = (unsigned __int8)((result) ^ (*(unsigned __int8 *)(v_rdi + 10)));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_005E9D77;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005E99D1;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 10)) ^ (*(unsigned __int8 *)(v_rdi + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_rdi + 8)));
    if ((*(unsigned __int8 *)(v_rdi + 11)) != ((unsigned __int8)(a1))) {
        a2 = v_rdi;
        a1 = a1;
        result = RtlpAnalyzeHeapFailure(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 16) + 8))) goto loc_005E99ED;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24))) == (v_rdi + 16)) goto loc_005E9A1C;
loc_005E99ED:
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24));
    result = RtlpLogHeapFailure(13, a1, v_rdi + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 16) + 8));
    if (0 != 0) goto loc_005E9D70;
    goto loc_005E9992;
loc_005E9A1C:
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E9A6A;
loc_005E9A37:
    if ((*(unsigned __int16 *)(v_rdi + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E9A52;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9A4D;
    goto loc_005E9A37;
loc_005E9A4D:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8))) - 1);
    goto loc_005E9A55;
loc_005E9A52:
loc_005E9A55:
    v_stack_m70 = *(unsigned __int16 *)(v_rdi + 8);
    v_stack_m78 = (unsigned int)(*(unsigned __int16 *)(v_rdi + 8));
    result = RtlpHeapRemoveListEntry(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)), *(unsigned __int16 *)(v_rdi + 8), v_rdi + 16);
loc_005E9A6A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24)) = *(unsigned __int64 *)(v_rdi + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 16) + 8) = *(unsigned __int64 *)(v_rdi + 24);
    if (a5 == 0) goto loc_005E9AD9;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 10))) & (4)) == 0) goto loc_005E9AD9;
    v_rbp = (*(unsigned __int16 *)(v_rdi + 8)) << (4);
    v_rbp = (v_rbp) - (32);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 10))) & (2)) == 0) goto loc_005E9AA5;
    if (v_rbp >= = 4) {
        v_rbp = (v_rbp) - (4);
    }
    result = RtlCompareMemoryUlong(v_rdi + 32, v_rbp, (unsigned int)((unsigned int)((unsigned int)(0xFEEEFEEEULL))), v_rdi + 16);
    if (result == v_rbp) goto loc_005E9AD9;
    a3 = (v_rdi + 32) + (result);
    result = DbgPrint(v_rip + 929558, v_rdi, a3, v_rdi + 16);
    if ((*(unsigned __int8 *)(v_rip + 9820962)) != 0) {
    }
    *(unsigned __int8 *)(a3 + 10) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 10));
    v_r15 = (a7) + (*(unsigned __int16 *)(v_rdi + 8));
    if (v_r15 > 0xFF00ULL) goto loc_005E9D5D;
    v_r15 = (v_r15) + (v_r15);
    *(unsigned __int16 *)(a3 + 8) = (unsigned __int16)((unsigned __int16)(v_r15));
    result = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(v_r15))) ^ (*(unsigned __int16 *)(a1 + 140)));
    *(unsigned __int16 *)(a3 + v_r15 * 8 + 12) = (unsigned __int16)(result);
    *(unsigned __int8 *)(a3 + 15) = 0;
    if (a5 != 0) goto loc_005E9BF8;
    *(unsigned __int8 *)(a3 + 10) = a5;
    if ((*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9B3F;
    result = RtlpFindEntry(a1, (unsigned int)((unsigned int)((unsigned __int16)(v_r15))), a3, v_rdi + 16);
    goto loc_005E9B42;
loc_005E9B3F:
loc_005E9B42:
    if ((a1 + 336) == (*(unsigned __int64 *)(a1 + 336))) goto loc_005E9B83;
loc_005E9B4A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005E9B6E;
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m60 = (unsigned int)(result);
    }
    goto loc_005E9B73;
loc_005E9B6E:
loc_005E9B73:
    if (((unsigned __int16)(v_r15)) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 336) - 8)))) goto loc_005E9B83;
    if ((a1 + 336) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9B4A;
loc_005E9B83:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9BA3;
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336));
    *(unsigned __int64 *)(a3 + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8)) = a3 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8) = a3 + 16;
    goto loc_005E9BBB;
loc_005E9BA3:
    a2 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8));
    a4 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)), a4);
loc_005E9BBB:
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E9D39;
loc_005E9BDA:
    if ((*(unsigned __int16 *)(a3 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E9D21;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9D1D;
    goto loc_005E9BDA;
loc_005E9BF8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (64)) == 0) goto loc_005E9C4F;
    a2 = ((unsigned __int16)(v_r15)) << (4);
    a2 = (a2) - (32);
    a2 = (a2) >> (2);
    if (a2 == 0) goto loc_005E9C4B;
    if ((((unsigned __int8)(a3 + 32)) & (4)) != 0) {
        a2 = (a2) - 1;
        *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)(0xFEEEFEEEULL));
        a3 = (a3 + 32) + (4);
    }
    a1 = (a2) >> (1);
    if ((((unsigned __int8)(a2)) & (1)) != 0) {
        *(unsigned int *)(a3 + a2 * 4 - 4) = (unsigned int)((unsigned int)(0xFEEEFEEEULL));
    }
loc_005E9C4F:
    if ((*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9C70;
    result = RtlpFindEntry(a1, (unsigned __int16)(v_r15), a3, a4);
    goto loc_005E9C73;
loc_005E9C70:
loc_005E9C73:
    if ((a1 + 336) == (*(unsigned __int64 *)(a1 + 336))) goto loc_005E9CB4;
loc_005E9C7B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005E9C9F;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m50 = (unsigned int)(result);
    }
    goto loc_005E9CA4;
loc_005E9C9F:
loc_005E9CA4:
    if (((unsigned __int16)(v_r15)) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 336) - 8)))) goto loc_005E9CB4;
    if ((a1 + 336) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9C7B;
loc_005E9CB4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9CD4;
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336));
    *(unsigned __int64 *)(a3 + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8)) = a3 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8) = a3 + 16;
    goto loc_005E9CEC;
loc_005E9CD4:
    a2 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8));
    a4 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)), a4);
loc_005E9CEC:
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E9D39;
loc_005E9D07:
    if ((*(unsigned __int16 *)(a3 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E9D21;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9D1D;
    goto loc_005E9D07;
loc_005E9D1D:
loc_005E9D21:
    v_stack_m70 = *(unsigned __int16 *)(a3 + 8);
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1);
loc_005E9D2E:
    result = RtlpHeapAddListEntry(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)), a3 + 16);
loc_005E9D39:
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_005E9FE7;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a3 + 10)) ^ (*(unsigned __int8 *)(a3 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(a3 + 8)));
    *(unsigned __int8 *)(a3 + 11) = (unsigned __int8)(a1);
    goto loc_005E9FE7;
loc_005E9D5D:
    result = RtlpInsertFreeBlock(a1, a3, v_r15, a3 + 16);
    goto loc_005E9FE7;
loc_005E9D70:
    result = 0;
    goto loc_005E9FE9;
loc_005E9D77:
    result = (unsigned __int16)((a5) ^ (*(unsigned __int16 *)(a1 + 140)));
    *(unsigned __int16 *)(a3 + 16 + 12) = (unsigned __int16)(result);
    *(unsigned __int8 *)(a3 + 15) = 0;
    if (a5 != 0) goto loc_005E9E85;
    *(unsigned __int8 *)(a3 + 10) = 0;
    if ((*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9DBD;
    result = RtlpFindEntry(a1, a5, v_r15, a3 + 16);
    goto loc_005E9DC0;
loc_005E9DBD:
loc_005E9DC0:
    if ((a1 + 336) == (*(unsigned __int64 *)(a1 + 336))) goto loc_005E9E01;
loc_005E9DC8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005E9DEC;
    v_stack_m40 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m40 = (unsigned int)(result);
    }
    goto loc_005E9DF1;
loc_005E9DEC:
loc_005E9DF1:
    if (a5 <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 336) - 8)))) goto loc_005E9E01;
    if ((a1 + 336) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9DC8;
loc_005E9E01:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9E21;
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336));
    *(unsigned __int64 *)(a3 + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8)) = a3 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8) = a3 + 16;
    goto loc_005E9E39;
loc_005E9E21:
    a2 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8));
    a4 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)), a4);
loc_005E9E39:
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E9D39;
loc_005E9E58:
    if ((*(unsigned __int16 *)(a3 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E9E73;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9E6E;
    goto loc_005E9E58;
loc_005E9E6E:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8))) - 1);
    goto loc_005E9E76;
loc_005E9E73:
loc_005E9E76:
    v_stack_m70 = *(unsigned __int16 *)(a3 + 8);
    v_stack_m78 = (unsigned int)(*(unsigned __int16 *)(a3 + 8));
    goto loc_005E9D2E;
loc_005E9E85:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (64)) == 0) goto loc_005E9EE2;
    a2 = (a5) << (4);
    a2 = (a2) - (32);
    a2 = (a2) >> (2);
    if (a2 == 0) goto loc_005E9EDE;
    if ((((unsigned __int8)(a3 + 32)) & (4)) != 0) {
        a2 = (a2) - 1;
        *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)(0xFEEEFEEEULL));
        a3 = (a3 + 32) + (4);
    }
    a1 = (a2) >> (1);
    if ((((unsigned __int8)(a2)) & (1)) != 0) {
        *(unsigned int *)(a3 + a2 * 4 - 4) = (unsigned int)((unsigned int)(0xFEEEFEEEULL));
    }
loc_005E9EE2:
    if ((*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9F03;
    result = RtlpFindEntry(a1, a5, a3, a4);
    goto loc_005E9F06;
loc_005E9F03:
loc_005E9F06:
    if ((a1 + 336) == (*(unsigned __int64 *)(a1 + 336))) goto loc_005E9F47;
loc_005E9F0E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005E9F32;
    v_stack_m30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m30 = (unsigned int)(result);
    }
    goto loc_005E9F37;
loc_005E9F32:
loc_005E9F37:
    if (a5 <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 336) - 8)))) goto loc_005E9F47;
    if ((a1 + 336) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9F0E;
loc_005E9F47:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_005E9F67;
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336));
    *(unsigned __int64 *)(a3 + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8)) = a3 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8) = a3 + 16;
    goto loc_005E9F7F;
loc_005E9F67:
    a2 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8));
    a4 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)), a4);
loc_005E9F7F:
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E9FCC;
loc_005E9F9A:
    if ((*(unsigned __int16 *)(a3 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E9FB4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_005E9FB0;
    goto loc_005E9F9A;
loc_005E9FB0:
loc_005E9FB4:
    v_stack_m70 = *(unsigned __int16 *)(a3 + 8);
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1);
    result = RtlpHeapAddListEntry(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)), a3 + 16);
loc_005E9FCC:
    if ((*(unsigned int *)(a1 + 124)) != 0) {
        a2 = *(unsigned __int8 *)(a3 + 10);
        a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(a3 + 9)));
        a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(a3 + 8)));
        *(unsigned __int8 *)(a3 + 11) = (unsigned __int8)(a2);
        a2 = *(unsigned int *)(a1 + 136);
    }
loc_005E9FE9:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCreateSplitBlock(void *Arg1, void *Arg2, void *Arg3, uint8_t Arg4, uint8_t Arg5, uint16_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m40;
    uint32_t v_stack_m50;
    uint32_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (112);
    local_r13 = 0;
    *(uint8_t *)(arg3 + 0xF) = 0;
    *(uint8_t *)(arg3 + 0xA) = Arg4;
    result = (uint16_t)((Arg6) ^ (*(uint16_t *)(arg1 + 0x8C)));
    *(uint16_t *)(arg3 + 0xC) = (uint16_t)(result);
    if ((*(uint64_t *)(arg2 + 0x28)) != Arg2) goto loc_005E993F;
    local_rdi = 0;
    goto loc_005E996F;
loc_005E993F:
    local_rdi = (Arg3) - (Arg2);
    local_rdi = (local_rdi) >> (16);
    local_rdi = (local_rdi) + 1;
    if (local_rdi >= 254) {
        Arg4 = Arg2;
        Arg2 = *(uint64_t *)(arg2 + 0x28);
        Arg1 = 3;
        result = RtlpLogHeapFailure(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(arg3 + 0xE) = (uint8_t)(local_rdi);
    local_rdi = (Arg7) << (4);
    local_rdi = (local_rdi) + (Arg3);
    *(uint8_t *)(arg3 + 0xB) = 0;
    *(uint16_t *)(arg3 + 0x8) = (uint16_t)((uint16_t)(Arg7));
loc_005E9992:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) >> (20));
    result = (uint8_t)((result) & (*(uint8_t *)(arg1 + 0x8A)));
    result = (uint8_t)((result) ^ (*(uint8_t *)(local_rdi + 0xA)));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_005E9D77;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005E99D1;
    Arg1 = (uint8_t)((*(uint8_t *)(local_rdi + 0xA)) ^ (*(uint8_t *)(local_rdi + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(local_rdi + 0x8)));
    if ((*(uint8_t *)(local_rdi + 0xB)) != ((uint8_t)(Arg1))) {
        Arg2 = local_rdi;
        Arg1 = Arg1;
        result = RtlpAnalyzeHeapFailure(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18))) != (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x8))) goto loc_005E99ED;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18))) == (local_rdi + 16)) goto loc_005E9A1C;
loc_005E99ED:
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18));
    result = RtlpLogHeapFailure(13, Arg1, local_rdi + 16, *(uint64_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x8));
    if (0 != 0) goto loc_005E9D70;
    goto loc_005E9992;
loc_005E9A1C:
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E9A6A;
loc_005E9A37:
    if ((*(uint16_t *)(local_rdi + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E9A52;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9A4D;
    goto loc_005E9A37;
loc_005E9A4D:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8))) - 1);
    goto loc_005E9A55;
loc_005E9A52:
loc_005E9A55:
    v_stack_m70 = *(uint16_t *)(local_rdi + 0x8);
    v_stack_m78 = (uint32_t)(*(uint16_t *)(local_rdi + 0x8));
    result = RtlpHeapRemoveListEntry(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x138)), *(uint16_t *)(local_rdi + 0x8), local_rdi + 16);
loc_005E9A6A:
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18)) = *(uint64_t *)(local_rdi + 0x10);
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x8) = *(uint64_t *)(local_rdi + 0x18);
    if (Arg5 == 0) goto loc_005E9AD9;
    if ((((uint8_t)(*(uint8_t *)(local_rdi + 0xA))) & (4)) == 0) goto loc_005E9AD9;
    local_rbp = (*(uint16_t *)(local_rdi + 0x8)) << (4);
    local_rbp = (local_rbp) - (32);
    if ((((uint8_t)(*(uint8_t *)(local_rdi + 0xA))) & (2)) == 0) goto loc_005E9AA5;
    if (local_rbp >= = 4) {
        local_rbp = (local_rbp) - (4);
    }
    result = RtlCompareMemoryUlong(local_rdi + 32, local_rbp, (uint32_t)((uint32_t)((uint32_t)(0xFEEEFEEEULL))), local_rdi + 16);
    if (result == local_rbp) goto loc_005E9AD9;
    Arg3 = (local_rdi + 32) + (result);
    result = DbgPrint(v_rip + 929558, local_rdi, Arg3, local_rdi + 16);
    if ((*(uint8_t *)(v_rip + 0x95DB22)) != 0) {
    }
    *(uint8_t *)(arg3 + 0xA) = (uint8_t)(*(uint8_t *)(local_rdi + 0xA));
    local_r15 = (Arg7) + (*(uint16_t *)(local_rdi + 0x8));
    if (local_r15 > 0xFF00ULL) goto loc_005E9D5D;
    local_r15 = (local_r15) + (local_r15);
    *(uint16_t *)(arg3 + 0x8) = (uint16_t)((uint16_t)(local_r15));
    result = (uint16_t)(((uint16_t)((uint16_t)(local_r15))) ^ (*(uint16_t *)(arg1 + 0x8C)));
    *(uint16_t *)(arg3 + local_r15 * 8 + 0xC) = (uint16_t)(result);
    *(uint8_t *)(arg3 + 0xF) = 0;
    if (Arg5 != 0) goto loc_005E9BF8;
    *(uint8_t *)(arg3 + 0xA) = Arg5;
    if ((*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9B3F;
    result = RtlpFindEntry(Arg1, (uint32_t)((uint32_t)((uint16_t)(local_r15))), Arg3, local_rdi + 16);
    goto loc_005E9B42;
loc_005E9B3F:
loc_005E9B42:
    if ((Arg1 + 336) == (*(uint64_t *)(arg1 + 0x150))) goto loc_005E9B83;
loc_005E9B4A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005E9B6E;
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m60 = (uint32_t)(result);
    }
    goto loc_005E9B73;
loc_005E9B6E:
loc_005E9B73:
    if (((uint16_t)(local_r15)) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)))) goto loc_005E9B83;
    if ((Arg1 + 336) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9B4A;
loc_005E9B83:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9BA3;
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x150));
    *(uint64_t *)(arg3 + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8)) = Arg3 + 16;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8) = Arg3 + 16;
    goto loc_005E9BBB;
loc_005E9BA3:
    Arg2 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8));
    Arg4 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x150)), Arg4);
loc_005E9BBB:
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E9D39;
loc_005E9BDA:
    if ((*(uint16_t *)(arg3 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E9D21;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9D1D;
    goto loc_005E9BDA;
loc_005E9BF8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (64)) == 0) goto loc_005E9C4F;
    Arg2 = ((uint16_t)(local_r15)) << (4);
    Arg2 = (Arg2) - (32);
    Arg2 = (Arg2) >> (2);
    if (Arg2 == NULL) goto loc_005E9C4B;
    if ((((uint8_t)(Arg3 + 32)) & (4)) != 0) {
        Arg2 = (Arg2) - 1;
        *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint32_t)(0xFEEEFEEEULL));
        Arg3 = (Arg3 + 32) + (4);
    }
    Arg1 = (Arg2) >> (1);
    if ((((uint8_t)(Arg2)) & (1)) != 0) {
        *(uint32_t *)(arg3 + arg2 * 4 - 0x4) = (uint32_t)((uint32_t)(0xFEEEFEEEULL));
    }
loc_005E9C4F:
    if ((*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9C70;
    result = RtlpFindEntry(Arg1, (uint16_t)(local_r15), Arg3, Arg4);
    goto loc_005E9C73;
loc_005E9C70:
loc_005E9C73:
    if ((Arg1 + 336) == (*(uint64_t *)(arg1 + 0x150))) goto loc_005E9CB4;
loc_005E9C7B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005E9C9F;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m50 = (uint32_t)(result);
    }
    goto loc_005E9CA4;
loc_005E9C9F:
loc_005E9CA4:
    if (((uint16_t)(local_r15)) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)))) goto loc_005E9CB4;
    if ((Arg1 + 336) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9C7B;
loc_005E9CB4:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9CD4;
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x150));
    *(uint64_t *)(arg3 + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8)) = Arg3 + 16;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8) = Arg3 + 16;
    goto loc_005E9CEC;
loc_005E9CD4:
    Arg2 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8));
    Arg4 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x150)), Arg4);
loc_005E9CEC:
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E9D39;
loc_005E9D07:
    if ((*(uint16_t *)(arg3 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E9D21;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9D1D;
    goto loc_005E9D07;
loc_005E9D1D:
loc_005E9D21:
    v_stack_m70 = *(uint16_t *)(arg3 + 0x8);
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1);
loc_005E9D2E:
    result = RtlpHeapAddListEntry(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x138)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)), Arg3 + 16);
loc_005E9D39:
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_005E9FE7;
    Arg1 = (uint8_t)((*(uint8_t *)(arg3 + 0xA)) ^ (*(uint8_t *)(arg3 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(arg3 + 0x8)));
    *(uint8_t *)(arg3 + 0xB) = (uint8_t)(Arg1);
    goto loc_005E9FE7;
loc_005E9D5D:
    result = RtlpInsertFreeBlock(Arg1, Arg3, local_r15, Arg3 + 16);
    goto loc_005E9FE7;
loc_005E9D70:
    result = 0;
    goto loc_005E9FE9;
loc_005E9D77:
    result = (uint16_t)((Arg5) ^ (*(uint16_t *)(arg1 + 0x8C)));
    *(uint16_t *)(arg3 + 0x10 + 0xC) = (uint16_t)(result);
    *(uint8_t *)(arg3 + 0xF) = 0;
    if (Arg5 != 0) goto loc_005E9E85;
    *(uint8_t *)(arg3 + 0xA) = 0;
    if ((*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9DBD;
    result = RtlpFindEntry(Arg1, Arg5, local_r15, Arg3 + 16);
    goto loc_005E9DC0;
loc_005E9DBD:
loc_005E9DC0:
    if ((Arg1 + 336) == (*(uint64_t *)(arg1 + 0x150))) goto loc_005E9E01;
loc_005E9DC8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005E9DEC;
    v_stack_m40 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m40 = (uint32_t)(result);
    }
    goto loc_005E9DF1;
loc_005E9DEC:
loc_005E9DF1:
    if (Arg5 <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)))) goto loc_005E9E01;
    if ((Arg1 + 336) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9DC8;
loc_005E9E01:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9E21;
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x150));
    *(uint64_t *)(arg3 + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8)) = Arg3 + 16;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8) = Arg3 + 16;
    goto loc_005E9E39;
loc_005E9E21:
    Arg2 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8));
    Arg4 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x150)), Arg4);
loc_005E9E39:
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E9D39;
loc_005E9E58:
    if ((*(uint16_t *)(arg3 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E9E73;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9E6E;
    goto loc_005E9E58;
loc_005E9E6E:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8))) - 1);
    goto loc_005E9E76;
loc_005E9E73:
loc_005E9E76:
    v_stack_m70 = *(uint16_t *)(arg3 + 0x8);
    v_stack_m78 = (uint32_t)(*(uint16_t *)(arg3 + 0x8));
    goto loc_005E9D2E;
loc_005E9E85:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (64)) == 0) goto loc_005E9EE2;
    Arg2 = (Arg5) << (4);
    Arg2 = (Arg2) - (32);
    Arg2 = (Arg2) >> (2);
    if (Arg2 == NULL) goto loc_005E9EDE;
    if ((((uint8_t)(Arg3 + 32)) & (4)) != 0) {
        Arg2 = (Arg2) - 1;
        *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint32_t)(0xFEEEFEEEULL));
        Arg3 = (Arg3 + 32) + (4);
    }
    Arg1 = (Arg2) >> (1);
    if ((((uint8_t)(Arg2)) & (1)) != 0) {
        *(uint32_t *)(arg3 + arg2 * 4 - 0x4) = (uint32_t)((uint32_t)(0xFEEEFEEEULL));
    }
loc_005E9EE2:
    if ((*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9F03;
    result = RtlpFindEntry(Arg1, Arg5, Arg3, Arg4);
    goto loc_005E9F06;
loc_005E9F03:
loc_005E9F06:
    if ((Arg1 + 336) == (*(uint64_t *)(arg1 + 0x150))) goto loc_005E9F47;
loc_005E9F0E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005E9F32;
    v_stack_m30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m30 = (uint32_t)(result);
    }
    goto loc_005E9F37;
loc_005E9F32:
loc_005E9F37:
    if (Arg5 <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)))) goto loc_005E9F47;
    if ((Arg1 + 336) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9F0E;
loc_005E9F47:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_005E9F67;
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x150));
    *(uint64_t *)(arg3 + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8)) = Arg3 + 16;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8) = Arg3 + 16;
    goto loc_005E9F7F;
loc_005E9F67:
    Arg2 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8));
    Arg4 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x150)), Arg4);
loc_005E9F7F:
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E9FCC;
loc_005E9F9A:
    if ((*(uint16_t *)(arg3 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E9FB4;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_005E9FB0;
    goto loc_005E9F9A;
loc_005E9FB0:
loc_005E9FB4:
    v_stack_m70 = *(uint16_t *)(arg3 + 0x8);
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1);
    result = RtlpHeapAddListEntry(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x138)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)), Arg3 + 16);
loc_005E9FCC:
    if ((*(uint32_t *)(arg1 + 0x7C)) != 0) {
        Arg2 = *(uint8_t *)(arg3 + 0xA);
        Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(arg3 + 0x9)));
        Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(arg3 + 0x8)));
        *(uint8_t *)(arg3 + 0xB) = (uint8_t)(Arg2);
        Arg2 = *(uint32_t *)(arg1 + 0x88);
    }
loc_005E9FE9:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x8A` | `8` | `R` |
| `Arg1` | `+ 0x8C` | `16` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R/W` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `8` | `R` |
| `Arg3` | `+ 0x8` | `16` | `R` |
| `Arg3` | `+ 0x8` | `16` | `W` |
| `Arg3` | `+ 0x8` | `32` | `R/W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x9` | `8` | `R` |
| `Arg3` | `+ 0xA` | `8` | `R` |
| `Arg3` | `+ 0xA` | `8` | `R/W` |
| `Arg3` | `+ 0xA` | `8` | `W` |
| `Arg3` | `+ 0xB` | `8` | `W` |
| `Arg3` | `+ 0xC` | `16` | `W` |
| `Arg3` | `+ 0xC + r15*8` | `16` | `W` |
| `Arg3` | `+ 0xE` | `8` | `W` |
| `Arg3` | `+ 0xF` | `8` | `W` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E98F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
