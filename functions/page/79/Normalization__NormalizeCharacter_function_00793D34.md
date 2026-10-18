# Normalization__NormalizeCharacter

- RVA: `0x00793D34`–`0x0079456A` (길이 `2,102` bytes)
- VA: `0x0000000140793D34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFE6C`
- 디코드: `580`개 명령, `2,102/2,102` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00793E96` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (function, `0x005ED8F8`)
- `0x00793EA3` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x00793EB6` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (function, `0x005EDDB4`)
- `0x00793F13` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (function, `0x005ED8F8`)
- `0x00793F1D` → [IsHangulLV](../../text/5E/IsHangulLV_function_005ED760.md) (function, `0x005ED760`)
- `0x00793F29` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (function, `0x005EDDB4`)
- `0x00793F34` → [ComposeHangulLVT](../../text/5E/ComposeHangulLVT_function_005ED728.md) (function, `0x005ED728`)
- `0x00793F3E` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (function, `0x005ED8F8`)
- `0x00793F54` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (function, `0x005EDDB4`)
- `0x00793F5F` → [ComposeHangulLV](../../text/5E/ComposeHangulLV_function_005ED6F8.md) (function, `0x005ED6F8`)
- `0x00793F6B` → [NormBuffer__Append](../../text/5E/NormBuffer__Append_function_005ED798.md) (function, `0x005ED798`)
- `0x00793FB7` → [ComposeHangulLV](../../text/5E/ComposeHangulLV_function_005ED6F8.md) (function, `0x005ED6F8`)
- `0x00793FD5` → [ComposeHangulLVT](../../text/5E/ComposeHangulLVT_function_005ED728.md) (function, `0x005ED728`)
- `0x00793FF6` → [IsHangulLV](../../text/5E/IsHangulLV_function_005ED760.md) (function, `0x005ED760`)
- `0x00794020` → [ComposeHangulLVT](../../text/5E/ComposeHangulLVT_function_005ED728.md) (function, `0x005ED728`)
- `0x00794073` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x007940AA` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x007940EC` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x00794123` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (function, `0x005ED8F8`)
- `0x007941A5` → [NormBuffer__IsBlocked](../../text/5E/NormBuffer__IsBlocked_function_005EDA7C.md) (function, `0x005EDA7C`)
- `0x007941B9` → [NormBuffer__InsertAtBlockedLocation](../../text/5E/NormBuffer__InsertAtBlockedLocation_function_005EDA50.md) (function, `0x005EDA50`)
- `0x007941E1` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x0079427D` → [NormBuffer__LastStartBasePair](../../text/5E/NormBuffer__LastStartBasePair_function_005EDB20.md) (function, `0x005EDB20`)
- `0x0079428A` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x0079429F` → [NormBuffer__LastStartBase](../../text/5E/NormBuffer__LastStartBase_function_005EDAF4.md) (function, `0x005EDAF4`)
- `0x007942AC` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x007942C7` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x007942D6` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (function, `0x005EDDB4`)
- `0x00794313` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x0079436D` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x00794389` → [NormBuffer__LastStartBasePair](../../text/5E/NormBuffer__LastStartBasePair_function_005EDB20.md) (function, `0x005EDB20`)
- `0x00794396` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x007943D9` → [NormBuffer__ReplaceLastStartBasePair](../../text/5E/NormBuffer__ReplaceLastStartBasePair_function_005EDD3C.md) (function, `0x005EDD3C`)
- `0x007943E3` → [NormBuffer__LastStartBase](../../text/5E/NormBuffer__LastStartBase_function_005EDAF4.md) (function, `0x005EDAF4`)
- `0x007943F0` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x00794437` → [NormBuffer__ReplaceLastStartBase](../../text/5E/NormBuffer__ReplaceLastStartBase_function_005EDCBC.md) (function, `0x005EDCBC`)
- `0x00794451` → [NormBuffer__RecheckStartCombinations](../../text/5E/NormBuffer__RecheckStartCombinations_function_005EDB70.md) (function, `0x005EDB70`)
- `0x00794464` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x00794477` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (function, `0x005EDDB4`)
- `0x007944BB` → [NormBuffer__IsBlocked](../../text/5E/NormBuffer__IsBlocked_function_005EDA7C.md) (function, `0x005EDA7C`)
- `0x007944CD` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x0079451F` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (function, `0x005ED858`)
- `0x00794544` → [Normalization__AppendDecomposedChar](Normalization__AppendDecomposedChar_function_00792E20.md) (function, `0x00792E20`)
- `0x00794563` → [NormBuffer__Append](../../text/5E/NormBuffer__Append_function_005ED798.md) (function, `0x005ED798`)

### Direct callers
- [Normalization__AppendDecomposedChar](Normalization__AppendDecomposedChar_function_00792E20.md) at `0x00792EF6`
- [Normalization__Normalize](Normalization__Normalize_function_00793B70.md) at `0x00793C63`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **35**
  - `0x00793E96` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (`PAGE` → `.text`)
  - `0x00793EB6` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (`PAGE` → `.text`)
  - `0x00793F13` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (`PAGE` → `.text`)
  - `0x00793F1D` → [IsHangulLV](../../text/5E/IsHangulLV_function_005ED760.md) (`PAGE` → `.text`)
  - `0x00793F29` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (`PAGE` → `.text`)
  - `0x00793F34` → [ComposeHangulLVT](../../text/5E/ComposeHangulLVT_function_005ED728.md) (`PAGE` → `.text`)
  - `0x00793F3E` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (`PAGE` → `.text`)
  - `0x00793F54` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (`PAGE` → `.text`)
  - `0x00793F5F` → [ComposeHangulLV](../../text/5E/ComposeHangulLV_function_005ED6F8.md) (`PAGE` → `.text`)
  - `0x00793F6B` → [NormBuffer__Append](../../text/5E/NormBuffer__Append_function_005ED798.md) (`PAGE` → `.text`)
  - `0x00793FB7` → [ComposeHangulLV](../../text/5E/ComposeHangulLV_function_005ED6F8.md) (`PAGE` → `.text`)
  - `0x00793FD5` → [ComposeHangulLVT](../../text/5E/ComposeHangulLVT_function_005ED728.md) (`PAGE` → `.text`)
  - `0x00793FF6` → [IsHangulLV](../../text/5E/IsHangulLV_function_005ED760.md) (`PAGE` → `.text`)
  - `0x00794020` → [ComposeHangulLVT](../../text/5E/ComposeHangulLVT_function_005ED728.md) (`PAGE` → `.text`)
  - `0x00794073` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x007940AA` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x007940EC` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x00794123` → [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) (`PAGE` → `.text`)
  - `0x007941A5` → [NormBuffer__IsBlocked](../../text/5E/NormBuffer__IsBlocked_function_005EDA7C.md) (`PAGE` → `.text`)
  - `0x007941B9` → [NormBuffer__InsertAtBlockedLocation](../../text/5E/NormBuffer__InsertAtBlockedLocation_function_005EDA50.md) (`PAGE` → `.text`)
  - `0x0079427D` → [NormBuffer__LastStartBasePair](../../text/5E/NormBuffer__LastStartBasePair_function_005EDB20.md) (`PAGE` → `.text`)
  - `0x0079429F` → [NormBuffer__LastStartBase](../../text/5E/NormBuffer__LastStartBase_function_005EDAF4.md) (`PAGE` → `.text`)
  - `0x007942D6` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (`PAGE` → `.text`)
  - `0x00794313` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x0079436D` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x00794389` → [NormBuffer__LastStartBasePair](../../text/5E/NormBuffer__LastStartBasePair_function_005EDB20.md) (`PAGE` → `.text`)
  - `0x007943D9` → [NormBuffer__ReplaceLastStartBasePair](../../text/5E/NormBuffer__ReplaceLastStartBasePair_function_005EDD3C.md) (`PAGE` → `.text`)
  - `0x007943E3` → [NormBuffer__LastStartBase](../../text/5E/NormBuffer__LastStartBase_function_005EDAF4.md) (`PAGE` → `.text`)
  - `0x00794437` → [NormBuffer__ReplaceLastStartBase](../../text/5E/NormBuffer__ReplaceLastStartBase_function_005EDCBC.md) (`PAGE` → `.text`)
  - `0x00794451` → [NormBuffer__RecheckStartCombinations](../../text/5E/NormBuffer__RecheckStartCombinations_function_005EDB70.md) (`PAGE` → `.text`)
  - `0x00794477` → [NormBuffer__RewindOutputCharacter](../../text/5E/NormBuffer__RewindOutputCharacter_function_005EDDB4.md) (`PAGE` → `.text`)
  - `0x007944BB` → [NormBuffer__IsBlocked](../../text/5E/NormBuffer__IsBlocked_function_005EDA7C.md) (`PAGE` → `.text`)
  - `0x007944CD` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x0079451F` → [NormBuffer__AppendEx](../../text/5E/NormBuffer__AppendEx_function_005ED858.md) (`PAGE` → `.text`)
  - `0x00794563` → [NormBuffer__Append](../../text/5E/NormBuffer__Append_function_005ED798.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00793D34  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00793D39  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00793D3E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00793D43  57                              push rdi
00793D44  41 54                           push r12
00793D46  41 55                           push r13
00793D48  41 56                           push r14
00793D4A  41 57                           push r15
00793D4C  48 83 EC 20                     sub rsp, 0x20
00793D50  49 8B D9                        mov rbx, r9
00793D53  45 8A E0                        mov r12b, r8b
00793D56  8B FA                           mov edi, edx
00793D58  48 8B F1                        mov rsi, rcx
00793D5B  45 33 ED                        xor r13d, r13d
00793D5E  44 8B F7                        mov r14d, edi
00793D61  45 84 E4                        test r12b, r12b
00793D64  0F 84 FC 01 00 00               je 0x140793f66
00793D6A  41 0F B6 D4                     movzx edx, r12b
00793D6E  8B CA                           mov ecx, edx
00793D70  45 84 E4                        test r12b, r12b
00793D73  0F 84 E5 07 00 00               je 0x14079455e
00793D79  81 E9 FB 00 00 00               sub ecx, 0xfb
00793D7F  0F 84 C9 07 00 00               je 0x14079454e
00793D85  83 E9 01                        sub ecx, 1
00793D88  0F 84 C6 07 00 00               je 0x140794554
00793D8E  83 E9 01                        sub ecx, 1
00793D91  0F 84 A5 07 00 00               je 0x14079453c
00793D97  83 E9 01                        sub ecx, 1
00793D9A  0F 84 23 01 00 00               je 0x140793ec3
00793DA0  83 F9 01                        cmp ecx, 1
00793DA3  0F 85 93 00 00 00               jne 0x140793e3c
00793DA9  81 FF 00 AC 00 00               cmp edi, 0xac00
00793DAF  7D 59                           jge 0x140793e0a
00793DB1  8D 87 00 EF FF FF               lea eax, [rdi - 0x1100]
00793DB7  41 8B FE                        mov edi, r14d
00793DBA  83 F8 12                        cmp eax, 0x12
00793DBD  0F 86 D8 01 00 00               jbe 0x140793f9b
00793DC3  41 8D 86 9F EE FF FF            lea eax, [r14 - 0x1161]
00793DCA  83 F8 14                        cmp eax, 0x14
00793DCD  0F 86 68 01 00 00               jbe 0x140793f3b
00793DD3  41 8D 86 58 EE FF FF            lea eax, [r14 - 0x11a8]
00793DDA  83 F8 1A                        cmp eax, 0x1a
00793DDD  0F 86 2D 01 00 00               jbe 0x140793f10
00793DE3  8B 06                           mov eax, dword ptr [rsi]
00793DE5  83 E8 0D                        sub eax, 0xd
00793DE8  A9 FF FE FF FF                  test eax, 0xfffffeff
00793DED  75 13                           jne 0x140793e02
00793DEF  41 8D 86 A1 EE FF FF            lea eax, [r14 - 0x115f]
00793DF6  3B C1                           cmp eax, ecx
00793DF8  77 08                           ja 0x140793e02
00793DFA  41 B4 FB                        mov r12b, 0xfb
00793DFD  E9 68 FF FF FF                  jmp 0x140793d6a
00793E02  45 8A E5                        mov r12b, r13b
00793E05  E9 54 FF FF FF                  jmp 0x140793d5e
00793E0A  81 FF A4 D7 00 00               cmp edi, 0xd7a4
00793E10  0F 8C D4 01 00 00               jl 0x140793fea
00793E16  41 8D 86 50 28 FF FF            lea eax, [r14 - 0xd7b0]
00793E1D  83 F8 16                        cmp eax, 0x16
00793E20  76 0F                           jbe 0x140793e31
00793E22  41 8D 86 35 28 FF FF            lea eax, [r14 - 0xd7cb]
00793E29  41 B4 FB                        mov r12b, 0xfb
00793E2C  83 F8 30                        cmp eax, 0x30
00793E2F  77 03                           ja 0x140793e34
00793E31  45 8A E5                        mov r12b, r13b
00793E34  41 8B FE                        mov edi, r14d
00793E37  E9 22 FF FF FF                  jmp 0x140793d5e
00793E3C  8B C7                           mov eax, edi
00793E3E  48 8B CA                        mov rcx, rdx
00793E41  83 E0 7F                        and eax, 0x7f
00793E44  48 C1 E1 07                     shl rcx, 7
00793E48  48 03 C8                        add rcx, rax
00793E4B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00793E4F  0F B6 54 01 80                  movzx edx, byte ptr [rcx + rax - 0x80]
00793E54  84 D2                           test dl, dl
00793E56  0F 84 B8 06 00 00               je 0x140794514
00793E5C  44 8A FA                        mov r15b, dl
00793E5F  40 8A EA                        mov bpl, dl
00793E62  41 80 E7 C0                     and r15b, 0xc0
00793E66  40 80 E5 3F                     and bpl, 0x3f
00793E6A  74 0A                           je 0x140793e76
00793E6C  40 80 FD 3F                     cmp bpl, 0x3f
00793E70  0F 85 A0 02 00 00               jne 0x140794116
00793E76  8B CA                           mov ecx, edx
00793E78  83 E9 7F                        sub ecx, 0x7f
00793E7B  0F 84 8D 06 00 00               je 0x14079450e
00793E81  83 E9 40                        sub ecx, 0x40
00793E84  0F 84 B2 06 00 00               je 0x14079453c
00793E8A  83 E9 01                        sub ecx, 1
00793E8D  0F 85 5F 06 00 00               jne 0x1407944f2
00793E93  48 8B CB                        mov rcx, rbx
00793E96  E8 5D 9A E5 FF                  call 0x1405ed8f8
00793E9B  8B D0                           mov edx, eax
00793E9D  44 8B C7                        mov r8d, edi
00793EA0  48 8B CE                        mov rcx, rsi
00793EA3  E8 84 F0 FF FF                  call 0x140792f2c
00793EA8  44 8B C8                        mov r9d, eax
00793EAB  85 C0                           test eax, eax
00793EAD  0F 84 AF 04 00 00               je 0x140794362
00793EB3  48 8B CB                        mov rcx, rbx
00793EB6  E8 F9 9E E5 FF                  call 0x1405eddb4
00793EBB  41 8B F9                        mov edi, r9d
00793EBE  E9 9B FE FF FF                  jmp 0x140793d5e
00793EC3  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00793EC7  48 3B 43 08                     cmp rax, qword ptr [rbx + 8]
00793ECB  0F 84 83 06 00 00               je 0x140794554
00793ED1  0F B7 08                        movzx ecx, word ptr [rax]
00793ED4  BA FF 03 00 00                  mov edx, 0x3ff
00793ED9  48 83 C0 02                     add rax, 2
00793EDD  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00793EE1  B8 00 24 00 00                  mov eax, 0x2400
00793EE6  03 C1                           add eax, ecx
00793EE8  66 3B C2                        cmp ax, dx
00793EEB  0F 87 63 06 00 00               ja 0x140794554
00793EF1  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00793EF5  81 C7 09 28 FF FF               add edi, 0xffff2809
00793EFB  C1 E7 0A                        shl edi, 0xa
00793EFE  03 F9                           add edi, ecx
00793F00  48 63 CF                        movsxd rcx, edi
00793F03  48 C1 F9 07                     sar rcx, 7
00793F07  44 8A 24 01                     mov r12b, byte ptr [rcx + rax]
00793F0B  E9 4E FE FF FF                  jmp 0x140793d5e
00793F10  48 8B CB                        mov rcx, rbx
00793F13  E8 E0 99 E5 FF                  call 0x1405ed8f8
00793F18  8B C8                           mov ecx, eax
00793F1A  44 8B C8                        mov r9d, eax
00793F1D  E8 3E 98 E5 FF                  call 0x1405ed760
00793F22  84 C0                           test al, al
00793F24  74 40                           je 0x140793f66
00793F26  48 8B CB                        mov rcx, rbx
00793F29  E8 86 9E E5 FF                  call 0x1405eddb4
00793F2E  41 8B D6                        mov edx, r14d
00793F31  41 8B C9                        mov ecx, r9d
00793F34  E8 EF 97 E5 FF                  call 0x1405ed728
00793F39  EB 29                           jmp 0x140793f64
00793F3B  48 8B CB                        mov rcx, rbx
00793F3E  E8 B5 99 E5 FF                  call 0x1405ed8f8
00793F43  44 8B C8                        mov r9d, eax
00793F46  8D 88 00 EF FF FF               lea ecx, [rax - 0x1100]
00793F4C  83 F9 12                        cmp ecx, 0x12
00793F4F  77 15                           ja 0x140793f66
00793F51  48 8B CB                        mov rcx, rbx
00793F54  E8 5B 9E E5 FF                  call 0x1405eddb4
00793F59  41 8B D6                        mov edx, r14d
00793F5C  41 8B C9                        mov ecx, r9d
00793F5F  E8 94 97 E5 FF                  call 0x1405ed6f8
00793F64  8B F8                           mov edi, eax
00793F66  8B D7                           mov edx, edi
00793F68  48 8B CB                        mov rcx, rbx
00793F6B  E8 28 98 E5 FF                  call 0x1405ed798
00793F70  84 C0                           test al, al
00793F72  0F 85 97 01 00 00               jne 0x14079410f
00793F78  B8 23 00 00 C0                  mov eax, 0xc0000023
00793F7D  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00793F82  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00793F87  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00793F8C  48 83 C4 20                     add rsp, 0x20
00793F90  41 5F                           pop r15
00793F92  41 5E                           pop r14
00793F94  41 5D                           pop r13
00793F96  41 5C                           pop r12
00793F98  5F                              pop rdi
00793F99  C3                              ret
00793F9A  CC                              int3
00793F9B  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00793F9F  4C 8B 4B 08                     mov r9, qword ptr [rbx + 8]
00793FA3  4D 3B C1                        cmp r8, r9
00793FA6  74 BE                           je 0x140793f66
00793FA8  41 0F B7 10                     movzx edx, word ptr [r8]
00793FAC  4D 8D 50 02                     lea r10, [r8 + 2]
00793FB0  41 8B CE                        mov ecx, r14d
00793FB3  4C 89 53 10                     mov qword ptr [rbx + 0x10], r10
00793FB7  E8 3C 97 E5 FF                  call 0x1405ed6f8
00793FBC  8B F8                           mov edi, eax
00793FBE  85 C0                           test eax, eax
00793FC0  74 22                           je 0x140793fe4
00793FC2  4D 3B D1                        cmp r10, r9
00793FC5  74 9F                           je 0x140793f66
00793FC7  41 0F B7 12                     movzx edx, word ptr [r10]
00793FCB  49 8D 42 02                     lea rax, [r10 + 2]
00793FCF  8B CF                           mov ecx, edi
00793FD1  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00793FD5  E8 4E 97 E5 FF                  call 0x1405ed728
00793FDA  85 C0                           test eax, eax
00793FDC  75 86                           jne 0x140793f64
00793FDE  4C 89 53 10                     mov qword ptr [rbx + 0x10], r10
00793FE2  EB 82                           jmp 0x140793f66
00793FE4  4C 89 43 10                     mov qword ptr [rbx + 0x10], r8
00793FE8  EB 49                           jmp 0x140794033
00793FEA  80 7E 70 01                     cmp byte ptr [rsi + 0x70], 1
00793FEE  74 4B                           je 0x14079403b
00793FF0  41 8B CE                        mov ecx, r14d
00793FF3  41 8B FE                        mov edi, r14d
00793FF6  E8 65 97 E5 FF                  call 0x1405ed760
00793FFB  84 C0                           test al, al
00793FFD  0F 84 63 FF FF FF               je 0x140793f66
00794003  4C 8B 53 10                     mov r10, qword ptr [rbx + 0x10]
00794007  4C 3B 53 08                     cmp r10, qword ptr [rbx + 8]
0079400B  0F 84 55 FF FF FF               je 0x140793f66
00794011  41 0F B7 12                     movzx edx, word ptr [r10]
00794015  49 8D 42 02                     lea rax, [r10 + 2]
00794019  41 8B CE                        mov ecx, r14d
0079401C  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00794020  E8 03 97 E5 FF                  call 0x1405ed728
00794025  8B F8                           mov edi, eax
00794027  85 C0                           test eax, eax
00794029  0F 85 37 FF FF FF               jne 0x140793f66
0079402F  4C 89 53 10                     mov qword ptr [rbx + 0x10], r10
00794033  41 8B FE                        mov edi, r14d
00794036  E9 2B FF FF FF                  jmp 0x140793f66
0079403B  41 81 C6 00 54 FF FF            add r14d, 0xffff5400
00794042  B8 27 AE 74 6F                  mov eax, 0x6f74ae27
00794047  41 F7 EE                        imul r14d
0079404A  41 8B F6                        mov esi, r14d
0079404D  45 33 C9                        xor r9d, r9d
00794050  C1 FA 08                        sar edx, 8
00794053  45 33 C0                        xor r8d, r8d
00794056  8B C2                           mov eax, edx
00794058  48 8B CB                        mov rcx, rbx
0079405B  C1 E8 1F                        shr eax, 0x1f
0079405E  03 D0                           add edx, eax
00794060  69 C2 4C 02 00 00               imul eax, edx, 0x24c
00794066  2B F0                           sub esi, eax
00794068  B8 00 11 00 00                  mov eax, 0x1100
0079406D  66 03 D0                        add dx, ax
00794070  0F B7 D2                        movzx edx, dx
00794073  E8 E0 97 E5 FF                  call 0x1405ed858
00794078  84 C0                           test al, al
0079407A  0F 84 F8 FE FF FF               je 0x140793f78
00794080  B9 61 11 00 00                  mov ecx, 0x1161
00794085  BD 93 24 49 92                  mov ebp, 0x92492493
0079408A  8B C5                           mov eax, ebp
0079408C  45 33 C9                        xor r9d, r9d
0079408F  F7 EE                           imul esi
00794091  45 33 C0                        xor r8d, r8d
00794094  8D 3C 16                        lea edi, [rsi + rdx]
00794097  C1 FF 04                        sar edi, 4
0079409A  8B C7                           mov eax, edi
0079409C  C1 E8 1F                        shr eax, 0x1f
0079409F  03 F8                           add edi, eax
007940A1  66 03 F9                        add di, cx
007940A4  48 8B CB                        mov rcx, rbx
007940A7  0F B7 D7                        movzx edx, di
007940AA  E8 A9 97 E5 FF                  call 0x1405ed858
007940AF  84 C0                           test al, al
007940B1  0F 84 C1 FE FF FF               je 0x140793f78
007940B7  8B C5                           mov eax, ebp
007940B9  41 F7 EE                        imul r14d
007940BC  41 03 D6                        add edx, r14d
007940BF  C1 FA 04                        sar edx, 4
007940C2  8B C2                           mov eax, edx
007940C4  C1 E8 1F                        shr eax, 0x1f
007940C7  03 D0                           add edx, eax
007940C9  6B C2 1C                        imul eax, edx, 0x1c
007940CC  44 2B F0                        sub r14d, eax
007940CF  B8 A7 11 00 00                  mov eax, 0x11a7
007940D4  41 03 C6                        add eax, r14d
007940D7  66 41 F7 DE                     neg r14w
007940DB  66 1B F6                        sbb si, si
007940DE  66 23 F0                        and si, ax
007940E1  74 19                           je 0x1407940fc
007940E3  0F B7 D6                        movzx edx, si
007940E6  45 33 C9                        xor r9d, r9d
007940E9  45 33 C0                        xor r8d, r8d
007940EC  E8 67 97 E5 FF                  call 0x1405ed858
007940F1  84 C0                           test al, al
007940F3  0F 84 7F FE FF FF               je 0x140793f78
007940F9  0F B7 FE                        movzx edi, si
007940FC  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00794100  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
00794104  0F B7 C7                        movzx eax, di
00794107  89 43 58                        mov dword ptr [rbx + 0x58], eax
0079410A  66 44 89 6B 5C                  mov word ptr [rbx + 0x5c], r13w
0079410F  33 C0                           xor eax, eax
00794111  E9 67 FE FF FF                  jmp 0x140793f7d
00794116  48 8B CB                        mov rcx, rbx
00794119  41 F6 C7 BF                     test r15b, 0xbf
0079411D  0F 84 A2 03 00 00               je 0x1407944c5
00794123  E8 D0 97 E5 FF                  call 0x1405ed8f8
00794128  44 8A 63 48                     mov r12b, byte ptr [rbx + 0x48]
0079412C  45 84 E4                        test r12b, r12b
0079412F  74 0E                           je 0x14079413f
00794131  41 80 FC 3F                     cmp r12b, 0x3f
00794135  74 08                           je 0x14079413f
00794137  8A 53 49                        mov dl, byte ptr [rbx + 0x49]
0079413A  F6 C2 BF                        test dl, 0xbf
0079413D  75 20                           jne 0x14079415f
0079413F  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00794143  8A 53 49                        mov dl, byte ptr [rbx + 0x49]
00794146  48 83 C0 02                     add rax, 2
0079414A  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
0079414E  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00794151  89 43 58                        mov dword ptr [rbx + 0x58], eax
00794154  44 88 63 5C                     mov byte ptr [rbx + 0x5c], r12b
00794158  88 53 5D                        mov byte ptr [rbx + 0x5d], dl
0079415B  4C 89 6B 60                     mov qword ptr [rbx + 0x60], r13
0079415F  41 80 FF 80                     cmp r15b, 0x80
00794163  0F 84 4C 03 00 00               je 0x1407944b5
00794169  8A 4B 5D                        mov cl, byte ptr [rbx + 0x5d]
0079416C  0A 4B 5C                        or cl, byte ptr [rbx + 0x5c]
0079416F  80 C1 40                        add cl, 0x40
00794172  F6 C1 BF                        test cl, 0xbf
00794175  0F 84 3A 03 00 00               je 0x1407944b5
0079417B  45 84 E4                        test r12b, r12b
0079417E  0F 84 D7 02 00 00               je 0x14079445b
00794184  41 80 FC 3F                     cmp r12b, 0x3f
00794188  0F 84 CD 02 00 00               je 0x14079445b
0079418E  84 D2                           test dl, dl
00794190  0F 84 B1 01 00 00               je 0x140794347
00794196  80 FA 40                        cmp dl, 0x40
00794199  0F 84 1F 01 00 00               je 0x1407942be
0079419F  40 8A D5                        mov dl, bpl
007941A2  48 8B CB                        mov rcx, rbx
007941A5  E8 D2 98 E5 FF                  call 0x1405eda7c
007941AA  84 C0                           test al, al
007941AC  74 15                           je 0x1407941c3
007941AE  45 8A CF                        mov r9b, r15b
007941B1  44 8A C5                        mov r8b, bpl
007941B4  8B D7                           mov edx, edi
007941B6  48 8B CB                        mov rcx, rbx
007941B9  E8 92 98 E5 FF                  call 0x1405eda50
007941BE  E9 AD FD FF FF                  jmp 0x140793f70
007941C3  44 8A 63 5C                     mov r12b, byte ptr [rbx + 0x5c]
007941C7  45 84 E4                        test r12b, r12b
007941CA  74 0C                           je 0x1407941d8
007941CC  41 80 FC 3F                     cmp r12b, 0x3f
007941D0  74 06                           je 0x1407941d8
007941D2  80 7B 5D 40                     cmp byte ptr [rbx + 0x5d], 0x40
007941D6  75 72                           jne 0x14079424a
007941D8  8B 53 58                        mov edx, dword ptr [rbx + 0x58]
007941DB  44 8B C7                        mov r8d, edi
007941DE  48 8B CE                        mov rcx, rsi
007941E1  E8 46 ED FF FF                  call 0x140792f2c
007941E6  4C 63 D0                        movsxd r10, eax
007941E9  85 C0                           test eax, eax
007941EB  74 4A                           je 0x140794237
007941ED  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
007941F1  4D 8B CA                        mov r9, r10
007941F4  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
007941F8  41 83 E1 7F                     and r9d, 0x7f
007941FC  49 8B D2                        mov rdx, r10
007941FF  48 C1 FA 07                     sar rdx, 7
00794203  44 0F B6 04 0A                  movzx r8d, byte ptr [rdx + rcx]
00794208  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0079420C  49 C1 E0 07                     shl r8, 7
00794210  4D 03 C1                        add r8, r9
00794213  41 8A 54 08 80                  mov dl, byte ptr [r8 + rcx - 0x80]
00794218  66 44 89 50 FE                  mov word ptr [rax - 2], r10w
0079421D  8A CA                           mov cl, dl
0079421F  80 E1 C0                        and cl, 0xc0
00794222  44 89 53 58                     mov dword ptr [rbx + 0x58], r10d
00794226  80 E2 3F                        and dl, 0x3f
00794229  88 4B 5D                        mov byte ptr [rbx + 0x5d], cl
0079422C  80 F9 40                        cmp cl, 0x40
0079422F  88 53 5C                        mov byte ptr [rbx + 0x5c], dl
00794232  E9 11 02 00 00                  jmp 0x140794448
00794237  45 84 E4                        test r12b, r12b
0079423A  0F 84 6E FF FF FF               je 0x1407941ae
00794240  41 80 FC 3F                     cmp r12b, 0x3f
00794244  0F 84 64 FF FF FF               je 0x1407941ae
0079424A  44 3A E5                        cmp r12b, bpl
0079424D  0F 86 5B FF FF FF               jbe 0x1407941ae
00794253  44 3A 66 74                     cmp r12b, byte ptr [rsi + 0x74]
00794257  75 12                           jne 0x14079426b
00794259  40 3A 6E 72                     cmp bpl, byte ptr [rsi + 0x72]
0079425D  72 3D                           jb 0x14079429c
0079425F  40 3A 6E 73                     cmp bpl, byte ptr [rsi + 0x73]
00794263  0F 85 45 FF FF FF               jne 0x1407941ae
00794269  EB 0C                           jmp 0x140794277
0079426B  44 3A 66 76                     cmp r12b, byte ptr [rsi + 0x76]
0079426F  75 2B                           jne 0x14079429c
00794271  40 3A 6E 75                     cmp bpl, byte ptr [rsi + 0x75]
00794275  75 25                           jne 0x14079429c
00794277  48 8B CB                        mov rcx, rbx
0079427A  4C 8B E6                        mov r12, rsi
0079427D  E8 9E 98 E5 FF                  call 0x1405edb20
00794282  8B D0                           mov edx, eax
00794284  45 8B C6                        mov r8d, r14d
00794287  48 8B CE                        mov rcx, rsi
0079428A  E8 9D EC FF FF                  call 0x140792f2c
0079428F  85 C0                           test eax, eax
00794291  0F 84 17 FF FF FF               je 0x1407941ae
00794297  E9 03 01 00 00                  jmp 0x14079439f
0079429C  48 8B CB                        mov rcx, rbx
0079429F  E8 50 98 E5 FF                  call 0x1405edaf4
007942A4  8B D0                           mov edx, eax
007942A6  44 8B C7                        mov r8d, edi
007942A9  48 8B CE                        mov rcx, rsi
007942AC  E8 7B EC FF FF                  call 0x140792f2c
007942B1  85 C0                           test eax, eax
007942B3  0F 85 44 01 00 00               jne 0x1407943fd
007942B9  E9 F0 FE FF FF                  jmp 0x1407941ae
007942BE  8B 53 58                        mov edx, dword ptr [rbx + 0x58]
007942C1  44 8B C7                        mov r8d, edi
007942C4  48 8B CE                        mov rcx, rsi
007942C7  E8 60 EC FF FF                  call 0x140792f2c
007942CC  4C 63 D0                        movsxd r10, eax
007942CF  85 C0                           test eax, eax
007942D1  74 74                           je 0x140794347
007942D3  48 8B CB                        mov rcx, rbx
007942D6  E8 D9 9A E5 FF                  call 0x1405eddb4
007942DB  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
007942DF  4D 8B CA                        mov r9, r10
007942E2  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
007942E6  41 83 E1 7F                     and r9d, 0x7f
007942EA  49 8B D2                        mov rdx, r10
007942ED  48 C1 FA 07                     sar rdx, 7
007942F1  44 0F B6 04 0A                  movzx r8d, byte ptr [rdx + rcx]
007942F6  41 8B D2                        mov edx, r10d
007942F9  49 C1 E0 07                     shl r8, 7
007942FD  48 8B CB                        mov rcx, rbx
00794300  4D 03 C1                        add r8, r9
00794303  45 8A 44 00 80                  mov r8b, byte ptr [r8 + rax - 0x80]
00794308  45 8A C8                        mov r9b, r8b
0079430B  41 80 E0 3F                     and r8b, 0x3f
0079430F  41 80 E1 C0                     and r9b, 0xc0
00794313  E8 40 95 E5 FF                  call 0x1405ed858
00794318  84 C0                           test al, al
0079431A  0F 84 58 FC FF FF               je 0x140793f78
00794320  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00794324  48 83 C0 02                     add rax, 2
00794328  4C 89 6B 60                     mov qword ptr [rbx + 0x60], r13
0079432C  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
00794330  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00794333  89 43 58                        mov dword ptr [rbx + 0x58], eax
00794336  8A 43 48                        mov al, byte ptr [rbx + 0x48]
00794339  88 43 5C                        mov byte ptr [rbx + 0x5c], al
0079433C  8A 43 49                        mov al, byte ptr [rbx + 0x49]
0079433F  88 43 5D                        mov byte ptr [rbx + 0x5d], al
00794342  E9 C8 FD FF FF                  jmp 0x14079410f
00794347  44 3A E5                        cmp r12b, bpl
0079434A  76 16                           jbe 0x140794362
0079434C  44 3A 66 74                     cmp r12b, byte ptr [rsi + 0x74]
00794350  75 25                           jne 0x140794377
00794352  40 3A 6E 72                     cmp bpl, byte ptr [rsi + 0x72]
00794356  0F 82 84 00 00 00               jb 0x1407943e0
0079435C  40 3A 6E 73                     cmp bpl, byte ptr [rsi + 0x73]
00794360  74 21                           je 0x140794383
00794362  45 8A CF                        mov r9b, r15b
00794365  44 8A C5                        mov r8b, bpl
00794368  8B D7                           mov edx, edi
0079436A  48 8B CB                        mov rcx, rbx
0079436D  E8 E6 94 E5 FF                  call 0x1405ed858
00794372  E9 F9 FB FF FF                  jmp 0x140793f70
00794377  44 3A 66 76                     cmp r12b, byte ptr [rsi + 0x76]
0079437B  75 63                           jne 0x1407943e0
0079437D  40 3A 6E 75                     cmp bpl, byte ptr [rsi + 0x75]
00794381  75 5D                           jne 0x1407943e0
00794383  48 8B CB                        mov rcx, rbx
00794386  4C 8B E6                        mov r12, rsi
00794389  E8 92 97 E5 FF                  call 0x1405edb20
0079438E  8B D0                           mov edx, eax
00794390  45 8B C6                        mov r8d, r14d
00794393  48 8B CE                        mov rcx, rsi
00794396  E8 91 EB FF FF                  call 0x140792f2c
0079439B  85 C0                           test eax, eax
0079439D  74 C3                           je 0x140794362
0079439F  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
007943A3  4C 63 C8                        movsxd r9, eax
007943A6  49 8B D1                        mov rdx, r9
007943A9  41 83 E1 7F                     and r9d, 0x7f
007943AD  48 C1 FA 07                     sar rdx, 7
007943B1  44 0F B6 04 0A                  movzx r8d, byte ptr [rdx + rcx]
007943B6  8B D0                           mov edx, eax
007943B8  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
007943BC  49 C1 E0 07                     shl r8, 7
007943C0  4D 03 C1                        add r8, r9
007943C3  45 8A 44 08 80                  mov r8b, byte ptr [r8 + rcx - 0x80]
007943C8  48 8B CB                        mov rcx, rbx
007943CB  41 8A F8                        mov dil, r8b
007943CE  41 80 E0 3F                     and r8b, 0x3f
007943D2  40 80 E7 C0                     and dil, 0xc0
007943D6  44 8A CF                        mov r9b, dil
007943D9  E8 5E 99 E5 FF                  call 0x1405edd3c
007943DE  EB 5C                           jmp 0x14079443c
007943E0  48 8B CB                        mov rcx, rbx
007943E3  E8 0C 97 E5 FF                  call 0x1405edaf4
007943E8  8B D0                           mov edx, eax
007943EA  44 8B C7                        mov r8d, edi
007943ED  48 8B CE                        mov rcx, rsi
007943F0  E8 37 EB FF FF                  call 0x140792f2c
007943F5  85 C0                           test eax, eax
007943F7  0F 84 65 FF FF FF               je 0x140794362
007943FD  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00794401  4C 63 C8                        movsxd r9, eax
00794404  49 8B D1                        mov rdx, r9
00794407  41 83 E1 7F                     and r9d, 0x7f
0079440B  48 C1 FA 07                     sar rdx, 7
0079440F  44 0F B6 04 0A                  movzx r8d, byte ptr [rdx + rcx]
00794414  8B D0                           mov edx, eax
00794416  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0079441A  49 C1 E0 07                     shl r8, 7
0079441E  4D 03 C1                        add r8, r9
00794421  45 8A 44 08 80                  mov r8b, byte ptr [r8 + rcx - 0x80]
00794426  48 8B CB                        mov rcx, rbx
00794429  41 8A F8                        mov dil, r8b
0079442C  41 80 E0 3F                     and r8b, 0x3f
00794430  40 80 E7 C0                     and dil, 0xc0
00794434  44 8A CF                        mov r9b, dil
00794437  E8 80 98 E5 FF                  call 0x1405edcbc
0079443C  84 C0                           test al, al
0079443E  0F 84 34 FB FF FF               je 0x140793f78
00794444  40 80 FF 40                     cmp dil, 0x40
00794448  0F 85 C1 FC FF FF               jne 0x14079410f
0079444E  48 8B CB                        mov rcx, rbx
00794451  E8 1A 97 E5 FF                  call 0x1405edb70
00794456  E9 B4 FC FF FF                  jmp 0x14079410f
0079445B  8B 53 58                        mov edx, dword ptr [rbx + 0x58]
0079445E  44 8B C7                        mov r8d, edi
00794461  48 8B CE                        mov rcx, rsi
00794464  E8 C3 EA FF FF                  call 0x140792f2c
00794469  4C 63 C8                        movsxd r9, eax
0079446C  85 C0                           test eax, eax
0079446E  0F 84 EE FE FF FF               je 0x140794362
00794474  48 8B CB                        mov rcx, rbx
00794477  E8 38 99 E5 FF                  call 0x1405eddb4
0079447C  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00794480  4D 8B C1                        mov r8, r9
00794483  41 83 E0 7F                     and r8d, 0x7f
00794487  49 8B C9                        mov rcx, r9
0079448A  48 C1 F9 07                     sar rcx, 7
0079448E  41 8B F9                        mov edi, r9d
00794491  0F B6 14 01                     movzx edx, byte ptr [rcx + rax]
00794495  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00794499  48 C1 E2 07                     shl rdx, 7
0079449D  49 03 D0                        add rdx, r8
007944A0  40 8A 6C 02 80                  mov bpl, byte ptr [rdx + rax - 0x80]
007944A5  44 8A FD                        mov r15b, bpl
007944A8  41 80 E7 C0                     and r15b, 0xc0
007944AC  40 80 E5 3F                     and bpl, 0x3f
007944B0  E9 AD FE FF FF                  jmp 0x140794362
007944B5  40 8A D5                        mov dl, bpl
007944B8  48 8B CB                        mov rcx, rbx
007944BB  E8 BC 95 E5 FF                  call 0x1405eda7c
007944C0  E9 E9 FC FF FF                  jmp 0x1407941ae
007944C5  45 8A CF                        mov r9b, r15b
007944C8  44 8A C5                        mov r8b, bpl
007944CB  8B D7                           mov edx, edi
007944CD  E8 86 93 E5 FF                  call 0x1405ed858
007944D2  84 C0                           test al, al
007944D4  0F 84 9E FA FF FF               je 0x140793f78
007944DA  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
007944DE  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
007944E2  89 7B 58                        mov dword ptr [rbx + 0x58], edi
007944E5  40 88 6B 5C                     mov byte ptr [rbx + 0x5c], bpl
007944E9  44 88 7B 5D                     mov byte ptr [rbx + 0x5d], r15b
007944ED  E9 1D FC FF FF                  jmp 0x14079410f
007944F2  83 F9 3F                        cmp ecx, 0x3f
007944F5  0F 85 67 FE FF FF               jne 0x140794362
007944FB  85 FF                           test edi, edi
007944FD  75 55                           jne 0x140794554
007944FF  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00794503  48 39 43 10                     cmp qword ptr [rbx + 0x10], rax
00794507  75 4B                           jne 0x140794554
00794509  E9 54 FE FF FF                  jmp 0x140794362
0079450E  44 38 6E 71                     cmp byte ptr [rsi + 0x71], r13b
00794512  74 40                           je 0x140794554
00794514  45 33 C9                        xor r9d, r9d
00794517  45 33 C0                        xor r8d, r8d
0079451A  8B D7                           mov edx, edi
0079451C  48 8B CB                        mov rcx, rbx
0079451F  E8 34 93 E5 FF                  call 0x1405ed858
00794524  84 C0                           test al, al
00794526  0F 84 4C FA FF FF               je 0x140793f78
0079452C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00794530  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
00794534  89 7B 58                        mov dword ptr [rbx + 0x58], edi
00794537  E9 CE FB FF FF                  jmp 0x14079410a
0079453C  4C 8B C3                        mov r8, rbx
0079453F  8B D7                           mov edx, edi
00794541  48 8B CE                        mov rcx, rsi
00794544  E8 D7 E8 FF FF                  call 0x140792e20
00794549  E9 2F FA FF FF                  jmp 0x140793f7d
0079454E  44 38 6E 71                     cmp byte ptr [rsi + 0x71], r13b
00794552  75 0A                           jne 0x14079455e
00794554  B8 17 07 00 C0                  mov eax, 0xc0000717
00794559  E9 1F FA FF FF                  jmp 0x140793f7d
0079455E  8B D7                           mov edx, edi
00794560  48 8B CB                        mov rcx, rbx
00794563  E8 30 92 E5 FF                  call 0x1405ed798
00794568  EB BA                           jmp 0x140794524
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Normalization__NormalizeCharacter(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r13 = 0;
loc_00793D5E:
    if (a3 == 0) goto loc_00793F66;
loc_00793D6A:
    if (a3 == 0) goto loc_0079455E;
    a1 = (unsigned int)(((unsigned int)(a3)) - (251));
    if (condition_is_equal) goto loc_0079454E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00794554;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0079453C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00793EC3;
    if (((unsigned int)(a1)) != 1) goto loc_00793E3C;
    if (((unsigned int)((unsigned int)(a2))) >= 0xAC00ULL) goto loc_00793E0A;
    if (((unsigned int)((unsigned int)(a2) - 4352)) <= 18) goto loc_00793F9B;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))) - 4449)) <= 20) goto loc_00793F3B;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))) - 4520)) <= 26) goto loc_00793F10;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (13));
    if ((((unsigned int)(result)) & (0xFFFFFEFFULL)) != 0) goto loc_00793E02;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))) - 4447)) > ((unsigned int)(a1))) goto loc_00793E02;
    goto loc_00793D6A;
loc_00793E02:
    goto loc_00793D5E;
loc_00793E0A:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))) < 0xD7A4ULL) goto loc_00793FEA;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))) - 55216)) <= 22) goto loc_00793E31;
    v_r12 = 251;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))) - 55243)) <= 48) {
        v_r12 = 0;
    }
    goto loc_00793D5E;
loc_00793E3C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2)))))))) & (127));
    a1 = (a3) << (7);
    a1 = (a1) + (result);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128)) == 0) goto loc_00794514;
    v_r15 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128))) & (192));
    v_rbp = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128))) & (63));
    if (condition_is_equal) goto loc_00793E76;
    if (((unsigned __int8)(v_rbp)) != 63) goto loc_00794116;
loc_00793E76:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128)))) - (127));
    if (condition_is_equal) goto loc_0079450E;
    a1 = (unsigned int)((a1) - (64));
    if (condition_is_equal) goto loc_0079453C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_007944F2;
    result = NormBuffer__GetLastChar(a4, *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128), a3, a4);
    result = Normalization__CanCombinableCharactersCombine(a1, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), a4);
    if ((unsigned int)(result) == 0) goto loc_00794362;
    result = NormBuffer__RewindOutputCharacter(a4, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    goto loc_00793D5E;
loc_00793EC3:
    if ((*(unsigned __int64 *)(a4 + 16)) == (*(unsigned __int64 *)(a4 + 8))) goto loc_00794554;
    result = (*(unsigned __int64 *)(a4 + 16)) + (2);
    *(unsigned __int64 *)(a4 + 16) = result;
    result = (unsigned int)(((unsigned int)(0x2400ULL)) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 16)))));
    if (((unsigned __int16)(result)) > ((unsigned __int16)((unsigned int)(0x3FFULL)))) goto loc_00794554;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) + (0xFFFF2809ULL));
    v_rdi = (unsigned int)((v_rdi) << (10));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 16)))));
    a1 = ((int)((unsigned int)(v_rdi))) >> (7);
    goto loc_00793D5E;
loc_00793F10:
    result = NormBuffer__GetLastChar(a4, (unsigned int)(0x3FFULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    result = IsHangulLV((unsigned int)((unsigned int)(result)), (unsigned int)(0x3FFULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    if ((unsigned __int8)(result) == 0) goto loc_00793F66;
    result = NormBuffer__RewindOutputCharacter(a4, (unsigned int)(0x3FFULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    result = ComposeHangulLVT((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    goto loc_00793F64;
loc_00793F3B:
    result = NormBuffer__GetLastChar(a4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    if (((unsigned int)(result - 4352)) > 18) goto loc_00793F66;
    result = NormBuffer__RewindOutputCharacter(a4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
    result = ComposeHangulLV((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
loc_00793F64:
loc_00793F66:
    result = NormBuffer__Append(a4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))))), (unsigned int)((unsigned int)(result)));
loc_00793F70:
    if ((unsigned __int8)(result) != 0) goto loc_0079410F;
loc_00793F78:
loc_00793F7D:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xC0000023ULL);
loc_00793F9B:
    if ((*(unsigned __int64 *)(v_stack_p8 + 16)) == (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00793F66;
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_stack_p8 + 16) + 2;
    result = ComposeHangulLV((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16)), *(unsigned __int64 *)(v_stack_p8 + 16), *(unsigned __int64 *)(v_stack_p8 + 8));
    if ((unsigned int)(result) == 0) goto loc_00793FE4;
    if ((*(unsigned __int64 *)(v_stack_p8 + 16) + 2) == (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00793F66;
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_stack_p8 + 16) + 2 + 2;
    result = ComposeHangulLVT((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 2), *(unsigned __int64 *)(v_stack_p8 + 16), *(unsigned __int64 *)(v_stack_p8 + 8));
    if ((unsigned int)(result) != 0) goto loc_00793F64;
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_stack_p8 + 16) + 2;
    goto loc_00793F66;
loc_00793FE4:
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_stack_p8 + 16);
    goto loc_00794033;
loc_00793FEA:
    if ((*(unsigned __int8 *)(v_stack_p18 + 112)) == 1) goto loc_0079403B;
    result = IsHangulLV((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 2), *(unsigned __int64 *)(v_stack_p8 + 16), *(unsigned __int64 *)(v_stack_p8 + 8));
    if ((unsigned __int8)(result) == 0) goto loc_00793F66;
    if ((*(unsigned __int64 *)(v_stack_p8 + 16)) == (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00793F66;
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_stack_p8 + 16) + 2;
    result = ComposeHangulLVT((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16)), *(unsigned __int64 *)(v_stack_p8 + 16), *(unsigned __int64 *)(v_stack_p8 + 8));
    if ((unsigned int)(result) != 0) goto loc_00793F66;
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_stack_p8 + 16);
loc_00794033:
    goto loc_00793F66;
loc_0079403B:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) + (0xFFFF5400ULL));
    a4 = 0;
    a2 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16))) >> (8));
    a3 = 0;
    result = (unsigned int)(((unsigned int)(a2)) >> (31));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    result = (unsigned int)((result) * (a2));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(result)));
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)((unsigned int)(0x1100ULL))));
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned __int16)(a2), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
    a4 = 0;
    a3 = 0;
    v_rdi = (unsigned int)((v_rsi + (unsigned __int16)(a2) * 1) >> (4));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (31));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(result)));
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0x1161ULL))));
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned __int16)(v_rdi), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
    a2 = (unsigned int)(((unsigned __int16)(v_rdi)) + ((unsigned int)(v_r14)));
    a2 = (unsigned int)((a2) >> (4));
    result = (unsigned int)(((unsigned int)(a2)) >> (31));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    result = (unsigned int)((result) * (a2));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)(0x11A7ULL)) + ((unsigned int)(v_r14)));
    v_r14 = (unsigned __int16)(-(v_r14));
    v_rsi = (unsigned __int16)((v_rsi) & ((unsigned __int16)(result)));
    if (condition_is_equal) goto loc_007940FC;
    a4 = 0;
    a3 = 0;
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned __int16)(v_rsi), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
loc_007940FC:
    *(unsigned __int64 *)(v_stack_p8 + 80) = *(unsigned __int64 *)(v_stack_p8 + 40);
    *(unsigned int *)(v_stack_p8 + 88) = (unsigned int)((unsigned __int16)((unsigned __int16)(v_rsi)));
loc_0079410A:
    *(unsigned __int16 *)(v_stack_p8 + 92) = 0;
loc_0079410F:
    result = 0;
    goto loc_00793F7D;
loc_00794116:
    if ((((unsigned __int8)(v_r15)) & (191)) == 0) goto loc_007944C5;
    result = NormBuffer__GetLastChar(v_stack_p8, (unsigned __int16)(v_rsi), a3, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 72)) == 0) goto loc_0079413F;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 72))) == 63) goto loc_0079413F;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 73))) & (191)) == 0) {
        result = *(unsigned __int64 *)(v_stack_p8 + 64);
        a2 = *(unsigned __int8 *)(v_stack_p8 + 73);
        result = (result) + (2);
        *(unsigned __int64 *)(v_stack_p8 + 80) = result;
        result = *(unsigned int *)(v_stack_p8 + 56);
        *(unsigned int *)(v_stack_p8 + 88) = (unsigned int)(result);
        *(unsigned __int8 *)(v_stack_p8 + 92) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 72));
        *(unsigned __int8 *)(v_stack_p8 + 93) = (unsigned __int8)(a2);
        *(unsigned __int64 *)(v_stack_p8 + 96) = 0;
    }
    if (((unsigned __int8)(v_r15)) == 128) goto loc_007944B5;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 93)) | (*(unsigned __int8 *)(v_stack_p8 + 92)));
    a1 = (unsigned __int8)((a1) + (64));
    if ((((unsigned __int8)(a1)) & (191)) == 0) goto loc_007944B5;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 72)) == 0) goto loc_0079445B;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 72))) == 63) goto loc_0079445B;
    if ((unsigned __int8)(a2) == 0) goto loc_00794347;
    if (((unsigned __int8)(a2)) == 64) goto loc_007942BE;
    result = NormBuffer__IsBlocked(v_stack_p8, (unsigned __int8)((unsigned int)(0x92492493ULL)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007941C3;
loc_007941AE:
    result = NormBuffer__InsertAtBlockedLocation(v_stack_p8, (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), (unsigned __int8)((unsigned int)(0x92492493ULL)), (unsigned __int8)(v_r15));
    goto loc_00793F70;
loc_007941C3:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92)) == 0) goto loc_007941D8;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92))) == 63) goto loc_007941D8;
    if ((*(unsigned __int8 *)(v_stack_p8 + 93)) != 64) goto loc_0079424A;
loc_007941D8:
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)), (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), (unsigned __int8)(v_r15));
    if ((unsigned int)(result) == 0) goto loc_00794237;
    a4 = (unsigned int)(((int)((unsigned int)(result))) & (127));
    a2 = ((int)((unsigned int)(result))) >> (7);
    a3 = (*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rsi + 32) * 1)) << (7);
    a3 = (a3) + (a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 80) - 2) = (unsigned __int16)((int)((unsigned int)(result)));
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128))) & (192));
    *(unsigned int *)(v_stack_p8 + 88) = (unsigned int)((int)((unsigned int)(result)));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128)) & (63));
    *(unsigned __int8 *)(v_stack_p8 + 93) = (unsigned __int8)(a1);
    *(unsigned __int8 *)(v_stack_p8 + 92) = (unsigned __int8)(a2);
    goto loc_00794448;
loc_00794237:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92)) == 0) goto loc_007941AE;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92))) == 63) goto loc_007941AE;
loc_0079424A:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92))) <= ((unsigned __int8)((unsigned int)(0x92492493ULL)))) goto loc_007941AE;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92))) != (*(unsigned __int8 *)(v_rsi + 116))) goto loc_0079426B;
    if (((unsigned __int8)((unsigned int)(0x92492493ULL))) < (*(unsigned __int8 *)(v_rsi + 114))) goto loc_0079429C;
    if (((unsigned __int8)((unsigned int)(0x92492493ULL))) != (*(unsigned __int8 *)(v_rsi + 115))) goto loc_007941AE;
    goto loc_00794277;
loc_0079426B:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 92))) != (*(unsigned __int8 *)(v_rsi + 118))) goto loc_0079429C;
    if (((unsigned __int8)((unsigned int)(0x92492493ULL))) != (*(unsigned __int8 *)(v_rsi + 117))) goto loc_0079429C;
loc_00794277:
    result = NormBuffer__LastStartBasePair(v_stack_p8, a2, a3, a4);
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r14)), a4);
    if ((unsigned int)(result) == 0) goto loc_007941AE;
    goto loc_0079439F;
loc_0079429C:
    result = NormBuffer__LastStartBase(v_stack_p8, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r14)), a4);
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), a4);
    if ((unsigned int)(result) != 0) goto loc_007943FD;
    goto loc_007941AE;
loc_007942BE:
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)), (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), a4);
    if ((unsigned int)(result) == 0) goto loc_00794347;
    result = NormBuffer__RewindOutputCharacter(v_stack_p8, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)), (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), a4);
    a4 = (unsigned int)(((int)((unsigned int)(result))) & (127));
    a2 = ((int)((unsigned int)(result))) >> (7);
    a3 = (*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rsi + 32) * 1)) << (7);
    a3 = (a3) + (a4);
    a3 = (unsigned __int8)((*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128)) & (63));
    a4 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128))) & (192));
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned int)((unsigned int)((int)((unsigned int)(result)))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
    result = (*(unsigned __int64 *)(v_stack_p8 + 64)) + (2);
    *(unsigned __int64 *)(v_stack_p8 + 96) = 0;
    *(unsigned __int64 *)(v_stack_p8 + 80) = result;
    *(unsigned int *)(v_stack_p8 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 56)));
    *(unsigned __int8 *)(v_stack_p8 + 92) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 72));
    *(unsigned __int8 *)(v_stack_p8 + 93) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 73));
    goto loc_0079410F;
loc_00794347:
    if (((unsigned __int8)(v_rsi)) <= ((unsigned __int8)((unsigned int)(0x92492493ULL)))) goto loc_00794362;
    if (((unsigned __int8)(v_rsi)) != (*(unsigned __int8 *)(v_rsi + 116))) goto loc_00794377;
    if (((unsigned __int8)((unsigned int)(0x92492493ULL))) < (*(unsigned __int8 *)(v_rsi + 114))) goto loc_007943E0;
    if (((unsigned __int8)((unsigned int)(0x92492493ULL))) == (*(unsigned __int8 *)(v_rsi + 115))) goto loc_00794383;
loc_00794362:
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), (unsigned __int8)((unsigned int)(0x92492493ULL)), (unsigned __int8)(v_r15));
    goto loc_00793F70;
loc_00794377:
    if (((unsigned __int8)(v_rsi)) != (*(unsigned __int8 *)(v_rsi + 118))) goto loc_007943E0;
    if (((unsigned __int8)((unsigned int)(0x92492493ULL))) != (*(unsigned __int8 *)(v_rsi + 117))) goto loc_007943E0;
loc_00794383:
    result = NormBuffer__LastStartBasePair(v_stack_p8, (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), (unsigned __int8)((unsigned int)(0x92492493ULL)), (unsigned __int8)(v_r15));
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r14)), (unsigned __int8)(v_r15));
    if ((unsigned int)(result) == 0) goto loc_00794362;
loc_0079439F:
    a4 = (unsigned int)(((int)((unsigned int)(result))) & (127));
    a2 = ((int)((unsigned int)(result))) >> (7);
    a3 = (*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rsi + 32) * 1)) << (7);
    a3 = (a3) + (a4);
    a3 = (unsigned __int8)((*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128)) & (63));
    v_rdi = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128))) & (192));
    result = NormBuffer__ReplaceLastStartBasePair(v_stack_p8, (unsigned int)((unsigned int)(result)), a3, (unsigned __int8)(v_rdi));
    goto loc_0079443C;
loc_007943E0:
    result = NormBuffer__LastStartBase(v_stack_p8, (unsigned int)((unsigned int)(result)), a3, (unsigned __int8)(v_rdi));
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_rdi)), (unsigned __int8)(v_rdi));
    if ((unsigned int)(result) == 0) goto loc_00794362;
loc_007943FD:
    a4 = (unsigned int)(((int)((unsigned int)(result))) & (127));
    a2 = ((int)((unsigned int)(result))) >> (7);
    a3 = (*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rsi + 32) * 1)) << (7);
    a3 = (a3) + (a4);
    a3 = (unsigned __int8)((*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128)) & (63));
    v_rdi = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128))) & (192));
    result = NormBuffer__ReplaceLastStartBase(v_stack_p8, (unsigned int)((unsigned int)(result)), a3, (unsigned __int8)(v_rdi));
loc_0079443C:
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
loc_00794448:
    if (((unsigned __int8)(v_rdi)) != 64) goto loc_0079410F;
    result = NormBuffer__RecheckStartCombinations(v_stack_p8, (unsigned int)((unsigned int)(result)), a3, (unsigned __int8)(v_rdi));
    goto loc_0079410F;
loc_0079445B:
    result = Normalization__CanCombinableCharactersCombine(v_rsi, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)), (unsigned int)((unsigned int)(v_rdi)), (unsigned __int8)(v_rdi));
    if ((unsigned int)(result) == 0) goto loc_00794362;
    result = NormBuffer__RewindOutputCharacter(v_stack_p8, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)), (unsigned int)((unsigned int)(v_rdi)), (int)((unsigned int)(result)));
    a3 = (unsigned int)(((int)((unsigned int)(result))) & (127));
    a1 = ((int)((unsigned int)(result))) >> (7);
    a2 = (*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rsi + 32) * 1)) << (7);
    a2 = (a2) + (a3);
    v_r15 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128))) & (192));
    v_rbp = (unsigned __int8)((*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rsi + 40) * 1 - 128)) & (63));
    goto loc_00794362;
loc_007944B5:
    result = NormBuffer__IsBlocked(v_stack_p8, (unsigned __int8)(v_rbp), a3, (int)((unsigned int)(result)));
    goto loc_007941AE;
loc_007944C5:
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result)))))), (unsigned __int8)(v_rbp), (unsigned __int8)(v_r15));
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
    *(unsigned __int64 *)(v_stack_p8 + 80) = *(unsigned __int64 *)(v_stack_p8 + 40);
    *(unsigned int *)(v_stack_p8 + 88) = (unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result)))));
    *(unsigned __int8 *)(v_stack_p8 + 92) = (unsigned __int8)(v_rbp);
    *(unsigned __int8 *)(v_stack_p8 + 93) = (unsigned __int8)(v_r15);
    goto loc_0079410F;
loc_007944F2:
    if (((unsigned int)(v_stack_p8)) != 63) goto loc_00794362;
    if ((unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result))))) != 0) goto loc_00794554;
    if ((*(unsigned __int64 *)(v_stack_p8 + 16)) != (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00794554;
    goto loc_00794362;
loc_0079450E:
    if ((*(unsigned __int8 *)(v_rsi + 113)) == 0) goto loc_00794554;
loc_00794514:
    a4 = 0;
    a3 = 0;
    result = NormBuffer__AppendEx(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result)))))), a3, a4);
loc_00794524:
    if ((unsigned __int8)(result) == 0) goto loc_00793F78;
    *(unsigned __int64 *)(v_stack_p8 + 80) = *(unsigned __int64 *)(v_stack_p8 + 40);
    *(unsigned int *)(v_stack_p8 + 88) = (unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result)))));
    goto loc_0079410A;
loc_0079453C:
    result = Normalization__AppendDecomposedChar(v_rsi, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result)))))), v_stack_p8, a4);
    goto loc_00793F7D;
loc_0079454E:
    if ((*(unsigned __int8 *)(v_rsi + 113)) != 0) goto loc_0079455E;
loc_00794554:
    goto loc_00793F7D;
loc_0079455E:
    result = NormBuffer__Append(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((int)((unsigned int)(result)))))), v_stack_p8, a4);
    goto loc_00794524;
}
```

## 5. (Beta) C Style

```c
int64_t Normalization__NormalizeCharacter(void *Arg1, int32_t Arg2, uint8_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r13 = 0;
loc_00793D5E:
    if (Arg3 == 0) goto loc_00793F66;
loc_00793D6A:
    if (Arg3 == 0) goto loc_0079455E;
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) - (251));
    if (condition_is_equal) goto loc_0079454E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00794554;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0079453C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00793EC3;
    if (((uint32_t)(Arg1)) != 1) goto loc_00793E3C;
    if (((uint32_t)((uint32_t)(Arg2))) >= 0xAC00ULL) goto loc_00793E0A;
    if (((uint32_t)((uint32_t)(Arg2) - 4352)) <= 18) goto loc_00793F9B;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))) - 4449)) <= 20) goto loc_00793F3B;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))) - 4520)) <= 26) goto loc_00793F10;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (13));
    if ((((uint32_t)(result)) & (0xFFFFFEFFULL)) != 0) goto loc_00793E02;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))) - 4447)) > ((uint32_t)(Arg1))) goto loc_00793E02;
    goto loc_00793D6A;
loc_00793E02:
    goto loc_00793D5E;
loc_00793E0A:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))) < 0xD7A4ULL) goto loc_00793FEA;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))) - 55216)) <= 22) goto loc_00793E31;
    local_r12 = 251;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))) - 55243)) <= 48) {
        local_r12 = 0;
    }
    goto loc_00793D5E;
loc_00793E3C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2)))))))) & (127));
    Arg1 = (Arg3) << (7);
    Arg1 = (Arg1) + (result);
    if ((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80)) == 0) goto loc_00794514;
    local_r15 = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80))) & (192));
    local_rbp = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80))) & (63));
    if (condition_is_equal) goto loc_00793E76;
    if (((uint8_t)(local_rbp)) != 63) goto loc_00794116;
loc_00793E76:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80)))) - (127));
    if (condition_is_equal) goto loc_0079450E;
    Arg1 = (uint32_t)((Arg1) - (64));
    if (condition_is_equal) goto loc_0079453C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_007944F2;
    result = NormBuffer__GetLastChar(Arg4, *(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80), Arg3, Arg4);
    result = Normalization__CanCombinableCharactersCombine(Arg1, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00794362;
    result = NormBuffer__RewindOutputCharacter(Arg4, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    goto loc_00793D5E;
loc_00793EC3:
    if ((*(uint64_t *)(arg4 + 0x10)) == (*(uint64_t *)(arg4 + 0x8))) goto loc_00794554;
    result = (*(uint64_t *)(arg4 + 0x10)) + (2);
    *(uint64_t *)(arg4 + 0x10) = result;
    result = (uint32_t)(((uint32_t)(0x2400ULL)) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x10)))));
    if (((uint16_t)(result)) > ((uint16_t)((uint32_t)(0x3FFULL)))) goto loc_00794554;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) + (0xFFFF2809ULL));
    local_rdi = (uint32_t)((local_rdi) << (10));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x10)))));
    Arg1 = ((int32_t)((uint32_t)(local_rdi))) >> (7);
    goto loc_00793D5E;
loc_00793F10:
    result = NormBuffer__GetLastChar(Arg4, (uint32_t)(0x3FFULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    result = IsHangulLV((uint32_t)((uint32_t)(result)), (uint32_t)(0x3FFULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    if ((uint8_t)(result) == 0) goto loc_00793F66;
    result = NormBuffer__RewindOutputCharacter(Arg4, (uint32_t)(0x3FFULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    result = ComposeHangulLVT((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    goto loc_00793F64;
loc_00793F3B:
    result = NormBuffer__GetLastChar(Arg4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    if (((uint32_t)(result - 4352)) > 18) goto loc_00793F66;
    result = NormBuffer__RewindOutputCharacter(Arg4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
    result = ComposeHangulLV((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
loc_00793F64:
loc_00793F66:
    result = NormBuffer__Append(Arg4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))))), (uint32_t)((uint32_t)(result)));
loc_00793F70:
    if ((uint8_t)(result) != 0) goto loc_0079410F;
loc_00793F78:
loc_00793F7D:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xC0000023ULL);
loc_00793F9B:
    if ((*(uint64_t *)(v_stack_p8 + 0x10)) == (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00793F66;
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x10) + 2;
    result = ComposeHangulLV((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), *(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x10)), *(uint64_t *)(v_stack_p8 + 0x10), *(uint64_t *)(v_stack_p8 + 0x8));
    if ((uint32_t)(result) == 0) goto loc_00793FE4;
    if ((*(uint64_t *)(v_stack_p8 + 0x10) + 2) == (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00793F66;
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x10) + 2 + 2;
    result = ComposeHangulLVT((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x2), *(uint64_t *)(v_stack_p8 + 0x10), *(uint64_t *)(v_stack_p8 + 0x8));
    if ((uint32_t)(result) != 0) goto loc_00793F64;
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x10) + 2;
    goto loc_00793F66;
loc_00793FE4:
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x10);
    goto loc_00794033;
loc_00793FEA:
    if ((*(uint8_t *)(v_stack_p18 + 0x70)) == 1) goto loc_0079403B;
    result = IsHangulLV((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), *(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x2), *(uint64_t *)(v_stack_p8 + 0x10), *(uint64_t *)(v_stack_p8 + 0x8));
    if ((uint8_t)(result) == 0) goto loc_00793F66;
    if ((*(uint64_t *)(v_stack_p8 + 0x10)) == (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00793F66;
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x10) + 2;
    result = ComposeHangulLVT((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))), *(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x10)), *(uint64_t *)(v_stack_p8 + 0x10), *(uint64_t *)(v_stack_p8 + 0x8));
    if ((uint32_t)(result) != 0) goto loc_00793F66;
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x10);
loc_00794033:
    goto loc_00793F66;
loc_0079403B:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) + (0xFFFF5400ULL));
    Arg4 = 0;
    Arg2 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x10))) >> (8));
    Arg3 = 0;
    result = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    result = (uint32_t)((result) * (Arg2));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(result)));
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)((uint32_t)(0x1100ULL))));
    result = NormBuffer__AppendEx(v_stack_p8, (uint16_t)(Arg2), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00793F78;
    Arg4 = 0;
    Arg3 = 0;
    local_rdi = (uint32_t)((local_rsi + (uint16_t)(Arg2) * 1) >> (4));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (31));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(result)));
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0x1161ULL))));
    result = NormBuffer__AppendEx(v_stack_p8, (uint16_t)(local_rdi), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00793F78;
    Arg2 = (uint32_t)(((uint16_t)(local_rdi)) + ((uint32_t)(local_r14)));
    Arg2 = (uint32_t)((Arg2) >> (4));
    result = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    result = (uint32_t)((result) * (Arg2));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)(0x11A7ULL)) + ((uint32_t)(local_r14)));
    local_r14 = (uint16_t)(-(local_r14));
    local_rsi = (uint16_t)((local_rsi) & ((uint16_t)(result)));
    if (condition_is_equal) goto loc_007940FC;
    Arg4 = 0;
    Arg3 = 0;
    result = NormBuffer__AppendEx(v_stack_p8, (uint16_t)(local_rsi), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00793F78;
loc_007940FC:
    *(uint64_t *)(v_stack_p8 + 0x50) = *(uint64_t *)(v_stack_p8 + 0x28);
    *(uint32_t *)(v_stack_p8 + 0x58) = (uint32_t)((uint16_t)((uint16_t)(local_rsi)));
loc_0079410A:
    *(uint16_t *)(v_stack_p8 + 0x5C) = 0;
loc_0079410F:
    result = 0;
    goto loc_00793F7D;
loc_00794116:
    if ((((uint8_t)(local_r15)) & (191)) == 0) goto loc_007944C5;
    result = NormBuffer__GetLastChar(v_stack_p8, (uint16_t)(local_rsi), Arg3, Arg4);
    if ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x48)) == 0) goto loc_0079413F;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x48))) == 63) goto loc_0079413F;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x49))) & (191)) == 0) {
        result = *(uint64_t *)(v_stack_p8 + 0x40);
        Arg2 = *(uint8_t *)(v_stack_p8 + 0x49);
        result = (result) + (2);
        *(uint64_t *)(v_stack_p8 + 0x50) = result;
        result = *(uint32_t *)(v_stack_p8 + 0x38);
        *(uint32_t *)(v_stack_p8 + 0x58) = (uint32_t)(result);
        *(uint8_t *)(v_stack_p8 + 0x5C) = (uint8_t)(*(uint8_t *)(v_stack_p8 + 0x48));
        *(uint8_t *)(v_stack_p8 + 0x5D) = (uint8_t)(Arg2);
        *(uint64_t *)(v_stack_p8 + 0x60) = 0;
    }
    if (((uint8_t)(local_r15)) == 128) goto loc_007944B5;
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x5D)) | (*(uint8_t *)(v_stack_p8 + 0x5C)));
    Arg1 = (uint8_t)((Arg1) + (64));
    if ((((uint8_t)(Arg1)) & (191)) == 0) goto loc_007944B5;
    if ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x48)) == 0) goto loc_0079445B;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x48))) == 63) goto loc_0079445B;
    if ((uint8_t)(Arg2) == 0) goto loc_00794347;
    if (((uint8_t)(Arg2)) == 64) goto loc_007942BE;
    result = NormBuffer__IsBlocked(v_stack_p8, (uint8_t)((uint32_t)(0x92492493ULL)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_007941C3;
loc_007941AE:
    result = NormBuffer__InsertAtBlockedLocation(v_stack_p8, (uint32_t)((uint32_t)((uint16_t)(local_rsi))), (uint8_t)((uint32_t)(0x92492493ULL)), (uint8_t)(local_r15));
    goto loc_00793F70;
loc_007941C3:
    if ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C)) == 0) goto loc_007941D8;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C))) == 63) goto loc_007941D8;
    if ((*(uint8_t *)(v_stack_p8 + 0x5D)) != 64) goto loc_0079424A;
loc_007941D8:
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)), (uint32_t)((uint32_t)((uint16_t)(local_rsi))), (uint8_t)(local_r15));
    if ((uint32_t)(result) == 0) goto loc_00794237;
    Arg4 = (uint32_t)(((int32_t)((uint32_t)(result))) & (127));
    Arg2 = ((int32_t)((uint32_t)(result))) >> (7);
    Arg3 = (*(uint8_t *)(Arg2 + *(uint64_t *)(local_rsi + 0x20) * 1)) << (7);
    Arg3 = (Arg3) + (Arg4);
    *(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x50) - 0x2) = (uint16_t)((int32_t)((uint32_t)(result)));
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80))) & (192));
    *(uint32_t *)(v_stack_p8 + 0x58) = (uint32_t)((int32_t)((uint32_t)(result)));
    Arg2 = (uint8_t)((*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80)) & (63));
    *(uint8_t *)(v_stack_p8 + 0x5D) = (uint8_t)(Arg1);
    *(uint8_t *)(v_stack_p8 + 0x5C) = (uint8_t)(Arg2);
    goto loc_00794448;
loc_00794237:
    if ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C)) == 0) goto loc_007941AE;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C))) == 63) goto loc_007941AE;
loc_0079424A:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C))) <= ((uint8_t)((uint32_t)(0x92492493ULL)))) goto loc_007941AE;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C))) != (*(uint8_t *)(local_rsi + 0x74))) goto loc_0079426B;
    if (((uint8_t)((uint32_t)(0x92492493ULL))) < (*(uint8_t *)(local_rsi + 0x72))) goto loc_0079429C;
    if (((uint8_t)((uint32_t)(0x92492493ULL))) != (*(uint8_t *)(local_rsi + 0x73))) goto loc_007941AE;
    goto loc_00794277;
loc_0079426B:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x5C))) != (*(uint8_t *)(local_rsi + 0x76))) goto loc_0079429C;
    if (((uint8_t)((uint32_t)(0x92492493ULL))) != (*(uint8_t *)(local_rsi + 0x75))) goto loc_0079429C;
loc_00794277:
    result = NormBuffer__LastStartBasePair(v_stack_p8, Arg2, Arg3, Arg4);
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r14)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_007941AE;
    goto loc_0079439F;
loc_0079429C:
    result = NormBuffer__LastStartBase(v_stack_p8, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r14)), Arg4);
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint16_t)(local_rsi))), Arg4);
    if ((uint32_t)(result) != 0) goto loc_007943FD;
    goto loc_007941AE;
loc_007942BE:
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)), (uint32_t)((uint32_t)((uint16_t)(local_rsi))), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00794347;
    result = NormBuffer__RewindOutputCharacter(v_stack_p8, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)), (uint32_t)((uint32_t)((uint16_t)(local_rsi))), Arg4);
    Arg4 = (uint32_t)(((int32_t)((uint32_t)(result))) & (127));
    Arg2 = ((int32_t)((uint32_t)(result))) >> (7);
    Arg3 = (*(uint8_t *)(Arg2 + *(uint64_t *)(local_rsi + 0x20) * 1)) << (7);
    Arg3 = (Arg3) + (Arg4);
    Arg3 = (uint8_t)((*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80)) & (63));
    Arg4 = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80))) & (192));
    result = NormBuffer__AppendEx(v_stack_p8, (uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00793F78;
    result = (*(uint64_t *)(v_stack_p8 + 0x40)) + (2);
    *(uint64_t *)(v_stack_p8 + 0x60) = 0;
    *(uint64_t *)(v_stack_p8 + 0x50) = result;
    *(uint32_t *)(v_stack_p8 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x38)));
    *(uint8_t *)(v_stack_p8 + 0x5C) = (uint8_t)(*(uint8_t *)(v_stack_p8 + 0x48));
    *(uint8_t *)(v_stack_p8 + 0x5D) = (uint8_t)(*(uint8_t *)(v_stack_p8 + 0x49));
    goto loc_0079410F;
loc_00794347:
    if (((uint8_t)(local_rsi)) <= ((uint8_t)((uint32_t)(0x92492493ULL)))) goto loc_00794362;
    if (((uint8_t)(local_rsi)) != (*(uint8_t *)(local_rsi + 0x74))) goto loc_00794377;
    if (((uint8_t)((uint32_t)(0x92492493ULL))) < (*(uint8_t *)(local_rsi + 0x72))) goto loc_007943E0;
    if (((uint8_t)((uint32_t)(0x92492493ULL))) == (*(uint8_t *)(local_rsi + 0x73))) goto loc_00794383;
loc_00794362:
    result = NormBuffer__AppendEx(v_stack_p8, (uint32_t)((uint32_t)((uint16_t)(local_rsi))), (uint8_t)((uint32_t)(0x92492493ULL)), (uint8_t)(local_r15));
    goto loc_00793F70;
loc_00794377:
    if (((uint8_t)(local_rsi)) != (*(uint8_t *)(local_rsi + 0x76))) goto loc_007943E0;
    if (((uint8_t)((uint32_t)(0x92492493ULL))) != (*(uint8_t *)(local_rsi + 0x75))) goto loc_007943E0;
loc_00794383:
    result = NormBuffer__LastStartBasePair(v_stack_p8, (uint32_t)((uint32_t)((uint16_t)(local_rsi))), (uint8_t)((uint32_t)(0x92492493ULL)), (uint8_t)(local_r15));
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r14)), (uint8_t)(local_r15));
    if ((uint32_t)(result) == 0) goto loc_00794362;
loc_0079439F:
    Arg4 = (uint32_t)(((int32_t)((uint32_t)(result))) & (127));
    Arg2 = ((int32_t)((uint32_t)(result))) >> (7);
    Arg3 = (*(uint8_t *)(Arg2 + *(uint64_t *)(local_rsi + 0x20) * 1)) << (7);
    Arg3 = (Arg3) + (Arg4);
    Arg3 = (uint8_t)((*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80)) & (63));
    local_rdi = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80))) & (192));
    result = NormBuffer__ReplaceLastStartBasePair(v_stack_p8, (uint32_t)((uint32_t)(result)), Arg3, (uint8_t)(local_rdi));
    goto loc_0079443C;
loc_007943E0:
    result = NormBuffer__LastStartBase(v_stack_p8, (uint32_t)((uint32_t)(result)), Arg3, (uint8_t)(local_rdi));
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_rdi)), (uint8_t)(local_rdi));
    if ((uint32_t)(result) == 0) goto loc_00794362;
loc_007943FD:
    Arg4 = (uint32_t)(((int32_t)((uint32_t)(result))) & (127));
    Arg2 = ((int32_t)((uint32_t)(result))) >> (7);
    Arg3 = (*(uint8_t *)(Arg2 + *(uint64_t *)(local_rsi + 0x20) * 1)) << (7);
    Arg3 = (Arg3) + (Arg4);
    Arg3 = (uint8_t)((*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80)) & (63));
    local_rdi = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80))) & (192));
    result = NormBuffer__ReplaceLastStartBase(v_stack_p8, (uint32_t)((uint32_t)(result)), Arg3, (uint8_t)(local_rdi));
loc_0079443C:
    if ((uint8_t)(result) == 0) goto loc_00793F78;
loc_00794448:
    if (((uint8_t)(local_rdi)) != 64) goto loc_0079410F;
    result = NormBuffer__RecheckStartCombinations(v_stack_p8, (uint32_t)((uint32_t)(result)), Arg3, (uint8_t)(local_rdi));
    goto loc_0079410F;
loc_0079445B:
    result = Normalization__CanCombinableCharactersCombine(local_rsi, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)), (uint32_t)((uint32_t)(local_rdi)), (uint8_t)(local_rdi));
    if ((uint32_t)(result) == 0) goto loc_00794362;
    result = NormBuffer__RewindOutputCharacter(v_stack_p8, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)), (uint32_t)((uint32_t)(local_rdi)), (int32_t)((uint32_t)(result)));
    Arg3 = (uint32_t)(((int32_t)((uint32_t)(result))) & (127));
    Arg1 = ((int32_t)((uint32_t)(result))) >> (7);
    Arg2 = (*(uint8_t *)(arg1 + *(uint64_t *)(local_rsi + 0x20) * 1)) << (7);
    Arg2 = (Arg2) + (Arg3);
    local_r15 = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg2 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80))) & (192));
    local_rbp = (uint8_t)((*(uint8_t *)(Arg2 + *(uint64_t *)(local_rsi + 0x28) * 1 - 0x80)) & (63));
    goto loc_00794362;
loc_007944B5:
    result = NormBuffer__IsBlocked(v_stack_p8, (uint8_t)(local_rbp), Arg3, (int32_t)((uint32_t)(result)));
    goto loc_007941AE;
loc_007944C5:
    result = NormBuffer__AppendEx(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))))), (uint8_t)(local_rbp), (uint8_t)(local_r15));
    if ((uint8_t)(result) == 0) goto loc_00793F78;
    *(uint64_t *)(v_stack_p8 + 0x50) = *(uint64_t *)(v_stack_p8 + 0x28);
    *(uint32_t *)(v_stack_p8 + 0x58) = (uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))));
    *(uint8_t *)(v_stack_p8 + 0x5C) = (uint8_t)(local_rbp);
    *(uint8_t *)(v_stack_p8 + 0x5D) = (uint8_t)(local_r15);
    goto loc_0079410F;
loc_007944F2:
    if (((uint32_t)(v_stack_p8)) != 63) goto loc_00794362;
    if ((uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result))))) != 0) goto loc_00794554;
    if ((*(uint64_t *)(v_stack_p8 + 0x10)) != (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00794554;
    goto loc_00794362;
loc_0079450E:
    if ((*(uint8_t *)(local_rsi + 0x71)) == 0) goto loc_00794554;
loc_00794514:
    Arg4 = 0;
    Arg3 = 0;
    result = NormBuffer__AppendEx(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))))), Arg3, Arg4);
loc_00794524:
    if ((uint8_t)(result) == 0) goto loc_00793F78;
    *(uint64_t *)(v_stack_p8 + 0x50) = *(uint64_t *)(v_stack_p8 + 0x28);
    *(uint32_t *)(v_stack_p8 + 0x58) = (uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))));
    goto loc_0079410A;
loc_0079453C:
    result = Normalization__AppendDecomposedChar(local_rsi, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))))), v_stack_p8, Arg4);
    goto loc_00793F7D;
loc_0079454E:
    if ((*(uint8_t *)(local_rsi + 0x71)) != 0) goto loc_0079455E;
loc_00794554:
    goto loc_00793F7D;
loc_0079455E:
    result = NormBuffer__Append(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((int32_t)((uint32_t)(result)))))), v_stack_p8, Arg4);
    goto loc_00794524;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x71` | `8` | `R` |
| `Arg1` | `+ 0x72` | `8` | `R` |
| `Arg1` | `+ 0x73` | `8` | `R` |
| `Arg1` | `+ 0x74` | `8` | `R` |
| `Arg1` | `+ 0x75` | `8` | `R` |
| `Arg1` | `+ 0x76` | `8` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x38` | `32` | `R` |
| `Arg4` | `+ 0x40` | `64` | `R` |
| `Arg4` | `+ 0x48` | `8` | `R` |
| `Arg4` | `+ 0x49` | `8` | `R` |
| `Arg4` | `+ 0x50` | `64` | `R` |
| `Arg4` | `+ 0x50` | `64` | `W` |
| `Arg4` | `+ 0x58` | `32` | `R` |
| `Arg4` | `+ 0x58` | `32` | `W` |
| `Arg4` | `+ 0x5C` | `8` | `R` |
| `Arg4` | `+ 0x5C` | `8` | `W` |
| `Arg4` | `+ 0x5C` | `16` | `W` |
| `Arg4` | `+ 0x5D` | `8` | `R` |
| `Arg4` | `+ 0x5D` | `8` | `W` |
| `Arg4` | `+ 0x60` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00793D34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
