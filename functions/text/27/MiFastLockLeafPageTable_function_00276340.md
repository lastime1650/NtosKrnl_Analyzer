# MiFastLockLeafPageTable

- RVA: `0x00276340`–`0x00277382` (길이 `4,162` bytes)
- VA: `0x0000000140276340`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065F18`
- 디코드: `915`개 명령, `4,162/4,162` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002765D7` → [KxTryToAcquireQueuedSpinLock](KxTryToAcquireQueuedSpinLock_function_00277388.md) (function, `0x00277388`)
- `0x002768DE` → [KxTryToAcquireQueuedSpinLock](KxTryToAcquireQueuedSpinLock_function_00277388.md) (function, `0x00277388`)
- `0x00276A4B` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00276C2E` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00276DC9` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00276EE8` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00276F55` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00276F64` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00276FCD` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00276FD8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0027701E` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0027704B` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002770B8` → [ExTryAcquireSpinLockExclusiveAtDpcLevel](../2B/ExTryAcquireSpinLockExclusiveAtDpcLevel_function_002BB800.md) (function, `0x002BB800`)
- `0x00277102` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0027711B` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x00277184` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x002771A1` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002771B1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002771CA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002771DA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00277310` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00277353` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00277376` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)

### Direct callers
- [MiLockPageLeafPageTable](../23/MiLockPageLeafPageTable_function_0023D160.md) at `0x0023D226`
- [sub_00243300](../24/Unknown_function_00243300.md) at `0x00243394`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x00243D38`
- [MiResolvePageTablePage](MiResolvePageTablePage_function_00275930.md) at `0x0027597F`
- [MiDeleteVaDirect](MiDeleteVaDirect_function_00277560.md) at `0x00277701`
- [MiCaptureDeleteHierarchy](MiCaptureDeleteHierarchy_function_0027F5F0.md) at `0x0027FA8A`
- [MiMakeSystemAddressValid](MiMakeSystemAddressValid_function_0027FF70.md) at `0x002804C6`
- [MiSynchronizeSystemVa](../28/MiSynchronizeSystemVa_function_0028ECB8.md) at `0x0028ED52`
- [MiLockStealUserVm](../2B/MiLockStealUserVm_function_002B3EDC.md) at `0x002B413A`
- [MiClearNonPagedPtes](../2C/MiClearNonPagedPtes_function_002C17A0.md) at `0x002C191E`
- [sub_002C2FAE](../2C/Unknown_function_002C2FAE.md) at `0x002C2FB7`
- [MiLockPoolCommitPageTable](../32/MiLockPoolCommitPageTable_function_00328BAC.md) at `0x00328BFB`
- [MiQueryAddressState](../32/MiQueryAddressState_function_0032C380.md) at `0x0032C4E0`
- [MiWriteAwePtes](../4C/MiWriteAwePtes_function_004C51E0.md) at `0x004C56F3`

### Static image references
- `0x002763C4` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0027694F` → RVA `0x00E2CB40` (`.data`; read)
- `0x00276A27` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00276C10` → RVA `0x00F0DE58` (`.data`; read)
- `0x00276EAA` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00276F47` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002772A0` → RVA `0x00FC6DE0` (`ALMOSTRO`; read)
- `0x002772B8` → RVA `0x00FC6C38` (`ALMOSTRO`; read)
- `0x00277316` → RVA `0x00E38C08` (`.data`; read)
- `0x0027731D` → RVA `0x00E38C10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00276340  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00276345  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0027634A  53                              push rbx
0027634B  56                              push rsi
0027634C  57                              push rdi
0027634D  41 54                           push r12
0027634F  41 55                           push r13
00276351  41 56                           push r14
00276353  41 57                           push r15
00276355  48 81 EC 20 01 00 00            sub rsp, 0x120
0027635C  4C 8B E9                        mov r13, rcx
0027635F  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00276369  49 8B C3                        mov rax, r11
0027636C  48 3B D0                        cmp rdx, rax
0027636F  0F 83 73 0F 00 00               jae 0x1402772e8
00276375  33 F6                           xor esi, esi
00276377  44 8B C6                        mov r8d, esi
0027637A  8B 89 B8 00 00 00               mov ecx, dword ptr [rcx + 0xb8]
00276380  80 E1 0F                        and cl, 0xf
00276383  80 F9 07                        cmp cl, 7
00276386  0F 84 52 0F 00 00               je 0x1402772de
0027638C  8D 41 FF                        lea eax, [rcx - 1]
0027638F  3C 01                           cmp al, 1
00276391  0F 86 47 0F 00 00               jbe 0x1402772de
00276397  80 F9 05                        cmp cl, 5
0027639A  0F 84 76 0F 00 00               je 0x140277316
002763A0  80 F9 03                        cmp cl, 3
002763A3  0F 84 F7 0E 00 00               je 0x1402772a0
002763A9  BF 01 00 00 00                  mov edi, 1
002763AE  84 C9                           test cl, cl
002763B0  44 0F 44 C7                     cmove r8d, edi
002763B4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002763BD  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002763C4  48 F7 05 B9 06 D5 00 00 00 80 00  test qword ptr [rip + 0xd506b9], 0x800000
002763CF  0F 84 A6 0F 00 00               je 0x14027737b
002763D5  48 85 C9                        test rcx, rcx
002763D8  0F 84 9D 0F 00 00               je 0x14027737b
002763DE  4C 8D B9 40 01 00 00            lea r15, [rcx + 0x140]
002763E5  4C 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r15
002763ED  41 39 37                        cmp dword ptr [r15], esi
002763F0  0F 85 85 0F 00 00               jne 0x14027737b
002763F6  41 89 3F                        mov dword ptr [r15], edi
002763F9  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
002763FD  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00276401  48 C1 EA 12                     shr rdx, 0x12
00276405  81 E2 F8 FF FF 3F               and edx, 0x3ffffff8
0027640B  48 BB 00 00 00 40 FB F6 FF FF   movabs rbx, 0xfffff6fb40000000
00276415  48 8B C3                        mov rax, rbx
00276418  4C 8D 0C 02                     lea r9, [rdx + rax]
0027641C  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
00276421  4C 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r9
00276429  49 8B C9                        mov rcx, r9
0027642C  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00276431  44 8B A4 24 70 01 00 00         mov r12d, dword ptr [rsp + 0x170]
00276439  41 83 CC 02                     or r12d, 2
0027643D  44 89 A4 24 70 01 00 00         mov dword ptr [rsp + 0x170], r12d
00276445  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
0027644F  45 85 C0                        test r8d, r8d
00276452  0F 84 8E 0D 00 00               je 0x1402771e6
00276458  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
00276460  4D 8B F1                        mov r14, r9
00276463  49 C1 EE 09                     shr r14, 9
00276467  4C 23 F2                        and r14, rdx
0027646A  49 8B C3                        mov rax, r11
0027646D  4C 03 F0                        add r14, rax
00276470  4C 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r14
00276478  49 8B 06                        mov rax, qword ptr [r14]
0027647B  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
00276485  49 8B CA                        mov rcx, r10
00276488  49 B8 F8 D7 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed7f8
00276492  4C 3B F1                        cmp r14, rcx
00276495  72 35                           jb 0x1402764cc
00276497  49 8B C8                        mov rcx, r8
0027649A  4C 3B F1                        cmp r14, rcx
0027649D  77 2D                           ja 0x1402764cc
0027649F  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
002764A7  A8 01                           test al, 1
002764A9  74 1C                           je 0x1402764c7
002764AB  A8 42                           test al, 0x42
002764AD  0F 95 C2                        setne dl
002764B0  A8 20                           test al, 0x20
002764B2  0F 95 C1                        setne cl
002764B5  84 D1                           test cl, dl
002764B7  0F 84 2C 01 00 00               je 0x1402765e9
002764BD  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
002764C7  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002764CC  A8 01                           test al, 1
002764CE  0F 84 AF 08 00 00               je 0x140276d83
002764D4  84 C0                           test al, al
002764D6  0F 88 35 04 00 00               js 0x140276911
002764DC  8B BC 24 70 01 00 00            mov edi, dword ptr [rsp + 0x170]
002764E3  40 F6 C7 08                     test dil, 8
002764E7  0F 85 67 03 00 00               jne 0x140276854
002764ED  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002764F2  BB 02 00 00 00                  mov ebx, 2
002764F7  48 8B 01                        mov rax, qword ptr [rcx]
002764FA  49 8B CA                        mov rcx, r10
002764FD  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
00276502  4C 3B C9                        cmp r9, rcx
00276505  72 35                           jb 0x14027653c
00276507  49 8B C8                        mov rcx, r8
0027650A  4C 3B C9                        cmp r9, rcx
0027650D  77 2D                           ja 0x14027653c
0027650F  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00276517  A8 01                           test al, 1
00276519  74 1C                           je 0x140276537
0027651B  A8 42                           test al, 0x42
0027651D  0F 95 C2                        setne dl
00276520  A8 20                           test al, 0x20
00276522  0F 95 C1                        setne cl
00276525  84 D1                           test cl, dl
00276527  0F 84 A3 02 00 00               je 0x1402767d0
0027652D  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
00276537  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0027653C  A8 01                           test al, 1
0027653E  0F 84 41 09 00 00               je 0x140276e85
00276544  84 C0                           test al, al
00276546  0F 88 22 0A 00 00               js 0x140276f6e
0027654C  89 B4 24 78 01 00 00            mov dword ptr [rsp + 0x178], esi
00276553  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0027655D  48 8B C0                        mov rax, rax
00276560  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
00276565  0F 85 00 01 00 00               jne 0x14027666b
0027656B  89 B4 24 80 00 00 00            mov dword ptr [rsp + 0x80], esi
00276572  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0027657B  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00276582  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00276589  24 0F                           and al, 0xf
0027658B  BF 01 00 00 00                  mov edi, 1
00276590  0F 85 A2 03 00 00               jne 0x140276938
00276596  49 8D 95 B0 00 00 00            lea rdx, [r13 + 0xb0]
0027659D  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
002765A5  8B C3                           mov eax, ebx
002765A7  48 8D 0C 40                     lea rcx, [rax + rax*2]
002765AB  49 8D 04 C8                     lea rax, [r8 + rcx*8]
002765AF  48 8D 88 40 9C 00 00            lea rcx, [rax + 0x9c40]
002765B6  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
002765BE  48 89 90 48 9C 00 00            mov qword ptr [rax + 0x9c48], rdx
002765C5  48 89 31                        mov qword ptr [rcx], rsi
002765C8  90                              nop
002765C9  F6 84 24 70 01 00 00 01         test byte ptr [rsp + 0x170], 1
002765D1  0F 84 50 04 00 00               je 0x140276a27
002765D7  E8 AC 0D 00 00                  call 0x140277388
002765DC  85 C0                           test eax, eax
002765DE  0F 84 F7 07 00 00               je 0x140276ddb
002765E4  E9 39 0C 00 00                  jmp 0x140277222
002765E9  48 F7 05 94 04 D5 00 00 00 60 00  test qword ptr [rip + 0xd50494], 0x600000
002765F4  0F 84 C3 FE FF FF               je 0x1402764bd
002765FA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00276603  48 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rcx
0027660B  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00276612  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00276619  0F 84 9E FE FF FF               je 0x1402764bd
0027661F  48 8B 92 08 05 00 00            mov rdx, qword ptr [rdx + 0x508]
00276626  48 85 D2                        test rdx, rdx
00276629  0F 84 8E FE FF FF               je 0x1402764bd
0027662F  49 8B CE                        mov rcx, r14
00276632  48 C1 E9 03                     shr rcx, 3
00276636  81 E1 FF 01 00 00               and ecx, 0x1ff
0027663C  48 8B 0C CA                     mov rcx, qword ptr [rdx + rcx*8]
00276640  F6 C1 20                        test cl, 0x20
00276643  74 0C                           je 0x140276651
00276645  48 83 C8 20                     or rax, 0x20
00276649  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00276651  F6 C1 42                        test cl, 0x42
00276654  0F 84 63 FE FF FF               je 0x1402764bd
0027665A  48 83 C8 42                     or rax, 0x42
0027665E  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00276666  E9 52 FE FF FF                  jmp 0x1402764bd
0027666B  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00276672  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00276679  A8 0F                           test al, 0xf
0027667B  0F 85 97 03 00 00               jne 0x140276a18
00276681  49 8B C2                        mov rax, r10
00276684  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00276689  48 3B C8                        cmp rcx, rax
0027668C  0F 82 86 03 00 00               jb 0x140276a18
00276692  48 BA FF DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedfff
0027669C  48 8B C2                        mov rax, rdx
0027669F  48 3B C8                        cmp rcx, rax
002766A2  77 2F                           ja 0x1402766d3
002766A4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002766AD  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
002766B5  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
002766BC  48 8B 88 10 04 00 00            mov rcx, qword ptr [rax + 0x410]
002766C3  4C 8B 89 68 05 00 00            mov r9, qword ptr [rcx + 0x568]
002766CA  4D 85 C9                        test r9, r9
002766CD  0F 85 55 09 00 00               jne 0x140277028
002766D3  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
002766DA  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
002766DE  A8 0F                           test al, 0xf
002766E0  0F 85 80 02 00 00               jne 0x140276966
002766E6  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002766EB  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
002766EF  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
002766F3  48 8B 19                        mov rbx, qword ptr [rcx]
002766F6  49 8B C2                        mov rax, r10
002766F9  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
002766FE  4C 3B C8                        cmp r9, rax
00276701  72 2E                           jb 0x140276731
00276703  49 8B C0                        mov rax, r8
00276706  4C 3B C8                        cmp r9, rax
00276709  77 26                           ja 0x140276731
0027670B  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00276713  F6 C3 01                        test bl, 1
00276716  74 14                           je 0x14027672c
00276718  F6 C3 42                        test bl, 0x42
0027671B  0F 95 C1                        setne cl
0027671E  F6 C3 20                        test bl, 0x20
00276721  0F 95 C0                        setne al
00276724  84 C8                           test al, cl
00276726  0F 84 29 03 00 00               je 0x140276a55
0027672C  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00276731  48 BF 00 00 00 00 00 00 00 10   movabs rdi, 0x1000000000000000
0027673B  49 BE 00 00 00 00 40 00 00 00   movabs r14, 0x4000000000
00276745  45 8B C4                        mov r8d, r12d
00276748  49 B9 20 00 00 00 00 00 00 10   movabs r9, 0x1000000000000020
00276752  49 BA 00 00 00 00 00 00 00 20   movabs r10, 0x2000000000000000
0027675C  41 83 E0 01                     and r8d, 1
00276760  48 BA FF FF FF FF FF FF FF DF   movabs rdx, 0xdfffffffffffffff
0027676A  48 B9 00 00 00 00 10 00 00 00   movabs rcx, 0x1000000000
00276774  F6 C3 01                        test bl, 1
00276777  74 3F                           je 0x1402767b8
00276779  48 8B C3                        mov rax, rbx
0027677C  48 C1 E8 3C                     shr rax, 0x3c
00276780  A8 01                           test al, 1
00276782  0F 85 E5 04 00 00               jne 0x140276c6d
00276788  48 8B CB                        mov rcx, rbx
0027678B  48 23 CA                        and rcx, rdx
0027678E  49 0B C9                        or rcx, r9
00276791  48 F7 05 EC 02 D5 00 00 00 00 02  test qword ptr [rip + 0xd502ec], 0x2000000
0027679C  74 03                           je 0x1402767a1
0027679E  0F AE E8                        lfence
002767A1  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
002767A6  48 8B C3                        mov rax, rbx
002767A9  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
002767AE  48 8B D8                        mov rbx, rax
002767B1  74 11                           je 0x1402767c4
002767B3  45 85 C0                        test r8d, r8d
002767B6  74 A8                           je 0x140276760
002767B8  8B C6                           mov eax, esi
002767BA  BF 01 00 00 00                  mov edi, 1
002767BF  E9 18 FE FF FF                  jmp 0x1402765dc
002767C4  BF 01 00 00 00                  mov edi, 1
002767C9  8B C7                           mov eax, edi
002767CB  E9 0C FE FF FF                  jmp 0x1402765dc
002767D0  48 F7 05 AD 02 D5 00 00 00 60 00  test qword ptr [rip + 0xd502ad], 0x600000
002767DB  0F 84 4C FD FF FF               je 0x14027652d
002767E1  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002767EA  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
002767F2  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
002767F9  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00276800  0F 84 27 FD FF FF               je 0x14027652d
00276806  4C 8B 8A 08 05 00 00            mov r9, qword ptr [rdx + 0x508]
0027680D  4D 85 C9                        test r9, r9
00276810  0F 84 17 FD FF FF               je 0x14027652d
00276816  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0027681B  48 C1 E9 03                     shr rcx, 3
0027681F  81 E1 FF 01 00 00               and ecx, 0x1ff
00276825  49 8B 0C C9                     mov rcx, qword ptr [r9 + rcx*8]
00276829  F6 C1 20                        test cl, 0x20
0027682C  74 0C                           je 0x14027683a
0027682E  48 83 C8 20                     or rax, 0x20
00276832  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0027683A  F6 C1 42                        test cl, 0x42
0027683D  0F 84 EA FC FF FF               je 0x14027652d
00276843  48 83 C8 42                     or rax, 0x42
00276847  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0027684F  E9 D9 FC FF FF                  jmp 0x14027652d
00276854  83 E7 F7                        and edi, 0xfffffff7
00276857  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
0027685B  89 B4 24 68 01 00 00            mov dword ptr [rsp + 0x168], esi
00276862  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0027686C  48 8B C0                        mov rax, rax
0027686F  4C 3B F0                        cmp r14, rax
00276872  0F 85 5E 02 00 00               jne 0x140276ad6
00276878  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
0027687C  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00276885  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
0027688C  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00276890  24 0F                           and al, 0xf
00276892  0F 85 A0 03 00 00               jne 0x140276c38
00276898  BB 02 00 00 00                  mov ebx, 2
0027689D  44 8B F3                        mov r14d, ebx
002768A0  49 8D 95 B0 00 00 00            lea rdx, [r13 + 0xb0]
002768A7  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
002768AF  41 8B C6                        mov eax, r14d
002768B2  48 8D 0C 40                     lea rcx, [rax + rax*2]
002768B6  49 8D 04 C8                     lea rax, [r8 + rcx*8]
002768BA  48 8D 88 40 9C 00 00            lea rcx, [rax + 0x9c40]
002768C1  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
002768C9  48 89 90 48 9C 00 00            mov qword ptr [rax + 0x9c48], rdx
002768D0  48 89 31                        mov qword ptr [rcx], rsi
002768D3  90                              nop
002768D4  40 F6 C7 01                     test dil, 1
002768D8  0F 84 C7 04 00 00               je 0x140276da5
002768DE  E8 A5 0A 00 00                  call 0x140277388
002768E3  44 8B F0                        mov r14d, eax
002768E6  45 85 F6                        test r14d, r14d
002768E9  0F 84 F8 06 00 00               je 0x140276fe7
002768EF  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
002768F3  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
002768F8  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00276902  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027690C  E9 66 09 00 00                  jmp 0x140277277
00276911  C7 44 24 44 03 00 00 00         mov dword ptr [rsp + 0x44], 3
00276919  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0027691E  48 C1 E9 12                     shr rcx, 0x12
00276922  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
00276928  48 8B C3                        mov rax, rbx
0027692B  48 03 C8                        add rcx, rax
0027692E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00276933  E9 BA FB FF FF                  jmp 0x1402764f2
00276938  3C 07                           cmp al, 7
0027693A  0F 84 3E 05 00 00               je 0x140276e7e
00276940  3C 05                           cmp al, 5
00276942  0F 84 C9 08 00 00               je 0x140277211
00276948  BB 03 00 00 00                  mov ebx, 3
0027694D  8B C3                           mov eax, ebx
0027694F  48 8D 15 EA 61 BB 00            lea rdx, [rip + 0xbb61ea]
00276956  48 8D 14 C2                     lea rdx, [rdx + rax*8]
0027695A  48 81 C2 80 32 00 00            add rdx, 0x3280
00276961  E9 37 FC FF FF                  jmp 0x14027659d
00276966  49 8B C2                        mov rax, r10
00276969  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0027696E  48 3B C8                        cmp rcx, rax
00276971  0F 82 74 FD FF FF               jb 0x1402766eb
00276977  48 8B C2                        mov rax, rdx
0027697A  48 3B C8                        cmp rcx, rax
0027697D  0F 87 68 FD FF FF               ja 0x1402766eb
00276983  89 B4 24 78 01 00 00            mov dword ptr [rsp + 0x178], esi
0027698A  49 8B C2                        mov rax, r10
0027698D  48 2B C8                        sub rcx, rax
00276990  48 C1 F9 03                     sar rcx, 3
00276994  44 8D 34 09                     lea r14d, [rcx + rcx]
00276998  45 8B CE                        mov r9d, r14d
0027699B  41 83 E6 1F                     and r14d, 0x1f
0027699F  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
002769A6  49 C1 E9 05                     shr r9, 5
002769AA  48 8D 15 8F 61 BB 00            lea rdx, [rip + 0xbb618f]
002769B1  48 8D 92 6C 26 00 00            lea rdx, [rdx + 0x266c]
002769B8  4E 8D 0C 8A                     lea r9, [rdx + r9*4]
002769BC  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
002769C1  45 8B 11                        mov r10d, dword ptr [r9]
002769C4  41 8B C4                        mov eax, r12d
002769C7  83 E0 01                        and eax, 1
002769CA  BF 01 00 00 00                  mov edi, 1
002769CF  41 8B CE                        mov ecx, r14d
002769D2  44 8B C3                        mov r8d, ebx
002769D5  41 D3 E0                        shl r8d, cl
002769D8  44 8B D8                        mov r11d, eax
002769DB  41 8B CE                        mov ecx, r14d
002769DE  41 8B D2                        mov edx, r10d
002769E1  D3 EA                           shr edx, cl
002769E3  40 84 D7                        test dil, dl
002769E6  0F 85 E7 03 00 00               jne 0x140276dd3
002769EC  8B D7                           mov edx, edi
002769EE  D3 E2                           shl edx, cl
002769F0  41 0B D2                        or edx, r10d
002769F3  41 8B C0                        mov eax, r8d
002769F6  F7 D0                           not eax
002769F8  23 D0                           and edx, eax
002769FA  41 8B C2                        mov eax, r10d
002769FD  F0 41 0F B1 11                  lock cmpxchg dword ptr [r9], edx
00276A02  44 8B D0                        mov r10d, eax
00276A05  0F 84 17 08 00 00               je 0x140277222
00276A0B  41 8B C3                        mov eax, r11d
00276A0E  45 85 DB                        test r11d, r11d
00276A11  74 C5                           je 0x1402769d8
00276A13  E9 C3 03 00 00                  jmp 0x140276ddb
00276A18  48 BA FF DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedfff
00276A22  E9 AC FC FF FF                  jmp 0x1402766d3
00276A27  F6 05 D8 00 D5 00 21            test byte ptr [rip + 0xd500d8], 0x21
00276A2E  0F 85 DC 01 00 00               jne 0x140276c10
00276A34  48 87 0A                        xchg qword ptr [rdx], rcx
00276A37  48 85 C9                        test rcx, rcx
00276A3A  0F 84 E2 07 00 00               je 0x140277222
00276A40  48 8B D1                        mov rdx, rcx
00276A43  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00276A4B  E8 60 14 FE FF                  call 0x140257eb0
00276A50  E9 CD 07 00 00                  jmp 0x140277222
00276A55  48 F7 05 28 00 D5 00 00 00 60 00  test qword ptr [rip + 0xd50028], 0x600000
00276A60  0F 84 C6 FC FF FF               je 0x14027672c
00276A66  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00276A6F  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
00276A77  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00276A7E  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00276A85  0F 84 A1 FC FF FF               je 0x14027672c
00276A8B  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00276A92  48 85 D2                        test rdx, rdx
00276A95  0F 84 91 FC FF FF               je 0x14027672c
00276A9B  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00276AA0  48 C1 E8 03                     shr rax, 3
00276AA4  25 FF 01 00 00                  and eax, 0x1ff
00276AA9  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00276AAD  A8 20                           test al, 0x20
00276AAF  74 0C                           je 0x140276abd
00276AB1  48 83 CB 20                     or rbx, 0x20
00276AB5  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00276ABD  A8 42                           test al, 0x42
00276ABF  0F 84 67 FC FF FF               je 0x14027672c
00276AC5  48 83 CB 42                     or rbx, 0x42
00276AC9  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00276AD1  E9 56 FC FF FF                  jmp 0x14027672c
00276AD6  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00276ADD  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
00276AE4  A8 0F                           test al, 0xf
00276AE6  0F 85 AA 02 00 00               jne 0x140276d96
00276AEC  49 8B C2                        mov rax, r10
00276AEF  4C 3B F0                        cmp r14, rax
00276AF2  0F 82 9E 02 00 00               jb 0x140276d96
00276AF8  48 BA FF DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedfff
00276B02  48 8B C2                        mov rax, rdx
00276B05  4C 3B F0                        cmp r14, rax
00276B08  77 2F                           ja 0x140276b39
00276B0A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00276B13  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
00276B1B  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00276B22  48 8B 88 10 04 00 00            mov rcx, qword ptr [rax + 0x410]
00276B29  4C 8B 89 68 05 00 00            mov r9, qword ptr [rcx + 0x568]
00276B30  4D 85 C9                        test r9, r9
00276B33  0F 85 D3 05 00 00               jne 0x14027710c
00276B39  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00276B40  89 84 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], eax
00276B47  A8 0F                           test al, 0xf
00276B49  0F 85 7F 01 00 00               jne 0x140276cce
00276B4F  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00276B53  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00276B57  49 8B 1E                        mov rbx, qword ptr [r14]
00276B5A  49 8B C2                        mov rax, r10
00276B5D  4C 3B F0                        cmp r14, rax
00276B60  72 2E                           jb 0x140276b90
00276B62  49 8B C0                        mov rax, r8
00276B65  4C 3B F0                        cmp r14, rax
00276B68  77 26                           ja 0x140276b90
00276B6A  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00276B72  F6 C3 01                        test bl, 1
00276B75  74 14                           je 0x140276b8b
00276B77  F6 C3 42                        test bl, 0x42
00276B7A  0F 95 C1                        setne cl
00276B7D  F6 C3 20                        test bl, 0x20
00276B80  0F 95 C0                        setne al
00276B83  84 C8                           test al, cl
00276B85  0F 84 74 02 00 00               je 0x140276dff
00276B8B  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00276B90  8B D7                           mov edx, edi
00276B92  49 B9 20 00 00 00 00 00 00 10   movabs r9, 0x1000000000000020
00276B9C  49 B8 FF FF FF FF FF FF FF DF   movabs r8, 0xdfffffffffffffff
00276BA6  49 BA 00 00 00 00 00 00 00 20   movabs r10, 0x2000000000000000
00276BB0  83 E2 01                        and edx, 1
00276BB3  48 B9 00 00 00 00 10 00 00 00   movabs rcx, 0x1000000000
00276BBD  F6 C3 01                        test bl, 1
00276BC0  74 39                           je 0x140276bfb
00276BC2  48 8B C3                        mov rax, rbx
00276BC5  48 C1 E8 3C                     shr rax, 0x3c
00276BC9  A8 01                           test al, 1
00276BCB  0F 85 21 03 00 00               jne 0x140276ef2
00276BD1  48 8B CB                        mov rcx, rbx
00276BD4  49 23 C8                        and rcx, r8
00276BD7  49 0B C9                        or rcx, r9
00276BDA  48 F7 05 A3 FE D4 00 00 00 00 02  test qword ptr [rip + 0xd4fea3], 0x2000000
00276BE5  74 03                           je 0x140276bea
00276BE7  0F AE E8                        lfence
00276BEA  48 8B C3                        mov rax, rbx
00276BED  F0 49 0F B1 0E                  lock cmpxchg qword ptr [r14], rcx
00276BF2  48 8B D8                        mov rbx, rax
00276BF5  74 09                           je 0x140276c00
00276BF7  85 D2                           test edx, edx
00276BF9  74 B8                           je 0x140276bb3
00276BFB  44 8B F6                        mov r14d, esi
00276BFE  EB 06                           jmp 0x140276c06
00276C00  41 BE 01 00 00 00               mov r14d, 1
00276C06  BB 02 00 00 00                  mov ebx, 2
00276C0B  E9 D6 FC FF FF                  jmp 0x1402768e6
00276C10  8B 05 42 72 C9 00               mov eax, dword ptr [rip + 0xc97242]
00276C16  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00276C1E  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00276C26  85 C0                           test eax, eax
00276C28  0F 85 06 FE FF FF               jne 0x140276a34
00276C2E  E8 1D EC FF FF                  call 0x140275850
00276C33  E9 EA 05 00 00                  jmp 0x140277222
00276C38  3C 07                           cmp al, 7
00276C3A  0F 84 52 03 00 00               je 0x140276f92
00276C40  3C 05                           cmp al, 5
00276C42  0F 84 B7 05 00 00               je 0x1402771ff
00276C48  41 BE 03 00 00 00               mov r14d, 3
00276C4E  41 8B C6                        mov eax, r14d
00276C51  48 8D 15 E8 5E BB 00            lea rdx, [rip + 0xbb5ee8]
00276C58  48 8D 14 C2                     lea rdx, [rdx + rax*8]
00276C5C  48 81 C2 80 32 00 00            add rdx, 0x3280
00276C63  BB 02 00 00 00                  mov ebx, 2
00276C68  E9 3A FC FF FF                  jmp 0x1402768a7
00276C6D  45 85 C0                        test r8d, r8d
00276C70  0F 85 42 FB FF FF               jne 0x1402767b8
00276C76  A8 02                           test al, 2
00276C78  0F 85 22 02 00 00               jne 0x140276ea0
00276C7E  48 8B FB                        mov rdi, rbx
00276C81  49 0B FA                        or rdi, r10
00276C84  48 F7 05 F9 FD D4 00 00 00 00 02  test qword ptr [rip + 0xd4fdf9], 0x2000000
00276C8F  74 03                           je 0x140276c94
00276C91  0F AE E8                        lfence
00276C94  48 85 0D ED FD D4 00            test qword ptr [rip + 0xd4fded], rcx
00276C9B  0F 85 4F 03 00 00               jne 0x140276ff0
00276CA1  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00276CA6  48 8B C3                        mov rax, rbx
00276CA9  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
00276CAE  48 8B D8                        mov rbx, rax
00276CB1  48 0F 44 DF                     cmove rbx, rdi
00276CB5  48 BF 00 00 00 00 00 00 00 10   movabs rdi, 0x1000000000000000
00276CBF  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00276CC9  E9 77 FA FF FF                  jmp 0x140276745
00276CCE  49 8B C2                        mov rax, r10
00276CD1  4C 3B F0                        cmp r14, rax
00276CD4  0F 82 75 FE FF FF               jb 0x140276b4f
00276CDA  48 8B C2                        mov rax, rdx
00276CDD  4C 3B F0                        cmp r14, rax
00276CE0  0F 87 69 FE FF FF               ja 0x140276b4f
00276CE6  89 B4 24 68 01 00 00            mov dword ptr [rsp + 0x168], esi
00276CED  49 8B C2                        mov rax, r10
00276CF0  4C 2B F0                        sub r14, rax
00276CF3  49 C1 FE 03                     sar r14, 3
00276CF7  47 8D 24 36                     lea r12d, [r14 + r14]
00276CFB  45 8B CC                        mov r9d, r12d
00276CFE  41 83 E4 1F                     and r12d, 0x1f
00276D02  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00276D09  49 C1 E9 05                     shr r9, 5
00276D0D  48 8D 15 2C 5E BB 00            lea rdx, [rip + 0xbb5e2c]
00276D14  48 8D 92 6C 26 00 00            lea rdx, [rdx + 0x266c]
00276D1B  4E 8D 0C 8A                     lea r9, [rdx + r9*4]
00276D1F  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00276D24  45 8B 11                        mov r10d, dword ptr [r9]
00276D27  8B C7                           mov eax, edi
00276D29  83 E0 01                        and eax, 1
00276D2C  BB 02 00 00 00                  mov ebx, 2
00276D31  44 8D 73 FF                     lea r14d, [rbx - 1]
00276D35  41 8B CC                        mov ecx, r12d
00276D38  44 8B C3                        mov r8d, ebx
00276D3B  41 D3 E0                        shl r8d, cl
00276D3E  44 8B D8                        mov r11d, eax
00276D41  41 8B CC                        mov ecx, r12d
00276D44  41 8B D2                        mov edx, r10d
00276D47  D3 EA                           shr edx, cl
00276D49  41 84 D6                        test r14b, dl
00276D4C  0F 85 8D 02 00 00               jne 0x140276fdf
00276D52  41 8B D6                        mov edx, r14d
00276D55  D3 E2                           shl edx, cl
00276D57  41 0B D2                        or edx, r10d
00276D5A  41 8B C0                        mov eax, r8d
00276D5D  F7 D0                           not eax
00276D5F  23 D0                           and edx, eax
00276D61  41 8B C2                        mov eax, r10d
00276D64  F0 41 0F B1 11                  lock cmpxchg dword ptr [r9], edx
00276D69  44 8B D0                        mov r10d, eax
00276D6C  0F 84 7D FB FF FF               je 0x1402768ef
00276D72  41 8B C3                        mov eax, r11d
00276D75  45 85 DB                        test r11d, r11d
00276D78  74 C4                           je 0x140276d3e
00276D7A  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
00276D7E  E9 70 FB FF FF                  jmp 0x1402768f3
00276D83  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
00276D87  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00276D91  E9 E1 04 00 00                  jmp 0x140277277
00276D96  48 BA FF DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedfff
00276DA0  E9 94 FD FF FF                  jmp 0x140276b39
00276DA5  F6 05 5A FD D4 00 21            test byte ptr [rip + 0xd4fd5a], 0x21
00276DAC  0F 85 18 01 00 00               jne 0x140276eca
00276DB2  48 87 0A                        xchg qword ptr [rdx], rcx
00276DB5  48 85 C9                        test rcx, rcx
00276DB8  0F 84 31 FB FF FF               je 0x1402768ef
00276DBE  48 8B D1                        mov rdx, rcx
00276DC1  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00276DC9  E8 E2 10 FE FF                  call 0x140257eb0
00276DCE  E9 1C FB FF FF                  jmp 0x1402768ef
00276DD3  85 C0                           test eax, eax
00276DD5  0F 84 7F 02 00 00               je 0x14027705a
00276DDB  8B DE                           mov ebx, esi
00276DDD  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00276DE1  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00276DE6  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00276DF0  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00276DFA  E9 78 04 00 00                  jmp 0x140277277
00276DFF  48 F7 05 7E FC D4 00 00 00 60 00  test qword ptr [rip + 0xd4fc7e], 0x600000
00276E0A  0F 84 7B FD FF FF               je 0x140276b8b
00276E10  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00276E19  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00276E21  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00276E28  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00276E2F  0F 84 56 FD FF FF               je 0x140276b8b
00276E35  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00276E3C  48 85 D2                        test rdx, rdx
00276E3F  0F 84 46 FD FF FF               je 0x140276b8b
00276E45  49 8B C6                        mov rax, r14
00276E48  48 C1 E8 03                     shr rax, 3
00276E4C  25 FF 01 00 00                  and eax, 0x1ff
00276E51  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00276E55  A8 20                           test al, 0x20
00276E57  74 0C                           je 0x140276e65
00276E59  48 83 CB 20                     or rbx, 0x20
00276E5D  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00276E65  A8 42                           test al, 0x42
00276E67  0F 84 1E FD FF FF               je 0x140276b8b
00276E6D  48 83 CB 42                     or rbx, 0x42
00276E71  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00276E79  E9 0D FD FF FF                  jmp 0x140276b8b
00276E7E  8B DF                           mov ebx, edi
00276E80  E9 C8 FA FF FF                  jmp 0x14027694d
00276E85  8B DE                           mov ebx, esi
00276E87  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00276E8B  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00276E90  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00276E9A  E9 D8 03 00 00                  jmp 0x140277277
00276E9F  90                              nop
00276EA0  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00276EA4  FF C3                           inc ebx
00276EA6  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00276EAA  85 1D FC E3 D4 00               test dword ptr [rip + 0xd4e3fc], ebx
00276EB0  0F 84 91 00 00 00               je 0x140276f47
00276EB6  F3 90                           pause
00276EB8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00276EBD  48 8B 1B                        mov rbx, qword ptr [rbx]
00276EC0  48 85 DF                        test rdi, rbx
00276EC3  75 DB                           jne 0x140276ea0
00276EC5  E9 F5 FD FF FF                  jmp 0x140276cbf
00276ECA  8B 05 88 6F C9 00               mov eax, dword ptr [rip + 0xc96f88]
00276ED0  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00276ED8  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00276EE0  85 C0                           test eax, eax
00276EE2  0F 85 CA FE FF FF               jne 0x140276db2
00276EE8  E8 63 E9 FF FF                  call 0x140275850
00276EED  E9 FD F9 FF FF                  jmp 0x1402768ef
00276EF2  85 D2                           test edx, edx
00276EF4  0F 85 01 FD FF FF               jne 0x140276bfb
00276EFA  A8 02                           test al, 2
00276EFC  0F 85 9E 00 00 00               jne 0x140276fa0
00276F02  48 8B FB                        mov rdi, rbx
00276F05  49 0B FA                        or rdi, r10
00276F08  48 F7 05 75 FB D4 00 00 00 00 02  test qword ptr [rip + 0xd4fb75], 0x2000000
00276F13  74 03                           je 0x140276f18
00276F15  0F AE E8                        lfence
00276F18  48 85 0D 69 FB D4 00            test qword ptr [rip + 0xd4fb69], rcx
00276F1F  0F 85 AA 01 00 00               jne 0x1402770cf
00276F25  48 8B C3                        mov rax, rbx
00276F28  F0 49 0F B1 3E                  lock cmpxchg qword ptr [r14], rdi
00276F2D  48 8B D8                        mov rbx, rax
00276F30  48 0F 44 DF                     cmove rbx, rdi
00276F34  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
00276F38  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00276F42  E9 49 FC FF FF                  jmp 0x140276b90
00276F47  8B 05 6B FB D4 00               mov eax, dword ptr [rip + 0xd4fb6b]
00276F4D  A8 40                           test al, 0x40
00276F4F  0F 84 61 FF FF FF               je 0x140276eb6
00276F55  E8 36 85 09 00                  call 0x14030f490
00276F5A  84 C0                           test al, al
00276F5C  0F 84 54 FF FF FF               je 0x140276eb6
00276F62  8B CB                           mov ecx, ebx
00276F64  E8 F7 84 09 00                  call 0x14030f460
00276F69  E9 4A FF FF FF                  jmp 0x140276eb8
00276F6E  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00276F72  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00276F76  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00276F7B  48 C1 E9 09                     shr rcx, 9
00276F7F  48 23 CA                        and rcx, rdx
00276F82  49 8B C3                        mov rax, r11
00276F85  48 03 C8                        add rcx, rax
00276F88  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00276F8D  E9 65 F5 FF FF                  jmp 0x1402764f7
00276F92  41 BE 01 00 00 00               mov r14d, 1
00276F98  E9 B1 FC FF FF                  jmp 0x140276c4e
00276F9D  0F 1F 00                        nop dword ptr [rax]
00276FA0  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
00276FA4  FF C3                           inc ebx
00276FA6  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00276FAA  85 1D FC E2 D4 00               test dword ptr [rip + 0xd4e2fc], ebx
00276FB0  74 11                           je 0x140276fc3
00276FB2  F3 90                           pause
00276FB4  49 8B 1E                        mov rbx, qword ptr [r14]
00276FB7  48 0F BA E3 3C                  bt rbx, 0x3c
00276FBC  72 E2                           jb 0x140276fa0
00276FBE  E9 75 FF FF FF                  jmp 0x140276f38
00276FC3  8B 05 EF FA D4 00               mov eax, dword ptr [rip + 0xd4faef]
00276FC9  A8 40                           test al, 0x40
00276FCB  74 E5                           je 0x140276fb2
00276FCD  E8 BE 84 09 00                  call 0x14030f490
00276FD2  84 C0                           test al, al
00276FD4  74 DC                           je 0x140276fb2
00276FD6  8B CB                           mov ecx, ebx
00276FD8  E8 83 84 09 00                  call 0x14030f460
00276FDD  EB D5                           jmp 0x140276fb4
00276FDF  85 C0                           test eax, eax
00276FE1  0F 84 43 01 00 00               je 0x14027712a
00276FE7  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
00276FEB  E9 03 F9 FF FF                  jmp 0x1402768f3
00276FF0  40 0F B6 C7                     movzx eax, dil
00276FF4  24 21                           and al, 0x21
00276FF6  3C 01                           cmp al, 1
00276FF8  0F 85 A3 FC FF FF               jne 0x140276ca1
00276FFE  49 8B C3                        mov rax, r11
00277001  49 03 C6                        add rax, r14
00277004  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
00277009  4C 3B C8                        cmp r9, rax
0027700C  0F 82 8F FC FF FF               jb 0x140276ca1
00277012  41 B8 80 00 00 00               mov r8d, 0x80
00277018  48 8B D7                        mov rdx, rdi
0027701B  49 8B C9                        mov rcx, r9
0027701E  E8 5D BD 01 00                  call 0x140292d80
00277023  E9 79 FC FF FF                  jmp 0x140276ca1
00277028  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0027702C  C1 E8 03                        shr eax, 3
0027702F  25 FF 01 00 00                  and eax, 0x1ff
00277034  49 8D 0C 81                     lea rcx, [r9 + rax*4]
00277038  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
0027703F  A8 04                           test al, 4
00277041  0F 85 3D 01 00 00               jne 0x140277184
00277047  A8 01                           test al, 1
00277049  75 6D                           jne 0x1402770b8
0027704B  E8 30 1E FD FF                  call 0x140248e80
00277050  BF 01 00 00 00                  mov edi, 1
00277055  E9 C8 01 00 00                  jmp 0x140277222
0027705A  84 D3                           test bl, dl
0027705C  75 22                           jne 0x140277080
0027705E  45 0B C2                        or r8d, r10d
00277061  41 8B C2                        mov eax, r10d
00277064  F0 45 0F B1 01                  lock cmpxchg dword ptr [r9], r8d
00277069  44 8B D0                        mov r10d, eax
0027706C  45 0F 44 D0                     cmove r10d, r8d
00277070  41 8B C4                        mov eax, r12d
00277073  23 C7                           and eax, edi
00277075  E9 55 F9 FF FF                  jmp 0x1402769cf
0027707A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00277080  8B 84 24 78 01 00 00            mov eax, dword ptr [rsp + 0x178]
00277087  FF C0                           inc eax
00277089  89 84 24 78 01 00 00            mov dword ptr [rsp + 0x178], eax
00277090  85 05 16 E2 D4 00               test dword ptr [rip + 0xd4e216], eax
00277096  0F 84 F7 00 00 00               je 0x140277193
0027709C  F3 90                           pause
0027709E  45 8B 11                        mov r10d, dword ptr [r9]
002770A1  41 8B C2                        mov eax, r10d
002770A4  41 8B CE                        mov ecx, r14d
002770A7  D3 E8                           shr eax, cl
002770A9  40 84 C7                        test dil, al
002770AC  75 D2                           jne 0x140277080
002770AE  41 8B C4                        mov eax, r12d
002770B1  23 C7                           and eax, edi
002770B3  E9 17 F9 FF FF                  jmp 0x1402769cf
002770B8  E8 43 47 04 00                  call 0x1402bb800
002770BD  85 C0                           test eax, eax
002770BF  0F 84 16 FD FF FF               je 0x140276ddb
002770C5  BF 01 00 00 00                  mov edi, 1
002770CA  E9 53 01 00 00                  jmp 0x140277222
002770CF  40 0F B6 C7                     movzx eax, dil
002770D3  24 21                           and al, 0x21
002770D5  3C 01                           cmp al, 1
002770D7  0F 85 48 FE FF FF               jne 0x140276f25
002770DD  49 8B C3                        mov rax, r11
002770E0  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
002770EA  48 03 C1                        add rax, rcx
002770ED  4C 3B F0                        cmp r14, rax
002770F0  0F 82 2F FE FF FF               jb 0x140276f25
002770F6  41 B8 80 00 00 00               mov r8d, 0x80
002770FC  48 8B D7                        mov rdx, rdi
002770FF  49 8B CE                        mov rcx, r14
00277102  E8 79 BC 01 00                  call 0x140292d80
00277107  E9 19 FE FF FF                  jmp 0x140276f25
0027710C  41 C1 EE 03                     shr r14d, 3
00277110  41 81 E6 FF 01 00 00            and r14d, 0x1ff
00277117  4B 8D 0C B1                     lea rcx, [r9 + r14*4]
0027711B  E8 10 1D FD FF                  call 0x140248e30
00277120  BB 02 00 00 00                  mov ebx, 2
00277125  E9 C5 F7 FF FF                  jmp 0x1402768ef
0027712A  84 D3                           test bl, dl
0027712C  75 22                           jne 0x140277150
0027712E  45 0B C2                        or r8d, r10d
00277131  41 8B C2                        mov eax, r10d
00277134  F0 45 0F B1 01                  lock cmpxchg dword ptr [r9], r8d
00277139  44 8B D0                        mov r10d, eax
0027713C  45 0F 44 D0                     cmove r10d, r8d
00277140  8B C7                           mov eax, edi
00277142  41 23 C6                        and eax, r14d
00277145  E9 EB FB FF FF                  jmp 0x140276d35
0027714A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00277150  8B 84 24 68 01 00 00            mov eax, dword ptr [rsp + 0x168]
00277157  FF C0                           inc eax
00277159  89 84 24 68 01 00 00            mov dword ptr [rsp + 0x168], eax
00277160  85 05 46 E1 D4 00               test dword ptr [rip + 0xd4e146], eax
00277166  74 58                           je 0x1402771c0
00277168  F3 90                           pause
0027716A  45 8B 11                        mov r10d, dword ptr [r9]
0027716D  41 8B C2                        mov eax, r10d
00277170  41 8B CC                        mov ecx, r12d
00277173  D3 E8                           shr eax, cl
00277175  41 84 C6                        test r14b, al
00277178  75 D6                           jne 0x140277150
0027717A  8B C7                           mov eax, edi
0027717C  41 23 C6                        and eax, r14d
0027717F  E9 B1 FB FF FF                  jmp 0x140276d35
00277184  E8 A7 1C FD FF                  call 0x140248e30
00277189  BF 01 00 00 00                  mov edi, 1
0027718E  E9 8F 00 00 00                  jmp 0x140277222
00277193  8B 05 1F F9 D4 00               mov eax, dword ptr [rip + 0xd4f91f]
00277199  A8 40                           test al, 0x40
0027719B  0F 84 FB FE FF FF               je 0x14027709c
002771A1  E8 EA 82 09 00                  call 0x14030f490
002771A6  84 C0                           test al, al
002771A8  74 6E                           je 0x140277218
002771AA  8B 8C 24 78 01 00 00            mov ecx, dword ptr [rsp + 0x178]
002771B1  E8 AA 82 09 00                  call 0x14030f460
002771B6  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
002771BB  E9 DE FE FF FF                  jmp 0x14027709e
002771C0  8B 05 F2 F8 D4 00               mov eax, dword ptr [rip + 0xd4f8f2]
002771C6  A8 40                           test al, 0x40
002771C8  74 9E                           je 0x140277168
002771CA  E8 C1 82 09 00                  call 0x14030f490
002771CF  84 C0                           test al, al
002771D1  74 34                           je 0x140277207
002771D3  8B 8C 24 68 01 00 00            mov ecx, dword ptr [rsp + 0x168]
002771DA  E8 81 82 09 00                  call 0x14030f460
002771DF  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
002771E4  EB 84                           jmp 0x14027716a
002771E6  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
002771F0  49 B8 F8 D7 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed7f8
002771FA  E9 F3 F2 FF FF                  jmp 0x1402764f2
002771FF  44 8B F6                        mov r14d, esi
00277202  E9 47 FA FF FF                  jmp 0x140276c4e
00277207  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0027720C  E9 57 FF FF FF                  jmp 0x140277168
00277211  8B DE                           mov ebx, esi
00277213  E9 35 F7 FF FF                  jmp 0x14027694d
00277218  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0027721D  E9 7A FE FF FF                  jmp 0x14027709c
00277222  8B DF                           mov ebx, edi
00277224  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00277228  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0027722D  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00277237  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00277241  EB 34                           jmp 0x140277277
00277243  33 DB                           xor ebx, ebx
00277245  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00277249  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
00277253  33 F6                           xor esi, esi
00277255  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027725F  4C 8B AC 24 60 01 00 00         mov r13, qword ptr [rsp + 0x160]
00277267  4C 8B 8C 24 E0 00 00 00         mov r9, qword ptr [rsp + 0xe0]
0027726F  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
00277277  41 89 37                        mov dword ptr [r15], esi
0027727A  85 DB                           test ebx, ebx
0027727C  74 0C                           je 0x14027728a
0027727E  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00277282  85 FF                           test edi, edi
00277284  0F 85 B4 00 00 00               jne 0x14027733e
0027728A  8B C3                           mov eax, ebx
0027728C  48 81 C4 20 01 00 00            add rsp, 0x120
00277293  41 5F                           pop r15
00277295  41 5E                           pop r14
00277297  41 5D                           pop r13
00277299  41 5C                           pop r12
0027729B  5F                              pop rdi
0027729C  5E                              pop rsi
0027729D  5B                              pop rbx
0027729E  C3                              ret
0027729F  CC                              int3
002772A0  4C 8B 0D 39 FB D4 00            mov r9, qword ptr [rip + 0xd4fb39]
002772A7  49 C1 E1 0C                     shl r9, 0xc
002772AB  48 B9 FF FF FF FF 7F 00 00 00   movabs rcx, 0x7fffffffff
002772B5  4C 03 C9                        add r9, rcx
002772B8  4C 03 0D 79 F9 D4 00            add r9, qword ptr [rip + 0xd4f979]
002772BF  48 B8 00 00 00 00 80 FF FF FF   movabs rax, 0xffffff8000000000
002772C9  4C 23 C8                        and r9, rax
002772CC  48 3B 15 65 F9 D4 00            cmp rdx, qword ptr [rip + 0xd4f965]
002772D3  72 09                           jb 0x1402772de
002772D5  49 3B D1                        cmp rdx, r9
002772D8  0F 82 9D 00 00 00               jb 0x14027737b
002772DE  BF 01 00 00 00                  mov edi, 1
002772E3  E9 CC F0 FF FF                  jmp 0x1402763b4
002772E8  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002772F2  48 3B D0                        cmp rdx, rax
002772F5  0F 87 7A F0 FF FF               ja 0x140276375
002772FB  45 8B C8                        mov r9d, r8d
002772FE  33 F6                           xor esi, esi
00277300  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00277305  4C 8B C2                        mov r8, rdx
00277308  BA 80 13 00 00                  mov edx, 0x1380
0027730D  8D 4E 1A                        lea ecx, [rsi + 0x1a]
00277310  E8 4B 63 28 00                  call 0x1404fd660
00277315  CC                              int3
00277316  48 8B 05 EB 18 BC 00            mov rax, qword ptr [rip + 0xbc18eb]
0027731D  48 8B 0D EC 18 BC 00            mov rcx, qword ptr [rip + 0xbc18ec]
00277324  48 3B D0                        cmp rdx, rax
00277327  72 08                           jb 0x140277331
00277329  48 03 C1                        add rax, rcx
0027732C  48 3B D0                        cmp rdx, rax
0027732F  72 4A                           jb 0x14027737b
00277331  BF 01 00 00 00                  mov edi, 1
00277336  44 8B C7                        mov r8d, edi
00277339  E9 76 F0 FF FF                  jmp 0x1402763b4
0027733E  83 FF 03                        cmp edi, 3
00277341  75 0D                           jne 0x140277350
00277343  49 C1 E9 09                     shr r9, 9
00277347  4C 23 C8                        and r9, rax
0027734A  49 8B C3                        mov rax, r11
0027734D  4C 03 C8                        add r9, rax
00277350  49 8B C9                        mov rcx, r9
00277353  E8 48 B5 00 00                  call 0x1402828a0
00277358  24 81                           and al, 0x81
0027735A  3C 81                           cmp al, 0x81
0027735C  75 10                           jne 0x14027736e
0027735E  8B DE                           mov ebx, esi
00277360  83 FF 03                        cmp edi, 3
00277363  0F 94 C3                        sete bl
00277366  83 C3 02                        add ebx, 2
00277369  E9 1C FF FF FF                  jmp 0x14027728a
0027736E  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00277373  49 8B CD                        mov rcx, r13
00277376  E8 45 FB F9 FF                  call 0x140216ec0
0027737B  33 C0                           xor eax, eax
0027737D  E9 0A FF FF FF                  jmp 0x14027728c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFastLockLeafPageTable(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (288);
    if (a2 >= v_r11) goto loc_002772E8;
loc_00276375:
    v_rsi = 0;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(a1)) == 7) goto loc_002772DE;
    if (((unsigned __int8)(a1 - 1)) <= 1) goto loc_002772DE;
    if (((unsigned __int8)(a1)) == 5) goto loc_00277316;
    if (((unsigned __int8)(a1)) == 3) goto loc_002772A0;
    a3 = 0;
    if ((unsigned __int8)(a1) == 0) { a3 = 1; }
loc_002763B4:
    if (((*(unsigned __int64 *)(v_rip + 13960889)) & (0x800000ULL)) == 0) goto loc_0027737B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_0027737B;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 320;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 320)) != 0) goto loc_0027737B;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 320) = 1;
    v_stack_m114 = 0;
    v_stack_m120 = 0;
    a2 = (a2) >> (18);
    a2 = (unsigned int)((a2) & (0x3FFFFFF8ULL));
    v_stack_mE0 = a2 + v_rbx * 1;
    v_stack_m78 = a2 + v_rbx * 1;
    v_stack_m128 = a2 + v_rbx * 1;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_p18)) | (2));
    v_stack_p18 = (unsigned int)(v_r12);
    if (a3 == 0) goto loc_002771E6;
    v_stack_m80 = 0;
    v_r14 = (a2 + v_rbx * 1) >> (9);
    v_r14 = (v_r14) & (a2);
    v_r14 = (v_r14) + (v_r11);
    v_stack_m80 = v_r14;
    if (v_r14 < v_r10) goto loc_002764CC;
    if (v_r14 > a3) goto loc_002764CC;
    v_stack_mB0 = *(unsigned __int64 *)(v_r14);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_002764C7;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_002765E9;
loc_002764BD:
loc_002764C7:
    v_stack_m100 = *(unsigned __int64 *)(v_r14);
loc_002764CC:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_00276D83;
    if (sign_flag) goto loc_00276911;
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (8)) != 0) goto loc_00276854;
loc_002764F2:
loc_002764F7:
    if (v_stack_m128 < v_r10) goto loc_0027653C;
    if (v_stack_m128 > a3) goto loc_0027653C;
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_m128);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (1)) == 0) goto loc_00276537;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_002767D0;
loc_0027652D:
loc_00276537:
    v_stack_mF0 = *(unsigned __int64 *)(v_stack_m128);
loc_0027653C:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (1)) == 0) goto loc_00276E85;
    if (sign_flag) goto loc_00276F6E;
    v_stack_p20 = 0;
    if (v_stack_m128 != (*(unsigned __int64 *)(v_stack_m128))) goto loc_0027666B;
    v_stack_mD8 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00276938;
loc_0027659D:
    v_stack_mC0 = a1 + 176;
    v_stack_mB8 = *(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40000;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40008) = a1 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40000) = 0;
    if (((v_stack_p18) & (1)) == 0) goto loc_00276A27;
    result = KxTryToAcquireQueuedSpinLock(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40000, a1 + 176, *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m128);
loc_002765DC:
    if ((unsigned int)(result) == 0) goto loc_00276DDB;
    goto loc_00277222;
loc_002765E9:
    if (((*(unsigned __int64 *)(v_rip + 13960340)) & (0x600000ULL)) == 0) goto loc_002764BD;
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002764BD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002764BD;
    a1 = (v_r14) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
        v_stack_mB0 = result;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) goto loc_002764BD;
    result = (result) | (66);
    v_stack_mB0 = result;
    goto loc_002764BD;
loc_0027666B:
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_00276A18;
    if (v_stack_m128 < v_r10) goto loc_00276A18;
    if (v_stack_m128 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288))) goto loc_002766D3;
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_00277028;
loc_002766D3:
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_00276966;
loc_002766EB:
    v_stack_m118 = 0;
    v_stack_m118 = 0;
    if (v_stack_m128 < v_r10) goto loc_00276731;
    if (v_stack_m128 > (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00276731;
    v_stack_m98 = *(unsigned __int64 *)(v_stack_m128);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (1)) == 0) goto loc_0027672C;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00276A55;
loc_0027672C:
    v_stack_mE8 = *(unsigned __int64 *)(v_stack_m128);
loc_00276731:
loc_00276745:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (1));
loc_00276760:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m128))) & (1)) == 0) goto loc_002767B8;
    result = (*(unsigned __int64 *)(v_stack_m128)) >> (60);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00276C6D;
    a1 = (*(unsigned __int64 *)(v_stack_m128)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
    a1 = (a1) | (v_stack_m128);
    if (((*(unsigned __int64 *)(v_rip + 13959916)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13959916)) & (0x2000000ULL)) == 0) goto loc_002767C4;
    if (a3 == 0) goto loc_00276760;
loc_002767B8:
    goto loc_002765DC;
loc_002767C4:
    goto loc_002765DC;
loc_002767D0:
    if (((*(unsigned __int64 *)(v_rip + 13959853)) & (0x600000ULL)) == 0) goto loc_0027652D;
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0027652D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0027652D;
    a1 = (v_stack_m128) >> (3);
    a1 = (unsigned int)((a1) & (511));
    result = 1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (1) | (32);
        v_stack_mA0 = result;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) goto loc_0027652D;
    result = (result) | (66);
    v_stack_mA0 = result;
    goto loc_0027652D;
loc_00276854:
    v_rdi = (unsigned int)((1) & (0xFFFFFFF7ULL));
    v_stack_m110 = (unsigned int)(v_rdi);
    v_stack_p10 = 0;
    if (v_r14 != result) goto loc_00276AD6;
    v_stack_m110 = 0;
    v_stack_m110 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00276C38;
loc_002768A7:
    v_stack_mD0 = a1 + 176;
    v_stack_mC8 = *(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40000;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40008) = a1 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40000) = 0;
    if ((((unsigned __int8)(v_rdi)) & (1)) == 0) goto loc_00276DA5;
    result = KxTryToAcquireQueuedSpinLock(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 * 2 * 8 + 40000, a1 + 176, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
loc_002768E6:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00276FE7;
loc_002768EF:
    v_stack_m120 = 2;
loc_002768F3:
    goto loc_00277277;
loc_00276911:
    v_stack_m114 = 3;
    a1 = (v_stack_m128) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    a1 = (a1) + (2);
    v_stack_m128 = a1;
    goto loc_002764F2;
loc_00276938:
    if (2 == 7) goto loc_00276E7E;
    if (2 == 5) goto loc_00277211;
loc_0027694D:
    a2 = (v_rip + 12280298 + 3 * 8) + (0x3280ULL);
    goto loc_0027659D;
loc_00276966:
    if (v_stack_m128 < v_r10) goto loc_002766EB;
    if (v_stack_m128 > a2) goto loc_002766EB;
    v_stack_p20 = 0;
    a1 = (v_stack_m128) - (v_r10);
    a1 = (a1) >> (3);
    v_r14 = (unsigned int)((a1 + a1 * 1) & (31));
    a4 = ((unsigned int)((unsigned int)(a1 + a1 * 1))) >> (5);
    v_stack_m108 = v_rip + 12280207 + 9836 + a4 * 4;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (1));
loc_002769CF:
    a3 = (unsigned int)((3) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
loc_002769D8:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    if (((1) & ((unsigned __int8)(a2))) != 0) goto loc_00276DD3;
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    a2 = (unsigned int)((a2) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4)))));
    result = (unsigned int)(~((unsigned int)(a3)));
    a2 = (unsigned int)((a2) & ((unsigned int)(result)));
    if (condition_is_equal) goto loc_00277222;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_002769D8;
    goto loc_00276DDB;
loc_00276A18:
    goto loc_002766D3;
loc_00276A27:
    if (((*(unsigned __int8 *)(v_rip + 13959384)) & (33)) != 0) goto loc_00276C10;
loc_00276A34:
    if ((unsigned int)((unsigned int)(v_r14)) == 0) goto loc_00277222;
    result = KxWaitForLockOwnerShip(v_stack_mB8, (unsigned int)((unsigned int)(v_r14)), a3, v_rip + 12280207 + 9836 + a4 * 4);
    goto loc_00277222;
loc_00276A55:
    if (((*(unsigned __int64 *)(v_rip + 13959208)) & (0x600000ULL)) == 0) goto loc_0027672C;
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0027672C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0027672C;
    result = (v_stack_m128) >> (3);
    result = (unsigned int)((result) & (511));
    v_rbx = 3;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (3) | (32);
        v_stack_m98 = v_rbx;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) goto loc_0027672C;
    v_rbx = (v_rbx) | (66);
    v_stack_m98 = v_rbx;
    goto loc_0027672C;
loc_00276AD6:
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_00276D96;
    if (v_r14 < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4)))))))) goto loc_00276D96;
    if (v_r14 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288))) goto loc_00276B39;
    v_stack_m60 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_0027710C;
loc_00276B39:
    v_stack_m8C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_00276CCE;
loc_00276B4F:
    v_stack_m11C = 0;
    v_stack_m11C = 0;
    if (v_r14 < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4)))))))) goto loc_00276B90;
    if (v_r14 > a3) goto loc_00276B90;
    v_stack_mA8 = *(unsigned __int64 *)(v_r14);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_00276B8B;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00276DFF;
loc_00276B8B:
    v_stack_mF8 = *(unsigned __int64 *)(v_r14);
loc_00276B90:
    a2 = (unsigned int)((1) & (1));
loc_00276BB3:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_00276BFB;
    result = (*(unsigned __int64 *)(v_r14)) >> (60);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00276EF2;
    a1 = (*(unsigned __int64 *)(v_r14)) & (a3);
    a1 = (a1) | (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384));
    if (((*(unsigned __int64 *)(v_rip + 13958819)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13958819)) & (0x2000000ULL)) == 0) goto loc_00276C00;
    if ((unsigned int)(a2) == 0) goto loc_00276BB3;
loc_00276BFB:
    goto loc_00276C06;
loc_00276C00:
loc_00276C06:
    goto loc_002768E6;
loc_00276C10:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13201986))) != 0) goto loc_00276A34;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mB8, v_stack_mC0, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384));
    goto loc_00277222;
loc_00276C38:
    if (((unsigned __int8)(result)) == 7) goto loc_00276F92;
    if (((unsigned __int8)(result)) == 5) goto loc_002771FF;
loc_00276C4E:
    a2 = (v_rip + 12279528 + 3 * 8) + (0x3280ULL);
    goto loc_002768A7;
loc_00276C6D:
    if (a3 != 0) goto loc_002767B8;
    if (((3) & (2)) != 0) goto loc_00276EA0;
    v_rdi = (2) | ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4)))))));
    if (((*(unsigned __int64 *)(v_rip + 13958649)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13958637)) & (v_stack_mB8)) != 0) goto loc_00276FF0;
loc_00276CA1:
    v_rbx = 2;
    if (((*(unsigned __int64 *)(v_rip + 13958637)) & (v_stack_mB8)) == 0) { v_rbx = v_rdi; }
loc_00276CBF:
    goto loc_00276745;
loc_00276CCE:
    if (3 < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4)))))))) goto loc_00276B4F;
    if (3 > a2) goto loc_00276B4F;
    v_stack_p10 = 0;
    v_r14 = (3) - ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12280207 + 9836 + a4 * 4)))))));
    v_r14 = (v_r14) >> (3);
    v_r12 = (unsigned int)((v_r14 + v_r14 * 1) & (31));
    a4 = ((unsigned int)((unsigned int)(v_r14 + v_r14 * 1))) >> (5);
    v_stack_m108 = v_rip + 12279340 + 9836 + a4 * 4;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (1));
loc_00276D35:
    a3 = (unsigned int)((2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
loc_00276D3E:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12279340 + 9836 + a4 * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
    if ((((unsigned __int8)(2 - 1)) & ((unsigned __int8)(a2))) != 0) goto loc_00276FDF;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(2 - 1))) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
    a2 = (unsigned int)((a2) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12279340 + 9836 + a4 * 4)))));
    result = (unsigned int)(~((unsigned int)(a3)));
    a2 = (unsigned int)((a2) & ((unsigned int)(result)));
    if (condition_is_equal) goto loc_002768EF;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00276D3E;
    goto loc_002768F3;
loc_00276D83:
    goto loc_00277277;
loc_00276D96:
    goto loc_00276B39;
loc_00276DA5:
    if (((*(unsigned __int8 *)(v_rip + 13958490)) & (33)) != 0) goto loc_00276ECA;
loc_00276DB2:
    if ((unsigned int)((unsigned int)(v_r12)) == 0) goto loc_002768EF;
    result = KxWaitForLockOwnerShip(v_stack_mC8, (unsigned int)((unsigned int)(v_r12)), a3, v_rip + 12279340 + 9836 + a4 * 4);
    goto loc_002768EF;
loc_00276DD3:
    if ((unsigned int)(result) == 0) goto loc_0027705A;
loc_00276DDB:
    v_stack_m120 = 0;
    goto loc_00277277;
loc_00276DFF:
    if (((*(unsigned __int64 *)(v_rip + 13958270)) & (0x600000ULL)) == 0) goto loc_00276B8B;
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00276B8B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00276B8B;
    result = (2 - 1) >> (3);
    result = (unsigned int)((result) & (511));
    v_rbx = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (0) | (32);
        v_stack_mA8 = v_rbx;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) goto loc_00276B8B;
    v_rbx = (v_rbx) | (66);
    v_stack_mA8 = v_rbx;
    goto loc_00276B8B;
loc_00276E7E:
    goto loc_0027694D;
loc_00276E85:
    v_stack_m120 = 0;
    goto loc_00277277;
loc_00276EA0:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m118)) + 1);
    v_stack_m118 = (unsigned int)(v_rbx);
    if (((*(unsigned int *)(v_rip + 13951996)) & ((unsigned int)(v_rbx))) == 0) goto loc_00276F47;
loc_00276EB6:
loc_00276EB8:
    if (((v_rdi) & (*(unsigned __int64 *)(v_stack_m128))) != 0) goto loc_00276EA0;
    goto loc_00276CBF;
loc_00276ECA:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13201288))) != 0) goto loc_00276DB2;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mC8, v_stack_mD0, a3, v_stack_mE0);
    goto loc_002768EF;
loc_00276EF2:
    if ((unsigned int)(v_stack_mD0) != 0) goto loc_00276BFB;
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00276FA0;
    v_rdi = (*(unsigned __int64 *)(v_stack_m128)) | ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12279340 + 9836 + a4 * 4)))))));
    if (((*(unsigned __int64 *)(v_rip + 13958005)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13957993)) & (v_stack_mC8)) != 0) goto loc_002770CF;
loc_00276F25:
    v_rbx = *(unsigned __int64 *)(v_stack_m128);
    if (((*(unsigned __int64 *)(v_rip + 13957993)) & (v_stack_mC8)) == 0) { v_rbx = v_rdi; }
loc_00276F38:
    goto loc_00276B90;
loc_00276F47:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13957995)))) & (64)) == 0) goto loc_00276EB6;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_mC8, v_stack_mD0, a3, v_stack_mE0);
    if ((unsigned __int8)(result) == 0) goto loc_00276EB6;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_mD0, a3, v_stack_mE0);
    goto loc_00276EB8;
loc_00276F6E:
    v_stack_m120 = (unsigned int)(v_rbx);
    v_stack_m114 = (unsigned int)(v_rbx);
    a1 = (v_stack_m128) >> (9);
    a1 = (a1) & (v_stack_mD0);
    a1 = (a1) + ((unsigned int)((unsigned int)(result)));
    v_stack_m128 = a1;
    goto loc_002764F7;
loc_00276F92:
    goto loc_00276C4E;
loc_00276FA0:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m11C)) + 1);
    v_stack_m11C = (unsigned int)(v_rbx);
    if (((*(unsigned int *)(v_rip + 13951740)) & ((unsigned int)(v_rbx))) == 0) goto loc_00276FC3;
loc_00276FB2:
loc_00276FB4:
    if (condition_is_below) goto loc_00276FA0;
    goto loc_00276F38;
loc_00276FC3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13957871)))) & (64)) == 0) goto loc_00276FB2;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_stack_mD0, a3, v_stack_mE0);
    if ((unsigned __int8)(result) == 0) goto loc_00276FB2;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(1))), v_stack_mD0, a3, v_stack_mE0);
    goto loc_00276FB4;
loc_00276FDF:
    if ((unsigned int)(result) == 0) goto loc_0027712A;
loc_00276FE7:
    goto loc_002768F3;
loc_00276FF0:
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m110))) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_00276CA1;
    result = ((unsigned int)((unsigned int)(result))) + (1);
    if (v_stack_m128 < result) goto loc_00276CA1;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_m128, (unsigned int)(v_stack_m110), 128, v_stack_m128);
    goto loc_00276CA1;
loc_00277028:
    result = (unsigned int)(((unsigned int)(v_stack_m128)) >> (3));
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (4)) != 0) goto loc_00277184;
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (1)) != 0) goto loc_002770B8;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_m128 + result * 4, (unsigned int)(v_stack_m110), 128, v_stack_m128);
    goto loc_00277222;
loc_0027705A:
    if ((((unsigned __int8)((unsigned int)(v_stack_m120))) & ((unsigned __int8)((unsigned int)(v_stack_m110)))) != 0) goto loc_00277080;
    a3 = (unsigned int)((128) | ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12279340 + 9836 + a4 * 4)))))))));
    v_r10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12279340 + 9836 + a4 * 4))))))))));
    if (condition_is_equal) { v_r10 = a3; }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (1));
    goto loc_002769CF;
loc_00277080:
    result = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_stack_p20 = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 13951510)) & ((unsigned int)(result))) == 0) goto loc_00277193;
loc_0027709C:
loc_0027709E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128))))) >> (1));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_00277080;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (1));
    goto loc_002769CF;
loc_002770B8:
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(1, (unsigned int)(v_stack_m110), a3, v_stack_m128);
    if ((unsigned int)(result) == 0) goto loc_00276DDB;
    goto loc_00277222;
loc_002770CF:
    result = (unsigned __int8)((1) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_00276F25;
    result = ((unsigned int)((unsigned int)(result))) + (1);
    if (1 < result) goto loc_00276F25;
    result = MiCheckLinearProtectedPteAccessedBit(1, 1, 128, v_stack_m128);
    goto loc_00276F25;
loc_0027710C:
    v_r14 = (unsigned int)((1) >> (3));
    v_r14 = (unsigned int)((v_r14) & (511));
    result = ExAcquireSpinLockSharedAtDpcLevel(v_stack_m128 + v_r14 * 4, 1, 128, v_stack_m128);
    goto loc_002768EF;
loc_0027712A:
    if (((2) & (1)) != 0) goto loc_00277150;
    a3 = (unsigned int)((128) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128)))));
    v_r10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128))))));
    if (condition_is_equal) { v_r10 = a3; }
    result = (unsigned int)((1) & ((unsigned int)(v_r14)));
    goto loc_00276D35;
loc_00277150:
    result = (unsigned int)(((unsigned int)(v_stack_p10)) + 1);
    v_stack_p10 = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 13951302)) & ((unsigned int)(result))) == 0) goto loc_002771C0;
loc_00277168:
loc_0027716A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(result))) != 0) goto loc_00277150;
    result = (unsigned int)((1) & ((unsigned int)(v_r14)));
    goto loc_00276D35;
loc_00277184:
    result = ExAcquireSpinLockSharedAtDpcLevel((unsigned int)((unsigned int)(v_r12)), 1, a3, v_stack_m128);
    goto loc_00277222;
loc_00277193:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13957407)))) & (64)) == 0) goto loc_0027709C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r12)), 1, a3, v_stack_m128);
    if ((unsigned __int8)(result) == 0) goto loc_00277218;
    result = HvlNotifyLongSpinWait((unsigned int)(v_stack_p20), 1, a3, v_stack_m128);
    goto loc_0027709E;
loc_002771C0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13957362)))) & (64)) == 0) goto loc_00277168;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(v_stack_p20), 1, a3, v_stack_m108);
    if ((unsigned __int8)(result) == 0) goto loc_00277207;
    result = HvlNotifyLongSpinWait((unsigned int)(v_stack_p10), 1, a3, v_stack_m108);
    goto loc_0027716A;
loc_002771E6:
    goto loc_002764F2;
loc_002771FF:
    goto loc_00276C4E;
loc_00277207:
    goto loc_00277168;
loc_00277211:
    goto loc_0027694D;
loc_00277218:
    goto loc_0027709C;
loc_00277222:
    v_stack_m120 = 1;
    goto loc_00277277;
loc_00277277:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 320) = 0;
    if (1 == 0) goto loc_0027728A;
    if ((unsigned int)((unsigned int)(v_stack_m114)) != 0) goto loc_0027733E;
loc_0027728A:
loc_0027728C:
    v_rsp = (v_rsp) + (288);
    return 1;
loc_002772A0:
    a4 = (*(unsigned __int64 *)(v_rip + 13957945)) << (12);
    a4 = (a4) + ((unsigned int)(v_stack_p10));
    a4 = (a4) + (*(unsigned __int64 *)(v_rip + 13957497));
    a4 = (a4) & (1);
    if (1 < (*(unsigned __int64 *)(v_rip + 13957477))) goto loc_002772DE;
    if (1 < a4) goto loc_0027737B;
loc_002772DE:
    goto loc_002763B4;
loc_002772E8:
    if (1 > 1) goto loc_00276375;
    v_rsi = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(v_rsi + 26, (unsigned int)(0x1380ULL), 1, (unsigned int)(a3));
loc_00277316:
    if (((unsigned int)(0x1380ULL)) < (*(unsigned __int64 *)(v_rip + 12327147))) goto loc_00277331;
    result = (*(unsigned __int64 *)(v_rip + 12327147)) + (*(unsigned __int64 *)(v_rip + 12327148));
    if (((unsigned int)(0x1380ULL)) < result) goto loc_0027737B;
loc_00277331:
    goto loc_002763B4;
loc_0027733E:
    if (1 == 3) {
        a4 = ((unsigned int)(a3)) >> (9);
        a4 = (a4) & (result);
        result = (unsigned int)((unsigned int)(result));
        a4 = (a4) + (result);
    }
    result = MI_READ_PTE_LOCK_FREE(a4, (unsigned int)(0x1380ULL), 1, a4);
    result = (unsigned __int8)((result) & (129));
    if (((unsigned __int8)(result)) != 129) goto loc_0027736E;
    v_rbx = (1 == 3) ? 1 : 0;
    v_rbx = (unsigned int)((v_rbx) + (2));
    goto loc_0027728A;
loc_0027736E:
    result = MiUnlockPageTable(a1, v_stack_p30, 1, a4);
loc_0027737B:
    result = 0;
    goto loc_0027728C;
}
```

## 5. (Beta) C Style

```c
int64_t MiFastLockLeafPageTable(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (288);
    if (Arg2 >= local_r11) goto loc_002772E8;
loc_00276375:
    local_rsi = 0;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(Arg1)) == 7) goto loc_002772DE;
    if (((uint8_t)(Arg1 - 1)) <= 1) goto loc_002772DE;
    if (((uint8_t)(Arg1)) == 5) goto loc_00277316;
    if (((uint8_t)(Arg1)) == 3) goto loc_002772A0;
    Arg3 = 0;
    if ((uint8_t)(Arg1) == 0) { Arg3 = 1; }
loc_002763B4:
    if (((*(uint64_t *)(v_rip + 0xD506B9)) & (0x800000ULL)) == 0) goto loc_0027737B;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_0027737B;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 320;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x140)) != 0) goto loc_0027737B;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x140) = 1;
    v_stack_m114 = 0;
    v_stack_m120 = 0;
    Arg2 = (Arg2) >> (18);
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFFF8ULL));
    v_stack_mE0 = Arg2 + local_rbx * 1;
    v_stack_m78 = Arg2 + local_rbx * 1;
    v_stack_m128 = Arg2 + local_rbx * 1;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_p18)) | (2));
    v_stack_p18 = (uint32_t)(local_r12);
    if (Arg3 == 0) goto loc_002771E6;
    v_stack_m80 = 0;
    local_r14 = (Arg2 + local_rbx * 1) >> (9);
    local_r14 = (local_r14) & (Arg2);
    local_r14 = (local_r14) + (local_r11);
    v_stack_m80 = local_r14;
    if (local_r14 < local_r10) goto loc_002764CC;
    if (local_r14 > Arg3) goto loc_002764CC;
    v_stack_mB0 = *(uint64_t *)(local_r14);
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_002764C7;
    Arg2 = ((((uint8_t)(*(uint64_t *)(local_r14))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_r14))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_002765E9;
loc_002764BD:
loc_002764C7:
    v_stack_m100 = *(uint64_t *)(local_r14);
loc_002764CC:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_00276D83;
    if (sign_flag) goto loc_00276911;
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (8)) != 0) goto loc_00276854;
loc_002764F2:
loc_002764F7:
    if (v_stack_m128 < local_r10) goto loc_0027653C;
    if (v_stack_m128 > Arg3) goto loc_0027653C;
    v_stack_mA0 = *(uint64_t *)(v_stack_m128);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (1)) == 0) goto loc_00276537;
    Arg2 = ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_002767D0;
loc_0027652D:
loc_00276537:
    v_stack_mF0 = *(uint64_t *)(v_stack_m128);
loc_0027653C:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (1)) == 0) goto loc_00276E85;
    if (sign_flag) goto loc_00276F6E;
    v_stack_p20 = 0;
    if (v_stack_m128 != (*(uint64_t *)(v_stack_m128))) goto loc_0027666B;
    v_stack_mD8 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00276938;
loc_0027659D:
    v_stack_mC0 = Arg1 + 176;
    v_stack_mB8 = *(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 * 2 * 8 + 40000;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 * 2 * 8 + 0x9C48) = Arg1 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 * 2 * 8 + 0x9C40) = 0;
    if (((v_stack_p18) & (1)) == 0) goto loc_00276A27;
    result = KxTryToAcquireQueuedSpinLock(*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 * 2 * 8 + 40000, Arg1 + 176, *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m128);
loc_002765DC:
    if ((uint32_t)(result) == 0) goto loc_00276DDB;
    goto loc_00277222;
loc_002765E9:
    if (((*(uint64_t *)(v_rip + 0xD50494)) & (0x600000ULL)) == 0) goto loc_002764BD;
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002764BD;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002764BD;
    Arg1 = (local_r14) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (result) | (32);
        v_stack_mB0 = result;
    }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) goto loc_002764BD;
    result = (result) | (66);
    v_stack_mB0 = result;
    goto loc_002764BD;
loc_0027666B:
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_00276A18;
    if (v_stack_m128 < local_r10) goto loc_00276A18;
    if (v_stack_m128 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508))) goto loc_002766D3;
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_00277028;
loc_002766D3:
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_00276966;
loc_002766EB:
    v_stack_m118 = 0;
    v_stack_m118 = 0;
    if (v_stack_m128 < local_r10) goto loc_00276731;
    if (v_stack_m128 > (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00276731;
    v_stack_m98 = *(uint64_t *)(v_stack_m128);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (1)) == 0) goto loc_0027672C;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00276A55;
loc_0027672C:
    v_stack_mE8 = *(uint64_t *)(v_stack_m128);
loc_00276731:
loc_00276745:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (1));
loc_00276760:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m128))) & (1)) == 0) goto loc_002767B8;
    result = (*(uint64_t *)(v_stack_m128)) >> (60);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00276C6D;
    Arg1 = (*(uint64_t *)(v_stack_m128)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
    Arg1 = (Arg1) | (v_stack_m128);
    if (((*(uint64_t *)(v_rip + 0xD502EC)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD502EC)) & (0x2000000ULL)) == 0) goto loc_002767C4;
    if (Arg3 == 0) goto loc_00276760;
loc_002767B8:
    goto loc_002765DC;
loc_002767C4:
    goto loc_002765DC;
loc_002767D0:
    if (((*(uint64_t *)(v_rip + 0xD502AD)) & (0x600000ULL)) == 0) goto loc_0027652D;
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0027652D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0027652D;
    Arg1 = (v_stack_m128) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    result = 1;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (1) | (32);
        v_stack_mA0 = result;
    }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) goto loc_0027652D;
    result = (result) | (66);
    v_stack_mA0 = result;
    goto loc_0027652D;
loc_00276854:
    local_rdi = (uint32_t)((1) & (0xFFFFFFF7ULL));
    v_stack_m110 = (uint32_t)(local_rdi);
    v_stack_p10 = 0;
    if (local_r14 != result) goto loc_00276AD6;
    v_stack_m110 = 0;
    v_stack_m110 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00276C38;
loc_002768A7:
    v_stack_mD0 = Arg1 + 176;
    v_stack_mC8 = *(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 * 2 * 8 + 40000;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 * 2 * 8 + 0x9C48) = Arg1 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 * 2 * 8 + 0x9C40) = 0;
    if ((((uint8_t)(local_rdi)) & (1)) == 0) goto loc_00276DA5;
    result = KxTryToAcquireQueuedSpinLock(*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 * 2 * 8 + 40000, Arg1 + 176, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
loc_002768E6:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00276FE7;
loc_002768EF:
    v_stack_m120 = 2;
loc_002768F3:
    goto loc_00277277;
loc_00276911:
    v_stack_m114 = 3;
    Arg1 = (v_stack_m128) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    Arg1 = (Arg1) + (2);
    v_stack_m128 = Arg1;
    goto loc_002764F2;
loc_00276938:
    if (2 == 7) goto loc_00276E7E;
    if (2 == 5) goto loc_00277211;
loc_0027694D:
    Arg2 = (v_rip + 12280298 + 3 * 8) + (0x3280ULL);
    goto loc_0027659D;
loc_00276966:
    if (v_stack_m128 < local_r10) goto loc_002766EB;
    if (v_stack_m128 > Arg2) goto loc_002766EB;
    v_stack_p20 = 0;
    Arg1 = (v_stack_m128) - (local_r10);
    Arg1 = (Arg1) >> (3);
    local_r14 = (uint32_t)((Arg1 + Arg1 * 1) & (31));
    a4 = ((uint32_t)((uint32_t)(Arg1 + Arg1 * 1))) >> (5);
    v_stack_m108 = v_rip + 12280207 + 9836 + a4 * 4;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (1));
loc_002769CF:
    Arg3 = (uint32_t)((3) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
loc_002769D8:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    if (((1) & ((uint8_t)(Arg2))) != 0) goto loc_00276DD3;
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4)))));
    result = (uint32_t)(~((uint32_t)(Arg3)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(result)));
    if (condition_is_equal) goto loc_00277222;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_002769D8;
    goto loc_00276DDB;
loc_00276A18:
    goto loc_002766D3;
loc_00276A27:
    if (((*(uint8_t *)(v_rip + 0xD500D8)) & (33)) != 0) goto loc_00276C10;
loc_00276A34:
    if ((uint32_t)((uint32_t)(local_r14)) == 0) goto loc_00277222;
    result = KxWaitForLockOwnerShip(v_stack_mB8, (uint32_t)((uint32_t)(local_r14)), Arg3, v_rip + 12280207 + 9836 + a4 * 4);
    goto loc_00277222;
loc_00276A55:
    if (((*(uint64_t *)(v_rip + 0xD50028)) & (0x600000ULL)) == 0) goto loc_0027672C;
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0027672C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0027672C;
    result = (v_stack_m128) >> (3);
    result = (uint32_t)((result) & (511));
    local_rbx = 3;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (3) | (32);
        v_stack_m98 = local_rbx;
    }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) goto loc_0027672C;
    local_rbx = (local_rbx) | (66);
    v_stack_m98 = local_rbx;
    goto loc_0027672C;
loc_00276AD6:
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_00276D96;
    if (local_r14 < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4)))))))) goto loc_00276D96;
    if (local_r14 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508))) goto loc_00276B39;
    v_stack_m60 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_0027710C;
loc_00276B39:
    v_stack_m8C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_00276CCE;
loc_00276B4F:
    v_stack_m11C = 0;
    v_stack_m11C = 0;
    if (local_r14 < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4)))))))) goto loc_00276B90;
    if (local_r14 > Arg3) goto loc_00276B90;
    v_stack_mA8 = *(uint64_t *)(local_r14);
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_00276B8B;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_r14))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_r14))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00276DFF;
loc_00276B8B:
    v_stack_mF8 = *(uint64_t *)(local_r14);
loc_00276B90:
    Arg2 = (uint32_t)((1) & (1));
loc_00276BB3:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_00276BFB;
    result = (*(uint64_t *)(local_r14)) >> (60);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00276EF2;
    Arg1 = (*(uint64_t *)(local_r14)) & (Arg3);
    Arg1 = (Arg1) | (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568));
    if (((*(uint64_t *)(v_rip + 0xD4FEA3)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD4FEA3)) & (0x2000000ULL)) == 0) goto loc_00276C00;
    if ((uint32_t)(Arg2) == 0) goto loc_00276BB3;
loc_00276BFB:
    goto loc_00276C06;
loc_00276C00:
loc_00276C06:
    goto loc_002768E6;
loc_00276C10:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC97242))) != 0) goto loc_00276A34;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mB8, v_stack_mC0, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568));
    goto loc_00277222;
loc_00276C38:
    if (((uint8_t)(result)) == 7) goto loc_00276F92;
    if (((uint8_t)(result)) == 5) goto loc_002771FF;
loc_00276C4E:
    Arg2 = (v_rip + 12279528 + 3 * 8) + (0x3280ULL);
    goto loc_002768A7;
loc_00276C6D:
    if (Arg3 != 0) goto loc_002767B8;
    if (((3) & (2)) != 0) goto loc_00276EA0;
    local_rdi = (2) | ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4)))))));
    if (((*(uint64_t *)(v_rip + 0xD4FDF9)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD4FDED)) & (v_stack_mB8)) != 0) goto loc_00276FF0;
loc_00276CA1:
    local_rbx = 2;
    if (((*(uint64_t *)(v_rip + 0xD4FDED)) & (v_stack_mB8)) == 0) { local_rbx = local_rdi; }
loc_00276CBF:
    goto loc_00276745;
loc_00276CCE:
    if (3 < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4)))))))) goto loc_00276B4F;
    if (3 > Arg2) goto loc_00276B4F;
    v_stack_p10 = 0;
    local_r14 = (3) - ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB618F + 0x266C + a4 * 4)))))));
    local_r14 = (local_r14) >> (3);
    local_r12 = (uint32_t)((local_r14 + local_r14 * 1) & (31));
    a4 = ((uint32_t)((uint32_t)(local_r14 + local_r14 * 1))) >> (5);
    v_stack_m108 = v_rip + 12279340 + 9836 + a4 * 4;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (1));
loc_00276D35:
    Arg3 = (uint32_t)((2) << ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
loc_00276D3E:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB5E2C + 0x266C + a4 * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
    if ((((uint8_t)(2 - 1)) & ((uint8_t)(Arg2))) != 0) goto loc_00276FDF;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(2 - 1))) << ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB5E2C + 0x266C + a4 * 4)))));
    result = (uint32_t)(~((uint32_t)(Arg3)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(result)));
    if (condition_is_equal) goto loc_002768EF;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00276D3E;
    goto loc_002768F3;
loc_00276D83:
    goto loc_00277277;
loc_00276D96:
    goto loc_00276B39;
loc_00276DA5:
    if (((*(uint8_t *)(v_rip + 0xD4FD5A)) & (33)) != 0) goto loc_00276ECA;
loc_00276DB2:
    if ((uint32_t)((uint32_t)(local_r12)) == 0) goto loc_002768EF;
    result = KxWaitForLockOwnerShip(v_stack_mC8, (uint32_t)((uint32_t)(local_r12)), Arg3, v_rip + 12279340 + 9836 + a4 * 4);
    goto loc_002768EF;
loc_00276DD3:
    if ((uint32_t)(result) == 0) goto loc_0027705A;
loc_00276DDB:
    v_stack_m120 = 0;
    goto loc_00277277;
loc_00276DFF:
    if (((*(uint64_t *)(v_rip + 0xD4FC7E)) & (0x600000ULL)) == 0) goto loc_00276B8B;
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00276B8B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00276B8B;
    result = (2 - 1) >> (3);
    result = (uint32_t)((result) & (511));
    local_rbx = 0;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (0) | (32);
        v_stack_mA8 = local_rbx;
    }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) goto loc_00276B8B;
    local_rbx = (local_rbx) | (66);
    v_stack_mA8 = local_rbx;
    goto loc_00276B8B;
loc_00276E7E:
    goto loc_0027694D;
loc_00276E85:
    v_stack_m120 = 0;
    goto loc_00277277;
loc_00276EA0:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m118)) + 1);
    v_stack_m118 = (uint32_t)(local_rbx);
    if (((*(uint32_t *)(v_rip + 0xD4E3FC)) & ((uint32_t)(local_rbx))) == 0) goto loc_00276F47;
loc_00276EB6:
loc_00276EB8:
    if (((local_rdi) & (*(uint64_t *)(v_stack_m128))) != 0) goto loc_00276EA0;
    goto loc_00276CBF;
loc_00276ECA:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC96F88))) != 0) goto loc_00276DB2;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mC8, v_stack_mD0, Arg3, v_stack_mE0);
    goto loc_002768EF;
loc_00276EF2:
    if ((uint32_t)(v_stack_mD0) != 0) goto loc_00276BFB;
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00276FA0;
    local_rdi = (*(uint64_t *)(v_stack_m128)) | ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB5E2C + 0x266C + a4 * 4)))))));
    if (((*(uint64_t *)(v_rip + 0xD4FB75)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD4FB69)) & (v_stack_mC8)) != 0) goto loc_002770CF;
loc_00276F25:
    local_rbx = *(uint64_t *)(v_stack_m128);
    if (((*(uint64_t *)(v_rip + 0xD4FB69)) & (v_stack_mC8)) == 0) { local_rbx = local_rdi; }
loc_00276F38:
    goto loc_00276B90;
loc_00276F47:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4FB6B)))) & (64)) == 0) goto loc_00276EB6;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_mC8, v_stack_mD0, Arg3, v_stack_mE0);
    if ((uint8_t)(result) == 0) goto loc_00276EB6;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_mD0, Arg3, v_stack_mE0);
    goto loc_00276EB8;
loc_00276F6E:
    v_stack_m120 = (uint32_t)(local_rbx);
    v_stack_m114 = (uint32_t)(local_rbx);
    Arg1 = (v_stack_m128) >> (9);
    Arg1 = (Arg1) & (v_stack_mD0);
    Arg1 = (Arg1) + ((uint32_t)((uint32_t)(result)));
    v_stack_m128 = Arg1;
    goto loc_002764F7;
loc_00276F92:
    goto loc_00276C4E;
loc_00276FA0:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m11C)) + 1);
    v_stack_m11C = (uint32_t)(local_rbx);
    if (((*(uint32_t *)(v_rip + 0xD4E2FC)) & ((uint32_t)(local_rbx))) == 0) goto loc_00276FC3;
loc_00276FB2:
loc_00276FB4:
    if (condition_is_below) goto loc_00276FA0;
    goto loc_00276F38;
loc_00276FC3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4FAEF)))) & (64)) == 0) goto loc_00276FB2;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, v_stack_mD0, Arg3, v_stack_mE0);
    if ((uint8_t)(result) == 0) goto loc_00276FB2;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(1))), v_stack_mD0, Arg3, v_stack_mE0);
    goto loc_00276FB4;
loc_00276FDF:
    if ((uint32_t)(result) == 0) goto loc_0027712A;
loc_00276FE7:
    goto loc_002768F3;
loc_00276FF0:
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m110))) & (33));
    if (((uint8_t)(result)) != 1) goto loc_00276CA1;
    result = ((uint32_t)((uint32_t)(result))) + (1);
    if (v_stack_m128 < result) goto loc_00276CA1;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_m128, (uint32_t)(v_stack_m110), 128, v_stack_m128);
    goto loc_00276CA1;
loc_00277028:
    result = (uint32_t)(((uint32_t)(v_stack_m128)) >> (3));
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (4)) != 0) goto loc_00277184;
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (1)) != 0) goto loc_002770B8;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_m128 + result * 4, (uint32_t)(v_stack_m110), 128, v_stack_m128);
    goto loc_00277222;
loc_0027705A:
    if ((((uint8_t)((uint32_t)(v_stack_m120))) & ((uint8_t)((uint32_t)(v_stack_m110)))) != 0) goto loc_00277080;
    Arg3 = (uint32_t)((128) | ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB5E2C + 0x266C + a4 * 4)))))))));
    local_r10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB5E2C + 0x266C + a4 * 4))))))))));
    if (condition_is_equal) { local_r10 = Arg3; }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (1));
    goto loc_002769CF;
loc_00277080:
    result = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    v_stack_p20 = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xD4E216)) & ((uint32_t)(result))) == 0) goto loc_00277193;
loc_0027709C:
loc_0027709E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128))))) >> (1));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_00277080;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (1));
    goto loc_002769CF;
loc_002770B8:
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(1, (uint32_t)(v_stack_m110), Arg3, v_stack_m128);
    if ((uint32_t)(result) == 0) goto loc_00276DDB;
    goto loc_00277222;
loc_002770CF:
    result = (uint8_t)((1) & (33));
    if (((uint8_t)(result)) != 1) goto loc_00276F25;
    result = ((uint32_t)((uint32_t)(result))) + (1);
    if (1 < result) goto loc_00276F25;
    result = MiCheckLinearProtectedPteAccessedBit(1, 1, 128, v_stack_m128);
    goto loc_00276F25;
loc_0027710C:
    local_r14 = (uint32_t)((1) >> (3));
    local_r14 = (uint32_t)((local_r14) & (511));
    result = ExAcquireSpinLockSharedAtDpcLevel(v_stack_m128 + local_r14 * 4, 1, 128, v_stack_m128);
    goto loc_002768EF;
loc_0027712A:
    if (((2) & (1)) != 0) goto loc_00277150;
    Arg3 = (uint32_t)((128) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128)))));
    local_r10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128))))));
    if (condition_is_equal) { local_r10 = Arg3; }
    result = (uint32_t)((1) & ((uint32_t)(local_r14)));
    goto loc_00276D35;
loc_00277150:
    result = (uint32_t)(((uint32_t)(v_stack_p10)) + 1);
    v_stack_p10 = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xD4E146)) & ((uint32_t)(result))) == 0) goto loc_002771C0;
loc_00277168:
loc_0027716A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
    if ((((uint8_t)(local_r14)) & ((uint8_t)(result))) != 0) goto loc_00277150;
    result = (uint32_t)((1) & ((uint32_t)(local_r14)));
    goto loc_00276D35;
loc_00277184:
    result = ExAcquireSpinLockSharedAtDpcLevel((uint32_t)((uint32_t)(local_r12)), 1, Arg3, v_stack_m128);
    goto loc_00277222;
loc_00277193:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4F91F)))) & (64)) == 0) goto loc_0027709C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r12)), 1, Arg3, v_stack_m128);
    if ((uint8_t)(result) == 0) goto loc_00277218;
    result = HvlNotifyLongSpinWait((uint32_t)(v_stack_p20), 1, Arg3, v_stack_m128);
    goto loc_0027709E;
loc_002771C0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4F8F2)))) & (64)) == 0) goto loc_00277168;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(v_stack_p20), 1, Arg3, v_stack_m108);
    if ((uint8_t)(result) == 0) goto loc_00277207;
    result = HvlNotifyLongSpinWait((uint32_t)(v_stack_p10), 1, Arg3, v_stack_m108);
    goto loc_0027716A;
loc_002771E6:
    goto loc_002764F2;
loc_002771FF:
    goto loc_00276C4E;
loc_00277207:
    goto loc_00277168;
loc_00277211:
    goto loc_0027694D;
loc_00277218:
    goto loc_0027709C;
loc_00277222:
    v_stack_m120 = 1;
    goto loc_00277277;
loc_00277277:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x140) = 0;
    if (1 == 0) goto loc_0027728A;
    if ((uint32_t)((uint32_t)(v_stack_m114)) != 0) goto loc_0027733E;
loc_0027728A:
loc_0027728C:
    local_rsp = (local_rsp) + (288);
    return 1;
loc_002772A0:
    a4 = (*(uint64_t *)(v_rip + 0xD4FB39)) << (12);
    a4 = (a4) + ((uint32_t)(v_stack_p10));
    a4 = (a4) + (*(uint64_t *)(v_rip + 0xD4F979));
    a4 = (a4) & (1);
    if (1 < (*(uint64_t *)(v_rip + 0xD4F965))) goto loc_002772DE;
    if (1 < a4) goto loc_0027737B;
loc_002772DE:
    goto loc_002763B4;
loc_002772E8:
    if (1 > 1) goto loc_00276375;
    local_rsi = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(local_rsi + 26, (uint32_t)(0x1380ULL), 1, (uint32_t)(Arg3));
loc_00277316:
    if (((uint32_t)(0x1380ULL)) < (*(uint64_t *)(v_rip + 0xBC18EB))) goto loc_00277331;
    result = (*(uint64_t *)(v_rip + 0xBC18EB)) + (*(uint64_t *)(v_rip + 0xBC18EC));
    if (((uint32_t)(0x1380ULL)) < result) goto loc_0027737B;
loc_00277331:
    goto loc_002763B4;
loc_0027733E:
    if (1 == 3) {
        a4 = ((uint32_t)(Arg3)) >> (9);
        a4 = (a4) & (result);
        result = (uint32_t)((uint32_t)(result));
        a4 = (a4) + (result);
    }
    result = MI_READ_PTE_LOCK_FREE(a4, (uint32_t)(0x1380ULL), 1, a4);
    result = (uint8_t)((result) & (129));
    if (((uint8_t)(result)) != 129) goto loc_0027736E;
    local_rbx = (1 == 3) ? 1 : 0;
    local_rbx = (uint32_t)((local_rbx) + (2));
    goto loc_0027728A;
loc_0027736E:
    result = MiUnlockPageTable(Arg1, v_stack_p30, 1, a4);
loc_0027737B:
    result = 0;
    goto loc_0027728C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00276340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
