# MiSetSystemCodeProtection

- RVA: `0x00384420`–`0x00384C20` (길이 `2,048` bytes)
- VA: `0x0000000140384420`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007BC2C`
- 디코드: `478`개 명령, `2,048/2,048` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00384490` → [MI_IS_PHYSICAL_ADDRESS](../23/MI_IS_PHYSICAL_ADDRESS_function_0023B3A0.md) (function, `0x0023B3A0`)
- `0x003844DD` → [MiMakeDriverPagesPrivate](MiMakeDriverPagesPrivate_function_00384C60.md) (function, `0x00384C60`)
- `0x003844F8` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00384545` → [MiMarkPfnVerified](MiMarkPfnVerified_function_003833C4.md) (function, `0x003833C4`)
- `0x0038457D` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00384597` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x003845BB` → [MI_TIGHTER_PERMISSIONS](MI_TIGHTER_PERMISSIONS_function_00384C30.md) (function, `0x00384C30`)
- `0x00384677` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x003846BB` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x003846E5` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x003846EA` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00384700` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00384713` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00384735` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00384756` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x00384767` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x003847A4` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x003847B9` → [MiSectionControlArea](../29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00384802` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00384815` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00384827` → [MiOffsetToProtos](../24/MiOffsetToProtos_function_0024D880.md) (function, `0x0024D880`)
- `0x0038483B` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0038484A` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x003848A4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003848B3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003848FF` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00384921` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x003849A7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x003849D9` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x00384AF9` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00384B12` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00384B1D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00384B4E` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00384B53` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00384B63` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00384B68` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00384B7B` → [MiRestrictSystemCodeProtection](../4F/MiRestrictSystemCodeProtection_function_004FD248.md) (function, `0x004FD248`)
- `0x00384BB4` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- [MiSetImageProtection](MiSetImageProtection_function_003843D0.md) at `0x0038440D`
- [MmProtectDriverSection](../67/MmProtectDriverSection_function_00670A80.md) at `0x00670DB7`
- [MiProtectSystemImage](../../page/AA/MiProtectSystemImage_function_00AA7D74.md) at `0x00AA7F5A`
- [MiProtectSystemImage](../../page/AA/MiProtectSystemImage_function_00AA7D74.md) at `0x00AA8028`
- [MiProtectKernelCfgData](../../init/C5/MiProtectKernelCfgData_function_00C5F5E0.md) at `0x00C5F6C8`

### Static image references
- `0x003844EC` → RVA `0x00E37E40` (`.data`; read)
- `0x0038459C` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0038469B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00384896` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0038492A` → RVA `0x00E2DC80` (`.data`; read)
- `0x0038496D` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003849B9` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00384B45` → [sub_006E49E8](../6E/Unknown_function_006E49E8.md) (`tail-transfer`)
  - `0x00384B5B` → [sub_006E49E8](../6E/Unknown_function_006E49E8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00384420  48 8B C4                        mov rax, rsp
00384423  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00384427  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0038442B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0038442F  53                              push rbx
00384430  55                              push rbp
00384431  56                              push rsi
00384432  57                              push rdi
00384433  41 54                           push r12
00384435  41 55                           push r13
00384437  41 56                           push r14
00384439  41 57                           push r15
0038443B  48 81 EC 88 00 00 00            sub rsp, 0x88
00384442  45 33 ED                        xor r13d, r13d
00384445  41 8B E9                        mov ebp, r9d
00384448  4C 89 68 88                     mov qword ptr [rax - 0x78], r13
0038444C  49 8B F8                        mov rdi, r8
0038444F  48 8B F2                        mov rsi, rdx
00384452  48 8B D9                        mov rbx, rcx
00384455  45 8D 7D 01                     lea r15d, [r13 + 1]
00384459  41 83 F9 18                     cmp r9d, 0x18
0038445D  74 0A                           je 0x140384469
0038445F  40 F6 C5 10                     test bpl, 0x10
00384463  0F 85 54 04 00 00               jne 0x1403848bd
00384469  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
0038446E  4C 8B E6                        mov r12, rsi
00384471  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0038447B  49 C1 E4 19                     shl r12, 0x19
0038447F  48 8B C8                        mov rcx, rax
00384482  48 C1 E1 19                     shl rcx, 0x19
00384486  4C 2B E1                        sub r12, rcx
00384489  49 C1 FC 10                     sar r12, 0x10
0038448D  49 8B CC                        mov rcx, r12
00384490  E8 0B 6F EB FF                  call 0x14023b3a0
00384495  85 C0                           test eax, eax
00384497  0F 85 7B 02 00 00               jne 0x140384718
0038449D  44 8B F5                        mov r14d, ebp
003844A0  81 FD 00 01 00 00               cmp ebp, 0x100
003844A6  0F 84 09 03 00 00               je 0x1403847b5
003844AC  8B C5                           mov eax, ebp
003844AE  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
003844B3  83 E0 05                        and eax, 5
003844B6  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
003844BB  41 83 E6 FE                     and r14d, 0xfffffffe
003844BF  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
003844C4  3C 05                           cmp al, 5
003844C6  4C 8B C7                        mov r8, rdi
003844C9  48 8B D6                        mov rdx, rsi
003844CC  48 8B CB                        mov rcx, rbx
003844CF  44 0F 45 F5                     cmovne r14d, ebp
003844D3  45 8B CE                        mov r9d, r14d
003844D6  41 D1 E9                        shr r9d, 1
003844D9  41 83 E1 02                     and r9d, 2
003844DD  E8 7E 07 00 00                  call 0x140384c60
003844E2  85 C0                           test eax, eax
003844E4  0F 88 C4 02 00 00               js 0x1403847ae
003844EA  33 FF                           xor edi, edi
003844EC  48 8D 0D 4D 39 AB 00            lea rcx, [rip + 0xab394d]
003844F3  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
003844F8  E8 F3 86 EF FF                  call 0x14027cbf0
003844FD  88 84 24 D8 00 00 00            mov byte ptr [rsp + 0xd8], al
00384504  E9 D6 00 00 00                  jmp 0x1403845df
00384509  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00384510  0F 82 82 01 00 00               jb 0x140384698
00384516  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0038451A  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0038451E  48 C1 E2 05                     shl rdx, 5
00384522  48 8B CA                        mov rcx, rdx
00384525  48 33 C8                        xor rcx, rax
00384528  48 81 E1 1F FC FF FF            and rcx, 0xfffffffffffffc1f
0038452F  48 33 CA                        xor rcx, rdx
00384532  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
00384537  48 89 4B 10                     mov qword ptr [rbx + 0x10], rcx
0038453B  74 0D                           je 0x14038454a
0038453D  BA 04 00 00 00                  mov edx, 4
00384542  48 8B CB                        mov rcx, rbx
00384545  E8 7A EE FF FF                  call 0x1403833c4
0038454A  33 C0                           xor eax, eax
0038454C  48 8B EF                        mov rbp, rdi
0038454F  83 E5 42                        and ebp, 0x42
00384552  0F 85 60 01 00 00               jne 0x1403846b8
00384558  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00384562  F0 48 21 4B 18                  lock and qword ptr [rbx + 0x18], rcx
00384567  48 85 C0                        test rax, rax
0038456A  0F 85 25 06 00 00               jne 0x140384b95
00384570  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00384575  48 8B CE                        mov rcx, rsi
00384578  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
0038457D  E8 0E 10 F4 FF                  call 0x1402c5590
00384582  48 8B D8                        mov rbx, rax
00384585  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00384589  A8 04                           test al, 4
0038458B  0F 85 2D 06 00 00               jne 0x140384bbe
00384591  48 8B D3                        mov rdx, rbx
00384594  48 8B CE                        mov rcx, rsi
00384597  E8 74 D2 EF FF                  call 0x140281810
0038459C  48 8B 05 E5 24 C4 00            mov rax, qword ptr [rip + 0xc424e5]
003845A3  48 0F BA E0 08                  bt rax, 8
003845A8  72 0B                           jb 0x1403845b5
003845AA  48 0F BA E0 09                  bt rax, 9
003845AF  0F 83 7B 01 00 00               jae 0x140384730
003845B5  48 8B D3                        mov rdx, rbx
003845B8  48 8B CF                        mov rcx, rdi
003845BB  E8 70 06 00 00                  call 0x140384c30
003845C0  85 C0                           test eax, eax
003845C2  0F 85 68 01 00 00               jne 0x140384730
003845C8  8B AC 24 E8 00 00 00            mov ebp, dword ptr [rsp + 0xe8]
003845CF  48 83 C6 08                     add rsi, 8
003845D3  49 81 C4 00 10 00 00            add r12, 0x1000
003845DA  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
003845DF  48 3B B4 24 E0 00 00 00         cmp rsi, qword ptr [rsp + 0xe0]
003845E7  0F 87 F0 00 00 00               ja 0x1403846dd
003845ED  48 85 FF                        test rdi, rdi
003845F0  0F 84 7B 01 00 00               je 0x140384771
003845F6  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
003845FD  0F 84 3F 05 00 00               je 0x140384b42
00384603  48 3B 74 24 58                  cmp rsi, qword ptr [rsp + 0x58]
00384608  0F 87 C4 01 00 00               ja 0x1403847d2
0038460E  83 BC 24 F0 00 00 00 00         cmp dword ptr [rsp + 0xf0], 0
00384616  48 8B 3E                        mov rdi, qword ptr [rsi]
00384619  0F 85 56 05 00 00               jne 0x140384b75
0038461F  41 8B C6                        mov eax, r14d
00384622  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00384626  41 84 FF                        test r15b, dil
00384629  0F 84 B7 02 00 00               je 0x1403848e6
0038462F  48 8B C7                        mov rax, rdi
00384632  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0038463C  48 C1 E8 0C                     shr rax, 0xc
00384640  48 23 C1                        and rax, rcx
00384643  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00384648  48 8D 1C 40                     lea rbx, [rax + rax*2]
0038464C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00384656  48 C1 E3 04                     shl rbx, 4
0038465A  48 8B C0                        mov rax, rax
0038465D  48 03 D8                        add rbx, rax
00384660  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00384664  48 85 C0                        test rax, rax
00384667  0F 88 62 FF FF FF               js 0x1403845cf
0038466D  45 33 C0                        xor r8d, r8d
00384670  48 8B CB                        mov rcx, rbx
00384673  41 8D 50 02                     lea edx, [r8 + 2]
00384677  E8 A4 0D F0 FF                  call 0x140285420
0038467C  A8 40                           test al, 0x40
0038467E  0F 85 01 05 00 00               jne 0x140384b85
00384684  48 F7 05 F9 23 C4 00 00 80 00 00  test qword ptr [rip + 0xc423f9], 0x8000
0038468F  75 34                           jne 0x1403846c5
00384691  33 ED                           xor ebp, ebp
00384693  E9 71 FE FF FF                  jmp 0x140384509
00384698  41 03 EF                        add ebp, r15d
0038469B  85 2D 0B 0C C4 00               test dword ptr [rip + 0xc40c0b], ebp
003846A1  0F 84 EF 01 00 00               je 0x140384896
003846A7  F3 90                           pause
003846A9  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
003846AD  48 85 C0                        test rax, rax
003846B0  0F 89 53 FE FF FF               jns 0x140384509
003846B6  EB E0                           jmp 0x140384698
003846B8  48 8B CB                        mov rcx, rbx
003846BB  E8 10 C7 FE FF                  call 0x140370dd0
003846C0  E9 93 FE FF FF                  jmp 0x140384558
003846C5  F6 44 24 30 04                  test byte ptr [rsp + 0x30], 4
003846CA  74 C5                           je 0x140384691
003846CC  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
003846D0  48 C1 E8 3C                     shr rax, 0x3c
003846D4  24 07                           and al, 7
003846D6  3C 03                           cmp al, 3
003846D8  75 B7                           jne 0x140384691
003846DA  45 33 FF                        xor r15d, r15d
003846DD  4D 85 ED                        test r13, r13
003846E0  74 0D                           je 0x1403846ef
003846E2  49 8B CD                        mov rcx, r13
003846E5  E8 D6 D8 F8 FF                  call 0x140311fc0
003846EA  E8 81 F5 F8 FF                  call 0x140313c70
003846EF  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003846F4  48 85 D2                        test rdx, rdx
003846F7  74 0C                           je 0x140384705
003846F9  48 8D 0D 40 37 AB 00            lea rcx, [rip + 0xab3740]
00384700  E8 BB 27 E9 FF                  call 0x140216ec0
00384705  8A 94 24 D8 00 00 00            mov dl, byte ptr [rsp + 0xd8]
0038470C  48 8D 0D 2D 37 AB 00            lea rcx, [rip + 0xab372d]
00384713  E8 78 8F EF FF                  call 0x14027d690
00384718  41 8B C7                        mov eax, r15d
0038471B  48 81 C4 88 00 00 00            add rsp, 0x88
00384722  41 5F                           pop r15
00384724  41 5E                           pop r14
00384726  41 5D                           pop r13
00384728  41 5C                           pop r12
0038472A  5F                              pop rdi
0038472B  5E                              pop rsi
0038472C  5D                              pop rbp
0038472D  5B                              pop rbx
0038472E  C3                              ret
0038472F  CC                              int3
00384730  4D 85 ED                        test r13, r13
00384733  75 26                           jne 0x14038475b
00384735  E8 56 E5 EB FF                  call 0x140242c90
0038473A  45 33 C9                        xor r9d, r9d
0038473D  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
00384745  48 8D 15 F4 36 AB 00            lea rdx, [rip + 0xab36f4]
0038474C  48 8B C8                        mov rcx, rax
0038474F  4C 8B E8                        mov r13, rax
00384752  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
00384756  E8 A5 07 F1 FF                  call 0x140294f00
0038475B  45 33 C9                        xor r9d, r9d
0038475E  4D 8B C7                        mov r8, r15
00384761  49 8B D4                        mov rdx, r12
00384764  49 8B CD                        mov rcx, r13
00384767  E8 04 EF F0 FF                  call 0x140293670
0038476C  E9 57 FE FF FF                  jmp 0x1403845c8
00384771  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0038477B  48 8B FE                        mov rdi, rsi
0038477E  48 C1 EF 09                     shr rdi, 9
00384782  48 23 F8                        and rdi, rax
00384785  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0038478F  48 8B C0                        mov rax, rax
00384792  48 03 F8                        add rdi, rax
00384795  48 8D 0D A4 36 AB 00            lea rcx, [rip + 0xab36a4]
0038479C  48 8B D7                        mov rdx, rdi
0038479F  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
003847A4  E8 E7 A0 EB FF                  call 0x14023e890
003847A9  E9 55 FE FF FF                  jmp 0x140384603
003847AE  33 C0                           xor eax, eax
003847B0  E9 66 FF FF FF                  jmp 0x14038471b
003847B5  48 8B 4B 70                     mov rcx, qword ptr [rbx + 0x70]
003847B9  E8 F2 04 F1 FF                  call 0x140294cb0
003847BE  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003847C3  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
003847C8  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
003847CD  E9 18 FD FF FF                  jmp 0x1403844ea
003847D2  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
003847DA  49 8B DC                        mov rbx, r12
003847DD  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
003847E2  48 2B 58 30                     sub rbx, qword ptr [rax + 0x30]
003847E6  4D 85 F6                        test r14, r14
003847E9  0F 85 E2 00 00 00               jne 0x1403848d1
003847EF  4D 85 ED                        test r13, r13
003847F2  0F 85 68 03 00 00               jne 0x140384b60
003847F8  48 8B D7                        mov rdx, rdi
003847FB  48 8D 0D 3E 36 AB 00            lea rcx, [rip + 0xab363e]
00384802  E8 B9 26 E9 FF                  call 0x140216ec0
00384807  8A 94 24 D8 00 00 00            mov dl, byte ptr [rsp + 0xd8]
0038480E  48 8D 0D 2B 36 AB 00            lea rcx, [rip + 0xab362b]
00384815  E8 76 8E EF FF                  call 0x14027d690
0038481A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0038481F  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00384824  48 8B D3                        mov rdx, rbx
00384827  E8 54 90 EC FF                  call 0x14024d880
0038482C  48 8D 0D 0D 36 AB 00            lea rcx, [rip + 0xab360d]
00384833  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00384838  4C 8B F0                        mov r14, rax
0038483B  E8 B0 83 EF FF                  call 0x14027cbf0
00384840  48 8B D7                        mov rdx, rdi
00384843  48 8D 0D F6 35 AB 00            lea rcx, [rip + 0xab35f6]
0038484A  E8 41 A0 EB FF                  call 0x14023e890
0038484F  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00384854  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
00384858  41 8B 4E 2C                     mov ecx, dword ptr [r14 + 0x2c]
0038485C  25 FF FF FF 3F                  and eax, 0x3fffffff
00384861  45 8B 76 20                     mov r14d, dword ptr [r14 + 0x20]
00384865  48 2B C8                        sub rcx, rax
00384868  48 2B CA                        sub rcx, rdx
0038486B  41 D1 EE                        shr r14d, 1
0038486E  41 83 E6 1F                     and r14d, 0x1f
00384872  48 8D 41 FF                     lea rax, [rcx - 1]
00384876  48 8D 04 C6                     lea rax, [rsi + rax*8]
0038487A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0038487F  41 8B C6                        mov eax, r14d
00384882  83 E0 05                        and eax, 5
00384885  3C 05                           cmp al, 5
00384887  0F 85 81 FD FF FF               jne 0x14038460e
0038488D  41 83 E6 FE                     and r14d, 0xfffffffe
00384891  E9 78 FD FF FF                  jmp 0x14038460e
00384896  8B 05 1C 22 C4 00               mov eax, dword ptr [rip + 0xc4221c]
0038489C  A8 40                           test al, 0x40
0038489E  0F 84 03 FE FF FF               je 0x1403846a7
003848A4  E8 E7 AB F8 FF                  call 0x14030f490
003848A9  84 C0                           test al, al
003848AB  0F 84 F6 FD FF FF               je 0x1403846a7
003848B1  8B CD                           mov ecx, ebp
003848B3  E8 A8 AB F8 FF                  call 0x14030f460
003848B8  E9 EC FD FF FF                  jmp 0x1403846a9
003848BD  83 E5 EF                        and ebp, 0xffffffef
003848C0  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
003848C5  89 AC 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebp
003848CC  E9 9D FB FF FF                  jmp 0x14038446e
003848D1  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
003848D5  33 D2                           xor edx, edx
003848D7  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
003848DC  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
003848E1  E9 6E FF FF FF                  jmp 0x140384854
003848E6  48 0F BA E7 0A                  bt rdi, 0xa
003848EB  0F 82 DE FC FF FF               jb 0x1403845cf
003848F1  48 0F BA E7 0B                  bt rdi, 0xb
003848F6  0F 83 F2 02 00 00               jae 0x140384bee
003848FC  48 8B CE                        mov rcx, rsi
003848FF  E8 9C DF EF FF                  call 0x1402828a0
00384904  8B AC 24 E8 00 00 00            mov ebp, dword ptr [rsp + 0xe8]
0038490B  48 8B D8                        mov rbx, rax
0038490E  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00384913  48 0F BA E0 0B                  bt rax, 0xb
00384918  0F 83 C1 FC FF FF               jae 0x1403845df
0038491E  48 8B C8                        mov rcx, rax
00384921  E8 EA E0 FE FF                  call 0x140372a10
00384926  85 C0                           test eax, eax
00384928  74 D2                           je 0x1403848fc
0038492A  48 8B 05 4F 93 AA 00            mov rax, qword ptr [rip + 0xaa934f]
00384931  48 85 C0                        test rax, rax
00384934  74 12                           je 0x140384948
00384936  F6 C3 10                        test bl, 0x10
00384939  0F 85 F1 01 00 00               jne 0x140384b30
0038493F  48 8B C8                        mov rcx, rax
00384942  48 F7 D1                        not rcx
00384945  48 23 CB                        and rcx, rbx
00384948  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00384952  48 C1 E9 0C                     shr rcx, 0xc
00384956  48 23 C8                        and rcx, rax
00384959  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00384963  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00384967  48 03 D2                        add rdx, rdx
0038496A  48 8B C0                        mov rax, rax
0038496D  48 3B 0D 6C 93 AA 00            cmp rcx, qword ptr [rip + 0xaa936c]
00384974  48 8D 3C D0                     lea rdi, [rax + rdx*8]
00384978  77 82                           ja 0x1403848fc
0038497A  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00384984  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
00384988  48 C1 E8 36                     shr rax, 0x36
0038498C  41 85 C7                        test r15d, eax
0038498F  0F 84 67 FF FF FF               je 0x1403848fc
00384995  33 ED                           xor ebp, ebp
00384997  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0038499E  0F 82 5B 01 00 00               jb 0x140384aff
003849A4  48 8B CE                        mov rcx, rsi
003849A7  E8 F4 DE EF FF                  call 0x1402828a0
003849AC  48 3B C3                        cmp rax, rbx
003849AF  0F 85 08 01 00 00               jne 0x140384abd
003849B5  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
003849B9  48 8B 15 C8 B6 AA 00            mov rdx, qword ptr [rip + 0xaab6c8]
003849C0  48 C1 E8 2B                     shr rax, 0x2b
003849C4  25 FF 03 00 00                  and eax, 0x3ff
003849C9  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
003849CD  8B 40 04                        mov eax, dword ptr [rax + 4]
003849D0  84 C0                           test al, al
003849D2  79 1D                           jns 0x1403849f1
003849D4  33 D2                           xor edx, edx
003849D6  48 8B CF                        mov rcx, rdi
003849D9  E8 12 00 08 00                  call 0x1404049f0
003849DE  8B AC 24 E8 00 00 00            mov ebp, dword ptr [rsp + 0xe8]
003849E5  48 8B F8                        mov rdi, rax
003849E8  48 85 C0                        test rax, rax
003849EB  0F 84 E9 FB FF FF               je 0x1403845da
003849F1  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003849F5  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
003849FF  48 0B C1                        or rax, rcx
00384A02  48 3B C6                        cmp rax, rsi
00384A05  0F 85 C6 00 00 00               jne 0x140384ad1
00384A0B  8B AC 24 E8 00 00 00            mov ebp, dword ptr [rsp + 0xe8]
00384A12  48 85 FF                        test rdi, rdi
00384A15  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00384A1A  0F 84 BF FB FF FF               je 0x1403845df
00384A20  48 8B 0E                        mov rcx, qword ptr [rsi]
00384A23  48 8B 15 56 92 AA 00            mov rdx, qword ptr [rip + 0xaa9256]
00384A2A  48 8B C1                        mov rax, rcx
00384A2D  48 85 D2                        test rdx, rdx
00384A30  74 12                           je 0x140384a44
00384A32  F6 C1 10                        test cl, 0x10
00384A35  0F 85 FE 00 00 00               jne 0x140384b39
00384A3B  48 8B C2                        mov rax, rdx
00384A3E  48 F7 D0                        not rax
00384A41  48 23 C1                        and rax, rcx
00384A44  48 C1 E8 0C                     shr rax, 0xc
00384A48  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00384A52  48 23 C2                        and rax, rdx
00384A55  49 BB 10 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000010
00384A5F  4C 8D 0C 40                     lea r9, [rax + rax*2]
00384A63  4D 03 C9                        add r9, r9
00384A66  49 8B C3                        mov rax, r11
00384A69  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00384A6E  49 C7 C2 1F FC FF FF            mov r10, 0xfffffffffffffc1f
00384A75  4A 8B 04 C8                     mov rax, qword ptr [rax + r9*8]
00384A79  49 C1 E0 05                     shl r8, 5
00384A7D  49 8B D0                        mov rdx, r8
00384A80  48 33 D0                        xor rdx, rax
00384A83  49 23 D2                        and rdx, r10
00384A86  49 33 D0                        xor rdx, r8
00384A89  49 8B C3                        mov rax, r11
00384A8C  4A 89 14 C8                     mov qword ptr [rax + r9*8], rdx
00384A90  49 8B C0                        mov rax, r8
00384A93  48 33 C1                        xor rax, rcx
00384A96  49 23 C2                        and rax, r10
00384A99  49 33 C0                        xor rax, r8
00384A9C  48 89 06                        mov qword ptr [rsi], rax
00384A9F  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
00384AA9  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00384AB3  F0 4A 21 0C C8                  lock and qword ptr [rax + r9*8], rcx
00384AB8  E9 0B FB FF FF                  jmp 0x1403845c8
00384ABD  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00384AC7  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00384ACC  E9 2B FE FF FF                  jmp 0x1403848fc
00384AD1  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00384AD5  48 0F BA E0 28                  bt rax, 0x28
00384ADA  0F 82 2B FF FF FF               jb 0x140384a0b
00384AE0  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00384AE4  4C 8B CB                        mov r9, rbx
00384AE7  4C 8B C6                        mov r8, rsi
00384AEA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00384AEF  BA 11 04 00 00                  mov edx, 0x411
00384AF4  B9 1A 00 00 00                  mov ecx, 0x1a
00384AF9  E8 62 8B 17 00                  call 0x1404fd660
00384AFE  CC                              int3
00384AFF  41 03 EF                        add ebp, r15d
00384B02  85 2D A4 07 C4 00               test dword ptr [rip + 0xc407a4], ebp
00384B08  0F 84 CD 00 00 00               je 0x140384bdb
00384B0E  F3 90                           pause
00384B10  EB 10                           jmp 0x140384b22
00384B12  E8 79 A9 F8 FF                  call 0x14030f490
00384B17  84 C0                           test al, al
00384B19  74 F3                           je 0x140384b0e
00384B1B  8B CD                           mov ecx, ebp
00384B1D  E8 3E A9 F8 FF                  call 0x14030f460
00384B22  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00384B26  48 85 C0                        test rax, rax
00384B29  78 D4                           js 0x140384aff
00384B2B  E9 67 FE FF FF                  jmp 0x140384997
00384B30  48 83 E1 EF                     and rcx, 0xffffffffffffffef
00384B34  E9 0F FE FF FF                  jmp 0x140384948
00384B39  48 83 E0 EF                     and rax, 0xffffffffffffffef
00384B3D  E9 02 FF FF FF                  jmp 0x140384a44
00384B42  4D 85 ED                        test r13, r13
00384B45  0F 84 9D FE 35 00               je 0x1406e49e8
00384B4B  49 8B CD                        mov rcx, r13
00384B4E  E8 6D D4 F8 FF                  call 0x140311fc0
00384B53  E8 18 F1 F8 FF                  call 0x140313c70
00384B58  45 33 ED                        xor r13d, r13d
00384B5B  E9 88 FE 35 00                  jmp 0x1406e49e8
00384B60  49 8B CD                        mov rcx, r13
00384B63  E8 58 D4 F8 FF                  call 0x140311fc0
00384B68  E8 03 F1 F8 FF                  call 0x140313c70
00384B6D  45 33 ED                        xor r13d, r13d
00384B70  E9 83 FC FF FF                  jmp 0x1403847f8
00384B75  41 8B D6                        mov edx, r14d
00384B78  48 8B CF                        mov rcx, rdi
00384B7B  E8 C8 86 17 00                  call 0x1404fd248
00384B80  E9 9D FA FF FF                  jmp 0x140384622
00384B85  F6 44 24 30 06                  test byte ptr [rsp + 0x30], 6
00384B8A  0F 85 4A FB FF FF               jne 0x1403846da
00384B90  E9 FC FA FF FF                  jmp 0x140384691
00384B95  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00384B99  48 8B D0                        mov rdx, rax
00384B9C  48 8B 05 E5 B4 AA 00            mov rax, qword ptr [rip + 0xaab4e5]
00384BA3  45 8B C7                        mov r8d, r15d
00384BA6  48 C1 E9 2B                     shr rcx, 0x2b
00384BAA  81 E1 FF 03 00 00               and ecx, 0x3ff
00384BB0  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
00384BB4  E8 17 F4 EF FF                  call 0x140283fd0
00384BB9  E9 B2 F9 FF FF                  jmp 0x140384570
00384BBE  48 85 ED                        test rbp, rbp
00384BC1  0F 95 C1                        setne cl
00384BC4  41 84 C7                        test r15b, al
00384BC7  0F 94 C0                        sete al
00384BCA  84 C8                           test al, cl
00384BCC  0F 84 BF F9 FF FF               je 0x140384591
00384BD2  48 83 CB 42                     or rbx, 0x42
00384BD6  E9 B6 F9 FF FF                  jmp 0x140384591
00384BDB  8B 05 D7 1E C4 00               mov eax, dword ptr [rip + 0xc41ed7]
00384BE1  A8 40                           test al, 0x40
00384BE3  0F 84 25 FF FF FF               je 0x140384b0e
00384BE9  E9 24 FF FF FF                  jmp 0x140384b12
00384BEE  48 85 FF                        test rdi, rdi
00384BF1  0F 84 D8 F9 FF FF               je 0x1403845cf
00384BF7  81 FD 00 01 00 00               cmp ebp, 0x100
00384BFD  0F 84 CC F9 FF FF               je 0x1403845cf
00384C03  8B C8                           mov ecx, eax
00384C05  48 C1 E1 05                     shl rcx, 5
00384C09  48 8B C1                        mov rax, rcx
00384C0C  48 33 C7                        xor rax, rdi
00384C0F  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00384C15  48 33 C1                        xor rax, rcx
00384C18  48 89 06                        mov qword ptr [rsi], rax
00384C1B  E9 AF F9 FF FF                  jmp 0x1403845cf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetSystemCodeProtection(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
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
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_pD0;
    unsigned __int8 v_stack_pD8;
    unsigned int v_stack_pE8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (136);
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    if (a4 == 24) goto loc_00384469;
    if ((((unsigned __int8)((unsigned int)(a4))) & (16)) != 0) goto loc_003848BD;
loc_00384469:
    v_stack_m88 = 0;
loc_0038446E:
    v_r12 = (a2) << (25);
    a1 = (v_rsp) << (25);
    v_r12 = (v_r12) - (a1);
    v_r12 = (v_r12) >> (16);
    result = MI_IS_PHYSICAL_ADDRESS(v_r12, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00384718;
    if (((unsigned int)((unsigned int)(a4))) == 256) goto loc_003847B5;
    v_stack_m70 = a3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (5));
    v_stack_m60 = 0;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0xFFFFFFFEULL));
    v_stack_m80 = 0;
    if (((unsigned __int8)(result)) != 5) { v_r14 = (unsigned int)((unsigned int)(a4)); }
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (1));
    a4 = (unsigned int)((a4) & (2));
    result = MiMakeDriverPagesPrivate(a1, a2, a3, a4);
    if (sign_flag) goto loc_003847AE;
loc_003844EA:
    v_rdi = 0;
    v_stack_m90 = 0;
    result = MiLockWorkingSetShared(v_rip + 11221325, a2, a3, a4);
    v_stack_p10 = (unsigned __int8)(result);
    goto loc_003845DF;
loc_00384509:
    if (condition_is_below) goto loc_00384698;
    a2 = ((unsigned int)(v_stack_m98)) << (5);
    a1 = (a2) ^ (*(unsigned __int64 *)(a1 + 16));
    a1 = (a1) & (-993);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(a1 + 16) = a1;
    result = *(unsigned __int64 *)(a1 + 16);
    if (v_stack_m88 != 0) {
        a2 = 4;
        a1 = a1;
        result = MiMarkPfnVerified(a1, a2, a3, a4);
    }
    result = 0;
    v_rbp = (unsigned int)((0) & (66));
    if (condition_is_not_equal) goto loc_003846B8;
loc_00384558:
    if (0 != 0) goto loc_00384B95;
loc_00384570:
    result = MiMakeValidPte(a2, v_stack_m68, (unsigned int)(v_stack_m98), a4);
    if ((((unsigned __int8)((unsigned int)(v_stack_m98))) & (4)) != 0) goto loc_00384BBE;
loc_00384591:
    result = MiWriteValidPteNewProtection(a2, result, (unsigned int)(v_stack_m98), a4);
    if (condition_is_below) goto loc_003845B5;
    if (condition_is_above_or_equal) goto loc_00384730;
loc_003845B5:
    result = MI_TIGHTER_PERMISSIONS(0, result, (unsigned int)(v_stack_m98), a4);
    if ((unsigned int)(result) != 0) goto loc_00384730;
loc_003845C8:
loc_003845CF:
    v_rsi = (a2) + (8);
    v_r12 = (v_r12) + (0x1000ULL);
loc_003845DA:
loc_003845DF:
    if (v_rsi > v_stack_p18) goto loc_003846DD;
    if (v_stack_m90 == 0) goto loc_00384771;
    if (((v_rsi) & (0xFFFULL)) == 0) goto loc_00384B42;
loc_00384603:
    if (v_rsi > v_stack_m70) goto loc_003847D2;
loc_0038460E:
    if (a5 != 0) goto loc_00384B75;
loc_00384622:
    v_stack_m98 = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    if ((((unsigned __int8)(v_r13 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rsi)))) == 0) goto loc_003848E6;
    result = (*(unsigned __int64 *)(v_rsi)) >> (12);
    result = (result) & (0);
    v_stack_m68 = result;
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (result);
    if (sign_flag) goto loc_003845CF;
    a3 = 0;
    result = MiGetPagePrivilege(v_rbx, a3 + 2, a3, a4);
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_00384B85;
    if (((*(unsigned __int64 *)(v_rip + 12854265)) & (0x8000ULL)) != 0) goto loc_003846C5;
loc_00384691:
    v_rbp = 0;
    goto loc_00384509;
loc_00384698:
    v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(v_r13 + 1)));
    if (((*(unsigned int *)(v_rip + 12848139)) & ((unsigned int)(v_rbp))) == 0) goto loc_00384896;
loc_003846A7:
loc_003846A9:
    if (!sign_flag) goto loc_00384509;
    goto loc_00384698;
loc_003846B8:
    result = MiCaptureDirtyBitToPfn(v_rbx, a3 + 2, a3, a4);
    goto loc_00384558;
loc_003846C5:
    if (((v_stack_m98) & (4)) == 0) goto loc_00384691;
    result = (*(unsigned __int64 *)(v_rbx + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_00384691;
loc_003846DA:
    v_r15 = 0;
loc_003846DD:
    if (0 != 0) {
        a1 = 0;
        result = MiFlushTbList(a1, a3 + 2, a3, a4);
        result = MiReleaseProcessorFlushList(a1, a3 + 2, a3, a4);
    }
    if (v_stack_m90 != 0) {
        a1 = v_rip + 11220800;
        result = MiUnlockPageTable(a1, v_stack_m90, a3, a4);
    }
    result = MiUnlockWorkingSetShared(v_rip + 11220781, v_stack_p10, a3, a4);
loc_00384718:
loc_0038471B:
    v_rsp = (v_rsp) + (136);
    return 0;
loc_00384730:
    result = 0;
    if (0 == 0) {
        result = MiGetProcessorFlushList(v_rip + 11220781, v_stack_p10, a3, a4);
        a4 = 0;
        v_stack_p20 = 32;
        a2 = v_rip + 11220724;
        a1 = result;
        v_r13 = result;
        a3 = *(unsigned int *)(result + 12);
        result = MiInitializeTbFlushList(a1, a2, a3, a4);
    }
    a4 = 0;
    result = MiInsertTbFlushEntry(v_r13, v_r12, 0, a4);
    goto loc_003845C8;
loc_00384771:
    v_rdi = (v_rsi) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) + (result);
    v_stack_p38 = v_rdi;
    result = MiLockNestedPageTable(v_rip + 11220644, v_rdi, 0, a4);
    goto loc_00384603;
loc_003847AE:
    result = 0;
    goto loc_0038471B;
loc_003847B5:
    result = MiSectionControlArea(*(unsigned __int64 *)(v_rbx + 112), v_rdi, 0, a4);
    v_stack_p68 = result;
    v_stack_p48 = v_r13;
    v_stack_p58 = v_r13;
    goto loc_003844EA;
loc_003847D2:
    v_rbx = (v_r12) - (*(unsigned __int64 *)(v_stack_pD0 + 48));
    if (v_stack_p48 != 0) goto loc_003848D1;
    if (v_r13 != 0) goto loc_00384B60;
loc_003847F8:
    result = MiUnlockPageTable(v_rip + 11220542, v_rdi, 0, a4);
    result = MiUnlockWorkingSetShared(v_rip + 11220523, v_stack_pD8, 0, a4);
    result = MiOffsetToProtos(v_stack_p68, v_rbx, v_stack_p50, a4);
    v_stack_p48 = result;
    result = MiLockWorkingSetShared(v_rip + 11220493, v_rbx, v_stack_p50, a4);
    result = MiLockNestedPageTable(v_rip + 11220470, v_rdi, v_stack_p50, a4);
loc_00384854:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 52))) & (0x3FFFFFFFULL));
    a1 = ((unsigned int)(*(unsigned int *)(result + 44))) - (result);
    a1 = (a1) - (v_stack_p50);
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (1));
    v_r14 = (unsigned int)((v_r14) & (31));
    v_stack_p58 = v_rsi + a1 - 1 * 8;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (5));
    if (((unsigned __int8)(result)) != 5) goto loc_0038460E;
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFFEULL));
    goto loc_0038460E;
loc_00384896:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12853788)))) & (64)) == 0) goto loc_003846A7;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_stack_p50, v_stack_p50, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003846A7;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), v_stack_p50, v_stack_p50, a4);
    goto loc_003846A9;
loc_003848BD:
    v_rbp = (unsigned int)((v_rbp) & (0xFFFFFFEFULL));
    v_stack_p40 = 0;
    v_stack_pE8 = (unsigned int)(v_rbp);
    goto loc_0038446E;
loc_003848D1:
    a2 = 0;
    v_stack_p48 = *(unsigned __int64 *)(v_r14 + 16);
    v_stack_p50 = 0;
    goto loc_00384854;
loc_003848E6:
    if (condition_is_below) goto loc_003845CF;
    if (condition_is_above_or_equal) goto loc_00384BEE;
loc_003848FC:
    result = MI_READ_PTE_LOCK_FREE(v_rsi, a2, v_stack_p50, a4);
    if (condition_is_above_or_equal) goto loc_003845DF;
    result = MiInvalidPteConforms(result, a2, v_stack_p50, a4);
    if ((unsigned int)(result) == 0) goto loc_003848FC;
    if (*(unsigned __int64 *)(v_rip + 11178831) == 0) goto loc_00384948;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00384B30;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11178831));
    a1 = (a1) & (result);
loc_00384948:
    a1 = (a1) >> (12);
    a1 = (a1) & (*(unsigned __int64 *)(v_rip + 11178831));
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 11178860))) goto loc_003848FC;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11178831) + a2 * 8)) >> (54);
    if (((0) & ((unsigned int)(result))) == 0) goto loc_003848FC;
    v_rbp = 0;
loc_00384997:
    if (condition_is_below) goto loc_00384AFF;
    result = MI_READ_PTE_LOCK_FREE(v_rsi, a2, v_stack_p50, a4);
    if (result != result) goto loc_00384ABD;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11178831) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (!sign_flag) goto loc_003849F1;
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(unsigned __int64 *)(v_rip + 11178831) + a2 * 8, a2, v_stack_p50, a4);
    if (result == 0) goto loc_003845DA;
loc_003849F1:
    result = (*(unsigned __int64 *)(result + 8)) | (*(unsigned __int64 *)(v_rip + 11178831) + a2 * 8);
    if (result != v_rsi) goto loc_00384AD1;
loc_00384A0B:
    if (result == 0) goto loc_003845DF;
    if (*(unsigned __int64 *)(v_rip + 11178582) == 0) goto loc_00384A44;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi))) & (16)) != 0) goto loc_00384B39;
    result = ~(*(unsigned __int64 *)(v_rip + 11178582));
    result = (result) & (*(unsigned __int64 *)(v_rsi));
loc_00384A44:
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 11178582));
    a4 = (result + result * 2) + (result + result * 2);
    a3 = ((unsigned int)(v_stack_p30)) << (5);
    a2 = (a3) ^ (*(unsigned __int64 *)(v_r11 + a4 * 8));
    a2 = (a2) & (-993);
    a2 = (a2) ^ (a3);
    *(unsigned __int64 *)(v_r11 + a4 * 8) = a2;
    result = (a3) ^ (*(unsigned __int64 *)(v_rsi));
    result = (result) & (-993);
    result = (result) ^ (a3);
    *(unsigned __int64 *)(v_rsi) = result;
    goto loc_003845C8;
loc_00384ABD:
    goto loc_003848FC;
loc_00384AD1:
    if (condition_is_below) goto loc_00384A0B;
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p38 + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), v_rsi, result);
loc_00384AFF:
    v_rbp = (unsigned int)(((unsigned int)(v_stack_pE8)) + (0));
    if (((*(unsigned int *)(v_rip + 12847012)) & ((unsigned int)(v_rbp))) == 0) goto loc_00384BDB;
loc_00384B0E:
    goto loc_00384B22;
loc_00384B12:
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), v_rsi, result);
    if ((unsigned __int8)(result) == 0) goto loc_00384B0E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0x411ULL), v_rsi, result);
loc_00384B22:
    if (sign_flag) goto loc_00384AFF;
    goto loc_00384997;
loc_00384B30:
    a1 = ((unsigned int)((unsigned int)(v_rbp))) & (-17);
    goto loc_00384948;
loc_00384B39:
    result = (*(unsigned __int64 *)(v_stack_p38 + 24)) & (-17);
    goto loc_00384A44;
loc_00384B42:
    result = MiFlushTbList(v_r13, (unsigned int)(0x411ULL), v_rsi, result);
    result = MiReleaseProcessorFlushList(v_r13, (unsigned int)(0x411ULL), v_rsi, result);
    v_r13 = 0;
loc_00384B60:
    result = MiFlushTbList(0, (unsigned int)(0x411ULL), v_rsi, result);
    result = MiReleaseProcessorFlushList(0, (unsigned int)(0x411ULL), v_rsi, result);
    v_r13 = 0;
    goto loc_003847F8;
loc_00384B75:
    result = MiRestrictSystemCodeProtection(v_stack_p38, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_r14 + 16))), v_rsi, result);
    goto loc_00384622;
loc_00384B85:
    if (((v_stack_p30) & (6)) != 0) goto loc_003846DA;
    goto loc_00384691;
loc_00384B95:
    a1 = (*(unsigned __int64 *)(result + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = MiReleasePageFileInfo(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11187429) + a1 * 8), result, 0, result);
    goto loc_00384570;
loc_00384BBE:
    a1 = (v_rbp != 0) ? 1 : 0;
    result = (((0) & ((unsigned __int8)(result))) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00384591;
    v_rbx = (result) | (66);
    goto loc_00384591;
loc_00384BDB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12852951)))) & (64)) == 0) goto loc_00384B0E;
    goto loc_00384B12;
loc_00384BEE:
    if (v_stack_p38 == 0) goto loc_003845CF;
    if (((unsigned int)(v_rbp)) == 256) goto loc_003845CF;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12852951))))) << (5);
    result = (a1) ^ (v_stack_p38);
    result = (result) & (-993);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rsi) = result;
    goto loc_003845CF;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetSystemCodeProtection(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

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
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_pD0;
    uint8_t v_stack_pD8;
    uint32_t v_stack_pE8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (136);
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    if (Arg4 == 24) goto loc_00384469;
    if ((((uint8_t)((uint32_t)(Arg4))) & (16)) != 0) goto loc_003848BD;
loc_00384469:
    v_stack_m88 = 0;
loc_0038446E:
    local_r12 = (Arg2) << (25);
    Arg1 = (local_rsp) << (25);
    local_r12 = (local_r12) - (Arg1);
    local_r12 = (local_r12) >> (16);
    result = MI_IS_PHYSICAL_ADDRESS(local_r12, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00384718;
    if (((uint32_t)((uint32_t)(Arg4))) == 256) goto loc_003847B5;
    v_stack_m70 = Arg3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (5));
    v_stack_m60 = 0;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0xFFFFFFFEULL));
    v_stack_m80 = 0;
    if (((uint8_t)(result)) != 5) { local_r14 = (uint32_t)((uint32_t)(Arg4)); }
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (1));
    Arg4 = (uint32_t)((Arg4) & (2));
    result = MiMakeDriverPagesPrivate(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_003847AE;
loc_003844EA:
    local_rdi = 0;
    v_stack_m90 = 0;
    result = MiLockWorkingSetShared(v_rip + 11221325, Arg2, Arg3, Arg4);
    v_stack_p10 = (uint8_t)(result);
    goto loc_003845DF;
loc_00384509:
    if (condition_is_below) goto loc_00384698;
    Arg2 = ((uint32_t)(v_stack_m98)) << (5);
    Arg1 = (Arg2) ^ (*(uint64_t *)(arg1 + 0x10));
    Arg1 = (Arg1) & (-993);
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(arg1 + 0x10) = Arg1;
    result = *(uint64_t *)(arg1 + 0x10);
    if (v_stack_m88 != 0) {
        Arg2 = 4;
        Arg1 = Arg1;
        result = MiMarkPfnVerified(Arg1, Arg2, Arg3, Arg4);
    }
    result = 0;
    local_rbp = (uint32_t)((0) & (66));
    if (condition_is_not_equal) goto loc_003846B8;
loc_00384558:
    if (0 != 0) goto loc_00384B95;
loc_00384570:
    result = MiMakeValidPte(Arg2, v_stack_m68, (uint32_t)(v_stack_m98), Arg4);
    if ((((uint8_t)((uint32_t)(v_stack_m98))) & (4)) != 0) goto loc_00384BBE;
loc_00384591:
    result = MiWriteValidPteNewProtection(Arg2, result, (uint32_t)(v_stack_m98), Arg4);
    if (condition_is_below) goto loc_003845B5;
    if (condition_is_above_or_equal) goto loc_00384730;
loc_003845B5:
    result = MI_TIGHTER_PERMISSIONS(0, result, (uint32_t)(v_stack_m98), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00384730;
loc_003845C8:
loc_003845CF:
    local_rsi = (Arg2) + (8);
    local_r12 = (local_r12) + (0x1000ULL);
loc_003845DA:
loc_003845DF:
    if (local_rsi > v_stack_p18) goto loc_003846DD;
    if (v_stack_m90 == 0) goto loc_00384771;
    if (((local_rsi) & (0xFFFULL)) == 0) goto loc_00384B42;
loc_00384603:
    if (local_rsi > v_stack_m70) goto loc_003847D2;
loc_0038460E:
    if (Arg5 != 0) goto loc_00384B75;
loc_00384622:
    v_stack_m98 = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    if ((((uint8_t)(local_r13 + 1)) & ((uint8_t)(*(uint64_t *)(local_rsi)))) == 0) goto loc_003848E6;
    result = (*(uint64_t *)(local_rsi)) >> (12);
    result = (result) & (0);
    v_stack_m68 = result;
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (result);
    if (sign_flag) goto loc_003845CF;
    Arg3 = 0;
    result = MiGetPagePrivilege(local_rbx, Arg3 + 2, Arg3, Arg4);
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_00384B85;
    if (((*(uint64_t *)(v_rip + 0xC423F9)) & (0x8000ULL)) != 0) goto loc_003846C5;
loc_00384691:
    local_rbp = 0;
    goto loc_00384509;
loc_00384698:
    local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(local_r13 + 1)));
    if (((*(uint32_t *)(v_rip + 0xC40C0B)) & ((uint32_t)(local_rbp))) == 0) goto loc_00384896;
loc_003846A7:
loc_003846A9:
    if (!sign_flag) goto loc_00384509;
    goto loc_00384698;
loc_003846B8:
    result = MiCaptureDirtyBitToPfn(local_rbx, Arg3 + 2, Arg3, Arg4);
    goto loc_00384558;
loc_003846C5:
    if (((v_stack_m98) & (4)) == 0) goto loc_00384691;
    result = (*(uint64_t *)(local_rbx + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 3) goto loc_00384691;
loc_003846DA:
    local_r15 = 0;
loc_003846DD:
    if (0 != 0) {
        Arg1 = 0;
        result = MiFlushTbList(Arg1, Arg3 + 2, Arg3, Arg4);
        result = MiReleaseProcessorFlushList(Arg1, Arg3 + 2, Arg3, Arg4);
    }
    if (v_stack_m90 != 0) {
        Arg1 = v_rip + 11220800;
        result = MiUnlockPageTable(Arg1, v_stack_m90, Arg3, Arg4);
    }
    result = MiUnlockWorkingSetShared(v_rip + 11220781, v_stack_p10, Arg3, Arg4);
loc_00384718:
loc_0038471B:
    local_rsp = (local_rsp) + (136);
    return 0;
loc_00384730:
    result = 0;
    if (0 == 0) {
        result = MiGetProcessorFlushList(v_rip + 11220781, v_stack_p10, Arg3, Arg4);
        Arg4 = 0;
        v_stack_p20 = 32;
        Arg2 = v_rip + 11220724;
        Arg1 = result;
        local_r13 = result;
        Arg3 = *(uint32_t *)(result + 0xC);
        result = MiInitializeTbFlushList(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    result = MiInsertTbFlushEntry(local_r13, local_r12, 0, Arg4);
    goto loc_003845C8;
loc_00384771:
    local_rdi = (local_rsi) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) + (result);
    v_stack_p38 = local_rdi;
    result = MiLockNestedPageTable(v_rip + 11220644, local_rdi, 0, Arg4);
    goto loc_00384603;
loc_003847AE:
    result = 0;
    goto loc_0038471B;
loc_003847B5:
    result = MiSectionControlArea(*(uint64_t *)(local_rbx + 0x70), local_rdi, 0, Arg4);
    v_stack_p68 = result;
    v_stack_p48 = local_r13;
    v_stack_p58 = local_r13;
    goto loc_003844EA;
loc_003847D2:
    local_rbx = (local_r12) - (*(uint64_t *)(v_stack_pD0 + 0x30));
    if (v_stack_p48 != 0) goto loc_003848D1;
    if (local_r13 != 0) goto loc_00384B60;
loc_003847F8:
    result = MiUnlockPageTable(v_rip + 11220542, local_rdi, 0, Arg4);
    result = MiUnlockWorkingSetShared(v_rip + 11220523, v_stack_pD8, 0, Arg4);
    result = MiOffsetToProtos(v_stack_p68, local_rbx, v_stack_p50, Arg4);
    v_stack_p48 = result;
    result = MiLockWorkingSetShared(v_rip + 11220493, local_rbx, v_stack_p50, Arg4);
    result = MiLockNestedPageTable(v_rip + 11220470, local_rdi, v_stack_p50, Arg4);
loc_00384854:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x34))) & (0x3FFFFFFFULL));
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x2C))) - (result);
    Arg1 = (Arg1) - (v_stack_p50);
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (1));
    local_r14 = (uint32_t)((local_r14) & (31));
    v_stack_p58 = local_rsi + Arg1 - 1 * 8;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (5));
    if (((uint8_t)(result)) != 5) goto loc_0038460E;
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFFEULL));
    goto loc_0038460E;
loc_00384896:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4221C)))) & (64)) == 0) goto loc_003846A7;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, v_stack_p50, v_stack_p50, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003846A7;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), v_stack_p50, v_stack_p50, Arg4);
    goto loc_003846A9;
loc_003848BD:
    local_rbp = (uint32_t)((local_rbp) & (0xFFFFFFEFULL));
    v_stack_p40 = 0;
    v_stack_pE8 = (uint32_t)(local_rbp);
    goto loc_0038446E;
loc_003848D1:
    Arg2 = 0;
    v_stack_p48 = *(uint64_t *)(local_r14 + 0x10);
    v_stack_p50 = 0;
    goto loc_00384854;
loc_003848E6:
    if (condition_is_below) goto loc_003845CF;
    if (condition_is_above_or_equal) goto loc_00384BEE;
loc_003848FC:
    result = MI_READ_PTE_LOCK_FREE(local_rsi, Arg2, v_stack_p50, Arg4);
    if (condition_is_above_or_equal) goto loc_003845DF;
    result = MiInvalidPteConforms(result, Arg2, v_stack_p50, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003848FC;
    if (*(uint64_t *)(v_rip + 0xAA934F) == 0) goto loc_00384948;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00384B30;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xAA934F));
    Arg1 = (Arg1) & (result);
loc_00384948:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (*(uint64_t *)(v_rip + 0xAA934F));
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xAA936C))) goto loc_003848FC;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAA934F) + Arg2 * 8)) >> (54);
    if (((0) & ((uint32_t)(result))) == 0) goto loc_003848FC;
    local_rbp = 0;
loc_00384997:
    if (condition_is_below) goto loc_00384AFF;
    result = MI_READ_PTE_LOCK_FREE(local_rsi, Arg2, v_stack_p50, Arg4);
    if (result != result) goto loc_00384ABD;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAA934F) + Arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (!sign_flag) goto loc_003849F1;
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(uint64_t *)(v_rip + 0xAA934F) + Arg2 * 8, Arg2, v_stack_p50, Arg4);
    if (result == 0) goto loc_003845DA;
loc_003849F1:
    result = (*(uint64_t *)(result + 0x8)) | (*(uint64_t *)(v_rip + 0xAA934F) + Arg2 * 8);
    if (result != local_rsi) goto loc_00384AD1;
loc_00384A0B:
    if (result == 0) goto loc_003845DF;
    if (*(uint64_t *)(v_rip + 0xAA9256) == 0) goto loc_00384A44;
    if ((((uint8_t)(*(uint64_t *)(local_rsi))) & (16)) != 0) goto loc_00384B39;
    result = ~(*(uint64_t *)(v_rip + 0xAA9256));
    result = (result) & (*(uint64_t *)(local_rsi));
loc_00384A44:
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xAA9256));
    Arg4 = (result + result * 2) + (result + result * 2);
    Arg3 = ((uint32_t)(v_stack_p30)) << (5);
    Arg2 = (Arg3) ^ (*(uint64_t *)(local_r11 + Arg4 * 8));
    Arg2 = (Arg2) & (-993);
    Arg2 = (Arg2) ^ (Arg3);
    *(uint64_t *)(local_r11 + Arg4 * 8) = Arg2;
    result = (Arg3) ^ (*(uint64_t *)(local_rsi));
    result = (result) & (-993);
    result = (result) ^ (Arg3);
    *(uint64_t *)(local_rsi) = result;
    goto loc_003845C8;
loc_00384ABD:
    goto loc_003848FC;
loc_00384AD1:
    if (condition_is_below) goto loc_00384A0B;
    v_stack_p20 = *(uint64_t *)(v_stack_p38 + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), local_rsi, result);
loc_00384AFF:
    local_rbp = (uint32_t)(((uint32_t)(v_stack_pE8)) + (0));
    if (((*(uint32_t *)(v_rip + 0xC407A4)) & ((uint32_t)(local_rbp))) == 0) goto loc_00384BDB;
loc_00384B0E:
    goto loc_00384B22;
loc_00384B12:
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), local_rsi, result);
    if ((uint8_t)(result) == 0) goto loc_00384B0E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0x411ULL), local_rsi, result);
loc_00384B22:
    if (sign_flag) goto loc_00384AFF;
    goto loc_00384997;
loc_00384B30:
    Arg1 = ((uint32_t)((uint32_t)(local_rbp))) & (-17);
    goto loc_00384948;
loc_00384B39:
    result = (*(uint64_t *)(v_stack_p38 + 0x18)) & (-17);
    goto loc_00384A44;
loc_00384B42:
    result = MiFlushTbList(local_r13, (uint32_t)(0x411ULL), local_rsi, result);
    result = MiReleaseProcessorFlushList(local_r13, (uint32_t)(0x411ULL), local_rsi, result);
    local_r13 = 0;
loc_00384B60:
    result = MiFlushTbList(0, (uint32_t)(0x411ULL), local_rsi, result);
    result = MiReleaseProcessorFlushList(0, (uint32_t)(0x411ULL), local_rsi, result);
    local_r13 = 0;
    goto loc_003847F8;
loc_00384B75:
    result = MiRestrictSystemCodeProtection(v_stack_p38, (uint32_t)((uint32_t)(*(uint64_t *)(local_r14 + 0x10))), local_rsi, result);
    goto loc_00384622;
loc_00384B85:
    if (((v_stack_p30) & (6)) != 0) goto loc_003846DA;
    goto loc_00384691;
loc_00384B95:
    Arg1 = (*(uint64_t *)(result + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = MiReleasePageFileInfo(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAB4E5) + arg1 * 8), result, 0, result);
    goto loc_00384570;
loc_00384BBE:
    Arg1 = (local_rbp != 0) ? 1 : 0;
    result = (((0) & ((uint8_t)(result))) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00384591;
    local_rbx = (result) | (66);
    goto loc_00384591;
loc_00384BDB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC41ED7)))) & (64)) == 0) goto loc_00384B0E;
    goto loc_00384B12;
loc_00384BEE:
    if (v_stack_p38 == 0) goto loc_003845CF;
    if (((uint32_t)(local_rbp)) == 256) goto loc_003845CF;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC41ED7))))) << (5);
    result = (Arg1) ^ (v_stack_p38);
    result = (result) & (-993);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rsi) = result;
    goto loc_003845CF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00384420&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
