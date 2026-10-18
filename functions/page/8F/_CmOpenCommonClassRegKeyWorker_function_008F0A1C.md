# _CmOpenCommonClassRegKeyWorker

- RVA: `0x008F0A1C`–`0x008F0FFD` (길이 `1,505` bytes)
- VA: `0x00000001408F0A1C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008721C`
- 디코드: `386`개 명령, `1,505/1,505` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008F0A7E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F0AAE` → [_CmGetCommonClassRegKeyPath](_CmGetCommonClassRegKeyPath_function_008F1CC0.md) (function, `0x008F1CC0`)
- `0x008F0ADA` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008F0B01` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F0B97` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F0BCF` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F0C48` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F0C8F` → [NLS_UPCASE](../../text/3F/NLS_UPCASE_function_003FF700.md) (function, `0x003FF700`)
- `0x008F0C9E` → [NLS_UPCASE](../../text/3F/NLS_UPCASE_function_003FF700.md) (function, `0x003FF700`)
- `0x008F0CB7` → [RtlPrefixUnicodeString](RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x008F0CFB` → [_PnpCtxGetCachedNodeBaseKey](../8E/_PnpCtxGetCachedNodeBaseKey_function_008EF9C0.md) (function, `0x008EF9C0`)
- `0x008F0D50` → [_RegRtlOpenKeyTransacted](../8E/_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x008F0EB4` → [SysCtxRegOpenCurrentUserKey](SysCtxRegOpenCurrentUserKey_function_008F455C.md) (function, `0x008F455C`)
- `0x008F0EFB` → [PnpCtxRegCreateTree](../93/PnpCtxRegCreateTree_function_00931CA0.md) (function, `0x00931CA0`)
- `0x008F0F36` → [_PnpCtxGetCachedContextBaseKey](../8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (function, `0x008EFB2C`)
- `0x008F0F5C` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x008F0F79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F0FF3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmOpenCommonClassRegKey](../8E/CmOpenCommonClassRegKey_function_008EFF5C.md) at `0x008F0059`
- [IopGetDeviceInterfaces](IopGetDeviceInterfaces_function_008F0120.md) at `0x008F02CF`

### Static image references
- `0x008F0B06` → RVA `0x00001A10` (`.rdata`; read)
- `0x008F0BD4` → RVA `0x00001A50` (`.rdata`; read)
- `0x008F0C4D` → RVA `0x00001A60` (`.rdata`; read)
- `0x008F0CB0` → RVA `0x00001B78` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x008F0A7E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F0ADA` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008F0B01` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F0B97` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F0BCF` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F0C48` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F0C8F` → [NLS_UPCASE](../../text/3F/NLS_UPCASE_function_003FF700.md) (`PAGE` → `.text`)
  - `0x008F0C9E` → [NLS_UPCASE](../../text/3F/NLS_UPCASE_function_003FF700.md) (`PAGE` → `.text`)
  - `0x008F0F79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F0FF3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x008F0F8F` → [sub_00B1E68E](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FA5` → [sub_00B1E68E + 0xA](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FAE` → [sub_00B1E68E + 0x35](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FB7` → [sub_00B1E68E + 0x23](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FC0` → [sub_00B1E68E + 0x35](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FC9` → [sub_00B1E68E + 0x35](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FD2` → [sub_00B1E68E + 0x1E](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)
  - `0x008F0FD8` → [sub_00B1E68E + 0x35](../B1/Unknown_function_00B1E68E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008F0A1C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008F0A21  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008F0A26  55                              push rbp
008F0A27  56                              push rsi
008F0A28  57                              push rdi
008F0A29  41 54                           push r12
008F0A2B  41 55                           push r13
008F0A2D  41 56                           push r14
008F0A2F  41 57                           push r15
008F0A31  48 8B EC                        mov rbp, rsp
008F0A34  48 83 EC 60                     sub rsp, 0x60
008F0A38  33 C0                           xor eax, eax
008F0A3A  0F 57 C0                        xorps xmm0, xmm0
008F0A3D  89 45 50                        mov dword ptr [rbp + 0x50], eax
008F0A40  45 8B E1                        mov r12d, r9d
008F0A43  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
008F0A47  45 8B F8                        mov r15d, r8d
008F0A4A  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
008F0A4E  48 8B DA                        mov rbx, rdx
008F0A51  44 8D 70 04                     lea r14d, [rax + 4]
008F0A55  48 8B F1                        mov rsi, rcx
008F0A58  41 8B C0                        mov eax, r8d
008F0A5B  25 00 02 00 00                  and eax, 0x200
008F0A60  F7 D8                           neg eax
008F0A62  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
008F0A66  1B FF                           sbb edi, edi
008F0A68  83 E7 78                        and edi, 0x78
008F0A6B  81 C7 C8 00 00 00               add edi, 0xc8
008F0A71  8B D7                           mov edx, edi
008F0A73  B9 00 01 00 00                  mov ecx, 0x100
008F0A78  41 B8 50 4E 50 52               mov r8d, 0x52504e50
008F0A7E  E8 6D 16 29 00                  call 0x140b820f0
008F0A83  4C 8B E8                        mov r13, rax
008F0A86  48 85 C0                        test rax, rax
008F0A89  0F 84 5A 05 00 00               je 0x1408f0fe9
008F0A8F  8B CF                           mov ecx, edi
008F0A91  48 8D 45 50                     lea rax, [rbp + 0x50]
008F0A95  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F0A9A  45 8B CC                        mov r9d, r12d
008F0A9D  D1 E9                           shr ecx, 1
008F0A9F  45 8B C7                        mov r8d, r15d
008F0AA2  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
008F0AA6  48 8B D3                        mov rdx, rbx
008F0AA9  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008F0AAE  E8 0D 12 00 00                  call 0x1408f1cc0
008F0AB3  8B D8                           mov ebx, eax
008F0AB5  3D 23 00 00 C0                  cmp eax, 0xc0000023
008F0ABA  0F 84 B4 04 00 00               je 0x1408f0f74
008F0AC0  85 C0                           test eax, eax
008F0AC2  0F 88 B8 00 00 00               js 0x1408f0b80
008F0AC8  41 0F BA E7 08                  bt r15d, 8
008F0ACD  0F 82 C7 03 00 00               jb 0x1408f0e9a
008F0AD3  49 8B D5                        mov rdx, r13
008F0AD6  48 8D 4D F0                     lea rcx, [rbp - 0x10]
008F0ADA  E8 81 2E B7 FF                  call 0x140463960
008F0ADF  8B D8                           mov ebx, eax
008F0AE1  85 C0                           test eax, eax
008F0AE3  0F 88 97 00 00 00               js 0x1408f0b80
008F0AE9  0F B7 5D F0                     movzx ebx, word ptr [rbp - 0x10]
008F0AED  3B DF                           cmp ebx, edi
008F0AEF  0F 83 86 00 00 00               jae 0x1408f0b7b
008F0AF5  41 B8 32 00 00 00               mov r8d, 0x32
008F0AFB  66 41 3B D8                     cmp bx, r8w
008F0AFF  76 7A                           jbe 0x1408f0b7b
008F0B01  E8 EA D6 A0 FF                  call 0x1402fe1f0
008F0B06  4C 8B 15 03 0F 71 FF            mov r10, qword ptr [rip - 0x8ef0fd]
008F0B0D  4C 8B 98 B0 04 00 00            mov r11, qword ptr [rax + 0x4b0]
008F0B14  41 3B D8                        cmp ebx, r8d
008F0B17  72 62                           jb 0x1408f0b7b
008F0B19  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
008F0B1D  4D 8D 7A 32                     lea r15, [r10 + 0x32]
008F0B21  49 2B FA                        sub rdi, r10
008F0B24  BA C0 00 00 00                  mov edx, 0xc0
008F0B29  4D 3B D7                        cmp r10, r15
008F0B2C  0F 83 85 00 00 00               jae 0x1408f0bb7
008F0B32  45 0F B7 02                     movzx r8d, word ptr [r10]
008F0B36  46 0F B7 0C 17                  movzx r9d, word ptr [rdi + r10]
008F0B3B  66 45 3B C1                     cmp r8w, r9w
008F0B3F  75 06                           jne 0x1408f0b47
008F0B41  49 83 C2 02                     add r10, 2
008F0B45  EB E2                           jmp 0x1408f0b29
008F0B47  41 83 F8 61                     cmp r8d, 0x61
008F0B4B  72 0F                           jb 0x1408f0b5c
008F0B4D  41 83 F8 7A                     cmp r8d, 0x7a
008F0B51  0F 87 1F 02 00 00               ja 0x1408f0d76
008F0B57  66 41 83 E8 20                  sub r8w, 0x20
008F0B5C  41 83 F9 61                     cmp r9d, 0x61
008F0B60  72 0F                           jb 0x1408f0b71
008F0B62  41 83 F9 7A                     cmp r9d, 0x7a
008F0B66  0F 87 50 02 00 00               ja 0x1408f0dbc
008F0B6C  66 41 83 E9 20                  sub r9w, 0x20
008F0B71  66 45 3B C1                     cmp r8w, r9w
008F0B75  0F 84 51 01 00 00               je 0x1408f0ccc
008F0B7B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F0B80  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
008F0B84  48 85 C9                        test rcx, rcx
008F0B87  0F 85 66 04 00 00               jne 0x1408f0ff3
008F0B8D  4D 85 ED                        test r13, r13
008F0B90  74 0A                           je 0x1408f0b9c
008F0B92  33 D2                           xor edx, edx
008F0B94  49 8B CD                        mov rcx, r13
008F0B97  E8 D4 1C 29 00                  call 0x140b82870
008F0B9C  8B C3                           mov eax, ebx
008F0B9E  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
008F0BA6  48 83 C4 60                     add rsp, 0x60
008F0BAA  41 5F                           pop r15
008F0BAC  41 5E                           pop r14
008F0BAE  41 5D                           pop r13
008F0BB0  41 5C                           pop r12
008F0BB2  5F                              pop rdi
008F0BB3  5E                              pop rsi
008F0BB4  5D                              pop rbp
008F0BB5  C3                              ret
008F0BB6  CC                              int3
008F0BB7  B8 CE FF 00 00                  mov eax, 0xffce
008F0BBC  49 8D 7D 32                     lea rdi, [r13 + 0x32]
008F0BC0  66 01 45 F2                     add word ptr [rbp - 0xe], ax
008F0BC4  66 03 D8                        add bx, ax
008F0BC7  66 89 5D F0                     mov word ptr [rbp - 0x10], bx
008F0BCB  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
008F0BCF  E8 1C D6 A0 FF                  call 0x1402fe1f0
008F0BD4  4C 8B 15 75 0E 71 FF            mov r10, qword ptr [rip - 0x8ef18b]
008F0BDB  4C 8B 98 B0 04 00 00            mov r11, qword ptr [rax + 0x4b0]
008F0BE2  B8 1C 00 00 00                  mov eax, 0x1c
008F0BE7  66 3B D8                        cmp bx, ax
008F0BEA  72 5C                           jb 0x1408f0c48
008F0BEC  4C 8B FF                        mov r15, rdi
008F0BEF  4D 8D 62 1C                     lea r12, [r10 + 0x1c]
008F0BF3  4D 2B FA                        sub r15, r10
008F0BF6  4D 3B D4                        cmp r10, r12
008F0BF9  0F 83 D7 00 00 00               jae 0x1408f0cd6
008F0BFF  45 0F B7 02                     movzx r8d, word ptr [r10]
008F0C03  47 0F B7 0C 17                  movzx r9d, word ptr [r15 + r10]
008F0C08  66 45 3B C1                     cmp r8w, r9w
008F0C0C  75 06                           jne 0x1408f0c14
008F0C0E  49 83 C2 02                     add r10, 2
008F0C12  EB E2                           jmp 0x1408f0bf6
008F0C14  41 83 F8 61                     cmp r8d, 0x61
008F0C18  72 0F                           jb 0x1408f0c29
008F0C1A  41 83 F8 7A                     cmp r8d, 0x7a
008F0C1E  0F 87 E8 01 00 00               ja 0x1408f0e0c
008F0C24  66 41 83 E8 20                  sub r8w, 0x20
008F0C29  41 83 F9 61                     cmp r9d, 0x61
008F0C2D  72 0F                           jb 0x1408f0c3e
008F0C2F  41 83 F9 7A                     cmp r9d, 0x7a
008F0C33  0F 87 19 02 00 00               ja 0x1408f0e52
008F0C39  66 41 83 E9 20                  sub r9w, 0x20
008F0C3E  66 45 3B C1                     cmp r8w, r9w
008F0C42  0F 84 24 01 00 00               je 0x1408f0d6c
008F0C48  E8 A3 D5 A0 FF                  call 0x1402fe1f0
008F0C4D  4C 8B 15 0C 0E 71 FF            mov r10, qword ptr [rip - 0x8ef1f4]
008F0C54  4C 8B B8 B0 04 00 00            mov r15, qword ptr [rax + 0x4b0]
008F0C5B  B8 2C 00 00 00                  mov eax, 0x2c
008F0C60  66 3B D8                        cmp bx, ax
008F0C63  72 44                           jb 0x1408f0ca9
008F0C65  4C 8B DF                        mov r11, rdi
008F0C68  4D 8D 62 2C                     lea r12, [r10 + 0x2c]
008F0C6C  4D 2B DA                        sub r11, r10
008F0C6F  4D 3B D4                        cmp r10, r12
008F0C72  0F 83 85 01 00 00               jae 0x1408f0dfd
008F0C78  41 0F B7 1A                     movzx ebx, word ptr [r10]
008F0C7C  43 0F B7 14 13                  movzx edx, word ptr [r11 + r10]
008F0C81  66 3B DA                        cmp bx, dx
008F0C84  75 06                           jne 0x1408f0c8c
008F0C86  49 83 C2 02                     add r10, 2
008F0C8A  EB E3                           jmp 0x1408f0c6f
008F0C8C  49 8B CF                        mov rcx, r15
008F0C8F  E8 6C EA B0 FF                  call 0x1403ff700
008F0C94  0F B7 D3                        movzx edx, bx
008F0C97  49 8B CF                        mov rcx, r15
008F0C9A  44 0F B7 C8                     movzx r9d, ax
008F0C9E  E8 5D EA B0 FF                  call 0x1403ff700
008F0CA3  66 41 3B C1                     cmp ax, r9w
008F0CA7  74 DD                           je 0x1408f0c86
008F0CA9  41 B0 01                        mov r8b, 1
008F0CAC  48 8D 55 F0                     lea rdx, [rbp - 0x10]
008F0CB0  48 8D 0D C1 0E 71 FF            lea rcx, [rip - 0x8ef13f]
008F0CB7  E8 B4 42 00 00                  call 0x1408f4f70
008F0CBC  84 C0                           test al, al
008F0CBE  74 20                           je 0x1408f0ce0
008F0CC0  41 BE 0E 00 00 00               mov r14d, 0xe
008F0CC6  48 83 C7 24                     add rdi, 0x24
008F0CCA  EB 14                           jmp 0x1408f0ce0
008F0CCC  BA C0 00 00 00                  mov edx, 0xc0
008F0CD1  E9 6B FE FF FF                  jmp 0x1408f0b41
008F0CD6  41 BE 07 00 00 00               mov r14d, 7
008F0CDC  48 83 C7 1C                     add rdi, 0x1c
008F0CE0  41 8B C6                        mov eax, r14d
008F0CE3  48 8B 54 C6 60                  mov rdx, qword ptr [rsi + rax*8 + 0x60]
008F0CE8  48 85 D2                        test rdx, rdx
008F0CEB  0F 84 AD 02 00 00               je 0x1408f0f9e
008F0CF1  4C 8D 4D E0                     lea r9, [rbp - 0x20]
008F0CF5  45 8B C6                        mov r8d, r14d
008F0CF8  48 8B CE                        mov rcx, rsi
008F0CFB  E8 C0 EC FF FF                  call 0x1408ef9c0
008F0D00  8B D8                           mov ebx, eax
008F0D02  85 C0                           test eax, eax
008F0D04  0F 88 76 FE FF FF               js 0x1408f0b80
008F0D0A  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008F0D0E  80 7D 68 00                     cmp byte ptr [rbp + 0x68], 0
008F0D12  0F 85 B8 01 00 00               jne 0x1408f0ed0
008F0D18  48 85 F6                        test rsi, rsi
008F0D1B  0F 84 72 01 00 00               je 0x1408f0e93
008F0D21  48 8B 86 E0 00 00 00            mov rax, qword ptr [rsi + 0xe0]
008F0D28  48 85 C0                        test rax, rax
008F0D2B  0F 84 62 01 00 00               je 0x1408f0e93
008F0D31  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
008F0D35  4C 8B 7D 70                     mov r15, qword ptr [rbp + 0x70]
008F0D39  45 33 C0                        xor r8d, r8d
008F0D3C  44 8B 65 60                     mov r12d, dword ptr [rbp + 0x60]
008F0D40  45 8B CC                        mov r9d, r12d
008F0D43  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
008F0D48  48 8B D7                        mov rdx, rdi
008F0D4B  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
008F0D50  E8 BB EA FF FF                  call 0x1408ef810
008F0D55  85 C0                           test eax, eax
008F0D57  0F 88 A5 01 00 00               js 0x1408f0f02
008F0D5D  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
008F0D61  C7 00 02 00 00 00               mov dword ptr [rax], 2
008F0D67  E9 14 FE FF FF                  jmp 0x1408f0b80
008F0D6C  BA C0 00 00 00                  mov edx, 0xc0
008F0D71  E9 98 FE FF FF                  jmp 0x1408f0c0e
008F0D76  4D 85 DB                        test r11, r11
008F0D79  0F 84 DD FD FF FF               je 0x1408f0b5c
008F0D7F  66 44 3B C2                     cmp r8w, dx
008F0D83  0F 82 D3 FD FF FF               jb 0x1408f0b5c
008F0D89  49 8B C0                        mov rax, r8
008F0D8C  41 8B D0                        mov edx, r8d
008F0D8F  48 C1 E8 08                     shr rax, 8
008F0D93  83 E2 0F                        and edx, 0xf
008F0D96  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
008F0D9B  41 8B C0                        mov eax, r8d
008F0D9E  C1 E8 04                        shr eax, 4
008F0DA1  83 E0 0F                        and eax, 0xf
008F0DA4  03 C8                           add ecx, eax
008F0DA6  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
008F0DAB  03 CA                           add ecx, edx
008F0DAD  BA C0 00 00 00                  mov edx, 0xc0
008F0DB2  66 45 03 04 4B                  add r8w, word ptr [r11 + rcx*2]
008F0DB7  E9 A0 FD FF FF                  jmp 0x1408f0b5c
008F0DBC  4D 85 DB                        test r11, r11
008F0DBF  0F 84 AC FD FF FF               je 0x1408f0b71
008F0DC5  66 44 3B CA                     cmp r9w, dx
008F0DC9  0F 82 A2 FD FF FF               jb 0x1408f0b71
008F0DCF  49 8B C1                        mov rax, r9
008F0DD2  41 8B D1                        mov edx, r9d
008F0DD5  48 C1 E8 08                     shr rax, 8
008F0DD9  83 E2 0F                        and edx, 0xf
008F0DDC  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
008F0DE1  41 8B C1                        mov eax, r9d
008F0DE4  C1 E8 04                        shr eax, 4
008F0DE7  83 E0 0F                        and eax, 0xf
008F0DEA  03 C8                           add ecx, eax
008F0DEC  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
008F0DF1  03 CA                           add ecx, edx
008F0DF3  66 45 03 0C 4B                  add r9w, word ptr [r11 + rcx*2]
008F0DF8  E9 74 FD FF FF                  jmp 0x1408f0b71
008F0DFD  41 BE 08 00 00 00               mov r14d, 8
008F0E03  48 83 C7 2C                     add rdi, 0x2c
008F0E07  E9 D4 FE FF FF                  jmp 0x1408f0ce0
008F0E0C  4D 85 DB                        test r11, r11
008F0E0F  0F 84 14 FE FF FF               je 0x1408f0c29
008F0E15  66 44 3B C2                     cmp r8w, dx
008F0E19  0F 82 0A FE FF FF               jb 0x1408f0c29
008F0E1F  49 8B C0                        mov rax, r8
008F0E22  41 8B D0                        mov edx, r8d
008F0E25  48 C1 E8 08                     shr rax, 8
008F0E29  83 E2 0F                        and edx, 0xf
008F0E2C  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
008F0E31  41 8B C0                        mov eax, r8d
008F0E34  C1 E8 04                        shr eax, 4
008F0E37  83 E0 0F                        and eax, 0xf
008F0E3A  03 C8                           add ecx, eax
008F0E3C  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
008F0E41  03 CA                           add ecx, edx
008F0E43  BA C0 00 00 00                  mov edx, 0xc0
008F0E48  66 45 03 04 4B                  add r8w, word ptr [r11 + rcx*2]
008F0E4D  E9 D7 FD FF FF                  jmp 0x1408f0c29
008F0E52  4D 85 DB                        test r11, r11
008F0E55  0F 84 E3 FD FF FF               je 0x1408f0c3e
008F0E5B  66 44 3B CA                     cmp r9w, dx
008F0E5F  0F 82 D9 FD FF FF               jb 0x1408f0c3e
008F0E65  49 8B C1                        mov rax, r9
008F0E68  41 8B D1                        mov edx, r9d
008F0E6B  48 C1 E8 08                     shr rax, 8
008F0E6F  83 E2 0F                        and edx, 0xf
008F0E72  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
008F0E77  41 8B C1                        mov eax, r9d
008F0E7A  C1 E8 04                        shr eax, 4
008F0E7D  83 E0 0F                        and eax, 0xf
008F0E80  03 C8                           add ecx, eax
008F0E82  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
008F0E87  03 CA                           add ecx, edx
008F0E89  66 45 03 0C 4B                  add r9w, word ptr [r11 + rcx*2]
008F0E8E  E9 AB FD FF FF                  jmp 0x1408f0c3e
008F0E93  33 D2                           xor edx, edx
008F0E95  E9 9B FE FF FF                  jmp 0x1408f0d35
008F0E9A  49 8B FD                        mov rdi, r13
008F0E9D  48 85 F6                        test rsi, rsi
008F0EA0  0F 85 37 01 00 00               jne 0x1408f0fdd
008F0EA6  33 C9                           xor ecx, ecx
008F0EA8  4C 8D 4D E8                     lea r9, [rbp - 0x18]
008F0EAC  33 D2                           xor edx, edx
008F0EAE  41 B8 00 00 00 02               mov r8d, 0x2000000
008F0EB4  E8 A3 36 00 00                  call 0x1408f455c
008F0EB9  8B D8                           mov ebx, eax
008F0EBB  85 C0                           test eax, eax
008F0EBD  0F 88 BD FC FF FF               js 0x1408f0b80
008F0EC3  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
008F0EC7  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
008F0ECB  E9 3E FE FF FF                  jmp 0x1408f0d0e
008F0ED0  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
008F0ED4  48 8B D1                        mov rdx, rcx
008F0ED7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F0EDC  45 33 C9                        xor r9d, r9d
008F0EDF  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
008F0EE3  4C 8B C7                        mov r8, rdi
008F0EE6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F0EEB  48 8B CE                        mov rcx, rsi
008F0EEE  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
008F0EF4  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
008F0EF7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008F0EFB  E8 A0 0D 04 00                  call 0x140931ca0
008F0F00  EB 07                           jmp 0x1408f0f09
008F0F02  3D 34 00 00 C0                  cmp eax, 0xc0000034
008F0F07  74 16                           je 0x1408f0f1f
008F0F09  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008F0F0E  74 5A                           je 0x1408f0f6a
008F0F10  85 C0                           test eax, eax
008F0F12  0F 89 68 FC FF FF               jns 0x1408f0b80
008F0F18  8B D8                           mov ebx, eax
008F0F1A  E9 61 FC FF FF                  jmp 0x1408f0b80
008F0F1F  41 83 FE 08                     cmp r14d, 8
008F0F23  75 F3                           jne 0x1408f0f18
008F0F25  80 7E 04 00                     cmp byte ptr [rsi + 4], 0
008F0F29  74 ED                           je 0x1408f0f18
008F0F2B  4C 8D 45 E0                     lea r8, [rbp - 0x20]
008F0F2F  48 8B CE                        mov rcx, rsi
008F0F32  41 8D 56 01                     lea edx, [r14 + 1]
008F0F36  E8 F1 EB FF FF                  call 0x1408efb2c
008F0F3B  8B D8                           mov ebx, eax
008F0F3D  85 C0                           test eax, eax
008F0F3F  0F 88 3B FC FF FF               js 0x1408f0b80
008F0F45  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
008F0F49  45 33 C9                        xor r9d, r9d
008F0F4C  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008F0F51  4C 8B C7                        mov r8, rdi
008F0F54  48 8B CE                        mov rcx, rsi
008F0F57  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008F0F5C  E8 57 E8 FF FF                  call 0x1408ef7b8
008F0F61  85 C0                           test eax, eax
008F0F63  78 A4                           js 0x1408f0f09
008F0F65  E9 F3 FD FF FF                  jmp 0x1408f0d5d
008F0F6A  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008F0F6F  E9 0C FC FF FF                  jmp 0x1408f0b80
008F0F74  33 D2                           xor edx, edx
008F0F76  49 8B CD                        mov rcx, r13
008F0F79  E8 F2 18 29 00                  call 0x140b82870
008F0F7E  8B 7D 50                        mov edi, dword ptr [rbp + 0x50]
008F0F81  45 33 ED                        xor r13d, r13d
008F0F84  48 03 FF                        add rdi, rdi
008F0F87  B8 FF FF FF FF                  mov eax, 0xffffffff
008F0F8C  48 3B F8                        cmp rdi, rax
008F0F8F  0F 87 F9 D6 22 00               ja 0x140b1e68e
008F0F95  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
008F0F99  E9 D3 FA FF FF                  jmp 0x1408f0a71
008F0F9E  41 8B CE                        mov ecx, r14d
008F0FA1  41 83 FE 0A                     cmp r14d, 0xa
008F0FA5  0F 87 ED D6 22 00               ja 0x140b1e698
008F0FAB  83 E9 04                        sub ecx, 4
008F0FAE  0F 84 0F D7 22 00               je 0x140b1e6c3
008F0FB4  83 E9 01                        sub ecx, 1
008F0FB7  0F 84 F4 D6 22 00               je 0x140b1e6b1
008F0FBD  83 E9 01                        sub ecx, 1
008F0FC0  0F 84 FD D6 22 00               je 0x140b1e6c3
008F0FC6  83 E9 01                        sub ecx, 1
008F0FC9  0F 84 F4 D6 22 00               je 0x140b1e6c3
008F0FCF  83 E9 01                        sub ecx, 1
008F0FD2  0F 85 D4 D6 22 00               jne 0x140b1e6ac
008F0FD8  E9 E6 D6 22 00                  jmp 0x140b1e6c3
008F0FDD  48 8B 8E E0 00 00 00            mov rcx, qword ptr [rsi + 0xe0]
008F0FE4  E9 BF FE FF FF                  jmp 0x1408f0ea8
008F0FE9  BB 17 00 00 C0                  mov ebx, 0xc0000017
008F0FEE  E9 8D FB FF FF                  jmp 0x1408f0b80
008F0FF3  E8 B8 C2 DB FF                  call 0x1406ad2b0
008F0FF8  E9 90 FB FF FF                  jmp 0x1408f0b8d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmOpenCommonClassRegKeyWorker(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, unsigned __int8 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int16 v_stack_m46;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_p18 = 0;
    v_stack_m58 = 0;
    v_stack_m50 = 0;
    result = (unsigned int)(((unsigned int)(a3)) & (512));
    result = (unsigned int)(-(result));
    v_stack_m48 = v_xmm0;
    v_rdi = (unsigned int)((v_rdi) & (120));
    v_rdi = (unsigned int)((v_rdi) + (200));
loc_008F0A71:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x52504E50ULL), a4);
    if (result == 0) goto loc_008F0FE9;
    v_stack_m60 = v_stack_p18;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (1));
    v_stack_m68 = (unsigned int)(a1);
    v_stack_m70 = result;
    result = _CmGetCommonClassRegKeyPath(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008F0F74;
    if (sign_flag) goto loc_008F0B80;
    if (condition_is_below) goto loc_008F0E9A;
    result = RtlInitUnicodeStringEx(v_stack_m48, result, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (sign_flag) goto loc_008F0B80;
    if (((unsigned int)(v_stack_m48)) >= ((unsigned int)(v_rdi))) goto loc_008F0B7B;
    if (((unsigned __int16)(v_stack_m48)) <= 50) goto loc_008F0B7B;
    result = PsGetCurrentServerSiloGlobals(v_stack_m48, result, 50, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (((unsigned int)(v_stack_m48)) < 50) goto loc_008F0B7B;
    v_rdi = (v_stack_m40) - (*(unsigned __int64 *)(v_rip - 9367805));
loc_008F0B29:
    if ((*(unsigned __int64 *)(v_rip - 9367805)) >= (*(unsigned __int64 *)(v_rip - 9367805) + 50)) goto loc_008F0BB7;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367805)))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9367805) * 1)))) goto loc_008F0B47;
loc_008F0B41:
    v_r10 = (*(unsigned __int64 *)(v_rip - 9367805)) + (2);
    goto loc_008F0B29;
loc_008F0B47:
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367805)))) < 97) goto loc_008F0B5C;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367805)))) > 122) goto loc_008F0D76;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367805))) - (32));
loc_008F0B5C:
    if (((unsigned int)(*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9367805) * 1))) < 97) goto loc_008F0B71;
    if (((unsigned int)(*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9367805) * 1))) > 122) goto loc_008F0DBC;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9367805) * 1)) - (32));
loc_008F0B71:
    if (((unsigned __int16)(a3)) == ((unsigned __int16)(a4))) goto loc_008F0CCC;
loc_008F0B7B:
loc_008F0B80:
    if (v_stack_m50 != 0) goto loc_008F0FF3;
loc_008F0B8D:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_008F0BB7:
    v_rbx = (unsigned __int16)((v_stack_p8) + ((unsigned __int16)((unsigned int)(0xFFCEULL))));
    v_stack_m48 = (unsigned __int16)(v_rbx);
    v_stack_m40 = result + 50;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    if (((unsigned __int16)(v_rbx)) < 28) goto loc_008F0C48;
    v_r15 = (result + 50) - (*(unsigned __int64 *)(v_rip - 9367947));
loc_008F0BF6:
    if ((*(unsigned __int64 *)(v_rip - 9367947)) >= (*(unsigned __int64 *)(v_rip - 9367947) + 28)) goto loc_008F0CD6;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367947)))) != ((unsigned __int16)(*(unsigned __int16 *)(v_r15 + *(unsigned __int64 *)(v_rip - 9367947) * 1)))) goto loc_008F0C14;
loc_008F0C0E:
    v_r10 = (*(unsigned __int64 *)(v_rip - 9367947)) + (2);
    goto loc_008F0BF6;
loc_008F0C14:
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367947)))) < 97) goto loc_008F0C29;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367947)))) > 122) goto loc_008F0E0C;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9367947))) - (32));
loc_008F0C29:
    if (((unsigned int)(*(unsigned __int16 *)(v_r15 + *(unsigned __int64 *)(v_rip - 9367947) * 1))) < 97) goto loc_008F0C3E;
    if (((unsigned int)(*(unsigned __int16 *)(v_r15 + *(unsigned __int64 *)(v_rip - 9367947) * 1))) > 122) goto loc_008F0E52;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(v_r15 + *(unsigned __int64 *)(v_rip - 9367947) * 1)) - (32));
loc_008F0C3E:
    if (((unsigned __int16)(a3)) == ((unsigned __int16)(a4))) goto loc_008F0D6C;
loc_008F0C48:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    if (((unsigned __int16)(v_rbx)) < 44) goto loc_008F0CA9;
    v_r11 = (result + 50) - (*(unsigned __int64 *)(v_rip - 9368052));
loc_008F0C6F:
    if ((*(unsigned __int64 *)(v_rip - 9368052)) >= (*(unsigned __int64 *)(v_rip - 9368052) + 44)) goto loc_008F0DFD;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9368052)))) != ((unsigned __int16)(*(unsigned __int16 *)(v_r11 + *(unsigned __int64 *)(v_rip - 9368052) * 1)))) goto loc_008F0C8C;
loc_008F0C86:
    v_r10 = (*(unsigned __int64 *)(v_rip - 9368052)) + (2);
    goto loc_008F0C6F;
loc_008F0C8C:
    result = NLS_UPCASE(*(unsigned __int64 *)(result + 1200), *(unsigned __int16 *)(v_r11 + *(unsigned __int64 *)(v_rip - 9368052) * 1), a3, a4);
    result = NLS_UPCASE(*(unsigned __int64 *)(result + 1200), (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9368052))), a3, (unsigned __int16)(result));
    if (((unsigned __int16)(result)) == ((unsigned __int16)((unsigned __int16)(result)))) goto loc_008F0C86;
loc_008F0CA9:
    result = RtlPrefixUnicodeString(v_rip - 9367871, v_stack_m48, 1, (unsigned __int16)(result));
    if ((unsigned __int8)(result) == 0) goto loc_008F0CE0;
    v_rdi = (result + 50) + (36);
    goto loc_008F0CE0;
loc_008F0CCC:
    goto loc_008F0B41;
loc_008F0CD6:
    v_rdi = (v_rdi) + (28);
loc_008F0CE0:
    if (*(unsigned __int64 *)(a1 + 7 * 8 + 96) == 0) goto loc_008F0F9E;
    result = _PnpCtxGetCachedNodeBaseKey(a1, *(unsigned __int64 *)(a1 + 7 * 8 + 96), 7, v_stack_m58);
    if (sign_flag) goto loc_008F0B80;
loc_008F0D0E:
    if (a6 != 0) goto loc_008F0ED0;
    if (a1 == 0) goto loc_008F0E93;
    if (*(unsigned __int64 *)(a1 + 224) == 0) goto loc_008F0E93;
loc_008F0D35:
    a3 = 0;
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8);
    v_stack_p20 = a7;
    result = _RegRtlOpenKeyTransacted(v_stack_m58, v_rdi, a3, (unsigned int)((unsigned int)((unsigned int)(a5))));
    if (sign_flag) goto loc_008F0F02;
loc_008F0D5D:
    *(unsigned int *)(a8) = 2;
    goto loc_008F0B80;
loc_008F0D6C:
    goto loc_008F0C0E;
loc_008F0D76:
    if (v_r11 == 0) goto loc_008F0B5C;
    if (0 < 192) goto loc_008F0B5C;
    result = (0) >> (8);
    a2 = (unsigned int)((0) & (15));
    result = (unsigned int)((0) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + a1 * 2)) + ((unsigned int)(a2)));
    a3 = (unsigned __int16)((a3) + (*(unsigned __int16 *)(v_r11 + a1 * 2)));
    goto loc_008F0B5C;
loc_008F0DBC:
    if (v_r11 == 0) goto loc_008F0B71;
    if (((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(a5))))) < 192) goto loc_008F0B71;
    result = ((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (8);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5)))))) & (15));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a5)))))) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)(((unsigned int)((unsigned int)((unsigned int)(a5)))) + (*(unsigned __int16 *)(v_r11 + a1 * 2)));
    goto loc_008F0B71;
loc_008F0DFD:
    v_rdi = (v_rdi) + (44);
    goto loc_008F0CE0;
loc_008F0E0C:
    if (v_r11 == 0) goto loc_008F0C29;
    if (((unsigned __int16)(a3)) < ((unsigned __int16)(a2))) goto loc_008F0C29;
    result = (a3) >> (8);
    a2 = (unsigned int)(((unsigned int)(a3)) & (15));
    result = (unsigned int)(((unsigned int)(a3)) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + a1 * 2)) + ((unsigned int)(a2)));
    a3 = (unsigned __int16)((a3) + (*(unsigned __int16 *)(v_r11 + a1 * 2)));
    goto loc_008F0C29;
loc_008F0E52:
    if (v_r11 == 0) goto loc_008F0C3E;
    if (((unsigned __int16)(a4)) < 192) goto loc_008F0C3E;
    result = (a4) >> (8);
    a2 = (unsigned int)(((unsigned int)(a4)) & (15));
    result = (unsigned int)(((unsigned int)(a4)) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)((a4) + (*(unsigned __int16 *)(v_r11 + a1 * 2)));
    goto loc_008F0C3E;
loc_008F0E93:
    a2 = 0;
    goto loc_008F0D35;
loc_008F0E9A:
    if (a1 != 0) goto loc_008F0FDD;
    a1 = 0;
loc_008F0EA8:
    a2 = 0;
    result = SysCtxRegOpenCurrentUserKey(a1, a2, (unsigned int)(0x2000000ULL), v_stack_m50);
    if (sign_flag) goto loc_008F0B80;
    v_stack_m58 = v_stack_m50;
    goto loc_008F0D0E;
loc_008F0ED0:
    v_stack_p38 = a8;
    a4 = 0;
    v_stack_p30 = a7;
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = PnpCtxRegCreateTree(0, v_stack_m50, result, a4);
    goto loc_008F0F09;
loc_008F0F02:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_008F0F1F;
loc_008F0F09:
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_008F0F6A;
    if (!sign_flag) goto loc_008F0B80;
loc_008F0F18:
    goto loc_008F0B80;
loc_008F0F1F:
    if (8 != 8) goto loc_008F0F18;
    if ((*(unsigned __int8 *)(a1 + 4)) == 0) goto loc_008F0F18;
    result = _PnpCtxGetCachedContextBaseKey(0, 8 + 1, v_stack_m58, a4);
    if (sign_flag) goto loc_008F0B80;
    a4 = 0;
    v_stack_p28 = a7;
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = PnpCtxRegOpenKey(0, v_stack_m58, result, a4);
    if (sign_flag) goto loc_008F0F09;
    goto loc_008F0D5D;
loc_008F0F6A:
    goto loc_008F0B80;
loc_008F0F74:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, result, a4);
    v_r13 = 0;
    v_rdi = ((unsigned int)(v_stack_p18)) + ((unsigned int)(v_stack_p18));
    goto loc_008F0A71;
loc_008F0F9E:
    a1 = (unsigned int)((8) - (4));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
loc_008F0FDD:
    goto loc_008F0EA8;
loc_008F0FE9:
    goto loc_008F0B80;
loc_008F0FF3:
    result = ZwClose(*(unsigned __int64 *)(a1 + 224), a2, result, a4);
    goto loc_008F0B8D;
}
```

## 5. (Beta) C Style

```c
int64_t _CmOpenCommonClassRegKeyWorker(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, int64_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint16_t v_stack_m46;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_p18 = 0;
    v_stack_m58 = 0;
    v_stack_m50 = 0;
    result = (uint32_t)(((uint32_t)(Arg3)) & (512));
    result = (uint32_t)(-(result));
    v_stack_m48 = v_xmm0;
    local_rdi = (uint32_t)((local_rdi) & (120));
    local_rdi = (uint32_t)((local_rdi) + (200));
loc_008F0A71:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x52504E50ULL), Arg4);
    if (result == 0) goto loc_008F0FE9;
    v_stack_m60 = v_stack_p18;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (1));
    v_stack_m68 = (uint32_t)(Arg1);
    v_stack_m70 = result;
    result = _CmGetCommonClassRegKeyPath(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008F0F74;
    if (sign_flag) goto loc_008F0B80;
    if (condition_is_below) goto loc_008F0E9A;
    result = RtlInitUnicodeStringEx(v_stack_m48, result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (sign_flag) goto loc_008F0B80;
    if (((uint32_t)(v_stack_m48)) >= ((uint32_t)(local_rdi))) goto loc_008F0B7B;
    if (((uint16_t)(v_stack_m48)) <= 50) goto loc_008F0B7B;
    result = PsGetCurrentServerSiloGlobals(v_stack_m48, result, 50, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (((uint32_t)(v_stack_m48)) < 50) goto loc_008F0B7B;
    local_rdi = (v_stack_m40) - (*(uint64_t *)(v_rip - 0x8EF0FD));
loc_008F0B29:
    if ((*(uint64_t *)(v_rip - 0x8EF0FD)) >= (*(uint64_t *)(v_rip - 0x8EF0FD) + 50)) goto loc_008F0BB7;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF0FD)))) != ((uint16_t)(*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8EF0FD) * 1)))) goto loc_008F0B47;
loc_008F0B41:
    local_r10 = (*(uint64_t *)(v_rip - 0x8EF0FD)) + (2);
    goto loc_008F0B29;
loc_008F0B47:
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF0FD)))) < 97) goto loc_008F0B5C;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF0FD)))) > 122) goto loc_008F0D76;
    Arg3 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF0FD))) - (32));
loc_008F0B5C:
    if (((uint32_t)(*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8EF0FD) * 1))) < 97) goto loc_008F0B71;
    if (((uint32_t)(*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8EF0FD) * 1))) > 122) goto loc_008F0DBC;
    Arg4 = (uint16_t)((*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8EF0FD) * 1)) - (32));
loc_008F0B71:
    if (((uint16_t)(Arg3)) == ((uint16_t)(Arg4))) goto loc_008F0CCC;
loc_008F0B7B:
loc_008F0B80:
    if (v_stack_m50 != 0) goto loc_008F0FF3;
loc_008F0B8D:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_008F0BB7:
    local_rbx = (uint16_t)((v_stack_p8) + ((uint16_t)((uint32_t)(0xFFCEULL))));
    v_stack_m48 = (uint16_t)(local_rbx);
    v_stack_m40 = result + 50;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    if (((uint16_t)(local_rbx)) < 28) goto loc_008F0C48;
    local_r15 = (result + 50) - (*(uint64_t *)(v_rip - 0x8EF18B));
loc_008F0BF6:
    if ((*(uint64_t *)(v_rip - 0x8EF18B)) >= (*(uint64_t *)(v_rip - 0x8EF18B) + 28)) goto loc_008F0CD6;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF18B)))) != ((uint16_t)(*(uint16_t *)(local_r15 + *(uint64_t *)(v_rip - 0x8EF18B) * 1)))) goto loc_008F0C14;
loc_008F0C0E:
    local_r10 = (*(uint64_t *)(v_rip - 0x8EF18B)) + (2);
    goto loc_008F0BF6;
loc_008F0C14:
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF18B)))) < 97) goto loc_008F0C29;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF18B)))) > 122) goto loc_008F0E0C;
    Arg3 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF18B))) - (32));
loc_008F0C29:
    if (((uint32_t)(*(uint16_t *)(local_r15 + *(uint64_t *)(v_rip - 0x8EF18B) * 1))) < 97) goto loc_008F0C3E;
    if (((uint32_t)(*(uint16_t *)(local_r15 + *(uint64_t *)(v_rip - 0x8EF18B) * 1))) > 122) goto loc_008F0E52;
    Arg4 = (uint16_t)((*(uint16_t *)(local_r15 + *(uint64_t *)(v_rip - 0x8EF18B) * 1)) - (32));
loc_008F0C3E:
    if (((uint16_t)(Arg3)) == ((uint16_t)(Arg4))) goto loc_008F0D6C;
loc_008F0C48:
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    if (((uint16_t)(local_rbx)) < 44) goto loc_008F0CA9;
    local_r11 = (result + 50) - (*(uint64_t *)(v_rip - 0x8EF1F4));
loc_008F0C6F:
    if ((*(uint64_t *)(v_rip - 0x8EF1F4)) >= (*(uint64_t *)(v_rip - 0x8EF1F4) + 44)) goto loc_008F0DFD;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF1F4)))) != ((uint16_t)(*(uint16_t *)(local_r11 + *(uint64_t *)(v_rip - 0x8EF1F4) * 1)))) goto loc_008F0C8C;
loc_008F0C86:
    local_r10 = (*(uint64_t *)(v_rip - 0x8EF1F4)) + (2);
    goto loc_008F0C6F;
loc_008F0C8C:
    result = NLS_UPCASE(*(uint64_t *)(result + 0x4B0), *(uint16_t *)(local_r11 + *(uint64_t *)(v_rip - 0x8EF1F4) * 1), Arg3, Arg4);
    result = NLS_UPCASE(*(uint64_t *)(result + 0x4B0), (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8EF1F4))), Arg3, (uint16_t)(result));
    if (((uint16_t)(result)) == ((uint16_t)((uint16_t)(result)))) goto loc_008F0C86;
loc_008F0CA9:
    result = RtlPrefixUnicodeString(v_rip - 9367871, v_stack_m48, 1, (uint16_t)(result));
    if ((uint8_t)(result) == 0) goto loc_008F0CE0;
    local_rdi = (result + 50) + (36);
    goto loc_008F0CE0;
loc_008F0CCC:
    goto loc_008F0B41;
loc_008F0CD6:
    local_rdi = (local_rdi) + (28);
loc_008F0CE0:
    if (*(uint64_t *)(arg1 + 0x7 * 8 + 0x60) == 0) goto loc_008F0F9E;
    result = _PnpCtxGetCachedNodeBaseKey(Arg1, *(uint64_t *)(arg1 + 0x7 * 8 + 0x60), 7, v_stack_m58);
    if (sign_flag) goto loc_008F0B80;
loc_008F0D0E:
    if (Arg6 != 0) goto loc_008F0ED0;
    if (Arg1 == NULL) goto loc_008F0E93;
    if (*(uint64_t *)(arg1 + 0xE0) == 0) goto loc_008F0E93;
loc_008F0D35:
    Arg3 = 0;
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x8);
    v_stack_p20 = Arg7;
    result = _RegRtlOpenKeyTransacted(v_stack_m58, local_rdi, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    if (sign_flag) goto loc_008F0F02;
loc_008F0D5D:
    *(uint32_t *)(arg8) = 2;
    goto loc_008F0B80;
loc_008F0D6C:
    goto loc_008F0C0E;
loc_008F0D76:
    if (local_r11 == 0) goto loc_008F0B5C;
    if (0 < 192) goto loc_008F0B5C;
    result = (0) >> (8);
    Arg2 = (uint32_t)((0) & (15));
    result = (uint32_t)((0) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg3 = (uint16_t)((Arg3) + (*(uint16_t *)(local_r11 + arg1 * 2)));
    goto loc_008F0B5C;
loc_008F0DBC:
    if (local_r11 == 0) goto loc_008F0B71;
    if (((uint16_t)((uint32_t)((uint32_t)((uint32_t)(Arg5))))) < 192) goto loc_008F0B71;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (8);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5)))))) & (15));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg5)))))) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) + (*(uint16_t *)(local_r11 + arg1 * 2)));
    goto loc_008F0B71;
loc_008F0DFD:
    local_rdi = (local_rdi) + (44);
    goto loc_008F0CE0;
loc_008F0E0C:
    if (local_r11 == 0) goto loc_008F0C29;
    if (((uint16_t)(Arg3)) < ((uint16_t)(Arg2))) goto loc_008F0C29;
    result = (Arg3) >> (8);
    Arg2 = (uint32_t)(((uint32_t)(Arg3)) & (15));
    result = (uint32_t)(((uint32_t)(Arg3)) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg3 = (uint16_t)((Arg3) + (*(uint16_t *)(local_r11 + arg1 * 2)));
    goto loc_008F0C29;
loc_008F0E52:
    if (local_r11 == 0) goto loc_008F0C3E;
    if (((uint16_t)(Arg4)) < 192) goto loc_008F0C3E;
    result = (Arg4) >> (8);
    Arg2 = (uint32_t)(((uint32_t)(Arg4)) & (15));
    result = (uint32_t)(((uint32_t)(Arg4)) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)((Arg4) + (*(uint16_t *)(local_r11 + arg1 * 2)));
    goto loc_008F0C3E;
loc_008F0E93:
    Arg2 = 0;
    goto loc_008F0D35;
loc_008F0E9A:
    if (Arg1 != NULL) goto loc_008F0FDD;
    Arg1 = 0;
loc_008F0EA8:
    Arg2 = 0;
    result = SysCtxRegOpenCurrentUserKey(Arg1, Arg2, (uint32_t)(0x2000000ULL), v_stack_m50);
    if (sign_flag) goto loc_008F0B80;
    v_stack_m58 = v_stack_m50;
    goto loc_008F0D0E;
loc_008F0ED0:
    v_stack_p38 = Arg8;
    Arg4 = 0;
    v_stack_p30 = Arg7;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = PnpCtxRegCreateTree(0, v_stack_m50, result, Arg4);
    goto loc_008F0F09;
loc_008F0F02:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_008F0F1F;
loc_008F0F09:
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_008F0F6A;
    if (!sign_flag) goto loc_008F0B80;
loc_008F0F18:
    goto loc_008F0B80;
loc_008F0F1F:
    if (8 != 8) goto loc_008F0F18;
    if ((*(uint8_t *)(arg1 + 0x4)) == 0) goto loc_008F0F18;
    result = _PnpCtxGetCachedContextBaseKey(0, 8 + 1, v_stack_m58, Arg4);
    if (sign_flag) goto loc_008F0B80;
    Arg4 = 0;
    v_stack_p28 = Arg7;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = PnpCtxRegOpenKey(0, v_stack_m58, result, Arg4);
    if (sign_flag) goto loc_008F0F09;
    goto loc_008F0D5D;
loc_008F0F6A:
    goto loc_008F0B80;
loc_008F0F74:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, result, Arg4);
    local_r13 = 0;
    local_rdi = ((uint32_t)(v_stack_p18)) + ((uint32_t)(v_stack_p18));
    goto loc_008F0A71;
loc_008F0F9E:
    Arg1 = (uint32_t)((8) - (4));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
loc_008F0FDD:
    goto loc_008F0EA8;
loc_008F0FE9:
    goto loc_008F0B80;
loc_008F0FF3:
    result = ZwClose(*(uint64_t *)(arg1 + 0xE0), Arg2, result, Arg4);
    goto loc_008F0B8D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60 + rax*8` | `64` | `R` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F0A1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
