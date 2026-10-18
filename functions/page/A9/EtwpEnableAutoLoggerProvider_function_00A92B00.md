# EtwpEnableAutoLoggerProvider

- RVA: `0x00A92B00`–`0x00A9323F` (길이 `1,855` bytes)
- VA: `0x0000000140A92B00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B946C`
- 디코드: `431`개 명령, `1,855/1,855` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00A92BA4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A92BB8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A92BC7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A92C0D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A92C38` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x00A92C4F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A92C83` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00A92CCE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A92CF3` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x00A92D03` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A92D37` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00A92EC8` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00A92F70` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00A92FFF` → [EtwpGetAutoLoggerProviderFilter](EtwpGetAutoLoggerProviderFilter_function_00A93248.md) (function, `0x00A93248`)
- `0x00A9300C` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00A9312A` → [EtwpEnableTrace](../A5/EtwpEnableTrace_function_00A5C8EC.md) (function, `0x00A5C8EC`)
- `0x00A93135` → [RtlNtStatusToDosError](../92/RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00A93164` → [RtlWriteRegistryValue](../A6/RtlWriteRegistryValue_function_00A6C620.md) (function, `0x00A6C620`)
- `0x00A93172` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A93181` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A9318F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A9319E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A931AE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A931BE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A931CE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A931DE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A931EA` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9320C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A93225` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpEnumerateKeyProviders](../AB/EtwpEnumerateKeyProviders_function_00AB029C.md) at `0x00AB03B2`

### Static image references
- `0x00A92B1C` → RVA `0x00E0A740` (`.data`; read)
- `0x00A92C2B` → RVA `0x00B07420` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A92D44` → RVA `0x007BEA40` (`EtwpQueryRegistryCallback`; read)
- `0x00A92D79` → RVA `0x00AFBEF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A92DBE` → RVA `0x00B06C60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A92DE5` → RVA `0x00B07E00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A92E0C` → RVA `0x00B07DE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A92E33` → RVA `0x00B07D40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A92E5A` → RVA `0x00B07D20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A93020` → RVA `0x0001C1E8` (`.rdata`; read)
- `0x00A9302D` → RVA `0x0001C1F0` (`.rdata`; read)
- `0x00A93039` → RVA `0x000113A0` (`.rdata`; read)
- `0x00A93046` → RVA `0x000113A8` (`.rdata`; read)
- `0x00A93056` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00A93151` → RVA `0x00AFF2C0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00A92BA4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A92BB8` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A92BC7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A92C0D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A92C38` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x00A92C4F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A92C83` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00A92CCE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A92CF3` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x00A92D03` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A92D37` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00A93172` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A93181` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A9318F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A9319E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A931AE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A931BE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A931CE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A931DE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A9320C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A93225` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A92B00  40 55                           push rbp
00A92B02  53                              push rbx
00A92B03  56                              push rsi
00A92B04  57                              push rdi
00A92B05  41 54                           push r12
00A92B07  41 55                           push r13
00A92B09  41 56                           push r14
00A92B0B  41 57                           push r15
00A92B0D  48 8D AC 24 48 F9 FF FF         lea rbp, [rsp - 0x6b8]
00A92B15  48 81 EC C8 07 00 00            sub rsp, 0x7c8
00A92B1C  48 8B 05 1D 7C 37 00            mov rax, qword ptr [rip + 0x377c1d]
00A92B23  48 33 C4                        xor rax, rsp
00A92B26  48 89 85 A0 06 00 00            mov qword ptr [rbp + 0x6a0], rax
00A92B2D  48 8B 85 20 07 00 00            mov rax, qword ptr [rbp + 0x720]
00A92B34  33 DB                           xor ebx, ebx
00A92B36  0F 57 C0                        xorps xmm0, xmm0
00A92B39  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00A92B3D  33 C0                           xor eax, eax
00A92B3F  89 55 C8                        mov dword ptr [rbp - 0x38], edx
00A92B42  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
00A92B46  49 8B D0                        mov rdx, r8
00A92B49  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00A92B4D  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00A92B51  89 45 28                        mov dword ptr [rbp + 0x28], eax
00A92B54  4D 8B E9                        mov r13, r9
00A92B57  4D 8B F0                        mov r14, r8
00A92B5A  89 5D 80                        mov dword ptr [rbp - 0x80], ebx
00A92B5D  8B F3                           mov esi, ebx
00A92B5F  89 5D 8C                        mov dword ptr [rbp - 0x74], ebx
00A92B62  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
00A92B66  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
00A92B69  89 5D 88                        mov dword ptr [rbp - 0x78], ebx
00A92B6C  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
00A92B70  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
00A92B74  89 5D 90                        mov dword ptr [rbp - 0x70], ebx
00A92B77  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
00A92B7B  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00A92B7F  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00A92B83  48 89 5D D8                     mov qword ptr [rbp - 0x28], rbx
00A92B87  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
00A92B8B  89 5D A8                        mov dword ptr [rbp - 0x58], ebx
00A92B8E  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00A92B92  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
00A92B96  89 5D A4                        mov dword ptr [rbp - 0x5c], ebx
00A92B99  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00A92B9D  89 5D A0                        mov dword ptr [rbp - 0x60], ebx
00A92BA0  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
00A92BA4  E8 D7 7B 99 FF                  call 0x14042a780
00A92BA9  33 D2                           xor edx, edx
00A92BAB  48 8D 8D 00 02 00 00            lea rcx, [rbp + 0x200]
00A92BB2  41 B8 98 04 00 00               mov r8d, 0x498
00A92BB8  E8 83 40 C3 FF                  call 0x1406c6c40
00A92BBD  33 D2                           xor edx, edx
00A92BBF  44 8D 43 40                     lea r8d, [rbx + 0x40]
00A92BC3  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00A92BC7  E8 74 40 C3 FF                  call 0x1406c6c40
00A92BCC  0F 57 C0                        xorps xmm0, xmm0
00A92BCF  48 83 CF FF                     or rdi, 0xffffffffffffffff
00A92BD3  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
00A92BD7  48 8B C7                        mov rax, rdi
00A92BDA  48 FF C0                        inc rax
00A92BDD  66 41 39 5C 45 00               cmp word ptr [r13 + rax*2], bx
00A92BE3  75 F5                           jne 0x140a92bda
00A92BE5  48 8B CF                        mov rcx, rdi
00A92BE8  48 FF C1                        inc rcx
00A92BEB  66 41 39 1C 4E                  cmp word ptr [r14 + rcx*2], bx
00A92BF0  75 F6                           jne 0x140a92be8
00A92BF2  48 03 C1                        add rax, rcx
00A92BF5  41 B8 45 74 77 50               mov r8d, 0x50777445
00A92BFB  B9 00 01 00 00                  mov ecx, 0x100
00A92C00  48 8D 04 45 04 00 00 00         lea rax, [rax*2 + 4]
00A92C08  8B D0                           mov edx, eax
00A92C0A  44 8B E0                        mov r12d, eax
00A92C0D  E8 DE F4 0E 00                  call 0x140b820f0
00A92C12  4C 8B F8                        mov r15, rax
00A92C15  BB 04 00 00 00                  mov ebx, 4
00A92C1A  48 85 C0                        test rax, rax
00A92C1D  0F 84 46 05 00 00               je 0x140a93169
00A92C23  4D 8B CD                        mov r9, r13
00A92C26  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A92C2B  4C 8D 05 EE 47 07 00            lea r8, [rip + 0x747ee]
00A92C32  41 8B D4                        mov edx, r12d
00A92C35  48 8B C8                        mov rcx, rax
00A92C38  E8 03 CF 97 FF                  call 0x14040fb40
00A92C3D  45 33 ED                        xor r13d, r13d
00A92C40  85 C0                           test eax, eax
00A92C42  0F 85 21 05 00 00               jne 0x140a93169
00A92C48  49 8B D7                        mov rdx, r15
00A92C4B  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00A92C4F  E8 2C 7B 99 FF                  call 0x14042a780
00A92C54  48 8D 45 30                     lea rax, [rbp + 0x30]
00A92C58  C7 45 00 30 00 00 00            mov dword ptr [rbp], 0x30
00A92C5F  0F 57 C0                        xorps xmm0, xmm0
00A92C62  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00A92C66  4C 8D 45 00                     lea r8, [rbp]
00A92C6A  4C 89 6D 08                     mov qword ptr [rbp + 8], r13
00A92C6E  BA 1F 00 02 00                  mov edx, 0x2001f
00A92C73  C7 45 18 40 02 00 00            mov dword ptr [rbp + 0x18], 0x240
00A92C7A  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A92C7E  F3 0F 7F 45 20                  movdqu xmmword ptr [rbp + 0x20], xmm0
00A92C83  E8 88 A6 C1 FF                  call 0x1406ad310
00A92C88  85 C0                           test eax, eax
00A92C8A  0F 88 D9 04 00 00               js 0x140a93169
00A92C90  4C 8B 65 B0                     mov r12, qword ptr [rbp - 0x50]
00A92C94  4D 85 E4                        test r12, r12
00A92C97  0F 84 A7 00 00 00               je 0x140a92d44
00A92C9D  48 8B C7                        mov rax, rdi
00A92CA0  48 FF C0                        inc rax
00A92CA3  66 45 39 2C 44                  cmp word ptr [r12 + rax*2], r13w
00A92CA8  75 F6                           jne 0x140a92ca0
00A92CAA  48 FF C7                        inc rdi
00A92CAD  66 45 39 2C 7E                  cmp word ptr [r14 + rdi*2], r13w
00A92CB2  75 F6                           jne 0x140a92caa
00A92CB4  48 03 C7                        add rax, rdi
00A92CB7  41 B8 45 74 77 50               mov r8d, 0x50777445
00A92CBD  B9 00 01 00 00                  mov ecx, 0x100
00A92CC2  48 8D 04 45 04 00 00 00         lea rax, [rax*2 + 4]
00A92CCA  8B D0                           mov edx, eax
00A92CCC  8B F8                           mov edi, eax
00A92CCE  E8 1D F4 0E 00                  call 0x140b820f0
00A92CD3  48 8B F0                        mov rsi, rax
00A92CD6  48 85 C0                        test rax, rax
00A92CD9  0F 84 8A 04 00 00               je 0x140a93169
00A92CDF  4D 8B CC                        mov r9, r12
00A92CE2  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A92CE7  4C 8D 05 32 47 07 00            lea r8, [rip + 0x74732]
00A92CEE  8B D7                           mov edx, edi
00A92CF0  48 8B C8                        mov rcx, rax
00A92CF3  E8 48 CE 97 FF                  call 0x14040fb40
00A92CF8  85 C0                           test eax, eax
00A92CFA  75 48                           jne 0x140a92d44
00A92CFC  48 8B D6                        mov rdx, rsi
00A92CFF  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00A92D03  E8 78 7A 99 FF                  call 0x14042a780
00A92D08  48 8D 45 30                     lea rax, [rbp + 0x30]
00A92D0C  C7 45 00 30 00 00 00            mov dword ptr [rbp], 0x30
00A92D13  0F 57 C0                        xorps xmm0, xmm0
00A92D16  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00A92D1A  4C 8D 45 00                     lea r8, [rbp]
00A92D1E  4C 89 6D 08                     mov qword ptr [rbp + 8], r13
00A92D22  BA 1F 00 02 00                  mov edx, 0x2001f
00A92D27  C7 45 18 40 02 00 00            mov dword ptr [rbp + 0x18], 0x240
00A92D2E  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00A92D32  F3 0F 7F 45 20                  movdqu xmmword ptr [rbp + 0x20], xmm0
00A92D37  E8 D4 A5 C1 FF                  call 0x1406ad310
00A92D3C  85 C0                           test eax, eax
00A92D3E  79 04                           jns 0x140a92d44
00A92D40  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
00A92D44  48 8D 15 F5 BC D2 FF            lea rdx, [rip - 0x2d430b]
00A92D4B  89 9D 20 02 00 00               mov dword ptr [rbp + 0x220], ebx
00A92D51  B9 0B 00 00 00                  mov ecx, 0xb
00A92D56  48 89 95 00 02 00 00            mov qword ptr [rbp + 0x200], rdx
00A92D5D  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00A92D64  48 89 95 38 02 00 00            mov qword ptr [rbp + 0x238], rdx
00A92D6B  48 89 85 18 02 00 00            mov qword ptr [rbp + 0x218], rax
00A92D72  4C 8D 85 00 02 00 00            lea r8, [rbp + 0x200]
00A92D79  48 8D 05 70 91 06 00            lea rax, [rip + 0x69170]
00A92D80  48 89 95 70 02 00 00            mov qword ptr [rbp + 0x270], rdx
00A92D87  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
00A92D8E  41 BE 00 00 00 40               mov r14d, 0x40000000
00A92D94  48 8D 45 80                     lea rax, [rbp - 0x80]
00A92D98  48 89 95 A8 02 00 00            mov qword ptr [rbp + 0x2a8], rdx
00A92D9F  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
00A92DA6  45 33 C9                        xor r9d, r9d
00A92DA9  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00A92DB0  48 89 95 E0 02 00 00            mov qword ptr [rbp + 0x2e0], rdx
00A92DB7  48 89 85 50 02 00 00            mov qword ptr [rbp + 0x250], rax
00A92DBE  48 8D 05 9B 3E 07 00            lea rax, [rip + 0x73e9b]
00A92DC5  48 89 85 48 02 00 00            mov qword ptr [rbp + 0x248], rax
00A92DCC  48 8D 45 88                     lea rax, [rbp - 0x78]
00A92DD0  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
00A92DD7  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
00A92DDE  48 89 85 88 02 00 00            mov qword ptr [rbp + 0x288], rax
00A92DE5  48 8D 05 14 50 07 00            lea rax, [rip + 0x75014]
00A92DEC  48 89 85 80 02 00 00            mov qword ptr [rbp + 0x280], rax
00A92DF3  48 8D 45 8C                     lea rax, [rbp - 0x74]
00A92DF7  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
00A92DFE  48 8D 85 E0 00 00 00            lea rax, [rbp + 0xe0]
00A92E05  48 89 85 C0 02 00 00            mov qword ptr [rbp + 0x2c0], rax
00A92E0C  48 8D 05 CD 4F 07 00            lea rax, [rip + 0x74fcd]
00A92E13  48 89 85 B8 02 00 00            mov qword ptr [rbp + 0x2b8], rax
00A92E1A  48 8D 45 84                     lea rax, [rbp - 0x7c]
00A92E1E  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
00A92E25  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
00A92E2C  48 89 85 F8 02 00 00            mov qword ptr [rbp + 0x2f8], rax
00A92E33  48 8D 05 06 4F 07 00            lea rax, [rip + 0x74f06]
00A92E3A  48 89 85 F0 02 00 00            mov qword ptr [rbp + 0x2f0], rax
00A92E41  48 8D 45 B8                     lea rax, [rbp - 0x48]
00A92E45  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00A92E4C  48 8D 85 00 01 00 00            lea rax, [rbp + 0x100]
00A92E53  48 89 85 30 03 00 00            mov qword ptr [rbp + 0x330], rax
00A92E5A  48 8D 05 BF 4E 07 00            lea rax, [rip + 0x74ebf]
00A92E61  48 89 85 28 03 00 00            mov qword ptr [rbp + 0x328], rax
00A92E68  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A92E6C  89 8D 00 03 00 00               mov dword ptr [rbp + 0x300], ecx
00A92E72  89 8D F0 00 00 00               mov dword ptr [rbp + 0xf0], ecx
00A92E78  48 89 95 18 03 00 00            mov qword ptr [rbp + 0x318], rdx
00A92E7F  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
00A92E83  89 8D 38 03 00 00               mov dword ptr [rbp + 0x338], ecx
00A92E89  89 8D 00 01 00 00               mov dword ptr [rbp + 0x100], ecx
00A92E8F  41 8B CE                        mov ecx, r14d
00A92E92  48 89 85 08 01 00 00            mov qword ptr [rbp + 0x108], rax
00A92E99  89 9D B0 00 00 00               mov dword ptr [rbp + 0xb0], ebx
00A92E9F  89 9D 58 02 00 00               mov dword ptr [rbp + 0x258], ebx
00A92EA5  89 9D C0 00 00 00               mov dword ptr [rbp + 0xc0], ebx
00A92EAB  89 9D 90 02 00 00               mov dword ptr [rbp + 0x290], ebx
00A92EB1  89 9D D0 00 00 00               mov dword ptr [rbp + 0xd0], ebx
00A92EB7  89 9D C8 02 00 00               mov dword ptr [rbp + 0x2c8], ebx
00A92EBD  89 9D E0 00 00 00               mov dword ptr [rbp + 0xe0], ebx
00A92EC3  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00A92EC8  E8 83 61 E3 FF                  call 0x1408c9050
00A92ECD  85 C0                           test eax, eax
00A92ECF  0F 88 5E 02 00 00               js 0x140a93133
00A92ED5  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00A92ED9  8B BD 28 07 00 00               mov edi, dword ptr [rbp + 0x728]
00A92EDF  48 85 D2                        test rdx, rdx
00A92EE2  0F 84 99 00 00 00               je 0x140a92f81
00A92EE8  85 FF                           test edi, edi
00A92EEA  0F 85 91 00 00 00               jne 0x140a92f81
00A92EF0  48 8D 45 80                     lea rax, [rbp - 0x80]
00A92EF4  89 9D 30 02 00 00               mov dword ptr [rbp + 0x230], ebx
00A92EFA  48 89 85 28 02 00 00            mov qword ptr [rbp + 0x228], rax
00A92F01  4C 8D 85 00 02 00 00            lea r8, [rbp + 0x200]
00A92F08  48 8D 45 88                     lea rax, [rbp - 0x78]
00A92F0C  89 9D 68 02 00 00               mov dword ptr [rbp + 0x268], ebx
00A92F12  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00A92F19  45 33 C9                        xor r9d, r9d
00A92F1C  48 8D 45 8C                     lea rax, [rbp - 0x74]
00A92F20  89 9D A0 02 00 00               mov dword ptr [rbp + 0x2a0], ebx
00A92F26  48 89 85 98 02 00 00            mov qword ptr [rbp + 0x298], rax
00A92F2D  41 8B CE                        mov ecx, r14d
00A92F30  48 8D 45 84                     lea rax, [rbp - 0x7c]
00A92F34  89 9D D8 02 00 00               mov dword ptr [rbp + 0x2d8], ebx
00A92F3A  48 89 85 D0 02 00 00            mov qword ptr [rbp + 0x2d0], rax
00A92F41  48 8D 45 B8                     lea rax, [rbp - 0x48]
00A92F45  48 89 85 08 03 00 00            mov qword ptr [rbp + 0x308], rax
00A92F4C  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A92F50  48 89 85 40 03 00 00            mov qword ptr [rbp + 0x340], rax
00A92F57  C7 85 10 03 00 00 08 00 00 00   mov dword ptr [rbp + 0x310], 8
00A92F61  C7 85 48 03 00 00 08 00 00 00   mov dword ptr [rbp + 0x348], 8
00A92F6B  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00A92F70  E8 DB 60 E3 FF                  call 0x1408c9050
00A92F75  85 C0                           test eax, eax
00A92F77  0F 88 B6 01 00 00               js 0x140a93133
00A92F7D  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00A92F81  44 39 6D 80                     cmp dword ptr [rbp - 0x80], r13d
00A92F85  0F 84 B6 01 00 00               je 0x140a93141
00A92F8B  85 FF                           test edi, edi
00A92F8D  4C 89 6D B0                     mov qword ptr [rbp - 0x50], r13
00A92F91  8B 7D C8                        mov edi, dword ptr [rbp - 0x38]
00A92F94  48 8B D6                        mov rdx, rsi
00A92F97  49 0F 45 D5                     cmovne rdx, r13
00A92F9B  0F 57 C0                        xorps xmm0, xmm0
00A92F9E  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
00A92FA2  85 FF                           test edi, edi
00A92FA4  74 06                           je 0x140a92fac
00A92FA6  66 89 7D B0                     mov word ptr [rbp - 0x50], di
00A92FAA  EB 09                           jmp 0x140a92fb5
00A92FAC  B8 FF FF 00 00                  mov eax, 0xffff
00A92FB1  66 89 45 B0                     mov word ptr [rbp - 0x50], ax
00A92FB5  48 8D 45 F0                     lea rax, [rbp - 0x10]
00A92FB9  49 8B CF                        mov rcx, r15
00A92FBC  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A92FC1  4C 8D 4D 40                     lea r9, [rbp + 0x40]
00A92FC5  48 8D 45 A0                     lea rax, [rbp - 0x60]
00A92FC9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A92FCE  4C 8D 45 70                     lea r8, [rbp + 0x70]
00A92FD2  48 8D 45 E8                     lea rax, [rbp - 0x18]
00A92FD6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A92FDB  48 8D 45 A4                     lea rax, [rbp - 0x5c]
00A92FDF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A92FE4  48 8D 45 E0                     lea rax, [rbp - 0x20]
00A92FE8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A92FED  48 8D 45 A8                     lea rax, [rbp - 0x58]
00A92FF1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A92FF6  48 8D 45 D8                     lea rax, [rbp - 0x28]
00A92FFA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A92FFF  E8 44 02 00 00                  call 0x140a93248
00A93004  48 8D 55 60                     lea rdx, [rbp + 0x60]
00A93008  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00A9300C  E8 DF EE E5 FF                  call 0x1408f1ef0
00A93011  85 C0                           test eax, eax
00A93013  0F 88 1A 01 00 00               js 0x140a93133
00A93019  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00A9301D  48 8B C8                        mov rcx, rax
00A93020  48 2B 0D C1 91 58 FF            sub rcx, qword ptr [rip - 0xa76e3f]
00A93027  75 0B                           jne 0x140a93034
00A93029  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00A9302D  48 2B 0D BC 91 58 FF            sub rcx, qword ptr [rip - 0xa76e44]
00A93034  48 85 C9                        test rcx, rcx
00A93037  74 19                           je 0x140a93052
00A93039  48 2B 05 60 E3 57 FF            sub rax, qword ptr [rip - 0xa81ca0]
00A93040  75 0B                           jne 0x140a9304d
00A93042  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00A93046  48 2B 05 5B E3 57 FF            sub rax, qword ptr [rip - 0xa81ca5]
00A9304D  48 85 C0                        test rax, rax
00A93050  75 41                           jne 0x140a93093
00A93052  4C 8B 55 F8                     mov r10, qword ptr [rbp - 8]
00A93056  4C 3B 15 4B 3A 53 00            cmp r10, qword ptr [rip + 0x533a4b]
00A9305D  0F 85 06 01 00 00               jne 0x140a93169
00A93063  41 3B 7A 10                     cmp edi, dword ptr [r10 + 0x10]
00A93067  73 2E                           jae 0x140a93097
00A93069  49 8B 82 C8 02 00 00            mov rax, qword ptr [r10 + 0x2c8]
00A93070  48 8B 14 F8                     mov rdx, qword ptr [rax + rdi*8]
00A93074  F6 C2 01                        test dl, 1
00A93077  75 1E                           jne 0x140a93097
00A93079  4C 39 AA A0 00 00 00            cmp qword ptr [rdx + 0xa0], r13
00A93080  0F 85 E3 00 00 00               jne 0x140a93169
00A93086  F0 81 8A 30 03 00 00 00 40 00 00  lock or dword ptr [rdx + 0x330], 0x4000
00A93091  EB 04                           jmp 0x140a93097
00A93093  4C 8B 55 F8                     mov r10, qword ptr [rbp - 8]
00A93097  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00A9309B  48 85 C9                        test rcx, rcx
00A9309E  75 07                           jne 0x140a930a7
00A930A0  8B 4D 84                        mov ecx, dword ptr [rbp - 0x7c]
00A930A3  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00A930A7  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00A930AB  48 8D 55 60                     lea rdx, [rbp + 0x60]
00A930AF  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
00A930B3  45 33 C0                        xor r8d, r8d
00A930B6  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00A930BE  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00A930C1  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00A930C8  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00A930CC  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A930D1  8B 45 A4                        mov eax, dword ptr [rbp - 0x5c]
00A930D4  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00A930D8  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00A930DC  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A930E1  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
00A930E4  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00A930E8  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00A930EC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A930F1  48 8D 45 40                     lea rax, [rbp + 0x40]
00A930F5  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A930FA  48 8D 45 70                     lea rax, [rbp + 0x70]
00A930FE  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A93103  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
00A93106  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A9310A  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A9310E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A93113  8A 45 8C                        mov al, byte ptr [rbp - 0x74]
00A93116  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A9311B  49 8B CA                        mov rcx, r10
00A9311E  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A93122  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00A9312A  E8 BD 97 FC FF                  call 0x140a5c8ec
00A9312F  85 C0                           test eax, eax
00A93131  79 0A                           jns 0x140a9313d
00A93133  8B C8                           mov ecx, eax
00A93135  E8 06 3B E9 FF                  call 0x140926c40
00A9313A  89 45 90                        mov dword ptr [rbp - 0x70], eax
00A9313D  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00A93141  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A93145  48 8D 45 90                     lea rax, [rbp - 0x70]
00A93149  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9314E  44 8B CB                        mov r9d, ebx
00A93151  4C 8D 05 68 C1 06 00            lea r8, [rip + 0x6c168]
00A93158  41 8B CE                        mov ecx, r14d
00A9315B  48 85 D2                        test rdx, rdx
00A9315E  75 04                           jne 0x140a93164
00A93160  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
00A93164  E8 B7 94 FD FF                  call 0x140a6c620
00A93169  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00A9316D  48 85 C9                        test rcx, rcx
00A93170  74 05                           je 0x140a93177
00A93172  E8 39 A1 C1 FF                  call 0x1406ad2b0
00A93177  4D 85 FF                        test r15, r15
00A9317A  74 0A                           je 0x140a93186
00A9317C  33 D2                           xor edx, edx
00A9317E  49 8B CF                        mov rcx, r15
00A93181  E8 EA F6 0E 00                  call 0x140b82870
00A93186  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A9318A  48 85 C9                        test rcx, rcx
00A9318D  74 05                           je 0x140a93194
00A9318F  E8 1C A1 C1 FF                  call 0x1406ad2b0
00A93194  48 85 F6                        test rsi, rsi
00A93197  74 0A                           je 0x140a931a3
00A93199  33 D2                           xor edx, edx
00A9319B  48 8B CE                        mov rcx, rsi
00A9319E  E8 CD F6 0E 00                  call 0x140b82870
00A931A3  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A931A7  48 85 C9                        test rcx, rcx
00A931AA  74 07                           je 0x140a931b3
00A931AC  33 D2                           xor edx, edx
00A931AE  E8 BD F6 0E 00                  call 0x140b82870
00A931B3  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A931B7  48 85 C9                        test rcx, rcx
00A931BA  74 07                           je 0x140a931c3
00A931BC  33 D2                           xor edx, edx
00A931BE  E8 AD F6 0E 00                  call 0x140b82870
00A931C3  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A931C7  48 85 C9                        test rcx, rcx
00A931CA  74 07                           je 0x140a931d3
00A931CC  33 D2                           xor edx, edx
00A931CE  E8 9D F6 0E 00                  call 0x140b82870
00A931D3  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00A931D7  48 85 C9                        test rcx, rcx
00A931DA  74 07                           je 0x140a931e3
00A931DC  33 D2                           xor edx, edx
00A931DE  E8 8D F6 0E 00                  call 0x140b82870
00A931E3  48 8D 7D 70                     lea rdi, [rbp + 0x70]
00A931E7  48 8B CF                        mov rcx, rdi
00A931EA  E8 11 D6 F2 FF                  call 0x1409c0800
00A931EF  48 83 C7 10                     add rdi, 0x10
00A931F3  48 83 EB 01                     sub rbx, 1
00A931F7  75 EE                           jne 0x140a931e7
00A931F9  48 8D 5D 40                     lea rbx, [rbp + 0x40]
00A931FD  BF 02 00 00 00                  mov edi, 2
00A93202  48 8B 0B                        mov rcx, qword ptr [rbx]
00A93205  48 85 C9                        test rcx, rcx
00A93208  74 07                           je 0x140a93211
00A9320A  33 D2                           xor edx, edx
00A9320C  E8 5F F6 0E 00                  call 0x140b82870
00A93211  48 83 C3 08                     add rbx, 8
00A93215  48 83 EF 01                     sub rdi, 1
00A93219  75 E7                           jne 0x140a93202
00A9321B  48 8B 8D A0 06 00 00            mov rcx, qword ptr [rbp + 0x6a0]
00A93222  48 33 CC                        xor rcx, rsp
00A93225  E8 16 94 C1 FF                  call 0x1406ac640
00A9322A  48 81 C4 C8 07 00 00            add rsp, 0x7c8
00A93231  41 5F                           pop r15
00A93233  41 5E                           pop r14
00A93235  41 5D                           pop r13
00A93237  41 5C                           pop r12
00A93239  5F                              pop rdi
00A9323A  5E                              pop rsi
00A9323B  5B                              pop rbx
00A9323C  5D                              pop rbp
00A9323D  C3                              ret
00A9323E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEnableAutoLoggerProvider(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned int v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3E0;
    unsigned int v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned int v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m418;
    unsigned int v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned int v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m450;
    unsigned int v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m488;
    unsigned int v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned int v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4C0;
    unsigned int v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned int v_stack_m4D8;
    unsigned __int64 v_stack_m4E0;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m4F8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F0;
    unsigned __int64 v_stack_m5F8;
    unsigned __int64 v_stack_m600;
    unsigned __int64 v_stack_m608;
    unsigned __int64 v_stack_m610;
    unsigned __int64 v_stack_m618;
    unsigned __int64 v_stack_m620;
    unsigned __int64 v_stack_m628;
    unsigned __int64 v_stack_m630;
    unsigned __int64 v_stack_m638;
    unsigned __int64 v_stack_m640;
    unsigned __int64 v_stack_m648;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m690;
    unsigned __int64 v_stack_m698;
    unsigned __int64 v_stack_m6A8;
    unsigned __int64 v_stack_m6B8;
    unsigned __int64 v_stack_m6C8;
    unsigned int v_stack_m6D0;
    unsigned __int64 v_stack_m6D8;
    unsigned int v_stack_m6E0;
    unsigned __int64 v_stack_m6E8;
    unsigned __int64 v_stack_m6F0;
    unsigned __int64 v_stack_m6F8;
    unsigned __int64 v_stack_m700;
    unsigned __int64 v_stack_m708;
    unsigned __int64 v_stack_m710;
    unsigned __int64 v_stack_m718;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned int v_stack_m730;
    unsigned __int64 v_stack_m738;
    unsigned __int64 v_stack_m740;
    unsigned __int64 v_stack_m748;
    unsigned int v_stack_m750;
    unsigned int v_stack_m754;
    unsigned int v_stack_m758;
    unsigned __int64 v_stack_m760;
    unsigned int v_stack_m768;
    unsigned int v_stack_m76C;
    unsigned int v_stack_m770;
    unsigned int v_stack_m774;
    unsigned int v_stack_m778;
    unsigned __int64 v_stack_m780;
    unsigned int v_stack_m788;
    unsigned __int64 v_stack_m790;
    unsigned int v_stack_m798;
    unsigned __int64 v_stack_m7A0;
    unsigned int v_stack_m7A8;
    unsigned __int64 v_stack_m7B0;
    unsigned __int64 v_stack_m7B8;
    unsigned __int64 v_stack_m7C0;
    unsigned __int64 v_stack_m7C8;
    unsigned __int64 v_stack_m7D0;
    unsigned __int64 v_stack_m7D8;
    unsigned __int8 v_stack_m7E0;
    unsigned __int64 v_stack_m7E8;

    v_rsp = (v_rsp) - (0x7C8ULL);
    result = (*(unsigned __int64 *)(v_rip + 3636253)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rbx = 0;
    v_stack_m748 = a5;
    result = 0;
    v_stack_m730 = a2;
    v_stack_m700 = a1;
    v_stack_m6D8 = 0;
    v_stack_m6D0 = 0;
    v_stack_m778 = 0;
    v_stack_m76C = 0;
    v_stack_m6A8 = v_xmm0;
    v_stack_m774 = 0;
    v_stack_m770 = 0;
    v_stack_m740 = 0;
    v_stack_m728 = 0;
    v_stack_m768 = 0;
    v_stack_m738 = 0;
    v_stack_m760 = 0;
    v_stack_m6F8 = v_xmm0;
    v_stack_m720 = 0;
    v_stack_m6E8 = v_xmm0;
    v_stack_m750 = 0;
    v_stack_m6C8 = v_xmm0;
    v_stack_m718 = 0;
    v_stack_m754 = 0;
    v_stack_m710 = 0;
    v_stack_m758 = 0;
    v_stack_m708 = 0;
    result = RtlInitUnicodeString(v_stack_m6A8, a3, a3, a4);
    a2 = 0;
    result = memset(v_stack_m4F8, a2, (unsigned int)(0x498ULL), a4);
    a2 = 0;
    result = memset(v_stack_m688, a2, v_rbx + 64, a4);
    v_rdi = (v_rdi) | (-1);
    v_stack_m6B8 = v_xmm0;
loc_00A92BDA:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(a4 + result * 2)) != 0) goto loc_00A92BDA;
loc_00A92BE8:
    a1 = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(a3 + a1 * 2)) != 0) goto loc_00A92BE8;
    result = (result) + (a1);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result * 2 + 4)), (unsigned int)(0x50777445ULL), a4);
    if (result == 0) goto loc_00A93169;
    v_stack_m7E8 = a3;
    result = RtlStringCbPrintfW(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result * 2 + 4)))), v_rip + 477166, a4);
    v_r13 = 0;
    if ((unsigned int)(result) != 0) goto loc_00A93169;
    result = RtlInitUnicodeString(v_stack_m6C8, result, v_rip + 477166, a4);
    v_stack_m6F8 = 48;
    v_stack_m6E8 = v_stack_m6C8;
    v_stack_m6F0 = 0;
    v_stack_m6E0 = 576;
    v_stack_m6D8 = v_xmm0;
    result = ZwOpenKey(v_stack_m738, (unsigned int)(0x2001FULL), v_stack_m6F8, a4);
    if (sign_flag) goto loc_00A93169;
    if (v_stack_m748 == 0) goto loc_00A92D44;
loc_00A92CA0:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m748 + result * 2)) != 0) goto loc_00A92CA0;
loc_00A92CAA:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(a3 + v_rdi * 2)) != 0) goto loc_00A92CAA;
    result = (result) + (v_rdi);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result * 2 + 4)), (unsigned int)(0x50777445ULL), a4);
    if (result == 0) goto loc_00A93169;
    v_stack_m7E8 = a3;
    result = RtlStringCbPrintfW(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result * 2 + 4)))), v_rip + 476978, v_stack_m748);
    if ((unsigned int)(result) != 0) goto loc_00A92D44;
    result = RtlInitUnicodeString(v_stack_m6C8, result, v_rip + 476978, v_stack_m748);
    v_stack_m6F8 = 48;
    v_stack_m6E8 = v_stack_m6C8;
    v_stack_m6F0 = 0;
    v_stack_m6E0 = 576;
    v_stack_m6D8 = v_xmm0;
    result = ZwOpenKey(v_stack_m760, (unsigned int)(0x2001FULL), v_stack_m6F8, v_stack_m748);
    if (sign_flag) {
        v_stack_m760 = 0;
    }
    v_stack_m4D8 = 4;
    v_stack_m4F8 = v_rip - 2966283;
    v_stack_m4C0 = v_rip - 2966283;
    v_stack_m4E0 = v_stack_m648;
    v_stack_m488 = v_rip - 2966283;
    v_stack_m4E8 = v_rip + 430448;
    v_stack_m450 = v_rip - 2966283;
    v_stack_m640 = v_stack_m778;
    a4 = 0;
    v_stack_m418 = v_rip - 2966283;
    v_stack_m4A8 = v_stack_m638;
    v_stack_m4B0 = v_rip + 474779;
    v_stack_m630 = v_stack_m770;
    v_stack_m470 = v_stack_m628;
    v_stack_m478 = v_rip + 479252;
    v_stack_m620 = v_stack_m76C;
    v_stack_m438 = v_stack_m618;
    v_stack_m440 = v_rip + 479181;
    v_stack_m610 = v_stack_m774;
    v_stack_m400 = v_stack_m608;
    v_stack_m408 = v_rip + 478982;
    v_stack_m600 = v_stack_m740;
    v_stack_m3C8 = v_stack_m5F8;
    v_stack_m3D0 = v_rip + 478911;
    v_stack_m3F8 = 11;
    v_stack_m608 = 11;
    v_stack_m3E0 = v_rip - 2966283;
    v_stack_m3C0 = 11;
    v_stack_m5F8 = 11;
    v_stack_m5F0 = v_stack_m728;
    v_stack_m648 = 4;
    v_stack_m4A0 = 4;
    v_stack_m638 = 4;
    v_stack_m468 = 4;
    v_stack_m628 = 4;
    v_stack_m430 = 4;
    v_stack_m618 = 4;
    v_stack_m7E0 = 1;
    result = RtlpQueryRegistryValues((unsigned int)((unsigned int)((unsigned int)(0x40000000ULL))), v_stack_m738, v_stack_m4F8, a4);
    if (sign_flag) goto loc_00A93133;
    if (v_stack_m760 == 0) goto loc_00A92F81;
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00A92F81;
    v_stack_m4C8 = 4;
    v_stack_m4D0 = v_stack_m778;
    v_stack_m490 = 4;
    v_stack_m498 = v_stack_m770;
    a4 = 0;
    v_stack_m458 = 4;
    v_stack_m460 = v_stack_m76C;
    v_stack_m420 = 4;
    v_stack_m428 = v_stack_m774;
    v_stack_m3F0 = v_stack_m740;
    v_stack_m3B8 = v_stack_m728;
    v_stack_m3E8 = 8;
    v_stack_m3B0 = 8;
    v_stack_m7E0 = 1;
    result = RtlpQueryRegistryValues((unsigned int)((unsigned int)((unsigned int)(0x40000000ULL))), v_stack_m760, v_stack_m4F8, a4);
    if (sign_flag) goto loc_00A93133;
loc_00A92F81:
    if (v_stack_m778 == 0) goto loc_00A93141;
    v_stack_m748 = 0;
    a2 = result;
    if ((unsigned int)((unsigned int)(a6)) != 0) { a2 = 0; }
    v_stack_m698 = v_xmm0;
    if ((unsigned int)((unsigned int)(v_stack_m730)) == 0) goto loc_00A92FAC;
    v_stack_m748 = (unsigned __int16)((unsigned int)(v_stack_m730));
    goto loc_00A92FB5;
loc_00A92FAC:
    v_stack_m748 = (unsigned __int16)((unsigned int)(0xFFFFULL));
loc_00A92FB5:
    v_stack_m7B8 = v_stack_m708;
    v_stack_m7C0 = v_stack_m758;
    v_stack_m7C8 = v_stack_m710;
    v_stack_m7D0 = v_stack_m754;
    v_stack_m7D8 = v_stack_m718;
    v_stack_m7E0 = v_stack_m750;
    v_stack_m7E8 = v_stack_m720;
    result = EtwpGetAutoLoggerProviderFilter(result, a2, v_stack_m688, v_stack_m6B8);
    result = RtlGUIDFromString(v_stack_m6A8, v_stack_m698, v_stack_m688, v_stack_m6B8);
    if (sign_flag) goto loc_00A93133;
    a1 = (v_stack_m698) - (*(unsigned __int64 *)(v_rip - 10972735));
    if (!(condition_is_not_equal)) {
        a1 = v_stack_m690;
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 10972740));
    }
    if (a1 == 0) goto loc_00A93052;
    result = (v_stack_m698) - (*(unsigned __int64 *)(v_rip - 11017376));
    if (!(condition_is_not_equal)) {
        result = v_stack_m690;
        result = (result) - (*(unsigned __int64 *)(v_rip - 11017381));
    }
    if (result != 0) goto loc_00A93093;
loc_00A93052:
    if (v_stack_m700 != (*(unsigned __int64 *)(v_rip + 5454411))) goto loc_00A93169;
    if (((unsigned int)((unsigned int)(v_stack_m730))) >= (*(unsigned int *)(v_stack_m700 + 16))) goto loc_00A93097;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m700 + 712) + (unsigned int)(v_stack_m730) * 8))) & (1)) != 0) goto loc_00A93097;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m700 + 712) + (unsigned int)(v_stack_m730) * 8) + 160)) != 0) goto loc_00A93169;
    goto loc_00A93097;
loc_00A93093:
loc_00A93097:
    if (v_stack_m740 == 0) {
        a1 = v_stack_m774;
        v_stack_m740 = a1;
    }
    a3 = 0;
    v_stack_m780 = v_stack_m708;
    v_stack_m788 = (unsigned int)((unsigned int)(v_stack_m758));
    v_stack_m790 = v_stack_m710;
    v_stack_m798 = (unsigned int)((unsigned int)(v_stack_m754));
    v_stack_m7A0 = v_stack_m718;
    v_stack_m7A8 = (unsigned int)((unsigned int)(v_stack_m750));
    v_stack_m7B0 = v_stack_m720;
    v_stack_m7B8 = v_stack_m6B8;
    v_stack_m7C0 = v_stack_m688;
    v_stack_m7C8 = (unsigned int)((unsigned int)(v_stack_m770));
    v_stack_m7D0 = v_stack_m728;
    v_stack_m7D8 = a1;
    v_stack_m7E0 = (unsigned __int8)(v_stack_m76C);
    v_stack_m7E8 = 1;
    result = EtwpEnableTrace(v_stack_m700, v_stack_m698, a3, v_stack_m748);
    if (sign_flag) {
        a1 = (unsigned int)(result);
        result = RtlNtStatusToDosError(a1, v_stack_m698, a3, v_stack_m748);
        v_stack_m768 = (unsigned int)(result);
    }
loc_00A93141:
    v_stack_m7E0 = 4;
    v_stack_m7E8 = v_stack_m768;
    if (v_stack_m760 == 0) {
        a2 = v_stack_m738;
    }
    result = RtlWriteRegistryValue((unsigned int)((unsigned int)((unsigned int)(0x40000000ULL))), a2, v_rip + 442728, 4);
loc_00A93169:
    if (v_stack_m738 != 0) {
        result = ZwClose(v_stack_m738, a2, v_rip + 442728, 4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 442728, 4);
    }
    if (v_stack_m760 != 0) {
        result = ZwClose(v_stack_m760, a2, v_rip + 442728, 4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 442728, 4);
    }
    if (v_stack_m720 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m720, a2, v_rip + 442728, 4);
    }
    if (v_stack_m718 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m718, a2, v_rip + 442728, 4);
    }
    if (v_stack_m710 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m710, a2, v_rip + 442728, 4);
    }
    if (v_stack_m708 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m708, a2, v_rip + 442728, 4);
    }
loc_00A931E7:
    result = RtlFreeAnsiString(v_stack_m688, a2, v_rip + 442728, 4);
    v_rdi = (v_stack_m688) + (16);
    v_rbx = (4) - (1);
    if (condition_is_not_equal) goto loc_00A931E7;
loc_00A93202:
    if (*(unsigned __int64 *)(v_stack_m6B8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m6B8), a2, v_rip + 442728, 4);
    }
    v_rbx = (v_stack_m6B8) + (8);
    v_rdi = (2) - (1);
    if (condition_is_not_equal) goto loc_00A93202;
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 442728, 4);
    v_rsp = (v_rsp) + (0x7C8ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEnableAutoLoggerProvider(int64_t Arg1, int32_t Arg2, void *Arg3, void *Arg4, int64_t Arg5, uint32_t Arg6)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint32_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3E0;
    uint32_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint32_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint64_t v_stack_m408;
    uint64_t v_stack_m418;
    uint32_t v_stack_m420;
    uint64_t v_stack_m428;
    uint32_t v_stack_m430;
    uint64_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m450;
    uint32_t v_stack_m458;
    uint64_t v_stack_m460;
    uint32_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m488;
    uint32_t v_stack_m490;
    uint64_t v_stack_m498;
    uint32_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4C0;
    uint32_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint32_t v_stack_m4D8;
    uint64_t v_stack_m4E0;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m4F8;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F0;
    uint64_t v_stack_m5F8;
    uint64_t v_stack_m600;
    uint64_t v_stack_m608;
    uint64_t v_stack_m610;
    uint64_t v_stack_m618;
    uint64_t v_stack_m620;
    uint64_t v_stack_m628;
    uint64_t v_stack_m630;
    uint64_t v_stack_m638;
    uint64_t v_stack_m640;
    uint64_t v_stack_m648;
    uint64_t v_stack_m688;
    uint64_t v_stack_m690;
    uint64_t v_stack_m698;
    uint64_t v_stack_m6A8;
    uint64_t v_stack_m6B8;
    uint64_t v_stack_m6C8;
    uint32_t v_stack_m6D0;
    uint64_t v_stack_m6D8;
    uint32_t v_stack_m6E0;
    uint64_t v_stack_m6E8;
    uint64_t v_stack_m6F0;
    uint64_t v_stack_m6F8;
    uint64_t v_stack_m700;
    uint64_t v_stack_m708;
    uint64_t v_stack_m710;
    uint64_t v_stack_m718;
    uint64_t v_stack_m720;
    uint64_t v_stack_m728;
    uint32_t v_stack_m730;
    uint64_t v_stack_m738;
    uint64_t v_stack_m740;
    uint64_t v_stack_m748;
    uint32_t v_stack_m750;
    uint32_t v_stack_m754;
    uint32_t v_stack_m758;
    uint64_t v_stack_m760;
    uint32_t v_stack_m768;
    uint32_t v_stack_m76C;
    uint32_t v_stack_m770;
    uint32_t v_stack_m774;
    uint32_t v_stack_m778;
    uint64_t v_stack_m780;
    uint32_t v_stack_m788;
    uint64_t v_stack_m790;
    uint32_t v_stack_m798;
    uint64_t v_stack_m7A0;
    uint32_t v_stack_m7A8;
    uint64_t v_stack_m7B0;
    uint64_t v_stack_m7B8;
    uint64_t v_stack_m7C0;
    uint64_t v_stack_m7C8;
    uint64_t v_stack_m7D0;
    uint64_t v_stack_m7D8;
    uint8_t v_stack_m7E0;
    uint64_t v_stack_m7E8;

    local_rsp = (local_rsp) - (0x7C8ULL);
    result = (*(uint64_t *)(v_rip + 0x377C1D)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rbx = 0;
    v_stack_m748 = Arg5;
    result = 0;
    v_stack_m730 = Arg2;
    v_stack_m700 = Arg1;
    v_stack_m6D8 = 0;
    v_stack_m6D0 = 0;
    v_stack_m778 = 0;
    v_stack_m76C = 0;
    v_stack_m6A8 = v_xmm0;
    v_stack_m774 = 0;
    v_stack_m770 = 0;
    v_stack_m740 = 0;
    v_stack_m728 = 0;
    v_stack_m768 = 0;
    v_stack_m738 = 0;
    v_stack_m760 = 0;
    v_stack_m6F8 = v_xmm0;
    v_stack_m720 = 0;
    v_stack_m6E8 = v_xmm0;
    v_stack_m750 = 0;
    v_stack_m6C8 = v_xmm0;
    v_stack_m718 = 0;
    v_stack_m754 = 0;
    v_stack_m710 = 0;
    v_stack_m758 = 0;
    v_stack_m708 = 0;
    result = RtlInitUnicodeString(v_stack_m6A8, Arg3, Arg3, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m4F8, Arg2, (uint32_t)(0x498ULL), Arg4);
    Arg2 = 0;
    result = memset(v_stack_m688, Arg2, local_rbx + 64, Arg4);
    local_rdi = (local_rdi) | (-1);
    v_stack_m6B8 = v_xmm0;
loc_00A92BDA:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(arg4 + result * 2)) != 0) goto loc_00A92BDA;
loc_00A92BE8:
    Arg1 = (local_rdi) + 1;
    if ((*(uint16_t *)(arg3 + Arg1 * 2)) != 0) goto loc_00A92BE8;
    result = (result) + (Arg1);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result * 2 + 4)), (uint32_t)(0x50777445ULL), Arg4);
    if (result == 0) goto loc_00A93169;
    v_stack_m7E8 = Arg3;
    result = RtlStringCbPrintfW(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result * 2 + 4)))), v_rip + 477166, Arg4);
    local_r13 = 0;
    if ((uint32_t)(result) != 0) goto loc_00A93169;
    result = RtlInitUnicodeString(v_stack_m6C8, result, v_rip + 477166, Arg4);
    v_stack_m6F8 = 48;
    v_stack_m6E8 = v_stack_m6C8;
    v_stack_m6F0 = 0;
    v_stack_m6E0 = 576;
    v_stack_m6D8 = v_xmm0;
    result = ZwOpenKey(v_stack_m738, (uint32_t)(0x2001FULL), v_stack_m6F8, Arg4);
    if (sign_flag) goto loc_00A93169;
    if (v_stack_m748 == 0) goto loc_00A92D44;
loc_00A92CA0:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(v_stack_m748 + result * 2)) != 0) goto loc_00A92CA0;
loc_00A92CAA:
    local_rdi = (local_rdi) + 1;
    if ((*(uint16_t *)(arg3 + local_rdi * 2)) != 0) goto loc_00A92CAA;
    result = (result) + (local_rdi);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result * 2 + 4)), (uint32_t)(0x50777445ULL), Arg4);
    if (result == 0) goto loc_00A93169;
    v_stack_m7E8 = Arg3;
    result = RtlStringCbPrintfW(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result * 2 + 4)))), v_rip + 476978, v_stack_m748);
    if ((uint32_t)(result) != 0) goto loc_00A92D44;
    result = RtlInitUnicodeString(v_stack_m6C8, result, v_rip + 476978, v_stack_m748);
    v_stack_m6F8 = 48;
    v_stack_m6E8 = v_stack_m6C8;
    v_stack_m6F0 = 0;
    v_stack_m6E0 = 576;
    v_stack_m6D8 = v_xmm0;
    result = ZwOpenKey(v_stack_m760, (uint32_t)(0x2001FULL), v_stack_m6F8, v_stack_m748);
    if (sign_flag) {
        v_stack_m760 = 0;
    }
    v_stack_m4D8 = 4;
    v_stack_m4F8 = v_rip - 2966283;
    v_stack_m4C0 = v_rip - 2966283;
    v_stack_m4E0 = v_stack_m648;
    v_stack_m488 = v_rip - 2966283;
    v_stack_m4E8 = v_rip + 430448;
    v_stack_m450 = v_rip - 2966283;
    v_stack_m640 = v_stack_m778;
    Arg4 = 0;
    v_stack_m418 = v_rip - 2966283;
    v_stack_m4A8 = v_stack_m638;
    v_stack_m4B0 = v_rip + 474779;
    v_stack_m630 = v_stack_m770;
    v_stack_m470 = v_stack_m628;
    v_stack_m478 = v_rip + 479252;
    v_stack_m620 = v_stack_m76C;
    v_stack_m438 = v_stack_m618;
    v_stack_m440 = v_rip + 479181;
    v_stack_m610 = v_stack_m774;
    v_stack_m400 = v_stack_m608;
    v_stack_m408 = v_rip + 478982;
    v_stack_m600 = v_stack_m740;
    v_stack_m3C8 = v_stack_m5F8;
    v_stack_m3D0 = v_rip + 478911;
    v_stack_m3F8 = 11;
    v_stack_m608 = 11;
    v_stack_m3E0 = v_rip - 2966283;
    v_stack_m3C0 = 11;
    v_stack_m5F8 = 11;
    v_stack_m5F0 = v_stack_m728;
    v_stack_m648 = 4;
    v_stack_m4A0 = 4;
    v_stack_m638 = 4;
    v_stack_m468 = 4;
    v_stack_m628 = 4;
    v_stack_m430 = 4;
    v_stack_m618 = 4;
    v_stack_m7E0 = 1;
    result = RtlpQueryRegistryValues((uint32_t)((uint32_t)((uint32_t)(0x40000000ULL))), v_stack_m738, v_stack_m4F8, Arg4);
    if (sign_flag) goto loc_00A93133;
    if (v_stack_m760 == 0) goto loc_00A92F81;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00A92F81;
    v_stack_m4C8 = 4;
    v_stack_m4D0 = v_stack_m778;
    v_stack_m490 = 4;
    v_stack_m498 = v_stack_m770;
    Arg4 = 0;
    v_stack_m458 = 4;
    v_stack_m460 = v_stack_m76C;
    v_stack_m420 = 4;
    v_stack_m428 = v_stack_m774;
    v_stack_m3F0 = v_stack_m740;
    v_stack_m3B8 = v_stack_m728;
    v_stack_m3E8 = 8;
    v_stack_m3B0 = 8;
    v_stack_m7E0 = 1;
    result = RtlpQueryRegistryValues((uint32_t)((uint32_t)((uint32_t)(0x40000000ULL))), v_stack_m760, v_stack_m4F8, Arg4);
    if (sign_flag) goto loc_00A93133;
loc_00A92F81:
    if (v_stack_m778 == 0) goto loc_00A93141;
    v_stack_m748 = 0;
    Arg2 = result;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) { Arg2 = 0; }
    v_stack_m698 = v_xmm0;
    if ((uint32_t)((uint32_t)(v_stack_m730)) == 0) goto loc_00A92FAC;
    v_stack_m748 = (uint16_t)((uint32_t)(v_stack_m730));
    goto loc_00A92FB5;
loc_00A92FAC:
    v_stack_m748 = (uint16_t)((uint32_t)(0xFFFFULL));
loc_00A92FB5:
    v_stack_m7B8 = v_stack_m708;
    v_stack_m7C0 = v_stack_m758;
    v_stack_m7C8 = v_stack_m710;
    v_stack_m7D0 = v_stack_m754;
    v_stack_m7D8 = v_stack_m718;
    v_stack_m7E0 = v_stack_m750;
    v_stack_m7E8 = v_stack_m720;
    result = EtwpGetAutoLoggerProviderFilter(result, Arg2, v_stack_m688, v_stack_m6B8);
    result = RtlGUIDFromString(v_stack_m6A8, v_stack_m698, v_stack_m688, v_stack_m6B8);
    if (sign_flag) goto loc_00A93133;
    Arg1 = (v_stack_m698) - (*(uint64_t *)(v_rip - 0xA76E3F));
    if (!(condition_is_not_equal)) {
        Arg1 = v_stack_m690;
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0xA76E44));
    }
    if (Arg1 == 0) goto loc_00A93052;
    result = (v_stack_m698) - (*(uint64_t *)(v_rip - 0xA81CA0));
    if (!(condition_is_not_equal)) {
        result = v_stack_m690;
        result = (result) - (*(uint64_t *)(v_rip - 0xA81CA5));
    }
    if (result != 0) goto loc_00A93093;
loc_00A93052:
    if (v_stack_m700 != (*(uint64_t *)(v_rip + 0x533A4B))) goto loc_00A93169;
    if (((uint32_t)((uint32_t)(v_stack_m730))) >= (*(uint32_t *)(v_stack_m700 + 0x10))) goto loc_00A93097;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m700 + 0x2C8) + (uint32_t)(v_stack_m730) * 8))) & (1)) != 0) goto loc_00A93097;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m700 + 0x2C8) + (uint32_t)(v_stack_m730) * 8) + 0xA0)) != 0) goto loc_00A93169;
    goto loc_00A93097;
loc_00A93093:
loc_00A93097:
    if (v_stack_m740 == 0) {
        Arg1 = v_stack_m774;
        v_stack_m740 = Arg1;
    }
    Arg3 = 0;
    v_stack_m780 = v_stack_m708;
    v_stack_m788 = (uint32_t)((uint32_t)(v_stack_m758));
    v_stack_m790 = v_stack_m710;
    v_stack_m798 = (uint32_t)((uint32_t)(v_stack_m754));
    v_stack_m7A0 = v_stack_m718;
    v_stack_m7A8 = (uint32_t)((uint32_t)(v_stack_m750));
    v_stack_m7B0 = v_stack_m720;
    v_stack_m7B8 = v_stack_m6B8;
    v_stack_m7C0 = v_stack_m688;
    v_stack_m7C8 = (uint32_t)((uint32_t)(v_stack_m770));
    v_stack_m7D0 = v_stack_m728;
    v_stack_m7D8 = Arg1;
    v_stack_m7E0 = (uint8_t)(v_stack_m76C);
    v_stack_m7E8 = 1;
    result = EtwpEnableTrace(v_stack_m700, v_stack_m698, Arg3, v_stack_m748);
    if (sign_flag) {
        Arg1 = (uint32_t)(result);
        result = RtlNtStatusToDosError(Arg1, v_stack_m698, Arg3, v_stack_m748);
        v_stack_m768 = (uint32_t)(result);
    }
loc_00A93141:
    v_stack_m7E0 = 4;
    v_stack_m7E8 = v_stack_m768;
    if (v_stack_m760 == 0) {
        Arg2 = v_stack_m738;
    }
    result = RtlWriteRegistryValue((uint32_t)((uint32_t)((uint32_t)(0x40000000ULL))), Arg2, v_rip + 442728, 4);
loc_00A93169:
    if (v_stack_m738 != 0) {
        result = ZwClose(v_stack_m738, Arg2, v_rip + 442728, 4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 442728, 4);
    }
    if (v_stack_m760 != 0) {
        result = ZwClose(v_stack_m760, Arg2, v_rip + 442728, 4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 442728, 4);
    }
    if (v_stack_m720 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m720, Arg2, v_rip + 442728, 4);
    }
    if (v_stack_m718 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m718, Arg2, v_rip + 442728, 4);
    }
    if (v_stack_m710 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m710, Arg2, v_rip + 442728, 4);
    }
    if (v_stack_m708 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m708, Arg2, v_rip + 442728, 4);
    }
loc_00A931E7:
    result = RtlFreeAnsiString(v_stack_m688, Arg2, v_rip + 442728, 4);
    local_rdi = (v_stack_m688) + (16);
    local_rbx = (4) - (1);
    if (condition_is_not_equal) goto loc_00A931E7;
loc_00A93202:
    if (*(uint64_t *)(v_stack_m6B8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m6B8), Arg2, v_rip + 442728, 4);
    }
    local_rbx = (v_stack_m6B8) + (8);
    local_rdi = (2) - (1);
    if (condition_is_not_equal) goto loc_00A93202;
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 442728, 4);
    local_rsp = (local_rsp) + (0x7C8ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + rcx*2` | `16` | `R` |
| `Arg3` | `+ 0x0 + rdi*2` | `16` | `R` |
| `Arg4` | `+ 0x0 + rax*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A92B00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
