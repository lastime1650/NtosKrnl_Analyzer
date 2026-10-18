# CmpParseInfBuffer

- RVA: `0x00C28734`–`0x00C28C0A` (길이 `1,238` bytes)
- VA: `0x0000000140C28734`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5C40`
- 디코드: `358`개 명령, `1,238/1,238` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C28774` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C287C9` → [CmpGetToken](CmpGetToken_function_00C28488.md) (function, `0x00C28488`)
- `0x00C28876` → [CmpAppendSection](CmpAppendSection_function_00C28158.md) (function, `0x00C28158`)
- `0x00C288B0` → [CmpAppendSection](CmpAppendSection_function_00C28158.md) (function, `0x00C28158`)
- `0x00C28972` → [CmpAppendLine](CmpAppendLine_function_00C280D0.md) (function, `0x00C280D0`)
- `0x00C28988` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)
- `0x00C289AC` → [CmpAppendLine](CmpAppendLine_function_00C280D0.md) (function, `0x00C280D0`)
- `0x00C289DC` → [CmpAppendLine](CmpAppendLine_function_00C280D0.md) (function, `0x00C280D0`)
- `0x00C289F2` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)
- `0x00C28A17` → [CmpAppendLine](CmpAppendLine_function_00C280D0.md) (function, `0x00C280D0`)
- `0x00C28A2F` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)
- `0x00C28AAF` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)
- `0x00C28AEE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C28B02` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C28B0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C28B33` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)
- `0x00C28B66` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)
- `0x00C28BAF` → [CmpAppendValue](CmpAppendValue_function_00C2826C.md) (function, `0x00C2826C`)

### Direct callers
- [EmpParseInfDatabase](EmpParseInfDatabase_function_00C26934.md) at `0x00C26990`

### Static image references
- `0x00C28913` → RVA `0x00C82170` (`EmptyValue`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C28774` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C28AEE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C28B02` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C28B0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C28734  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C28739  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00C2873E  55                              push rbp
00C2873F  56                              push rsi
00C28740  57                              push rdi
00C28741  41 54                           push r12
00C28743  41 55                           push r13
00C28745  41 56                           push r14
00C28747  41 57                           push r15
00C28749  48 8B EC                        mov rbp, rsp
00C2874C  48 83 EC 50                     sub rsp, 0x50
00C28750  33 C0                           xor eax, eax
00C28752  8B FA                           mov edi, edx
00C28754  48 8B D9                        mov rbx, rcx
00C28757  89 45 F8                        mov dword ptr [rbp - 8], eax
00C2875A  0F 57 C0                        xorps xmm0, xmm0
00C2875D  33 F6                           xor esi, esi
00C2875F  B9 00 01 00 00                  mov ecx, 0x100
00C28764  41 B8 43 4D 70 69               mov r8d, 0x69704d43
00C2876A  8D 50 30                        lea edx, [rax + 0x30]
00C2876D  44 8A E6                        mov r12b, sil
00C28770  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C28774  E8 77 99 F5 FF                  call 0x140b820f0
00C28779  4C 8B F0                        mov r14, rax
00C2877C  48 85 C0                        test rax, rax
00C2877F  0F 84 6C 04 00 00               je 0x140c28bf1
00C28785  41 BF 01 00 00 00               mov r15d, 1
00C2878B  48 89 30                        mov qword ptr [rax], rsi
00C2878E  48 89 70 08                     mov qword ptr [rax + 8], rsi
00C28792  4C 8B EE                        mov r13, rsi
00C28795  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C28799  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C2879D  89 70 20                        mov dword ptr [rax + 0x20], esi
00C287A0  48 89 70 28                     mov qword ptr [rax + 0x28], rsi
00C287A4  48 8D 04 3B                     lea rax, [rbx + rdi]
00C287A8  48 89 5D D8                     mov qword ptr [rbp - 0x28], rbx
00C287AC  41 8B FF                        mov edi, r15d
00C287AF  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00C287B3  40 8A DE                        mov bl, sil
00C287B6  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
00C287BA  44 89 7D 58                     mov dword ptr [rbp + 0x58], r15d
00C287BE  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00C287C2  48 8B D0                        mov rdx, rax
00C287C5  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C287C9  E8 BA FC FF FF                  call 0x140c28488
00C287CE  41 B9 06 00 00 00               mov r9d, 6
00C287D4  45 3B F9                        cmp r15d, r9d
00C287D7  0F 87 67 02 00 00               ja 0x140c28a44
00C287DD  0F 84 67 01 00 00               je 0x140c2894a
00C287E3  41 8B C7                        mov eax, r15d
00C287E6  83 E8 01                        sub eax, 1
00C287E9  0F 84 37 01 00 00               je 0x140c28926
00C287EF  83 E8 01                        sub eax, 1
00C287F2  0F 84 F5 00 00 00               je 0x140c288ed
00C287F8  83 E8 01                        sub eax, 1
00C287FB  0F 84 D9 00 00 00               je 0x140c288da
00C28801  83 E8 01                        sub eax, 1
00C28804  74 4A                           je 0x140c28850
00C28806  83 F8 01                        cmp eax, 1
00C28809  75 56                           jne 0x140c28861
00C2880B  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C2880E  8B CF                           mov ecx, edi
00C28810  85 FF                           test edi, edi
00C28812  0F 84 B6 00 00 00               je 0x140c288ce
00C28818  8B D0                           mov edx, eax
00C2881A  2B C8                           sub ecx, eax
00C2881C  0F 84 A5 02 00 00               je 0x140c28ac7
00C28822  2B C8                           sub ecx, eax
00C28824  74 1F                           je 0x140c28845
00C28826  83 F9 02                        cmp ecx, 2
00C28829  74 0A                           je 0x140c28835
00C2882B  8A DA                           mov bl, dl
00C2882D  40 8A F2                        mov sil, dl
00C28830  E9 9B 02 00 00                  jmp 0x140c28ad0
00C28835  4C 8B 6D F0                     mov r13, qword ptr [rbp - 0x10]
00C28839  45 8B F9                        mov r15d, r9d
00C2883C  44 8A 65 F8                     mov r12b, byte ptr [rbp - 8]
00C28840  E9 82 02 00 00                  jmp 0x140c28ac7
00C28845  41 BF 02 00 00 00               mov r15d, 2
00C2884B  E9 77 02 00 00                  jmp 0x140c28ac7
00C28850  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C28853  85 FF                           test edi, edi
00C28855  74 4F                           je 0x140c288a6
00C28857  83 FF 01                        cmp edi, 1
00C2885A  74 10                           je 0x140c2886c
00C2885C  BF 01 00 00 00                  mov edi, 1
00C28861  40 8A DF                        mov bl, dil
00C28864  40 8A F7                        mov sil, dil
00C28867  E9 64 02 00 00                  jmp 0x140c28ad0
00C2886C  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00C28870  45 8A C4                        mov r8b, r12b
00C28873  49 8B CE                        mov rcx, r14
00C28876  E8 DD F8 FF FF                  call 0x140c28158
00C2887B  45 33 C0                        xor r8d, r8d
00C2887E  41 8D 50 01                     lea edx, [r8 + 1]
00C28882  84 C0                           test al, al
00C28884  75 07                           jne 0x140c2888d
00C28886  8A DA                           mov bl, dl
00C28888  40 8A F2                        mov sil, dl
00C2888B  EB 06                           jmp 0x140c28893
00C2888D  41 BF 05 00 00 00               mov r15d, 5
00C28893  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00C28897  84 C0                           test al, al
00C28899  49 0F 45 C8                     cmovne rcx, r8
00C2889D  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00C288A1  E9 21 02 00 00                  jmp 0x140c28ac7
00C288A6  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00C288AA  45 8A C4                        mov r8b, r12b
00C288AD  49 8B CE                        mov rcx, r14
00C288B0  E8 A3 F8 FF FF                  call 0x140c28158
00C288B5  33 D2                           xor edx, edx
00C288B7  84 C0                           test al, al
00C288B9  75 0F                           jne 0x140c288ca
00C288BB  B8 01 00 00 00                  mov eax, 1
00C288C0  8A D8                           mov bl, al
00C288C2  40 8A F0                        mov sil, al
00C288C5  E9 06 02 00 00                  jmp 0x140c28ad0
00C288CA  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
00C288CE  BA 01 00 00 00                  mov edx, 1
00C288D3  8A DA                           mov bl, dl
00C288D5  E9 ED 01 00 00                  jmp 0x140c28ac7
00C288DA  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C288DD  83 FF 03                        cmp edi, 3
00C288E0  75 D9                           jne 0x140c288bb
00C288E2  41 BF 04 00 00 00               mov r15d, 4
00C288E8  E9 D5 01 00 00                  jmp 0x140c28ac2
00C288ED  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C288F0  8B CF                           mov ecx, edi
00C288F2  83 E9 03                        sub ecx, 3
00C288F5  74 1A                           je 0x140c28911
00C288F7  83 F9 01                        cmp ecx, 1
00C288FA  75 BF                           jne 0x140c288bb
00C288FC  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00C28900  44 8D 79 02                     lea r15d, [rcx + 2]
00C28904  44 8A 65 F8                     mov r12b, byte ptr [rbp - 8]
00C28908  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00C2890C  E9 B1 01 00 00                  jmp 0x140c28ac2
00C28911  33 D2                           xor edx, edx
00C28913  48 8D 05 56 98 05 00            lea rax, [rip + 0x59856]
00C2891A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C2891E  44 8A E2                        mov r12b, dl
00C28921  88 55 F8                        mov byte ptr [rbp - 8], dl
00C28924  EB BC                           jmp 0x140c288e2
00C28926  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C28929  8B CF                           mov ecx, edi
00C2892B  85 FF                           test edi, edi
00C2892D  74 9F                           je 0x140c288ce
00C2892F  83 E9 01                        sub ecx, 1
00C28932  0F 84 8A 01 00 00               je 0x140c28ac2
00C28938  83 E9 01                        sub ecx, 1
00C2893B  0F 85 7A FF FF FF               jne 0x140c288bb
00C28941  44 8D 79 02                     lea r15d, [rcx + 2]
00C28945  E9 78 01 00 00                  jmp 0x140c28ac2
00C2894A  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C2894D  8B CF                           mov ecx, edi
00C2894F  85 FF                           test edi, edi
00C28951  0F 84 B8 00 00 00               je 0x140c28a0f
00C28957  83 E9 01                        sub ecx, 1
00C2895A  74 78                           je 0x140c289d4
00C2895C  83 E9 04                        sub ecx, 4
00C2895F  74 42                           je 0x140c289a3
00C28961  83 F9 01                        cmp ecx, 1
00C28964  0F 85 51 FF FF FF               jne 0x140c288bb
00C2896A  45 33 C0                        xor r8d, r8d
00C2896D  33 D2                           xor edx, edx
00C2896F  49 8B CE                        mov rcx, r14
00C28972  E8 59 F7 FF FF                  call 0x140c280d0
00C28977  84 C0                           test al, al
00C28979  0F 84 3D 02 00 00               je 0x140c28bbc
00C2897F  45 8A C4                        mov r8b, r12b
00C28982  49 8B D5                        mov rdx, r13
00C28985  49 8B CE                        mov rcx, r14
00C28988  E8 DF F8 FF FF                  call 0x140c2826c
00C2898D  33 D2                           xor edx, edx
00C2898F  84 C0                           test al, al
00C28991  0F 84 25 02 00 00               je 0x140c28bbc
00C28997  44 8B EA                        mov r13d, edx
00C2899A  44 8D 7A 07                     lea r15d, [rdx + 7]
00C2899E  E9 1F 01 00 00                  jmp 0x140c28ac2
00C289A3  45 8A C4                        mov r8b, r12b
00C289A6  49 8B D5                        mov rdx, r13
00C289A9  49 8B CE                        mov rcx, r14
00C289AC  E8 1F F7 FF FF                  call 0x140c280d0
00C289B1  45 33 C0                        xor r8d, r8d
00C289B4  41 8D 50 01                     lea edx, [r8 + 1]
00C289B8  84 C0                           test al, al
00C289BA  75 07                           jne 0x140c289c3
00C289BC  8A DA                           mov bl, dl
00C289BE  40 8A F2                        mov sil, dl
00C289C1  EB 06                           jmp 0x140c289c9
00C289C3  41 BF 08 00 00 00               mov r15d, 8
00C289C9  84 C0                           test al, al
00C289CB  4D 0F 45 E8                     cmovne r13, r8
00C289CF  E9 F3 00 00 00                  jmp 0x140c28ac7
00C289D4  45 33 C0                        xor r8d, r8d
00C289D7  33 D2                           xor edx, edx
00C289D9  49 8B CE                        mov rcx, r14
00C289DC  E8 EF F6 FF FF                  call 0x140c280d0
00C289E1  84 C0                           test al, al
00C289E3  0F 84 D3 01 00 00               je 0x140c28bbc
00C289E9  45 8A C4                        mov r8b, r12b
00C289EC  49 8B D5                        mov rdx, r13
00C289EF  49 8B CE                        mov rcx, r14
00C289F2  E8 75 F8 FF FF                  call 0x140c2826c
00C289F7  33 D2                           xor edx, edx
00C289F9  84 C0                           test al, al
00C289FB  0F 84 BB 01 00 00               je 0x140c28bbc
00C28A01  44 8B EA                        mov r13d, edx
00C28A04  41 BF 05 00 00 00               mov r15d, 5
00C28A0A  E9 B3 00 00 00                  jmp 0x140c28ac2
00C28A0F  45 33 C0                        xor r8d, r8d
00C28A12  33 D2                           xor edx, edx
00C28A14  49 8B CE                        mov rcx, r14
00C28A17  E8 B4 F6 FF FF                  call 0x140c280d0
00C28A1C  33 DB                           xor ebx, ebx
00C28A1E  84 C0                           test al, al
00C28A20  0F 84 96 01 00 00               je 0x140c28bbc
00C28A26  45 8A C4                        mov r8b, r12b
00C28A29  49 8B D5                        mov rdx, r13
00C28A2C  49 8B CE                        mov rcx, r14
00C28A2F  E8 38 F8 FF FF                  call 0x140c2826c
00C28A34  84 C0                           test al, al
00C28A36  0F 84 80 01 00 00               je 0x140c28bbc
00C28A3C  44 8B EB                        mov r13d, ebx
00C28A3F  E9 8A FE FF FF                  jmp 0x140c288ce
00C28A44  41 8B C7                        mov eax, r15d
00C28A47  BA 07 00 00 00                  mov edx, 7
00C28A4C  2B C2                           sub eax, edx
00C28A4E  0F 84 2A 01 00 00               je 0x140c28b7e
00C28A54  83 E8 01                        sub eax, 1
00C28A57  74 2E                           je 0x140c28a87
00C28A59  83 E8 01                        sub eax, 1
00C28A5C  74 09                           je 0x140c28a67
00C28A5E  83 F8 01                        cmp eax, 1
00C28A61  0F 85 FA FD FF FF               jne 0x140c28861
00C28A67  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C28A6A  8B CF                           mov ecx, edi
00C28A6C  85 FF                           test edi, edi
00C28A6E  0F 84 5A FE FF FF               je 0x140c288ce
00C28A74  83 E9 01                        sub ecx, 1
00C28A77  74 8B                           je 0x140c28a04
00C28A79  83 F9 05                        cmp ecx, 5
00C28A7C  0F 85 39 FE FF FF               jne 0x140c288bb
00C28A82  44 8B FA                        mov r15d, edx
00C28A85  EB 3B                           jmp 0x140c28ac2
00C28A87  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C28A8A  33 C0                           xor eax, eax
00C28A8C  8B CF                           mov ecx, edi
00C28A8E  85 FF                           test edi, edi
00C28A90  0F 84 B6 00 00 00               je 0x140c28b4c
00C28A96  83 E9 01                        sub ecx, 1
00C28A99  74 7E                           je 0x140c28b19
00C28A9B  83 F9 03                        cmp ecx, 3
00C28A9E  0F 85 17 FE FF FF               jne 0x140c288bb
00C28AA4  44 8A 45 F8                     mov r8b, byte ptr [rbp - 8]
00C28AA8  49 8B CE                        mov rcx, r14
00C28AAB  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00C28AAF  E8 B8 F7 FF FF                  call 0x140c2826c
00C28AB4  84 C0                           test al, al
00C28AB6  0F 84 FF FD FF FF               je 0x140c288bb
00C28ABC  41 BF 09 00 00 00               mov r15d, 9
00C28AC2  BA 01 00 00 00                  mov edx, 1
00C28AC7  40 84 F6                        test sil, sil
00C28ACA  0F 84 FB 00 00 00               je 0x140c28bcb
00C28AD0  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00C28AD3  33 FF                           xor edi, edi
00C28AD5  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00C28AD9  89 01                           mov dword ptr [rcx], eax
00C28ADB  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00C28ADF  48 85 C0                        test rax, rax
00C28AE2  74 0F                           je 0x140c28af3
00C28AE4  45 84 E4                        test r12b, r12b
00C28AE7  74 0A                           je 0x140c28af3
00C28AE9  33 D2                           xor edx, edx
00C28AEB  48 8B C8                        mov rcx, rax
00C28AEE  E8 7D 9D F5 FF                  call 0x140b82870
00C28AF3  4D 85 ED                        test r13, r13
00C28AF6  74 0F                           je 0x140c28b07
00C28AF8  45 84 E4                        test r12b, r12b
00C28AFB  74 0A                           je 0x140c28b07
00C28AFD  33 D2                           xor edx, edx
00C28AFF  49 8B CD                        mov rcx, r13
00C28B02  E8 69 9D F5 FF                  call 0x140b82870
00C28B07  33 D2                           xor edx, edx
00C28B09  49 8B CE                        mov rcx, r14
00C28B0C  E8 5F 9D F5 FF                  call 0x140b82870
00C28B11  4C 8B F7                        mov r14, rdi
00C28B14  E9 B9 00 00 00                  jmp 0x140c28bd2
00C28B19  48 8D 0D 50 96 05 00            lea rcx, [rip + 0x59650]
00C28B20  88 45 F8                        mov byte ptr [rbp - 8], al
00C28B23  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00C28B27  48 8B D1                        mov rdx, rcx
00C28B2A  49 8B CE                        mov rcx, r14
00C28B2D  45 33 C0                        xor r8d, r8d
00C28B30  44 8A E0                        mov r12b, al
00C28B33  E8 34 F7 FF FF                  call 0x140c2826c
00C28B38  84 C0                           test al, al
00C28B3A  0F 85 C4 FE FF FF               jne 0x140c28a04
00C28B40  B8 01 00 00 00                  mov eax, 1
00C28B45  40 8A F0                        mov sil, al
00C28B48  8A D8                           mov bl, al
00C28B4A  EB 84                           jmp 0x140c28ad0
00C28B4C  48 8D 0D 1D 96 05 00            lea rcx, [rip + 0x5961d]
00C28B53  88 45 F8                        mov byte ptr [rbp - 8], al
00C28B56  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00C28B5A  48 8B D1                        mov rdx, rcx
00C28B5D  49 8B CE                        mov rcx, r14
00C28B60  45 33 C0                        xor r8d, r8d
00C28B63  44 8A E0                        mov r12b, al
00C28B66  E8 01 F7 FF FF                  call 0x140c2826c
00C28B6B  84 C0                           test al, al
00C28B6D  40 0F B6 F6                     movzx esi, sil
00C28B71  BA 01 00 00 00                  mov edx, 1
00C28B76  0F 44 F2                        cmove esi, edx
00C28B79  E9 55 FD FF FF                  jmp 0x140c288d3
00C28B7E  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C28B81  83 FF 04                        cmp edi, 4
00C28B84  0F 84 1A FF FF FF               je 0x140c28aa4
00C28B8A  41 3B F9                        cmp edi, r9d
00C28B8D  0F 85 28 FD FF FF               jne 0x140c288bb
00C28B93  48 8D 0D D6 95 05 00            lea rcx, [rip + 0x595d6]
00C28B9A  33 C0                           xor eax, eax
00C28B9C  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00C28BA0  48 8B D1                        mov rdx, rcx
00C28BA3  49 8B CE                        mov rcx, r14
00C28BA6  88 45 F8                        mov byte ptr [rbp - 8], al
00C28BA9  45 33 C0                        xor r8d, r8d
00C28BAC  44 8A E0                        mov r12b, al
00C28BAF  E8 B8 F6 FF FF                  call 0x140c2826c
00C28BB4  84 C0                           test al, al
00C28BB6  0F 85 06 FF FF FF               jne 0x140c28ac2
00C28BBC  BA 01 00 00 00                  mov edx, 1
00C28BC1  8A DA                           mov bl, dl
00C28BC3  40 8A F2                        mov sil, dl
00C28BC6  E9 FC FE FF FF                  jmp 0x140c28ac7
00C28BCB  3B FA                           cmp edi, edx
00C28BCD  75 03                           jne 0x140c28bd2
00C28BCF  01 55 58                        add dword ptr [rbp + 0x58], edx
00C28BD2  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00C28BD6  BF 01 00 00 00                  mov edi, 1
00C28BDB  84 DB                           test bl, bl
00C28BDD  0F 84 DB FB FF FF               je 0x140c287be
00C28BE3  33 C0                           xor eax, eax
00C28BE5  4D 85 F6                        test r14, r14
00C28BE8  74 04                           je 0x140c28bee
00C28BEA  49 89 46 08                     mov qword ptr [r14 + 8], rax
00C28BEE  49 8B C6                        mov rax, r14
00C28BF1  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00C28BF9  48 83 C4 50                     add rsp, 0x50
00C28BFD  41 5F                           pop r15
00C28BFF  41 5E                           pop r14
00C28C01  41 5D                           pop r13
00C28C03  41 5C                           pop r12
00C28C05  5F                              pop rdi
00C28C06  5E                              pop rsi
00C28C07  5D                              pop rbp
00C28C08  C3                              ret
00C28C09  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpParseInfBuffer(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m40 = 0;
    v_rsi = 0;
    v_stack_m50 = v_xmm0;
    result = ExAllocatePool2(256, result + 48, (unsigned int)(0x69704D43ULL), a4);
    if (result == 0) goto loc_00C28BF1;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned int *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
    v_stack_m60 = a1;
    v_stack_m58 = a1 + (unsigned int)(a2) * 1;
    v_stack_m68 = 0;
    v_stack_p20 = 1;
loc_00C287BE:
    result = CmpGetToken(v_stack_m60, a1 + (unsigned int)(a2) * 1, v_stack_m50, a4);
    if (1 > 6) goto loc_00C28A44;
    if (1 == 6) goto loc_00C2894A;
    result = (unsigned int)((1) - (1));
    if (condition_is_equal) goto loc_00C28926;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C288ED;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C288DA;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C28850;
    if (((unsigned int)(result)) != 1) goto loc_00C28861;
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00C288CE;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) - ((unsigned int)(result)));
    if (condition_is_equal) goto loc_00C28AC7;
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    if (condition_is_equal) goto loc_00C28845;
    if (((unsigned int)(a1)) == 2) goto loc_00C28835;
    goto loc_00C28AD0;
loc_00C28835:
    goto loc_00C28AC7;
loc_00C28845:
    goto loc_00C28AC7;
loc_00C28850:
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00C288A6;
    if (((unsigned int)((unsigned int)(v_stack_m50))) == 1) goto loc_00C2886C;
loc_00C28861:
    goto loc_00C28AD0;
loc_00C2886C:
    result = CmpAppendSection(result, v_stack_m68, (unsigned __int8)(v_stack_m40), 6);
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00C2888D;
    goto loc_00C28893;
loc_00C2888D:
loc_00C28893:
    a1 = v_stack_m68;
    if ((unsigned __int8)(result) != 0) { a1 = 0; }
    v_stack_m68 = a1;
    goto loc_00C28AC7;
loc_00C288A6:
    result = CmpAppendSection(result, v_stack_m68, (unsigned __int8)(v_stack_m40), 6);
    a2 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00C288CA;
loc_00C288BB:
    goto loc_00C28AD0;
loc_00C288CA:
    v_stack_m68 = 0;
loc_00C288CE:
loc_00C288D3:
    goto loc_00C28AC7;
loc_00C288DA:
    if (((unsigned int)((unsigned int)(v_stack_m50))) != 3) goto loc_00C288BB;
loc_00C288E2:
    goto loc_00C28AC2;
loc_00C288ED:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) - (3));
    if (condition_is_equal) goto loc_00C28911;
    if (((unsigned int)(a1)) != 1) goto loc_00C288BB;
    v_stack_m68 = v_stack_m48;
    goto loc_00C28AC2;
loc_00C28911:
    a2 = 0;
    v_stack_m48 = v_rip + 366678;
    v_stack_m40 = 0;
    goto loc_00C288E2;
loc_00C28926:
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00C288CE;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C28AC2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00C288BB;
    goto loc_00C28AC2;
loc_00C2894A:
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00C28A0F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C289D4;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00C289A3;
    if (((unsigned int)(a1)) != 1) goto loc_00C288BB;
    a3 = 0;
    a2 = 0;
    result = CmpAppendLine(result, a2, a3, 6);
    if ((unsigned __int8)(result) == 0) goto loc_00C28BBC;
    result = CmpAppendValue(result, v_stack_m48, 0, 6);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00C28BBC;
    goto loc_00C28AC2;
loc_00C289A3:
    result = CmpAppendLine(result, 0, 0, 6);
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00C289C3;
    goto loc_00C289C9;
loc_00C289C3:
loc_00C289C9:
    v_r13 = 0;
    if ((unsigned __int8)(result) != 0) { v_r13 = 0; }
    goto loc_00C28AC7;
loc_00C289D4:
    a3 = 0;
    a2 = 0;
    result = CmpAppendLine(result, a2, a3, 6);
    if ((unsigned __int8)(result) == 0) goto loc_00C28BBC;
    result = CmpAppendValue(result, v_r13, 0, 6);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00C28BBC;
loc_00C28A04:
    goto loc_00C28AC2;
loc_00C28A0F:
    a3 = 0;
    a2 = 0;
    result = CmpAppendLine(result, a2, a3, 6);
    v_rbx = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00C28BBC;
    result = CmpAppendValue(result, 0, 0, 6);
    if ((unsigned __int8)(result) == 0) goto loc_00C28BBC;
    goto loc_00C288CE;
loc_00C28A44:
    result = (unsigned int)((5) - (7));
    if (condition_is_equal) goto loc_00C28B7E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C28A87;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C28A67;
    if (((unsigned int)(result)) != 1) goto loc_00C28861;
loc_00C28A67:
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00C288CE;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C28A04;
    if (((unsigned int)(a1)) != 5) goto loc_00C288BB;
    goto loc_00C28AC2;
loc_00C28A87:
    result = 0;
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_00C28B4C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C28B19;
    if (((unsigned int)(a1)) != 3) goto loc_00C288BB;
loc_00C28AA4:
    result = CmpAppendValue(0, v_stack_m48, v_stack_m40, 6);
    if ((unsigned __int8)(result) == 0) goto loc_00C288BB;
loc_00C28AC2:
loc_00C28AC7:
    if ((unsigned __int8)((unsigned __int8)(a3 + 1)) == 0) goto loc_00C28BCB;
loc_00C28AD0:
    v_rdi = 0;
    *(unsigned int *)(v_stack_p18) = (unsigned int)((unsigned int)(v_stack_p20));
    if (v_stack_m68 == 0) goto loc_00C28AF3;
    result = v_stack_m68;
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_m68;
        result = ExFreePoolWithTag(a1, a2, v_stack_m40, 6);
    }
    if (0 == 0) goto loc_00C28B07;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m40, 6);
    }
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m40, 6);
    goto loc_00C28BD2;
loc_00C28B19:
    v_stack_m40 = (unsigned __int8)(result);
    v_stack_m48 = v_rip + 366160;
    a3 = 0;
    result = CmpAppendValue(0, v_rip + 366160, a3, 6);
    if ((unsigned __int8)(result) != 0) goto loc_00C28A04;
    goto loc_00C28AD0;
loc_00C28B4C:
    v_stack_m40 = 1;
    v_stack_m48 = v_rip + 366109;
    a3 = 0;
    result = CmpAppendValue(0, v_rip + 366109, a3, 6);
    v_rsi = 1;
    if ((unsigned __int8)(result) == 0) { v_rsi = 1; }
    goto loc_00C288D3;
loc_00C28B7E:
    if (((unsigned int)((unsigned int)(v_stack_m50))) == 4) goto loc_00C28AA4;
    if (((unsigned int)((unsigned int)(v_stack_m50))) != 6) goto loc_00C288BB;
    result = 0;
    v_stack_m48 = v_rip + 366038;
    v_stack_m40 = 0;
    a3 = 0;
    result = CmpAppendValue(0, v_rip + 366038, a3, 6);
    if ((unsigned __int8)(result) != 0) goto loc_00C28AC2;
loc_00C28BBC:
    goto loc_00C28AC7;
loc_00C28BCB:
    if (((unsigned int)((unsigned int)(v_stack_m50))) == 1) {
    }
    if (1 == 0) goto loc_00C287BE;
    result = 0;
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 8) = 0;
    }
loc_00C28BF1:
    v_rsp = (v_rsp) + (80);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t CmpParseInfBuffer(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m40 = 0;
    local_rsi = 0;
    v_stack_m50 = v_xmm0;
    result = ExAllocatePool2(256, result + 48, (uint32_t)(0x69704D43ULL), a4);
    if (result == 0) goto loc_00C28BF1;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    *(uint64_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint32_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
    v_stack_m60 = Arg1;
    v_stack_m58 = Arg1 + (uint32_t)(Arg2) * 1;
    v_stack_m68 = 0;
    v_stack_p20 = 1;
loc_00C287BE:
    result = CmpGetToken(v_stack_m60, Arg1 + (uint32_t)(Arg2) * 1, v_stack_m50, a4);
    if (1 > 6) goto loc_00C28A44;
    if (1 == 6) goto loc_00C2894A;
    result = (uint32_t)((1) - (1));
    if (condition_is_equal) goto loc_00C28926;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C288ED;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C288DA;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C28850;
    if (((uint32_t)(result)) != 1) goto loc_00C28861;
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00C288CE;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) - ((uint32_t)(result)));
    if (condition_is_equal) goto loc_00C28AC7;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    if (condition_is_equal) goto loc_00C28845;
    if (((uint32_t)(Arg1)) == 2) goto loc_00C28835;
    goto loc_00C28AD0;
loc_00C28835:
    goto loc_00C28AC7;
loc_00C28845:
    goto loc_00C28AC7;
loc_00C28850:
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00C288A6;
    if (((uint32_t)((uint32_t)(v_stack_m50))) == 1) goto loc_00C2886C;
loc_00C28861:
    goto loc_00C28AD0;
loc_00C2886C:
    result = CmpAppendSection(result, v_stack_m68, (uint8_t)(v_stack_m40), 6);
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_00C2888D;
    goto loc_00C28893;
loc_00C2888D:
loc_00C28893:
    Arg1 = v_stack_m68;
    if ((uint8_t)(result) != 0) { Arg1 = 0; }
    v_stack_m68 = Arg1;
    goto loc_00C28AC7;
loc_00C288A6:
    result = CmpAppendSection(result, v_stack_m68, (uint8_t)(v_stack_m40), 6);
    Arg2 = 0;
    if ((uint8_t)(result) != 0) goto loc_00C288CA;
loc_00C288BB:
    goto loc_00C28AD0;
loc_00C288CA:
    v_stack_m68 = 0;
loc_00C288CE:
loc_00C288D3:
    goto loc_00C28AC7;
loc_00C288DA:
    if (((uint32_t)((uint32_t)(v_stack_m50))) != 3) goto loc_00C288BB;
loc_00C288E2:
    goto loc_00C28AC2;
loc_00C288ED:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) - (3));
    if (condition_is_equal) goto loc_00C28911;
    if (((uint32_t)(Arg1)) != 1) goto loc_00C288BB;
    v_stack_m68 = v_stack_m48;
    goto loc_00C28AC2;
loc_00C28911:
    Arg2 = 0;
    v_stack_m48 = v_rip + 366678;
    v_stack_m40 = 0;
    goto loc_00C288E2;
loc_00C28926:
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00C288CE;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C28AC2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00C288BB;
    goto loc_00C28AC2;
loc_00C2894A:
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00C28A0F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C289D4;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00C289A3;
    if (((uint32_t)(Arg1)) != 1) goto loc_00C288BB;
    Arg3 = 0;
    Arg2 = 0;
    result = CmpAppendLine(result, Arg2, Arg3, 6);
    if ((uint8_t)(result) == 0) goto loc_00C28BBC;
    result = CmpAppendValue(result, v_stack_m48, 0, 6);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_00C28BBC;
    goto loc_00C28AC2;
loc_00C289A3:
    result = CmpAppendLine(result, 0, 0, 6);
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_00C289C3;
    goto loc_00C289C9;
loc_00C289C3:
loc_00C289C9:
    local_r13 = 0;
    if ((uint8_t)(result) != 0) { local_r13 = 0; }
    goto loc_00C28AC7;
loc_00C289D4:
    Arg3 = 0;
    Arg2 = 0;
    result = CmpAppendLine(result, Arg2, Arg3, 6);
    if ((uint8_t)(result) == 0) goto loc_00C28BBC;
    result = CmpAppendValue(result, local_r13, 0, 6);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_00C28BBC;
loc_00C28A04:
    goto loc_00C28AC2;
loc_00C28A0F:
    Arg3 = 0;
    Arg2 = 0;
    result = CmpAppendLine(result, Arg2, Arg3, 6);
    local_rbx = 0;
    if ((uint8_t)(result) == 0) goto loc_00C28BBC;
    result = CmpAppendValue(result, 0, 0, 6);
    if ((uint8_t)(result) == 0) goto loc_00C28BBC;
    goto loc_00C288CE;
loc_00C28A44:
    result = (uint32_t)((5) - (7));
    if (condition_is_equal) goto loc_00C28B7E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C28A87;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C28A67;
    if (((uint32_t)(result)) != 1) goto loc_00C28861;
loc_00C28A67:
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00C288CE;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C28A04;
    if (((uint32_t)(Arg1)) != 5) goto loc_00C288BB;
    goto loc_00C28AC2;
loc_00C28A87:
    result = 0;
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_00C28B4C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) - (1));
    if (condition_is_equal) goto loc_00C28B19;
    if (((uint32_t)(Arg1)) != 3) goto loc_00C288BB;
loc_00C28AA4:
    result = CmpAppendValue(0, v_stack_m48, v_stack_m40, 6);
    if ((uint8_t)(result) == 0) goto loc_00C288BB;
loc_00C28AC2:
loc_00C28AC7:
    if ((uint8_t)((uint8_t)(Arg3 + 1)) == 0) goto loc_00C28BCB;
loc_00C28AD0:
    local_rdi = 0;
    *(uint32_t *)(v_stack_p18) = (uint32_t)((uint32_t)(v_stack_p20));
    if (v_stack_m68 == 0) goto loc_00C28AF3;
    result = v_stack_m68;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m68;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m40, 6);
    }
    if (0 == 0) goto loc_00C28B07;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m40, 6);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m40, 6);
    goto loc_00C28BD2;
loc_00C28B19:
    v_stack_m40 = (uint8_t)(result);
    v_stack_m48 = v_rip + 366160;
    Arg3 = 0;
    result = CmpAppendValue(0, v_rip + 366160, Arg3, 6);
    if ((uint8_t)(result) != 0) goto loc_00C28A04;
    goto loc_00C28AD0;
loc_00C28B4C:
    v_stack_m40 = 1;
    v_stack_m48 = v_rip + 366109;
    Arg3 = 0;
    result = CmpAppendValue(0, v_rip + 366109, Arg3, 6);
    local_rsi = 1;
    if ((uint8_t)(result) == 0) { local_rsi = 1; }
    goto loc_00C288D3;
loc_00C28B7E:
    if (((uint32_t)((uint32_t)(v_stack_m50))) == 4) goto loc_00C28AA4;
    if (((uint32_t)((uint32_t)(v_stack_m50))) != 6) goto loc_00C288BB;
    result = 0;
    v_stack_m48 = v_rip + 366038;
    v_stack_m40 = 0;
    Arg3 = 0;
    result = CmpAppendValue(0, v_rip + 366038, Arg3, 6);
    if ((uint8_t)(result) != 0) goto loc_00C28AC2;
loc_00C28BBC:
    goto loc_00C28AC7;
loc_00C28BCB:
    if (((uint32_t)((uint32_t)(v_stack_m50))) == 1) {
    }
    if (1 == 0) goto loc_00C287BE;
    result = 0;
    if (0 != 0) {
        *(uint64_t *)(0 + 0x8) = 0;
    }
loc_00C28BF1:
    local_rsp = (local_rsp) + (80);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdi*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C28734&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
