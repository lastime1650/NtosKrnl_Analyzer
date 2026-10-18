# CmpLightWeightPrepareSetValueKeyUoW

- RVA: `0x00A0EF28`–`0x00A0F3CF` (길이 `1,191` bytes)
- VA: `0x0000000140A0EF28`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8F78`
- 디코드: `306`개 명령, `1,191/1,191` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A0EFB2` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00A0EFE2` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A0F031` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00A0F05E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A0F083` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00A0F0B6` → [CmpGetValueData](../85/CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x00A0F0FB` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A0F109` → [CmpLightWeightCreateSetValueData](CmpLightWeightCreateSetValueData_function_00A0F7EC.md) (function, `0x00A0F7EC`)
- `0x00A0F123` → [CmpLightWeightUpdateSharedSetValueData](CmpLightWeightUpdateSharedSetValueData_function_00A0F93C.md) (function, `0x00A0F93C`)
- `0x00A0F130` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A0F13A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A0F149` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0F17E` → [CmpAddValueToListEx](../85/CmpAddValueToListEx_function_0085B460.md) (function, `0x0085B460`)
- `0x00A0F1C9` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A0F1DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0F1FD` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A0F210` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00A0F232` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A0F249` → [CmpMarkValueDataDirty](../84/CmpMarkValueDataDirty_function_0084B910.md) (function, `0x0084B910`)
- `0x00A0F267` → [CmpSwapValueInList](../../text/4A/CmpSwapValueInList_function_004A266C.md) (function, `0x004A266C`)
- `0x00A0F271` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00A0F278` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A0F282` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A0F2A7` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A0F2CE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0F2EA` → [CmpInitializeValueNameString](CmpInitializeValueNameString_function_00A0F644.md) (function, `0x00A0F644`)
- `0x00A0F312` → [CmpFindNameInListWithStatus](../84/CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00A0F349` → [CmpAddValueKeyNew](../85/CmpAddValueKeyNew_function_0085AA58.md) (function, `0x0085AA58`)
- `0x00A0F360` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00A0F393` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x00A0F3C5` → [CmpFreeValue](../84/CmpFreeValue_function_0084AF98.md) (function, `0x0084AF98`)

### Direct callers
- [CmpProcessLightWeightUOW](../9B/CmpProcessLightWeightUOW_function_009B0EAC.md) at `0x009B106D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00A0EFB2` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x00A0F149` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0F1DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0F267` → [CmpSwapValueInList](../../text/4A/CmpSwapValueInList_function_004A266C.md) (`PAGE` → `.text`)
  - `0x00A0F2CE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0F393` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0EF28  40 55                           push rbp
00A0EF2A  53                              push rbx
00A0EF2B  56                              push rsi
00A0EF2C  57                              push rdi
00A0EF2D  41 54                           push r12
00A0EF2F  41 55                           push r13
00A0EF31  41 56                           push r14
00A0EF33  41 57                           push r15
00A0EF35  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00A0EF3A  48 81 EC A8 00 00 00            sub rsp, 0xa8
00A0EF41  48 8B 71 68                     mov rsi, qword ptr [rcx + 0x68]
00A0EF45  33 DB                           xor ebx, ebx
00A0EF47  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00A0EF4B  41 83 CC FF                     or r12d, 0xffffffff
00A0EF4F  44 89 65 C7                     mov dword ptr [rbp - 0x39], r12d
00A0EF53  0F 57 C0                        xorps xmm0, xmm0
00A0EF56  89 5D CB                        mov dword ptr [rbp - 0x35], ebx
00A0EF59  4C 8B F1                        mov r14, rcx
00A0EF5C  44 89 65 BF                     mov dword ptr [rbp - 0x41], r12d
00A0EF60  48 8B 78 20                     mov rdi, qword ptr [rax + 0x20]
00A0EF64  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
00A0EF67  44 89 65 DF                     mov dword ptr [rbp - 0x21], r12d
00A0EF6B  89 5D E3                        mov dword ptr [rbp - 0x1d], ebx
00A0EF6E  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
00A0EF71  89 5D CF                        mov dword ptr [rbp - 0x31], ebx
00A0EF74  44 89 65 B7                     mov dword ptr [rbp - 0x49], r12d
00A0EF78  89 5D BB                        mov dword ptr [rbp - 0x45], ebx
00A0EF7B  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
00A0EF7F  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
00A0EF83  88 5D 67                        mov byte ptr [rbp + 0x67], bl
00A0EF86  44 89 65 77                     mov dword ptr [rbp + 0x77], r12d
00A0EF8A  88 5D 6F                        mov byte ptr [rbp + 0x6f], bl
00A0EF8D  48 89 5D 0F                     mov qword ptr [rbp + 0xf], rbx
00A0EF91  48 89 75 D7                     mov qword ptr [rbp - 0x29], rsi
00A0EF95  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00A0EF99  48 85 F6                        test rsi, rsi
00A0EF9C  0F 84 63 01 00 00               je 0x140a0f105
00A0EFA2  BA 10 00 00 00                  mov edx, 0x10
00A0EFA7  B9 00 01 00 00                  mov ecx, 0x100
00A0EFAC  41 B8 43 4D 55 77               mov r8d, 0x77554d43
00A0EFB2  E8 4D E5 9B FF                  call 0x1403cd504
00A0EFB7  4C 8B F8                        mov r15, rax
00A0EFBA  48 85 C0                        test rax, rax
00A0EFBD  0F 84 B9 03 00 00               je 0x140a0f37c
00A0EFC3  44 89 20                        mov dword ptr [rax], r12d
00A0EFC6  4C 8D 45 C7                     lea r8, [rbp - 0x39]
00A0EFCA  44 89 60 04                     mov dword ptr [rax + 4], r12d
00A0EFCE  48 8B CF                        mov rcx, rdi
00A0EFD1  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0EFD8  41 8B 56 5C                     mov edx, dword ptr [r14 + 0x5c]
00A0EFDC  0F 84 A1 00 00 00               je 0x140a0f083
00A0EFE2  E8 79 5C E4 FF                  call 0x140854c60
00A0EFE7  4C 8B E8                        mov r13, rax
00A0EFEA  48 85 C0                        test rax, rax
00A0EFED  0F 84 93 03 00 00               je 0x140a0f386
00A0EFF3  8B 40 04                        mov eax, dword ptr [rax + 4]
00A0EFF6  B9 00 00 00 80                  mov ecx, 0x80000000
00A0EFFB  3B C1                           cmp eax, ecx
00A0EFFD  44 8D A0 00 00 00 80            lea r12d, [rax - 0x80000000]
00A0F004  44 0F 42 E0                     cmovb r12d, eax
00A0F008  44 89 65 D7                     mov dword ptr [rbp - 0x29], r12d
00A0F00C  44 89 65 EF                     mov dword ptr [rbp - 0x11], r12d
00A0F010  45 85 E4                        test r12d, r12d
00A0F013  74 0C                           je 0x140a0f021
00A0F015  3B C1                           cmp eax, ecx
00A0F017  72 74                           jb 0x140a0f08d
00A0F019  49 8D 45 08                     lea rax, [r13 + 8]
00A0F01D  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00A0F021  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
00A0F025  45 33 C9                        xor r9d, r9d
00A0F028  45 33 C0                        xor r8d, r8d
00A0F02B  48 8B CF                        mov rcx, rdi
00A0F02E  8B 50 28                        mov edx, dword ptr [rax + 0x28]
00A0F031  E8 4A 90 E4 FF                  call 0x140858080
00A0F036  8B D8                           mov ebx, eax
00A0F038  85 C0                           test eax, eax
00A0F03A  0F 89 4C 02 00 00               jns 0x140a0f28c
00A0F040  80 7D 67 00                     cmp byte ptr [rbp + 0x67], 0
00A0F044  0F 85 8E 00 00 00               jne 0x140a0f0d8
00A0F04A  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0F051  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00A0F055  48 8B CF                        mov rcx, rdi
00A0F058  0F 85 D2 00 00 00               jne 0x140a0f130
00A0F05E  E8 DD 6E E4 FF                  call 0x140855f40
00A0F063  4D 85 FF                        test r15, r15
00A0F066  0F 85 1F 03 00 00               jne 0x140a0f38b
00A0F06C  8B C3                           mov eax, ebx
00A0F06E  48 81 C4 A8 00 00 00            add rsp, 0xa8
00A0F075  41 5F                           pop r15
00A0F077  41 5E                           pop r14
00A0F079  41 5D                           pop r13
00A0F07B  41 5C                           pop r12
00A0F07D  5F                              pop rdi
00A0F07E  5E                              pop rsi
00A0F07F  5B                              pop rbx
00A0F080  5D                              pop rbp
00A0F081  C3                              ret
00A0F082  CC                              int3
00A0F083  E8 28 5C E4 FF                  call 0x140854cb0
00A0F088  E9 5A FF FF FF                  jmp 0x140a0efe7
00A0F08D  41 8B 56 5C                     mov edx, dword ptr [r14 + 0x5c]
00A0F091  48 8D 45 DF                     lea rax, [rbp - 0x21]
00A0F095  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0F09A  4C 8D 4D EF                     lea r9, [rbp - 0x11]
00A0F09E  48 8D 45 6F                     lea rax, [rbp + 0x6f]
00A0F0A2  4D 8B C5                        mov r8, r13
00A0F0A5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0F0AA  48 8B CF                        mov rcx, rdi
00A0F0AD  48 8D 45 E7                     lea rax, [rbp - 0x19]
00A0F0B1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0F0B6  E8 F5 7C E4 FF                  call 0x140856db0
00A0F0BB  84 C0                           test al, al
00A0F0BD  0F 84 DA 02 00 00               je 0x140a0f39d
00A0F0C3  44 8B 65 EF                     mov r12d, dword ptr [rbp - 0x11]
00A0F0C7  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00A0F0CB  44 89 65 D7                     mov dword ptr [rbp - 0x29], r12d
00A0F0CF  C6 45 67 01                     mov byte ptr [rbp + 0x67], 1
00A0F0D3  E9 45 FF FF FF                  jmp 0x140a0f01d
00A0F0D8  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
00A0F0DC  48 85 C0                        test rax, rax
00A0F0DF  0F 84 65 FF FF FF               je 0x140a0f04a
00A0F0E5  80 7D 6F 00                     cmp byte ptr [rbp + 0x6f], 0
00A0F0E9  75 59                           jne 0x140a0f144
00A0F0EB  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0F0F2  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00A0F0F6  48 8B CF                        mov rcx, rdi
00A0F0F9  75 3F                           jne 0x140a0f13a
00A0F0FB  E8 40 6E E4 FF                  call 0x140855f40
00A0F100  E9 45 FF FF FF                  jmp 0x140a0f04a
00A0F105  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00A0F109  E8 DE 06 00 00                  call 0x140a0f7ec
00A0F10E  8B D8                           mov ebx, eax
00A0F110  85 C0                           test eax, eax
00A0F112  0F 88 54 FF FF FF               js 0x140a0f06c
00A0F118  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
00A0F11C  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
00A0F120  48 8B CE                        mov rcx, rsi
00A0F123  E8 14 08 00 00                  call 0x140a0f93c
00A0F128  44 01 26                        add dword ptr [rsi], r12d
00A0F12B  E9 72 FE FF FF                  jmp 0x140a0efa2
00A0F130  E8 EB DA E4 FF                  call 0x14085cc20
00A0F135  E9 29 FF FF FF                  jmp 0x140a0f063
00A0F13A  E8 E1 DA E4 FF                  call 0x14085cc20
00A0F13F  E9 06 FF FF FF                  jmp 0x140a0f04a
00A0F144  33 D2                           xor edx, edx
00A0F146  48 8B C8                        mov rcx, rax
00A0F149  E8 22 37 17 00                  call 0x140b82870
00A0F14E  E9 F7 FE FF FF                  jmp 0x140a0f04a
00A0F153  44 8B 65 CF                     mov r12d, dword ptr [rbp - 0x31]
00A0F157  48 8B CF                        mov rcx, rdi
00A0F15A  41 83 FC FF                     cmp r12d, -1
00A0F15E  0F 85 A3 00 00 00               jne 0x140a0f207
00A0F164  45 8B 4E 48                     mov r9d, dword ptr [r14 + 0x48]
00A0F168  44 8B 45 7F                     mov r8d, dword ptr [rbp + 0x7f]
00A0F16C  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00A0F174  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A0F179  8B 75 77                        mov esi, dword ptr [rbp + 0x77]
00A0F17C  8B D6                           mov edx, esi
00A0F17E  E8 DD C2 E4 FF                  call 0x14085b460
00A0F183  4C 8B 6D 0F                     mov r13, qword ptr [rbp + 0xf]
00A0F187  8B D8                           mov ebx, eax
00A0F189  85 C0                           test eax, eax
00A0F18B  78 23                           js 0x140a0f1b0
00A0F18D  0F B7 45 FF                     movzx eax, word ptr [rbp - 1]
00A0F191  33 DB                           xor ebx, ebx
00A0F193  66 41 89 47 08                  mov word ptr [r15 + 8], ax
00A0F198  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
00A0F19B  41 89 37                        mov dword ptr [r15], esi
00A0F19E  41 89 47 0C                     mov dword ptr [r15 + 0xc], eax
00A0F1A2  45 89 67 04                     mov dword ptr [r15 + 4], r12d
00A0F1A6  4D 89 7E 70                     mov qword ptr [r14 + 0x70], r15
00A0F1AA  45 33 FF                        xor r15d, r15d
00A0F1AD  83 CE FF                        or esi, 0xffffffff
00A0F1B0  4D 85 ED                        test r13, r13
00A0F1B3  74 19                           je 0x140a0f1ce
00A0F1B5  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0F1BC  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00A0F1C0  48 8B CF                        mov rcx, rdi
00A0F1C3  0F 85 B9 00 00 00               jne 0x140a0f282
00A0F1C9  E8 72 6D E4 FF                  call 0x140855f40
00A0F1CE  83 FE FF                        cmp esi, -1
00A0F1D1  0F 85 E9 01 00 00               jne 0x140a0f3c0
00A0F1D7  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00A0F1DB  33 D2                           xor edx, edx
00A0F1DD  E8 8E 36 17 00                  call 0x140b82870
00A0F1E2  48 83 7D E7 00                  cmp qword ptr [rbp - 0x19], 0
00A0F1E7  0F 84 53 FE FF FF               je 0x140a0f040
00A0F1ED  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0F1F4  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00A0F1F8  48 8B CF                        mov rcx, rdi
00A0F1FB  75 7B                           jne 0x140a0f278
00A0F1FD  E8 3E 6D E4 FF                  call 0x140855f40
00A0F202  E9 39 FE FF FF                  jmp 0x140a0f040
00A0F207  45 33 C9                        xor r9d, r9d
00A0F20A  45 33 C0                        xor r8d, r8d
00A0F20D  41 8B D4                        mov edx, r12d
00A0F210  E8 6B 8E E4 FF                  call 0x140858080
00A0F215  8B D8                           mov ebx, eax
00A0F217  85 C0                           test eax, eax
00A0F219  0F 88 39 01 00 00               js 0x140a0f358
00A0F21F  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0F226  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00A0F22A  41 8B D4                        mov edx, r12d
00A0F22D  48 8B CF                        mov rcx, rdi
00A0F230  74 3F                           je 0x140a0f271
00A0F232  E8 29 5A E4 FF                  call 0x140854c60
00A0F237  4C 8B E8                        mov r13, rax
00A0F23A  48 85 C0                        test rax, rax
00A0F23D  0F 84 6E 01 00 00               je 0x140a0f3b1
00A0F243  48 8B D0                        mov rdx, rax
00A0F246  48 8B CF                        mov rcx, rdi
00A0F249  E8 C2 C6 E3 FF                  call 0x14084b910
00A0F24E  8B D8                           mov ebx, eax
00A0F250  85 C0                           test eax, eax
00A0F252  0F 88 60 01 00 00               js 0x140a0f3b8
00A0F258  44 8B 45 7F                     mov r8d, dword ptr [rbp + 0x7f]
00A0F25C  4C 8B CE                        mov r9, rsi
00A0F25F  8B 75 77                        mov esi, dword ptr [rbp + 0x77]
00A0F262  48 8B CF                        mov rcx, rdi
00A0F265  8B D6                           mov edx, esi
00A0F267  E8 00 34 A9 FF                  call 0x1404a266c
00A0F26C  E9 16 FF FF FF                  jmp 0x140a0f187
00A0F271  E8 3A 5A E4 FF                  call 0x140854cb0
00A0F276  EB BF                           jmp 0x140a0f237
00A0F278  E8 A3 D9 E4 FF                  call 0x14085cc20
00A0F27D  E9 BE FD FF FF                  jmp 0x140a0f040
00A0F282  E8 99 D9 E4 FF                  call 0x14085cc20
00A0F287  E9 42 FF FF FF                  jmp 0x140a0f1ce
00A0F28C  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00A0F293  4C 8D 45 BF                     lea r8, [rbp - 0x41]
00A0F297  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
00A0F29B  48 8B CF                        mov rcx, rdi
00A0F29E  8B 50 28                        mov edx, dword ptr [rax + 0x28]
00A0F2A1  0F 84 B9 00 00 00               je 0x140a0f360
00A0F2A7  E8 B4 59 E4 FF                  call 0x140854c60
00A0F2AC  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00A0F2B0  B9 00 01 00 00                  mov ecx, 0x100
00A0F2B5  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
00A0F2B9  41 B8 43 4D 53 62               mov r8d, 0x62534d43
00A0F2BF  8B 50 28                        mov edx, dword ptr [rax + 0x28]
00A0F2C2  C1 EA 1F                        shr edx, 0x1f
00A0F2C5  41 89 56 48                     mov dword ptr [r14 + 0x48], edx
00A0F2C9  BA 00 80 00 00                  mov edx, 0x8000
00A0F2CE  E8 1D 2E 17 00                  call 0x140b820f0
00A0F2D3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00A0F2D7  48 85 C0                        test rax, rax
00A0F2DA  0F 84 C7 00 00 00               je 0x140a0f3a7
00A0F2E0  4C 8B C0                        mov r8, rax
00A0F2E3  48 8D 55 FF                     lea rdx, [rbp - 1]
00A0F2E7  49 8B CD                        mov rcx, r13
00A0F2EA  E8 55 03 00 00                  call 0x140a0f644
00A0F2EF  48 8D 45 CF                     lea rax, [rbp - 0x31]
00A0F2F3  48 83 C6 04                     add rsi, 4
00A0F2F7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0F2FC  4C 8D 45 FF                     lea r8, [rbp - 1]
00A0F300  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00A0F304  45 33 C9                        xor r9d, r9d
00A0F307  48 8B D6                        mov rdx, rsi
00A0F30A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0F30F  48 8B CF                        mov rcx, rdi
00A0F312  E8 69 78 E3 FF                  call 0x140846b80
00A0F317  BA 00 00 00 80                  mov edx, 0x80000000
00A0F31C  8B C8                           mov ecx, eax
00A0F31E  03 C2                           add eax, edx
00A0F320  85 C2                           test edx, eax
00A0F322  74 46                           je 0x140a0f36a
00A0F324  4C 8B 4D F7                     mov r9, qword ptr [rbp - 9]
00A0F328  48 8D 45 77                     lea rax, [rbp + 0x77]
00A0F32C  45 8B 45 0C                     mov r8d, dword ptr [r13 + 0xc]
00A0F330  48 8D 55 FF                     lea rdx, [rbp - 1]
00A0F334  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0F339  48 8B CF                        mov rcx, rdi
00A0F33C  41 8B 46 48                     mov eax, dword ptr [r14 + 0x48]
00A0F340  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A0F344  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00A0F349  E8 0A B7 E4 FF                  call 0x14085aa58
00A0F34E  8B D8                           mov ebx, eax
00A0F350  85 C0                           test eax, eax
00A0F352  0F 89 FB FD FF FF               jns 0x140a0f153
00A0F358  8B 75 77                        mov esi, dword ptr [rbp + 0x77]
00A0F35B  E9 6E FE FF FF                  jmp 0x140a0f1ce
00A0F360  E8 4B 59 E4 FF                  call 0x140854cb0
00A0F365  E9 42 FF FF FF                  jmp 0x140a0f2ac
00A0F36A  81 F9 34 00 00 C0               cmp ecx, 0xc0000034
00A0F370  74 B2                           je 0x140a0f324
00A0F372  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A0F377  E9 5B FE FF FF                  jmp 0x140a0f1d7
00A0F37C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A0F381  E9 E6 FC FF FF                  jmp 0x140a0f06c
00A0F386  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A0F38B  BA 43 4D 55 77                  mov edx, 0x77554d43
00A0F390  49 8B CF                        mov rcx, r15
00A0F393  E8 48 96 A3 FF                  call 0x1404489e0
00A0F398  E9 CF FC FF FF                  jmp 0x140a0f06c
00A0F39D  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A0F3A2  E9 A3 FC FF FF                  jmp 0x140a0f04a
00A0F3A7  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A0F3AC  E9 31 FE FF FF                  jmp 0x140a0f1e2
00A0F3B1  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A0F3B6  EB A0                           jmp 0x140a0f358
00A0F3B8  8B 75 77                        mov esi, dword ptr [rbp + 0x77]
00A0F3BB  E9 F5 FD FF FF                  jmp 0x140a0f1b5
00A0F3C0  8B D6                           mov edx, esi
00A0F3C2  48 8B CF                        mov rcx, rdi
00A0F3C5  E8 CE BB E3 FF                  call 0x14084af98
00A0F3CA  E9 08 FE FF FF                  jmp 0x140a0f1d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLightWeightPrepareSetValueKeyUoW(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (168);
    v_rbx = 0;
    v_r12 = (unsigned int)((v_r12) | (0xFFFFFFFFULL));
    v_stack_m98 = (unsigned int)(v_r12);
    v_stack_m94 = 0;
    v_stack_mA0 = (unsigned int)(v_r12);
    v_stack_m9C = 0;
    v_stack_m80 = (unsigned int)(v_r12);
    v_stack_m7C = 0;
    v_stack_p20 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = (unsigned int)(v_r12);
    v_stack_mA4 = 0;
    v_stack_m68 = 0;
    v_stack_m78 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = (unsigned int)(v_r12);
    v_stack_p10 = 0;
    v_stack_m50 = 0;
    v_stack_m88 = *(unsigned __int64 *)(a1 + 104);
    v_stack_m60 = v_xmm0;
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_00A0F105;
loc_00A0EFA2:
    result = CmpAllocatePool(256, 16, (unsigned int)(0x77554D43ULL), a4);
    if (result == 0) goto loc_00A0F37C;
    *(unsigned int *)(result) = (unsigned int)(v_r12);
    *(unsigned int *)(result + 4) = (unsigned int)(v_r12);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) == 0) goto loc_00A0F083;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)(*(unsigned int *)(a1 + 92)), v_stack_m98, a4);
loc_00A0EFE7:
    if (result == 0) goto loc_00A0F386;
    v_r12 = (unsigned int)(*(unsigned int *)(result + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < ((unsigned int)((unsigned int)(0x80000000ULL)))) { v_r12 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4))); }
    v_stack_m88 = (unsigned int)(v_r12);
    v_stack_m70 = (unsigned int)(v_r12);
    if ((unsigned int)(v_r12) == 0) goto loc_00A0F021;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_00A0F08D;
loc_00A0F01D:
    v_stack_m68 = result + 8;
loc_00A0F021:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 40)), a3, a4);
    if (!sign_flag) goto loc_00A0F28C;
loc_00A0F040:
    if (v_stack_p8 != 0) goto loc_00A0F0D8;
loc_00A0F04A:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) != 0) goto loc_00A0F130;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m98, a3, a4);
loc_00A0F063:
    if (result != 0) goto loc_00A0F38B;
loc_00A0F06C:
    v_rsp = (v_rsp) + (168);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A0F083:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m98, a3, a4);
    goto loc_00A0EFE7;
loc_00A0F08D:
    v_stack_p30 = v_stack_m80;
    v_stack_p28 = v_stack_p10;
    v_stack_p20 = v_stack_m78;
    result = CmpGetValueData(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)(*(unsigned int *)(a1 + 92)), result, v_stack_m70);
    if ((unsigned __int8)(result) == 0) goto loc_00A0F39D;
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_m70));
    v_stack_p8 = 1;
    goto loc_00A0F01D;
loc_00A0F0D8:
    if (v_stack_m68 == 0) goto loc_00A0F04A;
    if (v_stack_p10 != 0) goto loc_00A0F144;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) != 0) goto loc_00A0F13A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m80, result, v_stack_m70);
    goto loc_00A0F04A;
loc_00A0F105:
    result = CmpLightWeightCreateSetValueData(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m88, result, v_stack_m70);
    if (sign_flag) goto loc_00A0F06C;
    result = CmpLightWeightUpdateSharedSetValueData(v_stack_m88, *(unsigned __int64 *)(a1 + 48), result, v_stack_m70);
    goto loc_00A0EFA2;
loc_00A0F130:
    result = HvpReleaseCellFlat(v_stack_m88, *(unsigned __int64 *)(a1 + 48), result, v_stack_m70);
    goto loc_00A0F063;
loc_00A0F13A:
    result = HvpReleaseCellFlat(v_stack_m88, *(unsigned __int64 *)(a1 + 48), result, v_stack_m70);
    goto loc_00A0F04A;
loc_00A0F144:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, result, v_stack_m70);
    goto loc_00A0F04A;
loc_00A0F153:
    if (((unsigned int)((unsigned int)(v_stack_m90))) != -1) goto loc_00A0F207;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_m88;
    result = CmpAddValueToListEx(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(v_stack_p20), (unsigned int)(*(unsigned int *)(a1 + 72)));
loc_00A0F187:
    v_rbx = (unsigned int)((unsigned int)(result));
    v_rsi = (unsigned int)(v_stack_p18);
    v_r15 = result;
    if (!(sign_flag)) {
        result = v_stack_m60;
        v_rbx = 0;
        *(unsigned __int16 *)(result + 8) = (unsigned __int16)(result);
        result = v_stack_m88;
        *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_p18));
        *(unsigned int *)(result + 12) = (unsigned int)(result);
        *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(v_stack_m90));
        *(unsigned __int64 *)(a1 + 112) = result;
        v_r15 = 0;
        v_rsi = (unsigned int)(((unsigned int)(v_stack_p18)) | (0xFFFFFFFFULL));
    }
    if (v_stack_m50 == 0) goto loc_00A0F1CE;
loc_00A0F1B5:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) != 0) goto loc_00A0F282;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_mA8, (unsigned int)(v_stack_p20), (unsigned int)(*(unsigned int *)(a1 + 72)));
loc_00A0F1CE:
    if (((unsigned int)(v_rsi)) != -1) goto loc_00A0F3C0;
loc_00A0F1D7:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, (unsigned int)(v_stack_p20), (unsigned int)(*(unsigned int *)(a1 + 72)));
loc_00A0F1E2:
    if (v_stack_m78 == 0) goto loc_00A0F040;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) != 0) goto loc_00A0F278;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_mA0, (unsigned int)(v_stack_p20), (unsigned int)(*(unsigned int *)(a1 + 72)));
    goto loc_00A0F040;
loc_00A0F207:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))), a3, a4);
    if (sign_flag) goto loc_00A0F358;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) == 0) goto loc_00A0F271;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))), v_stack_mA8, a4);
loc_00A0F237:
    if (result == 0) goto loc_00A0F3B1;
    result = CmpMarkValueDataDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), result, v_stack_mA8, a4);
    if (sign_flag) goto loc_00A0F3B8;
    result = CmpSwapValueInList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(v_stack_p20), v_rsi);
    goto loc_00A0F187;
loc_00A0F271:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(v_stack_p20), v_rsi);
    goto loc_00A0F237;
loc_00A0F278:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(v_stack_p20), v_rsi);
    goto loc_00A0F040;
loc_00A0F282:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(v_stack_p20), v_rsi);
    goto loc_00A0F1CE;
loc_00A0F28C:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) == 0) goto loc_00A0F360;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 40)), v_stack_mA0, v_rsi);
loc_00A0F2AC:
    v_stack_m78 = result;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 40))) >> (31));
    *(unsigned int *)(a1 + 72) = (unsigned int)(a2);
    result = ExAllocatePool2(256, (unsigned int)(0x8000ULL), (unsigned int)(0x62534D43ULL), v_rsi);
    v_stack_m70 = result;
    if (result == 0) goto loc_00A0F3A7;
    result = CmpInitializeValueNameString(result, v_stack_m60, result, v_rsi);
    v_rsi = ((unsigned int)(v_stack_p18)) + (4);
    v_stack_p28 = v_stack_m90;
    a4 = 0;
    v_stack_p20 = v_stack_p20;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_rsi, v_stack_m60, a4);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_00A0F36A;
loc_00A0F324:
    v_stack_p30 = v_stack_p18;
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m90));
    result = CmpAddValueKeyNew(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m60, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_m68);
    if (!sign_flag) goto loc_00A0F153;
loc_00A0F358:
    goto loc_00A0F1CE;
loc_00A0F360:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m60, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_m68);
    goto loc_00A0F2AC;
loc_00A0F36A:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32))) == 0xC0000034ULL) goto loc_00A0F324;
    goto loc_00A0F1D7;
loc_00A0F37C:
    goto loc_00A0F06C;
loc_00A0F386:
loc_00A0F38B:
    result = CmpFreePoolWithTag(0, (unsigned int)(0x77554D43ULL), (unsigned int)(*(unsigned int *)(result + 12)), v_stack_m68);
    goto loc_00A0F06C;
loc_00A0F39D:
    goto loc_00A0F04A;
loc_00A0F3A7:
    goto loc_00A0F1E2;
loc_00A0F3B1:
    goto loc_00A0F358;
loc_00A0F3B8:
    goto loc_00A0F1B5;
loc_00A0F3C0:
    result = CmpFreeValue(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(*(unsigned int *)(result + 12)), v_stack_m68);
    goto loc_00A0F1D7;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLightWeightPrepareSetValueKeyUoW(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (168);
    local_rbx = 0;
    local_r12 = (uint32_t)((local_r12) | (0xFFFFFFFFULL));
    v_stack_m98 = (uint32_t)(local_r12);
    v_stack_m94 = 0;
    v_stack_mA0 = (uint32_t)(local_r12);
    v_stack_m9C = 0;
    v_stack_m80 = (uint32_t)(local_r12);
    v_stack_m7C = 0;
    v_stack_p20 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = (uint32_t)(local_r12);
    v_stack_mA4 = 0;
    v_stack_m68 = 0;
    v_stack_m78 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = (uint32_t)(local_r12);
    v_stack_p10 = 0;
    v_stack_m50 = 0;
    v_stack_m88 = *(uint64_t *)(arg1 + 0x68);
    v_stack_m60 = v_xmm0;
    if (*(uint64_t *)(arg1 + 0x68) == 0) goto loc_00A0F105;
loc_00A0EFA2:
    result = CmpAllocatePool(256, 16, (uint32_t)(0x77554D43ULL), Arg4);
    if (result == 0) goto loc_00A0F37C;
    *(uint32_t *)(result) = (uint32_t)(local_r12);
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_r12);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00A0F083;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x5C)), v_stack_m98, Arg4);
loc_00A0EFE7:
    if (result == 0) goto loc_00A0F386;
    local_r12 = (uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < ((uint32_t)((uint32_t)(0x80000000ULL)))) { local_r12 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))); }
    v_stack_m88 = (uint32_t)(local_r12);
    v_stack_m70 = (uint32_t)(local_r12);
    if ((uint32_t)(local_r12) == 0) goto loc_00A0F021;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_00A0F08D;
loc_00A0F01D:
    v_stack_m68 = result + 8;
loc_00A0F021:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x28)), Arg3, Arg4);
    if (!sign_flag) goto loc_00A0F28C;
loc_00A0F040:
    if (v_stack_p8 != 0) goto loc_00A0F0D8;
loc_00A0F04A:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A0F130;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m98, Arg3, Arg4);
loc_00A0F063:
    if (result != 0) goto loc_00A0F38B;
loc_00A0F06C:
    local_rsp = (local_rsp) + (168);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A0F083:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m98, Arg3, Arg4);
    goto loc_00A0EFE7;
loc_00A0F08D:
    v_stack_p30 = v_stack_m80;
    v_stack_p28 = v_stack_p10;
    v_stack_p20 = v_stack_m78;
    result = CmpGetValueData(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x5C)), result, v_stack_m70);
    if ((uint8_t)(result) == 0) goto loc_00A0F39D;
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_m70));
    v_stack_p8 = 1;
    goto loc_00A0F01D;
loc_00A0F0D8:
    if (v_stack_m68 == 0) goto loc_00A0F04A;
    if (v_stack_p10 != 0) goto loc_00A0F144;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A0F13A;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m80, result, v_stack_m70);
    goto loc_00A0F04A;
loc_00A0F105:
    result = CmpLightWeightCreateSetValueData(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m88, result, v_stack_m70);
    if (sign_flag) goto loc_00A0F06C;
    result = CmpLightWeightUpdateSharedSetValueData(v_stack_m88, *(uint64_t *)(arg1 + 0x30), result, v_stack_m70);
    goto loc_00A0EFA2;
loc_00A0F130:
    result = HvpReleaseCellFlat(v_stack_m88, *(uint64_t *)(arg1 + 0x30), result, v_stack_m70);
    goto loc_00A0F063;
loc_00A0F13A:
    result = HvpReleaseCellFlat(v_stack_m88, *(uint64_t *)(arg1 + 0x30), result, v_stack_m70);
    goto loc_00A0F04A;
loc_00A0F144:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, result, v_stack_m70);
    goto loc_00A0F04A;
loc_00A0F153:
    if (((uint32_t)((uint32_t)(v_stack_m90))) != -1) goto loc_00A0F207;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_m88;
    result = CmpAddValueToListEx(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(v_stack_p20), (uint32_t)(*(uint32_t *)(arg1 + 0x48)));
loc_00A0F187:
    local_rbx = (uint32_t)((uint32_t)(result));
    local_rsi = (uint32_t)(v_stack_p18);
    local_r15 = result;
    if (!(sign_flag)) {
        result = v_stack_m60;
        local_rbx = 0;
        *(uint16_t *)(result + 0x8) = (uint16_t)(result);
        result = v_stack_m88;
        *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_p18));
        *(uint32_t *)(result + 0xC) = (uint32_t)(result);
        *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(v_stack_m90));
        *(uint64_t *)(arg1 + 0x70) = result;
        local_r15 = 0;
        local_rsi = (uint32_t)(((uint32_t)(v_stack_p18)) | (0xFFFFFFFFULL));
    }
    if (v_stack_m50 == 0) goto loc_00A0F1CE;
loc_00A0F1B5:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A0F282;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_mA8, (uint32_t)(v_stack_p20), (uint32_t)(*(uint32_t *)(arg1 + 0x48)));
loc_00A0F1CE:
    if (((uint32_t)(local_rsi)) != -1) goto loc_00A0F3C0;
loc_00A0F1D7:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, Arg2, (uint32_t)(v_stack_p20), (uint32_t)(*(uint32_t *)(arg1 + 0x48)));
loc_00A0F1E2:
    if (v_stack_m78 == 0) goto loc_00A0F040;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A0F278;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_mA0, (uint32_t)(v_stack_p20), (uint32_t)(*(uint32_t *)(arg1 + 0x48)));
    goto loc_00A0F040;
loc_00A0F207:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))), Arg3, Arg4);
    if (sign_flag) goto loc_00A0F358;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00A0F271;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))), v_stack_mA8, Arg4);
loc_00A0F237:
    if (result == 0) goto loc_00A0F3B1;
    result = CmpMarkValueDataDirty(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), result, v_stack_mA8, Arg4);
    if (sign_flag) goto loc_00A0F3B8;
    result = CmpSwapValueInList(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(v_stack_p20), local_rsi);
    goto loc_00A0F187;
loc_00A0F271:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(v_stack_p20), local_rsi);
    goto loc_00A0F237;
loc_00A0F278:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(v_stack_p20), local_rsi);
    goto loc_00A0F040;
loc_00A0F282:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(v_stack_p20), local_rsi);
    goto loc_00A0F1CE;
loc_00A0F28C:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00A0F360;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x28)), v_stack_mA0, local_rsi);
loc_00A0F2AC:
    v_stack_m78 = result;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x28))) >> (31));
    *(uint32_t *)(arg1 + 0x48) = (uint32_t)(Arg2);
    result = ExAllocatePool2(256, (uint32_t)(0x8000ULL), (uint32_t)(0x62534D43ULL), local_rsi);
    v_stack_m70 = result;
    if (result == 0) goto loc_00A0F3A7;
    result = CmpInitializeValueNameString(result, v_stack_m60, result, local_rsi);
    local_rsi = ((uint32_t)(v_stack_p18)) + (4);
    v_stack_p28 = v_stack_m90;
    Arg4 = 0;
    v_stack_p20 = v_stack_p20;
    result = CmpFindNameInListWithStatus(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), local_rsi, v_stack_m60, Arg4);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_00A0F36A;
loc_00A0F324:
    v_stack_p30 = v_stack_p18;
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m90));
    result = CmpAddValueKeyNew(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m60, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_m68);
    if (!sign_flag) goto loc_00A0F153;
loc_00A0F358:
    goto loc_00A0F1CE;
loc_00A0F360:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m60, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_m68);
    goto loc_00A0F2AC;
loc_00A0F36A:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20))) == 0xC0000034ULL) goto loc_00A0F324;
    goto loc_00A0F1D7;
loc_00A0F37C:
    goto loc_00A0F06C;
loc_00A0F386:
loc_00A0F38B:
    result = CmpFreePoolWithTag(0, (uint32_t)(0x77554D43ULL), (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_m68);
    goto loc_00A0F06C;
loc_00A0F39D:
    goto loc_00A0F04A;
loc_00A0F3A7:
    goto loc_00A0F1E2;
loc_00A0F3B1:
    goto loc_00A0F358;
loc_00A0F3B8:
    goto loc_00A0F1B5;
loc_00A0F3C0:
    result = CmpFreeValue(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_m68);
    goto loc_00A0F1D7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x48` | `32` | `W` |
| `Arg1` | `+ 0x5C` | `32` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0EF28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
