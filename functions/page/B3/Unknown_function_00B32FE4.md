# sub_00B32FE4

- RVA: `0x00B32FE4`–`0x00B33479` (길이 `1,173` bytes)
- VA: `0x0000000140B32FE4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7EE8`
- 디코드: `312`개 명령, `1,173/1,173` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B32FF8` → [GetNextNoneWhiteSpace](../7A/GetNextNoneWhiteSpace_function_007A576C.md) (function, `0x007A576C`)
- `0x00B33039` → [GetOperandValue](../A0/GetOperandValue_function_00A024C0.md) (function, `0x00A024C0`)
- `0x00B3306C` → [IsValueSizeFixed](../A0/IsValueSizeFixed_function_00A02664.md) (function, `0x00A02664`)
- `0x00B330B3` → [SddlpReAlloc](../7A/SddlpReAlloc_function_007A5278.md) (function, `0x007A5278`)
- `0x00B330E0` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00B33141` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B3314E` → [FreeOperandValue](../A0/FreeOperandValue_function_00A0262C.md) (function, `0x00A0262C`)
- `0x00B33169` → [GetNextNoneWhiteSpace](../7A/GetNextNoneWhiteSpace_function_007A576C.md) (function, `0x007A576C`)
- `0x00B331D8` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x00B331F0` → [GetNextNoneWhiteSpace](../7A/GetNextNoneWhiteSpace_function_007A576C.md) (function, `0x007A576C`)
- `0x00B33224` → [LocalGetSidForString](../92/LocalGetSidForString_function_009292B4.md) (function, `0x009292B4`)
- `0x00B33249` → [GetNextNoneWhiteSpace](../7A/GetNextNoneWhiteSpace_function_007A576C.md) (function, `0x007A576C`)
- `0x00B33276` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00B3329F` → [GetBinaryOperandLen](../7A/GetBinaryOperandLen_function_007A55F8.md) (function, `0x007A55F8`)
- `0x00B332D8` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00B33307` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00B3331E` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00B33371` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00B333D4` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00B33443` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B331CB` → RVA `0x00037F80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00B33141` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B331D8` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x00B33276` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00B33371` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
  - `0x00B333D4` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **19**
  - `0x00B32FEB` → [GetOperandValue + 0x8D](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33003` → [GetOperandValue + 0x11E](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33045` → [GetOperandValue + 0x11E](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B330C2` → [GetOperandValue + 0x119](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B330F0` → [GetOperandValue + 0x119](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33172` → [GetOperandValue + 0x11E](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33197` → [GetOperandValue + 0x11E](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B331A1` → [GetOperandValue + 0x11E](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B331B6` → [GetOperandValue + 0x91](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B331C0` → [GetOperandValue + 0x107](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B331F9` → [GetOperandValue + 0x11E](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33291` → [GetOperandValue + 0x91](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B3329A` → [GetOperandValue + 0x107](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B332E7` → [GetOperandValue + 0x119](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B332F8` → [GetOperandValue + 0x8D](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B3330E` → [GetOperandValue + 0x119](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33325` → [GetOperandValue + 0x119](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B3345B` → [GetOperandValue + 0x107](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)
  - `0x00B33474` → [GetOperandValue + 0x91](../A0/GetOperandValue_function_00A024C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B32FE4  8B C1                           mov eax, ecx
00B32FE6  66 44 39 24 43                  cmp word ptr [rbx + rax*2], r12w
00B32FEB  0F 84 5C F5 EC FF               je 0x140a0254d
00B32FF1  48 8D 55 70                     lea rdx, [rbp + 0x70]
00B32FF5  48 8B CB                        mov rcx, rbx
00B32FF8  E8 6F 27 C7 FF                  call 0x1407a576c
00B32FFD  33 D2                           xor edx, edx
00B32FFF  8B F0                           mov esi, eax
00B33001  85 C0                           test eax, eax
00B33003  0F 85 D5 F5 EC FF               jne 0x140a025de
00B33009  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
00B3300C  48 8D 0C 43                     lea rcx, [rbx + rax*2]
00B33010  66 83 39 7B                     cmp word ptr [rcx], 0x7b
00B33014  0F 84 78 01 00 00               je 0x140b33192
00B3301A  88 54 24 40                     mov byte ptr [rsp + 0x40], dl
00B3301E  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00B33022  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B33027  45 33 C0                        xor r8d, r8d
00B3302A  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00B3302F  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00B33034  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00B33039  E8 82 F4 EC FF                  call 0x140a024c0
00B3303E  45 33 DB                        xor r11d, r11d
00B33041  8B F0                           mov esi, eax
00B33043  85 C0                           test eax, eax
00B33045  0F 85 93 F5 EC FF               jne 0x140a025de
00B3304B  4C 8B 4D D8                     mov r9, qword ptr [rbp - 0x28]
00B3304F  44 38 5D 50                     cmp byte ptr [rbp + 0x50], r11b
00B33053  74 13                           je 0x140b33068
00B33055  45 84 ED                        test r13b, r13b
00B33058  74 0A                           je 0x140b33064
00B3305A  45 3A 69 01                     cmp r13b, byte ptr [r9 + 1]
00B3305E  0F 85 2E 01 00 00               jne 0x140b33192
00B33064  45 8A 69 01                     mov r13b, byte ptr [r9 + 1]
00B33068  41 8A 49 01                     mov cl, byte ptr [r9 + 1]
00B3306C  E8 F3 F5 EC FF                  call 0x140a02664
00B33071  4C 8B 17                        mov r10, qword ptr [rdi]
00B33074  8A C8                           mov cl, al
00B33076  F6 D9                           neg cl
00B33078  44 8A E0                        mov r12b, al
00B3307B  1B D2                           sbb edx, edx
00B3307D  4D 8B 42 08                     mov r8, qword ptr [r10 + 8]
00B33081  83 E2 FC                        and edx, 0xfffffffc
00B33084  83 C2 05                        add edx, 5
00B33087  4D 85 C0                        test r8, r8
00B3308A  74 3E                           je 0x140b330ca
00B3308C  45 8B 52 04                     mov r10d, dword ptr [r10 + 4]
00B33090  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00B33094  41 03 C2                        add eax, r10d
00B33097  41 3B C2                        cmp eax, r10d
00B3309A  0F 82 FC 00 00 00               jb 0x140b3319c
00B330A0  44 8D 34 02                     lea r14d, [rdx + rax]
00B330A4  44 3B F0                        cmp r14d, eax
00B330A7  0F 82 EF 00 00 00               jb 0x140b3319c
00B330AD  41 8B D6                        mov edx, r14d
00B330B0  41 8B CA                        mov ecx, r10d
00B330B3  E8 C0 21 C7 FF                  call 0x1407a5278
00B330B8  48 8B 37                        mov rsi, qword ptr [rdi]
00B330BB  48 89 46 08                     mov qword ptr [rsi + 8], rax
00B330BF  48 85 C0                        test rax, rax
00B330C2  0F 84 11 F5 EC FF               je 0x140a025d9
00B330C8  EB 1F                           jmp 0x140b330e9
00B330CA  45 8B 71 04                     mov r14d, dword ptr [r9 + 4]
00B330CE  44 03 F2                        add r14d, edx
00B330D1  44 3B F2                        cmp r14d, edx
00B330D4  0F 82 C2 00 00 00               jb 0x140b3319c
00B330DA  41 8B CE                        mov ecx, r14d
00B330DD  49 8B F2                        mov rsi, r10
00B330E0  E8 A3 2E DF FF                  call 0x140925f88
00B330E5  48 89 46 08                     mov qword ptr [rsi + 8], rax
00B330E9  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
00B330ED  4D 85 C0                        test r8, r8
00B330F0  0F 84 E3 F4 EC FF               je 0x140a025d9
00B330F6  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00B330FA  8B 56 04                        mov edx, dword ptr [rsi + 4]
00B330FD  8A 48 01                        mov cl, byte ptr [rax + 1]
00B33100  42 88 0C 02                     mov byte ptr [rdx + r8], cl
00B33104  45 84 E4                        test r12b, r12b
00B33107  75 14                           jne 0x140b3311d
00B33109  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00B3310D  44 8B 46 04                     mov r8d, dword ptr [rsi + 4]
00B33111  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00B33115  8B 48 04                        mov ecx, dword ptr [rax + 4]
00B33118  41 89 4C 10 01                  mov dword ptr [r8 + rdx + 1], ecx
00B3311D  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00B33121  41 F6 DC                        neg r12b
00B33124  8B 46 04                        mov eax, dword ptr [rsi + 4]
00B33127  48 1B C9                        sbb rcx, rcx
00B3312A  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00B3312E  44 8B 42 04                     mov r8d, dword ptr [rdx + 4]
00B33132  48 83 C1 05                     add rcx, 5
00B33136  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00B3313A  48 03 C8                        add rcx, rax
00B3313D  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00B33141  E8 FA 36 B9 FF                  call 0x1406c6840
00B33146  44 89 76 04                     mov dword ptr [rsi + 4], r14d
00B3314A  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00B3314E  E8 D9 F4 EC FF                  call 0x140a0262c
00B33153  33 C0                           xor eax, eax
00B33155  48 8D 55 70                     lea rdx, [rbp + 0x70]
00B33159  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00B3315D  48 8B CB                        mov rcx, rbx
00B33160  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
00B33163  41 03 07                        add eax, dword ptr [r15]
00B33166  89 45 70                        mov dword ptr [rbp + 0x70], eax
00B33169  E8 FE 25 C7 FF                  call 0x1407a576c
00B3316E  8B F0                           mov esi, eax
00B33170  85 C0                           test eax, eax
00B33172  0F 85 66 F4 EC FF               jne 0x140a025de
00B33178  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
00B3317B  0F B7 14 4B                     movzx edx, word ptr [rbx + rcx*2]
00B3317F  66 83 FA 2C                     cmp dx, 0x2c
00B33183  75 21                           jne 0x140b331a6
00B33185  FF C1                           inc ecx
00B33187  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
00B3318A  45 33 E4                        xor r12d, r12d
00B3318D  E9 52 FE FF FF                  jmp 0x140b32fe4
00B33192  BE 38 05 00 00                  mov esi, 0x538
00B33197  E9 42 F4 EC FF                  jmp 0x140a025de
00B3319C  BE 16 02 00 00                  mov esi, 0x216
00B331A1  E9 38 F4 EC FF                  jmp 0x140a025de
00B331A6  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
00B331AA  66 83 FA 7D                     cmp dx, 0x7d
00B331AE  75 0B                           jne 0x140b331bb
00B331B0  8D 41 01                        lea eax, [rcx + 1]
00B331B3  41 89 07                        mov dword ptr [r15], eax
00B331B6  E9 96 F3 EC FF                  jmp 0x140a02551
00B331BB  BE 38 05 00 00                  mov esi, 0x538
00B331C0  E9 02 F4 EC FF                  jmp 0x140a025c7
00B331C5  41 BE 03 00 00 00               mov r14d, 3
00B331CB  48 8D 15 AE 4D 50 FF            lea rdx, [rip - 0xafb252]
00B331D2  45 8B C6                        mov r8d, r14d
00B331D5  48 8B CB                        mov rcx, rbx
00B331D8  E8 E3 CF 9C FF                  call 0x1405001c0
00B331DD  48 8D 55 70                     lea rdx, [rbp + 0x70]
00B331E1  48 8B CB                        mov rcx, rbx
00B331E4  85 C0                           test eax, eax
00B331E6  0F 85 B3 00 00 00               jne 0x140b3329f
00B331EC  44 89 75 70                     mov dword ptr [rbp + 0x70], r14d
00B331F0  E8 77 25 C7 FF                  call 0x1407a576c
00B331F5  8B F0                           mov esi, eax
00B331F7  85 C0                           test eax, eax
00B331F9  0F 85 DF F3 EC FF               jne 0x140a025de
00B331FF  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
00B33202  66 83 3C 4B 28                  cmp word ptr [rbx + rcx*2], 0x28
00B33207  75 89                           jne 0x140b33192
00B33209  44 8D 71 01                     lea r14d, [rcx + 1]
00B3320D  4F 8D 24 36                     lea r12, [r14 + r14]
00B33211  49 8D 0C 1C                     lea rcx, [r12 + rbx]
00B33215  4C 8D 8D 80 00 00 00            lea r9, [rbp + 0x80]
00B3321C  4C 8D 45 F0                     lea r8, [rbp - 0x10]
00B33220  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00B33224  E8 8B 60 DF FF                  call 0x1409292b4
00B33229  8B F0                           mov esi, eax
00B3322B  85 C0                           test eax, eax
00B3322D  75 67                           jne 0x140b33296
00B3322F  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00B33233  48 8D 55 70                     lea rdx, [rbp + 0x70]
00B33237  49 2B C4                        sub rax, r12
00B3323A  48 8B CB                        mov rcx, rbx
00B3323D  48 2B C3                        sub rax, rbx
00B33240  48 D1 F8                        sar rax, 1
00B33243  41 03 C6                        add eax, r14d
00B33246  89 45 70                        mov dword ptr [rbp + 0x70], eax
00B33249  E8 1E 25 C7 FF                  call 0x1407a576c
00B3324E  8B F0                           mov esi, eax
00B33250  85 C0                           test eax, eax
00B33252  75 42                           jne 0x140b33296
00B33254  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
00B33257  66 83 3C 4B 29                  cmp word ptr [rbx + rcx*2], 0x29
00B3325C  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
00B33260  0F 85 55 FF FF FF               jne 0x140b331bb
00B33266  48 8B 3F                        mov rdi, qword ptr [rdi]
00B33269  8D 41 01                        lea eax, [rcx + 1]
00B3326C  48 8B CB                        mov rcx, rbx
00B3326F  41 89 07                        mov dword ptr [r15], eax
00B33272  C6 47 01 51                     mov byte ptr [rdi + 1], 0x51
00B33276  E8 F5 9F 92 FF                  call 0x14045d270
00B3327B  89 47 04                        mov dword ptr [rdi + 4], eax
00B3327E  33 C9                           xor ecx, ecx
00B33280  38 8D 80 00 00 00               cmp byte ptr [rbp + 0x80], cl
00B33286  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
00B3328A  8B D9                           mov ebx, ecx
00B3328C  0F 94 C0                        sete al
00B3328F  88 07                           mov byte ptr [rdi], al
00B33291  E9 BB F2 EC FF                  jmp 0x140a02551
00B33296  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
00B3329A  E9 28 F3 EC FF                  jmp 0x140a025c7
00B3329F  E8 54 23 C7 FF                  call 0x1407a55f8
00B332A4  66 83 3B 23                     cmp word ptr [rbx], 0x23
00B332A8  0F 85 96 00 00 00               jne 0x140b33344
00B332AE  44 8B 6D 70                     mov r13d, dword ptr [rbp + 0x70]
00B332B2  41 BC 02 00 00 00               mov r12d, 2
00B332B8  45 3B EC                        cmp r13d, r12d
00B332BB  0F 82 D1 FE FF FF               jb 0x140b33192
00B332C1  48 8B 07                        mov rax, qword ptr [rdi]
00B332C4  45 8B F5                        mov r14d, r13d
00B332C7  41 D1 EE                        shr r14d, 1
00B332CA  41 8B CE                        mov ecx, r14d
00B332CD  45 89 2F                        mov dword ptr [r15], r13d
00B332D0  C6 40 01 18                     mov byte ptr [rax + 1], 0x18
00B332D4  44 89 70 04                     mov dword ptr [rax + 4], r14d
00B332D8  E8 AB 2C DF FF                  call 0x140925f88
00B332DD  4C 8B 0F                        mov r9, qword ptr [rdi]
00B332E0  49 89 41 08                     mov qword ptr [r9 + 8], rax
00B332E4  48 85 C0                        test rax, rax
00B332E7  0F 84 EC F2 EC FF               je 0x140a025d9
00B332ED  41 8D 45 FF                     lea eax, [r13 - 1]
00B332F1  4C 63 C0                        movsxd r8, eax
00B332F4  49 83 F8 01                     cmp r8, 1
00B332F8  0F 8C 4F F2 EC FF               jl 0x140a0254d
00B332FE  42 0F B7 0C 43                  movzx ecx, word ptr [rbx + r8*2]
00B33303  48 8D 55 68                     lea rdx, [rbp + 0x68]
00B33307  E8 48 23 C7 FF                  call 0x1407a5654
00B3330C  84 C0                           test al, al
00B3330E  0F 84 C5 F2 EC FF               je 0x140a025d9
00B33314  42 0F B7 4C 43 FE               movzx ecx, word ptr [rbx + r8*2 - 2]
00B3331A  48 8D 55 58                     lea rdx, [rbp + 0x58]
00B3331E  E8 31 23 C7 FF                  call 0x1407a5654
00B33323  84 C0                           test al, al
00B33325  0F 84 AE F2 EC FF               je 0x140a025d9
00B3332B  8A 55 58                        mov dl, byte ptr [rbp + 0x58]
00B3332E  41 FF CE                        dec r14d
00B33331  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00B33335  C0 E2 04                        shl dl, 4
00B33338  0A 55 68                        or dl, byte ptr [rbp + 0x68]
00B3333B  4D 2B C4                        sub r8, r12
00B3333E  41 88 14 06                     mov byte ptr [r14 + rax], dl
00B33342  EB B0                           jmp 0x140b332f4
00B33344  44 8B 65 70                     mov r12d, dword ptr [rbp + 0x70]
00B33348  45 85 E4                        test r12d, r12d
00B3334B  0F 84 41 FE FF FF               je 0x140b33192
00B33351  48 8D 45 78                     lea rax, [rbp + 0x78]
00B33355  45 89 27                        mov dword ptr [r15], r12d
00B33358  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3335D  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00B33361  45 33 C9                        xor r9d, r9d
00B33364  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00B3336C  48 8B D3                        mov rdx, rbx
00B3336F  33 C9                           xor ecx, ecx
00B33371  E8 FE F2 9C FF                  call 0x140502674
00B33376  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00B3337A  45 33 C0                        xor r8d, r8d
00B3337D  4C 8B E8                        mov r13, rax
00B33380  48 3B D3                        cmp rdx, rbx
00B33383  75 09                           jne 0x140b3338e
00B33385  48 85 C0                        test rax, rax
00B33388  0F 84 04 FE FF FF               je 0x140b33192
00B3338E  4A 8D 0C 63                     lea rcx, [rbx + r12*2]
00B33392  48 3B D1                        cmp rdx, rcx
00B33395  0F 85 F7 FD FF FF               jne 0x140b33192
00B3339B  44 39 45 78                     cmp dword ptr [rbp + 0x78], r8d
00B3339F  0F 85 ED FD FF FF               jne 0x140b33192
00B333A5  0F B7 03                        movzx eax, word ptr [rbx]
00B333A8  41 BC 02 00 00 00               mov r12d, 2
00B333AE  66 83 F8 2D                     cmp ax, 0x2d
00B333B2  75 40                           jne 0x140b333f4
00B333B4  48 8D 45 78                     lea rax, [rbp + 0x78]
00B333B8  49 03 DC                        add rbx, r12
00B333BB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B333C0  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00B333C4  48 8B D3                        mov rdx, rbx
00B333C7  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00B333CF  45 33 C9                        xor r9d, r9d
00B333D2  33 C9                           xor ecx, ecx
00B333D4  E8 9B F2 9C FF                  call 0x140502674
00B333D9  49 3B C5                        cmp rax, r13
00B333DC  72 09                           jb 0x140b333e7
00B333DE  48 85 C0                        test rax, rax
00B333E1  0F 85 AB FD FF FF               jne 0x140b33192
00B333E7  0F B7 03                        movzx eax, word ptr [rbx]
00B333EA  45 0F B7 FC                     movzx r15d, r12w
00B333EE  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00B333F2  EB 18                           jmp 0x140b3340c
00B333F4  66 83 F8 2B                     cmp ax, 0x2b
00B333F8  75 0E                           jne 0x140b33408
00B333FA  49 03 DC                        add rbx, r12
00B333FD  41 BF 01 00 00 00               mov r15d, 1
00B33403  0F B7 03                        movzx eax, word ptr [rbx]
00B33406  EB 04                           jmp 0x140b3340c
00B33408  45 0F B7 FE                     movzx r15d, r14w
00B3340C  66 83 F8 30                     cmp ax, 0x30
00B33410  75 1F                           jne 0x140b33431
00B33412  48 8D 43 02                     lea rax, [rbx + 2]
00B33416  48 3B C2                        cmp rax, rdx
00B33419  73 11                           jae 0x140b3342c
00B3341B  0F B7 00                        movzx eax, word ptr [rax]
00B3341E  B9 DF FF 00 00                  mov ecx, 0xffdf
00B33423  66 83 E8 58                     sub ax, 0x58
00B33427  66 85 C1                        test cx, ax
00B3342A  74 08                           je 0x140b33434
00B3342C  41 B6 01                        mov r14b, 1
00B3342F  EB 03                           jmp 0x140b33434
00B33431  45 8A F4                        mov r14b, r12b
00B33434  48 8B 07                        mov rax, qword ptr [rdi]
00B33437  B9 0A 00 00 00                  mov ecx, 0xa
00B3343C  C6 40 01 04                     mov byte ptr [rax + 1], 4
00B33440  89 48 04                        mov dword ptr [rax + 4], ecx
00B33443  E8 40 2B DF FF                  call 0x140925f88
00B33448  48 8B 0F                        mov rcx, qword ptr [rdi]
00B3344B  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
00B3344F  48 89 41 08                     mov qword ptr [rcx + 8], rax
00B33453  48 85 C0                        test rax, rax
00B33456  75 08                           jne 0x140b33460
00B33458  8D 70 08                        lea esi, [rax + 8]
00B3345B  E9 67 F1 EC FF                  jmp 0x140a025c7
00B33460  4C 89 28                        mov qword ptr [rax], r13
00B33463  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00B33467  66 44 89 78 08                  mov word ptr [rax + 8], r15w
00B3346C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00B33470  44 88 70 09                     mov byte ptr [rax + 9], r14b
00B33474  E9 D8 F0 EC FF                  jmp 0x140a02551
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B32FE4(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;

    result = GetNextNoneWhiteSpace(v_rbx, v_rbp + 112, a3, a4);
    a2 = 0;
    if ((*(unsigned __int16 *)(v_rbx + (unsigned int)(*(unsigned int *)(v_rbp + 112)) * 2)) == 123) goto loc_00B33192;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    a3 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_r15;
    result = GetOperandValue(v_rbx + (unsigned int)(*(unsigned int *)(v_rbp + 112)) * 2, a2, a3, v_rbp - 40);
    v_r11 = 0;
    if ((*(unsigned __int8 *)(v_rbp + 80)) == 0) goto loc_00B33068;
    if ((unsigned __int8)(v_r13) == 0) goto loc_00B33064;
    if (((unsigned __int8)(v_r13)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 40) + 1))) goto loc_00B33192;
loc_00B33064:
loc_00B33068:
    result = IsValueSizeFixed(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 40) + 1), a2, a3, *(unsigned __int64 *)(v_rbp - 40));
    a1 = (unsigned __int8)(-((unsigned __int8)(result)));
    a2 = (unsigned int)((a2) & (0xFFFFFFFCULL));
    a2 = (unsigned int)((a2) + (5));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8) == 0) goto loc_00B330CA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40) + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)))));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4))))) goto loc_00B3319C;
    if (((unsigned int)(a2 + result * 1)) < ((unsigned int)(result))) goto loc_00B3319C;
    result = SddlpReAlloc((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)))), (unsigned int)((unsigned int)(a2 + result * 1)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8), *(unsigned __int64 *)(v_rbp - 40));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8) = result;
    goto loc_00B330E9;
loc_00B330CA:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40) + 4))) + ((unsigned int)((unsigned int)((unsigned int)(a2 + result * 1)))));
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)((unsigned int)(a2 + result * 1))))) goto loc_00B3319C;
    result = SddlpAlloc((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(a2 + result * 1)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8), *(unsigned __int64 *)(v_rbp - 40));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 8) = result;
loc_00B330E9:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 4)) + *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 8) * 1) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 40) + 1));
    result = *(unsigned __int64 *)(v_rbp - 40);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) {
        result = *(unsigned __int64 *)(v_rbp - 40);
        a3 = *(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 4);
        a2 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 8);
        a1 = *(unsigned int *)(result + 4);
        *(unsigned int *)(a3 + a2 * 1 + 1) = a1;
    }
    v_r12 = (unsigned __int8)(-((unsigned __int8)(result)));
    a1 = (a1) & (-4);
    a1 = (a1) + (5);
    a1 = (a1) + ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 4)));
    a1 = (a1) + (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 8));
    result = memcpy(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 40) + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40) + 4)), *(unsigned __int64 *)(v_rbp - 40));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 4)) + 4) = (unsigned int)(v_r14);
    result = FreeOperandValue(*(unsigned __int64 *)(v_rbp - 40), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 40) + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40) + 4)), *(unsigned __int64 *)(v_rbp - 40));
    result = 0;
    *(unsigned __int64 *)(v_rbp - 40) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 112))) + (*(unsigned int *)(v_r15)));
    *(unsigned int *)(v_rbp + 112) = (unsigned int)(result);
    result = GetNextNoneWhiteSpace(v_rbx, v_rbp + 112, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40) + 4)), *(unsigned __int64 *)(v_rbp - 40));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + (unsigned int)(*(unsigned int *)(v_rbp + 112)) * 2))) != 44) goto loc_00B331A6;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 112))) + 1);
    *(unsigned int *)(v_rbp + 112) = a1;
    v_r12 = 0;
    goto loc_00B32FE4;
loc_00B33192:
loc_00B3319C:
loc_00B331A6:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + (unsigned int)(*(unsigned int *)(v_rbp + 112)) * 2))) != 125) goto loc_00B331BB;
    *(unsigned int *)(v_r15) = (unsigned int)(a1 + 1);
loc_00B331BB:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B32FE4(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;

    result = GetNextNoneWhiteSpace(local_rbx, local_rbp + 112, Arg3, a4);
    Arg2 = 0;
    if ((*(uint16_t *)(local_rbx + (uint32_t)(*(uint32_t *)(local_rbp + 0x70)) * 2)) == 123) goto loc_00B33192;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    Arg3 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = local_r15;
    result = GetOperandValue(local_rbx + (uint32_t)(*(uint32_t *)(local_rbp + 0x70)) * 2, Arg2, Arg3, local_rbp - 40);
    local_r11 = 0;
    if ((*(uint8_t *)(local_rbp + 0x50)) == 0) goto loc_00B33068;
    if ((uint8_t)(local_r13) == 0) goto loc_00B33064;
    if (((uint8_t)(local_r13)) != (*(uint8_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x1))) goto loc_00B33192;
loc_00B33064:
loc_00B33068:
    result = IsValueSizeFixed(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x1), Arg2, Arg3, *(uint64_t *)(local_rbp - 0x28));
    Arg1 = (uint8_t)(-((uint8_t)(result)));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFFCULL));
    Arg2 = (uint32_t)((Arg2) + (5));
    if (*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8) == 0) goto loc_00B330CA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)))));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4))))) goto loc_00B3319C;
    if (((uint32_t)(Arg2 + result * 1)) < ((uint32_t)(result))) goto loc_00B3319C;
    result = SddlpReAlloc((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)))), (uint32_t)((uint32_t)(Arg2 + result * 1)), *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8), *(uint64_t *)(local_rbp - 0x28));
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8) = result;
    goto loc_00B330E9;
loc_00B330CA:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x4))) + ((uint32_t)((uint32_t)((uint32_t)(Arg2 + result * 1)))));
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)((uint32_t)(Arg2 + result * 1))))) goto loc_00B3319C;
    result = SddlpAlloc((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(Arg2 + result * 1)), *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8), *(uint64_t *)(local_rbp - 0x28));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x8) = result;
loc_00B330E9:
    *(uint8_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x4)) + *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x8) * 1) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x1));
    result = *(uint64_t *)(local_rbp - 0x28);
    if ((uint8_t)((uint8_t)(result)) == 0) {
        result = *(uint64_t *)(local_rbp - 0x28);
        Arg3 = *(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x4);
        Arg2 = *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x8);
        Arg1 = *(uint32_t *)(result + 0x4);
        *(uint32_t *)(Arg3 + Arg2 * 1 + 0x1) = Arg1;
    }
    local_r12 = (uint8_t)(-((uint8_t)(result)));
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) + (5);
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x4)));
    Arg1 = (Arg1) + (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x8));
    result = memcpy(Arg1, *(uint64_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x4)), *(uint64_t *)(local_rbp - 0x28));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x4)) + 0x4) = (uint32_t)(local_r14);
    result = FreeOperandValue(*(uint64_t *)(local_rbp - 0x28), *(uint64_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x4)), *(uint64_t *)(local_rbp - 0x28));
    result = 0;
    *(uint64_t *)(local_rbp - 0x28) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x70))) + (*(uint32_t *)(local_r15)));
    *(uint32_t *)(local_rbp + 0x70) = (uint32_t)(result);
    result = GetNextNoneWhiteSpace(local_rbx, local_rbp + 112, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x4)), *(uint64_t *)(local_rbp - 0x28));
    if (((uint16_t)(*(uint16_t *)(local_rbx + (uint32_t)(*(uint32_t *)(local_rbp + 0x70)) * 2))) != 44) goto loc_00B331A6;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x70))) + 1);
    *(uint32_t *)(local_rbp + 0x70) = Arg1;
    local_r12 = 0;
    goto loc_00B32FE4;
loc_00B33192:
loc_00B3319C:
loc_00B331A6:
    if (((uint16_t)(*(uint16_t *)(local_rbx + (uint32_t)(*(uint32_t *)(local_rbp + 0x70)) * 2))) != 125) goto loc_00B331BB;
    *(uint32_t *)(local_r15) = (uint32_t)(Arg1 + 1);
loc_00B331BB:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B32FE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
