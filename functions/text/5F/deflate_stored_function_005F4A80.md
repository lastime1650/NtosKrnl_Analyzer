# deflate_stored

- RVA: `0x005F4A80`–`0x005F4EE8` (길이 `1,128` bytes)
- VA: `0x00000001405F4A80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005D79C`
- 디코드: `305`개 명령, `1,128/1,128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005F4B55` → [tr_stored_block](../60/tr_stored_block_function_00600DC0.md) (function, `0x00600DC0`)
- `0x005F4BA2` → [flush_pending](flush_pending_function_005F5258.md) (function, `0x005F5258`)
- `0x005F4BCE` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F4C00` → [read_buf](read_buf_function_005F555C.md) (function, `0x005F555C`)
- `0x005F4C59` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F4C98` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F4CD7` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F4D99` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F4DE4` → [read_buf](read_buf_function_005F555C.md) (function, `0x005F555C`)
- `0x005F4EB4` → [tr_stored_block](../60/tr_stored_block_function_00600DC0.md) (function, `0x00600DC0`)
- `0x005F4EBE` → [flush_pending](flush_pending_function_005F5258.md) (function, `0x005F5258`)

### Direct callers
- [deflate](deflate_function_005F35C8.md) at `0x005F37B4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F4A80  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005F4A85  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
005F4A8A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
005F4A8F  57                              push rdi
005F4A90  41 54                           push r12
005F4A92  41 55                           push r13
005F4A94  41 56                           push r14
005F4A96  41 57                           push r15
005F4A98  48 83 EC 20                     sub rsp, 0x20
005F4A9C  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
005F4A9F  44 8B E2                        mov r12d, edx
005F4AA2  44 8B A9 94 00 00 00            mov r13d, dword ptr [rcx + 0x94]
005F4AA9  83 C0 FB                        add eax, -5
005F4AAC  41 3B C5                        cmp eax, r13d
005F4AAF  48 8B F9                        mov rdi, rcx
005F4AB2  44 0F 46 E8                     cmovbe r13d, eax
005F4AB6  48 8B 01                        mov rax, qword ptr [rcx]
005F4AB9  33 ED                           xor ebp, ebp
005F4ABB  44 8B 78 08                     mov r15d, dword ptr [rax + 8]
005F4ABF  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
005F4AC4  41 BF FF FF 00 00               mov r15d, 0xffff
005F4ACA  8B 87 60 17 00 00               mov eax, dword ptr [rdi + 0x1760]
005F4AD0  48 8B 17                        mov rdx, qword ptr [rdi]
005F4AD3  83 C0 2A                        add eax, 0x2a
005F4AD6  C1 F8 03                        sar eax, 3
005F4AD9  8B 4A 18                        mov ecx, dword ptr [rdx + 0x18]
005F4ADC  3B C8                           cmp ecx, eax
005F4ADE  0F 82 3E 01 00 00               jb 0x1405f4c22
005F4AE4  44 8B B7 E4 00 00 00            mov r14d, dword ptr [rdi + 0xe4]
005F4AEB  2B C8                           sub ecx, eax
005F4AED  44 2B B7 D4 00 00 00            sub r14d, dword ptr [rdi + 0xd4]
005F4AF4  41 8B F7                        mov esi, r15d
005F4AF7  8B 52 08                        mov edx, dword ptr [rdx + 8]
005F4AFA  42 8D 04 32                     lea eax, [rdx + r14]
005F4AFE  41 3B C7                        cmp eax, r15d
005F4B01  0F 42 F0                        cmovb esi, eax
005F4B04  3B F1                           cmp esi, ecx
005F4B06  0F 47 F1                        cmova esi, ecx
005F4B09  41 3B F5                        cmp esi, r13d
005F4B0C  73 25                           jae 0x1405f4b33
005F4B0E  85 F6                           test esi, esi
005F4B10  75 0C                           jne 0x1405f4b1e
005F4B12  41 83 FC 04                     cmp r12d, 4
005F4B16  0F 85 06 01 00 00               jne 0x1405f4c22
005F4B1C  EB 09                           jmp 0x1405f4b27
005F4B1E  45 85 E4                        test r12d, r12d
005F4B21  0F 84 FB 00 00 00               je 0x1405f4c22
005F4B27  42 8D 04 32                     lea eax, [rdx + r14]
005F4B2B  3B F0                           cmp esi, eax
005F4B2D  0F 85 EF 00 00 00               jne 0x1405f4c22
005F4B33  41 83 FC 04                     cmp r12d, 4
005F4B37  75 0F                           jne 0x1405f4b48
005F4B39  42 8D 04 32                     lea eax, [rdx + r14]
005F4B3D  3B F0                           cmp esi, eax
005F4B3F  75 07                           jne 0x1405f4b48
005F4B41  41 8D 6C 24 FD                  lea ebp, [r12 - 3]
005F4B46  EB 02                           jmp 0x1405f4b4a
005F4B48  33 ED                           xor ebp, ebp
005F4B4A  44 8B CD                        mov r9d, ebp
005F4B4D  45 33 C0                        xor r8d, r8d
005F4B50  33 D2                           xor edx, edx
005F4B52  48 8B CF                        mov rcx, rdi
005F4B55  E8 66 C2 00 00                  call 0x140600dc0
005F4B5A  8B 4F 28                        mov ecx, dword ptr [rdi + 0x28]
005F4B5D  8B D6                           mov edx, esi
005F4B5F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
005F4B63  83 E9 04                        sub ecx, 4
005F4B66  C1 EA 08                        shr edx, 8
005F4B69  40 88 34 01                     mov byte ptr [rcx + rax], sil
005F4B6D  8B 4F 28                        mov ecx, dword ptr [rdi + 0x28]
005F4B70  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
005F4B74  83 E9 03                        sub ecx, 3
005F4B77  88 14 01                        mov byte ptr [rcx + rax], dl
005F4B7A  40 8A D6                        mov dl, sil
005F4B7D  8B 4F 28                        mov ecx, dword ptr [rdi + 0x28]
005F4B80  F6 D2                           not dl
005F4B82  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
005F4B86  83 E9 02                        sub ecx, 2
005F4B89  88 14 01                        mov byte ptr [rcx + rax], dl
005F4B8C  8B D6                           mov edx, esi
005F4B8E  8B 4F 28                        mov ecx, dword ptr [rdi + 0x28]
005F4B91  F7 D2                           not edx
005F4B93  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
005F4B97  FF C9                           dec ecx
005F4B99  C1 EA 08                        shr edx, 8
005F4B9C  88 14 01                        mov byte ptr [rcx + rax], dl
005F4B9F  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4BA2  E8 B1 06 00 00                  call 0x1405f5258
005F4BA7  45 85 F6                        test r14d, r14d
005F4BAA  74 46                           je 0x1405f4bf2
005F4BAC  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4BAF  44 3B F6                        cmp r14d, esi
005F4BB2  48 63 97 D4 00 00 00            movsxd rdx, dword ptr [rdi + 0xd4]
005F4BB9  44 0F 47 F6                     cmova r14d, esi
005F4BBD  48 03 97 A0 00 00 00            add rdx, qword ptr [rdi + 0xa0]
005F4BC4  45 8B C6                        mov r8d, r14d
005F4BC7  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
005F4BCB  41 8B DE                        mov ebx, r14d
005F4BCE  E8 6D 1C 0D 00                  call 0x1406c6840
005F4BD3  48 8B 07                        mov rax, qword ptr [rdi]
005F4BD6  48 01 58 10                     add qword ptr [rax + 0x10], rbx
005F4BDA  48 8B 07                        mov rax, qword ptr [rdi]
005F4BDD  44 29 70 18                     sub dword ptr [rax + 0x18], r14d
005F4BE1  48 8B 07                        mov rax, qword ptr [rdi]
005F4BE4  44 01 70 1C                     add dword ptr [rax + 0x1c], r14d
005F4BE8  44 01 B7 D4 00 00 00            add dword ptr [rdi + 0xd4], r14d
005F4BEF  41 2B F6                        sub esi, r14d
005F4BF2  85 F6                           test esi, esi
005F4BF4  74 24                           je 0x1405f4c1a
005F4BF6  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4BF9  44 8B C6                        mov r8d, esi
005F4BFC  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
005F4C00  E8 57 09 00 00                  call 0x1405f555c
005F4C05  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4C08  8B C6                           mov eax, esi
005F4C0A  48 01 41 10                     add qword ptr [rcx + 0x10], rax
005F4C0E  48 8B 07                        mov rax, qword ptr [rdi]
005F4C11  29 70 18                        sub dword ptr [rax + 0x18], esi
005F4C14  48 8B 07                        mov rax, qword ptr [rdi]
005F4C17  01 70 1C                        add dword ptr [rax + 0x1c], esi
005F4C1A  85 ED                           test ebp, ebp
005F4C1C  0F 84 A8 FE FF FF               je 0x1405f4aca
005F4C22  48 8B 07                        mov rax, qword ptr [rdi]
005F4C25  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
005F4C2A  44 2B 78 08                     sub r15d, dword ptr [rax + 8]
005F4C2E  0F 84 DA 00 00 00               je 0x1405f4d0e
005F4C34  8B 97 94 00 00 00               mov edx, dword ptr [rdi + 0x94]
005F4C3A  44 3B FA                        cmp r15d, edx
005F4C3D  72 30                           jb 0x1405f4c6f
005F4C3F  48 8B 8F A0 00 00 00            mov rcx, qword ptr [rdi + 0xa0]
005F4C46  44 8B C2                        mov r8d, edx
005F4C49  C7 87 54 17 00 00 02 00 00 00   mov dword ptr [rdi + 0x1754], 2
005F4C53  48 8B 10                        mov rdx, qword ptr [rax]
005F4C56  49 2B D0                        sub rdx, r8
005F4C59  E8 E2 1B 0D 00                  call 0x1406c6840
005F4C5E  8B 87 94 00 00 00               mov eax, dword ptr [rdi + 0x94]
005F4C64  89 87 E4 00 00 00               mov dword ptr [rdi + 0xe4], eax
005F4C6A  E9 8D 00 00 00                  jmp 0x1405f4cfc
005F4C6F  8B 8F E4 00 00 00               mov ecx, dword ptr [rdi + 0xe4]
005F4C75  8B 87 A8 00 00 00               mov eax, dword ptr [rdi + 0xa8]
005F4C7B  2B C1                           sub eax, ecx
005F4C7D  41 3B C7                        cmp eax, r15d
005F4C80  77 42                           ja 0x1405f4cc4
005F4C82  2B CA                           sub ecx, edx
005F4C84  44 8B C1                        mov r8d, ecx
005F4C87  48 8B 8F A0 00 00 00            mov rcx, qword ptr [rdi + 0xa0]
005F4C8E  48 03 D1                        add rdx, rcx
005F4C91  44 89 87 E4 00 00 00            mov dword ptr [rdi + 0xe4], r8d
005F4C98  E8 A3 1B 0D 00                  call 0x1406c6840
005F4C9D  8B 87 54 17 00 00               mov eax, dword ptr [rdi + 0x1754]
005F4CA3  83 F8 02                        cmp eax, 2
005F4CA6  73 08                           jae 0x1405f4cb0
005F4CA8  FF C0                           inc eax
005F4CAA  89 87 54 17 00 00               mov dword ptr [rdi + 0x1754], eax
005F4CB0  8B 8F E4 00 00 00               mov ecx, dword ptr [rdi + 0xe4]
005F4CB6  39 8F 58 17 00 00               cmp dword ptr [rdi + 0x1758], ecx
005F4CBC  76 06                           jbe 0x1405f4cc4
005F4CBE  89 8F 58 17 00 00               mov dword ptr [rdi + 0x1758], ecx
005F4CC4  48 8B 07                        mov rax, qword ptr [rdi]
005F4CC7  48 03 8F A0 00 00 00            add rcx, qword ptr [rdi + 0xa0]
005F4CCE  45 8B C7                        mov r8d, r15d
005F4CD1  48 8B 10                        mov rdx, qword ptr [rax]
005F4CD4  49 2B D0                        sub rdx, r8
005F4CD7  E8 64 1B 0D 00                  call 0x1406c6840
005F4CDC  8B 8F 58 17 00 00               mov ecx, dword ptr [rdi + 0x1758]
005F4CE2  44 01 BF E4 00 00 00            add dword ptr [rdi + 0xe4], r15d
005F4CE9  8B 87 94 00 00 00               mov eax, dword ptr [rdi + 0x94]
005F4CEF  2B C1                           sub eax, ecx
005F4CF1  44 3B F8                        cmp r15d, eax
005F4CF4  44 0F 47 F8                     cmova r15d, eax
005F4CF8  42 8D 04 39                     lea eax, [rcx + r15]
005F4CFC  89 87 58 17 00 00               mov dword ptr [rdi + 0x1758], eax
005F4D02  8B 87 E4 00 00 00               mov eax, dword ptr [rdi + 0xe4]
005F4D08  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
005F4D0E  44 8B 87 E4 00 00 00            mov r8d, dword ptr [rdi + 0xe4]
005F4D15  44 39 87 64 17 00 00            cmp dword ptr [rdi + 0x1764], r8d
005F4D1C  73 07                           jae 0x1405f4d25
005F4D1E  44 89 87 64 17 00 00            mov dword ptr [rdi + 0x1764], r8d
005F4D25  85 ED                           test ebp, ebp
005F4D27  74 0A                           je 0x1405f4d33
005F4D29  B8 03 00 00 00                  mov eax, 3
005F4D2E  E9 97 01 00 00                  jmp 0x1405f4eca
005F4D33  41 F7 C4 FB FF FF FF            test r12d, 0xfffffffb
005F4D3A  74 1C                           je 0x1405f4d58
005F4D3C  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4D3F  83 79 08 00                     cmp dword ptr [rcx + 8], 0
005F4D43  75 13                           jne 0x1405f4d58
005F4D45  44 3B 87 D4 00 00 00            cmp r8d, dword ptr [rdi + 0xd4]
005F4D4C  75 0A                           jne 0x1405f4d58
005F4D4E  B8 01 00 00 00                  mov eax, 1
005F4D53  E9 72 01 00 00                  jmp 0x1405f4eca
005F4D58  48 8B 07                        mov rax, qword ptr [rdi]
005F4D5B  49 8B D0                        mov rdx, r8
005F4D5E  8B 9F A8 00 00 00               mov ebx, dword ptr [rdi + 0xa8]
005F4D64  41 2B D8                        sub ebx, r8d
005F4D67  39 58 08                        cmp dword ptr [rax + 8], ebx
005F4D6A  76 5F                           jbe 0x1405f4dcb
005F4D6C  8B 87 94 00 00 00               mov eax, dword ptr [rdi + 0x94]
005F4D72  8B 8F D4 00 00 00               mov ecx, dword ptr [rdi + 0xd4]
005F4D78  3B C8                           cmp ecx, eax
005F4D7A  7C 4F                           jl 0x1405f4dcb
005F4D7C  2B C8                           sub ecx, eax
005F4D7E  44 2B C0                        sub r8d, eax
005F4D81  89 8F D4 00 00 00               mov dword ptr [rdi + 0xd4], ecx
005F4D87  48 8B 8F A0 00 00 00            mov rcx, qword ptr [rdi + 0xa0]
005F4D8E  44 89 87 E4 00 00 00            mov dword ptr [rdi + 0xe4], r8d
005F4D95  48 8D 14 01                     lea rdx, [rcx + rax]
005F4D99  E8 A2 1A 0D 00                  call 0x1406c6840
005F4D9E  8B 87 54 17 00 00               mov eax, dword ptr [rdi + 0x1754]
005F4DA4  83 F8 02                        cmp eax, 2
005F4DA7  73 08                           jae 0x1405f4db1
005F4DA9  FF C0                           inc eax
005F4DAB  89 87 54 17 00 00               mov dword ptr [rdi + 0x1754], eax
005F4DB1  03 9F 94 00 00 00               add ebx, dword ptr [rdi + 0x94]
005F4DB7  8B 97 E4 00 00 00               mov edx, dword ptr [rdi + 0xe4]
005F4DBD  39 97 58 17 00 00               cmp dword ptr [rdi + 0x1758], edx
005F4DC3  76 06                           jbe 0x1405f4dcb
005F4DC5  89 97 58 17 00 00               mov dword ptr [rdi + 0x1758], edx
005F4DCB  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4DCE  8B 71 08                        mov esi, dword ptr [rcx + 8]
005F4DD1  3B DE                           cmp ebx, esi
005F4DD3  0F 46 F3                        cmovbe esi, ebx
005F4DD6  85 F6                           test esi, esi
005F4DD8  74 39                           je 0x1405f4e13
005F4DDA  48 03 97 A0 00 00 00            add rdx, qword ptr [rdi + 0xa0]
005F4DE1  44 8B C6                        mov r8d, esi
005F4DE4  E8 73 07 00 00                  call 0x1405f555c
005F4DE9  8B 8F 58 17 00 00               mov ecx, dword ptr [rdi + 0x1758]
005F4DEF  8B 97 E4 00 00 00               mov edx, dword ptr [rdi + 0xe4]
005F4DF5  8B 87 94 00 00 00               mov eax, dword ptr [rdi + 0x94]
005F4DFB  03 D6                           add edx, esi
005F4DFD  2B C1                           sub eax, ecx
005F4DFF  89 97 E4 00 00 00               mov dword ptr [rdi + 0xe4], edx
005F4E05  3B F0                           cmp esi, eax
005F4E07  0F 47 F0                        cmova esi, eax
005F4E0A  8D 04 31                        lea eax, [rcx + rsi]
005F4E0D  89 87 58 17 00 00               mov dword ptr [rdi + 0x1758], eax
005F4E13  39 97 64 17 00 00               cmp dword ptr [rdi + 0x1764], edx
005F4E19  73 06                           jae 0x1405f4e21
005F4E1B  89 97 64 17 00 00               mov dword ptr [rdi + 0x1764], edx
005F4E21  8B 87 60 17 00 00               mov eax, dword ptr [rdi + 0x1760]
005F4E27  48 8D B7 D4 00 00 00            lea rsi, [rdi + 0xd4]
005F4E2E  8B 5F 18                        mov ebx, dword ptr [rdi + 0x18]
005F4E31  83 C0 2A                        add eax, 0x2a
005F4E34  C1 F8 03                        sar eax, 3
005F4E37  2B D8                           sub ebx, eax
005F4E39  B8 FF FF 00 00                  mov eax, 0xffff
005F4E3E  3B D8                           cmp ebx, eax
005F4E40  0F 47 D8                        cmova ebx, eax
005F4E43  2B 16                           sub edx, dword ptr [rsi]
005F4E45  8B 87 94 00 00 00               mov eax, dword ptr [rdi + 0x94]
005F4E4B  3B D8                           cmp ebx, eax
005F4E4D  0F 46 C3                        cmovbe eax, ebx
005F4E50  3B D0                           cmp edx, eax
005F4E52  73 27                           jae 0x1405f4e7b
005F4E54  85 D2                           test edx, edx
005F4E56  75 08                           jne 0x1405f4e60
005F4E58  41 83 FC 04                     cmp r12d, 4
005F4E5C  75 65                           jne 0x1405f4ec3
005F4E5E  EB 05                           jmp 0x1405f4e65
005F4E60  45 85 E4                        test r12d, r12d
005F4E63  74 5E                           je 0x1405f4ec3
005F4E65  48 8B 07                        mov rax, qword ptr [rdi]
005F4E68  83 78 08 00                     cmp dword ptr [rax + 8], 0
005F4E6C  75 55                           jne 0x1405f4ec3
005F4E6E  3B D3                           cmp edx, ebx
005F4E70  77 51                           ja 0x1405f4ec3
005F4E72  48 8D B7 D4 00 00 00            lea rsi, [rdi + 0xd4]
005F4E79  EB 04                           jmp 0x1405f4e7f
005F4E7B  3B D3                           cmp edx, ebx
005F4E7D  77 02                           ja 0x1405f4e81
005F4E7F  8B DA                           mov ebx, edx
005F4E81  41 83 FC 04                     cmp r12d, 4
005F4E85  75 14                           jne 0x1405f4e9b
005F4E87  48 8B 07                        mov rax, qword ptr [rdi]
005F4E8A  83 78 08 00                     cmp dword ptr [rax + 8], 0
005F4E8E  75 0B                           jne 0x1405f4e9b
005F4E90  3B DA                           cmp ebx, edx
005F4E92  75 07                           jne 0x1405f4e9b
005F4E94  41 8D 6C 24 FD                  lea ebp, [r12 - 3]
005F4E99  EB 02                           jmp 0x1405f4e9d
005F4E9B  33 ED                           xor ebp, ebp
005F4E9D  48 63 97 D4 00 00 00            movsxd rdx, dword ptr [rdi + 0xd4]
005F4EA4  44 8B CD                        mov r9d, ebp
005F4EA7  48 03 97 A0 00 00 00            add rdx, qword ptr [rdi + 0xa0]
005F4EAE  44 8B C3                        mov r8d, ebx
005F4EB1  48 8B CF                        mov rcx, rdi
005F4EB4  E8 07 BF 00 00                  call 0x140600dc0
005F4EB9  48 8B 0F                        mov rcx, qword ptr [rdi]
005F4EBC  01 1E                           add dword ptr [rsi], ebx
005F4EBE  E8 95 03 00 00                  call 0x1405f5258
005F4EC3  F7 DD                           neg ebp
005F4EC5  1B C0                           sbb eax, eax
005F4EC7  83 E0 02                        and eax, 2
005F4ECA  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
005F4ECF  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
005F4ED4  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
005F4ED9  48 83 C4 20                     add rsp, 0x20
005F4EDD  41 5F                           pop r15
005F4EDF  41 5E                           pop r14
005F4EE1  41 5D                           pop r13
005F4EE3  41 5C                           pop r12
005F4EE5  5F                              pop rdi
005F4EE6  C3                              ret
005F4EE7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall deflate_stored(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) + (-5));
    v_r13 = (unsigned int)(*(unsigned int *)(a1 + 148));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148))))) { v_r13 = (unsigned int)(result); }
    v_rbp = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)));
loc_005F4ACA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 5984))) + (42));
    result = (unsigned int)((result) >> (3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24)))) < ((unsigned int)(result))) goto loc_005F4C22;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24))) - ((unsigned int)(result)));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) - (*(unsigned int *)(a1 + 212)));
    v_rsi = (unsigned int)((unsigned int)((unsigned int)(0xFFFFULL)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) + v_r14 * 1)) < ((unsigned int)((unsigned int)(0xFFFFULL)))) { v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) + v_r14 * 1); }
    if (((unsigned int)(v_rsi)) > ((unsigned int)(a1))) { v_rsi = (unsigned int)(a1); }
    if (((unsigned int)(v_rsi)) >= ((unsigned int)(v_r13))) goto loc_005F4B33;
    if ((unsigned int)(v_rsi) != 0) goto loc_005F4B1E;
    if (((unsigned int)((unsigned int)(a2))) != 4) goto loc_005F4C22;
    goto loc_005F4B27;
loc_005F4B1E:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_005F4C22;
loc_005F4B27:
    if (((unsigned int)(v_rsi)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) + v_r14 * 1))) goto loc_005F4C22;
loc_005F4B33:
    if (((unsigned int)((unsigned int)(a2))) != 4) goto loc_005F4B48;
    if (((unsigned int)(v_rsi)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) + v_r14 * 1))) goto loc_005F4B48;
    goto loc_005F4B4A;
loc_005F4B48:
    v_rbp = 0;
loc_005F4B4A:
    a3 = 0;
    a2 = 0;
    result = tr_stored_block(a1, a2, a3, 0);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) - (4));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (8));
    *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 16) * 1) = (unsigned __int8)(v_rsi);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) - (3));
    *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 16) * 1) = (unsigned __int8)(a2);
    a2 = (unsigned __int8)(~((unsigned __int8)(v_rsi)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) - (2));
    *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 16) * 1) = (unsigned __int8)(a2);
    a2 = (unsigned int)(~((unsigned int)((unsigned int)(v_rsi))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) - 1);
    a2 = (unsigned int)((a2) >> (8));
    *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 16) * 1) = (unsigned __int8)(a2);
    result = flush_pending(*(unsigned __int64 *)(a1), a2, a3, 0);
    if ((unsigned int)(v_r14) != 0) {
        a1 = *(unsigned __int64 *)(a1);
        a2 = (int)(*(unsigned int *)(a1 + 212));
        if (((unsigned int)(v_r14)) > ((unsigned int)(v_rsi))) { v_r14 = (unsigned int)(v_rsi); }
        a2 = (a2) + (*(unsigned __int64 *)(a1 + 160));
        a3 = (unsigned int)(v_r14);
        a1 = *(unsigned __int64 *)(a1 + 16);
        v_rbx = (unsigned int)(v_r14);
        result = memcpy(a1, a2, a3, 0);
        result = *(unsigned __int64 *)(a1);
        result = *(unsigned __int64 *)(a1);
        result = *(unsigned __int64 *)(a1);
        v_rsi = (unsigned int)((v_rsi) - ((unsigned int)(v_r14)));
    }
    if ((unsigned int)(v_rsi) != 0) {
        a1 = *(unsigned __int64 *)(a1);
        a3 = (unsigned int)(v_rsi);
        a2 = *(unsigned __int64 *)(a1 + 16);
        result = read_buf(a1, a2, a3, 0);
        a1 = *(unsigned __int64 *)(a1);
        result = (unsigned int)(v_rsi);
        result = *(unsigned __int64 *)(a1);
        result = *(unsigned __int64 *)(a1);
    }
    if (0 == 0) goto loc_005F4ACA;
loc_005F4C22:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p8)) - (*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)));
    if (condition_is_equal) goto loc_005F4D0E;
    if (((unsigned int)(v_r15)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148))))) goto loc_005F4C6F;
    *(unsigned int *)(a1 + 5972) = 2;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148)))));
    result = memcpy(*(unsigned __int64 *)(a1 + 160), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148)))), 0);
    *(unsigned int *)(a1 + 228) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148)));
    goto loc_005F4CFC;
loc_005F4C6F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 168))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)))));
    if (((unsigned int)(result)) > ((unsigned int)(v_r15))) goto loc_005F4CC4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) - (a2));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 160));
    *(unsigned int *)(a1 + 228) = (unsigned int)((unsigned int)((unsigned int)(a1)));
    result = memcpy(*(unsigned __int64 *)(a1 + 160), a2, (unsigned int)((unsigned int)(a1)), 0);
    result = (unsigned int)(*(unsigned int *)(a1 + 5972));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5972)))) < 2) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 5972))) + 1);
        *(unsigned int *)(a1 + 5972) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(a1 + 5976)) >= = ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228))))) {
        *(unsigned int *)(a1 + 5976) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)));
    }
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 228))) + (*(unsigned __int64 *)(a1 + 160));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) - ((unsigned int)((unsigned int)(v_r15)));
    result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_r15)), 0);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 148))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5976)))));
    if (((unsigned int)(v_r15)) > ((unsigned int)(result))) { v_r15 = (unsigned int)(result); }
loc_005F4CFC:
    *(unsigned int *)(a1 + 5976) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5976)) + v_r15 * 1);
    *(unsigned int *)(a1 + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)));
loc_005F4D0E:
    if ((*(unsigned int *)(a1 + 5988)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228))))) {
        *(unsigned int *)(a1 + 5988) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)));
    }
    if (0 == 0) goto loc_005F4D33;
    goto loc_005F4ECA;
loc_005F4D33:
    if ((((unsigned int)((unsigned int)(a2))) & (0xFFFFFFFBULL)) == 0) goto loc_005F4D58;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) != 0) goto loc_005F4D58;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)))) != (*(unsigned int *)(a1 + 212))) goto loc_005F4D58;
    goto loc_005F4ECA;
loc_005F4D58:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 168))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)))));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) <= ((unsigned int)(v_rbx))) goto loc_005F4DCB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 212)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148))))) goto loc_005F4DCB;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 212))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148)))));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148)))));
    *(unsigned int *)(a1 + 212) = (unsigned int)(a1);
    *(unsigned int *)(a1 + 228) = a3;
    result = memcpy(*(unsigned __int64 *)(a1 + 160), *(unsigned __int64 *)(a1 + 160) + (unsigned int)(*(unsigned int *)(a1 + 148)) * 1, a3, 0);
    result = (unsigned int)(*(unsigned int *)(a1 + 5972));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5972)))) < 2) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 5972))) + 1);
        *(unsigned int *)(a1 + 5972) = (unsigned int)(result);
    }
    v_rbx = (unsigned int)((v_rbx) + (*(unsigned int *)(a1 + 148)));
    if ((*(unsigned int *)(a1 + 5976)) >= = ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228))))) {
        *(unsigned int *)(a1 + 5976) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)));
    }
    v_rsi = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8));
    if (((unsigned int)(v_rbx)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8))))) { v_rsi = (unsigned int)(v_rbx); }
    if ((unsigned int)(v_rsi) != 0) {
        a2 = ((unsigned int)(*(unsigned int *)(a1 + 228))) + (*(unsigned __int64 *)(a1 + 160));
        a3 = (unsigned int)(v_rsi);
        result = read_buf(*(unsigned __int64 *)(a1), a2, a3, 0);
        a1 = *(unsigned int *)(a1 + 5976);
        a2 = *(unsigned int *)(a1 + 228);
        result = *(unsigned int *)(a1 + 148);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_rsi)));
        result = (unsigned int)((result) - ((unsigned int)(a1)));
        *(unsigned int *)(a1 + 228) = a2;
        if (((unsigned int)(v_rsi)) > ((unsigned int)(result))) { v_rsi = (unsigned int)(result); }
        result = a1 + v_rsi * 1;
        *(unsigned int *)(a1 + 5976) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(a1 + 5988)) < a2) {
        *(unsigned int *)(a1 + 5988) = a2;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 5984))) + (42));
    result = (unsigned int)((result) >> (3));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) - ((unsigned int)(result)));
    if (((unsigned int)(v_rbx)) > ((unsigned int)((unsigned int)(0xFFFFULL)))) { v_rbx = (unsigned int)((unsigned int)(0xFFFFULL)); }
    a2 = (unsigned int)((a2) - (*(unsigned int *)(a1 + 212)));
    result = (unsigned int)(*(unsigned int *)(a1 + 148));
    if (((unsigned int)(v_rbx)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 148))))) { result = (unsigned int)(v_rbx); }
    if (a2 >= ((unsigned int)(result))) goto loc_005F4E7B;
    if (a2 != 0) goto loc_005F4E60;
    if (((unsigned int)((unsigned int)(a2))) != 4) goto loc_005F4EC3;
    goto loc_005F4E65;
loc_005F4E60:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_005F4EC3;
loc_005F4E65:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) != 0) goto loc_005F4EC3;
    if (a2 > ((unsigned int)(v_rbx))) goto loc_005F4EC3;
    goto loc_005F4E7F;
loc_005F4E7B:
    if (a2 <= ((unsigned int)(v_rbx))) {
        v_rbx = a2;
    }
    if (((unsigned int)((unsigned int)(a2))) != 4) goto loc_005F4E9B;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) != 0) goto loc_005F4E9B;
    if (((unsigned int)(v_rbx)) != a2) goto loc_005F4E9B;
    goto loc_005F4E9D;
loc_005F4E9B:
    v_rbp = 0;
loc_005F4E9D:
    a2 = ((int)(*(unsigned int *)(a1 + 212))) + (*(unsigned __int64 *)(a1 + 160));
    result = tr_stored_block(a1, a2, (unsigned int)((unsigned int)(v_rbx)), 0);
    result = flush_pending(*(unsigned __int64 *)(a1), a2, (unsigned int)((unsigned int)(v_rbx)), 0);
loc_005F4EC3:
    v_rbp = (unsigned int)(-(v_rbp));
    result = (unsigned int)((result) & (2));
loc_005F4ECA:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t deflate_stored(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) + (-5));
    local_r13 = (uint32_t)(*(uint32_t *)(arg1 + 0x94));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94))))) { local_r13 = (uint32_t)(result); }
    local_rbp = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)));
loc_005F4ACA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1760))) + (42));
    result = (uint32_t)((result) >> (3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18)))) < ((uint32_t)(result))) goto loc_005F4C22;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18))) - ((uint32_t)(result)));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) - (*(uint32_t *)(arg1 + 0xD4)));
    local_rsi = (uint32_t)((uint32_t)((uint32_t)(0xFFFFULL)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) + local_r14 * 1)) < ((uint32_t)((uint32_t)(0xFFFFULL)))) { local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) + local_r14 * 1); }
    if (((uint32_t)(local_rsi)) > ((uint32_t)(Arg1))) { local_rsi = (uint32_t)(Arg1); }
    if (((uint32_t)(local_rsi)) >= ((uint32_t)(local_r13))) goto loc_005F4B33;
    if ((uint32_t)(local_rsi) != 0) goto loc_005F4B1E;
    if (((uint32_t)((uint32_t)(Arg2))) != 4) goto loc_005F4C22;
    goto loc_005F4B27;
loc_005F4B1E:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_005F4C22;
loc_005F4B27:
    if (((uint32_t)(local_rsi)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) + local_r14 * 1))) goto loc_005F4C22;
loc_005F4B33:
    if (((uint32_t)((uint32_t)(Arg2))) != 4) goto loc_005F4B48;
    if (((uint32_t)(local_rsi)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) + local_r14 * 1))) goto loc_005F4B48;
    goto loc_005F4B4A;
loc_005F4B48:
    local_rbp = 0;
loc_005F4B4A:
    Arg3 = 0;
    Arg2 = 0;
    result = tr_stored_block(Arg1, Arg2, Arg3, 0);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) - (4));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (8));
    *(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x10) * 1) = (uint8_t)(local_rsi);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) - (3));
    *(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x10) * 1) = (uint8_t)(Arg2);
    Arg2 = (uint8_t)(~((uint8_t)(local_rsi)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) - (2));
    *(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x10) * 1) = (uint8_t)(Arg2);
    Arg2 = (uint32_t)(~((uint32_t)((uint32_t)(local_rsi))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) - 1);
    Arg2 = (uint32_t)((Arg2) >> (8));
    *(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x10) * 1) = (uint8_t)(Arg2);
    result = flush_pending(*(uint64_t *)(arg1), Arg2, Arg3, 0);
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = *(uint64_t *)(arg1);
        Arg2 = (int32_t)(*(uint32_t *)(arg1 + 0xD4));
        if (((uint32_t)(local_r14)) > ((uint32_t)(local_rsi))) { local_r14 = (uint32_t)(local_rsi); }
        Arg2 = (Arg2) + (*(uint64_t *)(arg1 + 0xA0));
        Arg3 = (uint32_t)(local_r14);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        local_rbx = (uint32_t)(local_r14);
        result = memcpy(Arg1, Arg2, Arg3, 0);
        result = *(uint64_t *)(arg1);
        result = *(uint64_t *)(arg1);
        result = *(uint64_t *)(arg1);
        local_rsi = (uint32_t)((local_rsi) - ((uint32_t)(local_r14)));
    }
    if ((uint32_t)(local_rsi) != 0) {
        Arg1 = *(uint64_t *)(arg1);
        Arg3 = (uint32_t)(local_rsi);
        Arg2 = *(uint64_t *)(arg1 + 0x10);
        result = read_buf(Arg1, Arg2, Arg3, 0);
        Arg1 = *(uint64_t *)(arg1);
        result = (uint32_t)(local_rsi);
        result = *(uint64_t *)(arg1);
        result = *(uint64_t *)(arg1);
    }
    if (0 == 0) goto loc_005F4ACA;
loc_005F4C22:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p8)) - (*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)));
    if (condition_is_equal) goto loc_005F4D0E;
    if (((uint32_t)(local_r15)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94))))) goto loc_005F4C6F;
    *(uint32_t *)(arg1 + 0x1754) = 2;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94)))));
    result = memcpy(*(uint64_t *)(arg1 + 0xA0), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94)))), 0);
    *(uint32_t *)(arg1 + 0xE4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94)));
    goto loc_005F4CFC;
loc_005F4C6F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xA8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)))));
    if (((uint32_t)(result)) > ((uint32_t)(local_r15))) goto loc_005F4CC4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) - (Arg2));
    Arg2 = (Arg2) + (*(uint64_t *)(arg1 + 0xA0));
    *(uint32_t *)(arg1 + 0xE4) = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    result = memcpy(*(uint64_t *)(arg1 + 0xA0), Arg2, (uint32_t)((uint32_t)(Arg1)), 0);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x1754));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1754)))) < 2) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1754))) + 1);
        *(uint32_t *)(arg1 + 0x1754) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(arg1 + 0x1758)) >= = ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4))))) {
        *(uint32_t *)(arg1 + 0x1758) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)));
    }
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) + (*(uint64_t *)(arg1 + 0xA0));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1))) - ((uint32_t)((uint32_t)(local_r15)));
    result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_r15)), 0);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x94))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1758)))));
    if (((uint32_t)(local_r15)) > ((uint32_t)(result))) { local_r15 = (uint32_t)(result); }
loc_005F4CFC:
    *(uint32_t *)(arg1 + 0x1758) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1758)) + local_r15 * 1);
    *(uint32_t *)(arg1 + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)));
loc_005F4D0E:
    if ((*(uint32_t *)(arg1 + 0x1764)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4))))) {
        *(uint32_t *)(arg1 + 0x1764) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)));
    }
    if (0 == 0) goto loc_005F4D33;
    goto loc_005F4ECA;
loc_005F4D33:
    if ((((uint32_t)((uint32_t)(Arg2))) & (0xFFFFFFFBULL)) == 0) goto loc_005F4D58;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) != 0) goto loc_005F4D58;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)))) != (*(uint32_t *)(arg1 + 0xD4))) goto loc_005F4D58;
    goto loc_005F4ECA;
loc_005F4D58:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xA8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)))));
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) <= ((uint32_t)(local_rbx))) goto loc_005F4DCB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD4)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94))))) goto loc_005F4DCB;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xD4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94)))));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94)))));
    *(uint32_t *)(arg1 + 0xD4) = (uint32_t)(Arg1);
    *(uint32_t *)(arg1 + 0xE4) = Arg3;
    result = memcpy(*(uint64_t *)(arg1 + 0xA0), *(uint64_t *)(arg1 + 0xA0) + (uint32_t)(*(uint32_t *)(arg1 + 0x94)) * 1, Arg3, 0);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x1754));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1754)))) < 2) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1754))) + 1);
        *(uint32_t *)(arg1 + 0x1754) = (uint32_t)(result);
    }
    local_rbx = (uint32_t)((local_rbx) + (*(uint32_t *)(arg1 + 0x94)));
    if ((*(uint32_t *)(arg1 + 0x1758)) >= = ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4))))) {
        *(uint32_t *)(arg1 + 0x1758) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)));
    }
    local_rsi = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8));
    if (((uint32_t)(local_rbx)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8))))) { local_rsi = (uint32_t)(local_rbx); }
    if ((uint32_t)(local_rsi) != 0) {
        Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) + (*(uint64_t *)(arg1 + 0xA0));
        Arg3 = (uint32_t)(local_rsi);
        result = read_buf(*(uint64_t *)(arg1), Arg2, Arg3, 0);
        Arg1 = *(uint32_t *)(arg1 + 0x1758);
        Arg2 = *(uint32_t *)(arg1 + 0xE4);
        result = *(uint32_t *)(arg1 + 0x94);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_rsi)));
        result = (uint32_t)((result) - ((uint32_t)(Arg1)));
        *(uint32_t *)(arg1 + 0xE4) = Arg2;
        if (((uint32_t)(local_rsi)) > ((uint32_t)(result))) { local_rsi = (uint32_t)(result); }
        result = Arg1 + local_rsi * 1;
        *(uint32_t *)(arg1 + 0x1758) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(arg1 + 0x1764)) < Arg2) {
        *(uint32_t *)(arg1 + 0x1764) = Arg2;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1760))) + (42));
    result = (uint32_t)((result) >> (3));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) - ((uint32_t)(result)));
    if (((uint32_t)(local_rbx)) > ((uint32_t)((uint32_t)(0xFFFFULL)))) { local_rbx = (uint32_t)((uint32_t)(0xFFFFULL)); }
    Arg2 = (uint32_t)((Arg2) - (*(uint32_t *)(arg1 + 0xD4)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x94));
    if (((uint32_t)(local_rbx)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x94))))) { result = (uint32_t)(local_rbx); }
    if (Arg2 >= ((uint32_t)(result))) goto loc_005F4E7B;
    if (Arg2 != 0) goto loc_005F4E60;
    if (((uint32_t)((uint32_t)(Arg2))) != 4) goto loc_005F4EC3;
    goto loc_005F4E65;
loc_005F4E60:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_005F4EC3;
loc_005F4E65:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) != 0) goto loc_005F4EC3;
    if (Arg2 > ((uint32_t)(local_rbx))) goto loc_005F4EC3;
    goto loc_005F4E7F;
loc_005F4E7B:
    if (Arg2 <= ((uint32_t)(local_rbx))) {
        local_rbx = Arg2;
    }
    if (((uint32_t)((uint32_t)(Arg2))) != 4) goto loc_005F4E9B;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) != 0) goto loc_005F4E9B;
    if (((uint32_t)(local_rbx)) != Arg2) goto loc_005F4E9B;
    goto loc_005F4E9D;
loc_005F4E9B:
    local_rbp = 0;
loc_005F4E9D:
    Arg2 = ((int32_t)(*(uint32_t *)(arg1 + 0xD4))) + (*(uint64_t *)(arg1 + 0xA0));
    result = tr_stored_block(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), 0);
    result = flush_pending(*(uint64_t *)(arg1), Arg2, (uint32_t)((uint32_t)(local_rbx)), 0);
loc_005F4EC3:
    local_rbp = (uint32_t)(-(local_rbp));
    result = (uint32_t)((result) & (2));
loc_005F4ECA:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x94` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `32` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `R/W` |
| `Arg1` | `+ 0xD4` | `32` | `W` |
| `Arg1` | `+ 0xD4` | `64` | `R` |
| `Arg1` | `+ 0xE4` | `32` | `R` |
| `Arg1` | `+ 0xE4` | `32` | `R/W` |
| `Arg1` | `+ 0xE4` | `32` | `W` |
| `Arg1` | `+ 0x1754` | `32` | `R` |
| `Arg1` | `+ 0x1754` | `32` | `W` |
| `Arg1` | `+ 0x1758` | `32` | `R` |
| `Arg1` | `+ 0x1758` | `32` | `W` |
| `Arg1` | `+ 0x1760` | `32` | `R` |
| `Arg1` | `+ 0x1764` | `32` | `R` |
| `Arg1` | `+ 0x1764` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F4A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
