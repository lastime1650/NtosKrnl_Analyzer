# CmSaveMergedKeys

- RVA: `0x007DE040`–`0x007DE521` (길이 `1,249` bytes)
- VA: `0x00000001407DE040`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093850`
- 디코드: `325`개 명령, `1,249/1,249` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007DE0C6` → [CmpUuidCreate](../AB/CmpUuidCreate_function_00AB81F8.md) (function, `0x00AB81F8`)
- `0x007DE0D9` → [CmpUuidCreate](../AB/CmpUuidCreate_function_00AB81F8.md) (function, `0x00AB81F8`)
- `0x007DE110` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DE11F` → [CmpLockTwoKcbsShared](../84/CmpLockTwoKcbsShared_function_008485B4.md) (function, `0x008485B4`)
- `0x007DE148` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x007DE15A` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x007DE19B` → [CmpCreateTemporaryHive](CmpCreateTemporaryHive_function_007DE528.md) (function, `0x007DE528`)
- `0x007DE1BB` → [CmpBlockTwoHiveWrites](../84/CmpBlockTwoHiveWrites_function_0084DE64.md) (function, `0x0084DE64`)
- `0x007DE1D2` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (function, `0x00BC996C`)
- `0x007DE1F3` → [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) (function, `0x00BC9CD0`)
- `0x007DE1FD` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x007DE20D` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (function, `0x00BC996C`)
- `0x007DE22A` → [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) (function, `0x00BC9CD0`)
- `0x007DE234` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x007DE244` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DE272` → [CmpCopyKeyPartial](../85/CmpCopyKeyPartial_function_0085AFF4.md) (function, `0x0085AFF4`)
- `0x007DE2A7` → [CmpCopySyncTree](../7F/CmpCopySyncTree_function_007F21A0.md) (function, `0x007F21A0`)
- `0x007DE2B9` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DE2D6` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DE2DD` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DE307` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DE30E` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DE337` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DE356` → [CmpMergeKeyValues](../7F/CmpMergeKeyValues_function_007F2304.md) (function, `0x007F2304`)
- `0x007DE371` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DE378` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DE38D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DE394` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DE3B3` → [CmpCopySyncTree](../7F/CmpCopySyncTree_function_007F21A0.md) (function, `0x007F21A0`)
- `0x007DE3C4` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DE3CC` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DE3D9` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x007DE3DE` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DE3F1` → [HvWriteExternal](../A8/HvWriteExternal_function_00A83C20.md) (function, `0x00A83C20`)
- `0x007DE401` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DE41B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DE422` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DE42A` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DE438` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DE446` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DE45E` → [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x007DE470` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x007DE475` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DE482` → [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) (function, `0x009B1708`)
- `0x007DE4A7` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007DE4ED` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007DE500` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtSaveMergedKeys](../7E/NtSaveMergedKeys_function_007E1070.md) at `0x007E12CE`

### Static image references
- `0x007DE05C` → RVA `0x00E0A740` (`.data`; read)
- `0x007DE0E8` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x007DE48E` → RVA `0x00E09F58` (`.data`; read)
- `0x007DE4C0` → RVA `0x00055F7E` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x007DE110` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE148` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE15A` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE1D2` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE1F3` → [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE1FD` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE20D` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE22A` → [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE234` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE244` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE2B9` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE3C4` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE3CC` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE3DE` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE42A` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE438` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE446` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE475` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DE4A7` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007DE4ED` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007DE500` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007DE040  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
007DE045  55                              push rbp
007DE046  56                              push rsi
007DE047  57                              push rdi
007DE048  41 54                           push r12
007DE04A  41 55                           push r13
007DE04C  41 56                           push r14
007DE04E  41 57                           push r15
007DE050  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
007DE055  48 81 EC E0 00 00 00            sub rsp, 0xe0
007DE05C  48 8B 05 DD C6 62 00            mov rax, qword ptr [rip + 0x62c6dd]
007DE063  48 33 C4                        xor rax, rsp
007DE066  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007DE06A  48 8B F1                        mov rsi, rcx
007DE06D  44 88 4D 87                     mov byte ptr [rbp - 0x79], r9b
007DE071  33 C9                           xor ecx, ecx
007DE073  4C 89 45 BF                     mov qword ptr [rbp - 0x41], r8
007DE077  4C 8B E2                        mov r12, rdx
007DE07A  89 4D 8B                        mov dword ptr [rbp - 0x75], ecx
007DE07D  83 CA FF                        or edx, 0xffffffff
007DE080  89 4D A3                        mov dword ptr [rbp - 0x5d], ecx
007DE083  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
007DE087  0F 57 C0                        xorps xmm0, xmm0
007DE08A  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
007DE08E  4D 8B 6C 24 08                  mov r13, qword ptr [r12 + 8]
007DE093  8B F9                           mov edi, ecx
007DE095  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
007DE099  0F 57 C9                        xorps xmm1, xmm1
007DE09C  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
007DE0A0  4C 8B 78 20                     mov r15, qword ptr [rax + 0x20]
007DE0A4  8B 40 28                        mov eax, dword ptr [rax + 0x28]
007DE0A7  4D 8B 75 20                     mov r14, qword ptr [r13 + 0x20]
007DE0AB  89 45 A7                        mov dword ptr [rbp - 0x59], eax
007DE0AE  41 8B 45 28                     mov eax, dword ptr [r13 + 0x28]
007DE0B2  89 4D 9B                        mov dword ptr [rbp - 0x65], ecx
007DE0B5  48 8D 4D D7                     lea rcx, [rbp - 0x29]
007DE0B9  89 45 8F                        mov dword ptr [rbp - 0x71], eax
007DE0BC  89 55 9F                        mov dword ptr [rbp - 0x61], edx
007DE0BF  89 55 97                        mov dword ptr [rbp - 0x69], edx
007DE0C2  4C 89 6D AF                     mov qword ptr [rbp - 0x51], r13
007DE0C6  E8 2D A1 2D 00                  call 0x140ab81f8
007DE0CB  8B D8                           mov ebx, eax
007DE0CD  85 C0                           test eax, eax
007DE0CF  0F 88 22 04 00 00               js 0x1407de4f7
007DE0D5  48 8D 4D C7                     lea rcx, [rbp - 0x39]
007DE0D9  E8 1A A1 2D 00                  call 0x140ab81f8
007DE0DE  8B D8                           mov ebx, eax
007DE0E0  85 C0                           test eax, eax
007DE0E2  0F 88 0F 04 00 00               js 0x1407de4f7
007DE0E8  48 8B 05 A1 B9 7F 00            mov rax, qword ptr [rip + 0x7fb9a1]
007DE0EF  4C 3B F0                        cmp r14, rax
007DE0F2  0F 84 91 03 00 00               je 0x1407de489
007DE0F8  4C 3B F8                        cmp r15, rax
007DE0FB  0F 84 88 03 00 00               je 0x1407de489
007DE101  4D 3B F7                        cmp r14, r15
007DE104  75 0A                           jne 0x1407de110
007DE106  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007DE10B  E9 E7 03 00 00                  jmp 0x1407de4f7
007DE110  E8 1F BA 3E 00                  call 0x140bc9b34
007DE115  48 8B 5D B7                     mov rbx, qword ptr [rbp - 0x49]
007DE119  49 8B D5                        mov rdx, r13
007DE11C  48 8B CB                        mov rcx, rbx
007DE11F  E8 90 A4 06 00                  call 0x1408485b4
007DE124  33 C0                           xor eax, eax
007DE126  41 B5 01                        mov r13b, 1
007DE129  66 39 43 42                     cmp word ptr [rbx + 0x42], ax
007DE12D  0F 85 26 03 00 00               jne 0x1407de459
007DE133  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
007DE137  33 DB                           xor ebx, ebx
007DE139  66 39 58 42                     cmp word ptr [rax + 0x42], bx
007DE13D  0F 85 16 03 00 00               jne 0x1407de459
007DE143  33 D2                           xor edx, edx
007DE145  48 8B CE                        mov rcx, rsi
007DE148  E8 33 B3 3E 00                  call 0x140bc9480
007DE14D  84 C0                           test al, al
007DE14F  0F 85 FD 02 00 00               jne 0x1407de452
007DE155  33 D2                           xor edx, edx
007DE157  49 8B CC                        mov rcx, r12
007DE15A  E8 21 B3 3E 00                  call 0x140bc9480
007DE15F  84 C0                           test al, al
007DE161  0F 85 EB 02 00 00               jne 0x1407de452
007DE167  41 8B 87 A0 00 00 00            mov eax, dword ptr [r15 + 0xa0]
007DE16E  A8 02                           test al, 2
007DE170  74 06                           je 0x1407de178
007DE172  41 39 5F 68                     cmp dword ptr [r15 + 0x68], ebx
007DE176  75 11                           jne 0x1407de189
007DE178  41 8B 86 A0 00 00 00            mov eax, dword ptr [r14 + 0xa0]
007DE17F  A8 02                           test al, 2
007DE181  74 10                           je 0x1407de193
007DE183  41 39 5E 68                     cmp dword ptr [r14 + 0x68], ebx
007DE187  74 0A                           je 0x1407de193
007DE189  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007DE18E  E9 D5 02 00 00                  jmp 0x1407de468
007DE193  48 8D 55 C7                     lea rdx, [rbp - 0x39]
007DE197  48 8D 4D D7                     lea rcx, [rbp - 0x29]
007DE19B  E8 88 03 00 00                  call 0x1407de528
007DE1A0  48 8B F8                        mov rdi, rax
007DE1A3  48 85 C0                        test rax, rax
007DE1A6  75 0A                           jne 0x1407de1b2
007DE1A8  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DE1AD  E9 B6 02 00 00                  jmp 0x1407de468
007DE1B2  45 33 C0                        xor r8d, r8d
007DE1B5  49 8B D7                        mov rdx, r15
007DE1B8  49 8B CE                        mov rcx, r14
007DE1BB  E8 A4 FC 06 00                  call 0x14084de64
007DE1C0  8B D8                           mov ebx, eax
007DE1C2  85 C0                           test eax, eax
007DE1C4  0F 88 9E 02 00 00               js 0x1407de468
007DE1CA  49 8B CF                        mov rcx, r15
007DE1CD  BE 06 00 00 00                  mov esi, 6
007DE1D2  E8 95 B7 3E 00                  call 0x140bc996c
007DE1D7  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
007DE1DB  41 B9 19 00 02 00               mov r9d, 0x20019
007DE1E1  44 8A 45 87                     mov r8b, byte ptr [rbp - 0x79]
007DE1E5  41 8B D4                        mov edx, r12d
007DE1E8  49 8B CF                        mov rcx, r15
007DE1EB  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
007DE1F3  E8 D8 BA 3E 00                  call 0x140bc9cd0
007DE1F8  49 8B CF                        mov rcx, r15
007DE1FB  8B D8                           mov ebx, eax
007DE1FD  E8 C6 B7 3E 00                  call 0x140bc99c8
007DE202  85 DB                           test ebx, ebx
007DE204  0F 88 1D 02 00 00               js 0x1407de427
007DE20A  49 8B CE                        mov rcx, r14
007DE20D  E8 5A B7 3E 00                  call 0x140bc996c
007DE212  44 8A 45 87                     mov r8b, byte ptr [rbp - 0x79]
007DE216  41 B9 19 00 02 00               mov r9d, 0x20019
007DE21C  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
007DE21F  49 8B CE                        mov rcx, r14
007DE222  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
007DE22A  E8 A1 BA 3E 00                  call 0x140bc9cd0
007DE22F  49 8B CE                        mov rcx, r14
007DE232  8B D8                           mov ebx, eax
007DE234  E8 8F B7 3E 00                  call 0x140bc99c8
007DE239  85 DB                           test ebx, ebx
007DE23B  0F 88 E6 01 00 00               js 0x1407de427
007DE241  48 8B CF                        mov rcx, rdi
007DE244  E8 07 BA 3E 00                  call 0x140bc9c50
007DE249  48 8D 45 8B                     lea rax, [rbp - 0x75]
007DE24D  41 83 C9 FF                     or r9d, 0xffffffff
007DE251  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007DE256  4C 8B C7                        mov r8, rdi
007DE259  33 C0                           xor eax, eax
007DE25B  41 8B D4                        mov edx, r12d
007DE25E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007DE262  49 8B CF                        mov rcx, r15
007DE265  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
007DE26D  BE 07 00 00 00                  mov esi, 7
007DE272  E8 7D CD 07 00                  call 0x14085aff4
007DE277  33 C9                           xor ecx, ecx
007DE279  8B D8                           mov ebx, eax
007DE27B  85 C0                           test eax, eax
007DE27D  0F 88 A4 01 00 00               js 0x1407de427
007DE283  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DE287  4C 8B C7                        mov r8, rdi
007DE28A  44 8B 65 8B                     mov r12d, dword ptr [rbp - 0x75]
007DE28E  45 8B CC                        mov r9d, r12d
007DE291  8B 55 A7                        mov edx, dword ptr [rbp - 0x59]
007DE294  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
007DE298  49 8B CF                        mov rcx, r15
007DE29B  44 89 60 24                     mov dword ptr [rax + 0x24], r12d
007DE29F  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007DE2A7  E8 F4 3E 01 00                  call 0x1407f21a0
007DE2AC  8B D8                           mov ebx, eax
007DE2AE  85 C0                           test eax, eax
007DE2B0  0F 88 71 01 00 00               js 0x1407de427
007DE2B6  49 8B CF                        mov rcx, r15
007DE2B9  E8 76 B9 3E 00                  call 0x140bc9c34
007DE2BE  4C 8D 45 97                     lea r8, [rbp - 0x69]
007DE2C2  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
007DE2C5  BE 05 00 00 00                  mov esi, 5
007DE2CA  49 8B CE                        mov rcx, r14
007DE2CD  45 84 AE 8C 00 00 00            test byte ptr [r14 + 0x8c], r13b
007DE2D4  74 07                           je 0x1407de2dd
007DE2D6  E8 85 69 07 00                  call 0x140854c60
007DE2DB  EB 05                           jmp 0x1407de2e2
007DE2DD  E8 CE 69 07 00                  call 0x140854cb0
007DE2E2  48 8B D8                        mov rbx, rax
007DE2E5  48 85 C0                        test rax, rax
007DE2E8  75 0A                           jne 0x1407de2f4
007DE2EA  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DE2EF  E9 33 01 00 00                  jmp 0x1407de427
007DE2F4  4C 8D 45 9F                     lea r8, [rbp - 0x61]
007DE2F8  41 8B D4                        mov edx, r12d
007DE2FB  48 8B CF                        mov rcx, rdi
007DE2FE  44 84 AF 8C 00 00 00            test byte ptr [rdi + 0x8c], r13b
007DE305  74 07                           je 0x1407de30e
007DE307  E8 54 69 07 00                  call 0x140854c60
007DE30C  EB 05                           jmp 0x1407de313
007DE30E  E8 9D 69 07 00                  call 0x140854cb0
007DE313  4C 8B E0                        mov r12, rax
007DE316  48 85 C0                        test rax, rax
007DE319  75 26                           jne 0x1407de341
007DE31B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DE320  49 8D 86 8C 00 00 00            lea rax, [r14 + 0x8c]
007DE327  49 8B CE                        mov rcx, r14
007DE32A  F6 00 01                        test byte ptr [rax], 1
007DE32D  48 8D 55 97                     lea rdx, [rbp - 0x69]
007DE331  0F 84 CA 00 00 00               je 0x1407de401
007DE337  E8 E4 E8 07 00                  call 0x14085cc20
007DE33C  E9 C5 00 00 00                  jmp 0x1407de406
007DE341  8B 45 8B                        mov eax, dword ptr [rbp - 0x75]
007DE344  4C 8B CF                        mov r9, rdi
007DE347  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
007DE34C  4C 8B C3                        mov r8, rbx
007DE34F  49 8B CE                        mov rcx, r14
007DE352  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007DE356  E8 A9 3F 01 00                  call 0x1407f2304
007DE35B  8B D8                           mov ebx, eax
007DE35D  85 C0                           test eax, eax
007DE35F  78 BF                           js 0x1407de320
007DE361  48 8D 55 97                     lea rdx, [rbp - 0x69]
007DE365  49 8B CE                        mov rcx, r14
007DE368  45 84 AE 8C 00 00 00            test byte ptr [r14 + 0x8c], r13b
007DE36F  74 07                           je 0x1407de378
007DE371  E8 AA E8 07 00                  call 0x14085cc20
007DE376  EB 05                           jmp 0x1407de37d
007DE378  E8 C3 7B 07 00                  call 0x140855f40
007DE37D  48 8D 55 9F                     lea rdx, [rbp - 0x61]
007DE381  48 8B CF                        mov rcx, rdi
007DE384  44 84 AF 8C 00 00 00            test byte ptr [rdi + 0x8c], r13b
007DE38B  74 07                           je 0x1407de394
007DE38D  E8 8E E8 07 00                  call 0x14085cc20
007DE392  EB 05                           jmp 0x1407de399
007DE394  E8 A7 7B 07 00                  call 0x140855f40
007DE399  44 8B 4D 8B                     mov r9d, dword ptr [rbp - 0x75]
007DE39D  B8 02 00 00 00                  mov eax, 2
007DE3A2  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
007DE3A5  4C 8B C7                        mov r8, rdi
007DE3A8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007DE3AC  49 8B CE                        mov rcx, r14
007DE3AF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007DE3B3  E8 E8 3D 01 00                  call 0x1407f21a0
007DE3B8  45 33 E4                        xor r12d, r12d
007DE3BB  8B D8                           mov ebx, eax
007DE3BD  85 C0                           test eax, eax
007DE3BF  78 66                           js 0x1407de427
007DE3C1  49 8B CE                        mov rcx, r14
007DE3C4  E8 6B B8 3E 00                  call 0x140bc9c34
007DE3C9  48 8B CF                        mov rcx, rdi
007DE3CC  E8 63 B8 3E 00                  call 0x140bc9c34
007DE3D1  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
007DE3D5  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
007DE3D9  E8 BE A2 06 00                  call 0x14084869c
007DE3DE  E8 A1 B6 3E 00                  call 0x140bc9a84
007DE3E3  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
007DE3E7  48 8B CF                        mov rcx, rdi
007DE3EA  48 89 87 18 06 00 00            mov qword ptr [rdi + 0x618], rax
007DE3F1  E8 2A 58 2A 00                  call 0x140a83c20
007DE3F6  8B D8                           mov ebx, eax
007DE3F8  4C 89 A7 18 06 00 00            mov qword ptr [rdi + 0x618], r12
007DE3FF  EB 7E                           jmp 0x1407de47f
007DE401  E8 3A 7B 07 00                  call 0x140855f40
007DE406  4D 85 E4                        test r12, r12
007DE409  74 1C                           je 0x1407de427
007DE40B  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DE412  48 8D 55 9F                     lea rdx, [rbp - 0x61]
007DE416  48 8B CF                        mov rcx, rdi
007DE419  74 07                           je 0x1407de422
007DE41B  E8 00 E8 07 00                  call 0x14085cc20
007DE420  EB 05                           jmp 0x1407de427
007DE422  E8 19 7B 07 00                  call 0x140855f40
007DE427  49 8B CE                        mov rcx, r14
007DE42A  E8 05 B8 3E 00                  call 0x140bc9c34
007DE42F  40 F6 C6 02                     test sil, 2
007DE433  74 08                           je 0x1407de43d
007DE435  49 8B CF                        mov rcx, r15
007DE438  E8 F7 B7 3E 00                  call 0x140bc9c34
007DE43D  40 F6 C6 01                     test sil, 1
007DE441  74 08                           je 0x1407de44b
007DE443  48 8B CF                        mov rcx, rdi
007DE446  E8 E9 B7 3E 00                  call 0x140bc9c34
007DE44B  45 84 ED                        test r13b, r13b
007DE44E  74 2F                           je 0x1407de47f
007DE450  EB 16                           jmp 0x1407de468
007DE452  BB 7C 01 00 C0                  mov ebx, 0xc000017c
007DE457  EB 0F                           jmp 0x1407de468
007DE459  B9 13 00 00 00                  mov ecx, 0x13
007DE45E  E8 DD 05 1D 00                  call 0x1409aea40
007DE463  BB 02 00 00 C0                  mov ebx, 0xc0000002
007DE468  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
007DE46C  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
007DE470  E8 27 A2 06 00                  call 0x14084869c
007DE475  E8 0A B6 3E 00                  call 0x140bc9a84
007DE47A  48 85 FF                        test rdi, rdi
007DE47D  74 78                           je 0x1407de4f7
007DE47F  48 8B CF                        mov rcx, rdi
007DE482  E8 81 32 1D 00                  call 0x1409b1708
007DE487  EB 6E                           jmp 0x1407de4f7
007DE489  BE 05 00 00 00                  mov esi, 5
007DE48E  39 35 C4 BA 62 00               cmp dword ptr [rip + 0x62bac4], esi
007DE494  76 5C                           jbe 0x1407de4f2
007DE496  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
007DE4A0  48 8D 0D B1 BA 62 00            lea rcx, [rip + 0x62bab1]
007DE4A7  E8 F4 05 C5 FF                  call 0x14042eaa0
007DE4AC  84 C0                           test al, al
007DE4AE  74 42                           je 0x1407de4f2
007DE4B0  48 8D 45 BF                     lea rax, [rbp - 0x41]
007DE4B4  48 C7 45 BF 00 00 00 01         mov qword ptr [rbp - 0x41], 0x1000000
007DE4BC  48 89 45 07                     mov qword ptr [rbp + 7], rax
007DE4C0  48 8D 15 B7 7A 87 FF            lea rdx, [rip - 0x788549]
007DE4C7  48 8D 45 E7                     lea rax, [rbp - 0x19]
007DE4CB  48 C7 45 0F 08 00 00 00         mov qword ptr [rbp + 0xf], 8
007DE4D3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007DE4D8  48 8D 0D 79 BA 62 00            lea rcx, [rip + 0x62ba79]
007DE4DF  45 33 C9                        xor r9d, r9d
007DE4E2  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
007DE4EA  45 33 C0                        xor r8d, r8d
007DE4ED  E8 EE 7B C4 FF                  call 0x1404260e0
007DE4F2  BB 22 00 00 C0                  mov ebx, 0xc0000022
007DE4F7  8B C3                           mov eax, ebx
007DE4F9  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
007DE4FD  48 33 CC                        xor rcx, rsp
007DE500  E8 3B E1 EC FF                  call 0x1406ac640
007DE505  48 8B 9C 24 30 01 00 00         mov rbx, qword ptr [rsp + 0x130]
007DE50D  48 81 C4 E0 00 00 00            add rsp, 0xe0
007DE514  41 5F                           pop r15
007DE516  41 5E                           pop r14
007DE518  41 5D                           pop r13
007DE51A  41 5C                           pop r12
007DE51C  5F                              pop rdi
007DE51D  5E                              pop rsi
007DE51E  5D                              pop rbp
007DE51F  C3                              ret
007DE520  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSaveMergedKeys(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 6473437)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mD8 = a4;
    a1 = 0;
    v_stack_mA0 = a3;
    v_stack_mD4 = 0;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_mBC = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mA8 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m98 = v_xmm1;
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)));
    v_stack_mC4 = 0;
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 40)));
    v_stack_mC0 = (unsigned int)(a2);
    v_stack_mC8 = (unsigned int)(a2);
    v_stack_mB0 = *(unsigned __int64 *)(a2 + 8);
    result = CmpUuidCreate(v_stack_m88, a2, a3, a4);
    if (sign_flag) goto loc_007DE4F7;
    result = CmpUuidCreate(v_stack_m98, a2, a3, a4);
    if (sign_flag) goto loc_007DE4F7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32)) == (*(unsigned __int64 *)(v_rip + 8370593))) goto loc_007DE489;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32)) == (*(unsigned __int64 *)(v_rip + 8370593))) goto loc_007DE489;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32))) goto loc_007DE110;
    goto loc_007DE4F7;
loc_007DE110:
    result = CmpLockRegistry(v_stack_m98, a2, a3, a4);
    result = CmpLockTwoKcbsShared(v_stack_mA8, *(unsigned __int64 *)(a2 + 8), a3, a4);
    result = 0;
    if ((*(unsigned __int16 *)(v_stack_mA8 + 66)) != 0) goto loc_007DE459;
    v_rbx = 0;
    if ((*(unsigned __int16 *)(v_stack_mB0 + 66)) != 0) goto loc_007DE459;
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_007DE452;
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_007DE452;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)))) & (2)) == 0) goto loc_007DE178;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 104)) != 0) goto loc_007DE189;
loc_007DE178:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32) + 160)))) & (2)) == 0) goto loc_007DE193;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32) + 104)) == 0) goto loc_007DE193;
loc_007DE189:
    goto loc_007DE468;
loc_007DE193:
    result = CmpCreateTemporaryHive(v_stack_m88, v_stack_m98, a3, a4);
    if (result != 0) goto loc_007DE1B2;
    goto loc_007DE468;
loc_007DE1B2:
    a3 = 0;
    result = CmpBlockTwoHiveWrites(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a3, a4);
    if (sign_flag) goto loc_007DE468;
    result = CmLockHiveSecurityShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a3, a4);
    v_stack_mF8 = 3;
    result = CmpDoAccessCheckOnSubtree(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8))), v_stack_mD8, (unsigned int)(0x20019ULL));
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8))), v_stack_mD8, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_007DE427;
    result = CmLockHiveSecurityShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8))), v_stack_mD8, (unsigned int)(0x20019ULL));
    v_stack_mF8 = 3;
    result = CmpDoAccessCheckOnSubtree(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)(v_stack_mD0), v_stack_mD8, (unsigned int)(0x20019ULL));
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)(v_stack_mD0), v_stack_mD8, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_007DE427;
    result = HvLockHiveFlusherExclusive(result, (unsigned int)(v_stack_mD0), v_stack_mD8, (unsigned int)(0x20019ULL));
    a4 = (unsigned int)(((unsigned int)(0x20019ULL)) | (0xFFFFFFFFULL));
    v_stack_mE0 = v_stack_mD4;
    result = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = 6;
    result = CmpCopyKeyPartial(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8))), result, a4);
    a1 = 0;
    if (sign_flag) goto loc_007DE427;
    v_stack_mF0 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 64) + 36) = (unsigned int)((unsigned int)(v_stack_mD4));
    v_stack_mF8 = 2;
    result = CmpCopySyncTree(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_mB8), result, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
    if (sign_flag) goto loc_007DE427;
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_mB8), result, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DE2DD;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)(v_stack_mD0), v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
    goto loc_007DE2E2;
loc_007DE2DD:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)(v_stack_mD0), v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
loc_007DE2E2:
    if (result != 0) goto loc_007DE2F4;
    goto loc_007DE427;
loc_007DE2F4:
    if (((*(unsigned __int8 *)(result + 140)) & (1)) == 0) goto loc_007DE30E;
    result = HvpGetCellFlat(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
    goto loc_007DE313;
loc_007DE30E:
    result = HvpGetCellPaged(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
loc_007DE313:
    if (result != 0) goto loc_007DE341;
loc_007DE320:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DE401;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), v_stack_mC8, v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))));
    goto loc_007DE406;
loc_007DE341:
    v_stack_mF0 = result;
    v_stack_mF8 = (unsigned int)((unsigned int)(v_stack_mD4));
    result = CmpMergeKeyValues(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), v_stack_mC8, (unsigned int)(0xC000009AULL), result);
    if (sign_flag) goto loc_007DE320;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DE378;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), v_stack_mC8, (unsigned int)(0xC000009AULL), result);
    goto loc_007DE37D;
loc_007DE378:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), v_stack_mC8, (unsigned int)(0xC000009AULL), result);
loc_007DE37D:
    if (((*(unsigned __int8 *)(result + 140)) & (1)) == 0) goto loc_007DE394;
    result = HvpReleaseCellFlat(result, v_stack_mC0, (unsigned int)(0xC000009AULL), result);
    goto loc_007DE399;
loc_007DE394:
    result = HvpReleaseCellPaged(result, v_stack_mC0, (unsigned int)(0xC000009AULL), result);
loc_007DE399:
    v_stack_mF0 = 2;
    v_stack_mF8 = 2;
    result = CmpCopySyncTree(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)(v_stack_mD0), result, (unsigned int)(v_stack_mD4));
    v_r12 = 0;
    if (sign_flag) goto loc_007DE427;
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), (unsigned int)(v_stack_mD0), result, (unsigned int)(v_stack_mD4));
    result = HvUnlockHiveFlusherExclusive(result, (unsigned int)(v_stack_mD0), result, (unsigned int)(v_stack_mD4));
    result = CmpUnlockTwoKcbs(v_stack_mA8, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    result = CmpUnlockRegistry(v_stack_mA8, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    *(unsigned __int64 *)(result + 1560) = v_stack_mA0;
    result = HvWriteExternal(result, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    *(unsigned __int64 *)(result + 1560) = 0;
    goto loc_007DE47F;
loc_007DE401:
    result = HvpReleaseCellPaged(result, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
loc_007DE406:
    if (0 == 0) goto loc_007DE427;
    if (((*(unsigned __int8 *)(result + 140)) & (1)) == 0) goto loc_007DE422;
    result = HvpReleaseCellFlat(result, v_stack_mC0, result, (unsigned int)(v_stack_mD4));
    goto loc_007DE427;
loc_007DE422:
    result = HvpReleaseCellPaged(result, v_stack_mC0, result, (unsigned int)(v_stack_mD4));
loc_007DE427:
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 32), v_stack_mC0, result, (unsigned int)(v_stack_mD4));
    if (((5) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        result = HvUnlockHiveFlusherExclusive(a1, v_stack_mC0, result, (unsigned int)(v_stack_mD4));
    }
    if (((5) & (1)) != 0) {
        a1 = result;
        result = HvUnlockHiveFlusherExclusive(a1, v_stack_mC0, result, (unsigned int)(v_stack_mD4));
    }
    if (1 == 0) goto loc_007DE47F;
    goto loc_007DE468;
loc_007DE452:
    goto loc_007DE468;
loc_007DE459:
    result = CmpLogUnsupportedOperation(19, v_stack_mC0, result, (unsigned int)(v_stack_mD4));
loc_007DE468:
    result = CmpUnlockTwoKcbs(v_stack_mA8, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    result = CmpUnlockRegistry(v_stack_mA8, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    if (result == 0) goto loc_007DE4F7;
loc_007DE47F:
    result = CmpDestroyHive(result, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    goto loc_007DE4F7;
loc_007DE489:
    if ((*(unsigned int *)(v_rip + 6470340)) <= 5) goto loc_007DE4F2;
    result = tlgKeywordOn(v_rip + 6470321, v_stack_mB0, result, (unsigned int)(v_stack_mD4));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_mA0;
        v_stack_mA0 = 0x1000000ULL;
        v_stack_m58 = result;
        a2 = v_rip - 7898441;
        result = v_stack_m78;
        v_stack_m50 = 8;
        v_stack_mF0 = result;
        a1 = v_rip + 6470265;
        a4 = 0;
        v_stack_mF8 = 3;
        a3 = 0;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
loc_007DE4F7:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSaveMergedKeys(void *Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x62C6DD)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mD8 = Arg4;
    Arg1 = 0;
    v_stack_mA0 = Arg3;
    v_stack_mD4 = 0;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_mBC = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mA8 = *(uint64_t *)(arg1 + 0x8);
    v_stack_m98 = v_xmm1;
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)));
    v_stack_mC4 = 0;
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x28)));
    v_stack_mC0 = (uint32_t)(Arg2);
    v_stack_mC8 = (uint32_t)(Arg2);
    v_stack_mB0 = *(uint64_t *)(arg2 + 0x8);
    result = CmpUuidCreate(v_stack_m88, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_007DE4F7;
    result = CmpUuidCreate(v_stack_m98, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_007DE4F7;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20)) == (*(uint64_t *)(v_rip + 0x7FB9A1))) goto loc_007DE489;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20)) == (*(uint64_t *)(v_rip + 0x7FB9A1))) goto loc_007DE489;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20))) goto loc_007DE110;
    goto loc_007DE4F7;
loc_007DE110:
    result = CmpLockRegistry(v_stack_m98, Arg2, Arg3, Arg4);
    result = CmpLockTwoKcbsShared(v_stack_mA8, *(uint64_t *)(arg2 + 0x8), Arg3, Arg4);
    result = 0;
    if ((*(uint16_t *)(v_stack_mA8 + 0x42)) != 0) goto loc_007DE459;
    local_rbx = 0;
    if ((*(uint16_t *)(v_stack_mB0 + 0x42)) != 0) goto loc_007DE459;
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_007DE452;
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_007DE452;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)))) & (2)) == 0) goto loc_007DE178;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x68)) != 0) goto loc_007DE189;
loc_007DE178:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20) + 0xA0)))) & (2)) == 0) goto loc_007DE193;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20) + 0x68)) == 0) goto loc_007DE193;
loc_007DE189:
    goto loc_007DE468;
loc_007DE193:
    result = CmpCreateTemporaryHive(v_stack_m88, v_stack_m98, Arg3, Arg4);
    if (result != 0) goto loc_007DE1B2;
    goto loc_007DE468;
loc_007DE1B2:
    Arg3 = 0;
    result = CmpBlockTwoHiveWrites(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg3, Arg4);
    if (sign_flag) goto loc_007DE468;
    result = CmLockHiveSecurityShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg3, Arg4);
    v_stack_mF8 = 3;
    result = CmpDoAccessCheckOnSubtree(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8))), v_stack_mD8, (uint32_t)(0x20019ULL));
    result = CmUnlockHiveSecurity(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8))), v_stack_mD8, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_007DE427;
    result = CmLockHiveSecurityShared(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8))), v_stack_mD8, (uint32_t)(0x20019ULL));
    v_stack_mF8 = 3;
    result = CmpDoAccessCheckOnSubtree(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)(v_stack_mD0), v_stack_mD8, (uint32_t)(0x20019ULL));
    result = CmUnlockHiveSecurity(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)(v_stack_mD0), v_stack_mD8, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_007DE427;
    result = HvLockHiveFlusherExclusive(result, (uint32_t)(v_stack_mD0), v_stack_mD8, (uint32_t)(0x20019ULL));
    Arg4 = (uint32_t)(((uint32_t)(0x20019ULL)) | (0xFFFFFFFFULL));
    v_stack_mE0 = v_stack_mD4;
    result = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = 6;
    result = CmpCopyKeyPartial(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8))), result, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_007DE427;
    v_stack_mF0 = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x24) = (uint32_t)((uint32_t)(v_stack_mD4));
    v_stack_mF8 = 2;
    result = CmpCopySyncTree(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(v_stack_mB8), result, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
    if (sign_flag) goto loc_007DE427;
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(v_stack_mB8), result, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DE2DD;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)(v_stack_mD0), v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
    goto loc_007DE2E2;
loc_007DE2DD:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)(v_stack_mD0), v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
loc_007DE2E2:
    if (result != 0) goto loc_007DE2F4;
    goto loc_007DE427;
loc_007DE2F4:
    if (((*(uint8_t *)(result + 0x8C)) & (1)) == 0) goto loc_007DE30E;
    result = HvpGetCellFlat(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
    goto loc_007DE313;
loc_007DE30E:
    result = HvpGetCellPaged(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
loc_007DE313:
    if (result != 0) goto loc_007DE341;
loc_007DE320:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DE401;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), v_stack_mC8, v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))));
    goto loc_007DE406;
loc_007DE341:
    v_stack_mF0 = result;
    v_stack_mF8 = (uint32_t)((uint32_t)(v_stack_mD4));
    result = CmpMergeKeyValues(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), v_stack_mC8, (uint32_t)(0xC000009AULL), result);
    if (sign_flag) goto loc_007DE320;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DE378;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), v_stack_mC8, (uint32_t)(0xC000009AULL), result);
    goto loc_007DE37D;
loc_007DE378:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), v_stack_mC8, (uint32_t)(0xC000009AULL), result);
loc_007DE37D:
    if (((*(uint8_t *)(result + 0x8C)) & (1)) == 0) goto loc_007DE394;
    result = HvpReleaseCellFlat(result, v_stack_mC0, (uint32_t)(0xC000009AULL), result);
    goto loc_007DE399;
loc_007DE394:
    result = HvpReleaseCellPaged(result, v_stack_mC0, (uint32_t)(0xC000009AULL), result);
loc_007DE399:
    v_stack_mF0 = 2;
    v_stack_mF8 = 2;
    result = CmpCopySyncTree(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)(v_stack_mD0), result, (uint32_t)(v_stack_mD4));
    local_r12 = 0;
    if (sign_flag) goto loc_007DE427;
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), (uint32_t)(v_stack_mD0), result, (uint32_t)(v_stack_mD4));
    result = HvUnlockHiveFlusherExclusive(result, (uint32_t)(v_stack_mD0), result, (uint32_t)(v_stack_mD4));
    result = CmpUnlockTwoKcbs(v_stack_mA8, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    result = CmpUnlockRegistry(v_stack_mA8, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    *(uint64_t *)(result + 0x618) = v_stack_mA0;
    result = HvWriteExternal(result, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    *(uint64_t *)(result + 0x618) = 0;
    goto loc_007DE47F;
loc_007DE401:
    result = HvpReleaseCellPaged(result, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
loc_007DE406:
    if (0 == 0) goto loc_007DE427;
    if (((*(uint8_t *)(result + 0x8C)) & (1)) == 0) goto loc_007DE422;
    result = HvpReleaseCellFlat(result, v_stack_mC0, result, (uint32_t)(v_stack_mD4));
    goto loc_007DE427;
loc_007DE422:
    result = HvpReleaseCellPaged(result, v_stack_mC0, result, (uint32_t)(v_stack_mD4));
loc_007DE427:
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x20), v_stack_mC0, result, (uint32_t)(v_stack_mD4));
    if (((5) & (2)) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
        result = HvUnlockHiveFlusherExclusive(Arg1, v_stack_mC0, result, (uint32_t)(v_stack_mD4));
    }
    if (((5) & (1)) != 0) {
        Arg1 = result;
        result = HvUnlockHiveFlusherExclusive(Arg1, v_stack_mC0, result, (uint32_t)(v_stack_mD4));
    }
    if (1 == 0) goto loc_007DE47F;
    goto loc_007DE468;
loc_007DE452:
    goto loc_007DE468;
loc_007DE459:
    result = CmpLogUnsupportedOperation(19, v_stack_mC0, result, (uint32_t)(v_stack_mD4));
loc_007DE468:
    result = CmpUnlockTwoKcbs(v_stack_mA8, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    result = CmpUnlockRegistry(v_stack_mA8, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    if (result == 0) goto loc_007DE4F7;
loc_007DE47F:
    result = CmpDestroyHive(result, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    goto loc_007DE4F7;
loc_007DE489:
    if ((*(uint32_t *)(v_rip + 0x62BAC4)) <= 5) goto loc_007DE4F2;
    result = tlgKeywordOn(v_rip + 6470321, v_stack_mB0, result, (uint32_t)(v_stack_mD4));
    if ((uint8_t)(result) != 0) {
        result = v_stack_mA0;
        v_stack_mA0 = 0x1000000ULL;
        v_stack_m58 = result;
        Arg2 = v_rip - 7898441;
        result = v_stack_m78;
        v_stack_m50 = 8;
        v_stack_mF0 = result;
        Arg1 = v_rip + 6470265;
        Arg4 = 0;
        v_stack_mF8 = 3;
        Arg3 = 0;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
loc_007DE4F7:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (224);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007DE040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
