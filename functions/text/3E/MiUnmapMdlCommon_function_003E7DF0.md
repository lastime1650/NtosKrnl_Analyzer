# MiUnmapMdlCommon

- RVA: `0x003E7DF0`–`0x003E8485` (길이 `1,685` bytes)
- VA: `0x00000001403E7DF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009575C`
- 디코드: `400`개 명령, `1,685/1,685` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x003E7EBB` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x003E7EFE` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)
- `0x003E7F05` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x003E7F3F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003E7F44` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x003E7F67` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x003E7FB7` → [MiDecreaseUsedPtes](../37/MiDecreaseUsedPtes_function_00378080.md) (function, `0x00378080`)
- `0x003E7FC9` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x003E7FD4` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003E8003` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x003E8013` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x003E8064` → [MiRewritePteWithLockBit](../32/MiRewritePteWithLockBit_function_00322FEC.md) (function, `0x00322FEC`)
- `0x003E8076` → [MiInsertLargeTbFlushEntry](../37/MiInsertLargeTbFlushEntry_function_0037827C.md) (function, `0x0037827C`)
- `0x003E80D2` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x003E8146` → [MiDereferenceIoPages](../2A/MiDereferenceIoPages_function_002AB1B0.md) (function, `0x002AB1B0`)
- `0x003E8189` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003E81AF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003E81B5` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x003E81BA` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x003E81D9` → [MiDecreaseUsedPtes](../37/MiDecreaseUsedPtes_function_00378080.md) (function, `0x00378080`)
- `0x003E81E4` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003E81EF` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x003E820C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003E8238` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003E823F` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003E825E` → [MiSplitPageChain](../4A/MiSplitPageChain_function_004A9420.md) (function, `0x004A9420`)
- `0x003E826C` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003E82CE` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)
- `0x003E82D5` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x003E831B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003E8340` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x003E834A` → [MiUnlinkPageChainHead](../36/MiUnlinkPageChainHead_function_00365C40.md) (function, `0x00365C40`)
- `0x003E837D` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x003E839B` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x003E83AA` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x003E83B5` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x003E83C7` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x003E8407` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x003E8436` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003E8441` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x003E8475` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)

### Direct callers
- [MmUnmapReservedMapping](MmUnmapReservedMapping_function_003E7BE0.md) at `0x003E7CE4`
- [MmUnmapLockedRestartPages](../../page/7F/MmUnmapLockedRestartPages_function_007F90E0.md) at `0x007F912E`

### Static image references
- `0x003E7E12` → RVA `0x00E38200` (`.data`; read)
- `0x003E7F31` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003E8097` → RVA `0x00010880` (`.rdata`; read)
- `0x003E810D` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003E8229` → RVA `0x00E35FA8` (`.data`; read)
- `0x003E8257` → RVA `0x00E35FB8` (`.data`; read)
- `0x003E83CC` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E7DF0  4C 8B DC                        mov r11, rsp
003E7DF3  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
003E7DF7  53                              push rbx
003E7DF8  55                              push rbp
003E7DF9  56                              push rsi
003E7DFA  57                              push rdi
003E7DFB  41 54                           push r12
003E7DFD  41 55                           push r13
003E7DFF  41 56                           push r14
003E7E01  41 57                           push r15
003E7E03  48 81 EC A8 00 00 00            sub rsp, 0xa8
003E7E0A  33 C0                           xor eax, eax
003E7E0C  48 8B F1                        mov rsi, rcx
003E7E0F  0F 57 C0                        xorps xmm0, xmm0
003E7E12  48 8D 0D E7 03 A5 00            lea rcx, [rip + 0xa503e7]
003E7E19  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
003E7E1E  49 89 43 A0                     mov qword ptr [r11 - 0x60], rax
003E7E22  48 8B DE                        mov rbx, rsi
003E7E25  49 8D 41 30                     lea rax, [r9 + 0x30]
003E7E29  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
003E7E33  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003E7E38  48 8B EA                        mov rbp, rdx
003E7E3B  48 8B C2                        mov rax, rdx
003E7E3E  48 F7 D8                        neg rax
003E7E41  1B C0                           sbb eax, eax
003E7E43  F7 D0                           not eax
003E7E45  83 E0 08                        and eax, 8
003E7E48  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
003E7E4F  48 85 D2                        test rdx, rdx
003E7E52  48 8B C2                        mov rax, rdx
003E7E55  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
003E7E5F  48 0F 44 C1                     cmove rax, rcx
003E7E63  48 C1 EB 09                     shr rbx, 9
003E7E67  49 23 D8                        and rbx, r8
003E7E6A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003E7E6F  48 8B C2                        mov rax, rdx
003E7E72  48 03 D8                        add rbx, rax
003E7E75  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
003E7E7D  48 8B CB                        mov rcx, rbx
003E7E80  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
003E7E85  48 C1 E9 09                     shr rcx, 9
003E7E89  49 23 C8                        and rcx, r8
003E7E8C  48 8D 04 C3                     lea rax, [rbx + rax*8]
003E7E90  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003E7E95  48 8B C2                        mov rax, rdx
003E7E98  48 03 C8                        add rcx, rax
003E7E9B  41 BC 01 00 00 00               mov r12d, 1
003E7EA1  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
003E7EA6  48 8B 01                        mov rax, qword ptr [rcx]
003E7EA9  84 C0                           test al, al
003E7EAB  79 18                           jns 0x1403e7ec5
003E7EAD  41 8D 4C 24 0F                  lea ecx, [r12 + 0xf]
003E7EB2  48 C7 44 24 38 00 02 00 00      mov qword ptr [rsp + 0x38], 0x200
003E7EBB  E8 40 FB F4 FF                  call 0x140337a00
003E7EC0  48 8B F8                        mov rdi, rax
003E7EC3  EB 07                           jmp 0x1403e7ecc
003E7EC5  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
003E7ECA  33 FF                           xor edi, edi
003E7ECC  45 33 FF                        xor r15d, r15d
003E7ECF  44 89 BC 24 F0 00 00 00         mov dword ptr [rsp + 0xf0], r15d
003E7ED7  45 33 F6                        xor r14d, r14d
003E7EDA  44 0F 20 C1                     mov rcx, cr8
003E7EDE  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
003E7EE3  48 85 ED                        test rbp, rbp
003E7EE6  74 27                           je 0x1403e7f0f
003E7EE8  41 8D 47 02                     lea eax, [r15 + 2]
003E7EEC  44 89 A4 24 F8 00 00 00         mov dword ptr [rsp + 0xf8], r12d
003E7EF4  3A C8                           cmp cl, al
003E7EF6  48 8B CD                        mov rcx, rbp
003E7EF9  75 0A                           jne 0x1403e7f05
003E7EFB  41 B5 11                        mov r13b, 0x11
003E7EFE  E8 71 16 E5 FF                  call 0x140239574
003E7F03  EB 3F                           jmp 0x1403e7f44
003E7F05  E8 E6 4C E9 FF                  call 0x14027cbf0
003E7F0A  44 8A E8                        mov r13b, al
003E7F0D  EB 35                           jmp 0x1403e7f44
003E7F0F  44 21 B4 24 F8 00 00 00         and dword ptr [rsp + 0xf8], r14d
003E7F17  44 0F 20 C0                     mov rax, cr8
003E7F1B  B9 02 00 00 00                  mov ecx, 2
003E7F20  3A C1                           cmp al, cl
003E7F22  75 05                           jne 0x1403e7f29
003E7F24  41 B5 11                        mov r13b, 0x11
003E7F27  EB 1B                           jmp 0x1403e7f44
003E7F29  45 0F 20 C5                     mov r13, cr8
003E7F2D  44 0F 22 C1                     mov cr8, rcx
003E7F31  44 39 35 E8 ED BD 00            cmp dword ptr [rip + 0xbdede8], r14d
003E7F38  74 0A                           je 0x1403e7f44
003E7F3A  8A D1                           mov dl, cl
003E7F3C  41 8A CD                        mov cl, r13b
003E7F3F  E8 B8 D7 10 00                  call 0x1404f56fc
003E7F44  E8 47 AD E5 FF                  call 0x140242c90
003E7F49  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
003E7F4E  48 8B C8                        mov rcx, rax
003E7F51  44 8B 8C 24 08 01 00 00         mov r9d, dword ptr [rsp + 0x108]
003E7F59  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003E7F5E  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
003E7F62  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
003E7F67  E8 94 CF EA FF                  call 0x140294f00
003E7F6C  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003E7F71  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
003E7F7B  EB 08                           jmp 0x1403e7f85
003E7F7D  44 8B BC 24 F0 00 00 00         mov r15d, dword ptr [rsp + 0xf0]
003E7F85  48 3B 5C 24 50                  cmp rbx, qword ptr [rsp + 0x50]
003E7F8A  0F 83 25 02 00 00               jae 0x1403e81b5
003E7F90  83 BC 24 F8 00 00 00 00         cmp dword ptr [rsp + 0xf8], 0
003E7F98  74 70                           je 0x1403e800a
003E7F9A  4D 85 F6                        test r14, r14
003E7F9D  74 3A                           je 0x1403e7fd9
003E7F9F  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
003E7FA6  0F 85 80 00 00 00               jne 0x1403e802c
003E7FAC  45 85 FF                        test r15d, r15d
003E7FAF  74 18                           je 0x1403e7fc9
003E7FB1  45 8B C7                        mov r8d, r15d
003E7FB4  49 8B D6                        mov rdx, r14
003E7FB7  E8 C4 00 F9 FF                  call 0x140378080
003E7FBC  83 A4 24 F0 00 00 00 00         and dword ptr [rsp + 0xf0], 0
003E7FC4  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E7FC9  E8 F2 9F F2 FF                  call 0x140311fc0
003E7FCE  49 8B D6                        mov rdx, r14
003E7FD1  48 8B CD                        mov rcx, rbp
003E7FD4  E8 E7 EE E2 FF                  call 0x140216ec0
003E7FD9  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003E7FE3  4C 8B F3                        mov r14, rbx
003E7FE6  49 C1 EE 09                     shr r14, 9
003E7FEA  4C 23 F0                        and r14, rax
003E7FED  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003E7FF7  48 8B C0                        mov rax, rax
003E7FFA  4C 03 F0                        add r14, rax
003E7FFD  48 8B CD                        mov rcx, rbp
003E8000  49 8B D6                        mov rdx, r14
003E8003  E8 88 68 E5 FF                  call 0x14023e890
003E8008  EB 0E                           jmp 0x1403e8018
003E800A  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
003E8011  75 19                           jne 0x1403e802c
003E8013  E8 A8 9F F2 FF                  call 0x140311fc0
003E8018  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003E801D  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
003E8027  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E802C  49 3B D4                        cmp rdx, r12
003E802F  74 52                           je 0x1403e8083
003E8031  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
003E8036  48 8B 18                        mov rbx, qword ptr [rax]
003E8039  4C 8B FB                        mov r15, rbx
003E803C  49 C1 EF 0C                     shr r15, 0xc
003E8040  4D 23 F8                        and r15, r8
003E8043  84 DB                           test bl, bl
003E8045  0F 89 1E 01 00 00               jns 0x1403e8169
003E804B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
003E8050  4C 39 39                        cmp qword ptr [rcx], r15
003E8053  0F 85 10 01 00 00               jne 0x1403e8169
003E8059  4C 8B CF                        mov r9, rdi
003E805C  4C 8B C0                        mov r8, rax
003E805F  33 D2                           xor edx, edx
003E8061  48 8B CD                        mov rcx, rbp
003E8064  E8 83 AF F3 FF                  call 0x140322fec
003E8069  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
003E806E  41 8B D4                        mov edx, r12d
003E8071  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E8076  E8 01 02 F9 FF                  call 0x14037827c
003E807B  48 83 44 24 48 08               add qword ptr [rsp + 0x48], 8
003E8081  EB 54                           jmp 0x1403e80d7
003E8083  48 8B 1B                        mov rbx, qword ptr [rbx]
003E8086  41 84 DC                        test r12b, bl
003E8089  0F 84 00 01 00 00               je 0x1403e818f
003E808F  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
003E8094  4C 8B FB                        mov r15, rbx
003E8097  48 8B 05 E2 87 C2 FF            mov rax, qword ptr [rip - 0x3d781e]
003E809E  44 01 A4 24 F0 00 00 00         add dword ptr [rsp + 0xf0], r12d
003E80A6  49 C1 EF 0C                     shr r15, 0xc
003E80AA  48 89 02                        mov qword ptr [rdx], rax
003E80AD  4D 23 F8                        and r15, r8
003E80B0  48 C1 E2 19                     shl rdx, 0x19
003E80B4  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003E80BE  48 8B C0                        mov rax, rax
003E80C1  48 C1 E0 19                     shl rax, 0x19
003E80C5  45 33 C9                        xor r9d, r9d
003E80C8  48 2B D0                        sub rdx, rax
003E80CB  4D 8B C4                        mov r8, r12
003E80CE  48 C1 FA 10                     sar rdx, 0x10
003E80D2  E8 99 B5 EA FF                  call 0x140293670
003E80D7  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003E80DC  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
003E80E6  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E80EB  48 8D 04 D5 00 00 00 00         lea rax, [rdx*8]
003E80F3  48 01 44 24 40                  add qword ptr [rsp + 0x40], rax
003E80F8  48 01 44 24 60                  add qword ptr [rsp + 0x60], rax
003E80FD  48 0F BA E3 09                  bt rbx, 9
003E8102  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003E8107  0F 82 70 FE FF FF               jb 0x1403e7f7d
003E810D  4C 3B 3D CC 5B A4 00            cmp r15, qword ptr [rip + 0xa45bcc]
003E8114  77 27                           ja 0x1403e813d
003E8116  4B 8D 04 7F                     lea rax, [r15 + r15*2]
003E811A  48 03 C0                        add rax, rax
003E811D  48 B9 28 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000028
003E8127  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003E812B  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E8130  48 C1 E8 36                     shr rax, 0x36
003E8134  41 85 C4                        test r12d, eax
003E8137  0F 85 40 FE FF FF               jne 0x1403e7f7d
003E813D  4C 8B C2                        mov r8, rdx
003E8140  41 8B CC                        mov ecx, r12d
003E8143  49 8B D7                        mov rdx, r15
003E8146  E8 65 30 EC FF                  call 0x1402ab1b0
003E814B  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E8150  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
003E815A  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003E815F  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003E8164  E9 14 FE FF FF                  jmp 0x1403e7f7d
003E8169  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
003E8171  BA 0E 01 00 00                  mov edx, 0x10e
003E8176  44 8B 8C 24 00 01 00 00         mov r9d, dword ptr [rsp + 0x100]
003E817E  4C 8B C6                        mov r8, rsi
003E8181  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003E8186  8D 4A CC                        lea ecx, [rdx - 0x34]
003E8189  E8 D2 54 11 00                  call 0x1404fd660
003E818E  CC                              int3
003E818F  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
003E8197  BA 0B 01 00 00                  mov edx, 0x10b
003E819C  44 8B 8C 24 00 01 00 00         mov r9d, dword ptr [rsp + 0x100]
003E81A4  4C 8B C6                        mov r8, rsi
003E81A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003E81AC  8D 4A CF                        lea ecx, [rdx - 0x31]
003E81AF  E8 AC 54 11 00                  call 0x1404fd660
003E81B4  CC                              int3
003E81B5  E8 06 9E F2 FF                  call 0x140311fc0
003E81BA  E8 B1 BA F2 FF                  call 0x140313c70
003E81BF  83 BC 24 F8 00 00 00 00         cmp dword ptr [rsp + 0xf8], 0
003E81C7  74 2D                           je 0x1403e81f6
003E81C9  4D 85 F6                        test r14, r14
003E81CC  74 1B                           je 0x1403e81e9
003E81CE  45 85 FF                        test r15d, r15d
003E81D1  74 0B                           je 0x1403e81de
003E81D3  45 8B C7                        mov r8d, r15d
003E81D6  49 8B D6                        mov rdx, r14
003E81D9  E8 A2 FE F8 FF                  call 0x140378080
003E81DE  49 8B D6                        mov rdx, r14
003E81E1  48 8B CD                        mov rcx, rbp
003E81E4  E8 D7 EC E2 FF                  call 0x140216ec0
003E81E9  41 8A D5                        mov dl, r13b
003E81EC  48 8B CD                        mov rcx, rbp
003E81EF  E8 9C 54 E9 FF                  call 0x14027d690
003E81F4  EB 23                           jmp 0x1403e8219
003E81F6  41 80 FD 11                     cmp r13b, 0x11
003E81FA  74 1D                           je 0x1403e8219
003E81FC  83 3D 1D EB BD 00 00            cmp dword ptr [rip + 0xbdeb1d], 0
003E8203  74 0C                           je 0x1403e8211
003E8205  44 0F 20 C1                     mov rcx, cr8
003E8209  41 8A D5                        mov dl, r13b
003E820C  E8 87 D4 10 00                  call 0x1404f5698
003E8211  41 0F B6 C5                     movzx eax, r13b
003E8215  44 0F 22 C0                     mov cr8, rax
003E8219  4C 39 64 24 38                  cmp qword ptr [rsp + 0x38], r12
003E821E  0F 84 22 02 00 00               je 0x1403e8446
003E8224  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
003E8229  48 8D 0D 78 DD A4 00            lea rcx, [rip + 0xa4dd78]
003E8230  41 80 FE 02                     cmp r14b, 2
003E8234  75 09                           jne 0x1403e823f
003E8236  B3 11                           mov bl, 0x11
003E8238  E8 43 0C E6 FF                  call 0x140248e80
003E823D  EB 07                           jmp 0x1403e8246
003E823F  E8 4C 04 E6 FF                  call 0x140248690
003E8244  8A D8                           mov bl, al
003E8246  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
003E824E  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
003E8253  48 C1 EA 09                     shr rdx, 9
003E8257  48 8D 0D 5A DD A4 00            lea rcx, [rip + 0xa4dd5a]
003E825E  E8 BD 11 0C 00                  call 0x1404a9420
003E8263  8A D3                           mov dl, bl
003E8265  48 8D 0D 3C DD A4 00            lea rcx, [rip + 0xa4dd3c]
003E826C  E8 4F 00 E6 FF                  call 0x1402482c0
003E8271  48 C1 EE 12                     shr rsi, 0x12
003E8275  81 E6 F8 FF FF 3F               and esi, 0x3ffffff8
003E827B  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
003E8285  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
003E828A  48 03 F0                        add rsi, rax
003E828D  48 C1 EB 09                     shr rbx, 9
003E8291  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003E829B  48 23 D8                        and rbx, rax
003E829E  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
003E82A8  49 8B C5                        mov rax, r13
003E82AB  48 03 D8                        add rbx, rax
003E82AE  33 FF                           xor edi, edi
003E82B0  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003E82B5  48 85 ED                        test rbp, rbp
003E82B8  74 2C                           je 0x1403e82e6
003E82BA  48 8B CD                        mov rcx, rbp
003E82BD  41 80 FE 02                     cmp r14b, 2
003E82C1  75 12                           jne 0x1403e82d5
003E82C3  41 B7 11                        mov r15b, 0x11
003E82C6  44 88 BC 24 10 01 00 00         mov byte ptr [rsp + 0x110], r15b
003E82CE  E8 A1 12 E5 FF                  call 0x140239574
003E82D3  EB 1F                           jmp 0x1403e82f4
003E82D5  E8 16 49 E9 FF                  call 0x14027cbf0
003E82DA  44 8A F8                        mov r15b, al
003E82DD  88 84 24 10 01 00 00            mov byte ptr [rsp + 0x110], al
003E82E4  EB 0E                           jmp 0x1403e82f4
003E82E6  41 B7 11                        mov r15b, 0x11
003E82E9  45 33 E4                        xor r12d, r12d
003E82EC  44 88 BC 24 10 01 00 00         mov byte ptr [rsp + 0x110], r15b
003E82F4  48 3B F3                        cmp rsi, rbx
003E82F7  0F 83 29 01 00 00               jae 0x1403e8426
003E82FD  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
003E8302  45 85 E4                        test r12d, r12d
003E8305  74 3E                           je 0x1403e8345
003E8307  48 85 FF                        test rdi, rdi
003E830A  74 14                           je 0x1403e8320
003E830C  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
003E8313  75 30                           jne 0x1403e8345
003E8315  48 8B D7                        mov rdx, rdi
003E8318  48 8B CD                        mov rcx, rbp
003E831B  E8 A0 EB E2 FF                  call 0x140216ec0
003E8320  48 8B FE                        mov rdi, rsi
003E8323  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003E832D  48 C1 EF 09                     shr rdi, 9
003E8331  48 23 F8                        and rdi, rax
003E8334  49 8B C5                        mov rax, r13
003E8337  48 03 F8                        add rdi, rax
003E833A  48 8B CD                        mov rcx, rbp
003E833D  48 8B D7                        mov rdx, rdi
003E8340  E8 4B 65 E5 FF                  call 0x14023e890
003E8345  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
003E834A  E8 F1 D8 F7 FF                  call 0x140365c40
003E834F  4C 8B F0                        mov r14, rax
003E8352  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003E835C  49 8B D6                        mov rdx, r14
003E835F  41 B8 06 00 00 90               mov r8d, 0x90000006
003E8365  48 2B D0                        sub rdx, rax
003E8368  48 8B CE                        mov rcx, rsi
003E836B  48 C1 FA 04                     sar rdx, 4
003E836F  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
003E8379  48 0F AF D0                     imul rdx, rax
003E837D  E8 0E D2 ED FF                  call 0x1402c5590
003E8382  48 8B D8                        mov rbx, rax
003E8385  45 85 E4                        test r12d, r12d
003E8388  0F 85 CD 00 00 00               jne 0x1403e845b
003E838E  41 80 FF 02                     cmp r15b, 2
003E8392  0F 84 C3 00 00 00               je 0x1403e845b
003E8398  49 8B CE                        mov rcx, r14
003E839B  E8 A0 1F F3 FF                  call 0x14031a340
003E83A0  44 8A E8                        mov r13b, al
003E83A3  48 8B CE                        mov rcx, rsi
003E83A6  49 89 76 08                     mov qword ptr [r14 + 8], rsi
003E83AA  E8 41 E4 F5 FF                  call 0x1403467f0
003E83AF  48 8B D0                        mov rdx, rax
003E83B2  49 8B CE                        mov rcx, r14
003E83B5  E8 06 BC F7 FF                  call 0x140363fc0
003E83BA  41 8A D5                        mov dl, r13b
003E83BD  49 C7 06 00 00 00 00            mov qword ptr [r14], 0
003E83C4  49 8B CE                        mov rcx, r14
003E83C7  E8 14 20 F3 FF                  call 0x14031a3e0
003E83CC  48 0F BA 25 B3 E6 BD 00 24      bt qword ptr [rip + 0xbde6b3], 0x24
003E83D5  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
003E83DF  73 2B                           jae 0x1403e840c
003E83E1  F6 C3 20                        test bl, 0x20
003E83E4  75 26                           jne 0x1403e840c
003E83E6  49 8B C5                        mov rax, r13
003E83E9  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
003E83F3  48 03 C1                        add rax, rcx
003E83F6  48 3B F0                        cmp rsi, rax
003E83F9  72 11                           jb 0x1403e840c
003E83FB  41 B8 80 00 00 00               mov r8d, 0x80
003E8401  48 8B D3                        mov rdx, rbx
003E8404  48 8B CE                        mov rcx, rsi
003E8407  E8 74 A9 EA FF                  call 0x140292d80
003E840C  48 89 1E                        mov qword ptr [rsi], rbx
003E840F  48 83 C6 08                     add rsi, 8
003E8413  48 3B 74 24 50                  cmp rsi, qword ptr [rsp + 0x50]
003E8418  0F 82 E4 FE FF FF               jb 0x1403e8302
003E841E  44 8A BC 24 10 01 00 00         mov r15b, byte ptr [rsp + 0x110]
003E8426  45 85 E4                        test r12d, r12d
003E8429  74 1B                           je 0x1403e8446
003E842B  48 85 FF                        test rdi, rdi
003E842E  74 0B                           je 0x1403e843b
003E8430  48 8B D7                        mov rdx, rdi
003E8433  48 8B CD                        mov rcx, rbp
003E8436  E8 85 EA E2 FF                  call 0x140216ec0
003E843B  41 8A D7                        mov dl, r15b
003E843E  48 8B CD                        mov rcx, rbp
003E8441  E8 4A 52 E9 FF                  call 0x14027d690
003E8446  48 81 C4 A8 00 00 00            add rsp, 0xa8
003E844D  41 5F                           pop r15
003E844F  41 5E                           pop r14
003E8451  41 5D                           pop r13
003E8453  41 5C                           pop r12
003E8455  5F                              pop rdi
003E8456  5E                              pop rsi
003E8457  5D                              pop rbp
003E8458  5B                              pop rbx
003E8459  C3                              ret
003E845A  CC                              int3
003E845B  83 64 24 58 00                  and dword ptr [rsp + 0x58], 0
003E8460  41 B5 11                        mov r13b, 0x11
003E8463  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
003E846A  0F 83 33 FF FF FF               jae 0x1403e83a3
003E8470  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
003E8475  E8 86 38 01 00                  call 0x1403fbd00
003E847A  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
003E847E  48 85 C0                        test rax, rax
003E8481  78 ED                           js 0x1403e8470
003E8483  EB DE                           jmp 0x1403e8463
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnmapMdlCommon(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned int v_stack_p58;
    unsigned int v_stack_p8;

    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (168);
    result = 0;
    v_stack_m70 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    v_stack_m88 = a4 + 48;
    result = -(a2);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (8));
    v_stack_p20 = (unsigned int)(result);
    if (a2 == 0) { a2 = v_rip + 10814439; }
    v_rbx = (a1) >> (9);
    v_rbx = (v_rbx) & (a3);
    v_stack_m78 = a2;
    v_rbx = (v_rbx) + (a2);
    v_stack_mA8 = v_rbx;
    a1 = (v_rbx) >> (9);
    a1 = (a1) & (a3);
    v_stack_m98 = v_rbx + a5 * 8;
    a1 = (a1) + (a2);
    v_stack_mA0 = a1;
    if (!sign_flag) goto loc_003E7EC5;
    v_stack_mB0 = 512;
    result = MiMakeDemandZeroPte(1 + 15, a2, a3, a4);
    goto loc_003E7ECC;
loc_003E7EC5:
    v_stack_mB0 = 1;
    v_rdi = 0;
loc_003E7ECC:
    v_r15 = 0;
    v_stack_p8 = 0;
    v_r14 = 0;
    v_stack_m80 = v_cr8;
    if (a2 == 0) goto loc_003E7F0F;
    v_stack_p10 = 1;
    if (((unsigned __int8)(v_cr8)) != ((unsigned __int8)(v_r15 + 2))) goto loc_003E7F05;
    result = MiLockWorkingSetSharedAtDpc(a2, a2, a3, a4);
    goto loc_003E7F44;
loc_003E7F05:
    result = MiLockWorkingSetShared(a2, a2, a3, a4);
    goto loc_003E7F44;
loc_003E7F0F:
    if (((unsigned __int8)(v_cr8)) != 2) goto loc_003E7F29;
    goto loc_003E7F44;
loc_003E7F29:
    result = v_cr8;
    if ((*(unsigned int *)(v_rip + 12447208)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = MiGetProcessorFlushList(a1, a2, a3, a4);
    v_stack_mB8 = result;
    v_stack_mC8 = 1;
    result = MiInitializeTbFlushList(result, v_stack_m78, (unsigned int)(*(unsigned int *)(result + 12)), (unsigned int)(v_stack_p20));
    goto loc_003E7F85;
loc_003E7F7D:
loc_003E7F85:
    if (v_rbx >= v_stack_m98) goto loc_003E81B5;
    if (v_stack_p10 == 0) goto loc_003E800A;
    if (0 == 0) goto loc_003E7FD9;
    if (((v_rbx) & (0xFFFULL)) != 0) goto loc_003E802C;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) {
        a3 = (unsigned int)((unsigned int)(v_stack_p8));
        a2 = 0;
        result = MiDecreaseUsedPtes(result, a2, a3, (unsigned int)(v_stack_p20));
        a1 = v_stack_mB8;
    }
    result = MiFlushTbList(a1, a2, a3, (unsigned int)(v_stack_p20));
    result = MiUnlockPageTable(a2, 0, a3, (unsigned int)(v_stack_p20));
loc_003E7FD9:
    v_r14 = (v_rbx) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (result);
    result = MiLockNestedPageTable(a2, v_r14, a3, (unsigned int)(v_stack_p20));
    goto loc_003E8018;
loc_003E800A:
    if (((v_rbx) & (0xFFFULL)) != 0) goto loc_003E802C;
    result = MiFlushTbList(a2, v_r14, a3, (unsigned int)(v_stack_p20));
loc_003E8018:
loc_003E802C:
    if (v_stack_mB0 == 1) goto loc_003E8083;
    v_r15 = (*(unsigned __int64 *)(v_stack_mA0)) >> (12);
    v_r15 = (v_r15) & (a3);
    if (!sign_flag) goto loc_003E8169;
    if ((*(unsigned __int64 *)(v_stack_m88)) != v_r15) goto loc_003E8169;
    a2 = 0;
    result = MiRewritePteWithLockBit(0, a2, v_stack_mA0, 0);
    result = MiInsertLargeTbFlushEntry(v_stack_mB8, 1, v_stack_mA0, 0);
    goto loc_003E80D7;
loc_003E8083:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0))))) == 0) goto loc_003E818F;
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0))) >> (12);
    *(unsigned __int64 *)(v_stack_mA8) = *(unsigned __int64 *)(v_rip - 4028446);
    v_r15 = (v_r15) & (v_stack_mA0);
    a2 = (v_stack_mA8) << (25);
    result = (*(unsigned __int64 *)(v_rip - 4028446)) << (25);
    a4 = 0;
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_mB8, a2, 1, a4);
loc_003E80D7:
    if (condition_is_below) goto loc_003E7F7D;
    if (v_r15 > (*(unsigned __int64 *)(v_rip + 10771404))) goto loc_003E813D;
    result = (v_r15 + v_r15 * 2) + (v_r15 + v_r15 * 2);
    result = (*(unsigned __int64 *)(v_stack_mB8 + result * 8)) >> (54);
    if (((1) & ((unsigned int)(result))) != 0) goto loc_003E7F7D;
loc_003E813D:
    result = MiDereferenceIoPages(1, v_r15, v_stack_mB0, a4);
    goto loc_003E7F7D;
loc_003E8169:
    v_stack_mC8 = a5;
    result = KeBugCheckEx(270 - 52, 270, a1, (unsigned int)(v_stack_p18));
loc_003E818F:
    v_stack_mC8 = a5;
    result = KeBugCheckEx(267 - 49, 267, a1, (unsigned int)(v_stack_p18));
loc_003E81B5:
    result = MiFlushTbList(267 - 49, 267, a1, (unsigned int)(v_stack_p18));
    result = MiReleaseProcessorFlushList(267 - 49, 267, a1, (unsigned int)(v_stack_p18));
    if (v_stack_p10 == 0) goto loc_003E81F6;
    if (v_r14 == 0) goto loc_003E81E9;
    if ((unsigned int)(v_r15) != 0) {
        a3 = (unsigned int)(v_r15);
        a2 = v_r14;
        result = MiDecreaseUsedPtes(267 - 49, a2, a3, (unsigned int)(v_stack_p18));
    }
    result = MiUnlockPageTable(a2, v_r14, a3, (unsigned int)(v_stack_p18));
loc_003E81E9:
    result = MiUnlockWorkingSetShared(a2, (unsigned __int8)(v_cr8), a3, (unsigned int)(v_stack_p18));
    goto loc_003E8219;
loc_003E81F6:
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_003E8219;
    if ((*(unsigned int *)(v_rip + 12446493)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, (unsigned int)(v_stack_p18));
    }
loc_003E8219:
    if (v_stack_mB0 == 1) goto loc_003E8446;
    if (((unsigned __int8)(v_stack_m80)) != 2) goto loc_003E823F;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10804600, a2, a3, (unsigned int)(v_stack_p18));
    goto loc_003E8246;
loc_003E823F:
    result = ExAcquireSpinLockExclusive(v_rip + 10804600, a2, a3, (unsigned int)(v_stack_p18));
loc_003E8246:
    a2 = (a5) >> (9);
    result = MiSplitPageChain(v_rip + 10804570, a2, v_stack_m70, (unsigned int)(v_stack_p18));
    result = MiReleaseSpinLockExclusive(v_rip + 10804540, (unsigned __int8)((unsigned __int8)(result)), v_stack_m70, (unsigned int)(v_stack_p18));
    v_rsi = (a1) >> (18);
    v_rsi = (unsigned int)((v_rsi) & (0x3FFFFFF8ULL));
    v_rsi = (v_rsi) + (result);
    v_rbx = (v_stack_m98) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (v_cr8);
    v_rdi = 0;
    v_stack_m98 = v_rbx;
    if (a2 == 0) goto loc_003E82E6;
    if (((unsigned __int8)(v_stack_m80)) != 2) goto loc_003E82D5;
    v_stack_p28 = 17;
    result = MiLockWorkingSetSharedAtDpc(a2, (unsigned __int8)((unsigned __int8)(result)), v_stack_m70, (unsigned int)(v_stack_p18));
    goto loc_003E82F4;
loc_003E82D5:
    result = MiLockWorkingSetShared(a2, (unsigned __int8)((unsigned __int8)(result)), v_stack_m70, (unsigned int)(v_stack_p18));
    v_stack_p28 = (unsigned __int8)(result);
    goto loc_003E82F4;
loc_003E82E6:
    v_r12 = 0;
    v_stack_p28 = 17;
loc_003E82F4:
    if (v_rsi >= v_rbx) goto loc_003E8426;
loc_003E8302:
    if (0 == 0) goto loc_003E8345;
    if (0 == 0) goto loc_003E8320;
    if (((v_rsi) & (0xFFFULL)) != 0) goto loc_003E8345;
    result = MiUnlockPageTable(a2, 0, v_stack_m70, (unsigned int)(v_stack_p18));
loc_003E8320:
    v_rdi = (v_rsi) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) + (v_cr8);
    result = MiLockNestedPageTable(a2, v_rdi, v_stack_m70, (unsigned int)(v_stack_p18));
loc_003E8345:
    result = MiUnlinkPageChainHead(v_stack_m70, v_rdi, v_stack_m70, (unsigned int)(v_stack_p18));
    a2 = (result) - (result);
    a2 = (a2) >> (4);
    a2 = (a2) * (result);
    result = MiMakeValidPte(v_rsi, a2, (unsigned int)(0x90000006ULL), (unsigned int)(v_stack_p18));
    if (0 != 0) goto loc_003E845B;
    if (((unsigned __int8)(v_stack_m80)) == 2) goto loc_003E845B;
    result = MiLockPageInline(result, a2, (unsigned int)(0x90000006ULL), (unsigned int)(v_stack_p18));
loc_003E83A3:
    *(unsigned __int64 *)(result + 8) = v_rsi;
    result = MiGetContainingPageTable(v_rsi, a2, (unsigned int)(0x90000006ULL), (unsigned int)(v_stack_p18));
    result = MiSetPfnContainingFrame(result, result, (unsigned int)(0x90000006ULL), (unsigned int)(v_stack_p18));
    *(unsigned __int64 *)(result) = 0;
    result = MiUnlockPage(result, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x90000006ULL), (unsigned int)(v_stack_p18));
    if (((unsigned __int8)(v_stack_m80)) >= 2) goto loc_003E840C;
    if ((((unsigned __int8)(result)) & (32)) != 0) goto loc_003E840C;
    result = ((unsigned __int8)(result)) + (result);
    if (v_rsi >= result) {
        a3 = 128;
        a2 = result;
        a1 = v_rsi;
        result = MiCheckLinearProtectedPteAccessedBit(a1, a2, a3, (unsigned int)(v_stack_p18));
    }
    *(unsigned __int64 *)(v_rsi) = result;
    v_rsi = (v_rsi) + (8);
    if (v_rsi < v_stack_m98) goto loc_003E8302;
loc_003E8426:
    if (0 == 0) goto loc_003E8446;
    if (v_rdi != 0) {
        a2 = v_rdi;
        a1 = a2;
        result = MiUnlockPageTable(a1, a2, a3, (unsigned int)(v_stack_p18));
    }
    result = MiUnlockWorkingSetShared(a2, a5, a3, (unsigned int)(v_stack_p18));
loc_003E8446:
    v_rsp = (v_rsp) + (168);
    return result;
loc_003E845B:
loc_003E8463:
    if (condition_is_above_or_equal) goto loc_003E83A3;
loc_003E8470:
    result = KeYieldProcessorEx(v_stack_p58, a5, a3, (unsigned int)(v_stack_p18));
    if (sign_flag) goto loc_003E8470;
    goto loc_003E8463;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnmapMdlCommon(int64_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4, uint8_t Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint32_t v_stack_p58;
    uint32_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (168);
    result = 0;
    v_stack_m70 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    v_stack_m88 = Arg4 + 48;
    result = -(Arg2);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (8));
    v_stack_p20 = (uint32_t)(result);
    if (Arg2 == 0) { Arg2 = v_rip + 10814439; }
    local_rbx = (Arg1) >> (9);
    local_rbx = (local_rbx) & (Arg3);
    v_stack_m78 = Arg2;
    local_rbx = (local_rbx) + (Arg2);
    v_stack_mA8 = local_rbx;
    Arg1 = (local_rbx) >> (9);
    Arg1 = (Arg1) & (Arg3);
    v_stack_m98 = local_rbx + Arg5 * 8;
    Arg1 = (Arg1) + (Arg2);
    v_stack_mA0 = Arg1;
    if (!sign_flag) goto loc_003E7EC5;
    v_stack_mB0 = 512;
    result = MiMakeDemandZeroPte(1 + 15, Arg2, Arg3, Arg4);
    goto loc_003E7ECC;
loc_003E7EC5:
    v_stack_mB0 = 1;
    local_rdi = 0;
loc_003E7ECC:
    local_r15 = 0;
    v_stack_p8 = 0;
    local_r14 = 0;
    v_stack_m80 = v_cr8;
    if (Arg2 == 0) goto loc_003E7F0F;
    v_stack_p10 = 1;
    if (((uint8_t)(v_cr8)) != ((uint8_t)(local_r15 + 2))) goto loc_003E7F05;
    result = MiLockWorkingSetSharedAtDpc(Arg2, Arg2, Arg3, Arg4);
    goto loc_003E7F44;
loc_003E7F05:
    result = MiLockWorkingSetShared(Arg2, Arg2, Arg3, Arg4);
    goto loc_003E7F44;
loc_003E7F0F:
    if (((uint8_t)(v_cr8)) != 2) goto loc_003E7F29;
    goto loc_003E7F44;
loc_003E7F29:
    result = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xBDEDE8)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiGetProcessorFlushList(Arg1, Arg2, Arg3, Arg4);
    v_stack_mB8 = result;
    v_stack_mC8 = 1;
    result = MiInitializeTbFlushList(result, v_stack_m78, (uint32_t)(*(uint32_t *)(result + 0xC)), (uint32_t)(v_stack_p20));
    goto loc_003E7F85;
loc_003E7F7D:
loc_003E7F85:
    if (local_rbx >= v_stack_m98) goto loc_003E81B5;
    if (v_stack_p10 == 0) goto loc_003E800A;
    if (0 == 0) goto loc_003E7FD9;
    if (((local_rbx) & (0xFFFULL)) != 0) goto loc_003E802C;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) {
        Arg3 = (uint32_t)((uint32_t)(v_stack_p8));
        Arg2 = 0;
        result = MiDecreaseUsedPtes(result, Arg2, Arg3, (uint32_t)(v_stack_p20));
        Arg1 = v_stack_mB8;
    }
    result = MiFlushTbList(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p20));
    result = MiUnlockPageTable(Arg2, 0, Arg3, (uint32_t)(v_stack_p20));
loc_003E7FD9:
    local_r14 = (local_rbx) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (result);
    result = MiLockNestedPageTable(Arg2, local_r14, Arg3, (uint32_t)(v_stack_p20));
    goto loc_003E8018;
loc_003E800A:
    if (((local_rbx) & (0xFFFULL)) != 0) goto loc_003E802C;
    result = MiFlushTbList(Arg2, local_r14, Arg3, (uint32_t)(v_stack_p20));
loc_003E8018:
loc_003E802C:
    if (v_stack_mB0 == 1) goto loc_003E8083;
    local_r15 = (*(uint64_t *)(v_stack_mA0)) >> (12);
    local_r15 = (local_r15) & (Arg3);
    if (!sign_flag) goto loc_003E8169;
    if ((*(uint64_t *)(v_stack_m88)) != local_r15) goto loc_003E8169;
    Arg2 = 0;
    result = MiRewritePteWithLockBit(0, Arg2, v_stack_mA0, 0);
    result = MiInsertLargeTbFlushEntry(v_stack_mB8, 1, v_stack_mA0, 0);
    goto loc_003E80D7;
loc_003E8083:
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0))))) == 0) goto loc_003E818F;
    local_r15 = (*(uint64_t *)(*(uint64_t *)(v_stack_mA0))) >> (12);
    *(uint64_t *)(v_stack_mA8) = *(uint64_t *)(v_rip - 0x3D781E);
    local_r15 = (local_r15) & (v_stack_mA0);
    Arg2 = (v_stack_mA8) << (25);
    result = (*(uint64_t *)(v_rip - 0x3D781E)) << (25);
    Arg4 = 0;
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_mB8, Arg2, 1, Arg4);
loc_003E80D7:
    if (condition_is_below) goto loc_003E7F7D;
    if (local_r15 > (*(uint64_t *)(v_rip + 0xA45BCC))) goto loc_003E813D;
    result = (local_r15 + local_r15 * 2) + (local_r15 + local_r15 * 2);
    result = (*(uint64_t *)(v_stack_mB8 + result * 8)) >> (54);
    if (((1) & ((uint32_t)(result))) != 0) goto loc_003E7F7D;
loc_003E813D:
    result = MiDereferenceIoPages(1, local_r15, v_stack_mB0, Arg4);
    goto loc_003E7F7D;
loc_003E8169:
    v_stack_mC8 = Arg5;
    result = KeBugCheckEx(270 - 52, 270, Arg1, (uint32_t)(v_stack_p18));
loc_003E818F:
    v_stack_mC8 = Arg5;
    result = KeBugCheckEx(267 - 49, 267, Arg1, (uint32_t)(v_stack_p18));
loc_003E81B5:
    result = MiFlushTbList(267 - 49, 267, Arg1, (uint32_t)(v_stack_p18));
    result = MiReleaseProcessorFlushList(267 - 49, 267, Arg1, (uint32_t)(v_stack_p18));
    if (v_stack_p10 == 0) goto loc_003E81F6;
    if (local_r14 == 0) goto loc_003E81E9;
    if ((uint32_t)(local_r15) != 0) {
        Arg3 = (uint32_t)(local_r15);
        Arg2 = local_r14;
        result = MiDecreaseUsedPtes(267 - 49, Arg2, Arg3, (uint32_t)(v_stack_p18));
    }
    result = MiUnlockPageTable(Arg2, local_r14, Arg3, (uint32_t)(v_stack_p18));
loc_003E81E9:
    result = MiUnlockWorkingSetShared(Arg2, (uint8_t)(v_cr8), Arg3, (uint32_t)(v_stack_p18));
    goto loc_003E8219;
loc_003E81F6:
    if (((uint8_t)(v_cr8)) == 17) goto loc_003E8219;
    if ((*(uint32_t *)(v_rip + 0xBDEB1D)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
    }
loc_003E8219:
    if (v_stack_mB0 == 1) goto loc_003E8446;
    if (((uint8_t)(v_stack_m80)) != 2) goto loc_003E823F;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10804600, Arg2, Arg3, (uint32_t)(v_stack_p18));
    goto loc_003E8246;
loc_003E823F:
    result = ExAcquireSpinLockExclusive(v_rip + 10804600, Arg2, Arg3, (uint32_t)(v_stack_p18));
loc_003E8246:
    Arg2 = (Arg5) >> (9);
    result = MiSplitPageChain(v_rip + 10804570, Arg2, v_stack_m70, (uint32_t)(v_stack_p18));
    result = MiReleaseSpinLockExclusive(v_rip + 10804540, (uint8_t)((uint8_t)(result)), v_stack_m70, (uint32_t)(v_stack_p18));
    local_rsi = (Arg1) >> (18);
    local_rsi = (uint32_t)((local_rsi) & (0x3FFFFFF8ULL));
    local_rsi = (local_rsi) + (result);
    local_rbx = (v_stack_m98) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (v_cr8);
    local_rdi = 0;
    v_stack_m98 = local_rbx;
    if (Arg2 == 0) goto loc_003E82E6;
    if (((uint8_t)(v_stack_m80)) != 2) goto loc_003E82D5;
    v_stack_p28 = 17;
    result = MiLockWorkingSetSharedAtDpc(Arg2, (uint8_t)((uint8_t)(result)), v_stack_m70, (uint32_t)(v_stack_p18));
    goto loc_003E82F4;
loc_003E82D5:
    result = MiLockWorkingSetShared(Arg2, (uint8_t)((uint8_t)(result)), v_stack_m70, (uint32_t)(v_stack_p18));
    v_stack_p28 = (uint8_t)(result);
    goto loc_003E82F4;
loc_003E82E6:
    local_r12 = 0;
    v_stack_p28 = 17;
loc_003E82F4:
    if (local_rsi >= local_rbx) goto loc_003E8426;
loc_003E8302:
    if (0 == 0) goto loc_003E8345;
    if (0 == 0) goto loc_003E8320;
    if (((local_rsi) & (0xFFFULL)) != 0) goto loc_003E8345;
    result = MiUnlockPageTable(Arg2, 0, v_stack_m70, (uint32_t)(v_stack_p18));
loc_003E8320:
    local_rdi = (local_rsi) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) + (v_cr8);
    result = MiLockNestedPageTable(Arg2, local_rdi, v_stack_m70, (uint32_t)(v_stack_p18));
loc_003E8345:
    result = MiUnlinkPageChainHead(v_stack_m70, local_rdi, v_stack_m70, (uint32_t)(v_stack_p18));
    Arg2 = (result) - (result);
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (result);
    result = MiMakeValidPte(local_rsi, Arg2, (uint32_t)(0x90000006ULL), (uint32_t)(v_stack_p18));
    if (0 != 0) goto loc_003E845B;
    if (((uint8_t)(v_stack_m80)) == 2) goto loc_003E845B;
    result = MiLockPageInline(result, Arg2, (uint32_t)(0x90000006ULL), (uint32_t)(v_stack_p18));
loc_003E83A3:
    *(uint64_t *)(result + 0x8) = local_rsi;
    result = MiGetContainingPageTable(local_rsi, Arg2, (uint32_t)(0x90000006ULL), (uint32_t)(v_stack_p18));
    result = MiSetPfnContainingFrame(result, result, (uint32_t)(0x90000006ULL), (uint32_t)(v_stack_p18));
    *(uint64_t *)(result) = 0;
    result = MiUnlockPage(result, (uint8_t)((uint8_t)(result)), (uint32_t)(0x90000006ULL), (uint32_t)(v_stack_p18));
    if (((uint8_t)(v_stack_m80)) >= 2) goto loc_003E840C;
    if ((((uint8_t)(result)) & (32)) != 0) goto loc_003E840C;
    result = ((uint8_t)(result)) + (result);
    if (local_rsi >= result) {
        Arg3 = 128;
        Arg2 = result;
        Arg1 = local_rsi;
        result = MiCheckLinearProtectedPteAccessedBit(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
    }
    *(uint64_t *)(local_rsi) = result;
    local_rsi = (local_rsi) + (8);
    if (local_rsi < v_stack_m98) goto loc_003E8302;
loc_003E8426:
    if (0 == 0) goto loc_003E8446;
    if (local_rdi != 0) {
        Arg2 = local_rdi;
        Arg1 = Arg2;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
    }
    result = MiUnlockWorkingSetShared(Arg2, Arg5, Arg3, (uint32_t)(v_stack_p18));
loc_003E8446:
    local_rsp = (local_rsp) + (168);
    return result;
loc_003E845B:
loc_003E8463:
    if (condition_is_above_or_equal) goto loc_003E83A3;
loc_003E8470:
    result = KeYieldProcessorEx(v_stack_p58, Arg5, Arg3, (uint32_t)(v_stack_p18));
    if (sign_flag) goto loc_003E8470;
    goto loc_003E8463;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E7DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
