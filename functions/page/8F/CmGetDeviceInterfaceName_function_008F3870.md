# CmGetDeviceInterfaceName

- RVA: `0x008F3870`–`0x008F3CE3` (길이 `1,139` bytes)
- VA: `0x00000001408F3870`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087694`
- 디코드: `303`개 명령, `1,139/1,139` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008F38A4` → [PnpIsValidGuidString](PnpIsValidGuidString_function_008F37F8.md) (function, `0x008F37F8`)
- `0x008F38B4` → [CmValidateDeviceName](CmValidateDeviceName_function_008F3CF0.md) (function, `0x008F3CF0`)
- `0x008F393E` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x008F3967` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x008F3A64` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x008F3BE8` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x008F3C62` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (function, `0x0041E3F0`)
- `0x008F3CB1` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (function, `0x0041E3F0`)

### Direct callers
- [IoGetDeviceInterfaceAlias](IoGetDeviceInterfaceAlias_function_008F5570.md) at `0x008F585F`
- [IopRegisterDeviceInterface](../95/IopRegisterDeviceInterface_function_009501B0.md) at `0x009502A5`
- [sub_00B1EAB0](../B1/Unknown_function_00B1EAB0.md) at `0x00B1EB01`
- [sub_00B261E4](../B2/Unknown_function_00B261E4.md) at `0x00B2623A`

### Static image references
- `0x008F390F` → RVA `0x00B0D4E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008F3919` → RVA `0x00B013A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008F39B7` → RVA `0x00AFDC40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008F3B42` → RVA `0x00AFC990` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x008F393E` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x008F3967` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x008F3A64` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x008F3BE8` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x008F3C62` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (`PAGE` → `.text`)
  - `0x008F3CB1` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F3870  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008F3875  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008F387A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
008F387F  55                              push rbp
008F3880  56                              push rsi
008F3881  57                              push rdi
008F3882  41 54                           push r12
008F3884  41 55                           push r13
008F3886  41 56                           push r14
008F3888  41 57                           push r15
008F388A  48 8B EC                        mov rbp, rsp
008F388D  48 83 EC 50                     sub rsp, 0x50
008F3891  33 F6                           xor esi, esi
008F3893  48 8B CA                        mov rcx, rdx
008F3896  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
008F389A  4D 8B E9                        mov r13, r9
008F389D  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
008F38A1  49 8B D8                        mov rbx, r8
008F38A4  E8 4F FF FF FF                  call 0x1408f37f8
008F38A9  84 C0                           test al, al
008F38AB  0F 84 03 02 00 00               je 0x1408f3ab4
008F38B1  48 8B D3                        mov rdx, rbx
008F38B4  E8 37 04 00 00                  call 0x1408f3cf0
008F38B9  85 C0                           test eax, eax
008F38BB  0F 88 F3 01 00 00               js 0x1408f3ab4
008F38C1  48 83 C9 FF                     or rcx, 0xffffffffffffffff
008F38C5  4D 85 ED                        test r13, r13
008F38C8  0F 85 ED 01 00 00               jne 0x1408f3abb
008F38CE  44 8B FE                        mov r15d, esi
008F38D1  48 FF C1                        inc rcx
008F38D4  66 39 34 4B                     cmp word ptr [rbx + rcx*2], si
008F38D8  75 F7                           jne 0x1408f38d1
008F38DA  48 83 C1 2C                     add rcx, 0x2c
008F38DE  49 8D 47 02                     lea rax, [r15 + 2]
008F38E2  4D 85 FF                        test r15, r15
008F38E5  48 0F 44 C1                     cmove rax, rcx
008F38E9  B9 FF FF FF FF                  mov ecx, 0xffffffff
008F38EE  48 3B C1                        cmp rax, rcx
008F38F1  0F 87 9F 01 00 00               ja 0x1408f3a96
008F38F7  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
008F38FB  48 85 C9                        test rcx, rcx
008F38FE  74 02                           je 0x1408f3902
008F3900  89 01                           mov dword ptr [rcx], eax
008F3902  3B 45 70                        cmp eax, dword ptr [rbp + 0x70]
008F3905  0F 87 CE 03 00 00               ja 0x1408f3cd9
008F390B  40 38 75 60                     cmp byte ptr [rbp + 0x60], sil
008F390F  48 8D 05 CA 9B 21 00            lea rax, [rip + 0x219bca]
008F3916  8B 55 70                        mov edx, dword ptr [rbp + 0x70]
008F3919  4C 8D 05 80 DA 20 00            lea r8, [rip + 0x20da80]
008F3920  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
008F3924  4C 8D 4D E0                     lea r9, [rbp - 0x20]
008F3928  4C 0F 44 C0                     cmove r8, rax
008F392C  BF 00 09 00 00                  mov edi, 0x900
008F3931  48 8D 45 40                     lea rax, [rbp + 0x40]
008F3935  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
008F3939  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F393E  E8 7D A8 B2 FF                  call 0x14041e1c0
008F3943  85 C0                           test eax, eax
008F3945  0F 88 50 01 00 00               js 0x1408f3a9b
008F394B  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
008F394F  48 8D 45 40                     lea rax, [rbp + 0x40]
008F3953  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008F3957  4C 8D 4D E0                     lea r9, [rbp - 0x20]
008F395B  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
008F395F  4C 8B C3                        mov r8, rbx
008F3962  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F3967  E8 54 A8 B2 FF                  call 0x14041e1c0
008F396C  85 C0                           test eax, eax
008F396E  0F 88 27 01 00 00               js 0x1408f3a9b
008F3974  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
008F3978  41 BC FE FF FF 7F               mov r12d, 0x7ffffffe
008F397E  48 8B 7D 40                     mov rdi, qword ptr [rbp + 0x40]
008F3982  4D 85 F6                        test r14, r14
008F3985  0F 84 67 02 00 00               je 0x1408f3bf2
008F398B  48 81 FF FF FF FF 7F            cmp rdi, 0x7fffffff
008F3992  0F 87 63 02 00 00               ja 0x1408f3bfb
008F3998  4C 89 75 E8                     mov qword ptr [rbp - 0x18], r14
008F399C  4D 8B CE                        mov r9, r14
008F399F  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
008F39A3  4C 8B C7                        mov r8, rdi
008F39A6  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F39AB  48 85 FF                        test rdi, rdi
008F39AE  0F 84 7D 02 00 00               je 0x1408f3c31
008F39B4  4D 8B C4                        mov r8, r12
008F39B7  4C 8D 0D 82 A2 20 00            lea r9, [rip + 0x20a282]
008F39BE  4C 2B C7                        sub r8, rdi
008F39C1  48 8B D7                        mov rdx, rdi
008F39C4  4D 2B CE                        sub r9, r14
008F39C7  49 8B CE                        mov rcx, r14
008F39CA  4C 8B D6                        mov r10, rsi
008F39CD  4A 8D 04 02                     lea rax, [rdx + r8]
008F39D1  48 85 C0                        test rax, rax
008F39D4  74 1A                           je 0x1408f39f0
008F39D6  42 0F B7 04 09                  movzx eax, word ptr [rcx + r9]
008F39DB  66 85 C0                        test ax, ax
008F39DE  74 10                           je 0x1408f39f0
008F39E0  66 89 01                        mov word ptr [rcx], ax
008F39E3  49 FF C2                        inc r10
008F39E6  48 83 C1 02                     add rcx, 2
008F39EA  48 83 EA 01                     sub rdx, 1
008F39EE  75 DD                           jne 0x1408f39cd
008F39F0  48 85 D2                        test rdx, rdx
008F39F3  48 8D 41 FE                     lea rax, [rcx - 2]
008F39F7  4C 8B C7                        mov r8, rdi
008F39FA  48 0F 45 C1                     cmovne rax, rcx
008F39FE  49 8D 4A FF                     lea rcx, [r10 - 1]
008F3A02  49 0F 45 CA                     cmovne rcx, r10
008F3A06  66 89 30                        mov word ptr [rax], si
008F3A09  48 8B C2                        mov rax, rdx
008F3A0C  48 F7 D8                        neg rax
008F3A0F  4D 8D 0C 4E                     lea r9, [r14 + rcx*2]
008F3A13  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
008F3A17  1B F6                           sbb esi, esi
008F3A19  4C 2B C1                        sub r8, rcx
008F3A1C  F7 D6                           not esi
008F3A1E  4C 89 45 F0                     mov qword ptr [rbp - 0x10], r8
008F3A22  81 E6 05 00 00 80               and esi, 0x80000005
008F3A28  48 85 D2                        test rdx, rdx
008F3A2B  0F 84 10 02 00 00               je 0x1408f3c41
008F3A31  4D 8B F1                        mov r14, r9
008F3A34  4C 89 4D E0                     mov qword ptr [rbp - 0x20], r9
008F3A38  49 8B F8                        mov rdi, r8
008F3A3B  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
008F3A3F  8B C6                           mov eax, esi
008F3A41  85 F6                           test esi, esi
008F3A43  78 56                           js 0x1408f3a9b
008F3A45  4C 8B 45 48                     mov r8, qword ptr [rbp + 0x48]
008F3A49  48 8D 45 40                     lea rax, [rbp + 0x40]
008F3A4D  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
008F3A55  4C 8D 4D E0                     lea r9, [rbp - 0x20]
008F3A59  48 8B D7                        mov rdx, rdi
008F3A5C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F3A61  49 8B CE                        mov rcx, r14
008F3A64  E8 57 A7 B2 FF                  call 0x14041e1c0
008F3A69  45 33 D2                        xor r10d, r10d
008F3A6C  85 C0                           test eax, eax
008F3A6E  78 2B                           js 0x1408f3a9b
008F3A70  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
008F3A74  48 83 C2 08                     add rdx, 8
008F3A78  0F B7 0A                        movzx ecx, word ptr [rdx]
008F3A7B  66 85 C9                        test cx, cx
008F3A7E  0F 84 81 00 00 00               je 0x1408f3b05
008F3A84  66 83 F9 5C                     cmp cx, 0x5c
008F3A88  74 74                           je 0x1408f3afe
008F3A8A  66 83 F9 2F                     cmp cx, 0x2f
008F3A8E  74 6E                           je 0x1408f3afe
008F3A90  48 83 C2 02                     add rdx, 2
008F3A94  EB E2                           jmp 0x1408f3a78
008F3A96  B8 95 00 00 C0                  mov eax, 0xc0000095
008F3A9B  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
008F3AA3  48 83 C4 50                     add rsp, 0x50
008F3AA7  41 5F                           pop r15
008F3AA9  41 5E                           pop r14
008F3AAB  41 5D                           pop r13
008F3AAD  41 5C                           pop r12
008F3AAF  5F                              pop rdi
008F3AB0  5E                              pop rsi
008F3AB1  5D                              pop rbp
008F3AB2  C3                              ret
008F3AB3  CC                              int3
008F3AB4  B8 0D 00 00 C0                  mov eax, 0xc000000d
008F3AB9  EB E0                           jmp 0x1408f3a9b
008F3ABB  4C 8B F9                        mov r15, rcx
008F3ABE  49 FF C7                        inc r15
008F3AC1  66 43 39 74 7D 00               cmp word ptr [r13 + r15*2], si
008F3AC7  75 F5                           jne 0x1408f3abe
008F3AC9  49 8D 47 FF                     lea rax, [r15 - 1]
008F3ACD  48 3D 02 01 00 00               cmp rax, 0x102
008F3AD3  77 DF                           ja 0x1408f3ab4
008F3AD5  49 8B D5                        mov rdx, r13
008F3AD8  0F B7 02                        movzx eax, word ptr [rdx]
008F3ADB  66 85 C0                        test ax, ax
008F3ADE  0F 84 ED FD FF FF               je 0x1408f38d1
008F3AE4  66 83 F8 5C                     cmp ax, 0x5c
008F3AE8  0F 84 E1 01 00 00               je 0x1408f3ccf
008F3AEE  66 83 F8 2F                     cmp ax, 0x2f
008F3AF2  0F 84 D7 01 00 00               je 0x1408f3ccf
008F3AF8  48 83 C2 02                     add rdx, 2
008F3AFC  EB DA                           jmp 0x1408f3ad8
008F3AFE  66 C7 02 23 00                  mov word ptr [rdx], 0x23
008F3B03  EB 8B                           jmp 0x1408f3a90
008F3B05  4D 85 FF                        test r15, r15
008F3B08  74 91                           je 0x1408f3a9b
008F3B0A  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
008F3B0E  48 8B 7D 40                     mov rdi, qword ptr [rbp + 0x40]
008F3B12  48 85 F6                        test rsi, rsi
008F3B15  0F 84 FD 00 00 00               je 0x1408f3c18
008F3B1B  48 81 FF FF FF FF 7F            cmp rdi, 0x7fffffff
008F3B22  0F 87 F9 00 00 00               ja 0x1408f3c21
008F3B28  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
008F3B2C  4C 8B CE                        mov r9, rsi
008F3B2F  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
008F3B33  4C 8B C7                        mov r8, rdi
008F3B36  48 85 FF                        test rdi, rdi
008F3B39  0F 84 41 01 00 00               je 0x1408f3c80
008F3B3F  4C 2B E7                        sub r12, rdi
008F3B42  4C 8D 0D 47 8E 20 00            lea r9, [rip + 0x208e47]
008F3B49  4C 2B CE                        sub r9, rsi
008F3B4C  48 8B D7                        mov rdx, rdi
008F3B4F  48 8B CE                        mov rcx, rsi
008F3B52  4D 8B C2                        mov r8, r10
008F3B55  4A 8D 04 22                     lea rax, [rdx + r12]
008F3B59  48 85 C0                        test rax, rax
008F3B5C  74 1A                           je 0x1408f3b78
008F3B5E  42 0F B7 04 09                  movzx eax, word ptr [rcx + r9]
008F3B63  66 85 C0                        test ax, ax
008F3B66  74 10                           je 0x1408f3b78
008F3B68  66 89 01                        mov word ptr [rcx], ax
008F3B6B  49 FF C0                        inc r8
008F3B6E  48 83 C1 02                     add rcx, 2
008F3B72  48 83 EA 01                     sub rdx, 1
008F3B76  75 DD                           jne 0x1408f3b55
008F3B78  48 85 D2                        test rdx, rdx
008F3B7B  48 8D 41 FE                     lea rax, [rcx - 2]
008F3B7F  48 0F 45 C1                     cmovne rax, rcx
008F3B83  49 8D 48 FF                     lea rcx, [r8 - 1]
008F3B87  49 0F 45 C8                     cmovne rcx, r8
008F3B8B  4C 8B C7                        mov r8, rdi
008F3B8E  66 44 89 10                     mov word ptr [rax], r10w
008F3B92  48 8B C2                        mov rax, rdx
008F3B95  48 F7 D8                        neg rax
008F3B98  4C 8D 0C 4E                     lea r9, [rsi + rcx*2]
008F3B9C  4C 89 4D 40                     mov qword ptr [rbp + 0x40], r9
008F3BA0  1B DB                           sbb ebx, ebx
008F3BA2  4C 2B C1                        sub r8, rcx
008F3BA5  F7 D3                           not ebx
008F3BA7  4C 89 45 F0                     mov qword ptr [rbp - 0x10], r8
008F3BAB  81 E3 05 00 00 80               and ebx, 0x80000005
008F3BB1  48 85 D2                        test rdx, rdx
008F3BB4  0F 84 D6 00 00 00               je 0x1408f3c90
008F3BBA  49 8B F1                        mov rsi, r9
008F3BBD  49 8B F8                        mov rdi, r8
008F3BC0  8B C3                           mov eax, ebx
008F3BC2  85 DB                           test ebx, ebx
008F3BC4  0F 88 D1 FE FF FF               js 0x1408f3a9b
008F3BCA  48 8D 45 40                     lea rax, [rbp + 0x40]
008F3BCE  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
008F3BD6  4C 8D 4D E0                     lea r9, [rbp - 0x20]
008F3BDA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F3BDF  4D 8B C5                        mov r8, r13
008F3BE2  48 8B D7                        mov rdx, rdi
008F3BE5  48 8B CE                        mov rcx, rsi
008F3BE8  E8 D3 A5 B2 FF                  call 0x14041e1c0
008F3BED  E9 A9 FE FF FF                  jmp 0x1408f3a9b
008F3BF2  48 85 FF                        test rdi, rdi
008F3BF5  0F 84 90 FD FF FF               je 0x1408f398b
008F3BFB  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F3C00  33 C9                           xor ecx, ecx
008F3C02  8B F3                           mov esi, ebx
008F3C04  8B C3                           mov eax, ebx
008F3C06  48 85 FF                        test rdi, rdi
008F3C09  0F 84 30 FE FF FF               je 0x1408f3a3f
008F3C0F  66 41 89 0E                     mov word ptr [r14], cx
008F3C13  E9 83 FE FF FF                  jmp 0x1408f3a9b
008F3C18  48 85 FF                        test rdi, rdi
008F3C1B  0F 84 FA FE FF FF               je 0x1408f3b1b
008F3C21  8B C3                           mov eax, ebx
008F3C23  48 85 FF                        test rdi, rdi
008F3C26  74 98                           je 0x1408f3bc0
008F3C28  66 44 89 16                     mov word ptr [rsi], r10w
008F3C2C  E9 6A FE FF FF                  jmp 0x1408f3a9b
008F3C31  49 8B C6                        mov rax, r14
008F3C34  48 F7 D8                        neg rax
008F3C37  1B F6                           sbb esi, esi
008F3C39  81 E6 F8 FF FF BF               and esi, 0xbffffff8
008F3C3F  03 F3                           add esi, ebx
008F3C41  48 85 FF                        test rdi, rdi
008F3C44  74 29                           je 0x1408f3c6f
008F3C46  48 8D 45 F0                     lea rax, [rbp - 0x10]
008F3C4A  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
008F3C52  48 8D 14 3F                     lea rdx, [rdi + rdi]
008F3C56  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F3C5B  4C 8D 4D E8                     lea r9, [rbp - 0x18]
008F3C5F  49 8B CE                        mov rcx, r14
008F3C62  E8 89 A7 B2 FF                  call 0x14041e3f0
008F3C67  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
008F3C6B  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
008F3C6F  81 FE 05 00 00 80               cmp esi, 0x80000005
008F3C75  0F 85 C4 FD FF FF               jne 0x1408f3a3f
008F3C7B  E9 B1 FD FF FF                  jmp 0x1408f3a31
008F3C80  48 8B C6                        mov rax, rsi
008F3C83  48 F7 D8                        neg rax
008F3C86  1B C9                           sbb ecx, ecx
008F3C88  81 E1 F8 FF FF BF               and ecx, 0xbffffff8
008F3C8E  03 D9                           add ebx, ecx
008F3C90  48 85 FF                        test rdi, rdi
008F3C93  74 29                           je 0x1408f3cbe
008F3C95  48 8D 45 F0                     lea rax, [rbp - 0x10]
008F3C99  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
008F3CA1  48 8D 14 3F                     lea rdx, [rdi + rdi]
008F3CA5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F3CAA  4C 8D 4D 40                     lea r9, [rbp + 0x40]
008F3CAE  48 8B CE                        mov rcx, rsi
008F3CB1  E8 3A A7 B2 FF                  call 0x14041e3f0
008F3CB6  4C 8B 4D 40                     mov r9, qword ptr [rbp + 0x40]
008F3CBA  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
008F3CBE  81 FB 05 00 00 80               cmp ebx, 0x80000005
008F3CC4  0F 85 F6 FE FF FF               jne 0x1408f3bc0
008F3CCA  E9 EB FE FF FF                  jmp 0x1408f3bba
008F3CCF  B8 33 00 00 C0                  mov eax, 0xc0000033
008F3CD4  E9 C2 FD FF FF                  jmp 0x1408f3a9b
008F3CD9  B8 23 00 00 C0                  mov eax, 0xc0000023
008F3CDE  E9 B8 FD FF FF                  jmp 0x1408f3a9b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmGetDeviceInterfaceName(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    v_rsi = 0;
    v_stack_m58 = 0;
    v_stack_p8 = 0;
    result = PnpIsValidGuidString(a2, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008F3AB4;
    result = CmValidateDeviceName(a2, a3, a3, a4);
    if (sign_flag) goto loc_008F3AB4;
    a1 = (a2) | (-1);
    if (a4 != 0) goto loc_008F3ABB;
loc_008F38D1:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(a3 + a1 * 2)) != 0) goto loc_008F38D1;
    a1 = (a1) + (44);
    result = 0 + 2;
    if (0 == 0) { result = a1; }
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_008F3A96;
    if (a8 != 0) {
        *(unsigned int *)(a8) = (unsigned int)(result);
    }
    if (((unsigned int)(result)) > a7) goto loc_008F3CD9;
    a3 = v_rip + 2153088;
    if (a5 == 0) { a3 = v_rip + 2202570; }
    v_stack_m60 = (unsigned int)((unsigned int)(0x900ULL));
    v_stack_m68 = v_stack_p8;
    result = RtlStringCchCopyExW(a6, (unsigned int)(a7), a3, v_stack_m58);
    if (sign_flag) goto loc_008F3A9B;
    v_stack_m60 = (unsigned int)((unsigned int)(0x900ULL));
    v_stack_m68 = v_stack_p8;
    result = RtlStringCchCopyExW(v_stack_m58, v_stack_p8, a3, v_stack_m58);
    if (sign_flag) goto loc_008F3A9B;
    if (v_stack_m58 == 0) goto loc_008F3BF2;
loc_008F398B:
    if (v_stack_p8 > 0x7FFFFFFFULL) goto loc_008F3BFB;
    v_stack_m50 = v_stack_m58;
    v_stack_m48 = v_stack_p8;
    if (v_stack_p8 == 0) goto loc_008F3C31;
    a3 = ((unsigned int)(0x7FFFFFFEULL)) - (v_stack_p8);
    a4 = (v_rip + 2138754) - (v_stack_m58);
loc_008F39CD:
    if (v_stack_p8 + a3 * 1 == 0) goto loc_008F39F0;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + a4 * 1)) == 0) goto loc_008F39F0;
    *(unsigned __int16 *)(v_stack_m58) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + a4 * 1));
    v_r10 = (0) + 1;
    a1 = (v_stack_m58) + (2);
    a2 = (v_stack_p8) - (1);
    if (condition_is_not_equal) goto loc_008F39CD;
loc_008F39F0:
    result = a1 - 2;
    if (a2 != 0) { result = a1; }
    a1 = v_r10 - 1;
    if (a2 != 0) { a1 = v_r10; }
    *(unsigned __int16 *)(result) = 0;
    result = -(a2);
    v_stack_m50 = v_stack_m58 + a1 * 2;
    a3 = (v_stack_p8) - (a1);
    v_rsi = (unsigned int)(~(v_rsi));
    v_stack_m48 = a3;
    v_rsi = (unsigned int)((v_rsi) & (0x80000005ULL));
    if (a2 == 0) goto loc_008F3C41;
loc_008F3A31:
    v_stack_m58 = v_stack_m58 + a1 * 2;
    v_stack_p8 = a3;
loc_008F3A3F:
    if (sign_flag) goto loc_008F3A9B;
    v_stack_m60 = 0x900ULL;
    v_stack_m68 = v_stack_p8;
    result = RtlStringCchCopyExW(v_stack_m58 + a1 * 2, a3, v_stack_p10, v_stack_m58);
    v_r10 = 0;
    if (sign_flag) goto loc_008F3A9B;
    a2 = (a6) + (8);
loc_008F3A78:
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_008F3B05;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) == 92) goto loc_008F3AFE;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) == 47) goto loc_008F3AFE;
loc_008F3A90:
    a2 = (a2) + (2);
    goto loc_008F3A78;
loc_008F3A96:
loc_008F3A9B:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xC0000095ULL);
loc_008F3AB4:
    goto loc_008F3A9B;
loc_008F3ABB:
loc_008F3ABE:
    v_r15 = (*(unsigned __int16 *)(a2)) + 1;
    if ((*(unsigned __int16 *)(a4 + v_r15 * 2)) != ((unsigned __int16)(v_rsi))) goto loc_008F3ABE;
    if ((v_r15 - 1) > 258) goto loc_008F3AB4;
loc_008F3AD8:
    if ((unsigned __int16)(*(unsigned __int16 *)(a4)) == 0) goto loc_008F38D1;
    if (((unsigned __int16)(*(unsigned __int16 *)(a4))) == 92) goto loc_008F3CCF;
    if (((unsigned __int16)(*(unsigned __int16 *)(a4))) == 47) goto loc_008F3CCF;
    a2 = (a4) + (2);
    goto loc_008F3AD8;
loc_008F3AFE:
    *(unsigned __int16 *)(a2) = 35;
    goto loc_008F3A90;
loc_008F3B05:
    if (v_r15 == 0) goto loc_008F3A9B;
    if (v_stack_m58 == 0) goto loc_008F3C18;
loc_008F3B1B:
    if (v_stack_p8 > 0x7FFFFFFFULL) goto loc_008F3C21;
    v_stack_p8 = v_stack_m58;
    v_stack_m48 = v_stack_p8;
    if (v_stack_p8 == 0) goto loc_008F3C80;
    v_r12 = ((unsigned int)(0x7FFFFFFEULL)) - (v_stack_p8);
    a4 = (v_rip + 2133575) - (v_stack_m58);
loc_008F3B55:
    if (v_stack_p8 + v_r12 * 1 == 0) goto loc_008F3B78;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + a4 * 1)) == 0) goto loc_008F3B78;
    *(unsigned __int16 *)(v_stack_m58) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + a4 * 1));
    a3 = (0) + 1;
    a1 = (v_stack_m58) + (2);
    a2 = (v_stack_p8) - (1);
    if (condition_is_not_equal) goto loc_008F3B55;
loc_008F3B78:
    result = a1 - 2;
    if (a2 != 0) { result = a1; }
    a1 = a3 - 1;
    if (a2 != 0) { a1 = a3; }
    *(unsigned __int16 *)(result) = 0;
    result = -(a2);
    v_stack_p8 = v_stack_m58 + a1 * 2;
    a3 = (v_stack_p8) - (a1);
    v_rbx = (unsigned int)(~(v_stack_p18));
    v_stack_m48 = a3;
    v_rbx = (unsigned int)((v_rbx) & (0x80000005ULL));
    if (a2 == 0) goto loc_008F3C90;
loc_008F3BBA:
loc_008F3BC0:
    if (sign_flag) goto loc_008F3A9B;
    v_stack_p28 = 0x900ULL;
    v_stack_p20 = v_stack_p8;
    result = RtlStringCchCopyExW(v_stack_m58 + a1 * 2, a3, a4, v_stack_m58);
    goto loc_008F3A9B;
loc_008F3BF2:
    if (a3 == 0) goto loc_008F398B;
loc_008F3BFB:
    a1 = 0;
    if (a3 == 0) goto loc_008F3A3F;
    *(unsigned __int16 *)(v_stack_m58 + a1 * 2) = 0;
    goto loc_008F3A9B;
loc_008F3C18:
    if (a3 == 0) goto loc_008F3B1B;
loc_008F3C21:
    if (a3 == 0) goto loc_008F3BC0;
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))) = 0;
    goto loc_008F3A9B;
loc_008F3C31:
    result = -(v_stack_m58 + a1 * 2);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))) & (0xBFFFFFF8ULL));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)((unsigned int)(0xC000000DULL))));
loc_008F3C41:
    if (a3 != 0) {
        result = v_stack_m48;
        v_stack_p28 = 0x900ULL;
        a2 = a3 + a3 * 1;
        v_stack_p20 = result;
        a4 = v_stack_m50;
        a1 = v_stack_m58 + a1 * 2;
        result = RtlStringExHandleOtherFlagsW(a1, a2, a4, a4);
        a4 = v_stack_m50;
        a3 = v_stack_m48;
    }
    if (((unsigned int)(v_rsi)) != 0x80000005ULL) goto loc_008F3A3F;
    goto loc_008F3A31;
loc_008F3C80:
    result = -(v_rsi);
    a1 = (unsigned int)((a1) & (0xBFFFFFF8ULL));
    v_rbx = (unsigned int)(((unsigned int)(0xC000000DULL)) + ((unsigned int)(a1)));
loc_008F3C90:
    if (a3 != 0) {
        result = v_stack_m48;
        v_stack_p28 = 0x900ULL;
        a2 = a3 + a3 * 1;
        v_stack_p20 = result;
        a4 = v_stack_p8;
        a1 = v_rsi;
        result = RtlStringExHandleOtherFlagsW(a1, a2, a3, a4);
        a4 = v_stack_p8;
        a3 = v_stack_m48;
    }
    if (((unsigned int)(v_rbx)) != 0x80000005ULL) goto loc_008F3BC0;
    goto loc_008F3BBA;
loc_008F3CCF:
    goto loc_008F3A9B;
loc_008F3CD9:
    goto loc_008F3A9B;
}
```

## 5. (Beta) C Style

```c
int64_t CmGetDeviceInterfaceName(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, uint8_t Arg5, void *Arg6, uint32_t Arg7, int64_t Arg8)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    local_rsi = 0;
    v_stack_m58 = 0;
    v_stack_p8 = 0;
    result = PnpIsValidGuidString(Arg2, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008F3AB4;
    result = CmValidateDeviceName(Arg2, Arg3, Arg3, Arg4);
    if (sign_flag) goto loc_008F3AB4;
    Arg1 = (Arg2) | (-1);
    if (Arg4 != 0) goto loc_008F3ABB;
loc_008F38D1:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(arg3 + Arg1 * 2)) != 0) goto loc_008F38D1;
    Arg1 = (Arg1) + (44);
    result = 0 + 2;
    if (0 == 0) { result = Arg1; }
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_008F3A96;
    if (Arg8 != 0) {
        *(uint32_t *)(Arg8) = (uint32_t)(result);
    }
    if (((uint32_t)(result)) > Arg7) goto loc_008F3CD9;
    Arg3 = v_rip + 2153088;
    if (Arg5 == 0) { Arg3 = v_rip + 2202570; }
    v_stack_m60 = (uint32_t)((uint32_t)(0x900ULL));
    v_stack_m68 = v_stack_p8;
    result = RtlStringCchCopyExW(Arg6, (uint32_t)(Arg7), Arg3, v_stack_m58);
    if (sign_flag) goto loc_008F3A9B;
    v_stack_m60 = (uint32_t)((uint32_t)(0x900ULL));
    v_stack_m68 = v_stack_p8;
    result = RtlStringCchCopyExW(v_stack_m58, v_stack_p8, Arg3, v_stack_m58);
    if (sign_flag) goto loc_008F3A9B;
    if (v_stack_m58 == 0) goto loc_008F3BF2;
loc_008F398B:
    if (v_stack_p8 > 0x7FFFFFFFULL) goto loc_008F3BFB;
    v_stack_m50 = v_stack_m58;
    v_stack_m48 = v_stack_p8;
    if (v_stack_p8 == 0) goto loc_008F3C31;
    Arg3 = ((uint32_t)(0x7FFFFFFEULL)) - (v_stack_p8);
    Arg4 = (v_rip + 2138754) - (v_stack_m58);
loc_008F39CD:
    if (v_stack_p8 + Arg3 * 1 == 0) goto loc_008F39F0;
    if ((uint16_t)(*(uint16_t *)(v_stack_m58 + Arg4 * 1)) == 0) goto loc_008F39F0;
    *(uint16_t *)(v_stack_m58) = (uint16_t)(*(uint16_t *)(v_stack_m58 + Arg4 * 1));
    local_r10 = (0) + 1;
    Arg1 = (v_stack_m58) + (2);
    Arg2 = (v_stack_p8) - (1);
    if (condition_is_not_equal) goto loc_008F39CD;
loc_008F39F0:
    result = Arg1 - 2;
    if (Arg2 != 0) { result = Arg1; }
    Arg1 = local_r10 - 1;
    if (Arg2 != 0) { Arg1 = local_r10; }
    *(uint16_t *)(result) = 0;
    result = -(Arg2);
    v_stack_m50 = v_stack_m58 + Arg1 * 2;
    Arg3 = (v_stack_p8) - (Arg1);
    local_rsi = (uint32_t)(~(local_rsi));
    v_stack_m48 = Arg3;
    local_rsi = (uint32_t)((local_rsi) & (0x80000005ULL));
    if (Arg2 == 0) goto loc_008F3C41;
loc_008F3A31:
    v_stack_m58 = v_stack_m58 + Arg1 * 2;
    v_stack_p8 = Arg3;
loc_008F3A3F:
    if (sign_flag) goto loc_008F3A9B;
    v_stack_m60 = 0x900ULL;
    v_stack_m68 = v_stack_p8;
    result = RtlStringCchCopyExW(v_stack_m58 + Arg1 * 2, Arg3, v_stack_p10, v_stack_m58);
    local_r10 = 0;
    if (sign_flag) goto loc_008F3A9B;
    Arg2 = (Arg6) + (8);
loc_008F3A78:
    if ((uint16_t)(*(uint16_t *)(Arg2)) == 0) goto loc_008F3B05;
    if (((uint16_t)(*(uint16_t *)(Arg2))) == 92) goto loc_008F3AFE;
    if (((uint16_t)(*(uint16_t *)(Arg2))) == 47) goto loc_008F3AFE;
loc_008F3A90:
    Arg2 = (Arg2) + (2);
    goto loc_008F3A78;
loc_008F3A96:
loc_008F3A9B:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xC0000095ULL);
loc_008F3AB4:
    goto loc_008F3A9B;
loc_008F3ABB:
loc_008F3ABE:
    local_r15 = (*(uint16_t *)(Arg2)) + 1;
    if ((*(uint16_t *)(Arg4 + local_r15 * 2)) != ((uint16_t)(local_rsi))) goto loc_008F3ABE;
    if ((local_r15 - 1) > 258) goto loc_008F3AB4;
loc_008F3AD8:
    if ((uint16_t)(*(uint16_t *)(Arg4)) == 0) goto loc_008F38D1;
    if (((uint16_t)(*(uint16_t *)(Arg4))) == 92) goto loc_008F3CCF;
    if (((uint16_t)(*(uint16_t *)(Arg4))) == 47) goto loc_008F3CCF;
    Arg2 = (Arg4) + (2);
    goto loc_008F3AD8;
loc_008F3AFE:
    *(uint16_t *)(Arg2) = 35;
    goto loc_008F3A90;
loc_008F3B05:
    if (local_r15 == 0) goto loc_008F3A9B;
    if (v_stack_m58 == 0) goto loc_008F3C18;
loc_008F3B1B:
    if (v_stack_p8 > 0x7FFFFFFFULL) goto loc_008F3C21;
    v_stack_p8 = v_stack_m58;
    v_stack_m48 = v_stack_p8;
    if (v_stack_p8 == 0) goto loc_008F3C80;
    local_r12 = ((uint32_t)(0x7FFFFFFEULL)) - (v_stack_p8);
    Arg4 = (v_rip + 2133575) - (v_stack_m58);
loc_008F3B55:
    if (v_stack_p8 + local_r12 * 1 == 0) goto loc_008F3B78;
    if ((uint16_t)(*(uint16_t *)(v_stack_m58 + Arg4 * 1)) == 0) goto loc_008F3B78;
    *(uint16_t *)(v_stack_m58) = (uint16_t)(*(uint16_t *)(v_stack_m58 + Arg4 * 1));
    Arg3 = (0) + 1;
    Arg1 = (v_stack_m58) + (2);
    Arg2 = (v_stack_p8) - (1);
    if (condition_is_not_equal) goto loc_008F3B55;
loc_008F3B78:
    result = Arg1 - 2;
    if (Arg2 != 0) { result = Arg1; }
    Arg1 = Arg3 - 1;
    if (Arg2 != 0) { Arg1 = Arg3; }
    *(uint16_t *)(result) = 0;
    result = -(Arg2);
    v_stack_p8 = v_stack_m58 + Arg1 * 2;
    Arg3 = (v_stack_p8) - (Arg1);
    local_rbx = (uint32_t)(~(v_stack_p18));
    v_stack_m48 = Arg3;
    local_rbx = (uint32_t)((local_rbx) & (0x80000005ULL));
    if (Arg2 == 0) goto loc_008F3C90;
loc_008F3BBA:
loc_008F3BC0:
    if (sign_flag) goto loc_008F3A9B;
    v_stack_p28 = 0x900ULL;
    v_stack_p20 = v_stack_p8;
    result = RtlStringCchCopyExW(v_stack_m58 + Arg1 * 2, Arg3, Arg4, v_stack_m58);
    goto loc_008F3A9B;
loc_008F3BF2:
    if (Arg3 == NULL) goto loc_008F398B;
loc_008F3BFB:
    Arg1 = 0;
    if (Arg3 == NULL) goto loc_008F3A3F;
    *(uint16_t *)(v_stack_m58 + Arg1 * 2) = 0;
    goto loc_008F3A9B;
loc_008F3C18:
    if (Arg3 == NULL) goto loc_008F3B1B;
loc_008F3C21:
    if (Arg3 == NULL) goto loc_008F3BC0;
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))) = 0;
    goto loc_008F3A9B;
loc_008F3C31:
    result = -(v_stack_m58 + Arg1 * 2);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))) & (0xBFFFFFF8ULL));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)((uint32_t)(0xC000000DULL))));
loc_008F3C41:
    if (Arg3 != NULL) {
        result = v_stack_m48;
        v_stack_p28 = 0x900ULL;
        Arg2 = Arg3 + Arg3 * 1;
        v_stack_p20 = result;
        Arg4 = v_stack_m50;
        Arg1 = v_stack_m58 + Arg1 * 2;
        result = RtlStringExHandleOtherFlagsW(Arg1, Arg2, Arg4, Arg4);
        Arg4 = v_stack_m50;
        Arg3 = v_stack_m48;
    }
    if (((uint32_t)(local_rsi)) != 0x80000005ULL) goto loc_008F3A3F;
    goto loc_008F3A31;
loc_008F3C80:
    result = -(local_rsi);
    Arg1 = (uint32_t)((Arg1) & (0xBFFFFFF8ULL));
    local_rbx = (uint32_t)(((uint32_t)(0xC000000DULL)) + ((uint32_t)(Arg1)));
loc_008F3C90:
    if (Arg3 != NULL) {
        result = v_stack_m48;
        v_stack_p28 = 0x900ULL;
        Arg2 = Arg3 + Arg3 * 1;
        v_stack_p20 = result;
        Arg4 = v_stack_p8;
        Arg1 = local_rsi;
        result = RtlStringExHandleOtherFlagsW(Arg1, Arg2, Arg3, Arg4);
        Arg4 = v_stack_p8;
        Arg3 = v_stack_m48;
    }
    if (((uint32_t)(local_rbx)) != 0x80000005ULL) goto loc_008F3BC0;
    goto loc_008F3BBA;
loc_008F3CCF:
    goto loc_008F3A9B;
loc_008F3CD9:
    goto loc_008F3A9B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + rcx*2` | `16` | `R` |
| `Arg6` | `+ 0x0` | `16` | `R` |
| `Arg6` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F3870&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
