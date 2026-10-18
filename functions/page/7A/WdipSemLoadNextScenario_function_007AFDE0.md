# WdipSemLoadNextScenario

- RVA: `0x007AFDE0`–`0x007B02D2` (길이 `1,266` bytes)
- VA: `0x00000001407AFDE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2FF8`
- 디코드: `320`개 명령, `1,266/1,266` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x007AFE73` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007AFE97` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x007AFECF` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007AFEE0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007AFF61` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007AFF70` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007AFF7F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007AFF8E` → [WdipSemFastFree](../70/WdipSemFastFree_function_0070303C.md) (function, `0x0070303C`)
- `0x007AFF9F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x007AFFDA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007AFFE7` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x007B0007` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007B001B` → [RtlUnicodeStringToInteger](../99/RtlUnicodeStringToInteger_function_00993480.md) (function, `0x00993480`)
- `0x007B003F` → [WdipSemOpenRegistryKey](../7B/WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B0079` → [WdipSemQueryValueFromRegistry](../7B/WdipSemQueryValueFromRegistry_function_007B185C.md) (function, `0x007B185C`)
- `0x007B00D7` → [WdipSemQueryValueFromRegistry](../7B/WdipSemQueryValueFromRegistry_function_007B185C.md) (function, `0x007B185C`)
- `0x007B0132` → [WdipSemQueryValueFromRegistry](../7B/WdipSemQueryValueFromRegistry_function_007B185C.md) (function, `0x007B185C`)
- `0x007B0164` → [WdipSemOpenRegistryKey](../7B/WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B017F` → [WdipSemFastAllocate](../A5/WdipSemFastAllocate_function_00A5DC04.md) (function, `0x00A5DC04`)
- `0x007B01A9` → [WdipSemLoadNextEndEvent](WdipSemLoadNextEndEvent_function_007AFAD0.md) (function, `0x007AFAD0`)
- `0x007B01E6` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007B0202` → [WdipSemWriteScenarioLimitExceededEvent](../7B/WdipSemWriteScenarioLimitExceededEvent_function_007B15AC.md) (function, `0x007B15AC`)
- `0x007B0230` → [WdipSemOpenRegistryKey](../7B/WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B0259` → [WdipSemLoadNextContextProvider](WdipSemLoadNextContextProvider_function_007AF820.md) (function, `0x007AF820`)
- `0x007B028E` → [WdipSemFastAllocate](../A5/WdipSemFastAllocate_function_00A5DC04.md) (function, `0x00A5DC04`)
- `0x007B02B3` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007B02CC` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)

### Direct callers
- [WdipSemLoadScenarioTable](../7B/WdipSemLoadScenarioTable_function_007B02D8.md) at `0x007B0646`

### Static image references
- `0x007AFDFF` → RVA `0x00E0A740` (`.data`; read)
- `0x007B005D` → RVA `0x00B06D40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B00BC` → RVA `0x00B06D90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B0118` → RVA `0x00B06C60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B015D` → RVA `0x00B06C40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B01D8` → RVA `0x00F01DD0` (`.data`; read)
- `0x007B01DF` → RVA `0x00021520` (`.rdata`; read)
- `0x007B0229` → RVA `0x00B06D10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B02AC` → RVA `0x000217B8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x007AFE73` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007AFE97` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x007AFECF` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007AFEE0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007AFF61` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007AFF70` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007AFF7F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007AFF9F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x007AFFDA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007B0007` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007B01E6` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007B02B3` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007B02CC` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007AFDE0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007AFDE5  55                              push rbp
007AFDE6  56                              push rsi
007AFDE7  57                              push rdi
007AFDE8  41 54                           push r12
007AFDEA  41 55                           push r13
007AFDEC  41 56                           push r14
007AFDEE  41 57                           push r15
007AFDF0  48 8D AC 24 E0 FE FF FF         lea rbp, [rsp - 0x120]
007AFDF8  48 81 EC 20 02 00 00            sub rsp, 0x220
007AFDFF  48 8B 05 3A A9 65 00            mov rax, qword ptr [rip + 0x65a93a]
007AFE06  48 33 C4                        xor rax, rsp
007AFE09  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
007AFE10  45 33 E4                        xor r12d, r12d
007AFE13  0F 57 C0                        xorps xmm0, xmm0
007AFE16  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
007AFE1B  49 8B F8                        mov rdi, r8
007AFE1E  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
007AFE23  8B DA                           mov ebx, edx
007AFE25  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
007AFE2A  4C 8B F9                        mov r15, rcx
007AFE2D  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
007AFE32  41 8B F4                        mov esi, r12d
007AFE35  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
007AFE3A  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
007AFE3F  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
007AFE44  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
007AFE49  45 0F B6 F4                     movzx r14d, r12b
007AFE4D  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
007AFE52  48 85 C9                        test rcx, rcx
007AFE55  75 0A                           jne 0x1407afe61
007AFE57  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007AFE5C  E9 32 01 00 00                  jmp 0x1407aff93
007AFE61  48 85 FF                        test rdi, rdi
007AFE64  74 F1                           je 0x1407afe57
007AFE66  33 D2                           xor edx, edx
007AFE68  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
007AFE6D  41 B8 98 00 00 00               mov r8d, 0x98
007AFE73  E8 C8 6D F1 FF                  call 0x1406c6c40
007AFE78  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007AFE7D  45 33 C0                        xor r8d, r8d
007AFE80  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007AFE85  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
007AFE8A  8B D3                           mov edx, ebx
007AFE8C  C7 44 24 20 96 00 00 00         mov dword ptr [rsp + 0x20], 0x96
007AFE94  49 8B CF                        mov rcx, r15
007AFE97  E8 74 D8 EF FF                  call 0x1406ad710
007AFE9C  8B D8                           mov ebx, eax
007AFE9E  85 C0                           test eax, eax
007AFEA0  0F 88 B1 00 00 00               js 0x1407aff57
007AFEA6  BB 80 00 00 00                  mov ebx, 0x80
007AFEAB  39 5D 84                        cmp dword ptr [rbp - 0x7c], ebx
007AFEAE  72 0A                           jb 0x1407afeba
007AFEB0  BB 05 00 00 80                  mov ebx, 0x80000005
007AFEB5  E9 9D 00 00 00                  jmp 0x1407aff57
007AFEBA  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
007AFEBD  48 8D 4D 10                     lea rcx, [rbp + 0x10]
007AFEC1  48 D1 E8                        shr rax, 1
007AFEC4  4C 8B C3                        mov r8, rbx
007AFEC7  33 D2                           xor edx, edx
007AFEC9  66 44 89 64 45 88               mov word ptr [rbp + rax*2 - 0x78], r12w
007AFECF  E8 6C 6D F1 FF                  call 0x1406c6c40
007AFED4  4C 8B C3                        mov r8, rbx
007AFED7  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007AFEDE  33 D2                           xor edx, edx
007AFEE0  E8 5B 6D F1 FF                  call 0x1406c6c40
007AFEE5  41 8B D4                        mov edx, r12d
007AFEE8  41 BD 01 00 00 00               mov r13d, 1
007AFEEE  83 FA 40                        cmp edx, 0x40
007AFEF1  73 5F                           jae 0x1407aff52
007AFEF3  8B C2                           mov eax, edx
007AFEF5  48 03 C0                        add rax, rax
007AFEF8  0F B7 4C 05 88                  movzx ecx, word ptr [rbp + rax - 0x78]
007AFEFD  66 83 F9 3B                     cmp cx, 0x3b
007AFF01  74 0A                           je 0x1407aff0d
007AFF03  66 89 4C 05 10                  mov word ptr [rbp + rax + 0x10], cx
007AFF08  41 03 D5                        add edx, r13d
007AFF0B  EB E1                           jmp 0x1407afeee
007AFF0D  48 3B C3                        cmp rax, rbx
007AFF10  0F 83 B6 03 00 00               jae 0x1407b02cc
007AFF16  41 03 D5                        add edx, r13d
007AFF19  66 44 89 64 05 10               mov word ptr [rbp + rax + 0x10], r12w
007AFF1F  45 8B C4                        mov r8d, r12d
007AFF22  83 FA 40                        cmp edx, 0x40
007AFF25  73 2B                           jae 0x1407aff52
007AFF27  4C 8D 4D 88                     lea r9, [rbp - 0x78]
007AFF2B  4D 8D 0C 51                     lea r9, [r9 + rdx*2]
007AFF2F  41 0F B7 09                     movzx ecx, word ptr [r9]
007AFF33  41 8B C0                        mov eax, r8d
007AFF36  66 89 8C 45 90 00 00 00         mov word ptr [rbp + rax*2 + 0x90], cx
007AFF3E  66 85 C9                        test cx, cx
007AFF41  74 7D                           je 0x1407affc0
007AFF43  41 03 D5                        add edx, r13d
007AFF46  49 83 C1 02                     add r9, 2
007AFF4A  45 03 C5                        add r8d, r13d
007AFF4D  83 FA 40                        cmp edx, 0x40
007AFF50  72 DD                           jb 0x1407aff2f
007AFF52  BB 01 00 00 C0                  mov ebx, 0xc0000001
007AFF57  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007AFF5C  48 85 C9                        test rcx, rcx
007AFF5F  74 05                           je 0x1407aff66
007AFF61  E8 4A D3 EF FF                  call 0x1406ad2b0
007AFF66  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007AFF6B  48 85 C9                        test rcx, rcx
007AFF6E  74 05                           je 0x1407aff75
007AFF70  E8 3B D3 EF FF                  call 0x1406ad2b0
007AFF75  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007AFF7A  48 85 C9                        test rcx, rcx
007AFF7D  74 05                           je 0x1407aff84
007AFF7F  E8 2C D3 EF FF                  call 0x1406ad2b0
007AFF84  48 85 F6                        test rsi, rsi
007AFF87  74 0A                           je 0x1407aff93
007AFF89  48 8B D6                        mov rdx, rsi
007AFF8C  33 C9                           xor ecx, ecx
007AFF8E  E8 A9 30 F5 FF                  call 0x14070303c
007AFF93  8B C3                           mov eax, ebx
007AFF95  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
007AFF9C  48 33 CC                        xor rcx, rsp
007AFF9F  E8 9C C6 EF FF                  call 0x1406ac640
007AFFA4  48 8B 9C 24 78 02 00 00         mov rbx, qword ptr [rsp + 0x278]
007AFFAC  48 81 C4 20 02 00 00            add rsp, 0x220
007AFFB3  41 5F                           pop r15
007AFFB5  41 5E                           pop r14
007AFFB7  41 5D                           pop r13
007AFFB9  41 5C                           pop r12
007AFFBB  5F                              pop rdi
007AFFBC  5E                              pop rsi
007AFFBD  5D                              pop rbp
007AFFBE  C3                              ret
007AFFBF  CC                              int3
007AFFC0  45 3B C5                        cmp r8d, r13d
007AFFC3  75 0C                           jne 0x1407affd1
007AFFC5  66 83 BD 90 00 00 00 2A         cmp word ptr [rbp + 0x90], 0x2a
007AFFCD  45 0F 44 F5                     cmove r14d, r13d
007AFFD1  48 8D 55 10                     lea rdx, [rbp + 0x10]
007AFFD5  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007AFFDA  E8 A1 A7 C7 FF                  call 0x14042a780
007AFFDF  48 8B D7                        mov rdx, rdi
007AFFE2  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007AFFE7  E8 04 1F 14 00                  call 0x1408f1ef0
007AFFEC  8B D8                           mov ebx, eax
007AFFEE  85 C0                           test eax, eax
007AFFF0  0F 88 61 FF FF FF               js 0x1407aff57
007AFFF6  45 84 F6                        test r14b, r14b
007AFFF9  75 38                           jne 0x1407b0033
007AFFFB  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
007B0002  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007B0007  E8 74 A7 C7 FF                  call 0x14042a780
007B000C  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007B0011  BA 0A 00 00 00                  mov edx, 0xa
007B0016  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007B001B  E8 60 34 1E 00                  call 0x140993480
007B0020  8B D8                           mov ebx, eax
007B0022  85 C0                           test eax, eax
007B0024  0F 88 2D FF FF FF               js 0x1407aff57
007B002A  0F B7 44 24 40                  movzx eax, word ptr [rsp + 0x40]
007B002F  66 89 47 10                     mov word ptr [rdi + 0x10], ax
007B0033  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
007B0038  49 8B D7                        mov rdx, r15
007B003B  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007B003F  E8 84 17 00 00                  call 0x1407b17c8
007B0044  8B D8                           mov ebx, eax
007B0046  85 C0                           test eax, eax
007B0048  0F 88 09 FF FF FF               js 0x1407aff57
007B004E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B0053  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B0058  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B005D  48 8D 15 DC 6C 35 00            lea rdx, [rip + 0x356cdc]
007B0064  48 8D 44 24 44                  lea rax, [rsp + 0x44]
007B0069  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B006E  B8 04 00 00 00                  mov eax, 4
007B0073  44 8B C8                        mov r9d, eax
007B0076  44 8B C0                        mov r8d, eax
007B0079  E8 DE 17 00 00                  call 0x1407b185c
007B007E  8B D8                           mov ebx, eax
007B0080  41 BF 34 00 00 C0               mov r15d, 0xc0000034
007B0086  85 C0                           test eax, eax
007B0088  79 0F                           jns 0x1407b0099
007B008A  41 3B C7                        cmp eax, r15d
007B008D  0F 85 C4 FE FF FF               jne 0x1407aff57
007B0093  C6 47 12 FF                     mov byte ptr [rdi + 0x12], 0xff
007B0097  EB 14                           jmp 0x1407b00ad
007B0099  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
007B009D  BA FF 00 00 00                  mov edx, 0xff
007B00A2  85 C0                           test eax, eax
007B00A4  0F B6 C8                        movzx ecx, al
007B00A7  0F 44 CA                        cmove ecx, edx
007B00AA  88 4F 12                        mov byte ptr [rdi + 0x12], cl
007B00AD  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B00B2  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B00B7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B00BC  48 8D 15 CD 6C 35 00            lea rdx, [rip + 0x356ccd]
007B00C3  41 B9 08 00 00 00               mov r9d, 8
007B00C9  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007B00CE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B00D3  45 8D 41 03                     lea r8d, [r9 + 3]
007B00D7  E8 80 17 00 00                  call 0x1407b185c
007B00DC  8B D8                           mov ebx, eax
007B00DE  85 C0                           test eax, eax
007B00E0  79 13                           jns 0x1407b00f5
007B00E2  41 3B C7                        cmp eax, r15d
007B00E5  0F 85 6C FE FF FF               jne 0x1407aff57
007B00EB  48 83 C9 FF                     or rcx, 0xffffffffffffffff
007B00EF  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
007B00F3  EB 14                           jmp 0x1407b0109
007B00F5  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007B00FA  48 83 C9 FF                     or rcx, 0xffffffffffffffff
007B00FE  48 85 C0                        test rax, rax
007B0101  48 0F 44 C1                     cmove rax, rcx
007B0105  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
007B0109  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B010E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B0113  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B0118  48 8D 15 41 6B 35 00            lea rdx, [rip + 0x356b41]
007B011F  41 B8 04 00 00 00               mov r8d, 4
007B0125  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007B012A  45 8B C8                        mov r9d, r8d
007B012D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B0132  E8 25 17 00 00                  call 0x1407b185c
007B0137  8B D8                           mov ebx, eax
007B0139  85 C0                           test eax, eax
007B013B  79 0F                           jns 0x1407b014c
007B013D  41 3B C7                        cmp eax, r15d
007B0140  0F 85 11 FE FF FF               jne 0x1407aff57
007B0146  44 89 67 24                     mov dword ptr [rdi + 0x24], r12d
007B014A  EB 07                           jmp 0x1407b0153
007B014C  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
007B0150  89 47 24                        mov dword ptr [rdi + 0x24], eax
007B0153  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
007B0158  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
007B015D  48 8D 0D DC 6A 35 00            lea rcx, [rip + 0x356adc]
007B0164  E8 5F 16 00 00                  call 0x1407b17c8
007B0169  85 C0                           test eax, eax
007B016B  79 08                           jns 0x1407b0175
007B016D  41 8B DC                        mov ebx, r12d
007B0170  E9 E2 FD FF FF                  jmp 0x1407aff57
007B0175  45 8B FC                        mov r15d, r12d
007B0178  BA 30 00 00 00                  mov edx, 0x30
007B017D  33 C9                           xor ecx, ecx
007B017F  E8 80 DA 2A 00                  call 0x140a5dc04
007B0184  48 8B F0                        mov rsi, rax
007B0187  48 85 C0                        test rax, rax
007B018A  0F 84 0B 01 00 00               je 0x1407b029b
007B0190  0F 57 C0                        xorps xmm0, xmm0
007B0193  4C 8B C0                        mov r8, rax
007B0196  0F 11 00                        movups xmmword ptr [rax], xmm0
007B0199  41 8B D7                        mov edx, r15d
007B019C  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
007B01A0  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
007B01A4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007B01A9  E8 22 F9 FF FF                  call 0x1407afad0
007B01AE  45 03 FD                        add r15d, r13d
007B01B1  8B D8                           mov ebx, eax
007B01B3  3D 1A 00 00 80                  cmp eax, 0x8000001a
007B01B8  74 52                           je 0x1407b020c
007B01BA  85 C0                           test eax, eax
007B01BC  0F 88 95 FD FF FF               js 0x1407aff57
007B01C2  8B 47 34                        mov eax, dword ptr [rdi + 0x34]
007B01C5  83 F8 10                        cmp eax, 0x10
007B01C8  73 0E                           jae 0x1407b01d8
007B01CA  48 89 B4 C7 18 04 00 00         mov qword ptr [rdi + rax*8 + 0x418], rsi
007B01D2  44 01 6F 34                     add dword ptr [rdi + 0x34], r13d
007B01D6  EB A0                           jmp 0x1407b0178
007B01D8  48 8B 0D F1 1B 75 00            mov rcx, qword ptr [rip + 0x751bf1]
007B01DF  48 8D 15 3A 13 87 FF            lea rdx, [rip - 0x78ecc6]
007B01E6  E8 65 22 BE FF                  call 0x140392450
007B01EB  84 C0                           test al, al
007B01ED  0F 84 5F FD FF FF               je 0x1407aff52
007B01F3  48 8D 0D 26 13 87 FF            lea rcx, [rip - 0x78ecda]
007B01FA  44 0F B7 47 10                  movzx r8d, word ptr [rdi + 0x10]
007B01FF  48 8B D7                        mov rdx, rdi
007B0202  E8 A5 13 00 00                  call 0x1407b15ac
007B0207  E9 46 FD FF FF                  jmp 0x1407aff52
007B020C  44 39 67 34                     cmp dword ptr [rdi + 0x34], r12d
007B0210  0F 84 57 FF FF FF               je 0x1407b016d
007B0216  45 84 F6                        test r14b, r14b
007B0219  0F 85 33 FD FF FF               jne 0x1407aff52
007B021F  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
007B0224  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
007B0229  48 8D 0D E0 6A 35 00            lea rcx, [rip + 0x356ae0]
007B0230  E8 93 15 00 00                  call 0x1407b17c8
007B0235  85 C0                           test eax, eax
007B0237  0F 88 30 FF FF FF               js 0x1407b016d
007B023D  45 8B F4                        mov r14d, r12d
007B0240  0F 57 C0                        xorps xmm0, xmm0
007B0243  4C 8B C6                        mov r8, rsi
007B0246  0F 11 06                        movups xmmword ptr [rsi], xmm0
007B0249  41 8B D6                        mov edx, r14d
007B024C  0F 11 46 10                     movups xmmword ptr [rsi + 0x10], xmm0
007B0250  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
007B0254  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007B0259  E8 C2 F5 FF FF                  call 0x1407af820
007B025E  45 03 F5                        add r14d, r13d
007B0261  8B D8                           mov ebx, eax
007B0263  3D 1A 00 00 80                  cmp eax, 0x8000001a
007B0268  0F 84 FF FE FF FF               je 0x1407b016d
007B026E  85 C0                           test eax, eax
007B0270  0F 88 E1 FC FF FF               js 0x1407aff57
007B0276  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
007B0279  83 F8 7C                        cmp eax, 0x7c
007B027C  73 27                           jae 0x1407b02a5
007B027E  48 89 74 C7 38                  mov qword ptr [rdi + rax*8 + 0x38], rsi
007B0283  BA 30 00 00 00                  mov edx, 0x30
007B0288  44 01 6F 30                     add dword ptr [rdi + 0x30], r13d
007B028C  33 C9                           xor ecx, ecx
007B028E  E8 71 D9 2A 00                  call 0x140a5dc04
007B0293  48 8B F0                        mov rsi, rax
007B0296  48 85 C0                        test rax, rax
007B0299  75 A5                           jne 0x1407b0240
007B029B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007B02A0  E9 B2 FC FF FF                  jmp 0x1407aff57
007B02A5  48 8B 0D 24 1B 75 00            mov rcx, qword ptr [rip + 0x751b24]
007B02AC  48 8D 15 05 15 87 FF            lea rdx, [rip - 0x78eafb]
007B02B3  E8 98 21 BE FF                  call 0x140392450
007B02B8  84 C0                           test al, al
007B02BA  0F 84 92 FC FF FF               je 0x1407aff52
007B02C0  48 8D 0D F1 14 87 FF            lea rcx, [rip - 0x78eb0f]
007B02C7  E9 2E FF FF FF                  jmp 0x1407b01fa
007B02CC  E8 0B 5D D4 FF                  call 0x1404f5fdc
007B02D1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemLoadNextScenario(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned int v_stack_m214;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (544);
    result = (*(unsigned __int64 *)(v_rip + 6662458)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_stack_m220 = 0;
    v_stack_m208 = 0;
    v_stack_m200 = 0;
    v_stack_m228 = 0;
    v_stack_m218 = 0;
    v_stack_m214 = 0;
    v_stack_m210 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1F0 = v_xmm0;
    if (a1 != 0) goto loc_007AFE61;
loc_007AFE57:
    goto loc_007AFF93;
loc_007AFE61:
    if (a3 == 0) goto loc_007AFE57;
    a2 = 0;
    result = memset(v_stack_m1E0, a2, 152, a4);
    a3 = 0;
    v_stack_m230 = v_stack_m228;
    v_stack_m238 = 150;
    result = ZwEnumerateKey(a1, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), a3, v_stack_m1E0);
    if (sign_flag) goto loc_007AFF57;
    if (v_stack_m1D4 < 128) goto loc_007AFEBA;
    goto loc_007AFF57;
loc_007AFEBA:
    result = ((unsigned int)(v_stack_m1D4)) >> (1);
    a2 = 0;
    *(unsigned __int16 *)(v_stack_m158 + result * 2 - 120) = 0;
    result = memset(v_stack_m148, a2, (unsigned int)(0x80000005ULL), v_stack_m1E0);
    a2 = 0;
    result = memset(v_stack_mC8, a2, (unsigned int)(0x80000005ULL), v_stack_m1E0);
loc_007AFEEE:
    if (0 >= 64) goto loc_007AFF52;
    result = (0) + (0);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m158 + result * 1 - 120))) == 59) goto loc_007AFF0D;
    *(unsigned __int16 *)(v_stack_m158 + result * 1 + 16) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m158 + result * 1 - 120));
    a2 = (unsigned int)((0) + (1));
    goto loc_007AFEEE;
loc_007AFF0D:
    if (result >= ((unsigned int)(0x80000005ULL))) goto loc_007B02CC;
    a2 = (unsigned int)((a2) + (1));
    *(unsigned __int16 *)(v_stack_m158 + result * 1 + 16) = 0;
    if (a2 >= 64) goto loc_007AFF52;
loc_007AFF2F:
    *(unsigned __int16 *)(v_stack_m158 + 0 * 2 + 144) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1D0 + a2 * 2));
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1D0 + a2 * 2)) == 0) goto loc_007AFFC0;
    a2 = (unsigned int)((a2) + (1));
    a4 = (v_stack_m1D0 + a2 * 2) + (2);
    a3 = (unsigned int)((0) + (1));
    if (a2 < 64) goto loc_007AFF2F;
loc_007AFF52:
loc_007AFF57:
    result = 0;
    if (v_stack_m220 != 0) {
        result = ZwClose(v_stack_m220, a2, a3, a4);
    }
    if (v_stack_m208 != 0) {
        result = ZwClose(v_stack_m208, a2, a3, a4);
    }
    if (v_stack_m200 != 0) {
        result = ZwClose(v_stack_m200, a2, a3, a4);
    }
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = WdipSemFastFree(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (544);
    return result;
loc_007AFFC0:
    v_r14 = 0;
    if (((unsigned int)(a3)) == 1) {
        v_r14 = 0;
        if (v_stack_mC8 == 42) { v_r14 = 1; }
    }
    result = RtlInitUnicodeString(v_stack_p68, v_stack_m148, a3, a4);
    result = RtlGUIDFromString(v_stack_p68, a3, a3, a4);
    if (sign_flag) goto loc_007AFF57;
    if ((unsigned __int8)(v_r14) != 0) goto loc_007B0033;
    result = RtlInitUnicodeString(v_stack_p68, v_stack_mC8, a3, a4);
    result = RtlUnicodeStringToInteger(v_stack_p68, 10, v_stack_p40, a4);
    if (sign_flag) goto loc_007AFF57;
    *(unsigned __int16 *)(a3 + 16) = (unsigned __int16)(v_stack_p40);
loc_007B0033:
    result = WdipSemOpenRegistryKey(v_stack_m1D0, a1, v_stack_p38, a4);
    if (sign_flag) goto loc_007AFF57;
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p44;
    result = WdipSemQueryValueFromRegistry(v_stack_p38, v_rip + 3501276, 4, 4);
    if (!sign_flag) goto loc_007B0099;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_007AFF57;
    *(unsigned __int8 *)(a3 + 18) = 255;
    goto loc_007B00AD;
loc_007B0099:
    a1 = (unsigned __int8)((unsigned int)(v_stack_p44));
    if ((unsigned int)((unsigned int)(v_stack_p44)) == 0) { a1 = 255; }
    *(unsigned __int8 *)(a3 + 18) = (unsigned __int8)(a1);
loc_007B00AD:
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p60;
    result = WdipSemQueryValueFromRegistry(v_stack_p38, v_rip + 3501261, 8 + 3, 8);
    if (!sign_flag) goto loc_007B00F5;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_007AFF57;
    a1 = (v_stack_p38) | (-1);
    *(unsigned __int64 *)(a3 + 24) = a1;
    goto loc_007B0109;
loc_007B00F5:
    a1 = (a1) | (-1);
    result = v_stack_p60;
    if (v_stack_p60 == 0) { result = a1; }
    *(unsigned __int64 *)(a3 + 24) = result;
loc_007B0109:
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p48;
    result = WdipSemQueryValueFromRegistry(v_stack_p38, v_rip + 3500865, 4, 4);
    if (!sign_flag) goto loc_007B014C;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_007AFF57;
    *(unsigned int *)(a3 + 36) = 0;
    goto loc_007B0153;
loc_007B014C:
    *(unsigned int *)(a3 + 36) = (unsigned int)((unsigned int)(v_stack_p48));
loc_007B0153:
    result = WdipSemOpenRegistryKey(v_rip + 3500764, v_stack_p38, v_stack_p58, 4);
    if (!sign_flag) goto loc_007B0175;
loc_007B016D:
    goto loc_007AFF57;
loc_007B0175:
loc_007B0178:
    a1 = 0;
    result = WdipSemFastAllocate(a1, 48, v_stack_p58, 4);
    if (result == 0) goto loc_007B029B;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = WdipSemLoadNextEndEvent(v_stack_p58, 0, result, 4);
    v_r15 = (unsigned int)((0) + (1));
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007B020C;
    if (sign_flag) goto loc_007AFF57;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 52)))) >= 16) goto loc_007B01D8;
    *(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 52)) * 8 + 1048) = result;
    goto loc_007B0178;
loc_007B01D8:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7674865), v_rip - 7924934, result, 4);
    if ((unsigned __int8)(result) == 0) goto loc_007AFF52;
loc_007B01FA:
    result = WdipSemWriteScenarioLimitExceededEvent(v_rip - 7924954, a3, *(unsigned __int16 *)(a3 + 16), 4);
    goto loc_007AFF52;
loc_007B020C:
    if ((*(unsigned int *)(a3 + 52)) == 0) goto loc_007B016D;
    if ((unsigned __int8)(v_r14) != 0) goto loc_007AFF52;
    result = WdipSemOpenRegistryKey(v_rip + 3500768, v_stack_p38, v_stack_p50, 4);
    if (sign_flag) goto loc_007B016D;
loc_007B0240:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = WdipSemLoadNextContextProvider(v_stack_p50, 0, result, 4);
    v_r14 = (unsigned int)((0) + (1));
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007B016D;
    if (sign_flag) goto loc_007AFF57;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 48)))) >= 124) goto loc_007B02A5;
    *(unsigned __int64 *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 48)) * 8 + 56) = result;
    a1 = 0;
    result = WdipSemFastAllocate(a1, 48, result, 4);
    if (result != 0) goto loc_007B0240;
loc_007B029B:
    goto loc_007AFF57;
loc_007B02A5:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7674660), v_rip - 7924475, result, 4);
    if ((unsigned __int8)(result) == 0) goto loc_007AFF52;
    goto loc_007B01FA;
loc_007B02CC:
    result = _report_rangecheckfailure(v_rip - 7924495, v_rip - 7924475, result, 4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WdipSemLoadNextScenario(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint32_t v_stack_m214;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m48;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (544);
    result = (*(uint64_t *)(v_rip + 0x65A93A)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    v_stack_m220 = 0;
    v_stack_m208 = 0;
    v_stack_m200 = 0;
    v_stack_m228 = 0;
    v_stack_m218 = 0;
    v_stack_m214 = 0;
    v_stack_m210 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1F0 = v_xmm0;
    if (Arg1 != 0) goto loc_007AFE61;
loc_007AFE57:
    goto loc_007AFF93;
loc_007AFE61:
    if (Arg3 == 0) goto loc_007AFE57;
    Arg2 = 0;
    result = memset(v_stack_m1E0, Arg2, 152, a4);
    Arg3 = 0;
    v_stack_m230 = v_stack_m228;
    v_stack_m238 = 150;
    result = ZwEnumerateKey(Arg1, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), Arg3, v_stack_m1E0);
    if (sign_flag) goto loc_007AFF57;
    if (v_stack_m1D4 < 128) goto loc_007AFEBA;
    goto loc_007AFF57;
loc_007AFEBA:
    result = ((uint32_t)(v_stack_m1D4)) >> (1);
    Arg2 = 0;
    *(uint16_t *)(v_stack_m158 + result * 2 - 0x78) = 0;
    result = memset(v_stack_m148, Arg2, (uint32_t)(0x80000005ULL), v_stack_m1E0);
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, (uint32_t)(0x80000005ULL), v_stack_m1E0);
loc_007AFEEE:
    if (0 >= 64) goto loc_007AFF52;
    result = (0) + (0);
    if (((uint16_t)(*(uint16_t *)(v_stack_m158 + result * 1 - 0x78))) == 59) goto loc_007AFF0D;
    *(uint16_t *)(v_stack_m158 + result * 1 + 0x10) = (uint16_t)(*(uint16_t *)(v_stack_m158 + result * 1 - 0x78));
    Arg2 = (uint32_t)((0) + (1));
    goto loc_007AFEEE;
loc_007AFF0D:
    if (result >= ((uint32_t)(0x80000005ULL))) goto loc_007B02CC;
    Arg2 = (uint32_t)((Arg2) + (1));
    *(uint16_t *)(v_stack_m158 + result * 1 + 0x10) = 0;
    if (Arg2 >= 64) goto loc_007AFF52;
loc_007AFF2F:
    *(uint16_t *)(v_stack_m158 + 0x0 * 2 + 0x90) = (uint16_t)(*(uint16_t *)(v_stack_m1D0 + Arg2 * 2));
    if ((uint16_t)(*(uint16_t *)(v_stack_m1D0 + Arg2 * 2)) == 0) goto loc_007AFFC0;
    Arg2 = (uint32_t)((Arg2) + (1));
    a4 = (v_stack_m1D0 + Arg2 * 2) + (2);
    Arg3 = (uint32_t)((0) + (1));
    if (Arg2 < 64) goto loc_007AFF2F;
loc_007AFF52:
loc_007AFF57:
    result = 0;
    if (v_stack_m220 != 0) {
        result = ZwClose(v_stack_m220, Arg2, Arg3, a4);
    }
    if (v_stack_m208 != 0) {
        result = ZwClose(v_stack_m208, Arg2, Arg3, a4);
    }
    if (v_stack_m200 != 0) {
        result = ZwClose(v_stack_m200, Arg2, Arg3, a4);
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = WdipSemFastFree(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (544);
    return result;
loc_007AFFC0:
    local_r14 = 0;
    if (((uint32_t)(Arg3)) == 1) {
        local_r14 = 0;
        if (v_stack_mC8 == 42) { local_r14 = 1; }
    }
    result = RtlInitUnicodeString(v_stack_p68, v_stack_m148, Arg3, a4);
    result = RtlGUIDFromString(v_stack_p68, Arg3, Arg3, a4);
    if (sign_flag) goto loc_007AFF57;
    if ((uint8_t)(local_r14) != 0) goto loc_007B0033;
    result = RtlInitUnicodeString(v_stack_p68, v_stack_mC8, Arg3, a4);
    result = RtlUnicodeStringToInteger(v_stack_p68, 10, v_stack_p40, a4);
    if (sign_flag) goto loc_007AFF57;
    *(uint16_t *)(Arg3 + 0x10) = (uint16_t)(v_stack_p40);
loc_007B0033:
    result = WdipSemOpenRegistryKey(v_stack_m1D0, Arg1, v_stack_p38, a4);
    if (sign_flag) goto loc_007AFF57;
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p44;
    result = WdipSemQueryValueFromRegistry(v_stack_p38, v_rip + 3501276, 4, 4);
    if (!sign_flag) goto loc_007B0099;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_007AFF57;
    *(uint8_t *)(Arg3 + 0x12) = 255;
    goto loc_007B00AD;
loc_007B0099:
    Arg1 = (uint8_t)((uint32_t)(v_stack_p44));
    if ((uint32_t)((uint32_t)(v_stack_p44)) == 0) { Arg1 = 255; }
    *(uint8_t *)(Arg3 + 0x12) = (uint8_t)(Arg1);
loc_007B00AD:
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p60;
    result = WdipSemQueryValueFromRegistry(v_stack_p38, v_rip + 3501261, 8 + 3, 8);
    if (!sign_flag) goto loc_007B00F5;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_007AFF57;
    Arg1 = (v_stack_p38) | (-1);
    *(uint64_t *)(Arg3 + 0x18) = Arg1;
    goto loc_007B0109;
loc_007B00F5:
    Arg1 = (Arg1) | (-1);
    result = v_stack_p60;
    if (v_stack_p60 == 0) { result = Arg1; }
    *(uint64_t *)(Arg3 + 0x18) = result;
loc_007B0109:
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p48;
    result = WdipSemQueryValueFromRegistry(v_stack_p38, v_rip + 3500865, 4, 4);
    if (!sign_flag) goto loc_007B014C;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_007AFF57;
    *(uint32_t *)(Arg3 + 0x24) = 0;
    goto loc_007B0153;
loc_007B014C:
    *(uint32_t *)(Arg3 + 0x24) = (uint32_t)((uint32_t)(v_stack_p48));
loc_007B0153:
    result = WdipSemOpenRegistryKey(v_rip + 3500764, v_stack_p38, v_stack_p58, 4);
    if (!sign_flag) goto loc_007B0175;
loc_007B016D:
    goto loc_007AFF57;
loc_007B0175:
loc_007B0178:
    Arg1 = 0;
    result = WdipSemFastAllocate(Arg1, 48, v_stack_p58, 4);
    if (result == 0) goto loc_007B029B;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = WdipSemLoadNextEndEvent(v_stack_p58, 0, result, 4);
    local_r15 = (uint32_t)((0) + (1));
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007B020C;
    if (sign_flag) goto loc_007AFF57;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x34)))) >= 16) goto loc_007B01D8;
    *(uint64_t *)(Arg3 + (uint32_t)(*(uint32_t *)(Arg3 + 0x34)) * 8 + 0x418) = result;
    goto loc_007B0178;
loc_007B01D8:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x751BF1), v_rip - 7924934, result, 4);
    if ((uint8_t)(result) == 0) goto loc_007AFF52;
loc_007B01FA:
    result = WdipSemWriteScenarioLimitExceededEvent(v_rip - 7924954, Arg3, *(uint16_t *)(Arg3 + 0x10), 4);
    goto loc_007AFF52;
loc_007B020C:
    if ((*(uint32_t *)(Arg3 + 0x34)) == 0) goto loc_007B016D;
    if ((uint8_t)(local_r14) != 0) goto loc_007AFF52;
    result = WdipSemOpenRegistryKey(v_rip + 3500768, v_stack_p38, v_stack_p50, 4);
    if (sign_flag) goto loc_007B016D;
loc_007B0240:
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = WdipSemLoadNextContextProvider(v_stack_p50, 0, result, 4);
    local_r14 = (uint32_t)((0) + (1));
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007B016D;
    if (sign_flag) goto loc_007AFF57;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x30)))) >= 124) goto loc_007B02A5;
    *(uint64_t *)(Arg3 + (uint32_t)(*(uint32_t *)(Arg3 + 0x30)) * 8 + 0x38) = result;
    Arg1 = 0;
    result = WdipSemFastAllocate(Arg1, 48, result, 4);
    if (result != 0) goto loc_007B0240;
loc_007B029B:
    goto loc_007AFF57;
loc_007B02A5:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x751B24), v_rip - 7924475, result, 4);
    if ((uint8_t)(result) == 0) goto loc_007AFF52;
    goto loc_007B01FA;
loc_007B02CC:
    result = _report_rangecheckfailure(v_rip - 7924495, v_rip - 7924475, result, 4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007AFDE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
