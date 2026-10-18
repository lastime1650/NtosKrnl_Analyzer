# LocalGetStringForRelativeAttribute

- RVA: `0x00A02C38`–`0x00A03459` (길이 `2,081` bytes)
- VA: `0x0000000140A02C38`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7FA0`
- 디코드: `561`개 명령, `2,081/2,081` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A02C89` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A02C9A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A02CFA` → [ultow_s](../../text/50/ultow_s_function_00504F30.md) (function, `0x00504F30`)
- `0x00A02D1D` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x00A02D37` → [EncodeAttributeName](../7A/EncodeAttributeName_function_007A54D0.md) (function, `0x007A54D0`)
- `0x00A02EDE` → [LocalGetStringForSid](LocalGetStringForSid_function_00A00328.md) (function, `0x00A00328`)
- `0x00A02F1D` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A02F6A` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x00A02FCF` → [ui64tow_s](../../text/50/ui64tow_s_function_00504F10.md) (function, `0x00504F10`)
- `0x00A03037` → [i64tow_s](../../text/50/i64tow_s_function_00504EB0.md) (function, `0x00504EB0`)
- `0x00A0307B` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A030B6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A030F8` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A03166` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A03257` → [LocalGetStringForSid](LocalGetStringForSid_function_00A00328.md) (function, `0x00A00328`)
- `0x00A03288` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A0329A` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A032F3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A03348` → [ui64tow_s](../../text/50/ui64tow_s_function_00504F10.md) (function, `0x00504F10`)
- `0x00A0336F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A033B1` → [i64tow_s](../../text/50/i64tow_s_function_00504EB0.md) (function, `0x00504EB0`)
- `0x00A033D8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A0341D` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A0342A` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A03438` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [LocalGetAceCondition](LocalGetAceCondition_function_00A010BC.md) at `0x00A011F3`

### Static image references
- `0x00A02C54` → RVA `0x00E0A740` (`.data`; read)
- `0x00A031BE` → RVA `0x00037FA8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00A02C89` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A02C9A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A02CFA` → [ultow_s](../../text/50/ultow_s_function_00504F30.md) (`PAGE` → `.text`)
  - `0x00A02D1D` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x00A02F6A` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x00A02FCF` → [ui64tow_s](../../text/50/ui64tow_s_function_00504F10.md) (`PAGE` → `.text`)
  - `0x00A03037` → [i64tow_s](../../text/50/i64tow_s_function_00504EB0.md) (`PAGE` → `.text`)
  - `0x00A030B6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A03166` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A03288` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A032F3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A03348` → [ui64tow_s](../../text/50/ui64tow_s_function_00504F10.md) (`PAGE` → `.text`)
  - `0x00A0336F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A033B1` → [i64tow_s](../../text/50/i64tow_s_function_00504EB0.md) (`PAGE` → `.text`)
  - `0x00A033D8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A03438` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A02C38  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A02C3D  55                              push rbp
00A02C3E  56                              push rsi
00A02C3F  57                              push rdi
00A02C40  41 54                           push r12
00A02C42  41 55                           push r13
00A02C44  41 56                           push r14
00A02C46  41 57                           push r15
00A02C48  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00A02C4D  48 81 EC 70 01 00 00            sub rsp, 0x170
00A02C54  48 8B 05 E5 7A 40 00            mov rax, qword ptr [rip + 0x407ae5]
00A02C5B  48 33 C4                        xor rax, rsp
00A02C5E  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00A02C62  48 8B BD E0 00 00 00            mov rdi, qword ptr [rbp + 0xe0]
00A02C69  33 F6                           xor esi, esi
00A02C6B  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00A02C70  8B DA                           mov ebx, edx
00A02C72  4C 8B F1                        mov r14, rcx
00A02C75  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00A02C7A  33 D2                           xor edx, edx
00A02C7C  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A02C81  44 8D 46 46                     lea r8d, [rsi + 0x46]
00A02C85  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00A02C89  E8 B2 3F CC FF                  call 0x1406c6c40
00A02C8E  33 D2                           xor edx, edx
00A02C90  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00A02C94  41 B8 8C 00 00 00               mov r8d, 0x8c
00A02C9A  E8 A1 3F CC FF                  call 0x1406c6c40
00A02C9F  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A02CA4  44 8B EE                        mov r13d, esi
00A02CA7  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
00A02CAC  4D 85 F6                        test r14, r14
00A02CAF  0F 84 56 07 00 00               je 0x140a0340b
00A02CB5  85 DB                           test ebx, ebx
00A02CB7  0F 84 4E 07 00 00               je 0x140a0340b
00A02CBD  48 85 FF                        test rdi, rdi
00A02CC0  0F 84 45 07 00 00               je 0x140a0340b
00A02CC6  83 FB 14                        cmp ebx, 0x14
00A02CC9  73 0A                           jae 0x140a02cd5
00A02CCB  BE 38 05 00 00                  mov esi, 0x538
00A02CD0  E9 5A 07 00 00                  jmp 0x140a0342f
00A02CD5  45 8B 66 0C                     mov r12d, dword ptr [r14 + 0xc]
00A02CD9  45 0F B7 7E 04                  movzx r15d, word ptr [r14 + 4]
00A02CDE  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00A02CE3  45 85 E4                        test r12d, r12d
00A02CE6  74 E3                           je 0x140a02ccb
00A02CE8  41 8B 4E 08                     mov ecx, dword ptr [r14 + 8]
00A02CEC  48 8D 55 10                     lea rdx, [rbp + 0x10]
00A02CF0  41 B9 10 00 00 00               mov r9d, 0x10
00A02CF6  45 8D 41 13                     lea r8d, [r9 + 0x13]
00A02CFA  E8 31 22 B0 FF                  call 0x140504f30
00A02CFF  41 8B 0E                        mov ecx, dword ptr [r14]
00A02D02  3B D9                           cmp ebx, ecx
00A02D04  72 C5                           jb 0x140a02ccb
00A02D06  8B C3                           mov eax, ebx
00A02D08  2B C1                           sub eax, ecx
00A02D0A  83 F8 04                        cmp eax, 4
00A02D0D  72 BC                           jb 0x140a02ccb
00A02D0F  4D 8D 1C 0E                     lea r11, [r14 + rcx]
00A02D13  8B D0                           mov edx, eax
00A02D15  49 8B CB                        mov rcx, r11
00A02D18  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00A02D1D  E8 CA 48 A5 FF                  call 0x1404575ec
00A02D22  85 C0                           test eax, eax
00A02D24  78 A5                           js 0x140a02ccb
00A02D26  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00A02D2B  85 D2                           test edx, edx
00A02D2D  74 9C                           je 0x140a02ccb
00A02D2F  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00A02D34  49 8B CB                        mov rcx, r11
00A02D37  E8 94 27 DA FF                  call 0x1407a54d0
00A02D3C  45 33 DB                        xor r11d, r11d
00A02D3F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00A02D43  8B F0                           mov esi, eax
00A02D45  85 C0                           test eax, eax
00A02D47  0F 85 C3 06 00 00               jne 0x140a03410
00A02D4D  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A02D52  48 83 CF FF                     or rdi, 0xffffffffffffffff
00A02D56  48 8B CF                        mov rcx, rdi
00A02D59  48 FF C1                        inc rcx
00A02D5C  66 44 39 1C 48                  cmp word ptr [rax + rcx*2], r11w
00A02D61  75 F6                           jne 0x140a02d59
00A02D63  03 C9                           add ecx, ecx
00A02D65  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00A02D6A  4B 8D 04 24                     lea rax, [r12 + r12]
00A02D6E  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00A02D73  41 BA FF FF FF FF               mov r10d, 0xffffffff
00A02D79  4D 8B C4                        mov r8, r12
00A02D7C  49 3B C2                        cmp rax, r10
00A02D7F  0F 87 7F 06 00 00               ja 0x140a03404
00A02D85  83 C0 18                        add eax, 0x18
00A02D88  83 F8 18                        cmp eax, 0x18
00A02D8B  0F 82 73 06 00 00               jb 0x140a03404
00A02D91  03 C8                           add ecx, eax
00A02D93  3B C8                           cmp ecx, eax
00A02D95  0F 82 69 06 00 00               jb 0x140a03404
00A02D9B  4C 8D 4D 10                     lea r9, [rbp + 0x10]
00A02D9F  48 8B C7                        mov rax, rdi
00A02DA2  48 FF C0                        inc rax
00A02DA5  66 45 39 1C 41                  cmp word ptr [r9 + rax*2], r11w
00A02DAA  75 F6                           jne 0x140a02da2
00A02DAC  8D 3C 41                        lea edi, [rcx + rax*2]
00A02DAF  3B F9                           cmp edi, ecx
00A02DB1  0F 82 4D 06 00 00               jb 0x140a03404
00A02DB7  4A 8D 0C A5 00 00 00 00         lea rcx, [r12*4]
00A02DBF  49 3B CA                        cmp rcx, r10
00A02DC2  0F 87 3C 06 00 00               ja 0x140a03404
00A02DC8  8D 43 F0                        lea eax, [rbx - 0x10]
00A02DCB  3B C1                           cmp eax, ecx
00A02DCD  72 34                           jb 0x140a02e03
00A02DCF  41 8B CF                        mov ecx, r15d
00A02DD2  45 8B E7                        mov r12d, r15d
00A02DD5  83 E9 01                        sub ecx, 1
00A02DD8  0F 84 22 02 00 00               je 0x140a03000
00A02DDE  83 E9 01                        sub ecx, 1
00A02DE1  0F 84 AD 01 00 00               je 0x140a02f94
00A02DE7  83 E9 01                        sub ecx, 1
00A02DEA  0F 84 4A 01 00 00               je 0x140a02f3a
00A02DF0  83 E9 02                        sub ecx, 2
00A02DF3  74 6C                           je 0x140a02e61
00A02DF5  83 E9 01                        sub ecx, 1
00A02DF8  0F 84 96 01 00 00               je 0x140a02f94
00A02DFE  83 F9 0A                        cmp ecx, 0xa
00A02E01  74 0A                           je 0x140a02e0d
00A02E03  BE 38 05 00 00                  mov esi, 0x538
00A02E08  E9 03 06 00 00                  jmp 0x140a03410
00A02E0D  41 8B D3                        mov edx, r11d
00A02E10  41 3B D0                        cmp edx, r8d
00A02E13  0F 83 4F 02 00 00               jae 0x140a03068
00A02E19  8B C2                           mov eax, edx
00A02E1B  45 8B 44 86 10                  mov r8d, dword ptr [r14 + rax*4 + 0x10]
00A02E20  41 3B D8                        cmp ebx, r8d
00A02E23  72 DE                           jb 0x140a02e03
00A02E25  8B CB                           mov ecx, ebx
00A02E27  41 2B C8                        sub ecx, r8d
00A02E2A  83 F9 04                        cmp ecx, 4
00A02E2D  72 D4                           jb 0x140a02e03
00A02E2F  47 8B 04 30                     mov r8d, dword ptr [r8 + r14]
00A02E33  8D 41 FC                        lea eax, [rcx - 4]
00A02E36  41 3B C0                        cmp eax, r8d
00A02E39  72 C8                           jb 0x140a02e03
00A02E3B  41 8B C0                        mov eax, r8d
00A02E3E  48 C1 E0 02                     shl rax, 2
00A02E42  49 3B C2                        cmp rax, r10
00A02E45  0F 87 B9 05 00 00               ja 0x140a03404
00A02E4B  8D 0C 38                        lea ecx, [rax + rdi]
00A02E4E  3B CF                           cmp ecx, edi
00A02E50  0F 82 AE 05 00 00               jb 0x140a03404
00A02E56  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00A02E5B  8B F9                           mov edi, ecx
00A02E5D  FF C2                           inc edx
00A02E5F  EB AF                           jmp 0x140a02e10
00A02E61  45 8B FB                        mov r15d, r11d
00A02E64  45 3B F8                        cmp r15d, r8d
00A02E67  0F 83 FB 01 00 00               jae 0x140a03068
00A02E6D  41 8B C7                        mov eax, r15d
00A02E70  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
00A02E75  3B D9                           cmp ebx, ecx
00A02E77  72 8A                           jb 0x140a02e03
00A02E79  8B C3                           mov eax, ebx
00A02E7B  2B C1                           sub eax, ecx
00A02E7D  83 F8 04                        cmp eax, 4
00A02E80  72 81                           jb 0x140a02e03
00A02E82  42 8B 14 31                     mov edx, dword ptr [rcx + r14]
00A02E86  83 C1 04                        add ecx, 4
00A02E89  85 D2                           test edx, edx
00A02E8B  0F 84 72 FF FF FF               je 0x140a02e03
00A02E91  8B C3                           mov eax, ebx
00A02E93  2B C1                           sub eax, ecx
00A02E95  3B C2                           cmp eax, edx
00A02E97  0F 82 66 FF FF FF               jb 0x140a02e03
00A02E9D  83 F8 08                        cmp eax, 8
00A02EA0  0F 82 5D FF FF FF               jb 0x140a02e03
00A02EA6  49 03 CE                        add rcx, r14
00A02EA9  0F B6 51 01                     movzx edx, byte ptr [rcx + 1]
00A02EAD  84 D2                           test dl, dl
00A02EAF  0F 84 4E FF FF FF               je 0x140a02e03
00A02EB5  44 8B C2                        mov r8d, edx
00A02EB8  83 C0 F8                        add eax, -8
00A02EBB  49 C1 E0 02                     shl r8, 2
00A02EBF  8B D0                           mov edx, eax
00A02EC1  49 3B D0                        cmp rdx, r8
00A02EC4  0F 82 39 FF FF FF               jb 0x140a02e03
00A02ECA  8A 85 D8 00 00 00               mov al, byte ptr [rbp + 0xd8]
00A02ED0  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00A02ED5  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00A02EDA  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A02EDE  E8 45 D4 FF FF                  call 0x140a00328
00A02EE3  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00A02EE8  45 33 DB                        xor r11d, r11d
00A02EEB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00A02EEF  8B F0                           mov esi, eax
00A02EF1  85 C0                           test eax, eax
00A02EF3  0F 85 17 05 00 00               jne 0x140a03410
00A02EF9  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A02EFD  48 FF C0                        inc rax
00A02F00  66 45 39 5C 45 00               cmp word ptr [r13 + rax*2], r11w
00A02F06  75 F5                           jne 0x140a02efd
00A02F08  8D 14 47                        lea edx, [rdi + rax*2]
00A02F0B  3B D7                           cmp edx, edi
00A02F0D  0F 82 F1 04 00 00               jb 0x140a03404
00A02F13  8B FA                           mov edi, edx
00A02F15  4D 85 ED                        test r13, r13
00A02F18  74 13                           je 0x140a02f2d
00A02F1A  49 8B CD                        mov rcx, r13
00A02F1D  E8 E2 F4 EC FF                  call 0x1408d2404
00A02F22  45 33 DB                        xor r11d, r11d
00A02F25  45 8B EB                        mov r13d, r11d
00A02F28  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
00A02F2D  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00A02F32  41 FF C7                        inc r15d
00A02F35  E9 2A FF FF FF                  jmp 0x140a02e64
00A02F3A  45 3B D8                        cmp r11d, r8d
00A02F3D  0F 83 25 01 00 00               jae 0x140a03068
00A02F43  41 8B C3                        mov eax, r11d
00A02F46  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
00A02F4B  3B D9                           cmp ebx, ecx
00A02F4D  0F 82 B0 FE FF FF               jb 0x140a02e03
00A02F53  8B C3                           mov eax, ebx
00A02F55  2B C1                           sub eax, ecx
00A02F57  83 F8 02                        cmp eax, 2
00A02F5A  0F 82 A3 FE FF FF               jb 0x140a02e03
00A02F60  8B D0                           mov edx, eax
00A02F62  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00A02F67  49 03 CE                        add rcx, r14
00A02F6A  E8 7D 46 A5 FF                  call 0x1404575ec
00A02F6F  85 C0                           test eax, eax
00A02F71  0F 88 8C FE FF FF               js 0x140a02e03
00A02F77  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00A02F7B  83 C1 04                        add ecx, 4
00A02F7E  03 CF                           add ecx, edi
00A02F80  3B CF                           cmp ecx, edi
00A02F82  0F 82 7C 04 00 00               jb 0x140a03404
00A02F88  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00A02F8D  8B F9                           mov edi, ecx
00A02F8F  41 FF C3                        inc r11d
00A02F92  EB A6                           jmp 0x140a02f3a
00A02F94  45 8B FB                        mov r15d, r11d
00A02F97  45 3B F8                        cmp r15d, r8d
00A02F9A  0F 83 C8 00 00 00               jae 0x140a03068
00A02FA0  41 8B C7                        mov eax, r15d
00A02FA3  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
00A02FA8  3B D9                           cmp ebx, ecx
00A02FAA  0F 82 53 FE FF FF               jb 0x140a02e03
00A02FB0  8B C3                           mov eax, ebx
00A02FB2  2B C1                           sub eax, ecx
00A02FB4  83 F8 08                        cmp eax, 8
00A02FB7  0F 82 46 FE FF FF               jb 0x140a02e03
00A02FBD  4A 8B 0C 31                     mov rcx, qword ptr [rcx + r14]
00A02FC1  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A02FC5  41 B9 0A 00 00 00               mov r9d, 0xa
00A02FCB  45 8D 41 3C                     lea r8d, [r9 + 0x3c]
00A02FCF  E8 3C 1F B0 FF                  call 0x140504f10
00A02FD4  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A02FD8  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00A02FDC  45 33 DB                        xor r11d, r11d
00A02FDF  48 FF C0                        inc rax
00A02FE2  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A02FE7  75 F6                           jne 0x140a02fdf
00A02FE9  8D 0C 47                        lea ecx, [rdi + rax*2]
00A02FEC  3B CF                           cmp ecx, edi
00A02FEE  0F 82 10 04 00 00               jb 0x140a03404
00A02FF4  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00A02FF9  8B F9                           mov edi, ecx
00A02FFB  41 FF C7                        inc r15d
00A02FFE  EB 97                           jmp 0x140a02f97
00A03000  45 8B FB                        mov r15d, r11d
00A03003  45 3B F8                        cmp r15d, r8d
00A03006  73 60                           jae 0x140a03068
00A03008  41 8B C7                        mov eax, r15d
00A0300B  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
00A03010  3B D9                           cmp ebx, ecx
00A03012  0F 82 EB FD FF FF               jb 0x140a02e03
00A03018  8B C3                           mov eax, ebx
00A0301A  2B C1                           sub eax, ecx
00A0301C  83 F8 08                        cmp eax, 8
00A0301F  0F 82 DE FD FF FF               jb 0x140a02e03
00A03025  4A 8B 0C 31                     mov rcx, qword ptr [rcx + r14]
00A03029  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A0302D  41 B9 0A 00 00 00               mov r9d, 0xa
00A03033  45 8D 41 3C                     lea r8d, [r9 + 0x3c]
00A03037  E8 74 1E B0 FF                  call 0x140504eb0
00A0303C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A03040  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00A03044  45 33 DB                        xor r11d, r11d
00A03047  48 FF C0                        inc rax
00A0304A  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A0304F  75 F6                           jne 0x140a03047
00A03051  8D 0C 47                        lea ecx, [rdi + rax*2]
00A03054  3B CF                           cmp ecx, edi
00A03056  0F 82 A8 03 00 00               jb 0x140a03404
00A0305C  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00A03061  8B F9                           mov edi, ecx
00A03063  41 FF C7                        inc r15d
00A03066  EB 9B                           jmp 0x140a03003
00A03068  8D 4F 03                        lea ecx, [rdi + 3]
00A0306B  3B CF                           cmp ecx, edi
00A0306D  0F 82 91 03 00 00               jb 0x140a03404
00A03073  B8 FC FF FF FF                  mov eax, 0xfffffffc
00A03078  48 23 C8                        and rcx, rax
00A0307B  E8 08 2F F2 FF                  call 0x140925f88
00A03080  45 33 FF                        xor r15d, r15d
00A03083  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A03088  48 85 C0                        test rax, rax
00A0308B  75 08                           jne 0x140a03095
00A0308D  8D 70 08                        lea esi, [rax + 8]
00A03090  E9 7B 03 00 00                  jmp 0x140a03410
00A03095  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00A03099  48 8D 78 02                     lea rdi, [rax + 2]
00A0309D  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00A030A2  44 8B C3                        mov r8d, ebx
00A030A5  66 C7 07 22 00                  mov word ptr [rdi], 0x22
00A030AA  48 83 C7 02                     add rdi, 2
00A030AE  48 8B CF                        mov rcx, rdi
00A030B1  66 C7 00 28 00                  mov word ptr [rax], 0x28
00A030B6  E8 85 37 CC FF                  call 0x1406c6840
00A030BB  48 D1 EB                        shr rbx, 1
00A030BE  41 8B CC                        mov ecx, r12d
00A030C1  BA 2C 00 00 00                  mov edx, 0x2c
00A030C6  48 8D 3C 5F                     lea rdi, [rdi + rbx*2]
00A030CA  C7 07 22 00 2C 00               mov dword ptr [rdi], 0x2c0022
00A030D0  83 E9 01                        sub ecx, 1
00A030D3  74 5A                           je 0x140a0312f
00A030D5  83 E9 01                        sub ecx, 1
00A030D8  74 4C                           je 0x140a03126
00A030DA  83 E9 01                        sub ecx, 1
00A030DD  74 3E                           je 0x140a0311d
00A030DF  83 E9 02                        sub ecx, 2
00A030E2  74 30                           je 0x140a03114
00A030E4  83 E9 01                        sub ecx, 1
00A030E7  74 22                           je 0x140a0310b
00A030E9  83 F9 0A                        cmp ecx, 0xa
00A030EC  74 14                           je 0x140a03102
00A030EE  BE 38 05 00 00                  mov esi, 0x538
00A030F3  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00A030F8  E8 07 F3 EC FF                  call 0x1408d2404
00A030FD  E9 0E 03 00 00                  jmp 0x140a03410
00A03102  C7 47 04 54 00 58 00            mov dword ptr [rdi + 4], 0x580054
00A03109  EB 2B                           jmp 0x140a03136
00A0310B  C7 47 04 54 00 42 00            mov dword ptr [rdi + 4], 0x420054
00A03112  EB 22                           jmp 0x140a03136
00A03114  C7 47 04 54 00 44 00            mov dword ptr [rdi + 4], 0x440054
00A0311B  EB 19                           jmp 0x140a03136
00A0311D  C7 47 04 54 00 53 00            mov dword ptr [rdi + 4], 0x530054
00A03124  EB 10                           jmp 0x140a03136
00A03126  C7 47 04 54 00 55 00            mov dword ptr [rdi + 4], 0x550054
00A0312D  EB 07                           jmp 0x140a03136
00A0312F  C7 47 04 54 00 49 00            mov dword ptr [rdi + 4], 0x490054
00A03136  66 89 57 08                     mov word ptr [rdi + 8], dx
00A0313A  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00A0313E  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A03142  48 FF C0                        inc rax
00A03145  66 44 39 3C 41                  cmp word ptr [rcx + rax*2], r15w
00A0314A  75 F6                           jne 0x140a03142
00A0314C  8B D8                           mov ebx, eax
00A0314E  48 8D 55 10                     lea rdx, [rbp + 0x10]
00A03152  C7 47 0A 30 00 78 00            mov dword ptr [rdi + 0xa], 0x780030
00A03159  48 03 DB                        add rbx, rbx
00A0315C  48 83 C7 0E                     add rdi, 0xe
00A03160  4C 8B C3                        mov r8, rbx
00A03163  48 8B CF                        mov rcx, rdi
00A03166  E8 D5 36 CC FF                  call 0x1406c6840
00A0316B  48 03 FB                        add rdi, rbx
00A0316E  41 83 EC 01                     sub r12d, 1
00A03172  0F 84 0B 02 00 00               je 0x140a03383
00A03178  41 83 EC 01                     sub r12d, 1
00A0317C  0F 84 94 01 00 00               je 0x140a03316
00A03182  41 83 EC 01                     sub r12d, 1
00A03186  0F 84 23 01 00 00               je 0x140a032af
00A0318C  41 83 EC 02                     sub r12d, 2
00A03190  0F 84 86 00 00 00               je 0x140a0321c
00A03196  41 83 EC 01                     sub r12d, 1
00A0319A  0F 84 76 01 00 00               je 0x140a03316
00A031A0  41 83 FC 0A                     cmp r12d, 0xa
00A031A4  0F 85 44 FF FF FF               jne 0x140a030ee
00A031AA  44 39 7C 24 30                  cmp dword ptr [rsp + 0x30], r15d
00A031AF  0F 84 3A 02 00 00               je 0x140a033ef
00A031B5  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00A031BA  4D 8D 46 10                     lea r8, [r14 + 0x10]
00A031BE  4C 8D 1D E3 4D 63 FF            lea r11, [rip - 0x9cb21d]
00A031C5  66 C7 07 2C 00                  mov word ptr [rdi], 0x2c
00A031CA  48 83 C7 02                     add rdi, 2
00A031CE  41 8B 08                        mov ecx, dword ptr [r8]
00A031D1  46 8B 0C 31                     mov r9d, dword ptr [rcx + r14]
00A031D5  8D 51 04                        lea edx, [rcx + 4]
00A031D8  49 03 D6                        add rdx, r14
00A031DB  45 85 C9                        test r9d, r9d
00A031DE  74 2D                           je 0x140a0320d
00A031E0  45 8B D1                        mov r10d, r9d
00A031E3  0F B6 0A                        movzx ecx, byte ptr [rdx]
00A031E6  48 FF C2                        inc rdx
00A031E9  8B C1                           mov eax, ecx
00A031EB  83 E1 0F                        and ecx, 0xf
00A031EE  48 C1 E8 04                     shr rax, 4
00A031F2  41 0F B7 04 43                  movzx eax, word ptr [r11 + rax*2]
00A031F7  66 89 07                        mov word ptr [rdi], ax
00A031FA  41 0F B7 04 4B                  movzx eax, word ptr [r11 + rcx*2]
00A031FF  66 89 47 02                     mov word ptr [rdi + 2], ax
00A03203  48 83 C7 04                     add rdi, 4
00A03207  49 83 EA 01                     sub r10, 1
00A0320B  75 D6                           jne 0x140a031e3
00A0320D  49 83 C0 04                     add r8, 4
00A03211  49 83 EC 01                     sub r12, 1
00A03215  75 AE                           jne 0x140a031c5
00A03217  E9 D3 01 00 00                  jmp 0x140a033ef
00A0321C  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
00A03221  33 DB                           xor ebx, ebx
00A03223  45 3B FC                        cmp r15d, r12d
00A03226  0F 83 C3 01 00 00               jae 0x140a033ef
00A0322C  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00A03231  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00A03236  41 8B C7                        mov eax, r15d
00A03239  66 C7 07 2C 00                  mov word ptr [rdi], 0x2c
00A0323E  48 83 C7 02                     add rdi, 2
00A03242  41 8B 4C 86 10                  mov ecx, dword ptr [r14 + rax*4 + 0x10]
00A03247  8A 85 D8 00 00 00               mov al, byte ptr [rbp + 0xd8]
00A0324D  83 C1 04                        add ecx, 4
00A03250  49 03 CE                        add rcx, r14
00A03253  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A03257  E8 CC D0 FF FF                  call 0x140a00328
00A0325C  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00A03261  8B F0                           mov esi, eax
00A03263  85 C0                           test eax, eax
00A03265  0F 85 88 FE FF FF               jne 0x140a030f3
00A0326B  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A0326F  48 FF C0                        inc rax
00A03272  66 41 39 5C 45 00               cmp word ptr [r13 + rax*2], bx
00A03278  75 F5                           jne 0x140a0326f
00A0327A  8B D8                           mov ebx, eax
00A0327C  49 8B D5                        mov rdx, r13
00A0327F  48 03 DB                        add rbx, rbx
00A03282  48 8B CF                        mov rcx, rdi
00A03285  4C 8B C3                        mov r8, rbx
00A03288  E8 B3 35 CC FF                  call 0x1406c6840
00A0328D  48 03 FB                        add rdi, rbx
00A03290  33 DB                           xor ebx, ebx
00A03292  4D 85 ED                        test r13, r13
00A03295  74 10                           je 0x140a032a7
00A03297  49 8B CD                        mov rcx, r13
00A0329A  E8 65 F1 EC FF                  call 0x1408d2404
00A0329F  44 8B EB                        mov r13d, ebx
00A032A2  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00A032A7  41 FF C7                        inc r15d
00A032AA  E9 74 FF FF FF                  jmp 0x140a03223
00A032AF  44 39 7C 24 30                  cmp dword ptr [rsp + 0x30], r15d
00A032B4  0F 84 35 01 00 00               je 0x140a033ef
00A032BA  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00A032BF  4D 8D 7E 10                     lea r15, [r14 + 0x10]
00A032C3  41 BD 22 00 00 00               mov r13d, 0x22
00A032C9  C7 07 2C 00 22 00               mov dword ptr [rdi], 0x22002c
00A032CF  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A032D3  41 8B 17                        mov edx, dword ptr [r15]
00A032D6  48 83 C7 04                     add rdi, 4
00A032DA  49 03 D6                        add rdx, r14
00A032DD  33 C9                           xor ecx, ecx
00A032DF  48 FF C0                        inc rax
00A032E2  66 39 0C 42                     cmp word ptr [rdx + rax*2], cx
00A032E6  75 F7                           jne 0x140a032df
00A032E8  8B D8                           mov ebx, eax
00A032EA  48 8B CF                        mov rcx, rdi
00A032ED  48 03 DB                        add rbx, rbx
00A032F0  4C 8B C3                        mov r8, rbx
00A032F3  E8 48 35 CC FF                  call 0x1406c6840
00A032F8  48 03 FB                        add rdi, rbx
00A032FB  49 83 C7 04                     add r15, 4
00A032FF  66 44 89 2F                     mov word ptr [rdi], r13w
00A03303  48 83 C7 02                     add rdi, 2
00A03307  49 83 EC 01                     sub r12, 1
00A0330B  75 BC                           jne 0x140a032c9
00A0330D  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
00A03311  E9 D4 00 00 00                  jmp 0x140a033ea
00A03316  44 39 7C 24 30                  cmp dword ptr [rsp + 0x30], r15d
00A0331B  0F 84 CE 00 00 00               je 0x140a033ef
00A03321  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00A03326  4D 8D 7E 10                     lea r15, [r14 + 0x10]
00A0332A  66 C7 07 2C 00                  mov word ptr [rdi], 0x2c
00A0332F  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A03333  41 8B 0F                        mov ecx, dword ptr [r15]
00A03336  41 B9 0A 00 00 00               mov r9d, 0xa
00A0333C  48 83 C7 02                     add rdi, 2
00A03340  4A 8B 0C 31                     mov rcx, qword ptr [rcx + r14]
00A03344  45 8D 41 3C                     lea r8d, [r9 + 0x3c]
00A03348  E8 C3 1B B0 FF                  call 0x140504f10
00A0334D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A03351  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A03355  33 C9                           xor ecx, ecx
00A03357  48 FF C0                        inc rax
00A0335A  66 39 0C 42                     cmp word ptr [rdx + rax*2], cx
00A0335E  75 F7                           jne 0x140a03357
00A03360  8B D8                           mov ebx, eax
00A03362  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A03366  48 03 DB                        add rbx, rbx
00A03369  48 8B CF                        mov rcx, rdi
00A0336C  4C 8B C3                        mov r8, rbx
00A0336F  E8 CC 34 CC FF                  call 0x1406c6840
00A03374  48 03 FB                        add rdi, rbx
00A03377  49 83 C7 04                     add r15, 4
00A0337B  49 83 EC 01                     sub r12, 1
00A0337F  75 A9                           jne 0x140a0332a
00A03381  EB 67                           jmp 0x140a033ea
00A03383  44 39 7C 24 30                  cmp dword ptr [rsp + 0x30], r15d
00A03388  74 65                           je 0x140a033ef
00A0338A  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00A0338F  4D 8D 7E 10                     lea r15, [r14 + 0x10]
00A03393  66 C7 07 2C 00                  mov word ptr [rdi], 0x2c
00A03398  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A0339C  41 8B 0F                        mov ecx, dword ptr [r15]
00A0339F  41 B9 0A 00 00 00               mov r9d, 0xa
00A033A5  48 83 C7 02                     add rdi, 2
00A033A9  4A 8B 0C 31                     mov rcx, qword ptr [rcx + r14]
00A033AD  45 8D 41 3C                     lea r8d, [r9 + 0x3c]
00A033B1  E8 FA 1A B0 FF                  call 0x140504eb0
00A033B6  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A033BA  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A033BE  33 C9                           xor ecx, ecx
00A033C0  48 FF C0                        inc rax
00A033C3  66 39 0C 42                     cmp word ptr [rdx + rax*2], cx
00A033C7  75 F7                           jne 0x140a033c0
00A033C9  8B D8                           mov ebx, eax
00A033CB  48 8D 55 80                     lea rdx, [rbp - 0x80]
00A033CF  48 03 DB                        add rbx, rbx
00A033D2  48 8B CF                        mov rcx, rdi
00A033D5  4C 8B C3                        mov r8, rbx
00A033D8  E8 63 34 CC FF                  call 0x1406c6840
00A033DD  48 03 FB                        add rdi, rbx
00A033E0  49 83 C7 04                     add r15, 4
00A033E4  49 83 EC 01                     sub r12, 1
00A033E8  75 A9                           jne 0x140a03393
00A033EA  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00A033EF  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00A033F4  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00A033F9  C7 07 29 00 00 00               mov dword ptr [rdi], 0x29
00A033FF  48 89 01                        mov qword ptr [rcx], rax
00A03402  EB 0C                           jmp 0x140a03410
00A03404  BE 16 02 00 00                  mov esi, 0x216
00A03409  EB 05                           jmp 0x140a03410
00A0340B  BE 57 00 00 00                  mov esi, 0x57
00A03410  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A03415  48 85 C0                        test rax, rax
00A03418  74 08                           je 0x140a03422
00A0341A  48 8B C8                        mov rcx, rax
00A0341D  E8 E2 EF EC FF                  call 0x1408d2404
00A03422  4D 85 ED                        test r13, r13
00A03425  74 08                           je 0x140a0342f
00A03427  49 8B CD                        mov rcx, r13
00A0342A  E8 D5 EF EC FF                  call 0x1408d2404
00A0342F  8B C6                           mov eax, esi
00A03431  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00A03435  48 33 CC                        xor rcx, rsp
00A03438  E8 03 92 CA FF                  call 0x1406ac640
00A0343D  48 8B 9C 24 C8 01 00 00         mov rbx, qword ptr [rsp + 0x1c8]
00A03445  48 81 C4 70 01 00 00            add rsp, 0x170
00A0344C  41 5F                           pop r15
00A0344E  41 5E                           pop r14
00A03450  41 5D                           pop r13
00A03452  41 5C                           pop r12
00A03454  5F                              pop rdi
00A03455  5E                              pop rsi
00A03456  5D                              pop rbp
00A03457  C3                              ret
00A03458  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalGetStringForRelativeAttribute(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int8 v_stack_m180;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 4225765)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m148 = a3;
    v_stack_m138 = a7;
    a2 = 0;
    v_stack_m150 = 0;
    result = memset(v_stack_m98, a2, v_rsi + 70, a4);
    a2 = 0;
    result = memset(v_stack_m128, a2, 140, a4);
    v_stack_m170 = 0;
    v_stack_m168 = 0;
    if (a1 == 0) goto loc_00A0340B;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_00A0340B;
    if (a7 == 0) goto loc_00A0340B;
    if (((unsigned int)((unsigned int)(a2))) >= 20) goto loc_00A02CD5;
loc_00A02CCB:
    goto loc_00A0342F;
loc_00A02CD5:
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))) == 0) goto loc_00A02CCB;
    result = ultow_s((unsigned int)(*(unsigned int *)(a1 + 8)), v_stack_m98, 16 + 19, 16);
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) goto loc_00A02CCB;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    if (((unsigned int)(result)) < 4) goto loc_00A02CCB;
    result = RtlStringCbLengthW(a1 + (unsigned int)(*(unsigned int *)(a1)) * 1, (unsigned int)((unsigned int)(result)), v_stack_m168, 16);
    if (sign_flag) goto loc_00A02CCB;
    if ((unsigned int)(v_stack_m168) == 0) goto loc_00A02CCB;
    result = EncodeAttributeName(a1 + (unsigned int)(*(unsigned int *)(a1)) * 1, v_stack_m168, v_stack_m150, 16);
    v_r11 = 0;
    v_stack_m160 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00A03410;
    v_rdi = (a7) | (-1);
loc_00A02D59:
    a1 = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m150 + a1 * 2)) != 0) goto loc_00A02D59;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    v_stack_m158 = (unsigned int)(*(unsigned int *)(a1 + 12));
    v_stack_m140 = a1;
    if (((unsigned int)(*(unsigned int *)(a1 + 12)) + (unsigned int)(*(unsigned int *)(a1 + 12)) * 1) > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A03404;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12)) + (unsigned int)(*(unsigned int *)(a1 + 12)) * 1) + (24));
    if (((unsigned int)(result)) < 24) goto loc_00A03404;
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_00A03404;
loc_00A02DA2:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m98 + result * 2)) != 0) goto loc_00A02DA2;
    if (((unsigned int)(a1 + result * 2)) < ((unsigned int)(a1))) goto loc_00A03404;
    if (((unsigned int)(*(unsigned int *)(a1 + 12)) * 4) > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A03404;
    if (((unsigned int)((unsigned int)(a2) - 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)) * 4))) goto loc_00A02E03;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 4)))) - (1));
    if (condition_is_equal) goto loc_00A03000;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A02F94;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A02F3A;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A02E61;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A02F94;
    if (((unsigned int)(a1)) == 10) goto loc_00A02E0D;
loc_00A02E03:
    goto loc_00A03410;
loc_00A02E0D:
loc_00A02E10:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))))) goto loc_00A03068;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_00A02E03;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(a1)) < 4) goto loc_00A02E03;
    if (((unsigned int)(a1 - 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))))) goto loc_00A02E03;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))))) << (2);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A03404;
    if (((unsigned int)(result + a1 + result * 2 * 1)) < ((unsigned int)(a1 + result * 2))) goto loc_00A03404;
    a2 = (unsigned int)((0) + 1);
    goto loc_00A02E10;
loc_00A02E61:
loc_00A02E64:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00A03068;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_00A02E03;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(result)) < 4) goto loc_00A02E03;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))) + (4));
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))) == 0) goto loc_00A02E03;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(a1)));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1))))) goto loc_00A02E03;
    if (((unsigned int)(result)) < 8) goto loc_00A02E03;
    a1 = (a1) + (a1);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 1)) == 0) goto loc_00A02E03;
    result = (unsigned int)((result) + (-8));
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 1)))) << (2);
    if (((unsigned int)((unsigned int)(result))) < a3) goto loc_00A02E03;
    v_stack_m180 = a6;
    result = LocalGetStringForSid(a1, v_stack_m170, v_stack_m148, v_stack_m98);
    v_r11 = 0;
    v_stack_m160 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00A03410;
    result = (result) | (-1);
loc_00A02EFD:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m170 + result * 2)) != 0) goto loc_00A02EFD;
    if (((unsigned int)((unsigned int)((unsigned int)(result + a1 + result * 2 * 1)) + result * 2)) < ((unsigned int)((unsigned int)((unsigned int)(result + a1 + result * 2 * 1))))) goto loc_00A03404;
    v_r13 = v_stack_m170;
    if (v_stack_m170 != 0) {
        a1 = v_stack_m170;
        result = PdcCloseEvent(a1, (unsigned int)((unsigned int)(result + a1 + result * 2 * 1)) + result * 2, v_stack_m148, v_stack_m98);
        v_r11 = 0;
        v_r13 = 0;
        v_stack_m170 = 0;
    }
    v_r15 = (unsigned int)((0) + 1);
    goto loc_00A02E64;
loc_00A02F3A:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00A03068;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_00A02E03;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(result)) < 2) goto loc_00A02E03;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))) + (a1);
    result = RtlStringCbLengthW(a1, (unsigned int)((unsigned int)(result)), v_stack_m168, v_stack_m98);
    if (sign_flag) goto loc_00A02E03;
    a1 = (unsigned int)(((unsigned int)(v_stack_m168)) + (4));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + a1 + result * 2 * 1)) + result * 2)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + a1 + result * 2 * 1)) + result * 2))))) goto loc_00A03404;
    v_r11 = (unsigned int)((v_r11) + 1);
    goto loc_00A02F3A;
loc_00A02F94:
loc_00A02F97:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r11)))) >= ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00A03068;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11)))) * 4 + 16))))) goto loc_00A02E03;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11)))) * 4 + 16)))));
    if (((unsigned int)(result)) < 8) goto loc_00A02E03;
    result = ui64tow_s(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11)))) * 4 + 16)) + a1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    v_r11 = 0;
loc_00A02FDF:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m128 + result * 2)) != 0) goto loc_00A02FDF;
    if (((unsigned int)((unsigned int)((unsigned int)(a1)) + result * 2)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_00A03404;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) + 1);
    goto loc_00A02F97;
loc_00A03000:
loc_00A03003:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00A03068;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))))) goto loc_00A02E03;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)))));
    if (((unsigned int)(result)) < 8) goto loc_00A02E03;
    result = i64tow_s(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16)) + a1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    v_r11 = 0;
loc_00A03047:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m128 + result * 2)) != 0) goto loc_00A03047;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)) + result * 2)) + result * 2)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)) + result * 2))))) goto loc_00A03404;
    v_r15 = (unsigned int)((0) + 1);
    goto loc_00A03003;
loc_00A03068:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)) + result * 2)) + result * 2)) + 3)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)) + result * 2)) + result * 2))))) goto loc_00A03404;
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)) + result * 2)) + result * 2)) + 3) & ((unsigned int)(0xFFFFFFFCULL));
    result = SddlpAlloc(a1, v_stack_m128, (unsigned int)(v_stack_m178), 10);
    v_r15 = 0;
    v_stack_m168 = result;
    if (result != 0) goto loc_00A03095;
    goto loc_00A03410;
loc_00A03095:
    *(unsigned __int16 *)(result + 2) = 34;
    v_rdi = (result + 2) + (2);
    *(unsigned __int16 *)(result) = 40;
    result = memcpy(v_rdi, v_stack_m150, (unsigned int)((unsigned int)((unsigned int)(v_stack_m140))), 10);
    v_rbx = ((unsigned int)(v_stack_m140)) >> (1);
    *(unsigned int *)(v_rdi + v_rbx * 2) = 0x2C0022ULL;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 4)))))) - (1));
    if (condition_is_equal) goto loc_00A0312F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A03126;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0311D;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A03114;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0310B;
    if (((unsigned int)(a1)) == 10) goto loc_00A03102;
loc_00A030EE:
loc_00A030F3:
    result = PdcCloseEvent(v_stack_m168, 44, (unsigned int)((unsigned int)((unsigned int)(v_stack_m140))), 10);
    goto loc_00A03410;
loc_00A03102:
    *(unsigned int *)(v_rdi + v_rbx * 2 + 4) = 0x580054ULL;
    goto loc_00A03136;
loc_00A0310B:
    *(unsigned int *)(v_rdi + v_rbx * 2 + 4) = 0x420054ULL;
    goto loc_00A03136;
loc_00A03114:
    *(unsigned int *)(v_rdi + v_rbx * 2 + 4) = 0x440054ULL;
    goto loc_00A03136;
loc_00A0311D:
    *(unsigned int *)(v_rdi + v_rbx * 2 + 4) = 0x530054ULL;
    goto loc_00A03136;
loc_00A03126:
    *(unsigned int *)(v_rdi + v_rbx * 2 + 4) = 0x550054ULL;
    goto loc_00A03136;
loc_00A0312F:
    *(unsigned int *)(v_rdi + v_rbx * 2 + 4) = 0x490054ULL;
loc_00A03136:
    *(unsigned __int16 *)(v_rdi + v_rbx * 2 + 8) = 44;
    result = (result) | (-1);
loc_00A03142:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m98 + result * 2)) != 0) goto loc_00A03142;
    *(unsigned int *)(v_rdi + v_rbx * 2 + 10) = 0x780030ULL;
    v_rbx = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    v_rdi = (v_rdi + v_rbx * 2) + (14);
    result = memcpy(v_rdi, v_stack_m98, v_rbx, 10);
    v_rdi = (v_rdi) + (v_rbx);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 4)))) - (1));
    if (condition_is_equal) goto loc_00A03383;
    v_r12 = (unsigned int)((v_r12) - (1));
    if (condition_is_equal) goto loc_00A03316;
    v_r12 = (unsigned int)((v_r12) - (1));
    if (condition_is_equal) goto loc_00A032AF;
    v_r12 = (unsigned int)((v_r12) - (2));
    if (condition_is_equal) goto loc_00A0321C;
    v_r12 = (unsigned int)((v_r12) - (1));
    if (condition_is_equal) goto loc_00A03316;
    if (((unsigned int)(v_r12)) != 10) goto loc_00A030EE;
    if (v_stack_m178 == 0) goto loc_00A033EF;
loc_00A031C5:
    *(unsigned __int16 *)(v_rdi) = 44;
    v_rdi = (v_rdi) + (2);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 16)) + 4) + (a1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1))) == 0) goto loc_00A0320D;
loc_00A031E3:
    a2 = (a2) + 1;
    a1 = (unsigned int)((*(unsigned __int8 *)(a2)) & (15));
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a2)))) >> (4);
    *(unsigned __int16 *)(v_rdi) = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 10269213 + result * 2));
    *(unsigned __int16 *)(v_rdi + 2) = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 10269213 + a1 * 2));
    v_rdi = (v_rdi) + (4);
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1))))) - (1);
    if (condition_is_not_equal) goto loc_00A031E3;
loc_00A0320D:
    a3 = (a1 + 16) + (4);
    v_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A031C5;
    goto loc_00A033EF;
loc_00A0321C:
    v_rbx = 0;
loc_00A03223:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00A033EF;
    *(unsigned __int16 *)(v_rdi) = 44;
    v_rdi = (v_rdi) + (2);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 0 * 4 + 16))) + (4));
    a1 = (a1) + (a1);
    v_stack_m180 = a6;
    result = LocalGetStringForSid(a1, v_stack_m170, v_stack_m148, (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1)));
    if ((unsigned int)(result) != 0) goto loc_00A030F3;
    result = (result) | (-1);
loc_00A0326F:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m170 + result * 2)) != 0) goto loc_00A0326F;
    v_rbx = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    result = memcpy(v_rdi, v_stack_m170, v_rbx, (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1)));
    v_rdi = (v_rdi) + (v_rbx);
    v_rbx = 0;
    v_r13 = v_stack_m170;
    if (v_stack_m170 != 0) {
        a1 = v_stack_m170;
        result = PdcCloseEvent(a1, v_stack_m170, v_rbx, (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1)));
        v_r13 = 0;
        v_stack_m170 = 0;
    }
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_00A03223;
loc_00A032AF:
    if (v_stack_m178 == ((unsigned int)(v_r15))) goto loc_00A033EF;
loc_00A032C9:
    *(unsigned int *)(v_rdi) = 0x22002CULL;
    result = (result) | (-1);
    v_rdi = (v_rdi) + (4);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 16))) + (a1);
    a1 = 0;
loc_00A032DF:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(a2 + result * 2)) != 0) goto loc_00A032DF;
    v_rbx = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    result = memcpy(v_rdi, a2, v_rbx, (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1)));
    v_rdi = (v_rdi) + (v_rbx);
    v_r15 = (a1 + 16) + (4);
    *(unsigned __int16 *)(v_rdi) = 34;
    v_rdi = (v_rdi) + (2);
    v_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A032C9;
    goto loc_00A033EA;
loc_00A03316:
    if (v_stack_m178 == ((unsigned int)(v_r15))) goto loc_00A033EF;
loc_00A0332A:
    *(unsigned __int16 *)(v_rdi) = 44;
    v_rdi = (v_rdi) + (2);
    result = ui64tow_s(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    a1 = 0;
loc_00A03357:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m128 + result * 2)) != 0) goto loc_00A03357;
    v_rbx = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    result = memcpy(v_rdi, v_stack_m128, v_rbx, 10);
    v_rdi = (v_rdi) + (v_rbx);
    v_r15 = (a1 + 16) + (4);
    v_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A0332A;
    goto loc_00A033EA;
loc_00A03383:
    if (v_stack_m178 == ((unsigned int)(v_r15))) goto loc_00A033EF;
loc_00A03393:
    *(unsigned __int16 *)(v_rdi) = 44;
    v_rdi = (v_rdi) + (2);
    result = i64tow_s(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 16)) + a1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    a1 = 0;
loc_00A033C0:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m128 + result * 2)) != 0) goto loc_00A033C0;
    v_rbx = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    result = memcpy(v_rdi, v_stack_m128, v_rbx, 10);
    v_rdi = (v_rdi) + (v_rbx);
    v_r15 = (a1 + 16) + (4);
    v_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A03393;
loc_00A033EA:
loc_00A033EF:
    *(unsigned int *)(v_rdi) = 41;
    *(unsigned __int64 *)(v_stack_m138) = v_stack_m168;
    goto loc_00A03410;
loc_00A03404:
    goto loc_00A03410;
loc_00A0340B:
loc_00A03410:
    result = v_stack_m150;
    if (v_stack_m150 != 0) {
        a1 = v_stack_m150;
        result = PdcCloseEvent(a1, v_stack_m128, v_rbx, 10);
    }
    if (v_stack_m170 != 0) {
        a1 = v_stack_m170;
        result = PdcCloseEvent(a1, v_stack_m128, v_rbx, 10);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m128, v_rbx, 10);
    v_rsp = (v_rsp) + (368);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t LocalGetStringForRelativeAttribute(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint8_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint8_t v_stack_m180;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x407AE5)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m148 = Arg3;
    v_stack_m138 = Arg7;
    Arg2 = 0;
    v_stack_m150 = 0;
    result = memset(v_stack_m98, Arg2, local_rsi + 70, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, 140, Arg4);
    v_stack_m170 = 0;
    v_stack_m168 = 0;
    if (Arg1 == 0) goto loc_00A0340B;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_00A0340B;
    if (Arg7 == 0) goto loc_00A0340B;
    if (((uint32_t)((uint32_t)(Arg2))) >= 20) goto loc_00A02CD5;
loc_00A02CCB:
    goto loc_00A0342F;
loc_00A02CD5:
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC))) == 0) goto loc_00A02CCB;
    result = ultow_s((uint32_t)(*(uint32_t *)(Arg1 + 0x8)), v_stack_m98, 16 + 19, 16);
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) goto loc_00A02CCB;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))));
    if (((uint32_t)(result)) < 4) goto loc_00A02CCB;
    result = RtlStringCbLengthW(Arg1 + (uint32_t)(*(uint32_t *)(Arg1)) * 1, (uint32_t)((uint32_t)(result)), v_stack_m168, 16);
    if (sign_flag) goto loc_00A02CCB;
    if ((uint32_t)(v_stack_m168) == 0) goto loc_00A02CCB;
    result = EncodeAttributeName(Arg1 + (uint32_t)(*(uint32_t *)(Arg1)) * 1, v_stack_m168, v_stack_m150, 16);
    local_r11 = 0;
    v_stack_m160 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00A03410;
    local_rdi = (Arg7) | (-1);
loc_00A02D59:
    Arg1 = (local_rdi) + 1;
    if ((*(uint16_t *)(v_stack_m150 + Arg1 * 2)) != 0) goto loc_00A02D59;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    v_stack_m158 = (uint32_t)(*(uint32_t *)(Arg1 + 0xC));
    v_stack_m140 = Arg1;
    if (((uint32_t)(*(uint32_t *)(Arg1 + 0xC)) + (uint32_t)(*(uint32_t *)(Arg1 + 0xC)) * 1) > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A03404;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0xC)) + (uint32_t)(*(uint32_t *)(Arg1 + 0xC)) * 1) + (24));
    if (((uint32_t)(result)) < 24) goto loc_00A03404;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_00A03404;
loc_00A02DA2:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(v_stack_m98 + result * 2)) != 0) goto loc_00A02DA2;
    if (((uint32_t)(Arg1 + result * 2)) < ((uint32_t)(Arg1))) goto loc_00A03404;
    if (((uint32_t)(*(uint32_t *)(Arg1 + 0xC)) * 4) > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A03404;
    if (((uint32_t)((uint32_t)(Arg2) - 16)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC)) * 4))) goto loc_00A02E03;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(Arg1 + 0x4)))) - (1));
    if (condition_is_equal) goto loc_00A03000;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A02F94;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A02F3A;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A02E61;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A02F94;
    if (((uint32_t)(Arg1)) == 10) goto loc_00A02E0D;
loc_00A02E03:
    goto loc_00A03410;
loc_00A02E0D:
loc_00A02E10:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC))))) goto loc_00A03068;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))))) goto loc_00A02E03;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(Arg1)) < 4) goto loc_00A02E03;
    if (((uint32_t)(Arg1 - 4)) < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)) + Arg1 * 1))))) goto loc_00A02E03;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)) + Arg1 * 1))))) << (2);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A03404;
    if (((uint32_t)(result + Arg1 + result * 2 * 1)) < ((uint32_t)(Arg1 + result * 2))) goto loc_00A03404;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00A02E10;
loc_00A02E61:
loc_00A02E64:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00A03068;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))))) goto loc_00A02E03;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(result)) < 4) goto loc_00A02E03;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))) + (4));
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)) + Arg1 * 1))) == 0) goto loc_00A02E03;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)) + Arg1 * 1))))) goto loc_00A02E03;
    if (((uint32_t)(result)) < 8) goto loc_00A02E03;
    Arg1 = (Arg1) + (Arg1);
    if ((uint8_t)(*(uint8_t *)(Arg1 + 0x1)) == 0) goto loc_00A02E03;
    result = (uint32_t)((result) + (-8));
    Arg3 = ((uint32_t)((uint32_t)(*(uint8_t *)(Arg1 + 0x1)))) << (2);
    if (((uint32_t)((uint32_t)(result))) < Arg3) goto loc_00A02E03;
    v_stack_m180 = Arg6;
    result = LocalGetStringForSid(Arg1, v_stack_m170, v_stack_m148, v_stack_m98);
    local_r11 = 0;
    v_stack_m160 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00A03410;
    result = (result) | (-1);
loc_00A02EFD:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m170 + result * 2)) != 0) goto loc_00A02EFD;
    if (((uint32_t)((uint32_t)((uint32_t)(result + Arg1 + result * 2 * 1)) + result * 2)) < ((uint32_t)((uint32_t)((uint32_t)(result + Arg1 + result * 2 * 1))))) goto loc_00A03404;
    local_r13 = v_stack_m170;
    if (v_stack_m170 != 0) {
        Arg1 = v_stack_m170;
        result = PdcCloseEvent(Arg1, (uint32_t)((uint32_t)(result + Arg1 + result * 2 * 1)) + result * 2, v_stack_m148, v_stack_m98);
        local_r11 = 0;
        local_r13 = 0;
        v_stack_m170 = 0;
    }
    local_r15 = (uint32_t)((0) + 1);
    goto loc_00A02E64;
loc_00A02F3A:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00A03068;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))))) goto loc_00A02E03;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(result)) < 2) goto loc_00A02E03;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))) + (Arg1);
    result = RtlStringCbLengthW(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m168, v_stack_m98);
    if (sign_flag) goto loc_00A02E03;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m168)) + (4));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + Arg1 + result * 2 * 1)) + result * 2)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + Arg1 + result * 2 * 1)) + result * 2))))) goto loc_00A03404;
    local_r11 = (uint32_t)((local_r11) + 1);
    goto loc_00A02F3A;
loc_00A02F94:
loc_00A02F97:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r11)))) >= ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00A03068;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11)))) * 4 + 0x10))))) goto loc_00A02E03;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11)))) * 4 + 0x10)))));
    if (((uint32_t)(result)) < 8) goto loc_00A02E03;
    result = ui64tow_s(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11)))) * 4 + 0x10)) + Arg1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    local_r11 = 0;
loc_00A02FDF:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m128 + result * 2)) != 0) goto loc_00A02FDF;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)) + result * 2)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_00A03404;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) + 1);
    goto loc_00A02F97;
loc_00A03000:
loc_00A03003:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00A03068;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))))) goto loc_00A02E03;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)))));
    if (((uint32_t)(result)) < 8) goto loc_00A02E03;
    result = i64tow_s(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10)) + Arg1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    local_r11 = 0;
loc_00A03047:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m128 + result * 2)) != 0) goto loc_00A03047;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)) + result * 2)) + result * 2)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)) + result * 2))))) goto loc_00A03404;
    local_r15 = (uint32_t)((0) + 1);
    goto loc_00A03003;
loc_00A03068:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)) + result * 2)) + result * 2)) + 3)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)) + result * 2)) + result * 2))))) goto loc_00A03404;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)) + result * 2)) + result * 2)) + 3) & ((uint32_t)(0xFFFFFFFCULL));
    result = SddlpAlloc(Arg1, v_stack_m128, (uint32_t)(v_stack_m178), 10);
    local_r15 = 0;
    v_stack_m168 = result;
    if (result != 0) goto loc_00A03095;
    goto loc_00A03410;
loc_00A03095:
    *(uint16_t *)(result + 0x2) = 34;
    local_rdi = (result + 2) + (2);
    *(uint16_t *)(result) = 40;
    result = memcpy(local_rdi, v_stack_m150, (uint32_t)((uint32_t)((uint32_t)(v_stack_m140))), 10);
    local_rbx = ((uint32_t)(v_stack_m140)) >> (1);
    *(uint32_t *)(local_rdi + local_rbx * 2) = 0x2C0022ULL;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(Arg1 + 0x4)))))) - (1));
    if (condition_is_equal) goto loc_00A0312F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A03126;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0311D;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A03114;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0310B;
    if (((uint32_t)(Arg1)) == 10) goto loc_00A03102;
loc_00A030EE:
loc_00A030F3:
    result = PdcCloseEvent(v_stack_m168, 44, (uint32_t)((uint32_t)((uint32_t)(v_stack_m140))), 10);
    goto loc_00A03410;
loc_00A03102:
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0x4) = 0x580054ULL;
    goto loc_00A03136;
loc_00A0310B:
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0x4) = 0x420054ULL;
    goto loc_00A03136;
loc_00A03114:
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0x4) = 0x440054ULL;
    goto loc_00A03136;
loc_00A0311D:
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0x4) = 0x530054ULL;
    goto loc_00A03136;
loc_00A03126:
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0x4) = 0x550054ULL;
    goto loc_00A03136;
loc_00A0312F:
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0x4) = 0x490054ULL;
loc_00A03136:
    *(uint16_t *)(local_rdi + local_rbx * 2 + 0x8) = 44;
    result = (result) | (-1);
loc_00A03142:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m98 + result * 2)) != 0) goto loc_00A03142;
    *(uint32_t *)(local_rdi + local_rbx * 2 + 0xA) = 0x780030ULL;
    local_rbx = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    local_rdi = (local_rdi + local_rbx * 2) + (14);
    result = memcpy(local_rdi, v_stack_m98, local_rbx, 10);
    local_rdi = (local_rdi) + (local_rbx);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(Arg1 + 0x4)))) - (1));
    if (condition_is_equal) goto loc_00A03383;
    local_r12 = (uint32_t)((local_r12) - (1));
    if (condition_is_equal) goto loc_00A03316;
    local_r12 = (uint32_t)((local_r12) - (1));
    if (condition_is_equal) goto loc_00A032AF;
    local_r12 = (uint32_t)((local_r12) - (2));
    if (condition_is_equal) goto loc_00A0321C;
    local_r12 = (uint32_t)((local_r12) - (1));
    if (condition_is_equal) goto loc_00A03316;
    if (((uint32_t)(local_r12)) != 10) goto loc_00A030EE;
    if (v_stack_m178 == 0) goto loc_00A033EF;
loc_00A031C5:
    *(uint16_t *)(local_rdi) = 44;
    local_rdi = (local_rdi) + (2);
    Arg2 = ((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + 4) + (Arg1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1))) == 0) goto loc_00A0320D;
loc_00A031E3:
    Arg2 = (Arg2) + 1;
    Arg1 = (uint32_t)((*(uint8_t *)(Arg2)) & (15));
    result = ((uint32_t)((uint32_t)(*(uint8_t *)(Arg2)))) >> (4);
    *(uint16_t *)(local_rdi) = (uint16_t)(*(uint16_t *)(v_rip - 0x9CB21D + result * 2));
    *(uint16_t *)(local_rdi + 0x2) = (uint16_t)(*(uint16_t *)(v_rip - 0x9CB21D + Arg1 * 2));
    local_rdi = (local_rdi) + (4);
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1))))) - (1);
    if (condition_is_not_equal) goto loc_00A031E3;
loc_00A0320D:
    Arg3 = (Arg1 + 16) + (4);
    local_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A031C5;
    goto loc_00A033EF;
loc_00A0321C:
    local_rbx = 0;
loc_00A03223:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00A033EF;
    *(uint16_t *)(local_rdi) = 44;
    local_rdi = (local_rdi) + (2);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x0 * 4 + 0x10))) + (4));
    Arg1 = (Arg1) + (Arg1);
    v_stack_m180 = Arg6;
    result = LocalGetStringForSid(Arg1, v_stack_m170, v_stack_m148, (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1)));
    if ((uint32_t)(result) != 0) goto loc_00A030F3;
    result = (result) | (-1);
loc_00A0326F:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m170 + result * 2)) != 0) goto loc_00A0326F;
    local_rbx = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    result = memcpy(local_rdi, v_stack_m170, local_rbx, (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1)));
    local_rdi = (local_rdi) + (local_rbx);
    local_rbx = 0;
    local_r13 = v_stack_m170;
    if (v_stack_m170 != 0) {
        Arg1 = v_stack_m170;
        result = PdcCloseEvent(Arg1, v_stack_m170, local_rbx, (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1)));
        local_r13 = 0;
        v_stack_m170 = 0;
    }
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_00A03223;
loc_00A032AF:
    if (v_stack_m178 == ((uint32_t)(local_r15))) goto loc_00A033EF;
loc_00A032C9:
    *(uint32_t *)(local_rdi) = 0x22002CULL;
    result = (result) | (-1);
    local_rdi = (local_rdi) + (4);
    Arg2 = ((uint32_t)(*(uint32_t *)(Arg1 + 0x10))) + (Arg1);
    Arg1 = 0;
loc_00A032DF:
    result = (result) + 1;
    if ((*(uint16_t *)(Arg2 + result * 2)) != 0) goto loc_00A032DF;
    local_rbx = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    result = memcpy(local_rdi, Arg2, local_rbx, (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1)));
    local_rdi = (local_rdi) + (local_rbx);
    local_r15 = (Arg1 + 16) + (4);
    *(uint16_t *)(local_rdi) = 34;
    local_rdi = (local_rdi) + (2);
    local_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A032C9;
    goto loc_00A033EA;
loc_00A03316:
    if (v_stack_m178 == ((uint32_t)(local_r15))) goto loc_00A033EF;
loc_00A0332A:
    *(uint16_t *)(local_rdi) = 44;
    local_rdi = (local_rdi) + (2);
    result = ui64tow_s(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    Arg1 = 0;
loc_00A03357:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m128 + result * 2)) != 0) goto loc_00A03357;
    local_rbx = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    result = memcpy(local_rdi, v_stack_m128, local_rbx, 10);
    local_rdi = (local_rdi) + (local_rbx);
    local_r15 = (Arg1 + 16) + (4);
    local_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A0332A;
    goto loc_00A033EA;
loc_00A03383:
    if (v_stack_m178 == ((uint32_t)(local_r15))) goto loc_00A033EF;
loc_00A03393:
    *(uint16_t *)(local_rdi) = 44;
    local_rdi = (local_rdi) + (2);
    result = i64tow_s(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)) + Arg1 * 1), v_stack_m128, 10 + 60, 10);
    result = (result) | (-1);
    Arg1 = 0;
loc_00A033C0:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m128 + result * 2)) != 0) goto loc_00A033C0;
    local_rbx = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    result = memcpy(local_rdi, v_stack_m128, local_rbx, 10);
    local_rdi = (local_rdi) + (local_rbx);
    local_r15 = (Arg1 + 16) + (4);
    local_r12 = (v_stack_m158) - (1);
    if (condition_is_not_equal) goto loc_00A03393;
loc_00A033EA:
loc_00A033EF:
    *(uint32_t *)(local_rdi) = 41;
    *(uint64_t *)(v_stack_m138) = v_stack_m168;
    goto loc_00A03410;
loc_00A03404:
    goto loc_00A03410;
loc_00A0340B:
loc_00A03410:
    result = v_stack_m150;
    if (v_stack_m150 != 0) {
        Arg1 = v_stack_m150;
        result = PdcCloseEvent(Arg1, v_stack_m128, local_rbx, 10);
    }
    if (v_stack_m170 != 0) {
        Arg1 = v_stack_m170;
        result = PdcCloseEvent(Arg1, v_stack_m128, local_rbx, 10);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m128, local_rbx, 10);
    local_rsp = (local_rsp) + (368);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A02C38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
