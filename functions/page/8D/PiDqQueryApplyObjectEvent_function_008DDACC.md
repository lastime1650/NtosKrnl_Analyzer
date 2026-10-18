# PiDqQueryApplyObjectEvent

- RVA: `0x008DDACC`–`0x008DE1A9` (길이 `1,757` bytes)
- VA: `0x00000001408DDACC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00085AA4`
- 디코드: `463`개 명령, `1,757/1,757` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008DDB23` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DDB38` → [RtlLookupElementGenericTableAvl](../../text/3F/RtlLookupElementGenericTableAvl_function_003FEFB0.md) (function, `0x003FEFB0`)
- `0x008DDB43` → [PiDqQueryUnlock](PiDqQueryUnlock_function_008DDA6C.md) (function, `0x008DDA6C`)
- `0x008DDD24` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DDD3C` → [RtlLookupElementGenericTableAvl](../../text/3F/RtlLookupElementGenericTableAvl_function_003FEFB0.md) (function, `0x003FEFB0`)
- `0x008DDD47` → [PiDqQueryUnlock](PiDqQueryUnlock_function_008DDA6C.md) (function, `0x008DDA6C`)
- `0x008DDD8F` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DDD9A` → [PiDqQueryDeleteObjectFromResultSet](PiDqQueryDeleteObjectFromResultSet_function_008DC600.md) (function, `0x008DC600`)
- `0x008DDDA2` → [PiDqQueryUnlock](PiDqQueryUnlock_function_008DDA6C.md) (function, `0x008DDA6C`)
- `0x008DDDBA` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DDDC9` → [PiDqQueryFreeActiveData](PiDqQueryFreeActiveData_function_008DE4FC.md) (function, `0x008DE4FC`)
- `0x008DDDD1` → [PiDqQueryUnlock](PiDqQueryUnlock_function_008DDA6C.md) (function, `0x008DDA6C`)
- `0x008DDE44` → [PiPnpRtlApplyMandatoryFilters](../8E/PiPnpRtlApplyMandatoryFilters_function_008E5C80.md) (function, `0x008E5C80`)
- `0x008DDE95` → [PiDqQueryEvaluateFilter](../8E/PiDqQueryEvaluateFilter_function_008E01C4.md) (function, `0x008E01C4`)
- `0x008DDF6A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x008DDFDC` → [PiDqSameUserHive](../70/PiDqSameUserHive_function_007055B0.md) (function, `0x007055B0`)
- `0x008DE03A` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DE045` → [PiDqQueryAddObjectToResultSet](../A5/PiDqQueryAddObjectToResultSet_function_00A55624.md) (function, `0x00A55624`)
- `0x008DE050` → [PiDqQueryUnlock](PiDqQueryUnlock_function_008DDA6C.md) (function, `0x008DDA6C`)
- `0x008DE06F` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DE07A` → [PiDqQueryDeleteObjectFromResultSet](PiDqQueryDeleteObjectFromResultSet_function_008DC600.md) (function, `0x008DC600`)
- `0x008DE082` → [PiDqQueryUnlock](PiDqQueryUnlock_function_008DDA6C.md) (function, `0x008DDA6C`)
- `0x008DE0AB` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x008DE0F0` → [PiDqQueryActionQueueEntryCreate](PiDqQueryActionQueueEntryCreate_function_008DBE9C.md) (function, `0x008DBE9C`)
- `0x008DE100` → [PiDqQueryLock](PiDqQueryLock_function_008DDA0C.md) (function, `0x008DDA0C`)
- `0x008DE10C` → [PiDqQueryAppendActionEntry](PiDqQueryAppendActionEntry_function_008DEB34.md) (function, `0x008DEB34`)
- `0x008DE14C` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x008DE170` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)

### Direct callers
- [PiDqObjectManagerServiceActionQueue](PiDqObjectManagerServiceActionQueue_function_008DD640.md) at `0x008DD928`

### Static image references
- `0x008DDE2D` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x008DDB38` → [RtlLookupElementGenericTableAvl](../../text/3F/RtlLookupElementGenericTableAvl_function_003FEFB0.md) (`PAGE` → `.text`)
  - `0x008DDD3C` → [RtlLookupElementGenericTableAvl](../../text/3F/RtlLookupElementGenericTableAvl_function_003FEFB0.md) (`PAGE` → `.text`)
  - `0x008DDF6A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x008DE0AB` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x008DE14C` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x008DE170` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x008DDF5C` → [sub_00B1CE1E + 0x85](../B1/Unknown_function_00B1CE1E.md) (`tail-transfer`)
  - `0x008DDF74` → [sub_00B1CE1E + 0x90](../B1/Unknown_function_00B1CE1E.md) (`tail-transfer`)
  - `0x008DDF7E` → [sub_00B1CE1E + 0x6E](../B1/Unknown_function_00B1CE1E.md) (`tail-transfer`)
  - `0x008DDFCB` → [sub_00B1CE1E + 0x9D](../B1/Unknown_function_00B1CE1E.md) (`tail-transfer`)
  - `0x008DE123` → [sub_00B1CE1E](../B1/Unknown_function_00B1CE1E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008DDACC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008DDAD1  55                              push rbp
008DDAD2  56                              push rsi
008DDAD3  57                              push rdi
008DDAD4  41 54                           push r12
008DDAD6  41 55                           push r13
008DDAD8  41 56                           push r14
008DDADA  41 57                           push r15
008DDADC  48 8B EC                        mov rbp, rsp
008DDADF  48 83 EC 50                     sub rsp, 0x50
008DDAE3  8B 42 04                        mov eax, dword ptr [rdx + 4]
008DDAE6  45 33 D2                        xor r10d, r10d
008DDAE9  44 89 55 E4                     mov dword ptr [rbp - 0x1c], r10d
008DDAED  48 8B F1                        mov rsi, rcx
008DDAF0  4C 89 55 F0                     mov qword ptr [rbp - 0x10], r10
008DDAF4  41 8A CA                        mov cl, r10b
008DDAF7  88 4D E1                        mov byte ptr [rbp - 0x1f], cl
008DDAFA  41 8A DA                        mov bl, r10b
008DDAFD  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDB00  4C 8B F2                        mov r14, rdx
008DDB03  44 89 55 E8                     mov dword ptr [rbp - 0x18], r10d
008DDB07  45 8B FA                        mov r15d, r10d
008DDB0A  44 88 55 58                     mov byte ptr [rbp + 0x58], r10b
008DDB0E  45 8A E2                        mov r12b, r10b
008DDB11  44 88 55 50                     mov byte ptr [rbp + 0x50], r10b
008DDB15  45 8A EA                        mov r13b, r10b
008DDB18  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
008DDB1C  A8 01                           test al, 1
008DDB1E  74 37                           je 0x1408ddb57
008DDB20  48 8B CE                        mov rcx, rsi
008DDB23  E8 E4 FE FF FF                  call 0x1408dda0c
008DDB28  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
008DDB2C  48 8D 4E 48                     lea rcx, [rsi + 0x48]
008DDB30  48 8D 55 F8                     lea rdx, [rbp - 8]
008DDB34  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008DDB38  E8 73 14 B2 FF                  call 0x1403fefb0
008DDB3D  48 8B CE                        mov rcx, rsi
008DDB40  48 8B D8                        mov rbx, rax
008DDB43  E8 24 FF FF FF                  call 0x1408dda6c
008DDB48  45 33 D2                        xor r10d, r10d
008DDB4B  48 85 DB                        test rbx, rbx
008DDB4E  41 8A DA                        mov bl, r10b
008DDB51  0F 95 C1                        setne cl
008DDB54  88 4D E1                        mov byte ptr [rbp - 0x1f], cl
008DDB57  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
008DDB5B  A8 01                           test al, 1
008DDB5D  0F 85 AA 01 00 00               jne 0x1408ddd0d
008DDB63  A8 02                           test al, 2
008DDB65  0F 85 AA 01 00 00               jne 0x1408ddd15
008DDB6B  A8 08                           test al, 8
008DDB6D  75 0A                           jne 0x1408ddb79
008DDB6F  45 39 56 4C                     cmp dword ptr [r14 + 0x4c], r10d
008DDB73  0F 86 9C 01 00 00               jbe 0x1408ddd15
008DDB79  A8 04                           test al, 4
008DDB7B  0F 85 4F 04 00 00               jne 0x1408ddfd0
008DDB81  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
008DDB85  8B 4A 28                        mov ecx, dword ptr [rdx + 0x28]
008DDB88  44 8B C1                        mov r8d, ecx
008DDB8B  41 83 E0 04                     and r8d, 4
008DDB8F  F6 C1 02                        test cl, 2
008DDB92  0F 85 F4 03 00 00               jne 0x1408ddf8c
008DDB98  8B 42 40                        mov eax, dword ptr [rdx + 0x40]
008DDB9B  45 85 C0                        test r8d, r8d
008DDB9E  75 4B                           jne 0x1408ddbeb
008DDBA0  45 8B E2                        mov r12d, r10d
008DDBA3  85 C0                           test eax, eax
008DDBA5  0F 84 30 02 00 00               je 0x1408ddddb
008DDBAB  41 8B FC                        mov edi, r12d
008DDBAE  45 8B FA                        mov r15d, r10d
008DDBB1  48 C1 E7 05                     shl rdi, 5
008DDBB5  48 03 7A 48                     add rdi, qword ptr [rdx + 0x48]
008DDBB9  45 3B 7E 4C                     cmp r15d, dword ptr [r14 + 0x4c]
008DDBBD  73 1A                           jae 0x1408ddbd9
008DDBBF  41 8B DF                        mov ebx, r15d
008DDBC2  48 C1 E3 05                     shl rbx, 5
008DDBC6  42 8B 44 33 60                  mov eax, dword ptr [rbx + r14 + 0x60]
008DDBCB  39 47 10                        cmp dword ptr [rdi + 0x10], eax
008DDBCE  0F 84 E5 02 00 00               je 0x1408ddeb9
008DDBD4  41 FF C7                        inc r15d
008DDBD7  EB E0                           jmp 0x1408ddbb9
008DDBD9  8A 5D 48                        mov bl, byte ptr [rbp + 0x48]
008DDBDC  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
008DDBE0  41 FF C4                        inc r12d
008DDBE3  44 3B 62 40                     cmp r12d, dword ptr [rdx + 0x40]
008DDBE7  72 C2                           jb 0x1408ddbab
008DDBE9  EB 53                           jmp 0x1408ddc3e
008DDBEB  45 8B EA                        mov r13d, r10d
008DDBEE  85 C0                           test eax, eax
008DDBF0  74 50                           je 0x1408ddc42
008DDBF2  45 8B FD                        mov r15d, r13d
008DDBF5  41 8A DA                        mov bl, r10b
008DDBF8  49 C1 E7 05                     shl r15, 5
008DDBFC  45 8B E2                        mov r12d, r10d
008DDBFF  4C 03 7A 48                     add r15, qword ptr [rdx + 0x48]
008DDC03  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDC06  45 39 56 4C                     cmp dword ptr [r14 + 0x4c], r10d
008DDC0A  76 25                           jbe 0x1408ddc31
008DDC0C  41 8B FC                        mov edi, r12d
008DDC0F  41 8A DA                        mov bl, r10b
008DDC12  48 C1 E7 05                     shl rdi, 5
008DDC16  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDC19  42 8B 44 37 60                  mov eax, dword ptr [rdi + r14 + 0x60]
008DDC1E  41 39 47 10                     cmp dword ptr [r15 + 0x10], eax
008DDC22  0F 84 E3 02 00 00               je 0x1408ddf0b
008DDC28  41 FF C4                        inc r12d
008DDC2B  45 3B 66 4C                     cmp r12d, dword ptr [r14 + 0x4c]
008DDC2F  72 DB                           jb 0x1408ddc0c
008DDC31  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
008DDC35  41 FF C5                        inc r13d
008DDC38  44 3B 6A 40                     cmp r13d, dword ptr [rdx + 0x40]
008DDC3C  72 B4                           jb 0x1408ddbf2
008DDC3E  44 8A 65 50                     mov r12b, byte ptr [rbp + 0x50]
008DDC42  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
008DDC46  44 39 50 14                     cmp dword ptr [rax + 0x14], r10d
008DDC4A  75 0F                           jne 0x1408ddc5b
008DDC4C  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
008DDC50  A8 08                           test al, 8
008DDC52  0F 85 A0 03 00 00               jne 0x1408ddff8
008DDC58  45 8A E2                        mov r12b, r10b
008DDC5B  41 8B FA                        mov edi, r10d
008DDC5E  41 3B 7E 4C                     cmp edi, dword ptr [r14 + 0x4c]
008DDC62  73 7C                           jae 0x1408ddce0
008DDC64  8B DF                           mov ebx, edi
008DDC66  45 8B FA                        mov r15d, r10d
008DDC69  48 C1 E3 05                     shl rbx, 5
008DDC6D  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
008DDC71  45 3B 78 50                     cmp r15d, dword ptr [r8 + 0x50]
008DDC75  73 1C                           jae 0x1408ddc93
008DDC77  4D 8B 40 58                     mov r8, qword ptr [r8 + 0x58]
008DDC7B  41 8B C7                        mov eax, r15d
008DDC7E  48 6B D0 38                     imul rdx, rax, 0x38
008DDC82  42 8B 44 33 60                  mov eax, dword ptr [rbx + r14 + 0x60]
008DDC87  42 39 44 02 18                  cmp dword ptr [rdx + r8 + 0x18], eax
008DDC8C  74 09                           je 0x1408ddc97
008DDC8E  41 FF C7                        inc r15d
008DDC91  EB DA                           jmp 0x1408ddc6d
008DDC93  FF C7                           inc edi
008DDC95  EB C7                           jmp 0x1408ddc5e
008DDC97  4A 8B 4C 02 08                  mov rcx, qword ptr [rdx + r8 + 8]
008DDC9C  4A 2B 4C 33 50                  sub rcx, qword ptr [rbx + r14 + 0x50]
008DDCA1  75 0A                           jne 0x1408ddcad
008DDCA3  4A 8B 4C 02 10                  mov rcx, qword ptr [rdx + r8 + 0x10]
008DDCA8  4A 2B 4C 33 58                  sub rcx, qword ptr [rbx + r14 + 0x58]
008DDCAD  48 85 C9                        test rcx, rcx
008DDCB0  75 DC                           jne 0x1408ddc8e
008DDCB2  42 8B 44 33 64                  mov eax, dword ptr [rbx + r14 + 0x64]
008DDCB7  42 39 44 02 1C                  cmp dword ptr [rdx + r8 + 0x1c], eax
008DDCBC  75 D0                           jne 0x1408ddc8e
008DDCBE  4A 8B 4C 02 20                  mov rcx, qword ptr [rdx + r8 + 0x20]
008DDCC3  4A 8B 54 33 68                  mov rdx, qword ptr [rbx + r14 + 0x68]
008DDCC8  48 3B CA                        cmp rcx, rdx
008DDCCB  0F 85 69 04 00 00               jne 0x1408de13a
008DDCD1  42 83 7C 33 64 01               cmp dword ptr [rbx + r14 + 0x64], 1
008DDCD7  0F 84 44 03 00 00               je 0x1408de021
008DDCDD  41 B4 01                        mov r12b, 1
008DDCE0  8A 5D 48                        mov bl, byte ptr [rbp + 0x48]
008DDCE3  84 DB                           test bl, bl
008DDCE5  0F 85 98 02 00 00               jne 0x1408ddf83
008DDCEB  45 84 E4                        test r12b, r12b
008DDCEE  0F 85 8F 02 00 00               jne 0x1408ddf83
008DDCF4  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
008DDCFC  48 83 C4 50                     add rsp, 0x50
008DDD00  41 5F                           pop r15
008DDD02  41 5E                           pop r14
008DDD04  41 5D                           pop r13
008DDD06  41 5C                           pop r12
008DDD08  5F                              pop rdi
008DDD09  5E                              pop rsi
008DDD0A  5D                              pop rbp
008DDD0B  C3                              ret
008DDD0C  CC                              int3
008DDD0D  84 C9                           test cl, cl
008DDD0F  0F 85 4E FE FF FF               jne 0x1408ddb63
008DDD15  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
008DDD19  A8 01                           test al, 1
008DDD1B  0F 85 AD 03 00 00               jne 0x1408de0ce
008DDD21  48 8B CE                        mov rcx, rsi
008DDD24  E8 E3 FC FF FF                  call 0x1408dda0c
008DDD29  49 8D 7E 08                     lea rdi, [r14 + 8]
008DDD2D  48 8B 07                        mov rax, qword ptr [rdi]
008DDD30  48 8D 4E 48                     lea rcx, [rsi + 0x48]
008DDD34  48 8D 55 50                     lea rdx, [rbp + 0x50]
008DDD38  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
008DDD3C  E8 6F 12 B2 FF                  call 0x1403fefb0
008DDD41  48 8B CE                        mov rcx, rsi
008DDD44  48 8B D8                        mov rbx, rax
008DDD47  E8 20 FD FF FF                  call 0x1408dda6c
008DDD4C  45 33 D2                        xor r10d, r10d
008DDD4F  48 85 DB                        test rbx, rbx
008DDD52  41 0F 95 C5                     setne r13b
008DDD56  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
008DDD5A  A8 02                           test al, 2
008DDD5C  0F 85 F9 02 00 00               jne 0x1408de05b
008DDD62  48 8B D7                        mov rdx, rdi
008DDD65  A8 01                           test al, 1
008DDD67  75 7E                           jne 0x1408ddde7
008DDD69  45 84 E4                        test r12b, r12b
008DDD6C  75 75                           jne 0x1408ddde3
008DDD6E  41 8A CD                        mov cl, r13b
008DDD71  84 C9                           test cl, cl
008DDD73  0F 85 87 02 00 00               jne 0x1408de000
008DDD79  45 84 ED                        test r13b, r13b
008DDD7C  0F 84 96 02 00 00               je 0x1408de018
008DDD82  48 8B CE                        mov rcx, rsi
008DDD85  C6 45 58 01                     mov byte ptr [rbp + 0x58], 1
008DDD89  41 BF 03 00 00 00               mov r15d, 3
008DDD8F  E8 78 FC FF FF                  call 0x1408dda0c
008DDD94  48 8B 17                        mov rdx, qword ptr [rdi]
008DDD97  48 8B CE                        mov rcx, rsi
008DDD9A  E8 61 E8 FF FF                  call 0x1408dc600
008DDD9F  48 8B CE                        mov rcx, rsi
008DDDA2  E8 C5 FC FF FF                  call 0x1408dda6c
008DDDA7  45 33 D2                        xor r10d, r10d
008DDDAA  8A 5D 58                        mov bl, byte ptr [rbp + 0x58]
008DDDAD  44 39 55 E4                     cmp dword ptr [rbp - 0x1c], r10d
008DDDB1  0F 8D 24 03 00 00               jge 0x1408de0db
008DDDB7  48 8B CE                        mov rcx, rsi
008DDDBA  E8 4D FC FF FF                  call 0x1408dda0c
008DDDBF  83 8E D8 00 00 00 01            or dword ptr [rsi + 0xd8], 1
008DDDC6  48 8B CE                        mov rcx, rsi
008DDDC9  E8 2E 07 00 00                  call 0x1408de4fc
008DDDCE  48 8B CE                        mov rcx, rsi
008DDDD1  E8 96 FC FF FF                  call 0x1408dda6c
008DDDD6  E9 19 FF FF FF                  jmp 0x1408ddcf4
008DDDDB  45 8A E7                        mov r12b, r15b
008DDDDE  E9 5F FE FF FF                  jmp 0x1408ddc42
008DDDE3  49 8D 56 08                     lea rdx, [r14 + 8]
008DDDE7  48 8D 5E 18                     lea rbx, [rsi + 0x18]
008DDDEB  4C 8B 03                        mov r8, qword ptr [rbx]
008DDDEE  41 8B 48 14                     mov ecx, dword ptr [r8 + 0x14]
008DDDF2  85 C9                           test ecx, ecx
008DDDF4  0F 85 A5 01 00 00               jne 0x1408ddf9f
008DDDFA  B1 01                           mov cl, 1
008DDDFC  88 4D 50                        mov byte ptr [rbp + 0x50], cl
008DDDFF  EB 08                           jmp 0x1408dde09
008DDE01  84 C0                           test al, al
008DDE03  0F 84 70 FF FF FF               je 0x1408ddd79
008DDE09  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
008DDE0D  49 8D 7E 08                     lea rdi, [r14 + 8]
008DDE11  41 BC 34 00 00 C0               mov r12d, 0xc0000034
008DDE17  44 39 50 14                     cmp dword ptr [rax + 0x14], r10d
008DDE1B  75 51                           jne 0x1408dde6e
008DDE1D  48 8B 17                        mov rdx, qword ptr [rdi]
008DDE20  48 8D 4D 50                     lea rcx, [rbp + 0x50]
008DDE24  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008DDE29  48 8D 46 20                     lea rax, [rsi + 0x20]
008DDE2D  48 8B 0D 64 85 58 00            mov rcx, qword ptr [rip + 0x588564]
008DDE34  45 33 C9                        xor r9d, r9d
008DDE37  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DDE3C  44 8B 42 1C                     mov r8d, dword ptr [rdx + 0x1c]
008DDE40  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
008DDE44  E8 37 7E 00 00                  call 0x1408e5c80
008DDE49  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
008DDE4C  41 3B C4                        cmp eax, r12d
008DDE4F  0F 84 32 03 00 00               je 0x1408de187
008DDE55  3D 25 02 00 C0                  cmp eax, 0xc0000225
008DDE5A  0F 84 27 03 00 00               je 0x1408de187
008DDE60  45 33 D2                        xor r10d, r10d
008DDE63  85 C0                           test eax, eax
008DDE65  0F 88 4C FF FF FF               js 0x1408dddb7
008DDE6B  8A 4D 50                        mov cl, byte ptr [rbp + 0x50]
008DDE6E  84 C9                           test cl, cl
008DDE70  0F 84 03 FF FF FF               je 0x1408ddd79
008DDE76  48 8B 03                        mov rax, qword ptr [rbx]
008DDE79  4C 39 50 58                     cmp qword ptr [rax + 0x58], r10
008DDE7D  0F 84 EE FE FF FF               je 0x1408ddd71
008DDE83  49 8D 7E 08                     lea rdi, [r14 + 8]
008DDE87  48 8B CE                        mov rcx, rsi
008DDE8A  48 8B 17                        mov rdx, qword ptr [rdi]
008DDE8D  4C 8D 45 50                     lea r8, [rbp + 0x50]
008DDE91  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
008DDE95  E8 2A 23 00 00                  call 0x1408e01c4
008DDE9A  45 33 D2                        xor r10d, r10d
008DDE9D  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
008DDEA0  41 3B C4                        cmp eax, r12d
008DDEA3  0F 84 F4 02 00 00               je 0x1408de19d
008DDEA9  85 C0                           test eax, eax
008DDEAB  0F 88 06 FF FF FF               js 0x1408dddb7
008DDEB1  8A 4D 50                        mov cl, byte ptr [rbp + 0x50]
008DDEB4  E9 B8 FE FF FF                  jmp 0x1408ddd71
008DDEB9  48 8B 0F                        mov rcx, qword ptr [rdi]
008DDEBC  4A 2B 4C 33 50                  sub rcx, qword ptr [rbx + r14 + 0x50]
008DDEC1  75 09                           jne 0x1408ddecc
008DDEC3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008DDEC7  4A 2B 4C 33 58                  sub rcx, qword ptr [rbx + r14 + 0x58]
008DDECC  48 85 C9                        test rcx, rcx
008DDECF  0F 85 FF FC FF FF               jne 0x1408ddbd4
008DDED5  42 8B 44 33 64                  mov eax, dword ptr [rbx + r14 + 0x64]
008DDEDA  39 47 14                        cmp dword ptr [rdi + 0x14], eax
008DDEDD  0F 85 F1 FC FF FF               jne 0x1408ddbd4
008DDEE3  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
008DDEE7  4A 8B 54 33 68                  mov rdx, qword ptr [rbx + r14 + 0x68]
008DDEEC  48 3B CA                        cmp rcx, rdx
008DDEEF  0F 85 A4 01 00 00               jne 0x1408de099
008DDEF5  42 83 7C 33 64 01               cmp dword ptr [rbx + r14 + 0x64], 1
008DDEFB  0F 84 BF 01 00 00               je 0x1408de0c0
008DDF01  B3 01                           mov bl, 1
008DDF03  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDF06  E9 D1 FC FF FF                  jmp 0x1408ddbdc
008DDF0B  49 8B 0F                        mov rcx, qword ptr [r15]
008DDF0E  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDF11  4A 2B 4C 37 50                  sub rcx, qword ptr [rdi + r14 + 0x50]
008DDF16  75 09                           jne 0x1408ddf21
008DDF18  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
008DDF1C  4A 2B 4C 37 58                  sub rcx, qword ptr [rdi + r14 + 0x58]
008DDF21  48 85 C9                        test rcx, rcx
008DDF24  0F 85 FE FC FF FF               jne 0x1408ddc28
008DDF2A  42 8B 44 37 64                  mov eax, dword ptr [rdi + r14 + 0x64]
008DDF2F  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDF32  41 39 47 14                     cmp dword ptr [r15 + 0x14], eax
008DDF36  0F 85 EC FC FF FF               jne 0x1408ddc28
008DDF3C  83 F8 01                        cmp eax, 1
008DDF3F  0F 84 E3 01 00 00               je 0x1408de128
008DDF45  4E 39 54 37 68                  cmp qword ptr [rdi + r14 + 0x68], r10
008DDF4A  0F 84 3F 01 00 00               je 0x1408de08f
008DDF50  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
008DDF54  48 8B 58 38                     mov rbx, qword ptr [rax + 0x38]
008DDF58  66 44 39 13                     cmp word ptr [rbx], r10w
008DDF5C  0F 84 41 EF 23 00               je 0x140b1cea3
008DDF62  4A 8B 4C 37 68                  mov rcx, qword ptr [rdi + r14 + 0x68]
008DDF67  48 8B D3                        mov rdx, rbx
008DDF6A  E8 11 21 C2 FF                  call 0x140500080
008DDF6F  45 33 D2                        xor r10d, r10d
008DDF72  85 C0                           test eax, eax
008DDF74  0F 84 34 EF 23 00               je 0x140b1ceae
008DDF7A  48 83 C8 FF                     or rax, 0xffffffffffffffff
008DDF7E  E9 09 EF 23 00                  jmp 0x140b1ce8c
008DDF83  44 8B 7D E8                     mov r15d, dword ptr [rbp - 0x18]
008DDF87  E9 89 FD FF FF                  jmp 0x1408ddd15
008DDF8C  45 85 C0                        test r8d, r8d
008DDF8F  0F 85 81 01 00 00               jne 0x1408de116
008DDF95  B3 01                           mov bl, 1
008DDF97  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DDF9A  E9 A3 FC FF FF                  jmp 0x1408ddc42
008DDF9F  83 E9 01                        sub ecx, 1
008DDFA2  0F 84 B9 01 00 00               je 0x1408de161
008DDFA8  83 F9 01                        cmp ecx, 1
008DDFAB  0F 85 C8 FD FF FF               jne 0x1408ddd79
008DDFB1  49 8B 58 20                     mov rbx, qword ptr [r8 + 0x20]
008DDFB5  41 8A CA                        mov cl, r10b
008DDFB8  88 4D 50                        mov byte ptr [rbp + 0x50], cl
008DDFBB  48 8B FA                        mov rdi, rdx
008DDFBE  66 44 39 13                     cmp word ptr [rbx], r10w
008DDFC2  0F 84 B1 FD FF FF               je 0x1408ddd79
008DDFC8  41 8A C2                        mov al, r10b
008DDFCB  E9 EB EE 23 00                  jmp 0x140b1cebb
008DDFD0  49 8D 56 18                     lea rdx, [r14 + 0x18]
008DDFD4  48 8D 4E 20                     lea rcx, [rsi + 0x20]
008DDFD8  4C 8D 45 E0                     lea r8, [rbp - 0x20]
008DDFDC  E8 CF 75 E2 FF                  call 0x1407055b0
008DDFE1  45 33 D2                        xor r10d, r10d
008DDFE4  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
008DDFE7  85 C0                           test eax, eax
008DDFE9  0F 88 C8 FD FF FF               js 0x1408dddb7
008DDFEF  44 8A 6D E0                     mov r13b, byte ptr [rbp - 0x20]
008DDFF3  E9 89 FB FF FF                  jmp 0x1408ddb81
008DDFF8  41 B4 01                        mov r12b, 1
008DDFFB  E9 E3 FC FF FF                  jmp 0x1408ddce3
008DE000  45 84 ED                        test r13b, r13b
008DE003  74 2B                           je 0x1408de030
008DE005  44 38 55 48                     cmp byte ptr [rbp + 0x48], r10b
008DE009  C7 45 E8 02 00 00 00            mov dword ptr [rbp - 0x18], 2
008DE010  0F 95 45 58                     setne byte ptr [rbp + 0x58]
008DE014  49 8D 7E 08                     lea rdi, [r14 + 8]
008DE018  44 8B 7D E8                     mov r15d, dword ptr [rbp - 0x18]
008DE01C  E9 86 FD FF FF                  jmp 0x1408ddda7
008DE021  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
008DE025  0F 85 B2 FC FF FF               jne 0x1408ddcdd
008DE02B  E9 5E FC FF FF                  jmp 0x1408ddc8e
008DE030  48 8B CE                        mov rcx, rsi
008DE033  C7 45 E8 01 00 00 00            mov dword ptr [rbp - 0x18], 1
008DE03A  E8 CD F9 FF FF                  call 0x1408dda0c
008DE03F  48 8B 17                        mov rdx, qword ptr [rdi]
008DE042  48 8B CE                        mov rcx, rsi
008DE045  E8 DA 75 17 00                  call 0x140a55624
008DE04A  48 8B CE                        mov rcx, rsi
008DE04D  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
008DE050  E8 17 FA FF FF                  call 0x1408dda6c
008DE055  C6 45 58 01                     mov byte ptr [rbp + 0x58], 1
008DE059  EB B9                           jmp 0x1408de014
008DE05B  45 84 ED                        test r13b, r13b
008DE05E  0F 84 46 FD FF FF               je 0x1408dddaa
008DE064  48 8B CE                        mov rcx, rsi
008DE067  41 BF 03 00 00 00               mov r15d, 3
008DE06D  B3 01                           mov bl, 1
008DE06F  E8 98 F9 FF FF                  call 0x1408dda0c
008DE074  48 8B 17                        mov rdx, qword ptr [rdi]
008DE077  48 8B CE                        mov rcx, rsi
008DE07A  E8 81 E5 FF FF                  call 0x1408dc600
008DE07F  48 8B CE                        mov rcx, rsi
008DE082  E8 E5 F9 FF FF                  call 0x1408dda6c
008DE087  45 33 D2                        xor r10d, r10d
008DE08A  E9 1E FD FF FF                  jmp 0x1408dddad
008DE08F  B3 01                           mov bl, 1
008DE091  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DE094  E9 A5 FB FF FF                  jmp 0x1408ddc3e
008DE099  48 85 C9                        test rcx, rcx
008DE09C  0F 84 32 FB FF FF               je 0x1408ddbd4
008DE0A2  48 85 D2                        test rdx, rdx
008DE0A5  0F 84 29 FB FF FF               je 0x1408ddbd4
008DE0AB  E8 D0 1F C2 FF                  call 0x140500080
008DE0B0  45 33 D2                        xor r10d, r10d
008DE0B3  85 C0                           test eax, eax
008DE0B5  0F 85 19 FB FF FF               jne 0x1408ddbd4
008DE0BB  E9 35 FE FF FF                  jmp 0x1408ddef5
008DE0C0  45 84 ED                        test r13b, r13b
008DE0C3  0F 85 38 FE FF FF               jne 0x1408ddf01
008DE0C9  E9 06 FB FF FF                  jmp 0x1408ddbd4
008DE0CE  44 8A 6D E1                     mov r13b, byte ptr [rbp - 0x1f]
008DE0D2  49 8D 7E 08                     lea rdi, [r14 + 8]
008DE0D6  E9 7B FC FF FF                  jmp 0x1408ddd56
008DE0DB  84 DB                           test bl, bl
008DE0DD  0F 84 11 FC FF FF               je 0x1408ddcf4
008DE0E3  48 8B 17                        mov rdx, qword ptr [rdi]
008DE0E6  4C 8D 4D F0                     lea r9, [rbp - 0x10]
008DE0EA  4D 8B C6                        mov r8, r14
008DE0ED  41 8B CF                        mov ecx, r15d
008DE0F0  E8 A7 DD FF FF                  call 0x1408dbe9c
008DE0F5  85 C0                           test eax, eax
008DE0F7  0F 88 BA FC FF FF               js 0x1408dddb7
008DE0FD  48 8B CE                        mov rcx, rsi
008DE100  E8 07 F9 FF FF                  call 0x1408dda0c
008DE105  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
008DE109  48 8B CE                        mov rcx, rsi
008DE10C  E8 23 0A 00 00                  call 0x1408deb34
008DE111  E9 B8 FC FF FF                  jmp 0x1408dddce
008DE116  45 8B FA                        mov r15d, r10d
008DE119  45 39 56 4C                     cmp dword ptr [r14 + 0x4c], r10d
008DE11D  0F 86 1F FB FF FF               jbe 0x1408ddc42
008DE123  E9 F6 EC 23 00                  jmp 0x140b1ce1e
008DE128  88 5D 48                        mov byte ptr [rbp + 0x48], bl
008DE12B  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
008DE12F  0F 84 F3 FA FF FF               je 0x1408ddc28
008DE135  E9 0B FE FF FF                  jmp 0x1408ddf45
008DE13A  48 85 C9                        test rcx, rcx
008DE13D  0F 84 4B FB FF FF               je 0x1408ddc8e
008DE143  48 85 D2                        test rdx, rdx
008DE146  0F 84 42 FB FF FF               je 0x1408ddc8e
008DE14C  E8 2F 1F C2 FF                  call 0x140500080
008DE151  45 33 D2                        xor r10d, r10d
008DE154  85 C0                           test eax, eax
008DE156  0F 85 32 FB FF FF               jne 0x1408ddc8e
008DE15C  E9 70 FB FF FF                  jmp 0x1408ddcd1
008DE161  49 8B 48 18                     mov rcx, qword ptr [r8 + 0x18]
008DE165  49 8D 7E 08                     lea rdi, [r14 + 8]
008DE169  48 8B 17                        mov rdx, qword ptr [rdi]
008DE16C  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
008DE170  E8 0B 1F C2 FF                  call 0x140500080
008DE175  45 33 D2                        xor r10d, r10d
008DE178  85 C0                           test eax, eax
008DE17A  0F 94 C1                        sete cl
008DE17D  88 4D 50                        mov byte ptr [rbp + 0x50], cl
008DE180  8A C1                           mov al, cl
008DE182  E9 7A FC FF FF                  jmp 0x1408dde01
008DE187  45 33 D2                        xor r10d, r10d
008DE18A  49 8D 7E 08                     lea rdi, [r14 + 8]
008DE18E  41 8A CA                        mov cl, r10b
008DE191  44 89 55 E4                     mov dword ptr [rbp - 0x1c], r10d
008DE195  88 4D 50                        mov byte ptr [rbp + 0x50], cl
008DE198  E9 D1 FC FF FF                  jmp 0x1408dde6e
008DE19D  41 8A CA                        mov cl, r10b
008DE1A0  44 89 55 E4                     mov dword ptr [rbp - 0x1c], r10d
008DE1A4  E9 C8 FB FF FF                  jmp 0x1408ddd71
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqQueryApplyObjectEvent(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_m57;
    unsigned __int8 v_stack_m58;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_r10 = 0;
    v_stack_m54 = 0;
    v_stack_m48 = 0;
    v_stack_m57 = 0;
    v_stack_p10 = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    v_stack_p18 = 0;
    v_stack_m58 = 0;
    result = (unsigned int)(*(unsigned int *)(a2 + 4));
    v_rbx = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (1)) != 0) {
        a1 = a1;
        result = PiDqQueryLock(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(a2 + 8);
        a1 = a1 + 72;
        a2 = v_stack_m40;
        v_stack_m40 = result;
        result = RtlLookupElementGenericTableAvl(a1, a2, a3, a4);
        a1 = a1;
        v_rbx = result;
        result = PiDqQueryUnlock(a1, a2, a3, a4);
        v_r10 = 0;
        v_rbx = 0;
        a1 = (v_rbx != 0) ? 1 : 0;
        v_stack_m57 = (unsigned __int8)(a1);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (1)) != 0) goto loc_008DDD0D;
loc_008DDB63:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (2)) != 0) goto loc_008DDD15;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (8)) != 0) goto loc_008DDB79;
    if ((*(unsigned int *)(a2 + 76)) <= 0) goto loc_008DDD15;
loc_008DDB79:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (4)) != 0) goto loc_008DDFD0;
loc_008DDB81:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 40))))) & (4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 40)))) & (2)) != 0) goto loc_008DDF8C;
    if ((unsigned int)(a3) != 0) goto loc_008DDBEB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 64))) == 0) goto loc_008DDDDB;
loc_008DDBAB:
    v_rdi = (0) << (5);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 72));
loc_008DDBB9:
    if (0 >= (*(unsigned int *)(a2 + 76))) goto loc_008DDBD9;
    v_rbx = (0) << (5);
    if ((*(unsigned int *)(v_rdi + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + a2 * 1 + 96))))) goto loc_008DDEB9;
loc_008DDBD4:
    v_r15 = (unsigned int)((0) + 1);
    goto loc_008DDBB9;
loc_008DDBD9:
loc_008DDBDC:
    v_r12 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r12)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 64))) goto loc_008DDBAB;
    goto loc_008DDC3E;
loc_008DDBEB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + a2 * 1 + 96))) == 0) goto loc_008DDC42;
loc_008DDBF2:
    v_r15 = (0) << (5);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 72));
    v_stack_p10 = 0;
    if ((*(unsigned int *)(a2 + 76)) <= 0) goto loc_008DDC31;
loc_008DDC0C:
    v_rdi = (0) << (5);
    v_stack_p10 = 0;
    if ((*(unsigned int *)(v_r15 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + a2 * 1 + 96))))) goto loc_008DDF0B;
loc_008DDC28:
    v_r12 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r12)) < (*(unsigned int *)(a2 + 76))) goto loc_008DDC0C;
loc_008DDC31:
    v_r13 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r13)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 64))) goto loc_008DDBF2;
loc_008DDC3E:
loc_008DDC42:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 20)) != 0) goto loc_008DDC5B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (8)) != 0) goto loc_008DDFF8;
loc_008DDC5B:
loc_008DDC5E:
    if (0 >= (*(unsigned int *)(a2 + 76))) goto loc_008DDCE0;
    v_rbx = (0) << (5);
loc_008DDC6D:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 80))) goto loc_008DDC93;
    a2 = (*(unsigned __int64 *)(a1 + 24)) * (0);
    if ((*(unsigned int *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88) * 1 + 24)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + a2 * 1 + 96))))) goto loc_008DDC97;
loc_008DDC8E:
    v_r15 = (unsigned int)((0) + 1);
    goto loc_008DDC6D;
loc_008DDC93:
    v_rdi = (unsigned int)((0) + 1);
    goto loc_008DDC5E;
loc_008DDC97:
    a1 = (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88) * 1 + 8)) - (*(unsigned __int64 *)(v_rbx + a2 * 1 + 80));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88) * 1 + 16);
        a1 = (a1) - (*(unsigned __int64 *)(v_rbx + a2 * 1 + 88));
    }
    if (a1 != 0) goto loc_008DDC8E;
    if ((*(unsigned int *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88) * 1 + 28)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + a2 * 1 + 100))))) goto loc_008DDC8E;
    if ((*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88) * 1 + 32)) != (*(unsigned __int64 *)(v_rbx + a2 * 1 + 104))) goto loc_008DE13A;
loc_008DDCD1:
    if ((*(unsigned int *)(v_rbx + a2 * 1 + 100)) == 1) goto loc_008DE021;
loc_008DDCDD:
loc_008DDCE0:
loc_008DDCE3:
    if ((unsigned __int8)(v_stack_p10) != 0) goto loc_008DDF83;
    if (1 != 0) goto loc_008DDF83;
loc_008DDCF4:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(*(unsigned int *)(v_rbx + a2 * 1 + 100));
loc_008DDD0D:
    if ((unsigned __int8)(*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88) * 1 + 32)) != 0) goto loc_008DDB63;
loc_008DDD15:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (1)) != 0) goto loc_008DE0CE;
    result = PiDqQueryLock(a1, *(unsigned __int64 *)(v_rbx + a2 * 1 + 104), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    v_stack_p18 = *(unsigned __int64 *)(a2 + 8);
    result = RtlLookupElementGenericTableAvl(a1 + 72, v_stack_p18, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    result = PiDqQueryUnlock(a1, v_stack_p18, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    v_r10 = 0;
    v_r13 = (result != 0) ? 1 : 0;
loc_008DDD56:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (2)) != 0) goto loc_008DE05B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (1)) != 0) goto loc_008DDDE7;
    if (1 != 0) goto loc_008DDDE3;
loc_008DDD71:
    if ((unsigned __int8)((unsigned __int8)(v_r13)) != 0) goto loc_008DE000;
loc_008DDD79:
    if ((unsigned __int8)(v_r13) == 0) goto loc_008DE018;
    v_stack_p20 = 1;
    result = PiDqQueryLock(a1, a2 + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    result = PiDqQueryDeleteObjectFromResultSet(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    result = PiDqQueryUnlock(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
loc_008DDDA7:
    v_r10 = 0;
loc_008DDDAA:
loc_008DDDAD:
    if (v_stack_m54 >= 0) goto loc_008DE0DB;
loc_008DDDB7:
    result = PiDqQueryLock(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    result = PiDqQueryFreeActiveData(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
loc_008DDDCE:
    result = PiDqQueryUnlock(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88), a4);
    goto loc_008DDCF4;
loc_008DDDDB:
    goto loc_008DDC42;
loc_008DDDE3:
loc_008DDDE7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 20))) != 0) goto loc_008DDF9F;
    v_stack_p18 = 1;
    goto loc_008DDE09;
loc_008DDE01:
    if ((unsigned __int8)(result) == 0) goto loc_008DDD79;
loc_008DDE09:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 20)) != 0) goto loc_008DDE6E;
    v_stack_p28 = v_stack_p18;
    a4 = 0;
    v_stack_p20 = a1 + 32;
    result = PiPnpRtlApplyMandatoryFilters(*(unsigned __int64 *)(v_rip + 5801316), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 16), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 28)), a4);
    v_stack_m54 = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008DE187;
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_008DE187;
    v_r10 = 0;
    if (sign_flag) goto loc_008DDDB7;
loc_008DDE6E:
    if ((unsigned __int8)(v_stack_p18) == 0) goto loc_008DDD79;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 88)) == 0) goto loc_008DDD71;
    result = PiDqQueryEvaluateFilter(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 16), v_stack_p18, a4);
    v_r10 = 0;
    v_stack_m54 = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008DE19D;
    if (sign_flag) goto loc_008DDDB7;
    goto loc_008DDD71;
loc_008DDEB9:
    a1 = (*(unsigned __int64 *)(a2 + 8)) - (*(unsigned __int64 *)(a1 + 24 + a2 * 1 + 80));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a2 + 8 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a1 + 24 + a2 * 1 + 88));
    }
    if (a1 != 0) goto loc_008DDBD4;
    if ((*(unsigned int *)(a2 + 8 + 20)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24 + a2 * 1 + 100))))) goto loc_008DDBD4;
    if ((*(unsigned __int64 *)(a2 + 8 + 24)) != (*(unsigned __int64 *)(a1 + 24 + a2 * 1 + 104))) goto loc_008DE099;
loc_008DDEF5:
    if ((*(unsigned int *)(a1 + 24 + a2 * 1 + 100)) == 1) goto loc_008DE0C0;
loc_008DDF01:
    v_stack_p10 = 1;
    goto loc_008DDBDC;
loc_008DDF0B:
    v_stack_p10 = 1;
    a1 = (*(unsigned __int64 *)(3)) - (*(unsigned __int64 *)(a2 + 8 + a2 * 1 + 80));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(3 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a2 + 8 + a2 * 1 + 88));
    }
    if (a1 != 0) goto loc_008DDC28;
    v_stack_p10 = 1;
    if ((*(unsigned int *)(3 + 20)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8 + a2 * 1 + 100))))) goto loc_008DDC28;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8 + a2 * 1 + 100)))) == 1) goto loc_008DE128;
loc_008DDF45:
    if ((*(unsigned __int64 *)(a2 + 8 + a2 * 1 + 104)) == 0) goto loc_008DE08F;
    result = wcsicmp(*(unsigned __int64 *)(a2 + 8 + a2 * 1 + 104), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 56), v_stack_p18, a4);
    v_r10 = 0;
    result = (result) | (-1);
loc_008DDF83:
    goto loc_008DDD15;
loc_008DDF8C:
    if ((unsigned int)(v_stack_p18) != 0) goto loc_008DE116;
    v_stack_p10 = 1;
    goto loc_008DDC42;
loc_008DDF9F:
    a1 = (unsigned int)((*(unsigned __int64 *)(a2 + 8 + a2 * 1 + 104)) - (1));
    if (condition_is_equal) goto loc_008DE161;
    if (((unsigned int)(a1)) != 1) goto loc_008DDD79;
    v_stack_p18 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 32))) == 0) goto loc_008DDD79;
loc_008DDFD0:
    result = PiDqSameUserHive(a1 + 32, a2 + 24, v_stack_m58, a4);
    v_r10 = 0;
    v_stack_m54 = (unsigned int)(result);
    if (sign_flag) goto loc_008DDDB7;
    goto loc_008DDB81;
loc_008DDFF8:
    goto loc_008DDCE3;
loc_008DE000:
    if ((unsigned __int8)(v_stack_m58) == 0) goto loc_008DE030;
    v_stack_m50 = 2;
loc_008DE014:
loc_008DE018:
    goto loc_008DDDA7;
loc_008DE021:
    if (v_stack_m58 != 0) goto loc_008DDCDD;
    goto loc_008DDC8E;
loc_008DE030:
    v_stack_m50 = 1;
    result = PiDqQueryLock(a1, a2 + 24, v_stack_m58, a4);
    result = PiDqQueryAddObjectToResultSet(a1, *(unsigned __int64 *)(a2 + 8), v_stack_m58, a4);
    v_stack_m54 = (unsigned int)(result);
    result = PiDqQueryUnlock(a1, *(unsigned __int64 *)(a2 + 8), v_stack_m58, a4);
    v_stack_p20 = 1;
    goto loc_008DE014;
loc_008DE05B:
    if ((unsigned __int8)(v_stack_m58) == 0) goto loc_008DDDAA;
    result = PiDqQueryLock(a1, *(unsigned __int64 *)(a2 + 8), v_stack_m58, a4);
    result = PiDqQueryDeleteObjectFromResultSet(a1, *(unsigned __int64 *)(a2 + 8), v_stack_m58, a4);
    result = PiDqQueryUnlock(a1, *(unsigned __int64 *)(a2 + 8), v_stack_m58, a4);
    v_r10 = 0;
    goto loc_008DDDAD;
loc_008DE08F:
    v_stack_p10 = 1;
    goto loc_008DDC3E;
loc_008DE099:
    if (a1 == 0) goto loc_008DDBD4;
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_008DDBD4;
    result = wcsicmp(a1, *(unsigned __int64 *)(a2 + 8), v_stack_m58, a4);
    v_r10 = 0;
    if ((unsigned int)(result) != 0) goto loc_008DDBD4;
    goto loc_008DDEF5;
loc_008DE0C0:
    if ((unsigned __int8)(v_stack_m58) != 0) goto loc_008DDF01;
    goto loc_008DDBD4;
loc_008DE0CE:
    goto loc_008DDD56;
loc_008DE0DB:
    if (1 == 0) goto loc_008DDCF4;
    result = PiDqQueryActionQueueEntryCreate(3, *(unsigned __int64 *)(a2 + 8), a2, v_stack_m48);
    if (sign_flag) goto loc_008DDDB7;
    result = PiDqQueryLock(a1, *(unsigned __int64 *)(a2 + 8), a2, v_stack_m48);
    result = PiDqQueryAppendActionEntry(a1, v_stack_m48, a2, v_stack_m48);
    goto loc_008DDDCE;
loc_008DE116:
    if ((*(unsigned int *)(a2 + 76)) <= 0) goto loc_008DDC42;
loc_008DE128:
    v_stack_p10 = 1;
    if (v_stack_m58 == 0) goto loc_008DDC28;
    goto loc_008DDF45;
loc_008DE13A:
    if (a1 == 0) goto loc_008DDC8E;
    if (v_stack_m48 == 0) goto loc_008DDC8E;
    result = wcsicmp(a1, v_stack_m48, a2, v_stack_m48);
    v_r10 = 0;
    if ((unsigned int)(result) != 0) goto loc_008DDC8E;
    goto loc_008DDCD1;
loc_008DE161:
    result = wcsicmp(*(unsigned __int64 *)(a2 + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 16), a2, v_stack_m48);
    v_r10 = 0;
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    v_stack_p18 = (unsigned __int8)(a1);
    goto loc_008DDE01;
loc_008DE187:
    v_r10 = 0;
    v_stack_m54 = 0;
    v_stack_p18 = 0;
    goto loc_008DDE6E;
loc_008DE19D:
    v_stack_m54 = 0;
    goto loc_008DDD71;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqQueryApplyObjectEvent(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint8_t v_stack_m57;
    uint8_t v_stack_m58;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    local_r10 = 0;
    v_stack_m54 = 0;
    v_stack_m48 = 0;
    v_stack_m57 = 0;
    v_stack_p10 = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    v_stack_p18 = 0;
    v_stack_m58 = 0;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x4));
    local_rbx = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (1)) != 0) {
        Arg1 = Arg1;
        result = PiDqQueryLock(Arg1, Arg2, Arg3, Arg4);
        result = *(uint64_t *)(arg2 + 0x8);
        Arg1 = Arg1 + 72;
        Arg2 = v_stack_m40;
        v_stack_m40 = result;
        result = RtlLookupElementGenericTableAvl(Arg1, Arg2, Arg3, Arg4);
        Arg1 = Arg1;
        local_rbx = result;
        result = PiDqQueryUnlock(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
        local_rbx = 0;
        Arg1 = (local_rbx != 0) ? 1 : 0;
        v_stack_m57 = (uint8_t)(Arg1);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (1)) != 0) goto loc_008DDD0D;
loc_008DDB63:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (2)) != 0) goto loc_008DDD15;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (8)) != 0) goto loc_008DDB79;
    if ((*(uint32_t *)(arg2 + 0x4C)) <= 0) goto loc_008DDD15;
loc_008DDB79:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (4)) != 0) goto loc_008DDFD0;
loc_008DDB81:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28))))) & (4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28)))) & (2)) != 0) goto loc_008DDF8C;
    if ((uint32_t)(Arg3) != 0) goto loc_008DDBEB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x40))) == 0) goto loc_008DDDDB;
loc_008DDBAB:
    local_rdi = (0) << (5);
    local_rdi = (local_rdi) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x48));
loc_008DDBB9:
    if (0 >= (*(uint32_t *)(arg2 + 0x4C))) goto loc_008DDBD9;
    local_rbx = (0) << (5);
    if ((*(uint32_t *)(local_rdi + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + arg2 * 1 + 0x60))))) goto loc_008DDEB9;
loc_008DDBD4:
    local_r15 = (uint32_t)((0) + 1);
    goto loc_008DDBB9;
loc_008DDBD9:
loc_008DDBDC:
    local_r12 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r12)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x40))) goto loc_008DDBAB;
    goto loc_008DDC3E;
loc_008DDBEB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + arg2 * 1 + 0x60))) == 0) goto loc_008DDC42;
loc_008DDBF2:
    local_r15 = (0) << (5);
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x48));
    v_stack_p10 = 0;
    if ((*(uint32_t *)(arg2 + 0x4C)) <= 0) goto loc_008DDC31;
loc_008DDC0C:
    local_rdi = (0) << (5);
    v_stack_p10 = 0;
    if ((*(uint32_t *)(local_r15 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + arg2 * 1 + 0x60))))) goto loc_008DDF0B;
loc_008DDC28:
    local_r12 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r12)) < (*(uint32_t *)(arg2 + 0x4C))) goto loc_008DDC0C;
loc_008DDC31:
    local_r13 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r13)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x40))) goto loc_008DDBF2;
loc_008DDC3E:
loc_008DDC42:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x14)) != 0) goto loc_008DDC5B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (8)) != 0) goto loc_008DDFF8;
loc_008DDC5B:
loc_008DDC5E:
    if (0 >= (*(uint32_t *)(arg2 + 0x4C))) goto loc_008DDCE0;
    local_rbx = (0) << (5);
loc_008DDC6D:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x50))) goto loc_008DDC93;
    Arg2 = (*(uint64_t *)(arg1 + 0x18)) * (0);
    if ((*(uint32_t *)(arg2 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58) * 1 + 0x18)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + arg2 * 1 + 0x60))))) goto loc_008DDC97;
loc_008DDC8E:
    local_r15 = (uint32_t)((0) + 1);
    goto loc_008DDC6D;
loc_008DDC93:
    local_rdi = (uint32_t)((0) + 1);
    goto loc_008DDC5E;
loc_008DDC97:
    Arg1 = (*(uint64_t *)(arg2 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58) * 1 + 0x8)) - (*(uint64_t *)(local_rbx + arg2 * 1 + 0x50));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg2 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58) * 1 + 0x10);
        Arg1 = (Arg1) - (*(uint64_t *)(local_rbx + arg2 * 1 + 0x58));
    }
    if (Arg1 != NULL) goto loc_008DDC8E;
    if ((*(uint32_t *)(arg2 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58) * 1 + 0x1C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + arg2 * 1 + 0x64))))) goto loc_008DDC8E;
    if ((*(uint64_t *)(arg2 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58) * 1 + 0x20)) != (*(uint64_t *)(local_rbx + arg2 * 1 + 0x68))) goto loc_008DE13A;
loc_008DDCD1:
    if ((*(uint32_t *)(local_rbx + arg2 * 1 + 0x64)) == 1) goto loc_008DE021;
loc_008DDCDD:
loc_008DDCE0:
loc_008DDCE3:
    if ((uint8_t)(v_stack_p10) != 0) goto loc_008DDF83;
    if (1 != 0) goto loc_008DDF83;
loc_008DDCF4:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(*(uint32_t *)(local_rbx + arg2 * 1 + 0x64));
loc_008DDD0D:
    if ((uint8_t)(*(uint64_t *)(arg2 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58) * 1 + 0x20)) != 0) goto loc_008DDB63;
loc_008DDD15:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (1)) != 0) goto loc_008DE0CE;
    result = PiDqQueryLock(Arg1, *(uint64_t *)(local_rbx + arg2 * 1 + 0x68), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    v_stack_p18 = *(uint64_t *)(arg2 + 0x8);
    result = RtlLookupElementGenericTableAvl(Arg1 + 72, v_stack_p18, *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    result = PiDqQueryUnlock(Arg1, v_stack_p18, *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    local_r10 = 0;
    local_r13 = (result != 0) ? 1 : 0;
loc_008DDD56:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (2)) != 0) goto loc_008DE05B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) & (1)) != 0) goto loc_008DDDE7;
    if (1 != 0) goto loc_008DDDE3;
loc_008DDD71:
    if ((uint8_t)((uint8_t)(local_r13)) != 0) goto loc_008DE000;
loc_008DDD79:
    if ((uint8_t)(local_r13) == 0) goto loc_008DE018;
    v_stack_p20 = 1;
    result = PiDqQueryLock(Arg1, Arg2 + 8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    result = PiDqQueryDeleteObjectFromResultSet(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    result = PiDqQueryUnlock(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
loc_008DDDA7:
    local_r10 = 0;
loc_008DDDAA:
loc_008DDDAD:
    if (v_stack_m54 >= 0) goto loc_008DE0DB;
loc_008DDDB7:
    result = PiDqQueryLock(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    result = PiDqQueryFreeActiveData(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
loc_008DDDCE:
    result = PiDqQueryUnlock(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58), Arg4);
    goto loc_008DDCF4;
loc_008DDDDB:
    goto loc_008DDC42;
loc_008DDDE3:
loc_008DDDE7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x14))) != 0) goto loc_008DDF9F;
    v_stack_p18 = 1;
    goto loc_008DDE09;
loc_008DDE01:
    if ((uint8_t)(result) == 0) goto loc_008DDD79;
loc_008DDE09:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x14)) != 0) goto loc_008DDE6E;
    v_stack_p28 = v_stack_p18;
    Arg4 = 0;
    v_stack_p20 = Arg1 + 32;
    result = PiPnpRtlApplyMandatoryFilters(*(uint64_t *)(v_rip + 0x588564), *(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x1C)), Arg4);
    v_stack_m54 = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008DE187;
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_008DE187;
    local_r10 = 0;
    if (sign_flag) goto loc_008DDDB7;
loc_008DDE6E:
    if ((uint8_t)(v_stack_p18) == 0) goto loc_008DDD79;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x58)) == 0) goto loc_008DDD71;
    result = PiDqQueryEvaluateFilter(Arg1, *(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10), v_stack_p18, Arg4);
    local_r10 = 0;
    v_stack_m54 = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008DE19D;
    if (sign_flag) goto loc_008DDDB7;
    goto loc_008DDD71;
loc_008DDEB9:
    Arg1 = (*(uint64_t *)(arg2 + 0x8)) - (*(uint64_t *)(arg1 + 0x18 + arg2 * 1 + 0x50));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg2 + 0x8 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg1 + 0x18 + arg2 * 1 + 0x58));
    }
    if (Arg1 != NULL) goto loc_008DDBD4;
    if ((*(uint32_t *)(arg2 + 0x8 + 0x14)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18 + arg2 * 1 + 0x64))))) goto loc_008DDBD4;
    if ((*(uint64_t *)(arg2 + 0x8 + 0x18)) != (*(uint64_t *)(arg1 + 0x18 + arg2 * 1 + 0x68))) goto loc_008DE099;
loc_008DDEF5:
    if ((*(uint32_t *)(arg1 + 0x18 + arg2 * 1 + 0x64)) == 1) goto loc_008DE0C0;
loc_008DDF01:
    v_stack_p10 = 1;
    goto loc_008DDBDC;
loc_008DDF0B:
    v_stack_p10 = 1;
    Arg1 = (*(uint64_t *)(3)) - (*(uint64_t *)(arg2 + 0x8 + arg2 * 1 + 0x50));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(3 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg2 + 0x8 + arg2 * 1 + 0x58));
    }
    if (Arg1 != NULL) goto loc_008DDC28;
    v_stack_p10 = 1;
    if ((*(uint32_t *)(3 + 0x14)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8 + arg2 * 1 + 0x64))))) goto loc_008DDC28;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8 + arg2 * 1 + 0x64)))) == 1) goto loc_008DE128;
loc_008DDF45:
    if ((*(uint64_t *)(arg2 + 0x8 + arg2 * 1 + 0x68)) == 0) goto loc_008DE08F;
    result = wcsicmp(*(uint64_t *)(arg2 + 0x8 + arg2 * 1 + 0x68), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x38), v_stack_p18, Arg4);
    local_r10 = 0;
    result = (result) | (-1);
loc_008DDF83:
    goto loc_008DDD15;
loc_008DDF8C:
    if ((uint32_t)(v_stack_p18) != 0) goto loc_008DE116;
    v_stack_p10 = 1;
    goto loc_008DDC42;
loc_008DDF9F:
    Arg1 = (uint32_t)((*(uint64_t *)(arg2 + 0x8 + arg2 * 1 + 0x68)) - (1));
    if (condition_is_equal) goto loc_008DE161;
    if (((uint32_t)(Arg1)) != 1) goto loc_008DDD79;
    v_stack_p18 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x20))) == 0) goto loc_008DDD79;
loc_008DDFD0:
    result = PiDqSameUserHive(Arg1 + 32, Arg2 + 24, v_stack_m58, Arg4);
    local_r10 = 0;
    v_stack_m54 = (uint32_t)(result);
    if (sign_flag) goto loc_008DDDB7;
    goto loc_008DDB81;
loc_008DDFF8:
    goto loc_008DDCE3;
loc_008DE000:
    if ((uint8_t)(v_stack_m58) == 0) goto loc_008DE030;
    v_stack_m50 = 2;
loc_008DE014:
loc_008DE018:
    goto loc_008DDDA7;
loc_008DE021:
    if (v_stack_m58 != 0) goto loc_008DDCDD;
    goto loc_008DDC8E;
loc_008DE030:
    v_stack_m50 = 1;
    result = PiDqQueryLock(Arg1, Arg2 + 24, v_stack_m58, Arg4);
    result = PiDqQueryAddObjectToResultSet(Arg1, *(uint64_t *)(arg2 + 0x8), v_stack_m58, Arg4);
    v_stack_m54 = (uint32_t)(result);
    result = PiDqQueryUnlock(Arg1, *(uint64_t *)(arg2 + 0x8), v_stack_m58, Arg4);
    v_stack_p20 = 1;
    goto loc_008DE014;
loc_008DE05B:
    if ((uint8_t)(v_stack_m58) == 0) goto loc_008DDDAA;
    result = PiDqQueryLock(Arg1, *(uint64_t *)(arg2 + 0x8), v_stack_m58, Arg4);
    result = PiDqQueryDeleteObjectFromResultSet(Arg1, *(uint64_t *)(arg2 + 0x8), v_stack_m58, Arg4);
    result = PiDqQueryUnlock(Arg1, *(uint64_t *)(arg2 + 0x8), v_stack_m58, Arg4);
    local_r10 = 0;
    goto loc_008DDDAD;
loc_008DE08F:
    v_stack_p10 = 1;
    goto loc_008DDC3E;
loc_008DE099:
    if (Arg1 == NULL) goto loc_008DDBD4;
    if (*(uint64_t *)(arg2 + 0x8) == 0) goto loc_008DDBD4;
    result = wcsicmp(Arg1, *(uint64_t *)(arg2 + 0x8), v_stack_m58, Arg4);
    local_r10 = 0;
    if ((uint32_t)(result) != 0) goto loc_008DDBD4;
    goto loc_008DDEF5;
loc_008DE0C0:
    if ((uint8_t)(v_stack_m58) != 0) goto loc_008DDF01;
    goto loc_008DDBD4;
loc_008DE0CE:
    goto loc_008DDD56;
loc_008DE0DB:
    if (1 == 0) goto loc_008DDCF4;
    result = PiDqQueryActionQueueEntryCreate(3, *(uint64_t *)(arg2 + 0x8), Arg2, v_stack_m48);
    if (sign_flag) goto loc_008DDDB7;
    result = PiDqQueryLock(Arg1, *(uint64_t *)(arg2 + 0x8), Arg2, v_stack_m48);
    result = PiDqQueryAppendActionEntry(Arg1, v_stack_m48, Arg2, v_stack_m48);
    goto loc_008DDDCE;
loc_008DE116:
    if ((*(uint32_t *)(arg2 + 0x4C)) <= 0) goto loc_008DDC42;
loc_008DE128:
    v_stack_p10 = 1;
    if (v_stack_m58 == 0) goto loc_008DDC28;
    goto loc_008DDF45;
loc_008DE13A:
    if (Arg1 == NULL) goto loc_008DDC8E;
    if (v_stack_m48 == 0) goto loc_008DDC8E;
    result = wcsicmp(Arg1, v_stack_m48, Arg2, v_stack_m48);
    local_r10 = 0;
    if ((uint32_t)(result) != 0) goto loc_008DDC8E;
    goto loc_008DDCD1;
loc_008DE161:
    result = wcsicmp(*(uint64_t *)(arg2 + 0x18), *(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10), Arg2, v_stack_m48);
    local_r10 = 0;
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    v_stack_p18 = (uint8_t)(Arg1);
    goto loc_008DDE01;
loc_008DE187:
    local_r10 = 0;
    v_stack_m54 = 0;
    v_stack_p18 = 0;
    goto loc_008DDE6E;
loc_008DE19D:
    v_stack_m54 = 0;
    goto loc_008DDD71;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x4C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DDACC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
