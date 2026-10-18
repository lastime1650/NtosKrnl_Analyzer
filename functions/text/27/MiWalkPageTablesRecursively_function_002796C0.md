# MiWalkPageTablesRecursively

- RVA: `0x002796C0`–`0x0027B7F8` (길이 `8,504` bytes)
- VA: `0x00000001402796C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065FF4`
- 디코드: `1,977`개 명령, `8,504/8,504` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **63**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x002798F6` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027992B` → [MiReleaseWalkLocks](../23/MiReleaseWalkLocks_function_00239FD0.md) (function, `0x00239FD0`)
- `0x00279A32` → [MiComputePxeWalkAction](MiComputePxeWalkAction_function_0027B800.md) (function, `0x0027B800`)
- `0x00279B6D` → [MiGetLeafVa](MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x00279B7D` → [MiLockVadTree](MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x00279B85` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00279BB4` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x00279D98` → [MiWalkGetResumptionPxe](../46/MiWalkGetResumptionPxe_function_00466360.md) (function, `0x00466360`)
- `0x00279DC2` → [MiGetNextPageTablePte](MiGetNextPageTablePte_function_0027BB30.md) (function, `0x0027BB30`)
- `0x00279E34` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027A1D6` → [MiWalkGetResumptionPxe](../46/MiWalkGetResumptionPxe_function_00466360.md) (function, `0x00466360`)
- `0x0027A299` → [MiReacquireWalkLocks](../28/MiReacquireWalkLocks_function_002819A0.md) (function, `0x002819A0`)
- `0x0027A414` → [MiQueryLeafPte](../3D/MiQueryLeafPte_function_003D2160.md) (function, `0x003D2160`)
- `0x0027A449` → [MiYieldPageTableWalk](../23/MiYieldPageTableWalk_function_00239D20.md) (function, `0x00239D20`)
- `0x0027A454` → [MiWaitForFreePage](../2A/MiWaitForFreePage_function_002A3324.md) (function, `0x002A3324`)
- `0x0027A59C` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027A64C` → [EtwTraceShouldYieldProcessor](EtwTraceShouldYieldProcessor_function_00279088.md) (function, `0x00279088`)
- `0x0027A716` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027A739` → [MiReacquireWalkLocks](../28/MiReacquireWalkLocks_function_002819A0.md) (function, `0x002819A0`)
- `0x0027A748` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0027A7EC` → [MiAgePte](../28/MiAgePte_function_0028F750.md) (function, `0x0028F750`)
- `0x0027A891` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027A943` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027A9C7` → [MiLockWorkingSetExclusiveAtDpc](../23/MiLockWorkingSetExclusiveAtDpc_function_002395EC.md) (function, `0x002395EC`)
- `0x0027AA04` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027AAB7` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0027ACB1` → [MiWalkPageTablesRecursively](MiWalkPageTablesRecursively_function_002796C0.md) (function, `0x002796C0`)
- `0x0027AF7F` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0027AF9F` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0027B023` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0027B071` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0027B087` → [MiLockWorkingSetShared](MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0027B108` → [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) (function, `0x00372190`)
- `0x0027B14B` → [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x0027B166` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)
- `0x0027B173` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0027B1E3` → [MiPeriodicGoodCitizen](MiPeriodicGoodCitizen_function_00279250.md) (function, `0x00279250`)
- `0x0027B1F3` → [MiGetNextVad](../29/MiGetNextVad_function_00297224.md) (function, `0x00297224`)
- `0x0027B25E` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0027B29A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0027B367` → [ExReleaseSpinLockRegardlessFromDpcLevel](../23/ExReleaseSpinLockRegardlessFromDpcLevel_function_0023A330.md) (function, `0x0023A330`)
- `0x0027B397` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0027B4BC` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0027B4CB` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0027B4F3` → [MiReacquireHigherPageTableLock](../23/MiReacquireHigherPageTableLock_function_00239650.md) (function, `0x00239650`)
- `0x0027B533` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0027B5B0` → [MiDeleteVaTail](../47/MiDeleteVaTail_function_00473EF0.md) (function, `0x00473EF0`)
- `0x0027B5CF` → [MiDeleteVaTail](../47/MiDeleteVaTail_function_00473EF0.md) (function, `0x00473EF0`)
- `0x0027B5FE` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0027B632` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0027B673` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0027B690` → [MiDeleteVaTail](../47/MiDeleteVaTail_function_00473EF0.md) (function, `0x00473EF0`)
- `0x0027B6AC` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0027B6F6` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x0027B713` → [MiDeleteVaTail](../47/MiDeleteVaTail_function_00473EF0.md) (function, `0x00473EF0`)
- `0x0027B757` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x0027B764` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0027B76E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0027B77A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0027B78E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0027B79A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0027B7A1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0027B7C1` → [MiMarkResumptionPoint](../43/MiMarkResumptionPoint_function_004365F0.md) (function, `0x004365F0`)

### Direct callers
- [MiWalkPageTablesRecursively](MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027ACB1`
- [MiWalkPageTables](../2C/MiWalkPageTables_function_002C2710.md) at `0x002C29BE`

### Static image references
- `0x00279822` → RVA `0x00E38840` (`.data`; read)
- `0x002798B9` → RVA `0x00428D10` (`MiAgeWorkingSetTail`; read)
- `0x002798E0` → RVA `0x0048DE00` (`MiAgeWorkingSetVpabCallback`; read)
- `0x0027A067` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0027A12C` → RVA `0x00E2DCCC` (`.data`; read)
- `0x0027A136` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0027A3FB` → RVA `0x003D2160` (`MiQueryLeafPte`; read)
- `0x0027A4E2` → RVA `0x00E2CB40` (`.data`; read)
- `0x0027A56C` → RVA `0x00428C00` (`MiUpdateOldWorkingSetPagesTail`; read)
- `0x0027A586` → RVA `0x0049CF50` (`MiUpdateOldPagesVpabCallback`; read)
- `0x0027A639` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0027A7D9` → RVA `0x0028F750` (`MiAgePte`; read)
- `0x0027AA98` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0027B00A` → RVA `0x00F0DE58` (`.data`; read)
- `0x0027B0F5` → RVA `0x00372190` (`MiOutSwapWorkingSetPte`; read)
- `0x0027B272` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0027B2AD` → RVA `0x004ACD40` (`MiSimpleAgePte`; read)
- `0x0027B4AE` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0027B5A0` → RVA `0x00473EF0` (`MiDeleteVaTail`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002796C0  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
002796C5  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002796CA  53                              push rbx
002796CB  55                              push rbp
002796CC  56                              push rsi
002796CD  57                              push rdi
002796CE  41 54                           push r12
002796D0  41 55                           push r13
002796D2  41 56                           push r14
002796D4  41 57                           push r15
002796D6  48 81 EC 88 00 00 00            sub rsp, 0x88
002796DD  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
002796E1  48 8D 79 60                     lea rdi, [rcx + 0x60]
002796E5  49 63 E8                        movsxd rbp, r8d
002796E8  45 33 FF                        xor r15d, r15d
002796EB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002796F0  48 8D 3C EF                     lea rdi, [rdi + rbp*8]
002796F4  48 8B 81 A8 00 00 00            mov rax, qword ptr [rcx + 0xa8]
002796FB  4C 8B EA                        mov r13, rdx
002796FE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00279703  4C 8B F1                        mov r14, rcx
00279706  48 8B 07                        mov rax, qword ptr [rdi]
00279709  41 8D 5F 01                     lea ebx, [r15 + 1]
0027970D  48 3B D0                        cmp rdx, rax
00279710  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
00279715  4C 8B D5                        mov r10, rbp
00279718  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0027971D  4C 0F 42 E8                     cmovb r13, rax
00279721  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0027972B  48 8D 81 80 00 00 00            lea rax, [rcx + 0x80]
00279732  4D 8B DD                        mov r11, r13
00279735  49 81 E3 00 F0 FF FF            and r11, 0xfffffffffffff000
0027973C  48 8D 04 E8                     lea rax, [rax + rbp*8]
00279740  49 81 C3 F8 0F 00 00            add r11, 0xff8
00279747  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0027974C  48 8B 00                        mov rax, qword ptr [rax]
0027974F  45 8D 47 02                     lea r8d, [r15 + 2]
00279753  4C 3B D8                        cmp r11, rax
00279756  41 8B CF                        mov ecx, r15d
00279759  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00279760  4C 0F 47 D8                     cmova r11, rax
00279764  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00279769  44 89 BC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r15d
00279771  41 8B F7                        mov esi, r15d
00279774  49 BC 00 D0 BE 7D FB F6 FF FF   movabs r12, 0xfffff6fb7dbed000
0027977E  48 BA 68 DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedf68
00279788  4D 3B EB                        cmp r13, r11
0027978B  0F 87 90 10 00 00               ja 0x14027a821
00279791  85 C9                           test ecx, ecx
00279793  0F 85 AF 0A 00 00               jne 0x14027a248
00279799  49 8B 46 48                     mov rax, qword ptr [r14 + 0x48]
0027979D  85 ED                           test ebp, ebp
0027979F  45 8B E7                        mov r12d, r15d
002797A2  41 0F 95 C4                     setne r12b
002797A6  41 83 C4 02                     add r12d, 2
002797AA  48 85 C0                        test rax, rax
002797AD  0F 85 C0 01 00 00               jne 0x140279973
002797B3  49 8B 4E 50                     mov rcx, qword ptr [r14 + 0x50]
002797B7  48 85 C9                        test rcx, rcx
002797BA  0F 85 21 0B 00 00               jne 0x14027a2e1
002797C0  49 FF 86 A0 00 00 00            inc qword ptr [r14 + 0xa0]
002797C7  4D 8B 86 A0 00 00 00            mov r8, qword ptr [r14 + 0xa0]
002797CE  41 8B 16                        mov edx, dword ptr [r14]
002797D1  41 F6 C0 0F                     test r8b, 0xf
002797D5  0F 94 C1                        sete cl
002797D8  F6 C2 08                        test dl, 8
002797DB  0F 95 C0                        setne al
002797DE  84 C8                           test al, cl
002797E0  0F 85 27 09 00 00               jne 0x14027a10d
002797E6  F6 C2 02                        test dl, 2
002797E9  0F 84 2C 02 00 00               je 0x140279a1b
002797EF  45 84 46 08                     test byte ptr [r14 + 8], r8b
002797F3  0F 85 22 02 00 00               jne 0x140279a1b
002797F9  4D 8B 4E 20                     mov r9, qword ptr [r14 + 0x20]
002797FD  83 E2 04                        and edx, 4
00279800  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00279807  24 0F                           and al, 0xf
00279809  3C 05                           cmp al, 5
0027980B  0F 87 91 06 00 00               ja 0x140279ea2
00279811  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00279818  24 0F                           and al, 0xf
0027981A  3C 01                           cmp al, 1
0027981C  0F 85 F6 1C 00 00               jne 0x14027b518
00279822  4C 8D 05 17 F0 BB 00            lea r8, [rip + 0xbbf017]
00279829  4D 8B 00                        mov r8, qword ptr [r8]
0027982C  85 D2                           test edx, edx
0027982E  0F 84 4E 06 00 00               je 0x140279e82
00279834  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0027983D  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00279844  48 85 C9                        test rcx, rcx
00279847  0F 84 7F 05 00 00               je 0x140279dcc
0027984D  8B 81 44 01 00 00               mov eax, dword ptr [rcx + 0x144]
00279853  48 C1 E0 06                     shl rax, 6
00279857  41 8B 04 00                     mov eax, dword ptr [r8 + rax]
0027985B  0F BA E0 1E                     bt eax, 0x1e
0027985F  0F 83 3D 06 00 00               jae 0x140279ea2
00279865  48 BF 68 DF BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbedf68
0027986F  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
00279873  49 8D 4E 04                     lea rcx, [r14 + 4]
00279877  8B C2                           mov eax, edx
00279879  F6 C2 1C                        test dl, 0x1c
0027987C  75 24                           jne 0x1402798a2
0027987E  85 ED                           test ebp, ebp
00279880  74 20                           je 0x1402798a2
00279882  49 8D 4E 04                     lea rcx, [r14 + 4]
00279886  41 83 FC 03                     cmp r12d, 3
0027988A  74 16                           je 0x1402798a2
0027988C  40 0F B6 C5                     movzx eax, bpl
00279890  49 8D 4E 04                     lea rcx, [r14 + 4]
00279894  C1 E0 02                        shl eax, 2
00279897  33 C2                           xor eax, edx
00279899  4D 89 6E 48                     mov qword ptr [r14 + 0x48], r13
0027989D  83 E0 1C                        and eax, 0x1c
002798A0  33 C2                           xor eax, edx
002798A2  49 8B 96 B0 00 00 00            mov rdx, qword ptr [r14 + 0xb0]
002798A9  83 C8 20                        or eax, 0x20
002798AC  41 89 46 04                     mov dword ptr [r14 + 4], eax
002798B0  48 85 D2                        test rdx, rdx
002798B3  0F 84 04 0C 00 00               je 0x14027a4bd
002798B9  48 8D 05 50 F4 1A 00            lea rax, [rip + 0x1af450]
002798C0  48 3B D0                        cmp rdx, rax
002798C3  0F 85 A3 0C 00 00               jne 0x14027a56c
002798C9  49 8B 9E B8 00 00 00            mov rbx, qword ptr [r14 + 0xb8]
002798D0  8B 03                           mov eax, dword ptr [rbx]
002798D2  A8 03                           test al, 3
002798D4  0F 84 D3 19 00 00               je 0x14027b2ad
002798DA  41 B9 01 00 00 00               mov r9d, 1
002798E0  48 8D 05 19 45 21 00            lea rax, [rip + 0x214519]
002798E7  45 33 C0                        xor r8d, r8d
002798EA  48 8D 53 38                     lea rdx, [rbx + 0x38]
002798EE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002798F3  49 8B CE                        mov rcx, r14
002798F6  E8 95 05 FC FF                  call 0x140239e90
002798FB  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
002798FF  A8 20                           test al, 0x20
00279901  74 04                           je 0x140279907
00279903  C6 43 06 01                     mov byte ptr [rbx + 6], 1
00279907  41 8B DF                        mov ebx, r15d
0027990A  49 8D 4E 04                     lea rcx, [r14 + 4]
0027990E  83 21 DF                        and dword ptr [rcx], 0xffffffdf
00279911  8B 01                           mov eax, dword ptr [rcx]
00279913  A8 01                           test al, 1
00279915  75 19                           jne 0x140279930
00279917  83 FB 04                        cmp ebx, 4
0027991A  7D 19                           jge 0x140279935
0027991C  41 8B 16                        mov edx, dword ptr [r14]
0027991F  F6 C2 02                        test dl, 2
00279922  0F 84 E7 18 00 00               je 0x14027b20f
00279928  49 8B CE                        mov rcx, r14
0027992B  E8 A0 06 FC FF                  call 0x140239fd0
00279930  83 FB 04                        cmp ebx, 4
00279933  7C 07                           jl 0x14027993c
00279935  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
0027993C  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
00279943  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00279948  4C 63 D5                        movsxd r10, ebp
0027994B  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
00279950  BB 01 00 00 00                  mov ebx, 1
00279955  8B CB                           mov ecx, ebx
00279957  89 9C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebx
0027995E  41 B8 02 00 00 00               mov r8d, 2
00279964  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0027996E  E9 01 FE FF FF                  jmp 0x140279774
00279973  49 8B D5                        mov rdx, r13
00279976  49 8B C9                        mov rcx, r9
00279979  4C 3B E9                        cmp r13, rcx
0027997C  72 34                           jb 0x1402799b2
0027997E  48 BF FF FF FF FF FF F6 FF FF   movabs rdi, 0xfffff6ffffffffff
00279988  48 8B CF                        mov rcx, rdi
0027998B  48 3B D1                        cmp rdx, rcx
0027998E  77 1A                           ja 0x1402799aa
00279990  48 C1 E2 19                     shl rdx, 0x19
00279994  49 8B C9                        mov rcx, r9
00279997  48 C1 E1 19                     shl rcx, 0x19
0027999B  48 2B D1                        sub rdx, rcx
0027999E  48 C1 FA 10                     sar rdx, 0x10
002799A2  49 8B C9                        mov rcx, r9
002799A5  48 3B D1                        cmp rdx, rcx
002799A8  73 DE                           jae 0x140279988
002799AA  49 8D 7A 0C                     lea rdi, [r10 + 0xc]
002799AE  49 8D 3C FE                     lea rdi, [r14 + rdi*8]
002799B2  49 8B C9                        mov rcx, r9
002799B5  48 3B C1                        cmp rax, rcx
002799B8  72 34                           jb 0x1402799ee
002799BA  48 BF FF FF FF FF FF F6 FF FF   movabs rdi, 0xfffff6ffffffffff
002799C4  48 8B CF                        mov rcx, rdi
002799C7  48 3B C1                        cmp rax, rcx
002799CA  77 1A                           ja 0x1402799e6
002799CC  48 C1 E0 19                     shl rax, 0x19
002799D0  49 8B C9                        mov rcx, r9
002799D3  48 C1 E1 19                     shl rcx, 0x19
002799D7  48 2B C1                        sub rax, rcx
002799DA  48 C1 F8 10                     sar rax, 0x10
002799DE  49 8B C9                        mov rcx, r9
002799E1  48 3B C1                        cmp rax, rcx
002799E4  73 DE                           jae 0x1402799c4
002799E6  49 8D 7A 0C                     lea rdi, [r10 + 0xc]
002799EA  49 8D 3C FE                     lea rdi, [r14 + rdi*8]
002799EE  48 3B D0                        cmp rdx, rax
002799F1  0F 87 43 08 00 00               ja 0x14027a23a
002799F7  49 8B 4E 48                     mov rcx, qword ptr [r14 + 0x48]
002799FB  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
002799FF  49 3B CD                        cmp rcx, r13
00279A02  0F 85 8E 07 00 00               jne 0x14027a196
00279A08  83 E2 E3                        and edx, 0xffffffe3
00279A0B  4D 89 7E 48                     mov qword ptr [r14 + 0x48], r15
00279A0F  41 89 56 04                     mov dword ptr [r14 + 4], edx
00279A13  45 8B E0                        mov r12d, r8d
00279A16  E9 98 FD FF FF                  jmp 0x1402797b3
00279A1B  41 8B 06                        mov eax, dword ptr [r14]
00279A1E  45 8B CC                        mov r9d, r12d
00279A21  44 8B C5                        mov r8d, ebp
00279A24  49 8B D5                        mov rdx, r13
00279A27  49 8B CE                        mov rcx, r14
00279A2A  A8 20                           test al, 0x20
00279A2C  0F 85 90 03 00 00               jne 0x140279dc2
00279A32  E8 C9 1D 00 00                  call 0x14027b800
00279A37  44 8B D0                        mov r10d, eax
00279A3A  83 F8 04                        cmp eax, 4
00279A3D  0F 84 80 08 00 00               je 0x14027a2c3
00279A43  85 C0                           test eax, eax
00279A45  0F 84 6C 09 00 00               je 0x14027a3b7
00279A4B  45 8B 4E 04                     mov r9d, dword ptr [r14 + 4]
00279A4F  41 F6 C1 01                     test r9b, 1
00279A53  0F 85 AF 1B 00 00               jne 0x14027b608
00279A59  41 8B D9                        mov ebx, r9d
00279A5C  83 FD 01                        cmp ebp, 1
00279A5F  0F 8D 0F 03 00 00               jge 0x140279d74
00279A65  41 83 FA 01                     cmp r10d, 1
00279A69  0F 84 5D 02 00 00               je 0x140279ccc
00279A6F  41 83 FA 02                     cmp r10d, 2
00279A73  0F 85 5B 03 00 00               jne 0x140279dd4
00279A79  85 ED                           test ebp, ebp
00279A7B  0F 85 61 09 00 00               jne 0x14027a3e2
00279A81  41 8B 06                        mov eax, dword ptr [r14]
00279A84  A8 01                           test al, 1
00279A86  0F 85 56 09 00 00               jne 0x14027a3e2
00279A8C  49 8B 45 00                     mov rax, qword ptr [r13]
00279A90  A8 01                           test al, 1
00279A92  0F 84 4A 09 00 00               je 0x14027a3e2
00279A98  4D 8B C5                        mov r8, r13
00279A9B  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
00279AA5  49 C1 E0 19                     shl r8, 0x19
00279AA9  49 8B C4                        mov rax, r12
00279AAC  48 C1 E0 19                     shl rax, 0x19
00279AB0  4C 2B C0                        sub r8, rax
00279AB3  48 B8 00 F0 FF FF FF FF 00 00   movabs rax, 0xfffffffff000
00279ABD  49 C1 F8 10                     sar r8, 0x10
00279AC1  4C 23 C0                        and r8, rax
00279AC4  49 C1 E8 09                     shr r8, 9
00279AC8  49 8B C4                        mov rax, r12
00279ACB  4C 03 C0                        add r8, rax
00279ACE  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
00279AD8  49 8B 00                        mov rax, qword ptr [r8]
00279ADB  48 8B C9                        mov rcx, rcx
00279ADE  4C 3B C1                        cmp r8, rcx
00279AE1  72 28                           jb 0x140279b0b
00279AE3  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00279AED  48 8B C9                        mov rcx, rcx
00279AF0  4C 3B C1                        cmp r8, rcx
00279AF3  77 16                           ja 0x140279b0b
00279AF5  A8 01                           test al, 1
00279AF7  74 12                           je 0x140279b0b
00279AF9  A8 42                           test al, 0x42
00279AFB  0F 95 C2                        setne dl
00279AFE  A8 20                           test al, 0x20
00279B00  0F 95 C1                        setne cl
00279B03  84 D1                           test cl, dl
00279B05  0F 84 F8 09 00 00               je 0x14027a503
00279B0B  48 C1 E8 38                     shr rax, 0x38
00279B0F  24 0F                           and al, 0xf
00279B11  3C 0A                           cmp al, 0xa
00279B13  0F 85 B9 08 00 00               jne 0x14027a3d2
00279B19  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00279B1D  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00279B23  A8 0F                           test al, 0xf
00279B25  0F 85 54 09 00 00               jne 0x14027a47f
00279B2B  49 8B DD                        mov rbx, r13
00279B2E  49 8B C4                        mov rax, r12
00279B31  4C 3B E8                        cmp r13, rax
00279B34  72 34                           jb 0x140279b6a
00279B36  49 8B CC                        mov rcx, r12
00279B39  48 C1 E1 19                     shl rcx, 0x19
00279B3D  49 BE FF FF FF FF FF F6 FF FF   movabs r14, 0xfffff6ffffffffff
00279B47  49 8B C6                        mov rax, r14
00279B4A  48 3B D8                        cmp rbx, rax
00279B4D  77 13                           ja 0x140279b62
00279B4F  48 C1 E3 19                     shl rbx, 0x19
00279B53  48 2B D9                        sub rbx, rcx
00279B56  48 C1 FB 10                     sar rbx, 0x10
00279B5A  49 8B C4                        mov rax, r12
00279B5D  48 3B D8                        cmp rbx, rax
00279B60  73 E5                           jae 0x140279b47
00279B62  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
00279B6A  49 8B CD                        mov rcx, r13
00279B6D  E8 2E 25 00 00                  call 0x14027c0a0
00279B72  B9 01 00 00 00                  mov ecx, 1
00279B77  48 8B F8                        mov rdi, rax
00279B7A  41 8B EF                        mov ebp, r15d
00279B7D  E8 6E 25 00 00                  call 0x14027c0f0
00279B82  48 8B CF                        mov rcx, rdi
00279B85  E8 46 CD 09 00                  call 0x1403168d0
00279B8A  48 8B F0                        mov rsi, rax
00279B8D  48 85 C0                        test rax, rax
00279B90  0F 85 EA 15 00 00               jne 0x14027b180
00279B96  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00279B9F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00279BA6  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
00279BAD  48 81 C1 EC 03 00 00            add rcx, 0x3ec
00279BB4  E8 D7 09 FD FF                  call 0x14024a590
00279BB9  48 3B DF                        cmp rbx, rdi
00279BBC  0F 84 2A 1C 00 00               je 0x14027b7ec
00279BC2  48 C1 EF 09                     shr rdi, 9
00279BC6  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00279BD0  48 23 CF                        and rcx, rdi
00279BD3  49 8B C4                        mov rax, r12
00279BD6  48 03 C8                        add rcx, rax
00279BD9  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00279BDE  4C 8B 08                        mov r9, qword ptr [rax]
00279BE1  4C 8D 41 08                     lea r8, [rcx + 8]
00279BE5  48 B8 00 F0 FF FF FF FF 00 00   movabs rax, 0xfffffffff000
00279BEF  49 33 CD                        xor rcx, r13
00279BF2  48 85 C8                        test rax, rcx
00279BF5  0F 84 8D 08 00 00               je 0x14027a488
00279BFB  49 8B C8                        mov rcx, r8
00279BFE  49 8B C4                        mov rax, r12
00279C01  4C 3B C0                        cmp r8, rax
00279C04  72 2F                           jb 0x140279c35
00279C06  49 8B D4                        mov rdx, r12
00279C09  48 C1 E2 19                     shl rdx, 0x19
00279C0D  49 BF FF FF FF FF FF F6 FF FF   movabs r15, 0xfffff6ffffffffff
00279C17  49 8B C7                        mov rax, r15
00279C1A  48 3B C8                        cmp rcx, rax
00279C1D  77 13                           ja 0x140279c32
00279C1F  48 C1 E1 19                     shl rcx, 0x19
00279C23  48 2B CA                        sub rcx, rdx
00279C26  48 C1 F9 10                     sar rcx, 0x10
00279C2A  49 8B C4                        mov rax, r12
00279C2D  48 3B C8                        cmp rcx, rax
00279C30  73 E5                           jae 0x140279c17
00279C32  45 33 FF                        xor r15d, r15d
00279C35  49 83 E5 F8                     and r13, 0xfffffffffffffff8
00279C39  49 89 4E 50                     mov qword ptr [r14 + 0x50], rcx
00279C3D  49 81 CD F8 0F 00 00            or r13, 0xff8
00279C44  49 83 C5 08                     add r13, 8
00279C48  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00279C4D  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00279C52  49 8B C2                        mov rax, r10
00279C55  4C 89 2F                        mov qword ptr [rdi], r13
00279C58  4D 85 D2                        test r10, r10
00279C5B  74 22                           je 0x140279c7f
00279C5D  49 8B D4                        mov rdx, r12
00279C60  48 C1 E2 19                     shl rdx, 0x19
00279C64  48 8B CF                        mov rcx, rdi
00279C67  49 C1 E5 19                     shl r13, 0x19
00279C6B  48 8D 49 F8                     lea rcx, [rcx - 8]
00279C6F  4C 2B EA                        sub r13, rdx
00279C72  49 C1 FD 10                     sar r13, 0x10
00279C76  4C 89 29                        mov qword ptr [rcx], r13
00279C79  48 83 E8 01                     sub rax, 1
00279C7D  75 E8                           jne 0x140279c67
00279C7F  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
00279C86  41 8B C7                        mov eax, r15d
00279C89  41 89 46 0C                     mov dword ptr [r14 + 0xc], eax
00279C8D  4D 3B C1                        cmp r8, r9
00279C90  4C 8B 2F                        mov r13, qword ptr [rdi]
00279C93  B8 04 00 00 00                  mov eax, 4
00279C98  8B AC 24 E0 00 00 00            mov ebp, dword ptr [rsp + 0xe0]
00279C9F  0F 47 F0                        cmova esi, eax
00279CA2  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
00279CA9  E9 9D FC FF FF                  jmp 0x14027994b
00279CAE  A8 01                           test al, 1
00279CB0  0F 85 40 07 00 00               jne 0x14027a3f6
00279CB6  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00279CBB  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00279CC1  A8 0F                           test al, 0xf
00279CC3  0F 84 2D 07 00 00               je 0x14027a3f6
00279CC9  45 33 FF                        xor r15d, r15d
00279CCC  44 89 BC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r15d
00279CD4  41 8B F7                        mov esi, r15d
00279CD7  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
00279CDB  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00279CE0  FF C0                           inc eax
00279CE2  4C 63 D5                        movsxd r10, ebp
00279CE5  49 8B CA                        mov rcx, r10
00279CE8  4D 8D 6C C5 00                  lea r13, [r13 + rax*8]
00279CED  4C 89 2F                        mov qword ptr [rdi], r13
00279CF0  85 ED                           test ebp, ebp
00279CF2  74 2F                           je 0x140279d23
00279CF4  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00279CFE  4C 8B C0                        mov r8, rax
00279D01  49 C1 E0 19                     shl r8, 0x19
00279D05  48 8B D7                        mov rdx, rdi
00279D08  49 8B C5                        mov rax, r13
00279D0B  48 C1 E0 19                     shl rax, 0x19
00279D0F  48 8D 52 F8                     lea rdx, [rdx - 8]
00279D13  49 2B C0                        sub rax, r8
00279D16  48 C1 F8 10                     sar rax, 0x10
00279D1A  48 89 02                        mov qword ptr [rdx], rax
00279D1D  48 83 E9 01                     sub rcx, 1
00279D21  75 E8                           jne 0x140279d0b
00279D23  45 89 7E 0C                     mov dword ptr [r14 + 0xc], r15d
00279D27  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
00279D2E  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00279D32  A8 01                           test al, 1
00279D34  0F 85 11 FC FF FF               jne 0x14027994b
00279D3A  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
00279D3F  BB 01 00 00 00                  mov ebx, 1
00279D44  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
00279D4E  49 BC 00 D0 BE 7D FB F6 FF FF   movabs r12, 0xfffff6fb7dbed000
00279D58  48 BA 68 DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedf68
00279D62  44 8D 43 01                     lea r8d, [rbx + 1]
00279D66  83 FE 04                        cmp esi, 4
00279D69  0F 8C 19 FA FF FF               jl 0x140279788
00279D6F  E9 D7 FB FF FF                  jmp 0x14027994b
00279D74  41 83 FA 03                     cmp r10d, 3
00279D78  0F 84 E7 FC FF FF               je 0x140279a65
00279D7E  45 8B D9                        mov r11d, r9d
00279D81  41 C1 EB 02                     shr r11d, 2
00279D85  41 83 E3 07                     and r11d, 7
00279D89  41 F6 C1 1C                     test r9b, 0x1c
00279D8D  0F 84 D2 FC FF FF               je 0x140279a65
00279D93  8B D5                           mov edx, ebp
00279D95  49 8B CE                        mov rcx, r14
00279D98  E8 C3 C5 1E 00                  call 0x140466360
00279D9D  49 3B C5                        cmp rax, r13
00279DA0  0F 85 BF FC FF FF               jne 0x140279a65
00279DA6  41 8D 43 FF                     lea eax, [r11 - 1]
00279DAA  3B C5                           cmp eax, ebp
00279DAC  0F 8D B3 FC FF FF               jge 0x140279a65
00279DB2  83 E3 E3                        and ebx, 0xffffffe3
00279DB5  4D 89 7E 48                     mov qword ptr [r14 + 0x48], r15
00279DB9  41 89 5E 04                     mov dword ptr [r14 + 4], ebx
00279DBD  E9 A3 FC FF FF                  jmp 0x140279a65
00279DC2  E8 69 1D 00 00                  call 0x14027bb30
00279DC7  E9 6B FC FF FF                  jmp 0x140279a37
00279DCC  41 8B C7                        mov eax, r15d
00279DCF  E9 7F FA FF FF                  jmp 0x140279853
00279DD4  8B C3                           mov eax, ebx
00279DD6  C1 E8 06                        shr eax, 6
00279DD9  83 E0 07                        and eax, 7
00279DDC  3B E8                           cmp ebp, eax
00279DDE  0F 8E FE 05 00 00               jle 0x14027a3e2
00279DE4  49 8B 86 B0 00 00 00            mov rax, qword ptr [r14 + 0xb0]
00279DEB  83 CB 20                        or ebx, 0x20
00279DEE  41 89 5E 04                     mov dword ptr [r14 + 4], ebx
00279DF2  48 85 C0                        test rax, rax
00279DF5  74 4E                           je 0x140279e45
00279DF7  48 8D 0D 12 EF 1A 00            lea rcx, [rip + 0x1aef12]
00279DFE  48 3B C1                        cmp rax, rcx
00279E01  0F 85 DF 08 00 00               jne 0x14027a6e6
00279E07  49 8B 9E B8 00 00 00            mov rbx, qword ptr [r14 + 0xb8]
00279E0E  8B 03                           mov eax, dword ptr [rbx]
00279E10  A8 03                           test al, 3
00279E12  0F 84 E3 15 00 00               je 0x14027b3fb
00279E18  41 B9 01 00 00 00               mov r9d, 1
00279E1E  48 8D 05 DB 3F 21 00            lea rax, [rip + 0x213fdb]
00279E25  45 33 C0                        xor r8d, r8d
00279E28  48 8D 53 38                     lea rdx, [rbx + 0x38]
00279E2C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00279E31  49 8B CE                        mov rcx, r14
00279E34  E8 57 00 FC FF                  call 0x140239e90
00279E39  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00279E3D  A8 20                           test al, 0x20
00279E3F  74 04                           je 0x140279e45
00279E41  C6 43 06 01                     mov byte ptr [rbx + 6], 1
00279E45  41 8B CF                        mov ecx, r15d
00279E48  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00279E4C  83 E0 DF                        and eax, 0xffffffdf
00279E4F  41 89 46 04                     mov dword ptr [r14 + 4], eax
00279E53  A8 01                           test al, 1
00279E55  0F 85 95 02 00 00               jne 0x14027a0f0
00279E5B  83 F9 04                        cmp ecx, 4
00279E5E  0F 8C AA 0B 00 00               jl 0x14027aa0e
00279E64  8B 9C 24 D8 00 00 00            mov ebx, dword ptr [rsp + 0xd8]
00279E6B  83 F9 05                        cmp ecx, 5
00279E6E  B8 05 00 00 00                  mov eax, 5
00279E73  0F 44 D8                        cmove ebx, eax
00279E76  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
00279E7D  E9 77 02 00 00                  jmp 0x14027a0f9
00279E82  41 8B D7                        mov edx, r15d
00279E85  83 FA 04                        cmp edx, 4
00279E88  73 18                           jae 0x140279ea2
00279E8A  8B C2                           mov eax, edx
00279E8C  48 C1 E0 06                     shl rax, 6
00279E90  42 8B 0C 00                     mov ecx, dword ptr [rax + r8]
00279E94  0F BA E1 1E                     bt ecx, 0x1e
00279E98  0F 82 C7 F9 FF FF               jb 0x140279865
00279E9E  FF C2                           inc edx
00279EA0  EB E3                           jmp 0x140279e85
00279EA2  41 8B 06                        mov eax, dword ptr [r14]
00279EA5  A8 04                           test al, 4
00279EA7  0F 84 BE 00 00 00               je 0x140279f6b
00279EAD  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00279EB7  4D 8B C5                        mov r8, r13
00279EBA  49 C1 E8 09                     shr r8, 9
00279EBE  4C 23 C0                        and r8, rax
00279EC1  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00279ECB  48 8B C0                        mov rax, rax
00279ECE  4C 03 C0                        add r8, rax
00279ED1  48 BF 68 DF BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbedf68
00279EDB  48 8B C7                        mov rax, rdi
00279EDE  4C 3B C0                        cmp r8, rax
00279EE1  0F 84 A9 05 00 00               je 0x14027a490
00279EE7  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00279EEE  A8 0F                           test al, 0xf
00279EF0  0F 84 FE 00 00 00               je 0x140279ff4
00279EF6  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00279EFD  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
00279F07  A8 0F                           test al, 0xf
00279F09  74 1E                           je 0x140279f29
00279F0B  48 8B C1                        mov rax, rcx
00279F0E  4C 3B C0                        cmp r8, rax
00279F11  72 16                           jb 0x140279f29
00279F13  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00279F1D  48 8B C0                        mov rax, rax
00279F20  4C 3B C0                        cmp r8, rax
00279F23  0F 86 9C 05 00 00               jbe 0x14027a4c5
00279F29  49 8B 00                        mov rax, qword ptr [r8]
00279F2C  48 8B C9                        mov rcx, rcx
00279F2F  4C 3B C1                        cmp r8, rcx
00279F32  72 28                           jb 0x140279f5c
00279F34  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00279F3E  48 8B C9                        mov rcx, rcx
00279F41  4C 3B C1                        cmp r8, rcx
00279F44  77 16                           ja 0x140279f5c
00279F46  A8 01                           test al, 1
00279F48  74 12                           je 0x140279f5c
00279F4A  A8 42                           test al, 0x42
00279F4C  0F 95 C2                        setne dl
00279F4F  A8 20                           test al, 0x20
00279F51  0F 95 C1                        setne cl
00279F54  84 D1                           test cl, dl
00279F56  0F 84 0B 01 00 00               je 0x14027a067
00279F5C  48 C1 E8 3C                     shr rax, 0x3c
00279F60  83 E0 02                        and eax, 2
00279F63  85 C0                           test eax, eax
00279F65  0F 85 04 F9 FF FF               jne 0x14027986f
00279F6B  41 80 7E 09 02                  cmp byte ptr [r14 + 9], 2
00279F70  0F 83 A5 FA FF FF               jae 0x140279a1b
00279F76  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00279F7F  45 8B C7                        mov r8d, r15d
00279F82  45 8B CF                        mov r9d, r15d
00279F85  8B 91 BC 38 00 00               mov edx, dword ptr [rcx + 0x38bc]
00279F8B  8B B9 AC 83 00 00               mov edi, dword ptr [rcx + 0x83ac]
00279F91  8B B1 5C 86 00 00               mov esi, dword ptr [rcx + 0x865c]
00279F97  F6 C2 01                        test dl, 1
00279F9A  0F 85 30 01 00 00               jne 0x14027a0d0
00279FA0  80 79 20 00                     cmp byte ptr [rcx + 0x20], 0
00279FA4  0F 85 C5 06 00 00               jne 0x14027a66f
00279FAA  F6 C2 1E                        test dl, 0x1e
00279FAD  0F 85 81 06 00 00               jne 0x14027a634
00279FB3  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00279FBA  84 C0                           test al, al
00279FBC  0F 85 CF 06 00 00               jne 0x14027a691
00279FC2  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00279FC6  48 85 C0                        test rax, rax
00279FC9  0F 85 8F 06 00 00               jne 0x14027a65e
00279FCF  83 FF 07                        cmp edi, 7
00279FD2  0F 86 43 FA FF FF               jbe 0x140279a1b
00279FD8  45 85 C0                        test r8d, r8d
00279FDB  0F 84 B7 06 00 00               je 0x14027a698
00279FE1  F6 C2 1E                        test dl, 0x1e
00279FE4  0F 84 E8 06 00 00               je 0x14027a6d2
00279FEA  BB 05 00 00 00                  mov ebx, 5
00279FEF  E9 45 06 00 00                  jmp 0x14027a639
00279FF4  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00279FFE  48 8B C0                        mov rax, rax
0027A001  4C 3B C0                        cmp r8, rax
0027A004  0F 82 EC FE FF FF               jb 0x140279ef6
0027A00A  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027A014  48 8B C0                        mov rax, rax
0027A017  4C 3B C0                        cmp r8, rax
0027A01A  0F 87 D6 FE FF FF               ja 0x140279ef6
0027A020  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027A029  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027A030  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027A037  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0027A03E  48 85 C9                        test rcx, rcx
0027A041  0F 84 AF FE FF FF               je 0x140279ef6
0027A047  41 C1 E8 03                     shr r8d, 3
0027A04B  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0027A052  42 8B 0C 81                     mov ecx, dword ptr [rcx + r8*4]
0027A056  0F BA E1 1E                     bt ecx, 0x1e
0027A05A  0F 83 73 17 00 00               jae 0x14027b7d3
0027A060  8B C3                           mov eax, ebx
0027A062  E9 FC FE FF FF                  jmp 0x140279f63
0027A067  48 F7 05 16 CA D4 00 00 00 60 00  test qword ptr [rip + 0xd4ca16], 0x600000
0027A072  0F 84 E4 FE FF FF               je 0x140279f5c
0027A078  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0027A081  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0027A088  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
0027A08F  0F 84 C7 FE FF FF               je 0x140279f5c
0027A095  48 8B 8A 08 05 00 00            mov rcx, qword ptr [rdx + 0x508]
0027A09C  48 85 C9                        test rcx, rcx
0027A09F  0F 84 B7 FE FF FF               je 0x140279f5c
0027A0A5  49 C1 E8 03                     shr r8, 3
0027A0A9  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0027A0B0  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
0027A0B4  F6 C1 20                        test cl, 0x20
0027A0B7  74 04                           je 0x14027a0bd
0027A0B9  48 83 C8 20                     or rax, 0x20
0027A0BD  48 8B D0                        mov rdx, rax
0027A0C0  48 83 C8 42                     or rax, 0x42
0027A0C4  F6 C1 42                        test cl, 0x42
0027A0C7  48 0F 44 C2                     cmove rax, rdx
0027A0CB  E9 8C FE FF FF                  jmp 0x140279f5c
0027A0D0  44 8B C3                        mov r8d, ebx
0027A0D3  83 FE 07                        cmp esi, 7
0027A0D6  0F 86 F3 FE FF FF               jbe 0x140279fcf
0027A0DC  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0027A0E3  84 C0                           test al, al
0027A0E5  0F 85 4E 05 00 00               jne 0x14027a639
0027A0EB  E9 F1 FE FF FF                  jmp 0x140279fe1
0027A0F0  83 F9 04                        cmp ecx, 4
0027A0F3  0F 8D 6B FD FF FF               jge 0x140279e64
0027A0F9  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
0027A100  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A105  4C 63 D5                        movsxd r10, ebp
0027A108  E9 3E F8 FF FF                  jmp 0x14027994b
0027A10D  49 8B 4E 58                     mov rcx, qword ptr [r14 + 0x58]
0027A111  4C 8B 99 00 49 00 00            mov r11, qword ptr [rcx + 0x4900]
0027A118  49 81 FB 20 04 00 00            cmp r11, 0x420
0027A11F  0F 83 C1 F6 FF FF               jae 0x1402797e6
0027A125  48 8B 69 10                     mov rbp, qword ptr [rcx + 0x10]
0027A129  45 33 C9                        xor r9d, r9d
0027A12C  44 8B 3D 99 3B BB 00            mov r15d, dword ptr [rip + 0xbb3b99]
0027A133  41 8B C1                        mov eax, r9d
0027A136  0F B7 35 C3 AE D4 00            movzx esi, word ptr [rip + 0xd4aec3]
0027A13D  48 81 C5 60 3A 00 00            add rbp, 0x3a60
0027A144  3B C6                           cmp eax, esi
0027A146  0F 83 6A 15 00 00               jae 0x14027b6b6
0027A14C  49 8B D9                        mov rbx, r9
0027A14F  48 8B FD                        mov rdi, rbp
0027A152  48 83 FB 01                     cmp rbx, 1
0027A156  0F 8F F0 13 00 00               jg 0x14027b54c
0027A15C  4C 8B 17                        mov r10, qword ptr [rdi]
0027A15F  45 3B CF                        cmp r9d, r15d
0027A162  0F 83 D5 13 00 00               jae 0x14027b53d
0027A168  41 8B C9                        mov ecx, r9d
0027A16B  48 03 C9                        add rcx, rcx
0027A16E  41 0F B7 0C CA                  movzx ecx, word ptr [r10 + rcx*8]
0027A173  4C 03 D9                        add r11, rcx
0027A176  49 81 FB 20 04 00 00            cmp r11, 0x420
0027A17D  0F 82 D4 05 00 00               jb 0x14027a757
0027A183  8B AC 24 E0 00 00 00            mov ebp, dword ptr [rsp + 0xe0]
0027A18A  45 33 FF                        xor r15d, r15d
0027A18D  41 8D 5F 01                     lea ebx, [r15 + 1]
0027A191  E9 50 F6 FF FF                  jmp 0x1402797e6
0027A196  C1 EA 02                        shr edx, 2
0027A199  83 E2 07                        and edx, 7
0027A19C  3B EA                           cmp ebp, edx
0027A19E  74 28                           je 0x14027a1c8
0027A1A0  8B C5                           mov eax, ebp
0027A1A2  49 BB F8 FF FF FF 7F 00 00 00   movabs r11, 0x7ffffffff8
0027A1AC  2B C2                           sub eax, edx
0027A1AE  8B D0                           mov edx, eax
0027A1B0  48 C1 E9 09                     shr rcx, 9
0027A1B4  49 23 CB                        and rcx, r11
0027A1B7  49 8B C1                        mov rax, r9
0027A1BA  48 03 C8                        add rcx, rax
0027A1BD  48 83 EA 01                     sub rdx, 1
0027A1C1  75 ED                           jne 0x14027a1b0
0027A1C3  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0027A1C8  4C 3B E9                        cmp r13, rcx
0027A1CB  0F 83 E2 F5 FF FF               jae 0x1402797b3
0027A1D1  8B D5                           mov edx, ebp
0027A1D3  49 8B CE                        mov rcx, r14
0027A1D6  E8 85 C1 1E 00                  call 0x140466360
0027A1DB  48 89 07                        mov qword ptr [rdi], rax
0027A1DE  4C 8B E8                        mov r13, rax
0027A1E1  49 8B CA                        mov rcx, r10
0027A1E4  4D 85 D2                        test r10, r10
0027A1E7  74 22                           je 0x14027a20b
0027A1E9  4D 8B C1                        mov r8, r9
0027A1EC  49 C1 E0 19                     shl r8, 0x19
0027A1F0  48 8B D7                        mov rdx, rdi
0027A1F3  48 C1 E0 19                     shl rax, 0x19
0027A1F7  48 8D 52 F8                     lea rdx, [rdx - 8]
0027A1FB  49 2B C0                        sub rax, r8
0027A1FE  48 C1 F8 10                     sar rax, 0x10
0027A202  48 89 02                        mov qword ptr [rdx], rax
0027A205  48 83 E9 01                     sub rcx, 1
0027A209  75 E8                           jne 0x14027a1f3
0027A20B  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
0027A212  41 B8 02 00 00 00               mov r8d, 2
0027A218  49 BC 00 D0 BE 7D FB F6 FF FF   movabs r12, 0xfffff6fb7dbed000
0027A222  48 BA 68 DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedf68
0027A22C  4D 3B EB                        cmp r13, r11
0027A22F  0F 87 EC 05 00 00               ja 0x14027a821
0027A235  E9 2F F5 FF FF                  jmp 0x140279769
0027A23A  41 83 66 04 E3                  and dword ptr [r14 + 4], 0xffffffe3
0027A23F  4D 89 7E 48                     mov qword ptr [r14 + 0x48], r15
0027A243  E9 6B F5 FF FF                  jmp 0x1402797b3
0027A248  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0027A24C  A8 02                           test al, 2
0027A24E  0F 85 CC 04 00 00               jne 0x14027a720
0027A254  83 FE 04                        cmp esi, 4
0027A257  0F 8D C4 05 00 00               jge 0x14027a821
0027A25D  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0027A261  A8 01                           test al, 1
0027A263  74 51                           je 0x14027a2b6
0027A265  83 FD 03                        cmp ebp, 3
0027A268  0F 85 AB 05 00 00               jne 0x14027a819
0027A26E  41 8B 06                        mov eax, dword ptr [r14]
0027A271  A8 04                           test al, 4
0027A273  0F 84 CF 04 00 00               je 0x14027a748
0027A279  49 8B D5                        mov rdx, r13
0027A27C  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027A286  48 C1 EA 09                     shr rdx, 9
0027A28A  48 23 D0                        and rdx, rax
0027A28D  49 8B C1                        mov rax, r9
0027A290  48 03 D0                        add rdx, rax
0027A293  45 33 C0                        xor r8d, r8d
0027A296  49 8B CE                        mov rcx, r14
0027A299  E8 02 77 00 00                  call 0x1402819a0
0027A29E  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0027A2A3  41 B8 02 00 00 00               mov r8d, 2
0027A2A9  4C 63 D5                        movsxd r10, ebp
0027A2AC  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0027A2B6  44 89 BC 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r15d
0027A2BE  E9 D6 F4 FF FF                  jmp 0x140279799
0027A2C3  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A2C8  B8 04 00 00 00                  mov eax, 4
0027A2CD  8B F0                           mov esi, eax
0027A2CF  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0027A2D6  4C 63 D5                        movsxd r10, ebp
0027A2D9  4C 8B 2F                        mov r13, qword ptr [rdi]
0027A2DC  E9 6A F6 FF FF                  jmp 0x14027994b
0027A2E1  0F 57 C0                        xorps xmm0, xmm0
0027A2E4  4D 8B CD                        mov r9, r13
0027A2E7  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0027A2EC  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0027A2F1  85 ED                           test ebp, ebp
0027A2F3  0F 85 B8 04 00 00               jne 0x14027a7b1
0027A2F9  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027A303  48 8B D1                        mov rdx, rcx
0027A306  48 C1 EA 09                     shr rdx, 9
0027A30A  41 BA 00 10 00 00               mov r10d, 0x1000
0027A310  48 23 D0                        and rdx, rax
0027A313  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0027A31D  48 8B C0                        mov rax, rax
0027A320  48 03 D0                        add rdx, rax
0027A323  44 8B C5                        mov r8d, ebp
0027A326  85 ED                           test ebp, ebp
0027A328  0F 85 49 04 00 00               jne 0x14027a777
0027A32E  4C 3B EA                        cmp r13, rdx
0027A331  0F 84 72 02 00 00               je 0x14027a5a9
0027A337  0F 87 F2 10 00 00               ja 0x14027b42f
0027A33D  49 3B D3                        cmp rdx, r11
0027A340  0F 86 7A 04 00 00               jbe 0x14027a7c0
0027A346  4D 8D 4B 08                     lea r9, [r11 + 8]
0027A34A  49 8B CF                        mov rcx, r15
0027A34D  4C 89 0F                        mov qword ptr [rdi], r9
0027A350  49 8B C1                        mov rax, r9
0027A353  48 63 FD                        movsxd rdi, ebp
0027A356  4C 8B C7                        mov r8, rdi
0027A359  85 ED                           test ebp, ebp
0027A35B  74 31                           je 0x14027a38e
0027A35D  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0027A367  4C 8B D2                        mov r10, rdx
0027A36A  48 8D 57 0C                     lea rdx, [rdi + 0xc]
0027A36E  49 C1 E2 19                     shl r10, 0x19
0027A372  49 8D 14 D6                     lea rdx, [r14 + rdx*8]
0027A376  48 C1 E0 19                     shl rax, 0x19
0027A37A  48 8D 52 F8                     lea rdx, [rdx - 8]
0027A37E  49 2B C2                        sub rax, r10
0027A381  48 C1 F8 10                     sar rax, 0x10
0027A385  48 89 02                        mov qword ptr [rdx], rax
0027A388  49 83 E8 01                     sub r8, 1
0027A38C  75 E8                           jne 0x14027a376
0027A38E  48 85 C9                        test rcx, rcx
0027A391  0F 85 19 02 00 00               jne 0x14027a5b0
0027A397  4D 3B E9                        cmp r13, r9
0027A39A  0F 84 20 F4 FF FF               je 0x1402797c0
0027A3A0  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
0027A3A7  4D 8B E9                        mov r13, r9
0027A3AA  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A3AF  4C 63 D5                        movsxd r10, ebp
0027A3B2  E9 A7 F5 FF FF                  jmp 0x14027995e
0027A3B7  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A3BC  41 8B F7                        mov esi, r15d
0027A3BF  44 89 BC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r15d
0027A3C7  4C 63 D5                        movsxd r10, ebp
0027A3CA  4C 8B 2F                        mov r13, qword ptr [rdi]
0027A3CD  E9 79 F5 FF FF                  jmp 0x14027994b
0027A3D2  3C 09                           cmp al, 9
0027A3D4  0F 84 3F F7 FF FF               je 0x140279b19
0027A3DA  3C 08                           cmp al, 8
0027A3DC  0F 84 90 00 00 00               je 0x14027a472
0027A3E2  41 8B 06                        mov eax, dword ptr [r14]
0027A3E5  A8 40                           test al, 0x40
0027A3E7  0F 85 DC F8 FF FF               jne 0x140279cc9
0027A3ED  83 FD 01                        cmp ebp, 1
0027A3F0  0F 8D B8 F8 FF FF               jge 0x140279cae
0027A3F6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0027A3FB  48 8D 0D 5E 7D 15 00            lea rcx, [rip + 0x157d5e]
0027A402  44 8B C5                        mov r8d, ebp
0027A405  49 8B D5                        mov rdx, r13
0027A408  48 3B C1                        cmp rax, rcx
0027A40B  0F 85 C8 03 00 00               jne 0x14027a7d9
0027A411  49 8B CE                        mov rcx, r14
0027A414  E8 47 7D 15 00                  call 0x1403d2160
0027A419  8B F0                           mov esi, eax
0027A41B  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0027A422  45 33 FF                        xor r15d, r15d
0027A425  83 FE 02                        cmp esi, 2
0027A428  0F 84 31 03 00 00               je 0x14027a75f
0027A42E  83 FE 03                        cmp esi, 3
0027A431  0F 85 A0 F8 FF FF               jne 0x140279cd7
0027A437  41 8D 57 01                     lea edx, [r15 + 1]
0027A43B  44 89 BC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r15d
0027A443  49 8B CE                        mov rcx, r14
0027A446  41 8B F7                        mov esi, r15d
0027A449  E8 D2 F8 FB FF                  call 0x140239d20
0027A44E  49 8B 4E 58                     mov rcx, qword ptr [r14 + 0x58]
0027A452  33 D2                           xor edx, edx
0027A454  E8 CB 8E 02 00                  call 0x1402a3324
0027A459  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A45E  B9 01 00 00 00                  mov ecx, 1
0027A463  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
0027A46A  4C 63 D5                        movsxd r10, ebp
0027A46D  E9 BC F8 FF FF                  jmp 0x140279d2e
0027A472  41 F7 06 00 00 01 00            test dword ptr [r14], 0x10000
0027A479  0F 85 63 FF FF FF               jne 0x14027a3e2
0027A47F  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
0027A486  EB 9A                           jmp 0x14027a422
0027A488  4D 8B E8                        mov r13, r8
0027A48B  E9 B8 F7 FF FF                  jmp 0x140279c48
0027A490  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0027A499  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
0027A4A0  24 0F                           and al, 0xf
0027A4A2  0F 85 57 03 00 00               jne 0x14027a7ff
0027A4A8  B8 30 00 00 00                  mov eax, 0x30
0027A4AD  48 8B 84 08 40 9C 00 00         mov rax, qword ptr [rax + rcx + 0x9c40]
0027A4B5  48 85 C0                        test rax, rax
0027A4B8  E9 A8 FA FF FF                  jmp 0x140279f65
0027A4BD  41 8B DF                        mov ebx, r15d
0027A4C0  E9 49 F4 FF FF                  jmp 0x14027990e
0027A4C5  48 8B C1                        mov rax, rcx
0027A4C8  4C 2B C0                        sub r8, rax
0027A4CB  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
0027A4D2  49 C1 F8 03                     sar r8, 3
0027A4D6  43 8D 14 00                     lea edx, [r8 + r8]
0027A4DA  8B C2                           mov eax, edx
0027A4DC  8B CA                           mov ecx, edx
0027A4DE  48 C1 E8 05                     shr rax, 5
0027A4E2  48 8D 15 57 26 BB 00            lea rdx, [rip + 0xbb2657]
0027A4E9  83 E1 1F                        and ecx, 0x1f
0027A4EC  8B 94 82 6C 26 00 00            mov edx, dword ptr [rdx + rax*4 + 0x266c]
0027A4F3  D3 EA                           shr edx, cl
0027A4F5  F6 C2 02                        test dl, 2
0027A4F8  0F 84 6D FA FF FF               je 0x140279f6b
0027A4FE  E9 6C F3 FF FF                  jmp 0x14027986f
0027A503  48 F7 05 7A C5 D4 00 00 00 60 00  test qword ptr [rip + 0xd4c57a], 0x600000
0027A50E  0F 84 F7 F5 FF FF               je 0x140279b0b
0027A514  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0027A51D  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0027A524  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
0027A52B  0F 84 DA F5 FF FF               je 0x140279b0b
0027A531  48 8B 8A 08 05 00 00            mov rcx, qword ptr [rdx + 0x508]
0027A538  48 85 C9                        test rcx, rcx
0027A53B  0F 84 CA F5 FF FF               je 0x140279b0b
0027A541  49 C1 E8 03                     shr r8, 3
0027A545  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0027A54C  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
0027A550  F6 C1 20                        test cl, 0x20
0027A553  74 04                           je 0x14027a559
0027A555  48 83 C8 20                     or rax, 0x20
0027A559  48 8B D0                        mov rdx, rax
0027A55C  48 83 C8 42                     or rax, 0x42
0027A560  F6 C1 42                        test cl, 0x42
0027A563  48 0F 44 C2                     cmove rax, rdx
0027A567  E9 9F F5 FF FF                  jmp 0x140279b0b
0027A56C  48 8D 05 8D E6 1A 00            lea rax, [rip + 0x1ae68d]
0027A573  49 8B CE                        mov rcx, r14
0027A576  48 3B D0                        cmp rdx, rax
0027A579  0F 85 21 10 00 00               jne 0x14027b5a0
0027A57F  49 8B 96 B8 00 00 00            mov rdx, qword ptr [r14 + 0xb8]
0027A586  48 8D 05 C3 29 22 00            lea rax, [rip + 0x2229c3]
0027A58D  48 83 C2 30                     add rdx, 0x30
0027A591  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027A596  45 33 C9                        xor r9d, r9d
0027A599  45 33 C0                        xor r8d, r8d
0027A59C  E8 EF F8 FB FF                  call 0x140239e90
0027A5A1  41 8B DF                        mov ebx, r15d
0027A5A4  E9 61 F3 FF FF                  jmp 0x14027990a
0027A5A9  4D 89 7E 50                     mov qword ptr [r14 + 0x50], r15
0027A5AD  48 63 FD                        movsxd rdi, ebp
0027A5B0  48 C1 E9 09                     shr rcx, 9
0027A5B4  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0027A5BE  49 23 C8                        and rcx, r8
0027A5C1  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0027A5CB  48 8B C2                        mov rax, rdx
0027A5CE  48 03 C8                        add rcx, rax
0027A5D1  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0027A5D6  48 C1 E9 09                     shr rcx, 9
0027A5DA  49 23 C8                        and rcx, r8
0027A5DD  48 8B C2                        mov rax, rdx
0027A5E0  48 03 C8                        add rcx, rax
0027A5E3  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0027A5E8  48 C1 E9 09                     shr rcx, 9
0027A5EC  49 23 C8                        and rcx, r8
0027A5EF  48 8B C2                        mov rax, rdx
0027A5F2  48 03 C8                        add rcx, rax
0027A5F5  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0027A5FA  48 C1 E9 09                     shr rcx, 9
0027A5FE  49 23 C8                        and rcx, r8
0027A601  48 8B C2                        mov rax, rdx
0027A604  48 03 C8                        add rcx, rax
0027A607  8B D5                           mov edx, ebp
0027A609  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0027A60E  48 8B CF                        mov rcx, rdi
0027A611  48 8B 44 CC 60                  mov rax, qword ptr [rsp + rcx*8 + 0x60]
0027A616  3B D5                           cmp edx, ebp
0027A618  49 89 44 CE 60                  mov qword ptr [r14 + rcx*8 + 0x60], rax
0027A61D  49 0F 45 C1                     cmovne rax, r9
0027A621  4C 8B C8                        mov r9, rax
0027A624  48 85 C9                        test rcx, rcx
0027A627  0F 84 6A FD FF FF               je 0x14027a397
0027A62D  FF CA                           dec edx
0027A62F  48 FF C9                        dec rcx
0027A632  EB DD                           jmp 0x14027a611
0027A634  BB 02 00 00 00                  mov ebx, 2
0027A639  F7 05 C1 C4 D4 00 00 00 00 04   test dword ptr [rip + 0xd4c4c1], 0x4000000
0027A643  74 0C                           je 0x14027a651
0027A645  44 8B C6                        mov r8d, esi
0027A648  8B D7                           mov edx, edi
0027A64A  8B CB                           mov ecx, ebx
0027A64C  E8 37 EA FF FF                  call 0x140279088
0027A651  85 DB                           test ebx, ebx
0027A653  0F 85 0C F2 FF FF               jne 0x140279865
0027A659  E9 BD F3 FF FF                  jmp 0x140279a1b
0027A65E  48 3B 41 08                     cmp rax, qword ptr [rcx + 8]
0027A662  0F 84 67 F9 FF FF               je 0x140279fcf
0027A668  BB 04 00 00 00                  mov ebx, 4
0027A66D  EB CA                           jmp 0x14027a639
0027A66F  44 8B CB                        mov r9d, ebx
0027A672  83 FF 07                        cmp edi, 7
0027A675  0F 86 A0 F3 FF FF               jbe 0x140279a1b
0027A67B  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0027A682  84 C0                           test al, al
0027A684  0F 84 57 F9 FF FF               je 0x140279fe1
0027A68A  BB 07 00 00 00                  mov ebx, 7
0027A68F  EB A8                           jmp 0x14027a639
0027A691  BB 03 00 00 00                  mov ebx, 3
0027A696  EB A1                           jmp 0x14027a639
0027A698  45 85 C9                        test r9d, r9d
0027A69B  0F 85 40 F9 FF FF               jne 0x140279fe1
0027A6A1  FA                              cli
0027A6A2  44 89 B9 AC 83 00 00            mov dword ptr [rcx + 0x83ac], r15d
0027A6A9  44 89 B9 5C 86 00 00            mov dword ptr [rcx + 0x865c], r15d
0027A6B0  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0027A6B9  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0027A6C0  4D 85 C0                        test r8, r8
0027A6C3  0F 85 77 0B 00 00               jne 0x14027b240
0027A6C9  FB                              sti
0027A6CA  41 8B DF                        mov ebx, r15d
0027A6CD  E9 67 FF FF FF                  jmp 0x14027a639
0027A6D2  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0027A6D6  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0027A6DA  74 C5                           je 0x14027a6a1
0027A6DC  BB 06 00 00 00                  mov ebx, 6
0027A6E1  E9 53 FF FF FF                  jmp 0x14027a639
0027A6E6  48 8D 0D 13 E5 1A 00            lea rcx, [rip + 0x1ae513]
0027A6ED  48 3B C1                        cmp rax, rcx
0027A6F0  0F 85 C6 0E 00 00               jne 0x14027b5bc
0027A6F6  49 8B 96 B8 00 00 00            mov rdx, qword ptr [r14 + 0xb8]
0027A6FD  48 8D 05 4C 28 22 00            lea rax, [rip + 0x22284c]
0027A704  48 83 C2 30                     add rdx, 0x30
0027A708  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027A70D  45 33 C9                        xor r9d, r9d
0027A710  45 33 C0                        xor r8d, r8d
0027A713  49 8B CE                        mov rcx, r14
0027A716  E8 75 F7 FB FF                  call 0x140239e90
0027A71B  E9 25 F7 FF FF                  jmp 0x140279e45
0027A720  83 FD 03                        cmp ebp, 3
0027A723  0F 85 F0 00 00 00               jne 0x14027a819
0027A729  83 C8 01                        or eax, 1
0027A72C  41 89 46 04                     mov dword ptr [r14 + 4], eax
0027A730  48 8B D2                        mov rdx, rdx
0027A733  44 8B C3                        mov r8d, ebx
0027A736  49 8B CE                        mov rcx, r14
0027A739  E8 62 72 00 00                  call 0x1402819a0
0027A73E  41 83 66 04 FD                  and dword ptr [r14 + 4], 0xfffffffd
0027A743  E9 56 FB FF FF                  jmp 0x14027a29e
0027A748  E8 53 91 0A 00                  call 0x1403238a0
0027A74D  41 83 66 04 FE                  and dword ptr [r14 + 4], 0xfffffffe
0027A752  E9 47 FB FF FF                  jmp 0x14027a29e
0027A757  41 FF C1                        inc r9d
0027A75A  E9 00 FA FF FF                  jmp 0x14027a15f
0027A75F  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A764  41 8B F7                        mov esi, r15d
0027A767  44 89 BC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r15d
0027A76F  4C 63 D5                        movsxd r10, ebp
0027A772  E9 B0 F5 FF FF                  jmp 0x140279d27
0027A777  48 BF 00 00 00 00 80 F6 FF FF   movabs rdi, 0xfffff68000000000
0027A781  49 BB F8 FF FF FF 7F 00 00 00   movabs r11, 0x7ffffffff8
0027A78B  48 C1 EA 09                     shr rdx, 9
0027A78F  49 23 D3                        and rdx, r11
0027A792  48 8B C7                        mov rax, rdi
0027A795  48 03 D0                        add rdx, rax
0027A798  49 C1 E2 09                     shl r10, 9
0027A79C  41 83 E8 01                     sub r8d, 1
0027A7A0  75 E9                           jne 0x14027a78b
0027A7A2  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0027A7A7  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027A7AC  E9 7D FB FF FF                  jmp 0x14027a32e
0027A7B1  41 83 FC 03                     cmp r12d, 3
0027A7B5  0F 84 3E FB FF FF               je 0x14027a2f9
0027A7BB  E9 00 F0 FF FF                  jmp 0x1402797c0
0027A7C0  49 8D 42 FF                     lea rax, [r10 - 1]
0027A7C4  4C 8B CA                        mov r9, rdx
0027A7C7  48 85 C1                        test rcx, rax
0027A7CA  0F 85 7D FB FF FF               jne 0x14027a34d
0027A7D0  4D 89 7E 50                     mov qword ptr [r14 + 0x50], r15
0027A7D4  E9 74 FB FF FF                  jmp 0x14027a34d
0027A7D9  48 8D 0D 70 4F 01 00            lea rcx, [rip + 0x14f70]
0027A7E0  48 3B C1                        cmp rax, rcx
0027A7E3  0F 85 0C 09 00 00               jne 0x14027b0f5
0027A7E9  49 8B CE                        mov rcx, r14
0027A7EC  E8 5F 4F 01 00                  call 0x14028f750
0027A7F1  8B F0                           mov esi, eax
0027A7F3  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0027A7FA  E9 23 FC FF FF                  jmp 0x14027a422
0027A7FF  3C 07                           cmp al, 7
0027A801  0F 84 C2 0A 00 00               je 0x14027b2c9
0027A807  3C 05                           cmp al, 5
0027A809  0F 84 BC 0F 00 00               je 0x14027b7cb
0027A80F  B8 48 00 00 00                  mov eax, 0x48
0027A814  E9 94 FC FF FF                  jmp 0x14027a4ad
0027A819  A8 1C                           test al, 0x1c
0027A81B  0F 84 8A 0F 00 00               je 0x14027b7ab
0027A821  41 BD 05 00 00 00               mov r13d, 5
0027A827  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0027A82B  49 8D 5E 04                     lea rbx, [r14 + 4]
0027A82F  8B C1                           mov eax, ecx
0027A831  83 E0 01                        and eax, 1
0027A834  83 FD 03                        cmp ebp, 3
0027A837  0F 84 98 00 00 00               je 0x14027a8d5
0027A83D  85 C0                           test eax, eax
0027A83F  75 7D                           jne 0x14027a8be
0027A841  49 8B 86 B0 00 00 00            mov rax, qword ptr [r14 + 0xb0]
0027A848  83 C9 20                        or ecx, 0x20
0027A84B  89 0B                           mov dword ptr [rbx], ecx
0027A84D  48 85 C0                        test rax, rax
0027A850  74 52                           je 0x14027a8a4
0027A852  48 8D 0D B7 E4 1A 00            lea rcx, [rip + 0x1ae4b7]
0027A859  48 3B C1                        cmp rax, rcx
0027A85C  0F 85 72 01 00 00               jne 0x14027a9d4
0027A862  49 8B BE B8 00 00 00            mov rdi, qword ptr [r14 + 0xb8]
0027A869  8B 07                           mov eax, dword ptr [rdi]
0027A86B  A8 03                           test al, 3
0027A86D  0F 84 0D 0D 00 00               je 0x14027b580
0027A873  B8 01 00 00 00                  mov eax, 1
0027A878  48 8D 0D 81 35 21 00            lea rcx, [rip + 0x213581]
0027A87F  44 8B C8                        mov r9d, eax
0027A882  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0027A887  48 8D 57 38                     lea rdx, [rdi + 0x38]
0027A88B  49 8B CE                        mov rcx, r14
0027A88E  45 33 C0                        xor r8d, r8d
0027A891  E8 FA F5 FB FF                  call 0x140239e90
0027A896  8B 03                           mov eax, dword ptr [rbx]
0027A898  A8 20                           test al, 0x20
0027A89A  74 04                           je 0x14027a8a0
0027A89C  C6 47 06 01                     mov byte ptr [rdi + 6], 1
0027A8A0  49 8D 5E 04                     lea rbx, [r14 + 4]
0027A8A4  8B 0B                           mov ecx, dword ptr [rbx]
0027A8A6  83 E1 DF                        and ecx, 0xffffffdf
0027A8A9  89 0B                           mov dword ptr [rbx], ecx
0027A8AB  F6 C1 01                        test cl, 1
0027A8AE  75 06                           jne 0x14027a8b6
0027A8B0  41 83 FF 04                     cmp r15d, 4
0027A8B4  7C 08                           jl 0x14027a8be
0027A8B6  41 83 FF 05                     cmp r15d, 5
0027A8BA  41 0F 44 F5                     cmove esi, r13d
0027A8BE  8B C6                           mov eax, esi
0027A8C0  48 81 C4 88 00 00 00            add rsp, 0x88
0027A8C7  41 5F                           pop r15
0027A8C9  41 5E                           pop r14
0027A8CB  41 5D                           pop r13
0027A8CD  41 5C                           pop r12
0027A8CF  5F                              pop rdi
0027A8D0  5E                              pop rsi
0027A8D1  5D                              pop rbp
0027A8D2  5B                              pop rbx
0027A8D3  C3                              ret
0027A8D4  CC                              int3
0027A8D5  49 8B 6E 20                     mov rbp, qword ptr [r14 + 0x20]
0027A8D9  48 8B FB                        mov rdi, rbx
0027A8DC  85 C0                           test eax, eax
0027A8DE  0F 85 BD 00 00 00               jne 0x14027a9a1
0027A8E4  41 8B 06                        mov eax, dword ptr [r14]
0027A8E7  A8 40                           test al, 0x40
0027A8E9  0F 85 69 08 00 00               jne 0x14027b158
0027A8EF  49 8B 86 B0 00 00 00            mov rax, qword ptr [r14 + 0xb0]
0027A8F6  83 C9 20                        or ecx, 0x20
0027A8F9  89 0B                           mov dword ptr [rbx], ecx
0027A8FB  48 85 C0                        test rax, rax
0027A8FE  0F 84 90 07 00 00               je 0x14027b094
0027A904  48 8D 0D 05 E4 1A 00            lea rcx, [rip + 0x1ae405]
0027A90B  48 3B C1                        cmp rax, rcx
0027A90E  0F 85 07 08 00 00               jne 0x14027b11b
0027A914  49 8B 9E B8 00 00 00            mov rbx, qword ptr [r14 + 0xb8]
0027A91B  8B 03                           mov eax, dword ptr [rbx]
0027A91D  A8 03                           test al, 3
0027A91F  0F 84 B6 0C 00 00               je 0x14027b5db
0027A925  B8 01 00 00 00                  mov eax, 1
0027A92A  48 8D 0D CF 34 21 00            lea rcx, [rip + 0x2134cf]
0027A931  44 8B C8                        mov r9d, eax
0027A934  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0027A939  48 8D 53 38                     lea rdx, [rbx + 0x38]
0027A93D  49 8B CE                        mov rcx, r14
0027A940  45 33 C0                        xor r8d, r8d
0027A943  E8 48 F5 FB FF                  call 0x140239e90
0027A948  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0027A94C  A8 20                           test al, 0x20
0027A94E  74 04                           je 0x14027a954
0027A950  C6 43 06 01                     mov byte ptr [rbx + 6], 1
0027A954  41 8B F7                        mov esi, r15d
0027A957  49 8D 7E 04                     lea rdi, [r14 + 4]
0027A95B  83 27 DF                        and dword ptr [rdi], 0xffffffdf
0027A95E  49 8B 56 38                     mov rdx, qword ptr [r14 + 0x38]
0027A962  48 85 D2                        test rdx, rdx
0027A965  74 2B                           je 0x14027a992
0027A967  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0027A971  48 8B C0                        mov rax, rax
0027A974  41 F7 06 00 10 00 00            test dword ptr [r14], 0x1000
0027A97B  0F 84 5D 09 00 00               je 0x14027b2de
0027A981  48 3B D0                        cmp rdx, rax
0027A984  0F 85 5D 09 00 00               jne 0x14027b2e7
0027A98A  4D 89 7E 38                     mov qword ptr [r14 + 0x38], r15
0027A98E  49 8D 7E 04                     lea rdi, [r14 + 4]
0027A992  83 FE 05                        cmp esi, 5
0027A995  41 8B F5                        mov esi, r13d
0027A998  74 07                           je 0x14027a9a1
0027A99A  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
0027A9A1  8B 07                           mov eax, dword ptr [rdi]
0027A9A3  A8 01                           test al, 1
0027A9A5  0F 84 13 FF FF FF               je 0x14027a8be
0027A9AB  41 8B 06                        mov eax, dword ptr [r14]
0027A9AE  41 0F B6 4E 09                  movzx ecx, byte ptr [r14 + 9]
0027A9B3  A8 04                           test al, 4
0027A9B5  0F 85 C0 06 00 00               jne 0x14027b07b
0027A9BB  80 F9 11                        cmp cl, 0x11
0027A9BE  48 8B CD                        mov rcx, rbp
0027A9C1  0F 85 AC 07 00 00               jne 0x14027b173
0027A9C7  E8 20 EC FB FF                  call 0x1402395ec
0027A9CC  83 27 FE                        and dword ptr [rdi], 0xfffffffe
0027A9CF  E9 EA FE FF FF                  jmp 0x14027a8be
0027A9D4  48 8D 0D 25 E2 1A 00            lea rcx, [rip + 0x1ae225]
0027A9DB  48 3B C1                        cmp rax, rcx
0027A9DE  0F 85 99 0C 00 00               jne 0x14027b67d
0027A9E4  49 8B 96 B8 00 00 00            mov rdx, qword ptr [r14 + 0xb8]
0027A9EB  48 8D 05 5E 25 22 00            lea rax, [rip + 0x22255e]
0027A9F2  48 83 C2 30                     add rdx, 0x30
0027A9F6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027A9FB  45 33 C9                        xor r9d, r9d
0027A9FE  45 33 C0                        xor r8d, r8d
0027AA01  49 8B CE                        mov rcx, r14
0027AA04  E8 87 F4 FB FF                  call 0x140239e90
0027AA09  E9 92 FE FF FF                  jmp 0x14027a8a0
0027AA0E  41 8B 06                        mov eax, dword ptr [r14]
0027AA11  A8 04                           test al, 4
0027AA13  0F 84 F3 01 00 00               je 0x14027ac0c
0027AA19  49 8B F5                        mov rsi, r13
0027AA1C  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0027AA26  48 C1 EE 09                     shr rsi, 9
0027AA2A  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027AA34  48 23 F0                        and rsi, rax
0027AA37  48 8B C2                        mov rax, rdx
0027AA3A  48 03 F0                        add rsi, rax
0027AA3D  49 B9 68 DF BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbedf68
0027AA47  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
0027AA4F  49 8B C1                        mov rax, r9
0027AA52  4C 3B E8                        cmp r13, rax
0027AA55  75 6A                           jne 0x14027aac1
0027AA57  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0027AA5C  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0027AA65  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0027AA6B  24 0F                           and al, 0xf
0027AA6D  0F 85 F6 02 00 00               jne 0x14027ad69
0027AA73  B9 02 00 00 00                  mov ecx, 2
0027AA78  48 81 C2 B0 00 00 00            add rdx, 0xb0
0027AA7F  8B C1                           mov eax, ecx
0027AA81  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
0027AA88  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0027AA8C  49 8D 0C C8                     lea rcx, [r8 + rcx*8]
0027AA90  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0027AA94  4C 89 39                        mov qword ptr [rcx], r15
0027AA97  90                              nop
0027AA98  F6 05 67 C0 D4 00 21            test byte ptr [rip + 0xd4c067], 0x21
0027AA9F  0F 85 BE 05 00 00               jne 0x14027b063
0027AAA5  48 8B C1                        mov rax, rcx
0027AAA8  48 87 02                        xchg qword ptr [rdx], rax
0027AAAB  48 85 C0                        test rax, rax
0027AAAE  0F 84 3B 01 00 00               je 0x14027abef
0027AAB4  48 8B D0                        mov rdx, rax
0027AAB7  E8 F4 D3 FD FF                  call 0x140257eb0
0027AABC  E9 24 01 00 00                  jmp 0x14027abe5
0027AAC1  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0027AAC6  49 B9 00 D0 BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbed000
0027AAD0  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
0027AAD7  A8 0F                           test al, 0xf
0027AAD9  75 41                           jne 0x14027ab1c
0027AADB  49 8B C1                        mov rax, r9
0027AADE  4C 3B E8                        cmp r13, rax
0027AAE1  72 39                           jb 0x14027ab1c
0027AAE3  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027AAED  48 8B C0                        mov rax, rax
0027AAF0  4C 3B E8                        cmp r13, rax
0027AAF3  77 27                           ja 0x14027ab1c
0027AAF5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027AAFE  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027AB05  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027AB0C  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0027AB13  48 85 C9                        test rcx, rcx
0027AB16  0F 85 81 0B 00 00               jne 0x14027b69d
0027AB1C  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
0027AB23  A8 0F                           test al, 0xf
0027AB25  74 1E                           je 0x14027ab45
0027AB27  49 8B C1                        mov rax, r9
0027AB2A  4C 3B E8                        cmp r13, rax
0027AB2D  72 16                           jb 0x14027ab45
0027AB2F  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027AB39  48 8B C0                        mov rax, rax
0027AB3C  4C 3B E8                        cmp r13, rax
0027AB3F  0F 86 F3 08 00 00               jbe 0x14027b438
0027AB45  49 8B 5D 00                     mov rbx, qword ptr [r13]
0027AB49  41 8B EF                        mov ebp, r15d
0027AB4C  49 8B C1                        mov rax, r9
0027AB4F  4C 3B E8                        cmp r13, rax
0027AB52  72 2B                           jb 0x14027ab7f
0027AB54  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
0027AB5E  48 8B C0                        mov rax, rax
0027AB61  4C 3B E8                        cmp r13, rax
0027AB64  77 19                           ja 0x14027ab7f
0027AB66  F6 C3 01                        test bl, 1
0027AB69  74 14                           je 0x14027ab7f
0027AB6B  F6 C3 42                        test bl, 0x42
0027AB6E  0F 95 C1                        setne cl
0027AB71  F6 C3 20                        test bl, 0x20
0027AB74  0F 95 C0                        setne al
0027AB77  84 C8                           test al, cl
0027AB79  0F 84 7D 02 00 00               je 0x14027adfc
0027AB7F  48 BE FF FF FF FF FF FF FF DF   movabs rsi, 0xdfffffffffffffff
0027AB89  F6 C3 01                        test bl, 1
0027AB8C  74 40                           je 0x14027abce
0027AB8E  48 8B C3                        mov rax, rbx
0027AB91  48 C1 E8 3C                     shr rax, 0x3c
0027AB95  A8 01                           test al, 1
0027AB97  0F 85 02 05 00 00               jne 0x14027b09f
0027AB9D  48 8B CB                        mov rcx, rbx
0027ABA0  48 B8 20 00 00 00 00 00 00 10   movabs rax, 0x1000000000000020
0027ABAA  48 23 CE                        and rcx, rsi
0027ABAD  48 0B C8                        or rcx, rax
0027ABB0  48 F7 05 CD BE D4 00 00 00 00 02  test qword ptr [rip + 0xd4becd], 0x2000000
0027ABBB  74 03                           je 0x14027abc0
0027ABBD  0F AE E8                        lfence
0027ABC0  48 8B C3                        mov rax, rbx
0027ABC3  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
0027ABC9  48 8B D8                        mov rbx, rax
0027ABCC  75 BB                           jne 0x14027ab89
0027ABCE  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
0027ABD6  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
0027ABDE  8B AC 24 E0 00 00 00            mov ebp, dword ptr [rsp + 0xe0]
0027ABE5  49 B9 68 DF BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbedf68
0027ABEF  49 8B C1                        mov rax, r9
0027ABF2  41 F7 06 00 10 00 00            test dword ptr [r14], 0x1000
0027ABF9  0F 84 6B 02 00 00               je 0x14027ae6a
0027ABFF  48 3B F0                        cmp rsi, rax
0027AC02  0F 85 6B 02 00 00               jne 0x14027ae73
0027AC08  4D 89 6E 38                     mov qword ptr [r14 + 0x38], r13
0027AC0C  49 8B 45 00                     mov rax, qword ptr [r13]
0027AC10  49 BC 00 D0 BE 7D FB F6 FF FF   movabs r12, 0xfffff6fb7dbed000
0027AC1A  49 8B CC                        mov rcx, r12
0027AC1D  4C 3B E9                        cmp r13, rcx
0027AC20  72 66                           jb 0x14027ac88
0027AC22  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
0027AC2C  48 8B C9                        mov rcx, rcx
0027AC2F  4C 3B E9                        cmp r13, rcx
0027AC32  77 54                           ja 0x14027ac88
0027AC34  A8 01                           test al, 1
0027AC36  74 50                           je 0x14027ac88
0027AC38  A8 42                           test al, 0x42
0027AC3A  0F 95 C1                        setne cl
0027AC3D  A8 20                           test al, 0x20
0027AC3F  0F 95 C0                        setne al
0027AC42  84 C8                           test al, cl
0027AC44  75 42                           jne 0x14027ac88
0027AC46  48 F7 05 37 BE D4 00 00 00 60 00  test qword ptr [rip + 0xd4be37], 0x600000
0027AC51  74 35                           je 0x14027ac88
0027AC53  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027AC5C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027AC63  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
0027AC6A  74 1C                           je 0x14027ac88
0027AC6C  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
0027AC73  48 85 D2                        test rdx, rdx
0027AC76  74 10                           je 0x14027ac88
0027AC78  49 8B C5                        mov rax, r13
0027AC7B  48 C1 E8 03                     shr rax, 3
0027AC7F  25 FF 01 00 00                  and eax, 0x1ff
0027AC84  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0027AC88  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0027AC92  48 8B F8                        mov rdi, rax
0027AC95  49 8B DD                        mov rbx, r13
0027AC98  48 C1 E7 19                     shl rdi, 0x19
0027AC9C  48 C1 E3 19                     shl rbx, 0x19
0027ACA0  44 8D 45 FF                     lea r8d, [rbp - 1]
0027ACA4  48 2B DF                        sub rbx, rdi
0027ACA7  49 8B CE                        mov rcx, r14
0027ACAA  48 8B D3                        mov rdx, rbx
0027ACAD  48 C1 FA 10                     sar rdx, 0x10
0027ACB1  E8 0A EA FF FF                  call 0x1402796c0
0027ACB6  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
0027ACBA  8B F0                           mov esi, eax
0027ACBC  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0027ACC3  F6 C2 03                        test dl, 3
0027ACC6  0F 85 CB 00 00 00               jne 0x14027ad97
0027ACCC  83 F8 04                        cmp eax, 4
0027ACCF  0F 8C 0A 08 00 00               jl 0x14027b4df
0027ACD5  48 63 C5                        movsxd rax, ebp
0027ACD8  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0027ACE2  49 8B 4C C6 58                  mov rcx, qword ptr [r14 + rax*8 + 0x58]
0027ACE7  48 8D 83 00 00 00 10            lea rax, [rbx + 0x10000000]
0027ACEE  48 C1 F8 10                     sar rax, 0x10
0027ACF2  48 3B C8                        cmp rcx, rax
0027ACF5  0F 82 3D 09 00 00               jb 0x14027b638
0027ACFB  48 C1 E9 09                     shr rcx, 9
0027ACFF  49 BD F8 FF FF FF 7F 00 00 00   movabs r13, 0x7ffffffff8
0027AD09  4C 23 E9                        and r13, rcx
0027AD0C  49 8B C1                        mov rax, r9
0027AD0F  4C 03 E8                        add r13, rax
0027AD12  4C 63 D5                        movsxd r10, ebp
0027AD15  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0027AD1A  49 8B CA                        mov rcx, r10
0027AD1D  4C 89 28                        mov qword ptr [rax], r13
0027AD20  85 ED                           test ebp, ebp
0027AD22  74 1E                           je 0x14027ad42
0027AD24  48 8B D0                        mov rdx, rax
0027AD27  49 8B C5                        mov rax, r13
0027AD2A  48 C1 E0 19                     shl rax, 0x19
0027AD2E  48 8D 52 F8                     lea rdx, [rdx - 8]
0027AD32  48 2B C7                        sub rax, rdi
0027AD35  48 C1 F8 10                     sar rax, 0x10
0027AD39  48 89 02                        mov qword ptr [rdx], rax
0027AD3C  48 83 E9 01                     sub rcx, 1
0027AD40  75 E8                           jne 0x14027ad2a
0027AD42  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0027AD47  49 8D 7A 0C                     lea rdi, [r10 + 0xc]
0027AD4B  BB 01 00 00 00                  mov ebx, 1
0027AD50  49 8D 3C FE                     lea rdi, [r14 + rdi*8]
0027AD54  8B CB                           mov ecx, ebx
0027AD56  89 9C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebx
0027AD5D  45 33 FF                        xor r15d, r15d
0027AD60  44 8D 43 01                     lea r8d, [rbx + 1]
0027AD64  E9 15 EA FF FF                  jmp 0x14027977e
0027AD69  3C 07                           cmp al, 7
0027AD6B  0F 84 94 04 00 00               je 0x14027b205
0027AD71  3C 05                           cmp al, 5
0027AD73  0F 84 62 0A 00 00               je 0x14027b7db
0027AD79  B9 03 00 00 00                  mov ecx, 3
0027AD7E  8B C1                           mov eax, ecx
0027AD80  48 8D 15 B9 1D BB 00            lea rdx, [rip + 0xbb1db9]
0027AD87  48 8D 14 C2                     lea rdx, [rdx + rax*8]
0027AD8B  48 81 C2 80 32 00 00            add rdx, 0x3280
0027AD92  E9 E8 FC FF FF                  jmp 0x14027aa7f
0027AD97  F6 C2 1C                        test dl, 0x1c
0027AD9A  75 2F                           jne 0x14027adcb
0027AD9C  48 63 CD                        movsxd rcx, ebp
0027AD9F  48 8D 83 00 00 00 10            lea rax, [rbx + 0x10000000]
0027ADA6  48 C1 F8 10                     sar rax, 0x10
0027ADAA  49 39 44 CE 58                  cmp qword ptr [r14 + rcx*8 + 0x58], rax
0027ADAF  72 1A                           jb 0x14027adcb
0027ADB1  85 ED                           test ebp, ebp
0027ADB3  74 16                           je 0x14027adcb
0027ADB5  40 0F B6 C5                     movzx eax, bpl
0027ADB9  C1 E0 02                        shl eax, 2
0027ADBC  33 C2                           xor eax, edx
0027ADBE  4D 89 6E 48                     mov qword ptr [r14 + 0x48], r13
0027ADC2  83 E0 1C                        and eax, 0x1c
0027ADC5  33 C2                           xor eax, edx
0027ADC7  41 89 46 04                     mov dword ptr [r14 + 4], eax
0027ADCB  45 33 FF                        xor r15d, r15d
0027ADCE  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0027ADD3  BB 01 00 00 00                  mov ebx, 1
0027ADD8  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027ADDD  8B CB                           mov ecx, ebx
0027ADDF  89 9C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebx
0027ADE6  4C 63 D5                        movsxd r10, ebp
0027ADE9  44 8D 43 01                     lea r8d, [rbx + 1]
0027ADED  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0027ADF7  E9 82 E9 FF FF                  jmp 0x14027977e
0027ADFC  48 F7 05 81 BC D4 00 00 00 60 00  test qword ptr [rip + 0xd4bc81], 0x600000
0027AE07  0F 84 72 FD FF FF               je 0x14027ab7f
0027AE0D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027AE16  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027AE1D  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
0027AE24  0F 84 55 FD FF FF               je 0x14027ab7f
0027AE2A  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
0027AE31  48 85 D2                        test rdx, rdx
0027AE34  74 25                           je 0x14027ae5b
0027AE36  49 8B C5                        mov rax, r13
0027AE39  48 C1 E8 03                     shr rax, 3
0027AE3D  25 FF 01 00 00                  and eax, 0x1ff
0027AE42  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0027AE46  A8 20                           test al, 0x20
0027AE48  74 04                           je 0x14027ae4e
0027AE4A  48 83 CB 20                     or rbx, 0x20
0027AE4E  48 8B CB                        mov rcx, rbx
0027AE51  48 83 CB 42                     or rbx, 0x42
0027AE55  A8 42                           test al, 0x42
0027AE57  48 0F 44 D9                     cmove rbx, rcx
0027AE5B  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0027AE65  E9 15 FD FF FF                  jmp 0x14027ab7f
0027AE6A  48 3B F0                        cmp rsi, rax
0027AE6D  0F 84 B2 00 00 00               je 0x14027af25
0027AE73  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0027AE78  49 B9 00 D0 BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbed000
0027AE82  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
0027AE89  A8 0F                           test al, 0xf
0027AE8B  74 22                           je 0x14027aeaf
0027AE8D  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
0027AE94  A8 0F                           test al, 0xf
0027AE96  0F 85 0D 01 00 00               jne 0x14027afa9
0027AE9C  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
0027AEA6  F0 48 21 06                     lock and qword ptr [rsi], rax
0027AEAA  E9 59 FD FF FF                  jmp 0x14027ac08
0027AEAF  49 8B C1                        mov rax, r9
0027AEB2  48 3B F0                        cmp rsi, rax
0027AEB5  72 D6                           jb 0x14027ae8d
0027AEB7  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027AEC1  48 8B C0                        mov rax, rax
0027AEC4  48 3B F0                        cmp rsi, rax
0027AEC7  77 C4                           ja 0x14027ae8d
0027AEC9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027AED2  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027AED9  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027AEE0  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0027AEE7  48 85 C9                        test rcx, rcx
0027AEEA  74 A1                           je 0x14027ae8d
0027AEEC  C1 EE 03                        shr esi, 3
0027AEEF  81 E6 FF 01 00 00               and esi, 0x1ff
0027AEF5  8B 04 B1                        mov eax, dword ptr [rcx + rsi*4]
0027AEF8  48 8D 0C B1                     lea rcx, [rcx + rsi*4]
0027AEFC  A9 FF FF FF 3F                  test eax, 0x3fffffff
0027AF01  0F 85 26 01 00 00               jne 0x14027b02d
0027AF07  85 C0                           test eax, eax
0027AF09  0F 89 0D 07 00 00               jns 0x14027b61c
0027AF0F  F6 05 F0 BB D4 00 01            test byte ptr [rip + 0xd4bbf0], 1
0027AF16  0F 85 C4 07 00 00               jne 0x14027b6e0
0027AF1C  33 FF                           xor edi, edi
0027AF1E  89 39                           mov dword ptr [rcx], edi
0027AF20  E9 E3 FC FF FF                  jmp 0x14027ac08
0027AF25  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0027AF2A  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0027AF33  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
0027AF39  24 0F                           and al, 0xf
0027AF3B  0F 85 08 01 00 00               jne 0x14027b049
0027AF41  B8 30 00 00 00                  mov eax, 0x30
0027AF46  33 FF                           xor edi, edi
0027AF48  48 8D 99 40 9C 00 00            lea rbx, [rcx + 0x9c40]
0027AF4F  48 03 D8                        add rbx, rax
0027AF52  F6 05 AD BB D4 00 01            test byte ptr [rip + 0xd4bbad], 1
0027AF59  0F 85 AB 00 00 00               jne 0x14027b00a
0027AF5F  0F 0D 0B                        prefetchw byte ptr [rbx]
0027AF62  48 8B 03                        mov rax, qword ptr [rbx]
0027AF65  48 85 C0                        test rax, rax
0027AF68  75 1A                           jne 0x14027af84
0027AF6A  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0027AF6E  48 8B C3                        mov rax, rbx
0027AF71  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
0027AF76  0F 84 8C FC FF FF               je 0x14027ac08
0027AF7C  48 8B CB                        mov rcx, rbx
0027AF7F  E8 1C CB F9 FF                  call 0x140217aa0
0027AF84  48 8D 48 08                     lea rcx, [rax + 8]
0027AF88  48 89 3B                        mov qword ptr [rbx], rdi
0027AF8B  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0027AF8F  48 8B C2                        mov rax, rdx
0027AF92  48 87 01                        xchg qword ptr [rcx], rax
0027AF95  32 C2                           xor al, dl
0027AF97  A8 04                           test al, 4
0027AF99  0F 84 69 FC FF FF               je 0x14027ac08
0027AF9F  E8 7C CC F9 FF                  call 0x140217c20
0027AFA4  E9 5F FC FF FF                  jmp 0x14027ac08
0027AFA9  49 8B C1                        mov rax, r9
0027AFAC  48 3B F0                        cmp rsi, rax
0027AFAF  0F 82 E7 FE FF FF               jb 0x14027ae9c
0027AFB5  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027AFBF  48 8B C0                        mov rax, rax
0027AFC2  48 3B F0                        cmp rsi, rax
0027AFC5  0F 87 D1 FE FF FF               ja 0x14027ae9c
0027AFCB  49 8B C1                        mov rax, r9
0027AFCE  48 2B F0                        sub rsi, rax
0027AFD1  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
0027AFD8  48 C1 FE 03                     sar rsi, 3
0027AFDC  8D 14 36                        lea edx, [rsi + rsi]
0027AFDF  8B C2                           mov eax, edx
0027AFE1  8B CA                           mov ecx, edx
0027AFE3  48 C1 E8 05                     shr rax, 5
0027AFE7  48 8D 15 52 1B BB 00            lea rdx, [rip + 0xbb1b52]
0027AFEE  83 E1 1F                        and ecx, 0x1f
0027AFF1  48 8D 14 82                     lea rdx, [rdx + rax*4]
0027AFF5  B8 03 00 00 00                  mov eax, 3
0027AFFA  D3 E0                           shl eax, cl
0027AFFC  F7 D0                           not eax
0027AFFE  F0 21 82 6C 26 00 00            lock and dword ptr [rdx + 0x266c], eax
0027B005  E9 FE FB FF FF                  jmp 0x14027ac08
0027B00A  8B 05 48 2E C9 00               mov eax, dword ptr [rip + 0xc92e48]
0027B010  85 C0                           test eax, eax
0027B012  0F 85 47 FF FF FF               jne 0x14027af5f
0027B018  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0027B020  48 8B CB                        mov rcx, rbx
0027B023  E8 C8 C9 F9 FF                  call 0x1402179f0
0027B028  E9 DB FB FF FF                  jmp 0x14027ac08
0027B02D  F6 05 D2 BA D4 00 01            test byte ptr [rip + 0xd4bad2], 1
0027B034  0F 85 07 07 00 00               jne 0x14027b741
0027B03A  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
0027B041  F0 FF 09                        lock dec dword ptr [rcx]
0027B044  E9 BF FB FF FF                  jmp 0x14027ac08
0027B049  3C 07                           cmp al, 7
0027B04B  0F 84 84 04 00 00               je 0x14027b4d5
0027B051  3C 05                           cmp al, 5
0027B053  0F 84 8A 07 00 00               je 0x14027b7e3
0027B059  B8 48 00 00 00                  mov eax, 0x48
0027B05E  E9 E3 FE FF FF                  jmp 0x14027af46
0027B063  8B 05 EF 2D C9 00               mov eax, dword ptr [rip + 0xc92def]
0027B069  85 C0                           test eax, eax
0027B06B  0F 85 34 FA FF FF               jne 0x14027aaa5
0027B071  E8 DA A7 FF FF                  call 0x140275850
0027B076  E9 6A FB FF FF                  jmp 0x14027abe5
0027B07B  80 F9 11                        cmp cl, 0x11
0027B07E  48 8B CD                        mov rcx, rbp
0027B081  0F 84 DF 00 00 00               je 0x14027b166
0027B087  E8 64 1B 00 00                  call 0x14027cbf0
0027B08C  83 27 FE                        and dword ptr [rdi], 0xfffffffe
0027B08F  E9 2A F8 FF FF                  jmp 0x14027a8be
0027B094  41 8B F7                        mov esi, r15d
0027B097  48 8B FB                        mov rdi, rbx
0027B09A  E9 BC F8 FF FF                  jmp 0x14027a95b
0027B09F  A8 02                           test al, 2
0027B0A1  0F 85 C9 01 00 00               jne 0x14027b270
0027B0A7  48 8B FB                        mov rdi, rbx
0027B0AA  48 B8 00 00 00 00 00 00 00 20   movabs rax, 0x2000000000000000
0027B0B4  48 0B F8                        or rdi, rax
0027B0B7  48 F7 05 C6 B9 D4 00 00 00 00 02  test qword ptr [rip + 0xd4b9c6], 0x2000000
0027B0C2  74 03                           je 0x14027b0c7
0027B0C4  0F AE E8                        lfence
0027B0C7  48 0F BA 25 B8 B9 D4 00 24      bt qword ptr [rip + 0xd4b9b8], 0x24
0027B0D0  0F 82 6A 05 00 00               jb 0x14027b640
0027B0D6  48 8B C3                        mov rax, rbx
0027B0D9  F0 49 0F B1 7D 00               lock cmpxchg qword ptr [r13], rdi
0027B0DF  48 8B D8                        mov rbx, rax
0027B0E2  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0027B0EC  48 0F 44 DF                     cmove rbx, rdi
0027B0F0  E9 94 FA FF FF                  jmp 0x14027ab89
0027B0F5  48 8D 0D 94 70 0F 00            lea rcx, [rip + 0xf7094]
0027B0FC  48 3B C1                        cmp rax, rcx
0027B0FF  49 8B CE                        mov rcx, r14
0027B102  0F 85 92 01 00 00               jne 0x14027b29a
0027B108  E8 83 70 0F 00                  call 0x140372190
0027B10D  8B F0                           mov esi, eax
0027B10F  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0027B116  E9 07 F3 FF FF                  jmp 0x14027a422
0027B11B  48 8D 0D DE DA 1A 00            lea rcx, [rip + 0x1adade]
0027B122  48 3B C1                        cmp rax, rcx
0027B125  0F 85 D5 05 00 00               jne 0x14027b700
0027B12B  49 8B 96 B8 00 00 00            mov rdx, qword ptr [r14 + 0xb8]
0027B132  48 8D 05 17 1E 22 00            lea rax, [rip + 0x221e17]
0027B139  48 83 C2 30                     add rdx, 0x30
0027B13D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027B142  45 33 C9                        xor r9d, r9d
0027B145  45 33 C0                        xor r8d, r8d
0027B148  49 8B CE                        mov rcx, r14
0027B14B  E8 40 ED FB FF                  call 0x140239e90
0027B150  41 8B F7                        mov esi, r15d
0027B153  E9 FF F7 FF FF                  jmp 0x14027a957
0027B158  83 FE 04                        cmp esi, 4
0027B15B  0F 85 8E F7 FF FF               jne 0x14027a8ef
0027B161  E9 3B F8 FF FF                  jmp 0x14027a9a1
0027B166  E8 09 E4 FB FF                  call 0x140239574
0027B16B  83 27 FE                        and dword ptr [rdi], 0xfffffffe
0027B16E  E9 4B F7 FF FF                  jmp 0x14027a8be
0027B173  E8 28 87 0A 00                  call 0x1403238a0
0027B178  E9 4F F8 FF FF                  jmp 0x14027a9cc
0027B17D  0F 1F 00                        nop dword ptr [rax]
0027B180  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
0027B183  8B CA                           mov ecx, edx
0027B185  83 E1 70                        and ecx, 0x70
0027B188  80 F9 30                        cmp cl, 0x30
0027B18B  74 30                           je 0x14027b1bd
0027B18D  8B CA                           mov ecx, edx
0027B18F  80 E1 70                        and cl, 0x70
0027B192  80 F9 10                        cmp cl, 0x10
0027B195  74 26                           je 0x14027b1bd
0027B197  0F BA E2 15                     bt edx, 0x15
0027B19B  73 14                           jae 0x14027b1b1
0027B19D  0F BA E2 17                     bt edx, 0x17
0027B1A1  72 1A                           jb 0x14027b1bd
0027B1A3  8B C2                           mov eax, edx
0027B1A5  25 00 00 18 00                  and eax, 0x180000
0027B1AA  3D 00 00 10 00                  cmp eax, 0x100000
0027B1AF  73 0C                           jae 0x14027b1bd
0027B1B1  83 E2 70                        and edx, 0x70
0027B1B4  80 FA 50                        cmp dl, 0x50
0027B1B7  0F 85 D9 E9 FF FF               jne 0x140279b96
0027B1BD  0F B6 7E 21                     movzx edi, byte ptr [rsi + 0x21]
0027B1C1  FF C5                           inc ebp
0027B1C3  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
0027B1C6  48 C1 E7 20                     shl rdi, 0x20
0027B1CA  48 0B F8                        or rdi, rax
0027B1CD  48 C1 E7 0C                     shl rdi, 0xc
0027B1D1  48 81 CF FF 0F 00 00            or rdi, 0xfff
0027B1D8  40 84 ED                        test bpl, bpl
0027B1DB  75 13                           jne 0x14027b1f0
0027B1DD  49 8B D5                        mov rdx, r13
0027B1E0  49 8B CE                        mov rcx, r14
0027B1E3  E8 68 E0 FF FF                  call 0x140279250
0027B1E8  85 C0                           test eax, eax
0027B1EA  0F 85 A6 E9 FF FF               jne 0x140279b96
0027B1F0  48 8B CE                        mov rcx, rsi
0027B1F3  E8 2C C0 01 00                  call 0x140297224
0027B1F8  48 8B F0                        mov rsi, rax
0027B1FB  48 85 C0                        test rax, rax
0027B1FE  75 80                           jne 0x14027b180
0027B200  E9 91 E9 FF FF                  jmp 0x140279b96
0027B205  B9 01 00 00 00                  mov ecx, 1
0027B20A  E9 6F FB FF FF                  jmp 0x14027ad7e
0027B20F  4D 8B 46 38                     mov r8, qword ptr [r14 + 0x38]
0027B213  4D 85 C0                        test r8, r8
0027B216  0F 84 14 E7 FF FF               je 0x140279930
0027B21C  83 C8 02                        or eax, 2
0027B21F  89 01                           mov dword ptr [rcx], eax
0027B221  0F BA E2 0C                     bt edx, 0xc
0027B225  0F 83 CC 03 00 00               jae 0x14027b5f7
0027B22B  48 8B C7                        mov rax, rdi
0027B22E  4C 3B C0                        cmp r8, rax
0027B231  0F 85 C0 03 00 00               jne 0x14027b5f7
0027B237  4D 89 7E 38                     mov qword ptr [r14 + 0x38], r15
0027B23B  E9 F0 E6 FF FF                  jmp 0x140279930
0027B240  41 0F 0D 08                     prefetchw byte ptr [r8]
0027B244  41 8B 00                        mov eax, dword ptr [r8]
0027B247  8B D0                           mov edx, eax
0027B249  0F BA F2 15                     btr edx, 0x15
0027B24D  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0027B252  75 F3                           jne 0x14027b247
0027B254  0F BA E0 15                     bt eax, 0x15
0027B258  0F 83 6B F4 FF FF               jae 0x14027a6c9
0027B25E  E8 6D 7F FE FF                  call 0x1402631d0
0027B263  E9 61 F4 FF FF                  jmp 0x14027a6c9
0027B268  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0027B270  FF C5                           inc ebp
0027B272  85 2D 34 A0 D4 00               test dword ptr [rip + 0xd4a034], ebp
0027B278  0F 84 30 02 00 00               je 0x14027b4ae
0027B27E  F3 90                           pause
0027B280  49 8B 5D 00                     mov rbx, qword ptr [r13]
0027B284  48 0F BA E3 3C                  bt rbx, 0x3c
0027B289  72 E5                           jb 0x14027b270
0027B28B  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0027B295  E9 EF F8 FF FF                  jmp 0x14027ab89
0027B29A  E8 31 F8 43 00                  call 0x1406baad0
0027B29F  8B F0                           mov esi, eax
0027B2A1  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0027B2A8  E9 75 F1 FF FF                  jmp 0x14027a422
0027B2AD  48 8D 05 8C 1A 23 00            lea rax, [rip + 0x231a8c]
0027B2B4  49 39 86 A8 00 00 00            cmp qword ptr [r14 + 0xa8], rax
0027B2BB  0F 84 19 E6 FF FF               je 0x1402798da
0027B2C1  45 8B CF                        mov r9d, r15d
0027B2C4  E9 17 E6 FF FF                  jmp 0x1402798e0
0027B2C9  B8 18 00 00 00                  mov eax, 0x18
0027B2CE  48 8B 84 08 40 9C 00 00         mov rax, qword ptr [rax + rcx + 0x9c40]
0027B2D6  48 85 C0                        test rax, rax
0027B2D9  E9 87 EC FF FF                  jmp 0x140279f65
0027B2DE  48 3B D0                        cmp rdx, rax
0027B2E1  0F 84 8A 00 00 00               je 0x14027b371
0027B2E7  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
0027B2ED  A8 0F                           test al, 0xf
0027B2EF  74 2B                           je 0x14027b31c
0027B2F1  48 B9 FF DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedfff
0027B2FB  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
0027B301  A8 0F                           test al, 0xf
0027B303  0F 85 98 00 00 00               jne 0x14027b3a1
0027B309  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
0027B313  F0 48 21 02                     lock and qword ptr [rdx], rax
0027B317  E9 6E F6 FF FF                  jmp 0x14027a98a
0027B31C  49 8B C4                        mov rax, r12
0027B31F  48 B9 FF DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedfff
0027B329  48 3B D0                        cmp rdx, rax
0027B32C  72 CD                           jb 0x14027b2fb
0027B32E  48 8B C1                        mov rax, rcx
0027B331  48 3B D0                        cmp rdx, rax
0027B334  77 C5                           ja 0x14027b2fb
0027B336  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027B33F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027B346  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027B34D  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0027B354  48 85 C9                        test rcx, rcx
0027B357  74 98                           je 0x14027b2f1
0027B359  48 C1 EA 03                     shr rdx, 3
0027B35D  81 E2 FF 01 00 00               and edx, 0x1ff
0027B363  48 8D 0C 91                     lea rcx, [rcx + rdx*4]
0027B367  E8 C4 EF FB FF                  call 0x14023a330
0027B36C  E9 19 F6 FF FF                  jmp 0x14027a98a
0027B371  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0027B37A  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
0027B380  24 0F                           and al, 0xf
0027B382  0F 85 8F 00 00 00               jne 0x14027b417
0027B388  BA 30 00 00 00                  mov edx, 0x30
0027B38D  48 81 C1 40 9C 00 00            add rcx, 0x9c40
0027B394  48 03 CA                        add rcx, rdx
0027B397  E8 14 BE F9 FF                  call 0x1402171b0
0027B39C  E9 E9 F5 FF FF                  jmp 0x14027a98a
0027B3A1  49 8B C4                        mov rax, r12
0027B3A4  48 3B D0                        cmp rdx, rax
0027B3A7  0F 82 5C FF FF FF               jb 0x14027b309
0027B3AD  48 8B C1                        mov rax, rcx
0027B3B0  48 3B D0                        cmp rdx, rax
0027B3B3  0F 87 50 FF FF FF               ja 0x14027b309
0027B3B9  49 8B C4                        mov rax, r12
0027B3BC  48 2B D0                        sub rdx, rax
0027B3BF  41 B8 02 00 00 00               mov r8d, 2
0027B3C5  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
0027B3CB  48 C1 FA 03                     sar rdx, 3
0027B3CF  03 D2                           add edx, edx
0027B3D1  8B CA                           mov ecx, edx
0027B3D3  8B C2                           mov eax, edx
0027B3D5  83 E1 1F                        and ecx, 0x1f
0027B3D8  41 D3 E0                        shl r8d, cl
0027B3DB  41 F7 D0                        not r8d
0027B3DE  41 0F B3 C8                     btr r8d, ecx
0027B3E2  48 C1 E8 05                     shr rax, 5
0027B3E6  48 8D 0D 53 17 BB 00            lea rcx, [rip + 0xbb1753]
0027B3ED  F0 44 21 84 81 6C 26 00 00      lock and dword ptr [rcx + rax*4 + 0x266c], r8d
0027B3F6  E9 8F F5 FF FF                  jmp 0x14027a98a
0027B3FB  48 8D 05 3E 19 23 00            lea rax, [rip + 0x23193e]
0027B402  49 39 86 A8 00 00 00            cmp qword ptr [r14 + 0xa8], rax
0027B409  0F 84 09 EA FF FF               je 0x140279e18
0027B40F  45 8B CF                        mov r9d, r15d
0027B412  E9 07 EA FF FF                  jmp 0x140279e1e
0027B417  3C 07                           cmp al, 7
0027B419  0F 84 05 01 00 00               je 0x14027b524
0027B41F  3C 05                           cmp al, 5
0027B421  BA 48 00 00 00                  mov edx, 0x48
0027B426  49 0F 44 D7                     cmove rdx, r15
0027B42A  E9 5E FF FF FF                  jmp 0x14027b38d
0027B42F  4D 89 7E 50                     mov qword ptr [r14 + 0x50], r15
0027B433  E9 88 E3 FF FF                  jmp 0x1402797c0
0027B438  45 8B E7                        mov r12d, r15d
0027B43B  49 8B C1                        mov rax, r9
0027B43E  49 8B CD                        mov rcx, r13
0027B441  BD 01 00 00 00                  mov ebp, 1
0027B446  48 2B C8                        sub rcx, rax
0027B449  BF 02 00 00 00                  mov edi, 2
0027B44E  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
0027B455  48 C1 F9 03                     sar rcx, 3
0027B459  03 C9                           add ecx, ecx
0027B45B  44 8B F9                        mov r15d, ecx
0027B45E  8B D9                           mov ebx, ecx
0027B460  49 C1 EF 05                     shr r15, 5
0027B464  48 8D 0D D5 16 BB 00            lea rcx, [rip + 0xbb16d5]
0027B46B  48 8D 89 6C 26 00 00            lea rcx, [rcx + 0x266c]
0027B472  83 E3 1F                        and ebx, 0x1f
0027B475  46 8B 04 B9                     mov r8d, dword ptr [rcx + r15*4]
0027B479  4E 8D 3C B9                     lea r15, [rcx + r15*4]
0027B47D  8B CB                           mov ecx, ebx
0027B47F  D3 E5                           shl ebp, cl
0027B481  D3 E7                           shl edi, cl
0027B483  F7 D7                           not edi
0027B485  8B CB                           mov ecx, ebx
0027B487  41 8B C0                        mov eax, r8d
0027B48A  D3 E8                           shr eax, cl
0027B48C  A8 01                           test al, 1
0027B48E  0F 85 C6 00 00 00               jne 0x14027b55a
0027B494  8B CD                           mov ecx, ebp
0027B496  41 8B C0                        mov eax, r8d
0027B499  41 0B C8                        or ecx, r8d
0027B49C  23 CF                           and ecx, edi
0027B49E  F0 41 0F B1 0F                  lock cmpxchg dword ptr [r15], ecx
0027B4A3  44 8B C0                        mov r8d, eax
0027B4A6  0F 84 32 F7 FF FF               je 0x14027abde
0027B4AC  EB D7                           jmp 0x14027b485
0027B4AE  8B 05 04 B6 D4 00               mov eax, dword ptr [rip + 0xd4b604]
0027B4B4  A8 40                           test al, 0x40
0027B4B6  0F 84 C2 FD FF FF               je 0x14027b27e
0027B4BC  E8 CF 3F 09 00                  call 0x14030f490
0027B4C1  84 C0                           test al, al
0027B4C3  0F 84 B5 FD FF FF               je 0x14027b27e
0027B4C9  8B CD                           mov ecx, ebp
0027B4CB  E8 90 3F 09 00                  call 0x14030f460
0027B4D0  E9 AB FD FF FF                  jmp 0x14027b280
0027B4D5  B8 18 00 00 00                  mov eax, 0x18
0027B4DA  E9 67 FA FF FF                  jmp 0x14027af46
0027B4DF  41 8B 06                        mov eax, dword ptr [r14]
0027B4E2  A8 04                           test al, 4
0027B4E4  0F 84 F8 EE FF FF               je 0x14027a3e2
0027B4EA  44 8B C5                        mov r8d, ebp
0027B4ED  49 8B D5                        mov rdx, r13
0027B4F0  49 8B CE                        mov rcx, r14
0027B4F3  E8 58 E1 FB FF                  call 0x140239650
0027B4F8  85 C0                           test eax, eax
0027B4FA  0F 84 E2 EE FF FF               je 0x14027a3e2
0027B500  45 33 FF                        xor r15d, r15d
0027B503  83 F8 02                        cmp eax, 2
0027B506  41 8B F7                        mov esi, r15d
0027B509  0F 45 F0                        cmovne esi, eax
0027B50C  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
0027B513  E9 B6 F8 FF FF                  jmp 0x14027adce
0027B518  4D 8D 81 C0 00 00 00            lea r8, [r9 + 0xc0]
0027B51F  E9 05 E3 FF FF                  jmp 0x140279829
0027B524  BA 18 00 00 00                  mov edx, 0x18
0027B529  48 81 C1 40 9C 00 00            add rcx, 0x9c40
0027B530  48 03 CA                        add rcx, rdx
0027B533  E8 78 BC F9 FF                  call 0x1402171b0
0027B538  E9 4D F4 FF FF                  jmp 0x14027a98a
0027B53D  48 FF C3                        inc rbx
0027B540  48 83 C7 08                     add rdi, 8
0027B544  45 33 C9                        xor r9d, r9d
0027B547  E9 06 EC FF FF                  jmp 0x14027a152
0027B54C  48 81 C5 80 DF 00 00            add rbp, 0xdf80
0027B553  FF C0                           inc eax
0027B555  E9 EA EB FF FF                  jmp 0x14027a144
0027B55A  A8 02                           test al, 2
0027B55C  0F 85 BE 01 00 00               jne 0x14027b720
0027B562  BA 02 00 00 00                  mov edx, 2
0027B567  41 8B C0                        mov eax, r8d
0027B56A  D3 E2                           shl edx, cl
0027B56C  41 0B D0                        or edx, r8d
0027B56F  F0 41 0F B1 17                  lock cmpxchg dword ptr [r15], edx
0027B574  44 8B C0                        mov r8d, eax
0027B577  44 0F 44 C2                     cmove r8d, edx
0027B57B  E9 05 FF FF FF                  jmp 0x14027b485
0027B580  48 8D 05 B9 17 23 00            lea rax, [rip + 0x2317b9]
0027B587  49 8D 5E 04                     lea rbx, [r14 + 4]
0027B58B  49 39 86 A8 00 00 00            cmp qword ptr [r14 + 0xa8], rax
0027B592  0F 84 DB F2 FF FF               je 0x14027a873
0027B598  41 8B C7                        mov eax, r15d
0027B59B  E9 D8 F2 FF FF                  jmp 0x14027a878
0027B5A0  48 8D 05 49 89 1F 00            lea rax, [rip + 0x1f8949]
0027B5A7  48 3B D0                        cmp rdx, rax
0027B5AA  0F 85 B1 01 00 00               jne 0x14027b761
0027B5B0  E8 3B 89 1F 00                  call 0x140473ef0
0027B5B5  8B D8                           mov ebx, eax
0027B5B7  E9 4E E3 FF FF                  jmp 0x14027990a
0027B5BC  48 8D 0D 2D 89 1F 00            lea rcx, [rip + 0x1f892d]
0027B5C3  48 3B C1                        cmp rax, rcx
0027B5C6  49 8B CE                        mov rcx, r14
0027B5C9  0F 85 9F 01 00 00               jne 0x14027b76e
0027B5CF  E8 1C 89 1F 00                  call 0x140473ef0
0027B5D4  8B C8                           mov ecx, eax
0027B5D6  E9 6D E8 FF FF                  jmp 0x140279e48
0027B5DB  48 8D 05 5E 17 23 00            lea rax, [rip + 0x23175e]
0027B5E2  49 39 86 A8 00 00 00            cmp qword ptr [r14 + 0xa8], rax
0027B5E9  0F 84 36 F3 FF FF               je 0x14027a925
0027B5EF  41 8B C7                        mov eax, r15d
0027B5F2  E9 33 F3 FF FF                  jmp 0x14027a92a
0027B5F7  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0027B5FB  49 8B D0                        mov rdx, r8
0027B5FE  E8 BD B8 F9 FF                  call 0x140216ec0
0027B603  E9 2F FC FF FF                  jmp 0x14027b237
0027B608  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
0027B60F  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0027B614  4C 63 D5                        movsxd r10, ebp
0027B617  E9 2F E3 FF FF                  jmp 0x14027994b
0027B61C  33 FF                           xor edi, edi
0027B61E  48 8B D1                        mov rdx, rcx
0027B621  45 33 C9                        xor r9d, r9d
0027B624  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0027B629  41 B8 00 01 00 00               mov r8d, 0x100
0027B62F  8D 4F 10                        lea ecx, [rdi + 0x10]
0027B632  E8 29 20 28 00                  call 0x1404fd660
0027B637  CC                              int3
0027B638  4C 63 D5                        movsxd r10, ebp
0027B63B  E9 02 F7 FF FF                  jmp 0x14027ad42
0027B640  40 0F B6 C7                     movzx eax, dil
0027B644  24 21                           and al, 0x21
0027B646  3C 01                           cmp al, 1
0027B648  0F 85 88 FA FF FF               jne 0x14027b0d6
0027B64E  48 8B C2                        mov rax, rdx
0027B651  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
0027B65B  48 03 C1                        add rax, rcx
0027B65E  4C 3B E8                        cmp r13, rax
0027B661  0F 82 6F FA FF FF               jb 0x14027b0d6
0027B667  41 B8 80 00 00 00               mov r8d, 0x80
0027B66D  48 8B D7                        mov rdx, rdi
0027B670  49 8B CD                        mov rcx, r13
0027B673  E8 08 77 01 00                  call 0x140292d80
0027B678  E9 59 FA FF FF                  jmp 0x14027b0d6
0027B67D  48 8D 0D 6C 88 1F 00            lea rcx, [rip + 0x1f886c]
0027B684  48 3B C1                        cmp rax, rcx
0027B687  49 8B CE                        mov rcx, r14
0027B68A  0F 85 EA 00 00 00               jne 0x14027b77a
0027B690  E8 5B 88 1F 00                  call 0x140473ef0
0027B695  44 8B F8                        mov r15d, eax
0027B698  E9 03 F2 FF FF                  jmp 0x14027a8a0
0027B69D  41 8B C5                        mov eax, r13d
0027B6A0  C1 E8 03                        shr eax, 3
0027B6A3  25 FF 01 00 00                  and eax, 0x1ff
0027B6A8  48 8D 0C 81                     lea rcx, [rcx + rax*4]
0027B6AC  E8 CF D7 FC FF                  call 0x140248e80
0027B6B1  E9 2F F5 FF FF                  jmp 0x14027abe5
0027B6B6  8B AC 24 E0 00 00 00            mov ebp, dword ptr [rsp + 0xe0]
0027B6BD  41 BD 05 00 00 00               mov r13d, 5
0027B6C3  41 8B F5                        mov esi, r13d
0027B6C6  44 89 AC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r13d
0027B6CE  45 33 FF                        xor r15d, r15d
0027B6D1  49 BC 00 D0 BE 7D FB F6 FF FF   movabs r12, 0xfffff6fb7dbed000
0027B6DB  E9 47 F1 FF FF                  jmp 0x14027a827
0027B6E0  8B 05 72 27 C9 00               mov eax, dword ptr [rip + 0xc92772]
0027B6E6  85 C0                           test eax, eax
0027B6E8  0F 85 2E F8 FF FF               jne 0x14027af1c
0027B6EE  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0027B6F6  E8 49 58 04 00                  call 0x1402c0f44
0027B6FB  E9 08 F5 FF FF                  jmp 0x14027ac08
0027B700  48 8D 0D E9 87 1F 00            lea rcx, [rip + 0x1f87e9]
0027B707  48 3B C1                        cmp rax, rcx
0027B70A  49 8B CE                        mov rcx, r14
0027B70D  0F 85 8E 00 00 00               jne 0x14027b7a1
0027B713  E8 D8 87 1F 00                  call 0x140473ef0
0027B718  8B F0                           mov esi, eax
0027B71A  E9 38 F2 FF FF                  jmp 0x14027a957
0027B71F  90                              nop
0027B720  41 FF C4                        inc r12d
0027B723  44 85 25 82 9B D4 00            test dword ptr [rip + 0xd49b82], r12d
0027B72A  74 58                           je 0x14027b784
0027B72C  F3 90                           pause
0027B72E  45 8B 07                        mov r8d, dword ptr [r15]
0027B731  8B CB                           mov ecx, ebx
0027B733  41 8B C0                        mov eax, r8d
0027B736  D3 E8                           shr eax, cl
0027B738  A8 01                           test al, 1
0027B73A  75 E4                           jne 0x14027b720
0027B73C  E9 44 FD FF FF                  jmp 0x14027b485
0027B741  8B 05 11 27 C9 00               mov eax, dword ptr [rip + 0xc92711]
0027B747  85 C0                           test eax, eax
0027B749  0F 85 EB F8 FF FF               jne 0x14027b03a
0027B74F  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0027B757  E8 EC 57 07 00                  call 0x1402f0f48
0027B75C  E9 A7 F4 FF FF                  jmp 0x14027ac08
0027B761  48 8B C2                        mov rax, rdx
0027B764  E8 67 F3 43 00                  call 0x1406baad0
0027B769  E9 47 FE FF FF                  jmp 0x14027b5b5
0027B76E  E8 5D F3 43 00                  call 0x1406baad0
0027B773  8B C8                           mov ecx, eax
0027B775  E9 CE E6 FF FF                  jmp 0x140279e48
0027B77A  E8 51 F3 43 00                  call 0x1406baad0
0027B77F  E9 11 FF FF FF                  jmp 0x14027b695
0027B784  8B 05 2E B3 D4 00               mov eax, dword ptr [rip + 0xd4b32e]
0027B78A  A8 40                           test al, 0x40
0027B78C  74 9E                           je 0x14027b72c
0027B78E  E8 FD 3C 09 00                  call 0x14030f490
0027B793  84 C0                           test al, al
0027B795  74 95                           je 0x14027b72c
0027B797  41 8B CC                        mov ecx, r12d
0027B79A  E8 C1 3C 09 00                  call 0x14030f460
0027B79F  EB 8D                           jmp 0x14027b72e
0027B7A1  E8 2A F3 43 00                  call 0x1406baad0
0027B7A6  E9 6D FF FF FF                  jmp 0x14027b718
0027B7AB  85 ED                           test ebp, ebp
0027B7AD  45 8B CF                        mov r9d, r15d
0027B7B0  44 8B C5                        mov r8d, ebp
0027B7B3  49 8B D5                        mov rdx, r13
0027B7B6  41 0F 95 C1                     setne r9b
0027B7BA  49 8B CE                        mov rcx, r14
0027B7BD  41 83 C1 02                     add r9d, 2
0027B7C1  E8 2A AE 1B 00                  call 0x1404365f0
0027B7C6  E9 56 F0 FF FF                  jmp 0x14027a821
0027B7CB  49 8B C7                        mov rax, r15
0027B7CE  E9 DA EC FF FF                  jmp 0x14027a4ad
0027B7D3  41 8B C7                        mov eax, r15d
0027B7D6  E9 88 E7 FF FF                  jmp 0x140279f63
0027B7DB  41 8B CF                        mov ecx, r15d
0027B7DE  E9 9B F5 FF FF                  jmp 0x14027ad7e
0027B7E3  33 FF                           xor edi, edi
0027B7E5  8B C7                           mov eax, edi
0027B7E7  E9 5C F7 FF FF                  jmp 0x14027af48
0027B7EC  8B AC 24 E0 00 00 00            mov ebp, dword ptr [rsp + 0xe0]
0027B7F3  E9 87 EC FF FF                  jmp 0x14027a47f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWalkPageTablesRecursively(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pE0;
    unsigned int v_stack_pE8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    v_r15 = 0;
    v_stack_m88 = *(unsigned __int64 *)(a1 + 32);
    v_stack_m70 = *(unsigned __int64 *)(a1 + 168);
    v_stack_m78 = (int)(a3);
    v_stack_m90 = a1 + 96 + (int)(a3) * 8;
    if (a2 < (*(unsigned __int64 *)(a1 + 96 + (int)(a3) * 8))) { a2 = *(unsigned __int64 *)(a1 + 96 + (int)(a3) * 8); }
    v_r11 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    v_r11 = (v_r11) + (0xFF8ULL);
    v_stack_m80 = a1 + 128 + (int)(a3) * 8;
    v_stack_p20 = 0;
    if (v_r11 > (*(unsigned __int64 *)(a1 + 128 + (int)(a3) * 8))) { v_r11 = *(unsigned __int64 *)(a1 + 128 + (int)(a3) * 8); }
    v_stack_m98 = v_r11;
loc_00279769:
    v_stack_p10 = 0;
loc_00279774:
loc_0027977E:
loc_00279788:
    if (a2 > v_r11) goto loc_0027A821;
    if (0 != 0) goto loc_0027A248;
loc_00279799:
    v_r12 = ((unsigned int)((int)(a3)) != 0) ? 1 : 0;
    v_r12 = (unsigned int)((v_r12) + (2));
    if (*(unsigned __int64 *)(a1 + 72) != 0) goto loc_00279973;
loc_002797B3:
    if (*(unsigned __int64 *)(a1 + 80) != 0) goto loc_0027A2E1;
loc_002797C0:
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 160))) & (15)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (8)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0027A10D;
loc_002797E6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_00279A1B;
    if (((*(unsigned __int8 *)(a1 + 8)) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 160)))) != 0) goto loc_00279A1B;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (4));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (((unsigned __int8)(result)) > 5) goto loc_00279EA2;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0027B518;
loc_00279829:
    if ((unsigned int)(a2) == 0) goto loc_00279E82;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_00279DCC;
loc_00279853:
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324))) << (6);
    if (condition_is_above_or_equal) goto loc_00279EA2;
loc_00279865:
loc_0027986F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (28)) != 0) goto loc_002798A2;
    if ((unsigned int)((int)(a3)) == 0) goto loc_002798A2;
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))));
    if (((unsigned int)(v_r12)) != 3) {
        result = (unsigned __int8)((int)(a3));
        a1 = a1 + 4;
        result = (unsigned int)((result) << (2));
        result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
        *(unsigned __int64 *)(a1 + 72) = a2;
        result = (unsigned int)((result) & (28));
        result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    }
    result = (unsigned int)((result) | (32));
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if (*(unsigned __int64 *)(a1 + 176) == 0) goto loc_0027A4BD;
    if ((*(unsigned __int64 *)(a1 + 176)) != (v_rip + 1766480)) goto loc_0027A56C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184))))) & (3)) == 0) goto loc_0027B2AD;
loc_002798DA:
loc_002798E0:
    a3 = 0;
    v_stack_mA8 = v_rip + 2180377;
    result = MiAgeTrimListsTail(a1, *(unsigned __int64 *)(a1 + 184) + 56, a3, 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 184) + 6) = 1;
    }
loc_0027990A:
loc_0027990E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (1)) != 0) goto loc_00279930;
    if (0 >= 4) goto loc_00279935;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_0027B20F;
    result = MiReleaseWalkLocks(a1, (unsigned int)(*(unsigned int *)(a1)), a3, 1);
loc_00279930:
    if (0 >= 4) {
        v_stack_p10 = 0;
    }
loc_0027994B:
    v_stack_p20 = 1;
loc_0027995E:
    goto loc_00279774;
loc_00279973:
    if (a2 < 1) goto loc_002799B2;
loc_00279988:
    if (a2 > v_stack_m90) goto loc_002799AA;
    a2 = (a2) << (25);
    a1 = (1) << (25);
    a2 = (a2) - (a1);
    a2 = (a2) >> (16);
    if (a2 >= 1) goto loc_00279988;
loc_002799AA:
loc_002799B2:
    if (result < 1) goto loc_002799EE;
loc_002799C4:
    if (result > (a1 + (int)((unsigned int)((int)(a3))) + 12 * 8)) goto loc_002799E6;
    result = (result) << (25);
    a1 = (1) << (25);
    result = (result) - (a1);
    result = (result) >> (16);
    if (result >= 1) goto loc_002799C4;
loc_002799E6:
loc_002799EE:
    if (a2 > result) goto loc_0027A23A;
    if ((*(unsigned __int64 *)(a1 + 72)) != a2) goto loc_0027A196;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (0xFFFFFFE3ULL));
    *(unsigned __int64 *)(a1 + 72) = 0;
    *(unsigned int *)(a1 + 4) = (unsigned int)(a2);
    goto loc_002797B3;
loc_00279A1B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (32)) != 0) goto loc_00279DC2;
    result = MiComputePxeWalkAction(a1, a2, (unsigned int)((unsigned int)((int)(a3))), 2);
loc_00279A37:
    if (((unsigned int)(result)) == 4) goto loc_0027A2C3;
    if ((unsigned int)(result) == 0) goto loc_0027A3B7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (1)) != 0) goto loc_0027B608;
    if (((unsigned int)((int)(a3))) >= 1) goto loc_00279D74;
loc_00279A65:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 1) goto loc_00279CCC;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 2) goto loc_00279DD4;
    if ((unsigned int)((int)(a3)) != 0) goto loc_0027A3E2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) != 0) goto loc_0027A3E2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_0027A3E2;
    a3 = (a2) << (25);
    result = (2) << (25);
    a3 = (a3) - (result);
    a3 = (a3) >> (16);
    a3 = (a3) & (result);
    a3 = (a3) >> (9);
    a3 = (a3) + (2);
    if (a3 < a1) goto loc_00279B0B;
    if (a3 > a1) goto loc_00279B0B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_00279B0B;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_0027A503;
loc_00279B0B:
    result = (*(unsigned __int64 *)(a3)) >> (56);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) != 10) goto loc_0027A3D2;
loc_00279B19:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) != 0) goto loc_0027A47F;
    if (a2 < 2) goto loc_00279B6A;
    a1 = (2) << (25);
loc_00279B47:
    if (a2 > a1) goto loc_00279B62;
    v_rbx = (a2) << (25);
    v_rbx = (v_rbx) - (a1);
    v_rbx = (v_rbx) >> (16);
    if (v_rbx >= 2) goto loc_00279B47;
loc_00279B62:
loc_00279B6A:
    result = MiGetLeafVa(a2, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 4)));
    result = MiLockVadTree(1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 4)));
    result = MiLocateAddress(result, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 4)));
    if (result != 0) goto loc_0027B180;
loc_00279B96:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 4)));
    if (v_rbx == result) goto loc_0027B7EC;
    v_rdi = (result) >> (9);
    a1 = (a1) & (v_rdi);
    a1 = (a1) + (2);
    a1 = (a1) ^ (a2);
    if (((v_stack_m80) & (a1)) == 0) goto loc_0027A488;
    if ((a1 + 8) < 2) goto loc_00279C35;
    a2 = (2) << (25);
loc_00279C17:
    if ((a1 + 8) > 0) goto loc_00279C32;
    a1 = (a1 + 8) << (25);
    a1 = (a1) - (a2);
    a1 = (a1) >> (16);
    if (a1 >= 2) goto loc_00279C17;
loc_00279C32:
    v_r15 = 0;
loc_00279C35:
    v_r13 = (a2) & (-8);
    *(unsigned __int64 *)(v_stack_p8 + 80) = a1;
    v_r13 = (v_r13) | (0xFF8ULL);
    v_r13 = (v_r13) + (8);
loc_00279C48:
    *(unsigned __int64 *)(v_stack_m90) = v_r13;
    if (v_stack_m78 == 0) goto loc_00279C7F;
    a2 = (2) << (25);
loc_00279C67:
    v_r13 = (v_r13) << (25);
    v_r13 = (v_r13) - (a2);
    v_r13 = (v_r13) >> (16);
    *(unsigned __int64 *)(v_stack_m90 - 8) = v_r13;
    result = (v_stack_m78) - (1);
    if (condition_is_not_equal) goto loc_00279C67;
loc_00279C7F:
    *(unsigned int *)(v_stack_p8 + 12) = 0;
    v_rsi = (unsigned int)(v_stack_p10);
    if ((a1 + 8) > (*(unsigned __int64 *)(v_stack_m80))) { v_rsi = 4; }
    v_stack_p10 = (unsigned int)(v_rsi);
    goto loc_0027994B;
loc_00279CAE:
    if (((4) & (1)) != 0) goto loc_0027A3F6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m88 + 184)))) & (15)) == 0) goto loc_0027A3F6;
loc_00279CC9:
    v_r15 = 0;
loc_00279CCC:
    v_stack_p10 = 0;
loc_00279CD7:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 12))) + 1);
    *(unsigned __int64 *)(v_stack_m90) = *(unsigned __int64 *)(v_stack_m90) + result * 8;
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_00279D23;
    a3 = (result) << (25);
loc_00279D0B:
    result = (*(unsigned __int64 *)(v_stack_m90) + result * 8) << (25);
    result = (result) - (a3);
    result = (result) >> (16);
    *(unsigned __int64 *)(v_stack_m90 - 8) = result;
    a1 = ((int)((unsigned int)((unsigned int)(v_stack_p18)))) - (1);
    if (condition_is_not_equal) goto loc_00279D0B;
loc_00279D23:
    *(unsigned int *)(v_stack_p8 + 12) = 0;
loc_00279D27:
loc_00279D2E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (1)) != 0) goto loc_0027994B;
    if (0 < 4) goto loc_00279788;
    goto loc_0027994B;
loc_00279D74:
    if (((unsigned int)((int)((unsigned int)((unsigned int)(v_stack_p18))))) == 3) goto loc_00279A65;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m80)))) >> (2));
    v_r11 = (unsigned int)((v_r11) & (7));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m80))) & (28)) == 0) goto loc_00279A65;
    result = MiWalkGetResumptionPxe(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), 1 + 1, *(unsigned __int64 *)(v_stack_m80));
    if (result != (*(unsigned __int64 *)(v_stack_m90) + result * 8)) goto loc_00279A65;
    if (((unsigned int)(v_r11 - 1)) >= ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_00279A65;
    v_rbx = (unsigned int)((1) & (0xFFFFFFE3ULL));
    *(unsigned __int64 *)(v_stack_p8 + 72) = 0;
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(v_rbx);
    goto loc_00279A65;
loc_00279DC2:
    result = MiGetNextPageTablePte(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), 1 + 1, *(unsigned __int64 *)(v_stack_m80));
    goto loc_00279A37;
loc_00279DCC:
    goto loc_00279853;
loc_00279DD4:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (6));
    result = (unsigned int)((result) & (7));
    if (((unsigned int)((unsigned int)(v_stack_p18))) <= ((unsigned int)(result))) goto loc_0027A3E2;
    v_rbx = (unsigned int)((v_rbx) | (32));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(v_rbx);
    if (*(unsigned __int64 *)(v_stack_p8 + 176) == 0) goto loc_00279E45;
    if ((*(unsigned __int64 *)(v_stack_p8 + 176)) != (v_rip + 1765138)) goto loc_0027A6E6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 184))))) & (3)) == 0) goto loc_0027B3FB;
loc_00279E18:
loc_00279E1E:
    a3 = 0;
    v_stack_mA8 = v_rip + 2179035;
    result = MiAgeTrimListsTail(v_stack_p8, *(unsigned __int64 *)(v_stack_p8 + 184) + 56, a3, 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (32)) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 184) + 6) = 1;
    }
loc_00279E48:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) & (0xFFFFFFDFULL));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(result);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0027A0F0;
    if (0 < 4) goto loc_0027AA0E;
loc_00279E64:
    v_rbx = (unsigned int)(v_stack_p10);
    if (0 == 5) { v_rbx = 5; }
    v_stack_p10 = (unsigned int)(v_rbx);
    goto loc_0027A0F9;
loc_00279E82:
loc_00279E85:
    if (0 >= 4) goto loc_00279EA2;
    result = (0) << (6);
    if (condition_is_below) goto loc_00279865;
    a2 = (unsigned int)((0) + 1);
    goto loc_00279E85;
loc_00279EA2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (4)) == 0) goto loc_00279F6B;
    a3 = (*(unsigned __int64 *)(v_stack_m90) + result * 8) >> (9);
    a3 = (a3) & ((unsigned int)(*(unsigned int *)(v_stack_p8)));
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(v_stack_p8)));
    if (a3 == v_stack_m90) goto loc_0027A490;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 184)))) & (15)) == 0) goto loc_00279FF4;
loc_00279EF6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 184)))) & (15)) == 0) goto loc_00279F29;
    if (a3 < ((unsigned int)(*(unsigned int *)(result + a3 * 1)))) goto loc_00279F29;
    if (a3 <= ((unsigned int)(*(unsigned int *)(result + a3 * 1)))) goto loc_0027A4C5;
loc_00279F29:
    if (a3 < ((unsigned int)(*(unsigned int *)(result + a3 * 1)))) goto loc_00279F5C;
    if (a3 > ((unsigned int)(*(unsigned int *)(result + a3 * 1)))) goto loc_00279F5C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_00279F5C;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_0027A067;
loc_00279F5C:
    result = (*(unsigned __int64 *)(a3)) >> (60);
    result = (unsigned int)((result) & (2));
loc_00279F63:
loc_00279F65:
    if ((unsigned int)(result) != 0) goto loc_0027986F;
loc_00279F6B:
    if ((*(unsigned __int8 *)(v_stack_p8 + 9)) >= 2) goto loc_00279A1B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (1)) != 0) goto loc_0027A0D0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_0027A66F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) != 0) goto loc_0027A634;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521)) != 0) goto loc_0027A691;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) != 0) goto loc_0027A65E;
loc_00279FCF:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) <= 7) goto loc_00279A1B;
    if (0 == 0) goto loc_0027A698;
loc_00279FE1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) == 0) goto loc_0027A6D2;
    goto loc_0027A639;
loc_00279FF4:
    if (0 < (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16))) goto loc_00279EF6;
    if (0 > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16))) goto loc_00279EF6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_00279EF6;
    a3 = (unsigned int)((0) >> (3));
    a3 = (unsigned int)((a3) & (511));
    if (condition_is_above_or_equal) goto loc_0027B7D3;
    goto loc_00279F63;
loc_0027A067:
    if (((*(unsigned __int64 *)(v_rip + 13945366)) & (0x600000ULL)) == 0) goto loc_00279F5C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00279F5C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00279F5C;
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) & (511));
    result = 5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (32)) != 0) {
        result = (5) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (66)) == 0) { result = result; }
    goto loc_00279F5C;
loc_0027A0D0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)))) <= 7) goto loc_00279FCF;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8) + 14521)) != 0) goto loc_0027A639;
    goto loc_00279FE1;
loc_0027A0F0:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) >= 4) goto loc_00279E64;
loc_0027A0F9:
    goto loc_0027994B;
loc_0027A10D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 88) + 18688)) >= 0x420ULL) goto loc_002797E6;
    a4 = 0;
    v_rbp = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 88) + 16)) + (0x3A60ULL);
loc_0027A144:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13938371)))) goto loc_0027B6B6;
loc_0027A152:
    if (0 > 1) goto loc_0027B54C;
loc_0027A15F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12270489))))) goto loc_0027B53D;
    a1 = (0) + (0);
    v_r11 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 88) + 18688)) + (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp) + a1 * 8));
    if (v_r11 < 0x420ULL) goto loc_0027A757;
    v_r15 = 0;
    goto loc_002797E6;
loc_0027A196:
    a2 = (unsigned int)((result) >> (2));
    a2 = (unsigned int)((a2) & (7));
    if (((unsigned int)((unsigned int)(v_stack_p18))) == ((unsigned int)(a2))) goto loc_0027A1C8;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) - ((unsigned int)(a2)));
loc_0027A1B0:
    a1 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp) + a1 * 8)) >> (9);
    a1 = (a1) & (v_r11);
    a1 = (a1) + (0);
    a2 = ((unsigned int)((unsigned int)(result))) - (1);
    if (condition_is_not_equal) goto loc_0027A1B0;
loc_0027A1C8:
    if ((*(unsigned __int64 *)(v_stack_m90) + result * 8) >= a1) goto loc_002797B3;
    result = MiWalkGetResumptionPxe(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), 5, a4);
    *(unsigned __int64 *)(v_rbp) = result;
    if (*(unsigned __int64 *)(v_rbp) == 0) goto loc_0027A20B;
    a3 = (0) << (25);
loc_0027A1F3:
    result = (result) << (25);
    result = (result) - (a3);
    result = (result) >> (16);
    *(unsigned __int64 *)(v_rbp - 8) = result;
    a1 = (*(unsigned __int64 *)(v_rbp)) - (1);
    if (condition_is_not_equal) goto loc_0027A1F3;
loc_0027A20B:
    if (result > v_stack_m98) goto loc_0027A821;
    goto loc_00279769;
loc_0027A23A:
    *(unsigned __int64 *)(v_stack_p8 + 72) = 0;
    goto loc_002797B3;
loc_0027A248:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (2)) != 0) goto loc_0027A720;
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 13938371))) >= 4) goto loc_0027A821;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (1)) == 0) goto loc_0027A2B6;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 3) goto loc_0027A819;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (4)) == 0) goto loc_0027A748;
    a2 = (result) >> (9);
    a2 = (a2) & ((unsigned int)(*(unsigned int *)(v_stack_p8)));
    a2 = (a2) + (0);
    a3 = 0;
    result = MiReacquireWalkLocks(v_stack_p8, a2, a3, a4);
loc_0027A29E:
loc_0027A2B6:
    v_stack_p20 = 0;
    goto loc_00279799;
loc_0027A2C3:
    v_stack_p10 = 4;
    goto loc_0027994B;
loc_0027A2E1:
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_0027A7B1;
loc_0027A2F9:
    a2 = (v_stack_p8) >> (9);
    a2 = (a2) & (4);
    a2 = (a2) + (4);
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_0027A777;
loc_0027A32E:
    if ((*(unsigned __int64 *)(v_stack_m90)) == a2) goto loc_0027A5A9;
    if ((*(unsigned __int64 *)(v_stack_m90)) > a2) goto loc_0027B42F;
    if (a2 <= v_stack_m98) goto loc_0027A7C0;
loc_0027A34D:
    *(unsigned __int64 *)(v_stack_m90) = v_stack_m98 + 8;
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_0027A38E;
    v_r10 = (a2) << (25);
loc_0027A376:
    result = (v_stack_m98 + 8) << (25);
    result = (result) - (v_r10);
    result = (result) >> (16);
    *(unsigned __int64 *)(v_stack_p8 + (int)((unsigned int)((unsigned int)(v_stack_p18))) + 12 * 8 - 8) = result;
    a3 = ((int)((unsigned int)((unsigned int)(v_stack_p18)))) - (1);
    if (condition_is_not_equal) goto loc_0027A376;
loc_0027A38E:
    if (0 != 0) goto loc_0027A5B0;
loc_0027A397:
    if ((*(unsigned __int64 *)(v_stack_m90)) == (v_stack_m98 + 8)) goto loc_002797C0;
    goto loc_0027995E;
loc_0027A3B7:
    v_stack_p10 = 0;
    goto loc_0027994B;
loc_0027A3D2:
    if (((unsigned __int8)(result)) == 9) goto loc_00279B19;
    if (((unsigned __int8)(result)) == 8) goto loc_0027A472;
loc_0027A3E2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (64)) != 0) goto loc_00279CC9;
    if (((unsigned int)((unsigned int)(v_stack_p18))) >= 1) goto loc_00279CAE;
loc_0027A3F6:
    if (v_stack_m70 != (v_rip + 1408350)) goto loc_0027A7D9;
    result = MiQueryLeafPte(v_stack_p8, *(unsigned __int64 *)(v_stack_m90), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m98 + 8);
    v_stack_p10 = (unsigned int)(result);
loc_0027A422:
    v_r15 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 2) goto loc_0027A75F;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 3) goto loc_00279CD7;
    v_stack_p10 = 0;
    result = MiYieldPageTableWalk(v_stack_p8, v_r15 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m98 + 8);
    a2 = 0;
    result = MiWaitForFreePage(*(unsigned __int64 *)(v_stack_p8 + 88), a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m98 + 8);
    v_stack_p20 = 1;
    goto loc_00279D2E;
loc_0027A472:
    if (((*(unsigned int *)(v_stack_p8)) & (0x10000ULL)) != 0) goto loc_0027A3E2;
loc_0027A47F:
    goto loc_0027A422;
loc_0027A488:
    goto loc_00279C48;
loc_0027A490:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m98 + 8 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027A7FF;
loc_0027A4AD:
    goto loc_00279F65;
loc_0027A4BD:
    goto loc_0027990E;
loc_0027A4C5:
    a3 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) - (*(unsigned __int64 *)(gs_base + (0 + 32)));
    a3 = (a3) >> (3);
    result = ((unsigned int)((unsigned int)(a3 + a3 * 1))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3 + a3 * 1))) & (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12265047 + result * 4 + 9836))) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(a2)) & (2)) == 0) goto loc_00279F6B;
    goto loc_0027986F;
loc_0027A503:
    if (((*(unsigned __int64 *)(v_rip + 13944186)) & (0x600000ULL)) == 0) goto loc_00279B0B;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00279B0B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00279B0B;
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (66)) == 0) { result = result; }
    goto loc_00279B0B;
loc_0027A56C:
    if (result != (v_rip + 1762957)) goto loc_0027B5A0;
    a2 = (*(unsigned __int64 *)(v_stack_p8 + 184)) + (48);
    v_stack_mA8 = v_rip + 2238915;
    a4 = 0;
    a3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, a2, a3, a4);
    goto loc_0027990A;
loc_0027A5A9:
    *(unsigned __int64 *)(v_stack_p8 + 80) = 0;
loc_0027A5B0:
    a1 = (v_stack_p8) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (a2);
    v_stack_m68 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (a2);
    v_stack_m60 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (a2);
    v_stack_m58 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (a2);
    v_stack_m50 = a1;
loc_0027A611:
    *(unsigned __int64 *)(v_stack_p8 + (int)((unsigned int)((unsigned int)(v_stack_p18))) * 8 + 96) = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)((unsigned int)(v_stack_p18))) * 8 + 96);
    result = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)((unsigned int)(v_stack_p18))) * 8 + 96);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) != ((unsigned int)((unsigned int)(v_stack_p18)))) { result = 0; }
    if ((int)((unsigned int)((unsigned int)(v_stack_p18))) == 0) goto loc_0027A397;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) - 1);
    a1 = ((int)((unsigned int)((unsigned int)(v_stack_p18)))) - 1;
    goto loc_0027A611;
loc_0027A634:
loc_0027A639:
    if (((*(unsigned int *)(v_rip + 13944001)) & (0x4000000ULL)) != 0) {
        a3 = (unsigned int)((unsigned int)(v_stack_p10));
        a2 = (unsigned int)((int)((unsigned int)((unsigned int)(v_stack_p18))));
        a1 = 2;
        result = EtwTraceShouldYieldProcessor(a1, a2, a3, result);
    }
    if (2 != 0) goto loc_00279865;
    goto loc_00279A1B;
loc_0027A65E:
    if (result == (*(unsigned __int64 *)(a1 + 8))) goto loc_00279FCF;
    goto loc_0027A639;
loc_0027A66F:
    if (((unsigned int)((int)((unsigned int)((unsigned int)(v_stack_p18))))) <= 7) goto loc_00279A1B;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 14521)) == 0) goto loc_00279FE1;
    goto loc_0027A639;
loc_0027A691:
    goto loc_0027A639;
loc_0027A698:
    if (4 != 0) goto loc_00279FE1;
loc_0027A6A1:
    *(unsigned int *)(a1 + 33708) = 0;
    *(unsigned int *)(a1 + 34396) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0027B240;
loc_0027A6C9:
    goto loc_0027A639;
loc_0027A6D2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_0027A6A1;
    goto loc_0027A639;
loc_0027A6E6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) != (v_rip + 1762579)) goto loc_0027B5BC;
    a2 = (*(unsigned __int64 *)(v_stack_p8 + 184)) + (48);
    v_stack_mA8 = v_rip + 2238540;
    a4 = 0;
    a3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, a2, a3, a4);
    goto loc_00279E45;
loc_0027A720:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 3) goto loc_0027A819;
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(result);
    result = MiReacquireWalkLocks(v_stack_p8, a2, 6, a4);
    goto loc_0027A29E;
loc_0027A748:
    result = MiLockWorkingSetExclusive(v_stack_p8, a2, 6, a4);
    goto loc_0027A29E;
loc_0027A757:
    a4 = (unsigned int)((a4) + 1);
    goto loc_0027A15F;
loc_0027A75F:
    v_stack_p10 = 0;
    goto loc_00279D27;
loc_0027A777:
loc_0027A78B:
    a2 = (a2) >> (9);
    a2 = (a2) & (v_stack_m98);
    a2 = (a2) + (v_stack_m90);
    v_r10 = ((int)((unsigned int)((unsigned int)(v_stack_p18)))) << (9);
    a3 = (unsigned int)((6) - (1));
    if (condition_is_not_equal) goto loc_0027A78B;
    goto loc_0027A32E;
loc_0027A7B1:
    if (2 == 3) goto loc_0027A2F9;
    goto loc_002797C0;
loc_0027A7C0:
    if (((v_stack_p8) & (v_r10 - 1)) != 0) goto loc_0027A34D;
    *(unsigned __int64 *)(v_stack_p8 + 80) = 0;
    goto loc_0027A34D;
loc_0027A7D9:
    if ((v_r10 - 1) != (v_rip + 85872)) goto loc_0027B0F5;
    result = MiAgePte(v_stack_p8, a2, a3, a2);
    v_stack_p10 = (unsigned int)(result);
    goto loc_0027A422;
loc_0027A7FF:
    if (((unsigned __int8)(result)) == 7) goto loc_0027B2C9;
    if (((unsigned __int8)(result)) == 5) goto loc_0027B7CB;
    goto loc_0027A4AD;
loc_0027A819:
    if (((72) & (28)) == 0) goto loc_0027B7AB;
loc_0027A821:
loc_0027A827:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) & (1));
    if (((unsigned int)((unsigned int)(v_stack_p18))) == 3) goto loc_0027A8D5;
    if ((unsigned int)(result) != 0) goto loc_0027A8BE;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) | (32));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(a1);
    if (*(unsigned __int64 *)(v_stack_p8 + 176) == 0) goto loc_0027A8A4;
    if ((*(unsigned __int64 *)(v_stack_p8 + 176)) != (v_rip + 1762487)) goto loc_0027A9D4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 184))))) & (3)) == 0) goto loc_0027B580;
loc_0027A873:
loc_0027A878:
    v_stack_mA8 = v_rip + 2176385;
    a3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, *(unsigned __int64 *)(v_stack_p8 + 184) + 56, a3, 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (32)) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 184) + 6) = 1;
    }
loc_0027A8A4:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) & (0xFFFFFFDFULL));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(a1);
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_0027A8B6;
    v_rsi = (unsigned int)((unsigned int)(result));
    if (0 >= 4) {
        v_rsi = (unsigned int)((unsigned int)(result));
        if (0 == 5) { v_rsi = 5; }
    }
    v_rsp = (v_rsp) + (136);
    return (unsigned int)((unsigned int)(v_rsi));
loc_0027A8D5:
    if ((unsigned int)((unsigned int)((unsigned int)(v_rsi))) != 0) goto loc_0027A9A1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (64)) != 0) goto loc_0027B158;
loc_0027A8EF:
    a1 = (unsigned int)((a1) | (32));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(a1);
    if (*(unsigned __int64 *)(v_stack_p8 + 176) == 0) goto loc_0027B094;
    if ((*(unsigned __int64 *)(v_stack_p8 + 176)) != (v_rip + 1762309)) goto loc_0027B11B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 184))))) & (3)) == 0) goto loc_0027B5DB;
loc_0027A925:
loc_0027A92A:
    v_stack_p20 = v_rip + 2176207;
    a3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, *(unsigned __int64 *)(v_stack_p8 + 184) + 56, a3, 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (32)) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 184) + 6) = 1;
    }
loc_0027A957:
loc_0027A95B:
    if (*(unsigned __int64 *)(v_stack_p8 + 56) == 0) goto loc_0027A992;
    if (((*(unsigned int *)(v_stack_p8)) & (0x1000ULL)) == 0) goto loc_0027B2DE;
    if ((*(unsigned __int64 *)(v_stack_p8 + 56)) != ((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) goto loc_0027B2E7;
loc_0027A98A:
    *(unsigned __int64 *)(v_stack_p8 + 56) = 0;
loc_0027A992:
    v_rsi = 5;
    if (0 != 5) {
        v_rsi = v_stack_pD8;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (1)) == 0) goto loc_0027A8BE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (4)) != 0) goto loc_0027B07B;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 9))) != 17) goto loc_0027B173;
    result = MiLockWorkingSetExclusiveAtDpc(*(unsigned __int64 *)(v_stack_p8 + 32), *(unsigned __int64 *)(v_stack_p8 + 56), a3, 1);
loc_0027A9CC:
    goto loc_0027A8BE;
loc_0027A9D4:
    if (result != (v_rip + 1761829)) goto loc_0027B67D;
    a2 = (*(unsigned __int64 *)(v_stack_p8 + 184)) + (48);
    v_stack_p20 = v_rip + 2237790;
    a4 = 0;
    a3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, a2, a3, a4);
    goto loc_0027A8A0;
loc_0027AA0E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (4)) == 0) goto loc_0027AC0C;
    v_rsi = (5) >> (9);
    v_rsi = (v_rsi) & ((unsigned int)(*(unsigned int *)(v_stack_p8)));
    v_rsi = (v_rsi) + (a2);
    v_stack_pD8 = v_rsi;
    if (5 != 0) goto loc_0027AAC1;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027AD69;
    a2 = (v_stack_p40) + (176);
loc_0027AA7F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 8) = a2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13942887)) & (33)) != 0) goto loc_0027B063;
loc_0027AAA5:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_0027ABEF;
    result = KxWaitForLockOwnerShip(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    goto loc_0027ABE5;
loc_0027AAC1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 184)))) & (15)) != 0) goto loc_0027AB1C;
    if (5 < 0) goto loc_0027AB1C;
    if (5 > 0) goto loc_0027AB1C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_0027B69D;
loc_0027AB1C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 184)))) & (15)) == 0) goto loc_0027AB45;
    if (5 < 0) goto loc_0027AB45;
    if (5 <= 0) goto loc_0027B438;
loc_0027AB45:
    if (5 < 0) goto loc_0027AB7F;
    if (5 > 0) goto loc_0027AB7F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (1)) == 0) goto loc_0027AB7F;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0027ADFC;
loc_0027AB7F:
loc_0027AB89:
    if ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (1)) == 0) goto loc_0027ABCE;
    result = (*(unsigned __int64 *)(5)) >> (60);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0027B09F;
    a1 = (*(unsigned __int64 *)(5)) & (v_rsi);
    a1 = (a1) | (result);
    if (((*(unsigned __int64 *)(v_rip + 13942477)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13942477)) & (0x2000000ULL)) != 0) goto loc_0027AB89;
loc_0027ABCE:
loc_0027ABDE:
loc_0027ABE5:
loc_0027ABEF:
    if (((*(unsigned int *)(v_stack_pD0)) & (0x1000ULL)) == 0) goto loc_0027AE6A;
    if (v_stack_pD8 != 0) goto loc_0027AE73;
loc_0027AC08:
    *(unsigned __int64 *)(v_stack_pD0 + 56) = 5;
loc_0027AC0C:
    if (5 < 2) goto loc_0027AC88;
    if (5 > 2) goto loc_0027AC88;
    if ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (1)) == 0) goto loc_0027AC88;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(5))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0027AC88;
    if (((*(unsigned __int64 *)(v_rip + 13942327)) & (0x600000ULL)) == 0) goto loc_0027AC88;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0027AC88;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) != 0) {
        result = 5;
        result = (result) >> (3);
        result = (unsigned int)((result) & (511));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8);
    }
    v_rdi = (result) << (25);
    v_rbx = (5) << (25);
    v_rbx = (v_rbx) - (v_rdi);
    a2 = (v_rbx) >> (16);
    result = MiWalkPageTablesRecursively(v_stack_pD0, a2, (unsigned int)(v_stack_pE0) - 1, a4);
    v_stack_pD8 = (unsigned int)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pD0 + 4)))) & (3)) != 0) goto loc_0027AD97;
    if (((unsigned int)(result)) < 4) goto loc_0027B4DF;
    result = (v_rbx + 268435456) >> (16);
    if ((*(unsigned __int64 *)(v_stack_pD0 + (int)((unsigned int)((unsigned int)(v_stack_pE0))) * 8 + 88)) < result) goto loc_0027B638;
    a1 = (*(unsigned __int64 *)(v_stack_pD0 + (int)((unsigned int)((unsigned int)(v_stack_pE0))) * 8 + 88)) >> (9);
    v_r13 = (5) & (a1);
    v_r13 = (v_r13) + (0);
    *(unsigned __int64 *)(v_stack_p38) = v_r13;
    if ((unsigned int)((unsigned int)(v_stack_pE0)) == 0) goto loc_0027AD42;
loc_0027AD2A:
    result = (v_r13) << (25);
    result = (result) - (v_rdi);
    result = (result) >> (16);
    *(unsigned __int64 *)(v_stack_p38 - 8) = result;
    a1 = ((int)((unsigned int)((unsigned int)(v_stack_pE0)))) - (1);
    if (condition_is_not_equal) goto loc_0027AD2A;
loc_0027AD42:
    v_stack_pE8 = 1;
    v_r15 = 0;
    goto loc_0027977E;
loc_0027AD69:
    if (((unsigned __int8)(result)) == 7) goto loc_0027B205;
    if (((unsigned __int8)(result)) == 5) goto loc_0027B7DB;
loc_0027AD7E:
    a2 = (v_rip + 12262841 + 3 * 8) + (0x3280ULL);
    goto loc_0027AA7F;
loc_0027AD97:
    if ((((unsigned __int8)(a2)) & (28)) != 0) goto loc_0027ADCB;
    result = (1 + 268435456) >> (16);
    if ((*(unsigned __int64 *)(v_stack_pD0 + (int)((unsigned int)((unsigned int)(v_stack_pE0))) * 8 + 88)) < result) goto loc_0027ADCB;
    if ((unsigned int)((unsigned int)(v_stack_pE0)) != 0) {
        result = (unsigned __int8)((unsigned int)(v_stack_pE0));
        result = (unsigned int)((result) << (2));
        result = (unsigned int)((result) ^ ((unsigned int)(a2)));
        *(unsigned __int64 *)(v_stack_pD0 + 72) = v_r13;
        result = (unsigned int)((result) & (28));
        result = (unsigned int)((result) ^ ((unsigned int)(a2)));
        *(unsigned int *)(v_stack_pD0 + 4) = (unsigned int)(result);
    }
    v_r15 = 0;
loc_0027ADCE:
    v_stack_pE8 = 1;
    goto loc_0027977E;
loc_0027ADFC:
    if (((*(unsigned __int64 *)(v_rip + 13941889)) & (0x600000ULL)) == 0) goto loc_0027AB7F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0027AB7F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0027AE5B;
    result = (v_r13) >> (3);
    result = (unsigned int)((result) & (511));
    v_rbx = 1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (1) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
loc_0027AE5B:
    goto loc_0027AB7F;
loc_0027AE6A:
    if (((unsigned int)((unsigned int)(result))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) goto loc_0027AF25;
loc_0027AE73:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 184)))) & (15)) == 0) goto loc_0027AEAF;
loc_0027AE8D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 184)))) & (15)) != 0) goto loc_0027AFA9;
loc_0027AE9C:
    goto loc_0027AC08;
loc_0027AEAF:
    if (((unsigned int)((unsigned int)(result))) < 0) goto loc_0027AE8D;
    if (((unsigned int)((unsigned int)(result))) > 0) goto loc_0027AE8D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0027AE8D;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (3));
    v_rsi = (unsigned int)((v_rsi) & (511));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_rsi * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0027B02D;
    if (!sign_flag) goto loc_0027B61C;
    if (((*(unsigned __int8 *)(v_rip + 13941744)) & (1)) != 0) goto loc_0027B6E0;
loc_0027AF1C:
    v_rdi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_rsi * 4) = 0;
    goto loc_0027AC08;
loc_0027AF25:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027B049;
loc_0027AF46:
    v_rdi = 0;
loc_0027AF48:
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 40000) + (48);
    if (((*(unsigned __int8 *)(v_rip + 13941677)) & (1)) != 0) goto loc_0027B00A;
loc_0027AF5F:
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_0027AF84;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_0027AC08;
    result = KxWaitForLockChainValid(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), v_stack_p40, a4);
loc_0027AF84:
    *(unsigned __int64 *)(v_rbx) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rbx + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0027AC08;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rbx + 8), v_stack_p40, a4);
    goto loc_0027AC08;
loc_0027AFA9:
    if (v_rsi < 0) goto loc_0027AE9C;
    if (v_rsi > 0) goto loc_0027AE9C;
    v_rsi = (v_rsi) - (0);
    v_rsi = (v_rsi) >> (3);
    result = ((unsigned int)((unsigned int)(v_rsi + v_rsi * 1))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + v_rsi * 1))) & (31));
    result = (unsigned int)((3) << ((unsigned __int8)(a1)));
    result = (unsigned int)(~(result));
    goto loc_0027AC08;
loc_0027B00A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13184584))) != 0) goto loc_0027AF5F;
    result = KiReleaseQueuedSpinLockInstrumented(v_rbx, v_stack_pC8, v_stack_p40, a4);
    goto loc_0027AC08;
loc_0027B02D:
    if (((*(unsigned __int8 *)(v_rip + 13941458)) & (1)) != 0) goto loc_0027B741;
loc_0027B03A:
    goto loc_0027AC08;
loc_0027B049:
    if (((unsigned __int8)(result)) == 7) goto loc_0027B4D5;
    if (((unsigned __int8)(result)) == 5) goto loc_0027B7E3;
    goto loc_0027AF46;
loc_0027B063:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13184495))) != 0) goto loc_0027AAA5;
    result = KiAcquireQueuedSpinLockInstrumented(v_rbx, v_stack_pC8, v_stack_p40, a4);
    goto loc_0027ABE5;
loc_0027B07B:
    if (((unsigned __int8)(v_rbx)) == 17) goto loc_0027B166;
    result = MiLockWorkingSetShared((unsigned int)(v_stack_pE0), v_stack_pC8, v_stack_p40, a4);
    goto loc_0027A8BE;
loc_0027B094:
    goto loc_0027A95B;
loc_0027B09F:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_0027B270;
    v_rdi = (v_rbx) | (result);
    if (((*(unsigned __int64 *)(v_rip + 13941190)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_0027B640;
loc_0027B0D6:
    if (((*(unsigned __int64 *)(v_rip + 13941190)) & (0x2000000ULL)) == 0) { v_rbx = v_rdi; }
    goto loc_0027AB89;
loc_0027B0F5:
    if (v_rbx != (v_rip + 1011860)) goto loc_0027B29A;
    result = MiOutSwapWorkingSetPte(v_stack_pD0, v_stack_pC8, v_stack_p40, a4);
    v_stack_pD8 = (unsigned int)(result);
    goto loc_0027A422;
loc_0027B11B:
    if (result != (v_rip + 1759966)) goto loc_0027B700;
    a2 = (*(unsigned __int64 *)(v_stack_pD0 + 184)) + (48);
    v_stack_p20 = v_rip + 2235927;
    a4 = 0;
    a3 = 0;
    result = MiAgeTrimListsTail(v_stack_pD0, a2, a3, a4);
    goto loc_0027A957;
loc_0027B158:
    if (0 != 4) goto loc_0027A8EF;
    goto loc_0027A9A1;
loc_0027B166:
    result = MiLockWorkingSetSharedAtDpc(v_stack_pD0, a2, a3, a4);
    goto loc_0027A8BE;
loc_0027B173:
    result = MiLockWorkingSetExclusive(v_stack_pD0, a2, a3, a4);
    goto loc_0027A9CC;
loc_0027B180:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 48))))) & (112));
    if (((unsigned __int8)(a1)) == 48) goto loc_0027B1BD;
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 48))))) & (112));
    if (((unsigned __int8)(a1)) == 16) goto loc_0027B1BD;
    if (((unsigned __int8)(a1)) >= 16) goto loc_0027B1B1;
    if (((unsigned __int8)(a1)) < 16) goto loc_0027B1BD;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 48))))) & (0x180000ULL));
    if (((unsigned int)(result)) >= 0x100000ULL) goto loc_0027B1BD;
loc_0027B1B1:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 48))) & (112));
    if (((unsigned __int8)(a2)) != 80) goto loc_00279B96;
loc_0027B1BD:
    v_rbp = (unsigned int)(((unsigned int)(v_stack_pE0)) + 1);
    v_rdi = (*(unsigned __int8 *)(0 + 33)) << (32);
    v_rdi = (v_rdi) | ((unsigned int)(*(unsigned int *)(0 + 28)));
    v_rdi = (v_rdi) << (12);
    v_rdi = (v_rdi) | (0xFFFULL);
    if ((unsigned __int8)(v_rbp) != 0) goto loc_0027B1F0;
    result = MiPeriodicGoodCitizen(v_stack_pD0, v_r13, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00279B96;
loc_0027B1F0:
    result = MiGetNextVad(0, v_r13, a3, a4);
    if (result != 0) goto loc_0027B180;
    goto loc_00279B96;
loc_0027B205:
    goto loc_0027AD7E;
loc_0027B20F:
    if (*(unsigned __int64 *)(v_stack_pD0 + 56) == 0) goto loc_00279930;
    result = (unsigned int)((result) | (2));
    *(unsigned int *)(1) = (unsigned int)(result);
    if (condition_is_above_or_equal) goto loc_0027B5F7;
    if ((*(unsigned __int64 *)(v_stack_pD0 + 56)) != v_rdi) goto loc_0027B5F7;
loc_0027B237:
    *(unsigned __int64 *)(v_stack_pD0 + 56) = 0;
    goto loc_00279930;
loc_0027B240:
loc_0027B247:
    if ((*(unsigned __int64 *)(v_stack_pD0 + 56)) != v_rdi) goto loc_0027B247;
    if ((*(unsigned __int64 *)(v_stack_pD0 + 56)) >= v_rdi) goto loc_0027A6C9;
    result = KiRemoveSystemWorkPriorityKick(1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD0 + 56))))), *(unsigned __int64 *)(v_stack_pD0 + 56), a4);
    goto loc_0027A6C9;
loc_0027B270:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 13934644)) & ((unsigned int)(v_rbp))) == 0) goto loc_0027B4AE;
loc_0027B27E:
loc_0027B280:
    if (condition_is_below) goto loc_0027B270;
    goto loc_0027AB89;
loc_0027B29A:
    result = guard_dispatch_icall(1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD0 + 56))))), *(unsigned __int64 *)(v_stack_pD0 + 56), a4);
    v_stack_pD8 = (unsigned int)(result);
    goto loc_0027A422;
loc_0027B2AD:
    if ((*(unsigned __int64 *)(v_stack_pD0 + 168)) == (v_rip + 2300556)) goto loc_002798DA;
    goto loc_002798E0;
loc_0027B2C9:
    goto loc_00279F65;
loc_0027B2DE:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD0 + 56)))))) == (*(unsigned __int64 *)(24 + 1 * 1 + 40000))) goto loc_0027B371;
loc_0027B2E7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 184)))) & (15)) == 0) goto loc_0027B31C;
loc_0027B2F1:
loc_0027B2FB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 184)))) & (15)) != 0) goto loc_0027B3A1;
loc_0027B309:
    goto loc_0027A98A;
loc_0027B31C:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD0 + 56)))))) < 2) goto loc_0027B2FB;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD0 + 56)))))) > 1) goto loc_0027B2FB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0027B2F1;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD0 + 56)))))) >> (3);
    a2 = (unsigned int)((a2) & (511));
    result = ExReleaseSpinLockRegardlessFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + a2 * 4, a2, *(unsigned __int64 *)(v_stack_pD0 + 56), 0);
    goto loc_0027A98A;
loc_0027B371:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rbp + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027B417;
loc_0027B38D:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 32))) + (0x9C40ULL);
    a1 = (a1) + (48);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, 48, *(unsigned __int64 *)(v_stack_pD0 + 56), 0);
    goto loc_0027A98A;
loc_0027B3A1:
    if (48 < 2) goto loc_0027B309;
    if (48 > a1) goto loc_0027B309;
    a2 = (48) - (2);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (31));
    a3 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    a3 = (unsigned int)(~(a3));
    result = ((unsigned int)((unsigned int)(a2))) >> (5);
    goto loc_0027A98A;
loc_0027B3FB:
    if ((*(unsigned __int64 *)(v_stack_pD0 + 168)) == (v_rip + 2300222)) goto loc_00279E18;
    goto loc_00279E1E;
loc_0027B417:
    if (((unsigned __int8)(v_rip + 2300222)) == 7) goto loc_0027B524;
    a2 = 72;
    if (((unsigned __int8)(v_rip + 2300222)) == 5) { a2 = 0; }
    goto loc_0027B38D;
loc_0027B42F:
    *(unsigned __int64 *)(v_stack_pD0 + 80) = 0;
    goto loc_002797C0;
loc_0027B438:
    a1 = (v_r13) - (0);
    a1 = (a1) >> (3);
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    v_r15 = ((unsigned int)((unsigned int)(a1))) >> (5);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (31));
    v_rbp = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    v_rdi = (unsigned int)((2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    v_rdi = (unsigned int)(~(v_rdi));
loc_0027B485:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12261077 + 9836 + v_r15 * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0027B55A;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12261077 + 9836 + v_r15 * 4)))));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_rdi)));
    if (condition_is_equal) goto loc_0027ABDE;
    goto loc_0027B485;
loc_0027B4AE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13940228)))) & (64)) == 0) goto loc_0027B27E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12261077 + 9836 + v_r15 * 4)))))), 0);
    if ((unsigned __int8)(result) == 0) goto loc_0027B27E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12261077 + 9836 + v_r15 * 4)))))), 0);
    goto loc_0027B280;
loc_0027B4D5:
    goto loc_0027AF46;
loc_0027B4DF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pD0)))) & (4)) == 0) goto loc_0027A3E2;
    result = MiReacquireHigherPageTableLock(v_stack_pD0, v_r13, (unsigned int)((unsigned int)(v_rbp)), 0);
    if ((unsigned int)(result) == 0) goto loc_0027A3E2;
    v_r15 = 0;
    v_rsi = 0;
    if (((unsigned int)(result)) != 2) { v_rsi = (unsigned int)(result); }
    v_stack_pD8 = (unsigned int)(v_rsi);
    goto loc_0027ADCE;
loc_0027B518:
    goto loc_00279829;
loc_0027B524:
    a1 = (v_stack_pD0) + (0x9C40ULL);
    a1 = (a1) + (24);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, 24, 0 + 192, 0);
    goto loc_0027A98A;
loc_0027B53D:
    v_rbx = (v_rbx) + 1;
    v_rdi = (v_rdi) + (8);
    a4 = 0;
    goto loc_0027A152;
loc_0027B54C:
    v_rbp = (v_rbp) + (0xDF80ULL);
    result = (unsigned int)((result) + 1);
    goto loc_0027A144;
loc_0027B55A:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_0027B720;
    a2 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)((a2) | ((unsigned int)(0 + 192)));
    a3 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0 + 192))));
    if (condition_is_equal) { a3 = (unsigned int)(a2); }
    goto loc_0027B485;
loc_0027B580:
    if ((*(unsigned __int64 *)(v_stack_pD0 + 168)) == (v_rip + 2299833)) goto loc_0027A873;
    goto loc_0027A878;
loc_0027B5A0:
    if (a2 != (v_rip + 2066761)) goto loc_0027B761;
    result = MiDeleteVaTail(a1, a2, a3, a4);
loc_0027B5B5:
    goto loc_0027990A;
loc_0027B5BC:
    if (result != (v_rip + 2066733)) goto loc_0027B76E;
    result = MiDeleteVaTail(v_stack_pD0, a2, a3, a4);
    goto loc_00279E48;
loc_0027B5DB:
    if ((*(unsigned __int64 *)(v_stack_pD0 + 168)) == (v_rip + 2299742)) goto loc_0027A925;
    goto loc_0027A92A;
loc_0027B5F7:
    result = MiUnlockPageTable(*(unsigned __int64 *)(v_stack_pD0 + 32), a3, a3, a4);
    goto loc_0027B237;
loc_0027B608:
    goto loc_0027994B;
loc_0027B61C:
    v_rdi = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(v_rdi + 16, *(unsigned __int64 *)(v_stack_pD0 + 32), 256, a4);
loc_0027B638:
    goto loc_0027AD42;
loc_0027B640:
    result = (unsigned __int8)((0) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_0027B0D6;
    result = (*(unsigned __int64 *)(v_stack_pD0 + 32)) + (v_rdi + 16);
    if (v_r13 < result) goto loc_0027B0D6;
    result = MiCheckLinearProtectedPteAccessedBit(v_r13, 0, 128, a4);
    goto loc_0027B0D6;
loc_0027B67D:
    if (result != (v_rip + 2066540)) goto loc_0027B77A;
    result = MiDeleteVaTail(v_stack_pD0, 0, 128, a4);
loc_0027B695:
    goto loc_0027A8A0;
loc_0027B69D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (3));
    result = (unsigned int)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pD0 + result * 4, 0, 128, a4);
    goto loc_0027ABE5;
loc_0027B6B6:
    v_stack_pD8 = 5;
    v_r15 = 0;
    goto loc_0027A827;
loc_0027B6E0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13182834))) != 0) goto loc_0027AF1C;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_pD0 + result * 4, v_stack_pC8, 128, a4);
    goto loc_0027AC08;
loc_0027B700:
    if (result != (v_rip + 2066409)) goto loc_0027B7A1;
    result = MiDeleteVaTail(v_stack_pD0, v_stack_pC8, 128, a4);
loc_0027B718:
    goto loc_0027A957;
loc_0027B720:
    v_r12 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13933442)) & ((unsigned int)(v_r12))) == 0) goto loc_0027B784;
loc_0027B72C:
loc_0027B72E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15))))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0027B720;
    goto loc_0027B485;
loc_0027B741:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13182737))) != 0) goto loc_0027B03A;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    goto loc_0027AC08;
loc_0027B761:
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    goto loc_0027B5B5;
loc_0027B76E:
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    goto loc_00279E48;
loc_0027B77A:
    result = guard_dispatch_icall((unsigned int)((unsigned int)(result)), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    goto loc_0027B695;
loc_0027B784:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13939502)))) & (64)) == 0) goto loc_0027B72C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(result)), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0027B72C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    goto loc_0027B72E;
loc_0027B7A1:
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_r12)), v_stack_pC8, (unsigned int)(*(unsigned int *)(v_r15)), a4);
    goto loc_0027B718;
loc_0027B7AB:
    a4 = ((unsigned int)((unsigned int)(v_stack_pE0)) != 0) ? 1 : 0;
    a4 = (unsigned int)((a4) + (2));
    result = MiMarkResumptionPoint(v_stack_pD0, 5, (unsigned int)((unsigned int)((unsigned int)(v_stack_pE0))), a4);
    goto loc_0027A821;
loc_0027B7CB:
    goto loc_0027A4AD;
loc_0027B7D3:
    goto loc_00279F63;
loc_0027B7DB:
    goto loc_0027AD7E;
loc_0027B7E3:
    v_rdi = 0;
    goto loc_0027AF48;
loc_0027B7EC:
    goto loc_0027A47F;
}
```

## 5. (Beta) C Style

```c
int64_t MiWalkPageTablesRecursively(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pE0;
    uint32_t v_stack_pE8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    local_r15 = 0;
    v_stack_m88 = *(uint64_t *)(arg1 + 0x20);
    v_stack_m70 = *(uint64_t *)(arg1 + 0xA8);
    v_stack_m78 = (int32_t)(Arg3);
    v_stack_m90 = Arg1 + 96 + (int32_t)(Arg3) * 8;
    if (Arg2 < (*(uint64_t *)(arg1 + 0x60 + (int32_t)(Arg3) * 8))) { Arg2 = *(uint64_t *)(arg1 + 0x60 + (int32_t)(Arg3) * 8); }
    local_r11 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    local_r11 = (local_r11) + (0xFF8ULL);
    v_stack_m80 = Arg1 + 128 + (int32_t)(Arg3) * 8;
    v_stack_p20 = 0;
    if (local_r11 > (*(uint64_t *)(arg1 + 0x80 + (int32_t)(Arg3) * 8))) { local_r11 = *(uint64_t *)(arg1 + 0x80 + (int32_t)(Arg3) * 8); }
    v_stack_m98 = local_r11;
loc_00279769:
    v_stack_p10 = 0;
loc_00279774:
loc_0027977E:
loc_00279788:
    if (Arg2 > local_r11) goto loc_0027A821;
    if (0 != 0) goto loc_0027A248;
loc_00279799:
    local_r12 = ((uint32_t)((int32_t)(Arg3)) != 0) ? 1 : 0;
    local_r12 = (uint32_t)((local_r12) + (2));
    if (*(uint64_t *)(arg1 + 0x48) != 0) goto loc_00279973;
loc_002797B3:
    if (*(uint64_t *)(arg1 + 0x50) != 0) goto loc_0027A2E1;
loc_002797C0:
    Arg1 = ((((uint8_t)(*(uint64_t *)(arg1 + 0xA0))) & (15)) == 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (8)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0027A10D;
loc_002797E6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_00279A1B;
    if (((*(uint8_t *)(arg1 + 0x8)) & ((uint8_t)(*(uint64_t *)(arg1 + 0xA0)))) != 0) goto loc_00279A1B;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (4));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (((uint8_t)(result)) > 5) goto loc_00279EA2;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0027B518;
loc_00279829:
    if ((uint32_t)(Arg2) == 0) goto loc_00279E82;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_00279DCC;
loc_00279853:
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144))) << (6);
    if (condition_is_above_or_equal) goto loc_00279EA2;
loc_00279865:
loc_0027986F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (28)) != 0) goto loc_002798A2;
    if ((uint32_t)((int32_t)(Arg3)) == 0) goto loc_002798A2;
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))));
    if (((uint32_t)(local_r12)) != 3) {
        result = (uint8_t)((int32_t)(Arg3));
        Arg1 = Arg1 + 4;
        result = (uint32_t)((result) << (2));
        result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
        *(uint64_t *)(arg1 + 0x48) = Arg2;
        result = (uint32_t)((result) & (28));
        result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    }
    result = (uint32_t)((result) | (32));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if (*(uint64_t *)(arg1 + 0xB0) == 0) goto loc_0027A4BD;
    if ((*(uint64_t *)(arg1 + 0xB0)) != (v_rip + 1766480)) goto loc_0027A56C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8))))) & (3)) == 0) goto loc_0027B2AD;
loc_002798DA:
loc_002798E0:
    Arg3 = 0;
    v_stack_mA8 = v_rip + 2180377;
    result = MiAgeTrimListsTail(Arg1, *(uint64_t *)(arg1 + 0xB8) + 56, Arg3, 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (32)) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x6) = 1;
    }
loc_0027990A:
loc_0027990E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (1)) != 0) goto loc_00279930;
    if (0 >= 4) goto loc_00279935;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_0027B20F;
    result = MiReleaseWalkLocks(Arg1, (uint32_t)(*(uint32_t *)(arg1)), Arg3, 1);
loc_00279930:
    if (0 >= 4) {
        v_stack_p10 = 0;
    }
loc_0027994B:
    v_stack_p20 = 1;
loc_0027995E:
    goto loc_00279774;
loc_00279973:
    if (Arg2 < 1) goto loc_002799B2;
loc_00279988:
    if (Arg2 > v_stack_m90) goto loc_002799AA;
    Arg2 = (Arg2) << (25);
    Arg1 = (1) << (25);
    Arg2 = (Arg2) - (Arg1);
    Arg2 = (Arg2) >> (16);
    if (Arg2 >= 1) goto loc_00279988;
loc_002799AA:
loc_002799B2:
    if (result < 1) goto loc_002799EE;
loc_002799C4:
    if (result > (Arg1 + (int32_t)((uint32_t)((int32_t)(Arg3))) + 12 * 8)) goto loc_002799E6;
    result = (result) << (25);
    Arg1 = (1) << (25);
    result = (result) - (Arg1);
    result = (result) >> (16);
    if (result >= 1) goto loc_002799C4;
loc_002799E6:
loc_002799EE:
    if (Arg2 > result) goto loc_0027A23A;
    if ((*(uint64_t *)(arg1 + 0x48)) != Arg2) goto loc_0027A196;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (0xFFFFFFE3ULL));
    *(uint64_t *)(arg1 + 0x48) = 0;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(Arg2);
    goto loc_002797B3;
loc_00279A1B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (32)) != 0) goto loc_00279DC2;
    result = MiComputePxeWalkAction(Arg1, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), 2);
loc_00279A37:
    if (((uint32_t)(result)) == 4) goto loc_0027A2C3;
    if ((uint32_t)(result) == 0) goto loc_0027A3B7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (1)) != 0) goto loc_0027B608;
    if (((uint32_t)((int32_t)(Arg3))) >= 1) goto loc_00279D74;
loc_00279A65:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 1) goto loc_00279CCC;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 2) goto loc_00279DD4;
    if ((uint32_t)((int32_t)(Arg3)) != 0) goto loc_0027A3E2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) != 0) goto loc_0027A3E2;
    if ((((uint8_t)(*(uint64_t *)(Arg2))) & (1)) == 0) goto loc_0027A3E2;
    Arg3 = (Arg2) << (25);
    result = (2) << (25);
    Arg3 = (Arg3) - (result);
    Arg3 = (Arg3) >> (16);
    Arg3 = (Arg3) & (result);
    Arg3 = (Arg3) >> (9);
    Arg3 = (Arg3) + (2);
    if (Arg3 < Arg1) goto loc_00279B0B;
    if (Arg3 > Arg1) goto loc_00279B0B;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_00279B0B;
    Arg2 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_0027A503;
loc_00279B0B:
    result = (*(uint64_t *)(Arg3)) >> (56);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) != 10) goto loc_0027A3D2;
loc_00279B19:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) != 0) goto loc_0027A47F;
    if (Arg2 < 2) goto loc_00279B6A;
    Arg1 = (2) << (25);
loc_00279B47:
    if (Arg2 > Arg1) goto loc_00279B62;
    local_rbx = (Arg2) << (25);
    local_rbx = (local_rbx) - (Arg1);
    local_rbx = (local_rbx) >> (16);
    if (local_rbx >= 2) goto loc_00279B47;
loc_00279B62:
loc_00279B6A:
    result = MiGetLeafVa(Arg2, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    result = MiLockVadTree(1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    result = MiLocateAddress(result, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    if (result != 0) goto loc_0027B180;
loc_00279B96:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    if (local_rbx == result) goto loc_0027B7EC;
    local_rdi = (result) >> (9);
    Arg1 = (Arg1) & (local_rdi);
    Arg1 = (Arg1) + (2);
    Arg1 = (Arg1) ^ (Arg2);
    if (((v_stack_m80) & (Arg1)) == 0) goto loc_0027A488;
    if ((Arg1 + 8) < 2) goto loc_00279C35;
    Arg2 = (2) << (25);
loc_00279C17:
    if ((Arg1 + 8) > 0) goto loc_00279C32;
    Arg1 = (Arg1 + 8) << (25);
    Arg1 = (Arg1) - (Arg2);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= 2) goto loc_00279C17;
loc_00279C32:
    local_r15 = 0;
loc_00279C35:
    local_r13 = (Arg2) & (-8);
    *(void **)(v_stack_p8 + 0x50) = Arg1;
    local_r13 = (local_r13) | (0xFF8ULL);
    local_r13 = (local_r13) + (8);
loc_00279C48:
    *(uint64_t *)(v_stack_m90) = local_r13;
    if (v_stack_m78 == 0) goto loc_00279C7F;
    Arg2 = (2) << (25);
loc_00279C67:
    local_r13 = (local_r13) << (25);
    local_r13 = (local_r13) - (Arg2);
    local_r13 = (local_r13) >> (16);
    *(uint64_t *)(v_stack_m90 - 0x8) = local_r13;
    result = (v_stack_m78) - (1);
    if (condition_is_not_equal) goto loc_00279C67;
loc_00279C7F:
    *(uint32_t *)(v_stack_p8 + 0xC) = 0;
    local_rsi = (uint32_t)(v_stack_p10);
    if ((Arg1 + 8) > (*(uint64_t *)(v_stack_m80))) { local_rsi = 4; }
    v_stack_p10 = (uint32_t)(local_rsi);
    goto loc_0027994B;
loc_00279CAE:
    if (((4) & (1)) != 0) goto loc_0027A3F6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0xB8)))) & (15)) == 0) goto loc_0027A3F6;
loc_00279CC9:
    local_r15 = 0;
loc_00279CCC:
    v_stack_p10 = 0;
loc_00279CD7:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC))) + 1);
    *(uint64_t *)(v_stack_m90) = *(uint64_t *)(v_stack_m90) + result * 8;
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_00279D23;
    Arg3 = (result) << (25);
loc_00279D0B:
    result = (*(uint64_t *)(v_stack_m90) + result * 8) << (25);
    result = (result) - (Arg3);
    result = (result) >> (16);
    *(uint64_t *)(v_stack_m90 - 0x8) = result;
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - (1);
    if (condition_is_not_equal) goto loc_00279D0B;
loc_00279D23:
    *(uint32_t *)(v_stack_p8 + 0xC) = 0;
loc_00279D27:
loc_00279D2E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (1)) != 0) goto loc_0027994B;
    if (0 < 4) goto loc_00279788;
    goto loc_0027994B;
loc_00279D74:
    if (((uint32_t)((int32_t)((uint32_t)((uint32_t)(v_stack_p18))))) == 3) goto loc_00279A65;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m80)))) >> (2));
    local_r11 = (uint32_t)((local_r11) & (7));
    if ((((uint8_t)(*(uint64_t *)(v_stack_m80))) & (28)) == 0) goto loc_00279A65;
    result = MiWalkGetResumptionPxe(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), 1 + 1, *(uint64_t *)(v_stack_m80));
    if (result != (*(uint64_t *)(v_stack_m90) + result * 8)) goto loc_00279A65;
    if (((uint32_t)(local_r11 - 1)) >= ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_00279A65;
    local_rbx = (uint32_t)((1) & (0xFFFFFFE3ULL));
    *(uint64_t *)(v_stack_p8 + 0x48) = 0;
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(local_rbx);
    goto loc_00279A65;
loc_00279DC2:
    result = MiGetNextPageTablePte(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), 1 + 1, *(uint64_t *)(v_stack_m80));
    goto loc_00279A37;
loc_00279DCC:
    goto loc_00279853;
loc_00279DD4:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (6));
    result = (uint32_t)((result) & (7));
    if (((uint32_t)((uint32_t)(v_stack_p18))) <= ((uint32_t)(result))) goto loc_0027A3E2;
    local_rbx = (uint32_t)((local_rbx) | (32));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(local_rbx);
    if (*(uint64_t *)(v_stack_p8 + 0xB0) == 0) goto loc_00279E45;
    if ((*(uint64_t *)(v_stack_p8 + 0xB0)) != (v_rip + 1765138)) goto loc_0027A6E6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0xB8))))) & (3)) == 0) goto loc_0027B3FB;
loc_00279E18:
loc_00279E1E:
    Arg3 = 0;
    v_stack_mA8 = v_rip + 2179035;
    result = MiAgeTrimListsTail(v_stack_p8, *(uint64_t *)(v_stack_p8 + 0xB8) + 56, Arg3, 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (32)) != 0) {
        *(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0xB8) + 0x6) = 1;
    }
loc_00279E48:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) & (0xFFFFFFDFULL));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(result);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0027A0F0;
    if (0 < 4) goto loc_0027AA0E;
loc_00279E64:
    local_rbx = (uint32_t)(v_stack_p10);
    if (0 == 5) { local_rbx = 5; }
    v_stack_p10 = (uint32_t)(local_rbx);
    goto loc_0027A0F9;
loc_00279E82:
loc_00279E85:
    if (0 >= 4) goto loc_00279EA2;
    result = (0) << (6);
    if (condition_is_below) goto loc_00279865;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00279E85;
loc_00279EA2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (4)) == 0) goto loc_00279F6B;
    Arg3 = (*(uint64_t *)(v_stack_m90) + result * 8) >> (9);
    Arg3 = (Arg3) & ((uint32_t)(*(uint32_t *)(v_stack_p8)));
    Arg3 = (Arg3) + ((uint32_t)(*(uint32_t *)(v_stack_p8)));
    if (Arg3 == v_stack_m90) goto loc_0027A490;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0xB8)))) & (15)) == 0) goto loc_00279FF4;
loc_00279EF6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0xB8)))) & (15)) == 0) goto loc_00279F29;
    if (Arg3 < ((uint32_t)(*(uint32_t *)(result + Arg3 * 1)))) goto loc_00279F29;
    if (Arg3 <= ((uint32_t)(*(uint32_t *)(result + Arg3 * 1)))) goto loc_0027A4C5;
loc_00279F29:
    if (Arg3 < ((uint32_t)(*(uint32_t *)(result + Arg3 * 1)))) goto loc_00279F5C;
    if (Arg3 > ((uint32_t)(*(uint32_t *)(result + Arg3 * 1)))) goto loc_00279F5C;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_00279F5C;
    Arg2 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_0027A067;
loc_00279F5C:
    result = (*(uint64_t *)(Arg3)) >> (60);
    result = (uint32_t)((result) & (2));
loc_00279F63:
loc_00279F65:
    if ((uint32_t)(result) != 0) goto loc_0027986F;
loc_00279F6B:
    if ((*(uint8_t *)(v_stack_p8 + 0x9)) >= 2) goto loc_00279A1B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (1)) != 0) goto loc_0027A0D0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_0027A66F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) != 0) goto loc_0027A634;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9)) != 0) goto loc_0027A691;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) != 0) goto loc_0027A65E;
loc_00279FCF:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) <= 7) goto loc_00279A1B;
    if (0 == 0) goto loc_0027A698;
loc_00279FE1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) == 0) goto loc_0027A6D2;
    goto loc_0027A639;
loc_00279FF4:
    if (0 < (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10))) goto loc_00279EF6;
    if (0 > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10))) goto loc_00279EF6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_00279EF6;
    Arg3 = (uint32_t)((0) >> (3));
    Arg3 = (uint32_t)((Arg3) & (511));
    if (condition_is_above_or_equal) goto loc_0027B7D3;
    goto loc_00279F63;
loc_0027A067:
    if (((*(uint64_t *)(v_rip + 0xD4CA16)) & (0x600000ULL)) == 0) goto loc_00279F5C;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00279F5C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00279F5C;
    Arg3 = (Arg3) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    result = 5;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) & (32)) != 0) {
        result = (5) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) & (66)) == 0) { result = result; }
    goto loc_00279F5C;
loc_0027A0D0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)))) <= 7) goto loc_00279FCF;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8) + 0x38B9)) != 0) goto loc_0027A639;
    goto loc_00279FE1;
loc_0027A0F0:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) >= 4) goto loc_00279E64;
loc_0027A0F9:
    goto loc_0027994B;
loc_0027A10D:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x58) + 0x4900)) >= 0x420ULL) goto loc_002797E6;
    a4 = 0;
    local_rbp = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x58) + 0x10)) + (0x3A60ULL);
loc_0027A144:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0xD4AEC3)))) goto loc_0027B6B6;
loc_0027A152:
    if (0 > 1) goto loc_0027B54C;
loc_0027A15F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB3B99))))) goto loc_0027B53D;
    Arg1 = (0) + (0);
    local_r11 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x58) + 0x4900)) + (*(uint16_t *)(*(uint64_t *)(local_rbp) + arg1 * 8));
    if (local_r11 < 0x420ULL) goto loc_0027A757;
    local_r15 = 0;
    goto loc_002797E6;
loc_0027A196:
    Arg2 = (uint32_t)((result) >> (2));
    Arg2 = (uint32_t)((Arg2) & (7));
    if (((uint32_t)((uint32_t)(v_stack_p18))) == ((uint32_t)(Arg2))) goto loc_0027A1C8;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - ((uint32_t)(Arg2)));
loc_0027A1B0:
    Arg1 = (*(uint16_t *)(*(uint64_t *)(local_rbp) + arg1 * 8)) >> (9);
    Arg1 = (Arg1) & (local_r11);
    Arg1 = (Arg1) + (0);
    Arg2 = ((uint32_t)((uint32_t)(result))) - (1);
    if (condition_is_not_equal) goto loc_0027A1B0;
loc_0027A1C8:
    if ((*(uint64_t *)(v_stack_m90) + result * 8) >= Arg1) goto loc_002797B3;
    result = MiWalkGetResumptionPxe(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), 5, a4);
    *(uint64_t *)(local_rbp) = result;
    if (*(uint64_t *)(local_rbp) == 0) goto loc_0027A20B;
    Arg3 = (0) << (25);
loc_0027A1F3:
    result = (result) << (25);
    result = (result) - (Arg3);
    result = (result) >> (16);
    *(uint64_t *)(local_rbp - 0x8) = result;
    Arg1 = (*(uint64_t *)(local_rbp)) - (1);
    if (condition_is_not_equal) goto loc_0027A1F3;
loc_0027A20B:
    if (result > v_stack_m98) goto loc_0027A821;
    goto loc_00279769;
loc_0027A23A:
    *(uint64_t *)(v_stack_p8 + 0x48) = 0;
    goto loc_002797B3;
loc_0027A248:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (2)) != 0) goto loc_0027A720;
    if (((uint32_t)(*(uint16_t *)(v_rip + 0xD4AEC3))) >= 4) goto loc_0027A821;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (1)) == 0) goto loc_0027A2B6;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 3) goto loc_0027A819;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (4)) == 0) goto loc_0027A748;
    Arg2 = (result) >> (9);
    Arg2 = (Arg2) & ((uint32_t)(*(uint32_t *)(v_stack_p8)));
    Arg2 = (Arg2) + (0);
    Arg3 = 0;
    result = MiReacquireWalkLocks(v_stack_p8, Arg2, Arg3, a4);
loc_0027A29E:
loc_0027A2B6:
    v_stack_p20 = 0;
    goto loc_00279799;
loc_0027A2C3:
    v_stack_p10 = 4;
    goto loc_0027994B;
loc_0027A2E1:
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_0027A7B1;
loc_0027A2F9:
    Arg2 = (v_stack_p8) >> (9);
    Arg2 = (Arg2) & (4);
    Arg2 = (Arg2) + (4);
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_0027A777;
loc_0027A32E:
    if ((*(uint64_t *)(v_stack_m90)) == Arg2) goto loc_0027A5A9;
    if ((*(uint64_t *)(v_stack_m90)) > Arg2) goto loc_0027B42F;
    if (Arg2 <= v_stack_m98) goto loc_0027A7C0;
loc_0027A34D:
    *(uint64_t *)(v_stack_m90) = v_stack_m98 + 8;
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_0027A38E;
    local_r10 = (Arg2) << (25);
loc_0027A376:
    result = (v_stack_m98 + 8) << (25);
    result = (result) - (local_r10);
    result = (result) >> (16);
    *(uint64_t *)(v_stack_p8 + (int32_t)((uint32_t)((uint32_t)(v_stack_p18))) + 0xC * 8 - 0x8) = result;
    Arg3 = ((int32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - (1);
    if (condition_is_not_equal) goto loc_0027A376;
loc_0027A38E:
    if (0 != 0) goto loc_0027A5B0;
loc_0027A397:
    if ((*(uint64_t *)(v_stack_m90)) == (v_stack_m98 + 8)) goto loc_002797C0;
    goto loc_0027995E;
loc_0027A3B7:
    v_stack_p10 = 0;
    goto loc_0027994B;
loc_0027A3D2:
    if (((uint8_t)(result)) == 9) goto loc_00279B19;
    if (((uint8_t)(result)) == 8) goto loc_0027A472;
loc_0027A3E2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (64)) != 0) goto loc_00279CC9;
    if (((uint32_t)((uint32_t)(v_stack_p18))) >= 1) goto loc_00279CAE;
loc_0027A3F6:
    if (v_stack_m70 != (v_rip + 1408350)) goto loc_0027A7D9;
    result = MiQueryLeafPte(v_stack_p8, *(uint64_t *)(v_stack_m90), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m98 + 8);
    v_stack_p10 = (uint32_t)(result);
loc_0027A422:
    local_r15 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 2) goto loc_0027A75F;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 3) goto loc_00279CD7;
    v_stack_p10 = 0;
    result = MiYieldPageTableWalk(v_stack_p8, local_r15 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m98 + 8);
    Arg2 = 0;
    result = MiWaitForFreePage(*(uint64_t *)(v_stack_p8 + 0x58), Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m98 + 8);
    v_stack_p20 = 1;
    goto loc_00279D2E;
loc_0027A472:
    if (((*(uint32_t *)(v_stack_p8)) & (0x10000ULL)) != 0) goto loc_0027A3E2;
loc_0027A47F:
    goto loc_0027A422;
loc_0027A488:
    goto loc_00279C48;
loc_0027A490:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x8 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027A7FF;
loc_0027A4AD:
    goto loc_00279F65;
loc_0027A4BD:
    goto loc_0027990E;
loc_0027A4C5:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - (*(uint64_t *)(gs_base + (0 + 0x20)));
    Arg3 = (Arg3) >> (3);
    result = ((uint32_t)((uint32_t)(Arg3 + Arg3 * 1))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3 + Arg3 * 1))) & (31));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xBB2657 + result * 4 + 0x266C))) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(Arg2)) & (2)) == 0) goto loc_00279F6B;
    goto loc_0027986F;
loc_0027A503:
    if (((*(uint64_t *)(v_rip + 0xD4C57A)) & (0x600000ULL)) == 0) goto loc_00279B0B;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00279B0B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00279B0B;
    Arg3 = (Arg3) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) & (66)) == 0) { result = result; }
    goto loc_00279B0B;
loc_0027A56C:
    if (result != (v_rip + 1762957)) goto loc_0027B5A0;
    Arg2 = (*(uint64_t *)(v_stack_p8 + 0xB8)) + (48);
    v_stack_mA8 = v_rip + 2238915;
    a4 = 0;
    Arg3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, Arg2, Arg3, a4);
    goto loc_0027990A;
loc_0027A5A9:
    *(uint64_t *)(v_stack_p8 + 0x50) = 0;
loc_0027A5B0:
    Arg1 = (v_stack_p8) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (Arg2);
    v_stack_m68 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (Arg2);
    v_stack_m60 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (Arg2);
    v_stack_m58 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (Arg2);
    v_stack_m50 = Arg1;
loc_0027A611:
    *(uint64_t *)(v_stack_p8 + (int32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 8 + 0x60) = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 8 + 0x60);
    result = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 8 + 0x60);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) != ((uint32_t)((uint32_t)(v_stack_p18)))) { result = 0; }
    if ((int32_t)((uint32_t)((uint32_t)(v_stack_p18))) == 0) goto loc_0027A397;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - 1);
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - 1;
    goto loc_0027A611;
loc_0027A634:
loc_0027A639:
    if (((*(uint32_t *)(v_rip + 0xD4C4C1)) & (0x4000000ULL)) != 0) {
        Arg3 = (uint32_t)((uint32_t)(v_stack_p10));
        Arg2 = (uint32_t)((int32_t)((uint32_t)((uint32_t)(v_stack_p18))));
        Arg1 = 2;
        result = EtwTraceShouldYieldProcessor(Arg1, Arg2, Arg3, result);
    }
    if (2 != 0) goto loc_00279865;
    goto loc_00279A1B;
loc_0027A65E:
    if (result == (*(uint64_t *)(arg1 + 0x8))) goto loc_00279FCF;
    goto loc_0027A639;
loc_0027A66F:
    if (((uint32_t)((int32_t)((uint32_t)((uint32_t)(v_stack_p18))))) <= 7) goto loc_00279A1B;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x38B9)) == 0) goto loc_00279FE1;
    goto loc_0027A639;
loc_0027A691:
    goto loc_0027A639;
loc_0027A698:
    if (4 != 0) goto loc_00279FE1;
loc_0027A6A1:
    *(uint32_t *)(arg1 + 0x83AC) = 0;
    *(uint32_t *)(arg1 + 0x865C) = 0;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0027B240;
loc_0027A6C9:
    goto loc_0027A639;
loc_0027A6D2:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_0027A6A1;
    goto loc_0027A639;
loc_0027A6E6:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) != (v_rip + 1762579)) goto loc_0027B5BC;
    Arg2 = (*(uint64_t *)(v_stack_p8 + 0xB8)) + (48);
    v_stack_mA8 = v_rip + 2238540;
    a4 = 0;
    Arg3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, Arg2, Arg3, a4);
    goto loc_00279E45;
loc_0027A720:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 3) goto loc_0027A819;
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(result);
    result = MiReacquireWalkLocks(v_stack_p8, Arg2, 6, a4);
    goto loc_0027A29E;
loc_0027A748:
    result = MiLockWorkingSetExclusive(v_stack_p8, Arg2, 6, a4);
    goto loc_0027A29E;
loc_0027A757:
    a4 = (uint32_t)((a4) + 1);
    goto loc_0027A15F;
loc_0027A75F:
    v_stack_p10 = 0;
    goto loc_00279D27;
loc_0027A777:
loc_0027A78B:
    Arg2 = (Arg2) >> (9);
    Arg2 = (Arg2) & (v_stack_m98);
    Arg2 = (Arg2) + (v_stack_m90);
    local_r10 = ((int32_t)((uint32_t)((uint32_t)(v_stack_p18)))) << (9);
    Arg3 = (uint32_t)((6) - (1));
    if (condition_is_not_equal) goto loc_0027A78B;
    goto loc_0027A32E;
loc_0027A7B1:
    if (2 == 3) goto loc_0027A2F9;
    goto loc_002797C0;
loc_0027A7C0:
    if (((v_stack_p8) & (local_r10 - 1)) != 0) goto loc_0027A34D;
    *(uint64_t *)(v_stack_p8 + 0x50) = 0;
    goto loc_0027A34D;
loc_0027A7D9:
    if ((local_r10 - 1) != (v_rip + 85872)) goto loc_0027B0F5;
    result = MiAgePte(v_stack_p8, Arg2, Arg3, Arg2);
    v_stack_p10 = (uint32_t)(result);
    goto loc_0027A422;
loc_0027A7FF:
    if (((uint8_t)(result)) == 7) goto loc_0027B2C9;
    if (((uint8_t)(result)) == 5) goto loc_0027B7CB;
    goto loc_0027A4AD;
loc_0027A819:
    if (((72) & (28)) == 0) goto loc_0027B7AB;
loc_0027A821:
loc_0027A827:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) & (1));
    if (((uint32_t)((uint32_t)(v_stack_p18))) == 3) goto loc_0027A8D5;
    if ((uint32_t)(result) != 0) goto loc_0027A8BE;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) | (32));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(Arg1);
    if (*(uint64_t *)(v_stack_p8 + 0xB0) == 0) goto loc_0027A8A4;
    if ((*(uint64_t *)(v_stack_p8 + 0xB0)) != (v_rip + 1762487)) goto loc_0027A9D4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0xB8))))) & (3)) == 0) goto loc_0027B580;
loc_0027A873:
loc_0027A878:
    v_stack_mA8 = v_rip + 2176385;
    Arg3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, *(uint64_t *)(v_stack_p8 + 0xB8) + 56, Arg3, 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (32)) != 0) {
        *(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0xB8) + 0x6) = 1;
    }
loc_0027A8A4:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) & (0xFFFFFFDFULL));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(Arg1);
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_0027A8B6;
    local_rsi = (uint32_t)((uint32_t)(result));
    if (0 >= 4) {
        local_rsi = (uint32_t)((uint32_t)(result));
        if (0 == 5) { local_rsi = 5; }
    }
    local_rsp = (local_rsp) + (136);
    return (uint32_t)((uint32_t)(local_rsi));
loc_0027A8D5:
    if ((uint32_t)((uint32_t)((uint32_t)(local_rsi))) != 0) goto loc_0027A9A1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (64)) != 0) goto loc_0027B158;
loc_0027A8EF:
    Arg1 = (uint32_t)((Arg1) | (32));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(Arg1);
    if (*(uint64_t *)(v_stack_p8 + 0xB0) == 0) goto loc_0027B094;
    if ((*(uint64_t *)(v_stack_p8 + 0xB0)) != (v_rip + 1762309)) goto loc_0027B11B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0xB8))))) & (3)) == 0) goto loc_0027B5DB;
loc_0027A925:
loc_0027A92A:
    v_stack_p20 = v_rip + 2176207;
    Arg3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, *(uint64_t *)(v_stack_p8 + 0xB8) + 56, Arg3, 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (32)) != 0) {
        *(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0xB8) + 0x6) = 1;
    }
loc_0027A957:
loc_0027A95B:
    if (*(uint64_t *)(v_stack_p8 + 0x38) == 0) goto loc_0027A992;
    if (((*(uint32_t *)(v_stack_p8)) & (0x1000ULL)) == 0) goto loc_0027B2DE;
    if ((*(uint64_t *)(v_stack_p8 + 0x38)) != ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) goto loc_0027B2E7;
loc_0027A98A:
    *(uint64_t *)(v_stack_p8 + 0x38) = 0;
loc_0027A992:
    local_rsi = 5;
    if (0 != 5) {
        local_rsi = v_stack_pD8;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (1)) == 0) goto loc_0027A8BE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (4)) != 0) goto loc_0027B07B;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x9))) != 17) goto loc_0027B173;
    result = MiLockWorkingSetExclusiveAtDpc(*(uint64_t *)(v_stack_p8 + 0x20), *(uint64_t *)(v_stack_p8 + 0x38), Arg3, 1);
loc_0027A9CC:
    goto loc_0027A8BE;
loc_0027A9D4:
    if (result != (v_rip + 1761829)) goto loc_0027B67D;
    Arg2 = (*(uint64_t *)(v_stack_p8 + 0xB8)) + (48);
    v_stack_p20 = v_rip + 2237790;
    a4 = 0;
    Arg3 = 0;
    result = MiAgeTrimListsTail(v_stack_p8, Arg2, Arg3, a4);
    goto loc_0027A8A0;
loc_0027AA0E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (4)) == 0) goto loc_0027AC0C;
    local_rsi = (5) >> (9);
    local_rsi = (local_rsi) & ((uint32_t)(*(uint32_t *)(v_stack_p8)));
    local_rsi = (local_rsi) + (Arg2);
    v_stack_pD8 = local_rsi;
    if (5 != 0) goto loc_0027AAC1;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027AD69;
    Arg2 = (v_stack_p40) + (176);
loc_0027AA7F:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x8) = Arg2;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8) = 0;
    if (((*(uint8_t *)(v_rip + 0xD4C067)) & (33)) != 0) goto loc_0027B063;
loc_0027AAA5:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_0027ABEF;
    result = KxWaitForLockOwnerShip(*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)), a4);
    goto loc_0027ABE5;
loc_0027AAC1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xB8)))) & (15)) != 0) goto loc_0027AB1C;
    if (5 < 0) goto loc_0027AB1C;
    if (5 > 0) goto loc_0027AB1C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_0027B69D;
loc_0027AB1C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xB8)))) & (15)) == 0) goto loc_0027AB45;
    if (5 < 0) goto loc_0027AB45;
    if (5 <= 0) goto loc_0027B438;
loc_0027AB45:
    if (5 < 0) goto loc_0027AB7F;
    if (5 > 0) goto loc_0027AB7F;
    if ((((uint8_t)(*(uint64_t *)(5))) & (1)) == 0) goto loc_0027AB7F;
    Arg1 = ((((uint8_t)(*(uint64_t *)(5))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(5))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0027ADFC;
loc_0027AB7F:
loc_0027AB89:
    if ((((uint8_t)(*(uint64_t *)(5))) & (1)) == 0) goto loc_0027ABCE;
    result = (*(uint64_t *)(5)) >> (60);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0027B09F;
    Arg1 = (*(uint64_t *)(5)) & (local_rsi);
    Arg1 = (Arg1) | (result);
    if (((*(uint64_t *)(v_rip + 0xD4BECD)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD4BECD)) & (0x2000000ULL)) != 0) goto loc_0027AB89;
loc_0027ABCE:
loc_0027ABDE:
loc_0027ABE5:
loc_0027ABEF:
    if (((*(uint32_t *)(v_stack_pD0)) & (0x1000ULL)) == 0) goto loc_0027AE6A;
    if (v_stack_pD8 != 0) goto loc_0027AE73;
loc_0027AC08:
    *(uint64_t *)(v_stack_pD0 + 0x38) = 5;
loc_0027AC0C:
    if (5 < 2) goto loc_0027AC88;
    if (5 > 2) goto loc_0027AC88;
    if ((((uint8_t)(*(uint64_t *)(5))) & (1)) == 0) goto loc_0027AC88;
    Arg1 = ((((uint8_t)(*(uint64_t *)(5))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(5))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0027AC88;
    if (((*(uint64_t *)(v_rip + 0xD4BE37)) & (0x600000ULL)) == 0) goto loc_0027AC88;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0027AC88;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) != 0) {
        result = 5;
        result = (result) >> (3);
        result = (uint32_t)((result) & (511));
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8);
    }
    local_rdi = (result) << (25);
    local_rbx = (5) << (25);
    local_rbx = (local_rbx) - (local_rdi);
    Arg2 = (local_rbx) >> (16);
    result = MiWalkPageTablesRecursively(v_stack_pD0, Arg2, (uint32_t)(v_stack_pE0) - 1, a4);
    v_stack_pD8 = (uint32_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x4)))) & (3)) != 0) goto loc_0027AD97;
    if (((uint32_t)(result)) < 4) goto loc_0027B4DF;
    result = (local_rbx + 268435456) >> (16);
    if ((*(uint64_t *)(v_stack_pD0 + (int32_t)((uint32_t)((uint32_t)(v_stack_pE0))) * 8 + 0x58)) < result) goto loc_0027B638;
    Arg1 = (*(uint64_t *)(v_stack_pD0 + (int32_t)((uint32_t)((uint32_t)(v_stack_pE0))) * 8 + 0x58)) >> (9);
    local_r13 = (5) & (Arg1);
    local_r13 = (local_r13) + (0);
    *(uint64_t *)(v_stack_p38) = local_r13;
    if ((uint32_t)((uint32_t)(v_stack_pE0)) == 0) goto loc_0027AD42;
loc_0027AD2A:
    result = (local_r13) << (25);
    result = (result) - (local_rdi);
    result = (result) >> (16);
    *(uint64_t *)(v_stack_p38 - 0x8) = result;
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(v_stack_pE0)))) - (1);
    if (condition_is_not_equal) goto loc_0027AD2A;
loc_0027AD42:
    v_stack_pE8 = 1;
    local_r15 = 0;
    goto loc_0027977E;
loc_0027AD69:
    if (((uint8_t)(result)) == 7) goto loc_0027B205;
    if (((uint8_t)(result)) == 5) goto loc_0027B7DB;
loc_0027AD7E:
    Arg2 = (v_rip + 12262841 + 3 * 8) + (0x3280ULL);
    goto loc_0027AA7F;
loc_0027AD97:
    if ((((uint8_t)(Arg2)) & (28)) != 0) goto loc_0027ADCB;
    result = (1 + 268435456) >> (16);
    if ((*(uint64_t *)(v_stack_pD0 + (int32_t)((uint32_t)((uint32_t)(v_stack_pE0))) * 8 + 0x58)) < result) goto loc_0027ADCB;
    if ((uint32_t)((uint32_t)(v_stack_pE0)) != 0) {
        result = (uint8_t)((uint32_t)(v_stack_pE0));
        result = (uint32_t)((result) << (2));
        result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
        *(uint64_t *)(v_stack_pD0 + 0x48) = local_r13;
        result = (uint32_t)((result) & (28));
        result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
        *(uint32_t *)(v_stack_pD0 + 0x4) = (uint32_t)(result);
    }
    local_r15 = 0;
loc_0027ADCE:
    v_stack_pE8 = 1;
    goto loc_0027977E;
loc_0027ADFC:
    if (((*(uint64_t *)(v_rip + 0xD4BC81)) & (0x600000ULL)) == 0) goto loc_0027AB7F;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0027AB7F;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0027AE5B;
    result = (local_r13) >> (3);
    result = (uint32_t)((result) & (511));
    local_rbx = 1;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (1) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
loc_0027AE5B:
    goto loc_0027AB7F;
loc_0027AE6A:
    if (((uint32_t)((uint32_t)(result))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) goto loc_0027AF25;
loc_0027AE73:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xB8)))) & (15)) == 0) goto loc_0027AEAF;
loc_0027AE8D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xB8)))) & (15)) != 0) goto loc_0027AFA9;
loc_0027AE9C:
    goto loc_0027AC08;
loc_0027AEAF:
    if (((uint32_t)((uint32_t)(result))) < 0) goto loc_0027AE8D;
    if (((uint32_t)((uint32_t)(result))) > 0) goto loc_0027AE8D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0027AE8D;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (3));
    local_rsi = (uint32_t)((local_rsi) & (511));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_rsi * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0027B02D;
    if (!sign_flag) goto loc_0027B61C;
    if (((*(uint8_t *)(v_rip + 0xD4BBF0)) & (1)) != 0) goto loc_0027B6E0;
loc_0027AF1C:
    local_rdi = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_rsi * 4) = 0;
    goto loc_0027AC08;
loc_0027AF25:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027B049;
loc_0027AF46:
    local_rdi = 0;
loc_0027AF48:
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x20)) + 40000) + (48);
    if (((*(uint8_t *)(v_rip + 0xD4BBAD)) & (1)) != 0) goto loc_0027B00A;
loc_0027AF5F:
    if (*(uint64_t *)(local_rbx) != 0) goto loc_0027AF84;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_0027AC08;
    result = KxWaitForLockChainValid(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), v_stack_p40, a4);
loc_0027AF84:
    *(uint64_t *)(local_rbx) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rbx + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rbx + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0027AC08;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rbx + 0x8), v_stack_p40, a4);
    goto loc_0027AC08;
loc_0027AFA9:
    if (local_rsi < 0) goto loc_0027AE9C;
    if (local_rsi > 0) goto loc_0027AE9C;
    local_rsi = (local_rsi) - (0);
    local_rsi = (local_rsi) >> (3);
    result = ((uint32_t)((uint32_t)(local_rsi + local_rsi * 1))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + local_rsi * 1))) & (31));
    result = (uint32_t)((3) << ((uint8_t)(Arg1)));
    result = (uint32_t)(~(result));
    goto loc_0027AC08;
loc_0027B00A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92E48))) != 0) goto loc_0027AF5F;
    result = KiReleaseQueuedSpinLockInstrumented(local_rbx, v_stack_pC8, v_stack_p40, a4);
    goto loc_0027AC08;
loc_0027B02D:
    if (((*(uint8_t *)(v_rip + 0xD4BAD2)) & (1)) != 0) goto loc_0027B741;
loc_0027B03A:
    goto loc_0027AC08;
loc_0027B049:
    if (((uint8_t)(result)) == 7) goto loc_0027B4D5;
    if (((uint8_t)(result)) == 5) goto loc_0027B7E3;
    goto loc_0027AF46;
loc_0027B063:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92DEF))) != 0) goto loc_0027AAA5;
    result = KiAcquireQueuedSpinLockInstrumented(local_rbx, v_stack_pC8, v_stack_p40, a4);
    goto loc_0027ABE5;
loc_0027B07B:
    if (((uint8_t)(local_rbx)) == 17) goto loc_0027B166;
    result = MiLockWorkingSetShared((uint32_t)(v_stack_pE0), v_stack_pC8, v_stack_p40, a4);
    goto loc_0027A8BE;
loc_0027B094:
    goto loc_0027A95B;
loc_0027B09F:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_0027B270;
    local_rdi = (local_rbx) | (result);
    if (((*(uint64_t *)(v_rip + 0xD4B9C6)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_0027B640;
loc_0027B0D6:
    if (((*(uint64_t *)(v_rip + 0xD4B9C6)) & (0x2000000ULL)) == 0) { local_rbx = local_rdi; }
    goto loc_0027AB89;
loc_0027B0F5:
    if (local_rbx != (v_rip + 1011860)) goto loc_0027B29A;
    result = MiOutSwapWorkingSetPte(v_stack_pD0, v_stack_pC8, v_stack_p40, a4);
    v_stack_pD8 = (uint32_t)(result);
    goto loc_0027A422;
loc_0027B11B:
    if (result != (v_rip + 1759966)) goto loc_0027B700;
    Arg2 = (*(uint64_t *)(v_stack_pD0 + 0xB8)) + (48);
    v_stack_p20 = v_rip + 2235927;
    a4 = 0;
    Arg3 = 0;
    result = MiAgeTrimListsTail(v_stack_pD0, Arg2, Arg3, a4);
    goto loc_0027A957;
loc_0027B158:
    if (0 != 4) goto loc_0027A8EF;
    goto loc_0027A9A1;
loc_0027B166:
    result = MiLockWorkingSetSharedAtDpc(v_stack_pD0, Arg2, Arg3, a4);
    goto loc_0027A8BE;
loc_0027B173:
    result = MiLockWorkingSetExclusive(v_stack_pD0, Arg2, Arg3, a4);
    goto loc_0027A9CC;
loc_0027B180:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x30))))) & (112));
    if (((uint8_t)(Arg1)) == 48) goto loc_0027B1BD;
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x30))))) & (112));
    if (((uint8_t)(Arg1)) == 16) goto loc_0027B1BD;
    if (((uint8_t)(Arg1)) >= 16) goto loc_0027B1B1;
    if (((uint8_t)(Arg1)) < 16) goto loc_0027B1BD;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x30))))) & (0x180000ULL));
    if (((uint32_t)(result)) >= 0x100000ULL) goto loc_0027B1BD;
loc_0027B1B1:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x30))) & (112));
    if (((uint8_t)(Arg2)) != 80) goto loc_00279B96;
loc_0027B1BD:
    local_rbp = (uint32_t)(((uint32_t)(v_stack_pE0)) + 1);
    local_rdi = (*(uint8_t *)(0 + 0x21)) << (32);
    local_rdi = (local_rdi) | ((uint32_t)(*(uint32_t *)(0 + 0x1C)));
    local_rdi = (local_rdi) << (12);
    local_rdi = (local_rdi) | (0xFFFULL);
    if ((uint8_t)(local_rbp) != 0) goto loc_0027B1F0;
    result = MiPeriodicGoodCitizen(v_stack_pD0, local_r13, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_00279B96;
loc_0027B1F0:
    result = MiGetNextVad(0, local_r13, Arg3, a4);
    if (result != 0) goto loc_0027B180;
    goto loc_00279B96;
loc_0027B205:
    goto loc_0027AD7E;
loc_0027B20F:
    if (*(uint64_t *)(v_stack_pD0 + 0x38) == 0) goto loc_00279930;
    result = (uint32_t)((result) | (2));
    *(uint32_t *)(1) = (uint32_t)(result);
    if (condition_is_above_or_equal) goto loc_0027B5F7;
    if ((*(uint64_t *)(v_stack_pD0 + 0x38)) != local_rdi) goto loc_0027B5F7;
loc_0027B237:
    *(uint64_t *)(v_stack_pD0 + 0x38) = 0;
    goto loc_00279930;
loc_0027B240:
loc_0027B247:
    if ((*(uint64_t *)(v_stack_pD0 + 0x38)) != local_rdi) goto loc_0027B247;
    if ((*(uint64_t *)(v_stack_pD0 + 0x38)) >= local_rdi) goto loc_0027A6C9;
    result = KiRemoveSystemWorkPriorityKick(1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD0 + 0x38))))), *(uint64_t *)(v_stack_pD0 + 0x38), a4);
    goto loc_0027A6C9;
loc_0027B270:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xD4A034)) & ((uint32_t)(local_rbp))) == 0) goto loc_0027B4AE;
loc_0027B27E:
loc_0027B280:
    if (condition_is_below) goto loc_0027B270;
    goto loc_0027AB89;
loc_0027B29A:
    result = guard_dispatch_icall(1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD0 + 0x38))))), *(uint64_t *)(v_stack_pD0 + 0x38), a4);
    v_stack_pD8 = (uint32_t)(result);
    goto loc_0027A422;
loc_0027B2AD:
    if ((*(uint64_t *)(v_stack_pD0 + 0xA8)) == (v_rip + 2300556)) goto loc_002798DA;
    goto loc_002798E0;
loc_0027B2C9:
    goto loc_00279F65;
loc_0027B2DE:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD0 + 0x38)))))) == (*(uint64_t *)(24 + 0x1 * 1 + 0x9C40))) goto loc_0027B371;
loc_0027B2E7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0xB8)))) & (15)) == 0) goto loc_0027B31C;
loc_0027B2F1:
loc_0027B2FB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0xB8)))) & (15)) != 0) goto loc_0027B3A1;
loc_0027B309:
    goto loc_0027A98A;
loc_0027B31C:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD0 + 0x38)))))) < 2) goto loc_0027B2FB;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD0 + 0x38)))))) > 1) goto loc_0027B2FB;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0027B2F1;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD0 + 0x38)))))) >> (3);
    Arg2 = (uint32_t)((Arg2) & (511));
    result = ExReleaseSpinLockRegardlessFromDpcLevel(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + Arg2 * 4, Arg2, *(uint64_t *)(v_stack_pD0 + 0x38), 0);
    goto loc_0027A98A;
loc_0027B371:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027B417;
loc_0027B38D:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x20))) + (0x9C40ULL);
    Arg1 = (Arg1) + (48);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, 48, *(uint64_t *)(v_stack_pD0 + 0x38), 0);
    goto loc_0027A98A;
loc_0027B3A1:
    if (48 < 2) goto loc_0027B309;
    if (48 > Arg1) goto loc_0027B309;
    Arg2 = (48) - (2);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (31));
    Arg3 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    Arg3 = (uint32_t)(~(Arg3));
    result = ((uint32_t)((uint32_t)(Arg2))) >> (5);
    goto loc_0027A98A;
loc_0027B3FB:
    if ((*(uint64_t *)(v_stack_pD0 + 0xA8)) == (v_rip + 2300222)) goto loc_00279E18;
    goto loc_00279E1E;
loc_0027B417:
    if (((uint8_t)(v_rip + 2300222)) == 7) goto loc_0027B524;
    Arg2 = 72;
    if (((uint8_t)(v_rip + 2300222)) == 5) { Arg2 = 0; }
    goto loc_0027B38D;
loc_0027B42F:
    *(uint64_t *)(v_stack_pD0 + 0x50) = 0;
    goto loc_002797C0;
loc_0027B438:
    Arg1 = (local_r13) - (0);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    local_r15 = ((uint32_t)((uint32_t)(Arg1))) >> (5);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (31));
    local_rbp = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    local_rdi = (uint32_t)((2) << ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    local_rdi = (uint32_t)(~(local_rdi));
loc_0027B485:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB16D5 + 0x266C + local_r15 * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0027B55A;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB16D5 + 0x266C + local_r15 * 4)))));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_rdi)));
    if (condition_is_equal) goto loc_0027ABDE;
    goto loc_0027B485;
loc_0027B4AE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4B604)))) & (64)) == 0) goto loc_0027B27E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB16D5 + 0x266C + local_r15 * 4)))))), 0);
    if ((uint8_t)(result) == 0) goto loc_0027B27E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB16D5 + 0x266C + local_r15 * 4)))))), 0);
    goto loc_0027B280;
loc_0027B4D5:
    goto loc_0027AF46;
loc_0027B4DF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pD0)))) & (4)) == 0) goto loc_0027A3E2;
    result = MiReacquireHigherPageTableLock(v_stack_pD0, local_r13, (uint32_t)((uint32_t)(local_rbp)), 0);
    if ((uint32_t)(result) == 0) goto loc_0027A3E2;
    local_r15 = 0;
    local_rsi = 0;
    if (((uint32_t)(result)) != 2) { local_rsi = (uint32_t)(result); }
    v_stack_pD8 = (uint32_t)(local_rsi);
    goto loc_0027ADCE;
loc_0027B518:
    goto loc_00279829;
loc_0027B524:
    Arg1 = (v_stack_pD0) + (0x9C40ULL);
    Arg1 = (Arg1) + (24);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, 24, 0 + 192, 0);
    goto loc_0027A98A;
loc_0027B53D:
    local_rbx = (local_rbx) + 1;
    local_rdi = (local_rdi) + (8);
    a4 = 0;
    goto loc_0027A152;
loc_0027B54C:
    local_rbp = (local_rbp) + (0xDF80ULL);
    result = (uint32_t)((result) + 1);
    goto loc_0027A144;
loc_0027B55A:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_0027B720;
    Arg2 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(0 + 192)));
    Arg3 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0 + 192))));
    if (condition_is_equal) { Arg3 = (uint32_t)(Arg2); }
    goto loc_0027B485;
loc_0027B580:
    if ((*(uint64_t *)(v_stack_pD0 + 0xA8)) == (v_rip + 2299833)) goto loc_0027A873;
    goto loc_0027A878;
loc_0027B5A0:
    if (Arg2 != (v_rip + 2066761)) goto loc_0027B761;
    result = MiDeleteVaTail(Arg1, Arg2, Arg3, a4);
loc_0027B5B5:
    goto loc_0027990A;
loc_0027B5BC:
    if (result != (v_rip + 2066733)) goto loc_0027B76E;
    result = MiDeleteVaTail(v_stack_pD0, Arg2, Arg3, a4);
    goto loc_00279E48;
loc_0027B5DB:
    if ((*(uint64_t *)(v_stack_pD0 + 0xA8)) == (v_rip + 2299742)) goto loc_0027A925;
    goto loc_0027A92A;
loc_0027B5F7:
    result = MiUnlockPageTable(*(uint64_t *)(v_stack_pD0 + 0x20), Arg3, Arg3, a4);
    goto loc_0027B237;
loc_0027B608:
    goto loc_0027994B;
loc_0027B61C:
    local_rdi = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(local_rdi + 16, *(uint64_t *)(v_stack_pD0 + 0x20), 256, a4);
loc_0027B638:
    goto loc_0027AD42;
loc_0027B640:
    result = (uint8_t)((0) & (33));
    if (((uint8_t)(result)) != 1) goto loc_0027B0D6;
    result = (*(uint64_t *)(v_stack_pD0 + 0x20)) + (local_rdi + 16);
    if (local_r13 < result) goto loc_0027B0D6;
    result = MiCheckLinearProtectedPteAccessedBit(local_r13, 0, 128, a4);
    goto loc_0027B0D6;
loc_0027B67D:
    if (result != (v_rip + 2066540)) goto loc_0027B77A;
    result = MiDeleteVaTail(v_stack_pD0, 0, 128, a4);
loc_0027B695:
    goto loc_0027A8A0;
loc_0027B69D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (3));
    result = (uint32_t)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pD0 + result * 4, 0, 128, a4);
    goto loc_0027ABE5;
loc_0027B6B6:
    v_stack_pD8 = 5;
    local_r15 = 0;
    goto loc_0027A827;
loc_0027B6E0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92772))) != 0) goto loc_0027AF1C;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_pD0 + result * 4, v_stack_pC8, 128, a4);
    goto loc_0027AC08;
loc_0027B700:
    if (result != (v_rip + 2066409)) goto loc_0027B7A1;
    result = MiDeleteVaTail(v_stack_pD0, v_stack_pC8, 128, a4);
loc_0027B718:
    goto loc_0027A957;
loc_0027B720:
    local_r12 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD49B82)) & ((uint32_t)(local_r12))) == 0) goto loc_0027B784;
loc_0027B72C:
loc_0027B72E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15))))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0027B720;
    goto loc_0027B485;
loc_0027B741:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92711))) != 0) goto loc_0027B03A;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    goto loc_0027AC08;
loc_0027B761:
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    goto loc_0027B5B5;
loc_0027B76E:
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    goto loc_00279E48;
loc_0027B77A:
    result = guard_dispatch_icall((uint32_t)((uint32_t)(result)), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    goto loc_0027B695;
loc_0027B784:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4B32E)))) & (64)) == 0) goto loc_0027B72C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(result)), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    if ((uint8_t)(result) == 0) goto loc_0027B72C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    goto loc_0027B72E;
loc_0027B7A1:
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_r12)), v_stack_pC8, (uint32_t)(*(uint32_t *)(local_r15)), a4);
    goto loc_0027B718;
loc_0027B7AB:
    a4 = ((uint32_t)((uint32_t)(v_stack_pE0)) != 0) ? 1 : 0;
    a4 = (uint32_t)((a4) + (2));
    result = MiMarkResumptionPoint(v_stack_pD0, 5, (uint32_t)((uint32_t)((uint32_t)(v_stack_pE0))), a4);
    goto loc_0027A821;
loc_0027B7CB:
    goto loc_0027A4AD;
loc_0027B7D3:
    goto loc_00279F63;
loc_0027B7DB:
    goto loc_0027AD7E;
loc_0027B7E3:
    local_rdi = 0;
    goto loc_0027AF48;
loc_0027B7EC:
    goto loc_0027A47F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rbp*8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002796C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
