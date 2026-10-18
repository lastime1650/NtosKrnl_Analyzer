# CmpUndoDeleteKeyForTrans

- RVA: `0x0094A728`–`0x0094AC62` (길이 `1,338` bytes)
- VA: `0x000000014094A728`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00090E40`
- 디코드: `323`개 명령, `1,338/1,338` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0094A826` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0094A84D` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0094A868` → [CmpAllocateUnitOfWork](../84/CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x0094A883` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x0094A890` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x0094A8AA` → [CmpLockIXLockIntent](../84/CmpLockIXLockIntent_function_00844C08.md) (function, `0x00844C08`)
- `0x0094A8C8` → [CmpLockIXLockExclusive](../84/CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x0094A907` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0094A90F` → [CmpAllocateUnitOfWork](../84/CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x0094A923` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x0094A92E` → [CmLockHiveSecurityExclusive](../84/CmLockHiveSecurityExclusive_function_0084B1A8.md) (function, `0x0084B1A8`)
- `0x0094A939` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x0094A945` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x0094A961` → [CmpLockIXLockExclusive](../84/CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x0094A97E` → [CmpLockIXLockExclusive](../84/CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x0094A9BB` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0094A9EA` → [CmpGetSecurityDescriptorNodeEx](CmpGetSecurityDescriptorNodeEx_function_00949268.md) (function, `0x00949268`)
- `0x0094AA03` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x0094AA97` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0094AA9F` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x0094AAE1` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0094AAEB` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0094AB10` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0094AB37` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0094AB41` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0094AB50` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0094AB5A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0094AB64` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0094ABB2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0094ABCA` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x0094ABE1` → [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) (function, `0x004A672C`)
- `0x0094ABEE` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0094ABFB` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x0094AC08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0094AC44` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [CmpCreateChild](CmpCreateChild_function_0094817C.md) at `0x00948F59`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x0094A826` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0094A883` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x0094A890` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x0094A939` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x0094A945` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x0094AA03` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
  - `0x0094AA9F` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x0094ABB2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0094ABE1` → [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) (`PAGE` → `.text`)
  - `0x0094AC08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0094AC14` → [sub_00B25F08 + 0x24](../B2/Unknown_function_00B25F08.md) (`tail-transfer`)
  - `0x0094AC1F` → [sub_00B25F08 + 0x24](../B2/Unknown_function_00B25F08.md) (`tail-transfer`)
  - `0x0094AC2B` → [sub_00B25F08](../B2/Unknown_function_00B25F08.md) (`tail-transfer`)
  - `0x0094AC3E` → [sub_00B25F08 + 0x37](../B2/Unknown_function_00B25F08.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0094A728  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0094A72D  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0094A732  55                              push rbp
0094A733  53                              push rbx
0094A734  56                              push rsi
0094A735  57                              push rdi
0094A736  41 54                           push r12
0094A738  41 55                           push r13
0094A73A  41 56                           push r14
0094A73C  41 57                           push r15
0094A73E  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
0094A743  48 81 EC 88 00 00 00            sub rsp, 0x88
0094A74A  45 33 ED                        xor r13d, r13d
0094A74D  41 83 CA FF                     or r10d, 0xffffffff
0094A751  41 8B C2                        mov eax, r10d
0094A754  44 89 55 DF                     mov dword ptr [rbp - 0x21], r10d
0094A758  48 8B F1                        mov rsi, rcx
0094A75B  89 45 DB                        mov dword ptr [rbp - 0x25], eax
0094A75E  48 8B 49 48                     mov rcx, qword ptr [rcx + 0x48]
0094A762  4C 8B CA                        mov r9, rdx
0094A765  89 45 67                        mov dword ptr [rbp + 0x67], eax
0094A768  45 8B E5                        mov r12d, r13d
0094A76B  41 8B C5                        mov eax, r13d
0094A76E  44 89 6D E3                     mov dword ptr [rbp - 0x1d], r13d
0094A772  4C 89 6D F7                     mov qword ptr [rbp - 9], r13
0094A776  48 81 C1 D0 00 00 00            add rcx, 0xd0
0094A77D  44 89 55 EF                     mov dword ptr [rbp - 0x11], r10d
0094A781  44 89 6D F3                     mov dword ptr [rbp - 0xd], r13d
0094A785  44 89 6D D7                     mov dword ptr [rbp - 0x29], r13d
0094A789  48 85 C0                        test rax, rax
0094A78C  75 04                           jne 0x14094a792
0094A78E  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0094A792  48 3B C8                        cmp rcx, rax
0094A795  0F 84 BD 04 00 00               je 0x14094ac58
0094A79B  48 8D 50 E0                     lea rdx, [rax - 0x20]
0094A79F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0094A7A3  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
0094A7A7  48 85 D2                        test rdx, rdx
0094A7AA  0F 84 A8 04 00 00               je 0x14094ac58
0094A7B0  83 7A 44 03                     cmp dword ptr [rdx + 0x44], 3
0094A7B4  75 D3                           jne 0x14094a789
0094A7B6  48 39 72 58                     cmp qword ptr [rdx + 0x58], rsi
0094A7BA  75 CD                           jne 0x14094a789
0094A7BC  48 8D 96 D0 00 00 00            lea rdx, [rsi + 0xd0]
0094A7C3  4D 8B C5                        mov r8, r13
0094A7C6  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
0094A7CA  48 3B D1                        cmp rdx, rcx
0094A7CD  48 8D 41 E0                     lea rax, [rcx - 0x20]
0094A7D1  4C 0F 45 C0                     cmovne r8, rax
0094A7D5  4C 89 45 07                     mov qword ptr [rbp + 7], r8
0094A7D9  4D 85 C0                        test r8, r8
0094A7DC  0F 84 76 04 00 00               je 0x14094ac58
0094A7E2  41 83 78 44 02                  cmp dword ptr [r8 + 0x44], 2
0094A7E7  0F 85 6B 04 00 00               jne 0x14094ac58
0094A7ED  4C 8D 7E 20                     lea r15, [rsi + 0x20]
0094A7F1  4C 39 8E 20 01 00 00            cmp qword ptr [rsi + 0x120], r9
0094A7F8  0F 85 F7 02 00 00               jne 0x14094aaf5
0094A7FE  8B BE 18 01 00 00               mov edi, dword ptr [rsi + 0x118]
0094A804  8B 9E 1C 01 00 00               mov ebx, dword ptr [rsi + 0x11c]
0094A80A  89 7D 7F                        mov dword ptr [rbp + 0x7f], edi
0094A80D  85 FF                           test edi, edi
0094A80F  0F 84 FA 00 00 00               je 0x14094a90f
0094A815  8B D7                           mov edx, edi
0094A817  B9 00 01 00 00                  mov ecx, 0x100
0094A81C  48 C1 E2 03                     shl rdx, 3
0094A820  41 B8 43 4D 34 37               mov r8d, 0x37344d43
0094A826  E8 C5 78 23 00                  call 0x140b820f0
0094A82B  4C 8B E0                        mov r12, rax
0094A82E  48 85 C0                        test rax, rax
0094A831  0F 84 17 04 00 00               je 0x14094ac4e
0094A837  49 8B 0F                        mov rcx, qword ptr [r15]
0094A83A  4C 8D 45 DF                     lea r8, [rbp - 0x21]
0094A83E  8B D3                           mov edx, ebx
0094A840  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0094A847  0F 84 94 02 00 00               je 0x14094aae1
0094A84D  E8 0E A4 F0 FF                  call 0x140854c60
0094A852  48 8B F8                        mov rdi, rax
0094A855  48 85 C0                        test rax, rax
0094A858  0F 84 10 03 00 00               je 0x14094ab6e
0094A85E  44 3B 6D 7F                     cmp r13d, dword ptr [rbp + 0x7f]
0094A862  0F 83 8B 00 00 00               jae 0x14094a8f3
0094A868  E8 43 A3 EF FF                  call 0x140844bb0
0094A86D  45 8B F5                        mov r14d, r13d
0094A870  4B 89 04 F4                     mov qword ptr [r12 + r14*8], rax
0094A874  48 85 C0                        test rax, rax
0094A877  0F 84 F1 02 00 00               je 0x14094ab6e
0094A87D  48 8B D6                        mov rdx, rsi
0094A880  48 8B C8                        mov rcx, rax
0094A883  E8 0C 48 B4 FF                  call 0x14048f094
0094A888  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
0094A88C  4B 8B 0C F4                     mov rcx, qword ptr [r12 + r14*8]
0094A890  E8 9B 0A B4 FF                  call 0x14048b330
0094A895  8B D8                           mov ebx, eax
0094A897  85 C0                           test eax, eax
0094A899  0F 88 7B 03 00 00               js 0x14094ac1a
0094A89F  4B 8B 14 F4                     mov rdx, qword ptr [r12 + r14*8]
0094A8A3  48 8D 8E F8 00 00 00            lea rcx, [rsi + 0xf8]
0094A8AA  E8 59 A3 EF FF                  call 0x140844c08
0094A8AF  84 C0                           test al, al
0094A8B1  0F 84 C1 02 00 00               je 0x14094ab78
0094A8B7  4B 8B 14 F4                     mov rdx, qword ptr [r12 + r14*8]
0094A8BB  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
0094A8C2  41 B8 01 00 00 00               mov r8d, 1
0094A8C8  E8 E7 A3 EF FF                  call 0x140844cb4
0094A8CD  84 C0                           test al, al
0094A8CF  0F 84 A3 02 00 00               je 0x14094ab78
0094A8D5  4B 8B 04 F4                     mov rax, qword ptr [r12 + r14*8]
0094A8D9  41 FF C5                        inc r13d
0094A8DC  C7 40 44 06 00 00 00            mov dword ptr [rax + 0x44], 6
0094A8E3  4B 8B 0C F4                     mov rcx, qword ptr [r12 + r14*8]
0094A8E7  42 8B 04 B7                     mov eax, dword ptr [rdi + r14*4]
0094A8EB  89 41 58                        mov dword ptr [rcx + 0x58], eax
0094A8EE  E9 6B FF FF FF                  jmp 0x14094a85e
0094A8F3  49 8B 0F                        mov rcx, qword ptr [r15]
0094A8F6  48 8D 55 DF                     lea rdx, [rbp - 0x21]
0094A8FA  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0094A901  0F 85 49 02 00 00               jne 0x14094ab50
0094A907  E8 34 B6 F0 FF                  call 0x140855f40
0094A90C  45 33 ED                        xor r13d, r13d
0094A90F  E8 9C A2 EF FF                  call 0x140844bb0
0094A914  4C 8B F0                        mov r14, rax
0094A917  48 85 C0                        test rax, rax
0094A91A  0F 84 62 02 00 00               je 0x14094ab82
0094A920  49 8B 0F                        mov rcx, qword ptr [r15]
0094A923  E8 34 50 F0 FF                  call 0x14084f95c
0094A928  49 8B 0F                        mov rcx, qword ptr [r15]
0094A92B  41 B5 01                        mov r13b, 1
0094A92E  E8 75 08 F0 FF                  call 0x14084b1a8
0094A933  48 8B D6                        mov rdx, rsi
0094A936  49 8B CE                        mov rcx, r14
0094A939  E8 56 47 B4 FF                  call 0x14048f094
0094A93E  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
0094A942  49 8B CE                        mov rcx, r14
0094A945  E8 E6 09 B4 FF                  call 0x14048b330
0094A94A  8B D8                           mov ebx, eax
0094A94C  85 C0                           test eax, eax
0094A94E  0F 88 F4 01 00 00               js 0x14094ab48
0094A954  48 8D 8E F8 00 00 00            lea rcx, [rsi + 0xf8]
0094A95B  45 33 C0                        xor r8d, r8d
0094A95E  49 8B D6                        mov rdx, r14
0094A961  E8 4E A3 EF FF                  call 0x140844cb4
0094A966  84 C0                           test al, al
0094A968  0F 84 21 02 00 00               je 0x14094ab8f
0094A96E  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
0094A975  41 B8 01 00 00 00               mov r8d, 1
0094A97B  49 8B D6                        mov rdx, r14
0094A97E  E8 31 A3 EF FF                  call 0x140844cb4
0094A983  84 C0                           test al, al
0094A985  0F 84 04 02 00 00               je 0x14094ab8f
0094A98B  49 83 66 58 00                  and qword ptr [r14 + 0x58], 0
0094A990  4C 8D 45 EF                     lea r8, [rbp - 0x11]
0094A994  41 C7 46 44 09 00 00 00         mov dword ptr [r14 + 0x44], 9
0094A99C  83 CF FF                        or edi, 0xffffffff
0094A99F  41 89 7E 60                     mov dword ptr [r14 + 0x60], edi
0094A9A3  41 C6 46 64 00                  mov byte ptr [r14 + 0x64], 0
0094A9A8  49 8B 0F                        mov rcx, qword ptr [r15]
0094A9AB  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
0094A9AE  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
0094A9B5  0F 84 30 01 00 00               je 0x14094aaeb
0094A9BB  E8 A0 A2 F0 FF                  call 0x140854c60
0094A9C0  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
0094A9C3  48 8D 4D 67                     lea rcx, [rbp + 0x67]
0094A9C7  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0094A9CC  41 B9 01 00 00 00               mov r9d, 1
0094A9D2  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0094A9D6  4C 8B C0                        mov r8, rax
0094A9D9  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
0094A9DE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0094A9E3  49 8B 0F                        mov rcx, qword ptr [r15]
0094A9E6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0094A9EA  E8 79 E8 FF FF                  call 0x140949268
0094A9EF  8B D8                           mov ebx, eax
0094A9F1  85 C0                           test eax, eax
0094A9F3  0F 88 DB 01 00 00               js 0x14094abd4
0094A9F9  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
0094A9FC  4C 8D 45 D7                     lea r8, [rbp - 0x29]
0094AA00  49 8B 0F                        mov rcx, qword ptr [r15]
0094AA03  E8 58 D6 AD FF                  call 0x140428060
0094AA08  84 C0                           test al, al
0094AA0A  0F 84 8B 01 00 00               je 0x14094ab9b
0094AA10  49 8B 07                        mov rax, qword ptr [r15]
0094AA13  8B 55 D7                        mov edx, dword ptr [rbp - 0x29]
0094AA16  48 03 D2                        add rdx, rdx
0094AA19  48 8B 88 60 07 00 00            mov rcx, qword ptr [rax + 0x760]
0094AA20  48 8B 44 D1 08                  mov rax, qword ptr [rcx + rdx*8 + 8]
0094AA25  49 89 46 58                     mov qword ptr [r14 + 0x58], rax
0094AA29  8B 00                           mov eax, dword ptr [rax]
0094AA2B  41 89 46 60                     mov dword ptr [r14 + 0x60], eax
0094AA2F  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
0094AA33  45 88 6E 64                     mov byte ptr [r14 + 0x64], r13b
0094AA37  45 33 F6                        xor r14d, r14d
0094AA3A  C7 40 44 0D 00 00 00            mov dword ptr [rax + 0x44], 0xd
0094AA41  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
0094AA45  C7 40 44 0F 00 00 00            mov dword ptr [rax + 0x44], 0xf
0094AA4C  4C 39 B6 20 01 00 00            cmp qword ptr [rsi + 0x120], r14
0094AA53  0F 85 5F 01 00 00               jne 0x14094abb8
0094AA59  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0094AA5D  44 21 B6 18 01 00 00            and dword ptr [rsi + 0x118], r14d
0094AA64  83 8E 1C 01 00 00 FF            or dword ptr [rsi + 0x11c], 0xffffffff
0094AA6B  48 89 86 20 01 00 00            mov qword ptr [rsi + 0x120], rax
0094AA72  83 FF FF                        cmp edi, -1
0094AA75  0F 85 61 01 00 00               jne 0x14094abdc
0094AA7B  33 FF                           xor edi, edi
0094AA7D  48 39 7D F7                     cmp qword ptr [rbp - 9], rdi
0094AA81  74 19                           je 0x14094aa9c
0094AA83  49 8B 0F                        mov rcx, qword ptr [r15]
0094AA86  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0094AA8A  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
0094AA91  0F 85 C3 00 00 00               jne 0x14094ab5a
0094AA97  E8 A4 B4 F0 FF                  call 0x140855f40
0094AA9C  49 8B 0F                        mov rcx, qword ptr [r15]
0094AA9F  E8 24 EF 27 00                  call 0x140bc99c8
0094AAA4  45 84 ED                        test r13b, r13b
0094AAA7  0F 85 3E 01 00 00               jne 0x14094abeb
0094AAAD  4D 85 F6                        test r14, r14
0094AAB0  0F 85 42 01 00 00               jne 0x14094abf8
0094AAB6  8B C3                           mov eax, ebx
0094AAB8  4D 85 E4                        test r12, r12
0094AABB  0F 85 51 01 00 00               jne 0x14094ac12
0094AAC1  48 85 FF                        test rdi, rdi
0094AAC4  0F 85 66 01 00 00               jne 0x14094ac30
0094AACA  8B C3                           mov eax, ebx
0094AACC  48 81 C4 88 00 00 00            add rsp, 0x88
0094AAD3  41 5F                           pop r15
0094AAD5  41 5E                           pop r14
0094AAD7  41 5D                           pop r13
0094AAD9  41 5C                           pop r12
0094AADB  5F                              pop rdi
0094AADC  5E                              pop rsi
0094AADD  5B                              pop rbx
0094AADE  5D                              pop rbp
0094AADF  C3                              ret
0094AAE0  CC                              int3
0094AAE1  E8 CA A1 F0 FF                  call 0x140854cb0
0094AAE6  E9 67 FD FF FF                  jmp 0x14094a852
0094AAEB  E8 C0 A1 F0 FF                  call 0x140854cb0
0094AAF0  E9 CB FE FF FF                  jmp 0x14094a9c0
0094AAF5  49 8B 0F                        mov rcx, qword ptr [r15]
0094AAF8  4C 8D 45 E7                     lea r8, [rbp - 0x19]
0094AAFC  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
0094AAFF  44 89 55 E7                     mov dword ptr [rbp - 0x19], r10d
0094AB03  44 89 6D EB                     mov dword ptr [rbp - 0x15], r13d
0094AB07  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0094AB0E  74 31                           je 0x14094ab41
0094AB10  E8 4B A1 F0 FF                  call 0x140854c60
0094AB15  48 85 C0                        test rax, rax
0094AB18  0F 84 30 01 00 00               je 0x14094ac4e
0094AB1E  49 8B 0F                        mov rcx, qword ptr [r15]
0094AB21  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0094AB25  8B 78 24                        mov edi, dword ptr [rax + 0x24]
0094AB28  8B 58 28                        mov ebx, dword ptr [rax + 0x28]
0094AB2B  89 7D 7F                        mov dword ptr [rbp + 0x7f], edi
0094AB2E  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0094AB35  75 2D                           jne 0x14094ab64
0094AB37  E8 04 B4 F0 FF                  call 0x140855f40
0094AB3C  E9 CC FC FF FF                  jmp 0x14094a80d
0094AB41  E8 6A A1 F0 FF                  call 0x140854cb0
0094AB46  EB CD                           jmp 0x14094ab15
0094AB48  8B 7D DB                        mov edi, dword ptr [rbp - 0x25]
0094AB4B  E9 22 FF FF FF                  jmp 0x14094aa72
0094AB50  E8 CB 20 F1 FF                  call 0x14085cc20
0094AB55  E9 B2 FD FF FF                  jmp 0x14094a90c
0094AB5A  E8 C1 20 F1 FF                  call 0x14085cc20
0094AB5F  E9 38 FF FF FF                  jmp 0x14094aa9c
0094AB64  E8 B7 20 F1 FF                  call 0x14085cc20
0094AB69  E9 9F FC FF FF                  jmp 0x14094a80d
0094AB6E  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0094AB73  E9 A2 00 00 00                  jmp 0x14094ac1a
0094AB78  BB 01 00 19 C0                  mov ebx, 0xc0190001
0094AB7D  E9 98 00 00 00                  jmp 0x14094ac1a
0094AB82  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0094AB87  49 8B FD                        mov rdi, r13
0094AB8A  E9 27 FF FF FF                  jmp 0x14094aab6
0094AB8F  BB 01 00 19 C0                  mov ebx, 0xc0190001
0094AB94  33 FF                           xor edi, edi
0094AB96  E9 01 FF FF FF                  jmp 0x14094aa9c
0094AB9B  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0094AB9E  BA 04 00 00 00                  mov edx, 4
0094ABA3  4C 8B CE                        mov r9, rsi
0094ABA6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0094ABAB  8D 4A 4D                        lea ecx, [rdx + 0x4d]
0094ABAE  44 8D 42 FF                     lea r8d, [rdx - 1]
0094ABB2  E8 A9 2A BB FF                  call 0x1404fd660
0094ABB7  CC                              int3
0094ABB8  8B 96 1C 01 00 00               mov edx, dword ptr [rsi + 0x11c]
0094ABBE  83 FA FF                        cmp edx, -1
0094ABC1  0F 84 92 FE FF FF               je 0x14094aa59
0094ABC7  49 8B 0F                        mov rcx, qword ptr [r15]
0094ABCA  E8 5D FB F0 FF                  call 0x14085a72c
0094ABCF  E9 85 FE FF FF                  jmp 0x14094aa59
0094ABD4  8B 7D 67                        mov edi, dword ptr [rbp + 0x67]
0094ABD7  E9 96 FE FF FF                  jmp 0x14094aa72
0094ABDC  49 8B 0F                        mov rcx, qword ptr [r15]
0094ABDF  8B D7                           mov edx, edi
0094ABE1  E8 46 BB B5 FF                  call 0x1404a672c
0094ABE6  E9 90 FE FF FF                  jmp 0x14094aa7b
0094ABEB  49 8B 0F                        mov rcx, qword ptr [r15]
0094ABEE  E8 45 DB EF FF                  call 0x140848738
0094ABF3  E9 B5 FE FF FF                  jmp 0x14094aaad
0094ABF8  49 8B CE                        mov rcx, r14
0094ABFB  E8 7C 9D F2 FF                  call 0x14087497c
0094AC00  BA 43 4D 55 77                  mov edx, 0x77554d43
0094AC05  49 8B CE                        mov rcx, r14
0094AC08  E8 63 7C 23 00                  call 0x140b82870
0094AC0D  E9 A4 FE FF FF                  jmp 0x14094aab6
0094AC12  85 C0                           test eax, eax
0094AC14  0F 89 12 B3 1D 00               jns 0x140b25f2c
0094AC1A  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0094AC1D  85 C0                           test eax, eax
0094AC1F  0F 84 07 B3 1D 00               je 0x140b25f2c
0094AC25  49 8B F4                        mov rsi, r12
0094AC28  44 8B F0                        mov r14d, eax
0094AC2B  E9 D8 B2 1D 00                  jmp 0x140b25f08
0094AC30  49 8B 0F                        mov rcx, qword ptr [r15]
0094AC33  48 8D 55 DF                     lea rdx, [rbp - 0x21]
0094AC37  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0094AC3E  0F 84 FB B2 1D 00               je 0x140b25f3f
0094AC44  E8 D7 1F F1 FF                  call 0x14085cc20
0094AC49  E9 7C FE FF FF                  jmp 0x14094aaca
0094AC4E  B8 9A 00 00 C0                  mov eax, 0xc000009a
0094AC53  E9 74 FE FF FF                  jmp 0x14094aacc
0094AC58  B8 34 00 00 C0                  mov eax, 0xc0000034
0094AC5D  E9 6A FE FF FF                  jmp 0x14094aacc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpUndoDeleteKeyForTrans(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int8 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (136);
    v_r13 = 0;
    v_r10 = (unsigned int)((v_r10) | (0xFFFFFFFFULL));
    v_stack_m80 = (unsigned int)(v_r10);
    v_stack_m84 = (unsigned int)((unsigned int)((unsigned int)(v_r10)));
    v_stack_p8 = (unsigned int)((unsigned int)((unsigned int)(v_r10)));
    v_stack_m7C = 0;
    v_stack_m68 = 0;
    a1 = (*(unsigned __int64 *)(a1 + 72)) + (208);
    v_stack_m70 = (unsigned int)(v_r10);
    v_stack_m6C = 0;
    v_stack_m88 = 0;
loc_0094A789:
    result = 0;
    if (0 == 0) {
        result = *(unsigned __int64 *)(a1 + 8);
    }
    if (a1 == result) goto loc_0094AC58;
    v_stack_m60 = result - 32;
    if (result - 32 == 0) goto loc_0094AC58;
    if ((*(unsigned int *)(result - 32 + 68)) != 3) goto loc_0094A789;
    if ((*(unsigned __int64 *)(result - 32 + 88)) != a1) goto loc_0094A789;
    a3 = 0;
    if ((a1 + 208) != (*(unsigned __int64 *)(a1 + 208 + 8))) { a3 = *(unsigned __int64 *)(a1 + 208 + 8) - 32; }
    v_stack_m58 = a3;
    if (a3 == 0) goto loc_0094AC58;
    if ((*(unsigned int *)(a3 + 68)) != 2) goto loc_0094AC58;
    if ((*(unsigned __int64 *)(a1 + 288)) != a2) goto loc_0094AAF5;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 280)));
loc_0094A80D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 280))) == 0) goto loc_0094A90F;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 280))))) << (3);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x37344D43ULL), a2);
    if (result == 0) goto loc_0094AC4E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_0094AAE1;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 284)))), v_stack_m80, a2);
loc_0094A852:
    if (result == 0) goto loc_0094AB6E;
loc_0094A85E:
    if (0 >= v_stack_p20) goto loc_0094A8F3;
    result = CmpAllocateUnitOfWork(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 284)))), v_stack_m80, a2);
    *(unsigned __int64 *)(result + 0 * 8) = result;
    if (result == 0) goto loc_0094AB6E;
    result = CmpTransEnlistUowInKcb(result, a1, v_stack_m80, a2);
    result = CmpTransEnlistUowInCmTrans(*(unsigned __int64 *)(result + 0 * 8), v_stack_p10, v_stack_m80, a2);
    if (sign_flag) goto loc_0094AC1A;
    result = CmpLockIXLockIntent(a1 + 248, *(unsigned __int64 *)(result + 0 * 8), v_stack_m80, a2);
    if ((unsigned __int8)(result) == 0) goto loc_0094AB78;
    result = CmpLockIXLockExclusive(a1 + 264, *(unsigned __int64 *)(result + 0 * 8), 1, a2);
    if ((unsigned __int8)(result) == 0) goto loc_0094AB78;
    v_r13 = (unsigned int)((v_r13) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(result + 0 * 8) + 68) = 6;
    *(unsigned int *)(*(unsigned __int64 *)(result + 0 * 8) + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 0 * 4)));
    goto loc_0094A85E;
loc_0094A8F3:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_0094AB50;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m80, 1, a2);
loc_0094A90C:
    v_r13 = 0;
loc_0094A90F:
    result = CmpAllocateUnitOfWork(*(unsigned __int64 *)(a1 + 32), v_stack_m80, 1, a2);
    if (result == 0) goto loc_0094AB82;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(a1 + 32), v_stack_m80, 1, a2);
    result = CmLockHiveSecurityExclusive(*(unsigned __int64 *)(a1 + 32), v_stack_m80, 1, a2);
    result = CmpTransEnlistUowInKcb(result, a1, 1, a2);
    result = CmpTransEnlistUowInCmTrans(result, v_stack_p10, 1, a2);
    if (sign_flag) goto loc_0094AB48;
    a3 = 0;
    result = CmpLockIXLockExclusive(a1 + 248, result, a3, a2);
    if ((unsigned __int8)(result) == 0) goto loc_0094AB8F;
    result = CmpLockIXLockExclusive(a1 + 264, result, 1, a2);
    if ((unsigned __int8)(result) == 0) goto loc_0094AB8F;
    *(unsigned int *)(result + 68) = 9;
    v_rdi = (unsigned int)((result) | (0xFFFFFFFFULL));
    *(unsigned int *)(result + 96) = (unsigned int)(v_rdi);
    *(unsigned __int8 *)(result + 100) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_0094AAEB;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 40)), v_stack_m70, a2);
loc_0094A9C0:
    v_stack_m98 = v_stack_p8;
    v_stack_mA0 = 1;
    v_stack_mA8 = v_stack_p18;
    v_stack_m68 = result;
    result = CmpGetSecurityDescriptorNodeEx(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 40)), result, 1);
    if (sign_flag) goto loc_0094ABD4;
    result = CmpFindSecurityCellCacheIndex(*(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_p8), v_stack_m88, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0094AB9B;
    a2 = ((unsigned int)(v_stack_m88)) + ((unsigned int)(v_stack_m88));
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1888) + a2 * 8 + 8);
    *(unsigned int *)(result + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1888) + a2 * 8 + 8))));
    *(unsigned __int8 *)(result + 100) = 1;
    v_r14 = 0;
    *(unsigned int *)(v_stack_m60 + 68) = 13;
    *(unsigned int *)(v_stack_m58 + 68) = 15;
    if ((*(unsigned __int64 *)(a1 + 288)) != 0) goto loc_0094ABB8;
loc_0094AA59:
    *(unsigned __int64 *)(a1 + 288) = v_stack_p10;
loc_0094AA72:
    if (((unsigned int)(v_rdi)) != -1) goto loc_0094ABDC;
loc_0094AA7B:
    v_rdi = 0;
    if (v_stack_m68 == 0) goto loc_0094AA9C;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_0094AB5A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m70, v_stack_m88, 1);
loc_0094AA9C:
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(a1 + 32), v_stack_m70, v_stack_m88, 1);
    if (1 != 0) goto loc_0094ABEB;
loc_0094AAAD:
    if (0 != 0) goto loc_0094ABF8;
loc_0094AAB6:
    if (result != 0) goto loc_0094AC12;
    if (0 != 0) goto loc_0094AC30;
loc_0094AACA:
loc_0094AACC:
    v_rsp = (v_rsp) + (136);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0094AAE1:
    result = HvpGetCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m70, v_stack_m88, 1);
    goto loc_0094A852;
loc_0094AAEB:
    result = HvpGetCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m70, v_stack_m88, 1);
    goto loc_0094A9C0;
loc_0094AAF5:
    v_stack_m78 = (unsigned int)(v_r10);
    v_stack_m74 = 1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_0094AB41;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 40)), v_stack_m78, 1);
loc_0094AB15:
    if (result == 0) goto loc_0094AC4E;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_0094AB64;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m78, v_stack_m78, 1);
    goto loc_0094A80D;
loc_0094AB41:
    result = HvpGetCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m78, v_stack_m78, 1);
    goto loc_0094AB15;
loc_0094AB48:
    goto loc_0094AA72;
loc_0094AB50:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), v_stack_m78, v_stack_m78, 1);
    goto loc_0094A90C;
loc_0094AB5A:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), v_stack_m78, v_stack_m78, 1);
    goto loc_0094AA9C;
loc_0094AB64:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), v_stack_m78, v_stack_m78, 1);
    goto loc_0094A80D;
loc_0094AB6E:
    goto loc_0094AC1A;
loc_0094AB78:
    goto loc_0094AC1A;
loc_0094AB82:
    goto loc_0094AAB6;
loc_0094AB8F:
    v_rdi = 0;
    goto loc_0094AA9C;
loc_0094AB9B:
    v_stack_p20 = (unsigned int)(v_stack_p8);
    result = KeBugCheckEx(4 + 77, 4, 4 - 1, a1);
loc_0094ABB8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 284)))) == -1) goto loc_0094AA59;
    result = HvFreeCell(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 284)), 4 - 1, a1);
    goto loc_0094AA59;
loc_0094ABD4:
    goto loc_0094AA72;
loc_0094ABDC:
    result = CmpDereferenceSecurityNode(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), 4 - 1, a1);
    goto loc_0094AA7B;
loc_0094ABEB:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), 4 - 1, a1);
    goto loc_0094AAAD;
loc_0094ABF8:
    result = CmpRundownUnitOfWork(0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), 4 - 1, a1);
    result = ExFreePoolWithTag(0, (unsigned int)(0x77554D43ULL), 4 - 1, a1);
    goto loc_0094AAB6;
loc_0094AC12:
loc_0094AC1A:
loc_0094AC30:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), v_stack_m80, 4 - 1, a1);
    goto loc_0094AACA;
loc_0094AC4E:
    goto loc_0094AACC;
loc_0094AC58:
    goto loc_0094AACC;
}
```

## 5. (Beta) C Style

```c
int64_t CmpUndoDeleteKeyForTrans(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m98;
    uint8_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (136);
    local_r13 = 0;
    local_r10 = (uint32_t)((local_r10) | (0xFFFFFFFFULL));
    v_stack_m80 = (uint32_t)(local_r10);
    v_stack_m84 = (uint32_t)((uint32_t)((uint32_t)(local_r10)));
    v_stack_p8 = (uint32_t)((uint32_t)((uint32_t)(local_r10)));
    v_stack_m7C = 0;
    v_stack_m68 = 0;
    Arg1 = (*(uint64_t *)(arg1 + 0x48)) + (208);
    v_stack_m70 = (uint32_t)(local_r10);
    v_stack_m6C = 0;
    v_stack_m88 = 0;
loc_0094A789:
    result = 0;
    if (0 == 0) {
        result = *(uint64_t *)(arg1 + 0x8);
    }
    if (Arg1 == result) goto loc_0094AC58;
    v_stack_m60 = result - 32;
    if (result - 32 == 0) goto loc_0094AC58;
    if ((*(uint32_t *)(result - 0x20 + 0x44)) != 3) goto loc_0094A789;
    if ((*(uint64_t *)(result - 0x20 + 0x58)) != Arg1) goto loc_0094A789;
    Arg3 = 0;
    if ((Arg1 + 208) != (*(uint64_t *)(arg1 + 0xD0 + 0x8))) { Arg3 = *(uint64_t *)(arg1 + 0xD0 + 0x8) - 32; }
    v_stack_m58 = Arg3;
    if (Arg3 == 0) goto loc_0094AC58;
    if ((*(uint32_t *)(Arg3 + 0x44)) != 2) goto loc_0094AC58;
    if ((*(uint64_t *)(arg1 + 0x120)) != Arg2) goto loc_0094AAF5;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x118)));
loc_0094A80D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x118))) == 0) goto loc_0094A90F;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x118))))) << (3);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x37344D43ULL), Arg2);
    if (result == 0) goto loc_0094AC4E;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_0094AAE1;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x11C)))), v_stack_m80, Arg2);
loc_0094A852:
    if (result == 0) goto loc_0094AB6E;
loc_0094A85E:
    if (0 >= v_stack_p20) goto loc_0094A8F3;
    result = CmpAllocateUnitOfWork(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x11C)))), v_stack_m80, Arg2);
    *(uint64_t *)(result + 0x0 * 8) = result;
    if (result == 0) goto loc_0094AB6E;
    result = CmpTransEnlistUowInKcb(result, Arg1, v_stack_m80, Arg2);
    result = CmpTransEnlistUowInCmTrans(*(uint64_t *)(result + 0x0 * 8), v_stack_p10, v_stack_m80, Arg2);
    if (sign_flag) goto loc_0094AC1A;
    result = CmpLockIXLockIntent(Arg1 + 248, *(uint64_t *)(result + 0x0 * 8), v_stack_m80, Arg2);
    if ((uint8_t)(result) == 0) goto loc_0094AB78;
    result = CmpLockIXLockExclusive(Arg1 + 264, *(uint64_t *)(result + 0x0 * 8), 1, Arg2);
    if ((uint8_t)(result) == 0) goto loc_0094AB78;
    local_r13 = (uint32_t)((local_r13) + 1);
    *(uint32_t *)(*(uint64_t *)(result + 0x0 * 8) + 0x44) = 6;
    *(uint32_t *)(*(uint64_t *)(result + 0x0 * 8) + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 * 4)));
    goto loc_0094A85E;
loc_0094A8F3:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0094AB50;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m80, 1, Arg2);
loc_0094A90C:
    local_r13 = 0;
loc_0094A90F:
    result = CmpAllocateUnitOfWork(*(uint64_t *)(arg1 + 0x20), v_stack_m80, 1, Arg2);
    if (result == 0) goto loc_0094AB82;
    result = HvLockHiveFlusherShared(*(uint64_t *)(arg1 + 0x20), v_stack_m80, 1, Arg2);
    result = CmLockHiveSecurityExclusive(*(uint64_t *)(arg1 + 0x20), v_stack_m80, 1, Arg2);
    result = CmpTransEnlistUowInKcb(result, Arg1, 1, Arg2);
    result = CmpTransEnlistUowInCmTrans(result, v_stack_p10, 1, Arg2);
    if (sign_flag) goto loc_0094AB48;
    Arg3 = 0;
    result = CmpLockIXLockExclusive(Arg1 + 248, result, Arg3, Arg2);
    if ((uint8_t)(result) == 0) goto loc_0094AB8F;
    result = CmpLockIXLockExclusive(Arg1 + 264, result, 1, Arg2);
    if ((uint8_t)(result) == 0) goto loc_0094AB8F;
    *(uint32_t *)(result + 0x44) = 9;
    local_rdi = (uint32_t)((result) | (0xFFFFFFFFULL));
    *(uint32_t *)(result + 0x60) = (uint32_t)(local_rdi);
    *(uint8_t *)(result + 0x64) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_0094AAEB;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), v_stack_m70, Arg2);
loc_0094A9C0:
    v_stack_m98 = v_stack_p8;
    v_stack_mA0 = 1;
    v_stack_mA8 = v_stack_p18;
    v_stack_m68 = result;
    result = CmpGetSecurityDescriptorNodeEx(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), result, 1);
    if (sign_flag) goto loc_0094ABD4;
    result = CmpFindSecurityCellCacheIndex(*(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_p8), v_stack_m88, 1);
    if ((uint8_t)(result) == 0) goto loc_0094AB9B;
    Arg2 = ((uint32_t)(v_stack_m88)) + ((uint32_t)(v_stack_m88));
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x760) + Arg2 * 8 + 0x8);
    *(uint32_t *)(result + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x760) + Arg2 * 8 + 0x8))));
    *(uint8_t *)(result + 0x64) = 1;
    local_r14 = 0;
    *(uint32_t *)(v_stack_m60 + 0x44) = 13;
    *(uint32_t *)(v_stack_m58 + 0x44) = 15;
    if ((*(uint64_t *)(arg1 + 0x120)) != 0) goto loc_0094ABB8;
loc_0094AA59:
    *(uint64_t *)(arg1 + 0x120) = v_stack_p10;
loc_0094AA72:
    if (((uint32_t)(local_rdi)) != -1) goto loc_0094ABDC;
loc_0094AA7B:
    local_rdi = 0;
    if (v_stack_m68 == 0) goto loc_0094AA9C;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0094AB5A;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m70, v_stack_m88, 1);
loc_0094AA9C:
    result = CmUnlockHiveSecurity(*(uint64_t *)(arg1 + 0x20), v_stack_m70, v_stack_m88, 1);
    if (1 != 0) goto loc_0094ABEB;
loc_0094AAAD:
    if (0 != 0) goto loc_0094ABF8;
loc_0094AAB6:
    if (result != 0) goto loc_0094AC12;
    if (0 != 0) goto loc_0094AC30;
loc_0094AACA:
loc_0094AACC:
    local_rsp = (local_rsp) + (136);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0094AAE1:
    result = HvpGetCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m70, v_stack_m88, 1);
    goto loc_0094A852;
loc_0094AAEB:
    result = HvpGetCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m70, v_stack_m88, 1);
    goto loc_0094A9C0;
loc_0094AAF5:
    v_stack_m78 = (uint32_t)(local_r10);
    v_stack_m74 = 1;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_0094AB41;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), v_stack_m78, 1);
loc_0094AB15:
    if (result == 0) goto loc_0094AC4E;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0094AB64;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m78, v_stack_m78, 1);
    goto loc_0094A80D;
loc_0094AB41:
    result = HvpGetCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m78, v_stack_m78, 1);
    goto loc_0094AB15;
loc_0094AB48:
    goto loc_0094AA72;
loc_0094AB50:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), v_stack_m78, v_stack_m78, 1);
    goto loc_0094A90C;
loc_0094AB5A:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), v_stack_m78, v_stack_m78, 1);
    goto loc_0094AA9C;
loc_0094AB64:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), v_stack_m78, v_stack_m78, 1);
    goto loc_0094A80D;
loc_0094AB6E:
    goto loc_0094AC1A;
loc_0094AB78:
    goto loc_0094AC1A;
loc_0094AB82:
    goto loc_0094AAB6;
loc_0094AB8F:
    local_rdi = 0;
    goto loc_0094AA9C;
loc_0094AB9B:
    v_stack_p20 = (uint32_t)(v_stack_p8);
    result = KeBugCheckEx(4 + 77, 4, 4 - 1, Arg1);
loc_0094ABB8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x11C)))) == -1) goto loc_0094AA59;
    result = HvFreeCell(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x11C)), 4 - 1, Arg1);
    goto loc_0094AA59;
loc_0094ABD4:
    goto loc_0094AA72;
loc_0094ABDC:
    result = CmpDereferenceSecurityNode(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), 4 - 1, Arg1);
    goto loc_0094AA7B;
loc_0094ABEB:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), 4 - 1, Arg1);
    goto loc_0094AAAD;
loc_0094ABF8:
    result = CmpRundownUnitOfWork(0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), 4 - 1, Arg1);
    result = ExFreePoolWithTag(0, (uint32_t)(0x77554D43ULL), 4 - 1, Arg1);
    goto loc_0094AAB6;
loc_0094AC12:
loc_0094AC1A:
loc_0094AC30:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), v_stack_m80, 4 - 1, Arg1);
    goto loc_0094AACA;
loc_0094AC4E:
    goto loc_0094AACC;
loc_0094AC58:
    goto loc_0094AACC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0xF8` | `64` | `R` |
| `Arg1` | `+ 0x108` | `64` | `R` |
| `Arg1` | `+ 0x118` | `32` | `R` |
| `Arg1` | `+ 0x118` | `32` | `R/W` |
| `Arg1` | `+ 0x11C` | `32` | `R` |
| `Arg1` | `+ 0x11C` | `32` | `R/W` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x120` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094A728&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
