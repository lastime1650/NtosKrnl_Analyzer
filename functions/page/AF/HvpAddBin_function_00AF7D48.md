# HvpAddBin

- RVA: `0x00AF7D48`–`0x00AF84D6` (길이 `1,934` bytes)
- VA: `0x0000000140AF7D48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7524`
- 디코드: `522`개 명령, `1,934/1,934` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AF7E60` → [CmpCanGrowHive](../A6/CmpCanGrowHive_function_00A60C38.md) (function, `0x00A60C38`)
- `0x00AF7E78` → [HvpExpandMap](../A5/HvpExpandMap_function_00A56B90.md) (function, `0x00A56B90`)
- `0x00AF7EA3` → [HvpAdjustHiveFreeDisplay](../84/HvpAdjustHiveFreeDisplay_function_0084DB80.md) (function, `0x0084DB80`)
- `0x00AF7ED1` → [HvpGrowDirtyVectors](../../text/3E/HvpGrowDirtyVectors_function_003E2028.md) (function, `0x003E2028`)
- `0x00AF7F07` → [CmpDoFileSetSizeEx](../9B/CmpDoFileSetSizeEx_function_009B2A4C.md) (function, `0x009B2A4C`)
- `0x00AF7FAB` → [HvpMarkDirty](../85/HvpMarkDirty_function_008593C0.md) (function, `0x008593C0`)
- `0x00AF7FCB` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x00AF7FFF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF806B` → [HvpViewMapExtendStorage](../9B/HvpViewMapExtendStorage_function_009B4EF8.md) (function, `0x009B4EF8`)
- `0x00AF8095` → [CmpClaimGlobalQuota](../84/CmpClaimGlobalQuota_function_0084DDAC.md) (function, `0x0084DDAC`)
- `0x00AF80B6` → [HvpAdjustHiveFreeDisplay](../84/HvpAdjustHiveFreeDisplay_function_0084DB80.md) (function, `0x0084DB80`)
- `0x00AF80C6` → [HvpShrinkMap](../7F/HvpShrinkMap_function_007F3D78.md) (function, `0x007F3D78`)
- `0x00AF80FB` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x00AF811B` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x00AF8137` → [HvpViewMapShrinkStorage](../7E/HvpViewMapShrinkStorage_function_007EEE1C.md) (function, `0x007EEE1C`)
- `0x00AF815A` → [HvpFreeBin](../A8/HvpFreeBin_function_00A8158C.md) (function, `0x00A8158C`)
- `0x00AF8164` → [Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline_function_0066DE24.md) (function, `0x0066DE24`)
- `0x00AF81A1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF81BF` → [HvpFreeBin](../A8/HvpFreeBin_function_00A8158C.md) (function, `0x00A8158C`)
- `0x00AF81D1` → [CmpReleaseGlobalQuota](../84/CmpReleaseGlobalQuota_function_0084DB40.md) (function, `0x0084DB40`)
- `0x00AF81EF` → [HvpViewMapPromoteRangeToMapping](../9B/HvpViewMapPromoteRangeToMapping_function_009B94C8.md) (function, `0x009B94C8`)
- `0x00AF820F` → [HvpViewMapCOWAndUnsealRange](../9B/HvpViewMapCOWAndUnsealRange_function_009B5B44.md) (function, `0x009B5B44`)
- `0x00AF822E` → [HvpAllocateBin](../9B/HvpAllocateBin_function_009B78A4.md) (function, `0x009B78A4`)
- `0x00AF8256` → [HvpProtectBinPartial](../9B/HvpProtectBinPartial_function_009B5D84.md) (function, `0x009B5D84`)
- `0x00AF8277` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF82B2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF82C3` → [Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline_function_0066DE24.md) (function, `0x0066DE24`)
- `0x00AF82E5` → [CmpClaimGlobalQuota](../84/CmpClaimGlobalQuota_function_0084DDAC.md) (function, `0x0084DDAC`)
- `0x00AF8306` → [HvpViewMapPromoteRangeToMapping](../9B/HvpViewMapPromoteRangeToMapping_function_009B94C8.md) (function, `0x009B94C8`)
- `0x00AF8325` → [HvpViewMapCOWAndUnsealRange](../9B/HvpViewMapCOWAndUnsealRange_function_009B5B44.md) (function, `0x009B5B44`)
- `0x00AF8344` → [HvpAllocateBin](../9B/HvpAllocateBin_function_009B78A4.md) (function, `0x009B78A4`)
- `0x00AF8369` → [HvpProtectBinPartial](../9B/HvpProtectBinPartial_function_009B5D84.md) (function, `0x009B5D84`)
- `0x00AF8384` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF83D8` → [HvpPointMapEntriesToBuffer](../9B/HvpPointMapEntriesToBuffer_function_009B7328.md) (function, `0x009B7328`)
- `0x00AF842F` → [HvpPointMapEntriesToBuffer](../9B/HvpPointMapEntriesToBuffer_function_009B7328.md) (function, `0x009B7328`)
- `0x00AF8454` → [HvpMarkDirty](../85/HvpMarkDirty_function_008593C0.md) (function, `0x008593C0`)
- `0x00AF8472` → [CmpUpdateSystemHiveHysteresis](../A7/CmpUpdateSystemHiveHysteresis_function_00A720C4.md) (function, `0x00A720C4`)
- `0x00AF8489` → [HvpSetRangeProtection](../9B/HvpSetRangeProtection_function_009B58C0.md) (function, `0x009B58C0`)
- `0x00AF84D0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HvAllocateCell](../85/HvAllocateCell_function_00859C94.md) at `0x00859EAA`
- [sub_0085A1C1](../85/Unknown_function_0085A1C1.md) at `0x0085A1CE`

### Static image references
- `0x00AF8106` → RVA `0x00EF554C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00AF7ED1` → [HvpGrowDirtyVectors](../../text/3E/HvpGrowDirtyVectors_function_003E2028.md) (`PAGE` → `.text`)
  - `0x00AF7FCB` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x00AF7FFF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF80FB` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (`PAGE` → `.text`)
  - `0x00AF811B` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (`PAGE` → `.text`)
  - `0x00AF8164` → [Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline_function_0066DE24.md) (`PAGE` → `.text`)
  - `0x00AF81A1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF8277` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF82B2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF82C3` → [Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline_function_0066DE24.md) (`PAGE` → `.text`)
  - `0x00AF8384` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF84D0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF7D48  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00AF7D4D  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00AF7D52  55                              push rbp
00AF7D53  53                              push rbx
00AF7D54  56                              push rsi
00AF7D55  57                              push rdi
00AF7D56  41 54                           push r12
00AF7D58  41 55                           push r13
00AF7D5A  41 56                           push r14
00AF7D5C  41 57                           push r15
00AF7D5E  48 8B EC                        mov rbp, rsp
00AF7D61  48 83 EC 68                     sub rsp, 0x68
00AF7D65  8D BA 1F 10 00 00               lea edi, [rdx + 0x101f]
00AF7D6B  49 63 F0                        movsxd rsi, r8d
00AF7D6E  45 33 C0                        xor r8d, r8d
00AF7D71  81 E7 00 F0 FF FF               and edi, 0xfffff000
00AF7D77  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
00AF7D7B  4C 8B F1                        mov r14, rcx
00AF7D7E  44 88 45 C8                     mov byte ptr [rbp - 0x38], r8b
00AF7D82  45 8B E0                        mov r12d, r8d
00AF7D85  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00AF7D89  41 B9 00 10 00 00               mov r9d, 0x1000
00AF7D8F  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
00AF7D93  44 88 45 48                     mov byte ptr [rbp + 0x48], r8b
00AF7D97  44 89 45 D4                     mov dword ptr [rbp - 0x2c], r8d
00AF7D9B  44 88 45 50                     mov byte ptr [rbp + 0x50], r8b
00AF7D9F  81 FF 00 30 00 00               cmp edi, 0x3000
00AF7DA5  77 17                           ja 0x140af7dbe
00AF7DA7  8B CF                           mov ecx, edi
00AF7DA9  8B C2                           mov eax, edx
00AF7DAB  48 2B C8                        sub rcx, rax
00AF7DAE  48 83 E9 20                     sub rcx, 0x20
00AF7DB2  48 81 F9 00 0E 00 00            cmp rcx, 0xe00
00AF7DB9  73 03                           jae 0x140af7dbe
00AF7DBB  41 03 F9                        add edi, r9d
00AF7DBE  48 69 C6 78 02 00 00            imul rax, rsi, 0x278
00AF7DC5  49 8D 96 78 03 00 00            lea rdx, [r14 + 0x378]
00AF7DCC  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
00AF7DD0  48 03 D0                        add rdx, rax
00AF7DD3  4E 8D 3C 30                     lea r15, [rax + r14]
00AF7DD7  48 8B 1A                        mov rbx, qword ptr [rdx]
00AF7DDA  EB 1F                           jmp 0x140af7dfb
00AF7DDC  44 8B 6B 10                     mov r13d, dword ptr [rbx + 0x10]
00AF7DE0  44 3B EF                        cmp r13d, edi
00AF7DE3  72 13                           jb 0x140af7df8
00AF7DE5  8B 4B 14                        mov ecx, dword ptr [rbx + 0x14]
00AF7DE8  41 03 CD                        add ecx, r13d
00AF7DEB  41 3B 8F 18 01 00 00            cmp ecx, dword ptr [r15 + 0x118]
00AF7DF2  0F 86 75 01 00 00               jbe 0x140af7f6d
00AF7DF8  48 8B 1B                        mov rbx, qword ptr [rbx]
00AF7DFB  48 3B DA                        cmp rbx, rdx
00AF7DFE  75 DC                           jne 0x140af7ddc
00AF7E00  45 8B BF 18 01 00 00            mov r15d, dword ptr [r15 + 0x118]
00AF7E07  44 89 7D CC                     mov dword ptr [rbp - 0x34], r15d
00AF7E0B  45 8D 2C 3F                     lea r13d, [r15 + rdi]
00AF7E0F  85 F6                           test esi, esi
00AF7E11  75 3E                           jne 0x140af7e51
00AF7E13  81 FF 00 00 04 00               cmp edi, 0x40000
00AF7E19  77 36                           ja 0x140af7e51
00AF7E1B  41 8D 8D FF 0F 00 00            lea ecx, [r13 + 0xfff]
00AF7E22  BA 00 00 FC FF                  mov edx, 0xfffc0000
00AF7E27  41 8D 87 00 10 00 00            lea eax, [r15 + 0x1000]
00AF7E2E  33 C8                           xor ecx, eax
00AF7E30  85 CA                           test edx, ecx
00AF7E32  74 1D                           je 0x140af7e51
00AF7E34  41 8D 87 FF 0F 04 00            lea eax, [r15 + 0x40fff]
00AF7E3B  23 C2                           and eax, edx
00AF7E3D  41 2B C1                        sub eax, r9d
00AF7E40  44 8B C0                        mov r8d, eax
00AF7E43  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00AF7E46  45 2B C7                        sub r8d, r15d
00AF7E49  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
00AF7E4D  44 8D 2C 38                     lea r13d, [rax + rdi]
00AF7E51  45 3B EF                        cmp r13d, r15d
00AF7E54  0F 82 46 06 00 00               jb 0x140af84a0
00AF7E5A  41 8B D5                        mov edx, r13d
00AF7E5D  49 8B CE                        mov rcx, r14
00AF7E60  E8 D3 8D F6 FF                  call 0x140a60c38
00AF7E65  84 C0                           test al, al
00AF7E67  0F 84 33 06 00 00               je 0x140af84a0
00AF7E6D  45 8B CD                        mov r9d, r13d
00AF7E70  45 8B C7                        mov r8d, r15d
00AF7E73  8B D6                           mov edx, esi
00AF7E75  49 8B CE                        mov rcx, r14
00AF7E78  E8 13 ED F5 FF                  call 0x140a56b90
00AF7E7D  8B F0                           mov esi, eax
00AF7E7F  85 C0                           test eax, eax
00AF7E81  0F 88 1E 06 00 00               js 0x140af84a5
00AF7E87  48 69 45 F0 78 02 00 00         imul rax, qword ptr [rbp - 0x10], 0x278
00AF7E8F  8B 5D 58                        mov ebx, dword ptr [rbp + 0x58]
00AF7E92  41 8B D5                        mov edx, r13d
00AF7E95  44 8B C3                        mov r8d, ebx
00AF7E98  49 8B CE                        mov rcx, r14
00AF7E9B  46 89 AC 30 18 01 00 00         mov dword ptr [rax + r14 + 0x118], r13d
00AF7EA3  E8 D8 5C D5 FF                  call 0x14084db80
00AF7EA8  8B F0                           mov esi, eax
00AF7EAA  85 C0                           test eax, eax
00AF7EAC  0F 88 09 02 00 00               js 0x140af80bb
00AF7EB2  85 DB                           test ebx, ebx
00AF7EB4  0F 85 C3 01 00 00               jne 0x140af807d
00AF7EBA  49 8D 9E A0 00 00 00            lea rbx, [r14 + 0xa0]
00AF7EC1  8B 03                           mov eax, dword ptr [rbx]
00AF7EC3  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00AF7EC7  A8 01                           test al, 1
00AF7EC9  75 24                           jne 0x140af7eef
00AF7ECB  41 8B D5                        mov edx, r13d
00AF7ECE  49 8B CE                        mov rcx, r14
00AF7ED1  E8 52 A1 8E FF                  call 0x1403e2028
00AF7ED6  8B F0                           mov esi, eax
00AF7ED8  85 C0                           test eax, eax
00AF7EDA  0F 88 CA 01 00 00               js 0x140af80aa
00AF7EE0  49 8D 86 A0 00 00 00            lea rax, [r14 + 0xa0]
00AF7EE7  C6 45 C8 01                     mov byte ptr [rbp - 0x38], 1
00AF7EEB  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00AF7EEF  F7 03 01 80 00 00               test dword ptr [rbx], 0x8001
00AF7EF5  75 43                           jne 0x140af7f3a
00AF7EF7  33 D2                           xor edx, edx
00AF7EF9  45 8D 85 00 10 00 00            lea r8d, [r13 + 0x1000]
00AF7F00  49 8B CE                        mov rcx, r14
00AF7F03  44 8D 4A 01                     lea r9d, [rdx + 1]
00AF7F07  E8 40 AB EB FF                  call 0x1409b2a4c
00AF7F0C  8B F0                           mov esi, eax
00AF7F0E  85 C0                           test eax, eax
00AF7F10  0F 88 94 01 00 00               js 0x140af80aa
00AF7F16  41 F7 86 10 10 00 00 00 08 00 00  test dword ptr [r14 + 0x1010], 0x800
00AF7F21  74 17                           je 0x140af7f3a
00AF7F23  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00AF7F27  48 8B D8                        mov rbx, rax
00AF7F2A  45 39 A6 84 10 00 00            cmp dword ptr [r14 + 0x1084], r12d
00AF7F31  75 07                           jne 0x140af7f3a
00AF7F33  45 89 BE 84 10 00 00            mov dword ptr [r14 + 0x1084], r15d
00AF7F3A  F7 03 00 00 02 00               test dword ptr [rbx], 0x20000
00AF7F40  0F 84 37 01 00 00               je 0x140af807d
00AF7F46  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
00AF7F4D  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00AF7F54  BA 00 F0 FF 7F                  mov edx, 0x7ffff000
00AF7F59  A8 01                           test al, 1
00AF7F5B  0F 84 E4 00 00 00               je 0x140af8045
00AF7F61  49 8B 86 F0 00 00 00            mov rax, qword ptr [r14 + 0xf0]
00AF7F68  E9 E3 00 00 00                  jmp 0x140af8050
00AF7F6D  48 85 DB                        test rbx, rbx
00AF7F70  0F 84 8A FE FF FF               je 0x140af7e00
00AF7F76  48 8B 0B                        mov rcx, qword ptr [rbx]
00AF7F79  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
00AF7F7D  0F 85 16 05 00 00               jne 0x140af8499
00AF7F83  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF7F87  48 39 18                        cmp qword ptr [rax], rbx
00AF7F8A  0F 85 09 05 00 00               jne 0x140af8499
00AF7F90  48 89 08                        mov qword ptr [rax], rcx
00AF7F93  8B FE                           mov edi, esi
00AF7F95  48 89 41 08                     mov qword ptr [rcx + 8], rax
00AF7F99  45 33 C9                        xor r9d, r9d
00AF7F9C  8B 53 14                        mov edx, dword ptr [rbx + 0x14]
00AF7F9F  49 8B CE                        mov rcx, r14
00AF7FA2  44 8B 43 10                     mov r8d, dword ptr [rbx + 0x10]
00AF7FA6  C1 E7 1F                        shl edi, 0x1f
00AF7FA9  03 D7                           add edx, edi
00AF7FAB  E8 10 14 D6 FF                  call 0x1408593c0
00AF7FB0  8B F0                           mov esi, eax
00AF7FB2  85 C0                           test eax, eax
00AF7FB4  78 5B                           js 0x140af8011
00AF7FB6  03 7B 14                        add edi, dword ptr [rbx + 0x14]
00AF7FB9  45 33 C0                        xor r8d, r8d
00AF7FBC  45 85 ED                        test r13d, r13d
00AF7FBF  74 32                           je 0x140af7ff3
00AF7FC1  45 8D 1C 38                     lea r11d, [r8 + rdi]
00AF7FC5  49 8B CE                        mov rcx, r14
00AF7FC8  41 8B D3                        mov edx, r11d
00AF7FCB  E8 40 17 0D 00                  call 0x140bc9710
00AF7FD0  4C 8B D0                        mov r10, rax
00AF7FD3  48 85 C0                        test rax, rax
00AF7FD6  0F 84 DD 04 00 00               je 0x140af84b9
00AF7FDC  49 83 62 08 FD                  and qword ptr [r10 + 8], 0xfffffffffffffffd
00AF7FE1  41 8B C0                        mov eax, r8d
00AF7FE4  41 81 C0 00 10 00 00            add r8d, 0x1000
00AF7FEB  49 89 02                        mov qword ptr [r10], rax
00AF7FEE  45 3B C5                        cmp r8d, r13d
00AF7FF1  72 CE                           jb 0x140af7fc1
00AF7FF3  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00AF7FF7  BA 18 00 00 00                  mov edx, 0x18
00AF7FFC  48 8B CB                        mov rcx, rbx
00AF7FFF  E8 CC 2A BC FF                  call 0x1406baad0
00AF8004  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00AF8008  89 38                           mov dword ptr [rax], edi
00AF800A  33 F6                           xor esi, esi
00AF800C  E9 94 04 00 00                  jmp 0x140af84a5
00AF8011  48 63 45 58                     movsxd rax, dword ptr [rbp + 0x58]
00AF8015  48 69 C0 78 02 00 00            imul rax, rax, 0x278
00AF801C  48 05 78 03 00 00               add rax, 0x378
00AF8022  49 03 C6                        add rax, r14
00AF8025  48 8B 08                        mov rcx, qword ptr [rax]
00AF8028  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00AF802C  0F 85 67 04 00 00               jne 0x140af8499
00AF8032  48 89 0B                        mov qword ptr [rbx], rcx
00AF8035  48 89 43 08                     mov qword ptr [rbx + 8], rax
00AF8039  48 89 59 08                     mov qword ptr [rcx + 8], rbx
00AF803D  48 89 18                        mov qword ptr [rax], rbx
00AF8040  E9 60 04 00 00                  jmp 0x140af84a5
00AF8045  A8 08                           test al, 8
00AF8047  74 12                           je 0x140af805b
00AF8049  49 8B 86 E8 00 00 00            mov rax, qword ptr [r14 + 0xe8]
00AF8050  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00AF8056  48 3B C2                        cmp rax, rdx
00AF8059  7C 03                           jl 0x140af805e
00AF805B  48 8B C2                        mov rax, rdx
00AF805E  05 00 F0 FF FF                  add eax, 0xfffff000
00AF8063  44 3B E8                        cmp r13d, eax
00AF8066  77 15                           ja 0x140af807d
00AF8068  41 8B D5                        mov edx, r13d
00AF806B  E8 88 CE EB FF                  call 0x1409b4ef8
00AF8070  8B F0                           mov esi, eax
00AF8072  85 C0                           test eax, eax
00AF8074  78 34                           js 0x140af80aa
00AF8076  B3 01                           mov bl, 1
00AF8078  88 5D 48                        mov byte ptr [rbp + 0x48], bl
00AF807B  EB 03                           jmp 0x140af8080
00AF807D  41 8A DC                        mov bl, r12b
00AF8080  8B 75 D0                        mov esi, dword ptr [rbp - 0x30]
00AF8083  85 F6                           test esi, esi
00AF8085  0F 84 54 02 00 00               je 0x140af82df
00AF808B  84 DB                           test bl, bl
00AF808D  0F 84 83 01 00 00               je 0x140af8216
00AF8093  8B CE                           mov ecx, esi
00AF8095  E8 12 5D D5 FF                  call 0x14084ddac
00AF809A  84 C0                           test al, al
00AF809C  0F 85 39 01 00 00               jne 0x140af81db
00AF80A2  BE 9A 00 00 C0                  mov esi, 0xc000009a
00AF80A7  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF80AA  8B 5D 58                        mov ebx, dword ptr [rbp + 0x58]
00AF80AD  41 8B D7                        mov edx, r15d
00AF80B0  44 8B C3                        mov r8d, ebx
00AF80B3  49 8B CE                        mov rcx, r14
00AF80B6  E8 C5 5A D5 FF                  call 0x14084db80
00AF80BB  45 8B CF                        mov r9d, r15d
00AF80BE  45 8B C5                        mov r8d, r13d
00AF80C1  8B D3                           mov edx, ebx
00AF80C3  49 8B CE                        mov rcx, r14
00AF80C6  E8 AD BC CF FF                  call 0x1407f3d78
00AF80CB  48 63 C3                        movsxd rax, ebx
00AF80CE  48 69 C8 78 02 00 00            imul rcx, rax, 0x278
00AF80D5  80 7D C8 00                     cmp byte ptr [rbp - 0x38], 0
00AF80D9  46 89 BC 31 18 01 00 00         mov dword ptr [rcx + r14 + 0x118], r15d
00AF80E1  74 44                           je 0x140af8127
00AF80E3  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
00AF80E7  49 8D 4E 58                     lea rcx, [r14 + 0x58]
00AF80EB  48 89 41 08                     mov qword ptr [rcx + 8], rax
00AF80EF  41 8B FF                        mov edi, r15d
00AF80F2  C1 EF 09                        shr edi, 9
00AF80F5  89 39                           mov dword ptr [rcx], edi
00AF80F7  41 8B 5E 68                     mov ebx, dword ptr [r14 + 0x68]
00AF80FB  E8 70 BE 93 FF                  call 0x140433f70
00AF8100  41 89 46 68                     mov dword ptr [r14 + 0x68], eax
00AF8104  2B C3                           sub eax, ebx
00AF8106  F0 01 05 3F D4 3F 00            lock add dword ptr [rip + 0x3fd43f], eax
00AF810D  49 8B 46 78                     mov rax, qword ptr [r14 + 0x78]
00AF8111  49 8D 4E 70                     lea rcx, [r14 + 0x70]
00AF8115  89 39                           mov dword ptr [rcx], edi
00AF8117  48 89 41 08                     mov qword ptr [rcx + 8], rax
00AF811B  E8 50 BE 93 FF                  call 0x140433f70
00AF8120  41 89 86 80 00 00 00            mov dword ptr [r14 + 0x80], eax
00AF8127  80 7D 50 00                     cmp byte ptr [rbp + 0x50], 0
00AF812B  74 0F                           je 0x140af813c
00AF812D  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00AF8134  41 8B D7                        mov edx, r15d
00AF8137  E8 E0 6C CF FF                  call 0x1407eee1c
00AF813C  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00AF8140  8A 5D 48                        mov bl, byte ptr [rbp + 0x48]
00AF8143  8B 7D CC                        mov edi, dword ptr [rbp - 0x34]
00AF8146  48 85 C0                        test rax, rax
00AF8149  74 14                           je 0x140af815f
00AF814B  84 DB                           test bl, bl
00AF814D  75 10                           jne 0x140af815f
00AF814F  8B D7                           mov edx, edi
00AF8151  4C 8B C0                        mov r8, rax
00AF8154  41 2B D7                        sub edx, r15d
00AF8157  49 8B CE                        mov rcx, r14
00AF815A  E8 2D 94 F8 FF                  call 0x140a8158c
00AF815F  4D 85 E4                        test r12, r12
00AF8162  74 42                           je 0x140af81a6
00AF8164  E8 BB 5C B7 FF                  call 0x14066de24
00AF8169  85 C0                           test eax, eax
00AF816B  74 28                           je 0x140af8195
00AF816D  49 8B 04 24                     mov rax, qword ptr [r12]
00AF8171  49 3B C4                        cmp rax, r12
00AF8174  74 1F                           je 0x140af8195
00AF8176  4C 39 60 08                     cmp qword ptr [rax + 8], r12
00AF817A  0F 85 19 03 00 00               jne 0x140af8499
00AF8180  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
00AF8185  4C 39 21                        cmp qword ptr [rcx], r12
00AF8188  0F 85 0B 03 00 00               jne 0x140af8499
00AF818E  48 89 01                        mov qword ptr [rcx], rax
00AF8191  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AF8195  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00AF8199  BA 18 00 00 00                  mov edx, 0x18
00AF819E  49 8B CC                        mov rcx, r12
00AF81A1  E8 2A 29 BC FF                  call 0x1406baad0
00AF81A6  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00AF81AA  48 85 C0                        test rax, rax
00AF81AD  74 15                           je 0x140af81c4
00AF81AF  84 DB                           test bl, bl
00AF81B1  75 11                           jne 0x140af81c4
00AF81B3  44 2B EF                        sub r13d, edi
00AF81B6  4C 8B C0                        mov r8, rax
00AF81B9  41 8B D5                        mov edx, r13d
00AF81BC  49 8B CE                        mov rcx, r14
00AF81BF  E8 C8 93 F8 FF                  call 0x140a8158c
00AF81C4  8B 45 D4                        mov eax, dword ptr [rbp - 0x2c]
00AF81C7  85 C0                           test eax, eax
00AF81C9  0F 84 D6 02 00 00               je 0x140af84a5
00AF81CF  8B C8                           mov ecx, eax
00AF81D1  E8 6A 59 D5 FF                  call 0x14084db40
00AF81D6  E9 CA 02 00 00                  jmp 0x140af84a5
00AF81DB  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00AF81E2  89 75 D4                        mov dword ptr [rbp - 0x2c], esi
00AF81E5  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00AF81E9  44 8B C6                        mov r8d, esi
00AF81EC  41 8B D7                        mov edx, r15d
00AF81EF  E8 D4 12 EC FF                  call 0x1409b94c8
00AF81F4  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF81F7  8B F0                           mov esi, eax
00AF81F9  85 C0                           test eax, eax
00AF81FB  0F 88 A9 FE FF FF               js 0x140af80aa
00AF8201  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00AF8205  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00AF820C  41 8B D7                        mov edx, r15d
00AF820F  E8 30 D9 EB FF                  call 0x1409b5b44
00AF8214  EB 45                           jmp 0x140af825b
00AF8216  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
00AF821A  48 8D 45 E0                     lea rax, [rbp - 0x20]
00AF821E  41 B9 43 4D 32 30               mov r9d, 0x30324d43
00AF8224  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF8229  8B D6                           mov edx, esi
00AF822B  49 8B CE                        mov rcx, r14
00AF822E  E8 71 F6 EB FF                  call 0x1409b78a4
00AF8233  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF8236  8B F0                           mov esi, eax
00AF8238  85 C0                           test eax, eax
00AF823A  0F 88 6A FE FF FF               js 0x140af80aa
00AF8240  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00AF8243  45 33 C9                        xor r9d, r9d
00AF8246  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
00AF824A  49 8B CE                        mov rcx, r14
00AF824D  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00AF8252  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AF8256  E8 29 DB EB FF                  call 0x1409b5d84
00AF825B  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF825E  8B F0                           mov esi, eax
00AF8260  85 C0                           test eax, eax
00AF8262  0F 88 42 FE FF FF               js 0x140af80aa
00AF8268  8B 75 D0                        mov esi, dword ptr [rbp - 0x30]
00AF826B  33 D2                           xor edx, edx
00AF826D  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
00AF8271  44 8B C6                        mov r8d, esi
00AF8274  49 8B CC                        mov rcx, r12
00AF8277  E8 C4 E9 BC FF                  call 0x1406c6c40
00AF827C  41 83 64 24 1C 00               and dword ptr [r12 + 0x1c], 0
00AF8282  41 8B C7                        mov eax, r15d
00AF8285  0F BA F0 1F                     btr eax, 0x1f
00AF8289  41 C7 04 24 68 62 69 6E         mov dword ptr [r12], 0x6e696268
00AF8291  41 89 44 24 04                  mov dword ptr [r12 + 4], eax
00AF8296  33 D2                           xor edx, edx
00AF8298  8D 46 E0                        lea eax, [rsi - 0x20]
00AF829B  41 89 74 24 08                  mov dword ptr [r12 + 8], esi
00AF82A0  41 89 44 24 20                  mov dword ptr [r12 + 0x20], eax
00AF82A5  41 B8 43 4D 32 31               mov r8d, 0x31324d43
00AF82AB  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00AF82AF  8D 4A 18                        lea ecx, [rdx + 0x18]
00AF82B2  E8 19 28 BC FF                  call 0x1406baad0
00AF82B7  4C 8B E0                        mov r12, rax
00AF82BA  48 85 C0                        test rax, rax
00AF82BD  0F 84 DF FD FF FF               je 0x140af80a2
00AF82C3  E8 5C 5B B7 FF                  call 0x14066de24
00AF82C8  85 C0                           test eax, eax
00AF82CA  74 09                           je 0x140af82d5
00AF82CC  4D 89 64 24 08                  mov qword ptr [r12 + 8], r12
00AF82D1  4D 89 24 24                     mov qword ptr [r12], r12
00AF82D5  41 89 74 24 10                  mov dword ptr [r12 + 0x10], esi
00AF82DA  45 89 7C 24 14                  mov dword ptr [r12 + 0x14], r15d
00AF82DF  84 DB                           test bl, bl
00AF82E1  74 49                           je 0x140af832c
00AF82E3  8B CF                           mov ecx, edi
00AF82E5  E8 C2 5A D5 FF                  call 0x14084ddac
00AF82EA  84 C0                           test al, al
00AF82EC  0F 84 B0 FD FF FF               je 0x140af80a2
00AF82F2  8B 55 CC                        mov edx, dword ptr [rbp - 0x34]
00AF82F5  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00AF82FC  01 7D D4                        add dword ptr [rbp - 0x2c], edi
00AF82FF  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00AF8303  44 8B C7                        mov r8d, edi
00AF8306  E8 BD 11 EC FF                  call 0x1409b94c8
00AF830B  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF830E  8B F0                           mov esi, eax
00AF8310  85 C0                           test eax, eax
00AF8312  0F 88 92 FD FF FF               js 0x140af80aa
00AF8318  8B 55 CC                        mov edx, dword ptr [rbp - 0x34]
00AF831B  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00AF8322  44 8B C7                        mov r8d, edi
00AF8325  E8 1A D8 EB FF                  call 0x1409b5b44
00AF832A  EB 42                           jmp 0x140af836e
00AF832C  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
00AF8330  48 8D 45 D8                     lea rax, [rbp - 0x28]
00AF8334  41 B9 43 4D 31 36               mov r9d, 0x36314d43
00AF833A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF833F  8B D7                           mov edx, edi
00AF8341  49 8B CE                        mov rcx, r14
00AF8344  E8 5B F5 EB FF                  call 0x1409b78a4
00AF8349  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF834C  8B F0                           mov esi, eax
00AF834E  85 C0                           test eax, eax
00AF8350  0F 88 54 FD FF FF               js 0x140af80aa
00AF8356  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00AF835A  45 33 C9                        xor r9d, r9d
00AF835D  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00AF8362  49 8B CE                        mov rcx, r14
00AF8365  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AF8369  E8 16 DA EB FF                  call 0x1409b5d84
00AF836E  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF8371  8B F0                           mov esi, eax
00AF8373  85 C0                           test eax, eax
00AF8375  0F 88 2F FD FF FF               js 0x140af80aa
00AF837B  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00AF837F  33 D2                           xor edx, edx
00AF8381  44 8B C7                        mov r8d, edi
00AF8384  E8 B7 E8 BC FF                  call 0x1406c6c40
00AF8389  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00AF838D  8B 75 CC                        mov esi, dword ptr [rbp - 0x34]
00AF8390  8B C6                           mov eax, esi
00AF8392  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
00AF8396  0F BA F0 1F                     btr eax, 0x1f
00AF839A  83 61 1C 00                     and dword ptr [rcx + 0x1c], 0
00AF839E  89 41 04                        mov dword ptr [rcx + 4], eax
00AF83A1  8D 47 E0                        lea eax, [rdi - 0x20]
00AF83A4  89 41 20                        mov dword ptr [rcx + 0x20], eax
00AF83A7  C7 01 68 62 69 6E               mov dword ptr [rcx], 0x6e696268
00AF83AD  89 79 08                        mov dword ptr [rcx + 8], edi
00AF83B0  8B 4D 58                        mov ecx, dword ptr [rbp + 0x58]
00AF83B3  C1 E1 1F                        shl ecx, 0x1f
00AF83B6  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
00AF83B9  48 85 D2                        test rdx, rdx
00AF83BC  74 51                           je 0x140af840f
00AF83BE  8A C3                           mov al, bl
00AF83C0  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00AF83C5  44 8B C6                        mov r8d, esi
00AF83C8  46 8D 0C 39                     lea r9d, [rcx + r15]
00AF83CC  34 01                           xor al, 1
00AF83CE  45 2B C7                        sub r8d, r15d
00AF83D1  49 8B CE                        mov rcx, r14
00AF83D4  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AF83D8  E8 4B EF EB FF                  call 0x1409b7328
00AF83DD  48 69 4D F0 78 02 00 00         imul rcx, qword ptr [rbp - 0x10], 0x278
00AF83E5  48 81 C1 78 03 00 00            add rcx, 0x378
00AF83EC  49 03 CE                        add rcx, r14
00AF83EF  48 8B 01                        mov rax, qword ptr [rcx]
00AF83F2  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00AF83F6  0F 85 9D 00 00 00               jne 0x140af8499
00AF83FC  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
00AF8401  49 89 04 24                     mov qword ptr [r12], rax
00AF8405  4C 89 60 08                     mov qword ptr [rax + 8], r12
00AF8409  4C 89 21                        mov qword ptr [rcx], r12
00AF840C  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
00AF840F  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00AF8415  03 F1                           add esi, ecx
00AF8417  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00AF841B  8A C3                           mov al, bl
00AF841D  34 01                           xor al, 1
00AF841F  89 75 CC                        mov dword ptr [rbp - 0x34], esi
00AF8422  44 8B CE                        mov r9d, esi
00AF8425  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AF8429  44 8B C7                        mov r8d, edi
00AF842C  49 8B CE                        mov rcx, r14
00AF842F  E8 F4 EE EB FF                  call 0x1409b7328
00AF8434  83 7D 58 00                     cmp dword ptr [rbp + 0x58], 0
00AF8438  75 54                           jne 0x140af848e
00AF843A  41 8B 86 A0 00 00 00            mov eax, dword ptr [r14 + 0xa0]
00AF8441  A8 01                           test al, 1
00AF8443  75 24                           jne 0x140af8469
00AF8445  45 8B C5                        mov r8d, r13d
00AF8448  45 33 C9                        xor r9d, r9d
00AF844B  45 2B C7                        sub r8d, r15d
00AF844E  41 8B D7                        mov edx, r15d
00AF8451  49 8B CE                        mov rcx, r14
00AF8454  E8 67 0F D6 FF                  call 0x1408593c0
00AF8459  88 5D 50                        mov byte ptr [rbp + 0x50], bl
00AF845C  8B F0                           mov esi, eax
00AF845E  85 C0                           test eax, eax
00AF8460  0F 88 44 FC FF FF               js 0x140af80aa
00AF8466  8B 75 CC                        mov esi, dword ptr [rbp - 0x34]
00AF8469  45 8B C7                        mov r8d, r15d
00AF846C  41 8B D5                        mov edx, r13d
00AF846F  49 8B CE                        mov rcx, r14
00AF8472  E8 4D 9C F7 FF                  call 0x140a720c4
00AF8477  45 2B EF                        sub r13d, r15d
00AF847A  41 B9 04 00 00 00               mov r9d, 4
00AF8480  45 8B C5                        mov r8d, r13d
00AF8483  41 8B D7                        mov edx, r15d
00AF8486  49 8B CE                        mov rcx, r14
00AF8489  E8 32 D4 EB FF                  call 0x1409b58c0
00AF848E  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00AF8492  89 30                           mov dword ptr [rax], esi
00AF8494  E9 71 FB FF FF                  jmp 0x140af800a
00AF8499  B9 03 00 00 00                  mov ecx, 3
00AF849E  CD 29                           int 0x29
00AF84A0  BE 9A 00 00 C0                  mov esi, 0xc000009a
00AF84A5  8B C6                           mov eax, esi
00AF84A7  48 83 C4 68                     add rsp, 0x68
00AF84AB  41 5F                           pop r15
00AF84AD  41 5E                           pop r14
00AF84AF  41 5D                           pop r13
00AF84B1  41 5C                           pop r12
00AF84B3  5F                              pop rdi
00AF84B4  5E                              pop rsi
00AF84B5  5B                              pop rbx
00AF84B6  5D                              pop rbp
00AF84B7  C3                              ret
00AF84B8  CC                              int3
00AF84B9  BA 01 00 00 00                  mov edx, 1
00AF84BE  45 8B CB                        mov r9d, r11d
00AF84C1  4D 8B C6                        mov r8, r14
00AF84C4  48 C7 44 24 20 97 03 00 00      mov qword ptr [rsp + 0x20], 0x397
00AF84CD  8D 4A 50                        lea ecx, [rdx + 0x50]
00AF84D0  E8 8B 51 A0 FF                  call 0x1404fd660
00AF84D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpAddBin(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (104);
    a3 = 0;
    v_rdi = (unsigned int)((a2 + 4127) & (0xFFFFF000ULL));
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m60 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    v_stack_m6C = 0;
    v_stack_p10 = 0;
    if (((unsigned int)(v_rdi)) > 0x3000ULL) goto loc_00AF7DBE;
    a1 = ((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)((unsigned int)(a2)));
    a1 = (a1) - (32);
    if (a1 < 0xE00ULL) {
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)((unsigned int)(0x1000ULL))));
    }
    result = ((unsigned int)((unsigned int)(a2))) * ((int)(a3));
    v_stack_m50 = (int)(a3);
    a2 = (a1 + 888) + (result);
    goto loc_00AF7DFB;
loc_00AF7DDC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 16)))) < ((unsigned int)(v_rdi))) goto loc_00AF7DF8;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 20))) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 16)))));
    if (((unsigned int)(a1)) <= (*(unsigned int *)(result + a1 * 1 + 280))) goto loc_00AF7F6D;
loc_00AF7DF8:
loc_00AF7DFB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) != a2) goto loc_00AF7DDC;
loc_00AF7E00:
    v_stack_m74 = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)));
    if ((unsigned int)((int)(a3)) != 0) goto loc_00AF7E51;
    if (((unsigned int)(v_rdi)) > 0x40000ULL) goto loc_00AF7E51;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)) + v_rdi * 1 + 4095) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)) + 4096)));
    result = (unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)) + 4096;
    v_r13 = (unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)) + v_rdi * 1;
    if ((((unsigned int)((unsigned int)(0xFFFC0000ULL))) & ((unsigned int)(a1))) != 0) {
        result = (unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)) + 266239;
        result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFC0000ULL))));
        result = (unsigned int)((result) - ((unsigned int)((unsigned int)(0x1000ULL))));
        a3 = (unsigned int)(result);
        v_stack_m74 = (unsigned int)(result);
        a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
        v_stack_m70 = a3;
        v_r13 = result + v_rdi * 1;
    }
    if (((unsigned int)(v_r13)) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280))))) goto loc_00AF84A0;
    result = CmpCanGrowHive(a1, (unsigned int)((unsigned int)(v_r13)), a3, (unsigned int)(0x1000ULL));
    if ((unsigned __int8)(result) == 0) goto loc_00AF84A0;
    result = HvpExpandMap(a1, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_00AF84A5;
    result = (result) * (v_stack_m50);
    *(unsigned int *)(result + a1 * 1 + 280) = (unsigned int)(v_r13);
    result = HvpAdjustHiveFreeDisplay(a1, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_00AF80BB;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_00AF807D;
    v_stack_m58 = a1 + 160;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 160)))) & (1)) != 0) goto loc_00AF7EEF;
    result = HvpGrowDirtyVectors(a1, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_00AF80AA;
    v_stack_m78 = 1;
    v_stack_m58 = a1 + 160;
loc_00AF7EEF:
    if (((*(unsigned int *)(a1 + 160)) & (0x8001ULL)) != 0) goto loc_00AF7F3A;
    a2 = 0;
    result = CmpDoFileSetSizeEx(a1, a2, v_r13 + 4096, a2 + 1);
    if (sign_flag) goto loc_00AF80AA;
    if (((*(unsigned int *)(a1 + 4112)) & (0x800ULL)) == 0) goto loc_00AF7F3A;
    if ((*(unsigned int *)(a1 + 4228)) == 0) {
        *(unsigned int *)(a1 + 4228) = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)));
    }
    if (((*(unsigned int *)(v_stack_m58)) & (0x20000ULL)) == 0) goto loc_00AF807D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 256)))) & (1)) == 0) goto loc_00AF8045;
    goto loc_00AF8050;
loc_00AF7F6D:
    if (v_stack_m58 == 0) goto loc_00AF7E00;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 8)) != v_stack_m58) goto loc_00AF8499;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + 8))) != v_stack_m58) goto loc_00AF8499;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + 8)) = *(unsigned __int64 *)(v_stack_m58);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 8) = *(unsigned __int64 *)(v_stack_m58 + 8);
    a4 = 0;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) << (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 20))) + ((unsigned int)(v_rdi)));
    result = HvpMarkDirty(a1, a2, (unsigned int)(*(unsigned int *)(v_stack_m58 + 16)), a4);
    if (sign_flag) goto loc_00AF8011;
    v_rdi = (unsigned int)((v_rdi) + (*(unsigned int *)(v_stack_m58 + 20)));
    a3 = 0;
    if ((unsigned int)(v_r13) == 0) goto loc_00AF7FF3;
loc_00AF7FC1:
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)(a3 + v_rdi * 1)), a3, a4);
    if (result == 0) goto loc_00AF84B9;
    a3 = (unsigned int)((a3) + (0x1000ULL));
    *(unsigned __int64 *)(result) = 0;
    if (a3 < ((unsigned int)(v_r13))) goto loc_00AF7FC1;
loc_00AF7FF3:
    result = guard_dispatch_icall(v_stack_m58, 24, a3, a4);
    *(unsigned int *)(v_stack_p20) = (unsigned int)(v_rdi);
loc_00AF800A:
    v_rsi = 0;
    goto loc_00AF84A5;
loc_00AF8011:
    result = ((int)(v_stack_p18)) * ((int)(v_stack_p18));
    result = (result) + (888);
    result = (result) + (a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_00AF8499;
    *(unsigned __int64 *)(v_stack_m58) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(v_stack_m58 + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = v_stack_m58;
    *(unsigned __int64 *)(result) = v_stack_m58;
    goto loc_00AF84A5;
loc_00AF8045:
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00AF805B;
loc_00AF8050:
    result = (*(unsigned __int64 *)(a1 + 232)) & (0xFFFFFFFFFFFFF000ULL);
    if (result >= 24) {
        result = 24;
    }
    result = (unsigned int)((result) + (0xFFFFF000ULL));
    if (((unsigned int)(v_r13)) > ((unsigned int)(result))) goto loc_00AF807D;
    result = HvpViewMapExtendStorage(*(unsigned __int64 *)(result), (unsigned int)((unsigned int)(v_r13)), a3, a4);
    if (sign_flag) goto loc_00AF80AA;
    v_stack_p8 = 1;
    goto loc_00AF8080;
loc_00AF807D:
loc_00AF8080:
    if ((unsigned int)((unsigned int)(v_stack_m70)) == 0) goto loc_00AF82DF;
    if (0 == 0) goto loc_00AF8216;
    result = CmpClaimGlobalQuota((unsigned int)((unsigned int)((unsigned int)(v_stack_m70))), (unsigned int)((unsigned int)(v_r13)), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AF81DB;
loc_00AF80A2:
    v_stack_p10 = 0;
loc_00AF80AA:
    result = HvpAdjustHiveFreeDisplay(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), a4);
loc_00AF80BB:
    result = HvpShrinkMap(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    a1 = (a1) * ((int)((unsigned int)((unsigned int)(v_stack_p18))));
    *(unsigned int *)(a1 + a1 * 1 + 280) = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)));
    result = (int)((unsigned int)((unsigned int)(v_stack_p18)));
    v_rbx = (unsigned int)(v_stack_p18);
    if (v_stack_m78 != 0) {
        result = *(unsigned __int64 *)(a1 + 96);
        a1 = a1 + 88;
        *(unsigned __int64 *)(a1 + 8) = result;
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)));
        v_rdi = (unsigned int)((v_rdi) >> (9));
        *(unsigned int *)(a1) = (unsigned int)(v_rdi);
        v_rbx = *(unsigned int *)(a1 + 104);
        result = RtlNumberOfSetBits(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
        *(unsigned int *)(a1 + 104) = (unsigned int)(result);
        result = (unsigned int)((result) - ((unsigned int)(v_rbx)));
        result = *(unsigned __int64 *)(a1 + 120);
        a1 = a1 + 112;
        *(unsigned int *)(a1) = (unsigned int)(v_rdi);
        *(unsigned __int64 *)(a1 + 8) = result;
        result = RtlNumberOfSetBits(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
        *(unsigned int *)(a1 + 128) = (unsigned int)(result);
    }
    if (v_stack_p10 != 0) {
        a1 = a1 + 224;
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)));
        result = HvpViewMapShrinkStorage(a1, a2, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    }
    if (v_stack_m60 == 0) goto loc_00AF815F;
    result = v_stack_m60;
    if ((unsigned __int8)(v_stack_p8) == 0) {
        a2 = (unsigned int)((unsigned int)(v_stack_m74));
        a3 = v_stack_m60;
        a2 = (unsigned int)((a2) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
        a1 = a1;
        result = HvpFreeBin(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    }
    if (0 == 0) goto loc_00AF81A6;
    result = Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    if ((unsigned int)(result) == 0) goto loc_00AF8195;
    if ((*(unsigned __int64 *)(0)) == 0) goto loc_00AF8195;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0) + 8)) != 0) goto loc_00AF8499;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8))) != 0) goto loc_00AF8499;
    *(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8)) = *(unsigned __int64 *)(0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(0) + 8) = *(unsigned __int64 *)(0 + 8);
loc_00AF8195:
    result = guard_dispatch_icall(0, 24, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
loc_00AF81A6:
    if (v_stack_m68 == 0) goto loc_00AF81C4;
    result = v_stack_m68;
    if ((unsigned __int8)(v_stack_p8) == 0) {
        v_r13 = (unsigned int)((v_r13) - ((unsigned int)((unsigned int)(v_stack_m74))));
        a3 = v_stack_m68;
        a2 = (unsigned int)(v_r13);
        a1 = a1;
        result = HvpFreeBin(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    }
    if ((unsigned int)((unsigned int)(v_stack_m6C)) == 0) goto loc_00AF84A5;
    result = CmpReleaseGlobalQuota((unsigned int)((unsigned int)((unsigned int)(v_stack_m6C))), a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    goto loc_00AF84A5;
loc_00AF81DB:
    v_stack_m6C = (unsigned int)((unsigned int)(0xC000009AULL));
    result = HvpViewMapPromoteRangeToMapping(a1 + 224, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), v_stack_m60);
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    result = HvpViewMapCOWAndUnsealRange(a1 + 224, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), (unsigned int)(v_stack_m70), v_stack_m60);
    goto loc_00AF825B;
loc_00AF8216:
    v_stack_m88 = v_stack_m60;
    result = HvpAllocateBin(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_p18), (unsigned int)(0x30324D43ULL));
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    a4 = 0;
    v_stack_m80 = 1;
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_m70));
    result = HvpProtectBinPartial(a1, v_stack_m60, (unsigned int)(v_stack_p18), a4);
loc_00AF825B:
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    a2 = 0;
    result = memset(v_stack_m60, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m70))), a4);
    *(unsigned int *)(v_stack_m60) = 0x6E696268ULL;
    *(unsigned int *)(v_stack_m60 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    a2 = 0;
    *(unsigned int *)(v_stack_m60 + 8) = (unsigned int)((unsigned int)(v_stack_m70));
    *(unsigned int *)(v_stack_m60 + 32) = (unsigned int)((unsigned int)(v_stack_m70) - 32);
    result = guard_dispatch_icall(a2 + 24, a2, (unsigned int)(0x31324D43ULL), a4);
    if (result == 0) goto loc_00AF80A2;
    result = Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline(a2 + 24, a2, (unsigned int)(0x31324D43ULL), a4);
    if ((unsigned int)(result) != 0) {
        *(unsigned __int64 *)(result + 8) = result;
        *(unsigned __int64 *)(result) = result;
    }
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(v_stack_m70));
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)));
loc_00AF82DF:
    if ((unsigned __int8)(v_stack_p8) == 0) goto loc_00AF832C;
    result = CmpClaimGlobalQuota((unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), a2, (unsigned int)(0x31324D43ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF80A2;
    result = HvpViewMapPromoteRangeToMapping(a1 + 224, (unsigned int)(v_stack_m74), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_m68);
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    result = HvpViewMapCOWAndUnsealRange(a1 + 224, (unsigned int)(v_stack_m74), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_m68);
    goto loc_00AF836E;
loc_00AF832C:
    v_stack_m88 = v_stack_m68;
    result = HvpAllocateBin(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), (unsigned int)(v_stack_p18), (unsigned int)(0x36314D43ULL));
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    a4 = 0;
    v_stack_m80 = 1;
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_m74));
    result = HvpProtectBinPartial(a1, v_stack_m68, (unsigned int)(v_stack_p18), a4);
loc_00AF836E:
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    a2 = 0;
    result = memset(v_stack_m68, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), a4);
    *(unsigned int *)(v_stack_m68 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74))));
    *(unsigned int *)(v_stack_m68 + 32) = (unsigned int)((unsigned int)(v_stack_m74) - 32);
    *(unsigned int *)(v_stack_m68) = 0x6E696268ULL;
    *(unsigned int *)(v_stack_m68 + 8) = (unsigned int)((unsigned int)(v_stack_m74));
    a1 = (unsigned int)(((unsigned int)(v_stack_p18)) << (31));
    v_stack_p10 = (unsigned int)(a1);
    if (v_stack_m60 == 0) goto loc_00AF840F;
    v_stack_m80 = result;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p8)) ^ (1));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    v_stack_m88 = (unsigned __int8)(result);
    result = HvpPointMapEntriesToBuffer(a1, v_stack_m60, a3, a1 + (unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)) * 1);
    a1 = (a1) * (v_stack_m50);
    a1 = (a1) + (888);
    a1 = (a1) + (a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) != a1) goto loc_00AF8499;
    *(unsigned __int64 *)(result + 8) = a1;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) = result;
    *(unsigned __int64 *)(a1) = result;
loc_00AF840F:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m74)) + ((unsigned int)((unsigned int)(v_stack_p10))));
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p8)) ^ (1));
    v_stack_m74 = (unsigned int)(v_rsi);
    v_stack_m88 = (unsigned __int8)(result);
    result = HvpPointMapEntriesToBuffer(a1, v_stack_m68, (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), (unsigned int)((unsigned int)(v_rsi)));
    if (v_stack_p18 != 0) goto loc_00AF848E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 160)))) & (1)) != 0) goto loc_00AF8469;
    a4 = 0;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    result = HvpMarkDirty(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), a3, a4);
    v_stack_p10 = (unsigned __int8)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
loc_00AF8469:
    result = CmpUpdateSystemHiveHysteresis(a1, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), a4);
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))));
    result = HvpSetRangeProtection(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + a1 * 1 + 280)))), (unsigned int)((unsigned int)(v_r13)), 4);
loc_00AF848E:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(v_stack_m74));
    goto loc_00AF800A;
loc_00AF8499:
loc_00AF84A0:
loc_00AF84A5:
    v_rsp = (v_rsp) + (104);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
loc_00AF84B9:
    v_stack_p20 = 919;
    result = KeBugCheckEx(1 + 80, 1, a1, (unsigned int)((unsigned int)(a3 + v_rdi * 1)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvpAddBin(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint8_t v_stack_m80;
    uint64_t v_stack_m88;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (104);
    Arg3 = 0;
    local_rdi = (uint32_t)((Arg2 + 4127) & (0xFFFFF000ULL));
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m60 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    v_stack_m6C = 0;
    v_stack_p10 = 0;
    if (((uint32_t)(local_rdi)) > 0x3000ULL) goto loc_00AF7DBE;
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)((uint32_t)(Arg2)));
    Arg1 = (Arg1) - (32);
    if (Arg1 < 0xE00ULL) {
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)((uint32_t)(0x1000ULL))));
    }
    result = ((uint32_t)((uint32_t)(Arg2))) * ((int32_t)(Arg3));
    v_stack_m50 = (int32_t)(Arg3);
    Arg2 = (Arg1 + 888) + (result);
    goto loc_00AF7DFB;
loc_00AF7DDC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x10)))) < ((uint32_t)(local_rdi))) goto loc_00AF7DF8;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x14))) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x10)))));
    if (((uint32_t)(Arg1)) <= (*(uint32_t *)(result + arg1 * 1 + 0x118))) goto loc_00AF7F6D;
loc_00AF7DF8:
loc_00AF7DFB:
    if ((*(uint64_t *)(*(uint64_t *)(arg2))) != Arg2) goto loc_00AF7DDC;
loc_00AF7E00:
    v_stack_m74 = (uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)));
    if ((uint32_t)((int32_t)(Arg3)) != 0) goto loc_00AF7E51;
    if (((uint32_t)(local_rdi)) > 0x40000ULL) goto loc_00AF7E51;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)) + local_rdi * 1 + 4095) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)) + 4096)));
    result = (uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)) + 4096;
    local_r13 = (uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)) + local_rdi * 1;
    if ((((uint32_t)((uint32_t)(0xFFFC0000ULL))) & ((uint32_t)(Arg1))) != 0) {
        result = (uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)) + 266239;
        result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFC0000ULL))));
        result = (uint32_t)((result) - ((uint32_t)((uint32_t)(0x1000ULL))));
        Arg3 = (uint32_t)(result);
        v_stack_m74 = (uint32_t)(result);
        Arg3 = (uint32_t)((Arg3) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
        v_stack_m70 = Arg3;
        local_r13 = result + local_rdi * 1;
    }
    if (((uint32_t)(local_r13)) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118))))) goto loc_00AF84A0;
    result = CmpCanGrowHive(Arg1, (uint32_t)((uint32_t)(local_r13)), Arg3, (uint32_t)(0x1000ULL));
    if ((uint8_t)(result) == 0) goto loc_00AF84A0;
    result = HvpExpandMap(Arg1, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_00AF84A5;
    result = (result) * (v_stack_m50);
    *(uint32_t *)(result + arg1 * 1 + 0x118) = (uint32_t)(local_r13);
    result = HvpAdjustHiveFreeDisplay(Arg1, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_00AF80BB;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_00AF807D;
    v_stack_m58 = Arg1 + 160;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0)))) & (1)) != 0) goto loc_00AF7EEF;
    result = HvpGrowDirtyVectors(Arg1, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_00AF80AA;
    v_stack_m78 = 1;
    v_stack_m58 = Arg1 + 160;
loc_00AF7EEF:
    if (((*(uint32_t *)(arg1 + 0xA0)) & (0x8001ULL)) != 0) goto loc_00AF7F3A;
    Arg2 = 0;
    result = CmpDoFileSetSizeEx(Arg1, Arg2, local_r13 + 4096, Arg2 + 1);
    if (sign_flag) goto loc_00AF80AA;
    if (((*(uint32_t *)(arg1 + 0x1010)) & (0x800ULL)) == 0) goto loc_00AF7F3A;
    if ((*(uint32_t *)(arg1 + 0x1084)) == 0) {
        *(uint32_t *)(arg1 + 0x1084) = (uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)));
    }
    if (((*(uint32_t *)(v_stack_m58)) & (0x20000ULL)) == 0) goto loc_00AF807D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x100)))) & (1)) == 0) goto loc_00AF8045;
    goto loc_00AF8050;
loc_00AF7F6D:
    if (v_stack_m58 == 0) goto loc_00AF7E00;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x8)) != v_stack_m58) goto loc_00AF8499;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m58 + 0x8))) != v_stack_m58) goto loc_00AF8499;
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + 0x8)) = *(uint64_t *)(v_stack_m58);
    *(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x8) = *(uint64_t *)(v_stack_m58 + 0x8);
    Arg4 = 0;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) << (31));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x14))) + ((uint32_t)(local_rdi)));
    result = HvpMarkDirty(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x10)), Arg4);
    if (sign_flag) goto loc_00AF8011;
    local_rdi = (uint32_t)((local_rdi) + (*(uint32_t *)(v_stack_m58 + 0x14)));
    Arg3 = 0;
    if ((uint32_t)(local_r13) == 0) goto loc_00AF7FF3;
loc_00AF7FC1:
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)(Arg3 + local_rdi * 1)), Arg3, Arg4);
    if (result == 0) goto loc_00AF84B9;
    Arg3 = (uint32_t)((Arg3) + (0x1000ULL));
    *(uint64_t *)(result) = 0;
    if (Arg3 < ((uint32_t)(local_r13))) goto loc_00AF7FC1;
loc_00AF7FF3:
    result = guard_dispatch_icall(v_stack_m58, 24, Arg3, Arg4);
    *(uint32_t *)(v_stack_p20) = (uint32_t)(local_rdi);
loc_00AF800A:
    local_rsi = 0;
    goto loc_00AF84A5;
loc_00AF8011:
    result = ((int32_t)(v_stack_p18)) * ((int32_t)(v_stack_p18));
    result = (result) + (888);
    result = (result) + (Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_00AF8499;
    *(uint64_t *)(v_stack_m58) = *(uint64_t *)(result);
    *(uint64_t *)(v_stack_m58 + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = v_stack_m58;
    *(uint64_t *)(result) = v_stack_m58;
    goto loc_00AF84A5;
loc_00AF8045:
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00AF805B;
loc_00AF8050:
    result = (*(uint64_t *)(arg1 + 0xE8)) & (0xFFFFFFFFFFFFF000ULL);
    if (result >= 24) {
        result = 24;
    }
    result = (uint32_t)((result) + (0xFFFFF000ULL));
    if (((uint32_t)(local_r13)) > ((uint32_t)(result))) goto loc_00AF807D;
    result = HvpViewMapExtendStorage(*(uint64_t *)(result), (uint32_t)((uint32_t)(local_r13)), Arg3, Arg4);
    if (sign_flag) goto loc_00AF80AA;
    v_stack_p8 = 1;
    goto loc_00AF8080;
loc_00AF807D:
loc_00AF8080:
    if ((uint32_t)((uint32_t)(v_stack_m70)) == 0) goto loc_00AF82DF;
    if (0 == 0) goto loc_00AF8216;
    result = CmpClaimGlobalQuota((uint32_t)((uint32_t)((uint32_t)(v_stack_m70))), (uint32_t)((uint32_t)(local_r13)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AF81DB;
loc_00AF80A2:
    v_stack_p10 = 0;
loc_00AF80AA:
    result = HvpAdjustHiveFreeDisplay(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), Arg4);
loc_00AF80BB:
    result = HvpShrinkMap(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    Arg1 = (Arg1) * ((int32_t)((uint32_t)((uint32_t)(v_stack_p18))));
    *(uint32_t *)(arg1 + arg1 * 1 + 0x118) = (uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)));
    result = (int32_t)((uint32_t)((uint32_t)(v_stack_p18)));
    local_rbx = (uint32_t)(v_stack_p18);
    if (v_stack_m78 != 0) {
        result = *(uint64_t *)(arg1 + 0x60);
        Arg1 = Arg1 + 88;
        *(uint64_t *)(arg1 + 0x8) = result;
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)));
        local_rdi = (uint32_t)((local_rdi) >> (9));
        *(uint32_t *)(arg1) = (uint32_t)(local_rdi);
        local_rbx = *(uint32_t *)(arg1 + 0x68);
        result = RtlNumberOfSetBits(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
        *(uint32_t *)(arg1 + 0x68) = (uint32_t)(result);
        result = (uint32_t)((result) - ((uint32_t)(local_rbx)));
        result = *(uint64_t *)(arg1 + 0x78);
        Arg1 = Arg1 + 112;
        *(uint32_t *)(arg1) = (uint32_t)(local_rdi);
        *(uint64_t *)(arg1 + 0x8) = result;
        result = RtlNumberOfSetBits(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
        *(uint32_t *)(arg1 + 0x80) = (uint32_t)(result);
    }
    if (v_stack_p10 != 0) {
        Arg1 = Arg1 + 224;
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)));
        result = HvpViewMapShrinkStorage(Arg1, Arg2, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    }
    if (v_stack_m60 == 0) goto loc_00AF815F;
    result = v_stack_m60;
    if ((uint8_t)(v_stack_p8) == 0) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m74));
        Arg3 = v_stack_m60;
        Arg2 = (uint32_t)((Arg2) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
        Arg1 = Arg1;
        result = HvpFreeBin(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    }
    if (0 == 0) goto loc_00AF81A6;
    result = Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    if ((uint32_t)(result) == 0) goto loc_00AF8195;
    if ((*(uint64_t *)(0)) == 0) goto loc_00AF8195;
    if ((*(uint64_t *)(*(uint64_t *)(0) + 0x8)) != 0) goto loc_00AF8499;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x8))) != 0) goto loc_00AF8499;
    *(uint64_t *)(*(uint64_t *)(0 + 0x8)) = *(uint64_t *)(0);
    *(uint64_t *)(*(uint64_t *)(0) + 0x8) = *(uint64_t *)(0 + 0x8);
loc_00AF8195:
    result = guard_dispatch_icall(0, 24, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
loc_00AF81A6:
    if (v_stack_m68 == 0) goto loc_00AF81C4;
    result = v_stack_m68;
    if ((uint8_t)(v_stack_p8) == 0) {
        local_r13 = (uint32_t)((local_r13) - ((uint32_t)((uint32_t)(v_stack_m74))));
        Arg3 = v_stack_m68;
        Arg2 = (uint32_t)(local_r13);
        Arg1 = Arg1;
        result = HvpFreeBin(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    }
    if ((uint32_t)((uint32_t)(v_stack_m6C)) == 0) goto loc_00AF84A5;
    result = CmpReleaseGlobalQuota((uint32_t)((uint32_t)((uint32_t)(v_stack_m6C))), Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    goto loc_00AF84A5;
loc_00AF81DB:
    v_stack_m6C = (uint32_t)((uint32_t)(0xC000009AULL));
    result = HvpViewMapPromoteRangeToMapping(Arg1 + 224, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), v_stack_m60);
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    result = HvpViewMapCOWAndUnsealRange(Arg1 + 224, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), (uint32_t)(v_stack_m70), v_stack_m60);
    goto loc_00AF825B;
loc_00AF8216:
    v_stack_m88 = v_stack_m60;
    result = HvpAllocateBin(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_p18), (uint32_t)(0x30324D43ULL));
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    Arg4 = 0;
    v_stack_m80 = 1;
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_m70));
    result = HvpProtectBinPartial(Arg1, v_stack_m60, (uint32_t)(v_stack_p18), Arg4);
loc_00AF825B:
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    Arg2 = 0;
    result = memset(v_stack_m60, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m70))), Arg4);
    *(uint32_t *)(v_stack_m60) = 0x6E696268ULL;
    *(uint32_t *)(v_stack_m60 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    Arg2 = 0;
    *(uint32_t *)(v_stack_m60 + 0x8) = (uint32_t)((uint32_t)(v_stack_m70));
    *(uint32_t *)(v_stack_m60 + 0x20) = (uint32_t)((uint32_t)(v_stack_m70) - 32);
    result = guard_dispatch_icall(Arg2 + 24, Arg2, (uint32_t)(0x31324D43ULL), Arg4);
    if (result == 0) goto loc_00AF80A2;
    result = Feature_Servicing_RemoveAlignmentFreeBinFromList__private_IsEnabledDeviceUsageNoInline(Arg2 + 24, Arg2, (uint32_t)(0x31324D43ULL), Arg4);
    if ((uint32_t)(result) != 0) {
        *(uint64_t *)(result + 0x8) = result;
        *(uint64_t *)(result) = result;
    }
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(v_stack_m70));
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)));
loc_00AF82DF:
    if ((uint8_t)(v_stack_p8) == 0) goto loc_00AF832C;
    result = CmpClaimGlobalQuota((uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), Arg2, (uint32_t)(0x31324D43ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AF80A2;
    result = HvpViewMapPromoteRangeToMapping(Arg1 + 224, (uint32_t)(v_stack_m74), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_m68);
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    result = HvpViewMapCOWAndUnsealRange(Arg1 + 224, (uint32_t)(v_stack_m74), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_m68);
    goto loc_00AF836E;
loc_00AF832C:
    v_stack_m88 = v_stack_m68;
    result = HvpAllocateBin(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), (uint32_t)(v_stack_p18), (uint32_t)(0x36314D43ULL));
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    Arg4 = 0;
    v_stack_m80 = 1;
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_m74));
    result = HvpProtectBinPartial(Arg1, v_stack_m68, (uint32_t)(v_stack_p18), Arg4);
loc_00AF836E:
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), Arg4);
    *(uint32_t *)(v_stack_m68 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74))));
    *(uint32_t *)(v_stack_m68 + 0x20) = (uint32_t)((uint32_t)(v_stack_m74) - 32);
    *(uint32_t *)(v_stack_m68) = 0x6E696268ULL;
    *(uint32_t *)(v_stack_m68 + 0x8) = (uint32_t)((uint32_t)(v_stack_m74));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p18)) << (31));
    v_stack_p10 = (uint32_t)(Arg1);
    if (v_stack_m60 == 0) goto loc_00AF840F;
    v_stack_m80 = result;
    result = (uint8_t)(((uint8_t)(v_stack_p8)) ^ (1));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    v_stack_m88 = (uint8_t)(result);
    result = HvpPointMapEntriesToBuffer(Arg1, v_stack_m60, Arg3, Arg1 + (uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)) * 1);
    Arg1 = (Arg1) * (v_stack_m50);
    Arg1 = (Arg1) + (888);
    Arg1 = (Arg1) + (Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) != Arg1) goto loc_00AF8499;
    *(void **)(result + 0x8) = Arg1;
    *(uint64_t *)(result) = *(uint64_t *)(arg1);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) = result;
    *(uint64_t *)(arg1) = result;
loc_00AF840F:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m74)) + ((uint32_t)((uint32_t)(v_stack_p10))));
    result = (uint8_t)(((uint8_t)(v_stack_p8)) ^ (1));
    v_stack_m74 = (uint32_t)(local_rsi);
    v_stack_m88 = (uint8_t)(result);
    result = HvpPointMapEntriesToBuffer(Arg1, v_stack_m68, (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), (uint32_t)((uint32_t)(local_rsi)));
    if (v_stack_p18 != 0) goto loc_00AF848E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0)))) & (1)) != 0) goto loc_00AF8469;
    Arg4 = 0;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    result = HvpMarkDirty(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), Arg3, Arg4);
    v_stack_p10 = (uint8_t)(v_stack_p8);
    if (sign_flag) goto loc_00AF80AA;
loc_00AF8469:
    result = CmpUpdateSystemHiveHysteresis(Arg1, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), Arg4);
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))));
    result = HvpSetRangeProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + arg1 * 1 + 0x118)))), (uint32_t)((uint32_t)(local_r13)), 4);
loc_00AF848E:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(v_stack_m74));
    goto loc_00AF800A;
loc_00AF8499:
loc_00AF84A0:
loc_00AF84A5:
    local_rsp = (local_rsp) + (104);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
loc_00AF84B9:
    v_stack_p20 = 919;
    result = KeBugCheckEx(1 + 80, 1, Arg1, (uint32_t)((uint32_t)(Arg3 + local_rdi * 1)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x68` | `32` | `W` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x80` | `32` | `W` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0xE8` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0x100` | `32` | `R` |
| `Arg1` | `+ 0x378` | `64` | `R` |
| `Arg1` | `+ 0x1010` | `32` | `R` |
| `Arg1` | `+ 0x1084` | `32` | `R` |
| `Arg1` | `+ 0x1084` | `32` | `W` |
| `Arg2` | `+ 0x101F` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF7D48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
