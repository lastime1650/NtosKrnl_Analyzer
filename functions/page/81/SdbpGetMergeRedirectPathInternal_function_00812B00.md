# SdbpGetMergeRedirectPathInternal

- RVA: `0x00812B00`–`0x008130A1` (길이 `1,441` bytes)
- VA: `0x0000000140812B00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D98C4`
- 디코드: `373`개 명령, `1,441/1,441` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **20**

### Outgoing calls
- `0x00812BBD` → [AslPathGetFileNamePart](AslPathGetFileNamePart_function_0081B274.md) (function, `0x0081B274`)
- `0x00812BF7` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x00812C12` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)
- `0x00812C3A` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812C67` → [SdbpSafeAllocAndConcatW](SdbpSafeAllocAndConcatW_function_00813198.md) (function, `0x00813198`)
- `0x00812C8F` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812CBB` → [AslRegistryGetKey](AslRegistryGetKey_function_00819F64.md) (function, `0x00819F64`)
- `0x00812CEB` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812D00` → [AslRegistryGetString](AslRegistryGetString_function_0081A084.md) (function, `0x0081A084`)
- `0x00812D19` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00812D3C` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00812D6E` → [SdbpSafeAllocAndConcatW](SdbpSafeAllocAndConcatW_function_00813198.md) (function, `0x00813198`)
- `0x00812D9A` → [AslRegistryGetUInt32](AslRegistryGetUInt32_function_0081A228.md) (function, `0x0081A228`)
- `0x00812DD5` → [AslRegistryGetUInt32](AslRegistryGetUInt32_function_0081A228.md) (function, `0x0081A228`)
- `0x00812DFE` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812E19` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00812E26` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)
- `0x00812E33` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)
- `0x00812E40` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)
- `0x00812E51` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)
- `0x00812E62` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)
- `0x00812E70` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00812EB0` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812EC4` → [AslRegistryGetUInt32](AslRegistryGetUInt32_function_0081A228.md) (function, `0x0081A228`)
- `0x00812F00` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812F15` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)
- `0x00812F53` → [SdbpSafeAllocAndConcatW](SdbpSafeAllocAndConcatW_function_00813198.md) (function, `0x00813198`)
- `0x00812F74` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00812F90` → [SdbpGetFileTimestamp](SdbpGetFileTimestamp_function_00812558.md) (function, `0x00812558`)
- `0x00812FC2` → [SdbpGetFileTimestamp](SdbpGetFileTimestamp_function_00812558.md) (function, `0x00812558`)
- `0x00812FE6` → [SdbpGetManifestedMergeStubAlloc](SdbpGetManifestedMergeStubAlloc_function_0081275C.md) (function, `0x0081275C`)
- `0x00813020` → [SdbpGetFileTimestamp](SdbpGetFileTimestamp_function_00812558.md) (function, `0x00812558`)
- `0x00813041` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)

### Direct callers
- [SdbGetMergeRedirectPath](SdbGetMergeRedirectPath_function_0081210C.md) at `0x00812169`
- [SdbGetMergeRedirectPath](SdbGetMergeRedirectPath_function_0081210C.md) at `0x00812220`

### Static image references
- `0x00812B1C` → RVA `0x00E0A740` (`.data`; read)
- `0x00812B2A` → RVA `0x0003B710` (`.rdata`; read)
- `0x00812B33` → RVA `0x0003B700` (`.rdata`; read)
- `0x00812B3F` → RVA `0x0003B714` (`.rdata`; read)
- `0x00812C1D` → RVA `0x0003B7B8` (`.rdata`; read)
- `0x00812C2E` → RVA `0x0003B6D8` (`.rdata`; read)
- `0x00812C4E` → RVA `0x0003B6B8` (`.rdata`; read)
- `0x00812C72` → RVA `0x0003B688` (`.rdata`; read)
- `0x00812CA7` → RVA `0x0003B270` (`.rdata`; read)
- `0x00812CD1` → RVA `0x0003B238` (`.rdata`; read)
- `0x00812D32` → RVA `0x0003B660` (`.rdata`; read)
- `0x00812D5A` → RVA `0x0003B648` (`.rdata`; read)
- `0x00812DB1` → RVA `0x0003B628` (`.rdata`; read)
- `0x00812DC7` → RVA `0x0003B610` (`.rdata`; read)
- `0x00812E9E` → RVA `0x0003B5C0` (`.rdata`; read)
- `0x00812EB9` → RVA `0x0003B5A8` (`.rdata`; read)
- `0x00812EEE` → RVA `0x0003B550` (`.rdata`; read)
- `0x00812FA6` → RVA `0x0003B510` (`.rdata`; read)
- `0x00813000` → RVA `0x0003B838` (`.rdata`; read)
- `0x0081308B` → RVA `0x0003B530` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00812BF7` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x00812C12` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
  - `0x00812D19` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00812D3C` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00812E19` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00812E70` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00812F15` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00812B00  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00812B05  55                              push rbp
00812B06  56                              push rsi
00812B07  57                              push rdi
00812B08  41 54                           push r12
00812B0A  41 55                           push r13
00812B0C  41 56                           push r14
00812B0E  41 57                           push r15
00812B10  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00812B15  48 81 EC D0 00 00 00            sub rsp, 0xd0
00812B1C  48 8B 05 1D 7C 5F 00            mov rax, qword ptr [rip + 0x5f7c1d]
00812B23  48 33 C4                        xor rax, rsp
00812B26  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00812B2A  8B 05 E0 8B 82 FF               mov eax, dword ptr [rip - 0x7d7420]
00812B30  4C 8B E2                        mov r12, rdx
00812B33  0F 10 05 C6 8B 82 FF            movups xmm0, xmmword ptr [rip - 0x7d743a]
00812B3A  33 D2                           xor edx, edx
00812B3C  89 45 0F                        mov dword ptr [rbp + 0xf], eax
00812B3F  0F B7 05 CE 8B 82 FF            movzx eax, word ptr [rip - 0x7d7432]
00812B46  49 8B F1                        mov rsi, r9
00812B49  66 89 45 13                     mov word ptr [rbp + 0x13], ax
00812B4D  44 8B F2                        mov r14d, edx
00812B50  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
00812B54  44 8B EA                        mov r13d, edx
00812B57  44 89 45 9B                     mov dword ptr [rbp - 0x65], r8d
00812B5B  48 89 4D F7                     mov qword ptr [rbp - 9], rcx
00812B5F  89 55 97                        mov dword ptr [rbp - 0x69], edx
00812B62  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
00812B66  48 89 55 8F                     mov qword ptr [rbp - 0x71], rdx
00812B6A  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00812B6E  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
00812B72  89 55 9F                        mov dword ptr [rbp - 0x61], edx
00812B75  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
00812B79  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
00812B7D  48 89 55 E7                     mov qword ptr [rbp - 0x19], rdx
00812B81  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
00812B85  48 89 55 87                     mov qword ptr [rbp - 0x79], rdx
00812B89  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
00812B8D  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00812B91  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00812B95  48 85 C9                        test rcx, rcx
00812B98  75 0A                           jne 0x140812ba4
00812B9A  B8 EF 00 00 C0                  mov eax, 0xc00000ef
00812B9F  E9 C5 02 00 00                  jmp 0x140812e69
00812BA4  48 89 11                        mov qword ptr [rcx], rdx
00812BA7  4D 85 E4                        test r12, r12
00812BAA  74 09                           je 0x140812bb5
00812BAC  45 85 C0                        test r8d, r8d
00812BAF  74 04                           je 0x140812bb5
00812BB1  41 89 14 24                     mov dword ptr [r12], edx
00812BB5  48 8B CE                        mov rcx, rsi
00812BB8  BB 34 00 00 C0                  mov ebx, 0xc0000034
00812BBD  E8 B2 86 00 00                  call 0x14081b274
00812BC2  4C 8B F8                        mov r15, rax
00812BC5  48 3B C6                        cmp rax, rsi
00812BC8  0F 84 99 02 00 00               je 0x140812e67
00812BCE  48 8D 78 FC                     lea rdi, [rax - 4]
00812BD2  48 3B FE                        cmp rdi, rsi
00812BD5  0F 82 8C 02 00 00               jb 0x140812e67
00812BDB  0F B7 0F                        movzx ecx, word ptr [rdi]
00812BDE  66 83 F9 5C                     cmp cx, 0x5c
00812BE2  74 06                           je 0x140812bea
00812BE4  66 83 F9 2F                     cmp cx, 0x2f
00812BE8  75 16                           jne 0x140812c00
00812BEA  41 B8 0A 00 00 00               mov r8d, 0xa
00812BF0  48 8D 55 FF                     lea rdx, [rbp - 1]
00812BF4  48 8B CF                        mov rcx, rdi
00812BF7  E8 C4 D5 CE FF                  call 0x1405001c0
00812BFC  85 C0                           test eax, eax
00812BFE  74 06                           je 0x140812c06
00812C00  48 83 EF 02                     sub rdi, 2
00812C04  EB CC                           jmp 0x140812bd2
00812C06  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00812C0A  BA FF FF FF 7F                  mov edx, 0x7fffffff
00812C0F  49 8B CF                        mov rcx, r15
00812C12  E8 59 2E C2 FF                  call 0x140435a70
00812C17  8B D8                           mov ebx, eax
00812C19  85 C0                           test eax, eax
00812C1B  79 27                           jns 0x140812c44
00812C1D  4C 8D 0D 94 8B 82 FF            lea r9, [rip - 0x7d746c]
00812C24  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00812C28  41 B8 2B 07 00 00               mov r8d, 0x72b
00812C2E  48 8D 15 A3 8A 82 FF            lea rdx, [rip - 0x7d755d]
00812C35  B9 01 00 00 00                  mov ecx, 1
00812C3A  E8 AD B8 14 00                  call 0x14095e4ec
00812C3F  E9 23 02 00 00                  jmp 0x140812e67
00812C44  44 39 6D 9B                     cmp dword ptr [rbp - 0x65], r13d
00812C48  74 55                           je 0x140812c9f
00812C4A  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00812C4E  48 8D 15 63 8A 82 FF            lea rdx, [rip - 0x7d759d]
00812C55  4D 8B CF                        mov r9, r15
00812C58  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00812C5D  41 B8 0D 00 00 00               mov r8d, 0xd
00812C63  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00812C67  E8 2C 05 00 00                  call 0x140813198
00812C6C  8B D8                           mov ebx, eax
00812C6E  85 C0                           test eax, eax
00812C70  79 27                           jns 0x140812c99
00812C72  4C 8D 0D 0F 8A 82 FF            lea r9, [rip - 0x7d75f1]
00812C79  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00812C7D  41 B8 37 07 00 00               mov r8d, 0x737
00812C83  48 8D 15 4E 8A 82 FF            lea rdx, [rip - 0x7d75b2]
00812C8A  B9 01 00 00 00                  mov ecx, 1
00812C8F  E8 58 B8 14 00                  call 0x14095e4ec
00812C94  E9 BD 01 00 00                  jmp 0x140812e56
00812C99  48 8B 7D C7                     mov rdi, qword ptr [rbp - 0x39]
00812C9D  EB 03                           jmp 0x140812ca2
00812C9F  49 8B FF                        mov rdi, r15
00812CA2  BE 01 00 00 00                  mov esi, 1
00812CA7  48 8D 15 C2 85 82 FF            lea rdx, [rip - 0x7d7a3e]
00812CAE  44 8B CE                        mov r9d, esi
00812CB1  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00812CB5  41 B8 00 01 00 80               mov r8d, 0x80000100
00812CBB  E8 A4 72 00 00                  call 0x140819f64
00812CC0  8B D8                           mov ebx, eax
00812CC2  85 C0                           test eax, eax
00812CC4  79 2F                           jns 0x140812cf5
00812CC6  3D 34 00 00 C0                  cmp eax, 0xc0000034
00812CCB  0F 84 36 01 00 00               je 0x140812e07
00812CD1  4C 8D 0D 60 85 82 FF            lea r9, [rip - 0x7d7aa0]
00812CD8  41 B8 48 07 00 00               mov r8d, 0x748
00812CDE  48 8D 15 F3 89 82 FF            lea rdx, [rip - 0x7d760d]
00812CE5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00812CE9  8B CE                           mov ecx, esi
00812CEB  E8 FC B7 14 00                  call 0x14095e4ec
00812CF0  E9 12 01 00 00                  jmp 0x140812e07
00812CF5  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00812CF9  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00812CFD  4C 8B C7                        mov r8, rdi
00812D00  E8 7F 73 00 00                  call 0x14081a084
00812D05  4C 8B 75 8F                     mov r14, qword ptr [rbp - 0x71]
00812D09  8B D8                           mov ebx, eax
00812D0B  85 C0                           test eax, eax
00812D0D  0F 88 F4 00 00 00               js 0x140812e07
00812D13  49 8B D7                        mov rdx, r15
00812D16  49 8B CE                        mov rcx, r14
00812D19  E8 62 D3 CE FF                  call 0x140500080
00812D1E  85 C0                           test eax, eax
00812D20  75 0A                           jne 0x140812d2c
00812D22  BB 34 00 00 C0                  mov ebx, 0xc0000034
00812D27  E9 DB 00 00 00                  jmp 0x140812e07
00812D2C  44 39 6D 9B                     cmp dword ptr [rbp - 0x65], r13d
00812D30  74 23                           je 0x140812d55
00812D32  48 8D 15 27 89 82 FF            lea rdx, [rip - 0x7d76d9]
00812D39  49 8B CE                        mov rcx, r14
00812D3C  E8 3F D3 CE FF                  call 0x140500080
00812D41  85 C0                           test eax, eax
00812D43  75 10                           jne 0x140812d55
00812D45  4D 85 E4                        test r12, r12
00812D48  74 0B                           je 0x140812d55
00812D4A  41 89 34 24                     mov dword ptr [r12], esi
00812D4E  33 DB                           xor ebx, ebx
00812D50  E9 B2 00 00 00                  jmp 0x140812e07
00812D55  4C 21 6C 24 20                  and qword ptr [rsp + 0x20], r13
00812D5A  48 8D 15 E7 88 82 FF            lea rdx, [rip - 0x7d7719]
00812D61  4C 8B CF                        mov r9, rdi
00812D64  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00812D68  41 B8 09 00 00 00               mov r8d, 9
00812D6E  E8 25 04 00 00                  call 0x140813198
00812D73  8B D8                           mov ebx, eax
00812D75  85 C0                           test eax, eax
00812D77  79 12                           jns 0x140812d8b
00812D79  4C 8D 0D 08 89 82 FF            lea r9, [rip - 0x7d76f8]
00812D80  41 B8 6A 07 00 00               mov r8d, 0x76a
00812D86  E9 53 FF FF FF                  jmp 0x140812cde
00812D8B  48 8B 7D A7                     mov rdi, qword ptr [rbp - 0x59]
00812D8F  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00812D93  4C 8B 45 BF                     mov r8, qword ptr [rbp - 0x41]
00812D97  48 8B D7                        mov rdx, rdi
00812D9A  E8 89 74 00 00                  call 0x14081a228
00812D9F  8B D8                           mov ebx, eax
00812DA1  3D 34 00 00 C0                  cmp eax, 0xc0000034
00812DA6  75 05                           jne 0x140812dad
00812DA8  45 33 F6                        xor r14d, r14d
00812DAB  EB 1A                           jmp 0x140812dc7
00812DAD  85 C0                           test eax, eax
00812DAF  79 12                           jns 0x140812dc3
00812DB1  4C 8D 0D 70 88 82 FF            lea r9, [rip - 0x7d7790]
00812DB8  41 B8 73 07 00 00               mov r8d, 0x773
00812DBE  E9 1B FF FF FF                  jmp 0x140812cde
00812DC3  44 8B 75 9F                     mov r14d, dword ptr [rbp - 0x61]
00812DC7  4C 8D 05 42 88 82 FF            lea r8, [rip - 0x7d77be]
00812DCE  48 8B D7                        mov rdx, rdi
00812DD1  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00812DD5  E8 4E 74 00 00                  call 0x14081a228
00812DDA  8B D8                           mov ebx, eax
00812DDC  85 C0                           test eax, eax
00812DDE  0F 89 AD 00 00 00               jns 0x140812e91
00812DE4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00812DE8  4C 8D 0D 39 88 82 FF            lea r9, [rip - 0x7d77c7]
00812DEF  41 B8 79 07 00 00               mov r8d, 0x779
00812DF5  48 8D 15 DC 88 82 FF            lea rdx, [rip - 0x7d7724]
00812DFC  8B CE                           mov ecx, esi
00812DFE  E8 E9 B6 14 00                  call 0x14095e4ec
00812E03  4C 8B 75 8F                     mov r14, qword ptr [rbp - 0x71]
00812E07  4C 8B 7D 87                     mov r15, qword ptr [rbp - 0x79]
00812E0B  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00812E0F  48 8D 41 FF                     lea rax, [rcx - 1]
00812E13  48 83 F8 FD                     cmp rax, -3
00812E17  77 05                           ja 0x140812e1e
00812E19  E8 92 A4 E9 FF                  call 0x1406ad2b0
00812E1E  4D 85 F6                        test r14, r14
00812E21  74 08                           je 0x140812e2b
00812E23  49 8B D6                        mov rdx, r14
00812E26  E8 49 88 14 00                  call 0x14095b674
00812E2B  4D 85 ED                        test r13, r13
00812E2E  74 08                           je 0x140812e38
00812E30  49 8B D5                        mov rdx, r13
00812E33  E8 3C 88 14 00                  call 0x14095b674
00812E38  4D 85 FF                        test r15, r15
00812E3B  74 08                           je 0x140812e45
00812E3D  49 8B D7                        mov rdx, r15
00812E40  E8 2F 88 14 00                  call 0x14095b674
00812E45  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00812E49  48 85 C0                        test rax, rax
00812E4C  74 08                           je 0x140812e56
00812E4E  48 8B D0                        mov rdx, rax
00812E51  E8 1E 88 14 00                  call 0x14095b674
00812E56  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00812E5A  48 85 C0                        test rax, rax
00812E5D  74 08                           je 0x140812e67
00812E5F  48 8B D0                        mov rdx, rax
00812E62  E8 0D 88 14 00                  call 0x14095b674
00812E67  8B C3                           mov eax, ebx
00812E69  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00812E6D  48 33 CC                        xor rcx, rsp
00812E70  E8 CB 97 E9 FF                  call 0x1406ac640
00812E75  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
00812E7D  48 81 C4 D0 00 00 00            add rsp, 0xd0
00812E84  41 5F                           pop r15
00812E86  41 5E                           pop r14
00812E88  41 5D                           pop r13
00812E8A  41 5C                           pop r12
00812E8C  5F                              pop rdi
00812E8D  5E                              pop rsi
00812E8E  5D                              pop rbp
00812E8F  C3                              ret
00812E90  CC                              int3
00812E91  48 8D 3D 40 88 82 FF            lea rdi, [rip - 0x7d77c0]
00812E98  44 39 75 97                     cmp dword ptr [rbp - 0x69], r14d
00812E9C  73 17                           jae 0x140812eb5
00812E9E  4C 8D 0D 1B 87 82 FF            lea r9, [rip - 0x7d78e5]
00812EA5  41 B8 82 07 00 00               mov r8d, 0x782
00812EAB  48 8B D7                        mov rdx, rdi
00812EAE  8B CE                           mov ecx, esi
00812EB0  E8 37 B6 14 00                  call 0x14095e4ec
00812EB5  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00812EB9  4C 8D 05 E8 86 82 FF            lea r8, [rip - 0x7d7918]
00812EC0  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00812EC4  E8 5F 73 00 00                  call 0x14081a228
00812EC9  8B D8                           mov ebx, eax
00812ECB  85 C0                           test eax, eax
00812ECD  79 19                           jns 0x140812ee8
00812ECF  4C 8D 0D 52 87 82 FF            lea r9, [rip - 0x7d78ae]
00812ED6  41 B8 88 07 00 00               mov r8d, 0x788
00812EDC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00812EE0  48 8B D7                        mov rdx, rdi
00812EE3  E9 14 FF FF FF                  jmp 0x140812dfc
00812EE8  44 3B 75 97                     cmp r14d, dword ptr [rbp - 0x69]
00812EEC  73 17                           jae 0x140812f05
00812EEE  4C 8D 0D 5B 86 82 FF            lea r9, [rip - 0x7d79a5]
00812EF5  41 B8 91 07 00 00               mov r8d, 0x791
00812EFB  48 8B D7                        mov rdx, rdi
00812EFE  8B CE                           mov ecx, esi
00812F00  E8 E7 B5 14 00                  call 0x14095e4ec
00812F05  4C 8B 75 EF                     mov r14, qword ptr [rbp - 0x11]
00812F09  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00812F0D  49 8B CE                        mov rcx, r14
00812F10  BA FF FF FF 7F                  mov edx, 0x7fffffff
00812F15  E8 56 2B C2 FF                  call 0x140435a70
00812F1A  8B D8                           mov ebx, eax
00812F1C  85 C0                           test eax, eax
00812F1E  79 0F                           jns 0x140812f2f
00812F20  4C 8D 0D 91 88 82 FF            lea r9, [rip - 0x7d776f]
00812F27  41 B8 98 07 00 00               mov r8d, 0x798
00812F2D  EB AD                           jmp 0x140812edc
00812F2F  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00812F33  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00812F37  4C 3B C0                        cmp r8, rax
00812F3A  0F 82 46 01 00 00               jb 0x140813086
00812F40  4C 8B 4D 8F                     mov r9, qword ptr [rbp - 0x71]
00812F44  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00812F48  4C 21 6C 24 20                  and qword ptr [rsp + 0x20], r13
00812F4D  4C 2B C0                        sub r8, rax
00812F50  49 8B D6                        mov rdx, r14
00812F53  E8 40 02 00 00                  call 0x140813198
00812F58  8B D8                           mov ebx, eax
00812F5A  85 C0                           test eax, eax
00812F5C  79 24                           jns 0x140812f82
00812F5E  4C 8D 0D 23 87 82 FF            lea r9, [rip - 0x7d78dd]
00812F65  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00812F69  41 B8 A9 07 00 00               mov r8d, 0x7a9
00812F6F  48 8B D7                        mov rdx, rdi
00812F72  8B CE                           mov ecx, esi
00812F74  E8 73 B5 14 00                  call 0x14095e4ec
00812F79  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00812F7D  E9 81 FE FF FF                  jmp 0x140812e03
00812F82  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00812F86  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00812F8A  49 8B D5                        mov rdx, r13
00812F8D  44 8B C6                        mov r8d, esi
00812F90  E8 C3 F5 FF FF                  call 0x140812558
00812F95  8B D8                           mov ebx, eax
00812F97  85 C0                           test eax, eax
00812F99  79 1D                           jns 0x140812fb8
00812F9B  3D 34 00 00 C0                  cmp eax, 0xc0000034
00812FA0  0F 84 5D FE FF FF               je 0x140812e03
00812FA6  4C 8D 0D 63 85 82 FF            lea r9, [rip - 0x7d7a9d]
00812FAD  41 B8 B4 07 00 00               mov r8d, 0x7b4
00812FB3  E9 24 FF FF FF                  jmp 0x140812edc
00812FB8  45 33 C0                        xor r8d, r8d
00812FBB  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00812FBF  49 8B D6                        mov rdx, r14
00812FC2  E8 91 F5 FF FF                  call 0x140812558
00812FC7  8B D8                           mov ebx, eax
00812FC9  85 C0                           test eax, eax
00812FCB  79 12                           jns 0x140812fdf
00812FCD  4C 8D 0D 3C 85 82 FF            lea r9, [rip - 0x7d7ac4]
00812FD4  41 B8 BF 07 00 00               mov r8d, 0x7bf
00812FDA  E9 FD FE FF FF                  jmp 0x140812edc
00812FDF  49 8B D7                        mov rdx, r15
00812FE2  48 8D 4D 87                     lea rcx, [rbp - 0x79]
00812FE6  E8 71 F7 FF FF                  call 0x14081275c
00812FEB  8B D8                           mov ebx, eax
00812FED  3D 34 00 00 C0                  cmp eax, 0xc0000034
00812FF2  75 08                           jne 0x140812ffc
00812FF4  4C 8B 7D 87                     mov r15, qword ptr [rbp - 0x79]
00812FF8  33 C0                           xor eax, eax
00812FFA  EB 57                           jmp 0x140813053
00812FFC  85 C0                           test eax, eax
00812FFE  79 12                           jns 0x140813012
00813000  4C 8D 0D 31 88 82 FF            lea r9, [rip - 0x7d77cf]
00813007  41 B8 CD 07 00 00               mov r8d, 0x7cd
0081300D  E9 CA FE FF FF                  jmp 0x140812edc
00813012  4C 8B 7D 87                     mov r15, qword ptr [rbp - 0x79]
00813016  48 8D 4D D7                     lea rcx, [rbp - 0x29]
0081301A  49 8B D7                        mov rdx, r15
0081301D  45 33 C0                        xor r8d, r8d
00813020  E8 33 F5 FF FF                  call 0x140812558
00813025  8B D8                           mov ebx, eax
00813027  85 C0                           test eax, eax
00813029  79 24                           jns 0x14081304f
0081302B  4C 8D 0D DE 84 82 FF            lea r9, [rip - 0x7d7b22]
00813032  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00813036  41 B8 D7 07 00 00               mov r8d, 0x7d7
0081303C  48 8B D7                        mov rdx, rdi
0081303F  8B CE                           mov ecx, esi
00813041  E8 A6 B4 14 00                  call 0x14095e4ec
00813046  4C 8B 75 8F                     mov r14, qword ptr [rbp - 0x71]
0081304A  E9 BC FD FF FF                  jmp 0x140812e0b
0081304F  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
00813053  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
00813057  48 3B 4D E7                     cmp rcx, qword ptr [rbp - 0x19]
0081305B  72 22                           jb 0x14081307f
0081305D  48 3B C8                        cmp rcx, rax
00813060  72 1D                           jb 0x14081307f
00813062  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
00813066  4C 89 28                        mov qword ptr [rax], r13
00813069  4D 85 E4                        test r12, r12
0081306C  74 0A                           je 0x140813078
0081306E  83 7D 9B 00                     cmp dword ptr [rbp - 0x65], 0
00813072  74 04                           je 0x140813078
00813074  41 89 34 24                     mov dword ptr [r12], esi
00813078  45 33 ED                        xor r13d, r13d
0081307B  33 DB                           xor ebx, ebx
0081307D  EB C7                           jmp 0x140813046
0081307F  BB 34 00 00 C0                  mov ebx, 0xc0000034
00813084  EB C0                           jmp 0x140813046
00813086  BB 95 00 00 C0                  mov ebx, 0xc0000095
0081308B  4C 8D 0D 9E 84 82 FF            lea r9, [rip - 0x7d7b62]
00813092  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00813096  41 B8 9F 07 00 00               mov r8d, 0x79f
0081309C  E9 3F FE FF FF                  jmp 0x140812ee0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbpGetMergeRedirectPathInternal(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int16 v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m5F;
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
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 6257693)) ^ (v_rsp);
    v_stack_m48 = result;
    a2 = 0;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 8221728)));
    v_stack_m4C = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 8221746));
    v_stack_m70 = a4;
    v_stack_mC4 = a3;
    v_stack_m68 = a1;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    v_stack_mD0 = 0;
    v_stack_m90 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m88 = 0;
    v_stack_mD8 = 0;
    v_stack_mA0 = 0;
    v_stack_m98 = 0;
    v_stack_m60 = v_xmm0;
    if (a1 != 0) goto loc_00812BA4;
    goto loc_00812E69;
loc_00812BA4:
    *(unsigned __int64 *)(a1) = 0;
    if (0 == 0) goto loc_00812BB5;
    if (a3 != 0) {
        *(unsigned int *)(a2) = 0;
    }
    result = AslPathGetFileNamePart(a4, a2, a3, a4);
    if (result == a4) goto loc_00812E67;
loc_00812BD2:
    if ((result - 4) < a4) goto loc_00812E67;
    if (((unsigned __int16)(*(unsigned __int16 *)(result - 4))) == 92) goto loc_00812BEA;
    if (((unsigned __int16)(*(unsigned __int16 *)(result - 4))) != 47) goto loc_00812C00;
loc_00812BEA:
    result = wcsnicmp(result - 4, v_stack_m60, 10, a4);
    if ((unsigned int)(result) == 0) goto loc_00812C06;
loc_00812C00:
    v_rdi = (result - 4) - (2);
    goto loc_00812BD2;
loc_00812C06:
    result = RtlStringCchLengthW(result, (unsigned int)(0x7FFFFFFFULL), v_stack_mB0, a4);
    if (!sign_flag) goto loc_00812C44;
    v_stack_mE8 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8222045, (unsigned int)(0x72BULL), v_rip - 8221804);
    goto loc_00812E67;
loc_00812C44:
    if (v_stack_mC4 == 0) goto loc_00812C9F;
    v_stack_mE8 = v_stack_mB0;
    result = SdbpSafeAllocAndConcatW(v_stack_m98, v_rip - 8222109, 13, result);
    if (!sign_flag) goto loc_00812C99;
    v_stack_mE8 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8222130, (unsigned int)(0x737ULL), v_rip - 8222193);
    goto loc_00812E56;
loc_00812C99:
    goto loc_00812CA2;
loc_00812C9F:
loc_00812CA2:
    result = AslRegistryGetKey(v_stack_mB8, v_rip - 8223294, (unsigned int)(0x80000100ULL), 1);
    if (!sign_flag) goto loc_00812CF5;
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00812E07;
loc_00812CDE:
    v_stack_mE8 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8222221, (unsigned int)(0x748ULL), v_rip - 8223392);
    goto loc_00812E07;
loc_00812CF5:
    result = AslRegistryGetString(v_stack_mD0, v_stack_mB8, result, v_rip - 8223392);
    if (sign_flag) goto loc_00812E07;
    result = wcsicmp(v_stack_mD0, result, result, v_rip - 8223392);
    if ((unsigned int)(result) != 0) goto loc_00812D2C;
    goto loc_00812E07;
loc_00812D2C:
    if (v_stack_mC4 == 0) goto loc_00812D55;
    result = wcsicmp(v_stack_mD0, v_rip - 8222425, result, v_rip - 8223392);
    if ((unsigned int)(result) != 0) goto loc_00812D55;
    if (0 == 0) goto loc_00812D55;
    *(unsigned int *)(a2) = 1;
    v_rbx = 0;
    goto loc_00812E07;
loc_00812D55:
    result = SdbpSafeAllocAndConcatW(v_stack_mA0, v_rip - 8222489, 9, result);
    if (!sign_flag) goto loc_00812D8B;
    goto loc_00812CDE;
loc_00812D8B:
    result = AslRegistryGetUInt32(v_stack_mC0, v_stack_mB8, v_stack_mA0, v_rip - 8222456);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00812DAD;
    v_r14 = 0;
    goto loc_00812DC7;
loc_00812DAD:
    if (!sign_flag) goto loc_00812DC3;
    goto loc_00812CDE;
loc_00812DC3:
loc_00812DC7:
    result = AslRegistryGetUInt32(v_stack_mC8, v_stack_mB8, v_rip - 8222654, v_rip - 8222608);
    if (!sign_flag) goto loc_00812E91;
    v_stack_mE8 = (unsigned int)(result);
loc_00812DFC:
    result = AslLogCallPrintf(1, v_rip - 8222500, (unsigned int)(0x779ULL), v_rip - 8222663);
loc_00812E03:
loc_00812E07:
loc_00812E0B:
    result = v_stack_mB8 - 1;
    if ((v_stack_mB8 - 1) <= -3) {
        result = ZwClose(v_stack_mB8, v_rip - 8222500, (unsigned int)(0x779ULL), v_rip - 8222663);
    }
    if (v_stack_mD0 != 0) {
        a2 = v_stack_mD0;
        result = AslFree(v_stack_mB8, a2, (unsigned int)(0x779ULL), v_rip - 8222663);
    }
    if (0 != 0) {
        a2 = 0;
        result = AslFree(v_stack_mB8, a2, (unsigned int)(0x779ULL), v_rip - 8222663);
    }
    if (v_stack_mD8 != 0) {
        a2 = v_stack_mD8;
        result = AslFree(v_stack_mB8, a2, (unsigned int)(0x779ULL), v_rip - 8222663);
    }
    result = v_stack_mA0;
    if (v_stack_mA0 != 0) {
        a2 = v_stack_mA0;
        result = AslFree(v_stack_mB8, a2, (unsigned int)(0x779ULL), v_rip - 8222663);
    }
    result = v_stack_m98;
    if (v_stack_m98 != 0) {
        a2 = v_stack_m98;
        result = AslFree(v_stack_mB8, a2, (unsigned int)(0x779ULL), v_rip - 8222663);
    }
loc_00812E69:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x779ULL), v_rip - 8222663);
    v_rsp = (v_rsp) + (208);
    return result;
loc_00812E91:
    if (v_stack_mC8 < ((unsigned int)(v_stack_mD0))) {
        a4 = v_rip - 8222949;
        a3 = 0x782ULL;
        a2 = v_rip - 8222656;
        a1 = 1;
        result = AslLogCallPrintf(a1, a2, a3, a4);
    }
    result = AslRegistryGetUInt32(v_stack_mC8, v_stack_mB8, v_rip - 8223000, a4);
    if (!sign_flag) goto loc_00812EE8;
loc_00812EDC:
    v_stack_p20 = (unsigned int)(result);
loc_00812EE0:
    goto loc_00812DFC;
loc_00812EE8:
    if (((unsigned int)(v_stack_mD0)) < v_stack_mC8) {
        a4 = v_rip - 8223141;
        a3 = 0x791ULL;
        a2 = v_rip - 8222656;
        a1 = 1;
        result = AslLogCallPrintf(a1, a2, a3, a4);
    }
    result = RtlStringCchLengthW(v_stack_m70, (unsigned int)(0x7FFFFFFFULL), v_stack_m90, a4);
    if (!sign_flag) goto loc_00812F2F;
    goto loc_00812EDC;
loc_00812F2F:
    if (v_stack_m90 < v_stack_mB0) goto loc_00813086;
    a3 = (v_stack_m90) - (v_stack_mB0);
    result = SdbpSafeAllocAndConcatW(v_stack_mA8, v_stack_m70, a3, v_stack_mD0);
    if (!sign_flag) goto loc_00812F82;
    v_stack_p20 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8222656, (unsigned int)(0x7A9ULL), v_rip - 8222941);
    goto loc_00812E03;
loc_00812F82:
    result = SdbpGetFileTimestamp(v_stack_m80, v_stack_mA8, 1, v_rip - 8222941);
    if (!sign_flag) goto loc_00812FB8;
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00812E03;
    goto loc_00812EDC;
loc_00812FB8:
    a3 = 0;
    result = SdbpGetFileTimestamp(v_stack_m78, v_stack_m70, a3, v_rip - 8223389);
    if (!sign_flag) goto loc_00812FDF;
    goto loc_00812EDC;
loc_00812FDF:
    result = SdbpGetManifestedMergeStubAlloc(v_stack_mD8, v_stack_mD8, (unsigned int)(0x7BFULL), v_rip - 8223428);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00812FFC;
    result = 0;
    goto loc_00813053;
loc_00812FFC:
    if (!sign_flag) goto loc_00813012;
    goto loc_00812EDC;
loc_00813012:
    a3 = 0;
    result = SdbpGetFileTimestamp(v_stack_m88, v_stack_mD8, a3, v_rip - 8222671);
    if (!sign_flag) goto loc_0081304F;
    v_stack_p20 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8222656, (unsigned int)(0x7D7ULL), v_rip - 8223522);
loc_00813046:
    goto loc_00812E0B;
loc_0081304F:
loc_00813053:
    if (v_stack_m80 < v_stack_m78) goto loc_0081307F;
    if (v_stack_m80 < v_stack_m88) goto loc_0081307F;
    *(unsigned __int64 *)(v_stack_m68) = v_stack_mA8;
    if (a2 == 0) goto loc_00813078;
    if (v_stack_mC4 != 0) {
        *(unsigned int *)(a2) = 1;
    }
    v_r13 = 0;
    v_rbx = 0;
    goto loc_00813046;
loc_0081307F:
    goto loc_00813046;
loc_00813086:
    v_stack_p20 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_00812EE0;
}
```

## 5. (Beta) C Style

```c
int64_t SdbpGetMergeRedirectPathInternal(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint16_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m5F;
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
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x5F7C1D)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg2 = 0;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x7D7420)));
    v_stack_m4C = (uint16_t)(*(uint16_t *)(v_rip - 0x7D7432));
    v_stack_m70 = Arg4;
    v_stack_mC4 = Arg3;
    v_stack_m68 = Arg1;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    v_stack_mD0 = 0;
    v_stack_m90 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m88 = 0;
    v_stack_mD8 = 0;
    v_stack_mA0 = 0;
    v_stack_m98 = 0;
    v_stack_m60 = v_xmm0;
    if (Arg1 != 0) goto loc_00812BA4;
    goto loc_00812E69;
loc_00812BA4:
    *(uint64_t *)(Arg1) = 0;
    if (0 == 0) goto loc_00812BB5;
    if (Arg3 != 0) {
        *(uint32_t *)(Arg2) = 0;
    }
    result = AslPathGetFileNamePart(Arg4, Arg2, Arg3, Arg4);
    if (result == Arg4) goto loc_00812E67;
loc_00812BD2:
    if ((result - 4) < Arg4) goto loc_00812E67;
    if (((uint16_t)(*(uint16_t *)(result - 0x4))) == 92) goto loc_00812BEA;
    if (((uint16_t)(*(uint16_t *)(result - 0x4))) != 47) goto loc_00812C00;
loc_00812BEA:
    result = wcsnicmp(result - 4, v_stack_m60, 10, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00812C06;
loc_00812C00:
    local_rdi = (result - 4) - (2);
    goto loc_00812BD2;
loc_00812C06:
    result = RtlStringCchLengthW(result, (uint32_t)(0x7FFFFFFFULL), v_stack_mB0, Arg4);
    if (!sign_flag) goto loc_00812C44;
    v_stack_mE8 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8222045, (uint32_t)(0x72BULL), v_rip - 8221804);
    goto loc_00812E67;
loc_00812C44:
    if (v_stack_mC4 == 0) goto loc_00812C9F;
    v_stack_mE8 = v_stack_mB0;
    result = SdbpSafeAllocAndConcatW(v_stack_m98, v_rip - 8222109, 13, result);
    if (!sign_flag) goto loc_00812C99;
    v_stack_mE8 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8222130, (uint32_t)(0x737ULL), v_rip - 8222193);
    goto loc_00812E56;
loc_00812C99:
    goto loc_00812CA2;
loc_00812C9F:
loc_00812CA2:
    result = AslRegistryGetKey(v_stack_mB8, v_rip - 8223294, (uint32_t)(0x80000100ULL), 1);
    if (!sign_flag) goto loc_00812CF5;
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00812E07;
loc_00812CDE:
    v_stack_mE8 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8222221, (uint32_t)(0x748ULL), v_rip - 8223392);
    goto loc_00812E07;
loc_00812CF5:
    result = AslRegistryGetString(v_stack_mD0, v_stack_mB8, result, v_rip - 8223392);
    if (sign_flag) goto loc_00812E07;
    result = wcsicmp(v_stack_mD0, result, result, v_rip - 8223392);
    if ((uint32_t)(result) != 0) goto loc_00812D2C;
    goto loc_00812E07;
loc_00812D2C:
    if (v_stack_mC4 == 0) goto loc_00812D55;
    result = wcsicmp(v_stack_mD0, v_rip - 8222425, result, v_rip - 8223392);
    if ((uint32_t)(result) != 0) goto loc_00812D55;
    if (0 == 0) goto loc_00812D55;
    *(uint32_t *)(Arg2) = 1;
    local_rbx = 0;
    goto loc_00812E07;
loc_00812D55:
    result = SdbpSafeAllocAndConcatW(v_stack_mA0, v_rip - 8222489, 9, result);
    if (!sign_flag) goto loc_00812D8B;
    goto loc_00812CDE;
loc_00812D8B:
    result = AslRegistryGetUInt32(v_stack_mC0, v_stack_mB8, v_stack_mA0, v_rip - 8222456);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00812DAD;
    local_r14 = 0;
    goto loc_00812DC7;
loc_00812DAD:
    if (!sign_flag) goto loc_00812DC3;
    goto loc_00812CDE;
loc_00812DC3:
loc_00812DC7:
    result = AslRegistryGetUInt32(v_stack_mC8, v_stack_mB8, v_rip - 8222654, v_rip - 8222608);
    if (!sign_flag) goto loc_00812E91;
    v_stack_mE8 = (uint32_t)(result);
loc_00812DFC:
    result = AslLogCallPrintf(1, v_rip - 8222500, (uint32_t)(0x779ULL), v_rip - 8222663);
loc_00812E03:
loc_00812E07:
loc_00812E0B:
    result = v_stack_mB8 - 1;
    if ((v_stack_mB8 - 1) <= -3) {
        result = ZwClose(v_stack_mB8, v_rip - 8222500, (uint32_t)(0x779ULL), v_rip - 8222663);
    }
    if (v_stack_mD0 != 0) {
        Arg2 = v_stack_mD0;
        result = AslFree(v_stack_mB8, Arg2, (uint32_t)(0x779ULL), v_rip - 8222663);
    }
    if (0 != 0) {
        Arg2 = 0;
        result = AslFree(v_stack_mB8, Arg2, (uint32_t)(0x779ULL), v_rip - 8222663);
    }
    if (v_stack_mD8 != 0) {
        Arg2 = v_stack_mD8;
        result = AslFree(v_stack_mB8, Arg2, (uint32_t)(0x779ULL), v_rip - 8222663);
    }
    result = v_stack_mA0;
    if (v_stack_mA0 != 0) {
        Arg2 = v_stack_mA0;
        result = AslFree(v_stack_mB8, Arg2, (uint32_t)(0x779ULL), v_rip - 8222663);
    }
    result = v_stack_m98;
    if (v_stack_m98 != 0) {
        Arg2 = v_stack_m98;
        result = AslFree(v_stack_mB8, Arg2, (uint32_t)(0x779ULL), v_rip - 8222663);
    }
loc_00812E69:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x779ULL), v_rip - 8222663);
    local_rsp = (local_rsp) + (208);
    return result;
loc_00812E91:
    if (v_stack_mC8 < ((uint32_t)(v_stack_mD0))) {
        Arg4 = v_rip - 8222949;
        Arg3 = 0x782ULL;
        Arg2 = v_rip - 8222656;
        Arg1 = 1;
        result = AslLogCallPrintf(Arg1, Arg2, Arg3, Arg4);
    }
    result = AslRegistryGetUInt32(v_stack_mC8, v_stack_mB8, v_rip - 8223000, Arg4);
    if (!sign_flag) goto loc_00812EE8;
loc_00812EDC:
    v_stack_p20 = (uint32_t)(result);
loc_00812EE0:
    goto loc_00812DFC;
loc_00812EE8:
    if (((uint32_t)(v_stack_mD0)) < v_stack_mC8) {
        Arg4 = v_rip - 8223141;
        Arg3 = 0x791ULL;
        Arg2 = v_rip - 8222656;
        Arg1 = 1;
        result = AslLogCallPrintf(Arg1, Arg2, Arg3, Arg4);
    }
    result = RtlStringCchLengthW(v_stack_m70, (uint32_t)(0x7FFFFFFFULL), v_stack_m90, Arg4);
    if (!sign_flag) goto loc_00812F2F;
    goto loc_00812EDC;
loc_00812F2F:
    if (v_stack_m90 < v_stack_mB0) goto loc_00813086;
    Arg3 = (v_stack_m90) - (v_stack_mB0);
    result = SdbpSafeAllocAndConcatW(v_stack_mA8, v_stack_m70, Arg3, v_stack_mD0);
    if (!sign_flag) goto loc_00812F82;
    v_stack_p20 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8222656, (uint32_t)(0x7A9ULL), v_rip - 8222941);
    goto loc_00812E03;
loc_00812F82:
    result = SdbpGetFileTimestamp(v_stack_m80, v_stack_mA8, 1, v_rip - 8222941);
    if (!sign_flag) goto loc_00812FB8;
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00812E03;
    goto loc_00812EDC;
loc_00812FB8:
    Arg3 = 0;
    result = SdbpGetFileTimestamp(v_stack_m78, v_stack_m70, Arg3, v_rip - 8223389);
    if (!sign_flag) goto loc_00812FDF;
    goto loc_00812EDC;
loc_00812FDF:
    result = SdbpGetManifestedMergeStubAlloc(v_stack_mD8, v_stack_mD8, (uint32_t)(0x7BFULL), v_rip - 8223428);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00812FFC;
    result = 0;
    goto loc_00813053;
loc_00812FFC:
    if (!sign_flag) goto loc_00813012;
    goto loc_00812EDC;
loc_00813012:
    Arg3 = 0;
    result = SdbpGetFileTimestamp(v_stack_m88, v_stack_mD8, Arg3, v_rip - 8222671);
    if (!sign_flag) goto loc_0081304F;
    v_stack_p20 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8222656, (uint32_t)(0x7D7ULL), v_rip - 8223522);
loc_00813046:
    goto loc_00812E0B;
loc_0081304F:
loc_00813053:
    if (v_stack_m80 < v_stack_m78) goto loc_0081307F;
    if (v_stack_m80 < v_stack_m88) goto loc_0081307F;
    *(uint64_t *)(v_stack_m68) = v_stack_mA8;
    if (Arg2 == 0) goto loc_00813078;
    if (v_stack_mC4 != 0) {
        *(uint32_t *)(Arg2) = 1;
    }
    local_r13 = 0;
    local_rbx = 0;
    goto loc_00813046;
loc_0081307F:
    goto loc_00813046;
loc_00813086:
    v_stack_p20 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_00812EE0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00812B00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
