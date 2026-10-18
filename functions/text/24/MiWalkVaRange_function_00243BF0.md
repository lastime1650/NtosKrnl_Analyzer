# MiWalkVaRange

- RVA: `0x00243BF0`–`0x00244C82` (길이 `4,242` bytes)
- VA: `0x0000000140243BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00061CC0`
- 디코드: `975`개 명령, `4,242/4,242` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x00243CA5` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00243CCA` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00243D00` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x00243D38` → [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x00243EA3` → [MiRemoveLockedPageChargeAndDecRef](MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x00243EDA` → [MiRemoveLockedPageChargeAndDecRef](MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x00243F5C` → [MiActOnPte](MiActOnPte_function_00244C90.md) (function, `0x00244C90`)
- `0x0024409D` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00244204` → [MiUnlockProtoPoolPage](MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00244220` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00244275` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00244287` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002442AF` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00244302` → [MiGetProcessorFlushList](MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00244459` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0024448E` → [EtwTraceShouldYieldProcessor](../27/EtwTraceShouldYieldProcessor_function_00279088.md) (function, `0x00279088`)
- `0x00244594` → [MI_PROTO_FORMAT_COMBINED](../22/MI_PROTO_FORMAT_COMBINED_function_0022F720.md) (function, `0x0022F720`)
- `0x002445EC` → [MiUnlockProtoPoolPage](MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002445FE` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x00244629` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0024473B` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x0024476C` → [MiUnlockProtoPoolPage](MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0024478A` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002447D1` → [MiWalkPageTables](../2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x002447F7` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00244806` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024482E` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x002448CE` → [MiGetAnyMultiplexedVm](../44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x002448FA` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00244904` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x0024493A` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00244A01` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00244A06` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00244A27` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00244A3D` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00244A4F` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00244A6D` → [MI_PROTO_FORMAT_COMBINED](../22/MI_PROTO_FORMAT_COMBINED_function_0022F720.md) (function, `0x0022F720`)
- `0x00244A8F` → [MiUnlockProtoPoolPage](MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00244AAC` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00244AB1` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00244ACD` → [MiMakeProtoLeafValid](../2A/MiMakeProtoLeafValid_function_002A6710.md) (function, `0x002A6710`)
- `0x00244B59` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00244B64` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x00244BFB` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00244C0A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00244C6D` → [LOCK_ADDRESS_SPACE](../2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (function, `0x002A4944`)
- `0x00244C78` → [UNLOCK_ADDRESS_SPACE](../2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)

### Direct callers
- [MiResetVirtualMemory](../44/MiResetVirtualMemory_function_004486F0.md) at `0x00448758`
- [MiProcessVaRangesInfoClass](../../page/9F/MiProcessVaRangesInfoClass_function_009F4E50.md) at `0x009F4F34`

### Static image references
- `0x002440C2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002440DF` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0024447B` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00244552` → RVA `0x00E38840` (`.data`; read)
- `0x002445A1` → RVA `0x00E2DC80` (`.data`; read)
- `0x0024461C` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002447BA` → RVA `0x00313710` (`MiGetNextPageTableTail`; read)
- `0x002447E9` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002448B3` → RVA `0x00E2F380` (`.data`; read)
- `0x002448BC` → RVA `0x00E2F390` (`.data`; read)
- `0x002448ED` → RVA `0x00695890` (`MiTbFlushSort`; read)
- `0x00244B11` → RVA `0x00E2DB78` (`.data`; read)
- `0x00244BE1` → RVA `0x0100F4C0` (`INITDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002448AE` → [sub_006D7EC6](../6D/Unknown_function_006D7EC6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00243BF0  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00243BF5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00243BFA  55                              push rbp
00243BFB  53                              push rbx
00243BFC  56                              push rsi
00243BFD  57                              push rdi
00243BFE  41 54                           push r12
00243C00  41 55                           push r13
00243C02  41 56                           push r14
00243C04  41 57                           push r15
00243C06  48 8D AC 24 78 FF FF FF         lea rbp, [rsp - 0x88]
00243C0E  48 81 EC 88 01 00 00            sub rsp, 0x188
00243C15  4C 8B F9                        mov r15, rcx
00243C18  C6 85 D0 00 00 00 11            mov byte ptr [rbp + 0xd0], 0x11
00243C1F  33 C9                           xor ecx, ecx
00243C21  49 C1 EF 09                     shr r15, 9
00243C25  48 8B DA                        mov rbx, rdx
00243C28  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00243C2C  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
00243C36  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00243C3A  4C 23 FA                        and r15, rdx
00243C3D  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00243C41  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
00243C45  44 8B E9                        mov r13d, ecx
00243C48  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00243C4C  44 8B E1                        mov r12d, ecx
00243C4F  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00243C54  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00243C59  48 BF 00 00 00 00 80 F6 FF FF   movabs rdi, 0xfffff68000000000
00243C63  48 8B C7                        mov rax, rdi
00243C66  48 C1 EB 09                     shr rbx, 9
00243C6A  4C 03 F8                        add r15, rax
00243C6D  48 23 DA                        and rbx, rdx
00243C70  48 8B C7                        mov rax, rdi
00243C73  48 03 D8                        add rbx, rax
00243C76  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00243C7B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00243C84  48 89 9D D8 00 00 00            mov qword ptr [rbp + 0xd8], rbx
00243C8B  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00243C92  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00243C96  48 8D B0 00 04 00 00            lea rsi, [rax + 0x400]
00243C9D  48 8B CE                        mov rcx, rsi
00243CA0  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
00243CA5  E8 46 8F 03 00                  call 0x14027cbf0
00243CAA  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00243CAE  4C 3B FB                        cmp r15, rbx
00243CB1  0F 87 9A 07 00 00               ja 0x140244451
00243CB7  0F 57 C0                        xorps xmm0, xmm0
00243CBA  48 8D 4D C4                     lea rcx, [rbp - 0x3c]
00243CBE  33 D2                           xor edx, edx
00243CC0  41 B8 BC 00 00 00               mov r8d, 0xbc
00243CC6  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00243CCA  E8 71 2F 48 00                  call 0x1406c6c40
00243CCF  48 8B C7                        mov rax, rdi
00243CD2  48 C1 E0 19                     shl rax, 0x19
00243CD6  49 8B FF                        mov rdi, r15
00243CD9  48 C1 E7 19                     shl rdi, 0x19
00243CDD  48 8B F3                        mov rsi, rbx
00243CE0  48 2B F8                        sub rdi, rax
00243CE3  48 C1 E6 19                     shl rsi, 0x19
00243CE7  48 2B F0                        sub rsi, rax
00243CEA  48 C1 FF 10                     sar rdi, 0x10
00243CEE  48 8B CF                        mov rcx, rdi
00243CF1  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00243CF5  48 C1 FE 10                     sar rsi, 0x10
00243CF9  C7 45 C0 61 20 00 00            mov dword ptr [rbp - 0x40], 0x2061
00243D00  E8 9B 83 03 00                  call 0x14027c0a0
00243D05  48 B9 00 00 00 00 00 80 FF FF   movabs rcx, 0xffff800000000000
00243D0F  48 3B C1                        cmp rax, rcx
00243D12  0F 83 9B 0B 00 00               jae 0x1402448b3
00243D18  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00243D21  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00243D28  48 81 C3 00 04 00 00            add rbx, 0x400
00243D2F  45 33 C0                        xor r8d, r8d
00243D32  48 8B D7                        mov rdx, rdi
00243D35  48 8B CB                        mov rcx, rbx
00243D38  E8 03 26 03 00                  call 0x140276340
00243D3D  85 C0                           test eax, eax
00243D3F  0F 84 4F 0A 00 00               je 0x140244794
00243D45  FF C8                           dec eax
00243D47  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
00243D51  48 8B DF                        mov rbx, rdi
00243D54  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00243D57  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00243D61  48 C1 EB 09                     shr rbx, 9
00243D65  48 23 D8                        and rbx, rax
00243D68  48 8B C6                        mov rax, rsi
00243D6B  48 03 D8                        add rbx, rax
00243D6E  48 89 5D B0                     mov qword ptr [rbp - 0x50], rbx
00243D72  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
00243D7A  49 3B DF                        cmp rbx, r15
00243D7D  0F 85 A0 06 00 00               jne 0x140244423
00243D83  45 33 D2                        xor r10d, r10d
00243D86  48 85 DB                        test rbx, rbx
00243D89  74 1F                           je 0x140243daa
00243D8B  48 8B CB                        mov rcx, rbx
00243D8E  49 BE F8 FF FF FF 7F 00 00 00   movabs r14, 0x7ffffffff8
00243D98  48 C1 E9 09                     shr rcx, 9
00243D9C  49 23 CE                        and rcx, r14
00243D9F  48 8B C6                        mov rax, rsi
00243DA2  48 03 C8                        add rcx, rax
00243DA5  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00243DAA  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00243DAF  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
00243DB3  4C 89 55 98                     mov qword ptr [rbp - 0x68], r10
00243DB7  49 8B FA                        mov rdi, r10
00243DBA  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
00243DBF  45 8B EA                        mov r13d, r10d
00243DC2  41 8B F2                        mov esi, r10d
00243DC5  85 C9                           test ecx, ecx
00243DC7  0F 84 94 02 00 00               je 0x140244061
00243DCD  49 8B 1F                        mov rbx, qword ptr [r15]
00243DD0  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00243DDA  48 8B C0                        mov rax, rax
00243DDD  4C 3B F8                        cmp r15, rax
00243DE0  72 2B                           jb 0x140243e0d
00243DE2  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00243DEC  48 8B C0                        mov rax, rax
00243DEF  4C 3B F8                        cmp r15, rax
00243DF2  77 19                           ja 0x140243e0d
00243DF4  F6 C3 01                        test bl, 1
00243DF7  74 14                           je 0x140243e0d
00243DF9  F6 C3 42                        test bl, 0x42
00243DFC  0F 95 C1                        setne cl
00243DFF  F6 C3 20                        test bl, 0x20
00243E02  0F 95 C0                        setne al
00243E05  84 C8                           test al, cl
00243E07  0F 84 D2 02 00 00               je 0x1402440df
00243E0D  48 85 DB                        test rbx, rbx
00243E10  0F 84 4B 02 00 00               je 0x140244061
00243E16  F6 C3 01                        test bl, 1
00243E19  75 0B                           jne 0x140243e26
00243E1B  48 0F BA E3 0A                  bt rbx, 0xa
00243E20  0F 82 33 0C 00 00               jb 0x140244a59
00243E26  4D 85 F6                        test r14, r14
00243E29  0F 84 F4 00 00 00               je 0x140243f23
00243E2F  33 DB                           xor ebx, ebx
00243E31  80 BD D0 00 00 00 12            cmp byte ptr [rbp + 0xd0], 0x12
00243E38  0F 84 22 0B 00 00               je 0x140244960
00243E3E  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00243E45  0F 82 75 02 00 00               jb 0x1402440c0
00243E4B  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00243E4F  48 85 C0                        test rax, rax
00243E52  78 1D                           js 0x140243e71
00243E54  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00243E58  48 0F BA E0 28                  bt rax, 0x28
00243E5D  72 12                           jb 0x140243e71
00243E5F  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00243E63  48 C1 E8 3C                     shr rax, 0x3c
00243E67  24 07                           and al, 7
00243E69  3C 01                           cmp al, 1
00243E6B  74 04                           je 0x140243e71
00243E6D  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00243E71  49 8B 06                        mov rax, qword ptr [r14]
00243E74  48 B9 FE FF FF FF FF 0F 00 00   movabs rcx, 0xffffffffffe
00243E7E  48 85 C1                        test rcx, rax
00243E81  0F 85 E5 02 00 00               jne 0x14024416c
00243E87  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00243E8B  49 8B CE                        mov rcx, r14
00243E8E  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00243E92  C1 E8 10                        shr eax, 0x10
00243E95  24 DF                           and al, 0xdf
00243E97  88 44 24 72                     mov byte ptr [rsp + 0x72], al
00243E9B  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00243E9F  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00243EA3  E8 28 1B 00 00                  call 0x1402459d0
00243EA8  EB 42                           jmp 0x140243eec
00243EAA  48 89 12                        mov qword ptr [rdx], rdx
00243EAD  48 8B C2                        mov rax, rdx
00243EB0  48 89 42 08                     mov qword ptr [rdx + 8], rax
00243EB4  49 8B 06                        mov rax, qword ptr [r14]
00243EB7  48 C1 EA 04                     shr rdx, 4
00243EBB  48 03 D2                        add rdx, rdx
00243EBE  48 8B CA                        mov rcx, rdx
00243EC1  48 33 C8                        xor rcx, rax
00243EC4  48 B8 01 00 00 00 00 F0 FF FF   movabs rax, 0xfffff00000000001
00243ECE  48 23 C8                        and rcx, rax
00243ED1  48 33 CA                        xor rcx, rdx
00243ED4  49 89 0E                        mov qword ptr [r14], rcx
00243ED7  49 8B CE                        mov rcx, r14
00243EDA  E8 F1 1A 00 00                  call 0x1402459d0
00243EDF  48 85 DB                        test rbx, rbx
00243EE2  74 08                           je 0x140243eec
00243EE4  B8 01 00 00 00                  mov eax, 1
00243EE9  89 43 10                        mov dword ptr [rbx + 0x10], eax
00243EEC  80 BD D0 00 00 00 12            cmp byte ptr [rbp + 0xd0], 0x12
00243EF3  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00243EFD  0F 84 F1 07 00 00               je 0x1402446f4
00243F03  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00243F08  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
00243F0F  80 FA 01                        cmp dl, 1
00243F12  0F 86 04 07 00 00               jbe 0x14024461c
00243F18  45 33 F6                        xor r14d, r14d
00243F1B  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00243F20  45 33 E4                        xor r12d, r12d
00243F23  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
00243F27  48 8D 45 90                     lea rax, [rbp - 0x70]
00243F2B  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
00243F32  4C 8B CF                        mov r9, rdi
00243F35  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00243F3A  4D 8B C7                        mov r8, r15
00243F3D  48 8D 45 A0                     lea rax, [rbp - 0x60]
00243F41  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00243F46  48 8B 85 F0 00 00 00            mov rax, qword ptr [rbp + 0xf0]
00243F4D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00243F52  8B 85 E8 00 00 00               mov eax, dword ptr [rbp + 0xe8]
00243F58  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00243F5C  E8 2F 0D 00 00                  call 0x140244c90
00243F61  85 C0                           test eax, eax
00243F63  0F 85 66 03 00 00               jne 0x1402442cf
00243F69  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00243F6D  48 85 D2                        test rdx, rdx
00243F70  0F 85 E7 07 00 00               jne 0x14024475d
00243F76  49 83 C7 08                     add r15, 8
00243F7A  8B C6                           mov eax, esi
00243F7C  49 8B CF                        mov rcx, r15
00243F7F  45 85 ED                        test r13d, r13d
00243F82  0F 85 64 02 00 00               jne 0x1402441ec
00243F88  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00243F8D  44 8B E8                        mov r13d, eax
00243F90  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00243F95  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00243F9A  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00243F9F  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00243FA4  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00243FA9  85 C0                           test eax, eax
00243FAB  0F 88 40 02 00 00               js 0x1402441f1
00243FB1  48 3B 8D D8 00 00 00            cmp rcx, qword ptr [rbp + 0xd8]
00243FB8  0F 87 33 02 00 00               ja 0x1402441f1
00243FBE  48 F7 C1 FF 0F 00 00            test rcx, 0xfff
00243FC5  0F 84 26 02 00 00               je 0x1402441f1
00243FCB  F6 C1 78                        test cl, 0x78
00243FCE  0F 84 59 05 00 00               je 0x14024452d
00243FD4  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00243FDD  45 33 D2                        xor r10d, r10d
00243FE0  45 8B C2                        mov r8d, r10d
00243FE3  45 8B CA                        mov r9d, r10d
00243FE6  8B 91 BC 38 00 00               mov edx, dword ptr [rcx + 0x38bc]
00243FEC  8B B9 AC 83 00 00               mov edi, dword ptr [rcx + 0x83ac]
00243FF2  8B B1 5C 86 00 00               mov esi, dword ptr [rcx + 0x865c]
00243FF8  F6 C2 01                        test dl, 1
00243FFB  0F 85 46 01 00 00               jne 0x140244147
00244001  44 38 41 20                     cmp byte ptr [rcx + 0x20], r8b
00244005  0F 85 A9 04 00 00               jne 0x1402444b4
0024400B  F6 C2 1E                        test dl, 0x1e
0024400E  0F 85 62 04 00 00               jne 0x140244476
00244014  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0024401B  84 C0                           test al, al
0024401D  0F 85 B5 04 00 00               jne 0x1402444d8
00244023  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00244027  48 85 C0                        test rax, rax
0024402A  0F 85 73 04 00 00               jne 0x1402444a3
00244030  83 FF 07                        cmp edi, 7
00244033  0F 87 97 01 00 00               ja 0x1402441d0
00244039  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0024403D  4D 85 F6                        test r14, r14
00244040  0F 84 6D FD FF FF               je 0x140243db3
00244046  49 8B 06                        mov rax, qword ptr [r14]
00244049  48 B9 FE FF FF FF FF 0F 00 00   movabs rcx, 0xffffffffffe
00244053  48 85 C1                        test rcx, rax
00244056  0F 85 9E 01 00 00               jne 0x1402441fa
0024405C  E9 4E FD FF FF                  jmp 0x140243daf
00244061  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
00244068  F7 41 30 00 00 20 00            test dword ptr [rcx + 0x30], 0x200000
0024406F  0F 85 B1 FD FF FF               jne 0x140243e26
00244075  48 83 79 50 00                  cmp qword ptr [rcx + 0x50], 0
0024407A  0F 84 A6 FD FF FF               je 0x140243e26
00244080  49 8B D7                        mov rdx, r15
00244083  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00244087  48 C1 E2 19                     shl rdx, 0x19
0024408B  41 B8 08 00 00 00               mov r8d, 8
00244091  48 2B 55 80                     sub rdx, qword ptr [rbp - 0x80]
00244095  48 C1 FA 10                     sar rdx, 0x10
00244099  48 C1 EA 0C                     shr rdx, 0xc
0024409D  E8 CE A8 0E 00                  call 0x14032e970
002440A2  48 8B F8                        mov rdi, rax
002440A5  48 85 C0                        test rax, rax
002440A8  0F 85 1D 05 00 00               jne 0x1402445cb
002440AE  39 44 24 58                     cmp dword ptr [rsp + 0x58], eax
002440B2  0F 85 6E FD FF FF               jne 0x140243e26
002440B8  44 8B EE                        mov r13d, esi
002440BB  E9 31 01 00 00                  jmp 0x1402441f1
002440C0  FF C3                           inc ebx
002440C2  85 1D E4 11 D8 00               test dword ptr [rip + 0xd811e4], ebx
002440C8  0F 84 1B 07 00 00               je 0x1402447e9
002440CE  F3 90                           pause
002440D0  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002440D4  48 85 C0                        test rax, rax
002440D7  0F 89 61 FD FF FF               jns 0x140243e3e
002440DD  EB E1                           jmp 0x1402440c0
002440DF  48 F7 05 9E 29 D8 00 00 00 60 00  test qword ptr [rip + 0xd8299e], 0x600000
002440EA  0F 84 1D FD FF FF               je 0x140243e0d
002440F0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002440F9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00244100  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00244107  0F 84 00 FD FF FF               je 0x140243e0d
0024410D  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00244114  48 85 D2                        test rdx, rdx
00244117  0F 84 F0 FC FF FF               je 0x140243e0d
0024411D  49 8B C7                        mov rax, r15
00244120  48 C1 E8 03                     shr rax, 3
00244124  25 FF 01 00 00                  and eax, 0x1ff
00244129  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0024412D  A8 20                           test al, 0x20
0024412F  74 04                           je 0x140244135
00244131  48 83 CB 20                     or rbx, 0x20
00244135  48 8B CB                        mov rcx, rbx
00244138  48 83 CB 42                     or rbx, 0x42
0024413C  A8 42                           test al, 0x42
0024413E  48 0F 44 D9                     cmove rbx, rcx
00244142  E9 C6 FC FF FF                  jmp 0x140243e0d
00244147  41 BB 01 00 00 00               mov r11d, 1
0024414D  45 8B C3                        mov r8d, r11d
00244150  83 FE 07                        cmp esi, 7
00244153  0F 86 D7 FE FF FF               jbe 0x140244030
00244159  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00244160  84 C0                           test al, al
00244162  74 75                           je 0x1402441d9
00244164  41 8B DB                        mov ebx, r11d
00244167  E9 0F 03 00 00                  jmp 0x14024447b
0024416C  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00244170  48 B9 00 00 00 00 00 F0 FF FF   movabs rcx, 0xfffff00000000000
0024417A  48 0B C1                        or rax, rcx
0024417D  48 8B 14 C5 00 00 00 00         mov rdx, qword ptr [rax*8]
00244185  48 8D 1C C5 00 00 00 00         lea rbx, [rax*8]
0024418D  48 3B D3                        cmp rdx, rbx
00244190  0F 84 EA 06 00 00               je 0x140244880
00244196  48 8B 02                        mov rax, qword ptr [rdx]
00244199  48 39 5A 08                     cmp qword ptr [rdx + 8], rbx
0024419D  0F 85 37 0A 00 00               jne 0x140244bda
002441A3  48 39 50 08                     cmp qword ptr [rax + 8], rdx
002441A7  0F 85 2D 0A 00 00               jne 0x140244bda
002441AD  48 89 03                        mov qword ptr [rbx], rax
002441B0  48 89 58 08                     mov qword ptr [rax + 8], rbx
002441B4  48 8B 03                        mov rax, qword ptr [rbx]
002441B7  48 3B C3                        cmp rax, rbx
002441BA  0F 84 EA FC FF FF               je 0x140243eaa
002441C0  48 89 50 08                     mov qword ptr [rax + 8], rdx
002441C4  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002441C8  48 89 10                        mov qword ptr [rax], rdx
002441CB  E9 E0 FC FF FF                  jmp 0x140243eb0
002441D0  45 85 C0                        test r8d, r8d
002441D3  0F 84 06 03 00 00               je 0x1402444df
002441D9  F6 C2 1E                        test dl, 0x1e
002441DC  0F 84 37 03 00 00               je 0x140244519
002441E2  BB 05 00 00 00                  mov ebx, 5
002441E7  E9 8F 02 00 00                  jmp 0x14024447b
002441EC  44 8B 6C 24 44                  mov r13d, dword ptr [rsp + 0x44]
002441F1  4D 85 F6                        test r14, r14
002441F4  0F 84 EA 07 00 00               je 0x1402449e4
002441FA  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
00244201  49 8B CE                        mov rcx, r14
00244204  E8 87 1E 00 00                  call 0x140246090
00244209  33 FF                           xor edi, edi
0024420B  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00244210  44 8B E7                        mov r12d, edi
00244213  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00244218  48 85 C0                        test rax, rax
0024421B  74 43                           je 0x140244260
0024421D  48 8B C8                        mov rcx, rax
00244220  E8 9B DD 0C 00                  call 0x140311fc0
00244225  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0024422E  48 8B 90 38 88 00 00            mov rdx, qword ptr [rax + 0x8838]
00244235  48 85 D2                        test rdx, rdx
00244238  0F 84 A3 09 00 00               je 0x140244be1
0024423E  8B 82 5C 01 00 00               mov eax, dword ptr [rdx + 0x15c]
00244244  FF C8                           dec eax
00244246  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
0024424B  48 69 C8 78 50 00 00            imul rcx, rax, 0x5078
00244252  48 89 BC 11 F0 51 00 00         mov qword ptr [rcx + rdx + 0x51f0], rdi
0024425A  FF 8A 5C 01 00 00               dec dword ptr [rdx + 0x15c]
00244260  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00244265  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0024426A  48 85 DB                        test rbx, rbx
0024426D  74 10                           je 0x14024427f
0024426F  48 8B D3                        mov rdx, rbx
00244272  48 8B CE                        mov rcx, rsi
00244275  E8 46 2C FD FF                  call 0x140216ec0
0024427A  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0024427F  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00244284  48 8B CE                        mov rcx, rsi
00244287  E8 04 94 03 00                  call 0x14027d690
0024428C  45 85 ED                        test r13d, r13d
0024428F  79 1B                           jns 0x1402442ac
00244291  41 81 FD 34 04 00 C0            cmp r13d, 0xc0000434
00244298  0F 85 03 06 00 00               jne 0x1402448a1
0024429E  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
002442A4  A8 0F                           test al, 0xf
002442A6  0F 84 92 09 00 00               je 0x140244c3e
002442AC  48 8B CE                        mov rcx, rsi
002442AF  E8 3C 89 03 00                  call 0x14027cbf0
002442B4  44 8B 6C 24 48                  mov r13d, dword ptr [rsp + 0x48]
002442B9  48 8B 9D D8 00 00 00            mov rbx, qword ptr [rbp + 0xd8]
002442C0  48 BF 00 00 00 00 80 F6 FF FF   movabs rdi, 0xfffff68000000000
002442CA  E9 DF F9 FF FF                  jmp 0x140243cae
002442CF  3D 12 01 00 00                  cmp eax, 0x112
002442D4  0F 84 3F 04 00 00               je 0x140244719
002442DA  3D 21 00 00 C0                  cmp eax, 0xc0000021
002442DF  0F 85 B3 05 00 00               jne 0x140244898
002442E5  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
002442EA  49 8B DF                        mov rbx, r15
002442ED  48 C1 E3 19                     shl rbx, 0x19
002442F1  48 2B 5D 80                     sub rbx, qword ptr [rbp - 0x80]
002442F5  48 C1 FB 10                     sar rbx, 0x10
002442F9  4D 85 DB                        test r11, r11
002442FC  0F 85 86 06 00 00               jne 0x140244988
00244302  E8 89 E9 FF FF                  call 0x140242c90
00244307  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0024430C  4C 8B D8                        mov r11, rax
0024430F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00244314  45 33 C0                        xor r8d, r8d
00244317  44 89 40 10                     mov dword ptr [rax + 0x10], r8d
0024431B  C7 40 14 0A 00 00 00            mov dword ptr [rax + 0x14], 0xa
00244322  48 89 10                        mov qword ptr [rax], rdx
00244325  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0024432B  C1 E8 08                        shr eax, 8
0024432E  C0 E8 03                        shr al, 3
00244331  24 01                           and al, 1
00244333  41 88 43 18                     mov byte ptr [r11 + 0x18], al
00244337  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0024433D  A8 0F                           test al, 0xf
0024433F  75 20                           jne 0x140244361
00244341  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0024434A  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00244351  48 81 C1 00 04 00 00            add rcx, 0x400
00244358  48 3B D1                        cmp rdx, rcx
0024435B  0F 85 76 06 00 00               jne 0x1402449d7
00244361  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00244367  41 8B C8                        mov ecx, r8d
0024436A  A8 0F                           test al, 0xf
0024436C  B8 01 00 00 00                  mov eax, 1
00244371  0F 44 C8                        cmove ecx, eax
00244374  41 83 63 10 DB                  and dword ptr [r11 + 0x10], 0xffffffdb
00244379  41 89 4B 08                     mov dword ptr [r11 + 8], ecx
0024437D  66 45 89 43 19                  mov word ptr [r11 + 0x19], r8w
00244382  45 89 43 1C                     mov dword ptr [r11 + 0x1c], r8d
00244386  4D 89 43 20                     mov qword ptr [r11 + 0x20], r8
0024438A  4D 89 43 28                     mov qword ptr [r11 + 0x28], r8
0024438E  BF 01 00 00 00                  mov edi, 1
00244393  41 39 7B 08                     cmp dword ptr [r11 + 8], edi
00244397  0F 85 9E 04 00 00               jne 0x14024483b
0024439D  41 8B F0                        mov esi, r8d
002443A0  45 8B 53 1C                     mov r10d, dword ptr [r11 + 0x1c]
002443A4  45 85 D2                        test r10d, r10d
002443A7  0F 84 DF 02 00 00               je 0x14024468c
002443AD  41 8B 43 10                     mov eax, dword ptr [r11 + 0x10]
002443B1  A8 02                           test al, 2
002443B3  0F 85 85 02 00 00               jne 0x14024463e
002443B9  41 8D 42 FF                     lea eax, [r10 - 1]
002443BD  49 8B 4C C3 28                  mov rcx, qword ptr [r11 + rax*8 + 0x28]
002443C2  4D 8D 0C C3                     lea r9, [r11 + rax*8]
002443C6  48 F7 C1 00 0C 00 00            test rcx, 0xc00
002443CD  0F 85 B9 02 00 00               jne 0x14024468c
002443D3  4C 8B C1                        mov r8, rcx
002443D6  48 8B C1                        mov rax, rcx
002443D9  41 81 E0 FF 03 00 00            and r8d, 0x3ff
002443E0  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
002443E6  49 8D 50 01                     lea rdx, [r8 + 1]
002443EA  48 C1 E2 0C                     shl rdx, 0xc
002443EE  48 03 D0                        add rdx, rax
002443F1  48 3B D3                        cmp rdx, rbx
002443F4  75 15                           jne 0x14024440b
002443F6  4A 8D 04 07                     lea rax, [rdi + r8]
002443FA  49 3B C0                        cmp rax, r8
002443FD  76 0C                           jbe 0x14024440b
002443FF  48 3D FF 03 00 00               cmp rax, 0x3ff
00244405  0F 86 09 08 00 00               jbe 0x140244c14
0024440B  41 8D 4A FF                     lea ecx, [r10 - 1]
0024440F  48 8D 49 05                     lea rcx, [rcx + 5]
00244413  49 8B 04 CB                     mov rax, qword ptr [r11 + rcx*8]
00244417  4D 8D 0C CB                     lea r9, [r11 + rcx*8]
0024441B  48 8B C8                        mov rcx, rax
0024441E  E9 43 02 00 00                  jmp 0x140244666
00244423  4C 8B 95 E0 00 00 00            mov r10, qword ptr [rbp + 0xe0]
0024442A  41 F7 42 30 00 00 20 00         test dword ptr [r10 + 0x30], 0x200000
00244432  0F 84 E3 04 00 00               je 0x14024491b
00244438  41 BD 34 04 00 C0               mov r13d, 0xc0000434
0024443E  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
00244443  48 85 DB                        test rbx, rbx
00244446  0F 85 09 03 00 00               jne 0x140244755
0024444C  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00244451  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00244456  48 8B CE                        mov rcx, rsi
00244459  E8 32 92 03 00                  call 0x14027d690
0024445E  41 8B C5                        mov eax, r13d
00244461  48 81 C4 88 01 00 00            add rsp, 0x188
00244468  41 5F                           pop r15
0024446A  41 5E                           pop r14
0024446C  41 5D                           pop r13
0024446E  41 5C                           pop r12
00244470  5F                              pop rdi
00244471  5E                              pop rsi
00244472  5B                              pop rbx
00244473  5D                              pop rbp
00244474  C3                              ret
00244475  CC                              int3
00244476  BB 02 00 00 00                  mov ebx, 2
0024447B  F7 05 7F 26 D8 00 00 00 00 04   test dword ptr [rip + 0xd8267f], 0x4000000
00244485  74 0F                           je 0x140244496
00244487  44 8B C6                        mov r8d, esi
0024448A  8B D7                           mov edx, edi
0024448C  8B CB                           mov ecx, ebx
0024448E  E8 F5 4B 03 00                  call 0x140279088
00244493  45 33 D2                        xor r10d, r10d
00244496  85 DB                           test ebx, ebx
00244498  0F 85 53 FD FF FF               jne 0x1402441f1
0024449E  E9 96 FB FF FF                  jmp 0x140244039
002444A3  48 3B 41 08                     cmp rax, qword ptr [rcx + 8]
002444A7  0F 84 83 FB FF FF               je 0x140244030
002444AD  BB 04 00 00 00                  mov ebx, 4
002444B2  EB C7                           jmp 0x14024447b
002444B4  41 B9 01 00 00 00               mov r9d, 1
002444BA  83 FF 07                        cmp edi, 7
002444BD  0F 86 76 FB FF FF               jbe 0x140244039
002444C3  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
002444CA  84 C0                           test al, al
002444CC  0F 84 07 FD FF FF               je 0x1402441d9
002444D2  41 8D 59 06                     lea ebx, [r9 + 6]
002444D6  EB A3                           jmp 0x14024447b
002444D8  BB 03 00 00 00                  mov ebx, 3
002444DD  EB 9C                           jmp 0x14024447b
002444DF  45 85 C9                        test r9d, r9d
002444E2  0F 85 F1 FC FF FF               jne 0x1402441d9
002444E8  FA                              cli
002444E9  44 89 91 AC 83 00 00            mov dword ptr [rcx + 0x83ac], r10d
002444F0  44 89 91 5C 86 00 00            mov dword ptr [rcx + 0x865c], r10d
002444F7  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00244500  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00244507  4D 85 C0                        test r8, r8
0024450A  0F 85 00 03 00 00               jne 0x140244810
00244510  FB                              sti
00244511  41 8B DA                        mov ebx, r10d
00244514  E9 62 FF FF FF                  jmp 0x14024447b
00244519  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0024451D  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00244521  74 C5                           je 0x1402444e8
00244523  BB 06 00 00 00                  mov ebx, 6
00244528  E9 4E FF FF FF                  jmp 0x14024447b
0024452D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00244532  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00244538  24 0F                           and al, 0xf
0024453A  3C 05                           cmp al, 5
0024453C  0F 87 92 FA FF FF               ja 0x140243fd4
00244542  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00244548  24 0F                           and al, 0xf
0024454A  3C 01                           cmp al, 1
0024454C  0F 85 99 04 00 00               jne 0x1402449eb
00244552  48 8D 05 E7 42 BF 00            lea rax, [rip + 0xbf42e7]
00244559  48 8B 08                        mov rcx, qword ptr [rax]
0024455C  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00244565  48 8B 80 38 88 00 00            mov rax, qword ptr [rax + 0x8838]
0024456C  48 85 C0                        test rax, rax
0024456F  0F 84 7A 01 00 00               je 0x1402446ef
00244575  8B 80 44 01 00 00               mov eax, dword ptr [rax + 0x144]
0024457B  48 C1 E0 06                     shl rax, 6
0024457F  8B 04 01                        mov eax, dword ptr [rcx + rax]
00244582  0F BA E0 1E                     bt eax, 0x1e
00244586  0F 82 65 FC FF FF               jb 0x1402441f1
0024458C  E9 43 FA FF FF                  jmp 0x140243fd4
00244591  48 8B CB                        mov rcx, rbx
00244594  E8 87 B1 FE FF                  call 0x14022f720
00244599  84 C0                           test al, al
0024459B  0F 84 C9 04 00 00               je 0x140244a6a
002445A1  48 8B 05 D8 96 BE 00            mov rax, qword ptr [rip + 0xbe96d8]
002445A8  48 8B FB                        mov rdi, rbx
002445AB  48 85 C0                        test rax, rax
002445AE  74 0E                           je 0x1402445be
002445B0  F6 C3 10                        test bl, 0x10
002445B3  75 09                           jne 0x1402445be
002445B5  48 8B F8                        mov rdi, rax
002445B8  48 F7 D7                        not rdi
002445BB  48 23 FB                        and rdi, rbx
002445BE  48 C1 FF 10                     sar rdi, 0x10
002445C2  48 85 FF                        test rdi, rdi
002445C5  0F 84 5B F8 FF FF               je 0x140243e26
002445CB  49 8B C4                        mov rax, r12
002445CE  48 33 C7                        xor rax, rdi
002445D1  48 A9 00 F0 FF FF               test rax, -0x1000
002445D7  0F 84 46 F9 FF FF               je 0x140243f23
002445DD  4D 85 F6                        test r14, r14
002445E0  74 12                           je 0x1402445f4
002445E2  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
002445E9  49 8B CE                        mov rcx, r14
002445EC  E8 9F 1A 00 00                  call 0x140246090
002445F1  45 33 E4                        xor r12d, r12d
002445F4  48 8D 95 D0 00 00 00            lea rdx, [rbp + 0xd0]
002445FB  48 8B CF                        mov rcx, rdi
002445FE  E8 7D 45 07 00                  call 0x1402b8b80
00244603  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00244608  4C 8B F0                        mov r14, rax
0024460B  48 85 C0                        test rax, rax
0024460E  0F 84 E3 03 00 00               je 0x1402449f7
00244614  4C 8B E7                        mov r12, rdi
00244617  E9 07 F9 FF FF                  jmp 0x140243f23
0024461C  83 3D FD 26 D8 00 00            cmp dword ptr [rip + 0xd826fd], 0
00244623  74 09                           je 0x14024462e
00244625  44 0F 20 C1                     mov rcx, cr8
00244629  E8 6A 10 2B 00                  call 0x1404f5698
0024462E  0F B6 85 D0 00 00 00            movzx eax, byte ptr [rbp + 0xd0]
00244635  44 0F 22 C0                     mov cr8, rax
00244639  E9 DA F8 FF FF                  jmp 0x140243f18
0024463E  45 85 D2                        test r10d, r10d
00244641  74 49                           je 0x14024468c
00244643  41 8B 43 10                     mov eax, dword ptr [r11 + 0x10]
00244647  A8 02                           test al, 2
00244649  75 41                           jne 0x14024468c
0024464B  41 8D 4A FF                     lea ecx, [r10 - 1]
0024464F  48 8D 49 05                     lea rcx, [rcx + 5]
00244653  49 8B 04 CB                     mov rax, qword ptr [r11 + rcx*8]
00244657  4D 8D 0C CB                     lea r9, [r11 + rcx*8]
0024465B  48 8B C8                        mov rcx, rax
0024465E  48 A9 00 0C 00 00               test rax, 0xc00
00244664  75 26                           jne 0x14024468c
00244666  4C 8B DF                        mov r11, rdi
00244669  48 8B D1                        mov rdx, rcx
0024466C  49 C1 E3 0C                     shl r11, 0xc
00244670  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00244677  4E 8D 04 1B                     lea r8, [rbx + r11]
0024467B  49 3B D0                        cmp rdx, r8
0024467E  0F 84 0C 03 00 00               je 0x140244990
00244684  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00244689  45 33 C0                        xor r8d, r8d
0024468C  45 3B 53 0C                     cmp r10d, dword ptr [r11 + 0xc]
00244690  74 6C                           je 0x1402446fe
00244692  48 85 FF                        test rdi, rdi
00244695  74 7A                           je 0x140244711
00244697  48 8D 47 FF                     lea rax, [rdi - 1]
0024469B  48 8B CB                        mov rcx, rbx
0024469E  48 3D FF 03 00 00               cmp rax, 0x3ff
002446A4  BA 00 04 00 00                  mov edx, 0x400
002446A9  48 0F 46 D7                     cmovbe rdx, rdi
002446AD  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002446B4  48 8D 42 FF                     lea rax, [rdx - 1]
002446B8  25 FF 03 00 00                  and eax, 0x3ff
002446BD  48 0B C1                        or rax, rcx
002446C0  48 8B CA                        mov rcx, rdx
002446C3  4B 89 44 D3 28                  mov qword ptr [r11 + r10*8 + 0x28], rax
002446C8  45 8B 53 1C                     mov r10d, dword ptr [r11 + 0x1c]
002446CC  49 01 53 20                     add qword ptr [r11 + 0x20], rdx
002446D0  41 FF C2                        inc r10d
002446D3  48 C1 E1 0C                     shl rcx, 0xc
002446D7  48 03 D9                        add rbx, rcx
002446DA  45 89 53 1C                     mov dword ptr [r11 + 0x1c], r10d
002446DE  48 2B FA                        sub rdi, rdx
002446E1  74 AF                           je 0x140244692
002446E3  45 3B 53 0C                     cmp r10d, dword ptr [r11 + 0xc]
002446E7  0F 84 B0 FC FF FF               je 0x14024439d
002446ED  EB A3                           jmp 0x140244692
002446EF  E9 87 FE FF FF                  jmp 0x14024457b
002446F4  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
002446F9  E9 1A F8 FF FF                  jmp 0x140243f18
002446FE  85 F6                           test esi, esi
00244700  0F 84 D5 01 00 00               je 0x1402448db
00244706  41 80 7B 19 00                  cmp byte ptr [r11 + 0x19], 0
0024470B  0F 84 23 05 00 00               je 0x140244c34
00244711  41 8B F5                        mov esi, r13d
00244714  E9 50 F8 FF FF                  jmp 0x140243f69
00244719  45 33 C9                        xor r9d, r9d
0024471C  48 8D 45 98                     lea rax, [rbp - 0x68]
00244720  49 8B CF                        mov rcx, r15
00244723  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00244728  48 C1 E1 19                     shl rcx, 0x19
0024472C  49 8B D7                        mov rdx, r15
0024472F  48 2B 4D 80                     sub rcx, qword ptr [rbp - 0x80]
00244733  48 C1 F9 10                     sar rcx, 0x10
00244737  4D 8D 41 FF                     lea r8, [r9 - 1]
0024473B  E8 CC E2 11 00                  call 0x140362a0c
00244740  8B F0                           mov esi, eax
00244742  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00244746  49 83 EF 08                     sub r15, 8
0024474A  41 BD 01 00 00 00               mov r13d, 1
00244750  E9 14 F8 FF FF                  jmp 0x140243f69
00244755  4C 8B FB                        mov r15, rbx
00244758  E9 26 F6 FF FF                  jmp 0x140243d83
0024475D  4D 85 F6                        test r14, r14
00244760  74 1E                           je 0x140244780
00244762  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
00244769  49 8B CE                        mov rcx, r14
0024476C  E8 1F 19 00 00                  call 0x140246090
00244771  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00244775  45 33 F6                        xor r14d, r14d
00244778  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
0024477D  45 33 E4                        xor r12d, r12d
00244780  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00244784  41 B8 01 00 00 00               mov r8d, 1
0024478A  E8 41 F8 03 00                  call 0x140283fd0
0024478F  E9 E2 F7 FF FF                  jmp 0x140243f76
00244794  83 4D C0 04                     or dword ptr [rbp - 0x40], 4
00244798  48 8D 45 A8                     lea rax, [rbp - 0x58]
0024479C  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
002447A0  48 8D 4D C0                     lea rcx, [rbp - 0x40]
002447A4  8B 45 C4                        mov eax, dword ptr [rbp - 0x3c]
002447A7  25 7F FE FF FF                  and eax, 0xfffffe7f
002447AC  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
002447B0  83 C8 40                        or eax, 0x40
002447B3  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
002447B7  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
002447BA  48 8D 05 4F EF 0C 00            lea rax, [rip + 0xcef4f]
002447C1  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
002447C5  0F B6 44 24 40                  movzx eax, byte ptr [rsp + 0x40]
002447CA  88 45 C9                        mov byte ptr [rbp - 0x37], al
002447CD  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
002447D1  E8 3A DF 07 00                  call 0x1402c2710
002447D6  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
002447DA  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
002447E4  E9 89 F5 FF FF                  jmp 0x140243d72
002447E9  8B 05 C9 22 D8 00               mov eax, dword ptr [rip + 0xd822c9]
002447EF  A8 40                           test al, 0x40
002447F1  0F 84 D7 F8 FF FF               je 0x1402440ce
002447F7  E8 94 AC 0C 00                  call 0x14030f490
002447FC  84 C0                           test al, al
002447FE  0F 84 CA F8 FF FF               je 0x1402440ce
00244804  8B CB                           mov ecx, ebx
00244806  E8 55 AC 0C 00                  call 0x14030f460
0024480B  E9 C0 F8 FF FF                  jmp 0x1402440d0
00244810  41 0F 0D 08                     prefetchw byte ptr [r8]
00244814  41 8B 00                        mov eax, dword ptr [r8]
00244817  8B D0                           mov edx, eax
00244819  0F BA F2 15                     btr edx, 0x15
0024481D  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00244822  75 F3                           jne 0x140244817
00244824  0F BA E0 15                     bt eax, 0x15
00244828  0F 83 E2 FC FF FF               jae 0x140244510
0024482E  E8 9D E9 01 00                  call 0x1402631d0
00244833  45 33 D2                        xor r10d, r10d
00244836  E9 D5 FC FF FF                  jmp 0x140244510
0024483B  41 8B 4B 10                     mov ecx, dword ptr [r11 + 0x10]
0024483F  F6 C1 04                        test cl, 4
00244842  0F 85 55 FB FF FF               jne 0x14024439d
00244848  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00244852  48 8B C0                        mov rax, rax
00244855  48 3B D8                        cmp rbx, rax
00244858  0F 82 3F FB FF FF               jb 0x14024439d
0024485E  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00244868  48 8B C0                        mov rax, rax
0024486B  48 3B D8                        cmp rbx, rax
0024486E  0F 87 29 FB FF FF               ja 0x14024439d
00244874  83 C9 04                        or ecx, 4
00244877  41 89 4B 10                     mov dword ptr [r11 + 0x10], ecx
0024487B  E9 1D FB FF FF                  jmp 0x14024439d
00244880  49 8B 06                        mov rax, qword ptr [r14]
00244883  48 B9 01 00 00 00 00 F0 FF FF   movabs rcx, 0xfffff00000000001
0024488D  48 23 C1                        and rax, rcx
00244890  49 89 06                        mov qword ptr [r14], rax
00244893  E9 3F F6 FF FF                  jmp 0x140243ed7
00244898  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0024489C  E9 C8 F6 FF FF                  jmp 0x140243f69
002448A1  41 81 FD 17 00 00 C0            cmp r13d, 0xc0000017
002448A8  0F 85 FE F9 FF FF               jne 0x1402442ac
002448AE  E9 13 36 49 00                  jmp 0x1406d7ec6
002448B3  48 3B 05 C6 AA BE 00            cmp rax, qword ptr [rip + 0xbeaac6]
002448BA  72 0D                           jb 0x1402448c9
002448BC  48 3B 05 CD AA BE 00            cmp rax, qword ptr [rip + 0xbeaacd]
002448C3  0F 86 4F F4 FF FF               jbe 0x140243d18
002448C9  B9 02 00 00 00                  mov ecx, 2
002448CE  E8 FD 42 20 00                  call 0x140448bd0
002448D3  48 8B D8                        mov rbx, rax
002448D6  E9 54 F4 FF FF                  jmp 0x140243d2f
002448DB  41 80 7B 19 00                  cmp byte ptr [r11 + 0x19], 0
002448E0  0F 85 2B FE FF FF               jne 0x140244711
002448E6  49 8B D2                        mov rdx, r10
002448E9  49 8D 4B 28                     lea rcx, [r11 + 0x28]
002448ED  4C 8D 0D 9C 0F 45 00            lea r9, [rip + 0x450f9c]
002448F4  41 B8 08 00 00 00               mov r8d, 8
002448FA  E8 F1 C0 2B 00                  call 0x1405009f0
002448FF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00244904  E8 9F 4A 06 00                  call 0x1402a93a8
00244909  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
0024490E  45 33 C0                        xor r8d, r8d
00244911  BE 01 00 00 00                  mov esi, 1
00244916  E9 85 FA FF FF                  jmp 0x1402443a0
0024491B  49 83 7A 50 00                  cmp qword ptr [r10 + 0x50], 0
00244920  0F 84 12 FB FF FF               je 0x140244438
00244926  48 C1 EF 0C                     shr rdi, 0xc
0024492A  4C 8D 4D 88                     lea r9, [rbp - 0x78]
0024492E  48 8B D7                        mov rdx, rdi
00244931  41 B8 08 00 00 00               mov r8d, 8
00244937  49 8B CA                        mov rcx, r10
0024493A  E8 31 A0 0E 00                  call 0x14032e970
0024493F  48 85 C0                        test rax, rax
00244942  0F 84 F0 FA FF FF               je 0x140244438
00244948  45 33 D2                        xor r10d, r10d
0024494B  44 89 54 24 58                  mov dword ptr [rsp + 0x58], r10d
00244950  E9 31 F4 FF FF                  jmp 0x140243d86
00244955  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00244960  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00244967  0F 83 DE F4 FF FF               jae 0x140243e4b
0024496D  FF C3                           inc ebx
0024496F  85 1D 37 09 D8 00               test dword ptr [rip + 0xd80937], ebx
00244975  0F 84 72 02 00 00               je 0x140244bed
0024497B  F3 90                           pause
0024497D  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00244981  48 85 C0                        test rax, rax
00244984  79 DA                           jns 0x140244960
00244986  EB E5                           jmp 0x14024496d
00244988  45 33 C0                        xor r8d, r8d
0024498B  E9 FE F9 FF FF                  jmp 0x14024438e
00244990  81 E1 FF 03 00 00               and ecx, 0x3ff
00244996  48 8D 14 0F                     lea rdx, [rdi + rcx]
0024499A  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
002449A1  0F 87 DD FC FF FF               ja 0x140244684
002449A7  48 3B D1                        cmp rdx, rcx
002449AA  0F 86 D4 FC FF FF               jbe 0x140244684
002449B0  49 2B C3                        sub rax, r11
002449B3  41 8B F5                        mov esi, r13d
002449B6  48 8D 0C 38                     lea rcx, [rax + rdi]
002449BA  48 33 C1                        xor rax, rcx
002449BD  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
002449C3  48 33 C1                        xor rax, rcx
002449C6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002449CB  48 01 79 20                     add qword ptr [rcx + 0x20], rdi
002449CF  49 89 01                        mov qword ptr [r9], rax
002449D2  E9 92 F5 FF FF                  jmp 0x140243f69
002449D7  41 83 4B 10 09                  or dword ptr [r11 + 0x10], 9
002449DC  41 8B C8                        mov ecx, r8d
002449DF  E9 90 F9 FF FF                  jmp 0x140244374
002449E4  33 FF                           xor edi, edi
002449E6  E9 28 F8 FF FF                  jmp 0x140244213
002449EB  48 8D 81 C0 00 00 00            lea rax, [rcx + 0xc0]
002449F2  E9 62 FB FF FF                  jmp 0x140244559
002449F7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002449FC  48 85 C9                        test rcx, rcx
002449FF  74 11                           je 0x140244a12
00244A01  E8 BA D5 0C 00                  call 0x140311fc0
00244A06  E8 65 F2 0C 00                  call 0x140313c70
00244A0B  33 C9                           xor ecx, ecx
00244A0D  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00244A12  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00244A17  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00244A1C  48 85 DB                        test rbx, rbx
00244A1F  74 14                           je 0x140244a35
00244A21  48 8B D3                        mov rdx, rbx
00244A24  48 8B CE                        mov rcx, rsi
00244A27  E8 94 24 FD FF                  call 0x140216ec0
00244A2C  48 C7 44 24 78 00 00 00 00      mov qword ptr [rsp + 0x78], 0
00244A35  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00244A3A  48 8B CE                        mov rcx, rsi
00244A3D  E8 4E 8C 03 00                  call 0x14027d690
00244A42  45 33 C9                        xor r9d, r9d
00244A45  45 33 C0                        xor r8d, r8d
00244A48  48 8B D7                        mov rdx, rdi
00244A4B  41 8D 49 02                     lea ecx, [r9 + 2]
00244A4F  E8 2C A4 03 00                  call 0x14027ee80
00244A54  E9 53 F8 FF FF                  jmp 0x1402442ac
00244A59  44 8B 85 E8 00 00 00            mov r8d, dword ptr [rbp + 0xe8]
00244A60  41 83 F8 02                     cmp r8d, 2
00244A64  0F 84 27 FB FF FF               je 0x140244591
00244A6A  48 8B CB                        mov rcx, rbx
00244A6D  E8 AE AC FE FF                  call 0x14022f720
00244A72  84 C0                           test al, al
00244A74  74 7B                           je 0x140244af1
00244A76  41 83 F8 01                     cmp r8d, 1
00244A7A  0F 84 4D 01 00 00               je 0x140244bcd
00244A80  4D 85 F6                        test r14, r14
00244A83  74 1A                           je 0x140244a9f
00244A85  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
00244A8C  49 8B CE                        mov rcx, r14
00244A8F  E8 FC 15 00 00                  call 0x140246090
00244A94  45 33 F6                        xor r14d, r14d
00244A97  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00244A9C  45 33 E4                        xor r12d, r12d
00244A9F  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00244AA4  48 85 DB                        test rbx, rbx
00244AA7  74 16                           je 0x140244abf
00244AA9  48 8B CB                        mov rcx, rbx
00244AAC  E8 0F D5 0C 00                  call 0x140311fc0
00244AB1  E8 BA F1 0C 00                  call 0x140313c70
00244AB6  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
00244ABF  44 0F B6 44 24 40               movzx r8d, byte ptr [rsp + 0x40]
00244AC5  BA 18 00 00 00                  mov edx, 0x18
00244ACA  49 8B CF                        mov rcx, r15
00244ACD  E8 3E 1C 06 00                  call 0x1402a6710
00244AD2  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00244AD6  85 C0                           test eax, eax
00244AD8  0F 88 EF 00 00 00               js 0x140244bcd
00244ADE  49 83 EF 08                     sub r15, 8
00244AE2  49 8D 4F 08                     lea rcx, [r15 + 8]
00244AE6  44 8B EE                        mov r13d, esi
00244AE9  4C 8B F9                        mov r15, rcx
00244AEC  E9 C0 F4 FF FF                  jmp 0x140243fb1
00244AF1  49 8B D7                        mov rdx, r15
00244AF4  48 C1 E2 19                     shl rdx, 0x19
00244AF8  48 2B 55 80                     sub rdx, qword ptr [rbp - 0x80]
00244AFC  48 C1 FA 10                     sar rdx, 0x10
00244B00  48 8B C2                        mov rax, rdx
00244B03  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00244B09  48 3D 00 00 FE 7F               cmp rax, 0x7ffe0000
00244B0F  74 11                           je 0x140244b22
00244B11  48 8B 0D 60 90 BE 00            mov rcx, qword ptr [rip + 0xbe9060]
00244B18  48 3B C1                        cmp rax, rcx
00244B1B  75 17                           jne 0x140244b34
00244B1D  48 85 C9                        test rcx, rcx
00244B20  74 12                           je 0x140244b34
00244B22  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00244B26  8B 80 FC 05 00 00               mov eax, dword ptr [rax + 0x5fc]
00244B2C  A8 01                           test al, 1
00244B2E  0F 84 99 00 00 00               je 0x140244bcd
00244B34  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
00244B3B  F7 41 30 00 00 20 00            test dword ptr [rcx + 0x30], 0x200000
00244B42  75 5E                           jne 0x140244ba2
00244B44  48 83 79 50 00                  cmp qword ptr [rcx + 0x50], 0
00244B49  74 57                           je 0x140244ba2
00244B4B  48 C1 EA 0C                     shr rdx, 0xc
00244B4F  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00244B53  41 B8 08 00 00 00               mov r8d, 8
00244B59  E8 12 9E 0E 00                  call 0x14032e970
00244B5E  48 8B CB                        mov rcx, rbx
00244B61  48 8B F8                        mov rdi, rax
00244B64  E8 07 40 0E 00                  call 0x140328b70
00244B69  85 C0                           test eax, eax
00244B6B  0F 85 51 FA FF FF               jne 0x1402445c2
00244B71  48 8B 15 08 91 BE 00            mov rdx, qword ptr [rip + 0xbe9108]
00244B78  48 8B CB                        mov rcx, rbx
00244B7B  48 85 D2                        test rdx, rdx
00244B7E  74 0E                           je 0x140244b8e
00244B80  F6 C3 10                        test bl, 0x10
00244B83  75 09                           jne 0x140244b8e
00244B85  48 8B CA                        mov rcx, rdx
00244B88  48 F7 D1                        not rcx
00244B8B  48 23 CB                        and rcx, rbx
00244B8E  48 C1 F9 10                     sar rcx, 0x10
00244B92  48 3B F9                        cmp rdi, rcx
00244B95  0F 84 27 FA FF FF               je 0x1402445c2
00244B9B  44 8B 85 E8 00 00 00            mov r8d, dword ptr [rbp + 0xe8]
00244BA2  48 8B 05 D7 90 BE 00            mov rax, qword ptr [rip + 0xbe90d7]
00244BA9  48 8B FB                        mov rdi, rbx
00244BAC  48 85 C0                        test rax, rax
00244BAF  74 0E                           je 0x140244bbf
00244BB1  F6 C3 10                        test bl, 0x10
00244BB4  75 09                           jne 0x140244bbf
00244BB6  48 8B F8                        mov rdi, rax
00244BB9  48 F7 D7                        not rdi
00244BBC  48 23 FB                        and rdi, rbx
00244BBF  48 C1 FF 10                     sar rdi, 0x10
00244BC3  41 83 F8 02                     cmp r8d, 2
00244BC7  0F 84 F5 F9 FF FF               je 0x1402445c2
00244BCD  C7 44 24 48 34 04 00 C0         mov dword ptr [rsp + 0x48], 0xc0000434
00244BD5  E9 08 FF FF FF                  jmp 0x140244ae2
00244BDA  B9 03 00 00 00                  mov ecx, 3
00244BDF  CD 29                           int 0x29
00244BE1  48 8D 15 D8 A8 DC 00            lea rdx, [rip + 0xdca8d8]
00244BE8  E9 51 F6 FF FF                  jmp 0x14024423e
00244BED  8B 05 C5 1E D8 00               mov eax, dword ptr [rip + 0xd81ec5]
00244BF3  A8 40                           test al, 0x40
00244BF5  0F 84 80 FD FF FF               je 0x14024497b
00244BFB  E8 90 A8 0C 00                  call 0x14030f490
00244C00  84 C0                           test al, al
00244C02  0F 84 73 FD FF FF               je 0x14024497b
00244C08  8B CB                           mov ecx, ebx
00244C0A  E8 51 A8 0C 00                  call 0x14030f460
00244C0F  E9 69 FD FF FF                  jmp 0x14024497d
00244C14  48 8D 14 39                     lea rdx, [rcx + rdi]
00244C18  48 8B C2                        mov rax, rdx
00244C1B  48 33 C1                        xor rax, rcx
00244C1E  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00244C24  48 33 C2                        xor rax, rdx
00244C27  49 01 7B 20                     add qword ptr [r11 + 0x20], rdi
00244C2B  49 89 41 28                     mov qword ptr [r9 + 0x28], rax
00244C2F  E9 DD FA FF FF                  jmp 0x140244711
00244C34  41 C6 43 19 01                  mov byte ptr [r11 + 0x19], 1
00244C39  E9 D3 FA FF FF                  jmp 0x140244711
00244C3E  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00244C47  48 8B BB B8 00 00 00            mov rdi, qword ptr [rbx + 0xb8]
00244C4E  48 8B 87 70 02 00 00            mov rax, qword ptr [rdi + 0x270]
00244C55  48 85 C0                        test rax, rax
00244C58  0F 84 4E F6 FF FF               je 0x1402442ac
00244C5E  48 3B C3                        cmp rax, rbx
00244C61  0F 84 45 F6 FF FF               je 0x1402442ac
00244C67  48 8B D7                        mov rdx, rdi
00244C6A  48 8B CB                        mov rcx, rbx
00244C6D  E8 D2 FC 05 00                  call 0x1402a4944
00244C72  48 8B D7                        mov rdx, rdi
00244C75  48 8B CB                        mov rcx, rbx
00244C78  E8 C7 FB 05 00                  call 0x1402a4844
00244C7D  E9 2A F6 FF FF                  jmp 0x1402442ac
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWalkVaRange(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m156;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned int v_stack_m184;
    unsigned __int8 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mFF;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (392);
    v_stack_p8 = 17;
    a1 = 0;
    v_r15 = (a1) >> (9);
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_r15 = (v_r15) & (a2);
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    v_stack_m180 = 0;
    v_stack_m168 = 0;
    v_stack_m178 = 0;
    v_rbx = (a2) >> (9);
    v_r15 = (v_r15) + (v_rdi);
    v_rbx = (v_rbx) & (a2);
    v_rbx = (v_rbx) + (v_rdi);
    v_stack_m150 = 0;
    v_stack_p10 = v_rbx;
    v_stack_m110 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m160 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, a3, a4);
    v_stack_m188 = (unsigned __int8)(result);
loc_00243CAE:
    if (v_r15 > v_rbx) goto loc_00244451;
    a2 = 0;
    v_stack_m120 = v_xmm0;
    result = memset(v_stack_m104, a2, 188, a4);
    result = (v_rdi) << (25);
    v_rdi = (v_r15) << (25);
    v_rdi = (v_rdi) - (result);
    v_rsi = (v_rbx) << (25);
    v_rsi = (v_rsi) - (result);
    v_rdi = (v_rdi) >> (16);
    v_stack_m148 = result;
    v_rsi = (v_rsi) >> (16);
    v_stack_m108 = 0x2061ULL;
    result = MiGetLeafVa(v_rdi, a2, 188, a4);
    if (result >= v_rdi) goto loc_002448B3;
loc_00243D18:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
loc_00243D2F:
    a3 = 0;
    result = MiFastLockLeafPageTable(v_rbx, v_rdi, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00244794;
    result = (unsigned int)((result) - 1);
    v_stack_m120 = (unsigned int)(result);
    v_rbx = (v_rdi) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (v_rsi);
    v_stack_m118 = v_rbx;
loc_00243D72:
    v_stack_m170 = 1;
    if (v_rbx != v_r15) goto loc_00244423;
loc_00243D83:
    v_r10 = 0;
loc_00243D86:
    result = v_rsi;
    if (v_rbx != 0) {
        a1 = v_rbx;
        a1 = (a1) >> (9);
        a1 = (a1) & (v_r14);
        result = v_rsi;
        a1 = (a1) + (result);
        v_stack_m150 = a1;
    }
loc_00243DAF:
loc_00243DB3:
    v_stack_m130 = 0;
    v_stack_m184 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m170)) == 0) goto loc_00244061;
    if (v_r15 < result) goto loc_00243E0D;
    if (v_r15 > result) goto loc_00243E0D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_00243E0D;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002440DF;
loc_00243E0D:
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_00244061;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_00243E26;
    if (condition_is_below) goto loc_00244A59;
loc_00243E26:
    if (v_stack_m168 == 0) goto loc_00243F23;
    v_rbx = 0;
    if (v_stack_p8 == 18) goto loc_00244960;
loc_00243E3E:
    if (v_stack_p8 < 18) goto loc_002440C0;
loc_00243E4B:
    if (sign_flag) goto loc_00243E71;
    if (condition_is_below) goto loc_00243E71;
    result = (*(unsigned __int64 *)(v_stack_m168 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 1) {
        result = *(unsigned __int64 *)(v_stack_m168 + 8);
    }
    if (((a1) & (*(unsigned __int64 *)(v_stack_m168))) != 0) goto loc_0024416C;
    v_stack_m158 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m168 + 32))) >> (16));
    result = (unsigned __int8)((result) & (223));
    v_stack_m156 = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m168 + 32) = (unsigned int)((unsigned int)(v_stack_m158));
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_m168, v_rdi, a3, a4);
    goto loc_00243EEC;
loc_00243EAA:
    *(unsigned __int64 *)(v_rdi) = v_rdi;
loc_00243EB0:
    *(unsigned __int64 *)(v_rdi + 8) = v_rdi;
    a2 = (v_rdi) >> (4);
    a2 = (a2) + (a2);
    a1 = (a2) ^ (*(unsigned __int64 *)(v_stack_m168));
    a1 = (a1) & (*(unsigned __int64 *)(v_stack_m168));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(v_stack_m168) = a1;
loc_00243ED7:
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_m168, a2, a3, a4);
    if (0 != 0) {
        result = 1;
        *(unsigned int *)(v_rbx + 16) = (unsigned int)(result);
    }
    if (v_stack_p8 == 18) goto loc_002446F4;
    if (((unsigned __int8)(v_stack_p8)) <= 1) goto loc_0024461C;
loc_00243F18:
    v_r14 = 0;
    v_stack_m168 = 0;
    v_r12 = 0;
loc_00243F23:
    v_stack_m190 = v_stack_m138;
    v_stack_m198 = v_stack_m128;
    v_stack_m1A0 = a5;
    v_stack_m1A8 = (unsigned int)((unsigned int)(v_stack_p20));
    result = MiActOnPte(v_stack_p18, (unsigned int)(v_stack_m170), v_r15, 0);
    if ((unsigned int)(result) != 0) goto loc_002442CF;
loc_00243F69:
    if (v_stack_m138 != 0) goto loc_0024475D;
loc_00243F76:
    v_r15 = (v_r15) + (8);
    if (0 != 0) goto loc_002441EC;
    v_stack_m178 = v_stack_m178;
    v_stack_m180 = (unsigned int)((unsigned int)(v_stack_m180));
    v_stack_m168 = 0;
    v_stack_m158 = v_r15;
    if (sign_flag) goto loc_002441F1;
loc_00243FB1:
    if (v_r15 > v_stack_p10) goto loc_002441F1;
    if (((v_r15) & (0xFFFULL)) == 0) goto loc_002441F1;
    if ((((unsigned __int8)(v_r15)) & (120)) == 0) goto loc_0024452D;
loc_00243FD4:
    v_r10 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (1)) != 0) goto loc_00244147;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_002444B4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) != 0) goto loc_00244476;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521)) != 0) goto loc_002444D8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) != 0) goto loc_002444A3;
loc_00244030:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) > 7) goto loc_002441D0;
loc_00244039:
    if (0 == 0) goto loc_00243DB3;
    if ((((unsigned int)(v_stack_m170)) & (*(unsigned __int64 *)(v_r14))) != 0) goto loc_002441FA;
    goto loc_00243DAF;
loc_00244061:
    if (((*(unsigned int *)(v_stack_p18 + 48)) & (0x200000ULL)) != 0) goto loc_00243E26;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) == 0) goto loc_00243E26;
    a2 = (v_r15) << (25);
    a2 = (a2) - (v_stack_m148);
    a2 = (a2) >> (16);
    a2 = (a2) >> (12);
    result = MiGetProtoPteAddress(v_stack_p18, a2, 8, v_stack_m140);
    if (result != 0) goto loc_002445CB;
    if (v_stack_m170 != ((unsigned int)(result))) goto loc_00243E26;
    goto loc_002441F1;
loc_002440C0:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14160356)) & ((unsigned int)(v_rbx))) == 0) goto loc_002447E9;
loc_002440CE:
loc_002440D0:
    if (!sign_flag) goto loc_00243E3E;
    goto loc_002440C0;
loc_002440DF:
    if (((*(unsigned __int64 *)(v_rip + 14166430)) & (0x600000ULL)) == 0) goto loc_00243E0D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00243E0D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00243E0D;
    result = (v_r15) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (v_rbx) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_00243E0D;
loc_00244147:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)))) <= 7) goto loc_00244030;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 14521)) == 0) goto loc_002441D9;
    goto loc_0024447B;
loc_0024416C:
    result = (*(unsigned __int8 *)(v_rbx + 14521)) & (-2);
    result = (result) | (v_rbx);
    if ((*(unsigned __int64 *)(result * 8)) == (result * 8)) goto loc_00244880;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result * 8) + 8)) != (result * 8)) goto loc_00244BDA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result * 8)) + 8)) != (*(unsigned __int64 *)(result * 8))) goto loc_00244BDA;
    *(unsigned __int64 *)(result * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(result * 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result * 8)) + 8) = result * 8;
    if ((*(unsigned __int64 *)(result * 8)) == (result * 8)) goto loc_00243EAA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result * 8) + 8) = *(unsigned __int64 *)(result * 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result * 8 + 8)) = *(unsigned __int64 *)(result * 8);
    goto loc_00243EB0;
loc_002441D0:
    if (1 == 0) goto loc_002444DF;
loc_002441D9:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result * 8))) & (30)) == 0) goto loc_00244519;
    goto loc_0024447B;
loc_002441EC:
loc_002441F1:
    if (0 == 0) goto loc_002449E4;
loc_002441FA:
    result = MiUnlockProtoPoolPage(0, v_stack_p8, 1, v_stack_m140);
    v_rdi = 0;
    v_stack_m168 = 0;
loc_00244213:
    if (v_stack_m178 == 0) goto loc_00244260;
    result = MiFlushTbList(v_stack_m178, v_stack_p8, 1, v_stack_m140);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_00244BE1;
loc_0024423E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 348))) - 1);
    v_stack_m178 = 0;
    a1 = (v_stack_m178) * (result);
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) * 1 + 20976) = 0;
loc_00244260:
    if (v_stack_m150 != 0) {
        a2 = v_stack_m150;
        a1 = v_stack_m160;
        result = MiUnlockPageTable(a1, a2, 1, v_stack_m140);
        v_stack_m150 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_m160, v_stack_m188, 1, v_stack_m140);
    if (!sign_flag) goto loc_002442AC;
    if (((unsigned int)((unsigned int)(v_stack_m184))) != 0xC0000434ULL) goto loc_002448A1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m160 + 184)))) & (15)) == 0) goto loc_00244C3E;
loc_002442AC:
    result = MiLockWorkingSetShared(v_stack_m160, v_stack_m188, 1, v_stack_m140);
    goto loc_00243CAE;
loc_002442CF:
    if (((unsigned int)(result)) == 274) goto loc_00244719;
    if (((unsigned int)(result)) != 0xC0000021ULL) goto loc_00244898;
    v_rbx = (v_r15) << (25);
    v_rbx = (v_rbx) - (v_stack_m148);
    v_rbx = (v_rbx) >> (16);
    if (v_stack_m178 != 0) goto loc_00244988;
    result = MiGetProcessorFlushList(v_stack_m160, v_stack_m188, 1, v_stack_m140);
    v_stack_m178 = result;
    a3 = 0;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned int *)(result + 20) = 10;
    *(unsigned __int64 *)(result) = v_stack_m160;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m160 + 184))) >> (8));
    result = (unsigned __int8)((result) >> (3));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m160 + 184)))) & (15)) != 0) goto loc_00244361;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_stack_m160 != a1) goto loc_002449D7;
loc_00244361:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m160 + 184)))) & (15)) == 0) { a1 = 1; }
loc_00244374:
    *(unsigned int *)(result + 8) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 25) = 0;
    *(unsigned int *)(result + 28) = 0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
loc_0024438E:
    if ((*(unsigned int *)(result + 8)) != 1) goto loc_0024483B;
loc_0024439D:
loc_002443A0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 28))) == 0) goto loc_0024468C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (2)) != 0) goto loc_0024463E;
    if (((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0xC00ULL)) != 0) goto loc_0024468C;
    a3 = (unsigned int)((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0x3FFULL));
    result = (*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (result);
    if (a2 != v_rbx) goto loc_0024440B;
    if ((1 + a3 * 1) <= a3) goto loc_0024440B;
    if ((1 + a3 * 1) <= 0x3FFULL) goto loc_00244C14;
loc_0024440B:
    goto loc_00244666;
loc_00244423:
    if (((*(unsigned int *)(v_stack_p18 + 48)) & (0x200000ULL)) == 0) goto loc_0024491B;
loc_00244438:
    v_stack_m180 = (unsigned int)((unsigned int)(0xC0000434ULL));
    if (v_rbx != 0) goto loc_00244755;
loc_00244451:
    result = MiUnlockWorkingSetShared(v_stack_m160, v_stack_m188, a3, result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 + 5 * 8);
    v_rsp = (v_rsp) + (392);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000434ULL)));
loc_00244476:
loc_0024447B:
    result = (unsigned int)((unsigned int)((unsigned int)(0xC0000434ULL)));
    v_r10 = v_stack_p18;
    if (((*(unsigned int *)(v_rip + 14165631)) & (0x4000000ULL)) != 0) {
        a3 = (unsigned int)(v_stack_m160);
        a2 = 1;
        a1 = 2;
        result = EtwTraceShouldYieldProcessor(a1, a2, a3, result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 + 5 * 8);
        v_r10 = 0;
    }
    if (2 != 0) goto loc_002441F1;
    goto loc_00244039;
loc_002444A3:
    if (result == (*(unsigned __int64 *)(a1 + 8))) goto loc_00244030;
    goto loc_0024447B;
loc_002444B4:
    if (1 <= 7) goto loc_00244039;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 14521)) == 0) goto loc_002441D9;
    goto loc_0024447B;
loc_002444D8:
    goto loc_0024447B;
loc_002444DF:
    if (1 != 0) goto loc_002441D9;
loc_002444E8:
    *(unsigned int *)(a1 + 33708) = 0;
    *(unsigned int *)(a1 + 34396) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00244810;
loc_00244510:
    goto loc_0024447B;
loc_00244519:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_002444E8;
    goto loc_0024447B;
loc_0024452D:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p68 + 184))) & (15));
    if (((unsigned __int8)(result)) > 5) goto loc_00243FD4;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p68 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_002449EB;
loc_00244559:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_002446EF;
loc_0024457B:
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324))) << (6);
    if (condition_is_below) goto loc_002441F1;
    goto loc_00243FD4;
loc_00244591:
    result = MI_PROTO_FORMAT_COMBINED(6, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), 1);
    if ((unsigned __int8)(result) == 0) goto loc_00244A6A;
    if (*(unsigned __int64 *)(v_rip + 12490456) == 0) goto loc_002445BE;
    v_rdi = 6;
    if (((6) & (16)) == 0) {
        v_rdi = *(unsigned __int64 *)(v_rip + 12490456);
        v_rdi = ~(v_rdi);
        v_rdi = (v_rdi) & (6);
    }
    v_rdi = (v_rdi) >> (16);
loc_002445C2:
    if (v_rdi == 0) goto loc_00243E26;
loc_002445CB:
    result = (0) ^ (v_rdi);
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) == 0) goto loc_00243F23;
    v_r12 = 0;
    if (0 != 0) {
        a2 = v_stack_p8;
        a1 = 0;
        result = MiUnlockProtoPoolPage(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), 1);
        v_r12 = 0;
    }
    result = MiLockProtoPoolPage(v_rdi, v_stack_p8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), 1);
    v_stack_p60 = result;
    if (result == 0) goto loc_002449F7;
    goto loc_00243F23;
loc_0024461C:
    if ((*(unsigned int *)(v_rip + 14165757)) != 0) {
        a1 = v_cr8;
        result = KiLowerIrqlProcessIrqlFlags(a1, v_stack_p8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), 1);
    }
    goto loc_00243F18;
loc_0024463E:
    if (0 == 0) goto loc_0024468C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (2)) != 0) goto loc_0024468C;
    if (((*(unsigned __int64 *)(result + v_r10 - 1 + 5 * 8)) & (0xC00ULL)) != 0) goto loc_0024468C;
loc_00244666:
    v_r11 = (v_rdi) << (12);
    a2 = (*(unsigned __int64 *)(result + v_r10 - 1 + 5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (6 + v_r11 * 1)) goto loc_00244990;
loc_00244684:
    a3 = 0;
loc_0024468C:
    if (0 == (*(unsigned int *)(v_stack_p50 + 12))) goto loc_002446FE;
loc_00244692:
    if (v_rdi == 0) goto loc_00244711;
    a2 = (unsigned int)(0x400ULL);
    if ((v_rdi - 1) <= 0x3FFULL) { a2 = v_rdi; }
    a1 = (6) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(unsigned __int64 *)(v_stack_p50 + v_r10 * 8 + 40) = result;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 28))) + 1);
    a1 = (a2) << (12);
    v_rbx = (6) + (a1);
    *(unsigned int *)(v_stack_p50 + 28) = (unsigned int)(v_r10);
    v_rdi = (v_rdi) - (a2);
    if (condition_is_equal) goto loc_00244692;
    if (((unsigned int)(v_r10)) == (*(unsigned int *)(v_stack_p50 + 12))) goto loc_0024439D;
    goto loc_00244692;
loc_002446EF:
    goto loc_0024457B;
loc_002446F4:
    goto loc_00243F18;
loc_002446FE:
    if ((unsigned int)(v_stack_m160) == 0) goto loc_002448DB;
    if ((*(unsigned __int8 *)(v_stack_p50 + 25)) == 0) goto loc_00244C34;
loc_00244711:
    goto loc_00243F69;
loc_00244719:
    a4 = 0;
    v_stack_p20 = v_stack_m130;
    a1 = (v_r15) << (25);
    a1 = (a1) - (v_stack_m148);
    a1 = (a1) >> (16);
    result = MiCopyOnWrite(a1, v_r15, a4 - 1, a4);
    v_stack_p44 = (unsigned int)(result);
    v_r15 = (v_r15) - (8);
    goto loc_00243F69;
loc_00244755:
    goto loc_00243D83;
loc_0024475D:
    v_r12 = v_rdi;
    v_r14 = result;
    if (result != 0) {
        a2 = v_stack_p8;
        a1 = result;
        result = MiUnlockProtoPoolPage(a1, a2, a4 - 1, a4);
        a2 = v_stack_m138;
        v_r14 = 0;
        v_stack_p60 = 0;
        v_r12 = 0;
    }
    result = MiReleasePageFileInfo(v_stack_m128, a2, 1, a4);
    goto loc_00243F76;
loc_00244794:
    v_stack_m50 = v_stack_m120;
    result = (unsigned int)(((unsigned int)(v_stack_m104)) & (0xFFFFFE7FULL));
    v_stack_mE8 = v_rbx;
    result = (unsigned int)((result) | (64));
    v_stack_mE0 = v_rdi;
    v_stack_m104 = (unsigned int)(result);
    v_stack_m58 = v_rip + 847695;
    v_stack_mFF = (unsigned __int8)(v_stack_p40);
    v_stack_mD8 = (unsigned int)((unsigned int)(result));
    result = MiWalkPageTables(v_stack_m108, a2, 1, a4);
    goto loc_00243D72;
loc_002447E9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14164681)))) & (64)) == 0) goto loc_002440CE;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m108, a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002440CE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m118)), a2, 1, a4);
    goto loc_002440D0;
loc_00244810:
loc_00244817:
    if ((unsigned __int8)(result) != 0) goto loc_00244817;
    if (condition_is_above_or_equal) goto loc_00244510;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(v_stack_m118)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1)))), 1, a4);
    v_r10 = 0;
    goto loc_00244510;
loc_0024483B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p50 + 16)))) & (4)) != 0) goto loc_0024439D;
    if (v_stack_m118 < result) goto loc_0024439D;
    if (v_stack_m118 > result) goto loc_0024439D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 16))) | (4));
    *(unsigned int *)(v_stack_p50 + 16) = (unsigned int)(a1);
    goto loc_0024439D;
loc_00244880:
    result = (*(unsigned __int64 *)(v_r14)) & (a1);
    *(unsigned __int64 *)(v_r14) = result;
    goto loc_00243ED7;
loc_00244898:
    v_stack_p48 = (unsigned int)(result);
    goto loc_00243F69;
loc_002448A1:
    if (1 != 0xC0000017ULL) goto loc_002442AC;
loc_002448B3:
    if (result < (*(unsigned __int64 *)(v_rip + 12495558))) goto loc_002448C9;
    if (result <= (*(unsigned __int64 *)(v_rip + 12495565))) goto loc_00243D18;
loc_002448C9:
    result = MiGetAnyMultiplexedVm(2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1)))), 1, a4);
    goto loc_00243D2F;
loc_002448DB:
    if ((*(unsigned __int8 *)(v_stack_p50 + 25)) != 0) goto loc_00244711;
    result = qsort(v_stack_p50 + 40, 0, 8, v_rip + 4525980);
    result = MiCompressTbFlushList(v_stack_p50, 0, 8, v_rip + 4525980);
    a3 = 0;
    goto loc_002443A0;
loc_0024491B:
    if ((*(unsigned __int64 *)(v_r10 + 80)) == 0) goto loc_00244438;
    v_rdi = (v_rdi) >> (12);
    result = MiGetProtoPteAddress(0, v_rdi, 8, v_stack_m140);
    if (result == 0) goto loc_00244438;
    v_r10 = 0;
    v_stack_p58 = 0;
    goto loc_00243D86;
loc_00244960:
    if (condition_is_above_or_equal) goto loc_00243E4B;
loc_0024496D:
    v_rbx = (unsigned int)((result) + 1);
    if (((*(unsigned int *)(v_rip + 14158135)) & ((unsigned int)(v_rbx))) == 0) goto loc_00244BED;
loc_0024497B:
loc_0024497D:
    if (!sign_flag) goto loc_00244960;
    goto loc_0024496D;
loc_00244988:
    a3 = 0;
    goto loc_0024438E;
loc_00244990:
    a1 = (unsigned int)((0) & (0x3FFULL));
    if ((v_rdi + a1 * 1) > 0x3FFULL) goto loc_00244684;
    if ((v_rdi + a1 * 1) <= a1) goto loc_00244684;
    result = (*(unsigned __int64 *)(v_r14 + 24)) - (v_stack_p50);
    result = (result) ^ (result + v_rdi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + v_rdi * 1);
    *(unsigned __int64 *)(v_stack_m140) = result;
    goto loc_00243F69;
loc_002449D7:
    goto loc_00244374;
loc_002449E4:
    v_rdi = 0;
    goto loc_00244213;
loc_002449EB:
    goto loc_00244559;
loc_002449F7:
    result = 0 + 192;
    if (v_stack_p50 != 0) {
        result = MiFlushTbList(v_stack_p50, v_rdi + a1 * 1, a3, v_stack_m140);
        result = MiReleaseProcessorFlushList(v_stack_p50, v_rdi + a1 * 1, a3, v_stack_m140);
        a1 = 0;
        v_stack_p50 = 0;
    }
    if (v_stack_p78 != 0) {
        a2 = v_stack_p78;
        a1 = v_stack_p68;
        result = MiUnlockPageTable(a1, a2, a3, v_stack_m140);
        v_stack_p78 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p68, v_stack_p40, a3, v_stack_m140);
    a4 = 0;
    a3 = 0;
    result = MmAccessFault(a4 + 2, 0, a3, a4);
    goto loc_002442AC;
loc_00244A59:
    if (((unsigned int)((unsigned int)(v_stack_p20))) == 2) goto loc_00244591;
loc_00244A6A:
    result = MI_PROTO_FORMAT_COMBINED(v_stack_p78, 0, (unsigned int)(v_stack_p20), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00244AF1;
    if (((unsigned int)((unsigned int)(v_stack_p20))) == 1) goto loc_00244BCD;
    if (0 != 0) {
        a2 = v_stack_p8;
        a1 = 0;
        result = MiUnlockProtoPoolPage(a1, a2, (unsigned int)(v_stack_p20), a4);
        v_r14 = 0;
        v_stack_p60 = 0;
        v_r12 = 0;
    }
    if (v_stack_p50 != 0) {
        a1 = v_stack_p50;
        result = MiFlushTbList(a1, a2, (unsigned int)(v_stack_p20), a4);
        result = MiReleaseProcessorFlushList(a1, a2, (unsigned int)(v_stack_p20), a4);
        v_stack_p50 = 0;
    }
    result = MiMakeProtoLeafValid(v_rbx, 24, v_stack_p40, a4);
    v_stack_p48 = (unsigned int)(result);
    if (sign_flag) goto loc_00244BCD;
    v_r15 = (v_rbx) - (8);
loc_00244AE2:
    goto loc_00243FB1;
loc_00244AF1:
    a2 = (v_r15 + 8) << (25);
    a2 = (a2) - (v_stack_m148);
    a2 = (a2) >> (16);
    result = (a2) & (0xFFFFFFFFFFFFF000ULL);
    if (result == 0x7FFE0000ULL) goto loc_00244B22;
    if (result != (*(unsigned __int64 *)(v_rip + 12488800))) goto loc_00244B34;
    if (*(unsigned __int64 *)(v_rip + 12488800) == 0) goto loc_00244B34;
loc_00244B22:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m110 + 1532)))) & (1)) == 0) goto loc_00244BCD;
loc_00244B34:
    if (((*(unsigned int *)(v_stack_p18 + 48)) & (0x200000ULL)) != 0) goto loc_00244BA2;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) == 0) goto loc_00244BA2;
    a2 = (a2) >> (12);
    result = MiGetProtoPteAddress(v_stack_p18, a2, 8, v_stack_m140);
    result = MiIsPrototypePteVadLookup(v_stack_p50, a2, 8, v_stack_m140);
    if ((unsigned int)(result) != 0) goto loc_002445C2;
    if (*(unsigned __int64 *)(v_rip + 12488968) == 0) goto loc_00244B8E;
    if ((((unsigned __int8)(v_stack_p50)) & (16)) == 0) {
        a1 = *(unsigned __int64 *)(v_rip + 12488968);
        a1 = ~(a1);
        a1 = (a1) & (v_stack_p50);
    }
    a1 = (a1) >> (16);
    if (result == a1) goto loc_002445C2;
loc_00244BA2:
    if (*(unsigned __int64 *)(v_rip + 12488919) == 0) goto loc_00244BBF;
    v_rdi = v_stack_p50;
    if ((((unsigned __int8)(v_stack_p50)) & (16)) == 0) {
        v_rdi = *(unsigned __int64 *)(v_rip + 12488919);
        v_rdi = ~(v_rdi);
        v_rdi = (v_rdi) & (v_stack_p50);
    }
    v_rdi = (v_rdi) >> (16);
    if (((unsigned int)((unsigned int)(v_stack_p20))) == 2) goto loc_002445C2;
loc_00244BCD:
    v_stack_p48 = 0xC0000434ULL;
    goto loc_00244AE2;
loc_00244BDA:
loc_00244BE1:
    goto loc_0024423E;
loc_00244BED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14163653)))) & (64)) == 0) goto loc_0024497B;
    result = KiCheckVpBackingLongSpinWaitHypercall(3, v_rip + 14461144, (unsigned int)(v_stack_p20), v_stack_m140);
    if ((unsigned __int8)(result) == 0) goto loc_0024497B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p50)), v_rip + 14461144, (unsigned int)(v_stack_p20), v_stack_m140);
    goto loc_0024497D;
loc_00244C14:
    result = ((unsigned int)((unsigned int)(v_stack_p50)) + v_rdi * 1) ^ ((unsigned int)((unsigned int)(v_stack_p50)));
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ ((unsigned int)((unsigned int)(v_stack_p50)) + v_rdi * 1);
    *(unsigned __int64 *)(v_stack_m140 + 40) = result;
    goto loc_00244711;
loc_00244C34:
    *(unsigned __int8 *)(v_stack_p50 + 25) = 1;
    goto loc_00244711;
loc_00244C3E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 624) == 0) goto loc_002442AC;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 624)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_002442AC;
    result = LOCK_ADDRESS_SPACE(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(v_stack_p20), v_stack_m140);
    result = UNLOCK_ADDRESS_SPACE(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(v_stack_p20), v_stack_m140);
    goto loc_002442AC;
}
```

## 5. (Beta) C Style

```c
int64_t MiWalkVaRange(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint8_t v_stack_m156;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint32_t v_stack_m184;
    uint8_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mFF;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (392);
    v_stack_p8 = 17;
    Arg1 = 0;
    local_r15 = (Arg1) >> (9);
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    local_r15 = (local_r15) & (Arg2);
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    v_stack_m180 = 0;
    v_stack_m168 = 0;
    v_stack_m178 = 0;
    local_rbx = (Arg2) >> (9);
    local_r15 = (local_r15) + (local_rdi);
    local_rbx = (local_rbx) & (Arg2);
    local_rbx = (local_rbx) + (local_rdi);
    v_stack_m150 = 0;
    v_stack_p10 = local_rbx;
    v_stack_m110 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m160 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    result = MiLockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, Arg3, Arg4);
    v_stack_m188 = (uint8_t)(result);
loc_00243CAE:
    if (local_r15 > local_rbx) goto loc_00244451;
    Arg2 = 0;
    v_stack_m120 = v_xmm0;
    result = memset(v_stack_m104, Arg2, 188, Arg4);
    result = (local_rdi) << (25);
    local_rdi = (local_r15) << (25);
    local_rdi = (local_rdi) - (result);
    local_rsi = (local_rbx) << (25);
    local_rsi = (local_rsi) - (result);
    local_rdi = (local_rdi) >> (16);
    v_stack_m148 = result;
    local_rsi = (local_rsi) >> (16);
    v_stack_m108 = 0x2061ULL;
    result = MiGetLeafVa(local_rdi, Arg2, 188, Arg4);
    if (result >= local_rdi) goto loc_002448B3;
loc_00243D18:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
loc_00243D2F:
    Arg3 = 0;
    result = MiFastLockLeafPageTable(local_rbx, local_rdi, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00244794;
    result = (uint32_t)((result) - 1);
    v_stack_m120 = (uint32_t)(result);
    local_rbx = (local_rdi) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (local_rsi);
    v_stack_m118 = local_rbx;
loc_00243D72:
    v_stack_m170 = 1;
    if (local_rbx != local_r15) goto loc_00244423;
loc_00243D83:
    local_r10 = 0;
loc_00243D86:
    result = local_rsi;
    if (local_rbx != 0) {
        Arg1 = local_rbx;
        Arg1 = (Arg1) >> (9);
        Arg1 = (Arg1) & (local_r14);
        result = local_rsi;
        Arg1 = (Arg1) + (result);
        v_stack_m150 = Arg1;
    }
loc_00243DAF:
loc_00243DB3:
    v_stack_m130 = 0;
    v_stack_m184 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m170)) == 0) goto loc_00244061;
    if (local_r15 < result) goto loc_00243E0D;
    if (local_r15 > result) goto loc_00243E0D;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_00243E0D;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_r15))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_r15))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002440DF;
loc_00243E0D:
    if (*(uint64_t *)(local_r15) == 0) goto loc_00244061;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_00243E26;
    if (condition_is_below) goto loc_00244A59;
loc_00243E26:
    if (v_stack_m168 == 0) goto loc_00243F23;
    local_rbx = 0;
    if (v_stack_p8 == 18) goto loc_00244960;
loc_00243E3E:
    if (v_stack_p8 < 18) goto loc_002440C0;
loc_00243E4B:
    if (sign_flag) goto loc_00243E71;
    if (condition_is_below) goto loc_00243E71;
    result = (*(uint64_t *)(v_stack_m168 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 1) {
        result = *(uint64_t *)(v_stack_m168 + 0x8);
    }
    if (((Arg1) & (*(uint64_t *)(v_stack_m168))) != 0) goto loc_0024416C;
    v_stack_m158 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x20))) >> (16));
    result = (uint8_t)((result) & (223));
    v_stack_m156 = (uint8_t)(result);
    *(uint32_t *)(v_stack_m168 + 0x20) = (uint32_t)((uint32_t)(v_stack_m158));
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_m168, local_rdi, Arg3, Arg4);
    goto loc_00243EEC;
loc_00243EAA:
    *(uint64_t *)(local_rdi) = local_rdi;
loc_00243EB0:
    *(uint64_t *)(local_rdi + 0x8) = local_rdi;
    Arg2 = (local_rdi) >> (4);
    Arg2 = (Arg2) + (Arg2);
    Arg1 = (Arg2) ^ (*(uint64_t *)(v_stack_m168));
    Arg1 = (Arg1) & (*(uint64_t *)(v_stack_m168));
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(v_stack_m168) = Arg1;
loc_00243ED7:
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_m168, Arg2, Arg3, Arg4);
    if (0 != 0) {
        result = 1;
        *(uint32_t *)(local_rbx + 0x10) = (uint32_t)(result);
    }
    if (v_stack_p8 == 18) goto loc_002446F4;
    if (((uint8_t)(v_stack_p8)) <= 1) goto loc_0024461C;
loc_00243F18:
    local_r14 = 0;
    v_stack_m168 = 0;
    local_r12 = 0;
loc_00243F23:
    v_stack_m190 = v_stack_m138;
    v_stack_m198 = v_stack_m128;
    v_stack_m1A0 = Arg5;
    v_stack_m1A8 = (uint32_t)((uint32_t)(v_stack_p20));
    result = MiActOnPte(v_stack_p18, (uint32_t)(v_stack_m170), local_r15, 0);
    if ((uint32_t)(result) != 0) goto loc_002442CF;
loc_00243F69:
    if (v_stack_m138 != 0) goto loc_0024475D;
loc_00243F76:
    local_r15 = (local_r15) + (8);
    if (0 != 0) goto loc_002441EC;
    v_stack_m178 = v_stack_m178;
    v_stack_m180 = (uint32_t)((uint32_t)(v_stack_m180));
    v_stack_m168 = 0;
    v_stack_m158 = local_r15;
    if (sign_flag) goto loc_002441F1;
loc_00243FB1:
    if (local_r15 > v_stack_p10) goto loc_002441F1;
    if (((local_r15) & (0xFFFULL)) == 0) goto loc_002441F1;
    if ((((uint8_t)(local_r15)) & (120)) == 0) goto loc_0024452D;
loc_00243FD4:
    local_r10 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (1)) != 0) goto loc_00244147;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_002444B4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) != 0) goto loc_00244476;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9)) != 0) goto loc_002444D8;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) != 0) goto loc_002444A3;
loc_00244030:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) > 7) goto loc_002441D0;
loc_00244039:
    if (0 == 0) goto loc_00243DB3;
    if ((((uint32_t)(v_stack_m170)) & (*(uint64_t *)(local_r14))) != 0) goto loc_002441FA;
    goto loc_00243DAF;
loc_00244061:
    if (((*(uint32_t *)(v_stack_p18 + 0x30)) & (0x200000ULL)) != 0) goto loc_00243E26;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) == 0) goto loc_00243E26;
    Arg2 = (local_r15) << (25);
    Arg2 = (Arg2) - (v_stack_m148);
    Arg2 = (Arg2) >> (16);
    Arg2 = (Arg2) >> (12);
    result = MiGetProtoPteAddress(v_stack_p18, Arg2, 8, v_stack_m140);
    if (result != 0) goto loc_002445CB;
    if (v_stack_m170 != ((uint32_t)(result))) goto loc_00243E26;
    goto loc_002441F1;
loc_002440C0:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD811E4)) & ((uint32_t)(local_rbx))) == 0) goto loc_002447E9;
loc_002440CE:
loc_002440D0:
    if (!sign_flag) goto loc_00243E3E;
    goto loc_002440C0;
loc_002440DF:
    if (((*(uint64_t *)(v_rip + 0xD8299E)) & (0x600000ULL)) == 0) goto loc_00243E0D;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00243E0D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00243E0D;
    result = (local_r15) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (local_rbx) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_00243E0D;
loc_00244147:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)))) <= 7) goto loc_00244030;
    if ((uint8_t)(*(uint8_t *)(local_rbx + 0x38B9)) == 0) goto loc_002441D9;
    goto loc_0024447B;
loc_0024416C:
    result = (*(uint8_t *)(local_rbx + 0x38B9)) & (-2);
    result = (result) | (local_rbx);
    if ((*(uint64_t *)(result * 8)) == (result * 8)) goto loc_00244880;
    if ((*(uint64_t *)(*(uint64_t *)(result * 8) + 0x8)) != (result * 8)) goto loc_00244BDA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result * 8)) + 0x8)) != (*(uint64_t *)(result * 8))) goto loc_00244BDA;
    *(uint64_t *)(result * 8) = *(uint64_t *)(*(uint64_t *)(result * 8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result * 8)) + 0x8) = result * 8;
    if ((*(uint64_t *)(result * 8)) == (result * 8)) goto loc_00243EAA;
    *(uint64_t *)(*(uint64_t *)(result * 8) + 0x8) = *(uint64_t *)(result * 8);
    *(uint64_t *)(*(uint64_t *)(result * 8 + 0x8)) = *(uint64_t *)(result * 8);
    goto loc_00243EB0;
loc_002441D0:
    if (1 == 0) goto loc_002444DF;
loc_002441D9:
    if ((((uint8_t)(*(uint64_t *)(result * 8))) & (30)) == 0) goto loc_00244519;
    goto loc_0024447B;
loc_002441EC:
loc_002441F1:
    if (0 == 0) goto loc_002449E4;
loc_002441FA:
    result = MiUnlockProtoPoolPage(0, v_stack_p8, 1, v_stack_m140);
    local_rdi = 0;
    v_stack_m168 = 0;
loc_00244213:
    if (v_stack_m178 == 0) goto loc_00244260;
    result = MiFlushTbList(v_stack_m178, v_stack_p8, 1, v_stack_m140);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_00244BE1;
loc_0024423E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x15C))) - 1);
    v_stack_m178 = 0;
    Arg1 = (v_stack_m178) * (result);
    *(uint64_t *)(Arg1 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) * 1 + 0x51F0) = 0;
loc_00244260:
    if (v_stack_m150 != 0) {
        Arg2 = v_stack_m150;
        Arg1 = v_stack_m160;
        result = MiUnlockPageTable(Arg1, Arg2, 1, v_stack_m140);
        v_stack_m150 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_m160, v_stack_m188, 1, v_stack_m140);
    if (!sign_flag) goto loc_002442AC;
    if (((uint32_t)((uint32_t)(v_stack_m184))) != 0xC0000434ULL) goto loc_002448A1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8)))) & (15)) == 0) goto loc_00244C3E;
loc_002442AC:
    result = MiLockWorkingSetShared(v_stack_m160, v_stack_m188, 1, v_stack_m140);
    goto loc_00243CAE;
loc_002442CF:
    if (((uint32_t)(result)) == 274) goto loc_00244719;
    if (((uint32_t)(result)) != 0xC0000021ULL) goto loc_00244898;
    local_rbx = (local_r15) << (25);
    local_rbx = (local_rbx) - (v_stack_m148);
    local_rbx = (local_rbx) >> (16);
    if (v_stack_m178 != 0) goto loc_00244988;
    result = MiGetProcessorFlushList(v_stack_m160, v_stack_m188, 1, v_stack_m140);
    v_stack_m178 = result;
    Arg3 = 0;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0x14) = 10;
    *(uint64_t *)(result) = v_stack_m160;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8))) >> (8));
    result = (uint8_t)((result) >> (3));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(result + 0x18) = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8)))) & (15)) != 0) goto loc_00244361;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (v_stack_m160 != Arg1) goto loc_002449D7;
loc_00244361:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_00244374:
    *(uint32_t *)(result + 0x8) = (uint32_t)(Arg1);
    *(uint16_t *)(result + 0x19) = 0;
    *(uint32_t *)(result + 0x1C) = 0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
loc_0024438E:
    if ((*(uint32_t *)(result + 0x8)) != 1) goto loc_0024483B;
loc_0024439D:
loc_002443A0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C))) == 0) goto loc_0024468C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (2)) != 0) goto loc_0024463E;
    if (((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0xC00ULL)) != 0) goto loc_0024468C;
    Arg3 = (uint32_t)((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0x3FFULL));
    result = (*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg3 + 1) << (12);
    Arg2 = (Arg2) + (result);
    if (Arg2 != local_rbx) goto loc_0024440B;
    if ((1 + Arg3 * 1) <= Arg3) goto loc_0024440B;
    if ((1 + Arg3 * 1) <= 0x3FFULL) goto loc_00244C14;
loc_0024440B:
    goto loc_00244666;
loc_00244423:
    if (((*(uint32_t *)(v_stack_p18 + 0x30)) & (0x200000ULL)) == 0) goto loc_0024491B;
loc_00244438:
    v_stack_m180 = (uint32_t)((uint32_t)(0xC0000434ULL));
    if (local_rbx != 0) goto loc_00244755;
loc_00244451:
    result = MiUnlockWorkingSetShared(v_stack_m160, v_stack_m188, Arg3, result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 1 + 5 * 8);
    local_rsp = (local_rsp) + (392);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000434ULL)));
loc_00244476:
loc_0024447B:
    result = (uint32_t)((uint32_t)((uint32_t)(0xC0000434ULL)));
    local_r10 = v_stack_p18;
    if (((*(uint32_t *)(v_rip + 0xD8267F)) & (0x4000000ULL)) != 0) {
        Arg3 = (uint32_t)(v_stack_m160);
        Arg2 = 1;
        Arg1 = 2;
        result = EtwTraceShouldYieldProcessor(Arg1, Arg2, Arg3, result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 1 + 5 * 8);
        local_r10 = 0;
    }
    if (2 != 0) goto loc_002441F1;
    goto loc_00244039;
loc_002444A3:
    if (result == (*(uint64_t *)(Arg1 + 0x8))) goto loc_00244030;
    goto loc_0024447B;
loc_002444B4:
    if (1 <= 7) goto loc_00244039;
    if ((uint8_t)(*(uint8_t *)(Arg1 + 0x38B9)) == 0) goto loc_002441D9;
    goto loc_0024447B;
loc_002444D8:
    goto loc_0024447B;
loc_002444DF:
    if (1 != 0) goto loc_002441D9;
loc_002444E8:
    *(uint32_t *)(Arg1 + 0x83AC) = 0;
    *(uint32_t *)(Arg1 + 0x865C) = 0;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00244810;
loc_00244510:
    goto loc_0024447B;
loc_00244519:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_002444E8;
    goto loc_0024447B;
loc_0024452D:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p68 + 0xB8))) & (15));
    if (((uint8_t)(result)) > 5) goto loc_00243FD4;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p68 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_002449EB;
loc_00244559:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_002446EF;
loc_0024457B:
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144))) << (6);
    if (condition_is_below) goto loc_002441F1;
    goto loc_00243FD4;
loc_00244591:
    result = MI_PROTO_FORMAT_COMBINED(6, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), 1);
    if ((uint8_t)(result) == 0) goto loc_00244A6A;
    if (*(uint64_t *)(v_rip + 0xBE96D8) == 0) goto loc_002445BE;
    local_rdi = 6;
    if (((6) & (16)) == 0) {
        local_rdi = *(uint64_t *)(v_rip + 0xBE96D8);
        local_rdi = ~(local_rdi);
        local_rdi = (local_rdi) & (6);
    }
    local_rdi = (local_rdi) >> (16);
loc_002445C2:
    if (local_rdi == 0) goto loc_00243E26;
loc_002445CB:
    result = (0) ^ (local_rdi);
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) == 0) goto loc_00243F23;
    local_r12 = 0;
    if (0 != 0) {
        Arg2 = v_stack_p8;
        Arg1 = 0;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), 1);
        local_r12 = 0;
    }
    result = MiLockProtoPoolPage(local_rdi, v_stack_p8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), 1);
    v_stack_p60 = result;
    if (result == 0) goto loc_002449F7;
    goto loc_00243F23;
loc_0024461C:
    if ((*(uint32_t *)(v_rip + 0xD826FD)) != 0) {
        Arg1 = v_cr8;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, v_stack_p8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), 1);
    }
    goto loc_00243F18;
loc_0024463E:
    if (0 == 0) goto loc_0024468C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (2)) != 0) goto loc_0024468C;
    if (((*(uint64_t *)(result + local_r10 - 0x1 + 0x5 * 8)) & (0xC00ULL)) != 0) goto loc_0024468C;
loc_00244666:
    local_r11 = (local_rdi) << (12);
    Arg2 = (*(uint64_t *)(result + local_r10 - 0x1 + 0x5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg2 == (6 + local_r11 * 1)) goto loc_00244990;
loc_00244684:
    Arg3 = 0;
loc_0024468C:
    if (0 == (*(uint32_t *)(v_stack_p50 + 0xC))) goto loc_002446FE;
loc_00244692:
    if (local_rdi == 0) goto loc_00244711;
    Arg2 = (uint32_t)(0x400ULL);
    if ((local_rdi - 1) <= 0x3FFULL) { Arg2 = local_rdi; }
    Arg1 = (6) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((Arg2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    *(uint64_t *)(v_stack_p50 + local_r10 * 8 + 0x28) = result;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x1C))) + 1);
    Arg1 = (Arg2) << (12);
    local_rbx = (6) + (Arg1);
    *(uint32_t *)(v_stack_p50 + 0x1C) = (uint32_t)(local_r10);
    local_rdi = (local_rdi) - (Arg2);
    if (condition_is_equal) goto loc_00244692;
    if (((uint32_t)(local_r10)) == (*(uint32_t *)(v_stack_p50 + 0xC))) goto loc_0024439D;
    goto loc_00244692;
loc_002446EF:
    goto loc_0024457B;
loc_002446F4:
    goto loc_00243F18;
loc_002446FE:
    if ((uint32_t)(v_stack_m160) == 0) goto loc_002448DB;
    if ((*(uint8_t *)(v_stack_p50 + 0x19)) == 0) goto loc_00244C34;
loc_00244711:
    goto loc_00243F69;
loc_00244719:
    Arg4 = 0;
    v_stack_p20 = v_stack_m130;
    Arg1 = (local_r15) << (25);
    Arg1 = (Arg1) - (v_stack_m148);
    Arg1 = (Arg1) >> (16);
    result = MiCopyOnWrite(Arg1, local_r15, Arg4 - 1, Arg4);
    v_stack_p44 = (uint32_t)(result);
    local_r15 = (local_r15) - (8);
    goto loc_00243F69;
loc_00244755:
    goto loc_00243D83;
loc_0024475D:
    local_r12 = local_rdi;
    local_r14 = result;
    if (result != 0) {
        Arg2 = v_stack_p8;
        Arg1 = result;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, Arg4 - 1, Arg4);
        Arg2 = v_stack_m138;
        local_r14 = 0;
        v_stack_p60 = 0;
        local_r12 = 0;
    }
    result = MiReleasePageFileInfo(v_stack_m128, Arg2, 1, Arg4);
    goto loc_00243F76;
loc_00244794:
    v_stack_m50 = v_stack_m120;
    result = (uint32_t)(((uint32_t)(v_stack_m104)) & (0xFFFFFE7FULL));
    v_stack_mE8 = local_rbx;
    result = (uint32_t)((result) | (64));
    v_stack_mE0 = local_rdi;
    v_stack_m104 = (uint32_t)(result);
    v_stack_m58 = v_rip + 847695;
    v_stack_mFF = (uint8_t)(v_stack_p40);
    v_stack_mD8 = (uint32_t)((uint32_t)(result));
    result = MiWalkPageTables(v_stack_m108, Arg2, 1, Arg4);
    goto loc_00243D72;
loc_002447E9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD822C9)))) & (64)) == 0) goto loc_002440CE;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m108, Arg2, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002440CE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m118)), Arg2, 1, Arg4);
    goto loc_002440D0;
loc_00244810:
loc_00244817:
    if ((uint8_t)(result) != 0) goto loc_00244817;
    if (condition_is_above_or_equal) goto loc_00244510;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(v_stack_m118)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1)))), 1, Arg4);
    local_r10 = 0;
    goto loc_00244510;
loc_0024483B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x10)))) & (4)) != 0) goto loc_0024439D;
    if (v_stack_m118 < result) goto loc_0024439D;
    if (v_stack_m118 > result) goto loc_0024439D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x10))) | (4));
    *(uint32_t *)(v_stack_p50 + 0x10) = (uint32_t)(Arg1);
    goto loc_0024439D;
loc_00244880:
    result = (*(uint64_t *)(local_r14)) & (Arg1);
    *(uint64_t *)(local_r14) = result;
    goto loc_00243ED7;
loc_00244898:
    v_stack_p48 = (uint32_t)(result);
    goto loc_00243F69;
loc_002448A1:
    if (1 != 0xC0000017ULL) goto loc_002442AC;
loc_002448B3:
    if (result < (*(uint64_t *)(v_rip + 0xBEAAC6))) goto loc_002448C9;
    if (result <= (*(uint64_t *)(v_rip + 0xBEAACD))) goto loc_00243D18;
loc_002448C9:
    result = MiGetAnyMultiplexedVm(2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1)))), 1, Arg4);
    goto loc_00243D2F;
loc_002448DB:
    if ((*(uint8_t *)(v_stack_p50 + 0x19)) != 0) goto loc_00244711;
    result = qsort(v_stack_p50 + 40, 0, 8, v_rip + 4525980);
    result = MiCompressTbFlushList(v_stack_p50, 0, 8, v_rip + 4525980);
    Arg3 = 0;
    goto loc_002443A0;
loc_0024491B:
    if ((*(uint64_t *)(local_r10 + 0x50)) == 0) goto loc_00244438;
    local_rdi = (local_rdi) >> (12);
    result = MiGetProtoPteAddress(0, local_rdi, 8, v_stack_m140);
    if (result == 0) goto loc_00244438;
    local_r10 = 0;
    v_stack_p58 = 0;
    goto loc_00243D86;
loc_00244960:
    if (condition_is_above_or_equal) goto loc_00243E4B;
loc_0024496D:
    local_rbx = (uint32_t)((result) + 1);
    if (((*(uint32_t *)(v_rip + 0xD80937)) & ((uint32_t)(local_rbx))) == 0) goto loc_00244BED;
loc_0024497B:
loc_0024497D:
    if (!sign_flag) goto loc_00244960;
    goto loc_0024496D;
loc_00244988:
    Arg3 = 0;
    goto loc_0024438E;
loc_00244990:
    Arg1 = (uint32_t)((0) & (0x3FFULL));
    if ((local_rdi + Arg1 * 1) > 0x3FFULL) goto loc_00244684;
    if ((local_rdi + Arg1 * 1) <= Arg1) goto loc_00244684;
    result = (*(uint64_t *)(local_r14 + 0x18)) - (v_stack_p50);
    result = (result) ^ (result + local_rdi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + local_rdi * 1);
    *(uint64_t *)(v_stack_m140) = result;
    goto loc_00243F69;
loc_002449D7:
    goto loc_00244374;
loc_002449E4:
    local_rdi = 0;
    goto loc_00244213;
loc_002449EB:
    goto loc_00244559;
loc_002449F7:
    result = 0 + 192;
    if (v_stack_p50 != 0) {
        result = MiFlushTbList(v_stack_p50, local_rdi + Arg1 * 1, Arg3, v_stack_m140);
        result = MiReleaseProcessorFlushList(v_stack_p50, local_rdi + Arg1 * 1, Arg3, v_stack_m140);
        Arg1 = 0;
        v_stack_p50 = 0;
    }
    if (v_stack_p78 != 0) {
        Arg2 = v_stack_p78;
        Arg1 = v_stack_p68;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, v_stack_m140);
        v_stack_p78 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p68, v_stack_p40, Arg3, v_stack_m140);
    Arg4 = 0;
    Arg3 = 0;
    result = MmAccessFault(Arg4 + 2, 0, Arg3, Arg4);
    goto loc_002442AC;
loc_00244A59:
    if (((uint32_t)((uint32_t)(v_stack_p20))) == 2) goto loc_00244591;
loc_00244A6A:
    result = MI_PROTO_FORMAT_COMBINED(v_stack_p78, 0, (uint32_t)(v_stack_p20), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00244AF1;
    if (((uint32_t)((uint32_t)(v_stack_p20))) == 1) goto loc_00244BCD;
    if (0 != 0) {
        Arg2 = v_stack_p8;
        Arg1 = 0;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, (uint32_t)(v_stack_p20), Arg4);
        local_r14 = 0;
        v_stack_p60 = 0;
        local_r12 = 0;
    }
    if (v_stack_p50 != 0) {
        Arg1 = v_stack_p50;
        result = MiFlushTbList(Arg1, Arg2, (uint32_t)(v_stack_p20), Arg4);
        result = MiReleaseProcessorFlushList(Arg1, Arg2, (uint32_t)(v_stack_p20), Arg4);
        v_stack_p50 = 0;
    }
    result = MiMakeProtoLeafValid(local_rbx, 24, v_stack_p40, Arg4);
    v_stack_p48 = (uint32_t)(result);
    if (sign_flag) goto loc_00244BCD;
    local_r15 = (local_rbx) - (8);
loc_00244AE2:
    goto loc_00243FB1;
loc_00244AF1:
    Arg2 = (local_r15 + 8) << (25);
    Arg2 = (Arg2) - (v_stack_m148);
    Arg2 = (Arg2) >> (16);
    result = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    if (result == 0x7FFE0000ULL) goto loc_00244B22;
    if (result != (*(uint64_t *)(v_rip + 0xBE9060))) goto loc_00244B34;
    if (*(uint64_t *)(v_rip + 0xBE9060) == 0) goto loc_00244B34;
loc_00244B22:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m110 + 0x5FC)))) & (1)) == 0) goto loc_00244BCD;
loc_00244B34:
    if (((*(uint32_t *)(v_stack_p18 + 0x30)) & (0x200000ULL)) != 0) goto loc_00244BA2;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) == 0) goto loc_00244BA2;
    Arg2 = (Arg2) >> (12);
    result = MiGetProtoPteAddress(v_stack_p18, Arg2, 8, v_stack_m140);
    result = MiIsPrototypePteVadLookup(v_stack_p50, Arg2, 8, v_stack_m140);
    if ((uint32_t)(result) != 0) goto loc_002445C2;
    if (*(uint64_t *)(v_rip + 0xBE9108) == 0) goto loc_00244B8E;
    if ((((uint8_t)(v_stack_p50)) & (16)) == 0) {
        Arg1 = *(uint64_t *)(v_rip + 0xBE9108);
        Arg1 = ~(Arg1);
        Arg1 = (Arg1) & (v_stack_p50);
    }
    Arg1 = (Arg1) >> (16);
    if (result == Arg1) goto loc_002445C2;
loc_00244BA2:
    if (*(uint64_t *)(v_rip + 0xBE90D7) == 0) goto loc_00244BBF;
    local_rdi = v_stack_p50;
    if ((((uint8_t)(v_stack_p50)) & (16)) == 0) {
        local_rdi = *(uint64_t *)(v_rip + 0xBE90D7);
        local_rdi = ~(local_rdi);
        local_rdi = (local_rdi) & (v_stack_p50);
    }
    local_rdi = (local_rdi) >> (16);
    if (((uint32_t)((uint32_t)(v_stack_p20))) == 2) goto loc_002445C2;
loc_00244BCD:
    v_stack_p48 = 0xC0000434ULL;
    goto loc_00244AE2;
loc_00244BDA:
loc_00244BE1:
    goto loc_0024423E;
loc_00244BED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD81EC5)))) & (64)) == 0) goto loc_0024497B;
    result = KiCheckVpBackingLongSpinWaitHypercall(3, v_rip + 14461144, (uint32_t)(v_stack_p20), v_stack_m140);
    if ((uint8_t)(result) == 0) goto loc_0024497B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p50)), v_rip + 14461144, (uint32_t)(v_stack_p20), v_stack_m140);
    goto loc_0024497D;
loc_00244C14:
    result = ((uint32_t)((uint32_t)(v_stack_p50)) + local_rdi * 1) ^ ((uint32_t)((uint32_t)(v_stack_p50)));
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ ((uint32_t)((uint32_t)(v_stack_p50)) + local_rdi * 1);
    *(uint64_t *)(v_stack_m140 + 0x28) = result;
    goto loc_00244711;
loc_00244C34:
    *(uint8_t *)(v_stack_p50 + 0x19) = 1;
    goto loc_00244711;
loc_00244C3E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x270) == 0) goto loc_002442AC;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x270)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_002442AC;
    result = LOCK_ADDRESS_SPACE(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(v_stack_p20), v_stack_m140);
    result = UNLOCK_ADDRESS_SPACE(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(v_stack_p20), v_stack_m140);
    goto loc_002442AC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00243BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
