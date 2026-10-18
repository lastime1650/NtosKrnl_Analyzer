# MiOutSwapWorkingSetPte

- RVA: `0x00372190`–`0x003728D6` (길이 `1,862` bytes)
- VA: `0x0000000140372190`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A9E0`
- 디코드: `428`개 명령, `1,862/1,862` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003721E8` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0037229F` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x003722B1` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x003722D1` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x003722DE` → [MiCaptureDirtyBitToPfn](MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x00372311` → [MiSetStoreVirtualPagefileValue](MiSetStoreVirtualPagefileValue_function_00373B80.md) (function, `0x00373B80`)
- `0x00372407` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00372422` → [MiInvalidPteConforms](MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x003724AD` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0037254E` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00372567` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x003725FF` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x003726DF` → [MiReservePageFileSpaceForPage](../38/MiReservePageFileSpaceForPage_function_0038377C.md) (function, `0x0038377C`)
- `0x0037270D` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x0037274E` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x003727B6` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003727D4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003727E3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003727FB` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0037280B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00372849` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0037286F` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x003728CC` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B108`

### Static image references
- `0x0037220A` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0037242B` → RVA `0x00E2DC80` (`.data`; read)
- `0x003724C4` → RVA `0x00E30088` (`.data`; read)
- `0x00372652` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003727C6` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00372190  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00372195  55                              push rbp
00372196  56                              push rsi
00372197  57                              push rdi
00372198  41 54                           push r12
0037219A  41 55                           push r13
0037219C  41 56                           push r14
0037219E  41 57                           push r15
003721A0  48 83 EC 50                     sub rsp, 0x50
003721A4  4C 8B A1 B8 00 00 00            mov r12, qword ptr [rcx + 0xb8]
003721AB  4C 8B EA                        mov r13, rdx
003721AE  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
003721B3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003721B8  45 85 C0                        test r8d, r8d
003721BB  0F 85 28 02 00 00               jne 0x1403723e9
003721C1  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
003721C6  45 33 FF                        xor r15d, r15d
003721C9  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
003721D1  41 8B FF                        mov edi, r15d
003721D4  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
003721DC  41 8B EF                        mov ebp, r15d
003721DF  41 8B F7                        mov esi, r15d
003721E2  4D 8B F7                        mov r14, r15
003721E5  49 8B CD                        mov rcx, r13
003721E8  E8 B3 06 F1 FF                  call 0x1402828a0
003721ED  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003721F2  48 8B D8                        mov rbx, rax
003721F5  A8 01                           test al, 1
003721F7  74 76                           je 0x14037226f
003721F9  48 C1 E8 0C                     shr rax, 0xc
003721FD  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00372207  48 23 C1                        and rax, rcx
0037220A  48 3B 05 CF BA AB 00            cmp rax, qword ptr [rip + 0xabbacf]
00372211  0F 87 D2 01 00 00               ja 0x1403723e9
00372217  48 8D 0C 40                     lea rcx, [rax + rax*2]
0037221B  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00372225  48 03 C9                        add rcx, rcx
00372228  48 8B C0                        mov rax, rax
0037222B  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0037222F  48 C1 E8 36                     shr rax, 0x36
00372233  0F BA E0 00                     bt eax, 0
00372237  0F 83 AC 01 00 00               jae 0x1403723e9
0037223D  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00372247  48 8B C0                        mov rax, rax
0037224A  4C 8D 34 C8                     lea r14, [rax + rcx*8]
0037224E  48 8B 44 C8 28                  mov rax, qword ptr [rax + rcx*8 + 0x28]
00372253  48 85 C0                        test rax, rax
00372256  0F 89 15 03 00 00               jns 0x140372571
0037225C  49 8B 5C 24 08                  mov rbx, qword ptr [r12 + 8]
00372261  48 85 DB                        test rbx, rbx
00372264  0F 85 D9 00 00 00               jne 0x140372343
0037226A  E9 7A 01 00 00                  jmp 0x1403723e9
0037226F  48 0F BA E3 0A                  bt rbx, 0xa
00372274  0F 82 6F 01 00 00               jb 0x1403723e9
0037227A  48 0F BA E3 0B                  bt rbx, 0xb
0037227F  0F 82 7F 01 00 00               jb 0x140372404
00372285  D0 E8                           shr al, 1
00372287  A8 01                           test al, 1
00372289  0F 84 5A 01 00 00               je 0x1403723e9
0037228F  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00372294  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
0037229C  48 8B FB                        mov rdi, rbx
0037229F  E8 E8 93 FB FF                  call 0x14032b68c
003722A4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003722A9  49 8B CD                        mov rcx, r13
003722AC  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
003722B1  E8 4A D8 EC FF                  call 0x14023fb00
003722B6  85 C0                           test eax, eax
003722B8  0F 85 AC 05 00 00               jne 0x14037286a
003722BE  49 89 5D 00                     mov qword ptr [r13], rbx
003722C2  45 85 FF                        test r15d, r15d
003722C5  0F 84 04 01 00 00               je 0x1403723cf
003722CB  48 8B D3                        mov rdx, rbx
003722CE  49 8B CD                        mov rcx, r13
003722D1  E8 D6 2B F2 FF                  call 0x140294eac
003722D6  E9 DF 00 00 00                  jmp 0x1403723ba
003722DB  49 8B CE                        mov rcx, r14
003722DE  E8 ED EA FF FF                  call 0x140370dd0
003722E3  48 8B E8                        mov rbp, rax
003722E6  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
003722EA  C1 E8 10                        shr eax, 0x10
003722ED  24 C0                           and al, 0xc0
003722EF  3C 40                           cmp al, 0x40
003722F1  0F 85 1E 05 00 00               jne 0x140372815
003722F7  41 83 7C 24 20 FF               cmp dword ptr [r12 + 0x20], -1
003722FD  75 20                           jne 0x14037231f
003722FF  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
00372303  41 B8 02 00 00 00               mov r8d, 2
00372309  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00372311  E8 6A 18 00 00                  call 0x140373b80
00372316  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0037231B  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0037231F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00372329  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0037232E  41 8B 4C 24 20                  mov ecx, dword ptr [r12 + 0x20]
00372333  83 E6 FE                        and esi, 0xfffffffe
00372336  49 8B 1C 24                     mov rbx, qword ptr [r12]
0037233A  83 F9 FF                        cmp ecx, -1
0037233D  0F 85 62 03 00 00               jne 0x1403726a5
00372343  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0037234D  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00372351  48 3B 53 08                     cmp rdx, qword ptr [rbx + 8]
00372355  73 63                           jae 0x1403723ba
00372357  49 C1 E5 19                     shl r13, 0x19
0037235B  48 8B C0                        mov rax, rax
0037235E  48 C1 E0 19                     shl rax, 0x19
00372362  4C 8B C2                        mov r8, rdx
00372365  49 C1 E0 04                     shl r8, 4
00372369  4C 2B E8                        sub r13, rax
0037236C  4C 03 03                        add r8, qword ptr [rbx]
0037236F  49 C1 FD 10                     sar r13, 0x10
00372373  49 8D 48 F0                     lea rcx, [r8 - 0x10]
00372377  48 85 D2                        test rdx, rdx
0037237A  0F 84 A8 03 00 00               je 0x140372728
00372380  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00372384  48 03 01                        add rax, qword ptr [rcx]
00372387  49 3B C5                        cmp rax, r13
0037238A  0F 85 98 03 00 00               jne 0x140372728
00372390  48 81 41 08 00 10 00 00         add qword ptr [rcx + 8], 0x1000
00372398  48 FF 43 18                     inc qword ptr [rbx + 0x18]
0037239C  40 F6 C6 02                     test sil, 2
003723A0  0F 85 DB 03 00 00               jne 0x140372781
003723A6  40 F6 C6 04                     test sil, 4
003723AA  0F 85 8F 03 00 00               jne 0x14037273f
003723B0  40 F6 C6 08                     test sil, 8
003723B4  0F 85 D8 04 00 00               jne 0x140372892
003723BA  40 F6 C6 01                     test sil, 1
003723BE  74 0F                           je 0x1403723cf
003723C0  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003723CA  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003723CF  48 85 FF                        test rdi, rdi
003723D2  0F 85 52 04 00 00               jne 0x14037282a
003723D8  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
003723E0  48 85 ED                        test rbp, rbp
003723E3  0F 85 D7 04 00 00               jne 0x1403728c0
003723E9  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
003723F1  33 C0                           xor eax, eax
003723F3  48 83 C4 50                     add rsp, 0x50
003723F7  41 5F                           pop r15
003723F9  41 5E                           pop r14
003723FB  41 5D                           pop r13
003723FD  41 5C                           pop r12
003723FF  5F                              pop rdi
00372400  5E                              pop rsi
00372401  5D                              pop rbp
00372402  C3                              ret
00372403  CC                              int3
00372404  49 8B CD                        mov rcx, r13
00372407  E8 94 04 F1 FF                  call 0x1402828a0
0037240C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00372411  48 8B D8                        mov rbx, rax
00372414  48 0F BA E0 0B                  bt rax, 0xb
00372419  0F 83 C3 FD FF FF               jae 0x1403721e2
0037241F  48 8B C8                        mov rcx, rax
00372422  E8 E9 05 00 00                  call 0x140372a10
00372427  85 C0                           test eax, eax
00372429  74 D9                           je 0x140372404
0037242B  48 8B 05 4E B8 AB 00            mov rax, qword ptr [rip + 0xabb84e]
00372432  48 85 C0                        test rax, rax
00372435  74 12                           je 0x140372449
00372437  F6 C3 10                        test bl, 0x10
0037243A  0F 85 FC 01 00 00               jne 0x14037263c
00372440  48 8B C8                        mov rcx, rax
00372443  48 F7 D1                        not rcx
00372446  48 23 CB                        and rcx, rbx
00372449  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00372453  48 C1 E9 0C                     shr rcx, 0xc
00372457  48 23 C8                        and rcx, rax
0037245A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00372464  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00372468  48 03 D2                        add rdx, rdx
0037246B  48 8B C0                        mov rax, rax
0037246E  48 3B 0D 6B B8 AB 00            cmp rcx, qword ptr [rip + 0xabb86b]
00372475  4C 8D 34 D0                     lea r14, [rax + rdx*8]
00372479  77 89                           ja 0x140372404
0037247B  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00372485  48 8B C0                        mov rax, rax
00372488  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0037248C  48 C1 E8 36                     shr rax, 0x36
00372490  0F BA E0 00                     bt eax, 0
00372494  0F 83 6A FF FF FF               jae 0x140372404
0037249A  41 8B DF                        mov ebx, r15d
0037249D  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
003724A4  0F 82 A6 01 00 00               jb 0x140372650
003724AA  49 8B CD                        mov rcx, r13
003724AD  E8 EE 03 F1 FF                  call 0x1402828a0
003724B2  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003724B7  48 3B C3                        cmp rax, rbx
003724BA  0F 85 D1 01 00 00               jne 0x140372691
003724C0  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003724C4  48 8B 0D BD DB AB 00            mov rcx, qword ptr [rip + 0xabdbbd]
003724CB  48 C1 E8 2B                     shr rax, 0x2b
003724CF  25 FF 03 00 00                  and eax, 0x3ff
003724D4  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003724D8  8B 40 04                        mov eax, dword ptr [rax + 4]
003724DB  84 C0                           test al, al
003724DD  0F 88 66 02 00 00               js 0x140372749
003724E3  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003724E7  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
003724F1  48 0B C1                        or rax, rcx
003724F4  49 3B C5                        cmp rax, r13
003724F7  0F 85 91 02 00 00               jne 0x14037278e
003724FD  4D 85 F6                        test r14, r14
00372500  0F 84 DF FC FF FF               je 0x1403721e5
00372506  41 F6 46 22 28                  test byte ptr [r14 + 0x22], 0x28
0037250B  0F 85 AF FE FF FF               jne 0x1403723c0
00372511  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00372515  0F B6 C1                        movzx eax, cl
00372518  D0 E8                           shr al, 1
0037251A  A8 01                           test al, 1
0037251C  0F 84 9E FE FF FF               je 0x1403723c0
00372522  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00372526  48 8B F9                        mov rdi, rcx
00372529  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00372531  66 85 C0                        test ax, ax
00372534  0F 85 47 03 00 00               jne 0x140372881
0037253A  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
0037253F  24 07                           and al, 7
00372541  3C 03                           cmp al, 3
00372543  0F 85 38 03 00 00               jne 0x140372881
00372549  33 D2                           xor edx, edx
0037254B  49 8B CE                        mov rcx, r14
0037254E  E8 3D 50 F1 FF                  call 0x140287590
00372553  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00372557  BA 08 00 00 00                  mov edx, 8
0037255C  48 83 E0 FD                     and rax, 0xfffffffffffffffd
00372560  49 8B CE                        mov rcx, r14
00372563  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00372567  E8 94 7A F4 FF                  call 0x1402ba000
0037256C  E9 4F FE FF FF                  jmp 0x1403723c0
00372571  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00372575  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0037257F  48 0B C1                        or rax, rcx
00372582  49 3B C5                        cmp rax, r13
00372585  0F 85 5E FE FF FF               jne 0x1403723e9
0037258B  BE 01 00 00 00                  mov esi, 1
00372590  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00372597  0F 82 D3 00 00 00               jb 0x140372670
0037259D  41 F6 46 22 08                  test byte ptr [r14 + 0x22], 8
003725A2  4C 8B FF                        mov r15, rdi
003725A5  0F 85 15 FE FF FF               jne 0x1403723c0
003725AB  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
003725AF  D0 E8                           shr al, 1
003725B1  40 84 C6                        test sil, al
003725B4  0F 85 AA 01 00 00               jne 0x140372764
003725BA  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
003725C4  41 39 AC 24 90 00 00 00         cmp dword ptr [r12 + 0x90], ebp
003725CC  75 40                           jne 0x14037260e
003725CE  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
003725D2  66 3B C6                        cmp ax, si
003725D5  0F 85 E5 FD FF FF               jne 0x1403723c0
003725DB  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
003725E0  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
003725E6  A8 0F                           test al, 0xf
003725E8  75 24                           jne 0x14037260e
003725EA  49 8B D5                        mov rdx, r13
003725ED  48 C1 E2 19                     shl rdx, 0x19
003725F1  48 8B C1                        mov rax, rcx
003725F4  48 C1 E0 19                     shl rax, 0x19
003725F8  48 2B D0                        sub rdx, rax
003725FB  48 C1 FA 10                     sar rdx, 0x10
003725FF  E8 3C 3F FA FF                  call 0x140316540
00372604  24 0F                           and al, 0xf
00372606  3C 08                           cmp al, 8
00372608  0F 84 B2 FD FF FF               je 0x1403723c0
0037260E  F6 C3 42                        test bl, 0x42
00372611  0F 85 C4 FC FF FF               jne 0x1403722db
00372617  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
0037261C  0F 85 B9 FC FF FF               jne 0x1403722db
00372622  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00372626  C0 E8 02                        shr al, 2
00372629  40 84 C6                        test sil, al
0037262C  0F 84 8E FD FF FF               je 0x1403723c0
00372632  BE 03 00 00 00                  mov esi, 3
00372637  E9 9F FC FF FF                  jmp 0x1403722db
0037263C  48 83 E1 EF                     and rcx, 0xffffffffffffffef
00372640  E9 04 FE FF FF                  jmp 0x140372449
00372645  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00372650  FF C3                           inc ebx
00372652  85 1D 54 2C C5 00               test dword ptr [rip + 0xc52c54], ebx
00372658  0F 84 68 01 00 00               je 0x1403727c6
0037265E  F3 90                           pause
00372660  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00372664  48 85 C0                        test rax, rax
00372667  0F 89 30 FE FF FF               jns 0x14037249d
0037266D  EB E1                           jmp 0x140372650
0037266F  90                              nop
00372670  41 FF C7                        inc r15d
00372673  44 85 3D 32 2C C5 00            test dword ptr [rip + 0xc52c32], r15d
0037267A  0F 84 6D 01 00 00               je 0x1403727ed
00372680  F3 90                           pause
00372682  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00372686  48 85 C0                        test rax, rax
00372689  0F 89 01 FF FF FF               jns 0x140372590
0037268F  EB DF                           jmp 0x140372670
00372691  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0037269B  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003726A0  E9 5F FD FF FF                  jmp 0x140372404
003726A5  48 8B C1                        mov rax, rcx
003726A8  48 C1 E0 04                     shl rax, 4
003726AC  48 83 C0 28                     add rax, 0x28
003726B0  49 03 C4                        add rax, r12
003726B3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003726B8  83 F9 05                        cmp ecx, 5
003726BB  0F 83 F9 FC FF FF               jae 0x1403723ba
003726C1  44 39 78 08                     cmp dword ptr [rax + 8], r15d
003726C5  0F 84 EF FC FF FF               je 0x1403723ba
003726CB  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
003726D3  4C 8B C8                        mov r9, rax
003726D6  41 B8 80 00 00 00               mov r8d, 0x80
003726DC  49 8B D5                        mov rdx, r13
003726DF  E8 98 10 01 00                  call 0x14038377c
003726E4  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
003726E9  48 8B 05 90 B5 AB 00            mov rax, qword ptr [rip + 0xabb590]
003726F0  49 8B 10                        mov rdx, qword ptr [r8]
003726F3  48 85 C0                        test rax, rax
003726F6  74 0B                           je 0x140372703
003726F8  F6 C2 10                        test dl, 0x10
003726FB  75 06                           jne 0x140372703
003726FD  48 F7 D0                        not rax
00372700  48 23 D0                        and rdx, rax
00372703  49 8B 08                        mov rcx, qword ptr [r8]
00372706  48 C1 EA 20                     shr rdx, 0x20
0037270A  48 FF C2                        inc rdx
0037270D  E8 2E B1 FF FF                  call 0x14036d840
00372712  41 83 40 08 FF                  add dword ptr [r8 + 8], -1
00372717  49 89 00                        mov qword ptr [r8], rax
0037271A  0F 84 9C 00 00 00               je 0x1403727bc
00372720  83 CE 10                        or esi, 0x10
00372723  E9 1B FC FF FF                  jmp 0x140372343
00372728  48 8D 42 01                     lea rax, [rdx + 1]
0037272C  49 8B C8                        mov rcx, r8
0037272F  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00372733  4D 89 28                        mov qword ptr [r8], r13
00372736  4D 89 78 08                     mov qword ptr [r8 + 8], r15
0037273A  E9 51 FC FF FF                  jmp 0x140372390
0037273F  49 FF 44 24 78                  inc qword ptr [r12 + 0x78]
00372744  E9 71 FC FF FF                  jmp 0x1403723ba
00372749  33 D2                           xor edx, edx
0037274B  49 8B CE                        mov rcx, r14
0037274E  E8 9D 22 09 00                  call 0x1404049f0
00372753  4C 8B F0                        mov r14, rax
00372756  48 85 C0                        test rax, rax
00372759  0F 84 83 FA FF FF               je 0x1403721e2
0037275F  E9 7F FD FF FF                  jmp 0x1403724e3
00372764  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
00372768  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0037276C  48 83 E0 FD                     and rax, 0xfffffffffffffffd
00372770  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00372778  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0037277C  E9 39 FE FF FF                  jmp 0x1403725ba
00372781  49 FF 84 24 88 00 00 00         inc qword ptr [r12 + 0x88]
00372789  E9 18 FC FF FF                  jmp 0x1403723a6
0037278E  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00372792  48 0F BA E0 28                  bt rax, 0x28
00372797  0F 82 60 FD FF FF               jb 0x1403724fd
0037279D  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003727A1  4C 8B CB                        mov r9, rbx
003727A4  4D 8B C5                        mov r8, r13
003727A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003727AC  BA 11 04 00 00                  mov edx, 0x411
003727B1  B9 1A 00 00 00                  mov ecx, 0x1a
003727B6  E8 A5 AE 18 00                  call 0x1404fd660
003727BB  CC                              int3
003727BC  41 FF 44 24 20                  inc dword ptr [r12 + 0x20]
003727C1  E9 5A FF FF FF                  jmp 0x140372720
003727C6  8B 05 EC 42 C5 00               mov eax, dword ptr [rip + 0xc542ec]
003727CC  A8 40                           test al, 0x40
003727CE  0F 84 8A FE FF FF               je 0x14037265e
003727D4  E8 B7 CC F9 FF                  call 0x14030f490
003727D9  84 C0                           test al, al
003727DB  0F 84 7D FE FF FF               je 0x14037265e
003727E1  8B CB                           mov ecx, ebx
003727E3  E8 78 CC F9 FF                  call 0x14030f460
003727E8  E9 73 FE FF FF                  jmp 0x140372660
003727ED  8B 05 C5 42 C5 00               mov eax, dword ptr [rip + 0xc542c5]
003727F3  A8 40                           test al, 0x40
003727F5  0F 84 85 FE FF FF               je 0x140372680
003727FB  E8 90 CC F9 FF                  call 0x14030f490
00372800  84 C0                           test al, al
00372802  0F 84 78 FE FF FF               je 0x140372680
00372808  41 8B CF                        mov ecx, r15d
0037280B  E8 50 CC F9 FF                  call 0x14030f460
00372810  E9 6D FE FF FF                  jmp 0x140372682
00372815  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00372819  C1 E8 10                        shr eax, 0x10
0037281C  24 C0                           and al, 0xc0
0037281E  3C 80                           cmp al, 0x80
00372820  75 31                           jne 0x140372853
00372822  83 CE 04                        or esi, 4
00372825  E9 CD FA FF FF                  jmp 0x1403722f7
0037282A  40 0F B6 C7                     movzx eax, dil
0037282E  C0 E8 02                        shr al, 2
00372831  A8 01                           test al, 1
00372833  75 6A                           jne 0x14037289f
00372835  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0037283D  41 B8 01 00 00 00               mov r8d, 1
00372843  48 8B CB                        mov rcx, rbx
00372846  48 8B D7                        mov rdx, rdi
00372849  E8 82 17 F1 FF                  call 0x140283fd0
0037284E  E9 8D FB FF FF                  jmp 0x1403723e0
00372853  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00372857  C1 E8 10                        shr eax, 0x10
0037285A  3C 40                           cmp al, 0x40
0037285C  0F 83 95 FA FF FF               jae 0x1403722f7
00372862  83 CE 08                        or esi, 8
00372865  E9 8D FA FF FF                  jmp 0x1403722f7
0037286A  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0037286F  E8 F4 22 F2 FF                  call 0x140294b68
00372874  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00372879  44 8B F8                        mov r15d, eax
0037287C  E9 3D FA FF FF                  jmp 0x1403722be
00372881  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00372885  48 83 E0 FD                     and rax, 0xfffffffffffffffd
00372889  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0037288D  E9 2E FB FF FF                  jmp 0x1403723c0
00372892  49 FF 84 24 80 00 00 00         inc qword ptr [r12 + 0x80]
0037289A  E9 1B FB FF FF                  jmp 0x1403723ba
0037289F  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
003728A7  48 83 E0 FB                     and rax, 0xfffffffffffffffb
003728AB  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
003728B3  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
003728BB  E9 75 FF FF FF                  jmp 0x140372835
003728C0  41 B8 01 00 00 00               mov r8d, 1
003728C6  48 8B D5                        mov rdx, rbp
003728C9  48 8B CB                        mov rcx, rbx
003728CC  E8 FF 16 F1 FF                  call 0x140283fd0
003728D1  E9 13 FB FF FF                  jmp 0x1403723e9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiOutSwapWorkingSetPte(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 16);
    if (a3 != 0) goto loc_003723E9;
    v_r15 = 0;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 24);
    v_stack_p8 = 0;
loc_003721E2:
loc_003721E5:
    result = MI_READ_PTE_LOCK_FREE(a2, a2, a3, a4);
    v_stack_m58 = result;
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0037226F;
    result = (result) >> (12);
    result = (result) & (a2);
    if (result > (*(unsigned __int64 *)(v_rip + 11254479))) goto loc_003723E9;
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_003723E9;
    if (!sign_flag) goto loc_00372571;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) != 0) goto loc_00372343;
    goto loc_003723E9;
loc_0037226F:
    if (condition_is_below) goto loc_003723E9;
    if (condition_is_below) goto loc_00372404;
    result = (unsigned __int8)((*(unsigned __int64 *)(result + a1 * 8 + 40)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_003723E9;
    v_stack_p8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8);
    result = MiClearPageFileReservation(v_stack_m58, a2, a3, a4);
    v_stack_m50 = v_stack_m58;
    result = MiPteInShadowRange(a2, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0037286A;
loc_003722BE:
    *(unsigned __int64 *)(a2) = v_stack_m58;
    if (0 == 0) goto loc_003723CF;
    result = MiWritePteShadow(a2, v_stack_m58, a3, a4);
    goto loc_003723BA;
loc_003722DB:
    result = MiCaptureDirtyBitToPfn(result + a1 * 8, v_stack_m58, a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) != 64) goto loc_00372815;
loc_003722F7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 32)) == -1) {
        a2 = *(unsigned __int64 *)(result + a1 * 8 + 16);
        a3 = 2;
        a1 = v_stack_p20;
        result = MiSetStoreVirtualPagefileValue(a1, a2, a3, a4);
        v_stack_m58 = result;
        *(unsigned __int64 *)(result + a1 * 8 + 16) = result;
    }
    v_rsi = (unsigned int)((0) & (0xFFFFFFFEULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 32)))) != -1) goto loc_003726A5;
loc_00372343:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 8))) goto loc_003723BA;
    v_r13 = (a2) << (25);
    result = (result) << (25);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16)) << (4);
    v_r13 = (v_r13) - (result);
    a3 = (a3) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184))));
    v_r13 = (v_r13) >> (16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16) == 0) goto loc_00372728;
    result = (*(unsigned __int64 *)(a3 - 16 + 8)) + (*(unsigned __int64 *)(a3 - 16));
    if (result != v_r13) goto loc_00372728;
loc_00372390:
    if ((((unsigned __int8)(v_rsi)) & (2)) != 0) goto loc_00372781;
loc_003723A6:
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_0037273F;
    if ((((unsigned __int8)(v_rsi)) & (8)) != 0) goto loc_00372892;
loc_003723BA:
    if ((((unsigned __int8)(v_rsi)) & (1)) != 0) {
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) != 0) goto loc_0037282A;
loc_003723E0:
    if (result != 0) goto loc_003728C0;
loc_003723E9:
    result = 0;
    v_rsp = (v_rsp) + (80);
    return result;
loc_00372404:
    result = MI_READ_PTE_LOCK_FREE(v_r13, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16), a3, a4);
    v_stack_p40 = result;
    if (condition_is_above_or_equal) goto loc_003721E2;
    result = MiInvalidPteConforms(result, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 16), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00372404;
    if (*(unsigned __int64 *)(v_rip + 11253838) == 0) goto loc_00372449;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0037263C;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11253838));
    a1 = (a1) & (result);
loc_00372449:
    a1 = (a1) >> (12);
    a1 = (a1) & (*(unsigned __int64 *)(v_rip + 11253838));
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 11253867))) goto loc_00372404;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00372404;
loc_0037249D:
    if (condition_is_below) goto loc_00372650;
    result = MI_READ_PTE_LOCK_FREE(v_r13, a2, a3, a4);
    if (result != v_stack_p40) goto loc_00372691;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00372749;
loc_003724E3:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 8)) | (*(unsigned __int64 *)(v_rip + 11262909));
    if (result != v_r13) goto loc_0037278E;
loc_003724FD:
    if (*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 == 0) goto loc_003721E5;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 34)) & (40)) != 0) goto loc_003723C0;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_003723C0;
    v_stack_p90 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 32))) != 0) goto loc_00372881;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 34)) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_00372881;
    a2 = 0;
    result = MiUnlinkPageFromListEx(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8, a2, a3, a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16)) & (-3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16) = result;
    result = MiInsertPageInList(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8, 8, a3, a4);
    goto loc_003723C0;
loc_00372571:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 8)) | (*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8);
    if (result != v_r13) goto loc_003723E9;
loc_00372590:
    if (result < v_r13) goto loc_00372670;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 34)) & (8)) != 0) goto loc_003723C0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16))) >> (1));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_00372764;
loc_003725BA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 144)) != ((unsigned int)(result))) goto loc_0037260E;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 32)))) != 1) goto loc_003723C0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) != 0) goto loc_0037260E;
    a2 = (v_r13) << (25);
    result = (*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiGetWsleContents(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8, a2, a3, a4);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_003723C0;
loc_0037260E:
    if ((((unsigned __int8)(v_stack_p40)) & (66)) != 0) goto loc_003722DB;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 34)) & (16)) != 0) goto loc_003722DB;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16))) >> (2));
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_003723C0;
    goto loc_003722DB;
loc_0037263C:
    a1 = (*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8) & (-17);
    goto loc_00372449;
loc_00372650:
    v_rbx = (unsigned int)((v_stack_p40) + 1);
    if (((*(unsigned int *)(v_rip + 12921940)) & ((unsigned int)(v_rbx))) == 0) goto loc_003727C6;
loc_0037265E:
loc_00372660:
    if (!sign_flag) goto loc_0037249D;
    goto loc_00372650;
loc_00372670:
    v_r15 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8 + 16)) + 1);
    if (((*(unsigned int *)(v_rip + 12921906)) & ((unsigned int)(v_r15))) == 0) goto loc_003727ED;
loc_00372680:
loc_00372682:
    if (!sign_flag) goto loc_00372590;
    goto loc_00372670;
loc_00372691:
    goto loc_00372404;
loc_003726A5:
    result = (a1) << (4);
    result = (result) + (40);
    result = (result) + (*(unsigned __int64 *)(a1 + 184));
    v_stack_p40 = result;
    if (((unsigned int)(a1)) >= 5) goto loc_003723BA;
    if ((*(unsigned int *)(result + 8)) == ((unsigned int)(v_r15))) goto loc_003723BA;
    result = MiReservePageFileSpaceForPage(v_stack_pA8, v_r13, 128, result);
    if (*(unsigned __int64 *)(v_rip + 11253136) == 0) goto loc_00372703;
    result = *(unsigned __int64 *)(v_rip + 11253136);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p40))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11253136));
        a2 = (*(unsigned __int64 *)(v_stack_p40)) & (result);
    }
    a2 = (a2) >> (32);
    a2 = (a2) + 1;
    result = MiUpdatePageFileHighInPte(*(unsigned __int64 *)(v_stack_p40), a2, v_stack_p40, result);
    *(unsigned __int64 *)(v_stack_p40) = result;
    if (condition_is_equal) goto loc_003727BC;
loc_00372720:
    v_rsi = (unsigned int)((3) | (16));
    goto loc_00372343;
loc_00372728:
    *(unsigned __int64 *)(v_rbx + 16) = a2 + 1;
    *(unsigned __int64 *)(v_stack_p40) = v_r13;
    *(unsigned __int64 *)(v_stack_p40 + 8) = v_r15;
    goto loc_00372390;
loc_0037273F:
    goto loc_003723BA;
loc_00372749:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(unsigned __int64 *)(v_rip + 11253838) + a2 * 8, a2, v_stack_p40, result);
    if (result == 0) goto loc_003721E2;
    goto loc_003724E3;
loc_00372764:
    result = (*(unsigned __int64 *)(result + 16)) & (-3);
    v_stack_p90 = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(result + 16) = result;
    goto loc_003725BA;
loc_00372781:
    goto loc_003723A6;
loc_0037278E:
    if (condition_is_below) goto loc_003724FD;
    v_stack_p20 = *(unsigned __int64 *)(result + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), v_r13, v_rbx);
loc_003727BC:
    goto loc_00372720;
loc_003727C6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12927724)))) & (64)) == 0) goto loc_0037265E;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), v_r13, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_0037265E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x411ULL), v_r13, v_rbx);
    goto loc_00372660;
loc_003727ED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12927685)))) & (64)) == 0) goto loc_00372680;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x411ULL), v_r13, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_00372680;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x411ULL), v_r13, v_rbx);
    goto loc_00372682;
loc_00372815:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) != 128) goto loc_00372853;
    v_rsi = (unsigned int)((v_rsi) | (4));
    goto loc_003722F7;
loc_0037282A:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(result + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0037289F;
loc_00372835:
    result = MiReleasePageFileInfo(v_stack_pA8, *(unsigned __int64 *)(result + 16), 1, v_rbx);
    goto loc_003723E0;
loc_00372853:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    if (((unsigned __int8)(result)) >= 64) goto loc_003722F7;
    v_rsi = (unsigned int)((v_rsi) | (8));
    goto loc_003722F7;
loc_0037286A:
    result = MiSanitizeShadowPxe(v_stack_pA8, v_stack_p38, 1, v_rbx);
    goto loc_003722BE;
loc_00372881:
    result = (*(unsigned __int64 *)(result + 16)) & (-3);
    *(unsigned __int64 *)(result + 16) = result;
    goto loc_003723C0;
loc_00372892:
    goto loc_003723BA;
loc_0037289F:
    result = (v_stack_p90) & (-5);
    v_stack_p90 = result;
    goto loc_00372835;
loc_003728C0:
    result = MiReleasePageFileInfo(v_stack_p38, result, 1, v_rbx);
    goto loc_003723E9;
}
```

## 5. (Beta) C Style

```c
int64_t MiOutSwapWorkingSetPte(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (80);
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x10);
    if (Arg3 != 0) goto loc_003723E9;
    local_r15 = 0;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x18);
    v_stack_p8 = 0;
loc_003721E2:
loc_003721E5:
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, Arg3, a4);
    v_stack_m58 = result;
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0037226F;
    result = (result) >> (12);
    result = (result) & (Arg2);
    if (result > (*(uint64_t *)(v_rip + 0xABBACF))) goto loc_003723E9;
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_003723E9;
    if (!sign_flag) goto loc_00372571;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) != 0) goto loc_00372343;
    goto loc_003723E9;
loc_0037226F:
    if (condition_is_below) goto loc_003723E9;
    if (condition_is_below) goto loc_00372404;
    result = (uint8_t)((*(uint64_t *)(result + arg1 * 8 + 0x28)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_003723E9;
    v_stack_p8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8);
    result = MiClearPageFileReservation(v_stack_m58, Arg2, Arg3, a4);
    v_stack_m50 = v_stack_m58;
    result = MiPteInShadowRange(Arg2, Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_0037286A;
loc_003722BE:
    *(uint64_t *)(arg2) = v_stack_m58;
    if (0 == 0) goto loc_003723CF;
    result = MiWritePteShadow(Arg2, v_stack_m58, Arg3, a4);
    goto loc_003723BA;
loc_003722DB:
    result = MiCaptureDirtyBitToPfn(result + Arg1 * 8, v_stack_m58, Arg3, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) != 64) goto loc_00372815;
loc_003722F7:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x20)) == -1) {
        Arg2 = *(uint64_t *)(result + arg1 * 8 + 0x10);
        Arg3 = 2;
        Arg1 = v_stack_p20;
        result = MiSetStoreVirtualPagefileValue(Arg1, Arg2, Arg3, a4);
        v_stack_m58 = result;
        *(uint64_t *)(result + arg1 * 8 + 0x10) = result;
    }
    local_rsi = (uint32_t)((0) & (0xFFFFFFFEULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x20)))) != -1) goto loc_003726A5;
loc_00372343:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10)) >= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x8))) goto loc_003723BA;
    local_r13 = (Arg2) << (25);
    result = (result) << (25);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10)) << (4);
    local_r13 = (local_r13) - (result);
    Arg3 = (Arg3) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8))));
    local_r13 = (local_r13) >> (16);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10) == 0) goto loc_00372728;
    result = (*(uint64_t *)(Arg3 - 0x10 + 0x8)) + (*(uint64_t *)(Arg3 - 0x10));
    if (result != local_r13) goto loc_00372728;
loc_00372390:
    if ((((uint8_t)(local_rsi)) & (2)) != 0) goto loc_00372781;
loc_003723A6:
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_0037273F;
    if ((((uint8_t)(local_rsi)) & (8)) != 0) goto loc_00372892;
loc_003723BA:
    if ((((uint8_t)(local_rsi)) & (1)) != 0) {
    }
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) != 0) goto loc_0037282A;
loc_003723E0:
    if (result != 0) goto loc_003728C0;
loc_003723E9:
    result = 0;
    local_rsp = (local_rsp) + (80);
    return result;
loc_00372404:
    result = MI_READ_PTE_LOCK_FREE(local_r13, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10), Arg3, a4);
    v_stack_p40 = result;
    if (condition_is_above_or_equal) goto loc_003721E2;
    result = MiInvalidPteConforms(result, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x10), Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00372404;
    if (*(uint64_t *)(v_rip + 0xABB84E) == 0) goto loc_00372449;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0037263C;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xABB84E));
    Arg1 = (Arg1) & (result);
loc_00372449:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (*(uint64_t *)(v_rip + 0xABB84E));
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xABB86B))) goto loc_00372404;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00372404;
loc_0037249D:
    if (condition_is_below) goto loc_00372650;
    result = MI_READ_PTE_LOCK_FREE(local_r13, Arg2, Arg3, a4);
    if (result != v_stack_p40) goto loc_00372691;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00372749;
loc_003724E3:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x8)) | (*(uint64_t *)(v_rip + 0xABDBBD));
    if (result != local_r13) goto loc_0037278E;
loc_003724FD:
    if (*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8 == 0) goto loc_003721E5;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x22)) & (40)) != 0) goto loc_003723C0;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_003723C0;
    v_stack_p90 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x20))) != 0) goto loc_00372881;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x22)) & (7));
    if (((uint8_t)(result)) != 3) goto loc_00372881;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8, Arg2, Arg3, a4);
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10)) & (-3);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10) = result;
    result = MiInsertPageInList(*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8, 8, Arg3, a4);
    goto loc_003723C0;
loc_00372571:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x8)) | (*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8);
    if (result != local_r13) goto loc_003723E9;
loc_00372590:
    if (result < local_r13) goto loc_00372670;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x22)) & (8)) != 0) goto loc_003723C0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10))) >> (1));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_00372764;
loc_003725BA:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x90)) != ((uint32_t)(result))) goto loc_0037260E;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x20)))) != 1) goto loc_003723C0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) != 0) goto loc_0037260E;
    Arg2 = (local_r13) << (25);
    result = (*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiGetWsleContents(*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8, Arg2, Arg3, a4);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 8) goto loc_003723C0;
loc_0037260E:
    if ((((uint8_t)(v_stack_p40)) & (66)) != 0) goto loc_003722DB;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x22)) & (16)) != 0) goto loc_003722DB;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10))) >> (2));
    if (((1) & ((uint8_t)(result))) == 0) goto loc_003723C0;
    goto loc_003722DB;
loc_0037263C:
    Arg1 = (*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8) & (-17);
    goto loc_00372449;
loc_00372650:
    local_rbx = (uint32_t)((v_stack_p40) + 1);
    if (((*(uint32_t *)(v_rip + 0xC52C54)) & ((uint32_t)(local_rbx))) == 0) goto loc_003727C6;
loc_0037265E:
loc_00372660:
    if (!sign_flag) goto loc_0037249D;
    goto loc_00372650;
loc_00372670:
    local_r15 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xABB84E) + arg2 * 8 + 0x10)) + 1);
    if (((*(uint32_t *)(v_rip + 0xC52C32)) & ((uint32_t)(local_r15))) == 0) goto loc_003727ED;
loc_00372680:
loc_00372682:
    if (!sign_flag) goto loc_00372590;
    goto loc_00372670;
loc_00372691:
    goto loc_00372404;
loc_003726A5:
    result = (Arg1) << (4);
    result = (result) + (40);
    result = (result) + (*(uint64_t *)(arg1 + 0xB8));
    v_stack_p40 = result;
    if (((uint32_t)(Arg1)) >= 5) goto loc_003723BA;
    if ((*(uint32_t *)(result + 0x8)) == ((uint32_t)(local_r15))) goto loc_003723BA;
    result = MiReservePageFileSpaceForPage(v_stack_pA8, local_r13, 128, result);
    if (*(uint64_t *)(v_rip + 0xABB590) == 0) goto loc_00372703;
    result = *(uint64_t *)(v_rip + 0xABB590);
    if ((((uint8_t)(*(uint64_t *)(v_stack_p40))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xABB590));
        Arg2 = (*(uint64_t *)(v_stack_p40)) & (result);
    }
    Arg2 = (Arg2) >> (32);
    Arg2 = (Arg2) + 1;
    result = MiUpdatePageFileHighInPte(*(uint64_t *)(v_stack_p40), Arg2, v_stack_p40, result);
    *(uint64_t *)(v_stack_p40) = result;
    if (condition_is_equal) goto loc_003727BC;
loc_00372720:
    local_rsi = (uint32_t)((3) | (16));
    goto loc_00372343;
loc_00372728:
    *(void **)(local_rbx + 0x10) = Arg2 + 1;
    *(uint64_t *)(v_stack_p40) = local_r13;
    *(uint64_t *)(v_stack_p40 + 0x8) = local_r15;
    goto loc_00372390;
loc_0037273F:
    goto loc_003723BA;
loc_00372749:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(uint64_t *)(v_rip + 0xABB84E) + Arg2 * 8, Arg2, v_stack_p40, result);
    if (result == 0) goto loc_003721E2;
    goto loc_003724E3;
loc_00372764:
    result = (*(uint64_t *)(result + 0x10)) & (-3);
    v_stack_p90 = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(result + 0x10) = result;
    goto loc_003725BA;
loc_00372781:
    goto loc_003723A6;
loc_0037278E:
    if (condition_is_below) goto loc_003724FD;
    v_stack_p20 = *(uint64_t *)(result + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), local_r13, local_rbx);
loc_003727BC:
    goto loc_00372720;
loc_003727C6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC542EC)))) & (64)) == 0) goto loc_0037265E;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), local_r13, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_0037265E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x411ULL), local_r13, local_rbx);
    goto loc_00372660;
loc_003727ED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC542C5)))) & (64)) == 0) goto loc_00372680;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x411ULL), local_r13, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_00372680;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x411ULL), local_r13, local_rbx);
    goto loc_00372682;
loc_00372815:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) != 128) goto loc_00372853;
    local_rsi = (uint32_t)((local_rsi) | (4));
    goto loc_003722F7;
loc_0037282A:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(result + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0037289F;
loc_00372835:
    result = MiReleasePageFileInfo(v_stack_pA8, *(uint64_t *)(result + 0x10), 1, local_rbx);
    goto loc_003723E0;
loc_00372853:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    if (((uint8_t)(result)) >= 64) goto loc_003722F7;
    local_rsi = (uint32_t)((local_rsi) | (8));
    goto loc_003722F7;
loc_0037286A:
    result = MiSanitizeShadowPxe(v_stack_pA8, v_stack_p38, 1, local_rbx);
    goto loc_003722BE;
loc_00372881:
    result = (*(uint64_t *)(result + 0x10)) & (-3);
    *(uint64_t *)(result + 0x10) = result;
    goto loc_003723C0;
loc_00372892:
    goto loc_003723BA;
loc_0037289F:
    result = (v_stack_p90) & (-5);
    v_stack_p90 = result;
    goto loc_00372835;
loc_003728C0:
    result = MiReleasePageFileInfo(v_stack_p38, result, 1, local_rbx);
    goto loc_003723E9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00372190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
