# AuthzBasepConvertRelativeToAbsoluteTokenAttribute

- RVA: `0x004B97BC`–`0x004B9D23` (길이 `1,383` bytes)
- VA: `0x00000001404B97BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C2BC`
- 디코드: `381`개 명령, `1,383/1,383` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B99DE` → [RtlStringCbLengthW](../45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x004B9A81` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004B9AD0` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004B9BB4` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004B9C2D` → [RtlStringCbLengthW](../45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x004B9C78` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [sub_006E041A](../6E/Unknown_function_006E041A.md) at `0x006E0456`
- [sub_006E041A](../6E/Unknown_function_006E041A.md) at `0x006E049C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B97BC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004B97C1  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
004B97C6  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
004B97CB  57                              push rdi
004B97CC  41 54                           push r12
004B97CE  41 55                           push r13
004B97D0  41 56                           push r14
004B97D2  41 57                           push r15
004B97D4  48 83 EC 30                     sub rsp, 0x30
004B97D8  33 FF                           xor edi, edi
004B97DA  44 8B FA                        mov r15d, edx
004B97DD  4D 8B E9                        mov r13, r9
004B97E0  49 8B F0                        mov rsi, r8
004B97E3  4C 8B F1                        mov r14, rcx
004B97E6  48 85 C9                        test rcx, rcx
004B97E9  0F 84 0F 05 00 00               je 0x1404b9cfe
004B97EF  4D 85 C0                        test r8, r8
004B97F2  0F 84 06 05 00 00               je 0x1404b9cfe
004B97F8  4D 85 C9                        test r9, r9
004B97FB  0F 84 FD 04 00 00               je 0x1404b9cfe
004B9801  41 83 FF 14                     cmp r15d, 0x14
004B9805  73 0A                           jae 0x1404b9811
004B9807  BB 77 00 00 C0                  mov ebx, 0xc0000077
004B980C  E9 F2 04 00 00                  jmp 0x1404b9d03
004B9811  44 8B 51 0C                     mov r10d, dword ptr [rcx + 0xc]
004B9815  45 85 D2                        test r10d, r10d
004B9818  74 ED                           je 0x1404b9807
004B981A  8B 01                           mov eax, dword ptr [rcx]
004B981C  44 3B F8                        cmp r15d, eax
004B981F  72 E6                           jb 0x1404b9807
004B9821  41 8B CF                        mov ecx, r15d
004B9824  2B C8                           sub ecx, eax
004B9826  83 F9 04                        cmp ecx, 4
004B9829  72 DC                           jb 0x1404b9807
004B982B  49 03 C6                        add rax, r14
004B982E  0F 84 CA 04 00 00               je 0x1404b9cfe
004B9834  48 D1 E9                        shr rcx, 1
004B9837  41 B9 02 00 00 00               mov r9d, 2
004B983D  48 8B D1                        mov rdx, rcx
004B9840  74 0E                           je 0x1404b9850
004B9842  66 39 38                        cmp word ptr [rax], di
004B9845  74 09                           je 0x1404b9850
004B9847  49 03 C1                        add rax, r9
004B984A  48 83 E9 01                     sub rcx, 1
004B984E  75 F2                           jne 0x1404b9842
004B9850  48 8B C1                        mov rax, rcx
004B9853  48 F7 D8                        neg rax
004B9856  1B DB                           sbb ebx, ebx
004B9858  F7 D3                           not ebx
004B985A  81 E3 0D 00 00 C0               and ebx, 0xc000000d
004B9860  48 85 C9                        test rcx, rcx
004B9863  74 05                           je 0x1404b986a
004B9865  48 2B D1                        sub rdx, rcx
004B9868  EB 03                           jmp 0x1404b986d
004B986A  48 8B D7                        mov rdx, rdi
004B986D  48 85 C9                        test rcx, rcx
004B9870  0F 84 8D 04 00 00               je 0x1404b9d03
004B9876  48 8D 04 12                     lea rax, [rdx + rdx]
004B987A  8D 68 02                        lea ebp, [rax + 2]
004B987D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004B9882  3B E8                           cmp ebp, eax
004B9884  0F 82 90 01 00 00               jb 0x1404b9a1a
004B988A  44 8D 5D 03                     lea r11d, [rbp + 3]
004B988E  44 3B DD                        cmp r11d, ebp
004B9891  0F 82 83 01 00 00               jb 0x1404b9a1a
004B9897  BB FC FF FF FF                  mov ebx, 0xfffffffc
004B989C  44 23 DB                        and r11d, ebx
004B989F  41 83 C3 28                     add r11d, 0x28
004B98A3  41 83 FB 28                     cmp r11d, 0x28
004B98A7  0F 82 6D 01 00 00               jb 0x1404b9a1a
004B98AD  4A 8D 0C 95 00 00 00 00         lea rcx, [r10*4]
004B98B5  41 B8 FF FF FF FF               mov r8d, 0xffffffff
004B98BB  49 8B D2                        mov rdx, r10
004B98BE  49 3B C8                        cmp rcx, r8
004B98C1  0F 87 53 01 00 00               ja 0x1404b9a1a
004B98C7  41 8D 47 F0                     lea eax, [r15 - 0x10]
004B98CB  3B C1                           cmp eax, ecx
004B98CD  0F 82 34 FF FF FF               jb 0x1404b9807
004B98D3  41 0F B7 4E 04                  movzx ecx, word ptr [r14 + 4]
004B98D8  83 E9 01                        sub ecx, 1
004B98DB  0F 84 43 01 00 00               je 0x1404b9a24
004B98E1  83 E9 01                        sub ecx, 1
004B98E4  0F 84 3A 01 00 00               je 0x1404b9a24
004B98EA  83 E9 01                        sub ecx, 1
004B98ED  0F 84 A0 00 00 00               je 0x1404b9993
004B98F3  41 2B C9                        sub ecx, r9d
004B98F6  74 12                           je 0x1404b990a
004B98F8  83 E9 01                        sub ecx, 1
004B98FB  0F 84 23 01 00 00               je 0x1404b9a24
004B9901  83 F9 0A                        cmp ecx, 0xa
004B9904  0F 85 58 01 00 00               jne 0x1404b9a62
004B990A  48 C1 E2 04                     shl rdx, 4
004B990E  49 3B D0                        cmp rdx, r8
004B9911  0F 87 03 01 00 00               ja 0x1404b9a1a
004B9917  41 8D 04 13                     lea eax, [r11 + rdx]
004B991B  41 3B C3                        cmp eax, r11d
004B991E  0F 82 F6 00 00 00               jb 0x1404b9a1a
004B9924  44 8B D8                        mov r11d, eax
004B9927  8B D7                           mov edx, edi
004B9929  41 3B D2                        cmp edx, r10d
004B992C  0F 83 30 01 00 00               jae 0x1404b9a62
004B9932  8B C2                           mov eax, edx
004B9934  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
004B9939  44 3B F9                        cmp r15d, ecx
004B993C  0F 82 C5 FE FF FF               jb 0x1404b9807
004B9942  41 8B C7                        mov eax, r15d
004B9945  2B C1                           sub eax, ecx
004B9947  83 F8 04                        cmp eax, 4
004B994A  0F 82 B7 FE FF FF               jb 0x1404b9807
004B9950  46 8B 04 31                     mov r8d, dword ptr [rcx + r14]
004B9954  44 8D 49 04                     lea r9d, [rcx + 4]
004B9958  44 3B C9                        cmp r9d, ecx
004B995B  0F 82 B9 00 00 00               jb 0x1404b9a1a
004B9961  41 8B C7                        mov eax, r15d
004B9964  41 2B C1                        sub eax, r9d
004B9967  41 3B C0                        cmp eax, r8d
004B996A  0F 82 97 FE FF FF               jb 0x1404b9807
004B9970  41 8D 40 03                     lea eax, [r8 + 3]
004B9974  41 3B C0                        cmp eax, r8d
004B9977  0F 82 9D 00 00 00               jb 0x1404b9a1a
004B997D  23 C3                           and eax, ebx
004B997F  42 8D 0C 18                     lea ecx, [rax + r11]
004B9983  41 3B CB                        cmp ecx, r11d
004B9986  0F 82 8E 00 00 00               jb 0x1404b9a1a
004B998C  44 8B D9                        mov r11d, ecx
004B998F  FF C2                           inc edx
004B9991  EB 96                           jmp 0x1404b9929
004B9993  48 C1 E2 04                     shl rdx, 4
004B9997  49 3B D0                        cmp rdx, r8
004B999A  77 7E                           ja 0x1404b9a1a
004B999C  41 8D 04 13                     lea eax, [r11 + rdx]
004B99A0  41 3B C3                        cmp eax, r11d
004B99A3  72 75                           jb 0x1404b9a1a
004B99A5  44 8B D8                        mov r11d, eax
004B99A8  44 8B E7                        mov r12d, edi
004B99AB  45 3B 66 0C                     cmp r12d, dword ptr [r14 + 0xc]
004B99AF  0F 83 AD 00 00 00               jae 0x1404b9a62
004B99B5  41 8B C4                        mov eax, r12d
004B99B8  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
004B99BD  44 3B F9                        cmp r15d, ecx
004B99C0  0F 82 41 FE FF FF               jb 0x1404b9807
004B99C6  41 8B C7                        mov eax, r15d
004B99C9  2B C1                           sub eax, ecx
004B99CB  41 3B C1                        cmp eax, r9d
004B99CE  0F 82 33 FE FF FF               jb 0x1404b9807
004B99D4  8B D0                           mov edx, eax
004B99D6  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
004B99DB  49 03 CE                        add rcx, r14
004B99DE  E8 09 DC F9 FF                  call 0x1404575ec
004B99E3  8B D8                           mov ebx, eax
004B99E5  85 C0                           test eax, eax
004B99E7  0F 88 16 03 00 00               js 0x1404b9d03
004B99ED  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
004B99F2  8D 48 02                        lea ecx, [rax + 2]
004B99F5  3B C8                           cmp ecx, eax
004B99F7  72 21                           jb 0x1404b9a1a
004B99F9  8D 41 03                        lea eax, [rcx + 3]
004B99FC  3B C1                           cmp eax, ecx
004B99FE  72 1A                           jb 0x1404b9a1a
004B9A00  83 E0 FC                        and eax, 0xfffffffc
004B9A03  42 8D 0C 18                     lea ecx, [rax + r11]
004B9A07  41 3B CB                        cmp ecx, r11d
004B9A0A  72 0E                           jb 0x1404b9a1a
004B9A0C  44 8B D9                        mov r11d, ecx
004B9A0F  41 FF C4                        inc r12d
004B9A12  41 B9 02 00 00 00               mov r9d, 2
004B9A18  EB 91                           jmp 0x1404b99ab
004B9A1A  BB 95 00 00 C0                  mov ebx, 0xc0000095
004B9A1F  E9 DF 02 00 00                  jmp 0x1404b9d03
004B9A24  48 C1 E2 03                     shl rdx, 3
004B9A28  49 3B D0                        cmp rdx, r8
004B9A2B  77 ED                           ja 0x1404b9a1a
004B9A2D  41 8D 04 13                     lea eax, [r11 + rdx]
004B9A31  41 3B C3                        cmp eax, r11d
004B9A34  72 E4                           jb 0x1404b9a1a
004B9A36  44 8B D8                        mov r11d, eax
004B9A39  8B CF                           mov ecx, edi
004B9A3B  41 3B CA                        cmp ecx, r10d
004B9A3E  73 22                           jae 0x1404b9a62
004B9A40  8B C1                           mov eax, ecx
004B9A42  41 8B 54 86 10                  mov edx, dword ptr [r14 + rax*4 + 0x10]
004B9A47  44 3B FA                        cmp r15d, edx
004B9A4A  0F 82 B7 FD FF FF               jb 0x1404b9807
004B9A50  41 8B C7                        mov eax, r15d
004B9A53  2B C2                           sub eax, edx
004B9A55  83 F8 08                        cmp eax, 8
004B9A58  0F 82 A9 FD FF FF               jb 0x1404b9807
004B9A5E  FF C1                           inc ecx
004B9A60  EB D9                           jmp 0x1404b9a3b
004B9A62  41 8B 45 00                     mov eax, dword ptr [r13]
004B9A66  45 89 5D 00                     mov dword ptr [r13], r11d
004B9A6A  41 3B C3                        cmp eax, r11d
004B9A6D  73 0A                           jae 0x1404b9a79
004B9A6F  BB 23 00 00 C0                  mov ebx, 0xc0000023
004B9A74  E9 8A 02 00 00                  jmp 0x1404b9d03
004B9A79  45 8B C3                        mov r8d, r11d
004B9A7C  33 D2                           xor edx, edx
004B9A7E  48 8B CE                        mov rcx, rsi
004B9A81  E8 BA D1 20 00                  call 0x1406c6c40
004B9A86  41 0F B7 46 04                  movzx eax, word ptr [r14 + 4]
004B9A8B  4C 8D 66 28                     lea r12, [rsi + 0x28]
004B9A8F  66 89 46 10                     mov word ptr [rsi + 0x10], ax
004B9A93  41 0F B7 46 06                  movzx eax, word ptr [r14 + 6]
004B9A98  66 89 46 12                     mov word ptr [rsi + 0x12], ax
004B9A9C  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
004B9AA0  89 46 14                        mov dword ptr [rsi + 0x14], eax
004B9AA3  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
004B9AA7  89 46 18                        mov dword ptr [rsi + 0x18], eax
004B9AAA  8D 45 28                        lea eax, [rbp + 0x28]
004B9AAD  83 F8 28                        cmp eax, 0x28
004B9AB0  0F 82 64 FF FF FF               jb 0x1404b9a1a
004B9AB6  8D 58 03                        lea ebx, [rax + 3]
004B9AB9  3B D8                           cmp ebx, eax
004B9ABB  0F 82 59 FF FF FF               jb 0x1404b9a1a
004B9AC1  41 8B 16                        mov edx, dword ptr [r14]
004B9AC4  49 8B CC                        mov rcx, r12
004B9AC7  49 03 D6                        add rdx, r14
004B9ACA  44 8B C5                        mov r8d, ebp
004B9ACD  83 E3 FC                        and ebx, 0xfffffffc
004B9AD0  E8 6B CD 20 00                  call 0x1406c6840
004B9AD5  0F B7 4E 10                     movzx ecx, word ptr [rsi + 0x10]
004B9AD9  0F B7 C5                        movzx eax, bp
004B9ADC  41 B8 02 00 00 00               mov r8d, 2
004B9AE2  8B D3                           mov edx, ebx
004B9AE4  66 41 2B C0                     sub ax, r8w
004B9AE8  4C 89 66 08                     mov qword ptr [rsi + 8], r12
004B9AEC  48 03 D6                        add rdx, rsi
004B9AEF  66 89 06                        mov word ptr [rsi], ax
004B9AF2  66 89 6E 02                     mov word ptr [rsi + 2], bp
004B9AF6  83 E9 01                        sub ecx, 1
004B9AF9  0F 84 B7 01 00 00               je 0x1404b9cb6
004B9AFF  83 E9 01                        sub ecx, 1
004B9B02  0F 84 AE 01 00 00               je 0x1404b9cb6
004B9B08  83 E9 01                        sub ecx, 1
004B9B0B  0F 84 C8 00 00 00               je 0x1404b9bd9
004B9B11  41 2B C8                        sub ecx, r8d
004B9B14  74 12                           je 0x1404b9b28
004B9B16  83 E9 01                        sub ecx, 1
004B9B19  0F 84 97 01 00 00               je 0x1404b9cb6
004B9B1F  83 F9 0A                        cmp ecx, 0xa
004B9B22  0F 85 DF FC FF FF               jne 0x1404b9807
004B9B28  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
004B9B2B  41 B8 FF FF FF FF               mov r8d, 0xffffffff
004B9B31  48 C1 E0 04                     shl rax, 4
004B9B35  49 3B C0                        cmp rax, r8
004B9B38  0F 87 DC FE FF FF               ja 0x1404b9a1a
004B9B3E  8D 0C 18                        lea ecx, [rax + rbx]
004B9B41  3B CB                           cmp ecx, ebx
004B9B43  0F 82 D1 FE FF FF               jb 0x1404b9a1a
004B9B49  44 8B F9                        mov r15d, ecx
004B9B4C  48 8D 2C 0E                     lea rbp, [rsi + rcx]
004B9B50  8B DF                           mov ebx, edi
004B9B52  48 89 56 20                     mov qword ptr [rsi + 0x20], rdx
004B9B56  44 8B EF                        mov r13d, edi
004B9B59  44 3B 6E 18                     cmp r13d, dword ptr [rsi + 0x18]
004B9B5D  0F 83 A0 01 00 00               jae 0x1404b9d03
004B9B63  45 8B E5                        mov r12d, r13d
004B9B66  4B 8D 14 A6                     lea rdx, [r14 + r12*4]
004B9B6A  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
004B9B6D  42 8B 0C 30                     mov ecx, dword ptr [rax + r14]
004B9B71  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
004B9B75  42 8D 04 39                     lea eax, [rcx + r15]
004B9B79  41 3B C7                        cmp eax, r15d
004B9B7C  0F 82 98 FE FF FF               jb 0x1404b9a1a
004B9B82  44 8D 78 03                     lea r15d, [rax + 3]
004B9B86  44 3B F8                        cmp r15d, eax
004B9B89  0F 82 8B FE FF FF               jb 0x1404b9a1a
004B9B8F  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
004B9B93  4D 03 E4                        add r12, r12
004B9B96  41 83 E7 FC                     and r15d, 0xfffffffc
004B9B9A  8B DF                           mov ebx, edi
004B9B9C  4A 89 3C E0                     mov qword ptr [rax + r12*8], rdi
004B9BA0  85 C9                           test ecx, ecx
004B9BA2  74 21                           je 0x1404b9bc5
004B9BA4  8B 52 10                        mov edx, dword ptr [rdx + 0x10]
004B9BA7  44 8B C1                        mov r8d, ecx
004B9BAA  48 83 C2 04                     add rdx, 4
004B9BAE  48 8B CD                        mov rcx, rbp
004B9BB1  49 03 D6                        add rdx, r14
004B9BB4  E8 87 CC 20 00                  call 0x1406c6840
004B9BB9  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
004B9BBD  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
004B9BC1  4A 89 2C E0                     mov qword ptr [rax + r12*8], rbp
004B9BC5  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
004B9BC9  41 8B EF                        mov ebp, r15d
004B9BCC  48 03 EE                        add rbp, rsi
004B9BCF  41 FF C5                        inc r13d
004B9BD2  42 89 4C E0 08                  mov dword ptr [rax + r12*8 + 8], ecx
004B9BD7  EB 80                           jmp 0x1404b9b59
004B9BD9  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
004B9BDC  41 B8 FF FF FF FF               mov r8d, 0xffffffff
004B9BE2  48 C1 E0 04                     shl rax, 4
004B9BE6  49 3B C0                        cmp rax, r8
004B9BE9  0F 87 2B FE FF FF               ja 0x1404b9a1a
004B9BEF  8D 0C 18                        lea ecx, [rax + rbx]
004B9BF2  3B CB                           cmp ecx, ebx
004B9BF4  0F 82 20 FE FF FF               jb 0x1404b9a1a
004B9BFA  8B E9                           mov ebp, ecx
004B9BFC  4C 8D 2C 0E                     lea r13, [rsi + rcx]
004B9C00  8B DF                           mov ebx, edi
004B9C02  48 89 56 20                     mov qword ptr [rsi + 0x20], rdx
004B9C06  8B C7                           mov eax, edi
004B9C08  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
004B9C0C  3B 46 18                        cmp eax, dword ptr [rsi + 0x18]
004B9C0F  0F 83 EE 00 00 00               jae 0x1404b9d03
004B9C15  44 8B D8                        mov r11d, eax
004B9C18  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
004B9C1D  49 8B D7                        mov rdx, r15
004B9C20  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
004B9C25  43 8B 4C 9E 10                  mov ecx, dword ptr [r14 + r11*4 + 0x10]
004B9C2A  49 03 CE                        add rcx, r14
004B9C2D  E8 BA D9 F9 FF                  call 0x1404575ec
004B9C32  8B D8                           mov ebx, eax
004B9C34  85 C0                           test eax, eax
004B9C36  0F 88 C7 00 00 00               js 0x1404b9d03
004B9C3C  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
004B9C41  44 8D 60 02                     lea r12d, [rax + 2]
004B9C45  44 3B E0                        cmp r12d, eax
004B9C48  0F 82 CC FD FF FF               jb 0x1404b9a1a
004B9C4E  41 8D 04 2C                     lea eax, [r12 + rbp]
004B9C52  3B C5                           cmp eax, ebp
004B9C54  0F 82 C0 FD FF FF               jb 0x1404b9a1a
004B9C5A  8D 68 03                        lea ebp, [rax + 3]
004B9C5D  3B E8                           cmp ebp, eax
004B9C5F  0F 82 B5 FD FF FF               jb 0x1404b9a1a
004B9C65  43 8B 54 9E 10                  mov edx, dword ptr [r14 + r11*4 + 0x10]
004B9C6A  49 8B CD                        mov rcx, r13
004B9C6D  49 03 D6                        add rdx, r14
004B9C70  45 8B C4                        mov r8d, r12d
004B9C73  8B DF                           mov ebx, edi
004B9C75  83 E5 FC                        and ebp, 0xfffffffc
004B9C78  E8 C3 CB 20 00                  call 0x1406c6840
004B9C7D  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
004B9C81  41 8D 4C 24 FE                  lea ecx, [r12 - 2]
004B9C86  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
004B9C8B  48 03 D2                        add rdx, rdx
004B9C8E  4C 89 6C D0 08                  mov qword ptr [rax + rdx*8 + 8], r13
004B9C93  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
004B9C97  44 8B ED                        mov r13d, ebp
004B9C9A  4C 03 EE                        add r13, rsi
004B9C9D  66 89 0C D0                     mov word ptr [rax + rdx*8], cx
004B9CA1  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
004B9CA5  66 44 89 64 D0 02               mov word ptr [rax + rdx*8 + 2], r12w
004B9CAB  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
004B9CAF  FF C0                           inc eax
004B9CB1  E9 52 FF FF FF                  jmp 0x1404b9c08
004B9CB6  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
004B9CB9  41 B8 FF FF FF FF               mov r8d, 0xffffffff
004B9CBF  8B C1                           mov eax, ecx
004B9CC1  48 C1 E0 03                     shl rax, 3
004B9CC5  49 3B C0                        cmp rax, r8
004B9CC8  0F 87 4C FD FF FF               ja 0x1404b9a1a
004B9CCE  03 C3                           add eax, ebx
004B9CD0  3B C3                           cmp eax, ebx
004B9CD2  0F 82 42 FD FF FF               jb 0x1404b9a1a
004B9CD8  48 89 56 20                     mov qword ptr [rsi + 0x20], rdx
004B9CDC  8B DF                           mov ebx, edi
004B9CDE  85 C9                           test ecx, ecx
004B9CE0  74 21                           je 0x1404b9d03
004B9CE2  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
004B9CE6  8B D7                           mov edx, edi
004B9CE8  FF C7                           inc edi
004B9CEA  41 8B 44 96 10                  mov eax, dword ptr [r14 + rdx*4 + 0x10]
004B9CEF  4A 8B 04 30                     mov rax, qword ptr [rax + r14]
004B9CF3  48 89 04 D1                     mov qword ptr [rcx + rdx*8], rax
004B9CF7  3B 7E 18                        cmp edi, dword ptr [rsi + 0x18]
004B9CFA  72 E6                           jb 0x1404b9ce2
004B9CFC  EB 05                           jmp 0x1404b9d03
004B9CFE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004B9D03  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
004B9D08  8B C3                           mov eax, ebx
004B9D0A  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
004B9D0F  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
004B9D14  48 83 C4 30                     add rsp, 0x30
004B9D18  41 5F                           pop r15
004B9D1A  41 5E                           pop r14
004B9D1C  41 5D                           pop r13
004B9D1E  41 5C                           pop r12
004B9D20  5F                              pop rdi
004B9D21  C3                              ret
004B9D22  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepConvertRelativeToAbsoluteTokenAttribute(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rdi = 0;
    if (a1 == 0) goto loc_004B9CFE;
    if (a3 == 0) goto loc_004B9CFE;
    if (a4 == 0) goto loc_004B9CFE;
    if (((unsigned int)((unsigned int)(a2))) >= 20) goto loc_004B9811;
loc_004B9807:
    goto loc_004B9D03;
loc_004B9811:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))) == 0) goto loc_004B9807;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) goto loc_004B9807;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    if (((unsigned int)(a1)) < 4) goto loc_004B9807;
    result = ((unsigned int)(*(unsigned int *)(a1))) + (a1);
    if (condition_is_equal) goto loc_004B9CFE;
    a1 = (a1) >> (1);
    if (condition_is_equal) goto loc_004B9850;
loc_004B9842:
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_004B9850;
    result = (result) + (2);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_004B9842;
loc_004B9850:
    result = -(a1);
    v_rbx = (unsigned int)(~((unsigned int)(0xC0000077ULL)));
    v_rbx = (unsigned int)((v_rbx) & (0xC000000DULL));
    if (a1 == 0) goto loc_004B986A;
    a2 = (a1) - (a1);
    goto loc_004B986D;
loc_004B986A:
loc_004B986D:
    if (a1 == 0) goto loc_004B9D03;
    v_stack_m38 = 0 + 0 * 1;
    if (((unsigned int)(0 + 0 * 1 + 2)) < ((unsigned int)(0 + 0 * 1))) goto loc_004B9A1A;
    if (((unsigned int)(0 + 0 * 1 + 2 + 3)) < ((unsigned int)(0 + 0 * 1 + 2))) goto loc_004B9A1A;
    v_r11 = (unsigned int)((0 + 0 * 1 + 2 + 3) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_r11 = (unsigned int)((v_r11) + (40));
    if (((unsigned int)(v_r11)) < 40) goto loc_004B9A1A;
    if (((unsigned int)(*(unsigned int *)(a1 + 12)) * 4) > ((unsigned int)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((unsigned int)((unsigned int)(a2) - 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)) * 4))) goto loc_004B9807;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1 + 4)) - (1));
    if (condition_is_equal) goto loc_004B9A24;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004B9A24;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004B9993;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_004B990A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004B9A24;
    if (((unsigned int)(a1)) != 10) goto loc_004B9A62;
loc_004B990A:
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 12))) << (4);
    if (a2 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((unsigned int)(v_r11 + a2 * 1)) < ((unsigned int)(v_r11))) goto loc_004B9A1A;
loc_004B9929:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))))) goto loc_004B9A62;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_004B9807;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(result)) < 4) goto loc_004B9807;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_004B9A1A;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + 4)));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))))) goto loc_004B9807;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)) + 3)) < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))))) goto loc_004B9A1A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)) + 3) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    if (((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(v_r11 + a2 * 1))))) goto loc_004B9A1A;
    a2 = (unsigned int)((0) + 1);
    goto loc_004B9929;
loc_004B9993:
    a2 = (a2) << (4);
    if (a2 > ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)))) goto loc_004B9A1A;
    if (((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) < ((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1))))) goto loc_004B9A1A;
loc_004B99AB:
    if (0 >= (*(unsigned int *)(a1 + 12))) goto loc_004B9A62;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_004B9807;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + 4))) goto loc_004B9807;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))) + (a1);
    result = RtlStringCbLengthW(a1, (unsigned int)((unsigned int)(result)), v_stack_m38, (unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + 4);
    if (sign_flag) goto loc_004B9D03;
    if (((unsigned int)(v_stack_m38 + 2)) < ((unsigned int)(v_stack_m38))) goto loc_004B9A1A;
    if (((unsigned int)(v_stack_m38 + 2 + 3)) < ((unsigned int)(v_stack_m38 + 2))) goto loc_004B9A1A;
    result = (unsigned int)((v_stack_m38 + 2 + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1))))) goto loc_004B9A1A;
    v_r12 = (unsigned int)((0) + 1);
    goto loc_004B99AB;
loc_004B9A1A:
    goto loc_004B9D03;
loc_004B9A24:
    a2 = ((unsigned int)((unsigned int)(result))) << (3);
    if (a2 > v_stack_m38) goto loc_004B9A1A;
    if (((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) * 1)) + a2 * 1)) < ((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) * 1))))) goto loc_004B9A1A;
loc_004B9A3B:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))))) goto loc_004B9A62;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_004B9807;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(result)) < 8) goto loc_004B9807;
    a1 = (unsigned int)((0) + 1);
    goto loc_004B9A3B;
loc_004B9A62:
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) * 1)) + a2 * 1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) >= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) * 1)) + a2 * 1))))) goto loc_004B9A79;
    goto loc_004B9D03;
loc_004B9A79:
    a2 = 0;
    result = memset(a3, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + (unsigned int)((unsigned int)(v_r11 + a2 * 1)) * 1)) + a2 * 1)) * 1)) + a2 * 1)))), 2);
    *(unsigned __int16 *)(a3 + 16) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 4));
    *(unsigned __int16 *)(a3 + 18) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 6));
    *(unsigned int *)(a3 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    *(unsigned int *)(a3 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)));
    if (((unsigned int)(0 + 0 * 1 + 2 + 40)) < 40) goto loc_004B9A1A;
    if (((unsigned int)(0 + 0 * 1 + 2 + 40 + 3)) < ((unsigned int)(0 + 0 * 1 + 2 + 40))) goto loc_004B9A1A;
    a2 = ((unsigned int)(*(unsigned int *)(a1))) + (a1);
    v_rbx = (unsigned int)((0 + 0 * 1 + 2 + 40 + 3) & (0xFFFFFFFCULL));
    result = memcpy(a3 + 40, a2, (unsigned int)((unsigned int)(0 + 0 * 1 + 2)), 2);
    result = (unsigned __int16)(((unsigned __int16)(0 + 0 * 1 + 2)) - (2));
    *(unsigned __int64 *)(a3 + 8) = a3 + 40;
    a2 = ((unsigned int)((unsigned int)(v_rbx))) + (a3);
    *(unsigned __int16 *)(a3) = (unsigned __int16)(result);
    *(unsigned __int16 *)(a3 + 2) = (unsigned __int16)(0 + 0 * 1 + 2);
    a1 = (unsigned int)((*(unsigned __int16 *)(a3 + 16)) - (1));
    if (condition_is_equal) goto loc_004B9CB6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004B9CB6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004B9BD9;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_004B9B28;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004B9CB6;
    if (((unsigned int)(a1)) != 10) goto loc_004B9807;
loc_004B9B28:
    result = ((unsigned int)(*(unsigned int *)(a3 + 24))) << (4);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((unsigned int)(result + v_rbx * 1)) < ((unsigned int)(v_rbx))) goto loc_004B9A1A;
    *(unsigned __int64 *)(a3 + 32) = a2;
loc_004B9B59:
    if (0 >= (*(unsigned int *)(a3 + 24))) goto loc_004B9D03;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)) + (unsigned int)((unsigned int)(result + v_rbx * 1)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(result + v_rbx * 1))))) goto loc_004B9A1A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)) + (unsigned int)((unsigned int)(result + v_rbx * 1)) * 1 + 3)) < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)) + (unsigned int)((unsigned int)(result + v_rbx * 1)) * 1))) goto loc_004B9A1A;
    v_r12 = (0) + (0);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)) + (unsigned int)((unsigned int)(result + v_rbx * 1)) * 1 + 3) & (0xFFFFFFFCULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 32) + v_r12 * 8) = 0;
    result = *(unsigned __int64 *)(a3 + 32);
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))) != 0) {
        a2 = *(unsigned int *)(a1 + 0 * 4 + 16);
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1)));
        a2 = (a2) + (4);
        a1 = a3 + result + v_rbx * 1 * 1;
        a2 = (a2) + (a1);
        result = memcpy(a1, a2, a3, 2);
        result = *(unsigned __int64 *)(a3 + 32);
        a1 = v_stack_p8;
        *(unsigned __int64 *)(result + v_r12 * 8) = a3 + result + v_rbx * 1 * 1;
    }
    v_rbp = ((unsigned int)((unsigned int)(v_r15))) + (a3);
    v_r13 = (unsigned int)((0) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 32) + v_r12 * 8 + 8) = (unsigned int)(a1);
    goto loc_004B9B59;
loc_004B9BD9:
    result = ((unsigned int)(*(unsigned int *)(a3 + 24))) << (4);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((unsigned int)(result + 0 * 1)) < 0) goto loc_004B9A1A;
    *(unsigned __int64 *)(a3 + 32) = a2;
loc_004B9C08:
    v_stack_p8 = 0;
    if (0 >= (*(unsigned int *)(a3 + 24))) goto loc_004B9D03;
    v_stack_m30 = 0;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))) + (a1);
    result = RtlStringCbLengthW(a1, v_r15, v_stack_m38, 2);
    if (sign_flag) goto loc_004B9D03;
    if (((unsigned int)(v_stack_m38 + 2)) < ((unsigned int)(v_stack_m38))) goto loc_004B9A1A;
    if (((unsigned int)(v_stack_m38 + 2 + (unsigned int)((unsigned int)(result + 0 * 1)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(result + 0 * 1))))) goto loc_004B9A1A;
    if (((unsigned int)(v_stack_m38 + 2 + (unsigned int)((unsigned int)(result + 0 * 1)) * 1 + 3)) < ((unsigned int)(v_stack_m38 + 2 + (unsigned int)((unsigned int)(result + 0 * 1)) * 1))) goto loc_004B9A1A;
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))) + (a1);
    v_rbp = (unsigned int)((v_stack_m38 + 2 + (unsigned int)((unsigned int)(result + 0 * 1)) * 1 + 3) & (0xFFFFFFFCULL));
    result = memcpy(a3 + result + 0 * 1 * 1, a2, (unsigned int)((unsigned int)(v_stack_m38 + 2)), 2);
    a2 = (v_stack_m30) + (v_stack_m30);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 32) + a2 * 8 + 8) = a3 + result + 0 * 1 * 1;
    v_r13 = ((unsigned int)((unsigned int)(v_rbp))) + (a3);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 32) + a2 * 8) = (unsigned __int16)(v_stack_m38 + 2 - 2);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 32) + a2 * 8 + 2) = (unsigned __int16)(v_stack_m38 + 2);
    result = (unsigned int)(((unsigned int)(v_stack_p8)) + 1);
    goto loc_004B9C08;
loc_004B9CB6:
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24))))) << (3);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    result = (unsigned int)((result) + (0));
    if (((unsigned int)(result)) < 0) goto loc_004B9A1A;
    *(unsigned __int64 *)(a3 + 32) = a2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24))) == 0) goto loc_004B9D03;
loc_004B9CE2:
    v_rdi = (unsigned int)((v_rdi) + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 32) + 0 * 8) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1);
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(a3 + 24))) goto loc_004B9CE2;
    goto loc_004B9D03;
loc_004B9CFE:
loc_004B9D03:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepConvertRelativeToAbsoluteTokenAttribute(void *Arg1, int32_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rdi = 0;
    if (Arg1 == NULL) goto loc_004B9CFE;
    if (Arg3 == NULL) goto loc_004B9CFE;
    if (Arg4 == NULL) goto loc_004B9CFE;
    if (((uint32_t)((uint32_t)(Arg2))) >= 20) goto loc_004B9811;
loc_004B9807:
    goto loc_004B9D03;
loc_004B9811:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))) == 0) goto loc_004B9807;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) goto loc_004B9807;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))));
    if (((uint32_t)(Arg1)) < 4) goto loc_004B9807;
    result = ((uint32_t)(*(uint32_t *)(arg1))) + (Arg1);
    if (condition_is_equal) goto loc_004B9CFE;
    Arg1 = (Arg1) >> (1);
    if (condition_is_equal) goto loc_004B9850;
loc_004B9842:
    if ((*(uint16_t *)(result)) == 0) goto loc_004B9850;
    result = (result) + (2);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_004B9842;
loc_004B9850:
    result = -(Arg1);
    local_rbx = (uint32_t)(~((uint32_t)(0xC0000077ULL)));
    local_rbx = (uint32_t)((local_rbx) & (0xC000000DULL));
    if (Arg1 == NULL) goto loc_004B986A;
    Arg2 = (Arg1) - (Arg1);
    goto loc_004B986D;
loc_004B986A:
loc_004B986D:
    if (Arg1 == NULL) goto loc_004B9D03;
    v_stack_m38 = 0 + 0 * 1;
    if (((uint32_t)(0 + 0 * 1 + 2)) < ((uint32_t)(0 + 0 * 1))) goto loc_004B9A1A;
    if (((uint32_t)(0 + 0 * 1 + 2 + 3)) < ((uint32_t)(0 + 0 * 1 + 2))) goto loc_004B9A1A;
    local_r11 = (uint32_t)((0 + 0 * 1 + 2 + 3) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    local_r11 = (uint32_t)((local_r11) + (40));
    if (((uint32_t)(local_r11)) < 40) goto loc_004B9A1A;
    if (((uint32_t)(*(uint32_t *)(arg1 + 0xC)) * 4) > ((uint32_t)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((uint32_t)((uint32_t)(Arg2) - 16)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)) * 4))) goto loc_004B9807;
    Arg1 = (uint32_t)((*(uint16_t *)(arg1 + 0x4)) - (1));
    if (condition_is_equal) goto loc_004B9A24;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004B9A24;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004B9993;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_004B990A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004B9A24;
    if (((uint32_t)(Arg1)) != 10) goto loc_004B9A62;
loc_004B990A:
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0xC))) << (4);
    if (Arg2 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((uint32_t)(local_r11 + Arg2 * 1)) < ((uint32_t)(local_r11))) goto loc_004B9A1A;
loc_004B9929:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))))) goto loc_004B9A62;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))))) goto loc_004B9807;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(result)) < 4) goto loc_004B9807;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + 4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))))) goto loc_004B9A1A;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + 4)));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1))))) goto loc_004B9807;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)) + 3)) < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1))))) goto loc_004B9A1A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)) + 3) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    if (((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(local_r11 + Arg2 * 1))))) goto loc_004B9A1A;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_004B9929;
loc_004B9993:
    Arg2 = (Arg2) << (4);
    if (Arg2 > ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)))) goto loc_004B9A1A;
    if (((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) < ((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1))))) goto loc_004B9A1A;
loc_004B99AB:
    if (0 >= (*(uint32_t *)(arg1 + 0xC))) goto loc_004B9A62;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))))) goto loc_004B9807;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + 4))) goto loc_004B9807;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))) + (Arg1);
    result = RtlStringCbLengthW(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m38, (uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + 4);
    if (sign_flag) goto loc_004B9D03;
    if (((uint32_t)(v_stack_m38 + 2)) < ((uint32_t)(v_stack_m38))) goto loc_004B9A1A;
    if (((uint32_t)(v_stack_m38 + 2 + 3)) < ((uint32_t)(v_stack_m38 + 2))) goto loc_004B9A1A;
    result = (uint32_t)((v_stack_m38 + 2 + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1))))) goto loc_004B9A1A;
    local_r12 = (uint32_t)((0) + 1);
    goto loc_004B99AB;
loc_004B9A1A:
    goto loc_004B9D03;
loc_004B9A24:
    Arg2 = ((uint32_t)((uint32_t)(result))) << (3);
    if (Arg2 > v_stack_m38) goto loc_004B9A1A;
    if (((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) * 1)) + Arg2 * 1)) < ((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) * 1))))) goto loc_004B9A1A;
loc_004B9A3B:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))))) goto loc_004B9A62;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))))) goto loc_004B9807;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(result)) < 8) goto loc_004B9807;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_004B9A3B;
loc_004B9A62:
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) * 1)) + Arg2 * 1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) >= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) * 1)) + Arg2 * 1))))) goto loc_004B9A79;
    goto loc_004B9D03;
loc_004B9A79:
    Arg2 = 0;
    result = memset(Arg3, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + (uint32_t)((uint32_t)(local_r11 + Arg2 * 1)) * 1)) + Arg2 * 1)) * 1)) + Arg2 * 1)))), 2);
    *(uint16_t *)(arg3 + 0x10) = (uint16_t)(*(uint16_t *)(arg1 + 0x4));
    *(uint16_t *)(arg3 + 0x12) = (uint16_t)(*(uint16_t *)(arg1 + 0x6));
    *(uint32_t *)(arg3 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)));
    if (((uint32_t)(0 + 0 * 1 + 2 + 40)) < 40) goto loc_004B9A1A;
    if (((uint32_t)(0 + 0 * 1 + 2 + 40 + 3)) < ((uint32_t)(0 + 0 * 1 + 2 + 40))) goto loc_004B9A1A;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1))) + (Arg1);
    local_rbx = (uint32_t)((0 + 0 * 1 + 2 + 40 + 3) & (0xFFFFFFFCULL));
    result = memcpy(Arg3 + 40, Arg2, (uint32_t)((uint32_t)(0 + 0 * 1 + 2)), 2);
    result = (uint16_t)(((uint16_t)(0 + 0 * 1 + 2)) - (2));
    *(void **)(arg3 + 0x8) = Arg3 + 40;
    Arg2 = ((uint32_t)((uint32_t)(local_rbx))) + (Arg3);
    *(uint16_t *)(arg3) = (uint16_t)(result);
    *(uint16_t *)(arg3 + 0x2) = (uint16_t)(0 + 0 * 1 + 2);
    Arg1 = (uint32_t)((*(uint16_t *)(arg3 + 0x10)) - (1));
    if (condition_is_equal) goto loc_004B9CB6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004B9CB6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004B9BD9;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_004B9B28;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004B9CB6;
    if (((uint32_t)(Arg1)) != 10) goto loc_004B9807;
loc_004B9B28:
    result = ((uint32_t)(*(uint32_t *)(arg3 + 0x18))) << (4);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((uint32_t)(result + local_rbx * 1)) < ((uint32_t)(local_rbx))) goto loc_004B9A1A;
    *(uint64_t *)(arg3 + 0x20) = Arg2;
loc_004B9B59:
    if (0 >= (*(uint32_t *)(arg3 + 0x18))) goto loc_004B9D03;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)) + (uint32_t)((uint32_t)(result + local_rbx * 1)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(result + local_rbx * 1))))) goto loc_004B9A1A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)) + (uint32_t)((uint32_t)(result + local_rbx * 1)) * 1 + 3)) < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)) + (uint32_t)((uint32_t)(result + local_rbx * 1)) * 1))) goto loc_004B9A1A;
    local_r12 = (0) + (0);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)) + (uint32_t)((uint32_t)(result + local_rbx * 1)) * 1 + 3) & (0xFFFFFFFCULL));
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x20) + local_r12 * 8) = 0;
    result = *(uint64_t *)(arg3 + 0x20);
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1))) != 0) {
        Arg2 = *(uint32_t *)(arg1 + 0x0 * 4 + 0x10);
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1)));
        Arg2 = (Arg2) + (4);
        Arg1 = Arg3 + result + local_rbx * 1 * 1;
        Arg2 = (Arg2) + (Arg1);
        result = memcpy(Arg1, Arg2, Arg3, 2);
        result = *(uint64_t *)(arg3 + 0x20);
        Arg1 = v_stack_p8;
        *(void **)(result + local_r12 * 8) = Arg3 + result + local_rbx * 1 * 1;
    }
    local_rbp = ((uint32_t)((uint32_t)(local_r15))) + (Arg3);
    local_r13 = (uint32_t)((0) + 1);
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x20) + local_r12 * 8 + 0x8) = (uint32_t)(Arg1);
    goto loc_004B9B59;
loc_004B9BD9:
    result = ((uint32_t)(*(uint32_t *)(arg3 + 0x18))) << (4);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    if (((uint32_t)(result + 0 * 1)) < 0) goto loc_004B9A1A;
    *(uint64_t *)(arg3 + 0x20) = Arg2;
loc_004B9C08:
    v_stack_p8 = 0;
    if (0 >= (*(uint32_t *)(arg3 + 0x18))) goto loc_004B9D03;
    v_stack_m30 = 0;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))) + (Arg1);
    result = RtlStringCbLengthW(Arg1, local_r15, v_stack_m38, 2);
    if (sign_flag) goto loc_004B9D03;
    if (((uint32_t)(v_stack_m38 + 2)) < ((uint32_t)(v_stack_m38))) goto loc_004B9A1A;
    if (((uint32_t)(v_stack_m38 + 2 + (uint32_t)((uint32_t)(result + 0 * 1)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(result + 0 * 1))))) goto loc_004B9A1A;
    if (((uint32_t)(v_stack_m38 + 2 + (uint32_t)((uint32_t)(result + 0 * 1)) * 1 + 3)) < ((uint32_t)(v_stack_m38 + 2 + (uint32_t)((uint32_t)(result + 0 * 1)) * 1))) goto loc_004B9A1A;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10))) + (Arg1);
    local_rbp = (uint32_t)((v_stack_m38 + 2 + (uint32_t)((uint32_t)(result + 0 * 1)) * 1 + 3) & (0xFFFFFFFCULL));
    result = memcpy(Arg3 + result + 0 * 1 * 1, Arg2, (uint32_t)((uint32_t)(v_stack_m38 + 2)), 2);
    Arg2 = (v_stack_m30) + (v_stack_m30);
    *(void **)(*(uint64_t *)(arg3 + 0x20) + Arg2 * 8 + 0x8) = Arg3 + result + 0 * 1 * 1;
    local_r13 = ((uint32_t)((uint32_t)(local_rbp))) + (Arg3);
    *(uint16_t *)(*(uint64_t *)(arg3 + 0x20) + Arg2 * 8) = (uint16_t)(v_stack_m38 + 2 - 2);
    *(uint16_t *)(*(uint64_t *)(arg3 + 0x20) + Arg2 * 8 + 0x2) = (uint16_t)(v_stack_m38 + 2);
    result = (uint32_t)(((uint32_t)(v_stack_p8)) + 1);
    goto loc_004B9C08;
loc_004B9CB6:
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18))))) << (3);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_004B9A1A;
    result = (uint32_t)((result) + (0));
    if (((uint32_t)(result)) < 0) goto loc_004B9A1A;
    *(uint64_t *)(arg3 + 0x20) = Arg2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18))) == 0) goto loc_004B9D03;
loc_004B9CE2:
    local_rdi = (uint32_t)((local_rdi) + 1);
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x20) + 0x0 * 8) = *(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 4 + 0x10)) + arg1 * 1);
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(arg3 + 0x18))) goto loc_004B9CE2;
    goto loc_004B9D03;
loc_004B9CFE:
loc_004B9D03:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0 + r12*4` | `64` | `R` |
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10 + r11*4` | `32` | `R` |
| `Arg1` | `+ 0x10 + rax*4` | `32` | `R` |
| `Arg1` | `+ 0x10 + rdx*4` | `32` | `R` |
| `Arg3` | `+ 0x0` | `16` | `W` |
| `Arg3` | `+ 0x0 + rcx*1` | `64` | `R` |
| `Arg3` | `+ 0x2` | `16` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `16` | `R` |
| `Arg3` | `+ 0x10` | `16` | `W` |
| `Arg3` | `+ 0x12` | `16` | `W` |
| `Arg3` | `+ 0x14` | `32` | `W` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x18` | `32` | `W` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `W` |
| `Arg3` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B97BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
