# CmpCheckValueList

- RVA: `0x00970F6C`–`0x00971E05` (길이 `3,737` bytes)
- VA: `0x0000000140970F6C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00096084`
- 디코드: `840`개 명령, `3,737/3,737` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **67**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00971048` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x00971070` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x009711A4` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971200` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x00971228` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00971282` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971296` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x009712CC` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0097132A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971365` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0097139B` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009713B7` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x009713D4` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x009713F1` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00971431` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00971459` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971468` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00971472` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x009714A0` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009714CA` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971505` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971535` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971574` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x009715A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009715DF` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971608` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0097162E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971638` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971690` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x009716BB` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00971739` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x00971768` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x009717A0` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009717B1` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x009718A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0097191B` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0097192C` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00971995` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x009719A3` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x009719D7` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971A08` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971A2A` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971A43` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971A5C` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971A7D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971AB0` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971AD8` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971AF1` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971AFB` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00971B05` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971B47` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971B7C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971B86` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00971B90` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BB0` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BBA` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BC4` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BCE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BD8` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BE2` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00971BF0` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00971C3B` → [CmpCompareUnicodeString](../A1/CmpCompareUnicodeString_function_00A17340.md) (function, `0x00A17340`)
- `0x00971CD9` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971D25` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971D54` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971D93` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00971DDE` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)

### Direct callers
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096F270`

### Static image references
- `0x0097137B` → RVA `0x00FD8002` (`PAGEDATA`; read)
- `0x0097147C` → RVA `0x00EF7C60` (`.data`; read)
- `0x009717CE` → RVA `0x00FD9C00` (`PAGEDATA`; read)
- `0x009717DB` → RVA `0x00FD9C08` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x0097132A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0097139B` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971431` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009714A0` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009714CA` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971535` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009715A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971608` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009718A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0097191B` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009719D7` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971A08` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971AB0` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971B47` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971CD9` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971D25` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971D54` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971D93` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00971DDE` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **18**
  - `0x00971697` → [sub_00B28F1E + 0x10E](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x009716E0` → [sub_00B28F1E + 0x7E](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x009716F2` → [sub_00B28F1E + 0x7E](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971786` → [sub_00B28F1E + 0x9](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971977` → [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971982` → [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971C78` → [sub_00B28F1E + 0x86](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971C9C` → [sub_00B28F1E + 0x19F](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971CA9` → [sub_00B28F1E + 0x19F](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971CB6` → [sub_00B28F1E + 0x19F](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971CE1` → [sub_00B28F1E + 0x1A9](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971CF5` → [sub_00B28F1E + 0x1A9](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971D9B` → [sub_00B28F1E + 0x1B2](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971DBF` → [sub_00B28F1E + 0x1B2](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971DE6` → [sub_00B28F1E + 0x1D5](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971DEC` → [sub_00B28F1E + 0x1E8](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971DF6` → [sub_00B28F1E + 0x219](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)
  - `0x00971E00` → [sub_00B28F1E + 0x219](../B2/Unknown_function_00B28F1E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00970F6C  48 8B C4                        mov rax, rsp
00970F6F  48 89 58 08                     mov qword ptr [rax + 8], rbx
00970F73  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00970F77  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00970F7B  88 50 10                        mov byte ptr [rax + 0x10], dl
00970F7E  55                              push rbp
00970F7F  56                              push rsi
00970F80  57                              push rdi
00970F81  41 54                           push r12
00970F83  41 55                           push r13
00970F85  41 56                           push r14
00970F87  41 57                           push r15
00970F89  48 8D 68 C1                     lea rbp, [rax - 0x3f]
00970F8D  48 81 EC A0 00 00 00            sub rsp, 0xa0
00970F94  48 8B 7D 7F                     mov rdi, qword ptr [rbp + 0x7f]
00970F98  33 F6                           xor esi, esi
00970F9A  45 8B F1                        mov r14d, r9d
00970F9D  89 75 9F                        mov dword ptr [rbp - 0x61], esi
00970FA0  41 83 C9 FF                     or r9d, 0xffffffff
00970FA4  89 75 9B                        mov dword ptr [rbp - 0x65], esi
00970FA7  44 89 4D 97                     mov dword ptr [rbp - 0x69], r9d
00970FAB  0F 57 C0                        xorps xmm0, xmm0
00970FAE  44 89 4D A7                     mov dword ptr [rbp - 0x59], r9d
00970FB2  48 8B D9                        mov rbx, rcx
00970FB5  89 75 AB                        mov dword ptr [rbp - 0x55], esi
00970FB8  44 8B FE                        mov r15d, esi
00970FBB  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
00970FBF  44 8A E6                        mov r12b, sil
00970FC2  89 75 CB                        mov dword ptr [rbp - 0x35], esi
00970FC5  44 89 4D BF                     mov dword ptr [rbp - 0x41], r9d
00970FC9  89 75 C3                        mov dword ptr [rbp - 0x3d], esi
00970FCC  44 89 4D AF                     mov dword ptr [rbp - 0x51], r9d
00970FD0  89 75 B3                        mov dword ptr [rbp - 0x4d], esi
00970FD3  40 88 75 7F                     mov byte ptr [rbp + 0x7f], sil
00970FD7  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00970FDB  48 85 FF                        test rdi, rdi
00970FDE  74 1B                           je 0x140970ffb
00970FE0  4C 89 87 10 01 00 00            mov qword ptr [rdi + 0x110], r8
00970FE7  44 89 8F 18 01 00 00            mov dword ptr [rdi + 0x118], r9d
00970FEE  89 B7 1C 01 00 00               mov dword ptr [rdi + 0x11c], esi
00970FF4  48 89 B7 20 01 00 00            mov qword ptr [rdi + 0x120], rsi
00970FFB  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00971002  B9 01 00 00 00                  mov ecx, 1
00971007  89 30                           mov dword ptr [rax], esi
00971009  44 8D 69 0E                     lea r13d, [rcx + 0xe]
0097100D  48 8B 85 8F 00 00 00            mov rax, qword ptr [rbp + 0x8f]
00971014  89 30                           mov dword ptr [rax], esi
00971016  45 3B FE                        cmp r15d, r14d
00971019  0F 83 81 02 00 00               jae 0x1409712a0
0097101F  41 8B C7                        mov eax, r15d
00971022  49 8D 04 80                     lea rax, [r8 + rax*4]
00971026  44 8B 20                        mov r12d, dword ptr [rax]
00971029  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0097102D  84 D2                           test dl, dl
0097102F  0F 85 4D 08 00 00               jne 0x140971882
00971035  45 3B E1                        cmp r12d, r9d
00971038  0F 84 AB 05 00 00               je 0x1409715e9
0097103E  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
00971042  41 8B D4                        mov edx, r12d
00971045  48 8B CB                        mov rcx, rbx
00971048  E8 13 4D EE FF                  call 0x140855d60
0097104D  B9 01 00 00 00                  mov ecx, 1
00971052  84 C0                           test al, al
00971054  0F 84 61 0C 00 00               je 0x140971cbb
0097105A  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00971060  4C 8D 45 97                     lea r8, [rbp - 0x69]
00971064  48 8B CB                        mov rcx, rbx
00971067  41 8B D4                        mov edx, r12d
0097106A  0F 84 26 02 00 00               je 0x140971296
00971070  E8 EB 3B EE FF                  call 0x140854c60
00971075  4C 8B F8                        mov r15, rax
00971078  48 85 C0                        test rax, rax
0097107B  0F 84 9B 04 00 00               je 0x14097151c
00971081  B8 FC FF FF FF                  mov eax, 0xfffffffc
00971086  41 2B 47 FC                     sub eax, dword ptr [r15 - 4]
0097108A  83 F8 14                        cmp eax, 0x14
0097108D  0F 82 1B 0C 00 00               jb 0x140971cae
00971093  B9 76 6B 00 00                  mov ecx, 0x6b76
00971098  66 41 39 0F                     cmp word ptr [r15], cx
0097109C  0F 85 FF 0B 00 00               jne 0x140971ca1
009710A2  41 0F B7 57 02                  movzx edx, word ptr [r15 + 2]
009710A7  8D 4A 14                        lea ecx, [rdx + 0x14]
009710AA  83 F9 14                        cmp ecx, 0x14
009710AD  0F 82 E1 0B 00 00               jb 0x140971c94
009710B3  3B C8                           cmp ecx, eax
009710B5  0F 87 D9 0B 00 00               ja 0x140971c94
009710BB  45 0F B7 47 10                  movzx r8d, word ptr [r15 + 0x10]
009710C0  41 BB 01 00 00 00               mov r11d, 1
009710C6  45 84 C3                        test r11b, r8b
009710C9  0F 84 07 02 00 00               je 0x1409712d6
009710CF  B8 FF 3F 00 00                  mov eax, 0x3fff
009710D4  66 3B D0                        cmp dx, ax
009710D7  0F 87 CD 03 00 00               ja 0x1409714aa
009710DD  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
009710E1  F6 80 90 00 00 00 02            test byte ptr [rax + 0x90], 2
009710E8  0F 94 C1                        sete cl
009710EB  66 45 0F A3 D8                  bt r8w, r11w
009710F0  0F 92 C0                        setb al
009710F3  84 C8                           test al, cl
009710F5  0F 85 CA 07 00 00               jne 0x1409718c5
009710FB  44 8A 4D 4F                     mov r9b, byte ptr [rbp + 0x4f]
009710FF  45 84 C9                        test r9b, r9b
00971102  0F 85 B3 06 00 00               jne 0x1409717bb
00971108  41 0F B7 4F 02                  movzx ecx, word ptr [r15 + 2]
0097110D  45 0F B7 47 10                  movzx r8d, word ptr [r15 + 0x10]
00971112  0F B7 C1                        movzx eax, cx
00971115  4C 8B 95 87 00 00 00            mov r10, qword ptr [rbp + 0x87]
0097111C  66 03 C0                        add ax, ax
0097111F  41 0F B7 D0                     movzx edx, r8w
00971123  66 41 23 D3                     and dx, r11w
00971127  66 0F 44 C1                     cmove ax, cx
0097112B  0F B7 C0                        movzx eax, ax
0097112E  41 39 02                        cmp dword ptr [r10], eax
00971131  73 13                           jae 0x140971146
00971133  0F B7 C1                        movzx eax, cx
00971136  66 03 C0                        add ax, ax
00971139  66 85 D2                        test dx, dx
0097113C  66 0F 44 C1                     cmove ax, cx
00971140  0F B7 C0                        movzx eax, ax
00971143  41 89 02                        mov dword ptr [r10], eax
00971146  41 8B 4F 04                     mov ecx, dword ptr [r15 + 4]
0097114A  89 4D BB                        mov dword ptr [rbp - 0x45], ecx
0097114D  45 84 C9                        test r9b, r9b
00971150  0F 85 B5 0A 00 00               jne 0x140971c0b
00971156  41 F6 C0 02                     test r8b, 2
0097115A  75 75                           jne 0x1409711d1
0097115C  81 F9 00 00 00 80               cmp ecx, 0x80000000
00971162  72 7F                           jb 0x1409711e3
00971164  8D 81 00 00 00 80               lea eax, [rcx - 0x80000000]
0097116A  83 F8 04                        cmp eax, 4
0097116D  0F 87 AE 04 00 00               ja 0x140971621
00971173  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
00971177  3D 00 00 00 80                  cmp eax, 0x80000000
0097117C  72 05                           jb 0x140971183
0097117E  05 00 00 00 80                  add eax, 0x80000000
00971183  48 8B 8D 8F 00 00 00            mov rcx, qword ptr [rbp + 0x8f]
0097118A  39 01                           cmp dword ptr [rcx], eax
0097118C  73 02                           jae 0x140971190
0097118E  89 01                           mov dword ptr [rcx], eax
00971190  48 8D 55 97                     lea rdx, [rbp - 0x69]
00971194  48 8B CB                        mov rcx, rbx
00971197  44 84 9B 8C 00 00 00            test byte ptr [rbx + 0x8c], r11b
0097119E  0F 85 CE 02 00 00               jne 0x140971472
009711A4  E8 97 4D EE FF                  call 0x140855f40
009711A9  44 8B 7D 9F                     mov r15d, dword ptr [rbp - 0x61]
009711AD  B9 01 00 00 00                  mov ecx, 1
009711B2  44 8A 65 7F                     mov r12b, byte ptr [rbp + 0x7f]
009711B6  44 03 F9                        add r15d, ecx
009711B9  44 8B 75 5F                     mov r14d, dword ptr [rbp + 0x5f]
009711BD  44 89 7D 9F                     mov dword ptr [rbp - 0x61], r15d
009711C1  8A 55 4F                        mov dl, byte ptr [rbp + 0x4f]
009711C4  41 83 C9 FF                     or r9d, 0xffffffff
009711C8  4C 8B 45 57                     mov r8, qword ptr [rbp + 0x57]
009711CC  E9 45 FE FF FF                  jmp 0x140971016
009711D1  85 C9                           test ecx, ecx
009711D3  0F 85 31 01 00 00               jne 0x14097130a
009711D9  41 39 77 0C                     cmp dword ptr [r15 + 0xc], esi
009711DD  0F 85 27 01 00 00               jne 0x14097130a
009711E3  45 8B 77 08                     mov r14d, dword ptr [r15 + 8]
009711E7  4C 8B EE                        mov r13, rsi
009711EA  44 89 75 B7                     mov dword ptr [rbp - 0x49], r14d
009711EE  85 C9                           test ecx, ecx
009711F0  0F 84 04 01 00 00               je 0x1409712fa
009711F6  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
009711FA  41 8B D6                        mov edx, r14d
009711FD  48 8B CB                        mov rcx, rbx
00971200  E8 5B 4B EE FF                  call 0x140855d60
00971205  B9 01 00 00 00                  mov ecx, 1
0097120A  84 C0                           test al, al
0097120C  0F 84 3F 03 00 00               je 0x140971551
00971212  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00971218  4C 8D 45 A7                     lea r8, [rbp - 0x59]
0097121C  48 8B CB                        mov rcx, rbx
0097121F  41 8B D6                        mov edx, r14d
00971222  0F 84 A4 00 00 00               je 0x1409712cc
00971228  E8 33 3A EE FF                  call 0x140854c60
0097122D  4C 8B E8                        mov r13, rax
00971230  48 85 C0                        test rax, rax
00971233  0F 84 01 0B 00 00               je 0x140971d3a
00971239  8B 4D BB                        mov ecx, dword ptr [rbp - 0x45]
0097123C  41 BB 01 00 00 00               mov r11d, 1
00971242  81 F9 D8 3F 00 00               cmp ecx, 0x3fd8
00971248  0F 87 F4 03 00 00               ja 0x140971642
0097124E  85 C9                           test ecx, ecx
00971250  74 11                           je 0x140971263
00971252  B8 FC FF FF FF                  mov eax, 0xfffffffc
00971257  41 2B 45 FC                     sub eax, dword ptr [r13 - 4]
0097125B  3B C8                           cmp ecx, eax
0097125D  0F 87 1B 03 00 00               ja 0x14097157e
00971263  41 BE 01 00 00 00               mov r14d, 1
00971269  4D 85 ED                        test r13, r13
0097126C  74 19                           je 0x140971287
0097126E  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00971272  48 8B CB                        mov rcx, rbx
00971275  44 84 B3 8C 00 00 00            test byte ptr [rbx + 0x8c], r14b
0097127C  0F 85 F2 02 00 00               jne 0x140971574
00971282  E8 B9 4C EE FF                  call 0x140855f40
00971287  41 BD 0F 00 00 00               mov r13d, 0xf
0097128D  45 8D 5D F2                     lea r11d, [r13 - 0xe]
00971291  E9 DD FE FF FF                  jmp 0x140971173
00971296  E8 15 3A EE FF                  call 0x140854cb0
0097129B  E9 D5 FD FF FF                  jmp 0x140971075
009712A0  41 F6 DC                        neg r12b
009712A3  45 1B F6                        sbb r14d, r14d
009712A6  41 81 E6 2A 00 00 80            and r14d, 0x8000002a
009712AD  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
009712B5  41 8B C6                        mov eax, r14d
009712B8  48 81 C4 A0 00 00 00            add rsp, 0xa0
009712BF  41 5F                           pop r15
009712C1  41 5E                           pop r14
009712C3  41 5D                           pop r13
009712C5  41 5C                           pop r12
009712C7  5F                              pop rdi
009712C8  5E                              pop rsi
009712C9  5D                              pop rbp
009712CA  C3                              ret
009712CB  CC                              int3
009712CC  E8 DF 39 EE FF                  call 0x140854cb0
009712D1  E9 57 FF FF FF                  jmp 0x14097122d
009712D6  41 84 D3                        test r11b, dl
009712D9  0F 85 33 02 00 00               jne 0x140971512
009712DF  B8 FF 7F 00 00                  mov eax, 0x7fff
009712E4  66 3B D0                        cmp dx, ax
009712E7  0F 86 F0 FD FF FF               jbe 0x1409710dd
009712ED  C7 44 24 20 96 00 00 00         mov dword ptr [rsp + 0x20], 0x96
009712F5  E9 B8 01 00 00                  jmp 0x1409714b2
009712FA  41 83 FE FF                     cmp r14d, -1
009712FE  0F 84 FA 08 00 00               je 0x140971bfe
00971304  41 BD 0F 00 00 00               mov r13d, 0xf
0097130A  C7 44 24 20 E0 00 00 00         mov dword ptr [rsp + 0x20], 0xe0
00971312  B9 4C 01 00 C0                  mov ecx, 0xc000014c
00971317  44 88 5D 7F                     mov byte ptr [rbp + 0x7f], r11b
0097131B  44 8B F1                        mov r14d, ecx
0097131E  44 8B C9                        mov r9d, ecx
00971321  48 8B CF                        mov rcx, rdi
00971324  45 8B C5                        mov r8d, r13d
00971327  41 8B D3                        mov edx, r11d
0097132A  E8 25 DC AF FF                  call 0x14046ef54
0097132F  48 85 FF                        test rdi, rdi
00971332  74 17                           je 0x14097134b
00971334  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00971337  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
0097133D  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
00971344  4C 89 BF 20 01 00 00            mov qword ptr [rdi + 0x120], r15
0097134B  41 BF 01 00 00 00               mov r15d, 1
00971351  48 8D 55 97                     lea rdx, [rbp - 0x69]
00971355  48 8B CB                        mov rcx, rbx
00971358  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
0097135F  0F 85 D3 02 00 00               jne 0x140971638
00971365  E8 D6 4B EE FF                  call 0x140855f40
0097136A  44 8A 65 7F                     mov r12b, byte ptr [rbp + 0x7f]
0097136E  F7 45 6F 00 00 02 00            test dword ptr [rbp + 0x6f], 0x20000
00971375  0F 85 0F 01 00 00               jne 0x14097148a
0097137B  40 38 35 80 6C 66 00            cmp byte ptr [rip + 0x666c80], sil
00971382  0F 84 F4 00 00 00               je 0x14097147c
00971388  41 B9 4C 01 00 C0               mov r9d, 0xc000014c
0097138E  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00971392  45 8B C5                        mov r8d, r13d
00971395  41 8B D7                        mov edx, r15d
00971398  48 8B CF                        mov rcx, rdi
0097139B  E8 B4 DB AF FF                  call 0x14046ef54
009713A0  4C 8D 45 C7                     lea r8, [rbp - 0x39]
009713A4  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
009713A7  48 8B CB                        mov rcx, rbx
009713AA  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
009713B1  0F 84 B1 00 00 00               je 0x140971468
009713B7  E8 A4 38 EE FF                  call 0x140854c60
009713BC  4C 8B F8                        mov r15, rax
009713BF  48 85 C0                        test rax, rax
009713C2  0F 84 D2 07 00 00               je 0x140971b9a
009713C8  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
009713CB  45 33 C9                        xor r9d, r9d
009713CE  45 33 C0                        xor r8d, r8d
009713D1  48 8B CB                        mov rcx, rbx
009713D4  E8 A7 6C EE FF                  call 0x140858080
009713D9  44 8B F0                        mov r14d, eax
009713DC  85 C0                           test eax, eax
009713DE  0F 88 17 0A 00 00               js 0x140971dfb
009713E4  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
009713E8  45 33 C9                        xor r9d, r9d
009713EB  45 33 C0                        xor r8d, r8d
009713EE  48 8B CB                        mov rcx, rbx
009713F1  E8 8A 6C EE FF                  call 0x140858080
009713F6  44 8B F0                        mov r14d, eax
009713F9  85 C0                           test eax, eax
009713FB  0F 88 F0 09 00 00               js 0x140971df1
00971401  44 8B 75 5F                     mov r14d, dword ptr [rbp + 0x5f]
00971405  83 C8 FF                        or eax, 0xffffffff
00971408  41 01 47 24                     add dword ptr [r15 + 0x24], eax
0097140C  44 03 F0                        add r14d, eax
0097140F  44 8B 7D 9F                     mov r15d, dword ptr [rbp - 0x61]
00971413  45 8B C6                        mov r8d, r14d
00971416  48 8B 45 57                     mov rax, qword ptr [rbp + 0x57]
0097141A  45 2B C7                        sub r8d, r15d
0097141D  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00971421  49 C1 E0 02                     shl r8, 2
00971425  41 8D 57 01                     lea edx, [r15 + 1]
00971429  44 89 75 5F                     mov dword ptr [rbp + 0x5f], r14d
0097142D  48 8D 14 90                     lea rdx, [rax + rdx*4]
00971431  E8 0A 54 D5 FF                  call 0x1406c6840
00971436  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0097143A  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0097143E  B9 01 00 00 00                  mov ecx, 1
00971443  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0097144A  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00971450  48 8B CB                        mov rcx, rbx
00971453  0F 85 D5 01 00 00               jne 0x14097162e
00971459  E8 E2 4A EE FF                  call 0x140855f40
0097145E  B9 01 00 00 00                  mov ecx, 1
00971463  E9 59 FD FF FF                  jmp 0x1409711c1
00971468  E8 43 38 EE FF                  call 0x140854cb0
0097146D  E9 4A FF FF FF                  jmp 0x1409713bc
00971472  E8 A9 B7 EE FF                  call 0x14085cc20
00971477  E9 2D FD FF FF                  jmp 0x1409711a9
0097147C  8B 05 DE 67 58 00               mov eax, dword ptr [rip + 0x5867de]
00971482  A8 06                           test al, 6
00971484  0F 85 FE FE FF FF               jne 0x140971388
0097148A  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
00971492  41 B9 4C 01 00 C0               mov r9d, 0xc000014c
00971498  45 8B C5                        mov r8d, r13d
0097149B  33 D2                           xor edx, edx
0097149D  48 8B CF                        mov rcx, rdi
009714A0  E8 AF DA AF FF                  call 0x14046ef54
009714A5  E9 03 FE FF FF                  jmp 0x1409712ad
009714AA  C7 44 24 20 92 00 00 00         mov dword ptr [rsp + 0x20], 0x92
009714B2  B9 4C 01 00 C0                  mov ecx, 0xc000014c
009714B7  44 88 5D 7F                     mov byte ptr [rbp + 0x7f], r11b
009714BB  44 8B F1                        mov r14d, ecx
009714BE  44 8B C9                        mov r9d, ecx
009714C1  41 8B D3                        mov edx, r11d
009714C4  45 8B C5                        mov r8d, r13d
009714C7  48 8B CF                        mov rcx, rdi
009714CA  E8 85 DA AF FF                  call 0x14046ef54
009714CF  48 85 FF                        test rdi, rdi
009714D2  74 17                           je 0x1409714eb
009714D4  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
009714D7  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
009714DD  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
009714E4  4C 89 BF 20 01 00 00            mov qword ptr [rdi + 0x120], r15
009714EB  41 BF 01 00 00 00               mov r15d, 1
009714F1  48 8D 55 97                     lea rdx, [rbp - 0x69]
009714F5  48 8B CB                        mov rcx, rbx
009714F8  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
009714FF  0F 85 AC 02 00 00               jne 0x1409717b1
00971505  E8 36 4A EE FF                  call 0x140855f40
0097150A  45 8A E7                        mov r12b, r15b
0097150D  E9 5C FE FF FF                  jmp 0x14097136e
00971512  C7 44 24 20 94 00 00 00         mov dword ptr [rsp + 0x20], 0x94
0097151A  EB 96                           jmp 0x1409714b2
0097151C  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00971522  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
0097152A  45 8B C5                        mov r8d, r13d
0097152D  33 D2                           xor edx, edx
0097152F  48 8B CF                        mov rcx, rdi
00971532  45 8B F1                        mov r14d, r9d
00971535  E8 1A DA AF FF                  call 0x14046ef54
0097153A  48 85 FF                        test rdi, rdi
0097153D  0F 84 6A FD FF FF               je 0x1409712ad
00971543  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00971546  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
0097154C  E9 68 03 00 00                  jmp 0x1409718b9
00971551  C7 44 24 20 F0 00 00 00         mov dword ptr [rsp + 0x20], 0xf0
00971559  41 BD 0F 00 00 00               mov r13d, 0xf
0097155F  BA 4C 01 00 C0                  mov edx, 0xc000014c
00971564  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00971567  44 8B F2                        mov r14d, edx
0097156A  44 8B CA                        mov r9d, edx
0097156D  8B D1                           mov edx, ecx
0097156F  E9 50 FF FF FF                  jmp 0x1409714c4
00971574  E8 A7 B6 EE FF                  call 0x14085cc20
00971579  E9 09 FD FF FF                  jmp 0x140971287
0097157E  B9 4C 01 00 C0                  mov ecx, 0xc000014c
00971583  44 88 5D 7F                     mov byte ptr [rbp + 0x7f], r11b
00971587  44 8B F1                        mov r14d, ecx
0097158A  C7 44 24 20 90 01 00 00         mov dword ptr [rsp + 0x20], 0x190
00971592  44 8B C9                        mov r9d, ecx
00971595  41 BD 0F 00 00 00               mov r13d, 0xf
0097159B  48 8B CF                        mov rcx, rdi
0097159E  45 8B C5                        mov r8d, r13d
009715A1  41 8B D3                        mov edx, r11d
009715A4  E8 AB D9 AF FF                  call 0x14046ef54
009715A9  48 85 FF                        test rdi, rdi
009715AC  74 17                           je 0x1409715c5
009715AE  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
009715B1  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
009715B7  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
009715BE  4C 89 BF 20 01 00 00            mov qword ptr [rdi + 0x120], r15
009715C5  41 BF 01 00 00 00               mov r15d, 1
009715CB  48 8D 55 A7                     lea rdx, [rbp - 0x59]
009715CF  48 8B CB                        mov rcx, rbx
009715D2  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
009715D9  0F 85 26 05 00 00               jne 0x140971b05
009715DF  E8 5C 49 EE FF                  call 0x140855f40
009715E4  E9 68 FD FF FF                  jmp 0x140971351
009715E9  44 8A E1                        mov r12b, cl
009715EC  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
009715EF  8B D1                           mov edx, ecx
009715F1  C7 44 24 20 50 00 00 00         mov dword ptr [rsp + 0x20], 0x50
009715F9  41 BE 4C 01 00 C0               mov r14d, 0xc000014c
009715FF  45 8B C5                        mov r8d, r13d
00971602  45 8B CE                        mov r9d, r14d
00971605  48 8B CF                        mov rcx, rdi
00971608  E8 47 D9 AF FF                  call 0x14046ef54
0097160D  48 85 FF                        test rdi, rdi
00971610  0F 85 E4 06 00 00               jne 0x140971cfa
00971616  41 BF 01 00 00 00               mov r15d, 1
0097161C  E9 4D FD FF FF                  jmp 0x14097136e
00971621  C7 44 24 20 A0 01 00 00         mov dword ptr [rsp + 0x20], 0x1a0
00971629  E9 E4 FC FF FF                  jmp 0x140971312
0097162E  E8 ED B5 EE FF                  call 0x14085cc20
00971633  E9 26 FE FF FF                  jmp 0x14097145e
00971638  E8 E3 B5 EE FF                  call 0x14085cc20
0097163D  E9 28 FD FF FF                  jmp 0x14097136a
00971642  83 BB DC 00 00 00 04            cmp dword ptr [rbx + 0xdc], 4
00971649  0F 82 FF FB FF FF               jb 0x14097124e
0097164F  B8 FC FF FF FF                  mov eax, 0xfffffffc
00971654  41 2B 45 FC                     sub eax, dword ptr [r13 - 4]
00971658  83 F8 08                        cmp eax, 8
0097165B  0F 82 26 04 00 00               jb 0x140971a87
00971661  B8 64 62 00 00                  mov eax, 0x6264
00971666  66 41 39 45 00                  cmp word ptr [r13], ax
0097166B  0F 85 16 04 00 00               jne 0x140971a87
00971671  66 41 39 75 02                  cmp word ptr [r13 + 2], si
00971676  0F 84 0B 04 00 00               je 0x140971a87
0097167C  41 8B 55 04                     mov edx, dword ptr [r13 + 4]
00971680  83 FA FF                        cmp edx, -1
00971683  0F 84 FE 03 00 00               je 0x140971a87
00971689  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
0097168D  48 8B CB                        mov rcx, rbx
00971690  E8 CB 46 EE FF                  call 0x140855d60
00971695  84 C0                           test al, al
00971697  0F 84 8F 79 1B 00               je 0x140b2902c
0097169D  41 8B 55 04                     mov edx, dword ptr [r13 + 4]
009716A1  4C 8D 45 AF                     lea r8, [rbp - 0x51]
009716A5  41 BE 01 00 00 00               mov r14d, 1
009716AB  48 8B CB                        mov rcx, rbx
009716AE  44 84 B3 8C 00 00 00            test byte ptr [rbx + 0x8c], r14b
009716B5  0F 84 40 04 00 00               je 0x140971afb
009716BB  E8 A0 35 EE FF                  call 0x140854c60
009716C0  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
009716C4  4C 8B C8                        mov r9, rax
009716C7  48 85 C0                        test rax, rax
009716CA  0F 84 F4 06 00 00               je 0x140971dc4
009716D0  45 0F B7 45 02                  movzx r8d, word ptr [r13 + 2]
009716D5  41 8B C8                        mov ecx, r8d
009716D8  48 C1 E1 02                     shl rcx, 2
009716DC  48 83 F9 04                     cmp rcx, 4
009716E0  0F 82 B6 78 1B 00               jb 0x140b28f9c
009716E6  B8 FC FF FF FF                  mov eax, 0xfffffffc
009716EB  41 2B 41 FC                     sub eax, dword ptr [r9 - 4]
009716EF  48 3B C8                        cmp rcx, rax
009716F2  0F 87 A4 78 1B 00               ja 0x140b28f9c
009716F8  8B 4D BB                        mov ecx, dword ptr [rbp - 0x45]
009716FB  B8 3F 64 A0 00                  mov eax, 0xa0643f
00971700  81 C1 D7 3F 00 00               add ecx, 0x3fd7
00971706  F7 E1                           mul ecx
00971708  2B CA                           sub ecx, edx
0097170A  D1 E9                           shr ecx, 1
0097170C  03 CA                           add ecx, edx
0097170E  C1 E9 0D                        shr ecx, 0xd
00971711  44 3B C1                        cmp r8d, ecx
00971714  0F 85 56 05 00 00               jne 0x140971c70
0097171A  44 8B E6                        mov r12d, esi
0097171D  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
00971722  48 8B CB                        mov rcx, rbx
00971725  44 3B E0                        cmp r12d, eax
00971728  0F 83 3E 03 00 00               jae 0x140971a6c
0097172E  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
00971732  45 8B F4                        mov r14d, r12d
00971735  43 8B 14 B1                     mov edx, dword ptr [r9 + r14*4]
00971739  E8 22 46 EE FF                  call 0x140855d60
0097173E  84 C0                           test al, al
00971740  0F 84 9B 02 00 00               je 0x1409719e1
00971746  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0097174A  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0097174E  48 8B CB                        mov rcx, rbx
00971751  42 8B 14 B0                     mov edx, dword ptr [rax + r14*4]
00971755  41 BE 01 00 00 00               mov r14d, 1
0097175B  44 84 B3 8C 00 00 00            test byte ptr [rbx + 0x8c], r14b
00971762  0F 84 2D 02 00 00               je 0x140971995
00971768  E8 F3 34 EE FF                  call 0x140854c60
0097176D  48 8B C8                        mov rcx, rax
00971770  48 85 C0                        test rax, rax
00971773  0F 84 00 06 00 00               je 0x140971d79
00971779  B8 FC FF FF FF                  mov eax, 0xfffffffc
0097177E  2B 41 FC                        sub eax, dword ptr [rcx - 4]
00971781  3D D8 3F 00 00                  cmp eax, 0x3fd8
00971786  0F 82 9B 77 1B 00               jb 0x140b28f27
0097178C  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00971790  48 8B CB                        mov rcx, rbx
00971793  44 84 B3 8C 00 00 00            test byte ptr [rbx + 0x8c], r14b
0097179A  0F 85 F0 03 00 00               jne 0x140971b90
009717A0  E8 9B 47 EE FF                  call 0x140855f40
009717A5  4C 8B 4D CF                     mov r9, qword ptr [rbp - 0x31]
009717A9  45 03 E6                        add r12d, r14d
009717AC  E9 6C FF FF FF                  jmp 0x14097171d
009717B1  E8 6A B4 EE FF                  call 0x14085cc20
009717B6  E9 4F FD FF FF                  jmp 0x14097150a
009717BB  49 8D 57 14                     lea rdx, [r15 + 0x14]
009717BF  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
009717C4  45 84 5F 10                     test byte ptr [r15 + 0x10], r11b
009717C8  0F 84 53 04 00 00               je 0x140971c21
009717CE  0F B7 0D 2B 84 66 00            movzx ecx, word ptr [rip + 0x66842b]
009717D5  41 B9 FF FF 00 00               mov r9d, 0xffff
009717DB  4C 8B 05 26 84 66 00            mov r8, qword ptr [rip + 0x668426]
009717E2  66 D1 E9                        shr cx, 1
009717E5  66 89 45 BB                     mov word ptr [rbp - 0x45], ax
009717E9  66 89 4D B7                     mov word ptr [rbp - 0x49], cx
009717ED  66 85 C9                        test cx, cx
009717F0  0F 84 66 01 00 00               je 0x14097195c
009717F6  66 85 C0                        test ax, ax
009717F9  0F 84 5D 01 00 00               je 0x14097195c
009717FF  45 0F B7 30                     movzx r14d, word ptr [r8]
00971803  49 83 C0 02                     add r8, 2
00971807  44 0F B6 2A                     movzx r13d, byte ptr [rdx]
0097180B  49 03 D3                        add rdx, r11
0097180E  4C 89 45 EF                     mov qword ptr [rbp - 0x11], r8
00971812  48 89 55 E7                     mov qword ptr [rbp - 0x19], rdx
00971816  66 45 3B F5                     cmp r14w, r13w
0097181A  74 59                           je 0x140971875
0097181C  66 41 83 FE 61                  cmp r14w, 0x61
00971821  0F 82 85 01 00 00               jb 0x1409719ac
00971827  66 41 83 FE 7A                  cmp r14w, 0x7a
0097182C  0F 87 6D 01 00 00               ja 0x14097199f
00971832  B8 E0 FF 00 00                  mov eax, 0xffe0
00971837  66 44 03 F0                     add r14w, ax
0097183B  41 83 FD 61                     cmp r13d, 0x61
0097183F  72 0E                           jb 0x14097184f
00971841  41 83 FD 7A                     cmp r13d, 0x7a
00971845  0F 87 A1 03 00 00               ja 0x140971bec
0097184B  66 44 03 E8                     add r13w, ax
0097184F  66 45 3B F5                     cmp r14w, r13w
00971853  0F 85 B6 02 00 00               jne 0x140971b0f
00971859  0F B7 4D B7                     movzx ecx, word ptr [rbp - 0x49]
0097185D  41 BB 01 00 00 00               mov r11d, 1
00971863  0F B7 45 BB                     movzx eax, word ptr [rbp - 0x45]
00971867  41 B9 FF FF 00 00               mov r9d, 0xffff
0097186D  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
00971871  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
00971875  66 41 03 C9                     add cx, r9w
00971879  66 41 03 C1                     add ax, r9w
0097187D  E9 63 FF FF FF                  jmp 0x1409717e5
00971882  44 3B F1                        cmp r14d, ecx
00971885  0F 84 AA F7 FF FF               je 0x140971035
0097188B  41 BE 4C 01 00 C0               mov r14d, 0xc000014c
00971891  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
00971899  45 8B CE                        mov r9d, r14d
0097189C  45 8B C5                        mov r8d, r13d
0097189F  33 D2                           xor edx, edx
009718A1  48 8B CF                        mov rcx, rdi
009718A4  E8 AB D6 AF FF                  call 0x14046ef54
009718A9  48 85 FF                        test rdi, rdi
009718AC  0F 84 FB F9 FF FF               je 0x1409712ad
009718B2  44 89 BF 18 01 00 00            mov dword ptr [rdi + 0x118], r15d
009718B9  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
009718C0  E9 E8 F9 FF FF                  jmp 0x1409712ad
009718C5  44 88 5D 7F                     mov byte ptr [rbp + 0x7f], r11b
009718C9  B9 4C 01 00 C0                  mov ecx, 0xc000014c
009718CE  44 8B F1                        mov r14d, ecx
009718D1  48 85 FF                        test rdi, rdi
009718D4  74 17                           je 0x1409718ed
009718D6  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
009718D9  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
009718DF  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
009718E6  4C 89 BF 20 01 00 00            mov qword ptr [rdi + 0x120], r15
009718ED  F7 45 6F 00 00 02 00            test dword ptr [rbp + 0x6f], 0x20000
009718F4  0F 85 CA 00 00 00               jne 0x1409719c4
009718FA  40 38 35 01 67 66 00            cmp byte ptr [rip + 0x666701], sil
00971901  0F 84 AF 00 00 00               je 0x1409719b6
00971907  44 8B C9                        mov r9d, ecx
0097190A  C7 44 24 20 98 00 00 00         mov dword ptr [rsp + 0x20], 0x98
00971912  48 8B CF                        mov rcx, rdi
00971915  45 8B C5                        mov r8d, r13d
00971918  41 8B D3                        mov edx, r11d
0097191B  E8 34 D6 AF FF                  call 0x14046ef54
00971920  45 33 C9                        xor r9d, r9d
00971923  45 33 C0                        xor r8d, r8d
00971926  41 8B D4                        mov edx, r12d
00971929  48 8B CB                        mov rcx, rbx
0097192C  E8 4F 67 EE FF                  call 0x140858080
00971931  44 8B F0                        mov r14d, eax
00971934  85 C0                           test eax, eax
00971936  0F 88 D1 03 00 00               js 0x140971d0d
0097193C  B8 FD FF 00 00                  mov eax, 0xfffd
00971941  41 BB 01 00 00 00               mov r11d, 1
00971947  66 41 21 47 10                  and word ptr [r15 + 0x10], ax
0097194C  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00971950  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
00971957  E9 9F F7 FF FF                  jmp 0x1409710fb
0097195C  0F B7 C0                        movzx eax, ax
0097195F  41 BD 0F 00 00 00               mov r13d, 0xf
00971965  0F B7 C9                        movzx ecx, cx
00971968  2B C8                           sub ecx, eax
0097196A  85 C9                           test ecx, ecx
0097196C  0F 85 A3 01 00 00               jne 0x140971b15
00971972  41 83 7F 0C 06                  cmp dword ptr [r15 + 0xc], 6
00971977  0F 84 A1 75 1B 00               je 0x140b28f1e
0097197D  41 F6 47 10 02                  test byte ptr [r15 + 0x10], 2
00971982  0F 85 96 75 1B 00               jne 0x140b28f1e
00971988  C7 44 24 20 B0 00 00 00         mov dword ptr [rsp + 0x20], 0xb0
00971990  E9 9F 01 00 00                  jmp 0x140971b34
00971995  E8 16 33 EE FF                  call 0x140854cb0
0097199A  E9 CE FD FF FF                  jmp 0x14097176d
0097199F  41 0F B7 CE                     movzx ecx, r14w
009719A3  E8 48 D7 EE FF                  call 0x14085f0f0
009719A8  44 0F B7 F0                     movzx r14d, ax
009719AC  B8 E0 FF 00 00                  mov eax, 0xffe0
009719B1  E9 85 FE FF FF                  jmp 0x14097183b
009719B6  8B 05 A4 62 58 00               mov eax, dword ptr [rip + 0x5862a4]
009719BC  A8 06                           test al, 6
009719BE  0F 85 43 FF FF FF               jne 0x140971907
009719C4  44 8B C9                        mov r9d, ecx
009719C7  C7 44 24 20 9C 00 00 00         mov dword ptr [rsp + 0x20], 0x9c
009719CF  48 8B CF                        mov rcx, rdi
009719D2  45 8B C5                        mov r8d, r13d
009719D5  33 D2                           xor edx, edx
009719D7  E8 78 D5 AF FF                  call 0x14046ef54
009719DC  E9 87 01 00 00                  jmp 0x140971b68
009719E1  41 BF 01 00 00 00               mov r15d, 1
009719E7  C7 44 24 20 60 01 00 00         mov dword ptr [rsp + 0x20], 0x160
009719EF  B9 4C 01 00 C0                  mov ecx, 0xc000014c
009719F4  44 88 7D 7F                     mov byte ptr [rbp + 0x7f], r15b
009719F8  44 8B F1                        mov r14d, ecx
009719FB  44 8B C9                        mov r9d, ecx
009719FE  41 8B D7                        mov edx, r15d
00971A01  48 8B CF                        mov rcx, rdi
00971A04  45 8D 47 0E                     lea r8d, [r15 + 0xe]
00971A08  E8 47 D5 AF FF                  call 0x14046ef54
00971A0D  48 85 FF                        test rdi, rdi
00971A10  0F 85 37 02 00 00               jne 0x140971c4d
00971A16  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00971A1A  48 8B CB                        mov rcx, rbx
00971A1D  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
00971A24  0F 85 86 01 00 00               jne 0x140971bb0
00971A2A  E8 11 45 EE FF                  call 0x140855f40
00971A2F  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00971A33  48 8B CB                        mov rcx, rbx
00971A36  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
00971A3D  0F 85 77 01 00 00               jne 0x140971bba
00971A43  E8 F8 44 EE FF                  call 0x140855f40
00971A48  48 8D 55 97                     lea rdx, [rbp - 0x69]
00971A4C  48 8B CB                        mov rcx, rbx
00971A4F  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
00971A56  0F 85 68 01 00 00               jne 0x140971bc4
00971A5C  E8 DF 44 EE FF                  call 0x140855f40
00971A61  41 BD 0F 00 00 00               mov r13d, 0xf
00971A67  E9 9E FA FF FF                  jmp 0x14097150a
00971A6C  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00971A70  44 84 B3 8C 00 00 00            test byte ptr [rbx + 0x8c], r14b
00971A77  0F 85 51 01 00 00               jne 0x140971bce
00971A7D  E8 BE 44 EE FF                  call 0x140855f40
00971A82  E9 E2 F7 FF FF                  jmp 0x140971269
00971A87  B8 4C 01 00 C0                  mov eax, 0xc000014c
00971A8C  44 88 5D 7F                     mov byte ptr [rbp + 0x7f], r11b
00971A90  41 BD 0F 00 00 00               mov r13d, 0xf
00971A96  C7 44 24 20 10 01 00 00         mov dword ptr [rsp + 0x20], 0x110
00971A9E  44 8B C8                        mov r9d, eax
00971AA1  45 8B C5                        mov r8d, r13d
00971AA4  41 8B D3                        mov edx, r11d
00971AA7  48 8B CF                        mov rcx, rdi
00971AAA  44 8B F0                        mov r14d, eax
00971AAD  45 8A E3                        mov r12b, r11b
00971AB0  E8 9F D4 AF FF                  call 0x14046ef54
00971AB5  48 85 FF                        test rdi, rdi
00971AB8  0F 85 BF 01 00 00               jne 0x140971c7d
00971ABE  41 BF 01 00 00 00               mov r15d, 1
00971AC4  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00971AC8  48 8B CB                        mov rcx, rbx
00971ACB  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
00971AD2  0F 85 00 01 00 00               jne 0x140971bd8
00971AD8  E8 63 44 EE FF                  call 0x140855f40
00971ADD  48 8D 55 97                     lea rdx, [rbp - 0x69]
00971AE1  48 8B CB                        mov rcx, rbx
00971AE4  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
00971AEB  0F 85 F1 00 00 00               jne 0x140971be2
00971AF1  E8 4A 44 EE FF                  call 0x140855f40
00971AF6  E9 73 F8 FF FF                  jmp 0x14097136e
00971AFB  E8 B0 31 EE FF                  call 0x140854cb0
00971B00  E9 BB FB FF FF                  jmp 0x1409716c0
00971B05  E8 16 B1 EE FF                  call 0x14085cc20
00971B0A  E9 42 F8 FF FF                  jmp 0x140971351
00971B0F  41 BD 0F 00 00 00               mov r13d, 0xf
00971B15  C7 44 24 20 A0 00 00 00         mov dword ptr [rsp + 0x20], 0xa0
00971B1D  EB 15                           jmp 0x140971b34
00971B1F  B8 FF FF 00 00                  mov eax, 0xffff
00971B24  3B C8                           cmp ecx, eax
00971B26  0F 86 2A F6 FF FF               jbe 0x140971156
00971B2C  C7 44 24 20 D0 00 00 00         mov dword ptr [rsp + 0x20], 0xd0
00971B34  B8 4C 01 00 C0                  mov eax, 0xc000014c
00971B39  45 8B C5                        mov r8d, r13d
00971B3C  44 8B C8                        mov r9d, eax
00971B3F  33 D2                           xor edx, edx
00971B41  48 8B CF                        mov rcx, rdi
00971B44  44 8B F0                        mov r14d, eax
00971B47  E8 08 D4 AF FF                  call 0x14046ef54
00971B4C  48 85 FF                        test rdi, rdi
00971B4F  74 17                           je 0x140971b68
00971B51  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00971B54  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
00971B5A  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
00971B61  4C 89 BF 20 01 00 00            mov qword ptr [rdi + 0x120], r15
00971B68  48 8D 55 97                     lea rdx, [rbp - 0x69]
00971B6C  B9 01 00 00 00                  mov ecx, 1
00971B71  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00971B77  48 8B CB                        mov rcx, rbx
00971B7A  74 0A                           je 0x140971b86
00971B7C  E8 9F B0 EE FF                  call 0x14085cc20
00971B81  E9 27 F7 FF FF                  jmp 0x1409712ad
00971B86  E8 B5 43 EE FF                  call 0x140855f40
00971B8B  E9 1D F7 FF FF                  jmp 0x1409712ad
00971B90  E8 8B B0 EE FF                  call 0x14085cc20
00971B95  E9 0B FC FF FF                  jmp 0x1409717a5
00971B9A  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00971BA0  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00971BA8  45 8B F1                        mov r14d, r9d
00971BAB  E9 E8 F8 FF FF                  jmp 0x140971498
00971BB0  E8 6B B0 EE FF                  call 0x14085cc20
00971BB5  E9 75 FE FF FF                  jmp 0x140971a2f
00971BBA  E8 61 B0 EE FF                  call 0x14085cc20
00971BBF  E9 84 FE FF FF                  jmp 0x140971a48
00971BC4  E8 57 B0 EE FF                  call 0x14085cc20
00971BC9  E9 93 FE FF FF                  jmp 0x140971a61
00971BCE  E8 4D B0 EE FF                  call 0x14085cc20
00971BD3  E9 91 F6 FF FF                  jmp 0x140971269
00971BD8  E8 43 B0 EE FF                  call 0x14085cc20
00971BDD  E9 FB FE FF FF                  jmp 0x140971add
00971BE2  E8 39 B0 EE FF                  call 0x14085cc20
00971BE7  E9 82 F7 FF FF                  jmp 0x14097136e
00971BEC  41 0F B7 CD                     movzx ecx, r13w
00971BF0  E8 FB D4 EE FF                  call 0x14085f0f0
00971BF5  44 0F B7 E8                     movzx r13d, ax
00971BF9  E9 51 FC FF FF                  jmp 0x14097184f
00971BFE  85 C9                           test ecx, ecx
00971C00  0F 84 3C F6 FF FF               je 0x140971242
00971C06  E9 EB F5 FF FF                  jmp 0x1409711f6
00971C0B  41 84 CB                        test r11b, cl
00971C0E  0F 84 0B FF FF FF               je 0x140971b1f
00971C14  C7 44 24 20 C0 00 00 00         mov dword ptr [rsp + 0x20], 0xc0
00971C1C  E9 13 FF FF FF                  jmp 0x140971b34
00971C21  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
00971C25  48 8D 0D D4 7F 66 00            lea rcx, [rip + 0x667fd4]
00971C2C  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00971C30  66 89 45 D7                     mov word ptr [rbp - 0x29], ax
00971C34  45 33 C0                        xor r8d, r8d
00971C37  66 89 45 D9                     mov word ptr [rbp - 0x27], ax
00971C3B  E8 00 57 0A 00                  call 0x140a17340
00971C40  8B C8                           mov ecx, eax
00971C42  41 BB 01 00 00 00               mov r11d, 1
00971C48  E9 1D FD FF FF                  jmp 0x14097196a
00971C4D  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00971C51  41 8B C4                        mov eax, r12d
00971C54  44 89 A7 18 01 00 00            mov dword ptr [rdi + 0x118], r12d
00971C5B  8B 04 81                        mov eax, dword ptr [rcx + rax*4]
00971C5E  89 87 1C 01 00 00               mov dword ptr [rdi + 0x11c], eax
00971C64  4C 89 AF 20 01 00 00            mov qword ptr [rdi + 0x120], r13
00971C6B  E9 A6 FD FF FF                  jmp 0x140971a16
00971C70  C7 44 24 20 50 01 00 00         mov dword ptr [rsp + 0x20], 0x150
00971C78  E9 27 73 1B 00                  jmp 0x140b28fa4
00971C7D  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00971C80  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
00971C86  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
00971C89  89 87 1C 01 00 00               mov dword ptr [rdi + 0x11c], eax
00971C8F  E9 2A FE FF FF                  jmp 0x140971abe
00971C94  C7 44 24 20 90 00 00 00         mov dword ptr [rsp + 0x20], 0x90
00971C9C  E9 1C 74 1B 00                  jmp 0x140b290bd
00971CA1  C7 44 24 20 88 00 00 00         mov dword ptr [rsp + 0x20], 0x88
00971CA9  E9 0F 74 1B 00                  jmp 0x140b290bd
00971CAE  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
00971CB6  E9 02 74 1B 00                  jmp 0x140b290bd
00971CBB  BA 4C 01 00 C0                  mov edx, 0xc000014c
00971CC0  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00971CC3  44 8B F2                        mov r14d, edx
00971CC6  C7 44 24 20 60 00 00 00         mov dword ptr [rsp + 0x20], 0x60
00971CCE  44 8B CA                        mov r9d, edx
00971CD1  45 8B C5                        mov r8d, r13d
00971CD4  8B D1                           mov edx, ecx
00971CD6  48 8B CF                        mov rcx, rdi
00971CD9  E8 76 D2 AF FF                  call 0x14046ef54
00971CDE  48 85 FF                        test rdi, rdi
00971CE1  0F 84 E0 73 1B 00               je 0x140b290c7
00971CE7  44 89 BF 18 01 00 00            mov dword ptr [rdi + 0x118], r15d
00971CEE  44 89 A7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r12d
00971CF5  E9 CD 73 1B 00                  jmp 0x140b290c7
00971CFA  83 8F 1C 01 00 00 FF            or dword ptr [rdi + 0x11c], 0xffffffff
00971D01  44 89 BF 18 01 00 00            mov dword ptr [rdi + 0x118], r15d
00971D08  E9 09 F9 FF FF                  jmp 0x140971616
00971D0D  BE 01 00 00 00                  mov esi, 1
00971D12  C7 44 24 20 9A 00 00 00         mov dword ptr [rsp + 0x20], 0x9a
00971D1A  8B D6                           mov edx, esi
00971D1C  44 8B C8                        mov r9d, eax
00971D1F  45 8B C5                        mov r8d, r13d
00971D22  48 8B CF                        mov rcx, rdi
00971D25  E8 2A D2 AF FF                  call 0x14046ef54
00971D2A  40 84 B3 8C 00 00 00            test byte ptr [rbx + 0x8c], sil
00971D31  48 8D 55 97                     lea rdx, [rbp - 0x69]
00971D35  E9 3D FE FF FF                  jmp 0x140971b77
00971D3A  33 D2                           xor edx, edx
00971D3C  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
00971D44  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00971D4A  48 8B CF                        mov rcx, rdi
00971D4D  45 8B F1                        mov r14d, r9d
00971D50  44 8D 42 0F                     lea r8d, [rdx + 0xf]
00971D54  E8 FB D1 AF FF                  call 0x14046ef54
00971D59  48 85 FF                        test rdi, rdi
00971D5C  0F 84 06 FE FF FF               je 0x140971b68
00971D62  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00971D65  89 87 18 01 00 00               mov dword ptr [rdi + 0x118], eax
00971D6B  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
00971D6E  89 87 1C 01 00 00               mov dword ptr [rdi + 0x11c], eax
00971D74  E9 EF FD FF FF                  jmp 0x140971b68
00971D79  33 D2                           xor edx, edx
00971D7B  C7 44 24 20 70 01 00 00         mov dword ptr [rsp + 0x20], 0x170
00971D83  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00971D89  48 8B CF                        mov rcx, rdi
00971D8C  45 8B F1                        mov r14d, r9d
00971D8F  44 8D 42 0F                     lea r8d, [rdx + 0xf]
00971D93  E8 BC D1 AF FF                  call 0x14046ef54
00971D98  48 85 FF                        test rdi, rdi
00971D9B  0F 84 2F 73 1B 00               je 0x140b290d0
00971DA1  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00971DA5  41 8B C4                        mov eax, r12d
00971DA8  44 89 A7 18 01 00 00            mov dword ptr [rdi + 0x118], r12d
00971DAF  8B 04 81                        mov eax, dword ptr [rcx + rax*4]
00971DB2  89 87 1C 01 00 00               mov dword ptr [rdi + 0x11c], eax
00971DB8  4C 89 AF 20 01 00 00            mov qword ptr [rdi + 0x120], r13
00971DBF  E9 0C 73 1B 00                  jmp 0x140b290d0
00971DC4  33 D2                           xor edx, edx
00971DC6  C7 44 24 20 30 01 00 00         mov dword ptr [rsp + 0x20], 0x130
00971DCE  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00971DD4  48 8B CF                        mov rcx, rdi
00971DD7  45 8B F1                        mov r14d, r9d
00971DDA  44 8D 42 0F                     lea r8d, [rdx + 0xf]
00971DDE  E8 71 D1 AF FF                  call 0x14046ef54
00971DE3  48 85 FF                        test rdi, rdi
00971DE6  0F 85 07 73 1B 00               jne 0x140b290f3
00971DEC  E9 15 73 1B 00                  jmp 0x140b29106
00971DF1  B8 28 00 00 00                  mov eax, 0x28
00971DF6  E9 3C 73 1B 00                  jmp 0x140b29137
00971DFB  B8 18 00 00 00                  mov eax, 0x18
00971E00  E9 32 73 1B 00                  jmp 0x140b29137
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCheckValueList(__int64 a1, unsigned __int8 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int8 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (160);
    v_rsi = 0;
    *(unsigned int *)(v_rsp - 63 - 97) = 0;
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 63 - 101) = 0;
    *(unsigned int *)(v_rsp - 63 - 105) = a4;
    *(unsigned int *)(v_rsp - 63 - 89) = a4;
    *(unsigned int *)(v_rsp - 63 - 85) = 0;
    *(unsigned int *)(v_rsp - 63 - 57) = a4;
    *(unsigned int *)(v_rsp - 63 - 53) = 0;
    *(unsigned int *)(v_rsp - 63 - 65) = a4;
    *(unsigned int *)(v_rsp - 63 - 61) = 0;
    *(unsigned int *)(v_rsp - 63 - 81) = a4;
    *(unsigned int *)(v_rsp - 63 - 77) = 0;
    *(unsigned __int8 *)(v_rsp - 63 + 127) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = v_xmm0;
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 272) = a3;
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = a4;
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = 0;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = 0;
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 135)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 143)) = 0;
loc_00971016:
    if (0 >= ((unsigned int)((unsigned int)(a4)))) goto loc_009712A0;
    *(unsigned __int64 *)(v_rsp - 63 - 9) = a3 + 0 * 4;
    if (a2 != 0) goto loc_00971882;
loc_00971035:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 0 * 4)))) == a4) goto loc_009715E9;
    result = HvIsCellAllocated(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 0 * 4)))), *(unsigned __int64 *)(v_rsp - 63 + 119), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00971CBB;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00971296;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 0 * 4)))), v_rsp - 63 - 105, a4);
loc_00971075:
    if (result == 0) goto loc_0097151C;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((unsigned int)(result)) < 20) goto loc_00971CAE;
    if ((*(unsigned __int16 *)(result)) != ((unsigned __int16)((unsigned int)(0x6B76ULL)))) goto loc_00971CA1;
    if (((unsigned int)(*(unsigned __int16 *)(result + 2) + 20)) < 20) goto loc_00971C94;
    if (((unsigned int)(*(unsigned __int16 *)(result + 2) + 20)) > ((unsigned int)(result))) goto loc_00971C94;
    if (((1) & ((unsigned __int8)(*(unsigned __int16 *)(result + 16)))) == 0) goto loc_009712D6;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 2))) > ((unsigned __int16)((unsigned int)(0x3FFFULL)))) goto loc_009714AA;
loc_009710DD:
    a1 = (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 144)) & (2)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_009718C5;
loc_009710FB:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 + 79)) != 0) goto loc_009717BB;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 2))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(result + 2)))));
    a2 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 16))) & (1));
    if (condition_is_equal) { result = (unsigned __int16)(*(unsigned __int16 *)(result + 2)); }
    result = (unsigned __int16)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 135))) < ((unsigned int)((unsigned __int16)(result)))) {
        result = (unsigned __int16)(*(unsigned __int16 *)(result + 2));
        result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
        if (a2 == 0) { result = (unsigned __int16)(*(unsigned __int16 *)(result + 2)); }
        result = (unsigned __int16)(result);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 135)) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rsp - 63 - 69) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 + 79)) != 0) goto loc_00971C0B;
loc_00971156:
    if ((((unsigned __int8)(*(unsigned __int16 *)(result + 16))) & (2)) != 0) goto loc_009711D1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < 0x80000000ULL) goto loc_009711E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)) - 2147483648)) > 4) goto loc_00971621;
loc_00971173:
    result = (unsigned int)(*(unsigned int *)(result + 4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) >= 0x80000000ULL) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) + (0x80000000ULL));
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 143))) < ((unsigned int)(result))) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 143)) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00971472;
    result = HvpReleaseCellPaged(a1, v_rsp - 63 - 105, *(unsigned __int16 *)(result + 16), *(unsigned __int8 *)(v_rsp - 63 + 79));
loc_009711A9:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 - 97))) + (1));
    *(unsigned int *)(v_rsp - 63 - 97) = (unsigned int)(v_r15);
loc_009711C1:
    a4 = (unsigned int)((*(unsigned __int8 *)(v_rsp - 63 + 79)) | (0xFFFFFFFFULL));
    goto loc_00971016;
loc_009711D1:
    if (1 != 0) goto loc_0097130A;
    if ((*(unsigned int *)(v_r15 + 12)) != 0) goto loc_0097130A;
loc_009711E3:
    *(unsigned int *)(v_rsp - 63 - 73) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 8)));
    if (1 == 0) goto loc_009712FA;
loc_009711F6:
    result = HvIsCellAllocated(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 8)))), *(unsigned __int64 *)(v_rsp - 63 + 119), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00971551;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_009712CC;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 8)))), v_rsp - 63 - 89, a4);
loc_0097122D:
    if (result == 0) goto loc_00971D3A;
loc_00971242:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 69)))) > 0x3FD8ULL) goto loc_00971642;
loc_0097124E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 69))) == 0) goto loc_00971263;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 69)))) > ((unsigned int)(result))) goto loc_0097157E;
loc_00971263:
loc_00971269:
    if (result == 0) goto loc_00971287;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00971574;
    result = HvpReleaseCellPaged(a1, v_rsp - 63 - 89, v_rsp - 63 - 89, a4);
loc_00971287:
    goto loc_00971173;
loc_00971296:
    result = HvpGetCellPaged(a1, v_rsp - 63 - 89, v_rsp - 63 - 89, a4);
    goto loc_00971075;
loc_009712A0:
    v_r12 = (unsigned __int8)(-(*(unsigned __int8 *)(v_rsp - 63 + 127)));
    v_r14 = (unsigned int)((1) & (0x8000002AULL));
loc_009712AD:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)((unsigned int)(v_r14));
loc_009712CC:
    result = HvpGetCellPaged(a1, v_rsp - 63 - 89, v_rsp - 63 - 89, a4);
    goto loc_0097122D;
loc_009712D6:
    if ((((unsigned __int8)(15 - 14)) & ((unsigned __int8)(v_rsp - 63 - 89))) != 0) goto loc_00971512;
    if (((unsigned __int16)(v_rsp - 63 - 89)) <= ((unsigned __int16)((unsigned int)(0x7FFFULL)))) goto loc_009710DD;
    v_stack_p20 = 150;
    goto loc_009714B2;
loc_009712FA:
    if (((unsigned int)(v_r14)) == -1) goto loc_00971BFE;
loc_0097130A:
    v_stack_p20 = 224;
loc_00971312:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = (unsigned __int8)(15 - 14);
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(15 - 14)), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) {
        result = *(unsigned int *)(v_rsp - 63 - 97);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)(result);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)(v_r12);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = v_r15;
    }
loc_00971351:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971638;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_0097136A:
loc_0097136E:
    if (((*(unsigned int *)(v_rsp - 63 + 111)) & (0x20000ULL)) != 0) goto loc_0097148A;
    if ((*(unsigned __int8 *)(v_rip + 6712448)) == 0) goto loc_0097147C;
loc_00971388:
    v_stack_p20 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), 1, 15, (unsigned int)(0xC000014CULL));
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) == 0) goto loc_00971468;
    result = HvpGetCellFlat(v_stack_p8, (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)), v_rsp - 63 - 57, (unsigned int)(0xC000014CULL));
loc_009713BC:
    if (result == 0) goto loc_00971B9A;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_p8, (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)), a3, a4);
    if (sign_flag) goto loc_00971DFB;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_p8, (unsigned int)(*(unsigned int *)(result + 40)), a3, a4);
    if (sign_flag) goto loc_00971DF1;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 + 95))) + ((unsigned int)(result)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 97)))));
    a3 = (a3) << (2);
    *(unsigned int *)(v_rsp - 63 + 95) = (unsigned int)(v_r14);
    result = memcpy(*(unsigned __int64 *)(v_rsp - 63 - 9), *(unsigned __int64 *)(v_rsp - 63 + 87) + (unsigned int)(*(unsigned int *)(v_rsp - 63 - 97)) + 1 * 4, a3, a4);
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_0097162E;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 57, a3, a4);
loc_0097145E:
    goto loc_009711C1;
loc_00971468:
    result = HvpGetCellPaged(1, v_rsp - 63 - 57, a3, a4);
    goto loc_009713BC;
loc_00971472:
    result = HvpReleaseCellFlat(1, v_rsp - 63 - 57, a3, a4);
    goto loc_009711A9;
loc_0097147C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5793758)))) & (6)) != 0) goto loc_00971388;
loc_0097148A:
    v_stack_p20 = 48;
loc_00971498:
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, 15, (unsigned int)(0xC000014CULL));
    goto loc_009712AD;
loc_009714AA:
    v_stack_p20 = 146;
loc_009714B2:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = (unsigned __int8)(15 - 14);
loc_009714C4:
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(15 - 14)), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) {
        result = *(unsigned int *)(v_rsp - 63 - 97);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)(result);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)(*(unsigned __int8 *)(v_rsp - 63 + 127));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = (unsigned int)(*(unsigned int *)(v_rsp - 63 - 97));
    }
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_009717B1;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_0097150A:
    goto loc_0097136E;
loc_00971512:
    v_stack_p20 = 148;
    goto loc_009714B2;
loc_0097151C:
    v_stack_p20 = 112;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, 15, (unsigned int)(0xC000009AULL));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) == 0) goto loc_009712AD;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 97)));
    goto loc_009718B9;
loc_00971551:
    v_stack_p20 = 240;
    *(unsigned __int8 *)(v_rsp - 63 + 127) = (unsigned __int8)(*(unsigned __int64 *)(v_rsp - 63 + 127));
    goto loc_009714C4;
loc_00971574:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 + 127))), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00971287;
loc_0097157E:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = (unsigned __int8)(15 - 14);
    v_stack_p20 = 400;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(15 - 14)), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) {
        result = *(unsigned int *)(v_rsp - 63 - 97);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)(result);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = 1;
    }
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971B05;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 89, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00971351;
loc_009715E9:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = (unsigned __int8)(v_stack_p8);
    v_stack_p20 = 80;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(v_stack_p8)), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) goto loc_00971CFA;
loc_00971616:
    goto loc_0097136E;
loc_00971621:
    v_stack_p20 = 416;
    goto loc_00971312;
loc_0097162E:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(v_stack_p8)), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0097145E;
loc_00971638:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(v_stack_p8)), 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0097136A;
loc_00971642:
    if ((*(unsigned int *)(v_stack_p8 + 220)) < 4) goto loc_0097124E;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(15 - 4)));
    if (((unsigned int)(result)) < 8) goto loc_00971A87;
    if ((*(unsigned __int16 *)(15)) != ((unsigned __int16)((unsigned int)(0x6264ULL)))) goto loc_00971A87;
    if ((*(unsigned __int16 *)(15 + 2)) == 0) goto loc_00971A87;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(15 + 4)))) == -1) goto loc_00971A87;
    result = HvIsCellAllocated(v_stack_p8, (unsigned int)(*(unsigned int *)(15 + 4)), *(unsigned __int64 *)(v_rsp - 63 + 119), (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) == 0) goto loc_00971AFB;
    result = HvpGetCellFlat(v_stack_p8, (unsigned int)(*(unsigned int *)(15 + 4)), v_rsp - 63 - 81, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_009716C0:
    *(unsigned __int64 *)(v_rsp - 63 - 49) = result;
    if (result == 0) goto loc_00971DC4;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(15 + 2)))) << (2);
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 - 69))) + (0x3FD7ULL));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(*(unsigned int *)(15 + 4)))));
    a1 = (unsigned int)((a1) >> (1));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(*(unsigned int *)(15 + 4)))));
    a1 = (unsigned int)((a1) >> (13));
    if (((unsigned int)(*(unsigned __int16 *)(15 + 2))) != ((unsigned int)(a1))) goto loc_00971C70;
loc_0097171D:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(15 + 2)))) goto loc_00971A6C;
    result = HvIsCellAllocated(v_stack_p8, (unsigned int)(*(unsigned int *)(result + 0 * 4)), *(unsigned __int64 *)(v_rsp - 63 + 119), result);
    if ((unsigned __int8)(result) == 0) goto loc_009719E1;
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) == 0) goto loc_00971995;
    result = HvpGetCellFlat(v_stack_p8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 49) + 0 * 4)), v_rsp - 63 - 65, result);
loc_0097176D:
    if (result == 0) goto loc_00971D79;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971B90;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 65, v_rsp - 63 - 65, result);
loc_009717A5:
    v_r12 = (unsigned int)((0) + (1));
    goto loc_0097171D;
loc_009717B1:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 65, v_rsp - 63 - 65, *(unsigned __int64 *)(v_rsp - 63 - 49));
    goto loc_0097150A;
loc_009717BB:
    if (((*(unsigned __int8 *)(1 + 16)) & ((unsigned __int8)(15 - 14))) == 0) goto loc_00971C21;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_rip + 6718507)) >> (1));
loc_009717E5:
    *(unsigned __int16 *)(v_rsp - 63 - 69) = (unsigned __int16)(*(unsigned __int16 *)(1 + 2));
    *(unsigned __int16 *)(v_rsp - 63 - 73) = (unsigned __int16)(a1);
    if ((unsigned __int16)(a1) == 0) goto loc_0097195C;
    if ((unsigned __int16)(*(unsigned __int16 *)(1 + 2)) == 0) goto loc_0097195C;
    a3 = (*(unsigned __int64 *)(v_rip + 6718502)) + (2);
    a2 = (1 + 20) + (15 - 14);
    *(unsigned __int64 *)(v_rsp - 63 - 17) = a3;
    *(unsigned __int64 *)(v_rsp - 63 - 25) = a2;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6718502)))) == ((unsigned __int16)(*(unsigned __int8 *)(1 + 20)))) goto loc_00971875;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6718502)))) < 97) goto loc_009719AC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6718502)))) > 122) goto loc_0097199F;
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6718502))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0097183B:
    if (((unsigned int)(*(unsigned __int8 *)(1 + 20))) < 97) goto loc_0097184F;
    if (((unsigned int)(*(unsigned __int8 *)(1 + 20))) > 122) goto loc_00971BEC;
    v_r13 = (unsigned __int16)((*(unsigned __int8 *)(1 + 20)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0097184F:
    if (((unsigned __int16)(v_r14)) != ((unsigned __int16)(v_r13))) goto loc_00971B0F;
loc_00971875:
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 63 - 73)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 63 - 69)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_009717E5;
loc_00971882:
    if (((unsigned int)(v_r14)) == ((unsigned int)(a1))) goto loc_00971035;
    v_stack_p20 = 64;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) == 0) goto loc_009712AD;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = 1;
loc_009718B9:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)(v_r12);
    goto loc_009712AD;
loc_009718C5:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = 1;
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) {
        result = *(unsigned int *)(v_rsp - 63 - 97);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)(result);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)(v_r12);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = 1;
    }
    if (((*(unsigned int *)(v_rsp - 63 + 111)) & (0x20000ULL)) != 0) goto loc_009719C4;
    if ((*(unsigned __int8 *)(v_rip + 6711041)) == 0) goto loc_009719B6;
loc_00971907:
    v_stack_p20 = 152;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), 1, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_p8, (unsigned int)((unsigned int)(v_r12)), a3, a4);
    if (sign_flag) goto loc_00971D0D;
    goto loc_009710FB;
loc_0097195C:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_p8)) - ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(v_stack_p8 + 64)))));
loc_0097196A:
    if ((unsigned int)(a1) != 0) goto loc_00971B15;
    v_stack_p20 = 176;
    goto loc_00971B34;
loc_00971995:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)(v_r12)), a3, a4);
    goto loc_0097176D;
loc_0097199F:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)((unsigned int)(result))), (unsigned int)((unsigned int)(v_r12)), a3, a4);
loc_009719AC:
    goto loc_0097183B;
loc_009719B6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5792420)))) & (6)) != 0) goto loc_00971907;
loc_009719C4:
    v_stack_p20 = 156;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, 15, (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)((unsigned int)(result))))));
    goto loc_00971B68;
loc_009719E1:
    v_stack_p20 = 352;
    *(unsigned __int8 *)(v_rsp - 63 + 127) = 1;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), 1, 1 + 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) goto loc_00971C4D;
loc_00971A16:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971BB0;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 81, 1 + 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_00971A2F:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971BBA;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 89, 1 + 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_00971A48:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971BC4;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 105, 1 + 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_00971A61:
    goto loc_0097150A;
loc_00971A6C:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) != 0) goto loc_00971BCE;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 81, 1 + 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00971269;
loc_00971A87:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = 1;
    v_stack_p20 = 272;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), 1, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) goto loc_00971C7D;
loc_00971ABE:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971BD8;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 89, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_00971ADD:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00971BE2;
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0097136E;
loc_00971AFB:
    result = HvpGetCellPaged(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009716C0;
loc_00971B05:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00971351;
loc_00971B0F:
loc_00971B15:
    v_stack_p20 = 160;
    goto loc_00971B34;
loc_00971B1F:
    if (((unsigned int)(v_stack_p8)) <= ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_00971156;
    v_stack_p20 = 208;
loc_00971B34:
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) != 0) {
        result = *(unsigned int *)(v_rsp - 63 - 97);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)(result);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = 1;
    }
loc_00971B77:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) == 0) goto loc_00971B86;
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009712AD;
loc_00971B86:
    result = HvpReleaseCellPaged(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009712AD;
loc_00971B90:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009717A5;
loc_00971B9A:
    v_stack_p20 = 16;
    goto loc_00971498;
loc_00971BB0:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_00971A2F;
loc_00971BBA:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_00971A48;
loc_00971BC4:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_00971A61;
loc_00971BCE:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_00971269;
loc_00971BD8:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_00971ADD;
loc_00971BE2:
    result = HvpReleaseCellFlat(v_stack_p8, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_0097136E;
loc_00971BEC:
    result = RtlUpcaseUnicodeChar(15, v_rsp - 63 - 105, 15, (unsigned int)(0xC000009AULL));
    goto loc_0097184F;
loc_00971BFE:
    if (15 == 0) goto loc_00971242;
    goto loc_009711F6;
loc_00971C0B:
    if (((1) & (15)) == 0) goto loc_00971B1F;
    v_stack_p20 = 192;
    goto loc_00971B34;
loc_00971C21:
    *(unsigned __int64 *)(v_rsp - 63 - 33) = v_rsp - 63 - 105;
    *(unsigned __int16 *)(v_rsp - 63 - 41) = (unsigned __int16)(result);
    a3 = 0;
    *(unsigned __int16 *)(v_rsp - 63 - 39) = (unsigned __int16)(result);
    result = CmpCompareUnicodeString(v_rip + 6717396, v_rsp - 63 - 41, a3, (unsigned int)(0xC000009AULL));
    goto loc_0097196A;
loc_00971C4D:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 49) + 1 * 4)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = (unsigned __int16)(result);
    goto loc_00971A16;
loc_00971C70:
    v_stack_p20 = 336;
loc_00971C7D:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 97)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 73)));
    goto loc_00971ABE;
loc_00971C94:
    v_stack_p20 = 144;
loc_00971CA1:
    v_stack_p20 = 136;
loc_00971CAE:
    v_stack_p20 = 128;
loc_00971CBB:
    *(unsigned __int8 *)(v_rsp - 63 + 127) = (unsigned __int8)(*(unsigned __int64 *)(v_rsp - 63 - 49));
    v_stack_p20 = 96;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 49))), (unsigned int)((unsigned int)((unsigned __int16)(result))), (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = 1;
loc_00971CFA:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = 1;
    goto loc_00971616;
loc_00971D0D:
    v_stack_p20 = 154;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), 1, (unsigned int)((unsigned int)((unsigned __int16)(result))), (unsigned int)((unsigned int)(result)));
    goto loc_00971B77;
loc_00971D3A:
    a2 = 0;
    v_stack_p20 = 256;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, a2 + 15, (unsigned int)(0xC000009AULL));
    if (*(unsigned __int64 *)(v_rsp - 63 + 127) == 0) goto loc_00971B68;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 97)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 73)));
    goto loc_00971B68;
loc_00971D79:
    a2 = 0;
    v_stack_p20 = 368;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, a2 + 15, (unsigned int)(0xC000009AULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 280) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 284) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 49) + 1 * 4)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 127) + 288) = (unsigned __int16)(result);
loc_00971DC4:
    a2 = 0;
    v_stack_p20 = 304;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 63 + 127), a2, a2 + 15, (unsigned int)(0xC000009AULL));
loc_00971DF1:
loc_00971DFB:
}
```

## 5. (Beta) C Style

```c
int64_t CmpCheckValueList(void *Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint8_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (160);
    local_rsi = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x61) = 0;
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x3F - 0x65) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x69) = Arg4;
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = Arg4;
    *(uint32_t *)(local_rsp - 0x3F - 0x55) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x39) = Arg4;
    *(uint32_t *)(local_rsp - 0x3F - 0x35) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x41) = Arg4;
    *(uint32_t *)(local_rsp - 0x3F - 0x3D) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x51) = Arg4;
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = 0;
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = v_xmm0;
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x110) = Arg3;
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = Arg4;
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = 0;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = 0;
    }
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87)) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F)) = 0;
loc_00971016:
    if (0 >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_009712A0;
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = Arg3 + 0 * 4;
    if (Arg2 != 0) goto loc_00971882;
loc_00971035:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x0 * 4)))) == Arg4) goto loc_009715E9;
    result = HvIsCellAllocated(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x0 * 4)))), *(uint64_t *)(local_rsp - 0x3F + 0x77), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00971CBB;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00971296;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x0 * 4)))), local_rsp - 63 - 105, Arg4);
loc_00971075:
    if (result == 0) goto loc_0097151C;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((uint32_t)(result)) < 20) goto loc_00971CAE;
    if ((*(uint16_t *)(result)) != ((uint16_t)((uint32_t)(0x6B76ULL)))) goto loc_00971CA1;
    if (((uint32_t)(*(uint16_t *)(result + 0x2) + 20)) < 20) goto loc_00971C94;
    if (((uint32_t)(*(uint16_t *)(result + 0x2) + 20)) > ((uint32_t)(result))) goto loc_00971C94;
    if (((1) & ((uint8_t)(*(uint16_t *)(result + 0x10)))) == 0) goto loc_009712D6;
    if (((uint16_t)(*(uint16_t *)(result + 0x2))) > ((uint16_t)((uint32_t)(0x3FFFULL)))) goto loc_009714AA;
loc_009710DD:
    Arg1 = (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0x90)) & (2)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_009718C5;
loc_009710FB:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F + 0x4F)) != 0) goto loc_009717BB;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x2))) + ((uint16_t)((uint16_t)(*(uint16_t *)(result + 0x2)))));
    Arg2 = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x10))) & (1));
    if (condition_is_equal) { result = (uint16_t)(*(uint16_t *)(result + 0x2)); }
    result = (uint16_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87))) < ((uint32_t)((uint16_t)(result)))) {
        result = (uint16_t)(*(uint16_t *)(result + 0x2));
        result = (uint16_t)((result) + ((uint16_t)(result)));
        if (Arg2 == 0) { result = (uint16_t)(*(uint16_t *)(result + 0x2)); }
        result = (uint16_t)(result);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87)) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rsp - 0x3F - 0x45) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F + 0x4F)) != 0) goto loc_00971C0B;
loc_00971156:
    if ((((uint8_t)(*(uint16_t *)(result + 0x10))) & (2)) != 0) goto loc_009711D1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < 0x80000000ULL) goto loc_009711E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648)) > 4) goto loc_00971621;
loc_00971173:
    result = (uint32_t)(*(uint32_t *)(result + 0x4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) >= 0x80000000ULL) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) + (0x80000000ULL));
    }
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F))) < ((uint32_t)(result))) {
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x8F)) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00971472;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 63 - 105, *(uint16_t *)(result + 0x10), *(uint8_t *)(local_rsp - 0x3F + 0x4F));
loc_009711A9:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61))) + (1));
    *(uint32_t *)(local_rsp - 0x3F - 0x61) = (uint32_t)(local_r15);
loc_009711C1:
    Arg4 = (uint32_t)((*(uint8_t *)(local_rsp - 0x3F + 0x4F)) | (0xFFFFFFFFULL));
    goto loc_00971016;
loc_009711D1:
    if (1 != 0) goto loc_0097130A;
    if ((*(uint32_t *)(local_r15 + 0xC)) != 0) goto loc_0097130A;
loc_009711E3:
    *(uint32_t *)(local_rsp - 0x3F - 0x49) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x8)));
    if (1 == 0) goto loc_009712FA;
loc_009711F6:
    result = HvIsCellAllocated(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x8)))), *(uint64_t *)(local_rsp - 0x3F + 0x77), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00971551;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_009712CC;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x8)))), local_rsp - 63 - 89, Arg4);
loc_0097122D:
    if (result == 0) goto loc_00971D3A;
loc_00971242:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x45)))) > 0x3FD8ULL) goto loc_00971642;
loc_0097124E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x45))) == 0) goto loc_00971263;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x45)))) > ((uint32_t)(result))) goto loc_0097157E;
loc_00971263:
loc_00971269:
    if (result == 0) goto loc_00971287;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00971574;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 63 - 89, local_rsp - 63 - 89, Arg4);
loc_00971287:
    goto loc_00971173;
loc_00971296:
    result = HvpGetCellPaged(Arg1, local_rsp - 63 - 89, local_rsp - 63 - 89, Arg4);
    goto loc_00971075;
loc_009712A0:
    local_r12 = (uint8_t)(-(*(uint8_t *)(local_rsp - 0x3F + 0x7F)));
    local_r14 = (uint32_t)((1) & (0x8000002AULL));
loc_009712AD:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)((uint32_t)(local_r14));
loc_009712CC:
    result = HvpGetCellPaged(Arg1, local_rsp - 63 - 89, local_rsp - 63 - 89, Arg4);
    goto loc_0097122D;
loc_009712D6:
    if ((((uint8_t)(15 - 14)) & ((uint8_t)(local_rsp - 63 - 89))) != 0) goto loc_00971512;
    if (((uint16_t)(local_rsp - 63 - 89)) <= ((uint16_t)((uint32_t)(0x7FFFULL)))) goto loc_009710DD;
    v_stack_p20 = 150;
    goto loc_009714B2;
loc_009712FA:
    if (((uint32_t)(local_r14)) == -1) goto loc_00971BFE;
loc_0097130A:
    v_stack_p20 = 224;
loc_00971312:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = (uint8_t)(15 - 14);
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(15 - 14)), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) {
        result = *(uint32_t *)(local_rsp - 0x3F - 0x61);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)(result);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)(local_r12);
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = local_r15;
    }
loc_00971351:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971638;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_0097136A:
loc_0097136E:
    if (((*(uint32_t *)(local_rsp - 0x3F + 0x6F)) & (0x20000ULL)) != 0) goto loc_0097148A;
    if ((*(uint8_t *)(v_rip + 0x666C80)) == 0) goto loc_0097147C;
loc_00971388:
    v_stack_p20 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), 1, 15, (uint32_t)(0xC000014CULL));
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) == 0) goto loc_00971468;
    result = HvpGetCellFlat(v_stack_p8, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)), local_rsp - 63 - 57, (uint32_t)(0xC000014CULL));
loc_009713BC:
    if (result == 0) goto loc_00971B9A;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(v_stack_p8, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)), Arg3, Arg4);
    if (sign_flag) goto loc_00971DFB;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(v_stack_p8, (uint32_t)(*(uint32_t *)(result + 0x28)), Arg3, Arg4);
    if (sign_flag) goto loc_00971DF1;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x5F))) + ((uint32_t)(result)));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61)))));
    Arg3 = (Arg3) << (2);
    *(uint32_t *)(local_rsp - 0x3F + 0x5F) = (uint32_t)(local_r14);
    result = memcpy(*(uint64_t *)(local_rsp - 0x3F - 0x9), *(uint64_t *)(local_rsp - 0x3F + 0x57) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61)) + 1 * 4, Arg3, Arg4);
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_0097162E;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 57, Arg3, Arg4);
loc_0097145E:
    goto loc_009711C1;
loc_00971468:
    result = HvpGetCellPaged(1, local_rsp - 63 - 57, Arg3, Arg4);
    goto loc_009713BC;
loc_00971472:
    result = HvpReleaseCellFlat(1, local_rsp - 63 - 57, Arg3, Arg4);
    goto loc_009711A9;
loc_0097147C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5867DE)))) & (6)) != 0) goto loc_00971388;
loc_0097148A:
    v_stack_p20 = 48;
loc_00971498:
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, 15, (uint32_t)(0xC000014CULL));
    goto loc_009712AD;
loc_009714AA:
    v_stack_p20 = 146;
loc_009714B2:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = (uint8_t)(15 - 14);
loc_009714C4:
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(15 - 14)), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) {
        result = *(uint32_t *)(local_rsp - 0x3F - 0x61);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)(result);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)(*(uint8_t *)(local_rsp - 0x3F + 0x7F));
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61));
    }
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_009717B1;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_0097150A:
    goto loc_0097136E;
loc_00971512:
    v_stack_p20 = 148;
    goto loc_009714B2;
loc_0097151C:
    v_stack_p20 = 112;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, 15, (uint32_t)(0xC000009AULL));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) == 0) goto loc_009712AD;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61)));
    goto loc_009718B9;
loc_00971551:
    v_stack_p20 = 240;
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = (uint8_t)(*(uint64_t *)(local_rsp - 0x3F + 0x7F));
    goto loc_009714C4;
loc_00971574:
    result = HvpReleaseCellFlat(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x3F + 0x7F))), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00971287;
loc_0097157E:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = (uint8_t)(15 - 14);
    v_stack_p20 = 400;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(15 - 14)), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) {
        result = *(uint32_t *)(local_rsp - 0x3F - 0x61);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)(result);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = 1;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = 1;
    }
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971B05;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 89, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00971351;
loc_009715E9:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = (uint8_t)(v_stack_p8);
    v_stack_p20 = 80;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(v_stack_p8)), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) goto loc_00971CFA;
loc_00971616:
    goto loc_0097136E;
loc_00971621:
    v_stack_p20 = 416;
    goto loc_00971312;
loc_0097162E:
    result = HvpReleaseCellFlat(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(v_stack_p8)), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0097145E;
loc_00971638:
    result = HvpReleaseCellFlat(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(v_stack_p8)), 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0097136A;
loc_00971642:
    if ((*(uint32_t *)(v_stack_p8 + 0xDC)) < 4) goto loc_0097124E;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(15 - 0x4)));
    if (((uint32_t)(result)) < 8) goto loc_00971A87;
    if ((*(uint16_t *)(15)) != ((uint16_t)((uint32_t)(0x6264ULL)))) goto loc_00971A87;
    if ((*(uint16_t *)(15 + 0x2)) == 0) goto loc_00971A87;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(15 + 0x4)))) == -1) goto loc_00971A87;
    result = HvIsCellAllocated(v_stack_p8, (uint32_t)(*(uint32_t *)(15 + 0x4)), *(uint64_t *)(local_rsp - 0x3F + 0x77), (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) == 0) goto loc_00971AFB;
    result = HvpGetCellFlat(v_stack_p8, (uint32_t)(*(uint32_t *)(15 + 0x4)), local_rsp - 63 - 81, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_009716C0:
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = result;
    if (result == 0) goto loc_00971DC4;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(15 + 0x2)))) << (2);
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x45))) + (0x3FD7ULL));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(*(uint32_t *)(15 + 0x4)))));
    Arg1 = (uint32_t)((Arg1) >> (1));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(*(uint32_t *)(15 + 0x4)))));
    Arg1 = (uint32_t)((Arg1) >> (13));
    if (((uint32_t)(*(uint16_t *)(15 + 0x2))) != ((uint32_t)(Arg1))) goto loc_00971C70;
loc_0097171D:
    if (0 >= ((uint32_t)(*(uint16_t *)(15 + 0x2)))) goto loc_00971A6C;
    result = HvIsCellAllocated(v_stack_p8, (uint32_t)(*(uint32_t *)(result + 0x0 * 4)), *(uint64_t *)(local_rsp - 0x3F + 0x77), result);
    if ((uint8_t)(result) == 0) goto loc_009719E1;
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) == 0) goto loc_00971995;
    result = HvpGetCellFlat(v_stack_p8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x31) + 0x0 * 4)), local_rsp - 63 - 65, result);
loc_0097176D:
    if (result == 0) goto loc_00971D79;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971B90;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 65, local_rsp - 63 - 65, result);
loc_009717A5:
    local_r12 = (uint32_t)((0) + (1));
    goto loc_0097171D;
loc_009717B1:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 65, local_rsp - 63 - 65, *(uint64_t *)(local_rsp - 0x3F - 0x31));
    goto loc_0097150A;
loc_009717BB:
    if (((*(uint8_t *)(1 + 0x10)) & ((uint8_t)(15 - 14))) == 0) goto loc_00971C21;
    Arg1 = (uint16_t)((*(uint16_t *)(v_rip + 0x66842B)) >> (1));
loc_009717E5:
    *(uint16_t *)(local_rsp - 0x3F - 0x45) = (uint16_t)(*(uint16_t *)(1 + 0x2));
    *(uint16_t *)(local_rsp - 0x3F - 0x49) = (uint16_t)(Arg1);
    if ((uint16_t)(Arg1) == 0) goto loc_0097195C;
    if ((uint16_t)(*(uint16_t *)(1 + 0x2)) == 0) goto loc_0097195C;
    Arg3 = (*(uint64_t *)(v_rip + 0x668426)) + (2);
    Arg2 = (1 + 20) + (15 - 14);
    *(uint64_t *)(local_rsp - 0x3F - 0x11) = Arg3;
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = Arg2;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x668426)))) == ((uint16_t)(*(uint8_t *)(1 + 0x14)))) goto loc_00971875;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x668426)))) < 97) goto loc_009719AC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x668426)))) > 122) goto loc_0097199F;
    local_r14 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x668426))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0097183B:
    if (((uint32_t)(*(uint8_t *)(1 + 0x14))) < 97) goto loc_0097184F;
    if (((uint32_t)(*(uint8_t *)(1 + 0x14))) > 122) goto loc_00971BEC;
    local_r13 = (uint16_t)((*(uint8_t *)(1 + 0x14)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0097184F:
    if (((uint16_t)(local_r14)) != ((uint16_t)(local_r13))) goto loc_00971B0F;
loc_00971875:
    Arg1 = (uint16_t)((*(uint16_t *)(local_rsp - 0x3F - 0x49)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    result = (uint16_t)((*(uint16_t *)(local_rsp - 0x3F - 0x45)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_009717E5;
loc_00971882:
    if (((uint32_t)(local_r14)) == ((uint32_t)(Arg1))) goto loc_00971035;
    v_stack_p20 = 64;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) == 0) goto loc_009712AD;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = 1;
loc_009718B9:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)(local_r12);
    goto loc_009712AD;
loc_009718C5:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = 1;
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) {
        result = *(uint32_t *)(local_rsp - 0x3F - 0x61);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)(result);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)(local_r12);
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = 1;
    }
    if (((*(uint32_t *)(local_rsp - 0x3F + 0x6F)) & (0x20000ULL)) != 0) goto loc_009719C4;
    if ((*(uint8_t *)(v_rip + 0x666701)) == 0) goto loc_009719B6;
loc_00971907:
    v_stack_p20 = 152;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), 1, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(v_stack_p8, (uint32_t)((uint32_t)(local_r12)), Arg3, Arg4);
    if (sign_flag) goto loc_00971D0D;
    goto loc_009710FB;
loc_0097195C:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_p8)) - ((uint32_t)((uint16_t)(*(uint64_t *)(v_stack_p8 + 0x40)))));
loc_0097196A:
    if ((uint32_t)(Arg1) != 0) goto loc_00971B15;
    v_stack_p20 = 176;
    goto loc_00971B34;
loc_00971995:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)(local_r12)), Arg3, Arg4);
    goto loc_0097176D;
loc_0097199F:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)((uint32_t)(result))), (uint32_t)((uint32_t)(local_r12)), Arg3, Arg4);
loc_009719AC:
    goto loc_0097183B;
loc_009719B6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5862A4)))) & (6)) != 0) goto loc_00971907;
loc_009719C4:
    v_stack_p20 = 156;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, 15, (uint32_t)((uint32_t)((uint16_t)((uint32_t)((uint32_t)(result))))));
    goto loc_00971B68;
loc_009719E1:
    v_stack_p20 = 352;
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = 1;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), 1, 1 + 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) goto loc_00971C4D;
loc_00971A16:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971BB0;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 81, 1 + 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_00971A2F:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971BBA;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 89, 1 + 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_00971A48:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971BC4;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 105, 1 + 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_00971A61:
    goto loc_0097150A;
loc_00971A6C:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) != 0) goto loc_00971BCE;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 81, 1 + 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00971269;
loc_00971A87:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = 1;
    v_stack_p20 = 272;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), 1, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) goto loc_00971C7D;
loc_00971ABE:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971BD8;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 89, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_00971ADD:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00971BE2;
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0097136E;
loc_00971AFB:
    result = HvpGetCellPaged(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009716C0;
loc_00971B05:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00971351;
loc_00971B0F:
loc_00971B15:
    v_stack_p20 = 160;
    goto loc_00971B34;
loc_00971B1F:
    if (((uint32_t)(v_stack_p8)) <= ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_00971156;
    v_stack_p20 = 208;
loc_00971B34:
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) != 0) {
        result = *(uint32_t *)(local_rsp - 0x3F - 0x61);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)(result);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = 1;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = 1;
    }
loc_00971B77:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) == 0) goto loc_00971B86;
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009712AD;
loc_00971B86:
    result = HvpReleaseCellPaged(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009712AD;
loc_00971B90:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009717A5;
loc_00971B9A:
    v_stack_p20 = 16;
    goto loc_00971498;
loc_00971BB0:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_00971A2F;
loc_00971BBA:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_00971A48;
loc_00971BC4:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_00971A61;
loc_00971BCE:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_00971269;
loc_00971BD8:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_00971ADD;
loc_00971BE2:
    result = HvpReleaseCellFlat(v_stack_p8, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_0097136E;
loc_00971BEC:
    result = RtlUpcaseUnicodeChar(15, local_rsp - 63 - 105, 15, (uint32_t)(0xC000009AULL));
    goto loc_0097184F;
loc_00971BFE:
    if (15 == 0) goto loc_00971242;
    goto loc_009711F6;
loc_00971C0B:
    if (((1) & (15)) == 0) goto loc_00971B1F;
    v_stack_p20 = 192;
    goto loc_00971B34;
loc_00971C21:
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = local_rsp - 63 - 105;
    *(uint16_t *)(local_rsp - 0x3F - 0x29) = (uint16_t)(result);
    Arg3 = 0;
    *(uint16_t *)(local_rsp - 0x3F - 0x27) = (uint16_t)(result);
    result = CmpCompareUnicodeString(v_rip + 6717396, local_rsp - 63 - 41, Arg3, (uint32_t)(0xC000009AULL));
    goto loc_0097196A;
loc_00971C4D:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = 1;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x31) + 0x1 * 4)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = (uint16_t)(result);
    goto loc_00971A16;
loc_00971C70:
    v_stack_p20 = 336;
loc_00971C7D:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x49)));
    goto loc_00971ABE;
loc_00971C94:
    v_stack_p20 = 144;
loc_00971CA1:
    v_stack_p20 = 136;
loc_00971CAE:
    v_stack_p20 = 128;
loc_00971CBB:
    *(uint8_t *)(local_rsp - 0x3F + 0x7F) = (uint8_t)(*(uint64_t *)(local_rsp - 0x3F - 0x31));
    v_stack_p20 = 96;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x31))), (uint32_t)((uint32_t)((uint16_t)(result))), (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = 1;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = 1;
loc_00971CFA:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = 1;
    goto loc_00971616;
loc_00971D0D:
    v_stack_p20 = 154;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), 1, (uint32_t)((uint32_t)((uint16_t)(result))), (uint32_t)((uint32_t)(result)));
    goto loc_00971B77;
loc_00971D3A:
    Arg2 = 0;
    v_stack_p20 = 256;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, Arg2 + 15, (uint32_t)(0xC000009AULL));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x7F) == 0) goto loc_00971B68;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x61)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x49)));
    goto loc_00971B68;
loc_00971D79:
    Arg2 = 0;
    v_stack_p20 = 368;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, Arg2 + 15, (uint32_t)(0xC000009AULL));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x118) = 1;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x11C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x31) + 0x1 * 4)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F) + 0x120) = (uint16_t)(result);
loc_00971DC4:
    Arg2 = 0;
    v_stack_p20 = 304;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x3F + 0x7F), Arg2, Arg2 + 15, (uint32_t)(0xC000009AULL));
loc_00971DF1:
loc_00971DFB:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg1` | `+ 0xDC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00970F6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
