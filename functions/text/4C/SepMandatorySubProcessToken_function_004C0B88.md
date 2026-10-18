# SepMandatorySubProcessToken

- RVA: `0x004C0B88`–`0x004C0F54` (길이 `972` bytes)
- VA: `0x00000001404C0B88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC7B4`
- 디코드: `271`개 명령, `972/972` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004C0BFB` → [PsReferenceProcessFilePointer](../../page/8D/PsReferenceProcessFilePointer_function_008D6870.md) (function, `0x008D6870`)
- `0x004C0C21` → [RtlCreateSecurityDescriptor](../../page/9F/RtlCreateSecurityDescriptor_function_009F1DF0.md) (function, `0x009F1DF0`)
- `0x004C0C4D` → [ObQuerySecurityObject](../../page/9A/ObQuerySecurityObject_function_009A3564.md) (function, `0x009A3564`)
- `0x004C0C6A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004C0C89` → [RtlCreateSecurityDescriptor](../../page/9F/RtlCreateSecurityDescriptor_function_009F1DF0.md) (function, `0x009F1DF0`)
- `0x004C0CB2` → [ObQuerySecurityObject](../../page/9A/ObQuerySecurityObject_function_009A3564.md) (function, `0x009A3564`)
- `0x004C0CF4` → [RtlFindAceByType](../41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x004C0D09` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004C0D25` → [RtlSidDominates](../3F/RtlSidDominates_function_003FBD50.md) (function, `0x003FBD50`)
- `0x004C0D3F` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x004C0E0B` → [SeTokenIsAdmin](../../page/9F/SeTokenIsAdmin_function_009FE650.md) (function, `0x009FE650`)
- `0x004C0E23` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004C0E76` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004C0F14` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004C0F2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004C0F3A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADB2B`

### Static image references
- `0x004C0BA1` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x004C0BFB` → [PsReferenceProcessFilePointer](../../page/8D/PsReferenceProcessFilePointer_function_008D6870.md) (`.text` → `PAGE`)
  - `0x004C0C21` → [RtlCreateSecurityDescriptor](../../page/9F/RtlCreateSecurityDescriptor_function_009F1DF0.md) (`.text` → `PAGE`)
  - `0x004C0C4D` → [ObQuerySecurityObject](../../page/9A/ObQuerySecurityObject_function_009A3564.md) (`.text` → `PAGE`)
  - `0x004C0C6A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004C0C89` → [RtlCreateSecurityDescriptor](../../page/9F/RtlCreateSecurityDescriptor_function_009F1DF0.md) (`.text` → `PAGE`)
  - `0x004C0CB2` → [ObQuerySecurityObject](../../page/9A/ObQuerySecurityObject_function_009A3564.md) (`.text` → `PAGE`)
  - `0x004C0E0B` → [SeTokenIsAdmin](../../page/9F/SeTokenIsAdmin_function_009FE650.md) (`.text` → `PAGE`)
  - `0x004C0F2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C0B88  40 55                           push rbp
004C0B8A  53                              push rbx
004C0B8B  56                              push rsi
004C0B8C  57                              push rdi
004C0B8D  41 54                           push r12
004C0B8F  41 55                           push r13
004C0B91  41 56                           push r14
004C0B93  41 57                           push r15
004C0B95  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
004C0B9A  48 81 EC E8 00 00 00            sub rsp, 0xe8
004C0BA1  48 8B 05 98 9B 94 00            mov rax, qword ptr [rip + 0x949b98]
004C0BA8  48 33 C4                        xor rax, rsp
004C0BAB  48 89 45 07                     mov qword ptr [rbp + 7], rax
004C0BAF  45 33 F6                        xor r14d, r14d
004C0BB2  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
004C0BB7  4D 89 31                        mov qword ptr [r9], r14
004C0BBA  4D 8B F9                        mov r15, r9
004C0BBD  41 8B 80 FC 05 00 00            mov eax, dword ptr [r8 + 0x5fc]
004C0BC4  48 8B FA                        mov rdi, rdx
004C0BC7  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
004C0BCC  4C 8B E9                        mov r13, rcx
004C0BCF  44 88 74 24 30                  mov byte ptr [rsp + 0x30], r14b
004C0BD4  41 8B DE                        mov ebx, r14d
004C0BD7  45 8B E6                        mov r12d, r14d
004C0BDA  41 8B F6                        mov esi, r14d
004C0BDD  A8 01                           test al, 1
004C0BDF  0F 85 09 02 00 00               jne 0x1404c0dee
004C0BE5  8B 82 D4 00 00 00               mov eax, dword ptr [rdx + 0xd4]
004C0BEB  A8 02                           test al, 2
004C0BED  0F 84 FB 01 00 00               je 0x1404c0dee
004C0BF3  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004C0BF8  49 8B C8                        mov rcx, r8
004C0BFB  E8 70 5C 41 00                  call 0x1408d6870
004C0C00  8B D8                           mov ebx, eax
004C0C02  85 C0                           test eax, eax
004C0C04  0F 88 D2 01 00 00               js 0x1404c0ddc
004C0C0A  41 BC 80 00 00 00               mov r12d, 0x80
004C0C10  41 8D 56 01                     lea edx, [r14 + 1]
004C0C14  48 8D 4D 87                     lea rcx, [rbp - 0x79]
004C0C18  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
004C0C1D  48 8D 75 87                     lea rsi, [rbp - 0x79]
004C0C21  E8 CA 11 53 00                  call 0x1409f1df0
004C0C26  8B D8                           mov ebx, eax
004C0C28  85 C0                           test eax, eax
004C0C2A  0F 88 AC 01 00 00               js 0x1404c0ddc
004C0C30  45 8B CC                        mov r9d, r12d
004C0C33  48 8D 44 24 34                  lea rax, [rsp + 0x34]
004C0C38  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
004C0C3D  4C 8D 45 87                     lea r8, [rbp - 0x79]
004C0C41  49 8B CC                        mov rcx, r12
004C0C44  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004C0C49  41 8D 56 10                     lea edx, [r14 + 0x10]
004C0C4D  E8 12 29 4E 00                  call 0x1409a3564
004C0C52  8B D8                           mov ebx, eax
004C0C54  3D 23 00 00 C0                  cmp eax, 0xc0000023
004C0C59  75 5E                           jne 0x1404c0cb9
004C0C5B  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
004C0C5F  B9 00 01 00 00                  mov ecx, 0x100
004C0C64  41 B8 53 65 20 20               mov r8d, 0x20206553
004C0C6A  E8 81 14 6C 00                  call 0x140b820f0
004C0C6F  48 8B F0                        mov rsi, rax
004C0C72  48 85 C0                        test rax, rax
004C0C75  75 0A                           jne 0x1404c0c81
004C0C77  BB 17 00 00 C0                  mov ebx, 0xc0000017
004C0C7C  E9 86 02 00 00                  jmp 0x1404c0f07
004C0C81  BA 01 00 00 00                  mov edx, 1
004C0C86  48 8B CE                        mov rcx, rsi
004C0C89  E8 62 11 53 00                  call 0x1409f1df0
004C0C8E  8B D8                           mov ebx, eax
004C0C90  85 C0                           test eax, eax
004C0C92  0F 88 6F 02 00 00               js 0x1404c0f07
004C0C98  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
004C0C9D  48 8D 44 24 34                  lea rax, [rsp + 0x34]
004C0CA2  4C 8B C6                        mov r8, rsi
004C0CA5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004C0CAA  BA 10 00 00 00                  mov edx, 0x10
004C0CAF  49 8B CC                        mov rcx, r12
004C0CB2  E8 AD 28 4E 00                  call 0x1409a3564
004C0CB7  8B D8                           mov ebx, eax
004C0CB9  85 DB                           test ebx, ebx
004C0CBB  0F 88 16 01 00 00               js 0x1404c0dd7
004C0CC1  48 85 F6                        test rsi, rsi
004C0CC4  0F 84 0D 01 00 00               je 0x1404c0dd7
004C0CCA  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
004C0CCE  A8 10                           test al, 0x10
004C0CD0  75 05                           jne 0x1404c0cd7
004C0CD2  49 8B CE                        mov rcx, r14
004C0CD5  EB 16                           jmp 0x1404c0ced
004C0CD7  66 85 C0                        test ax, ax
004C0CDA  79 0D                           jns 0x1404c0ce9
004C0CDC  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
004C0CDF  85 C0                           test eax, eax
004C0CE1  74 EF                           je 0x1404c0cd2
004C0CE3  48 8D 0C 06                     lea rcx, [rsi + rax]
004C0CE7  EB 04                           jmp 0x1404c0ced
004C0CE9  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
004C0CED  45 33 C0                        xor r8d, r8d
004C0CF0  41 8D 50 11                     lea edx, [r8 + 0x11]
004C0CF4  E8 F7 FD F4 FF                  call 0x140410af0
004C0CF9  48 85 C0                        test rax, rax
004C0CFC  0F 84 EC 00 00 00               je 0x1404c0dee
004C0D02  48 8B CF                        mov rcx, rdi
004C0D05  4C 8D 70 08                     lea r14, [rax + 8]
004C0D09  E8 02 B2 F5 FF                  call 0x14041bf10
004C0D0E  4C 8B F8                        mov r15, rax
004C0D11  48 85 C0                        test rax, rax
004C0D14  0F 84 CC 00 00 00               je 0x1404c0de6
004C0D1A  48 8B 08                        mov rcx, qword ptr [rax]
004C0D1D  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
004C0D22  49 8B D6                        mov rdx, r14
004C0D25  E8 26 B0 F3 FF                  call 0x1403fbd50
004C0D2A  8B D8                           mov ebx, eax
004C0D2C  85 C0                           test eax, eax
004C0D2E  0F 88 D3 01 00 00               js 0x1404c0f07
004C0D34  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
004C0D39  0F 84 A7 00 00 00               je 0x1404c0de6
004C0D3F  E8 A4 6B 00 00                  call 0x1404c78e8
004C0D44  85 C0                           test eax, eax
004C0D46  74 2F                           je 0x1404c0d77
004C0D48  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
004C0D4D  84 C0                           test al, al
004C0D4F  75 04                           jne 0x1404c0d55
004C0D51  33 D2                           xor edx, edx
004C0D53  EB 07                           jmp 0x1404c0d5c
004C0D55  FF C8                           dec eax
004C0D57  41 8B 54 86 08                  mov edx, dword ptr [r14 + rax*4 + 8]
004C0D5C  49 8B 0F                        mov rcx, qword ptr [r15]
004C0D5F  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004C0D63  84 C0                           test al, al
004C0D65  74 10                           je 0x1404c0d77
004C0D67  FF C8                           dec eax
004C0D69  3B 54 81 08                     cmp edx, dword ptr [rcx + rax*4 + 8]
004C0D6D  73 08                           jae 0x1404c0d77
004C0D6F  0F BA B7 C8 00 00 00 0C         btr dword ptr [rdi + 0xc8], 0xc
004C0D77  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
004C0D7C  84 C0                           test al, al
004C0D7E  75 04                           jne 0x1404c0d84
004C0D80  33 C9                           xor ecx, ecx
004C0D82  EB 07                           jmp 0x1404c0d8b
004C0D84  FF C8                           dec eax
004C0D86  41 8B 4C 86 08                  mov ecx, dword ptr [r14 + rax*4 + 8]
004C0D8B  49 8B 07                        mov rax, qword ptr [r15]
004C0D8E  89 48 08                        mov dword ptr [rax + 8], ecx
004C0D91  49 8B 07                        mov rax, qword ptr [r15]
004C0D94  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
004C0D99  49 89 07                        mov qword ptr [r15], rax
004C0D9C  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
004C0DA1  84 C0                           test al, al
004C0DA3  75 08                           jne 0x1404c0dad
004C0DA5  45 33 F6                        xor r14d, r14d
004C0DA8  41 8B CE                        mov ecx, r14d
004C0DAB  EB 0A                           jmp 0x1404c0db7
004C0DAD  FF C8                           dec eax
004C0DAF  41 8B 4C 86 08                  mov ecx, dword ptr [r14 + rax*4 + 8]
004C0DB4  45 33 F6                        xor r14d, r14d
004C0DB7  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
004C0DBD  81 F9 00 20 00 00               cmp ecx, 0x2000
004C0DC3  73 06                           jae 0x1404c0dcb
004C0DC5  0F BA F0 0D                     btr eax, 0xd
004C0DC9  EB 04                           jmp 0x1404c0dcf
004C0DCB  0F BA E8 0D                     bts eax, 0xd
004C0DCF  89 87 C8 00 00 00               mov dword ptr [rdi + 0xc8], eax
004C0DD5  EB 17                           jmp 0x1404c0dee
004C0DD7  41 8B DE                        mov ebx, r14d
004C0DDA  EB 12                           jmp 0x1404c0dee
004C0DDC  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
004C0DE1  E9 21 01 00 00                  jmp 0x1404c0f07
004C0DE6  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
004C0DEB  45 33 F6                        xor r14d, r14d
004C0DEE  4D 85 ED                        test r13, r13
004C0DF1  0F 84 10 01 00 00               je 0x1404c0f07
004C0DF7  41 F7 85 C8 00 00 00 00 10 00 00  test dword ptr [r13 + 0xc8], 0x1000
004C0E02  0F 84 FF 00 00 00               je 0x1404c0f07
004C0E08  49 8B CD                        mov rcx, r13
004C0E0B  E8 40 D8 53 00                  call 0x1409fe650
004C0E10  84 C0                           test al, al
004C0E12  0F 85 EF 00 00 00               jne 0x1404c0f07
004C0E18  0F BA B7 C8 00 00 00 0C         btr dword ptr [rdi + 0xc8], 0xc
004C0E20  48 8B CF                        mov rcx, rdi
004C0E23  E8 E8 B0 F5 FF                  call 0x14041bf10
004C0E28  4C 8B C0                        mov r8, rax
004C0E2B  48 85 C0                        test rax, rax
004C0E2E  0F 84 D3 00 00 00               je 0x1404c0f07
004C0E34  48 8B 8F D8 00 00 00            mov rcx, qword ptr [rdi + 0xd8]
004C0E3B  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
004C0E3F  48 85 C9                        test rcx, rcx
004C0E42  75 32                           jne 0x1404c0e76
004C0E44  48 8B 10                        mov rdx, qword ptr [rax]
004C0E47  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
004C0E4B  84 C0                           test al, al
004C0E4D  0F 84 B4 00 00 00               je 0x1404c0f07
004C0E53  8D 48 FF                        lea ecx, [rax - 1]
004C0E56  41 B9 00 20 00 00               mov r9d, 0x2000
004C0E5C  44 39 4C 8A 08                  cmp dword ptr [rdx + rcx*4 + 8], r9d
004C0E61  0F 86 A0 00 00 00               jbe 0x1404c0f07
004C0E67  44 89 4A 08                     mov dword ptr [rdx + 8], r9d
004C0E6B  49 8B 00                        mov rax, qword ptr [r8]
004C0E6E  49 89 07                        mov qword ptr [r15], rax
004C0E71  E9 91 00 00 00                  jmp 0x1404c0f07
004C0E76  E8 95 B0 F5 FF                  call 0x14041bf10
004C0E7B  4C 8B D8                        mov r11, rax
004C0E7E  48 85 C0                        test rax, rax
004C0E81  0F 84 80 00 00 00               je 0x1404c0f07
004C0E87  4D 8B 08                        mov r9, qword ptr [r8]
004C0E8A  41 0F B6 49 01                  movzx ecx, byte ptr [r9 + 1]
004C0E8F  84 C9                           test cl, cl
004C0E91  74 08                           je 0x1404c0e9b
004C0E93  8D 41 FF                        lea eax, [rcx - 1]
004C0E96  45 8B 74 81 08                  mov r14d, dword ptr [r9 + rax*4 + 8]
004C0E9B  4D 8B 13                        mov r10, qword ptr [r11]
004C0E9E  41 0F B6 52 01                  movzx edx, byte ptr [r10 + 1]
004C0EA3  8D 4A FF                        lea ecx, [rdx - 1]
004C0EA6  84 D2                           test dl, dl
004C0EA8  75 04                           jne 0x1404c0eae
004C0EAA  33 C0                           xor eax, eax
004C0EAC  EB 05                           jmp 0x1404c0eb3
004C0EAE  41 8B 44 8A 08                  mov eax, dword ptr [r10 + rcx*4 + 8]
004C0EB3  44 3B F0                        cmp r14d, eax
004C0EB6  76 4F                           jbe 0x1404c0f07
004C0EB8  45 33 F6                        xor r14d, r14d
004C0EBB  41 8B C6                        mov eax, r14d
004C0EBE  84 D2                           test dl, dl
004C0EC0  74 05                           je 0x1404c0ec7
004C0EC2  41 8B 44 8A 08                  mov eax, dword ptr [r10 + rcx*4 + 8]
004C0EC7  41 89 41 08                     mov dword ptr [r9 + 8], eax
004C0ECB  49 8B 00                        mov rax, qword ptr [r8]
004C0ECE  49 89 07                        mov qword ptr [r15], rax
004C0ED1  49 8B 0B                        mov rcx, qword ptr [r11]
004C0ED4  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004C0ED8  84 C0                           test al, al
004C0EDA  75 05                           jne 0x1404c0ee1
004C0EDC  41 8B CE                        mov ecx, r14d
004C0EDF  EB 06                           jmp 0x1404c0ee7
004C0EE1  FF C8                           dec eax
004C0EE3  8B 4C 81 08                     mov ecx, dword ptr [rcx + rax*4 + 8]
004C0EE7  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
004C0EED  41 B9 00 20 00 00               mov r9d, 0x2000
004C0EF3  41 3B C9                        cmp ecx, r9d
004C0EF6  73 06                           jae 0x1404c0efe
004C0EF8  0F BA F0 0D                     btr eax, 0xd
004C0EFC  EB 03                           jmp 0x1404c0f01
004C0EFE  41 0B C1                        or eax, r9d
004C0F01  89 87 C8 00 00 00               mov dword ptr [rdi + 0xc8], eax
004C0F07  4D 85 E4                        test r12, r12
004C0F0A  74 0D                           je 0x1404c0f19
004C0F0C  BA 44 66 6C 74                  mov edx, 0x746c6644
004C0F11  49 8B CC                        mov rcx, r12
004C0F14  E8 C7 69 E3 FF                  call 0x1402f78e0
004C0F19  48 85 F6                        test rsi, rsi
004C0F1C  74 13                           je 0x1404c0f31
004C0F1E  48 8D 45 87                     lea rax, [rbp - 0x79]
004C0F22  48 3B F0                        cmp rsi, rax
004C0F25  74 0A                           je 0x1404c0f31
004C0F27  33 D2                           xor edx, edx
004C0F29  48 8B CE                        mov rcx, rsi
004C0F2C  E8 3F 19 6C 00                  call 0x140b82870
004C0F31  8B C3                           mov eax, ebx
004C0F33  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
004C0F37  48 33 CC                        xor rcx, rsp
004C0F3A  E8 01 B7 1E 00                  call 0x1406ac640
004C0F3F  48 81 C4 E8 00 00 00            add rsp, 0xe8
004C0F46  41 5F                           pop r15
004C0F48  41 5E                           pop r14
004C0F4A  41 5D                           pop r13
004C0F4C  41 5C                           pop r12
004C0F4E  5F                              pop rdi
004C0F4F  5E                              pop rsi
004C0F50  5B                              pop rbx
004C0F51  5D                              pop rbp
004C0F52  C3                              ret
004C0F53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepMandatorySubProcessToken(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int8 v_stack_mF8;

    v_rsp = (v_rsp) - (232);
    result = (*(unsigned __int64 *)(v_rip + 9739160)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r14 = 0;
    v_stack_mE8 = a4;
    *(unsigned __int64 *)(a4) = 0;
    v_stack_mF0 = 0;
    v_stack_mF8 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 1532)))) & (1)) != 0) goto loc_004C0DEE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 212)))) & (2)) == 0) goto loc_004C0DEE;
    result = PsReferenceProcessFilePointer(a3, v_stack_mF0, a3, a4);
    if (sign_flag) goto loc_004C0DDC;
    v_stack_mF4 = 128;
    result = RtlCreateSecurityDescriptor(v_stack_mD8, v_r14 + 1, a3, a4);
    if (sign_flag) goto loc_004C0DDC;
    v_stack_m108 = v_stack_mF4;
    result = ObQuerySecurityObject(v_stack_mF0, v_r14 + 16, v_stack_mD8, 128);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_004C0CB9;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mF4), (unsigned int)(0x20206553ULL), 128);
    if (result != 0) goto loc_004C0C81;
    goto loc_004C0F07;
loc_004C0C81:
    result = RtlCreateSecurityDescriptor(result, 1, (unsigned int)(0x20206553ULL), 128);
    if (sign_flag) goto loc_004C0F07;
    v_stack_m108 = v_stack_mF4;
    result = ObQuerySecurityObject(v_stack_mF0, 16, result, (unsigned int)(v_stack_mF4));
loc_004C0CB9:
    if (sign_flag) goto loc_004C0DD7;
    if (result == 0) goto loc_004C0DD7;
    if ((((unsigned __int8)(*(unsigned __int16 *)(result + 2))) & (16)) != 0) goto loc_004C0CD7;
loc_004C0CD2:
    goto loc_004C0CED;
loc_004C0CD7:
    if (!sign_flag) goto loc_004C0CE9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 12))) == 0) goto loc_004C0CD2;
    goto loc_004C0CED;
loc_004C0CE9:
loc_004C0CED:
    a3 = 0;
    result = RtlFindAceByType(*(unsigned __int64 *)(result + 24), a3 + 17, a3, (unsigned int)(v_stack_mF4));
    if (result == 0) goto loc_004C0DEE;
    result = SepLocateTokenIntegrity(a2, a3 + 17, a3, (unsigned int)(v_stack_mF4));
    if (result == 0) goto loc_004C0DE6;
    result = RtlSidDominates(*(unsigned __int64 *)(result), result + 8, v_stack_mF8, (unsigned int)(v_stack_mF4));
    if (sign_flag) goto loc_004C0F07;
    if (v_stack_mF8 == 0) goto loc_004C0DE6;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(result), result + 8, v_stack_mF8, (unsigned int)(v_stack_mF4));
    if ((unsigned int)(result) == 0) goto loc_004C0D77;
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 8 + 1)) != 0) goto loc_004C0D55;
    a2 = 0;
    goto loc_004C0D5C;
loc_004C0D55:
    result = (unsigned int)((*(unsigned __int8 *)(result + 8 + 1)) - 1);
loc_004C0D5C:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004C0D77;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8 + result * 4 + 8)))) < (*(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8))) {
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 8 + 1)) != 0) goto loc_004C0D84;
    a1 = 0;
    goto loc_004C0D8B;
loc_004C0D84:
    result = (unsigned int)((*(unsigned __int8 *)(result + 8 + 1)) - 1);
loc_004C0D8B:
    *(unsigned int *)(*(unsigned __int64 *)(result) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8 + result * 4 + 8)));
    *(unsigned __int64 *)(v_stack_mE8) = *(unsigned __int64 *)(result);
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 8 + 1)) != 0) goto loc_004C0DAD;
    v_r14 = 0;
    goto loc_004C0DB7;
loc_004C0DAD:
    result = (unsigned int)((*(unsigned __int8 *)(result + 8 + 1)) - 1);
    v_r14 = 0;
loc_004C0DB7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + result * 4 + 8)))) >= 0x2000ULL) goto loc_004C0DCB;
    goto loc_004C0DCF;
loc_004C0DCB:
loc_004C0DCF:
    *(unsigned int *)(a2 + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 200)));
    goto loc_004C0DEE;
loc_004C0DD7:
    goto loc_004C0DEE;
loc_004C0DDC:
    goto loc_004C0F07;
loc_004C0DE6:
    v_r14 = 0;
loc_004C0DEE:
    if (0 == 0) goto loc_004C0F07;
    if (((*(unsigned int *)(a1 + 200)) & (0x1000ULL)) == 0) goto loc_004C0F07;
    result = SeTokenIsAdmin(0, (unsigned int)(*(unsigned int *)(result + 8 + result * 4 + 8)), v_stack_mF8, (unsigned int)(v_stack_mF4));
    if ((unsigned __int8)(result) != 0) goto loc_004C0F07;
    result = SepLocateTokenIntegrity(0, (unsigned int)(*(unsigned int *)(result + 8 + result * 4 + 8)), v_stack_mF8, (unsigned int)(v_stack_mF4));
    if (result == 0) goto loc_004C0F07;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 216) + 56) != 0) goto loc_004C0E76;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004C0F07;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1 * 4 + 8)) <= ((unsigned int)((unsigned int)(0x2000ULL)))) goto loc_004C0F07;
    *(unsigned int *)(*(unsigned __int64 *)(result) + 8) = (unsigned int)((unsigned int)(0x2000ULL));
    *(unsigned __int64 *)(v_stack_mE8) = *(unsigned __int64 *)(result);
    goto loc_004C0F07;
loc_004C0E76:
    result = SepLocateTokenIntegrity(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1, *(unsigned __int64 *)(result), result, (unsigned int)(0x2000ULL));
    if (result == 0) goto loc_004C0F07;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1;
        v_r14 = *(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8);
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004C0EAE;
    result = 0;
    goto loc_004C0EB3;
loc_004C0EAE:
loc_004C0EB3:
    if (((unsigned int)(v_r14)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1 * 4 + 8))))) goto loc_004C0F07;
    v_r14 = 0;
    result = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(result) + *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1 * 4 + 8);
    }
    *(unsigned int *)(*(unsigned __int64 *)(result) + 8) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_mE8) = *(unsigned __int64 *)(result);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004C0EE1;
    goto loc_004C0EE7;
loc_004C0EE1:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
loc_004C0EE7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + result * 4 + 8)))) >= ((unsigned int)((unsigned int)(0x2000ULL)))) goto loc_004C0EFE;
    goto loc_004C0F01;
loc_004C0EFE:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 200))) | ((unsigned int)((unsigned int)(0x2000ULL))));
loc_004C0F01:
    *(unsigned int *)(a2 + 200) = (unsigned int)(result);
loc_004C0F07:
    if (v_stack_mF0 != 0) {
        a2 = 0x746C6644ULL;
        a1 = v_stack_mF0;
        result = ObfDereferenceObjectWithTag(a1, a2, result, (unsigned int)(0x2000ULL));
    }
    if (result == 0) goto loc_004C0F31;
    result = v_stack_mD8;
    if (result != v_stack_mD8) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)(0x2000ULL));
    }
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, result, (unsigned int)(0x2000ULL));
    v_rsp = (v_rsp) + (232);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepMandatorySubProcessToken(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint8_t v_stack_mF8;

    local_rsp = (local_rsp) - (232);
    result = (*(uint64_t *)(v_rip + 0x949B98)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r14 = 0;
    v_stack_mE8 = Arg4;
    *(uint64_t *)(arg4) = 0;
    v_stack_mF0 = 0;
    v_stack_mF8 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x5FC)))) & (1)) != 0) goto loc_004C0DEE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xD4)))) & (2)) == 0) goto loc_004C0DEE;
    result = PsReferenceProcessFilePointer(Arg3, v_stack_mF0, Arg3, Arg4);
    if (sign_flag) goto loc_004C0DDC;
    v_stack_mF4 = 128;
    result = RtlCreateSecurityDescriptor(v_stack_mD8, local_r14 + 1, Arg3, Arg4);
    if (sign_flag) goto loc_004C0DDC;
    v_stack_m108 = v_stack_mF4;
    result = ObQuerySecurityObject(v_stack_mF0, local_r14 + 16, v_stack_mD8, 128);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_004C0CB9;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mF4), (uint32_t)(0x20206553ULL), 128);
    if (result != 0) goto loc_004C0C81;
    goto loc_004C0F07;
loc_004C0C81:
    result = RtlCreateSecurityDescriptor(result, 1, (uint32_t)(0x20206553ULL), 128);
    if (sign_flag) goto loc_004C0F07;
    v_stack_m108 = v_stack_mF4;
    result = ObQuerySecurityObject(v_stack_mF0, 16, result, (uint32_t)(v_stack_mF4));
loc_004C0CB9:
    if (sign_flag) goto loc_004C0DD7;
    if (result == 0) goto loc_004C0DD7;
    if ((((uint8_t)(*(uint16_t *)(result + 0x2))) & (16)) != 0) goto loc_004C0CD7;
loc_004C0CD2:
    goto loc_004C0CED;
loc_004C0CD7:
    if (!sign_flag) goto loc_004C0CE9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC))) == 0) goto loc_004C0CD2;
    goto loc_004C0CED;
loc_004C0CE9:
loc_004C0CED:
    Arg3 = 0;
    result = RtlFindAceByType(*(uint64_t *)(result + 0x18), Arg3 + 17, Arg3, (uint32_t)(v_stack_mF4));
    if (result == 0) goto loc_004C0DEE;
    result = SepLocateTokenIntegrity(Arg2, Arg3 + 17, Arg3, (uint32_t)(v_stack_mF4));
    if (result == 0) goto loc_004C0DE6;
    result = RtlSidDominates(*(uint64_t *)(result), result + 8, v_stack_mF8, (uint32_t)(v_stack_mF4));
    if (sign_flag) goto loc_004C0F07;
    if (v_stack_mF8 == 0) goto loc_004C0DE6;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(result), result + 8, v_stack_mF8, (uint32_t)(v_stack_mF4));
    if ((uint32_t)(result) == 0) goto loc_004C0D77;
    if ((uint8_t)(*(uint8_t *)(result + 0x8 + 0x1)) != 0) goto loc_004C0D55;
    Arg2 = 0;
    goto loc_004C0D5C;
loc_004C0D55:
    result = (uint32_t)((*(uint8_t *)(result + 0x8 + 0x1)) - 1);
loc_004C0D5C:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004C0D77;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8 + result * 4 + 0x8)))) < (*(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8))) {
    }
    if ((uint8_t)(*(uint8_t *)(result + 0x8 + 0x1)) != 0) goto loc_004C0D84;
    Arg1 = 0;
    goto loc_004C0D8B;
loc_004C0D84:
    result = (uint32_t)((*(uint8_t *)(result + 0x8 + 0x1)) - 1);
loc_004C0D8B:
    *(uint32_t *)(*(uint64_t *)(result) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8 + result * 4 + 0x8)));
    *(uint64_t *)(v_stack_mE8) = *(uint64_t *)(result);
    if ((uint8_t)(*(uint8_t *)(result + 0x8 + 0x1)) != 0) goto loc_004C0DAD;
    local_r14 = 0;
    goto loc_004C0DB7;
loc_004C0DAD:
    result = (uint32_t)((*(uint8_t *)(result + 0x8 + 0x1)) - 1);
    local_r14 = 0;
loc_004C0DB7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + result * 4 + 0x8)))) >= 0x2000ULL) goto loc_004C0DCB;
    goto loc_004C0DCF;
loc_004C0DCB:
loc_004C0DCF:
    *(uint32_t *)(arg2 + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC8)));
    goto loc_004C0DEE;
loc_004C0DD7:
    goto loc_004C0DEE;
loc_004C0DDC:
    goto loc_004C0F07;
loc_004C0DE6:
    local_r14 = 0;
loc_004C0DEE:
    if (0 == 0) goto loc_004C0F07;
    if (((*(uint32_t *)(Arg1 + 0xC8)) & (0x1000ULL)) == 0) goto loc_004C0F07;
    result = SeTokenIsAdmin(0, (uint32_t)(*(uint32_t *)(result + 0x8 + result * 4 + 0x8)), v_stack_mF8, (uint32_t)(v_stack_mF4));
    if ((uint8_t)(result) != 0) goto loc_004C0F07;
    result = SepLocateTokenIntegrity(0, (uint32_t)(*(uint32_t *)(result + 0x8 + result * 4 + 0x8)), v_stack_mF8, (uint32_t)(v_stack_mF4));
    if (result == 0) goto loc_004C0F07;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0xD8) + 0x38) != 0) goto loc_004C0E76;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004C0F07;
    if ((*(uint32_t *)(*(uint64_t *)(result) + *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 0x1 * 4 + 0x8)) <= ((uint32_t)((uint32_t)(0x2000ULL)))) goto loc_004C0F07;
    *(uint32_t *)(*(uint64_t *)(result) + 0x8) = (uint32_t)((uint32_t)(0x2000ULL));
    *(uint64_t *)(v_stack_mE8) = *(uint64_t *)(result);
    goto loc_004C0F07;
loc_004C0E76:
    result = SepLocateTokenIntegrity(*(uint8_t *)(*(uint64_t *)(result) + 0x1) - 1, *(uint64_t *)(result), result, (uint32_t)(0x2000ULL));
    if (result == 0) goto loc_004C0F07;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 1;
        local_r14 = *(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8);
    }
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004C0EAE;
    result = 0;
    goto loc_004C0EB3;
loc_004C0EAE:
loc_004C0EB3:
    if (((uint32_t)(local_r14)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 0x1 * 4 + 0x8))))) goto loc_004C0F07;
    local_r14 = 0;
    result = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(result) + *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 0x1 * 4 + 0x8);
    }
    *(uint32_t *)(*(uint64_t *)(result) + 0x8) = (uint32_t)(result);
    *(uint64_t *)(v_stack_mE8) = *(uint64_t *)(result);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004C0EE1;
    goto loc_004C0EE7;
loc_004C0EE1:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
loc_004C0EE7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + result * 4 + 0x8)))) >= ((uint32_t)((uint32_t)(0x2000ULL)))) goto loc_004C0EFE;
    goto loc_004C0F01;
loc_004C0EFE:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0xC8))) | ((uint32_t)((uint32_t)(0x2000ULL))));
loc_004C0F01:
    *(uint32_t *)(arg2 + 0xC8) = (uint32_t)(result);
loc_004C0F07:
    if (v_stack_mF0 != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = v_stack_mF0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, result, (uint32_t)(0x2000ULL));
    }
    if (result == 0) goto loc_004C0F31;
    result = v_stack_mD8;
    if (result != v_stack_mD8) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)(0x2000ULL));
    }
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, result, (uint32_t)(0x2000ULL));
    local_rsp = (local_rsp) + (232);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xC8` | `32` | `R` |
| `Arg2` | `+ 0xC8` | `32` | `R/W` |
| `Arg2` | `+ 0xC8` | `32` | `W` |
| `Arg2` | `+ 0xD4` | `32` | `R` |
| `Arg2` | `+ 0xD8` | `64` | `R` |
| `Arg3` | `+ 0x5FC` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C0B88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
