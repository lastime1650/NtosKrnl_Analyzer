# MiCompletePrivateZeroFault

- RVA: `0x00330CC0`–`0x00331E4B` (길이 `4,491` bytes)
- VA: `0x0000000140330CC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076574`
- 디코드: `1,063`개 명령, `4,491/4,491` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00330EB2` → [MiIsAddressGlobal](MiIsAddressGlobal_function_003308D0.md) (function, `0x003308D0`)
- `0x00331027` → [MiInitializePfn](MiInitializePfn_function_00331E60.md) (function, `0x00331E60`)
- `0x0033119E` → [MiAddWorkingSetEntries](../27/MiAddWorkingSetEntries_function_0027DC00.md) (function, `0x0027DC00`)
- `0x00331202` → [MiAllocateWsle](MiAllocateWsle_function_003332C0.md) (function, `0x003332C0`)
- `0x0033126F` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x003313C0` → [MiMapPageInHyperSpaceWorker](MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x00331538` → [MiInsertPageInFreeOrZeroedList](MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x00331561` → [MiDecrementShareCountEx](MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x00331599` → [MiReleaseFreshPage](MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x00331603` → [MiMapPageInHyperSpaceWorker](MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x003316D7` → [MiEmptyDeferredWorkingSetEntries](../34/MiEmptyDeferredWorkingSetEntries_function_00347910.md) (function, `0x00347910`)
- `0x003317C1` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00331802` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x0033185F` → [MiAdvanceFaultList](../36/MiAdvanceFaultList_function_003637A0.md) (function, `0x003637A0`)
- `0x003318A6` → [MiUserPdeOrAbove](../2C/MiUserPdeOrAbove_function_002C57F0.md) (function, `0x002C57F0`)
- `0x0033193E` → [MiUpdatePageTableUseCount](../3D/MiUpdatePageTableUseCount_function_003D34F0.md) (function, `0x003D34F0`)
- `0x00331965` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x00331976` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x003319B0` → [MiDecrementShareCountEx](MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x003319FE` → [MiEmptyDeferredWorkingSetEntries](../34/MiEmptyDeferredWorkingSetEntries_function_00347910.md) (function, `0x00347910`)
- `0x00331A36` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00331AC4` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00331B05` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x00331B2E` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00331B4E` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00331B5E` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00331B79` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00331B88` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00331BA0` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00331BAF` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00331C07` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00331C6A` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x00331C8E` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x00331CAD` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x00331CD2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00331CE1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00331D38` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x00331D4E` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x00331D68` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x00331D72` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00331D7E` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x00331DA4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00331DB3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00331DE5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00331E28` → [MiBadShareCount](../37/MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)

### Direct callers
- [sub_0032FBA9](../32/Unknown_function_0032FBA9.md) at `0x0032FE29`

### Static image references
- `0x00330DEF` → RVA `0x00010990` (`.rdata`; read)
- `0x00330EDD` → RVA `0x00E2EE84` (`.data`; read)
- `0x0033123E` → RVA `0x00E2DC80` (`.data`; read)
- `0x0033148C` → RVA `0x00010880` (`.rdata`; read)
- `0x003314CE` → RVA `0x00E30088` (`.data`; read)
- `0x00331664` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00331742` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00331B6B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00330CC0  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00330CC5  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00330CCA  55                              push rbp
00330CCB  53                              push rbx
00330CCC  56                              push rsi
00330CCD  57                              push rdi
00330CCE  41 54                           push r12
00330CD0  41 55                           push r13
00330CD2  41 56                           push r14
00330CD4  41 57                           push r15
00330CD6  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00330CDB  48 81 EC C8 00 00 00            sub rsp, 0xc8
00330CE2  4C 8B 79 10                     mov r15, qword ptr [rcx + 0x10]
00330CE6  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
00330CF0  48 8B 79 38                     mov rdi, qword ptr [rcx + 0x38]
00330CF4  4C 8B EA                        mov r13, rdx
00330CF7  49 C1 EF 09                     shr r15, 9
00330CFB  4C 8B E1                        mov r12, rcx
00330CFE  4D 23 FA                        and r15, r10
00330D01  48 89 7D D7                     mov qword ptr [rbp - 0x29], rdi
00330D05  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
00330D0F  49 8B C1                        mov rax, r9
00330D12  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00330D16  4C 03 F8                        add r15, rax
00330D19  45 33 DB                        xor r11d, r11d
00330D1C  C6 45 67 00                     mov byte ptr [rbp + 0x67], 0
00330D20  BB 01 00 00 00                  mov ebx, 1
00330D25  41 8B D3                        mov edx, r11d
00330D28  89 55 97                        mov dword ptr [rbp - 0x69], edx
00330D2B  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00330D2F  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00330D33  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00330D37  84 C3                           test bl, al
00330D39  0F 85 D2 0C 00 00               jne 0x140331a11
00330D3F  41 F6 04 24 20                  test byte ptr [r12], 0x20
00330D44  49 8B C3                        mov rax, r11
00330D47  48 0F 45 C7                     cmovne rax, rdi
00330D4B  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00330D4F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00330D58  48 8B 09                        mov rcx, qword ptr [rcx]
00330D5B  48 C1 E9 09                     shr rcx, 9
00330D5F  49 23 CA                        and rcx, r10
00330D62  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00330D69  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00330D6D  49 8B C1                        mov rax, r9
00330D70  48 03 C8                        add rcx, rax
00330D73  44 89 5D A7                     mov dword ptr [rbp - 0x59], r11d
00330D77  49 8B 44 24 40                  mov rax, qword ptr [r12 + 0x40]
00330D7C  BF 10 20 00 00                  mov edi, 0x2010
00330D81  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
00330D85  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00330D89  89 7D 7F                        mov dword ptr [rbp + 0x7f], edi
00330D8C  48 85 C0                        test rax, rax
00330D8F  74 26                           je 0x140330db7
00330D91  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
00330D94  0F B6 50 22                     movzx edx, byte ptr [rax + 0x22]
00330D98  48 B8 FE FF FF FF 07 00 00 00   movabs rax, 0x7fffffffe
00330DA2  48 C1 E2 20                     shl rdx, 0x20
00330DA6  48 0B D1                        or rdx, rcx
00330DA9  B9 50 20 00 00                  mov ecx, 0x2050
00330DAE  48 3B D0                        cmp rdx, rax
00330DB1  0F 44 F9                        cmove edi, ecx
00330DB4  89 7D 7F                        mov dword ptr [rbp + 0x7f], edi
00330DB7  41 8B 74 24 20                  mov esi, dword ptr [r12 + 0x20]
00330DBC  48 B9 78 FF FF FF 3F 00 00 00   movabs rcx, 0x3fffffff78
00330DC6  89 75 B7                        mov dword ptr [rbp - 0x49], esi
00330DC9  40 F6 C6 02                     test sil, 2
00330DCD  0F 85 E6 0D 00 00               jne 0x140331bb9
00330DD3  0F BA EE 1F                     bts esi, 0x1f
00330DD7  89 75 B7                        mov dword ptr [rbp - 0x49], esi
00330DDA  45 39 5C 24 24                  cmp dword ptr [r12 + 0x24], r11d
00330DDF  75 08                           jne 0x140330de9
00330DE1  65 FF 04 25 9C 2E 00 00         inc dword ptr gs:[0x2e9c]
00330DE9  8B DE                           mov ebx, esi
00330DEB  44 89 5D 9B                     mov dword ptr [rbp - 0x65], r11d
00330DEF  48 8D 05 9A FB CD FF            lea rax, [rip - 0x320466]
00330DF6  44 89 5D AB                     mov dword ptr [rbp - 0x55], r11d
00330DFA  83 E3 1F                        and ebx, 0x1f
00330DFD  45 8B D3                        mov r10d, r11d
00330E00  48 8B 3C D8                     mov rdi, qword ptr [rax + rbx*8]
00330E04  48 B8 7F 0E 00 00 00 00 F0 FF   movabs rax, 0xfff0000000000e7f
00330E0E  48 23 F8                        and rdi, rax
00330E11  48 83 CF 21                     or rdi, 0x21
00330E15  49 8B C1                        mov rax, r9
00330E18  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00330E22  4C 3B F8                        cmp r15, rax
00330E25  0F 82 01 09 00 00               jb 0x14033172c
00330E2B  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
00330E35  49 8B C1                        mov rax, r9
00330E38  4C 3B F8                        cmp r15, rax
00330E3B  0F 87 EB 08 00 00               ja 0x14033172c
00330E41  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00330E4B  4C 3B F8                        cmp r15, rax
00330E4E  0F 83 20 0A 00 00               jae 0x140331874
00330E54  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
00330E5E  49 8B D6                        mov rdx, r14
00330E61  48 C1 E2 19                     shl rdx, 0x19
00330E65  49 8B CF                        mov rcx, r15
00330E68  48 C1 E1 19                     shl rcx, 0x19
00330E6C  48 2B CA                        sub rcx, rdx
00330E6F  48 C1 F9 10                     sar rcx, 0x10
00330E73  0F BA E6 1A                     bt esi, 0x1a
00330E77  73 23                           jae 0x140330e9c
00330E79  49 8B C6                        mov rax, r14
00330E7C  48 3B C8                        cmp rcx, rax
00330E7F  72 1B                           jb 0x140330e9c
00330E81  49 8B C1                        mov rax, r9
00330E84  48 3B C8                        cmp rcx, rax
00330E87  77 13                           ja 0x140330e9c
00330E89  48 C1 E1 19                     shl rcx, 0x19
00330E8D  48 2B CA                        sub rcx, rdx
00330E90  48 C1 F9 10                     sar rcx, 0x10
00330E94  49 8B C6                        mov rax, r14
00330E97  48 3B C8                        cmp rcx, rax
00330E9A  73 E5                           jae 0x140330e81
00330E9C  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
00330EA6  48 3B C8                        cmp rcx, rax
00330EA9  0F 86 87 08 00 00               jbe 0x140331736
00330EAF  48 8B D7                        mov rdx, rdi
00330EB2  E8 19 FA FF FF                  call 0x1403308d0
00330EB7  48 0F BA EF 08                  bts rdi, 8
00330EBC  85 C0                           test eax, eax
00330EBE  48 0F 44 FA                     cmove rdi, rdx
00330EC2  85 F6                           test esi, esi
00330EC4  0F 88 21 0F 00 00               js 0x140331deb
00330ECA  0F BA E6 1E                     bt esi, 0x1e
00330ECE  0F 82 0D 08 00 00               jb 0x1403316e1
00330ED4  48 8B CF                        mov rcx, rdi
00330ED7  0F BA E6 1D                     bt esi, 0x1d
00330EDB  73 19                           jae 0x140330ef6
00330EDD  0F B6 05 A0 DF AF 00            movzx eax, byte ptr [rip + 0xafdfa0]
00330EE4  48 C1 E0 08                     shl rax, 8
00330EE8  48 8B F8                        mov rdi, rax
00330EEB  48 33 F9                        xor rdi, rcx
00330EEE  48 0F BA F7 08                  btr rdi, 8
00330EF3  48 33 F8                        xor rdi, rax
00330EF6  48 B8 FF FF FF FF FF FF FF FA   movabs rax, 0xfaffffffffffffff
00330F00  48 8B D7                        mov rdx, rdi
00330F03  48 0F BA F2 08                  btr rdx, 8
00330F08  0F BA E6 1B                     bt esi, 0x1b
00330F0C  48 0F 43 D7                     cmovae rdx, rdi
00330F10  48 8B CA                        mov rcx, rdx
00330F13  48 0F BA E9 07                  bts rcx, 7
00330F18  0F BA E6 1A                     bt esi, 0x1a
00330F1C  48 0F 43 CA                     cmovae rcx, rdx
00330F20  48 23 C8                        and rcx, rax
00330F23  48 B8 00 00 00 00 00 00 00 0A   movabs rax, 0xa00000000000000
00330F2D  48 0B C8                        or rcx, rax
00330F30  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
00330F34  49 83 F8 01                     cmp r8, 1
00330F38  0F 87 8B 0A 00 00               ja 0x1403319c9
00330F3E  49 8B CB                        mov rcx, r11
00330F41  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
00330F4B  BB FF 01 00 00                  mov ebx, 0x1ff
00330F50  49 B9 F8 D7 BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbed7f8
00330F5A  48 BA 00 D0 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed000
00330F64  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00330F68  49 3B C8                        cmp rcx, r8
00330F6B  0F 83 5C 09 00 00               jae 0x1403318cd
00330F71  49 8B 37                        mov rsi, qword ptr [r15]
00330F74  48 8B C2                        mov rax, rdx
00330F77  4C 3B F8                        cmp r15, rax
00330F7A  72 28                           jb 0x140330fa4
00330F7C  49 8B C1                        mov rax, r9
00330F7F  4C 3B F8                        cmp r15, rax
00330F82  77 20                           ja 0x140330fa4
00330F84  40 F6 C6 01                     test sil, 1
00330F88  74 1A                           je 0x140330fa4
00330F8A  40 F6 C6 42                     test sil, 0x42
00330F8E  0F 95 C1                        setne cl
00330F91  40 F6 C6 20                     test sil, 0x20
00330F95  0F 95 C0                        setne al
00330F98  84 C8                           test al, cl
00330F9A  0F 84 C4 06 00 00               je 0x140331664
00330FA0  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00330FA4  41 83 7C 24 24 00               cmp dword ptr [r12 + 0x24], 0
00330FAA  0F 84 7D 02 00 00               je 0x14033122d
00330FB0  48 0F BA E6 0A                  bt rsi, 0xa
00330FB5  72 0B                           jb 0x140330fc2
00330FB7  48 0F BA E6 1A                  bt rsi, 0x1a
00330FBC  0F 82 7F 0B 00 00               jb 0x140331b41
00330FC2  4D 8B 75 00                     mov r14, qword ptr [r13]
00330FC6  4D 85 F6                        test r14, r14
00330FC9  74 12                           je 0x140330fdd
00330FCB  49 83 6D 10 01                  sub qword ptr [r13 + 0x10], 1
00330FD0  49 8B 06                        mov rax, qword ptr [r14]
00330FD3  49 89 45 00                     mov qword ptr [r13], rax
00330FD7  75 04                           jne 0x140330fdd
00330FD9  4D 89 5D 08                     mov qword ptr [r13 + 8], r11
00330FDD  48 8B C7                        mov rax, rdi
00330FE0  49 8B DE                        mov rbx, r14
00330FE3  48 2B D8                        sub rbx, rax
00330FE6  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00330FF0  48 C1 FB 04                     sar rbx, 4
00330FF4  48 0F AF D8                     imul rbx, rax
00330FF8  41 83 7C 24 24 00               cmp dword ptr [r12 + 0x24], 0
00330FFE  0F 85 9C 05 00 00               jne 0x1403315a0
00331004  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00331007  33 F6                           xor esi, esi
00331009  45 8B 44 24 20                  mov r8d, dword ptr [r12 + 0x20]
0033100E  8B D1                           mov edx, ecx
00331010  83 CA 20                        or edx, 0x20
00331013  41 F6 04 24 02                  test byte ptr [r12], 2
00331018  0F 44 D1                        cmove edx, ecx
0033101B  49 8B CE                        mov rcx, r14
0033101E  89 55 7F                        mov dword ptr [rbp + 0x7f], edx
00331021  44 8B CA                        mov r9d, edx
00331024  49 8B D7                        mov rdx, r15
00331027  E8 34 0E 00 00                  call 0x140331e60
0033102C  48 8B 7D D7                     mov rdi, qword ptr [rbp - 0x29]
00331030  48 85 FF                        test rdi, rdi
00331033  0F 85 DB 07 00 00               jne 0x140331814
00331039  41 8B 0C 24                     mov ecx, dword ptr [r12]
0033103D  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00331047  48 23 D8                        and rbx, rax
0033104A  F6 C1 10                        test cl, 0x10
0033104D  0F 85 FB 08 00 00               jne 0x14033194e
00331053  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00331057  48 BA FF 0F 00 00 00 00 F0 FF   movabs rdx, 0xfff0000000000fff
00331061  48 23 C2                        and rax, rdx
00331064  48 C1 E3 0C                     shl rbx, 0xc
00331068  48 0B D8                        or rbx, rax
0033106B  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00331075  48 8B C3                        mov rax, rbx
00331078  48 83 E3 DF                     and rbx, 0xffffffffffffffdf
0033107C  48 83 C8 20                     or rax, 0x20
00331080  F6 C1 02                        test cl, 2
00331083  48 0F 44 D8                     cmove rbx, rax
00331087  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
0033108B  49 8B C0                        mov rax, r8
0033108E  48 BA 78 FF FF FF 3F 00 00 00   movabs rdx, 0x3fffffff78
00331098  48 8D 0C 10                     lea rcx, [rax + rdx]
0033109C  4C 3B F9                        cmp r15, rcx
0033109F  0F 87 9B 09 00 00               ja 0x140331a40
003310A5  49 8B C0                        mov rax, r8
003310A8  4C 3B F8                        cmp r15, rax
003310AB  0F 82 8F 09 00 00               jb 0x140331a40
003310B1  49 83 7C 24 48 00               cmp qword ptr [r12 + 0x48], 0
003310B7  0F 85 9C 09 00 00               jne 0x140331a59
003310BD  4C 3B 7D EF                     cmp r15, qword ptr [rbp - 0x11]
003310C1  74 39                           je 0x1403310fc
003310C3  41 F7 04 24 00 02 00 00         test dword ptr [r12], 0x200
003310CB  74 2F                           je 0x1403310fc
003310CD  48 83 E3 DF                     and rbx, 0xffffffffffffffdf
003310D1  83 7D B7 00                     cmp dword ptr [rbp - 0x49], 0
003310D5  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
003310D9  7D 21                           jge 0x1403310fc
003310DB  4C 3B F9                        cmp r15, rcx
003310DE  77 1C                           ja 0x1403310fc
003310E0  49 8B C0                        mov rax, r8
003310E3  4C 3B F8                        cmp r15, rax
003310E6  72 14                           jb 0x1403310fc
003310E8  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
003310EC  F7 80 F4 01 00 00 00 80 00 00   test dword ptr [rax + 0x1f4], 0x8000
003310F6  0F 85 13 0A 00 00               jne 0x140331b0f
003310FC  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00331101  0F B6 4A 45                     movzx ecx, byte ptr [rdx + 0x45]
00331105  48 8D 7A 38                     lea rdi, [rdx + 0x38]
00331109  0F B6 C1                        movzx eax, cl
0033110C  24 09                           and al, 9
0033110E  3C 08                           cmp al, 8
00331110  0F 85 53 07 00 00               jne 0x140331869
00331116  F6 C1 04                        test cl, 4
00331119  0F 85 4A 07 00 00               jne 0x140331869
0033111F  0F B7 47 0A                     movzx eax, word ptr [rdi + 0xa]
00331123  BB FF 01 00 00                  mov ebx, 0x1ff
00331128  66 85 C0                        test ax, ax
0033112B  74 7A                           je 0x1403311a7
0033112D  8B C8                           mov ecx, eax
0033112F  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
00331133  03 C8                           add ecx, eax
00331135  41 8B C7                        mov eax, r15d
00331138  C1 E8 03                        shr eax, 3
0033113B  23 C3                           and eax, ebx
0033113D  3B C8                           cmp ecx, eax
0033113F  0F 85 8F 05 00 00               jne 0x1403316d4
00331145  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00331149  48 85 C0                        test rax, rax
0033114C  0F 88 78 05 00 00               js 0x1403316ca
00331152  F6 47 0D 02                     test byte ptr [rdi + 0xd], 2
00331156  75 4F                           jne 0x1403311a7
00331158  49 8B C0                        mov rax, r8
0033115B  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0033115F  48 8B 0F                        mov rcx, qword ptr [rdi]
00331162  48 C1 E2 19                     shl rdx, 0x19
00331166  48 C1 E0 19                     shl rax, 0x19
0033116A  48 2B D0                        sub rdx, rax
0033116D  48 C1 FA 10                     sar rdx, 0x10
00331171  48 C1 E2 19                     shl rdx, 0x19
00331175  48 2B D0                        sub rdx, rax
00331178  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
0033117C  48 C1 E0 0C                     shl rax, 0xc
00331180  48 C1 FA 10                     sar rdx, 0x10
00331184  48 03 D0                        add rdx, rax
00331187  49 8B C0                        mov rax, r8
0033118A  48 3B D0                        cmp rdx, rax
0033118D  0F 83 EC 05 00 00               jae 0x14033177f
00331193  41 B9 05 00 00 00               mov r9d, 5
00331199  44 0F B7 47 0A                  movzx r8d, word ptr [rdi + 0xa]
0033119E  E8 5D CA F4 FF                  call 0x14027dc00
003311A3  66 89 77 0A                     mov word ptr [rdi + 0xa], si
003311A7  0F B7 47 0A                     movzx eax, word ptr [rdi + 0xa]
003311AB  66 85 C0                        test ax, ax
003311AE  0F 84 36 05 00 00               je 0x1403316ea
003311B4  66 FF C0                        inc ax
003311B7  66 89 47 0A                     mov word ptr [rdi + 0xa], ax
003311BB  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
003311C0  8B 4D 97                        mov ecx, dword ptr [rbp - 0x69]
003311C3  83 C9 04                        or ecx, 4
003311C6  F6 42 45 10                     test byte ptr [rdx + 0x45], 0x10
003311CA  0F 85 41 0A 00 00               jne 0x140331c11
003311D0  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
003311D4  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
003311D8  8B F1                           mov esi, ecx
003311DA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003311DF  83 CE 10                        or esi, 0x10
003311E2  F6 42 45 01                     test byte ptr [rdx + 0x45], 1
003311E6  4D 8B C6                        mov r8, r14
003311E9  49 8B D7                        mov rdx, r15
003311EC  0F 44 F1                        cmove esi, ecx
003311EF  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
003311F3  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
003311F7  45 33 C9                        xor r9d, r9d
003311FA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003311FF  89 75 97                        mov dword ptr [rbp - 0x69], esi
00331202  E8 B9 20 00 00                  call 0x1403332c0
00331207  85 C0                           test eax, eax
00331209  0F 84 8A 00 00 00               je 0x140331299
0033120F  FF 45 AB                        inc dword ptr [rbp - 0x55]
00331212  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00331216  49 83 C7 08                     add r15, 8
0033121A  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
0033121E  48 FF C1                        inc rcx
00331221  44 8B 55 9B                     mov r10d, dword ptr [rbp - 0x65]
00331225  45 33 DB                        xor r11d, r11d
00331228  E9 14 FD FF FF                  jmp 0x140330f41
0033122D  48 85 F6                        test rsi, rsi
00331230  0F 85 8C FD FF FF               jne 0x140330fc2
00331236  41 8B 74 24 20                  mov esi, dword ptr [r12 + 0x20]
0033123B  41 FF C2                        inc r10d
0033123E  48 8B 0D 3B CA AF 00            mov rcx, qword ptr [rip + 0xafca3b]
00331245  83 E6 1F                        and esi, 0x1f
00331248  48 C1 E6 05                     shl rsi, 5
0033124C  44 89 55 9B                     mov dword ptr [rbp - 0x65], r10d
00331250  48 85 C9                        test rcx, rcx
00331253  74 0D                           je 0x140331262
00331255  48 85 CE                        test rsi, rcx
00331258  0F 84 AE 05 00 00               je 0x14033180c
0033125E  48 83 CE 10                     or rsi, 0x10
00331262  49 8B CF                        mov rcx, r15
00331265  48 89 75 CF                     mov qword ptr [rbp - 0x31], rsi
00331269  48 8B FE                        mov rdi, rsi
0033126C  41 8B DB                        mov ebx, r11d
0033126F  E8 8C E8 F0 FF                  call 0x14023fb00
00331274  85 C0                           test eax, eax
00331276  0F 85 EA 09 00 00               jne 0x140331c66
0033127C  49 89 3F                        mov qword ptr [r15], rdi
0033127F  85 DB                           test ebx, ebx
00331281  0F 85 20 0A 00 00               jne 0x140331ca7
00331287  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
00331291  45 33 DB                        xor r11d, r11d
00331294  E9 29 FD FF FF                  jmp 0x140330fc2
00331299  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0033129D  49 BB FF FF FF FF FF 00 00 00   movabs r11, 0xffffffffff
003312A7  49 23 C3                        and rax, r11
003312AA  48 8D 1C 40                     lea rbx, [rax + rax*2]
003312AE  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003312B8  48 C1 E3 04                     shl rbx, 4
003312BC  48 8B C0                        mov rax, rax
003312BF  48 03 D8                        add rbx, rax
003312C2  45 33 FF                        xor r15d, r15d
003312C5  41 8B FF                        mov edi, r15d
003312C8  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
003312CF  0F 82 6B 04 00 00               jb 0x140331740
003312D5  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003312D9  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
003312DD  C0 E8 02                        shr al, 2
003312E0  A8 01                           test al, 1
003312E2  0F 85 0D 08 00 00               jne 0x140331af5
003312E8  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
003312EC  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003312F0  48 B9 00 00 00 00 00 00 00 40   movabs rcx, 0x4000000000000000
003312FA  48 83 E0 FD                     and rax, 0xfffffffffffffffd
003312FE  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00331302  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00331306  48 0B C1                        or rax, rcx
00331309  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0033130D  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
00331312  24 07                           and al, 7
00331314  3C 06                           cmp al, 6
00331316  0F 85 09 0B 00 00               jne 0x140331e25
0033131C  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00331320  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
0033132A  48 8B D0                        mov rdx, rax
0033132D  41 B8 FF FF 00 00               mov r8d, 0xffff
00331333  48 23 D1                        and rdx, rcx
00331336  48 FF CA                        dec rdx
00331339  48 8B CA                        mov rcx, rdx
0033133C  48 33 C8                        xor rcx, rax
0033133F  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
00331349  48 23 C8                        and rcx, rax
0033134C  48 33 CA                        xor rcx, rdx
0033134F  49 89 4E 18                     mov qword ptr [r14 + 0x18], rcx
00331353  48 85 D2                        test rdx, rdx
00331356  0F 85 58 04 00 00               jne 0x1403317b4
0033135C  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00331360  89 45 77                        mov dword ptr [rbp + 0x77], eax
00331363  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00331367  48 85 C0                        test rax, rax
0033136A  0F 89 29 01 00 00               jns 0x140331499
00331370  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
00331374  33 F6                           xor esi, esi
00331376  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0033137A  4D 8B FE                        mov r15, r14
0033137D  49 C1 E9 05                     shr r9, 5
00331381  8B FE                           mov edi, esi
00331383  4C 89 4D 7F                     mov qword ptr [rbp + 0x7f], r9
00331387  49 BB FF FF FF FF FF 00 00 00   movabs r11, 0xffffffffff
00331391  44 8B EE                        mov r13d, esi
00331394  49 83 FD 01                     cmp r13, 1
00331398  0F 83 AD 00 00 00               jae 0x14033144b
0033139E  49 8B 77 08                     mov rsi, qword ptr [r15 + 8]
003313A2  B8 FF 01 00 00                  mov eax, 0x1ff
003313A7  C1 EE 03                        shr esi, 3
003313AA  23 F0                           and esi, eax
003313AC  48 85 FF                        test rdi, rdi
003313AF  75 25                           jne 0x1403313d6
003313B1  49 8B 4F 28                     mov rcx, qword ptr [r15 + 0x28]
003313B5  33 D2                           xor edx, edx
003313B7  49 23 CB                        and rcx, r11
003313BA  41 B8 00 00 00 80               mov r8d, 0x80000000
003313C0  E8 4B 17 00 00                  call 0x140332b10
003313C5  4C 8B 4D 7F                     mov r9, qword ptr [rbp + 0x7f]
003313C9  48 8B F8                        mov rdi, rax
003313CC  49 BB FF FF FF FF FF 00 00 00   movabs r11, 0xffffffffff
003313D6  48 8B 04 F7                     mov rax, qword ptr [rdi + rsi*8]
003313DA  4C 8D 14 F7                     lea r10, [rdi + rsi*8]
003313DE  4C 8B C0                        mov r8, rax
003313E1  48 BE 00 00 00 00 00 DE FF FF   movabs rsi, 0xffffde0000000000
003313EB  49 C1 E8 0C                     shr r8, 0xc
003313EF  4D 23 C3                        and r8, r11
003313F2  4B 8D 14 40                     lea rdx, [r8 + r8*2]
003313F6  48 C1 E2 04                     shl rdx, 4
003313FA  48 8B CE                        mov rcx, rsi
003313FD  48 03 D1                        add rdx, rcx
00331400  49 3B D7                        cmp rdx, r15
00331403  0F 85 B4 09 00 00               jne 0x140331dbd
00331409  48 8B 15 70 C8 AF 00            mov rdx, qword ptr [rip + 0xafc870]
00331410  41 8B C1                        mov eax, r9d
00331413  83 E0 1F                        and eax, 0x1f
00331416  49 C1 E0 07                     shl r8, 7
0033141A  49 0B C0                        or rax, r8
0033141D  48 83 C8 40                     or rax, 0x40
00331421  48 C1 E0 05                     shl rax, 5
00331425  48 85 D2                        test rdx, rdx
00331428  74 0D                           je 0x140331437
0033142A  48 85 D0                        test rax, rdx
0033142D  0F 84 79 03 00 00               je 0x1403317ac
00331433  48 83 C8 10                     or rax, 0x10
00331437  49 89 02                        mov qword ptr [r10], rax
0033143A  49 8D 45 01                     lea rax, [r13 + 1]
0033143E  4C 8B E8                        mov r13, rax
00331441  48 83 F8 01                     cmp rax, 1
00331445  0F 85 C8 02 00 00               jne 0x140331713
0033144B  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00331455  48 C1 EF 09                     shr rdi, 9
00331459  48 23 F8                        and rdi, rax
0033145C  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00331466  48 8B C0                        mov rax, rax
00331469  4C 8B 6D 6F                     mov r13, qword ptr [rbp + 0x6f]
0033146D  48 03 F8                        add rdi, rax
00331470  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00331479  45 33 FF                        xor r15d, r15d
0033147C  8B 75 97                        mov esi, dword ptr [rbp - 0x69]
0033147F  41 B8 FF FF 00 00               mov r8d, 0xffff
00331485  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
0033148C  48 8B 05 ED F3 CD FF            mov rax, qword ptr [rip - 0x320c13]
00331493  4C 89 39                        mov qword ptr [rcx], r15
00331496  48 89 07                        mov qword ptr [rdi], rax
00331499  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0033149D  48 C1 E8 3E                     shr rax, 0x3e
003314A1  83 E0 01                        and eax, 1
003314A4  66 44 01 45 77                  add word ptr [rbp + 0x77], r8w
003314A9  0F 85 E0 05 00 00               jne 0x140331a8f
003314AF  85 C0                           test eax, eax
003314B1  0F 84 06 03 00 00               je 0x1403317bd
003314B7  0F B6 45 7A                     movzx eax, byte ptr [rbp + 0x7a]
003314BB  A8 10                           test al, 0x10
003314BD  0F 85 6B 09 00 00               jne 0x140331e2e
003314C3  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
003314C6  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
003314CA  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003314CE  48 8B 0D B3 EB AF 00            mov rcx, qword ptr [rip + 0xafebb3]
003314D5  48 C1 E8 2B                     shr rax, 0x2b
003314D9  25 FF 03 00 00                  and eax, 0x3ff
003314DE  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
003314E2  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003314E6  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
003314EA  48 0F BA E0 0A                  bt rax, 0xa
003314EF  72 1D                           jb 0x14033150e
003314F1  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
003314F5  C0 E8 02                        shr al, 2
003314F8  A8 01                           test al, 1
003314FA  75 09                           jne 0x140331505
003314FC  0F B6 C2                        movzx eax, dl
003314FF  D0 E8                           shr al, 1
00331501  A8 01                           test al, 1
00331503  74 09                           je 0x14033150e
00331505  48 85 D2                        test rdx, rdx
00331508  0F 85 1A 06 00 00               jne 0x140331b28
0033150E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00331518  48 8B C0                        mov rax, rax
0033151B  49 8B CE                        mov rcx, r14
0033151E  BA 02 00 00 00                  mov edx, 2
00331523  48 2B C8                        sub rcx, rax
00331526  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00331530  48 C1 F9 04                     sar rcx, 4
00331534  48 0F AF C8                     imul rcx, rax
00331538  E8 E3 37 00 00                  call 0x140334d20
0033153D  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00331547  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0033154C  41 8B FF                        mov edi, r15d
0033154F  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00331556  0F 82 04 02 00 00               jb 0x140331760
0033155C  33 D2                           xor edx, edx
0033155E  48 8B CB                        mov rcx, rbx
00331561  E8 0A 2A 00 00                  call 0x140333f70
00331566  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00331570  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
00331575  BF 17 00 00 C0                  mov edi, 0xc0000017
0033157A  49 8B 4D 00                     mov rcx, qword ptr [r13]
0033157E  48 85 C9                        test rcx, rcx
00331581  0F 84 4D 03 00 00               je 0x1403318d4
00331587  49 83 6D 10 01                  sub qword ptr [r13 + 0x10], 1
0033158C  48 8B 01                        mov rax, qword ptr [rcx]
0033158F  49 89 45 00                     mov qword ptr [r13], rax
00331593  75 04                           jne 0x140331599
00331595  4D 89 7D 08                     mov qword ptr [r13 + 8], r15
00331599  E8 42 35 00 00                  call 0x140334ae0
0033159E  EB DA                           jmp 0x14033157a
003315A0  49 83 7C 24 48 00               cmp qword ptr [r12 + 0x48], 0
003315A6  0F 85 58 FA FF FF               jne 0x140331004
003315AC  48 0F BA E6 0A                  bt rsi, 0xa
003315B1  0F 83 4D FA FF FF               jae 0x140331004
003315B7  48 8B 0D C2 C6 AF 00            mov rcx, qword ptr [rip + 0xafc6c2]
003315BE  48 8B C6                        mov rax, rsi
003315C1  48 85 C9                        test rcx, rcx
003315C4  74 0F                           je 0x1403315d5
003315C6  40 F6 C6 10                     test sil, 0x10
003315CA  75 09                           jne 0x1403315d5
003315CC  48 8B C1                        mov rax, rcx
003315CF  48 F7 D0                        not rax
003315D2  48 23 C6                        and rax, rsi
003315D5  48 C1 F8 10                     sar rax, 0x10
003315D9  48 85 C0                        test rax, rax
003315DC  0F 85 98 06 00 00               jne 0x140331c7a
003315E2  48 F7 C6 E0 03 00 00            test rsi, 0x3e0
003315E9  0F 84 3D 07 00 00               je 0x140331d2c
003315EF  48 0F BA F6 0A                  btr rsi, 0xa
003315F4  33 D2                           xor edx, edx
003315F6  41 B8 00 00 00 80               mov r8d, 0x80000000
003315FC  48 8B CB                        mov rcx, rbx
003315FF  48 83 E6 FD                     and rsi, 0xfffffffffffffffd
00331603  E8 08 15 00 00                  call 0x140332b10
00331608  48 8B D0                        mov rdx, rax
0033160B  48 8B F8                        mov rdi, rax
0033160E  48 8B C6                        mov rax, rsi
00331611  48 C1 EA 09                     shr rdx, 9
00331615  B9 00 02 00 00                  mov ecx, 0x200
0033161A  F3 48 AB                        rep stosq qword ptr [rdi], rax
0033161D  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00331627  48 23 D0                        and rdx, rax
0033162A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00331634  48 8B C8                        mov rcx, rax
00331637  48 03 D1                        add rdx, rcx
0033163A  33 F6                           xor esi, esi
0033163C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00331645  48 8B 81 38 88 00 00            mov rax, qword ptr [rcx + 0x8838]
0033164C  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
0033164F  83 C9 08                        or ecx, 8
00331652  48 89 30                        mov qword ptr [rax], rsi
00331655  48 8B 05 24 F2 CD FF            mov rax, qword ptr [rip - 0x320ddc]
0033165C  48 89 02                        mov qword ptr [rdx], rax
0033165F  E9 A5 F9 FF FF                  jmp 0x140331009
00331664  48 F7 05 19 54 C9 00 00 00 60 00  test qword ptr [rip + 0xc95419], 0x600000
0033166F  0F 84 2B F9 FF FF               je 0x140330fa0
00331675  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0033167E  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00331685  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
0033168C  0F 84 0E F9 FF FF               je 0x140330fa0
00331692  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00331699  48 85 D2                        test rdx, rdx
0033169C  0F 84 FE F8 FF FF               je 0x140330fa0
003316A2  49 8B C7                        mov rax, r15
003316A5  48 C1 E8 03                     shr rax, 3
003316A9  48 23 C3                        and rax, rbx
003316AC  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
003316B0  A8 20                           test al, 0x20
003316B2  74 04                           je 0x1403316b8
003316B4  48 83 CE 20                     or rsi, 0x20
003316B8  48 8B CE                        mov rcx, rsi
003316BB  48 83 CE 42                     or rsi, 0x42
003316BF  A8 42                           test al, 0x42
003316C1  48 0F 44 F1                     cmove rsi, rcx
003316C5  E9 D6 F8 FF FF                  jmp 0x140330fa0
003316CA  F6 47 0D 02                     test byte ptr [rdi + 0xd], 2
003316CE  0F 84 D3 FA FF FF               je 0x1403311a7
003316D4  48 8B CF                        mov rcx, rdi
003316D7  E8 34 62 01 00                  call 0x140347910
003316DC  E9 C6 FA FF FF                  jmp 0x1403311a7
003316E1  48 83 E7 FB                     and rdi, 0xfffffffffffffffb
003316E5  E9 EA F7 FF FF                  jmp 0x140330ed4
003316EA  41 8B C7                        mov eax, r15d
003316ED  66 C7 47 0A 01 00               mov word ptr [rdi + 0xa], 1
003316F3  C1 E8 03                        shr eax, 3
003316F6  66 23 C3                        and ax, bx
003316F9  66 89 47 08                     mov word ptr [rdi + 8], ax
003316FD  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00331701  48 85 C0                        test rax, rax
00331704  0F 89 3B 02 00 00               jns 0x140331945
0033170A  80 67 0D FD                     and byte ptr [rdi + 0xd], 0xfd
0033170E  E9 A8 FA FF FF                  jmp 0x1403311bb
00331713  49 8B 07                        mov rax, qword ptr [r15]
00331716  49 23 C3                        and rax, r11
00331719  4C 8D 3C 40                     lea r15, [rax + rax*2]
0033171D  49 C1 E7 04                     shl r15, 4
00331721  48 8B C6                        mov rax, rsi
00331724  4C 03 F8                        add r15, rax
00331727  E9 68 FC FF FF                  jmp 0x140331394
0033172C  48 0F BA EF 08                  bts rdi, 8
00331731  E9 8C F7 FF FF                  jmp 0x140330ec2
00331736  48 83 CF 04                     or rdi, 4
0033173A  E9 70 F7 FF FF                  jmp 0x140330eaf
0033173F  90                              nop
00331740  FF C7                           inc edi
00331742  85 3D 64 3B C9 00               test dword ptr [rip + 0xc93b64], edi
00331748  0F 84 1D 04 00 00               je 0x140331b6b
0033174E  F3 90                           pause
00331750  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00331754  48 85 C0                        test rax, rax
00331757  0F 89 6B FB FF FF               jns 0x1403312c8
0033175D  EB E1                           jmp 0x140331740
0033175F  90                              nop
00331760  FF C7                           inc edi
00331762  85 3D 44 3B C9 00               test dword ptr [rip + 0xc93b44], edi
00331768  0F 84 24 04 00 00               je 0x140331b92
0033176E  F3 90                           pause
00331770  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00331774  48 85 C0                        test rax, rax
00331777  0F 89 D2 FD FF FF               jns 0x14033154f
0033177D  EB E1                           jmp 0x140331760
0033177F  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00331789  48 8B C0                        mov rax, rax
0033178C  48 3B D0                        cmp rdx, rax
0033178F  0F 87 FE F9 FF FF               ja 0x140331193
00331795  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0033179B  41 B9 04 00 00 00               mov r9d, 4
003317A1  A8 0F                           test al, 0xf
003317A3  44 0F 45 CE                     cmovne r9d, esi
003317A7  E9 ED F9 FF FF                  jmp 0x140331199
003317AC  48 0B C2                        or rax, rdx
003317AF  E9 83 FC FF FF                  jmp 0x140331437
003317B4  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003317B8  E9 80 FD FF FF                  jmp 0x14033153d
003317BD  49 8D 4E 10                     lea rcx, [r14 + 0x10]
003317C1  E8 DA 10 F5 FF                  call 0x1402828a0
003317C6  48 8B C8                        mov rcx, rax
003317C9  48 0F BA E0 0A                  bt rax, 0xa
003317CE  48 C7 C0 F7 FF FF FF            mov rax, 0xfffffffffffffff7
003317D5  48 C7 C2 FF F7 FF FF            mov rdx, 0xfffffffffffff7ff
003317DC  48 0F 42 C2                     cmovb rax, rdx
003317E0  48 23 C1                        and rax, rcx
003317E3  49 8B CE                        mov rcx, r14
003317E6  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
003317EA  0F B6 45 79                     movzx eax, byte ptr [rbp + 0x79]
003317EE  A8 10                           test al, 0x10
003317F0  0F 84 2D 02 00 00               je 0x140331a23
003317F6  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
003317F9  BA 08 00 00 00                  mov edx, 8
003317FE  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00331802  E8 F9 87 F8 FF                  call 0x1402ba000
00331807  E9 31 FD FF FF                  jmp 0x14033153d
0033180C  48 0B F1                        or rsi, rcx
0033180F  E9 4E FA FF FF                  jmp 0x140331262
00331814  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
00331818  49 8B CF                        mov rcx, r15
0033181B  48 C1 E2 04                     shl rdx, 4
0033181F  48 03 57 08                     add rdx, qword ptr [rdi + 8]
00331823  48 C1 E1 19                     shl rcx, 0x19
00331827  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00331831  48 8B C0                        mov rax, rax
00331834  48 C1 E0 19                     shl rax, 0x19
00331838  48 2B C8                        sub rcx, rax
0033183B  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0033183F  48 C1 E0 0C                     shl rax, 0xc
00331843  48 03 02                        add rax, qword ptr [rdx]
00331846  48 C1 F9 10                     sar rcx, 0x10
0033184A  48 3B C8                        cmp rcx, rax
0033184D  0F 85 E6 F7 FF FF               jne 0x140331039
00331853  80 3F 05                        cmp byte ptr [rdi], 5
00331856  0F 84 DD F7 FF FF               je 0x140331039
0033185C  48 8B CF                        mov rcx, rdi
0033185F  E8 3C 1F 03 00                  call 0x1403637a0
00331864  E9 D0 F7 FF FF                  jmp 0x140331039
00331869  8B 4D 97                        mov ecx, dword ptr [rbp - 0x69]
0033186C  83 E1 FB                        and ecx, 0xfffffffb
0033186F  E9 60 F9 FF FF                  jmp 0x1403311d4
00331874  48 B8 FF FF FF 7F FB F6 FF FF   movabs rax, 0xfffff6fb7fffffff
0033187E  4C 3B F8                        cmp r15, rax
00331881  0F 87 CD F5 FF FF               ja 0x140330e54
00331887  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00331891  4C 3B F8                        cmp r15, rax
00331894  0F 84 51 04 00 00               je 0x140331ceb
0033189A  0F BA E6 1A                     bt esi, 0x1a
0033189E  72 03                           jb 0x1403318a3
003318A0  48 23 F9                        and rdi, rcx
003318A3  49 8B CF                        mov rcx, r15
003318A6  E8 45 3F F9 FF                  call 0x1402c57f0
003318AB  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
003318AF  44 8B 55 9B                     mov r10d, dword ptr [rbp - 0x65]
003318B3  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
003318BD  85 C0                           test eax, eax
003318BF  74 04                           je 0x1403318c5
003318C1  48 83 CF 04                     or rdi, 4
003318C5  45 33 DB                        xor r11d, r11d
003318C8  E9 87 F5 FF FF                  jmp 0x140330e54
003318CD  BF 11 01 00 00                  mov edi, 0x111
003318D2  EB 0A                           jmp 0x1403318de
003318D4  40 F6 C6 04                     test sil, 4
003318D8  0F 85 5A 05 00 00               jne 0x140331e38
003318DE  80 7D 67 00                     cmp byte ptr [rbp + 0x67], 0
003318E2  0F 85 00 01 00 00               jne 0x1403319e8
003318E8  41 83 7C 24 24 00               cmp dword ptr [r12 + 0x24], 0
003318EE  74 42                           je 0x140331932
003318F0  44 8B 75 AB                     mov r14d, dword ptr [rbp - 0x55]
003318F4  45 85 F6                        test r14d, r14d
003318F7  74 22                           je 0x14033191b
003318F9  41 F7 04 24 00 01 00 00         test dword ptr [r12], 0x100
00331901  74 0F                           je 0x140331912
00331903  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00331907  41 8B CE                        mov ecx, r14d
0033190A  F0 48 01 88 88 02 00 00         lock add qword ptr [rax + 0x288], rcx
00331912  65 44 01 34 25 9C 2E 00 00      add dword ptr gs:[0x2e9c], r14d
0033191B  8B C7                           mov eax, edi
0033191D  48 81 C4 C8 00 00 00            add rsp, 0xc8
00331924  41 5F                           pop r15
00331926  41 5E                           pop r14
00331928  41 5D                           pop r13
0033192A  41 5C                           pop r12
0033192C  5F                              pop rdi
0033192D  5E                              pop rsi
0033192E  5B                              pop rbx
0033192F  5D                              pop rbp
00331930  C3                              ret
00331931  CC                              int3
00331932  8B 55 9B                        mov edx, dword ptr [rbp - 0x65]
00331935  85 D2                           test edx, edx
00331937  74 B7                           je 0x1403318f0
00331939  49 8B 4C 24 10                  mov rcx, qword ptr [r12 + 0x10]
0033193E  E8 AD 1B 0A 00                  call 0x1403d34f0
00331943  EB AB                           jmp 0x1403318f0
00331945  80 4F 0D 02                     or byte ptr [rdi + 0xd], 2
00331949  E9 6D F8 FF FF                  jmp 0x1403311bb
0033194E  41 8B 4C 24 20                  mov ecx, dword ptr [r12 + 0x20]
00331953  83 E1 1F                        and ecx, 0x1f
00331956  48 C1 E3 07                     shl rbx, 7
0033195A  48 0B CB                        or rcx, rbx
0033195D  48 83 C9 40                     or rcx, 0x40
00331961  48 C1 E1 05                     shl rcx, 5
00331965  E8 76 DC F5 FF                  call 0x14028f5e0
0033196A  49 8B CF                        mov rcx, r15
0033196D  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00331971  48 8B F8                        mov rdi, rax
00331974  8B DE                           mov ebx, esi
00331976  E8 85 E1 F0 FF                  call 0x14023fb00
0033197B  85 C0                           test eax, eax
0033197D  0F 85 B1 03 00 00               jne 0x140331d34
00331983  49 89 3F                        mov qword ptr [r15], rdi
00331986  85 DB                           test ebx, ebx
00331988  0F 85 BA 03 00 00               jne 0x140331d48
0033198E  41 F7 04 24 00 01 00 00         test dword ptr [r12], 0x100
00331996  0F 85 64 04 00 00               jne 0x140331e00
0033199C  8B FE                           mov edi, esi
0033199E  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
003319A5  0F 82 C5 00 00 00               jb 0x140331a70
003319AB  33 D2                           xor edx, edx
003319AD  49 8B CE                        mov rcx, r14
003319B0  E8 BB 25 00 00                  call 0x140333f70
003319B5  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003319BF  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003319C4  E9 49 F8 FF FF                  jmp 0x140331212
003319C9  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
003319CE  0F B6 41 45                     movzx eax, byte ptr [rcx + 0x45]
003319D2  A8 08                           test al, 8
003319D4  0F 85 64 F5 FF FF               jne 0x140330f3e
003319DA  0C 08                           or al, 8
003319DC  C6 45 67 01                     mov byte ptr [rbp + 0x67], 1
003319E0  88 41 45                        mov byte ptr [rcx + 0x45], al
003319E3  E9 56 F5 FF FF                  jmp 0x140330f3e
003319E8  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
003319ED  F6 41 45 08                     test byte ptr [rcx + 0x45], 8
003319F1  74 10                           je 0x140331a03
003319F3  66 83 79 42 00                  cmp word ptr [rcx + 0x42], 0
003319F8  74 09                           je 0x140331a03
003319FA  48 83 C1 38                     add rcx, 0x38
003319FE  E8 0D 5F 01 00                  call 0x140347910
00331A03  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00331A08  80 60 45 F7                     and byte ptr [rax + 0x45], 0xf7
00331A0C  E9 D7 FE FF FF                  jmp 0x1403318e8
00331A11  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00331A15  80 38 03                        cmp byte ptr [rax], 3
00331A18  0F 44 D3                        cmove edx, ebx
00331A1B  89 55 97                        mov dword ptr [rbp - 0x69], edx
00331A1E  E9 1C F3 FF FF                  jmp 0x140330d3f
00331A23  24 FA                           and al, 0xfa
00331A25  BA 04 00 00 00                  mov edx, 4
00331A2A  0C 02                           or al, 2
00331A2C  88 45 79                        mov byte ptr [rbp + 0x79], al
00331A2F  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00331A32  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00331A36  E8 C5 85 F8 FF                  call 0x1402ba000
00331A3B  E9 FD FA FF FF                  jmp 0x14033153d
00331A40  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00331A44  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00331A4A  49 8B C8                        mov rcx, r8
00331A4D  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00331A51  48 03 CA                        add rcx, rdx
00331A54  E9 58 F6 FF FF                  jmp 0x1403310b1
00331A59  48 0F BA 25 26 50 C9 00 24      bt qword ptr [rip + 0xc95026], 0x24
00331A62  0F 82 71 01 00 00               jb 0x140331bd9
00331A68  49 89 1F                        mov qword ptr [r15], rbx
00331A6B  E9 A2 F7 FF FF                  jmp 0x140331212
00331A70  FF C7                           inc edi
00331A72  85 3D 34 38 C9 00               test dword ptr [rip + 0xc93834], edi
00331A78  0F 84 46 02 00 00               je 0x140331cc4
00331A7E  F3 90                           pause
00331A80  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00331A84  48 85 C0                        test rax, rax
00331A87  0F 89 11 FF FF FF               jns 0x14033199e
00331A8D  EB E1                           jmp 0x140331a70
00331A8F  85 C0                           test eax, eax
00331A91  0F 85 A1 00 00 00               jne 0x140331b38
00331A97  0F B6 45 79                     movzx eax, byte ptr [rbp + 0x79]
00331A9B  A8 10                           test al, 0x10
00331A9D  0F 84 7C 02 00 00               je 0x140331d1f
00331AA3  24 FB                           and al, 0xfb
00331AA5  0C 03                           or al, 3
00331AA7  88 45 79                        mov byte ptr [rbp + 0x79], al
00331AAA  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00331AAD  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00331AB1  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00331AB5  48 0F BA E0 0A                  bt rax, 0xa
00331ABA  0F 82 7D FA FF FF               jb 0x14033153d
00331AC0  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00331AC4  E8 67 DA 03 00                  call 0x14036f530
00331AC9  85 C0                           test eax, eax
00331ACB  0F 84 6C FA FF FF               je 0x14033153d
00331AD1  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00331AD5  48 8B 0D AC E5 AF 00            mov rcx, qword ptr [rip + 0xafe5ac]
00331ADC  48 C1 E8 2B                     shr rax, 0x2b
00331AE0  25 FF 03 00 00                  and eax, 0x3ff
00331AE5  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00331AE9  C6 82 D3 02 00 00 01            mov byte ptr [rdx + 0x2d3], 1
00331AF0  E9 48 FA FF FF                  jmp 0x14033153d
00331AF5  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00331AF9  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00331AFD  48 83 E0 FB                     and rax, 0xfffffffffffffffb
00331B01  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00331B05  E8 82 9B FF FF                  call 0x14032b68c
00331B0A  E9 DD F7 FF FF                  jmp 0x1403312ec
00331B0F  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
00331B12  85 C0                           test eax, eax
00331B14  0F 84 1D 01 00 00               je 0x140331c37
00331B1A  83 F8 02                        cmp eax, 2
00331B1D  0F 85 D9 F5 FF FF               jne 0x1403310fc
00331B23  E9 F0 02 00 00                  jmp 0x140331e18
00331B28  41 B8 01 00 00 00               mov r8d, 1
00331B2E  E8 9D 24 F5 FF                  call 0x140283fd0
00331B33  E9 D6 F9 FF FF                  jmp 0x14033150e
00331B38  80 4D 79 07                     or byte ptr [rbp + 0x79], 7
00331B3C  E9 69 FF FF FF                  jmp 0x140331aaa
00331B41  48 85 C9                        test rcx, rcx
00331B44  0F 85 78 F4 FF FF               jne 0x140330fc2
00331B4A  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00331B4E  E8 4D 0D F5 FF                  call 0x1402828a0
00331B53  48 83 C8 40                     or rax, 0x40
00331B57  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00331B5B  48 8B D0                        mov rdx, rax
00331B5E  E8 AD FC F4 FF                  call 0x140281810
00331B63  45 33 DB                        xor r11d, r11d
00331B66  E9 57 F4 FF FF                  jmp 0x140330fc2
00331B6B  8B 05 47 4F C9 00               mov eax, dword ptr [rip + 0xc94f47]
00331B71  A8 40                           test al, 0x40
00331B73  0F 84 D5 FB FF FF               je 0x14033174e
00331B79  E8 12 D9 FD FF                  call 0x14030f490
00331B7E  84 C0                           test al, al
00331B80  0F 84 C8 FB FF FF               je 0x14033174e
00331B86  8B CF                           mov ecx, edi
00331B88  E8 D3 D8 FD FF                  call 0x14030f460
00331B8D  E9 BE FB FF FF                  jmp 0x140331750
00331B92  8B 05 20 4F C9 00               mov eax, dword ptr [rip + 0xc94f20]
00331B98  A8 40                           test al, 0x40
00331B9A  0F 84 CE FB FF FF               je 0x14033176e
00331BA0  E8 EB D8 FD FF                  call 0x14030f490
00331BA5  84 C0                           test al, al
00331BA7  0F 84 C1 FB FF FF               je 0x14033176e
00331BAD  8B CF                           mov ecx, edi
00331BAF  E8 AC D8 FD FF                  call 0x14030f460
00331BB4  E9 B7 FB FF FF                  jmp 0x140331770
00331BB9  49 8B C1                        mov rax, r9
00331BBC  48 03 C1                        add rax, rcx
00331BBF  4C 3B F8                        cmp r15, rax
00331BC2  0F 87 0B F2 FF FF               ja 0x140330dd3
00331BC8  49 8B C1                        mov rax, r9
00331BCB  4C 3B F8                        cmp r15, rax
00331BCE  0F 83 06 F2 FF FF               jae 0x140330dda
00331BD4  E9 FA F1 FF FF                  jmp 0x140330dd3
00331BD9  F6 C3 20                        test bl, 0x20
00331BDC  0F 85 86 FE FF FF               jne 0x140331a68
00331BE2  49 8B C0                        mov rax, r8
00331BE5  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00331BEF  48 03 C1                        add rax, rcx
00331BF2  4C 3B F8                        cmp r15, rax
00331BF5  0F 82 6D FE FF FF               jb 0x140331a68
00331BFB  41 B8 80 00 00 00               mov r8d, 0x80
00331C01  48 8B D3                        mov rdx, rbx
00331C04  49 8B CF                        mov rcx, r15
00331C07  E8 74 11 F6 FF                  call 0x140292d80
00331C0C  E9 57 FE FF FF                  jmp 0x140331a68
00331C11  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00331C15  A8 01                           test al, 1
00331C17  74 0D                           je 0x140331c26
00331C19  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00331C1D  80 38 02                        cmp byte ptr [rax], 2
00331C20  0F 84 AA F5 FF FF               je 0x1403311d0
00331C26  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00331C2A  48 83 E3 DF                     and rbx, 0xffffffffffffffdf
00331C2E  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
00331C32  E9 9D F5 FF FF                  jmp 0x1403311d4
00331C37  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
00331C3B  48 85 C0                        test rax, rax
00331C3E  0F 84 1D 01 00 00               je 0x140331d61
00331C44  48 8B F8                        mov rdi, rax
00331C47  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00331C4A  25 00 00 60 00                  and eax, 0x600000
00331C4F  3D 00 00 60 00                  cmp eax, 0x600000
00331C54  0F 84 B7 01 00 00               je 0x140331e11
00331C5A  C7 45 A7 01 00 00 00            mov dword ptr [rbp - 0x59], 1
00331C61  E9 96 F4 FF FF                  jmp 0x1403310fc
00331C66  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00331C6A  E8 F9 2E F6 FF                  call 0x140294b68
00331C6F  48 8B 7D CF                     mov rdi, qword ptr [rbp - 0x31]
00331C73  8B D8                           mov ebx, eax
00331C75  E9 02 F6 FF FF                  jmp 0x14033127c
00331C7A  41 8B FB                        mov edi, r11d
00331C7D  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00331C84  72 7A                           jb 0x140331d00
00331C86  BA 04 00 00 00                  mov edx, 4
00331C8B  49 8B CE                        mov rcx, r14
00331C8E  E8 BD 06 F7 FF                  call 0x1402a2350
00331C93  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00331C9D  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00331CA2  E9 4D F9 FF FF                  jmp 0x1403315f4
00331CA7  48 8B D7                        mov rdx, rdi
00331CAA  49 8B CF                        mov rcx, r15
00331CAD  E8 FA 31 F6 FF                  call 0x140294eac
00331CB2  45 33 DB                        xor r11d, r11d
00331CB5  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
00331CBF  E9 FE F2 FF FF                  jmp 0x140330fc2
00331CC4  8B 05 EE 4D C9 00               mov eax, dword ptr [rip + 0xc94dee]
00331CCA  A8 40                           test al, 0x40
00331CCC  0F 84 AC FD FF FF               je 0x140331a7e
00331CD2  E8 B9 D7 FD FF                  call 0x14030f490
00331CD7  84 C0                           test al, al
00331CD9  0F 84 9F FD FF FF               je 0x140331a7e
00331CDF  8B CF                           mov ecx, edi
00331CE1  E8 7A D7 FD FF                  call 0x14030f460
00331CE6  E9 95 FD FF FF                  jmp 0x140331a80
00331CEB  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00331CF5  48 0B F8                        or rdi, rax
00331CF8  E9 A6 FB FF FF                  jmp 0x1403318a3
00331CFD  0F 1F 00                        nop dword ptr [rax]
00331D00  FF C7                           inc edi
00331D02  85 3D A4 35 C9 00               test dword ptr [rip + 0xc935a4], edi
00331D08  0F 84 88 00 00 00               je 0x140331d96
00331D0E  F3 90                           pause
00331D10  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00331D14  48 85 C0                        test rax, rax
00331D17  0F 89 60 FF FF FF               jns 0x140331c7d
00331D1D  EB E1                           jmp 0x140331d00
00331D1F  A8 08                           test al, 8
00331D21  75 35                           jne 0x140331d58
00331D23  24 FA                           and al, 0xfa
00331D25  0C 02                           or al, 2
00331D27  E9 7B FD FF FF                  jmp 0x140331aa7
00331D2C  49 8B F3                        mov rsi, r11
00331D2F  E9 C0 F8 FF FF                  jmp 0x1403315f4
00331D34  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00331D38  E8 2B 2E F6 FF                  call 0x140294b68
00331D3D  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
00331D41  8B D8                           mov ebx, eax
00331D43  E9 3B FC FF FF                  jmp 0x140331983
00331D48  48 8B D7                        mov rdx, rdi
00331D4B  49 8B CF                        mov rcx, r15
00331D4E  E8 59 31 F6 FF                  call 0x140294eac
00331D53  E9 36 FC FF FF                  jmp 0x14033198e
00331D58  24 FB                           and al, 0xfb
00331D5A  0C 03                           or al, 3
00331D5C  E9 46 FD FF FF                  jmp 0x140331aa7
00331D61  BB 01 00 00 00                  mov ebx, 1
00331D66  8B CB                           mov ecx, ebx
00331D68  E8 83 A3 F4 FF                  call 0x14027c0f0
00331D6D  49 8B 4C 24 10                  mov rcx, qword ptr [r12 + 0x10]
00331D72  E8 59 4B FE FF                  call 0x1403168d0
00331D77  B2 11                           mov dl, 0x11
00331D79  8B CB                           mov ecx, ebx
00331D7B  48 8B F8                        mov rdi, rax
00331D7E  E8 9D 52 F6 FF                  call 0x140297020
00331D83  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00331D87  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00331D91  E9 B1 FE FF FF                  jmp 0x140331c47
00331D96  8B 05 1C 4D C9 00               mov eax, dword ptr [rip + 0xc94d1c]
00331D9C  A8 40                           test al, 0x40
00331D9E  0F 84 6A FF FF FF               je 0x140331d0e
00331DA4  E8 E7 D6 FD FF                  call 0x14030f490
00331DA9  84 C0                           test al, al
00331DAB  0F 84 5D FF FF FF               je 0x140331d0e
00331DB1  8B CF                           mov ecx, edi
00331DB3  E8 A8 D6 FD FF                  call 0x14030f460
00331DB8  E9 53 FF FF FF                  jmp 0x140331d10
00331DBD  48 8B CE                        mov rcx, rsi
00331DC0  4C 2B F9                        sub r15, rcx
00331DC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00331DC8  49 C1 FF 04                     sar r15, 4
00331DCC  BA 06 00 00 00                  mov edx, 6
00331DD1  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
00331DDB  4D 8B CA                        mov r9, r10
00331DDE  4D 0F AF C7                     imul r8, r15
00331DE2  8D 4A 48                        lea ecx, [rdx + 0x48]
00331DE5  E8 76 B8 1C 00                  call 0x1404fd660
00331DEA  CC                              int3
00331DEB  80 E3 05                        and bl, 5
00331DEE  80 FB 04                        cmp bl, 4
00331DF1  0F 85 D3 F0 FF FF               jne 0x140330eca
00331DF7  48 83 CF 42                     or rdi, 0x42
00331DFB  E9 CA F0 FF FF                  jmp 0x140330eca
00331E00  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00331E04  F0 48 FF 80 88 02 00 00         lock inc qword ptr [rax + 0x288]
00331E0C  E9 8B FB FF FF                  jmp 0x14033199c
00331E11  C7 45 A7 02 00 00 00            mov dword ptr [rbp - 0x59], 2
00331E18  48 83 E3 BD                     and rbx, 0xffffffffffffffbd
00331E1C  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
00331E20  E9 D7 F2 FF FF                  jmp 0x1403310fc
00331E25  49 8B CE                        mov rcx, r14
00331E28  E8 CB F0 03 00                  call 0x140370ef8
00331E2D  CC                              int3
00331E2E  24 EF                           and al, 0xef
00331E30  88 45 7A                        mov byte ptr [rbp + 0x7a], al
00331E33  E9 8B F6 FF FF                  jmp 0x1403314c3
00331E38  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00331E3D  B9 FF FF 00 00                  mov ecx, 0xffff
00331E42  66 01 48 42                     add word ptr [rax + 0x42], cx
00331E46  E9 93 FA FF FF                  jmp 0x1403318de
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCompletePrivateZeroFault(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p1A;
    unsigned __int8 v_stack_p1B;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (200);
    v_r15 = (*(unsigned __int64 *)(a1 + 16)) >> (9);
    v_r15 = (v_r15) & (v_r10);
    v_stack_m88 = *(unsigned __int64 *)(a1 + 56);
    v_r15 = (v_r15) + (a4);
    v_r11 = 0;
    v_stack_p8 = 0;
    v_stack_mC8 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 56);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 16)))) != 0) goto loc_00331A11;
loc_00330D3F:
    result = 0;
    if (((*(unsigned __int8 *)(a1)) & (32)) != 0) { result = *(unsigned __int64 *)(a1 + 56); }
    v_stack_m80 = result;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) >> (9);
    a1 = (a1) & (v_r10);
    v_stack_m98 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    a1 = (a1) + (a4);
    v_stack_mB8 = 0;
    v_stack_m70 = a1;
    v_stack_m68 = *(unsigned __int64 *)(a1 + 64);
    v_stack_p20 = (unsigned int)((unsigned int)(0x2010ULL));
    v_rdi = (unsigned int)(0x2010ULL);
    if (*(unsigned __int64 *)(a1 + 64) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 52);
        a2 = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 34);
        a2 = (a2) << (32);
        a2 = (a2) | (a1);
        a1 = 0x2050ULL;
        v_rdi = (unsigned int)(0x2010ULL);
        if (a2 == (*(unsigned __int64 *)(a1 + 64))) { v_rdi = (unsigned int)(a1); }
        v_stack_p20 = (unsigned int)(v_rdi);
    }
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (2)) != 0) goto loc_00331BB9;
loc_00330DD3:
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
loc_00330DDA:
    if ((*(unsigned int *)(a1 + 36)) == 0) {
    }
    v_stack_mC4 = 0;
    v_stack_mB4 = 0;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (31));
    v_rdi = (*(unsigned __int64 *)(v_rip - 3277926 + v_rbx * 8)) & (v_rip - 3277926);
    v_rdi = (v_rdi) | (33);
    if (v_r15 < a4) goto loc_0033172C;
    if (v_r15 > a4) goto loc_0033172C;
    if (v_r15 >= a4) goto loc_00331874;
loc_00330E54:
    a2 = (v_r14) << (25);
    a1 = (v_r15) << (25);
    a1 = (a1) - (a2);
    a1 = (a1) >> (16);
    if (condition_is_above_or_equal) goto loc_00330E9C;
    if (a1 < v_r14) goto loc_00330E9C;
loc_00330E81:
    if (a1 > a4) goto loc_00330E9C;
    a1 = (a1) << (25);
    a1 = (a1) - (a2);
    a1 = (a1) >> (16);
    if (a1 >= v_r14) goto loc_00330E81;
loc_00330E9C:
    if (a1 <= v_r14) goto loc_00331736;
loc_00330EAF:
    result = MiIsAddressGlobal(a1, v_rdi, a3, a4);
    if ((unsigned int)(result) == 0) { v_rdi = v_rdi; }
loc_00330EC2:
    if (sign_flag) goto loc_00331DEB;
loc_00330ECA:
    if (condition_is_below) goto loc_003316E1;
loc_00330ED4:
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int8 *)(v_rip + 11526048);
        result = (result) << (8);
        v_rdi = result;
        v_rdi = (v_rdi) ^ (v_rdi);
        v_rdi = (v_rdi) ^ (result);
    }
    a2 = v_rdi;
    if (condition_is_above_or_equal) {
        a2 = v_rdi;
        a2 = a2;
    }
    a1 = (a2) & (result);
    a1 = (a1) | (result);
    v_stack_mC0 = a1;
    if (a3 > 1) goto loc_003319C9;
loc_00330F3E:
loc_00330F41:
    v_stack_mB0 = 0;
    if (0 >= a3) goto loc_003318CD;
    if (v_r15 < a2) goto loc_00330FA4;
    if (v_r15 > a4) goto loc_00330FA4;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_00330FA4;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00331664;
loc_00330FA0:
loc_00330FA4:
    if ((*(unsigned int *)(a1 + 36)) == 0) goto loc_0033122D;
    if ((*(unsigned int *)(a1 + 36)) < 0) goto loc_00330FC2;
    if ((*(unsigned int *)(a1 + 36)) < 0) goto loc_00331B41;
loc_00330FC2:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00330FDD;
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2));
    if (*(unsigned __int64 *)(a2) == 0) {
        *(unsigned __int64 *)(a2 + 8) = 0;
    }
    v_rbx = (*(unsigned __int64 *)(a2)) - (v_rdi);
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * (v_rdi);
    if ((*(unsigned int *)(a1 + 36)) != 0) goto loc_003315A0;
loc_00331004:
    v_rsi = 0;
loc_00331009:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p20)))) | (32));
    if (((*(unsigned __int8 *)(a1)) & (2)) == 0) { a2 = (unsigned int)((unsigned int)(v_stack_p20)); }
    v_stack_p20 = (unsigned int)(a2);
    result = MiInitializePfn(*(unsigned __int64 *)(a2), v_r15, (unsigned int)(*(unsigned int *)(a1 + 32)), (unsigned int)((unsigned int)(a2)));
    if (v_stack_m88 != 0) goto loc_00331814;
loc_00331039:
    v_rbx = (v_rbx) & (result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (16)) != 0) goto loc_0033194E;
    result = (v_stack_mC0) & (v_r15);
    v_rbx = (v_rbx) << (12);
    v_rbx = (v_rbx) | (result);
    v_rbx = (v_rbx) & (-33);
    result = (v_rbx) | (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) { v_rbx = result; }
    v_stack_mC0 = v_rbx;
    if (v_r15 > ((unsigned int)(*(unsigned int *)(a1 + 32)) + v_r15 * 1)) goto loc_00331A40;
    if (v_r15 < ((unsigned int)(*(unsigned int *)(a1 + 32)))) goto loc_00331A40;
loc_003310B1:
    if ((*(unsigned __int64 *)(a1 + 72)) != 0) goto loc_00331A59;
    if (v_r15 == v_stack_m70) goto loc_003310FC;
    if (((*(unsigned int *)(a1)) & (512)) == 0) goto loc_003310FC;
    v_rbx = (v_rbx) & (-33);
    v_stack_mC0 = v_rbx;
    if (v_stack_mA8 >= 0) goto loc_003310FC;
    if (v_r15 > ((unsigned int)(*(unsigned int *)(a1 + 32)) + v_r15 * 1)) goto loc_003310FC;
    if (v_r15 < ((unsigned int)(*(unsigned int *)(a1 + 32)))) goto loc_003310FC;
    if (((*(unsigned int *)(v_stack_m98 + 500)) & (0x8000ULL)) != 0) goto loc_00331B0F;
loc_003310FC:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69))) & (9));
    if (((unsigned __int8)(result)) != 8) goto loc_00331869;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69))) & (4)) != 0) goto loc_00331869;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10)) == 0) goto loc_003311A7;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10)))) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 8))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (3));
    result = (unsigned int)((result) & (511));
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_003316D4;
    if (sign_flag) goto loc_003316CA;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 13)) & (2)) != 0) goto loc_003311A7;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 16)) << (25);
    result = ((unsigned int)(*(unsigned int *)(a1 + 32))) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    a2 = (a2) << (25);
    a2 = (a2) - (result);
    result = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 8)) << (12);
    a2 = (a2) >> (16);
    a2 = (a2) + (result);
    if (a2 >= ((unsigned int)(*(unsigned int *)(a1 + 32)))) goto loc_0033177F;
loc_00331193:
loc_00331199:
    result = MiAddWorkingSetEntries(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 56), a2, *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10), 5);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10) = 0;
loc_003311A7:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10)) == 0) goto loc_003316EA;
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10)) + 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 56 + 10) = (unsigned __int16)(result);
loc_003311BB:
    a1 = (unsigned int)(((unsigned int)(v_stack_mC8)) | (4));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69)) & (16)) != 0) goto loc_00331C11;
loc_003311D0:
loc_003311D4:
    v_stack_mD8 = v_stack_m80;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (16));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69)) & (1)) == 0) { v_rsi = (unsigned int)(a1); }
    v_stack_mE0 = (unsigned int)(v_rsi);
    a4 = 0;
    v_stack_mE8 = v_stack_mC0;
    v_stack_mC8 = (unsigned int)(v_rsi);
    result = MiAllocateWsle(v_stack_mA0, v_r15, *(unsigned __int64 *)(a2), a4);
    if ((unsigned int)(result) == 0) goto loc_00331299;
loc_00331212:
    v_r15 = (v_r15) + (8);
    a1 = (v_stack_mB0) + 1;
    v_r11 = 0;
    goto loc_00330F41;
loc_0033122D:
    if (v_rsi != 0) goto loc_00330FC2;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mC4)) + 1);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (31));
    v_rsi = (v_rsi) << (5);
    v_stack_mC4 = (unsigned int)(v_r10);
    if (*(unsigned __int64 *)(v_rip + 11520571) == 0) goto loc_00331262;
    if (((v_rsi) & (*(unsigned __int64 *)(v_rip + 11520571))) == 0) goto loc_0033180C;
    v_rsi = (v_rsi) | (16);
loc_00331262:
    v_stack_m90 = v_rsi;
    result = MiPteInShadowRange(v_r15, v_r15, v_stack_p18, a4);
    if ((unsigned int)(result) != 0) goto loc_00331C66;
loc_0033127C:
    *(unsigned __int64 *)(v_r15) = v_rsi;
    if (0 != 0) goto loc_00331CA7;
    v_r11 = 0;
    goto loc_00330FC2;
loc_00331299:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 40)) & (0);
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (result);
    v_r15 = 0;
loc_003312C8:
    if (condition_is_below) goto loc_00331740;
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16);
    result = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00331AF5;
    v_stack_mA0 = 0;
loc_003312EC:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16)) & (-3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24)) | (0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24) = result;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2) + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_00331E25;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24)) & (0);
    a2 = (a2) - 1;
    a1 = (a2) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24));
    a1 = (a1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24) = a1;
    if (a2 != 0) goto loc_003317B4;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 32)));
    if (!sign_flag) goto loc_00331499;
    v_rsi = 0;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16)) >> (5);
    v_stack_p20 = a4;
loc_00331394:
    if (0 >= 1) goto loc_0033144B;
    v_rsi = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8)) >> (3));
    v_rsi = (unsigned int)((v_rsi) & (511));
    result = 511;
    v_rdi = 0;
    if (0 == 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 40);
        a2 = 0;
        a1 = (a1) & (0);
        a3 = 0x80000000ULL;
        result = MiMapPageInHyperSpaceWorker(a1, a2, a3, a4);
        a4 = v_stack_p20;
        v_rdi = result;
    }
    a3 = (*(unsigned __int64 *)(v_rdi + v_rsi * 8)) >> (12);
    a3 = (a3) & (0);
    a2 = (a3 + a3 * 2) << (4);
    a2 = (a2) + (v_rsi);
    if (a2 != (*(unsigned __int64 *)(a2))) goto loc_00331DBD;
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (31));
    a3 = (a3) << (7);
    result = (result) | (a3);
    result = (result) | (64);
    result = (result) << (5);
    if (*(unsigned __int64 *)(v_rip + 11520112) == 0) goto loc_00331437;
    if (((result) & (*(unsigned __int64 *)(v_rip + 11520112))) == 0) goto loc_003317AC;
    result = (result) | (16);
loc_00331437:
    *(unsigned __int64 *)(v_rdi + v_rsi * 8) = result;
    if ((0 + 1) != 1) goto loc_00331713;
loc_0033144B:
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & (0 + 1);
    v_rdi = (v_rdi) + (0 + 1);
    v_r15 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872)) = 0;
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_rip - 3279891);
loc_00331499:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24)) >> (62);
    result = (unsigned int)((result) & (1));
    if (condition_is_not_equal) goto loc_00331A8F;
    if ((unsigned int)(result) == 0) goto loc_003317BD;
    if ((((unsigned __int8)(v_stack_p1B)) & (16)) != 0) goto loc_00331E2E;
loc_003314C3:
    *(unsigned int *)(*(unsigned __int64 *)(a2) + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16);
    if (condition_is_below) goto loc_0033150E;
    result = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00331505;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m88)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0033150E;
loc_00331505:
    if (v_stack_m88 != 0) goto loc_00331B28;
loc_0033150E:
    a1 = (*(unsigned __int64 *)(a2)) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    result = MiInsertPageInFreeOrZeroedList(a1, 2, (unsigned int)(0xFFFFULL), a4);
loc_0033153D:
loc_0033154F:
    if (condition_is_below) goto loc_00331760;
    a2 = 0;
    result = MiDecrementShareCountEx(v_rbx, a2, (unsigned int)(0xFFFFULL), a4);
loc_0033157A:
    if (*(unsigned __int64 *)(v_stack_p10) == 0) goto loc_003318D4;
    *(unsigned __int64 *)(v_stack_p10) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10));
    if (*(unsigned __int64 *)(v_stack_p10) == 0) {
        *(unsigned __int64 *)(v_stack_p10 + 8) = 0;
    }
    result = MiReleaseFreshPage(*(unsigned __int64 *)(v_stack_p10), a2, (unsigned int)(0xFFFFULL), a4);
    goto loc_0033157A;
loc_003315A0:
    if ((*(unsigned __int64 *)(a1 + 72)) != 0) goto loc_00331004;
    if ((*(unsigned __int64 *)(a1 + 72)) >= 0) goto loc_00331004;
    if (*(unsigned __int64 *)(v_rip + 11519682) == 0) goto loc_003315D5;
    result = (unsigned int)(v_stack_mC8);
    if ((((unsigned __int8)((unsigned int)(v_stack_mC8))) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 11519682);
        result = ~(result);
        result = (result) & ((unsigned int)(v_stack_mC8));
    }
    result = (result) >> (16);
    if (result != 0) goto loc_00331C7A;
    if ((((unsigned int)(v_stack_mC8)) & (992)) == 0) goto loc_00331D2C;
loc_003315F4:
    a2 = 0;
    v_rsi = ((unsigned int)(v_stack_mC8)) & (-3);
    result = MiMapPageInHyperSpaceWorker(v_rbx, a2, (unsigned int)(0x80000000ULL), a4);
    a2 = (result) >> (9);
    a2 = (a2) & (v_rsi);
    a2 = (a2) + (v_rsi);
    v_rsi = 0;
    a1 = (unsigned int)(((unsigned int)(v_stack_p20)) | (8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872)) = 0;
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(v_rip - 3280348);
    goto loc_00331009;
loc_00331664:
    if (((*(unsigned __int64 *)(v_rip + 13194265)) & (0x600000ULL)) == 0) goto loc_00330FA0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00330FA0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00330FA0;
    result = (0) >> (3);
    result = (result) & (v_rbx);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rsi = (v_rsi) | (32);
    }
    v_rsi = (v_rsi) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rsi = v_rsi; }
    goto loc_00330FA0;
loc_003316CA:
    if (((*(unsigned __int8 *)(result + 13)) & (2)) == 0) goto loc_003311A7;
loc_003316D4:
    result = MiEmptyDeferredWorkingSetEntries(result, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), (unsigned int)(0x80000000ULL), a4);
    goto loc_003311A7;
loc_003316E1:
    v_rdi = (result) & (-5);
    goto loc_00330ED4;
loc_003316EA:
    *(unsigned __int16 *)(v_rdi + 10) = 1;
    result = (unsigned int)((0) >> (3));
    result = (unsigned __int16)((result) & ((unsigned __int16)(v_rbx)));
    *(unsigned __int16 *)(v_rdi + 8) = (unsigned __int16)(result);
    if (!sign_flag) goto loc_00331945;
    goto loc_003311BB;
loc_00331713:
    result = (*(unsigned __int64 *)(v_r15)) & (0);
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + (v_rsi);
    goto loc_00331394;
loc_0033172C:
    goto loc_00330EC2;
loc_00331736:
    v_rdi = (v_rdi) | (4);
    goto loc_00330EAF;
loc_00331740:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13187940)) & ((unsigned int)(v_rdi))) == 0) goto loc_00331B6B;
loc_0033174E:
loc_00331750:
    if (!sign_flag) goto loc_003312C8;
    goto loc_00331740;
loc_00331760:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13187908)) & ((unsigned int)(v_rdi))) == 0) goto loc_00331B92;
loc_0033176E:
loc_00331770:
    if (!sign_flag) goto loc_0033154F;
    goto loc_00331760;
loc_0033177F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288)) > (*(unsigned __int64 *)(v_rbx + 24))) goto loc_00331193;
    a4 = 4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (15)) != 0) { a4 = (unsigned int)(v_rsi); }
    goto loc_00331199;
loc_003317AC:
    result = ((unsigned int)(*(unsigned int *)(result + 184))) | (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
    goto loc_00331437;
loc_003317B4:
    goto loc_0033153D;
loc_003317BD:
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(a2) + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), (unsigned int)(0x80000000ULL), a4);
    result = -9;
    if (condition_is_below) { result = 0xFFFFFFFFFFFFF7FFULL; }
    result = (result) & (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) = result;
    if ((((unsigned __int8)(v_stack_p1A)) & (16)) == 0) goto loc_00331A23;
    *(unsigned int *)(*(unsigned __int64 *)(a2) + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    result = MiInsertPageInList(*(unsigned __int64 *)(a2), 8, (unsigned int)(0x80000000ULL), a4);
    goto loc_0033153D;
loc_0033180C:
    v_rsi = (v_rsi) | (*(unsigned __int64 *)(a2));
    goto loc_00331262;
loc_00331814:
    a2 = (*(unsigned __int64 *)(v_rdi + 24)) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rdi + 8));
    a1 = (v_r15) << (25);
    result = (result) << (25);
    a1 = (a1) - (result);
    result = (*(unsigned __int64 *)(v_rdi + 32)) << (12);
    result = (result) + (*(unsigned __int64 *)(a2));
    a1 = (a1) >> (16);
    if (a1 != result) goto loc_00331039;
    if ((*(unsigned __int8 *)(v_rdi)) == 5) goto loc_00331039;
    result = MiAdvanceFaultList(v_rdi, a2, (unsigned int)(0x80000000ULL), a4);
    goto loc_00331039;
loc_00331869:
    a1 = (unsigned int)(((unsigned int)(v_stack_mC8)) & (0xFFFFFFFBULL));
    goto loc_003311D4;
loc_00331874:
    if (v_r15 > result) goto loc_00330E54;
    if (v_r15 == result) goto loc_00331CEB;
    if (v_r15 >= result) {
        v_rdi = (v_rdi) & (a1);
    }
    result = MiUserPdeOrAbove(v_r15, a2, (unsigned int)(0x80000000ULL), a4);
    if ((unsigned int)(result) != 0) {
        v_rdi = (v_rdi) | (4);
    }
    v_r11 = 0;
    goto loc_00330E54;
loc_003318CD:
    goto loc_003318DE;
loc_003318D4:
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_00331E38;
loc_003318DE:
    if (v_stack_p8 != 0) goto loc_003319E8;
loc_003318E8:
    if ((*(unsigned int *)(a1 + 36)) == 0) goto loc_00331932;
loc_003318F0:
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_0033191B;
    if (((*(unsigned int *)(a1)) & (256)) != 0) {
        result = v_stack_m98;
        a1 = (unsigned int)((unsigned int)(v_stack_mB4));
    }
loc_0033191B:
    v_rsp = (v_rsp) + (200);
    return 273;
loc_00331932:
    if ((unsigned int)((unsigned int)(v_stack_mC4)) == 0) goto loc_003318F0;
    result = MiUpdatePageTableUseCount(*(unsigned __int64 *)(a1 + 16), (unsigned int)(v_stack_mC4), v_stack_p18, a4);
    goto loc_003318F0;
loc_00331945:
    goto loc_003311BB;
loc_0033194E:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (31));
    v_rbx = (v_rbx) << (7);
    a1 = (a1) | (v_rbx);
    a1 = (a1) | (64);
    a1 = (a1) << (5);
    result = MiSwizzleInvalidPte(a1, (unsigned int)(v_stack_mC4), v_stack_p18, a4);
    v_stack_m78 = result;
    result = MiPteInShadowRange(v_r15, (unsigned int)(v_stack_mC4), v_stack_p18, a4);
    if ((unsigned int)(result) != 0) goto loc_00331D34;
loc_00331983:
    *(unsigned __int64 *)(v_r15) = result;
    if ((unsigned int)((unsigned int)((unsigned int)(v_rsi))) != 0) goto loc_00331D48;
loc_0033198E:
    if (((*(unsigned int *)(a1)) & (256)) != 0) goto loc_00331E00;
loc_0033199C:
loc_0033199E:
    if (condition_is_below) goto loc_00331A70;
    a2 = 0;
    result = MiDecrementShareCountEx((unsigned int)(v_stack_mB4), a2, v_stack_p18, a4);
    goto loc_00331212;
loc_003319C9:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69))) & (8)) != 0) goto loc_00330F3E;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69)) | (8));
    v_stack_p8 = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69) = (unsigned __int8)(result);
    goto loc_00330F3E;
loc_003319E8:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 69)) & (8)) == 0) goto loc_00331A03;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 8)) + (56);
        result = MiEmptyDeferredWorkingSetEntries(a1, a2, v_stack_p18, a4);
    }
    goto loc_003318E8;
loc_00331A11:
    result = (*(unsigned __int64 *)(a1 + 8)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 3) { a2 = (unsigned int)((unsigned int)((unsigned int)(v_rsi))); }
    v_stack_mC8 = (unsigned int)(a2);
    goto loc_00330D3F;
loc_00331A23:
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_p1A = (unsigned __int8)(result);
    *(unsigned int *)((unsigned int)(v_stack_mB4) + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    result = MiInsertPageInList(a1, 4, v_stack_p18, a4);
    goto loc_0033153D;
loc_00331A40:
    a1 = (v_stack_p18) + (4);
    goto loc_003310B1;
loc_00331A59:
    if (condition_is_below) goto loc_00331BD9;
loc_00331A68:
    *(unsigned __int64 *)(v_r15) = v_stack_mC0;
    goto loc_00331212;
loc_00331A70:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + 1);
    if (((*(unsigned int *)(v_rip + 13187124)) & ((unsigned int)(v_rdi))) == 0) goto loc_00331CC4;
loc_00331A7E:
loc_00331A80:
    if (!sign_flag) goto loc_0033199E;
    goto loc_00331A70;
loc_00331A8F:
    if ((unsigned int)(*(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 24)) != 0) goto loc_00331B38;
    if ((((unsigned __int8)(v_stack_p1A)) & (16)) == 0) goto loc_00331D1F;
    result = (unsigned __int8)((v_stack_p1A) & (251));
    result = (unsigned __int8)((result) | (3));
loc_00331AA7:
    v_stack_p1A = (unsigned __int8)(result);
loc_00331AAA:
    *(unsigned int *)((unsigned int)(v_stack_mB4) + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    if (condition_is_below) goto loc_0033153D;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 16), 4, v_stack_p18, a4);
    if ((unsigned int)(result) == 0) goto loc_0033153D;
    result = (*(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11527596) + result * 8) + 723) = 1;
    goto loc_0033153D;
loc_00331AF5:
    result = (*(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 16)) & (-5);
    *(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 16) = result;
    result = MiClearPageFileReservation(v_stack_mA0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11527596) + result * 8), v_stack_p18, a4);
    goto loc_003312EC;
loc_00331B0F:
    if ((unsigned int)((unsigned int)(v_stack_mB8)) == 0) goto loc_00331C37;
    if (((unsigned int)((unsigned int)(v_stack_mB8))) != 2) goto loc_003310FC;
    goto loc_00331E18;
loc_00331B28:
    result = MiReleasePageFileInfo(v_stack_mA0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11527596) + result * 8), 1, a4);
    goto loc_0033150E;
loc_00331B38:
    goto loc_00331AAA;
loc_00331B41:
    if (v_stack_mA0 != 0) goto loc_00330FC2;
    result = MI_READ_PTE_LOCK_FREE(v_stack_mC0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11527596) + result * 8), 1, a4);
    result = (result) | (64);
    result = MiWriteValidPteNewProtection(v_stack_mC0, result, 1, a4);
    v_r11 = 0;
    goto loc_00330FC2;
loc_00331B6B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13193031)))) & (64)) == 0) goto loc_0033174E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_mC0, result, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0033174E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), result, 1, a4);
    goto loc_00331750;
loc_00331B92:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13192992)))) & (64)) == 0) goto loc_0033176E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rdi)), result, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0033176E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), result, 1, a4);
    goto loc_00331770;
loc_00331BB9:
    result = (a4) + ((unsigned int)((unsigned int)(v_rdi)));
    if (v_r15 > result) goto loc_00330DD3;
    if (v_r15 >= a4) goto loc_00330DDA;
    goto loc_00330DD3;
loc_00331BD9:
    if ((((unsigned __int8)(v_stack_mC0)) & (32)) != 0) goto loc_00331A68;
    result = (1) + ((unsigned int)((unsigned int)(v_rdi)));
    if (v_r15 < result) goto loc_00331A68;
    result = MiCheckLinearProtectedPteAccessedBit(v_r15, v_stack_mC0, 128, a4);
    goto loc_00331A68;
loc_00331C11:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_mC0 + 16))) & (1)) == 0) goto loc_00331C26;
    result = (*(unsigned __int64 *)(v_stack_mC0 + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 2) goto loc_003311D0;
loc_00331C26:
    v_rbx = (v_stack_mC0) & (-33);
    v_stack_mC0 = v_rbx;
    goto loc_003311D4;
loc_00331C37:
    if (v_stack_m68 == 0) goto loc_00331D61;
loc_00331C47:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m68 + 48))) & (0x600000ULL));
    if (((unsigned int)(result)) == 0x600000ULL) goto loc_00331E11;
    v_stack_mB8 = 1;
    goto loc_003310FC;
loc_00331C66:
    result = MiSanitizeShadowPxe(v_r15, v_stack_m90, 128, a4);
    goto loc_0033127C;
loc_00331C7A:
loc_00331C7D:
    if (((unsigned int)(result)) < 0x600000ULL) goto loc_00331D00;
    result = MiSetPfnIdentity((unsigned int)(v_stack_mB4), 4, 128, a4);
    goto loc_003315F4;
loc_00331CA7:
    result = MiWritePteShadow(v_r15, 0, 128, a4);
    v_r11 = 0;
    goto loc_00330FC2;
loc_00331CC4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13192686)))) & (64)) == 0) goto loc_00331A7E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r15, 0, 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00331A7E;
    result = HvlNotifyLongSpinWait(0, 0, 128, a4);
    goto loc_00331A80;
loc_00331CEB:
    v_rdi = (0) | (result);
    goto loc_003318A3;
loc_00331D00:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13186468)) & ((unsigned int)(v_rdi))) == 0) goto loc_00331D96;
loc_00331D0E:
loc_00331D10:
    if (!sign_flag) goto loc_00331C7D;
    goto loc_00331D00;
loc_00331D1F:
    if ((((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 24))) & (8)) != 0) goto loc_00331D58;
    result = (unsigned __int8)((*(unsigned __int64 *)((unsigned int)(v_stack_mB4) + 24)) & (250));
    result = (unsigned __int8)((result) | (2));
    goto loc_00331AA7;
loc_00331D2C:
    goto loc_003315F4;
loc_00331D34:
    result = MiSanitizeShadowPxe(0, v_stack_m78, 128, a4);
    goto loc_00331983;
loc_00331D48:
    result = MiWritePteShadow(v_r15, v_stack_m78, 128, a4);
    goto loc_0033198E;
loc_00331D58:
    result = (unsigned __int8)((result) & (251));
    result = (unsigned __int8)((result) | (3));
    goto loc_00331AA7;
loc_00331D61:
    result = MiLockVadTree(1, v_stack_m78, 128, a4);
    result = MiLocateAddress(*(unsigned __int64 *)(a1 + 16), v_stack_m78, 128, a4);
    result = MiUnlockVadTree(1, 17, 128, a4);
    goto loc_00331C47;
loc_00331D96:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13192476)))) & (64)) == 0) goto loc_00331D0E;
    result = KiCheckVpBackingLongSpinWaitHypercall(1, 17, 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00331D0E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), 17, 128, a4);
    goto loc_00331D10;
loc_00331DBD:
    v_r15 = (v_r15) - (0);
    v_stack_p20 = result;
    v_r15 = (v_r15) >> (4);
    a3 = (128) * (v_r15);
    result = KeBugCheckEx(6 + 72, 6, a3, (unsigned int)(v_stack_mC4));
loc_00331DEB:
    v_rbx = (unsigned __int8)((v_stack_mC0) & (5));
    if (((unsigned __int8)(v_rbx)) != 4) goto loc_00330ECA;
    v_rdi = (result) | (66);
    goto loc_00330ECA;
loc_00331E00:
    goto loc_0033199C;
loc_00331E11:
    v_stack_mB8 = 2;
loc_00331E18:
    v_rbx = (v_rbx) & (-67);
    v_stack_mC0 = v_rbx;
    goto loc_003310FC;
loc_00331E25:
    result = MiBadShareCount((unsigned int)(v_stack_mB4), 6, a3, (unsigned int)(v_stack_mC4));
loc_00331E2E:
    result = (unsigned __int8)((result) & (239));
    v_stack_p1B = (unsigned __int8)(result);
    goto loc_003314C3;
loc_00331E38:
    goto loc_003318DE;
}
```

## 5. (Beta) C Style

```c
int64_t MiCompletePrivateZeroFault(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p1A;
    uint8_t v_stack_p1B;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (200);
    local_r15 = (*(uint64_t *)(arg1 + 0x10)) >> (9);
    local_r15 = (local_r15) & (local_r10);
    v_stack_m88 = *(uint64_t *)(arg1 + 0x38);
    local_r15 = (local_r15) + (a4);
    local_r11 = 0;
    v_stack_p8 = 0;
    v_stack_mC8 = 0;
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38);
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)))) != 0) goto loc_00331A11;
loc_00330D3F:
    result = 0;
    if (((*(uint8_t *)(arg1)) & (32)) != 0) { result = *(uint64_t *)(arg1 + 0x38); }
    v_stack_m80 = result;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) >> (9);
    Arg1 = (Arg1) & (local_r10);
    v_stack_m98 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    Arg1 = (Arg1) + (a4);
    v_stack_mB8 = 0;
    v_stack_m70 = Arg1;
    v_stack_m68 = *(uint64_t *)(arg1 + 0x40);
    v_stack_p20 = (uint32_t)((uint32_t)(0x2010ULL));
    local_rdi = (uint32_t)(0x2010ULL);
    if (*(uint64_t *)(arg1 + 0x40) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x34);
        Arg2 = *(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0x22);
        Arg2 = (Arg2) << (32);
        Arg2 = (Arg2) | (Arg1);
        Arg1 = 0x2050ULL;
        local_rdi = (uint32_t)(0x2010ULL);
        if (Arg2 == (*(uint64_t *)(arg1 + 0x40))) { local_rdi = (uint32_t)(Arg1); }
        v_stack_p20 = (uint32_t)(local_rdi);
    }
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (2)) != 0) goto loc_00331BB9;
loc_00330DD3:
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
loc_00330DDA:
    if ((*(uint32_t *)(arg1 + 0x24)) == 0) {
    }
    v_stack_mC4 = 0;
    v_stack_mB4 = 0;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (31));
    local_rdi = (*(uint64_t *)(v_rip - 0x320466 + local_rbx * 8)) & (v_rip - 3277926);
    local_rdi = (local_rdi) | (33);
    if (local_r15 < a4) goto loc_0033172C;
    if (local_r15 > a4) goto loc_0033172C;
    if (local_r15 >= a4) goto loc_00331874;
loc_00330E54:
    Arg2 = (local_r14) << (25);
    Arg1 = (local_r15) << (25);
    Arg1 = (Arg1) - (Arg2);
    Arg1 = (Arg1) >> (16);
    if (condition_is_above_or_equal) goto loc_00330E9C;
    if (Arg1 < local_r14) goto loc_00330E9C;
loc_00330E81:
    if (Arg1 > a4) goto loc_00330E9C;
    Arg1 = (Arg1) << (25);
    Arg1 = (Arg1) - (Arg2);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= local_r14) goto loc_00330E81;
loc_00330E9C:
    if (Arg1 <= local_r14) goto loc_00331736;
loc_00330EAF:
    result = MiIsAddressGlobal(Arg1, local_rdi, Arg3, a4);
    if ((uint32_t)(result) == 0) { local_rdi = local_rdi; }
loc_00330EC2:
    if (sign_flag) goto loc_00331DEB;
loc_00330ECA:
    if (condition_is_below) goto loc_003316E1;
loc_00330ED4:
    if (!(condition_is_above_or_equal)) {
        result = *(uint8_t *)(v_rip + 0xAFDFA0);
        result = (result) << (8);
        local_rdi = result;
        local_rdi = (local_rdi) ^ (local_rdi);
        local_rdi = (local_rdi) ^ (result);
    }
    Arg2 = local_rdi;
    if (condition_is_above_or_equal) {
        Arg2 = local_rdi;
        Arg2 = Arg2;
    }
    Arg1 = (Arg2) & (result);
    Arg1 = (Arg1) | (result);
    v_stack_mC0 = Arg1;
    if (Arg3 > 1) goto loc_003319C9;
loc_00330F3E:
loc_00330F41:
    v_stack_mB0 = 0;
    if (0 >= Arg3) goto loc_003318CD;
    if (local_r15 < Arg2) goto loc_00330FA4;
    if (local_r15 > a4) goto loc_00330FA4;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_00330FA4;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_r15))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_r15))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00331664;
loc_00330FA0:
loc_00330FA4:
    if ((*(uint32_t *)(arg1 + 0x24)) == 0) goto loc_0033122D;
    if ((*(uint32_t *)(arg1 + 0x24)) < 0) goto loc_00330FC2;
    if ((*(uint32_t *)(arg1 + 0x24)) < 0) goto loc_00331B41;
loc_00330FC2:
    if (*(uint64_t *)(Arg2) == 0) goto loc_00330FDD;
    *(uint64_t *)(Arg2) = *(uint64_t *)(*(uint64_t *)(Arg2));
    if (*(uint64_t *)(Arg2) == 0) {
        *(uint64_t *)(Arg2 + 0x8) = 0;
    }
    local_rbx = (*(uint64_t *)(Arg2)) - (local_rdi);
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * (local_rdi);
    if ((*(uint32_t *)(arg1 + 0x24)) != 0) goto loc_003315A0;
loc_00331004:
    local_rsi = 0;
loc_00331009:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p20)))) | (32));
    if (((*(uint8_t *)(arg1)) & (2)) == 0) { Arg2 = (uint32_t)((uint32_t)(v_stack_p20)); }
    v_stack_p20 = (uint32_t)(Arg2);
    result = MiInitializePfn(*(uint64_t *)(Arg2), local_r15, (uint32_t)(*(uint32_t *)(arg1 + 0x20)), (uint32_t)((uint32_t)(Arg2)));
    if (v_stack_m88 != 0) goto loc_00331814;
loc_00331039:
    local_rbx = (local_rbx) & (result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (16)) != 0) goto loc_0033194E;
    result = (v_stack_mC0) & (local_r15);
    local_rbx = (local_rbx) << (12);
    local_rbx = (local_rbx) | (result);
    local_rbx = (local_rbx) & (-33);
    result = (local_rbx) | (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) { local_rbx = result; }
    v_stack_mC0 = local_rbx;
    if (local_r15 > ((uint32_t)(*(uint32_t *)(arg1 + 0x20)) + local_r15 * 1)) goto loc_00331A40;
    if (local_r15 < ((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) goto loc_00331A40;
loc_003310B1:
    if ((*(uint64_t *)(arg1 + 0x48)) != 0) goto loc_00331A59;
    if (local_r15 == v_stack_m70) goto loc_003310FC;
    if (((*(uint32_t *)(arg1)) & (512)) == 0) goto loc_003310FC;
    local_rbx = (local_rbx) & (-33);
    v_stack_mC0 = local_rbx;
    if (v_stack_mA8 >= 0) goto loc_003310FC;
    if (local_r15 > ((uint32_t)(*(uint32_t *)(arg1 + 0x20)) + local_r15 * 1)) goto loc_003310FC;
    if (local_r15 < ((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) goto loc_003310FC;
    if (((*(uint32_t *)(v_stack_m98 + 0x1F4)) & (0x8000ULL)) != 0) goto loc_00331B0F;
loc_003310FC:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45))) & (9));
    if (((uint8_t)(result)) != 8) goto loc_00331869;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45))) & (4)) != 0) goto loc_00331869;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA)) == 0) goto loc_003311A7;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA)))) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0x8))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (3));
    result = (uint32_t)((result) & (511));
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_003316D4;
    if (sign_flag) goto loc_003316CA;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xD)) & (2)) != 0) goto loc_003311A7;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0x10)) << (25);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x20))) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    Arg2 = (Arg2) << (25);
    Arg2 = (Arg2) - (result);
    result = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0x8)) << (12);
    Arg2 = (Arg2) >> (16);
    Arg2 = (Arg2) + (result);
    if (Arg2 >= ((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) goto loc_0033177F;
loc_00331193:
loc_00331199:
    result = MiAddWorkingSetEntries(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38), Arg2, *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA), 5);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA) = 0;
loc_003311A7:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA)) == 0) goto loc_003316EA;
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA)) + 1);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38 + 0xA) = (uint16_t)(result);
loc_003311BB:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mC8)) | (4));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45)) & (16)) != 0) goto loc_00331C11;
loc_003311D0:
loc_003311D4:
    v_stack_mD8 = v_stack_m80;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (16));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45)) & (1)) == 0) { local_rsi = (uint32_t)(Arg1); }
    v_stack_mE0 = (uint32_t)(local_rsi);
    a4 = 0;
    v_stack_mE8 = v_stack_mC0;
    v_stack_mC8 = (uint32_t)(local_rsi);
    result = MiAllocateWsle(v_stack_mA0, local_r15, *(uint64_t *)(Arg2), a4);
    if ((uint32_t)(result) == 0) goto loc_00331299;
loc_00331212:
    local_r15 = (local_r15) + (8);
    Arg1 = (v_stack_mB0) + 1;
    local_r11 = 0;
    goto loc_00330F41;
loc_0033122D:
    if (local_rsi != 0) goto loc_00330FC2;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mC4)) + 1);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (31));
    local_rsi = (local_rsi) << (5);
    v_stack_mC4 = (uint32_t)(local_r10);
    if (*(uint64_t *)(v_rip + 0xAFCA3B) == 0) goto loc_00331262;
    if (((local_rsi) & (*(uint64_t *)(v_rip + 0xAFCA3B))) == 0) goto loc_0033180C;
    local_rsi = (local_rsi) | (16);
loc_00331262:
    v_stack_m90 = local_rsi;
    result = MiPteInShadowRange(local_r15, local_r15, v_stack_p18, a4);
    if ((uint32_t)(result) != 0) goto loc_00331C66;
loc_0033127C:
    *(uint64_t *)(local_r15) = local_rsi;
    if (0 != 0) goto loc_00331CA7;
    local_r11 = 0;
    goto loc_00330FC2;
loc_00331299:
    result = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x28)) & (0);
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (result);
    local_r15 = 0;
loc_003312C8:
    if (condition_is_below) goto loc_00331740;
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(Arg2) + 0x10);
    result = (uint8_t)((*(uint64_t *)(*(uint64_t *)(Arg2) + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00331AF5;
    v_stack_mA0 = 0;
loc_003312EC:
    result = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x10)) & (-3);
    *(uint64_t *)(*(uint64_t *)(Arg2) + 0x10) = result;
    result = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x18)) | (0);
    *(uint64_t *)(*(uint64_t *)(Arg2) + 0x18) = result;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(Arg2) + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_00331E25;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x18)) & (0);
    Arg2 = (Arg2) - 1;
    Arg1 = (Arg2) ^ (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x18));
    Arg1 = (Arg1) & (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x18));
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(*(uint64_t *)(Arg2) + 0x18) = Arg1;
    if (Arg2 != 0) goto loc_003317B4;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2) + 0x20)));
    if (!sign_flag) goto loc_00331499;
    local_rsi = 0;
    a4 = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x10)) >> (5);
    v_stack_p20 = a4;
loc_00331394:
    if (0 >= 1) goto loc_0033144B;
    local_rsi = (uint32_t)((*(uint64_t *)(*(uint64_t *)(Arg2) + 0x8)) >> (3));
    local_rsi = (uint32_t)((local_rsi) & (511));
    result = 511;
    local_rdi = 0;
    if (0 == 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg2) + 0x28);
        Arg2 = 0;
        Arg1 = (Arg1) & (0);
        Arg3 = 0x80000000ULL;
        result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, a4);
        a4 = v_stack_p20;
        local_rdi = result;
    }
    Arg3 = (*(uint64_t *)(local_rdi + local_rsi * 8)) >> (12);
    Arg3 = (Arg3) & (0);
    Arg2 = (Arg3 + Arg3 * 2) << (4);
    Arg2 = (Arg2) + (local_rsi);
    if (Arg2 != (*(uint64_t *)(Arg2))) goto loc_00331DBD;
    result = (uint32_t)(((uint32_t)((uint32_t)(a4))) & (31));
    Arg3 = (Arg3) << (7);
    result = (result) | (Arg3);
    result = (result) | (64);
    result = (result) << (5);
    if (*(uint64_t *)(v_rip + 0xAFC870) == 0) goto loc_00331437;
    if (((result) & (*(uint64_t *)(v_rip + 0xAFC870))) == 0) goto loc_003317AC;
    result = (result) | (16);
loc_00331437:
    *(uint64_t *)(local_rdi + local_rsi * 8) = result;
    if ((0 + 1) != 1) goto loc_00331713;
loc_0033144B:
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & (0 + 1);
    local_rdi = (local_rdi) + (0 + 1);
    local_r15 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838)) = 0;
    *(uint64_t *)(local_rdi) = *(uint64_t *)(v_rip - 0x320C13);
loc_00331499:
    result = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x18)) >> (62);
    result = (uint32_t)((result) & (1));
    if (condition_is_not_equal) goto loc_00331A8F;
    if ((uint32_t)(result) == 0) goto loc_003317BD;
    if ((((uint8_t)(v_stack_p1B)) & (16)) != 0) goto loc_00331E2E;
loc_003314C3:
    *(uint32_t *)(*(uint64_t *)(Arg2) + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    result = (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)(Arg2) + 0x10);
    if (condition_is_below) goto loc_0033150E;
    result = (uint8_t)((*(uint64_t *)(*(uint64_t *)(Arg2) + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00331505;
    result = (uint8_t)(((uint8_t)(v_stack_m88)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0033150E;
loc_00331505:
    if (v_stack_m88 != 0) goto loc_00331B28;
loc_0033150E:
    Arg1 = (*(uint64_t *)(Arg2)) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    result = MiInsertPageInFreeOrZeroedList(Arg1, 2, (uint32_t)(0xFFFFULL), a4);
loc_0033153D:
loc_0033154F:
    if (condition_is_below) goto loc_00331760;
    Arg2 = 0;
    result = MiDecrementShareCountEx(local_rbx, Arg2, (uint32_t)(0xFFFFULL), a4);
loc_0033157A:
    if (*(uint64_t *)(v_stack_p10) == 0) goto loc_003318D4;
    *(uint64_t *)(v_stack_p10) = *(uint64_t *)(*(uint64_t *)(v_stack_p10));
    if (*(uint64_t *)(v_stack_p10) == 0) {
        *(uint64_t *)(v_stack_p10 + 0x8) = 0;
    }
    result = MiReleaseFreshPage(*(uint64_t *)(v_stack_p10), Arg2, (uint32_t)(0xFFFFULL), a4);
    goto loc_0033157A;
loc_003315A0:
    if ((*(uint64_t *)(arg1 + 0x48)) != 0) goto loc_00331004;
    if ((*(uint64_t *)(arg1 + 0x48)) >= 0) goto loc_00331004;
    if (*(uint64_t *)(v_rip + 0xAFC6C2) == 0) goto loc_003315D5;
    result = (uint32_t)(v_stack_mC8);
    if ((((uint8_t)((uint32_t)(v_stack_mC8))) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xAFC6C2);
        result = ~(result);
        result = (result) & ((uint32_t)(v_stack_mC8));
    }
    result = (result) >> (16);
    if (result != 0) goto loc_00331C7A;
    if ((((uint32_t)(v_stack_mC8)) & (992)) == 0) goto loc_00331D2C;
loc_003315F4:
    Arg2 = 0;
    local_rsi = ((uint32_t)(v_stack_mC8)) & (-3);
    result = MiMapPageInHyperSpaceWorker(local_rbx, Arg2, (uint32_t)(0x80000000ULL), a4);
    Arg2 = (result) >> (9);
    Arg2 = (Arg2) & (local_rsi);
    Arg2 = (Arg2) + (local_rsi);
    local_rsi = 0;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p20)) | (8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838)) = 0;
    *(uint64_t *)(Arg2) = *(uint64_t *)(v_rip - 0x320DDC);
    goto loc_00331009;
loc_00331664:
    if (((*(uint64_t *)(v_rip + 0xC95419)) & (0x600000ULL)) == 0) goto loc_00330FA0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00330FA0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00330FA0;
    result = (0) >> (3);
    result = (result) & (local_rbx);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rsi = (local_rsi) | (32);
    }
    local_rsi = (local_rsi) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rsi = local_rsi; }
    goto loc_00330FA0;
loc_003316CA:
    if (((*(uint8_t *)(result + 0xD)) & (2)) == 0) goto loc_003311A7;
loc_003316D4:
    result = MiEmptyDeferredWorkingSetEntries(result, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), (uint32_t)(0x80000000ULL), a4);
    goto loc_003311A7;
loc_003316E1:
    local_rdi = (result) & (-5);
    goto loc_00330ED4;
loc_003316EA:
    *(uint16_t *)(local_rdi + 0xA) = 1;
    result = (uint32_t)((0) >> (3));
    result = (uint16_t)((result) & ((uint16_t)(local_rbx)));
    *(uint16_t *)(local_rdi + 0x8) = (uint16_t)(result);
    if (!sign_flag) goto loc_00331945;
    goto loc_003311BB;
loc_00331713:
    result = (*(uint64_t *)(local_r15)) & (0);
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + (local_rsi);
    goto loc_00331394;
loc_0033172C:
    goto loc_00330EC2;
loc_00331736:
    local_rdi = (local_rdi) | (4);
    goto loc_00330EAF;
loc_00331740:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC93B64)) & ((uint32_t)(local_rdi))) == 0) goto loc_00331B6B;
loc_0033174E:
loc_00331750:
    if (!sign_flag) goto loc_003312C8;
    goto loc_00331740;
loc_00331760:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC93B44)) & ((uint32_t)(local_rdi))) == 0) goto loc_00331B92;
loc_0033176E:
loc_00331770:
    if (!sign_flag) goto loc_0033154F;
    goto loc_00331760;
loc_0033177F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508)) > (*(uint64_t *)(local_rbx + 0x18))) goto loc_00331193;
    a4 = 4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (15)) != 0) { a4 = (uint32_t)(local_rsi); }
    goto loc_00331199;
loc_003317AC:
    result = ((uint32_t)(*(uint32_t *)(result + 0xB8))) | (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
    goto loc_00331437;
loc_003317B4:
    goto loc_0033153D;
loc_003317BD:
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(Arg2) + 16, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), (uint32_t)(0x80000000ULL), a4);
    result = -9;
    if (condition_is_below) { result = 0xFFFFFFFFFFFFF7FFULL; }
    result = (result) & (result);
    *(uint64_t *)(*(uint64_t *)(Arg2) + 0x10) = result;
    if ((((uint8_t)(v_stack_p1A)) & (16)) == 0) goto loc_00331A23;
    *(uint32_t *)(*(uint64_t *)(Arg2) + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    result = MiInsertPageInList(*(uint64_t *)(Arg2), 8, (uint32_t)(0x80000000ULL), a4);
    goto loc_0033153D;
loc_0033180C:
    local_rsi = (local_rsi) | (*(uint64_t *)(Arg2));
    goto loc_00331262;
loc_00331814:
    Arg2 = (*(uint64_t *)(local_rdi + 0x18)) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(local_rdi + 0x8));
    Arg1 = (local_r15) << (25);
    result = (result) << (25);
    Arg1 = (Arg1) - (result);
    result = (*(uint64_t *)(local_rdi + 0x20)) << (12);
    result = (result) + (*(uint64_t *)(Arg2));
    Arg1 = (Arg1) >> (16);
    if (Arg1 != result) goto loc_00331039;
    if ((*(uint8_t *)(local_rdi)) == 5) goto loc_00331039;
    result = MiAdvanceFaultList(local_rdi, Arg2, (uint32_t)(0x80000000ULL), a4);
    goto loc_00331039;
loc_00331869:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mC8)) & (0xFFFFFFFBULL));
    goto loc_003311D4;
loc_00331874:
    if (local_r15 > result) goto loc_00330E54;
    if (local_r15 == result) goto loc_00331CEB;
    if (local_r15 >= result) {
        local_rdi = (local_rdi) & (Arg1);
    }
    result = MiUserPdeOrAbove(local_r15, Arg2, (uint32_t)(0x80000000ULL), a4);
    if ((uint32_t)(result) != 0) {
        local_rdi = (local_rdi) | (4);
    }
    local_r11 = 0;
    goto loc_00330E54;
loc_003318CD:
    goto loc_003318DE;
loc_003318D4:
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_00331E38;
loc_003318DE:
    if (v_stack_p8 != 0) goto loc_003319E8;
loc_003318E8:
    if ((*(uint32_t *)(arg1 + 0x24)) == 0) goto loc_00331932;
loc_003318F0:
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_0033191B;
    if (((*(uint32_t *)(arg1)) & (256)) != 0) {
        result = v_stack_m98;
        Arg1 = (uint32_t)((uint32_t)(v_stack_mB4));
    }
loc_0033191B:
    local_rsp = (local_rsp) + (200);
    return 273;
loc_00331932:
    if ((uint32_t)((uint32_t)(v_stack_mC4)) == 0) goto loc_003318F0;
    result = MiUpdatePageTableUseCount(*(uint64_t *)(arg1 + 0x10), (uint32_t)(v_stack_mC4), v_stack_p18, a4);
    goto loc_003318F0;
loc_00331945:
    goto loc_003311BB;
loc_0033194E:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (31));
    local_rbx = (local_rbx) << (7);
    Arg1 = (Arg1) | (local_rbx);
    Arg1 = (Arg1) | (64);
    Arg1 = (Arg1) << (5);
    result = MiSwizzleInvalidPte(Arg1, (uint32_t)(v_stack_mC4), v_stack_p18, a4);
    v_stack_m78 = result;
    result = MiPteInShadowRange(local_r15, (uint32_t)(v_stack_mC4), v_stack_p18, a4);
    if ((uint32_t)(result) != 0) goto loc_00331D34;
loc_00331983:
    *(uint64_t *)(local_r15) = result;
    if ((uint32_t)((uint32_t)((uint32_t)(local_rsi))) != 0) goto loc_00331D48;
loc_0033198E:
    if (((*(uint32_t *)(arg1)) & (256)) != 0) goto loc_00331E00;
loc_0033199C:
loc_0033199E:
    if (condition_is_below) goto loc_00331A70;
    Arg2 = 0;
    result = MiDecrementShareCountEx((uint32_t)(v_stack_mB4), Arg2, v_stack_p18, a4);
    goto loc_00331212;
loc_003319C9:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45))) & (8)) != 0) goto loc_00330F3E;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45)) | (8));
    v_stack_p8 = 1;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45) = (uint8_t)(result);
    goto loc_00330F3E;
loc_003319E8:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x45)) & (8)) == 0) goto loc_00331A03;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x8)) + (56);
        result = MiEmptyDeferredWorkingSetEntries(Arg1, Arg2, v_stack_p18, a4);
    }
    goto loc_003318E8;
loc_00331A11:
    result = (*(uint64_t *)(arg1 + 0x8)) & (-2);
    if ((*(uint8_t *)(result)) == 3) { Arg2 = (uint32_t)((uint32_t)((uint32_t)(local_rsi))); }
    v_stack_mC8 = (uint32_t)(Arg2);
    goto loc_00330D3F;
loc_00331A23:
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_p1A = (uint8_t)(result);
    *(uint32_t *)((uint32_t)(v_stack_mB4) + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    result = MiInsertPageInList(Arg1, 4, v_stack_p18, a4);
    goto loc_0033153D;
loc_00331A40:
    Arg1 = (v_stack_p18) + (4);
    goto loc_003310B1;
loc_00331A59:
    if (condition_is_below) goto loc_00331BD9;
loc_00331A68:
    *(uint64_t *)(local_r15) = v_stack_mC0;
    goto loc_00331212;
loc_00331A70:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + 1);
    if (((*(uint32_t *)(v_rip + 0xC93834)) & ((uint32_t)(local_rdi))) == 0) goto loc_00331CC4;
loc_00331A7E:
loc_00331A80:
    if (!sign_flag) goto loc_0033199E;
    goto loc_00331A70;
loc_00331A8F:
    if ((uint32_t)(*(uint64_t *)((uint32_t)(v_stack_mB4) + 0x18)) != 0) goto loc_00331B38;
    if ((((uint8_t)(v_stack_p1A)) & (16)) == 0) goto loc_00331D1F;
    result = (uint8_t)((v_stack_p1A) & (251));
    result = (uint8_t)((result) | (3));
loc_00331AA7:
    v_stack_p1A = (uint8_t)(result);
loc_00331AAA:
    *(uint32_t *)((uint32_t)(v_stack_mB4) + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    if (condition_is_below) goto loc_0033153D;
    result = MiGetPagingFileOffset(*(uint64_t *)((uint32_t)(v_stack_mB4) + 0x10), 4, v_stack_p18, a4);
    if ((uint32_t)(result) == 0) goto loc_0033153D;
    result = (*(uint64_t *)((uint32_t)(v_stack_mB4) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAFE5AC) + result * 8) + 0x2D3) = 1;
    goto loc_0033153D;
loc_00331AF5:
    result = (*(uint64_t *)((uint32_t)(v_stack_mB4) + 0x10)) & (-5);
    *(uint64_t *)((uint32_t)(v_stack_mB4) + 0x10) = result;
    result = MiClearPageFileReservation(v_stack_mA0, *(uint64_t *)(*(uint64_t *)(v_rip + 0xAFE5AC) + result * 8), v_stack_p18, a4);
    goto loc_003312EC;
loc_00331B0F:
    if ((uint32_t)((uint32_t)(v_stack_mB8)) == 0) goto loc_00331C37;
    if (((uint32_t)((uint32_t)(v_stack_mB8))) != 2) goto loc_003310FC;
    goto loc_00331E18;
loc_00331B28:
    result = MiReleasePageFileInfo(v_stack_mA0, *(uint64_t *)(*(uint64_t *)(v_rip + 0xAFE5AC) + result * 8), 1, a4);
    goto loc_0033150E;
loc_00331B38:
    goto loc_00331AAA;
loc_00331B41:
    if (v_stack_mA0 != 0) goto loc_00330FC2;
    result = MI_READ_PTE_LOCK_FREE(v_stack_mC0, *(uint64_t *)(*(uint64_t *)(v_rip + 0xAFE5AC) + result * 8), 1, a4);
    result = (result) | (64);
    result = MiWriteValidPteNewProtection(v_stack_mC0, result, 1, a4);
    local_r11 = 0;
    goto loc_00330FC2;
loc_00331B6B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC94F47)))) & (64)) == 0) goto loc_0033174E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_mC0, result, 1, a4);
    if ((uint8_t)(result) == 0) goto loc_0033174E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), result, 1, a4);
    goto loc_00331750;
loc_00331B92:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC94F20)))) & (64)) == 0) goto loc_0033176E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rdi)), result, 1, a4);
    if ((uint8_t)(result) == 0) goto loc_0033176E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), result, 1, a4);
    goto loc_00331770;
loc_00331BB9:
    result = (a4) + ((uint32_t)((uint32_t)(local_rdi)));
    if (local_r15 > result) goto loc_00330DD3;
    if (local_r15 >= a4) goto loc_00330DDA;
    goto loc_00330DD3;
loc_00331BD9:
    if ((((uint8_t)(v_stack_mC0)) & (32)) != 0) goto loc_00331A68;
    result = (1) + ((uint32_t)((uint32_t)(local_rdi)));
    if (local_r15 < result) goto loc_00331A68;
    result = MiCheckLinearProtectedPteAccessedBit(local_r15, v_stack_mC0, 128, a4);
    goto loc_00331A68;
loc_00331C11:
    if ((((uint8_t)(*(uint64_t *)(v_stack_mC0 + 0x10))) & (1)) == 0) goto loc_00331C26;
    result = (*(uint64_t *)(v_stack_mC0 + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 2) goto loc_003311D0;
loc_00331C26:
    local_rbx = (v_stack_mC0) & (-33);
    v_stack_mC0 = local_rbx;
    goto loc_003311D4;
loc_00331C37:
    if (v_stack_m68 == 0) goto loc_00331D61;
loc_00331C47:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x30))) & (0x600000ULL));
    if (((uint32_t)(result)) == 0x600000ULL) goto loc_00331E11;
    v_stack_mB8 = 1;
    goto loc_003310FC;
loc_00331C66:
    result = MiSanitizeShadowPxe(local_r15, v_stack_m90, 128, a4);
    goto loc_0033127C;
loc_00331C7A:
loc_00331C7D:
    if (((uint32_t)(result)) < 0x600000ULL) goto loc_00331D00;
    result = MiSetPfnIdentity((uint32_t)(v_stack_mB4), 4, 128, a4);
    goto loc_003315F4;
loc_00331CA7:
    result = MiWritePteShadow(local_r15, 0, 128, a4);
    local_r11 = 0;
    goto loc_00330FC2;
loc_00331CC4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC94DEE)))) & (64)) == 0) goto loc_00331A7E;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r15, 0, 128, a4);
    if ((uint8_t)(result) == 0) goto loc_00331A7E;
    result = HvlNotifyLongSpinWait(0, 0, 128, a4);
    goto loc_00331A80;
loc_00331CEB:
    local_rdi = (0) | (result);
    goto loc_003318A3;
loc_00331D00:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC935A4)) & ((uint32_t)(local_rdi))) == 0) goto loc_00331D96;
loc_00331D0E:
loc_00331D10:
    if (!sign_flag) goto loc_00331C7D;
    goto loc_00331D00;
loc_00331D1F:
    if ((((uint8_t)(*(uint64_t *)((uint32_t)(v_stack_mB4) + 0x18))) & (8)) != 0) goto loc_00331D58;
    result = (uint8_t)((*(uint64_t *)((uint32_t)(v_stack_mB4) + 0x18)) & (250));
    result = (uint8_t)((result) | (2));
    goto loc_00331AA7;
loc_00331D2C:
    goto loc_003315F4;
loc_00331D34:
    result = MiSanitizeShadowPxe(0, v_stack_m78, 128, a4);
    goto loc_00331983;
loc_00331D48:
    result = MiWritePteShadow(local_r15, v_stack_m78, 128, a4);
    goto loc_0033198E;
loc_00331D58:
    result = (uint8_t)((result) & (251));
    result = (uint8_t)((result) | (3));
    goto loc_00331AA7;
loc_00331D61:
    result = MiLockVadTree(1, v_stack_m78, 128, a4);
    result = MiLocateAddress(*(uint64_t *)(arg1 + 0x10), v_stack_m78, 128, a4);
    result = MiUnlockVadTree(1, 17, 128, a4);
    goto loc_00331C47;
loc_00331D96:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC94D1C)))) & (64)) == 0) goto loc_00331D0E;
    result = KiCheckVpBackingLongSpinWaitHypercall(1, 17, 128, a4);
    if ((uint8_t)(result) == 0) goto loc_00331D0E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), 17, 128, a4);
    goto loc_00331D10;
loc_00331DBD:
    local_r15 = (local_r15) - (0);
    v_stack_p20 = result;
    local_r15 = (local_r15) >> (4);
    Arg3 = (128) * (local_r15);
    result = KeBugCheckEx(6 + 72, 6, Arg3, (uint32_t)(v_stack_mC4));
loc_00331DEB:
    local_rbx = (uint8_t)((v_stack_mC0) & (5));
    if (((uint8_t)(local_rbx)) != 4) goto loc_00330ECA;
    local_rdi = (result) | (66);
    goto loc_00330ECA;
loc_00331E00:
    goto loc_0033199C;
loc_00331E11:
    v_stack_mB8 = 2;
loc_00331E18:
    local_rbx = (local_rbx) & (-67);
    v_stack_mC0 = local_rbx;
    goto loc_003310FC;
loc_00331E25:
    result = MiBadShareCount((uint32_t)(v_stack_mB4), 6, Arg3, (uint32_t)(v_stack_mC4));
loc_00331E2E:
    result = (uint8_t)((result) & (239));
    v_stack_p1B = (uint8_t)(result);
    goto loc_003314C3;
loc_00331E38:
    goto loc_003318DE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00330CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
