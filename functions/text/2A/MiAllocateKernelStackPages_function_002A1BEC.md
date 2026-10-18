# MiAllocateKernelStackPages

- RVA: `0x002A1BEC`–`0x002A2287` (길이 `1,691` bytes)
- VA: `0x00000001402A1BEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00068554`
- 디코드: `407`개 명령, `1,691/1,691` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002A1C8E` → [MiAssignDefaultChannel](../31/MiAssignDefaultChannel_function_0031E5B0.md) (function, `0x0031E5B0`)
- `0x002A1CED` → [MiAcquireNonPagedResources](../28/MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x002A1D62` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x002A1DCA` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x002A1DF2` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x002A1E12` → [MiVaToFlushVm](../31/MiVaToFlushVm_function_0031AD84.md) (function, `0x0031AD84`)
- `0x002A1E28` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002A1ED5` → [MiInitializePfn](../33/MiInitializePfn_function_00331E60.md) (function, `0x00331E60`)
- `0x002A1EE1` → [MiMarkKernelStack](MiMarkKernelStack_function_002A2290.md) (function, `0x002A2290`)
- `0x002A1F3A` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002A1FCD` → [MiDeleteKernelStackPages](../2D/MiDeleteKernelStackPages_function_002D9938.md) (function, `0x002D9938`)
- `0x002A1FEA` → [MiWaitForFreePage](MiWaitForFreePage_function_002A3324.md) (function, `0x002A3324`)
- `0x002A1FFB` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002A200B` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x002A2026` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x002A2034` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002A2063` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x002A207E` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x002A208A` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002A20A6` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)
- `0x002A20E8` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002A20FA` → [MiFinalizePageAttribute](../33/MiFinalizePageAttribute_function_00332E30.md) (function, `0x00332E30`)
- `0x002A2115` → [MiInitializeMdlSinglePage](../2C/MiInitializeMdlSinglePage_function_002C939C.md) (function, `0x002C939C`)
- `0x002A2126` → [MiSetPfnIdentity](MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x002A2162` → [MiGetSlabPage](../37/MiGetSlabPage_function_00376FBC.md) (function, `0x00376FBC`)
- `0x002A218C` → [MiIsPfnFromChargedSlabAllocation](MiIsPfnFromChargedSlabAllocation_function_002A2968.md) (function, `0x002A2968`)
- `0x002A2202` → [VslAllocateKernelShadowStack](../../page/A5/VslAllocateKernelShadowStack_function_00A54174.md) (function, `0x00A54174`)
- `0x002A223F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002A224E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002A225B` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x002A2270` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x002A227D` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)

### Direct callers
- [MmGrowKernelStackEx](MmGrowKernelStackEx_function_002A04E0.md) at `0x002A0640`
- [sub_0033827F](../33/Unknown_function_0033827F.md) at `0x0033839D`

### Static image references
- `0x002A1C2C` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002A1DAE` → RVA `0x00E38D00` (`.data`; read)
- `0x002A1DBD` → RVA `0x00E376E8` (`.data`; read/write)
- `0x002A1EFC` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002A1F64` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002A20FF` → RVA `0x00010880` (`.rdata`; read)
- `0x002A2231` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002A2202` → [VslAllocateKernelShadowStack](../../page/A5/VslAllocateKernelShadowStack_function_00A54174.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002A2218` → [sub_006DAE30](../6D/Unknown_function_006DAE30.md) (`tail-transfer`)
  - `0x002A2226` → [sub_006DAE30](../6D/Unknown_function_006DAE30.md) (`tail-transfer`)
  - `0x002A222C` → [sub_006DAE30 + 0xB](../6D/Unknown_function_006DAE30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002A1BEC  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002A1BF1  55                              push rbp
002A1BF2  53                              push rbx
002A1BF3  56                              push rsi
002A1BF4  57                              push rdi
002A1BF5  41 54                           push r12
002A1BF7  41 55                           push r13
002A1BF9  41 56                           push r14
002A1BFB  41 57                           push r15
002A1BFD  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
002A1C02  48 81 EC 88 00 00 00            sub rsp, 0x88
002A1C09  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
002A1C0D  45 33 ED                        xor r13d, r13d
002A1C10  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
002A1C14  48 8B F1                        mov rsi, rcx
002A1C17  44 89 6D 0B                     mov dword ptr [rbp + 0xb], r13d
002A1C1B  4C 89 69 40                     mov qword ptr [rcx + 0x40], r13
002A1C1F  48 85 FF                        test rdi, rdi
002A1C22  0F 84 20 03 00 00               je 0x1402a1f48
002A1C28  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
002A1C2C  48 8D 15 CD E3 D5 FF            lea rdx, [rip - 0x2a1c33]
002A1C33  4C 8B 79 08                     mov r15, qword ptr [rcx + 8]
002A1C37  45 8B E5                        mov r12d, r13d
002A1C3A  44 8B 49 30                     mov r9d, dword ptr [rcx + 0x30]
002A1C3E  48 8B 19                        mov rbx, qword ptr [rcx]
002A1C41  44 8A 71 24                     mov r14b, byte ptr [rcx + 0x24]
002A1C45  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
002A1C49  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
002A1C4D  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
002A1C51  49 8D 04 FF                     lea rax, [r15 + rdi*8]
002A1C55  48 89 45 F7                     mov qword ptr [rbp - 9], rax
002A1C59  41 8D 41 01                     lea eax, [r9 + 1]
002A1C5D  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
002A1C61  44 88 75 6F                     mov byte ptr [rbp + 0x6f], r14b
002A1C65  85 C0                           test eax, eax
002A1C67  0F 85 27 04 00 00               jne 0x1402a2094
002A1C6D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002A1C76  8B 88 4C 02 00 00               mov ecx, dword ptr [rax + 0x24c]
002A1C7C  4C 8B 9C CA 40 8C FC 00         mov r11, qword ptr [rdx + rcx*8 + 0xfc8c40]
002A1C84  45 8B 8B 54 87 00 00            mov r9d, dword ptr [r11 + 0x8754]
002A1C8B  41 8B C9                        mov ecx, r9d
002A1C8E  E8 1D C9 07 00                  call 0x14031e5b0
002A1C93  41 83 E1 3F                     and r9d, 0x3f
002A1C97  33 D2                           xor edx, edx
002A1C99  41 81 C9 80 03 00 00            or r9d, 0x380
002A1CA0  89 55 7F                        mov dword ptr [rbp + 0x7f], edx
002A1CA3  44 8A D0                        mov r10b, al
002A1CA6  89 55 77                        mov dword ptr [rbp + 0x77], edx
002A1CA9  41 83 E2 01                     and r10d, 1
002A1CAD  49 8D 83 50 87 00 00            lea rax, [r11 + 0x8750]
002A1CB4  45 03 C9                        add r9d, r9d
002A1CB7  48 89 45 FF                     mov qword ptr [rbp - 1], rax
002A1CBB  45 0B D1                        or r10d, r9d
002A1CBE  41 C1 E2 08                     shl r10d, 8
002A1CC2  44 89 55 07                     mov dword ptr [rbp + 7], r10d
002A1CC6  48 39 55 DF                     cmp qword ptr [rbp - 0x21], rdx
002A1CCA  0F 85 D4 04 00 00               jne 0x1402a21a4
002A1CD0  44 8B 4E 20                     mov r9d, dword ptr [rsi + 0x20]
002A1CD4  8B C2                           mov eax, edx
002A1CD6  41 80 FE 02                     cmp r14b, 2
002A1CDA  48 8B D7                        mov rdx, rdi
002A1CDD  48 8B CB                        mov rcx, rbx
002A1CE0  0F 94 C0                        sete al
002A1CE3  41 83 E1 02                     and r9d, 2
002A1CE7  45 33 C0                        xor r8d, r8d
002A1CEA  89 45 C7                        mov dword ptr [rbp - 0x39], eax
002A1CED  E8 6E 4F FE FF                  call 0x140286c60
002A1CF2  45 33 D2                        xor r10d, r10d
002A1CF5  85 C0                           test eax, eax
002A1CF7  0F 88 D5 02 00 00               js 0x1402a1fd2
002A1CFD  45 8B F2                        mov r14d, r10d
002A1D00  41 8B C2                        mov eax, r10d
002A1D03  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
002A1D07  48 3B C7                        cmp rax, rdi
002A1D0A  0F 83 91 00 00 00               jae 0x1402a1da1
002A1D10  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
002A1D14  41 B8 01 00 00 00               mov r8d, 1
002A1D1A  F0 44 0F C1 00                  lock xadd dword ptr [rax], r8d
002A1D1F  4C 8B 4D 07                     mov r9, qword ptr [rbp + 7]
002A1D23  41 8B C0                        mov eax, r8d
002A1D26  49 8B C9                        mov rcx, r9
002A1D29  4C 8D 05 D0 E2 D5 FF            lea r8, [rip - 0x2a1d30]
002A1D30  48 C1 E9 10                     shr rcx, 0x10
002A1D34  33 D2                           xor edx, edx
002A1D36  83 E1 03                        and ecx, 3
002A1D39  41 81 E1 00 FF FF FF            and r9d, 0xffffff00
002A1D40  41 F7 B4 88 C0 DC E2 00         div dword ptr [r8 + rcx*4 + 0xe2dcc0]
002A1D48  0F B6 DA                        movzx ebx, dl
002A1D4B  41 0B D9                        or ebx, r9d
002A1D4E  44 39 55 77                     cmp dword ptr [rbp + 0x77], r10d
002A1D52  0F 85 E4 03 00 00               jne 0x1402a213c
002A1D58  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
002A1D5C  8B D3                           mov edx, ebx
002A1D5E  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002A1D62  E8 59 67 FE FF                  call 0x1402884c0
002A1D67  4C 8B C8                        mov r9, rax
002A1D6A  48 83 F8 FF                     cmp rax, -1
002A1D6E  0F 84 65 02 00 00               je 0x1402a1fd9
002A1D74  45 33 D2                        xor r10d, r10d
002A1D77  4B 8D 0C 49                     lea rcx, [r9 + r9*2]
002A1D7B  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002A1D85  48 C1 E1 04                     shl rcx, 4
002A1D89  48 8B C0                        mov rax, rax
002A1D8C  48 03 C8                        add rcx, rax
002A1D8F  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
002A1D93  48 FF C0                        inc rax
002A1D96  4C 89 21                        mov qword ptr [rcx], r12
002A1D99  4C 8B E1                        mov r12, rcx
002A1D9C  E9 62 FF FF FF                  jmp 0x1402a1d03
002A1DA1  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
002A1DA5  4D 85 F6                        test r14, r14
002A1DA8  0F 85 C9 04 00 00               jne 0x1402a2277
002A1DAE  48 8D 05 4B 6F B9 00            lea rax, [rip + 0xb96f4b]
002A1DB5  48 3B D8                        cmp rbx, rax
002A1DB8  75 0B                           jne 0x1402a1dc5
002A1DBA  49 2B FE                        sub rdi, r14
002A1DBD  F0 48 01 3D 23 59 B9 00         lock add qword ptr [rip + 0xb95923], rdi
002A1DC5  B9 04 00 00 00                  mov ecx, 4
002A1DCA  E8 31 5C 09 00                  call 0x140337a00
002A1DCF  48 8B 5D DF                     mov rbx, qword ptr [rbp - 0x21]
002A1DD3  48 8B F8                        mov rdi, rax
002A1DD6  48 8B C3                        mov rax, rbx
002A1DD9  49 8B CF                        mov rcx, r15
002A1DDC  48 F7 D8                        neg rax
002A1DDF  45 1B C0                        sbb r8d, r8d
002A1DE2  33 D2                           xor edx, edx
002A1DE4  41 81 E0 FD FF FF 7F            and r8d, 0x7ffffffd
002A1DEB  41 81 C0 04 00 00 A0            add r8d, 0xa0000004
002A1DF2  E8 99 37 02 00                  call 0x1402c5590
002A1DF7  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
002A1DFB  48 85 DB                        test rbx, rbx
002A1DFE  0F 85 F3 01 00 00               jne 0x1402a1ff7
002A1E04  48 83 65 77 00                  and qword ptr [rbp + 0x77], 0
002A1E09  49 8B CF                        mov rcx, r15
002A1E0C  45 33 ED                        xor r13d, r13d
002A1E0F  45 33 F6                        xor r14d, r14d
002A1E12  E8 6D 8F 07 00                  call 0x14031ad84
002A1E17  80 7D 6F 02                     cmp byte ptr [rbp + 0x6f], 2
002A1E1B  48 8B C8                        mov rcx, rax
002A1E1E  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
002A1E22  0F 84 7A 02 00 00               je 0x1402a20a2
002A1E28  E8 C3 AD FD FF                  call 0x14027cbf0
002A1E2D  88 45 6F                        mov byte ptr [rbp + 0x6f], al
002A1E30  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
002A1E34  49 8B DC                        mov rbx, r12
002A1E37  4D 85 E4                        test r12, r12
002A1E3A  74 04                           je 0x1402a1e40
002A1E3C  4D 8B 24 24                     mov r12, qword ptr [r12]
002A1E40  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002A1E4A  48 8B C0                        mov rax, rax
002A1E4D  48 8B CB                        mov rcx, rbx
002A1E50  48 BA FF 0F 00 00 00 00 F0 FF   movabs rdx, 0xfff0000000000fff
002A1E5A  48 2B C8                        sub rcx, rax
002A1E5D  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002A1E67  48 C1 F9 04                     sar rcx, 4
002A1E6B  48 0F AF C8                     imul rcx, rax
002A1E6F  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002A1E79  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
002A1E7D  48 23 C8                        and rcx, rax
002A1E80  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
002A1E84  48 23 C2                        and rax, rdx
002A1E87  48 C1 E1 0C                     shl rcx, 0xc
002A1E8B  48 0B C8                        or rcx, rax
002A1E8E  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
002A1E92  4D 85 F6                        test r14, r14
002A1E95  0F 84 9E 01 00 00               je 0x1402a2039
002A1E9B  49 F7 C7 FF 0F 00 00            test r15, 0xfff
002A1EA2  0F 84 6D 01 00 00               je 0x1402a2015
002A1EA8  33 F6                           xor esi, esi
002A1EAA  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
002A1EB1  0F 82 AB 00 00 00               jb 0x1402a1f62
002A1EB7  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
002A1EBB  48 8B CB                        mov rcx, rbx
002A1EBE  48 85 F6                        test rsi, rsi
002A1EC1  0F 85 2B 02 00 00               jne 0x1402a20f2
002A1EC7  44 8D 4E 05                     lea r9d, [rsi + 5]
002A1ECB  49 89 3F                        mov qword ptr [r15], rdi
002A1ECE  44 8D 46 04                     lea r8d, [rsi + 4]
002A1ED2  49 8B D7                        mov rdx, r15
002A1ED5  E8 86 FF 08 00                  call 0x140331e60
002A1EDA  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
002A1EDE  48 8B D3                        mov rdx, rbx
002A1EE1  E8 AA 03 00 00                  call 0x1402a2290
002A1EE6  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002A1EF0  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
002A1EF5  48 8B 5D D7                     mov rbx, qword ptr [rbp - 0x29]
002A1EF9  41 FF C5                        inc r13d
002A1EFC  48 0F BA 25 83 4B D2 00 24      bt qword ptr [rip + 0xd24b83], 0x24
002A1F05  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
002A1F09  0F 82 A1 01 00 00               jb 0x1402a20b0
002A1F0F  48 FF 45 77                     inc qword ptr [rbp + 0x77]
002A1F13  49 89 1F                        mov qword ptr [r15], rbx
002A1F16  49 83 C7 08                     add r15, 8
002A1F1A  4C 3B 7D F7                     cmp r15, qword ptr [rbp - 9]
002A1F1E  0F 82 10 FF FF FF               jb 0x1402a1e34
002A1F24  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
002A1F28  33 FF                           xor edi, edi
002A1F2A  4D 85 F6                        test r14, r14
002A1F2D  0F 85 3A 01 00 00               jne 0x1402a206d
002A1F33  8A 55 6F                        mov dl, byte ptr [rbp + 0x6f]
002A1F36  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
002A1F3A  E8 51 B7 FD FF                  call 0x14027d690
002A1F3F  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
002A1F43  4D 85 C0                        test r8, r8
002A1F46  75 39                           jne 0x1402a1f81
002A1F48  B8 01 00 00 00                  mov eax, 1
002A1F4D  48 81 C4 88 00 00 00            add rsp, 0x88
002A1F54  41 5F                           pop r15
002A1F56  41 5E                           pop r14
002A1F58  41 5D                           pop r13
002A1F5A  41 5C                           pop r12
002A1F5C  5F                              pop rdi
002A1F5D  5E                              pop rsi
002A1F5E  5B                              pop rbx
002A1F5F  5D                              pop rbp
002A1F60  C3                              ret
002A1F61  CC                              int3
002A1F62  FF C6                           inc esi
002A1F64  85 35 42 33 D2 00               test dword ptr [rip + 0xd23342], esi
002A1F6A  0F 84 C1 02 00 00               je 0x1402a2231
002A1F70  F3 90                           pause
002A1F72  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002A1F76  48 85 C0                        test rax, rax
002A1F79  0F 89 2B FF FF FF               jns 0x1402a1eaa
002A1F7F  EB E1                           jmp 0x1402a1f62
002A1F81  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
002A1F85  48 83 EB 08                     sub rbx, 8
002A1F89  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002A1F93  48 C1 E3 19                     shl rbx, 0x19
002A1F97  48 8B C0                        mov rax, rax
002A1F9A  48 C1 E0 19                     shl rax, 0x19
002A1F9E  48 2B D8                        sub rbx, rax
002A1FA1  48 C1 FB 10                     sar rbx, 0x10
002A1FA5  48 0F BA 25 DA 4A D2 00 29      bt qword ptr [rip + 0xd24ada], 0x29
002A1FAE  0F 82 2D 02 00 00               jb 0x1402a21e1
002A1FB4  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
002A1FB8  44 8B 4E 34                     mov r9d, dword ptr [rsi + 0x34]
002A1FBC  48 83 EA 08                     sub rdx, 8
002A1FC0  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
002A1FC4  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002A1FC8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002A1FCD  E8 66 79 03 00                  call 0x1402d9938
002A1FD2  33 C0                           xor eax, eax
002A1FD4  E9 74 FF FF FF                  jmp 0x1402a1f4d
002A1FD9  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002A1FDC  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002A1FE0  A8 02                           test al, 2
002A1FE2  0F 85 70 02 00 00               jne 0x1402a2258
002A1FE8  33 D2                           xor edx, edx
002A1FEA  E8 35 13 00 00                  call 0x1402a3324
002A1FEF  45 33 D2                        xor r10d, r10d
002A1FF2  E9 57 FD FF FF                  jmp 0x1402a1d4e
002A1FF7  48 8D 4D D7                     lea rcx, [rbp - 0x29]
002A1FFB  E8 A0 08 FE FF                  call 0x1402828a0
002A2000  48 83 C8 40                     or rax, 0x40
002A2004  48 8D 4D D7                     lea rcx, [rbp - 0x29]
002A2008  48 8B D0                        mov rdx, rax
002A200B  E8 00 F8 FD FF                  call 0x140281810
002A2010  E9 EF FD FF FF                  jmp 0x1402a1e04
002A2015  45 85 ED                        test r13d, r13d
002A2018  74 14                           je 0x1402a202e
002A201A  41 B9 02 00 00 00               mov r9d, 2
002A2020  45 8B C5                        mov r8d, r13d
002A2023  49 8B D6                        mov rdx, r14
002A2026  E8 05 16 FA FF                  call 0x140243630
002A202B  45 33 ED                        xor r13d, r13d
002A202E  49 8B D6                        mov rdx, r14
002A2031  48 8B CE                        mov rcx, rsi
002A2034  E8 87 4E F7 FF                  call 0x140216ec0
002A2039  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002A2043  4D 8B F7                        mov r14, r15
002A2046  49 C1 EE 09                     shr r14, 9
002A204A  4C 23 F0                        and r14, rax
002A204D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002A2057  48 8B C0                        mov rax, rax
002A205A  4C 03 F0                        add r14, rax
002A205D  48 8B CE                        mov rcx, rsi
002A2060  49 8B D6                        mov rdx, r14
002A2063  E8 28 C8 F9 FF                  call 0x14023e890
002A2068  E9 3B FE FF FF                  jmp 0x1402a1ea8
002A206D  45 85 ED                        test r13d, r13d
002A2070  74 11                           je 0x1402a2083
002A2072  41 B9 02 00 00 00               mov r9d, 2
002A2078  45 8B C5                        mov r8d, r13d
002A207B  49 8B D6                        mov rdx, r14
002A207E  E8 AD 15 FA FF                  call 0x140243630
002A2083  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
002A2087  49 8B D6                        mov rdx, r14
002A208A  E8 31 4E F7 FF                  call 0x140216ec0
002A208F  E9 9F FE FF FF                  jmp 0x1402a1f33
002A2094  65 4C 8B 1C 25 20 00 00 00      mov r11, qword ptr gs:[0x20]
002A209D  E9 E9 FB FF FF                  jmp 0x1402a1c8b
002A20A2  C6 45 6F 11                     mov byte ptr [rbp + 0x6f], 0x11
002A20A6  E8 C9 74 F9 FF                  call 0x140239574
002A20AB  E9 80 FD FF FF                  jmp 0x1402a1e30
002A20B0  F6 C3 20                        test bl, 0x20
002A20B3  0F 85 56 FE FF FF               jne 0x1402a1f0f
002A20B9  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002A20C3  48 8B C0                        mov rax, rax
002A20C6  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
002A20D0  48 03 C1                        add rax, rcx
002A20D3  4C 3B F8                        cmp r15, rax
002A20D6  0F 82 33 FE FF FF               jb 0x1402a1f0f
002A20DC  41 B8 80 00 00 00               mov r8d, 0x80
002A20E2  48 8B D3                        mov rdx, rbx
002A20E5  49 8B CF                        mov rcx, r15
002A20E8  E8 93 0C FF FF                  call 0x140292d80
002A20ED  E9 1D FE FF FF                  jmp 0x1402a1f0f
002A20F2  BA 01 00 00 00                  mov edx, 1
002A20F7  44 8B C2                        mov r8d, edx
002A20FA  E8 31 0D 09 00                  call 0x140332e30
002A20FF  4C 8B 0D 7A E7 D6 FF            mov r9, qword ptr [rip - 0x291886]
002A2106  48 8B D3                        mov rdx, rbx
002A2109  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
002A210D  48 8B CB                        mov rcx, rbx
002A2110  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
002A2115  E8 82 72 02 00                  call 0x1402c939c
002A211A  BA 03 00 00 00                  mov edx, 3
002A211F  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
002A2123  48 8B CB                        mov rcx, rbx
002A2126  E8 25 02 00 00                  call 0x1402a2350
002A212B  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
002A212F  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
002A2133  48 89 04 CE                     mov qword ptr [rsi + rcx*8], rax
002A2137  E9 AA FD FF FF                  jmp 0x1402a1ee6
002A213C  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
002A213F  41 B9 10 00 00 00               mov r9d, 0x10
002A2145  80 7D 6F 02                     cmp byte ptr [rbp + 0x6f], 2
002A2149  44 8B C3                        mov r8d, ebx
002A214C  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002A2150  BA 03 00 00 00                  mov edx, 3
002A2155  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002A2159  45 0F 45 CA                     cmovne r9d, r10d
002A215D  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
002A2162  E8 55 4E 0D 00                  call 0x140376fbc
002A2167  4C 8B C8                        mov r9, rax
002A216A  48 83 F8 FF                     cmp rax, -1
002A216E  0F 84 E4 FB FF FF               je 0x1402a1d58
002A2174  48 8D 0C 40                     lea rcx, [rax + rax*2]
002A2178  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002A2182  48 C1 E1 04                     shl rcx, 4
002A2186  48 8B C0                        mov rax, rax
002A2189  48 03 C8                        add rcx, rax
002A218C  E8 D7 07 00 00                  call 0x1402a2968
002A2191  45 33 D2                        xor r10d, r10d
002A2194  85 C0                           test eax, eax
002A2196  0F 84 DB FB FF FF               je 0x1402a1d77
002A219C  49 FF C6                        inc r14
002A219F  E9 D3 FB FF FF                  jmp 0x1402a1d77
002A21A4  8B 43 04                        mov eax, dword ptr [rbx + 4]
002A21A7  A8 08                           test al, 8
002A21A9  0F 84 21 FB FF FF               je 0x1402a1cd0
002A21AF  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
002A21B2  83 E1 02                        and ecx, 2
002A21B5  C7 45 77 01 00 00 00            mov dword ptr [rbp + 0x77], 1
002A21BC  8B C1                           mov eax, ecx
002A21BE  F7 D8                           neg eax
002A21C0  4D 1B ED                        sbb r13, r13
002A21C3  49 F7 DD                        neg r13
002A21C6  49 FF CD                        dec r13
002A21C9  F7 D9                           neg ecx
002A21CB  1B DB                           sbb ebx, ebx
002A21CD  F7 D3                           not ebx
002A21CF  81 E3 00 00 02 00               and ebx, 0x20000
002A21D5  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
002A21D8  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
002A21DC  E9 EF FA FF FF                  jmp 0x1402a1cd0
002A21E1  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
002A21E5  48 8D 46 40                     lea rax, [rsi + 0x40]
002A21E9  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
002A21EC  4D 8B C8                        mov r9, r8
002A21EF  44 8B 46 34                     mov r8d, dword ptr [rsi + 0x34]
002A21F3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002A21F8  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
002A21FC  48 8B CB                        mov rcx, rbx
002A21FF  C1 E2 0C                        shl edx, 0xc
002A2202  E8 6D 1F 7B 00                  call 0x140a54174
002A2207  85 C0                           test eax, eax
002A2209  0F 89 39 FD FF FF               jns 0x1402a1f48
002A220F  8D 88 F3 FF FF 3F               lea ecx, [rax + 0x3ffffff3]
002A2215  83 F9 15                        cmp ecx, 0x15
002A2218  0F 87 12 8C 43 00               ja 0x1406dae30
002A221E  BA 01 08 20 00                  mov edx, 0x200801
002A2223  0F A3 CA                        bt edx, ecx
002A2226  0F 83 04 8C 43 00               jae 0x1406dae30
002A222C  E9 0A 8C 43 00                  jmp 0x1406dae3b
002A2231  8B 05 81 48 D2 00               mov eax, dword ptr [rip + 0xd24881]
002A2237  A8 40                           test al, 0x40
002A2239  0F 84 31 FD FF FF               je 0x1402a1f70
002A223F  E8 4C D2 06 00                  call 0x14030f490
002A2244  84 C0                           test al, al
002A2246  0F 84 24 FD FF FF               je 0x1402a1f70
002A224C  8B CE                           mov ecx, esi
002A224E  E8 0D D2 06 00                  call 0x14030f460
002A2253  E9 1A FD FF FF                  jmp 0x1402a1f72
002A2258  48 8B D7                        mov rdx, rdi
002A225B  E8 3C 07 08 00                  call 0x14032299c
002A2260  49 8B CC                        mov rcx, r12
002A2263  4D 85 E4                        test r12, r12
002A2266  0F 84 66 FD FF FF               je 0x1402a1fd2
002A226C  4D 8B 24 24                     mov r12, qword ptr [r12]
002A2270  E8 6B 28 09 00                  call 0x140334ae0
002A2275  EB E9                           jmp 0x1402a2260
002A2277  49 8B D6                        mov rdx, r14
002A227A  48 8B CB                        mov rcx, rbx
002A227D  E8 1A 07 08 00                  call 0x14032299c
002A2282  E9 27 FB FF FF                  jmp 0x1402a1dae
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateKernelStackPages(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    v_r13 = 0;
    v_stack_m88 = 0;
    v_stack_m54 = 0;
    *(unsigned __int64 *)(a1 + 64) = 0;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_002A1F48;
    v_stack_m80 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m70 = *(unsigned __int64 *)(a1 + 40);
    v_stack_m68 = *(unsigned __int64 *)(a1 + 8) + *(unsigned __int64 *)(a1 + 24) * 8;
    v_stack_m90 = *(unsigned __int64 *)(a1);
    v_stack_p10 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 36));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)) + 1) != 0) goto loc_002A2094;
loc_002A1C8B:
    result = MiAssignDefaultChannel((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2759731 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34644)))), v_rip - 2759731, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2759731 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34644)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2759731 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34644))) & (63));
    a2 = 0;
    a4 = (unsigned int)((a4) | (896));
    v_stack_p20 = 0;
    v_stack_p18 = 0;
    v_r10 = (unsigned int)(((unsigned __int8)(result)) & (1));
    a4 = (unsigned int)((a4) + ((unsigned int)(a4)));
    v_stack_m60 = *(unsigned __int64 *)(v_rip - 2759731 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8 + 16550976) + 34640;
    v_r10 = (unsigned int)((v_r10) | ((unsigned int)(a4)));
    v_r10 = (unsigned int)((v_r10) << (8));
    v_stack_m58 = (unsigned int)(v_r10);
    if (v_stack_m80 != 0) goto loc_002A21A4;
loc_002A1CD0:
    result = (((unsigned __int8)(*(unsigned __int8 *)(a1 + 36))) == 2) ? 1 : 0;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (2));
    a3 = 0;
    v_stack_m98 = (unsigned int)(result);
    result = MiAcquireNonPagedResources(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 24), a3, a4);
    v_r10 = 0;
    if (sign_flag) goto loc_002A1FD2;
loc_002A1D03:
    v_stack_m78 = 0;
    if (0 >= (*(unsigned __int64 *)(a1 + 24))) goto loc_002A1DA1;
    a1 = (v_stack_m58) >> (16);
    a2 = 0;
    a1 = (unsigned int)((a1) & (3));
    a4 = (unsigned int)((v_stack_m58) & (0xFFFFFF00ULL));
    v_rbx = (unsigned int)((0) | ((unsigned int)(a4)));
loc_002A1D4E:
    if (v_stack_p18 != 0) goto loc_002A213C;
loc_002A1D58:
    result = MiGetPage(v_stack_m90, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m98), a4);
    if (result == -1) goto loc_002A1FD9;
    v_r10 = 0;
loc_002A1D77:
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = (v_stack_m78) + 1;
    *(unsigned __int64 *)(a1) = 0;
    goto loc_002A1D03;
loc_002A1DA1:
    if (0 != 0) goto loc_002A2277;
loc_002A1DAE:
    v_rdi = *(unsigned __int64 *)(a1 + 24);
    if (v_stack_m90 == (v_rip + 12152651)) {
        v_rdi = (*(unsigned __int64 *)(a1 + 24)) - (0);
    }
    result = MiMakeDemandZeroPte(4, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m98), result);
    result = -(v_stack_m80);
    a2 = 0;
    a3 = (unsigned int)(((unsigned int)(v_stack_m98)) & (0x7FFFFFFDULL));
    a3 = (unsigned int)((a3) + (0xA0000004ULL));
    result = MiMakeValidPte(*(unsigned __int64 *)(a1 + 8), a2, a3, result);
    v_stack_m88 = result;
    if (v_stack_m80 != 0) goto loc_002A1FF7;
loc_002A1E04:
    v_r13 = 0;
    v_r14 = 0;
    result = MiVaToFlushVm(*(unsigned __int64 *)(a1 + 8), a2, a3, result);
    v_stack_p20 = result;
    if (v_stack_p10 == 2) goto loc_002A20A2;
    result = MiLockWorkingSetShared(result, a2, a3, result);
    v_stack_p10 = (unsigned __int8)(result);
loc_002A1E30:
loc_002A1E34:
    v_r12 = a1;
    if (a1 != 0) {
        v_r12 = *(unsigned __int64 *)(a1);
    }
    a1 = (a1) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    v_stack_m78 = a1;
    a1 = (a1) & (result);
    result = (v_stack_m88) & (0);
    a1 = (a1) << (12);
    a1 = (a1) | (result);
    v_stack_m88 = a1;
    if (0 == 0) goto loc_002A2039;
    if (((*(unsigned __int64 *)(a1 + 8)) & (0xFFFULL)) == 0) goto loc_002A2015;
loc_002A1EA8:
    v_rsi = 0;
loc_002A1EAA:
    if (condition_is_below) goto loc_002A1F62;
    if (v_stack_m80 != 0) goto loc_002A20F2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = result;
    result = MiInitializePfn(a1, *(unsigned __int64 *)(a1 + 8), v_stack_m80 + 4, v_stack_m80 + 5);
    result = MiMarkKernelStack(a1, a1, v_stack_m70, v_stack_m80 + 5);
loc_002A1EE6:
    v_r13 = (unsigned int)((v_r13) + 1);
    if (condition_is_below) goto loc_002A20B0;
loc_002A1F0F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = v_stack_m88;
    v_r15 = (*(unsigned __int64 *)(a1 + 8)) + (8);
    if (v_r15 < v_stack_m68) goto loc_002A1E34;
    v_rdi = 0;
    if (0 != 0) goto loc_002A206D;
loc_002A1F33:
    result = MiUnlockWorkingSetShared(v_stack_p20, v_stack_p10, v_stack_m70, v_stack_m80 + 5);
    if (v_stack_m80 != 0) goto loc_002A1F81;
loc_002A1F48:
loc_002A1F4D:
    v_rsp = (v_rsp) + (136);
    return 1;
loc_002A1F62:
    v_rsi = (unsigned int)((v_stack_p8) + 1);
    if (((*(unsigned int *)(v_rip + 13775682)) & ((unsigned int)(v_rsi))) == 0) goto loc_002A2231;
loc_002A1F70:
loc_002A1F72:
    if (!sign_flag) goto loc_002A1EAA;
    goto loc_002A1F62;
loc_002A1F81:
    v_rbx = (*(unsigned __int64 *)(v_rsi + 8)) - (8);
    v_rbx = (v_rbx) << (25);
    result = (*(unsigned __int64 *)(v_stack_m88 + 24)) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if (condition_is_below) goto loc_002A21E1;
    a2 = (*(unsigned __int64 *)(v_rsi + 8)) - (8);
    v_stack_p20 = 0;
    result = MiDeleteKernelStackPages(v_stack_m90, a2, v_stack_p18, (unsigned int)(*(unsigned int *)(v_rsi + 52)));
loc_002A1FD2:
    result = 0;
    goto loc_002A1F4D;
loc_002A1FD9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) & (2)) != 0) goto loc_002A2258;
    a2 = 0;
    result = MiWaitForFreePage(v_stack_m90, a2, v_stack_p18, (unsigned int)(*(unsigned int *)(v_rsi + 52)));
    v_r10 = 0;
    goto loc_002A1D4E;
loc_002A1FF7:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m88, a2, v_stack_p18, (unsigned int)(*(unsigned int *)(v_rsi + 52)));
    result = (result) | (64);
    result = MiWriteValidPteNewProtection(v_stack_m88, result, v_stack_p18, (unsigned int)(*(unsigned int *)(v_rsi + 52)));
    goto loc_002A1E04;
loc_002A2015:
    if ((unsigned int)(v_r13) != 0) {
        a4 = 2;
        a3 = (unsigned int)(v_r13);
        a2 = 0;
        result = MiIncreaseUsedPtes(v_stack_m88, a2, a3, a4);
        v_r13 = 0;
    }
    result = MiUnlockPageTable(v_rsi, 0, a3, a4);
loc_002A2039:
    v_r14 = (v_r15) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (result);
    result = MiLockNestedPageTable(v_rsi, v_r14, a3, a4);
    goto loc_002A1EA8;
loc_002A206D:
    if (0 != 0) {
        a4 = 2;
        a3 = 0;
        a2 = v_r14;
        result = MiIncreaseUsedPtes(v_rsi, a2, a3, a4);
    }
    result = MiUnlockPageTable(v_stack_p20, v_r14, a3, a4);
    goto loc_002A1F33;
loc_002A2094:
    goto loc_002A1C8B;
loc_002A20A2:
    v_stack_p10 = 17;
    result = MiLockWorkingSetSharedAtDpc(v_stack_p20, v_r14, a3, a4);
    goto loc_002A1E30;
loc_002A20B0:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_002A1F0F;
    result = (result) + (v_stack_p20);
    if (v_r15 < result) goto loc_002A1F0F;
    result = MiCheckLinearProtectedPteAccessedBit(v_r15, v_rbx, 128, a4);
    goto loc_002A1F0F;
loc_002A20F2:
    result = MiFinalizePageAttribute(v_r15, 1, 1, a4);
    result = MiInitializeMdlSinglePage(v_rbx, v_rbx, v_stack_m70, *(unsigned __int64 *)(v_rip - 2693254));
    *(unsigned __int64 *)(v_rbx + 8) = v_r15;
    result = MiSetPfnIdentity(v_rbx, 3, v_stack_m70, *(unsigned __int64 *)(v_rip - 2693254));
    *(unsigned __int64 *)(v_rsi + v_stack_p18 * 8) = v_stack_m78;
    goto loc_002A1EE6;
loc_002A213C:
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p20));
    a4 = 16;
    if (v_stack_p10 != 2) { a4 = 0; }
    v_stack_p20 = 0;
    result = MiGetSlabPage(v_stack_m90, 3, (unsigned int)((unsigned int)(v_rbx)), a4);
    if (result == -1) goto loc_002A1D58;
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiIsPfnFromChargedSlabAllocation(a1, 3, (unsigned int)((unsigned int)(v_rbx)), result);
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_002A1D77;
    v_r14 = (v_r14) + 1;
    goto loc_002A1D77;
loc_002A21A4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 4)))) & (8)) == 0) goto loc_002A1CD0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) & (2));
    v_stack_p18 = 1;
    result = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    v_r13 = -(v_r13);
    v_r13 = (v_r13) - 1;
    a1 = (unsigned int)(-(a1));
    v_rbx = (unsigned int)(~(v_rbx));
    v_rbx = (unsigned int)((v_rbx) & (0x20000ULL));
    v_stack_p20 = (unsigned int)(v_rbx);
    goto loc_002A1CD0;
loc_002A21E1:
    v_stack_p28 = v_rsi + 64;
    v_stack_p20 = (unsigned int)(v_stack_p18);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 16))) << (12));
    result = VslAllocateKernelShadowStack(v_stack_m90, a2, (unsigned int)(*(unsigned int *)(v_rsi + 52)), (unsigned int)((unsigned int)(v_rbx)));
    if (!sign_flag) goto loc_002A1F48;
loc_002A2231:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13781121)))) & (64)) == 0) goto loc_002A1F70;
    result = KiCheckVpBackingLongSpinWaitHypercall(result + 1073741811, (unsigned int)(0x200801ULL), (unsigned int)(*(unsigned int *)(v_rsi + 52)), (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned __int8)(result) == 0) goto loc_002A1F70;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x200801ULL), (unsigned int)(*(unsigned int *)(v_rsi + 52)), (unsigned int)((unsigned int)(v_rbx)));
    goto loc_002A1F72;
loc_002A2258:
    result = MiReleaseNonPagedResources((unsigned int)((unsigned int)(v_rsi)), 0, (unsigned int)(*(unsigned int *)(v_rsi + 52)), (unsigned int)((unsigned int)(v_rbx)));
loc_002A2260:
    if (v_r12 == 0) goto loc_002A1FD2;
    result = MiReleaseFreshPage(v_r12, 0, (unsigned int)(*(unsigned int *)(v_rsi + 52)), (unsigned int)((unsigned int)(v_rbx)));
    goto loc_002A2260;
loc_002A2277:
    result = MiReleaseNonPagedResources(v_stack_m90, v_r14, (unsigned int)(*(unsigned int *)(v_rsi + 52)), (unsigned int)((unsigned int)(v_rbx)));
    goto loc_002A1DAE;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateKernelStackPages(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    local_r13 = 0;
    v_stack_m88 = 0;
    v_stack_m54 = 0;
    *(uint64_t *)(arg1 + 0x40) = 0;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_002A1F48;
    v_stack_m80 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m70 = *(uint64_t *)(arg1 + 0x28);
    v_stack_m68 = *(uint64_t *)(arg1 + 0x8) + *(uint64_t *)(arg1 + 0x18) * 8;
    v_stack_m90 = *(uint64_t *)(arg1);
    v_stack_p10 = (uint8_t)(*(uint8_t *)(arg1 + 0x24));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)) + 1) != 0) goto loc_002A2094;
loc_002A1C8B:
    result = MiAssignDefaultChannel((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x2A1C33 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 0x8754)))), v_rip - 2759731, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x2A1C33 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 0x8754)));
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x2A1C33 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 0x8754))) & (63));
    Arg2 = 0;
    a4 = (uint32_t)((a4) | (896));
    v_stack_p20 = 0;
    v_stack_p18 = 0;
    local_r10 = (uint32_t)(((uint8_t)(result)) & (1));
    a4 = (uint32_t)((a4) + ((uint32_t)(a4)));
    v_stack_m60 = *(uint64_t *)(v_rip - 0x2A1C33 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8 + 0xFC8C40) + 34640;
    local_r10 = (uint32_t)((local_r10) | ((uint32_t)(a4)));
    local_r10 = (uint32_t)((local_r10) << (8));
    v_stack_m58 = (uint32_t)(local_r10);
    if (v_stack_m80 != 0) goto loc_002A21A4;
loc_002A1CD0:
    result = (((uint8_t)(*(uint8_t *)(arg1 + 0x24))) == 2) ? 1 : 0;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (2));
    Arg3 = 0;
    v_stack_m98 = (uint32_t)(result);
    result = MiAcquireNonPagedResources(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x18), Arg3, a4);
    local_r10 = 0;
    if (sign_flag) goto loc_002A1FD2;
loc_002A1D03:
    v_stack_m78 = 0;
    if (0 >= (*(uint64_t *)(arg1 + 0x18))) goto loc_002A1DA1;
    Arg1 = (v_stack_m58) >> (16);
    Arg2 = 0;
    Arg1 = (uint32_t)((Arg1) & (3));
    a4 = (uint32_t)((v_stack_m58) & (0xFFFFFF00ULL));
    local_rbx = (uint32_t)((0) | ((uint32_t)(a4)));
loc_002A1D4E:
    if (v_stack_p18 != 0) goto loc_002A213C;
loc_002A1D58:
    result = MiGetPage(v_stack_m90, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m98), a4);
    if (result == -1) goto loc_002A1FD9;
    local_r10 = 0;
loc_002A1D77:
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = (v_stack_m78) + 1;
    *(uint64_t *)(arg1) = 0;
    goto loc_002A1D03;
loc_002A1DA1:
    if (0 != 0) goto loc_002A2277;
loc_002A1DAE:
    local_rdi = *(uint64_t *)(arg1 + 0x18);
    if (v_stack_m90 == (v_rip + 12152651)) {
        local_rdi = (*(uint64_t *)(arg1 + 0x18)) - (0);
    }
    result = MiMakeDemandZeroPte(4, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m98), result);
    result = -(v_stack_m80);
    Arg2 = 0;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m98)) & (0x7FFFFFFDULL));
    Arg3 = (uint32_t)((Arg3) + (0xA0000004ULL));
    result = MiMakeValidPte(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, result);
    v_stack_m88 = result;
    if (v_stack_m80 != 0) goto loc_002A1FF7;
loc_002A1E04:
    local_r13 = 0;
    local_r14 = 0;
    result = MiVaToFlushVm(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, result);
    v_stack_p20 = result;
    if (v_stack_p10 == 2) goto loc_002A20A2;
    result = MiLockWorkingSetShared(result, Arg2, Arg3, result);
    v_stack_p10 = (uint8_t)(result);
loc_002A1E30:
loc_002A1E34:
    local_r12 = Arg1;
    if (Arg1 != NULL) {
        local_r12 = *(uint64_t *)(arg1);
    }
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    v_stack_m78 = Arg1;
    Arg1 = (Arg1) & (result);
    result = (v_stack_m88) & (0);
    Arg1 = (Arg1) << (12);
    Arg1 = (Arg1) | (result);
    v_stack_m88 = Arg1;
    if (0 == 0) goto loc_002A2039;
    if (((*(uint64_t *)(arg1 + 0x8)) & (0xFFFULL)) == 0) goto loc_002A2015;
loc_002A1EA8:
    local_rsi = 0;
loc_002A1EAA:
    if (condition_is_below) goto loc_002A1F62;
    if (v_stack_m80 != 0) goto loc_002A20F2;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) = result;
    result = MiInitializePfn(Arg1, *(uint64_t *)(arg1 + 0x8), v_stack_m80 + 4, v_stack_m80 + 5);
    result = MiMarkKernelStack(Arg1, Arg1, v_stack_m70, v_stack_m80 + 5);
loc_002A1EE6:
    local_r13 = (uint32_t)((local_r13) + 1);
    if (condition_is_below) goto loc_002A20B0;
loc_002A1F0F:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) = v_stack_m88;
    local_r15 = (*(uint64_t *)(arg1 + 0x8)) + (8);
    if (local_r15 < v_stack_m68) goto loc_002A1E34;
    local_rdi = 0;
    if (0 != 0) goto loc_002A206D;
loc_002A1F33:
    result = MiUnlockWorkingSetShared(v_stack_p20, v_stack_p10, v_stack_m70, v_stack_m80 + 5);
    if (v_stack_m80 != 0) goto loc_002A1F81;
loc_002A1F48:
loc_002A1F4D:
    local_rsp = (local_rsp) + (136);
    return 1;
loc_002A1F62:
    local_rsi = (uint32_t)((v_stack_p8) + 1);
    if (((*(uint32_t *)(v_rip + 0xD23342)) & ((uint32_t)(local_rsi))) == 0) goto loc_002A2231;
loc_002A1F70:
loc_002A1F72:
    if (!sign_flag) goto loc_002A1EAA;
    goto loc_002A1F62;
loc_002A1F81:
    local_rbx = (*(uint64_t *)(local_rsi + 0x8)) - (8);
    local_rbx = (local_rbx) << (25);
    result = (*(uint64_t *)(v_stack_m88 + 0x18)) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if (condition_is_below) goto loc_002A21E1;
    Arg2 = (*(uint64_t *)(local_rsi + 0x8)) - (8);
    v_stack_p20 = 0;
    result = MiDeleteKernelStackPages(v_stack_m90, Arg2, v_stack_p18, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)));
loc_002A1FD2:
    result = 0;
    goto loc_002A1F4D;
loc_002A1FD9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) & (2)) != 0) goto loc_002A2258;
    Arg2 = 0;
    result = MiWaitForFreePage(v_stack_m90, Arg2, v_stack_p18, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)));
    local_r10 = 0;
    goto loc_002A1D4E;
loc_002A1FF7:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m88, Arg2, v_stack_p18, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)));
    result = (result) | (64);
    result = MiWriteValidPteNewProtection(v_stack_m88, result, v_stack_p18, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)));
    goto loc_002A1E04;
loc_002A2015:
    if ((uint32_t)(local_r13) != 0) {
        a4 = 2;
        Arg3 = (uint32_t)(local_r13);
        Arg2 = 0;
        result = MiIncreaseUsedPtes(v_stack_m88, Arg2, Arg3, a4);
        local_r13 = 0;
    }
    result = MiUnlockPageTable(local_rsi, 0, Arg3, a4);
loc_002A2039:
    local_r14 = (local_r15) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (result);
    result = MiLockNestedPageTable(local_rsi, local_r14, Arg3, a4);
    goto loc_002A1EA8;
loc_002A206D:
    if (0 != 0) {
        a4 = 2;
        Arg3 = 0;
        Arg2 = local_r14;
        result = MiIncreaseUsedPtes(local_rsi, Arg2, Arg3, a4);
    }
    result = MiUnlockPageTable(v_stack_p20, local_r14, Arg3, a4);
    goto loc_002A1F33;
loc_002A2094:
    goto loc_002A1C8B;
loc_002A20A2:
    v_stack_p10 = 17;
    result = MiLockWorkingSetSharedAtDpc(v_stack_p20, local_r14, Arg3, a4);
    goto loc_002A1E30;
loc_002A20B0:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_002A1F0F;
    result = (result) + (v_stack_p20);
    if (local_r15 < result) goto loc_002A1F0F;
    result = MiCheckLinearProtectedPteAccessedBit(local_r15, local_rbx, 128, a4);
    goto loc_002A1F0F;
loc_002A20F2:
    result = MiFinalizePageAttribute(local_r15, 1, 1, a4);
    result = MiInitializeMdlSinglePage(local_rbx, local_rbx, v_stack_m70, *(uint64_t *)(v_rip - 0x291886));
    *(uint64_t *)(local_rbx + 0x8) = local_r15;
    result = MiSetPfnIdentity(local_rbx, 3, v_stack_m70, *(uint64_t *)(v_rip - 0x291886));
    *(uint64_t *)(local_rsi + v_stack_p18 * 8) = v_stack_m78;
    goto loc_002A1EE6;
loc_002A213C:
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p20));
    a4 = 16;
    if (v_stack_p10 != 2) { a4 = 0; }
    v_stack_p20 = 0;
    result = MiGetSlabPage(v_stack_m90, 3, (uint32_t)((uint32_t)(local_rbx)), a4);
    if (result == -1) goto loc_002A1D58;
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiIsPfnFromChargedSlabAllocation(Arg1, 3, (uint32_t)((uint32_t)(local_rbx)), result);
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_002A1D77;
    local_r14 = (local_r14) + 1;
    goto loc_002A1D77;
loc_002A21A4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4)))) & (8)) == 0) goto loc_002A1CD0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) & (2));
    v_stack_p18 = 1;
    result = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    local_r13 = -(local_r13);
    local_r13 = (local_r13) - 1;
    Arg1 = (uint32_t)(-(Arg1));
    local_rbx = (uint32_t)(~(local_rbx));
    local_rbx = (uint32_t)((local_rbx) & (0x20000ULL));
    v_stack_p20 = (uint32_t)(local_rbx);
    goto loc_002A1CD0;
loc_002A21E1:
    v_stack_p28 = local_rsi + 64;
    v_stack_p20 = (uint32_t)(v_stack_p18);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x10))) << (12));
    result = VslAllocateKernelShadowStack(v_stack_m90, Arg2, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)), (uint32_t)((uint32_t)(local_rbx)));
    if (!sign_flag) goto loc_002A1F48;
loc_002A2231:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD24881)))) & (64)) == 0) goto loc_002A1F70;
    result = KiCheckVpBackingLongSpinWaitHypercall(result + 1073741811, (uint32_t)(0x200801ULL), (uint32_t)(*(uint32_t *)(local_rsi + 0x34)), (uint32_t)((uint32_t)(local_rbx)));
    if ((uint8_t)(result) == 0) goto loc_002A1F70;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x200801ULL), (uint32_t)(*(uint32_t *)(local_rsi + 0x34)), (uint32_t)((uint32_t)(local_rbx)));
    goto loc_002A1F72;
loc_002A2258:
    result = MiReleaseNonPagedResources((uint32_t)((uint32_t)(local_rsi)), 0, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)), (uint32_t)((uint32_t)(local_rbx)));
loc_002A2260:
    if (local_r12 == 0) goto loc_002A1FD2;
    result = MiReleaseFreshPage(local_r12, 0, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)), (uint32_t)((uint32_t)(local_rbx)));
    goto loc_002A2260;
loc_002A2277:
    result = MiReleaseNonPagedResources(v_stack_m90, local_r14, (uint32_t)(*(uint32_t *)(local_rsi + 0x34)), (uint32_t)((uint32_t)(local_rbx)));
    goto loc_002A1DAE;
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
| `Arg1` | `+ 0x24` | `8` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A1BEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
