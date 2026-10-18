# MmSetAddressRangeModifiedEx

- RVA: `0x00236F20`–`0x002375DC` (길이 `1,724` bytes)
- VA: `0x0000000140236F20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060944`
- 디코드: `394`개 명령, `1,724/1,724` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00236F4B` → [MiMakeProtectionMask](../32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x00236FC0` → [MiLockWorkingSetOptimal](MiLockWorkingSetOptimal_function_00238FC0.md) (function, `0x00238FC0`)
- `0x00236FCD` → [MiGetMultiplexedVm](../34/MiGetMultiplexedVm_function_003479B0.md) (function, `0x003479B0`)
- `0x00237081` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002370A2` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002370D5` → [MiPteInShadowRange](MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x0023710D` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00237233` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x002372D2` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002372D7` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002372EF` → [MiUnlockWorkingSetOptimal](MiUnlockWorkingSetOptimal_function_00238DFC.md) (function, `0x00238DFC`)
- `0x002373F4` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00237451` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00237461` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00237498` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x002374B5` → [MI_TIGHTER_PERMISSIONS](../38/MI_TIGHTER_PERMISSIONS_function_00384C30.md) (function, `0x00384C30`)
- `0x00237503` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x0023750B` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x0023751F` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x002375AB` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)

### Direct callers
- [CcFlushCacheOneRange](CcFlushCacheOneRange_function_00236A30.md) at `0x00236BD6`
- [CcZeroDataInCache](../29/CcZeroDataInCache_function_0029E894.md) at `0x0029E9BA`
- [CcPurgeAndClearCacheSection](../38/CcPurgeAndClearCacheSection_function_0038A614.md) at `0x0038A7B2`
- [MmSetAddressRangeModified](../48/MmSetAddressRangeModified_function_0048DDE0.md) at `0x0048DDE4`
- [CcUnpinRepinnedBcb](../49/CcUnpinRepinnedBcb_function_0049F560.md) at `0x0049F5EB`

### Static image references
- `0x00236FAB` → RVA `0x00E3D680` (`.data`; read)
- `0x00237038` → RVA `0x00E30088` (`.data`; read)
- `0x002370E2` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00237243` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00237443` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002374F6` → RVA `0x00695890` (`MiTbFlushSort`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00236F20  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00236F25  53                              push rbx
00236F26  55                              push rbp
00236F27  56                              push rsi
00236F28  57                              push rdi
00236F29  41 54                           push r12
00236F2B  41 55                           push r13
00236F2D  41 56                           push r14
00236F2F  41 57                           push r15
00236F31  48 83 EC 58                     sub rsp, 0x58
00236F35  48 8B D9                        mov rbx, rcx
00236F38  C6 84 24 B0 00 00 00 00         mov byte ptr [rsp + 0xb0], 0
00236F40  B9 04 00 00 00                  mov ecx, 4
00236F45  4C 8B C2                        mov r8, rdx
00236F48  45 32 ED                        xor r13b, r13b
00236F4B  E8 30 25 0F 00                  call 0x140329480
00236F50  4C 8B F3                        mov r14, rbx
00236F53  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00236F5A  8B F8                           mov edi, eax
00236F5C  49 C1 EE 09                     shr r14, 9
00236F60  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00236F6A  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00236F74  45 33 E4                        xor r12d, r12d
00236F77  4C 23 F0                        and r14, rax
00236F7A  45 8B FC                        mov r15d, r12d
00236F7D  48 8B CA                        mov rcx, rdx
00236F80  4C 03 F1                        add r14, rcx
00236F83  49 8D 48 FF                     lea rcx, [r8 - 1]
00236F87  48 03 CB                        add rcx, rbx
00236F8A  48 C1 E9 09                     shr rcx, 9
00236F8E  48 23 C8                        and rcx, rax
00236F91  48 8B C2                        mov rax, rdx
00236F94  48 03 C8                        add rcx, rax
00236F97  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
00236F9F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00236FA4  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
00236FAB  48 8D 0D CE 66 C0 00            lea rcx, [rip + 0xc066ce]
00236FB2  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
00236FBA  49 8B D6                        mov rdx, r14
00236FBD  41 8B F4                        mov esi, r12d
00236FC0  E8 FB 1F 00 00                  call 0x140238fc0
00236FC5  48 8B D3                        mov rdx, rbx
00236FC8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00236FCD  E8 DE 09 11 00                  call 0x1403479b0
00236FD2  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00236FD7  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
00236FE1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00236FE6  48 8B C3                        mov rax, rbx
00236FE9  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
00236FF3  49 8B 1E                        mov rbx, qword ptr [r14]
00236FF6  F6 C3 01                        test bl, 1
00236FF9  0F 84 62 02 00 00               je 0x140237261
00236FFF  48 8B C3                        mov rax, rbx
00237002  44 89 A4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r12d
0023700A  48 C1 E8 0C                     shr rax, 0xc
0023700E  49 8B FC                        mov rdi, r12
00237011  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00237016  49 23 C0                        and rax, r8
00237019  48 8D 2C 40                     lea rbp, [rax + rax*2]
0023701D  48 C1 E5 04                     shl rbp, 4
00237021  48 8B C2                        mov rax, rdx
00237024  48 03 E8                        add rbp, rax
00237027  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
0023702E  0F 82 0C 02 00 00               jb 0x140237240
00237034  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00237038  48 8B 0D 49 90 BF 00            mov rcx, qword ptr [rip + 0xbf9049]
0023703F  48 C1 E8 2B                     shr rax, 0x2b
00237043  25 FF 03 00 00                  and eax, 0x3ff
00237048  F6 45 22 10                     test byte ptr [rbp + 0x22], 0x10
0023704C  4C 8B 24 C1                     mov r12, qword ptr [rcx + rax*8]
00237050  0F 84 DA 01 00 00               je 0x140237230
00237056  8B 45 10                        mov eax, dword ptr [rbp + 0x10]
00237059  48 0F BA E0 0A                  bt rax, 0xa
0023705E  0F 83 CC 01 00 00               jae 0x140237230
00237064  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0023706E  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
00237073  48 85 FF                        test rdi, rdi
00237076  74 0E                           je 0x140237086
00237078  45 33 C0                        xor r8d, r8d
0023707B  48 8B D7                        mov rdx, rdi
0023707E  49 8B CC                        mov rcx, r12
00237081  E8 4A CF 04 00                  call 0x140283fd0
00237086  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
0023708D  83 FF 02                        cmp edi, 2
00237090  0F 84 D5 03 00 00               je 0x14023746b
00237096  F6 C3 42                        test bl, 0x42
00237099  0F 84 9E 04 00 00               je 0x14023753d
0023709F  49 8B CE                        mov rcx, r14
002370A2  E8 F9 B7 04 00                  call 0x1402828a0
002370A7  48 8B F8                        mov rdi, rax
002370AA  45 33 E4                        xor r12d, r12d
002370AD  48 B8 00 00 00 00 00 00 00 7F   movabs rax, 0x7f00000000000000
002370B7  49 8B CE                        mov rcx, r14
002370BA  48 23 F8                        and rdi, rax
002370BD  48 B8 BD FF FF FF FF FF FF 80   movabs rax, 0x80ffffffffffffbd
002370C7  48 23 D8                        and rbx, rax
002370CA  48 0B FB                        or rdi, rbx
002370CD  41 8B DC                        mov ebx, r12d
002370D0  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
002370D5  E8 26 8A 00 00                  call 0x14023fb00
002370DA  85 C0                           test eax, eax
002370DC  0F 85 38 04 00 00               jne 0x14023751a
002370E2  48 0F BA 25 9D F9 D8 00 24      bt qword ptr [rip + 0xd8f99d], 0x24
002370EB  0F 82 CA 02 00 00               jb 0x1402373bb
002370F1  49 89 3E                        mov qword ptr [r14], rdi
002370F4  85 DB                           test ebx, ebx
002370F6  0F 85 A9 04 00 00               jne 0x1402375a5
002370FC  41 B5 01                        mov r13b, 1
002370FF  BD 01 00 00 00                  mov ebp, 1
00237104  4D 85 FF                        test r15, r15
00237107  0F 85 83 00 00 00               jne 0x140237190
0023710D  E8 7E BB 00 00                  call 0x140242c90
00237112  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00237117  4C 8B F8                        mov r15, rax
0023711A  44 89 60 10                     mov dword ptr [rax + 0x10], r12d
0023711E  C7 40 14 20 00 00 00            mov dword ptr [rax + 0x14], 0x20
00237125  48 89 10                        mov qword ptr [rax], rdx
00237128  8B 8A B8 00 00 00               mov ecx, dword ptr [rdx + 0xb8]
0023712E  C1 E9 08                        shr ecx, 8
00237131  C0 E9 03                        shr cl, 3
00237134  80 E1 01                        and cl, 1
00237137  88 48 18                        mov byte ptr [rax + 0x18], cl
0023713A  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00237140  A8 0F                           test al, 0xf
00237142  75 20                           jne 0x140237164
00237144  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0023714D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00237154  48 81 C1 00 04 00 00            add rcx, 0x400
0023715B  48 3B D1                        cmp rdx, rcx
0023715E  0F 85 CC 03 00 00               jne 0x140237530
00237164  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0023716A  A8 0F                           test al, 0xf
0023716C  0F 85 C3 03 00 00               jne 0x140237535
00237172  8B C5                           mov eax, ebp
00237174  41 83 67 10 DB                  and dword ptr [r15 + 0x10], 0xffffffdb
00237179  41 89 47 08                     mov dword ptr [r15 + 8], eax
0023717D  66 41 C7 47 19 00 00            mov word ptr [r15 + 0x19], 0
00237184  45 89 67 1C                     mov dword ptr [r15 + 0x1c], r12d
00237188  4D 89 67 20                     mov qword ptr [r15 + 0x20], r12
0023718C  4D 89 67 28                     mov qword ptr [r15 + 0x28], r12
00237190  41 83 7F 08 01                  cmp dword ptr [r15 + 8], 1
00237195  48 8B DD                        mov rbx, rbp
00237198  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
002371A0  48 8B FA                        mov rdi, rdx
002371A3  0F 85 55 02 00 00               jne 0x1402373fe
002371A9  41 8B EC                        mov ebp, r12d
002371AC  45 8B 4F 1C                     mov r9d, dword ptr [r15 + 0x1c]
002371B0  45 85 C9                        test r9d, r9d
002371B3  0F 84 97 01 00 00               je 0x140237350
002371B9  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
002371BD  A8 02                           test al, 2
002371BF  0F 85 45 01 00 00               jne 0x14023730a
002371C5  41 8D 41 FF                     lea eax, [r9 - 1]
002371C9  4D 8D 14 C7                     lea r10, [r15 + rax*8]
002371CD  49 8B 44 C7 28                  mov rax, qword ptr [r15 + rax*8 + 0x28]
002371D2  48 A9 00 0C 00 00               test rax, 0xc00
002371D8  0F 85 72 01 00 00               jne 0x140237350
002371DE  4C 8B C0                        mov r8, rax
002371E1  48 8B C8                        mov rcx, rax
002371E4  41 81 E0 FF 03 00 00            and r8d, 0x3ff
002371EB  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002371F2  49 8D 50 01                     lea rdx, [r8 + 1]
002371F6  48 C1 E2 0C                     shl rdx, 0xc
002371FA  48 03 D1                        add rdx, rcx
002371FD  48 3B D7                        cmp rdx, rdi
00237200  75 16                           jne 0x140237218
00237202  4A 8D 0C 03                     lea rcx, [rbx + r8]
00237206  49 3B C8                        cmp rcx, r8
00237209  76 0D                           jbe 0x140237218
0023720B  48 81 F9 FF 03 00 00            cmp rcx, 0x3ff
00237212  0F 86 9D 03 00 00               jbe 0x1402375b5
00237218  41 8D 49 FF                     lea ecx, [r9 - 1]
0023721C  48 8D 49 05                     lea rcx, [rcx + 5]
00237220  49 8B 04 CF                     mov rax, qword ptr [r15 + rcx*8]
00237224  4D 8D 14 CF                     lea r10, [r15 + rcx*8]
00237228  48 8B C8                        mov rcx, rax
0023722B  E9 02 01 00 00                  jmp 0x140237332
00237230  48 8B CD                        mov rcx, rbp
00237233  E8 98 9B 13 00                  call 0x140370dd0
00237238  48 8B F8                        mov rdi, rax
0023723B  E9 24 FE FF FF                  jmp 0x140237064
00237240  41 FF C4                        inc r12d
00237243  44 85 25 62 E0 D8 00            test dword ptr [rip + 0xd8e062], r12d
0023724A  0F 84 F3 01 00 00               je 0x140237443
00237250  F3 90                           pause
00237252  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00237256  48 85 C0                        test rax, rax
00237259  0F 89 C8 FD FF FF               jns 0x140237027
0023725F  EB DF                           jmp 0x140237240
00237261  83 FF 02                        cmp edi, 2
00237264  75 49                           jne 0x1402372af
00237266  F6 C3 08                        test bl, 8
00237269  75 44                           jne 0x1402372af
0023726B  48 83 CB 08                     or rbx, 8
0023726F  49 89 1E                        mov qword ptr [r14], rbx
00237272  EB 3B                           jmp 0x1402372af
00237274  85 ED                           test ebp, ebp
00237276  0F 84 68 02 00 00               je 0x1402374e4
0023727C  41 80 7F 19 00                  cmp byte ptr [r15 + 0x19], 0
00237281  0F 84 4B 03 00 00               je 0x1402375d2
00237287  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
0023728E  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00237296  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
002372A0  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
002372A5  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
002372AF  48 05 00 10 00 00               add rax, 0x1000
002372B5  49 83 C6 08                     add r14, 8
002372B9  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
002372C1  4C 3B F1                        cmp r14, rcx
002372C4  0F 86 29 FD FF FF               jbe 0x140236ff3
002372CA  4D 85 FF                        test r15, r15
002372CD  74 0D                           je 0x1402372dc
002372CF  49 8B CF                        mov rcx, r15
002372D2  E8 E9 AC 0D 00                  call 0x140311fc0
002372D7  E8 94 C9 0D 00                  call 0x140313c70
002372DC  44 0F B6 84 24 B0 00 00 00      movzx r8d, byte ptr [rsp + 0xb0]
002372E5  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
002372EA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002372EF  E8 08 1B 00 00                  call 0x140238dfc
002372F4  41 0F B6 C5                     movzx eax, r13b
002372F8  48 83 C4 58                     add rsp, 0x58
002372FC  41 5F                           pop r15
002372FE  41 5E                           pop r14
00237300  41 5D                           pop r13
00237302  41 5C                           pop r12
00237304  5F                              pop rdi
00237305  5E                              pop rsi
00237306  5D                              pop rbp
00237307  5B                              pop rbx
00237308  C3                              ret
00237309  CC                              int3
0023730A  45 85 C9                        test r9d, r9d
0023730D  74 41                           je 0x140237350
0023730F  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00237313  A8 02                           test al, 2
00237315  75 39                           jne 0x140237350
00237317  41 8D 49 FF                     lea ecx, [r9 - 1]
0023731B  48 8D 49 05                     lea rcx, [rcx + 5]
0023731F  49 8B 04 CF                     mov rax, qword ptr [r15 + rcx*8]
00237323  4D 8D 14 CF                     lea r10, [r15 + rcx*8]
00237327  48 8B C8                        mov rcx, rax
0023732A  48 A9 00 0C 00 00               test rax, 0xc00
00237330  75 1E                           jne 0x140237350
00237332  4C 8B DB                        mov r11, rbx
00237335  48 8B D1                        mov rdx, rcx
00237338  49 C1 E3 0C                     shl r11, 0xc
0023733C  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00237343  4E 8D 04 1F                     lea r8, [rdi + r11]
00237347  49 3B D0                        cmp rdx, r8
0023734A  0F 84 F5 01 00 00               je 0x140237545
00237350  45 3B 4F 0C                     cmp r9d, dword ptr [r15 + 0xc]
00237354  0F 84 1A FF FF FF               je 0x140237274
0023735A  48 85 DB                        test rbx, rbx
0023735D  0F 84 24 FF FF FF               je 0x140237287
00237363  48 8D 43 FF                     lea rax, [rbx - 1]
00237367  48 8B CF                        mov rcx, rdi
0023736A  48 3D FF 03 00 00               cmp rax, 0x3ff
00237370  BA 00 04 00 00                  mov edx, 0x400
00237375  48 0F 46 D3                     cmovbe rdx, rbx
00237379  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00237380  48 8D 42 FF                     lea rax, [rdx - 1]
00237384  25 FF 03 00 00                  and eax, 0x3ff
00237389  48 0B C1                        or rax, rcx
0023738C  48 8B CA                        mov rcx, rdx
0023738F  4B 89 44 CF 28                  mov qword ptr [r15 + r9*8 + 0x28], rax
00237394  45 8B 4F 1C                     mov r9d, dword ptr [r15 + 0x1c]
00237398  49 01 57 20                     add qword ptr [r15 + 0x20], rdx
0023739C  41 FF C1                        inc r9d
0023739F  48 C1 E1 0C                     shl rcx, 0xc
002373A3  48 03 F9                        add rdi, rcx
002373A6  45 89 4F 1C                     mov dword ptr [r15 + 0x1c], r9d
002373AA  48 2B DA                        sub rbx, rdx
002373AD  74 AB                           je 0x14023735a
002373AF  45 3B 4F 0C                     cmp r9d, dword ptr [r15 + 0xc]
002373B3  0F 84 F0 FD FF FF               je 0x1402371a9
002373B9  EB 9F                           jmp 0x14023735a
002373BB  40 F6 C7 20                     test dil, 0x20
002373BF  0F 85 2C FD FF FF               jne 0x1402370f1
002373C5  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002373CF  48 8B C8                        mov rcx, rax
002373D2  48 B8 00 00 00 00 40 00 00 00   movabs rax, 0x4000000000
002373DC  48 03 C8                        add rcx, rax
002373DF  4C 3B F1                        cmp r14, rcx
002373E2  0F 82 09 FD FF FF               jb 0x1402370f1
002373E8  41 B8 80 00 00 00               mov r8d, 0x80
002373EE  48 8B D7                        mov rdx, rdi
002373F1  49 8B CE                        mov rcx, r14
002373F4  E8 87 B9 05 00                  call 0x140292d80
002373F9  E9 F3 FC FF FF                  jmp 0x1402370f1
002373FE  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
00237402  F6 C1 04                        test cl, 4
00237405  0F 85 9E FD FF FF               jne 0x1402371a9
0023740B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00237415  48 8B C0                        mov rax, rax
00237418  48 3B D0                        cmp rdx, rax
0023741B  0F 82 88 FD FF FF               jb 0x1402371a9
00237421  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0023742B  48 8B C0                        mov rax, rax
0023742E  48 3B D0                        cmp rdx, rax
00237431  0F 87 72 FD FF FF               ja 0x1402371a9
00237437  83 C9 04                        or ecx, 4
0023743A  41 89 4F 10                     mov dword ptr [r15 + 0x10], ecx
0023743E  E9 66 FD FF FF                  jmp 0x1402371a9
00237443  8B 05 6F F6 D8 00               mov eax, dword ptr [rip + 0xd8f66f]
00237449  A8 40                           test al, 0x40
0023744B  0F 84 FF FD FF FF               je 0x140237250
00237451  E8 3A 80 0D 00                  call 0x14030f490
00237456  84 C0                           test al, al
00237458  0F 84 F2 FD FF FF               je 0x140237250
0023745E  41 8B CC                        mov ecx, r12d
00237461  E8 FA 7F 0D 00                  call 0x14030f460
00237466  E9 E7 FD FF FF                  jmp 0x140237252
0023746B  48 0F BA E3 0B                  bt rbx, 0xb
00237470  0F 83 20 FC FF FF               jae 0x140237096
00237476  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0023747B  48 B8 FF 0F 00 00 00 00 F0 FF   movabs rax, 0xfff0000000000fff
00237485  48 C1 E1 0C                     shl rcx, 0xc
00237489  48 33 F1                        xor rsi, rcx
0023748C  48 23 F0                        and rsi, rax
0023748F  48 33 F1                        xor rsi, rcx
00237492  49 8B CE                        mov rcx, r14
00237495  48 8B D6                        mov rdx, rsi
00237498  E8 73 A3 04 00                  call 0x140281810
0023749D  48 8B 05 E4 F5 D8 00            mov rax, qword ptr [rip + 0xd8f5e4]
002374A4  48 0F BA E0 08                  bt rax, 8
002374A9  0F 83 D5 00 00 00               jae 0x140237584
002374AF  48 8B D6                        mov rdx, rsi
002374B2  48 8B CB                        mov rcx, rbx
002374B5  E8 76 D7 14 00                  call 0x140384c30
002374BA  85 C0                           test eax, eax
002374BC  0F 84 D2 00 00 00               je 0x140237594
002374C2  BD 01 00 00 00                  mov ebp, 1
002374C7  8B C5                           mov eax, ebp
002374C9  F6 C3 42                        test bl, 0x42
002374CC  45 0F B6 ED                     movzx r13d, r13b
002374D0  44 0F 45 ED                     cmovne r13d, ebp
002374D4  45 33 E4                        xor r12d, r12d
002374D7  85 C0                           test eax, eax
002374D9  0F 84 AF FD FF FF               je 0x14023728e
002374DF  E9 20 FC FF FF                  jmp 0x140237104
002374E4  41 80 7F 19 00                  cmp byte ptr [r15 + 0x19], 0
002374E9  0F 85 98 FD FF FF               jne 0x140237287
002374EF  49 8B D1                        mov rdx, r9
002374F2  49 8D 4F 28                     lea rcx, [r15 + 0x28]
002374F6  4C 8D 0D 93 E3 45 00            lea r9, [rip + 0x45e393]
002374FD  41 B8 08 00 00 00               mov r8d, 8
00237503  E8 E8 94 2C 00                  call 0x1405009f0
00237508  49 8B CF                        mov rcx, r15
0023750B  E8 98 1E 07 00                  call 0x1402a93a8
00237510  BD 01 00 00 00                  mov ebp, 1
00237515  E9 92 FC FF FF                  jmp 0x1402371ac
0023751A  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
0023751F  E8 44 D6 05 00                  call 0x140294b68
00237524  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00237529  8B D8                           mov ebx, eax
0023752B  E9 B2 FB FF FF                  jmp 0x1402370e2
00237530  41 83 4F 10 09                  or dword ptr [r15 + 0x10], 9
00237535  41 8B C4                        mov eax, r12d
00237538  E9 37 FC FF FF                  jmp 0x140237174
0023753D  45 33 E4                        xor r12d, r12d
00237540  E9 49 FD FF FF                  jmp 0x14023728e
00237545  81 E1 FF 03 00 00               and ecx, 0x3ff
0023754B  48 8D 14 0B                     lea rdx, [rbx + rcx]
0023754F  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
00237556  0F 87 F4 FD FF FF               ja 0x140237350
0023755C  48 3B D1                        cmp rdx, rcx
0023755F  0F 86 EB FD FF FF               jbe 0x140237350
00237565  49 01 5F 20                     add qword ptr [r15 + 0x20], rbx
00237569  49 2B C3                        sub rax, r11
0023756C  48 8D 0C 18                     lea rcx, [rax + rbx]
00237570  48 33 C1                        xor rax, rcx
00237573  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00237579  48 33 C1                        xor rax, rcx
0023757C  49 89 02                        mov qword ptr [r10], rax
0023757F  E9 03 FD FF FF                  jmp 0x140237287
00237584  48 0F BA E0 09                  bt rax, 9
00237589  0F 83 33 FF FF FF               jae 0x1402374c2
0023758F  E9 1B FF FF FF                  jmp 0x1402374af
00237594  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
0023759B  BD 01 00 00 00                  mov ebp, 1
002375A0  E9 24 FF FF FF                  jmp 0x1402374c9
002375A5  48 8B D7                        mov rdx, rdi
002375A8  49 8B CE                        mov rcx, r14
002375AB  E8 FC D8 05 00                  call 0x140294eac
002375B0  E9 47 FB FF FF                  jmp 0x1402370fc
002375B5  49 01 5F 20                     add qword ptr [r15 + 0x20], rbx
002375B9  48 8D 0C 18                     lea rcx, [rax + rbx]
002375BD  48 33 C1                        xor rax, rcx
002375C0  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
002375C6  48 33 C1                        xor rax, rcx
002375C9  49 89 42 28                     mov qword ptr [r10 + 0x28], rax
002375CD  E9 B5 FC FF FF                  jmp 0x140237287
002375D2  41 C6 47 19 01                  mov byte ptr [r15 + 0x19], 1
002375D7  E9 AB FC FF FF                  jmp 0x140237287
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmSetAddressRangeModifiedEx(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
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
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pB8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (88);
    v_stack_p18 = 0;
    v_r13 = 0;
    result = MiMakeProtectionMask(4, a2, a2, a4);
    v_stack_p10 = (unsigned int)(result);
    v_r14 = (a1) >> (9);
    v_r12 = 0;
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (a2);
    a1 = (a2 - 1) + (a1);
    a1 = (a1) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (a2);
    v_stack_m78 = a1;
    v_rbx = (a1) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p8 = v_rbx;
    result = MiLockWorkingSetOptimal(v_rip + 12609230, v_r14, v_stack_p18, a4);
    v_stack_m58 = result;
    result = MiGetMultiplexedVm(v_rip + 12609230, v_rbx, v_stack_p18, a4);
    v_stack_m68 = result;
loc_00236FF3:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_00237261;
    v_stack_p20 = 0;
    result = (*(unsigned __int64 *)(v_r14)) >> (12);
    v_stack_m60 = result;
    result = (result) & (v_stack_p18);
    v_rbp = (result + result * 2) << (4);
    v_rbp = (v_rbp) + (v_rbx);
loc_00237027:
    if (condition_is_below) goto loc_00237240;
    result = (*(unsigned __int64 *)(v_rbp + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (((*(unsigned __int8 *)(v_rbp + 34)) & (16)) == 0) goto loc_00237230;
    if (condition_is_above_or_equal) goto loc_00237230;
loc_00237064:
    result = (unsigned int)(*(unsigned int *)(v_rbp + 16));
    if (0 != 0) {
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12554313) + result * 8);
        result = MiReleasePageFileInfo(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(v_stack_p10))) == 2) goto loc_0023746B;
loc_00237096:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (66)) == 0) goto loc_0023753D;
    result = MI_READ_PTE_LOCK_FREE(v_r14, a2, a3, a4);
    v_r12 = 0;
    v_rdi = (result) & (result);
    v_rbx = (*(unsigned __int64 *)(v_r14)) & (result);
    v_rdi = (v_rdi) | (v_rbx);
    v_stack_m70 = v_rdi;
    result = MiPteInShadowRange(v_r14, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0023751A;
loc_002370E2:
    if (condition_is_below) goto loc_002373BB;
loc_002370F1:
    *(unsigned __int64 *)(v_r14) = v_rdi;
    if (0 != 0) goto loc_002375A5;
loc_002370FC:
loc_00237104:
    if (0 != 0) goto loc_00237190;
    result = MiGetProcessorFlushList(v_r14, a2, a3, a4);
    *(unsigned int *)(result + 16) = 0;
    *(unsigned int *)(result + 20) = 32;
    *(unsigned __int64 *)(result) = v_stack_m68;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m68 + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m68 + 184)))) & (15)) != 0) goto loc_00237164;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_stack_m68 != a1) goto loc_00237530;
loc_00237164:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m68 + 184)))) & (15)) != 0) goto loc_00237535;
loc_00237174:
    *(unsigned int *)(result + 8) = 1;
    *(unsigned __int16 *)(result + 25) = 0;
    *(unsigned int *)(result + 28) = 0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
loc_00237190:
    if ((*(unsigned int *)(result + 8)) != 1) goto loc_002373FE;
loc_002371A9:
loc_002371AC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 28))) == 0) goto loc_00237350;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (2)) != 0) goto loc_0023730A;
    if (((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0xC00ULL)) != 0) goto loc_00237350;
    a3 = (unsigned int)((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_stack_p8) goto loc_00237218;
    if ((1 + a3 * 1) <= a3) goto loc_00237218;
    if ((1 + a3 * 1) <= 0x3FFULL) goto loc_002375B5;
loc_00237218:
    goto loc_00237332;
loc_00237230:
    result = MiCaptureDirtyBitToPfn(0, a2, a3, (unsigned int)(*(unsigned int *)(result + 28)));
    goto loc_00237064;
loc_00237240:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 14213218)) & ((unsigned int)(v_r12))) == 0) goto loc_00237443;
loc_00237250:
loc_00237252:
    if (!sign_flag) goto loc_00237027;
    goto loc_00237240;
loc_00237261:
    if (((unsigned int)(result)) != 2) goto loc_002372AF;
    if (((1) & (8)) != 0) goto loc_002372AF;
    v_rbx = (1) | (8);
    *(unsigned __int64 *)(v_r14) = v_rbx;
    goto loc_002372AF;
loc_00237274:
    if (0 == 0) goto loc_002374E4;
    if ((*(unsigned __int8 *)(result + 25)) == 0) goto loc_002375D2;
loc_00237287:
loc_0023728E:
loc_002372AF:
    result = (v_stack_p8) + (0x1000ULL);
    v_r14 = (v_r14) + (8);
    v_stack_p8 = result;
    if (v_r14 <= v_stack_m78) goto loc_00236FF3;
    if (result != 0) {
        a1 = result;
        result = MiFlushTbList(a1, a2, a3, (unsigned int)(*(unsigned int *)(result + 28)));
        result = MiReleaseProcessorFlushList(a1, a2, a3, (unsigned int)(*(unsigned int *)(result + 28)));
    }
    result = MiUnlockWorkingSetOptimal(v_stack_m68, v_stack_m58, v_stack_p18, (unsigned int)(*(unsigned int *)(result + 28)));
    v_rsp = (v_rsp) + (88);
    return 1;
loc_0023730A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 28))) == 0) goto loc_00237350;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (2)) != 0) goto loc_00237350;
    if (((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 + 5 * 8)) & (0xC00ULL)) != 0) goto loc_00237350;
loc_00237332:
    v_r11 = (v_rbx) << (12);
    a2 = (*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 + 5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == ((unsigned int)(v_stack_p10) + v_r11 * 1)) goto loc_00237545;
loc_00237350:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 28)))) == (*(unsigned int *)(result + 12))) goto loc_00237274;
loc_0023735A:
    if (v_rbx == 0) goto loc_00237287;
    a2 = (unsigned int)(0x400ULL);
    if ((v_rbx - 1) <= 0x3FFULL) { a2 = v_rbx; }
    a1 = ((unsigned int)(v_stack_p10)) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) * 8 + 40) = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 28))) + 1);
    a1 = (a2) << (12);
    v_rdi = ((unsigned int)(v_stack_p10)) + (a1);
    *(unsigned int *)(result + 28) = (unsigned int)(a4);
    v_rbx = (v_rbx) - (a2);
    if (condition_is_equal) goto loc_0023735A;
    if (((unsigned int)(a4)) == (*(unsigned int *)(result + 12))) goto loc_002371A9;
    goto loc_0023735A;
loc_002373BB:
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_002370F1;
    a1 = (result) + (result);
    if (v_r14 < a1) goto loc_002370F1;
    result = MiCheckLinearProtectedPteAccessedBit(v_r14, v_rdi, 128, a4);
    goto loc_002370F1;
loc_002373FE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (4)) != 0) goto loc_002371A9;
    if (v_rdi < result) goto loc_002371A9;
    if (v_rdi > result) goto loc_002371A9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) | (4));
    *(unsigned int *)(result + 16) = (unsigned int)(a1);
    goto loc_002371A9;
loc_00237443:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14218863)))) & (64)) == 0) goto loc_00237250;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_rdi, 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00237250;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_rdi, 128, a4);
    goto loc_00237252;
loc_0023746B:
    if (condition_is_above_or_equal) goto loc_00237096;
    a1 = (v_stack_p38) << (12);
    v_rsi = (0) ^ (a1);
    v_rsi = (v_rsi) & (result);
    v_rsi = (v_rsi) ^ (a1);
    result = MiWriteValidPteNewProtection(v_r14, v_rsi, 128, a4);
    if (condition_is_above_or_equal) goto loc_00237584;
loc_002374AF:
    result = MI_TIGHTER_PERMISSIONS(v_rbx, v_rsi, 128, a4);
    if ((unsigned int)(result) == 0) goto loc_00237594;
loc_002374C2:
loc_002374C9:
    v_r13 = 1;
    if ((((unsigned __int8)(v_rbx)) & (66)) != 0) { v_r13 = 1; }
    v_r12 = 0;
    if (1 == 0) goto loc_0023728E;
    goto loc_00237104;
loc_002374E4:
    if ((*(unsigned __int8 *)(result + 25)) != 0) goto loc_00237287;
    result = qsort(result + 40, a4, 8, v_rip + 4580243);
    result = MiCompressTbFlushList(result, a4, 8, v_rip + 4580243);
    goto loc_002371AC;
loc_0023751A:
    result = MiSanitizeShadowPxe(result, v_stack_p28, 8, v_rip + 4580243);
    goto loc_002370E2;
loc_00237530:
loc_00237535:
    goto loc_00237174;
loc_0023753D:
    v_r12 = 0;
    goto loc_0023728E;
loc_00237545:
    a1 = (unsigned int)((result) & (0x3FFULL));
    if (((unsigned int)((unsigned int)(result)) + a1 * 1) > 0x3FFULL) goto loc_00237350;
    if (((unsigned int)((unsigned int)(result)) + a1 * 1) <= a1) goto loc_00237350;
    result = (0) - (v_r11);
    result = (result) ^ (result + (unsigned int)((unsigned int)(result)) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (unsigned int)((unsigned int)(result)) * 1);
    *(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 + 5 * 8) = result;
    goto loc_00237287;
loc_00237584:
    if (condition_is_above_or_equal) goto loc_002374C2;
    goto loc_002374AF;
loc_00237594:
    goto loc_002374C9;
loc_002375A5:
    result = MiWritePteShadow(v_r14, v_stack_p28, 8, v_rip + 4580243);
    goto loc_002370FC;
loc_002375B5:
    result = (result) ^ (result + (unsigned int)((unsigned int)(result)) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (unsigned int)((unsigned int)(result)) * 1);
    *(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 + 5 * 8 + 40) = result;
    goto loc_00237287;
loc_002375D2:
    *(unsigned __int8 *)(result + 25) = 1;
    goto loc_00237287;
}
```

## 5. (Beta) C Style

```c
int64_t MmSetAddressRangeModifiedEx(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
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
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;
    uint32_t v_stack_pB8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (88);
    v_stack_p18 = 0;
    local_r13 = 0;
    result = MiMakeProtectionMask(4, Arg2, Arg2, a4);
    v_stack_p10 = (uint32_t)(result);
    local_r14 = (Arg1) >> (9);
    local_r12 = 0;
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (Arg2);
    Arg1 = (Arg2 - 1) + (Arg1);
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (Arg2);
    v_stack_m78 = Arg1;
    local_rbx = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p8 = local_rbx;
    result = MiLockWorkingSetOptimal(v_rip + 12609230, local_r14, v_stack_p18, a4);
    v_stack_m58 = result;
    result = MiGetMultiplexedVm(v_rip + 12609230, local_rbx, v_stack_p18, a4);
    v_stack_m68 = result;
loc_00236FF3:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_00237261;
    v_stack_p20 = 0;
    result = (*(uint64_t *)(local_r14)) >> (12);
    v_stack_m60 = result;
    result = (result) & (v_stack_p18);
    local_rbp = (result + result * 2) << (4);
    local_rbp = (local_rbp) + (local_rbx);
loc_00237027:
    if (condition_is_below) goto loc_00237240;
    result = (*(uint64_t *)(local_rbp + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (((*(uint8_t *)(local_rbp + 0x22)) & (16)) == 0) goto loc_00237230;
    if (condition_is_above_or_equal) goto loc_00237230;
loc_00237064:
    result = (uint32_t)(*(uint32_t *)(local_rbp + 0x10));
    if (0 != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBF9049) + result * 8);
        result = MiReleasePageFileInfo(Arg1, Arg2, Arg3, a4);
    }
    if (((uint32_t)((uint32_t)(v_stack_p10))) == 2) goto loc_0023746B;
loc_00237096:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (66)) == 0) goto loc_0023753D;
    result = MI_READ_PTE_LOCK_FREE(local_r14, Arg2, Arg3, a4);
    local_r12 = 0;
    local_rdi = (result) & (result);
    local_rbx = (*(uint64_t *)(local_r14)) & (result);
    local_rdi = (local_rdi) | (local_rbx);
    v_stack_m70 = local_rdi;
    result = MiPteInShadowRange(local_r14, Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_0023751A;
loc_002370E2:
    if (condition_is_below) goto loc_002373BB;
loc_002370F1:
    *(uint64_t *)(local_r14) = local_rdi;
    if (0 != 0) goto loc_002375A5;
loc_002370FC:
loc_00237104:
    if (0 != 0) goto loc_00237190;
    result = MiGetProcessorFlushList(local_r14, Arg2, Arg3, a4);
    *(uint32_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0x14) = 32;
    *(uint64_t *)(result) = v_stack_m68;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m68 + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    *(uint8_t *)(result + 0x18) = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0xB8)))) & (15)) != 0) goto loc_00237164;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (v_stack_m68 != Arg1) goto loc_00237530;
loc_00237164:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0xB8)))) & (15)) != 0) goto loc_00237535;
loc_00237174:
    *(uint32_t *)(result + 0x8) = 1;
    *(uint16_t *)(result + 0x19) = 0;
    *(uint32_t *)(result + 0x1C) = 0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
loc_00237190:
    if ((*(uint32_t *)(result + 0x8)) != 1) goto loc_002373FE;
loc_002371A9:
loc_002371AC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C))) == 0) goto loc_00237350;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (2)) != 0) goto loc_0023730A;
    if (((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0xC00ULL)) != 0) goto loc_00237350;
    Arg3 = (uint32_t)((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0x3FFULL));
    Arg1 = (*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg3 + 1) << (12);
    Arg2 = (Arg2) + (Arg1);
    if (Arg2 != v_stack_p8) goto loc_00237218;
    if ((1 + Arg3 * 1) <= Arg3) goto loc_00237218;
    if ((1 + Arg3 * 1) <= 0x3FFULL) goto loc_002375B5;
loc_00237218:
    goto loc_00237332;
loc_00237230:
    result = MiCaptureDirtyBitToPfn(0, Arg2, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    goto loc_00237064;
loc_00237240:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD8E062)) & ((uint32_t)(local_r12))) == 0) goto loc_00237443;
loc_00237250:
loc_00237252:
    if (!sign_flag) goto loc_00237027;
    goto loc_00237240;
loc_00237261:
    if (((uint32_t)(result)) != 2) goto loc_002372AF;
    if (((1) & (8)) != 0) goto loc_002372AF;
    local_rbx = (1) | (8);
    *(uint64_t *)(local_r14) = local_rbx;
    goto loc_002372AF;
loc_00237274:
    if (0 == 0) goto loc_002374E4;
    if ((*(uint8_t *)(result + 0x19)) == 0) goto loc_002375D2;
loc_00237287:
loc_0023728E:
loc_002372AF:
    result = (v_stack_p8) + (0x1000ULL);
    local_r14 = (local_r14) + (8);
    v_stack_p8 = result;
    if (local_r14 <= v_stack_m78) goto loc_00236FF3;
    if (result != 0) {
        Arg1 = result;
        result = MiFlushTbList(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
        result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    }
    result = MiUnlockWorkingSetOptimal(v_stack_m68, v_stack_m58, v_stack_p18, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    local_rsp = (local_rsp) + (88);
    return 1;
loc_0023730A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C))) == 0) goto loc_00237350;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (2)) != 0) goto loc_00237350;
    if (((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 + 0x5 * 8)) & (0xC00ULL)) != 0) goto loc_00237350;
loc_00237332:
    local_r11 = (local_rbx) << (12);
    Arg2 = (*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 + 0x5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg2 == ((uint32_t)(v_stack_p10) + local_r11 * 1)) goto loc_00237545;
loc_00237350:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C)))) == (*(uint32_t *)(result + 0xC))) goto loc_00237274;
loc_0023735A:
    if (local_rbx == 0) goto loc_00237287;
    Arg2 = (uint32_t)(0x400ULL);
    if ((local_rbx - 1) <= 0x3FFULL) { Arg2 = local_rbx; }
    Arg1 = ((uint32_t)(v_stack_p10)) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((Arg2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    *(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) * 8 + 0x28) = result;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x1C))) + 1);
    Arg1 = (Arg2) << (12);
    local_rdi = ((uint32_t)(v_stack_p10)) + (Arg1);
    *(uint32_t *)(result + 0x1C) = (uint32_t)(a4);
    local_rbx = (local_rbx) - (Arg2);
    if (condition_is_equal) goto loc_0023735A;
    if (((uint32_t)(a4)) == (*(uint32_t *)(result + 0xC))) goto loc_002371A9;
    goto loc_0023735A;
loc_002373BB:
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_002370F1;
    Arg1 = (result) + (result);
    if (local_r14 < Arg1) goto loc_002370F1;
    result = MiCheckLinearProtectedPteAccessedBit(local_r14, local_rdi, 128, a4);
    goto loc_002370F1;
loc_002373FE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (4)) != 0) goto loc_002371A9;
    if (local_rdi < result) goto loc_002371A9;
    if (local_rdi > result) goto loc_002371A9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) | (4));
    *(uint32_t *)(result + 0x10) = (uint32_t)(Arg1);
    goto loc_002371A9;
loc_00237443:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD8F66F)))) & (64)) == 0) goto loc_00237250;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, local_rdi, 128, a4);
    if ((uint8_t)(result) == 0) goto loc_00237250;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), local_rdi, 128, a4);
    goto loc_00237252;
loc_0023746B:
    if (condition_is_above_or_equal) goto loc_00237096;
    Arg1 = (v_stack_p38) << (12);
    local_rsi = (0) ^ (Arg1);
    local_rsi = (local_rsi) & (result);
    local_rsi = (local_rsi) ^ (Arg1);
    result = MiWriteValidPteNewProtection(local_r14, local_rsi, 128, a4);
    if (condition_is_above_or_equal) goto loc_00237584;
loc_002374AF:
    result = MI_TIGHTER_PERMISSIONS(local_rbx, local_rsi, 128, a4);
    if ((uint32_t)(result) == 0) goto loc_00237594;
loc_002374C2:
loc_002374C9:
    local_r13 = 1;
    if ((((uint8_t)(local_rbx)) & (66)) != 0) { local_r13 = 1; }
    local_r12 = 0;
    if (1 == 0) goto loc_0023728E;
    goto loc_00237104;
loc_002374E4:
    if ((*(uint8_t *)(result + 0x19)) != 0) goto loc_00237287;
    result = qsort(result + 40, a4, 8, v_rip + 4580243);
    result = MiCompressTbFlushList(result, a4, 8, v_rip + 4580243);
    goto loc_002371AC;
loc_0023751A:
    result = MiSanitizeShadowPxe(result, v_stack_p28, 8, v_rip + 4580243);
    goto loc_002370E2;
loc_00237530:
loc_00237535:
    goto loc_00237174;
loc_0023753D:
    local_r12 = 0;
    goto loc_0023728E;
loc_00237545:
    Arg1 = (uint32_t)((result) & (0x3FFULL));
    if (((uint32_t)((uint32_t)(result)) + Arg1 * 1) > 0x3FFULL) goto loc_00237350;
    if (((uint32_t)((uint32_t)(result)) + Arg1 * 1) <= Arg1) goto loc_00237350;
    result = (0) - (local_r11);
    result = (result) ^ (result + (uint32_t)((uint32_t)(result)) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (uint32_t)((uint32_t)(result)) * 1);
    *(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 + 0x5 * 8) = result;
    goto loc_00237287;
loc_00237584:
    if (condition_is_above_or_equal) goto loc_002374C2;
    goto loc_002374AF;
loc_00237594:
    goto loc_002374C9;
loc_002375A5:
    result = MiWritePteShadow(local_r14, v_stack_p28, 8, v_rip + 4580243);
    goto loc_002370FC;
loc_002375B5:
    result = (result) ^ (result + (uint32_t)((uint32_t)(result)) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (uint32_t)((uint32_t)(result)) * 1);
    *(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 + 0x5 * 8 + 0x28) = result;
    goto loc_00237287;
loc_002375D2:
    *(uint8_t *)(result + 0x19) = 1;
    goto loc_00237287;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00236F20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
