# CmpFindSubKeyInRoot

- RVA: `0x0085D890`–`0x0085E317` (길이 `2,695` bytes)
- VA: `0x000000014085D890`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B058`
- 디코드: `702`개 명령, `2,695/2,695` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085D90A` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085D9FB` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085DA0F` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085DA89` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085DB03` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085DB17` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085DB79` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085DBBE` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085DC83` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085DCCA` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085DD9A` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085DDC9` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085DDF1` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085DE29` → [CmpCompareInIndex](CmpCompareInIndex_function_0085CC40.md) (function, `0x0085CC40`)
- `0x0085DE5B` → [CmpCompareInIndex](CmpCompareInIndex_function_0085CC40.md) (function, `0x0085CC40`)
- `0x0085DE8A` → [CmpDoCompareKeyName](CmpDoCompareKeyName_function_00854E80.md) (function, `0x00854E80`)
- `0x0085DEC1` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085DEDD` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085DEFA` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085DF1C` → [CmpDoCompareKeyName](CmpDoCompareKeyName_function_00854E80.md) (function, `0x00854E80`)
- `0x0085DF5E` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085DF68` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085DF87` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085DFDF` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085E003` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085E02C` → [CmpCompareInIndex](CmpCompareInIndex_function_0085CC40.md) (function, `0x0085CC40`)
- `0x0085E05A` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085E087` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085E0A7` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085E0BD` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085E0E8` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085E0F2` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085E111` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085E132` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085E14D` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085E15C` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085E16C` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085E19B` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x0085E1CA` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x0085E2CC` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085E2E1` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085E2F3` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085E300` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A261`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C049`
- [CmpFindSubKeyByNameWithStatus](CmpFindSubKeyByNameWithStatus_function_00852770.md) at `0x00852AC6`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x008536DB`
- [CmpMarkIndexDirtyInStorageType](../A3/CmpMarkIndexDirtyInStorageType_function_00A325B0.md) at `0x00A32720`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0085D890  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0085D895  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0085D89A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0085D89F  55                              push rbp
0085D8A0  53                              push rbx
0085D8A1  56                              push rsi
0085D8A2  57                              push rdi
0085D8A3  41 54                           push r12
0085D8A5  41 55                           push r13
0085D8A7  41 56                           push r14
0085D8A9  41 57                           push r15
0085D8AB  48 8B EC                        mov rbp, rsp
0085D8AE  48 83 EC 78                     sub rsp, 0x78
0085D8B2  0F B7 7A 02                     movzx edi, word ptr [rdx + 2]
0085D8B6  4C 8B E9                        mov r13, rcx
0085D8B9  33 C9                           xor ecx, ecx
0085D8BB  C7 45 B8 FF FF FF FF            mov dword ptr [rbp - 0x48], 0xffffffff
0085D8C2  FF CF                           dec edi
0085D8C4  89 4D BC                        mov dword ptr [rbp - 0x44], ecx
0085D8C7  89 7D E0                        mov dword ptr [rbp - 0x20], edi
0085D8CA  49 8B D9                        mov rbx, r9
0085D8CD  4D 8B F0                        mov r14, r8
0085D8D0  89 4D DC                        mov dword ptr [rbp - 0x24], ecx
0085D8D3  8B F1                           mov esi, ecx
0085D8D5  44 8B FF                        mov r15d, edi
0085D8D8  4C 8D 45 B8                     lea r8, [rbp - 0x48]
0085D8DC  44 2B FE                        sub r15d, esi
0085D8DF  41 BC 6C 66 00 00               mov r12d, 0x666c
0085D8E5  41 D1 EF                        shr r15d, 1
0085D8E8  44 03 FE                        add r15d, esi
0085D8EB  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085D8F3  44 89 7D 48                     mov dword ptr [rbp + 0x48], r15d
0085D8F7  42 8B 4C BA 04                  mov ecx, dword ptr [rdx + r15*4 + 4]
0085D8FC  8B D1                           mov edx, ecx
0085D8FE  89 4D E4                        mov dword ptr [rbp - 0x1c], ecx
0085D901  49 8B CD                        mov rcx, r13
0085D904  0F 84 7F 01 00 00               je 0x14085da89
0085D90A  E8 51 73 FF FF                  call 0x140854c60
0085D90F  4C 8B C0                        mov r8, rax
0085D912  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0085D916  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0085D91A  C7 00 FF FF FF FF               mov dword ptr [rax], 0xffffffff
0085D920  4D 85 C0                        test r8, r8
0085D923  0F 84 72 06 00 00               je 0x14085df9b
0085D929  41 0F B7 08                     movzx ecx, word ptr [r8]
0085D92D  41 B9 FF FD 00 00               mov r9d, 0xfdff
0085D933  41 0F B7 50 02                  movzx edx, word ptr [r8 + 2]
0085D938  0F B7 C1                        movzx eax, cx
0085D93B  FF CA                           dec edx
0085D93D  66 41 2B C4                     sub ax, r12w
0085D941  89 55 D8                        mov dword ptr [rbp - 0x28], edx
0085D944  66 41 85 C1                     test r9w, ax
0085D948  0F 85 56 03 00 00               jne 0x14085dca4
0085D94E  4C 8D 0C D5 04 00 00 00         lea r9, [rdx*8 + 4]
0085D956  4D 03 C8                        add r9, r8
0085D959  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
0085D95D  66 41 3B CC                     cmp cx, r12w
0085D961  0F 85 2F 02 00 00               jne 0x14085db96
0085D967  33 C9                           xor ecx, ecx
0085D969  41 BC 04 00 00 00               mov r12d, 4
0085D96F  8B C1                           mov eax, ecx
0085D971  41 3B C4                        cmp eax, r12d
0085D974  73 11                           jae 0x14085d987
0085D976  8B C8                           mov ecx, eax
0085D978  42 80 7C 09 04 00               cmp byte ptr [rcx + r9 + 4], 0
0085D97E  74 04                           je 0x14085d984
0085D980  FF C0                           inc eax
0085D982  EB ED                           jmp 0x14085d971
0085D984  44 8B E0                        mov r12d, eax
0085D987  48 85 DB                        test rbx, rbx
0085D98A  0F 85 79 07 00 00               jne 0x14085e109
0085D990  41 0F B7 06                     movzx eax, word ptr [r14]
0085D994  D1 E8                           shr eax, 1
0085D996  41 3B C4                        cmp eax, r12d
0085D999  4C 8D 34 D5 00 00 00 00         lea r14, [rdx*8]
0085D9A1  44 0F 42 E0                     cmovb r12d, eax
0085D9A5  33 F6                           xor esi, esi
0085D9A7  41 3B F4                        cmp esi, r12d
0085D9AA  0F 83 DF 01 00 00               jae 0x14085db8f
0085D9B0  48 85 DB                        test rbx, rbx
0085D9B3  0F 85 22 07 00 00               jne 0x14085e0db
0085D9B9  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0085D9BD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0085D9C1  0F B7 0C 70                     movzx ecx, word ptr [rax + rsi*2]
0085D9C5  4A 8D 04 36                     lea rax, [rsi + r14]
0085D9C9  42 0F B6 5C 00 08               movzx ebx, byte ptr [rax + r8 + 8]
0085D9CF  66 83 F9 61                     cmp cx, 0x61
0085D9D3  73 30                           jae 0x14085da05
0085D9D5  0F B7 F9                        movzx edi, cx
0085D9D8  83 FB 61                        cmp ebx, 0x61
0085D9DB  73 12                           jae 0x14085d9ef
0085D9DD  8B C3                           mov eax, ebx
0085D9DF  2B F8                           sub edi, eax
0085D9E1  75 36                           jne 0x14085da19
0085D9E3  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
0085D9E7  FF C6                           inc esi
0085D9E9  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
0085D9ED  EB B8                           jmp 0x14085d9a7
0085D9EF  83 FB 7A                        cmp ebx, 0x7a
0085D9F2  0F 86 F7 04 00 00               jbe 0x14085deef
0085D9F8  0F B7 CB                        movzx ecx, bx
0085D9FB  E8 F0 16 00 00                  call 0x14085f0f0
0085DA00  0F B7 C0                        movzx eax, ax
0085DA03  EB DA                           jmp 0x14085d9df
0085DA05  66 83 F9 7A                     cmp cx, 0x7a
0085DA09  0F 86 5C 03 00 00               jbe 0x14085dd6b
0085DA0F  E8 DC 16 00 00                  call 0x14085f0f0
0085DA14  0F B7 F8                        movzx edi, ax
0085DA17  EB BF                           jmp 0x14085d9d8
0085DA19  85 FF                           test edi, edi
0085DA1B  BA 01 00 00 00                  mov edx, 1
0085DA20  B8 FF FF FF FF                  mov eax, 0xffffffff
0085DA25  0F 4E D0                        cmovle edx, eax
0085DA28  4C 8B 65 C0                     mov r12, qword ptr [rbp - 0x40]
0085DA2C  85 D2                           test edx, edx
0085DA2E  0F 84 93 06 00 00               je 0x14085e0c7
0085DA34  0F 89 E7 00 00 00               jns 0x14085db21
0085DA3A  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
0085DA3F  BA 6C 66 00 00                  mov edx, 0x666c
0085DA44  48 8B 5D 68                     mov rbx, qword ptr [rbp + 0x68]
0085DA48  0F B7 C1                        movzx eax, cx
0085DA4B  66 2B C2                        sub ax, dx
0085DA4E  41 B8 FF FD 00 00               mov r8d, 0xfdff
0085DA54  C7 03 FF FF FF FF               mov dword ptr [rbx], 0xffffffff
0085DA5A  66 41 85 C0                     test r8w, ax
0085DA5E  0F 85 A8 04 00 00               jne 0x14085df0c
0085DA64  66 3B CA                        cmp cx, dx
0085DA67  0F 85 0A 04 00 00               jne 0x14085de77
0085DA6D  33 D2                           xor edx, edx
0085DA6F  41 BE 04 00 00 00               mov r14d, 4
0085DA75  8B CA                           mov ecx, edx
0085DA77  41 3B CE                        cmp ecx, r14d
0085DA7A  73 1A                           jae 0x14085da96
0085DA7C  8B C1                           mov eax, ecx
0085DA7E  42 38 54 20 08                  cmp byte ptr [rax + r12 + 8], dl
0085DA83  74 0E                           je 0x14085da93
0085DA85  FF C1                           inc ecx
0085DA87  EB EE                           jmp 0x14085da77
0085DA89  E8 22 72 FF FF                  call 0x140854cb0
0085DA8E  E9 7C FE FF FF                  jmp 0x14085d90f
0085DA93  44 8B F1                        mov r14d, ecx
0085DA96  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0085DA9A  48 85 C9                        test rcx, rcx
0085DA9D  0F 85 78 06 00 00               jne 0x14085e11b
0085DAA3  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0085DAA7  0F B7 00                        movzx eax, word ptr [rax]
0085DAAA  D1 E8                           shr eax, 1
0085DAAC  41 3B C6                        cmp eax, r14d
0085DAAF  8B F2                           mov esi, edx
0085DAB1  44 0F 42 F0                     cmovb r14d, eax
0085DAB5  41 3B F6                        cmp esi, r14d
0085DAB8  0F 83 93 05 00 00               jae 0x14085e051
0085DABE  8B D6                           mov edx, esi
0085DAC0  48 85 C9                        test rcx, rcx
0085DAC3  0F 85 33 06 00 00               jne 0x14085e0fc
0085DAC9  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0085DACD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0085DAD1  0F B7 0C 50                     movzx ecx, word ptr [rax + rdx*2]
0085DAD5  42 0F B6 7C 22 08               movzx edi, byte ptr [rdx + r12 + 8]
0085DADB  66 83 F9 61                     cmp cx, 0x61
0085DADF  73 2C                           jae 0x14085db0d
0085DAE1  0F B7 D9                        movzx ebx, cx
0085DAE4  83 FF 61                        cmp edi, 0x61
0085DAE7  73 0E                           jae 0x14085daf7
0085DAE9  8B C7                           mov eax, edi
0085DAEB  2B D8                           sub ebx, eax
0085DAED  75 3E                           jne 0x14085db2d
0085DAEF  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0085DAF3  FF C6                           inc esi
0085DAF5  EB BE                           jmp 0x14085dab5
0085DAF7  83 FF 7A                        cmp edi, 0x7a
0085DAFA  0F 86 A5 04 00 00               jbe 0x14085dfa5
0085DB00  0F B7 CF                        movzx ecx, di
0085DB03  E8 E8 15 00 00                  call 0x14085f0f0
0085DB08  0F B7 C0                        movzx eax, ax
0085DB0B  EB DE                           jmp 0x14085daeb
0085DB0D  66 83 F9 7A                     cmp cx, 0x7a
0085DB11  0F 86 29 04 00 00               jbe 0x14085df40
0085DB17  E8 D4 15 00 00                  call 0x14085f0f0
0085DB1C  0F B7 D8                        movzx ebx, ax
0085DB1F  EB C3                           jmp 0x14085dae4
0085DB21  8B 7D E0                        mov edi, dword ptr [rbp - 0x20]
0085DB24  41 8B F7                        mov esi, r15d
0085DB27  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
0085DB2B  EB 2A                           jmp 0x14085db57
0085DB2D  85 DB                           test ebx, ebx
0085DB2F  BA 01 00 00 00                  mov edx, 1
0085DB34  B8 FF FF FF FF                  mov eax, 0xffffffff
0085DB39  0F 4E D0                        cmovle edx, eax
0085DB3C  83 FA 02                        cmp edx, 2
0085DB3F  0F 84 55 03 00 00               je 0x14085de9a
0085DB45  85 D2                           test edx, edx
0085DB47  0F 89 74 04 00 00               jns 0x14085dfc1
0085DB4D  8B 75 DC                        mov esi, dword ptr [rbp - 0x24]
0085DB50  41 8B FF                        mov edi, r15d
0085DB53  44 89 7D E0                     mov dword ptr [rbp - 0x20], r15d
0085DB57  8B C7                           mov eax, edi
0085DB59  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0085DB5D  2B C6                           sub eax, esi
0085DB5F  49 8B CD                        mov rcx, r13
0085DB62  83 F8 01                        cmp eax, 1
0085DB65  0F 86 50 02 00 00               jbe 0x14085ddbb
0085DB6B  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DB73  0F 85 2E 05 00 00               jne 0x14085e0a7
0085DB79  E8 C2 83 FF FF                  call 0x140855f40
0085DB7E  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
0085DB82  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
0085DB86  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
0085DB8A  E9 46 FD FF FF                  jmp 0x14085d8d5
0085DB8F  8B 55 D8                        mov edx, dword ptr [rbp - 0x28]
0085DB92  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
0085DB96  33 F6                           xor esi, esi
0085DB98  8B C2                           mov eax, edx
0085DB9A  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DBA2  49 8B CD                        mov rcx, r13
0085DBA5  C7 45 D0 FF FF FF FF            mov dword ptr [rbp - 0x30], 0xffffffff
0085DBAC  89 75 D4                        mov dword ptr [rbp - 0x2c], esi
0085DBAF  41 8B 54 C0 04                  mov edx, dword ptr [r8 + rax*8 + 4]
0085DBB4  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0085DBB8  0F 84 A0 03 00 00               je 0x14085df5e
0085DBBE  E8 9D 70 FF FF                  call 0x140854c60
0085DBC3  48 8B C8                        mov rcx, rax
0085DBC6  48 85 C0                        test rax, rax
0085DBC9  0F 84 CB 02 00 00               je 0x14085de9a
0085DBCF  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085DBD3  4C 8D 60 4C                     lea r12, [rax + 0x4c]
0085DBD7  0F 84 9C 05 00 00               je 0x14085e179
0085DBDD  48 85 DB                        test rbx, rbx
0085DBE0  0F 85 3D 05 00 00               jne 0x14085e123
0085DBE6  41 0F B7 3E                     movzx edi, word ptr [r14]
0085DBEA  4D 8B 7E 08                     mov r15, qword ptr [r14 + 8]
0085DBEE  44 0F B7 70 48                  movzx r14d, word ptr [rax + 0x48]
0085DBF3  66 D1 EF                        shr di, 1
0085DBF6  66 85 FF                        test di, di
0085DBF9  74 64                           je 0x14085dc5f
0085DBFB  66 45 85 F6                     test r14w, r14w
0085DBFF  74 5E                           je 0x14085dc5f
0085DC01  41 0F B7 1F                     movzx ebx, word ptr [r15]
0085DC05  49 83 C7 02                     add r15, 2
0085DC09  41 0F B6 34 24                  movzx esi, byte ptr [r12]
0085DC0E  49 FF C4                        inc r12
0085DC11  66 3B DE                        cmp bx, si
0085DC14  74 3B                           je 0x14085dc51
0085DC16  66 83 FB 61                     cmp bx, 0x61
0085DC1A  0F 82 C5 02 00 00               jb 0x14085dee5
0085DC20  66 83 FB 7A                     cmp bx, 0x7a
0085DC24  0F 87 B0 02 00 00               ja 0x14085deda
0085DC2A  B8 E0 FF 00 00                  mov eax, 0xffe0
0085DC2F  66 03 D8                        add bx, ax
0085DC32  83 FE 61                        cmp esi, 0x61
0085DC35  72 0C                           jb 0x14085dc43
0085DC37  83 FE 7A                        cmp esi, 0x7a
0085DC3A  0F 87 19 05 00 00               ja 0x14085e159
0085DC40  66 03 F0                        add si, ax
0085DC43  0F B7 C6                        movzx eax, si
0085DC46  0F B7 DB                        movzx ebx, bx
0085DC49  2B D8                           sub ebx, eax
0085DC4B  0F 85 1B 04 00 00               jne 0x14085e06c
0085DC51  B8 FF FF 00 00                  mov eax, 0xffff
0085DC56  66 03 F8                        add di, ax
0085DC59  66 44 03 F0                     add r14w, ax
0085DC5D  EB 97                           jmp 0x14085dbf6
0085DC5F  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
0085DC63  41 0F B7 C6                     movzx eax, r14w
0085DC67  0F B7 DF                        movzx ebx, di
0085DC6A  2B D8                           sub ebx, eax
0085DC6C  33 F6                           xor esi, esi
0085DC6E  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DC76  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0085DC7A  49 8B CD                        mov rcx, r13
0085DC7D  0F 85 3A 04 00 00               jne 0x14085e0bd
0085DC83  E8 B8 82 FF FF                  call 0x140855f40
0085DC88  85 DB                           test ebx, ebx
0085DC8A  0F 84 BB 02 00 00               je 0x14085df4b
0085DC90  85 DB                           test ebx, ebx
0085DC92  BA 01 00 00 00                  mov edx, 1
0085DC97  B8 FF FF FF FF                  mov eax, 0xffffffff
0085DC9C  0F 48 D0                        cmovs edx, eax
0085DC9F  E9 84 FD FF FF                  jmp 0x14085da28
0085DCA4  41 8B 54 90 04                  mov edx, dword ptr [r8 + rdx*4 + 4]
0085DCA9  33 F6                           xor esi, esi
0085DCAB  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DCB3  4C 8D 45 C8                     lea r8, [rbp - 0x38]
0085DCB7  C7 45 C8 FF FF FF FF            mov dword ptr [rbp - 0x38], 0xffffffff
0085DCBE  49 8B CD                        mov rcx, r13
0085DCC1  89 75 CC                        mov dword ptr [rbp - 0x34], esi
0085DCC4  0F 84 9E 02 00 00               je 0x14085df68
0085DCCA  E8 91 6F FF FF                  call 0x140854c60
0085DCCF  48 8B C8                        mov rcx, rax
0085DCD2  48 85 C0                        test rax, rax
0085DCD5  0F 84 BF 01 00 00               je 0x14085de9a
0085DCDB  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085DCDF  4C 8D 60 4C                     lea r12, [rax + 0x4c]
0085DCE3  0F 84 BB 04 00 00               je 0x14085e1a4
0085DCE9  48 85 DB                        test rbx, rbx
0085DCEC  0F 85 4C 04 00 00               jne 0x14085e13e
0085DCF2  41 0F B7 3E                     movzx edi, word ptr [r14]
0085DCF6  4D 8B 7E 08                     mov r15, qword ptr [r14 + 8]
0085DCFA  44 0F B7 70 48                  movzx r14d, word ptr [rax + 0x48]
0085DCFF  66 D1 EF                        shr di, 1
0085DD02  66 85 FF                        test di, di
0085DD05  74 6F                           je 0x14085dd76
0085DD07  66 45 85 F6                     test r14w, r14w
0085DD0B  74 69                           je 0x14085dd76
0085DD0D  41 0F B7 1F                     movzx ebx, word ptr [r15]
0085DD11  49 83 C7 02                     add r15, 2
0085DD15  41 0F B6 34 24                  movzx esi, byte ptr [r12]
0085DD1A  49 FF C4                        inc r12
0085DD1D  66 3B DE                        cmp bx, si
0085DD20  74 3B                           je 0x14085dd5d
0085DD22  66 83 FB 61                     cmp bx, 0x61
0085DD26  0F 82 D6 01 00 00               jb 0x14085df02
0085DD2C  66 83 FB 7A                     cmp bx, 0x7a
0085DD30  0F 87 C1 01 00 00               ja 0x14085def7
0085DD36  B8 E0 FF 00 00                  mov eax, 0xffe0
0085DD3B  66 03 D8                        add bx, ax
0085DD3E  83 FE 61                        cmp esi, 0x61
0085DD41  72 0C                           jb 0x14085dd4f
0085DD43  83 FE 7A                        cmp esi, 0x7a
0085DD46  0F 87 1D 04 00 00               ja 0x14085e169
0085DD4C  66 03 F0                        add si, ax
0085DD4F  0F B7 C6                        movzx eax, si
0085DD52  0F B7 DB                        movzx ebx, bx
0085DD55  2B D8                           sub ebx, eax
0085DD57  0F 85 3F 03 00 00               jne 0x14085e09c
0085DD5D  B8 FF FF 00 00                  mov eax, 0xffff
0085DD62  66 03 F8                        add di, ax
0085DD65  66 44 03 F0                     add r14w, ax
0085DD69  EB 97                           jmp 0x14085dd02
0085DD6B  0F B7 F9                        movzx edi, cx
0085DD6E  83 EF 20                        sub edi, 0x20
0085DD71  E9 62 FC FF FF                  jmp 0x14085d9d8
0085DD76  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
0085DD7A  41 0F B7 C6                     movzx eax, r14w
0085DD7E  0F B7 DF                        movzx ebx, di
0085DD81  2B D8                           sub ebx, eax
0085DD83  33 F6                           xor esi, esi
0085DD85  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DD8D  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0085DD91  49 8B CD                        mov rcx, r13
0085DD94  0F 85 4E 03 00 00               jne 0x14085e0e8
0085DD9A  E8 A1 81 FF FF                  call 0x140855f40
0085DD9F  4C 8B 65 C0                     mov r12, qword ptr [rbp - 0x40]
0085DDA3  85 DB                           test ebx, ebx
0085DDA5  0F 84 C7 01 00 00               je 0x14085df72
0085DDAB  0F 88 5C 05 00 00               js 0x14085e30d
0085DDB1  BA 01 00 00 00                  mov edx, 1
0085DDB6  E9 71 FC FF FF                  jmp 0x14085da2c
0085DDBB  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DDC3  0F 85 29 03 00 00               jne 0x14085e0f2
0085DDC9  E8 72 81 FF FF                  call 0x140855f40
0085DDCE  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DDD6  4C 8D 45 B8                     lea r8, [rbp - 0x48]
0085DDDA  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
0085DDDE  49 8B CD                        mov rcx, r13
0085DDE1  8B C6                           mov eax, esi
0085DDE3  45 8B 74 86 04                  mov r14d, dword ptr [r14 + rax*4 + 4]
0085DDE8  41 8B D6                        mov edx, r14d
0085DDEB  0F 84 96 01 00 00               je 0x14085df87
0085DDF1  E8 6A 6E FF FF                  call 0x140854c60
0085DDF6  48 8B D8                        mov rbx, rax
0085DDF9  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0085DDFD  48 85 DB                        test rbx, rbx
0085DE00  0F 84 8F 01 00 00               je 0x14085df95
0085DE06  44 0F B7 4B 02                  movzx r9d, word ptr [rbx + 2]
0085DE0B  49 8B CD                        mov rcx, r13
0085DE0E  4C 8B 7D 60                     mov r15, qword ptr [rbp + 0x60]
0085DE12  41 FF C9                        dec r9d
0085DE15  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
0085DE19  4D 8B C7                        mov r8, r15
0085DE1C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085DE21  49 8B D4                        mov rdx, r12
0085DE24  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0085DE29  E8 12 EE FF FF                  call 0x14085cc40
0085DE2E  83 F8 02                        cmp eax, 2
0085DE31  74 67                           je 0x14085de9a
0085DE33  85 C0                           test eax, eax
0085DE35  0F 84 9B 03 00 00               je 0x14085e1d6
0085DE3B  49 8B CD                        mov rcx, r13
0085DE3E  0F 89 89 01 00 00               jns 0x14085dfcd
0085DE44  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0085DE48  45 33 C9                        xor r9d, r9d
0085DE4B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085DE50  4D 8B C7                        mov r8, r15
0085DE53  49 8B D4                        mov rdx, r12
0085DE56  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0085DE5B  E8 E0 ED FF FF                  call 0x14085cc40
0085DE60  83 F8 02                        cmp eax, 2
0085DE63  74 35                           je 0x14085de9a
0085DE65  8B DE                           mov ebx, esi
0085DE67  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
0085DE6B  85 C0                           test eax, eax
0085DE6D  79 3A                           jns 0x14085dea9
0085DE6F  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085DE75  EB 32                           jmp 0x14085dea9
0085DE77  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0085DE7B  45 8B 4C 24 04                  mov r9d, dword ptr [r12 + 4]
0085DE80  4C 8B C1                        mov r8, rcx
0085DE83  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
0085DE87  49 8B CD                        mov rcx, r13
0085DE8A  E8 F1 6F FF FF                  call 0x140854e80
0085DE8F  8B D0                           mov edx, eax
0085DE91  83 F8 02                        cmp eax, 2
0085DE94  0F 85 13 01 00 00               jne 0x14085dfad
0085DE9A  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085DEA0  BB 00 00 00 80                  mov ebx, 0x80000000
0085DEA5  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
0085DEA9  44 89 36                        mov dword ptr [rsi], r14d
0085DEAC  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0085DEB0  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DEB8  49 8B CD                        mov rcx, r13
0085DEBB  0F 85 C6 01 00 00               jne 0x14085e087
0085DEC1  E8 7A 80 FF FF                  call 0x140855f40
0085DEC6  8B C3                           mov eax, ebx
0085DEC8  48 83 C4 78                     add rsp, 0x78
0085DECC  41 5F                           pop r15
0085DECE  41 5E                           pop r14
0085DED0  41 5D                           pop r13
0085DED2  41 5C                           pop r12
0085DED4  5F                              pop rdi
0085DED5  5E                              pop rsi
0085DED6  5B                              pop rbx
0085DED7  5D                              pop rbp
0085DED8  C3                              ret
0085DED9  CC                              int3
0085DEDA  0F B7 CB                        movzx ecx, bx
0085DEDD  E8 0E 12 00 00                  call 0x14085f0f0
0085DEE2  0F B7 D8                        movzx ebx, ax
0085DEE5  B8 E0 FF 00 00                  mov eax, 0xffe0
0085DEEA  E9 43 FD FF FF                  jmp 0x14085dc32
0085DEEF  8D 43 E0                        lea eax, [rbx - 0x20]
0085DEF2  E9 E8 FA FF FF                  jmp 0x14085d9df
0085DEF7  0F B7 CB                        movzx ecx, bx
0085DEFA  E8 F1 11 00 00                  call 0x14085f0f0
0085DEFF  0F B7 D8                        movzx ebx, ax
0085DF02  B8 E0 FF 00 00                  mov eax, 0xffe0
0085DF07  E9 32 FE FF FF                  jmp 0x14085dd3e
0085DF0C  45 8B 4C 24 04                  mov r9d, dword ptr [r12 + 4]
0085DF11  49 8B CD                        mov rcx, r13
0085DF14  4C 8B 45 60                     mov r8, qword ptr [rbp + 0x60]
0085DF18  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
0085DF1C  E8 5F 6F FF FF                  call 0x140854e80
0085DF21  8B D0                           mov edx, eax
0085DF23  83 F8 02                        cmp eax, 2
0085DF26  0F 84 6E FF FF FF               je 0x14085de9a
0085DF2C  85 C0                           test eax, eax
0085DF2E  0F 85 08 FC FF FF               jne 0x14085db3c
0085DF34  41 8B 4C 24 04                  mov ecx, dword ptr [r12 + 4]
0085DF39  89 0B                           mov dword ptr [rbx], ecx
0085DF3B  E9 FC FB FF FF                  jmp 0x14085db3c
0085DF40  0F B7 D9                        movzx ebx, cx
0085DF43  83 EB 20                        sub ebx, 0x20
0085DF46  E9 99 FB FF FF                  jmp 0x14085dae4
0085DF4B  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0085DF4F  8B D6                           mov edx, esi
0085DF51  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
0085DF55  8B 00                           mov eax, dword ptr [rax]
0085DF57  89 06                           mov dword ptr [rsi], eax
0085DF59  E9 CA FA FF FF                  jmp 0x14085da28
0085DF5E  E8 4D 6D FF FF                  call 0x140854cb0
0085DF63  E9 5B FC FF FF                  jmp 0x14085dbc3
0085DF68  E8 43 6D FF FF                  call 0x140854cb0
0085DF6D  E9 5D FD FF FF                  jmp 0x14085dccf
0085DF72  8B 45 D8                        mov eax, dword ptr [rbp - 0x28]
0085DF75  8B D6                           mov edx, esi
0085DF77  41 8B 4C 84 04                  mov ecx, dword ptr [r12 + rax*4 + 4]
0085DF7C  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0085DF80  89 08                           mov dword ptr [rax], ecx
0085DF82  E9 A5 FA FF FF                  jmp 0x14085da2c
0085DF87  E8 24 6D FF FF                  call 0x140854cb0
0085DF8C  E9 65 FE FF FF                  jmp 0x14085ddf6
0085DF91  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0085DF95  C7 00 FF FF FF FF               mov dword ptr [rax], 0xffffffff
0085DF9B  BB 00 00 00 80                  mov ebx, 0x80000000
0085DFA0  E9 21 FF FF FF                  jmp 0x14085dec6
0085DFA5  8D 47 E0                        lea eax, [rdi - 0x20]
0085DFA8  E9 3E FB FF FF                  jmp 0x14085daeb
0085DFAD  85 C0                           test eax, eax
0085DFAF  0F 85 87 FB FF FF               jne 0x14085db3c
0085DFB5  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
0085DFBA  89 03                           mov dword ptr [rbx], eax
0085DFBC  E9 7B FB FF FF                  jmp 0x14085db3c
0085DFC1  8B 5D 48                        mov ebx, dword ptr [rbp + 0x48]
0085DFC4  44 8B 75 E4                     mov r14d, dword ptr [rbp - 0x1c]
0085DFC8  E9 D8 FE FF FF                  jmp 0x14085dea5
0085DFCD  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DFD5  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0085DFD9  0F 85 32 01 00 00               jne 0x14085e111
0085DFDF  E8 5C 7F FF FF                  call 0x140855f40
0085DFE4  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085DFEC  4C 8D 45 B8                     lea r8, [rbp - 0x48]
0085DFF0  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0085DFF4  8B C7                           mov eax, edi
0085DFF6  44 8B 74 81 04                  mov r14d, dword ptr [rcx + rax*4 + 4]
0085DFFB  41 8B D6                        mov edx, r14d
0085DFFE  49 8B CD                        mov rcx, r13
0085E001  74 57                           je 0x14085e05a
0085E003  E8 58 6C FF FF                  call 0x140854c60
0085E008  48 85 C0                        test rax, rax
0085E00B  74 84                           je 0x14085df91
0085E00D  44 0F B7 48 02                  movzx r9d, word ptr [rax + 2]
0085E012  4D 8B C7                        mov r8, r15
0085E015  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
0085E019  41 FF C9                        dec r9d
0085E01C  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0085E021  49 8B D4                        mov rdx, r12
0085E024  49 8B CD                        mov rcx, r13
0085E027  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085E02C  E8 0F EC FF FF                  call 0x14085cc40
0085E031  83 F8 02                        cmp eax, 2
0085E034  74 41                           je 0x14085e077
0085E036  8B DF                           mov ebx, edi
0085E038  85 C0                           test eax, eax
0085E03A  0F 84 69 FE FF FF               je 0x14085dea9
0085E040  0F 88 63 FE FF FF               js 0x14085dea9
0085E046  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085E04C  E9 58 FE FF FF                  jmp 0x14085dea9
0085E051  48 8B 5D 68                     mov rbx, qword ptr [rbp + 0x68]
0085E055  E9 21 FE FF FF                  jmp 0x14085de7b
0085E05A  E8 51 6C FF FF                  call 0x140854cb0
0085E05F  EB A7                           jmp 0x14085e008
0085E061  41 0F B7 C6                     movzx eax, r14w
0085E065  0F B7 DE                        movzx ebx, si
0085E068  2B D8                           sub ebx, eax
0085E06A  F7 DB                           neg ebx
0085E06C  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
0085E070  33 F6                           xor esi, esi
0085E072  E9 F7 FB FF FF                  jmp 0x14085dc6e
0085E077  BB 00 00 00 80                  mov ebx, 0x80000000
0085E07C  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085E082  E9 22 FE FF FF                  jmp 0x14085dea9
0085E087  E8 94 EB FF FF                  call 0x14085cc20
0085E08C  E9 35 FE FF FF                  jmp 0x14085dec6
0085E091  41 0F B7 C6                     movzx eax, r14w
0085E095  0F B7 DE                        movzx ebx, si
0085E098  2B D8                           sub ebx, eax
0085E09A  F7 DB                           neg ebx
0085E09C  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
0085E0A0  33 F6                           xor esi, esi
0085E0A2  E9 DE FC FF FF                  jmp 0x14085dd85
0085E0A7  E8 74 EB FF FF                  call 0x14085cc20
0085E0AC  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
0085E0B0  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
0085E0B4  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
0085E0B8  E9 18 F8 FF FF                  jmp 0x14085d8d5
0085E0BD  E8 5E EB FF FF                  call 0x14085cc20
0085E0C2  E9 C1 FB FF FF                  jmp 0x14085dc88
0085E0C7  48 8B 5D 68                     mov rbx, qword ptr [rbp + 0x68]
0085E0CB  44 8B 75 E4                     mov r14d, dword ptr [rbp - 0x1c]
0085E0CF  48 89 5D 68                     mov qword ptr [rbp + 0x68], rbx
0085E0D3  41 8B DF                        mov ebx, r15d
0085E0D6  E9 CA FD FF FF                  jmp 0x14085dea5
0085E0DB  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0085E0DF  0F B6 0C 30                     movzx ecx, byte ptr [rax + rsi]
0085E0E3  E9 DD F8 FF FF                  jmp 0x14085d9c5
0085E0E8  E8 33 EB FF FF                  call 0x14085cc20
0085E0ED  E9 AD FC FF FF                  jmp 0x14085dd9f
0085E0F2  E8 29 EB FF FF                  call 0x14085cc20
0085E0F7  E9 D2 FC FF FF                  jmp 0x14085ddce
0085E0FC  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0085E100  0F B6 0C 10                     movzx ecx, byte ptr [rax + rdx]
0085E104  E9 CC F9 FF FF                  jmp 0x14085dad5
0085E109  0F B7 03                        movzx eax, word ptr [rbx]
0085E10C  E9 85 F8 FF FF                  jmp 0x14085d996
0085E111  E8 0A EB FF FF                  call 0x14085cc20
0085E116  E9 C9 FE FF FF                  jmp 0x14085dfe4
0085E11B  0F B7 01                        movzx eax, word ptr [rcx]
0085E11E  E9 89 F9 FF FF                  jmp 0x14085daac
0085E123  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085E128  4D 8B C4                        mov r8, r12
0085E12B  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0085E12F  0F B7 13                        movzx edx, word ptr [rbx]
0085E132  E8 D9 94 FE FF                  call 0x140847610
0085E137  8B D8                           mov ebx, eax
0085E139  E9 30 FB FF FF                  jmp 0x14085dc6e
0085E13E  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085E143  4D 8B C4                        mov r8, r12
0085E146  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0085E14A  0F B7 13                        movzx edx, word ptr [rbx]
0085E14D  E8 BE 94 FE FF                  call 0x140847610
0085E152  8B D8                           mov ebx, eax
0085E154  E9 2C FC FF FF                  jmp 0x14085dd85
0085E159  0F B7 CE                        movzx ecx, si
0085E15C  E8 8F 0F 00 00                  call 0x14085f0f0
0085E161  0F B7 F0                        movzx esi, ax
0085E164  E9 DA FA FF FF                  jmp 0x14085dc43
0085E169  0F B7 CE                        movzx ecx, si
0085E16C  E8 7F 0F 00 00                  call 0x14085f0f0
0085E171  0F B7 F0                        movzx esi, ax
0085E174  E9 D6 FB FF FF                  jmp 0x14085dd4f
0085E179  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
0085E17D  48 85 DB                        test rbx, rbx
0085E180  75 5B                           jne 0x14085e1dd
0085E182  41 0F B7 16                     movzx edx, word ptr [r14]
0085E186  44 8B CE                        mov r9d, esi
0085E189  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0085E18D  4D 8B C4                        mov r8, r12
0085E190  49 D1 E9                        shr r9, 1
0085E193  48 D1 EA                        shr rdx, 1
0085E196  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0085E19B  E8 40 46 11 00                  call 0x1409727e0
0085E1A0  33 F6                           xor esi, esi
0085E1A2  EB 93                           jmp 0x14085e137
0085E1A4  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
0085E1A8  48 85 DB                        test rbx, rbx
0085E1AB  0F 85 A8 00 00 00               jne 0x14085e259
0085E1B1  41 0F B7 16                     movzx edx, word ptr [r14]
0085E1B5  44 8B CE                        mov r9d, esi
0085E1B8  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0085E1BC  4D 8B C4                        mov r8, r12
0085E1BF  49 D1 E9                        shr r9, 1
0085E1C2  48 D1 EA                        shr rdx, 1
0085E1C5  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0085E1CA  E8 11 46 11 00                  call 0x1409727e0
0085E1CF  33 F6                           xor esi, esi
0085E1D1  E9 7C FF FF FF                  jmp 0x14085e152
0085E1D6  8B DE                           mov ebx, esi
0085E1D8  E9 C8 FC FF FF                  jmp 0x14085dea5
0085E1DD  4C 8B 7B 08                     mov r15, qword ptr [rbx + 8]
0085E1E1  44 0F B7 33                     movzx r14d, word ptr [rbx]
0085E1E5  66 D1 EE                        shr si, 1
0085E1E8  66 85 F6                        test si, si
0085E1EB  0F 84 70 FE FF FF               je 0x14085e061
0085E1F1  66 45 85 F6                     test r14w, r14w
0085E1F5  0F 84 66 FE FF FF               je 0x14085e061
0085E1FB  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
0085E200  49 83 C4 02                     add r12, 2
0085E204  41 0F B6 3F                     movzx edi, byte ptr [r15]
0085E208  49 FF C7                        inc r15
0085E20B  66 3B DF                        cmp bx, di
0085E20E  74 3B                           je 0x14085e24b
0085E210  66 83 FB 61                     cmp bx, 0x61
0085E214  0F 82 BA 00 00 00               jb 0x14085e2d4
0085E21A  66 83 FB 7A                     cmp bx, 0x7a
0085E21E  0F 87 A5 00 00 00               ja 0x14085e2c9
0085E224  B8 E0 FF 00 00                  mov eax, 0xffe0
0085E229  66 03 D8                        add bx, ax
0085E22C  83 FF 61                        cmp edi, 0x61
0085E22F  72 0C                           jb 0x14085e23d
0085E231  83 FF 7A                        cmp edi, 0x7a
0085E234  0F 87 C3 00 00 00               ja 0x14085e2fd
0085E23A  66 03 F8                        add di, ax
0085E23D  0F B7 C7                        movzx eax, di
0085E240  0F B7 DB                        movzx ebx, bx
0085E243  2B D8                           sub ebx, eax
0085E245  0F 85 1F FE FF FF               jne 0x14085e06a
0085E24B  B8 FF FF 00 00                  mov eax, 0xffff
0085E250  66 03 F0                        add si, ax
0085E253  66 44 03 F0                     add r14w, ax
0085E257  EB 8F                           jmp 0x14085e1e8
0085E259  4C 8B 7B 08                     mov r15, qword ptr [rbx + 8]
0085E25D  44 0F B7 33                     movzx r14d, word ptr [rbx]
0085E261  66 D1 EE                        shr si, 1
0085E264  66 85 F6                        test si, si
0085E267  0F 84 24 FE FF FF               je 0x14085e091
0085E26D  66 45 85 F6                     test r14w, r14w
0085E271  0F 84 1A FE FF FF               je 0x14085e091
0085E277  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
0085E27C  49 83 C4 02                     add r12, 2
0085E280  41 0F B6 3F                     movzx edi, byte ptr [r15]
0085E284  49 FF C7                        inc r15
0085E287  66 3B DF                        cmp bx, di
0085E28A  74 2F                           je 0x14085e2bb
0085E28C  66 83 FB 61                     cmp bx, 0x61
0085E290  72 57                           jb 0x14085e2e9
0085E292  66 83 FB 7A                     cmp bx, 0x7a
0085E296  77 46                           ja 0x14085e2de
0085E298  B8 E0 FF 00 00                  mov eax, 0xffe0
0085E29D  66 03 D8                        add bx, ax
0085E2A0  83 FF 61                        cmp edi, 0x61
0085E2A3  72 08                           jb 0x14085e2ad
0085E2A5  83 FF 7A                        cmp edi, 0x7a
0085E2A8  77 46                           ja 0x14085e2f0
0085E2AA  66 03 F8                        add di, ax
0085E2AD  0F B7 C7                        movzx eax, di
0085E2B0  0F B7 DB                        movzx ebx, bx
0085E2B3  2B D8                           sub ebx, eax
0085E2B5  0F 85 DF FD FF FF               jne 0x14085e09a
0085E2BB  B8 FF FF 00 00                  mov eax, 0xffff
0085E2C0  66 03 F0                        add si, ax
0085E2C3  66 44 03 F0                     add r14w, ax
0085E2C7  EB 9B                           jmp 0x14085e264
0085E2C9  0F B7 CB                        movzx ecx, bx
0085E2CC  E8 1F 0E 00 00                  call 0x14085f0f0
0085E2D1  0F B7 D8                        movzx ebx, ax
0085E2D4  B8 E0 FF 00 00                  mov eax, 0xffe0
0085E2D9  E9 4E FF FF FF                  jmp 0x14085e22c
0085E2DE  0F B7 CB                        movzx ecx, bx
0085E2E1  E8 0A 0E 00 00                  call 0x14085f0f0
0085E2E6  0F B7 D8                        movzx ebx, ax
0085E2E9  B8 E0 FF 00 00                  mov eax, 0xffe0
0085E2EE  EB B0                           jmp 0x14085e2a0
0085E2F0  0F B7 CF                        movzx ecx, di
0085E2F3  E8 F8 0D 00 00                  call 0x14085f0f0
0085E2F8  0F B7 F8                        movzx edi, ax
0085E2FB  EB B0                           jmp 0x14085e2ad
0085E2FD  0F B7 CF                        movzx ecx, di
0085E300  E8 EB 0D 00 00                  call 0x14085f0f0
0085E305  0F B7 F8                        movzx edi, ax
0085E308  E9 30 FF FF FF                  jmp 0x14085e23d
0085E30D  BA FF FF FF FF                  mov edx, 0xffffffff
0085E312  E9 15 F7 FF FF                  jmp 0x14085da2c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFindSubKeyInRoot(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (120);
    a1 = 0;
    v_stack_m88 = 0xFFFFFFFFULL;
    v_rdi = (unsigned int)((*(unsigned __int16 *)(a2 + 2)) - 1);
    v_stack_m84 = 0;
    v_stack_m60 = (unsigned int)(v_rdi);
    v_stack_m64 = 0;
loc_0085D8D5:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (0));
    v_r15 = (unsigned int)((v_r15) >> (1));
    v_r15 = (unsigned int)((v_r15) + (0));
    v_stack_p8 = (unsigned int)(v_r15);
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_r15 * 4 + 4)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085DA89;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_r15 * 4 + 4)))), v_stack_m88, a4);
loc_0085D90F:
    v_stack_m80 = result;
    *(unsigned int *)(a5) = 0xFFFFFFFFULL;
    if (result == 0) goto loc_0085DF9B;
    a2 = (unsigned int)((*(unsigned __int16 *)(result + 2)) - 1);
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    v_stack_m68 = (unsigned int)(a2);
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_0085DCA4;
    a4 = (a2 * 8 + 4) + (result);
    v_stack_m58 = a4;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) != ((unsigned __int16)((unsigned int)(0x666CULL)))) goto loc_0085DB96;
    a1 = 0;
loc_0085D971:
    if (0 >= 4) goto loc_0085D987;
    if ((*(unsigned __int8 *)(0 + a4 * 1 + 4)) == 0) goto loc_0085D984;
    result = (unsigned int)((0) + 1);
    goto loc_0085D971;
loc_0085D984:
loc_0085D987:
    if (a4 != 0) goto loc_0085E109;
    result = (unsigned int)((*(unsigned __int16 *)(a3)) >> (1));
loc_0085D996:
    v_r12 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) { v_r12 = (unsigned int)(result); }
    v_rsi = 0;
loc_0085D9A7:
    if (0 >= ((unsigned int)(v_r12))) goto loc_0085DB8F;
    if (a4 != 0) goto loc_0085E0DB;
loc_0085D9C5:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8) + v_rsi * 2))) >= 97) goto loc_0085DA05;
loc_0085D9D8:
    if (((unsigned int)(*(unsigned __int8 *)(v_rsi + a2 * 8 * 1 + result * 1 + 8))) >= 97) goto loc_0085D9EF;
loc_0085D9DF:
    v_rdi = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8) + v_rsi * 2))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rsi + a2 * 8 * 1 + result * 1 + 8))))));
    if (condition_is_not_equal) goto loc_0085DA19;
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_0085D9A7;
loc_0085D9EF:
    if (((unsigned int)(v_stack_p20)) <= 122) goto loc_0085DEEF;
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_stack_p20), a2, v_stack_m80, a4);
    goto loc_0085D9DF;
loc_0085DA05:
    if (((unsigned __int16)((unsigned __int16)(v_stack_p20))) <= 122) goto loc_0085DD6B;
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_stack_p20), a2, v_stack_m80, a4);
    goto loc_0085D9D8;
loc_0085DA19:
    a2 = 1;
    if (condition_is_less_or_equal) { a2 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
loc_0085DA28:
loc_0085DA2C:
    if ((unsigned int)(a2) == 0) goto loc_0085E0C7;
    if (!sign_flag) goto loc_0085DB21;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m80))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    *(unsigned int *)(a5) = 0xFFFFFFFFULL;
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_0085DF0C;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m80))) != ((unsigned __int16)((unsigned int)(0x666CULL)))) goto loc_0085DE77;
    a2 = 0;
loc_0085DA77:
    if (0 >= 4) goto loc_0085DA96;
    if ((*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8)) == 0) goto loc_0085DA93;
    a1 = (unsigned int)((0) + 1);
    goto loc_0085DA77;
loc_0085DA89:
    result = HvpGetCellPaged(a1, a2, (unsigned int)(0xFDFFULL), a4);
    goto loc_0085D90F;
loc_0085DA93:
loc_0085DA96:
    if (v_stack_p20 != 0) goto loc_0085E11B;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_p18)) >> (1));
loc_0085DAAC:
    v_r14 = (unsigned int)((unsigned int)(a1));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) { v_r14 = (unsigned int)(result); }
loc_0085DAB5:
    if (0 >= ((unsigned int)(v_r14))) goto loc_0085E051;
    if (v_stack_p20 != 0) goto loc_0085E0FC;
loc_0085DAD5:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8) + 0 * 2))) >= 97) goto loc_0085DB0D;
loc_0085DAE4:
    if (((unsigned int)(*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8))) >= 97) goto loc_0085DAF7;
loc_0085DAEB:
    v_rbx = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8) + 0 * 2))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8))))));
    if (condition_is_not_equal) goto loc_0085DB2D;
    v_rsi = (unsigned int)((0) + 1);
    goto loc_0085DAB5;
loc_0085DAF7:
    if (((unsigned int)(*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8))) <= 122) goto loc_0085DFA5;
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8)), 0, (unsigned int)(0xFDFFULL), a4);
    goto loc_0085DAEB;
loc_0085DB0D:
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8)))) <= 122) goto loc_0085DF40;
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int8 *)(0 + v_stack_m80 * 1 + 8)), 0, (unsigned int)(0xFDFFULL), a4);
    goto loc_0085DAE4;
loc_0085DB21:
    v_stack_m64 = (unsigned int)(v_r15);
    goto loc_0085DB57;
loc_0085DB2D:
    a2 = 1;
    if (condition_is_less_or_equal) { a2 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
loc_0085DB3C:
    if (((unsigned int)(a2)) == 2) goto loc_0085DE9A;
    if (!sign_flag) goto loc_0085DFC1;
    v_stack_m60 = (unsigned int)(v_r15);
loc_0085DB57:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15))))) - ((unsigned int)((unsigned int)(v_stack_m64))));
    if (((unsigned int)(result)) <= 1) goto loc_0085DDBB;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085E0A7;
    result = HvpReleaseCellPaged(a1, v_stack_m88, (unsigned int)(0xFDFFULL), a4);
    goto loc_0085D8D5;
loc_0085DB8F:
loc_0085DB96:
    v_rsi = 0;
    v_stack_m70 = 0xFFFFFFFFULL;
    v_stack_m6C = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085DF5E;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)((unsigned int)(0xFDFFULL) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m68))) * 8 + 4)), v_stack_m70, a4);
loc_0085DBC3:
    if (result == 0) goto loc_0085DE9A;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_0085E179;
    if (v_stack_p20 != 0) goto loc_0085E123;
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p18)) >> (1));
loc_0085DBF6:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_0085DC5F;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_0085DC5F;
    v_r15 = (*(unsigned __int64 *)(v_stack_p18 + 8)) + (2);
    v_r12 = (result + 76) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_0085DC51;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8)))) < 97) goto loc_0085DEE5;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8)))) > 122) goto loc_0085DEDA;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085DC32:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_0085DC43;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_0085E159;
    v_rsi = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085DC43:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rsi))));
    if (condition_is_not_equal) goto loc_0085E06C;
loc_0085DC51:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_0085DBF6;
loc_0085DC5F:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_r14))));
    v_rsi = 0;
loc_0085DC6E:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085E0BD;
    result = HvpReleaseCellPaged(a1, v_stack_m70, v_stack_m70, a4);
loc_0085DC88:
    if ((unsigned int)(v_rbx) == 0) goto loc_0085DF4B;
    a2 = 1;
    if (sign_flag) { a2 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
    goto loc_0085DA28;
loc_0085DCA4:
    v_rsi = 0;
    v_stack_m78 = 0xFFFFFFFFULL;
    v_stack_m74 = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085DF68;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(v_stack_m70 + a2 * 4 + 4)), v_stack_m78, a4);
loc_0085DCCF:
    if (result == 0) goto loc_0085DE9A;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_0085E1A4;
    if (v_rbx != 0) goto loc_0085E13E;
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(v_r14)) >> (1));
loc_0085DD02:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_0085DD76;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_0085DD76;
    v_r15 = (*(unsigned __int64 *)(v_r14 + 8)) + (2);
    v_r12 = (result + 76) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_0085DD5D;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) < 97) goto loc_0085DF02;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) > 122) goto loc_0085DEF7;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085DD3E:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_0085DD4F;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_0085E169;
    v_rsi = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085DD4F:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rsi))));
    if (condition_is_not_equal) goto loc_0085E09C;
loc_0085DD5D:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_0085DD02;
loc_0085DD6B:
    v_rdi = (unsigned int)(((unsigned __int16)(result)) - (32));
    goto loc_0085D9D8;
loc_0085DD76:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_r14))));
    v_rsi = 0;
loc_0085DD85:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085E0E8;
    result = HvpReleaseCellPaged(a1, v_stack_m78, v_stack_m78, a4);
loc_0085DD9F:
    if ((unsigned int)(v_rbx) == 0) goto loc_0085DF72;
    if (sign_flag) goto loc_0085E30D;
    goto loc_0085DA2C;
loc_0085DDBB:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085E0F2;
    result = HvpReleaseCellPaged(a1, 1, v_stack_m78, a4);
loc_0085DDCE:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085DF87;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 0 * 4 + 4)))), v_stack_m88, a4);
loc_0085DDF6:
    if (result == 0) goto loc_0085DF95;
    a4 = (unsigned int)((*(unsigned __int16 *)(result + 2)) - 1);
    v_stack_m90 = a5;
    v_stack_m98 = result;
    result = CmpCompareInIndex(a1, v_stack_p18, v_stack_p20, a4);
    if (((unsigned int)(result)) == 2) goto loc_0085DE9A;
    if ((unsigned int)(result) == 0) goto loc_0085E1D6;
    if (!sign_flag) goto loc_0085DFCD;
    a4 = 0;
    v_stack_m90 = a5;
    v_stack_m98 = result;
    result = CmpCompareInIndex(a1, v_stack_p18, v_stack_p20, a4);
    if (((unsigned int)(result)) == 2) goto loc_0085DE9A;
    if (!sign_flag) goto loc_0085DEA9;
    goto loc_0085DEA9;
loc_0085DE77:
loc_0085DE7B:
    result = CmpDoCompareKeyName(a1, v_stack_p18, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    if (((unsigned int)(result)) != 2) goto loc_0085DFAD;
loc_0085DE9A:
loc_0085DEA5:
loc_0085DEA9:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085E087;
    result = HvpReleaseCellPaged(a1, v_stack_m88, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
loc_0085DEC6:
    v_rsp = (v_rsp) + (120);
    return (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)));
loc_0085DEDA:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)(0x80000000ULL)), v_stack_m88, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
loc_0085DEE5:
    goto loc_0085DC32;
loc_0085DEEF:
    goto loc_0085D9DF;
loc_0085DEF7:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), v_stack_m88, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
loc_0085DF02:
    goto loc_0085DD3E;
loc_0085DF0C:
    result = CmpDoCompareKeyName(a1, v_stack_p18, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    if (((unsigned int)(result)) == 2) goto loc_0085DE9A;
    if ((unsigned int)(result) != 0) goto loc_0085DB3C;
    *(unsigned int *)((unsigned __int16)(result)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    goto loc_0085DB3C;
loc_0085DF40:
    v_rbx = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)))) - (32));
    goto loc_0085DAE4;
loc_0085DF4B:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58)));
    goto loc_0085DA28;
loc_0085DF5E:
    result = HvpGetCellPaged((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)), (unsigned int)((unsigned int)(a5)), v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    goto loc_0085DBC3;
loc_0085DF68:
    result = HvpGetCellPaged((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)), (unsigned int)((unsigned int)(a5)), v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    goto loc_0085DCCF;
loc_0085DF72:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + (unsigned int)(v_stack_m68) * 4 + 4)));
    goto loc_0085DA2C;
loc_0085DF87:
    result = HvpGetCellPaged((unsigned int)(*(unsigned int *)(v_stack_p18 + (unsigned int)(v_stack_m68) * 4 + 4)), (unsigned int)((unsigned int)(a5)), v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    goto loc_0085DDF6;
loc_0085DF91:
loc_0085DF95:
    *(unsigned int *)(a5) = 0xFFFFFFFFULL;
loc_0085DF9B:
    goto loc_0085DEC6;
loc_0085DFA5:
    goto loc_0085DAEB;
loc_0085DFAD:
    if ((unsigned int)(v_rdi - 32) != 0) goto loc_0085DB3C;
    *(unsigned int *)((unsigned int)(0x80000000ULL)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    goto loc_0085DB3C;
loc_0085DFC1:
    goto loc_0085DEA5;
loc_0085DFCD:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0085E111;
    result = HvpReleaseCellPaged((unsigned int)(*(unsigned int *)(v_stack_p18 + (unsigned int)(v_stack_m68) * 4 + 4)), v_stack_m88, v_stack_p20, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
loc_0085DFE4:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085E05A;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + (unsigned int)((unsigned int)(v_rdi)) * 4 + 4)))), v_stack_m88, (unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
loc_0085E008:
    if (result == 0) goto loc_0085DF91;
    a4 = (unsigned int)((*(unsigned __int16 *)(result + 2)) - 1);
    v_stack_p28 = a5;
    v_stack_p20 = result;
    result = CmpCompareInIndex(a1, v_stack_p18, v_stack_p20, a4);
    if (((unsigned int)(result)) == 2) goto loc_0085E077;
    if ((unsigned int)(result) == 0) goto loc_0085DEA9;
    if (sign_flag) goto loc_0085DEA9;
    goto loc_0085DEA9;
loc_0085E051:
    goto loc_0085DE7B;
loc_0085E05A:
    result = HvpGetCellPaged(a1, v_stack_p18, v_stack_p20, a4);
    goto loc_0085E008;
loc_0085E061:
    v_rbx = (unsigned int)(((unsigned __int16)(a5)) - ((unsigned int)((unsigned __int16)((unsigned int)(0xFFFFFFFFULL)))));
loc_0085E06A:
    v_rbx = (unsigned int)(-(v_rbx));
loc_0085E06C:
    v_rsi = 0;
    goto loc_0085DC6E;
loc_0085E077:
    goto loc_0085DEA9;
loc_0085E087:
    result = HvpReleaseCellFlat(a1, v_stack_p18, v_stack_p20, a4);
    goto loc_0085DEC6;
loc_0085E091:
    v_rbx = (unsigned int)((0) - ((unsigned int)((unsigned __int16)((unsigned int)(0xFFFFFFFFULL)))));
loc_0085E09A:
    v_rbx = (unsigned int)(-(v_rbx));
loc_0085E09C:
    v_rsi = 0;
    goto loc_0085DD85;
loc_0085E0A7:
    result = HvpReleaseCellFlat(a1, v_stack_p18, v_stack_p20, a4);
    goto loc_0085D8D5;
loc_0085E0BD:
    result = HvpReleaseCellFlat(a1, v_stack_p10, v_stack_p20, a4);
    goto loc_0085DC88;
loc_0085E0C7:
    v_stack_p28 = a5;
    goto loc_0085DEA5;
loc_0085E0DB:
    goto loc_0085D9C5;
loc_0085E0E8:
    result = HvpReleaseCellFlat(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + v_rsi * 1), v_stack_p10, v_stack_p20, a4);
    goto loc_0085DD9F;
loc_0085E0F2:
    result = HvpReleaseCellFlat(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + v_rsi * 1), v_stack_p10, v_stack_p20, a4);
    goto loc_0085DDCE;
loc_0085E0FC:
    goto loc_0085DAD5;
loc_0085E109:
    goto loc_0085D996;
loc_0085E111:
    result = HvpReleaseCellFlat(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + v_rsi * 1) + 8) + v_stack_p10 * 1), v_stack_p10, v_stack_p20, a4);
    goto loc_0085DFE4;
loc_0085E11B:
    goto loc_0085DAAC;
loc_0085E123:
    result = CmpCompareTwoCompressedNames(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8), *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))), v_stack_p18, *(unsigned __int16 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + v_rsi * 1) + 8) + v_stack_p10 * 1) + 72));
loc_0085E137:
    goto loc_0085DC6E;
loc_0085E13E:
    result = CmpCompareTwoCompressedNames(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), v_stack_p18, *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + 72));
loc_0085E152:
    goto loc_0085DD85;
loc_0085E159:
    result = RtlUpcaseUnicodeChar(0, *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), v_stack_p18, *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + 72));
    goto loc_0085DC43;
loc_0085E169:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), v_stack_p18, *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) + 8) + 72));
    goto loc_0085DD4F;
loc_0085E179:
    if ((unsigned int)((unsigned int)(result)) != 0) goto loc_0085E1DD;
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned __int16)((unsigned __int16)(result)) + 72)))) >> (1);
    a2 = (*(unsigned __int16 *)((unsigned int)(v_stack_m5C))) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)((unsigned int)(v_stack_m5C) + 8), a2, v_stack_p18, a4);
    v_rsi = 0;
    goto loc_0085E137;
loc_0085E1A4:
    if ((unsigned int)((unsigned int)(result)) != 0) goto loc_0085E259;
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m5C) + 8) + 72)))) >> (1);
    a2 = (*(unsigned __int16 *)((unsigned int)(v_stack_m5C))) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)((unsigned int)(v_stack_m5C) + 8), a2, v_stack_p18, a4);
    v_rsi = 0;
    goto loc_0085E152;
loc_0085E1D6:
    goto loc_0085DEA5;
loc_0085E1DD:
    v_rsi = (unsigned __int16)((v_rsi) >> (1));
loc_0085E1E8:
    if ((unsigned __int16)(v_rsi) == 0) goto loc_0085E061;
    if ((unsigned __int16)(*(unsigned __int16 *)(0)) == 0) goto loc_0085E061;
    v_r12 = (v_stack_p18) + (2);
    v_r15 = (*(unsigned __int64 *)(0 + 8)) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p18))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 8))))) goto loc_0085E24B;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p18))) < 97) goto loc_0085E2D4;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p18))) > 122) goto loc_0085E2C9;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p18)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085E22C:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 8)))) < 97) goto loc_0085E23D;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 8)))) > 122) goto loc_0085E2FD;
    v_rdi = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085E23D:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rdi))));
    if (condition_is_not_equal) goto loc_0085E06A;
loc_0085E24B:
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(0)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_0085E1E8;
loc_0085E259:
    v_rsi = (unsigned __int16)((v_rsi) >> (1));
loc_0085E264:
    if ((unsigned __int16)(v_rsi) == 0) goto loc_0085E091;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_0085E091;
    v_r12 = (v_r12) + (2);
    v_r15 = (*(unsigned __int64 *)(v_rbx + 8)) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r12))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 8))))) goto loc_0085E2BB;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r12))) < 97) goto loc_0085E2E9;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r12))) > 122) goto loc_0085E2DE;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(v_r12)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085E2A0:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 8)))) < 97) goto loc_0085E2AD;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 8)))) > 122) goto loc_0085E2F0;
    v_rdi = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085E2AD:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rdi))));
    if (condition_is_not_equal) goto loc_0085E09A;
loc_0085E2BB:
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_0085E264;
loc_0085E2C9:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rbx), a2, v_stack_p18, a4);
loc_0085E2D4:
    goto loc_0085E22C;
loc_0085E2DE:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), a2, v_stack_p18, a4);
loc_0085E2E9:
    goto loc_0085E2A0;
loc_0085E2F0:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rdi), a2, v_stack_p18, a4);
    goto loc_0085E2AD;
loc_0085E2FD:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), a2, v_stack_p18, a4);
    goto loc_0085E23D;
loc_0085E30D:
    goto loc_0085DA2C;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFindSubKeyInRoot(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (120);
    Arg1 = 0;
    v_stack_m88 = 0xFFFFFFFFULL;
    local_rdi = (uint32_t)((*(uint16_t *)(arg2 + 0x2)) - 1);
    v_stack_m84 = 0;
    v_stack_m60 = (uint32_t)(local_rdi);
    v_stack_m64 = 0;
loc_0085D8D5:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (0));
    local_r15 = (uint32_t)((local_r15) >> (1));
    local_r15 = (uint32_t)((local_r15) + (0));
    v_stack_p8 = (uint32_t)(local_r15);
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + local_r15 * 4 + 0x4)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085DA89;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + local_r15 * 4 + 0x4)))), v_stack_m88, Arg4);
loc_0085D90F:
    v_stack_m80 = result;
    *(uint32_t *)(arg5) = 0xFFFFFFFFULL;
    if (result == 0) goto loc_0085DF9B;
    Arg2 = (uint32_t)((*(uint16_t *)(result + 0x2)) - 1);
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(result))) - ((uint16_t)((uint32_t)(0x666CULL))));
    v_stack_m68 = (uint32_t)(Arg2);
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) != 0) goto loc_0085DCA4;
    Arg4 = (Arg2 * 8 + 4) + (result);
    v_stack_m58 = Arg4;
    if (((uint16_t)(*(uint16_t *)(result))) != ((uint16_t)((uint32_t)(0x666CULL)))) goto loc_0085DB96;
    Arg1 = 0;
loc_0085D971:
    if (0 >= 4) goto loc_0085D987;
    if ((*(uint8_t *)(0 + Arg4 * 1 + 0x4)) == 0) goto loc_0085D984;
    result = (uint32_t)((0) + 1);
    goto loc_0085D971;
loc_0085D984:
loc_0085D987:
    if (Arg4 != 0) goto loc_0085E109;
    result = (uint32_t)((*(uint16_t *)(Arg3)) >> (1));
loc_0085D996:
    local_r12 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) { local_r12 = (uint32_t)(result); }
    local_rsi = 0;
loc_0085D9A7:
    if (0 >= ((uint32_t)(local_r12))) goto loc_0085DB8F;
    if (Arg4 != 0) goto loc_0085E0DB;
loc_0085D9C5:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8) + local_rsi * 2))) >= 97) goto loc_0085DA05;
loc_0085D9D8:
    if (((uint32_t)(*(uint8_t *)(local_rsi + arg2 * 8 * 1 + result * 1 + 0x8))) >= 97) goto loc_0085D9EF;
loc_0085D9DF:
    local_rdi = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8) + local_rsi * 2))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rsi + arg2 * 8 * 1 + result * 1 + 0x8))))));
    if (condition_is_not_equal) goto loc_0085DA19;
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_0085D9A7;
loc_0085D9EF:
    if (((uint32_t)(v_stack_p20)) <= 122) goto loc_0085DEEF;
    result = RtlUpcaseUnicodeChar((uint16_t)(v_stack_p20), Arg2, v_stack_m80, Arg4);
    goto loc_0085D9DF;
loc_0085DA05:
    if (((uint16_t)((uint16_t)(v_stack_p20))) <= 122) goto loc_0085DD6B;
    result = RtlUpcaseUnicodeChar((uint16_t)(v_stack_p20), Arg2, v_stack_m80, Arg4);
    goto loc_0085D9D8;
loc_0085DA19:
    Arg2 = 1;
    if (condition_is_less_or_equal) { Arg2 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
loc_0085DA28:
loc_0085DA2C:
    if ((uint32_t)(Arg2) == 0) goto loc_0085E0C7;
    if (!sign_flag) goto loc_0085DB21;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m80))) - ((uint16_t)((uint32_t)(0x666CULL))));
    *(uint32_t *)(arg5) = 0xFFFFFFFFULL;
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) != 0) goto loc_0085DF0C;
    if (((uint16_t)(*(uint16_t *)(v_stack_m80))) != ((uint16_t)((uint32_t)(0x666CULL)))) goto loc_0085DE77;
    Arg2 = 0;
loc_0085DA77:
    if (0 >= 4) goto loc_0085DA96;
    if ((*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8)) == 0) goto loc_0085DA93;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0085DA77;
loc_0085DA89:
    result = HvpGetCellPaged(Arg1, Arg2, (uint32_t)(0xFDFFULL), Arg4);
    goto loc_0085D90F;
loc_0085DA93:
loc_0085DA96:
    if (v_stack_p20 != 0) goto loc_0085E11B;
    result = (uint32_t)((*(uint16_t *)(v_stack_p18)) >> (1));
loc_0085DAAC:
    local_r14 = (uint32_t)((uint32_t)(Arg1));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) { local_r14 = (uint32_t)(result); }
loc_0085DAB5:
    if (0 >= ((uint32_t)(local_r14))) goto loc_0085E051;
    if (v_stack_p20 != 0) goto loc_0085E0FC;
loc_0085DAD5:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8) + 0x0 * 2))) >= 97) goto loc_0085DB0D;
loc_0085DAE4:
    if (((uint32_t)(*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8))) >= 97) goto loc_0085DAF7;
loc_0085DAEB:
    local_rbx = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8) + 0x0 * 2))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8))))));
    if (condition_is_not_equal) goto loc_0085DB2D;
    local_rsi = (uint32_t)((0) + 1);
    goto loc_0085DAB5;
loc_0085DAF7:
    if (((uint32_t)(*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8))) <= 122) goto loc_0085DFA5;
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8)), 0, (uint32_t)(0xFDFFULL), Arg4);
    goto loc_0085DAEB;
loc_0085DB0D:
    if (((uint16_t)((uint16_t)(*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8)))) <= 122) goto loc_0085DF40;
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint8_t *)(0 + v_stack_m80 * 1 + 0x8)), 0, (uint32_t)(0xFDFFULL), Arg4);
    goto loc_0085DAE4;
loc_0085DB21:
    v_stack_m64 = (uint32_t)(local_r15);
    goto loc_0085DB57;
loc_0085DB2D:
    Arg2 = 1;
    if (condition_is_less_or_equal) { Arg2 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
loc_0085DB3C:
    if (((uint32_t)(Arg2)) == 2) goto loc_0085DE9A;
    if (!sign_flag) goto loc_0085DFC1;
    v_stack_m60 = (uint32_t)(local_r15);
loc_0085DB57:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15))))) - ((uint32_t)((uint32_t)(v_stack_m64))));
    if (((uint32_t)(result)) <= 1) goto loc_0085DDBB;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085E0A7;
    result = HvpReleaseCellPaged(Arg1, v_stack_m88, (uint32_t)(0xFDFFULL), Arg4);
    goto loc_0085D8D5;
loc_0085DB8F:
loc_0085DB96:
    local_rsi = 0;
    v_stack_m70 = 0xFFFFFFFFULL;
    v_stack_m6C = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085DF5E;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)((uint32_t)(0xFDFFULL) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m68))) * 8 + 0x4)), v_stack_m70, Arg4);
loc_0085DBC3:
    if (result == 0) goto loc_0085DE9A;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_0085E179;
    if (v_stack_p20 != 0) goto loc_0085E123;
    local_rdi = (uint16_t)((*(uint16_t *)(v_stack_p18)) >> (1));
loc_0085DBF6:
    if ((uint16_t)(local_rdi) == 0) goto loc_0085DC5F;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_0085DC5F;
    local_r15 = (*(uint64_t *)(v_stack_p18 + 0x8)) + (2);
    local_r12 = (result + 76) + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_0085DC51;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8)))) < 97) goto loc_0085DEE5;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8)))) > 122) goto loc_0085DEDA;
    local_rbx = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085DC32:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_0085DC43;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_0085E159;
    local_rsi = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085DC43:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rsi))));
    if (condition_is_not_equal) goto loc_0085E06C;
loc_0085DC51:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_0085DBF6;
loc_0085DC5F:
    local_rbx = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_r14))));
    local_rsi = 0;
loc_0085DC6E:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085E0BD;
    result = HvpReleaseCellPaged(Arg1, v_stack_m70, v_stack_m70, Arg4);
loc_0085DC88:
    if ((uint32_t)(local_rbx) == 0) goto loc_0085DF4B;
    Arg2 = 1;
    if (sign_flag) { Arg2 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
    goto loc_0085DA28;
loc_0085DCA4:
    local_rsi = 0;
    v_stack_m78 = 0xFFFFFFFFULL;
    v_stack_m74 = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085DF68;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m70 + arg2 * 4 + 0x4)), v_stack_m78, Arg4);
loc_0085DCCF:
    if (result == 0) goto loc_0085DE9A;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_0085E1A4;
    if (local_rbx != 0) goto loc_0085E13E;
    local_rdi = (uint16_t)((*(uint16_t *)(local_r14)) >> (1));
loc_0085DD02:
    if ((uint16_t)(local_rdi) == 0) goto loc_0085DD76;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_0085DD76;
    local_r15 = (*(uint64_t *)(local_r14 + 0x8)) + (2);
    local_r12 = (result + 76) + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_0085DD5D;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) < 97) goto loc_0085DF02;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) > 122) goto loc_0085DEF7;
    local_rbx = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085DD3E:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_0085DD4F;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_0085E169;
    local_rsi = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085DD4F:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rsi))));
    if (condition_is_not_equal) goto loc_0085E09C;
loc_0085DD5D:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_0085DD02;
loc_0085DD6B:
    local_rdi = (uint32_t)(((uint16_t)(result)) - (32));
    goto loc_0085D9D8;
loc_0085DD76:
    local_rbx = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_r14))));
    local_rsi = 0;
loc_0085DD85:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085E0E8;
    result = HvpReleaseCellPaged(Arg1, v_stack_m78, v_stack_m78, Arg4);
loc_0085DD9F:
    if ((uint32_t)(local_rbx) == 0) goto loc_0085DF72;
    if (sign_flag) goto loc_0085E30D;
    goto loc_0085DA2C;
loc_0085DDBB:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085E0F2;
    result = HvpReleaseCellPaged(Arg1, 1, v_stack_m78, Arg4);
loc_0085DDCE:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085DF87;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x0 * 4 + 0x4)))), v_stack_m88, Arg4);
loc_0085DDF6:
    if (result == 0) goto loc_0085DF95;
    Arg4 = (uint32_t)((*(uint16_t *)(result + 0x2)) - 1);
    v_stack_m90 = Arg5;
    v_stack_m98 = result;
    result = CmpCompareInIndex(Arg1, v_stack_p18, v_stack_p20, Arg4);
    if (((uint32_t)(result)) == 2) goto loc_0085DE9A;
    if ((uint32_t)(result) == 0) goto loc_0085E1D6;
    if (!sign_flag) goto loc_0085DFCD;
    Arg4 = 0;
    v_stack_m90 = Arg5;
    v_stack_m98 = result;
    result = CmpCompareInIndex(Arg1, v_stack_p18, v_stack_p20, Arg4);
    if (((uint32_t)(result)) == 2) goto loc_0085DE9A;
    if (!sign_flag) goto loc_0085DEA9;
    goto loc_0085DEA9;
loc_0085DE77:
loc_0085DE7B:
    result = CmpDoCompareKeyName(Arg1, v_stack_p18, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    if (((uint32_t)(result)) != 2) goto loc_0085DFAD;
loc_0085DE9A:
loc_0085DEA5:
loc_0085DEA9:
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085E087;
    result = HvpReleaseCellPaged(Arg1, v_stack_m88, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
loc_0085DEC6:
    local_rsp = (local_rsp) + (120);
    return (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)));
loc_0085DEDA:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)(0x80000000ULL)), v_stack_m88, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
loc_0085DEE5:
    goto loc_0085DC32;
loc_0085DEEF:
    goto loc_0085D9DF;
loc_0085DEF7:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), v_stack_m88, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
loc_0085DF02:
    goto loc_0085DD3E;
loc_0085DF0C:
    result = CmpDoCompareKeyName(Arg1, v_stack_p18, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    if (((uint32_t)(result)) == 2) goto loc_0085DE9A;
    if ((uint32_t)(result) != 0) goto loc_0085DB3C;
    *(uint32_t *)((uint16_t)(result)) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    goto loc_0085DB3C;
loc_0085DF40:
    local_rbx = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)))) - (32));
    goto loc_0085DAE4;
loc_0085DF4B:
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58)));
    goto loc_0085DA28;
loc_0085DF5E:
    result = HvpGetCellPaged((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)), (uint32_t)((uint32_t)(Arg5)), v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    goto loc_0085DBC3;
loc_0085DF68:
    result = HvpGetCellPaged((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)), (uint32_t)((uint32_t)(Arg5)), v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    goto loc_0085DCCF;
loc_0085DF72:
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + (uint32_t)(v_stack_m68) * 4 + 0x4)));
    goto loc_0085DA2C;
loc_0085DF87:
    result = HvpGetCellPaged((uint32_t)(*(uint32_t *)(v_stack_p18 + (uint32_t)(v_stack_m68) * 4 + 0x4)), (uint32_t)((uint32_t)(Arg5)), v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    goto loc_0085DDF6;
loc_0085DF91:
loc_0085DF95:
    *(uint32_t *)(arg5) = 0xFFFFFFFFULL;
loc_0085DF9B:
    goto loc_0085DEC6;
loc_0085DFA5:
    goto loc_0085DAEB;
loc_0085DFAD:
    if ((uint32_t)(local_rdi - 32) != 0) goto loc_0085DB3C;
    *(uint32_t *)((uint32_t)(0x80000000ULL)) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    goto loc_0085DB3C;
loc_0085DFC1:
    goto loc_0085DEA5;
loc_0085DFCD:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0085E111;
    result = HvpReleaseCellPaged((uint32_t)(*(uint32_t *)(v_stack_p18 + (uint32_t)(v_stack_m68) * 4 + 0x4)), v_stack_m88, v_stack_p20, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
loc_0085DFE4:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085E05A;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x4)))), v_stack_m88, (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
loc_0085E008:
    if (result == 0) goto loc_0085DF91;
    Arg4 = (uint32_t)((*(uint16_t *)(result + 0x2)) - 1);
    v_stack_p28 = Arg5;
    v_stack_p20 = result;
    result = CmpCompareInIndex(Arg1, v_stack_p18, v_stack_p20, Arg4);
    if (((uint32_t)(result)) == 2) goto loc_0085E077;
    if ((uint32_t)(result) == 0) goto loc_0085DEA9;
    if (sign_flag) goto loc_0085DEA9;
    goto loc_0085DEA9;
loc_0085E051:
    goto loc_0085DE7B;
loc_0085E05A:
    result = HvpGetCellPaged(Arg1, v_stack_p18, v_stack_p20, Arg4);
    goto loc_0085E008;
loc_0085E061:
    local_rbx = (uint32_t)(((uint16_t)(Arg5)) - ((uint32_t)((uint16_t)((uint32_t)(0xFFFFFFFFULL)))));
loc_0085E06A:
    local_rbx = (uint32_t)(-(local_rbx));
loc_0085E06C:
    local_rsi = 0;
    goto loc_0085DC6E;
loc_0085E077:
    goto loc_0085DEA9;
loc_0085E087:
    result = HvpReleaseCellFlat(Arg1, v_stack_p18, v_stack_p20, Arg4);
    goto loc_0085DEC6;
loc_0085E091:
    local_rbx = (uint32_t)((0) - ((uint32_t)((uint16_t)((uint32_t)(0xFFFFFFFFULL)))));
loc_0085E09A:
    local_rbx = (uint32_t)(-(local_rbx));
loc_0085E09C:
    local_rsi = 0;
    goto loc_0085DD85;
loc_0085E0A7:
    result = HvpReleaseCellFlat(Arg1, v_stack_p18, v_stack_p20, Arg4);
    goto loc_0085D8D5;
loc_0085E0BD:
    result = HvpReleaseCellFlat(Arg1, v_stack_p10, v_stack_p20, Arg4);
    goto loc_0085DC88;
loc_0085E0C7:
    v_stack_p28 = Arg5;
    goto loc_0085DEA5;
loc_0085E0DB:
    goto loc_0085D9C5;
loc_0085E0E8:
    result = HvpReleaseCellFlat(*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + local_rsi * 1), v_stack_p10, v_stack_p20, Arg4);
    goto loc_0085DD9F;
loc_0085E0F2:
    result = HvpReleaseCellFlat(*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + local_rsi * 1), v_stack_p10, v_stack_p20, Arg4);
    goto loc_0085DDCE;
loc_0085E0FC:
    goto loc_0085DAD5;
loc_0085E109:
    goto loc_0085D996;
loc_0085E111:
    result = HvpReleaseCellFlat(*(uint8_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + local_rsi * 1) + 0x8) + v_stack_p10 * 1), v_stack_p10, v_stack_p20, Arg4);
    goto loc_0085DFE4;
loc_0085E11B:
    goto loc_0085DAAC;
loc_0085E123:
    result = CmpCompareTwoCompressedNames(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8), *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))), v_stack_p18, *(uint16_t *)(*(uint8_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + local_rsi * 1) + 0x8) + v_stack_p10 * 1) + 0x48));
loc_0085E137:
    goto loc_0085DC6E;
loc_0085E13E:
    result = CmpCompareTwoCompressedNames(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8), *(uint16_t *)((uint32_t)((uint32_t)(result))), v_stack_p18, *(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + 0x48));
loc_0085E152:
    goto loc_0085DD85;
loc_0085E159:
    result = RtlUpcaseUnicodeChar(0, *(uint16_t *)((uint32_t)((uint32_t)(result))), v_stack_p18, *(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + 0x48));
    goto loc_0085DC43;
loc_0085E169:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), *(uint16_t *)((uint32_t)((uint32_t)(result))), v_stack_p18, *(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) + 0x8) + 0x48));
    goto loc_0085DD4F;
loc_0085E179:
    if ((uint32_t)((uint32_t)(result)) != 0) goto loc_0085E1DD;
    Arg4 = ((uint32_t)((uint32_t)(*(uint16_t *)((uint16_t)((uint16_t)(result)) + 0x48)))) >> (1);
    Arg2 = (*(uint16_t *)((uint32_t)(v_stack_m5C))) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)((uint32_t)(v_stack_m5C) + 0x8), Arg2, v_stack_p18, Arg4);
    local_rsi = 0;
    goto loc_0085E137;
loc_0085E1A4:
    if ((uint32_t)((uint32_t)(result)) != 0) goto loc_0085E259;
    Arg4 = ((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(v_stack_m5C) + 0x8) + 0x48)))) >> (1);
    Arg2 = (*(uint16_t *)((uint32_t)(v_stack_m5C))) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)((uint32_t)(v_stack_m5C) + 0x8), Arg2, v_stack_p18, Arg4);
    local_rsi = 0;
    goto loc_0085E152;
loc_0085E1D6:
    goto loc_0085DEA5;
loc_0085E1DD:
    local_rsi = (uint16_t)((local_rsi) >> (1));
loc_0085E1E8:
    if ((uint16_t)(local_rsi) == 0) goto loc_0085E061;
    if ((uint16_t)(*(uint16_t *)(0)) == 0) goto loc_0085E061;
    local_r12 = (v_stack_p18) + (2);
    local_r15 = (*(uint64_t *)(0 + 0x8)) + 1;
    if (((uint16_t)(*(uint16_t *)(v_stack_p18))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(0 + 0x8))))) goto loc_0085E24B;
    if (((uint16_t)(*(uint16_t *)(v_stack_p18))) < 97) goto loc_0085E2D4;
    if (((uint16_t)(*(uint16_t *)(v_stack_p18))) > 122) goto loc_0085E2C9;
    local_rbx = (uint16_t)((*(uint16_t *)(v_stack_p18)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085E22C:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(0 + 0x8)))) < 97) goto loc_0085E23D;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(0 + 0x8)))) > 122) goto loc_0085E2FD;
    local_rdi = (uint16_t)((*(uint8_t *)(*(uint64_t *)(0 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085E23D:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rdi))));
    if (condition_is_not_equal) goto loc_0085E06A;
loc_0085E24B:
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(0)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_0085E1E8;
loc_0085E259:
    local_rsi = (uint16_t)((local_rsi) >> (1));
loc_0085E264:
    if ((uint16_t)(local_rsi) == 0) goto loc_0085E091;
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_0085E091;
    local_r12 = (local_r12) + (2);
    local_r15 = (*(uint64_t *)(local_rbx + 0x8)) + 1;
    if (((uint16_t)(*(uint16_t *)(local_r12))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(local_rbx + 0x8))))) goto loc_0085E2BB;
    if (((uint16_t)(*(uint16_t *)(local_r12))) < 97) goto loc_0085E2E9;
    if (((uint16_t)(*(uint16_t *)(local_r12))) > 122) goto loc_0085E2DE;
    local_rbx = (uint16_t)((*(uint16_t *)(local_r12)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085E2A0:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbx + 0x8)))) < 97) goto loc_0085E2AD;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbx + 0x8)))) > 122) goto loc_0085E2F0;
    local_rdi = (uint16_t)((*(uint8_t *)(*(uint64_t *)(local_rbx + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085E2AD:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rdi))));
    if (condition_is_not_equal) goto loc_0085E09A;
loc_0085E2BB:
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(local_rbx)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_0085E264;
loc_0085E2C9:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rbx), Arg2, v_stack_p18, Arg4);
loc_0085E2D4:
    goto loc_0085E22C;
loc_0085E2DE:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), Arg2, v_stack_p18, Arg4);
loc_0085E2E9:
    goto loc_0085E2A0;
loc_0085E2F0:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rdi), Arg2, v_stack_p18, Arg4);
    goto loc_0085E2AD;
loc_0085E2FD:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), Arg2, v_stack_p18, Arg4);
    goto loc_0085E23D;
loc_0085E30D:
    goto loc_0085DA2C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085D890&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
