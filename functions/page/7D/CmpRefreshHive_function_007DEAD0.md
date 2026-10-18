# CmpRefreshHive

- RVA: `0x007DEAD0`–`0x007DEF55` (길이 `1,157` bytes)
- VA: `0x00000001407DEAD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D65A4`
- 디코드: `303`개 명령, `1,157/1,157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007DEB19` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007DEB22` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007DEB2B` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x007DEB38` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (function, `0x00BC9C6C`)
- `0x007DEB55` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x007DEB6E` → [CmpBecomeActiveFlusherAndReconciler](../7E/CmpBecomeActiveFlusherAndReconciler_function_007E7E20.md) (function, `0x007E7E20`)
- `0x007DEB78` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DEB83` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x007DEB8D` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x007DEBA9` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x007DEBC0` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x007DEBC8` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x007DEBDF` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x007DEBE7` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x007DEBF4` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x007DEBFC` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x007DEC27` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x007DEC2C` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DEC44` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x007DED0E` → [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) (function, `0x00879DF0`)
- `0x007DED19` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DED23` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x007DED47` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007DED51` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DED61` → [CmpFinishBeingActiveFlusherAndReconciler](../7E/CmpFinishBeingActiveFlusherAndReconciler_function_007E7EB0.md) (function, `0x007E7EB0`)
- `0x007DED73` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x007DED7E` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (function, `0x00BC9CAC`)
- `0x007DED8C` → [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) (function, `0x009B1708`)
- `0x007DED99` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x007DEE11` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DEE18` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DEE37` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DEE3E` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DEE57` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007DEE84` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DEE8B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DEEA1` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DEEA8` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DEEB0` → [CmpCleanUpKCBCacheTable](../9B/CmpCleanUpKCBCacheTable_function_009B0478.md) (function, `0x009B0478`)
- `0x007DEECB` → [CmpSearchKeyControlBlockTreeEx](../A6/CmpSearchKeyControlBlockTreeEx_function_00A65548.md) (function, `0x00A65548`)
- `0x007DEEDC` → [CmpFlushNotifiesOnKeyBodyList](../9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (function, `0x009B3594`)
- `0x007DEEE8` → [CmpSwapHiveStorage](../7E/CmpSwapHiveStorage_function_007EE54C.md) (function, `0x007EE54C`)
- `0x007DEEF4` → [CmpRebuildKcbCache](../87/CmpRebuildKcbCache_function_00874DF8.md) (function, `0x00874DF8`)
- `0x007DEF1B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DEF22` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DEF41` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DEF4B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)

### Direct callers
- [CmRestoreKey](CmRestoreKey_function_007DCF04.md) at `0x007DD048`

### Static image references
- `0x007DEEC4` → RVA `0x007DEF60` (`CmpRefreshWorkerRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x007DEB2B` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x007DEB38` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEB55` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x007DEB78` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEB83` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEB8D` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEBA9` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEC27` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEC2C` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DEC44` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x007DED23` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DED47` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007DED51` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DED73` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x007DED7E` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (`PAGE` → `PAGECMRC`)
  - `0x007DED99` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007DEAD0  40 55                           push rbp
007DEAD2  53                              push rbx
007DEAD3  56                              push rsi
007DEAD4  57                              push rdi
007DEAD5  41 54                           push r12
007DEAD7  41 55                           push r13
007DEAD9  41 56                           push r14
007DEADB  41 57                           push r15
007DEADD  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
007DEAE2  48 81 EC B8 00 00 00            sub rsp, 0xb8
007DEAE9  33 DB                           xor ebx, ebx
007DEAEB  0F 57 C0                        xorps xmm0, xmm0
007DEAEE  4C 8B F1                        mov r14, rcx
007DEAF1  48 89 5D 7F                     mov qword ptr [rbp + 0x7f], rbx
007DEAF5  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
007DEAF9  48 89 5D D7                     mov qword ptr [rbp - 0x29], rbx
007DEAFD  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
007DEB01  88 5D 6F                        mov byte ptr [rbp + 0x6f], bl
007DEB04  40 8A F3                        mov sil, bl
007DEB07  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
007DEB0B  44 8A FB                        mov r15b, bl
007DEB0E  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
007DEB12  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
007DEB16  44 8B E3                        mov r12d, ebx
007DEB19  E8 F2 73 07 00                  call 0x140855f10
007DEB1E  48 8D 4D D7                     lea rcx, [rbp - 0x29]
007DEB22  E8 E9 73 07 00                  call 0x140855f10
007DEB27  48 8D 4D E7                     lea rcx, [rbp - 0x19]
007DEB2B  E8 C0 BC C4 FF                  call 0x14042a7f0
007DEB30  4D 8B 6E 08                     mov r13, qword ptr [r14 + 8]
007DEB34  49 8B 7D 20                     mov rdi, qword ptr [r13 + 0x20]
007DEB38  E8 2F B1 3E 00                  call 0x140bc9c6c
007DEB3D  88 45 77                        mov byte ptr [rbp + 0x77], al
007DEB40  84 C0                           test al, al
007DEB42  75 0A                           jne 0x1407deb4e
007DEB44  BB 89 01 00 C0                  mov ebx, 0xc0000189
007DEB49  E9 F3 01 00 00                  jmp 0x1407ded41
007DEB4E  48 8D 8F 68 06 00 00            lea rcx, [rdi + 0x668]
007DEB55  E8 C6 7A A3 FF                  call 0x140216620
007DEB5A  88 45 6F                        mov byte ptr [rbp + 0x6f], al
007DEB5D  84 C0                           test al, al
007DEB5F  75 0A                           jne 0x1407deb6b
007DEB61  BB 25 04 00 C0                  mov ebx, 0xc0000425
007DEB66  E9 D6 01 00 00                  jmp 0x1407ded41
007DEB6B  48 8B CF                        mov rcx, rdi
007DEB6E  E8 AD 92 00 00                  call 0x1407e7e20
007DEB73  BE 01 00 00 00                  mov esi, 1
007DEB78  E8 B7 AF 3E 00                  call 0x140bc9b34
007DEB7D  49 8B CD                        mov rcx, r13
007DEB80  44 8A FE                        mov r15b, sil
007DEB83  E8 94 AE 3E 00                  call 0x140bc9a1c
007DEB88  33 D2                           xor edx, edx
007DEB8A  49 8B CE                        mov rcx, r14
007DEB8D  E8 3E AC 3E 00                  call 0x140bc97d0
007DEB92  8B D8                           mov ebx, eax
007DEB94  85 C0                           test eax, eax
007DEB96  78 0E                           js 0x1407deba6
007DEB98  40 38 B7 80 0B 00 00            cmp byte ptr [rdi + 0xb80], sil
007DEB9F  75 12                           jne 0x1407debb3
007DEBA1  BB 89 01 00 C0                  mov ebx, 0xc0000189
007DEBA6  49 8B CD                        mov rcx, r13
007DEBA9  E8 12 A7 3E 00                  call 0x140bc92c0
007DEBAE  E9 8E 01 00 00                  jmp 0x1407ded41
007DEBB3  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
007DEBB9  A8 02                           test al, 2
007DEBBB  74 51                           je 0x1407dec0e
007DEBBD  48 8B CF                        mov rcx, rdi
007DEBC0  E8 97 0D 07 00                  call 0x14084f95c
007DEBC5  48 8B CF                        mov rcx, rdi
007DEBC8  E8 C7 AC 07 00                  call 0x140859894
007DEBCD  33 DB                           xor ebx, ebx
007DEBCF  48 8B CF                        mov rcx, rdi
007DEBD2  39 9F 90 03 00 00               cmp dword ptr [rdi + 0x390], ebx
007DEBD8  74 1A                           je 0x1407debf4
007DEBDA  BB 01 00 00 C0                  mov ebx, 0xc0000001
007DEBDF  E8 00 AD 07 00                  call 0x1408598e4
007DEBE4  48 8B CF                        mov rcx, rdi
007DEBE7  E8 4C 9B 06 00                  call 0x140848738
007DEBEC  8A 45 6F                        mov al, byte ptr [rbp + 0x6f]
007DEBEF  88 45 6F                        mov byte ptr [rbp + 0x6f], al
007DEBF2  EB B2                           jmp 0x1407deba6
007DEBF4  E8 EB AC 07 00                  call 0x1408598e4
007DEBF9  48 8B CF                        mov rcx, rdi
007DEBFC  E8 37 9B 06 00                  call 0x140848738
007DEC01  41 F7 85 B8 00 00 00 00 00 04 00  test dword ptr [r13 + 0xb8], 0x40000
007DEC0C  75 07                           jne 0x1407dec15
007DEC0E  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007DEC13  EB 91                           jmp 0x1407deba6
007DEC15  39 9F 68 0B 00 00               cmp dword ptr [rdi + 0xb68], ebx
007DEC1B  76 07                           jbe 0x1407dec24
007DEC1D  BB 01 00 00 C0                  mov ebx, 0xc0000001
007DEC22  EB 82                           jmp 0x1407deba6
007DEC24  49 8B CD                        mov rcx, r13
007DEC27  E8 94 A6 3E 00                  call 0x140bc92c0
007DEC2C  E8 53 AE 3E 00                  call 0x140bc9a84
007DEC31  BA B0 01 00 00                  mov edx, 0x1b0
007DEC36  B9 00 01 00 00                  mov ecx, 0x100
007DEC3B  41 B8 43 4D 39 33               mov r8d, 0x33394d43
007DEC41  44 8A FB                        mov r15b, bl
007DEC44  E8 BB E8 BE FF                  call 0x1403cd504
007DEC49  4C 8B E0                        mov r12, rax
007DEC4C  48 85 C0                        test rax, rax
007DEC4F  75 0A                           jne 0x1407dec5b
007DEC51  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DEC56  E9 E6 00 00 00                  jmp 0x1407ded41
007DEC5B  48 89 5D 0F                     mov qword ptr [rbp + 0xf], rbx
007DEC5F  0F 57 C0                        xorps xmm0, xmm0
007DEC62  F3 0F 7F 45 FF                  movdqu xmmword ptr [rbp - 1], xmm0
007DEC67  48 8B 87 08 06 00 00            mov rax, qword ptr [rdi + 0x608]
007DEC6E  48 89 45 F7                     mov qword ptr [rbp - 9], rax
007DEC72  8B 87 A8 00 00 00               mov eax, dword ptr [rdi + 0xa8]
007DEC78  85 C0                           test eax, eax
007DEC7A  75 05                           jne 0x1407dec81
007DEC7C  44 8B CB                        mov r9d, ebx
007DEC7F  EB 30                           jmp 0x1407decb1
007DEC81  3B C6                           cmp eax, esi
007DEC83  75 10                           jne 0x1407dec95
007DEC85  48 8B 87 10 06 00 00            mov rax, qword ptr [rdi + 0x610]
007DEC8C  44 8B CE                        mov r9d, esi
007DEC8F  48 89 45 FF                     mov qword ptr [rbp - 1], rax
007DEC93  EB 1C                           jmp 0x1407decb1
007DEC95  48 8B 87 28 06 00 00            mov rax, qword ptr [rdi + 0x628]
007DEC9C  41 B9 02 00 00 00               mov r9d, 2
007DECA2  48 89 45 FF                     mov qword ptr [rbp - 1], rax
007DECA6  48 8B 87 30 06 00 00            mov rax, qword ptr [rdi + 0x630]
007DECAD  48 89 45 07                     mov qword ptr [rbp + 7], rax
007DECB1  8B 87 10 10 00 00               mov eax, dword ptr [rdi + 0x1010]
007DECB7  BA 02 00 00 00                  mov edx, 2
007DECBC  44 8B 87 A0 00 00 00            mov r8d, dword ptr [rdi + 0xa0]
007DECC3  25 00 00 01 00                  and eax, 0x10000
007DECC8  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
007DECCD  41 0F BA F0 10                  btr r8d, 0x10
007DECD2  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
007DECD7  F7 D8                           neg eax
007DECD9  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
007DECDE  48 8D 45 F7                     lea rax, [rbp - 9]
007DECE2  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
007DECE7  1B C9                           sbb ecx, ecx
007DECE9  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
007DECEE  83 E1 E0                        and ecx, 0xffffffe0
007DECF1  81 C1 42 00 19 01               add ecx, 0x1190042
007DECF7  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
007DECFB  48 8D 4D DF                     lea rcx, [rbp - 0x21]
007DECFF  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
007DED04  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007DED09  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007DED0E  E8 DD B0 09 00                  call 0x140879df0
007DED13  8B D8                           mov ebx, eax
007DED15  85 C0                           test eax, eax
007DED17  78 28                           js 0x1407ded41
007DED19  E8 96 0C 07 00                  call 0x14084f9b4
007DED1E  33 D2                           xor edx, edx
007DED20  49 8B CE                        mov rcx, r14
007DED23  E8 A8 AA 3E 00                  call 0x140bc97d0
007DED28  33 C9                           xor ecx, ecx
007DED2A  8B D8                           mov ebx, eax
007DED2C  85 C0                           test eax, eax
007DED2E  78 0E                           js 0x1407ded3e
007DED30  40 38 B7 80 0B 00 00            cmp byte ptr [rdi + 0xb80], sil
007DED37  75 7C                           jne 0x1407dedb5
007DED39  BB 89 01 00 C0                  mov ebx, 0xc0000189
007DED3E  44 8A FE                        mov r15b, sil
007DED41  33 D2                           xor edx, edx
007DED43  48 8D 4D E7                     lea rcx, [rbp - 0x19]
007DED47  E8 54 CC C3 FF                  call 0x14041b9a0
007DED4C  45 84 FF                        test r15b, r15b
007DED4F  74 05                           je 0x1407ded56
007DED51  E8 2E AD 3E 00                  call 0x140bc9a84
007DED56  45 33 FF                        xor r15d, r15d
007DED59  40 84 F6                        test sil, sil
007DED5C  74 08                           je 0x1407ded66
007DED5E  48 8B CF                        mov rcx, rdi
007DED61  E8 4A 91 00 00                  call 0x1407e7eb0
007DED66  44 38 7D 6F                     cmp byte ptr [rbp + 0x6f], r15b
007DED6A  74 0C                           je 0x1407ded78
007DED6C  48 8D 8F 68 06 00 00            lea rcx, [rdi + 0x668]
007DED73  E8 08 B1 B6 FF                  call 0x140349e80
007DED78  44 38 7D 77                     cmp byte ptr [rbp + 0x77], r15b
007DED7C  74 05                           je 0x1407ded83
007DED7E  E8 29 AF 3E 00                  call 0x140bc9cac
007DED83  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
007DED87  48 85 C9                        test rcx, rcx
007DED8A  74 05                           je 0x1407ded91
007DED8C  E8 77 29 1D 00                  call 0x1409b1708
007DED91  4D 85 E4                        test r12, r12
007DED94  74 08                           je 0x1407ded9e
007DED96  49 8B CC                        mov rcx, r12
007DED99  E8 E2 6F C9 FF                  call 0x140475d80
007DED9E  8B C3                           mov eax, ebx
007DEDA0  48 81 C4 B8 00 00 00            add rsp, 0xb8
007DEDA7  41 5F                           pop r15
007DEDA9  41 5E                           pop r14
007DEDAB  41 5D                           pop r13
007DEDAD  41 5C                           pop r12
007DEDAF  5F                              pop rdi
007DEDB0  5E                              pop rsi
007DEDB1  5B                              pop rbx
007DEDB2  5D                              pop rbp
007DEDB3  C3                              ret
007DEDB4  CC                              int3
007DEDB5  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
007DEDBB  A8 02                           test al, 2
007DEDBD  75 0A                           jne 0x1407dedc9
007DEDBF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007DEDC4  E9 75 FF FF FF                  jmp 0x1407ded3e
007DEDC9  39 8F 90 03 00 00               cmp dword ptr [rdi + 0x390], ecx
007DEDCF  74 0A                           je 0x1407deddb
007DEDD1  BB 01 00 00 C0                  mov ebx, 0xc0000001
007DEDD6  E9 63 FF FF FF                  jmp 0x1407ded3e
007DEDDB  41 F7 85 B8 00 00 00 00 00 04 00  test dword ptr [r13 + 0xb8], 0x40000
007DEDE6  74 D7                           je 0x1407dedbf
007DEDE8  39 8F 68 0B 00 00               cmp dword ptr [rdi + 0xb68], ecx
007DEDEE  77 E1                           ja 0x1407dedd1
007DEDF0  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
007DEDF4  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
007DEDF8  8B 50 24                        mov edx, dword ptr [rax + 0x24]
007DEDFB  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DEDFF  3B 50 24                        cmp edx, dword ptr [rax + 0x24]
007DEE02  75 BB                           jne 0x1407dedbf
007DEE04  4C 8D 45 D7                     lea r8, [rbp - 0x29]
007DEE08  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
007DEE0F  74 07                           je 0x1407dee18
007DEE11  E8 4A 5E 07 00                  call 0x140854c60
007DEE16  EB 05                           jmp 0x1407dee1d
007DEE18  E8 93 5E 07 00                  call 0x140854cb0
007DEE1D  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
007DEE21  4C 8B F0                        mov r14, rax
007DEE24  48 8B CF                        mov rcx, rdi
007DEE27  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DEE2B  8B 50 24                        mov edx, dword ptr [rax + 0x24]
007DEE2E  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DEE35  74 07                           je 0x1407dee3e
007DEE37  E8 24 5E 07 00                  call 0x140854c60
007DEE3C  EB 05                           jmp 0x1407dee43
007DEE3E  E8 6D 5E 07 00                  call 0x140854cb0
007DEE43  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
007DEE47  4C 8B F8                        mov r15, rax
007DEE4A  45 33 C9                        xor r9d, r9d
007DEE4D  45 33 C0                        xor r8d, r8d
007DEE50  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
007DEE54  8B 50 24                        mov edx, dword ptr [rax + 0x24]
007DEE57  E8 24 92 07 00                  call 0x140858080
007DEE5C  8B D8                           mov ebx, eax
007DEE5E  85 C0                           test eax, eax
007DEE60  0F 88 A0 00 00 00               js 0x1407def06
007DEE66  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
007DEE6A  48 8D 55 7F                     lea rdx, [rbp + 0x7f]
007DEE6E  66 41 83 4E 02 0C               or word ptr [r14 + 2], 0xc
007DEE74  48 8B CF                        mov rcx, rdi
007DEE77  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
007DEE7B  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DEE82  74 07                           je 0x1407dee8b
007DEE84  E8 97 DD 07 00                  call 0x14085cc20
007DEE89  EB 05                           jmp 0x1407dee90
007DEE8B  E8 B0 70 07 00                  call 0x140855f40
007DEE90  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
007DEE94  48 8D 55 D7                     lea rdx, [rbp - 0x29]
007DEE98  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
007DEE9F  74 07                           je 0x1407deea8
007DEEA1  E8 7A DD 07 00                  call 0x14085cc20
007DEEA6  EB 05                           jmp 0x1407deead
007DEEA8  E8 93 70 07 00                  call 0x140855f40
007DEEAD  48 8B CF                        mov rcx, rdi
007DEEB0  E8 C3 15 1D 00                  call 0x1409b0478
007DEEB5  45 33 C9                        xor r9d, r9d
007DEEB8  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
007DEEBD  4C 8D 45 E7                     lea r8, [rbp - 0x19]
007DEEC1  48 8B D7                        mov rdx, rdi
007DEEC4  48 8D 0D 95 00 00 00            lea rcx, [rip + 0x95]
007DEECB  E8 78 66 28 00                  call 0x140a65548
007DEED0  44 8A CE                        mov r9b, sil
007DEED3  4C 8D 45 E7                     lea r8, [rbp - 0x19]
007DEED7  33 D2                           xor edx, edx
007DEED9  49 8B CD                        mov rcx, r13
007DEEDC  E8 B3 46 1D 00                  call 0x1409b3594
007DEEE1  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
007DEEE5  48 8B CF                        mov rcx, rdi
007DEEE8  E8 5F F6 00 00                  call 0x1407ee54c
007DEEED  48 8D 55 E7                     lea rdx, [rbp - 0x19]
007DEEF1  49 8B CD                        mov rcx, r13
007DEEF4  E8 FF 5E 09 00                  call 0x140874df8
007DEEF9  01 B7 D4 00 00 00               add dword ptr [rdi + 0xd4], esi
007DEEFF  33 DB                           xor ebx, ebx
007DEF01  E9 38 FE FF FF                  jmp 0x1407ded3e
007DEF06  4D 85 FF                        test r15, r15
007DEF09  74 1C                           je 0x1407def27
007DEF0B  48 8D 55 7F                     lea rdx, [rbp + 0x7f]
007DEF0F  48 8B CF                        mov rcx, rdi
007DEF12  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DEF19  74 07                           je 0x1407def22
007DEF1B  E8 00 DD 07 00                  call 0x14085cc20
007DEF20  EB 05                           jmp 0x1407def27
007DEF22  E8 19 70 07 00                  call 0x140855f40
007DEF27  4D 85 F6                        test r14, r14
007DEF2A  0F 84 0E FE FF FF               je 0x1407ded3e
007DEF30  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
007DEF34  48 8D 55 D7                     lea rdx, [rbp - 0x29]
007DEF38  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
007DEF3F  74 0A                           je 0x1407def4b
007DEF41  E8 DA DC 07 00                  call 0x14085cc20
007DEF46  E9 F3 FD FF FF                  jmp 0x1407ded3e
007DEF4B  E8 F0 6F 07 00                  call 0x140855f40
007DEF50  E9 E9 FD FF FF                  jmp 0x1407ded3e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpRefreshHive(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (184);
    v_rbx = 0;
    v_stack_p20 = 0;
    v_stack_m88 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_p10 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m80 = 0;
    v_stack_m78 = v_xmm0;
    result = HvpGetCellContextInitialize(v_stack_p20, a2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m88, a2, a3, a4);
    result = CmpInitializeDelayDerefContext(v_stack_m78, a2, a3, a4);
    result = CmpAcquireHiveLoadUnloadRundown(v_stack_m78, a2, a3, a4);
    v_stack_p18 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_007DEB4E;
    goto loc_007DED41;
loc_007DEB4E:
    result = ExAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1640, a2, a3, a4);
    v_stack_p10 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_007DEB6B;
    goto loc_007DED41;
loc_007DEB6B:
    result = CmpBecomeActiveFlusherAndReconciler(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    result = CmpLockRegistry(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    result = CmpLockKcbShared(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, a3, a4);
    if (sign_flag) goto loc_007DEBA6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2944)) != 1) goto loc_007DEBB3;
loc_007DEBA6:
    result = CmpUnlockKcb(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    goto loc_007DED41;
loc_007DEBB3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)))) & (2)) == 0) goto loc_007DEC0E;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    result = HvLockHiveWriter(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    v_rbx = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 912)) == 0) goto loc_007DEBF4;
    result = HvUnlockHiveWriter(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    v_stack_p10 = (unsigned __int8)(v_stack_p10);
    goto loc_007DEBA6;
loc_007DEBF4:
    result = HvUnlockHiveWriter(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)) & (0x40000ULL)) != 0) goto loc_007DEC15;
loc_007DEC0E:
    goto loc_007DEBA6;
loc_007DEC15:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2920)) <= ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_007DEC24;
    goto loc_007DEBA6;
loc_007DEC24:
    result = CmpUnlockKcb(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    result = CmpAllocatePool(256, 432, (unsigned int)(0x33394D43ULL), a4);
    if (result != 0) goto loc_007DEC5B;
    goto loc_007DED41;
loc_007DEC5B:
    v_stack_m50 = (unsigned int)(0xC000009AULL);
    v_stack_m60 = v_xmm0;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1544);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 168))) != 0) goto loc_007DEC81;
    goto loc_007DECB1;
loc_007DEC81:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 168)))) != 1) goto loc_007DEC95;
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1552);
    goto loc_007DECB1;
loc_007DEC95:
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1576);
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1584);
loc_007DECB1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4112))) & (0x10000ULL));
    v_stack_m98 = result;
    v_stack_mA0 = (unsigned int)(0xC000009AULL);
    result = (unsigned int)(-(result));
    v_stack_mA8 = (unsigned int)(0xC000009AULL);
    v_stack_mB0 = (unsigned int)(0xC000009AULL);
    v_stack_mB8 = (unsigned int)(0xC000009AULL);
    a1 = (unsigned int)((256) & (0xFFFFFFE0ULL));
    a1 = (unsigned int)((a1) + (0x1190042ULL));
    v_stack_mC0 = (unsigned int)(a1);
    v_stack_mC8 = (unsigned int)(0xC000009AULL);
    v_stack_mD0 = v_stack_m68;
    v_stack_mD8 = (unsigned int)(0xC000009AULL);
    result = CmpCreateHive(v_stack_m80, 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    if (sign_flag) goto loc_007DED41;
    result = CmpLockRegistryExclusive(v_stack_m80, 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    a1 = 0;
    if (sign_flag) goto loc_007DED3E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2944)) != 1) goto loc_007DEDB5;
loc_007DED3E:
loc_007DED41:
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m78, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    if (1 != 0) {
        result = CmpUnlockRegistry(v_stack_m78, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    }
    v_r15 = 0;
    if (1 != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        result = CmpFinishBeingActiveFlusherAndReconciler(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    }
    if (v_stack_p10 != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1640;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    }
    if (v_stack_p18 != 0) {
        result = CmpReleaseHiveLoadUnloadRundown(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    }
    if (v_stack_m80 != 0) {
        result = CmpDestroyHive(v_stack_m80, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    }
    if (result != 0) {
        a1 = result;
        result = CmSiFreeMemory(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)), 2);
    }
    v_rsp = (v_rsp) + (184);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL)));
loc_007DEDB5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)))) & (2)) != 0) goto loc_007DEDC9;
loc_007DEDBF:
    goto loc_007DED3E;
loc_007DEDC9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 912)) == ((unsigned int)(a1))) goto loc_007DEDDB;
loc_007DEDD1:
    goto loc_007DED3E;
loc_007DEDDB:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)) & (0x40000ULL)) == 0) goto loc_007DEDBF;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2920)) > ((unsigned int)(a1))) goto loc_007DEDD1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m80 + 64) + 36)))) != (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 64) + 36))) goto loc_007DEDBF;
    if (((*(unsigned __int8 *)(v_stack_m80 + 140)) & (1)) == 0) goto loc_007DEE18;
    result = HvpGetCellFlat(v_stack_m80, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m80 + 64) + 36)), v_stack_m88, 2);
    goto loc_007DEE1D;
loc_007DEE18:
    result = HvpGetCellPaged(v_stack_m80, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m80 + 64) + 36)), v_stack_m88, 2);
loc_007DEE1D:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DEE3E;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 64) + 36)), v_stack_p20, 2);
    goto loc_007DEE43;
loc_007DEE3E:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 64) + 36)), v_stack_p20, 2);
loc_007DEE43:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_m80, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m80 + 64) + 36)), a3, a4);
    if (sign_flag) goto loc_007DEF06;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DEE8B;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p20, a3, a4);
    goto loc_007DEE90;
loc_007DEE8B:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p20, a3, a4);
loc_007DEE90:
    if (((*(unsigned __int8 *)(v_stack_m80 + 140)) & (1)) == 0) goto loc_007DEEA8;
    result = HvpReleaseCellFlat(v_stack_m80, v_stack_m88, a3, a4);
    goto loc_007DEEAD;
loc_007DEEA8:
    result = HvpReleaseCellPaged(v_stack_m80, v_stack_m88, a3, a4);
loc_007DEEAD:
    result = CmpCleanUpKCBCacheTable(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m88, a3, a4);
    a4 = 0;
    v_stack_p20 = 1;
    result = CmpSearchKeyControlBlockTreeEx(v_rip + 149, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m78, a4);
    a2 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(unsigned __int64 *)(a1 + 8), a2, v_stack_m78, 1);
    result = CmpSwapHiveStorage(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m80, v_stack_m78, 1);
    result = CmpRebuildKcbCache(*(unsigned __int64 *)(a1 + 8), v_stack_m78, v_stack_m78, 1);
    v_rbx = 0;
    goto loc_007DED3E;
loc_007DEF06:
    if (result == 0) goto loc_007DEF27;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DEF22;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p20, v_stack_m78, 1);
    goto loc_007DEF27;
loc_007DEF22:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p20, v_stack_m78, 1);
loc_007DEF27:
    if (result == 0) goto loc_007DED3E;
    if (((*(unsigned __int8 *)(v_stack_m80 + 140)) & (1)) == 0) goto loc_007DEF4B;
    result = HvpReleaseCellFlat(v_stack_m80, v_stack_m88, v_stack_m78, 1);
    goto loc_007DED3E;
loc_007DEF4B:
    result = HvpReleaseCellPaged(v_stack_m80, v_stack_m88, v_stack_m78, 1);
    goto loc_007DED3E;
}
```

## 5. (Beta) C Style

```c
int64_t CmpRefreshHive(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (184);
    local_rbx = 0;
    v_stack_p20 = 0;
    v_stack_m88 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_p10 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m80 = 0;
    v_stack_m78 = v_xmm0;
    result = HvpGetCellContextInitialize(v_stack_p20, Arg2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m88, Arg2, a3, a4);
    result = CmpInitializeDelayDerefContext(v_stack_m78, Arg2, a3, a4);
    result = CmpAcquireHiveLoadUnloadRundown(v_stack_m78, Arg2, a3, a4);
    v_stack_p18 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_007DEB4E;
    goto loc_007DED41;
loc_007DEB4E:
    result = ExAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 1640, Arg2, a3, a4);
    v_stack_p10 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_007DEB6B;
    goto loc_007DED41;
loc_007DEB6B:
    result = CmpBecomeActiveFlusherAndReconciler(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    result = CmpLockRegistry(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    result = CmpLockKcbShared(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, a3, a4);
    if (sign_flag) goto loc_007DEBA6;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB80)) != 1) goto loc_007DEBB3;
loc_007DEBA6:
    result = CmpUnlockKcb(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    goto loc_007DED41;
loc_007DEBB3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)))) & (2)) == 0) goto loc_007DEC0E;
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    result = HvLockHiveWriter(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    local_rbx = 0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x390)) == 0) goto loc_007DEBF4;
    result = HvUnlockHiveWriter(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    v_stack_p10 = (uint8_t)(v_stack_p10);
    goto loc_007DEBA6;
loc_007DEBF4:
    result = HvUnlockHiveWriter(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, a3, a4);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)) & (0x40000ULL)) != 0) goto loc_007DEC15;
loc_007DEC0E:
    goto loc_007DEBA6;
loc_007DEC15:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB68)) <= ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_007DEC24;
    goto loc_007DEBA6;
loc_007DEC24:
    result = CmpUnlockKcb(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    result = CmpAllocatePool(256, 432, (uint32_t)(0x33394D43ULL), a4);
    if (result != 0) goto loc_007DEC5B;
    goto loc_007DED41;
loc_007DEC5B:
    v_stack_m50 = (uint32_t)(0xC000009AULL);
    v_stack_m60 = v_xmm0;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x608);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA8))) != 0) goto loc_007DEC81;
    goto loc_007DECB1;
loc_007DEC81:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA8)))) != 1) goto loc_007DEC95;
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x610);
    goto loc_007DECB1;
loc_007DEC95:
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x628);
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x630);
loc_007DECB1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1010))) & (0x10000ULL));
    v_stack_m98 = result;
    v_stack_mA0 = (uint32_t)(0xC000009AULL);
    result = (uint32_t)(-(result));
    v_stack_mA8 = (uint32_t)(0xC000009AULL);
    v_stack_mB0 = (uint32_t)(0xC000009AULL);
    v_stack_mB8 = (uint32_t)(0xC000009AULL);
    Arg1 = (uint32_t)((256) & (0xFFFFFFE0ULL));
    Arg1 = (uint32_t)((Arg1) + (0x1190042ULL));
    v_stack_mC0 = (uint32_t)(Arg1);
    v_stack_mC8 = (uint32_t)(0xC000009AULL);
    v_stack_mD0 = v_stack_m68;
    v_stack_mD8 = (uint32_t)(0xC000009AULL);
    result = CmpCreateHive(v_stack_m80, 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    if (sign_flag) goto loc_007DED41;
    result = CmpLockRegistryExclusive(v_stack_m80, 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    Arg1 = 0;
    if (sign_flag) goto loc_007DED3E;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB80)) != 1) goto loc_007DEDB5;
loc_007DED3E:
loc_007DED41:
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m78, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    if (1 != 0) {
        result = CmpUnlockRegistry(v_stack_m78, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    }
    local_r15 = 0;
    if (1 != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
        result = CmpFinishBeingActiveFlusherAndReconciler(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    }
    if (v_stack_p10 != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 1640;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    }
    if (v_stack_p18 != 0) {
        result = CmpReleaseHiveLoadUnloadRundown(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    }
    if (v_stack_m80 != 0) {
        result = CmpDestroyHive(v_stack_m80, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    }
    if (result != 0) {
        Arg1 = result;
        result = CmSiFreeMemory(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)), 2);
    }
    local_rsp = (local_rsp) + (184);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL)));
loc_007DEDB5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)))) & (2)) != 0) goto loc_007DEDC9;
loc_007DEDBF:
    goto loc_007DED3E;
loc_007DEDC9:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x390)) == ((uint32_t)(Arg1))) goto loc_007DEDDB;
loc_007DEDD1:
    goto loc_007DED3E;
loc_007DEDDB:
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)) & (0x40000ULL)) == 0) goto loc_007DEDBF;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB68)) > ((uint32_t)(Arg1))) goto loc_007DEDD1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m80 + 0x40) + 0x24)))) != (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x40) + 0x24))) goto loc_007DEDBF;
    if (((*(uint8_t *)(v_stack_m80 + 0x8C)) & (1)) == 0) goto loc_007DEE18;
    result = HvpGetCellFlat(v_stack_m80, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m80 + 0x40) + 0x24)), v_stack_m88, 2);
    goto loc_007DEE1D;
loc_007DEE18:
    result = HvpGetCellPaged(v_stack_m80, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m80 + 0x40) + 0x24)), v_stack_m88, 2);
loc_007DEE1D:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DEE3E;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x40) + 0x24)), v_stack_p20, 2);
    goto loc_007DEE43;
loc_007DEE3E:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x40) + 0x24)), v_stack_p20, 2);
loc_007DEE43:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_m80, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m80 + 0x40) + 0x24)), a3, a4);
    if (sign_flag) goto loc_007DEF06;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DEE8B;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_p20, a3, a4);
    goto loc_007DEE90;
loc_007DEE8B:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_p20, a3, a4);
loc_007DEE90:
    if (((*(uint8_t *)(v_stack_m80 + 0x8C)) & (1)) == 0) goto loc_007DEEA8;
    result = HvpReleaseCellFlat(v_stack_m80, v_stack_m88, a3, a4);
    goto loc_007DEEAD;
loc_007DEEA8:
    result = HvpReleaseCellPaged(v_stack_m80, v_stack_m88, a3, a4);
loc_007DEEAD:
    result = CmpCleanUpKCBCacheTable(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m88, a3, a4);
    a4 = 0;
    v_stack_p20 = 1;
    result = CmpSearchKeyControlBlockTreeEx(v_rip + 149, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m78, a4);
    Arg2 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(uint64_t *)(arg1 + 0x8), Arg2, v_stack_m78, 1);
    result = CmpSwapHiveStorage(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m80, v_stack_m78, 1);
    result = CmpRebuildKcbCache(*(uint64_t *)(arg1 + 0x8), v_stack_m78, v_stack_m78, 1);
    local_rbx = 0;
    goto loc_007DED3E;
loc_007DEF06:
    if (result == 0) goto loc_007DEF27;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DEF22;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_p20, v_stack_m78, 1);
    goto loc_007DEF27;
loc_007DEF22:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_p20, v_stack_m78, 1);
loc_007DEF27:
    if (result == 0) goto loc_007DED3E;
    if (((*(uint8_t *)(v_stack_m80 + 0x8C)) & (1)) == 0) goto loc_007DEF4B;
    result = HvpReleaseCellFlat(v_stack_m80, v_stack_m88, v_stack_m78, 1);
    goto loc_007DED3E;
loc_007DEF4B:
    result = HvpReleaseCellPaged(v_stack_m80, v_stack_m88, v_stack_m78, 1);
    goto loc_007DED3E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007DEAD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
