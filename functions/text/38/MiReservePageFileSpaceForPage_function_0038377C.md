# MiReservePageFileSpaceForPage

- RVA: `0x0038377C`–`0x00383E6F` (길이 `1,779` bytes)
- VA: `0x000000014038377C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007BBD4`
- 디코드: `424`개 명령, `1,779/1,779` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003837D6` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00383881` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x0038388A` → [MI_IS_RESET_PTE](MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x00383913` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00383929` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x003839A0` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00383A3F` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00383A79` → [MI_IS_RESET_PTE](MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x00383ABA` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x00383AED` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00383B2C` → [MiTransferSoftwarePte](MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x00383B5E` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00383B95` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x00383BF1` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x00383C14` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00383C6E` → [MiPageStandbyLookasideStatus](../40/MiPageStandbyLookasideStatus_function_0040E0B0.md) (function, `0x0040E0B0`)
- `0x00383C7A` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00383C88` → [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) (function, `0x00375954`)
- `0x00383D12` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x00383D21` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x00383D4C` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00383D77` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00383D89` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00383DBE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00383E07` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00383E16` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00383E31` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x00383E4E` → [MiPageStandbyLookasideStatus](../40/MiPageStandbyLookasideStatus_function_0040E0B0.md) (function, `0x0040E0B0`)

### Direct callers
- [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) at `0x003726DF`
- [MiReservePageFileSpace](MiReservePageFileSpace_function_00383ED8.md) at `0x003840F2`
- [MiReservePageFileSpace](MiReservePageFileSpace_function_00383ED8.md) at `0x00384137`
- [MiReservePageFileSpace](MiReservePageFileSpace_function_00383ED8.md) at `0x00384209`

### Static image references
- `0x0038384E` → RVA `0x00E30088` (`.data`; read)
- `0x00383932` → RVA `0x00E2DC80` (`.data`; read)
- `0x0038396B` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00383A08` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00383D69` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00383E60` → [sub_006E497E](../6E/Unknown_function_006E497E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0038377C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00383781  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00383786  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0038378B  55                              push rbp
0038378C  56                              push rsi
0038378D  57                              push rdi
0038378E  41 54                           push r12
00383790  41 55                           push r13
00383792  41 56                           push r14
00383794  41 57                           push r15
00383796  48 83 EC 40                     sub rsp, 0x40
0038379A  41 8B F8                        mov edi, r8d
0038379D  4C 8B FA                        mov r15, rdx
003837A0  45 33 C0                        xor r8d, r8d
003837A3  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
003837A8  41 8B F0                        mov esi, r8d
003837AB  44 89 84 24 90 00 00 00         mov dword ptr [rsp + 0x90], r8d
003837B3  45 8B E8                        mov r13d, r8d
003837B6  41 8D 58 01                     lea ebx, [r8 + 1]
003837BA  45 8B E0                        mov r12d, r8d
003837BD  48 BD FF FF FF FF FF 00 00 00   movabs rbp, 0xffffffffff
003837C7  40 84 FF                        test dil, dil
003837CA  0F 89 E5 02 00 00               jns 0x140383ab5
003837D0  4D 8B F0                        mov r14, r8
003837D3  49 8B CF                        mov rcx, r15
003837D6  E8 C5 F0 EF FF                  call 0x1402828a0
003837DB  41 BA 01 00 00 00               mov r10d, 1
003837E1  48 8B D8                        mov rbx, rax
003837E4  41 84 C2                        test r10b, al
003837E7  0F 84 05 01 00 00               je 0x1403838f2
003837ED  40 84 FF                        test dil, dil
003837F0  0F 89 6B 05 00 00               jns 0x140383d61
003837F6  48 C1 E8 0C                     shr rax, 0xc
003837FA  48 23 C5                        and rax, rbp
003837FD  4C 8D 34 40                     lea r14, [rax + rax*2]
00383801  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0038380B  49 C1 E6 04                     shl r14, 4
0038380F  48 8B C0                        mov rax, rax
00383812  4C 03 F0                        add r14, rax
00383815  45 33 C0                        xor r8d, r8d
00383818  41 84 FA                        test r10b, dil
0038381B  75 1C                           jne 0x140383839
0038381D  41 8B F2                        mov esi, r10d
00383820  45 8B E2                        mov r12d, r10d
00383823  41 8B E8                        mov ebp, r8d
00383826  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
0038382D  0F 82 D3 01 00 00               jb 0x140383a06
00383833  49 8B F5                        mov rsi, r13
00383836  45 8B D4                        mov r10d, r12d
00383839  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0038383D  48 85 C0                        test rax, rax
00383840  78 76                           js 0x1403838b8
00383842  49 8B 06                        mov rax, qword ptr [r14]
00383845  41 84 C2                        test r10b, al
00383848  74 6E                           je 0x1403838b8
0038384A  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0038384E  48 8B 0D 33 C8 AA 00            mov rcx, qword ptr [rip + 0xaac833]
00383855  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
0038385D  48 C1 E8 2B                     shr rax, 0x2b
00383861  25 FF 03 00 00                  and eax, 0x3ff
00383866  48 39 2C C1                     cmp qword ptr [rcx + rax*8], rbp
0038386A  75 4C                           jne 0x1403838b8
0038386C  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00383870  C1 E8 18                        shr eax, 0x18
00383873  A8 08                           test al, 8
00383875  75 41                           jne 0x1403838b8
00383877  48 8B D3                        mov rdx, rbx
0038387A  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
0038387E  48 8B CB                        mov rcx, rbx
00383881  E8 8A F1 FE FF                  call 0x140372a10
00383886  85 C0                           test eax, eax
00383888  74 2E                           je 0x1403838b8
0038388A  E8 F1 05 00 00                  call 0x140383e80
0038388F  85 C0                           test eax, eax
00383891  0F 85 2D 05 00 00               jne 0x140383dc4
00383897  8A C3                           mov al, bl
00383899  D0 E8                           shr al, 1
0038389B  41 84 C2                        test r10b, al
0038389E  0F 85 3C 05 00 00               jne 0x140383de0
003838A4  4D 85 F6                        test r14, r14
003838A7  0F 84 21 02 00 00               je 0x140383ace
003838AD  41 F6 46 22 28                  test byte ptr [r14 + 0x22], 0x28
003838B2  0F 84 16 02 00 00               je 0x140383ace
003838B8  45 85 E4                        test r12d, r12d
003838BB  74 0F                           je 0x1403838cc
003838BD  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003838C7  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003838CC  48 85 F6                        test rsi, rsi
003838CF  0F 85 59 01 00 00               jne 0x140383a2e
003838D5  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
003838D9  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
003838E1  48 83 C4 40                     add rsp, 0x40
003838E5  41 5F                           pop r15
003838E7  41 5E                           pop r14
003838E9  41 5D                           pop r13
003838EB  41 5C                           pop r12
003838ED  5F                              pop rdi
003838EE  5E                              pop rsi
003838EF  5D                              pop rbp
003838F0  C3                              ret
003838F1  CC                              int3
003838F2  48 0F BA E3 0A                  bt rbx, 0xa
003838F7  72 BF                           jb 0x1403838b8
003838F9  48 0F BA E3 0B                  bt rbx, 0xb
003838FE  0F 83 82 02 00 00               jae 0x140383b86
00383904  40 84 FF                        test dil, dil
00383907  0F 89 3C 01 00 00               jns 0x140383a49
0038390D  45 33 E4                        xor r12d, r12d
00383910  49 8B CF                        mov rcx, r15
00383913  E8 88 EF EF FF                  call 0x1402828a0
00383918  48 8B D8                        mov rbx, rax
0038391B  48 0F BA E0 0B                  bt rax, 0xb
00383920  0F 83 1A 05 00 00               jae 0x140383e40
00383926  48 8B C8                        mov rcx, rax
00383929  E8 E2 F0 FE FF                  call 0x140372a10
0038392E  85 C0                           test eax, eax
00383930  74 DE                           je 0x140383910
00383932  48 8B 05 47 A3 AA 00            mov rax, qword ptr [rip + 0xaaa347]
00383939  48 85 C0                        test rax, rax
0038393C  74 12                           je 0x140383950
0038393E  F6 C3 10                        test bl, 0x10
00383941  0F 85 DE 00 00 00               jne 0x140383a25
00383947  48 8B C8                        mov rcx, rax
0038394A  48 F7 D1                        not rcx
0038394D  48 23 CB                        and rcx, rbx
00383950  48 C1 E9 0C                     shr rcx, 0xc
00383954  48 23 CD                        and rcx, rbp
00383957  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00383961  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00383965  48 03 D2                        add rdx, rdx
00383968  48 8B C0                        mov rax, rax
0038396B  48 3B 0D 6E A3 AA 00            cmp rcx, qword ptr [rip + 0xaaa36e]
00383972  4C 8D 34 D0                     lea r14, [rax + rdx*8]
00383976  77 98                           ja 0x140383910
00383978  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00383982  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
00383986  48 0F BA E0 36                  bt rax, 0x36
0038398B  73 83                           jae 0x140383910
0038398D  41 8B EC                        mov ebp, r12d
00383990  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00383997  0F 82 F9 00 00 00               jb 0x140383a96
0038399D  49 8B CF                        mov rcx, r15
003839A0  E8 FB EE EF FF                  call 0x1402828a0
003839A5  48 3B C3                        cmp rax, rbx
003839A8  0F 85 E4 02 00 00               jne 0x140383c92
003839AE  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003839B2  48 8B 0D CF C6 AA 00            mov rcx, qword ptr [rip + 0xaac6cf]
003839B9  48 C1 E8 2B                     shr rax, 0x2b
003839BD  25 FF 03 00 00                  and eax, 0x3ff
003839C2  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003839C6  8B 40 04                        mov eax, dword ptr [rax + 4]
003839C9  84 C0                           test al, al
003839CB  0F 88 4B 03 00 00               js 0x140383d1c
003839D1  45 33 C0                        xor r8d, r8d
003839D4  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003839D8  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
003839E2  48 0B C1                        or rax, rcx
003839E5  49 3B C7                        cmp rax, r15
003839E8  0F 85 A8 03 00 00               jne 0x140383d96
003839EE  4D 85 F6                        test r14, r14
003839F1  0F 85 B9 02 00 00               jne 0x140383cb0
003839F7  48 BD FF FF FF FF FF 00 00 00   movabs rbp, 0xffffffffff
00383A01  E9 3D 04 00 00                  jmp 0x140383e43
00383A06  03 EE                           add ebp, esi
00383A08  85 2D 9E 18 C4 00               test dword ptr [rip + 0xc4189e], ebp
00383A0E  0F 84 55 03 00 00               je 0x140383d69
00383A14  F3 90                           pause
00383A16  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00383A1A  48 85 C0                        test rax, rax
00383A1D  0F 89 03 FE FF FF               jns 0x140383826
00383A23  EB E1                           jmp 0x140383a06
00383A25  48 83 E1 EF                     and rcx, 0xffffffffffffffef
00383A29  E9 22 FF FF FF                  jmp 0x140383950
00383A2E  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00383A36  41 B8 01 00 00 00               mov r8d, 1
00383A3C  48 8B D6                        mov rdx, rsi
00383A3F  E8 8C 05 F0 FF                  call 0x140283fd0
00383A44  E9 8C FE FF FF                  jmp 0x1403838d5
00383A49  45 33 C0                        xor r8d, r8d
00383A4C  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00383A50  48 8B 0D 31 C6 AA 00            mov rcx, qword ptr [rip + 0xaac631]
00383A57  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
00383A5F  48 C1 E8 2B                     shr rax, 0x2b
00383A63  25 FF 03 00 00                  and eax, 0x3ff
00383A68  48 39 2C C1                     cmp qword ptr [rcx + rax*8], rbp
00383A6C  0F 85 46 FE FF FF               jne 0x1403838b8
00383A72  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
00383A76  48 8B CB                        mov rcx, rbx
00383A79  E8 02 04 00 00                  call 0x140383e80
00383A7E  85 C0                           test eax, eax
00383A80  0F 84 11 FE FF FF               je 0x140383897
00383A86  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
00383A8B  0F 85 06 FE FF FF               jne 0x140383897
00383A91  E9 22 FE FF FF                  jmp 0x1403838b8
00383A96  FF C5                           inc ebp
00383A98  85 2D 0E 18 C4 00               test dword ptr [rip + 0xc4180e], ebp
00383A9E  0F 84 55 03 00 00               je 0x140383df9
00383AA4  F3 90                           pause
00383AA6  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00383AAA  48 85 C0                        test rax, rax
00383AAD  0F 89 DD FE FF FF               jns 0x140383990
00383AB3  EB E1                           jmp 0x140383a96
00383AB5  33 D2                           xor edx, edx
00383AB7  49 8B CF                        mov rcx, r15
00383ABA  E8 01 1E FE FF                  call 0x1403658c0
00383ABF  48 85 C0                        test rax, rax
00383AC2  4C 8B F0                        mov r14, rax
00383AC5  44 0F 45 E3                     cmovne r12d, ebx
00383AC9  E9 05 FD FF FF                  jmp 0x1403837d3
00383ACE  8A C3                           mov al, bl
00383AD0  C0 E8 02                        shr al, 2
00383AD3  41 84 C2                        test r10b, al
00383AD6  0F 85 4B 01 00 00               jne 0x140383c27
00383ADC  41 84 FA                        test r10b, dil
00383ADF  0F 85 91 00 00 00               jne 0x140383b76
00383AE5  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00383AED  E8 AE ED EF FF                  call 0x1402828a0
00383AF2  48 8B C8                        mov rcx, rax
00383AF5  48 C1 E9 0C                     shr rcx, 0xc
00383AF9  83 E1 0F                        and ecx, 0xf
00383AFC  48 8B 94 CD 60 48 00 00         mov rdx, qword ptr [rbp + rcx*8 + 0x4860]
00383B04  48 8B 0D 75 A1 AA 00            mov rcx, qword ptr [rip + 0xaaa175]
00383B0B  48 85 C9                        test rcx, rcx
00383B0E  74 0A                           je 0x140383b1a
00383B10  A8 10                           test al, 0x10
00383B12  75 6C                           jne 0x140383b80
00383B14  48 F7 D1                        not rcx
00383B17  48 23 C1                        and rax, rcx
00383B1A  48 C1 E8 20                     shr rax, 0x20
00383B1E  BF 02 00 00 00                  mov edi, 2
00383B23  44 8B CF                        mov r9d, edi
00383B26  44 8B C0                        mov r8d, eax
00383B29  48 8B CB                        mov rcx, rbx
00383B2C  E8 BF E6 FF FF                  call 0x1403821f0
00383B31  45 33 C0                        xor r8d, r8d
00383B34  48 8B D8                        mov rbx, rax
00383B37  4D 85 F6                        test r14, r14
00383B3A  0F 84 8B 01 00 00               je 0x140383ccb
00383B40  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00383B44  66 85 C0                        test ax, ax
00383B47  0F 84 AE 00 00 00               je 0x140383bfb
00383B4D  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
00383B51  45 85 ED                        test r13d, r13d
00383B54  74 10                           je 0x140383b66
00383B56  BA 08 00 00 00                  mov edx, 8
00383B5B  49 8B CE                        mov rcx, r14
00383B5E  E8 9D 64 F3 FF                  call 0x1402ba000
00383B63  45 33 C0                        xor r8d, r8d
00383B66  44 39 84 24 90 00 00 00         cmp dword ptr [rsp + 0x90], r8d
00383B6E  75 5A                           jne 0x140383bca
00383B70  41 BA 01 00 00 00               mov r10d, 1
00383B76  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
00383B7B  E9 38 FD FF FF                  jmp 0x1403838b8
00383B80  48 83 E0 EF                     and rax, 0xffffffffffffffef
00383B84  EB 94                           jmp 0x140383b1a
00383B86  45 33 C0                        xor r8d, r8d
00383B89  48 85 DB                        test rbx, rbx
00383B8C  0F 84 A8 01 00 00               je 0x140383d3a
00383B92  48 8B CB                        mov rcx, rbx
00383B95  E8 76 EE FE FF                  call 0x140372a10
00383B9A  85 C0                           test eax, eax
00383B9C  0F 84 16 FD FF FF               je 0x1403838b8
00383BA2  48 8B C3                        mov rax, rbx
00383BA5  48 C1 E8 05                     shr rax, 5
00383BA9  83 E0 1F                        and eax, 0x1f
00383BAC  83 F8 10                        cmp eax, 0x10
00383BAF  0F 84 03 FD FF FF               je 0x1403838b8
00383BB5  85 C0                           test eax, eax
00383BB7  0F 84 FB FC FF FF               je 0x1403838b8
00383BBD  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
00383BC5  E9 CD FC FF FF                  jmp 0x140383897
00383BCA  49 C1 EF 09                     shr r15, 9
00383BCE  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
00383BD8  49 23 D7                        and rdx, r15
00383BDB  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00383BE5  48 03 D0                        add rdx, rax
00383BE8  44 8B CF                        mov r9d, edi
00383BEB  41 B8 01 00 00 00               mov r8d, 1
00383BF1  E8 3A FA EB FF                  call 0x140243630
00383BF6  E9 75 FF FF FF                  jmp 0x140383b70
00383BFB  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
00383C00  0F 84 47 FF FF FF               je 0x140383b4d
00383C06  45 85 ED                        test r13d, r13d
00383C09  0F 85 3E FF FF FF               jne 0x140383b4d
00383C0F  33 D2                           xor edx, edx
00383C11  49 8B CE                        mov rcx, r14
00383C14  E8 77 39 F0 FF                  call 0x140287590
00383C19  45 33 C0                        xor r8d, r8d
00383C1C  41 BD 01 00 00 00               mov r13d, 1
00383C22  E9 26 FF FF FF                  jmp 0x140383b4d
00383C27  4D 85 F6                        test r14, r14
00383C2A  0F 84 88 FC FF FF               je 0x1403838b8
00383C30  41 84 FA                        test r10b, dil
00383C33  0F 85 3D FF FF FF               jne 0x140383b76
00383C39  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00383C3D  66 85 C0                        test ax, ax
00383C40  0F 85 A9 00 00 00               jne 0x140383cef
00383C46  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00383C50  48 8B C0                        mov rax, rax
00383C53  49 8B FE                        mov rdi, r14
00383C56  48 2B F8                        sub rdi, rax
00383C59  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00383C63  48 C1 FF 04                     sar rdi, 4
00383C67  48 0F AF F8                     imul rdi, rax
00383C6B  48 8B CF                        mov rcx, rdi
00383C6E  E8 3D A4 08 00                  call 0x14040e0b0
00383C73  33 D2                           xor edx, edx
00383C75  49 8B CE                        mov rcx, r14
00383C78  8B E8                           mov ebp, eax
00383C7A  E8 11 39 F0 FF                  call 0x140287590
00383C7F  A8 03                           test al, 3
00383C81  74 50                           je 0x140383cd3
00383C83  33 D2                           xor edx, edx
00383C85  49 8B CE                        mov rcx, r14
00383C88  E8 C7 1C FF FF                  call 0x140375954
00383C8D  E9 26 FC FF FF                  jmp 0x1403838b8
00383C92  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00383C9C  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00383CA1  48 BD FF FF FF FF FF 00 00 00   movabs rbp, 0xffffffffff
00383CAB  E9 60 FC FF FF                  jmp 0x140383910
00383CB0  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00383CB4  41 BA 01 00 00 00               mov r10d, 1
00383CBA  45 8B E2                        mov r12d, r10d
00383CBD  48 85 C0                        test rax, rax
00383CC0  0F 88 F7 FB FF FF               js 0x1403838bd
00383CC6  E9 81 FD FF FF                  jmp 0x140383a4c
00383CCB  49 89 1F                        mov qword ptr [r15], rbx
00383CCE  E9 93 FE FF FF                  jmp 0x140383b66
00383CD3  45 33 C0                        xor r8d, r8d
00383CD6  85 ED                           test ebp, ebp
00383CD8  0F 84 6D 01 00 00               je 0x140383e4b
00383CDE  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
00383CE6  41 BA 01 00 00 00               mov r10d, 1
00383CEC  45 8B EA                        mov r13d, r10d
00383CEF  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00383CF3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00383CF8  C0 E8 02                        shr al, 2
00383CFB  41 84 C2                        test r10b, al
00383CFE  0F 85 1C 01 00 00               jne 0x140383e20
00383D04  49 8B F0                        mov rsi, r8
00383D07  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00383D0C  41 8B D2                        mov edx, r10d
00383D0F  49 8B CE                        mov rcx, r14
00383D12  E8 49 EC FD FF                  call 0x140362960
00383D17  E9 C9 FD FF FF                  jmp 0x140383ae5
00383D1C  33 D2                           xor edx, edx
00383D1E  49 8B CE                        mov rcx, r14
00383D21  E8 CA 0C 08 00                  call 0x1404049f0
00383D26  45 33 C0                        xor r8d, r8d
00383D29  4C 8B F0                        mov r14, rax
00383D2C  48 85 C0                        test rax, rax
00383D2F  0F 84 C2 FC FF FF               je 0x1403839f7
00383D35  E9 9A FC FF FF                  jmp 0x1403839d4
00383D3A  40 F6 C7 02                     test dil, 2
00383D3E  0F 84 74 FB FF FF               je 0x1403838b8
00383D44  8B CF                           mov ecx, edi
00383D46  C1 E9 02                        shr ecx, 2
00383D49  83 E1 1F                        and ecx, 0x1f
00383D4C  E8 AF 3C FB FF                  call 0x140337a00
00383D51  48 8B D8                        mov rbx, rax
00383D54  44 89 94 24 90 00 00 00         mov dword ptr [rsp + 0x90], r10d
00383D5C  E9 5C FE FF FF                  jmp 0x140383bbd
00383D61  45 33 C0                        xor r8d, r8d
00383D64  E9 D9 FA FF FF                  jmp 0x140383842
00383D69  8B 05 49 2D C4 00               mov eax, dword ptr [rip + 0xc42d49]
00383D6F  A8 40                           test al, 0x40
00383D71  0F 84 9D FC FF FF               je 0x140383a14
00383D77  E8 14 B7 F8 FF                  call 0x14030f490
00383D7C  45 33 C0                        xor r8d, r8d
00383D7F  84 C0                           test al, al
00383D81  0F 84 8D FC FF FF               je 0x140383a14
00383D87  8B CD                           mov ecx, ebp
00383D89  E8 D2 B6 F8 FF                  call 0x14030f460
00383D8E  45 33 C0                        xor r8d, r8d
00383D91  E9 80 FC FF FF                  jmp 0x140383a16
00383D96  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00383D9A  48 0F BA E0 28                  bt rax, 0x28
00383D9F  0F 82 49 FC FF FF               jb 0x1403839ee
00383DA5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00383DA9  4C 8B CB                        mov r9, rbx
00383DAC  4D 8B C7                        mov r8, r15
00383DAF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00383DB4  BA 11 04 00 00                  mov edx, 0x411
00383DB9  B9 1A 00 00 00                  mov ecx, 0x1a
00383DBE  E8 9D 98 17 00                  call 0x1404fd660
00383DC3  CC                              int3
00383DC4  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
00383DC9  0F 85 C8 FA FF FF               jne 0x140383897
00383DCF  40 84 FF                        test dil, dil
00383DD2  0F 89 E0 FA FF FF               jns 0x1403838b8
00383DD8  F6 C2 42                        test dl, 0x42
00383DDB  E9 AB FC FF FF                  jmp 0x140383a8b
00383DE0  41 84 FA                        test r10b, dil
00383DE3  0F 84 CF FA FF FF               je 0x1403838b8
00383DE9  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00383DF1  48 89 19                        mov qword ptr [rcx], rbx
00383DF4  E9 BF FA FF FF                  jmp 0x1403838b8
00383DF9  8B 05 B9 2C C4 00               mov eax, dword ptr [rip + 0xc42cb9]
00383DFF  A8 40                           test al, 0x40
00383E01  0F 84 9D FC FF FF               je 0x140383aa4
00383E07  E8 84 B6 F8 FF                  call 0x14030f490
00383E0C  84 C0                           test al, al
00383E0E  0F 84 90 FC FF FF               je 0x140383aa4
00383E14  8B CD                           mov ecx, ebp
00383E16  E8 45 B6 F8 FF                  call 0x14030f460
00383E1B  E9 86 FC FF FF                  jmp 0x140383aa6
00383E20  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00383E24  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00383E29  48 83 E0 FB                     and rax, 0xfffffffffffffffb
00383E2D  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00383E31  E8 56 78 FA FF                  call 0x14032b68c
00383E36  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00383E3B  E9 CC FE FF FF                  jmp 0x140383d0c
00383E40  45 33 C0                        xor r8d, r8d
00383E43  45 8B E0                        mov r12d, r8d
00383E46  E9 85 F9 FF FF                  jmp 0x1403837d0
00383E4B  48 8B CF                        mov rcx, rdi
00383E4E  E8 5D A2 08 00                  call 0x14040e0b0
00383E53  85 C0                           test eax, eax
00383E55  0F 84 83 FE FF FF               je 0x140383cde
00383E5B  48 0F BA E3 0A                  bt rbx, 0xa
00383E60  0F 83 18 0B 36 00               jae 0x1406e497e
00383E66  48 83 E3 F7                     and rbx, 0xfffffffffffffff7
00383E6A  E9 6F FE FF FF                  jmp 0x140383cde
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReservePageFileSpaceForPage(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p90;
    unsigned __int64 v_stack_p98;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    a3 = 0;
    v_stack_m48 = 0;
    v_stack_p18 = 0;
    if (!sign_flag) goto loc_00383AB5;
loc_003837D0:
loc_003837D3:
    result = MI_READ_PTE_LOCK_FREE(a2, a2, a3, a4);
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_003838F2;
    if (!sign_flag) goto loc_00383D61;
    result = (result) >> (12);
    result = (result) & (v_rbp);
    v_r14 = (result + result * 2) << (4);
    v_r14 = (v_r14) + (result);
    a3 = 0;
    if (((1) & ((unsigned __int8)((unsigned int)(a3)))) != 0) goto loc_00383839;
loc_00383826:
    if (condition_is_below) goto loc_00383A06;
loc_00383839:
    if (sign_flag) goto loc_003838B8;
loc_00383842:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) == 0) goto loc_003838B8;
    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11192371) + result * 8)) != v_stack_p8) goto loc_003838B8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_003838B8;
    result = MiInvalidPteConforms(*(unsigned __int64 *)(v_r14 + 16), result, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_003838B8;
    result = MI_IS_RESET_PTE(*(unsigned __int64 *)(v_r14 + 16), result, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00383DC4;
loc_00383897:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_r14 + 16))) >> (1));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_00383DE0;
    if (v_r14 == 0) goto loc_00383ACE;
    if (((*(unsigned __int8 *)(v_r14 + 34)) & (40)) == 0) goto loc_00383ACE;
loc_003838B8:
    if (1 != 0) {
    }
    if (0 != 0) goto loc_00383A2E;
loc_003838D5:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m48);
loc_003838F2:
    if (condition_is_below) goto loc_003838B8;
    if (condition_is_above_or_equal) goto loc_00383B86;
    if (!sign_flag) goto loc_00383A49;
    v_r12 = 0;
loc_00383910:
    result = MI_READ_PTE_LOCK_FREE(a2, result, a3, a4);
    if (condition_is_above_or_equal) goto loc_00383E40;
    result = MiInvalidPteConforms(result, result, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00383910;
    if (*(unsigned __int64 *)(v_rip + 11182919) == 0) goto loc_00383950;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00383A25;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11182919));
    a1 = (a1) & (result);
loc_00383950:
    a1 = (a1) >> (12);
    a1 = (a1) & (v_stack_p8);
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 11182958))) goto loc_00383910;
    if (a1 >= (*(unsigned __int64 *)(v_rip + 11182958))) goto loc_00383910;
loc_00383990:
    if (a1 < (*(unsigned __int64 *)(v_rip + 11182958))) goto loc_00383A96;
    result = MI_READ_PTE_LOCK_FREE(a2, a2, a3, a4);
    if (result != result) goto loc_00383C92;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00383D1C;
    a3 = 0;
loc_003839D4:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 8)) | (*(unsigned __int64 *)(v_rip + 11192015));
    if (result != a2) goto loc_00383D96;
loc_003839EE:
    if (*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 != 0) goto loc_00383CB0;
loc_003839F7:
    goto loc_00383E43;
loc_00383A06:
    v_rbp = (unsigned int)((0) + (0));
    if (((*(unsigned int *)(v_rip + 12851358)) & ((unsigned int)(v_rbp))) == 0) goto loc_00383D69;
loc_00383A14:
loc_00383A16:
    if (!sign_flag) goto loc_00383826;
    goto loc_00383A06;
loc_00383A25:
    a1 = (*(unsigned __int64 *)(v_rip + 11192015)) & (-17);
    goto loc_00383950;
loc_00383A2E:
    result = MiReleasePageFileInfo(v_stack_p80, 0, 1, a4);
    goto loc_003838D5;
loc_00383A49:
    a3 = 0;
loc_00383A4C:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11191857) + result * 8)) != v_stack_p80) goto loc_003838B8;
    result = MI_IS_RESET_PTE(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 16), 0, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00383897;
loc_00383A8B:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 34)) & (16)) != 0) goto loc_00383897;
    goto loc_003838B8;
loc_00383A96:
    v_rbp = (unsigned int)((v_stack_p80) + 1);
    if (((*(unsigned int *)(v_rip + 12851214)) & ((unsigned int)(v_rbp))) == 0) goto loc_00383DF9;
loc_00383AA4:
loc_00383AA6:
    if (!sign_flag) goto loc_00383990;
    goto loc_00383A96;
loc_00383AB5:
    a2 = 0;
    result = MiLockLeafPage(0, a2, a3, a4);
    if (result != 0) { v_r12 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 16)); }
    goto loc_003837D3;
loc_00383ACE:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 16))) >> (2));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_00383C27;
    if (((1) & ((unsigned __int8)((unsigned int)(a3)))) != 0) goto loc_00383B76;
loc_00383AE5:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p98, a2, a3, a4);
    a1 = (result) >> (12);
    a1 = (unsigned int)((a1) & (15));
    if (*(unsigned __int64 *)(v_rip + 11182453) == 0) goto loc_00383B1A;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00383B80;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11182453));
    result = (result) & (a1);
loc_00383B1A:
    result = (result) >> (32);
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11182919) + a2 * 8 + 16), *(unsigned __int64 *)(v_rbp + a1 * 8 + 18528), (unsigned int)((unsigned int)(result)), 2);
    a3 = 0;
    if (result == 0) goto loc_00383CCB;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) == 0) goto loc_00383BFB;
loc_00383B4D:
    *(unsigned __int64 *)(result + 16) = result;
    result = (unsigned int)(*(unsigned int *)(result + 32));
    if (0 != 0) {
        a2 = 8;
        a1 = result;
        result = MiInsertPageInList(a1, a2, a3, 2);
        a3 = 0;
    }
    if (v_stack_p90 != 0) goto loc_00383BCA;
loc_00383B70:
loc_00383B76:
    v_stack_p30 = 1;
    goto loc_003838B8;
loc_00383B80:
    result = (result) & (-17);
    goto loc_00383B1A;
loc_00383B86:
    a3 = 0;
    if (result == 0) goto loc_00383D3A;
    result = MiInvalidPteConforms(result, a2, a3, 2);
    if ((unsigned int)(result) == 0) goto loc_003838B8;
    result = (result) >> (5);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) == 16) goto loc_003838B8;
    if ((unsigned int)(result) == 0) goto loc_003838B8;
loc_00383BBD:
    goto loc_00383897;
loc_00383BCA:
    v_r15 = (a2) >> (9);
    a2 = (a2) & (v_r15);
    a2 = (a2) + (result);
    result = MiIncreaseUsedPtes(result, a2, 1, 2);
    goto loc_00383B70;
loc_00383BFB:
    if (((*(unsigned __int8 *)(result + 34)) & (16)) == 0) goto loc_00383B4D;
    if (0 != 0) goto loc_00383B4D;
    a2 = 0;
    result = MiUnlinkPageFromListEx(result, a2, 1, 2);
    a3 = 0;
    goto loc_00383B4D;
loc_00383C27:
    if (result == 0) goto loc_003838B8;
    if (((1) & (2)) != 0) goto loc_00383B76;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) != 0) goto loc_00383CEF;
    v_rdi = (result) - ((unsigned int)(*(unsigned int *)(result + 32)));
    v_rdi = (v_rdi) >> (4);
    v_rdi = (v_rdi) * ((unsigned int)(*(unsigned int *)(result + 32)));
    result = MiPageStandbyLookasideStatus(v_rdi, a2, a3, 2);
    a2 = 0;
    result = MiUnlinkPageFromListEx(result, a2, a3, 2);
    if ((((unsigned __int8)(result)) & (3)) == 0) goto loc_00383CD3;
    a2 = 0;
    result = MiDiscardTransitionPteEx(result, a2, a3, 2);
    goto loc_003838B8;
loc_00383C92:
    goto loc_00383910;
loc_00383CB0:
    if (sign_flag) goto loc_003838BD;
    goto loc_00383A4C;
loc_00383CCB:
    *(unsigned __int64 *)(v_r15) = result;
    goto loc_00383B66;
loc_00383CD3:
    a3 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00383E4B;
loc_00383CDE:
loc_00383CEF:
    v_stack_p38 = *(unsigned __int64 *)(result + 16);
    result = (unsigned __int8)((*(unsigned __int64 *)(result + 16)) >> (2));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_00383E20;
    v_stack_p38 = 0;
loc_00383D0C:
    result = MiSetPfnModified(result, 1, a3, 2);
    goto loc_00383AE5;
loc_00383D1C:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(result, a2, a3, 2);
    a3 = 0;
    if (result == 0) goto loc_003839F7;
    goto loc_003839D4;
loc_00383D3A:
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_003838B8;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (2));
    a1 = (unsigned int)((a1) & (31));
    result = MiMakeDemandZeroPte(a1, a2, a3, 2);
    v_stack_p90 = 1;
    goto loc_00383BBD;
loc_00383D61:
    a3 = 0;
    goto loc_00383842;
loc_00383D69:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12856649)))) & (64)) == 0) goto loc_00383A14;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, 2);
    a3 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00383A14;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p80)), a2, a3, 2);
    a3 = 0;
    goto loc_00383A16;
loc_00383D96:
    if (condition_is_below) goto loc_003839EE;
    v_stack_p20 = *(unsigned __int64 *)(result + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), v_r15, result);
loc_00383DC4:
    if (((*(unsigned __int8 *)(result + 34)) & (16)) != 0) goto loc_00383897;
    if (!sign_flag) goto loc_003838B8;
    goto loc_00383A8B;
loc_00383DE0:
    if (((1) & ((unsigned __int8)(v_rdi))) == 0) goto loc_003838B8;
    *(unsigned __int64 *)(v_stack_p98) = result;
    goto loc_003838B8;
loc_00383DF9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12856505)))) & (64)) == 0) goto loc_00383AA4;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p98, (unsigned int)(0x411ULL), v_r15, result);
    if ((unsigned __int8)(result) == 0) goto loc_00383AA4;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p80)), (unsigned int)(0x411ULL), v_r15, result);
    goto loc_00383AA6;
loc_00383E20:
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
    result = MiClearPageFileReservation(v_stack_p38, (unsigned int)(0x411ULL), v_r15, result);
    goto loc_00383D0C;
loc_00383E40:
    a3 = 0;
loc_00383E43:
    goto loc_003837D0;
loc_00383E4B:
    result = MiPageStandbyLookasideStatus(v_rdi, (unsigned int)(0x411ULL), a3, result);
    if ((unsigned int)(result) == 0) goto loc_00383CDE;
    v_rbx = (result) & (-9);
    goto loc_00383CDE;
}
```

## 5. (Beta) C Style

```c
int64_t MiReservePageFileSpaceForPage(int64_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_p90;
    uint64_t v_stack_p98;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    Arg3 = 0;
    v_stack_m48 = 0;
    v_stack_p18 = 0;
    if (!sign_flag) goto loc_00383AB5;
loc_003837D0:
loc_003837D3:
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, Arg3, Arg4);
    if (((1) & ((uint8_t)(result))) == 0) goto loc_003838F2;
    if (!sign_flag) goto loc_00383D61;
    result = (result) >> (12);
    result = (result) & (local_rbp);
    local_r14 = (result + result * 2) << (4);
    local_r14 = (local_r14) + (result);
    Arg3 = 0;
    if (((1) & ((uint8_t)((uint32_t)(Arg3)))) != 0) goto loc_00383839;
loc_00383826:
    if (condition_is_below) goto loc_00383A06;
loc_00383839:
    if (sign_flag) goto loc_003838B8;
loc_00383842:
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r14)))) == 0) goto loc_003838B8;
    result = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAC833) + result * 8)) != v_stack_p8) goto loc_003838B8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_003838B8;
    result = MiInvalidPteConforms(*(uint64_t *)(local_r14 + 0x10), result, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003838B8;
    result = MI_IS_RESET_PTE(*(uint64_t *)(local_r14 + 0x10), result, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00383DC4;
loc_00383897:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(local_r14 + 0x10))) >> (1));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_00383DE0;
    if (local_r14 == 0) goto loc_00383ACE;
    if (((*(uint8_t *)(local_r14 + 0x22)) & (40)) == 0) goto loc_00383ACE;
loc_003838B8:
    if (1 != 0) {
    }
    if (0 != 0) goto loc_00383A2E;
loc_003838D5:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m48);
loc_003838F2:
    if (condition_is_below) goto loc_003838B8;
    if (condition_is_above_or_equal) goto loc_00383B86;
    if (!sign_flag) goto loc_00383A49;
    local_r12 = 0;
loc_00383910:
    result = MI_READ_PTE_LOCK_FREE(Arg2, result, Arg3, Arg4);
    if (condition_is_above_or_equal) goto loc_00383E40;
    result = MiInvalidPteConforms(result, result, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00383910;
    if (*(uint64_t *)(v_rip + 0xAAA347) == 0) goto loc_00383950;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00383A25;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xAAA347));
    Arg1 = (Arg1) & (result);
loc_00383950:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (v_stack_p8);
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xAAA36E))) goto loc_00383910;
    if (Arg1 >= (*(uint64_t *)(v_rip + 0xAAA36E))) goto loc_00383910;
loc_00383990:
    if (Arg1 < (*(uint64_t *)(v_rip + 0xAAA36E))) goto loc_00383A96;
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, Arg3, Arg4);
    if (result != result) goto loc_00383C92;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00383D1C;
    Arg3 = 0;
loc_003839D4:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x8)) | (*(uint64_t *)(v_rip + 0xAAC6CF));
    if (result != Arg2) goto loc_00383D96;
loc_003839EE:
    if (*(uint64_t *)(v_rip + 0xAAA347) + Arg2 * 8 != 0) goto loc_00383CB0;
loc_003839F7:
    goto loc_00383E43;
loc_00383A06:
    local_rbp = (uint32_t)((0) + (0));
    if (((*(uint32_t *)(v_rip + 0xC4189E)) & ((uint32_t)(local_rbp))) == 0) goto loc_00383D69;
loc_00383A14:
loc_00383A16:
    if (!sign_flag) goto loc_00383826;
    goto loc_00383A06;
loc_00383A25:
    Arg1 = (*(uint64_t *)(v_rip + 0xAAC6CF)) & (-17);
    goto loc_00383950;
loc_00383A2E:
    result = MiReleasePageFileInfo(v_stack_p80, 0, 1, Arg4);
    goto loc_003838D5;
loc_00383A49:
    Arg3 = 0;
loc_00383A4C:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAC631) + result * 8)) != v_stack_p80) goto loc_003838B8;
    result = MI_IS_RESET_PTE(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x10), 0, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00383897;
loc_00383A8B:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x22)) & (16)) != 0) goto loc_00383897;
    goto loc_003838B8;
loc_00383A96:
    local_rbp = (uint32_t)((v_stack_p80) + 1);
    if (((*(uint32_t *)(v_rip + 0xC4180E)) & ((uint32_t)(local_rbp))) == 0) goto loc_00383DF9;
loc_00383AA4:
loc_00383AA6:
    if (!sign_flag) goto loc_00383990;
    goto loc_00383A96;
loc_00383AB5:
    Arg2 = 0;
    result = MiLockLeafPage(0, Arg2, Arg3, Arg4);
    if (result != 0) { local_r12 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x10)); }
    goto loc_003837D3;
loc_00383ACE:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x10))) >> (2));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_00383C27;
    if (((1) & ((uint8_t)((uint32_t)(Arg3)))) != 0) goto loc_00383B76;
loc_00383AE5:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p98, Arg2, Arg3, Arg4);
    Arg1 = (result) >> (12);
    Arg1 = (uint32_t)((Arg1) & (15));
    if (*(uint64_t *)(v_rip + 0xAAA175) == 0) goto loc_00383B1A;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00383B80;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xAAA175));
    result = (result) & (Arg1);
loc_00383B1A:
    result = (result) >> (32);
    result = MiTransferSoftwarePte(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAA347) + arg2 * 8 + 0x10), *(uint64_t *)(local_rbp + Arg1 * 8 + 0x4860), (uint32_t)((uint32_t)(result)), 2);
    Arg3 = 0;
    if (result == 0) goto loc_00383CCB;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) == 0) goto loc_00383BFB;
loc_00383B4D:
    *(uint64_t *)(result + 0x10) = result;
    result = (uint32_t)(*(uint32_t *)(result + 0x20));
    if (0 != 0) {
        Arg2 = 8;
        Arg1 = result;
        result = MiInsertPageInList(Arg1, Arg2, Arg3, 2);
        Arg3 = 0;
    }
    if (v_stack_p90 != 0) goto loc_00383BCA;
loc_00383B70:
loc_00383B76:
    v_stack_p30 = 1;
    goto loc_003838B8;
loc_00383B80:
    result = (result) & (-17);
    goto loc_00383B1A;
loc_00383B86:
    Arg3 = 0;
    if (result == 0) goto loc_00383D3A;
    result = MiInvalidPteConforms(result, Arg2, Arg3, 2);
    if ((uint32_t)(result) == 0) goto loc_003838B8;
    result = (result) >> (5);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) == 16) goto loc_003838B8;
    if ((uint32_t)(result) == 0) goto loc_003838B8;
loc_00383BBD:
    goto loc_00383897;
loc_00383BCA:
    local_r15 = (Arg2) >> (9);
    Arg2 = (Arg2) & (local_r15);
    Arg2 = (Arg2) + (result);
    result = MiIncreaseUsedPtes(result, Arg2, 1, 2);
    goto loc_00383B70;
loc_00383BFB:
    if (((*(uint8_t *)(result + 0x22)) & (16)) == 0) goto loc_00383B4D;
    if (0 != 0) goto loc_00383B4D;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(result, Arg2, 1, 2);
    Arg3 = 0;
    goto loc_00383B4D;
loc_00383C27:
    if (result == 0) goto loc_003838B8;
    if (((1) & (2)) != 0) goto loc_00383B76;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) != 0) goto loc_00383CEF;
    local_rdi = (result) - ((uint32_t)(*(uint32_t *)(result + 0x20)));
    local_rdi = (local_rdi) >> (4);
    local_rdi = (local_rdi) * ((uint32_t)(*(uint32_t *)(result + 0x20)));
    result = MiPageStandbyLookasideStatus(local_rdi, Arg2, Arg3, 2);
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(result, Arg2, Arg3, 2);
    if ((((uint8_t)(result)) & (3)) == 0) goto loc_00383CD3;
    Arg2 = 0;
    result = MiDiscardTransitionPteEx(result, Arg2, Arg3, 2);
    goto loc_003838B8;
loc_00383C92:
    goto loc_00383910;
loc_00383CB0:
    if (sign_flag) goto loc_003838BD;
    goto loc_00383A4C;
loc_00383CCB:
    *(uint64_t *)(local_r15) = result;
    goto loc_00383B66;
loc_00383CD3:
    Arg3 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00383E4B;
loc_00383CDE:
loc_00383CEF:
    v_stack_p38 = *(uint64_t *)(result + 0x10);
    result = (uint8_t)((*(uint64_t *)(result + 0x10)) >> (2));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_00383E20;
    v_stack_p38 = 0;
loc_00383D0C:
    result = MiSetPfnModified(result, 1, Arg3, 2);
    goto loc_00383AE5;
loc_00383D1C:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(result, Arg2, Arg3, 2);
    Arg3 = 0;
    if (result == 0) goto loc_003839F7;
    goto loc_003839D4;
loc_00383D3A:
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_003838B8;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (2));
    Arg1 = (uint32_t)((Arg1) & (31));
    result = MiMakeDemandZeroPte(Arg1, Arg2, Arg3, 2);
    v_stack_p90 = 1;
    goto loc_00383BBD;
loc_00383D61:
    Arg3 = 0;
    goto loc_00383842;
loc_00383D69:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC42D49)))) & (64)) == 0) goto loc_00383A14;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, Arg3, 2);
    Arg3 = 0;
    if ((uint8_t)(result) == 0) goto loc_00383A14;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p80)), Arg2, Arg3, 2);
    Arg3 = 0;
    goto loc_00383A16;
loc_00383D96:
    if (condition_is_below) goto loc_003839EE;
    v_stack_p20 = *(uint64_t *)(result + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), local_r15, result);
loc_00383DC4:
    if (((*(uint8_t *)(result + 0x22)) & (16)) != 0) goto loc_00383897;
    if (!sign_flag) goto loc_003838B8;
    goto loc_00383A8B;
loc_00383DE0:
    if (((1) & ((uint8_t)(local_rdi))) == 0) goto loc_003838B8;
    *(uint64_t *)(v_stack_p98) = result;
    goto loc_003838B8;
loc_00383DF9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC42CB9)))) & (64)) == 0) goto loc_00383AA4;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p98, (uint32_t)(0x411ULL), local_r15, result);
    if ((uint8_t)(result) == 0) goto loc_00383AA4;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p80)), (uint32_t)(0x411ULL), local_r15, result);
    goto loc_00383AA6;
loc_00383E20:
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
    result = MiClearPageFileReservation(v_stack_p38, (uint32_t)(0x411ULL), local_r15, result);
    goto loc_00383D0C;
loc_00383E40:
    Arg3 = 0;
loc_00383E43:
    goto loc_003837D0;
loc_00383E4B:
    result = MiPageStandbyLookasideStatus(local_rdi, (uint32_t)(0x411ULL), Arg3, result);
    if ((uint32_t)(result) == 0) goto loc_00383CDE;
    local_rbx = (result) & (-9);
    goto loc_00383CDE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038377C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
