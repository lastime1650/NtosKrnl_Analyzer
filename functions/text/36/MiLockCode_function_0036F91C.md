# MiLockCode

- RVA: `0x0036F91C`–`0x003701AE` (길이 `2,194` bytes)
- VA: `0x000000014036F91C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007A6AC`
- 디코드: `522`개 명령, `2,194/2,194` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0036F96F` → [MI_IS_PHYSICAL_ADDRESS](../23/MI_IS_PHYSICAL_ADDRESS_function_0023B3A0.md) (function, `0x0023B3A0`)
- `0x0036F97F` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0036F9BF` → [MiPrefetchDriverPages](../../page/9F/MiPrefetchDriverPages_function_009F6A50.md) (function, `0x009F6A50`)
- `0x0036F9D2` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0036FA14` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x0036FA91` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x0036FB20` → [MiReferenceDriverPage](../37/MiReferenceDriverPage_function_003701B4.md) (function, `0x003701B4`)
- `0x0036FB3A` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x0036FC51` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0036FC5C` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0036FC6C` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x0036FC7F` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0036FCB2` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0036FCF2` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0036FCFE` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0036FD15` → [MiAllocateDriverPage](../../page/A8/MiAllocateDriverPage_function_00A80128.md) (function, `0x00A80128`)
- `0x0036FD28` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0036FD48` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0036FD63` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x0036FD83` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x0036FDA6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0036FDB6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0036FDDD` → [MiRemoveSystemImagePage](../48/MiRemoveSystemImagePage_function_0048B398.md) (function, `0x0048B398`)
- `0x0036FE14` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x0036FE42` → [MiBetterDriverPageNeeded](../48/MiBetterDriverPageNeeded_function_004819E0.md) (function, `0x004819E0`)
- `0x0036FEAD` → [MiTradeActivePage](../37/MiTradeActivePage_function_00374424.md) (function, `0x00374424`)
- `0x0036FEC9` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x0036FED1` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x0036FF2A` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036FF44` → [MiWriteValidPteVolatile](../29/MiWriteValidPteVolatile_function_00292B60.md) (function, `0x00292B60`)
- `0x0036FF52` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x0036FF6F` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x0036FF7C` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x0036FFBB` → [MiCopyOnWrite](MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x0036FFE2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0036FFF2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00370016` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00370021` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00370084` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00370089` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00370098` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0037009D` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x003700AF` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003700BA` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x003700C7` → [MiCopyOnWriteCheckConditions](../2A/MiCopyOnWriteCheckConditions_function_002A750C.md) (function, `0x002A750C`)
- `0x003700DE` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x003700E3` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x003700EF` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x00370108` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0037010D` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0037013F` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0037014C` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00370151` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00370160` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00370165` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00370187` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x003701A8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiLockRegistryRecoverySection](../../page/7F/MiLockRegistryRecoverySection_function_007F8C10.md) at `0x007F8C6C`
- [MiLockImageSection](../../page/A4/MiLockImageSection_function_00A48D78.md) at `0x00A48DE9`
- [MmResetDriverPaging](../../page/A4/MmResetDriverPaging_function_00A4ADB0.md) at `0x00A4AE9A`
- [MiHandleDriverNonPagedSections](../../page/A4/MiHandleDriverNonPagedSections_function_00A4AEA8.md) at `0x00A4AFA6`
- [MiHandleDriverNonPagedSections](../../page/A4/MiHandleDriverNonPagedSections_function_00A4AEA8.md) at `0x00A4B059`
- [MiDisablePagingOfDriver](../../page/A4/MiDisablePagingOfDriver_function_00A4B074.md) at `0x00A4B100`
- [MmLockPreChargedPagedPool](../../page/AD/MmLockPreChargedPagedPool_function_00AD6E20.md) at `0x00AD6E53`

### Static image references
- `0x0036F984` → RVA `0x00E37E40` (`.data`; read)
- `0x0036F98E` → RVA `0x00E380C0` (`.data`; read)
- `0x0036F9F9` → RVA `0x00E30088` (`.data`; read)
- `0x0036FA7E` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0036FC91` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0036FD98` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0036FEBB` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0036F9BF` → [MiPrefetchDriverPages](../../page/9F/MiPrefetchDriverPages_function_009F6A50.md) (`.text` → `PAGE`)
  - `0x0036FD15` → [MiAllocateDriverPage](../../page/A8/MiAllocateDriverPage_function_00A80128.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0036FDF8` → [sub_006E3CBA](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)
  - `0x0036FDFE` → [sub_006E3CBA + 0xF](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)
  - `0x0036FF4C` → [sub_006E3CBA + 0x6F](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)
  - `0x0036FF75` → [sub_006E3CBA + 0x6F](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)
  - `0x003700CD` → [sub_006E3CBA + 0x40](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)
  - `0x003700D5` → [sub_006E3CBA + 0x51](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)
  - `0x003700EA` → [sub_006E3CBA + 0x51](../6E/Unknown_function_006E3CBA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0036F91C  48 8B C4                        mov rax, rsp
0036F91F  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0036F923  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0036F927  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0036F92B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0036F92F  53                              push rbx
0036F930  55                              push rbp
0036F931  56                              push rsi
0036F932  57                              push rdi
0036F933  41 54                           push r12
0036F935  41 55                           push r13
0036F937  41 56                           push r14
0036F939  41 57                           push r15
0036F93B  48 83 EC 78                     sub rsp, 0x78
0036F93F  49 8B E8                        mov rbp, r8
0036F942  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
0036F94C  4C 8B FA                        mov r15, rdx
0036F94F  48 8B F9                        mov rdi, rcx
0036F952  49 8B F4                        mov rsi, r12
0036F955  48 8B DA                        mov rbx, rdx
0036F958  48 C1 E6 19                     shl rsi, 0x19
0036F95C  48 C1 E3 19                     shl rbx, 0x19
0036F960  48 2B DE                        sub rbx, rsi
0036F963  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0036F968  48 C1 FB 10                     sar rbx, 0x10
0036F96C  48 8B CB                        mov rcx, rbx
0036F96F  E8 2C BA EC FF                  call 0x14023b3a0
0036F974  85 C0                           test eax, eax
0036F976  0F 85 B4 06 00 00               jne 0x140370030
0036F97C  48 8B CB                        mov rcx, rbx
0036F97F  E8 FC F2 F1 FF                  call 0x14028ec80
0036F984  48 8D 0D B5 84 AC 00            lea rcx, [rip + 0xac84b5]
0036F98B  83 F8 05                        cmp eax, 5
0036F98E  4C 8D 35 2B 87 AC 00            lea r14, [rip + 0xac872b]
0036F995  4C 0F 45 F1                     cmovne r14, rcx
0036F999  33 C9                           xor ecx, ecx
0036F99B  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0036F9A0  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0036F9A4  8D 51 02                        lea edx, [rcx + 2]
0036F9A7  48 85 FF                        test rdi, rdi
0036F9AA  74 0D                           je 0x14036f9b9
0036F9AC  84 97 B8 00 00 00               test byte ptr [rdi + 0xb8], dl
0036F9B2  0F 44 CA                        cmove ecx, edx
0036F9B5  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0036F9B9  48 8B D5                        mov rdx, rbp
0036F9BC  49 8B CF                        mov rcx, r15
0036F9BF  E8 8C 70 68 00                  call 0x1409f6a50
0036F9C4  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
0036F9CA  49 8B CE                        mov rcx, r14
0036F9CD  33 ED                           xor ebp, ebp
0036F9CF  45 33 ED                        xor r13d, r13d
0036F9D2  E8 19 D2 F0 FF                  call 0x14027cbf0
0036F9D7  40 8A F8                        mov dil, al
0036F9DA  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0036F9DE  44 8D 5D 01                     lea r11d, [rbp + 1]
0036F9E2  E9 BA 01 00 00                  jmp 0x14036fba1
0036F9E7  48 0F BA E3 09                  bt rbx, 9
0036F9EC  0F 82 E0 06 00 00               jb 0x1403700d2
0036F9F2  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0036F9F6  49 8B D4                        mov rdx, r12
0036F9F9  48 8B 0D 88 06 AC 00            mov rcx, qword ptr [rip + 0xac0688]
0036FA00  33 FF                           xor edi, edi
0036FA02  48 C1 E8 2B                     shr rax, 0x2b
0036FA06  25 FF 03 00 00                  and eax, 0x3ff
0036FA0B  4C 8B 14 C1                     mov r10, qword ptr [rcx + rax*8]
0036FA0F  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0036FA14  E8 27 6B FA FF                  call 0x140316540
0036FA19  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0036FA1E  8A D8                           mov bl, al
0036FA20  49 83 F8 FF                     cmp r8, -1
0036FA24  0F 85 1A 06 00 00               jne 0x140370044
0036FA2A  BA 02 00 00 00                  mov edx, 2
0036FA2F  84 94 24 D8 00 00 00            test byte ptr [rsp + 0xd8], dl
0036FA36  75 0F                           jne 0x14036fa47
0036FA38  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0036FA3B  66 41 3B C3                     cmp ax, r11w
0036FA3F  0F 85 A2 00 00 00               jne 0x14036fae7
0036FA45  EB 0C                           jmp 0x14036fa53
0036FA47  8A C3                           mov al, bl
0036FA49  24 0F                           and al, 0xf
0036FA4B  3C 09                           cmp al, 9
0036FA4D  0F 84 94 00 00 00               je 0x14036fae7
0036FA53  48 0F BA 66 28 35               bt qword ptr [rsi + 0x28], 0x35
0036FA59  0F 82 88 00 00 00               jb 0x14036fae7
0036FA5F  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0036FA63  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
0036FA6D  48 23 C1                        and rax, rcx
0036FA70  49 3B C3                        cmp rax, r11
0036FA73  75 72                           jne 0x14036fae7
0036FA75  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0036FA78  66 41 3B C3                     cmp ax, r11w
0036FA7C  75 69                           jne 0x14036fae7
0036FA7E  48 F7 05 FF 6F C5 00 00 40 00 00  test qword ptr [rip + 0xc56fff], 0x4000
0036FA89  74 12                           je 0x14036fa9d
0036FA8B  45 33 C0                        xor r8d, r8d
0036FA8E  48 8B CE                        mov rcx, rsi
0036FA91  E8 8A 59 F1 FF                  call 0x140285420
0036FA96  85 C0                           test eax, eax
0036FA98  75 4D                           jne 0x14036fae7
0036FA9A  8D 50 02                        lea edx, [rax + 2]
0036FA9D  48 F7 05 E0 6F C5 00 00 00 02 00  test qword ptr [rip + 0xc56fe0], 0x20000
0036FAA8  0F 85 CF 02 00 00               jne 0x14036fd7d
0036FAAE  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0036FAB8  49 8B CC                        mov rcx, r12
0036FABB  48 C1 E9 09                     shr rcx, 9
0036FABF  48 23 C8                        and rcx, rax
0036FAC2  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0036FACC  48 8B C0                        mov rax, rax
0036FACF  48 8B 04 01                     mov rax, qword ptr [rcx + rax]
0036FAD3  A8 42                           test al, 0x42
0036FAD5  0F 95 C1                        setne cl
0036FAD8  84 54 24 34                     test byte ptr [rsp + 0x34], dl
0036FADC  0F 94 C0                        sete al
0036FADF  84 C8                           test al, cl
0036FAE1  0F 84 C8 01 00 00               je 0x14036fcaf
0036FAE7  45 33 FF                        xor r15d, r15d
0036FAEA  45 8D 77 01                     lea r14d, [r15 + 1]
0036FAEE  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
0036FAF5  0F 82 93 01 00 00               jb 0x14036fc8e
0036FAFB  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0036FB00  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0036FB05  49 83 F8 FF                     cmp r8, -1
0036FB09  0F 85 F4 02 00 00               jne 0x14036fe03
0036FB0F  F6 84 24 D8 00 00 00 02         test byte ptr [rsp + 0xd8], 2
0036FB17  0F 85 A3 02 00 00               jne 0x14036fdc0
0036FB1D  48 8B CE                        mov rcx, rsi
0036FB20  E8 8F 06 00 00                  call 0x1403701b4
0036FB25  4C 8B BC 24 C8 00 00 00         mov r15, qword ptr [rsp + 0xc8]
0036FB2D  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
0036FB30  48 0F BA E0 0A                  bt rax, 0xa
0036FB35  72 0B                           jb 0x14036fb42
0036FB37  48 8B CE                        mov rcx, rsi
0036FB3A  E8 91 12 00 00                  call 0x140370dd0
0036FB3F  48 8B F8                        mov rdi, rax
0036FB42  49 8B 0F                        mov rcx, qword ptr [r15]
0036FB45  48 0F BA E1 0B                  bt rcx, 0xb
0036FB4A  0F 82 E1 03 00 00               jb 0x14036ff31
0036FB50  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0036FB55  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0036FB5F  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0036FB64  48 85 FF                        test rdi, rdi
0036FB67  0F 85 C4 05 00 00               jne 0x140370131
0036FB6D  40 8A 7C 24 30                  mov dil, byte ptr [rsp + 0x30]
0036FB72  49 83 C7 08                     add r15, 8
0036FB76  4C 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r15
0036FB7E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0036FB83  41 BB 01 00 00 00               mov r11d, 1
0036FB89  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
0036FB93  4C 3B BC 24 D0 00 00 00         cmp r15, qword ptr [rsp + 0xd0]
0036FB9B  0F 87 5B 04 00 00               ja 0x14036fffc
0036FBA1  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
0036FBAB  48 BB F8 FF FF FF 7F 00 00 00   movabs rbx, 0x7ffffffff8
0036FBB5  4D 85 ED                        test r13, r13
0036FBB8  0F 84 8F 01 00 00               je 0x14036fd4d
0036FBBE  49 F7 C7 FF 0F 00 00            test r15, 0xfff
0036FBC5  0F 84 6E 01 00 00               je 0x14036fd39
0036FBCB  49 8B 1F                        mov rbx, qword ptr [r15]
0036FBCE  4D 8B E7                        mov r12, r15
0036FBD1  49 C1 E4 19                     shl r12, 0x19
0036FBD5  4C 2B E6                        sub r12, rsi
0036FBD8  49 C1 FC 10                     sar r12, 0x10
0036FBDC  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0036FBE1  41 84 DB                        test r11b, bl
0036FBE4  74 5C                           je 0x14036fc42
0036FBE6  48 8B C3                        mov rax, rbx
0036FBE9  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0036FBF3  48 C1 E8 0C                     shr rax, 0xc
0036FBF7  48 23 C1                        and rax, rcx
0036FBFA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0036FBFF  48 8D 34 40                     lea rsi, [rax + rax*2]
0036FC03  48 C1 E6 04                     shl rsi, 4
0036FC07  48 8B C2                        mov rax, rdx
0036FC0A  48 03 F0                        add rsi, rax
0036FC0D  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0036FC11  48 0F BA E0 28                  bt rax, 0x28
0036FC16  72 0D                           jb 0x14036fc25
0036FC18  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0036FC1C  48 85 C0                        test rax, rax
0036FC1F  0F 89 6D 03 00 00               jns 0x14036ff92
0036FC25  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0036FC29  48 85 C0                        test rax, rax
0036FC2C  0F 88 B5 01 00 00               js 0x14036fde7
0036FC32  48 0F BA E3 0B                  bt rbx, 0xb
0036FC37  0F 82 B5 FD FF FF               jb 0x14036f9f2
0036FC3D  E9 A5 FD FF FF                  jmp 0x14036f9e7
0036FC42  48 85 ED                        test rbp, rbp
0036FC45  0F 85 FE 04 00 00               jne 0x140370149
0036FC4B  49 8B D5                        mov rdx, r13
0036FC4E  49 8B CE                        mov rcx, r14
0036FC51  E8 6A 72 EA FF                  call 0x140216ec0
0036FC56  40 8A D7                        mov dl, dil
0036FC59  49 8B CE                        mov rcx, r14
0036FC5C  E8 2F DA F0 FF                  call 0x14027d690
0036FC61  45 33 C9                        xor r9d, r9d
0036FC64  45 33 C0                        xor r8d, r8d
0036FC67  49 8B D4                        mov rdx, r12
0036FC6A  33 C9                           xor ecx, ecx
0036FC6C  E8 0F F2 F0 FF                  call 0x14027ee80
0036FC71  85 C0                           test eax, eax
0036FC73  0F 88 18 05 00 00               js 0x140370191
0036FC79  45 33 ED                        xor r13d, r13d
0036FC7C  49 8B CE                        mov rcx, r14
0036FC7F  E8 6C CF F0 FF                  call 0x14027cbf0
0036FC84  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0036FC89  E9 F5 FE FF FF                  jmp 0x14036fb83
0036FC8E  45 03 FE                        add r15d, r14d
0036FC91  44 85 3D 14 56 C5 00            test dword ptr [rip + 0xc55614], r15d
0036FC98  0F 84 FA 00 00 00               je 0x14036fd98
0036FC9E  F3 90                           pause
0036FCA0  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0036FCA4  48 85 C0                        test rax, rax
0036FCA7  0F 89 41 FE FF FF               jns 0x14036faee
0036FCAD  EB DF                           jmp 0x14036fc8e
0036FCAF  48 8B CE                        mov rcx, rsi
0036FCB2  E8 19 E6 F1 FF                  call 0x14028e2d0
0036FCB7  83 F8 09                        cmp eax, 9
0036FCBA  0F 85 27 FE FF FF               jne 0x14036fae7
0036FCC0  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0036FCC5  49 8B 83 38 41 00 00            mov rax, qword ptr [r11 + 0x4138]
0036FCCC  48 85 C0                        test rax, rax
0036FCCF  74 12                           je 0x14036fce3
0036FCD1  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0036FCD6  4D 3B 93 28 41 00 00            cmp r10, qword ptr [r11 + 0x4128]
0036FCDD  0F 83 04 FE FF FF               jae 0x14036fae7
0036FCE3  48 85 ED                        test rbp, rbp
0036FCE6  0F 85 19 04 00 00               jne 0x140370105
0036FCEC  49 8B D5                        mov rdx, r13
0036FCEF  49 8B CE                        mov rcx, r14
0036FCF2  E8 C9 71 EA FF                  call 0x140216ec0
0036FCF7  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
0036FCFB  49 8B CE                        mov rcx, r14
0036FCFE  E8 8D D9 F0 FF                  call 0x14027d690
0036FD03  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
0036FD06  45 33 C0                        xor r8d, r8d
0036FD09  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0036FD0E  48 C1 EA 05                     shr rdx, 5
0036FD12  83 E2 1F                        and edx, 0x1f
0036FD15  E8 0E 04 71 00                  call 0x140a80128
0036FD1A  49 8B CE                        mov rcx, r14
0036FD1D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0036FD22  45 33 ED                        xor r13d, r13d
0036FD25  48 8B D8                        mov rbx, rax
0036FD28  E8 C3 CE F0 FF                  call 0x14027cbf0
0036FD2D  40 8A F8                        mov dil, al
0036FD30  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0036FD34  E9 45 FE FF FF                  jmp 0x14036fb7e
0036FD39  48 85 ED                        test rbp, rbp
0036FD3C  0F 85 3F 03 00 00               jne 0x140370081
0036FD42  49 8B D5                        mov rdx, r13
0036FD45  49 8B CE                        mov rcx, r14
0036FD48  E8 73 71 EA FF                  call 0x140216ec0
0036FD4D  4D 8B EF                        mov r13, r15
0036FD50  49 C1 ED 09                     shr r13, 9
0036FD54  4C 23 EB                        and r13, rbx
0036FD57  49 8B C4                        mov rax, r12
0036FD5A  4C 03 E8                        add r13, rax
0036FD5D  49 8B CE                        mov rcx, r14
0036FD60  49 8B D5                        mov rdx, r13
0036FD63  E8 28 EB EC FF                  call 0x14023e890
0036FD68  41 BB 01 00 00 00               mov r11d, 1
0036FD6E  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
0036FD78  E9 4E FE FF FF                  jmp 0x14036fbcb
0036FD7D  45 33 C0                        xor r8d, r8d
0036FD80  48 8B CE                        mov rcx, rsi
0036FD83  E8 98 56 F1 FF                  call 0x140285420
0036FD88  85 C0                           test eax, eax
0036FD8A  0F 85 57 FD FF FF               jne 0x14036fae7
0036FD90  8D 50 02                        lea edx, [rax + 2]
0036FD93  E9 16 FD FF FF                  jmp 0x14036faae
0036FD98  8B 05 1A 6D C5 00               mov eax, dword ptr [rip + 0xc56d1a]
0036FD9E  A8 40                           test al, 0x40
0036FDA0  0F 84 F8 FE FF FF               je 0x14036fc9e
0036FDA6  E8 E5 F6 F9 FF                  call 0x14030f490
0036FDAB  84 C0                           test al, al
0036FDAD  0F 84 EB FE FF FF               je 0x14036fc9e
0036FDB3  41 8B CF                        mov ecx, r15d
0036FDB6  E8 A5 F6 F9 FF                  call 0x14030f460
0036FDBB  E9 E0 FE FF FF                  jmp 0x14036fca0
0036FDC0  4C 8B BC 24 C8 00 00 00         mov r15, qword ptr [rsp + 0xc8]
0036FDC8  80 E3 0F                        and bl, 0xf
0036FDCB  80 FB 09                        cmp bl, 9
0036FDCE  0F 84 59 FD FF FF               je 0x14036fb2d
0036FDD4  4C 8B C6                        mov r8, rsi
0036FDD7  49 8B D7                        mov rdx, r15
0036FDDA  49 8B CE                        mov rcx, r14
0036FDDD  E8 B6 B5 11 00                  call 0x14048b398
0036FDE2  E9 46 FD FF FF                  jmp 0x14036fb2d
0036FDE7  44 84 9C 24 D8 00 00 00         test byte ptr [rsp + 0xd8], r11b
0036FDEF  0F 84 3D FE FF FF               je 0x14036fc32
0036FDF5  48 85 ED                        test rbp, rbp
0036FDF8  0F 85 BC 3E 37 00               jne 0x1406e3cba
0036FDFE  E9 C6 3E 37 00                  jmp 0x1406e3cc9
0036FE03  F6 84 24 D8 00 00 00 02         test byte ptr [rsp + 0xd8], 2
0036FE0B  0F 84 08 03 00 00               je 0x140370119
0036FE11  49 8B D4                        mov rdx, r12
0036FE14  E8 27 67 FA FF                  call 0x140316540
0036FE19  8A D8                           mov bl, al
0036FE1B  24 0F                           and al, 0xf
0036FE1D  3C 09                           cmp al, 9
0036FE1F  74 9F                           je 0x14036fdc0
0036FE21  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0036FE26  41 BF 01 00 00 00               mov r15d, 1
0036FE2C  48 0F BA 66 28 35               bt qword ptr [rsi + 0x28], 0x35
0036FE32  0F 82 D7 FC FF FF               jb 0x14036fb0f
0036FE38  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0036FE3D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0036FE42  E8 99 1B 11 00                  call 0x1404819e0
0036FE47  85 C0                           test eax, eax
0036FE49  0F 84 C0 FC FF FF               je 0x14036fb0f
0036FE4F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0036FE59  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0036FE5E  4F 8D 24 40                     lea r12, [r8 + r8*2]
0036FE62  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036FE6C  49 C1 E4 04                     shl r12, 4
0036FE70  48 8B C0                        mov rax, rax
0036FE73  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0036FE77  4C 03 E0                        add r12, rax
0036FE7A  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0036FE84  48 0B C8                        or rcx, rax
0036FE87  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0036FE8B  48 85 C0                        test rax, rax
0036FE8E  0F 88 E6 00 00 00               js 0x14036ff7a
0036FE94  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0036FE98  41 B9 02 00 00 00               mov r9d, 2
0036FE9E  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0036FEA3  49 8B D4                        mov rdx, r12
0036FEA6  48 8B CE                        mov rcx, rsi
0036FEA9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0036FEAD  E8 72 45 00 00                  call 0x140374424
0036FEB2  B9 01 00 00 00                  mov ecx, 1
0036FEB7  3B C1                           cmp eax, ecx
0036FEB9  75 24                           jne 0x14036fedf
0036FEBB  48 8B 05 BE 09 CA FF            mov rax, qword ptr [rip - 0x35f642]
0036FEC2  48 8D 4E 10                     lea rcx, [rsi + 0x10]
0036FEC6  48 89 01                        mov qword ptr [rcx], rax
0036FEC9  E8 CE AA F1 FF                  call 0x14028a99c
0036FECE  48 8B CE                        mov rcx, rsi
0036FED1  E8 7A 4C FC FF                  call 0x140334b50
0036FED6  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
0036FEDC  49 8B F4                        mov rsi, r12
0036FEDF  B8 01 00 00 00                  mov eax, 1
0036FEE4  4C 3B F8                        cmp r15, rax
0036FEE7  77 3C                           ja 0x14036ff25
0036FEE9  45 33 FF                        xor r15d, r15d
0036FEEC  45 8D 77 01                     lea r14d, [r15 + 1]
0036FEF0  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
0036FEF7  72 0F                           jb 0x14036ff08
0036FEF9  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0036FEFE  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0036FF03  E9 07 FC FF FF                  jmp 0x14036fb0f
0036FF08  45 03 FE                        add r15d, r14d
0036FF0B  44 85 3D 9A 53 C5 00            test dword ptr [rip + 0xc5539a], r15d
0036FF12  0F 84 BC 00 00 00               je 0x14036ffd4
0036FF18  F3 90                           pause
0036FF1A  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0036FF1E  48 85 C0                        test rax, rax
0036FF21  79 CD                           jns 0x14036fef0
0036FF23  EB E3                           jmp 0x14036ff08
0036FF25  B2 11                           mov dl, 0x11
0036FF27  49 8B CF                        mov rcx, r15
0036FF2A  E8 61 61 ED FF                  call 0x140246090
0036FF2F  EB B8                           jmp 0x14036fee9
0036FF31  F6 C1 42                        test cl, 0x42
0036FF34  0F 85 16 FC FF FF               jne 0x14036fb50
0036FF3A  45 33 C0                        xor r8d, r8d
0036FF3D  49 8B CF                        mov rcx, r15
0036FF40  41 8D 50 02                     lea edx, [r8 + 2]
0036FF44  E8 17 2C F2 FF                  call 0x140292b60
0036FF49  48 85 ED                        test rbp, rbp
0036FF4C  0F 85 D7 3D 37 00               jne 0x1406e3d29
0036FF52  E8 39 2D ED FF                  call 0x140242c90
0036FF57  45 33 C9                        xor r9d, r9d
0036FF5A  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0036FF62  49 8B D6                        mov rdx, r14
0036FF65  48 8B C8                        mov rcx, rax
0036FF68  48 8B E8                        mov rbp, rax
0036FF6B  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
0036FF6F  E8 8C 4F F2 FF                  call 0x140294f00
0036FF74  90                              nop
0036FF75  E9 AF 3D 37 00                  jmp 0x1406e3d29
0036FF7A  33 D2                           xor edx, edx
0036FF7C  E8 FF 8B F4 FF                  call 0x1402b8b80
0036FF81  4C 8B F8                        mov r15, rax
0036FF84  48 85 C0                        test rax, rax
0036FF87  0F 85 07 FF FF FF               jne 0x14036fe94
0036FF8D  E9 57 FF FF FF                  jmp 0x14036fee9
0036FF92  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0036FF96  48 85 C0                        test rax, rax
0036FF99  0F 84 86 FC FF FF               je 0x14036fc25
0036FF9F  48 85 ED                        test rbp, rbp
0036FFA2  0F 85 ED 00 00 00               jne 0x140370095
0036FFA8  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0036FFAE  45 33 C9                        xor r9d, r9d
0036FFB1  49 83 C8 FF                     or r8, 0xffffffffffffffff
0036FFB5  49 8B D7                        mov rdx, r15
0036FFB8  49 8B CC                        mov rcx, r12
0036FFBB  E8 4C 2A FF FF                  call 0x140362a0c
0036FFC0  8B D8                           mov ebx, eax
0036FFC2  85 C0                           test eax, eax
0036FFC4  0F 88 DF 00 00 00               js 0x1403700a9
0036FFCA  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0036FFCF  E9 AA FB FF FF                  jmp 0x14036fb7e
0036FFD4  8B 05 DE 6A C5 00               mov eax, dword ptr [rip + 0xc56ade]
0036FFDA  A8 40                           test al, 0x40
0036FFDC  0F 84 36 FF FF FF               je 0x14036ff18
0036FFE2  E8 A9 F4 F9 FF                  call 0x14030f490
0036FFE7  84 C0                           test al, al
0036FFE9  0F 84 29 FF FF FF               je 0x14036ff18
0036FFEF  41 8B CF                        mov ecx, r15d
0036FFF2  E8 69 F4 F9 FF                  call 0x14030f460
0036FFF7  E9 1E FF FF FF                  jmp 0x14036ff1a
0036FFFC  40 80 FF 11                     cmp dil, 0x11
00370000  74 24                           je 0x140370026
00370002  48 85 ED                        test rbp, rbp
00370005  0F 85 52 01 00 00               jne 0x14037015d
0037000B  4D 85 ED                        test r13, r13
0037000E  74 0B                           je 0x14037001b
00370010  49 8B D5                        mov rdx, r13
00370013  49 8B CE                        mov rcx, r14
00370016  E8 A5 6E EA FF                  call 0x140216ec0
0037001B  40 8A D7                        mov dl, dil
0037001E  49 8B CE                        mov rcx, r14
00370021  E8 6A D6 F0 FF                  call 0x14027d690
00370026  48 83 FB FF                     cmp rbx, -1
0037002A  0F 85 3F 01 00 00               jne 0x14037016f
00370030  33 C0                           xor eax, eax
00370032  48 83 C4 78                     add rsp, 0x78
00370036  41 5F                           pop r15
00370038  41 5E                           pop r14
0037003A  41 5D                           pop r13
0037003C  41 5C                           pop r12
0037003E  5F                              pop rdi
0037003F  5E                              pop rsi
00370040  5D                              pop rbp
00370041  5B                              pop rbx
00370042  C3                              ret
00370043  CC                              int3
00370044  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
00370048  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00370052  48 C1 E1 04                     shl rcx, 4
00370056  48 8B C0                        mov rax, rax
00370059  48 03 C8                        add rcx, rax
0037005C  48 8B 51 28                     mov rdx, qword ptr [rcx + 0x28]
00370060  48 8B 05 21 00 AC 00            mov rax, qword ptr [rip + 0xac0021]
00370067  48 C1 EA 2B                     shr rdx, 0x2b
0037006B  81 E2 FF 03 00 00               and edx, 0x3ff
00370071  4C 3B 14 D0                     cmp r10, qword ptr [rax + rdx*8]
00370075  75 78                           jne 0x1403700ef
00370077  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0037007C  E9 66 FA FF FF                  jmp 0x14036fae7
00370081  48 8B CD                        mov rcx, rbp
00370084  E8 37 1F FA FF                  call 0x140311fc0
00370089  E8 E2 3B FA FF                  call 0x140313c70
0037008E  33 ED                           xor ebp, ebp
00370090  E9 AD FC FF FF                  jmp 0x14036fd42
00370095  48 8B CD                        mov rcx, rbp
00370098  E8 23 1F FA FF                  call 0x140311fc0
0037009D  E8 CE 3B FA FF                  call 0x140313c70
003700A2  33 ED                           xor ebp, ebp
003700A4  E9 FF FE FF FF                  jmp 0x14036ffa8
003700A9  49 8B D5                        mov rdx, r13
003700AC  49 8B CE                        mov rcx, r14
003700AF  E8 0C 6E EA FF                  call 0x140216ec0
003700B4  40 8A D7                        mov dl, dil
003700B7  49 8B CE                        mov rcx, r14
003700BA  E8 D1 D5 F0 FF                  call 0x14027d690
003700BF  45 33 C0                        xor r8d, r8d
003700C2  8B D3                           mov edx, ebx
003700C4  49 8B CE                        mov rcx, r14
003700C7  E8 40 74 F3 FF                  call 0x1402a750c
003700CC  90                              nop
003700CD  E9 28 3C 37 00                  jmp 0x1406e3cfa
003700D2  48 85 ED                        test rbp, rbp
003700D5  0F 84 30 3C 37 00               je 0x1406e3d0b
003700DB  48 8B CD                        mov rcx, rbp
003700DE  E8 DD 1E FA FF                  call 0x140311fc0
003700E3  E8 88 3B FA FF                  call 0x140313c70
003700E8  33 ED                           xor ebp, ebp
003700EA  E9 1C 3C 37 00                  jmp 0x1406e3d0b
003700EF  E8 5C 4A FC FF                  call 0x140334b50
003700F4  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
003700FA  41 BB 01 00 00 00               mov r11d, 1
00370100  E9 25 F9 FF FF                  jmp 0x14036fa2a
00370105  48 8B CD                        mov rcx, rbp
00370108  E8 B3 1E FA FF                  call 0x140311fc0
0037010D  E8 5E 3B FA FF                  call 0x140313c70
00370112  33 ED                           xor ebp, ebp
00370114  E9 D3 FB FF FF                  jmp 0x14036fcec
00370119  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0037011C  41 BF 01 00 00 00               mov r15d, 1
00370122  66 41 3B C7                     cmp ax, r15w
00370126  0F 85 F1 F9 FF FF               jne 0x14036fb1d
0037012C  E9 FB FC FF FF                  jmp 0x14036fe2c
00370131  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00370136  41 B8 01 00 00 00               mov r8d, 1
0037013C  48 8B D7                        mov rdx, rdi
0037013F  E8 8C 3E F1 FF                  call 0x140283fd0
00370144  E9 24 FA FF FF                  jmp 0x14036fb6d
00370149  48 8B CD                        mov rcx, rbp
0037014C  E8 6F 1E FA FF                  call 0x140311fc0
00370151  E8 1A 3B FA FF                  call 0x140313c70
00370156  33 ED                           xor ebp, ebp
00370158  E9 EE FA FF FF                  jmp 0x14036fc4b
0037015D  48 8B CD                        mov rcx, rbp
00370160  E8 5B 1E FA FF                  call 0x140311fc0
00370165  E8 06 3B FA FF                  call 0x140313c70
0037016A  E9 9C FE FF FF                  jmp 0x14037000b
0037016F  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
00370173  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0037017D  48 C1 E1 04                     shl rcx, 4
00370181  48 8B C0                        mov rax, rax
00370184  48 03 C8                        add rcx, rax
00370187  E8 54 49 FC FF                  call 0x140334ae0
0037018C  E9 9F FE FF FF                  jmp 0x140370030
00370191  48 98                           cdqe
00370193  4C 8B CB                        mov r9, rbx
00370196  4D 8B C4                        mov r8, r12
00370199  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0037019E  BA 1B 10 00 00                  mov edx, 0x101b
003701A3  B9 1A 00 00 00                  mov ecx, 0x1a
003701A8  E8 B3 D4 18 00                  call 0x1404fd660
003701AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockCode(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p48;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (120);
    v_rsi = (v_r12) << (25);
    v_rbx = (a2) << (25);
    v_rbx = (v_rbx) - (v_rsi);
    v_stack_m78 = v_rsi;
    v_rbx = (v_rbx) >> (16);
    result = MI_IS_PHYSICAL_ADDRESS(v_rbx, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00370030;
    result = MiGetSystemRegionType(v_rbx, a2, a3, a4);
    v_r14 = v_rip + 11306795;
    if (((unsigned int)(result)) != 5) { v_r14 = v_rip + 11306165; }
    a1 = 0;
    v_stack_m60 = v_r14;
    v_stack_m84 = 0;
    if (0 != 0) {
        if (((*(unsigned __int8 *)(a1 + 184)) & ((unsigned __int8)(a1 + 2))) == 0) { a1 = (unsigned int)(a1 + 2); }
        v_stack_m84 = (unsigned int)(a1);
    }
    result = MiPrefetchDriverPages(a2, a3, a3, a4);
    v_rbp = 0;
    v_r13 = 0;
    result = MiLockWorkingSetShared(v_r14, a3, a3, a4);
    v_stack_m88 = (unsigned __int8)(result);
    goto loc_0036FBA1;
loc_0036F9E7:
    if (condition_is_below) goto loc_003700D2;
loc_0036F9F2:
    v_rdi = 0;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11273864) + result * 8);
    result = MiGetWsleContents(*(unsigned __int64 *)(v_rip + 11273864), v_r12, a3, a4);
    if (v_stack_m80 != -1) goto loc_00370044;
loc_0036FA2A:
    if (((v_stack_p20) & (2)) != 0) goto loc_0036FA47;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) != ((unsigned __int16)(v_rbp + 1))) goto loc_0036FAE7;
    goto loc_0036FA53;
loc_0036FA47:
    result = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(result))) & (15));
    if (((unsigned __int8)(result)) == 9) goto loc_0036FAE7;
loc_0036FA53:
    if (((unsigned __int8)(result)) < 9) goto loc_0036FAE7;
    result = (*(unsigned __int64 *)(v_rsi + 24)) & (*(unsigned __int64 *)(v_rip + 11273864));
    if (result != (v_rbp + 1)) goto loc_0036FAE7;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) != ((unsigned __int16)(v_rbp + 1))) goto loc_0036FAE7;
    if (((*(unsigned __int64 *)(v_rip + 12939263)) & (0x4000ULL)) == 0) goto loc_0036FA9D;
    a3 = 0;
    result = MiGetPagePrivilege(v_rsi, 2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0036FAE7;
loc_0036FA9D:
    if (((*(unsigned __int64 *)(v_rip + 12939232)) & (0x20000ULL)) != 0) goto loc_0036FD7D;
loc_0036FAAE:
    a1 = (v_r12) >> (9);
    a1 = (a1) & (result);
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a1 + result * 1))) & (66)) != 0) ? 1 : 0;
    result = (((v_stack_m84) & ((unsigned __int8)(result + 2))) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0036FCAF;
loc_0036FAE7:
    v_r15 = 0;
loc_0036FAEE:
    if (condition_is_below) goto loc_0036FC8E;
    if (v_stack_m80 != -1) goto loc_0036FE03;
loc_0036FB0F:
    if (((v_stack_p20) & (2)) != 0) goto loc_0036FDC0;
loc_0036FB1D:
    result = MiReferenceDriverPage(v_rsi, result + 2, v_stack_m80, a4);
loc_0036FB2D:
    result = (unsigned int)(*(unsigned int *)(v_rsi + 16));
    if (!(condition_is_below)) {
        a1 = v_rsi;
        result = MiCaptureDirtyBitToPfn(a1, result + 2, v_stack_m80, a4);
        v_rdi = result;
    }
    if (condition_is_below) goto loc_0036FF31;
loc_0036FB50:
    if (v_rdi != 0) goto loc_00370131;
loc_0036FB6D:
    v_r15 = (v_stack_p10) + (8);
    v_stack_p10 = v_r15;
loc_0036FB7E:
loc_0036FB83:
    if (v_r15 > v_stack_p18) goto loc_0036FFFC;
loc_0036FBA1:
    if (0 == 0) goto loc_0036FD4D;
    if (((v_r15) & (0xFFFULL)) == 0) goto loc_0036FD39;
loc_0036FBCB:
    v_r12 = (v_r15) << (25);
    v_r12 = (v_r12) - (v_stack_m78);
    v_r12 = (v_r12) >> (16);
    v_stack_m58 = v_r12;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r15)))) == 0) goto loc_0036FC42;
    result = (*(unsigned __int64 *)(v_r15)) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_stack_p10));
    v_stack_m68 = result;
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result + 2);
    if (condition_is_below) goto loc_0036FC25;
    if (!sign_flag) goto loc_0036FF92;
loc_0036FC25:
    if (sign_flag) goto loc_0036FDE7;
loc_0036FC32:
    if (condition_is_below) goto loc_0036F9F2;
    goto loc_0036F9E7;
loc_0036FC42:
    if (0 != 0) goto loc_00370149;
loc_0036FC4B:
    result = MiUnlockPageTable(v_stack_m60, 0, v_stack_m80, a4);
    result = MiUnlockWorkingSetShared(v_stack_m60, (unsigned __int8)(v_stack_m88), v_stack_m80, a4);
    a4 = 0;
    a3 = 0;
    a1 = 0;
    result = MmAccessFault(a1, v_r12, a3, a4);
    if (sign_flag) goto loc_00370191;
    v_r13 = 0;
    result = MiLockWorkingSetShared(v_stack_m60, v_r12, a3, a4);
    goto loc_0036FB83;
loc_0036FC8E:
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_stack_m60)));
    if (((*(unsigned int *)(v_rip + 12932628)) & ((unsigned int)(v_r15))) == 0) goto loc_0036FD98;
loc_0036FC9E:
loc_0036FCA0:
    if (!sign_flag) goto loc_0036FAEE;
    goto loc_0036FC8E;
loc_0036FCAF:
    result = MiGetPfnSlabType(v_rsi, v_r12, a3, a4);
    if (((unsigned int)(result)) != 9) goto loc_0036FAE7;
    if (*(unsigned __int64 *)(v_stack_m70 + 16696) == 0) goto loc_0036FCE3;
    if (v_stack_m68 >= (*(unsigned __int64 *)(v_stack_m70 + 16680))) goto loc_0036FAE7;
loc_0036FCE3:
    if (0 != 0) goto loc_00370105;
loc_0036FCEC:
    result = MiUnlockPageTable(v_stack_m60, 0, a3, a4);
    result = MiUnlockWorkingSetShared(v_stack_m60, v_stack_m88, a3, a4);
    a3 = 0;
    a2 = ((unsigned int)(*(unsigned int *)(v_rsi + 16))) >> (5);
    a2 = (unsigned int)((a2) & (31));
    result = MiAllocateDriverPage(v_stack_m70, a2, a3, a4);
    v_stack_m80 = result;
    v_r13 = 0;
    result = MiLockWorkingSetShared(v_stack_m60, a2, a3, a4);
    v_stack_m88 = (unsigned __int8)(result);
    goto loc_0036FB7E;
loc_0036FD39:
    if (0 != 0) goto loc_00370081;
loc_0036FD42:
    result = MiUnlockPageTable(v_stack_m60, 0, a3, a4);
loc_0036FD4D:
    v_r13 = (v_r15) >> (9);
    v_r13 = (v_r13) & (result);
    v_r13 = (v_r13) + (v_r12);
    result = MiLockNestedPageTable(v_stack_m60, v_r13, a3, a4);
    goto loc_0036FBCB;
loc_0036FD7D:
    a3 = 0;
    result = MiGetPagePrivilege(v_rsi, v_r13, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0036FAE7;
    goto loc_0036FAAE;
loc_0036FD98:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12938522)))) & (64)) == 0) goto loc_0036FC9E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rsi, result + 2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0036FC9E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), result + 2, a3, a4);
    goto loc_0036FCA0;
loc_0036FDC0:
    v_rbx = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(v_rbx)) == 9) goto loc_0036FB2D;
    result = MiRemoveSystemImagePage(v_stack_m60, v_stack_p10, v_rsi, a4);
    goto loc_0036FB2D;
loc_0036FDE7:
    if (((v_stack_p20) & (1)) == 0) goto loc_0036FC32;
loc_0036FE03:
    if (((v_stack_p20) & (2)) == 0) goto loc_00370119;
    result = MiGetWsleContents(v_stack_m60, v_r12, v_rsi, a4);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 9) goto loc_0036FDC0;
loc_0036FE2C:
    if (((unsigned __int8)(result)) < 9) goto loc_0036FB0F;
    result = MiBetterDriverPageNeeded(v_stack_m70, v_stack_m68, v_stack_m80, a4);
    if ((unsigned int)(result) == 0) goto loc_0036FB0F;
    v_r12 = (v_stack_m80 + v_stack_m80 * 2) << (4);
    v_r12 = (v_r12) + (result);
    a1 = (*(unsigned __int64 *)(v_rsi + 8)) | (result);
    if (sign_flag) goto loc_0036FF7A;
loc_0036FE94:
    v_stack_m98 = (unsigned int)((unsigned int)(v_stack_m84));
    result = MiTradeActivePage(v_rsi, v_r12, v_stack_m58, 2);
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(v_rip - 3536450);
        a1 = v_rsi + 16;
        *(unsigned __int64 *)(a1) = result;
        result = MiSetOriginalPtePfnFromFreeList(a1, v_r12, v_stack_m58, 2);
        a1 = v_rsi;
        result = MiReleaseFreshPageAtDpc(a1, v_r12, v_stack_m58, 2);
        v_rsi = v_r12;
    }
    if (1 > 1) goto loc_0036FF25;
loc_0036FEE9:
    v_r15 = 0;
loc_0036FEF0:
    if (condition_is_below) goto loc_0036FF08;
    goto loc_0036FB0F;
loc_0036FF08:
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_stack_m60)));
    if (((*(unsigned int *)(v_rip + 12931994)) & ((unsigned int)(v_r15))) == 0) goto loc_0036FFD4;
loc_0036FF18:
loc_0036FF1A:
    if (!sign_flag) goto loc_0036FEF0;
    goto loc_0036FF08;
loc_0036FF25:
    result = MiUnlockProtoPoolPage(v_r15, 17, v_stack_m58, 2);
    goto loc_0036FEE9;
loc_0036FF31:
    if ((((unsigned __int8)(v_r15)) & (66)) != 0) goto loc_0036FB50;
    a3 = 0;
    result = MiWriteValidPteVolatile(v_r15, a3 + 2, a3, 2);
    result = MiGetProcessorFlushList(v_r15, a3 + 2, a3, 2);
    a4 = 0;
    v_stack_m98 = 32;
    result = MiInitializeTbFlushList(result, v_stack_m60, (unsigned int)(*(unsigned int *)(result + 12)), a4);
loc_0036FF7A:
    a2 = 0;
    result = MiLockProtoPoolPage(result, a2, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    if (result != 0) goto loc_0036FE94;
    goto loc_0036FEE9;
loc_0036FF92:
    if (*(unsigned __int64 *)(v_rsi + 8) == 0) goto loc_0036FC25;
    if (result != 0) goto loc_00370095;
loc_0036FFA8:
    a4 = 0;
    a3 = ((unsigned int)(*(unsigned int *)(result + 12))) | (-1);
    result = MiCopyOnWrite(v_stack_m58, result, a3, a4);
    if (sign_flag) goto loc_003700A9;
    goto loc_0036FB7E;
loc_0036FFD4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12937950)))) & (64)) == 0) goto loc_0036FF18;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m58, result, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0036FF18;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), result, a3, a4);
    goto loc_0036FF1A;
loc_0036FFFC:
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_00370026;
    if (result != 0) goto loc_0037015D;
loc_0037000B:
    if (v_r13 != 0) {
        a2 = v_r13;
        a1 = v_stack_m60;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(v_stack_m60, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
loc_00370026:
    if (v_stack_m80 != -1) goto loc_0037016F;
loc_00370030:
    result = 0;
    v_rsp = (v_rsp) + (120);
    return result;
loc_00370044:
    a1 = (a3 + a3 * 2) << (4);
    a1 = (a1) + (0);
    a2 = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    a2 = (unsigned int)((a2) & (0x3FFULL));
    if (v_stack_m68 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11272225) + a2 * 8))) goto loc_003700EF;
    v_stack_p38 = a3;
    goto loc_0036FAE7;
loc_00370081:
    result = MiFlushTbList(0, a2, a3, a4);
    result = MiReleaseProcessorFlushList(0, a2, a3, a4);
    v_rbp = 0;
    goto loc_0036FD42;
loc_00370095:
    result = MiFlushTbList(0, a2, a3, a4);
    result = MiReleaseProcessorFlushList(0, a2, a3, a4);
    v_rbp = 0;
    goto loc_0036FFA8;
loc_003700A9:
    result = MiUnlockPageTable(v_stack_m60, v_r13, a3, a4);
    result = MiUnlockWorkingSetShared(v_stack_m60, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    a3 = 0;
    result = MiCopyOnWriteCheckConditions(v_stack_m60, (unsigned int)((unsigned int)(v_stack_m80)), a3, a4);
loc_003700D2:
    result = MiFlushTbList(0, (unsigned int)((unsigned int)(v_stack_m80)), a3, a4);
    result = MiReleaseProcessorFlushList(0, (unsigned int)((unsigned int)(v_stack_m80)), a3, a4);
    v_rbp = 0;
loc_003700EF:
    result = MiReleaseFreshPageAtDpc(0, (unsigned int)((unsigned int)(v_stack_m80)), a3, a4);
    goto loc_0036FA2A;
loc_00370105:
    result = MiFlushTbList(0, (unsigned int)((unsigned int)(v_stack_m80)), a3, a4);
    result = MiReleaseProcessorFlushList(0, (unsigned int)((unsigned int)(v_stack_m80)), a3, a4);
    v_rbp = 0;
    goto loc_0036FCEC;
loc_00370119:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) != 1) goto loc_0036FB1D;
    goto loc_0036FE2C;
loc_00370131:
    result = MiReleasePageFileInfo(v_stack_p48, (unsigned __int8)(result), 1, a4);
    goto loc_0036FB6D;
loc_00370149:
    result = MiFlushTbList(0, (unsigned __int8)(result), 1, a4);
    result = MiReleaseProcessorFlushList(0, (unsigned __int8)(result), 1, a4);
    v_rbp = 0;
    goto loc_0036FC4B;
loc_0037015D:
    result = MiFlushTbList(0, (unsigned __int8)(result), 1, a4);
    result = MiReleaseProcessorFlushList(0, (unsigned __int8)(result), 1, a4);
    goto loc_0037000B;
loc_0037016F:
    a1 = (v_stack_m80 + v_stack_m80 * 2) << (4);
    a1 = (a1) + (result);
    result = MiReleaseFreshPage(a1, (unsigned __int8)(result), 1, a4);
    goto loc_00370030;
loc_00370191:
    v_stack_p20 = result;
    result = KeBugCheckEx(26, (unsigned int)(0x101BULL), v_stack_m58, v_stack_m80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockCode(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m88;
    uint32_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p48;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (120);
    local_rsi = (local_r12) << (25);
    local_rbx = (Arg2) << (25);
    local_rbx = (local_rbx) - (local_rsi);
    v_stack_m78 = local_rsi;
    local_rbx = (local_rbx) >> (16);
    result = MI_IS_PHYSICAL_ADDRESS(local_rbx, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00370030;
    result = MiGetSystemRegionType(local_rbx, Arg2, Arg3, Arg4);
    local_r14 = v_rip + 11306795;
    if (((uint32_t)(result)) != 5) { local_r14 = v_rip + 11306165; }
    Arg1 = 0;
    v_stack_m60 = local_r14;
    v_stack_m84 = 0;
    if (0 != 0) {
        if (((*(uint8_t *)(Arg1 + 0xB8)) & ((uint8_t)(Arg1 + 2))) == 0) { Arg1 = (uint32_t)(Arg1 + 2); }
        v_stack_m84 = (uint32_t)(Arg1);
    }
    result = MiPrefetchDriverPages(Arg2, Arg3, Arg3, Arg4);
    local_rbp = 0;
    local_r13 = 0;
    result = MiLockWorkingSetShared(local_r14, Arg3, Arg3, Arg4);
    v_stack_m88 = (uint8_t)(result);
    goto loc_0036FBA1;
loc_0036F9E7:
    if (condition_is_below) goto loc_003700D2;
loc_0036F9F2:
    local_rdi = 0;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC0688) + result * 8);
    result = MiGetWsleContents(*(uint64_t *)(v_rip + 0xAC0688), local_r12, Arg3, Arg4);
    if (v_stack_m80 != -1) goto loc_00370044;
loc_0036FA2A:
    if (((v_stack_p20) & (2)) != 0) goto loc_0036FA47;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) != ((uint16_t)(local_rbp + 1))) goto loc_0036FAE7;
    goto loc_0036FA53;
loc_0036FA47:
    result = (uint8_t)(((uint8_t)((uint8_t)(result))) & (15));
    if (((uint8_t)(result)) == 9) goto loc_0036FAE7;
loc_0036FA53:
    if (((uint8_t)(result)) < 9) goto loc_0036FAE7;
    result = (*(uint64_t *)(local_rsi + 0x18)) & (*(uint64_t *)(v_rip + 0xAC0688));
    if (result != (local_rbp + 1)) goto loc_0036FAE7;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) != ((uint16_t)(local_rbp + 1))) goto loc_0036FAE7;
    if (((*(uint64_t *)(v_rip + 0xC56FFF)) & (0x4000ULL)) == 0) goto loc_0036FA9D;
    Arg3 = 0;
    result = MiGetPagePrivilege(local_rsi, 2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0036FAE7;
loc_0036FA9D:
    if (((*(uint64_t *)(v_rip + 0xC56FE0)) & (0x20000ULL)) != 0) goto loc_0036FD7D;
loc_0036FAAE:
    Arg1 = (local_r12) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg1 + result * 1))) & (66)) != 0) ? 1 : 0;
    result = (((v_stack_m84) & ((uint8_t)(result + 2))) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0036FCAF;
loc_0036FAE7:
    local_r15 = 0;
loc_0036FAEE:
    if (condition_is_below) goto loc_0036FC8E;
    if (v_stack_m80 != -1) goto loc_0036FE03;
loc_0036FB0F:
    if (((v_stack_p20) & (2)) != 0) goto loc_0036FDC0;
loc_0036FB1D:
    result = MiReferenceDriverPage(local_rsi, result + 2, v_stack_m80, Arg4);
loc_0036FB2D:
    result = (uint32_t)(*(uint32_t *)(local_rsi + 0x10));
    if (!(condition_is_below)) {
        Arg1 = local_rsi;
        result = MiCaptureDirtyBitToPfn(Arg1, result + 2, v_stack_m80, Arg4);
        local_rdi = result;
    }
    if (condition_is_below) goto loc_0036FF31;
loc_0036FB50:
    if (local_rdi != 0) goto loc_00370131;
loc_0036FB6D:
    local_r15 = (v_stack_p10) + (8);
    v_stack_p10 = local_r15;
loc_0036FB7E:
loc_0036FB83:
    if (local_r15 > v_stack_p18) goto loc_0036FFFC;
loc_0036FBA1:
    if (0 == 0) goto loc_0036FD4D;
    if (((local_r15) & (0xFFFULL)) == 0) goto loc_0036FD39;
loc_0036FBCB:
    local_r12 = (local_r15) << (25);
    local_r12 = (local_r12) - (v_stack_m78);
    local_r12 = (local_r12) >> (16);
    v_stack_m58 = local_r12;
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r15)))) == 0) goto loc_0036FC42;
    result = (*(uint64_t *)(local_r15)) >> (12);
    result = (result) & (*(uint64_t *)(v_stack_p10));
    v_stack_m68 = result;
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result + 2);
    if (condition_is_below) goto loc_0036FC25;
    if (!sign_flag) goto loc_0036FF92;
loc_0036FC25:
    if (sign_flag) goto loc_0036FDE7;
loc_0036FC32:
    if (condition_is_below) goto loc_0036F9F2;
    goto loc_0036F9E7;
loc_0036FC42:
    if (0 != 0) goto loc_00370149;
loc_0036FC4B:
    result = MiUnlockPageTable(v_stack_m60, 0, v_stack_m80, Arg4);
    result = MiUnlockWorkingSetShared(v_stack_m60, (uint8_t)(v_stack_m88), v_stack_m80, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = MmAccessFault(Arg1, local_r12, Arg3, Arg4);
    if (sign_flag) goto loc_00370191;
    local_r13 = 0;
    result = MiLockWorkingSetShared(v_stack_m60, local_r12, Arg3, Arg4);
    goto loc_0036FB83;
loc_0036FC8E:
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(v_stack_m60)));
    if (((*(uint32_t *)(v_rip + 0xC55614)) & ((uint32_t)(local_r15))) == 0) goto loc_0036FD98;
loc_0036FC9E:
loc_0036FCA0:
    if (!sign_flag) goto loc_0036FAEE;
    goto loc_0036FC8E;
loc_0036FCAF:
    result = MiGetPfnSlabType(local_rsi, local_r12, Arg3, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_0036FAE7;
    if (*(uint64_t *)(v_stack_m70 + 0x4138) == 0) goto loc_0036FCE3;
    if (v_stack_m68 >= (*(uint64_t *)(v_stack_m70 + 0x4128))) goto loc_0036FAE7;
loc_0036FCE3:
    if (0 != 0) goto loc_00370105;
loc_0036FCEC:
    result = MiUnlockPageTable(v_stack_m60, 0, Arg3, Arg4);
    result = MiUnlockWorkingSetShared(v_stack_m60, v_stack_m88, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rsi + 0x10))) >> (5);
    Arg2 = (uint32_t)((Arg2) & (31));
    result = MiAllocateDriverPage(v_stack_m70, Arg2, Arg3, Arg4);
    v_stack_m80 = result;
    local_r13 = 0;
    result = MiLockWorkingSetShared(v_stack_m60, Arg2, Arg3, Arg4);
    v_stack_m88 = (uint8_t)(result);
    goto loc_0036FB7E;
loc_0036FD39:
    if (0 != 0) goto loc_00370081;
loc_0036FD42:
    result = MiUnlockPageTable(v_stack_m60, 0, Arg3, Arg4);
loc_0036FD4D:
    local_r13 = (local_r15) >> (9);
    local_r13 = (local_r13) & (result);
    local_r13 = (local_r13) + (local_r12);
    result = MiLockNestedPageTable(v_stack_m60, local_r13, Arg3, Arg4);
    goto loc_0036FBCB;
loc_0036FD7D:
    Arg3 = 0;
    result = MiGetPagePrivilege(local_rsi, local_r13, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0036FAE7;
    goto loc_0036FAAE;
loc_0036FD98:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56D1A)))) & (64)) == 0) goto loc_0036FC9E;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rsi, result + 2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0036FC9E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), result + 2, Arg3, Arg4);
    goto loc_0036FCA0;
loc_0036FDC0:
    local_rbx = (uint8_t)((result) & (15));
    if (((uint8_t)(local_rbx)) == 9) goto loc_0036FB2D;
    result = MiRemoveSystemImagePage(v_stack_m60, v_stack_p10, local_rsi, Arg4);
    goto loc_0036FB2D;
loc_0036FDE7:
    if (((v_stack_p20) & (1)) == 0) goto loc_0036FC32;
loc_0036FE03:
    if (((v_stack_p20) & (2)) == 0) goto loc_00370119;
    result = MiGetWsleContents(v_stack_m60, local_r12, local_rsi, Arg4);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 9) goto loc_0036FDC0;
loc_0036FE2C:
    if (((uint8_t)(result)) < 9) goto loc_0036FB0F;
    result = MiBetterDriverPageNeeded(v_stack_m70, v_stack_m68, v_stack_m80, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0036FB0F;
    local_r12 = (v_stack_m80 + v_stack_m80 * 2) << (4);
    local_r12 = (local_r12) + (result);
    Arg1 = (*(uint64_t *)(local_rsi + 0x8)) | (result);
    if (sign_flag) goto loc_0036FF7A;
loc_0036FE94:
    v_stack_m98 = (uint32_t)((uint32_t)(v_stack_m84));
    result = MiTradeActivePage(local_rsi, local_r12, v_stack_m58, 2);
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(v_rip - 0x35F642);
        Arg1 = local_rsi + 16;
        *(uint64_t *)(Arg1) = result;
        result = MiSetOriginalPtePfnFromFreeList(Arg1, local_r12, v_stack_m58, 2);
        Arg1 = local_rsi;
        result = MiReleaseFreshPageAtDpc(Arg1, local_r12, v_stack_m58, 2);
        local_rsi = local_r12;
    }
    if (1 > 1) goto loc_0036FF25;
loc_0036FEE9:
    local_r15 = 0;
loc_0036FEF0:
    if (condition_is_below) goto loc_0036FF08;
    goto loc_0036FB0F;
loc_0036FF08:
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(v_stack_m60)));
    if (((*(uint32_t *)(v_rip + 0xC5539A)) & ((uint32_t)(local_r15))) == 0) goto loc_0036FFD4;
loc_0036FF18:
loc_0036FF1A:
    if (!sign_flag) goto loc_0036FEF0;
    goto loc_0036FF08;
loc_0036FF25:
    result = MiUnlockProtoPoolPage(local_r15, 17, v_stack_m58, 2);
    goto loc_0036FEE9;
loc_0036FF31:
    if ((((uint8_t)(local_r15)) & (66)) != 0) goto loc_0036FB50;
    Arg3 = 0;
    result = MiWriteValidPteVolatile(local_r15, Arg3 + 2, Arg3, 2);
    result = MiGetProcessorFlushList(local_r15, Arg3 + 2, Arg3, 2);
    Arg4 = 0;
    v_stack_m98 = 32;
    result = MiInitializeTbFlushList(result, v_stack_m60, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
loc_0036FF7A:
    Arg2 = 0;
    result = MiLockProtoPoolPage(result, Arg2, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    if (result != 0) goto loc_0036FE94;
    goto loc_0036FEE9;
loc_0036FF92:
    if (*(uint64_t *)(local_rsi + 0x8) == 0) goto loc_0036FC25;
    if (result != 0) goto loc_00370095;
loc_0036FFA8:
    Arg4 = 0;
    Arg3 = ((uint32_t)(*(uint32_t *)(result + 0xC))) | (-1);
    result = MiCopyOnWrite(v_stack_m58, result, Arg3, Arg4);
    if (sign_flag) goto loc_003700A9;
    goto loc_0036FB7E;
loc_0036FFD4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56ADE)))) & (64)) == 0) goto loc_0036FF18;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m58, result, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0036FF18;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), result, Arg3, Arg4);
    goto loc_0036FF1A;
loc_0036FFFC:
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_00370026;
    if (result != 0) goto loc_0037015D;
loc_0037000B:
    if (local_r13 != 0) {
        Arg2 = local_r13;
        Arg1 = v_stack_m60;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockWorkingSetShared(v_stack_m60, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
loc_00370026:
    if (v_stack_m80 != -1) goto loc_0037016F;
loc_00370030:
    result = 0;
    local_rsp = (local_rsp) + (120);
    return result;
loc_00370044:
    Arg1 = (Arg3 + Arg3 * 2) << (4);
    Arg1 = (Arg1) + (0);
    Arg2 = (*(uint64_t *)(Arg1 + 0x28)) >> (43);
    Arg2 = (uint32_t)((Arg2) & (0x3FFULL));
    if (v_stack_m68 != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC0021) + Arg2 * 8))) goto loc_003700EF;
    v_stack_p38 = Arg3;
    goto loc_0036FAE7;
loc_00370081:
    result = MiFlushTbList(0, Arg2, Arg3, Arg4);
    result = MiReleaseProcessorFlushList(0, Arg2, Arg3, Arg4);
    local_rbp = 0;
    goto loc_0036FD42;
loc_00370095:
    result = MiFlushTbList(0, Arg2, Arg3, Arg4);
    result = MiReleaseProcessorFlushList(0, Arg2, Arg3, Arg4);
    local_rbp = 0;
    goto loc_0036FFA8;
loc_003700A9:
    result = MiUnlockPageTable(v_stack_m60, local_r13, Arg3, Arg4);
    result = MiUnlockWorkingSetShared(v_stack_m60, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    Arg3 = 0;
    result = MiCopyOnWriteCheckConditions(v_stack_m60, (uint32_t)((uint32_t)(v_stack_m80)), Arg3, Arg4);
loc_003700D2:
    result = MiFlushTbList(0, (uint32_t)((uint32_t)(v_stack_m80)), Arg3, Arg4);
    result = MiReleaseProcessorFlushList(0, (uint32_t)((uint32_t)(v_stack_m80)), Arg3, Arg4);
    local_rbp = 0;
loc_003700EF:
    result = MiReleaseFreshPageAtDpc(0, (uint32_t)((uint32_t)(v_stack_m80)), Arg3, Arg4);
    goto loc_0036FA2A;
loc_00370105:
    result = MiFlushTbList(0, (uint32_t)((uint32_t)(v_stack_m80)), Arg3, Arg4);
    result = MiReleaseProcessorFlushList(0, (uint32_t)((uint32_t)(v_stack_m80)), Arg3, Arg4);
    local_rbp = 0;
    goto loc_0036FCEC;
loc_00370119:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) != 1) goto loc_0036FB1D;
    goto loc_0036FE2C;
loc_00370131:
    result = MiReleasePageFileInfo(v_stack_p48, (uint8_t)(result), 1, Arg4);
    goto loc_0036FB6D;
loc_00370149:
    result = MiFlushTbList(0, (uint8_t)(result), 1, Arg4);
    result = MiReleaseProcessorFlushList(0, (uint8_t)(result), 1, Arg4);
    local_rbp = 0;
    goto loc_0036FC4B;
loc_0037015D:
    result = MiFlushTbList(0, (uint8_t)(result), 1, Arg4);
    result = MiReleaseProcessorFlushList(0, (uint8_t)(result), 1, Arg4);
    goto loc_0037000B;
loc_0037016F:
    Arg1 = (v_stack_m80 + v_stack_m80 * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiReleaseFreshPage(Arg1, (uint8_t)(result), 1, Arg4);
    goto loc_00370030;
loc_00370191:
    v_stack_p20 = result;
    result = KeBugCheckEx(26, (uint32_t)(0x101BULL), v_stack_m58, v_stack_m80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036F91C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
