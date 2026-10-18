# MmDuplicateMemory

- RVA: `0x00B74158`–`0x00B74572` (길이 `1,050` bytes)
- VA: `0x0000000140B74158`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7D44`
- 디코드: `288`개 명령, `1,050/1,050` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x00B741F0` → [CcNotifyWriteBehind](../../text/57/CcNotifyWriteBehind_function_0057BA4C.md) (function, `0x0057BA4C`)
- `0x00B7423A` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00B74267` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (function, `0x00A4D1E0`)
- `0x00B74280` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00B742AB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00B742C3` → [MiLockDynamicMemoryShared](../../text/3B/MiLockDynamicMemoryShared_function_003B8AA8.md) (function, `0x003B8AA8`)
- `0x00B742DA` → [MiUpdateMirrorBitmaps](../../page/AD/MiUpdateMirrorBitmaps_function_00ADA220.md) (function, `0x00ADA220`)
- `0x00B74306` → [MiActOnMirrorBitmap](../../page/AC/MiActOnMirrorBitmap_function_00AC21D0.md) (function, `0x00AC21D0`)
- `0x00B7434B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7436A` → [MiMirrorBrownPhase](MiMirrorBrownPhase_function_00B7C6B4.md) (function, `0x00B7C6B4`)
- `0x00B7439B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B743C0` → [MiActOnMirrorBitmap](../../page/AC/MiActOnMirrorBitmap_function_00AC21D0.md) (function, `0x00AC21D0`)
- `0x00B743E5` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00B743ED` → [MiLockAllMemoryLists](../../text/47/MiLockAllMemoryLists_function_0047FBD8.md) (function, `0x0047FBD8`)
- `0x00B74412` → [MiMirrorBlackPhase](../../text/67/MiMirrorBlackPhase_function_00678B4C.md) (function, `0x00678B4C`)
- `0x00B74422` → [MiMirrorVerify](../../text/67/MiMirrorVerify_function_00678C84.md) (function, `0x00678C84`)
- `0x00B7443A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B74453` → [MiResumeFromHibernate](../../text/67/MiResumeFromHibernate_function_00678EC0.md) (function, `0x00678EC0`)
- `0x00B74492` → [MiUnlockAllMemoryLists](../../text/68/MiUnlockAllMemoryLists_function_0068B820.md) (function, `0x0068B820`)
- `0x00B744A8` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B744CD` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00B744E7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00B744F6` → [MiUnlockDynamicMemoryShared](../../text/3B/MiUnlockDynamicMemoryShared_function_003B8A48.md) (function, `0x003B8A48`)
- `0x00B74514` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00B74520` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B7453D` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00B74552` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (function, `0x002A39F0`)

### Direct callers
- [IopLiveDumpCapture](../../text/59/IopLiveDumpCapture_function_0059AF88.md) at `0x0059B009`
- [MmCreateMirror](../../page/7F/MmCreateMirror_function_007FCB50.md) at `0x007FCC14`
- [PnprInitiateReplaceOperation](../B6/PnprInitiateReplaceOperation_function_00B64034.md) at `0x00B641DE`
- [sub_00B8053E](../B8/Unknown_function_00B8053E.md) at `0x00B80638`

### Static image references
- `0x00B7422F` → RVA `0x00E30150` (`.data`; read)
- `0x00B74257` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00B74260` → RVA `0x00FC6C00` (`ALMOSTRO`; read)
- `0x00B74273` → RVA `0x00E30048` (`.data`; read)
- `0x00B742BC` → RVA `0x00E38D00` (`.data`; read)
- `0x00B742C8` → RVA `0x00E37610` (`.data`; read/write)
- `0x00B742D1` → RVA `0x00E30188` (`.data`; write)
- `0x00B742FF` → RVA `0x00E301A0` (`.data`; read)
- `0x00B74360` → RVA `0x00E3014C` (`.data`; write)
- `0x00B74389` → RVA `0x00E37418` (`.data`; read/write)
- `0x00B743B9` → RVA `0x00E30190` (`.data`; read)
- `0x00B743D9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B744BD` → RVA `0x00E30168` (`.data`; read)
- `0x00B744C6` → RVA `0x00E30180` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x00B741F0` → [CcNotifyWriteBehind](../../text/57/CcNotifyWriteBehind_function_0057BA4C.md) (`PAGELK` → `.text`)
  - `0x00B7423A` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGELK` → `.text`)
  - `0x00B74267` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (`PAGELK` → `PAGE`)
  - `0x00B74280` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGELK` → `.text`)
  - `0x00B742AB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGELK` → `.text`)
  - `0x00B742C3` → [MiLockDynamicMemoryShared](../../text/3B/MiLockDynamicMemoryShared_function_003B8AA8.md) (`PAGELK` → `.text`)
  - `0x00B742DA` → [MiUpdateMirrorBitmaps](../../page/AD/MiUpdateMirrorBitmaps_function_00ADA220.md) (`PAGELK` → `PAGE`)
  - `0x00B74306` → [MiActOnMirrorBitmap](../../page/AC/MiActOnMirrorBitmap_function_00AC21D0.md) (`PAGELK` → `PAGE`)
  - `0x00B7434B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7439B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B743C0` → [MiActOnMirrorBitmap](../../page/AC/MiActOnMirrorBitmap_function_00AC21D0.md) (`PAGELK` → `PAGE`)
  - `0x00B743E5` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGELK` → `.text`)
  - `0x00B743ED` → [MiLockAllMemoryLists](../../text/47/MiLockAllMemoryLists_function_0047FBD8.md) (`PAGELK` → `.text`)
  - `0x00B74412` → [MiMirrorBlackPhase](../../text/67/MiMirrorBlackPhase_function_00678B4C.md) (`PAGELK` → `.text`)
  - `0x00B74422` → [MiMirrorVerify](../../text/67/MiMirrorVerify_function_00678C84.md) (`PAGELK` → `.text`)
  - `0x00B7443A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B74453` → [MiResumeFromHibernate](../../text/67/MiResumeFromHibernate_function_00678EC0.md) (`PAGELK` → `.text`)
  - `0x00B74492` → [MiUnlockAllMemoryLists](../../text/68/MiUnlockAllMemoryLists_function_0068B820.md) (`PAGELK` → `.text`)
  - `0x00B744A8` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGELK` → `.text`)
  - `0x00B744CD` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGELK` → `.text`)
  - `0x00B744E7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGELK` → `.text`)
  - `0x00B744F6` → [MiUnlockDynamicMemoryShared](../../text/3B/MiUnlockDynamicMemoryShared_function_003B8A48.md) (`PAGELK` → `.text`)
  - `0x00B74514` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGELK` → `.text`)
  - `0x00B74520` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGELK` → `.text`)
  - `0x00B7453D` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGELK` → `.text`)
  - `0x00B74552` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B74158  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00B7415D  55                              push rbp
00B7415E  56                              push rsi
00B7415F  57                              push rdi
00B74160  41 54                           push r12
00B74162  41 55                           push r13
00B74164  41 56                           push r14
00B74166  41 57                           push r15
00B74168  48 8B EC                        mov rbp, rsp
00B7416B  48 83 EC 50                     sub rsp, 0x50
00B7416F  33 FF                           xor edi, edi
00B74171  4C 8B F1                        mov r14, rcx
00B74174  33 C0                           xor eax, eax
00B74176  48 89 7D 40                     mov qword ptr [rbp + 0x40], rdi
00B7417A  0F 57 C0                        xorps xmm0, xmm0
00B7417D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00B74181  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00B74185  41 8B 56 20                     mov edx, dword ptr [r14 + 0x20]
00B74189  8D 4F 11                        lea ecx, [rdi + 0x11]
00B7418C  8D 5F 01                        lea ebx, [rdi + 1]
00B7418F  89 55 E8                        mov dword ptr [rbp - 0x18], edx
00B74192  44 8A E1                        mov r12b, cl
00B74195  44 8A F9                        mov r15b, cl
00B74198  84 D3                           test bl, dl
00B7419A  74 08                           je 0x140b741a4
00B7419C  F7 C2 04 04 00 00               test edx, 0x404
00B741A2  75 37                           jne 0x140b741db
00B741A4  F6 C2 08                        test dl, 8
00B741A7  74 09                           je 0x140b741b2
00B741A9  81 E2 FA FB FF FF               and edx, 0xfffffbfa
00B741AF  89 55 E8                        mov dword ptr [rbp - 0x18], edx
00B741B2  0F BA E2 0A                     bt edx, 0xa
00B741B6  73 05                           jae 0x140b741bd
00B741B8  F6 C2 04                        test dl, 4
00B741BB  75 1E                           jne 0x140b741db
00B741BD  F6 C2 C0                        test dl, 0xc0
00B741C0  74 23                           je 0x140b741e5
00B741C2  F7 C2 2E FC FF FF               test edx, 0xfffffc2e
00B741C8  75 11                           jne 0x140b741db
00B741CA  8B C2                           mov eax, edx
00B741CC  23 C1                           and eax, ecx
00B741CE  3A C1                           cmp al, cl
00B741D0  75 09                           jne 0x140b741db
00B741D2  F6 C2 40                        test dl, 0x40
00B741D5  74 0E                           je 0x140b741e5
00B741D7  84 D2                           test dl, dl
00B741D9  79 0A                           jns 0x140b741e5
00B741DB  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B741E0  E9 74 03 00 00                  jmp 0x140b74559
00B741E5  0F BA E2 0B                     bt edx, 0xb
00B741E9  72 0A                           jb 0x140b741f5
00B741EB  F6 C2 0A                        test dl, 0xa
00B741EE  75 05                           jne 0x140b741f5
00B741F0  E8 57 78 A0 FF                  call 0x14057ba4c
00B741F5  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
00B741F9  44 8B EF                        mov r13d, edi
00B741FC  C7 45 EC 08 00 00 00            mov dword ptr [rbp - 0x14], 8
00B74203  40 88 7D F4                     mov byte ptr [rbp - 0xc], dil
00B74207  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00B74210  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
00B74213  25 00 02 00 00                  and eax, 0x200
00B74218  F7 D8                           neg eax
00B7421A  48 8D 45 40                     lea rax, [rbp + 0x40]
00B7421E  48 1B C9                        sbb rcx, rcx
00B74221  45 33 C9                        xor r9d, r9d
00B74224  48 23 C8                        and rcx, rax
00B74227  45 33 C0                        xor r8d, r8d
00B7422A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B7422F  48 8D 0D 1A BF 2B 00            lea rcx, [rip + 0x2bbf1a]
00B74236  41 8D 51 12                     lea edx, [r9 + 0x12]
00B7423A  E8 71 A4 69 FF                  call 0x14020e6b0
00B7423F  85 C0                           test eax, eax
00B74241  0F 88 12 03 00 00               js 0x140b74559
00B74247  B9 02 01 00 00                  mov ecx, 0x102
00B7424C  3B C1                           cmp eax, ecx
00B7424E  75 07                           jne 0x140b74257
00B74250  8B C1                           mov eax, ecx
00B74252  E9 02 03 00 00                  jmp 0x140b74559
00B74257  F6 05 2A 28 45 00 04            test byte ptr [rip + 0x45282a], 4
00B7425E  75 0C                           jne 0x140b7426c
00B74260  48 8B 0D 99 29 45 00            mov rcx, qword ptr [rip + 0x452999]
00B74267  E8 74 8F ED FF                  call 0x140a4d1e0
00B7426C  66 29 9E E6 01 00 00            sub word ptr [rsi + 0x1e6], bx
00B74273  48 8D 0D CE BD 2B 00            lea rcx, [rip + 0x2bbdce]
00B7427A  45 33 C0                        xor r8d, r8d
00B7427D  33 D2                           xor edx, edx
00B7427F  90                              nop
00B74280  E8 AB BF 69 FF                  call 0x140210230
00B74285  48 8B D8                        mov rbx, rax
00B74288  33 C0                           xor eax, eax
00B7428A  8D 48 11                        lea ecx, [rax + 0x11]
00B7428D  F0 48 0F B1 0D B2 BD 2B 00      lock cmpxchg qword ptr [rip + 0x2bbdb2], rcx
00B74296  74 18                           je 0x140b742b0
00B74298  4C 8D 0D A9 BD 2B 00            lea r9, [rip + 0x2bbda9]
00B7429F  4C 8B C3                        mov r8, rbx
00B742A2  33 D2                           xor edx, edx
00B742A4  48 8D 0D 9D BD 2B 00            lea rcx, [rip + 0x2bbd9d]
00B742AB  E8 9C C1 69 FF                  call 0x14021044c
00B742B0  48 85 DB                        test rbx, rbx
00B742B3  74 04                           je 0x140b742b9
00B742B5  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00B742B9  48 8B D6                        mov rdx, rsi
00B742BC  48 8D 0D 3D 4A 2C 00            lea rcx, [rip + 0x2c4a3d]
00B742C3  E8 E0 47 84 FF                  call 0x1403b8aa8
00B742C8  F0 FF 05 41 33 2C 00            lock inc dword ptr [rip + 0x2c3341]
00B742CF  33 D2                           xor edx, edx
00B742D1  48 89 35 B0 BE 2B 00            mov qword ptr [rip + 0x2bbeb0], rsi
00B742D8  33 C9                           xor ecx, ecx
00B742DA  E8 41 5F F6 FF                  call 0x140ada220
00B742DF  33 DB                           xor ebx, ebx
00B742E1  BF 02 00 00 00                  mov edi, 2
00B742E6  85 C0                           test eax, eax
00B742E8  75 10                           jne 0x140b742fa
00B742EA  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00B742EF  44 8D 77 FF                     lea r14d, [rdi - 1]
00B742F3  33 C9                           xor ecx, ecx
00B742F5  E9 70 01 00 00                  jmp 0x140b7446a
00B742FA  BA 01 00 00 00                  mov edx, 1
00B742FF  48 8D 0D 9A BE 2B 00            lea rcx, [rip + 0x2bbe9a]
00B74306  E8 C5 DE F4 FF                  call 0x140ac21d0
00B7430B  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
00B7430E  BF 01 00 00 00                  mov edi, 1
00B74313  89 5D F0                        mov dword ptr [rbp - 0x10], ebx
00B74316  40 84 C7                        test dil, al
00B74319  74 09                           je 0x140b74324
00B7431B  C7 45 F0 03 00 00 00            mov dword ptr [rbp - 0x10], 3
00B74322  EB 22                           jmp 0x140b74346
00B74324  0F BA E0 0A                     bt eax, 0xa
00B74328  72 11                           jb 0x140b7433b
00B7432A  A8 04                           test al, 4
00B7432C  74 09                           je 0x140b74337
00B7432E  C7 45 EC 07 00 00 00            mov dword ptr [rbp - 0x14], 7
00B74335  EB 07                           jmp 0x140b7433e
00B74337  A8 08                           test al, 8
00B74339  74 0D                           je 0x140b74348
00B7433B  89 5D EC                        mov dword ptr [rbp - 0x14], ebx
00B7433E  B8 02 00 00 00                  mov eax, 2
00B74343  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00B74346  8B FB                           mov edi, ebx
00B74348  49 8B 06                        mov rax, qword ptr [r14]
00B7434B  E8 80 67 B4 FF                  call 0x1406baad0
00B74350  33 C9                           xor ecx, ecx
00B74352  8B D8                           mov ebx, eax
00B74354  85 C0                           test eax, eax
00B74356  0F 88 03 01 00 00               js 0x140b7445f
00B7435C  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00B74360  C7 05 E2 BD 2B 00 01 00 00 00   mov dword ptr [rip + 0x2bbde2], 1
00B7436A  E8 45 83 00 00                  call 0x140b7c6b4
00B7436F  33 C9                           xor ecx, ecx
00B74371  8B D8                           mov ebx, eax
00B74373  85 C0                           test eax, eax
00B74375  0F 88 E4 00 00 00               js 0x140b7445f
00B7437B  F7 45 E8 02 08 00 00            test dword ptr [rbp - 0x18], 0x802
00B74382  75 0F                           jne 0x140b74393
00B74384  38 4D F4                        cmp byte ptr [rbp - 0xc], cl
00B74387  74 0A                           je 0x140b74393
00B74389  F0 FF 0D 88 30 2C 00            lock dec dword ptr [rip + 0x2c3088]
00B74390  88 4D F4                        mov byte ptr [rbp - 0xc], cl
00B74393  45 0F 20 C4                     mov r12, cr8
00B74397  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00B7439B  E8 30 67 B4 FF                  call 0x1406baad0
00B743A0  33 C9                           xor ecx, ecx
00B743A2  8B D8                           mov ebx, eax
00B743A4  85 C0                           test eax, eax
00B743A6  0F 88 B3 00 00 00               js 0x140b7445f
00B743AC  45 0F 20 C7                     mov r15, cr8
00B743B0  49 39 4E 18                     cmp qword ptr [r14 + 0x18], rcx
00B743B4  74 11                           je 0x140b743c7
00B743B6  8D 51 01                        lea edx, [rcx + 1]
00B743B9  48 8D 0D D0 BD 2B 00            lea rcx, [rip + 0x2bbdd0]
00B743C0  E8 0B DE F4 FF                  call 0x140ac21d0
00B743C5  33 C9                           xor ecx, ecx
00B743C7  B8 02 00 00 00                  mov eax, 2
00B743CC  44 3A F8                        cmp r15b, al
00B743CF  73 1C                           jae 0x140b743ed
00B743D1  44 0F 20 C3                     mov rbx, cr8
00B743D5  44 0F 22 C0                     mov cr8, rax
00B743D9  39 0D 41 29 45 00               cmp dword ptr [rip + 0x452941], ecx
00B743DF  74 09                           je 0x140b743ea
00B743E1  8A D0                           mov dl, al
00B743E3  8A CB                           mov cl, bl
00B743E5  E8 12 13 98 FF                  call 0x1404f56fc
00B743EA  44 8A FB                        mov r15b, bl
00B743ED  E8 E6 B7 90 FF                  call 0x14047fbd8
00B743F2  33 C0                           xor eax, eax
00B743F4  38 45 F4                        cmp byte ptr [rbp - 0xc], al
00B743F7  74 0A                           je 0x140b74403
00B743F9  F0 FF 0D 18 30 2C 00            lock dec dword ptr [rip + 0x2c3018]
00B74400  88 45 F4                        mov byte ptr [rbp - 0xc], al
00B74403  B8 02 00 00 00                  mov eax, 2
00B74408  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00B7440C  89 05 3A BD 2B 00               mov dword ptr [rip + 0x2bbd3a], eax
00B74412  E8 35 47 B0 FF                  call 0x140678b4c
00B74417  33 C9                           xor ecx, ecx
00B74419  8B D8                           mov ebx, eax
00B7441B  85 C0                           test eax, eax
00B7441D  78 40                           js 0x140b7445f
00B7441F  49 8B CE                        mov rcx, r14
00B74422  E8 5D 48 B0 FF                  call 0x140678c84
00B74427  33 C9                           xor ecx, ecx
00B74429  8B D8                           mov ebx, eax
00B7442B  85 C0                           test eax, eax
00B7442D  78 30                           js 0x140b7445f
00B7442F  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00B74433  44 8D 71 01                     lea r14d, [rcx + 1]
00B74437  41 8B CE                        mov ecx, r14d
00B7443A  E8 91 66 B4 FF                  call 0x1406baad0
00B7443F  33 C9                           xor ecx, ecx
00B74441  8B D8                           mov ebx, eax
00B74443  3D 94 02 00 40                  cmp eax, 0x40000294
00B74448  75 1B                           jne 0x140b74465
00B7444A  85 FF                           test edi, edi
00B7444C  75 17                           jne 0x140b74465
00B7444E  8B D9                           mov ebx, ecx
00B74450  8B 4D EC                        mov ecx, dword ptr [rbp - 0x14]
00B74453  E8 68 4A B0 FF                  call 0x140678ec0
00B74458  33 C9                           xor ecx, ecx
00B7445A  45 8B EE                        mov r13d, r14d
00B7445D  EB 06                           jmp 0x140b74465
00B7445F  41 BE 01 00 00 00               mov r14d, 1
00B74465  BF 02 00 00 00                  mov edi, 2
00B7446A  89 0D DC BC 2B 00               mov dword ptr [rip + 0x2bbcdc], ecx
00B74470  48 89 0D 11 BD 2B 00            mov qword ptr [rip + 0x2bbd11], rcx
00B74477  38 4D F4                        cmp byte ptr [rbp - 0xc], cl
00B7447A  74 07                           je 0x140b74483
00B7447C  F0 FF 0D 95 2F 2C 00            lock dec dword ptr [rip + 0x2c2f95]
00B74483  B8 11 00 00 00                  mov eax, 0x11
00B74488  44 3A E0                        cmp r12b, al
00B7448B  74 28                           je 0x140b744b5
00B7448D  44 3A F8                        cmp r15b, al
00B74490  74 07                           je 0x140b74499
00B74492  E8 89 73 B1 FF                  call 0x14068b820
00B74497  33 C9                           xor ecx, ecx
00B74499  39 0D 81 28 45 00               cmp dword ptr [rip + 0x452881], ecx
00B7449F  74 0C                           je 0x140b744ad
00B744A1  44 0F 20 C1                     mov rcx, cr8
00B744A5  41 8A D4                        mov dl, r12b
00B744A8  E8 EB 11 98 FF                  call 0x1404f5698
00B744AD  41 0F B6 C4                     movzx eax, r12b
00B744B1  44 0F 22 C0                     mov cr8, rax
00B744B5  45 85 ED                        test r13d, r13d
00B744B8  74 1A                           je 0x140b744d4
00B744BA  8B 45 EC                        mov eax, dword ptr [rbp - 0x14]
00B744BD  48 8D 0D A4 BC 2B 00            lea rcx, [rip + 0x2bbca4]
00B744C4  8B D7                           mov edx, edi
00B744C6  48 89 05 B3 BC 2B 00            mov qword ptr [rip + 0x2bbcb3], rax
00B744CD  E8 4E 50 78 FF                  call 0x1402f9520
00B744D2  EB 18                           jmp 0x140b744ec
00B744D4  F0 FF 0D 35 31 2C 00            lock dec dword ptr [rip + 0x2c3135]
00B744DB  48 8D 0D 6E BC 2B 00            lea rcx, [rip + 0x2bbc6e]
00B744E2  45 33 C0                        xor r8d, r8d
00B744E5  33 D2                           xor edx, edx
00B744E7  E8 24 AE 7C FF                  call 0x14033f310
00B744EC  48 8B D6                        mov rdx, rsi
00B744EF  48 8D 0D 0A 48 2C 00            lea rcx, [rip + 0x2c480a]
00B744F6  E8 4D 45 84 FF                  call 0x1403b8a48
00B744FB  B8 11 00 00 00                  mov eax, 0x11
00B74500  33 D2                           xor edx, edx
00B74502  F0 48 0F B1 15 3D BB 2B 00      lock cmpxchg qword ptr [rip + 0x2bbb3d], rdx
00B7450B  74 0C                           je 0x140b74519
00B7450D  48 8D 0D 34 BB 2B 00            lea rcx, [rip + 0x2bbb34]
00B74514  E8 27 EF 6E FF                  call 0x140263440
00B74519  48 8D 0D 28 BB 2B 00            lea rcx, [rip + 0x2bbb28]
00B74520  E8 DB D0 76 FF                  call 0x1402e1600
00B74525  90                              nop
00B74526  66 44 01 B6 E6 01 00 00         add word ptr [rsi + 0x1e6], r14w
00B7452E  75 12                           jne 0x140b74542
00B74530  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
00B74537  90                              nop
00B74538  48 39 00                        cmp qword ptr [rax], rax
00B7453B  74 05                           je 0x140b74542
00B7453D  E8 3E E7 76 FF                  call 0x1402e2c80
00B74542  F6 05 3F 25 45 00 04            test byte ptr [rip + 0x45253f], 4
00B74549  75 0C                           jne 0x140b74557
00B7454B  48 8B 0D AE 26 45 00            mov rcx, qword ptr [rip + 0x4526ae]
00B74552  E8 99 F4 72 FF                  call 0x1402a39f0
00B74557  8B C3                           mov eax, ebx
00B74559  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00B74561  48 83 C4 50                     add rsp, 0x50
00B74565  41 5F                           pop r15
00B74567  41 5E                           pop r14
00B74569  41 5D                           pop r13
00B7456B  41 5C                           pop r12
00B7456D  5F                              pop rdi
00B7456E  5E                              pop rsi
00B7456F  5D                              pop rbp
00B74570  C3                              ret
00B74571  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmDuplicateMemory(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_rdi = 0;
    result = 0;
    v_stack_p8 = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    if ((((unsigned __int8)(v_rdi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32))))) == 0) goto loc_00B741A4;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (0x404ULL)) != 0) goto loc_00B741DB;
loc_00B741A4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (8)) != 0) {
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (0xFFFFFBFAULL));
        v_stack_m50 = (unsigned int)(a2);
    }
    if (condition_is_above_or_equal) goto loc_00B741BD;
    if ((((unsigned __int8)(a2)) & (4)) != 0) goto loc_00B741DB;
loc_00B741BD:
    if ((((unsigned __int8)(a2)) & (192)) == 0) goto loc_00B741E5;
    if ((((unsigned int)(a2)) & (0xFFFFFC2EULL)) != 0) goto loc_00B741DB;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) & ((unsigned int)(v_rdi + 17)));
    if (((unsigned __int8)(result)) != ((unsigned __int8)(v_rdi + 17))) goto loc_00B741DB;
    if ((((unsigned __int8)(a2)) & (64)) == 0) goto loc_00B741E5;
    if (!sign_flag) goto loc_00B741E5;
loc_00B741DB:
    goto loc_00B74559;
loc_00B741E5:
    if (condition_is_below) goto loc_00B741F5;
    result = (unsigned int)(0xC000000DULL);
    if ((((unsigned __int8)(a2)) & (10)) == 0) {
        result = CcNotifyWriteBehind(v_rdi + 17, a2, a3, a4);
    }
    v_stack_m58 = a1;
    v_stack_m4C = 8;
    v_stack_m44 = 0;
    result = (unsigned int)(((unsigned int)(v_stack_m50)) & (512));
    result = (unsigned int)(-(result));
    a4 = 0;
    a1 = (v_rdi + 17) & (v_stack_p8);
    a3 = 0;
    v_stack_m68 = a1;
    result = KeWaitForSingleObject(v_rip + 2866970, a4 + 18, a3, a4);
    if (sign_flag) goto loc_00B74559;
    if (((unsigned int)(result)) != 258) goto loc_00B74257;
    goto loc_00B74559;
loc_00B74257:
    result = 258;
    if (((*(unsigned __int8 *)(v_rip + 4532266)) & (4)) == 0) {
        a1 = *(unsigned __int64 *)(v_rip + 4532633);
        result = MmLockPagableSectionByHandle(a1, a4 + 18, a3, a4);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 2866638, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 2866601;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 2866589;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = MiLockDynamicMemoryShared(v_rip + 2902589, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rip + 2866864) = *(unsigned __int64 *)(gs_base + (0 + 392));
    a1 = 0;
    result = MiUpdateMirrorBitmaps(a1, a2, a3, a4);
    v_rbx = 0;
    if ((unsigned int)(result) != 0) goto loc_00B742FA;
    a1 = 0;
    goto loc_00B7446A;
loc_00B742FA:
    result = MiActOnMirrorBitmap(v_rip + 2866842, 1, a3, a4);
    v_stack_m48 = (unsigned int)((unsigned int)(0xC000009AULL));
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_m50)))) == 0) goto loc_00B74324;
    v_stack_m48 = 3;
    goto loc_00B74346;
loc_00B74324:
    if (condition_is_below) goto loc_00B7433B;
    if ((((unsigned __int8)((unsigned int)(v_stack_m50))) & (4)) == 0) goto loc_00B74337;
    v_stack_m4C = 7;
    goto loc_00B7433E;
loc_00B74337:
    if ((((unsigned __int8)((unsigned int)(v_stack_m50))) & (8)) == 0) goto loc_00B74348;
loc_00B7433B:
    v_stack_m4C = (unsigned int)((unsigned int)(0xC000009AULL));
loc_00B7433E:
    v_stack_m48 = 2;
loc_00B74346:
loc_00B74348:
    result = guard_dispatch_icall(v_rip + 2866842, 1, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00B7445F;
    *(unsigned int *)(v_rip + 2866658) = 1;
    result = MiMirrorBrownPhase(v_stack_m58, 1, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00B7445F;
    if (((v_stack_m50) & (0x802ULL)) != 0) goto loc_00B74393;
    if (v_stack_m44 != 0) {
        v_stack_m44 = 0;
    }
    result = guard_dispatch_icall(a1, 1, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00B7445F;
    if ((*(unsigned __int64 *)(2 - 1 + 24)) != 0) {
        a2 = a1 + 1;
        a1 = v_rip + 2866640;
        result = MiActOnMirrorBitmap(a1, a2, a3, a4);
        a1 = 0;
    }
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_00B743ED;
    result = 2;
    if ((*(unsigned int *)(v_rip + 4532545)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00B743ED:
    result = MiLockAllMemoryLists(a1, a2, a3, a4);
    result = 0;
    if (v_stack_m44 != 0) {
        v_stack_m44 = 0;
    }
    *(unsigned int *)(v_rip + 2866490) = 2;
    result = MiMirrorBlackPhase(v_stack_m58, a2, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00B7445F;
    result = MiMirrorVerify(2 - 1, a2, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00B7445F;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(a1 + 1)), a2, a3, a4);
    a1 = 0;
    if (((unsigned int)(result)) != 0x40000294ULL) goto loc_00B74465;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))) != 0) goto loc_00B74465;
    result = MiResumeFromHibernate((unsigned int)(v_stack_m4C), a2, a3, a4);
    a1 = 0;
    goto loc_00B74465;
loc_00B7445F:
loc_00B74465:
loc_00B7446A:
    *(unsigned int *)(v_rip + 2866396) = 0;
    *(unsigned __int64 *)(v_rip + 2866449) = 0;
    if (v_stack_m44 != 0) {
    }
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00B744B5;
    result = 17;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) != 17) {
        result = MiUnlockAllMemoryLists(a1, a2, a3, a4);
        a1 = 0;
    }
    if ((*(unsigned int *)(v_rip + 4532353)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00B744B5:
    if ((unsigned int)((unsigned int)((unsigned int)(a1 + 1))) == 0) goto loc_00B744D4;
    *(unsigned __int64 *)(v_rip + 2866355) = (unsigned int)(v_stack_m4C);
    result = ExQueueWorkItem(v_rip + 2866340, 2, a3, a4);
    goto loc_00B744EC;
loc_00B744D4:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 2866286, a2, a3, a4);
loc_00B744EC:
    result = MiUnlockDynamicMemoryShared(v_rip + 2902026, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    a2 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rip + 2865972;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 2865960, a2, a3, a4);
    if (condition_is_not_equal) goto loc_00B74542;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 2865960, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 4531519)) & (4)) == 0) {
        a1 = *(unsigned __int64 *)(v_rip + 4531886);
        result = MmUnlockPagableImageSection(a1, a2, a3, a4);
    }
loc_00B74559:
    v_rsp = (v_rsp) + (80);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t MmDuplicateMemory(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint8_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (80);
    local_rdi = 0;
    result = 0;
    v_stack_p8 = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    if ((((uint8_t)(local_rdi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) == 0) goto loc_00B741A4;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (0x404ULL)) != 0) goto loc_00B741DB;
loc_00B741A4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (8)) != 0) {
        Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (0xFFFFFBFAULL));
        v_stack_m50 = (uint32_t)(Arg2);
    }
    if (condition_is_above_or_equal) goto loc_00B741BD;
    if ((((uint8_t)(Arg2)) & (4)) != 0) goto loc_00B741DB;
loc_00B741BD:
    if ((((uint8_t)(Arg2)) & (192)) == 0) goto loc_00B741E5;
    if ((((uint32_t)(Arg2)) & (0xFFFFFC2EULL)) != 0) goto loc_00B741DB;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & ((uint32_t)(local_rdi + 17)));
    if (((uint8_t)(result)) != ((uint8_t)(local_rdi + 17))) goto loc_00B741DB;
    if ((((uint8_t)(Arg2)) & (64)) == 0) goto loc_00B741E5;
    if (!sign_flag) goto loc_00B741E5;
loc_00B741DB:
    goto loc_00B74559;
loc_00B741E5:
    if (condition_is_below) goto loc_00B741F5;
    result = (uint32_t)(0xC000000DULL);
    if ((((uint8_t)(Arg2)) & (10)) == 0) {
        result = CcNotifyWriteBehind(local_rdi + 17, Arg2, Arg3, Arg4);
    }
    v_stack_m58 = Arg1;
    v_stack_m4C = 8;
    v_stack_m44 = 0;
    result = (uint32_t)(((uint32_t)(v_stack_m50)) & (512));
    result = (uint32_t)(-(result));
    Arg4 = 0;
    Arg1 = (local_rdi + 17) & (v_stack_p8);
    Arg3 = 0;
    v_stack_m68 = Arg1;
    result = KeWaitForSingleObject(v_rip + 2866970, Arg4 + 18, Arg3, Arg4);
    if (sign_flag) goto loc_00B74559;
    if (((uint32_t)(result)) != 258) goto loc_00B74257;
    goto loc_00B74559;
loc_00B74257:
    result = 258;
    if (((*(uint8_t *)(v_rip + 0x45282A)) & (4)) == 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x452999);
        result = MmLockPagableSectionByHandle(Arg1, Arg4 + 18, Arg3, Arg4);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 2866638, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = v_rip + 2866601;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 2866589;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = MiLockDynamicMemoryShared(v_rip + 2902589, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    Arg2 = 0;
    *(uint64_t *)(v_rip + 0x2BBEB0) = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg1 = 0;
    result = MiUpdateMirrorBitmaps(Arg1, Arg2, Arg3, Arg4);
    local_rbx = 0;
    if ((uint32_t)(result) != 0) goto loc_00B742FA;
    Arg1 = 0;
    goto loc_00B7446A;
loc_00B742FA:
    result = MiActOnMirrorBitmap(v_rip + 2866842, 1, Arg3, Arg4);
    v_stack_m48 = (uint32_t)((uint32_t)(0xC000009AULL));
    if (((1) & ((uint8_t)((uint32_t)(v_stack_m50)))) == 0) goto loc_00B74324;
    v_stack_m48 = 3;
    goto loc_00B74346;
loc_00B74324:
    if (condition_is_below) goto loc_00B7433B;
    if ((((uint8_t)((uint32_t)(v_stack_m50))) & (4)) == 0) goto loc_00B74337;
    v_stack_m4C = 7;
    goto loc_00B7433E;
loc_00B74337:
    if ((((uint8_t)((uint32_t)(v_stack_m50))) & (8)) == 0) goto loc_00B74348;
loc_00B7433B:
    v_stack_m4C = (uint32_t)((uint32_t)(0xC000009AULL));
loc_00B7433E:
    v_stack_m48 = 2;
loc_00B74346:
loc_00B74348:
    result = guard_dispatch_icall(v_rip + 2866842, 1, Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00B7445F;
    *(uint32_t *)(v_rip + 0x2BBDE2) = 1;
    result = MiMirrorBrownPhase(v_stack_m58, 1, Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00B7445F;
    if (((v_stack_m50) & (0x802ULL)) != 0) goto loc_00B74393;
    if (v_stack_m44 != 0) {
        v_stack_m44 = 0;
    }
    result = guard_dispatch_icall(Arg1, 1, Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00B7445F;
    if ((*(uint64_t *)(2 - 0x1 + 0x18)) != 0) {
        Arg2 = Arg1 + 1;
        Arg1 = v_rip + 2866640;
        result = MiActOnMirrorBitmap(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 0;
    }
    if (((uint8_t)(v_cr8)) >= 2) goto loc_00B743ED;
    result = 2;
    if ((*(uint32_t *)(v_rip + 0x452941)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_00B743ED:
    result = MiLockAllMemoryLists(Arg1, Arg2, Arg3, Arg4);
    result = 0;
    if (v_stack_m44 != 0) {
        v_stack_m44 = 0;
    }
    *(uint32_t *)(v_rip + 0x2BBD3A) = 2;
    result = MiMirrorBlackPhase(v_stack_m58, Arg2, Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00B7445F;
    result = MiMirrorVerify(2 - 1, Arg2, Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00B7445F;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(Arg1 + 1)), Arg2, Arg3, Arg4);
    Arg1 = 0;
    if (((uint32_t)(result)) != 0x40000294ULL) goto loc_00B74465;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))) != 0) goto loc_00B74465;
    result = MiResumeFromHibernate((uint32_t)(v_stack_m4C), Arg2, Arg3, Arg4);
    Arg1 = 0;
    goto loc_00B74465;
loc_00B7445F:
loc_00B74465:
loc_00B7446A:
    *(uint32_t *)(v_rip + 0x2BBCDC) = 0;
    *(uint64_t *)(v_rip + 0x2BBD11) = 0;
    if (v_stack_m44 != 0) {
    }
    if (((uint8_t)(v_cr8)) == 17) goto loc_00B744B5;
    result = 17;
    if (((uint8_t)((uint8_t)(v_cr8))) != 17) {
        result = MiUnlockAllMemoryLists(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 0;
    }
    if ((*(uint32_t *)(v_rip + 0x452881)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_00B744B5:
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1 + 1))) == 0) goto loc_00B744D4;
    *(uint64_t *)(v_rip + 0x2BBCB3) = (uint32_t)(v_stack_m4C);
    result = ExQueueWorkItem(v_rip + 2866340, 2, Arg3, Arg4);
    goto loc_00B744EC;
loc_00B744D4:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 2866286, Arg2, Arg3, Arg4);
loc_00B744EC:
    result = MiUnlockDynamicMemoryShared(v_rip + 2902026, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    Arg2 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = v_rip + 2865972;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_rip + 2865960, Arg2, Arg3, Arg4);
    if (condition_is_not_equal) goto loc_00B74542;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 2865960, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(v_rip + 0x45253F)) & (4)) == 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x4526AE);
        result = MmUnlockPagableImageSection(Arg1, Arg2, Arg3, Arg4);
    }
loc_00B74559:
    local_rsp = (local_rsp) + (80);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B74158&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
