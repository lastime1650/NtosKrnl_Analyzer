# CmDeviceClassesSubkeyCallback

- RVA: `0x0082C940`–`0x0082CE45` (길이 `1,285` bytes)
- VA: `0x000000014082C940`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7294`
- 디코드: `313`개 명령, `1,285/1,285` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0082CA2F` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x0082CA78` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082CAAD` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x0082CAE1` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0082CAF5` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0082CB12` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x0082CB60` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082CB9B` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x0082CBCE` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x0082CC07` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082CC3D` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x0082CC62` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x0082CCE0` → [PnpCtxRegEnumKeyWithCallback](../AA/PnpCtxRegEnumKeyWithCallback_function_00AA146C.md) (function, `0x00AA146C`)
- `0x0082CD2A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082CD41` → [CmValidateDeviceInterfaceName](../8F/CmValidateDeviceInterfaceName_function_008F1A40.md) (function, `0x008F1A40`)
- `0x0082CD55` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0082CD7B` → [CmIsDeviceInterfaceEnabled](../9F/CmIsDeviceInterfaceEnabled_function_009F21E0.md) (function, `0x009F21E0`)
- `0x0082CDA9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0082CDDE` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x0082CDFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082CE0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082CE1C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0082CA9A` → RVA `0x00B0D7F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0082CC6E` → RVA `0x0082C940` (`CmDeviceClassesSubkeyCallback`; read)
- `0x0082CD34` → RVA `0x00B0D4E0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x0082CA78` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082CAE1` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x0082CAF5` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x0082CB60` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082CB9B` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x0082CBCE` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x0082CC07` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082CC3D` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x0082CC62` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x0082CD2A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082CD55` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x0082CDA9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0082CDDE` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x0082CDFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082CE0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082CE1C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0082C940  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0082C945  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0082C94A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0082C94F  55                              push rbp
0082C950  41 54                           push r12
0082C952  41 55                           push r13
0082C954  41 56                           push r14
0082C956  41 57                           push r15
0082C958  48 8B EC                        mov rbp, rsp
0082C95B  48 81 EC 80 00 00 00            sub rsp, 0x80
0082C962  49 8B D9                        mov rbx, r9
0082C965  0F 57 C0                        xorps xmm0, xmm0
0082C968  45 33 C9                        xor r9d, r9d
0082C96B  4C 8B E9                        mov r13, rcx
0082C96E  4D 8B F0                        mov r14, r8
0082C971  4C 89 4D B8                     mov qword ptr [rbp - 0x48], r9
0082C975  0F 57 C9                        xorps xmm1, xmm1
0082C978  44 89 4D B0                     mov dword ptr [rbp - 0x50], r9d
0082C97C  8B 0B                           mov ecx, dword ptr [rbx]
0082C97E  45 8B F9                        mov r15d, r9d
0082C981  8B C1                           mov eax, ecx
0082C983  4C 89 4D C0                     mov qword ptr [rbp - 0x40], r9
0082C987  45 8D 41 01                     lea r8d, [r9 + 1]
0082C98B  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
0082C98F  45 0F B6 E1                     movzx r12d, r9b
0082C993  41 8B F9                        mov edi, r9d
0082C996  44 88 4D 48                     mov byte ptr [rbp + 0x48], r9b
0082C99A  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0082C99E  0F 11 4D E0                     movups xmmword ptr [rbp - 0x20], xmm1
0082C9A2  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0082C9A6  41 2B C0                        sub eax, r8d
0082C9A9  74 41                           je 0x14082c9ec
0082C9AB  48 83 CE FF                     or rsi, 0xffffffffffffffff
0082C9AF  41 2B C0                        sub eax, r8d
0082C9B2  74 05                           je 0x14082c9b9
0082C9B4  41 3B C0                        cmp eax, r8d
0082C9B7  75 21                           jne 0x14082c9da
0082C9B9  48 8B C6                        mov rax, rsi
0082C9BC  48 FF C0                        inc rax
0082C9BF  66 45 39 0C 46                  cmp word ptr [r14 + rax*2], r9w
0082C9C4  75 F6                           jne 0x14082c9bc
0082C9C6  49 3B C0                        cmp rax, r8
0082C9C9  0F 82 52 04 00 00               jb 0x14082ce21
0082C9CF  66 41 83 3E 23                  cmp word ptr [r14], 0x23
0082C9D4  0F 85 47 04 00 00               jne 0x14082ce21
0082C9DA  83 F9 03                        cmp ecx, 3
0082C9DD  72 33                           jb 0x14082ca12
0082C9DF  75 62                           jne 0x14082ca43
0082C9E1  44 38 8B 94 05 00 00            cmp byte ptr [rbx + 0x594], r9b
0082C9E8  74 59                           je 0x14082ca43
0082C9EA  EB 26                           jmp 0x14082ca12
0082C9EC  48 83 CE FF                     or rsi, 0xffffffffffffffff
0082C9F0  48 8B C6                        mov rax, rsi
0082C9F3  48 FF C0                        inc rax
0082C9F6  66 45 39 0C 46                  cmp word ptr [r14 + rax*2], r9w
0082C9FB  75 F6                           jne 0x14082c9f3
0082C9FD  48 83 F8 26                     cmp rax, 0x26
0082CA01  0F 85 1A 04 00 00               jne 0x14082ce21
0082CA07  66 41 83 3E 7B                  cmp word ptr [r14], 0x7b
0082CA0C  0F 85 0F 04 00 00               jne 0x14082ce21
0082CA12  48 8D 45 B8                     lea rax, [rbp - 0x48]
0082CA16  41 B9 08 00 00 00               mov r9d, 8
0082CA1C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082CA21  4D 8B C6                        mov r8, r14
0082CA24  49 8B CD                        mov rcx, r13
0082CA27  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
0082CA2F  E8 84 2D 0C 00                  call 0x1408ef7b8
0082CA34  45 33 C9                        xor r9d, r9d
0082CA37  85 C0                           test eax, eax
0082CA39  0F 88 D4 03 00 00               js 0x14082ce13
0082CA3F  45 8D 41 01                     lea r8d, [r9 + 1]
0082CA43  8B 03                           mov eax, dword ptr [rbx]
0082CA45  83 F8 03                        cmp eax, 3
0082CA48  0F 83 D3 00 00 00               jae 0x14082cb21
0082CA4E  83 F8 02                        cmp eax, 2
0082CA51  0F 85 EB 00 00 00               jne 0x14082cb42
0082CA57  48 8D B3 F4 03 00 00            lea rsi, [rbx + 0x3f4]
0082CA5E  66 44 39 0E                     cmp word ptr [rsi], r9w
0082CA62  0F 84 DA 00 00 00               je 0x14082cb42
0082CA68  BA 90 01 00 00                  mov edx, 0x190
0082CA6D  B9 00 01 00 00                  mov ecx, 0x100
0082CA72  41 B8 50 4E 50 52               mov r8d, 0x52504e50
0082CA78  E8 73 56 35 00                  call 0x140b820f0
0082CA7D  4C 8B F8                        mov r15, rax
0082CA80  48 85 C0                        test rax, rax
0082CA83  0F 84 8A 03 00 00               je 0x14082ce13
0082CA89  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
0082CA8D  48 8D 45 B4                     lea rax, [rbp - 0x4c]
0082CA91  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082CA96  4C 8D 4D B0                     lea r9, [rbp - 0x50]
0082CA9A  4C 8D 05 4F 0D 2E 00            lea r8, [rip + 0x2e0d4f]
0082CAA1  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0082CAA6  C7 45 B4 90 01 00 00            mov dword ptr [rbp - 0x4c], 0x190
0082CAAD  E8 4A 76 16 00                  call 0x1409940fc
0082CAB2  33 C9                           xor ecx, ecx
0082CAB4  85 C0                           test eax, eax
0082CAB6  0F 88 4D 03 00 00               js 0x14082ce09
0082CABC  8D 41 01                        lea eax, [rcx + 1]
0082CABF  39 45 B0                        cmp dword ptr [rbp - 0x50], eax
0082CAC2  0F 85 41 03 00 00               jne 0x14082ce09
0082CAC8  83 7D B4 02                     cmp dword ptr [rbp - 0x4c], 2
0082CACC  0F 82 37 03 00 00               jb 0x14082ce09
0082CAD2  66 41 89 8F 8E 01 00 00         mov word ptr [r15 + 0x18e], cx
0082CADA  49 8B D7                        mov rdx, r15
0082CADD  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0082CAE1  E8 7A 6E C3 FF                  call 0x140463960
0082CAE6  85 C0                           test eax, eax
0082CAE8  0F 88 1B 03 00 00               js 0x14082ce09
0082CAEE  48 8B D6                        mov rdx, rsi
0082CAF1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0082CAF5  E8 66 6E C3 FF                  call 0x140463960
0082CAFA  85 C0                           test eax, eax
0082CAFC  0F 88 07 03 00 00               js 0x14082ce09
0082CB02  BE 01 00 00 00                  mov esi, 1
0082CB07  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0082CB0B  44 8A C6                        mov r8b, sil
0082CB0E  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0082CB12  E8 09 5F 10 00                  call 0x140932a20
0082CB17  84 C0                           test al, al
0082CB19  0F 84 EA 02 00 00               je 0x14082ce09
0082CB1F  EB 26                           jmp 0x14082cb47
0082CB21  75 1F                           jne 0x14082cb42
0082CB23  48 FF C6                        inc rsi
0082CB26  66 45 39 0C 76                  cmp word ptr [r14 + rsi*2], r9w
0082CB2B  75 F6                           jne 0x14082cb23
0082CB2D  49 3B F0                        cmp rsi, r8
0082CB30  BE 01 00 00 00                  mov esi, 1
0082CB35  76 10                           jbe 0x14082cb47
0082CB37  66 41 83 3E 23                  cmp word ptr [r14], 0x23
0082CB3C  45 0F 44 E0                     cmove r12d, r8d
0082CB40  EB 05                           jmp 0x14082cb47
0082CB42  BE 01 00 00 00                  mov esi, 1
0082CB47  83 3B 02                        cmp dword ptr [rbx], 2
0082CB4A  0F 82 9B 00 00 00               jb 0x14082cbeb
0082CB50  BA F0 03 00 00                  mov edx, 0x3f0
0082CB55  B9 00 01 00 00                  mov ecx, 0x100
0082CB5A  41 B8 50 4E 50 52               mov r8d, 0x52504e50
0082CB60  E8 8B 55 35 00                  call 0x140b820f0
0082CB65  45 33 C9                        xor r9d, r9d
0082CB68  48 8B F8                        mov rdi, rax
0082CB6B  48 85 C0                        test rax, rax
0082CB6E  0F 84 90 02 00 00               je 0x14082ce04
0082CB74  4C 8D 43 04                     lea r8, [rbx + 4]
0082CB78  BA F8 01 00 00                  mov edx, 0x1f8
0082CB7D  66 45 39 08                     cmp word ptr [r8], r9w
0082CB81  74 38                           je 0x14082cbbb
0082CB83  48 8D 45 C8                     lea rax, [rbp - 0x38]
0082CB87  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
0082CB8F  4C 8D 4D C0                     lea r9, [rbp - 0x40]
0082CB93  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0082CB98  48 8B CF                        mov rcx, rdi
0082CB9B  E8 20 16 BF FF                  call 0x14041e1c0
0082CBA0  33 C9                           xor ecx, ecx
0082CBA2  85 C0                           test eax, eax
0082CBA4  0F 88 50 02 00 00               js 0x14082cdfa
0082CBAA  4C 8B 5D C0                     mov r11, qword ptr [rbp - 0x40]
0082CBAE  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0082CBB2  48 FF CA                        dec rdx
0082CBB5  66 41 89 0B                     mov word ptr [r11], cx
0082CBB9  EB 03                           jmp 0x14082cbbe
0082CBBB  4C 8B DF                        mov r11, rdi
0082CBBE  83 3B 02                        cmp dword ptr [rbx], 2
0082CBC1  74 05                           je 0x14082cbc8
0082CBC3  44 3A E6                        cmp r12b, sil
0082CBC6  75 23                           jne 0x14082cbeb
0082CBC8  4D 8B C6                        mov r8, r14
0082CBCB  49 8B CB                        mov rcx, r11
0082CBCE  E8 D1 1D A4 FF                  call 0x14026e9a4
0082CBD3  45 33 F6                        xor r14d, r14d
0082CBD6  85 C0                           test eax, eax
0082CBD8  0F 88 1C 02 00 00               js 0x14082cdfa
0082CBDE  44 3A E6                        cmp r12b, sil
0082CBE1  75 0B                           jne 0x14082cbee
0082CBE3  66 41 C7 03 5C 00               mov word ptr [r11], 0x5c
0082CBE9  EB 03                           jmp 0x14082cbee
0082CBEB  45 33 F6                        xor r14d, r14d
0082CBEE  83 3B 03                        cmp dword ptr [rbx], 3
0082CBF1  0F 83 3D 01 00 00               jae 0x14082cd34
0082CBF7  BA B8 05 00 00                  mov edx, 0x5b8
0082CBFC  B9 00 01 00 00                  mov ecx, 0x100
0082CC01  41 B8 50 4E 50 52               mov r8d, 0x52504e50
0082CC07  E8 E4 54 35 00                  call 0x140b820f0
0082CC0C  48 8B F0                        mov rsi, rax
0082CC0F  48 85 C0                        test rax, rax
0082CC12  0F 84 DD 01 00 00               je 0x14082cdf5
0082CC18  8B 0B                           mov ecx, dword ptr [rbx]
0082CC1A  41 BC 00 09 00 00               mov r12d, 0x900
0082CC20  FF C1                           inc ecx
0082CC22  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
0082CC27  89 08                           mov dword ptr [rax], ecx
0082CC29  45 33 C9                        xor r9d, r9d
0082CC2C  48 8D 48 04                     lea rcx, [rax + 4]
0082CC30  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0082CC35  4C 8B C7                        mov r8, rdi
0082CC38  BA F8 01 00 00                  mov edx, 0x1f8
0082CC3D  E8 7E 15 BF FF                  call 0x14041e1c0
0082CC42  4C 8D 83 F4 03 00 00            lea r8, [rbx + 0x3f4]
0082CC49  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
0082CC4E  48 8D 8E F4 03 00 00            lea rcx, [rsi + 0x3f4]
0082CC55  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0082CC5A  45 33 C9                        xor r9d, r9d
0082CC5D  BA C8 00 00 00                  mov edx, 0xc8
0082CC62  E8 59 15 BF FF                  call 0x14041e1c0
0082CC67  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0082CC6E  4C 8D 05 CB FC FF FF            lea r8, [rip - 0x335]
0082CC75  48 89 86 88 05 00 00            mov qword ptr [rsi + 0x588], rax
0082CC7C  4C 8B CE                        mov r9, rsi
0082CC7F  8B 83 90 05 00 00               mov eax, dword ptr [rbx + 0x590]
0082CC85  49 8B CD                        mov rcx, r13
0082CC88  89 86 90 05 00 00               mov dword ptr [rsi + 0x590], eax
0082CC8E  8A 83 94 05 00 00               mov al, byte ptr [rbx + 0x594]
0082CC94  88 86 94 05 00 00               mov byte ptr [rsi + 0x594], al
0082CC9A  48 8B 83 98 05 00 00            mov rax, qword ptr [rbx + 0x598]
0082CCA1  48 89 86 98 05 00 00            mov qword ptr [rsi + 0x598], rax
0082CCA8  48 8B 83 A0 05 00 00            mov rax, qword ptr [rbx + 0x5a0]
0082CCAF  48 89 86 A0 05 00 00            mov qword ptr [rsi + 0x5a0], rax
0082CCB6  48 8B 83 A8 05 00 00            mov rax, qword ptr [rbx + 0x5a8]
0082CCBD  48 89 86 A8 05 00 00            mov qword ptr [rsi + 0x5a8], rax
0082CCC4  8B 83 B0 05 00 00               mov eax, dword ptr [rbx + 0x5b0]
0082CCCA  89 86 B0 05 00 00               mov dword ptr [rsi + 0x5b0], eax
0082CCD0  8B 83 B4 05 00 00               mov eax, dword ptr [rbx + 0x5b4]
0082CCD6  89 86 B4 05 00 00               mov dword ptr [rsi + 0x5b4], eax
0082CCDC  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
0082CCE0  E8 87 47 27 00                  call 0x140aa146c
0082CCE5  48 8B 86 88 05 00 00            mov rax, qword ptr [rsi + 0x588]
0082CCEC  33 D2                           xor edx, edx
0082CCEE  48 89 83 88 05 00 00            mov qword ptr [rbx + 0x588], rax
0082CCF5  48 8B CE                        mov rcx, rsi
0082CCF8  8B 86 90 05 00 00               mov eax, dword ptr [rsi + 0x590]
0082CCFE  89 83 90 05 00 00               mov dword ptr [rbx + 0x590], eax
0082CD04  8B 86 B4 05 00 00               mov eax, dword ptr [rsi + 0x5b4]
0082CD0A  89 83 B4 05 00 00               mov dword ptr [rbx + 0x5b4], eax
0082CD10  48 8B 86 A8 05 00 00            mov rax, qword ptr [rsi + 0x5a8]
0082CD17  48 89 83 A8 05 00 00            mov qword ptr [rbx + 0x5a8], rax
0082CD1E  8B 86 B0 05 00 00               mov eax, dword ptr [rsi + 0x5b0]
0082CD24  89 83 B0 05 00 00               mov dword ptr [rbx + 0x5b0], eax
0082CD2A  E8 41 5B 35 00                  call 0x140b82870
0082CD2F  E9 C1 00 00 00                  jmp 0x14082cdf5
0082CD34  48 8B 05 A5 07 2E 00            mov rax, qword ptr [rip + 0x2e07a5]
0082CD3B  48 8B D7                        mov rdx, rdi
0082CD3E  48 89 07                        mov qword ptr [rdi], rax
0082CD41  E8 FA 4C 0C 00                  call 0x1408f1a40
0082CD46  85 C0                           test eax, eax
0082CD48  0F 88 A7 00 00 00               js 0x14082cdf5
0082CD4E  48 8B D7                        mov rdx, rdi
0082CD51  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0082CD55  E8 06 6C C3 FF                  call 0x140463960
0082CD5A  85 C0                           test eax, eax
0082CD5C  0F 88 93 00 00 00               js 0x14082cdf5
0082CD62  0F B7 75 F2                     movzx esi, word ptr [rbp - 0xe]
0082CD66  D1 EE                           shr esi, 1
0082CD68  44 38 B3 94 05 00 00            cmp byte ptr [rbx + 0x594], r14b
0082CD6F  74 19                           je 0x14082cd8a
0082CD71  4C 8D 4D 48                     lea r9, [rbp + 0x48]
0082CD75  48 8B D7                        mov rdx, rdi
0082CD78  49 8B CD                        mov rcx, r13
0082CD7B  E8 60 54 1C 00                  call 0x1409f21e0
0082CD80  85 C0                           test eax, eax
0082CD82  78 71                           js 0x14082cdf5
0082CD84  44 38 75 48                     cmp byte ptr [rbp + 0x48], r14b
0082CD88  74 6B                           je 0x14082cdf5
0082CD8A  48 8B 83 98 05 00 00            mov rax, qword ptr [rbx + 0x598]
0082CD91  48 85 C0                        test rax, rax
0082CD94  74 1C                           je 0x14082cdb2
0082CD96  4C 8B 8B A0 05 00 00            mov r9, qword ptr [rbx + 0x5a0]
0082CD9D  41 B8 03 00 00 00               mov r8d, 3
0082CDA3  48 8B D7                        mov rdx, rdi
0082CDA6  49 8B CD                        mov rcx, r13
0082CDA9  E8 22 DD E8 FF                  call 0x1406baad0
0082CDAE  84 C0                           test al, al
0082CDB0  74 43                           je 0x14082cdf5
0082CDB2  01 B3 B4 05 00 00               add dword ptr [rbx + 0x5b4], esi
0082CDB8  8B 83 B0 05 00 00               mov eax, dword ptr [rbx + 0x5b0]
0082CDBE  3B C6                           cmp eax, esi
0082CDC0  76 33                           jbe 0x14082cdf5
0082CDC2  48 8B 8B A8 05 00 00            mov rcx, qword ptr [rbx + 0x5a8]
0082CDC9  8B D0                           mov edx, eax
0082CDCB  C7 44 24 28 00 09 00 00         mov dword ptr [rsp + 0x28], 0x900
0082CDD3  45 33 C9                        xor r9d, r9d
0082CDD6  4C 8B C7                        mov r8, rdi
0082CDD9  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0082CDDE  E8 DD 13 BF FF                  call 0x14041e1c0
0082CDE3  8B C6                           mov eax, esi
0082CDE5  48 03 C0                        add rax, rax
0082CDE8  48 01 83 A8 05 00 00            add qword ptr [rbx + 0x5a8], rax
0082CDEF  29 B3 B0 05 00 00               sub dword ptr [rbx + 0x5b0], esi
0082CDF5  48 85 FF                        test rdi, rdi
0082CDF8  74 0A                           je 0x14082ce04
0082CDFA  33 D2                           xor edx, edx
0082CDFC  48 8B CF                        mov rcx, rdi
0082CDFF  E8 6C 5A 35 00                  call 0x140b82870
0082CE04  4D 85 FF                        test r15, r15
0082CE07  74 0A                           je 0x14082ce13
0082CE09  33 D2                           xor edx, edx
0082CE0B  49 8B CF                        mov rcx, r15
0082CE0E  E8 5D 5A 35 00                  call 0x140b82870
0082CE13  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
0082CE17  48 85 C9                        test rcx, rcx
0082CE1A  74 05                           je 0x14082ce21
0082CE1C  E8 8F 04 E8 FF                  call 0x1406ad2b0
0082CE21  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
0082CE29  33 C0                           xor eax, eax
0082CE2B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0082CE2F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0082CE33  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0082CE37  49 8B E3                        mov rsp, r11
0082CE3A  41 5F                           pop r15
0082CE3C  41 5E                           pop r14
0082CE3E  41 5D                           pop r13
0082CE40  41 5C                           pop r12
0082CE42  5D                              pop rbp
0082CE43  C3                              ret
0082CE44  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmDeviceClassesSubkeyCallback(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int16 v_stack_m36;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (128);
    a4 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_p20 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m48 = v_xmm1;
    v_stack_m58 = v_xmm0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) - ((unsigned int)(a4 + 1)));
    if (condition_is_equal) goto loc_0082C9EC;
    v_rsi = (v_rsi) | (-1);
    result = (unsigned int)((result) - ((unsigned int)(a4 + 1)));
    if (condition_is_equal) goto loc_0082C9B9;
    if (((unsigned int)(result)) != ((unsigned int)(a4 + 1))) goto loc_0082C9DA;
loc_0082C9B9:
loc_0082C9BC:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(a3 + result * 2)) != 0) goto loc_0082C9BC;
    if (result < (a4 + 1)) goto loc_0082CE21;
    if ((*(unsigned __int16 *)(a3)) != 35) goto loc_0082CE21;
loc_0082C9DA:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) < 3) goto loc_0082CA12;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) != 3) goto loc_0082CA43;
    if ((*(unsigned __int8 *)(a4 + 1428)) == 0) goto loc_0082CA43;
    goto loc_0082CA12;
loc_0082C9EC:
    v_rsi = (v_rsi) | (-1);
loc_0082C9F3:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(a3 + result * 2)) != 0) goto loc_0082C9F3;
    if (result != 38) goto loc_0082CE21;
    if ((*(unsigned __int16 *)(a3)) != 123) goto loc_0082CE21;
loc_0082CA12:
    v_stack_m80 = v_stack_m70;
    v_stack_m88 = 0x20019ULL;
    result = PnpCtxRegOpenKey(a1, a2, a3, 8);
    a4 = 0;
    if (sign_flag) goto loc_0082CE13;
loc_0082CA43:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) >= 3) goto loc_0082CB21;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) != 2) goto loc_0082CB42;
    if ((*(unsigned __int16 *)(a4 + 1012)) == 0) goto loc_0082CB42;
    result = ExAllocatePool2(256, 400, (unsigned int)(0x52504E50ULL), a4);
    if (result == 0) goto loc_0082CE13;
    v_stack_m80 = v_stack_m74;
    v_stack_m88 = result;
    v_stack_m74 = 400;
    result = PnpCtxRegQueryValue(256, v_stack_m70, v_rip + 3018063, v_stack_m78);
    a1 = 0;
    if (sign_flag) goto loc_0082CE09;
    if (v_stack_m78 != ((unsigned int)(a1 + 1))) goto loc_0082CE09;
    if (v_stack_m74 < 2) goto loc_0082CE09;
    *(unsigned __int16 *)(result + 398) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m48, result, v_rip + 3018063, v_stack_m78);
    if (sign_flag) goto loc_0082CE09;
    result = RtlInitUnicodeStringEx(v_stack_m58, a4 + 1012, v_rip + 3018063, v_stack_m78);
    if (sign_flag) goto loc_0082CE09;
    result = RtlEqualUnicodeString(v_stack_m48, v_stack_m58, 1, v_stack_m78);
    if ((unsigned __int8)(result) == 0) goto loc_0082CE09;
    goto loc_0082CB47;
loc_0082CB21:
    if ((unsigned __int8)(result) != 0) goto loc_0082CB42;
loc_0082CB23:
    v_rsi = (1) + 1;
    if ((*(unsigned __int16 *)(a3 + v_rsi * 2)) != ((unsigned __int16)(v_stack_m78))) goto loc_0082CB23;
    if (v_rsi <= 1) goto loc_0082CB47;
    v_r12 = 0;
    if ((*(unsigned __int16 *)(a3)) == 35) { v_r12 = 1; }
    goto loc_0082CB47;
loc_0082CB42:
loc_0082CB47:
    if ((*(unsigned int *)(a4)) < 2) goto loc_0082CBEB;
    result = ExAllocatePool2(256, (unsigned int)(0x3F0ULL), (unsigned int)(0x52504E50ULL), v_stack_m78);
    a4 = 0;
    if (result == 0) goto loc_0082CE04;
    if ((*(unsigned __int16 *)(a4 + 4)) == 0) goto loc_0082CBBB;
    v_stack_m80 = 0x900ULL;
    v_stack_m88 = v_stack_m60;
    result = RtlStringCchCopyExW(result, 504, a4 + 4, v_stack_m68);
    a1 = 0;
    if (sign_flag) goto loc_0082CDFA;
    a2 = (v_stack_m60) - 1;
    *(unsigned __int16 *)(v_stack_m68) = 0;
    goto loc_0082CBBE;
loc_0082CBBB:
loc_0082CBBE:
    if ((*(unsigned int *)(a4)) == 2) goto loc_0082CBC8;
    if (((unsigned __int8)(v_r12)) != 1) goto loc_0082CBEB;
loc_0082CBC8:
    result = RtlStringCchCopyW(result, a2, a3, v_stack_m68);
    v_r14 = 0;
    if (sign_flag) goto loc_0082CDFA;
    if (((unsigned __int8)(v_r12)) != 1) goto loc_0082CBEE;
    *(unsigned __int16 *)(result) = 92;
    goto loc_0082CBEE;
loc_0082CBEB:
    v_r14 = 0;
loc_0082CBEE:
    if ((*(unsigned int *)(a4)) >= 3) goto loc_0082CD34;
    result = ExAllocatePool2(256, (unsigned int)(0x5B8ULL), (unsigned int)(0x52504E50ULL), v_stack_m68);
    if (result == 0) goto loc_0082CDF5;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) + 1);
    v_stack_m80 = (unsigned int)((unsigned int)(0x900ULL));
    *(unsigned int *)(result) = (unsigned int)(a1);
    a4 = 0;
    v_stack_m88 = 0;
    result = RtlStringCchCopyExW(result + 4, 504, result, a4);
    v_stack_m80 = (unsigned int)((unsigned int)(0x900ULL));
    v_stack_m88 = 0;
    a4 = 0;
    result = RtlStringCchCopyExW(result + 1012, 200, a4 + 1012, a4);
    *(unsigned __int64 *)(result + 1416) = *(unsigned __int64 *)(a4 + 1416);
    *(unsigned int *)(result + 1424) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 1424)));
    *(unsigned __int8 *)(result + 1428) = (unsigned __int8)(*(unsigned __int8 *)(a4 + 1428));
    *(unsigned __int64 *)(result + 1432) = *(unsigned __int64 *)(a4 + 1432);
    *(unsigned __int64 *)(result + 1440) = *(unsigned __int64 *)(a4 + 1440);
    *(unsigned __int64 *)(result + 1448) = *(unsigned __int64 *)(a4 + 1448);
    *(unsigned int *)(result + 1456) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 1456)));
    *(unsigned int *)(result + 1460) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 1460)));
    result = PnpCtxRegEnumKeyWithCallback(a1, v_stack_m70, v_rip - 821, result);
    a2 = 0;
    *(unsigned __int64 *)(a4 + 1416) = *(unsigned __int64 *)(result + 1416);
    *(unsigned int *)(a4 + 1424) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 1424)));
    *(unsigned int *)(a4 + 1460) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 1460)));
    *(unsigned __int64 *)(a4 + 1448) = *(unsigned __int64 *)(result + 1448);
    *(unsigned int *)(a4 + 1456) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 1456)));
    result = ExFreePoolWithTag(result, a2, v_rip - 821, result);
    goto loc_0082CDF5;
loc_0082CD34:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rip + 3016613);
    result = CmValidateDeviceInterfaceName(result, result, v_rip - 821, result);
    if (sign_flag) goto loc_0082CDF5;
    result = RtlInitUnicodeStringEx(v_stack_m38, result, v_rip - 821, result);
    if (sign_flag) goto loc_0082CDF5;
    v_rsi = (unsigned int)((v_stack_m36) >> (1));
    if ((*(unsigned __int8 *)(a4 + 1428)) == 0) goto loc_0082CD8A;
    result = CmIsDeviceInterfaceEnabled(a1, result, v_rip - 821, v_stack_p20);
    if (sign_flag) goto loc_0082CDF5;
    if (v_stack_p20 == 0) goto loc_0082CDF5;
loc_0082CD8A:
    if (*(unsigned __int64 *)(a4 + 1432) == 0) goto loc_0082CDB2;
    result = guard_dispatch_icall(a1, result, 3, *(unsigned __int64 *)(a4 + 1440));
    if ((unsigned __int8)(result) == 0) goto loc_0082CDF5;
loc_0082CDB2:
    result = (unsigned int)(*(unsigned int *)(a4 + 1456));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 1456)))) >= = ((unsigned int)(v_rsi))) {
        a1 = *(unsigned __int64 *)(a4 + 1448);
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 1456)));
        v_stack_m80 = 0x900ULL;
        a4 = 0;
        a3 = result;
        v_stack_m88 = 0;
        result = RtlStringCchCopyExW(a1, a2, a3, a4);
        result = (unsigned int)(v_rsi);
        result = (result) + (result);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m70 != 0) {
        result = ZwClose(v_stack_m70, a2, a3, a4);
    }
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmDeviceClassesSubkeyCallback(int64_t Arg1, int64_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint16_t v_stack_m36;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (128);
    Arg4 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_p20 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m48 = v_xmm1;
    v_stack_m58 = v_xmm0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) - ((uint32_t)(Arg4 + 1)));
    if (condition_is_equal) goto loc_0082C9EC;
    local_rsi = (local_rsi) | (-1);
    result = (uint32_t)((result) - ((uint32_t)(Arg4 + 1)));
    if (condition_is_equal) goto loc_0082C9B9;
    if (((uint32_t)(result)) != ((uint32_t)(Arg4 + 1))) goto loc_0082C9DA;
loc_0082C9B9:
loc_0082C9BC:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(arg3 + result * 2)) != 0) goto loc_0082C9BC;
    if (result < (Arg4 + 1)) goto loc_0082CE21;
    if ((*(uint16_t *)(arg3)) != 35) goto loc_0082CE21;
loc_0082C9DA:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) < 3) goto loc_0082CA12;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) != 3) goto loc_0082CA43;
    if ((*(uint8_t *)(arg4 + 0x594)) == 0) goto loc_0082CA43;
    goto loc_0082CA12;
loc_0082C9EC:
    local_rsi = (local_rsi) | (-1);
loc_0082C9F3:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(arg3 + result * 2)) != 0) goto loc_0082C9F3;
    if (result != 38) goto loc_0082CE21;
    if ((*(uint16_t *)(arg3)) != 123) goto loc_0082CE21;
loc_0082CA12:
    v_stack_m80 = v_stack_m70;
    v_stack_m88 = 0x20019ULL;
    result = PnpCtxRegOpenKey(Arg1, Arg2, Arg3, 8);
    Arg4 = 0;
    if (sign_flag) goto loc_0082CE13;
loc_0082CA43:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) >= 3) goto loc_0082CB21;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) != 2) goto loc_0082CB42;
    if ((*(uint16_t *)(arg4 + 0x3F4)) == 0) goto loc_0082CB42;
    result = ExAllocatePool2(256, 400, (uint32_t)(0x52504E50ULL), Arg4);
    if (result == 0) goto loc_0082CE13;
    v_stack_m80 = v_stack_m74;
    v_stack_m88 = result;
    v_stack_m74 = 400;
    result = PnpCtxRegQueryValue(256, v_stack_m70, v_rip + 3018063, v_stack_m78);
    Arg1 = 0;
    if (sign_flag) goto loc_0082CE09;
    if (v_stack_m78 != ((uint32_t)(Arg1 + 1))) goto loc_0082CE09;
    if (v_stack_m74 < 2) goto loc_0082CE09;
    *(uint16_t *)(result + 0x18E) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m48, result, v_rip + 3018063, v_stack_m78);
    if (sign_flag) goto loc_0082CE09;
    result = RtlInitUnicodeStringEx(v_stack_m58, Arg4 + 1012, v_rip + 3018063, v_stack_m78);
    if (sign_flag) goto loc_0082CE09;
    result = RtlEqualUnicodeString(v_stack_m48, v_stack_m58, 1, v_stack_m78);
    if ((uint8_t)(result) == 0) goto loc_0082CE09;
    goto loc_0082CB47;
loc_0082CB21:
    if ((uint8_t)(result) != 0) goto loc_0082CB42;
loc_0082CB23:
    local_rsi = (1) + 1;
    if ((*(uint16_t *)(arg3 + local_rsi * 2)) != ((uint16_t)(v_stack_m78))) goto loc_0082CB23;
    if (local_rsi <= 1) goto loc_0082CB47;
    local_r12 = 0;
    if ((*(uint16_t *)(arg3)) == 35) { local_r12 = 1; }
    goto loc_0082CB47;
loc_0082CB42:
loc_0082CB47:
    if ((*(uint32_t *)(arg4)) < 2) goto loc_0082CBEB;
    result = ExAllocatePool2(256, (uint32_t)(0x3F0ULL), (uint32_t)(0x52504E50ULL), v_stack_m78);
    Arg4 = 0;
    if (result == 0) goto loc_0082CE04;
    if ((*(uint16_t *)(arg4 + 0x4)) == 0) goto loc_0082CBBB;
    v_stack_m80 = 0x900ULL;
    v_stack_m88 = v_stack_m60;
    result = RtlStringCchCopyExW(result, 504, Arg4 + 4, v_stack_m68);
    Arg1 = 0;
    if (sign_flag) goto loc_0082CDFA;
    Arg2 = (v_stack_m60) - 1;
    *(uint16_t *)(v_stack_m68) = 0;
    goto loc_0082CBBE;
loc_0082CBBB:
loc_0082CBBE:
    if ((*(uint32_t *)(arg4)) == 2) goto loc_0082CBC8;
    if (((uint8_t)(local_r12)) != 1) goto loc_0082CBEB;
loc_0082CBC8:
    result = RtlStringCchCopyW(result, Arg2, Arg3, v_stack_m68);
    local_r14 = 0;
    if (sign_flag) goto loc_0082CDFA;
    if (((uint8_t)(local_r12)) != 1) goto loc_0082CBEE;
    *(uint16_t *)(result) = 92;
    goto loc_0082CBEE;
loc_0082CBEB:
    local_r14 = 0;
loc_0082CBEE:
    if ((*(uint32_t *)(arg4)) >= 3) goto loc_0082CD34;
    result = ExAllocatePool2(256, (uint32_t)(0x5B8ULL), (uint32_t)(0x52504E50ULL), v_stack_m68);
    if (result == 0) goto loc_0082CDF5;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) + 1);
    v_stack_m80 = (uint32_t)((uint32_t)(0x900ULL));
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    Arg4 = 0;
    v_stack_m88 = 0;
    result = RtlStringCchCopyExW(result + 4, 504, result, Arg4);
    v_stack_m80 = (uint32_t)((uint32_t)(0x900ULL));
    v_stack_m88 = 0;
    Arg4 = 0;
    result = RtlStringCchCopyExW(result + 1012, 200, Arg4 + 1012, Arg4);
    *(uint64_t *)(result + 0x588) = *(uint64_t *)(arg4 + 0x588);
    *(uint32_t *)(result + 0x590) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x590)));
    *(uint8_t *)(result + 0x594) = (uint8_t)(*(uint8_t *)(arg4 + 0x594));
    *(uint64_t *)(result + 0x598) = *(uint64_t *)(arg4 + 0x598);
    *(uint64_t *)(result + 0x5A0) = *(uint64_t *)(arg4 + 0x5A0);
    *(uint64_t *)(result + 0x5A8) = *(uint64_t *)(arg4 + 0x5A8);
    *(uint32_t *)(result + 0x5B0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x5B0)));
    *(uint32_t *)(result + 0x5B4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x5B4)));
    result = PnpCtxRegEnumKeyWithCallback(Arg1, v_stack_m70, v_rip - 821, result);
    Arg2 = 0;
    *(uint64_t *)(arg4 + 0x588) = *(uint64_t *)(result + 0x588);
    *(uint32_t *)(arg4 + 0x590) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x590)));
    *(uint32_t *)(arg4 + 0x5B4) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x5B4)));
    *(uint64_t *)(arg4 + 0x5A8) = *(uint64_t *)(result + 0x5A8);
    *(uint32_t *)(arg4 + 0x5B0) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x5B0)));
    result = ExFreePoolWithTag(result, Arg2, v_rip - 821, result);
    goto loc_0082CDF5;
loc_0082CD34:
    *(uint64_t *)(result) = *(uint64_t *)(v_rip + 0x2E07A5);
    result = CmValidateDeviceInterfaceName(result, result, v_rip - 821, result);
    if (sign_flag) goto loc_0082CDF5;
    result = RtlInitUnicodeStringEx(v_stack_m38, result, v_rip - 821, result);
    if (sign_flag) goto loc_0082CDF5;
    local_rsi = (uint32_t)((v_stack_m36) >> (1));
    if ((*(uint8_t *)(arg4 + 0x594)) == 0) goto loc_0082CD8A;
    result = CmIsDeviceInterfaceEnabled(Arg1, result, v_rip - 821, v_stack_p20);
    if (sign_flag) goto loc_0082CDF5;
    if (v_stack_p20 == 0) goto loc_0082CDF5;
loc_0082CD8A:
    if (*(uint64_t *)(arg4 + 0x598) == 0) goto loc_0082CDB2;
    result = guard_dispatch_icall(Arg1, result, 3, *(uint64_t *)(arg4 + 0x5A0));
    if ((uint8_t)(result) == 0) goto loc_0082CDF5;
loc_0082CDB2:
    result = (uint32_t)(*(uint32_t *)(arg4 + 0x5B0));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x5B0)))) >= = ((uint32_t)(local_rsi))) {
        Arg1 = *(uint64_t *)(arg4 + 0x5A8);
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x5B0)));
        v_stack_m80 = 0x900ULL;
        Arg4 = 0;
        Arg3 = result;
        v_stack_m88 = 0;
        result = RtlStringCchCopyExW(Arg1, Arg2, Arg3, Arg4);
        result = (uint32_t)(local_rsi);
        result = (result) + (result);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m70 != 0) {
        result = ZwClose(v_stack_m70, Arg2, Arg3, Arg4);
    }
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x0 + rax*2` | `16` | `R` |
| `Arg3` | `+ 0x0 + rsi*2` | `16` | `R` |
| `Arg4` | `+ 0x0` | `16` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x4` | `64` | `R` |
| `Arg4` | `+ 0x3F4` | `64` | `R` |
| `Arg4` | `+ 0x588` | `64` | `R` |
| `Arg4` | `+ 0x588` | `64` | `W` |
| `Arg4` | `+ 0x590` | `32` | `R` |
| `Arg4` | `+ 0x590` | `32` | `W` |
| `Arg4` | `+ 0x594` | `8` | `R` |
| `Arg4` | `+ 0x598` | `64` | `R` |
| `Arg4` | `+ 0x5A0` | `64` | `R` |
| `Arg4` | `+ 0x5A8` | `64` | `R` |
| `Arg4` | `+ 0x5A8` | `64` | `R/W` |
| `Arg4` | `+ 0x5A8` | `64` | `W` |
| `Arg4` | `+ 0x5B0` | `32` | `R` |
| `Arg4` | `+ 0x5B0` | `32` | `R/W` |
| `Arg4` | `+ 0x5B0` | `32` | `W` |
| `Arg4` | `+ 0x5B4` | `32` | `R` |
| `Arg4` | `+ 0x5B4` | `32` | `R/W` |
| `Arg4` | `+ 0x5B4` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0082C940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
