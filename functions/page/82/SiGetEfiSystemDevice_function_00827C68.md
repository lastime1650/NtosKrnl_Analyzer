# SiGetEfiSystemDevice

- RVA: `0x00827C68`–`0x008280B9` (길이 `1,105` bytes)
- VA: `0x0000000140827C68`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DA6F8`
- 디코드: `293`개 명령, `1,105/1,105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00827D17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00827D3D` → [SiDisambiguateSystemDevice](SiDisambiguateSystemDevice_function_00827B9C.md) (function, `0x00827B9C`)
- `0x00827D55` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00827D8A` → [ZwOpenDirectoryObject](../../text/6A/ZwOpenDirectoryObject_function_006ADBD0.md) (function, `0x006ADBD0`)
- `0x00827DAD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00827DE5` → [ZwQueryDirectoryObject](../../text/6A/ZwQueryDirectoryObject_function_006AFAB0.md) (function, `0x006AFAB0`)
- `0x00827DF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00827E37` → [SiIsValidDiskDevice](SiIsValidDiskDevice_function_00828470.md) (function, `0x00828470`)
- `0x00827E5E` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x00827E8F` → [SiIssueSynchronousIoctl](SiIssueSynchronousIoctl_function_00827A34.md) (function, `0x00827A34`)
- `0x00827EE2` → [SiIssueSynchronousIoctl](SiIssueSynchronousIoctl_function_00827A34.md) (function, `0x00827A34`)
- `0x00827F0D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00827F20` → [SiGetDriveLayoutInformation](SiGetDriveLayoutInformation_function_00827934.md) (function, `0x00827934`)
- `0x00827FD0` → [SiGetEspFromFirmware](SiGetEspFromFirmware_function_008280C0.md) (function, `0x008280C0`)
- `0x0082802F` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x00828042` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x00828052` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828066` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828075` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00828084` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00828092` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00B3A076](../B3/Unknown_function_00B3A076.md) at `0x00B3A07B`
- [sub_00B3A106](../B3/Unknown_function_00B3A106.md) at `0x00B3A10E`

### Static image references
- `0x00827C8B` → RVA `0x00E0A740` (`.data`; read)
- `0x00827D4A` → RVA `0x00B0BD30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00827E57` → RVA `0x00B0BD40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00827F4F` → RVA `0x0001ABB0` (`.rdata`; read)
- `0x00827F5C` → RVA `0x0001ABB8` (`.rdata`; read)
- `0x0082803B` → RVA `0x00B08940` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00827D17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00827D55` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00827D8A` → [ZwOpenDirectoryObject](../../text/6A/ZwOpenDirectoryObject_function_006ADBD0.md) (`PAGE` → `.text`)
  - `0x00827DAD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00827DE5` → [ZwQueryDirectoryObject](../../text/6A/ZwQueryDirectoryObject_function_006AFAB0.md) (`PAGE` → `.text`)
  - `0x00827DF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00827E5E` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x00827F0D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082802F` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x00828042` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x00828052` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828066` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828075` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00828084` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00828092` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00827C68  48 8B C4                        mov rax, rsp
00827C6B  48 89 58 08                     mov qword ptr [rax + 8], rbx
00827C6F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00827C73  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00827C77  55                              push rbp
00827C78  41 54                           push r12
00827C7A  41 55                           push r13
00827C7C  41 56                           push r14
00827C7E  41 57                           push r15
00827C80  48 8D 68 C8                     lea rbp, [rax - 0x38]
00827C84  48 81 EC 10 01 00 00            sub rsp, 0x110
00827C8B  48 8B 05 AE 2A 5E 00            mov rax, qword ptr [rip + 0x5e2aae]
00827C92  48 33 C4                        xor rax, rsp
00827C95  48 89 45 08                     mov qword ptr [rbp + 8], rax
00827C99  45 33 E4                        xor r12d, r12d
00827C9C  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
00827CA1  33 C0                           xor eax, eax
00827CA3  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00827CA7  0F 57 C0                        xorps xmm0, xmm0
00827CAA  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00827CAE  4D 8B F0                        mov r14, r8
00827CB1  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
00827CB6  0F 57 C9                        xorps xmm1, xmm1
00827CB9  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00827CBD  41 8B DC                        mov ebx, r12d
00827CC0  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00827CC3  8D 50 6A                        lea edx, [rax + 0x6a]
00827CC6  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00827CCA  B9 00 01 00 00                  mov ecx, 0x100
00827CCF  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00827CD2  41 B8 53 59 50 4B               mov r8d, 0x4b505953
00827CD8  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00827CDD  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00827CE1  45 8B FC                        mov r15d, r12d
00827CE4  41 8B F4                        mov esi, r12d
00827CE7  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00827CEB  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00827CF0  45 8B EC                        mov r13d, r12d
00827CF3  0F 11 4D D0                     movups xmmword ptr [rbp - 0x30], xmm1
00827CF7  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00827CFC  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00827D00  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00827D05  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
00827D09  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
00827D0E  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00827D12  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00827D17  E8 D4 A3 35 00                  call 0x140b820f0
00827D1C  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00827D21  48 8B F8                        mov rdi, rax
00827D24  48 85 C0                        test rax, rax
00827D27  75 0A                           jne 0x140827d33
00827D29  BB 17 00 00 C0                  mov ebx, 0xc0000017
00827D2E  E9 47 03 00 00                  jmp 0x14082807a
00827D33  48 8D 54 24 44                  lea rdx, [rsp + 0x44]
00827D38  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00827D3D  E8 5A FE FF FF                  call 0x140827b9c
00827D42  85 C0                           test eax, eax
00827D44  0F 89 B0 02 00 00               jns 0x140827ffa
00827D4A  48 8D 15 DF 3F 2E 00            lea rdx, [rip + 0x2e3fdf]
00827D51  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00827D55  E8 26 2A C0 FF                  call 0x14042a780
00827D5A  48 8D 45 B0                     lea rax, [rbp - 0x50]
00827D5E  C7 45 80 30 00 00 00            mov dword ptr [rbp - 0x80], 0x30
00827D65  0F 57 C0                        xorps xmm0, xmm0
00827D68  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00827D6C  4C 8D 45 80                     lea r8, [rbp - 0x80]
00827D70  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
00827D74  BA 01 00 00 00                  mov edx, 1
00827D79  C7 45 98 40 02 00 00            mov dword ptr [rbp - 0x68], 0x240
00827D80  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00827D85  F3 0F 7F 45 A0                  movdqu xmmword ptr [rbp - 0x60], xmm0
00827D8A  E8 41 5E E8 FF                  call 0x1406adbd0
00827D8F  8B D8                           mov ebx, eax
00827D91  85 C0                           test eax, eax
00827D93  0F 88 B4 02 00 00               js 0x14082804d
00827D99  41 BE 00 10 00 00               mov r14d, 0x1000
00827D9F  41 8B D6                        mov edx, r14d
00827DA2  B9 00 01 00 00                  mov ecx, 0x100
00827DA7  41 B8 53 59 50 4B               mov r8d, 0x4b505953
00827DAD  E8 3E A3 35 00                  call 0x140b820f0
00827DB2  4C 8B F8                        mov r15, rax
00827DB5  48 85 C0                        test rax, rax
00827DB8  0F 84 35 02 00 00               je 0x140827ff3
00827DBE  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00827DC3  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
00827DC8  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00827DCD  45 33 C9                        xor r9d, r9d
00827DD0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00827DD5  45 8B C6                        mov r8d, r14d
00827DD8  49 8B D7                        mov rdx, r15
00827DDB  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00827DE0  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
00827DE5  E8 C6 7C E8 FF                  call 0x1406afab0
00827DEA  8B D8                           mov ebx, eax
00827DEC  3D 05 01 00 00                  cmp eax, 0x105
00827DF1  75 13                           jne 0x140827e06
00827DF3  33 D2                           xor edx, edx
00827DF5  49 8B CF                        mov rcx, r15
00827DF8  E8 73 AA 35 00                  call 0x140b82870
00827DFD  41 81 C6 00 10 00 00            add r14d, 0x1000
00827E04  EB 99                           jmp 0x140827d9f
00827E06  B9 00 00 00 80                  mov ecx, 0x80000000
00827E0B  03 C1                           add eax, ecx
00827E0D  85 C1                           test ecx, eax
00827E0F  75 0C                           jne 0x140827e1d
00827E11  81 FB 1A 00 00 80               cmp ebx, 0x8000001a
00827E17  0F 85 30 02 00 00               jne 0x14082804d
00827E1D  66 45 39 27                     cmp word ptr [r15], r12w
00827E21  0F 84 C5 01 00 00               je 0x140827fec
00827E27  44 8B 64 24 44                  mov r12d, dword ptr [rsp + 0x44]
00827E2C  49 8D 5F 08                     lea rbx, [r15 + 8]
00827E30  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00827E34  48 8B 0B                        mov rcx, qword ptr [rbx]
00827E37  E8 34 06 00 00                  call 0x140828470
00827E3C  45 33 C0                        xor r8d, r8d
00827E3F  84 C0                           test al, al
00827E41  0F 84 5C 01 00 00               je 0x140827fa3
00827E47  4C 8B 0B                        mov r9, qword ptr [rbx]
00827E4A  BA 6A 00 00 00                  mov edx, 0x6a
00827E4F  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00827E54  48 8B CF                        mov rcx, rdi
00827E57  4C 8D 05 E2 3E 2E 00            lea r8, [rip + 0x2e3ee2]
00827E5E  E8 DD 7C BE FF                  call 0x14040fb40
00827E63  33 C0                           xor eax, eax
00827E65  C7 44 24 28 18 00 00 00         mov dword ptr [rsp + 0x28], 0x18
00827E6D  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00827E71  0F 57 C0                        xorps xmm0, xmm0
00827E74  48 8D 45 D0                     lea rax, [rbp - 0x30]
00827E78  45 33 C9                        xor r9d, r9d
00827E7B  45 33 C0                        xor r8d, r8d
00827E7E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00827E83  BA 10 00 70 00                  mov edx, 0x700010
00827E88  48 8B CF                        mov rcx, rdi
00827E8B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00827E8F  E8 A0 FB FF FF                  call 0x140827a34
00827E94  45 33 C0                        xor r8d, r8d
00827E97  85 C0                           test eax, eax
00827E99  78 0A                           js 0x140827ea5
00827E9B  83 7D D4 02                     cmp dword ptr [rbp - 0x2c], 2
00827E9F  0F 84 FE 00 00 00               je 0x140827fa3
00827EA5  0F 57 C0                        xorps xmm0, xmm0
00827EA8  4C 89 45 C4                     mov qword ptr [rbp - 0x3c], r8
00827EAC  45 0F B6 F0                     movzx r14d, r8b
00827EB0  48 8D 45 E8                     lea rax, [rbp - 0x18]
00827EB4  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00827EB8  C7 44 24 28 20 00 00 00         mov dword ptr [rsp + 0x28], 0x20
00827EC0  41 B9 0C 00 00 00               mov r9d, 0xc
00827EC6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00827ECB  BA 00 14 2D 00                  mov edx, 0x2d1400
00827ED0  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
00827ED7  48 8B CF                        mov rcx, rdi
00827EDA  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00827EDE  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00827EE2  E8 4D FB FF FF                  call 0x140827a34
00827EE7  45 33 C0                        xor r8d, r8d
00827EEA  85 C0                           test eax, eax
00827EEC  78 15                           js 0x140827f03
00827EEE  8A 45 00                        mov al, byte ptr [rbp]
00827EF1  3C 0F                           cmp al, 0xf
00827EF3  0F 84 AA 00 00 00               je 0x140827fa3
00827EF9  3C 10                           cmp al, 0x10
00827EFB  41 8D 40 01                     lea eax, [r8 + 1]
00827EFF  44 0F 44 F0                     cmove r14d, eax
00827F03  48 85 F6                        test rsi, rsi
00827F06  74 10                           je 0x140827f18
00827F08  33 D2                           xor edx, edx
00827F0A  48 8B CE                        mov rcx, rsi
00827F0D  E8 5E A9 35 00                  call 0x140b82870
00827F12  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
00827F18  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00827F1D  48 8B CF                        mov rcx, rdi
00827F20  E8 0F FA FF FF                  call 0x140827934
00827F25  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00827F2A  45 33 C0                        xor r8d, r8d
00827F2D  45 8D 48 01                     lea r9d, [r8 + 1]
00827F31  85 C0                           test eax, eax
00827F33  78 74                           js 0x140827fa9
00827F35  44 39 0E                        cmp dword ptr [rsi], r9d
00827F38  75 6F                           jne 0x140827fa9
00827F3A  8B 46 04                        mov eax, dword ptr [rsi + 4]
00827F3D  85 C0                           test eax, eax
00827F3F  74 68                           je 0x140827fa9
00827F41  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
00827F45  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00827F49  8B D0                           mov edx, eax
00827F4B  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00827F4F  48 2B 05 5A 2C 7F FF            sub rax, qword ptr [rip - 0x80d3a6]
00827F56  75 0B                           jne 0x140827f63
00827F58  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00827F5C  48 2B 05 55 2C 7F FF            sub rax, qword ptr [rip - 0x80d3ab]
00827F63  48 85 C0                        test rax, rax
00827F66  75 24                           jne 0x140827f8c
00827F68  45 85 ED                        test r13d, r13d
00827F6B  74 09                           je 0x140827f76
00827F6D  85 FF                           test edi, edi
00827F6F  75 10                           jne 0x140827f81
00827F71  45 84 F6                        test r14b, r14b
00827F74  74 0B                           je 0x140827f81
00827F76  48 8B 03                        mov rax, qword ptr [rbx]
00827F79  44 8B 21                        mov r12d, dword ptr [rcx]
00827F7C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00827F81  45 03 E9                        add r13d, r9d
00827F84  45 84 F6                        test r14b, r14b
00827F87  74 03                           je 0x140827f8c
00827F89  41 03 F9                        add edi, r9d
00827F8C  48 81 C1 90 00 00 00            add rcx, 0x90
00827F93  49 2B D1                        sub rdx, r9
00827F96  75 B3                           jne 0x140827f4b
00827F98  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00827F9C  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00827FA1  EB 06                           jmp 0x140827fa9
00827FA3  41 B9 01 00 00 00               mov r9d, 1
00827FA9  48 83 C3 20                     add rbx, 0x20
00827FAD  66 44 39 43 F8                  cmp word ptr [rbx - 8], r8w
00827FB2  0F 85 78 FE FF FF               jne 0x140827e30
00827FB8  45 85 ED                        test r13d, r13d
00827FBB  74 2F                           je 0x140827fec
00827FBD  45 3B E9                        cmp r13d, r9d
00827FC0  76 3F                           jbe 0x140828001
00827FC2  44 39 4C 24 40                  cmp dword ptr [rsp + 0x40], r9d
00827FC7  74 38                           je 0x140828001
00827FC9  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00827FCD  48 8B D7                        mov rdx, rdi
00827FD0  E8 EB 00 00 00                  call 0x1408280c0
00827FD5  8B D8                           mov ebx, eax
00827FD7  85 C0                           test eax, eax
00827FD9  79 07                           jns 0x140827fe2
00827FDB  BB 51 04 00 C0                  mov ebx, 0xc0000451
00827FE0  EB 6B                           jmp 0x14082804d
00827FE2  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00827FE7  48 89 38                        mov qword ptr [rax], rdi
00827FEA  EB 70                           jmp 0x14082805c
00827FEC  BB 52 04 00 C0                  mov ebx, 0xc0000452
00827FF1  EB 5A                           jmp 0x14082804d
00827FF3  BB 17 00 00 C0                  mov ebx, 0xc0000017
00827FF8  EB 53                           jmp 0x14082804d
00827FFA  44 8B 64 24 44                  mov r12d, dword ptr [rsp + 0x44]
00827FFF  EB 0A                           jmp 0x14082800b
00828001  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00828006  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0082800B  F7 5C 24 48                     neg dword ptr [rsp + 0x48]
0082800F  BA 6A 00 00 00                  mov edx, 0x6a
00828014  48 8B CF                        mov rcx, rdi
00828017  1B C0                           sbb eax, eax
00828019  41 23 C4                        and eax, r12d
0082801C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00828020  48 85 DB                        test rbx, rbx
00828023  74 11                           je 0x140828036
00828025  4C 8B CB                        mov r9, rbx
00828028  4C 8D 05 11 3D 2E 00            lea r8, [rip + 0x2e3d11]
0082802F  E8 0C 7B BE FF                  call 0x14040fb40
00828034  EB 11                           jmp 0x140828047
00828036  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
0082803B  4C 8D 05 FE 08 2E 00            lea r8, [rip + 0x2e08fe]
00828042  E8 F9 7A BE FF                  call 0x14040fb40
00828047  8B D8                           mov ebx, eax
00828049  85 C0                           test eax, eax
0082804B  79 0C                           jns 0x140828059
0082804D  33 D2                           xor edx, edx
0082804F  48 8B CF                        mov rcx, rdi
00828052  E8 19 A8 35 00                  call 0x140b82870
00828057  EB 03                           jmp 0x14082805c
00828059  49 89 3E                        mov qword ptr [r14], rdi
0082805C  48 85 F6                        test rsi, rsi
0082805F  74 0A                           je 0x14082806b
00828061  33 D2                           xor edx, edx
00828063  48 8B CE                        mov rcx, rsi
00828066  E8 05 A8 35 00                  call 0x140b82870
0082806B  4D 85 FF                        test r15, r15
0082806E  74 0A                           je 0x14082807a
00828070  33 D2                           xor edx, edx
00828072  49 8B CF                        mov rcx, r15
00828075  E8 F6 A7 35 00                  call 0x140b82870
0082807A  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0082807F  48 85 C9                        test rcx, rcx
00828082  74 05                           je 0x140828089
00828084  E8 27 52 E8 FF                  call 0x1406ad2b0
00828089  8B C3                           mov eax, ebx
0082808B  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
0082808F  48 33 CC                        xor rcx, rsp
00828092  E8 A9 45 E8 FF                  call 0x1406ac640
00828097  4C 8D 9C 24 10 01 00 00         lea r11, [rsp + 0x110]
0082809F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008280A3  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
008280A7  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
008280AB  49 8B E3                        mov rsp, r11
008280AE  41 5F                           pop r15
008280B0  41 5E                           pop r14
008280B2  41 5D                           pop r13
008280B4  41 5C                           pop r12
008280B6  5D                              pop rbp
008280B7  C3                              ret
008280B8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SiGetEfiSystemDevice(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 6171310)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 56 + 8) = result;
    v_r12 = 0;
    v_stack_mD0 = a3;
    result = 0;
    v_stack_mF0 = a1;
    *(unsigned __int64 *)(v_rsp - 56 - 32) = 0;
    v_stack_mEC = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 96) = 0;
    *(unsigned int *)(v_rsp - 56 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 64) = 0;
    *(unsigned int *)(v_rsp - 56 - 56) = 0;
    v_stack_mC8 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 8) = v_xmm0;
    v_stack_mE0 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 48) = v_xmm1;
    v_stack_mD8 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 80) = v_xmm0;
    v_stack_mE8 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 128) = v_xmm0;
    v_stack_mF4 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm0;
    v_stack_mF8 = 0;
    result = ExAllocatePool2(256, result + 106, (unsigned int)(0x4B505953ULL), a4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_00827D33;
    goto loc_0082807A;
loc_00827D33:
    result = SiDisambiguateSystemDevice(v_stack_mE8, v_stack_mF4, (unsigned int)(0x4B505953ULL), a4);
    if (!sign_flag) goto loc_00827FFA;
    result = RtlInitUnicodeString(v_rsp - 56 - 80, v_rip + 3031007, (unsigned int)(0x4B505953ULL), a4);
    *(unsigned int *)(v_rsp - 56 - 128) = 48;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_rsp - 56 - 80;
    *(unsigned __int64 *)(v_rsp - 56 - 120) = 0;
    *(unsigned int *)(v_rsp - 56 - 104) = 576;
    *(unsigned __int64 *)(v_rsp - 56 - 96) = v_xmm0;
    result = ZwOpenDirectoryObject(v_stack_mC8, 1, v_rsp - 56 - 128, a4);
    if (sign_flag) goto loc_0082804D;
loc_00827D9F:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)(0x4B505953ULL), a4);
    if (result == 0) goto loc_00827FF3;
    v_stack_m108 = 0;
    a4 = 0;
    v_stack_m110 = v_stack_mEC;
    v_stack_m118 = 1;
    v_stack_mEC = 0;
    result = ZwQueryDirectoryObject(v_stack_mC8, result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a4);
    if (((unsigned int)(result)) != 261) goto loc_00827E06;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a4);
    v_r14 = (unsigned int)(((unsigned int)(0x1000ULL)) + (0x1000ULL));
    goto loc_00827D9F;
loc_00827E06:
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00827E1D;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0x8000001AULL) goto loc_0082804D;
loc_00827E1D:
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00827FEC;
loc_00827E30:
    result = SiIsValidDiskDevice(*(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 8 + 16), (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a4);
    a3 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00827FA3;
    v_stack_m118 = 0;
    result = RtlStringCbPrintfW(result, 106, v_rip + 3030754, *(unsigned __int64 *)(result + 8));
    result = 0;
    v_stack_m110 = 24;
    *(unsigned __int64 *)(v_rsp - 56 - 32) = 0;
    a4 = 0;
    a3 = 0;
    v_stack_m118 = v_rsp - 56 - 48;
    *(unsigned __int64 *)(v_rsp - 56 - 48) = v_xmm0;
    result = SiIssueSynchronousIoctl(0, (unsigned int)(0x700010ULL), a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00827EA5;
    if ((*(unsigned int *)(v_rsp - 56 - 44)) == 2) goto loc_00827FA3;
loc_00827EA5:
    *(unsigned __int64 *)(v_rsp - 56 - 60) = 0;
    v_stack_m110 = 32;
    v_stack_m118 = v_rsp - 56 - 24;
    *(unsigned int *)(v_rsp - 56 - 64) = 1;
    *(unsigned __int64 *)(v_rsp - 56 - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 8) = v_xmm0;
    result = SiIssueSynchronousIoctl(result, (unsigned int)(0x2D1400ULL), v_rsp - 56 - 64, 12);
    a3 = 0;
    if (sign_flag) goto loc_00827F03;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 56))) == 15) goto loc_00827FA3;
    v_r14 = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 56))) == 16) { v_r14 = (unsigned int)(a3 + 1); }
loc_00827F03:
    result = a3 + 1;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, 12);
    }
    result = SiGetDriveLayoutInformation(result, v_stack_mE0, a3, 12);
    a3 = 0;
    if (sign_flag) goto loc_00827FA9;
    if ((*(unsigned int *)(v_stack_mE0)) != ((unsigned int)(a3 + 1))) goto loc_00827FA9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 4))) == 0) goto loc_00827FA9;
loc_00827F4B:
    result = (*(unsigned __int64 *)(v_stack_mE0 + 72 + 8)) - (*(unsigned __int64 *)(v_rip - 8442790));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_stack_mE0 + 72 + 16);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8442795));
    }
    if (result != 0) goto loc_00827F8C;
    if (0 == 0) goto loc_00827F76;
    if ((unsigned int)((unsigned int)(v_stack_mF8)) != 0) goto loc_00827F81;
    v_r12 = (unsigned int)(v_stack_mF4);
    if ((unsigned __int8)(v_r14) != 0) {
        result = *(unsigned __int64 *)(result + 8);
        v_r12 = *(unsigned int *)(v_stack_mE0 + 72);
        v_stack_mD8 = result;
    }
    v_r13 = (unsigned int)((0) + ((unsigned int)(a3 + 1)));
    v_rdi = (unsigned int)(v_stack_mF8);
    if ((unsigned __int8)(v_r14) != 0) {
        v_rdi = (unsigned int)(((unsigned int)(v_stack_mF8)) + ((unsigned int)(a3 + 1)));
    }
    a1 = (v_stack_mE0 + 72) + (144);
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 4))))) - (a3 + 1);
    if (condition_is_not_equal) goto loc_00827F4B;
    v_stack_mF8 = (unsigned int)(v_rdi);
    goto loc_00827FA9;
loc_00827FA3:
loc_00827FA9:
    v_rbx = (result + 8) + (32);
    if ((*(unsigned __int16 *)(v_rbx - 8)) != 0) goto loc_00827E30;
    if ((unsigned int)(v_r13) == 0) goto loc_00827FEC;
    if (((unsigned int)(v_r13)) <= 1) goto loc_00828001;
    if (v_stack_mF8 == 1) goto loc_00828001;
    result = SiGetEspFromFirmware((unsigned int)(v_stack_mF0), v_stack_mC0, a3, 1);
    if (!sign_flag) goto loc_00827FE2;
    goto loc_0082804D;
loc_00827FE2:
    *(unsigned __int64 *)(v_stack_mD0) = v_stack_mC0;
    goto loc_0082805C;
loc_00827FEC:
    goto loc_0082804D;
loc_00827FF3:
    goto loc_0082804D;
loc_00827FFA:
    goto loc_0082800B;
loc_00828001:
loc_0082800B:
    result = (unsigned int)((v_stack_mD0) & ((unsigned int)((unsigned int)(v_stack_mF4))));
    v_stack_m118 = (unsigned int)(result);
    if (v_stack_mD8 == 0) goto loc_00828036;
    result = RtlStringCbPrintfW(v_stack_mC0, 106, v_rip + 3030289, v_stack_mD8);
    goto loc_00828047;
loc_00828036:
    result = RtlStringCbPrintfW(v_stack_mC0, 106, v_rip + 3016958, (unsigned int)(v_stack_mE8));
loc_00828047:
    if (!sign_flag) goto loc_00828059;
loc_0082804D:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mC0, a2, v_rip + 3016958, (unsigned int)(v_stack_mE8));
    goto loc_0082805C;
loc_00828059:
    *(unsigned __int64 *)(v_stack_mD0) = v_stack_mC0;
loc_0082805C:
    if (v_stack_mE0 != 0) {
        a2 = 0;
        a1 = v_stack_mE0;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3016958, (unsigned int)(v_stack_mE8));
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3016958, (unsigned int)(v_stack_mE8));
    }
    if (v_stack_mC8 != 0) {
        result = ZwClose(v_stack_mC8, a2, v_rip + 3016958, (unsigned int)(v_stack_mE8));
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 56 + 8)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 3016958, (unsigned int)(v_stack_mE8));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SiGetEfiSystemDevice(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint8_t v_stack_m118;
    uint64_t v_stack_m28;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x5E2AAE)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x38 + 0x8) = result;
    local_r12 = 0;
    v_stack_mD0 = Arg3;
    result = 0;
    v_stack_mF0 = Arg1;
    *(uint64_t *)(local_rsp - 0x38 - 0x20) = 0;
    v_stack_mEC = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x60) = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x40) = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x38) = 0;
    v_stack_mC8 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x18) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x8) = v_xmm0;
    v_stack_mE0 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x30) = v_xmm1;
    v_stack_mD8 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x50) = v_xmm0;
    v_stack_mE8 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x80) = v_xmm0;
    v_stack_mF4 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm0;
    v_stack_mF8 = 0;
    result = ExAllocatePool2(256, result + 106, (uint32_t)(0x4B505953ULL), Arg4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_00827D33;
    goto loc_0082807A;
loc_00827D33:
    result = SiDisambiguateSystemDevice(v_stack_mE8, v_stack_mF4, (uint32_t)(0x4B505953ULL), Arg4);
    if (!sign_flag) goto loc_00827FFA;
    result = RtlInitUnicodeString(local_rsp - 56 - 80, v_rip + 3031007, (uint32_t)(0x4B505953ULL), Arg4);
    *(uint32_t *)(local_rsp - 0x38 - 0x80) = 48;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = local_rsp - 56 - 80;
    *(uint64_t *)(local_rsp - 0x38 - 0x78) = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x68) = 576;
    *(uint64_t *)(local_rsp - 0x38 - 0x60) = v_xmm0;
    result = ZwOpenDirectoryObject(v_stack_mC8, 1, local_rsp - 56 - 128, Arg4);
    if (sign_flag) goto loc_0082804D;
loc_00827D9F:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)(0x4B505953ULL), Arg4);
    if (result == 0) goto loc_00827FF3;
    v_stack_m108 = 0;
    Arg4 = 0;
    v_stack_m110 = v_stack_mEC;
    v_stack_m118 = 1;
    v_stack_mEC = 0;
    result = ZwQueryDirectoryObject(v_stack_mC8, result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), Arg4);
    if (((uint32_t)(result)) != 261) goto loc_00827E06;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), Arg4);
    local_r14 = (uint32_t)(((uint32_t)(0x1000ULL)) + (0x1000ULL));
    goto loc_00827D9F;
loc_00827E06:
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00827E1D;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0x8000001AULL) goto loc_0082804D;
loc_00827E1D:
    if ((*(uint16_t *)(result)) == 0) goto loc_00827FEC;
loc_00827E30:
    result = SiIsValidDiskDevice(*(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x8 + 0x10), (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), Arg4);
    Arg3 = 0;
    if ((uint8_t)(result) == 0) goto loc_00827FA3;
    v_stack_m118 = 0;
    result = RtlStringCbPrintfW(result, 106, v_rip + 3030754, *(uint64_t *)(result + 0x8));
    result = 0;
    v_stack_m110 = 24;
    *(uint64_t *)(local_rsp - 0x38 - 0x20) = 0;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m118 = local_rsp - 56 - 48;
    *(uint64_t *)(local_rsp - 0x38 - 0x30) = v_xmm0;
    result = SiIssueSynchronousIoctl(0, (uint32_t)(0x700010ULL), Arg3, Arg4);
    Arg3 = 0;
    if (sign_flag) goto loc_00827EA5;
    if ((*(uint32_t *)(local_rsp - 0x38 - 0x2C)) == 2) goto loc_00827FA3;
loc_00827EA5:
    *(uint64_t *)(local_rsp - 0x38 - 0x3C) = 0;
    v_stack_m110 = 32;
    v_stack_m118 = local_rsp - 56 - 24;
    *(uint32_t *)(local_rsp - 0x38 - 0x40) = 1;
    *(uint64_t *)(local_rsp - 0x38 - 0x18) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x8) = v_xmm0;
    result = SiIssueSynchronousIoctl(result, (uint32_t)(0x2D1400ULL), local_rsp - 56 - 64, 12);
    Arg3 = 0;
    if (sign_flag) goto loc_00827F03;
    if (((uint8_t)(*(uint8_t *)(local_rsp - 0x38))) == 15) goto loc_00827FA3;
    local_r14 = 0;
    if (((uint8_t)(*(uint8_t *)(local_rsp - 0x38))) == 16) { local_r14 = (uint32_t)(Arg3 + 1); }
loc_00827F03:
    result = Arg3 + 1;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, 12);
    }
    result = SiGetDriveLayoutInformation(result, v_stack_mE0, Arg3, 12);
    Arg3 = 0;
    if (sign_flag) goto loc_00827FA9;
    if ((*(uint32_t *)(v_stack_mE0)) != ((uint32_t)(Arg3 + 1))) goto loc_00827FA9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x4))) == 0) goto loc_00827FA9;
loc_00827F4B:
    result = (*(uint64_t *)(v_stack_mE0 + 0x48 + 0x8)) - (*(uint64_t *)(v_rip - 0x80D3A6));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(v_stack_mE0 + 0x48 + 0x10);
        result = (result) - (*(uint64_t *)(v_rip - 0x80D3AB));
    }
    if (result != 0) goto loc_00827F8C;
    if (0 == 0) goto loc_00827F76;
    if ((uint32_t)((uint32_t)(v_stack_mF8)) != 0) goto loc_00827F81;
    local_r12 = (uint32_t)(v_stack_mF4);
    if ((uint8_t)(local_r14) != 0) {
        result = *(uint64_t *)(result + 0x8);
        local_r12 = *(uint32_t *)(v_stack_mE0 + 0x48);
        v_stack_mD8 = result;
    }
    local_r13 = (uint32_t)((0) + ((uint32_t)(Arg3 + 1)));
    local_rdi = (uint32_t)(v_stack_mF8);
    if ((uint8_t)(local_r14) != 0) {
        local_rdi = (uint32_t)(((uint32_t)(v_stack_mF8)) + ((uint32_t)(Arg3 + 1)));
    }
    Arg1 = (v_stack_mE0 + 72) + (144);
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x4))))) - (Arg3 + 1);
    if (condition_is_not_equal) goto loc_00827F4B;
    v_stack_mF8 = (uint32_t)(local_rdi);
    goto loc_00827FA9;
loc_00827FA3:
loc_00827FA9:
    local_rbx = (result + 8) + (32);
    if ((*(uint16_t *)(local_rbx - 0x8)) != 0) goto loc_00827E30;
    if ((uint32_t)(local_r13) == 0) goto loc_00827FEC;
    if (((uint32_t)(local_r13)) <= 1) goto loc_00828001;
    if (v_stack_mF8 == 1) goto loc_00828001;
    result = SiGetEspFromFirmware((uint32_t)(v_stack_mF0), v_stack_mC0, Arg3, 1);
    if (!sign_flag) goto loc_00827FE2;
    goto loc_0082804D;
loc_00827FE2:
    *(uint64_t *)(v_stack_mD0) = v_stack_mC0;
    goto loc_0082805C;
loc_00827FEC:
    goto loc_0082804D;
loc_00827FF3:
    goto loc_0082804D;
loc_00827FFA:
    goto loc_0082800B;
loc_00828001:
loc_0082800B:
    result = (uint32_t)((v_stack_mD0) & ((uint32_t)((uint32_t)(v_stack_mF4))));
    v_stack_m118 = (uint32_t)(result);
    if (v_stack_mD8 == 0) goto loc_00828036;
    result = RtlStringCbPrintfW(v_stack_mC0, 106, v_rip + 3030289, v_stack_mD8);
    goto loc_00828047;
loc_00828036:
    result = RtlStringCbPrintfW(v_stack_mC0, 106, v_rip + 3016958, (uint32_t)(v_stack_mE8));
loc_00828047:
    if (!sign_flag) goto loc_00828059;
loc_0082804D:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mC0, Arg2, v_rip + 3016958, (uint32_t)(v_stack_mE8));
    goto loc_0082805C;
loc_00828059:
    *(uint64_t *)(v_stack_mD0) = v_stack_mC0;
loc_0082805C:
    if (v_stack_mE0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mE0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3016958, (uint32_t)(v_stack_mE8));
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3016958, (uint32_t)(v_stack_mE8));
    }
    if (v_stack_mC8 != 0) {
        result = ZwClose(v_stack_mC8, Arg2, v_rip + 3016958, (uint32_t)(v_stack_mE8));
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x38 + 0x8)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 3016958, (uint32_t)(v_stack_mE8));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00827C68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
