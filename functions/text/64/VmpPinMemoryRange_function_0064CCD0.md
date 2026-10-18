# VmpPinMemoryRange

- RVA: `0x0064CCD0`–`0x0064D1B7` (길이 `1,255` bytes)
- VA: `0x000000014064CCD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2E44`
- 디코드: `353`개 명령, `1,255/1,255` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0064CD65` → [VmpCheckPinTooLate](../../page/7A/VmpCheckPinTooLate_function_007AD990.md) (function, `0x007AD990`)
- `0x0064CD75` → [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) (function, `0x003147A4`)
- `0x0064CE30` → [VmpCountNewPinnedRangesNeeded](VmpCountNewPinnedRangesNeeded_function_0064C62C.md) (function, `0x0064C62C`)
- `0x0064CE5F` → [VmpProcessContextUnlockExclusive](../48/VmpProcessContextUnlockExclusive_function_004894C8.md) (function, `0x004894C8`)
- `0x0064CE73` → [VmpAllocatePinnedRanges](../../page/7A/VmpAllocatePinnedRanges_function_007AD8FC.md) (function, `0x007AD8FC`)
- `0x0064CEA5` → [VmpSecureMemoryForPin](../../page/7A/VmpSecureMemoryForPin_function_007ADED4.md) (function, `0x007ADED4`)
- `0x0064CEC4` → [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) (function, `0x003147A4`)
- `0x0064CF2F` → [VmpCheckPinAndReference](VmpCheckPinAndReference_function_0064C44C.md) (function, `0x0064C44C`)
- `0x0064CF5F` → [VmpProcessContextUnlockExclusive](../48/VmpProcessContextUnlockExclusive_function_004894C8.md) (function, `0x004894C8`)
- `0x0064CF7E` → [MmLockPhysicalPagesByVa](../../page/7F/MmLockPhysicalPagesByVa_function_007FB930.md) (function, `0x007FB930`)
- `0x0064CF99` → [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) (function, `0x003147A4`)
- `0x0064CFC7` → [VmpCheckPinAndReference](VmpCheckPinAndReference_function_0064C44C.md) (function, `0x0064C44C`)
- `0x0064CFE8` → [VmpCountNewPinnedRangesNeeded](VmpCountNewPinnedRangesNeeded_function_0064C62C.md) (function, `0x0064C62C`)
- `0x0064D015` → [VmpUpdatePinRangesForFirstPin](VmpUpdatePinRangesForFirstPin_function_0064D7AC.md) (function, `0x0064D7AC`)
- `0x0064D058` → [VmpProcessContextUnlockExclusive](../48/VmpProcessContextUnlockExclusive_function_004894C8.md) (function, `0x004894C8`)
- `0x0064D092` → [VmAccessFault](../../page/A1/VmAccessFault_function_00A18BF0.md) (function, `0x00A18BF0`)
- `0x0064D0B5` → [VmpProcessContextUnlockExclusive](../48/VmpProcessContextUnlockExclusive_function_004894C8.md) (function, `0x004894C8`)
- `0x0064D0D0` → [MmUnlockPhysicalPagesByVa](../../page/7F/MmUnlockPhysicalPagesByVa_function_007FBA3C.md) (function, `0x007FBA3C`)
- `0x0064D0E8` → [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) (function, `0x003147A4`)
- `0x0064D0F3` → [VmpDereferencePinInProgress](VmpDereferencePinInProgress_function_0064C7C4.md) (function, `0x0064C7C4`)
- `0x0064D10E` → [VmpProcessContextUnlockExclusive](../48/VmpProcessContextUnlockExclusive_function_004894C8.md) (function, `0x004894C8`)
- `0x0064D131` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (function, `0x007AE05C`)
- `0x0064D152` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (function, `0x007AE05C`)
- `0x0064D185` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0064D19D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [VmPinMemoryRange](../../page/7A/VmPinMemoryRange_function_007AD450.md) at `0x007AD53C`
- [VmPinMemoryRange](../../page/7A/VmPinMemoryRange_function_007AD450.md) at `0x007AD59D`

### Static image references
- `0x0064CCE9` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0064CD65` → [VmpCheckPinTooLate](../../page/7A/VmpCheckPinTooLate_function_007AD990.md) (`.text` → `PAGE`)
  - `0x0064CE73` → [VmpAllocatePinnedRanges](../../page/7A/VmpAllocatePinnedRanges_function_007AD8FC.md) (`.text` → `PAGE`)
  - `0x0064CEA5` → [VmpSecureMemoryForPin](../../page/7A/VmpSecureMemoryForPin_function_007ADED4.md) (`.text` → `PAGE`)
  - `0x0064CF7E` → [MmLockPhysicalPagesByVa](../../page/7F/MmLockPhysicalPagesByVa_function_007FB930.md) (`.text` → `PAGE`)
  - `0x0064D092` → [VmAccessFault](../../page/A1/VmAccessFault_function_00A18BF0.md) (`.text` → `PAGE`)
  - `0x0064D0D0` → [MmUnlockPhysicalPagesByVa](../../page/7F/MmUnlockPhysicalPagesByVa_function_007FBA3C.md) (`.text` → `PAGE`)
  - `0x0064D131` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (`.text` → `PAGE`)
  - `0x0064D152` → [VmpUnsecureMemoryForPin](../../page/7A/VmpUnsecureMemoryForPin_function_007AE05C.md) (`.text` → `PAGE`)
  - `0x0064D185` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064CCD0  40 55                           push rbp
0064CCD2  53                              push rbx
0064CCD3  56                              push rsi
0064CCD4  57                              push rdi
0064CCD5  41 54                           push r12
0064CCD7  41 55                           push r13
0064CCD9  41 56                           push r14
0064CCDB  41 57                           push r15
0064CCDD  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
0064CCE2  48 81 EC D8 00 00 00            sub rsp, 0xd8
0064CCE9  48 8B 05 50 DA 7B 00            mov rax, qword ptr [rip + 0x7bda50]
0064CCF0  48 33 C4                        xor rax, rsp
0064CCF3  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0064CCF7  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
0064CCFC  49 8B C0                        mov rax, r8
0064CCFF  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0064CD03  45 33 ED                        xor r13d, r13d
0064CD06  44 21 6C 24 44                  and dword ptr [rsp + 0x44], r13d
0064CD0B  48 8B D9                        mov rbx, rcx
0064CD0E  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0064CD12  33 FF                           xor edi, edi
0064CD14  4C 21 6D 87                     and qword ptr [rbp - 0x79], r13
0064CD18  0F 57 C0                        xorps xmm0, xmm0
0064CD1B  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0064CD1F  4C 8B E2                        mov r12, rdx
0064CD22  33 C0                           xor eax, eax
0064CD24  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
0064CD28  21 39                           and dword ptr [rcx], edi
0064CD2A  45 33 FF                        xor r15d, r15d
0064CD2D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0064CD32  48 8B CB                        mov rcx, rbx
0064CD35  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0064CD39  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064CD3D  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0064CD41  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064CD45  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0064CD49  49 8D 41 FF                     lea rax, [r9 - 1]
0064CD4D  48 03 C2                        add rax, rdx
0064CD50  4C 89 4D CF                     mov qword ptr [rbp - 0x31], r9
0064CD54  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
0064CD58  48 89 55 9F                     mov qword ptr [rbp - 0x61], rdx
0064CD5C  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0064CD60  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
0064CD65  E8 26 0C 16 00                  call 0x1407ad990
0064CD6A  44 8B F0                        mov r14d, eax
0064CD6D  85 C0                           test eax, eax
0064CD6F  0F 88 9E 03 00 00               js 0x14064d113
0064CD75  E8 2A 7A CC FF                  call 0x1403147a4
0064CD7A  48 8B F0                        mov rsi, rax
0064CD7D  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0064CD81  48 39 43 68                     cmp qword ptr [rbx + 0x68], rax
0064CD85  74 02                           je 0x14064cd89
0064CD87  CD 2C                           int 0x2c
0064CD89  48 8D 53 08                     lea rdx, [rbx + 8]
0064CD8D  F6 42 08 01                     test byte ptr [rdx + 8], 1
0064CD91  48 8B 0A                        mov rcx, qword ptr [rdx]
0064CD94  74 08                           je 0x14064cd9e
0064CD96  48 85 C9                        test rcx, rcx
0064CD99  74 03                           je 0x14064cd9e
0064CD9B  48 33 CA                        xor rcx, rdx
0064CD9E  0F B6 42 08                     movzx eax, byte ptr [rdx + 8]
0064CDA2  83 E0 01                        and eax, 1
0064CDA5  EB 26                           jmp 0x14064cdcd
0064CDA7  4C 3B 61 20                     cmp r12, qword ptr [rcx + 0x20]
0064CDAB  76 06                           jbe 0x14064cdb3
0064CDAD  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0064CDB1  EB 09                           jmp 0x14064cdbc
0064CDB3  4C 3B 61 18                     cmp r12, qword ptr [rcx + 0x18]
0064CDB7  73 19                           jae 0x14064cdd2
0064CDB9  48 8B 11                        mov rdx, qword ptr [rcx]
0064CDBC  85 C0                           test eax, eax
0064CDBE  74 0A                           je 0x14064cdca
0064CDC0  48 85 D2                        test rdx, rdx
0064CDC3  74 05                           je 0x14064cdca
0064CDC5  48 33 CA                        xor rcx, rdx
0064CDC8  EB 03                           jmp 0x14064cdcd
0064CDCA  48 8B CA                        mov rcx, rdx
0064CDCD  48 85 C9                        test rcx, rcx
0064CDD0  75 D5                           jne 0x14064cda7
0064CDD2  48 8D 41 E8                     lea rax, [rcx - 0x18]
0064CDD6  48 F7 D9                        neg rcx
0064CDD9  4D 1B ED                        sbb r13, r13
0064CDDC  4C 23 E8                        and r13, rax
0064CDDF  75 02                           jne 0x14064cde3
0064CDE1  CD 2C                           int 0x2c
0064CDE3  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
0064CDE7  49 39 55 38                     cmp qword ptr [r13 + 0x38], rdx
0064CDEB  73 02                           jae 0x14064cdef
0064CDED  CD 2C                           int 0x2c
0064CDEF  49 8B 7D 10                     mov rdi, qword ptr [r13 + 0x10]
0064CDF3  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
0064CDF7  49 2B C4                        sub rax, r12
0064CDFA  48 03 45 B7                     add rax, qword ptr [rbp - 0x49]
0064CDFE  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0064CE02  48 3B C8                        cmp rcx, rax
0064CE05  74 02                           je 0x14064ce09
0064CE07  CD 2C                           int 0x2c
0064CE09  4C 8B 7F 20                     mov r15, qword ptr [rdi + 0x20]
0064CE0D  4C 8B C2                        mov r8, rdx
0064CE10  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
0064CE13  4C 2B F9                        sub r15, rcx
0064CE16  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
0064CE1A  49 FF C7                        inc r15
0064CE1D  83 E0 02                        and eax, 2
0064CE20  41 BC 00 00 00 00               mov r12d, 0
0064CE26  48 8B CB                        mov rcx, rbx
0064CE29  89 45 93                        mov dword ptr [rbp - 0x6d], eax
0064CE2C  41 0F 95 C4                     setne r12b
0064CE30  E8 F7 F7 FF FF                  call 0x14064c62c
0064CE35  33 C9                           xor ecx, ecx
0064CE37  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0064CE3B  4C 8B F0                        mov r14, rax
0064CE3E  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
0064CE42  48 85 C0                        test rax, rax
0064CE45  0F 94 C1                        sete cl
0064CE48  89 4D 8F                        mov dword ptr [rbp - 0x71], ecx
0064CE4B  4D 85 F6                        test r14, r14
0064CE4E  75 09                           jne 0x14064ce59
0064CE50  48 85 C0                        test rax, rax
0064CE53  0F 85 B0 00 00 00               jne 0x14064cf09
0064CE59  48 8B D6                        mov rdx, rsi
0064CE5C  48 8B CB                        mov rcx, rbx
0064CE5F  E8 64 C6 E3 FF                  call 0x1404894c8
0064CE64  4D 85 F6                        test r14, r14
0064CE67  74 28                           je 0x14064ce91
0064CE69  4D 8B C6                        mov r8, r14
0064CE6C  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0064CE70  48 8B CB                        mov rcx, rbx
0064CE73  E8 84 0A 16 00                  call 0x1407ad8fc
0064CE78  44 8B F0                        mov r14d, eax
0064CE7B  85 C0                           test eax, eax
0064CE7D  0F 88 D4 02 00 00               js 0x14064d157
0064CE83  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0064CE87  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
0064CE8B  33 C0                           xor eax, eax
0064CE8D  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0064CE91  83 7D 8F 00                     cmp dword ptr [rbp - 0x71], 0
0064CE95  74 25                           je 0x14064cebc
0064CE97  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0064CE9B  4C 8D 4D C7                     lea r9, [rbp - 0x39]
0064CE9F  4D 8B C7                        mov r8, r15
0064CEA2  48 8B CB                        mov rcx, rbx
0064CEA5  E8 2A 10 16 00                  call 0x1407aded4
0064CEAA  44 8B F0                        mov r14d, eax
0064CEAD  85 C0                           test eax, eax
0064CEAF  78 38                           js 0x14064cee9
0064CEB1  4C 8B 75 C7                     mov r14, qword ptr [rbp - 0x39]
0064CEB5  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
0064CEBA  EB 05                           jmp 0x14064cec1
0064CEBC  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0064CEC1  48 8B CB                        mov rcx, rbx
0064CEC4  E8 DB 78 CC FF                  call 0x1403147a4
0064CEC9  48 8B F0                        mov rsi, rax
0064CECC  33 C0                           xor eax, eax
0064CECE  48 39 47 38                     cmp qword ptr [rdi + 0x38], rax
0064CED2  75 35                           jne 0x14064cf09
0064CED4  4D 85 F6                        test r14, r14
0064CED7  75 1E                           jne 0x14064cef7
0064CED9  4C 8B 75 BF                     mov r14, qword ptr [rbp - 0x41]
0064CEDD  C7 45 8F 01 00 00 00            mov dword ptr [rbp - 0x71], 1
0064CEE4  E9 70 FF FF FF                  jmp 0x14064ce59
0064CEE9  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
0064CEED  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0064CEF2  E9 21 02 00 00                  jmp 0x14064d118
0064CEF7  4C 89 77 38                     mov qword ptr [rdi + 0x38], r14
0064CEFB  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0064CF00  39 45 93                        cmp dword ptr [rbp - 0x6d], eax
0064CF03  74 04                           je 0x14064cf09
0064CF05  83 4F 48 01                     or dword ptr [rdi + 0x48], 1
0064CF09  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
0064CF0D  48 8B D7                        mov rdx, rdi
0064CF10  4C 8B 4D 97                     mov r9, qword ptr [rbp - 0x69]
0064CF14  48 8B CB                        mov rcx, rbx
0064CF17  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
0064CF1B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0064CF20  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0064CF25  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0064CF2A  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0064CF2F  E8 18 F5 FF FF                  call 0x14064c44c
0064CF34  44 8B F0                        mov r14d, eax
0064CF37  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0064CF3B  45 85 F6                        test r14d, r14d
0064CF3E  0F 88 F1 00 00 00               js 0x14064d035
0064CF44  85 C0                           test eax, eax
0064CF46  0F 85 F1 00 00 00               jne 0x14064d03d
0064CF4C  4C 8B 77 38                     mov r14, qword ptr [rdi + 0x38]
0064CF50  48 8B D6                        mov rdx, rsi
0064CF53  48 FF 47 40                     inc qword ptr [rdi + 0x40]
0064CF57  48 8B CB                        mov rcx, rbx
0064CF5A  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0064CF5F  E8 64 C5 E3 FF                  call 0x1404894c8
0064CF64  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
0064CF68  45 8B CC                        mov r9d, r12d
0064CF6B  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
0064CF6F  4D 8B C6                        mov r8, r14
0064CF72  48 C1 E2 0C                     shl rdx, 0xc
0064CF76  48 83 CE FF                     or rsi, 0xffffffffffffffff
0064CF7A  48 C1 E1 0C                     shl rcx, 0xc
0064CF7E  E8 AD E9 1A 00                  call 0x1407fb930
0064CF83  44 8B F0                        mov r14d, eax
0064CF86  85 C0                           test eax, eax
0064CF88  0F 88 47 01 00 00               js 0x14064d0d5
0064CF8E  48 8B CB                        mov rcx, rbx
0064CF91  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
0064CF99  E8 06 78 CC FF                  call 0x1403147a4
0064CF9E  4C 8B 4D 97                     mov r9, qword ptr [rbp - 0x69]
0064CFA2  48 8B F0                        mov rsi, rax
0064CFA5  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
0064CFA9  48 8B D7                        mov rdx, rdi
0064CFAC  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
0064CFB0  48 8B CB                        mov rcx, rbx
0064CFB3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0064CFB8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0064CFBD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0064CFC2  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0064CFC7  E8 80 F4 FF FF                  call 0x14064c44c
0064CFCC  44 8B F0                        mov r14d, eax
0064CFCF  85 C0                           test eax, eax
0064CFD1  78 52                           js 0x14064d025
0064CFD3  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
0064CFD8  75 52                           jne 0x14064d02c
0064CFDA  4C 8B 75 9F                     mov r14, qword ptr [rbp - 0x61]
0064CFDE  48 8B CB                        mov rcx, rbx
0064CFE1  4C 8B 45 97                     mov r8, qword ptr [rbp - 0x69]
0064CFE5  49 8B D6                        mov rdx, r14
0064CFE8  E8 3F F6 FF FF                  call 0x14064c62c
0064CFED  48 39 45 87                     cmp qword ptr [rbp - 0x79], rax
0064CFF1  73 0F                           jae 0x14064d002
0064CFF3  41 BE 2D 02 00 C0               mov r14d, 0xc000022d
0064CFF9  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
0064CFFD  E9 A7 00 00 00                  jmp 0x14064d0a9
0064D002  4C 8B 45 97                     mov r8, qword ptr [rbp - 0x69]
0064D006  4C 8D 4D A7                     lea r9, [rbp - 0x59]
0064D00A  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
0064D00F  49 8B D6                        mov rdx, r14
0064D012  48 8B CB                        mov rcx, rbx
0064D015  E8 92 07 00 00                  call 0x14064d7ac
0064D01A  41 83 4D 40 01                  or dword ptr [r13 + 0x40], 1
0064D01F  48 FF 43 48                     inc qword ptr [rbx + 0x48]
0064D023  EB 23                           jmp 0x14064d048
0064D025  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
0064D02A  74 CD                           je 0x14064cff9
0064D02C  48 83 7F 40 01                  cmp qword ptr [rdi + 0x40], 1
0064D031  75 15                           jne 0x14064d048
0064D033  EB C4                           jmp 0x14064cff9
0064D035  85 C0                           test eax, eax
0064D037  0F 84 C0 00 00 00               je 0x14064d0fd
0064D03D  48 83 7F 40 00                  cmp qword ptr [rdi + 0x40], 0
0064D042  0F 84 B5 00 00 00               je 0x14064d0fd
0064D048  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0064D04D  48 8B D6                        mov rdx, rsi
0064D050  48 8B CB                        mov rcx, rbx
0064D053  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
0064D058  E8 6B C4 E3 FF                  call 0x1404894c8
0064D05D  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0064D061  48 8D 55 DF                     lea rdx, [rbp - 0x21]
0064D065  44 8B 4D 6F                     mov r9d, dword ptr [rbp + 0x6f]
0064D069  48 8D 4D E7                     lea rcx, [rbp - 0x19]
0064D06D  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0064D071  41 B8 01 00 00 00               mov r8d, 1
0064D077  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0064D07B  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0064D07F  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0064D083  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0064D088  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
0064D08D  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
0064D092  E8 59 BB 3C 00                  call 0x140a18bf0
0064D097  45 33 F6                        xor r14d, r14d
0064D09A  48 83 CE FF                     or rsi, 0xffffffffffffffff
0064D09E  44 39 74 24 44                  cmp dword ptr [rsp + 0x44], r14d
0064D0A3  74 30                           je 0x14064d0d5
0064D0A5  4C 8B 6D DF                     mov r13, qword ptr [rbp - 0x21]
0064D0A9  48 83 FE FF                     cmp rsi, -1
0064D0AD  74 0F                           je 0x14064d0be
0064D0AF  48 8B D6                        mov rdx, rsi
0064D0B2  48 8B CB                        mov rcx, rbx
0064D0B5  E8 0E C4 E3 FF                  call 0x1404894c8
0064D0BA  48 83 CE FF                     or rsi, 0xffffffffffffffff
0064D0BE  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
0064D0C2  45 8B CC                        mov r9d, r12d
0064D0C5  49 C1 E5 0C                     shl r13, 0xc
0064D0C9  48 C1 E2 0C                     shl rdx, 0xc
0064D0CD  49 8B CD                        mov rcx, r13
0064D0D0  E8 67 E9 1A 00                  call 0x1407fba3c
0064D0D5  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0064D0DA  4D 85 ED                        test r13, r13
0064D0DD  74 23                           je 0x14064d102
0064D0DF  48 83 FE FF                     cmp rsi, -1
0064D0E3  75 0B                           jne 0x14064d0f0
0064D0E5  48 8B CB                        mov rcx, rbx
0064D0E8  E8 B7 76 CC FF                  call 0x1403147a4
0064D0ED  48 8B F0                        mov rsi, rax
0064D0F0  48 8B CF                        mov rcx, rdi
0064D0F3  E8 CC F6 FF FF                  call 0x14064c7c4
0064D0F8  4C 8B E8                        mov r13, rax
0064D0FB  EB 05                           jmp 0x14064d102
0064D0FD  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0064D102  48 83 FE FF                     cmp rsi, -1
0064D106  74 0B                           je 0x14064d113
0064D108  48 8B D6                        mov rdx, rsi
0064D10B  48 8B CB                        mov rcx, rbx
0064D10E  E8 B5 C3 E3 FF                  call 0x1404894c8
0064D113  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0064D118  48 85 D2                        test rdx, rdx
0064D11B  74 19                           je 0x14064d136
0064D11D  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
0064D121  4D 8B CF                        mov r9, r15
0064D124  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0064D129  48 8B CB                        mov rcx, rbx
0064D12C  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0064D131  E8 26 0F 16 00                  call 0x1407ae05c
0064D136  4D 85 ED                        test r13, r13
0064D139  74 1C                           je 0x14064d157
0064D13B  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
0064D13F  4D 8B CF                        mov r9, r15
0064D142  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0064D147  49 8B D5                        mov rdx, r13
0064D14A  48 8B CB                        mov rcx, rbx
0064D14D  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0064D152  E8 05 0F 16 00                  call 0x1407ae05c
0064D157  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0064D15B  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064D15F  48 3B C8                        cmp rcx, rax
0064D162  74 2F                           je 0x14064d193
0064D164  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064D168  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0064D16C  75 1E                           jne 0x14064d18c
0064D16E  48 8B 01                        mov rax, qword ptr [rcx]
0064D171  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0064D175  75 15                           jne 0x14064d18c
0064D177  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0064D17B  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0064D17F  48 89 50 08                     mov qword ptr [rax + 8], rdx
0064D183  33 D2                           xor edx, edx
0064D185  E8 E6 56 53 00                  call 0x140b82870
0064D18A  EB CB                           jmp 0x14064d157
0064D18C  B9 03 00 00 00                  mov ecx, 3
0064D191  CD 29                           int 0x29
0064D193  41 8B C6                        mov eax, r14d
0064D196  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
0064D19A  48 33 CC                        xor rcx, rsp
0064D19D  E8 9E F4 05 00                  call 0x1406ac640
0064D1A2  48 81 C4 D8 00 00 00            add rsp, 0xd8
0064D1A9  41 5F                           pop r15
0064D1AB  41 5E                           pop r14
0064D1AD  41 5D                           pop r13
0064D1AF  41 5C                           pop r12
0064D1B1  5F                              pop rdi
0064D1B2  5E                              pop rsi
0064D1B3  5B                              pop rbx
0064D1B4  5D                              pop rbp
0064D1B5  C3                              ret
0064D1B6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpPinMemoryRange(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (216);
    result = (*(unsigned __int64 *)(v_rip + 8116816)) ^ (v_rsp);
    v_stack_m50 = result;
    v_stack_m90 = a3;
    v_r13 = 0;
    v_rdi = 0;
    v_stack_m68 = a3;
    result = 0;
    v_stack_m70 = a7;
    v_r15 = 0;
    v_stack_mC8 = 0;
    v_stack_m80 = 0;
    v_stack_m98 = v_stack_mA0;
    v_stack_mA0 = v_stack_mA0;
    result = (a4 - 1) + (a2);
    v_stack_m78 = a4;
    v_stack_mB0 = result;
    v_stack_mA8 = a2;
    v_stack_m60 = v_xmm0;
    v_stack_mD0 = 0;
    result = VmpCheckPinTooLate(a1, a2, a3, a4);
    if (sign_flag) goto loc_0064D113;
    result = VmpProcessContextLockExclusive(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 104)) != a6) {
    }
    if (((*(unsigned __int8 *)(a1 + 8 + 8)) & (1)) == 0) goto loc_0064CD9E;
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 8)) ^ (a1 + 8);
    }
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 8 + 8)) & (1));
    goto loc_0064CDCD;
loc_0064CDA7:
    if (a2 <= (*(unsigned __int64 *)(a1 + 32))) goto loc_0064CDB3;
    goto loc_0064CDBC;
loc_0064CDB3:
    if (a2 >= (*(unsigned __int64 *)(a1 + 24))) goto loc_0064CDD2;
loc_0064CDBC:
    if ((unsigned int)(result) == 0) goto loc_0064CDCA;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_0064CDCA;
    a1 = (a1) ^ (*(unsigned __int64 *)(a1));
    goto loc_0064CDCD;
loc_0064CDCA:
loc_0064CDCD:
    if (*(unsigned __int64 *)(a1) != 0) goto loc_0064CDA7;
loc_0064CDD2:
    a1 = -(*(unsigned __int64 *)(a1));
    v_r13 = (v_r13) & (*(unsigned __int64 *)(a1) - 24);
    if (!(condition_is_not_equal)) {
    }
    if ((*(unsigned __int64 *)(v_r13 + 56)) < v_stack_mB0) {
    }
    result = (*(unsigned __int64 *)(v_r13 + 48)) - (a2);
    result = (result) + (v_stack_m90);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 24)) != result) {
    }
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 32)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 24));
    v_r15 = (v_r15) + 1;
    result = (unsigned int)(((unsigned int)(a5)) & (2));
    v_stack_mB4 = (unsigned int)(result);
    v_r12 = (condition_is_not_equal) ? 1 : 0;
    result = VmpCountNewPinnedRangesNeeded(a1, v_stack_mA8, v_stack_mB0, a4);
    a1 = 0;
    v_stack_m88 = result;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56) == 0) ? 1 : 0;
    v_stack_mB8 = (unsigned int)(a1);
    if (result != 0) goto loc_0064CE59;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56) != 0) goto loc_0064CF09;
loc_0064CE59:
    result = VmpProcessContextUnlockExclusive(a1, result, v_stack_mB0, a4);
    if (result == 0) goto loc_0064CE91;
    result = VmpAllocatePinnedRanges(a1, v_stack_mA0, result, a4);
    if (sign_flag) goto loc_0064D157;
    v_stack_mC0 = v_stack_m88;
    result = 0;
    v_stack_m88 = 0;
loc_0064CE91:
    if (v_stack_mB8 == 0) goto loc_0064CEBC;
    result = VmpSecureMemoryForPin(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 24), v_r15, v_stack_m80);
    if (sign_flag) goto loc_0064CEE9;
    v_stack_mC8 = v_stack_m80;
    goto loc_0064CEC1;
loc_0064CEBC:
loc_0064CEC1:
    result = VmpProcessContextLockExclusive(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 24), v_r15, v_stack_m80);
    result = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56)) != 0) goto loc_0064CF09;
    if (v_stack_mC8 != 0) goto loc_0064CEF7;
    v_stack_mB8 = 1;
    goto loc_0064CE59;
loc_0064CEE9:
    goto loc_0064D118;
loc_0064CEF7:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56) = v_stack_m88;
    v_stack_mC8 = 0;
    if (v_stack_mB4 != 0) {
    }
    v_stack_mE8 = v_stack_m70;
    v_stack_mF0 = v_stack_mD8;
    v_stack_mF8 = (unsigned int)(v_r12);
    result = VmpCheckPinAndReference(a1, *(unsigned __int64 *)(v_r13 + 16), v_stack_mA8, v_stack_mB0);
    if (sign_flag) goto loc_0064D035;
    if ((unsigned int)((unsigned int)(v_stack_mD8)) != 0) goto loc_0064D03D;
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56);
    result = VmpProcessContextUnlockExclusive(a1, result, v_stack_mA8, v_stack_mB0);
    a2 = (v_stack_m78) << (12);
    v_rsi = (result) | (-1);
    a1 = (v_stack_m90) << (12);
    result = MmLockPhysicalPagesByVa(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56), (unsigned int)((unsigned int)(v_r12)));
    if (sign_flag) goto loc_0064D0D5;
    v_stack_mD4 = 1;
    result = VmpProcessContextLockExclusive(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 56), (unsigned int)((unsigned int)(v_r12)));
    v_stack_mE8 = v_stack_m70;
    v_stack_mF0 = v_stack_mD8;
    v_stack_mF8 = (unsigned int)(v_r12);
    result = VmpCheckPinAndReference(a1, *(unsigned __int64 *)(v_r13 + 16), v_stack_mA8, v_stack_mB0);
    if (sign_flag) goto loc_0064D025;
    if (v_stack_mD8 != 0) goto loc_0064D02C;
    result = VmpCountNewPinnedRangesNeeded(a1, v_stack_mA8, v_stack_mB0, v_stack_mB0);
    if (v_stack_mC0 >= result) goto loc_0064D002;
loc_0064CFF9:
    goto loc_0064D0A9;
loc_0064D002:
    result = VmpUpdatePinRangesForFirstPin(a1, (unsigned int)(0xC000022DULL), v_stack_mB0, v_stack_mA0);
    goto loc_0064D048;
loc_0064D025:
    if (v_stack_mD8 == 0) goto loc_0064CFF9;
loc_0064D02C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 64)) != 1) goto loc_0064D048;
    goto loc_0064CFF9;
loc_0064D035:
    if ((unsigned int)(result) == 0) goto loc_0064D0FD;
loc_0064D03D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 64)) == 0) goto loc_0064D0FD;
loc_0064D048:
    v_stack_mD0 = v_stack_mD0;
    result = VmpProcessContextUnlockExclusive(a1, result, v_stack_mB0, v_stack_mA0);
    v_stack_m60 = v_stack_mA8;
    v_stack_m58 = v_stack_m78;
    v_stack_mE8 = a6;
    result = VmAccessFault(v_stack_m60, v_stack_m68, 1, (unsigned int)(a5));
    v_r14 = 0;
    v_rsi = (result) | (-1);
    if (v_stack_mD4 == 0) goto loc_0064D0D5;
loc_0064D0A9:
    if (v_rsi != -1) {
        a2 = v_rsi;
        a1 = a1;
        result = VmpProcessContextUnlockExclusive(a1, a2, 1, (unsigned int)(a5));
        v_rsi = (v_rsi) | (-1);
    }
    v_r13 = (v_stack_m68) << (12);
    a2 = (v_stack_m78) << (12);
    result = MmUnlockPhysicalPagesByVa(v_r13, a2, 1, (unsigned int)((unsigned int)(v_r12)));
loc_0064D0D5:
    if (v_stack_mD0 == 0) goto loc_0064D102;
    if (v_rsi == -1) {
        a1 = a1;
        result = VmpProcessContextLockExclusive(a1, a2, 1, (unsigned int)((unsigned int)(v_r12)));
        v_rsi = result;
    }
    result = VmpDereferencePinInProgress(*(unsigned __int64 *)(v_r13 + 16), a2, 1, (unsigned int)((unsigned int)(v_r12)));
    goto loc_0064D102;
loc_0064D0FD:
loc_0064D102:
    if (v_rsi != -1) {
        a2 = v_rsi;
        a1 = a1;
        result = VmpProcessContextUnlockExclusive(a1, a2, 1, (unsigned int)((unsigned int)(v_r12)));
    }
loc_0064D118:
    if (v_stack_mC8 != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 24);
        a4 = v_r15;
        v_stack_mF0 = v_r15;
        a1 = a1;
        v_stack_mF8 = a3;
        result = VmpUnsecureMemoryForPin(a1, v_stack_mC8, a3, a4);
    }
    if (v_stack_mD0 != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16) + 24);
        a4 = v_r15;
        v_stack_mF0 = v_r15;
        a2 = v_stack_mD0;
        a1 = a1;
        v_stack_mF8 = a3;
        result = VmpUnsecureMemoryForPin(a1, a2, a3, a4);
    }
    if (v_stack_mA0 == v_stack_mA0) goto loc_0064D193;
    if ((*(unsigned __int64 *)(v_stack_mA0 + 8)) != v_stack_mA0) goto loc_0064D18C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0) + 8)) != v_stack_mA0) goto loc_0064D18C;
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_mA0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0) + 8) = v_stack_mA0;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mA0, a2, a3, a4);
    goto loc_0064D157;
loc_0064D18C:
loc_0064D193:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (216);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpPinMemoryRange(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (216);
    result = (*(uint64_t *)(v_rip + 0x7BDA50)) ^ (local_rsp);
    v_stack_m50 = result;
    v_stack_m90 = Arg3;
    local_r13 = 0;
    local_rdi = 0;
    v_stack_m68 = Arg3;
    result = 0;
    v_stack_m70 = Arg7;
    local_r15 = 0;
    v_stack_mC8 = 0;
    v_stack_m80 = 0;
    v_stack_m98 = v_stack_mA0;
    v_stack_mA0 = v_stack_mA0;
    result = (Arg4 - 1) + (Arg2);
    v_stack_m78 = Arg4;
    v_stack_mB0 = result;
    v_stack_mA8 = Arg2;
    v_stack_m60 = v_xmm0;
    v_stack_mD0 = 0;
    result = VmpCheckPinTooLate(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0064D113;
    result = VmpProcessContextLockExclusive(Arg1, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x68)) != Arg6) {
    }
    if (((*(uint8_t *)(arg1 + 0x8 + 0x8)) & (1)) == 0) goto loc_0064CD9E;
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x8)) ^ (Arg1 + 8);
    }
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x8 + 0x8)) & (1));
    goto loc_0064CDCD;
loc_0064CDA7:
    if (Arg2 <= (*(uint64_t *)(arg1 + 0x20))) goto loc_0064CDB3;
    goto loc_0064CDBC;
loc_0064CDB3:
    if (Arg2 >= (*(uint64_t *)(arg1 + 0x18))) goto loc_0064CDD2;
loc_0064CDBC:
    if ((uint32_t)(result) == 0) goto loc_0064CDCA;
    if (*(uint64_t *)(arg1) == 0) goto loc_0064CDCA;
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1));
    goto loc_0064CDCD;
loc_0064CDCA:
loc_0064CDCD:
    if (*(uint64_t *)(arg1) != 0) goto loc_0064CDA7;
loc_0064CDD2:
    Arg1 = -(*(uint64_t *)(arg1));
    local_r13 = (local_r13) & (*(uint64_t *)(arg1) - 24);
    if (!(condition_is_not_equal)) {
    }
    if ((*(uint64_t *)(local_r13 + 0x38)) < v_stack_mB0) {
    }
    result = (*(uint64_t *)(local_r13 + 0x30)) - (Arg2);
    result = (result) + (v_stack_m90);
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x18)) != result) {
    }
    local_r15 = (*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x20)) - (*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x18));
    local_r15 = (local_r15) + 1;
    result = (uint32_t)(((uint32_t)(Arg5)) & (2));
    v_stack_mB4 = (uint32_t)(result);
    local_r12 = (condition_is_not_equal) ? 1 : 0;
    result = VmpCountNewPinnedRangesNeeded(Arg1, v_stack_mA8, v_stack_mB0, Arg4);
    Arg1 = 0;
    v_stack_m88 = result;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38) == 0) ? 1 : 0;
    v_stack_mB8 = (uint32_t)(Arg1);
    if (result != 0) goto loc_0064CE59;
    if (*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38) != 0) goto loc_0064CF09;
loc_0064CE59:
    result = VmpProcessContextUnlockExclusive(Arg1, result, v_stack_mB0, Arg4);
    if (result == 0) goto loc_0064CE91;
    result = VmpAllocatePinnedRanges(Arg1, v_stack_mA0, result, Arg4);
    if (sign_flag) goto loc_0064D157;
    v_stack_mC0 = v_stack_m88;
    result = 0;
    v_stack_m88 = 0;
loc_0064CE91:
    if (v_stack_mB8 == 0) goto loc_0064CEBC;
    result = VmpSecureMemoryForPin(Arg1, *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x18), local_r15, v_stack_m80);
    if (sign_flag) goto loc_0064CEE9;
    v_stack_mC8 = v_stack_m80;
    goto loc_0064CEC1;
loc_0064CEBC:
loc_0064CEC1:
    result = VmpProcessContextLockExclusive(Arg1, *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x18), local_r15, v_stack_m80);
    result = 0;
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38)) != 0) goto loc_0064CF09;
    if (v_stack_mC8 != 0) goto loc_0064CEF7;
    v_stack_mB8 = 1;
    goto loc_0064CE59;
loc_0064CEE9:
    goto loc_0064D118;
loc_0064CEF7:
    *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38) = v_stack_m88;
    v_stack_mC8 = 0;
    if (v_stack_mB4 != 0) {
    }
    v_stack_mE8 = v_stack_m70;
    v_stack_mF0 = v_stack_mD8;
    v_stack_mF8 = (uint32_t)(local_r12);
    result = VmpCheckPinAndReference(Arg1, *(uint64_t *)(local_r13 + 0x10), v_stack_mA8, v_stack_mB0);
    if (sign_flag) goto loc_0064D035;
    if ((uint32_t)((uint32_t)(v_stack_mD8)) != 0) goto loc_0064D03D;
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38);
    result = VmpProcessContextUnlockExclusive(Arg1, result, v_stack_mA8, v_stack_mB0);
    Arg2 = (v_stack_m78) << (12);
    local_rsi = (result) | (-1);
    Arg1 = (v_stack_m90) << (12);
    result = MmLockPhysicalPagesByVa(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38), (uint32_t)((uint32_t)(local_r12)));
    if (sign_flag) goto loc_0064D0D5;
    v_stack_mD4 = 1;
    result = VmpProcessContextLockExclusive(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x38), (uint32_t)((uint32_t)(local_r12)));
    v_stack_mE8 = v_stack_m70;
    v_stack_mF0 = v_stack_mD8;
    v_stack_mF8 = (uint32_t)(local_r12);
    result = VmpCheckPinAndReference(Arg1, *(uint64_t *)(local_r13 + 0x10), v_stack_mA8, v_stack_mB0);
    if (sign_flag) goto loc_0064D025;
    if (v_stack_mD8 != 0) goto loc_0064D02C;
    result = VmpCountNewPinnedRangesNeeded(Arg1, v_stack_mA8, v_stack_mB0, v_stack_mB0);
    if (v_stack_mC0 >= result) goto loc_0064D002;
loc_0064CFF9:
    goto loc_0064D0A9;
loc_0064D002:
    result = VmpUpdatePinRangesForFirstPin(Arg1, (uint32_t)(0xC000022DULL), v_stack_mB0, v_stack_mA0);
    goto loc_0064D048;
loc_0064D025:
    if (v_stack_mD8 == 0) goto loc_0064CFF9;
loc_0064D02C:
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x40)) != 1) goto loc_0064D048;
    goto loc_0064CFF9;
loc_0064D035:
    if ((uint32_t)(result) == 0) goto loc_0064D0FD;
loc_0064D03D:
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x40)) == 0) goto loc_0064D0FD;
loc_0064D048:
    v_stack_mD0 = v_stack_mD0;
    result = VmpProcessContextUnlockExclusive(Arg1, result, v_stack_mB0, v_stack_mA0);
    v_stack_m60 = v_stack_mA8;
    v_stack_m58 = v_stack_m78;
    v_stack_mE8 = Arg6;
    result = VmAccessFault(v_stack_m60, v_stack_m68, 1, (uint32_t)(Arg5));
    local_r14 = 0;
    local_rsi = (result) | (-1);
    if (v_stack_mD4 == 0) goto loc_0064D0D5;
loc_0064D0A9:
    if (local_rsi != -1) {
        Arg2 = local_rsi;
        Arg1 = Arg1;
        result = VmpProcessContextUnlockExclusive(Arg1, Arg2, 1, (uint32_t)(Arg5));
        local_rsi = (local_rsi) | (-1);
    }
    local_r13 = (v_stack_m68) << (12);
    Arg2 = (v_stack_m78) << (12);
    result = MmUnlockPhysicalPagesByVa(local_r13, Arg2, 1, (uint32_t)((uint32_t)(local_r12)));
loc_0064D0D5:
    if (v_stack_mD0 == 0) goto loc_0064D102;
    if (local_rsi == -1) {
        Arg1 = Arg1;
        result = VmpProcessContextLockExclusive(Arg1, Arg2, 1, (uint32_t)((uint32_t)(local_r12)));
        local_rsi = result;
    }
    result = VmpDereferencePinInProgress(*(uint64_t *)(local_r13 + 0x10), Arg2, 1, (uint32_t)((uint32_t)(local_r12)));
    goto loc_0064D102;
loc_0064D0FD:
loc_0064D102:
    if (local_rsi != -1) {
        Arg2 = local_rsi;
        Arg1 = Arg1;
        result = VmpProcessContextUnlockExclusive(Arg1, Arg2, 1, (uint32_t)((uint32_t)(local_r12)));
    }
loc_0064D118:
    if (v_stack_mC8 != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x18);
        Arg4 = local_r15;
        v_stack_mF0 = local_r15;
        Arg1 = Arg1;
        v_stack_mF8 = Arg3;
        result = VmpUnsecureMemoryForPin(Arg1, v_stack_mC8, Arg3, Arg4);
    }
    if (v_stack_mD0 != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(local_r13 + 0x10) + 0x18);
        Arg4 = local_r15;
        v_stack_mF0 = local_r15;
        Arg2 = v_stack_mD0;
        Arg1 = Arg1;
        v_stack_mF8 = Arg3;
        result = VmpUnsecureMemoryForPin(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_mA0 == v_stack_mA0) goto loc_0064D193;
    if ((*(uint64_t *)(v_stack_mA0 + 0x8)) != v_stack_mA0) goto loc_0064D18C;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0) + 0x8)) != v_stack_mA0) goto loc_0064D18C;
    v_stack_mA0 = *(uint64_t *)(v_stack_mA0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0) + 0x8) = v_stack_mA0;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mA0, Arg2, Arg3, Arg4);
    goto loc_0064D157;
loc_0064D18C:
loc_0064D193:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (216);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R/W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg4` | `- 0x1` | `64` | `R` |
| `Arg7` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064CCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
