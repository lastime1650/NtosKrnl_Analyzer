# CmQueryKey

- RVA: `0x00858240`–`0x00858E5C` (길이 `3,100` bytes)
- VA: `0x0000000140858240`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A868`
- 디코드: `688`개 명령, `3,100/3,100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **36**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008582E7` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x008582F4` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x008582F9` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0085834A` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00858369` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x008583CD` → [CmpQueryKeyDataFromCache](CmpQueryKeyDataFromCache_function_00858F70.md) (function, `0x00858F70`)
- `0x00858476` → [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) (function, `0x00AB8284`)
- `0x008584D9` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00858518` → [CmpQueryKeyDataFromNode](../84/CmpQueryKeyDataFromNode_function_0084EAE0.md) (function, `0x0084EAE0`)
- `0x00858538` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00858548` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00858590` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008585F3` → [PsGetCurrentThreadProcess](../../text/47/PsGetCurrentThreadProcess_function_0047C7E0.md) (function, `0x0047C7E0`)
- `0x00858606` → [SeCaptureSubjectContextEx](../8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x00858651` → [CmpIsKcbInsideVirtualizedHive](../8B/CmpIsKcbInsideVirtualizedHive_function_008B4E70.md) (function, `0x008B4E70`)
- `0x00858679` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x00858776` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00858780` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008587A5` → [CmGetKeyFlags](../AA/CmGetKeyFlags_function_00AA23A4.md) (function, `0x00AA23A4`)
- `0x008588D8` → [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) (function, `0x00AB8284`)
- `0x0085893A` → [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) (function, `0x00A7D650`)
- `0x00858993` → [CmpQueryKeyData](CmpQueryKeyData_function_00858E70.md) (function, `0x00858E70`)
- `0x00858A62` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00858A9E` → [CmpConstructName](CmpConstructName_function_00856BE0.md) (function, `0x00856BE0`)
- `0x00858B0B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00858B6B` → [CmVirtualKCBToRealPath](../A7/CmVirtualKCBToRealPath_function_00A76BE8.md) (function, `0x00A76BE8`)
- `0x00858BE6` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00858BF5` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00858BFA` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00858C07` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00858C2B` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x00858C3E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00858C57` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00858C61` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00858C6B` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00858C7B` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00858CD0` → [CmpTransReferenceTransaction](../87/CmpTransReferenceTransaction_function_00873434.md) (function, `0x00873434`)
- `0x00858D16` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00858D7E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00858D83` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00858D90` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00858DBD` → [CmQueryLayeredKey](../../text/46/CmQueryLayeredKey_function_0046A930.md) (function, `0x0046A930`)
- `0x00858DC4` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00858DD1` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00858DF4` → [CmpTransSearchAddTrans](../87/CmpTransSearchAddTrans_function_008743FC.md) (function, `0x008743FC`)
- `0x00858E3A` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x00858E4B` → [CmpLockTwoKcbsShared](../84/CmpLockTwoKcbsShared_function_008485B4.md) (function, `0x008485B4`)

### Direct callers
- [NtQueryKey](../86/NtQueryKey_function_008676E0.md) at `0x00867CC1`

### Static image references
- `0x00858259` → RVA `0x00E0A740` (`.data`; read)
- `0x008583F1` → RVA `0x00E0ECA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x008582E7` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x008582F4` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008582F9` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0085834A` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00858369` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00858548` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x008585F3` → [PsGetCurrentThreadProcess](../../text/47/PsGetCurrentThreadProcess_function_0047C7E0.md) (`PAGE` → `.text`)
  - `0x00858A62` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00858B0B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00858BE6` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00858BF5` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00858BFA` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00858C07` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00858C2B` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x00858C3E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00858C57` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00858C61` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00858C6B` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00858C7B` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00858D16` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00858D7E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00858D83` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00858D90` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00858DBD` → [CmQueryLayeredKey](../../text/46/CmQueryLayeredKey_function_0046A930.md) (`PAGE` → `.text`)
  - `0x00858DC4` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00858DD1` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00858240  4C 8B DC                        mov r11, rsp
00858243  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
00858247  53                              push rbx
00858248  56                              push rsi
00858249  57                              push rdi
0085824A  41 54                           push r12
0085824C  41 55                           push r13
0085824E  41 56                           push r14
00858250  41 57                           push r15
00858252  48 81 EC 50 01 00 00            sub rsp, 0x150
00858259  48 8B 05 E0 24 5B 00            mov rax, qword ptr [rip + 0x5b24e0]
00858260  48 33 C4                        xor rax, rsp
00858263  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
0085826B  4D 8B F1                        mov r14, r9
0085826E  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
00858273  45 8B F8                        mov r15d, r8d
00858276  48 8B DA                        mov rbx, rdx
00858279  48 8B F1                        mov rsi, rcx
0085827C  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00858284  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
0085828C  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00858291  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00858299  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
008582A1  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008582A6  45 33 E4                        xor r12d, r12d
008582A9  4D 89 A3 00 FF FF FF            mov qword ptr [r11 - 0x100], r12
008582B0  45 8B EC                        mov r13d, r12d
008582B3  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
008582BB  0F 57 C0                        xorps xmm0, xmm0
008582BE  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008582C6  0F 57 C9                        xorps xmm1, xmm1
008582C9  41 0F 11 4B 88                  movups xmmword ptr [r11 - 0x78], xmm1
008582CE  41 0F 11 4B 98                  movups xmmword ptr [r11 - 0x68], xmm1
008582D3  41 0F 11 4B A8                  movups xmmword ptr [r11 - 0x58], xmm1
008582D8  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008582E0  49 8D 8B 38 FF FF FF            lea rcx, [r11 - 0xc8]
008582E7  E8 04 25 BD FF                  call 0x14042a7f0
008582EC  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
008582F4  E8 E7 15 37 00                  call 0x140bc98e0
008582F9  E8 36 18 37 00                  call 0x140bc9b34
008582FE  48 8B 7E 08                     mov rdi, qword ptr [rsi + 8]
00858302  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
0085830A  66 44 39 67 42                  cmp word ptr [rdi + 0x42], r12w
0085830F  0F 85 8D 0A 00 00               jne 0x140858da2
00858315  4C 39 66 38                     cmp qword ptr [rsi + 0x38], r12
00858319  0F 85 3F 09 00 00               jne 0x140858c5e
0085831F  4C 39 66 40                     cmp qword ptr [rsi + 0x40], r12
00858323  0F 85 35 09 00 00               jne 0x140858c5e
00858329  48 85 DB                        test rbx, rbx
0085832C  74 0C                           je 0x14085833a
0085832E  48 8B 7B 08                     mov rdi, qword ptr [rbx + 8]
00858332  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
0085833A  48 8B C6                        mov rax, rsi
0085833D  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00858341  48 85 DB                        test rbx, rbx
00858344  0F 85 FA 0A 00 00               jne 0x140858e44
0085834A  E8 CD 16 37 00                  call 0x140bc9a1c
0085834F  90                              nop
00858350  41 83 FF 03                     cmp r15d, 3
00858354  0F 84 FE 06 00 00               je 0x140858a58
0085835A  48 85 DB                        test rbx, rbx
0085835D  0F 85 DF 01 00 00               jne 0x140858542
00858363  49 8B D5                        mov rdx, r13
00858366  48 8B CE                        mov rcx, rsi
00858369  E8 12 11 37 00                  call 0x140bc9480
0085836E  84 C0                           test al, al
00858370  0F 85 DF 01 00 00               jne 0x140858555
00858376  41 83 FF 05                     cmp r15d, 5
0085837A  0F 84 0A 04 00 00               je 0x14085878a
00858380  41 83 FF 06                     cmp r15d, 6
00858384  0F 84 4D 02 00 00               je 0x1408585d7
0085838A  41 83 FF 08                     cmp r15d, 8
0085838E  0F 84 06 02 00 00               je 0x14085859a
00858394  C7 44 24 68 FF FF FF FF         mov dword ptr [rsp + 0x68], 0xffffffff
0085839C  44 89 64 24 6C                  mov dword ptr [rsp + 0x6c], r12d
008583A1  41 83 FF 04                     cmp r15d, 4
008583A5  0F 85 15 01 00 00               jne 0x1408584c0
008583AB  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008583B0  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
008583B5  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
008583BA  44 8B 8C 24 B0 01 00 00         mov r9d, dword ptr [rsp + 0x1b0]
008583C2  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
008583C7  41 8B D7                        mov edx, r15d
008583CA  48 8B CF                        mov rcx, rdi
008583CD  E8 9E 0B 00 00                  call 0x140858f70
008583D2  44 8B F0                        mov r14d, eax
008583D5  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
008583DA  45 85 F6                        test r14d, r14d
008583DD  0F 88 EE 07 00 00               js 0x140858bd1
008583E3  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008583E8  48 85 DB                        test rbx, rbx
008583EB  0F 85 4E 04 00 00               jne 0x14085883f
008583F1  38 1D A9 68 5B 00               cmp byte ptr [rip + 0x5b68a9], bl
008583F7  0F 84 D4 07 00 00               je 0x140858bd1
008583FD  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00858401  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00858407  0F BA E0 18                     bt eax, 0x18
0085840B  0F 83 C0 07 00 00               jae 0x140858bd1
00858411  41 8D 47 FE                     lea eax, [r15 - 2]
00858415  A9 FD FF FF FF                  test eax, 0xfffffffd
0085841A  0F 85 B1 07 00 00               jne 0x140858bd1
00858420  44 89 A4 24 80 00 00 00         mov dword ptr [rsp + 0x80], r12d
00858428  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
00858430  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
00858435  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0085843D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00858442  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00858447  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0085844C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00858451  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00858459  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085845E  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00858466  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085846B  4D 8B CD                        mov r9, r13
0085846E  33 D2                           xor edx, edx
00858470  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00858476  E8 09 FE 25 00                  call 0x140ab8284
0085847B  44 8B F0                        mov r14d, eax
0085847E  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858482  3D 1A 00 00 80                  cmp eax, 0x8000001a
00858487  0F 85 44 07 00 00               jne 0x140858bd1
0085848D  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00858494  41 83 FF 02                     cmp r15d, 2
00858498  75 05                           jne 0x14085849f
0085849A  89 47 14                        mov dword ptr [rdi + 0x14], eax
0085849D  EB 03                           jmp 0x1408584a2
0085849F  89 47 0C                        mov dword ptr [rdi + 0xc], eax
008584A2  45 8B F4                        mov r14d, r12d
008584A5  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
008584AA  E9 22 07 00 00                  jmp 0x140858bd1
008584AF  44 8B F0                        mov r14d, eax
008584B2  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008584B6  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
008584BB  E9 11 07 00 00                  jmp 0x140858bd1
008584C0  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
008584C3  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008584C7  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
008584CC  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008584D3  0F 84 B7 00 00 00               je 0x140858590
008584D9  E8 82 C7 FF FF                  call 0x140854c60
008584DE  48 8B C8                        mov rcx, rax
008584E1  48 85 C0                        test rax, rax
008584E4  0F 84 DC 06 00 00               je 0x140858bc6
008584EA  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
008584EF  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008584F4  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
008584F9  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
008584FE  8B 84 24 B0 01 00 00            mov eax, dword ptr [rsp + 0x1b0]
00858505  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00858509  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
0085850E  45 8B C7                        mov r8d, r15d
00858511  48 8B D1                        mov rdx, rcx
00858514  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00858518  E8 C3 65 FF FF                  call 0x14084eae0
0085851D  44 8B F0                        mov r14d, eax
00858520  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00858524  0F B6 81 8C 00 00 00            movzx eax, byte ptr [rcx + 0x8c]
0085852B  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00858530  A8 01                           test al, 1
00858532  0F 85 48 02 00 00               jne 0x140858780
00858538  E8 03 DA FF FF                  call 0x140855f40
0085853D  E9 93 FE FF FF                  jmp 0x1408583d5
00858542  49 8B D5                        mov rdx, r13
00858545  48 8B CB                        mov rcx, rbx
00858548  E8 33 0F 37 00                  call 0x140bc9480
0085854D  84 C0                           test al, al
0085854F  0F 84 0E FE FF FF               je 0x140858363
00858555  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00858558  A8 01                           test al, 1
0085855A  75 1C                           jne 0x140858578
0085855C  B8 7C 01 00 C0                  mov eax, 0xc000017c
00858561  44 8B F0                        mov r14d, eax
00858564  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858568  E9 64 06 00 00                  jmp 0x140858bd1
0085856D  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00858570  A8 01                           test al, 1
00858572  0F 84 D2 04 00 00               je 0x140858a4a
00858578  41 BE 25 04 00 C0               mov r14d, 0xc0000425
0085857E  EB 06                           jmp 0x140858586
00858580  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
00858586  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
0085858B  E9 41 06 00 00                  jmp 0x140858bd1
00858590  E8 1B C7 FF FF                  call 0x140854cb0
00858595  E9 44 FF FF FF                  jmp 0x1408584de
0085859A  41 BE 04 00 00 00               mov r14d, 4
008585A0  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
008585A5  44 89 32                        mov dword ptr [rdx], r14d
008585A8  44 39 B4 24 B0 01 00 00         cmp dword ptr [rsp + 0x1b0], r14d
008585B0  0F 82 84 04 00 00               jb 0x140858a3a
008585B6  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
008585BA  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008585BF  8B 0F                           mov ecx, dword ptr [rdi]
008585C1  8B 80 10 10 00 00               mov eax, dword ptr [rax + 0x1010]
008585C7  A8 01                           test al, 1
008585C9  0F 85 59 04 00 00               jne 0x140858a28
008585CF  83 C9 01                        or ecx, 1
008585D2  E9 54 04 00 00                  jmp 0x140858a2b
008585D7  0F 57 C0                        xorps xmm0, xmm0
008585DA  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
008585E2  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
008585EA  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
008585F3  E8 E8 41 C2 FF                  call 0x14047c7e0
008585F8  48 8B D0                        mov rdx, rax
008585FB  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
00858603  48 8B CF                        mov rcx, rdi
00858606  E8 85 C6 06 00                  call 0x1408c4c90
0085860B  90                              nop
0085860C  41 BE 04 00 00 00               mov r14d, 4
00858612  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00858617  44 89 32                        mov dword ptr [rdx], r14d
0085861A  44 39 B4 24 B0 01 00 00         cmp dword ptr [rsp + 0x1b0], r14d
00858622  0F 82 FA 00 00 00               jb 0x140858722
00858628  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
00858630  80 3D 69 66 5B 00 00            cmp byte ptr [rip + 0x5b6669], 0
00858637  0F 84 DD 00 00 00               je 0x14085871a
0085863D  41 F7 80 B8 00 00 00 00 00 00 02  test dword ptr [r8 + 0xb8], 0x2000000
00858648  0F 85 CC 00 00 00               jne 0x14085871a
0085864E  49 8B C8                        mov rcx, r8
00858651  E8 1A C8 05 00                  call 0x1408b4e70
00858656  84 C0                           test al, al
00858658  0F 84 BC 00 00 00               je 0x14085871a
0085865E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00858667  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
0085866E  45 33 C0                        xor r8d, r8d
00858671  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00858679  E8 12 C8 05 00                  call 0x1408b4e90
0085867E  84 C0                           test al, al
00858680  41 0F 94 C2                     sete r10b
00858684  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
0085868C  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00858691  8B 0A                           mov ecx, dword ptr [rdx]
00858693  83 E1 FE                        and ecx, 0xfffffffe
00858696  41 0F B6 C2                     movzx eax, r10b
0085869A  0B C8                           or ecx, eax
0085869C  89 0A                           mov dword ptr [rdx], ecx
0085869E  83 E1 FD                        and ecx, 0xfffffffd
008586A1  89 0A                           mov dword ptr [rdx], ecx
008586A3  44 8B C9                        mov r9d, ecx
008586A6  45 84 D2                        test r10b, r10b
008586A9  74 18                           je 0x1408586c3
008586AB  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
008586B2  A8 20                           test al, 0x20
008586B4  75 79                           jne 0x14085872f
008586B6  B0 01                           mov al, 1
008586B8  84 C0                           test al, al
008586BA  74 07                           je 0x1408586c3
008586BC  41 83 C9 02                     or r9d, 2
008586C0  44 89 0A                        mov dword ptr [rdx], r9d
008586C3  80 3D D6 65 5B 00 00            cmp byte ptr [rip + 0x5b65d6], 0
008586CA  74 0D                           je 0x1408586d9
008586CC  41 F7 80 B8 00 00 00 00 00 00 01  test dword ptr [r8 + 0xb8], 0x1000000
008586D7  75 03                           jne 0x1408586dc
008586D9  45 8B F4                        mov r14d, r12d
008586DC  41 83 E1 FB                     and r9d, 0xfffffffb
008586E0  45 0B CE                        or r9d, r14d
008586E3  44 89 0A                        mov dword ptr [rdx], r9d
008586E6  41 8B 88 B8 00 00 00            mov ecx, dword ptr [r8 + 0xb8]
008586ED  C1 E9 16                        shr ecx, 0x16
008586F0  83 E1 08                        and ecx, 8
008586F3  41 83 E1 F7                     and r9d, 0xfffffff7
008586F7  41 0B C9                        or ecx, r9d
008586FA  89 0A                           mov dword ptr [rdx], ecx
008586FC  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00858703  C1 E8 13                        shr eax, 0x13
00858706  83 E0 10                        and eax, 0x10
00858709  83 E1 EF                        and ecx, 0xffffffef
0085870C  0B C1                           or eax, ecx
0085870E  89 02                           mov dword ptr [rdx], eax
00858710  45 8B F4                        mov r14d, r12d
00858713  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00858718  EB 19                           jmp 0x140858733
0085871A  45 32 D2                        xor r10b, r10b
0085871D  E9 6A FF FF FF                  jmp 0x14085868c
00858722  41 BE 23 00 00 C0               mov r14d, 0xc0000023
00858728  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
0085872D  EB 04                           jmp 0x140858733
0085872F  32 C0                           xor al, al
00858731  EB 85                           jmp 0x1408586b8
00858733  EB 39                           jmp 0x14085876e
00858735  44 8B F0                        mov r14d, eax
00858738  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0085873C  45 33 E4                        xor r12d, r12d
0085873F  44 8B BC 24 A0 01 00 00         mov r15d, dword ptr [rsp + 0x1a0]
00858747  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
0085874F  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00858757  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0085875C  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00858764  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00858769  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0085876E  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00858776  E8 95 2F 01 00                  call 0x14086b710
0085877B  E9 5A FC FF FF                  jmp 0x1408583da
00858780  E8 9B 44 00 00                  call 0x14085cc20
00858785  E9 4B FC FF FF                  jmp 0x1408583d5
0085878A  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0085878F  C7 00 0C 00 00 00               mov dword ptr [rax], 0xc
00858795  83 BC 24 B0 01 00 00 0C         cmp dword ptr [rsp + 0x1b0], 0xc
0085879D  72 52                           jb 0x1408587f1
0085879F  49 8B D5                        mov rdx, r13
008587A2  48 8B CF                        mov rcx, rdi
008587A5  E8 FA 9B 24 00                  call 0x140aa23a4
008587AA  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
008587AF  89 02                           mov dword ptr [rdx], eax
008587B1  44 89 62 04                     mov dword ptr [rdx + 4], r12d
008587B5  41 8B CC                        mov ecx, r12d
008587B8  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
008587BC  7D 08                           jge 0x1408587c6
008587BE  B9 01 00 00 00                  mov ecx, 1
008587C3  89 4A 04                        mov dword ptr [rdx + 4], ecx
008587C6  F7 87 B8 00 00 00 00 00 10 00   test dword ptr [rdi + 0xb8], 0x100000
008587D0  74 06                           je 0x1408587d8
008587D2  83 C9 02                        or ecx, 2
008587D5  89 4A 04                        mov dword ptr [rdx + 4], ecx
008587D8  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
008587DE  C1 E8 04                        shr eax, 4
008587E1  83 E0 0F                        and eax, 0xf
008587E4  89 42 08                        mov dword ptr [rdx + 8], eax
008587E7  45 8B F4                        mov r14d, r12d
008587EA  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
008587EF  EB 0B                           jmp 0x1408587fc
008587F1  41 BE 23 00 00 C0               mov r14d, 0xc0000023
008587F7  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
008587FC  E9 D9 FB FF FF                  jmp 0x1408583da
00858801  44 8B F0                        mov r14d, eax
00858804  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858808  45 33 E4                        xor r12d, r12d
0085880B  44 8B BC 24 A0 01 00 00         mov r15d, dword ptr [rsp + 0x1a0]
00858813  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
0085881B  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00858823  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00858828  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00858830  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00858835  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0085883A  E9 9B FB FF FF                  jmp 0x1408583da
0085883F  41 8D 47 FD                     lea eax, [r15 - 3]
00858843  A9 FC FF FF FF                  test eax, 0xfffffffc
00858848  0F 85 37 03 00 00               jne 0x140858b85
0085884E  41 83 FF 04                     cmp r15d, 4
00858852  0F 84 2D 03 00 00               je 0x140858b85
00858858  41 8D 47 FE                     lea eax, [r15 - 2]
0085885C  A9 FD FF FF FF                  test eax, 0xfffffffd
00858861  0F 85 6A 03 00 00               jne 0x140858bd1
00858867  44 89 64 24 70                  mov dword ptr [rsp + 0x70], r12d
0085886C  4C 89 A4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r12
00858874  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00858879  0F 57 C0                        xorps xmm0, xmm0
0085887C  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00858884  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
0085888C  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
00858894  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00858899  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0085889E  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
008588A3  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008588A8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008588AD  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008588B5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008588BA  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
008588C2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008588C7  4D 8B CD                        mov r9, r13
008588CA  41 B8 FF FF FF FF               mov r8d, 0xffffffff
008588D0  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
008588D4  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008588D8  E8 A7 F9 25 00                  call 0x140ab8284
008588DD  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008588E1  3D 1A 00 00 80                  cmp eax, 0x8000001a
008588E6  75 25                           jne 0x14085890d
008588E8  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008588EC  41 83 FF 02                     cmp r15d, 2
008588F0  75 05                           jne 0x1408588f7
008588F2  89 47 14                        mov dword ptr [rdi + 0x14], eax
008588F5  EB 03                           jmp 0x1408588fa
008588F7  89 47 0C                        mov dword ptr [rdi + 0xc], eax
008588FA  EB 11                           jmp 0x14085890d
008588FC  44 8B F0                        mov r14d, eax
008588FF  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858903  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00858908  E9 C4 02 00 00                  jmp 0x140858bd1
0085890D  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00858912  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00858917  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0085891C  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00858921  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00858926  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0085892B  41 B9 FF FF FF FF               mov r9d, 0xffffffff
00858931  41 B0 01                        mov r8b, 1
00858934  48 8B D3                        mov rdx, rbx
00858937  48 8B CE                        mov rcx, rsi
0085893A  E8 11 4D 22 00                  call 0x140a7d650
0085893F  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858943  3D 1A 00 00 80                  cmp eax, 0x8000001a
00858948  75 25                           jne 0x14085896f
0085894A  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0085894E  41 83 FF 02                     cmp r15d, 2
00858952  75 05                           jne 0x140858959
00858954  89 47 20                        mov dword ptr [rdi + 0x20], eax
00858957  EB 03                           jmp 0x14085895c
00858959  89 47 14                        mov dword ptr [rdi + 0x14], eax
0085895C  EB 11                           jmp 0x14085896f
0085895E  44 8B F0                        mov r14d, eax
00858961  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858965  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0085896A  E9 62 02 00 00                  jmp 0x140858bd1
0085896F  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00858974  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00858979  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085897E  41 B9 30 00 00 00               mov r9d, 0x30
00858984  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
0085898C  41 8B D7                        mov edx, r15d
0085898F  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00858993  E8 D8 04 00 00                  call 0x140858e70
00858998  44 8B F0                        mov r14d, eax
0085899B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0085899F  B8 00 00 00 80                  mov eax, 0x80000000
008589A4  41 8D 0C 06                     lea ecx, [r14 + rax]
008589A8  85 C8                           test eax, ecx
008589AA  0F 84 07 02 00 00               je 0x140858bb7
008589B0  41 83 FF 02                     cmp r15d, 2
008589B4  75 2F                           jne 0x1408589e5
008589B6  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
008589BD  3B 47 18                        cmp eax, dword ptr [rdi + 0x18]
008589C0  76 03                           jbe 0x1408589c5
008589C2  89 47 18                        mov dword ptr [rdi + 0x18], eax
008589C5  8B 84 24 04 01 00 00            mov eax, dword ptr [rsp + 0x104]
008589CC  3B 47 24                        cmp eax, dword ptr [rdi + 0x24]
008589CF  76 03                           jbe 0x1408589d4
008589D1  89 47 24                        mov dword ptr [rdi + 0x24], eax
008589D4  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
008589DB  3B 47 28                        cmp eax, dword ptr [rdi + 0x28]
008589DE  76 32                           jbe 0x140858a12
008589E0  89 47 28                        mov dword ptr [rdi + 0x28], eax
008589E3  EB 2D                           jmp 0x140858a12
008589E5  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
008589EC  3B 47 10                        cmp eax, dword ptr [rdi + 0x10]
008589EF  76 03                           jbe 0x1408589f4
008589F1  89 47 10                        mov dword ptr [rdi + 0x10], eax
008589F4  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
008589FB  3B 47 18                        cmp eax, dword ptr [rdi + 0x18]
008589FE  76 03                           jbe 0x140858a03
00858A00  89 47 18                        mov dword ptr [rdi + 0x18], eax
00858A03  8B 84 24 FC 00 00 00            mov eax, dword ptr [rsp + 0xfc]
00858A0A  3B 47 1C                        cmp eax, dword ptr [rdi + 0x1c]
00858A0D  76 03                           jbe 0x140858a12
00858A0F  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
00858A12  E9 BA 01 00 00                  jmp 0x140858bd1
00858A17  44 8B F0                        mov r14d, eax
00858A1A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858A1E  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00858A23  E9 A9 01 00 00                  jmp 0x140858bd1
00858A28  83 E1 FE                        and ecx, 0xfffffffe
00858A2B  89 0F                           mov dword ptr [rdi], ecx
00858A2D  45 8B F4                        mov r14d, r12d
00858A30  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00858A35  E9 AE F9 FF FF                  jmp 0x1408583e8
00858A3A  41 BE 23 00 00 C0               mov r14d, 0xc0000023
00858A40  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00858A45  E9 87 01 00 00                  jmp 0x140858bd1
00858A4A  B8 7C 01 00 C0                  mov eax, 0xc000017c
00858A4F  44 8B F0                        mov r14d, eax
00858A52  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858A56  EB 1F                           jmp 0x140858a77
00858A58  48 8B 7E 08                     mov rdi, qword ptr [rsi + 8]
00858A5C  49 8B D5                        mov rdx, r13
00858A5F  48 8B CE                        mov rcx, rsi
00858A62  E8 19 0A 37 00                  call 0x140bc9480
00858A67  84 C0                           test al, al
00858A69  0F 85 FE FA FF FF               jne 0x14085856d
00858A6F  45 8B F4                        mov r14d, r12d
00858A72  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00858A77  48 83 7F 50 00                  cmp qword ptr [rdi + 0x50], 0
00858A7C  0F 84 FE FA FF FF               je 0x140858580
00858A82  80 3D 17 62 5B 00 00            cmp byte ptr [rip + 0x5b6217], 0
00858A89  74 10                           je 0x140858a9b
00858A8B  F7 87 B8 00 00 00 00 00 00 01   test dword ptr [rdi + 0xb8], 0x1000000
00858A95  0F 85 C5 00 00 00               jne 0x140858b60
00858A9B  48 8B CF                        mov rcx, rdi
00858A9E  E8 3D E1 FF FF                  call 0x140856be0
00858AA3  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00858AAB  48 83 BC 24 88 00 00 00 00      cmp qword ptr [rsp + 0x88], 0
00858AB4  0F 84 C6 FA FF FF               je 0x140858580
00858ABA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00858AC2  0F B7 08                        movzx ecx, word ptr [rax]
00858AC5  8B C1                           mov eax, ecx
00858AC7  83 C1 04                        add ecx, 4
00858ACA  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00858ACF  89 0A                           mov dword ptr [rdx], ecx
00858AD1  8B 8C 24 B0 01 00 00            mov ecx, dword ptr [rsp + 0x1b0]
00858AD8  83 F9 04                        cmp ecx, 4
00858ADB  72 35                           jb 0x140858b12
00858ADD  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00858AE2  89 07                           mov dword ptr [rdi], eax
00858AE4  83 C1 FC                        add ecx, -4
00858AE7  3B C8                           cmp ecx, eax
00858AE9  73 0D                           jae 0x140858af8
00858AEB  8B C1                           mov eax, ecx
00858AED  41 BE 05 00 00 80               mov r14d, 0x80000005
00858AF3  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00858AF8  44 8B C0                        mov r8d, eax
00858AFB  48 8D 4F 04                     lea rcx, [rdi + 4]
00858AFF  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00858B07  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00858B0B  E8 30 DD E6 FF                  call 0x1406c6840
00858B10  EB 0B                           jmp 0x140858b1d
00858B12  41 BE 23 00 00 C0               mov r14d, 0xc0000023
00858B18  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00858B1D  E9 B8 F8 FF FF                  jmp 0x1408583da
00858B22  44 8B F0                        mov r14d, eax
00858B25  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858B29  45 33 E4                        xor r12d, r12d
00858B2C  44 8B BC 24 A0 01 00 00         mov r15d, dword ptr [rsp + 0x1a0]
00858B34  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
00858B3C  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00858B44  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00858B49  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00858B51  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00858B56  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00858B5B  E9 7A F8 FF FF                  jmp 0x1408583da
00858B60  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
00858B68  48 8B CF                        mov rcx, rdi
00858B6B  E8 78 E0 21 00                  call 0x140a76be8
00858B70  85 C0                           test eax, eax
00858B72  0F 88 33 FF FF FF               js 0x140858aab
00858B78  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
00858B80  E9 1E FF FF FF                  jmp 0x140858aa3
00858B85  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00858B89  48 8B 88 A8 00 00 00            mov rcx, qword ptr [rax + 0xa8]
00858B90  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00858B94  48 39 88 A8 00 00 00            cmp qword ptr [rax + 0xa8], rcx
00858B9B  0F 8D B7 FC FF FF               jge 0x140858858
00858BA1  48 89 0F                        mov qword ptr [rdi], rcx
00858BA4  E9 AF FC FF FF                  jmp 0x140858858
00858BA9  44 8B F0                        mov r14d, eax
00858BAC  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00858BB0  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00858BB5  EB 1A                           jmp 0x140858bd1
00858BB7  41 81 FE 05 00 00 80            cmp r14d, 0x80000005
00858BBE  0F 84 EC FD FF FF               je 0x1408589b0
00858BC4  EB 0B                           jmp 0x140858bd1
00858BC6  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
00858BCC  E9 04 F8 FF FF                  jmp 0x1408583d5
00858BD1  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00858BD9  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00858BDD  48 85 DB                        test rbx, rbx
00858BE0  0F 85 4D 02 00 00               jne 0x140858e33
00858BE6  E8 D5 06 37 00                  call 0x140bc92c0
00858BEB  33 D2                           xor edx, edx
00858BED  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00858BF5  E8 A6 2D BC FF                  call 0x14041b9a0
00858BFA  E8 85 0E 37 00                  call 0x140bc9a84
00858BFF  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00858C07  E8 14 0D 37 00                  call 0x140bc9920
00858C0C  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00858C14  48 85 C9                        test rcx, rcx
00858C17  75 3E                           jne 0x140858c57
00858C19  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00858C21  48 85 C9                        test rcx, rcx
00858C24  74 0A                           je 0x140858c30
00858C26  BA 43 4D 4E 62                  mov edx, 0x624e4d43
00858C2B  E8 B0 FD BE FF                  call 0x1404489e0
00858C30  41 8B C6                        mov eax, r14d
00858C33  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00858C3B  48 33 CC                        xor rcx, rsp
00858C3E  E8 FD 39 E5 FF                  call 0x1406ac640
00858C43  48 81 C4 50 01 00 00            add rsp, 0x150
00858C4A  41 5F                           pop r15
00858C4C  41 5E                           pop r14
00858C4E  41 5D                           pop r13
00858C50  41 5C                           pop r12
00858C52  5F                              pop rdi
00858C53  5E                              pop rsi
00858C54  5B                              pop rbx
00858C55  C3                              ret
00858C56  CC                              int3
00858C57  E8 F4 9B 32 00                  call 0x140b82850
00858C5C  EB D2                           jmp 0x140858c30
00858C5E  48 8B CF                        mov rcx, rdi
00858C61  E8 B6 0D 37 00                  call 0x140bc9a1c
00858C66  33 D2                           xor edx, edx
00858C68  48 8B CE                        mov rcx, rsi
00858C6B  E8 10 08 37 00                  call 0x140bc9480
00858C70  84 C0                           test al, al
00858C72  0F 85 E5 00 00 00               jne 0x140858d5d
00858C78  48 8B CF                        mov rcx, rdi
00858C7B  E8 40 06 37 00                  call 0x140bc92c0
00858C80  49 8B C4                        mov rax, r12
00858C83  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00858C8B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00858C90  4C 8B 46 38                     mov r8, qword ptr [rsi + 0x38]
00858C94  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
00858C99  4D 85 C0                        test r8, r8
00858C9C  0F 84 7C 01 00 00               je 0x140858e1e
00858CA2  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00858CA6  48 8B D1                        mov rdx, rcx
00858CA9  48 83 F2 01                     xor rdx, 1
00858CAD  F6 C1 01                        test cl, 1
00858CB0  48 0F 44 D1                     cmove rdx, rcx
00858CB4  41 F6 C0 01                     test r8b, 1
00858CB8  0F 84 83 00 00 00               je 0x140858d41
00858CBE  49 8B C0                        mov rax, r8
00858CC1  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00858CC5  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00858CCD  49 8B C8                        mov rcx, r8
00858CD0  E8 5F A7 01 00                  call 0x140873434
00858CD5  44 8B F0                        mov r14d, eax
00858CD8  85 C0                           test eax, eax
00858CDA  0F 88 BA 00 00 00               js 0x140858d9a
00858CE0  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00858CE8  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00858CEC  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00858CF4  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
00858CFC  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00858D01  48 85 C0                        test rax, rax
00858D04  0F 84 FC 00 00 00               je 0x140858e06
00858D0A  45 8B F4                        mov r14d, r12d
00858D0D  48 85 C9                        test rcx, rcx
00858D10  74 09                           je 0x140858d1b
00858D12  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00858D16  E8 35 06 AA FF                  call 0x1402f9350
00858D1B  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00858D23  45 85 F6                        test r14d, r14d
00858D26  78 5B                           js 0x140858d83
00858D28  4C 8B E8                        mov r13, rax
00858D2B  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00858D33  45 8B F4                        mov r14d, r12d
00858D36  45 85 F6                        test r14d, r14d
00858D39  0F 89 EA F5 FF FF               jns 0x140858329
00858D3F  EB 42                           jmp 0x140858d83
00858D41  4C 8B 4A 20                     mov r9, qword ptr [rdx + 0x20]
00858D45  4D 8B 81 38 10 00 00            mov r8, qword ptr [r9 + 0x1038]
00858D4C  4D 85 C0                        test r8, r8
00858D4F  0F 85 88 00 00 00               jne 0x140858ddd
00858D55  41 BE 05 00 19 C0               mov r14d, 0xc0190005
00858D5B  EB D9                           jmp 0x140858d36
00858D5D  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00858D60  A8 01                           test al, 1
00858D62  0F 84 ED 00 00 00               je 0x140858e55
00858D68  B1 01                           mov cl, 1
00858D6A  B8 7C 01 00 C0                  mov eax, 0xc000017c
00858D6F  41 BE 25 04 00 C0               mov r14d, 0xc0000425
00858D75  84 C9                           test cl, cl
00858D77  44 0F 44 F0                     cmove r14d, eax
00858D7B  48 8B CF                        mov rcx, rdi
00858D7E  E8 3D 05 37 00                  call 0x140bc92c0
00858D83  E8 FC 0C 37 00                  call 0x140bc9a84
00858D88  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00858D90  E8 8B 0B 37 00                  call 0x140bc9920
00858D95  E9 96 FE FF FF                  jmp 0x140858c30
00858D9A  49 8B CC                        mov rcx, r12
00858D9D  E9 6B FF FF FF                  jmp 0x140858d0d
00858DA2  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00858DA7  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00858DAC  44 8B 8C 24 B0 01 00 00         mov r9d, dword ptr [rsp + 0x1b0]
00858DB4  4D 8B C6                        mov r8, r14
00858DB7  41 8B D7                        mov edx, r15d
00858DBA  48 8B CE                        mov rcx, rsi
00858DBD  E8 6E 1B C1 FF                  call 0x14046a930
00858DC2  8B D8                           mov ebx, eax
00858DC4  E8 BB 0C 37 00                  call 0x140bc9a84
00858DC9  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00858DD1  E8 4A 0B 37 00                  call 0x140bc9920
00858DD6  8B C3                           mov eax, ebx
00858DD8  E9 56 FE FF FF                  jmp 0x140858c33
00858DDD  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00858DE2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00858DE7  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00858DEC  48 8B 56 40                     mov rdx, qword ptr [rsi + 0x40]
00858DF0  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
00858DF4  E8 03 B6 01 00                  call 0x1408743fc
00858DF9  44 8B F0                        mov r14d, eax
00858DFC  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00858E01  E9 1D FF FF FF                  jmp 0x140858d23
00858E06  41 BE 02 00 19 C0               mov r14d, 0xc0190002
00858E0C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00858E11  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00858E19  E9 EF FE FF FF                  jmp 0x140858d0d
00858E1E  48 39 46 40                     cmp qword ptr [rsi + 0x40], rax
00858E22  0F 85 7A FE FF FF               jne 0x140858ca2
00858E28  41 BE 02 00 19 C0               mov r14d, 0xc0190002
00858E2E  E9 03 FF FF FF                  jmp 0x140858d36
00858E33  48 8B D1                        mov rdx, rcx
00858E36  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00858E3A  E8 5D F8 FE FF                  call 0x14084869c
00858E3F  E9 A7 FD FF FF                  jmp 0x140858beb
00858E44  48 8B D1                        mov rdx, rcx
00858E47  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00858E4B  E8 64 F7 FE FF                  call 0x1408485b4
00858E50  E9 FB F4 FF FF                  jmp 0x140858350
00858E55  32 C9                           xor cl, cl
00858E57  E9 0E FF FF FF                  jmp 0x140858d6a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmQueryKey(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p110;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;

    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 5973216)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m128 = a4;
    v_stack_mF0 = a1;
    v_stack_mD0 = a1;
    v_stack_m110 = a2;
    v_stack_m108 = a4;
    v_stack_m130 = a6;
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 256) = 0;
    v_stack_mE0 = 0;
    v_stack_mB8 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm1;
    v_stack_mC8 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_rsp - 200, a2, a3, a4);
    result = CmpAttachToRegistryProcess(v_stack_m78, a2, a3, a4);
    result = CmpLockRegistry(v_stack_m78, a2, a3, a4);
    v_stack_mF8 = *(unsigned __int64 *)(a1 + 8);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) goto loc_00858DA2;
    if ((*(unsigned __int64 *)(a1 + 56)) != 0) goto loc_00858C5E;
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_00858C5E;
loc_00858329:
    v_rdi = *(unsigned __int64 *)(a1 + 8);
    if (a2 != 0) {
        v_rdi = *(unsigned __int64 *)(a2 + 8);
        v_stack_mF8 = v_rdi;
    }
    if (a2 != 0) goto loc_00858E44;
    result = CmpLockKcbShared(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
loc_00858350:
    if (((unsigned int)((unsigned int)(a3))) == 3) goto loc_00858A58;
    if (a2 != 0) goto loc_00858542;
loc_00858363:
    result = CmpIsKeyDeletedForKeyBody(a1, 0, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00858555;
    if (((unsigned int)((unsigned int)(a3))) == 5) goto loc_0085878A;
    if (((unsigned int)((unsigned int)(a3))) == 6) goto loc_008585D7;
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_0085859A;
    v_stack_m120 = 0xFFFFFFFFULL;
    v_stack_m11C = 0;
    if (((unsigned int)((unsigned int)(a3))) != 4) goto loc_008584C0;
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_m130;
    result = CmpQueryKeyDataFromCache(v_rdi, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m128, (unsigned int)(a5));
loc_008583D5:
    v_stack_m138 = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_008583DA:
    if (sign_flag) goto loc_00858BD1;
loc_008583E8:
    if (a2 != 0) goto loc_0085883F;
    if ((*(unsigned __int8 *)(v_rip + 5990569)) == ((unsigned __int8)(a2))) goto loc_00858BD1;
    if ((*(unsigned __int8 *)(v_rip + 5990569)) >= ((unsigned __int8)(a2))) goto loc_00858BD1;
    if ((((unsigned int)((unsigned int)(a3) - 2)) & (0xFFFFFFFDULL)) != 0) goto loc_00858BD1;
    v_stack_m108 = 0;
    v_stack_mE8 = 0;
    v_stack_m130 = 0;
    v_stack_m148 = v_stack_m108;
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_m130;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = v_stack_mC8;
    a2 = 0;
    result = CmpFindSubKeyByNumberFromMergedView(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)(0xFFFFFFFFULL), 0);
    v_stack_m138 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0x8000001AULL) goto loc_00858BD1;
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_0085849F;
    *(unsigned int *)(v_stack_m128 + 20) = (unsigned int)((unsigned int)(v_stack_m108));
    goto loc_008584A2;
loc_0085849F:
    *(unsigned int *)(v_stack_m128 + 12) = (unsigned int)((unsigned int)(v_stack_m108));
loc_008584A2:
    v_stack_m138 = 0;
    goto loc_00858BD1;
loc_008584C0:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m128 + 32) + 140)) & (1)) == 0) goto loc_00858590;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m128 + 32), (unsigned int)(*(unsigned int *)(v_stack_m128 + 40)), v_stack_m120, 0);
loc_008584DE:
    if (result == 0) goto loc_00858BC6;
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_m128;
    v_stack_m160 = v_stack_m130;
    v_stack_m168 = (unsigned int)((unsigned int)(a5));
    result = CmpQueryKeyDataFromNode(*(unsigned __int64 *)(v_stack_m128 + 32), result, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m128);
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m128 + 32) + 140))) & (1)) != 0) goto loc_00858780;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m128 + 32), v_stack_m120, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m128);
    goto loc_008583D5;
loc_00858542:
    result = CmpIsKeyDeletedForKeyBody(0, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m128);
    if ((unsigned __int8)(result) == 0) goto loc_00858363;
loc_00858555:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (1)) != 0) goto loc_00858578;
    v_stack_m138 = (unsigned int)((unsigned int)(0xC000017CULL));
    goto loc_00858BD1;
loc_0085856D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (1)) == 0) goto loc_00858A4A;
loc_00858578:
    goto loc_00858586;
loc_00858580:
loc_00858586:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00858BD1;
loc_00858590:
    result = HvpGetCellPaged(0, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m128);
    goto loc_008584DE;
loc_0085859A:
    *(unsigned int *)(v_stack_m130) = 4;
    if (a5 < 4) goto loc_00858A3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m128 + 32) + 4112)))) & (1)) != 0) goto loc_00858A28;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128))) | (1));
    goto loc_00858A2B;
loc_008585D7:
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    result = PsGetCurrentThreadProcess(a1, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m128);
    result = SeCaptureSubjectContextEx(*(unsigned __int64 *)(gs_base + (0 + 392)), result, v_stack_mA8, v_stack_m128);
    *(unsigned int *)(v_stack_m130) = 4;
    if (a5 < 4) goto loc_00858722;
    if ((*(unsigned __int8 *)(v_rip + 5989993)) == 0) goto loc_0085871A;
    if (((*(unsigned int *)(v_stack_mF8 + 184)) & (0x2000000ULL)) != 0) goto loc_0085871A;
    result = CmpIsKcbInsideVirtualizedHive(v_stack_mF8, v_stack_m130, v_stack_mF8, v_stack_m128);
    if ((unsigned __int8)(result) == 0) goto loc_0085871A;
    a3 = 0;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_stack_mA8, a3, v_stack_m128);
    v_r10 = ((unsigned __int8)(result) == 0) ? 1 : 0;
loc_0085868C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128))) & (0xFFFFFFFEULL));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned __int8)(v_r10))));
    *(unsigned int *)(v_stack_m128) = (unsigned int)(a1);
    a1 = (unsigned int)((a1) & (0xFFFFFFFDULL));
    *(unsigned int *)(v_stack_m128) = (unsigned int)(a1);
    if ((unsigned __int8)(v_r10) == 0) goto loc_008586C3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 184)))) & (32)) != 0) goto loc_0085872F;
loc_008586B8:
    if (1 != 0) {
        a4 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (2));
        *(unsigned int *)(v_stack_m128) = (unsigned int)(a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 5989846)) == 0) goto loc_008586D9;
    v_r14 = 4;
    if (((*(unsigned int *)(v_stack_mF8 + 184)) & (0x1000000ULL)) == 0) {
        v_r14 = 0;
    }
    a4 = (unsigned int)((a4) & (0xFFFFFFFBULL));
    a4 = (unsigned int)((a4) | ((unsigned int)(v_r14)));
    *(unsigned int *)(v_stack_m128) = (unsigned int)(a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mF8 + 184))) >> (22));
    a1 = (unsigned int)((a1) & (8));
    a4 = (unsigned int)((a4) & (0xFFFFFFF7ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(a4)));
    *(unsigned int *)(v_stack_m128) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mF8 + 184))) >> (19));
    result = (unsigned int)((result) & (16));
    a1 = (unsigned int)((a1) & (0xFFFFFFEFULL));
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    *(unsigned int *)(v_stack_m128) = (unsigned int)(result);
    v_stack_m138 = 0;
    goto loc_00858733;
loc_0085871A:
    v_r10 = 0;
    goto loc_0085868C;
loc_00858722:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00858733;
loc_0085872F:
    result = 0;
    goto loc_008586B8;
loc_00858733:
    goto loc_0085876E;
loc_0085876E:
    result = SeReleaseSubjectContext(v_stack_mA8, v_stack_m128, v_stack_mF8, a4);
    goto loc_008583DA;
loc_00858780:
    result = HvpReleaseCellFlat(v_stack_mA8, v_stack_m128, v_stack_mF8, a4);
    goto loc_008583D5;
loc_0085878A:
    *(unsigned int *)(v_stack_m130) = 12;
    if (a5 < 12) goto loc_008587F1;
    result = CmGetKeyFlags(*(unsigned __int64 *)(gs_base + (0 + 392)), 0, v_stack_mF8, a4);
    *(unsigned int *)(v_stack_m128) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m128 + 4) = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40)) < 0) {
        a1 = 1;
        *(unsigned int *)(v_stack_m128 + 4) = (unsigned int)(a1);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) & (0x100000ULL)) != 0) {
        a1 = (unsigned int)((a1) | (2));
        *(unsigned int *)(v_stack_m128 + 4) = (unsigned int)(a1);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) >> (4));
    result = (unsigned int)((result) & (15));
    *(unsigned int *)(v_stack_m128 + 8) = (unsigned int)(result);
    v_stack_m138 = 0;
    goto loc_008587FC;
loc_008587F1:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC0000023ULL));
loc_008587FC:
    goto loc_008583DA;
loc_0085883F:
    if ((((unsigned int)((unsigned int)(a3) - 3)) & (0xFFFFFFFCULL)) != 0) goto loc_00858B85;
    if (((unsigned int)((unsigned int)(a3))) == 4) goto loc_00858B85;
loc_00858858:
    if ((((unsigned int)((unsigned int)(a3) - 2)) & (0xFFFFFFFDULL)) != 0) goto loc_00858BD1;
    v_stack_m118 = 0;
    v_stack_mD8 = 0;
    v_stack_m128 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m148 = v_stack_m118;
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_m128;
    v_stack_m160 = v_stack_mD8;
    v_stack_m168 = v_stack_mC8;
    result = CmpFindSubKeyByNumberFromMergedView(*(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(a1 + 8), (unsigned int)(0xFFFFFFFFULL), 0);
    v_stack_m138 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0x8000001AULL) goto loc_0085890D;
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_008588F7;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 20) = (unsigned int)((unsigned int)(v_stack_m118));
    goto loc_008588FA;
loc_008588F7:
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 12) = (unsigned int)((unsigned int)(v_stack_m118));
loc_008588FA:
    goto loc_0085890D;
loc_0085890D:
    v_stack_m148 = v_stack_m118;
    v_stack_m150 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    result = CmEnumerateValueKeyFromMergedView(a1, 0, 1, (unsigned int)(0xFFFFFFFFULL));
    v_stack_m138 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0x8000001AULL) goto loc_0085896F;
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_00858959;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 32) = (unsigned int)((unsigned int)(v_stack_m118));
    goto loc_0085895C;
loc_00858959:
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 20) = (unsigned int)((unsigned int)(v_stack_m118));
loc_0085895C:
    goto loc_0085896F;
loc_0085896F:
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_m130;
    result = CmpQueryKeyData(*(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_mA8, 48);
    v_stack_m138 = (unsigned int)(result);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) == 0) goto loc_00858BB7;
loc_008589B0:
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_008589E5;
    if (((unsigned int)((unsigned int)(v_stack_m90))) >= = (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 24))) {
        *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 24) = (unsigned int)((unsigned int)(v_stack_m90));
    }
    if (((unsigned int)((unsigned int)(v_stack_m84))) >= = (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 36))) {
        *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 36) = (unsigned int)((unsigned int)(v_stack_m84));
    }
    if (((unsigned int)((unsigned int)(v_stack_m80))) <= (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40))) goto loc_00858A12;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40) = (unsigned int)((unsigned int)(v_stack_m80));
    goto loc_00858A12;
loc_008589E5:
    if (((unsigned int)((unsigned int)(v_stack_m98))) >= = (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 16))) {
        *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 16) = (unsigned int)((unsigned int)(v_stack_m98));
    }
    if (((unsigned int)((unsigned int)(v_stack_m90))) >= = (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 24))) {
        *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 24) = (unsigned int)((unsigned int)(v_stack_m90));
    }
    if (((unsigned int)((unsigned int)(v_stack_m8C))) >= = (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 28))) {
        *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 28) = (unsigned int)((unsigned int)(v_stack_m8C));
    }
    goto loc_00858BD1;
loc_00858A28:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1) & (0xFFFFFFFEULL));
loc_00858A2B:
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392))) = (unsigned int)(a1);
    v_stack_m138 = 0;
    goto loc_008583E8;
loc_00858A3A:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00858BD1;
loc_00858A4A:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC000017CULL));
    goto loc_00858A77;
loc_00858A58:
    result = CmpIsKeyDeletedForKeyBody(a1, 0, v_stack_mA8, 48);
    if ((unsigned __int8)(result) != 0) goto loc_0085856D;
    v_stack_m138 = 0;
loc_00858A77:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 80)) == 0) goto loc_00858580;
    if ((*(unsigned __int8 *)(v_rip + 5988887)) == 0) goto loc_00858A9B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)) & (0x1000000ULL)) != 0) goto loc_00858B60;
loc_00858A9B:
    result = CmpConstructName(*(unsigned __int64 *)(a1 + 8), 0, v_stack_mA8, 48);
loc_00858AA3:
    v_stack_m100 = result;
loc_00858AAB:
    if (v_stack_m100 == 0) goto loc_00858580;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m100)) + (4));
    *(unsigned int *)(v_stack_m130) = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(a5))) < 4) goto loc_00858B12;
    *(unsigned int *)(v_stack_m128) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m100))));
    a1 = (unsigned int)(((unsigned int)(a5)) + (-4));
    result = (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m100)));
    v_r14 = 0;
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m100)))))) {
        result = (unsigned int)(a1);
        v_r14 = 0x80000005ULL;
        v_stack_m138 = (unsigned int)(v_r14);
    }
    result = memcpy(v_stack_m128 + 4, *(unsigned __int64 *)(v_stack_m100 + 8), (unsigned int)((unsigned int)(result)), 48);
    goto loc_00858B1D;
loc_00858B12:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC0000023ULL));
loc_00858B1D:
    goto loc_008583DA;
loc_00858B60:
    result = CmVirtualKCBToRealPath(v_stack_m128, v_stack_mB8, (unsigned int)((unsigned int)(result)), 48);
    if (sign_flag) goto loc_00858AAB;
    goto loc_00858AA3;
loc_00858B85:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 168)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 168))) goto loc_00858858;
    *(unsigned __int64 *)(v_stack_m128) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 168);
    goto loc_00858858;
loc_00858BB7:
    if (((unsigned int)((unsigned int)(0xC0000023ULL))) == 0x80000005ULL) goto loc_008589B0;
    goto loc_00858BD1;
loc_00858BC6:
    goto loc_008583D5;
loc_00858BD1:
    if (0 != 0) goto loc_00858E33;
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_mD0 + 8), v_stack_mB8, (unsigned int)((unsigned int)(result)), 48);
loc_00858BEB:
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mC8, a2, (unsigned int)((unsigned int)(result)), 48);
    result = CmpUnlockRegistry(v_stack_mC8, a2, (unsigned int)((unsigned int)(result)), 48);
    result = CmpDetachFromRegistryProcess(v_stack_m78, a2, (unsigned int)((unsigned int)(result)), 48);
    if (v_stack_mB0 != 0) goto loc_00858C57;
    if (v_stack_m100 != 0) {
        a2 = 0x624E4D43ULL;
        result = CmpFreePoolWithTag(v_stack_m100, a2, (unsigned int)((unsigned int)(result)), 48);
    }
loc_00858C33:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(result)), 48);
    v_rsp = (v_rsp) + (336);
    return result;
loc_00858C57:
    result = ExFreePool(a1, a2, (unsigned int)((unsigned int)(result)), 48);
    goto loc_00858C30;
loc_00858C5E:
    result = CmpLockKcbShared(v_stack_m128, a2, (unsigned int)((unsigned int)(result)), 48);
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(a1, a2, (unsigned int)((unsigned int)(result)), 48);
    if ((unsigned __int8)(result) != 0) goto loc_00858D5D;
    result = CmpUnlockKcb(v_stack_m128, a2, (unsigned int)((unsigned int)(result)), 48);
    v_stack_pA0 = 0;
    v_stack_p68 = 0;
    v_stack_p70 = *(unsigned __int64 *)(a1 + 56);
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_00858E1E;
loc_00858CA2:
    a2 = (*(unsigned __int64 *)(a1 + 8)) ^ (1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (1)) == 0) { a2 = *(unsigned __int64 *)(a1 + 8); }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 56))) & (1)) == 0) goto loc_00858D41;
    result = (*(unsigned __int64 *)(a1 + 56)) & (-2);
    v_stack_pB0 = result;
    result = CmpTransReferenceTransaction(*(unsigned __int64 *)(a1 + 56), a2, *(unsigned __int64 *)(a1 + 56), 48);
    if (sign_flag) goto loc_00858D9A;
    v_stack_pA0 = *(unsigned __int64 *)(v_stack_pB0 + 16);
    if (*(unsigned __int64 *)(v_stack_pB0 + 16) == 0) goto loc_00858E06;
loc_00858D0D:
    result = *(unsigned __int64 *)(v_stack_pB0 + 16);
    if (v_stack_p70 != 0) {
        a1 = (v_stack_p70) & (-2);
        result = ObfDereferenceObject(a1, a2, *(unsigned __int64 *)(a1 + 56), 48);
    }
loc_00858D23:
    if (sign_flag) goto loc_00858D83;
    v_stack_pA8 = v_stack_pA0;
loc_00858D36:
    if (!sign_flag) goto loc_00858329;
    goto loc_00858D83;
loc_00858D41:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 4152) != 0) goto loc_00858DDD;
    goto loc_00858D36;
loc_00858D5D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (1)) == 0) goto loc_00858E55;
loc_00858D6A:
    v_r14 = (unsigned int)(0xC0000425ULL);
    if (1 == 0) { v_r14 = (unsigned int)((unsigned int)(0xC000017CULL)); }
    result = CmpUnlockKcb(v_stack_p90, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 4152), *(unsigned __int64 *)(a2 + 32));
loc_00858D83:
    result = CmpUnlockRegistry(v_stack_p90, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 4152), *(unsigned __int64 *)(a2 + 32));
    result = CmpDetachFromRegistryProcess(v_stack_p110, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 4152), *(unsigned __int64 *)(a2 + 32));
    goto loc_00858C30;
loc_00858D9A:
    goto loc_00858D0D;
loc_00858DA2:
    v_stack_p20 = v_stack_p58;
    result = CmQueryLayeredKey(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_r14, (unsigned int)(a5));
    result = CmpUnlockRegistry(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_r14, (unsigned int)(a5));
    result = CmpDetachFromRegistryProcess(v_stack_p110, (unsigned int)((unsigned int)((unsigned int)(a3))), v_r14, (unsigned int)(a5));
    goto loc_00858C33;
loc_00858DDD:
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = 0;
    result = CmpTransSearchAddTrans(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 64), v_r14, (unsigned int)(a5));
    goto loc_00858D23;
loc_00858E06:
    v_stack_pA0 = v_stack_p68;
    goto loc_00858D0D;
loc_00858E1E:
    if ((*(unsigned __int64 *)(a1 + 64)) != v_stack_p68) goto loc_00858CA2;
    goto loc_00858D36;
loc_00858E33:
    result = CmpUnlockTwoKcbs(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8), *(unsigned __int64 *)(a1 + 56), v_r14, (unsigned int)(a5));
    goto loc_00858BEB;
loc_00858E44:
    result = CmpLockTwoKcbsShared(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8), *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8), v_r14, (unsigned int)(a5));
    goto loc_00858350;
loc_00858E55:
    a1 = 0;
    goto loc_00858D6A;
}
```

## 5. (Beta) C Style

```c
int64_t CmQueryKey(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m48;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p110;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x5B24E0)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m128 = Arg4;
    v_stack_mF0 = Arg1;
    v_stack_mD0 = Arg1;
    v_stack_m110 = Arg2;
    v_stack_m108 = Arg4;
    v_stack_m130 = Arg6;
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0x100) = 0;
    v_stack_mE0 = 0;
    v_stack_mB8 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm1;
    v_stack_mC8 = v_xmm0;
    result = CmpInitializeDelayDerefContext(local_rsp - 200, Arg2, Arg3, Arg4);
    result = CmpAttachToRegistryProcess(v_stack_m78, Arg2, Arg3, Arg4);
    result = CmpLockRegistry(v_stack_m78, Arg2, Arg3, Arg4);
    v_stack_mF8 = *(uint64_t *)(arg1 + 0x8);
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)) != 0) goto loc_00858DA2;
    if ((*(uint64_t *)(arg1 + 0x38)) != 0) goto loc_00858C5E;
    if ((*(uint64_t *)(arg1 + 0x40)) != 0) goto loc_00858C5E;
loc_00858329:
    local_rdi = *(uint64_t *)(arg1 + 0x8);
    if (Arg2 != 0) {
        local_rdi = *(uint64_t *)(Arg2 + 0x8);
        v_stack_mF8 = local_rdi;
    }
    if (Arg2 != 0) goto loc_00858E44;
    result = CmpLockKcbShared(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, Arg4);
loc_00858350:
    if (((uint32_t)((uint32_t)(Arg3))) == 3) goto loc_00858A58;
    if (Arg2 != 0) goto loc_00858542;
loc_00858363:
    result = CmpIsKeyDeletedForKeyBody(Arg1, 0, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00858555;
    if (((uint32_t)((uint32_t)(Arg3))) == 5) goto loc_0085878A;
    if (((uint32_t)((uint32_t)(Arg3))) == 6) goto loc_008585D7;
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_0085859A;
    v_stack_m120 = 0xFFFFFFFFULL;
    v_stack_m11C = 0;
    if (((uint32_t)((uint32_t)(Arg3))) != 4) goto loc_008584C0;
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_m130;
    result = CmpQueryKeyDataFromCache(local_rdi, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m128, (uint32_t)(Arg5));
loc_008583D5:
    v_stack_m138 = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_008583DA:
    if (sign_flag) goto loc_00858BD1;
loc_008583E8:
    if (Arg2 != 0) goto loc_0085883F;
    if ((*(uint8_t *)(v_rip + 0x5B68A9)) == ((uint8_t)(Arg2))) goto loc_00858BD1;
    if ((*(uint8_t *)(v_rip + 0x5B68A9)) >= ((uint8_t)(Arg2))) goto loc_00858BD1;
    if ((((uint32_t)((uint32_t)(Arg3) - 2)) & (0xFFFFFFFDULL)) != 0) goto loc_00858BD1;
    v_stack_m108 = 0;
    v_stack_mE8 = 0;
    v_stack_m130 = 0;
    v_stack_m148 = v_stack_m108;
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_m130;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = v_stack_mC8;
    Arg2 = 0;
    result = CmpFindSubKeyByNumberFromMergedView(*(uint64_t *)(arg1 + 0x8), Arg2, (uint32_t)(0xFFFFFFFFULL), 0);
    v_stack_m138 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0x8000001AULL) goto loc_00858BD1;
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_0085849F;
    *(uint32_t *)(v_stack_m128 + 0x14) = (uint32_t)((uint32_t)(v_stack_m108));
    goto loc_008584A2;
loc_0085849F:
    *(uint32_t *)(v_stack_m128 + 0xC) = (uint32_t)((uint32_t)(v_stack_m108));
loc_008584A2:
    v_stack_m138 = 0;
    goto loc_00858BD1;
loc_008584C0:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m128 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00858590;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m128 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x28)), v_stack_m120, 0);
loc_008584DE:
    if (result == 0) goto loc_00858BC6;
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_m128;
    v_stack_m160 = v_stack_m130;
    v_stack_m168 = (uint32_t)((uint32_t)(Arg5));
    result = CmpQueryKeyDataFromNode(*(uint64_t *)(v_stack_m128 + 0x20), result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m128);
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m128 + 0x20) + 0x8C))) & (1)) != 0) goto loc_00858780;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m128 + 0x20), v_stack_m120, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m128);
    goto loc_008583D5;
loc_00858542:
    result = CmpIsKeyDeletedForKeyBody(0, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m128);
    if ((uint8_t)(result) == 0) goto loc_00858363;
loc_00858555:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (1)) != 0) goto loc_00858578;
    v_stack_m138 = (uint32_t)((uint32_t)(0xC000017CULL));
    goto loc_00858BD1;
loc_0085856D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (1)) == 0) goto loc_00858A4A;
loc_00858578:
    goto loc_00858586;
loc_00858580:
loc_00858586:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00858BD1;
loc_00858590:
    result = HvpGetCellPaged(0, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m128);
    goto loc_008584DE;
loc_0085859A:
    *(uint32_t *)(v_stack_m130) = 4;
    if (Arg5 < 4) goto loc_00858A3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m128 + 0x20) + 0x1010)))) & (1)) != 0) goto loc_00858A28;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128))) | (1));
    goto loc_00858A2B;
loc_008585D7:
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    result = PsGetCurrentThreadProcess(Arg1, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m128);
    result = SeCaptureSubjectContextEx(*(uint64_t *)(gs_base + (0 + 0x188)), result, v_stack_mA8, v_stack_m128);
    *(uint32_t *)(v_stack_m130) = 4;
    if (Arg5 < 4) goto loc_00858722;
    if ((*(uint8_t *)(v_rip + 0x5B6669)) == 0) goto loc_0085871A;
    if (((*(uint32_t *)(v_stack_mF8 + 0xB8)) & (0x2000000ULL)) != 0) goto loc_0085871A;
    result = CmpIsKcbInsideVirtualizedHive(v_stack_mF8, v_stack_m130, v_stack_mF8, v_stack_m128);
    if ((uint8_t)(result) == 0) goto loc_0085871A;
    Arg3 = 0;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_stack_mA8, Arg3, v_stack_m128);
    local_r10 = ((uint8_t)(result) == 0) ? 1 : 0;
loc_0085868C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128))) & (0xFFFFFFFEULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint8_t)(local_r10))));
    *(uint32_t *)(v_stack_m128) = (uint32_t)(Arg1);
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFDULL));
    *(uint32_t *)(v_stack_m128) = (uint32_t)(Arg1);
    if ((uint8_t)(local_r10) == 0) goto loc_008586C3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0xB8)))) & (32)) != 0) goto loc_0085872F;
loc_008586B8:
    if (1 != 0) {
        Arg4 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (2));
        *(uint32_t *)(v_stack_m128) = (uint32_t)(Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0x5B65D6)) == 0) goto loc_008586D9;
    local_r14 = 4;
    if (((*(uint32_t *)(v_stack_mF8 + 0xB8)) & (0x1000000ULL)) == 0) {
        local_r14 = 0;
    }
    Arg4 = (uint32_t)((Arg4) & (0xFFFFFFFBULL));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(local_r14)));
    *(uint32_t *)(v_stack_m128) = (uint32_t)(Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0xB8))) >> (22));
    Arg1 = (uint32_t)((Arg1) & (8));
    Arg4 = (uint32_t)((Arg4) & (0xFFFFFFF7ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg4)));
    *(uint32_t *)(v_stack_m128) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0xB8))) >> (19));
    result = (uint32_t)((result) & (16));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFEFULL));
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_m128) = (uint32_t)(result);
    v_stack_m138 = 0;
    goto loc_00858733;
loc_0085871A:
    local_r10 = 0;
    goto loc_0085868C;
loc_00858722:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00858733;
loc_0085872F:
    result = 0;
    goto loc_008586B8;
loc_00858733:
    goto loc_0085876E;
loc_0085876E:
    result = SeReleaseSubjectContext(v_stack_mA8, v_stack_m128, v_stack_mF8, Arg4);
    goto loc_008583DA;
loc_00858780:
    result = HvpReleaseCellFlat(v_stack_mA8, v_stack_m128, v_stack_mF8, Arg4);
    goto loc_008583D5;
loc_0085878A:
    *(uint32_t *)(v_stack_m130) = 12;
    if (Arg5 < 12) goto loc_008587F1;
    result = CmGetKeyFlags(*(uint64_t *)(gs_base + (0 + 0x188)), 0, v_stack_mF8, Arg4);
    *(uint32_t *)(v_stack_m128) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m128 + 0x4) = 0;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28)) < 0) {
        Arg1 = 1;
        *(uint32_t *)(v_stack_m128 + 0x4) = (uint32_t)(Arg1);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) & (0x100000ULL)) != 0) {
        Arg1 = (uint32_t)((Arg1) | (2));
        *(uint32_t *)(v_stack_m128 + 0x4) = (uint32_t)(Arg1);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) >> (4));
    result = (uint32_t)((result) & (15));
    *(uint32_t *)(v_stack_m128 + 0x8) = (uint32_t)(result);
    v_stack_m138 = 0;
    goto loc_008587FC;
loc_008587F1:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC0000023ULL));
loc_008587FC:
    goto loc_008583DA;
loc_0085883F:
    if ((((uint32_t)((uint32_t)(Arg3) - 3)) & (0xFFFFFFFCULL)) != 0) goto loc_00858B85;
    if (((uint32_t)((uint32_t)(Arg3))) == 4) goto loc_00858B85;
loc_00858858:
    if ((((uint32_t)((uint32_t)(Arg3) - 2)) & (0xFFFFFFFDULL)) != 0) goto loc_00858BD1;
    v_stack_m118 = 0;
    v_stack_mD8 = 0;
    v_stack_m128 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m148 = v_stack_m118;
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_m128;
    v_stack_m160 = v_stack_mD8;
    v_stack_m168 = v_stack_mC8;
    result = CmpFindSubKeyByNumberFromMergedView(*(uint64_t *)(Arg2 + 0x8), *(uint64_t *)(arg1 + 0x8), (uint32_t)(0xFFFFFFFFULL), 0);
    v_stack_m138 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0x8000001AULL) goto loc_0085890D;
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_008588F7;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x14) = (uint32_t)((uint32_t)(v_stack_m118));
    goto loc_008588FA;
loc_008588F7:
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC) = (uint32_t)((uint32_t)(v_stack_m118));
loc_008588FA:
    goto loc_0085890D;
loc_0085890D:
    v_stack_m148 = v_stack_m118;
    v_stack_m150 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    result = CmEnumerateValueKeyFromMergedView(Arg1, 0, 1, (uint32_t)(0xFFFFFFFFULL));
    v_stack_m138 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0x8000001AULL) goto loc_0085896F;
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_00858959;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x20) = (uint32_t)((uint32_t)(v_stack_m118));
    goto loc_0085895C;
loc_00858959:
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x14) = (uint32_t)((uint32_t)(v_stack_m118));
loc_0085895C:
    goto loc_0085896F;
loc_0085896F:
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_m130;
    result = CmpQueryKeyData(*(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_mA8, 48);
    v_stack_m138 = (uint32_t)(result);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) == 0) goto loc_00858BB7;
loc_008589B0:
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_008589E5;
    if (((uint32_t)((uint32_t)(v_stack_m90))) >= = (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x18))) {
        *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x18) = (uint32_t)((uint32_t)(v_stack_m90));
    }
    if (((uint32_t)((uint32_t)(v_stack_m84))) >= = (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24))) {
        *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24) = (uint32_t)((uint32_t)(v_stack_m84));
    }
    if (((uint32_t)((uint32_t)(v_stack_m80))) <= (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28))) goto loc_00858A12;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28) = (uint32_t)((uint32_t)(v_stack_m80));
    goto loc_00858A12;
loc_008589E5:
    if (((uint32_t)((uint32_t)(v_stack_m98))) >= = (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x10))) {
        *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x10) = (uint32_t)((uint32_t)(v_stack_m98));
    }
    if (((uint32_t)((uint32_t)(v_stack_m90))) >= = (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x18))) {
        *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x18) = (uint32_t)((uint32_t)(v_stack_m90));
    }
    if (((uint32_t)((uint32_t)(v_stack_m8C))) >= = (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1C))) {
        *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1C) = (uint32_t)((uint32_t)(v_stack_m8C));
    }
    goto loc_00858BD1;
loc_00858A28:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1) & (0xFFFFFFFEULL));
loc_00858A2B:
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188))) = (uint32_t)(Arg1);
    v_stack_m138 = 0;
    goto loc_008583E8;
loc_00858A3A:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00858BD1;
loc_00858A4A:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC000017CULL));
    goto loc_00858A77;
loc_00858A58:
    result = CmpIsKeyDeletedForKeyBody(Arg1, 0, v_stack_mA8, 48);
    if ((uint8_t)(result) != 0) goto loc_0085856D;
    v_stack_m138 = 0;
loc_00858A77:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x50)) == 0) goto loc_00858580;
    if ((*(uint8_t *)(v_rip + 0x5B6217)) == 0) goto loc_00858A9B;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)) & (0x1000000ULL)) != 0) goto loc_00858B60;
loc_00858A9B:
    result = CmpConstructName(*(uint64_t *)(arg1 + 0x8), 0, v_stack_mA8, 48);
loc_00858AA3:
    v_stack_m100 = result;
loc_00858AAB:
    if (v_stack_m100 == 0) goto loc_00858580;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m100)) + (4));
    *(uint32_t *)(v_stack_m130) = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(Arg5))) < 4) goto loc_00858B12;
    *(uint32_t *)(v_stack_m128) = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m100))));
    Arg1 = (uint32_t)(((uint32_t)(Arg5)) + (-4));
    result = (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m100)));
    local_r14 = 0;
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m100)))))) {
        result = (uint32_t)(Arg1);
        local_r14 = 0x80000005ULL;
        v_stack_m138 = (uint32_t)(local_r14);
    }
    result = memcpy(v_stack_m128 + 4, *(uint64_t *)(v_stack_m100 + 0x8), (uint32_t)((uint32_t)(result)), 48);
    goto loc_00858B1D;
loc_00858B12:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC0000023ULL));
loc_00858B1D:
    goto loc_008583DA;
loc_00858B60:
    result = CmVirtualKCBToRealPath(v_stack_m128, v_stack_mB8, (uint32_t)((uint32_t)(result)), 48);
    if (sign_flag) goto loc_00858AAB;
    goto loc_00858AA3;
loc_00858B85:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xA8)) >= (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0xA8))) goto loc_00858858;
    *(uint64_t *)(v_stack_m128) = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8) + 0xA8);
    goto loc_00858858;
loc_00858BB7:
    if (((uint32_t)((uint32_t)(0xC0000023ULL))) == 0x80000005ULL) goto loc_008589B0;
    goto loc_00858BD1;
loc_00858BC6:
    goto loc_008583D5;
loc_00858BD1:
    if (0 != 0) goto loc_00858E33;
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_mD0 + 0x8), v_stack_mB8, (uint32_t)((uint32_t)(result)), 48);
loc_00858BEB:
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mC8, Arg2, (uint32_t)((uint32_t)(result)), 48);
    result = CmpUnlockRegistry(v_stack_mC8, Arg2, (uint32_t)((uint32_t)(result)), 48);
    result = CmpDetachFromRegistryProcess(v_stack_m78, Arg2, (uint32_t)((uint32_t)(result)), 48);
    if (v_stack_mB0 != 0) goto loc_00858C57;
    if (v_stack_m100 != 0) {
        Arg2 = 0x624E4D43ULL;
        result = CmpFreePoolWithTag(v_stack_m100, Arg2, (uint32_t)((uint32_t)(result)), 48);
    }
loc_00858C33:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(result)), 48);
    local_rsp = (local_rsp) + (336);
    return result;
loc_00858C57:
    result = ExFreePool(Arg1, Arg2, (uint32_t)((uint32_t)(result)), 48);
    goto loc_00858C30;
loc_00858C5E:
    result = CmpLockKcbShared(v_stack_m128, Arg2, (uint32_t)((uint32_t)(result)), 48);
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(Arg1, Arg2, (uint32_t)((uint32_t)(result)), 48);
    if ((uint8_t)(result) != 0) goto loc_00858D5D;
    result = CmpUnlockKcb(v_stack_m128, Arg2, (uint32_t)((uint32_t)(result)), 48);
    v_stack_pA0 = 0;
    v_stack_p68 = 0;
    v_stack_p70 = *(uint64_t *)(arg1 + 0x38);
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_00858E1E;
loc_00858CA2:
    Arg2 = (*(uint64_t *)(arg1 + 0x8)) ^ (1);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x8))) & (1)) == 0) { Arg2 = *(uint64_t *)(arg1 + 0x8); }
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x38))) & (1)) == 0) goto loc_00858D41;
    result = (*(uint64_t *)(arg1 + 0x38)) & (-2);
    v_stack_pB0 = result;
    result = CmpTransReferenceTransaction(*(uint64_t *)(arg1 + 0x38), Arg2, *(uint64_t *)(arg1 + 0x38), 48);
    if (sign_flag) goto loc_00858D9A;
    v_stack_pA0 = *(uint64_t *)(v_stack_pB0 + 0x10);
    if (*(uint64_t *)(v_stack_pB0 + 0x10) == 0) goto loc_00858E06;
loc_00858D0D:
    result = *(uint64_t *)(v_stack_pB0 + 0x10);
    if (v_stack_p70 != 0) {
        Arg1 = (v_stack_p70) & (-2);
        result = ObfDereferenceObject(Arg1, Arg2, *(uint64_t *)(arg1 + 0x38), 48);
    }
loc_00858D23:
    if (sign_flag) goto loc_00858D83;
    v_stack_pA8 = v_stack_pA0;
loc_00858D36:
    if (!sign_flag) goto loc_00858329;
    goto loc_00858D83;
loc_00858D41:
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x20) + 0x1038) != 0) goto loc_00858DDD;
    goto loc_00858D36;
loc_00858D5D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (1)) == 0) goto loc_00858E55;
loc_00858D6A:
    local_r14 = (uint32_t)(0xC0000425ULL);
    if (1 == 0) { local_r14 = (uint32_t)((uint32_t)(0xC000017CULL)); }
    result = CmpUnlockKcb(v_stack_p90, Arg2, *(uint64_t *)(*(uint64_t *)(Arg2 + 0x20) + 0x1038), *(uint64_t *)(Arg2 + 0x20));
loc_00858D83:
    result = CmpUnlockRegistry(v_stack_p90, Arg2, *(uint64_t *)(*(uint64_t *)(Arg2 + 0x20) + 0x1038), *(uint64_t *)(Arg2 + 0x20));
    result = CmpDetachFromRegistryProcess(v_stack_p110, Arg2, *(uint64_t *)(*(uint64_t *)(Arg2 + 0x20) + 0x1038), *(uint64_t *)(Arg2 + 0x20));
    goto loc_00858C30;
loc_00858D9A:
    goto loc_00858D0D;
loc_00858DA2:
    v_stack_p20 = v_stack_p58;
    result = CmQueryLayeredKey(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), local_r14, (uint32_t)(Arg5));
    result = CmpUnlockRegistry(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), local_r14, (uint32_t)(Arg5));
    result = CmpDetachFromRegistryProcess(v_stack_p110, (uint32_t)((uint32_t)((uint32_t)(Arg3))), local_r14, (uint32_t)(Arg5));
    goto loc_00858C33;
loc_00858DDD:
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = 0;
    result = CmpTransSearchAddTrans(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x40), local_r14, (uint32_t)(Arg5));
    goto loc_00858D23;
loc_00858E06:
    v_stack_pA0 = v_stack_p68;
    goto loc_00858D0D;
loc_00858E1E:
    if ((*(uint64_t *)(arg1 + 0x40)) != v_stack_p68) goto loc_00858CA2;
    goto loc_00858D36;
loc_00858E33:
    result = CmpUnlockTwoKcbs(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8), *(uint64_t *)(arg1 + 0x38), local_r14, (uint32_t)(Arg5));
    goto loc_00858BEB;
loc_00858E44:
    result = CmpLockTwoKcbsShared(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8), *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8), local_r14, (uint32_t)(Arg5));
    goto loc_00858350;
loc_00858E55:
    Arg1 = 0;
    goto loc_00858D6A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00858240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
