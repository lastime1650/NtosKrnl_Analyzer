# MiReferenceIoPages

- RVA: `0x0023C804`–`0x0023D105` (길이 `2,305` bytes)
- VA: `0x000000014023C804`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00061000`
- 디코드: `550`개 명령, `2,305/2,305` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0023C867` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0023C920` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x0023C939` → [MiLockIoPfnTree](../2A/MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x0023C9F8` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x0023CA1F` → [MiLockIoPfnTree](../2A/MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x0023CA9A` → [MiUnlockIoPfnTree](../2A/MiUnlockIoPfnTree_function_002AC7F8.md) (function, `0x002AC7F8`)
- `0x0023CABE` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0023CB13` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0023CB5A` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0023CBBD` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x0023CBE7` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x0023CBF1` → [MiLockIoPfnTree](../2A/MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x0023CD69` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x0023CD85` → [ExAllocatePoolMm](../35/ExAllocatePoolMm_function_0035B690.md) (function, `0x0035B690`)
- `0x0023CDA7` → [MiDereferenceIoPages](../2A/MiDereferenceIoPages_function_002AB1B0.md) (function, `0x002AB1B0`)
- `0x0023CDC3` → [MiIsPageInIoHugeRangeTransition](../2A/MiIsPageInIoHugeRangeTransition_function_002AB7A0.md) (function, `0x002AB7A0`)
- `0x0023CDE1` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0023CE41` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0023CE87` → [MiFlushEntireTbDueToAttributeChange](../30/MiFlushEntireTbDueToAttributeChange_function_00308AE0.md) (function, `0x00308AE0`)
- `0x0023CF01` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0023CF28` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0023CF4A` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x0023CF72` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0023CF83` → [MiInitializeIoPageNodeArray](../49/MiInitializeIoPageNodeArray_function_00495B10.md) (function, `0x00495B10`)
- `0x0023CFB1` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0023CFE4` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x0023D03C` → [MiFlushCachedIoPfnRange](../67/MiFlushCachedIoPfnRange_function_0067BC24.md) (function, `0x0067BC24`)
- `0x0023D05A` → [MiFlushCachedIoPfnRange](../67/MiFlushCachedIoPfnRange_function_0067BC24.md) (function, `0x0067BC24`)
- `0x0023D06E` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x0023D0A1` → [MiFlushCachedIoPfnRange](../67/MiFlushCachedIoPfnRange_function_0067BC24.md) (function, `0x0067BC24`)
- `0x0023D0EC` → [MiDereferenceIoPages](../2A/MiDereferenceIoPages_function_002AB1B0.md) (function, `0x002AB1B0`)
- `0x0023D0FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiProbeLockFrame](MiProbeLockFrame_function_0023C1B0.md) at `0x0023C1FA`
- [MiFillSystemPtes](../31/MiFillSystemPtes_function_00319850.md) at `0x00319EB5`
- [MiMapContiguousMemoryLarge](../3B/MiMapContiguousMemoryLarge_function_003B44CC.md) at `0x003B46E0`
- [MiMapMdlCommon](../67/MiMapMdlCommon_function_00674524.md) at `0x006747C7`
- [MiMapViewOfPhysicalSection](../../page/97/MiMapViewOfPhysicalSection_function_0097F984.md) at `0x0097FD14`
- [MiMapLockedPagesInUserSpace](../../page/97/MiMapLockedPagesInUserSpace_function_0097FE04.md) at `0x00980067`
- [MiRotateToFrameBuffer](../../page/A3/MiRotateToFrameBuffer_function_00A38214.md) at `0x00A382C7`
- [MiRotateToFrameBufferNoCopy](../../page/A3/MiRotateToFrameBufferNoCopy_function_00A38530.md) at `0x00A385EC`
- [MiAddLoaderHalIoPte](../../init/C5/MiAddLoaderHalIoPte_function_00C5E610.md) at `0x00C5E6AC`

### Static image references
- `0x0023C820` → RVA `0x00E0A740` (`.data`; read)
- `0x0023C88F` → RVA `0x00E2DC38` (`.data`; read)
- `0x0023C8B3` → RVA `0x00E37280` (`.data`; read)
- `0x0023C8EF` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0023C973` → RVA `0x00E37308` (`.data`; read)
- `0x0023CA82` → RVA `0x00E37348` (`.data`; read/write)
- `0x0023D00F` → RVA `0x00E3733C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0023D0FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **18**
  - `0x0023CCE9` → [sub_006D79AA + 0xD](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CCFB` → [sub_006D79AA + 0xD](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CDFF` → [sub_006D79AA + 0xB9](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CE11` → [sub_006D79AA + 0xB9](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CF1B` → [sub_006D79AA](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CF2E` → [sub_006D79AA](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CF65` → [sub_006D79AA + 0x2F](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CF78` → [sub_006D79AA + 0x2F](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CF8C` → [sub_006D79AA + 0x3F](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CFA6` → [sub_006D79AA + 0x3C](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CFB7` → [sub_006D79AA + 0x3C](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CFC9` → [sub_006D79AA + 0x52](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023CFCF` → [sub_006D79AA + 0x66](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023D01D` → [sub_006D79AA + 0xE1](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023D028` → [sub_006D79AA + 0xF3](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023D044` → [sub_006D79AA + 0xE1](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023D08E` → [sub_006D79AA + 0x139](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)
  - `0x0023D0C6` → [sub_006D79AA + 0x139](../6D/Unknown_function_006D79AA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0023C804  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0023C809  55                              push rbp
0023C80A  56                              push rsi
0023C80B  57                              push rdi
0023C80C  41 54                           push r12
0023C80E  41 55                           push r13
0023C810  41 56                           push r14
0023C812  41 57                           push r15
0023C814  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
0023C819  48 81 EC 70 01 00 00            sub rsp, 0x170
0023C820  48 8B 05 19 DF BC 00            mov rax, qword ptr [rip + 0xbcdf19]
0023C827  48 33 C4                        xor rax, rsp
0023C82A  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0023C82E  4C 8B A5 D0 00 00 00            mov r12, qword ptr [rbp + 0xd0]
0023C835  4D 8B F0                        mov r14, r8
0023C838  48 8B BD D8 00 00 00            mov rdi, qword ptr [rbp + 0xd8]
0023C83F  48 8B DA                        mov rbx, rdx
0023C842  48 63 F1                        movsxd rsi, ecx
0023C845  33 D2                           xor edx, edx
0023C847  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0023C84C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0023C850  41 B8 B0 00 00 00               mov r8d, 0xb0
0023C856  89 74 24 2C                     mov dword ptr [rsp + 0x2c], esi
0023C85A  4C 89 65 98                     mov qword ptr [rbp - 0x68], r12
0023C85E  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
0023C862  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
0023C867  E8 D4 A3 48 00                  call 0x1406c6c40
0023C86C  33 C0                           xor eax, eax
0023C86E  45 33 D2                        xor r10d, r10d
0023C871  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0023C876  0F 57 C0                        xorps xmm0, xmm0
0023C879  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0023C87E  4D 85 E4                        test r12, r12
0023C881  0F 85 84 06 00 00               jne 0x14023cf0b
0023C887  48 85 FF                        test rdi, rdi
0023C88A  74 03                           je 0x14023c88f
0023C88C  4C 89 17                        mov qword ptr [rdi], r10
0023C88F  8A 0D A3 13 BF 00               mov cl, byte ptr [rip + 0xbf13a3]
0023C895  BF 01 00 00 00                  mov edi, 1
0023C89A  48 83 4D 80 FF                  or qword ptr [rbp - 0x80], 0xffffffffffffffff
0023C89F  80 C1 F4                        add cl, 0xf4
0023C8A2  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0023C8A7  4D 8B FA                        mov r15, r10
0023C8AA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0023C8AE  8B C7                           mov eax, edi
0023C8B0  48 D3 E0                        shl rax, cl
0023C8B3  48 8D 0D C6 A9 BF 00            lea rcx, [rip + 0xbfa9c6]
0023C8BA  48 2B C7                        sub rax, rdi
0023C8BD  44 89 54 24 3C                  mov dword ptr [rsp + 0x3c], r10d
0023C8C2  48 23 D8                        and rbx, rax
0023C8C5  4C 89 55 90                     mov qword ptr [rbp - 0x70], r10
0023C8C9  48 8B C6                        mov rax, rsi
0023C8CC  C7 44 24 64 03 00 00 00         mov dword ptr [rsp + 0x64], 3
0023C8D4  48 C1 E0 06                     shl rax, 6
0023C8D8  48 03 C1                        add rax, rcx
0023C8DB  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0023C8E0  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0023C8E4  44 0F 20 C6                     mov rsi, cr8
0023C8E8  8D 4F 01                        lea ecx, [rdi + 1]
0023C8EB  44 0F 22 C1                     mov cr8, rcx
0023C8EF  44 39 15 2A A4 D8 00            cmp dword ptr [rip + 0xd8a42a], r10d
0023C8F6  0F 85 E0 04 00 00               jne 0x14023cddc
0023C8FC  40 3A F1                        cmp sil, cl
0023C8FF  44 0F B6 EE                     movzx r13d, sil
0023C903  41 BB 11 00 00 00               mov r11d, 0x11
0023C909  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0023C90E  48 8B D3                        mov rdx, rbx
0023C911  45 0F 44 EB                     cmove r13d, r11d
0023C915  41 8D 43 F4                     lea eax, [r11 - 0xc]
0023C919  0F 45 C7                        cmovne eax, edi
0023C91C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0023C920  E8 03 FE 06 00                  call 0x1402ac728
0023C925  83 7C 24 5C 03                  cmp dword ptr [rsp + 0x5c], 3
0023C92A  8B 74 24 2C                     mov esi, dword ptr [rsp + 0x2c]
0023C92E  0F 85 F5 03 00 00               jne 0x14023cd29
0023C934  B9 05 00 00 00                  mov ecx, 5
0023C939  E8 66 FF 06 00                  call 0x1402ac8a4
0023C93E  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0023C943  4D 8B C6                        mov r8, r14
0023C946  45 33 F6                        xor r14d, r14d
0023C949  41 8B D1                        mov edx, r9d
0023C94C  4D 85 C0                        test r8, r8
0023C94F  0F 84 6D 07 00 00               je 0x14023d0c2
0023C955  48 3B 5C 24 48                  cmp rbx, qword ptr [rsp + 0x48]
0023C95A  0F 82 E2 05 00 00               jb 0x14023cf42
0023C960  48 3B 5C 24 50                  cmp rbx, qword ptr [rsp + 0x50]
0023C965  0F 87 D7 05 00 00               ja 0x14023cf42
0023C96B  3B F7                           cmp esi, edi
0023C96D  0F 84 68 03 00 00               je 0x14023ccdb
0023C973  48 8B 05 8E A9 BF 00            mov rax, qword ptr [rip + 0xbfa98e]
0023C97A  48 8D 4B FF                     lea rcx, [rbx - 1]
0023C97E  49 03 C8                        add rcx, r8
0023C981  48 85 C0                        test rax, rax
0023C984  74 1B                           je 0x14023c9a1
0023C986  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
0023C98A  0F 83 C5 00 00 00               jae 0x14023ca55
0023C990  48 8B 00                        mov rax, qword ptr [rax]
0023C993  48 85 C0                        test rax, rax
0023C996  75 EE                           jne 0x14023c986
0023C998  48 85 C0                        test rax, rax
0023C99B  0F 85 DF 06 00 00               jne 0x14023d080
0023C9A1  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0023C9A5  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0023C9AA  48 8B 30                        mov rsi, qword ptr [rax]
0023C9AD  48 85 F6                        test rsi, rsi
0023C9B0  74 28                           je 0x14023c9da
0023C9B2  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0023C9B6  48 3B D8                        cmp rbx, rax
0023C9B9  0F 82 5C 03 00 00               jb 0x14023cd1b
0023C9BF  48 05 00 02 00 00               add rax, 0x200
0023C9C5  48 3B D8                        cmp rbx, rax
0023C9C8  0F 82 11 01 00 00               jb 0x14023cadf
0023C9CE  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0023C9D2  48 8B F0                        mov rsi, rax
0023C9D5  48 85 C0                        test rax, rax
0023C9D8  75 D8                           jne 0x14023c9b2
0023C9DA  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0023C9E3  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
0023C9EA  48 8B 89 48 01 00 00            mov rcx, qword ptr [rcx + 0x148]
0023C9F1  48 81 C1 80 02 00 00            add rcx, 0x280
0023C9F8  E8 93 DB 00 00                  call 0x14024a590
0023C9FD  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0023CA01  48 85 C0                        test rax, rax
0023CA04  0F 84 52 03 00 00               je 0x14023cd5c
0023CA0A  4C 8B F0                        mov r14, rax
0023CA0D  48 8B C3                        mov rax, rbx
0023CA10  B9 06 00 00 00                  mov ecx, 6
0023CA15  48 25 00 FE FF FF               and rax, 0xfffffffffffffe00
0023CA1B  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0023CA1F  E8 80 FE 06 00                  call 0x1402ac8a4
0023CA24  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
0023CA29  45 33 C9                        xor r9d, r9d
0023CA2C  48 8B 05 D5 A8 BF 00            mov rax, qword ptr [rip + 0xbfa8d5]
0023CA33  48 8D 4E FF                     lea rcx, [rsi - 1]
0023CA37  48 03 CB                        add rcx, rbx
0023CA3A  48 85 C0                        test rax, rax
0023CA3D  0F 84 79 05 00 00               je 0x14023cfbc
0023CA43  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
0023CA47  72 1F                           jb 0x14023ca68
0023CA49  48 3B 58 20                     cmp rbx, qword ptr [rax + 0x20]
0023CA4D  76 21                           jbe 0x14023ca70
0023CA4F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0023CA53  EB 16                           jmp 0x14023ca6b
0023CA55  48 3B 58 20                     cmp rbx, qword ptr [rax + 0x20]
0023CA59  0F 86 39 FF FF FF               jbe 0x14023c998
0023CA5F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0023CA63  E9 2B FF FF FF                  jmp 0x14023c993
0023CA68  48 8B 00                        mov rax, qword ptr [rax]
0023CA6B  48 85 C0                        test rax, rax
0023CA6E  75 D3                           jne 0x14023ca43
0023CA70  48 85 C0                        test rax, rax
0023CA73  0F 84 43 05 00 00               je 0x14023cfbc
0023CA79  8B 54 24 28                     mov edx, dword ptr [rsp + 0x28]
0023CA7D  BB 18 00 00 C0                  mov ebx, 0xc0000018
0023CA82  01 3D C0 A8 BF 00               add dword ptr [rip + 0xbfa8c0], edi
0023CA88  83 E2 FE                        and edx, 0xfffffffe
0023CA8B  83 CA 02                        or edx, 2
0023CA8E  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0023CA93  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
0023CA97  41 8A CD                        mov cl, r13b
0023CA9A  E8 59 FD 06 00                  call 0x1402ac7f8
0023CA9F  48 85 F6                        test rsi, rsi
0023CAA2  0F 85 23 06 00 00               jne 0x14023d0cb
0023CAA8  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0023CAAC  48 85 C0                        test rax, rax
0023CAAF  0F 85 41 06 00 00               jne 0x14023d0f6
0023CAB5  8B C3                           mov eax, ebx
0023CAB7  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0023CABB  48 33 CC                        xor rcx, rsp
0023CABE  E8 7D FB 46 00                  call 0x1406ac640
0023CAC3  48 8B 9C 24 C8 01 00 00         mov rbx, qword ptr [rsp + 0x1c8]
0023CACB  48 81 C4 70 01 00 00            add rsp, 0x170
0023CAD2  41 5F                           pop r15
0023CAD4  41 5E                           pop r14
0023CAD6  41 5D                           pop r13
0023CAD8  41 5C                           pop r12
0023CADA  5F                              pop rdi
0023CADB  5E                              pop rsi
0023CADC  5D                              pop rbp
0023CADD  C3                              ret
0023CADE  CC                              int3
0023CADF  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0023CAE3  4C 8B F3                        mov r14, rbx
0023CAE6  4C 2B F0                        sub r14, rax
0023CAE9  33 D2                           xor edx, edx
0023CAEB  48 8D 88 00 02 00 00            lea rcx, [rax + 0x200]
0023CAF2  48 85 C9                        test rcx, rcx
0023CAF5  0F 85 05 02 00 00               jne 0x14023cd00
0023CAFB  4B 8D 04 30                     lea rax, [r8 + r14]
0023CAFF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0023CB04  48 8D 8E AC 00 00 00            lea rcx, [rsi + 0xac]
0023CB0B  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
0023CB0F  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
0023CB13  E8 68 C3 00 00                  call 0x140248e80
0023CB18  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
0023CB1D  45 33 DB                        xor r11d, r11d
0023CB20  45 85 C0                        test r8d, r8d
0023CB23  0F 85 AB 04 00 00               jne 0x14023cfd4
0023CB29  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0023CB2E  4C 3B F2                        cmp r14, rdx
0023CB31  0F 82 CE 00 00 00               jb 0x14023cc05
0023CB37  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0023CB3C  45 33 F6                        xor r14d, r14d
0023CB3F  48 85 C0                        test rax, rax
0023CB42  0F 85 01 05 00 00               jne 0x14023d049
0023CB48  44 38 74 24 38                  cmp byte ptr [rsp + 0x38], r14b
0023CB4D  0F 85 63 02 00 00               jne 0x14023cdb6
0023CB53  48 8D 8E AC 00 00 00            lea rcx, [rsi + 0xac]
0023CB5A  E8 81 CC 00 00                  call 0x1402497e0
0023CB5F  4C 8B 44 24 20                  mov r8, qword ptr [rsp + 0x20]
0023CB64  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0023CB69  41 8B D1                        mov edx, r9d
0023CB6C  4D 85 C0                        test r8, r8
0023CB6F  0F 84 42 05 00 00               je 0x14023d0b7
0023CB75  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0023CB7E  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
0023CB85  48 8B 81 48 01 00 00            mov rax, qword ptr [rcx + 0x148]
0023CB8C  8B 88 80 02 00 00               mov ecx, dword ptr [rax + 0x280]
0023CB92  0F BA E1 1E                     bt ecx, 0x1e
0023CB96  0F 83 4D 03 00 00               jae 0x14023cee9
0023CB9C  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0023CBA5  41 8A D5                        mov dl, r13b
0023CBA8  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
0023CBAF  48 8B 89 48 01 00 00            mov rcx, qword ptr [rcx + 0x148]
0023CBB6  48 81 C1 80 02 00 00            add rcx, 0x280
0023CBBD  E8 2E C0 10 00                  call 0x140348bf0
0023CBC2  44 0F 20 C6                     mov rsi, cr8
0023CBC6  B8 02 00 00 00                  mov eax, 2
0023CBCB  44 0F 22 C0                     mov cr8, rax
0023CBCF  44 39 35 4A A1 D8 00            cmp dword ptr [rip + 0xd8a14a], r14d
0023CBD6  0F 85 20 03 00 00               jne 0x14023cefc
0023CBDC  48 8B D3                        mov rdx, rbx
0023CBDF  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0023CBE4  44 8A EE                        mov r13b, sil
0023CBE7  E8 3C FB 06 00                  call 0x1402ac728
0023CBEC  B9 05 00 00 00                  mov ecx, 5
0023CBF1  E8 AE FC 06 00                  call 0x1402ac8a4
0023CBF6  4C 8B 44 24 20                  mov r8, qword ptr [rsp + 0x20]
0023CBFB  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0023CC00  E9 EE 02 00 00                  jmp 0x14023cef3
0023CC05  48 3B 5C 24 48                  cmp rbx, qword ptr [rsp + 0x48]
0023CC0A  0F 82 CC 03 00 00               jb 0x14023cfdc
0023CC10  48 3B 5C 24 50                  cmp rbx, qword ptr [rsp + 0x50]
0023CC15  0F 87 C1 03 00 00               ja 0x14023cfdc
0023CC1B  83 7C 24 5C 03                  cmp dword ptr [rsp + 0x5c], 3
0023CC20  0F 85 CC 01 00 00               jne 0x14023cdf2
0023CC26  8A 0D 0C 10 BF 00               mov cl, byte ptr [rip + 0xbf100c]
0023CC2C  48 8B C7                        mov rax, rdi
0023CC2F  42 0F B7 94 76 B0 00 00 00      movzx edx, word ptr [rsi + r14*2 + 0xb0]
0023CC38  80 C1 F4                        add cl, 0xf4
0023CC3B  48 D3 E0                        shl rax, cl
0023CC3E  48 2B C7                        sub rax, rdi
0023CC41  48 23 C3                        and rax, rbx
0023CC44  48 2B 46 18                     sub rax, qword ptr [rsi + 0x18]
0023CC48  8D 0C 00                        lea ecx, [rax + rax]
0023CC4B  8B C1                           mov eax, ecx
0023CC4D  83 E1 1F                        and ecx, 0x1f
0023CC50  48 C1 E8 05                     shr rax, 5
0023CC54  44 8B 64 86 2C                  mov r12d, dword ptr [rsi + rax*4 + 0x2c]
0023CC59  B8 FF FF 00 00                  mov eax, 0xffff
0023CC5E  41 D3 EC                        shr r12d, cl
0023CC61  41 83 E4 03                     and r12d, 3
0023CC65  66 3B D0                        cmp dx, ax
0023CC68  0F 84 BE 01 00 00               je 0x14023ce2c
0023CC6E  66 85 D2                        test dx, dx
0023CC71  75 1E                           jne 0x14023cc91
0023CC73  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0023CC76  85 C0                           test eax, eax
0023CC78  0F 84 98 01 00 00               je 0x14023ce16
0023CC7E  44 8B 54 24 30                  mov r10d, dword ptr [rsp + 0x30]
0023CC83  FF C0                           inc eax
0023CC85  89 46 20                        mov dword ptr [rsi + 0x20], eax
0023CC88  45 3B E2                        cmp r12d, r10d
0023CC8B  0F 85 E0 01 00 00               jne 0x14023ce71
0023CC91  4C 39 5D 98                     cmp qword ptr [rbp - 0x68], r11
0023CC95  0F 84 CD 01 00 00               je 0x14023ce68
0023CC9B  41 8B CC                        mov ecx, r12d
0023CC9E  8B C7                           mov eax, edi
0023CCA0  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
0023CCA4  D3 E0                           shl eax, cl
0023CCA6  41 09 04 24                     or dword ptr [r12], eax
0023CCAA  66 42 01 BC 76 B0 00 00 00      add word ptr [rsi + r14*2 + 0xb0], di
0023CCB3  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0023CCB7  48 85 C0                        test rax, rax
0023CCBA  75 15                           jne 0x14023ccd1
0023CCBC  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
0023CCC1  4C 03 F7                        add r14, rdi
0023CCC4  48 03 DF                        add rbx, rdi
0023CCC7  48 29 7C 24 20                  sub qword ptr [rsp + 0x20], rdi
0023CCCC  E9 58 FE FF FF                  jmp 0x14023cb29
0023CCD1  4C 39 18                        cmp qword ptr [rax], r11
0023CCD4  75 E6                           jne 0x14023ccbc
0023CCD6  48 89 30                        mov qword ptr [rax], rsi
0023CCD9  EB E1                           jmp 0x14023ccbc
0023CCDB  83 7C 24 5C 03                  cmp dword ptr [rsp + 0x5c], 3
0023CCE0  0F 84 8D FC FF FF               je 0x14023c973
0023CCE6  4D 85 E4                        test r12, r12
0023CCE9  0F 84 C8 AC 49 00               je 0x1406d79b7
0023CCEF  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0023CCF3  8B C7                           mov eax, edi
0023CCF5  D3 E0                           shl eax, cl
0023CCF7  41 09 04 24                     or dword ptr [r12], eax
0023CCFB  E9 B7 AC 49 00                  jmp 0x1406d79b7
0023CD00  49 8D 04 18                     lea rax, [r8 + rbx]
0023CD04  48 3B C1                        cmp rax, rcx
0023CD07  0F 86 EE FD FF FF               jbe 0x14023cafb
0023CD0D  48 C7 44 24 70 00 02 00 00      mov qword ptr [rsp + 0x70], 0x200
0023CD16  E9 E9 FD FF FF                  jmp 0x14023cb04
0023CD1B  48 8B 06                        mov rax, qword ptr [rsi]
0023CD1E  48 8B F0                        mov rsi, rax
0023CD21  48 85 C0                        test rax, rax
0023CD24  E9 87 FC FF FF                  jmp 0x14023c9b0
0023CD29  3B F7                           cmp esi, edi
0023CD2B  0F 85 03 FC FF FF               jne 0x14023c934
0023CD31  49 8D 46 FF                     lea rax, [r14 - 1]
0023CD35  48 03 C3                        add rax, rbx
0023CD38  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
0023CD3D  0F 87 F1 FB FF FF               ja 0x14023c934
0023CD43  45 3A EB                        cmp r13b, r11b
0023CD46  0F 85 C8 01 00 00               jne 0x14023cf14
0023CD4C  4D 85 E4                        test r12, r12
0023CD4F  0F 85 DE 01 00 00               jne 0x14023cf33
0023CD55  33 C0                           xor eax, eax
0023CD57  E9 5B FD FF FF                  jmp 0x14023cab7
0023CD5C  41 80 FD 11                     cmp r13b, 0x11
0023CD60  0F 85 F8 01 00 00               jne 0x14023cf5e
0023CD66  48 8B CB                        mov rcx, rbx
0023CD69  E8 62 BF 0F 00                  call 0x140338cd0
0023CD6E  0F BA E8 1F                     bts eax, 0x1f
0023CD72  BA B0 04 00 00                  mov edx, 0x4b0
0023CD77  44 8B C8                        mov r9d, eax
0023CD7A  B9 40 00 00 00                  mov ecx, 0x40
0023CD7F  41 B8 4D 69 49 6F               mov r8d, 0x6f49694d
0023CD85  E8 06 E9 11 00                  call 0x14035b690
0023CD8A  4C 8B F0                        mov r14, rax
0023CD8D  48 85 C0                        test rax, rax
0023CD90  0F 85 E7 01 00 00               jne 0x14023cf7d
0023CD96  48 2B 5C 24 40                  sub rbx, qword ptr [rsp + 0x40]
0023CD9B  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0023CDA0  4C 8B C3                        mov r8, rbx
0023CDA3  8B 4C 24 2C                     mov ecx, dword ptr [rsp + 0x2c]
0023CDA7  E8 04 E4 06 00                  call 0x1402ab1b0
0023CDAC  B8 9A 00 00 C0                  mov eax, 0xc000009a
0023CDB1  E9 01 FD FF FF                  jmp 0x14023cab7
0023CDB6  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0023CDBA  F0 49 FF 49 08                  lock dec qword ptr [r9 + 8]
0023CDBF  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0023CDC3  E8 D8 E9 06 00                  call 0x1402ab7a0
0023CDC8  85 C0                           test eax, eax
0023CDCA  0F 85 94 02 00 00               jne 0x14023d064
0023CDD0  41 8A C6                        mov al, r14b
0023CDD3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0023CDD7  E9 77 FD FF FF                  jmp 0x14023cb53
0023CDDC  8A D1                           mov dl, cl
0023CDDE  40 8A CE                        mov cl, sil
0023CDE1  E8 16 89 2B 00                  call 0x1404f56fc
0023CDE6  45 33 D2                        xor r10d, r10d
0023CDE9  41 8D 4A 02                     lea ecx, [r10 + 2]
0023CDED  E9 0A FB FF FF                  jmp 0x14023c8fc
0023CDF2  39 7C 24 2C                     cmp dword ptr [rsp + 0x2c], edi
0023CDF6  0F 85 2A FE FF FF               jne 0x14023cc26
0023CDFC  4D 85 E4                        test r12, r12
0023CDFF  0F 84 5E AC 49 00               je 0x1406d7a63
0023CE05  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0023CE09  8B C7                           mov eax, edi
0023CE0B  D3 E0                           shl eax, cl
0023CE0D  41 09 04 24                     or dword ptr [r12], eax
0023CE11  E9 4D AC 49 00                  jmp 0x1406d7a63
0023CE16  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
0023CE1A  45 85 C0                        test r8d, r8d
0023CE1D  0F B6 C9                        movzx ecx, cl
0023CE20  0F 44 CF                        cmove ecx, edi
0023CE23  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0023CE27  E9 52 FE FF FF                  jmp 0x14023cc7e
0023CE2C  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0023CE31  48 85 C0                        test rax, rax
0023CE34  0F 85 59 02 00 00               jne 0x14023d093
0023CE3A  48 8D 8E AC 00 00 00            lea rcx, [rsi + 0xac]
0023CE41  E8 9A C9 00 00                  call 0x1402497e0
0023CE46  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0023CE4B  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
0023CE4F  8B D0                           mov edx, eax
0023CE51  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
0023CE56  48 3B DF                        cmp rbx, rdi
0023CE59  0F 85 4C 02 00 00               jne 0x14023d0ab
0023CE5F  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
0023CE63  E9 2B FC FF FF                  jmp 0x14023ca93
0023CE68  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
0023CE6C  E9 39 FE FF FF                  jmp 0x14023ccaa
0023CE71  44 3B D7                        cmp r10d, edi
0023CE74  0F 84 7E 01 00 00               je 0x14023cff8
0023CE7A  41 83 FC 03                     cmp r12d, 3
0023CE7E  74 21                           je 0x14023cea1
0023CE80  44 39 5C 24 60                  cmp dword ptr [rsp + 0x60], r11d
0023CE85  75 11                           jne 0x14023ce98
0023CE87  E8 54 BC 0C 00                  call 0x140308ae0
0023CE8C  44 8B 54 24 30                  mov r10d, dword ptr [rsp + 0x30]
0023CE91  45 33 DB                        xor r11d, r11d
0023CE94  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
0023CE98  44 3B E7                        cmp r12d, edi
0023CE9B  0F 84 60 01 00 00               je 0x14023d001
0023CEA1  8A 0D 91 0D BF 00               mov cl, byte ptr [rip + 0xbf0d91]
0023CEA7  48 8B C7                        mov rax, rdi
0023CEAA  80 C1 F4                        add cl, 0xf4
0023CEAD  BA 03 00 00 00                  mov edx, 3
0023CEB2  48 D3 E0                        shl rax, cl
0023CEB5  45 8B E2                        mov r12d, r10d
0023CEB8  48 2B C7                        sub rax, rdi
0023CEBB  48 23 C3                        and rax, rbx
0023CEBE  48 2B 46 18                     sub rax, qword ptr [rsi + 0x18]
0023CEC2  8D 0C 00                        lea ecx, [rax + rax]
0023CEC5  8B C1                           mov eax, ecx
0023CEC7  83 E1 1F                        and ecx, 0x1f
0023CECA  C1 E8 05                        shr eax, 5
0023CECD  D3 E2                           shl edx, cl
0023CECF  44 8B C0                        mov r8d, eax
0023CED2  F7 D2                           not edx
0023CED4  23 54 86 2C                     and edx, dword ptr [rsi + rax*4 + 0x2c]
0023CED8  41 8B C2                        mov eax, r10d
0023CEDB  D3 E0                           shl eax, cl
0023CEDD  0B D0                           or edx, eax
0023CEDF  42 89 54 86 2C                  mov dword ptr [rsi + r8*4 + 0x2c], edx
0023CEE4  E9 A8 FD FF FF                  jmp 0x14023cc91
0023CEE9  41 80 FD 11                     cmp r13b, 0x11
0023CEED  0F 85 7B 01 00 00               jne 0x14023d06e
0023CEF3  8B 74 24 2C                     mov esi, dword ptr [rsp + 0x2c]
0023CEF7  E9 4D FA FF FF                  jmp 0x14023c949
0023CEFC  8A D0                           mov dl, al
0023CEFE  40 8A CE                        mov cl, sil
0023CF01  E8 F6 87 2B 00                  call 0x1404f56fc
0023CF06  E9 D1 FC FF FF                  jmp 0x14023cbdc
0023CF0B  45 89 14 24                     mov dword ptr [r12], r10d
0023CF0F  E9 73 F9 FF FF                  jmp 0x14023c887
0023CF14  44 39 15 05 9E D8 00            cmp dword ptr [rip + 0xd89e05], r10d
0023CF1B  0F 84 89 AA 49 00               je 0x1406d79aa
0023CF21  44 0F 20 C1                     mov rcx, cr8
0023CF25  41 8A D5                        mov dl, r13b
0023CF28  E8 6B 87 2B 00                  call 0x1404f5698
0023CF2D  90                              nop
0023CF2E  E9 77 AA 49 00                  jmp 0x1406d79aa
0023CF33  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0023CF37  D3 E7                           shl edi, cl
0023CF39  41 09 3C 24                     or dword ptr [r12], edi
0023CF3D  E9 13 FE FF FF                  jmp 0x14023cd55
0023CF42  48 8B D3                        mov rdx, rbx
0023CF45  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0023CF4A  E8 D9 F7 06 00                  call 0x1402ac728
0023CF4F  4C 8B 44 24 20                  mov r8, qword ptr [rsp + 0x20]
0023CF54  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0023CF59  E9 0D FA FF FF                  jmp 0x14023c96b
0023CF5E  44 39 35 BB 9D D8 00            cmp dword ptr [rip + 0xd89dbb], r14d
0023CF65  0F 84 6E AA 49 00               je 0x1406d79d9
0023CF6B  44 0F 20 C1                     mov rcx, cr8
0023CF6F  41 8A D5                        mov dl, r13b
0023CF72  E8 21 87 2B 00                  call 0x1404f5698
0023CF77  90                              nop
0023CF78  E9 5C AA 49 00                  jmp 0x1406d79d9
0023CF7D  48 8B C8                        mov rcx, rax
0023CF80  89 78 20                        mov dword ptr [rax + 0x20], edi
0023CF83  E8 88 8B 25 00                  call 0x140495b10
0023CF88  41 80 FD 11                     cmp r13b, 0x11
0023CF8C  0F 84 57 AA 49 00               je 0x1406d79e9
0023CF92  44 0F 20 C6                     mov rsi, cr8
0023CF96  B8 02 00 00 00                  mov eax, 2
0023CF9B  44 0F 22 C0                     mov cr8, rax
0023CF9F  83 3D 7A 9D D8 00 00            cmp dword ptr [rip + 0xd89d7a], 0
0023CFA6  0F 84 3A AA 49 00               je 0x1406d79e6
0023CFAC  8A D0                           mov dl, al
0023CFAE  40 8A CE                        mov cl, sil
0023CFB1  E8 46 87 2B 00                  call 0x1404f56fc
0023CFB6  90                              nop
0023CFB7  E9 2A AA 49 00                  jmp 0x1406d79e6
0023CFBC  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0023CFC0  45 8A C1                        mov r8b, r9b
0023CFC3  48 8B 10                        mov rdx, qword ptr [rax]
0023CFC6  48 85 D2                        test rdx, rdx
0023CFC9  0F 85 2D AA 49 00               jne 0x1406d79fc
0023CFCF  E9 3C AA 49 00                  jmp 0x1406d7a10
0023CFD4  FF 4E 20                        dec dword ptr [rsi + 0x20]
0023CFD7  E9 4D FB FF FF                  jmp 0x14023cb29
0023CFDC  48 8B D3                        mov rdx, rbx
0023CFDF  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0023CFE4  E8 3F F7 06 00                  call 0x1402ac728
0023CFE9  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
0023CFEE  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0023CFF3  E9 23 FC FF FF                  jmp 0x14023cc1b
0023CFF8  40 88 7E 28                     mov byte ptr [rsi + 0x28], dil
0023CFFC  E9 79 FE FF FF                  jmp 0x14023ce7a
0023D001  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
0023D006  45 85 E4                        test r12d, r12d
0023D009  0F 85 92 FE FF FF               jne 0x14023cea1
0023D00F  01 3D 27 A3 BF 00               add dword ptr [rip + 0xbfa327], edi
0023D015  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0023D01A  4D 85 C9                        test r9, r9
0023D01D  0F 84 68 AA 49 00               je 0x1406d7a8b
0023D023  44 39 54 24 64                  cmp dword ptr [rsp + 0x64], r10d
0023D028  0F 84 6F AA 49 00               je 0x1406d7a9d
0023D02E  4D 2B F9                        sub r15, r9
0023D031  49 8B C9                        mov rcx, r9
0023D034  49 8D 57 D0                     lea rdx, [r15 - 0x30]
0023D038  48 C1 FA 03                     sar rdx, 3
0023D03C  E8 E3 EB 43 00                  call 0x14067bc24
0023D041  45 33 DB                        xor r11d, r11d
0023D044  E9 42 AA 49 00                  jmp 0x1406d7a8b
0023D049  49 8B D7                        mov rdx, r15
0023D04C  48 8B C8                        mov rcx, rax
0023D04F  48 2B D0                        sub rdx, rax
0023D052  48 83 EA 30                     sub rdx, 0x30
0023D056  48 C1 FA 03                     sar rdx, 3
0023D05A  E8 C5 EB 43 00                  call 0x14067bc24
0023D05F  E9 E4 FA FF FF                  jmp 0x14023cb48
0023D064  F0 49 FF 49 10                  lock dec qword ptr [r9 + 0x10]
0023D069  E9 62 FD FF FF                  jmp 0x14023cdd0
0023D06E  E8 6D A3 03 00                  call 0x1402773e0
0023D073  85 C0                           test eax, eax
0023D075  0F 84 7B FB FF FF               je 0x14023cbf6
0023D07B  E9 1C FB FF FF                  jmp 0x14023cb9c
0023D080  01 3D C2 A2 BF 00               add dword ptr [rip + 0xbfa2c2], edi
0023D086  BB 18 00 00 C0                  mov ebx, 0xc0000018
0023D08B  41 8B D1                        mov edx, r9d
0023D08E  E9 50 AA 49 00                  jmp 0x1406d7ae3
0023D093  4C 2B F8                        sub r15, rax
0023D096  48 8B C8                        mov rcx, rax
0023D099  49 8D 57 D0                     lea rdx, [r15 - 0x30]
0023D09D  48 C1 FA 03                     sar rdx, 3
0023D0A1  E8 7E EB 43 00                  call 0x14067bc24
0023D0A6  E9 8F FD FF FF                  jmp 0x14023ce3a
0023D0AB  4C 8B F3                        mov r14, rbx
0023D0AE  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
0023D0B2  E9 E0 F9 FF FF                  jmp 0x14023ca97
0023D0B7  49 8B F0                        mov rsi, r8
0023D0BA  41 8B DE                        mov ebx, r14d
0023D0BD  E9 CC F9 FF FF                  jmp 0x14023ca8e
0023D0C2  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
0023D0C6  E9 18 AA 49 00                  jmp 0x1406d7ae3
0023D0CB  85 DB                           test ebx, ebx
0023D0CD  B8 9A 00 00 C0                  mov eax, 0xc000009a
0023D0D2  0F 49 D8                        cmovns ebx, eax
0023D0D5  49 83 FE FF                     cmp r14, -1
0023D0D9  0F 84 C9 F9 FF FF               je 0x14023caa8
0023D0DF  8B 4C 24 2C                     mov ecx, dword ptr [rsp + 0x2c]
0023D0E3  4C 2B F7                        sub r14, rdi
0023D0E6  4D 8B C6                        mov r8, r14
0023D0E9  48 8B D7                        mov rdx, rdi
0023D0EC  E8 BF E0 06 00                  call 0x1402ab1b0
0023D0F1  E9 B2 F9 FF FF                  jmp 0x14023caa8
0023D0F6  33 D2                           xor edx, edx
0023D0F8  48 8B C8                        mov rcx, rax
0023D0FB  E8 70 57 94 00                  call 0x140b82870
0023D100  E9 B0 F9 FF FF                  jmp 0x14023cab5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReferenceIoPages(int a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m144;
    unsigned int v_stack_m14C;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p2C;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int8 v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 12377881)) ^ (v_rsp);
    v_stack_m48 = result;
    a2 = 0;
    v_stack_m188 = a3;
    v_stack_m17C = (unsigned int)((int)(a1));
    v_stack_m110 = a5;
    v_stack_m108 = a6;
    v_stack_m178 = a4;
    result = memset(v_stack_mF8, a2, 176, a4);
    result = 0;
    v_r10 = 0;
    v_stack_m150 = 0;
    v_stack_m160 = v_xmm0;
    if (a5 != 0) goto loc_0023CF0B;
loc_0023C887:
    if (a6 != 0) {
        *(unsigned __int64 *)(a6) = 0;
    }
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 12522403)) + (244));
    v_stack_m130 = 0;
    v_stack_m170 = 0;
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - (1);
    v_stack_m16C = 0;
    v_rbx = (a2) & (result);
    v_stack_m118 = 0;
    v_stack_m144 = 3;
    result = ((int)(a1)) << (6);
    result = (result) + (v_rip + 12560838);
    v_stack_m168 = v_rbx;
    v_stack_m120 = result;
    if ((*(unsigned int *)(v_rip + 14197802)) != 0) goto loc_0023CDDC;
loc_0023C8FC:
    v_r13 = (unsigned __int8)(v_cr8);
    if (((unsigned __int8)(v_cr8)) == ((unsigned __int8)(1 + 1))) { v_r13 = 17; }
    result = 17 - 12;
    if (((unsigned __int8)(v_cr8)) != ((unsigned __int8)(1 + 1))) { result = 1; }
    v_stack_m180 = (unsigned int)(result);
    result = MiIoSpaceGetBounds(v_stack_m160, v_rbx, 176, a4);
    if (v_stack_m14C != 3) goto loc_0023CD29;
loc_0023C934:
    result = MiLockIoPfnTree(5, v_rbx, 176, a4);
    v_r14 = 0;
loc_0023C949:
    if (a3 == 0) goto loc_0023D0C2;
    if (v_rbx < v_stack_m160) goto loc_0023CF42;
    if (v_rbx > v_stack_m158) goto loc_0023CF42;
loc_0023C96B:
    if (((unsigned int)((unsigned int)(v_stack_m17C))) == 1) goto loc_0023CCDB;
loc_0023C973:
    a1 = (v_rbx - 1) + (a3);
    if (*(unsigned __int64 *)(v_rip + 12560782) == 0) goto loc_0023C9A1;
loc_0023C986:
    if (a1 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560782) + 24))) goto loc_0023CA55;
loc_0023C993:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560782)) != 0) goto loc_0023C986;
loc_0023C998:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560782)) != 0) goto loc_0023D080;
loc_0023C9A1:
    v_stack_m174 = 0;
loc_0023C9B0:
    if (*(unsigned __int64 *)(v_stack_m120) == 0) goto loc_0023C9DA;
loc_0023C9B2:
    if (v_rbx < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m120) + 24))) goto loc_0023CD1B;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m120) + 24)) + (512);
    if (v_rbx < result) goto loc_0023CADF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m120) + 8) != 0) goto loc_0023C9B2;
loc_0023C9DA:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 328)) + (640);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m180))), a3, (unsigned int)(v_stack_m180));
    if (v_stack_m118 == 0) goto loc_0023CD5C;
    result = (v_rbx) & (-512);
    *(unsigned __int64 *)(v_stack_m118 + 24) = result;
    result = MiLockIoPfnTree(6, (unsigned int)((unsigned int)((unsigned int)(v_stack_m180))), a3, (unsigned int)(v_stack_m180));
    a4 = 0;
    a1 = (v_stack_m188 - 1) + (v_rbx);
    if (*(unsigned __int64 *)(v_rip + 12560597) == 0) goto loc_0023CFBC;
loc_0023CA43:
    if (a1 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560597) + 24))) goto loc_0023CA68;
    if (v_rbx <= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560597) + 32))) goto loc_0023CA70;
    goto loc_0023CA6B;
loc_0023CA55:
    if (v_rbx <= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560597) + 8) + 32))) goto loc_0023C998;
    goto loc_0023C993;
loc_0023CA68:
loc_0023CA6B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560597) + 8) + 8)) != 0) goto loc_0023CA43;
loc_0023CA70:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12560597) + 8) + 8)) == 0) goto loc_0023CFBC;
    a2 = (unsigned int)(((unsigned int)(v_stack_m180)) & (0xFFFFFFFEULL));
    a2 = (unsigned int)((a2) | (2));
loc_0023CA8E:
loc_0023CA93:
loc_0023CA97:
    result = MiUnlockIoPfnTree((unsigned __int8)(v_r13), a2, a3, a4);
    if (v_stack_m188 != 0) goto loc_0023D0CB;
loc_0023CAA8:
    if (v_stack_m118 != 0) goto loc_0023D0F6;
loc_0023CAB5:
loc_0023CAB7:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (368);
    return result;
loc_0023CADF:
    v_r14 = (v_stack_p20) - (*(unsigned __int64 *)(v_stack_m188 + 24));
    a2 = 0;
    if (*(unsigned __int64 *)(v_stack_m188 + 24) + 512 != 0) goto loc_0023CD00;
loc_0023CAFB:
    v_stack_p70 = a3 + v_r14 * 1;
loc_0023CB04:
    v_stack_p60 = 0;
    v_stack_p68 = 0;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_m188 + 172, a2, a3, a4);
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(v_stack_p34)) != 0) goto loc_0023CFD4;
loc_0023CB29:
    if (v_r14 < v_stack_p70) goto loc_0023CC05;
    v_r14 = 0;
    if (v_stack_p78 != 0) goto loc_0023D049;
loc_0023CB48:
    if (v_stack_p38 != 0) goto loc_0023CDB6;
loc_0023CB53:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_m188 + 172, v_stack_p70, (unsigned int)(v_stack_p34), a4);
    if (v_stack_p20 == 0) goto loc_0023D0B7;
    if (condition_is_above_or_equal) goto loc_0023CEE9;
loc_0023CB9C:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 328)) + (640);
    result = MiReleaseSpinLockShared(a1, (unsigned __int8)(v_r13), v_stack_p20, (unsigned int)(v_stack_p28));
    if ((*(unsigned int *)(v_rip + 14197066)) != 0) goto loc_0023CEFC;
loc_0023CBDC:
    result = MiIoSpaceGetBounds(v_stack_p48, v_stack_p20, v_stack_p20, (unsigned int)(v_stack_p28));
    result = MiLockIoPfnTree(5, v_stack_p20, v_stack_p20, (unsigned int)(v_stack_p28));
loc_0023CBF6:
    goto loc_0023CEF3;
loc_0023CC05:
    if (v_stack_p20 < v_stack_p48) goto loc_0023CFDC;
    if (v_stack_p20 > v_stack_p50) goto loc_0023CFDC;
loc_0023CC1B:
    if (v_stack_p5C != 3) goto loc_0023CDF2;
loc_0023CC26:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 12521484)) + (244));
    result = (v_stack_m168) << ((unsigned __int8)(a1));
    result = (result) - (v_stack_m168);
    result = (result) & (v_stack_p20);
    result = (result) - (*(unsigned __int64 *)(1 + 1 + 24));
    a1 = (unsigned int)((result + result * 1) & (31));
    result = ((unsigned int)((unsigned int)(result + result * 1))) >> (5);
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 1 + result * 4 + 44))) >> ((unsigned __int8)(a1)));
    v_r12 = (unsigned int)((v_r12) & (3));
    if (((unsigned __int16)(*(unsigned __int16 *)(1 + 1 + v_r14 * 2 + 176))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0023CE2C;
    if ((unsigned __int16)(*(unsigned __int16 *)(1 + 1 + v_r14 * 2 + 176)) != 0) goto loc_0023CC91;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 1 + 32))) == 0) goto loc_0023CE16;
loc_0023CC7E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 1 + 32))) + 1);
    *(unsigned int *)(1 + 1 + 32) = (unsigned int)(result);
    if (((unsigned int)(v_r12)) != ((unsigned int)((unsigned int)(v_stack_p30)))) goto loc_0023CE71;
loc_0023CC91:
    if (v_stack_m110 == 0) goto loc_0023CE68;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m168))) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
loc_0023CCAA:
    if (v_stack_m108 != 0) goto loc_0023CCD1;
loc_0023CCBC:
    v_r14 = (v_r14) + (v_stack_m168);
    v_rbx = (v_stack_p20) + (v_stack_m168);
    goto loc_0023CB29;
loc_0023CCD1:
    if ((*(unsigned __int64 *)(v_stack_m108)) != 0) goto loc_0023CCBC;
    *(unsigned __int64 *)(v_stack_m108) = 1 + 1;
    goto loc_0023CCBC;
loc_0023CCDB:
    if (v_stack_p5C == 3) goto loc_0023C973;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m168))) << ((unsigned __int8)((unsigned int)(v_stack_p58))));
loc_0023CD00:
    if (((unsigned int)(v_stack_p34) + v_rbx * 1) <= ((unsigned int)(v_stack_p58))) goto loc_0023CAFB;
    v_stack_p70 = 512;
    goto loc_0023CB04;
loc_0023CD1B:
    goto loc_0023C9B0;
loc_0023CD29:
    if (((unsigned int)(*(unsigned __int64 *)(1 + 1))) != ((unsigned int)(v_stack_m168))) goto loc_0023C934;
    result = (v_r14 - 1) + (v_rbx);
    if (result > v_stack_p50) goto loc_0023C934;
    if (((unsigned __int8)((unsigned __int8)(1 + 1))) != 0) goto loc_0023CF14;
    if (v_stack_m110 != 0) goto loc_0023CF33;
loc_0023CD55:
    result = 0;
    goto loc_0023CAB7;
loc_0023CD5C:
    if (((unsigned __int8)((unsigned __int8)(1 + 1))) != 17) goto loc_0023CF5E;
    result = MiPageToNode(v_rbx, *(unsigned __int16 *)(1 + 1 + v_r14 * 2 + 176), (unsigned int)(v_stack_p34), (unsigned int)(v_stack_p28));
    result = ExAllocatePoolMm(64, (unsigned int)(0x4B0ULL), (unsigned int)(0x6F49694DULL), (unsigned int)((unsigned int)(result)));
    if (result != 0) goto loc_0023CF7D;
    v_rbx = (v_rbx) - (v_stack_p40);
    result = MiDereferenceIoPages((unsigned int)(v_stack_p2C), v_stack_p40, v_rbx, (unsigned int)((unsigned int)(result)));
    goto loc_0023CAB7;
loc_0023CDB6:
    result = MiIsPageInIoHugeRangeTransition(*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1) + 24), v_stack_p40, v_rbx, v_stack_m120);
    if ((unsigned int)(result) != 0) goto loc_0023D064;
loc_0023CDD0:
    v_stack_p38 = (unsigned int)((unsigned __int8)(result));
    goto loc_0023CB53;
loc_0023CDDC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(1 + 1)), (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1) + 24)), v_rbx, v_stack_m120);
    v_r10 = 0;
    goto loc_0023C8FC;
loc_0023CDF2:
    if (v_stack_p2C != ((unsigned int)(v_stack_m168))) goto loc_0023CC26;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m168))) << ((unsigned __int8)((unsigned int)(v_stack_p58))));
loc_0023CE16:
    a1 = (unsigned __int8)((unsigned int)(v_stack_p38));
    if ((unsigned int)(v_rbx) == 0) { a1 = (unsigned int)(v_stack_m168); }
    v_stack_p38 = a1;
    goto loc_0023CC7E;
loc_0023CE2C:
    if (v_stack_p78 != 0) goto loc_0023D093;
loc_0023CE3A:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(1 + 1) + 172, (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1) + 24)), v_rbx, v_stack_m120);
    if (v_rbx != v_stack_p40) goto loc_0023D0AB;
    goto loc_0023CA93;
loc_0023CE68:
    goto loc_0023CCAA;
loc_0023CE71:
    if (0 == ((unsigned int)(v_stack_p40))) goto loc_0023CFF8;
loc_0023CE7A:
    if (((unsigned int)(v_stack_m110)) == 3) goto loc_0023CEA1;
    result = (unsigned int)(v_stack_p28);
    if (v_stack_p60 == 0) {
        result = MiFlushEntireTbDueToAttributeChange(*(unsigned __int64 *)(1 + 1) + 172, (unsigned int)((unsigned int)((unsigned int)(v_stack_p28))), v_rbx, v_stack_m120);
        v_r10 = v_stack_p30;
        v_r11 = 0;
        v_stack_p60 = (unsigned int)(v_stack_p40);
    }
    if (((unsigned int)(v_stack_m110)) == ((unsigned int)(v_stack_p40))) goto loc_0023D001;
loc_0023CEA1:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 12520849)) + (244));
    result = (v_stack_p40) << ((unsigned __int8)(a1));
    result = (result) - (v_stack_p40);
    result = (result) & ((unsigned int)(v_stack_p3C));
    result = (result) - (*(unsigned __int64 *)(v_stack_p20 + 24));
    a1 = (unsigned int)((result + result * 1) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + result * 1))) >> (5));
    a2 = (unsigned int)((3) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)(~(a2));
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_stack_p20 + result * 4 + 44)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    *(unsigned int *)(v_stack_p20 + (unsigned int)((unsigned int)(result)) * 4 + 44) = (unsigned int)(a2);
    goto loc_0023CC91;
loc_0023CEE9:
    if (((unsigned __int8)((unsigned __int8)(1 + 1))) != 17) goto loc_0023D06E;
loc_0023CEF3:
    goto loc_0023C949;
loc_0023CEFC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)(v_stack_p2C)), (unsigned __int8)(result), (unsigned int)((unsigned int)(result)), v_stack_m120);
    goto loc_0023CBDC;
loc_0023CF0B:
    *(unsigned int *)((unsigned int)((unsigned int)(v_r10))) = (unsigned int)(v_r10);
    goto loc_0023C887;
loc_0023CF14:
    result = KiLowerIrqlProcessIrqlFlags(2, (unsigned __int8)((unsigned __int8)(1 + 1)), (unsigned int)((unsigned int)(result)), v_stack_m120);
loc_0023CF33:
    v_rdi = (unsigned int)((v_stack_p40) << ((unsigned __int8)((unsigned int)(v_stack_p58))));
    goto loc_0023CD55;
loc_0023CF42:
    result = MiIoSpaceGetBounds(v_stack_p48, (unsigned int)(v_stack_p3C), (unsigned int)((unsigned int)(result)), v_stack_m120);
    goto loc_0023C96B;
loc_0023CF5E:
    result = KiLowerIrqlProcessIrqlFlags(2, (unsigned __int8)((unsigned __int8)(1 + 1)), v_stack_p20, (unsigned int)(v_stack_p28));
loc_0023CF7D:
    *(unsigned int *)(result + 32) = (unsigned int)(v_rdi);
    result = MiInitializeIoPageNodeArray(result, (unsigned __int8)((unsigned __int8)(1 + 1)), v_stack_p20, (unsigned int)(v_stack_p28));
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, v_stack_p20, (unsigned int)(v_stack_p28));
loc_0023CFBC:
loc_0023CFD4:
    goto loc_0023CB29;
loc_0023CFDC:
    result = MiIoSpaceGetBounds(v_stack_p48, (unsigned int)(v_stack_p3C), (unsigned __int8)((unsigned int)(v_stack_p28)), (unsigned int)(v_stack_p28));
    goto loc_0023CC1B;
loc_0023CFF8:
    *(unsigned __int8 *)(2 + 40) = (unsigned __int8)(v_rdi);
    goto loc_0023CE7A;
loc_0023D001:
    if ((unsigned int)((unsigned int)(v_stack_p68)) != 0) goto loc_0023CEA1;
    v_r15 = (0) - (v_stack_p78);
    a2 = (v_r15 - 48) >> (3);
    result = MiFlushCachedIoPfnRange(v_stack_p78, a2, (unsigned int)(v_stack_p34), v_stack_p78);
    v_r11 = 0;
loc_0023D049:
    a2 = (v_r15) - (result);
    a2 = (a2) - (48);
    a2 = (a2) >> (3);
    result = MiFlushCachedIoPfnRange(result, a2, (unsigned int)(v_stack_p34), v_stack_p78);
    goto loc_0023CB48;
loc_0023D064:
    goto loc_0023CDD0;
loc_0023D06E:
    result = KeShouldYieldProcessor(result, a2, (unsigned int)(v_stack_p34), v_stack_p78);
    if ((unsigned int)(result) == 0) goto loc_0023CBF6;
    goto loc_0023CB9C;
loc_0023D080:
loc_0023D093:
    v_r15 = (v_r15) - (result);
    a2 = (v_r15 - 48) >> (3);
    result = MiFlushCachedIoPfnRange(result, a2, (unsigned int)(v_stack_p34), v_stack_p78);
    goto loc_0023CE3A;
loc_0023D0AB:
    goto loc_0023CA97;
loc_0023D0B7:
    goto loc_0023CA8E;
loc_0023D0C2:
loc_0023D0CB:
    v_rbx = (unsigned int)(v_stack_p3C);
    if (!sign_flag) { v_rbx = (unsigned int)((unsigned int)(0xC000009AULL)); }
    if (((unsigned int)(0xC0000018ULL)) == -1) goto loc_0023CAA8;
    v_r14 = ((unsigned int)(0xC0000018ULL)) - (v_rdi);
    result = MiDereferenceIoPages((unsigned int)(v_stack_p2C), v_rdi, v_r14, v_stack_p78);
    goto loc_0023CAA8;
loc_0023D0F6:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_r14, v_stack_p78);
    goto loc_0023CAB5;
}
```

## 5. (Beta) C Style

```c
int64_t MiReferenceIoPages(int32_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m144;
    uint32_t v_stack_m14C;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m48;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p2C;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint8_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0xBCDF19)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg2 = 0;
    v_stack_m188 = Arg3;
    v_stack_m17C = (uint32_t)((int32_t)(Arg1));
    v_stack_m110 = Arg5;
    v_stack_m108 = Arg6;
    v_stack_m178 = Arg4;
    result = memset(v_stack_mF8, Arg2, 176, Arg4);
    result = 0;
    local_r10 = 0;
    v_stack_m150 = 0;
    v_stack_m160 = v_xmm0;
    if (Arg5 != 0) goto loc_0023CF0B;
loc_0023C887:
    if (Arg6 != 0) {
        *(uint64_t *)(Arg6) = 0;
    }
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xBF13A3)) + (244));
    v_stack_m130 = 0;
    v_stack_m170 = 0;
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - (1);
    v_stack_m16C = 0;
    local_rbx = (Arg2) & (result);
    v_stack_m118 = 0;
    v_stack_m144 = 3;
    result = ((int32_t)(Arg1)) << (6);
    result = (result) + (v_rip + 12560838);
    v_stack_m168 = local_rbx;
    v_stack_m120 = result;
    if ((*(uint32_t *)(v_rip + 0xD8A42A)) != 0) goto loc_0023CDDC;
loc_0023C8FC:
    local_r13 = (uint8_t)(v_cr8);
    if (((uint8_t)(v_cr8)) == ((uint8_t)(1 + 1))) { local_r13 = 17; }
    result = 17 - 12;
    if (((uint8_t)(v_cr8)) != ((uint8_t)(1 + 1))) { result = 1; }
    v_stack_m180 = (uint32_t)(result);
    result = MiIoSpaceGetBounds(v_stack_m160, local_rbx, 176, Arg4);
    if (v_stack_m14C != 3) goto loc_0023CD29;
loc_0023C934:
    result = MiLockIoPfnTree(5, local_rbx, 176, Arg4);
    local_r14 = 0;
loc_0023C949:
    if (Arg3 == NULL) goto loc_0023D0C2;
    if (local_rbx < v_stack_m160) goto loc_0023CF42;
    if (local_rbx > v_stack_m158) goto loc_0023CF42;
loc_0023C96B:
    if (((uint32_t)((uint32_t)(v_stack_m17C))) == 1) goto loc_0023CCDB;
loc_0023C973:
    Arg1 = (local_rbx - 1) + (Arg3);
    if (*(uint64_t *)(v_rip + 0xBFA98E) == 0) goto loc_0023C9A1;
loc_0023C986:
    if (Arg1 >= (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA98E) + 0x18))) goto loc_0023CA55;
loc_0023C993:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA98E)) != 0) goto loc_0023C986;
loc_0023C998:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA98E)) != 0) goto loc_0023D080;
loc_0023C9A1:
    v_stack_m174 = 0;
loc_0023C9B0:
    if (*(uint64_t *)(v_stack_m120) == 0) goto loc_0023C9DA;
loc_0023C9B2:
    if (local_rbx < (*(uint64_t *)(*(uint64_t *)(v_stack_m120) + 0x18))) goto loc_0023CD1B;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m120) + 0x18)) + (512);
    if (local_rbx < result) goto loc_0023CADF;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m120) + 0x8) != 0) goto loc_0023C9B2;
loc_0023C9DA:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x148)) + (640);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m180))), Arg3, (uint32_t)(v_stack_m180));
    if (v_stack_m118 == 0) goto loc_0023CD5C;
    result = (local_rbx) & (-512);
    *(uint64_t *)(v_stack_m118 + 0x18) = result;
    result = MiLockIoPfnTree(6, (uint32_t)((uint32_t)((uint32_t)(v_stack_m180))), Arg3, (uint32_t)(v_stack_m180));
    Arg4 = 0;
    Arg1 = (v_stack_m188 - 1) + (local_rbx);
    if (*(uint64_t *)(v_rip + 0xBFA8D5) == 0) goto loc_0023CFBC;
loc_0023CA43:
    if (Arg1 < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA8D5) + 0x18))) goto loc_0023CA68;
    if (local_rbx <= (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA8D5) + 0x20))) goto loc_0023CA70;
    goto loc_0023CA6B;
loc_0023CA55:
    if (local_rbx <= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA8D5) + 0x8) + 0x20))) goto loc_0023C998;
    goto loc_0023C993;
loc_0023CA68:
loc_0023CA6B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA8D5) + 0x8) + 0x8)) != 0) goto loc_0023CA43;
loc_0023CA70:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFA8D5) + 0x8) + 0x8)) == 0) goto loc_0023CFBC;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m180)) & (0xFFFFFFFEULL));
    Arg2 = (uint32_t)((Arg2) | (2));
loc_0023CA8E:
loc_0023CA93:
loc_0023CA97:
    result = MiUnlockIoPfnTree((uint8_t)(local_r13), Arg2, Arg3, Arg4);
    if (v_stack_m188 != 0) goto loc_0023D0CB;
loc_0023CAA8:
    if (v_stack_m118 != 0) goto loc_0023D0F6;
loc_0023CAB5:
loc_0023CAB7:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (368);
    return result;
loc_0023CADF:
    local_r14 = (v_stack_p20) - (*(uint64_t *)(v_stack_m188 + 0x18));
    Arg2 = 0;
    if (*(uint64_t *)(v_stack_m188 + 0x18) + 512 != 0) goto loc_0023CD00;
loc_0023CAFB:
    v_stack_p70 = Arg3 + local_r14 * 1;
loc_0023CB04:
    v_stack_p60 = 0;
    v_stack_p68 = 0;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_m188 + 172, Arg2, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(v_stack_p34)) != 0) goto loc_0023CFD4;
loc_0023CB29:
    if (local_r14 < v_stack_p70) goto loc_0023CC05;
    local_r14 = 0;
    if (v_stack_p78 != 0) goto loc_0023D049;
loc_0023CB48:
    if (v_stack_p38 != 0) goto loc_0023CDB6;
loc_0023CB53:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_m188 + 172, v_stack_p70, (uint32_t)(v_stack_p34), Arg4);
    if (v_stack_p20 == 0) goto loc_0023D0B7;
    if (condition_is_above_or_equal) goto loc_0023CEE9;
loc_0023CB9C:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x148)) + (640);
    result = MiReleaseSpinLockShared(Arg1, (uint8_t)(local_r13), v_stack_p20, (uint32_t)(v_stack_p28));
    if ((*(uint32_t *)(v_rip + 0xD8A14A)) != 0) goto loc_0023CEFC;
loc_0023CBDC:
    result = MiIoSpaceGetBounds(v_stack_p48, v_stack_p20, v_stack_p20, (uint32_t)(v_stack_p28));
    result = MiLockIoPfnTree(5, v_stack_p20, v_stack_p20, (uint32_t)(v_stack_p28));
loc_0023CBF6:
    goto loc_0023CEF3;
loc_0023CC05:
    if (v_stack_p20 < v_stack_p48) goto loc_0023CFDC;
    if (v_stack_p20 > v_stack_p50) goto loc_0023CFDC;
loc_0023CC1B:
    if (v_stack_p5C != 3) goto loc_0023CDF2;
loc_0023CC26:
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xBF100C)) + (244));
    result = (v_stack_m168) << ((uint8_t)(Arg1));
    result = (result) - (v_stack_m168);
    result = (result) & (v_stack_p20);
    result = (result) - (*(uint64_t *)(1 + 0x1 + 0x18));
    Arg1 = (uint32_t)((result + result * 1) & (31));
    result = ((uint32_t)((uint32_t)(result + result * 1))) >> (5);
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x1 + result * 4 + 0x2C))) >> ((uint8_t)(Arg1)));
    local_r12 = (uint32_t)((local_r12) & (3));
    if (((uint16_t)(*(uint16_t *)(1 + 0x1 + local_r14 * 2 + 0xB0))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0023CE2C;
    if ((uint16_t)(*(uint16_t *)(1 + 0x1 + local_r14 * 2 + 0xB0)) != 0) goto loc_0023CC91;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x1 + 0x20))) == 0) goto loc_0023CE16;
loc_0023CC7E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x1 + 0x20))) + 1);
    *(uint32_t *)(1 + 0x1 + 0x20) = (uint32_t)(result);
    if (((uint32_t)(local_r12)) != ((uint32_t)((uint32_t)(v_stack_p30)))) goto loc_0023CE71;
loc_0023CC91:
    if (v_stack_m110 == 0) goto loc_0023CE68;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m168))) << ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
loc_0023CCAA:
    if (v_stack_m108 != 0) goto loc_0023CCD1;
loc_0023CCBC:
    local_r14 = (local_r14) + (v_stack_m168);
    local_rbx = (v_stack_p20) + (v_stack_m168);
    goto loc_0023CB29;
loc_0023CCD1:
    if ((*(uint64_t *)(v_stack_m108)) != 0) goto loc_0023CCBC;
    *(uint64_t *)(v_stack_m108) = 1 + 1;
    goto loc_0023CCBC;
loc_0023CCDB:
    if (v_stack_p5C == 3) goto loc_0023C973;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m168))) << ((uint8_t)((uint32_t)(v_stack_p58))));
loc_0023CD00:
    if (((uint32_t)(v_stack_p34) + local_rbx * 1) <= ((uint32_t)(v_stack_p58))) goto loc_0023CAFB;
    v_stack_p70 = 512;
    goto loc_0023CB04;
loc_0023CD1B:
    goto loc_0023C9B0;
loc_0023CD29:
    if (((uint32_t)(*(uint64_t *)(1 + 0x1))) != ((uint32_t)(v_stack_m168))) goto loc_0023C934;
    result = (local_r14 - 1) + (local_rbx);
    if (result > v_stack_p50) goto loc_0023C934;
    if (((uint8_t)((uint8_t)(1 + 1))) != 0) goto loc_0023CF14;
    if (v_stack_m110 != 0) goto loc_0023CF33;
loc_0023CD55:
    result = 0;
    goto loc_0023CAB7;
loc_0023CD5C:
    if (((uint8_t)((uint8_t)(1 + 1))) != 17) goto loc_0023CF5E;
    result = MiPageToNode(local_rbx, *(uint16_t *)(1 + 0x1 + local_r14 * 2 + 0xB0), (uint32_t)(v_stack_p34), (uint32_t)(v_stack_p28));
    result = ExAllocatePoolMm(64, (uint32_t)(0x4B0ULL), (uint32_t)(0x6F49694DULL), (uint32_t)((uint32_t)(result)));
    if (result != 0) goto loc_0023CF7D;
    local_rbx = (local_rbx) - (v_stack_p40);
    result = MiDereferenceIoPages((uint32_t)(v_stack_p2C), v_stack_p40, local_rbx, (uint32_t)((uint32_t)(result)));
    goto loc_0023CAB7;
loc_0023CDB6:
    result = MiIsPageInIoHugeRangeTransition(*(uint64_t *)(*(uint64_t *)(1 + 0x1) + 0x18), v_stack_p40, local_rbx, v_stack_m120);
    if ((uint32_t)(result) != 0) goto loc_0023D064;
loc_0023CDD0:
    v_stack_p38 = (uint32_t)((uint8_t)(result));
    goto loc_0023CB53;
loc_0023CDDC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(1 + 0x1)), (uint8_t)(*(uint64_t *)(*(uint64_t *)(1 + 0x1) + 0x18)), local_rbx, v_stack_m120);
    local_r10 = 0;
    goto loc_0023C8FC;
loc_0023CDF2:
    if (v_stack_p2C != ((uint32_t)(v_stack_m168))) goto loc_0023CC26;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m168))) << ((uint8_t)((uint32_t)(v_stack_p58))));
loc_0023CE16:
    Arg1 = (uint8_t)((uint32_t)(v_stack_p38));
    if ((uint32_t)(local_rbx) == 0) { Arg1 = (uint32_t)(v_stack_m168); }
    v_stack_p38 = Arg1;
    goto loc_0023CC7E;
loc_0023CE2C:
    if (v_stack_p78 != 0) goto loc_0023D093;
loc_0023CE3A:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(1 + 0x1) + 172, (uint8_t)(*(uint64_t *)(*(uint64_t *)(1 + 0x1) + 0x18)), local_rbx, v_stack_m120);
    if (local_rbx != v_stack_p40) goto loc_0023D0AB;
    goto loc_0023CA93;
loc_0023CE68:
    goto loc_0023CCAA;
loc_0023CE71:
    if (0 == ((uint32_t)(v_stack_p40))) goto loc_0023CFF8;
loc_0023CE7A:
    if (((uint32_t)(v_stack_m110)) == 3) goto loc_0023CEA1;
    result = (uint32_t)(v_stack_p28);
    if (v_stack_p60 == 0) {
        result = MiFlushEntireTbDueToAttributeChange(*(uint64_t *)(1 + 0x1) + 172, (uint32_t)((uint32_t)((uint32_t)(v_stack_p28))), local_rbx, v_stack_m120);
        local_r10 = v_stack_p30;
        local_r11 = 0;
        v_stack_p60 = (uint32_t)(v_stack_p40);
    }
    if (((uint32_t)(v_stack_m110)) == ((uint32_t)(v_stack_p40))) goto loc_0023D001;
loc_0023CEA1:
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xBF0D91)) + (244));
    result = (v_stack_p40) << ((uint8_t)(Arg1));
    result = (result) - (v_stack_p40);
    result = (result) & ((uint32_t)(v_stack_p3C));
    result = (result) - (*(uint64_t *)(v_stack_p20 + 0x18));
    Arg1 = (uint32_t)((result + result * 1) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + result * 1))) >> (5));
    Arg2 = (uint32_t)((3) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)(~(Arg2));
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_stack_p20 + result * 4 + 0x2C)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    *(uint32_t *)(v_stack_p20 + (uint32_t)((uint32_t)(result)) * 4 + 0x2C) = (uint32_t)(Arg2);
    goto loc_0023CC91;
loc_0023CEE9:
    if (((uint8_t)((uint8_t)(1 + 1))) != 17) goto loc_0023D06E;
loc_0023CEF3:
    goto loc_0023C949;
loc_0023CEFC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint32_t)(v_stack_p2C)), (uint8_t)(result), (uint32_t)((uint32_t)(result)), v_stack_m120);
    goto loc_0023CBDC;
loc_0023CF0B:
    *(uint32_t *)((uint32_t)((uint32_t)(local_r10))) = (uint32_t)(local_r10);
    goto loc_0023C887;
loc_0023CF14:
    result = KiLowerIrqlProcessIrqlFlags(2, (uint8_t)((uint8_t)(1 + 1)), (uint32_t)((uint32_t)(result)), v_stack_m120);
loc_0023CF33:
    local_rdi = (uint32_t)((v_stack_p40) << ((uint8_t)((uint32_t)(v_stack_p58))));
    goto loc_0023CD55;
loc_0023CF42:
    result = MiIoSpaceGetBounds(v_stack_p48, (uint32_t)(v_stack_p3C), (uint32_t)((uint32_t)(result)), v_stack_m120);
    goto loc_0023C96B;
loc_0023CF5E:
    result = KiLowerIrqlProcessIrqlFlags(2, (uint8_t)((uint8_t)(1 + 1)), v_stack_p20, (uint32_t)(v_stack_p28));
loc_0023CF7D:
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rdi);
    result = MiInitializeIoPageNodeArray(result, (uint8_t)((uint8_t)(1 + 1)), v_stack_p20, (uint32_t)(v_stack_p28));
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, v_stack_p20, (uint32_t)(v_stack_p28));
loc_0023CFBC:
loc_0023CFD4:
    goto loc_0023CB29;
loc_0023CFDC:
    result = MiIoSpaceGetBounds(v_stack_p48, (uint32_t)(v_stack_p3C), (uint8_t)((uint32_t)(v_stack_p28)), (uint32_t)(v_stack_p28));
    goto loc_0023CC1B;
loc_0023CFF8:
    *(uint8_t *)(2 + 0x28) = (uint8_t)(local_rdi);
    goto loc_0023CE7A;
loc_0023D001:
    if ((uint32_t)((uint32_t)(v_stack_p68)) != 0) goto loc_0023CEA1;
    local_r15 = (0) - (v_stack_p78);
    Arg2 = (local_r15 - 48) >> (3);
    result = MiFlushCachedIoPfnRange(v_stack_p78, Arg2, (uint32_t)(v_stack_p34), v_stack_p78);
    local_r11 = 0;
loc_0023D049:
    Arg2 = (local_r15) - (result);
    Arg2 = (Arg2) - (48);
    Arg2 = (Arg2) >> (3);
    result = MiFlushCachedIoPfnRange(result, Arg2, (uint32_t)(v_stack_p34), v_stack_p78);
    goto loc_0023CB48;
loc_0023D064:
    goto loc_0023CDD0;
loc_0023D06E:
    result = KeShouldYieldProcessor(result, Arg2, (uint32_t)(v_stack_p34), v_stack_p78);
    if ((uint32_t)(result) == 0) goto loc_0023CBF6;
    goto loc_0023CB9C;
loc_0023D080:
loc_0023D093:
    local_r15 = (local_r15) - (result);
    Arg2 = (local_r15 - 48) >> (3);
    result = MiFlushCachedIoPfnRange(result, Arg2, (uint32_t)(v_stack_p34), v_stack_p78);
    goto loc_0023CE3A;
loc_0023D0AB:
    goto loc_0023CA97;
loc_0023D0B7:
    goto loc_0023CA8E;
loc_0023D0C2:
loc_0023D0CB:
    local_rbx = (uint32_t)(v_stack_p3C);
    if (!sign_flag) { local_rbx = (uint32_t)((uint32_t)(0xC000009AULL)); }
    if (((uint32_t)(0xC0000018ULL)) == -1) goto loc_0023CAA8;
    local_r14 = ((uint32_t)(0xC0000018ULL)) - (local_rdi);
    result = MiDereferenceIoPages((uint32_t)(v_stack_p2C), local_rdi, local_r14, v_stack_p78);
    goto loc_0023CAA8;
loc_0023D0F6:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_r14, v_stack_p78);
    goto loc_0023CAB5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `- 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023C804&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
