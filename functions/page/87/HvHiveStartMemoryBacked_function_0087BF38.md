# HvHiveStartMemoryBacked

- RVA: `0x0087BF38`–`0x0087C644` (길이 `1,804` bytes)
- VA: `0x000000014087BF38`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF4C`
- 디코드: `412`개 명령, `1,804/1,804` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0087C0AA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C0D0` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087C117` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C131` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C182` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0087C1AC` → [HvpFillFileName](../9B/HvpFillFileName_function_009B9A2C.md) (function, `0x009B9A2C`)
- `0x0087C2BA` → [HvIsInPlaceBaseBlockValid](../7F/HvIsInPlaceBaseBlockValid_function_007F19D4.md) (function, `0x007F19D4`)
- `0x0087C322` → [HvpAdjustHiveFreeDisplay](../84/HvpAdjustHiveFreeDisplay_function_0084DB80.md) (function, `0x0084DB80`)
- `0x0087C361` → [HvpBuildMapForMemoryBackedHive](../7F/HvpBuildMapForMemoryBackedHive_function_007F3B4C.md) (function, `0x007F3B4C`)
- `0x0087C3E7` → [HvpHeaderCheckSum](../../pagecmrc/BC/HvpHeaderCheckSum_function_00BC97A0.md) (function, `0x00BC97A0`)
- `0x0087C40B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C443` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C45B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C55E` → [HvpAdjustHiveFreeDisplay](../84/HvpAdjustHiveFreeDisplay_function_0084DB80.md) (function, `0x0084DB80`)
- `0x0087C576` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C5B2` → [HvpBuildMapForMemoryBackedHive](../7F/HvpBuildMapForMemoryBackedHive_function_007F3B4C.md) (function, `0x007F3B4C`)
- `0x0087C5D4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087C5E6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087C621` → [HvpFillFileName](../9B/HvpFillFileName_function_009B9A2C.md) (function, `0x009B9A2C`)

### Direct callers
- [CmpCreateHive](CmpCreateHive_function_00879DF0.md) at `0x0087A0B8`
- [CmpGetSystemControlValues](../../init/C5/CmpGetSystemControlValues_function_00C5959C.md) at `0x00C596B3`

### Static image references
- `0x0087C033` → RVA `0x00854CB0` (`HvpGetCellPaged`; read)
- `0x0087C059` → RVA `0x00855F40` (`HvpReleaseCellPaged`; read)
- `0x0087C270` → RVA `0x00854C60` (`HvpGetCellFlat`; read)
- `0x0087C27B` → RVA `0x0085CC20` (`HvpReleaseCellFlat`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0087C0AA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C0D0` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087C117` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C131` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C182` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0087C3E7` → [HvpHeaderCheckSum](../../pagecmrc/BC/HvpHeaderCheckSum_function_00BC97A0.md) (`PAGE` → `PAGECMRC`)
  - `0x0087C40B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C443` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C45B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C576` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087C5D4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087C5E6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0087BF38  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0087BF3D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0087BF42  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0087BF47  57                              push rdi
0087BF48  41 54                           push r12
0087BF4A  41 55                           push r13
0087BF4C  41 56                           push r14
0087BF4E  41 57                           push r15
0087BF50  48 83 EC 30                     sub rsp, 0x30
0087BF54  48 8B AC 24 D8 00 00 00         mov rbp, qword ptr [rsp + 0xd8]
0087BF5C  48 8B F9                        mov rdi, rcx
0087BF5F  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0087BF67  45 8B F0                        mov r14d, r8d
0087BF6A  48 89 69 38                     mov qword ptr [rcx + 0x38], rbp
0087BF6E  B9 05 00 00 00                  mov ecx, 5
0087BF73  44 8D 41 FD                     lea r8d, [rcx - 3]
0087BF77  41 3B D0                        cmp edx, r8d
0087BF7A  0F 84 C2 06 00 00               je 0x14087c642
0087BF80  3B D1                           cmp edx, ecx
0087BF82  0F 83 BA 06 00 00               jae 0x14087c642
0087BF88  41 F7 C6 EC 7C 61 F5            test r14d, 0xf5617cec
0087BF8F  0F 85 AD 06 00 00               jne 0x14087c642
0087BF95  45 3B C8                        cmp r9d, r8d
0087BF98  0F 87 A4 06 00 00               ja 0x14087c642
0087BF9E  44 8B BC 24 90 00 00 00         mov r15d, dword ptr [rsp + 0x90]
0087BFA6  41 8D 47 FF                     lea eax, [r15 - 1]
0087BFAA  83 F8 07                        cmp eax, 7
0087BFAD  0F 87 8F 06 00 00               ja 0x14087c642
0087BFB3  45 33 D2                        xor r10d, r10d
0087BFB6  48 85 F6                        test rsi, rsi
0087BFB9  75 13                           jne 0x14087bfce
0087BFBB  8D 42 FF                        lea eax, [rdx - 1]
0087BFBE  A9 FC FF FF FF                  test eax, 0xfffffffc
0087BFC3  75 09                           jne 0x14087bfce
0087BFC5  41 3B D0                        cmp edx, r8d
0087BFC8  0F 85 74 06 00 00               jne 0x14087c642
0087BFCE  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
0087BFD6  4D 85 E4                        test r12, r12
0087BFD9  74 04                           je 0x14087bfdf
0087BFDB  45 88 14 24                     mov byte ptr [r12], r10b
0087BFDF  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0087BFE7  48 85 C9                        test rcx, rcx
0087BFEA  74 1F                           je 0x14087c00b
0087BFEC  48 8B 01                        mov rax, qword ptr [rcx]
0087BFEF  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0087BFF3  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0087BFF7  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
0087BFFB  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0087BFFF  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
0087C003  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0087C007  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
0087C00B  41 BD 04 00 00 00               mov r13d, 4
0087C011  45 8D 5D FD                     lea r11d, [r13 - 3]
0087C015  45 85 C9                        test r9d, r9d
0087C018  75 09                           jne 0x14087c023
0087C01A  44 89 97 A8 00 00 00            mov dword ptr [rdi + 0xa8], r10d
0087C021  EB 10                           jmp 0x14087c033
0087C023  45 3B CB                        cmp r9d, r11d
0087C026  41 8B C5                        mov eax, r13d
0087C029  41 0F 44 C3                     cmove eax, r11d
0087C02D  89 87 A8 00 00 00               mov dword ptr [rdi + 0xa8], eax
0087C033  48 8D 05 76 8C FD FF            lea rax, [rip - 0x2738a]
0087C03A  44 89 B7 A0 00 00 00            mov dword ptr [rdi + 0xa0], r14d
0087C041  48 89 47 08                     mov qword ptr [rdi + 8], rax
0087C045  45 8A CE                        mov r9b, r14b
0087C048  48 BB 14 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000014
0087C052  44 89 BF 88 00 00 00            mov dword ptr [rdi + 0x88], r15d
0087C059  48 8D 05 E0 9E FD FF            lea rax, [rip - 0x26120]
0087C060  44 89 87 D8 00 00 00            mov dword ptr [rdi + 0xd8], r8d
0087C067  41 F6 D1                        not r9b
0087C06A  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0087C06E  C7 87 84 00 00 00 00 10 00 00   mov dword ptr [rdi + 0x84], 0x1000
0087C078  45 22 CB                        and r9b, r11b
0087C07B  48 8B 1B                        mov rbx, qword ptr [rbx]
0087C07E  48 89 9F C8 00 00 00            mov qword ptr [rdi + 0xc8], rbx
0087C085  44 88 9F C2 00 00 00            mov byte ptr [rdi + 0xc2], r11b
0087C08C  85 D2                           test edx, edx
0087C08E  0F 85 BC 01 00 00               jne 0x14087c250
0087C094  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0087C098  41 BD 43 4D 31 31               mov r13d, 0x31314d43
0087C09E  8B 8F 84 00 00 00               mov ecx, dword ptr [rdi + 0x84]
0087C0A4  45 8B C5                        mov r8d, r13d
0087C0A7  41 8A D1                        mov dl, r9b
0087C0AA  E8 21 EA E3 FF                  call 0x1406baad0
0087C0AF  48 8B F0                        mov rsi, rax
0087C0B2  48 85 C0                        test rax, rax
0087C0B5  75 3E                           jne 0x14087c0f5
0087C0B7  C7 44 24 20 60 00 00 00         mov dword ptr [rsp + 0x20], 0x60
0087C0BF  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0087C0C4  33 D2                           xor edx, edx
0087C0C6  44 8B CB                        mov r9d, ebx
0087C0C9  48 8B CD                        mov rcx, rbp
0087C0CC  44 8D 42 19                     lea r8d, [rdx + 0x19]
0087C0D0  E8 7F 2E BF FF                  call 0x14046ef54
0087C0D5  8B C3                           mov eax, ebx
0087C0D7  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0087C0DC  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0087C0E1  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0087C0E6  48 83 C4 30                     add rsp, 0x30
0087C0EA  41 5F                           pop r15
0087C0EC  41 5E                           pop r14
0087C0EE  41 5D                           pop r13
0087C0F0  41 5C                           pop r12
0087C0F2  5F                              pop rdi
0087C0F3  C3                              ret
0087C0F4  CC                              int3
0087C0F5  41 C1 E7 09                     shl r15d, 9
0087C0F9  41 BC 01 00 00 00               mov r12d, 1
0087C0FF  45 2B FC                        sub r15d, r12d
0087C102  41 8B C7                        mov eax, r15d
0087C105  48 85 C6                        test rsi, rax
0087C108  74 5D                           je 0x14087c167
0087C10A  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0087C10E  48 8B CE                        mov rcx, rsi
0087C111  8B 97 84 00 00 00               mov edx, dword ptr [rdi + 0x84]
0087C117  E8 B4 E9 E3 FF                  call 0x1406baad0
0087C11C  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0087C120  41 BF 43 4D 31 32               mov r15d, 0x32314d43
0087C126  45 8B C7                        mov r8d, r15d
0087C129  41 8A D4                        mov dl, r12b
0087C12C  B9 00 10 00 00                  mov ecx, 0x1000
0087C131  E8 9A E9 E3 FF                  call 0x1406baad0
0087C136  48 8B F0                        mov rsi, rax
0087C139  48 85 C0                        test rax, rax
0087C13C  75 0D                           jne 0x14087c14b
0087C13E  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
0087C146  E9 74 FF FF FF                  jmp 0x14087c0bf
0087C14B  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0087C153  C7 87 84 00 00 00 00 10 00 00   mov dword ptr [rdi + 0x84], 0x1000
0087C15D  48 85 C0                        test rax, rax
0087C160  74 15                           je 0x14087c177
0087C162  44 89 38                        mov dword ptr [rax], r15d
0087C165  EB 10                           jmp 0x14087c177
0087C167  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0087C16F  48 85 C0                        test rax, rax
0087C172  74 03                           je 0x14087c177
0087C174  44 89 28                        mov dword ptr [rax], r13d
0087C177  33 D2                           xor edx, edx
0087C179  41 B8 00 10 00 00               mov r8d, 0x1000
0087C17F  48 8B CE                        mov rcx, rsi
0087C182  E8 B9 AA E4 FF                  call 0x1406c6c40
0087C187  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0087C18F  48 8B CE                        mov rcx, rsi
0087C192  83 4E 24 FF                     or dword ptr [rsi + 0x24], 0xffffffff
0087C196  C7 06 72 65 67 66               mov dword ptr [rsi], 0x66676572
0087C19C  44 89 66 04                     mov dword ptr [rsi + 4], r12d
0087C1A0  44 89 66 08                     mov dword ptr [rsi + 8], r12d
0087C1A4  44 89 66 20                     mov dword ptr [rsi + 0x20], r12d
0087C1A8  44 89 66 2C                     mov dword ptr [rsi + 0x2c], r12d
0087C1AC  E8 7B D8 13 00                  call 0x1409b9a2c
0087C1B1  83 A6 90 00 00 00 00            and dword ptr [rsi + 0x90], 0
0087C1B8  41 81 E6 00 00 08 00            and r14d, 0x80000
0087C1BF  74 0A                           je 0x14087c1cb
0087C1C1  C7 86 90 00 00 00 02 00 00 00   mov dword ptr [rsi + 0x90], 2
0087C1CB  44 89 66 14                     mov dword ptr [rsi + 0x14], r12d
0087C1CF  41 F7 DE                        neg r14d
0087C1D2  1B C0                           sbb eax, eax
0087C1D4  83 E0 03                        and eax, 3
0087C1D7  83 C0 03                        add eax, 3
0087C1DA  89 46 18                        mov dword ptr [rsi + 0x18], eax
0087C1DD  89 87 DC 00 00 00               mov dword ptr [rdi + 0xdc], eax
0087C1E3  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0087C1EB  C7 86 A4 00 00 00 72 6D 74 6D   mov dword ptr [rsi + 0xa4], 0x6d746d72
0087C1F5  44 89 A7 AC 00 00 00            mov dword ptr [rdi + 0xac], r12d
0087C1FC  44 89 A7 B8 00 00 00            mov dword ptr [rdi + 0xb8], r12d
0087C203  44 89 A7 B0 00 00 00            mov dword ptr [rdi + 0xb0], r12d
0087C20A  48 89 5E 0C                     mov qword ptr [rsi + 0xc], rbx
0087C20E  48 85 C0                        test rax, rax
0087C211  74 13                           je 0x14087c226
0087C213  0F 10 00                        movups xmm0, xmmword ptr [rax]
0087C216  F3 0F 7F 46 70                  movdqu xmmword ptr [rsi + 0x70], xmm0
0087C21B  0F 10 08                        movups xmm1, xmmword ptr [rax]
0087C21E  F3 0F 7F 8E 80 00 00 00         movdqu xmmword ptr [rsi + 0x80], xmm1
0087C226  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0087C22E  48 85 C0                        test rax, rax
0087C231  74 0B                           je 0x14087c23e
0087C233  0F 10 00                        movups xmm0, xmmword ptr [rax]
0087C236  F3 0F 7F 86 94 00 00 00         movdqu xmmword ptr [rsi + 0x94], xmm0
0087C23E  48 89 77 40                     mov qword ptr [rdi + 0x40], rsi
0087C242  83 A6 F8 0F 00 00 00            and dword ptr [rsi + 0xff8], 0
0087C249  33 C0                           xor eax, eax
0087C24B  E9 87 FE FF FF                  jmp 0x14087c0d7
0087C250  41 3B D5                        cmp edx, r13d
0087C253  75 59                           jne 0x14087c2ae
0087C255  48 89 77 40                     mov qword ptr [rdi + 0x40], rsi
0087C259  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0087C25C  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
0087C25F  05 00 F0 FF FF                  add eax, 0xfffff000
0087C264  80 8F 8C 00 00 00 03            or byte ptr [rdi + 0x8c], 3
0087C26B  C1 E1 0C                        shl ecx, 0xc
0087C26E  03 C8                           add ecx, eax
0087C270  48 8D 05 E9 89 FD FF            lea rax, [rip - 0x27617]
0087C277  48 89 47 08                     mov qword ptr [rdi + 8], rax
0087C27B  48 8D 05 9E 09 FE FF            lea rax, [rip - 0x1f662]
0087C282  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0087C286  89 8F DC 00 00 00               mov dword ptr [rdi + 0xdc], ecx
0087C28C  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
0087C28F  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
0087C295  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0087C29D  44 89 9F D8 00 00 00            mov dword ptr [rdi + 0xd8], r11d
0087C2A4  48 85 C0                        test rax, rax
0087C2A7  74 A0                           je 0x14087c249
0087C2A9  44 89 10                        mov dword ptr [rax], r10d
0087C2AC  EB 9B                           jmp 0x14087c249
0087C2AE  83 FA 03                        cmp edx, 3
0087C2B1  0F 85 DB 00 00 00               jne 0x14087c392
0087C2B7  48 8B CE                        mov rcx, rsi
0087C2BA  E8 15 57 F7 FF                  call 0x1407f19d4
0087C2BF  84 C0                           test al, al
0087C2C1  75 12                           jne 0x14087c2d5
0087C2C3  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
0087C2CB  BB 4C 01 00 C0                  mov ebx, 0xc000014c
0087C2D0  E9 EF FD FF FF                  jmp 0x14087c0c4
0087C2D5  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
0087C2D8  45 33 C0                        xor r8d, r8d
0087C2DB  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0087C2DE  80 A7 8C 00 00 00 FD            and byte ptr [rdi + 0x8c], 0xfd
0087C2E5  05 00 F0 FF FF                  add eax, 0xfffff000
0087C2EA  48 89 77 40                     mov qword ptr [rdi + 0x40], rsi
0087C2EE  44 89 9F D8 00 00 00            mov dword ptr [rdi + 0xd8], r11d
0087C2F5  C1 E1 0C                        shl ecx, 0xc
0087C2F8  03 C8                           add ecx, eax
0087C2FA  89 8F DC 00 00 00               mov dword ptr [rdi + 0xdc], ecx
0087C300  48 8B CF                        mov rcx, rdi
0087C303  44 89 96 F8 0F 00 00            mov dword ptr [rsi + 0xff8], r10d
0087C30A  8B 46 04                        mov eax, dword ptr [rsi + 4]
0087C30D  89 87 AC 00 00 00               mov dword ptr [rdi + 0xac], eax
0087C313  89 87 B8 00 00 00               mov dword ptr [rdi + 0xb8], eax
0087C319  89 87 B0 00 00 00               mov dword ptr [rdi + 0xb0], eax
0087C31F  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
0087C322  E8 59 18 FD FF                  call 0x14084db80
0087C327  8B D8                           mov ebx, eax
0087C329  85 C0                           test eax, eax
0087C32B  79 0D                           jns 0x14087c33a
0087C32D  C7 44 24 20 90 00 00 00         mov dword ptr [rsp + 0x20], 0x90
0087C335  E9 8A FD FF FF                  jmp 0x14087c0c4
0087C33A  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0087C342  48 8D 96 00 10 00 00            lea rdx, [rsi + 0x1000]
0087C349  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
0087C351  48 8B CF                        mov rcx, rdi
0087C354  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
0087C35C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087C361  E8 E6 77 F7 FF                  call 0x1407f3b4c
0087C366  8B D8                           mov ebx, eax
0087C368  85 C0                           test eax, eax
0087C36A  79 0D                           jns 0x14087c379
0087C36C  C7 44 24 20 A0 00 00 00         mov dword ptr [rsp + 0x20], 0xa0
0087C374  E9 4B FD FF FF                  jmp 0x14087c0c4
0087C379  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0087C381  48 85 C0                        test rax, rax
0087C384  0F 84 BF FE FF FF               je 0x14087c249
0087C38A  83 20 00                        and dword ptr [rax], 0
0087C38D  E9 B7 FE FF FF                  jmp 0x14087c249
0087C392  41 3B D3                        cmp edx, r11d
0087C395  0F 85 9D 02 00 00               jne 0x14087c638
0087C39B  81 3E 72 65 67 66               cmp dword ptr [rsi], 0x66676572
0087C3A1  0F 85 84 02 00 00               jne 0x14087c62b
0087C3A7  44 39 56 1C                     cmp dword ptr [rsi + 0x1c], r10d
0087C3AB  0F 85 7A 02 00 00               jne 0x14087c62b
0087C3B1  44 39 5E 20                     cmp dword ptr [rsi + 0x20], r11d
0087C3B5  0F 85 70 02 00 00               jne 0x14087c62b
0087C3BB  44 39 5E 14                     cmp dword ptr [rsi + 0x14], r11d
0087C3BF  0F 87 66 02 00 00               ja 0x14087c62b
0087C3C5  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0087C3C8  83 E8 03                        sub eax, 3
0087C3CB  83 F8 03                        cmp eax, 3
0087C3CE  0F 87 57 02 00 00               ja 0x14087c62b
0087C3D4  48 8D 5E 28                     lea rbx, [rsi + 0x28]
0087C3D8  81 3B 00 E0 FF 7F               cmp dword ptr [rbx], 0x7fffe000
0087C3DE  0F 87 47 02 00 00               ja 0x14087c62b
0087C3E4  48 8B CE                        mov rcx, rsi
0087C3E7  E8 B4 D3 34 00                  call 0x140bc97a0
0087C3EC  3B 86 FC 01 00 00               cmp eax, dword ptr [rsi + 0x1fc]
0087C3F2  0F 85 33 02 00 00               jne 0x14087c62b
0087C3F8  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0087C3FC  41 B8 43 4D 31 33               mov r8d, 0x33314d43
0087C402  8B 8F 84 00 00 00               mov ecx, dword ptr [rdi + 0x84]
0087C408  41 8A D1                        mov dl, r9b
0087C40B  E8 C0 E6 E3 FF                  call 0x1406baad0
0087C410  4C 8D 77 40                     lea r14, [rdi + 0x40]
0087C414  48 8B C8                        mov rcx, rax
0087C417  49 89 06                        mov qword ptr [r14], rax
0087C41A  48 85 C0                        test rax, rax
0087C41D  75 0D                           jne 0x14087c42c
0087C41F  C7 44 24 20 C0 00 00 00         mov dword ptr [rsp + 0x20], 0xc0
0087C427  E9 93 FC FF FF                  jmp 0x14087c0bf
0087C42C  41 C1 E7 09                     shl r15d, 9
0087C430  41 8D 47 FF                     lea eax, [r15 - 1]
0087C434  48 85 C1                        test rcx, rax
0087C437  74 62                           je 0x14087c49b
0087C439  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0087C43D  8B 97 84 00 00 00               mov edx, dword ptr [rdi + 0x84]
0087C443  E8 88 E6 E3 FF                  call 0x1406baad0
0087C448  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0087C44C  BB 43 4D 31 34                  mov ebx, 0x34314d43
0087C451  44 8B C3                        mov r8d, ebx
0087C454  B2 01                           mov dl, 1
0087C456  B9 00 10 00 00                  mov ecx, 0x1000
0087C45B  E8 70 E6 E3 FF                  call 0x1406baad0
0087C460  49 89 06                        mov qword ptr [r14], rax
0087C463  48 85 C0                        test rax, rax
0087C466  75 0D                           jne 0x14087c475
0087C468  C7 44 24 20 D0 00 00 00         mov dword ptr [rsp + 0x20], 0xd0
0087C470  E9 4A FC FF FF                  jmp 0x14087c0bf
0087C475  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0087C47D  4D 8B FE                        mov r15, r14
0087C480  C7 87 84 00 00 00 00 10 00 00   mov dword ptr [rdi + 0x84], 0x1000
0087C48A  48 85 C0                        test rax, rax
0087C48D  74 06                           je 0x14087c495
0087C48F  89 18                           mov dword ptr [rax], ebx
0087C491  4C 8D 7F 40                     lea r15, [rdi + 0x40]
0087C495  48 8D 5E 28                     lea rbx, [rsi + 0x28]
0087C499  EB 16                           jmp 0x14087c4b1
0087C49B  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0087C4A3  4D 8B FE                        mov r15, r14
0087C4A6  48 85 C0                        test rax, rax
0087C4A9  74 06                           je 0x14087c4b1
0087C4AB  C7 00 43 4D 31 33               mov dword ptr [rax], 0x33314d43
0087C4B1  49 8B 06                        mov rax, qword ptr [r14]
0087C4B4  48 8B CE                        mov rcx, rsi
0087C4B7  BA 80 00 00 00                  mov edx, 0x80
0087C4BC  0F 10 01                        movups xmm0, xmmword ptr [rcx]
0087C4BF  0F 11 00                        movups xmmword ptr [rax], xmm0
0087C4C2  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
0087C4C6  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
0087C4CA  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
0087C4CE  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
0087C4D2  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
0087C4D6  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
0087C4DA  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
0087C4DE  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
0087C4E2  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
0087C4E6  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
0087C4EA  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
0087C4EE  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
0087C4F2  48 03 C2                        add rax, rdx
0087C4F5  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
0087C4F9  48 03 CA                        add rcx, rdx
0087C4FC  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
0087C500  49 83 ED 01                     sub r13, 1
0087C504  75 B6                           jne 0x14087c4bc
0087C506  8B 86 FC 0F 00 00               mov eax, dword ptr [rsi + 0xffc]
0087C50C  49 8B 0E                        mov rcx, qword ptr [r14]
0087C50F  89 81 FC 0F 00 00               mov dword ptr [rcx + 0xffc], eax
0087C515  8B 86 F8 0F 00 00               mov eax, dword ptr [rsi + 0xff8]
0087C51B  49 8B 0E                        mov rcx, qword ptr [r14]
0087C51E  89 81 F8 0F 00 00               mov dword ptr [rcx + 0xff8], eax
0087C524  48 8B CF                        mov rcx, rdi
0087C527  8B 46 04                        mov eax, dword ptr [rsi + 4]
0087C52A  89 87 AC 00 00 00               mov dword ptr [rdi + 0xac], eax
0087C530  89 87 B8 00 00 00               mov dword ptr [rdi + 0xb8], eax
0087C536  89 87 B0 00 00 00               mov dword ptr [rdi + 0xb0], eax
0087C53C  49 8B 06                        mov rax, qword ptr [r14]
0087C53F  44 8B 40 14                     mov r8d, dword ptr [rax + 0x14]
0087C543  8B 40 18                        mov eax, dword ptr [rax + 0x18]
0087C546  41 C1 E0 0C                     shl r8d, 0xc
0087C54A  05 00 F0 FF FF                  add eax, 0xfffff000
0087C54F  44 03 C0                        add r8d, eax
0087C552  44 89 87 DC 00 00 00            mov dword ptr [rdi + 0xdc], r8d
0087C559  45 33 C0                        xor r8d, r8d
0087C55C  8B 13                           mov edx, dword ptr [rbx]
0087C55E  E8 1D 16 FD FF                  call 0x14084db80
0087C563  8B D8                           mov ebx, eax
0087C565  85 C0                           test eax, eax
0087C567  79 22                           jns 0x14087c58b
0087C569  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0087C56D  8B 97 84 00 00 00               mov edx, dword ptr [rdi + 0x84]
0087C573  49 8B 0E                        mov rcx, qword ptr [r14]
0087C576  E8 55 E5 E3 FF                  call 0x1406baad0
0087C57B  4D 21 2F                        and qword ptr [r15], r13
0087C57E  C7 44 24 20 E0 00 00 00         mov dword ptr [rsp + 0x20], 0xe0
0087C586  E9 39 FB FF FF                  jmp 0x14087c0c4
0087C58B  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0087C593  48 8D 96 00 10 00 00            lea rdx, [rsi + 0x1000]
0087C59A  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
0087C5A2  48 8B CF                        mov rcx, rdi
0087C5A5  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
0087C5AD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087C5B2  E8 95 75 F7 FF                  call 0x1407f3b4c
0087C5B7  85 C0                           test eax, eax
0087C5B9  79 39                           jns 0x14087c5f4
0087C5BB  33 D2                           xor edx, edx
0087C5BD  C7 44 24 20 F0 00 00 00         mov dword ptr [rsp + 0x20], 0xf0
0087C5C5  BB 4C 01 00 C0                  mov ebx, 0xc000014c
0087C5CA  48 8B CD                        mov rcx, rbp
0087C5CD  44 8B CB                        mov r9d, ebx
0087C5D0  44 8D 42 19                     lea r8d, [rdx + 0x19]
0087C5D4  E8 7B 29 BF FF                  call 0x14046ef54
0087C5D9  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0087C5DD  8B 97 84 00 00 00               mov edx, dword ptr [rdi + 0x84]
0087C5E3  49 8B 0E                        mov rcx, qword ptr [r14]
0087C5E6  E8 E5 E4 E3 FF                  call 0x1406baad0
0087C5EB  49 83 27 00                     and qword ptr [r15], 0
0087C5EF  E9 E1 FA FF FF                  jmp 0x14087c0d5
0087C5F4  49 8B 06                        mov rax, qword ptr [r14]
0087C5F7  8B 90 90 00 00 00               mov edx, dword ptr [rax + 0x90]
0087C5FD  F6 C2 01                        test dl, 1
0087C600  74 0A                           je 0x14087c60c
0087C602  4D 85 E4                        test r12, r12
0087C605  74 05                           je 0x14087c60c
0087C607  41 C6 04 24 01                  mov byte ptr [r12], 1
0087C60C  49 8B 07                        mov rax, qword ptr [r15]
0087C60F  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0087C617  83 A0 90 00 00 00 FE            and dword ptr [rax + 0x90], 0xfffffffe
0087C61E  49 8B 0F                        mov rcx, qword ptr [r15]
0087C621  E8 06 D4 13 00                  call 0x1409b9a2c
0087C626  E9 1E FC FF FF                  jmp 0x14087c249
0087C62B  C7 44 24 20 B0 00 00 00         mov dword ptr [rsp + 0x20], 0xb0
0087C633  E9 93 FC FF FF                  jmp 0x14087c2cb
0087C638  B8 0D 00 00 C0                  mov eax, 0xc000000d
0087C63D  E9 95 FA FF FF                  jmp 0x14087c0d7
0087C642  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvHiveStartMemoryBacked(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(a1 + 56) = a16;
    if (((unsigned int)(a2)) == ((unsigned int)(5 - 3))) goto loc_0087C642;
    if (((unsigned int)(a2)) >= 5) goto loc_0087C642;
    if ((((unsigned int)((unsigned int)(a3))) & (0xF5617CECULL)) != 0) goto loc_0087C642;
    if (a4 > ((unsigned int)(5 - 3))) goto loc_0087C642;
    if (((unsigned int)((unsigned int)(a7) - 1)) > 7) goto loc_0087C642;
    v_r10 = 0;
    if (a5 != 0) goto loc_0087BFCE;
    if ((((unsigned int)(a2 - 1)) & (0xFFFFFFFCULL)) != 0) goto loc_0087BFCE;
    if (((unsigned int)(a2)) != ((unsigned int)(5 - 3))) goto loc_0087C642;
loc_0087BFCE:
    if (a14 != 0) {
        *(unsigned __int8 *)(a14) = 0;
    }
    result = a2 - 1;
    if (a6 != 0) {
        result = *(unsigned __int64 *)(a6);
        *(unsigned __int64 *)(a1 + 24) = result;
        result = *(unsigned __int64 *)(a6 + 8);
        *(unsigned __int64 *)(a1 + 32) = result;
        result = *(unsigned __int64 *)(a6 + 24);
        *(unsigned __int64 *)(a1 + 40) = result;
        result = *(unsigned __int64 *)(a6 + 32);
        *(unsigned __int64 *)(a1 + 48) = result;
    }
    if (a4 != 0) goto loc_0087C023;
    *(unsigned int *)(a1 + 168) = 0;
    goto loc_0087C033;
loc_0087C023:
    result = 4;
    if (a4 == ((unsigned int)(4 - 3))) { result = (unsigned int)(4 - 3); }
    *(unsigned int *)(a1 + 168) = (unsigned int)(result);
loc_0087C033:
    *(unsigned int *)(a1 + 160) = (unsigned int)((unsigned int)(a3));
    *(unsigned __int64 *)(a1 + 8) = v_rip - 160650;
    *(unsigned int *)(a1 + 136) = (unsigned int)((unsigned int)(a7));
    *(unsigned int *)(a1 + 216) = (unsigned int)(5 - 3);
    a4 = (unsigned __int8)(~((unsigned __int8)((unsigned int)(a3))));
    *(unsigned __int64 *)(a1 + 16) = v_rip - 155936;
    *(unsigned int *)(a1 + 132) = 0x1000ULL;
    a4 = (unsigned __int8)((a4) & ((unsigned __int8)(4 - 3)));
    *(unsigned __int64 *)(a1 + 200) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int8 *)(a1 + 194) = (unsigned __int8)(4 - 3);
    if ((unsigned int)(a2) != 0) goto loc_0087C250;
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(a1 + 132)), (unsigned __int8)(a4), (unsigned int)((unsigned int)((unsigned int)(0x31314D43ULL))), a4);
    if (result != 0) goto loc_0087C0F5;
    v_stack_m38 = 96;
loc_0087C0BF:
loc_0087C0C4:
    a2 = 0;
    result = SetFailureLocation(a16, a2, a2 + 25, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
loc_0087C0D5:
loc_0087C0D7:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
loc_0087C0F5:
    v_r15 = (unsigned int)(((unsigned int)(a7)) << (9));
    v_r15 = (unsigned int)((v_r15) - (1));
    if (((v_stack_p18) & ((unsigned int)((unsigned int)(v_r15)))) == 0) goto loc_0087C167;
    result = guard_dispatch_icall(v_stack_p18, (unsigned int)(*(unsigned int *)(a1 + 132)), a2 + 25, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
    result = guard_dispatch_icall((unsigned int)(0x1000ULL), 1, (unsigned int)((unsigned int)((unsigned int)(0x32314D43ULL))), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
    if (result != 0) goto loc_0087C14B;
    v_stack_p20 = 112;
    goto loc_0087C0BF;
loc_0087C14B:
    *(unsigned int *)(a1 + 132) = 0x1000ULL;
    if (a15 == 0) goto loc_0087C177;
    *(unsigned int *)(a15) = (unsigned int)((unsigned int)(0x32314D43ULL));
    goto loc_0087C177;
loc_0087C167:
    if (a15 != 0) {
        *(unsigned int *)(a15) = (unsigned int)((unsigned int)(0x31314D43ULL));
    }
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
    *(unsigned int *)(result) = 0x66676572ULL;
    *(unsigned int *)(result + 4) = 1;
    *(unsigned int *)(result + 8) = 1;
    *(unsigned int *)(result + 32) = 1;
    *(unsigned int *)(result + 44) = 1;
    result = HvpFillFileName(result, a8, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
    v_r14 = (unsigned int)(((unsigned int)(a3)) & (0x80000ULL));
    if (!(condition_is_equal)) {
        *(unsigned int *)(result + 144) = 2;
    }
    *(unsigned int *)(result + 20) = 1;
    v_r14 = (unsigned int)(-(v_r14));
    result = (unsigned int)((result) & (3));
    result = (unsigned int)((result) + (3));
    *(unsigned int *)(result + 24) = (unsigned int)(result);
    *(unsigned int *)(a1 + 220) = (unsigned int)(result);
    *(unsigned int *)(result + 164) = 0x6D746D72ULL;
    *(unsigned int *)(a1 + 172) = 1;
    *(unsigned int *)(a1 + 184) = 1;
    *(unsigned int *)(a1 + 176) = 1;
    *(unsigned __int64 *)(result + 12) = v_stack_p8;
    if (a10 != 0) {
        *(unsigned __int64 *)(result + 112) = v_xmm0;
        *(unsigned __int64 *)(result + 128) = v_xmm1;
    }
    if (a11 != 0) {
        *(unsigned __int64 *)(result + 148) = v_xmm0;
    }
    *(unsigned __int64 *)(a1 + 64) = result;
loc_0087C249:
    result = 0;
    goto loc_0087C0D7;
loc_0087C250:
    if (((unsigned int)(a8)) != ((unsigned int)((unsigned int)(0x31314D43ULL)))) goto loc_0087C2AE;
    *(unsigned __int64 *)(a1 + 64) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) + (0xFFFFF000ULL));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 20))) << (12));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    *(unsigned __int64 *)(a1 + 8) = v_rip - 161303;
    *(unsigned __int64 *)(a1 + 16) = v_rip - 128610;
    *(unsigned int *)(a1 + 220) = (unsigned int)(a1);
    *(unsigned int *)(a1 + 280) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    *(unsigned int *)(a1 + 216) = (unsigned int)(4 - 3);
    if (a15 == 0) goto loc_0087C249;
    *(unsigned int *)(a15) = 0;
    goto loc_0087C249;
loc_0087C2AE:
    if (((unsigned int)(a8)) != 3) goto loc_0087C392;
    result = HvIsInPlaceBaseBlockValid(result, a8, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
    if ((unsigned __int8)(result) != 0) goto loc_0087C2D5;
    v_stack_p20 = 128;
loc_0087C2CB:
    goto loc_0087C0C4;
loc_0087C2D5:
    a3 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) + (0xFFFFF000ULL));
    *(unsigned __int64 *)(a1 + 64) = result;
    *(unsigned int *)(a1 + 216) = (unsigned int)(4 - 3);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 20))) << (12));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    *(unsigned int *)(a1 + 220) = (unsigned int)(a1);
    *(unsigned int *)(result + 4088) = 0;
    *(unsigned int *)(a1 + 172) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    *(unsigned int *)(a1 + 184) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    *(unsigned int *)(a1 + 176) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    result = HvpAdjustHiveFreeDisplay(a1, (unsigned int)(*(unsigned int *)(result + 40)), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))));
    if (!sign_flag) goto loc_0087C33A;
    v_stack_p20 = 144;
    goto loc_0087C0C4;
loc_0087C33A:
    v_stack_p20 = a13;
    result = HvpBuildMapForMemoryBackedHive(a1, result + 4096, (unsigned int)(a9), a12);
    if (!sign_flag) goto loc_0087C379;
    v_stack_p20 = 160;
    goto loc_0087C0C4;
loc_0087C379:
    if (a15 == 0) goto loc_0087C249;
    goto loc_0087C249;
loc_0087C392:
    if (((unsigned int)(result + 4096)) != ((unsigned int)(4 - 3))) goto loc_0087C638;
    if ((*(unsigned int *)(result)) != 0x66676572ULL) goto loc_0087C62B;
    if ((*(unsigned int *)(result + 28)) != 0) goto loc_0087C62B;
    if ((*(unsigned int *)(result + 32)) != ((unsigned int)(4 - 3))) goto loc_0087C62B;
    if ((*(unsigned int *)(result + 20)) > ((unsigned int)(4 - 3))) goto loc_0087C62B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) - (3));
    if (((unsigned int)(result)) > 3) goto loc_0087C62B;
    if ((*(unsigned int *)(result + 40)) > 0x7FFFE000ULL) goto loc_0087C62B;
    result = HvpHeaderCheckSum(result, result + 4096, (unsigned int)(a9), a12);
    if (((unsigned int)(result)) != (*(unsigned int *)(result + 508))) goto loc_0087C62B;
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(a1 + 132)), (unsigned __int8)(a12), (unsigned int)(0x33314D43ULL), a12);
    *(unsigned __int64 *)(a1 + 64) = result;
    if (result != 0) goto loc_0087C42C;
    v_stack_p20 = 192;
    goto loc_0087C0BF;
loc_0087C42C:
    v_r15 = (unsigned int)(((unsigned int)(0x32314D43ULL)) << (9));
    if (((result) & (v_r15 - 1)) == 0) goto loc_0087C49B;
    result = guard_dispatch_icall(result, (unsigned int)(*(unsigned int *)(a1 + 132)), (unsigned int)(0x33314D43ULL), a12);
    result = guard_dispatch_icall((unsigned int)(0x1000ULL), 1, (unsigned int)((unsigned int)((unsigned int)(0x34314D43ULL))), a12);
    *(unsigned __int64 *)(a1 + 64) = result;
    if (result != 0) goto loc_0087C475;
    v_stack_p20 = 208;
    goto loc_0087C0BF;
loc_0087C475:
    *(unsigned int *)(a1 + 132) = 0x1000ULL;
    v_r15 = a1 + 64;
    if (a15 != 0) {
        *(unsigned int *)(a15) = (unsigned int)((unsigned int)(0x34314D43ULL));
        v_r15 = a1 + 64;
    }
    goto loc_0087C4B1;
loc_0087C49B:
    if (a15 != 0) {
        *(unsigned int *)(a15) = 0x33314D43ULL;
    }
loc_0087C4BC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 48) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 80) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 96) = v_xmm0;
    result = (*(unsigned __int64 *)(a1 + 64)) + (128);
    a1 = (result) + (128);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    v_r13 = ((unsigned int)(0x31314D43ULL)) - (1);
    if (condition_is_not_equal) goto loc_0087C4BC;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 4092) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4092)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 4088) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4088)));
    *(unsigned int *)(a1 + 172) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    *(unsigned int *)(a1 + 184) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    *(unsigned int *)(a1 + 176) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 20))) << (12));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 24))) + (0xFFFFF000ULL));
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
    *(unsigned int *)(a1 + 220) = a3;
    a3 = 0;
    result = HvpAdjustHiveFreeDisplay(a1, (unsigned int)(*(unsigned int *)(result + 40)), a3, a12);
    if (!sign_flag) goto loc_0087C58B;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 64), (unsigned int)(*(unsigned int *)(a1 + 132)), a3, a12);
    v_stack_p20 = 224;
    goto loc_0087C0C4;
loc_0087C58B:
    v_stack_p20 = a13;
    result = HvpBuildMapForMemoryBackedHive(a1, result + 4096, (unsigned int)(a9), a12);
    if (!sign_flag) goto loc_0087C5F4;
    a2 = 0;
    v_stack_p20 = 240;
    result = SetFailureLocation(v_stack_p10, a2, a2 + 25, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 64), (unsigned int)(*(unsigned int *)(a1 + 132)), a2 + 25, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0087C0D5;
loc_0087C5F4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 144)))) & (1)) == 0) goto loc_0087C60C;
    if (1 != 0) {
        *(unsigned __int8 *)(1) = 1;
    }
    result = HvpFillFileName(*(unsigned __int64 *)(a1 + 64), a8, a2 + 25, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0087C249;
loc_0087C62B:
    v_stack_p20 = 176;
    goto loc_0087C2CB;
loc_0087C638:
    goto loc_0087C0D7;
loc_0087C642:
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t HvHiveStartMemoryBacked(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, uint32_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(arg1 + 0x38) = Arg16;
    if (((uint32_t)(Arg2)) == ((uint32_t)(5 - 3))) goto loc_0087C642;
    if (((uint32_t)(Arg2)) >= 5) goto loc_0087C642;
    if ((((uint32_t)((uint32_t)(Arg3))) & (0xF5617CECULL)) != 0) goto loc_0087C642;
    if (Arg4 > ((uint32_t)(5 - 3))) goto loc_0087C642;
    if (((uint32_t)((uint32_t)(Arg7) - 1)) > 7) goto loc_0087C642;
    local_r10 = 0;
    if (Arg5 != 0) goto loc_0087BFCE;
    if ((((uint32_t)(Arg2 - 1)) & (0xFFFFFFFCULL)) != 0) goto loc_0087BFCE;
    if (((uint32_t)(Arg2)) != ((uint32_t)(5 - 3))) goto loc_0087C642;
loc_0087BFCE:
    if (Arg14 != 0) {
        *(uint8_t *)(Arg14) = 0;
    }
    result = Arg2 - 1;
    if (Arg6 != 0) {
        result = *(uint64_t *)(Arg6);
        *(uint64_t *)(arg1 + 0x18) = result;
        result = *(uint64_t *)(Arg6 + 0x8);
        *(uint64_t *)(arg1 + 0x20) = result;
        result = *(uint64_t *)(Arg6 + 0x18);
        *(uint64_t *)(arg1 + 0x28) = result;
        result = *(uint64_t *)(Arg6 + 0x20);
        *(uint64_t *)(arg1 + 0x30) = result;
    }
    if (Arg4 != 0) goto loc_0087C023;
    *(uint32_t *)(arg1 + 0xA8) = 0;
    goto loc_0087C033;
loc_0087C023:
    result = 4;
    if (Arg4 == ((uint32_t)(4 - 3))) { result = (uint32_t)(4 - 3); }
    *(uint32_t *)(arg1 + 0xA8) = (uint32_t)(result);
loc_0087C033:
    *(uint32_t *)(arg1 + 0xA0) = (uint32_t)((uint32_t)(Arg3));
    *(uint64_t *)(arg1 + 0x8) = v_rip - 160650;
    *(uint32_t *)(arg1 + 0x88) = (uint32_t)((uint32_t)(Arg7));
    *(uint32_t *)(arg1 + 0xD8) = (uint32_t)(5 - 3);
    Arg4 = (uint8_t)(~((uint8_t)((uint32_t)(Arg3))));
    *(uint64_t *)(arg1 + 0x10) = v_rip - 155936;
    *(uint32_t *)(arg1 + 0x84) = 0x1000ULL;
    Arg4 = (uint8_t)((Arg4) & ((uint8_t)(4 - 3)));
    *(uint64_t *)(arg1 + 0xC8) = *(uint64_t *)(local_rbx);
    *(uint8_t *)(arg1 + 0xC2) = (uint8_t)(4 - 3);
    if ((uint32_t)(Arg2) != 0) goto loc_0087C250;
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(arg1 + 0x84)), (uint8_t)(Arg4), (uint32_t)((uint32_t)((uint32_t)(0x31314D43ULL))), Arg4);
    if (result != 0) goto loc_0087C0F5;
    v_stack_m38 = 96;
loc_0087C0BF:
loc_0087C0C4:
    Arg2 = 0;
    result = SetFailureLocation(Arg16, Arg2, Arg2 + 25, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
loc_0087C0D5:
loc_0087C0D7:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
loc_0087C0F5:
    local_r15 = (uint32_t)(((uint32_t)(Arg7)) << (9));
    local_r15 = (uint32_t)((local_r15) - (1));
    if (((v_stack_p18) & ((uint32_t)((uint32_t)(local_r15)))) == 0) goto loc_0087C167;
    result = guard_dispatch_icall(v_stack_p18, (uint32_t)(*(uint32_t *)(arg1 + 0x84)), Arg2 + 25, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
    result = guard_dispatch_icall((uint32_t)(0x1000ULL), 1, (uint32_t)((uint32_t)((uint32_t)(0x32314D43ULL))), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
    if (result != 0) goto loc_0087C14B;
    v_stack_p20 = 112;
    goto loc_0087C0BF;
loc_0087C14B:
    *(uint32_t *)(arg1 + 0x84) = 0x1000ULL;
    if (Arg15 == 0) goto loc_0087C177;
    *(uint32_t *)(Arg15) = (uint32_t)((uint32_t)(0x32314D43ULL));
    goto loc_0087C177;
loc_0087C167:
    if (Arg15 != 0) {
        *(uint32_t *)(Arg15) = (uint32_t)((uint32_t)(0x31314D43ULL));
    }
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
    *(uint32_t *)(result) = 0x66676572ULL;
    *(uint32_t *)(result + 0x4) = 1;
    *(uint32_t *)(result + 0x8) = 1;
    *(uint32_t *)(result + 0x20) = 1;
    *(uint32_t *)(result + 0x2C) = 1;
    result = HvpFillFileName(result, Arg8, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
    local_r14 = (uint32_t)(((uint32_t)(Arg3)) & (0x80000ULL));
    if (!(condition_is_equal)) {
        *(uint32_t *)(result + 0x90) = 2;
    }
    *(uint32_t *)(result + 0x14) = 1;
    local_r14 = (uint32_t)(-(local_r14));
    result = (uint32_t)((result) & (3));
    result = (uint32_t)((result) + (3));
    *(uint32_t *)(result + 0x18) = (uint32_t)(result);
    *(uint32_t *)(arg1 + 0xDC) = (uint32_t)(result);
    *(uint32_t *)(result + 0xA4) = 0x6D746D72ULL;
    *(uint32_t *)(arg1 + 0xAC) = 1;
    *(uint32_t *)(arg1 + 0xB8) = 1;
    *(uint32_t *)(arg1 + 0xB0) = 1;
    *(uint64_t *)(result + 0xC) = v_stack_p8;
    if (Arg10 != 0) {
        *(uint64_t *)(result + 0x70) = v_xmm0;
        *(uint64_t *)(result + 0x80) = v_xmm1;
    }
    if (Arg11 != 0) {
        *(uint64_t *)(result + 0x94) = v_xmm0;
    }
    *(uint64_t *)(arg1 + 0x40) = result;
loc_0087C249:
    result = 0;
    goto loc_0087C0D7;
loc_0087C250:
    if (((uint32_t)(Arg8)) != ((uint32_t)((uint32_t)(0x31314D43ULL)))) goto loc_0087C2AE;
    *(uint64_t *)(arg1 + 0x40) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) + (0xFFFFF000ULL));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x14))) << (12));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    *(uint64_t *)(arg1 + 0x8) = v_rip - 161303;
    *(uint64_t *)(arg1 + 0x10) = v_rip - 128610;
    *(uint32_t *)(arg1 + 0xDC) = (uint32_t)(Arg1);
    *(uint32_t *)(arg1 + 0x118) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    *(uint32_t *)(arg1 + 0xD8) = (uint32_t)(4 - 3);
    if (Arg15 == 0) goto loc_0087C249;
    *(uint32_t *)(Arg15) = 0;
    goto loc_0087C249;
loc_0087C2AE:
    if (((uint32_t)(Arg8)) != 3) goto loc_0087C392;
    result = HvIsInPlaceBaseBlockValid(result, Arg8, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
    if ((uint8_t)(result) != 0) goto loc_0087C2D5;
    v_stack_p20 = 128;
loc_0087C2CB:
    goto loc_0087C0C4;
loc_0087C2D5:
    Arg3 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) + (0xFFFFF000ULL));
    *(uint64_t *)(arg1 + 0x40) = result;
    *(uint32_t *)(arg1 + 0xD8) = (uint32_t)(4 - 3);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x14))) << (12));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0xDC) = (uint32_t)(Arg1);
    *(uint32_t *)(result + 0xFF8) = 0;
    *(uint32_t *)(arg1 + 0xAC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    *(uint32_t *)(arg1 + 0xB8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    *(uint32_t *)(arg1 + 0xB0) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    result = HvpAdjustHiveFreeDisplay(Arg1, (uint32_t)(*(uint32_t *)(result + 0x28)), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))));
    if (!sign_flag) goto loc_0087C33A;
    v_stack_p20 = 144;
    goto loc_0087C0C4;
loc_0087C33A:
    v_stack_p20 = Arg13;
    result = HvpBuildMapForMemoryBackedHive(Arg1, result + 4096, (uint32_t)(Arg9), Arg12);
    if (!sign_flag) goto loc_0087C379;
    v_stack_p20 = 160;
    goto loc_0087C0C4;
loc_0087C379:
    if (Arg15 == 0) goto loc_0087C249;
    goto loc_0087C249;
loc_0087C392:
    if (((uint32_t)(result + 4096)) != ((uint32_t)(4 - 3))) goto loc_0087C638;
    if ((*(uint32_t *)(result)) != 0x66676572ULL) goto loc_0087C62B;
    if ((*(uint32_t *)(result + 0x1C)) != 0) goto loc_0087C62B;
    if ((*(uint32_t *)(result + 0x20)) != ((uint32_t)(4 - 3))) goto loc_0087C62B;
    if ((*(uint32_t *)(result + 0x14)) > ((uint32_t)(4 - 3))) goto loc_0087C62B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) - (3));
    if (((uint32_t)(result)) > 3) goto loc_0087C62B;
    if ((*(uint32_t *)(result + 0x28)) > 0x7FFFE000ULL) goto loc_0087C62B;
    result = HvpHeaderCheckSum(result, result + 4096, (uint32_t)(Arg9), Arg12);
    if (((uint32_t)(result)) != (*(uint32_t *)(result + 0x1FC))) goto loc_0087C62B;
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(arg1 + 0x84)), (uint8_t)(Arg12), (uint32_t)(0x33314D43ULL), Arg12);
    *(uint64_t *)(arg1 + 0x40) = result;
    if (result != 0) goto loc_0087C42C;
    v_stack_p20 = 192;
    goto loc_0087C0BF;
loc_0087C42C:
    local_r15 = (uint32_t)(((uint32_t)(0x32314D43ULL)) << (9));
    if (((result) & (local_r15 - 1)) == 0) goto loc_0087C49B;
    result = guard_dispatch_icall(result, (uint32_t)(*(uint32_t *)(arg1 + 0x84)), (uint32_t)(0x33314D43ULL), Arg12);
    result = guard_dispatch_icall((uint32_t)(0x1000ULL), 1, (uint32_t)((uint32_t)((uint32_t)(0x34314D43ULL))), Arg12);
    *(uint64_t *)(arg1 + 0x40) = result;
    if (result != 0) goto loc_0087C475;
    v_stack_p20 = 208;
    goto loc_0087C0BF;
loc_0087C475:
    *(uint32_t *)(arg1 + 0x84) = 0x1000ULL;
    local_r15 = Arg1 + 64;
    if (Arg15 != 0) {
        *(uint32_t *)(Arg15) = (uint32_t)((uint32_t)(0x34314D43ULL));
        local_r15 = Arg1 + 64;
    }
    goto loc_0087C4B1;
loc_0087C49B:
    if (Arg15 != 0) {
        *(uint32_t *)(Arg15) = 0x33314D43ULL;
    }
loc_0087C4BC:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x30) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x50) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x60) = v_xmm0;
    result = (*(uint64_t *)(arg1 + 0x40)) + (128);
    Arg1 = (result) + (128);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    local_r13 = ((uint32_t)(0x31314D43ULL)) - (1);
    if (condition_is_not_equal) goto loc_0087C4BC;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0xFFC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xFFC)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0xFF8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xFF8)));
    *(uint32_t *)(arg1 + 0xAC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    *(uint32_t *)(arg1 + 0xB8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    *(uint32_t *)(arg1 + 0xB0) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x14))) << (12));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x18))) + (0xFFFFF000ULL));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0xDC) = Arg3;
    Arg3 = 0;
    result = HvpAdjustHiveFreeDisplay(Arg1, (uint32_t)(*(uint32_t *)(result + 0x28)), Arg3, Arg12);
    if (!sign_flag) goto loc_0087C58B;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x40), (uint32_t)(*(uint32_t *)(arg1 + 0x84)), Arg3, Arg12);
    v_stack_p20 = 224;
    goto loc_0087C0C4;
loc_0087C58B:
    v_stack_p20 = Arg13;
    result = HvpBuildMapForMemoryBackedHive(Arg1, result + 4096, (uint32_t)(Arg9), Arg12);
    if (!sign_flag) goto loc_0087C5F4;
    Arg2 = 0;
    v_stack_p20 = 240;
    result = SetFailureLocation(v_stack_p10, Arg2, Arg2 + 25, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x40), (uint32_t)(*(uint32_t *)(arg1 + 0x84)), Arg2 + 25, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0087C0D5;
loc_0087C5F4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x90)))) & (1)) == 0) goto loc_0087C60C;
    if (1 != 0) {
        *(uint8_t *)(1) = 1;
    }
    result = HvpFillFileName(*(uint64_t *)(arg1 + 0x40), Arg8, Arg2 + 25, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0087C249;
loc_0087C62B:
    v_stack_p20 = 176;
    goto loc_0087C2CB;
loc_0087C638:
    goto loc_0087C0D7;
loc_0087C642:
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x84` | `32` | `R` |
| `Arg1` | `+ 0x84` | `32` | `W` |
| `Arg1` | `+ 0x88` | `32` | `W` |
| `Arg1` | `+ 0x8C` | `8` | `R/W` |
| `Arg1` | `+ 0xA0` | `32` | `W` |
| `Arg1` | `+ 0xA8` | `32` | `W` |
| `Arg1` | `+ 0xAC` | `32` | `W` |
| `Arg1` | `+ 0xB0` | `32` | `W` |
| `Arg1` | `+ 0xB8` | `32` | `W` |
| `Arg1` | `+ 0xC2` | `8` | `W` |
| `Arg1` | `+ 0xC8` | `64` | `W` |
| `Arg1` | `+ 0xD8` | `32` | `W` |
| `Arg1` | `+ 0xDC` | `32` | `W` |
| `Arg1` | `+ 0x118` | `32` | `W` |
| `Arg7` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087BF38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
