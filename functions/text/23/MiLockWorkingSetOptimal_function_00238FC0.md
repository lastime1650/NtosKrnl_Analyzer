# MiLockWorkingSetOptimal

- RVA: `0x00238FC0`–`0x002394BD` (길이 `1,277` bytes)
- VA: `0x0000000140238FC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BA4`
- 디코드: `305`개 명령, `1,277/1,277` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **19**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00239083` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x00239116` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00239141` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x002391B4` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0023930D` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0023932A` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00239391` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002393D7` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002393E3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023943C` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00239474` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002394AA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002394B6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [MmSetAddressRangeModifiedEx](MmSetAddressRangeModifiedEx_function_00236F20.md) at `0x00236FC0`
- [MiDirtyPte](MiDirtyPte_function_00237C5C.md) at `0x00237C87`
- [sub_00238945](Unknown_function_00238945.md) at `0x00238AD5`
- [MmMapViewInSystemCache](../27/MmMapViewInSystemCache_function_00273094.md) at `0x002731F0`
- [sub_00293C9B](../29/Unknown_function_00293C9B.md) at `0x00293CB4`
- [sub_00293F76](../29/Unknown_function_00293F76.md) at `0x002942CB`
- [MiMakeSystemCachePteValid](../2A/MiMakeSystemCachePteValid_function_002A35D8.md) at `0x002A3638`
- [sub_00347472](../34/Unknown_function_00347472.md) at `0x003474B9`
- [sub_003490AD](../34/Unknown_function_003490AD.md) at `0x003491E9`
- [MiExpandSystemCache](../3B/MiExpandSystemCache_function_003B3DC8.md) at `0x003B3E93`
- [MiReturnSystemCacheRegionsToKva](../49/MiReturnSystemCacheRegionsToKva_function_00494DFC.md) at `0x00494E7C`
- [MiBuildForkPageTable](../4A/MiBuildForkPageTable_function_004ACF5C.md) at `0x004AD220`
- [MiAddMappedPtesPadding](../4D/MiAddMappedPtesPadding_function_004DA2E8.md) at `0x004DA3A9`
- [MiInitializeDynamicBitmap](../67/MiInitializeDynamicBitmap_function_0067F5BC.md) at `0x0067F792`
- [MiInitializeDynamicBitmap](../67/MiInitializeDynamicBitmap_function_0067F5BC.md) at `0x0067F85C`
- [MiMarkBootGuardPage](../68/MiMarkBootGuardPage_function_0068643C.md) at `0x0068648A`
- [sub_006FB3A8](../6F/Unknown_function_006FB3A8.md) at `0x006FB3DD`
- [MiMapDummyPages](../../init/C6/MiMapDummyPages_function_00C60A58.md) at `0x00C60ADA`
- [MiProtectSharedUserPage](../../init/C6/MiProtectSharedUserPage_function_00C60F44.md) at `0x00C6105A`
- [MiInitializeBootShadowStackPage](../../init/C6/MiInitializeBootShadowStackPage_function_00C67D8C.md) at `0x00C67E9B`
- [MiInitializeBootShadowStackPage](../../init/C6/MiInitializeBootShadowStackPage_function_00C67D8C.md) at `0x00C67F59`

### Static image references
- `0x00239026` → RVA `0x00E38840` (`.data`; read)
- `0x00239054` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00239061` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0023906E` → RVA `0x00F0DE58` (`.data`; read)
- `0x0023920B` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00239265` → RVA `0x00E2CB40` (`.data`; read)
- `0x002393B3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002393CD` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00238FC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00238FC5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00238FCA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00238FCF  57                              push rdi
00238FD0  41 54                           push r12
00238FD2  41 55                           push r13
00238FD4  41 56                           push r14
00238FD6  41 57                           push r15
00238FD8  48 83 EC 20                     sub rsp, 0x20
00238FDC  48 8B F2                        mov rsi, rdx
00238FDF  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
00238FE9  48 C1 EE 09                     shr rsi, 9
00238FED  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00238FF7  48 23 F0                        and rsi, rax
00238FFA  4D 8B F8                        mov r15, r8
00238FFD  48 8B E9                        mov rbp, rcx
00239000  49 8B C5                        mov rax, r13
00239003  48 03 F0                        add rsi, rax
00239006  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0023900C  24 0F                           and al, 0xf
0023900E  3C 06                           cmp al, 6
00239010  0F 83 59 03 00 00               jae 0x14023936f
00239016  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0023901C  24 0F                           and al, 0xf
0023901E  3C 01                           cmp al, 1
00239020  0F 85 E1 03 00 00               jne 0x140239407
00239026  48 8D 05 13 F8 BF 00            lea rax, [rip + 0xbff813]
0023902D  65 8B 1C 25 A4 01 00 00         mov ebx, dword ptr gs:[0x1a4]
00239035  48 8B 00                        mov rax, qword ptr [rax]
00239038  D1 EB                           shr ebx, 1
0023903A  83 E3 03                        and ebx, 3
0023903D  8B FB                           mov edi, ebx
0023903F  48 C1 E7 06                     shl rdi, 6
00239043  48 03 F8                        add rdi, rax
00239046  45 0F 20 C6                     mov r14, cr8
0023904A  41 BC 02 00 00 00               mov r12d, 2
00239050  45 0F 22 C4                     mov cr8, r12
00239054  83 3D C5 DC D8 00 00            cmp dword ptr [rip + 0xd8dcc5], 0
0023905B  0F 85 A4 02 00 00               jne 0x140239305
00239061  F6 05 9E DA D8 00 21            test byte ptr [rip + 0xd8da9e], 0x21
00239068  0F 84 B2 00 00 00               je 0x140239120
0023906E  8B 05 E4 4D CD 00               mov eax, dword ptr [rip + 0xcd4de4]
00239074  85 C0                           test eax, eax
00239076  0F 85 A4 00 00 00               jne 0x140239120
0023907C  41 0F B6 D6                     movzx edx, r14b
00239080  48 8B CF                        mov rcx, rdi
00239083  E8 98 3C 04 00                  call 0x14027cd20
00239088  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00239091  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00239098  48 85 C9                        test rcx, rcx
0023909B  74 06                           je 0x1402390a3
0023909D  89 99 44 01 00 00               mov dword ptr [rcx + 0x144], ebx
002390A3  41 0F B6 DE                     movzx ebx, r14b
002390A7  41 88 1F                        mov byte ptr [r15], bl
002390AA  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
002390B4  48 3B F0                        cmp rsi, rax
002390B7  0F 85 8E 00 00 00               jne 0x14023914b
002390BD  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
002390C6  8B 8D B8 00 00 00               mov ecx, dword ptr [rbp + 0xb8]
002390CC  80 E1 0F                        and cl, 0xf
002390CF  0F 85 74 01 00 00               jne 0x140239249
002390D5  48 81 C5 B0 00 00 00            add rbp, 0xb0
002390DC  45 33 F6                        xor r14d, r14d
002390DF  41 8B C4                        mov eax, r12d
002390E2  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
002390E9  48 8D 0C 48                     lea rcx, [rax + rcx*2]
002390ED  48 8D 0C CA                     lea rcx, [rdx + rcx*8]
002390F1  48 89 69 08                     mov qword ptr [rcx + 8], rbp
002390F5  4C 89 31                        mov qword ptr [rcx], r14
002390F8  90                              nop
002390F9  F6 05 06 DA D8 00 21            test byte ptr [rip + 0xd8da06], 0x21
00239100  0F 85 11 02 00 00               jne 0x140239317
00239106  48 8B D1                        mov rdx, rcx
00239109  48 87 55 00                     xchg qword ptr [rbp], rdx
0023910D  48 85 D2                        test rdx, rdx
00239110  0F 84 12 01 00 00               je 0x140239228
00239116  E8 95 ED 01 00                  call 0x140257eb0
0023911B  E9 08 01 00 00                  jmp 0x140239228
00239120  0F 0D 0F                        prefetchw byte ptr [rdi]
00239123  8B 07                           mov eax, dword ptr [rdi]
00239125  0F BA F0 1F                     btr eax, 0x1f
00239129  8D 48 01                        lea ecx, [rax + 1]
0023912C  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
00239130  0F 84 52 FF FF FF               je 0x140239088
00239136  85 C0                           test eax, eax
00239138  79 EF                           jns 0x140239129
0023913A  41 0F B6 D6                     movzx edx, r14b
0023913E  48 8B CF                        mov rcx, rdi
00239141  E8 3A 92 12 00                  call 0x140362380
00239146  E9 3D FF FF FF                  jmp 0x140239088
0023914B  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00239151  48 BA 00 D0 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed000
0023915B  49 B8 FF DF BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbedfff
00239165  A8 0F                           test al, 0xf
00239167  75 37                           jne 0x1402391a0
00239169  48 8B C2                        mov rax, rdx
0023916C  48 3B F0                        cmp rsi, rax
0023916F  72 2F                           jb 0x1402391a0
00239171  49 8B C0                        mov rax, r8
00239174  48 3B F0                        cmp rsi, rax
00239177  77 27                           ja 0x1402391a0
00239179  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00239182  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00239189  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00239190  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00239197  48 85 C9                        test rcx, rcx
0023919A  0F 85 C4 02 00 00               jne 0x140239464
002391A0  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
002391A6  A8 0F                           test al, 0xf
002391A8  0F 85 CE 00 00 00               jne 0x14023927c
002391AE  45 33 F6                        xor r14d, r14d
002391B1  48 8B CE                        mov rcx, rsi
002391B4  E8 E7 96 04 00                  call 0x1402828a0
002391B9  48 8B D8                        mov rbx, rax
002391BC  48 BD FF FF FF FF FF FF FF DF   movabs rbp, 0xdfffffffffffffff
002391C6  49 BF 20 00 00 00 00 00 00 10   movabs r15, 0x1000000000000020
002391D0  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
002391DA  48 BA 00 00 00 00 00 00 00 20   movabs rdx, 0x2000000000000000
002391E4  48 B9 00 00 00 00 10 00 00 00   movabs rcx, 0x1000000000
002391EE  F6 C3 01                        test bl, 1
002391F1  74 35                           je 0x140239228
002391F3  48 8B C3                        mov rax, rbx
002391F6  48 C1 E8 3C                     shr rax, 0x3c
002391FA  A8 01                           test al, 1
002391FC  0F 85 32 01 00 00               jne 0x140239334
00239202  48 8B CB                        mov rcx, rbx
00239205  48 23 CD                        and rcx, rbp
00239208  49 0B CF                        or rcx, r15
0023920B  48 F7 05 72 D8 D8 00 00 00 00 02  test qword ptr [rip + 0xd8d872], 0x2000000
00239216  74 03                           je 0x14023921b
00239218  0F AE E8                        lfence
0023921B  48 8B C3                        mov rax, rbx
0023921E  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
00239223  48 8B D8                        mov rbx, rax
00239226  75 BC                           jne 0x1402391e4
00239228  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0023922D  48 8B C6                        mov rax, rsi
00239230  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00239235  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0023923A  48 83 C4 20                     add rsp, 0x20
0023923E  41 5F                           pop r15
00239240  41 5E                           pop r14
00239242  41 5D                           pop r13
00239244  41 5C                           pop r12
00239246  5F                              pop rdi
00239247  C3                              ret
00239248  CC                              int3
00239249  45 33 F6                        xor r14d, r14d
0023924C  80 F9 07                        cmp cl, 7
0023924F  0F 84 46 01 00 00               je 0x14023939b
00239255  80 F9 05                        cmp cl, 5
00239258  41 BC 03 00 00 00               mov r12d, 3
0023925E  45 0F 44 E6                     cmove r12d, r14d
00239262  41 8B EC                        mov ebp, r12d
00239265  48 8D 0D D4 38 BF 00            lea rcx, [rip + 0xbf38d4]
0023926C  48 8D 89 80 32 00 00            lea rcx, [rcx + 0x3280]
00239273  48 8D 2C E9                     lea rbp, [rcx + rbp*8]
00239277  E9 63 FE FF FF                  jmp 0x1402390df
0023927C  48 8B C2                        mov rax, rdx
0023927F  48 3B F0                        cmp rsi, rax
00239282  0F 82 26 FF FF FF               jb 0x1402391ae
00239288  49 8B C0                        mov rax, r8
0023928B  48 3B F0                        cmp rsi, rax
0023928E  0F 87 1A FF FF FF               ja 0x1402391ae
00239294  45 33 F6                        xor r14d, r14d
00239297  48 8B C2                        mov rax, rdx
0023929A  48 8B CE                        mov rcx, rsi
0023929D  BB 01 00 00 00                  mov ebx, 1
002392A2  48 2B C8                        sub rcx, rax
002392A5  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
002392AB  48 C1 F9 03                     sar rcx, 3
002392AF  03 C9                           add ecx, ecx
002392B1  8B F9                           mov edi, ecx
002392B3  44 8B F9                        mov r15d, ecx
002392B6  48 C1 EF 05                     shr rdi, 5
002392BA  48 8D 0D 7F 38 BF 00            lea rcx, [rip + 0xbf387f]
002392C1  48 8D 89 6C 26 00 00            lea rcx, [rcx + 0x266c]
002392C8  41 83 E7 1F                     and r15d, 0x1f
002392CC  8B 14 B9                        mov edx, dword ptr [rcx + rdi*4]
002392CF  48 8D 3C B9                     lea rdi, [rcx + rdi*4]
002392D3  41 8B CF                        mov ecx, r15d
002392D6  D3 E3                           shl ebx, cl
002392D8  41 D3 E4                        shl r12d, cl
002392DB  41 8B EC                        mov ebp, r12d
002392DE  F7 D5                           not ebp
002392E0  41 8B CF                        mov ecx, r15d
002392E3  8B C2                           mov eax, edx
002392E5  D3 E8                           shr eax, cl
002392E7  A8 01                           test al, 1
002392E9  0F 85 FB 00 00 00               jne 0x1402393ea
002392EF  8B CB                           mov ecx, ebx
002392F1  8B C2                           mov eax, edx
002392F3  0B CA                           or ecx, edx
002392F5  23 CD                           and ecx, ebp
002392F7  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
002392FB  8B D0                           mov edx, eax
002392FD  0F 84 25 FF FF FF               je 0x140239228
00239303  EB DB                           jmp 0x1402392e0
00239305  41 0F B6 D4                     movzx edx, r12b
00239309  41 0F B6 CE                     movzx ecx, r14b
0023930D  E8 EA C3 2B 00                  call 0x1404f56fc
00239312  E9 4A FD FF FF                  jmp 0x140239061
00239317  44 8B 05 3A 4B CD 00            mov r8d, dword ptr [rip + 0xcd4b3a]
0023931E  45 85 C0                        test r8d, r8d
00239321  0F 85 DF FD FF FF               jne 0x140239106
00239327  48 8B D5                        mov rdx, rbp
0023932A  E8 21 C5 03 00                  call 0x140275850
0023932F  E9 F4 FE FF FF                  jmp 0x140239228
00239334  A8 02                           test al, 2
00239336  75 78                           jne 0x1402393b0
00239338  48 8B FB                        mov rdi, rbx
0023933B  48 0B FA                        or rdi, rdx
0023933E  48 F7 05 3F D7 D8 00 00 00 00 02  test qword ptr [rip + 0xd8d73f], 0x2000000
00239349  74 03                           je 0x14023934e
0023934B  0F AE E8                        lfence
0023934E  48 85 0D 33 D7 D8 00            test qword ptr [rip + 0xd8d733], rcx
00239355  0F 85 B8 00 00 00               jne 0x140239413
0023935B  48 8B C3                        mov rax, rbx
0023935E  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
00239363  48 8B D8                        mov rbx, rax
00239366  48 0F 44 DF                     cmove rbx, rdi
0023936A  E9 7F FE FF FF                  jmp 0x1402391ee
0023936F  44 0F 20 C3                     mov rbx, cr8
00239373  41 BC 02 00 00 00               mov r12d, 2
00239379  45 0F 22 C4                     mov cr8, r12
0023937D  83 3D 9C D9 D8 00 00            cmp dword ptr [rip + 0xd8d99c], 0
00239384  0F 84 1D FD FF FF               je 0x1402390a7
0023938A  41 0F B6 D4                     movzx edx, r12b
0023938E  0F B6 CB                        movzx ecx, bl
00239391  E8 66 C3 2B 00                  call 0x1404f56fc
00239396  E9 0C FD FF FF                  jmp 0x1402390a7
0023939B  41 BC 01 00 00 00               mov r12d, 1
002393A1  E9 BC FE FF FF                  jmp 0x140239262
002393A6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
002393B0  41 FF C6                        inc r14d
002393B3  44 85 35 F2 BE D8 00            test dword ptr [rip + 0xd8bef2], r14d
002393BA  74 11                           je 0x1402393cd
002393BC  F3 90                           pause
002393BE  48 8B 1E                        mov rbx, qword ptr [rsi]
002393C1  48 0F BA E3 3C                  bt rbx, 0x3c
002393C6  72 E8                           jb 0x1402393b0
002393C8  E9 03 FE FF FF                  jmp 0x1402391d0
002393CD  8B 05 E5 D6 D8 00               mov eax, dword ptr [rip + 0xd8d6e5]
002393D3  A8 40                           test al, 0x40
002393D5  74 E5                           je 0x1402393bc
002393D7  E8 B4 60 0D 00                  call 0x14030f490
002393DC  84 C0                           test al, al
002393DE  74 DC                           je 0x1402393bc
002393E0  41 8B CE                        mov ecx, r14d
002393E3  E8 78 60 0D 00                  call 0x14030f460
002393E8  EB D4                           jmp 0x1402393be
002393EA  A8 02                           test al, 2
002393EC  0F 85 8E 00 00 00               jne 0x140239480
002393F2  41 8B CC                        mov ecx, r12d
002393F5  8B C2                           mov eax, edx
002393F7  0B CA                           or ecx, edx
002393F9  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
002393FD  8B D0                           mov edx, eax
002393FF  0F 44 D1                        cmove edx, ecx
00239402  E9 D9 FE FF FF                  jmp 0x1402392e0
00239407  48 8D 81 C0 00 00 00            lea rax, [rcx + 0xc0]
0023940E  E9 1A FC FF FF                  jmp 0x14023902d
00239413  40 0F B6 C7                     movzx eax, dil
00239417  24 21                           and al, 0x21
00239419  3C 01                           cmp al, 1
0023941B  0F 85 3A FF FF FF               jne 0x14023935b
00239421  49 8B C5                        mov rax, r13
00239424  49 03 C0                        add rax, r8
00239427  48 3B F0                        cmp rsi, rax
0023942A  0F 82 2B FF FF FF               jb 0x14023935b
00239430  41 B8 80 00 00 00               mov r8d, 0x80
00239436  48 8B D7                        mov rdx, rdi
00239439  48 8B CE                        mov rcx, rsi
0023943C  E8 3F 99 05 00                  call 0x140292d80
00239441  48 B9 00 00 00 00 10 00 00 00   movabs rcx, 0x1000000000
0023944B  48 BA 00 00 00 00 00 00 00 20   movabs rdx, 0x2000000000000000
00239455  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
0023945F  E9 F7 FE FF FF                  jmp 0x14023935b
00239464  48 8B C6                        mov rax, rsi
00239467  48 C1 E8 03                     shr rax, 3
0023946B  25 FF 01 00 00                  and eax, 0x1ff
00239470  48 8D 0C 81                     lea rcx, [rcx + rax*4]
00239474  E8 07 FA 00 00                  call 0x140248e80
00239479  E9 AA FD FF FF                  jmp 0x140239228
0023947E  66 90                           nop
00239480  41 FF C6                        inc r14d
00239483  44 85 35 22 BE D8 00            test dword ptr [rip + 0xd8be22], r14d
0023948A  74 14                           je 0x1402394a0
0023948C  F3 90                           pause
0023948E  8B 17                           mov edx, dword ptr [rdi]
00239490  41 8B CF                        mov ecx, r15d
00239493  8B C2                           mov eax, edx
00239495  D3 E8                           shr eax, cl
00239497  A8 01                           test al, 1
00239499  75 E5                           jne 0x140239480
0023949B  E9 40 FE FF FF                  jmp 0x1402392e0
002394A0  8B 05 12 D6 D8 00               mov eax, dword ptr [rip + 0xd8d612]
002394A6  A8 40                           test al, 0x40
002394A8  74 E2                           je 0x14023948c
002394AA  E8 E1 5F 0D 00                  call 0x14030f490
002394AF  84 C0                           test al, al
002394B1  74 D9                           je 0x14023948c
002394B3  41 8B CE                        mov ecx, r14d
002394B6  E8 A5 5F 0D 00                  call 0x14030f460
002394BB  EB D1                           jmp 0x14023948e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockWorkingSetOptimal(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rsi = (a2) >> (9);
    v_rsi = (v_rsi) & (result);
    v_rsi = (v_rsi) + (v_r13);
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) >= 6) goto loc_0023936F;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_00239407;
loc_0023902D:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) >> (1));
    v_rbx = (unsigned int)((v_rbx) & (3));
    v_rdi = ((unsigned int)((unsigned int)(v_rbx))) << (6);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 12580883));
    if ((*(unsigned int *)(v_rip + 14212293)) != 0) goto loc_00239305;
loc_00239061:
    if (((*(unsigned __int8 *)(v_rip + 14211742)) & (33)) == 0) goto loc_00239120;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13454820))) != 0) goto loc_00239120;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rdi, (unsigned __int8)(v_cr8), a3, a4);
loc_00239088:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324) = (unsigned int)(v_rbx);
    }
loc_002390A7:
    *(unsigned __int8 *)(a3) = (unsigned __int8)((unsigned __int8)(v_cr8));
    if (v_rsi != (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_0023914B;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00239249;
    v_rbp = (a1) + (176);
    v_r14 = 0;
loc_002390DF:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 8) = v_rbp;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8) = 0;
    if (((*(unsigned __int8 *)(v_rip + 14211590)) & (33)) != 0) goto loc_00239317;
loc_00239106:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_00239228;
    result = KxWaitForLockOwnerShip(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, a3, a4);
    goto loc_00239228;
loc_00239120:
loc_00239129:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_00239088;
    if (!sign_flag) goto loc_00239129;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rdi, 0, a3, a4);
    goto loc_00239088;
loc_0023914B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 184)))) & (15)) != 0) goto loc_002391A0;
    if (v_rsi < 0) goto loc_002391A0;
    if (v_rsi > a3) goto loc_002391A0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_00239464;
loc_002391A0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 184)))) & (15)) != 0) goto loc_0023927C;
loc_002391AE:
    v_r14 = 0;
    result = MI_READ_PTE_LOCK_FREE(v_rsi, 0, a3, a4);
loc_002391D0:
loc_002391E4:
loc_002391EE:
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00239228;
    result = (result) >> (60);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00239334;
    a1 = (result) & (v_rbp);
    a1 = (a1) | (a3);
    if (((*(unsigned __int64 *)(v_rip + 14211186)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 14211186)) & (0x2000000ULL)) != 0) goto loc_002391E4;
loc_00239228:
    v_rsp = (v_rsp) + (32);
    return v_rsi;
loc_00239249:
    v_r14 = 0;
    if (((unsigned __int8)(a1)) == 7) goto loc_0023939B;
    v_r12 = 3;
    if (((unsigned __int8)(a1)) == 5) { v_r12 = 0; }
loc_00239262:
    goto loc_002390DF;
loc_0023927C:
    if (v_stack_p18 < 0) goto loc_002391AE;
    if (v_stack_p18 > a3) goto loc_002391AE;
    v_r14 = 0;
    a1 = (v_stack_p18) - (0);
    a1 = (a1) >> (3);
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    v_rdi = ((unsigned int)((unsigned int)(a1))) >> (5);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (31));
    v_rbx = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r15)))));
    v_r12 = (unsigned int)((v_r12) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r15)))));
    v_rbp = (unsigned int)(~((unsigned int)((unsigned int)(v_r12))));
loc_002392E0:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12531839 + 9836 + v_rdi * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r15)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002393EA;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12531839 + 9836 + v_rdi * 4)))));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_rbp)));
    if (condition_is_equal) goto loc_00239228;
    goto loc_002392E0;
loc_00239305:
    result = KiRaiseIrqlProcessIrqlFlags(0, (unsigned __int8)(v_r12), a3, a4);
    goto loc_00239061;
loc_00239317:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13454138))) != 0) goto loc_00239106;
    result = KiAcquireQueuedSpinLockInstrumented(0, v_rbp, (unsigned int)(*(unsigned int *)(v_rip + 13454138)), a4);
    goto loc_00239228;
loc_00239334:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_002393B0;
    v_rdi = (v_rbx) | (v_rbp);
    if (((*(unsigned __int64 *)(v_rip + 14210879)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 14210867)) & (0)) != 0) goto loc_00239413;
loc_0023935B:
    if (((*(unsigned __int64 *)(v_rip + 14210867)) & (0)) == 0) { v_rbx = v_rdi; }
    goto loc_002391EE;
loc_0023936F:
    if ((*(unsigned int *)(v_rip + 14211484)) == 0) goto loc_002390A7;
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, (unsigned int)(*(unsigned int *)(v_rip + 13454138)), a4);
    goto loc_002390A7;
loc_0023939B:
    goto loc_00239262;
loc_002393B0:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14204658)) & ((unsigned int)(v_r14))) == 0) goto loc_002393CD;
loc_002393BC:
loc_002393BE:
    if (condition_is_below) goto loc_002393B0;
    goto loc_002391D0;
loc_002393CD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14210789)))) & (64)) == 0) goto loc_002393BC;
    result = KiCheckVpBackingLongSpinWaitHypercall(2, 2, (unsigned int)(*(unsigned int *)(v_rip + 13454138)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_002393BC;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), 2, (unsigned int)(*(unsigned int *)(v_rip + 13454138)), a4);
    goto loc_002393BE;
loc_002393EA:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00239480;
    a1 = (unsigned int)((1) | (2));
    a2 = 2;
    if (condition_is_equal) { a2 = (unsigned int)(a1); }
    goto loc_002392E0;
loc_00239407:
    goto loc_0023902D;
loc_00239413:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_0023935B;
    result = (v_r13) + ((unsigned int)(*(unsigned int *)(v_rip + 13454138)));
    if (v_stack_p18 < result) goto loc_0023935B;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p18, v_rdi, 128, a4);
    goto loc_0023935B;
loc_00239464:
    result = (v_stack_p18) >> (3);
    result = (unsigned int)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_p18 + result * 4, v_rdi, 128, a4);
    goto loc_00239228;
loc_00239480:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14204450)) & ((unsigned int)(v_r14))) == 0) goto loc_002394A0;
loc_0023948C:
loc_0023948E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r15)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00239480;
    goto loc_002392E0;
loc_002394A0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14210578)))) & (64)) == 0) goto loc_0023948C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(v_rdi)), 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0023948C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), (unsigned int)(*(unsigned int *)(v_rdi)), 128, a4);
    goto loc_0023948E;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockWorkingSetOptimal(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rsi = (Arg2) >> (9);
    local_rsi = (local_rsi) & (result);
    local_rsi = (local_rsi) + (local_r13);
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) >= 6) goto loc_0023936F;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_00239407;
loc_0023902D:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) >> (1));
    local_rbx = (uint32_t)((local_rbx) & (3));
    local_rdi = ((uint32_t)((uint32_t)(local_rbx))) << (6);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xBFF813));
    if ((*(uint32_t *)(v_rip + 0xD8DCC5)) != 0) goto loc_00239305;
loc_00239061:
    if (((*(uint8_t *)(v_rip + 0xD8DA9E)) & (33)) == 0) goto loc_00239120;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCD4DE4))) != 0) goto loc_00239120;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(local_rdi, (uint8_t)(v_cr8), Arg3, a4);
loc_00239088:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) != 0) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144) = (uint32_t)(local_rbx);
    }
loc_002390A7:
    *(uint8_t *)(arg3) = (uint8_t)((uint8_t)(v_cr8));
    if (local_rsi != (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_0023914B;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00239249;
    local_rbp = (Arg1) + (176);
    local_r14 = 0;
loc_002390DF:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x8) = local_rbp;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8) = 0;
    if (((*(uint8_t *)(v_rip + 0xD8DA06)) & (33)) != 0) goto loc_00239317;
loc_00239106:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_00239228;
    result = KxWaitForLockOwnerShip(*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, Arg3, a4);
    goto loc_00239228;
loc_00239120:
loc_00239129:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_00239088;
    if (!sign_flag) goto loc_00239129;
    result = ExpWaitForSpinLockSharedAndAcquire(local_rdi, 0, Arg3, a4);
    goto loc_00239088;
loc_0023914B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0xB8)))) & (15)) != 0) goto loc_002391A0;
    if (local_rsi < 0) goto loc_002391A0;
    if (local_rsi > Arg3) goto loc_002391A0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_00239464;
loc_002391A0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0xB8)))) & (15)) != 0) goto loc_0023927C;
loc_002391AE:
    local_r14 = 0;
    result = MI_READ_PTE_LOCK_FREE(local_rsi, 0, Arg3, a4);
loc_002391D0:
loc_002391E4:
loc_002391EE:
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00239228;
    result = (result) >> (60);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00239334;
    Arg1 = (result) & (local_rbp);
    Arg1 = (Arg1) | (Arg3);
    if (((*(uint64_t *)(v_rip + 0xD8D872)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD8D872)) & (0x2000000ULL)) != 0) goto loc_002391E4;
loc_00239228:
    local_rsp = (local_rsp) + (32);
    return local_rsi;
loc_00239249:
    local_r14 = 0;
    if (((uint8_t)(Arg1)) == 7) goto loc_0023939B;
    local_r12 = 3;
    if (((uint8_t)(Arg1)) == 5) { local_r12 = 0; }
loc_00239262:
    goto loc_002390DF;
loc_0023927C:
    if (v_stack_p18 < 0) goto loc_002391AE;
    if (v_stack_p18 > Arg3) goto loc_002391AE;
    local_r14 = 0;
    Arg1 = (v_stack_p18) - (0);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    local_rdi = ((uint32_t)((uint32_t)(Arg1))) >> (5);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (31));
    local_rbx = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r15)))));
    local_r12 = (uint32_t)((local_r12) << ((uint8_t)((uint32_t)((uint32_t)(local_r15)))));
    local_rbp = (uint32_t)(~((uint32_t)((uint32_t)(local_r12))));
loc_002392E0:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF387F + 0x266C + local_rdi * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_r15)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002393EA;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF387F + 0x266C + local_rdi * 4)))));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_rbp)));
    if (condition_is_equal) goto loc_00239228;
    goto loc_002392E0;
loc_00239305:
    result = KiRaiseIrqlProcessIrqlFlags(0, (uint8_t)(local_r12), Arg3, a4);
    goto loc_00239061;
loc_00239317:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCD4B3A))) != 0) goto loc_00239106;
    result = KiAcquireQueuedSpinLockInstrumented(0, local_rbp, (uint32_t)(*(uint32_t *)(v_rip + 0xCD4B3A)), a4);
    goto loc_00239228;
loc_00239334:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_002393B0;
    local_rdi = (local_rbx) | (local_rbp);
    if (((*(uint64_t *)(v_rip + 0xD8D73F)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD8D733)) & (0)) != 0) goto loc_00239413;
loc_0023935B:
    if (((*(uint64_t *)(v_rip + 0xD8D733)) & (0)) == 0) { local_rbx = local_rdi; }
    goto loc_002391EE;
loc_0023936F:
    if ((*(uint32_t *)(v_rip + 0xD8D99C)) == 0) goto loc_002390A7;
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, (uint32_t)(*(uint32_t *)(v_rip + 0xCD4B3A)), a4);
    goto loc_002390A7;
loc_0023939B:
    goto loc_00239262;
loc_002393B0:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD8BEF2)) & ((uint32_t)(local_r14))) == 0) goto loc_002393CD;
loc_002393BC:
loc_002393BE:
    if (condition_is_below) goto loc_002393B0;
    goto loc_002391D0;
loc_002393CD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD8D6E5)))) & (64)) == 0) goto loc_002393BC;
    result = KiCheckVpBackingLongSpinWaitHypercall(2, 2, (uint32_t)(*(uint32_t *)(v_rip + 0xCD4B3A)), a4);
    if ((uint8_t)(result) == 0) goto loc_002393BC;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), 2, (uint32_t)(*(uint32_t *)(v_rip + 0xCD4B3A)), a4);
    goto loc_002393BE;
loc_002393EA:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00239480;
    Arg1 = (uint32_t)((1) | (2));
    Arg2 = 2;
    if (condition_is_equal) { Arg2 = (uint32_t)(Arg1); }
    goto loc_002392E0;
loc_00239407:
    goto loc_0023902D;
loc_00239413:
    result = (uint8_t)(((uint8_t)(local_rdi)) & (33));
    if (((uint8_t)(result)) != 1) goto loc_0023935B;
    result = (local_r13) + ((uint32_t)(*(uint32_t *)(v_rip + 0xCD4B3A)));
    if (v_stack_p18 < result) goto loc_0023935B;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p18, local_rdi, 128, a4);
    goto loc_0023935B;
loc_00239464:
    result = (v_stack_p18) >> (3);
    result = (uint32_t)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_p18 + result * 4, local_rdi, 128, a4);
    goto loc_00239228;
loc_00239480:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD8BE22)) & ((uint32_t)(local_r14))) == 0) goto loc_002394A0;
loc_0023948C:
loc_0023948E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_r15)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00239480;
    goto loc_002392E0;
loc_002394A0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD8D612)))) & (64)) == 0) goto loc_0023948C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(local_rdi)), 128, a4);
    if ((uint8_t)(result) == 0) goto loc_0023948C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), (uint32_t)(*(uint32_t *)(local_rdi)), 128, a4);
    goto loc_0023948E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00238FC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
