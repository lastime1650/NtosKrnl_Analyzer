# MiUserFault

- RVA: `0x00329840`–`0x0032A157` (길이 `2,327` bytes)
- VA: `0x0000000140329840`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00076028`
- 디코드: `539`개 명령, `2,327/2,327` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00329919` → [MiGetCurrentSlabIdentity](../3B/MiGetCurrentSlabIdentity_function_003BD020.md) (function, `0x003BD020`)
- `0x0032994D` → [MiCanFlushMakeProgress](../3B/MiCanFlushMakeProgress_function_003BC9D0.md) (function, `0x003BC9D0`)
- `0x00329A09` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x00329AC0` → [MiResolvePageTablePage](../27/MiResolvePageTablePage_function_00275930.md) (function, `0x00275930`)
- `0x00329B5B` → [MiCheckProtoAccess](MiCheckProtoAccess_function_0032DFE0.md) (function, `0x0032DFE0`)
- `0x00329B9A` → [MiZeroFault](MiZeroFault_function_0032D680.md) (function, `0x0032D680`)
- `0x00329CA2` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x00329D4C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00329D59` → [MiWaitForRotateToComplete](../4A/MiWaitForRotateToComplete_function_004A54F4.md) (function, `0x004A54F4`)
- `0x00329D6F` → [MiUnlockFaultPageTable](../27/MiUnlockFaultPageTable_function_0027D870.md) (function, `0x0027D870`)
- `0x00329D87` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00329DE3` → [MiCheckFatalAccessViolation](../3F/MiCheckFatalAccessViolation_function_003F00F0.md) (function, `0x003F00F0`)
- `0x00329DF4` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x00329E06` → [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) (function, `0x00A30854`)
- `0x00329E12` → [MiPteHasShadow](MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00329E62` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x00329E7D` → [MiValidFault](MiValidFault_function_003280B4.md) (function, `0x003280B4`)
- `0x00329EBE` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00329ECF` → [MiDelayFaultingThread](../2A/MiDelayFaultingThread_function_002A3054.md) (function, `0x002A3054`)
- `0x00329F99` → [MiAllowGuardFault](../34/MiAllowGuardFault_function_0034B5B0.md) (function, `0x0034B5B0`)
- `0x00329FD7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00329FDF` → [IS_PTE_NOT_DEMAND_ZERO](../22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (function, `0x0022F4D0`)
- `0x00329FFD` → [MiResolveDemandZeroFault](../2B/MiResolveDemandZeroFault_function_002B5A40.md) (function, `0x002B5A40`)
- `0x0032A00A` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x0032A014` → [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) (function, `0x00A30854`)
- `0x0032A028` → [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) (function, `0x00A30854`)
- `0x0032A034` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0032A06B` → [MiCheckHoldFaultForHotPatch](../3D/MiCheckHoldFaultForHotPatch_function_003D4BA8.md) (function, `0x003D4BA8`)
- `0x0032A09B` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0032A0A3` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0032A0B0` → [MiIsVadEligibleForCommitRelease](../4F/MiIsVadEligibleForCommitRelease_function_004FB6FC.md) (function, `0x004FB6FC`)
- `0x0032A0BD` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0032A0D0` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0032A0EB` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0032A0F3` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0032A0FF` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0032A111` → [MiLockTransitionLeafPageEx](../40/MiLockTransitionLeafPageEx_function_00405884.md) (function, `0x00405884`)
- `0x0032A11C` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)

### Direct callers
- [sub_0027F063](../27/Unknown_function_0027F063.md) at `0x0027F089`

### Static image references
- `0x00329888` → RVA `0x00E37418` (`.data`; read)
- `0x003298B7` → RVA `0x00E30088` (`.data`; read)
- `0x003298E1` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x003299B2` → RVA `0x00E38840` (`.data`; read)
- `0x003299DA` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003299E7` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003299F4` → RVA `0x00F0DE58` (`.data`; read)
- `0x00329A51` → RVA `0x00E38860` (`.data`; read)
- `0x00329C29` → RVA `0x00011060` (`.rdata`; read)
- `0x00329CDB` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00329F20` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00329E06` → [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) (`.text` → `PAGE`)
  - `0x0032A014` → [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) (`.text` → `PAGE`)
  - `0x0032A028` → [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0032A127` → [sub_006E1E80](../6E/Unknown_function_006E1E80.md) (`tail-transfer`)
  - `0x0032A152` → [sub_006E1E80](../6E/Unknown_function_006E1E80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00329840  4C 8B DC                        mov r11, rsp
00329843  53                              push rbx
00329844  55                              push rbp
00329845  56                              push rsi
00329846  57                              push rdi
00329847  41 54                           push r12
00329849  41 55                           push r13
0032984B  41 56                           push r14
0032984D  41 57                           push r15
0032984F  48 83 EC 38                     sub rsp, 0x38
00329853  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
0032985C  4C 8D 79 38                     lea r15, [rcx + 0x38]
00329860  45 33 ED                        xor r13d, r13d
00329863  4C 8B F1                        mov r14, rcx
00329866  41 8B DD                        mov ebx, r13d
00329869  45 89 6B 10                     mov dword ptr [r11 + 0x10], r13d
0032986D  49 8B B1 B8 00 00 00            mov rsi, qword ptr [r9 + 0xb8]
00329874  41 8D 4D 02                     lea ecx, [r13 + 2]
00329878  48 8D 86 00 04 00 00            lea rax, [rsi + 0x400]
0032987F  49 89 07                        mov qword ptr [r15], rax
00329882  8B 86 B8 04 00 00               mov eax, dword ptr [rsi + 0x4b8]
00329888  39 1D 8A DB B0 00               cmp dword ptr [rip + 0xb0db8a], ebx
0032988E  4D 89 6B 18                     mov qword ptr [r11 + 0x18], r13
00329892  0F 85 30 06 00 00               jne 0x140329ec8
00329898  8B 86 50 05 00 00               mov eax, dword ptr [rsi + 0x550]
0032989E  83 F8 10                        cmp eax, 0x10
003298A1  0F 86 EB 00 00 00               jbe 0x140329992
003298A7  F7 86 FC 05 00 00 00 10 00 00   test dword ptr [rsi + 0x5fc], 0x1000
003298B1  0F 85 DB 00 00 00               jne 0x140329992
003298B7  48 8B 05 CA 67 B0 00            mov rax, qword ptr [rip + 0xb067ca]
003298BE  0F B7 8E AE 04 00 00            movzx ecx, word ptr [rsi + 0x4ae]
003298C5  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
003298C9  8B 82 B4 04 00 00               mov eax, dword ptr [rdx + 0x4b4]
003298CF  83 F8 FF                        cmp eax, -1
003298D2  74 0D                           je 0x1403298e1
003298D4  48 39 B2 A0 06 00 00            cmp qword ptr [rdx + 0x6a0], rsi
003298DB  0F 84 AC 00 00 00               je 0x14032998d
003298E1  66 83 3D 17 B7 C9 00 01         cmp word ptr [rip + 0xc9b717], 1
003298E9  41 BA 20 04 00 00               mov r10d, 0x420
003298EF  0F B7 8E AE 04 00 00            movzx ecx, word ptr [rsi + 0x4ae]
003298F6  48 8B 05 8B 67 B0 00            mov rax, qword ptr [rip + 0xb0678b]
003298FD  4C 8B 1C C8                     mov r11, qword ptr [rax + rcx*8]
00329901  0F 87 D2 05 00 00               ja 0x140329ed9
00329907  49 8B 93 00 49 00 00            mov rdx, qword ptr [r11 + 0x4900]
0032990E  49 3B D2                        cmp rdx, r10
00329911  73 7A                           jae 0x14032998d
00329913  49 8B C9                        mov rcx, r9
00329916  41 8B FD                        mov edi, r13d
00329919  E8 02 37 09 00                  call 0x1403bd020
0032991E  3C FF                           cmp al, 0xff
00329920  74 14                           je 0x140329936
00329922  49 8B 83 80 47 00 00            mov rax, qword ptr [r11 + 0x4780]
00329929  48 03 D0                        add rdx, rax
0032992C  49 3B D2                        cmp rdx, r10
0032992F  73 5C                           jae 0x14032998d
00329931  BF 02 00 00 00                  mov edi, 2
00329936  49 8B 83 C0 4B 00 00            mov rax, qword ptr [r11 + 0x4bc0]
0032993D  4C 2B D2                        sub r10, rdx
00329940  49 3B C2                        cmp rax, r10
00329943  72 3F                           jb 0x140329984
00329945  4D 8B C2                        mov r8, r10
00329948  33 D2                           xor edx, edx
0032994A  49 8B CB                        mov rcx, r11
0032994D  E8 7E 30 09 00                  call 0x1403bc9d0
00329952  85 C0                           test eax, eax
00329954  74 2E                           je 0x140329984
00329956  44 89 AE 50 05 00 00            mov dword ptr [rsi + 0x550], r13d
0032995D  80 BE 90 00 00 00 09            cmp byte ptr [rsi + 0x90], 9
00329964  0F 8D 13 07 00 00               jge 0x14032a07d
0032996A  48 39 9E 70 06 00 00            cmp qword ptr [rsi + 0x670], rbx
00329971  0F 85 06 07 00 00               jne 0x14032a07d
00329977  BB F4 01 01 00                  mov ebx, 0x101f4
0032997C  85 FF                           test edi, edi
0032997E  74 04                           je 0x140329984
00329980  0F BA EB 11                     bts ebx, 0x11
00329984  66 85 DB                        test bx, bx
00329987  0F 85 40 05 00 00               jne 0x140329ecd
0032998D  B9 02 00 00 00                  mov ecx, 2
00329992  8B 86 B8 04 00 00               mov eax, dword ptr [rsi + 0x4b8]
00329998  24 0F                           and al, 0xf
0032999A  3C 06                           cmp al, 6
0032999C  0F 83 02 05 00 00               jae 0x140329ea4
003299A2  8B 86 B8 04 00 00               mov eax, dword ptr [rsi + 0x4b8]
003299A8  24 0F                           and al, 0xf
003299AA  3C 01                           cmp al, 1
003299AC  0F 85 CE 05 00 00               jne 0x140329f80
003299B2  48 8D 05 87 EE B0 00            lea rax, [rip + 0xb0ee87]
003299B9  65 8B 1C 25 A4 01 00 00         mov ebx, dword ptr gs:[0x1a4]
003299C1  48 8B 00                        mov rax, qword ptr [rax]
003299C4  D1 EB                           shr ebx, 1
003299C6  83 E3 03                        and ebx, 3
003299C9  8B FB                           mov edi, ebx
003299CB  48 C1 E7 06                     shl rdi, 6
003299CF  48 03 F8                        add rdi, rax
003299D2  44 0F 20 C5                     mov rbp, cr8
003299D6  44 0F 22 C1                     mov cr8, rcx
003299DA  44 39 2D 3F D3 C9 00            cmp dword ptr [rip + 0xc9d33f], r13d
003299E1  0F 85 5F 03 00 00               jne 0x140329d46
003299E7  F6 05 18 D1 C9 00 21            test byte ptr [rip + 0xc9d118], 0x21
003299EE  0F 84 8D 02 00 00               je 0x140329c81
003299F4  8B 05 5E 44 BE 00               mov eax, dword ptr [rip + 0xbe445e]
003299FA  85 C0                           test eax, eax
003299FC  0F 85 7F 02 00 00               jne 0x140329c81
00329A02  40 0F B6 D5                     movzx edx, bpl
00329A06  48 8B CF                        mov rcx, rdi
00329A09  E8 12 33 F5 FF                  call 0x14027cd20
00329A0E  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00329A17  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00329A1E  48 85 C9                        test rcx, rcx
00329A21  74 06                           je 0x140329a29
00329A23  89 99 44 01 00 00               mov dword ptr [rcx + 0x144], ebx
00329A29  40 0F B6 DD                     movzx ebx, bpl
00329A2D  41 88 5F 0C                     mov byte ptr [r15 + 0xc], bl
00329A31  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00329A3A  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00329A41  8B 81 B8 04 00 00               mov eax, dword ptr [rcx + 0x4b8]
00329A47  24 0F                           and al, 0xf
00329A49  3C 01                           cmp al, 1
00329A4B  0F 85 23 05 00 00               jne 0x140329f74
00329A51  48 8D 15 08 EE B0 00            lea rdx, [rip + 0xb0ee08]
00329A58  8B 81 B8 04 00 00               mov eax, dword ptr [rcx + 0x4b8]
00329A5E  BF 01 00 00 00                  mov edi, 1
00329A63  C1 E8 18                        shr eax, 0x18
00329A66  49 B8 00 00 00 00 00 80 FF FF   movabs r8, 0xffff800000000000
00329A70  24 30                           and al, 0x30
00329A72  3C 30                           cmp al, 0x30
00329A74  0F 84 0D 06 00 00               je 0x14032a087
00329A7A  49 8B 0E                        mov rcx, qword ptr [r14]
00329A7D  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
00329A87  49 3B C8                        cmp rcx, r8
00329A8A  0F 82 B0 05 00 00               jb 0x14032a040
00329A90  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00329A99  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00329AA0  4C 39 AB 68 02 00 00            cmp qword ptr [rbx + 0x268], r13
00329AA7  0F 85 A9 02 00 00               jne 0x140329d56
00329AAD  48 8B 8B 78 07 00 00            mov rcx, qword ptr [rbx + 0x778]
00329AB4  48 85 C9                        test rcx, rcx
00329AB7  0F 85 AB 05 00 00               jne 0x14032a068
00329ABD  49 8B CE                        mov rcx, r14
00329AC0  E8 6B BE F4 FF                  call 0x140275930
00329AC5  8B D8                           mov ebx, eax
00329AC7  3D 34 04 00 C0                  cmp eax, 0xc0000434
00329ACC  0F 84 94 02 00 00               je 0x140329d66
00329AD2  85 C0                           test eax, eax
00329AD4  0F 88 8F 02 00 00               js 0x140329d69
00329ADA  49 8B 6E 18                     mov rbp, qword ptr [r14 + 0x18]
00329ADE  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
00329AE8  48 8B 45 00                     mov rax, qword ptr [rbp]
00329AEC  49 8B CA                        mov rcx, r10
00329AEF  49 BC F8 D7 BE 7D FB F6 FF FF   movabs r12, 0xfffff6fb7dbed7f8
00329AF9  48 3B E9                        cmp rbp, rcx
00329AFC  72 1F                           jb 0x140329b1d
00329AFE  49 8B CC                        mov rcx, r12
00329B01  48 3B E9                        cmp rbp, rcx
00329B04  77 17                           ja 0x140329b1d
00329B06  40 84 C7                        test dil, al
00329B09  74 1B                           je 0x140329b26
00329B0B  A8 42                           test al, 0x42
00329B0D  0F 95 C2                        setne dl
00329B10  A8 20                           test al, 0x20
00329B12  0F 95 C1                        setne cl
00329B15  84 D1                           test cl, dl
00329B17  0F 84 BE 01 00 00               je 0x140329cdb
00329B1D  40 84 C7                        test dil, al
00329B20  0F 85 51 03 00 00               jne 0x140329e77
00329B26  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00329B2A  F6 C2 02                        test dl, 2
00329B2D  0F 85 79 01 00 00               jne 0x140329cac
00329B33  48 85 C0                        test rax, rax
00329B36  74 3F                           je 0x140329b77
00329B38  48 8B C8                        mov rcx, rax
00329B3B  48 C1 E9 05                     shr rcx, 5
00329B3F  83 E1 1F                        and ecx, 0x1f
00329B42  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
00329B49  48 0F BA E0 0A                  bt rax, 0xa
00329B4E  73 70                           jae 0x140329bc0
00329B50  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00329B58  48 8B CD                        mov rcx, rbp
00329B5B  E8 80 44 00 00                  call 0x14032dfe0
00329B60  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00329B68  48 85 C0                        test rax, rax
00329B6B  75 49                           jne 0x140329bb6
00329B6D  BB 05 00 00 C0                  mov ebx, 0xc0000005
00329B72  E9 F2 01 00 00                  jmp 0x140329d69
00329B77  4C 8D 8C 24 90 00 00 00         lea r9, [rsp + 0x90]
00329B7F  44 88 AC 24 80 00 00 00         mov byte ptr [rsp + 0x80], r13b
00329B87  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
00329B8F  49 8B CE                        mov rcx, r14
00329B92  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00329B9A  E8 E1 3A 00 00                  call 0x14032d680
00329B9F  0F B6 9C 24 80 00 00 00         movzx ebx, byte ptr [rsp + 0x80]
00329BA7  8B F8                           mov edi, eax
00329BA9  84 DB                           test bl, bl
00329BAB  0F 85 A9 02 00 00               jne 0x140329e5a
00329BB1  BF 01 00 00 00                  mov edi, 1
00329BB6  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
00329BC0  81 BC 24 88 00 00 00 00 01 00 00  cmp dword ptr [rsp + 0x88], 0x100
00329BCB  0F 84 8D 00 00 00               je 0x140329c5e
00329BD1  41 8B 56 08                     mov edx, dword ptr [r14 + 8]
00329BD5  41 8B 46 50                     mov eax, dword ptr [r14 + 0x50]
00329BD9  83 E2 02                        and edx, 2
00329BDC  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
00329BE0  C1 E8 08                        shr eax, 8
00329BE3  A8 01                           test al, 1
00329BE5  0F 85 A8 01 00 00               jne 0x140329d93
00329BEB  48 8B 5D 00                     mov rbx, qword ptr [rbp]
00329BEF  49 8B C2                        mov rax, r10
00329BF2  48 3B E8                        cmp rbp, rax
00329BF5  72 21                           jb 0x140329c18
00329BF7  49 8B C4                        mov rax, r12
00329BFA  48 3B E8                        cmp rbp, rax
00329BFD  77 19                           ja 0x140329c18
00329BFF  F6 C3 01                        test bl, 1
00329C02  74 1D                           je 0x140329c21
00329C04  F6 C3 42                        test bl, 0x42
00329C07  0F 95 C1                        setne cl
00329C0A  F6 C3 20                        test bl, 0x20
00329C0D  0F 95 C0                        setne al
00329C10  84 C8                           test al, cl
00329C12  0F 84 FA 01 00 00               je 0x140329e12
00329C18  F6 C3 01                        test bl, 1
00329C1B  0F 85 68 02 00 00               jne 0x140329e89
00329C21  44 8B A4 24 88 00 00 00         mov r12d, dword ptr [rsp + 0x88]
00329C29  48 8D 0D 30 74 CE FF            lea rcx, [rip - 0x318bd0]
00329C30  48 85 D2                        test rdx, rdx
00329C33  41 8B C4                        mov eax, r12d
00329C36  48 0F 45 D7                     cmovne rdx, rdi
00329C3A  83 E0 07                        and eax, 7
00329C3D  41 8B FC                        mov edi, r12d
00329C40  0F BE 04 08                     movsx eax, byte ptr [rax + rcx]
00329C44  2B C2                           sub eax, edx
00329C46  83 F8 0A                        cmp eax, 0xa
00329C49  0F 8C 6F 01 00 00               jl 0x140329dbe
00329C4F  41 8B C4                        mov eax, r12d
00329C52  83 E0 F8                        and eax, 0xfffffff8
00329C55  83 F8 10                        cmp eax, 0x10
00329C58  0F 84 2E 03 00 00               je 0x140329f8c
00329C5E  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00329C66  49 89 46 68                     mov qword ptr [r14 + 0x68], rax
00329C6A  B8 16 00 00 C0                  mov eax, 0xc0000016
00329C6F  48 83 C4 38                     add rsp, 0x38
00329C73  41 5F                           pop r15
00329C75  41 5E                           pop r14
00329C77  41 5D                           pop r13
00329C79  41 5C                           pop r12
00329C7B  5F                              pop rdi
00329C7C  5E                              pop rsi
00329C7D  5D                              pop rbp
00329C7E  5B                              pop rbx
00329C7F  C3                              ret
00329C80  CC                              int3
00329C81  0F 0D 0F                        prefetchw byte ptr [rdi]
00329C84  8B 07                           mov eax, dword ptr [rdi]
00329C86  0F BA F0 1F                     btr eax, 0x1f
00329C8A  8D 48 01                        lea ecx, [rax + 1]
00329C8D  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
00329C91  0F 84 77 FD FF FF               je 0x140329a0e
00329C97  85 C0                           test eax, eax
00329C99  79 EF                           jns 0x140329c8a
00329C9B  40 0F B6 D5                     movzx edx, bpl
00329C9F  48 8B CF                        mov rcx, rdi
00329CA2  E8 D9 86 03 00                  call 0x140362380
00329CA7  E9 62 FD FF FF                  jmp 0x140329a0e
00329CAC  8B 8E F4 01 00 00               mov ecx, dword ptr [rsi + 0x1f4]
00329CB2  F6 C1 10                        test cl, 0x10
00329CB5  0F 84 78 FE FF FF               je 0x140329b33
00329CBB  48 B9 00 00 00 00 00 80 FF FF   movabs rcx, 0xffff800000000000
00329CC5  49 39 0E                        cmp qword ptr [r14], rcx
00329CC8  0F 83 65 FE FF FF               jae 0x140329b33
00329CCE  48 83 E2 FD                     and rdx, 0xfffffffffffffffd
00329CD2  49 89 56 08                     mov qword ptr [r14 + 8], rdx
00329CD6  E9 58 FE FF FF                  jmp 0x140329b33
00329CDB  48 F7 05 A2 CD C9 00 00 00 60 00  test qword ptr [rip + 0xc9cda2], 0x600000
00329CE6  0F 84 31 FE FF FF               je 0x140329b1d
00329CEC  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00329CF5  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00329CFC  40 38 BA 60 01 00 00            cmp byte ptr [rdx + 0x160], dil
00329D03  0F 84 14 FE FF FF               je 0x140329b1d
00329D09  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
00329D10  4D 85 C0                        test r8, r8
00329D13  0F 84 04 FE FF FF               je 0x140329b1d
00329D19  48 8B CD                        mov rcx, rbp
00329D1C  48 C1 E9 03                     shr rcx, 3
00329D20  81 E1 FF 01 00 00               and ecx, 0x1ff
00329D26  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
00329D2A  F6 C1 20                        test cl, 0x20
00329D2D  74 04                           je 0x140329d33
00329D2F  48 83 C8 20                     or rax, 0x20
00329D33  48 8B D0                        mov rdx, rax
00329D36  48 83 C8 42                     or rax, 0x42
00329D3A  F6 C1 42                        test cl, 0x42
00329D3D  48 0F 44 C2                     cmove rax, rdx
00329D41  E9 D7 FD FF FF                  jmp 0x140329b1d
00329D46  B2 02                           mov dl, 2
00329D48  40 0F B6 CD                     movzx ecx, bpl
00329D4C  E8 AB B9 1C 00                  call 0x1404f56fc
00329D51  E9 91 FC FF FF                  jmp 0x1403299e7
00329D56  49 8B D7                        mov rdx, r15
00329D59  E8 96 B7 17 00                  call 0x1404a54f4
00329D5E  85 C0                           test eax, eax
00329D60  0F 84 47 FD FF FF               je 0x140329aad
00329D66  41 8B DD                        mov ebx, r13d
00329D69  49 8B 3F                        mov rdi, qword ptr [r15]
00329D6C  49 8B CF                        mov rcx, r15
00329D6F  E8 FC 3A F5 FF                  call 0x14027d870
00329D74  41 F6 47 0D 01                  test byte ptr [r15 + 0xd], 1
00329D79  48 8B CF                        mov rcx, rdi
00329D7C  41 0F B6 57 0C                  movzx edx, byte ptr [r15 + 0xc]
00329D81  0F 85 AD 02 00 00               jne 0x14032a034
00329D87  E8 04 39 F5 FF                  call 0x14027d690
00329D8C  8B C3                           mov eax, ebx
00329D8E  E9 DC FE FF FF                  jmp 0x140329c6f
00329D93  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
00329D9D  49 8B C1                        mov rax, r9
00329DA0  48 B9 78 FF FF FF 3F 00 00 00   movabs rcx, 0x3fffffff78
00329DAA  48 03 C1                        add rax, rcx
00329DAD  48 3B E8                        cmp rbp, rax
00329DB0  77 0C                           ja 0x140329dbe
00329DB2  49 8B C1                        mov rax, r9
00329DB5  48 3B E8                        cmp rbp, rax
00329DB8  0F 83 2D FE FF FF               jae 0x140329beb
00329DBE  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00329DC8  BB 05 00 00 C0                  mov ebx, 0xc0000005
00329DCD  49 39 06                        cmp qword ptr [r14], rax
00329DD0  0F 82 0E 03 00 00               jb 0x14032a0e4
00329DD6  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00329DDA  4C 8B CE                        mov r9, rsi
00329DDD  49 8B 0E                        mov rcx, qword ptr [r14]
00329DE0  49 8B D5                        mov rdx, r13
00329DE3  E8 08 63 0C 00                  call 0x1403f00f0
00329DE8  4D 89 6E 58                     mov qword ptr [r14 + 0x58], r13
00329DEC  45 33 C0                        xor r8d, r8d
00329DEF  B2 11                           mov dl, 0x11
00329DF1  49 8B CF                        mov rcx, r15
00329DF4  E8 97 34 F5 FF                  call 0x14027d290
00329DF9  81 FB 01 00 00 80               cmp ebx, 0x80000001
00329DFF  75 8B                           jne 0x140329d8c
00329E01  49 8B 0E                        mov rcx, qword ptr [r14]
00329E04  33 D2                           xor edx, edx
00329E06  E8 49 6A 70 00                  call 0x140a30854
00329E0B  8B D8                           mov ebx, eax
00329E0D  E9 5D FE FF FF                  jmp 0x140329c6f
00329E12  E8 81 1B 00 00                  call 0x14032b998
00329E17  48 85 C0                        test rax, rax
00329E1A  0F 84 F8 FD FF FF               je 0x140329c18
00329E20  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00329E27  48 85 C9                        test rcx, rcx
00329E2A  0F 84 E8 FD FF FF               je 0x140329c18
00329E30  48 8B C5                        mov rax, rbp
00329E33  48 C1 E8 03                     shr rax, 3
00329E37  25 FF 01 00 00                  and eax, 0x1ff
00329E3C  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00329E40  A8 20                           test al, 0x20
00329E42  74 04                           je 0x140329e48
00329E44  48 83 CB 20                     or rbx, 0x20
00329E48  48 8B CB                        mov rcx, rbx
00329E4B  48 83 CB 42                     or rbx, 0x42
00329E4F  A8 42                           test al, 0x42
00329E51  48 0F 44 D9                     cmove rbx, rcx
00329E55  E9 BE FD FF FF                  jmp 0x140329c18
00329E5A  45 33 C0                        xor r8d, r8d
00329E5D  B2 11                           mov dl, 0x11
00329E5F  49 8B CF                        mov rcx, r15
00329E62  E8 29 34 F5 FF                  call 0x14027d290
00329E67  80 FB 02                        cmp bl, 2
00329E6A  0F 84 B0 01 00 00               je 0x14032a020
00329E70  8B C7                           mov eax, edi
00329E72  E9 F8 FD FF FF                  jmp 0x140329c6f
00329E77  48 8B D0                        mov rdx, rax
00329E7A  49 8B CE                        mov rcx, r14
00329E7D  E8 32 E2 FF FF                  call 0x1403280b4
00329E82  8B D8                           mov ebx, eax
00329E84  E9 E0 FE FF FF                  jmp 0x140329d69
00329E89  48 85 D2                        test rdx, rdx
00329E8C  0F 84 CC FD FF FF               je 0x140329c5e
00329E92  48 F7 C3 00 0A 00 00            test rbx, 0xa00
00329E99  0F 85 BF FD FF FF               jne 0x140329c5e
00329E9F  E9 1A FF FF FF                  jmp 0x140329dbe
00329EA4  44 0F 20 C3                     mov rbx, cr8
00329EA8  44 0F 22 C1                     mov cr8, rcx
00329EAC  44 39 2D 6D CE C9 00            cmp dword ptr [rip + 0xc9ce6d], r13d
00329EB3  0F 84 74 FB FF FF               je 0x140329a2d
00329EB9  B2 02                           mov dl, 2
00329EBB  0F B6 CB                        movzx ecx, bl
00329EBE  E8 39 B8 1C 00                  call 0x1404f56fc
00329EC3  E9 65 FB FF FF                  jmp 0x140329a2d
00329EC8  BB 0A 00 00 00                  mov ebx, 0xa
00329ECD  8B CB                           mov ecx, ebx
00329ECF  E8 80 91 F7 FF                  call 0x1402a3054
00329ED4  E9 B4 FA FF FF                  jmp 0x14032998d
00329ED9  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00329EE2  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
00329EE9  0F B7 81 8A 00 00 00            movzx eax, word ptr [rcx + 0x8a]
00329EF0  48 69 F8 80 DF 00 00            imul rdi, rax, 0xdf80
00329EF7  49 03 7B 10                     add rdi, qword ptr [r11 + 0x10]
00329EFB  48 8B 8F 08 0F 00 00            mov rcx, qword ptr [rdi + 0xf08]
00329F02  48 8B 97 10 0F 00 00            mov rdx, qword ptr [rdi + 0xf10]
00329F09  48 03 D1                        add rdx, rcx
00329F0C  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00329F14  49 3B D2                        cmp rdx, r10
00329F17  0F 83 70 FA FF FF               jae 0x14032998d
00329F1D  4D 8B E5                        mov r12, r13
00329F20  48 8D 2D 39 7D CE FF            lea rbp, [rip - 0x3182c7]
00329F27  48 83 C7 10                     add rdi, 0x10
00329F2B  41 BF 03 00 00 00               mov r15d, 3
00329F31  48 8B 4F F8                     mov rcx, qword ptr [rdi - 8]
00329F35  48 8B 17                        mov rdx, qword ptr [rdi]
00329F38  48 8D BF 00 05 00 00            lea rdi, [rdi + 0x500]
00329F3F  4C 8B 45 00                     mov r8, qword ptr [rbp]
00329F43  48 8D 6D 08                     lea rbp, [rbp + 8]
00329F47  48 03 D1                        add rdx, rcx
00329F4A  49 0F AF D0                     imul rdx, r8
00329F4E  4C 03 E2                        add r12, rdx
00329F51  49 83 EF 01                     sub r15, 1
00329F55  75 DA                           jne 0x140329f31
00329F57  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00329F5F  4D 8D 7E 38                     lea r15, [r14 + 0x38]
00329F63  49 03 C4                        add rax, r12
00329F66  49 3B C2                        cmp rax, r10
00329F69  0F 82 98 F9 FF FF               jb 0x140329907
00329F6F  E9 19 FA FF FF                  jmp 0x14032998d
00329F74  48 8D 91 E0 04 00 00            lea rdx, [rcx + 0x4e0]
00329F7B  E9 D8 FA FF FF                  jmp 0x140329a58
00329F80  48 8D 86 C0 04 00 00            lea rax, [rsi + 0x4c0]
00329F87  E9 2D FA FF FF                  jmp 0x1403299b9
00329F8C  41 F6 C0 01                     test r8b, 1
00329F90  0F 85 BD 00 00 00               jne 0x14032a053
00329F96  49 8B C8                        mov rcx, r8
00329F99  E8 12 16 02 00                  call 0x14034b5b0
00329F9E  85 C0                           test eax, eax
00329FA0  0F 84 18 FE FF FF               je 0x140329dbe
00329FA6  48 8B C3                        mov rax, rbx
00329FA9  25 00 0C 00 00                  and eax, 0xc00
00329FAE  48 3D 00 08 00 00               cmp rax, 0x800
00329FB4  0F 84 4F 01 00 00               je 0x14032a109
00329FBA  83 E7 0F                        and edi, 0xf
00329FBD  48 81 E3 1F FC FF FF            and rbx, 0xfffffffffffffc1f
00329FC4  48 C1 E7 05                     shl rdi, 5
00329FC8  48 0B FB                        or rdi, rbx
00329FCB  48 89 7D 00                     mov qword ptr [rbp], rdi
00329FCF  48 8B CD                        mov rcx, rbp
00329FD2  BB 01 00 00 80                  mov ebx, 0x80000001
00329FD7  E8 C4 88 F5 FF                  call 0x1402828a0
00329FDC  48 8B C8                        mov rcx, rax
00329FDF  E8 EC 54 F0 FF                  call 0x14022f4d0
00329FE4  85 C0                           test eax, eax
00329FE6  0F 85 00 FE FF FF               jne 0x140329dec
00329FEC  45 8B 4E 08                     mov r9d, dword ptr [r14 + 8]
00329FF0  45 33 C0                        xor r8d, r8d
00329FF3  41 83 E1 02                     and r9d, 2
00329FF7  48 8B D5                        mov rdx, rbp
00329FFA  49 8B CE                        mov rcx, r14
00329FFD  E8 3E BA F8 FF                  call 0x1402b5a40
0032A002  45 33 C0                        xor r8d, r8d
0032A005  B2 11                           mov dl, 0x11
0032A007  49 8B CF                        mov rcx, r15
0032A00A  E8 81 32 F5 FF                  call 0x14027d290
0032A00F  49 8B 0E                        mov rcx, qword ptr [r14]
0032A012  33 D2                           xor edx, edx
0032A014  E8 3B 68 70 00                  call 0x140a30854
0032A019  8B D8                           mov ebx, eax
0032A01B  E9 4F FC FF FF                  jmp 0x140329c6f
0032A020  49 8B 0E                        mov rcx, qword ptr [r14]
0032A023  BA 01 00 00 00                  mov edx, 1
0032A028  E8 27 68 70 00                  call 0x140a30854
0032A02D  8B F8                           mov edi, eax
0032A02F  E9 3C FE FF FF                  jmp 0x140329e70
0032A034  E8 37 4C F5 FF                  call 0x14027ec70
0032A039  8B C3                           mov eax, ebx
0032A03B  E9 2F FC FF FF                  jmp 0x140329c6f
0032A040  48 3B C8                        cmp rcx, rax
0032A043  0F 86 47 FA FF FF               jbe 0x140329a90
0032A049  BB 05 00 00 C0                  mov ebx, 0xc0000005
0032A04E  E9 16 FD FF FF                  jmp 0x140329d69
0032A053  49 8B C0                        mov rax, r8
0032A056  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0032A05A  80 38 01                        cmp byte ptr [rax], 1
0032A05D  0F 84 FB FB FF FF               je 0x140329c5e
0032A063  E9 2E FF FF FF                  jmp 0x140329f96
0032A068  49 8B D6                        mov rdx, r14
0032A06B  E8 38 AB 0A 00                  call 0x1403d4ba8
0032A070  85 C0                           test eax, eax
0032A072  0F 84 45 FA FF FF               je 0x140329abd
0032A078  E9 E9 FC FF FF                  jmp 0x140329d66
0032A07D  BB 1E 00 01 00                  mov ebx, 0x1001e
0032A082  E9 F5 F8 FF FF                  jmp 0x14032997c
0032A087  4C 39 2A                        cmp qword ptr [rdx], r13
0032A08A  0F 84 EA F9 FF FF               je 0x140329a7a
0032A090  4D 3B F0                        cmp r14, r8
0032A093  0F 83 E1 F9 FF FF               jae 0x140329a7a
0032A099  8B CF                           mov ecx, edi
0032A09B  E8 50 20 F5 FF                  call 0x14027c0f0
0032A0A0  49 8B CE                        mov rcx, r14
0032A0A3  E8 28 C8 FE FF                  call 0x1403168d0
0032A0A8  48 85 C0                        test rax, rax
0032A0AB  74 0C                           je 0x14032a0b9
0032A0AD  48 8B C8                        mov rcx, rax
0032A0B0  E8 47 16 1D 00                  call 0x1404fb6fc
0032A0B5  85 C0                           test eax, eax
0032A0B7  74 13                           je 0x14032a0cc
0032A0B9  B2 11                           mov dl, 0x11
0032A0BB  8B CF                           mov ecx, edi
0032A0BD  E8 5E CF F6 FF                  call 0x140297020
0032A0C2  BB 05 00 00 C0                  mov ebx, 0xc0000005
0032A0C7  E9 9D FC FF FF                  jmp 0x140329d69
0032A0CC  B2 11                           mov dl, 0x11
0032A0CE  8B CF                           mov ecx, edi
0032A0D0  E8 4B CF F6 FF                  call 0x140297020
0032A0D5  49 B8 00 00 00 00 00 80 FF FF   movabs r8, 0xffff800000000000
0032A0DF  E9 96 F9 FF FF                  jmp 0x140329a7a
0032A0E4  BF 01 00 00 00                  mov edi, 1
0032A0E9  8B CF                           mov ecx, edi
0032A0EB  E8 00 20 F5 FF                  call 0x14027c0f0
0032A0F0  49 8B 0E                        mov rcx, qword ptr [r14]
0032A0F3  E8 D8 C7 FE FF                  call 0x1403168d0
0032A0F8  B2 11                           mov dl, 0x11
0032A0FA  8B CF                           mov ecx, edi
0032A0FC  4C 8B E8                        mov r13, rax
0032A0FF  E8 1C CF F6 FF                  call 0x140297020
0032A104  E9 CD FC FF FF                  jmp 0x140329dd6
0032A109  45 33 C0                        xor r8d, r8d
0032A10C  33 D2                           xor edx, edx
0032A10E  48 8B CD                        mov rcx, rbp
0032A111  E8 6E B7 0D 00                  call 0x140405884
0032A116  48 8B CD                        mov rcx, rbp
0032A119  48 8B D8                        mov rbx, rax
0032A11C  E8 7F 87 F5 FF                  call 0x1402828a0
0032A121  48 8B D0                        mov rdx, rax
0032A124  48 85 DB                        test rbx, rbx
0032A127  0F 84 53 7D 3B 00               je 0x1406e1e80
0032A12D  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0032A131  44 8B A4 24 88 00 00 00         mov r12d, dword ptr [rsp + 0x88]
0032A139  48 81 E1 1F FC FF FF            and rcx, 0xfffffffffffffc1f
0032A140  45 8B C4                        mov r8d, r12d
0032A143  41 83 E0 0F                     and r8d, 0xf
0032A147  49 C1 E0 05                     shl r8, 5
0032A14B  4C 0B C1                        or r8, rcx
0032A14E  4C 89 43 10                     mov qword ptr [rbx + 0x10], r8
0032A152  E9 29 7D 3B 00                  jmp 0x1406e1e80
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUserFault(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p8;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p98;

    v_rsp = (v_rsp) - (56);
    v_r13 = 0;
    *(unsigned int *)(v_rsp + 16) = 0;
    *(unsigned __int64 *)(a1 + 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    *(unsigned __int64 *)(v_rsp + 24) = 0;
    if ((*(unsigned int *)(v_rip + 11590538)) != 0) goto loc_00329EC8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1360)))) <= 16) goto loc_00329992;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)) & (0x1000ULL)) != 0) goto loc_00329992;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560906) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 1204)))) == -1) goto loc_003298E1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560906) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 1696)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_0032998D;
loc_003298E1:
    if ((*(unsigned __int16 *)(v_rip + 13219607)) > 1) goto loc_00329ED9;
loc_00329907:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 18688)) >= ((unsigned int)(0x420ULL))) goto loc_0032998D;
    result = MiGetCurrentSlabIdentity(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 18688), a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (((unsigned __int8)(result)) == 255) goto loc_00329936;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 18688)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 18304));
    if (a2 >= ((unsigned int)(0x420ULL))) goto loc_0032998D;
loc_00329936:
    v_r10 = ((unsigned int)(0x420ULL)) - (a2);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 19392)) < v_r10) goto loc_00329984;
    a2 = 0;
    result = MiCanFlushMakeProgress(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8), a2, v_r10, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if ((unsigned int)(result) == 0) goto loc_00329984;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1360) = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 144)) >= 9) goto loc_0032A07D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1648)) != 0) goto loc_0032A07D;
loc_0032997C:
    if (2 != 0) {
    }
    if ((unsigned __int16)((unsigned int)(0x101F4ULL)) != 0) goto loc_00329ECD;
loc_0032998D:
loc_00329992:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1208))) & (15));
    if (((unsigned __int8)(result)) >= 6) goto loc_00329EA4;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1208))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_00329F80;
loc_003299B9:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) >> (1));
    v_rbx = (unsigned int)((v_rbx) & (3));
    v_rdi = ((unsigned int)((unsigned int)(v_rbx))) << (6);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 11595399));
    if ((*(unsigned int *)(v_rip + 13226815)) != 0) goto loc_00329D46;
loc_003299E7:
    if (((*(unsigned __int8 *)(v_rip + 13226264)) & (33)) == 0) goto loc_00329C81;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12469342))) != 0) goto loc_00329C81;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rdi, (unsigned __int8)(v_cr8), v_r10, *(unsigned __int64 *)(gs_base + (0 + 392)));
loc_00329A0E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324) = (unsigned int)(v_rbx);
    }
loc_00329A2D:
    *(unsigned __int8 *)(a1 + 56 + 12) = (unsigned __int8)((unsigned __int8)(v_cr8));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1208))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_00329F74;
loc_00329A58:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1208))) >> (24));
    result = (unsigned __int8)((result) & (48));
    if (((unsigned __int8)(result)) == 48) goto loc_0032A087;
loc_00329A7A:
    if ((*(unsigned __int64 *)(a1)) < v_r10) goto loc_0032A040;
loc_00329A90:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 616)) != 0) goto loc_00329D56;
loc_00329AAD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1912) != 0) goto loc_0032A068;
loc_00329ABD:
    result = MiResolvePageTablePage(a1, v_rip + 11595272, v_r10, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (((unsigned int)(result)) == 0xC0000434ULL) goto loc_00329D66;
    if (sign_flag) goto loc_00329D69;
    if ((*(unsigned __int64 *)(a1 + 24)) < v_r10) goto loc_00329B1D;
    if ((*(unsigned __int64 *)(a1 + 24)) > v_r12) goto loc_00329B1D;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))))) == 0) goto loc_00329B26;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_00329CDB;
loc_00329B1D:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))))) != 0) goto loc_00329E77;
loc_00329B26:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (2)) != 0) goto loc_00329CAC;
loc_00329B33:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)) == 0) goto loc_00329B77;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))) >> (5);
    a1 = (unsigned int)((a1) & (31));
    v_stack_p10 = (unsigned int)(a1);
    if (condition_is_above_or_equal) goto loc_00329BC0;
    result = MiCheckProtoAccess(*(unsigned __int64 *)(a1 + 24), v_stack_p10, v_r10, *(unsigned __int64 *)(gs_base + (0 + 392)));
    v_stack_p18 = result;
    if (result != 0) goto loc_00329BB6;
    goto loc_00329D69;
loc_00329B77:
    v_stack_p8 = 0;
    result = MiZeroFault(a1, v_stack_p8, v_stack_p10, v_stack_p18);
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_00329E5A;
loc_00329BB6:
loc_00329BC0:
    if (v_stack_p10 == 256) goto loc_00329C5E;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) & (2));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) >> (8));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00329D93;
loc_00329BEB:
    if ((*(unsigned __int64 *)(a1 + 24)) < v_r10) goto loc_00329C18;
    if ((*(unsigned __int64 *)(a1 + 24)) > v_r12) goto loc_00329C18;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (1)) == 0) goto loc_00329C21;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00329E12;
loc_00329C18:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (1)) != 0) goto loc_00329E89;
loc_00329C21:
    if (a2 != 0) { a2 = 1; }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) & (7));
    result = (unsigned int)(((__int8)(*(unsigned __int8 *)(result + v_rip - 3247056 * 1))) - ((unsigned int)(a2)));
    if (((unsigned int)(result)) < 10) goto loc_00329DBE;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) == 16) goto loc_00329F8C;
loc_00329C5E:
    *(unsigned __int64 *)(a1 + 104) = v_stack_p18;
loc_00329C6F:
    v_rsp = (v_rsp) + (56);
    return (unsigned int)(0xC0000016ULL);
loc_00329C81:
loc_00329C8A:
    if (condition_is_equal) goto loc_00329A0E;
    if (!sign_flag) goto loc_00329C8A;
    result = ExpWaitForSpinLockSharedAndAcquire((unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), (unsigned __int8)(*(unsigned __int64 *)(a1 + 24)), *(unsigned __int64 *)(a1 + 16), v_stack_p18);
    goto loc_00329A0E;
loc_00329CAC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)))) & (16)) == 0) goto loc_00329B33;
    if ((*(unsigned __int64 *)(a1)) >= ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)))) goto loc_00329B33;
    a2 = ((unsigned __int8)(*(unsigned __int64 *)(a1 + 24))) & (-3);
    *(unsigned __int64 *)(a1 + 8) = a2;
    goto loc_00329B33;
loc_00329CDB:
    if (((*(unsigned __int64 *)(v_rip + 13225378)) & (0x600000ULL)) == 0) goto loc_00329B1D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))))) goto loc_00329B1D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00329B1D;
    a1 = (*(unsigned __int64 *)(a1 + 24)) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { result = result; }
    goto loc_00329B1D;
loc_00329D46:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(a1 + 24)), 2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), v_stack_p18);
    goto loc_003299E7;
loc_00329D56:
    result = MiWaitForRotateToComplete((unsigned __int8)(*(unsigned __int64 *)(a1 + 24)), a1 + 56, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), v_stack_p18);
    if ((unsigned int)(result) == 0) goto loc_00329AAD;
loc_00329D66:
loc_00329D69:
    result = MiUnlockFaultPageTable(a1 + 56, a1 + 56, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), v_stack_p18);
    if (((*(unsigned __int8 *)(a1 + 56 + 13)) & (1)) != 0) goto loc_0032A034;
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(a1 + 56), *(unsigned __int8 *)(a1 + 56 + 12), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), v_stack_p18);
loc_00329D8C:
    goto loc_00329C6F;
loc_00329D93:
    result = (v_stack_p18) + (*(unsigned __int64 *)(a1 + 56));
    if ((*(unsigned __int64 *)(a1 + 24)) > result) goto loc_00329DBE;
    if ((*(unsigned __int64 *)(a1 + 24)) >= v_stack_p18) goto loc_00329BEB;
loc_00329DBE:
    if ((*(unsigned __int64 *)(a1)) < v_stack_p18) goto loc_0032A0E4;
loc_00329DD6:
    result = MiCheckFatalAccessViolation(*(unsigned __int64 *)(a1), 0, *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    *(unsigned __int64 *)(a1 + 88) = 0;
loc_00329DEC:
    a3 = 0;
    result = MiReleaseFaultState(a1 + 56, 17, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if (((unsigned int)((unsigned int)(0xC0000005ULL))) != 0x80000001ULL) goto loc_00329D8C;
    a2 = 0;
    result = MiCheckForUserStackOverflow(*(unsigned __int64 *)(a1), a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    goto loc_00329C6F;
loc_00329E12:
    result = MiPteHasShadow(*(unsigned __int64 *)(a1), a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if (result == 0) goto loc_00329C18;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00329C18;
    result = (*(unsigned __int64 *)(a1 + 24)) >> (3);
    result = (unsigned int)((result) & (511));
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = ((unsigned int)((unsigned int)(result))) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_00329C18;
loc_00329E5A:
    a3 = 0;
    result = MiReleaseFaultState(a1 + 56, 17, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0032A020;
loc_00329E70:
    goto loc_00329C6F;
loc_00329E77:
    result = MiValidFault(a1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 56))), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    goto loc_00329D69;
loc_00329E89:
    if ((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 56))) == 0) goto loc_00329C5E;
    if ((((unsigned int)((unsigned int)(result))) & (0xA00ULL)) != 0) goto loc_00329C5E;
    goto loc_00329DBE;
loc_00329EA4:
    if ((*(unsigned int *)(v_rip + 13225581)) == 0) goto loc_00329A2D;
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    goto loc_00329A2D;
loc_00329EC8:
loc_00329ECD:
    result = MiDelayFaultingThread(10, 2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    goto loc_0032998D;
loc_00329ED9:
    v_rdi = (*(unsigned __int64 *)(a1 + 56)) * (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138));
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11560843) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 16));
    a2 = (*(unsigned __int64 *)(v_rdi + 3856)) + (*(unsigned __int64 *)(v_rdi + 3848));
    v_stack_p98 = a2;
    if (a2 >= v_r10) goto loc_0032998D;
    v_rdi = (v_rdi) + (16);
loc_00329F31:
    a2 = (*(unsigned __int64 *)(v_rdi)) + (*(unsigned __int64 *)(v_rdi - 8));
    a2 = (a2) * (*(unsigned __int64 *)(v_rip - 3244743));
    v_r12 = (0) + (a2);
    v_r15 = (3) - (1);
    if (condition_is_not_equal) goto loc_00329F31;
    result = (v_stack_p98) + (v_r12);
    if (result < v_r10) goto loc_00329907;
    goto loc_0032998D;
loc_00329F74:
    goto loc_00329A58;
loc_00329F80:
    goto loc_003299B9;
loc_00329F8C:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3244743))) & (1)) != 0) goto loc_0032A053;
loc_00329F96:
    result = MiAllowGuardFault(*(unsigned __int64 *)(v_rip - 3244743), *(unsigned __int64 *)(v_rdi - 8) + 1248, *(unsigned __int64 *)(v_rip - 3244743), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if ((unsigned int)(result) == 0) goto loc_00329DBE;
    result = (unsigned int)((10) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_0032A109;
    v_rdi = (unsigned int)((v_rdi + 1280) & (15));
    v_rbx = (10) & (-993);
    v_rdi = (v_rdi) << (5);
    v_rdi = (v_rdi) | (v_rbx);
    *(unsigned __int64 *)(v_rip - 3244743 + 8) = v_rdi;
    result = MI_READ_PTE_LOCK_FREE(v_rip - 3244743 + 8, *(unsigned __int64 *)(v_rdi - 8) + 1248, *(unsigned __int64 *)(v_rip - 3244743), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    result = IS_PTE_NOT_DEMAND_ZERO(result, *(unsigned __int64 *)(v_rdi - 8) + 1248, *(unsigned __int64 *)(v_rip - 3244743), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if ((unsigned int)(result) != 0) goto loc_00329DEC;
    a3 = 0;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) & (2));
    result = MiResolveDemandZeroFault(a1, v_rip - 3244743 + 8, a3, a4);
    a3 = 0;
    result = MiReleaseFaultState(a1 + 56, 17, a3, a4);
    a2 = 0;
    result = MiCheckForUserStackOverflow(*(unsigned __int64 *)(a1), a2, a3, a4);
    goto loc_00329C6F;
loc_0032A020:
    result = MiCheckForUserStackOverflow(*(unsigned __int64 *)(a1), 1, a3, a4);
    goto loc_00329E70;
loc_0032A034:
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(a1), 1, a3, a4);
    goto loc_00329C6F;
loc_0032A040:
    if ((*(unsigned __int64 *)(a1)) <= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) goto loc_00329A90;
    goto loc_00329D69;
loc_0032A053:
    result = (0) & (-2);
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_00329C5E;
    goto loc_00329F96;
loc_0032A068:
    result = MiCheckHoldFaultForHotPatch(*(unsigned __int64 *)(a1), a1, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00329ABD;
    goto loc_00329D66;
loc_0032A07D:
    goto loc_0032997C;
loc_0032A087:
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_00329A7A;
    if (a1 >= 0) goto loc_00329A7A;
    result = MiLockVadTree((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a1, a3, a4);
    result = MiLocateAddress(a1, a1, a3, a4);
    if (result == 0) goto loc_0032A0B9;
    result = MiIsVadEligibleForCommitRelease(result, a1, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0032A0CC;
loc_0032A0B9:
    result = MiUnlockVadTree((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 17, a3, a4);
    goto loc_00329D69;
loc_0032A0CC:
    result = MiUnlockVadTree((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 17, a3, a4);
    goto loc_00329A7A;
loc_0032A0E4:
    result = MiLockVadTree(1, 17, a3, a4);
    result = MiLocateAddress(*(unsigned __int64 *)(a1), 17, a3, a4);
    result = MiUnlockVadTree(1, 17, a3, a4);
    goto loc_00329DD6;
loc_0032A109:
    a3 = 0;
    a2 = 0;
    result = MiLockTransitionLeafPageEx(v_rip - 3244743 + 8, a2, a3, a4);
    result = MI_READ_PTE_LOCK_FREE(v_rip - 3244743 + 8, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(result + 16)) & (-993);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p88)))) & (15));
    a3 = (a3) << (5);
    a3 = (a3) | (a1);
    *(unsigned __int64 *)(result + 16) = a3;
}
```

## 5. (Beta) C Style

```c
int64_t MiUserFault(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p8;
    uint32_t v_stack_p88;
    uint64_t v_stack_p98;

    local_rsp = (local_rsp) - (56);
    local_r13 = 0;
    *(uint32_t *)(local_rsp + 0x10) = 0;
    *(uint64_t *)(arg1 + 0x38) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    *(uint64_t *)(local_rsp + 0x18) = 0;
    if ((*(uint32_t *)(v_rip + 0xB0DB8A)) != 0) goto loc_00329EC8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x550)))) <= 16) goto loc_00329992;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)) & (0x1000ULL)) != 0) goto loc_00329992;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB067CA) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x4B4)))) == -1) goto loc_003298E1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB067CA) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x6A0)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_0032998D;
loc_003298E1:
    if ((*(uint16_t *)(v_rip + 0xC9B717)) > 1) goto loc_00329ED9;
loc_00329907:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x4900)) >= ((uint32_t)(0x420ULL))) goto loc_0032998D;
    result = MiGetCurrentSlabIdentity(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x4900), a3, *(uint64_t *)(gs_base + (0 + 0x188)));
    if (((uint8_t)(result)) == 255) goto loc_00329936;
    a2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x4900)) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x4780));
    if (a2 >= ((uint32_t)(0x420ULL))) goto loc_0032998D;
loc_00329936:
    local_r10 = ((uint32_t)(0x420ULL)) - (a2);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x4BC0)) < local_r10) goto loc_00329984;
    a2 = 0;
    result = MiCanFlushMakeProgress(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8), a2, local_r10, *(uint64_t *)(gs_base + (0 + 0x188)));
    if ((uint32_t)(result) == 0) goto loc_00329984;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x550) = 0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x90)) >= 9) goto loc_0032A07D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x670)) != 0) goto loc_0032A07D;
loc_0032997C:
    if (2 != 0) {
    }
    if ((uint16_t)((uint32_t)(0x101F4ULL)) != 0) goto loc_00329ECD;
loc_0032998D:
loc_00329992:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4B8))) & (15));
    if (((uint8_t)(result)) >= 6) goto loc_00329EA4;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4B8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_00329F80;
loc_003299B9:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) >> (1));
    local_rbx = (uint32_t)((local_rbx) & (3));
    local_rdi = ((uint32_t)((uint32_t)(local_rbx))) << (6);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xB0EE87));
    if ((*(uint32_t *)(v_rip + 0xC9D33F)) != 0) goto loc_00329D46;
loc_003299E7:
    if (((*(uint8_t *)(v_rip + 0xC9D118)) & (33)) == 0) goto loc_00329C81;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE445E))) != 0) goto loc_00329C81;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(local_rdi, (uint8_t)(v_cr8), local_r10, *(uint64_t *)(gs_base + (0 + 0x188)));
loc_00329A0E:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) != 0) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144) = (uint32_t)(local_rbx);
    }
loc_00329A2D:
    *(uint8_t *)(arg1 + 0x38 + 0xC) = (uint8_t)((uint8_t)(v_cr8));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4B8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_00329F74;
loc_00329A58:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4B8))) >> (24));
    result = (uint8_t)((result) & (48));
    if (((uint8_t)(result)) == 48) goto loc_0032A087;
loc_00329A7A:
    if ((*(uint64_t *)(arg1)) < local_r10) goto loc_0032A040;
loc_00329A90:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x268)) != 0) goto loc_00329D56;
loc_00329AAD:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x778) != 0) goto loc_0032A068;
loc_00329ABD:
    result = MiResolvePageTablePage(Arg1, v_rip + 11595272, local_r10, *(uint64_t *)(gs_base + (0 + 0x188)));
    if (((uint32_t)(result)) == 0xC0000434ULL) goto loc_00329D66;
    if (sign_flag) goto loc_00329D69;
    if ((*(uint64_t *)(arg1 + 0x18)) < local_r10) goto loc_00329B1D;
    if ((*(uint64_t *)(arg1 + 0x18)) > local_r12) goto loc_00329B1D;
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18))))) == 0) goto loc_00329B26;
    a2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(a2))) == 0) goto loc_00329CDB;
loc_00329B1D:
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18))))) != 0) goto loc_00329E77;
loc_00329B26:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x8))) & (2)) != 0) goto loc_00329CAC;
loc_00329B33:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)) == 0) goto loc_00329B77;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18))) >> (5);
    Arg1 = (uint32_t)((Arg1) & (31));
    v_stack_p10 = (uint32_t)(Arg1);
    if (condition_is_above_or_equal) goto loc_00329BC0;
    result = MiCheckProtoAccess(*(uint64_t *)(arg1 + 0x18), v_stack_p10, local_r10, *(uint64_t *)(gs_base + (0 + 0x188)));
    v_stack_p18 = result;
    if (result != 0) goto loc_00329BB6;
    goto loc_00329D69;
loc_00329B77:
    v_stack_p8 = 0;
    result = MiZeroFault(Arg1, v_stack_p8, v_stack_p10, v_stack_p18);
    if ((uint8_t)(v_stack_p8) != 0) goto loc_00329E5A;
loc_00329BB6:
loc_00329BC0:
    if (v_stack_p10 == 256) goto loc_00329C5E;
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) & (2));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) >> (8));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00329D93;
loc_00329BEB:
    if ((*(uint64_t *)(arg1 + 0x18)) < local_r10) goto loc_00329C18;
    if ((*(uint64_t *)(arg1 + 0x18)) > local_r12) goto loc_00329C18;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (1)) == 0) goto loc_00329C21;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00329E12;
loc_00329C18:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (1)) != 0) goto loc_00329E89;
loc_00329C21:
    if (a2 != 0) { a2 = 1; }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) & (7));
    result = (uint32_t)(((int8_t)(*(uint8_t *)(result + v_rip - 0x318BD0 * 1))) - ((uint32_t)(a2)));
    if (((uint32_t)(result)) < 10) goto loc_00329DBE;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) == 16) goto loc_00329F8C;
loc_00329C5E:
    *(uint64_t *)(arg1 + 0x68) = v_stack_p18;
loc_00329C6F:
    local_rsp = (local_rsp) + (56);
    return (uint32_t)(0xC0000016ULL);
loc_00329C81:
loc_00329C8A:
    if (condition_is_equal) goto loc_00329A0E;
    if (!sign_flag) goto loc_00329C8A;
    result = ExpWaitForSpinLockSharedAndAcquire((uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), (uint8_t)(*(uint64_t *)(arg1 + 0x18)), *(uint64_t *)(arg1 + 0x10), v_stack_p18);
    goto loc_00329A0E;
loc_00329CAC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)))) & (16)) == 0) goto loc_00329B33;
    if ((*(uint64_t *)(arg1)) >= ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)))) goto loc_00329B33;
    a2 = ((uint8_t)(*(uint64_t *)(arg1 + 0x18))) & (-3);
    *(uint64_t *)(arg1 + 0x8) = a2;
    goto loc_00329B33;
loc_00329CDB:
    if (((*(uint64_t *)(v_rip + 0xC9CDA2)) & (0x600000ULL)) == 0) goto loc_00329B1D;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))))) goto loc_00329B1D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00329B1D;
    Arg1 = (*(uint64_t *)(arg1 + 0x18)) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { result = result; }
    goto loc_00329B1D;
loc_00329D46:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(arg1 + 0x18)), 2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), v_stack_p18);
    goto loc_003299E7;
loc_00329D56:
    result = MiWaitForRotateToComplete((uint8_t)(*(uint64_t *)(arg1 + 0x18)), Arg1 + 56, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), v_stack_p18);
    if ((uint32_t)(result) == 0) goto loc_00329AAD;
loc_00329D66:
loc_00329D69:
    result = MiUnlockFaultPageTable(Arg1 + 56, Arg1 + 56, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), v_stack_p18);
    if (((*(uint8_t *)(arg1 + 0x38 + 0xD)) & (1)) != 0) goto loc_0032A034;
    result = MiUnlockWorkingSetShared(*(uint64_t *)(arg1 + 0x38), *(uint8_t *)(arg1 + 0x38 + 0xC), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), v_stack_p18);
loc_00329D8C:
    goto loc_00329C6F;
loc_00329D93:
    result = (v_stack_p18) + (*(uint64_t *)(arg1 + 0x38));
    if ((*(uint64_t *)(arg1 + 0x18)) > result) goto loc_00329DBE;
    if ((*(uint64_t *)(arg1 + 0x18)) >= v_stack_p18) goto loc_00329BEB;
loc_00329DBE:
    if ((*(uint64_t *)(arg1)) < v_stack_p18) goto loc_0032A0E4;
loc_00329DD6:
    result = MiCheckFatalAccessViolation(*(uint64_t *)(arg1), 0, *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    *(uint64_t *)(arg1 + 0x58) = 0;
loc_00329DEC:
    a3 = 0;
    result = MiReleaseFaultState(Arg1 + 56, 17, a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if (((uint32_t)((uint32_t)(0xC0000005ULL))) != 0x80000001ULL) goto loc_00329D8C;
    a2 = 0;
    result = MiCheckForUserStackOverflow(*(uint64_t *)(arg1), a2, a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    goto loc_00329C6F;
loc_00329E12:
    result = MiPteHasShadow(*(uint64_t *)(arg1), a2, a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if (result == 0) goto loc_00329C18;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00329C18;
    result = (*(uint64_t *)(arg1 + 0x18)) >> (3);
    result = (uint32_t)((result) & (511));
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = ((uint32_t)((uint32_t)(result))) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_00329C18;
loc_00329E5A:
    a3 = 0;
    result = MiReleaseFaultState(Arg1 + 56, 17, a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0032A020;
loc_00329E70:
    goto loc_00329C6F;
loc_00329E77:
    result = MiValidFault(Arg1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x38))), a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    goto loc_00329D69;
loc_00329E89:
    if ((uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x38))) == 0) goto loc_00329C5E;
    if ((((uint32_t)((uint32_t)(result))) & (0xA00ULL)) != 0) goto loc_00329C5E;
    goto loc_00329DBE;
loc_00329EA4:
    if ((*(uint32_t *)(v_rip + 0xC9CE6D)) == 0) goto loc_00329A2D;
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    goto loc_00329A2D;
loc_00329EC8:
loc_00329ECD:
    result = MiDelayFaultingThread(10, 2, a3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    goto loc_0032998D;
loc_00329ED9:
    local_rdi = (*(uint64_t *)(arg1 + 0x38)) * (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A));
    local_rdi = (local_rdi) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0678B) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x10));
    a2 = (*(uint64_t *)(local_rdi + 0xF10)) + (*(uint64_t *)(local_rdi + 0xF08));
    v_stack_p98 = a2;
    if (a2 >= local_r10) goto loc_0032998D;
    local_rdi = (local_rdi) + (16);
loc_00329F31:
    a2 = (*(uint64_t *)(local_rdi)) + (*(uint64_t *)(local_rdi - 0x8));
    a2 = (a2) * (*(uint64_t *)(v_rip - 0x3182C7));
    local_r12 = (0) + (a2);
    local_r15 = (3) - (1);
    if (condition_is_not_equal) goto loc_00329F31;
    result = (v_stack_p98) + (local_r12);
    if (result < local_r10) goto loc_00329907;
    goto loc_0032998D;
loc_00329F74:
    goto loc_00329A58;
loc_00329F80:
    goto loc_003299B9;
loc_00329F8C:
    if ((((uint8_t)(*(uint64_t *)(v_rip - 0x3182C7))) & (1)) != 0) goto loc_0032A053;
loc_00329F96:
    result = MiAllowGuardFault(*(uint64_t *)(v_rip - 0x3182C7), *(uint64_t *)(local_rdi - 0x8) + 1248, *(uint64_t *)(v_rip - 0x3182C7), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if ((uint32_t)(result) == 0) goto loc_00329DBE;
    result = (uint32_t)((10) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_0032A109;
    local_rdi = (uint32_t)((local_rdi + 1280) & (15));
    local_rbx = (10) & (-993);
    local_rdi = (local_rdi) << (5);
    local_rdi = (local_rdi) | (local_rbx);
    *(uint64_t *)(v_rip - 0x3182C7 + 0x8) = local_rdi;
    result = MI_READ_PTE_LOCK_FREE(v_rip - 3244743 + 8, *(uint64_t *)(local_rdi - 0x8) + 1248, *(uint64_t *)(v_rip - 0x3182C7), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    result = IS_PTE_NOT_DEMAND_ZERO(result, *(uint64_t *)(local_rdi - 0x8) + 1248, *(uint64_t *)(v_rip - 0x3182C7), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if ((uint32_t)(result) != 0) goto loc_00329DEC;
    a3 = 0;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) & (2));
    result = MiResolveDemandZeroFault(Arg1, v_rip - 3244743 + 8, a3, a4);
    a3 = 0;
    result = MiReleaseFaultState(Arg1 + 56, 17, a3, a4);
    a2 = 0;
    result = MiCheckForUserStackOverflow(*(uint64_t *)(arg1), a2, a3, a4);
    goto loc_00329C6F;
loc_0032A020:
    result = MiCheckForUserStackOverflow(*(uint64_t *)(arg1), 1, a3, a4);
    goto loc_00329E70;
loc_0032A034:
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(arg1), 1, a3, a4);
    goto loc_00329C6F;
loc_0032A040:
    if ((*(uint64_t *)(arg1)) <= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) goto loc_00329A90;
    goto loc_00329D69;
loc_0032A053:
    result = (0) & (-2);
    if ((*(uint8_t *)(result)) == 1) goto loc_00329C5E;
    goto loc_00329F96;
loc_0032A068:
    result = MiCheckHoldFaultForHotPatch(*(uint64_t *)(arg1), Arg1, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00329ABD;
    goto loc_00329D66;
loc_0032A07D:
    goto loc_0032997C;
loc_0032A087:
    if ((*(uint64_t *)(arg1)) == 0) goto loc_00329A7A;
    if (Arg1 >= 0) goto loc_00329A7A;
    result = MiLockVadTree((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg1, a3, a4);
    result = MiLocateAddress(Arg1, Arg1, a3, a4);
    if (result == 0) goto loc_0032A0B9;
    result = MiIsVadEligibleForCommitRelease(result, Arg1, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0032A0CC;
loc_0032A0B9:
    result = MiUnlockVadTree((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 17, a3, a4);
    goto loc_00329D69;
loc_0032A0CC:
    result = MiUnlockVadTree((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 17, a3, a4);
    goto loc_00329A7A;
loc_0032A0E4:
    result = MiLockVadTree(1, 17, a3, a4);
    result = MiLocateAddress(*(uint64_t *)(arg1), 17, a3, a4);
    result = MiUnlockVadTree(1, 17, a3, a4);
    goto loc_00329DD6;
loc_0032A109:
    a3 = 0;
    a2 = 0;
    result = MiLockTransitionLeafPageEx(v_rip - 3244743 + 8, a2, a3, a4);
    result = MI_READ_PTE_LOCK_FREE(v_rip - 3244743 + 8, a2, a3, a4);
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-993);
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p88)))) & (15));
    a3 = (a3) << (5);
    a3 = (a3) | (Arg1);
    *(uint64_t *)(result + 0x10) = a3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `W` |
| `Arg1` | `+ 0xD` | `8` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00329840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
