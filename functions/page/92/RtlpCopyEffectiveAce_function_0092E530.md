# RtlpCopyEffectiveAce

- RVA: `0x0092E530`–`0x0092EA62` (길이 `1,330` bytes)
- VA: `0x000000014092E530`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008DC8C`
- 디코드: `332`개 명령, `1,330/1,330` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0092E619` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092E667` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0092E7A5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092E7CE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092E90B` → [RtlEqualPrefixSid](RtlEqualPrefixSid_function_0092EBF4.md) (function, `0x0092EBF4`)
- `0x0092E938` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092E9B8` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x0092E9CB` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x0092EA1F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092EA4A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [RtlpGenerateInheritedAce](RtlpGenerateInheritedAce_function_0092DB80.md) at `0x0092DCF6`
- [sub_0092E268](Unknown_function_0092E268.md) at `0x0092E31E`

### Static image references
- `0x0092E54C` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0092E619` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092E667` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0092E7A5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092E7CE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092E938` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092E9B8` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x0092E9CB` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x0092EA1F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092EA4A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0092E8C6` → [sub_00B22F88 + 0x28A](../B2/Unknown_function_00B22F88.md) (`tail-transfer`)
  - `0x0092E993` → [sub_00B22F88](../B2/Unknown_function_00B22F88.md) (`tail-transfer`)
  - `0x0092E99C` → [sub_00B22F88](../B2/Unknown_function_00B22F88.md) (`tail-transfer`)
  - `0x0092EA0D` → [sub_00B22F88 + 0x384](../B2/Unknown_function_00B22F88.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0092E530  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0092E535  55                              push rbp
0092E536  56                              push rsi
0092E537  57                              push rdi
0092E538  41 54                           push r12
0092E53A  41 55                           push r13
0092E53C  41 56                           push r14
0092E53E  41 57                           push r15
0092E540  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
0092E545  48 81 EC 10 01 00 00            sub rsp, 0x110
0092E54C  48 8B 05 ED C1 4D 00            mov rax, qword ptr [rip + 0x4dc1ed]
0092E553  48 33 C4                        xor rax, rsp
0092E556  48 89 45 00                     mov qword ptr [rbp], rax
0092E55A  4C 8B 65 78                     mov r12, qword ptr [rbp + 0x78]
0092E55E  4D 8B D1                        mov r10, r9
0092E561  4C 8B AD 80 00 00 00            mov r13, qword ptr [rbp + 0x80]
0092E568  48 8B F9                        mov rdi, rcx
0092E56B  4C 8B 5D 70                     mov r11, qword ptr [rbp + 0x70]
0092E56F  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
0092E576  4C 8B B5 A0 00 00 00            mov r14, qword ptr [rbp + 0xa0]
0092E57D  48 8B B5 B0 00 00 00            mov rsi, qword ptr [rbp + 0xb0]
0092E584  4C 8B BD C8 00 00 00            mov r15, qword ptr [rbp + 0xc8]
0092E58B  44 88 44 24 21                  mov byte ptr [rsp + 0x21], r8b
0092E590  45 33 C0                        xor r8d, r8d
0092E593  4D 85 E4                        test r12, r12
0092E596  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
0092E59A  4C 8B 8D C0 00 00 00            mov r9, qword ptr [rbp + 0xc0]
0092E5A1  4D 0F 44 E2                     cmove r12, r10
0092E5A5  88 54 24 60                     mov byte ptr [rsp + 0x60], dl
0092E5A9  48 8B 95 B8 00 00 00            mov rdx, qword ptr [rbp + 0xb8]
0092E5B0  4D 85 ED                        test r13, r13
0092E5B3  4C 89 5D 90                     mov qword ptr [rbp - 0x70], r11
0092E5B7  4D 0F 44 EB                     cmove r13, r11
0092E5BB  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0092E5BF  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
0092E5C4  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0092E5C9  C7 45 B0 01 01 00 00            mov dword ptr [rbp - 0x50], 0x101
0092E5D0  48 C7 45 B4 00 00 00 03         mov qword ptr [rbp - 0x4c], 0x3000000
0092E5D8  45 88 01                        mov byte ptr [r9], r8b
0092E5DB  48 85 D2                        test rdx, rdx
0092E5DE  74 03                           je 0x14092e5e3
0092E5E0  44 88 02                        mov byte ptr [rdx], r8b
0092E5E3  45 88 07                        mov byte ptr [r15], r8b
0092E5E6  0F B7 59 02                     movzx ebx, word ptr [rcx + 2]
0092E5EA  0F B6 09                        movzx ecx, byte ptr [rcx]
0092E5ED  8D 41 F5                        lea eax, [rcx - 0xb]
0092E5F0  3C 01                           cmp al, 1
0092E5F2  76 09                           jbe 0x14092e5fd
0092E5F4  80 F9 0F                        cmp cl, 0xf
0092E5F7  0F 82 8B 00 00 00               jb 0x14092e688
0092E5FD  49 8B 0E                        mov rcx, qword ptr [r14]
0092E600  4C 8B C3                        mov r8, rbx
0092E603  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0092E607  48 2B C1                        sub rax, rcx
0092E60A  48 03 C6                        add rax, rsi
0092E60D  48 3B D8                        cmp rbx, rax
0092E610  0F 8F E5 02 00 00               jg 0x14092e8fb
0092E616  48 8B D7                        mov rdx, rdi
0092E619  E8 22 82 D9 FF                  call 0x1406c6840
0092E61E  41 80 3F 00                     cmp byte ptr [r15], 0
0092E622  75 1D                           jne 0x14092e641
0092E624  85 DB                           test ebx, ebx
0092E626  74 19                           je 0x14092e641
0092E628  49 8B 06                        mov rax, qword ptr [r14]
0092E62B  80 60 01 E0                     and byte ptr [rax + 1], 0xe0
0092E62F  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
0092E634  74 07                           je 0x14092e63d
0092E636  49 8B 06                        mov rax, qword ptr [r14]
0092E639  80 48 01 10                     or byte ptr [rax + 1], 0x10
0092E63D  66 FF 46 04                     inc word ptr [rsi + 4]
0092E641  81 FB FF FF 00 00               cmp ebx, 0xffff
0092E647  0F 87 C2 01 00 00               ja 0x14092e80f
0092E64D  41 80 3F 00                     cmp byte ptr [r15], 0
0092E651  75 05                           jne 0x14092e658
0092E653  8B C3                           mov eax, ebx
0092E655  49 01 06                        add qword ptr [r14], rax
0092E658  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0092E65C  89 18                           mov dword ptr [rax], ebx
0092E65E  B0 01                           mov al, 1
0092E660  48 8B 4D 00                     mov rcx, qword ptr [rbp]
0092E664  48 33 CC                        xor rcx, rsp
0092E667  E8 D4 DF D7 FF                  call 0x1406ac640
0092E66C  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
0092E674  48 81 C4 10 01 00 00            add rsp, 0x110
0092E67B  41 5F                           pop r15
0092E67D  41 5E                           pop r14
0092E67F  41 5D                           pop r13
0092E681  41 5C                           pop r12
0092E683  5F                              pop rdi
0092E684  5E                              pop rsi
0092E685  5D                              pop rbp
0092E686  C3                              ret
0092E687  CC                              int3
0092E688  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
0092E68D  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
0092E692  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0092E697  80 F9 03                        cmp cl, 3
0092E69A  0F 87 ED 02 00 00               ja 0x14092e98d
0092E6A0  4C 8D 57 08                     lea r10, [rdi + 8]
0092E6A4  C7 44 24 28 08 00 00 00         mov dword ptr [rsp + 0x28], 8
0092E6AC  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
0092E6B1  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0092E6B6  85 DB                           test ebx, ebx
0092E6B8  0F 84 60 FF FF FF               je 0x14092e61e
0092E6BE  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
0092E6C1  48 8B 95 88 00 00 00            mov rdx, qword ptr [rbp + 0x88]
0092E6C8  85 C9                           test ecx, ecx
0092E6CA  79 02                           jns 0x14092e6ce
0092E6CC  0B 0A                           or ecx, dword ptr [rdx]
0092E6CE  0F BA E1 1E                     bt ecx, 0x1e
0092E6D2  73 03                           jae 0x14092e6d7
0092E6D4  0B 4A 04                        or ecx, dword ptr [rdx + 4]
0092E6D7  0F BA E1 1D                     bt ecx, 0x1d
0092E6DB  73 03                           jae 0x14092e6e0
0092E6DD  0B 4A 08                        or ecx, dword ptr [rdx + 8]
0092E6E0  0F BA E1 1C                     bt ecx, 0x1c
0092E6E4  73 03                           jae 0x14092e6e9
0092E6E6  0B 4A 0C                        or ecx, dword ptr [rdx + 0xc]
0092E6E9  0F B6 07                        movzx eax, byte ptr [rdi]
0092E6EC  3C 0A                           cmp al, 0xa
0092E6EE  0F 87 51 02 00 00               ja 0x14092e945
0092E6F4  41 B8 73 06 00 00               mov r8d, 0x673
0092E6FA  41 0F A3 C0                     bt r8d, eax
0092E6FE  0F 83 41 02 00 00               jae 0x14092e945
0092E704  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
0092E707  23 C1                           and eax, ecx
0092E709  25 FF FF FF 0F                  and eax, 0xfffffff
0092E70E  3B 47 04                        cmp eax, dword ptr [rdi + 4]
0092E711  74 04                           je 0x14092e717
0092E713  41 C6 01 01                     mov byte ptr [r9], 1
0092E717  25 FF FF 1F 01                  and eax, 0x11fffff
0092E71C  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
0092E720  0F 84 DE 01 00 00               je 0x14092e904
0092E726  41 80 3A 01                     cmp byte ptr [r10], 1
0092E72A  75 2E                           jne 0x14092e75a
0092E72C  41 80 7A 02 00                  cmp byte ptr [r10 + 2], 0
0092E731  75 27                           jne 0x14092e75a
0092E733  41 80 7A 03 00                  cmp byte ptr [r10 + 3], 0
0092E738  75 20                           jne 0x14092e75a
0092E73A  41 80 7A 04 00                  cmp byte ptr [r10 + 4], 0
0092E73F  75 19                           jne 0x14092e75a
0092E741  41 80 7A 05 00                  cmp byte ptr [r10 + 5], 0
0092E746  75 12                           jne 0x14092e75a
0092E748  41 80 7A 06 00                  cmp byte ptr [r10 + 6], 0
0092E74D  75 0B                           jne 0x14092e75a
0092E74F  41 80 7A 07 03                  cmp byte ptr [r10 + 7], 3
0092E754  0F 84 BC 00 00 00               je 0x14092e816
0092E75A  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
0092E75F  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
0092E764  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0092E769  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
0092E76E  84 D2                           test dl, dl
0092E770  0F 85 82 02 00 00               jne 0x14092e9f8
0092E776  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0092E77B  4D 8B 26                        mov r12, qword ptr [r14]
0092E77E  4D 85 E4                        test r12, r12
0092E781  0F 84 74 01 00 00               je 0x14092e8fb
0092E787  0F B7 4E 02                     movzx ecx, word ptr [rsi + 2]
0092E78B  49 2B CC                        sub rcx, r12
0092E78E  8B C3                           mov eax, ebx
0092E790  48 03 CE                        add rcx, rsi
0092E793  48 3B C1                        cmp rax, rcx
0092E796  0F 8F 5F 01 00 00               jg 0x14092e8fb
0092E79C  41 8B F8                        mov edi, r8d
0092E79F  49 8B CC                        mov rcx, r12
0092E7A2  45 8B C0                        mov r8d, r8d
0092E7A5  E8 96 80 D9 FF                  call 0x1406c6840
0092E7AA  49 03 FC                        add rdi, r12
0092E7AD  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
0092E7B2  4D 85 E4                        test r12, r12
0092E7B5  0F 85 7B 02 00 00               jne 0x14092ea36
0092E7BB  45 0F B6 45 01                  movzx r8d, byte ptr [r13 + 1]
0092E7C0  49 8B D5                        mov rdx, r13
0092E7C3  48 8B CF                        mov rcx, rdi
0092E7C6  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092E7CE  E8 6D 80 D9 FF                  call 0x1406c6840
0092E7D3  41 0F B6 45 01                  movzx eax, byte ptr [r13 + 1]
0092E7D8  48 83 C0 02                     add rax, 2
0092E7DC  4C 8D 24 87                     lea r12, [rdi + rax*4]
0092E7E0  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0092E7E5  48 85 C0                        test rax, rax
0092E7E8  0F 85 31 01 00 00               jne 0x14092e91f
0092E7EE  45 2B 26                        sub r12d, dword ptr [r14]
0092E7F1  41 3B DC                        cmp ebx, r12d
0092E7F4  72 19                           jb 0x14092e80f
0092E7F6  49 8B 06                        mov rax, qword ptr [r14]
0092E7F9  41 8B DC                        mov ebx, r12d
0092E7FC  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
0092E800  66 89 58 02                     mov word ptr [rax + 2], bx
0092E804  49 8B 06                        mov rax, qword ptr [r14]
0092E807  89 48 04                        mov dword ptr [rax + 4], ecx
0092E80A  E9 0F FE FF FF                  jmp 0x14092e61e
0092E80F  32 C0                           xor al, al
0092E811  E9 4A FE FF FF                  jmp 0x14092e660
0092E816  41 80 7A 01 01                  cmp byte ptr [r10 + 1], 1
0092E81B  0F 85 39 FF FF FF               jne 0x14092e75a
0092E821  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
0092E826  48 8D 45 B8                     lea rax, [rbp - 0x48]
0092E82A  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0092E82F  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0092E833  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
0092E838  33 C9                           xor ecx, ecx
0092E83A  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0092E83E  49 8B C2                        mov rax, r10
0092E841  48 2B C2                        sub rax, rdx
0092E844  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0092E849  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
0092E84E  48 83 C0 08                     add rax, 8
0092E852  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
0092E857  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0092E85B  0F B6 44 24 20                  movzx eax, byte ptr [rsp + 0x20]
0092E860  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0092E864  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
0092E869  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0092E86D  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0092E872  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0092E877  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
0092E87C  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0092E881  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0092E886  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0092E88B  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0092E890  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
0092E894  4D 8B C2                        mov r8, r10
0092E897  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
0092E89B  0F B6 D0                        movzx edx, al
0092E89E  88 44 24 21                     mov byte ptr [rsp + 0x21], al
0092E8A2  3B 4C 24 78                     cmp ecx, dword ptr [rsp + 0x78]
0092E8A6  0F 8C A5 00 00 00               jl 0x14092e951
0092E8AC  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
0092E8B0  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0092E8B5  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0092E8BA  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
0092E8BF  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0092E8C4  85 C0                           test eax, eax
0092E8C6  0F 85 46 49 1F 00               jne 0x140b23212
0092E8CC  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0092E8D0  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0092E8D5  4C 8B E8                        mov r13, rax
0092E8D8  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
0092E8DC  8D 0C 85 FC FF FF FF            lea ecx, [rax*4 - 4]
0092E8E3  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0092E8E8  03 D9                           add ebx, ecx
0092E8EA  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0092E8EE  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0092E8F3  C6 00 01                        mov byte ptr [rax], 1
0092E8F6  E9 73 FE FF FF                  jmp 0x14092e76e
0092E8FB  41 C6 07 01                     mov byte ptr [r15], 1
0092E8FF  E9 3D FD FF FF                  jmp 0x14092e641
0092E904  48 8D 55 B0                     lea rdx, [rbp - 0x50]
0092E908  49 8B CA                        mov rcx, r10
0092E90B  E8 E4 02 00 00                  call 0x14092ebf4
0092E910  84 C0                           test al, al
0092E912  0F 85 D6 00 00 00               jne 0x14092e9ee
0092E918  33 DB                           xor ebx, ebx
0092E91A  E9 FF FC FF FF                  jmp 0x14092e61e
0092E91F  48 63 4C 24 38                  movsxd rcx, dword ptr [rsp + 0x38]
0092E924  85 C9                           test ecx, ecx
0092E926  0F 8E C2 FE FF FF               jle 0x14092e7ee
0092E92C  48 8B F9                        mov rdi, rcx
0092E92F  4C 8B C1                        mov r8, rcx
0092E932  49 8B CC                        mov rcx, r12
0092E935  48 8B D0                        mov rdx, rax
0092E938  E8 03 7F D9 FF                  call 0x1406c6840
0092E93D  4C 03 E7                        add r12, rdi
0092E940  E9 A9 FE FF FF                  jmp 0x14092e7ee
0092E945  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
0092E948  0F BA E8 18                     bts eax, 0x18
0092E94C  E9 B6 FD FF FF                  jmp 0x14092e707
0092E951  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0092E955  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
0092E959  8B 02                           mov eax, dword ptr [rdx]
0092E95B  41 39 04 10                     cmp dword ptr [r8 + rdx], eax
0092E95F  0F 85 F5 FD FF FF               jne 0x14092e75a
0092E965  0F B6 44 24 20                  movzx eax, byte ptr [rsp + 0x20]
0092E96A  FF C1                           inc ecx
0092E96C  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0092E971  48 83 C2 04                     add rdx, 4
0092E975  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
0092E97A  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
0092E97F  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0092E983  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
0092E988  E9 F4 FE FF FF                  jmp 0x14092e881
0092E98D  44 8B DF                        mov r11d, edi
0092E990  80 F9 09                        cmp cl, 9
0092E993  0F 82 EF 45 1F 00               jb 0x140b22f88
0092E999  80 F9 0A                        cmp cl, 0xa
0092E99C  0F 87 E6 45 1F 00               ja 0x140b22f88
0092E9A2  48 8D 47 08                     lea rax, [rdi + 8]
0092E9A6  B9 08 00 00 00                  mov ecx, 8
0092E9AB  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0092E9B0  48 8B C8                        mov rcx, rax
0092E9B3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092E9B8  E8 B3 E8 B2 FF                  call 0x14045d270
0092E9BD  8B C0                           mov eax, eax
0092E9BF  48 8D 4F 08                     lea rcx, [rdi + 8]
0092E9C3  48 03 C1                        add rax, rcx
0092E9C6  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0092E9CB  E8 A0 E8 B2 FF                  call 0x14045d270
0092E9D0  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0092E9D5  4C 8D 57 08                     lea r10, [rdi + 8]
0092E9D9  8B CB                           mov ecx, ebx
0092E9DB  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0092E9E0  2B C8                           sub ecx, eax
0092E9E2  83 E9 08                        sub ecx, 8
0092E9E5  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0092E9E9  E9 C8 FC FF FF                  jmp 0x14092e6b6
0092E9EE  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0092E9F3  E9 2E FD FF FF                  jmp 0x14092e726
0092E9F8  80 38 00                        cmp byte ptr [rax], 0
0092E9FB  0F 84 75 FD FF FF               je 0x14092e776
0092EA01  8B 47 08                        mov eax, dword ptr [rdi + 8]
0092EA04  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0092EA08  48 8B D7                        mov rdx, rdi
0092EA0B  A8 01                           test al, 1
0092EA0D  0F 84 F9 48 1F 00               je 0x140b2330c
0092EA13  41 83 C0 F0                     add r8d, -0x10
0092EA17  83 C3 F0                        add ebx, -0x10
0092EA1A  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0092EA1F  E8 1C 7E D9 FF                  call 0x1406c6840
0092EA24  83 65 E8 FD                     and dword ptr [rbp - 0x18], 0xfffffffd
0092EA28  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0092EA2C  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
0092EA31  E9 45 FD FF FF                  jmp 0x14092e77b
0092EA36  45 0F B6 44 24 01               movzx r8d, byte ptr [r12 + 1]
0092EA3C  49 8B D4                        mov rdx, r12
0092EA3F  48 8B CF                        mov rcx, rdi
0092EA42  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092EA4A  E8 F1 7D D9 FF                  call 0x1406c6840
0092EA4F  41 0F B6 44 24 01               movzx eax, byte ptr [r12 + 1]
0092EA55  48 8D 3C 87                     lea rdi, [rdi + rax*4]
0092EA59  48 83 C7 08                     add rdi, 8
0092EA5D  E9 59 FD FF FF                  jmp 0x14092e7bb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCopyEffectiveAce(__int64 a1, unsigned __int8 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int8 v_stack_m127;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned int v_stack_p7C;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 5095917)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m127 = (unsigned __int8)(a3);
    a3 = 0;
    v_stack_mB0 = a4;
    if (a6 == 0) { a6 = a4; }
    v_stack_mE8 = a2;
    v_stack_mB8 = a5;
    if (a7 == 0) { a7 = a5; }
    v_stack_mA0 = a12;
    v_stack_m118 = a15;
    v_stack_m128 = 0;
    v_stack_m98 = 257;
    v_stack_m94 = 0x3000000ULL;
    *(unsigned __int8 *)(a15) = 0;
    if (a14 != 0) {
        *(unsigned __int8 *)(a14) = 0;
    }
    *(unsigned __int8 *)(a16) = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1) - 11)) <= 1) goto loc_0092E5FD;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) < 15) goto loc_0092E688;
loc_0092E5FD:
    result = (*(unsigned __int16 *)(a13 + 2)) - (*(unsigned __int64 *)(a11));
    result = (result) + (a13);
    if ((*(unsigned __int16 *)(a1 + 2)) > result) goto loc_0092E8FB;
    result = memcpy(*(unsigned __int64 *)(a11), a1, *(unsigned __int16 *)(a1 + 2), a15);
loc_0092E61E:
    if ((*(unsigned __int8 *)(a16)) != 0) goto loc_0092E641;
    if ((unsigned int)(*(unsigned __int16 *)(a1 + 2)) == 0) goto loc_0092E641;
    result = *(unsigned __int64 *)(a11);
    if (v_stack_mE8 != 0) {
        result = *(unsigned __int64 *)(a11);
    }
loc_0092E641:
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 2))) > 0xFFFFULL) goto loc_0092E80F;
    if ((*(unsigned __int8 *)(a16)) == 0) {
        result = (unsigned int)(*(unsigned __int16 *)(a1 + 2));
    }
    *(unsigned int *)(v_stack_mA0) = (unsigned int)(*(unsigned __int16 *)(a1 + 2));
loc_0092E660:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a1, *(unsigned __int16 *)(a1 + 2), a15);
    v_rsp = (v_rsp) + (272);
    return result;
loc_0092E688:
    v_stack_p48 = *(unsigned __int16 *)(a1 + 2);
    v_stack_p68 = *(unsigned __int16 *)(a1 + 2);
    v_stack_p38 = (unsigned int)(*(unsigned __int16 *)(a1 + 2));
    if (((unsigned __int8)(a1)) > 3) goto loc_0092E98D;
    v_stack_p28 = 8;
    v_stack_p40 = a1 + 8;
    v_stack_p58 = a1;
loc_0092E6B6:
    if ((unsigned int)(v_stack_p10) == 0) goto loc_0092E61E;
    if (sign_flag) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) | (*(unsigned int *)(a8)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(a8 + 4)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(a8 + 8)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(a8 + 12)));
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) > 10) goto loc_0092E945;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) >= 10) goto loc_0092E945;
loc_0092E707:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a8 + 12))) & ((unsigned int)(a1)));
    result = (unsigned int)((result) & (0xFFFFFFFULL));
    if (((unsigned int)(result)) != (*(unsigned int *)(a1 + 4))) {
        *(unsigned __int8 *)(a15) = 1;
    }
    result = (unsigned int)((result) & (0x11FFFFFULL));
    v_stack_p7C = (unsigned int)(result);
    if (condition_is_equal) goto loc_0092E904;
loc_0092E726:
    if ((*(unsigned __int8 *)(a1 + 8)) != 1) goto loc_0092E75A;
    if ((*(unsigned __int8 *)(a1 + 8 + 2)) != 0) goto loc_0092E75A;
    if ((*(unsigned __int8 *)(a1 + 8 + 3)) != 0) goto loc_0092E75A;
    if ((*(unsigned __int8 *)(a1 + 8 + 4)) != 0) goto loc_0092E75A;
    if ((*(unsigned __int8 *)(a1 + 8 + 5)) != 0) goto loc_0092E75A;
    if ((*(unsigned __int8 *)(a1 + 8 + 6)) != 0) goto loc_0092E75A;
    if ((*(unsigned __int8 *)(a1 + 8 + 7)) == 3) goto loc_0092E816;
loc_0092E75A:
loc_0092E76E:
    if ((unsigned __int8)(v_stack_p20) != 0) goto loc_0092E9F8;
loc_0092E776:
loc_0092E77B:
    if (*(unsigned __int64 *)(a11) == 0) goto loc_0092E8FB;
    a1 = (*(unsigned __int16 *)(a13 + 2)) - (*(unsigned __int64 *)(a11));
    a1 = (a1) + (a13);
    if (((unsigned int)((unsigned int)(v_stack_p10))) > a1) goto loc_0092E8FB;
    result = memcpy(*(unsigned __int64 *)(a11), v_stack_p58, (unsigned int)((unsigned int)(v_stack_p28)), a15);
    v_rdi = ((unsigned int)((unsigned int)(v_stack_p28))) + (*(unsigned __int64 *)(a11));
    if (v_stack_p48 != 0) goto loc_0092EA36;
loc_0092E7BB:
    result = memcpy(v_rdi, v_stack_p40, *(unsigned __int8 *)(v_stack_p40 + 1) * 4 + 8, a15);
    result = (*(unsigned __int8 *)(v_stack_p40 + 1)) + (2);
    if (v_stack_p68 != 0) goto loc_0092E91F;
loc_0092E7EE:
    v_r12 = (unsigned int)((v_rdi + result * 4) - (*(unsigned int *)(a11)));
    if (((unsigned int)(v_stack_p10)) < ((unsigned int)(v_r12))) goto loc_0092E80F;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a11) + 2) = (unsigned __int16)((unsigned int)((unsigned int)(v_r12)));
    *(unsigned int *)(*(unsigned __int64 *)(a11) + 4) = (unsigned int)((unsigned int)(v_stack_p7C));
    goto loc_0092E61E;
loc_0092E80F:
    result = 0;
    goto loc_0092E660;
loc_0092E816:
    if ((*(unsigned __int8 *)(a1 + 8 + 1)) != 1) goto loc_0092E75A;
    a1 = 0;
    v_stack_mC0 = v_stack_m90;
    result = (a1 + 8) - (v_stack_m90);
    v_stack_p48 = v_stack_p48;
    result = (result) + (8);
    v_stack_mA8 = result;
    v_stack_p20 = (unsigned __int8)(v_stack_p20);
    v_stack_p40 = a1 + 8;
    v_stack_p78 = 0;
    v_stack_p28 = v_stack_p28;
    v_stack_p58 = v_stack_p58;
    v_stack_p68 = v_stack_p68;
    v_stack_p38 = (unsigned int)((unsigned int)(v_stack_p38));
loc_0092E881:
    v_stack_p70 = v_stack_p48;
    v_stack_mC8 = v_stack_p58;
    v_stack_p50 = (unsigned int)(v_stack_p28);
    v_stack_p21 = (unsigned __int8)(v_stack_p20);
    if (0 < v_stack_p78) goto loc_0092E951;
    v_stack_p48 = v_stack_p70;
    v_stack_p68 = v_stack_p68;
    v_stack_p38 = (unsigned int)((unsigned int)(v_stack_p38));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)(*(unsigned __int8 *)(v_stack_mB0 + 1) * 4 - 4)));
    v_stack_p58 = v_stack_mC8;
    *(unsigned __int8 *)(v_stack_p30) = 1;
    goto loc_0092E76E;
loc_0092E8FB:
    *(unsigned __int8 *)(a16) = 1;
    goto loc_0092E641;
loc_0092E904:
    result = RtlEqualPrefixSid(v_stack_p70, v_stack_m98, (unsigned int)(v_stack_p50), (unsigned int)(v_stack_p38));
    if ((unsigned __int8)(result) != 0) goto loc_0092E9EE;
    v_rbx = 0;
    goto loc_0092E61E;
loc_0092E91F:
    if (condition_is_less_or_equal) goto loc_0092E7EE;
    result = memcpy(v_r12, result, (int)(v_stack_p38), (unsigned int)(v_stack_p38));
    v_r12 = (v_r12) + ((int)(v_stack_p38));
    goto loc_0092E7EE;
loc_0092E945:
    goto loc_0092E707;
loc_0092E951:
    if ((*(unsigned int *)(v_stack_mA8 + v_stack_mC0 * 1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC0))))) goto loc_0092E75A;
    a1 = (unsigned int)((v_r12) + 1);
    a2 = (v_stack_mC0) + (4);
    v_stack_mC0 = a2;
    goto loc_0092E881;
loc_0092E98D:
    v_stack_p28 = 8;
    v_stack_p40 = (int)(v_stack_p38) + 8;
    result = RtlLengthSid((int)(v_stack_p38) + 8, v_stack_p28, v_stack_p58, (unsigned int)(v_stack_p38));
    result = ((unsigned int)((unsigned int)(result))) + ((int)(v_stack_p38) + 8);
    v_stack_p68 = result;
    result = RtlLengthSid((int)(v_stack_p38) + 8, v_stack_p28, v_stack_p58, (unsigned int)(v_stack_p38));
    v_stack_p58 = (int)(v_stack_p38);
    a1 = (unsigned int)((0) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) - (8));
    v_stack_p38 = (unsigned int)(a1);
    goto loc_0092E6B6;
loc_0092E9EE:
    goto loc_0092E726;
loc_0092E9F8:
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_0092E776;
    a3 = (unsigned int)((v_stack_p58) + (-16));
    v_rbx = (unsigned int)((v_rbx) + (-16));
    v_stack_p28 = a3;
    result = memcpy(v_stack_m68, (int)(v_stack_p38), a3, v_stack_p30);
    goto loc_0092E77B;
loc_0092EA36:
    result = memcpy((int)(v_stack_p38), v_r12, *(unsigned __int8 *)(v_r12 + 1) * 4 + 8, v_stack_p30);
    v_rdi = ((int)(v_stack_p38) + *(unsigned __int8 *)(v_r12 + 1) * 4) + (8);
    goto loc_0092E7BB;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCopyEffectiveAce(void *Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, void *Arg8, uint64_t Arg9, uint64_t Arg10, void *Arg11, int64_t Arg12, void *Arg13, int64_t Arg14, void *Arg15, void *Arg16)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg11 = (uint8_t *)Arg11;
    uint8_t *arg13 = (uint8_t *)Arg13;
    uint8_t *arg15 = (uint8_t *)Arg15;
    uint8_t *arg16 = (uint8_t *)Arg16;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint8_t v_stack_m127;
    uint8_t v_stack_m128;
    uint64_t v_stack_m48;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m90;
    uint64_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p21;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint32_t v_stack_p7C;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x4DC1ED)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m127 = (uint8_t)(Arg3);
    Arg3 = 0;
    v_stack_mB0 = Arg4;
    if (Arg6 == 0) { Arg6 = Arg4; }
    v_stack_mE8 = Arg2;
    v_stack_mB8 = Arg5;
    if (Arg7 == 0) { Arg7 = Arg5; }
    v_stack_mA0 = Arg12;
    v_stack_m118 = Arg15;
    v_stack_m128 = 0;
    v_stack_m98 = 257;
    v_stack_m94 = 0x3000000ULL;
    *(uint8_t *)(arg15) = 0;
    if (Arg14 != 0) {
        *(uint8_t *)(Arg14) = 0;
    }
    *(uint8_t *)(arg16) = 0;
    if (((uint8_t)(*(uint8_t *)(arg1) - 11)) <= 1) goto loc_0092E5FD;
    if (((uint8_t)(*(uint8_t *)(arg1))) < 15) goto loc_0092E688;
loc_0092E5FD:
    result = (*(uint16_t *)(arg13 + 0x2)) - (*(uint64_t *)(arg11));
    result = (result) + (Arg13);
    if ((*(uint16_t *)(arg1 + 0x2)) > result) goto loc_0092E8FB;
    result = memcpy(*(uint64_t *)(arg11), Arg1, *(uint16_t *)(arg1 + 0x2), Arg15);
loc_0092E61E:
    if ((*(uint8_t *)(arg16)) != 0) goto loc_0092E641;
    if ((uint32_t)(*(uint16_t *)(arg1 + 0x2)) == 0) goto loc_0092E641;
    result = *(uint64_t *)(arg11);
    if (v_stack_mE8 != 0) {
        result = *(uint64_t *)(arg11);
    }
loc_0092E641:
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2))) > 0xFFFFULL) goto loc_0092E80F;
    if ((*(uint8_t *)(arg16)) == 0) {
        result = (uint32_t)(*(uint16_t *)(arg1 + 0x2));
    }
    *(uint32_t *)(v_stack_mA0) = (uint32_t)(*(uint16_t *)(arg1 + 0x2));
loc_0092E660:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1, *(uint16_t *)(arg1 + 0x2), Arg15);
    local_rsp = (local_rsp) + (272);
    return result;
loc_0092E688:
    v_stack_p48 = *(uint16_t *)(arg1 + 0x2);
    v_stack_p68 = *(uint16_t *)(arg1 + 0x2);
    v_stack_p38 = (uint32_t)(*(uint16_t *)(arg1 + 0x2));
    if (((uint8_t)(Arg1)) > 3) goto loc_0092E98D;
    v_stack_p28 = 8;
    v_stack_p40 = Arg1 + 8;
    v_stack_p58 = Arg1;
loc_0092E6B6:
    if ((uint32_t)(v_stack_p10) == 0) goto loc_0092E61E;
    if (sign_flag) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) | (*(uint32_t *)(arg8)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(arg8 + 0x4)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(arg8 + 0x8)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(arg8 + 0xC)));
    }
    if (((uint8_t)(*(uint8_t *)(arg1))) > 10) goto loc_0092E945;
    if (((uint8_t)(*(uint8_t *)(arg1))) >= 10) goto loc_0092E945;
loc_0092E707:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg8 + 0xC))) & ((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (0xFFFFFFFULL));
    if (((uint32_t)(result)) != (*(uint32_t *)(arg1 + 0x4))) {
        *(uint8_t *)(arg15) = 1;
    }
    result = (uint32_t)((result) & (0x11FFFFFULL));
    v_stack_p7C = (uint32_t)(result);
    if (condition_is_equal) goto loc_0092E904;
loc_0092E726:
    if ((*(uint8_t *)(arg1 + 0x8)) != 1) goto loc_0092E75A;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x2)) != 0) goto loc_0092E75A;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x3)) != 0) goto loc_0092E75A;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x4)) != 0) goto loc_0092E75A;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x5)) != 0) goto loc_0092E75A;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x6)) != 0) goto loc_0092E75A;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x7)) == 3) goto loc_0092E816;
loc_0092E75A:
loc_0092E76E:
    if ((uint8_t)(v_stack_p20) != 0) goto loc_0092E9F8;
loc_0092E776:
loc_0092E77B:
    if (*(uint64_t *)(arg11) == 0) goto loc_0092E8FB;
    Arg1 = (*(uint16_t *)(arg13 + 0x2)) - (*(uint64_t *)(arg11));
    Arg1 = (Arg1) + (Arg13);
    if (((uint32_t)((uint32_t)(v_stack_p10))) > Arg1) goto loc_0092E8FB;
    result = memcpy(*(uint64_t *)(arg11), v_stack_p58, (uint32_t)((uint32_t)(v_stack_p28)), Arg15);
    local_rdi = ((uint32_t)((uint32_t)(v_stack_p28))) + (*(uint64_t *)(arg11));
    if (v_stack_p48 != 0) goto loc_0092EA36;
loc_0092E7BB:
    result = memcpy(local_rdi, v_stack_p40, *(uint8_t *)(v_stack_p40 + 0x1) * 4 + 8, Arg15);
    result = (*(uint8_t *)(v_stack_p40 + 0x1)) + (2);
    if (v_stack_p68 != 0) goto loc_0092E91F;
loc_0092E7EE:
    local_r12 = (uint32_t)((local_rdi + result * 4) - (*(uint32_t *)(arg11)));
    if (((uint32_t)(v_stack_p10)) < ((uint32_t)(local_r12))) goto loc_0092E80F;
    *(uint16_t *)(*(uint64_t *)(arg11) + 0x2) = (uint16_t)((uint32_t)((uint32_t)(local_r12)));
    *(uint32_t *)(*(uint64_t *)(arg11) + 0x4) = (uint32_t)((uint32_t)(v_stack_p7C));
    goto loc_0092E61E;
loc_0092E80F:
    result = 0;
    goto loc_0092E660;
loc_0092E816:
    if ((*(uint8_t *)(arg1 + 0x8 + 0x1)) != 1) goto loc_0092E75A;
    Arg1 = 0;
    v_stack_mC0 = v_stack_m90;
    result = (Arg1 + 8) - (v_stack_m90);
    v_stack_p48 = v_stack_p48;
    result = (result) + (8);
    v_stack_mA8 = result;
    v_stack_p20 = (uint8_t)(v_stack_p20);
    v_stack_p40 = Arg1 + 8;
    v_stack_p78 = 0;
    v_stack_p28 = v_stack_p28;
    v_stack_p58 = v_stack_p58;
    v_stack_p68 = v_stack_p68;
    v_stack_p38 = (uint32_t)((uint32_t)(v_stack_p38));
loc_0092E881:
    v_stack_p70 = v_stack_p48;
    v_stack_mC8 = v_stack_p58;
    v_stack_p50 = (uint32_t)(v_stack_p28);
    v_stack_p21 = (uint8_t)(v_stack_p20);
    if (0 < v_stack_p78) goto loc_0092E951;
    v_stack_p48 = v_stack_p70;
    v_stack_p68 = v_stack_p68;
    v_stack_p38 = (uint32_t)((uint32_t)(v_stack_p38));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)(*(uint8_t *)(v_stack_mB0 + 0x1) * 4 - 4)));
    v_stack_p58 = v_stack_mC8;
    *(uint8_t *)(v_stack_p30) = 1;
    goto loc_0092E76E;
loc_0092E8FB:
    *(uint8_t *)(arg16) = 1;
    goto loc_0092E641;
loc_0092E904:
    result = RtlEqualPrefixSid(v_stack_p70, v_stack_m98, (uint32_t)(v_stack_p50), (uint32_t)(v_stack_p38));
    if ((uint8_t)(result) != 0) goto loc_0092E9EE;
    local_rbx = 0;
    goto loc_0092E61E;
loc_0092E91F:
    if (condition_is_less_or_equal) goto loc_0092E7EE;
    result = memcpy(local_r12, result, (int32_t)(v_stack_p38), (uint32_t)(v_stack_p38));
    local_r12 = (local_r12) + ((int32_t)(v_stack_p38));
    goto loc_0092E7EE;
loc_0092E945:
    goto loc_0092E707;
loc_0092E951:
    if ((*(uint32_t *)(v_stack_mA8 + v_stack_mC0 * 1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC0))))) goto loc_0092E75A;
    Arg1 = (uint32_t)((local_r12) + 1);
    Arg2 = (v_stack_mC0) + (4);
    v_stack_mC0 = Arg2;
    goto loc_0092E881;
loc_0092E98D:
    v_stack_p28 = 8;
    v_stack_p40 = (int32_t)(v_stack_p38) + 8;
    result = RtlLengthSid((int32_t)(v_stack_p38) + 8, v_stack_p28, v_stack_p58, (uint32_t)(v_stack_p38));
    result = ((uint32_t)((uint32_t)(result))) + ((int32_t)(v_stack_p38) + 8);
    v_stack_p68 = result;
    result = RtlLengthSid((int32_t)(v_stack_p38) + 8, v_stack_p28, v_stack_p58, (uint32_t)(v_stack_p38));
    v_stack_p58 = (int32_t)(v_stack_p38);
    Arg1 = (uint32_t)((0) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) - (8));
    v_stack_p38 = (uint32_t)(Arg1);
    goto loc_0092E6B6;
loc_0092E9EE:
    goto loc_0092E726;
loc_0092E9F8:
    if ((*(uint8_t *)(result)) == 0) goto loc_0092E776;
    Arg3 = (uint32_t)((v_stack_p58) + (-16));
    local_rbx = (uint32_t)((local_rbx) + (-16));
    v_stack_p28 = Arg3;
    result = memcpy(v_stack_m68, (int32_t)(v_stack_p38), Arg3, v_stack_p30);
    goto loc_0092E77B;
loc_0092EA36:
    result = memcpy((int32_t)(v_stack_p38), local_r12, *(uint8_t *)(local_r12 + 0x1) * 4 + 8, v_stack_p30);
    local_rdi = ((int32_t)(v_stack_p38) + *(uint8_t *)(local_r12 + 0x1) * 4) + (8);
    goto loc_0092E7BB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x4` | `32` | `R` |
| `Arg8` | `+ 0x8` | `32` | `R` |
| `Arg8` | `+ 0xC` | `32` | `R` |
| `Arg11` | `+ 0x0` | `32` | `R` |
| `Arg11` | `+ 0x0` | `64` | `R` |
| `Arg11` | `+ 0x0` | `64` | `R/W` |
| `Arg13` | `+ 0x2` | `16` | `R` |
| `Arg13` | `+ 0x4` | `16` | `R/W` |
| `Arg15` | `+ 0x0` | `8` | `W` |
| `Arg16` | `+ 0x0` | `8` | `R` |
| `Arg16` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092E530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
