# PiDevCfgResolveVariableExpression

- RVA: `0x00AA8C00`–`0x00AA9E5C` (길이 `4,700` bytes)
- VA: `0x0000000140AA8C00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBC24`
- 디코드: `1,296`개 명령, `4,700/4,700` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00AA8C62` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00AA8C7B` → [PnpValidateRegistryMultiSz](../../text/4D/PnpValidateRegistryMultiSz_function_004DC170.md) (function, `0x004DC170`)
- `0x00AA8CE6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA8EA0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA8EC5` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00AA8F4B` → [PnpStringToDwordValue](../../text/4E/PnpStringToDwordValue_function_004E1894.md) (function, `0x004E1894`)
- `0x00AA90C6` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00AA90EB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA910F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA91D6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA91FB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9228` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA927B` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA929D` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA92C1` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA92E8` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA9307` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA93C2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA93E0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9453` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00AA9472` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00AA9490` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00AA94BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA94EA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9539` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA955B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9577` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA975F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00AA9788` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00AA9820` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00AA9852` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA9876` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9890` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA98B3` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00AA9973` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA999D` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA99CD` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA99F8` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA9A1B` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA9A46` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00AA9ACB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA9AF1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9B0F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA9BA2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA9C1A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA9C7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9C86` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9CEE` → [PiDevCfgResolveVariable](../A8/PiDevCfgResolveVariable_function_00A81AB8.md) (function, `0x00A81AB8`)
- `0x00AA9D17` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9D69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9D73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9DBE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9DC8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9DE2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9E0E` → [PiDevCfgCopyVariableData](../73/PiDevCfgCopyVariableData_function_007327F8.md) (function, `0x007327F8`)
- `0x00AA9E2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA9E3B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AA8C1C` → RVA `0x00E0A740` (`.data`; read)
- `0x00AA8C4D` → RVA `0x00AFF570` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AA8D0A` → RVA `0x00B50EE0` (`PAGE`; read)
- `0x00AA8E18` → RVA `0x00B4AEB0` (`PAGE`; read)
- `0x00AA8EB7` → RVA `0x00AFDAA0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **42**
  - `0x00AA8C7B` → [PnpValidateRegistryMultiSz](../../text/4D/PnpValidateRegistryMultiSz_function_004DC170.md) (`PAGE` → `.text`)
  - `0x00AA8CE6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA8EA0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA8EC5` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x00AA8F4B` → [PnpStringToDwordValue](../../text/4E/PnpStringToDwordValue_function_004E1894.md) (`PAGE` → `.text`)
  - `0x00AA90C6` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00AA90EB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA910F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA91D6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA91FB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA93C2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA93E0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA9453` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00AA9472` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00AA9490` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00AA94BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA94EA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA9539` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA955B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA9577` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA975F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00AA9788` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00AA9820` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00AA9852` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9876` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA9890` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA98B3` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00AA9ACB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9AF1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA9B0F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA9BA2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9C1A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9C7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9C86` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9D17` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9D69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9D73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9DBE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9DC8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9DE2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9E2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA9E3B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA8C00  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AA8C05  55                              push rbp
00AA8C06  56                              push rsi
00AA8C07  57                              push rdi
00AA8C08  41 54                           push r12
00AA8C0A  41 55                           push r13
00AA8C0C  41 56                           push r14
00AA8C0E  41 57                           push r15
00AA8C10  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00AA8C15  48 81 EC B0 00 00 00            sub rsp, 0xb0
00AA8C1C  48 8B 05 1D 1B 36 00            mov rax, qword ptr [rip + 0x361b1d]
00AA8C23  48 33 C4                        xor rax, rsp
00AA8C26  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
00AA8C2A  48 8B C2                        mov rax, rdx
00AA8C2D  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
00AA8C31  33 D2                           xor edx, edx
00AA8C33  4C 89 45 FF                     mov qword ptr [rbp - 1], r8
00AA8C37  33 C9                           xor ecx, ecx
00AA8C39  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
00AA8C3D  44 8B E2                        mov r12d, edx
00AA8C40  89 55 C7                        mov dword ptr [rbp - 0x39], edx
00AA8C43  44 8B F2                        mov r14d, edx
00AA8C46  48 89 4D 17                     mov qword ptr [rbp + 0x17], rcx
00AA8C4A  0F 57 C0                        xorps xmm0, xmm0
00AA8C4D  48 8D 15 1C 69 05 00            lea rdx, [rip + 0x5691c]
00AA8C54  48 8B C8                        mov rcx, rax
00AA8C57  4C 8D 4D F7                     lea r9, [rbp - 9]
00AA8C5B  45 33 C0                        xor r8d, r8d
00AA8C5E  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00AA8C62  E8 85 04 EF FF                  call 0x1409990ec
00AA8C67  45 33 DB                        xor r11d, r11d
00AA8C6A  8B D8                           mov ebx, eax
00AA8C6C  85 C0                           test eax, eax
00AA8C6E  0F 88 AB 11 00 00               js 0x140aa9e1f
00AA8C74  4C 8B 55 F7                     mov r10, qword ptr [rbp - 9]
00AA8C78  49 8B CA                        mov rcx, r10
00AA8C7B  E8 F0 34 A3 FF                  call 0x1404dc170
00AA8C80  84 C0                           test al, al
00AA8C82  0F 84 92 11 00 00               je 0x140aa9e1a
00AA8C88  41 8B 72 08                     mov esi, dword ptr [r10 + 8]
00AA8C8C  49 03 F2                        add rsi, r10
00AA8C8F  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
00AA8C93  48 8B C6                        mov rax, rsi
00AA8C96  66 44 39 1E                     cmp word ptr [rsi], r11w
00AA8C9A  0F 84 7A 11 00 00               je 0x140aa9e1a
00AA8CA0  45 8D 6B 01                     lea r13d, [r11 + 1]
00AA8CA4  45 03 E5                        add r12d, r13d
00AA8CA7  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00AA8CAB  48 FF C1                        inc rcx
00AA8CAE  66 44 39 1C 48                  cmp word ptr [rax + rcx*2], r11w
00AA8CB3  75 F6                           jne 0x140aa8cab
00AA8CB5  48 8D 04 48                     lea rax, [rax + rcx*2]
00AA8CB9  48 83 C0 02                     add rax, 2
00AA8CBD  66 44 39 18                     cmp word ptr [rax], r11w
00AA8CC1  75 E1                           jne 0x140aa8ca4
00AA8CC3  4C 8B 6D EF                     mov r13, qword ptr [rbp - 0x11]
00AA8CC7  44 89 65 E7                     mov dword ptr [rbp - 0x19], r12d
00AA8CCB  45 85 E4                        test r12d, r12d
00AA8CCE  0F 84 46 11 00 00               je 0x140aa9e1a
00AA8CD4  41 8B D4                        mov edx, r12d
00AA8CD7  B9 00 01 00 00                  mov ecx, 0x100
00AA8CDC  48 C1 E2 03                     shl rdx, 3
00AA8CE0  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA8CE6  E8 05 94 0D 00                  call 0x140b820f0
00AA8CEB  45 33 DB                        xor r11d, r11d
00AA8CEE  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00AA8CF2  4C 8B F8                        mov r15, rax
00AA8CF5  48 85 C0                        test rax, rax
00AA8CF8  75 0A                           jne 0x140aa8d04
00AA8CFA  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AA8CFF  E9 1B 11 00 00                  jmp 0x140aa9e1f
00AA8D04  41 B9 01 00 00 00               mov r9d, 1
00AA8D0A  4C 8D 15 CF 81 0A 00            lea r10, [rip + 0xa81cf]
00AA8D11  8B FB                           mov edi, ebx
00AA8D13  66 44 39 1E                     cmp word ptr [rsi], r11w
00AA8D17  0F 84 E1 10 00 00               je 0x140aa9dfe
00AA8D1D  66 44 39 5E 02                  cmp word ptr [rsi + 2], r11w
00AA8D22  74 0B                           je 0x140aa8d2f
00AA8D24  66 44 39 5E 04                  cmp word ptr [rsi + 4], r11w
00AA8D29  0F 85 A8 0F 00 00               jne 0x140aa9cd7
00AA8D2F  41 8B D1                        mov edx, r9d
00AA8D32  83 FA 1B                        cmp edx, 0x1b
00AA8D35  0F 83 9C 0F 00 00               jae 0x140aa9cd7
00AA8D3B  8B C2                           mov eax, edx
00AA8D3D  4C 8D 04 40                     lea r8, [rax + rax*2]
00AA8D41  4B 8B 44 C2 08                  mov rax, qword ptr [r10 + r8*8 + 8]
00AA8D46  8B 08                           mov ecx, dword ptr [rax]
00AA8D48  39 0E                           cmp dword ptr [rsi], ecx
00AA8D4A  74 05                           je 0x140aa8d51
00AA8D4C  41 03 D1                        add edx, r9d
00AA8D4F  EB E1                           jmp 0x140aa8d32
00AA8D51  4B 8D 14 C2                     lea rdx, [r10 + r8*8]
00AA8D55  48 85 D2                        test rdx, rdx
00AA8D58  0F 84 79 0F 00 00               je 0x140aa9cd7
00AA8D5E  44 8B 42 10                     mov r8d, dword ptr [rdx + 0x10]
00AA8D62  45 8B D3                        mov r10d, r11d
00AA8D65  44 89 5D AB                     mov dword ptr [rbp - 0x55], r11d
00AA8D69  41 83 CD FF                     or r13d, 0xffffffff
00AA8D6D  45 3B D0                        cmp r10d, r8d
00AA8D70  73 25                           jae 0x140aa8d97
00AA8D72  45 85 F6                        test r14d, r14d
00AA8D75  0F 84 92 0F 00 00               je 0x140aa9d0d
00AA8D7B  45 03 F5                        add r14d, r13d
00AA8D7E  41 8B CA                        mov ecx, r10d
00AA8D81  45 03 D1                        add r10d, r9d
00AA8D84  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
00AA8D88  44 89 55 AB                     mov dword ptr [rbp - 0x55], r10d
00AA8D8C  4B 8B 04 F7                     mov rax, qword ptr [r15 + r14*8]
00AA8D90  48 89 44 CD 07                  mov qword ptr [rbp + rcx*8 + 7], rax
00AA8D95  EB D6                           jmp 0x140aa8d6d
00AA8D97  85 FF                           test edi, edi
00AA8D99  0F 88 A3 0F 00 00               js 0x140aa9d42
00AA8D9F  44 89 5D CF                     mov dword ptr [rbp - 0x31], r11d
00AA8DA3  45 0F B7 F3                     movzx r14d, r11w
00AA8DA7  4C 89 75 AF                     mov qword ptr [rbp - 0x51], r14
00AA8DAB  45 0F B7 E3                     movzx r12d, r11w
00AA8DAF  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00AA8DB3  41 8B F3                        mov esi, r11d
00AA8DB6  4C 89 5D BF                     mov qword ptr [rbp - 0x41], r11
00AA8DBA  4D 8B FB                        mov r15, r11
00AA8DBD  4C 89 5D B7                     mov qword ptr [rbp - 0x49], r11
00AA8DC1  45 3B D1                        cmp r10d, r9d
00AA8DC4  0F 85 E1 01 00 00               jne 0x140aa8fab
00AA8DCA  8B 0A                           mov ecx, dword ptr [rdx]
00AA8DCC  8B D1                           mov edx, ecx
00AA8DCE  83 EA 16                        sub edx, 0x16
00AA8DD1  0F 84 BE 01 00 00               je 0x140aa8f95
00AA8DD7  83 FA 01                        cmp edx, 1
00AA8DDA  0F 84 A4 01 00 00               je 0x140aa8f84
00AA8DE0  4C 8B 45 07                     mov r8, qword ptr [rbp + 7]
00AA8DE4  41 8B 50 20                     mov edx, dword ptr [r8 + 0x20]
00AA8DE8  83 EA 01                        sub edx, 1
00AA8DEB  0F 84 27 01 00 00               je 0x140aa8f18
00AA8DF1  83 EA 01                        sub edx, 1
00AA8DF4  0F 84 1E 01 00 00               je 0x140aa8f18
00AA8DFA  41 BD 02 00 00 00               mov r13d, 2
00AA8E00  41 2B D5                        sub edx, r13d
00AA8E03  74 5B                           je 0x140aa8e60
00AA8E05  83 FA 03                        cmp edx, 3
00AA8E08  75 0E                           jne 0x140aa8e18
00AA8E0A  49 8B 50 28                     mov rdx, qword ptr [r8 + 0x28]
00AA8E0E  83 E9 0B                        sub ecx, 0xb
00AA8E11  74 1E                           je 0x140aa8e31
00AA8E13  83 E9 01                        sub ecx, 1
00AA8E16  74 0C                           je 0x140aa8e24
00AA8E18  4C 8D 2D 91 20 0A 00            lea r13, [rip + 0xa2091]
00AA8E1F  E9 2C 0E 00 00                  jmp 0x140aa9c50
00AA8E24  66 44 39 1A                     cmp word ptr [rdx], r11w
00AA8E28  40 0F 94 C6                     sete sil
00AA8E2C  E9 61 0D 00 00                  jmp 0x140aa9b92
00AA8E31  66 44 39 1A                     cmp word ptr [rdx], r11w
00AA8E35  0F 84 57 0D 00 00               je 0x140aa9b92
00AA8E3B  FF C6                           inc esi
00AA8E3D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AA8E41  48 FF C0                        inc rax
00AA8E44  66 44 39 1C 42                  cmp word ptr [rdx + rax*2], r11w
00AA8E49  75 F6                           jne 0x140aa8e41
00AA8E4B  48 8D 14 42                     lea rdx, [rdx + rax*2]
00AA8E4F  49 03 D5                        add rdx, r13
00AA8E52  66 44 39 1A                     cmp word ptr [rdx], r11w
00AA8E56  75 E3                           jne 0x140aa8e3b
00AA8E58  4D 8B EB                        mov r13, r11
00AA8E5B  E9 EA 02 00 00                  jmp 0x140aa914a
00AA8E60  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
00AA8E64  8B 18                           mov ebx, dword ptr [rax]
00AA8E66  83 E9 0B                        sub ecx, 0xb
00AA8E69  0F 84 9B 00 00 00               je 0x140aa8f0a
00AA8E6F  83 E9 01                        sub ecx, 1
00AA8E72  0F 84 8A 00 00 00               je 0x140aa8f02
00AA8E78  83 E9 0D                        sub ecx, 0xd
00AA8E7B  74 7C                           je 0x140aa8ef9
00AA8E7D  83 F9 01                        cmp ecx, 1
00AA8E80  74 0E                           je 0x140aa8e90
00AA8E82  4C 8D 2D 27 20 0A 00            lea r13, [rip + 0xa2027]
00AA8E89  8B DF                           mov ebx, edi
00AA8E8B  E9 C0 0D 00 00                  jmp 0x140aa9c50
00AA8E90  BA 16 00 00 00                  mov edx, 0x16
00AA8E95  B9 00 01 00 00                  mov ecx, 0x100
00AA8E9A  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA8EA0  E8 4B 92 0D 00                  call 0x140b820f0
00AA8EA5  45 33 DB                        xor r11d, r11d
00AA8EA8  4C 8B F8                        mov r15, rax
00AA8EAB  48 85 C0                        test rax, rax
00AA8EAE  0F 84 70 0E 00 00               je 0x140aa9d24
00AA8EB4  44 8B CB                        mov r9d, ebx
00AA8EB7  4C 8D 05 E2 4B 05 00            lea r8, [rip + 0x54be2]
00AA8EBE  41 8D 53 0B                     lea edx, [r11 + 0xb]
00AA8EC2  48 8B C8                        mov rcx, rax
00AA8EC5  E8 92 9E 9D FF                  call 0x140482d5c
00AA8ECA  33 D2                           xor edx, edx
00AA8ECC  8B D8                           mov ebx, eax
00AA8ECE  85 C0                           test eax, eax
00AA8ED0  0F 88 3E 0E 00 00               js 0x140aa9d14
00AA8ED6  49 83 CE FF                     or r14, 0xffffffffffffffff
00AA8EDA  49 FF C6                        inc r14
00AA8EDD  66 43 39 14 77                  cmp word ptr [r15 + r14*2], dx
00AA8EE2  75 F6                           jne 0x140aa8eda
00AA8EE4  66 45 03 F6                     add r14w, r14w
00AA8EE8  45 0F B7 E6                     movzx r12d, r14w
00AA8EEC  66 45 03 F5                     add r14w, r13w
00AA8EF0  4C 89 75 AF                     mov qword ptr [rbp - 0x51], r14
00AA8EF4  E9 99 0C 00 00                  jmp 0x140aa9b92
00AA8EF9  8B F3                           mov esi, ebx
00AA8EFB  8B DF                           mov ebx, edi
00AA8EFD  E9 90 0C 00 00                  jmp 0x140aa9b92
00AA8F02  85 DB                           test ebx, ebx
00AA8F04  40 0F 94 C6                     sete sil
00AA8F08  EB F1                           jmp 0x140aa8efb
00AA8F0A  8B F3                           mov esi, ebx
00AA8F0C  F7 D6                           not esi
00AA8F0E  8B DF                           mov ebx, edi
00AA8F10  4D 8B EB                        mov r13, r11
00AA8F13  E9 6D 0C 00 00                  jmp 0x140aa9b85
00AA8F18  4D 8B 48 28                     mov r9, qword ptr [r8 + 0x28]
00AA8F1C  83 E9 0B                        sub ecx, 0xb
00AA8F1F  74 53                           je 0x140aa8f74
00AA8F21  83 E9 01                        sub ecx, 1
00AA8F24  74 44                           je 0x140aa8f6a
00AA8F26  83 E9 0D                        sub ecx, 0xd
00AA8F29  74 19                           je 0x140aa8f44
00AA8F2B  83 F9 01                        cmp ecx, 1
00AA8F2E  74 0C                           je 0x140aa8f3c
00AA8F30  4C 8D 2D 79 1F 0A 00            lea r13, [rip + 0xa1f79]
00AA8F37  E9 49 0C 00 00                  jmp 0x140aa9b85
00AA8F3C  4D 8B E8                        mov r13, r8
00AA8F3F  E9 41 0C 00 00                  jmp 0x140aa9b85
00AA8F44  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00AA8F48  49 8B C9                        mov rcx, r9
00AA8F4B  E8 44 89 A3 FF                  call 0x1404e1894
00AA8F50  45 33 DB                        xor r11d, r11d
00AA8F53  4D 8B EF                        mov r13, r15
00AA8F56  84 C0                           test al, al
00AA8F58  75 08                           jne 0x140aa8f62
00AA8F5A  41 8B F3                        mov esi, r11d
00AA8F5D  E9 23 0C 00 00                  jmp 0x140aa9b85
00AA8F62  8B 75 CF                        mov esi, dword ptr [rbp - 0x31]
00AA8F65  E9 1B 0C 00 00                  jmp 0x140aa9b85
00AA8F6A  66 45 39 19                     cmp word ptr [r9], r11w
00AA8F6E  40 0F 94 C6                     sete sil
00AA8F72  EB 9C                           jmp 0x140aa8f10
00AA8F74  48 83 CE FF                     or rsi, 0xffffffffffffffff
00AA8F78  48 FF C6                        inc rsi
00AA8F7B  66 45 39 1C 71                  cmp word ptr [r9 + rsi*2], r11w
00AA8F80  75 F6                           jne 0x140aa8f78
00AA8F82  EB 8C                           jmp 0x140aa8f10
00AA8F84  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00AA8F88  44 39 58 20                     cmp dword ptr [rax + 0x20], r11d
00AA8F8C  41 0F 44 F1                     cmove esi, r9d
00AA8F90  E9 FD 0B 00 00                  jmp 0x140aa9b92
00AA8F95  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00AA8F99  44 39 58 20                     cmp dword ptr [rax + 0x20], r11d
00AA8F9D  0F 84 EF 0B 00 00               je 0x140aa9b92
00AA8FA3  41 8B F1                        mov esi, r9d
00AA8FA6  E9 65 FF FF FF                  jmp 0x140aa8f10
00AA8FAB  41 B8 02 00 00 00               mov r8d, 2
00AA8FB1  45 3B D0                        cmp r10d, r8d
00AA8FB4  0F 85 78 0B 00 00               jne 0x140aa9b32
00AA8FBA  48 8B 5D 0F                     mov rbx, qword ptr [rbp + 0xf]
00AA8FBE  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
00AA8FC1  83 E9 01                        sub ecx, 1
00AA8FC4  0F 84 E8 07 00 00               je 0x140aa97b2
00AA8FCA  83 E9 01                        sub ecx, 1
00AA8FCD  0F 84 DF 07 00 00               je 0x140aa97b2
00AA8FD3  83 E9 01                        sub ecx, 1
00AA8FD6  0F 84 49 07 00 00               je 0x140aa9725
00AA8FDC  83 E9 01                        sub ecx, 1
00AA8FDF  0F 84 B6 05 00 00               je 0x140aa959b
00AA8FE5  83 F9 03                        cmp ecx, 3
00AA8FE8  0F 85 94 FE FF FF               jne 0x140aa8e82
00AA8FEE  4C 8B 7D 07                     mov r15, qword ptr [rbp + 7]
00AA8FF2  41 8B 4F 20                     mov ecx, dword ptr [r15 + 0x20]
00AA8FF6  83 F9 07                        cmp ecx, 7
00AA8FF9  0F 85 30 03 00 00               jne 0x140aa932f
00AA8FFF  44 8B 6B 24                     mov r13d, dword ptr [rbx + 0x24]
00AA9003  4D 8B 47 28                     mov r8, qword ptr [r15 + 0x28]
00AA9007  4C 8B 63 28                     mov r12, qword ptr [rbx + 0x28]
00AA900B  45 8B 77 24                     mov r14d, dword ptr [r15 + 0x24]
00AA900F  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
00AA9013  41 81 FD FE FF 00 00            cmp r13d, 0xfffe
00AA901A  0F 87 0E 0D 00 00               ja 0x140aa9d2e
00AA9020  41 81 FE FE FF 00 00            cmp r14d, 0xfffe
00AA9027  0F 87 01 0D 00 00               ja 0x140aa9d2e
00AA902D  8B 0A                           mov ecx, dword ptr [rdx]
00AA902F  83 F9 0F                        cmp ecx, 0xf
00AA9032  0F 8F 0F 02 00 00               jg 0x140aa9247
00AA9038  0F 84 D6 01 00 00               je 0x140aa9214
00AA903E  83 E9 01                        sub ecx, 1
00AA9041  0F 84 44 01 00 00               je 0x140aa918b
00AA9047  83 E9 07                        sub ecx, 7
00AA904A  74 45                           je 0x140aa9091
00AA904C  83 E9 01                        sub ecx, 1
00AA904F  0F 84 36 01 00 00               je 0x140aa918b
00AA9055  83 E9 04                        sub ecx, 4
00AA9058  74 13                           je 0x140aa906d
00AA905A  83 F9 01                        cmp ecx, 1
00AA905D  0F 85 1F FE FF FF               jne 0x140aa8e82
00AA9063  8D 41 01                        lea eax, [rcx + 1]
00AA9066  44 3B E8                        cmp r13d, eax
00AA9069  76 0C                           jbe 0x140aa9077
00AA906B  EB 0F                           jmp 0x140aa907c
00AA906D  B8 02 00 00 00                  mov eax, 2
00AA9072  44 3B E8                        cmp r13d, eax
00AA9075  76 08                           jbe 0x140aa907f
00AA9077  44 3B F0                        cmp r14d, eax
00AA907A  76 03                           jbe 0x140aa907f
00AA907C  41 8B F1                        mov esi, r9d
00AA907F  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA9083  8B DF                           mov ebx, edi
00AA9085  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA9089  4D 8B FB                        mov r15, r11
00AA908C  E9 01 0B 00 00                  jmp 0x140aa9b92
00AA9091  41 8B C3                        mov eax, r11d
00AA9094  8B DF                           mov ebx, edi
00AA9096  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00AA9099  4D 8B FB                        mov r15, r11
00AA909C  49 8B CF                        mov rcx, r15
00AA909F  66 45 39 1C 24                  cmp word ptr [r12], r11w
00AA90A4  0F 84 AD 00 00 00               je 0x140aa9157
00AA90AA  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AA90AE  48 FF C0                        inc rax
00AA90B1  66 45 39 1C 44                  cmp word ptr [r12 + rax*2], r11w
00AA90B6  75 F6                           jne 0x140aa90ae
00AA90B8  49 8B D4                        mov rdx, r12
00AA90BB  44 8D 34 45 02 00 00 00         lea r14d, [rax*2 + 2]
00AA90C3  49 8B C8                        mov rcx, r8
00AA90C6  E8 75 96 A1 FF                  call 0x1404c2740
00AA90CB  45 33 DB                        xor r11d, r11d
00AA90CE  48 85 C0                        test rax, rax
00AA90D1  74 50                           je 0x140aa9123
00AA90D3  4D 85 FF                        test r15, r15
00AA90D6  75 27                           jne 0x140aa90ff
00AA90D8  49 8B D5                        mov rdx, r13
00AA90DB  66 44 89 5D A7                  mov word ptr [rbp - 0x59], r11w
00AA90E0  B9 00 01 00 00                  mov ecx, 0x100
00AA90E5  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA90EB  E8 00 90 0D 00                  call 0x140b820f0
00AA90F0  45 33 DB                        xor r11d, r11d
00AA90F3  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA90F7  4C 8B F8                        mov r15, rax
00AA90FA  48 85 C0                        test rax, rax
00AA90FD  74 3A                           je 0x140aa9139
00AA90FF  0F B7 4D A7                     movzx ecx, word ptr [rbp - 0x59]
00AA9103  49 8B D4                        mov rdx, r12
00AA9106  49 03 CF                        add rcx, r15
00AA9109  45 8B C6                        mov r8d, r14d
00AA910C  41 8B FE                        mov edi, r14d
00AA910F  E8 2C D7 C1 FF                  call 0x1406c6840
00AA9114  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
00AA9117  66 41 03 C6                     add ax, r14w
00AA911B  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00AA911E  45 33 DB                        xor r11d, r11d
00AA9121  EB 06                           jmp 0x140aa9129
00AA9123  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
00AA9126  41 8B FE                        mov edi, r14d
00AA9129  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00AA912D  48 D1 EF                        shr rdi, 1
00AA9130  4D 8D 24 7C                     lea r12, [r12 + rdi*2]
00AA9134  E9 63 FF FF FF                  jmp 0x140aa909c
00AA9139  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA913D  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AA9142  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA9146  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00AA914A  85 DB                           test ebx, ebx
00AA914C  0F 88 E8 0B 00 00               js 0x140aa9d3a
00AA9152  E9 2E 0A 00 00                  jmp 0x140aa9b85
00AA9157  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00AA915B  44 0F B7 E0                     movzx r12d, ax
00AA915F  48 85 C9                        test rcx, rcx
00AA9162  74 DE                           je 0x140aa9142
00AA9164  66 83 C0 02                     add ax, 2
00AA9168  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00AA916C  0F B7 C0                        movzx eax, ax
00AA916F  0F B7 F8                        movzx edi, ax
00AA9172  44 0F B7 F0                     movzx r14d, ax
00AA9176  48 D1 E8                        shr rax, 1
00AA9179  44 8B E7                        mov r12d, edi
00AA917C  89 7D A7                        mov dword ptr [rbp - 0x59], edi
00AA917F  4C 89 75 AF                     mov qword ptr [rbp - 0x51], r14
00AA9183  66 45 89 5C 47 FE               mov word ptr [r15 + rax*2 - 2], r11w
00AA9189  EB BB                           jmp 0x140aa9146
00AA918B  66 45 39 1C 24                  cmp word ptr [r12], r11w
00AA9190  75 08                           jne 0x140aa919a
00AA9192  4D 8B EF                        mov r13, r15
00AA9195  E9 02 07 00 00                  jmp 0x140aa989c
00AA919A  66 45 39 18                     cmp word ptr [r8], r11w
00AA919E  0F 84 1C 07 00 00               je 0x140aa98c0
00AA91A4  43 8D 0C 2E                     lea ecx, [r14 + r13]
00AA91A8  BA 02 00 00 00                  mov edx, 2
00AA91AD  48 2B CA                        sub rcx, rdx
00AA91B0  48 81 F9 FE FF 00 00            cmp rcx, 0xfffe
00AA91B7  0F 87 71 0B 00 00               ja 0x140aa9d2e
00AA91BD  43 8D 04 2E                     lea eax, [r14 + r13]
00AA91C1  B9 00 01 00 00                  mov ecx, 0x100
00AA91C6  66 2B C2                        sub ax, dx
00AA91C9  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA91CF  0F B7 D0                        movzx edx, ax
00AA91D2  66 89 55 A7                     mov word ptr [rbp - 0x59], dx
00AA91D6  E8 15 8F 0D 00                  call 0x140b820f0
00AA91DB  45 33 DB                        xor r11d, r11d
00AA91DE  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA91E2  4C 8B F8                        mov r15, rax
00AA91E5  48 85 C0                        test rax, rax
00AA91E8  0F 84 36 0B 00 00               je 0x140aa9d24
00AA91EE  4D 8D 45 FE                     lea r8, [r13 - 2]
00AA91F2  49 8B D4                        mov rdx, r12
00AA91F5  48 8B C8                        mov rcx, rax
00AA91F8  49 8B DD                        mov rbx, r13
00AA91FB  E8 40 D6 C1 FF                  call 0x1406c6840
00AA9200  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00AA9204  48 D1 EB                        shr rbx, 1
00AA9207  48 8D 4B FF                     lea rcx, [rbx - 1]
00AA920B  49 8D 0C 4F                     lea rcx, [r15 + rcx*2]
00AA920F  E9 79 06 00 00                  jmp 0x140aa988d
00AA9214  4D 8B CE                        mov r9, r14
00AA9217  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA921C  49 8B D5                        mov rdx, r13
00AA921F  49 D1 E9                        shr r9, 1
00AA9222  48 D1 EA                        shr rdx, 1
00AA9225  49 8B CC                        mov rcx, r12
00AA9228  E8 B3 95 EC FF                  call 0x1409727e0
00AA922D  33 D2                           xor edx, edx
00AA922F  85 C0                           test eax, eax
00AA9231  8B CA                           mov ecx, edx
00AA9233  0F 94 C1                        sete cl
00AA9236  8B F1                           mov esi, ecx
00AA9238  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA923C  8B DF                           mov ebx, edi
00AA923E  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA9242  E9 47 09 00 00                  jmp 0x140aa9b8e
00AA9247  83 E9 10                        sub ecx, 0x10
00AA924A  0F 84 9F 00 00 00               je 0x140aa92ef
00AA9250  83 E9 01                        sub ecx, 1
00AA9253  74 7F                           je 0x140aa92d4
00AA9255  83 E9 01                        sub ecx, 1
00AA9258  74 53                           je 0x140aa92ad
00AA925A  83 E9 01                        sub ecx, 1
00AA925D  74 2A                           je 0x140aa9289
00AA925F  83 F9 01                        cmp ecx, 1
00AA9262  0F 85 1A FC FF FF               jne 0x140aa8e82
00AA9268  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00AA926C  4D 8B CE                        mov r9, r14
00AA926F  49 8B D5                        mov rdx, r13
00AA9272  49 D1 E9                        shr r9, 1
00AA9275  48 D1 EA                        shr rdx, 1
00AA9278  49 8B CC                        mov rcx, r12
00AA927B  E8 60 95 EC FF                  call 0x1409727e0
00AA9280  F7 D0                           not eax
00AA9282  C1 E8 1F                        shr eax, 0x1f
00AA9285  8B F0                           mov esi, eax
00AA9287  EB AF                           jmp 0x140aa9238
00AA9289  4D 8B CE                        mov r9, r14
00AA928C  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA9291  49 8B D5                        mov rdx, r13
00AA9294  49 D1 E9                        shr r9, 1
00AA9297  48 D1 EA                        shr rdx, 1
00AA929A  49 8B CC                        mov rcx, r12
00AA929D  E8 3E 95 EC FF                  call 0x1409727e0
00AA92A2  33 D2                           xor edx, edx
00AA92A4  85 C0                           test eax, eax
00AA92A6  8B CA                           mov ecx, edx
00AA92A8  0F 9E C1                        setle cl
00AA92AB  EB 89                           jmp 0x140aa9236
00AA92AD  4D 8B CE                        mov r9, r14
00AA92B0  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA92B5  49 8B D5                        mov rdx, r13
00AA92B8  49 D1 E9                        shr r9, 1
00AA92BB  48 D1 EA                        shr rdx, 1
00AA92BE  49 8B CC                        mov rcx, r12
00AA92C1  E8 1A 95 EC FF                  call 0x1409727e0
00AA92C6  33 D2                           xor edx, edx
00AA92C8  85 C0                           test eax, eax
00AA92CA  8B CA                           mov ecx, edx
00AA92CC  0F 9F C1                        setg cl
00AA92CF  E9 62 FF FF FF                  jmp 0x140aa9236
00AA92D4  4D 8B CE                        mov r9, r14
00AA92D7  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA92DC  49 8B D5                        mov rdx, r13
00AA92DF  49 D1 E9                        shr r9, 1
00AA92E2  48 D1 EA                        shr rdx, 1
00AA92E5  49 8B CC                        mov rcx, r12
00AA92E8  E8 F3 94 EC FF                  call 0x1409727e0
00AA92ED  EB 93                           jmp 0x140aa9282
00AA92EF  4D 8B CE                        mov r9, r14
00AA92F2  49 8B D5                        mov rdx, r13
00AA92F5  BB 01 00 00 00                  mov ebx, 1
00AA92FA  49 D1 E9                        shr r9, 1
00AA92FD  48 D1 EA                        shr rdx, 1
00AA9300  49 8B CC                        mov rcx, r12
00AA9303  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
00AA9307  E8 D4 94 EC FF                  call 0x1409727e0
00AA930C  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA9310  45 33 DB                        xor r11d, r11d
00AA9313  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA9317  85 C0                           test eax, eax
00AA9319  74 09                           je 0x140aa9324
00AA931B  8B F3                           mov esi, ebx
00AA931D  8B DF                           mov ebx, edi
00AA931F  E9 6A 08 00 00                  jmp 0x140aa9b8e
00AA9324  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00AA9328  8B DF                           mov ebx, edi
00AA932A  E9 56 08 00 00                  jmp 0x140aa9b85
00AA932F  8D 41 FF                        lea eax, [rcx - 1]
00AA9332  41 3B C1                        cmp eax, r9d
00AA9335  0F 86 C6 00 00 00               jbe 0x140aa9401
00AA933B  83 F9 04                        cmp ecx, 4
00AA933E  0F 85 3E FB FF FF               jne 0x140aa8e82
00AA9344  83 3A 18                        cmp dword ptr [rdx], 0x18
00AA9347  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00AA934B  44 8B 00                        mov r8d, dword ptr [rax]
00AA934E  0F 85 2E FB FF FF               jne 0x140aa8e82
00AA9354  4C 8B 73 28                     mov r14, qword ptr [rbx + 0x28]
00AA9358  45 8B FB                        mov r15d, r11d
00AA935B  8B DF                           mov ebx, edi
00AA935D  41 8B CB                        mov ecx, r11d
00AA9360  EB 28                           jmp 0x140aa938a
00AA9362  49 83 CF FF                     or r15, 0xffffffffffffffff
00AA9366  49 FF C7                        inc r15
00AA9369  66 47 39 1C 7E                  cmp word ptr [r14 + r15*2], r11w
00AA936E  75 F6                           jne 0x140aa9366
00AA9370  46 8D 3C 7D 02 00 00 00         lea r15d, [r15*2 + 2]
00AA9378  41 3B C8                        cmp ecx, r8d
00AA937B  74 18                           je 0x140aa9395
00AA937D  41 8B C7                        mov eax, r15d
00AA9380  48 D1 E8                        shr rax, 1
00AA9383  41 03 C9                        add ecx, r9d
00AA9386  4D 8D 34 46                     lea r14, [r14 + rax*2]
00AA938A  66 45 39 1E                     cmp word ptr [r14], r11w
00AA938E  75 D2                           jne 0x140aa9362
00AA9390  41 3B C8                        cmp ecx, r8d
00AA9393  75 5C                           jne 0x140aa93f1
00AA9395  66 45 39 1E                     cmp word ptr [r14], r11w
00AA9399  74 56                           je 0x140aa93f1
00AA939B  BA 02 00 00 00                  mov edx, 2
00AA93A0  44 3B FA                        cmp r15d, edx
00AA93A3  76 4C                           jbe 0x140aa93f1
00AA93A5  41 0F B7 D7                     movzx edx, r15w
00AA93A9  B9 00 01 00 00                  mov ecx, 0x100
00AA93AE  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA93B4  8D 42 F0                        lea eax, [rdx - 0x10]
00AA93B7  66 89 45 A7                     mov word ptr [rbp - 0x59], ax
00AA93BB  0F B7 C2                        movzx eax, dx
00AA93BE  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00AA93C2  E8 29 8D 0D 00                  call 0x140b820f0
00AA93C7  45 33 DB                        xor r11d, r11d
00AA93CA  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA93CE  48 85 C0                        test rax, rax
00AA93D1  0F 84 4D 09 00 00               je 0x140aa9d24
00AA93D7  45 8B C7                        mov r8d, r15d
00AA93DA  49 8B D6                        mov rdx, r14
00AA93DD  48 8B C8                        mov rcx, rax
00AA93E0  E8 5B D4 C1 FF                  call 0x1406c6840
00AA93E5  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA93E9  45 33 DB                        xor r11d, r11d
00AA93EC  E9 51 FD FF FF                  jmp 0x140aa9142
00AA93F1  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA93F5  4C 8D 2D B4 1A 0A 00            lea r13, [rip + 0xa1ab4]
00AA93FC  E9 49 FD FF FF                  jmp 0x140aa914a
00AA9401  44 8B 73 24                     mov r14d, dword ptr [rbx + 0x24]
00AA9405  4D 8B 47 28                     mov r8, qword ptr [r15 + 0x28]
00AA9409  4C 8B 6B 28                     mov r13, qword ptr [rbx + 0x28]
00AA940D  45 8B 67 24                     mov r12d, dword ptr [r15 + 0x24]
00AA9411  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
00AA9415  41 81 FE FE FF 00 00            cmp r14d, 0xfffe
00AA941C  0F 87 0C 09 00 00               ja 0x140aa9d2e
00AA9422  41 81 FC FE FF 00 00            cmp r12d, 0xfffe
00AA9429  0F 87 FF 08 00 00               ja 0x140aa9d2e
00AA942F  8B 0A                           mov ecx, dword ptr [rdx]
00AA9431  83 E9 01                        sub ecx, 1
00AA9434  0F 84 CF 00 00 00               je 0x140aa9509
00AA943A  83 E9 01                        sub ecx, 1
00AA943D  74 4B                           je 0x140aa948a
00AA943F  83 E9 06                        sub ecx, 6
00AA9442  74 28                           je 0x140aa946c
00AA9444  83 F9 01                        cmp ecx, 1
00AA9447  0F 85 35 FA FF FF               jne 0x140aa8e82
00AA944D  49 8B D0                        mov rdx, r8
00AA9450  49 8B CD                        mov rcx, r13
00AA9453  E8 E8 92 A1 FF                  call 0x1404c2740
00AA9458  45 33 DB                        xor r11d, r11d
00AA945B  48 85 C0                        test rax, rax
00AA945E  0F 84 A5 00 00 00               je 0x140aa9509
00AA9464  4C 8B EB                        mov r13, rbx
00AA9467  E9 20 01 00 00                  jmp 0x140aa958c
00AA946C  49 8B D0                        mov rdx, r8
00AA946F  49 8B CD                        mov rcx, r13
00AA9472  E8 C9 92 A1 FF                  call 0x1404c2740
00AA9477  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00AA947B  45 33 DB                        xor r11d, r11d
00AA947E  48 85 C0                        test rax, rax
00AA9481  4D 0F 45 EF                     cmovne r13, r15
00AA9485  E9 02 01 00 00                  jmp 0x140aa958c
00AA948A  49 8B D0                        mov rdx, r8
00AA948D  49 8B CD                        mov rcx, r13
00AA9490  E8 AB 92 A1 FF                  call 0x1404c2740
00AA9495  45 33 DB                        xor r11d, r11d
00AA9498  4C 8B F8                        mov r15, rax
00AA949B  48 85 C0                        test rax, rax
00AA949E  0F 84 1C 04 00 00               je 0x140aa98c0
00AA94A4  41 0F B7 CE                     movzx ecx, r14w
00AA94A8  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA94AE  66 41 2B CC                     sub cx, r12w
00AA94B2  0F B7 D1                        movzx edx, cx
00AA94B5  B9 00 01 00 00                  mov ecx, 0x100
00AA94BA  66 89 55 A7                     mov word ptr [rbp - 0x59], dx
00AA94BE  E8 2D 8C 0D 00                  call 0x140b820f0
00AA94C3  45 33 DB                        xor r11d, r11d
00AA94C6  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA94CA  48 85 C0                        test rax, rax
00AA94CD  0F 84 51 08 00 00               je 0x140aa9d24
00AA94D3  49 8B DF                        mov rbx, r15
00AA94D6  49 2B DD                        sub rbx, r13
00AA94D9  48 D1 FB                        sar rbx, 1
00AA94DC  48 85 DB                        test rbx, rbx
00AA94DF  7E 12                           jle 0x140aa94f3
00AA94E1  4C 8B C3                        mov r8, rbx
00AA94E4  49 8B D5                        mov rdx, r13
00AA94E7  48 8B C8                        mov rcx, rax
00AA94EA  E8 51 D3 C1 FF                  call 0x1406c6840
00AA94EF  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00AA94F3  45 2B F4                        sub r14d, r12d
00AA94F6  4B 8D 14 27                     lea rdx, [r15 + r12]
00AA94FA  45 8B C6                        mov r8d, r14d
00AA94FD  48 8D 0C 18                     lea rcx, [rax + rbx]
00AA9501  4C 2B C3                        sub r8, rbx
00AA9504  E9 87 03 00 00                  jmp 0x140aa9890
00AA9509  43 8D 04 34                     lea eax, [r12 + r14]
00AA950D  3D FE FF 00 00                  cmp eax, 0xfffe
00AA9512  0F 87 16 08 00 00               ja 0x140aa9d2e
00AA9518  43 8D 04 34                     lea eax, [r12 + r14]
00AA951C  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA9522  44 0F B7 F8                     movzx r15d, ax
00AA9526  B9 00 01 00 00                  mov ecx, 0x100
00AA952B  41 0F B7 C7                     movzx eax, r15w
00AA952F  41 8B D7                        mov edx, r15d
00AA9532  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00AA9535  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00AA9539  E8 B2 8B 0D 00                  call 0x140b820f0
00AA953E  45 33 DB                        xor r11d, r11d
00AA9541  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA9545  48 85 C0                        test rax, rax
00AA9548  0F 84 D6 07 00 00               je 0x140aa9d24
00AA954E  4D 8D 46 FE                     lea r8, [r14 - 2]
00AA9552  49 8B D5                        mov rdx, r13
00AA9555  48 8B C8                        mov rcx, rax
00AA9558  49 8B DE                        mov rbx, r14
00AA955B  E8 E0 D2 C1 FF                  call 0x1406c6840
00AA9560  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00AA9564  4D 8B C4                        mov r8, r12
00AA9567  4C 8B 65 BF                     mov r12, qword ptr [rbp - 0x41]
00AA956B  48 D1 EB                        shr rbx, 1
00AA956E  49 8D 4C 24 FE                  lea rcx, [r12 - 2]
00AA9573  48 8D 0C 59                     lea rcx, [rcx + rbx*2]
00AA9577  E8 C4 D2 C1 FF                  call 0x1406c6840
00AA957C  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00AA9580  49 D1 EF                        shr r15, 1
00AA9583  45 33 DB                        xor r11d, r11d
00AA9586  66 47 89 5C 7C FE               mov word ptr [r12 + r15*2 - 2], r11w
00AA958C  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA9590  8B DF                           mov ebx, edi
00AA9592  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA9596  E9 EA 05 00 00                  jmp 0x140aa9b85
00AA959B  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
00AA959F  83 79 20 04                     cmp dword ptr [rcx + 0x20], 4
00AA95A3  0F 85 F3 01 00 00               jne 0x140aa979c
00AA95A9  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00AA95AD  44 8B 08                        mov r9d, dword ptr [rax]
00AA95B0  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00AA95B4  8B 0A                           mov ecx, dword ptr [rdx]
00AA95B6  44 8B 00                        mov r8d, dword ptr [rax]
00AA95B9  83 F9 0A                        cmp ecx, 0xa
00AA95BC  0F 8F AC 00 00 00               jg 0x140aa966e
00AA95C2  0F 84 A1 00 00 00               je 0x140aa9669
00AA95C8  83 E9 01                        sub ecx, 1
00AA95CB  0F 84 8F 00 00 00               je 0x140aa9660
00AA95D1  83 E9 01                        sub ecx, 1
00AA95D4  74 7F                           je 0x140aa9655
00AA95D6  83 E9 01                        sub ecx, 1
00AA95D9  74 6E                           je 0x140aa9649
00AA95DB  83 E9 01                        sub ecx, 1
00AA95DE  74 4B                           je 0x140aa962b
00AA95E0  83 E9 01                        sub ecx, 1
00AA95E3  74 32                           je 0x140aa9617
00AA95E5  83 E9 01                        sub ecx, 1
00AA95E8  74 25                           je 0x140aa960f
00AA95EA  83 E9 01                        sub ecx, 1
00AA95ED  74 18                           je 0x140aa9607
00AA95EF  83 E9 01                        sub ecx, 1
00AA95F2  74 0E                           je 0x140aa9602
00AA95F4  83 F9 01                        cmp ecx, 1
00AA95F7  0F 85 9D 00 00 00               jne 0x140aa969a
00AA95FD  45 0B C1                        or r8d, r9d
00AA9600  EB 4B                           jmp 0x140aa964d
00AA9602  45 23 C1                        and r8d, r9d
00AA9605  EB 46                           jmp 0x140aa964d
00AA9607  41 8B C8                        mov ecx, r8d
00AA960A  41 D3 E9                        shr r9d, cl
00AA960D  EB 49                           jmp 0x140aa9658
00AA960F  41 8B C8                        mov ecx, r8d
00AA9612  41 D3 E1                        shl r9d, cl
00AA9615  EB 41                           jmp 0x140aa9658
00AA9617  45 85 C0                        test r8d, r8d
00AA961A  74 23                           je 0x140aa963f
00AA961C  33 D2                           xor edx, edx
00AA961E  41 8B C1                        mov eax, r9d
00AA9621  41 F7 F0                        div r8d
00AA9624  8B F2                           mov esi, edx
00AA9626  E9 D0 F8 FF FF                  jmp 0x140aa8efb
00AA962B  45 85 C0                        test r8d, r8d
00AA962E  74 0F                           je 0x140aa963f
00AA9630  33 D2                           xor edx, edx
00AA9632  41 8B C1                        mov eax, r9d
00AA9635  41 F7 F0                        div r8d
00AA9638  8B F0                           mov esi, eax
00AA963A  E9 BC F8 FF FF                  jmp 0x140aa8efb
00AA963F  BB 94 00 00 C0                  mov ebx, 0xc0000094
00AA9644  E9 0F F8 FF FF                  jmp 0x140aa8e58
00AA9649  45 0F AF C1                     imul r8d, r9d
00AA964D  41 8B F0                        mov esi, r8d
00AA9650  E9 A6 F8 FF FF                  jmp 0x140aa8efb
00AA9655  45 2B C8                        sub r9d, r8d
00AA9658  41 8B F1                        mov esi, r9d
00AA965B  E9 9B F8 FF FF                  jmp 0x140aa8efb
00AA9660  43 8D 34 08                     lea esi, [r8 + r9]
00AA9664  E9 92 F8 FF FF                  jmp 0x140aa8efb
00AA9669  45 33 C1                        xor r8d, r9d
00AA966C  EB DF                           jmp 0x140aa964d
00AA966E  83 E9 0D                        sub ecx, 0xd
00AA9671  0F 84 92 00 00 00               je 0x140aa9709
00AA9677  83 E9 01                        sub ecx, 1
00AA967A  74 7D                           je 0x140aa96f9
00AA967C  83 E9 01                        sub ecx, 1
00AA967F  74 6A                           je 0x140aa96eb
00AA9681  83 E9 01                        sub ecx, 1
00AA9684  74 57                           je 0x140aa96dd
00AA9686  83 E9 01                        sub ecx, 1
00AA9689  74 44                           je 0x140aa96cf
00AA968B  83 E9 01                        sub ecx, 1
00AA968E  74 31                           je 0x140aa96c1
00AA9690  83 E9 01                        sub ecx, 1
00AA9693  74 1E                           je 0x140aa96b3
00AA9695  83 F9 01                        cmp ecx, 1
00AA9698  74 0E                           je 0x140aa96a8
00AA969A  4C 8D 2D 0F 18 0A 00            lea r13, [rip + 0xa180f]
00AA96A1  8B DF                           mov ebx, edi
00AA96A3  E9 A2 05 00 00                  jmp 0x140aa9c4a
00AA96A8  45 3B C8                        cmp r9d, r8d
00AA96AB  41 8B C3                        mov eax, r11d
00AA96AE  0F 93 C0                        setae al
00AA96B1  EB 85                           jmp 0x140aa9638
00AA96B3  45 3B C8                        cmp r9d, r8d
00AA96B6  41 8B C3                        mov eax, r11d
00AA96B9  0F 96 C0                        setbe al
00AA96BC  E9 77 FF FF FF                  jmp 0x140aa9638
00AA96C1  45 3B C8                        cmp r9d, r8d
00AA96C4  41 8B C3                        mov eax, r11d
00AA96C7  0F 97 C0                        seta al
00AA96CA  E9 69 FF FF FF                  jmp 0x140aa9638
00AA96CF  45 3B C8                        cmp r9d, r8d
00AA96D2  41 8B C3                        mov eax, r11d
00AA96D5  0F 92 C0                        setb al
00AA96D8  E9 5B FF FF FF                  jmp 0x140aa9638
00AA96DD  45 3B C8                        cmp r9d, r8d
00AA96E0  41 8B C3                        mov eax, r11d
00AA96E3  0F 95 C0                        setne al
00AA96E6  E9 4D FF FF FF                  jmp 0x140aa9638
00AA96EB  45 3B C8                        cmp r9d, r8d
00AA96EE  41 8B C3                        mov eax, r11d
00AA96F1  0F 94 C0                        sete al
00AA96F4  E9 3F FF FF FF                  jmp 0x140aa9638
00AA96F9  45 85 C9                        test r9d, r9d
00AA96FC  75 1D                           jne 0x140aa971b
00AA96FE  45 85 C0                        test r8d, r8d
00AA9701  0F 84 F4 F7 FF FF               je 0x140aa8efb
00AA9707  EB 12                           jmp 0x140aa971b
00AA9709  45 85 C9                        test r9d, r9d
00AA970C  0F 84 FC F7 FF FF               je 0x140aa8f0e
00AA9712  45 85 C0                        test r8d, r8d
00AA9715  0F 84 F3 F7 FF FF               je 0x140aa8f0e
00AA971B  BE 01 00 00 00                  mov esi, 1
00AA9720  E9 D6 F7 FF FF                  jmp 0x140aa8efb
00AA9725  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00AA9729  83 78 20 03                     cmp dword ptr [rax + 0x20], 3
00AA972D  75 6D                           jne 0x140aa979c
00AA972F  8B 0A                           mov ecx, dword ptr [rdx]
00AA9731  4C 8B 53 28                     mov r10, qword ptr [rbx + 0x28]
00AA9735  44 8B 43 24                     mov r8d, dword ptr [rbx + 0x24]
00AA9739  4C 8B 58 28                     mov r11, qword ptr [rax + 0x28]
00AA973D  44 8B 48 24                     mov r9d, dword ptr [rax + 0x24]
00AA9741  83 E9 0F                        sub ecx, 0xf
00AA9744  74 37                           je 0x140aa977d
00AA9746  83 F9 01                        cmp ecx, 1
00AA9749  74 09                           je 0x140aa9754
00AA974B  4C 8D 2D 5E 17 0A 00            lea r13, [rip + 0xa175e]
00AA9752  EB 54                           jmp 0x140aa97a8
00AA9754  45 3B C1                        cmp r8d, r9d
00AA9757  75 17                           jne 0x140aa9770
00AA9759  49 8B D3                        mov rdx, r11
00AA975C  49 8B CA                        mov rcx, r10
00AA975F  E8 AC D3 C1 FF                  call 0x1406c6b10
00AA9764  45 33 DB                        xor r11d, r11d
00AA9767  85 C0                           test eax, eax
00AA9769  75 08                           jne 0x140aa9773
00AA976B  41 8B F3                        mov esi, r11d
00AA976E  EB 08                           jmp 0x140aa9778
00AA9770  45 33 DB                        xor r11d, r11d
00AA9773  BE 01 00 00 00                  mov esi, 1
00AA9778  4D 8B EF                        mov r13, r15
00AA977B  EB 2E                           jmp 0x140aa97ab
00AA977D  45 3B C1                        cmp r8d, r9d
00AA9780  75 23                           jne 0x140aa97a5
00AA9782  49 8B D3                        mov rdx, r11
00AA9785  49 8B CA                        mov rcx, r10
00AA9788  E8 83 D3 C1 FF                  call 0x1406c6b10
00AA978D  45 33 DB                        xor r11d, r11d
00AA9790  4D 8B EF                        mov r13, r15
00AA9793  85 C0                           test eax, eax
00AA9795  75 14                           jne 0x140aa97ab
00AA9797  8D 70 01                        lea esi, [rax + 1]
00AA979A  EB 0F                           jmp 0x140aa97ab
00AA979C  4C 8D 2D 0D 17 0A 00            lea r13, [rip + 0xa170d]
00AA97A3  EB 06                           jmp 0x140aa97ab
00AA97A5  4D 8B EF                        mov r13, r15
00AA97A8  45 33 DB                        xor r11d, r11d
00AA97AB  8B DF                           mov ebx, edi
00AA97AD  E9 D3 03 00 00                  jmp 0x140aa9b85
00AA97B2  4C 8B 6D 07                     mov r13, qword ptr [rbp + 7]
00AA97B6  41 8B 4D 20                     mov ecx, dword ptr [r13 + 0x20]
00AA97BA  8D 41 FF                        lea eax, [rcx - 1]
00AA97BD  41 3B C1                        cmp eax, r9d
00AA97C0  0F 86 FF 00 00 00               jbe 0x140aa98c5
00AA97C6  83 F9 07                        cmp ecx, 7
00AA97C9  75 D1                           jne 0x140aa979c
00AA97CB  44 8B 7B 24                     mov r15d, dword ptr [rbx + 0x24]
00AA97CF  4D 8B 45 28                     mov r8, qword ptr [r13 + 0x28]
00AA97D3  4C 8B 63 28                     mov r12, qword ptr [rbx + 0x28]
00AA97D7  45 8B 75 24                     mov r14d, dword ptr [r13 + 0x24]
00AA97DB  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
00AA97DF  41 81 FF FE FF 00 00            cmp r15d, 0xfffe
00AA97E6  0F 87 42 05 00 00               ja 0x140aa9d2e
00AA97EC  41 81 FE FE FF 00 00            cmp r14d, 0xfffe
00AA97F3  0F 87 35 05 00 00               ja 0x140aa9d2e
00AA97F9  8B 0A                           mov ecx, dword ptr [rdx]
00AA97FB  83 E9 01                        sub ecx, 1
00AA97FE  74 2D                           je 0x140aa982d
00AA9800  83 E9 07                        sub ecx, 7
00AA9803  0F 84 A4 00 00 00               je 0x140aa98ad
00AA9809  83 F9 01                        cmp ecx, 1
00AA980C  74 0C                           je 0x140aa981a
00AA980E  4C 8D 2D 9B 16 0A 00            lea r13, [rip + 0xa169b]
00AA9815  E9 82 00 00 00                  jmp 0x140aa989c
00AA981A  49 8B D4                        mov rdx, r12
00AA981D  49 8B C8                        mov rcx, r8
00AA9820  E8 1B 8F A1 FF                  call 0x1404c2740
00AA9825  45 33 DB                        xor r11d, r11d
00AA9828  48 85 C0                        test rax, rax
00AA982B  75 6F                           jne 0x140aa989c
00AA982D  43 8D 04 3E                     lea eax, [r14 + r15]
00AA9831  3D FE FF 00 00                  cmp eax, 0xfffe
00AA9836  0F 87 F2 04 00 00               ja 0x140aa9d2e
00AA983C  43 8D 04 3E                     lea eax, [r14 + r15]
00AA9840  B9 00 01 00 00                  mov ecx, 0x100
00AA9845  0F B7 D0                        movzx edx, ax
00AA9848  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA984E  66 89 55 A7                     mov word ptr [rbp - 0x59], dx
00AA9852  E8 99 88 0D 00                  call 0x140b820f0
00AA9857  45 33 DB                        xor r11d, r11d
00AA985A  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA985E  4C 8B E8                        mov r13, rax
00AA9861  48 85 C0                        test rax, rax
00AA9864  0F 84 BA 04 00 00               je 0x140aa9d24
00AA986A  4D 8B C7                        mov r8, r15
00AA986D  49 8B D4                        mov rdx, r12
00AA9870  48 8B C8                        mov rcx, rax
00AA9873  49 8B DF                        mov rbx, r15
00AA9876  E8 C5 CF C1 FF                  call 0x1406c6840
00AA987B  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00AA987F  48 D1 EB                        shr rbx, 1
00AA9882  48 8D 0C 5D 00 00 00 00         lea rcx, [rbx*2]
00AA988A  49 03 CD                        add rcx, r13
00AA988D  4D 8B C6                        mov r8, r14
00AA9890  E8 AB CF C1 FF                  call 0x1406c6840
00AA9895  45 33 DB                        xor r11d, r11d
00AA9898  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00AA989C  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA98A0  45 0F B7 F4                     movzx r14d, r12w
00AA98A4  4C 89 75 AF                     mov qword ptr [rbp - 0x51], r14
00AA98A8  E9 FE FE FF FF                  jmp 0x140aa97ab
00AA98AD  49 8B D4                        mov rdx, r12
00AA98B0  49 8B C8                        mov rcx, r8
00AA98B3  E8 88 8E A1 FF                  call 0x1404c2740
00AA98B8  45 33 DB                        xor r11d, r11d
00AA98BB  48 85 C0                        test rax, rax
00AA98BE  74 D8                           je 0x140aa9898
00AA98C0  4C 8B EB                        mov r13, rbx
00AA98C3  EB D7                           jmp 0x140aa989c
00AA98C5  81 7B 24 FE FF 00 00            cmp dword ptr [rbx + 0x24], 0xfffe
00AA98CC  0F 87 56 02 00 00               ja 0x140aa9b28
00AA98D2  41 81 7D 24 FE FF 00 00         cmp dword ptr [r13 + 0x24], 0xfffe
00AA98DA  0F 87 48 02 00 00               ja 0x140aa9b28
00AA98E0  44 0F B7 43 24                  movzx r8d, word ptr [rbx + 0x24]
00AA98E5  B8 02 00 00 00                  mov eax, 2
00AA98EA  45 0F B7 75 24                  movzx r14d, word ptr [r13 + 0x24]
00AA98EF  45 0F B7 F8                     movzx r15d, r8w
00AA98F3  8B 0A                           mov ecx, dword ptr [rdx]
00AA98F5  66 44 2B F8                     sub r15w, ax
00AA98F9  4C 8B 53 28                     mov r10, qword ptr [rbx + 0x28]
00AA98FD  66 44 2B F0                     sub r14w, ax
00AA9901  4D 8B 65 28                     mov r12, qword ptr [r13 + 0x28]
00AA9905  4C 89 55 CF                     mov qword ptr [rbp - 0x31], r10
00AA9909  83 E9 01                        sub ecx, 1
00AA990C  0F 84 68 01 00 00               je 0x140aa9a7a
00AA9912  83 E9 0C                        sub ecx, 0xc
00AA9915  0F 84 57 01 00 00               je 0x140aa9a72
00AA991B  83 E9 01                        sub ecx, 1
00AA991E  0F 84 37 01 00 00               je 0x140aa9a5b
00AA9924  83 E9 01                        sub ecx, 1
00AA9927  0F 84 00 01 00 00               je 0x140aa9a2d
00AA992D  83 E9 01                        sub ecx, 1
00AA9930  0F 84 CC 00 00 00               je 0x140aa9a02
00AA9936  83 E9 01                        sub ecx, 1
00AA9939  0F 84 A0 00 00 00               je 0x140aa99df
00AA993F  83 E9 01                        sub ecx, 1
00AA9942  74 70                           je 0x140aa99b4
00AA9944  83 E9 01                        sub ecx, 1
00AA9947  74 3B                           je 0x140aa9984
00AA9949  83 F9 01                        cmp ecx, 1
00AA994C  74 0C                           je 0x140aa995a
00AA994E  4C 8D 2D 5B 15 0A 00            lea r13, [rip + 0xa155b]
00AA9955  E9 C1 01 00 00                  jmp 0x140aa9b1b
00AA995A  45 0F B7 CE                     movzx r9d, r14w
00AA995E  4D 8B C4                        mov r8, r12
00AA9961  41 0F B7 D7                     movzx edx, r15w
00AA9965  49 8B CA                        mov rcx, r10
00AA9968  49 D1 E9                        shr r9, 1
00AA996B  48 D1 EA                        shr rdx, 1
00AA996E  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA9973  E8 68 8E EC FF                  call 0x1409727e0
00AA9978  F7 D0                           not eax
00AA997A  C1 E8 1F                        shr eax, 0x1f
00AA997D  8B F0                           mov esi, eax
00AA997F  E9 90 01 00 00                  jmp 0x140aa9b14
00AA9984  45 0F B7 CE                     movzx r9d, r14w
00AA9988  4D 8B C4                        mov r8, r12
00AA998B  41 0F B7 D7                     movzx edx, r15w
00AA998F  49 8B CA                        mov rcx, r10
00AA9992  49 D1 E9                        shr r9, 1
00AA9995  48 D1 EA                        shr rdx, 1
00AA9998  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA999D  E8 3E 8E EC FF                  call 0x1409727e0
00AA99A2  45 33 DB                        xor r11d, r11d
00AA99A5  85 C0                           test eax, eax
00AA99A7  41 8B CB                        mov ecx, r11d
00AA99AA  0F 9E C1                        setle cl
00AA99AD  8B F1                           mov esi, ecx
00AA99AF  E9 63 01 00 00                  jmp 0x140aa9b17
00AA99B4  45 0F B7 CE                     movzx r9d, r14w
00AA99B8  4D 8B C4                        mov r8, r12
00AA99BB  41 0F B7 D7                     movzx edx, r15w
00AA99BF  49 8B CA                        mov rcx, r10
00AA99C2  49 D1 E9                        shr r9, 1
00AA99C5  48 D1 EA                        shr rdx, 1
00AA99C8  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA99CD  E8 0E 8E EC FF                  call 0x1409727e0
00AA99D2  45 33 DB                        xor r11d, r11d
00AA99D5  85 C0                           test eax, eax
00AA99D7  41 8B CB                        mov ecx, r11d
00AA99DA  0F 9F C1                        setg cl
00AA99DD  EB CE                           jmp 0x140aa99ad
00AA99DF  45 0F B7 CE                     movzx r9d, r14w
00AA99E3  4D 8B C4                        mov r8, r12
00AA99E6  41 0F B7 D7                     movzx edx, r15w
00AA99EA  49 8B CA                        mov rcx, r10
00AA99ED  49 D1 E9                        shr r9, 1
00AA99F0  48 D1 EA                        shr rdx, 1
00AA99F3  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA99F8  E8 E3 8D EC FF                  call 0x1409727e0
00AA99FD  E9 78 FF FF FF                  jmp 0x140aa997a
00AA9A02  45 0F B7 CE                     movzx r9d, r14w
00AA9A06  4D 8B C4                        mov r8, r12
00AA9A09  41 0F B7 D7                     movzx edx, r15w
00AA9A0D  49 8B CA                        mov rcx, r10
00AA9A10  49 D1 E9                        shr r9, 1
00AA9A13  48 D1 EA                        shr rdx, 1
00AA9A16  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA9A1B  E8 C0 8D EC FF                  call 0x1409727e0
00AA9A20  45 33 DB                        xor r11d, r11d
00AA9A23  85 C0                           test eax, eax
00AA9A25  41 8B CB                        mov ecx, r11d
00AA9A28  0F 95 C1                        setne cl
00AA9A2B  EB 80                           jmp 0x140aa99ad
00AA9A2D  45 0F B7 CE                     movzx r9d, r14w
00AA9A31  4D 8B C4                        mov r8, r12
00AA9A34  41 0F B7 D7                     movzx edx, r15w
00AA9A38  49 8B CA                        mov rcx, r10
00AA9A3B  49 D1 E9                        shr r9, 1
00AA9A3E  48 D1 EA                        shr rdx, 1
00AA9A41  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AA9A46  E8 95 8D EC FF                  call 0x1409727e0
00AA9A4B  45 33 DB                        xor r11d, r11d
00AA9A4E  85 C0                           test eax, eax
00AA9A50  41 8B CB                        mov ecx, r11d
00AA9A53  0F 94 C1                        sete cl
00AA9A56  E9 52 FF FF FF                  jmp 0x140aa99ad
00AA9A5B  66 44 3B F8                     cmp r15w, ax
00AA9A5F  73 06                           jae 0x140aa9a67
00AA9A61  66 44 3B F0                     cmp r14w, ax
00AA9A65  72 03                           jb 0x140aa9a6a
00AA9A67  41 8B F1                        mov esi, r9d
00AA9A6A  4D 8B EB                        mov r13, r11
00AA9A6D  E9 A9 00 00 00                  jmp 0x140aa9b1b
00AA9A72  66 44 3B F8                     cmp r15w, ax
00AA9A76  72 F2                           jb 0x140aa9a6a
00AA9A78  EB E7                           jmp 0x140aa9a61
00AA9A7A  66 45 39 1A                     cmp word ptr [r10], r11w
00AA9A7E  0F 84 97 00 00 00               je 0x140aa9b1b
00AA9A84  66 45 39 1C 24                  cmp word ptr [r12], r11w
00AA9A89  75 08                           jne 0x140aa9a93
00AA9A8B  4C 8B EB                        mov r13, rbx
00AA9A8E  E9 88 00 00 00                  jmp 0x140aa9b1b
00AA9A93  41 0F B7 CE                     movzx ecx, r14w
00AA9A97  41 0F B7 C7                     movzx eax, r15w
00AA9A9B  03 C8                           add ecx, eax
00AA9A9D  81 F9 FE FF 00 00               cmp ecx, 0xfffe
00AA9AA3  0F 83 85 02 00 00               jae 0x140aa9d2e
00AA9AA9  43 8D 04 37                     lea eax, [r15 + r14]
00AA9AAD  66 45 03 C6                     add r8w, r14w
00AA9AB1  41 0F B7 D0                     movzx edx, r8w
00AA9AB5  B9 00 01 00 00                  mov ecx, 0x100
00AA9ABA  66 89 45 A7                     mov word ptr [rbp - 0x59], ax
00AA9ABE  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA9AC4  0F B7 C2                        movzx eax, dx
00AA9AC7  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00AA9ACB  E8 20 86 0D 00                  call 0x140b820f0
00AA9AD0  45 33 DB                        xor r11d, r11d
00AA9AD3  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AA9AD7  4C 8B E8                        mov r13, rax
00AA9ADA  48 85 C0                        test rax, rax
00AA9ADD  0F 84 41 02 00 00               je 0x140aa9d24
00AA9AE3  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00AA9AE7  48 8B C8                        mov rcx, rax
00AA9AEA  41 0F B7 DF                     movzx ebx, r15w
00AA9AEE  44 8B C3                        mov r8d, ebx
00AA9AF1  E8 4A CD C1 FF                  call 0x1406c6840
00AA9AF6  48 D1 EB                        shr rbx, 1
00AA9AF9  49 8B D4                        mov rdx, r12
00AA9AFC  45 0F B7 C6                     movzx r8d, r14w
00AA9B00  49 83 C0 02                     add r8, 2
00AA9B04  48 8D 0C 5D 00 00 00 00         lea rcx, [rbx*2]
00AA9B0C  49 03 CD                        add rcx, r13
00AA9B0F  E8 2C CD C1 FF                  call 0x1406c6840
00AA9B14  45 33 DB                        xor r11d, r11d
00AA9B17  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00AA9B1B  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00AA9B1F  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00AA9B23  E9 83 FC FF FF                  jmp 0x140aa97ab
00AA9B28  BB 05 00 00 80                  mov ebx, 0x80000005
00AA9B2D  E9 26 F3 FF FF                  jmp 0x140aa8e58
00AA9B32  41 83 FA 03                     cmp r10d, 3
00AA9B36  75 5A                           jne 0x140aa9b92
00AA9B38  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00AA9B3C  8B 51 20                        mov edx, dword ptr [rcx + 0x20]
00AA9B3F  8B C2                           mov eax, edx
00AA9B41  83 E8 01                        sub eax, 1
00AA9B44  0F 84 AD 00 00 00               je 0x140aa9bf7
00AA9B4A  83 E8 01                        sub eax, 1
00AA9B4D  0F 84 A4 00 00 00               je 0x140aa9bf7
00AA9B53  83 E8 01                        sub eax, 1
00AA9B56  0F 84 81 00 00 00               je 0x140aa9bdd
00AA9B5C  83 E8 01                        sub eax, 1
00AA9B5F  74 12                           je 0x140aa9b73
00AA9B61  41 3B C2                        cmp eax, r10d
00AA9B64  74 04                           je 0x140aa9b6a
00AA9B66  85 D2                           test edx, edx
00AA9B68  EB 10                           jmp 0x140aa9b7a
00AA9B6A  83 79 24 04                     cmp dword ptr [rcx + 0x24], 4
00AA9B6E  0F 97 C0                        seta al
00AA9B71  EB 0A                           jmp 0x140aa9b7d
00AA9B73  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00AA9B77  44 39 18                        cmp dword ptr [rax], r11d
00AA9B7A  0F 95 C0                        setne al
00AA9B7D  84 C0                           test al, al
00AA9B7F  75 7C                           jne 0x140aa9bfd
00AA9B81  4C 8B 6D 07                     mov r13, qword ptr [rbp + 7]
00AA9B85  4D 85 ED                        test r13, r13
00AA9B88  0F 85 B8 00 00 00               jne 0x140aa9c46
00AA9B8E  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
00AA9B92  BA 30 00 00 00                  mov edx, 0x30
00AA9B97  B9 00 01 00 00                  mov ecx, 0x100
00AA9B9C  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA9BA2  E8 49 85 0D 00                  call 0x140b820f0
00AA9BA7  45 33 DB                        xor r11d, r11d
00AA9BAA  4C 8B E8                        mov r13, rax
00AA9BAD  48 85 C0                        test rax, rax
00AA9BB0  0F 84 7F 01 00 00               je 0x140aa9d35
00AA9BB6  44 89 58 10                     mov dword ptr [rax + 0x10], r11d
00AA9BBA  4C 89 58 18                     mov qword ptr [rax + 0x18], r11
00AA9BBE  4D 85 FF                        test r15, r15
00AA9BC1  74 40                           je 0x140aa9c03
00AA9BC3  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00AA9BC7  41 8D 7B 07                     lea edi, [r11 + 7]
00AA9BCB  66 44 3B E0                     cmp r12w, ax
00AA9BCF  45 0F B7 F6                     movzx r14d, r14w
00AA9BD3  45 8D 4B 01                     lea r9d, [r11 + 1]
00AA9BD7  41 0F 45 F9                     cmovne edi, r9d
00AA9BDB  EB 57                           jmp 0x140aa9c34
00AA9BDD  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
00AA9BE1  8B 51 24                        mov edx, dword ptr [rcx + 0x24]
00AA9BE4  85 D2                           test edx, edx
00AA9BE6  74 99                           je 0x140aa9b81
00AA9BE8  41 8A 00                        mov al, byte ptr [r8]
00AA9BEB  4D 03 C1                        add r8, r9
00AA9BEE  84 C0                           test al, al
00AA9BF0  75 0B                           jne 0x140aa9bfd
00AA9BF2  41 03 D5                        add edx, r13d
00AA9BF5  EB ED                           jmp 0x140aa9be4
00AA9BF7  44 39 41 24                     cmp dword ptr [rcx + 0x24], r8d
00AA9BFB  72 84                           jb 0x140aa9b81
00AA9BFD  4C 8B 6D 0F                     mov r13, qword ptr [rbp + 0xf]
00AA9C01  EB 82                           jmp 0x140aa9b85
00AA9C03  B8 04 00 00 00                  mov eax, 4
00AA9C08  41 B8 50 70 64 63               mov r8d, 0x63647050
00AA9C0E  8B D0                           mov edx, eax
00AA9C10  B9 00 01 00 00                  mov ecx, 0x100
00AA9C15  8B F8                           mov edi, eax
00AA9C17  44 8B F0                        mov r14d, eax
00AA9C1A  E8 D1 84 0D 00                  call 0x140b820f0
00AA9C1F  45 33 DB                        xor r11d, r11d
00AA9C22  4C 8B F8                        mov r15, rax
00AA9C25  48 85 C0                        test rax, rax
00AA9C28  0F 84 07 01 00 00               je 0x140aa9d35
00AA9C2E  89 30                           mov dword ptr [rax], esi
00AA9C30  45 8D 4B 01                     lea r9d, [r11 + 1]
00AA9C34  44 8B 55 AB                     mov r10d, dword ptr [rbp - 0x55]
00AA9C38  41 89 7D 20                     mov dword ptr [r13 + 0x20], edi
00AA9C3C  45 89 75 24                     mov dword ptr [r13 + 0x24], r14d
00AA9C40  4D 89 7D 28                     mov qword ptr [r13 + 0x28], r15
00AA9C44  EB 0A                           jmp 0x140aa9c50
00AA9C46  44 8B 55 AB                     mov r10d, dword ptr [rbp - 0x55]
00AA9C4A  41 B9 01 00 00 00               mov r9d, 1
00AA9C50  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00AA9C54  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA9C58  4F 89 2C F7                     mov qword ptr [r15 + r14*8], r13
00AA9C5C  45 85 D2                        test r10d, r10d
00AA9C5F  74 3E                           je 0x140aa9c9f
00AA9C61  48 8D 75 07                     lea rsi, [rbp + 7]
00AA9C65  45 8B F2                        mov r14d, r10d
00AA9C68  48 8B 3E                        mov rdi, qword ptr [rsi]
00AA9C6B  4C 39 5F 18                     cmp qword ptr [rdi + 0x18], r11
00AA9C6F  75 21                           jne 0x140aa9c92
00AA9C71  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00AA9C75  48 85 C9                        test rcx, rcx
00AA9C78  74 07                           je 0x140aa9c81
00AA9C7A  33 D2                           xor edx, edx
00AA9C7C  E8 EF 8B 0D 00                  call 0x140b82870
00AA9C81  33 D2                           xor edx, edx
00AA9C83  48 8B CF                        mov rcx, rdi
00AA9C86  E8 E5 8B 0D 00                  call 0x140b82870
00AA9C8B  45 33 DB                        xor r11d, r11d
00AA9C8E  45 8D 4B 01                     lea r9d, [r11 + 1]
00AA9C92  48 83 C6 08                     add rsi, 8
00AA9C96  4D 2B F1                        sub r14, r9
00AA9C99  75 CD                           jne 0x140aa9c68
00AA9C9B  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00AA9C9F  4C 8B 6D EF                     mov r13, qword ptr [rbp - 0x11]
00AA9CA3  44 8B 65 E7                     mov r12d, dword ptr [rbp - 0x19]
00AA9CA7  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
00AA9CAB  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AA9CAF  48 FF C0                        inc rax
00AA9CB2  66 44 39 1C 46                  cmp word ptr [rsi + rax*2], r11w
00AA9CB7  75 F6                           jne 0x140aa9caf
00AA9CB9  48 8D 34 46                     lea rsi, [rsi + rax*2]
00AA9CBD  41 B9 01 00 00 00               mov r9d, 1
00AA9CC3  48 83 C6 02                     add rsi, 2
00AA9CC7  45 03 F1                        add r14d, r9d
00AA9CCA  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
00AA9CCE  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
00AA9CD2  E9 33 F0 FF FF                  jmp 0x140aa8d0a
00AA9CD7  45 3B F4                        cmp r14d, r12d
00AA9CDA  0F 83 17 01 00 00               jae 0x140aa9df7
00AA9CE0  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00AA9CE4  4C 89 5D DF                     mov qword ptr [rbp - 0x21], r11
00AA9CE8  48 8B D6                        mov rdx, rsi
00AA9CEB  49 8B CD                        mov rcx, r13
00AA9CEE  E8 C5 7D FD FF                  call 0x140a81ab8
00AA9CF3  45 33 DB                        xor r11d, r11d
00AA9CF6  8B D8                           mov ebx, eax
00AA9CF8  85 C0                           test eax, eax
00AA9CFA  0F 88 E9 00 00 00               js 0x140aa9de9
00AA9D00  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00AA9D04  41 8B CE                        mov ecx, r14d
00AA9D07  49 89 04 CF                     mov qword ptr [r15 + rcx*8], rax
00AA9D0B  EB 9E                           jmp 0x140aa9cab
00AA9D0D  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AA9D12  EB 2E                           jmp 0x140aa9d42
00AA9D14  49 8B CF                        mov rcx, r15
00AA9D17  E8 54 8B 0D 00                  call 0x140b82870
00AA9D1C  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00AA9D1F  45 33 DB                        xor r11d, r11d
00AA9D22  EB 25                           jmp 0x140aa9d49
00AA9D24  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AA9D29  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00AA9D2C  EB 1B                           jmp 0x140aa9d49
00AA9D2E  BB 05 00 00 80                  mov ebx, 0x80000005
00AA9D33  EB F4                           jmp 0x140aa9d29
00AA9D35  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AA9D3A  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00AA9D3E  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA9D42  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00AA9D45  85 C0                           test eax, eax
00AA9D47  74 50                           je 0x140aa9d99
00AA9D49  44 8B F0                        mov r14d, eax
00AA9D4C  48 8D 7D 07                     lea rdi, [rbp + 7]
00AA9D50  B8 01 00 00 00                  mov eax, 1
00AA9D55  48 8B 37                        mov rsi, qword ptr [rdi]
00AA9D58  4C 39 5E 18                     cmp qword ptr [rsi + 0x18], r11
00AA9D5C  75 21                           jne 0x140aa9d7f
00AA9D5E  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00AA9D62  48 85 C9                        test rcx, rcx
00AA9D65  74 07                           je 0x140aa9d6e
00AA9D67  33 D2                           xor edx, edx
00AA9D69  E8 02 8B 0D 00                  call 0x140b82870
00AA9D6E  33 D2                           xor edx, edx
00AA9D70  48 8B CE                        mov rcx, rsi
00AA9D73  E8 F8 8A 0D 00                  call 0x140b82870
00AA9D78  45 33 DB                        xor r11d, r11d
00AA9D7B  41 8D 43 01                     lea eax, [r11 + 1]
00AA9D7F  48 83 C7 08                     add rdi, 8
00AA9D83  4C 2B F0                        sub r14, rax
00AA9D86  75 CD                           jne 0x140aa9d55
00AA9D88  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA9D8C  4D 85 FF                        test r15, r15
00AA9D8F  0F 84 8A 00 00 00               je 0x140aa9e1f
00AA9D95  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00AA9D99  45 85 F6                        test r14d, r14d
00AA9D9C  74 3F                           je 0x140aa9ddd
00AA9D9E  49 8B FF                        mov rdi, r15
00AA9DA1  41 8B F6                        mov esi, r14d
00AA9DA4  41 BF 01 00 00 00               mov r15d, 1
00AA9DAA  48 8B 07                        mov rax, qword ptr [rdi]
00AA9DAD  4C 39 58 18                     cmp qword ptr [rax + 0x18], r11
00AA9DB1  75 1D                           jne 0x140aa9dd0
00AA9DB3  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00AA9DB7  48 85 C9                        test rcx, rcx
00AA9DBA  74 07                           je 0x140aa9dc3
00AA9DBC  33 D2                           xor edx, edx
00AA9DBE  E8 AD 8A 0D 00                  call 0x140b82870
00AA9DC3  48 8B 0F                        mov rcx, qword ptr [rdi]
00AA9DC6  33 D2                           xor edx, edx
00AA9DC8  E8 A3 8A 0D 00                  call 0x140b82870
00AA9DCD  45 33 DB                        xor r11d, r11d
00AA9DD0  48 83 C7 08                     add rdi, 8
00AA9DD4  49 2B F7                        sub rsi, r15
00AA9DD7  75 D1                           jne 0x140aa9daa
00AA9DD9  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00AA9DDD  33 D2                           xor edx, edx
00AA9DDF  49 8B CF                        mov rcx, r15
00AA9DE2  E8 89 8A 0D 00                  call 0x140b82870
00AA9DE7  EB 36                           jmp 0x140aa9e1f
00AA9DE9  3D 34 00 00 C0                  cmp eax, 0xc0000034
00AA9DEE  75 A9                           jne 0x140aa9d99
00AA9DF0  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AA9DF5  EB A2                           jmp 0x140aa9d99
00AA9DF7  BB FD 00 00 C0                  mov ebx, 0xc00000fd
00AA9DFC  EB 9B                           jmp 0x140aa9d99
00AA9DFE  85 FF                           test edi, edi
00AA9E00  78 97                           js 0x140aa9d99
00AA9E02  45 3B F1                        cmp r14d, r9d
00AA9E05  75 E9                           jne 0x140aa9df0
00AA9E07  49 8B 17                        mov rdx, qword ptr [r15]
00AA9E0A  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00AA9E0E  E8 E5 89 C8 FF                  call 0x1407327f8
00AA9E13  8B D8                           mov ebx, eax
00AA9E15  45 33 DB                        xor r11d, r11d
00AA9E18  EB 84                           jmp 0x140aa9d9e
00AA9E1A  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AA9E1F  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
00AA9E23  48 85 C0                        test rax, rax
00AA9E26  74 0A                           je 0x140aa9e32
00AA9E28  33 D2                           xor edx, edx
00AA9E2A  48 8B C8                        mov rcx, rax
00AA9E2D  E8 3E 8A 0D 00                  call 0x140b82870
00AA9E32  8B C3                           mov eax, ebx
00AA9E34  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
00AA9E38  48 33 CC                        xor rcx, rsp
00AA9E3B  E8 00 28 C0 FF                  call 0x1406ac640
00AA9E40  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
00AA9E48  48 81 C4 B0 00 00 00            add rsp, 0xb0
00AA9E4F  41 5F                           pop r15
00AA9E51  41 5E                           pop r14
00AA9E53  41 5D                           pop r13
00AA9E55  41 5C                           pop r12
00AA9E57  5F                              pop rdi
00AA9E58  5E                              pop rsi
00AA9E59  5D                              pop rbp
00AA9E5A  C3                              ret
00AA9E5B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgResolveVariableExpression(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 3545885)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m70 = a1;
    a2 = 0;
    v_stack_m60 = a3;
    a1 = 0;
    v_stack_m68 = 0;
    v_stack_m98 = 0;
    v_stack_m48 = 0;
    a3 = 0;
    v_stack_m58 = v_xmm0;
    result = IopGetRegistryValue(0, v_rip + 354588, a3, v_stack_m68);
    v_r11 = 0;
    if (sign_flag) goto loc_00AA9E1F;
    result = PnpValidateRegistryMultiSz(v_stack_m68, v_rip + 354588, a3, v_stack_m68);
    if ((unsigned __int8)(result) == 0) goto loc_00AA9E1A;
    v_rsi = ((unsigned int)(*(unsigned int *)(v_stack_m68 + 8))) + (v_stack_m68);
    v_stack_m80 = v_rsi;
    if ((*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AA9E1A;
loc_00AA8CA4:
    v_r12 = (unsigned int)((0) + ((unsigned int)(v_r11 + 1)));
    a1 = (v_stack_m68) | (-1);
loc_00AA8CAB:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(v_rsi + a1 * 2)) != 0) goto loc_00AA8CAB;
    result = (v_rsi + a1 * 2) + (2);
    if ((*(unsigned __int16 *)(result)) != 0) goto loc_00AA8CA4;
    v_stack_m78 = (unsigned int)(v_r12);
    if ((unsigned int)(v_r12) == 0) goto loc_00AA9E1A;
    a2 = ((unsigned int)((unsigned int)(v_r12))) << (3);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x63647050ULL), v_stack_m68);
    v_r11 = 0;
    v_stack_m88 = result;
    if (result != 0) goto loc_00AA8D04;
    goto loc_00AA9E1F;
loc_00AA8D04:
loc_00AA8D0A:
    if ((*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AA9DFE;
    if ((*(unsigned __int16 *)(v_rsi + 2)) == 0) goto loc_00AA8D2F;
    if ((*(unsigned __int16 *)(v_rsi + 4)) != 0) goto loc_00AA9CD7;
loc_00AA8D2F:
loc_00AA8D32:
    if (1 >= 27) goto loc_00AA9CD7;
    if ((*(unsigned int *)(v_rsi)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 688591 + 1 + 1 * 2 * 8 + 8)))))) goto loc_00AA8D51;
    a2 = (unsigned int)((1) + (1));
    goto loc_00AA8D32;
loc_00AA8D51:
    if (v_rip + 688591 + 1 + 1 * 2 * 8 == 0) goto loc_00AA9CD7;
    v_stack_mB4 = 0;
    v_r13 = (unsigned int)((v_stack_m70) | (0xFFFFFFFFULL));
loc_00AA8D6D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 688591 + 1 + 1 * 2 * 8 + 16))))) goto loc_00AA8D97;
    if (0 == 0) goto loc_00AA9D0D;
    v_r14 = (unsigned int)((0) + ((unsigned int)(v_r13)));
    v_r10 = (unsigned int)((0) + (1));
    v_stack_m98 = (unsigned int)(v_r14);
    v_stack_mB4 = (unsigned int)(v_r10);
    *(unsigned __int64 *)(v_stack_m5F + 0 * 8 + 7) = *(unsigned __int64 *)(result + v_r14 * 8);
    goto loc_00AA8D6D;
loc_00AA8D97:
    if (sign_flag) goto loc_00AA9D42;
    v_stack_m90 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    if (((unsigned int)(v_r10)) != 1) goto loc_00AA8FAB;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 688591 + 1 + 1 * 2 * 8))))) - (22));
    if (condition_is_equal) goto loc_00AA8F95;
    if (((unsigned int)(a2)) == 1) goto loc_00AA8F84;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 32))) - (1));
    if (condition_is_equal) goto loc_00AA8F18;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00AA8F18;
    a2 = (unsigned int)((a2) - (2));
    if (condition_is_equal) goto loc_00AA8E60;
    if (((unsigned int)(a2)) != 3) goto loc_00AA8E18;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 688591 + 1 + 1 * 2 * 8))) - (11));
    if (condition_is_equal) goto loc_00AA8E31;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA8E24;
loc_00AA8E18:
    goto loc_00AA9C50;
loc_00AA8E24:
    v_rsi = ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 40))) == 0) ? 1 : 0;
    goto loc_00AA9B92;
loc_00AA8E31:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 40))) == 0) goto loc_00AA9B92;
loc_00AA8E3B:
    v_rsi = (unsigned int)((v_rsi) + 1);
    result = (*(unsigned __int64 *)(result + v_r14 * 8)) | (-1);
loc_00AA8E41:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 40) + result * 2)) != 0) goto loc_00AA8E41;
    a2 = (*(unsigned __int64 *)(v_stack_m58 + 40) + result * 2) + (v_rip + 663697);
    if ((*(unsigned __int16 *)(a2)) != 0) goto loc_00AA8E3B;
loc_00AA8E58:
    goto loc_00AA914A;
loc_00AA8E60:
    a1 = (unsigned int)((a1) - (11));
    if (condition_is_equal) goto loc_00AA8F0A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA8F02;
    a1 = (unsigned int)((a1) - (13));
    if (condition_is_equal) goto loc_00AA8EF9;
    if (((unsigned int)(a1)) == 1) goto loc_00AA8E90;
loc_00AA8E82:
    goto loc_00AA9C50;
loc_00AA8E90:
    result = ExAllocatePool2(256, 22, (unsigned int)(0x63647050ULL), 1);
    v_r11 = 0;
    if (result == 0) goto loc_00AA9D24;
    result = RtlStringCchPrintfW(result, v_r11 + 11, v_rip + 347106, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))))));
    a2 = 0;
    if (sign_flag) goto loc_00AA9D14;
    v_r14 = (0) | (-1);
loc_00AA8EDA:
    v_r14 = (v_r14) + 1;
    if ((*(unsigned __int16 *)(result + v_r14 * 2)) != 0) goto loc_00AA8EDA;
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(v_r14)));
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(v_rip + 663591)));
    v_stack_mB0 = v_r14;
    goto loc_00AA9B92;
loc_00AA8EF9:
loc_00AA8EFB:
    goto loc_00AA9B92;
loc_00AA8F02:
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))))) == 0) ? 1 : 0;
    goto loc_00AA8EFB;
loc_00AA8F0A:
    v_rsi = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))))))));
loc_00AA8F0E:
loc_00AA8F10:
    goto loc_00AA9B85;
loc_00AA8F18:
    a1 = (unsigned int)((result) - (11));
    if (condition_is_equal) goto loc_00AA8F74;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA8F6A;
    a1 = (unsigned int)((a1) - (13));
    if (condition_is_equal) goto loc_00AA8F44;
    if (((unsigned int)(a1)) == 1) goto loc_00AA8F3C;
    goto loc_00AA9B85;
loc_00AA8F3C:
    goto loc_00AA9B85;
loc_00AA8F44:
    result = PnpStringToDwordValue(*(unsigned __int64 *)(v_rip + 347106 + 40), v_stack_m90, v_rip + 347106, *(unsigned __int64 *)(v_rip + 347106 + 40));
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00AA8F62;
    goto loc_00AA9B85;
loc_00AA8F62:
    goto loc_00AA9B85;
loc_00AA8F6A:
    v_rsi = ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 347106 + 40))) == 0) ? 1 : 0;
    goto loc_00AA8F10;
loc_00AA8F74:
    v_rsi = (v_rsi) | (-1);
loc_00AA8F78:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 347106 + 40) + v_rsi * 2)) != 0) goto loc_00AA8F78;
    goto loc_00AA8F10;
loc_00AA8F84:
    if ((*(unsigned int *)(v_stack_m58 + 32)) == 0) { v_rsi = (unsigned int)(*(unsigned __int64 *)(v_rip + 347106 + 40)); }
    goto loc_00AA9B92;
loc_00AA8F95:
    if ((*(unsigned int *)(v_stack_m58 + 32)) == 0) goto loc_00AA9B92;
    goto loc_00AA8F10;
loc_00AA8FAB:
    if (((unsigned int)(v_r10)) != 2) goto loc_00AA9B32;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m50 + 32))) - (1));
    if (condition_is_equal) goto loc_00AA97B2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA97B2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9725;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA959B;
    if (((unsigned int)(a1)) != 3) goto loc_00AA8E82;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 32)))) != 7) goto loc_00AA932F;
    v_stack_m90 = *(unsigned __int64 *)(v_stack_m58 + 40);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 36)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90)))) > 15) goto loc_00AA9247;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90)))) == 15) goto loc_00AA9214;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90))) - (1));
    if (condition_is_equal) goto loc_00AA918B;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00AA9091;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA918B;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00AA906D;
    if (((unsigned int)(a1)) != 1) goto loc_00AA8E82;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 36)))) <= ((unsigned int)(a1 + 1))) goto loc_00AA9077;
    goto loc_00AA907C;
loc_00AA906D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 36)))) <= 2) goto loc_00AA907F;
loc_00AA9077:
    v_rsi = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 347106 + 40)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)))) >= = 2) {
        v_rsi = (unsigned int)(*(unsigned __int64 *)(v_rip + 347106 + 40));
    }
    goto loc_00AA9B92;
loc_00AA9091:
    v_stack_mB8 = 0;
loc_00AA909C:
    if ((*(unsigned __int16 *)((unsigned int)(v_stack_mB8))) == 0) goto loc_00AA9157;
    result = (0) | (-1);
loc_00AA90AE:
    result = (result) + 1;
    if ((*(unsigned __int16 *)((unsigned int)(v_stack_mB8) + result * 2)) != 0) goto loc_00AA90AE;
    result = PnpMultiSzContainsString(*(unsigned __int64 *)(v_stack_m58 + 40), (unsigned int)(v_stack_mB8), *(unsigned __int64 *)(v_stack_m58 + 40), *(unsigned __int64 *)(v_rip + 347106 + 40));
    v_r11 = 0;
    if (result == 0) goto loc_00AA9123;
    if (0 != 0) goto loc_00AA90FF;
    v_stack_mB8 = 0;
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_stack_m50 + 36)), (unsigned int)(0x63647050ULL), *(unsigned __int64 *)(v_rip + 347106 + 40));
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9139;
loc_00AA90FF:
    a1 = (v_stack_mB8) + (result);
    result = memcpy(a1, (unsigned int)(v_stack_mB8), (unsigned int)((unsigned int)(result * 2 + 2)), *(unsigned __int64 *)(v_rip + 347106 + 40));
    result = (unsigned __int16)(((unsigned int)(v_stack_mB8)) + ((unsigned __int16)(result * 2 + 2)));
    v_stack_mB8 = (unsigned int)(result);
    v_r11 = 0;
    goto loc_00AA9129;
loc_00AA9123:
loc_00AA9129:
    v_rdi = ((unsigned int)((unsigned int)(result * 2 + 2))) >> (1);
    goto loc_00AA909C;
loc_00AA9139:
loc_00AA9142:
loc_00AA9146:
loc_00AA914A:
    if (sign_flag) goto loc_00AA9D3A;
    goto loc_00AA9B85;
loc_00AA9157:
    v_stack_mA0 = a1;
    if (a1 == 0) goto loc_00AA9142;
    result = (unsigned __int16)(((unsigned int)(v_stack_mB8)) + (2));
    v_stack_mA0 = a1;
    result = ((unsigned __int16)(result)) >> (1);
    v_stack_mB8 = (unsigned int)((unsigned __int16)((unsigned __int16)(result)));
    v_stack_mB0 = (unsigned __int16)((unsigned __int16)(result));
    *(unsigned __int16 *)(result + result * 2 - 2) = 0;
    goto loc_00AA9146;
loc_00AA918B:
    if ((*(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))))) != 0) goto loc_00AA919A;
    goto loc_00AA989C;
loc_00AA919A:
    if ((*(unsigned __int16 *)(v_stack_m90)) == 0) goto loc_00AA98C0;
    a1 = ((unsigned __int16)((unsigned __int16)(result)) + result * 1) - (2);
    if (a1 > 0xFFFEULL) goto loc_00AA9D2E;
    result = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(result)) + result * 1) - (2));
    v_stack_mB8 = (unsigned __int16)((unsigned __int16)(result));
    result = ExAllocatePool2(256, (unsigned __int16)(result), (unsigned int)(0x63647050ULL), *(unsigned __int64 *)(v_rip + 347106 + 40));
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, (unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))), result - 2, *(unsigned __int64 *)(v_rip + 347106 + 40));
    v_rbx = (result) >> (1);
    goto loc_00AA988D;
loc_00AA9214:
    v_stack_mC8 = 1;
    a4 = ((unsigned __int16)((unsigned __int16)(result))) >> (1);
    a2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))), a2, result - 2, a4);
    a2 = 0;
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
loc_00AA9236:
loc_00AA9238:
    goto loc_00AA9B8E;
loc_00AA9247:
    a1 = (unsigned int)((a1) - (16));
    if (condition_is_equal) goto loc_00AA92EF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA92D4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA92AD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9289;
    if (((unsigned int)(a1)) != 1) goto loc_00AA8E82;
    v_stack_mC8 = (unsigned __int8)(a1);
    a4 = (v_stack_mB0) >> (1);
    a2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((unsigned int)(v_stack_mB8), a2, result - 2, a4);
    result = (unsigned int)(~(result));
loc_00AA9282:
    result = (unsigned int)((result) >> (31));
    goto loc_00AA9238;
loc_00AA9289:
    v_stack_mC8 = 1;
    a4 = (v_stack_mB0) >> (1);
    a2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((unsigned int)(v_stack_mB8), a2, result - 2, a4);
    a2 = 0;
    a1 = (condition_is_less_or_equal) ? 1 : 0;
    goto loc_00AA9236;
loc_00AA92AD:
    v_stack_mC8 = 1;
    a4 = (v_stack_mB0) >> (1);
    a2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((unsigned int)(v_stack_mB8), a2, result - 2, a4);
    a2 = 0;
    a1 = (condition_is_greater) ? 1 : 0;
    goto loc_00AA9236;
loc_00AA92D4:
    v_stack_mC8 = 1;
    a4 = (v_stack_mB0) >> (1);
    a2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((unsigned int)(v_stack_mB8), a2, result - 2, a4);
    goto loc_00AA9282;
loc_00AA92EF:
    a4 = (v_stack_mB0) >> (1);
    a2 = (result) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings((unsigned int)(v_stack_mB8), a2, result - 2, a4);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AA9324;
    goto loc_00AA9B8E;
loc_00AA9324:
    goto loc_00AA9B85;
loc_00AA932F:
    if (((unsigned int)((unsigned int)(v_stack_mB8) - 1)) <= ((unsigned int)(a4))) goto loc_00AA9401;
    if (((unsigned int)((unsigned int)(v_stack_mB8))) != 4) goto loc_00AA8E82;
    if ((*(unsigned int *)(a2)) != 24) goto loc_00AA8E82;
    goto loc_00AA938A;
loc_00AA9362:
    v_r15 = (0) | (-1);
loc_00AA9366:
    v_r15 = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40) + v_r15 * 2)) != 0) goto loc_00AA9366;
    if (0 == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 40)))))) goto loc_00AA9395;
    result = ((unsigned int)((unsigned int)(v_r15 * 2 + 2))) >> (1);
    a1 = (unsigned int)((0) + ((unsigned int)(a4)));
loc_00AA938A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40) + result * 2)) != 0) goto loc_00AA9362;
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 40)))))) goto loc_00AA93F1;
loc_00AA9395:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40) + result * 2)) == 0) goto loc_00AA93F1;
    if (((unsigned int)(v_r15 * 2 + 2)) <= 2) goto loc_00AA93F1;
    v_stack_mB8 = (unsigned __int16)((unsigned __int16)(v_r15 * 2 + 2) - 16);
    v_stack_mB0 = (unsigned __int16)((unsigned __int16)(v_r15 * 2 + 2));
    result = ExAllocatePool2(256, (unsigned __int16)(v_r15 * 2 + 2), (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40) + result * 2, (unsigned int)((unsigned int)(v_r15 * 2 + 2)), a4);
    v_r11 = 0;
    goto loc_00AA9142;
loc_00AA93F1:
    goto loc_00AA914A;
loc_00AA9401:
    v_stack_m90 = *(unsigned __int64 *)(v_r15 * 2 + 2 + 40);
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)))) > 0xFFFEULL) goto loc_00AA9D2E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40) + result * 2))) - (1));
    if (condition_is_equal) goto loc_00AA9509;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA948A;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00AA946C;
    if (((unsigned int)(a1)) != 1) goto loc_00AA8E82;
    result = PnpMultiSzContainsString(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40), *(unsigned __int64 *)(v_r15 * 2 + 2 + 40), *(unsigned __int64 *)(v_r15 * 2 + 2 + 40), a4);
    v_r11 = 0;
    if (result == 0) goto loc_00AA9509;
    goto loc_00AA958C;
loc_00AA946C:
    result = PnpMultiSzContainsString((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))), *(unsigned __int64 *)(v_r15 * 2 + 2 + 40), *(unsigned __int64 *)(v_r15 * 2 + 2 + 40), a4);
    v_r11 = 0;
    v_r13 = v_stack_mA8;
    if (result != 0) { v_r13 = v_r15 * 2 + 2; }
    goto loc_00AA958C;
loc_00AA948A:
    result = PnpMultiSzContainsString(v_r13, *(unsigned __int64 *)(v_r15 * 2 + 2 + 40), *(unsigned __int64 *)(v_r15 * 2 + 2 + 40), a4);
    v_r11 = 0;
    if (result == 0) goto loc_00AA98C0;
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)))) - ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)))));
    v_stack_mB8 = (unsigned __int16)((unsigned __int16)(a1));
    result = ExAllocatePool2(256, (unsigned __int16)(a1), (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    v_rbx = (result) - (v_r13);
    v_rbx = (v_rbx) >> (1);
    if (!(condition_is_less_or_equal)) {
        a3 = v_rbx;
        a2 = v_r13;
        a1 = result;
        result = memcpy(a1, a2, a3, a4);
        result = v_stack_mA0;
    }
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)))));
    a3 = ((unsigned int)((unsigned int)(v_r14))) - (v_rbx);
    goto loc_00AA9890;
loc_00AA9509:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)) + v_r14 * 1)) > 0xFFFEULL) goto loc_00AA9D2E;
    v_stack_mB8 = (unsigned int)((unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)) + v_r14 * 1)));
    v_stack_mB0 = (unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)) + v_r14 * 1));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)) + v_r14 * 1))), (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, v_r13, v_r14 - 2, a4);
    v_rbx = (v_r14) >> (1);
    result = memcpy(v_stack_mA0 - 2 + v_rbx * 2, v_stack_m90, (unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)), a4);
    v_r15 = ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r15 * 2 + 2 + 36)) + v_r14 * 1)) >> (1);
    v_r11 = 0;
    *(unsigned __int16 *)(v_stack_mA0 + v_r15 * 2 - 2) = 0;
loc_00AA958C:
    goto loc_00AA9B85;
loc_00AA959B:
    if ((*(unsigned int *)(v_stack_m58 + 32)) != 4) goto loc_00AA979C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90)))) > 10) goto loc_00AA966E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90)))) == 10) goto loc_00AA9669;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90))) - (1));
    if (condition_is_equal) goto loc_00AA9660;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9655;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9649;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA962B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9617;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA960F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9607;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9602;
    if (((unsigned int)(a1)) != 1) goto loc_00AA969A;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m58 + 40)))) | ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40))))));
    goto loc_00AA964D;
loc_00AA9602:
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40))))));
    goto loc_00AA964D;
loc_00AA9607:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40)))) >> ((unsigned __int8)((unsigned int)((unsigned int)(a3)))));
    goto loc_00AA9658;
loc_00AA960F:
    a4 = (unsigned int)((a4) << ((unsigned __int8)((unsigned int)((unsigned int)(a3)))));
    goto loc_00AA9658;
loc_00AA9617:
    if ((unsigned int)(a3) == 0) goto loc_00AA963F;
    a2 = 0;
    goto loc_00AA8EFB;
loc_00AA962B:
    if ((unsigned int)(a3) == 0) goto loc_00AA963F;
    a2 = 0;
loc_00AA9638:
    goto loc_00AA8EFB;
loc_00AA963F:
    goto loc_00AA8E58;
loc_00AA9649:
    a3 = (unsigned int)((a3) * ((unsigned int)(a4)));
loc_00AA964D:
    goto loc_00AA8EFB;
loc_00AA9655:
    a4 = (unsigned int)((a4) - ((unsigned int)(a3)));
loc_00AA9658:
    goto loc_00AA8EFB;
loc_00AA9660:
    goto loc_00AA8EFB;
loc_00AA9669:
    a3 = (unsigned int)((a3) ^ ((unsigned int)(a4)));
    goto loc_00AA964D;
loc_00AA966E:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - (13));
    if (condition_is_equal) goto loc_00AA9709;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA96F9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA96EB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA96DD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA96CF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA96C1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA96B3;
    if (((unsigned int)(a1)) == 1) goto loc_00AA96A8;
loc_00AA969A:
    goto loc_00AA9C4A;
loc_00AA96A8:
    result = (((unsigned int)(a4)) >= ((unsigned int)(a3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96B3:
    result = (((unsigned int)(a4)) <= ((unsigned int)(a3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96C1:
    result = (((unsigned int)(a4)) > ((unsigned int)(a3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96CF:
    result = (((unsigned int)(a4)) < ((unsigned int)(a3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96DD:
    result = (((unsigned int)(a4)) != ((unsigned int)(a3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96EB:
    result = (((unsigned int)(a4)) == ((unsigned int)(a3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96F9:
    if ((unsigned int)(a4) != 0) goto loc_00AA971B;
    if ((unsigned int)(a3) == 0) goto loc_00AA8EFB;
    goto loc_00AA971B;
loc_00AA9709:
    if ((unsigned int)(a4) == 0) goto loc_00AA8F0E;
    if ((unsigned int)(a3) == 0) goto loc_00AA8F0E;
loc_00AA971B:
    goto loc_00AA8EFB;
loc_00AA9725:
    if ((*(unsigned int *)(v_stack_m58 + 32)) != 3) goto loc_00AA979C;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) - (15));
    if (condition_is_equal) goto loc_00AA977D;
    if (((unsigned int)(a1)) == 1) goto loc_00AA9754;
    goto loc_00AA97A8;
loc_00AA9754:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36))))) goto loc_00AA9770;
    result = memcmp(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40), *(unsigned __int64 *)(v_stack_m58 + 40), (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00AA9773;
    goto loc_00AA9778;
loc_00AA9770:
    v_r11 = 0;
loc_00AA9773:
loc_00AA9778:
    goto loc_00AA97AB;
loc_00AA977D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36))))) goto loc_00AA97A5;
    result = memcmp(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40), 0, (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00AA97AB;
    goto loc_00AA97AB;
loc_00AA979C:
    goto loc_00AA97AB;
loc_00AA97A5:
loc_00AA97A8:
    v_r11 = 0;
loc_00AA97AB:
    goto loc_00AA9B85;
loc_00AA97B2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 32)) - 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36))))) goto loc_00AA98C5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 32)))) != 7) goto loc_00AA979C;
    v_stack_mB0 = *(unsigned __int64 *)(v_stack_m58 + 40);
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)))) > 0xFFFEULL) goto loc_00AA9D2E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0))) - (1));
    if (condition_is_equal) goto loc_00AA982D;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00AA98AD;
    if (((unsigned int)(a1)) == 1) goto loc_00AA981A;
    goto loc_00AA989C;
loc_00AA981A:
    result = PnpMultiSzContainsString(*(unsigned __int64 *)(v_stack_m58 + 40), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40), *(unsigned __int64 *)(v_stack_m58 + 40), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_r11 = 0;
    if (result != 0) goto loc_00AA989C;
loc_00AA982D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)) + (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)) * 1)) > 0xFFFEULL) goto loc_00AA9D2E;
    v_stack_mB8 = (unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)) + (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)) * 1));
    result = ExAllocatePool2(256, (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)) + (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)) * 1), (unsigned int)(0x63647050ULL), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 40), (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36)), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_rbx = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))) + 36))) >> (1);
    a1 = (v_rbx * 2) + (result);
loc_00AA988D:
loc_00AA9890:
    result = memcpy(a1, v_stack_mB0, (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_r11 = 0;
loc_00AA9898:
loc_00AA989C:
    v_stack_mB0 = (unsigned __int16)((unsigned int)(v_stack_mB8));
    goto loc_00AA97AB;
loc_00AA98AD:
    result = PnpMultiSzContainsString((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)), (unsigned int)(v_stack_mB8), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)), (unsigned int)(*(unsigned int *)(v_stack_m58 + 36)));
    v_r11 = 0;
    if (result == 0) goto loc_00AA9898;
loc_00AA98C0:
    goto loc_00AA989C;
loc_00AA98C5:
    if ((*(unsigned int *)(v_rbx + 36)) > 0xFFFEULL) goto loc_00AA9B28;
    if ((*(unsigned int *)(v_rbx + 36)) > 0xFFFEULL) goto loc_00AA9B28;
    v_r15 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 36))) - (2));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + 36)) - (2));
    v_stack_m90 = *(unsigned __int64 *)(v_rbx + 40);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB8)))) - (1));
    if (condition_is_equal) goto loc_00AA9A7A;
    a1 = (unsigned int)((a1) - (12));
    if (condition_is_equal) goto loc_00AA9A72;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9A5B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9A2D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9A02;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA99DF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA99B4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AA9984;
    if (((unsigned int)(a1)) == 1) goto loc_00AA995A;
    goto loc_00AA9B1B;
loc_00AA995A:
    a4 = ((unsigned __int16)(v_r14)) >> (1);
    a2 = ((unsigned __int16)(v_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 40), a2, *(unsigned __int64 *)(v_rbx + 40), a4);
    result = (unsigned int)(~(result));
loc_00AA997A:
    result = (unsigned int)((result) >> (31));
    goto loc_00AA9B14;
loc_00AA9984:
    a4 = ((unsigned __int16)(v_r14)) >> (1);
    a2 = ((unsigned __int16)(v_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 40), a2, *(unsigned __int64 *)(v_rbx + 40), a4);
    v_r11 = 0;
    a1 = (condition_is_less_or_equal) ? 1 : 0;
loc_00AA99AD:
    goto loc_00AA9B17;
loc_00AA99B4:
    a4 = ((unsigned __int16)(v_r14)) >> (1);
    a2 = ((unsigned __int16)(v_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 40), a2, *(unsigned __int64 *)(v_rbx + 40), a4);
    v_r11 = 0;
    a1 = (condition_is_greater) ? 1 : 0;
    goto loc_00AA99AD;
loc_00AA99DF:
    a4 = ((unsigned __int16)(v_r14)) >> (1);
    a2 = ((unsigned __int16)(v_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 40), a2, *(unsigned __int64 *)(v_rbx + 40), a4);
    goto loc_00AA997A;
loc_00AA9A02:
    a4 = ((unsigned __int16)(v_r14)) >> (1);
    a2 = ((unsigned __int16)(v_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 40), a2, *(unsigned __int64 *)(v_rbx + 40), a4);
    v_r11 = 0;
    a1 = ((unsigned int)(result) != 0) ? 1 : 0;
    goto loc_00AA99AD;
loc_00AA9A2D:
    a4 = ((unsigned __int16)(v_r14)) >> (1);
    a2 = ((unsigned __int16)(v_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 40), a2, *(unsigned __int64 *)(v_rbx + 40), a4);
    v_r11 = 0;
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    goto loc_00AA99AD;
loc_00AA9A5B:
    if (((unsigned __int16)(v_r15)) >= ((unsigned __int16)(result))) goto loc_00AA9A67;
loc_00AA9A61:
    v_rsi = (unsigned int)((unsigned int)(a1));
    if (((unsigned __int16)(v_r14)) >= ((unsigned __int16)(result))) {
        v_rsi = (unsigned int)(a4);
    }
    goto loc_00AA9B1B;
loc_00AA9A72:
    if (((unsigned __int16)(v_r15)) < ((unsigned __int16)(result))) goto loc_00AA9A6A;
    goto loc_00AA9A61;
loc_00AA9A7A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 40))) == 0) goto loc_00AA9B1B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 40))) != 0) goto loc_00AA9A93;
    goto loc_00AA9B1B;
loc_00AA9A93:
    a1 = (unsigned int)(((unsigned __int16)(v_r14)) + ((unsigned int)((unsigned __int16)(v_r15))));
    if (((unsigned int)(a1)) >= 0xFFFEULL) goto loc_00AA9D2E;
    a3 = (unsigned __int16)((*(unsigned __int64 *)(v_rbx + 40)) + ((unsigned __int16)(v_r14)));
    v_stack_mB8 = (unsigned __int16)(v_r15 + v_r14 * 1);
    v_stack_mB0 = (unsigned __int16)((unsigned __int16)(a3));
    result = ExAllocatePool2(256, (unsigned __int16)(a3), (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, v_stack_m90, (unsigned int)((unsigned int)((unsigned __int16)(v_r15))), a4);
    v_rbx = ((unsigned __int16)(v_r15)) >> (1);
    a3 = ((unsigned __int16)(v_r14)) + (2);
    a1 = (v_rbx * 2) + (result);
    result = memcpy(a1, *(unsigned __int64 *)(v_rbx + 40), a3, a4);
loc_00AA9B14:
    v_r11 = 0;
loc_00AA9B17:
loc_00AA9B1B:
    goto loc_00AA97AB;
loc_00AA9B28:
    goto loc_00AA8E58;
loc_00AA9B32:
    if (((unsigned int)(*(unsigned __int64 *)(v_rbx + 40))) != 3) goto loc_00AA9B92;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m48 + 32))))) - (1));
    if (condition_is_equal) goto loc_00AA9BF7;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AA9BF7;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AA9BDD;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AA9B73;
    if (((unsigned int)(result)) == ((unsigned int)(*(unsigned __int64 *)(v_rbx + 40)))) goto loc_00AA9B6A;
    goto loc_00AA9B7A;
loc_00AA9B6A:
    result = ((*(unsigned int *)(v_stack_m48 + 36)) > 4) ? 1 : 0;
    goto loc_00AA9B7D;
loc_00AA9B73:
loc_00AA9B7A:
    result = ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m48 + 40))) != 0) ? 1 : 0;
loc_00AA9B7D:
    if ((unsigned __int8)(result) != 0) goto loc_00AA9BFD;
loc_00AA9B81:
loc_00AA9B85:
    if (v_stack_m58 != 0) goto loc_00AA9C46;
loc_00AA9B8E:
loc_00AA9B92:
    result = ExAllocatePool2(256, 48, (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    if (result == 0) goto loc_00AA9D35;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    if (v_stack_mA0 == 0) goto loc_00AA9C03;
    v_rdi = v_r11 + 7;
    if (((unsigned __int16)((unsigned int)(v_stack_mB8))) != ((unsigned __int16)(v_stack_mB0))) { v_rdi = (unsigned int)(v_r11 + 1); }
    goto loc_00AA9C34;
loc_00AA9BDD:
loc_00AA9BE4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(256 + 36))) == 0) goto loc_00AA9B81;
    a3 = (*(unsigned __int64 *)(256 + 40)) + (v_r11 + 1);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(256 + 40))) != 0) goto loc_00AA9BFD;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(256 + 36))) + ((unsigned int)(result)));
    goto loc_00AA9BE4;
loc_00AA9BF7:
    if ((*(unsigned int *)(256 + 36)) < ((unsigned int)(a3))) goto loc_00AA9B81;
loc_00AA9BFD:
    goto loc_00AA9B85;
loc_00AA9C03:
    result = ExAllocatePool2(256, 4, (unsigned int)(0x63647050ULL), v_r11 + 1);
    v_r11 = 0;
    if (result == 0) goto loc_00AA9D35;
    *(unsigned int *)(result) = (unsigned int)(v_rsi);
loc_00AA9C34:
    *(unsigned int *)(v_stack_m50 + 32) = 4;
    *(unsigned int *)(v_stack_m50 + 36) = 4;
    *(unsigned __int64 *)(v_stack_m50 + 40) = result;
    goto loc_00AA9C50;
loc_00AA9C46:
loc_00AA9C4A:
loc_00AA9C50:
    *(unsigned __int64 *)(v_stack_m88 + (unsigned int)(v_stack_m98) * 8) = v_stack_m50;
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_00AA9C9F;
loc_00AA9C68:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 24)) != 0) goto loc_00AA9C92;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 40), a2, (unsigned int)(0x63647050ULL), 1);
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m58), a2, (unsigned int)(0x63647050ULL), 1);
    v_r11 = 0;
loc_00AA9C92:
    v_rsi = (v_stack_m58) + (8);
    v_r14 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mB4)))) - (v_r11 + 1);
    if (condition_is_not_equal) goto loc_00AA9C68;
loc_00AA9C9F:
loc_00AA9CAB:
    result = (result) | (-1);
loc_00AA9CAF:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m80 + result * 2)) != 0) goto loc_00AA9CAF;
    v_rsi = (v_stack_m80 + result * 2) + (2);
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m98)) + (1));
    v_stack_m80 = v_rsi;
    v_stack_m98 = (unsigned int)(v_r14);
    goto loc_00AA8D0A;
loc_00AA9CD7:
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_00AA9DF7;
    v_stack_m80 = 0;
    result = PiDevCfgResolveVariable(v_stack_m70, v_rsi, v_stack_m80, 1);
    v_r11 = 0;
    if (sign_flag) goto loc_00AA9DE9;
    *(unsigned __int64 *)(v_stack_m88 + (unsigned int)((unsigned int)(v_r14)) * 8) = v_stack_m80;
    goto loc_00AA9CAB;
loc_00AA9D0D:
    goto loc_00AA9D42;
loc_00AA9D14:
    result = ExFreePoolWithTag(v_stack_m88, v_rsi, v_stack_m80, 1);
    v_r11 = 0;
    goto loc_00AA9D49;
loc_00AA9D24:
loc_00AA9D29:
    goto loc_00AA9D49;
loc_00AA9D2E:
    goto loc_00AA9D29;
loc_00AA9D35:
loc_00AA9D3A:
loc_00AA9D42:
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_00AA9D99;
loc_00AA9D49:
loc_00AA9D55:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 24)) != 0) goto loc_00AA9D7F;
    result = 1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 40), a2, v_stack_m80, 1);
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m58), a2, v_stack_m80, 1);
    v_r11 = 0;
loc_00AA9D7F:
    v_rdi = (v_stack_m58) + (8);
    v_r14 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mB4)))) - (v_r11 + 1);
    if (condition_is_not_equal) goto loc_00AA9D55;
    if (v_stack_m88 == 0) goto loc_00AA9E1F;
loc_00AA9D99:
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_00AA9DDD;
loc_00AA9D9E:
loc_00AA9DAA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88) + 24)) != 0) goto loc_00AA9DD0;
    result = *(unsigned __int64 *)(v_stack_m88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88) + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88) + 40), a2, v_stack_m80, 1);
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m88), a2, v_stack_m80, 1);
    v_r11 = 0;
loc_00AA9DD0:
    v_rdi = (v_stack_m88) + (8);
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m98)))) - (1);
    if (condition_is_not_equal) goto loc_00AA9DAA;
loc_00AA9DDD:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, a2, v_stack_m80, 1);
    goto loc_00AA9E1F;
loc_00AA9DE9:
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00AA9D99;
loc_00AA9DF0:
    goto loc_00AA9D99;
loc_00AA9DF7:
    goto loc_00AA9D99;
loc_00AA9DFE:
    if (sign_flag) goto loc_00AA9D99;
    if (((unsigned int)((unsigned int)(v_stack_m98))) != 1) goto loc_00AA9DF0;
    result = PiDevCfgCopyVariableData(v_stack_m60, *(unsigned __int64 *)(v_stack_m88), v_stack_m80, 1);
    v_r11 = 0;
    goto loc_00AA9D9E;
loc_00AA9E1A:
loc_00AA9E1F:
    result = v_stack_m68;
    if (v_stack_m68 != 0) {
        a2 = 0;
        a1 = v_stack_m68;
        result = ExFreePoolWithTag(a1, a2, v_stack_m80, 1);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m80, 1);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgResolveVariableExpression(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint8_t v_stack_mC8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x361B1D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m70 = Arg1;
    Arg2 = 0;
    v_stack_m60 = Arg3;
    Arg1 = 0;
    v_stack_m68 = 0;
    v_stack_m98 = 0;
    v_stack_m48 = 0;
    Arg3 = 0;
    v_stack_m58 = v_xmm0;
    result = IopGetRegistryValue(0, v_rip + 354588, Arg3, v_stack_m68);
    local_r11 = 0;
    if (sign_flag) goto loc_00AA9E1F;
    result = PnpValidateRegistryMultiSz(v_stack_m68, v_rip + 354588, Arg3, v_stack_m68);
    if ((uint8_t)(result) == 0) goto loc_00AA9E1A;
    local_rsi = ((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8))) + (v_stack_m68);
    v_stack_m80 = local_rsi;
    if ((*(uint16_t *)(local_rsi)) == 0) goto loc_00AA9E1A;
loc_00AA8CA4:
    local_r12 = (uint32_t)((0) + ((uint32_t)(local_r11 + 1)));
    Arg1 = (v_stack_m68) | (-1);
loc_00AA8CAB:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(local_rsi + Arg1 * 2)) != 0) goto loc_00AA8CAB;
    result = (local_rsi + Arg1 * 2) + (2);
    if ((*(uint16_t *)(result)) != 0) goto loc_00AA8CA4;
    v_stack_m78 = (uint32_t)(local_r12);
    if ((uint32_t)(local_r12) == 0) goto loc_00AA9E1A;
    Arg2 = ((uint32_t)((uint32_t)(local_r12))) << (3);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x63647050ULL), v_stack_m68);
    local_r11 = 0;
    v_stack_m88 = result;
    if (result != 0) goto loc_00AA8D04;
    goto loc_00AA9E1F;
loc_00AA8D04:
loc_00AA8D0A:
    if ((*(uint16_t *)(local_rsi)) == 0) goto loc_00AA9DFE;
    if ((*(uint16_t *)(local_rsi + 0x2)) == 0) goto loc_00AA8D2F;
    if ((*(uint16_t *)(local_rsi + 0x4)) != 0) goto loc_00AA9CD7;
loc_00AA8D2F:
loc_00AA8D32:
    if (1 >= 27) goto loc_00AA9CD7;
    if ((*(uint32_t *)(local_rsi)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA81CF + 0x1 + 0x1 * 2 * 8 + 0x8)))))) goto loc_00AA8D51;
    Arg2 = (uint32_t)((1) + (1));
    goto loc_00AA8D32;
loc_00AA8D51:
    if (v_rip + 688591 + 1 + 1 * 2 * 8 == 0) goto loc_00AA9CD7;
    v_stack_mB4 = 0;
    local_r13 = (uint32_t)((v_stack_m70) | (0xFFFFFFFFULL));
loc_00AA8D6D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA81CF + 0x1 + 0x1 * 2 * 8 + 0x10))))) goto loc_00AA8D97;
    if (0 == 0) goto loc_00AA9D0D;
    local_r14 = (uint32_t)((0) + ((uint32_t)(local_r13)));
    local_r10 = (uint32_t)((0) + (1));
    v_stack_m98 = (uint32_t)(local_r14);
    v_stack_mB4 = (uint32_t)(local_r10);
    *(uint64_t *)(v_stack_m5F + 0x0 * 8 + 0x7) = *(uint64_t *)(result + local_r14 * 8);
    goto loc_00AA8D6D;
loc_00AA8D97:
    if (sign_flag) goto loc_00AA9D42;
    v_stack_m90 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    if (((uint32_t)(local_r10)) != 1) goto loc_00AA8FAB;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA81CF + 0x1 + 0x1 * 2 * 8))))) - (22));
    if (condition_is_equal) goto loc_00AA8F95;
    if (((uint32_t)(Arg2)) == 1) goto loc_00AA8F84;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20))) - (1));
    if (condition_is_equal) goto loc_00AA8F18;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00AA8F18;
    Arg2 = (uint32_t)((Arg2) - (2));
    if (condition_is_equal) goto loc_00AA8E60;
    if (((uint32_t)(Arg2)) != 3) goto loc_00AA8E18;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA81CF + 0x1 + 0x1 * 2 * 8))) - (11));
    if (condition_is_equal) goto loc_00AA8E31;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA8E24;
loc_00AA8E18:
    goto loc_00AA9C50;
loc_00AA8E24:
    local_rsi = ((*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x28))) == 0) ? 1 : 0;
    goto loc_00AA9B92;
loc_00AA8E31:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x28))) == 0) goto loc_00AA9B92;
loc_00AA8E3B:
    local_rsi = (uint32_t)((local_rsi) + 1);
    result = (*(uint64_t *)(result + local_r14 * 8)) | (-1);
loc_00AA8E41:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x28) + result * 2)) != 0) goto loc_00AA8E41;
    Arg2 = (*(uint64_t *)(v_stack_m58 + 0x28) + result * 2) + (v_rip + 663697);
    if ((*(uint16_t *)(Arg2)) != 0) goto loc_00AA8E3B;
loc_00AA8E58:
    goto loc_00AA914A;
loc_00AA8E60:
    Arg1 = (uint32_t)((Arg1) - (11));
    if (condition_is_equal) goto loc_00AA8F0A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA8F02;
    Arg1 = (uint32_t)((Arg1) - (13));
    if (condition_is_equal) goto loc_00AA8EF9;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AA8E90;
loc_00AA8E82:
    goto loc_00AA9C50;
loc_00AA8E90:
    result = ExAllocatePool2(256, 22, (uint32_t)(0x63647050ULL), 1);
    local_r11 = 0;
    if (result == 0) goto loc_00AA9D24;
    result = RtlStringCchPrintfW(result, local_r11 + 11, v_rip + 347106, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))))));
    Arg2 = 0;
    if (sign_flag) goto loc_00AA9D14;
    local_r14 = (0) | (-1);
loc_00AA8EDA:
    local_r14 = (local_r14) + 1;
    if ((*(uint16_t *)(result + local_r14 * 2)) != 0) goto loc_00AA8EDA;
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(local_r14)));
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(v_rip + 663591)));
    v_stack_mB0 = local_r14;
    goto loc_00AA9B92;
loc_00AA8EF9:
loc_00AA8EFB:
    goto loc_00AA9B92;
loc_00AA8F02:
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))))) == 0) ? 1 : 0;
    goto loc_00AA8EFB;
loc_00AA8F0A:
    local_rsi = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))))))));
loc_00AA8F0E:
loc_00AA8F10:
    goto loc_00AA9B85;
loc_00AA8F18:
    Arg1 = (uint32_t)((result) - (11));
    if (condition_is_equal) goto loc_00AA8F74;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA8F6A;
    Arg1 = (uint32_t)((Arg1) - (13));
    if (condition_is_equal) goto loc_00AA8F44;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AA8F3C;
    goto loc_00AA9B85;
loc_00AA8F3C:
    goto loc_00AA9B85;
loc_00AA8F44:
    result = PnpStringToDwordValue(*(uint64_t *)(v_rip + 0x54BE2 + 0x28), v_stack_m90, v_rip + 347106, *(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_00AA8F62;
    goto loc_00AA9B85;
loc_00AA8F62:
    goto loc_00AA9B85;
loc_00AA8F6A:
    local_rsi = ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x54BE2 + 0x28))) == 0) ? 1 : 0;
    goto loc_00AA8F10;
loc_00AA8F74:
    local_rsi = (local_rsi) | (-1);
loc_00AA8F78:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x54BE2 + 0x28) + local_rsi * 2)) != 0) goto loc_00AA8F78;
    goto loc_00AA8F10;
loc_00AA8F84:
    if ((*(uint32_t *)(v_stack_m58 + 0x20)) == 0) { local_rsi = (uint32_t)(*(uint64_t *)(v_rip + 0x54BE2 + 0x28)); }
    goto loc_00AA9B92;
loc_00AA8F95:
    if ((*(uint32_t *)(v_stack_m58 + 0x20)) == 0) goto loc_00AA9B92;
    goto loc_00AA8F10;
loc_00AA8FAB:
    if (((uint32_t)(local_r10)) != 2) goto loc_00AA9B32;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x20))) - (1));
    if (condition_is_equal) goto loc_00AA97B2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA97B2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9725;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA959B;
    if (((uint32_t)(Arg1)) != 3) goto loc_00AA8E82;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20)))) != 7) goto loc_00AA932F;
    v_stack_m90 = *(uint64_t *)(v_stack_m58 + 0x28);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90)))) > 15) goto loc_00AA9247;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90)))) == 15) goto loc_00AA9214;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90))) - (1));
    if (condition_is_equal) goto loc_00AA918B;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00AA9091;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA918B;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00AA906D;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AA8E82;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)))) <= ((uint32_t)(Arg1 + 1))) goto loc_00AA9077;
    goto loc_00AA907C;
loc_00AA906D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)))) <= 2) goto loc_00AA907F;
loc_00AA9077:
    local_rsi = (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x54BE2 + 0x28)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)))) >= = 2) {
        local_rsi = (uint32_t)(*(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    }
    goto loc_00AA9B92;
loc_00AA9091:
    v_stack_mB8 = 0;
loc_00AA909C:
    if ((*(uint16_t *)((uint32_t)(v_stack_mB8))) == 0) goto loc_00AA9157;
    result = (0) | (-1);
loc_00AA90AE:
    result = (result) + 1;
    if ((*(uint16_t *)((uint32_t)(v_stack_mB8) + result * 2)) != 0) goto loc_00AA90AE;
    result = PnpMultiSzContainsString(*(uint64_t *)(v_stack_m58 + 0x28), (uint32_t)(v_stack_mB8), *(uint64_t *)(v_stack_m58 + 0x28), *(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    local_r11 = 0;
    if (result == 0) goto loc_00AA9123;
    if (0 != 0) goto loc_00AA90FF;
    v_stack_mB8 = 0;
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)), (uint32_t)(0x63647050ULL), *(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9139;
loc_00AA90FF:
    Arg1 = (v_stack_mB8) + (result);
    result = memcpy(Arg1, (uint32_t)(v_stack_mB8), (uint32_t)((uint32_t)(result * 2 + 2)), *(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    result = (uint16_t)(((uint32_t)(v_stack_mB8)) + ((uint16_t)(result * 2 + 2)));
    v_stack_mB8 = (uint32_t)(result);
    local_r11 = 0;
    goto loc_00AA9129;
loc_00AA9123:
loc_00AA9129:
    local_rdi = ((uint32_t)((uint32_t)(result * 2 + 2))) >> (1);
    goto loc_00AA909C;
loc_00AA9139:
loc_00AA9142:
loc_00AA9146:
loc_00AA914A:
    if (sign_flag) goto loc_00AA9D3A;
    goto loc_00AA9B85;
loc_00AA9157:
    v_stack_mA0 = Arg1;
    if (Arg1 == 0) goto loc_00AA9142;
    result = (uint16_t)(((uint32_t)(v_stack_mB8)) + (2));
    v_stack_mA0 = Arg1;
    result = ((uint16_t)(result)) >> (1);
    v_stack_mB8 = (uint32_t)((uint16_t)((uint16_t)(result)));
    v_stack_mB0 = (uint16_t)((uint16_t)(result));
    *(uint16_t *)(result + result * 2 - 0x2) = 0;
    goto loc_00AA9146;
loc_00AA918B:
    if ((*(uint16_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))))) != 0) goto loc_00AA919A;
    goto loc_00AA989C;
loc_00AA919A:
    if ((*(uint16_t *)(v_stack_m90)) == 0) goto loc_00AA98C0;
    Arg1 = ((uint16_t)((uint16_t)(result)) + result * 1) - (2);
    if (Arg1 > 0xFFFEULL) goto loc_00AA9D2E;
    result = (uint16_t)(((uint16_t)((uint16_t)(result)) + result * 1) - (2));
    v_stack_mB8 = (uint16_t)((uint16_t)(result));
    result = ExAllocatePool2(256, (uint16_t)(result), (uint32_t)(0x63647050ULL), *(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, (uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))), result - 2, *(uint64_t *)(v_rip + 0x54BE2 + 0x28));
    local_rbx = (result) >> (1);
    goto loc_00AA988D;
loc_00AA9214:
    v_stack_mC8 = 1;
    a4 = ((uint16_t)((uint16_t)(result))) >> (1);
    Arg2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))), Arg2, result - 2, a4);
    Arg2 = 0;
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
loc_00AA9236:
loc_00AA9238:
    goto loc_00AA9B8E;
loc_00AA9247:
    Arg1 = (uint32_t)((Arg1) - (16));
    if (condition_is_equal) goto loc_00AA92EF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA92D4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA92AD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9289;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AA8E82;
    v_stack_mC8 = (uint8_t)(Arg1);
    a4 = (v_stack_mB0) >> (1);
    Arg2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((uint32_t)(v_stack_mB8), Arg2, result - 2, a4);
    result = (uint32_t)(~(result));
loc_00AA9282:
    result = (uint32_t)((result) >> (31));
    goto loc_00AA9238;
loc_00AA9289:
    v_stack_mC8 = 1;
    a4 = (v_stack_mB0) >> (1);
    Arg2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((uint32_t)(v_stack_mB8), Arg2, result - 2, a4);
    Arg2 = 0;
    Arg1 = (condition_is_less_or_equal) ? 1 : 0;
    goto loc_00AA9236;
loc_00AA92AD:
    v_stack_mC8 = 1;
    a4 = (v_stack_mB0) >> (1);
    Arg2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((uint32_t)(v_stack_mB8), Arg2, result - 2, a4);
    Arg2 = 0;
    Arg1 = (condition_is_greater) ? 1 : 0;
    goto loc_00AA9236;
loc_00AA92D4:
    v_stack_mC8 = 1;
    a4 = (v_stack_mB0) >> (1);
    Arg2 = (result) >> (1);
    result = RtlCompareUnicodeStrings((uint32_t)(v_stack_mB8), Arg2, result - 2, a4);
    goto loc_00AA9282;
loc_00AA92EF:
    a4 = (v_stack_mB0) >> (1);
    Arg2 = (result) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings((uint32_t)(v_stack_mB8), Arg2, result - 2, a4);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AA9324;
    goto loc_00AA9B8E;
loc_00AA9324:
    goto loc_00AA9B85;
loc_00AA932F:
    if (((uint32_t)((uint32_t)(v_stack_mB8) - 1)) <= ((uint32_t)(a4))) goto loc_00AA9401;
    if (((uint32_t)((uint32_t)(v_stack_mB8))) != 4) goto loc_00AA8E82;
    if ((*(uint32_t *)(Arg2)) != 24) goto loc_00AA8E82;
    goto loc_00AA938A;
loc_00AA9362:
    local_r15 = (0) | (-1);
loc_00AA9366:
    local_r15 = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28) + local_r15 * 2)) != 0) goto loc_00AA9366;
    if (0 == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x28)))))) goto loc_00AA9395;
    result = ((uint32_t)((uint32_t)(local_r15 * 2 + 2))) >> (1);
    Arg1 = (uint32_t)((0) + ((uint32_t)(a4)));
loc_00AA938A:
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28) + result * 2)) != 0) goto loc_00AA9362;
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x28)))))) goto loc_00AA93F1;
loc_00AA9395:
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28) + result * 2)) == 0) goto loc_00AA93F1;
    if (((uint32_t)(local_r15 * 2 + 2)) <= 2) goto loc_00AA93F1;
    v_stack_mB8 = (uint16_t)((uint16_t)(local_r15 * 2 + 2) - 16);
    v_stack_mB0 = (uint16_t)((uint16_t)(local_r15 * 2 + 2));
    result = ExAllocatePool2(256, (uint16_t)(local_r15 * 2 + 2), (uint32_t)(0x63647050ULL), a4);
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, *(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28) + result * 2, (uint32_t)((uint32_t)(local_r15 * 2 + 2)), a4);
    local_r11 = 0;
    goto loc_00AA9142;
loc_00AA93F1:
    goto loc_00AA914A;
loc_00AA9401:
    v_stack_m90 = *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28);
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)))) > 0xFFFEULL) goto loc_00AA9D2E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28) + result * 2))) - (1));
    if (condition_is_equal) goto loc_00AA9509;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA948A;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00AA946C;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AA8E82;
    result = PnpMultiSzContainsString(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28), *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28), *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28), a4);
    local_r11 = 0;
    if (result == 0) goto loc_00AA9509;
    goto loc_00AA958C;
loc_00AA946C:
    result = PnpMultiSzContainsString((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))), *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28), *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28), a4);
    local_r11 = 0;
    local_r13 = v_stack_mA8;
    if (result != 0) { local_r13 = local_r15 * 2 + 2; }
    goto loc_00AA958C;
loc_00AA948A:
    result = PnpMultiSzContainsString(local_r13, *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28), *(uint64_t *)(local_r15 * 2 + 0x2 + 0x28), a4);
    local_r11 = 0;
    if (result == 0) goto loc_00AA98C0;
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)))) - ((uint16_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)))));
    v_stack_mB8 = (uint16_t)((uint16_t)(Arg1));
    result = ExAllocatePool2(256, (uint16_t)(Arg1), (uint32_t)(0x63647050ULL), a4);
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    local_rbx = (result) - (local_r13);
    local_rbx = (local_rbx) >> (1);
    if (!(condition_is_less_or_equal)) {
        Arg3 = local_rbx;
        Arg2 = local_r13;
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, a4);
        result = v_stack_mA0;
    }
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)))));
    Arg3 = ((uint32_t)((uint32_t)(local_r14))) - (local_rbx);
    goto loc_00AA9890;
loc_00AA9509:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)) + local_r14 * 1)) > 0xFFFEULL) goto loc_00AA9D2E;
    v_stack_mB8 = (uint32_t)((uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)) + local_r14 * 1)));
    v_stack_mB0 = (uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)) + local_r14 * 1));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)) + local_r14 * 1))), (uint32_t)(0x63647050ULL), a4);
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, local_r13, local_r14 - 2, a4);
    local_rbx = (local_r14) >> (1);
    result = memcpy(v_stack_mA0 - 2 + local_rbx * 2, v_stack_m90, (uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)), a4);
    local_r15 = ((uint16_t)((uint32_t)(*(uint32_t *)(local_r15 * 2 + 0x2 + 0x24)) + local_r14 * 1)) >> (1);
    local_r11 = 0;
    *(uint16_t *)(v_stack_mA0 + local_r15 * 2 - 0x2) = 0;
loc_00AA958C:
    goto loc_00AA9B85;
loc_00AA959B:
    if ((*(uint32_t *)(v_stack_m58 + 0x20)) != 4) goto loc_00AA979C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90)))) > 10) goto loc_00AA966E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90)))) == 10) goto loc_00AA9669;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90))) - (1));
    if (condition_is_equal) goto loc_00AA9660;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9655;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9649;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA962B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9617;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA960F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9607;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9602;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AA969A;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m58 + 0x28)))) | ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28))))));
    goto loc_00AA964D;
loc_00AA9602:
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28))))));
    goto loc_00AA964D;
loc_00AA9607:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28)))) >> ((uint8_t)((uint32_t)((uint32_t)(Arg3)))));
    goto loc_00AA9658;
loc_00AA960F:
    a4 = (uint32_t)((a4) << ((uint8_t)((uint32_t)((uint32_t)(Arg3)))));
    goto loc_00AA9658;
loc_00AA9617:
    if ((uint32_t)(Arg3) == 0) goto loc_00AA963F;
    Arg2 = 0;
    goto loc_00AA8EFB;
loc_00AA962B:
    if ((uint32_t)(Arg3) == 0) goto loc_00AA963F;
    Arg2 = 0;
loc_00AA9638:
    goto loc_00AA8EFB;
loc_00AA963F:
    goto loc_00AA8E58;
loc_00AA9649:
    Arg3 = (uint32_t)((Arg3) * ((uint32_t)(a4)));
loc_00AA964D:
    goto loc_00AA8EFB;
loc_00AA9655:
    a4 = (uint32_t)((a4) - ((uint32_t)(Arg3)));
loc_00AA9658:
    goto loc_00AA8EFB;
loc_00AA9660:
    goto loc_00AA8EFB;
loc_00AA9669:
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(a4)));
    goto loc_00AA964D;
loc_00AA966E:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - (13));
    if (condition_is_equal) goto loc_00AA9709;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA96F9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA96EB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA96DD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA96CF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA96C1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA96B3;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AA96A8;
loc_00AA969A:
    goto loc_00AA9C4A;
loc_00AA96A8:
    result = (((uint32_t)(a4)) >= ((uint32_t)(Arg3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96B3:
    result = (((uint32_t)(a4)) <= ((uint32_t)(Arg3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96C1:
    result = (((uint32_t)(a4)) > ((uint32_t)(Arg3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96CF:
    result = (((uint32_t)(a4)) < ((uint32_t)(Arg3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96DD:
    result = (((uint32_t)(a4)) != ((uint32_t)(Arg3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96EB:
    result = (((uint32_t)(a4)) == ((uint32_t)(Arg3))) ? 1 : 0;
    goto loc_00AA9638;
loc_00AA96F9:
    if ((uint32_t)(a4) != 0) goto loc_00AA971B;
    if ((uint32_t)(Arg3) == 0) goto loc_00AA8EFB;
    goto loc_00AA971B;
loc_00AA9709:
    if ((uint32_t)(a4) == 0) goto loc_00AA8F0E;
    if ((uint32_t)(Arg3) == 0) goto loc_00AA8F0E;
loc_00AA971B:
    goto loc_00AA8EFB;
loc_00AA9725:
    if ((*(uint32_t *)(v_stack_m58 + 0x20)) != 3) goto loc_00AA979C;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) - (15));
    if (condition_is_equal) goto loc_00AA977D;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AA9754;
    goto loc_00AA97A8;
loc_00AA9754:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24))))) goto loc_00AA9770;
    result = memcmp(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28), *(uint64_t *)(v_stack_m58 + 0x28), (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00AA9773;
    goto loc_00AA9778;
loc_00AA9770:
    local_r11 = 0;
loc_00AA9773:
loc_00AA9778:
    goto loc_00AA97AB;
loc_00AA977D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24))))) goto loc_00AA97A5;
    result = memcmp(*(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28), 0, (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00AA97AB;
    goto loc_00AA97AB;
loc_00AA979C:
    goto loc_00AA97AB;
loc_00AA97A5:
loc_00AA97A8:
    local_r11 = 0;
loc_00AA97AB:
    goto loc_00AA9B85;
loc_00AA97B2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20)) - 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24))))) goto loc_00AA98C5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20)))) != 7) goto loc_00AA979C;
    v_stack_mB0 = *(uint64_t *)(v_stack_m58 + 0x28);
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)))) > 0xFFFEULL) goto loc_00AA9D2E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)))) > 0xFFFEULL) goto loc_00AA9D2E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0))) - (1));
    if (condition_is_equal) goto loc_00AA982D;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00AA98AD;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AA981A;
    goto loc_00AA989C;
loc_00AA981A:
    result = PnpMultiSzContainsString(*(uint64_t *)(v_stack_m58 + 0x28), *(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28), *(uint64_t *)(v_stack_m58 + 0x28), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_r11 = 0;
    if (result != 0) goto loc_00AA989C;
loc_00AA982D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)) + (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)) * 1)) > 0xFFFEULL) goto loc_00AA9D2E;
    v_stack_mB8 = (uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)) + (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)) * 1));
    result = ExAllocatePool2(256, (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)) + (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)) * 1), (uint32_t)(0x63647050ULL), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, *(uint64_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x28), (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24)), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_rbx = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))) + 0x24))) >> (1);
    Arg1 = (local_rbx * 2) + (result);
loc_00AA988D:
loc_00AA9890:
    result = memcpy(Arg1, v_stack_mB0, (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_r11 = 0;
loc_00AA9898:
loc_00AA989C:
    v_stack_mB0 = (uint16_t)((uint32_t)(v_stack_mB8));
    goto loc_00AA97AB;
loc_00AA98AD:
    result = PnpMultiSzContainsString((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)), (uint32_t)(v_stack_mB8), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)), (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)));
    local_r11 = 0;
    if (result == 0) goto loc_00AA9898;
loc_00AA98C0:
    goto loc_00AA989C;
loc_00AA98C5:
    if ((*(uint32_t *)(local_rbx + 0x24)) > 0xFFFEULL) goto loc_00AA9B28;
    if ((*(uint32_t *)(local_rbx + 0x24)) > 0xFFFEULL) goto loc_00AA9B28;
    local_r15 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_rbx + 0x24))) - (2));
    local_r14 = (uint16_t)((*(uint16_t *)(local_rbx + 0x24)) - (2));
    v_stack_m90 = *(uint64_t *)(local_rbx + 0x28);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB8)))) - (1));
    if (condition_is_equal) goto loc_00AA9A7A;
    Arg1 = (uint32_t)((Arg1) - (12));
    if (condition_is_equal) goto loc_00AA9A72;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9A5B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9A2D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9A02;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA99DF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA99B4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AA9984;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AA995A;
    goto loc_00AA9B1B;
loc_00AA995A:
    a4 = ((uint16_t)(local_r14)) >> (1);
    Arg2 = ((uint16_t)(local_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x28), Arg2, *(uint64_t *)(local_rbx + 0x28), a4);
    result = (uint32_t)(~(result));
loc_00AA997A:
    result = (uint32_t)((result) >> (31));
    goto loc_00AA9B14;
loc_00AA9984:
    a4 = ((uint16_t)(local_r14)) >> (1);
    Arg2 = ((uint16_t)(local_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x28), Arg2, *(uint64_t *)(local_rbx + 0x28), a4);
    local_r11 = 0;
    Arg1 = (condition_is_less_or_equal) ? 1 : 0;
loc_00AA99AD:
    goto loc_00AA9B17;
loc_00AA99B4:
    a4 = ((uint16_t)(local_r14)) >> (1);
    Arg2 = ((uint16_t)(local_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x28), Arg2, *(uint64_t *)(local_rbx + 0x28), a4);
    local_r11 = 0;
    Arg1 = (condition_is_greater) ? 1 : 0;
    goto loc_00AA99AD;
loc_00AA99DF:
    a4 = ((uint16_t)(local_r14)) >> (1);
    Arg2 = ((uint16_t)(local_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x28), Arg2, *(uint64_t *)(local_rbx + 0x28), a4);
    goto loc_00AA997A;
loc_00AA9A02:
    a4 = ((uint16_t)(local_r14)) >> (1);
    Arg2 = ((uint16_t)(local_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x28), Arg2, *(uint64_t *)(local_rbx + 0x28), a4);
    local_r11 = 0;
    Arg1 = ((uint32_t)(result) != 0) ? 1 : 0;
    goto loc_00AA99AD;
loc_00AA9A2D:
    a4 = ((uint16_t)(local_r14)) >> (1);
    Arg2 = ((uint16_t)(local_r15)) >> (1);
    v_stack_mC8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x28), Arg2, *(uint64_t *)(local_rbx + 0x28), a4);
    local_r11 = 0;
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    goto loc_00AA99AD;
loc_00AA9A5B:
    if (((uint16_t)(local_r15)) >= ((uint16_t)(result))) goto loc_00AA9A67;
loc_00AA9A61:
    local_rsi = (uint32_t)((uint32_t)(Arg1));
    if (((uint16_t)(local_r14)) >= ((uint16_t)(result))) {
        local_rsi = (uint32_t)(a4);
    }
    goto loc_00AA9B1B;
loc_00AA9A72:
    if (((uint16_t)(local_r15)) < ((uint16_t)(result))) goto loc_00AA9A6A;
    goto loc_00AA9A61;
loc_00AA9A7A:
    if ((*(uint16_t *)(*(uint64_t *)(local_rbx + 0x28))) == 0) goto loc_00AA9B1B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rbx + 0x28))) != 0) goto loc_00AA9A93;
    goto loc_00AA9B1B;
loc_00AA9A93:
    Arg1 = (uint32_t)(((uint16_t)(local_r14)) + ((uint32_t)((uint16_t)(local_r15))));
    if (((uint32_t)(Arg1)) >= 0xFFFEULL) goto loc_00AA9D2E;
    Arg3 = (uint16_t)((*(uint64_t *)(local_rbx + 0x28)) + ((uint16_t)(local_r14)));
    v_stack_mB8 = (uint16_t)(local_r15 + local_r14 * 1);
    v_stack_mB0 = (uint16_t)((uint16_t)(Arg3));
    result = ExAllocatePool2(256, (uint16_t)(Arg3), (uint32_t)(0x63647050ULL), a4);
    local_r11 = 0;
    v_stack_mA0 = result;
    if (result == 0) goto loc_00AA9D24;
    result = memcpy(result, v_stack_m90, (uint32_t)((uint32_t)((uint16_t)(local_r15))), a4);
    local_rbx = ((uint16_t)(local_r15)) >> (1);
    Arg3 = ((uint16_t)(local_r14)) + (2);
    Arg1 = (local_rbx * 2) + (result);
    result = memcpy(Arg1, *(uint64_t *)(local_rbx + 0x28), Arg3, a4);
loc_00AA9B14:
    local_r11 = 0;
loc_00AA9B17:
loc_00AA9B1B:
    goto loc_00AA97AB;
loc_00AA9B28:
    goto loc_00AA8E58;
loc_00AA9B32:
    if (((uint32_t)(*(uint64_t *)(local_rbx + 0x28))) != 3) goto loc_00AA9B92;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x20))))) - (1));
    if (condition_is_equal) goto loc_00AA9BF7;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AA9BF7;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AA9BDD;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AA9B73;
    if (((uint32_t)(result)) == ((uint32_t)(*(uint64_t *)(local_rbx + 0x28)))) goto loc_00AA9B6A;
    goto loc_00AA9B7A;
loc_00AA9B6A:
    result = ((*(uint32_t *)(v_stack_m48 + 0x24)) > 4) ? 1 : 0;
    goto loc_00AA9B7D;
loc_00AA9B73:
loc_00AA9B7A:
    result = ((*(uint32_t *)(*(uint64_t *)(v_stack_m48 + 0x28))) != 0) ? 1 : 0;
loc_00AA9B7D:
    if ((uint8_t)(result) != 0) goto loc_00AA9BFD;
loc_00AA9B81:
loc_00AA9B85:
    if (v_stack_m58 != 0) goto loc_00AA9C46;
loc_00AA9B8E:
loc_00AA9B92:
    result = ExAllocatePool2(256, 48, (uint32_t)(0x63647050ULL), a4);
    local_r11 = 0;
    if (result == 0) goto loc_00AA9D35;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x18) = 0;
    if (v_stack_mA0 == 0) goto loc_00AA9C03;
    local_rdi = local_r11 + 7;
    if (((uint16_t)((uint32_t)(v_stack_mB8))) != ((uint16_t)(v_stack_mB0))) { local_rdi = (uint32_t)(local_r11 + 1); }
    goto loc_00AA9C34;
loc_00AA9BDD:
loc_00AA9BE4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(256 + 0x24))) == 0) goto loc_00AA9B81;
    Arg3 = (*(uint64_t *)(256 + 0x28)) + (local_r11 + 1);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(256 + 0x28))) != 0) goto loc_00AA9BFD;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(256 + 0x24))) + ((uint32_t)(result)));
    goto loc_00AA9BE4;
loc_00AA9BF7:
    if ((*(uint32_t *)(256 + 0x24)) < ((uint32_t)(Arg3))) goto loc_00AA9B81;
loc_00AA9BFD:
    goto loc_00AA9B85;
loc_00AA9C03:
    result = ExAllocatePool2(256, 4, (uint32_t)(0x63647050ULL), local_r11 + 1);
    local_r11 = 0;
    if (result == 0) goto loc_00AA9D35;
    *(uint32_t *)(result) = (uint32_t)(local_rsi);
loc_00AA9C34:
    *(uint32_t *)(v_stack_m50 + 0x20) = 4;
    *(uint32_t *)(v_stack_m50 + 0x24) = 4;
    *(uint64_t *)(v_stack_m50 + 0x28) = result;
    goto loc_00AA9C50;
loc_00AA9C46:
loc_00AA9C4A:
loc_00AA9C50:
    *(uint64_t *)(v_stack_m88 + (uint32_t)(v_stack_m98) * 8) = v_stack_m50;
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_00AA9C9F;
loc_00AA9C68:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x18)) != 0) goto loc_00AA9C92;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x28), Arg2, (uint32_t)(0x63647050ULL), 1);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m58), Arg2, (uint32_t)(0x63647050ULL), 1);
    local_r11 = 0;
loc_00AA9C92:
    local_rsi = (v_stack_m58) + (8);
    local_r14 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mB4)))) - (local_r11 + 1);
    if (condition_is_not_equal) goto loc_00AA9C68;
loc_00AA9C9F:
loc_00AA9CAB:
    result = (result) | (-1);
loc_00AA9CAF:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m80 + result * 2)) != 0) goto loc_00AA9CAF;
    local_rsi = (v_stack_m80 + result * 2) + (2);
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m98)) + (1));
    v_stack_m80 = local_rsi;
    v_stack_m98 = (uint32_t)(local_r14);
    goto loc_00AA8D0A;
loc_00AA9CD7:
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_00AA9DF7;
    v_stack_m80 = 0;
    result = PiDevCfgResolveVariable(v_stack_m70, local_rsi, v_stack_m80, 1);
    local_r11 = 0;
    if (sign_flag) goto loc_00AA9DE9;
    *(uint64_t *)(v_stack_m88 + (uint32_t)((uint32_t)(local_r14)) * 8) = v_stack_m80;
    goto loc_00AA9CAB;
loc_00AA9D0D:
    goto loc_00AA9D42;
loc_00AA9D14:
    result = ExFreePoolWithTag(v_stack_m88, local_rsi, v_stack_m80, 1);
    local_r11 = 0;
    goto loc_00AA9D49;
loc_00AA9D24:
loc_00AA9D29:
    goto loc_00AA9D49;
loc_00AA9D2E:
    goto loc_00AA9D29;
loc_00AA9D35:
loc_00AA9D3A:
loc_00AA9D42:
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_00AA9D99;
loc_00AA9D49:
loc_00AA9D55:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x18)) != 0) goto loc_00AA9D7F;
    result = 1;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x28), Arg2, v_stack_m80, 1);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m58), Arg2, v_stack_m80, 1);
    local_r11 = 0;
loc_00AA9D7F:
    local_rdi = (v_stack_m58) + (8);
    local_r14 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mB4)))) - (local_r11 + 1);
    if (condition_is_not_equal) goto loc_00AA9D55;
    if (v_stack_m88 == 0) goto loc_00AA9E1F;
loc_00AA9D99:
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_00AA9DDD;
loc_00AA9D9E:
loc_00AA9DAA:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m88) + 0x18)) != 0) goto loc_00AA9DD0;
    result = *(uint64_t *)(v_stack_m88);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m88) + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m88) + 0x28), Arg2, v_stack_m80, 1);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m88), Arg2, v_stack_m80, 1);
    local_r11 = 0;
loc_00AA9DD0:
    local_rdi = (v_stack_m88) + (8);
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m98)))) - (1);
    if (condition_is_not_equal) goto loc_00AA9DAA;
loc_00AA9DDD:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, Arg2, v_stack_m80, 1);
    goto loc_00AA9E1F;
loc_00AA9DE9:
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00AA9D99;
loc_00AA9DF0:
    goto loc_00AA9D99;
loc_00AA9DF7:
    goto loc_00AA9D99;
loc_00AA9DFE:
    if (sign_flag) goto loc_00AA9D99;
    if (((uint32_t)((uint32_t)(v_stack_m98))) != 1) goto loc_00AA9DF0;
    result = PiDevCfgCopyVariableData(v_stack_m60, *(uint64_t *)(v_stack_m88), v_stack_m80, 1);
    local_r11 = 0;
    goto loc_00AA9D9E;
loc_00AA9E1A:
loc_00AA9E1F:
    result = v_stack_m68;
    if (v_stack_m68 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m68;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m80, 1);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m80, 1);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA8C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
