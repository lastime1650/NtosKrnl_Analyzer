# MiAllocateFileExtents

- RVA: `0x00ABDF54`–`0x00ABE530` (길이 `1,500` bytes)
- VA: `0x0000000140ABDF54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD684`
- 디코드: `433`개 명령, `1,500/1,500` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00ABDFE1` → [MiStartingOffset](../../text/34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x00ABDFEC` → [MiEndingOffset](../../text/2A/MiEndingOffset_function_002ACEC8.md) (function, `0x002ACEC8`)
- `0x00ABE04D` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (function, `0x00431554`)
- `0x00ABE09A` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00ABE13D` → [MiChangingSubsectionProtos](../../text/68/MiChangingSubsectionProtos_function_0068057C.md) (function, `0x0068057C`)
- `0x00ABE167` → [FsRtlGetFileExtents](../../text/58/FsRtlGetFileExtents_function_00580F40.md) (function, `0x00580F40`)
- `0x00ABE190` → [MiUnlinkSubsectionWaitBlock](../../text/68/MiUnlinkSubsectionWaitBlock_function_00681EDC.md) (function, `0x00681EDC`)
- `0x00ABE1A1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE1B8` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (function, `0x004345E0`)
- `0x00ABE1C0` → [MiNewPfnsSuitable](../7F/MiNewPfnsSuitable_function_007FAC24.md) (function, `0x007FAC24`)
- `0x00ABE21B` → [MiConvertRunsToPages](../80/MiConvertRunsToPages_function_00800BC8.md) (function, `0x00800BC8`)
- `0x00ABE257` → [MiChangingSubsectionProtos](../../text/68/MiChangingSubsectionProtos_function_0068057C.md) (function, `0x0068057C`)
- `0x00ABE267` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE279` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE2C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE300` → [MiEliminateStaleExtents](../../text/68/MiEliminateStaleExtents_function_006809A8.md) (function, `0x006809A8`)
- `0x00ABE323` → [MiInsertCopyExtents](../../text/68/MiInsertCopyExtents_function_00681440.md) (function, `0x00681440`)
- `0x00ABE341` → [MiMergeCopyExtents](../../text/68/MiMergeCopyExtents_function_00681844.md) (function, `0x00681844`)
- `0x00ABE36C` → [MiSubsectionProtosCreated](../../text/4D/MiSubsectionProtosCreated_function_004D9570.md) (function, `0x004D9570`)
- `0x00ABE3BD` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (function, `0x00295F0C`)
- `0x00ABE3D8` → [MiCreateFileOnlyPfns](../80/MiCreateFileOnlyPfns_function_00800DB4.md) (function, `0x00800DB4`)
- `0x00ABE405` → [MiSetSubsectionBase](../../text/49/MiSetSubsectionBase_function_0049CE98.md) (function, `0x0049CE98`)
- `0x00ABE41E` → [MiReplaceSystemProtoPtesNode](../../text/69/MiReplaceSystemProtoPtesNode_function_00699658.md) (function, `0x00699658`)
- `0x00ABE44A` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (function, `0x00295F0C`)
- `0x00ABE46B` → [MiSubsectionProtosCreated](../../text/4D/MiSubsectionProtosCreated_function_004D9570.md) (function, `0x004D9570`)
- `0x00ABE478` → [MiDeleteFileExtentList](../80/MiDeleteFileExtentList_function_00800F6C.md) (function, `0x00800F6C`)
- `0x00ABE487` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE4AA` → [MiUnlinkSubsectionWaitBlock](../../text/68/MiUnlinkSubsectionWaitBlock_function_00681EDC.md) (function, `0x00681EDC`)
- `0x00ABE4B8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE4C5` → [MiDeleteFileExtentList](../80/MiDeleteFileExtentList_function_00800F6C.md) (function, `0x00800F6C`)
- `0x00ABE4D2` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (function, `0x004345E0`)
- `0x00ABE4E9` → [MiUnlinkSubsectionWaitBlock](../../text/68/MiUnlinkSubsectionWaitBlock_function_00681EDC.md) (function, `0x00681EDC`)
- `0x00ABE4F6` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (function, `0x004345E0`)
- `0x00ABE500` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABE511` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (function, `0x004345E0`)

### Direct callers
- [MiCreatePrototypePtes](../../text/29/MiCreatePrototypePtes_function_002950FC.md) at `0x002954B5`
- [MiFaultGetFileExtents](../../text/47/MiFaultGetFileExtents_function_00479758.md) at `0x0047981A`
- [MiRefillPurgedExtents](../../text/47/MiRefillPurgedExtents_function_00479988.md) at `0x004799EC`
- [MiInitializeCachedExtentWalker](../../text/4C/MiInitializeCachedExtentWalker_function_004CAC6C.md) at `0x004CAD3B`
- [MiUpdateActiveSubsection](../../text/67/MiUpdateActiveSubsection_function_0067F034.md) at `0x0067F0C9`
- [sub_006E19B0](../../text/6E/Unknown_function_006E19B0.md) at `0x006E1A02`
- [MiInitializeImageExtents](../80/MiInitializeImageExtents_function_00800FE8.md) at `0x00801031`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x00ABDFE1` → [MiStartingOffset](../../text/34/MiStartingOffset_function_003482E0.md) (`PAGE` → `.text`)
  - `0x00ABDFEC` → [MiEndingOffset](../../text/2A/MiEndingOffset_function_002ACEC8.md) (`PAGE` → `.text`)
  - `0x00ABE04D` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (`PAGE` → `.text`)
  - `0x00ABE09A` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00ABE13D` → [MiChangingSubsectionProtos](../../text/68/MiChangingSubsectionProtos_function_0068057C.md) (`PAGE` → `.text`)
  - `0x00ABE167` → [FsRtlGetFileExtents](../../text/58/FsRtlGetFileExtents_function_00580F40.md) (`PAGE` → `.text`)
  - `0x00ABE190` → [MiUnlinkSubsectionWaitBlock](../../text/68/MiUnlinkSubsectionWaitBlock_function_00681EDC.md) (`PAGE` → `.text`)
  - `0x00ABE1A1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE1B8` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (`PAGE` → `.text`)
  - `0x00ABE257` → [MiChangingSubsectionProtos](../../text/68/MiChangingSubsectionProtos_function_0068057C.md) (`PAGE` → `.text`)
  - `0x00ABE267` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE279` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE2C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE300` → [MiEliminateStaleExtents](../../text/68/MiEliminateStaleExtents_function_006809A8.md) (`PAGE` → `.text`)
  - `0x00ABE323` → [MiInsertCopyExtents](../../text/68/MiInsertCopyExtents_function_00681440.md) (`PAGE` → `.text`)
  - `0x00ABE341` → [MiMergeCopyExtents](../../text/68/MiMergeCopyExtents_function_00681844.md) (`PAGE` → `.text`)
  - `0x00ABE36C` → [MiSubsectionProtosCreated](../../text/4D/MiSubsectionProtosCreated_function_004D9570.md) (`PAGE` → `.text`)
  - `0x00ABE3BD` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (`PAGE` → `.text`)
  - `0x00ABE405` → [MiSetSubsectionBase](../../text/49/MiSetSubsectionBase_function_0049CE98.md) (`PAGE` → `.text`)
  - `0x00ABE41E` → [MiReplaceSystemProtoPtesNode](../../text/69/MiReplaceSystemProtoPtesNode_function_00699658.md) (`PAGE` → `.text`)
  - `0x00ABE44A` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (`PAGE` → `.text`)
  - `0x00ABE46B` → [MiSubsectionProtosCreated](../../text/4D/MiSubsectionProtosCreated_function_004D9570.md) (`PAGE` → `.text`)
  - `0x00ABE487` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE4AA` → [MiUnlinkSubsectionWaitBlock](../../text/68/MiUnlinkSubsectionWaitBlock_function_00681EDC.md) (`PAGE` → `.text`)
  - `0x00ABE4B8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE4D2` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (`PAGE` → `.text`)
  - `0x00ABE4E9` → [MiUnlinkSubsectionWaitBlock](../../text/68/MiUnlinkSubsectionWaitBlock_function_00681EDC.md) (`PAGE` → `.text`)
  - `0x00ABE4F6` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (`PAGE` → `.text`)
  - `0x00ABE500` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABE511` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABDF54  48 8B C4                        mov rax, rsp
00ABDF57  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00ABDF5B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00ABDF5F  89 50 10                        mov dword ptr [rax + 0x10], edx
00ABDF62  55                              push rbp
00ABDF63  53                              push rbx
00ABDF64  56                              push rsi
00ABDF65  57                              push rdi
00ABDF66  41 54                           push r12
00ABDF68  41 55                           push r13
00ABDF6A  41 56                           push r14
00ABDF6C  41 57                           push r15
00ABDF6E  48 8D 68 B1                     lea rbp, [rax - 0x4f]
00ABDF72  48 81 EC C8 00 00 00            sub rsp, 0xc8
00ABDF79  41 8B C1                        mov eax, r9d
00ABDF7C  0F 57 C9                        xorps xmm1, xmm1
00ABDF7F  0F 57 C0                        xorps xmm0, xmm0
00ABDF82  4D 8B C8                        mov r9, r8
00ABDF85  45 33 C0                        xor r8d, r8d
00ABDF88  4C 8B F9                        mov r15, rcx
00ABDF8B  33 C9                           xor ecx, ecx
00ABDF8D  4C 89 45 8F                     mov qword ptr [rbp - 0x71], r8
00ABDF91  C1 E0 0C                        shl eax, 0xc
00ABDF94  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00ABDF98  0F 11 45 A7                     movups xmmword ptr [rbp - 0x59], xmm0
00ABDF9C  48 89 4D C7                     mov qword ptr [rbp - 0x39], rcx
00ABDFA0  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
00ABDFA4  4C 89 45 87                     mov qword ptr [rbp - 0x79], r8
00ABDFA8  0F 11 4D CF                     movups xmmword ptr [rbp - 0x31], xmm1
00ABDFAC  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
00ABDFB0  0F 11 4D EF                     movups xmmword ptr [rbp - 0x11], xmm1
00ABDFB4  4D 8B 37                        mov r14, qword ptr [r15]
00ABDFB7  4C 8B E0                        mov r12, rax
00ABDFBA  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00ABDFBE  A8 20                           test al, 0x20
00ABDFC0  74 63                           je 0x140abe025
00ABDFC2  C7 45 57 01 00 00 00            mov dword ptr [rbp + 0x57], 1
00ABDFC9  4D 39 47 08                     cmp qword ptr [r15 + 8], r8
00ABDFCD  75 08                           jne 0x140abdfd7
00ABDFCF  8B FA                           mov edi, edx
00ABDFD1  48 C1 E7 0C                     shl rdi, 0xc
00ABDFD5  EB 12                           jmp 0x140abdfe9
00ABDFD7  44 8B 45 7F                     mov r8d, dword ptr [rbp + 0x7f]
00ABDFDB  49 8B D1                        mov rdx, r9
00ABDFDE  49 8B CF                        mov rcx, r15
00ABDFE1  E8 FA A2 88 FF                  call 0x1403482e0
00ABDFE6  48 8B F8                        mov rdi, rax
00ABDFE9  49 8B CF                        mov rcx, r15
00ABDFEC  E8 D7 EE 7E FF                  call 0x1402acec8
00ABDFF1  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
00ABDFF5  48 3B F8                        cmp rdi, rax
00ABDFF8  75 09                           jne 0x140abe003
00ABDFFA  48 85 FF                        test rdi, rdi
00ABDFFD  0F 84 9A 02 00 00               je 0x140abe29d
00ABE003  49 8D 0C 3C                     lea rcx, [r12 + rdi]
00ABE007  48 3B C8                        cmp rcx, rax
00ABE00A  76 3E                           jbe 0x140abe04a
00ABE00C  4C 8B E0                        mov r12, rax
00ABE00F  4C 2B E7                        sub r12, rdi
00ABE012  45 8B E4                        mov r12d, r12d
00ABE015  49 81 C4 FF 01 00 00            add r12, 0x1ff
00ABE01C  49 81 E4 00 FE FF FF            and r12, 0xfffffffffffffe00
00ABE023  EB 25                           jmp 0x140abe04a
00ABE025  41 8B 7F 20                     mov edi, dword ptr [r15 + 0x20]
00ABE029  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
00ABE02D  81 E7 C0 FF 00 00               and edi, 0xffc0
00ABE033  48 C1 E7 1A                     shl rdi, 0x1a
00ABE037  48 0B F8                        or rdi, rax
00ABE03A  C7 45 57 02 00 00 00            mov dword ptr [rbp + 0x57], 2
00ABE041  8B C2                           mov eax, edx
00ABE043  48 03 F8                        add rdi, rax
00ABE046  48 C1 E7 0C                     shl rdi, 0xc
00ABE04A  49 8B CE                        mov rcx, r14
00ABE04D  E8 02 35 97 FF                  call 0x140431554
00ABE052  48 8B D8                        mov rbx, rax
00ABE055  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00ABE059  0F 31                           rdtsc
00ABE05B  48 C1 E2 20                     shl rdx, 0x20
00ABE05F  48 0B C2                        or rax, rdx
00ABE062  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00ABE06A  4C 8B E8                        mov r13, rax
00ABE06D  49 C1 ED 04                     shr r13, 4
00ABE071  41 83 E5 07                     and r13d, 7
00ABE075  41 83 C5 08                     add r13d, 8
00ABE079  41 83 FD 01                     cmp r13d, 1
00ABE07D  0F 82 88 04 00 00               jb 0x140abe50b
00ABE083  41 8D 55 FF                     lea edx, [r13 - 1]
00ABE087  B9 40 00 00 00                  mov ecx, 0x40
00ABE08C  48 C1 E2 04                     shl rdx, 4
00ABE090  41 B8 4D 69 46 34               mov r8d, 0x3446694d
00ABE096  48 83 C2 18                     add rdx, 0x18
00ABE09A  E8 A1 D4 89 FF                  call 0x14035b540
00ABE09F  45 33 C0                        xor r8d, r8d
00ABE0A2  48 8B F0                        mov rsi, rax
00ABE0A5  48 85 C0                        test rax, rax
00ABE0A8  75 10                           jne 0x140abe0ba
00ABE0AA  44 39 44 24 30                  cmp dword ptr [rsp + 0x30], r8d
00ABE0AF  0F 84 56 04 00 00               je 0x140abe50b
00ABE0B5  41 D1 ED                        shr r13d, 1
00ABE0B8  EB BF                           jmp 0x140abe079
00ABE0BA  8B 55 57                        mov edx, dword ptr [rbp + 0x57]
00ABE0BD  44 89 28                        mov dword ptr [rax], r13d
00ABE0C0  44 89 40 04                     mov dword ptr [rax + 4], r8d
00ABE0C4  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00ABE0C9  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00ABE0CE  83 FA 01                        cmp edx, 1
00ABE0D1  75 42                           jne 0x140abe115
00ABE0D3  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00ABE0D7  49 8D 04 3C                     lea rax, [r12 + rdi]
00ABE0DB  48 3B C1                        cmp rax, rcx
00ABE0DE  76 09                           jbe 0x140abe0e9
00ABE0E0  4C 8B E1                        mov r12, rcx
00ABE0E3  4C 2B E7                        sub r12, rdi
00ABE0E6  45 8B E4                        mov r12d, r12d
00ABE0E9  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00ABE0ED  48 85 C9                        test rcx, rcx
00ABE0F0  74 23                           je 0x140abe115
00ABE0F2  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
00ABE0F6  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00ABE0FA  F7 40 38 00 10 00 00            test dword ptr [rax + 0x38], 0x1000
00ABE101  74 12                           je 0x140abe115
00ABE103  49 8B 06                        mov rax, qword ptr [r14]
00ABE106  48 8B F9                        mov rdi, rcx
00ABE109  48 2B 78 40                     sub rdi, qword ptr [rax + 0x40]
00ABE10D  48 C1 FF 03                     sar rdi, 3
00ABE111  48 C1 E7 0C                     shl rdi, 0xc
00ABE115  49 81 C4 FF 0F 00 00            add r12, 0xfff
00ABE11C  49 81 E4 00 F0 FF FF            and r12, 0xfffffffffffff000
00ABE123  83 FA 01                        cmp edx, 1
00ABE126  75 08                           jne 0x140abe130
00ABE128  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00ABE12C  A8 02                           test al, 2
00ABE12E  75 29                           jne 0x140abe159
00ABE130  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
00ABE133  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00ABE137  83 CA 08                        or edx, 8
00ABE13A  49 8B CF                        mov rcx, r15
00ABE13D  E8 3A 24 BC FF                  call 0x14068057c
00ABE142  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00ABE146  85 C0                           test eax, eax
00ABE148  0F 88 A2 03 00 00               js 0x140abe4f0
00ABE14E  8B 55 57                        mov edx, dword ptr [rbp + 0x57]
00ABE151  C7 44 24 34 01 00 00 00         mov dword ptr [rsp + 0x34], 1
00ABE159  4D 8B CC                        mov r9, r12
00ABE15C  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00ABE161  4C 8B C7                        mov r8, rdi
00ABE164  48 8B CB                        mov rcx, rbx
00ABE167  E8 D4 2D AC FF                  call 0x140580f40
00ABE16C  33 C9                           xor ecx, ecx
00ABE16E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00ABE172  85 C0                           test eax, eax
00ABE174  0F 88 52 03 00 00               js 0x140abe4cc
00ABE17A  44 39 6E 04                     cmp dword ptr [rsi + 4], r13d
00ABE17E  76 32                           jbe 0x140abe1b2
00ABE180  39 4C 24 34                     cmp dword ptr [rsp + 0x34], ecx
00ABE184  74 0F                           je 0x140abe195
00ABE186  45 33 C0                        xor r8d, r8d
00ABE189  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00ABE18D  49 8B CF                        mov rcx, r15
00ABE190  E8 47 3D BC FF                  call 0x140681edc
00ABE195  8B 5E 04                        mov ebx, dword ptr [rsi + 4]
00ABE198  33 D2                           xor edx, edx
00ABE19A  48 8B CE                        mov rcx, rsi
00ABE19D  44 89 6E 04                     mov dword ptr [rsi + 4], r13d
00ABE1A1  E8 CA 46 0C 00                  call 0x140b82870
00ABE1A6  44 8B EB                        mov r13d, ebx
00ABE1A9  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
00ABE1AD  E9 C7 FE FF FF                  jmp 0x140abe079
00ABE1B2  48 8B D3                        mov rdx, rbx
00ABE1B5  49 8B CE                        mov rcx, r14
00ABE1B8  E8 23 64 97 FF                  call 0x1404345e0
00ABE1BD  48 8B CE                        mov rcx, rsi
00ABE1C0  E8 5F CA D3 FF                  call 0x1407fac24
00ABE1C5  33 DB                           xor ebx, ebx
00ABE1C7  85 C0                           test eax, eax
00ABE1C9  0F 84 C4 02 00 00               je 0x140abe493
00ABE1CF  44 8B EB                        mov r13d, ebx
00ABE1D2  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
00ABE1DA  44 8B E3                        mov r12d, ebx
00ABE1DD  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00ABE1E2  39 5E 04                        cmp dword ptr [rsi + 4], ebx
00ABE1E5  75 2A                           jne 0x140abe211
00ABE1E7  F6 45 77 40                     test byte ptr [rbp + 0x77], 0x40
00ABE1EB  0F 85 B3 00 00 00               jne 0x140abe2a4
00ABE1F1  8B 7D 57                        mov edi, dword ptr [rbp + 0x57]
00ABE1F4  83 FF 01                        cmp edi, 1
00ABE1F7  0F 84 A7 00 00 00               je 0x140abe2a4
00ABE1FD  41 8A 46 3E                     mov al, byte ptr [r14 + 0x3e]
00ABE201  24 0C                           and al, 0xc
00ABE203  3C 08                           cmp al, 8
00ABE205  75 43                           jne 0x140abe24a
00ABE207  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00ABE20C  E9 87 02 00 00                  jmp 0x140abe498
00ABE211  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00ABE216  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00ABE21B  E8 A8 29 D4 FF                  call 0x140800bc8
00ABE220  4C 8B E0                        mov r12, rax
00ABE223  48 85 C0                        test rax, rax
00ABE226  74 DF                           je 0x140abe207
00ABE228  F6 45 77 40                     test byte ptr [rbp + 0x77], 0x40
00ABE22C  74 07                           je 0x140abe235
00ABE22E  83 7C 24 30 01                  cmp dword ptr [rsp + 0x30], 1
00ABE233  77 79                           ja 0x140abe2ae
00ABE235  8B 7D 57                        mov edi, dword ptr [rbp + 0x57]
00ABE238  83 FF 01                        cmp edi, 1
00ABE23B  75 08                           jne 0x140abe245
00ABE23D  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00ABE241  A8 02                           test al, 2
00ABE243  75 73                           jne 0x140abe2b8
00ABE245  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00ABE24A  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
00ABE24D  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00ABE251  83 CA 10                        or edx, 0x10
00ABE254  49 8B CF                        mov rcx, r15
00ABE257  E8 20 23 BC FF                  call 0x14068057c
00ABE25C  8B D8                           mov ebx, eax
00ABE25E  85 C0                           test eax, eax
00ABE260  79 7F                           jns 0x140abe2e1
00ABE262  33 D2                           xor edx, edx
00ABE264  48 8B CE                        mov rcx, rsi
00ABE267  E8 04 46 0C 00                  call 0x140b82870
00ABE26C  45 33 C0                        xor r8d, r8d
00ABE26F  4D 85 E4                        test r12, r12
00ABE272  74 0D                           je 0x140abe281
00ABE274  33 D2                           xor edx, edx
00ABE276  49 8B CC                        mov rcx, r12
00ABE279  E8 F2 45 0C 00                  call 0x140b82870
00ABE27E  45 33 C0                        xor r8d, r8d
00ABE281  81 FB 34 04 00 C0               cmp ebx, 0xc0000434
00ABE287  0F 85 FF 01 00 00               jne 0x140abe48c
00ABE28D  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
00ABE291  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
00ABE294  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00ABE298  E9 17 FD FF FF                  jmp 0x140abdfb4
00ABE29D  33 C0                           xor eax, eax
00ABE29F  E9 77 02 00 00                  jmp 0x140abe51b
00ABE2A4  BB 01 00 00 C0                  mov ebx, 0xc0000001
00ABE2A9  E9 EA 01 00 00                  jmp 0x140abe498
00ABE2AE  BB 18 00 00 C0                  mov ebx, 0xc0000018
00ABE2B3  E9 E0 01 00 00                  jmp 0x140abe498
00ABE2B8  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00ABE2BD  48 8B 7D 87                     mov rdi, qword ptr [rbp - 0x79]
00ABE2C1  33 D2                           xor edx, edx
00ABE2C3  48 8B CE                        mov rcx, rsi
00ABE2C6  E8 A5 45 0C 00                  call 0x140b82870
00ABE2CB  33 F6                           xor esi, esi
00ABE2CD  48 85 FF                        test rdi, rdi
00ABE2D0  0F 84 A0 00 00 00               je 0x140abe376
00ABE2D6  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
00ABE2DA  8B DE                           mov ebx, esi
00ABE2DC  E9 02 01 00 00                  jmp 0x140abe3e3
00ABE2E1  4D 85 E4                        test r12, r12
00ABE2E4  74 1F                           je 0x140abe305
00ABE2E6  41 8A 46 3E                     mov al, byte ptr [r14 + 0x3e]
00ABE2EA  24 0C                           and al, 0xc
00ABE2EC  3C 04                           cmp al, 4
00ABE2EE  75 15                           jne 0x140abe305
00ABE2F0  F6 45 77 01                     test byte ptr [rbp + 0x77], 1
00ABE2F4  75 0F                           jne 0x140abe305
00ABE2F6  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00ABE2FA  4D 8B C5                        mov r8, r13
00ABE2FD  49 8B D4                        mov rdx, r12
00ABE300  E8 A3 26 BC FF                  call 0x1406809a8
00ABE305  83 FF 01                        cmp edi, 1
00ABE308  74 B3                           je 0x140abe2bd
00ABE30A  41 8A 46 3E                     mov al, byte ptr [r14 + 0x3e]
00ABE30E  24 0C                           and al, 0xc
00ABE310  3C 08                           cmp al, 8
00ABE312  75 A9                           jne 0x140abe2bd
00ABE314  F6 45 77 01                     test byte ptr [rbp + 0x77], 1
00ABE318  74 1D                           je 0x140abe337
00ABE31A  33 D2                           xor edx, edx
00ABE31C  48 8B CE                        mov rcx, rsi
00ABE31F  44 8D 42 01                     lea r8d, [rdx + 1]
00ABE323  E8 18 31 BC FF                  call 0x140681440
00ABE328  48 8B F8                        mov rdi, rax
00ABE32B  48 85 C0                        test rax, rax
00ABE32E  75 91                           jne 0x140abe2c1
00ABE330  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00ABE335  EB 28                           jmp 0x140abe35f
00ABE337  4C 8D 4D 87                     lea r9, [rbp - 0x79]
00ABE33B  48 8B D6                        mov rdx, rsi
00ABE33E  49 8B CF                        mov rcx, r15
00ABE341  E8 FE 34 BC FF                  call 0x140681844
00ABE346  8B D8                           mov ebx, eax
00ABE348  33 C0                           xor eax, eax
00ABE34A  85 DB                           test ebx, ebx
00ABE34C  0F 89 6B FF FF FF               jns 0x140abe2bd
00ABE352  48 8B 7D 87                     mov rdi, qword ptr [rbp - 0x79]
00ABE356  81 FB 0A 02 00 C0               cmp ebx, 0xc000020a
00ABE35C  0F 44 D8                        cmove ebx, eax
00ABE35F  45 33 C9                        xor r9d, r9d
00ABE362  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00ABE366  45 33 C0                        xor r8d, r8d
00ABE369  49 8B CF                        mov rcx, r15
00ABE36C  E8 FF B1 A1 FF                  call 0x1404d9570
00ABE371  E9 3D 01 00 00                  jmp 0x140abe4b3
00ABE376  4D 85 E4                        test r12, r12
00ABE379  74 47                           je 0x140abe3c2
00ABE37B  41 F6 46 38 20                  test byte ptr [r14 + 0x38], 0x20
00ABE380  0F 94 C1                        sete cl
00ABE383  F6 45 77 01                     test byte ptr [rbp + 0x77], 1
00ABE387  0F 95 C0                        setne al
00ABE38A  84 C8                           test al, cl
00ABE38C  74 34                           je 0x140abe3c2
00ABE38E  41 8A 46 3E                     mov al, byte ptr [r14 + 0x3e]
00ABE392  24 0C                           and al, 0xc
00ABE394  3C 04                           cmp al, 4
00ABE396  75 2A                           jne 0x140abe3c2
00ABE398  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00ABE39C  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ABE3A0  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00ABE3A4  4C 89 6D F7                     mov qword ptr [rbp - 9], r13
00ABE3A8  48 83 C8 04                     or rax, 4
00ABE3AC  BA 01 00 00 00                  mov edx, 1
00ABE3B1  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00ABE3B5  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00ABE3B9  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00ABE3BD  E8 4A 7B 7D FF                  call 0x140295f0c
00ABE3C2  44 8B 45 77                     mov r8d, dword ptr [rbp + 0x77]
00ABE3C6  4D 8B CC                        mov r9, r12
00ABE3C9  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00ABE3CE  49 8B CF                        mov rcx, r15
00ABE3D1  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
00ABE3D5  49 8B D5                        mov rdx, r13
00ABE3D8  E8 D7 29 D4 FF                  call 0x140800db4
00ABE3DD  8B D8                           mov ebx, eax
00ABE3DF  85 C0                           test eax, eax
00ABE3E1  78 5B                           js 0x140abe43e
00ABE3E3  F6 45 77 01                     test byte ptr [rbp + 0x77], 1
00ABE3E7  74 4B                           je 0x140abe434
00ABE3E9  F6 45 77 40                     test byte ptr [rbp + 0x77], 0x40
00ABE3ED  74 08                           je 0x140abe3f7
00ABE3EF  41 C7 47 6C 02 00 00 00         mov dword ptr [r15 + 0x6c], 2
00ABE3F7  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00ABE3FC  4C 8B CF                        mov r9, rdi
00ABE3FF  49 8B D5                        mov rdx, r13
00ABE402  49 8B CF                        mov rcx, r15
00ABE405  E8 8E EA 9D FF                  call 0x14049ce98
00ABE40A  49 8D 4F 78                     lea rcx, [r15 + 0x78]
00ABE40E  48 8B FE                        mov rdi, rsi
00ABE411  48 39 75 EF                     cmp qword ptr [rbp - 0x11], rsi
00ABE415  74 0E                           je 0x140abe425
00ABE417  48 8B D1                        mov rdx, rcx
00ABE41A  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ABE41E  E8 35 B2 BD FF                  call 0x140699658
00ABE423  EB 2A                           jmp 0x140abe44f
00ABE425  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00ABE429  A8 20                           test al, 0x20
00ABE42B  75 22                           jne 0x140abe44f
00ABE42D  BA 01 00 00 00                  mov edx, 1
00ABE432  EB 16                           jmp 0x140abe44a
00ABE434  48 85 FF                        test rdi, rdi
00ABE437  74 16                           je 0x140abe44f
00ABE439  48 8B FE                        mov rdi, rsi
00ABE43C  EB 11                           jmp 0x140abe44f
00ABE43E  48 39 75 EF                     cmp qword ptr [rbp - 0x11], rsi
00ABE442  74 0B                           je 0x140abe44f
00ABE444  33 D2                           xor edx, edx
00ABE446  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ABE44A  E8 BD 7A 7D FF                  call 0x140295f0c
00ABE44F  83 7D 57 01                     cmp dword ptr [rbp + 0x57], 1
00ABE453  75 08                           jne 0x140abe45d
00ABE455  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00ABE459  A8 02                           test al, 2
00ABE45B  75 13                           jne 0x140abe470
00ABE45D  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
00ABE461  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00ABE465  45 33 C9                        xor r9d, r9d
00ABE468  49 8B CF                        mov rcx, r15
00ABE46B  E8 00 B1 A1 FF                  call 0x1404d9570
00ABE470  48 85 FF                        test rdi, rdi
00ABE473  74 08                           je 0x140abe47d
00ABE475  48 8B CF                        mov rcx, rdi
00ABE478  E8 EF 2A D4 FF                  call 0x140800f6c
00ABE47D  4D 85 E4                        test r12, r12
00ABE480  74 0A                           je 0x140abe48c
00ABE482  33 D2                           xor edx, edx
00ABE484  49 8B CC                        mov rcx, r12
00ABE487  E8 E4 43 0C 00                  call 0x140b82870
00ABE48C  8B C3                           mov eax, ebx
00ABE48E  E9 88 00 00 00                  jmp 0x140abe51b
00ABE493  BB 27 04 00 C0                  mov ebx, 0xc0000427
00ABE498  33 C9                           xor ecx, ecx
00ABE49A  39 4C 24 34                     cmp dword ptr [rsp + 0x34], ecx
00ABE49E  74 0F                           je 0x140abe4af
00ABE4A0  45 33 C0                        xor r8d, r8d
00ABE4A3  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00ABE4A7  49 8B CF                        mov rcx, r15
00ABE4AA  E8 2D 3A BC FF                  call 0x140681edc
00ABE4AF  48 8B 7D 87                     mov rdi, qword ptr [rbp - 0x79]
00ABE4B3  33 D2                           xor edx, edx
00ABE4B5  48 8B CE                        mov rcx, rsi
00ABE4B8  E8 B3 43 0C 00                  call 0x140b82870
00ABE4BD  48 85 FF                        test rdi, rdi
00ABE4C0  74 CA                           je 0x140abe48c
00ABE4C2  48 8B CF                        mov rcx, rdi
00ABE4C5  E8 A2 2A D4 FF                  call 0x140800f6c
00ABE4CA  EB C0                           jmp 0x140abe48c
00ABE4CC  48 8B D3                        mov rdx, rbx
00ABE4CF  49 8B CE                        mov rcx, r14
00ABE4D2  E8 09 61 97 FF                  call 0x1404345e0
00ABE4D7  33 C0                           xor eax, eax
00ABE4D9  39 44 24 34                     cmp dword ptr [rsp + 0x34], eax
00ABE4DD  74 1C                           je 0x140abe4fb
00ABE4DF  45 33 C0                        xor r8d, r8d
00ABE4E2  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00ABE4E6  49 8B CF                        mov rcx, r15
00ABE4E9  E8 EE 39 BC FF                  call 0x140681edc
00ABE4EE  EB 0B                           jmp 0x140abe4fb
00ABE4F0  48 8B D3                        mov rdx, rbx
00ABE4F3  49 8B CE                        mov rcx, r14
00ABE4F6  E8 E5 60 97 FF                  call 0x1404345e0
00ABE4FB  33 D2                           xor edx, edx
00ABE4FD  48 8B CE                        mov rcx, rsi
00ABE500  E8 6B 43 0C 00                  call 0x140b82870
00ABE505  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00ABE509  EB 10                           jmp 0x140abe51b
00ABE50B  48 8B D3                        mov rdx, rbx
00ABE50E  49 8B CE                        mov rcx, r14
00ABE511  E8 CA 60 97 FF                  call 0x1404345e0
00ABE516  B8 9A 00 00 C0                  mov eax, 0xc000009a
00ABE51B  48 81 C4 C8 00 00 00            add rsp, 0xc8
00ABE522  41 5F                           pop r15
00ABE524  41 5E                           pop r14
00ABE526  41 5D                           pop r13
00ABE528  41 5C                           pop r12
00ABE52A  5F                              pop rdi
00ABE52B  5E                              pop rsi
00ABE52C  5B                              pop rbx
00ABE52D  5D                              pop rbp
00ABE52E  C3                              ret
00ABE52F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateFileExtents(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (200);
    a3 = 0;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 113) = 0;
    result = (unsigned int)(((unsigned int)(a4)) << (12));
    *(unsigned __int64 *)(v_rsp - 79 - 97) = result;
    *(unsigned __int64 *)(v_rsp - 79 - 89) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 73) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 121) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 49) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 79 - 33) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = v_xmm1;
loc_00ABDFB4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) == 0) goto loc_00ABE025;
    *(unsigned int *)(v_rsp - 79 + 87) = 1;
    if ((*(unsigned __int64 *)(a1 + 8)) != 0) goto loc_00ABDFD7;
    v_rdi = ((unsigned int)(a2)) << (12);
    goto loc_00ABDFE9;
loc_00ABDFD7:
    result = MiStartingOffset(0, 0, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 127)), a3);
loc_00ABDFE9:
    result = MiEndingOffset(0, 0, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 127)), a3);
    *(unsigned __int64 *)(v_rsp - 79 - 113) = result;
    if (result != result) goto loc_00ABE003;
    if (result == 0) goto loc_00ABE29D;
loc_00ABE003:
    if ((result + result * 1) <= result) goto loc_00ABE04A;
    v_r12 = (result) - (result);
    v_r12 = ((unsigned int)((unsigned int)(v_r12))) + (511);
    v_r12 = (v_r12) & (-512);
    goto loc_00ABE04A;
loc_00ABE025:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (0xFFC0ULL));
    v_rdi = (v_rdi) << (26);
    v_rdi = (v_rdi) | ((unsigned int)(*(unsigned int *)(a1 + 36)));
    *(unsigned int *)(v_rsp - 79 + 87) = 2;
    v_rdi = (v_rdi) + (0);
    v_rdi = (v_rdi) << (12);
loc_00ABE04A:
    result = MiReferenceControlAreaFile(*(unsigned __int64 *)(a1), 0, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 127)), a3);
    *(unsigned __int64 *)(v_rsp - 79 - 105) = result;
    a2 = (0) << (32);
    result = (result) | (a2);
    v_stack_mD8 = 1;
    v_r13 = (result) >> (4);
    v_r13 = (unsigned int)((v_r13) & (7));
    v_r13 = (unsigned int)((v_r13) + (8));
loc_00ABE079:
    if (((unsigned int)(v_r13)) < 1) goto loc_00ABE50B;
    a2 = (v_r13 - 1) << (4);
    a2 = (a2) + (24);
    result = MiAllocatePool(64, a2, (unsigned int)(0x3446694DULL), a3);
    a3 = 0;
    if (result != 0) goto loc_00ABE0BA;
    if (v_stack_mD8 == 0) goto loc_00ABE50B;
    v_r13 = (unsigned int)((v_r13) >> (1));
    goto loc_00ABE079;
loc_00ABE0BA:
    *(unsigned int *)(result) = (unsigned int)(v_r13);
    *(unsigned int *)(result + 4) = 0;
    v_stack_mD8 = 0;
    v_stack_mD4 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)))) != 1) goto loc_00ABE115;
    if ((v_r12 + v_rdi * 1) >= = (*(unsigned __int64 *)(v_rsp - 79 - 113))) {
        v_r12 = *(unsigned __int64 *)(v_rsp - 79 - 113);
        v_r12 = (v_r12) - (v_rdi);
        v_r12 = (unsigned int)(v_r12);
    }
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00ABE115;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 96)) & (-8);
    if (((*(unsigned int *)(result + 56)) & (0x1000ULL)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
        v_rdi = *(unsigned __int64 *)(a1 + 8);
        v_rdi = (v_rdi) - (*(unsigned __int64 *)(result + 64));
        v_rdi = (v_rdi) >> (3);
        v_rdi = (v_rdi) << (12);
    }
    v_r12 = (v_r12) + (0xFFFULL);
    v_r12 = (v_r12) & (0xFFFFFFFFFFFFF000ULL);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)))) != 1) goto loc_00ABE130;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (2)) != 0) goto loc_00ABE159;
loc_00ABE130:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119))) | (8));
    result = MiChangingSubsectionProtos(0, a2, v_rsp - 79 - 89, a3);
    v_stack_mD0 = (unsigned int)(result);
    if (sign_flag) goto loc_00ABE4F0;
    v_stack_mD4 = 1;
loc_00ABE159:
    v_stack_mE8 = result;
    result = FsRtlGetFileExtents(result, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)), v_rdi, v_r12);
    a1 = 0;
    v_stack_mD0 = (unsigned int)(result);
    if (sign_flag) goto loc_00ABE4CC;
    if ((*(unsigned int *)(result + 4)) <= ((unsigned int)(v_r13))) goto loc_00ABE1B2;
    if (v_stack_mD4 != 0) {
        a3 = 0;
        a2 = v_rsp - 79 - 89;
        a1 = 0;
        result = MiUnlinkSubsectionWaitBlock(a1, a2, a3, v_r12);
    }
    a2 = 0;
    *(unsigned int *)(result + 4) = (unsigned int)(v_r13);
    result = ExFreePoolWithTag(result, a2, a3, v_r12);
    goto loc_00ABE079;
loc_00ABE1B2:
    result = MiDereferenceControlAreaFile(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(v_rsp - 79 - 105), a3, v_r12);
    result = MiNewPfnsSuitable(result, *(unsigned __int64 *)(v_rsp - 79 - 105), a3, v_r12);
    v_rbx = 0;
    if ((unsigned int)(result) == 0) goto loc_00ABE493;
    v_stack_mD8 = 3;
    v_stack_mD0 = 0;
    if ((*(unsigned int *)(result + 4)) != 0) goto loc_00ABE211;
    if (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (64)) != 0) goto loc_00ABE2A4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)))) == 1) goto loc_00ABE2A4;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    if (((unsigned __int8)(result)) != 8) goto loc_00ABE24A;
loc_00ABE207:
    goto loc_00ABE498;
loc_00ABE211:
    result = MiConvertRunsToPages(result, *(unsigned __int64 *)(v_rsp - 79 - 105), v_stack_mD0, v_stack_mD8);
    if (result == 0) goto loc_00ABE207;
    if (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (64)) == 0) goto loc_00ABE235;
    if (v_stack_mD8 > 1) goto loc_00ABE2AE;
loc_00ABE235:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)))) != 1) goto loc_00ABE245;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (2)) != 0) goto loc_00ABE2B8;
loc_00ABE245:
loc_00ABE24A:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119))) | (16));
    result = MiChangingSubsectionProtos(a1, a2, v_rsp - 79 - 89, v_stack_mD8);
    if (!sign_flag) goto loc_00ABE2E1;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 79 - 89, v_stack_mD8);
    a3 = 0;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_mD8);
        a3 = 0;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000434ULL) goto loc_00ABE48C;
    goto loc_00ABDFB4;
loc_00ABE29D:
    result = 0;
    goto loc_00ABE51B;
loc_00ABE2A4:
    goto loc_00ABE498;
loc_00ABE2AE:
    goto loc_00ABE498;
loc_00ABE2B8:
loc_00ABE2BD:
loc_00ABE2C1:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, *(unsigned __int64 *)(v_rsp - 79 + 103));
    v_rsi = 0;
    if (*(unsigned __int64 *)(v_rsp - 79 - 121) == 0) goto loc_00ABE376;
    goto loc_00ABE3E3;
loc_00ABE2E1:
    if (result == 0) goto loc_00ABE305;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    if (((unsigned __int8)(result)) != 4) goto loc_00ABE305;
    if (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (1)) == 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 79 + 103);
        a3 = *(unsigned __int64 *)(v_rsp - 79 + 103);
        a2 = result;
        result = MiEliminateStaleExtents(a1, a2, a3, *(unsigned __int64 *)(v_rsp - 79 + 103));
    }
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 121))) == 1) goto loc_00ABE2BD;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    if (((unsigned __int8)(result)) != 8) goto loc_00ABE2BD;
    if (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (1)) == 0) goto loc_00ABE337;
    a2 = 0;
    result = MiInsertCopyExtents(0, a2, a2 + 1, *(unsigned __int64 *)(v_rsp - 79 + 103));
    if (result != 0) goto loc_00ABE2C1;
    goto loc_00ABE35F;
loc_00ABE337:
    result = MiMergeCopyExtents(a1, 0, a2 + 1, v_rsp - 79 - 121);
    result = 0;
    if (!sign_flag) goto loc_00ABE2BD;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000020AULL) { v_rbx = 0; }
loc_00ABE35F:
    a4 = 0;
    a3 = 0;
    result = MiSubsectionProtosCreated(a1, v_rsp - 79 - 89, a3, a4);
    goto loc_00ABE4B3;
loc_00ABE376:
    if (result == 0) goto loc_00ABE3C2;
    a1 = (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 56)) & (32)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (1)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00ABE3C2;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    if (((unsigned __int8)(result)) == 4) {
        result = *(unsigned __int64 *)(v_rsp - 79 - 25);
        a1 = v_rsp - 79 - 49;
        result = (result) & (-4);
        *(unsigned __int64 *)(v_rsp - 79 - 9) = *(unsigned __int64 *)(v_rsp - 79 + 103);
        result = (result) | (4);
        a2 = 1;
        *(unsigned __int64 *)(v_rsp - 79 - 25) = result;
        result = *(unsigned __int64 *)(v_rsp - 79 + 103);
        *(unsigned __int64 *)(v_rsp - 79 - 17) = result;
        result = MiUpdateSystemProtoPtesTree(a1, a2, a3, a4);
    }
    v_stack_mE8 = *(unsigned __int64 *)(v_rsp - 79 + 103);
    result = MiCreateFileOnlyPfns(a1, *(unsigned __int64 *)(v_rsp - 79 + 103), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), result);
    if (sign_flag) goto loc_00ABE43E;
loc_00ABE3E3:
    if (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (1)) == 0) goto loc_00ABE434;
    if (((*(unsigned __int8 *)(v_rsp - 79 + 119)) & (64)) != 0) {
        *(unsigned int *)(a1 + 108) = 2;
    }
    result = MiSetSubsectionBase(a1, *(unsigned __int64 *)(v_rsp - 79 + 103), (unsigned int)(v_stack_mD8), *(unsigned __int64 *)(v_rsp - 79 - 121));
    if ((*(unsigned __int64 *)(v_rsp - 79 - 17)) == 0) goto loc_00ABE425;
    result = MiReplaceSystemProtoPtesNode(v_rsp - 79 - 49, a1 + 120, (unsigned int)(v_stack_mD8), *(unsigned __int64 *)(v_rsp - 79 - 121));
    goto loc_00ABE44F;
loc_00ABE425:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) != 0) goto loc_00ABE44F;
    goto loc_00ABE44A;
loc_00ABE434:
    if (0 == 0) goto loc_00ABE44F;
    goto loc_00ABE44F;
loc_00ABE43E:
    if ((*(unsigned __int64 *)(v_rsp - 79 - 17)) == 0) goto loc_00ABE44F;
    a2 = 0;
loc_00ABE44A:
    result = MiUpdateSystemProtoPtesTree(v_rsp - 79 - 49, a2, (unsigned int)(v_stack_mD8), *(unsigned __int64 *)(v_rsp - 79 - 121));
loc_00ABE44F:
    if ((*(unsigned int *)(v_rsp - 79 + 87)) != 1) goto loc_00ABE45D;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (2)) == 0) {
        a3 = *(unsigned int *)(v_rsp - 79 + 111);
        a2 = v_rsp - 79 - 89;
        a4 = 0;
        a1 = a1;
        result = MiSubsectionProtosCreated(a1, a2, a3, a4);
    }
    if (0 != 0) {
        a1 = 0;
        result = MiDeleteFileExtentList(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    goto loc_00ABE51B;
loc_00ABE493:
loc_00ABE498:
    a1 = 0;
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    if (v_stack_mD4 != 0) {
        a3 = 0;
        a2 = v_rsp - 79 - 89;
        a1 = 0;
        result = MiUnlinkSubsectionWaitBlock(a1, a2, a3, a4);
    }
loc_00ABE4B3:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rsp - 79 - 121) == 0) goto loc_00ABE48C;
    result = MiDeleteFileExtentList(*(unsigned __int64 *)(v_rsp - 79 - 121), a2, a3, a4);
    goto loc_00ABE48C;
loc_00ABE4CC:
    result = MiDereferenceControlAreaFile(*(unsigned __int64 *)(a1), (unsigned int)(0xC0000427ULL), a3, a4);
    result = 0;
    if (v_stack_mD4 == 0) goto loc_00ABE4FB;
    a3 = 0;
    result = MiUnlinkSubsectionWaitBlock(a1, v_rsp - 79 - 89, a3, a4);
    goto loc_00ABE4FB;
loc_00ABE4F0:
    result = MiDereferenceControlAreaFile(*(unsigned __int64 *)(a1), (unsigned int)(0xC0000427ULL), a3, a4);
loc_00ABE4FB:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, a4);
    goto loc_00ABE51B;
loc_00ABE50B:
    result = MiDereferenceControlAreaFile(*(unsigned __int64 *)(a1), (unsigned int)(0xC0000427ULL), a3, a4);
loc_00ABE51B:
    v_rsp = (v_rsp) + (200);
    return (unsigned int)(0xC000009AULL);
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateFileExtents(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (200);
    Arg3 = 0;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x71) = 0;
    result = (uint32_t)(((uint32_t)(Arg4)) << (12));
    *(uint64_t *)(local_rsp - 0x4F - 0x61) = result;
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x49) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x79) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x31) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x4F - 0x21) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = v_xmm1;
loc_00ABDFB4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) == 0) goto loc_00ABE025;
    *(uint32_t *)(local_rsp - 0x4F + 0x57) = 1;
    if ((*(uint64_t *)(arg1 + 0x8)) != 0) goto loc_00ABDFD7;
    local_rdi = ((uint32_t)(Arg2)) << (12);
    goto loc_00ABDFE9;
loc_00ABDFD7:
    result = MiStartingOffset(0, 0, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x7F)), Arg3);
loc_00ABDFE9:
    result = MiEndingOffset(0, 0, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x7F)), Arg3);
    *(uint64_t *)(local_rsp - 0x4F - 0x71) = result;
    if (result != result) goto loc_00ABE003;
    if (result == 0) goto loc_00ABE29D;
loc_00ABE003:
    if ((result + result * 1) <= result) goto loc_00ABE04A;
    local_r12 = (result) - (result);
    local_r12 = ((uint32_t)((uint32_t)(local_r12))) + (511);
    local_r12 = (local_r12) & (-512);
    goto loc_00ABE04A;
loc_00ABE025:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (0xFFC0ULL));
    local_rdi = (local_rdi) << (26);
    local_rdi = (local_rdi) | ((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    *(uint32_t *)(local_rsp - 0x4F + 0x57) = 2;
    local_rdi = (local_rdi) + (0);
    local_rdi = (local_rdi) << (12);
loc_00ABE04A:
    result = MiReferenceControlAreaFile(*(uint64_t *)(arg1), 0, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x7F)), Arg3);
    *(uint64_t *)(local_rsp - 0x4F - 0x69) = result;
    Arg2 = (0) << (32);
    result = (result) | (Arg2);
    v_stack_mD8 = 1;
    local_r13 = (result) >> (4);
    local_r13 = (uint32_t)((local_r13) & (7));
    local_r13 = (uint32_t)((local_r13) + (8));
loc_00ABE079:
    if (((uint32_t)(local_r13)) < 1) goto loc_00ABE50B;
    Arg2 = (local_r13 - 1) << (4);
    Arg2 = (Arg2) + (24);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x3446694DULL), Arg3);
    Arg3 = 0;
    if (result != 0) goto loc_00ABE0BA;
    if (v_stack_mD8 == 0) goto loc_00ABE50B;
    local_r13 = (uint32_t)((local_r13) >> (1));
    goto loc_00ABE079;
loc_00ABE0BA:
    *(uint32_t *)(result) = (uint32_t)(local_r13);
    *(uint32_t *)(result + 0x4) = 0;
    v_stack_mD8 = 0;
    v_stack_mD4 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)))) != 1) goto loc_00ABE115;
    if ((local_r12 + local_rdi * 1) >= = (*(uint64_t *)(local_rsp - 0x4F - 0x71))) {
        local_r12 = *(uint64_t *)(local_rsp - 0x4F - 0x71);
        local_r12 = (local_r12) - (local_rdi);
        local_r12 = (uint32_t)(local_r12);
    }
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00ABE115;
    result = (*(uint64_t *)(*(uint64_t *)(arg1) + 0x60)) & (-8);
    if (((*(uint32_t *)(result + 0x38)) & (0x1000ULL)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1));
        local_rdi = *(uint64_t *)(arg1 + 0x8);
        local_rdi = (local_rdi) - (*(uint64_t *)(result + 0x40));
        local_rdi = (local_rdi) >> (3);
        local_rdi = (local_rdi) << (12);
    }
    local_r12 = (local_r12) + (0xFFFULL);
    local_r12 = (local_r12) & (0xFFFFFFFFFFFFF000ULL);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)))) != 1) goto loc_00ABE130;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (2)) != 0) goto loc_00ABE159;
loc_00ABE130:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77))) | (8));
    result = MiChangingSubsectionProtos(0, Arg2, local_rsp - 79 - 89, Arg3);
    v_stack_mD0 = (uint32_t)(result);
    if (sign_flag) goto loc_00ABE4F0;
    v_stack_mD4 = 1;
loc_00ABE159:
    v_stack_mE8 = result;
    result = FsRtlGetFileExtents(result, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)), local_rdi, local_r12);
    Arg1 = 0;
    v_stack_mD0 = (uint32_t)(result);
    if (sign_flag) goto loc_00ABE4CC;
    if ((*(uint32_t *)(result + 0x4)) <= ((uint32_t)(local_r13))) goto loc_00ABE1B2;
    if (v_stack_mD4 != 0) {
        Arg3 = 0;
        Arg2 = local_rsp - 79 - 89;
        Arg1 = 0;
        result = MiUnlinkSubsectionWaitBlock(Arg1, Arg2, Arg3, local_r12);
    }
    Arg2 = 0;
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_r13);
    result = ExFreePoolWithTag(result, Arg2, Arg3, local_r12);
    goto loc_00ABE079;
loc_00ABE1B2:
    result = MiDereferenceControlAreaFile(*(uint64_t *)(arg1), *(uint64_t *)(local_rsp - 0x4F - 0x69), Arg3, local_r12);
    result = MiNewPfnsSuitable(result, *(uint64_t *)(local_rsp - 0x4F - 0x69), Arg3, local_r12);
    local_rbx = 0;
    if ((uint32_t)(result) == 0) goto loc_00ABE493;
    v_stack_mD8 = 3;
    v_stack_mD0 = 0;
    if ((*(uint32_t *)(result + 0x4)) != 0) goto loc_00ABE211;
    if (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (64)) != 0) goto loc_00ABE2A4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)))) == 1) goto loc_00ABE2A4;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    if (((uint8_t)(result)) != 8) goto loc_00ABE24A;
loc_00ABE207:
    goto loc_00ABE498;
loc_00ABE211:
    result = MiConvertRunsToPages(result, *(uint64_t *)(local_rsp - 0x4F - 0x69), v_stack_mD0, v_stack_mD8);
    if (result == 0) goto loc_00ABE207;
    if (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (64)) == 0) goto loc_00ABE235;
    if (v_stack_mD8 > 1) goto loc_00ABE2AE;
loc_00ABE235:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)))) != 1) goto loc_00ABE245;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (2)) != 0) goto loc_00ABE2B8;
loc_00ABE245:
loc_00ABE24A:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77))) | (16));
    result = MiChangingSubsectionProtos(Arg1, Arg2, local_rsp - 79 - 89, v_stack_mD8);
    if (!sign_flag) goto loc_00ABE2E1;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 79 - 89, v_stack_mD8);
    Arg3 = 0;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_mD8);
        Arg3 = 0;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000434ULL) goto loc_00ABE48C;
    goto loc_00ABDFB4;
loc_00ABE29D:
    result = 0;
    goto loc_00ABE51B;
loc_00ABE2A4:
    goto loc_00ABE498;
loc_00ABE2AE:
    goto loc_00ABE498;
loc_00ABE2B8:
loc_00ABE2BD:
loc_00ABE2C1:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, Arg3, *(uint64_t *)(local_rsp - 0x4F + 0x67));
    local_rsi = 0;
    if (*(uint64_t *)(local_rsp - 0x4F - 0x79) == 0) goto loc_00ABE376;
    goto loc_00ABE3E3;
loc_00ABE2E1:
    if (result == 0) goto loc_00ABE305;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    if (((uint8_t)(result)) != 4) goto loc_00ABE305;
    if (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (1)) == 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
        Arg3 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
        Arg2 = result;
        result = MiEliminateStaleExtents(Arg1, Arg2, Arg3, *(uint64_t *)(local_rsp - 0x4F + 0x67));
    }
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x79))) == 1) goto loc_00ABE2BD;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    if (((uint8_t)(result)) != 8) goto loc_00ABE2BD;
    if (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (1)) == 0) goto loc_00ABE337;
    Arg2 = 0;
    result = MiInsertCopyExtents(0, Arg2, Arg2 + 1, *(uint64_t *)(local_rsp - 0x4F + 0x67));
    if (result != 0) goto loc_00ABE2C1;
    goto loc_00ABE35F;
loc_00ABE337:
    result = MiMergeCopyExtents(Arg1, 0, Arg2 + 1, local_rsp - 79 - 121);
    result = 0;
    if (!sign_flag) goto loc_00ABE2BD;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000020AULL) { local_rbx = 0; }
loc_00ABE35F:
    Arg4 = 0;
    Arg3 = 0;
    result = MiSubsectionProtosCreated(Arg1, local_rsp - 79 - 89, Arg3, Arg4);
    goto loc_00ABE4B3;
loc_00ABE376:
    if (result == 0) goto loc_00ABE3C2;
    Arg1 = (((*(uint8_t *)(*(uint64_t *)(arg1) + 0x38)) & (32)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (1)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00ABE3C2;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    if (((uint8_t)(result)) == 4) {
        result = *(uint64_t *)(local_rsp - 0x4F - 0x19);
        Arg1 = local_rsp - 79 - 49;
        result = (result) & (-4);
        *(uint64_t *)(local_rsp - 0x4F - 0x9) = *(uint64_t *)(local_rsp - 0x4F + 0x67);
        result = (result) | (4);
        Arg2 = 1;
        *(uint64_t *)(local_rsp - 0x4F - 0x19) = result;
        result = *(uint64_t *)(local_rsp - 0x4F + 0x67);
        *(uint64_t *)(local_rsp - 0x4F - 0x11) = result;
        result = MiUpdateSystemProtoPtesTree(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mE8 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    result = MiCreateFileOnlyPfns(Arg1, *(uint64_t *)(local_rsp - 0x4F + 0x67), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), result);
    if (sign_flag) goto loc_00ABE43E;
loc_00ABE3E3:
    if (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (1)) == 0) goto loc_00ABE434;
    if (((*(uint8_t *)(local_rsp - 0x4F + 0x77)) & (64)) != 0) {
        *(uint32_t *)(arg1 + 0x6C) = 2;
    }
    result = MiSetSubsectionBase(Arg1, *(uint64_t *)(local_rsp - 0x4F + 0x67), (uint32_t)(v_stack_mD8), *(uint64_t *)(local_rsp - 0x4F - 0x79));
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x11)) == 0) goto loc_00ABE425;
    result = MiReplaceSystemProtoPtesNode(local_rsp - 79 - 49, Arg1 + 120, (uint32_t)(v_stack_mD8), *(uint64_t *)(local_rsp - 0x4F - 0x79));
    goto loc_00ABE44F;
loc_00ABE425:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) != 0) goto loc_00ABE44F;
    goto loc_00ABE44A;
loc_00ABE434:
    if (0 == 0) goto loc_00ABE44F;
    goto loc_00ABE44F;
loc_00ABE43E:
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x11)) == 0) goto loc_00ABE44F;
    Arg2 = 0;
loc_00ABE44A:
    result = MiUpdateSystemProtoPtesTree(local_rsp - 79 - 49, Arg2, (uint32_t)(v_stack_mD8), *(uint64_t *)(local_rsp - 0x4F - 0x79));
loc_00ABE44F:
    if ((*(uint32_t *)(local_rsp - 0x4F + 0x57)) != 1) goto loc_00ABE45D;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (2)) == 0) {
        Arg3 = *(uint32_t *)(local_rsp - 0x4F + 0x6F);
        Arg2 = local_rsp - 79 - 89;
        Arg4 = 0;
        Arg1 = Arg1;
        result = MiSubsectionProtosCreated(Arg1, Arg2, Arg3, Arg4);
    }
    if (0 != 0) {
        Arg1 = 0;
        result = MiDeleteFileExtentList(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00ABE51B;
loc_00ABE493:
loc_00ABE498:
    Arg1 = 0;
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    if (v_stack_mD4 != 0) {
        Arg3 = 0;
        Arg2 = local_rsp - 79 - 89;
        Arg1 = 0;
        result = MiUnlinkSubsectionWaitBlock(Arg1, Arg2, Arg3, Arg4);
    }
loc_00ABE4B3:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(local_rsp - 0x4F - 0x79) == 0) goto loc_00ABE48C;
    result = MiDeleteFileExtentList(*(uint64_t *)(local_rsp - 0x4F - 0x79), Arg2, Arg3, Arg4);
    goto loc_00ABE48C;
loc_00ABE4CC:
    result = MiDereferenceControlAreaFile(*(uint64_t *)(arg1), (uint32_t)(0xC0000427ULL), Arg3, Arg4);
    result = 0;
    if (v_stack_mD4 == 0) goto loc_00ABE4FB;
    Arg3 = 0;
    result = MiUnlinkSubsectionWaitBlock(Arg1, local_rsp - 79 - 89, Arg3, Arg4);
    goto loc_00ABE4FB;
loc_00ABE4F0:
    result = MiDereferenceControlAreaFile(*(uint64_t *)(arg1), (uint32_t)(0xC0000427ULL), Arg3, Arg4);
loc_00ABE4FB:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, Arg3, Arg4);
    goto loc_00ABE51B;
loc_00ABE50B:
    result = MiDereferenceControlAreaFile(*(uint64_t *)(arg1), (uint32_t)(0xC0000427ULL), Arg3, Arg4);
loc_00ABE51B:
    local_rsp = (local_rsp) + (200);
    return (uint32_t)(0xC000009AULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x6C` | `32` | `W` |
| `Arg1` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABDF54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
